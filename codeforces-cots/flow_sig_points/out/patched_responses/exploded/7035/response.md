<think>
Okay, so I need to solve this problem where I have to find the minimal radius r such that every city is within r distance of at least one cellular tower. The input gives me the cities and towers in non-decreasing order. Hmm, let's think about how to approach this efficiently.

First, the key is that both arrays are sorted. That's a big hint. Sorting is expensive with large n and m (up to 1e5 each), but since they're already sorted, I can take advantage of that. For each city, I need to find the closest tower. The maximum of these minimal distances across all cities will be the answer r.

So, for each city coordinate a_i, find the closest tower coordinate in the towers array. The minimal possible r is the maximum of all these minimal distances.

How do I efficiently find the closest tower for each city? Since the towers are sorted, I can use binary search. For each city a_i, binary search the towers array to find the insertion point, then check the closest tower(s) around that position. For example, if the binary search returns index 'pos', the closest tower could be at pos or pos-1 (if pos is not zero). We need to compare the distances to both of those and take the minimum.

Wait, but what if the insertion point is at the end of the array? Then only the last tower is available. Similarly, if it's at the start, then the first tower is the only candidate.

So the steps would be:

1. Read the cities and towers arrays. They are already sorted, so no need to sort them.
2. For each city in the cities array:
   a. Perform a binary search on the towers array to find where the city would be inserted.
   b. Check the closest tower(s) around that position.
   c. Compute the minimal distance for this city.
3. The answer is the maximum of all these minimal distances.

But wait, binary search in Python is done via the bisect module. The bisect.bisect_left function returns the insertion point. Let's see. For a city at position x, bisect_left(towers, x) gives the first index where x can be inserted to keep the array sorted. So the closest towers would be at pos-1 and pos (if pos is within the array bounds). For example, if the insertion point is 0, then the closest tower is at 0. If it's m (the length of towers), then the closest is m-1. Otherwise, compare with pos-1 and pos.

So for each city, the minimal distance is the minimum of (towers[pos] - city) if pos < m, (city - towers[pos-1]) if pos >0, and take the minimum of those. But if pos is 0, then the only candidate is towers[0]. If pos is m, then the candidate is towers[m-1]. Otherwise, compare both adjacent.

Yes. So for each city, compute the closest tower and then take the maximum of all those distances.

But since the towers are sorted, this approach should work in O(n log m) time. Since n and m are up to 1e5, log m is around 20, so 1e5 * 20 = 2e6 operations. Which is acceptable for Python within the time constraints (3 seconds). Because 2e6 operations are manageable.

So the plan is:

- Read n and m.
- Read the cities array (already sorted).
- Read the towers array (already sorted).
- Initialize max_r to 0.
- For each city in cities:
   - Use bisect_left to find pos in towers.
   - Check the possible candidates (pos-1 and pos)
   - Calculate the minimal distance for this city.
   - Update max_r if this distance is larger than current max_r.
- Finally, output max_r.

But let's think about some edge cases.

Example 1:

Cities: [-2, 2, 4]
Towers: [-3, 0]

For city -2:

bisect_left on towers (sorted [-3, 0]) with x=-2. The insertion point is 1. Because -2 is between -3 and 0. So check index 0 and 1. Towers[0] is -3 (distance 1), towers[1] is 0 (distance 2). Minimal is 1. So for this city, r is 1. But wait, the example's answer is 4. Wait, wait, maybe I'm misunderstanding something.

Wait the first example's output is 4, but according to this approach, let's check each city:

City -2:

Towers are at -3 and 0. The closest tower is -3 (distance 1). So r for this city is 1.

City 2: Towers are at -3 (distance 5) and 0 (distance 2). So closest is 0, distance 2. So r is 2 here.

City 4: closest is 0 (distance 4) and there's no tower after 0. So distance is 4. So the maximum is 4. Which matches the example.

So the approach works here.

Another example:

Second input:

Cities: 1,5,10,14,17
Towers:4,11,15.

City 1: closest is 4 (distance 3)
City5: closest is4 (distance1)
City10: closest is11 (distance1)
City14: closest is11 (3) or 15 (1). So 1.
City17: closest is15 (distance2)
Maximum is 3. Which matches the example.

So the approach works.

What about a city that is exactly at a tower's position? Then the distance is zero, which is acceptable.

So the code needs to handle all these cases.

In Python, the bisect module has bisect_left. So for each city, the code can do something like:

import bisect

towers = sorted list (but input is already sorted, so just read it)

for city in cities:
    pos = bisect.bisect_left(towers, city)
    min_dist = infinity
    if pos < len(towers):
        min_dist = towers[pos] - city
    if pos > 0:
        min_dist = min(min_dist, city - towers[pos-1])
    max_r = max(max_r, min_dist)

But wait, in the code, for example, if pos is 0, then the first condition (pos < len) is true (if len is at least 1). So for pos 0, we check towers[0] - city. But since the array is sorted, and pos is insertion point 0, that means city is <= towers[0]. Wait no, bisect_left finds the insertion point such that all elements before are <= x. Wait no. Wait, bisect_left returns the first position where x can be inserted. So if the array has elements [a, b], and x is between a and b, then pos is the index where x would be inserted. So for example, in the first example, towers are [-3, 0], city is -2. bisect_left finds that -2 is between -3 and 0, so insertion point is 1. So the code checks towers[1] (0 - (-2) = 2) and towers[0] (-3 - (-2) = -1, but the absolute distance is 1). So the code takes the minimum of 1 and 2, which is 1. Correct.

