<think>
Okay, let's see. The problem is about finding the maximum possible minimal distance between two time periods selected from two different sets. Hmm. So Anton wants to choose one chess period and one programming period such that the distance between them is as large as possible. The distance here is defined as the minimal possible |i - j| where i is in the chess interval and j is in the programming interval. Oh right, and if the intervals overlap at all, the distance is zero.

So the first step is to figure out how to compute the distance between two intervals (a, b) and (c, d). Let's think about possible cases. 

Case 1: The intervals don't overlap. That can be either when the chess interval is entirely before the programming one (b < c) or the other way around (d < a). The distance in that case would be the difference between the start of the later interval and the end of the earlier one. For example, if chess ends at b and programming starts at c where b < c, then the minimal distance is c - b. Similarly, if programming ends at d and chess starts at a where d < a, then the distance is a - d.

Case 2: The intervals overlap. Then the minimal distance is zero. Because there's at least one point where they overlap, so you can pick i and j such that |i - j| is zero.

So the problem reduces to finding the maximum possible distance between two intervals from the two sets. But how do we compute this efficiently given the constraints of n and m up to 2e5 each?

If we naively check all possible pairs, that's 2e5 * 2e5 = 4e10 operations, which is way too slow. So we need a smarter approach.

The key here is to precompute some extremal values from the chess and programming intervals. Let's think about what contributes to the maximum possible distance.

For example, to get a maximum distance when chess is entirely before programming, we need the earliest programming start (c) minus the latest chess end (b). Because the maximum distance in this case is c - b. So for this scenario, we need the maximum (c - b) where chess interval ends at b and programming starts at c. The maximum is achieved when b is as large as possible (so latest end of chess) and c is as small as possible (earliest start of programming). Wait, no. Wait, if chess ends at a late time, and programming starts early, then the difference could be small. Wait, no. Wait, if chess is before programming: chess ends at b_max, programming starts at c_min. Then the distance would be c_min - b_max. But if that's positive, that's a candidate. Alternatively, if programming is before chess: programming ends at d_max, chess starts at a_min. Then the distance is a_min - d_max. So the maximum possible distance is the maximum between these two possibilities.

So the approach is:

1. Find the maximum b (end of chess intervals) and the minimum c (start of programming intervals). The distance for chess before programming is max(0, c_min - b_max).

2. Find the maximum d (end of programming intervals) and the minimum a (start of chess intervals). The distance for programming before chess is max(0, a_min - d_max).

The overall maximum distance is the maximum between these two values.

But wait, is that correct? Let's see.

Suppose all chess intervals are (1,5), (2,6), (2,3). So the maximum b is 6. Programming intervals are (2,4), (6,8). The minimum c is 2. Wait, then c_min - b_max is 2 - 6 = -4. So the max would be 0. But in the first example, the correct answer is 3, which comes from the chess interval (2,3) ending at 3, and programming interval (6,8) starting at 6. So 6 -3 =3. Hmm. So in that case, the programming start is 6. So why didn't our approach pick that?

Ah, because in the first example, the programming intervals are (2,4) and (6,8). So the minimum c (start) is 2, but for the chess intervals, the maximum end is 6. So c_min -b_max is 2-6 =-4. So that scenario's distance is zero. But the other scenario is when programming is after chess. So perhaps the code I thought of is missing something.

Wait, wait. Let's re-examine. For the chess intervals, to find the case where chess is before programming, the maximum possible distance would be (c - b) where c is the programming start and b is the chess end. So to maximize (c -b), we need the largest possible c -b. That's equivalent to finding the minimal possible b (so that when subtracted from c, we get a larger value) and the maximum possible c. Wait, no. Let's see: (c - b) is maximized when c is as large as possible and b as small as possible. Oh right! Because c is the start of programming. Wait, no: in the case where chess ends at b, and programming starts at c. So c must be after b. Then the distance is c -b. To maximize this, we want the largest possible c and the smallest possible b. Wait no, wait: for example, if chess ends at 3 (small b) and programming starts at 6 (large c), then c -b is 3, which is good. So the maximum is achieved when c is maximum and b is minimum. Wait, but that's not what the initial approach considered.

