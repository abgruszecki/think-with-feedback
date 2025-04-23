<think>
Okay, let's see. The problem is to find, for each query k and pos, the element at position pos in the optimal subsequence of length k. The optimal subsequence is the one with maximum sum, and among those, lexicographically smallest. Hmm.

So first, for each query (k_j), we need to construct this optimal subsequence and then answer the pos_j-th element. The challenge is to find an efficient way to compute this subsequence for multiple queries.

Let's think about how to construct the optimal subsequence. The optimal subsequence must have the maximum possible sum. But then, among all possible subsequences with that sum, we need the lexicographically smallest one. Wait, lexicographical order here is determined by the elements in the subsequence. So, lex order is about the earliest position where there's a difference. So even if two subsequences have the same sum, the lex order would pick the one that is lex smaller.

But how do we find such a subsequence? Let's think about the steps. For a given k, the optimal subsequence is built by selecting elements in a way that first maximizes the sum, then ensures lex order.

So, the approach would be similar to selecting the elements in a way that we pick the largest elements possible, but when there are multiple options for a certain element, we choose the earliest possible occurrence to ensure lex order. Wait, no. Wait, lex order for the subsequence. Let's see, the lex smallest subsequence among all maximum sum subsequences. For example, if two elements are equal in sum, but choosing earlier elements in the array allows for a lex smaller subsequence. Hmm.

Wait, let's take an example. Suppose the array is [10, 20, 10], and k=2. The maximum sum is 30. The possible subsequences are [10,20], [10,10], [20,10]. The sum for the first and third is 30, the second is 20. So the optimal is between [10,20] and [20,10]. The lex order here would pick [10,20] because in the first position, 10 is less than 20? Wait, no. Wait lex order compares elements from left to right. So [10,20] is lex smaller than [20,10] because at the first position, 10 < 20. So the lex minimal is [10,20]. But that's the correct answer for the first example.

Wait in the first example's note, for k=2, the optimal subsequence is [10,20]. But why? Because sum is 30, which is the maximum. Then among all such subsequences (which are [10,20], [20,10], etc.), the lex smallest is [10,20]. But wait, how are the positions considered here? Because the original array is [10,20,10], the subsequence [10,20] is formed by elements at positions 1 and 2. The [20,10] is positions 2 and 3. So sum is same. Then lex order: comparing the two subsequences, the first element of [10,20] is 10 vs 20 in [20,10], so [10,20] is lex smaller. Wait, but lex order is determined by the elements, not their positions. So even if the elements are same, their positions in the original array don't matter for lex order. Wait no. The lex order is based on the elements in the subsequence. So, for example, two different subsequences with same elements in same order are considered equal, but the positions in the original array are irrelevant. So the lex order is purely based on the elements in the subsequence's order.

Wait, so to find the lex minimal subsequence among all with maximum sum, when there are multiple options, we need to pick the one that has the earliest possible smaller element. So for example, if there are two possible elements to choose next, but one is smaller than the other, even if the rest can form a valid subsequence, we need to pick the smaller one if that's possible. Wait, but that's conflicting with the sum. Because the sum is already maximum. So once the sum is maximum, how do we choose the lex smallest.

Wait the process is: first, select the elements that give the maximum sum. Then, among all such subsequences, select the lex smallest one.

So how to construct such a subsequence?

Let's think of the approach for selecting the lex smallest maximum sum subsequence of length k.

One approach is to model this as a greedy selection. Let's say we need to select k elements. We need to select them in such a way that each step chooses the earliest possible element that allows the remaining elements to form a subsequence of the required length, and that contributes to the maximum sum.

Alternatively, the standard approach for such problems is to model it as selecting elements in a way that for each position in the subsequence, we pick the smallest possible element (to get lex order), but only if that element is part of some maximum sum subsequence.

Wait, here's a possible approach:

The lex smallest subsequence among the maximum sum subsequences can be constructed by greedily choosing the earliest possible elements when there's a choice.

