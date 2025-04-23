<think>
Okay, let's see. I need to find the smallest x such that when I add x to each element in a, modulo m, the resulting array can be permuted to match array b. Hmm.

So the approach here is to figure out what possible x's are valid, and then pick the smallest one. But how do I check if a particular x works?

For each possible x candidate, after adding x to all elements of a mod m, the resulting multiset should exactly match the multiset of b. So the problem reduces to finding the minimal x where this condition holds.

But how do I efficiently check for all possible x's? The constraints say n is up to 2000, and m can be up to 1e9. So trying every possible x from 0 to m-1 would be O(mn), which is way too slow if m is 1e9. So we need a smarter approach.

Wait, but for x to be valid, when you add x to each a_i mod m, it must match some permutation of b. Let's think: for each a_i, (a_i + x) mod m must equal some b_j. So for each a_i and b_j, the possible x is (b_j - a_i) mod m. Because x can be that difference. But then, all elements in a must have their (a_i + x) mod m be present in b, and the counts must match.

So the possible x's are the ones that can be derived from each (b_j - a_i) mod m, but only those x's that work for all elements in a. Because when you pick x, all a_i's after adding x mod m must match exactly the elements in b (counted with multiplicity).

Therefore, the possible candidates for x are the (b_j - a_0) mod m for each j in the first element of a. Wait, but perhaps considering the first a element (a_0) and possible matches in b. For example, for x to work, when we add x to a_0 mod m, it must equal some b_j. So x must be (b_j - a_0) mod m for some j. Then, for each such candidate x, we check if all a_i + x mod m can be matched to b's elements.

But since we have to check for all a elements, perhaps the correct approach is:

1. For each element in b, compute the possible x as (b_k - a_0) mod m. Then check if this x is valid for all other a_i's. That's O(n^2) time because for each possible candidate x (there are n candidates, one for each possible b element paired with a_0), check if all a_i + x mod m are in b, considering counts.

But wait, if there are multiple elements in b equal to the same value, we need to account for that. So for example, if a_0 can pair with a certain b element, but others might require different x's, but perhaps some x's are overlapping.

Wait, but the x has to be the same for all elements. So for each a_i, (a_i + x) mod m must be in the multiset of b, and the counts must exactly match.

So the approach is:

- Collect all possible x candidates from (b_j - a_i) mod m for all j and i. Then, check each candidate x to see if when applied to all a elements, the resulting array is a permutation of b. The minimal x is the answer.

But even this is O(n^2 * n log n) which for n=2000 is 2000^3 = 8e10 operations. That's way too slow.

Hmm. So this approach isn't feasible. Need a better way.

Alternative idea: For x to be valid, the multiset {(a_i + x) mod m} must be equal to the multiset {b_j}. So for each possible x candidate, we can check if this is true.

But generating all possible x candidates is impossible when m is 1e9. So the key is to find all possible x candidates that could possibly be valid, and check each one.

But how do we find those x candidates efficiently?

Wait, the x must be such that for each a_i, (a_i + x) mod m exists in the multiset of b. So for each a_i, the possible x's are (b_j - a_i) mod m for some j. But x has to be the same across all a_i's. So for x to be valid, it must be that for each a_i, (a_i + x) mod m is present in the multiset of b, and the counts are exactly matched.

So the possible x's must be in the intersection of all possible (b_j - a_i) mod m for each a_i. But that's not exactly correct. Because for a_i, the x can be any (b_j - a_i) mod m, but for all a_i's, the x must be such that (a_i + x) mod m is in the multiset of b. But each a_i's x is same, so for x to work, for each a_i, (a_i +x) must be congruent mod m to some element in b. So the x must be (b_j - a_i) mod m for some j for each a_i. But that's not possible unless all a_i's have x such that the same x is (b_j - a_i) mod m for different j's.

Wait, perhaps the x is determined by the difference between a particular a_i and some b_j, but for all a_i's. So, for example, consider the first a element, a_0. For x to be valid, x must be (b_j - a_0) mod m for some j. Then, for all other a_i's, (a_i + x) mod m must be present in the multiset of b (with correct counts).

So the candidate x's are the possible (b_j - a_0) mod m, for all j. Then, for each of these x candidates, check if the transformed a array (each element (a_i +x) mod m) is a permutation of the b array.

