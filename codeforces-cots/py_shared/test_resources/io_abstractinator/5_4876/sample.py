n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(n):
    total += abs(a[i] - (i+1))
print(total)