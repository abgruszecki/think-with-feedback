<think>
Okay, let's see. We need to solve this problem where passengers are entering a bus with rows of seats, and depending on whether they are introverts or extroverts, they choose seats in specific rows. The problem is to determine which row each passenger takes.

Hmm. Let's start by understanding the problem deeply. So each row has two seats. For an introvert, they pick a row that's completely empty, and among those, the one with the smallest width. For an extrovert, they pick a row that has exactly one occupied seat (so introverts must have taken one seat there), and among those, the largest width.

So the order in which the passengers come is given as a string of 0s and 1s. Each 0 is an introvert, each 1 is extrovert. We need to output the row numbers for each of the 2n passengers in order.

The constraints are up to n=200,000, which is 2e5. So any O(n log n) algorithm would be acceptable, but O(n^2) would be way too slow.

First, let's think about how to model the available rows for introverts and extroverts.

For introverts: They choose the smallest available width row. So initially, all rows are available. As introverts take seats, the available rows decrease. But since each row has two seats, an introvert takes one seat, leaving the row with one seat left. So after an introvert picks a row, that row is no longer available for other introverts (since it's no longer fully empty). Instead, it becomes a candidate for extroverts.

For extroverts: They need a row that has exactly one seat occupied. So whenever an extrovert comes, they pick the largest width row among those rows that have one seat occupied. Once they take the seat, that row is filled (both seats taken) and is no longer available for anyone.

So the key is to manage two data structures:

1. For introverts: a priority queue (min-heap) of rows that are completely empty. Each time an introvert comes, we take the smallest width row, assign one seat, and move the row to a structure that extroverts can use.

2. For extroverts: a priority queue (max-heap) of rows that have exactly one seat occupied. Each time an extrovert comes, we take the largest width row from this heap, assign the seat, and remove the row from consideration.

But how do we efficiently manage these transitions?

Let's break it down step by step.

Initially, all rows are in the introvert's available pool. So we need to sort them by width in ascending order (since the introverts pick the smallest first). But since the rows are given in any order, we can process them by sorting once.

Wait, the input gives w_i as a sequence. So first, we can sort the rows by their width. For introverts, the order they take them is the sorted order, but each row is used once (each row can be taken by an introvert once, as after that it has one seat filled, and then when an extrovert takes the other seat, the row is filled).

Wait no. Because each introvert takes a row that's completely empty. So each row can be chosen by an introvert exactly once. So, for example, the first introvert picks the row with the smallest width. Then the next introvert picks the next smallest, etc. So the rows available for introverts are the ones that are still completely empty.

So, for the introverts, the order in which rows are selected is the sorted order of their widths. But once a row is chosen by an introvert, it's no longer available for other introverts. So we can model the available rows for introverts as a min-heap. Each time an introvert comes, we extract the smallest row from the heap. Then, this row has one seat occupied, so it's added to a max-heap for extroverts (since when an extrovert comes, they need the largest available row from those with one seat occupied).

So the steps would be:

- Preprocess the rows by sorting them in increasing order of width. Then, create a min-heap (but actually, since they are already sorted, perhaps we can use a pointer to track the next available row for introverts). Wait, wait. Because the rows are sorted, and for introverts, each time they pick the next smallest available row, perhaps we can just process them in order. Because once the first introvert picks the first row, the next introvert picks the next in the sorted list, but only if that row hasn't been taken yet. Wait no. Because once a row is picked by an introvert, it's removed from the available pool. So the next introvert must pick the next smallest available row.

Wait, but if all the rows are sorted in ascending order, and we have them in a list, then each time an introvert comes, we can pick the next row in the sorted list. Because once a row is taken by an introvert, it's no longer available for other introverts. So for the introverts' choices, the order is exactly the sorted order of the rows. So the first introvert takes the first in the sorted list, the second takes the second, etc.

But this is only true if all the introverts are consecutive. But the order of passengers can be mixed. For example, in the first sample input, the order is 0011. So the first two passengers are introverts, then two extroverts. So the first introvert picks the smallest row (row 2, width 1), the second picks the next smallest (row 1, width 3). Then the extroverts pick the largest available from the rows that have one seat. So the third passenger is extrovert, so looks at rows 2 and 1 (since they each have one seat occupied). The largest width is row 1 (3), so they take that. Then the fourth extrovert has only row 2 left (width 1) to take.

But in this case, the sorted list of rows would be [row 2 (w=1), row 1 (w=3)]. So the first two introverts take those two rows in order. Then when extroverts come, they look for rows with one seat occupied, which are these two. So the max-heap for extroverts would need to have the rows sorted by width in descending order.

So the plan is:

1. Sort all the rows by their width in ascending order. This gives the order in which introverts will take them. So the first introvert takes the first in the sorted list, the next the second, etc.

2. However, the order of the passengers is arbitrary. So whenever a 0 (introvert) comes, we take the next row in the sorted list. But how to track which rows are available for introverts?

Wait, but since each row can be taken by an introvert exactly once (only once when it's empty), the sorted list can be processed in order. So the first 0 in the passenger list would take the first row in the sorted list. The second 0 would take the next, etc. So regardless of when the 0s come in the passenger order, each 0 takes the next row in the sorted list.

Wait, no. For example, imagine a passenger order like 0,1,0,1. So the first 0 takes the first sorted row, then the 1 takes the largest available row with one seat (which is that first row). Then the next 0 would take the next sorted row, and the next 1 takes that.

Ah, right. So the introverts are processed in the order of the sorted list, regardless of when they appear in the passenger sequence. So the available rows for introverts are the next in the sorted list, but only if they haven't been taken by a previous introvert.

Wait, but how can that be? Because once a row is taken by an introvert, it's added to the extrovert's max-heap. But if an introvert comes after an extrovert, they can't take a row that was already taken by an introvert. So the introverts must take the rows in the sorted order, in the order they appear in the sorted list, regardless of when the 0s are in the passenger sequence.

Wait, no. Suppose the passenger sequence has a 0, then a 1 (extrovert), then another 0. The first 0 takes the first row. The 1 takes that row (since it's now one seat occupied). The next 0 comes, and needs to take the next row in the sorted list. But what if the next row in the sorted list hasn't been taken by an introvert yet? So the introverts must take the rows in the order of the sorted list, one after another, each time a 0 is encountered.

So, the sorted list is the order in which the introverts will pick. So for example, if there are 5 rows sorted as row1, row2, row3, row4, row5 (ascending), then the first 0 takes row1, the next 0 takes row2, and so on, regardless of how the 0s are interleaved with 1s in the passenger list.

Wait, but that can't be. Suppose there are three rows sorted as w1 < w2 < w3. The passenger sequence is 0,1,0,1,0,1. The first 0 takes row1. The 1 takes row1. Then the next 0 takes row2. The next 1 takes row2. Then next 0 takes row3, and the 1 takes row3.

So the order in which the introverts take the rows is in the sorted order, regardless of when the 0s are in the passenger sequence. So each time a 0 is processed, we take the next row in the sorted list. So the key is to track the index of the next available row in the sorted list for introverts.

But how do we model this? Because each 0 in the passenger sequence must take the next row in the sorted list, regardless of other operations. So even if there's a 0 followed by a 1, and then another 0, the second 0 takes the next row in the sorted list after the first 0's row.

So this suggests that the introverts' rows are allocated in the order of the sorted list, and the next available row for introverts is tracked by a pointer. So for example, we can have a variable 'next_introvert' which starts at 0 and increments each time a 0 is processed. Then, each 0 in the passenger sequence would take the row at index 'next_introvert' in the sorted list. Then, that row is added to a max-heap for extroverts.

But how does that work with the example? Let's take the first sample input:

n=2, w = [3,1]. So sorted list is sorted by w: [1 (row 2), 3 (row 1)]. The passenger sequence is 0011.

The first 0: next_introvert is 0, so take row 2 (index 0 in sorted list). Then next_introvert becomes 1. Then the next 0 takes row 1 (index 1). Then for the 1s, they take from the max-heap.

Each time a 0 is processed, the row is added to the extrovert's max-heap, which is a max-heap based on the width. So when an extrovert comes, we take the largest available row from the max-heap.

So the steps for the first example:

Passenger 0 (0th index in input string) is 0. Assign row 2 (sorted list index 0), then add this row to the extrovert's max-heap. Output is 2.

Passenger 1 (1st index) is 0. Assign row 1 (sorted index 1). Add to max-heap. Output is 1.

Passenger 2 is 1. Take the max from the heap (row 1, width 3). Output 1.

Passenger 3 is 1. Take the next max (row 2, width 1). Output 2.

So the output is 2 1 1 2, which matches the sample.

Another example: when the passenger order has 0,1,0,1. Let's say sorted list is row1 (w1), row2 (w2), row3 (w3). Then:

Passenger 0: take row1. Add to max-heap.

Passenger1 is 1: take max (row1), output.

Passenger2 is 0: take next_introvert (index 1) row2. Add to heap.

Passenger3 is 1: take row2.

So the output would be 1,1,2,2.

So this seems to work.

So the approach is:

- Sort the rows in ascending order of width.

- For each 0 in the passenger sequence, assign the next row in the sorted list. Each time a 0 is processed, the row is added to the extrovert's max-heap.

- For each 1 in the passenger sequence, extract the maximum element from the extrovert's max-heap.

So the key data structures are:

- The sorted list of rows for introverts (sorted by width ascending).

- A max-heap for the extroverts (rows with exactly one seat taken, sorted by width descending).

Now, the problem is implementing this efficiently.

In Python, the heapq module only implements a min-heap. To create a max-heap, we can insert negative values.

So steps for implementation:

1. Read n.

2. Read the list of w. But we need to track the original row numbers (1-based). So each row is (w, index). So we create a list of tuples (w_i, original index).

3. Sort this list by the w in ascending order.

4. For the sorted list, the order in which introverts pick the rows is the order of the list. So for each 0 in the passenger sequence, we take the next row from this sorted list.

5. For the extroverts, each time a row is picked by an introvert, it is added to the max-heap (which is sorted by descending w). For Python's heapq, we can push tuples of (-w, original index), so that the smallest (most negative) comes first, which represents the largest w.

6. So, for each character in the passenger string:

   a. If it's '0', take the next row from the sorted list (tracked by a pointer, say 'current_introvert'), assign the original index, then push (-w, original index) into the heap.

   b. If it's '1', pop the smallest element from the heap (which is the max w), and assign the original index.

Now, the time complexity for this approach is O(n log n). Sorting is O(n log n). Each 0 adds to the heap (O(log n) per insertion). Each 1 pops from the heap (O(log n) per pop). Since there are n 0s and n 1s, the total time is O(n log n), which should be acceptable for n=2e5.

But in Python, using the heapq module for the max-heap may be efficient enough, as each operation is O(log k), where k is the number of elements in the heap. Since in the worst case, all n 0s come first, and the heap grows to n elements. Then for each 1, popping is O(log n) each. So 2n log n operations.

Memory-wise, storing the sorted list is O(n). The heap can take up O(n) space. Which should be manageable for n=2e5.

So the plan is:

- Pre-sort the rows by w in ascending order.

- Use a pointer to track the next row to assign for introverts.

- Use a max-heap (implemented as a min-heap with negative w) to track available rows for extroverts.

So code steps:

Read n.

Read the list of w_i. Then create a list of tuples (w_i, original index (1-based)), sort this list in ascending order of w_i.

Read the passenger string.

Initialize current_introvert = 0, which points to the next available row in the sorted list.

Initialize a max-heap (using heapq, but storing -w and the original index).

For each c in the passenger string:

   if c == '0':

       take sorted_rows[current_introvert], add its original index to the output.

       push (-w, original index) into the heap.

       current_introvert += 1

   else:

       pop from heap, append the original index to the output.

So, for example, in the first sample:

sorted rows after sorting by w:

(1, 2), (3, 1)

current_introvert starts at 0.

passenger string is '0011'.

First two 0s:

current_introvert 0 → row 2, push (-1, 2). current_introvert becomes 1.

current_introvert 1 → row 1, push (-3, 1). current_introvert becomes 2.

Then two 1s:

pop (-1) → 1, which is the smallest in the heap (but represents the largest w, which is 3. Wait no. Wait, the heap stores (-w, index). So when you pop the smallest (i.e., most negative), that's the largest w. Let me see:

In the first case, after two 0s, the heap has elements (-1, 2) and (-3, 1). The heap is a min-heap, so the first element is the smallest, which is -3. Wait no. Wait, when you push (-3, 1) and (-1, 2), the heap structure would have the smallest element at the root. So -3 is smaller than -1, so the root is -3. So when you pop, you get (-3, 1), which corresponds to w=3 (original index 1). Then the next pop would get (-1, 2), which is w=1. So the first 1 in the sample would get row 1, the next 1 would get row 2.

Which matches the sample's output.

So the code for the first sample would output 2, 1, 1, 2.

So the approach is correct.

Now, the code in Python:

We need to read n, then the list of w, then the string. Then sort the list of (w, index) tuples.

Then process each character in the string.

So code:

import heapq

n = int(input())
w_list = list(map(int, input().split()))
rows = sorted([(w, i+1) for i, w in enumerate(w_list)], key=lambda x: x[0])
s = input().strip()

output = []
current_intro = 0
heap = []

for c in s:
    if c == '0':
        w, idx = rows[current_intro]
        output.append(idx)
        heapq.heappush(heap, (-w, idx))
        current_intro += 1
    else:
        neg_w, idx = heapq.heappop(heap)
        output.append(idx)

print(' '.join(map(str, output)))

Wait, but in the first sample, after adding the first two rows (2 and 1) to the heap, the heap elements are (-1, 2) and (-3, 1). When we push into the heap, the heapq in Python maintains it as a min-heap. So the first element is the smallest. So after pushing (-1,2) and (-3, 1), the heap structure is:

The root is -3 (since it's smaller than -1). So when you pop, you get (-3, 1), which is the row with w=3. So the first '1' in the sample would output 1. The second '1' would pop (-1, 2), output 2.

Which matches the sample's output.

Yes, the code seems correct.

Testing the second sample:

Input:

6

10 8 9 11 13 5

010010011101

The sorted rows are:

5 (row 6), 8 (row2), 9 (row3), 10 (row1), 11 (row4), 13 (row5).

The passenger string is 0 1 0 0 1 0 0 1 1 1 0 1.

Processing each character:

Let's index the sorted rows as 0:5 (6), 1:8 (2), 2:9 (3), 3:10 (1), 4:11 (4), 5:13 (5).

current_intro starts at 0.

heap is empty.

Processing each character:

0: take row 0 (5,6). push (-5,6). output 6.

current_intro is 1.

1: pop the heap. Only (-5,6). output 6.

current_intro still 1.

0: take row1 (8,2). push (-8,2). output 2.

current_intro 2.

0: take row2 (9,3). push (-9,3). output3.

current_intro 3.

1: pop max from heap. The heap has (-8,2), (-9,3). The smallest is -9, so pop (-9,3). output3.

current_intro 3.

0: take row3 (10,1). push (-10,1). output1.

current_intro4.

0: take row4 (11,4). push (-11,4). output4.

current_intro5.

1: pop max. The heap has (-8,2), (-10,1), (-11,4). The smallest is -11, so pop (-11,4). output4.

1: pop next smallest, which is -10 (row1). output1.

1: pop next, which is -8 (row2). output2.

0: take row5 (13,5). push (-13,5). output5.

current_intro6 (but n is 6, so no more).

1: pop (-13,5). output5.

So the output is 6,6,2,3,3,1,4,4,1,2,5,5. Which matches the sample.

Yes, so the code works.

Now, for the code:

We need to read the input correctly, then process the string.

The code is as written above. Let's test for possible edge cases.

Edge case 1: n=1. Input:

1

5

01

The sorted rows is [(5,1)].

Passenger string is '01'.

Processing:

0: take row1. Push (-5,1). output [1].

1: pop (-5,1). output [1,1].

Which is correct.

Another edge case: all introverts first, then extroverts.

n=3.

w: 3,2,1 (so sorted order 1,2,3. row indices 3,2,1).

passenger string: '000111'.

Processing:

0: row3 → push (-1,3)

0: row2 → push (-2,2)

0: row1 → push (-3,1)

Then three 1s:

pop -3 → row1, output1.

pop -2 → row2, output2.

pop -1 → row3, output3.

So output is 3 2 1 1 2 3.

Which is correct.

So the code seems correct.
</think>

```python
import heapq

n = int(input())
w_list = list(map(int, input().split()))
rows = sorted([(w, i + 1) for i, w in enumerate(w_list)], key=lambda x: x[0])
s = input().strip()

output = []
current_intro = 0
heap = []

for c in s:
    if c == '0':
        w, idx = rows[current_intro]
        output.append(idx)
        heapq.heappush(heap, (-w, idx))
        current_intro += 1
    else:
        neg_w, idx = heapq.heappop(heap)
        output.append(idx)

print(' '.join(map(str, output)))
```