But why the first element? Because if x is valid, then x must be (some b_j - a_0) mod m, where j is the position that a_0's transformed value matches. So the x candidates come from the possible differences between a_0 and each b_j. Then, for each such x, check if all other a_i's plus x mod m are present in b.

This reduces the possible x candidates from O(n^2) to O(n) possibilities. For each x candidate (n possibilities), check if the transformed a array matches b as a multiset.

But checking each x candidate would require O(n) time to check all elements. Wait, no: for each x, we need to check that the multiset of (a_i +x) mod m is exactly the multiset of b. So how to do this efficiently?

We can pre-sort the b array. Then, for each x candidate, compute the transformed a array, sort it, and compare to the sorted b array. If they are the same, then x is a valid candidate.

The steps would be:

1. Sort the array b. Also, count the frequency of each element in b (but sorting is easier for comparison).

2. For each element b_j in b:

   a. Compute x_candidate = (b_j - a[0]) mod m.

   b. Compute all (a_i + x_candidate) mod m, sort them, and see if they match the sorted b array.

3. Among all valid x_candidates, choose the smallest one.

But since we need the minimal x, we can collect all valid x candidates and pick the smallest.

But the problem is that for n up to 2000, each x candidate requires O(n log n) time (sorting the transformed a array and comparing to sorted b). So for n=2000, each iteration is O(2000 log 2000) which is manageable. And since there are up to 2000 x candidates, the total time is O(n^2 log n), which for 2000 is 2000^2 * log 2000 ≈ 4e6 * 11 = ~44 million operations. That's acceptable for Python, as 3 seconds can handle that.

Wait, but 44 million operations in Python can be a bit tight. Let's see: for each x_candidate, we need to generate a new array, compute (a_i +x) mod m for each element, then sort it, then compare to sorted_b. So for 2000 elements, each sort is O(n log n), which for 2000 is about 2000 * 11 = 22,000 steps. Multiply by 2000 candidates gives 44 million steps, which should be manageable within 3 seconds, but perhaps there's a way to optimize.

Alternatively, maybe we can pre-sort the transformed arrays in a clever way. For example, if we pre-sort the original a array and the b array. Then, for a given x_candidate, the transformed a array would be (a_i + x) mod m. But mod m complicates things. However, when sorted, the transformed a array would have elements that can wrap around (like if adding x pushes some elements over m, so mod m brings them back to 0, etc).

Wait, but for each x_candidate, the transformed a array is (a_i + x) mod m. Let's sort this array. The sorted transformed array must equal the sorted b array.

So, the steps would be:

- Sort the original b array into sorted_b.

- For each x_candidate (based on a[0] and each b_j):

   a. Compute transformed_a = [(a_i + x_candidate) % m for all i]

   b. Sort transformed_a and compare to sorted_b.

   c. If equal, record x_candidate as a possible solution.

Then, among all possible x_candidates, pick the smallest one.

But how to generate the x_candidates correctly? For the first a element (a[0]), the x_candidate must be such that (a[0] + x_candidate) mod m is equal to some element in b. So x_candidate can be (b_j - a[0]) mod m for each j. But since the problem states that a solution exists, there must be at least one x_candidate that works.

So the plan is:

1. Sort the b array.

2. Sort the a array.

Wait, wait. Wait, no. Because the transformed a array's sorted version must equal the sorted b array. So regardless of how the elements are arranged, after sorting, they must match. Therefore, we can pre-sort the b array once. Then, for each x_candidate, compute the transformed a array, sort it, and compare to the sorted b array.

But for each x_candidate, the transformed a array is (a_i + x_candidate) mod m. Then, when sorted, it must match sorted_b.

So, the steps are:

- Precompute sorted_b = sorted(b)

- For each j in 0..n-1:

   x_candidate = (b[j] - a[0]) % m

   transformed_a = [(a_i + x_candidate) % m for all i]

   sorted_transformed = sorted(transformed_a)

   if sorted_transformed == sorted_b:

      collect x_candidate

- Then, among all collected x_candidates, return the minimal one.

But wait, the x_candidate is derived from a[0] and each b[j]. But since after adding x, the transformed a array must have all elements in b (after permutation), the a[0] + x mod m must be one of the elements in b. So by generating x_candidates as (b[j] - a[0]) mod m, we cover all possible x's that could work for a[0], which is necessary for the x to be valid. Because if x is valid, then a[0] +x mod m must be present in b, hence x must be (b_j - a_0) mod m for some j. Therefore, all possible valid x's must be among the candidates generated from the first element and each possible element in b.

