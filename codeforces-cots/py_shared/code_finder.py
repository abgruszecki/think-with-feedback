import re

from .py_parser import check_is_python


offset_re = re.compile(r'^<think>\n?')
# par_sep_re = re.compile(r'\n\n+|\n?</think>\n*|[^\n]\n```(.*?)\n+', re.MULTILINE)
par_sep_re = re.compile(r'\n\n+|(\n?</think>\n*)', re.MULTILINE)
fence_start_re = re.compile(r'^```(.*)\n+', re.MULTILINE)
fence_end_re = re.compile(r'^```($|\n+)', re.MULTILINE)
nonspace_char_rx = re.compile(r'\S')


def clean_backtick_fences(string: str) -> str:
    # TODO use a regex
    string = string.removeprefix('```')
    string = string.removeprefix('python')
    string = string.removeprefix('\n')
    string = string.removesuffix('```')
    string = string.removesuffix('\n')
    return string


def find_code_blocks(
    response: str,
    offset: int = 0,
    only_process_thinks: bool = True,
) -> tuple[list[tuple[str, int]], int]:
    results: list[tuple[str, int]] = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = par_sep_re.search(response, cur_idx)
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
            cur_match = par_sep_re.search(response, cur_idx)

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
            # Par should be non-empty.
            m = nonspace_char_rx.search(par)
            assert m is not None
            whitespace_offset = m.start()

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
) -> str | None:
    # early exit on valid input
    if offset == len(response):
        return None

    # NOTE we just accumulate all the blocks b/c this is copypasta, clean up as needed
    results: list[tuple[str, int]] = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = fence_start_re.search(response, cur_idx)
    loop = True
    while loop:
        if cur_match:
            cur_par_start = cur_match.end()
            fence_end_match = fence_end_re.search(response, cur_match.end())
            if not fence_end_match:
                # we can't find any closing fences,
                # so we can't find any more answer blocks,
                # so we're done
                break

            cur_par_end = fence_end_match.start()

            par = response[cur_par_start:cur_par_end]

            # prepare for next par
            cur_idx = fence_end_match.end()
            cur_match = fence_start_re.search(response, cur_idx)
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
            if check_is_python(par)[0]:
                results.append(par)

    return results[-1] if results else None


def find_code(response: str) -> tuple[list[str], str | None]:
    offset = 0
    if m := offset_re.search(response):
        offset = m.end()

    think_code_blocks, offset = find_code_blocks(response, offset)

    final_answer = find_final_answer_block(response, offset)

    return [r[0] for r in think_code_blocks], final_answer