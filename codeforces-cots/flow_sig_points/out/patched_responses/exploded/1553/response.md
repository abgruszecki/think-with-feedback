<think>
Okay, let's tackle this problem. So the task is to process a line of people, each being a boy or a girl. Whenever there's at least one adjacent boy-girl pair, we need to select the pair with the minimal absolute difference in their skills. If there are multiple such pairs, pick the leftmost one. Then, remove that pair (they leave to dance), and repeat the process until no such pairs exist. The output is the order in which these pairs are removed, along with their original positions.

Hmm, the constraints are tight. The input size can be up to 2e5, so any O(n^2) approach is definitely out of the question. We need something efficient, maybe O(n log n) time.

Let's think about how the process works. Each time a pair is removed, the line closes, meaning adjacent elements become next to each other. But since the line is contiguous, removing a pair (two elements) might split the line into two parts, or connect parts around them. Wait, but the pair is adjacent. So when we remove two adjacent people, the remaining people to the left and right of the pair are now adjacent. For example, if we have A B C D and B and C are removed, then A and D become adjacent.

So each removal affects the neighboring elements. The key challenge is efficiently tracking possible pairs after each removal, and finding the minimal difference pair each time.

The naive approach would be, for each step, scan the entire current line and find all possible boy-girl adjacent pairs, compute their differences, find the minimal one, and remove them. But that's O(n) per step, leading to O(n^2) time overall. Which is way too slow for n=2e5.

So we need a data structure that can efficiently track the possible adjacent pairs, and allow us to quickly find the pair with the minimal difference, and when a pair is removed, update the adjacent relationships accordingly.

This sounds similar to a priority queue problem, where the priority is the difference (and leftmost position as a tiebreaker). But the problem is that when a pair is removed, adjacent elements are now connected, which might form new pairs. So inserting new possible pairs into the priority queue.

But how to manage this efficiently?

Another thing to note: the original positions are fixed. The numbers in the output are based on the original indices. So even when elements are removed, the indices of the remaining people remain as per their original numbering.

So the steps are:

1. Track which people are still present in the line. Initially, all are present.
2. For each possible adjacent pair, determine if it's a boy-girl pair (different genders), and compute their difference.
3. Among all such possible pairs, select the one with the smallest difference. If there are ties, choose the leftmost.
4. Remove that pair, mark them as deleted.
5. Check the neighbors of the removed pair (the elements before and after the pair) to form new adjacent pairs, and add those to the possible candidates.

But how to manage this efficiently?

The problem is that when a pair is removed, the adjacent elements (left of the pair and right of the pair) become adjacent. So for example, if the pair is at positions i and i+1, then after removal, the elements at i-1 and i+2 (if they exist) are now adjacent. So we need to check if that new adjacency forms a valid pair (boy-girl) and then track it.

So for each step, when a pair (x, x+1) is removed, we need to check if x-1 and x+2 are valid (i.e., not removed and exist), and then create the new pair (x-1, x+2) if they are adjacent.

Wait, but when we remove a pair (a, a+1), the next adjacent pair is (a-1, a+2). Because the line is continuous, after a and a+1 are removed, the line becomes ... a-1, a+2, ... so those two are now adjacent.

So the main challenge is efficiently tracking these possible pairs as they are created and removed.

But how to manage this with a priority queue?

Each time a pair is considered, it needs to be valid (both elements exist). But if either element is removed, the pair is invalid and should be ignored.

So here's an idea:

- Use a priority queue (heap) to store all possible valid pairs, ordered by their difference, then by their left index.
- Each time a pair is popped from the heap, we check if both elements are still present. If yes, process them (remove them, add to the result) and then check the neighbors to form new pairs.
- If either element is already removed, skip this pair.

But the problem is that the heap might contain old pairs that are no longer valid. For example, if a pair (i, i+1) was in the heap, but then either i or i+1 was removed by another pair's processing. So when we pop (i, i+1), we have to check if they are still present.

This approach would work, but the problem is that the heap could have O(n) elements, and each step could involve O(log n) time for heap operations. But since for each pair, when it's removed, we might add O(1) new pairs (the neighboring pairs after removal), the total number of pairs in the heap could be O(n). So the time complexity would be O(n log n), which is acceptable.

