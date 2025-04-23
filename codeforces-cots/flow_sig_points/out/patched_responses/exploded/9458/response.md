<think>
Okay, let's tackle this problem. The task is to determine the number of distinct pitches in a given range of frets across all strings. Each string's pitch at fret j is s_i + j. For each query l and r, we need to find how many unique values there are in the union of all s_i + j where j ranges from l to r inclusive, for all i.

Hmm. The constraints are tight. n and q can be up to 1e5, which suggests that O(n) per query is too slow. We need a way to process each query in O(1) or O(log n) time.

Let's think about the problem. For each query [l, r], the pitches for each string i form a consecutive sequence of integers from s_i + l to s_i + r. So each string contributes a range of (r - l + 1) numbers, but these ranges might overlap between different strings.

The total distinct numbers would be the union of all these ranges. So the problem reduces to finding the union of multiple ranges, each of which is [s_i + l, s_i + r], and then calculating the total length of this union.

But calculating this union directly for each query is computationally impossible given the constraints, because the number of ranges is up to 1e5 and queries are 1e5 as well.

So we need a smarter approach. Let's think of the ranges [s_i + l, s_i + r] as [a_i, b_i], where a_i = s_i + l and b_i = s_i + r. The union of these ranges is the total number of distinct integers covered.

The key observation here is that if we sort the s_i values, the merged ranges can be processed efficiently. Let's sort the s_i in ascending order. Then, for each consecutive pair of s_i and s_{i+1}, there's a certain condition under which their ranges overlap.

Wait, but when you add l and r to s_i and s_j, the ranges [s_i + l, s_i + r] and [s_j + l, s_j + r] will be non-overlapping if s_j + l > s_i + r. Otherwise, they overlap. So for two sorted s_i and s_j (assuming s_i <= s_j), the ranges overlap if s_j + l <= s_i + r. Rearranged, this is s_j - s_i <= r - l.

So the distance between s_j and s_i must be <= (r - l) for their ranges to overlap. If that's the case, the merged range for these two would be [s_i + l, s_j + r]. But if the distance is larger than (r - l), then the ranges are separate.

Therefore, when the s_i are sorted, the merged ranges can be determined by checking consecutive s_i's. For each s_i, if the next s (s_{i+1}) minus s_i is greater than (r - l), then the ranges are separate. Otherwise, their merged ranges overlap, so we can merge them.

So the problem reduces to:

1. Sort the s array.
2. For each query [l, r], compute the total union of the ranges [s_i + l, s_i + r] for all i.

But how to compute this efficiently?

The total union can be calculated as the sum of all individual ranges minus the overlaps. But that's not straightforward. Alternatively, when sorted, the merged ranges can be found by grouping consecutive s_i's where the difference between consecutive s_i's is <= (r - l). Each such group contributes a merged range of length (s_max_in_group + r) - (s_min_in_group + l) + 1. The sum of all these merged ranges is the answer for the query.

Wait, right! So for the sorted s array, we can group the strings into intervals where each interval consists of consecutive s_i's where each adjacent pair in the group has s_{i+1} - s_i <= (r - l). The merged range for such a group would start at s_start + l and end at s_end + r. The length is (s_end + r) - (s_start + l) + 1.

The total number of distinct pitches is the sum over all groups of (s_end + r - s_start - l + 1).

So the algorithm for a query would be:

- Compute the interval length: r - l + 1 (call this L).
- For the sorted s array, find the number of groups where consecutive s_i's are more than L apart. Each group contributes a merged range.
- For each group, the start is the first s in the group, end is the last s in the group. The merged range is (end + r) - (start + l) + 1.

But how to compute this efficiently for each query?

Let me think. The sorted s array can be processed once. For each query, we need to find the number of "gaps" between consecutive s_i's that are larger than L = (r - l). Because each such gap indicates a separation between groups. The number of groups is equal to the number of gaps exceeding L plus 1 (since each gap splits into a new group).

Wait, for example, sorted s: [s1, s2, s3, s4], where s2 - s1 > L, s3 - s2 <= L, s4 - s3 > L. Then the groups are [s1], [s2, s3], [s4]. The gaps are between s1-s2, s2-s3, s3-s4. The gaps > L are s1-s2 and s3-s4. So the number of groups is 3 (number of gaps > L is 2, plus 1).

Yes. So the number of merged groups is equal to the number of gaps (s_{i+1} - s_i) > L, plus 1.

