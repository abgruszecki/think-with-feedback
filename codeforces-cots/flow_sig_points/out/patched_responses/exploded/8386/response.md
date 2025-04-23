<think>
Okay, let's try to solve this problem. Hmm. So the problem is about minimizing the sum of squared differences between two arrays after performing some operations. We have to do exactly k1 operations on A and k2 on B. Each operation is increasing or decreasing an element by 1. 

First, I need to understand what's the best way to allocate these operations to minimize the total error. Let's think about each element individually. For each i, the initial difference is a_i - b_i. Then, each operation on a_i changes this difference by +1 or -1, and similarly for operations on b_i. Wait, no. Because if I increase a_i by 1, the difference (a_i - b_i) increases by 1. If I increase b_i by 1, the difference decreases by 1. So the net effect of using x operations on a_i and y operations on b_i would be that the difference becomes (original difference) + x (from a) - y (from b). But each operation is either on A or B. Wait, but each operation is a single change. So for each element, the total change in the difference (a_i - b_i) is the sum of operations applied to a_i (each +1 or -1 per operation) minus the sum of operations applied to b_i (each +1 or -1 would subtract from the difference). Wait, no. Let me clarify:

If I have a_i' = a_i + delta_a (where delta_a could be + or - per operation) and b_i' = b_i + delta_b, then the new difference is (a_i + delta_a) - (b_i + delta_b) = (a_i - b_i) + (delta_a - delta_b). So each operation on a_i adds 1 or subtracts 1 (depending on the direction) to the difference, and each operation on b_i subtracts 1 or adds 1 (since delta_b is +1 or -1). 

But since the goal is to minimize the sum of squares of these differences, for each element, the optimal way is to make the absolute difference as small as possible. However, the operations are split between A and B, and the total operations (k1 + k2) can be applied across all elements.

Wait, but the operations are split: exactly k1 on A (any elements) and exactly k2 on B (any elements). So the total number of operations available is k1 + k2, but they are allocated to A and B. For example, if I have to use exactly k1 on A and k2 on B, how to distribute them across elements to minimize the sum.

So the key is that for each element, the net change in the difference (a_i - b_i) is (delta_a_i - delta_b_i), where delta_a_i is the total number of operations applied to a_i (could be positive or negative, but since each operation is +1 or -1, the total delta_a_i is the sum of those). Wait, no. Each operation on a_i can be adding or subtracting. But when the problem says "exactly k1 operations on array A", each operation is a single increment or decrement. So for each element in A, we can apply some number of operations (each being +1 or -1), but the total number of operations across all elements in A must be exactly k1, and similarly for B.

But perhaps it's better to model this as: for each element i, we can choose to use x_i operations on a_i and y_i operations on b_i, such that sum over all x_i = k1 and sum over all y_i = k2. Then the new difference for i is (a_i + x_a_i_sign * x_i) - (b_i + y_i_sign * y_i). Wait, but the operations can be either increments or decrements. So for each operation on a_i, we can choose to add or subtract 1. Similarly for B. 

But this seems complicated. Let's think differently. For each element i, the initial difference is d_i = a_i - b_i. After applying some operations, the new difference is d_i + delta_i, where delta_i is the net change from operations on a_i and b_i. Each operation on a_i (either +1 or -1) changes delta_i by +1 or -1. Each operation on b_i (either +1 or -1) changes delta_i by -1 or +1. Wait, no. Because if you add 1 to a_i, the difference increases by 1. If you subtract 1 from a_i, the difference decreases by 1. For b_i, adding 1 to it decreases the difference by 1, subtracting 1 increases the difference by 1. So each operation on A can contribute either +1 or -1 to delta_i. Each operation on B can contribute either -1 or +1 to delta_i. 

But since the goal is to minimize the sum of squares of the final differences, perhaps the optimal way is to arrange that delta_i is as close as possible to zero, given the number of operations available.

