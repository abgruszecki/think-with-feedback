<think>
Okay, let's tackle this problem. Hmm, the problem says Sagheer wants to buy as many souvenirs as possible without exceeding his budget S. And if there's a tie in the number of items, he picks the one with the minimal total cost. 

So, the key here is to find the maximum possible k such that the sum of the adjusted costs (ai + xi * k for each item xi selected) is <= S. And we need to compute this efficiently, considering that n can be up to 1e5. 

First, how do we approach this? For a given k, we can select the k items with the smallest (ai + xi * k) values. Then, sum those and check if it's within S. Our goal is to find the largest possible k where this sum is <= S. 

Since the possible k ranges from 0 to n, we can perform a binary search on k. For each candidate k in the binary search, we compute the minimum possible sum for that k and see if it's <= S. 

But how do we compute the sum for a given k quickly? Well, for each item, the adjusted cost is ai + i * k (since indices are 1-based here). So for each k, we can compute ai + i*k for all items, then pick the k smallest ones and sum them. If this sum is <= S, then that k is possible. 

But calculating this for each k in O(n) time would be O(n log n) per binary search step. Since binary search would take up to log n steps, the total time would be O(n (log n)^2), which for n=1e5 is around 1e5 * (20)^2 = 4e6 operations. That's acceptable within the time constraints, I think. 

Wait, but what's the maximum possible binary search steps? The maximum k can be up to 1e5, so binary search would take about 20 steps. Each step requires O(n) to compute the modified costs and then a sort, but sorting n elements each time would be O(n log n), making the overall complexity O(n (log n)^2). Wait, 1e5 * (log 1e5)^2 is about 1e5 * (17)^2 = ~2.89e7, which is manageable. But maybe we can optimize further.

Alternatively, for each k, the adjusted cost is ai + i*k. Let's think about how to compute the sum of the k smallest elements efficiently. Instead of sorting all elements, can we find the k smallest elements in O(n) time? Well, the problem requires the sum of the k smallest values. So for each k, we can compute ai + i*k for all i, and then find the sum of the k smallest such values. 

But even to compute that sum, we need to find the k smallest elements. The fastest way to get the sum is to generate an array of ai + i*k for all i, then sort it, take the first k elements and sum. But that's O(n log n) per step. 

But with n up to 1e5 and binary search steps up to 20, this would be 2e6 operations. Wait, 1e5 * 20 steps is 2e6, but each step involves O(n log n) operations, which for n=1e5 is 1e5 * 17 ~ 1.7e6 per step. So total operations would be 20 * 1.7e6 = ~34 million. Python can handle that, but it's tight. So maybe we need a smarter approach. 

Wait, for each candidate k, the cost for each item is ai + k * i. Let's precompute all possible ai + i * k. But how can we compute this quickly for varying k? Well, for each k, we need to generate a new array. So for each binary search step, we generate the array, sort it, sum the first k elements. 

But perhaps there's a way to find the sum without sorting. Let's think. The sum is the sum of the k smallest (ai + i*k) values. For a given k, the ai + i*k can be thought of as a linear function of i. So for each k, we need to find the k items with the smallest (ai + i*k). 

But how else can we find the sum of the k smallest elements? Maybe using a priority queue. For each k, we can iterate through all items, compute ai + i*k, and keep track of the k smallest values using a max-heap. But even that would take O(n log k) time per k. Which for k up to 1e5 is O(n log n) again. So maybe that's not better than sorting. 

So perhaps the straightforward approach is acceptable. Let's outline the steps:

1. Binary search on k (the maximum possible number of items). The lower bound is 0, the upper bound is n. 

2. For each candidate k in binary search:
   a. Compute for each item the value (ai + i * k).
   b. Find the sum of the k smallest such values.
   c. If the sum is <= S, then this k is possible. We can try to see if a larger k is possible. Otherwise, try a smaller k.

3. Once the maximum k is found, compute the minimal sum for that k. 

But there's a problem here. For example, in the first sample input, when k=2, the sum is 4+7=11. But how do we compute that sum?

Wait, in the first sample input, the items are [2,3,5]. The indices are 1,2,3. For k=2, each item's cost is ai + i*2. So:

Item 1: 2 + 1*2 =4
Item 2:3+2*2=7
Item3:5+3*2=11
The two smallest are 4 and7, sum 11. Which is correct. 

So the approach is to compute all ai + i*k, sort them, sum the first k. 

