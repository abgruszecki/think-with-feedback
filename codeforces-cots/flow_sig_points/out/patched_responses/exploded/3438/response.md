<think>
Okay, let's see. So the problem is about partitioning a permutation into k segments such that the sum of the maximums of each segment is maximized, and then finding how many ways there are to do this. Hmm.

First, I need to understand how to approach this. Since it's a permutation, all elements are distinct. So the maximums in the segments are going to be some subset of the largest elements in the permutation. Oh right, because to maximize the sum, we want the k largest elements each to be the maximum of their own segments. Because adding a larger element as a maximum contributes more to the sum than a smaller one. So the maximum sum would be the sum of the top k elements in the permutation. That makes sense.

So the first part of the problem is easy: the maximum possible partition value is the sum of the k largest elements in the permutation. But then we have to count the number of ways to split the permutation into k segments such that each of these top k elements is the maximum in their respective segments, and the positions of these top k elements must allow the partitioning into exactly k segments.

Wait, right. Because the order of these elements in the permutation matters. For example, if the top k elements are all consecutive, then splitting them into individual segments would require that each is in a separate segment, but how exactly?

Let me think. Let's collect the indices of the top k elements. Let's sort them in the order they appear in the permutation. Let's call these positions pos_1, pos_2, ..., pos_k. These positions must be the maximums of their segments. Since each segment's maximum is the maximum in that segment, for the top k elements, each must be in a different segment. Also, since the permutation is a permutation, any segment containing one of these top k elements must have that element as its maximum. So the way to split the permutation into k segments is such that each segment contains exactly one of the top k elements, which is the maximum of that segment.

But how do the positions of these top k elements affect the possible partitions? For example, the segments must be non-overlapping and cover the entire array. So the first segment must start at 1 and end at pos_1, or include pos_1 as its maximum. Wait, no. Let's think again. The top k elements must be the maximums of their segments. So for each of these top k elements, their positions in the permutation must be such that each is the maximum in their respective segment. So the segments must be arranged such that each of these elements is in a separate segment. Moreover, the segments must be ordered such that their starting and ending positions form a partition of the array into k consecutive intervals.

So the key idea here is that the top k elements must be arranged in the permutation in such a way that when sorted by their positions, the positions are in increasing order, and the gaps between them determine the possible places to split. For example, between pos_i and pos_{i+1}, there are some elements, and the split between the i-th and (i+1)-th segments must be between pos_i and pos_{i+1}.

Wait, more precisely: the top k elements' positions, when sorted, form an increasing sequence. The split points are between these positions. The number of ways to split between pos_i and pos_{i+1} is (pos_{i+1} - pos_i). Because the i-th segment can end anywhere between pos_i and pos_{i+1} - 1, but wait, maybe that's not right. Let's take an example.

Take the first sample input: 3 2, permutation [2,1,3]. The top 2 elements are 3 and 2. Their positions are 3 and 1. So sorted positions are [1,3]. The splits are between the first and second elements. So the split must occur between position 1 and 3. The possible splits are between 1 and 2, or between 2 and 3. So the number of ways is (3-1) = 2. Which matches the sample output.

So the general approach is: 

1. Find the k largest elements in the permutation. Sort their positions in increasing order. Let's call this list sorted_positions.

2. The maximum sum is the sum of these elements.

3. The number of valid partitions is the product of (pos_{i} - pos_{i-1}) for i from 2 to k. Because between each pair of consecutive top elements (sorted by position), the split can be made anywhere in the gap between them. So for each such gap, the number of possible splits is (pos_{i} - pos_{i-1}).

Wait, let's think again. Suppose sorted_positions is [a_1, a_2, ..., a_k]. For the partitions to have exactly k segments, each containing exactly one of the top k elements as their maximum, the splits must occur between a_1 and a_2, a_2 and a_3, etc. 

For example, the first segment must end at a_1. The next segment starts at a_1 + 1. Then between a_1 and a_2, there are (a_2 - a_1) possible positions to split. Because the first split can be made after any position up to a_2 - 1. Wait, perhaps not. Let's think: between a_1 and a_2, the split between the first and second segment must be between a_1 and a_2-1. Because the second segment starts at a_1 +1 (if split is after a_1), but the second segment's maximum is a_2, which must be in that segment. So the split between the first and second segment can be anywhere after a_1 but before a_2. So the number of possible splits between a_1 and a_2 is (a_2 - a_1) ways. Similarly, between a_{i-1} and a_i}, there are (a_i - a_{i-1}) possible splits.

