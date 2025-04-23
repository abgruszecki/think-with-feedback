<think>
Okay, let's try to figure out this problem. The task is to permute the array such that as many elements as possible are larger than the original elements at their positions. So for each position in the new array, we want the element there to be bigger than the original element in that position.

Hmm. So the first thought is: how can we arrange the elements to maximize the count. Let's think about sorting. Because when you sort, you can have a systematic way of pairing elements.

Wait, the original array is given. So for each position i, the original a[i] is fixed. We need to permute the elements such that the new array's element at position i is greater than the original a[i], and we want as many such positions as possible.

Wait, but the original array isn't sorted. Oh right, the original array is given as is. So for each i in the original array, the original a[i] is fixed. We need to assign a permutation of the array's elements to each position, such that the number of positions where the new element is larger than the original a[i] is maximized.

So the problem is to rearrange the elements such that the maximum number of new elements are greater than their original counterparts.

So the approach should be to find a way to pair each new element with an original position such that the new element is larger than the original a[i], and this count is maximized.

So how can we model this?

Let's think of this as a matching problem. For each element in the new array (which is a permutation), we want to assign it to a position where it is larger than the original a[i]. But since the permutation is a rearrangement of all elements, each element is used exactly once.

So the problem reduces to: assign each element in the array to a position such that the element is larger than the original a[i] of that position, and maximize the number of such assignments.

So the maximum possible is the number of elements that can be placed in positions where they are larger than the original value.

The key is to find a way to pair elements (from the array) with positions (original indices) such that the element is larger than the original value of the position. And we need as many pairs as possible.

To maximize this, we can sort the array and the original array in a certain way. Let's see.

Let's sort the original array in increasing order, and the new array (sorted) in increasing order as well. Then, use a two-pointer approach to find how many elements in the new array can be matched with original elements such that the new element is larger.

Wait, but the original array's elements are for each position. So the original array's positions are fixed. So when we permute, the original a[i] for position i is fixed, and the new element at i is some element from the array. So for each i, the new element must be > original a[i].

So the problem is similar to, for each original a[i], how many elements in the array are larger than a[i]. But since all elements are used exactly once, we can't just count for each a[i] the number of elements larger than it. Because once an element is assigned to a position, it's no longer available for others.

So this is a problem of maximum matching between elements and positions where the element is larger than the original a[i] of the position.

The optimal way is to find a way to assign the largest possible elements to the positions where their original a[i] is smallest, so that each large element can cover a small a[i], thus allowing more elements to be used for other positions.

Wait, perhaps we can sort the original array's elements and the permutation array's elements, then use a two-pointer approach.

Wait, let's think: suppose we sort the original array (original a's) in ascending order. Let's call this S. Then, sort the permutation array (which is the same elements as the original array) in ascending order as well. Let's call this T.

Now, we can try to find the maximum number of elements in T that can be matched to elements in S such that T[j] > S[i], and each T[j] is used exactly once, and each S[i] is matched to at most one T[j].

The way to do this is similar to the classic two-sum approach. For example, for the sorted S and T:

We can iterate through T in ascending order and try to assign the smallest possible T[j] to the smallest S[i] that it can be larger than, but perhaps a better approach is to assign the largest possible T[j] to the largest S[i] possible where T[j] > S[i].

Wait, the approach to maximize the count would be to match the largest possible T[j] with the largest possible S[i] that it can beat. Let's think of this:

Sort S in ascending order. Sort T in ascending order.

Then, for each element in T (starting from the end), we check if it's larger than S[i], starting from the end of S. Each time we find a T[j] > S[i], we count it and move to the next S[i] and the next T[j].

Wait, but the positions are fixed. Wait, no. Because in the original array, each S is the original a[i], but the permutation can assign any element to any position. So the problem is not to assign elements to the original array's positions in the same order, but to assign each element to a position (could be any) such that the element is larger than the original a[i] of that position.