Ah, this is the mistake. The initial approach thought of taking the maximum chess end and the minimum programming start, but that's wrong. Because in the scenario where chess is before programming, the maximum distance would be (programming start - chess end) when that's positive. To maximize this value, we need programming start to be as large as possible and chess end as small as possible.

So the correct way to compute this scenario is:

max_c_start = maximum of all programming starts (c) in programming intervals.

min_b_end = minimum of all chess ends (r1_i) in chess intervals.

Then the distance for chess before programming is max(0, max_c_start - min_b_end).

Wait, wait, no. Wait, if the programming starts at c, and the chess ends at b. Then the distance is c -b, but only if c >=b. If c <b, then the intervals overlap, so distance is zero.

But in the case where chess is before programming, the maximum possible distance between the two intervals would be (c -b), and we need to find the maximum possible value of this across all possible pairs. So the maximum of (c -b) across all possible c (programming starts) and b (chess ends). But to get the maximum (c -b), we need the maximum c and the minimum b. Because for each possible pair (c_i, b_j), the maximum (c_i - b_j) is achieved when c_i is as large as possible and b_j as small as possible.

Ah, right! So for the chess before programming scenario, the maximum possible distance is max(0, (max_programming_start - min_chess_end)).

Similarly, for the programming before chess scenario, the maximum possible distance is max(0, (max_chess_start - min_programming_end)).

So the overall maximum is the maximum between these two values.

Wait, let's test this with the first example.

First example:

Chess intervals:

1 5 → ends at 5.

2 6 → ends at 6.

2 3 → ends at 3.

So min_chess_end is 3 (the smallest end is 3). The programming starts are 2 and 6. The max_programming_start is 6. So 6 -3 =3. So the distance is 3. Which matches the first example's answer.

So the initial approach was wrong. The correct way is to take the maximum programming start (c) and the minimum chess end (b) for the chess before programming case.

Similarly, for programming before chess: the programming's end is d. The chess's start is a. The distance is a -d. So to maximize this, we take the maximum a (chess start) and the minimum d (programming end). Wait, no. For programming before chess, the programming ends at d, and the chess starts at a. So the distance is a -d. To maximize this, we need a to be as large as possible and d as small as possible.

So for programming before chess:

max_chess_start = maximum of all chess starts (a) → in the first example, the chess starts are 1,2,2. So max is 2.

min_programming_end = minimum of all programming ends (d) → in programming intervals, ends are 4 and 8. Min is 4. So a -d is 2-4= -2. So the distance is 0. So the maximum for this scenario is 0.

So the overall maximum is max(3,0) =3, which is correct.

So the approach is:

Compute two possibilities:

1. Chess is before programming: distance is max(0, max_c_start - min_b_end), where max_c_start is the maximum of all l2_i (programming starts), and min_b_end is the minimum of all r1_i (chess ends).

2. Programming is before chess: distance is max(0, max_a_start - min_d_end), where max_a_start is the maximum of all l1_i (chess starts), and min_d_end is the minimum of all r2_i (programming ends).

Then the answer is the maximum of these two possibilities.

Wait, wait. Let's rephrase:

For scenario 1: chess ends before programming starts. So the distance is programming start (l2_i) minus chess end (r1_j). We want this value to be as large as possible. The maximum possible value for (l2_i - r1_j) is when l2_i is as large as possible and r1_j as small as possible. So among all programming intervals, take the maximum l2_i (since l2_i is the start of programming). Among all chess intervals, take the minimum r1_i (end of chess). Then compute (max_l2 - min_r1). If this is positive, that's a candidate.

