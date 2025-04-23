<think>
Okay, let's try to figure out this problem. So, the problem is about frogs crossing a river using stones. Each stone can be used once, and frogs can jump up to l units. We need to find the maximum number of frogs that can cross the river.

Hmm, first, let's understand the setup. The river is w units wide. The frogs start on one bank (say position 0) and need to reach the other bank (position w). They can jump up to l units. So, each jump must be between 0 and l units. But they have to step on stones. The stones are at positions 1 to w-1. Each position i (from 1 to w-1) has a_i stones. Each stone can be used by only one frog. So once a stone is used, it's gone.

The question is, what's the maximum number of frogs that can cross, considering all the stones and the jumping constraints.

Let me think about the approach. The key is to model the path a frog takes and determine how many such paths are possible without overlapping stone usage.

Wait, but how do the frogs' paths work? Each frog must make a sequence of jumps where each jump is at most l units. So their path is a sequence of positions starting at 0, then x1, x2, ..., xn, where each consecutive position is at most l units apart, and the last position is >=w (but since the river's width is w, the last step would be to position w).

But the stones are only from 1 to w-1. So, the frog must jump from some position x to x + d where d <= l, and x + d can be the next stone. But since the stones are at positions up to w-1, the frog's last jump must be from some position y where y + d >= w, so that they reach the other bank.

Wait, but the frog's path must consist of stones. So for example, a frog could start at 0, jump to position a (which must be <= l), then from a to b where b -a <= l, and so on until the last jump. The last jump's starting position must be such that starting from there, the frog can jump to w (so the distance is w - starting_pos <= l).

So, the problem reduces to finding a set of stones such that for each frog's path, the stones are in order, each consecutive step is within l, and the last step can reach the other bank. And each stone in the path is used once.

But how do we model this optimally?

The brute force approach would be to model each possible path for each frog and subtract the stones used, but that's not feasible given the constraints (w up to 1e5). So we need a smarter approach.

Let's think about the bottleneck. For a frog to cross, their path must have stones in such a way that between any two consecutive stones in their path, the distance is at most l. Additionally, the first stone must be within l units of 0 (so position <= l), and the last stone must be within l units of w (so position >= w - l).

But perhaps the key insight here is that the maximum number of frogs that can cross is determined by the minimum sum of stones in any window of size l. Wait, that's similar to the sliding window approach used in some other problems. Let me think.

Each frog's path must have at least one stone in each of certain overlapping intervals. For example, the first jump must land in [1, l], the next jump must land in [current position + 1, current position + l], and so on. But this seems complicated.

Alternatively, the path of a frog can be represented as a series of positions where each consecutive step is at most l apart. However, considering all possible paths is not feasible. Instead, maybe the problem can be reduced to sliding windows where the sum of stones in each window of length l is considered. The minimum of these sums will be the maximum number of frogs possible.

Wait, let's think about this. For a frog to cross, it's necessary that for each position i in their path, there is a stone. But the path can vary. However, regardless of the path, each jump of a frog must land in some window of positions that are reachable from the previous position. The critical point is that the stones required for any possible path must cover all the windows of size l that overlap. Hmm, perhaps the maximum number of frogs is determined by the minimal sum of stones in any l-length window.

Wait, here's an alternative way to model it. Let's consider that for a frog to cross, they must step on at least one stone in each of certain ranges. For example, the first jump must land in the first l positions (1..l). Then, the next jump must be in a window of l positions starting from the first stone's position. But this seems too variable.

Alternatively, think of the problem as the frog needs to have stones in intervals such that each interval is of length l, and each interval is consecutive. For example, the first interval is [1..l], the next interval is [k+1 .. k+l], where k is the first stone. But this approach might not capture all possible paths, leading to a possible underestimation.

Wait, but maybe the minimal sum of stones in any window of l consecutive positions (overlapping or not) is the limiting factor. Because for any path a frog takes, it must step on at least one stone in each of the sliding windows of size l. For instance, if there's a window of l consecutive positions where the sum of stones is x, then x is the maximum number of frogs that can pass through that window. So the minimal x across all such windows would be the answer.

But how to model these windows correctly?

Let me think with the examples.

Take the first sample input:

10 5

0 0 1 0 2 0 0 1 0

The positions are 1-9. The stones are:

1: 0

2:0

3:1

4:0

5:2

6:0

7:0

8:1

9:0

The output is 3.

Looking for sliding windows of 5 consecutive positions. Wait, the windows would be:

