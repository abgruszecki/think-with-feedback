<think>
Okay, let's try to figure out this problem. So the problem is about performing at most k swaps in an array to maximize the maximum subarray sum. Hmm.

First, I need to understand what the maximum subarray sum is. Oh right, that's the Kadane's algorithm problem. But here we can swap elements up to k times to maximize this sum. The challenge is to find the optimal swaps to do this.

Constraints: n is up to 200, which isn't too big. But k is up to 10. Wait, but trying all possible swaps for each step would be computationally expensive. So I need a dynamic programming approach here.

Let me think. For each step, how can we model the state? Maybe the state represents the number of swaps used so far, and for each state, we track the best possible elements in certain positions. But how?

Alternatively, since we can swap any two elements, perhaps the optimal strategy is to swap the largest elements into the positions that contribute the most to the maximum subarray. But that's vague. Let's think more carefully.

The maximum subarray can be any contiguous subarray. If we can choose which elements are part of that subarray, then perhaps the best approach is to select a subarray and swap the largest elements from the rest of the array into this subarray to maximize their sum.

Wait, but the order of swaps matters. For example, for a given subarray [l..r], the sum is the sum of the elements in that range. To maximize it, we can swap the largest possible elements into this subarray, replacing the smallest ones. So for each possible subarray [l..r], we can consider how many swaps we can perform to replace the smallest elements in [l..r] with the largest elements outside [l..r].

So the idea would be:

1. For every possible subarray [l..r], calculate the initial sum.
2. Then, collect the elements inside [l..r], sort them in ascending order (so the smallest are first).
3. Collect the elements outside [l..r], sort them in descending order (so the largest are first).
4. For each possible number of swaps s (from 0 to min(k, len(inside))), take the s largest elements from outside and replace the s smallest elements in the subarray. The maximum possible sum would be the initial sum of the subarray minus the sum of the s smallest elements in the subarray plus the sum of the s largest elements from outside.
5. Keep track of the maximum sum across all possible l, r, and s (where s <= k and the available elements allow).

So the plan is:

- Generate all possible subarrays [l..r].
- For each such subarray, collect the elements inside and outside.
- Sort the inside elements in ascending order (to take the smallest s elements to replace).
- Sort the outside elements in descending order (to take the largest s elements to bring in).
- For s from 0 to min(k, possible swaps for this subarray), compute the possible sum after s swaps and track the maximum.

The key here is to consider all possible subarrays and for each, compute the best possible gain by swapping up to k elements from outside into the subarray.

But how to efficiently compute this for all possible subarrays?

The constraints are n=200, so the number of subarrays is O(n^2) = 200*200 = 40,000. For each subarray, we need to process up to k swaps. Let's say k is 10. So total operations would be 40,000 * 10 = 400,000, which is manageable.

So steps for the algorithm:

1. Precompute all possible subarrays [l..r] (1-based? 0-based? Doesn't matter as long as we handle it correctly).

2. For each [l..r]:
   a. Collect elements inside: inside = a[l..r]
   b. Collect elements outside: outside = a[0..l-1] + a[r+1..n-1]
   c. Sort inside in ascending order (so we can replace the smallest s elements)
   d. Sort outside in descending order (so we can take the largest s elements)
   e. Precompute the prefix sums for inside (sum of the first t elements) and outside (sum of the first t elements)
   f. For s in 0 to min(k, len(inside), len(outside)):
      i. Take s elements from inside (smallest) and replace with s elements from outside (largest)
      ii. The gain is (sum of outside elements) - (sum of inside elements)
      iii. The new sum is original_sum - (sum of inside elements) + (sum of outside elements)
      iv. Track the maximum sum across all s (up to k swaps allowed)

3. The maximum of all these possibilities is the answer.

Wait, but the original sum of the subarray is the sum of all elements in [l..r]. When we replace s elements, we subtract the s smallest elements and add s largest from outside.

So for each s from 0 to min(k, len(inside), len(outside)), compute the sum as original_sum + (sum of top s outside elements - sum of bottom s inside elements).

We need to precompute the prefix sums for the sorted inside (ascending) and outside (descending).

For example, sorted_inside = sorted(inside) (ascending order). The sum of the first s elements is sum( sorted_inside[:s] )

sorted_outside = sorted(outside, reverse=True). The sum of the first s elements is sum( sorted_outside[:s] )

Then for each s, the maximum possible sum for this subarray with s swaps is original_sum - sum_inside_s + sum_outside_s.

But s can't be larger than the length of inside (since we can't replace more elements than are in the subarray), and also can't be larger than the length of outside (since you need elements to swap in). So s_max = min(k, len(inside), len(outside)).

