n, m = map(int, input().split())

a = list(map(int, input().split()))

if m <n:

    print(0)

else:

    from collections import Counter

    counts = Counter(a)

    max_d = m //n

    for d in range(max_d, 0, -1):

        total = 0

        for c in counts.values():

            total += c //d

            if total >=n:  # early exit

                break

        if total >=n:

            print(d)

            exit()

    print(0)