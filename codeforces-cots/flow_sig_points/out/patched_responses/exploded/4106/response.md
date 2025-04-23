<think>
Okay, let's tackle this problem. So the problem is about Maxim buying items with discounts optimally to minimize the total cost. Let me try to understand the problem step by step.

The discounts are of m types. Each discount i requires using a basket with exactly qi items. Then, the customer can take up to two items for free. The free items must each be no more expensive than the cheapest item in the basket. So, the strategy here is to maximize the number of free items by choosing the best possible discounts.

The goal is to buy all n items with the minimum cost. So, the approach would involve selecting how to group the items into baskets (using discounts) and adding free items where possible.

First, let's think about the steps needed to solve this:

1. **Sort the items**: Since the free items must be as expensive as possible (but not more than the basket's cheapest), we need the most expensive items in the basket to maximize the savings. Wait, no. Wait, when you use a discount, the basket has qi items, and then you can take up to two free items that are each <= the cheapest in the basket. So, the cheapest in the basket is the minimum of the qi items. Therefore, to maximize the value of the free items, the free items should be as expensive as possible but not exceeding that minimum.

So, the optimal approach would be to sort the items in descending order. Then, when using a discount, select the qi most expensive items (so that their minimum is as high as possible), allowing the free items to be the next two most expensive items that are <= that minimum.

But how do we group the items to maximize the discount usage?

Let me think about the approach:

- Sort all the items in non-increasing order. So a1 >= a2 >= ... >= an.
- For each group of items selected as a basket (using a discount), the qi items in the basket. The minimum of these is a_k (since sorted), so the next two items (if available) can be taken for free, provided they are <= a_k.

So the strategy is to take the largest possible qi (or the best possible qi) for grouping, then take two free items. Wait, but the discount types can have various qi values. So the optimal qi for each group is the smallest possible qi that allows us to get the maximum number of free items. Wait, no. The problem allows us to choose any discount type each time. So for each group, we can choose the best qi that gives the maximum savings.

Wait, but how to model this. For example, the best qi for a group would be the one that requires the smallest number of items to buy (so we can get more free items per paid item). Because using a smaller qi (like qi=1) would allow you to get two free items every time you buy one. But qi can't be smaller than 1. Wait, the problem says that when you use discount i, you have to put exactly qi items in the basket. So using a discount i with qi=2 requires buying 2 items and then getting up to two free ones. So per discount application, you can get up to two free items. So the optimal way is to use the discount that allows you to get as many free items as possible per paid item.

So, the key is to find the minimal qi among all discount types. Let's call this q_min. Because using a discount with q_min gives the most frequent opportunity to take two free items. For example, if q_min is 1, then every time you buy one item, you can take two free items. So groups of 1+2 =3 items. But if q_min is 2, then each group is 2 paid items +2 free items. So every 4 items, but paying for 2. So the minimal qi is the best because it allows the highest ratio of free items per paid item.

So the first step is to compute q_min = min(q1, q2, ..., qm). Because using this q_min gives the best possible way to get free items.

Once we have q_min, the optimal strategy is to group the items into batches of (q_min + 2) items as much as possible. Because for each q_min items paid, you can get 2 free. So every group of (q_min + 2) items, you pay for q_min, and get 2 free. However, if there are remaining items that can't form a full group of (q_min + 2), then we need to handle those as well.

Wait, but how do we apply this grouping? Let's think:

1. Sort all a_i in descending order. So the most expensive items come first.

2. For the first x groups of (q_min + 2) items: in each group, pay for the first q_min items (since they are the most expensive), and take the next two as free.

Wait, but the free items must be <= the cheapest in the paid items. So, the q_min items in the basket must have their minimum (the last one in the group of q_min) >= the free items.

So, in order for the two free items to be valid, they must be <= the minimum of the q_min items in the basket.

But when we sort the array in descending order, the first q_min items in the group are the largest. So the minimum of these q_min items is the last one in that subset. The next two items (the ones taken as free) must be <= that minimum.

But when the array is sorted in descending order, the next two items are the next two in the list, which are <= the previous items. But since the minimum of the q_min items is the last one in their subset (the q_min-th item in the group), the next two items (which are part of the group in the sorted list) must be <= that.

Wait, yes. Because in the sorted array, each item is <= the previous. So the q_min items are the first q_min in the group, their minimum is the last one (the q_min-th item). Then the next two items are part of the group (q_min + 1 and q_min + 2) in the sorted array, which are <= the q_min-th item. Therefore, they are valid as free items.

Therefore, by grouping the sorted array into chunks of (q_min + 2) items, and in each chunk paying for the first q_min and getting the next two for free, this is a valid and optimal approach.

So the steps would be:

- Sort the array in non-increasing order.

- Find q_min = min(q_i) from all discount types.

- Process the sorted array in chunks of (q_min + 2). For each chunk:

   - The first q_min items are paid (sum them).

   - The next two are free (add 0).

   - Then, proceed to the next chunk.

- Any remaining items after forming as many such chunks as possible are handled as follows:

   - For the remaining items, if there are any, they can't form a full (q_min + 2) chunk. So, for these, we can take the first (remaining) items, up to q_min + any remaining, but we can't get any free items. Or maybe, perhaps there's a better way.

Wait, but perhaps for the remaining items, we can still apply discounts to some of them. For example, if there are r items left after forming k full chunks, then for these r items:

- If r >= q_min, then we can take a discount (q_min items) and possibly take up to two free items if available. But wait, the remaining items are after the chunks. Let's say the remaining are in positions (k*(q_min+2) + 1) to n. So, in sorted order, these are the least expensive items. So, taking a discount for q_min of them (the last few items, which are the cheapest) and then taking free items (if any) which are even cheaper. But since they are in sorted order, after the full chunks, these are the cheapest. So, if there are remaining items, perhaps taking the first q_min and then the next two, but these next two would be cheaper than the q_min's minimum.

Wait, no. Wait, the sorted array is in descending order. So the first items are the most expensive. The chunks are formed by grouping the first (q_min + 2) items as a group, then the next (q_min +2), etc. So the remaining items after all full chunks are the least expensive. So when processing the remaining items, if we take a discount on some of them, we can get up to two free items, but those free items would be even cheaper. But since they are part of the sorted array, the next items after the q_min in the remaining group would be <= the minimum of the q_min items. So, perhaps even the remaining items can be split into a discount group and some free items.

Wait, let's think with an example. Suppose after processing all full (q_min + 2) chunks, we have 5 items left. Let's say q_min is 2. Then 5 items left. So the first two would be paid (sum them). Then next two are free. Then one more item left, which has to be paid. So total paid is sum of first two + sum of last one. So total paid 3 items. But wait, the free items are possible only if they are <= the minimum of the basket. Since the array is sorted in descending order, the first two (paid) items are the highest of the remaining. The minimum of those two is the second one. The next two (free) items are the third and fourth, which are <= the second. The fifth is left, which is paid.

So in this case, for the remaining 5 items, using one discount (q_min=2) would allow two free items, and then the fifth item is paid. So total paid is 2+1=3 items.

But how do we model this for the remaining items after full chunks?

The approach would be:

For the remaining items after forming k full (q_min + 2) chunks, let's process them as follows:

- Take the first q_min items (if possible), pay for them. Then take up to two free items (if available). Then the remaining items (if any) are paid.

So for the remaining r items (r = n - k*(q_min + 2)):

If r >= q_min:

   - pay for the first q_min items.

   - take min(2, r - q_min) items as free.

   - the remaining (r - q_min - 2) items (if any) are paid.

Else:

   - all r items are paid.

Wait, but this may not be optimal. For example, maybe there's a better way to group the remaining items using other discount types. But since q_min is the minimal possible qi, using a discount with higher qi may not give us as many free items. Because using higher qi would require more items to be paid, but gives the same number of free items (max 2). So it's better to use the minimal qi possible, which is q_min. So for the remaining items, the optimal approach is to use the same q_min discount.

So the plan is:

1. Sort all a_i in descending order.

2. Find q_min as the minimal qi.

3. Process the sorted list in chunks of (q_min + 2) items. For each chunk, add the sum of the first q_min items (the rest are free).

4. For the remaining items (after as many chunks as possible), process them by:

   a. Taking as many q_min groups as possible, each time getting up to two free items.

Wait, maybe not. Let's think again.

Wait, when processing the remaining items after full chunks, the approach is:

For the remaining r items:

- If possible, take a group of q_min items (paid) and up to two free items.

So the number of free items is min(2, r - q_min). If r >= q_min, then you can take two free items if available, else take as many as possible. Then the rest are paid.

So in code:

sum += sum of a[0..q_min-1]

sum += sum of a[q_min + 2..r-1] (if any)

Wait, no. Because the first q_min items are paid, then the next two are free, then any remaining items are paid. Because after the first q_min + 2 items (paid q_min, free 2), any remaining items are beyond that and can't form another group. So for example, if r is 5, q_min=2:

positions 0-1: paid (sum += a[0] + a[1])

positions 2-3: free

position 4: paid.

So for the remaining 5 items (indices 0 to 4 in the remaining list):

sum += a[0] + a[1] + a[4]

So total of 3 paid items.

So the code for the remaining items would be:

start = k*(q_min + 2)

end = n

sum += sum of a[start : start + q_min]

free = min(2, end - (start + q_min))

remaining_start = start + q_min + free

sum += sum of a[remaining_start : end]

Wait, that's right. Because in the remaining items, the first q_min are paid, then up to two are free. The rest (after start + q_min + free) are paid.

So the steps are:

sum += sum of a from start to start + q_min -1.

sum += sum of a from (start + q_min + free) to end -1.

But how to calculate this in code?

In Python, slicing is easy. But since the array is sorted in descending order, the first part (paid) are the highest in the remaining items.

So the algorithm steps:

Sort the array in non-increasing order.

Compute q_min as min of all qi.

Compute the number of full chunks: each chunk is (q_min + 2) items.

For each full chunk, sum the first q_min items.

For the remaining items:

start = full_chunks * (q_min + 2)

If start >= n: nothing to do.

Else:

r = n - start

paid_in_remaining = 0

if r >= q_min:

   paid_in_remaining += sum(a[start : start + q_min])

   free = min(2, r - q_min)

   remaining = r - q_min - free

   if remaining > 0:

      paid_in_remaining += sum(a[start + q_min + free : start + q_min + free + remaining])

else:

   paid_in_remaining += sum(a[start : start + r])

sum += paid_in_remaining

So the total sum is sum of all paid items.

Wait, but what if there are multiple discount types with varying qi, but the q_min is the best. So the approach is to use q_min as much as possible to get the maximum number of free items.

So the steps are correct.

Now, let's test with the examples.

First example:

Input:

1

2

4

50 50 100 100

Sorted a: 100,100,50,50

q_min is 2.

Each chunk is 2+2=4 items. So one full chunk.

Paid items are the first 2: 100 + 100 = 200. The next two (50,50) are free. So sum is 200, which matches the output.

Second example:

Input:

2

2 3

5

50 50 50 50 50

q_min is 2.

Each chunk is 4 items.

But n=5. So full chunks = 1 (4 items). Remaining 1.

Processing full chunk: first 2 are paid (50+50=100), next two free (50+50). Sum is 100.

Remaining 1 item (50). Paid.

Total sum: 100 +50=150. Which matches the output.

Third example:

Input:

1

1

7

1 1 1 1 1 1 1

q_min=1. So each chunk is 1+2=3 items.

7 items: 7//3=2 full chunks (2*3=6 items). Remaining 1.

Full chunks:

Each chunk: pay first 1, get two free. So 2 chunks: 1+1=2. Remaining 1 paid. Total 3.

Which matches the sample.

So the approach works.

Now, how to implement this efficiently.

First, read m, then the list of q's. Find the minimum q. Then read n, the list a, sort it in reverse order.

Then compute the sum as per the algorithm.

But since n can be up to 1e5, and the list a can be up to 1e5 elements, we need an O(n log n) solution, which is acceptable.

The steps are:

Sort the array in non-increasing order.

Calculate the sum by:

- For each full chunk of (q_min + 2) items, sum the first q_min items.

- For the remaining items, sum the first q_min (if possible) and the leftover after taking up to two free.

Now, let's code this.

In Python, to compute the sum efficiently, precompute the prefix sums.

For example, compute the prefix sum array of the sorted list. Then, for each full chunk, the sum is the sum of the first q_min elements in that chunk.

But the chunk is (q_min + 2) elements. So for the first chunk (0 to q_min+1), the sum is a[0] + a[1] + ... + a[q_min-1].

Then, for the next chunk, it's a[q_min+2 + 0] to a[q_min+2 + q_min-1], etc.

So the full_chunks = (n) // (q_min + 2). Wait, no. Wait, the number of full chunks is the number of times we can take (q_min + 2) elements from the sorted list.

So full_chunks = n // (q_min + 2) if the division is exact, else floor(n / (q_min+2)).

Wait, no. Because each chunk is (q_min + 2) elements. So the maximum possible number of full chunks is k = (n) // (q_min + 2). For example, if n=7 and q_min +2=3, then 7//3=2 full chunks (6 elements), with 1 left.

Wait, yes.

So the number of full chunks is k = n // (q_min + 2).

Wait, no. For example, n=5, q_min+2=4: 5//4=1 full chunk (4 elements), with 1 left.

So the code would be:

k = n // (q_min + 2)

Then, each chunk has (q_min + 2) elements, and the sum for each chunk is the sum of the first q_min elements.

So for each chunk i (0 <= i <k), the start index is i*(q_min+2), and end index is i*(q_min+2) + q_min.

So the sum for the full chunks is sum of a[0..q_min-1] + sum a[q_min+2..q_min+2 + q_min-1] + ... for each chunk.

But if we have a prefix sum array, this can be computed as:

for each chunk, the start is i*(q_min+2), the end is start + q_min.

So the sum for full chunks is sum from prefix[start] to prefix[end].

But building the prefix sum array is O(n), which is acceptable.

So the code steps:

Sort the array in non-increasing order.

Compute prefix sums.

Calculate the sum for full chunks:

sum_full = sum of a[i*(q_min+2) : i*(q_min+2) + q_min] for i in 0..k-1.

Which can be calculated using the prefix sum array.

Then process the remaining elements:

start = k*(q_min+2)

r = n - start

if r ==0:

   sum_remaining =0

else:

   sum_remaining =0

   if r >= q_min:

      sum_remaining += prefix[start + q_min] - prefix[start]

      free = min(2, r - q_min)

      remaining_items = r - q_min - free

      if remaining_items >0:

          sum_remaining += prefix[start + q_min + free + remaining_items] - prefix[start + q_min + free]

   else:

      sum_remaining += prefix[start + r] - prefix[start]

Total sum is sum_full + sum_remaining.

So the code can be written with prefix sums.

But building the prefix array is easy. Let's see.

In Python:

a_sorted = sorted(a, reverse=True)

prefix = [0]*(n+1)

for i in range(n):

    prefix[i+1] = prefix[i] + a_sorted[i]

Then:

q_min = min(q_list)

chunk_size = q_min + 2

k = n // chunk_size

sum_full = 0

for i in range(k):

    start = i * chunk_size

    end = start + q_min

    sum_full += prefix[end] - prefix[start]

start_remaining = k * chunk_size

r = n - start_remaining

sum_remaining = 0

if r >0:

    if r >= q_min:

        sum_remaining += prefix[start_remaining + q_min] - prefix[start_remaining]

        free = min(2, r - q_min)

        remaining_start = start_remaining + q_min + free

        sum_remaining += prefix[start_remaining + r] - prefix[remaining_start]

    else:

        sum_remaining += prefix[start_remaining + r] - prefix[start_remaining]

total = sum_full + sum_remaining

print(total)

Wait, but in the case where r >= q_min:

sum_remaining is sum of the first q_min items (start_remaining to start_remaining + q_min -1), which is prefix[start_remaining + q_min] - prefix[start_remaining].

Then, the free items are the next free (0, 1, or 2) items. So the remaining items after the first q_min + free items is start_remaining + q_min + free. The sum is sum of the items from start_remaining + q_min + free to the end (start_remaining + r -1). Which is prefix[start_remaining + r] - prefix[start_remaining + q_min + free]

So code for that part:

sum_remaining += prefix[start_remaining + q_min] - prefix[start_remaining]

free = min(2, r - q_min)

remaining_start = start_remaining + q_min + free

sum_remaining += prefix[start_remaining + r] - prefix[remaining_start]

Yes.

But what if after taking q_min + free, there are no remaining items? Then remaining_start would be start_remaining + r, and prefix[remaining_start] would be same as prefix[start_remaining + r], so the second term is zero.

So that's correct.

Testing with the first example:

n=4, q_min=2, chunk_size=4. k=4//4=1. sum_full is sum of 0-1 (100+100). start_remaining=4, which is beyond n=4, so sum_remaining is zero. total=200.

Second example:

n=5, q_min=2, chunk_size=4. k=5//4=1. sum_full is sum of 0-1 (50+50). start_remaining=4, r=1. Since r < q_min (2), sum_remaining is sum of [4:5] (50). total 100+50=150.

Third example:

n=7, q_min=1, chunk_size=3. k=7//3=2. sum_full is sum of 0-0 (1) for first chunk (0-0) and sum of 3-3 (1) for second chunk. sum_full=1+1=2. start_remaining=6, r=1. sum_remaining is 1. total=3.

Which matches the sample.

Another test case: when r is 5, q_min=2.

r=5 >= q_min=2.

sum_remaining first part: sum of 2 items.

free = min(2, 5-2=3) => 2.

remaining_start = 2+2=4.

remaining items: 5-2-2=1. sum from 4 to 4 (since 5 is start_remaining +r = start_remaining +5, which is 6+5=11? Wait, maybe not. Let's see.

Suppose start_remaining is 6, r=5. Then start_remaining is 6, q_min=2.

sum_remaining first part: sum of a[6..7] (assuming a is sorted). Then free is 2 (r - q_min=3). Then remaining items: 5-2-2=1. So the sum_remaining is sum of a[6..7] + sum a[6+2+2 ... 6+5-1] = sum a[6..7] + sum a[10..10] (since 6+5-1 =10). But if the array is of size 11 (n=11?), but this is just an example.

So code for sum_remaining in this case would be:

sum_remaining += a[6] + a[7]

sum_remaining += a[10]

Which is correct.

Thus, the code seems to handle all cases.

Now, the code must read input correctly. So:

Read m.

Read m q's as a list.

Read n.

Read a list of n integers.

Sort a in reverse order.

Compute q_min.

Compute chunk_size = q_min + 2.

Compute k = n // chunk_size.

Compute sum_full as sum of first q_min elements in each chunk.

Then compute sum_remaining.

But in code, the prefix array is built as follows:

prefix[0] =0.

prefix[1] = a[0]

prefix[2] = a[0] +a[1], etc.

So in Python:

a_sorted = sorted(a, reverse=True)

prefix = [0] * (len(a_sorted) + 1)

for i in range(len(a_sorted)):

    prefix[i+1] = prefix[i] + a_sorted[i]

Then, the code proceeds.

Now, considering the constraints:

n is up to 1e5. Sorting a list of 1e5 elements is O(n log n), which is acceptable for Python.

The prefix sum is O(n), which is acceptable.

The rest of the code is O(1) or O(k), which is O(n / chunk_size). Since chunk_size can be as small as 1+2=3 (if q_min=1), so k can be up to 1e5 /3 ≈ 3e4. But even if m is up to 1e5, the code will handle it.

Wait, but in code, the loop for i in range(k) is O(k), which is up to 1e5 / 3 = 33334 iterations. Which is acceptable.

But for Python, even 1e5 iterations are acceptable.

But wait, when chunk_size is 3, k can be up to 1e5 /3 ≈ 33334. So looping 33334 times in Python is acceptable.

But perhaps there's a smarter way to compute sum_full without a loop.

Because sum_full is the sum of the first q_min elements in each chunk.

Each chunk is of size (q_min+2), and there are k chunks. So for the first chunk, elements 0 to q_min-1. Second chunk: (q_min+2) to (q_min+2) + q_min-1, etc.

The sum can be computed as sum( a_sorted[i*(chunk_size) + j] for j in 0..q_min-1 for i in 0..k-1 )

But with the prefix sum array, this can be calculated as sum( prefix[i*chunk_size + q_min] - prefix[i*chunk_size] for i in 0..k-1 )

Which is the same as:

sum_full = sum( prefix[i * chunk_size + q_min] - prefix[i * chunk_size] for i in range(k) )

But in Python, list comprehensions are efficient. But for k up to 3e4, this is manageable.

Alternatively, since the chunks are consecutive and non-overlapping, we can compute the start and end indices for each chunk and sum the prefix sums.

Another approach is to compute the total sum_full as:

sum_full = prefix[k * chunk_size + q_min * k] - sum of the parts where the chunks are skipped.

Wait, perhaps not. Because each chunk contributes q_min elements, but the chunks are spaced by chunk_size elements. So the first chunk is 0 to chunk_size-1, but the sum is first q_min elements. Second chunk starts at chunk_size, sum next q_min elements, and so on.

But the code as written is correct.

So the code seems correct.

Now, let's write the Python code.

But in Python, reading input correctly is important.

The input has:

First line: m.

Second line: m integers separated by spaces.

Third line: n.

Fourth line: n integers separated by spaces.

So code:

import sys

m = int(sys.stdin.readline())

q_list = list(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

a_sorted = sorted(a, reverse=True)

q_min = min(q_list)

chunk_size = q_min + 2

prefix = [0] * (n + 1)

for i in range(n):

    prefix[i+1] = prefix[i] + a_sorted[i]

k = n // chunk_size

sum_full = 0

for i in range(k):

    start = i * chunk_size

    end = start + q_min

    sum_full += prefix[end] - prefix[start]

start_remaining = k * chunk_size

r = n - start_remaining

sum_remaining = 0

if r > 0:

    if r >= q_min:

        sum_remaining += prefix[start_remaining + q_min] - prefix[start_remaining]

        free = min(2, r - q_min)

        remaining_start = start_remaining + q_min + free

        sum_remaining += prefix[start_remaining + r] - prefix[remaining_start]

    else:

        sum_remaining += prefix[start_remaining + r] - prefix[start_remaining]

total = sum_full + sum_remaining

print(total)

But wait, in the remaining code, when r >= q_min:

sum_remaining is sum of the first q_min items (start_remaining to start_remaining + q_min -1), which is prefix[start_remaining + q_min] - prefix[start_remaining].

Then, free is the number of free items, which is min(2, r - q_min). Then, the remaining items after start_remaining + q_min + free are summed. So from start_remaining + q_min + free to start_remaining + r -1 (since r is the total remaining items, which are from start_remaining to start_remaining + r -1).

Yes.

Testing this code with the samples.

Sample 1:

Input:

1

2

4

50 50 100 100

a_sorted becomes [100,100,50,50]

prefix is [0, 100, 200, 250, 300]

q_min is 2, chunk_size=4.

k=4//4=1. sum_full = prefix[2] - prefix[0] = 200.

start_remaining=4. r=0. sum_remaining=0. Total 200.

Sample 2:

Input:

2

2 3

5

50 50 50 50 50

a_sorted [50,50,50,50,50]

prefix [0,50,100,150,200,250]

q_min=2, chunk_size=4.

k=5//4=1. sum_full is prefix[2] - prefix[0] =100.

start_remaining=4. r=1.

r < q_min (2). sum_remaining = prefix[4+1] - prefix[4] = 50. Total 150.

Sample 3:

Input:

1

1

7

1 1 1 1 1 1 1

a_sorted [1,1,1,1,1,1,1]

prefix [0,1,2,3,4,5,6,7]

q_min=1, chunk_size=3.

k=7//3=2. sum_full:

i=0: start=0, end=1. prefix[1]-prefix[0] =1.

i=1: start=3, end=4. prefix[4]-prefix[3] =1.

sum_full=2.

start_remaining=6. r=1.

sum_remaining = prefix[7] - prefix[6] =1. Total 3.

All tests pass.

Thus, the code should work.
</think>

```python
import sys

def main():
    m = int(sys.stdin.readline())
    q_list = list(map(int, sys.stdin.readline().split()))
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a_sorted = sorted(a, reverse=True)
    q_min = min(q_list)
    chunk_size = q_min + 2
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a_sorted[i]
    k = n // chunk_size
    sum_full = 0
    for i in range(k):
        start = i * chunk_size
        end = start + q_min
        sum_full += prefix[end] - prefix[start]
    start_remaining = k * chunk_size
    r = n - start_remaining
    sum_remaining = 0
    if r > 0:
        if r >= q_min:
            sum_remaining += prefix[start_remaining + q_min] - prefix[start_remaining]
            free = min(2, r - q_min)
            remaining_start = start_remaining + q_min + free
            sum_remaining += prefix[start_remaining + r] - prefix[remaining_start]
        else:
            sum_remaining += prefix[start_remaining + r] - prefix[start_remaining]
    total = sum_full + sum_remaining
    print(total)

if __name__ == "__main__":
    main()
```