Wait, for the first split between a_1 and a_2: the first segment can end anywhere from a_1 to a_2 -1. Then the second segment starts at the next position. So the number of options is (a_2 - a_1) ways. Then the same applies for each consecutive pair. So the total number of partitions is the product of (a_i - a_{i-1}) for each i from 2 to k.

Yes, that makes sense. Because each of these gaps contributes a multiplicative factor to the total number of ways.

So the algorithm steps are:

- Find the k largest elements in the permutation.

- Collect their positions and sort them in increasing order.

- Compute the product of (sorted_pos[i] - sorted_pos[i-1]) for i from 1 to k-1 (since the list is zero-based). Wait, no. If sorted_pos is a list of length k, then i runs from 1 to k-1. Because the pairs are (sorted_pos[0], sorted_pos[1]), (sorted_pos[1], sorted_pos[2]), ..., (sorted_pos[k-2], sorted_pos[k-1]). So the product is the product of (sorted_pos[i] - sorted_pos[i-1]) for i in 1..k-1.

Then, multiply all these differences together modulo 998244353.

So the first part is summing the k largest elements, which is straightforward. The second part is multiplying the gaps between consecutive positions (sorted) of these elements.

But wait, the problem states that the permutation is a permutation of 1..n. So the elements are distinct, and the k largest elements are just the elements from (n - k +1) to n. Wait, no. Wait, permutation is a permutation of 1..n, so the k largest elements are n, n-1, ..., n -k +1. So the sum of these is n + (n-1) + ... + (n -k +1) which is k*(2n -k +1)/2. But perhaps it's easier to just collect the top k elements and sum them.

But in code, since the permutation is given as a list of numbers, perhaps we can collect the k largest elements by value, sort them, and sum them. But given that the permutation is unique, we can find the indices of the top k elements.

So for example, for the sample input 3 2, the permutation is [2,1,3]. The top 2 elements are 3 and 2. Their positions are 3 and 1. Sorted positions are [1,3], so the product is (3-1) = 2. Which matches the sample.

Another sample: input 5 5. The permutation is [2,1,5,3,4]. The top 5 elements are all elements (since k=5). So their positions are sorted as [1,2,3,4,5]. The product is (2-1)*(3-2)*(4-3)*(5-4) = 1*1*1*1=1. So the count is 1.

Which matches the sample.

The third sample: permutation [2,7,3,1,5,4,6], n=7, k=3. The top 3 elements are 7,6,5. Wait, wait. Let's see the elements: 2,7,3,1,5,4,6. So the elements are 2,7,3,1,5,4,6. The top 3 elements are 7 (value 7), 6 (value 6), and 5 (value 5). Their positions are 2,7,5. Sorted positions are [2,5,7]. The gaps are 5-2=3 and 7-5=2. So product is 3*2=6, which matches the sample.

So the approach works.

Now, the steps for the code are:

1. Read n and k.

2. Read the permutation array p.

3. Find the indices of the top k elements.

But since the permutation is a permutation of 1..n, the top k elements are the numbers from (n -k +1) to n. Because for example, in the third sample, n=7, k=3. The top 3 elements are 7-3+1=5, so 5,6,7. Wait, but in the sample, the elements are 2,7,3,1,5,4,6. So the top 3 elements are 7,6,5. Which are 7,6,5. So n=7, (n -k +1) is 7-3+1=5. So the top elements are 5,6,7. But in the permutation, the elements are 7,5,6. So their positions are 2,5,7. So yes, the top k elements are the largest k elements, which are n, n-1, ..., n -k +1.

Wait, but in the third sample, 5 is the third largest. So in general, the top k elements are the k largest in the permutation, which is the numbers from (n -k +1) to n. So in the third sample, n=7, k=3: the top 3 elements are 7,6,5.

So to find their positions, we can create a list where for each value from (n -k +1) to n, we find their index in the permutation array.

But since the permutation is a permutation, each value from 1 to n appears exactly once. So we can create a dictionary or a list that maps the value to its index.

So in code:

- Create a list pos where pos[v] is the index (1-based?) of the value v in the permutation array. Wait, in the problem statement, the permutation is given as p_1 to p_n. So the positions are 1-based? Because in the first sample input, the permutation is [2,1,3], which are p_1=2, p_2=1, p_3=3. So the positions of the top 2 elements (3 and 2) are 3 and 1. So yes, the positions are 1-based.

So, for the code, the steps are:

- Read the permutation as a list.

