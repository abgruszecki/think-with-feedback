import re

from loguru import logger

from .py_parser import check_is_python


offset_rx = re.compile(r'^<think>\n?')
par_sep_rx = re.compile(r'\n\n+|(\n?</think>\n*)', re.MULTILINE)
fence_start_line_rx = re.compile(r'^```(.*)\n+', re.MULTILINE)
fence_end_line_rx = re.compile(r'^```($|\n+)', re.MULTILINE)
fence_rx = re.compile(r'```(.*)\n+')
has_input_rx = re.compile(r'input\(\)|stdin')
has_output_rx = re.compile(r'print\(|stdout')
leading_space_rx = re.compile(r'^\s+')
nonspace_char_rx = re.compile(r'\S')
# This can be used by other code, to find the end of the thinks.
thinks_end_rx = re.compile(r'\n*</think>\n*')

def looks_like_answer(code: str) -> bool:
    """
    Allows filtering the results of find_code_blocks.
    """
    return bool(
        has_input_rx.search(code) and
        has_output_rx.search(code)
    )


def clean_backtick_fences(string: str) -> str:
    offset = 0
    end = len(string)
    if m := leading_space_rx.search(string):
        offset = m.end()
    # .match only matches at the start of the string
    # (we can't just use .search with ^ because maybe pos!=0)
    if m := fence_rx.match(string, pos=offset):
        offset = m.end()
    # I wonder if this should be the /last/ match?
    if m := fence_end_line_rx.search(string, pos=offset):
        end = m.start()
    return string[offset:end]


def find_code_blocks(
    response: str,
    offset: int = 0,
    only_process_thinks: bool = True,
) -> tuple[list[tuple[str, int]], int]:
    results: list[tuple[str, int]] = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = par_sep_rx.search(response, cur_idx)
    last_par_was_code = False
    loop = True
    # next_match = None
    while loop:
        par = None
        # the start of the current "logical" code block,
        # which may be the start of a *previous* paragraph
        # if we're currently working through R1's newline-separated code block
        cur_log_block_start = cur_par_start
        # start of match is cur par's end
        # end of match is next par's start
        if cur_match and (cur_match.group(1) is None or not only_process_thinks):
            cur_par_end = cur_match.start()

            cur_idx = cur_match.end()
            cur_match = par_sep_rx.search(response, cur_idx)

            # if cur_match and cur_match.group(1) is not None:
            #     # next match is a mid-paragraph code block
            #     # just assume this means what we have so far is not code
            #     # TODO this jump logic should also set last_* variables
            #     cur_idx = cur_par_start = cur_match.end()
            #     fence_end_match = fence_end_re.search(response, cur_idx)
            #     continue

            par = response[cur_par_start:cur_par_end]
            # prepare for next par
            cur_par_start = cur_idx
        else:
            loop = False
            if cur_match:
                cur_par_end = cur_match.start()
                cur_idx = cur_match.end()
                par = response[cur_par_start:cur_par_end]
            else:
                # we set cur_idx, cur_par_end and
                # let the last iteration set other variables
                cur_idx = cur_par_end = len(response)

        found_code = False
        if par is not None:
            # Par should be non-empty, but right now it sometimes is.
            # TODO figure out why par is sometimes empty
            if m := nonspace_char_rx.search(par):
                whitespace_offset = m.start()
            else:
                whitespace_offset = 0

        if par and (
            # listing more keywords is unimportant: Python lines are usually short
            # and checking the len is a better heuristic.
            # OTOH checking for # can matter since sometimes R1 adds newlines
            # between each code line and the comment lines can be very long.
            par.startswith(('```', '#', 'import ', 'from '), whitespace_offset) or
            len(par) < 100 or
            '\n' in par
        ):
            par = clean_backtick_fences(par)
            if last_par_was_code:
                last_par_str, cur_log_block_start = results[-1]
                par = ''.join((last_par_str, '\n\n', par))

            if check_is_python(par)[0]:
                cur_res = (par, cur_log_block_start)
                if last_par_was_code:
                    results[-1] = cur_res
                else:
                    results.append(cur_res)
                found_code = True

        last_par_was_code = found_code

    return results, cur_idx


def find_final_answer_block(
    response: str,
    offset: int,
    answer_must_be_valid_python: bool = True,
) -> str | None:
    # NOTE this guy finds specifically fenced code blocks, it ignores inline code.
    # early exit on valid input
    if offset == len(response):
        return None

    # NOTE we just accumulate all the blocks b/c this is copypasta, clean up as needed
    results = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = fence_start_line_rx.search(response, cur_idx)
    loop = True
    while loop:
        if cur_match:
            cur_par_start = cur_match.end()
            fence_end_match = fence_end_line_rx.search(response, cur_match.end())
            if not fence_end_match:
                # we can't find any closing fences,
                # so we can't find any more answer blocks,
                # so we're done
                break

            cur_par_end = fence_end_match.start()

            par = response[cur_par_start:cur_par_end]

            # prepare for next par
            cur_idx = fence_end_match.end()
            cur_match = fence_start_line_rx.search(response, cur_idx)
        else:
            loop = False
            if cur_match:
                cur_par_end = cur_match.start()
                cur_idx = cur_match.end()
            else:
                cur_idx = cur_par_end = len(response)
            par = response[cur_par_start:cur_par_end]

        if (
            # TODO regex, this is very Schlemiel-like
            any(par.startswith(p) for p in ('```', 'import ', 'from ')) or
            len(par) < 100 or
            '\n' in par
        ):
            par = clean_backtick_fences(par)
            if not answer_must_be_valid_python or check_is_python(par)[0]:
                results.append(par)

    return results[-1] if results else None


def find_code(response: str) -> tuple[list[str], str | None]:
    offset = 0
    if m := offset_rx.search(response):
        offset = m.end()

    think_code_blocks, offset = find_code_blocks(response, offset)

    final_answer = find_final_answer_block(response, offset)

    return [r[0] for r in think_code_blocks], final_answer