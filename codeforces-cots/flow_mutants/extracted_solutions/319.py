MOD = 998244353

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx +=1
        a = list(map(int, input[idx:idx+n]))
        idx +=n
        sum_total = sum(a)
        if sum_total == 0:
            print(0)
            continue
        count = 0
        left = 0
        current_sum = 0
        target = sum_total
        for right in range(n):
            current_sum += a[right]
            while left <= right and current_sum * 2 >= target:
                current_sum -= a[left]
                left +=1
            count += right - left + 1
        if sum_total > 0:
            count +=1
        print(count % MOD)

if __name__ == "__main__":
    main()