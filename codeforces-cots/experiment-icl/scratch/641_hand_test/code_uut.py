def _print(*args, **kwargs):
    print(*args, **kwargs)

def main(in_stream, out_stream):
    input = in_stream.readline
    print = lambda s: _print(s, file=out_stream)

    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    print(' '.join(map(str, arr)))