So for each subarray and each possible s (from 0 to s_max), compute the sum as original_sum + (sum_outside_s - sum_inside_s) and check if it's better than the current maximum.

The original sum is fixed for the subarray. So for each subarray, we can precompute the sorted_inside and sorted_outside, then compute the prefix sums once for all s.

So the algorithm would work as follows.

Now, let's think about edge cases. For example, if all elements are negative. Then the best is to choose the maximum single element (since any swap won't help if all are negative, but maybe if k is enough to swap to bring a larger element in. Wait, but in the sample input 2, all are -1. So after any swaps, the max subarray is still -1. So the answer is -1.

Another case: when the subarray is the entire array. Then there are no elements outside. So the maximum swaps possible would be zero, unless we can swap elements within the subarray. Wait, but swapping elements within the subarray (since the entire array is the subarray) can help. But in that case, how? Because the maximum subarray would be the entire array. So swapping elements within the array can help maximize the sum, but in this approach, when the subarray is the entire array, the outside elements are empty, so no swaps can be done (since you need elements from outside). Wait, no. Because the entire array's inside is all elements. The outside is empty. So you can't take any elements from outside. So for the subarray [1..n], the only possible s is zero. So the sum would be the sum of the entire array. But maybe if you can swap elements inside the subarray (the entire array) to arrange them in a way that the sum is higher. For example, if you have a subarray of [3, -5], the sum is -2. But swapping the two elements would make the sum -2. So no change. Wait, but the maximum subarray can be a single element. So in that case, swapping would allow us to have the maximum element in a position. Wait, but in this approach, the swaps can be used anywhere in the array, but the approach is considering for each possible subarray the best possible swaps that replace elements in that subarray with elements outside. So if the entire array is the subarray, you can't swap any elements from outside (since there are none), but you can swap elements within the subarray. However, in that case, the sum of the entire array remains the same. So swapping elements within the subarray (the entire array) doesn't change the sum. So the maximum subarray sum could be the same as the sum of the array, or possibly a different subarray.

Wait, but in the approach I outlined earlier, when the subarray is the entire array, then swapping elements inside the array can't be captured by this method. Because the swaps are considered as replacing elements in the subarray with elements from outside. So in this case, when the subarray is the entire array, the outside is empty. So we can't perform any swaps in this approach. But that's a problem because swapping elements within the subarray could allow us to have a higher maximum subarray sum. For example, consider an array like [5, -2, 3]. The sum of the entire array is 6. But the maximum subarray is the entire array. If we can swap the -2 with a 10 (if there was one in the array), but if not, then swapping within the subarray (entire array) might not help. Hmm.

Wait, but in this problem, the swaps can be between any two elements. So when you swap elements inside the subarray, the sum of that subarray remains the same. However, the maximum subarray could be a different subarray after the swaps. But in our approach, for each possible subarray, we are considering replacing elements in that subarray with elements from outside. So when considering other subarrays, their swaps could include elements that are part of the array but outside the subarray. So perhaps the approach is correct because for the maximum subarray, even if it's a part of the array, the swaps that could help it are the ones where we take elements from outside that subarray and replace elements inside it. But in cases where the maximum subarray is part of the array and swapping elements inside the array can lead to a better sum, how do we capture that?

