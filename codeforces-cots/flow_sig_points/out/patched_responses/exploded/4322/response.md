<think>
Okay, let's see. We have a sorted array and need to split it into k consecutive subarrays such that the sum of the max minus min of each subarray is minimized. Hmm. Since the array is sorted, each subarray's max and min are the first and last elements, or maybe the other way around? Wait, because the array is non-decreasing. So for any subarray, the min is the first element and the max is the last. Because the array is sorted. So the cost for a subarray from i to j is a[j] - a[i]. So the total cost is the sum of (a[j] - a[i]) for each of the k subarrays.

Our goal is to split the array into k parts such that this sum is minimized. How can we approach this?

Let's think. Since the array is sorted, the minimal cost would be achieved by making the differences (a[j] - a[i]) as small as possible for each subarray. But when we split into k parts, we have to place k-1 splits. Each split is between two elements. For example, splitting after index m would create two parts: up to m, and from m+1 onwards.

Wait, but how to model this. Let's think of the total cost. The total cost is the sum of (a[end of subarray] - a[start of subarray]) for each of the k subarrays.

But since the array is sorted, each subarray's start is <= end. So each term is a[end] - a[start]. The sum of all these terms is equal to the sum of (a[end1] - a[start1]) + ... + a[endk] - a[startk]. But the starts and ends are consecutive. For example, the end of the first subarray is the start of the second minus one. Wait, no. Let's say the first subarray is from s1 to e1, the next from s2 = e1 + 1 to e2, and so on. Then the sum is (a[e1] - a[s1]) + (a[e2] - a[s2]) + ... + (a[ek] - a[sk]).

But s1 = 0 (if we index from 0), e1 = x, s2 = x+1, etc. So the sum can be rewritten as (a[e1] - a[0]) + (a[e2] - a[e1+1]) + ... + (a[n-1] - a[e_{k-1}+1]).

Wait, maybe there's a way to model this. Let's see: the total sum of all the (max - min) for the subarrays is (a[e1] - a[0]) + (a[e2] - a[e1+1]) + ... + (a[n-1] - a[e_{k-1}+1]). Let's expand this sum. It's (a[e1] + a[e2] + ... + a[n-1]) - (a[0] + a[e1+1] + a[e2+1] + ... + a[e_{k-1}+1} ). 

So the total cost is equal to (sum of the last elements of each subarray) minus (sum of the first elements of each subarray). But since each subarray is consecutive, the first element of a subarray is the next element after the end of the previous subarray. For example, after splitting into k subarrays, the first elements are a[0], a[e1+1], a[e2+1], etc. And the last elements are a[e1], a[e2], ..., a[n-1].

Wait, so the sum of last elements is a[e1] + a[e2] + ... + a[n-1], and the sum of first elements is a[0] + a[e1+1] + a[e2+1] + ... + a[e_{k-1}+1}. So the total cost is (sum of last elements) - (sum of first elements).

Hmm. That's a crucial observation. So the problem reduces to choosing k-1 split points to minimize this difference. Now, how can we model this?

Let's see. The sum of last elements is fixed as a[n-1] (the last element of the last subarray) plus the sum of the other k-1 last elements. Wait, no. The last elements are the end of each subarray. For example, if the array is split into k subarrays, the last elements are the ends of each subarray. So the sum is sum of a[e1], a[e2], ..., a[e_{k}], where e_k = n-1.

Similarly, the sum of first elements is a[0] (the start of the first subarray) plus a[e1+1], a[e2+1], ..., a[e_{k-1}+1]. Because each next subarray starts at e_i +1.

So, the total cost is (sum of a[e1], a[e2], ..., a[n-1]) - (a[0] + a[e1+1] + a[e2+1] + ... + a[e_{k-1}+1}).

Hmm. So maybe we can model this as choosing k-1 split points (positions between elements) such that the sum of the differences between the end elements and the next start elements is maximized, which would minimize the total cost. Because the total cost is (sum of ends) - (sum of starts) = (a[n-1] - a[0]) - sum of (a[e1+1] - a[e1] + a[e2+1] - a[e2] + ... + a[e_{k-1}+1} - a[e_{k-1}} ]). Wait, maybe not. Let me think again.

Wait, the sum of the ends is the sum of the last elements of each subarray. The sum of the starts is the sum of the first elements of each subarray. The first element of the first subarray is a[0]. The first element of the second subarray is a[e1+1], and so on.

So the total cost is (sum of ends) - sum of starts.

But the sum of the ends can be written as a[e1] + a[e2] + ... + a[ek], where ek = n-1.