But for large n, say 1e5, and binary search steps, this approach could be feasible. 

But in Python, sorting a list of 1e5 elements takes O(n log n) time. For 1e5 elements, that's about 1e5 * 17 = 1.7e6 operations. Multiply by 20 steps gives 34e6 operations, which should be manageable. 

But let's test this. Let's consider that for n=1e5, each binary step would take about 0.1 seconds (since Python can handle about 1e6 operations per second). 34e6 is about 34 seconds. That's way over the time limit. Wait, but maybe I'm miscalculating. 

Wait, for each binary search step, the time per step is O(n log n). For n=1e5, that's 1e5 * log2(1e5) ~ 1e5 * 17 = 1.7e6 per step. For 30 steps (since log2(1e5) is ~17, so binary search steps would be around 17), that's 17 * 1.7e6 = ~28.9e6 operations. Which in Python might be tight. But perhaps with optimizations, like precomputing the sorted list for each k, but how?

Wait, perhaps there's a way to precompute the optimal k and sum. Let's think differently. 

The key observation is that for each item, the cost when selecting k items is ai + i*k. But when k changes, the cost of each item changes. However, the optimal selection of k items (those with the smallest ai + i*k) can vary with k. 

But maybe there's a way to model this and find the maximum k efficiently. Alternatively, perhaps we can find for each possible k the sum of the k smallest (ai + i*k) efficiently. 

Another approach: For each item, the function f(k) = ai + i*k. The sum for a particular k is the sum of the k smallest f(k) values. We need to find the largest k where this sum is <= S. 

But the sum for a given k is a non-decreasing function. Because as k increases, each f(k) increases by i per unit k. So the sum of the k smallest terms for k+1 may be larger than for k. But how can we model this? 

Wait, when k increases by 1, the cost of each item in the selected set increases by i. For example, if we select items x1, x2, ..., xk for k, then when moving to k+1, the cost for each xj would be axj +xj*(k+1) = (axj + xj*k) + xj. So the sum increases by sum(xj) for the selected items. 

But this seems complicated. So maybe the binary search approach is the way to go. 

But how can we optimize the per-step computation? Let's think: for a given k, the cost for each item is ai + i*k. The sum of the k smallest such values. 

Wait, for a given k, the value ai + i*k can be rewritten as i*(k) + ai. So for each item, the cost is linear in k. But the selection of which items are the k smallest depends on k. 

But during binary search, we need to compute for various k. 

Wait, here's an alternative idea: the function for each item is a linear function of k. The cost for item i at k is ai + i*k. So for each item, this is a line with slope i and intercept ai. The sum over k items is the sum of the k lines with the smallest values at a particular k. 

But how does the selection of which k items are chosen vary with k? For example, for two items i and j, which one is better depends on k. Suppose i < j. At very small k, ai +i*k may be less than aj + j*k. But as k increases, since j's slope is steeper, at some k where (ai +i*k) < (aj +j*k) until k crosses a certain threshold. 

So the set of items selected for the optimal sum changes as k increases. This makes it difficult to model, as the optimal set isn't a fixed subset. 

Therefore, binary search seems necessary, and for each step, compute the sum for that k. 

So the steps are:

- Binary search the maximum k where the sum of the k smallest (ai + i*k) is <= S. 

Once the maximum k is found, compute the minimal sum. 

Now, how to implement this efficiently. 

First, the binary search. The low is 0, high is n. 

For each mid in binary search (mid is the candidate k), we compute the sum of the k=mid smallest (ai + i*mid) values. 

If the sum is <= S, we can try a higher k. Otherwise, try lower. 

Once the maximum possible k is found, we need to compute the sum again to get the minimal total cost for that k. 

