<think>
Okay, let's try to figure out this problem. The task is to count the number of subarrays where the median is exactly m. The array is a permutation, so all elements are unique, which helps.

First, I need to understand what makes a subarray have m as its median. The median is the middle element when the subarray is sorted. If the length is even, it's the left of the two middle elements. So for a subarray of length k, the median is at position ceil(k/2) - 1 if we index from 0 after sorting. Wait, no, let's think again. For example, when k is odd, say 3, the median is the second element (index 1). When k is even, say 4, the median is the second element (index 1) after sorting. So for a subarray of length L, the median is the element at position (L-1)//2 in the sorted array.

So, for a given subarray from l to r (inclusive), when we sort the elements, the element at position (r-l+1 -1)//2 = (r-l)//2 must be m. So the key is to find all intervals [l, r] where m is the element in this particular position after sorting.

But how do we efficiently compute this? Because checking every possible subarray is O(n^2), which is way too slow for n up to 2e5.

Hmm. Let's think about the position of m in the original array. Let's say m is located at position pos in the array. Because the array is a permutation, there's exactly one occurrence of m.

For a subarray [l, r] to include m as the median, the subarray must include pos, since otherwise m isn't even in the subarray. So all valid intervals must include pos.

Wait, right. Because if a subarray doesn't include pos, then m isn't part of it, so its median can't be m. So the first thing to do is find the position of m in the array, and then consider all subarrays that include this position.

So the approach can be split into two parts: subarrays where pos is the median, and the subarray includes pos. So all valid subarrays must contain pos, and within those, the count of elements less than m and greater than m must satisfy certain conditions.

Let's think: For a subarray that includes pos, how many elements are less than m and greater than m in the left and right parts.

Let me model the problem as follows: For the subarray [l, r], which must include pos (so l <= pos <= r), the median is m. So in the sorted version of this subarray, m is in the middle position.

The median's position in the sorted array is (k-1)//2, where k is the length of the subarray. So the number of elements in the subarray that are less than m must be equal to the number of elements greater than m in such a way that m is placed exactly in the required position.

Wait, let's break it down. Let's consider all elements in the subarray. Let's split them into three parts: elements less than m, equal to m (exactly one), and greater than m. Let the count of elements less than m in the subarray be c_less, and count greater be c_greater. The total elements is k = c_less + 1 + c_greater.

For m to be the median, in the sorted array, the position of m must be (k-1)//2. That position is determined by the number of elements less than m. Because after sorting, all elements less than m come first, then m, then the greater ones. So the position of m is exactly c_less. So the condition is that c_less must be equal to (k-1)//2.

But since k = c_less + 1 + c_greater, substituting k:

c_less = ( (c_less + 1 + c_greater) -1 ) // 2

Simplify the right-hand side: (c_less + c_greater) // 2.

So c_less = (c_less + c_greater) // 2.

Multiply both sides by 2:

2 c_less = c_less + c_greater → c_less = c_greater.

So the number of elements less than m in the subarray must equal the number of elements greater than m. So for any subarray that includes pos, the count of elements less than m equals the count of elements greater than m. Then m will be the median.

Alternatively, another way to see it: for a subarray containing m, the median is m if and only if the number of elements less than m is equal to the number of elements greater than m. Because then, in the sorted array, m will be exactly in the middle.

Wait, let's take the example of subarray length 3 (odd). For m to be the median, there must be 1 element less and 1 greater. Then, m is the middle. If the subarray length is even (say 4), then the median is the second element. So in that case, the number of elements less than m must be equal to the number of elements greater than m. Because the sorted array would be [less, m, greater] (if counts are 1 each, but length 3, but maybe I'm mixing up). Wait, no. Let's see:

If subarray length is even: k is even. Then (k-1)//2 = (even-1)//2 → (2m-1)//2 = m-1. So in a subarray of length even (like 4), (4-1)//2 = 1. So the median is at index 1. So the sorted array's 2nd element (0-based) is the median. So how many elements less than m would there be?

If in the subarray, there are c_less elements less than m, and c_greater elements greater. Then the sorted array will have:

[ ... (c_less elements) , m, ... (c_greater elements) ]

So the position of m is c_less. For this to be equal to (k-1)//2 → since k = c_less + 1 + c_greater, (k-1) is c_less + c_greater. So (k-1)//2 = (c_less + c_greater) // 2.

So setting c_less = (c_less + c_greater) // 2. Which leads to 2c_less = c_less + c_greater → c_less = c_greater.

So regardless of whether the subarray length is even or odd, the condition is that the number of elements less than m equals the number of elements greater than m in the subarray.

That's a key insight. So the problem reduces to finding all intervals [l, r] that include pos (the position of m in the array) and in which the count of elements less than m is equal to the count of elements greater than m.

So how to compute this efficiently.

Let's split the problem into two parts: left of pos and right of pos.

We can model the elements as follows: For each element in the array, we can assign a value of +1 if it's greater than m, -1 if it's less than m, and 0 if it's m. Then, for the subarray to include pos (the position of m), and the sum of the values in the subarray must be 0 (since the number of elements greater than m (each +1) and less than m (each -1) must sum to 0, so their counts are equal).