For scenario 2: programming ends before chess starts. So the distance is chess start (l1_i) minus programming end (r2_j). To maximize this, take the maximum l1_i and the minimum r2_j. So (max_l1 - min_r2). Again, if positive.

The overall maximum is the maximum of scenario 1 and scenario 2.

Yes, that makes sense.

So the solution is to precompute:

max_l1 = maximum of all l1_i (chess starts)

min_r1 = minimum of all r1_i (chess ends)

max_l2 = maximum of all l2_i (programming starts)

min_r2 = minimum of all r2_i (programming ends)

Then the two candidates are:

candidate1 = max_l2 - min_r1

candidate2 = max_l1 - min_r2

The answer is the maximum between (candidate1, candidate2, 0). Because if both candidates are negative, then the maximum possible distance is 0 (since all pairs of intervals overlap).

So the plan is:

- Read all chess intervals and compute max_l1 and min_r1.

- Read all programming intervals and compute max_l2 and min_r2.

- Compute the two candidates as max(0, candidate1) and max(0, candidate2).

- The answer is the maximum of these two.

This approach is O(n + m) time, which is acceptable for n and m up to 2e5.

Let's test this logic against the examples.

First example:

Chess intervals:

1-5 → l1=1, r1=5

2-6 → l1=2, r1=6

2-3 → l1=2, r1=3

max_l1 is max(1,2,2) =2.

min_r1 is min(5,6,3) →3.

Programming intervals:

2-4 → l2=2, r2=4

6-8 → l2=6, r2=8

max_l2 is max(2,6) →6.

min_r2 is min(4,8) →4.

candidate1 =6 -3 →3. max(0,3) →3.

candidate2 = max_l1 (2) - min_r2 (4) →2-4 =-2 →0.

So maximum is 3. Correct.

Second example:

Chess intervals:

1-5, 2-6,3-7.

max_l1 is 3 (since l1 is 1,2,3).

min_r1 is 5 (since r1 is5,6,7 → min is5).

Programming intervals:

2-4 → l2=2, r2=4

1-4 →l2=1, r2=4.

max_l2 is max(2,1) →2.

min_r2 is min(4,4) →4.

candidate1: 2-5 =-3 →0.

candidate2:3 -4 →-1 →0.

So maximum is 0. Correct.

Another test case: suppose chess intervals have min_r1 = 10, and programming has max_l2=15. Then candidate1 is 5, candidate2 is max_l1 (say 20) - min_r2 (say 5) →15. So answer is 15.

So this approach works.

So the code needs to compute these four values.

Now, how to implement this efficiently in Python.

Read n chess intervals:

For each chess interval, track the maximum l1_i and minimum r1_i.

Similarly for m programming intervals: track the maximum l2_i and minimum r2_i.

So in code:

Read n.

Initialize max_l1 = -infinity

min_r1 = +infinity

For each of the n lines:

    read l, r.

    if l > max_l1: update max_l1.

    if r < min_r1: update min_r1.

Same for m programming intervals.

Compute candidate1 = max(0, max_l2 - min_r1)

candidate2 = max(0, max_l1 - min_r2)

answer = max(candidate1, candidate2)

Print answer.

This is straightforward and O(n+m) time. Which is acceptable for 2e5 entries.

Edge cases:

- All chess intervals are after programming. For example, all chess starts at 100, programming ends at 50. Then candidate2 would be 100 - 50_min (assuming min_r2 is 50). So 100-50=50, which is candidate2, and the answer is 50.

Another case: All programming intervals start after all chess end. Then candidate1 is the difference between the max programming start and min chess end.

Yes.

So the code should work.

Now, let's implement this.

But in Python, for 2e5 entries, reading via input() is possible but needs to be efficient. However, using the standard input method with split may be slow if not read properly.

So, perhaps the code should read all input at once.

But in practice, for Python, when the input is large, it's better to read via sys.stdin. So we can read the entire input at once and split into tokens.

But let's code this.

The code:

Read n.

