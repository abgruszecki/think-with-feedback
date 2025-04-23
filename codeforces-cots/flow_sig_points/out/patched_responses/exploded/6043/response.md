<think>
Okay, let's see. So the problem is about selecting k pairs of intervals in a sequence of numbers. Each interval must be of length m, and they can't overlap. The goal is to maximize the sum of the elements in these intervals. Hmm.

First, let's understand the constraints. The maximum n is 5000, and m*k can be up to n. So for example, if m is 1 and k is 5000, then n has to be 5000. So we need an efficient algorithm that can handle up to 5000 elements.

The straightforward approach would be to compute all possible intervals of length m, then select k non-overlapping ones such that their sum is maximum. But how to do this efficiently?

Let me think. Since each interval is of length m, we can precompute the sum of each possible interval. Let's call this array 'sums', where sums[i] is the sum of elements from index i to i+m-1. Then the problem reduces to selecting k non-overlapping intervals (each of length m), such that the sum of their sums is maximum.

But how do we model the selection of these intervals with the non-overlapping condition? Because once we pick an interval starting at i, the next interval can't start before i + m. So it's similar to scheduling jobs where each job takes a certain time and you can't overlap. But here the jobs are fixed in position and have a fixed length m.

This seems like a dynamic programming problem. Let's think about dynamic programming. Let's define dp[i][j] as the maximum sum we can get by considering the first i elements and selecting j intervals. But how to transition between states?

Wait, but the intervals have to be of exactly length m. So for each position, if we decide to take an interval starting here, then we must jump m positions ahead. So the transitions would be: for each position i, if we take the interval starting here, then the next interval can't start before i + m. So the DP state could be based on the current position and the number of intervals selected so far.

Yes. Let's model it as follows:

We can precompute the sum of each possible interval. Then, for each position i in the array (where i can be the start of an interval), and for each count j (number of intervals selected so far up to j), we can track the maximum sum.

The DP state would be dp[j][i], representing the maximum sum when we have selected j intervals, and the last interval ends at i + m - 1 (or starts at i). Wait, maybe better to have the DP state as the current position and the number of intervals taken. So, dp[i][k] = maximum sum when we are at position i (i.e., next interval can start at i or later) and have taken k intervals so far.

Wait, maybe the DP state can be defined as dp[j][i], where j is the number of intervals selected, and i is the current position. The value is the maximum sum. For each state (j, i), we can decide to take an interval starting at i (if possible) and add its sum, then move to i + m. Or we can skip this position and move to i+1.

But how do we handle overlapping? If we take the interval starting at i, the next interval must start at i + m or later. So the transitions would be:

For each j in 1..k:
For each possible starting position i, if we take this interval, then the next possible starting positions are i + m.

So the DP approach might look like this:

Precompute all the sums.

Initialize dp[0][i] for all i as 0 (since taking 0 intervals, sum is 0).

Then, for each j from 1 to k:
   For each possible starting position i:
       if we can take an interval starting at i (i + m -1 <=n), then the maximum sum would be the sum of this interval plus the maximum sum from previous j-1 intervals where the last interval ends before i.

