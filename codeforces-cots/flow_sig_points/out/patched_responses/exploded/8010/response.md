<think>
Okay, let's see the problem. So Zane wants to buy a house as close as possible to his crush's house, which is house m. The houses are in a straight line, each 10 meters apart. The goal is to find the minimum distance possible based on the houses he can afford.

First, the constraints. The maximum n is 100, which is small. So even a O(n) solution would work here, but we need to make sure we process each house correctly.

So the approach is: iterate through each house, check if it's affordable (a[i] <= k and a[i] is not zero because that's occupied). Then for each such house, calculate the distance from m. The distance between house i and m is |i - m| *10 meters. Then we take the minimum of these distances.

Wait, but how to process the houses. Let's think.

The steps would be:

1. Read n, m, k. Note that m is the girl's house, which is already occupied (a[m-1] is 0, since the input is 1-based to n). So we can ignore house m.

2. Iterate over each house from 1 to n (1-based index). For each house i (1-based), check if a[i-1] is not 0 (since 0 means occupied), and a[i-1] <=k. If so, compute the distance as |i - m| *10.

3. Among all valid houses, find the smallest distance.

So the steps are straightforward.

Now, what about the edge cases?

Like, when there are multiple houses at the same minimal distance. Then any of them would give the same minimal distance. So we just need the minimum possible.

Examples:

In the third sample input, the girl's house is 5, which is already 0, so he can't buy that. The affordable houses are 3, 4 (but a[3] is 0?), wait no:

Wait the input is:

10 5 100

The array is 1 0 1 0 0 0 0 0 1 1. So the houses are 1-based:

House 1: 1 (price 1, affordable)
House 2: 0 (occupied)
House 3: 1 (affordable)
House4: 0
House5:0 (girl's house)
House6:0
House7:0
House8:0
House9:1
House10:1.

But the girl is in house 5. The affordable houses are 1,3,9,10 (since their a[i] is <=100, which k is 100). The distances:

House1: (5-1) =4 → 40 meters.

House3: (5-3) →2 →20 meters. So that's better.

House9: (9-5) →4 →40.

House10: 5 →5 →50.

So the minimum is 20 meters. Which matches the sample.

So the approach seems correct.

Now, in code:

Read the three integers n, m, k. Then read the list a.

Initialize the minimum distance as a very large number.

Loop through each index i (1-based) from 1 to n:

If i == m: skip (since a[m-1] is 0, but the problem says it's given that the girl's house is occupied and a[m] is 0, so we can skip this house.

Else:

Check if a[i-1] is not 0, and a[i-1] <=k. If yes, compute the distance as abs(i - m) *10. Keep track of the minimum such distance.

At the end, output the minimum distance.

Wait, but in the second sample input:

7 3 50

The array is 62 0 0 0 99 33 22. The girl's house is 3 (a is 0), and the other houses. The available houses are the 0s? No, wait a[i] is 0 means occupied. Wait, in the input, the second line has a list of a1 to an, where ai=0 means occupied. So the houses that can be bought are those with ai>0 and ai <=k.

Wait, in the second sample input, the array is [62,0,0,0,99,33,22]. So:

Houses 2,3,4 are 0 (occupied). So the houses that can be bought are those with ai>0 and <=50. Let's check:

House1: 62 >50 → no.

House5:99>50 → no.

House6:33 <=50 → yes.

House7:22 <=50 → yes.

So the distances from m=3:

House6: 6-3 =3 →30 meters.

House7:7-3=4 →40. So minimal is 30.

So the code should pick that.

So in code, for each house i from 1 to n, except m (since it's occupied), check if a[i-1] >0 and <=k. Then compute the distance.

So the code steps:

Read n, m, k.

Read a as list of integers.

min_dist = something large like infinity.

for i in range(1, n+1):

    if i == m:

        continue  # can't buy

    price = a[i-1]

    if price ==0:

        continue  # occupied

    if price >k:

        continue  # can't afford

    distance = abs(i - m) *10

    if distance < min_dist:

        min_dist = distance

print(min_dist)

Yes. So this code should work.

Now, in Python, the code would look like this.

Testing the first sample:

Input:

5 1 20

0 27 32 21 19

So m=1. The houses:

i=1: skip.

i=2: a[1]=27>20 → no.

i=3: 32>20 → no.

i=4:21>20 → no.

i=5:19 <=20 → yes. distance is 4*10=40. So output is 40.

Which is correct.

So code seems correct.

Now, considering all possible cases. Since n is up to 100, this code is O(n), which is acceptable.

So this is the correct approach.
</think>

```python
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
min_dist = float('inf')
for i in range(1, n + 1):
    if i == m:
        continue
    price = a[i - 1]
    if price == 0 or price > k:
        continue
    distance = abs(i - m) * 10
    if distance < min_dist:
        min_dist = distance
print(min_dist)
```