Wait, that's the key. So the permutation can arrange the elements in any order, but the original array's elements are fixed for each position. So the original a[i] is the value at position i in the original array, and the permutation's element at position i can be any element from the array (once).

But the count is the number of positions where the permutation's element is larger than the original a[i] at that position.

So the problem is to find a bijection (permutation) of the array elements such that for as many positions i as possible, permutation[i] > original[i].

Hmm. So the way to maximize this is to assign each element in the permutation array to a position i where it is larger than original[i], and as many as possible.

So the original array's elements are fixed for each position. The permutation array must be a rearrangement of the original elements, and we need to maximize the count of i where permutation[i] > original[i].

So the problem reduces to: assign each element from the array to a position (original a[i]) such that the element is larger than the original a[i] of the position, and maximize the number of such assignments.

So this is a bipartite matching problem, but with n up to 1e5, we need a more efficient approach.

An efficient approach would be to sort the original array's elements and the array's elements (after being sorted) in a way that allows maximum matching.

Let me think of the following approach:

Sort the original array in ascending order. Let's call this sorted_original.

Sort the array (elements to be permuted) in ascending order. Let's call this sorted_elements.

Now, the goal is to assign each element in sorted_elements to a position in sorted_original such that the element is larger than the original, and each element is used exactly once.

But since sorted_original is sorted, the idea is to use the smallest elements possible to cover the smallest sorted_original elements.

Wait, perhaps a two-pointer approach. Let's have two pointers, i for sorted_original (starting at 0) and j for sorted_elements (starting at 0). For each element in sorted_elements, check if it is larger than sorted_original[i]. If yes, we can count this as a match and move both pointers forward. If not, move j forward. The total count would be the maximum possible matches.

Wait, but this approach is for the case where we can pair elements from the two sorted arrays in a way that each element in sorted_elements can be matched to a sorted_original element, and the count is maximized.

Yes. Because sorted_original is sorted in ascending order, sorted_elements is also in ascending order. So to find the maximum number of elements in sorted_elements that can be matched to sorted_original elements such that sorted_elements[j] > sorted_original[i], we can use the two-pointer approach.

For example:

sorted_original: [1, 1, 1, 3, 5, 5, 10] (original array sorted)
sorted_elements: [1, 1, 3, 5, 5, 10, 20] (hypothetically sorted elements)

Wait, in the first example's input:

Original array is [10, 1, 1, 1, 5, 5, 3]. So sorted_original would be [1, 1, 1, 3, 5, 5, 10].

The sorted_elements is the same as the original array, sorted: [1, 1, 1, 3, 5, 5, 10].

Wait, but in the first sample, the answer is 4. Let's see. When we apply the two-pointer approach:

i starts at 0 (sorted_original[i] = 1), j starts at 0 (sorted_elements[j] = 1). Since 1 is not > 1, we move j to 1. Still 1 <=1, move j to 2. Now j=2, element is 1. Still not > 1. j=3, element 3. 3>1: count increases by 1, i=1, j=4. Now sorted_original[i] is 1. sorted_elements[j] is 5: yes. count is 2, i=2, j=5. j=5, element 5>1. count 3, i=3 (3), j=6 (element 10). 10>3: count 4. i=4 (5). j=6 is 10>5: yes, count 5. i=5 (5). j=6: 10>5: count 6. i=6 (10). j=6: 10>10? No. So total 4+2? Wait, wait this approach would give 5+1=6? But the first sample's answer is 4. So this approach must be wrong.

Wait, that's a problem. Because the sample's answer is 4, but according to this two-pointer approach, the count would be higher.

Wait, perhaps there's a misunderstanding here. Because the original array's elements are fixed per position. So when you sort the original array, the positions are lost. So matching based on sorted_original's elements isn't directly applicable. Because the permutation can assign elements to any position, but each position's original a[i] is fixed. So the permutation has to assign elements to the original positions such that the element is larger than the original a[i] of that position.

