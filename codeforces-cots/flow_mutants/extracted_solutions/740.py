n, T = map(int, input().split())
bits = [[] for _ in range(101)]  # d ranges from 0 to 100

for _ in range(n):
    ti, qi = map(int, input().split())
    max_d = T - ti
    if max_d < 0:
        continue
    max_d = min(max_d, 100)
    for d in range(max_d + 1):
        bits[d].append(qi)

prefix = []
for d in range(101):
    bits[d].sort(reverse=True)
    curr = [0]
    s = 0
    for q in bits[d]:
        s += q
        curr.append(s)
    prefix.append(curr)

dp = {0: 0}
for d in range(100, -1, -1):
    new_dp = {}
    p = prefix[d]
    m = len(p) - 1
    for carry_in, sum_qi in dp.items():
        for t in range(0, m + 1):
            total = t + carry_in
            if d > 0:
                if total % 2 != 0:
                    continue
                new_carry = total // 2
                new_sum = sum_qi + p[t]
                if new_carry in new_dp:
                    new_dp[new_carry] = max(new_dp[new_carry], new_sum)
                else:
                    new_dp[new_carry] = new_sum
            else:
                if total != 1:
                    continue
                new_sum = sum_qi + p[t]
                if 0 in new_dp:
                    new_dp[0] = max(new_dp[0], new_sum)
                else:
                    new_dp[0] = new_sum
    dp = new_dp

print(dp.get(0, 0))