The sum of the starts is a[0] + a[e1+1] + a[e2+1] + ... + a[e_{k-1}+1}.

So the total cost is (sum of ends) - (sum of starts) = [a[e1] + a[e2] + ... + a[ek]] - [a[0] + a[e1+1] + ... + a[e_{k-1}+1}].

But notice that a[ek] is a[n-1], and the sum of ends is the sum of the last elements of each subarray.

Alternatively, we can model this as follows: the sum of (max - min) for all subarrays is equal to (a[e1] - a[0]) + (a[e2] - a[e1+1}) + ... + (a[ek] - a[e_{k-1}+1}).

Which is equal to (a[e1] + a[e2] + ... + a[ek}) - (a[0] + a[e1+1} + a[e2+1} + ... + a[e_{k-1}+1}).

So this is the same as the previous expression. Now, how can we maximize this sum? Wait, no. We need to minimize the total cost. Wait, the total cost is exactly this sum. So our goal is to split the array into k parts such that this sum is as small as possible.

Alternatively, since the array is sorted, maybe the minimal possible cost is when the sum of (a[e_i] - a[start_i]) for each subarray is minimized. How can we do that?

Wait, but a[e_i] - a[start_i] is the difference between the first and last element of the subarray. Since the array is sorted, each subarray's start_i <= end_i. So the difference is a[end_i] - a[start_i]. So for each subarray, the difference is the maximum possible in that subarray minus the minimum possible, which is the same as the last element minus the first element.

So the problem reduces to selecting k-1 split points such that the sum of (a[end_i] - a[start_i]) for each subarray is minimized.

But how to model this. Let's think of the splits. Let's say we split the array into k parts. The first part is from 0 to s1-1, the second from s1 to s2-1, etc., and the k-th part is from s_{k-1} to n-1.

Each split is between elements. So the splits are at positions s1, s2, ..., s_{k-1} where each s is the start of a new subarray. So the first subarray is 0 to s1-1, the second s1 to s2-1, etc.

The sum is (a[s1-1] - a[0]) + (a[s2-1] - a[s1]) + ... + (a[n-1] - a[s_{k-1}]).

So, the total sum can be rewritten as (a[s1-1] + a[s2-1] + ... + a[n-1]) - (a[0] + a[s1] + a[s2] + ... + a[s_{k-1}])).

Hmm. So the sum is (sum of ends) - (sum of starts). So to minimize this sum, we need to maximize the sum of starts, or minimize the sum of ends. Wait, but how?

Wait, the sum is (sum of ends) minus (sum of starts). To minimize the total sum, we need to maximize the sum of starts and minimize the sum of ends. But the sum of ends is the sum of the last elements of each subarray. The sum of starts is the sum of the first elements of each subarray. Since the array is sorted, the starts are non-decreasing. So for the first subarray, the start is a[0], then next start is a[s1], then a[s2], etc., each being >= the previous.

So the sum of starts is a[0] + a[s1] + a[s2] + ... + a[s_{k-1}]. The sum of ends is a[s1-1] + a[s2-1] + ... + a[n-1}.

We need to choose k-1 split points such that sum(ends) - sum(starts) is minimized.

But how to find this efficiently.

Let's think about the difference between sum(ends) and sum(starts). Since the array is sorted, a[s_i-1] <= a[s_i]. So each end term is <= the next start term. So sum(ends) is <= sum(starts) + ... ?

Not sure. But maybe there's a way to model this problem using greedy approach or dynamic programming.

Alternatively, let's see the problem in another way. The total cost is equal to the sum over all subarrays of (last element - first element). Since the array is sorted, each subarray's last element is >= the first. So the sum is the sum of (last elements) - sum of (first elements).

But the sum of the last elements is a[s1-1] + a[s2-1] + ... + a[n-1}. The sum of the first elements is a[0] + a[s1] + a[s2] + ... + a[s_{k-1}].

So the total cost can be written as:

(total_ends) - (total_starts)

where total_ends is sum of last elements of each subarray, and total_starts is sum of first elements.

But how can we model this?

Another approach: The total cost can also be expressed as (a[n-1] - a[0]) - sum_{i=1}^{k-1} (a[s_i] - a[s_i -1]).

Wait, let's see. Because:

sum_ends = a[s1-1] + a[s2-1] + ... + a[s_{k-1}-1} + a[n-1]

sum_starts = a[0] + a[s1] + a[s2] + ... + a[s_{k-1}]

sum_ends - sum_starts = [a[s1-1] + a[s2-1} + ... + a[n-1}] - [a[0} + a[s1} + ... + a[s_{k-1}} ]