1-5: 0+0+1+0+2=3

2-6:0+1+0+2+0=3

3-7:1+0+2+0+0=3

4-8:0+2+0+0+1=3

5-9:2+0+0+1+0=3

So all windows sum to 3, which matches the output.

Another sample:

Input:

10 3

1 1 1 1 2 1 1 1 1

Positions 1-9.

l is 3. So the windows are of size 3.

The output is 3.

Looking at the windows:

1-3: sum 1+1+1=3

2-4: 1+1+1=3

3-5:1+1+2=4

4-6:1+2+1=4

5-7:2+1+1=4

6-8:1+1+1=3

7-9:1+1+1=3

So the minimal sum here is 3, which matches the output.

So this seems to fit. So the approach is to compute the minimal sum of stones in any window of size l, but the way these windows are formed depends on the problem.

Wait, but why is this approach correct?

Because each frog must pass through each of these windows. For example, a frog's path must have at least one stone in each window of l consecutive positions. Because, if you consider any window of l positions, the frog's next jump must land within that window. Wait, maybe not. Let me think again.

Wait, the frog starts at 0. Their first jump can be up to l units, so they land in positions 1..l. Then, their next jump can be up to l units again. So the next stone must be within (current position) + 1 to (current position + l). So the stones they can use in the next step depend on their current position.

But this makes the possible stones vary, which complicates the problem. So, how to model this.

Alternatively, the approach of taking the minimal sum over all possible sliding windows of length l gives the correct answer. Let's see why. Each frog's path must choose one stone in each of some consecutive windows. For example, the first window is positions 1..l. Then, the next window could be positions (k+1)..(k+l), where k is the first stone's position. But this makes the windows variable per frog's path. However, the minimal sum in any consecutive l-length window (from 1 to w-1) would be a bottleneck. Because, regardless of how the frog chooses their path, there is a window of l consecutive positions that their path must include at least one stone from. The minimal sum of stones in such a window would limit the maximum number of frogs.

Wait, perhaps the correct way to model it is that the stones required for the frogs must be in such a way that any possible path requires taking a stone in some window. For example, the first l positions (1..l) must have enough stones for all frogs. Because each frog's first jump must land in this window. Similarly, the next l positions (2..l+1) must have enough stones for the frogs that have passed the first window. But this seems like overlapping and the sum in each consecutive window of l positions is the minimal.

Wait, maybe the problem can be reduced to the minimal sum of any sliding window of l consecutive stones. Because, for each frog to cross, their path must include at least one stone in each of certain windows. However, the sliding window approach ensures that the sum of each window must be >= the number of frogs, otherwise, that window would be the bottleneck.

For example, in the first sample, all windows of 5 stones sum to 3, so the maximum is 3. Which matches the answer. Similarly, the second sample's minimal window sum is 3.

So the algorithm is to compute the sum of every window of l consecutive stones in positions 1 to w-1. Then, the minimal sum among these windows is the answer.

But wait, why? Because each frog must step on at least one stone in each window of l consecutive positions. For example, the frog's path must have a stone in positions 1..l (the first window). Then, the next stone must be in positions (current position +1) to (current position +l). But since the current position is in 1..l, the next stone could be in (1+1)..(l + l). But the next stone could be anywhere up to l steps ahead, but that's not a fixed window. So this approach might not account for overlapping or variable-length windows.

But according to the examples, the sliding window approach works. So perhaps this is the correct approach.

Wait, maybe the answer is the minimum of the sum of every window of l consecutive stones. Because, any path must include at least one stone in each of l-length windows. Wait, no. For example, suppose l is 3. If a frog jumps from 0 to 3 (which is within l=3), then the next jump must be to a stone between 4 and 6 (since 3 +3 =6). Then, the next jump must be to between 7 and 9, etc. So each of these steps uses stones in windows of 3 positions (3,4,5,6...). However, the sliding window approach would consider all possible consecutive l-length windows, which may not align with the required steps. So how does this approach capture the minimal sum?

Alternatively, perhaps the minimal sum is the minimal of all windows that can be steps for the frogs. Let me think of it as the frogs can choose any possible path, but each step they take must land in a window of l stones. However, the overlapping of these windows is such that the minimal sum in any window of l consecutive stones will determine the maximum number of frogs. Because any frog's path must pass through some window of l consecutive stones, and the minimal such sum would be the limiting factor.

But how to model this.

