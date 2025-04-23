<think>
Okay, let's tackle this problem. So the goal is to find the minimum number of swaps needed to arrange the soldiers such that the first is the maximum height and the last is the minimum height. And the swaps are between adjacent soldiers, each taking 1 second. Hmm.

First, I need to figure out which positions the max and min should be in. Wait, but the array can have multiple max or min elements. Like, maybe there are several soldiers with the maximum height. So the first element needs to be any of the max elements, and the last needs to be any of the min elements. But to minimize the swaps, we need to choose the optimal positions for these.

Wait, the problem is to make sure the first element is the maximum possible, and the last is the minimum possible. So the steps would be:

1. Find the maximum value in the array.
2. Find the minimum value in the array.
3. Find the earliest occurrence of the maximum value, because moving that to the first position would require the least swaps. Or wait, maybe the latest occurrence? Wait, no. For the maximum, we need to choose the leftmost occurrence to minimize the number of swaps needed to bring it to the front. Wait, no. Wait, if the maximum is already in the first position, no swaps needed. If it's at position i (0-based or 1-based?), then to bring it to the first position (index 0 if 0-based), it needs i swaps. So the earliest occurrence (the leftmost) is better because it's closest to the front. So for the maximum, we want the first occurrence of the maximum, so that the number of swaps to bring it to the front is minimal.

Wait, but the array can have multiple maxima. For example, if the array is [5, 5, 3, 2], then the first occurrence of 5 is index 0. So no swaps needed. But if the array is [3,5,5,2], then the first occurrence of 5 is index 1. So we need 1 swap to bring it to front.

Similarly for the minimum. We need to find the last occurrence of the minimum because that's the closest to the end. For example, if the array is [5, 1, 3, 1], the last occurrence of 1 is index 3. So bringing that to the end requires zero swaps. But if the array is [5,1,3,4,1], then the last occurrence is index 4. But if there's another 1 at index 1, the last occurrence is at 4. So moving that to the end (position n-1) would take (n-1 - 4) steps? Wait, no. Wait, if the element is at position i (0-based), and the end is position len(arr)-1, then the number of swaps needed is (len(arr)-1 - i). So for the minimum, the rightmost occurrence (last occurrence) would require the least swaps to get to the end.

But here's the catch: moving the maximum to the front and the minimum to the end. But when you move the maximum, it might affect the position of the minimum. For example, if the maximum is to the right of the minimum, then moving the maximum to the front would shift the minimum one position to the right. So the total swaps would be (pos_max) to move it to front, and (n-1 - pos_min_original) for the original pos_min. But if the original pos_min is before pos_max, then after moving the max to front, the pos_min shifts by +1. So the total would be pos_max + (n-1 - (pos_min_original + 1)).

So the problem is to find the positions of the max and min such that when you move them, you account for this overlap. Wait, that complicates things.

So the approach is:

Find the index of the first occurrence of the maximum (max_pos), because that's the earliest, which would need the least swaps to bring to front.

Find the index of the last occurrence of the minimum (min_pos), because that's the closest to the end, requiring the least swaps.

But if max_pos comes after min_pos, then when we swap the max to the front, the min's position shifts by +1. Because moving the max (which is after the min) to the front would shift the min's original position by one.

So the total swaps would be (max_pos) + (n-1 - min_pos) - 1. Because after moving the max, the min's position is now at min_pos_original + 1 (if the max was after it), so the number of swaps to get it to the end is (n-1 - (min_pos_original + 1)).

Wait, let's take an example.

Suppose the array is [5, 3, 1, 4, 2], and the max is 5 (at index 0), min is 1 (index 2). So max is already in position, min is at index 2. To get it to the end (index 4), requires 4-2=2 swaps. So total swaps 0 + 2 = 2.

Another example: the first sample input is 4 soldiers with heights [33,44,11,22]. The max is 44 at index 1. The min is 11 at index 2. Wait, but the sample output says that after swapping first and second (44 becomes first), then third and fourth (22 and 11 swapped) to get 44, 33, 22, 11. Wait, the min here is 11, which is at position 3 (original index 2). So the min's last occurrence is index 2. So in this case, the max is at index 1, the min at index 2. When we move the max to index 0 (needs 1 swap), the min's original index is 2. But after moving the max, the array becomes [44, 33, 11, 22]. Then the min is at index 2, but we need to swap the 11 and 22. So that's one swap (positions 2 and 3). So total swaps 1 +1=2. Which matches the sample.