So this approach covers all possible x's that could be valid, and we can check each one in O(n log n) time.

But wait, what if there are multiple j's where b[j] is the same? For example, if b has multiple elements equal to some value. Then, the same x_candidate would be generated multiple times. So in that case, we can deduplicate the x_candidates before checking them. But since the problem allows x to be minimal, we can process the x_candidates in sorted order and return the first one that works. Alternatively, we can collect all possible x_candidates and then pick the minimal one.

So the steps in code:

Read n, m.

Read a array.

Read b array.

sorted_b = sorted(b)

Generate all x_candidates as (b_j - a[0]) mod m for each j in 0..n-1. But since there might be duplicate x_candidates, we can deduplicate them to avoid redundant checks.

Sort the list of x_candidates (with deduplication), and then check each in ascending order. The first one that works is the minimal x.

Wait, but deduplication is necessary because if two j's generate the same x_candidate, we don't need to check it twice. So for example, if multiple elements in b are the same, then (b_j - a[0]) mod m could be the same for those j's. So deduplicate the x_candidates.

Then, for each x_candidate in the sorted (and deduplicated) list, check if the transformed a array sorted is equal to sorted_b. The first such x_candidate (since sorted in increasing order) is the minimal x.

But wait, the x_candidates are (b_j - a[0]) mod m. So when sorted, they could be in any order. But when mod m is applied, the actual x is considered as non-negative, so (b_j - a[0]) mod m gives a value between 0 and m-1. So to get the minimal x, we need to find the smallest x_candidate in the list.

But how to sort the x_candidates in ascending order? For example, if x_candidate is (b_j - a_0) mod m, which could be (say) m-1 if (b_j - a_0) is negative. But the minimal x is the one with the smallest value.

So for example, x=0 is better than x=1, etc. So when generating x_candidates, after mod m, they are in 0 to m-1. So we can collect all unique x_candidates, sort them in ascending order, and check each in order. The first x that works is the minimal possible.

So the algorithm steps:

1. Precompute sorted_b = sorted(b)

2. Generate all possible x_candidates: for each j in 0..n-1, x = (b[j] - a[0]) % m. Collect all these x values, then deduplicate and sort them in ascending order.

3. For each x in the sorted x_candidates list:

   a. Compute transformed_a as (a_i + x) % m for each a_i in a.

   b. Sort transformed_a and compare to sorted_b.

   c. If equal, return x as the answer.

Since the problem states that there is at least one x that works, we can return the first x in the sorted list that satisfies the condition.

Now, the question is, how efficient is this approach?

The deduplication step would process up to n x_candidates. For n=2000, that's manageable. Then, sorting the x_candidates (after deduplication) would take O(k log k), where k is up to 2000. Then, for each x in the sorted list, we process O(n) elements (transform each a_i), sort them (O(n log n)), and compare. So for each x, the steps are O(n + n log n). For 2000 x candidates (worst case), this would be 2000 * (2000 + 2000 log 2000) ≈ 2000*(2000 + 2000*11) = 2000 * (24000) = 48,000,000 operations. That's acceptable for Python.

But perhaps we can optimize further.

Wait, but in practice, the number of unique x_candidates can be up to n, which is 2000. So the worst case is 2000 checks, each taking O(n log n) time.

But in the sample input:

First example:

n=4, m=3, a = [0,0,2,1], b = [2,0,1,1].

The sorted_b is [0, 1, 1, 2].

The x_candidates are (b[0]-a[0]) mod 3 = (2-0) mod3=2; (0-0) mod3=0; (1-0) mod3=1; (1-0) mod3=1. So unique x_candidates are 0,1,2. Sorted order is 0,1,2. Now, for x=0:

transformed a is [0,0,2,1] mod3 → sorted is [0,0,1,2], which doesn't match sorted_b [0,1,1,2].

x=1: transformed a is [1,1,0,2] → sorted [0,1,1,2] which matches sorted_b. So returns 1.

So the algorithm works.

Another example:

Sample input 2: n=3, m=2.

a = [0,0,0], b = [1,1,1].