Wait, perhaps the approach is missing some possibilities. For example, suppose we have a subarray [1..3], and after swapping some elements within the array (but not in the subarray), the elements in the subarray could have higher values, leading to a higher sum. But in our approach, when considering this subarray [1..3], the outside elements are the ones not in this subarray. If we swap elements outside the subarray, but those elements are swapped with others outside the subarray, that wouldn't affect the sum of [1..3]. So perhaps the approach is not considering all possible swaps that could affect the maximum subarray sum.

Hmm, this is a problem. Because swapping elements not in the current subarray could affect the maximum sum in other subarrays. For example, swapping elements outside of [l..r] might allow a different subarray [l'..r'] to have a higher sum. But in our approach, we only consider swaps that replace elements inside [l..r] with elements outside. So the approach might not capture all possible scenarios.

Wait, but the key observation here is that the maximum sum after swaps can be achieved by selecting a subarray and making that subarray as strong as possible (by swapping in the best possible elements). Even if other subarrays could be considered, the maximum is achieved by focusing on a particular subarray and optimizing it with swaps.

So, for example, the optimal strategy would be to pick some subarray [l..r], then take the best possible elements from the entire array (excluding [l..r]) and swap them into [l..r], replacing the worst elements in [l..r]. Thus, the approach of considering all possible subarrays and for each, calculate the maximum possible sum after up to k swaps (replacing elements in the subarray with elements outside) is correct.

But what about cases where we swap elements within the array, but not into the subarray? For example, suppose there's a subarray [a, b] where a and b are negative. But if we swap two elements outside of [a, b], such that some other subarray becomes better.

But in that case, the approach would not capture that. So, perhaps the approach is incomplete. However, given the constraints of k up to 10 and n up to 200, perhaps considering all possible subarrays and their best possible swaps is manageable, but how do we account for swaps that are not part of any particular subarray's swaps?

Wait, but when you swap elements, you can do it to improve multiple subarrays. However, the maximum subarray sum is the maximum over all possible subarrays. So the optimal solution would be the maximum subarray after making swaps. So the swaps should be chosen to maximize the maximum subarray.

But how to model that? Because each swap can affect multiple subarrays.

This seems complicated. So maybe the approach is to consider that the optimal maximum subarray after swaps is one where we have a subarray [l..r], and in this subarray, we have replaced up to k elements with the best possible elements from the rest of the array. Then, the maximum of these would be the answer.

But why is this correct? Let's see.

Suppose that after swapping, the maximum subarray is [l..r]. Then the optimal swaps would be to replace the worst elements in [l..r] with the best elements from outside. So, even if we perform swaps that affect other subarrays, the maximum is achieved by this particular [l..r] after replacing some elements.

So, the approach of considering all possible [l..r], and for each, compute the best possible sum after replacing up to k elements (from outside to inside [l..r]) would capture the correct answer.

But what if the optimal swaps include swapping elements not in any particular [l..r], but the maximum subarray is formed by combining some elements from the swaps?

For example, imagine an array like [10, -1, 2, 2, 2, 2, 2, 2, -1, 10]. The sample input. The optimal solution is to swap the two 10s into the middle, forming a subarray of 10, 10, which gives sum 20. But according to the sample output, the answer is 32, which suggests that the maximum subarray is longer. Let me look at the sample input again.

Sample input 1:

10 2

10 -1 2 2 2 2 2 2 -1 10

So the array is [10, -1, 2, 2, 2, 2, 2, 2, -1, 10]. The maximum after two swaps would be to swap the two -1's (at positions 2 and 9) with the two 10s (positions 1 and 10). So the array becomes [ -1, -1, 2, 2, 2, 2, 2, 2, 10, 10]. Then the maximum subarray is from position 9 to 10: sum 20. Wait, but the sample output is 32. Oh, perhaps I got the sample input wrong. Let me check.

Wait the sample input is 10 2 followed by 10 -1 2 2 2 2 2 2 -1 10.

Original array: [10, -1, 2, 2, 2, 2, 2, 2, -1, 10]. So the two 10s are at the ends, and the middle is 2s. The two -1s are at positions 2 and 9.

