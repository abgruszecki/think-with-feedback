def _print(*args, **kwargs):
    print(*args, **kwargs)

def main(in_stream, out_stream):
    input = in_stream.readline
    print = lambda s: _print(s, file=out_stream)

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        total = sum(a)
        print(0 if total % n == 0 else 1)