Wait, let's think of the selection process. For each step from 1 to k, we need to select the next element in the subsequence. The idea is that, for the current position in the subsequence, we select the earliest element in the array such that:

- The element is after the previous element's position.

- There are enough elements remaining (including this one) to complete the subsequence (i.e., after this element, there are (k - current_step) elements left).

- The sum of the selected elements plus the maximum possible sum of the remaining elements (given that they have to be chosen) is equal to the maximum possible sum.

But how to compute this?

Alternatively, the problem can be broken down into two steps: first, select the indices that form the optimal subsequence. Then, for each query, pick the pos_j-th element of that subsequence.

The key is to find for each k, the optimal subsequence's indices.

So for each query (k_j), we need to find the indices of the optimal subsequence of length k_j. Once we have these indices, the answer for pos_j is the element at position pos_j-1 in the list (since it's 1-based).

The challenge is to compute these indices efficiently for each k.

Given that n and m are up to 100, we can process each query independently, even with O(n^2) algorithms.

So let's focus on how to compute the optimal subsequence for a given k.

The standard approach for selecting the lex smallest subsequence with maximum sum is a greedy algorithm. Let's see:

To find the optimal subsequence for a given k, we can model the selection as follows:

We need to select k elements. For each position in the subsequence (from 1 to k), we select the earliest element possible that allows the remaining elements to be chosen such that the sum is maximized.

Wait, perhaps the algorithm is similar to the one used for lex smallest subsequence of a certain length, but here combined with sum maximization.

Alternatively, here's a possible approach:

The optimal subsequence can be built by choosing elements one by one. For each step i (from 0 to k-1), we select the element in the array starting from the position after the previous selected element, such that:

1. The selected element is as small as possible (to get lex order), but only if selecting it allows us to select the remaining elements (k - i - 1) elements from the remaining array.

Wait, no. Because sum is the primary concern. So first, we need to select elements that maximize the sum, and then among those, choose lex smallest.

So, the selection must be such that the sum is maximum possible. So the initial step is to find the indices that contribute to the maximum sum. Then, among those, select the lex smallest subsequence.

So how to combine both sum and lex order.

An approach inspired by the "greedy algorithm with look-ahead" might work.

For example, when building the optimal subsequence step by step:

At each step, for the current position in the subsequence (say, the t-th element, 0-based), we need to choose the leftmost possible element in the array (starting from the current start position) such that:

- The number of elements remaining (n - current index) is >= (k - t) elements needed.

- Including this element allows the sum of the entire subsequence to be maximized.

But how to determine that?

Alternatively, for the current position, iterate over possible candidates. For each candidate element, check if the sum of the elements selected so far plus the sum of the best possible elements remaining (with the correct count) is equal to the maximum sum.

But how to compute this efficiently.

Another approach is to model the problem as follows:

The maximum sum subsequence of length k can be found by selecting the k elements with the highest values. But when there are ties (elements with same values), their positions determine which ones are selected to ensure lex order.

Wait, but the lex order is for the subsequence's elements. So even if two elements have the same value, their position in the original array may affect the lex order of the subsequence.

Wait, no. Lex order is based on the elements in the subsequence. For example, if two subsequences have the same elements in the same order, they are considered equal, regardless of their positions in the original array.

So the problem is to select a subsequence of length k with maximum sum. If there are multiple such subsequences, choose the lex smallest one (i.e., the one that is lex smallest when the elements are compared in order).

To maximize the sum, we need to select the k largest elements. But if there are multiple elements with the same value, their selection affects the lex order.

But wait, maybe even after selecting the k largest elements, their order in the original array affects the lex order. For example, if you have elements like [5, 5], and k=1, both are same sum. So the lex smallest is [5] (from the first element). So the lex order prefers elements that come earlier in the original array when they have the same value.

Wait no. Wait, the lex order is determined by the elements in the subsequence. So when two subsequences have the same elements, they are the same lex order. But when they have different elements, even if they are same values, the positions in the original array don't matter. Wait, but in the problem statement, the lex order is between two sequences. So if the elements in the two sequences are the same, but their positions in the original array are different, but the elements in the sequences are the same, then they are considered equal.

But that's not possible. Because the elements in the sequences are the same. For example, in the array [5,5], the two possible subsequences of length 1 are [5] (from index 0) and [5] (from index 1). Both are lex equal. So in such a case, either can be chosen. But according to the problem's definition, the lex order is determined by the elements. So the two are equal, so any would do.

But the problem says that among all such subsequences, the lex smallest is chosen. So in the case where multiple subsequences have the same sum and same elements (but different positions in the original array), the lex order is same, so any can be chosen. But according to the problem's example, when there are multiple options, the lex smallest is the one that occurs earliest in the array.

Wait, in the first example, when k=3, the optimal subsequence is [10, 20, 10], which is the original array. But that's the only possible subsequence of length 3. So that makes sense. But in the first example's note, for k=2, the optimal subsequence is [10,20], which is selected by taking the first 10 and the 20. But why not take the 20 and the next 10? Because sum is the same. But the lex order of [10,20] is smaller than [20,10], so the first is chosen.

So the lex order is determined by the elements in the subsequence, regardless of their positions in the original array. So the way to get the lex smallest subsequence among all those with maximum sum is to choose the elements in such a way that, for the earliest possible position where a decision can be made, the smallest possible element is selected, provided that the remaining elements can form a subsequence of the required length and sum.

Hmm. So how to model this?

The approach is to construct the subsequence step by step. For each step (from 1 to k), select the earliest possible element that can be part of a maximum sum subsequence. The selection must satisfy:

After selecting an element at position i, there are enough elements left (from i+1 to end) to select the remaining (k - current step) elements, and the sum of the selected elements plus the maximum possible sum of the remaining elements equals the total maximum sum.

So here's an algorithm outline for a given k:

Initialize the start index as 0. The number of elements to pick is remaining = k.

For each step in 1..k:

   For each possible index j from start to (n - remaining) (inclusive):

      Check if selecting a[j] as the next element allows us to pick (remaining-1) elements from the remaining array (after j) such that the sum is maximized.

   Among all possible j where the sum is maximized, select the smallest a[j]. If there are multiple elements with the same a[j], select the earliest one (since that would lead to a lex smaller subsequence).

Wait, but the problem requires the lex smallest subsequence. So even if two elements a[j1] and a[j2] (j1 < j2) have the same value, selecting j1 would allow the remaining elements to be chosen from a[j1+1..n], which might include elements that can form a lex smaller sequence. So even if a[j1] == a[j2], we should choose the earliest possible j to allow more flexibility in the remaining selections.

So the algorithm would be:

For each step, choose the leftmost possible j in the current window where the sum of the current element plus the sum of the best (remaining-1) elements in the remaining array is equal to the maximum possible sum.

But how to compute this for each j?

The key is that, for the current j, the best sum is a[j] plus the sum of the (remaining-1) largest elements in the remaining array (from j+1 to end). Because to maximize the sum, we need to pick the largest possible elements after j. However, when choosing j, if there are multiple j's that can contribute to the same maximum sum, then among them, we need to pick the leftmost j with the smallest a[j], and if a[j] is same, the leftmost j.

Wait, but the problem is that when considering a[j], the sum is a[j] plus the sum of the (remaining-1) largest elements in the rest of the array. So for each j, the sum is a[j] + sum of top (remaining-1) elements in the subarray starting from j+1.

But how to compute this efficiently.

An alternative approach is to precompute for each position i and required number of elements l, the sum of the top l elements in the subarray starting from i.

But given that n is up to 100, and k is up to 100, this is feasible.

So here's the plan:

For a given k, the optimal subsequence is built as follows:

Initialize variables: start = 0 (the current start index), remaining = k (number of elements left to pick), and selected = empty list.

For each step from 1 to k:

   The current step is to pick the next element in the subsequence. The element must be chosen from the current start to (n - remaining) (since after choosing this element, we need to have (remaining -1) elements left in the rest of the array).

   For each possible j in start <= j <= (n - remaining):

      Compute the sum of a[j] + sum of the (remaining -1) largest elements in a[j+1 ... n-1].

   Find the maximum possible sum value among all j.

   Among all j's that give this maximum sum, select the j with the smallest a[j]. If there are multiple j's with the same a[j], choose the leftmost one.

   Add a[j] to the selected list. Update start to j+1 and remaining to remaining-1.

Repeat until all elements are selected.

This way, each step ensures that the selected element contributes to the maximum sum, and among all possible choices, the lex smallest element is chosen first (since a[j] is as small as possible among the possible maximum choices), but when a[j] is same, the leftmost j is chosen to allow the remaining elements to be as left as possible.

This approach should work.

Now, to implement this:

For each query k, we need to generate the optimal subsequence.

The main challenge is, for each possible j in the current window, compute the sum of the (remaining-1) largest elements in the subarray from j+1 to end.

To compute this efficiently, for each possible j and remaining elements l, we can precompute the sum of the top l elements in the subarray from j+1 to end.

But since n is small (100), for each query, even if we compute this on the fly, it's manageable.

So for a given j and remaining (after selecting j, we need to pick l = remaining-1 elements), how do we compute the maximum sum of l elements in the subarray starting at j+1.

The maximum sum is the sum of the l largest elements in that subarray.

So for the subarray a[j+1 ... n-1], the sum of the top l elements.

So for each j, and for a given l, we need to compute the sum of the l largest elements in a[j+1 ... end].

This can be done by taking the subarray, sorting it in descending order, summing the first l elements (if l is not zero), else zero.

But for each j and l, this is O(n log n) time, which for n=100 and l=100 is manageable.

So the steps for processing a single query (k):

1. Compute the optimal subsequence for k.

   a. Initialize start=0, remaining=k.

   b. For each step:

      i. Determine the window from start to (n - remaining) (inclusive). Because after selecting j, we need to have (remaining-1) elements left in the remaining array (from j+1 to end). So the number of elements left after j is (n - (j+1)) elements. So (n - j -1) >= (remaining-1), which implies j <= (n - remaining).

      ii. For each j in start <= j <= (n - remaining):

         - Compute the sum of a[j] + sum of top (remaining-1) elements in a[j+1 ... n-1].

      iii. Find the maximum sum value among these j's.

      iv. Among all j's that achieve this maximum sum, select the one with the smallest a[j]. If multiple j's have the same a[j], select the leftmost (smallest index).

      v. Add a[j] to the selected list. Update start to j+1, remaining to remaining-1.

   c. Repeat until remaining becomes zero.

2. Once the selected list is built, answer the pos_j by selecting the element at position pos_j-1.

Now, the key is to implement step 1b.ii correctly.

So for each j in start to (n - remaining), compute a[j] plus the sum of the top (remaining-1) elements in a[j+1...n-1].

But how to compute that sum.

An efficient way is to take the subarray a[j+1 ... n-1], sort it in descending order, take the first (remaining-1) elements, sum them.

But for each j and remaining, this is O(n log n) time, but for n=100 and k=100, the total steps per query are O(k * n^2 log n), which for m=100 queries would be O(1e6) operations, which is acceptable given the time constraints.

So let's code this.

Let's take the first example:

n=3, a = [10,20,10]

For k=2:

remaining=2, start=0.

In first step, j can be from 0 to (3 - 2) =1.

So j=0 and j=1.

For j=0: sum is a[0] (10) + sum of top 1 elements in a[1,2]. The top 1 is 20. So sum is 30.

For j=1: sum is 20 + sum of top 1 elements in a[2]. Which is 10. Sum is 30.

So maximum sum is 30. Now, among j=0 and j=1, we need to select the j with the smallest a[j]. a[0] is 10, a[1] is 20. So select j=0.

Add a[0] to the list. Now remaining is 1, start is 1.

Second step: remaining=1. So j can be from start (1) to (3-1)=2.

So j can be 1 or 2.

For each j:

sum is a[j] + sum of top 0 elements (since remaining-1=0) = a[j].

So for j=1, sum is 20. For j=2, sum is 10. So maximum is 20. So select j=1.

Thus, the selected list is [10,20], which matches the example.

So this approach works.

Now, the code.

So for each query k_j:

We need to generate the selected list as per the steps.

Now, code steps:

Read n, a, then m queries.

For each query (k, pos):

   Generate the selected list for k.

   Output selected[pos-1].

So the code outline is:

Read n.

a = list of integers.

Read m.

queries = list of (k, pos) pairs.

for each query in queries:

    k, pos = query.

    selected = compute_optimal_subsequence(a, k)

    print(selected[pos-1])

Now, the function compute_optimal_subsequence:

def compute_optimal_subsequence(a, k):

    n = len(a)

    selected = []

    start = 0

    remaining = k

    for _ in range(k):

        max_sum = -inf

        best_j = -1

        # possible j's are from start to (n - remaining) inclusive.

        end_j = n - remaining

        for j in range(start, end_j + 1):

            # compute sum of a[j] plus sum of top (remaining-1) elements in a[j+1 ... ]

            if remaining -1 ==0:

                current_sum = a[j]

            else:

                # get the subarray a[j+1 ...]

                sub = a[j+1 : ]

                # sort in descending order

                sub_sorted = sorted(sub, reverse=True)

                # take first (remaining-1) elements, sum them.

                sum_rest = sum(sub_sorted[: remaining-1])

                current_sum = a[j] + sum_rest

            if current_sum > max_sum:

                max_sum = current_sum

                best_j = j

                best_val = a[j]

            elif current_sum == max_sum:

                # compare a[j] with best_val. If a[j] is smaller, then update.

                if a[j] < best_val:

                    best_val = a[j]

                    best_j = j

                elif a[j] == best_val:

                    # prefer the leftmost j.

                    if j < best_j:

                        best_j = j

        # after processing all j's, select best_j.

        selected.append(a[best_j])

        start = best_j +1

        remaining -=1

    return selected

This function should return the optimal subsequence.

Testing this with the first example:

n=3, a = [10,20,10], k=2.

First step: remaining=2, start=0, end_j =3-2=1.

Loop j from 0 to 1.

j=0:

sub is a[1:3] = [20,10]. sorted desc: [20,10]. sum_rest is sum of 1 element (remaining-1=1) →20. current_sum=10+20=30.

j=1:

sub is a[2:3] →[10]. sum_rest is 0 (since remaining-1=1, but the sub has length 1. So sum is 10. current_sum =20+10=30.

max_sum is 30. Now, between j=0 and j=1: a[j] is 10 and 20. So best_j is 0.

selected becomes [10]. start=1, remaining=1.

Second step: remaining=1, start=1, end_j =3-1=2.

j can be 1 or 2.

For j=1:

sum_rest is sum of 0 elements →0. current_sum is 20.

For j=2: sum_rest 0 →10.

max_sum is 20. best_j=1.

selected is [10,20], which is correct.

So this works.

Another example:

Second sample input:

7

1 2 1 3 1 2 1

For query k=2, the optimal subsequence is [3, ...] ?

Wait the sample output for query k=2, pos=1 and 2 gives 2 and 3, which suggests that the optimal subsequence for k=2 is [2,3]. But how?

Wait in the array [1,2,1,3,1,2,1], when k=2.

The maximum sum would be 3+2=5. But possible elements:

3 is in position 3. The next element after 3 is 1,1,2,1. So the best is 3 and then 2 (position 5). Sum is 5.

Alternatively, 2 (position 1) and 3 (position 3) sum to 5. Or 3 (position3) and 2 (position5). Both sum to 5.

But the lex order between [2,3] and [3,2] is [2,3] which is lex smaller.

So the optimal subsequence is [2,3].

How does the algorithm find this?

In step 1:

remaining=2, start=0, end_j=7-2=5.

j can be from 0 to 5.

For each j in 0-5, compute a[j] + sum of top 1 element in j+1 to 6.

We need to find which j gives the maximum sum.

a[0] =1. sum of top 1 in 1-6. The array is [2,1,3,1,2,1]. The top is 3. sum_rest=3. current_sum=1+3=4.

a[1]=2. sum of top 1 in 2-6: elements [1,3,1,2,1]. top is 3. sum_rest=3. current_sum=5.

a[2]=1. sum of top1 in 3-6: [3,1,2,1] →3. sum_rest=3. sum=4.

a[3]=3. sum of top1 in 4-6 → [1,2,1]. sum_rest=2. current_sum=3+2=5.

a[4]=1. sum of top1 in 5-6 →2. sum_rest=2. current_sum=3.

a[5]=2. sum of top1 in 6-6 →1. sum_rest=1. current_sum=3.

So the maximum sum is 5, achieved at j=1 and j=3.

Now, between j=1 (a[j]=2) and j=3 (a[j]=3), the a[j] values are 2 and 3. So j=1 is chosen because a[j] is smaller. So the first element is 2 (a[1]).

Then, in step 2, remaining=1, start=2 (j=1+1=2), end_j=7-1=6.

We need to select j in 2<=j<=6, and select the element with maximum a[j]. Because remaining-1=0, so sum is a[j]. The maximum a[j] in positions 2 to 6 is 3 (at j=3), but j starts from 2.

Wait, after j=1 is chosen, start is 2. So the next j can be from 2 to 6 (since remaining=1, end_j=7-1=6).

So for j=2, a[j] is 1. j=3:3. j=4:1. j=5:2. j=6:1.

The maximum is 3 at j=3. So selected list is [2,3], which is correct.

Thus, the code works.

So the code seems correct.

Now, implement this in Python.

Edge Cases:

- n=1, m=1, k=1, pos=1 → returns the single element.

- All elements are the same. For example, a = [5,5,5], k=3 → the entire array is selected.

- When the optimal subsequence is the first k elements (if they have the maximum sum).

So the code should handle these.

Now, code:

Read the input as per the problem statement.

Then for each query, compute the optimal subsequence and select the required pos.

Now, code:

Read n.

Read a as a list of integers.

Read m.

Then read m lines of k and pos.

For each query:

Compute the optimal subsequence for k.

Then output the pos-1 element.

Implementing the function as described.

Now, code:

But in Python, list slicing is straightforward.

Testing the code.

For the first sample input:

3

10 20 10

6 queries.

The first query is k=1, pos=1. The optimal subsequence is [20], so output 20.

Another query: k=2, pos=1 →10.

Which the code would select.

So code seems correct.

Now, let's code.
</think>

```python
def compute_optimal_subsequence(a, k):
    n = len(a)
    selected = []
    start = 0
    remaining = k
    
    for _ in range(k):
        max_sum = -float('inf')
        best_j = -1
        best_val = None
        end_j = n - remaining
        
        for j in range(start, end_j + 1):
            if remaining - 1 == 0:
                current_sum = a[j]
            else:
                sub = a[j+1:]
                sub_sorted = sorted(sub, reverse=True)
                sum_rest = sum(sub_sorted[:remaining-1]) if remaining-1 <= len(sub) else sum(sub_sorted)
                current_sum = a[j] + sum_rest
            
            if current_sum > max_sum:
                max_sum = current_sum
                best_j = j
                best_val = a[j]
            elif current_sum == max_sum:
                if a[j] < best_val or (a[j] == best_val and j < best_j):
                    best_j = j
                    best_val = a[j]
        
        selected.append(a[best_j])
        start = best_j + 1
        remaining -= 1
    
    return selected

n = int(input())
a = list(map(int, input().split()))
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

for k, pos in queries:
    subsequence = compute_optimal_subsequence(a, k)
    print(subsequence[pos-1])
```