So, the code structure would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, S = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    low = 0
    high = n
    best_k = 0
    best_sum = 0

    while low <= high:
        mid = (low + high) // 2
        # Compute sum for k=mid
        costs = [a[i] + (i+1)*mid for i in range(n)]  # since the indices are 1-based
        costs.sort()
        total = sum(costs[:mid])
        if total <= S:
            best_k = mid
            best_sum = total
            low = mid + 1
        else:
            high = mid -1

    print(best_k, best_sum, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 100
1 2 5 6
""",
            "output": \
"""\
4 54
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

Another sample:

Input 4 100

1 2 5 6

Output is 4 54.

For k=4:

costs are 1+1*4=5, 2+2*4=10,5+3*4=17,6+4*4=22. sum 5+10+17+22=54. Correct. 

Third sample:

1 7

7

k=1: cost is 7+1*1=8, which is over 7. So maximum k is 0. 

So the code works for samples.

But the problem is with the time. For n=1e5, the code would have to process 1e5 elements for each binary step, sort them, sum the first k. 

But sorting a list of 1e5 elements in Python is possible. Let's see: Python's list.sort() is very efficient. Let's check the time. 

But for n=1e5, each sort takes about O(n log n) time. So 1e5 elements, sorted 20 times. Maybe it's acceptable. But I'm not sure. 

Wait, the time limit is 2 seconds. Let's estimate:

Assuming that each sort of 1e5 elements takes 0.1 seconds. Then 20 sorts would take 2 seconds. So that's acceptable. But in practice, Python's sort is implemented in C and is very fast. So perhaps even for 1e5 elements, the sort takes less than 0.01 seconds. So 20 steps would be 0.2 seconds. 

But to confirm, perhaps there's a way to optimize this. 

Alternative approach: precompute a list for each k. But that's not feasible. 

Another idea: when computing the sum for a given k, instead of sorting the entire list, find the k smallest elements and sum them. This can be done using a selection algorithm like quickselect, which can find the k smallest elements in O(n) time on average. However, in Python, there's no built-in quickselect, but you can implement it. However, implementing quickselect in Python may be slower than just using the built-in sort. 

Alternatively, using the heapq module's nsmallest function. 

For example, in Python, heapq.nsmallest(k, list) returns a list of the k smallest elements. This is implemented in C and is optimized. For large k, the time complexity is O(n) (since the implementation uses a heap of size k, which for k approaching n is O(n log k)), but for k up to 1e5, this might be slower than sorting. 

Let's compare:

Option 1: Sort the entire list and sum the first k elements. Time O(n log n).

Option 2: Use heapq.nsmallest(k, list), then sum. For k up to 1e5, the time would be O(n + k log k) (since after building a heap of size k, which takes O(n) time, then extracting them in order). But for k=1e5, log k is about 17, so it's O(n + 1e5 * 17) = O(n). But comparing this to O(n log n) for the sort approach. 

For n=1e5, n log n is 1e5 * 17 ≈ 1.7e6, while option 2 is 1e5 + 1e5 *17 = 1.8e6. But perhaps in practice, the heapq approach is faster for smaller k. But for k approaching n, sorting might be better. 

But in the binary search steps, mid can be up to n, so in those steps, k is large. So for the steps where mid is large, the sort approach is O(n log n) time. Whereas heapq.nsmallest would take O(n) time. Wait, no. Because when you use heapq.nsmallest(n, list), the implementation will sort the entire list. So for k >= n, it's equivalent to sorting. So for k close to n, it's better to sort and sum. 

So perhaps the optimal approach is to check whether k is small (like, say, less than 1e4) and use heapq.nsmallest, else use the sort approach. But this adds complexity and may not be worth it. 

Alternatively, perhaps the sort approach is faster in Python because the built-in sort is very optimized. So even though the time complexity is O(n log n), the actual time is better than using heapq for large k. 

So perhaps the original code is acceptable. 

But let's think about how to optimize further. 

Another optimization is to precompute the list of a[i] + i*k for each k. But this is not possible as k varies. 

Alternatively, for each k, the cost array can be computed as a list. But for n=1e5, creating this list each time would take O(n) time. But in Python, list comprehensions are fast. 

Another possible optimization is to precompute the a[i] and i values (i+1) as tuples, and then compute the cost for each k on the fly. 

But let's look at the code again. For each mid, the code creates a list of a[i] + (i+1)*mid. Then sorts it, and sums the first mid elements. 

So, for mid=0, the cost is a[i] +0, so sum of the first 0 elements is 0. But in the code, when mid is 0, the list is created, sorted, but then sum of first 0 elements. 

But for mid=0, the code will proceed, but since mid=0, sum is 0. But in practice, in the binary search, the code will only compute for mid=0 once. 

But for large mid, say 1e5, the code creates a list of 1e5 elements, sorts them (O(n log n)), and sums the first 1e5 elements (which is sum of all elements). 

So, perhaps for mid=1e5, the code can compute the sum as sum(a[i] + (i+1)*mid for i in 0..n-1). But in this case, the sum of all elements is the sum of a[i] plus mid * sum(i+1 for i in 0..n-1). 

Wait, that's a key insight! For a given k, when you have to select all k elements (since k is equal to n), the sum is sum(a) + k * sum(i+1 for i in 0..n-1) = sum(a) + k * sum(1..n). 

So when k ==n, the sum can be computed in O(1) time (assuming precomputed sums). 

Similarly, when the code is considering a k where the sum is the sum of all elements. 

But in the binary search steps, when the code is checking for k=n, it can compute the sum quickly. 

But how to generalize this. 

Alternatively, precompute sum_a = sum(a), sum_i = sum(1..n) = n*(n+1)//2. Then for a given k, if the code is considering the sum of all k elements (when k is the candidate), then the sum is sum_a + k * sum_i. But this is only valid if all elements are selected, which is when the sum is sum of all a[i] +k*(i+1). 

But for the code's binary search steps, when the code is checking for a particular k, the sum is the sum of the k smallest elements. However, for k =n, the sum is sum(a[i] + (i+1)*k) for all i. Which is sum_a +k * sum_i. 

But that's the same as the sum of all elements. So if sum_a +k*sum_i <= S, then k=n is possible. 

So, in the code, for mid=k, when the code checks for the sum, if mid is equal to n, the sum can be computed as sum_a +mid * sum_i. 

But this is only when mid is n. For other mid values, the sum is the sum of the k smallest elements. 

So, this can be optimized for the case when mid ==n. 

But perhaps this isn't a big optimization. 

Another approach: precompute the sum_i array. For example, sum_i is the sum of the indices (1-based). 

But perhaps the code can precompute sum_i once. sum_i = n*(n+1)//2. 

So, during binary search:

if mid ==n:
   total = sum_a + mid * sum_i
   if total <=S:
       best_k =n, best_sum= total
       ... 

Else:
   compute the sum as before. 

This could save time when the maximum possible k is n. But in the general case, it's not helpful. 

But the code would need to check for mid ==n. 

But perhaps this isn't worth the effort, as the code would only save one step. 

Another optimization: precompute all the possible a[i] + i*mid. But that's not possible as mid varies. 

Alternatively, note that for each i, a[i] + i*k is a linear function in k. So for each i, the function is linear, and the cost for different k's can be considered as lines. 

But how does this help in finding the sum of the k smallest lines for a particular k? 

Hmm. This seems like a problem that can be modeled using convex hull trick or similar, but I'm not sure. 

Alternatively, think of the problem as for each k, the cost of item i is a_i + i*k. The sum of the k smallest such costs is what we need. 

But for a given k, which items are the k cheapest? 

Each item's cost is a_i + i*k. So for a given k, items with lower a_i and lower i would be cheaper. But for higher k, higher i items become more expensive. 

But how to model the selection of items. 

Perhaps for a given k, the optimal selection is the items with the smallest a_i +i*k. So the code's current approach is correct. 

But given the time constraints, we need to optimize the code as much as possible. 

Another idea: precompute the (a_i, i) pairs and for each binary search step, compute a_i +i*k and sort. 

But in Python, list comprehensions are fast. So the line:

costs = [a[i] + (i+1)*mid for i in range(n)]

should be efficient. 

But perhaps we can precompute a list of (i+1) for each element. 

Like, indices = [i+1 for i in range(n)], then for each mid, compute a[i] + indices[i] * mid. 

But again, the code's approach is to compute this for each mid. 

Another optimization: using generator expressions and early termination when possible. 

But I think the code as written is correct but may need to be optimized for Python's speed. 

So, how to speed up the code in Python. 

In Python, list comprehensions are faster than for loops. So the line:

costs = [a[i] + (i+1)*mid for i in range(n)]

is already as efficient as possible. 

Then, sorting the list. 

The sum is sum(costs[:mid]), which is O(k) time. For mid up to 1e5, summing 1e5 elements takes O(1e5) time. So per step, O(n) to create the list, O(n log n) to sort, O(k) to sum. 

But in Python, the sum is done in C, so sum(costs[:mid]) is fast. 

So, the main bottleneck is sorting. 

Alternative approach: when mid is large, say mid >= n/2, perhaps we can compute the sum of all elements and subtract the sum of the (n - mid) largest elements. 

Because sum of the mid smallest elements is equal to the total sum minus the sum of the (n - mid) largest elements. 

But this approach would require computing the total sum of a_i +i*mid for all elements, then subtracting the sum of the (n - mid) largest elements. 

But for mid=1e5, this would require summing all elements (1e5 operations) and then summing the (0) largest elements. So same as before. 

But for mid = 5e4, this would require summing the 5e4 smallest elements or the 5e4 largest elements. 

But how to compute the sum of the (n - mid) largest elements. 

For example, for mid=5e4 and n=1e5:

sum_smallest = sum(sorted_list[:5e4])

Alternatively, sum_total = sum(sorted_list)

sum_smallest = sum_total - sum(sorted_list[5e4:])

But this requires summing the entire list once (sum_total), which is O(n), and then summing the sorted_list[5e4:], which is O(n - mid). 

But this could save time for mid close to n, but not sure. 

For example, if mid is 1e5 (n=1e5), sum_smallest is sum_total. 

But if mid is 5e4, sum_smallest is sum(sorted_list[:5e4]) which is 5e4 elements. But sum_total is O(n), which is 1e5 steps. 

But sum_total would take O(n) time, which is the same as summing the sorted list. 

So this approach would not save time. 

Another idea: for the sum, since the list is sorted, sum the first mid elements. But in Python, summing a slice of a list is O(k) time, but it's done in C. So even for k=1e5, it's very fast. 

But for the code as written, the main issue is the sorting step. 

So perhaps, to optimize, precompute the (i+1) and a[i] as separate arrays, but no. 

Alternatively, precompute for each item, the (a[i], i+1) as a tuple. But I don't think that helps. 

Another approach: during binary search, for each candidate k, compute the required sum and store it. But this doesn't help. 

So perhaps the code as written is the best possible. 

But let's try to test for n=1e5. 

Suppose we have n=1e5 and each a[i] is 1. The code would run 20 steps, each time creating a list of 1e5 elements, sorting them, summing the first mid elements. 

In Python, creating a list of 1e5 elements with list comprehensions is fast. Sorting 1e5 elements takes about 0.01 seconds. Summing 1e5 elements is also fast. So for 20 steps, 0.2 seconds. 

So within the 2-second time limit. 

But what if the code is accepted? 

Another possible optimization is to avoid sorting when k is 0 or 1. But these are edge cases. 

Alternatively, in the binary search step, we can check if mid is 0 and skip processing. 

But in the code as written, when mid is 0, the code creates a list of a[i] +0, which is a[i], then sorts and sums the first 0 elements. But sum is zero. 

But that's unnecessary. So perhaps, in the code, for mid=0, the sum is zero. So we can handle mid=0 as a special case. 

But in the binary search steps, when mid=0, it's only checked once. 

So perhaps that's not worth optimizing. 

Another observation: for a given k, the sum is the sum of the k smallest (a[i] + (i+1)*k) values. 

But can we precompute the sorted list of (a[i] + (i+1)*k) more efficiently? 

In Python, using list comprehensions is already efficient. 

Alternatively, using NumPy arrays for faster computation, but in some programming contest environments, importing numpy is not allowed. 

But the problem statement doesn't allow any additional output, and the code must be in standard Python. 

So the code must use standard Python features. 

So, the code as written seems correct and should pass all test cases within the time constraints. 

But let's check the third sample:

Input 1 7 7. The code's binary search would check mid=1. sum is 7+1*1=8, which is larger than 7. So high becomes 0, and the code returns best_k=0, sum 0. 

Which is correct. 

So the code works for all samples. 

Now, to write the code. 

But wait, what about the data types? For n=1e5 and each a[i] up to 1e5, and k up to 1e5, the term (i+1)*k can be up to (1e5) * 1e5 = 1e10. Summing 1e5 such terms can be up to 1e15. Which fits into Python's integer type. So no overflow issues. 

So the code is correct. 

Thus, the final code is as written.
</think>

```python
n, S = map(int, input().split())
a = list(map(int, input().split()))
max_k = 0
min_cost = 0

low, high = 0, n
sum_a = sum(a)
sum_i = n * (n + 1) // 2

while low <= high:
    mid = (low + high) // 2
    if mid == 0:
        current_sum = 0
        valid = True
    else:
        costs = [a[i] + (i + 1) * mid for i in range(n)]
        costs.sort()
        current_sum = sum(costs[:mid])
        valid = current_sum <= S
    if valid:
        if mid > max_k or (mid == max_k and current_sum < min_cost):
            max_k = mid
            min_cost = current_sum
        low = mid + 1
    else:
        high = mid - 1

print(max_k, min_cost)
```