Wait, let's see. Let's create a balance array where each element contributes to a balance. For elements greater than m, they add +1, for less than m, subtract 1. The element m itself is 0. Then, the sum of the subarray (including m's position) is equal to (number of greater elements) - (number of less elements). For this sum to be zero, we need (number of greater) = (number of less). Which is exactly the condition required.

So the problem becomes: count the number of intervals [l, r] that include pos, and have a sum of 0 in the balance array.

So this is a classic problem that can be solved with prefix sums and hash maps.

But the key is that the interval must include pos, and the sum from l to r (including pos) must be zero.

So how to approach this.

First, find the position pos where m is located.

Then, compute the prefix sums array for the balance. Let's say the balance array is B, and the prefix sum array is S, where S[0] = 0, S[i] = B[0] + B[1] + ... + B[i-1]. So the sum from l to r (1-based?) Hmm, need to get the indexing right.

Wait, the array is 1-based in the problem. So in the code, maybe it's easier to index from 0 to n-1. Let's adjust.

The balance array B will have B[i] = 0 if p[i] == m, else 1 if p[i] > m, else -1.

Then, the sum from l to r (inclusive) in B is equal to (number of elements greater than m in [l..r]) - (number of elements less than m in [l..r]).

For this sum to be zero, the counts are equal. So the sum must be zero.

Now, the sum of B from l to r is S[r+1] - S[l], where S is the prefix sum array. So we need S[r+1] - S[l] = 0 → S[r+1] = S[l].

But the interval [l, r] must include pos. So pos must be between l and r.

So the approach is to split the problem into two parts: the part to the left of pos, and the part to the right. Then, for each possible interval that includes pos, compute the sum and count the occurrences.

Wait, here's an alternative approach inspired by some prefix sum techniques.

We can compute the prefix sum array from pos to the left and to the right. Then, for any interval that starts at some l <= pos and ends at some r >= pos, the sum from l to r is the sum from l to pos plus the sum from pos+1 to r. But since the element at pos is 0, the sum from l to r is sum(l to pos-1) + sum(pos to r) = sum(l to pos-1) + sum(pos+1 to r) (since B[pos] is 0). So sum(l, r) = (sum from l to pos-1) + (sum from pos+1 to r).

But we need this total sum to be zero. So sum(l, r) = sum_left + sum_right = 0 → sum_left = -sum_right.

So, for each possible left part (from pos to the left) and right part (from pos to the right), we can track the sum of the left part and the sum of the right part. Then, the total combinations are the number of left sums and right sums that add up to zero.

But how to compute this efficiently.

Let me think:

The left part is from some l to pos-1. The sum of this part is sum_left = S[pos] - S[l], where S is the prefix sum array. The right part is from pos+1 to r. The sum_right is S[r+1] - S[pos+1].

The total sum is sum_left + sum_right = (S[pos] - S[l]) + (S[r+1] - S[pos+1]).

But B[pos] is 0, so S[pos+1] = S[pos] + 0 = S[pos]. So sum_left + sum_right = (S[pos] - S[l]) + (S[r+1] - S[pos]) ) = S[r+1] - S[l].

So for the sum to be zero, S[r+1] - S[l] = 0 → S[r+1] = S[l].

Which brings us back to the original problem: we need to count pairs (l, r) where l <= pos <= r and S[r+1] = S[l].

So the problem reduces to counting all such pairs where l is in [0, pos] and r is in [pos, n-1], and S[r+1] equals S[l].

But how to compute this efficiently.

We can precompute the prefix sums, and then for the left part (from 0 to pos), track the counts of each sum value. Then, for each position in the right part (from pos to n-1), we can check how many times the sum S[r+1] appeared in the left part.

Wait, here's a plan:

1. Find the index pos of m in the array.

2. Compute the prefix sum array S, where S[0] = 0, S[i] = S[i-1] + B[i-1]. Because the array is 0-based in Python. So for example, B is the array of -1, 0, 1, etc. So for i from 0 to n-1, S[i+1] = S[i] + B[i].

3. The interval [l, r] (0-based indices) must satisfy l <= pos <= r. The sum from l to r is S[r+1] - S[l], which must equal 0. So S[r+1] = S[l].

4. So for each possible l in 0 to pos, we can note the value of S[l], and then for each possible r in pos to n-1, check if S[r+1] equals S[l]. The total count is the sum over all such pairs.

But how to compute this efficiently.

If we precompute a frequency map for the left part (sums S[0], S[1], ..., S[pos]), and then iterate over the right part (sums S[pos], S[pos+1], ..., S[n]), and for each S[r+1], add the frequency of S[r+1] in the left part.

Wait, because the left part is l ranges from 0 to pos. So S[l] can be S[0], S[1], ..., S[pos]. Then, for each r >= pos (since r can be as small as pos, the interval [pos, pos] is allowed), S[r+1] can be S[pos], S[pos+1], ..., S[n].

So for each r in pos to n-1, we look at S[r+1], and check how many times S[r+1] appeared in the left part (sums up to S[pos]).

So the approach is:

- Create a dictionary that counts the frequency of each sum value in S[0..pos].

- Then, iterate over each r from pos to n-1 inclusive. For each such r, get the value S[r+1], and add to the total the count of times S[r+1] appears in the left part's frequency map.

This will count all pairs (l, r) where l <= pos <= r and S[r+1] = S[l].

This is O(n) time and space, which should work for n=2e5.

Yes, that seems correct.

Let's test this logic with the first example.

First example:

Input:

5 4

2 4 5 3 1

The array is [2,4,5,3,1]. So m=4 is at position 1 (0-based, since index 0 is 2, index 1 is 4).

B array:

elements less than 4 (m) are 2,3,1. Greater than 4 are 5.

So B would be:

2 is less than 4 → -1.

4 is equal → 0.

5 → +1.

3 → -1.

1 → -1.

So B = [-1, 0, 1, -1, -1]

Prefix sums S:

S[0] = 0

S[1] = 0 + (-1) = -1

S[2] = -1 + 0 = -1

S[3] = -1 + 1 = 0

S[4] = 0 + (-1) = -1

S[5] = -1 + (-1) = -2

So S array is [0, -1, -1, 0, -1, -2]

pos is 1.

Left part is S[0], S[1], S[2] (since l can be 0, 1, or 2 (since pos is 1, 0-based, and the left part is up to pos=1. Wait, the left part is l in 0..pos, where l is the start of the interval. So for the left part, S[l] can be S[0], S[1], S[2], because l can be 0 (start at 0, end at pos=1), l=1 (start at 1, end at pos=1), l=2 (start at 2, which is pos=1, but that's l=1 in 0-based. Wait, maybe I messed up the indices here. Let's recheck.

Wait, the left part is l can range from 0 to pos (inclusive). Because the interval [l, r] must include pos, so l can be as low as 0 and as high as pos (since if l is pos, then r must be >= pos). So for the left part, l can be 0, 1, or 2 (pos is 1? Wait, in the first example, pos is 1 (0-based). So l can be from 0 to 1. Wait, no. Let me recheck:

The array indices are 0-based. The array is [2,4,5,3,1]. The m is 4, which is at index 1. So pos=1.

So l can be any from 0 to 1 (since l must be <= pos). Because the interval [l, r] must include pos (1), so l <= 1 <= r.

So the left part is l in [0, 1], and r can be in [1,4] (since 0-based, the array has indices 0 to 4, so r can be up to 4).

Wait, but when l is 0, the interval starts at 0 and includes pos=1. Similarly, l can be 1. What about l=2? Then the interval starts at 2, which is after pos=1, so it can't include pos. So l can't be greater than pos.

Wait, no. Because the interval [l, r] must include pos. So l <= pos <= r. So l can be from 0 to pos, and r must be from pos to n-1.

So in the first example, pos is 1. So l can be 0 or 1. The left part is l in 0 and 1.

So the left part's S[l] are S[0] (0) and S[1] (-1), S[2] (-1). Wait, S[0] is 0, S[1] is -1, S[2] is -1. So for l=0, the interval starts at 0 (element 2), and includes pos=1. For l=1, the interval starts at 1 (element 4), which is pos. For l=2, the interval starts at 2 (element 5), which is after pos, so l=2 is not allowed. So in the first example, the left part is l=0 and l=1.

So the left part's sum is S[0], S[1], and S[2] (since l can be up to pos, which is 1, so S[0], S[1], S[2] for l=0,1,2? Wait, no. Because S is the prefix sum array. The sum from l to r is S[r+1] - S[l]. For l=0, the sum is S[r+1] - S[0]. For l=1, it's S[r+1] - S[1]. But l can be up to pos (1) because the interval must include pos. So the left part's l can be 0, 1, or 2? No. Because l is the starting index of the interval. For example, if l=2, then the interval starts at 2 (element 5), and pos is 1. So the interval [2, r] would not include pos=1. So l must be <= pos. So l can be from 0 to pos (inclusive).

Wait, in the first example, pos is 1. So l can be 0,1, but not 2.

So the left part's S[l] is S[0], S[1], and S[2]? Wait, no. Because l is the left index of the interval. For example, if l is 0, the sum is S[r+1] - S[0]. So for l=0, the interval starts at 0 and ends at r. For l=1, the interval starts at 1 and ends at r. But l must be <= pos (1). So l can be 0 or 1.

Ah, I see. So the possible l values are 0,1. So the left part's sums are S[0], S[1], S[2] (since l ranges from 0 to pos, which is 1. l can be 0,1. S[0], S[1], S[2]? Wait, no. For l=0, S[l] is S[0]. For l=1, S[l] is S[1]. For l=2, which is beyond pos, but l can't be 2. So left part's S[l] are S[0], S[1]. Wait, but why S[2]?

Wait, the left part's l can be 0 to pos. pos is 1. So l can be 0 or 1. So the S[l] values are S[0] and S[1]. But in the first example, S[0] is 0, S[1] is -1, S[2] is -1.

Wait, perhaps I made a mistake in the calculation of S. Let's recompute the prefix sums for the first example.

Original array: [2,4,5,3,1]

m=4. So B is:

2 <4 → -1

4 ==4 →0

5>4 →+1

3<4 →-1

1<4 →-1

So B array is [-1, 0, 1, -1, -1]

Prefix sum S:

S[0] = 0

S[1] = S[0] + B[0] = 0 + (-1) = -1

S[2] = S[1] + B[1] = -1 +0 =-1

S[3] = S[2] + B[2] = -1 +1=0

S[4] = S[3] + B[3] =0 + (-1) =-1

S[5] = S[4] + B[4] =-1 + (-1) =-2

So S = [0, -1, -1, 0, -1, -2]

So for l in 0 and 1:

When l=0, the sum is S[r+1] - S[0].

When l=1, the sum is S[r+1] - S[1].

But since r must be >= pos (1), the possible r's are 1,2,3,4 (0-based). So r can be from 1 to 4, inclusive.

For each r in [1,4], we look at S[r+1], which is S[2], S[3], S[4], S[5]. The values are -1, 0, -1, -2.

Now, the left part's possible S[l] values are S[0]=0, S[1]=-1, and S[2]=-1. Wait, no. Because the left part l can be 0 or 1. So l can be 0: S[0], l=1: S[1]. But l can't be 2 because that's larger than pos=1. So the left part's S[l] values are 0 and -1.

But in the code, when building the frequency map, we have to collect all S[l] for l in 0 to pos (inclusive). So for pos=1, l can be 0 and 1. So S[0], S[1], S[2]. Wait, wait, no. Because l is the start of the interval. The S array is 0-based for the prefix sum. So S[0] corresponds to the sum up to index 0 (exclusive), S[1] up to index 1 (exclusive), etc. So for the interval l to r (inclusive), the sum is S[r+1] - S[l]. So l can be any index from 0 to n. But in our case, l must be <= pos, and r must be >= pos.

So for the left part, l ranges from 0 to pos (inclusive). Because the interval starts at l and ends at r (>=pos), so l must be <= pos.

So in the first example, pos is 1. So l can be 0, 1. So the left part's S[l] values are S[0], S[1], S[2]. Wait, wait, no. Because the S array is of length n+1. For example, for n=5 elements, S has 6 elements (0 to 5). So when l is 0, it's S[0], l=1 is S[1], etc.

Wait, no. For l in 0 to pos, which is 1. So l can be 0 or 1. So S[0] and S[1] are the possible values.

But in the code, when building the frequency map for the left part, we need to include all S[l] for l in 0 to pos (inclusive). So for l in 0,1,2? No. Because pos is 1. So l can be 0,1.

So in the first example, the frequency map for the left part (S[0] and S[1]) is:

S[0] → count 1

S[1] → count 1

Wait, but S[2] is S[2] = -1. But l can be 2? No, because l can be up to pos=1. So l can't be 2.

So the frequency map in the first example has:

0: 1

-1: 1

Then, for the right part, we iterate r from pos (1) to n-1 (4). For each r, we look at S[r+1].

For r=1 (r is 1, which is pos), S[r+1] = S[2] = -1. We check how many times -1 is in the left part's frequency map. Which is 1. So this contributes 1 to the total.

Then r=2: S[3] =0. Check how many times 0 is in the left part → 1. Add 1.

r=3: S[4] =-1 → count 1. Add 1.

r=4: S[5] =-2 → count 0. So add 0.

Total so far is 1+1+1=3.

Wait, but the first example's answer is 4. Hmm. So something's wrong here.

Wait, the first example's answer is 4. So where is the missing count?

Let me recheck the code approach.

Wait, perhaps the code approach is missing some possibilities. Let's think again.

The code approach counts for each r >= pos, the number of l's <= pos such that S[r+1] = S[l]. So the total is the sum of counts for all r >= pos.

But in the first example, the answer is 4. So according to the code approach, the count is 1 (r=1) + 1 (r=2) +1 (r=3) +0 (r=4) → total 3. But the correct answer is 4.

So there's a mistake in this approach. Which suggests that the code approach is missing something.

Hmm. Let's re-examine the problem.

What's the correct answer in the first example?

The valid intervals are:

(1,3) → indices 0-based (0,2) → l=0, r=2. The sum is S[3] - S[0] =0-0=0 → yes. So this should be counted. But according to the code approach, for r=2 (0-based), S[r+1] is S[3] =0. So in the left part, S[0] is 0. So count 1.

So r=2 is included. So this interval is counted.

Another interval is (2,2) → the element [4]. The median is 4. So sum is 0. So l=1 (0-based), r=1. So S[r+1] is S[2] =-1. So look for S[l] =-1. S[1] is -1. So count is 1. So this interval is counted.

Another interval is (2,3) → elements [4,5,3]. The median is 4. The sum is (0) - S[1] = (-1) → sum is (-1) - (-1) =0. Wait, sum is S[r+1] - S[l]. For l=1 (start at 1), r=2. S[r+1] is S[3]=0. S[l] is S[1]=-1. 0 - (-1) =1 → sum is 1. So this interval's sum is 1. Which isn't zero. So why is this interval valid?

Wait, perhaps my model is incorrect.

Wait, the interval (2,3) is l=1, r=3 (0-based) in the first example's note. Wait, the note says the intervals are (1,3), (2,2), (2,3), (2,4). Let's convert them to 0-based:

Original problem's indices are 1-based. So (1,3) is l=0, r=2 (0-based). (2,2) is l=1, r=1. (2,3) is l=1, r=2. (2,4) is l=1, r=3.

So the four intervals are:

1. [0,2] (elements 2,4,5 → median 4). The balance sum is B[0] + B[1] + B[2] → -1 +0 +1=0. So sum is 0 → valid.

2. [1,1] → just 4. sum is 0 → valid.

3. [1,2] → elements 4,5. sum is 0+1=1 → sum is 1. But according to the code approach, the sum is S[r+1] - S[l]. For l=1 (S[1]=-1), r=2 (r+1=3, S[3]=0). 0 - (-1) =1. So sum is 1. But according to the problem's note, this interval is valid. But according to the code approach, it's not counted.

Hmm. This indicates that the code approach is wrong.

So what's wrong with the initial model.

Ah! Wait, the sum in the code approach is sum of B elements from l to r. For the interval [l, r], which includes pos=1 (element 4), which is B[1] =0.

So for the interval [1,2], elements 4 and 5. The sum is 0 +1=1. So the sum is 1. Which is not zero. But according to the problem's example, this interval is valid.

But according to the problem's example, the median is 4. How is that possible?

Wait, the interval [4,5] (elements 4 and 5). The sorted array is [4,5], median is the left of two elements, which is 4. So the median is indeed 4.

But in the balance sum approach, the sum is (number of greater) - (number of less) → 1 (greater) - 0 (less) =1. Which is not zero. So according to the model, this interval should not be counted. But according to the problem's example, it is counted.

So this indicates that the model is incorrect.

What's wrong here.

Ah! The model's condition is that (number of greater elements) equals (number of less elements). But in the example [4,5], there are zero less elements, and one greater. So counts are not equal. But the median is 4.

So according to the model, this interval would not be counted. But according to the problem's example, it is counted. So the model is wrong.

So the initial approach is incorrect. That's a problem.

What's the error here?

The error comes from the initial assumption that the number of elements less than m must equal the number of elements greater than m. But this is not always the case.

Let's re-examine the conditions for the median.

The median is the element at position (k-1)//2 in the sorted array, where k is the length of the interval.

In the example interval [4,5], k=2. (k-1)//2 = (1)//2 =0. So the first element in the sorted array is the median. The sorted array is [4,5], so the median is 4. So the median is m.

In this case, the number of elements less than m is zero, and the number of elements greater than m is 1. So the counts are not equal. But the median is m.

So the initial model's condition (c_less == c_greater) is not correct.

So where is the mistake in the earlier reasoning?

The initial reasoning stated that the position of m in the sorted array is c_less. And this must equal (k-1)//2. But in the case where k is even, the position is (k-1)//2. For k=2, (2-1)//2=0. So the position is 0. So m must be at position 0 in the sorted array, which requires that all elements before m are less than m, and after are greater.

But in this example, the sorted array is [4,5], so m is at position 0. So c_less is zero, which is the number of elements less than m. The condition is that c_less must equal the position. Wait, the position is (k-1)//2. So for k=2, (2-1)//2=0. So c_less must be 0. Which is indeed the case here.

So the correct condition is that c_less = (k-1)//2.

But k is the length of the interval, which is equal to c_less +1 + c_greater.

So substituting:

c_less = ( (c_less +1 + c_greater) -1 )//2 → c_less = (c_less + c_greater) //2.

Multiply both sides by 2: 2c_less = c_less + c_greater → c_less = c_greater.

But in the example where k=2, c_less=0, c_greater=1. This would imply 0=1, which is not true. But the condition here is satisfied for the median.

Wait, this suggests that the earlier conclusion is incorrect.

So the mistake was in the earlier reasoning. The condition is not c_less = c_greater, but c_less = (k-1)//2. But k = c_less +1 + c_greater.

So for the example where k=2, c_less=0. The equation becomes 0 = ( (0 +1 +1) -1 ) //2 → (1) //2=0. So 0=0, which is correct.

So the correct condition is c_less = ( (c_less + c_greater +1 -1) )//2 → c_less = (c_less + c_greater) //2.

So how to model this.

Let me re-express this. Let's denote delta = c_greater - c_less. Then the equation is:

c_less = (c_less + c_greater) //2 → 2c_less = c_less + c_greater → c_less = c_greater → delta=0.

But in the case where k is even, like k=2, c_less=0, c_greater=1, delta=1, but the equation 0=(0+1)/2 → 0=0.5//2 → 0=0. So in integer division, 0 equals (0+1)/2 → (1)/2=0. So the equation holds.

Wait, but (0+1) is 1, divided by 2 is 0.5, but integer division in Python is floor division. So (0+1)//2=0. So c_less=0 equals 0, so the condition holds.

Ah! So even though c_less and c_greater are not equal, the equation holds because of integer division.

So the model's condition is correct.

But then why does the example where c_less=0 and c_greater=1 work?

Because (c_less + c_greater) is 1, divided by 2 gives 0, which equals c_less=0.

So the equation holds, so the condition is satisfied.

But according to the model's initial approach, the sum of the balance array (c_greater - c_less) would be 1-0=1. Which is not zero. But the condition holds, so the model's approach of checking whether the balance sum is zero is incorrect.

Ah, here's the key mistake. The initial model assumes that the sum of the balance array (c_greater - c_less) must be zero. But in reality, the condition is c_less = (c_less + c_greater) //2.

So the sum of the balance array is delta = c_greater - c_less. We need to find delta such that c_less = (c_less + c_greater) //2.

But delta = c_greater - c_less → c_greater = c_less + delta.

Substituting into the equation:

c_less = (c_less + (c_less + delta)) // 2 → c_less = (2c_less + delta) //2 → 2c_less = 2c_less + delta → delta =0.

Wait, this suggests that delta must be zero. But that's not the case in the example.

What's wrong here?

Let's compute again:

delta = c_greater - c_less.

Then the equation is c_less = (c_less + c_greater) //2.

Substituting c_greater = c_less + delta:

c_less = (c_less + c_less + delta) //2 → c_less = (2c_less + delta) //2.

Multiply both sides by 2: 2c_less = 2c_less + delta → delta=0.

So this suggests that the only solution is delta=0, which would mean that c_greater = c_less.

But this contradicts the previous example where delta=1 and the equation holds.

Wait, that can't be. Let's substitute the numbers:

In the example where c_less=0, delta=1 (c_greater=1):

The equation is 0 = (0 +1) //2 → 0 =0.5 →0=0 (integer division). So yes.

But according to the substitution above, delta must be zero.

Ah, because when we substitute, we get 2c_less = 2c_less + delta → delta=0. So this suggests that the only solution is delta=0. But the example shows that delta can be 1 and the equation holds.

But why? Because when we perform integer division, (2c_less + delta) must be even in order for the division to yield c_less.

Wait, let's see:

In the example, c_less=0, delta=1.

(2c_less + delta) = 0*2 +1=1. Divided by 2 gives 0.5 → 0 in integer division. So the equation is 0=0. Which holds.

But according to the substitution, delta must be zero.

This suggests that the substitution is only valid when delta is even or when the sum 2c_less + delta is even.

So the model's initial approach of delta=0 (sum of balance array is zero) is incorrect. The correct condition is that 2c_less + delta is even and 2c_less = 2c_less + delta.

No, this is not leading anywhere.

Alternative approach: Let's think of the correct condition.

The correct condition is c_less = (k-1) //2, where k = c_less +1 + c_greater.

We need to find all subarrays [l, r] that include pos and satisfy this condition.

But how to model this.

Let's denote that the subarray has k elements. k = (r - l +1).

The position of m in the sorted subarray is (k-1)//2.

The number of elements less than m in the subarray is c_less.

So c_less must be equal to (k-1)//2.

But k = c_less + 1 + c_greater.

Substituting k into the equation:

c_less = ( (c_less +1 + c_greater) -1 ) //2 → c_less = (c_less + c_greater) //2 → 2c_less = c_less + c_greater → c_less = c_greater.

Wait, this brings us back to the initial model. But this contradicts the example where c_less=0 and c_greater=1.

So what's wrong here?

Wait, substituting the example:

c_less =0, c_greater=1.

k=0+1+1=2.

(k-1)//2 = (1)//2=0.

So c_less=0 =0 → condition holds.

But according to the equation, 2c_less = c_less + c_greater → 0=0+1 → 0=1, which is false. But why does the equation hold here?

Ah! The mistake is in the substitution. The equation is derived as:

c_less = (c_less + c_greater) //2.

In the example, 0 = (0 +1) //2 → 0=0.5//2 → 0=0.

So the equation holds, but the substitution into 2c_less = c_less + c_greater is only valid when (c_less + c_greater) is even. Otherwise, integer division causes the equation to hold even if 2c_less is not equal to c_less + c_greater.

So the initial model's approach of checking for delta=0 is incorrect. The correct condition is that (c_less + c_greater) must be even and delta=0, or it can be odd and delta=1.

Wait, no. Let's think differently.

Let's express the condition:

c_less = (c_less + c_greater) //2.

Multiply both sides by 2:

2c_less = c_less + c_greater - rem, where rem is the remainder of (c_less + c_greater) divided by 2. rem can be 0 or 1.

So 2c_less = c_less + c_greater - rem → c_less = c_greater - rem.

Which can be rewritten as:

c_greater = c_less + rem.

Since rem is 0 or 1, we have:

- If (c_less + c_greater) is even (rem=0), then c_greater = c_less.

- If (c_less + c_greater) is odd (rem=1), then c_greater = c_less +1.

But c_greater and c_less are counts of elements, so they are non-negative integers.

So, the delta between c_greater and c_less can be 0 or 1.

So the sum of the balance array, which is delta = c_greater - c_less, can be 0 or 1.

So the correct condition is that delta is either 0 or 1.

But how to model this.

For a subarray to have m as its median, the sum of the balance array must be either 0 or 1.

Because delta = c_greater - c_less can be 0 or 1.

Wait, no. Because delta can be 0 or 1.

For example:

In the case where c_less=0 and c_greater=1, delta=1. The equation holds.

In the case where c_less=1 and c_greater=1, delta=0. Equation holds.

So the sum of the balance array can be 0 or 1.

So the correct condition is that the sum of the balance array is 0 or 1.

This changes everything.

So the initial model's approach of checking for sum zero is wrong. The correct approach is to check for sum 0 or 1.

So how to adjust the model.

The balance sum for the subarray must be 0 or 1.

So for each subarray [l, r] that includes pos, we need sum(B[l..r]) ∈ {0, 1}.

So the problem reduces to counting the number of subarrays including pos where the sum is 0 or 1.

But how to compute this efficiently.

This complicates the initial approach.

So, the initial approach was to count the number of pairs (l, r) where l <= pos <= r and sum B[l..r] = 0.

Now, the sum can be 0 or 1.

So we need to count the number of pairs (l, r) where l <= pos <= r and sum B[l..r] is 0 or 1.

So the approach should be modified to account for both possible sums.

So how to compute this.

The sum of the subarray [l, r] is S[r+1] - S[l], where S is the prefix sum array.

So, for a subarray [l, r], the sum can be 0 or 1.

So S[r+1] - S[l] =0 → S[r+1] = S[l].

Or S[r+1] - S[l] =1 → S[r+1] = S[l] +1.

So for each r >= pos, we need to find the number of l's <= pos such that S[r+1] equals S[l] or S[l] +1.

So the code approach needs to track, for each r >= pos, the number of S[l] and S[l]+1 in the left part.

But how to compute this.

The initial approach used a frequency map for the left part (S[0..pos]).

For each r, we look for S[r+1] and S[r+1] -1 in the frequency map.

So for each r:

count += freq.get(S[r+1], 0)

count += freq.get(S[r+1] -1, 0)

This would cover both possibilities (sum is 0 or 1).

But this would double the work. For each r, we have to check two possible values.

In the first example, let's re-calculate with this corrected approach.

Left part's frequency map (S[0..pos=1]):

S[0] =0 → count 1

S[1] =-1 → count 1

For each r >= pos (r=1,2,3,4):

For r=1:

S[r+1] = S[2] =-1.

Check for S[r+1] = -1 and S[r+1]-1 =-2.

In the frequency map, freq[-1] is 1, freq[-2] is 0.

So contributions: 1 +0 =1.

For r=2:

S[r+1] = S[3] =0.

Check 0 and -1.

freq[0] is 1, freq[-1] is 1 → 1+1=2.

For r=3:

S[r+1] = S[4] =-1.

Check -1 and -2 →1 +0=1.

For r=4:

S[r+1] = S[5] =-2.

Check -2 and -3 →0+0=0.

Total contributions: 1+2+1+0=4 → which matches the first example's answer.

Yes! So this approach is correct.

So the correct model is to count for each r >= pos, the number of l's <= pos where S[r+1] is either S[l] or S[l]+1.

Thus, the code needs to build the frequency map for the left part (S[0..pos]) and then for each r >= pos, look up the count of S[r+1] and S[r+1]-1 in the frequency map, and sum those counts.

So the revised approach is:

1. Find pos.

2. Compute prefix sums S.

3. For the left part (S[0..pos]), build a frequency map that tracks how many times each sum occurs.

4. Iterate over each r >= pos, compute S[r+1], then add to the total the frequency of S[r+1] and the frequency of (S[r+1] -1).

This will count all subarrays [l, r] including pos where the sum is 0 or 1.

So in the first example, this correct approach yields the correct answer.

Now, let's adjust the code accordingly.

The steps are:

- Compute the balance array.

- Compute the prefix sum array S.

- Build a frequency dictionary for S[0..pos] (inclusive).

- Initialize the total to 0.

- For each r in pos to n-1:

   - current_sum = S[r+1]

   - total += frequency.get(current_sum, 0)

   - total += frequency.get(current_sum -1, 0)

- Return total.

This should give the correct count.

Now, let's test this logic with the first example.

Left part's frequency map has S[0] =0 (count 1), S[1]=-1 (count 1), and S[2]=-1 (but pos is 1, so l can be 0 or 1. So the left part is l ranges from 0 to 1. So S[0] and S[1] are in the frequency map. S[2] is not considered.

Wait, no. l can be 0,1. So the S[l] values are S[0], S[1], and S[2]?

Wait, no. The interval [l, r] must include pos. So l can be from 0 to pos (inclusive) (0-based), and r can be from pos to n-1 (inclusive).

So for the left part, l is in 0 to pos (inclusive). So for the first example, pos=1. So l can be 0 or 1.

So S[l] for l=0 is S[0], for l=1 is S[1], for l=2 is S[2], but l=2 is beyond pos=1, so it's not included.

Wait, no. l is the starting index of the interval. The interval [l, r] must include pos. So l must be <= pos and r >= pos.

So l can be 0,1 in the first example.

Thus, the left part's S[l] are S[0] and S[1].

So the frequency map for the first example is:

0: 1

-1:1.

For r=1 (0-based), r+1=2, S[2]=-1.

current_sum =-1.

Check frequency[-1] → 1.

Check frequency[-2] → 0.

Total contribution for this r is 1.

r=2 → r+1=3, S[3]=0.

Check frequency[0] →1.

Check frequency[-1] →1.

Contribution 2 → 1+1=2.

r=3 → r+1=4 → S[4] =-1.

Check frequency[-1] →1.

Check frequency[-2] →0.

Contribution 1.

r=4 → r+1=5 → S[5] =-2.

Check frequency[-2] →0.

Check frequency[-3] →0.

Contribution 0.

Total is 1+2+1+0=4 → correct.

So this approach works.

Thus, the correct code is to build the frequency map for the left part (S[0..pos]), then for each r >= pos, add the frequency of current_sum (S[r+1]) and current_sum-1.

Now, to implement this in Python.

The steps are:

- Read n, m.

- Read the array p.

- Find pos = p.index(m) (0-based).

- Compute the balance array B:

   for each element in p:

      if element == m: 0

      elif element > m: 1

      else: -1

- Compute the prefix sums S, where S[0] =0, S[i] = S[i-1] + B[i-1].

- Create a frequency dictionary for S[0], S[1], ..., S[pos].

- Iterate over r from pos to n-1, inclusive. For each r:

   current_sum = S[r+1]

   add to total the frequency.get(current_sum, 0) + frequency.get(current_sum -1, 0).

- Return total.

Now, to handle the frequency map efficiently.

We can build the frequency map by iterating from l=0 to pos, and for each l, increment the count of S[l] in the frequency map.

In Python, for large n (2e5), using a defaultdict(int) would be efficient.

Thus, the code would be:

Read n, m.

p = list(map(int, input().split()))

pos = p.index(m)

B = []

for num in p:

    if num == m:

        B.append(0)

    elif num > m:

        B.append(1)

    else:

        B.append(-1)

Compute prefix sums S.

S = [0]*(n+1)

for i in range(n):

    S[i+1] = S[i] + B[i]

Then, build frequency map for S[0], S[1], ..., S[pos].

from collections import defaultdict

freq = defaultdict(int)

for i in range(pos+1):

    freq[S[i]] +=1

Then, iterate r from pos to n-1:

total =0

for r in range(pos, n):

    current_sum = S[r+1]

    total += freq.get(current_sum, 0)

    total += freq.get(current_sum -1, 0)

print(total)

Yes.

Let's test this code with the first example.

The first example:

n=5, m=4.

p = [2,4,5,3,1]

pos =1.

B = [-1,0,1,-1,-1]

S is [0, -1, -1, 0, -1, -2]

Frequency map for S[0] to S[1] (i from 0 to 1):

S[0]=0 → count 1.

S[1]=-1 → count 1.

Then, for r=1 (inclusive) to 4:

r=0-based.

r ranges from 1 to4.

For r=1 (r=1 in code):

current_sum = S[2] =-1.

Add freq[-1] (1) and freq[-2] (0). Total +=1.

For r=2:

current_sum = S[3] =0.

Add freq[0] (1) and freq[-1] (1). Total +=2.

For r=3:

current_sum = S[4] =-1.

Add 1 (freq[-1]) and 0 (freq[-2]). Total +=1.

For r=4:

current_sum = S[5] =-2.

Add 0 (freq[-2] not present) and 0 (freq[-3] not present). Total +=0.

Total is 1+2+1+0=4. Correct.

Now, the second example:

Input:

5 5

1 2 3 4 5

pos=4 (0-based).

B array: all elements except 5 are less than 5. So B is [-1, -1, -1, -1, 0].

Prefix sums S:

S[0] =0.

S[1]=-1.

S[2]=-2.

S[3]=-3.

S[4]=-4.

S[5]=-4.

Frequency map for S[0..4] (i from 0 to 4):

S[0] =0 → count 1.

S[1]=-1 → count 1.

S[2]=-2 → count 1.

S[3]=-3 → count1.

S[4]=-4 → count1.

So freq has 0:1, -1:1, -2:1, -3:1, -4:1.

For each r from 4 to4 (since n=5):

r=4.

current_sum = S[5] =-4.

Add freq[-4] (1) and freq[-5] (0). So total +=1.

So output is 1. Which matches the example.

Third example's output is 48, but the code will handle it correctly.

Thus, the code is correct.
</think>

```python
n, m = map(int, input().split())
p = list(map(int, input().split()))
pos = p.index(m)

balance = []
for num in p:
    if num == m:
        balance.append(0)
    elif num > m:
        balance.append(1)
    else:
        balance.append(-1)

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + balance[i]

from collections import defaultdict
freq = defaultdict(int)
for i in range(pos + 1):
    freq[prefix[i]] += 1

total = 0
for r in range(pos, n):
    current = prefix[r + 1]
    total += freq.get(current, 0)
    total += freq.get(current - 1, 0)

print(total)
```