We can rearrange this:

= a[s1-1} - a[s1} + a[s2-1} - a[s2} + ... + a[s_{k-1}-1} - a[s_{k-1}} } + (a[n-1] - a[0})

Because:

sum_ends = a[s1-1} + a[s2-1} + ... + a[s_{k-1}-1} + a[n-1}

sum_starts = a[0} + a[s1} + ... + a[s_{k-1}} 

sum_ends - sum_starts = (a[s1-1} - a[s1}) + (a[s2-1} - a[s2}) + ... + (a[s_{k-1}-1} - a[s_{k-1}} )) + (a[n-1} - a[0} )

So the total cost is (a[n-1] - a[0}) + sum_{i=1 to k-1} (a[s_i -1} - a[s_i} )

So, since a[n-1] and a[0} are fixed (they are the first and last elements of the entire array), the problem reduces to selecting k-1 split points (s_1, s_2, ..., s_{k-1}) such that the sum of (a[s_i-1} - a[s_i}) is as large as possible. Because this sum is subtracted from the initial (a[n-1} - a[0}) term. Wait, no. Wait, the total cost is (a[n-1] - a[0}) plus the sum of (a[s_i-1} - a[s_i} ). Wait, because each term (a[s_i-1} - a[s_i} ) is subtracted from the sum_ends - sum_starts. Wait, no. Let's recheck:

sum_ends - sum_starts = (sum of (a[s_i-1} for i in 1..k-1) + a[n-1} ) - (a[0} + sum of (a[s_i} for i in 1..k-1) )

= (sum of (a[s_i-1} - a[s_i} ) for i in 1..k-1) ) + (a[n-1} - a[0} )

So total cost is (a[n-1} - a[0} ) + sum_{i=1 to k-1} (a[s_i-1} - a[s_i} )

But since a[s_i-1} <= a[s_i} (because the array is sorted), each term (a[s_i-1} - a[s_i} ) is <= 0. So to minimize the total cost, we need to choose split points such that the sum of these terms is as small as possible (i.e., as negative as possible). But wait, wait. The total cost is (a[n-1} - a[0} ) + sum (a[s_i-1} - a[s_i} ). Let's call this sum S. So S = (a[n-1} - a[0} ) + sum (each term).

Each term in the sum is (a[s_i-1} - a[s_i} ), which is non-positive. So the sum of these terms is non-positive. Therefore, adding this sum to (a[n-1} -a[0}) reduces the total cost. But since we need to find the minimal possible total cost, we want the sum of the terms (a[s_i-1} - a[s_i} ) to be as small as possible (i.e., as negative as possible), so that the total cost is minimized.

Wait, no. Because the sum of (a[s_i-1} - a[s_i} ) is the sum of (s_i-1 term - s_i term), which is the same as (a[s_1-1} - a[s_1} ) + (a[s_2-1} -a[s_2} ) + ... + (a[s_{k-1}-1} -a[s_{k-1}} )

Each of these terms is (a[x] - a[x+1} ), where x is s_i-1. Since the array is sorted in non-decreasing order, a[x] <= a[x+1}, so each term is <=0. So the sum is a non-positive value.

So the total cost is (a[n-1} - a[0}) + (sum of terms). Since the sum is non-positive, adding it to (a[n-1} - a[0}) gives a value <= a[n-1} - a[0}. So the minimal possible total cost is achieved when the sum of the terms is as small as possible (i.e., as negative as possible). Wait, no. Because sum of terms is a negative value. So the more negative the sum is, the smaller the total cost. Because adding a more negative number (sum) reduces the total.

Wait, for example, (a[n-1} -a[0}) is a fixed value. Let's say it's 10. Then, sum of terms could be -5, making the total 5. Or sum could be -10, making total 0. So yes, we need to make the sum as small as possible (as negative as possible) to minimize the total cost.

So, the problem reduces to selecting k-1 split points such that the sum of (a[x] - a[x+1}) for each split point x is minimized (i.e., as negative as possible). Wait, each split is between x and x+1. For example, if we split after x, then x is the end of the previous subarray, and x+1 is the start of the next. So for this split, the term in the sum is a[x] - a[x+1}.

So, the sum of (a[x] - a[x+1}) for each split x. Each split x is between elements x and x+1. So each split corresponds to a position x (after element x). So, each split contributes a term of a[x] - a[x+1}.

We need to choose k-1 splits such that the sum of these terms is as small as possible (i.e., most negative). Because that would subtract the largest possible value from the (a[n-1} -a[0}) term, giving the minimal possible total cost.