When we swap the two -1s (positions 2 and 9) with the two 10s (positions 1 and 10), the array becomes:

[ -1, 10, 2, 2, 2, 2, 2, 2, 10, -1 ].

Now, the maximum subarray is from position 2 to 9: 10 + 2*6 + 10 = 10 +12 +10 = 32. Which explains the sample output. So in this case, the swaps are between elements inside and outside the subarray. So the subarray is [2..9] in the original array (but after swaps, those positions are 10, 2, ..., 10). So the approach of considering the subarray [2..9], then replacing the two elements (the -1 and -1) with the two 10s from outside would give the maximum sum.

So in the approach, for the subarray [2..9], the inside elements are the two -1s and the six 2s. The outside elements are 10 and 10. So when we replace the two smallest elements (the -1s) with the two largest outside elements (10 and 10), the sum increases by (10 +10) - (-1 + -1) = 20 +2 = 22. The original sum for the subarray [2..9] is (-1) + 2*6 + (-1) = (-2) + 12 = 10. Adding 22 gives 32. Which matches the sample.

So the approach works here.

But in this case, the swaps are between elements outside and inside the subarray. So the approach correctly captures that.

So the key is that for each possible subarray, the best possible swaps are to take the s largest elements from outside the subarray and replace the s smallest elements inside the subarray, for s up to k. Then, the maximum of all these possibilities is the answer.

Therefore, the approach is correct.

Now, the next step is to implement this.

Let's outline the steps for the code.

First, read n and k.

Then read the array a.

Initialize the maximum answer to negative infinity.

For each possible subarray [l..r], 0 <= l <= r < n (assuming 0-based indices):

- Collect the elements inside: inside = a[l:r+1]

- Collect the elements outside: outside = a[0:l] + a[r+1:n]

- Sort inside in ascending order (so the first s elements are the smallest)

- Sort outside in descending order (so the first s elements are the largest)

- Precompute the prefix sums for inside and outside.

For inside, the prefix sum after taking i elements is sum(inside[0...i-1]).

For outside, the prefix sum after taking i elements is sum(outside[0...i-1]).

Compute the original sum of the subarray: sum_initial = sum(inside).

Now, for s in 0 to min(k, len(inside), len(outside)):

   if s is 0: the sum is sum_initial.

   else:

      sum_swapped = sum_initial - sum_inside_prefix[s] + sum_outside_prefix[s]

   compare this sum with the current maximum and update.

So, for each s from 0 up to min(k, len(inside), len(outside)), compute the possible sum and track the maximum.

But we can precompute the prefix sums for inside and outside once per subarray.

So, for each subarray [l, r], we do the following:

inside = a[l..r]

sum_initial = sum(inside)

sorted_inside = sorted(inside)  # ascending

sorted_outside = sorted(outside, reverse=True)  # descending

precompute the prefix sums for sorted_inside and sorted_outside.

sum_inside = [0]*(len(inside)+1)

sum_outside = [0]*(len(outside)+1)

for i in range(len(inside)):

   sum_inside[i+1] = sum_inside[i] + sorted_inside[i]

for i in range(len(outside)):

   sum_outside[i+1] = sum_outside[i] + sorted_outside[i]

Then, for s in 0 to min(k, len(inside), len(outside)):

current_sum = sum_initial - sum_inside[s] + sum_outside[s]

if current_sum > max_sum:

   max_sum = current_sum

Also, note that for s=0, sum_inside[0] is 0, sum_outside[0] is 0, so current_sum is sum_initial.

So this covers all possible swaps for each subarray.

Now, considering all possible subarrays and s up to k, the maximum of all these is the answer.

But what about the case where the maximum is achieved by a subarray that is not modified by swaps? For example, a subarray that already has the maximum sum possible, and no swaps are needed.

The code would handle that, as s can be zero.

Another edge case: when k is zero. Then, the answer is the maximum subarray sum of the original array.

