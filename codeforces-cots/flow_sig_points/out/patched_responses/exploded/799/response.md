<think>
Okay, let's see. The problem is about finding the maximum possible distance between the minimum and maximum elements in a permutation after exactly one swap. So the initial permutation has all elements from 1 to n. We need to swap exactly two elements to maximize the absolute difference between the positions of 1 and n.

Hmm. First, I need to find where the current minimum (1) and maximum (n) are located. Then, figure out the best way to swap such that after swapping, their positions are as far apart as possible.

Wait, but the swap could involve either moving the min to a position that's far from the current max, or moving the max to a position far from the current min, or maybe both. But since we can only do one swap, we have to decide which swap gives the maximum possible distance.

Let me think. The initial positions of min and max are known. Let's call min_pos and max_pos. The current distance is abs(min_pos - max_pos). Our goal is to perform a swap that maximizes this distance.

So, what options do we have?

Option 1: Swap the min with the element that is farthest to the right (so that the new min_pos is as far left as possible). Wait, no. Wait, if we swap min with the element at position 0 (assuming 1-based or 0-based?), wait, the positions here are 1-based? Because in the input examples, like the first sample:

Input is 5, array 4 5 1 3 2. So the positions are indices 0 to 4 (if 0-based). Then the 1 is at index 2 (third position) and max 5 is at index 1. Their distance is 1 (abs(2-1) =1). Then swapping 1 and 2 (values 1 and 2) moves 1 to position 4, so the new positions are max at 1 and min at 4. Distance 3, which is the maximum possible. So the output is 3.

So the positions here are 0-based. Or wait, in the first example, after swapping, the min is at position 4 (0-based?), which would make the distance 1 to 4 (positions of max and min) as 3. So in that case, the initial positions of min and max are 2 and 1, distance 1. After swapping, min is at 4, max remains at 1, distance 3.

So the positions in the array are 0-based. So when the problem says the distance is the absolute difference between their positions, that's 0-based.

So first, we need to find the positions of 1 and n in the array. Then, the initial distance is their positions' difference.

Then, we can perform any one swap. But which swap would maximize the distance?

The possible best options are:

1. Swap the current minimum (1) with the first or last element. So if the current minimum is somewhere in the middle, moving it to the leftmost or rightmost position would potentially maximize the distance. Similarly for the maximum (n).

But since we can only swap two elements, perhaps the best way is to see what possible swaps can move the min as far left or right as possible, or move the max as far left or right as possible. Alternatively, perhaps swapping the min with the leftmost element or the rightmost, and the same for the max. Then, for each possible swap candidate, compute the resulting distance.

Wait, but there's a lot of possible swaps. How can we efficiently check which swap gives the maximum possible distance?

But since n is up to 100, checking all possible swaps is feasible. Because there are n*(n-1)/2 possible swaps, which for n=100 is 4950 swaps. For each swap, we can compute the new positions of min and max. Then compute the maximum possible distance.

But wait, in the original array, the min and max are at certain positions. When we perform a swap, it's possible that the swap involves either the min, the max, or neither. For example:

- If we swap the min with some other element, then the new position of min is the position of that element. The max's position remains the same, unless the other element was the max.

- Similarly, if we swap the max with some other element.

- If we swap two elements that are not min or max, then the positions of min and max remain the same. So such a swap does not affect the distance. Therefore, the best possible swap must involve either the min, the max, or both.

So the key is that only swaps involving the min, the max, or both will affect the positions of min and max. So, any swap that doesn't involve either of them is irrelevant. So we can ignore those swaps because after the swap, the distance remains the same as before. However, the problem says we must perform exactly one swap. So even if the current distance is already maximum, we have to swap two elements. But in that case, swapping two elements that are not min or max will not change the distance. For example, in the third sample input:

6
6 5 4 3 2 1

The min is at position 5 (value 1) and the max is at position 0 (value 6). The distance is 5, which is maximum possible. So any swap between elements that are not min and max will leave the distance at 5, which is the same. So the answer is 5.

So, in that case, even though swapping two elements not involving min or max gives the same distance, but the problem requires us to swap once, so the answer is correct.

