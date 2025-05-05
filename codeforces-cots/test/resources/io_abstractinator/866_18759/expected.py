import sys


def main(input_stream, output_stream):
    t = int(input_stream.readline())
    for _ in range(t):
        n = int(input_stream.readline())
        a = list(map(int, input_stream.readline().split()))
        seen = set()
        left = 0
        for i in range(n-1, -1, -1):
            if a[i] in seen:
                left = max(left, i+1)
            else:
                seen.add(a[i])
        print(left, file=output_stream)

