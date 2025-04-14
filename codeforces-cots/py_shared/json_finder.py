import sys
import regex as reg


thinks_end_re = reg.compile(r'</think>\n*', flags=reg.REVERSE)
fence_start_re = reg.compile(r'^```(.*)\n+', flags=reg.MULTILINE)
fence_end_re = reg.compile(r'^```($|\n+)', flags=reg.MULTILINE)


def clean_backtick_fences(string: str) -> str:
    # TODO use a regex
    string = string.removeprefix('```')
    string = string.removeprefix('json')
    string = string.removeprefix('\n')
    string = string.removesuffix('```')
    string = string.removesuffix('\n')
    return string


def find_final_backticked_block(
    response: str,
    offset: int | None = None,
    skip_thinks: bool = True,
    expect_thinks: bool = True, # just for warning/double-checking
) -> str | None:
    # early exit on valid input
    if offset == len(response):
        return None

    if offset is None and skip_thinks:
        if m := thinks_end_re.search(response):
            offset = m.end()
        else:
            if expect_thinks:
                print('No thinks end found!', file=sys.stderr)
            offset = 0

    # NOTE we just accumulate all the blocks b/c this is copypasta, clean up as needed
    results = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = fence_start_re.search(response, cur_idx)
    loop = True
    while loop:
        par = None
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
            par = clean_backtick_fences(par)
            results.append(par)

            # prepare for next par
            cur_idx = fence_end_match.end()
            cur_match = fence_start_re.search(response, cur_idx)
        else:
            loop = False
            cur_idx = cur_par_end = len(response)


    return results[-1] if results else None


def find_json(
    response: str,
    offset: int | None = None,
    skip_thinks: bool = True,
    expect_thinks: bool = True, # just for warning/double-checking
) -> str | None:
    """
    Finds the final backticked block in the response.

    By default skips the "think" section as an optimization.
    """

    return find_final_backticked_block(response, offset, skip_thinks, expect_thinks)