x_candidates are (1-0) mod2=1, (1-0) mod2=1, (1-0) mod2=1. So unique x is 1. Check x=1: transformed a is [1,1,1] mod2 → [1,1,1], sorted matches sorted_b. So returns 1.

Third sample: a is [0,0,0,1,2], b is [2,1,0,0,0]. sorted_b is [0,0,0,1,2]. For x_candidates, a[0] is 0. So each x_candidate is (2-0) mod10=2, (1-0) mod10=1, (0-0) mod10=0, etc. So x_candidates are 2,1,0,0,0. Unique sorted as 0,1,2. Check x=0: transformed a is [0,0,0,1,2], sorted is same as sorted_b. So returns 0.

So the algorithm works for the samples.

Now, code steps:

Read n and m.

Read a as a list of integers.

Read b as a list of integers.

sorted_b = sorted(b)

Generate the x_candidates:

x_candidates = set()

for each b_j in b:

   x = (b_j - a[0]) % m

   x_candidates.add(x)

Then, sorted_x = sorted(x_candidates)

For each x in sorted_x:

   transformed = [(ai + x) % m for ai in a]

   sorted_transformed = sorted(transformed)

   if sorted_transformed == sorted_b:

      print(x)

      exit()

But why? Because the first x in sorted order that meets the condition is the smallest possible x.

Yes.

Now, code in Python.

But wait, for the transformed list, we can generate it as a list, then sort it, then compare to sorted_b.

But in Python, list comprehensions are efficient.

But for n=2000, each iteration is manageable.

Now, code:

Read the input.

n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

sorted_b = sorted(b)

x_candidates = set()

first_a = a[0]

for bj in b:

    x = (bj - first_a) % m

    x_candidates.add(x)

for x in sorted(x_candidates):

    transformed = [(ai + x) % m for ai in a]

    if sorted(transformed) == sorted_b:

        print(x)

        exit()

Wait, but according to the problem statement, there's a solution, so the code will always find one. So no need to handle the case where no x is found.

This code should work.

Testing the first sample:

Sample 1:

a = [0,0,2,1], first_a is 0. For each bj in [2,0,1,1], x candidates are (2-0) mod3=2, (0-0) mod3=0, (1-0) mod3=1, (1-0) mod3=1. So x_candidates are {0,1,2}. Sorted as 0,1,2.

Check x=0: transformed a is [0,0,2,1]. sorted [0,0,1,2] vs sorted_b [0,1,1,2] → no.

x=1: transformed [1,1,0,2] → sorted [0,1,1,2] → yes. So output 1.

Sample 2:

n=3, m=2. a = [0,0,0], first_a=0. b is [1,1,1]. x_candidates are (1-0) mod2=1, 1,1. So x_candidates {1}. sorted is [1]. Check x=1: transformed is [1,1,1] → sorted matches.

Sample3:

a is [0,0,0,1,2], first_a is 0. b is [2,1,0,0,0]. So sorted_b is [0,0,0,1,2]. x_candidates from each bj:

2-0 mod10=2, 1-0 mod10=1, 0-0 mod10=0, 0-0=0, 0-0=0. So x_candidates {0,1,2}. Sorted as 0,1,2. Check x=0: transformed a is [0,0,0,1,2] → sorted matches sorted_b. So output 0.

So code works for samples.

Now, edge cases. For example, when all elements are the same. Or when x is m-1. Or when m is 1. Wait, if m=1, then all a and b elements are 0 mod1. So x can be 0, since all (a_i +x) mod 1 is 0. So code should handle that.

Another test case: n=1. Then a has one element, and b has one. x_candidate is (b[0] - a[0]) mod m. Then check if transformed a[0] mod m equals b[0], which it does, so x is that.

So the code is correct.

Now, regarding Python's speed. For n=2000, each iteration is O(n log n) for the sorted. In Python, sorting 2000 elements is quick. So even 2000 iterations would take acceptable time.

But let's think: for each x_candidate, the transformed array is generated as a list comprehension. Then sorted. Then compared.

Yes.

Thus, this code should work efficiently and correctly.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sorted_b = sorted(b)
first_a = a[0]
x_candidates = {(bj - first_a) % m for bj in b}
for x in sorted(x_candidates):
    transformed = [(ai + x) % m for ai in a]
    if sorted(transformed) == sorted_b:
        print(x)
        exit()
```