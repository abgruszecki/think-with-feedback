<think>
Okay, let's try to figure out this problem. The problem statement says that for each student i, we need to find the minimum number of students before or at i that need to fail so that the sum of the chosen students' times plus t_i is <= M. And we have to do this for each i independently.

Hmm. So for each i-th student, we want to select a subset of students from 1 to i (excluding those who are failed) such that the sum of their t's (including the i-th) is <= M. But the subset must include the i-th student. The goal is to minimize the number of students removed (i.e., maximize the number kept, but the sum must be under M).

Wait, right. The minimal number of students to fail is equivalent to the maximum possible number of students we can keep (including i) such that the sum of their t's plus t_i is <= M. Wait, no. Wait, the i-th student has to be kept. So for each i, we need to select a subset S of the first i students, which includes i, such that the sum of t_j for j in S is <= M. We need to maximize the size of S, which would minimize the number of students removed (since the number removed is (i - 1) - (k - 1) where k is the number of students kept before i, because i must be kept). Wait, the total students from 1 to i is i. If we keep k students (including i), then the number of students removed is i - k. But since the problem requires that the i-th student must pass, we have to include him. So for each i, we need to choose a subset of the first i students that includes i, sum of their t's <= M. Then the minimal number of students to fail is i - the size of the largest such subset. Because the size of the subset is the number of students that are kept (including i). So the number of students to remove is (i) - size_of_subset (since total students up to i is i, and the subset is size s, so the removed is i - s). Wait, but the subset includes i, so the kept students are s, and the removed is (i) - s. But for each i, the answer is the minimal number of students that need to fail so that the sum of their times (including i) is <= M.

So the approach for each i is to select a subset of the first i students (including i) such that their sum of t's is <= M. We need to select as large a subset as possible (so that the number of students to remove is minimized). For each i, the answer is (number of students in the first i) minus the maximum possible size of such a subset.

So for each i, the problem reduces to: among the first i students (with i-th included), what's the maximum number of students we can include (must include i) such that their total sum is <= M. Then the answer for i is (i - max_size).

But how to compute this efficiently?

Let's think for each i. The i-th student is included. Then, from the first (i-1) students, we need to choose as many as possible (let's say k) such that the sum of their t's plus t_i is <= M. So the maximum k is (the maximum number of students from 1..i-1 that can be taken, along with their t's, such that their sum plus t_i <= M). Then the total number of students kept is k + 1 (the i-th plus those k). So the answer is (i - (k+1)) = i-1 -k.

But how to find this k?

The problem is similar to a knapsack problem. For each i-1 elements, select a subset of maximum size where the sum is <= (M - t_i). Because the sum of selected t's must be <= (M - t_i). And we want the maximum possible size.

Ah, right. So for each i, we can compute S_i = M - t_i. Then, from the first i-1 students, select a subset with maximum possible size such that their sum <= S_i. The answer for i is (i-1 - k), where k is the maximum size possible. If even taking all the first i-1 students sum to more than S_i, then we need to remove some. But how?

But for each i, the time required for this approach could vary. Given that n is up to 100, but even if we do this for each i, and for each i, process the first i-1 elements, what's the time complexity?

