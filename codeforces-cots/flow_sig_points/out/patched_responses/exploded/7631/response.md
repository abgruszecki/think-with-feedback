<think>
Okay, let's see. The problem is about replacing exactly one element in an array, then sorting it, and for each position, find the minimal possible value after these operations. Hmm. So the key here is to find for each position the smallest possible number that can be achieved by changing one element and then sorting.

First, I need to understand how replacing one element affects the sorted array. Let's think. The original array is sorted. Wait, no. Wait, after replacement, we sort the array. So regardless of the original order, after replacement, the array is sorted in non-decreasing order. But the original array might not be sorted. Oh, wait, no. The problem says that after the replacement, Petya sorted the array. So the replacement happens, then the array is sorted. So the order of elements before replacement doesn't matter because after replacement, the array is sorted. Wait, but the replacement is done on any element, and then the array is sorted. So the original array's order is irrelevant. Because after replacing one element, the array is sorted again. So, regardless of the original order, the final array is sorted. So the problem is essentially: find the minimal possible sorted array after replacing one element (with any value except itself) and then sorting.

Wait, but the replacement is of exactly one element. So we have to change exactly one element. So, the approach would be to consider all possible ways to replace one element in the array, then sort, and then for each position, find the minimal possible value.

But since n can be up to 1e5, we need an O(n) or O(n log n) solution. So iterating through each element and trying to replace it with the minimal possible value (1?), then seeing how that affects the sorted array, and then for each position, track the minimal possible value.

Wait, but the minimal possible array would be obtained by replacing the largest element in the array with 1. Because then, when sorted, 1 would be the first element, and others would shift accordingly. But that's not necessarily the case. For example, in the first sample input: 1 2 3 4 5. If we replace 5 with 1, the sorted array becomes [1,1,2,3,4]. Which gives the output as in the sample. But what if there's a way to get even lower numbers in other positions? Hmm, but according to the problem, each position's minimal possible value is required. So for each position i, what's the smallest possible value that can be there after replacing exactly one element and sorting.

The key insight here is that for each position i, the minimal possible value is the minimal between:

1. The scenario where we replace some element (could be any) with a value that allows the i-th position to be as small as possible.

But how do we model this?

Alternative approach: the minimal possible array (sorted) after replacing one element is the same as the array where we can take the original array, replace one element with the minimal possible (1), then sort, but also considering that we have to replace exactly one element. Wait, but if the original array already contains 1, then replacing another element with 1 could be better.

Alternatively, perhaps the optimal approach is to find the minimal possible array that can be obtained by replacing any element in the original array with a value (not equal to the original) and then sorting. Since after replacing, the array is sorted, the minimal array would have as many small elements as possible.

But how do we compute this for all positions?

Let's think: when we replace an element, the new element can be as small as possible (1), then the array is sorted. So for each possible candidate (each element in the array), replacing it with 1 (if possible) and then sorting. But since after replacement, the array is sorted, the minimal possible array would be the original array sorted, then replacing the largest element with 1 and re-sorting. Or perhaps replacing the largest element with 1 gives the minimal array.

Wait, but maybe there's a better way. For example, in the second sample input: 2 3 4 5 6. Replacing 2 with 1 gives [1,3,4,5,6] sorted as [1,3,4,5,6]. But the output is [1,2,3,4,5]. Wait, how does that happen? Oh, because in the sample input, the array is already sorted. So after replacing 2 (the first element) with 1, the sorted array becomes [1,3,4,5,6], but that's not the output. Wait, the sample output is 1 2 3 4 5. So how is that possible? Oh, maybe the sample input given isn't the original array. Wait, no. Wait, the second sample input is:

5
2 3 4 5 6

The output is 1 2 3 4 5.

So replacing the 2 with 1 would result in [1,3,4,5,6], sorted as [1,3,4,5,6], which would give output [1,3,4,5,6], but the sample output is [1,2,3,4,5]. So that's conflicting. Therefore, my previous assumption is wrong.

