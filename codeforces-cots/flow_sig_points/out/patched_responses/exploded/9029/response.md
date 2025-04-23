<think>
Okay, let's try to understand the problem here. So Sonya has these two robots, one starting on the left and one on the right. Each robot is given a number, and they move towards each other. The first robot (left) stops when it finds its number, and the second robot (right) stops when it finds its number. The condition is that their stopping positions must be such that the left robot's position is strictly less than the right's. Also, the numbers given must exist in the array, otherwise the robots would never stop and meet, which Sonya wants to avoid.

Our goal is to count the number of valid (p, q) pairs where p is the number given to the left robot and q is given to the right robot, such that when they stop, their positions don't cross each other.

Hmm. Let's think about how to model this. For a pair (p, q) to be valid, the left robot's stopping position (the first occurrence of p when moving from left to right) must be before the right robot's stopping position (the first occurrence of q when moving from right to left). Wait, no. Wait, the left robot is moving right, so it stops at the first occurrence of p. The right robot is moving left, so it stops at the first occurrence of q in that direction. So for example, the right robot's first occurrence when moving left is the same as the last occurrence in the array. Wait, no. Wait, when moving left, the right robot starts at the end, and moves left until it finds q. So the first occurrence it finds when moving left is the rightmost occurrence of q. Wait, no. Let me think: suppose the array is [1,5,4,1,3]. The right robot starts to the right of the array (position 5's right, index 5 maybe). When it moves left, it checks the elements from the end. So for example, if the number is 1, the right robot would stop at index 3 (the fourth element, since the array is 0-based or 1-based? The problem statement's example says in the first input that the first robot stops at position 1, which is the first element. So probably the array is 1-based. So in the first example, the array is [1,5,4,1,3]. The left robot (given 1) stops at position 1. The right robot (given 4) would move left from position 5 (after the 3) to position 3 (the 4 in the array). So the left robot is at 1, the right at 3. So yes, valid. 

So the positions where the robots stop are determined as follows: for the left robot, the first occurrence of p in the array (left to right). For the right robot, the first occurrence of q when moving from the end (right to left). So the right robot's stopping position is the last occurrence of q in the array. Wait, no. Wait, when moving right to left, the first occurrence encountered is the rightmost occurrence. So the right robot stops at the rightmost occurrence of q. So for the right robot, the stopping position is the last occurrence of q in the array.

So for a pair (p, q) to be valid, two conditions must hold:

1. The first occurrence of p (left to right) must be before the last occurrence of q (right to left). Because if the left robot's position is <= the right's, then they are okay. Wait, the problem says that the robots stop at different positions such that the first is to the left of the second. So left_pos < right_pos.

So for the pair (p, q), the first occurrence of p (call it L_p) must be < the last occurrence of q (call it R_q). 

But also, p must exist in the array (so L_p exists) and q must exist (so R_q exists). Because if either doesn't exist, the robot would never stop, which Sonya avoids.

So the problem reduces to counting all pairs (p, q) where p is present in the array, q is present in the array, and first occurrence of p < last occurrence of q.

Wait, yes. Because if first occurrence of p is before last occurrence of q, then the left robot stops at L_p, the right at R_q. Since L_p < R_q, the robots don't meet.

So the approach is to compute the first occurrence of each possible value (p) in the array, and the last occurrence of each possible value (q) in the array. Then, for all pairs (p, q) where p's first occurrence is less than q's last occurrence, count them.

But how to compute this efficiently?

First, collect all the unique elements in the array, since p and q must be among them.

Then, for each unique p, find first_occurrence[p], which is the index of the first occurrence of p. Similarly, for each unique q, last_occurrence[q] is the index of the last occurrence of q.

Then, the total number of valid pairs is the sum over all p in unique_elements of the number of q in unique_elements where first_occurrence[p] < last_occurrence[q].

But how to compute this sum efficiently, considering that n can be up to 1e5, and unique elements could be up to 1e5 as well.

If we do this naively, for each p, loop through all q and check if first_occurrence[p] < last_occurrence[q], that's O(k^2) where k is the number of unique elements, which could be up to 1e5, leading to 1e10 operations. Which is way too slow.

So we need a smarter approach.

Alternative approach: For each q, collect all p where first_occurrence[p] < last_occurrence[q]. Then sum the count for each q.

But again, how to do this efficiently.

Let's think of the first_occurrence and last_occurrence as values.

Suppose we have all the first occurrences stored in a list, and sorted. Then for each q's last_occurrence, we can find the number of p's first_occurrence that are less than this last_occurrence. Summing this over all q would give the total.

But how to handle duplicates. For example, if two different q's have the same last_occurrence, how many times do we count the same p's.

Wait, each q is considered individually. So for each q in unique elements, find the number of p's in unique elements where first_occurrence[p] < last_occurrence[q].

So the total is sum over q (count of p where first_occurrence[p] < last_occurrence[q]).

So, if we can collect all the first_occurrence values, sort them, then for each q's last_occurrence, compute how many first_occurrence values are less than last_occurrence[q]. Then sum all these counts.

That's a feasible approach. Because:

- Collecting all first_occurrence values and sorting them is O(k log k), which is acceptable for k up to 1e5.

- Then, for each q's last_occurrence, perform a binary search to find how many first_occurrence are less than it, which is O(log k) per q. So overall O(k log k), which is manageable.

So the steps would be:

1. Preprocess the array to find first_occurrence and last_occurrence for each unique element.

   For first_occurrence: iterate through the array from left to right, and for each element, if it's the first time we see it, record the index.

   For last_occurrence: iterate through the array from right to left, and for each element, if it's the first time we see it in this direction, record the index.

2. Collect all the first_occurrence values into a list and sort it.

3. For each unique element q, get its last_occurrence value. Then, perform a binary search on the sorted first_occurrence list to find how many elements are less than last_occurrence[q]. The count for this q is the number of such elements. Sum all these counts across all q.

This should give the total number of valid (p, q) pairs.

But wait, each p and q must be unique elements. Because when we collect all unique elements, the first_occurrence and last_occurrence are stored for each unique element. So each p is a unique element, and same for q.

Yes, because even if an element appears multiple times, its first and last occurrence are determined, but in the unique elements, each element is considered once. For example, if the array has 1,5,4,1,3, the unique elements are 1,5,4,3. So first_occurrence for 1 is 0 (assuming 0-based index), and last_occurrence for 1 is 3 (the fourth element). 

Wait, in the first example, the array is 1,5,4,1,3. The first occurrence of 1 is index 0. The last occurrence of 1 is index 3. The first occurrence of 5 is index 1. The last occurrence of 5 is index 1, since it's only once. So for q=5, last_occurrence is 1. So when q is 5, any p with first_occurrence[p] < 1. So p can be 1 (0 < 1) and 5 (1 is not less than 1). So for q=5, the count is 1. Which in the first example's valid pairs includes (1,5), (5,5) is not allowed. Wait but according to the problem's sample output, the pair (5,4) is valid. Let me see the sample input.

In the first sample input:

The array is [1,5,4,1,3]

Valid pairs according to the note are (1,1), (1,3), (1,4), (1,5), (4,1), (4,3), (5,1), (5,3), (5,4). So total 9 pairs.

Looking at q's:

For each q, we look at last_occurrence[q]:

q=1: last occurrence is index 3 (element is 1 at position 4 (1-based?), but in 0-based, the array is 0-based in code. Let's clarify.

In the first example, the array is 1,5,4,1,3. The first occurrence of 1 is 0 (0-based), the last occurrence is 3 (the fourth element in the array, which is 1). For q=4, last occurrence is 2 (the third element). For q=3, last occurrence is 4. For q=5, last occurrence is 1.

So for each q in the unique elements (1,5,4,3):

q=1: last_occurrence is 3. The number of p's with first_occurrence[p] <3. Let's see the first_occurrence for each unique p:

p can be 1 (0),5 (1),4 (2),3 (4). So p's first_occurrence:

p=1: 0

p=5:1

p=4:2

p=3:4.

So for q=1 (last_occurrence 3), how many p's first_occurrence is less than 3? p=1 (0), p=5 (1), p=4 (2) → 3 p's. So the count for q=1 is 3. But in the sample, the pairs where q is 1 are (p,1) where p's first_occurrence <3. So (1,1), (5,1), (4,1). Wait but according to the sample's valid pairs, (5,1) is present. But in the first sample's explanation, (4,1) is present but (5,1) is not. Wait, maybe I'm misunderstanding.

Wait the sample's note says that in the first example, the valid pairs include (5,1), (5,3), (5,4). Let me check the pairs where q is 1. For q=1, the last_occurrence is 3. So any p where first_occurrence[p] <3. So p can be 1,5,4, which gives (1,1), (5,1), (4,1). But in the sample explanation, (5,1) is a valid pair, but in the note, (5,1) is present, but (4,1) is also present. So according to the sample, (4,1) is allowed because the first_occurrence of 4 is 2, which is less than 3. So those three pairs are counted. But in the sample's output, the count is 9, which would sum up all q's.

Wait, perhaps my approach is correct. Let's see.

For each q, the count is the number of p's where first_occurrence[p] < last_occurrence[q].

So for the first example, the unique elements are 1,5,4,3,3 is the last element. Let's process each q:

q=1: last_occurrence is 3. Number of p's with first_occurrence[p] <3 is 3 (p=1,5,4). So contributes 3 pairs.

q=5: last_occurrence is 1. Number of p's <1: only p=1 (0 <1). So contributes 1 pair.

q=4: last_occurrence is 2. p's with first_occurrence <2: p=1 (0) and p=5 (1). So contributes 2 pairs.

q=3: last_occurrence is4. p's with first_occurrence <4: all p's except 3 (4 is 4's first_occurrence is 2, and 3's is 4). So p=1 (0),5 (1),4 (2). So 3 pairs.

So total is 3 +1 +2 +3 =9. Which matches the sample output. So the approach is correct.

Thus, the algorithm is correct.

Now, the implementation steps:

1. Read n and the array.

2. For each element in the array, compute first_occurrence and last_occurrence for each unique value.

   For first_occurrence:

   Initialize a dictionary. Iterate through the array from left to right. For each element a[i], if not in the dictionary, add it with value i.

   For last_occurrence:

   Initialize a dictionary. Iterate through the array from right to left. For each element a[i], if not in the dictionary, add it with value i.

3. Collect all the first_occurrence values into a list, sort it.

4. For each unique q in last_occurrence, get its last_occurrence value. Use binary search to find the number of elements in the sorted first_occurrence list that are less than the q's last_occurrence. Sum all these counts.

But wait: first_occurrence and last_occurrence are for the same set of unique elements. So for example, if a value is present in first_occurrence but not in last_occurrence (which is impossible since we process all elements in the array), but in reality, both will have all the unique elements. Because for any element that appears in the array, it must have a first and last occurrence.

So after building first_occurrence and last_occurrence, we can get the unique elements as the keys of either. But to be safe, perhaps use the keys from first_occurrence, since every element must have a first occurrence.

But since the problem statement says that Sonya must choose p and q that exist in the array, the pairs (p, q) must be such that p is present (in first_occurrence) and q is present (in last_occurrence). But since the array is the same, the keys of first_occurrence and last_occurrence are the same, the unique elements.

So, the code steps:

Read the array.

Compute first_occurrence: iterate left to right.

Compute last_occurrence: iterate right to left.

Then, collect all the first_occurrence values into a list and sort it.

Then, for each q in last_occurrence, get last_occurrence[q], and find the count of first_occurrence values < last_occurrence[q].

Sum all these counts.

Yes.

Now, the code.

But let's think about possible edge cases.

Case where all elements are the same. For example, n=3, array [2,2,2]. Then first_occurrence for 2 is 0, last_occurrence is 2. The valid pairs are (2,2) if 0 <2. So yes. So count is 1.

Another case: n=1. Then first_occurrence and last_occurrence are the same. So p and q must be the same element, but first_occurrence[p] is 0, last_occurrence[q] is 0. So 0 <0 is false. So no valid pairs. So output 0.

Wait, but if n=1, the two robots are placed at either end. The left robot is to the left of the first element, the right robot to the right of the first element. The array has one element. So the left robot's stopping position is the first occurrence of p (the element), which is index 0, but the right robot's stopping position is the last occurrence of q, which is also index 0. So 0 <0 is false, hence (p, q) is invalid. So the count is 0.

Another example: the second sample input.

Sample Input 2:

7

1 2 1 1 1 3 2

The array is 1-based indexes here (assuming code uses 0-based). The first_occurrence:

1:0

2:1

3:5.

Wait, in the array [1,2,1,1,1,3,2], 0-based indices:

elements are 0:1, 1:2, 2:1, 3:1,4:1,5:3,6:2.

So first_occurrence for 1 is 0, 2 is 1, 3 is 5.

Last_occurrence:

We iterate from right to left (indices 6 to 0). For each element:

element 6 is 2: add to last_occurrence with index 6.

element 5 is 3: add to last_occurrence with index5.

element4:1, not in last_occurrence: add index4? Wait no. When iterating from the end, the first occurrence of a value in this direction is the last occurrence in the original array.

Wait, no. Let's see:

We process the array from the end. For each element, if it's not in last_occurrence, add its index. So for the array [1,2,1,1,1,3,2], processing indices 6,5,4,3,2,1,0.

At index6: element 2. Not in last_occurrence, add 6.

index5:3. Add 5.

index4:1. Not present, add 4.

index3:1. Already present.

index2:1. Already present.

index1:2. Already present.

index0:1. Already present.

So last_occurrence for 2 is6, 3 is5, 1 is4.

Wait, but in the array, the last occurrence of 1 is index4? No. The array is [1,2,1,1,1,3,2]. The last occurrence of 1 is index4 (the fifth element in 1-based, 0-based index4). Wait no: the elements after index4 are index5 (3) and 6 (2). So the last occurrence of 1 is at index4.

Hmm, but in the sample input 2's note, the valid pairs include (1,1), which would have first_occurrence of 1 (0) < last_occurrence of 1 (4). So yes. So the count for q=1 is the number of p's where first_occurrence[p] <4. The first_occurrence values are 1:0, 2:1,3:5, and 2's first occurrence is 1. So for q=1, the last_occurrence is4. So p's first_occurrence less than4 are 0,1,5 (but wait, wait 3's first_occurrence is5, which is 5 <4? No. Wait, 5 is not less than4. So the p's are 1 (0),2 (1). 3's first_occurrence is5, which is greater than4. So count is 2. But according to the sample explanation, (1,1) is allowed, (2,1) is allowed. So the count for q=1 is 2, but according to the sample output, the total is7. Let's see.

But according to the approach:

The first_occurrence list is [0,1,5]. Because the unique elements are 1,2,3. So their first_occurrence is 0,1,5. So sorted first_occurrence list is [0,1,5].

For each q in last_occurrence (which is 1,2,3, but wait the array's unique elements are 1,2,3, but last_occurrence for 2 is6, 3 is5, 1 is4.

Wait, the array has elements 1,2,1,1,1,3,2. The unique elements are 1,2,3.

So for each q in 1,2,3:

q=1: last_occurrence is4. Number of first_occurrence[p] <4. first_occurrence list is [0,1,5]. So all elements less than4 are 0,1,5? No. 5 is5>4, so no. So elements <4 are 0 and1. So count is 2.

q=2: last_occurrence is6. first_occurrence list sorted is [0,1,5]. All are <6. So count is3.

q=3: last_occurrence is5. first_occurrence list elements <5 are 0,1. Because5 is equal to5, not less. So count is2.

Summing 2 (q=1) +3 (q=2) +2 (q=3) =7, which matches the sample. So the approach works.

Thus, the code seems correct.

Now, code implementation.

In Python, for handling first_occurrence and last_occurrence:

We can use two dictionaries. Then, collect all the first_occurrence values, sort them. Then for each q in last_occurrence's keys, find the count via bisect.

But to get the unique elements, we can use the keys of first_occurrence or last_occurrence. But since every element in the array is present in both, since first_occurrence is built from left to right, and last_occurrence from right to left. So the keys of first_occurrence and last_occurrence are the same. So we can take the keys from any of them.

Now, code steps:

Read n.

Read the array as list of integers.

Compute first_occurrence:

Initialize a dictionary, first = {}

for i in range(n):

   if a[i] not in first:

       first[a[i]] = i

Compute last_occurrence:

Initialize a dictionary, last = {}

for i in range(n-1, -1, -1):

   if a[i] not in last:

       last[a[i]] = i

Collect all first_occurrence values into a list, sort it.

sorted_first = sorted(first.values())

Then, for each q in last:

   r = last[q]

   count += number of elements in sorted_first that are < r

The total count is the sum.

Implementing this with bisect.

In Python, the bisect module's bisect_left function returns the insertion point which is the number of elements less than the target.

Thus, for each q in last:

   r = last[q]

   cnt = bisect.bisect_left(sorted_first, r)

   total += cnt

Yes.

So the code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    first = {}
    for i in range(n):
        if a[i] not in first:
            first[a[i]] = i

    last = {}
    for i in range(n-1, -1, -1):
        if a[i] not in last:
            last[a[i]] = i

    sorted_first = sorted(first.values())

    total = 0
    for q in last:
        r = last[q]
        cnt = bisect.bisect_left(sorted_first, r)
        total += cnt

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
1 2 1 1 1 3 2
""",
            "output": \
"""\
7
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

Sample 2:

As discussed, the code should output7.

Another test case with n=1: input is [5]. Then first_occurrence[5] =0, last_occurrence[5] =0. The sorted_first is [0]. For q=5, r=0. bisect_left([0],0) returns0. So total is0. Correct.

Another test case where all elements are same: n=3, elements [2,2,2]. first_occurrence[2] =0. last_occurrence[2]=2. sorted_first is [0]. For q=2, r=2 → bisect_left returns0 (elements less than2 is 0). So total is0. Wait, no. Wait first_occurrence[p] for p=2 is0. last_occurrence[q=2] is2. So the pair (2,2) is valid only if0 <2, which is true. So the code would count for q=2, the count is1 (bisect_left returns the index where 0 is inserted in a list [0], but target is2. So bisect_left would return1. Because 2 is larger than all elements. So the count is1. So the code would output1. But according to the problem statement, the pair (2,2) is allowed? Let's see.

In this case, the left robot would stop at first occurrence (0), the right robot stops at last occurrence (2). 0<2, so the pair is valid. So the code's count is1. But according to the code's logic:

sorted_first is [0]. For q=2, r=2. bisect_left([0],2) → returns1 (since 0 <2, 2 is inserted at index1). So the count is1. So code returns1. So the code is correct.

So the code seems correct.

Now, the code needs to be written in Python, using bisect.

Make sure that the code reads the input correctly and that all the elements are considered. Also, the code should be optimized for speed and memory.

In Python, the code should be efficient enough for n=1e5. The steps:

- first_occurrence and last_occurrence are built in O(n) time.

- Sorting the first_occurrence values is O(k log k), where k is the number of unique elements (up to 1e5).

- Then, for each q in the last_occurrence (up to 1e5 elements), a binary search is done in O(log k) time.

Total time is O(n + k log k + k log k) = O(n + k log k). For n=1e5 and k=1e5, this is manageable.

Memory-wise, storing the first_occurrence and last_occurrence dictionaries is O(k) each. The sorted_first list is O(k). So memory is acceptable.

So the code is correct and optimized.
</think>

```python
import bisect

n = int(input())
a = list(map(int, input().split()))

first_occurrence = {}
for idx, num in enumerate(a):
    if num not in first_occurrence:
        first_occurrence[num] = idx

last_occurrence = {}
for idx in reversed(range(n)):
    num = a[idx]
    if num not in last_occurrence:
        last_occurrence[num] = idx

sorted_first = sorted(first_occurrence.values())
total = 0

for q in last_occurrence.values():
    cnt = bisect.bisect_left(sorted_first, q)
    total += cnt

print(total)
```
