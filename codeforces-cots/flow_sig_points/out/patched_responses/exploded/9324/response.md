<think>
Okay, let's see. The problem is to find all values x in the array that meet certain conditions. The conditions are that all occurrences of x form positions which, when sorted, form an arithmetic progression. And for each such x, we need to output x and the common difference, which is zero if there's only one occurrence.

First, I need to understand what exactly constitutes an arithmetic progression here. For the positions of x, when sorted, the consecutive differences must be the same. So, if the positions are [i1, i2, ..., ik], then i2 - i1 = i3 - i2 = ... = ik - ik-1. If there's only one position, the difference is zero, which is allowed.

So the steps I need to take are:

1. For each unique x in the array, collect all the indices where x occurs, sorted in increasing order. Since the array is processed in order, maybe storing the positions in a list in the order they appear will already be sorted. Because as we read the array from left to right, each occurrence of x is added to the list in the order of their positions (like 0, 1, 2, etc. indexes). Wait, no, the positions are the actual indices of the array. So for example, if the array is [1,2,1], the positions for 1 are [0, 2], which are already in order.

So first, I can create a dictionary where the key is the value x, and the value is a list of indices where x occurs, in the order they appear (which is sorted since we process the array from left to right). That makes sense.

2. For each x's list of positions, check if they form an arithmetic progression. How?

If the list has length 1: automatically valid, difference is 0.

If the list has length 2: also automatically valid, difference is (pos2 - pos1). Because any two elements form an arithmetic progression.

If the list has length >=3: then all consecutive differences must be the same. So the difference between the first two positions gives the common difference, and all subsequent differences must match that.

For example, for positions [1,3,5,7], the difference is 2 each time, so it's valid. But if it's [1,3,5,8], then the difference between 5 and 8 is 3, which is different from the previous difference of 2. So it's invalid.

So the algorithm for checking is:

For a list of positions for x:

- If length <= 2: valid. The common difference is (pos[-1] - pos[0]) if len is 2, else 0.

- Else: compute the common difference as (pos[1] - pos[0]). Then check that for every i >=2, pos[i] - pos[i-1] equals this difference. If any of them doesn't, then x is invalid.

If any x's positions pass this check, then x is part of the answer.

So the plan is:

- Read the input array.

- For each element, record the indices where each x occurs.