Hmm. So perhaps there's a different approach here.

Wait, in the second sample, the correct output is achieved by replacing 6 with 1. Then the array becomes [2,3,4,5,1]. After sorting, it's [1,2,3,4,5], which gives the desired output. So replacing the largest element with 1 gives a better result than replacing the smallest element. So in that case, replacing the largest element is better.

But why?

Ah, because when you replace the largest element with 1, inserting 1 into the array may allow the new minimal element to be 1, and the other elements shift. So perhaps the optimal way to minimize each position is to replace the largest element with 1. But that's not always the case.

Alternatively, perhaps the minimal possible array is obtained by replacing the largest element with 1, then sorting, but only if that actually changes the array. Otherwise, if all elements are 1, then you have to replace one of them with a different value (since you can't replace with the same value). Wait, but the problem says that the replacement must be exactly one element, which cannot be the same as the original. So if all elements are 1, we have to replace one of them with a different value (e.g., 2) and then sort.

So, the general approach is:

Find the minimal possible array after replacing exactly one element (with a different value) and then sorting. For each position in this array, output the minimal possible value.

So the problem is to find the array that is the sorted version of the original array with exactly one element changed (to a different value), and then determine for each position the minimal possible value.

The challenge is to compute this efficiently.

Let's think: for each possible replacement (any element in the array), replacing it with a value that allows the array to be as small as possible after sorting. So for each element in the original array, the best way to replace it is to make it as small as possible (i.e., 1, unless the original element is 1, in which case you have to replace it with something else, but then that would increase the array's elements. So perhaps replacing the element with 1 is the best option whenever possible.

But we have to replace exactly one element. So, for each element in the array, we can consider replacing it with the minimal possible value (1 if possible, otherwise something else), then compute the sorted array. Then, for all possible such replacements, track the minimal possible array (element-wise) after sorting.

But how to do this efficiently?

Wait, but considering all possible replacements is O(n), which is acceptable for n=1e5.

But how to find the minimal array after replacing each element and then merging all possibilities.

Wait, but the minimal array after replacing any element would be the sorted array with the minimal elements possible.

So the minimal possible array is the one where we have as many 1's as possible, but considering that exactly one element must be replaced.

Wait, but in the original array, there may already be 1's. For example, if the array has two 1's, then replacing one of them with 1 is not allowed (since the replacement must be different from the original). So in that case, we have to replace one of the 1's with a different number. But that would make the array worse. So in that case, perhaps replacing a different element (the largest one) with 1 is better.

So the approach is:

We can either replace the largest element with 1 (if possible), or if the array contains elements that are not 1, then replacing the largest element with 1 would give the minimal possible array.

But wait, for example, if the array is [2, 2, 2], replacing one of the elements with 1 would result in [1,2,2], which when sorted gives the minimal array. So the output in the third sample is 1 2 2.

Another example: the first sample input is [1,2,3,4,5]. Replacing 5 with 1 gives [1,1,2,3,4] when sorted, which is the sample output.

The second sample input is [2,3,4,5,6]. Replacing 6 with 1 gives [1,2,3,4,5], which is the sample output.

So the pattern here is that replacing the largest element with 1 gives the minimal possible array after sorting.

But is this always the case?

Suppose we have an array [5, 4, 3, 2, 1]. Then replacing the first element (5) with 1 gives [1,4,3,2,1], which when sorted becomes [1,1,2,3,4]. The minimal possible array. But if we replaced another element, like 4 with 1, the array after sorting would be [1, 1, 2, 3,5], which is worse for the last position.

So replacing the largest element (5 in this case) with 1 is better.

But what if the array is [3, 1, 2]. The largest element is 3. Replacing it with 1 gives [1,1,2], sorted. The output array would be [1,1,2], which for the second position is 1, which is better than if we replaced another element.

But the original array has one 1. If we replace 3 with 1, then the array is [1,1,2], which is better. So again, replacing the largest element with 1 is better.

Another example: array is [1, 3]. Replacing 3 with 1 is allowed (since it's different). The sorted array is [1,1]. So the output is [1,1].

But if the array is [1,1], then we have to replace one element with a value different from 1. So replacing one 1 with 0 (but the problem says the replacement must be between 1 and 1e9. So we can't use 0. So the replacement must be >=1 but not 1. So the minimal possible is 2. Then the array becomes [1,2], sorted. So the output is [1,2].

So in that case, replacing one 1 with 2 gives a worse array than if we had replaced another element. But in this case, all elements are 1, so the only option is to replace one with 2 (or higher), leading to the array [1,2], which is worse than the original array except for the first element. But since the original array was [1,1], replacing one with 2 gives the array [1,2], sorted. The output would be [1,2].

So the approach here is to find the minimal possible array after replacing exactly one element, which can be achieved by replacing the largest element with 1, unless that element is 1. But if all elements are 1, then we have to replace one with 2 (the next smallest possible), which gives the array [1,1,...2] sorted, which for the first n-1 positions is 1, and the last is 2.

So the general approach is:

1. Find the position of the maximum element in the array.

Wait, but there could be multiple maximum elements. For example, array [5,5,5]. Replacing any one of them with 1 gives [1,5,5] sorted as [1,5,5], which is better than replacing with any other value.

So, to minimize the array after replacement, the best is to replace the largest element (or one of them if there are multiple) with the smallest possible value (1, if possible). Because that will insert a 1 into the array, which when sorted will be the first element, and all others shift right. However, if the largest element is already 1, then all elements are 1, and replacing one with 2 is required.

So, the steps are:

- Find the maximum element in the array. Let's call it max_val.

- If max_val > 1: then the best way to minimize the array is to replace one occurrence of max_val with 1 (since that gives the smallest possible value in the array). Then, after sorting, the array will have 1 as the first element, and the rest as the sorted remaining elements.

- If all elements are 1: then we must replace one element with 2 (the smallest possible value allowed). Then the sorted array will have [1,1,...,2], so the first n-1 elements are 1, and the last is 2.

But wait, what if the original array has elements other than 1?

Wait, if the original array has a mix of 1's and other elements. For example, [1,3,1]. The maximum is 3. Replacing 3 with 1 gives [1,1,1], sorted. Then the output is [1,1,1]. But since the replacement has to be different. Wait, the original array is [1,3,1]. The 3 is replaced with 1, which is different (since original is 3). So that's allowed. The new array is [1,1,1], sorted. So the output is [1,1,1], which is correct.

So in this case, replacing the max element (3) with 1 is correct.

But what if the array is [2, 2, 2], then replacing one 2 with 1 gives [1,2,2], sorted, which is better than any other replacement.

So the general approach is:

If the array has at least one element that is not 1:

- Find the maximum element (or any occurrence of the maximum if there are multiple) and replace it with 1. Then sort. This will give the minimal possible array.

But wait, what if there are elements in the array that are larger than the max? No. The max is the maximum. So replacing the max with 1 gives the minimal possible array.

But why not replace a non-max element? For example, suppose the array is [5, 4, 3]. The max is 5. Replacing 5 with 1 gives [1,4,3], sorted as [1,3,4]. If instead, we replace 4 with 1, the array becomes [5,1,3], sorted as [1,3,5]. The first array is [1,3,4], which has smaller elements overall than [1,3,5]. So replacing the max is better.

So replacing the max is always better than replacing other elements (when the max is greater than 1).

But what if the array is [5, 5, 3]. The max is 5. Replacing one 5 with 1 gives [1,5,3], sorted as [1,3,5]. The output array would be 1,3,5. But if instead, we replace the other 5 with 1, it's the same. So in this case, the result is correct.

Another case: array [5, 5, 5]. Replacing one 5 with 1 gives [1,5,5], sorted as [1,5,5], which is the minimal possible.

So the approach seems to work.

But how to handle the case where all elements are 1? Then, the replacement must be to a different value (since we can't replace a 1 with 1). So we have to replace one 1 with 2. Then the sorted array is [1,1,...,2], so the first n-1 elements are 1, and the last is 2.

So the steps are:

1. Check if all elements are 1. If yes:

   a. The minimal possible array after replacement is [1, 1, ..., 2], sorted. So the output for each position i is 1 if i < n-1, and 2 for i = n-1.

2. Else:

   a. Find the maximum element in the array.

   b. Replace one occurrence of the maximum with 1.

   c. Sort the modified array.

   d. The output is this sorted array.

But wait, what if the array has multiple maximum elements, but also other elements? For example, [5,5,3]. Replacing any 5 with 1 gives [5,3,1] sorted as [1,3,5]. Which is correct. So replacing any of the max elements is okay.

But the problem states that we must replace exactly one element. So in this case, replacing any of the max elements is sufficient.

So the approach is:

- If all elements are 1: replace one with 2, sort, output.

- Else: replace one occurrence of the maximum element with 1, sort, output.

But the sample input 2:

Original array is [2,3,4,5,6]. The max is 6. Replace with 1: array becomes [2,3,4,5,1]. Sorted is [1,2,3,4,5], which matches the sample output.

Another sample: the third input is [2,2,2]. The max is 2. Since max is not 1, replace one with 1. Sorted array is [1,2,2], which matches the sample output.

So this approach works for the samples.

But what about the case where replacing a non-max element with 1 gives a better result?

Wait, let's take an array [3, 2, 4]. Max is 4. Replace with 1: array becomes [3,2,1], sorted as [1,2,3]. Output is [1,2,3]. If instead, replacing 3 with 1 gives [1,2,4], sorted as [1,2,4]. The output would be [1,2,4], which is worse than the first case. So replacing the max is better.

Another example: array [4, 3, 5]. Max is 5. Replace with 1 gives [4,3,1], sorted as [1,3,4]. Output is [1,3,4]. If we replace 4 with 1, sorted array is [1,3,5], which is worse. So replacing the max is better.

So the approach of replacing the max with 1 (when possible) seems to always yield the minimal possible array.

So the steps for the solution are:

1. Check if all elements are 1.

   a. If yes: create a new array where one element is replaced with 2, then sort.

   b. The minimal array is [1, 1, ..., 2], so output is 1 for first n-1 positions and 2 for last.

2. Else:

   a. Find the maximum value in the array.

   b. Replace the first occurrence (or any occurrence) of the maximum value with 1.

   c. Sort the array and output it.

But wait, when there are multiple max elements, replacing any of them with 1 will have the same effect, since after sorting, the array would have 1 and the remaining elements sorted.

For example, array [5,5,5,3]. Replacing any 5 with 1 gives [5,5,3,1], sorted as [1,3,5,5]. The output is [1,3,5,5]. So all positions are as minimal as possible.

But what if the array is [5,5,5,5]. Replacing any 5 with 1 gives [5,5,5,1], sorted as [1,5,5,5]. So the output is [1,5,5,5]. Which is better than any other possible replacement (e.g., replacing a 5 with 2 would give [2,5,5,5], sorted as [2,5,5,5], which is worse for the first position.

So replacing the max with 1 is better.

So the approach is correct.

Now, let's think about the code.

First, read n and the array.

Check if all elements are 1. How to do that efficiently? Sum or loop.

But for n up to 1e5, looping is O(n), which is acceptable.

Then, for the case where all elements are 1:

We need to replace exactly one element with a different value, which has to be at least 1 (but not 1). So the minimal possible is 2.

So the new array would be n-1 1s and one 2. When sorted, the 2 is at the end. So the output is [1,1,...,1,2].

For other cases:

Find the maximum element, replace the first occurrence (or any occurrence) with 1, then sort.

Wait, but in the original array, after replacing the max with 1, when we sort, the 1 will be first, and the rest are the sorted remaining elements.

So the code steps:

Read array.

Check if all elements are 1.

If yes:

   create a new array which is all 1s except one element is 2.

   sort it.

   output.

Else:

   find the maximum.

   create a copy of the array, replace the first occurrence of max with 1.

   sort.

   output.

But for n=1e5, this requires O(n) time (for the copy and the replacement and the sort). But sorting is O(n log n), which is acceptable for 1e5 elements (since 1e5 log 1e5 is about 5e6 operations, which is manageable in Python for 2 seconds).

But what about the case where the array already has a 1? For example, original array is [1,5,3]. The maximum is 5. Replace with 1. The array becomes [1,1,3], sorted as [1,1,3]. Which is correct. So replacing the max even if there are existing 1s is correct.

Another example: array [1,2,3,4,5]. The max is 5. Replace with 1. Sorted array is [1,1,2,3,4], which matches the sample output.

So the code seems correct.

But wait, in the first step of checking if all elements are 1:

How to check if all elements are 1. We can loop through the array, and if any element is not 1, break and proceed to the else case.

In Python:

all_ones = True

for num in a:

    if num != 1:

        all_ones = False

        break

If all_ones is True, then replace one element with 2 and sort.

Else, proceed to replace max with 1.

But when all_ones is True, the code creates a list of n-1 1s and one 2, sorted, which would have the 2 at the end.

But in Python, how to create this efficiently?

For example, if the original array is [1,1,1], then after replacement, the array becomes [1,1,2], sorted as [1,1,2].

So code:

if all_ones:

    new_arr = [1]*(n-1) + [2]

else:

    # find max, replace first occurrence with 1, sort.

But in Python, lists are mutable, so:

Else case:

max_val = max(a)

index = a.index(max_val)

new_arr = a.copy()

new_arr[index] = 1

new_arr.sort()

But for large arrays (n=1e5), a.copy() would take O(n) time, which is acceptable. Then sorting is O(n log n), which is acceptable.

So the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if all(num == 1 for num in a):

        # replace one with 2

        res = [1]*(n-1) + [2]

    else:

        max_val = max(a)

        # find first occurrence of max_val

        idx = a.index(max_val)

        a = a.copy()

        a[idx] = 1

        a.sort()

        res = a

    print(' '.join(map(str, res)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
2 3 4 5 6
""",
            "output": \
"""\
1 2 3 4 5
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if all(num == 1 for num in a):

        # replace one with 2

        res = [1]*(n-1) + [2]

    else:

        max_val = max(a)

        # find first occurrence of max_val

        idx = a.index(max_val)

        a = a.copy()

        a[idx] = 1

        a.sort()

        res = a

    print(' '.join(map(str, res)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
2 2 2
""",
            "output": \
"""\
1 2 2
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

Sample3:

3

2 2 2

all_ones? No. Max is 2. Replace first occurrence with 1. New array [1,2,2]. sorted as [1,2,2]. Output matches.

Another test case: all elements are 1.

Input:

3

1 1 1

all_ones is True. So res is [1,1,2]. Sorted is [1,1,2]. Output is 1 1 2.

Another test case where the array has elements 1 and others.

Input:

4

1 3 1 5

max is 5. Replace with 1. Array becomes [1,3,1,1]. Sorted [1,1,1,3]. Output is 1 1 1 3.

So this code should work.

But wait, in the else case, when the array is modified, we are modifying a copy. Because in Python, a = a.copy() then modifying a. So yes.

Yes, the code looks correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

all_ones = True
for num in a:
    if num != 1:
        all_ones = False
        break

if all_ones:
    res = [1] * (n - 1) + [2]
else:
    max_val = max(a)
    idx = a.index(max_val)
    a = a.copy()
    a[idx] = 1
    a.sort()
    res = a

print(' '.join(map(str, res)))
```
