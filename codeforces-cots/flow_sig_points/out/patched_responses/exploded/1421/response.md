<think>
Okay, let's see. The problem is to find the maximum number of blocks we can split the array into such that when each block is sorted, the entire array becomes sorted. Hmm. So each block, when sorted individually, must result in the entire array being non-decreasing. And we want as many blocks as possible.

So how do we approach this? Let's think. The key here is that after sorting each block, the combined array must be non-decreasing. So the blocks must be arranged such that when each is sorted, their concatenation is a sorted array. But how to model this.

Let me think of the sorted version of each block. When we sort all the blocks, the entire array should be sorted. So the sorted blocks, when placed in their original order, must form a non-decreasing sequence. But wait, the blocks are consecutive. So maybe the maximum number of blocks is determined by positions where the maximum of the previous elements is less than or equal to the minimum of the remaining elements.

Wait, that's a common approach in such problems. For example, in the problem where you need to split the array into the maximum number of partitions such that each partition's max is less than or equal to the next's min. So maybe this applies here.

Because, after sorting each block, each block's elements will be sorted. So for the entire array to be non-decreasing, the maximum of the current block (after sorting) must be <= the minimum of the next block (after sorting). But since each block is sorted, the max of a block is the last element of the sorted block, and the min is the first. So the sorted blocks' concatenation must be non-decreasing.

But how to model this. Let's think of the original array. For each position i, if the maximum of the first i elements is <= the minimum of the elements from i+1 to end, then we can split here. Each such split gives a possible block. The number of such splits +1 is the maximum possible blocks.

Yes. So the approach would be:

1. Precompute the maximum from the start up to each index.
2. Precompute the minimum from each index to the end.
3. Then, iterate through the array, and whenever the max up to i is <= the min from i+1, that's a possible split point.

Each time this condition is met, we can split here. The total number of splits is the number of such positions, and the total blocks would be splits +1.

So for example, in the first sample input:

3
1 2 3

The max array is [1,2,3], min array is [1,2,3]. Then for each i from 0 to n-2 (assuming 0-based), check if max[i] <= min[i+1]. For i=0, max[0] =1 <= min[1] =2 → split. For i=1, max[1] =2 <= min[2]=3 → split. So total splits 2, blocks 3.

In the second example:

4
2 1 3 2

The max array would be [2,2,3,3]. The min array would be [1,1,2,2]. Then check for i=0: max up to 0 is 2, min from 1 is 1 → 2>1 → no split. i=1: max up to 1 is 2, min from 2 is 2 → 2 <=2 → split. So split here. Then check i=2: max up to 2 is 3, min from 3 is 2 → 3>2 → no split. So only one split → 2 blocks. Which matches the sample.

So this approach seems correct.

Now, how to compute the max and min arrays efficiently.

For the max array: we can iterate from left to right, keeping track of the current maximum. So for each index i, max_so_far[i] = max(h[0..i]).

For the min array: iterate from right to left. For each index i, min_so_far[i] = min(h[i..n-1]).

Once we have these two arrays, we can loop through each index i from 0 to n-2 (since the split is after i), and check if max_so_far[i] <= min_so_far[i+1]. Each such condition being true increases the block count by 1.

The initial block count is 1 (the whole array), and each split adds 1. So the total blocks is the number of splits +1.

So the steps are:

- Compute max_so_far array.
- Compute min_so_far array.
- Iterate through the array, count the number of splits where max_so_far[i] <= min_so_far[i+1].
- The answer is the count +1.

Now, let's think about the time and space constraints. For n up to 1e5, O(n) time and space is acceptable. Since both max and min arrays can be computed in O(n) time, and the iteration is O(n). So overall O(n) time. Space is O(n) for the two arrays, which is acceptable for 1e5.

In Python, for n=1e5, this should work fine.

Now, let's code this.

First, read n, then the list h.

Compute max_so_far:

Initialize max_so_far as a list of the same length as h. The first element is h[0]. For each i from 1 to n-1: max_so_far[i] = max(max_so_far[i-1], h[i]).

Then compute min_so_far:

Initialize min_so_far as a list of same length. The last element is h[-1]. For i from n-2 down to 0: min_so_far[i] = min(min_so_far[i+1], h[i]).

Then, count the number of i's where max_so_far[i] <= min_so_far[i+1]. The answer is count +1.

But wait, in the sample input 2, the split is after index 1 (0-based):

h = [2,1,3,2]

max_so_far would be [2,2,3,3]

min_so_far is [1,1,2,2]

For i=0: max_so_far[0]=2, min_so_far[1] =1 → 2>1 → no.

i=1: max_so_far[1]=2, min_so_far[2]=2 → yes. count +=1.

i=2: max_so_far[2]=3, min_so_far[3]=2 →3>2 → no.

So count is 1, answer is 2.

Which is correct.

Another test case: when all elements are the same. Then every possible split is allowed. So the answer is n. For example, n=5, all 3's. Then each can be a separate block. So the max and min arrays are all 3. So for each i, the split is possible. So count is 4, answer is 5.

Yes.

So the code should handle that.

Now, code in Python:

Read n, then h.

Compute max_so_far:

max_so_far = [0]*n

max_so_far[0] = h[0]

for i in range(1, n):

    max_so_far[i] = max(max_so_far[i-1], h[i])

Compute min_so_far:

min_so_far = [0]*n

min_so_far[-1] = h[-1]

for i in range(n-2, -1, -1):

    min_so_far[i] = min(min_so_far[i+1], h[i])

count = 0

for i in range(n-1):

    if max_so_far[i] <= min_so_far[i+1]:

        count +=1

answer = count +1

print(answer)

Yes. Now, let's test this code against the samples.

First sample:

n=3, h=[1,2,3]

max_so_far is [1,2,3]

min_so_far is [1,2,3]

Check i=0: 1 <= 2 → yes → count=1

i=1: 2 <=3 → yes → count=2

total count=2 → answer=3. Correct.

Second sample:

n=4, h=[2,1,3,2]

max_so_far is [2,2,3,3]

min_so_far is [1,1,2,2]

i=0: 2 <=1? No. Count remains 0.

i=1: 2<=2 → yes. Count becomes 1.

i=2:3<=2 → no.

count=1 → answer 2. Correct.

Yes. So this should work.

Now, edge cases. What if n=1? Then answer is 1. Because there's only one block.

Another case where all elements are the same. For example, n=5, h = [5,5,5,5,5]. Each split is allowed. So answer 5.

The code would compute for each i from 0 to 3 (since n-1 is 4, loop up to 3), check if max_so_far[i] (which is 5) <= min_so_far[i+1] (5). So yes. So count is 4, answer is 5.

Yes.

Another case: decreasing array. Like 3,2,1. Then the only possible split is the entire array. So answer 1. Because:

max_so_far is [3,3,3]

min_so_far is [1,1,1]

Check i=0: 3 <=1? No.

i=1:3 <=1? No.

So count is 0. Answer 1.

Which is correct.

Thus, the code should handle all cases.
</think>

```python
n = int(input())
h = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

max_so_far = [0] * n
max_so_far[0] = h[0]
for i in range(1, n):
    max_so_far[i] = max(max_so_far[i-1], h[i])

min_so_far = [0] * n
min_so_far[-1] = h[-1]
for i in range(n-2, -1, -1):
    min_so_far[i] = min(min_so_far[i+1], h[i])

count = 0
for i in range(n-1):
    if max_so_far[i] <= min_so_far[i+1]:
        count += 1

print(count + 1)
```