But how do we do that? Because each split's term is a[x] -a[x+1}. Since a is non-decreasing, a[x] <= a[x+1}, so each term is <=0. So the sum is the sum of k-1 terms, each <=0. To make this sum as small as possible, we need to select the k-1 terms with the smallest (most negative) values.

Wait, no. For example, if the term a[x] -a[x+1} is -5, that's better (more negative) than -2. So to maximize the sum of the terms (since the sum is being added to the base cost), but wait, the sum of the terms is added to the base (a[n-1} -a[0}). Wait, no: the base is (a[n-1} -a[0}), then plus the sum of the terms (each of which is a[x] - a[x+1} for each split x). So the total cost is (a[n-1} -a[0}) + sum_{splits} (a[x] -a[x+1}).

So, the sum of the terms is sum (a[x] -a[x+1}) = sum (each split x contributes (a[x] -a[x+1} )).

But this can be rewritten as sum (a[x] -a[x+1} ) = sum (a[x]) for x in splits minus sum (a[x+1}) for x in splits.

But perhaps that's not helpful. Let's think of it differently.

Each split x (the split is between x and x+1) contributes (a[x] -a[x+1}) to the sum. So, the sum is sum over all splits x of (a[x] - a[x+1}).

But since each split x is a position between elements, we can select any k-1 positions. The problem is to choose k-1 positions such that the sum of (a[x] -a[x+1}) is as small as possible (most negative).

So, the approach is to choose the k-1 splits where the value (a[x] -a[x+1}) is the smallest (most negative) possible. Because each such split adds that value to the sum, which reduces the total cost.

But wait, because the sum of these terms is added to (a[n-1} -a[0}), which is fixed. So the minimal total cost is achieved by making the sum of these terms as small as possible. So, select the k-1 splits where (a[x] -a[x+1}) is the smallest possible. For example, if a[x] -a[x+1} is very negative, including it in the sum will reduce the total cost.

So, the solution is to select the k-1 splits with the smallest (a[x] -a[x+1}) values. Because each split's contribution is a[x] -a[x+1}, which is the difference between adjacent elements. So the minimal sum is achieved by taking the k-1 smallest differences (most negative) between consecutive elements. Wait, wait: because the sum is the sum of (a[x] -a[x+1}) for each split x. So, each term is (a[x] -a[x+1}) = -(a[x+1} - a[x}).

So the sum of these terms is equal to sum (a[x] -a[x+1}) = -sum (a[x+1} - a[x} ), for x in the splits.

So the sum is equal to the negative sum of the differences between consecutive elements at the split points. So, to minimize the sum (which is the negative of the sum of the split differences), we need to select splits where the differences (a[x+1} -a[x}) are the largest. Because summing those differences gives the largest possible positive sum, which when multiplied by -1 gives the most negative sum. Hence, the sum of (a[x] -a[x+1}) is minimized (most negative) when we select the splits where the differences (a[x+1} -a[x}) are the largest.

Ah! So here's the key insight. Let's rephrase:

The sum of the split terms is sum (a[x] -a[x+1} ) for each split x. Which is equal to - sum ( (a[x+1} - a[x}) for each split x). So, the sum is the negative of the sum of the differences between the elements at the split points. So, to minimize the sum (make it as small as possible), we need to maximize the sum of (a[x+1} -a[x}) for the split points. Because then, the negative sum would be as large in magnitude as possible, making the total sum as small (negative) as possible.

Thus, the optimal strategy is to select the k-1 splits where the differences a[x+1} -a[x} are the largest. Then, the sum of these differences is maximized, and the sum of (a[x] -a[x+1}) is minimized (most negative), leading to the minimal total cost.

Therefore, the solution is:

1. Compute all possible differences between consecutive elements. There are n-1 such differences (since the array has n elements, there are n-1 adjacent pairs).

2. Select the top k-1 largest differences. These will correspond to the splits that will be made. For example, if the largest difference is between x and x+1, we split here to take advantage of this large difference. Because by splitting here, we subtract this large difference from the total cost.

3. The minimal total cost is (a[n-1] -a[0}) minus the sum of these k-1 largest differences.

Wait, no. Wait, the sum of (a[x] -a[x+1}) is equal to -sum of (a[x+1} -a[x}) for the split x. So the total cost is (a[n-1} -a[0}) + sum (a[x] -a[x+1} ) for splits x. Which is equal to (a[n-1} -a[0}) - sum (a[x+1} -a[x} ) for splits x.