Another case: when all elements are negative. Then, the answer is the maximum single element (since the maximum subarray can't be improved by swapping unless there's a larger element, but if all elements are the same, like in sample input 2, the answer is that element.

So this approach should handle all cases.

Now, implement this in Python.

But with n=200, the number of subarrays is 200*201/2 = 20,100. For each subarray, we process up to min(k, len(inside), len(outside)) steps, which is up to 10. So total steps are 20,100 * 10 = 201,000, which is acceptable.

Now, code.

First, read n and k.

Then read the array as a list.

Initialize max_sum to the maximum possible minimum (e.g., -infinity).

Then, for l in 0 to n-1:

   for r in l to n-1:

      inside = a[l:r+1]

      outside = a[0:l] + a[r+1:n]

      sorted_inside = sorted(inside)

      sorted_outside = sorted(outside, reverse=True)

      sum_initial = sum(inside)

      # compute prefix sums for inside and outside

      sum_in = [0]

      for num in sorted_inside:

          sum_in.append(sum_in[-1] + num)

      sum_out = [0]

      for num in sorted_outside:

          sum_out.append(sum_out[-1] + num)

      # compute maximum possible s swaps for this subarray

      max_possible_swaps = min(k, len(sorted_inside), len(sorted_outside))

      for s in range(0, max_possible_swaps +1):

          if s > len(sum_in)-1 or s > len(sum_out)-1:

              continue  # but this should not happen due to max_possible_swaps

          current = sum_initial - sum_in[s] + sum_out[s]

          if current > max_sum:

              max_sum = current

So, this code would loop through all possible subarrays and compute the maximum possible sum after s swaps.

Now, handling the case where outside is empty. For example, when the subarray is the entire array. Then sorted_outside is empty. So max_possible_swaps is min(k, len(inside), 0) → 0. So s can only be 0, so current is sum_initial.

Which is correct.

In the sample input 2, where all are -1, and k is 10, the code would iterate all possible subarrays. For each subarray, the inside is a collection of -1's. The outside for a subarray of length 1 (say, l=r) would have n-1 elements of -1. So sorted_inside is [-1], sorted_outside is sorted descending (so all -1's). sum_initial is -1. For s=0: sum is -1. For s=1: sum_initial - (-1) + (-1) → -1 +1 -1 = -1. So no improvement. Hence, the maximum remains -1.

Which is correct.

Another test case: when the array is [3, -1, 4, -1, 5], and k=2. The best would be to swap the two -1's with the 3 and 5 (if possible). Wait, but that depends on the subarray. For example, if the subarray is [2,3,4] (the elements 4, -1, 5), then the inside is [4,-1,5]. The outside is [3, -1]. sorted_inside is [-1,4,5], sum_initial is 8. The outside sorted is [3, -1]. So for s=1: replace -1 with 3. sum becomes 8 - (-1) +3 = 12. For s=2: replace two elements. The sorted_inside has two elements to replace (s=2, but the sorted_inside has 3 elements). The two smallest are -1 and 4. But the outside has two elements (3 and -1). So replacing with 3 and -1. Sum would be 8 - (-1+4) + (3 + (-1)) = 8-3 +2 =7. Which is worse than s=1. So the maximum for this subarray is 12.

So code would pick that, but maybe there's a better subarray. For example, if the subarray is the entire array. Then outside is empty. So no swaps allowed. Sum is 3-1+4-1+5= 10. But swapping elements within the array (but the code's approach wouldn't consider that). But in that case, even if you swap elements within the array, the sum of the entire array remains 10, but the maximum subarray could be a single element. For example, swapping 3 and 5 would make the array [5, -1,4,-1,3]. The entire array sum is 5-1+4-1+3=10. But the maximum subarray is the first element (5) if we can't find a better one. But in the code's approach, considering the subarray [0..0] (the first element), inside is [3]. The outside is [ -1,4,-1,5]. sorted_inside is [3]. sorted_outside is [5,4,-1,-1]. For s=1, replacing 3 with 5. So sum is 5. Which is better than 3. So the code would capture that. So the maximum sum would be 12 (from the previous example), but this would give 5. Wait, no. The code would consider all possible subarrays and their possible swaps.

