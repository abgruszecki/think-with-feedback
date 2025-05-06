import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr + 1])
        ptr += 2
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        a.sort()
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        max_sum = 0
        for j in range(n):
            target = a[j] - 1
            i_pos = bisect.bisect_left(a, target, 0, j + 1)
            sum_total = prefix[j + 1] - prefix[i_pos]
            if sum_total <= m:
                current = sum_total
            else:
                low, high = 1, j - i_pos + 1
                best = 0
                while low <= high:
                    mid = (low + high) // 2
                    start = j + 1 - mid
                    s = prefix[j + 1] - prefix[start] if start >= i_pos else 0
                    if s > m:
                        high = mid - 1
                    else:
                        best = s
                        low = mid + 1
                current = best
            if current > max_sum:
                max_sum = current
        print(max_sum)

if __name__ == "__main__":
    main()