Then read n lines, each with two integers l and r.

Compute max_l1 and min_r1.

Then read m.

Then read m lines, each with two integers l and r.

Compute max_l2 and min_r2.

Then compute the two candidates.

Take the max between them and print.

Implementing this.

Now, for reading the input.

In Python, the standard input can be read with sys.stdin.read().split() to get all tokens, then process them in order.

This is faster than reading line by line for large inputs.

So the code would be:

import sys

data = list(map(int, sys.stdin.read().split()))

pointer =0

n = data[pointer]

pointer +=1

max_l1 = -float('inf')

min_r1 = float('inf')

for _ in range(n):

    l = data[pointer]

    r = data[pointer+1]

    pointer +=2

    if l > max_l1:

        max_l1 = l

    if r < min_r1:

        min_r1 = r

m = data[pointer]

pointer +=1

max_l2 = -float('inf')

min_r2 = float('inf')

for _ in range(m):

    l = data[pointer]

    r = data[pointer+1]

    pointer +=2

    if l > max_l2:

        max_l2 = l

    if r < min_r2:

        min_r2 = r

candidate1 = max(0, max_l2 - min_r1)

candidate2 = max(0, max_l1 - min_r2)

ans = max(candidate1, candidate2)

print(ans)

Yes. That should work.

Let's test the first example:

Input:

3

1 5

2 6

2 3

2

2 4

6 8

Processing:

n=3. The first three intervals:

(1,5): max_l1 is 1. Then 2 comes in, max becomes 2. Then another 2. So max_l1 is 2.

min_r1: 5, then 6 (no change), then 3. So min_r1 is 3.

Then m=2. Programming intervals:

(2,4): l is 2. Then (6,8) l is6. So max_l2 is6.

r is4 and 8. min_r2 is4.

candidate1:6-3=3. candidate2:2-4= -2 →0. Ans 3.

Which matches.

Second example:

3

1 5

2 6

3 7

2

2 4

1 4

max_l1 for chess: 3.

min_r1:5.

max_l2 for programming:2.

min_r2:4.

candidate1:2-5= -3 →0.

candidate2:3-4= -1 →0.

ans 0.

Yes.

Another test case where chess is before programming:

Chess intervals:

[1,2], [3,4]

max_l1 is 3 (the start of the second interval).

min_r1 is 2 (the end of the first interval).

Programming intervals:

[5,6], [7,8]

max_l2 is7.

min_r2 is6.

candidate1:7-2=5.

candidate2:3-6= -3 →0.

ans 5.

Which is correct.

Another case where programming ends before chess starts.

Chess intervals:

[10,20], [15,25]

max_l1 is15.

min_r1 is20.

Programming intervals:

[5,8], [6,9]

max_l2 is6 (no, wait, no. The programming starts are 5 and 6. So max_l2 is 6. min_r2 is 8 (from first interval) and 9. min_r2 is 8.

candidate2:15 (max_l1) -8 (min_r2) →7.

So candidate2 is 7. So ans 7.

Which is correct. So the code would output 7.

Thus, the code seems correct.
</think>

```python
import sys

data = list(map(int, sys.stdin.read().split()))
ptr = 0

n = data[ptr]
ptr += 1

max_l1 = -float('inf')
min_r1 = float('inf')
for _ in range(n):
    l = data[ptr]
    r = data[ptr + 1]
    ptr += 2
    if l > max_l1:
        max_l1 = l
    if r < min_r1:
        min_r1 = r

m = data[ptr]
ptr += 1

max_l2 = -float('inf')
min_r2 = float('inf')
for _ in range(m):
    l = data[ptr]
    r = data[ptr + 1]
    ptr += 2
    if l > max_l2:
        max_l2 = l
    if r < min_r2:
        min_r2 = r

candidate1 = max(0, max_l2 - min_r1)
candidate2 = max(0, max_l1 - min_r2)
print(max(candidate1, candidate2))
```