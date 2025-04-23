<think>
Okay, let's see. So the problem is about selecting the maximum number of non-overlapping orders from a list. Each order has a start and end time, and we can't have any overlapping. Oh right, even if one ends exactly when another starts, that's allowed. Wait no, wait the problem says if one ends at the same moment another starts, they can't both be accepted. So like order A ends at 7 and order B starts at 7, then they can't both be accepted. So the intervals must not even touch.

So the classic approach for this kind of problem is to sort the intervals and then select as many as possible. But how to sort them? The usual greedy algorithm for interval scheduling is to sort by end time and pick the earliest ending first, then the next one that starts after the previous end. That's the optimal approach. Let's think about that.

Yes, because choosing the earliest possible end time allows you to fit more intervals afterward. So the steps would be:

1. Sort all the intervals by their end time in ascending order.
2. Iterate through them, keeping track of the last end time. For each interval, if its start time is strictly greater than the last end time, select it and update the last end.

So for the first example input:

2
7 11
4 7

After sorting by end time, the second interval (4-7) comes first. Then the next interval starts at 7 which is not strictly greater than 7, so it's not selected. So maximum 1.

The second example:

5 intervals, all consecutive. Sorting by end time would have them ordered 1-2, 2-3, 3-4, etc. Then we pick 1-2 (last end 2), next start is 2, which is not >2, so skip. Then 3-4: starts at 3 which is >2, so take it. Now last end is 4. Then next is 4-5: starts at 4, not >4. Then 5-6: starts at 5>4, take it. So total 3. Which matches the sample.

So the algorithm seems correct.

Now the challenge is to implement this efficiently for large n (up to 5e5). So in Python, the steps would be:

- Read n.
- Read n pairs of l and r.
- Sort the list of intervals by their end (r) in ascending order.
- Then iterate, keeping track of the last end. For each interval, if l > last_end, take it and update last_end.

But how to handle the sorting efficiently? Well, in Python, the sort is O(n log n) which is acceptable for n=5e5. So that's manageable.

Now the code:

Read n. Then read n lines. For each line, read l and r, maybe as integers. Then sort the list of tuples (r, l) perhaps. Or perhaps just sort using the end as key.

So code outline:

n = int(input())
orders = []
for _ in range(n):
    l, r = map(int, input().split())
    orders.append( (r, l) )

orders.sort()

count = 0
last_end = -infinity (like 0?)

last_end = -1
for r, l in orders:
    if l > last_end:
        count +=1
        last_end = r

print(count)

Wait, but in the sorted list, since we sorted by r, then l can be anything? Because if two intervals have the same end time, which one comes first? For example, if two intervals have same r but different l, which one is better to pick first? Well, the one with the earliest possible end time, but in that case, since r is same, the order of l doesn't matter. But perhaps we should sort by r, then by l. Because for same r, the one with lower l is picked, but that's not necessary. Because once you pick the earliest r, you can't pick any others with same r. So perhaps sorting by r first and then l is redundant. But the code would work either way.

But the sort is done correctly. For example, when you sort the tuples (r, l), then the comparison first compares r. So the list will be sorted by r in ascending order. For same r, the l's are compared. But since we are considering l > last_end, perhaps in some cases, the order of same r intervals can affect the count. Wait, but for same r, if two intervals have l1 and l2. Suppose we pick the first one with l1. Then the next one has l2 which is >= l1 (since sorted by r then l). So l2 would be <= r (since r is same for both). So the next interval can't be selected. So in this case, it's better to pick the one with the largest l, but that's not possible. Wait, no. Because if two intervals have same end r, but one starts at l1 and the other at l2 (l1 < l2), then when sorted by (r, l), the first is (r, l1), then (r, l2). But in the iteration, the first interval's l is l1, and if last_end is set to r, then the next interval's l (l2) is not greater than r. So in the case where two intervals have same end, we should pick the one with the earliest start time. But in this case, if there are two intervals with same end, say (5, 5) and (3,5), then when sorted, they are ordered as (5,3), (5,5). Then, when iterating, the first one's l is 3, which is compared to the initial last_end of -1. So 3 > -1 is true. So count becomes 1, last_end is 5. The next interval's l is 5, which is not greater than 5, so not selected. So total 1. But if there's another interval that starts after 5, then we can include it. So the order in which same-end intervals are sorted doesn't matter in this case, since once you pick one, the others with same end are skipped.

So the code is correct.

Now for handling the input. For n up to 5e5, reading the input via standard input can be slow if using input() each time. So in Python, it's better to read all input at once. So perhaps read via sys.stdin.

So the code can be optimized for speed by reading all the input at once.

So:

import sys

n = int(sys.stdin.readline())
orders = []
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    orders.append( (r, l) )

orders.sort()

count = 0
last_end = -1

for r, l in orders:
    if l > last_end:
        count +=1
        last_end = r

print(count)

But even better, for reading n lines, perhaps using sys.stdin.read() and split into tokens.

Because using sys.stdin.readline() in a loop for 5e5 times may be slow. So better read all data at once.

So here's the code:

import sys

data = sys.stdin.read().split()
n = int(data[0])
orders = []
idx = 1
for i in range(n):
    l = int(data[idx])
    r = int(data[idx+1])
    orders.append( (r, l) )
    idx +=2

orders.sort()

count =0
last_end = -1

for r, l in orders:
    if l > last_end:
        count +=1
        last_end = r

print(count)

This approach is faster because it reads all the data in one go.

Yes, this should work.

Testing the sample inputs.

First sample:

Input is 2 lines after n=2:

7 11 and 4 7.

After data is read, the first two elements after n are 7 and 11 (as data[1] and data[2]), then 4 and 7 (data[3],4).

So orders would be [(11,7), (7,4)]? Wait no, no. Wait the code appends (r, l). So for the first line, the l is 7, r is 11. So the tuple is (11,7). The second line l is 4, r is7. So tuple is (7,4). So orders is [ (11,7), (7,4) ] ?

Wait no, wait the code in the loop:

for i in range(n):

    l = int(data[idx])

    r = int(data[idx+1])

    orders.append( (r, l) )

Yes. So the first line's l is data[1], which is 7, r is data[2], which is 11. So the tuple is (11,7).

The second line's l is data[3], which is 4, r is data[4],7. So tuple (7,4). So orders is [ (11,7), (7,4) ].

Then we sort orders. When sorted by r, the order is (7,4) and (11,7). So the sorted list is [ (7,4), (11,7) ].

Then iteration:

First element: r=7, l=4. Check if l (4) > last_end (-1). Yes. count becomes 1. last_end is 7.

Next element: r=11, l=7. Check if 7>7. No. So count remains 1. So output is 1. Correct.

Second sample input:

5 lines:

1 2

2 3

3 4

4 5

5 6

After parsing, the orders list will have tuples (2,1), (3,2), (4,3), (5,4), (6,5). After sorting, they are in order (2,1), (3,2), (4,3), (5,4), (6,5). Iteration:

count starts 0, last_end -1.

First: l=1 > -1 → count 1, last_end 2.

Next: l=2 → 2 not >2 → no.

Next: l=3>2 → count 2, last_end 3's r is 3.

Wait wait. Wait, the tuples in orders are (r, l). So when sorted, the first tuple is (2,1), then (3,2), (4,3), etc. So during iteration:

For each tuple (r, l) in the sorted list:

Check if l > last_end.

So first (r=2, l=1). l=1 > last_end (-1) → yes. count 1. last_end 2.

Second tuple (3,2). l=2 >2? No. So skip.

Third (4,3): l=3>2 → yes. count 2. last_end 4.

Fourth (5,4): l=4>4? No. Skip.

Fifth (6,5): l=5>4 → yes. count 3. last_end 6. So output 3. Correct.

Third sample:

6
4 8
1 5
4 7
2 5
1 3
6 8

The orders would be:

Original lines:

Line 1: 4 8 → (8,4)

Line 2:1 5 → (5,1)

Line3:4 7 → (7,4)

Line4:2 5 → (5,2)

Line5:1 3 → (3,1)

Line6:6 8 → (8,6)

So the tuples are:

(8,4), (5,1), (7,4), (5,2), (3,1), (8,6)

Sorting these by r:

Order is sorted by r in ascending order, then l.

So first, tuples with r=3: (3,1)

Then r=5: (5,1), (5,2) → sorted by l? Because when r is same, the tuples are sorted by l. So (5,1) comes before (5,2) since 1 < 2.

Then r=7: (7,4)

Then r=8: (8,4), (8,6) → sorted by l (4 <6).

So sorted list:

[(3,1), (5,1), (5,2), (7,4), (8,4), (8,6)]

Now iterate:

count=0, last_end=-1.

First tuple (3,1). l=1 >-1 → yes. count=1, last_end=3.

Next (5,1). l=1>3? No. Skip.

Next (5,2): l=2>3? No. Skip.

Next (7,4):4>3 → yes. count=2, last_end=7.

Next (8,4):4>7? No. Skip.

Next (8,6):6>7? No. So total 2. Correct.

So code works for samples.

Now for handling large n. The code is O(n log n) time, which for 5e5 is acceptable. The space is O(n), which for 5e5 tuples is manageable. In Python, each tuple of two integers takes about 80 bytes (if I remember correctly), so 5e5 tuples would be 40 million bytes, which is 40MB. Well under the 256MB limit.

So the code should work.
</think>

To solve this problem, we need to determine the maximum number of non-overlapping orders that a restaurant can accept. Each order is defined by a start time and an end time, and no two accepted orders can overlap, even at the boundaries.

### Approach
The optimal approach to solve this problem is based on the greedy algorithm. The key steps are as follows:
1. **Sort Orders by End Time**: By sorting the orders based on their end times, we can always pick the order that ends the earliest. This allows us to maximize the number of subsequent orders that can be accommodated.
2. **Iterate and Select Non-overlapping Orders**: After sorting, iterate through the orders and select each order if its start time is strictly greater than the end time of the last selected order. This ensures no overlap between consecutive orders.

### Solution Code
```python
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    orders = []
    idx = 1
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx + 1])
        orders.append((r, l))
        idx += 2
    
    orders.sort()
    
    count = 0
    last_end = -1
    for r, l in orders:
        if l > last_end:
            count += 1
            last_end = r
    
    print(count)

if __name__ == "__main__":
    main()
```

### Explanation
1. **Reading Input Efficiently**: The input is read all at once using `sys.stdin.read()` for efficiency, especially given the large input size constraints.
2. **Sorting**: The orders are sorted by their end times (and then by start times if end times are the same) to facilitate the greedy selection of the earliest ending orders.
3. **Greedy Selection**: By iterating through the sorted orders and selecting each order that starts after the end of the last selected order, we ensure that we maximize the number of non-overlapping orders.

This approach ensures an optimal time complexity of \(O(n \log n)\) due to sorting, followed by a linear scan, making it efficient and suitable for the given problem constraints.