But in other cases, to find the maximum possible distance, we need to consider all possible swaps that could affect the min or max positions. So the possible swaps are:

1. Swap min with some element (could be max, or another element).

2. Swap max with some element (could be min, or another element).

3. Swap some element that is not min or max with another element (but this won't affect the distance).

So, to find the optimal swap, we need to consider all possible swaps where either min or max is involved, as well as the swap between min and max. But even swapping min and max would affect their positions.

So, the approach is:

1. Find the initial positions of min and max.

2. The initial distance is d_initial = abs(min_pos - max_pos).

3. Then, for all possible pairs (i,j) where i < j, simulate swapping the elements at positions i and j. For each swap, check if the positions of min or max have changed. Compute the new distance, and track the maximum possible.

But given that n is up to 100, the total number of possible swaps is 100*99/2 = 4950, which is manageable.

So, even though this is a brute-force approach, for n=100, it's acceptable. Because 4950 iterations are very fast.

So the steps for the solution would be:

- Read the array.

- Find the positions of min (which is 1) and max (which is n). Let's call them min_pos and max_pos.

- Compute the initial distance as abs(min_pos - max_pos).

- The maximum possible after swap can be up to n-1 (if they are at opposite ends). So we need to see if any swap can achieve that.

- For each possible i and j (i < j), swap the elements, then check where the min and max are. But wait, in the swapped array, after swapping a[i] and a[j], the new min and max positions could change.

Wait, but the min is 1 and the max is n. So in the array, after swapping, the new positions of 1 and n would be:

- If the swapped elements are a[i] and a[j], then:

If a[i] is 1, then after swap, the new position of 1 is j.

If a[j] is 1, then after swap, the new position of 1 is i.

Similarly for a[i] being n, then after swap, the position is j, etc.

But if neither a[i] nor a[j] is 1 or n, then the positions of 1 and n remain the same.

So for each swap (i,j), we can determine:

new_min_pos = if a[i] is 1: j; else if a[j] is 1: i; else: min_pos.

Similarly for new_max_pos: if a[i] is n: j; else if a[j] is n: i; else: max_pos.

Then compute the distance between new_min_pos and new_max_pos.

We can compute this without actually modifying the array. Because we can check what the swapped elements were.

So, the approach is:

For each possible swap (i, j):

- Check if either a[i] or a[j] is 1 or n.

- Then compute new positions of 1 and n after this swap.

- Compute the distance.

Track the maximum distance found.

After considering all possible swaps, return the maximum distance.

But how to efficiently compute new_min_pos and new_max_pos?

Let's think:

Original min_pos is where 1 is located.

Original max_pos is where n is located.

When we swap elements at i and j:

Case 1: The swap includes the current min (1):

If a[i] is 1, then after swap, the new min_pos is j.

If a[j] is 1, then after swap, the new min_pos is i.

Case 2: The swap includes the current max (n):

If a[i] is n, then after swap, the new max_pos is j.

If a[j] is n, then after swap, the new max_pos is i.

But also, if both elements are min and max. For example, swapping min and max (i=min_pos and j=max_pos), then after swap, min is at j (original max_pos) and max is at i (original min_pos). So their positions are swapped.

So, for each possible swap (i,j):

Check if a[i] is 1 or a[j] is 1. Then, the new min_pos is j (if a[i] was 1) or i (if a[j] was 1). Otherwise, the min_pos remains the same.

Similarly for the max.

So, the steps for each swap (i,j):

Compute new_min and new_max positions:

new_min = min_pos

if a[i] == 1:

    new_min = j

elif a[j] == 1:

    new_min = i

new_max = max_pos

if a[i] == n:

    new_max = j

elif a[j] == n:

    new_max = i

Then compute the distance as abs(new_min - new_max).

Compare this with the current maximum and update accordingly.

This way, we don't need to modify the array for each swap. We can compute the new positions directly based on the original array's elements.

So the algorithm would be:

Find initial min_pos and max_pos.

Initialize max_distance as the initial distance.

Then, iterate over all possible pairs i < j:

For each pair, compute new_min and new_max as described.

Calculate the new distance.

Update max_distance if the new distance is larger.

After checking all pairs, output the max_distance.

Yes, this approach works and is efficient.

So the steps in code:

Read n.

Read the array as a list.

Find min_pos and max_pos by searching for 1 and n.

Compute initial distance.

Initialize max_dist as this initial distance.

Iterate through all possible i and j (i < j):

Check if a[i] is 1, a[j] is 1, a[i] is n, a[j] is n.

Compute new_min and new_max based on those conditions.

Compute current_dist as abs(new_min - new_max).

If current_dist > max_dist, update max_dist.

After checking all pairs, output max_dist.

But wait, the problem says that we must perform exactly one swap. So even if the initial distance is the maximum possible, we have to perform a swap. For example, in the third sample input, the initial distance is 5 (positions 5 and 0, 0-based?), which for n=6 is 5, which is maximum possible. But the code will check all possible swaps. However, any swap not involving min or max will leave the new_min and new_max positions the same, so their distance remains 5. So the code will find that the maximum is 5, which is correct.

So the code would correctly handle all cases.

So in code:

In Python, first read n, then the list as a list of integers.

Find min_val = 1, max_val = n.

min_pos = a.index(1)

max_pos = a.index(n)

initial_dist = abs(min_pos - max_pos)

max_dist = initial_dist

Then, for i in range(n):

   for j in range(i+1, n):

       # check if swapping i and j affects min or max positions

       new_min = min_pos

       new_max = max_pos

       # check if 1 is being moved

       if a[i] == 1:

           new_min = j

       elif a[j] == 1:

           new_min = i

       # check if n is being moved

       if a[i] == n:

           new_max = j

       elif a[j] == n:

           new_max = i

       current_dist = abs(new_min - new_max)

       if current_dist > max_dist:

           max_dist = current_dist

So this code will check all possible swaps and compute the maximum possible distance.

Yes, that's correct.

So the code would handle all cases.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    min_pos = a.index(1)
    max_pos = a.index(n)
    max_dist = abs(min_pos - max_pos)

    for i in range(n):
        for j in range(i + 1, n):
            new_min = min_pos
            new_max = max_pos
            if a[i] == 1:
                new_min = j
            elif a[j] == 1:
                new_min = i
            if a[i] == n:
                new_max = j
            elif a[j] == n:
                new_max = i
            current_dist = abs(new_min - new_max)
            if current_dist > max_dist:
                max_dist = current_dist

    print(max_dist, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
1 6 5 3 4 7 2
""",
            "output": \
"""\
6
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    min_pos = a.index(1)
    max_pos = a.index(n)
    max_dist = abs(min_pos - max_pos)

    for i in range(n):
        for j in range(i + 1, n):
            new_min = min_pos
            new_max = max_pos
            if a[i] == 1:
                new_min = j
            elif a[j] == 1:
                new_min = i
            if a[i] == n:
                new_max = j
            elif a[j] == n:
                new_max = i
            current_dist = abs(new_min - new_max)
            if current_dist > max_dist:
                max_dist = current_dist

    print(max_dist, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
6 5 4 3 2 1
""",
            "output": \
"""\
5
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

Third sample:

Input array is [6,5,4,3,2,1]

n=6. min is 1 at position 5. max is 6 at position 0. initial distance is 5-0=5. The code checks all swaps. Any swap not involving min or max will leave new_min and new_max positions as 5 and 0, distance 5. The swap between 5 and 2 (elements 5 and 2) in positions 1 and 4 (values 5 and 2) won't affect the min and max positions. So the maximum remains 5. So output is 5.

So the code works.

Thus, the approach is correct. The code should be written in Python, considering 0-based indices.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
min_pos = a.index(1)
max_pos = a.index(n)
max_dist = abs(min_pos - max_pos)

for i in range(n):
    for j in range(i + 1, n):
        new_min = min_pos
        new_max = max_pos
        if a[i] == 1:
            new_min = j
        elif a[j] == 1:
            new_min = i
        if a[i] == n:
            new_max = j
        elif a[j] == n:
            new_max = i
        current_dist = abs(new_min - new_max)
        if current_dist > max_dist:
            max_dist = current_dist

print(max_dist)
```