- For each value from (n -k +1) to n, find their positions in the permutation.

But wait, perhaps the values are not sorted in the permutation. So the order is not necessarily consecutive. Wait, no. The permutation is a permutation of 1..n, but the elements can be in any order. The top k elements are the k largest, which are the numbers from (n -k +1) up to n, but when ordered in decreasing order. For example, when k=3 and n=7, the top 3 elements are 7,6,5. So to get the top k elements, we can collect the numbers in the permutation that are >= (n -k +1). Then take the top k of them. Wait, but since it's a permutation, all numbers from 1 to n are present. So the top k elements are exactly the numbers (n -k +1) to n. Because those are the k largest numbers in 1..n. So to find their positions, we can iterate through the permutation and collect the positions of all numbers >= (n -k +1). Then, since there are exactly k of them, collect their positions and sort them.

So in code:

max_sum = sum of (n, n-1, ..., n -k +1) → which is sum(range(n -k +1, n+1)) → that's an arithmetic series. The sum is k*(n + (n -k +1)) // 2 → but in code, perhaps it's easier to compute as sum(range(n -k +1, n+1)).

But since the permutation can have these elements in any order, but their values are exactly the top k elements. So for each element in p, if it is >= (n -k +1), then it's part of the top k elements. So collect their positions (indices +1, since the input is 1-based?), then sort those positions.

Once sorted, compute the product of (sorted_pos[i] - sorted_pos[i-1]) for i from 1 to k-1.

So the code steps:

Read n and k.

Read p as a list of integers.

Compute threshold = n -k + 1.

Collect all positions (i+1, since indices are 0-based in Python) where p[i] >= threshold.

Sort these positions.

Compute the product of (positions[i] - positions[i-1]) for i in 1 to len(positions)-1.

But wait, len(positions) must be exactly k. Because the permutation is a permutation, so each of the k elements (n -k +1, ..., n) is present once. So the length is k.

So the code can proceed safely.

Then, the answer is sum of the top k elements (which is sum of numbers from n -k +1 to n) and the product modulo 998244353.

Wait, no. Because the sum is the sum of the top k elements, which are exactly the numbers n, n-1, ..., n -k +1. So the sum is (k) * (n + (n -k +1)) // 2.

But in code, perhaps it's easier to compute this as (k*(2n -k +1))//2.

But in Python, it's straightforward to compute the sum of the top k elements. Alternatively, we can generate the sum as the sum of the elements in the list [n - i for i in range(k)] ] → no, wait. Let's see:

n = 7, k=3 → elements 7,6,5 → sum 18.

Which is (7+6+5) = 18. The formula (3*(7 +5 )) / 2 → 3*12/2 = 18. So yes.

So the sum is (k*(n + (n -k +1)))//2.

But when implementing, perhaps it's better to compute it as sum of the top k elements. But since the code needs to process the permutation, but the sum doesn't depend on the permutation. Because the top k elements are fixed as the values from n-k+1 to n. So the sum is the sum of those numbers, regardless of their positions in the permutation.

So the maximum partition value is fixed as the sum of the top k elements. Then the count is the product of the gaps between their sorted positions.

So for the code:

sum_value = (k*(n + (n -k +1))) // 2

But in code:

sum_value = sum(range(n, n -k, -1))

Which is the same as sum of n, n-1, ..., n -k +1.

So for example, n=3, k=2: sum(3, 2) →5. Which matches the first sample.

Yes.

Now, the code steps:

Read n, k.

p = list of integers.

Compute the threshold = n -k +1.

positions = list of (i+1) for i in range(n) if p[i] >= threshold.

Sort positions.

Compute product:

res = 1

for i in range(1, k):

    res *= (positions[i] - positions[i-1])

    res %= 998244353

Then output sum_value and res.

But wait, in the first sample, the positions are [1,3], sorted. The product is 3-1=2. Which is correct.

Yes.

So the code should be straightforward.

Now, considering the constraints: n can be up to 2e5. So the code needs to process that quickly.