Wait, but the operations are applied across all elements. So for each element i, we can use some of the operations to reduce the squared term (d_i + delta_i)^2, but the total operations used (x_i from A and y_i from B) must sum to x_i's totaling k1 and y_i's totaling k2.

Hmm. Let's think: for each element i, the minimal contribution is when the difference is as small as possible. But given the total operations (k1 +k2), how to distribute them among the elements to minimize the sum.

Wait, but each operation on A is equivalent to a delta_i change of either +1 or -1. Similarly, each operation on B is equivalent to a delta_i change of either -1 or +1. So in the end, each operation (whether on A or B) can contribute either +1 or -1 to the delta_i of some element. Wait, but that's not correct. Because for example, if you apply an operation to a_i (adding 1), that's a delta_i of +1. If you apply an operation to a_i (subtracting 1), that's a delta_i of -1. Similarly, applying an operation to b_i (adding 1) is a delta_i of -1, and subtracting is +1. 

So the direction of the operation (whether you add or subtract) affects the delta_i. But since we want to minimize the sum of squares, for each operation, we should choose the direction that best reduces the squared term. 

But how do we model this? Because for each element, we can choose how many operations to apply to A and B, and the direction of each. But this seems complicated. 

Alternatively, perhaps the key insight is that the optimal way is to first compute the absolute differences |d_i|, and then apply the maximum possible number of operations to reduce these differences, using the available total operations (k1 +k2). Because the order in which we use A and B operations might not matter as much as the total number of operations applied to each difference. 

Wait, maybe we can model this as follows: the initial difference for each element is d_i = a_i - b_i. Each operation (whether on A or B) can adjust this difference by +1 or -1. So each operation is effectively a step that can decrease or increase |d_i|. To minimize the sum of squares, the optimal strategy is to use as many operations as possible to reduce |d_i|. However, since each operation can be applied to any element, and the direction (add or subtract) can be chosen optimally. 

So perhaps the problem can be transformed into: given the initial differences d_i, and a total of K =k1 +k2 operations, each of which can subtract 1 from the absolute value (i.e., reduce the absolute difference by 1), but after that, if there are remaining operations, we have to add them in a way that minimizes the sum of squares. 

Wait, here's the idea. For each element, the maximum possible reduction in the squared term is achieved by reducing the absolute difference. For example, if the initial difference is 5, and we can apply 3 operations, we can reduce it to 2, which gives a squared term of 4 instead of 25, saving 21. If we have more operations, we can make the difference even lower. 

But since each operation (whether from A or B) can be used to decrease |d_i| by 1, but the total number of operations is K. So the optimal way is to sort the differences in descending order of their absolute values. Then, for each operation, take the largest |d_i| and reduce it by 1. Repeat this for all K operations. Then, the sum of squares is minimized. 

But wait, in the problem statement, the operations are split into exactly k1 on A and exactly k2 on B. So the total K is k1 +k2. So the initial idea that the sum is k1 +k2 is the key here. Because regardless of which array's operations are used, each operation can be considered as a unit of "change" towards the total delta_i. 