Then the total distinct pitches would be:

sum over each group ( (s_end + r) - (s_start + l) + 1 )

But s_start is the first element in the group, s_end is the last. For the entire group, the merged range starts at s_start + l, ends at s_end + r. The length is (s_end + r) - (s_start + l) + 1.

Alternatively, for each group, the merged range length is (s_end - s_start) + (r - l) + 1.

Because (s_end + r) - (s_start + l) +1 = (s_end - s_start) + (r - l) + 1.

So the total is sum for each group (s_end - s_start + (r - l) + 1).

But the sum of (s_end - s_start) for all groups is (sum of (s_end) for all groups) - (sum of s_start for all groups). But since each group is a consecutive sequence, the sum of (s_end - s_start) for all groups is equal to (last element of sorted s array - first element of sorted s array) minus the sum of all gaps that are larger than L. Wait, perhaps not. Let's think:

The sorted s array is s1 <= s2 <= ... <= sn.

The sum of s_end - s_start for all groups is equal to the sum for each group of (s_last_in_group - s_first_in_group). For example:

Groups: [s1], [s2, s3], [s4]. Sum is (s1 - s1) + (s3 - s2) + (s4 - s4) = s3 - s2.

But this is the sum of (s_last - s_first) for each group.

But the total of all (s_last - s_first) for all groups is equal to the sum of all consecutive s_i differences that are not part of a split. Hmm, maybe there's another way to compute this.

Wait, considering the entire sorted array, the total sum of (s_i+1 - s_i) is s_n - s_1. Now, when we split the array into groups whenever a gap is larger than L, the sum of (s_last - s_first) for each group is equal to the sum of all (s_i+1 - s_i) that are not gaps larger than L. Because each group is formed by consecutive elements where all adjacent gaps within the group are <= L. So the sum of (s_last - s_first) for each group is (s_last_in_group - s_first_in_group) = sum of (s_i+1 - s_i) for all consecutive pairs in the group. So the sum over all groups is (s_n - s_1) - sum of gaps where (s_i+1 - s_i) > L.

Because, the sum of all (s_i+1 - s_i) is s_n - s_1. The gaps that are > L are excluded from the group sums. So the sum of group (s_last - s_first) is (s_n - s_1) minus the sum of gaps that are > L.

Therefore, the total distinct pitches can be computed as:

number_of_groups * (r - l + 1) + (sum of (s_last - s_first) for each group).

Which can be rewritten as:

number_of_groups * (r - l + 1) + (s_n - s_1 - sum_of_gaps).

Where sum_of_gaps is the sum of (s_{i+1} - s_i) for all i where s_{i+1} - s_i > L.

But the sum of (s_last - s_first) is (s_n - s_1 - sum_of_gaps). So the total distinct pitches is:

number_of_groups * (r - l + 1) + (s_n - s_1 - sum_of_gaps).

But how to compute sum_of_gaps and the number_of_groups (which is the count of gaps > L plus 1) efficiently for each query?

Wait, for each query, L is (r - l). So the key is to compute:

- The number of gaps (s_{i+1} - s_i) > L. Let's call this C.
- The sum of all gaps (s_{i+1} - s_i) where the gap > L. Let's call this S.

Then, the number_of_groups is C + 1.

The total distinct pitches would be:

(C + 1) * (r - l + 1) + (s[-1] - s[0] - S) 

Because (s[-1] - s[0]) is the sum of all gaps (s_{i+1} - s_i) for i from 0 to n-2 (assuming 0-based). Subtract S (sum of gaps > L) gives the sum of gaps <= L, which is the sum of (s_last - s_first) for each group. Then, multiplied by the (r - l + 1) per group (number of groups) plus that sum.

Wait, let me check:

Total distinct pitches = sum for each group ( (s_end + r) - (s_start + l) + 1 )

Which is sum( (s_end - s_start) + (r - l) + 1 )

Which is sum( (s_end - s_start) ) + sum( (r - l + 1) )

The sum of (s_end - s_start) is (s_n - s_1 - sum_of_gaps), as discussed.

The sum of (r - l + 1) is number_of_groups * (r - l + 1).

So overall, it's (C + 1) * (r - l + 1) + (s_n - s_1 - S).

Yes.

So, the problem reduces to, for each query, compute C (number of gaps > L) and S (sum of those gaps). Then plug into the formula.