The steps are O(n) time for collecting the positions, O(k log k) time for sorting the positions (since k can be up to n, but in the problem statement k can be up to n, but when k=n, the product is 1 (each element is its own segment). So for example, when k=5 and n=5, the positions are 1,2,3,4,5, sorted. The product is (2-1)*(3-2)*...*(5-4)=1*1*1*1=1.

So the code should handle this.

But for n up to 2e5, the code is acceptable. Because collecting the positions is O(n), sorting is O(k log k), which for k up to 2e5 is O(2e5 log 2e5) which is manageable.

But wait, when k is 2e5, the code will collect 2e5 positions and sort them. The sort time is O(k log k), which is 2e5 * 20 → around 4e6 operations. Which is acceptable.

So the code is efficient.

Now, let's test the code against the samples.

First sample:

3 2

2 1 3.

threshold = 3 -2 +1 = 2. So collect positions where p[i] >= 2. The elements are 2,1,3. So the positions (1-based) are 1,3. Sorted as [1,3]. Product 3-1=2. Sum is 3+2=5.

Which matches.

Second sample:

5 5.

threshold =5-5+1=1. So all elements are included. Positions are [1,2,3,4,5]. Product is (2-1)*(3-2)*(4-3)*(5-4) = 1. Sum is 5+4+3+2+1=15. Correct.

Third sample:

7 3.

threshold =7-3+1=5. So collect elements >=5. The elements in the permutation are 2,7,3,1,5,4,6. So elements >=5 are 7,5,6. Their positions are 2,5,7. Sorted. The product is (5-2)*(7-5) =3*2=6. Sum is7+6+5=18. Correct.

So the code works for the samples.

Now, edge cases.

What if k=1. Then threshold is n. So only the element n is in the list. So positions sorted is [pos_of_n]. Product is 1 (since there are no gaps). So the answer is sum(n) =n, and 1. Which is correct. Because the entire array is a single segment, so only one way.

Another edge case: n=1, k=1. The permutation is [1]. Sum is 1, product 1. Correct.

Another case: when the sorted positions are [a1, a2, ..., ak], where each consecutive pair is adjacent. For example, positions [3,4,5]. Then the product is (4-3)*(5-4) =1*1=1. So one way.

So the code seems correct.

Now, code implementation in Python.

Read n and k.

Read the permutation as a list.

Compute threshold =n -k +1.

Collect positions as 1-based indices.

Sort positions.

Compute the product of differences between consecutive positions modulo 998244353.

Sum the sum of the top k numbers, which is sum of (n -k +1) to n.

Now, in Python, for the sum, since the numbers are a consecutive sequence, it's more efficient to compute it using the formula for arithmetic series sum.

sum_value = (k * (n + (n -k +1))) // 2.

But in code, for example:

sum_val = (k * (n + (n -k +1))) // 2

But we can also compute it as sum(range(n, n -k, -1)).

Which is more efficient? For large k, sum(range(...)) is O(k), which is O(2e5) steps. The formula is O(1), so better to use the formula.

Yes.

So code:

n, k = map(int, input().split())
p = list(map(int, input().split()))
MOD = 998244353

if k ==0:
    # but according to constraints, 1<=k <=n, so this is not possible.
    pass

threshold = n -k +1

positions = []
for idx, val in enumerate(p):
    if val >= threshold:
        positions.append(idx+1)  # 1-based positions

positions.sort()

product = 1
for i in range(1, k):
    product = (product * (positions[i] - positions[i-1])) % MOD

sum_val = k * (n + (n -k +1)) // 2

print(sum_val, product)

Yes.

Testing this code against the samples.

First sample:

n=3, k=2. threshold=3-2+1=2.

p is [2,1,3].

positions: 2 is in index 0 (1-based pos 1), 1 is index 1 (pos 2) but val 1<2. 3 is index 2 (pos3, val3>=2). So positions are [1,3]. sorted.

product is 3-1=2. sum_val is 2*(3 + (3-2 +1)) / 2 → 2*(3+2) /2 = 5. Correct.

Second sample:

n=5, k=5. threshold=5-5+1=1. All elements are included. positions sorted are 1,2,3,4,5. product is 1. sum_val is 5+4+3+2+1=15. Correct.

Third sample: sum_val is 3*(7 +5)/2 →3*(12)/2=18. Correct.

So the code works.

Now, for the permutation with k=3 and elements in positions [5, 2, 7], etc. the code would sort them and compute the product correctly.

I think this is the correct approach.
</think>

```python
n, k = map(int, input().split())
p = list(map(int, input().split()))
MOD = 998244353

threshold = n - k + 1
positions = []
for idx, val in enumerate(p):
    if val >= threshold:
        positions.append(idx + 1)  # 1-based index

positions.sort()

product = 1
for i in range(1, k):
    product = (product * (positions[i] - positions[i-1])) % MOD

sum_val = k * (n + (n - k + 1)) // 2

print(sum_val, product)
```