So let's outline the steps:

1. Preprocess the original array to track each person's gender and skill.
2. For each adjacent pair in the original array (i and i+1 for i from 0 to n-2), check if they are a boy-girl pair. If yes, compute their difference and add them to a priority queue. The priority is (difference, left index). But since the heap in Python is a min-heap, and we want the smallest difference first, and then the smallest left index, we can store tuples (diff, i, i+1), where i is the original left index (0-based or 1-based? Well, the original problem uses 1-based indices for output. But for processing, it's easier to work with 0-based, then adjust to 1-based in the output.)

Wait, the problem states that people are numbered from 1 to n in the input order. So the first person is 1, the next 2, etc. So when a pair (i, j) is formed (i and j are original indices, 1-based), and i < j, we need to output them in order.

So in the code, we need to process 1-based indices.

But in the code, when working with the array, perhaps 0-based is easier. Wait, maybe not. Let's see.

Hmm, perhaps we can process the original array as 0-based, but the output requires 1-based indices. So when a pair is between positions i and i+1 (0-based), their original indices are i+1 and i+2. So when adding to the heap, we need to track their original indices.

Wait, no. The original indices are fixed. For example, in the first example:

Input:

4

BGBG

4 2 4 3

The people are numbered 1,2,3,4. The first pair processed is 3 and 4 (original indices) which have a difference of 1. Then 1 and 2, which have a difference of 2.

So the original indices are fixed, regardless of the order of removal. So when a pair (i, j) is removed (i and j are original indices), their order in the output is sorted. So when adding to the priority queue, each possible pair is stored with their original indices. But pairs can only be adjacent in the current line.

Wait, but the pairs in the priority queue are adjacent in the current line. So how to track that?

This complicates things. Because when some pairs are removed, the adjacency in the original array doesn't correspond to adjacency in the current line. For example, after some elements are removed, two elements that were not originally adjacent could become adjacent.

So the adjacency is dynamic, based on the current line. So the problem is that the pairs in the priority queue are pairs of original indices that are adjacent in the current line.

So the challenge is to model the adjacency correctly.

Thus, the key data structures needed are:

- A way to track for each original index, the next and previous alive elements. So that when a pair is removed, we can find the new adjacent pairs (left and right of the removed pair) and add them to the priority queue if they form a boy-girl pair.

This suggests using a doubly linked list structure. Each node (person) has a 'prev' and 'next' pointer, indicating their current left and right neighbors in the line. When a pair is removed (i, j), we need to:

- Remove i and j from the linked list.
- Then, the previous node of i (let's call it left_node) and the next node of j (right_node) become adjacent. So we need to check if left_node and right_node form a valid pair (B and G of different types) and add them to the priority queue.

But how to efficiently manage the linked list and the priority queue?

So the plan is:

1. Initialize a doubly linked list for all the people. Each person has a 'prev' and 'next' pointer. Initially, each person's prev is i-1 and next is i+1, except for the first and last.

2. Precompute all initial adjacent pairs (i and i+1 for 0-based indices). For each such pair, check if they are boy and girl. If yes, compute their difference and add to the priority queue. The priority is (difference, left index, right index). But since the left index in the original array is i (0-based), which becomes (i+1) in 1-based. Wait, the original indices are 1-based. So for a pair (i, i+1) in 0-based (original indices i+1 and i+2 in 1-based), their left index in 1-based is i+1, which is the smaller of the two. So when added to the priority queue, the left index is i+1, and the right is i+2.

3. The priority queue is a min-heap, ordered by the difference, then the left index (smallest first). So each element in the heap is a tuple (diff, left, right), where left and right are the original 1-based indices. But wait, in the problem statement, the pair is ordered in the output as sorted, but when added to the heap, the left is the smaller index. Wait, no. The original pair could be (i, i+1), but their genders determine whether they are a valid pair. So for example, if i is B and i+1 is G, that's a valid pair regardless of order. The pair is stored with left index i (original 1-based) and right i+1. But when stored in the heap, the left and right are in their original positions.

But the priority queue is ordered first by difference, then by the left index. So for two pairs with same difference, the one with the smaller left index is processed first.

4. For each pair in the heap, when we pop it, we need to check if both are still alive (not removed). If either is removed, skip this pair. Otherwise, process them: add to the result list, mark them as removed, and then check their previous and next to form a new pair.

Wait, but the pair (left, right) in the heap may not be adjacent anymore. Because between the time they are added to the heap and when they are processed, other pairs could have been removed that affect their adjacency. So how do we ensure that the pair (left, right) is still adjacent?

This is the crux of the problem. Because the heap may contain pairs that are no longer adjacent. So when we pop a pair (left, right), we need to check not only that both are alive but that they are adjacent in the current linked list.

Wait, no. Because if the pair was added to the heap when they were adjacent, but then other pairs were processed, making them no longer adjacent. So for example, suppose the heap has a pair (A, B), which are adjacent. Then another pair (B, C) is processed, which removes B and C. Now A and D (the next of C) become adjacent. The pair (A, D) is added to the heap. The original pair (A, B) is still in the heap. But when we process (A, B), we need to check if they are adjacent and alive. But B was already removed, so the pair (A, B) is invalid.

Thus, the approach is:

- When a pair (u, v) is popped from the heap, we first check if u and v are both alive and adjacent. If not, skip this pair. If they are, process them (mark as removed), add to the result, and then check the neighboring pairs (prev of u and next of v) to see if they form a new valid pair. If so, add that to the heap.

But how to check if u and v are adjacent? Because in the linked list, each node's next and prev pointers indicate their current neighbors. So for u to be adjacent to v, u's next must be v and v's prev must be u. So during the check, we can verify that u's next is v and v's prev is u.

So the steps for processing a popped pair (u, v) would be:

1. Check if u is alive and v is alive.
2. Check if u's next is v and v's prev is u.
3. If both conditions are true, process the pair.
   a. Add (u, v) to the result list (sorted as min and max).
   b. Mark u and v as removed (alive = False).
   c. Find left_node (prev of u) and right_node (next of v).
   d. If left_node exists, update its next to right_node.
   e. If right_node exists, update its prev to left_node.
   f. If left_node and right_node exist, check if they form a boy-girl pair. If yes, compute their difference and add to the heap.

But how to represent the linked list? Let's think in terms of 1-based indices for the original positions.

Each person has a 'prev' and 'next' pointer. We can represent these as arrays. For example:

prev = [0]*(n+2)  # 1-based to n
next = [0]*(n+2)

Initially, for person i (1<=i<=n), prev[i] = i-1 if i>1 else None, and next[i] = i+1 if i <n else None.

But for handling the edges, perhaps we can use 0 to represent a non-existent prev or next. So for the first person, prev is 0, and next is 2, etc.

So when initializing:

prev = [0]*(n+2)
next = [0]*(n+2)
for i in range(1, n+1):
    prev[i] = i-1 if i >1 else 0
    next[i] = i+1 if i <n else 0

Wait, but for i=1, prev is 0, and next is 2. For i=n, next is 0.

Then, when we process a pair (u, v):

Check if next[u] == v and prev[v] == u. If yes, they are adjacent.

Once we process them, we mark them as removed (alive[u] = alive[v] = False). Then, get left_node = prev[u], right_node = next[v].

If left_node is not 0 and right_node is not 0, we need to link left_node and right_node. So set next[left_node] = right_node and prev[right_node] = left_node.

Then, check if left_node and right_node are a valid boy-girl pair. If so, compute their difference and add to the heap.

This seems manageable.

So the steps in code would be:

1. Read n, genders (as a string), and a list of a_i.

2. Initialize prev and next arrays.

3. Initialize alive array (alive[i] = True for all i initially).

4. For each initial adjacent pair (i, i+1) in 1-based indices (so i from 1 to n-1), check if genders are different. If so, compute their difference, and add to the heap as (diff, i, i+1).

5. The heap is a priority queue that pops the smallest diff, then the smallest left index.

6. Process the heap:

   a. While the heap is not empty:

      i. Pop the smallest (diff, u, v).

      ii. Check if u and v are alive and adjacent (next[u] == v and prev[v] == u). If not, skip.

      iii. If they are alive and adjacent, add the pair (min(u, v), max(u, v)) to the result list.

      iv. Mark u and v as not alive.

      v. Get left_node = prev[u], right_node = next[v].

      vi. Update next[left_node] to right_node and prev[right_node] to left_node.

      vii. If left_node and right_node are valid (non-zero), check if they form a boy-girl pair. If so, compute their difference and add (diff, left_node, right_node) to the heap.

7. After processing all possible pairs, output the result list.

Now, the key points are:

- The heap may have duplicate or invalid entries, but when popped, they are checked and skipped if invalid.

- Each time a new pair is added to the heap (like left_node and right_node after a removal), it's a possible candidate for processing.

This approach ensures that all valid pairs are considered, even those formed after previous removals.

But what about the time complexity?

Each pair can be added to the heap at most once. Because each time a pair is added, it's because they are adjacent, and once processed, their neighbors are linked and a new pair (if any) is added once.

But how many times can a pair (x, y) be added to the heap? Only once, because once x or y is removed, they are marked as not alive, so any future attempts to process (x, y) will skip them.

But wait, suppose a pair (x, y) is added to the heap, but before it's processed, another pair involving x or y is processed, making (x, y) no longer adjacent. Then, when (x, y) is popped, it's checked and skipped. So the same pair could be added multiple times if the heap is modified in such a way. But in reality, each new pair is formed only when their adjacency is created. For example, when two nodes are linked, their pair is added once.

But the maximum number of pairs added to the heap is O(n), since each pair can be added once when they are adjacent. Since each removal of a pair can add at most one new pair (the left and right neighbors), the total number of pairs is O(n). Because each removal of a pair reduces the number of elements by 2, but each removal can add at most one new pair, which may be processed later.

So the total heap operations are O(n log n), which is acceptable.

Now, the implementation details:

In Python, the heap is implemented using the heapq module. However, since Python's heapq is a min-heap, the tuples are ordered as (diff, left, right). Since we want the smallest difference first, and then the smallest left index, this ordering works.

But when a pair is added to the heap, it's stored with the left and right indices (as per their original positions). For example, if the new pair is left_node and right_node, the left index is left_node, which is smaller than right_node (since they are adjacent in the current line, which may not be the original order). Wait, not necessarily. For example, in the first example, when the pair 3 and 4 is removed, the new pair is 2 and ... wait, no. Let's see:

Original indices are 1,2,3,4. After removing 3 and4, the line becomes 1,2. So the next pair is 1 and2 (B and G, difference 2). So the new pair is (1,2).

But how is that pair added to the heap? When 3 and4 are removed, the left_node is 2 (prev of 3) and right_node is 5 (next of4), but 5 is 0 (invalid). So no new pair is added. Wait, perhaps I'm getting confused with the indices.

Let me re-examine the linked list logic.

Suppose after processing pair (3,4):

prev[3] = 2, next[3] =4.

prev[4] =3, next[4] =0.

When they are removed, alive[3] and alive[4] become False. Then, left_node is prev[u] = prev[3] =2. right_node is next[v] = next[4] =0. So right_node is 0. So we update next[left_node] (which is 2) to right_node (0), and prev[right_node] (which is 0, so nothing is done). Then, since right_node is 0, there's no new pair. So the remaining people are 1 and2. But how are they considered adjacent?

Wait, in the original setup, the next of 1 is 2, and the next of 2 is 3. After processing 3 and4, we set next[2] to next[3], which is 4. Then, after processing 3 and4, the next[2] becomes 4. But since 4 is now dead, next[2] is 4, but 4 is dead. Then, when we process the next step, the next of 2 is 4, which is dead, so when the heap processes the pair (1,2), how does that happen?

Wait, maybe I'm making a mistake in the linked list management. Let's see:

When pair (3,4) is processed:

left_node is prev[3] =2, right_node is next[4] =0.

We set next[2] =0 and prev[0] is undefined. So the next of 2 is 0, which is invalid. The remaining people are 1, 2 (alive), and 3,4 (dead). But 1's next is 2, and 2's next is 0. So the line is 1,2. Are they adjacent? Because next[1] is 2, and prev[2] is 1.

So the pair (1,2) is still adjacent, but they were added to the heap initially. But in the initial step, all adjacent pairs are added. So (1,2) was added initially if they are B and G.

In the first example, the genders are BGBG. So 1 is B, 2 is G, which is a valid pair. So (1,2) was added to the heap with a difference of 2. Then when (3,4) is processed, the heap still contains (1,2) with diff 2. So when that pair is popped next, we check if 1 and2 are alive and adjacent. Since they are, they are processed.

Thus, the linked list correctly manages the adjacency.

So the code steps are:

- For each pair in the heap, when popped, check if they are alive and adjacent.

Now, the code in Python:

We need to manage the prev and next arrays, alive array, and the heap.

But in Python, for n up to 2e5, using lists for prev and next is manageable.

Let's outline the code:

Read n.

Read the gender string (s), which is a string of 'B's and 'G's. So s[i] is the gender of the (i+1)-th person.

Read the a list as integers.

Initialize:

prev = [0]*(n+2)  # 0-based indices for people 1..n

next = [0]*(n+2)

for i in range(1, n+1):

    prev[i] = i-1 if i>1 else 0

    next[i] = i+1 if i <n else 0

alive = [False]*(n+2)  # indexes 0 and n+1 are not used

for i in range(1, n+1):

    alive[i] = True

Then, the heap is initialized with all valid adjacent pairs.

heap = []

for i in range(1, n):

    u = i

    v = i+1

    if s[u-1] != s[v-1]:  # because s is 0-based for the string

        diff = abs(a[u-1] - a[v-1])

        heapq.heappush(heap, (diff, u, v))

But wait, in the input, the third line is the a_i for each person, 1-based. So a[0] is the first person's skill, a[1] the second, etc.

So for person u (1-based), their skill is a[u-1].

Thus, the code for the initial heap is:

import heapq

n = int(input())

s = input().strip()

a = list(map(int, input().split()))

prev = [0]*(n+2)

next_ = [0]*(n+2)  # next is a keyword in Python, so use next_

for i in range(1, n+1):

    prev[i] = i-1 if i > 1 else 0

    next_[i] = i+1 if i < n else 0

alive = [False]*(n+2)

for i in range(1, n+1):

    alive[i] = True

heap = []

for i in range(1, n):

    u = i

    v = i + 1

    if s[u-1] != s[v-1]:

        diff = abs(a[u-1] - a[v-1])

        heapq.heappush(heap, (diff, u, v))

result = []

while heap:

    diff, u, v = heapq.heappop(heap)

    # Check if u and v are alive and adjacent

    if not (alive[u] and alive[v]):

        continue

    if next_[u] != v or prev[v] != u:

        continue

    # They are a valid pair

    result.append( (min(u, v), max(u, v)) )

    # Mark them as not alive

    alive[u] = False

    alive[v] = False

    # Get left and right nodes

    left_node = prev[u]

    right_node = next_[v]

    # Update the links

    if left_node != 0:

        next_[left_node] = right_node

    if right_node != 0:

        prev[right_node] = left_node

    # Check if left_node and right_node form a valid pair

    if left_node !=0 and right_node !=0:

        if s[left_node-1] != s[right_node-1]:

            new_diff = abs(a[left_node-1] - a[right_node-1])

            heapq.heappush(heap, (new_diff, left_node, right_node))

print(len(result))

for pair in result:

    print(pair[0], pair[1])

Wait, but this code may have an issue. Because after removing u and v, the new pair is left_node and right_node. But their adjacency is now direct (since the links are updated), so their next and prev pointers are set correctly.

But when we add left_node and right_node to the heap, it's possible that they were added before, but that's okay. Because when the pair is popped again, it's checked whether they are alive and adjacent.

But since they are now adjacent, and alive (since they are part of the linked list), the check will pass only if they are alive and adjacent.

But what if left_node and right_node are not adjacent in the original array but are now adjacent after some removals?

Yes, that's possible. But since the code uses the linked list to track their adjacency, the check during processing will correctly verify if they are adjacent.

This code should handle all cases.

Testing this code against the examples:

First example:

Input:

4

BGBG

4 2 4 3

Initial pairs:

1-2: B vs G → valid. diff is |4-2|=2.

2-3: G vs B → valid. |2-4|=2.

3-4: B vs G → valid. |4-3|=1.

So the heap contains (2,1,2), (2,2,3), (1,3,4). Ordered as 1 (3,4), then 2 (1,2), then 2 (2,3).

Processing the heap:

The first popped is (1,3,4). Check if 3 and4 are alive and adjacent. They are. Process them. Add (3,4) to result. Mark them as dead. left_node is prev[3] =2, right_node is next[4]=0. So next[2] is set to 0. prev[0] is not set. Then check left_node (2) and right_node (0) → no new pair.

The heap now has (2,1,2) and (2,2,3).

Next popped is (2,1,2). Check if alive and adjacent. 1's next is 2, 2's prev is 1. So yes. Process. Add (1,2) to result. Mark them as dead. left_node is prev[1] =0, right_node is next[2]=3 (but 3 is dead). So next[0] is 3 (but 0 is not a valid node). So no new pair added.

The heap now has (2,2,3), but when popped, check if 2 and3 are alive. 2 is now dead (processed in previous step). So the pair is skipped. So the result is 2 pairs, which matches the example.

Second example:

Input:

4

BBGG

4 6 1 5

The genders are B B G G.

Initial pairs:

1-2: B B → invalid.

2-3: B G → valid. |6-1|=5.

3-4: G G → invalid.

So the initial heap has (5,2,3).

Another pairs may be added during processing.

Processing:

First popped (5,2,3). Check if 2 and3 are alive and adjacent. They are. Process them. Add (2,3) to result. Mark them as dead. left_node is 1, right_node is4. Now, 1's next is4, 4's prev is1. Check if they are B and G (s[0] is B, s[3] is G). So valid. Compute |4-5|=1. Add (1,4) to heap.

Next popped is (1,1,4). Check if 1 and4 are alive and adjacent. 1's next is4, and 4's prev is1. So yes. Process. Add (1,4) to result. Now, left_node is prev[1] =0, right_node is next[4] =0. No new pair.

So the output is 2 pairs: 2 3 and 1 4, which matches the example.

Third example:

Input:

4

BGBB

1 1 2 3

Genders: B G B B.

Initial pairs:

1-2: B G → valid. diff 0.

2-3: G B → valid. |1-2|=1.

3-4: B B → invalid.

So the heap has (0,1,2), (1,2,3).

Processing:

First popped is (0,1,2). Check if alive and adjacent. Yes. Process. Add (1,2) to result. Mark them as dead. left_node is 0, right_node is3. No new pair (left_node is 0). Heap now has (1,2,3).

Next popped (1,2,3). Check if 2 and3 are alive. 2 is dead. So skip. No more pairs.

So the result is 1 pair. Which matches the example.

Thus, the code seems correct.

Now, considering the constraints. The code uses O(n) space for prev, next, alive. The heap can have O(n) elements. For n=2e5, this is manageable.

In Python, using heapq for 2e5 elements is feasible. The heappush and heappop operations are O(log n), which for 2e5 elements is acceptable.

Thus, the code should work within the time and memory constraints.
</think>

```python
import heapq

n = int(input())
s = input().strip()
a = list(map(int, input().split()))

prev = [0] * (n + 2)
next_ = [0] * (n + 2)

for i in range(1, n+1):
    prev[i] = i-1 if i > 1 else 0
    next_[i] = i+1 if i < n else 0

alive = [False] * (n + 2)
for i in range(1, n+1):
    alive[i] = True

heap = []
for i in range(1, n):
    u = i
    v = i + 1
    if s[u-1] != s[v-1]:
        diff = abs(a[u-1] - a[v-1])
        heapq.heappush(heap, (diff, u, v))

result = []

while heap:
    diff, u, v = heapq.heappop(heap)
    if not (alive[u] and alive[v]):
        continue
    if next_[u] != v or prev[v] != u:
        continue
    result.append((min(u, v), max(u, v)))
    alive[u] = False
    alive[v] = False
    
    left_node = prev[u]
    right_node = next_[v]
    
    if left_node != 0:
        next_[left_node] = right_node
    if right_node != 0:
        prev[right_node] = left_node
    
    if left_node != 0 and right_node != 0:
        if s[left_node - 1] != s[right_node - 1]:
            new_diff = abs(a[left_node - 1] - a[right_node - 1])
            heapq.heappush(heap, (new_diff, left_node, right_node))

print(len(result))
for pair in result:
    print(pair[0], pair[1])
```