So the code's approach covers all possibilities.

So the code is correct.

Now, code in Python.

But to optimize for speed, perhaps precompute the sorted and prefix sums efficiently.

Also, in Python, for a list, a[l:r+1] gives the elements from index l to r inclusive (since r+1 is exclusive). But Python uses 0-based indices.

So the code:

Read n, k.

Read list a (assuming 0-based).

Initialize max_sum to negative infinity.

Then loop l from 0 to n-1:

   for r in range(l, n):

      inside = a[l : r+1]

      outside = a[:l] + a[r+1:]

      # sort inside in ascending order

      sorted_inside = sorted(inside)

      # sort outside in descending order

      sorted_outside = sorted(outside, reverse=True)

      sum_initial = sum(inside)

      # compute prefix sums for inside and outside

      sum_in = [0]

      current_sum = 0

      for num in sorted_inside:

          current_sum += num

          sum_in.append(current_sum)

      sum_out = [0]

      current_sum = 0

      for num in sorted_outside:

          current_sum += num

          sum_out.append(current_sum)

      # calculate maximum possible swaps s

      max_swaps = min(k, len(sorted_inside), len(sorted_outside))

      for s in range(0, max_swaps +1):

          # s can be up to max_swaps

          # sum_in[s] is sum of s smallest elements in inside

          # sum_out[s] is sum of s largest elements in outside

          current = sum_initial - sum_in[s] + sum_out[s]

          if current > max_sum:

              max_sum = current

So, this should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    max_sum = -float('inf')

    for l in range(n):
        for r in range(l, n):
            inside = a[l:r+1]
            outside = a[:l] + a[r+1:]
            sorted_inside = sorted(inside)
            sorted_outside = sorted(outside, reverse=True)
            
            sum_initial = sum(inside)
            sum_in = [0]
            current = 0
            for num in sorted_inside:
                current += num
                sum_in.append(current)
            
            sum_out = [0]
            current = 0
            for num in sorted_outside:
                current += num
                sum_out.append(current)
            
            max_swaps = min(k, len(sorted_inside), len(sorted_outside))
            for s in range(max_swaps + 1):
                current_sum = sum_initial - sum_in[s] + sum_out[s]
                if current_sum > max_sum:
                    max_sum = current_sum

    print(max_sum, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 10
-1 -1 -1 -1 -1
""",
            "output": \
"""\
-1
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

Another sample input:

5 10

-1 -1 -1 -1 -1 → all elements are -1.

For any subarray, inside is all -1's. outside has len (5 - (r-l+1)) elements. For example, a subarray of length 1 (l=r):

inside is [-1], outside is 4 elements of -1.

sorted_inside is [-1], sorted_outside is sorted in descending order → [-1, -1, -1, -1].

sum_initial is -1.

sum_in is [0, -1].

sum_out for s=0:0, s=1: -1.

max_swaps = min(10, 1, 4) → 1.

s can be 0 and 1.

s=0: sum is -1.

s=1: sum_initial - (-1) + (-1) → -1 +1 -1 =-1.

So no improvement. Thus, the maximum remains -1.

So code works.

Thus, the code should handle all cases correctly.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
max_sum = -float('inf')

for l in range(n):
    for r in range(l, n):
        inside = a[l:r+1]
        outside = a[:l] + a[r+1:]
        sorted_inside = sorted(inside)
        sorted_outside = sorted(outside, reverse=True)
        
        sum_initial = sum(inside)
        sum_in = [0]
        current = 0
        for num in sorted_inside:
            current += num
            sum_in.append(current)
        
        sum_out = [0]
        current = 0
        for num in sorted_outside:
            current += num
            sum_out.append(current)
        
        max_swaps = min(k, len(sorted_inside), len(sorted_outside))
        for s in range(max_swaps + 1):
            current_sum = sum_initial - sum_in[s] + sum_out[s]
            if current_sum > max_sum:
                max_sum = current_sum

print(max_sum)
```
