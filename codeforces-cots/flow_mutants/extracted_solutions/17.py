n = int(input())
x = list(map(int, input().split()))
x.sort()
piles = []
for s in x:
    found = False
    for i in range(len(piles)):
        if piles[i] <= s:
            piles[i] += 1
            found = True
            break
    if not found:
        piles.append(1)
print(len(piles))