Wait, that's a bit tricky. Let's think: for j intervals, the current interval starts at i, which requires that the previous interval ended before i (i.e., the previous interval's start was <= i - m). So perhaps for each j, when considering starting at i, we need the maximum value from dp[j-1][0...i - m].

But if we precompute prefix maxima for the dp[j-1] array, then for each i, the maximum value we can get from the previous j-1 intervals up to i - m is accessible quickly.

Yes, that's a common approach in DP optimizations. So, for each j, we can compute a prefix maximum array of the dp[j-1], up to each possible i, and then for a current i, the maximum value is the maximum of dp[j-1][0...i - m].

Let me structure it step by step.

First, compute the sums of all possible intervals. Let's create an array s where s[i] is the sum of the interval starting at index i (0-based or 1-based? Need to clarify the input format.)

Wait, the input is given as p_1 to p_n. So the first element is p_1. So in Python, if the input is read as a list, say p, then p[0] is p_1. Wait, no, the problem says p_1, p_2, ..., p_n. So in the code, the first element would be p[0] if stored as a list in Python. So perhaps the intervals are 0-based in the code. Let me clarify.

Suppose the array is 0-based. So the interval starting at position i (0-based) includes elements i, i+1, ..., i+m-1. So the sum for this interval is sum(p[i:i+m]).

So first, compute all possible s[i] = sum(p[i:i+m]). The length of s is n - m + 1. Because the last possible interval starts at n - m.

Now, the problem is to select k intervals from this s array, such that they are non-overlapping. The non-overlapping condition here is that the next interval starts at or after the current interval's start + m. Because the current interval ends at i + m - 1. So the next interval must start at i + m or later.

So the problem reduces to selecting k elements from s (each with their starting index) such that each selected index is at least m higher than the previous one, and the sum of the selected s elements is maximized.

This is similar to the problem where you have to pick k elements with certain constraints, and maximize the sum. So dynamic programming is a good approach here.

The DP state can be dp[i][j], which represents the maximum sum we can get by selecting j intervals, with the last interval starting at or before index i.

Wait, perhaps not. Let's think of it as dp[j][i] = maximum sum when selecting j intervals, and the last interval starts at i. Then, for each j and i, we can look back to any i' where i' <= i - m, and take the maximum dp[j-1][i'] + s[i]. But this would require O(k * n^2) time, which would be too slow for n=5000 and k=5000 (but wait, m*k <= n, so k can be up to 5000/m. For m=1, k can be up to 5000, but then m*k=5000 which is allowed. So if k is 5000, then O(k * n^2) is 5000 * 5000^2 = 125 billion operations, which is way too much for 1 second. So this approach is not feasible.

So we need a way to optimize this. Let's think of the DP transitions again.

Another approach is to model the DP as follows: dp[j][i] is the maximum sum when we have selected j intervals, and the last interval starts at position i. Then, for j=1, dp[1][i] = s[i]. For j>1, dp[j][i] = s[i] + max(dp[j-1][i'] for i' <= i - m). The problem is that computing the max for each i and j is O(n), leading to O(k n^2) time.

But if we can precompute the maximum up to i - m for each j-1, then we can compute this in O(1) per i.

So here's the idea: for each j, we keep track of a prefix maximum array. For j-1, after we compute all dp[j-1][i], we create an array max_prev where max_prev[i] is the maximum value of dp[j-1][0..i]. Then, when computing dp[j][i], the max_prev[i - m] will give the maximum dp[j-1][i'] for i' <= i - m. So for each i, the transition becomes:

dp[j][i] = s[i] + (max_prev_prev[i - m] if i >= m else 0)

But wait, the max_prev_prev is the prefix maximum up to i - m. So for example, for j-th step, when processing i, the max_prev_prev is the maximum of all dp[j-1][i'] where i' <= i - m.

So this approach can reduce the time complexity.

Let's outline the steps:

1. Precompute s[i] for each i (sum of interval starting at i of length m).

2. Initialize a DP table. Since for each j, we only need the previous j-1 values, we can use a 2D array, but maybe optimize space by using two 1D arrays.

3. For each j from 1 to k:

   a. For j=1, dp[j][i] = s[i], but the intervals can't be overlapping. Wait, no, for j=1, you can pick any interval. So for j=1, the maximum possible sum is the maximum s[i], but in the DP approach, for j=1, all positions are allowed. Wait, no. Because for j=1, you can choose any interval, but the problem is to select exactly k intervals, each non-overlapping. Wait, no. For j=1, you just pick one interval, so the maximum sum is the maximum s[i]. But in the DP approach, the dp[j][i] for j=1 would be s[i], but when j=2, you need to find the maximum sum of two non-overlapping intervals.

Wait, perhaps the DP[j][i] represents the maximum sum when selecting j intervals, and the last interval is at i. Then, the maximum for j intervals would be the maximum over all dp[j][i] for all possible i. So for j=1, the maximum is the maximum s[i]. For j=2, the maximum is the maximum of s[i] + max_prev[i - m], where max_prev is the maximum of dp[1][0..i - m].

So the approach is as follows:

- Precompute s[i] for all possible i.

- Initialize an array prev_max, where prev_max[i] is the maximum value of dp[j-1][0..i].

- For each j from 1 to k:

   - Compute the current dp[j][i] as s[i] + (prev_max[i - m] if i >= m else 0) for each i.

   - Then compute the current prev_max array for the next j.

But how to manage the prev_max array?

Let me think. For j=1:

prev_max starts as the prefix maximum of s. For example, prev_max[i] = max(prev_max[i-1], s[i]).

Then for j=2:

for each i, dp[2][i] = s[i] + (prev_max[i - m] if i >= m else 0). Then, the new prev_max is the prefix maximum of these dp[2][i] values.

So, in code:

Compute s array.

Initialize prev_dp as s (for j=1).

Then, compute the prefix maximum array for prev_dp. So for each i, prev_max[i] = max(prev_max[i-1], prev_dp[i]).

Then, for j from 2 to k:

   For each i in 0 to len(s)-1:

       current_dp[i] = s[i]

       if i >= m:

           current_dp[i] += prev_max[i - m]

   Then, compute the new prev_max array as the prefix maximum of current_dp.

   Set prev_dp = current_dp.

Finally, the answer is the maximum value in prev_dp after k steps.

Wait, this seems plausible. Let's test this with the sample input.

Sample input 1:

5 2 1

1 2 3 4 5

So the array is [1,2,3,4,5]. The sum of each interval of length 2:

s[0] = 1+2=3

s[1] = 2+3=5

s[2] =3+4=7

s[3] =4+5=9

So s = [3,5,7,9]

k=1. So the maximum is 9. Which matches the sample output.

Sample input 2:

7 1 3

2 10 7 18 5 33 0

So m=1. Each interval is a single element. So s is [2,10,7,18,5,33,0]. We need to select 3 non-overlapping elements (since m=1, next interval must be after i+0). So the intervals can be any three elements as long as they are at least 1 apart. Wait, no. Because if m=1, then each interval is of length 1, so the next interval must start at i+1 or later. So the problem is to select three elements, no two of which are adjacent.

So the maximum sum is 10 + 18 +33 =61, which matches the sample.

In this case, the DP approach would work as follows.

For j=1: prev_dp is [2,10,7,18,5,33,0]. The maximum is 33.

prev_max is the prefix maximum: [2,10,10,18,18,33,33].

For j=2:

current_dp[i] = s[i] + prev_max[i - 1] if i >=1.

For example, i=0: can't add (i <1). So current_dp[0] =2.

i=1: s[1] =10 + prev_max[0] (2) → 12. So current_dp[1] =12.

i=2: s[2]=7 + prev_max[1] (10) →17.

i=3: 18 + prev_max[2] (10) →28.

i=4:5 + prev_max[3] (18) →23.

i=5:33 + prev_max[4] (18) →51.

i=6:0 + prev_max[5] (33) →33.

prev_max for j=2 is built as [2,12,17,28,28,51,51].

Then j=3:

current_dp[i] = s[i] + (prev_max[i-1] if i >=1).

For i=0: can't (j=3 requires 2 intervals before, which is impossible here), but current_dp[0] would be s[0] + prev_max[-1], but since i=0 <1, so just s[0] =2. But prev_max for j=2 is [2,12,17,28,28,51,51]. For i=0, i-1 is -1. So current_dp[0] =2 (s[0] + 0? Or maybe we need to check if i >=1 for j>=2.

Wait, for j steps, each step requires adding j intervals. So for j=3, the third interval must start after the second interval's start + m -1 (since m=1 here, the next interval must be after the previous one's end. So for m=1, each interval is length 1, and next must be at least 1 away. So for j=3, the current_dp[i] for j=3 is s[i] plus the maximum value of j=2's dp up to i-1 (since the previous interval must end before i-1 (if m=1). Wait, perhaps in code, for j=3, when adding the third interval, the previous two intervals must end before i (start at i - m? Wait, when m=1, the previous interval's start must be <= i-1.

So for j-th step, when considering i as the starting position, the previous j-1 intervals must have started at <= i - m. So in code, for current_dp[j][i] = s[i] + prev_max[i - m], where prev_max is the maximum up to i - m.

In the sample input 2, when j=3, for i=5 (33), i - m =4. prev_max[4] is 28 (from j=2's prev_max). So current_dp[5] =33 +28=61. Which is the correct answer.

So this approach works.

So the algorithm steps are:

1. Compute the s array.

2. Initialize prev_dp as the s array (for j=1).

3. Compute the prefix maximum array of prev_dp, called prev_max.

4. For each j from 2 to k:

   a. For each i in 0 to len(s)-1:

       if i >= (j-1)*m:  (Wait, no. Because for j intervals, each of m length, the first interval starts at s1, the next at s2 >= s1 +m, etc. So the earliest possible starting position for the j-th interval is (j-1)*m. But perhaps that's not necessary, as the code would take care of it.)

       current_dp[i] = s[i]

       if i >= m: current_dp[i] += prev_max[i - m]

       else: current_dp[i] = -infinity or 0? No, because if i < m, then it's impossible to have j intervals (since each interval takes m positions). Wait, for j intervals, the first interval starts at some a1, then a2 >=a1 +m, etc. So the minimum possible starting position for the j-th interval is (j-1)*m. So for j intervals, the starting positions must be >= (j-1)*m.

But in the code, when j=2, the i must be at least m, because the first interval's start can be up to i - m. So for i >= m, it's possible.

But when j is 3, and i is >= 2m, etc.

But in the code, when j=3, the current i must be >= (j-1)*m. Wait, no. Because the previous j-1 intervals could start at positions that leave room for the current i. For example, j=3, m=1, then the previous two intervals can be at positions 0 and 2, then the current can be at 4. So (j-1)*m = 2*1=2. i=4 >= 2, which is correct. So for j-th interval, the earliest possible i is (j-1)*m.

But in the code, the current_dp will automatically not have any valid values for i less than (j-1)*m. Because for j steps, each step adds at least m positions. So for j=2, the earliest i is m. For j=3, it's 2m, etc. So in the code, when building the current_dp, for i < (j-1)*m, current_dp[i] can be set to -infinity, but in practice, since the prev_max for i -m would be 0 when i < m (for j=2). Wait, when j=2 and i=1 (if m=1), then i -m =0. So for j=2, the code would allow i >= m (since m=1, i >=1). So when j=2, the code allows i >=1.

But how to handle the case when j is large enough that (j-1)*m > len(s)-1. Then, there are no possible intervals. So the answer would be 0 if k is possible, but according to the problem statement, it's guaranteed that m*k <=n. So there are enough intervals.

So the code can proceed as follows:

Compute the s array.

If k=0: sum is 0.

Else:

Initialize prev_dp as s.

Compute prev_max as the prefix maximum.

Then for each j from 2 to k:

   Create current_dp array of size len(s), initialized to 0.

   For each i in 0.. len(s)-1:

       if i >= m * (j-1):

           current_dp[i] = s[i]

           if i >= m:

               current_dp[i] += prev_max[i - m]

       else:

           current_dp[i] = -infinity (or not considered)

   Then compute prev_max as the prefix maximum for current_dp.

   prev_dp = current_dp.

But wait, in the code, for j=2, the previous j-1 steps have intervals that can start anywhere. Then, the code for j=2's current_dp[i] is s[i] + prev_max[i -m], where prev_max is from j=1's dp. But j=1's dp is allowed for any i, but j=2's intervals must start after the previous interval. So the code is correct.

But when building current_dp, for i < m, i -m is negative, so prev_max[i -m] would be out of bounds. So we need to handle that case.

So for i >= m:

current_dp[i] = s[i] + prev_max[i - m]

Else if i < m and j >1:

current_dp[i] = s[i] (but only if j=1). So for j>1, if i < m, then it's impossible to have a previous interval (since previous interval's start must be <= i -m, which is negative). So for j>1 and i <m, current_dp[i] is not possible, so we can set it to -infinity.

Wait, but in the code for j steps, when j=2, each current interval must have a previous interval. So for i <m, there is no way to have a previous interval. So in that case, current_dp[i] is s[i] (for j=2) but since i <m, there's no previous interval. So for j=2, i must be >=m, because the previous interval would start at i -m, but that's for the first interval. Wait, j=2 means that we have two intervals. The first interval must start at i1, the second at i2 >=i1 +m. So for the second interval (i2), the first interval can start at i2 -m (no, wait: if the second interval starts at i2, the first must end before i2. The first interval starts at i1 and ends at i1 +m -1. So i1 +m -1 < i2. So i2 >= i1 +m. So i1 <= i2 -m. So when j=2, the second interval starts at i2, and the first interval must start at <= i2 -m. So for i2 >=m, there exists possible i1 <=i2 -m. For i2 <m, there is no possible i1 (since i1 >=0 and i2 -m would be negative). So for j=2, current_dp[i2] can be non-zero only when i2 >=m.

So in code, when j>=2, for i in 0 to len(s)-1:

current_dp[i] = s[i] + (prev_max[i -m] if i >=m else 0)

But wait, for j=2, we need to have selected one interval before. So if i <m, then there's no previous interval, so j=2 is not possible, so current_dp[i] for j=2 and i <m should be invalid (i.e., -infinity). But in code, if i <m, then i -m is negative, so prev_max[i -m] is prev_max[-1], which is not allowed. So we need to handle that.

So the code can be:

for each i in 0.. len(s)-1:

   if i >= m:

       current_dp[i] = s[i] + prev_max[i -m]

   else:

       current_dp[i] = -infinity (since there's no way to have a previous interval)

But in Python, we can handle this by initializing prev_max with a -infinity for indices <0.

Wait, but in Python, accessing prev_max[i -m] when i -m <0 would be an invalid index. So perhaps in code, we need to compute the maximum up to i -m, but if i -m is negative, then it's 0.

Wait, maybe when i <m, the previous_max is 0. For example, in the first sample input, when j=1, the current_dp is s[i], and prev_max is the prefix maximum. Then, for j=2, when i <m, i -m is negative. So we can't have a previous interval. So for current_dp[i] to be valid, we must have a previous interval, which is not possible. So current_dp[i] is s[i] + 0 (no previous sum). But j=2 requires two intervals. So in this case, current_dp[i] for j=2 and i <m is invalid.

So for j>1, when i < m*(j-1), the current_dp[i] is invalid. So in code, we can precompute the earliest possible i for each j.

Alternatively, during the j-th iteration, for each i, if i >= (j-1)*m, then it's possible to have j intervals. Otherwise, it's not. So during the j-th iteration, we can ignore i < (j-1)*m.

But for code, perhaps it's better to compute all i and handle the i >= m case.

Wait, but how to compute prev_max[i -m] when i -m is negative?

We can set prev_max[0... len(prev_max)-1], and for any i -m <0, the value is 0.

So for j=2:

current_dp[i] = s[i] + (prev_max[i -m] if i >=m else 0)

But this would allow for j=2, current_dp[i] to be s[i] when i <m, which is invalid.

Wait, no. Because for j=2, we need to select two intervals. The current interval is the second one, so the first must be in 0..i -m. If i <m, then i -m is negative. So there is no possible first interval. So the current_dp[i] for i <m and j=2 should be invalid. So in code, for j >=2, we need to compute current_dp[i] as s[i] + (prev_max[i -m] if i >=m else -infinity).

But how to handle that in code?

Perhaps, the code can proceed as:

prev_max is the prefix maximum array of the previous DP array. For the j-th step:

current_dp[i] = s[i] + (prev_max[i -m] if i >=m else 0) if j ==1 else s[i] + (prev_max[i -m] if i >=m else -infinity)

Wait, no. For j=1, there is no previous interval, so current_dp[i] is just s[i]. For j>1, current_dp[i] is s[i] plus the maximum of the previous j-1 intervals' dp, which can only be added if there's a valid previous interval (i >=m).

But how to handle the j>1 case?

Alternative approach: For j >=1:

current_dp[i] = s[i] + (max_prev[i -m] if i >=m else 0) if j ==1 else s[i] + (max_prev[i -m] if i >=m else -infinity)

But in the code, for j>1, if i <m, then current_dp[i] is s[i] + (invalid), so it's not possible. So set current_dp[i] = -infinity in that case.

Wait, but for j=2, the first interval must have been taken in the first j-1 steps (i.e., j-1=1). The first interval could start anywhere. Then the second interval must start at i >= first interval's start +m. So for j=2, the second interval's start i must be >= m.

Because the first interval could start at 0 (m=2), then the next interval must start at >=0 +2 =2.

So for j=2, the current interval's start i must be >= m.

So for j=2, the code should only consider i >= m.

But in the code, when j=2, we can loop through all i, but for i <m, the current_dp[i] is invalid. So in the code:

current_dp[i] = s[i] + prev_max[i - m] if i >=m else -infinity.

But how to handle this in code.

Perhaps, during the j-th iteration, for each i:

if i >= m:

   current_dp[i] = s[i] + prev_max[i -m]

else:

   current_dp[i] = -infinity.

Then, after building current_dp for j steps, compute the new prev_max as the prefix maximum. But for j steps, the valid i's are those >= m*(j-1). So for j=2, the earliest possible i is m*1 = m. For j=3, earliest possible i is 2*m, etc.

But in code, the current_dp for j steps would have valid values starting from i >= (j-1)*m. So during the j-th iteration, when building the current_dp array, the code can loop through all i from (j-1)*m to len(s)-1.

This would save time, but how to compute (j-1)*m?

But the code can proceed by, for each j, loop over i from 0 to len(s)-1, but set current_dp[i] to s[i] + (prev_max[i -m] if i >=m else -infinity) for j>1.

But then, the prefix max would have to take into account the -infinity values.

Alternatively, perhaps in code, for each j>1, the current_dp[i] is computed as follows:

current_dp = [-inf] * len(s)

for i in range(len(s)):

    if i >= m:

        current_dp[i] = s[i] + prev_max[i - m]

    else:

        current_dp[i] = -inf

prev_max is then the prefix maximum of current_dp, but since for i <m, current_dp[i] is -inf, the prefix maximum will ignore those.

But in Python, how to handle -inf.

So the code would look like:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().rstrip("\n").split())

    p = list(map(int, input_stream.readline().rstrip("\n").split()))

    # Compute the s array

    s = []

    for i in range(n - m + 1):

        s.append(sum(p[i:i+m]))

    s_len = len(s)

    if k ==0:

        print(0, file=output_stream)

        sys.exit()

    # Initialize DP

    prev_dp = [0] * s_len

    for i in range(s_len):

        prev_dp[i] = s[i]

    prev_max = [0]*s_len

    prev_max[0] = prev_dp[0]

    for i in range(1, s_len):

        prev_max[i] = max(prev_max[i-1], prev_dp[i])

    for j in range(2, k+1):

        current_dp = [-float('inf')] * s_len

        for i in range(s_len):

            # For current j-th interval, can only start at i if there's j-1 intervals before

            # which requires that i >= m*(j-1)

            # but how to check this?

            # Alternatively, since j-th interval must have j-1 intervals before, each of length m.

            # So the earliest possible i for j-th interval is (j-1)*m.

            if i < m*(j-1):

                continue

            if i >= m:

                current_dp[i] = s[i] + prev_max[i -m]

            else:

                # i >=m*(j-1) but i <m: possible only if m=0, which is not allowed.

                # So this case can't happen.

                current_dp[i] = -float('inf')

        # Compute new prev_max

        new_prev_max = [-float('inf')] * s_len

        new_prev_max[0] = current_dp[0]

        for i in range(1, s_len):

            new_prev_max[i] = max(new_prev_max[i-1], current_dp[i])

        prev_max = new_prev_max

        prev_dp = current_dp

    print(max(prev_dp), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 1 3
2 10 7 18 5 33 0
""",
            "output": \
"""\
61
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

Another edge case: k=0, but according to constraints, k is at least 1. Wait, the problem statement says k is given as input. But according to the input constraints, m*k >=1? No, according to the constraints, (m×k) ≤n. But k can be zero? Let's check the problem statement. The problem says: "choose k pairs". So k can be zero? But the first sample has k=1. The input constraints are 1 ≤ (m ×k) ≤n ≤5000. Wait, the input constraints for m and k are (m ×k) ≤n, but the problem statement's sample has 2×1=2 ≤5. So k can be zero? Or no. Wait, the input constraints are (m ×k) ≤n. So if m=0, but according to the problem statement, m is part of the input. Wait, the problem statement's constraints are:

1 ≤ (m ×k) ≤n ≤5000.

Wait, no, the problem says:

Constraints:

Time limit per test: 1.0 seconds

Memory limit per test: 256.0 megabytes

Input Format:

The first line contains three integers n, m and k (1 ≤ (m ×k) ≤n ≤5000).

So m ×k must be at least 1. Which implies that m and k are at least 1. Because m and k are integers. So m >=1, k >=1, and m ×k >=1. So the code doesn't need to handle k=0.

Thus, in code, the case when k=0 is not needed.

So the code can proceed.

Now, the code in Python.

But in Python, for large n=5000, the sum of the intervals can be up to 5000 * 1e9 =5e12, which is within Python's integer range.

So the code can proceed as follows.

Another thing: when m=0, but according to the problem constraints, m ×k >=1, which implies m >=1.

Thus, the code can proceed.

Now, let's code this.

But wait, in code, when m=0, but the constraints ensure that m >=1. So no need to handle that.

So, the code:

Read n, m, k.

Read the array p.

Compute s as the sums of intervals of length m.

Compute s_len = len(s) = n -m +1.

Then, handle k steps.

But for m=0, but the code is correct because m is at least 1.

Now, code:

But in code, for j from 2 to k:

Loop over i from 0 to s_len-1.

But for i < m*(j-1), we skip (current_dp[i] is set to -inf).

But perhaps, in code, it's more efficient to loop i from m*(j-1) to s_len-1.

Thus, in code:

for j in range(2, k+1):

    current_dp = [-inf] * s_len

    min_i = m * (j-1)

    for i in range(min_i, s_len):

        if i >= m:

            current_dp[i] = s[i] + prev_max[i -m]

        else:

            current_dp[i] = -inf  # but since i >= min_i and j >=2, m >=1, min_i is m*(j-1) >= m*1= m. So when j >=2, i >= m, so this else case is never taken.

    # Compute prev_max for current_dp.

    new_prev_max = [ -inf ] * s_len

    new_prev_max[0] = current_dp[0]

    for i in range(1, s_len):

        new_prev_max[i] = max(new_prev_max[i-1], current_dp[i])

    prev_max = new_prev_max

This way, for each j, the loop over i starts from min_i = m*(j-1), which is the earliest possible i for j intervals.

Thus, the code is optimized.

Now, let's code this.

Final code:

Read the input.

Compute s as the sum of each interval.

Handle k steps.

Then, output the maximum of the last DP array.

So the code is:

import sys

n, m, k = map(int, sys.stdin.readline().split())

p = list(map(int, sys.stdin.readline().split()))

# Compute the sum array s

s = []

for i in range(n - m + 1):

    total = sum(p[i:i+m])

    s.append(total)

s_len = len(s)

if s_len ==0:  # this can't happen as per constraints m×k <=n

    print(0)

    sys.exit()

prev_max = [0] * s_len

prev_max[0] = s[0]

for i in range(1, s_len):

    prev_max[i] = max(prev_max[i-1], s[i])

for j in range(2, k+1):

    current_dp = [ -float('inf') ] * s_len

    min_i = m * (j-1)

    for i in range(min_i, s_len):

        if i >= m:

            current_val = s[i] + prev_max[i - m]

        else:

            current_val = -float('inf')  # this case is impossible since j>=2 and i >= m*(j-1) >= m*1 =m

        current_dp[i] = current_val

    # compute new_prev_max

    new_prev_max = [ -float('inf') ] * s_len

    new_prev_max[0] = current_dp[0]

    for i in range(1, s_len):

        if current_dp[i] > new_prev_max[i-1]:

            new_prev_max[i] = current_dp[i]

        else:

            new_prev_max[i] = new_prev_max[i-1]

    prev_max = new_prev_max

if k ==1:

    print(max(s))

else:

    print(max(prev_max))

Wait, but for k=1, the prev_max is the maximum of s. So the code can handle k=1 in the loop.

Wait, the initial prev_max is for j=1. Then, for j=2 to k, we compute current_dp and update prev_max. For k=1, the code skips the loop and outputs max(prev_max), which is the maximum of s.

So the code can be simplified.

But in the code above, when k ==1, the code prints max(s). Otherwise, after the loop, prints the max of the last prev_max.

But the code after the loop for j in 2..k, the prev_max is the prefix maximum array of the current_dp for j=k. So the maximum value is the last element of prev_max.

Wait, no. For example, in the sample input 2, after j=3, the prev_max is [ -inf, -inf, 19,35,35,61,61 ]. The maximum is 61.

But the code prints max(prev_max), which is 61.

Yes.

But when the code for k=3 is executed, the code enters the loop for j=2 and j=3. After j=3, prev_max is the prefix maxima of current_dp for j=3, which is the last step. So the maximum value is the last element of prev_max, but also could be the maximum of the current_dp array.

But the code prints max(prev_max), which is the same as the maximum of current_dp.

Alternatively, after the loop, the prev_max is the prefix maxima of the current_dp for j=k. So the maximum of current_dp is the last element of prev_max.

But to confirm, for example, current_dp for j=3 is [ -inf, -inf, 19,35,33,61,51]. The prev_max for this current_dp is [ -inf, -inf, 19,35,35,61,61]. The maximum of current_dp is 61, which is the last element of prev_max.

So the code can print the last element of prev_max.

But in the code as written, when k >=2, after the loop, the code prints max(prev_max). Which is the same as the last element of prev_max.

But in Python, the max(prev_max) would scan the entire array, which is O(n), but it's acceptable.

Alternatively, the code can track the maximum during the loop.

But for code simplicity, the current approach is acceptable.

So the code:

After computing the initial prev_max for j=1, which is the prefix maximum of s.

Then, for j from 2 to k:

   compute current_dp and new_prev_max.

   set prev_max = new_prev_max.

After all steps, the answer is the maximum of prev_max.

But when j=1, prev_max is the prefix maximum of s. So the maximum is the last element of prev_max.

Thus, the code can be written as:

After the loop, the answer is prev_max[-1].

But wait, in the first sample input, after j=1, prev_max is [3,5,7,9]. The maximum is 9, which is prev_max[-1].

For j=2, after processing, the answer is max(current_dp) = 9 (if possible). But wait, in the first sample, k=1, so the code outputs prev_max[-1], which is correct.

Thus, the code can be structured as:

after the loop, the answer is prev_max[-1].

So the code can be adjusted:

prev_max is initialized as the prefix maximum of s.

for j in 2 to k:

   compute current_dp and new_prev_max.

   set prev_max = new_prev_max.

print(prev_max[-1])

This will work.

Let me test this.

Sample input 2: after j=3, prev_max is [ -inf, -inf, 19,35,35,61,61]. prev_max[-1] is 61. Correct.

Sample input 1: prev_max after j=1 is [3,5,7,9]. prev_max[-1] is 9. Correct.

Another test case: n=4, m=2, k=2. p = [1,2,3,4].

s = [3,5,7].

prev_max for j=1 is [3,5,7].

j=2:

min_i = 2*(2-1) =2.

i ranges from 2 to 2.

i=2:

current_dp[2] =7 + prev_max[2-2=0] →7 +3=10.

prev_max becomes [3,5,10].

So prev_max[-1] is 10. Correct.

Thus, the code can be modified to print prev_max[-1].

So the code becomes:

import sys

n, m, k = map(int, sys.stdin.readline().split())

p = list(map(int, sys.stdin.readline().split()))

s = []
for i in range(n - m + 1):
    s.append(sum(p[i:i+m]))

s_len = len(s)

# Initialize prev_max for j=1
prev_max = [0] * s_len
prev_max[0] = s[0]
for i in range(1, s_len):
    prev_max[i] = max(prev_max[i-1], s[i])

if k ==1:
    print(prev_max[-1])
    sys.exit()

for j in range(2, k+1):
    current_dp = [-float('inf')] * s_len
    min_i = m * (j-1)
    for i in range(min_i, s_len):
        if i >= m:
            current_val = s[i] + prev_max[i - m]
        else:
            current_val = -float('inf')
        current_dp[i] = current_val
    # compute new_prev_max
    new_prev_max = [-float('inf')] * s_len
    new_prev_max[0] = current_dp[0]
    for i in range(1, s_len):
        new_prev_max[i] = max(new_prev_max[i-1], current_dp[i])
    prev_max = new_prev_max

print(prev_max[-1] if prev_max else 0)

This code should handle all cases.

Now, test the first sample:

Sample input1:

n=5, m=2, k=1.

s = [3,5,7,9].

prev_max is [3,5,7,9]. print prev_max[-1] →9. Correct.

Sample input2:

After j=3, prev_max's last element is 61. Correct.

Another test case with k=2:

n=4, m=2, k=2.

prev_max after j=2 is [3,5,10]. prev_max[-1] is 10. Correct.

Thus, the code should work.
</think>

```python
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    
    # Compute the sum of each m-length interval
    s = []
    for i in range(n - m + 1):
        s.append(sum(p[i:i+m]))
    s_len = len(s)
    
    if k == 0:
        print(0)
        return
    
    # Initialize prev_max for j=1 (k=1 case)
    prev_max = [0] * s_len
    prev_max[0] = s[0]
    for i in range(1, s_len):
        prev_max[i] = max(prev_max[i-1], s[i])
    
    if k == 1:
        print(prev_max[-1])
        return
    
    for j in range(2, k+1):
        current_dp = [-float('inf')] * s_len
        min_i = m * (j-1)
        for i in range(min_i, s_len):
            if i >= m:
                current_val = s[i] + prev_max[i - m]
            else:
                current_val = -float('inf')  # This case is impossible as min_i >= m for j >=2
            current_dp[i] = current_val
        
        # Compute new_prev_max for the current DP state
        new_prev_max = [-float('inf')] * s_len
        new_prev_max[0] = current_dp[0]
        for i in range(1, s_len):
            new_prev_max[i] = max(new_prev_max[i-1], current_dp[i])
        prev_max = new_prev_max
    
    print(prev_max[-1] if prev_max else 0)

if __name__ == "__main__":
    main()
```