So the sorted_original approach and the two-pointer approach may not capture this because the positions are not considered in their original order.

Wait, but when you permute the array, you can arrange the elements in any order. So the original array's a[i] is fixed for each position. For example, if the original array is [10, 1, 1, 1, 5,5,3], then each position has a certain a[i]. The permutation can assign elements to these positions. So the problem is to assign each element of the array (the same elements) to the positions such that as many as possible of them are larger than the original a[i] of that position.

So the key is to find a way to assign elements to positions such that for as many positions as possible, the element is larger than the original a[i] of that position.

So the approach is: for each element in the permutation array, assign it to a position where the original a[i] is as small as possible but smaller than the element, to allow larger elements to be used for larger original a[i]s.

But how to model this?

Let's think of the following approach: sort the original array's elements (original a's) in ascending order. Then, sort the elements of the array (the permutation elements) in ascending order. Then, for each element in the sorted permutation array, we try to match it with the smallest possible original a[i] that is less than the element and hasn't been matched yet.

This way, the smallest elements in the permutation array are used to cover the smallest original a[i]s, leaving the larger permutation elements to cover larger original a[i]s.

So the algorithm would be:

Sort the original array (original_a) in ascending order.

Sort the permutation array (sorted_perm) in ascending order.

Initialize two pointers: i (for sorted_perm) and j (for original_a), both starting at 0.

Initialize count to 0.

For each element in sorted_perm:

   if element > original_a[j], then count +=1, j +=1.

   else, do nothing (move to next element in sorted_perm).

Wait, but in this case, the elements are processed in sorted_perm's order. So the smallest elements in sorted_perm are matched with the smallest original_a[j] that they can beat. This way, larger elements in sorted_perm can be used to beat larger original_a elements.

Wait, but let's test this with the first sample.

Sample input:

7

10 1 1 1 5 5 3

Original array (original_a) is [10,1,1,1,5,5,3]. When sorted, original_a becomes [1,1,1,3,5,5,10].

sorted_perm is the sorted array of elements: [1,1,1,3,5,5,10].

Now, the two-pointer approach would be:

i starts at 0 (element 1), j starts at 0 (original_a[0] is 1). 1 is not >1. So move to next element (i=1, element 1). Still no. i=2, element 1. No. i=3, element 3. Compare with original_a[j=0] (1). 3>1: count becomes 1, j=1. Next element is 5 (i=4). original_a[j=1] is 1. 5>1: count 2, j=2. Next element 5 (i=5): 5>1, count 3, j=3. Next element 10 (i=6): compare with original_a[3]=3. 10>3: count 4, j=4. Now, original_a[j=4] is 5. But there are no more elements in sorted_perm. So total count is 4, which matches the sample's output.

Ah, so this approach works for the first sample. Let's see the second sample, where all elements are 1. Original_a sorted is [1,1,1,1,1], sorted_perm is the same. All elements in sorted_perm are 1. So the two-pointer approach would compare each 1 to original_a[j]. Since 1 is not greater than 1, no count is made. So the answer is 0, which matches the sample.

So this approach seems to work. So the steps are:

1. Sort the original array (original_a) in ascending order.

2. Sort the permutation array (sorted_perm) in ascending order.

3. For each element in sorted_perm, in order, check if it is larger than original_a[j], where j starts at 0. If yes, increment count and j. Otherwise, move to next element.

The reason this works is that by sorting both arrays, we can greedily match the smallest possible elements in sorted_perm to the smallest possible original_a elements that they can beat. This allows larger elements in sorted_perm to have a chance to beat larger original_a elements, thus maximizing the total count.

So the optimal algorithm is O(n log n) time, which is acceptable for n up to 1e5.

Now, the code can be written as follows:

Read n.

Read the array as a list.

Create a copy of the array, sort it as sorted_perm.

Sort the original array (original_a) as sorted_original.

Then, apply the two-pointer approach.

Wait, but wait: the original array is the array given in the input. So sorted_original is a sorted version of the original array's elements. Because in the problem, each position in the original array has a fixed a[i], but when we permute, we can assign any element to any position. However, for the two-pointer approach to work, we need to sort the original array's elements. Because in the code, we are trying to match each element in sorted_perm to the smallest possible original element in sorted_original.

But since in the permutation, the elements can be assigned to any positions, the way to maximize the count is to match elements to the original elements (sorted_original) in a way that the smallest possible elements in sorted_perm are matched to the smallest possible original elements that they can beat. This way, larger elements can be used to beat larger original elements.

Thus, the code should:

- Sort the original array (original_a) in ascending order.

- Sort the permutation array (sorted_perm) in ascending order.

- Use two pointers to count how many elements in sorted_perm can be matched to elements in sorted_original such that sorted_perm[i] > sorted_original[j], and each element is matched to one.

So the code would be:

n = int(input())

a = list(map(int, input().split()))

sorted_original = sorted(a)

sorted_perm = sorted(a)

i = 0  # pointer for sorted_original
j = 0  # pointer for sorted_perm
count = 0

for num in sorted_perm:
    if num > sorted_original[i]:
        count +=1
        i +=1

print(count)

Wait, but wait, in the code above, the loop is over sorted_perm, but for each num in sorted_perm, we check if it's > sorted_original[i]. If yes, increment count and i. Else, move to next. So this is a linear scan.

Testing this code against the first sample:

Original a: [10,1,1,1,5,5,3]

sorted_original becomes [1,1,1,3,5,5,10]

sorted_perm is the same as sorted_original.

Loop over each num in sorted_perm:

num=1: compare with sorted_original[0] =1. Not greater. So no count.

num=1: same as above.

num=1: same. No count.

num=3: compare with sorted_original[0]=1. 3>1. So count=1, i=1.

Next num=5: compare with sorted_original[1]=1. 5>1: count=2, i=2.

Next num=5: compare with sorted_original[2]=1: 5>1: count=3, i=3.

Next num=10: compare with sorted_original[3]=3: 10>3: count=4, i=4.

Next, num=10 (no, sorted_perm is [1,1,1,3,5,5,10]? Wait no. Wait, the original array is [10,1,1,1,5,5,3]. sorted_perm is sorted of this array, which is [1,1,1,3,5,5,10]. So the loop is:

num in sorted_perm: 1,1,1,3,5,5,10.

So after the first three 1s, the fourth element is 3. Then 5,5,10.

So in the loop:

First three 1s: none are > sorted_original[i=0] (1). So i remains 0.

Fourth element is 3: >1 → count 1, i=1.

Fifth element is 5: >1 → count 2, i=2.

Sixth element is 5: >1 → count3, i=3.

Seventh element is 10: compare with sorted_original[3] (3). Yes → count4, i=4.

Now, i=4. sorted_original[i] is 5.

But there are no more elements in sorted_perm. So total count is 4, which matches the sample.

Yes, this works.

Another test case: all 1's. The code counts 0, which is correct.

Another example: original array [10,20,30,40], sorted_original [10,20,30,40], sorted_perm [10,20,30,40]. The code would check each element:

10 is not >10. 20>10 → count1, i=1. 30>20 → count2, i=2. 40>30 → count3. i=3. So total 3. But in the example given, the sample output is 2. Wait, wait, the example given in the problem statement:

Original array is [10,20,30,40]. The permutation given is [20,40,10,30]. The count is 2 (positions 0 and 1: 20>10 and 40>20). But according to the code's approach, sorted_original is [10,20,30,40], sorted_perm is [10,20,30,40].

The code's loop would be:

sorted_perm elements:10,20,30,40.

For 10: compare to 10 → no.

20: compare to 10 → yes. count1, i=1.

30: compare to 20 → yes. count2, i=2.

40: compare to 30 → yes. count3, i=3.

So code would output 3, but the sample says the maximum possible is 2.

Wait, that's a problem. So what's wrong here?

Wait the original sample input is:

Original array is [10, 20, 30, 40]. The code's approach says the maximum possible is 3, but the sample says the maximum is 2.

But wait, the sample given in the problem's note says that for this original array, the permutation [20,40,10,30] gives 2. But according to the code's approach, the maximum possible is 3. So the code's approach must be wrong.

Wait, that's a contradiction. So there's a mistake in the approach.

Wait, perhaps the code's approach is not correct. Let's think again.

The original array is [10,20,30,40]. The code's approach says that the maximum is 3. But according to the code's algorithm, how?

The sorted_original is [10,20,30,40], sorted_perm is same as sorted_original.

Loop:

i=0, j=0 (sorted_perm elements are 10, 20, 30,40).

Check 10: 10>10? No. Next element.

20: compare to sorted_original[0]=10 → yes. count=1, i=1.

30: compare to sorted_original[1]=20 → yes. count=2, i=2.

40: compare to sorted_original[2]=30 → yes. count=3, i=3.

So code outputs 3, but the sample in the problem description says that the answer is 2. What's wrong here?

Ah, the problem's note example is different. Wait, wait. Let's check the problem statement again.

In the problem statement's first paragraph, the example given is:

Original array is [10,20,30,40]. The permutation given is [20,40,10,30], which gives count 2. But according to the code's approach, the maximum possible is 3. So either there's a mistake in the code's approach, or the problem's example is incorrect.

But according to the problem statement's example, the maximum possible is 2. However, according to the code's approach, it's possible to get 3.

Wait, let's see. How can we arrange the elements to get 3.

Original array is [10,20,30,40]. Permutation must be a rearrangement of these elements.

Suppose permutation is [20,30,40,10].

Then:

At position 0: 20>10 → yes.

Position1:30>20 → yes.

Position2:40>30 → yes.

Position3:10>40 → no.

Total 3. Which is possible. So the code's approach is correct and the problem's example is wrong?

Wait, but the problem's example says that the permutation [20,40,10,30] gives 2. But there exists a permutation that gives 3. So the maximum possible answer is 3. So the code's approach is correct, and the problem's example explanation is incorrect.

But the problem's first example in the note says that the answer for that permutation is 2, but there exists a better permutation. So the problem's note is just giving one possible permutation and not the optimal one.

Ah, right. The note says "for instance" and "one of the best permutations", but maybe there's a better one.

So the code's approach is correct, and the note's example is just one of the possible permutations, but not the optimal one.

So for the original array [10,20,30,40], the maximum possible is indeed 3, which is what the code's approach gives.

Therefore, the code's approach is correct.

So why in the problem's example for this case the answer is 2? Because the note's example is not the optimal permutation. So the problem's note is not the maximum possible, but just an example of a permutation that gives a certain count.

So the code's approach is correct.

Thus, the code should be as follows: sort the original array and the permutation array, then apply the two-pointer approach.

Thus, the code will correctly handle all test cases.

Now, considering the constraints. Since n can be up to 1e5, sorting two arrays (each O(n log n)) is acceptable. The two-pointer loop is O(n), which is acceptable.

Now, in Python, reading the input, sorting, and then processing as described.

So the code:

Read n.

Read a as list of integers.

sorted_original = sorted(a)

sorted_perm = sorted(a)

Initialize i=0, count=0.

For each num in sorted_perm:

   if num > sorted_original[i]:

       count +=1

       i +=1

       if i == n: break

print(count)

Yes.

Thus, the code should be as follows.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
sorted_original = sorted(a)
sorted_perm = sorted(a)
count = i = 0
for num in sorted_perm:
    if i < n and num > sorted_original[i]:
        count += 1
        i += 1
print(count)
```