- For each x in the dictionary:

   - Check if the list of positions satisfies the arithmetic progression condition.

   - If yes, record x and the common difference (if len is 1, 0; else, the difference between the first two, but wait: no. The difference for len 2 is the difference between the two positions, which is the same as the common difference. For example, positions [a, b] have a common difference of (b - a). So for len >=2, the common difference is (positions[1] - positions[0]). But wait, what if the list is longer than 2? Then the common difference must be consistent across all consecutive elements.

But once we've checked that all consecutive differences are equal (for len >=3), then the common difference is the same as the first difference. So regardless of the length, for a valid x, the common difference is positions[1] - positions[0], except when len is 1, which is 0.

Wait, no. For len 2, the common difference is (positions[1] - positions[0]). For len >=3, after checking that all differences are equal, the common difference is the same as the first difference.

So for valid x's, the px is:

if len ==1 → 0

else → positions[1] - positions[0]

So, once we have a valid x, we compute px as follows.

So, the steps are:

For each x's position list:

   if len ==1:

       add to answer (x, 0)

   else:

       compute d = positions[1] - positions[0]

       if len >=3:

           check all subsequent differences are equal to d. If any is not, x is invalid.

       if valid:

           add (x, d) to the answer.

So that's the plan.

Now, the next part is to implement this efficiently.

Given that n can be up to 1e5, the algorithm must run in O(n) or O(n log n) time.

The steps:

1. Create a dictionary (hash map) to store the positions for each x. This is O(n) time and space.

2. For each x in the dictionary:

   a. Check the positions list as per the above logic.

   For each x, the check is O(k), where k is the number of occurrences of x.

   The total sum of k across all x is n. So this part is O(n) time.

So overall, the algorithm is O(n) time.

So this should be acceptable.

Now, for the data structures:

We can use a defaultdict(list) to store the positions. For each element in the input array, append its index (starting from 0) to the list for its value.

Then, for each x in the keys of the dictionary, sorted in increasing order (since the output must be ordered by x in increasing order), process the list.

Now, edge cases:

- All elements are the same. Like [5,5,5,5]. The positions are [0,1,2,3]. Check if the differences are the same. The differences are 1 each (1-0=1, 2-1=1, 3-2=1). So d is 1. So x=5 is valid, with px=1.

Another example: [1,3,5,7]. The differences are 2 each. So px=2.

Another example: [1,3,5,8]. Then 5-3=2, 8-5=3 → invalid. So x is not part of the answer.

So, the code steps:

Read n.

Read the array a (as list of integers).

Create a dictionary, say pos_dict, where each key is a value in a, and the value is a list of indices (0-based) where the key occurs.

Sort the keys of pos_dict in increasing order.

For each x in sorted keys:

   get the list of positions.

   if len == 1:

       add to answer (x, 0)

   else:

       d = list[1] - list[0]

       valid = True

       for i in range(2, len(list)):

           if (list[i] - list[i-1]) != d:

               valid = False

               break

       if valid:

           add (x, d) to answer.

Finally, output the count of valid x's, followed by each x and px in order.

Now, for the example:

In the second sample input:

8

1 2 1 3 1 2 1 5

pos_dict for 1 is [0, 2,4,6]

Check: len is 4 >=3.

d = 2-0=2.

Check positions 4-2 = 2? Yes. 6-4=2? Yes. So d=2. So valid. So output 1 2.

Similarly for 2: positions are [1,5]. d=4. Since len is 2, valid. So output 2 4.

3 occurs once, so 3 0.

5 occurs once, 5 0.

So the four x's are 1,2,3,5. Sorted order.

So code works.

Now, the code.

In Python:

We can read the input as:

n = int(input())

a = list(map(int, input().split()))

Then, build the pos_dict.

We can use a defaultdict from collections.

But since in Python, for efficiency, it's better to use a normal dict and check for existence.

But in practice, for Python, even for 1e5 elements, using a defaultdict(list) is acceptable.

So code:

from collections import defaultdict

pos_dict = defaultdict(list)

for idx, num in enumerate(a):

    pos_dict[num].append(idx)

Then, collect the keys, sort them.

sorted_x = sorted(pos_dict.keys())

Then, process each x in sorted_x, and collect the valid ones.

result = []

for x in sorted_x:

    positions = pos_dict[x]

    k = len(positions)

    if k ==1:

        result.append( (x, 0) )

    else:

        d = positions[1] - positions[0]

        valid = True

        for i in range(2, k):

            if positions[i] - positions[i-1] != d:

                valid = False

                break

        if valid:

            result.append( (x, d) )

Then, output:

print(len(result))

for x, px in result:

    print(x, px)

This should work.

Testing the sample input:

First sample:

n=1, a=[2]

pos_dict[2] = [0]

k=1 → added to result as (2,0).

Output is 1 followed by 2 0.

Second sample:

pos_dict[1] has [0,2,4,6]. len=4.

d=2.

Check positions 4-2=2, 6-4=2 → valid. So added (1, 2).

pos_dict[2] has [1,5]. len=2 → d=4. valid. added.

others are len 1.

So output as in example.

This code should handle all cases.

Now, checking for time and memory.

n is up to 1e5. The code processes each element once. For each x, the checking is O(k) steps. So total O(n) time.

Space: The pos_dict stores each occurrence's index. So for n elements, it's O(n) space.

In Python, handling 1e5 elements is acceptable.

So this should be the optimal solution.

Edge cases to consider:

- All elements same: e.g., [5,5,5,5]. Then, positions are 0,1,2,3. Check d=1. All differences are 1. So valid. Output 5 1.

- A case where x has three occurrences, but the third is not in arithmetic progression.

Like x occurs at 0, 2, 5. Then d=2. 5-2=3 !=2. So invalid. So x is excluded.

Another case: x occurs once. Included.

Another case: x occurs twice. Included.

Another case: x occurs 3 times, but the first two have d=3, then third is +3. Like positions [0,3,6]. Valid, d=3.

So code should handle all.

Thus, this is the correct approach.
</think>

```python
from collections import defaultdict
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    pos_dict = defaultdict(list)
    for idx, num in enumerate(a):
        pos_dict[num].append(idx)
    
    result = []
    for x in sorted(pos_dict.keys()):
        positions = pos_dict[x]
        k = len(positions)
        if k == 1:
            result.append((x, 0))
        else:
            d = positions[1] - positions[0]
            valid = True
            for i in range(2, k):
                if positions[i] - positions[i-1] != d:
                    valid = False
                    break
            if valid:
                result.append((x, d))
    
    print(len(result))
    for x, px in result:
        print(x, px)

if __name__ == "__main__":
    main()
```