<think>
Okay, let's see. The problem is about finding for each city the minimum and maximum cost when sending a letter to another city. The cost is the absolute distance between the cities. Since all cities are on a line and sorted in ascending order, there must be an efficient way to compute these min and max values without checking all pairs, which would be O(n^2) and not feasible for n up to 1e5.

Hmm, the input is sorted. That's a big clue. So the cities are given in increasing order of their x-coordinates. For any city i, the maximum distance must be either the distance to the first city (the leftmost) or the last city (the rightmost), whichever is larger. Because the cities are sorted, the leftmost is the smallest and the rightmost is the largest. So for city i, maxi is max(x[i] - x[0], x[-1] - x[i]). That makes sense. For example, in the first sample input, the first city is at -5, the last at 7. For the city at -2 (second position), the max is max(-2 - (-5)=3, 7 - (-2)=9) → 9. Which matches the sample.

As for the minimum distance, for each city, except the first and last, the closest city would be either the next one or the previous one. For the first city, the closest is the next one. For the last city, the closest is the previous one. So for city i (where i is not the first or last), the minimum is min(x[i] - x[i-1], x[i+1] - x[i]). For the first city, the minimum is x[1] - x[0], and for the last, x[-1] - x[-2].

So the approach is to process each city in O(1) time, leading to O(n) time overall, which is acceptable for n up to 1e5.

So the steps are:

1. Read n and the list of x coordinates (which is sorted).
2. For each i in 0 to n-1:
   a. Compute the maximum as the maximum between (x[i] - x[0]) and (x[-1] - x[i]).
   b. Compute the minimum as follows:
      - if i is 0: x[1] - x[0]
      - if i is n-1: x[n-1] - x[n-2]
      - else: min(x[i] - x[i-1], x[i+1] - x[i])
3. Output the min and max for each city.

This should handle all cases efficiently.

Testing this logic against the sample inputs:

First sample input: 4 cities at -5, -2, 2, 7.

For the first city (i=0):
min is x[1]-x[0] = (-2) - (-5) = 3.
max is max(-5 - (-5) (0?), 7 - (-5) (12). So max is 12. So output 3 12. Which matches.

Second city (i=1):
min is min( (x[1]-x[0])=3, x[2]-x[1] =4 → 3. Max is max(-2 - (-5)=3, 7 - (-2)=9 →9. So 3 9. Which matches.

Third city (i=2):
min is min(2 - (-2) =4, 7-2=5 →4. Max is max(2 - (-5)=7, 7-2=5 →7. So 4 7. Correct.

Fourth city (i=3):
min is 7-2=5. Max is 7 - (-5) =12. So 5 12. Correct.

The second sample input has two cities. For each, the min and max are the same. Since there's only two cities, each's min and max is the distance between them, which is 2. So output is correct.

So the approach seems solid.

Now, coding this in Python. Since the input is already sorted, we don't need to sort it again. So steps:

Read n, then the list of x's. Then for each i, compute min and max as per the rules.

Edge cases:

- n=2: each city has min and max equal to the difference between them.
- Cities in order but with varying gaps. For example, a city in the middle with neighbors on both sides.

So code:

Read input, then loop over each i from 0 to n-1.

For the maximum, compute the difference with first and last.

For the minimum:

if i ==0: x[1]-x[0]

elif i ==n-1: x[i]-x[i-1]

else: min(x[i]-x[i-1], x[i+1]-x[i])

Yes.

Now, code this in Python.

But wait, in Python, for handling large n (up to 1e5), reading input efficiently is important. So using sys.stdin.readline might be better. But the problem says input must be read via input(), so perhaps that's okay. However, for 1e5 numbers, using split() and list comprehensions is efficient.

So code outline:

n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    if i ==0:
        mini = x[1] - x[0]
    elif i ==n-1:
        mini = x[i] - x[i-1]
    else:
        mini = min(x[i] - x[i-1], x[i+1] - x[i])
    maxi = max(x[i] - x[0], x[-1] - x[i])
    print(mini, maxi)

But wait, in the first sample, the first city's maxi is x[-1] - x[0], which is 7 - (-5) =12. For city 0, x[i] -x[0] is zero, but x[-1] -x[i] is 12. So the max is 12, which is correct.

Yes. So that code should work.

Testing the code with the first sample:

Input is 4, then -5 -2 2 7.

i=0:

mini = x[1]-x[0] →3.

maxi = max(0, 12) →12. So output 3 12.

i=1:

mini is min(3 (from x[1]-x[0]), 4 (x[2]-x[1])) →3.

maxi is max( (-2 - (-5) )=3, (7 - (-2))=9 →9. So output 3 9.

i=2:

mini is min(4 (x[2]-x[1]=4), 5 (x[3]-x[2]=5) →4.

maxi: x[2]-x[0] →2 - (-5)=7, x[-1]-x[2] →5. So max 7. Output 4 7.

i=3:

mini is x[3]-x[2]=5.

maxi: 7 - (-5) =12. Output 5 12. Correct.

Second sample: n=2. x[0]=-1, x[1]=1.

i=0:

mini is x[1]-x[0] →2.

maxi is max(0, 2) →2.

i=1:

mini is x[1]-x[0] →2.

maxi is max(2, 0) →2.

So output is 2 2 for both. Correct.

So the code works for these samples.

Now, what about the case when n is 1e5? The code is O(n), which is acceptable.

In terms of memory, storing the list x is O(n), which is acceptable since 1e5 elements take about 800KB (each int in Python is ~28 bytes, but for a list of 1e5 elements, it's manageable within 256MB).

So the code is correct and efficient.
</think>

```python
n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        mini = x[1] - x[0]
    elif i == n - 1:
        mini = x[i] - x[i-1]
    else:
        mini = min(x[i] - x[i-1], x[i+1] - x[i])
    maxi = max(x[i] - x[0], x[-1] - x[i])
    print(mini, maxi)
```