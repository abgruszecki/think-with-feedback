import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    seen = set()
    left = 0
    for i in range(n-1, -1, -1):
        if a[i] in seen:
            left = max(left, i+1)
        else:
            seen.add(a[i])
    print(left)
