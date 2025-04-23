import sys

def main():
    n, k, q = map(int, sys.stdin.readline().split())
    max_temp = 200000
    diff = [0] * (max_temp + 2)  # 1-based to 200001

    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        diff[l] += 1
        if r + 1 <= max_temp:
            diff[r + 1] -= 1
        else:
            # r is 200000, so r+1 is 200001, which is within diff's size (index up to 200001)
            diff[r + 1] -= 1

    # Compute counts for each temperature
    counts = [0] * (max_temp + 1)  # 1-based to 200000
    current = 0
    for i in range(1, max_temp + 1):
        current += diff[i]
        counts[i] = current

    # Compute prefix sums of admissible temperatures
    prefix = [0] * (max_temp + 1)
    current_sum = 0
    for i in range(1, max_temp + 1):
        if counts[i] >= k:
            current_sum += 1
        prefix[i] = current_sum

    # Process queries
    for _ in range(q):
        a, b = map(int, sys.stdin.readline().split())
        res = prefix[b] - (prefix[a - 1] if a > 1 else 0)
        print(res)

if __name__ == "__main__":
    main()