So, the problem reduces to: we have K =k1 +k2 operations, and each operation can be used to adjust the difference (a_i -b_i) by either +1 or -1 (since each operation can be a subtraction from a_i, which is like adding -1 to a_i, hence +1 to the difference; or adding to a_i, which adds +1 to the difference. Or, for B's operations, subtracting from B adds +1 to the difference, adding to B subtracts 1 from the difference. But regardless of which array the operation is applied to, the direction can be chosen to optimally decrease the absolute value of the difference. 

So the key insight here is that the allocation of operations between A and B does not affect the minimal possible sum of squares. Because regardless of whether an operation is done on A or B, we can choose the direction (increment or decrement) such that the effect on the difference is the same. For example, to decrease the absolute value of the difference, suppose the current difference is positive. Then, applying an operation on A (decrement a_i by 1) would decrease the difference by 1. Alternatively, applying an operation on B (increment b_i by 1) also decreases the difference by 1. So in both cases, the effect is the same. Therefore, the sum of squares only depends on the total number of operations (k1 +k2), not on how they are split between A and B. 

Wait, that's a crucial observation. So the problem's constraints require that exactly k1 operations are on A and k2 on B, but the effect of those operations can be modeled as K =k1 +k2 total operations that can each adjust the differences (a_i -b_i) by +1 or -1 in the optimal direction. So the optimal way to minimize the sum is to use all K operations in the best possible way to minimize the sum of squares. 

Therefore, the split between k1 and k2 does not matter because any combination of using operations on A or B can be used to achieve the same effect. For example, if you need to apply 1 operation to A and 0 to B, you can choose to apply that operation on A in a way that reduces the difference. Similarly, if you have 0 on A and 1 on B, you can apply it on B to reduce the difference. So regardless of which array you apply the operation to, you can choose the direction (add or subtract) to have the same effect. 

So this means that the minimal sum of squares is determined by the total K =k1 +k2 operations, regardless of how they are split between A and B. But wait, but the problem says that exactly k1 operations must be performed on A and exactly k2 on B. But according to this logic, the split between A and B doesn't affect the sum. So maybe that's the case. 

If that's true, then the solution is to compute for each element the optimal way to adjust the difference using a total of K =k1 +k2 operations, and then the split between A and B is irrelevant. So the problem reduces to K operations that can be allocated to adjust the differences, and the sum is the same as if you had K operations, regardless of how they are split. 

But wait, that can't be right. Let's take the sample input 2:

Sample 2:

Input:

2 1 0

1 2

2 2

So the initial differences are (1-2) = -1 and (2-2) =0. The K is 1+0 =1. So we can apply one operation. The optimal is to use it on A to change the first element to 2, making the difference (2-2)=0. The sum is 0. 

Alternatively, if K is 1, but if you have to use 0 operations on A and 1 on B (but sample input is k1=1, k2=0), but in this case, the sample would require the operation to be on A. So the split between A and B is not arbitrary. But according to the previous logic, the split doesn't affect the sum, but in this case, the split is fixed. So how is that possible?

Wait, perhaps in the previous reasoning, the split between A and B can be arbitrary, but the problem requires that exactly k1 and k2 are used. So perhaps the split between A and B does not affect the minimal sum, and so the minimal sum can be computed as if we have K total operations, regardless of how they are split. 

In other words, the minimal sum is the same as if you have K operations, regardless of whether they are applied to A or B, because you can choose the direction of the operation (increase or decrease) to get the same effect. So the answer depends only on K, not on k1 and k2. So the answer is the same as if you had K =k1 +k2 operations. 

Wait, but the sample input 2:

Sample 2 input has K=1. The answer is 0. So in this case, the split between A and B (1 and 0) allows using the operation to adjust A. But if the split were 0 and 1, then you can adjust B. For example, in sample 2, if the problem allowed k1=0 and k2=1, then you can adjust B's first element by subtracting 1 (since B's element is 2; changing it to 1 would make the difference (1-1)=0. So the sum is also 0. So in either case, the sum is 0. 

So, regardless of whether the operation is applied to A or B, the sum can be the same. Hence, the split between A and B is irrelevant. Therefore, the problem can be reduced to finding the minimal sum of squares when we can apply K =k1 +k2 operations, each of which can be used to adjust the difference by +1 or -1. 

Thus, the steps to solve the problem are:

1. Compute the initial differences d_i = a_i - b_i for each element.

2. The goal is to apply exactly K =k1 +k2 operations (each operation can be a +1 or -1 on any d_i) to minimize the sum of squares of the new differences. 

3. The optimal way is to use the operations to reduce the absolute differences as much as possible.

So, the approach is:

- For each d_i, the best way to use x_i operations on it is to reduce |d_i| by x_i, but if x_i is more than |d_i|, then the remaining operations would increase the absolute difference again (but this is only when we have excess operations). 

So, the plan is:

- For each d_i, compute how much we can reduce its absolute value. The maximum possible reduction is min( K, |d_i| ). But since K is the total, we need to distribute the operations in a way that the largest possible reductions are done first.

Wait, this is similar to the problem where you have K operations to reduce the elements, and each operation reduces the absolute value by 1. The minimal sum of squares is achieved by taking the elements with the largest absolute values first, subtracting as much as possible. 

So the algorithm is:

1. Calculate the list of differences d_i = a_i - b_i.

2. Compute the absolute differences |d_i|.

3. Sort the |d_i| in descending order.

4. Use the K operations to reduce the largest |d_i| as much as possible. For each of the K steps:

   a. Take the largest current |d_i|.

   b. Reduce it by 1. 

   c. If it becomes zero, proceed to the next largest.

   d. If K is larger than the sum of all |d_i|, then after reducing all to zero, the remaining operations will toggle between 0 and 1. For even remaining K, all can be zeros again. For odd, one will be 1. 

So, after K operations, each |d_i| is reduced by as much as possible, with the largest ones first. 

But wait, after K operations, the sum of the squares will be the sum of the squares of the adjusted |d_i|. 

So the steps are:

- For each i, the adjusted value is:

   adjusted_i = |d_i| - x_i, where x_i is the number of operations allocated to this element. But x_i can't exceed |d_i|, and sum x_i <= K. However, if sum x_i < K, then the remaining K - sum x_i operations are distributed as follows: each remaining operation alternately adds and subtracts 1. But since they can be applied to any element, the minimal sum of squares is achieved by distributing the remaining operations as evenly as possible. 

Wait, for example, if after using all possible operations to reduce all |d_i| to zero, but K is larger than the sum of |d_i|, then the remaining operations would have to add to the differences. But each such operation would increase the absolute value by 1. However, because we can choose the direction, each such operation would contribute 1^2. So, if there are R = K - sum |d_i| remaining operations, then R can be even or odd. 

If R is even, the sum is (R/2)*1^2 + (R/2)*1^2 (since each pair of operations can be +1 and -1, but since the absolute value is squared, it doesn't matter). So the sum would be R. 

Wait no. For example, if R is even, then we can split the operations into R/2 increments and R/2 decrements, but that's not possible. Wait, no. Because each operation is a +1 or -1. Wait, after all |d_i| are zero, applying one operation would make one of the differences 1 or -1. Applying another operation could reduce it back to zero. So for even R, the sum would be zero. For odd R, the sum is 1. 

Wait, let's think:

Initial differences: all zeros.

K = 3. 

First operation: one element becomes 1. Sum is 1.

Second: another element becomes 1. Sum is 2. 

Third: any element can be adjusted. For example, subtract 1 from the first element (which was 1), making it 0. Sum becomes 1. 

So for K=3, the sum is 1. 

Alternatively, after each pair of operations (increase and decrease), the sum goes back to zero. So for even R, sum is zero; for odd R, sum is 1. 

Wait, this is only possible if R is even. Because each pair of operations (adding 1 and subtracting 1) cancels out, but each operation uses K. But perhaps the minimal sum is R % 2. Because if you have R operations left after all |d_i| are reduced to zero, then you can split them into pairs where each pair adds and subtracts 1, leading to no change, but for odd R, you have one operation left which adds 1 (or subtracts, but squared is same). So the sum would be 1 if R is odd, 0 if even. 

But that's only possible if you can split the operations into pairs. But the sum of squares is (1^2) for odd R and 0 for even. 

So the algorithm is:

Compute the sum of all |d_i|. Let total_reductions = sum |d_i|.

If K <= total_reductions:

   For each element, sort the |d_i| in descending order. Then, allocate K operations to the largest elements. For each of the largest elements, subtract 1 until K is exhausted. 

   The sum of squares is sum (max(|d_i| - x_i, 0))^2, where x_i is the number of operations allocated to that element.

Else:

   After reducing all |d_i| to zero, the remaining operations (R = K - total_reductions) can be used to add 1 to some elements. But since each operation can be paired (add 1 and subtract 1), the sum of squares would be R % 2 (if R is even, sum is 0; else 1).

Wait, that's the key. Because once all differences are zero, each additional operation must toggle between 1 and -1. But since the square is same, the sum would be R % 2. 

So the steps to compute the minimal sum are:

1. Compute all |d_i| where d_i = a_i - b_i.

2. Compute the sum of |d_i| as total_reductions.

3. If K <= total_reductions:

   - Sort the |d_i| in descending order.

   - Distribute the K operations to reduce the largest elements first. For example, subtract 1 from each largest until K is zero.

   - The remaining |d_i| (after reduction) are summed as squares.

4. Else:

   - R = K - total_reductions. The sum of squares is R % 2.

So the sum is R mod 2. Because each pair of operations can be applied to the same element, adding 1 then subtracting 1, leading to zero, but each uses two operations. If R is even, all pairs can be done, sum is zero. If R is odd, one operation remains, sum is 1.

So this is the approach.

Now, how to implement this.

First, compute the initial differences and their absolute values.

Then compute the total_reductions = sum of |d_i|.

If K <= total_reductions:

   Then, we need to subtract as much as possible from the largest elements.

   So, we can use a max-heap to track the largest elements. For each of the K operations, take the largest element, subtract 1, then put it back.

But with n up to 1e3 and K up to 1e3, this is feasible. Alternatively, we can sort the list in descending order and process the elements in a way that subtracts the maximum possible.

For example, let's sort the list in descending order. Then, for the K steps:

At each step, find the maximum current value, subtract 1, and then re-sort. But this is O(K * n log n), which with K=1e3 and n=1e3, would be 1e6 * 1e3 log n, which is 1e9 operations. That's way too slow.

Alternative approach: find the number of steps needed to bring the largest elements down.

For example, let's sort the list in descending order. Then, process the elements in a way that subtracts as much as possible.

We can model this as follows:

We have a list sorted in non-increasing order. Let's process the elements in such a way that we take the first element, and subtract as much as possible until the next element is larger than the current (or K is exhausted). 

This approach can be done in O(n) time for each step.

Alternatively, for example:

Suppose we have elements like [5, 4, 3, 2]. K = 5.

First, we can subtract 1 from 5, making it 4. Now the list is [4,4,3,2]. Then subtract another 1 from the first two 4's until they are equal to the next elements. 

Alternatively, the optimal way is to subtract 1 from the largest elements in each step.

But for K up to 2e3 (since k1 +k2 can be up to 1e3?), wait the problem statement says "0 ≤ k1 +k2 ≤ 1e3". So K is up to 1e3. So for K=1e3 and n=1e3, perhaps using a priority queue (max-heap) is feasible. Because each of the K steps requires a heap operation which is O(log n), leading to O(K log n) operations, which for K=1e3 and n=1e3 is acceptable (1e3 * 10 = 1e4 steps).

But in Python, using a max-heap can be implemented with heapq, which by default is a min-heap. So we can store the negative values.

So here's the plan:

Compute the list of absolute differences.

If K is 0: sum is sum of squares of d_i.

Else:

Compute the total_reductions. If K <= total_reductions:

   Create a max-heap (using negatives) of the absolute differences.

   For each operation in 1..K:

      take the largest element (pop the negative value, get the max).

      subtract 1.

      if the result is >0, push back into the heap.

      else, push 0 (but since we can't have negative, just push 0).

   Then, sum the squares of the elements in the heap plus any remaining elements.

Wait, no. The heap after K operations will have the modified absolute differences. Then sum the squares.

Else:

   The sum is (K - total_reductions) % 2.

So, let's see the sample input 3:

Sample 3:

n=2, k1=5, k2=7 → K=12.

A is [3,4], B is [14,4].

Initial differences:

3-14 = -11 → | -11 | =11

4-4=0 → |0|=0.

So sum_reductions is 11 +0=11. K=12.

Since 12 >11, sum is R=12-11=1, which is odd. So sum is 1. Which matches the sample output.

Sample 2:

Initial differences: -1 and 0 → absolute values 1 and 0. sum_reductions=1. K=1. So after using all 1 operations, the largest (1) is reduced to 0. The sum of squares is 0^2 +0^2=0. So sample 2's answer is 0.

Sample 1: K=0, sum is (1^2 +1^2) =2.

So this approach works.

Now, how to implement this in Python.

First, read the input.

n, k1, k2 = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

Then compute the absolute differences:

diffs = [abs(a[i] - b[i]) for i in range(n)]

total_reductions = sum(diffs)

K = k1 +k2

if K >= total_reductions:

    R = K - total_reductions

    print(R %2)

else:

    # Use a max heap to distribute the K operations.

    import heapq

    heap = [-x for x in diffs]  # max heap via min heap with negative values

    heapq.heapify(heap)

    for _ in range(K):

        current = -heapq.heappop(heap)

        current -=1

        heapq.heappush(heap, -current)

    # compute sum of squares

    total = 0

    for num in heap:

        total += (-num)**2

    print(total)

Wait, but when K is exactly total_reductions, then after all elements are zero, the sum is zero. Then, the code would compute sum of squares as zero. Which is correct.

But in the code, after K steps, which is K = total_reductions, each step reduces a element by 1. The heap becomes all zeros. So sum is zero.

Yes.

But in the code, for the else clause (K < total_reductions), the code would process each operation, subtract 1 from the largest, and push back. Then, sum the squares.

But wait, in the code, the elements in the heap are the absolute differences after K operations. So the sum of their squares is correct.

Yes.

This approach should handle all cases correctly.

Testing against sample input 2.

```python
import heapq


def main(input_stream, output_stream):
    n, k1, k2 = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    diffs = [abs(a[i] - b[i]) for i in range(n)]
    total_reductions = sum(diffs)
    K = k1 + k2

    if K >= total_reductions:
        remainder = (K - total_reductions) % 2
        print(remainder, file=output_stream)
    else:
        heap = [-d for d in diffs]
        heapq.heapify(heap)
        
        for _ in range(K):
            current = -heapq.heappop(heap)
            current -= 1
            heapq.heappush(heap, -current)
        
        min_error = sum((-x)**2 for x in heap)
        print(min_error, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 5 7
3 4
14 4
""",
            "output": \
"""\
1
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

Sample 3:

diffs [11,0]. K=12.

Since 12>11 → R=1 → sum is 1.

Sample 1:

K=0 → sum of squares 1^2 +1^2=2.

Yes.

Another test case: K=3, sum_reductions=2. Then R=1, sum is 1.

Another case: K=4, sum_reductions=3. R=1. sum is 1.

So code seems correct.

Now, the code's time complexity: For K up to 1e3, and each heap operation is O(log n) for n up to 1e3. So 1e3 * log(1e3) ≈ 1e3 *10 =1e4 operations. That's acceptable.

Space: O(n) for the heap. That's acceptable.

Thus, the code should work.
</think>

```python
import heapq

n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diffs = [abs(a[i] - b[i]) for i in range(n)]
total_reductions = sum(diffs)
K = k1 + k2

if K >= total_reductions:
    remainder = (K - total_reductions) % 2
    print(remainder)
else:
    heap = [-d for d in diffs]
    heapq.heapify(heap)
    
    for _ in range(K):
        current = -heapq.heappop(heap)
        current -= 1
        heapq.heappush(heap, -current)
    
    min_error = sum((-x)**2 for x in heap)
    print(min_error)
```