So the total cost is (a[n-1} -a[0}) minus the sum of the differences at the split points. So, to minimize the total cost, we need to maximize the sum of the differences at the split points. So, select the k-1 largest differences and subtract their sum from the initial difference (a[n-1} -a[0}).

So, the minimal total cost is (a[n-1} - a[0}) - sum of the k-1 largest adjacent differences.

So the steps are:

- Compute all adjacent differences (a[i+1] - a[i] for i from 0 to n-2).

- Find the top k-1 largest of these differences.

- Sum those top k-1 differences.

- Subtract that sum from (a[-1] - a[0}).

Thus, the answer is (a[-1] - a[0}) - sum_of_largest_k-1_differences.

This approach has a time complexity of O(n), which is acceptable for n up to 3e5.

Let me test this logic against the examples.

First example:

Input:

6 3

4 8 15 16 23 42

The differences are:

8-4=4

15-8=7

16-15=1

23-16=7

42-23=19

So adjacent differences are [4,7,1,7,19].

We need to choose k-1=2 largest differences. The two largest are 19 and 7. Or wait, sorted in descending order: 19,7,7,4,1. The top two are 19 and 7 (the first two 7s? Wait, the differences are [4,7,1,7,19]. The largest is 19, then 7, then 7, then 4, then 1. So the two largest are 19 and 7. Sum is 26.

a[-1] - a[0} is 42-4=38. Then subtract 26: 38-26=12. Which matches the sample output.

Yes, correct.

Second example:

Input:

4 4

1 3 3 7

k=4. So k-1=3 splits. The array is split into 4 subarrays, each with one element. So all possible splits are made. The differences are 3-1=2, 3-3=0,7-3=4. We need to choose the 3 largest differences. There are 3 differences. All are selected. The sum is 2+0+4=6. a[-1] -a[0} =7-1=6. 6-6=0. Correct.

Third example:

Input:

8 1

1 1 2 3 5 8 13 21

k=1. So no splits. The total cost is a[-1] -a[0} =21-1=20. Which matches the sample.

So the logic holds. Therefore, the approach is to compute the sum of the k-1 largest adjacent differences, subtract that from the total difference between first and last elements.

So the steps to implement:

1. Read n and k.

2. Read the array.

3. Compute the list of adjacent differences (a[i+1] -a[i] for i in 0..n-2).

4. If there are no differences (n=1, but then k must be 1), then the cost is 0.

5. Sort the differences in descending order.

6. Take the first k-1 differences and sum them.

7. Subtract this sum from the (a[-1] -a[0}) to get the answer.

But wait, for n=3e5, sorting all the differences would take O(n log n) time. But n can be up to 3e5, and 3e5 log 3e5 is about 3e5 * 19 ≈5.7e6 operations, which is acceptable. However, in Python, using the built-in sort is O(n log n), which for 3e5 elements is manageable within 2 seconds.

Alternatively, we can compute the sum of the top k-1 elements without sorting the entire array, which would be O(n) time. How?

Yes. We can use a selection algorithm to find the k-1 largest elements. For example, using a heap-based approach. But for k up to 3e5, this might be efficient.

Wait, but for k-1 up to 3e5, building a heap of all elements and then extracting the top k-1 elements would take O(n + k log n) time. For example, if n is 3e5 and k is 3e5, then this would be O(n) time to heapify, and O(k log n) for extracting. Which for k=3e5 is 3e5 * 19 = 5.7e6 operations. That's manageable.

Alternatively, since the problem requires the sum of the k-1 largest elements, we can use a max-heap approach. But perhaps the simplest way is to sort the list in descending order and take the first k-1 elements.

So, in code:

Compute the list of differences.

Sort them in reverse order (descending).

Take the first (k-1) elements.

Sum them.

Subtract from (a[-1] - a[0}).

Thus, the code will be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if n == 0 or k == 0:

        print(0, file=output_stream)

    else:

        total = a[-1] - a[0]

        if k == 1:

            print(total, file=output_stream)

        else:

            diffs = [a[i+1] - a[i] for i in range(len(a)-1)]

            # take the top k-1 largest diffs

            diffs.sort(reverse=True)

            sum_max = sum(diffs[:k-1])

            print(total - sum_max, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4
1 3 3 7
""",
            "output": \
"""\
0
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

</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(a[-1] - a[0])
else:
    diffs = [a[i+1] - a[i] for i in range(n-1)]
    diffs.sort(reverse=True)
    sum_max = sum(diffs[:k-1])
    print(a[-1] - a[0] - sum_max)
```