Now, the question is, how to compute C and S efficiently for a given L (which is r - l) for each query.

The sorted s array can be pre-processed. The gaps can be stored as a sorted list. Then, for each query L, we can find how many gaps are larger than L, and sum those gaps.

So the gaps between consecutive sorted s_i's can be precomputed. Let's call the gaps array G, where G[i] = s_{i+1} - s[i], for i from 0 to n-2.

Then, G is a list of (n-1) elements. We can sort G. Wait, no, because the gaps are between consecutive sorted s_i's, so G is a list of (n-1) elements, but they are in the order of the sorted s array. So, for example, if s is sorted as [1,3,5], then G is [2,2].

Wait, but for processing queries, when given L = r - l, we need to find the number of elements in G that are > L, and their sum. How to do this efficiently?

We can pre-process the gaps into a sorted list. Then, for each query L, perform a binary search to find how many gaps are > L. Similarly, the sum of gaps > L can be found using a prefix sum array.

So the steps would be:

1. Sort the s array.
2. Compute the gaps G between consecutive elements in the sorted s array.
3. Sort the gaps G in ascending order, and compute a prefix sum array of the sorted gaps. Wait, but to find the sum of gaps greater than L, we can sort G in ascending order and have a prefix sum array. Wait, no. For example, if sorted G is [g1, g2, ..., gm] in ascending order, the sum of all gaps > L is sum of all gaps where g_i > L. Since the gaps are sorted, we can find the first index where g_i > L, and take the sum from that index to the end.

So, the plan is:

- Precompute the sorted gaps in ascending order (so that binary search can be used to find how many are > L).
- Precompute a prefix sum array of the sorted gaps. Wait, but sorted in ascending order, so the prefix sum is sum[0..i] of the sorted gaps. Then, to get the sum of gaps > L, we need the sum from the first gap greater than L to the end. Let's see.

Suppose the gaps are sorted in ascending order. Then, for a given L, find the smallest index pos where gaps[pos] > L. All gaps from pos to m-1 (where m is the number of gaps) are > L. The sum would be the total sum of all gaps minus the prefix sum up to pos-1.

Wait, for example, if gaps are [1,2,3,4,5], sorted in ascending order. Suppose L=3. Then gaps >3 are 4 and 5. The sum is 4+5=9. The prefix sum up to index 3 (value 4) is 1+2+3+4=10. The total sum is 15. So sum of gaps >3 is 15 - 10 = 5+4=9? Wait, no, wait in this example, the sum is 4+5=9. The prefix sum up to index 3 is 1+2+3+4=10, but gaps after pos (where pos is the first index where gap>3) is index 3 (gaps[3]=4>3). So the sum from 3 to 4 is 4+5=9. The prefix sum up to index 2 (3 elements) is 1+2+3=6. So sum = total_sum - prefix_sum up to index 2.

So to compute the sum of gaps > L, given that gaps are sorted in ascending order:

1. Find the first index pos where gaps[pos] > L. All gaps from pos to end are > L.
2. The sum is total_sum_gaps - prefix_sum[pos].

But the prefix sum array is the sum of gaps up to index i (inclusive). So for example, prefix_sum[i] = sum of gaps[0..i].

So the sum of gaps > L is (sum of all gaps) - (prefix_sum[pos-1]).

But how to handle when pos is 0? If all gaps are > L, then pos is 0, sum is sum of all gaps. So in that case, prefix_sum[pos-1] is prefix_sum[-1], which we can consider as 0.

So the steps are:

- Sort the gaps in ascending order. Let's call this sorted_gaps.
- Compute the prefix_sum array for sorted_gaps. prefix_sum[0] = sorted_gaps[0], prefix_sum[1] = prefix_sum[0] + sorted_gaps[1], etc.
- Compute the total_sum = sum of all gaps (which is prefix_sum[-1] if prefix_sum is built correctly).
- For a given L, find the smallest pos where sorted_gaps[pos] > L. Then, the number of gaps > L is m - pos, where m is the number of gaps (n-1).
- The sum of these gaps is total_sum - (prefix_sum[pos-1] if pos >0 else 0).

So, for each query, given L = r - l, we can:

- Compute C = (number of gaps > L) = m - pos.
- Compute S = sum of gaps > L = total_sum - (prefix_sum[pos-1] if pos >0 else 0).

Then, the formula for the answer is:

answer = (C + 1) * (r - l + 1) + (s_n_minus_1 - s_0) - S + (s_n_minus_1 - s_0) ?

Wait, wait. The formula is:

answer = (C + 1) * (r - l + 1) + (s[-1] - s[0] - S)

Because s[-1] - s[0] is the sum of all gaps (since the sum of all gaps is s[-1] - s[0]). Then subtract S (sum of gaps > L) gives the sum of gaps <= L, which is the sum of (s_end - s_start) for each group.

So, the formula is correct.

Putting it all together:

We pre-process the sorted s array, compute the sorted_gaps and the prefix_sum array.

For each query l, r:

1. Compute L = r - l.
2. Compute C and S as per the sorted_gaps.
3. The answer is (C + 1) * (r - l + 1) + (s[-1] - s[0] - S).

But we need to handle the case when n = 1. Because when n=1, there are no gaps (m=0). So for n=1, the number of groups is 1, and the answer is (r - l + 1). Because the single string contributes a range of length (r - l + 1).

Yes.

So, the steps for code:

Read n.

Read s array.

Sort s array.

Compute the gaps between consecutive elements. For i in 0 to n-2, gaps[i] = s[i+1] - s[i].

Sort the gaps array in ascending order.

Compute the prefix_sum array of the sorted gaps.

Compute the total_sum = sum of all gaps (which is s[-1] - s[0]).

Then, for each query:

Read l, r.

If n == 1:

   The answer is (r - l + 1).

Else:

   L = r - l.

   Use binary search to find the first index pos in sorted_gaps where the gap > L.

   C = len(sorted_gaps) - pos.

   sum_S = total_sum - (prefix_sum[pos-1] if pos >0 else 0).

   answer = (C + 1) * (r - l + 1) + (s[-1] - s[0] - sum_S).

But wait, wait. Let's check.

Wait, the formula is:

answer = (C + 1) * (r - l + 1) + (s_end - s_start - sum_S).

Yes. Because:

- (C+1) is the number of groups.