But according to the formula: max_pos is 1 (original index). min_pos is 2 (original index). Since max_pos is before min_pos, so the total swaps would be (1) + (4-1 -2) = 1 + (3-2) = 2. Which is correct.

Another example: if max is at index i and min is at j < i. Then moving max to front takes i swaps, but this moves the min's position from j to j+1. So to get min to the end, we need (n-1 - (j+1)) swaps. So total is i + (n-1 - (j+1)).

But if i < j, then moving the max first doesn't affect the min's position (since the max is before the min). So the total is i + (n-1 - j).

So the formula is:

if max_pos < min_pos: total = max_pos + (n-1 - min_pos)

else: total = max_pos + (n-1 - min_pos) -1 

Because when the max is after the min, moving it to front shifts the min's position by 1 to the right.

Wait, let's see. Suppose the array is:

Indices: 0 1 2 3

Values: 1 5 3 1

max is 5 at index 1. min is 1 at index 0 and 3. The last occurrence of min is 3. So max_pos is 1, min_pos is 3. So max is before min. So total swaps is 1 (moving max to front) + (3 (n-1 is 3) -3) = 1 +0=1. But after moving max to front, the array becomes 5,1,3,1. The min is already at the end. So correct.

Another example where max is after min.

Original array: 3, 1, 5, 4, 2. So max is 5 at index 2. min is 1 at index 1. But the last occurrence of min is 1. So to move max to front: 2 swaps. But when we move it, the array becomes 5,3,1,4,2. Now the min is at index 2, which was originally 1, but after moving the max (which was at 2) to front, all elements from 0 to 1 are shifted right. Wait no. Let's think again.

Original array: [3,1,5,4,2]. max is at index 2. To move it to index 0, each swap shifts it left by one. So first swap indices 2 and 1: [3,5,1,4,2]. Then swap indices 0 and 1: [5,3,1,4,2]. So it took 2 swaps. Now the min is 1 at index 2. The last occurrence of min was originally at index 1, but after moving the max, the min's position shifted. Wait, no. Wait the original array is 3,1,5,4,2. So the min is 1 at index 1. The last occurrence of the min is index 1 because there's another min (2) but maybe not. Wait, in this example, the min is 1. The last occurrence of 1 is index 1. Then after moving the max (5) to index 0, the array becomes 5,3,1,4,2. The min is still 1 at index 2. So to move that to the end (index 4), requires 4-2=2 swaps. So total swaps is 2 (max) + 2 (min) =4.

But according to the formula: since max_pos (2) is > min_pos (1), then total is 2 + (4 -1) - (1+1) = 2 + 3-2=3? Wait, maybe my formula is wrong.

Wait in the case where max_pos is after min_pos, the formula would be:

max_pos (2) steps to bring it to front. But when we do that, the min_pos (originally 1) moves to 1 + (if the max was after it, and we move the max past the min, then the min's position would have been shifted to the right by one each time the max passes it. So if the max was at index 2, and the min is at index 1. Moving the max to the front requires two swaps. The first swap (indices 1 and 2) moves the max to index 1, but the min is at index 1? Wait no. Wait the initial array is [3,1,5,4,2]. Max is 5 at index 2. So when moving it to front:

Step 1: swap 5 and 1 (indices 2 and 1) → [3,5,1,4,2]. The min (1) was at index 1, now it's at index 2.

Step 2: swap 5 and 3 (indices 1 and 0) → [5,3,1,4,2]. The min is now at index 2.

So after moving the max, the original min's position (1) has been shifted to 2. So now, to move the min (1) to the end (index 4), we need 4-2=2 swaps.

So total swaps is 2 (max) + 2 (min) =4. But according to the formula, when max_pos (2) is > min_pos (1), the formula would be:

max_pos + (n-1 - min_pos) -1 → 2 + (4 -1) -1 → 2 +3-1=4. Which matches.

So the correct formula is:

if the max is to the left of the min, then the total is (max_pos) + (n-1 - min_pos)

else, (max_pos) + (n-1 - min_pos) -1.

So the steps to compute the answer are:

1. Find the maximum value in the array.

2. Find the leftmost occurrence of the maximum (earliest index) → this gives the minimal steps to move to front.

3. Find the minimum value in the array.

4. Find the rightmost occurrence of the minimum (latest index) → this gives the minimal steps to move to end.

5. Calculate the sum of steps to move the max to front (max_pos) and steps to move the min to end (n-1 - min_pos).

6. However, if the original max_pos is after the original min_pos, then when moving the max, the min's position increases by 1, so we subtract 1 from the total.

So the code steps:

Read n, read the list.

Find max_val = max(a)

min_val = min(a)

max_pos = first index where a[i] == max_val

min_pos = last index where a[i] == min_val

if max_pos < min_pos:

    answer = max_pos + (n-1 - min_pos)

else:

    answer = max_pos + (n-1 - min_pos) -1

So how to implement this in Python?

In Python, to find the first occurrence of max_val, we can loop from the start until we find the first element equal to max_val.

For the last occurrence of min_val, loop from the end until we find the first (from the end) element equal to min_val.

For example:

a = [10, 10, 58, 31, 63, 40, 76]

max_val is 76, first occurrence at index 6.

min_val is 10. Last occurrence is index 1 (since 0 and 1 are 10s). So max_pos is 6, min_pos is 1. Since 6>1, so answer is 6 + (7-1 -1) -1 → 6 + (5) -1 →10. Which matches the second sample.

Yes.

So code steps:

Read n.

Read list a as integers.

max_val = max(a)

min_val = min(a)

max_pos = a.index(max_val)

for min_pos, loop from the end backwards to find the first occurrence of min_val.

In Python, to get the last occurrence of min_val:

min_pos = len(a) - 1 - a[::-1].index(min_val)

Because reversing the list and finding the first occurrence of min_val gives the last occurrence in the original list.

But wait:

For example, a = [1,2,3,2,1]. min_val is 1. reversed list is [1,2,3,2,1]. index(1) is 0 → original index is len(a)-1 - 0 =4. Which is correct.

Yes.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    max_val = max(a)

    min_val = min(a)

    max_pos = a.index(max_val)

    min_pos = len(a) -1 - a[::-1].index(min_val)

    if max_pos < min_pos:

        res = max_pos + (n-1 - min_pos)

    else:

        res = max_pos + (n-1 - min_pos) -1

    print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
10 10 58 31 63 40 76
""",
            "output": \
"""\
10
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

Sample 2:

7

10 10 58 31 63 40 76 → reversed is [76,40,63,31,58,10,10]. Looking for min_val 10. reversed list's index is 5 (since reversed list starts with 76, then 40, 63, 31,58,10 (index5?), wait wait:

Original array is [10,10,58,31,63,40,76]. Reversed is [76,40,63,31,58,10,10]. So the reversed list is in order of 76,40,63,31,58,10,10. So the first occurrence of 10 in reversed list is at index 5. So len(a)-1 -5 =6-5=1. So min_pos is 1. max_pos is 6. 6>1 → res=6 + (6-1) -1 →6+5-1=10. Correct.

Another test case where max is after min:

Example:

5

3 1 5 4 2 → max is 5 at index 2. min is 1 at index 1 (last occurrence is 1). So max_pos (2) > min_pos (1). So res=2 + (4-1) -1 →2 +3-1=4. Which matches the earlier example.

So the code seems correct.

This approach is O(n) time and O(1) space (since the list is processed in linear time). For n up to 100, which is way within the constraints, this is optimal. No need for any other data structures. The code is straightforward and efficient.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_val = max(a)
min_val = min(a)
max_pos = a.index(max_val)
min_pos = len(a) - 1 - a[::-1].index(min_val)
if max_pos < min_pos:
    print(max_pos + (n - 1 - min_pos))
else:
    print(max_pos + (n - 1 - min_pos) - 1)
```