Wait, the constraints say n can be up to 100. So for each i, the maximum possible subset size is i-1, but the sum can be up to 100*100=10^4. Wait, M is up to 100. So S_i = M - t_i. Since t_i can be up to 100, S_i can be as low as 0 (if M=100 and t_i=100), but the problem states that t_i <= M, so S_i is >=0. So for each i, S_i can be up to M (if t_i is 0, but the problem says t_i >=1? No, the input says 1<= t_i <= M. So S_i can be up to M-1, like M=100, t_i=1: S_i=99.

But for each i, the problem reduces to: for the first i-1 elements, select a subset with sum <= S_i, and the maximum possible size. Then, the answer is (i-1 - max_size).

So for each i, we need to solve a knapsack-like problem where the value is the count (each item has value 1), and the weight is t_j, and we want the maximum number of items that sum up to <= S_i.

This is the standard unbounded knapsack problem where each item can be taken once (since each student is either taken or not). Wait, no: each student can be either included (if they are not failed) or excluded. So the problem is a 0-1 knapsack where the capacity is S_i, and we want maximum count of items, with sum of their weights <= S_i.

But 0-1 knapsack for maximum count with sum <= capacity can be solved greedily. Because the maximum count is achieved by selecting the smallest possible elements. For example, to maximize the number of items, select the items with the smallest t_j. So for each i, S_i = M - t_i. Then, among the first i-1 students, take as many as possible of those with the smallest t_j's such that their sum plus t_i is <= M. Wait, because that's equivalent to sum of their t_j's <= S_i. So the sum of the smallest t_j's (from the first i-1) must be <= S_i, and we take as many as possible.

Oh right! Because if you sort the first i-1 t_j's in ascending order, the maximum number of elements you can take is the largest k such that the sum of the first k elements is <= S_i. So this is a greedy problem. So for each i, the optimal approach is to take the smallest k t_j's from the first i-1 students, such that their sum is <= S_i, and k is as large as possible.

So the steps for each i are:

1. Compute S_i = M - t_i. If S_i <0, then even the i-th student's time is more than M. But according to the problem statement, t_i <= M, so S_i is >=0. So no need to worry about that.

2. Take the list of the first i-1 students' t_j's.

3. Sort this list in ascending order.

4. Find the maximum number of elements (k) such that the sum of the first k elements is <= S_i.

5. The answer for i is (i-1 - k), because we can keep k elements from the first i-1, plus the i-th, so total kept is k+1. The number of students to fail is (i) - (k+1) = i -k -1. But wait, the first i students are 1..i. But we are only considering the first i-1 students (the ones before i). So for the i-th student, the answer is the number of students in the first i-1 that are not taken (i-1 -k) plus whether the i-th is taken (but he must be taken). So yes, the answer is (i-1 -k).

So the approach is for each i, sort the first i-1 t_j's in ascending order, and then compute the prefix sums, and find the maximum k where sum of first k is <= S_i.

This is O(n^2 log n) time. Because for each i (up to n), we sort O(i) elements (i up to 100, so log i is manageable), and then compute prefix sums and check.

This is feasible for n=100. For each i, the first i-1 elements are sorted, then the prefix sum is computed. Then, for each possible k from 0 to i-1, check the sum. The maximum k is the largest where the sum is <= S_i.

Wait, but how to compute the maximum k efficiently?

Once the list is sorted and prefix sums are computed, we can iterate from k=0 to len(sorted_list) and check the sum. But even better, since the prefix sums are non-decreasing (since the elements are sorted in ascending order), we can binary search the maximum k where the sum up to k is <= S_i.

Yes. So for each i:

- Collect the first i-1 t's.

- Sort them in ascending order.

- Compute the prefix sum array.

- Then, binary search for the largest k where prefix_sum[k] <= S_i.

But since the elements are sorted, the prefix sum is non-decreasing. So binary search can find the maximum k where the sum is <= S_i.

This would reduce the time per i from O(i) to O(log i), which for n=100 is negligible.

So the overall steps are:

Read n and M.

Read the list t.

For each i from 0 to n-1 (since the input is 1-based, but in code 0-based):

Wait, the students are numbered from 1 to n. So for each i (1-based) in 1..n:

S_i = M - t[i]

Take the list of t_1 to t_{i-1}.

Sort this list.

Compute prefix sums.

Find the maximum k where sum of first k elements <= S_i.

The answer is (i-1) - k.

But wait, the first i-1 elements are 1..i-1. So for i=1, there are 0 elements before, so S_i = M - t[1], which must be >=0 (since t[1] <= M). So the sum of zero elements is 0. So if S_i >=0, then the answer for i=1 is 0 (since 0 elements can be kept, so (i-1) -0 = 0). Which makes sense.

So for example, in the first sample input:

n=7, M=15.

t = [1,2,3,4,5,6,7]

For i=6 (0-based?), wait no. Let's clarify. Let's say in code, the list is 0-based, so the first student is index 0. Then for the 6th student (0-based index 5), which is the 6th in 1-based, his t is 6. Then S_i is 15-6=9. The first 5 elements (indices 0-4) are [1,2,3,4,5]. Their sorted list is [1,2,3,4,5]. The prefix sums are [1,3,6, 10, 15]. Wait, the sum of first 3 elements is 1+2+3=6 <=9. Sum of first 4 is 10>9. So the maximum k is 3. So the answer is (5) -3 =2, which matches the first sample.

So this approach works.

So the plan is:

For each i in 0..n-1 (assuming 0-based):

- Compute S_i = M - t[i]

- Take the list of t[0..i-1] (if any)

- Sort this list in ascending order.

- Compute the prefix sum array.

- Use binary search to find the maximum k where sum of first k elements <= S_i.

- The answer for (i+1)-th student (if 0-based) is (i) -k.

Wait, no. Because for i-th in 0-based, the student is the (i+1)-th in 1-based. But when considering the i-th student (0-based), the students before him are 0..i-1. So for each 0-based index i:

S_i = M - t[i]

students before him are 0..i-1 (if i>0)

So for example, in the first sample, the 5th student (0-based index 5) is the 6th in the input, t=6. The students before are 0-4 (t=1,2,3,4,5). So sorted, their sum after k elements. So for that case, the answer is (5 (number of students before) -3 (k)) =2, which is correct.

So the code steps:

Read n and M.

t = list of n integers.

for each i in 0 to n-1:

   current_t = t[i]

   S = M - current_t

   previous = t[0..i-1] (if i>0)

   sorted_prev = sorted(previous)

   compute prefix sums of sorted_prev.

   find the largest k where sum of first k elements <= S.

   answer[i] = (i) -k

Wait, because the number of students before i is i (since 0..i-1 is i elements). So the answer is i -k (since k is the maximum number of students kept from the previous ones). So (i -k) is the number of students to remove from the previous ones. Because total students before i is i, and we keep k. Then, adding the current i-th student, the total kept is k +1, but the answer is the number of students to remove, which is (i) -k (since the current student is kept, so we don't count him in the removal).

Yes.

So the code can proceed as follows.

Now, for each i, collect the t's of previous students, sort them, compute prefix sums, and find the maximum k via binary search.

In Python, for each i, the code can be written as follows.

Let's take an example.

Sample input 2:

5 100

80 40 40 40 60

The output is 0 1 1 2 3.

For i=0 (student 1, t=80):

S = 100-80=20. Previous students are none. So sum is 0. So k=0. Answer is 0 -0=0.

Which matches the first output.

For i=1 (student 2, t=40). S=100-40=60.

Previous students are [80]. sorted is [80]. sum of first 0 elements is 0, which is <=60. sum of 1 element is 80>60. So maximum k is 0. So answer is 1 (number of previous students) -0 =1. Which matches the second output.

For i=2 (student 3, t=40). S=60.

Previous students are [80,40]. sorted is [40,80]. sum after 1 is 40 <=60. sum after 2 is 40+80=120>60. So k=1. answer is 2-1=1.

Which matches the third output.

For i=3 (student4, t=40). S=100-40=60.

Previous students are [80,40,40]. sorted is [40,40,80]. prefix sums:40,80, 160.

We need sum <=60. 40 is <=60. 80 is >60. So k=1. sum is40. So answer is3-1=2.

Which matches the fourth output.

For i=4 (student5, t=60). S=100-60=40.

Previous students are [80,40,40,40]. sorted: [40,40,40,80]. prefix sums:40,80,120, 200.

Find maximum k where sum <=40. So k=1 (sum 40). So answer is 4-1=3. Which matches the fifth output.

So this approach works.

So the code can be structured as follows.

In Python:

Read n and M.

t = list(map(int, input().split())).

Then for each i in 0..n-1:

   if i ==0:

      answer is 0 (since no previous students).

   else:

      previous = t[:i]

      sorted_prev = sorted(previous)

      prefix = [0]*(len(sorted_prev)+1)

      for j in range(1, len(sorted_prev)+1):

          prefix[j] = prefix[j-1] + sorted_prev[j-1]

      # Now find the maximum k where prefix[k] <= S.

      S = M - t[i]

      # binary search.

      low = 0

      high = len(sorted_prev)

      best =0

      while low <= high:

          mid = (low + high) //2

          if prefix[mid] <= S:

              best = mid

              low = mid +1

          else:

              high = mid -1

      answer = i - best

   print the answers.

Wait, but for i=0, the code:

previous is t[:0] which is empty. So sorted_prev is empty. Then prefix is [0]. So the maximum k is 0. answer is 0-0=0.

Which is correct.

So the code can handle all cases.

Now, considering the constraints: n is up to 100, M up to 100. So for each i, the sorted list is up to 99 elements, and the sum can be up to 99*100=9900, but S_i can be up to 100.

But the binary search is O(log i), which is acceptable.

Thus, the code should be efficient enough.

Now, let's test this approach against the sample input 1.

Sample Input 1:

7 15

1 2 3 4 5 6 7

Sample Output:0 0 0 0 0 2 3.

Let's check i=5 (0-based, which is the 6th student in 1-based, t=6). S_i=15-6=9.

Previous students are t[0..4] = [1,2,3,4,5]. sorted_prev is [1,2,3,4,5].

prefix sums: 0,1,3,6,10,15.

We need sum <=9.

Looking for the largest k where sum <=9. Let's see:

k=3: sum is6 <=9.

k=4: sum is10>9.

So best is3. answer is5-3=2. Which matches the sample.

Similarly, for i=6 (0-based, student7, t=7). S_i=15-7=8.

Previous students are t[0..5]=[1,2,3,4,5,6]. sorted is [1,2,3,4,5,6].

prefix sums:0,1,3,6,10,15,21.

Looking for sum <=8. The maximum k is 3 (sum 6). So answer is6-3=3.

Which matches the sample.

So the code works.

Thus, this approach is correct.

Now, the code can be written in Python as follows.

But in Python, for each i, we can precompute the sorted list and prefix sums. Also, for the binary search, since the prefix array is sorted, we can use bisect module.

Alternatively, use bisect_right.

Wait, the prefix array is prefix[0], prefix[1], ..., prefix[m], where m is the length of the sorted_prev list. And since sorted_prev is sorted in ascending order, the prefix sums are strictly increasing. So to find the largest k where prefix[k] <= S, we can use bisect_right on the prefix array for S.

For example, the prefix array for the first sample i=5 is [0,1,3,6,10,15]. For S=9, bisect_right returns the first index where the value is greater than 9. The prefix array is [0,1,3,6,10,15]. So bisect_right(prefix, 9) returns 4, since 10 is the first element greater than9. So the largest k is 4-1=3. Because prefix[3] is6, prefix[4] is10>9.

So for each i, the code can be written as:

import bisect

...

prefix = [0]

for j in range(len(sorted_prev)):

    prefix.append(prefix[-1] + sorted_prev[j])

max_k = bisect.bisect_right(prefix, S) -1

This would give the maximum k.

Thus, using bisect can make the code more efficient and concise.

So the code can be structured with that in mind.

Putting it all together:

Read n, M.

t = list(map(int, input().split())).

answers = []

for i in range(n):

    current_t = t[i]

    S = M - current_t

    if S <0:  # but according to problem statement, this can't happen.

        # but the problem says t_i <= M, so S is >=0.

    prev_list = t[:i]

    prev_list.sort()

    # compute prefix sums.

    prefix = [0]

    for num in prev_list:

        prefix.append(prefix[-1] + num)

    # find the largest k where prefix[k] <= S.

    k = bisect.bisect_right(prefix, S) -1

    ans = i - k

    answers.append(str(ans))

print(' '.join(answers))

Yes.

Testing this code with the sample inputs:

Sample 1:

n=7, M=15.

t = [1,2,3,4,5,6,7].

For i=5 (0-based):

prev_list is [1,2,3,4,5]. sorted is same. prefix is [0,1,3,6,10,15].

bisect_right(prefix, 9) returns 4 (since prefix[4]=10>9). So k=3. ans=5-3=2.

Sample 2:

n=5, M=100.

t = [80,40,40,40,60].

For i=4 (0-based, student5):

prev_list is [80,40,40,40]. sorted is [40,40,40,80]. prefix sums [0,40,80, 120, 200, 280].

S=100-60=40.

bisect_right(prefix,40) returns 2 (since prefix[2]=40 is equal, but the next is 80>40. So k=2-1=1. ans=4-1=3.

Which matches the sample.

So the code works.

Therefore, this is the correct and efficient approach for the problem.
</think>

```python
import bisect

n, M = map(int, input().split())
t = list(map(int, input().split()))
answers = []

for i in range(n):
    current_t = t[i]
    S = M - current_t
    prev_list = t[:i]
    prev_list.sort()
    prefix = [0]
    for num in prev_list:
        prefix.append(prefix[-1] + num)
    k = bisect.bisect_right(prefix, S) - 1
    answers.append(str(i - k))

print(' '.join(answers))
```