- (r - l +1) is the length contributed per group (since each group's length is (r-l+1) + (s_end - s_start)). Wait no, the formula is (r - l +1) multiplied by the number of groups, and then add (sum of (s_end - s_start) for each group).

But sum of (s_end - s_start) per group is s[-1] - s[0] - sum_S.

So the total is (C + 1) * (r-l+1) + (s[-1] - s[0] - sum_S).

So code for when n >= 1.

But in code, when n is 1, the gaps array is empty. So the code for n=1 is handled as a separate case.

Now, the steps for code:

Implement the above logic.

But in Python, how to handle the binary search?

We can use the bisect module. The sorted_gaps array is sorted in ascending order. For a given L, we want to find the first position where gap > L. Since the array is sorted, bisect_right can be used to find the insertion point of L, then all elements after that are > L.

Wait, no. For example, if sorted_gaps is [1,2,3,4,5], and L=3, then the elements >3 are 4,5. The bisect.bisect_right gives the insertion point after elements <= L. So for L=3, bisect_right returns 4 (since 3 is found at index 2, and elements after are 4 and 5). Wait no, sorted_gaps is [1,2,3,4,5]. bisect.bisect_right(sorted_gaps, 3) returns 3, because 3 is at index 2. The elements after index 3 (exclusive) are 4 and 5.

Wait, bisect_right returns the insertion point, so for example, inserting L into the list would be placed after all existing entries <= L.

So for sorted_gaps, the number of elements > L is len(sorted_gaps) - bisect_right(sorted_gaps, L).

Yes.

So in code:

pos = bisect.bisect_right(sorted_gaps, L)

C = len(sorted_gaps) - pos

sum_S = total_sum - (prefix_sum[pos-1] if pos > 0 else 0)

But the prefix_sum array is for the sorted_gaps. For example, prefix_sum[i] is sum of sorted_gaps[0..i]. So the sum of elements up to pos-1 is prefix_sum[pos-1] if pos>0.

So the code for the sum_S is correct.

Now, handling the sorted_gaps and prefix_sum:

We can compute sorted_gaps as sorted(gaps) where gaps are the differences between consecutive elements of the sorted s array.

But in code:

s = sorted(s_list)

gaps = [s[i+1] - s[i] for i in range(len(s)-1)]

sorted_gaps = sorted(gaps)

Then compute prefix_sum as a list where prefix_sum[i] = sum of sorted_gaps[0..i].

In Python, we can compute this with a list:

prefix_sum = []
current_sum = 0
for gap in sorted_gaps:
    current_sum += gap
    prefix_sum.append(current_sum)

total_sum = current_sum if sorted_gaps else 0

Wait, but if there are no gaps (n=1), sorted_gaps is empty. So in that case, total_sum is 0.

But when n >=2, sorted_gaps is non-empty.

Now, for each query:

if n == 1:

   answer is (r-l+1)

else:

   L = r - l

   pos = bisect.bisect_right(sorted_gaps, L)

   C = len(sorted_gaps) - pos

   sum_S = total_sum - (prefix_sum[pos-1] if pos >0 else 0)

   answer = (C + 1) * (r - l + 1) + (s[-1] - s[0] - sum_S)

Yes.

Now, let's test this against the examples.

First example:

Input:

6

3 1 4 1 5 9

After sorting s: [1,1,3,4,5,9]

gaps between consecutive elements:

1-1: 0 (s[1]-s[0] = 0)

3-1: 2 (s[2]-s[1] = 2)

4-3:1 (s[3]-s[2] =1)

5-4:1 (s[4]-s[3] =1)

9-5:4 (s[5]-s[4] =4)

gaps = [0,2,1,1,4]

sorted_gaps = [0,1,1,2,4]

prefix_sum: 0, 1, 2, 4, 8.

total_sum = 0+2+1+1+4 =8? Wait, no:

Wait original gaps are [0,2,1,1,4]. When sorted, sorted_gaps is [0,1,1,2,4]. So the prefix_sum would be 0, 1, 2, 4, 8. And total_sum is 8.

Let's take the first query: 7 7.

L = 7-7 =0.

We need to find the number of gaps >0. sorted_gaps is [0,1,1,2,4]. So bisect_right(sorted_gaps, 0) is the index where 0 is found. Since sorted_gaps[0] is 0, and all elements after that are >=0. So bisect_right returns 1 (the insertion point after all 0s). Because elements after index 0 are 1,1,2,4.

So pos=1. C=5-1=4 (number of gaps>0 is 4). sum_S is total_sum (8) minus prefix_sum[0] (0) → 8-0=8.

answer = (4+1) * (7-7+1) + (9-1 - 8) → 5 * 1 + (8 -8) =5 +0=5. Which matches the first sample.

Yes.

Second query: 0 2. L=2-0=2.

sorted_gaps is [0,1,1,2,4]. We want gaps >2. The elements are 4. So pos is the first index where gap >2. Since sorted_gaps has 0,1,1,2,4. So 2 is at index 3. bisect_right(sorted_gaps, 2) returns 4 (since all elements up to index 3 are <=2). So pos=4. C=5-4=1. sum_S is 8 - prefix_sum[3] (0+1+1+2=4) → 8-4=4.

answer = (1+1) * (2-0 +1) + (9-1 -4) → 2 *3 + (8-4) →6 +4=10. Which matches the sample.

Third query:8 17. L=17-8=9. All gaps in sorted_gaps are 0,1,1,2,4. All are <=9. So pos = bisect_right(sorted_gaps,9) →5, since all elements are <=9. C=5-5=0. sum_S=8- prefix_sum[4] =8-8=0. answer= (0+1)*(17-8+1) + (9-1 -0) → 1*10 +8 =18. Which matches the sample.

Yes.

Second sample input:

2

1 500000000000000000

Queries:

1000000000000000000 1000000000000000000 → l=1e18, r=1e18. L=0.

and 0 to 1e18.

First query:

s after sorting is [1,5e17]. gap is 5e17 -1 =499999999999999999.

sorted_gaps is [499999999999999999]. prefix_sum is [499999999999999999]. total_sum is 499999999999999999.

For L=0, which is 0. The gap is 499999999999999999, which is >0. So bisect_right(sorted_gaps, 0) returns 0. pos=0. C=1-0=1. sum_S=499999999999999999 -0 (since pos=0, prefix_sum[pos-1] is invalid, so sum_S = total_sum -0). So sum_S =499999999999999999.

answer = (1+1) * (0 +1) → 2*1=2, plus (5e17 -1 - 499999999999999999). 5e17 is 500000000000000000. So 5e17-1 is 499999999999999999. 499999999999999999 -499999999999999999 =0. So total answer is 2*1 +0=2. Which matches the sample.

Second query: l=0, r=1e18. L=1e18-0=1e18. The gap is 5e17-1=499999999999999999, which is less than 1e18 (since 1e18 is 1000000000000000000). So bisect_right(sorted_gaps, 1e18) returns 1 (since 499999999999999999 is less than 1e18, and there's one element in sorted_gaps). So C=1-1=0. sum_S=499999999999999999 - prefix_sum[0] (since pos=1, sum_S = total_sum - prefix_sum[0] → 499999999999999999 -499999999999999999 =0). So answer is (0+1) * (1e18 -0 +1) + (5e17 -1 -0). 1e18+1 is 1000000000000000001. So 1 * (1e18+1) → 1e18+1. Then, 5e17-1 is 499999999999999999. So total is 1e18+1 +499999999999999999. 1e18 is 1000000000000000000. Adding 1 gives 1000000000000000001. Adding 499999999999999999 gives 1499999999999999999 +1 → 1500000000000000000. Which matches the sample output.

So the approach works.

Now, implement this in Python.

But handling large numbers, but Python can handle big integers.

Edge cases:

- n=1: return (r - l + 1).

- All gaps are <= L: then sum_S is 0.

Now, code:

Read n.

Read s array.

Sort s.

If n ==1:

   handle queries as r - l +1.

Else:

   compute gaps.

   sorted_gaps = sorted(gaps).

   compute prefix_sum.

   total_sum = sum of gaps.

For each query:

   read l, r.

   if n==1:

      print(r-l+1, end=' ')

   else:

      L = r - l.

      pos = bisect.bisect_right(sorted_gaps, L)

      C = len(sorted_gaps) - pos

      if pos ==0:

          sum_S = total_sum

      else:

          sum_S = total_sum - prefix_sum[pos-1]

      ans = (C +1) * (r - l +1) + (s[-1] - s[0] - sum_S)

      print(ans, end=' ')

But wait, code for sum_S:

sum_S = total_sum - (prefix_sum[pos-1] if pos>0 else 0)

So code:

if pos >0:

    sum_S = total_sum - prefix_sum[pos-1]

else:

    sum_S = total_sum

So that's correct.

Implement this.

But in code, the prefix_sum is a list. For example, for sorted_gaps [0,1,1,2,4], prefix_sum is [0,1,2,4,8].

Now, code in Python:

import bisect

n = int(input())
s = list(map(int, input().split()))
s.sort()
queries = []
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

if n == 1:
    res = []
    for l, r in queries:
        res.append(r - l + 1)
    print(' '.join(map(str, res)))
else:
    # Compute gaps
    gaps = []
    for i in range(n-1):
        gaps.append(s[i+1] - s[i])
    sorted_gaps = sorted(gaps)
    # Compute prefix sum
    prefix_sum = []
    total = 0
    for gap in sorted_gaps:
        total += gap
        prefix_sum.append(total)
    total_sum = sum(gaps)  # which is s[-1] - s[0]

    res = []
    for l, r in queries:
        L = r - l
        pos = bisect.bisect_right(sorted_gaps, L)
        C = len(sorted_gaps) - pos
        if pos == 0:
            sum_S = total_sum
        else:
            sum_S = total_sum - prefix_sum[pos-1]
        ans = (C +1) * (r - l + 1) + (s[-1] - s[0] - sum_S)
        res.append(ans)
    print(' '.join(map(str, res)))

But wait, when n=1, s has one element. So s[-1] - s[0] is zero, but since n is 1, the code path for n==1 is separate.

Yes.

Testing this code with the first sample input:

Sample Input 1:

6

3 1 4 1 5 9 → sorted s becomes [1,1,3,4,5,9]

gaps are [0,2,1,1,4]. sorted_gaps becomes [0,1,1,2,4], prefix_sum [0,1,2,4,8].

Queries:

7 7 → L=0.

pos = bisect.bisect_right([0,1,1,2,4], 0) → returns 1. C=5-1=4. sum_S = 8 - prefix_sum[0] (0) →8. ans = (4+1)*1 + (9-1 -8) →5*1 +0=5.

Second query 0 2 → L=2. pos = bisect_right([0,1,1,2,4], 2) → returns 4. C=5-4=1. sum_S=8-4 (prefix_sum[3] is 0+1+1+2=4). 8-4=4. ans= (1+1)*3 + (9-1-4) →2*3 +4=6+4=10.

Third query 8 17 → L=9. bisect_right on [0,1,1,2,4] returns 5. C=0. sum_S=8 - prefix_sum[4] (8) →0. ans=1*10 + (9-1 -0) →10+8=18.

Which matches.

Sample 2:

n=2.

s = [1,500000000000000000]. sorted.

gaps is [499999999999999999].

sorted_gaps is same. prefix_sum [499999999999999999]. total_sum is 499999999999999999.

First query L=0. bisect_right([499999999999999999],0) →0. C=1-0=1. sum_S=499999999999999999 -0 →499999999999999999. ans=2*1 + (500000000000000000-1 -499999999999999999) →2 + (500000000000000000-1 -499999999999999999) →2 + (499999999999999999 -499999999999999999) →2.

Second query L=1e18-0=1e18. sorted_gaps has 499999999999999999, which is 5e17-1. 5e17-1 is 499,999,999,999,999,999 which is 4.999...e17. So 1e18 is larger. So bisect_right returns 1. C=0. sum_S=0. ans=1*(1e18+1) + (5e17-1 -0) →1e18+1 +5e17-1 →1e18 +5e17 →1.5e18.

Which matches the sample.

So code should work.

Now, code optimizations:

Reading input as per the problem's constraints. For n up to 1e5, and q up to 1e5, reading inputs efficiently is important.

In Python, using sys.stdin.readline can be faster. So perhaps we can read the input with sys.stdin.

But the code as written uses input(), which might be acceptable, but for large inputs, it's better to read via sys.stdin.

So modifying the code to use sys.stdin:

But given that the problem requires reading from stdin and writing to stdout, and that Python's input() is sometimes slow for large data, it's better to read the entire input at once.

Here's the modified code using sys.stdin:

import bisect
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr +=1
    s = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    q = int(input[ptr])
    ptr +=1
    queries = []
    for _ in range(q):
        l = int(input[ptr])
        r = int(input[ptr+1])
        queries.append( (l, r) )
        ptr +=2
    s.sort()
    if n ==1:
        res = [ (r-l +1) for l, r in queries ]
        print(' '.join(map(str, res)))
        return
    gaps = []
    for i in range(n-1):
        gaps.append(s[i+1] - s[i])
    sorted_gaps = sorted(gaps)
    prefix_sum = []
    total =0
    for gap in sorted_gaps:
        total += gap
        prefix_sum.append(total)
    total_sum = s[-1] - s[0]
    res = []
    for l, r in queries:
        L = r - l
        pos = bisect.bisect_right(sorted_gaps, L)
        C = len(sorted_gaps) - pos
        if pos ==0:
            sum_S = total_sum
        else:
            sum_S = total_sum - prefix_sum[pos-1]
        ans = (C+1)*(r - l +1) + (s[-1] - s[0] - sum_S)
        res.append(ans)
    print(' '.join(map(str, res)))
    
if __name__ == "__main__":
    main()

This code reads all input at once using sys.stdin.read(), splits into a list of strings, and processes them via a pointer. This is more efficient for large inputs.

Testing this code with the samples should work.

Yes.

Thus, this code should pass all test cases efficiently.
</think>

```python
import bisect
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    s = list(map(int, input[ptr:ptr + n]))
    ptr += n
    q = int(input[ptr])
    ptr += 1
    queries = []
    for _ in range(q):
        l = int(input[ptr])
        r = int(input[ptr + 1])
        queries.append((l, r))
        ptr += 2
    s.sort()
    if n == 1:
        res = [(r - l + 1) for l, r in queries]
        print(' '.join(map(str, res)))
        return
    gaps = []
    for i in range(n - 1):
        gaps.append(s[i + 1] - s[i])
    sorted_gaps = sorted(gaps)
    prefix_sum = []
    total = 0
    for gap in sorted_gaps:
        total += gap
        prefix_sum.append(total)
    total_sum = s[-1] - s[0]
    res = []
    for l, r in queries:
        L = r - l
        pos = bisect.bisect_right(sorted_gaps, L)
        C = len(sorted_gaps) - pos
        if pos == 0:
            sum_S = total_sum
        else:
            sum_S = total_sum - prefix_sum[pos - 1]
        ans = (C + 1) * (r - l + 1) + (s[-1] - s[0] - sum_S)
        res.append(ans)
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
```