Wait, but the code as I wrote earlier computes min_dist as (towers[pos] - city) when pos is valid, and (city - towers[pos-1]) when pos>0. But since the array is sorted, towers[pos] >= city (if pos is the insertion point from bisect_left). Because bisect_left returns the index where the element can be inserted to maintain the sorted order. So for example, in the first example, city is -2, insertion point is 1. towers[1] is 0, which is greater than -2. So towers[pos] - city is 2. The pos-1 is 0, towers[0] is -3. So city - towers[pos-1] is (-2) - (-3) = 1. So the minimal is 1. Correct.

But what if the insertion pos is 0. For example, a city at -4. Then pos is 0. So towers[0] is -3. city is -4. towers[pos] - city = (-3) - (-4) =1. But since the city is to the left of all towers, the distance is 1. But in this case, the correct minimal distance is 1.

Another example: city is 5, and towers are [4, 6]. bisect_left returns 1 (since 5 is between 4 and 6). So check towers[1] (6-5=1) and towers[0] (5-4=1). min is 1.

So the code as written should be correct.

So the code steps are:

Read n and m.

Read the cities list as integers, sorted. But the input is given in non-decreasing order.

Read the towers list as integers, also sorted.

Initialize max_r =0.

For each city in cities:

   pos = bisect.bisect_left(towers, city)

   current_min = some large value

   if pos < m:

       current_min = towers[pos] - city

   if pos >0:

       candidate = city - towers[pos-1]

       if candidate < current_min:

           current_min = candidate

   max_r = max(max_r, current_min)

At the end, output max_r.

But wait, the code is written with towers in a list. So in Python, the bisect module's bisect_left is O(log m) per city. For 1e5 cities, that's 1e5 * 20 steps, which is acceptable.

Yes. So this approach should work.

Now, considering the input sizes. The input lines can be large (1e5 numbers per line). So reading them with input().split() can be efficient enough, but in Python, using sys.stdin.readline() is faster. So to read the input faster, perhaps using sys.stdin.

So the code can be written as:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    cities = list(map(int, input_stream.readline().rstrip("\n").split()))
    towers = list(map(int, input_stream.readline().rstrip("\n").split()))

    max_r = 0

    for city in cities:
        pos = bisect.bisect_left(towers, city)
        current_min = float('inf')
        if pos < m:
            current_min = towers[pos] - city
        if pos > 0:
            current_min = min(current_min, city - towers[pos-1])
        max_r = max(max_r, current_min)

    print(max_r, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
1 5 10 14 17
4 11 15
""",
            "output": \
"""\
3
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

So the code works.

Another sample input:

5 3

1 5 10 14 17

4 11 15

Cities: [1,5,10,14,17]

Towers: [4,11,15]

Check each city:

1:

bisect_left in [4,11,15] for 1 returns 0. So pos=0. Check pos <3: 4-1=3. pos>0 is no. So current_min is3. max_r=3.

5:

bisect_left returns 0 (since 5 is inserted at 0? Wait no. Wait the towers are [4,11,15]. 5 is between 4 and 11. So bisect_left returns 1 (since 4 <5 <11). So pos=1. Check pos<3: 11-5=6. pos>0: 5-4=1. current_min is1. max_r remains3.

10:

bisect_left returns 1 (since 4<10<11). So check 11-10=1 and 10-4=6. current_min 1. max_r remains3.

14: bisect_left returns 2 (since 15 is the next after 11. 14 is between 11 and15. pos=2. Check 15-14=1 and 14-11=3. current_min 1. max_r still 3.

17: bisect_left returns 3 (since all elements are <17). So check pos>0: 17-15=2. current_min 2. max_r remains3. So output is3. Correct.

Yes, the code works for this case.

So the code seems correct. Now, the code uses O(n log m) time and O(1) space (other than the input storage). Since n and m are up to 1e5, this is acceptable.

But what about the data input? For reading 1e5 elements, the input may be large. Using split() can be efficient enough in Python, but for very large inputs, using sys.stdin may be faster. But in the problem statement, the user is instructed to read via input(), and output via print(). So in the code, using the standard input() and split() is acceptable.

But in Python, when the input is large, using input().split() can be slow. But given that the constraints allow up to 3 seconds, and for 1e5 elements, the code should run fine. Because in practice, the input lines are read as a single string and split into a list, which is manageable.

So the code should pass all test cases.
</think>

```python
import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx+1])
    idx +=2
    cities = list(map(int, data[idx:idx+n]))
    idx +=n
    towers = list(map(int, data[idx:idx+m]))
    max_r = 0
    for city in cities:
        pos = bisect.bisect_left(towers, city)
        current_min = float('inf')
        if pos < m:
            current_min = towers[pos] - city
        if pos > 0:
            current_min = min(current_min, city - towers[pos-1])
        if current_min > max_r:
            max_r = current_min
    print(max_r)

if __name__ == "__main__":
    main()
```