Let's take another example. Suppose w=6, l=2. The stones are [1,0,0,2,3]. So the positions are 1 to 5.

The possible windows of size 2 are:

1-2: 1+0=1

2-3:0+0=0

3-4:0+2=2

4-5:2+3=5

The minimal sum is 0 (window 2-3). But according to the problem, how many frogs can cross?

Wait, in this case, the answer should be 0, because the window 2-3 has sum 0. So no frogs can cross. But let's see why.

A frog needs to jump from 0 to positions 1 or 2 (since l=2). But if it jumps to 1, then next jump can be up to 3. Suppose there's a stone at 4 (which has 2 stones) and 5 (3 stones). So the frog could go 0->1 (uses a stone here), then 1->3 (no stone?), but 3's a_i is 0. Wait, no. The stones in positions 3 and 4 are 0 and 2. So after position 1, the frog can jump up to 3. But positions 3 is 0 stones, so that's not possible. So the frog can't make that jump. Alternatively, if the frog jumps to position 2 (a_i=0). But there's no stone there, so that's impossible. So in this case, the answer is 0, which matches the minimal window sum of 0.

So that makes sense. So the sliding window approach seems to work here.

Another example: suppose w=5, l=2. Stones are [3,0,3]. So positions 1-3.

Windows of size 2:

1-2:3+0=3

2-3:0+3=3

So the minimal sum is 3. So the answer is 3. Let's see if that's possible.

Each frog must start in 1 or 2. Then next jump must be to 3 (since w=5, so the next jump from 3 can reach 5. So a path could be 0->1->3, or 0->2->3 (but a_2 is 0, so that's not possible). So each frog must use a stone at 1 or 3. The first jump is 0->1 (using a_1=3 stones). Then the next jump is from 1 to 3 (distance 2). So the stones at 3 are 3. So each frog uses one stone from position 1 and one from position 3. The total number of frogs is min(3,3) =3, which matches the window sum.

So this approach works.

Therefore, the correct approach is to compute the sum of every window of l consecutive stones (from position 1 to position w-1), and take the minimal sum. That minimal sum is the maximum number of frogs that can cross.

But wait, what about the last window? For example, in a river of width w and maximum jump l, the frog's last jump must be from a position >=w-l. Because, they can jump up to l units, so from position w-l, they can reach w. So the stones in positions (w-l) to (w-1) must be considered. But according to our current approach, the window is of size l. But the positions from w-l to w-1 are l positions (since (w-1) - (w-l) +1 = l). So the window that includes these positions would be considered. So, the approach automatically includes that.

Therefore, the algorithm is as follows:

Compute the sum of every window of l consecutive stones in positions 1 to w-1. The minimal sum of these windows is the answer.

This is efficient because the number of windows is (w-1 - l +1) = w - l. For w up to 1e5, this is manageable with O(w) time.

But how to compute these sums efficiently.

The sliding window technique can be used here. We can compute the sum of the first window (positions 1 to l). Then, for each subsequent window, subtract the leftmost element and add the next right element. This way, each window sum is computed in O(1) time after the first.

Yes, this is O(w) time, which is acceptable for w up to 1e5.

So the steps are:

1. Read w and l.

2. Read the array a of size w-1. (positions 1 to w-1).

3. Compute the sum of the first l elements (indices 0 to l-1 in the array, since a_1 is index 0, etc.)

Wait, wait. Let's clarify the indices. The input is a_1 to a_{w-1}, given as a list. So in Python, the list will be a list of w-1 elements, where a[0] is a_1, a[1] is a_2, and so on.

Wait, for example, the first sample input:

10 5

0 0 1 0 2 0 0 1 0

Which is 9 elements (since w is 10, w-1=9). The positions are 1-9.

So for l=5, the first window is positions 1-5 (indices 0-4 in the list). Then the next window is 2-6 (indices 1-5), etc. So yes, the sliding window approach works.

So in code:

sums = sum(a[i] for i in range(l))

min_sum = sums

for i in range(l, len(a)):

    sums += a[i] - a[i - l]

    if sums < min_sum:

        min_sum = sums

return min_sum

But len(a) is w-1. So the loop runs from i=l to len(a)-1. So the number of windows is (w-1 - l +1) = w - l.

Yes.

But wait, in the first example, len(a) is 9. l=5. The loop starts at i=5 (the next element after the initial window of 0-4). Then the sum is computed by adding a[5] and subtracting a[0], etc. Each iteration moves the window by one.

Yes.

Therefore, the code for this is straightforward.

Now, edge cases.

Case where l >= w-1. For example, w=5, l=4. So the entire stones are in a window of 4 positions. So sum of all stones.

But according to the problem statement, l < w. So l can be up to w-1.

Another edge case is when l=1. Then each window is of size 1, so the sum of each a_i is a_i itself. The minimal a_i is the answer.

Another case where some a_i in the middle are zero. For example, if there's a window where all a_i are zero, then the answer is zero.

So the code should handle all these cases.

Now, let's code this.

Read w and l from input. Then read the array a as a list of integers.

Compute the initial sum for the first window (elements 0 to l-1). Then slide the window, subtracting the leftmost element and adding the next element. Keep track of the minimum sum.

Return the minimum sum.

But wait, the windows are of length l. However, in the problem statement, the frog's path must start at 0 and reach the other bank. So the last window to consider is the one that includes positions (w - l) to (w-1). Because the frog must jump from there to the other bank, which is possible.

So the code must compute all the windows of length l in the array. Because each window's sum represents the maximum number of frogs that can pass through that window. The minimal sum among all such windows is the answer.

Yes.

So the code is as follows:

Read w and l.

a = list(map(int, input().split())).

If len(a) != w-1, that's a problem, but the input is given as per the problem statement.

Then, compute the initial sum of the first l elements.

But if the array's length is less than l? For example, when w-1 < l. But according to the constraints, l < w. So w-1 >= l is possible only when l < w. For example, w=3, l=2. Then the array has 2 elements, which is equal to l. So the window is the entire array. So sum all elements.

But if l is larger than the array's length? Wait, no. Because l < w. For example, w=5, l=4. Then the array has 4 elements (w-1=4). So l is 4. The window is 4 elements. Sum all.

But what about when the array's length is less than l? For example, w=2, l=1. Then the array has length 1. Which is equal to l=1. So window is the array. Sum is a[0].

So the code can handle that.

So code steps:

Read w, l.

Read a as list.

If the array's length is less than l, which can't happen because l < w implies that w-1 >= l only when w > l+1. For example, if w=5, l=3. Then w-1=4 >=3. But if w=3, l=2. Then array length is 2 (w-1=2), l=2. So the window is 2 elements.

So code:

sum_ = sum(a[0:l])

min_sum = sum_

for i in range(l, len(a)):

    sum_ += a[i] - a[i - l]

    if sum_ < min_sum:

        min_sum = sum_

print(min_sum)

Yes.

But wait, when len(a) is exactly l, then the loop runs for i from l to len(a)-1. len(a) is l, so len(a)-1 is l-1. The loop runs when i is in the range l <= i <= len(a)-1. But if len(a) is l, then the loop runs only if i is >= l and <= l-1, which is impossible. So the loop doesn't run, and min_sum is the initial sum.

Which is correct.

So this code works for all cases.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    w, l = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    window_sum = sum(a[:l])
    min_sum = window_sum
    for i in range(l, len(a)):
        window_sum += a[i] - a[i - l]
        if window_sum < min_sum:
            min_sum = window_sum
    print(min_sum, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 3
1 1 1 1 2 1 1 1 1
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

Second sample:

Input:

10 3

1 1 1 1 2 1 1 1 1

len(a) is 9. l=3.

sum initial is a[0]+a[1]+a[2] =1+1+1=3.

Then, i=3: sum +=a[3] -a[0] → 1+1+1+1 -1 → sum becomes 3+ (1-1)=3.

i=4: sum +=a[4] -a[1] → 2 -1 → sum +=1 → sum=4.

i=5: sum +=a[5]-a[2] →1-1=0 → sum remains4.

i=6: sum +=a[6]-a[3] →1-1=0 → sum remains4.

i=7: sum +=a[7] -a[4] →1-2= -1 → sum=4-1=3.

i=8: sum +=a[8] -a[5] →1-1=0 → sum remains3.

So during the loop, the sum varies. The min_sum is 3, which is the correct answer.

Thus, the code works.

Therefore, the correct approach is to compute the sliding window sum of size l and take the minimum. The code is straightforward and efficient.
</think>

```python
w, l = map(int, input().split())
a = list(map(int, input().split()))
window_sum = sum(a[:l])
min_sum = window_sum
for i in range(l, len(a)):
    window_sum += a[i] - a[i - l]
    if window_sum < min_sum:
        min_sum = window_sum
print(min_sum)
```
