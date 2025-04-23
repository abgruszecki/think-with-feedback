<think>
Okay, let's try to solve this problem. The task is to determine how many operations Vasya needs to perform to empty the array. Each operation involves removing the longest consecutive segment (leftmost if there are ties). 

First, let's understand the problem with the examples. Like in the first example, the array is [2,5,5,2]. The first step is to remove the two 5s because they form the longest consecutive segment (length 2, but maybe the leftmost? Wait, wait. Wait, in the first example, the segments are [2], [5,5], [2]. So the longest is the [5,5] and [2,2] in the next step. So after removing the 5s, the array becomes [2,2], which is then removed in the second operation. So total 2 steps.

Another example: the fourth input is [10,10,50,10,50,50]. The first operation removes the first two 10s. Then the array becomes [50,10,50,50]. Next, the longest consecutive is the last two 50s. Wait, but according to the note, after removing the first two 10s, the array is [50,10,50,50]. Then the longest consecutive is the two 50s at the end. So in the second operation, they are removed, leaving [50,10]. Then the next longest is the single 50 (since the segment [50] is the leftmost longest). So third operation removes 50, leaving [10], which is then removed in the fourth step. So total 4 steps.

Hmm. So the key is that in each step, we find the leftmost longest consecutive segment and remove it. Then the array is modified, and the process repeats until empty.

The problem is to compute the number of such steps required.

Now, considering the constraints: n can be up to 200,000. So any O(n^2) approach is definitely going to be too slow. We need an O(n) or O(n log n) solution.

So the challenge is to model the process efficiently. Let's think about how the array is modified after each step. Each removal splits the array into parts, but we need to track the segments that are formed after each removal. 

Wait, but each removal operation can split the array into parts. For example, if we have a segment in the middle of the array being removed, then the left and right parts become separate. However, if those left and right parts have the same value, they might merge into a single consecutive segment in subsequent steps. But this merging only happens if they are adjacent after the removal. So, for example, if we remove a middle segment, the left and right parts are now adjacent. If their values are the same, they form a new consecutive segment.

So the problem requires tracking the current segments in the array, and after each removal, potentially merging adjacent segments if their values are the same.

But how do we model this efficiently?

Alternative approach: Perhaps the process can be represented as a sequence of segments, with their positions and lengths, and each time when a segment is removed, we check the neighbors to see if they can be merged. This seems similar to a doubly linked list structure where each node represents a segment. Each node would contain the value, the length of the segment, and pointers to the previous and next nodes. 

But even with this structure, the problem is to find the leftmost longest segment each time. So for each step, we need to find the segment with the maximum length, and in case of ties, the leftmost one. Then, after removing that segment, we need to check if the previous and next segments (if they exist) have the same value. If so, merge them into a new segment.

Wait, but how do we efficiently find the leftmost maximum-length segment each time?

This seems tricky. Because each time after a removal and possible merge, the segments change, and we need to track the maximum length again. 

So perhaps, the data structure needed is a priority queue (heap) that keeps track of the segments ordered by their length (descending) and position (ascending). But the problem is that when a segment is merged, we need to remove the old segments from the heap and add the new merged one. However, standard heaps in Python (the heapq module) don't support efficient deletion of arbitrary elements. So this approach may not be feasible for large n, as each merge could involve multiple heap operations which may not be efficient enough.

Alternatively, maybe we can model the process by grouping consecutive elements into runs (like Run-Length Encoding) first. Then, the initial list is a list of runs. For example, the array [10,10,50,10,50,50] becomes [(10, 2), (50,1), (10,1), (50,2)]. Then, each time we select the leftmost longest run. But wait, the problem says to select the longest consecutive segment. So in the initial array, the runs are the consecutive elements. So when selecting the longest segment, the leftmost run with maximum length. So in the first step, the leftmost run with maximum length is the first run (10,2). But wait, in the fourth example, the first run is 2, the second is 1, third 1, fourth 2. So the maximum length is 2. The leftmost is the first run, so we remove it. Then, after removing that run, the array becomes the remaining runs: [50,1, 10,1, 50,2]. Then, after that, the next longest is the fourth run (length 2). So that's the leftmost with maximum length. So we remove that run, leaving [50,1, 10,1]. Then the longest is 1. The leftmost is the first run (50,1), which is removed. Then the next step removes the 10,1. Then the 50,1? Wait, perhaps the example's note explains better.

Wait, in the fourth example:

Original array is [10,10,50,10,50,50]. The runs are:

10 (2), 50 (1), 10 (1), 50 (2).

First step removes the first run (length 2). The array becomes [50,10,50,50]. Which is runs 50 (1), 10 (1), 50 (2). The next step's longest is 2. The leftmost run with that length is the third run (50,2). So removing it leaves [50,10]. Now the runs are 50 (1), 10 (1). Next step, the longest is 1, leftmost is the first run. Remove it, leaving [10]. Then remove that. So total steps: 4.

So, the process is:

Each step, select the leftmost run with the maximum length. Then remove that run. Then check if the previous and next runs (after removal) are present and have the same value. If so, merge them into a single run.

Wait, but in the step where a run is removed, the previous and next runs (if any) are now adjacent. For example, if we have runs A, B, C. We remove B. Then A and C are now adjacent. If A and C's values are equal, they merge into a new run with length A.length + C.length.

So, the key is that when a run is removed, we need to check the adjacent runs and possibly merge them. This affects the available runs for the next steps.

But how do we model this efficiently?

So the initial approach is:

1. Preprocess the array into a list of runs (value and length). For example, the array [2,5,5,2] becomes [(2,1), (5,2), (2,1)].

2. Each run is represented as an object or a data structure that can be quickly accessed, modified, and removed.

3. Use a priority queue (max heap) that keeps track of the runs, ordered by their length (descending) and their position (ascending, to break ties for leftmost).

4. For each step:
   a. Extract the run with maximum length and leftmost position.
   b. Remove this run from the data structure.
   c. Check the previous and next runs (if any) of the removed run. If their values are equal, merge them into a single run.
   d. Update the priority queue with any new runs created from merging.
   e. Increment the operation count.

But the problem is how to efficiently manage the priority queue when elements are merged. Because when a run is removed, its previous and next may be merged into a new run, which needs to be added to the heap, and the old previous and next runs need to be marked as invalid (since they are no longer in the data structure).

This is tricky because the heap may contain old entries (for runs that have been merged and thus are invalid). So when we extract a run from the heap, we need to check if it's still active. If not, we skip it.

This approach can work but might be efficient enough if the number of such invalid entries in the heap is manageable.

So, here's the plan:

- Represent each run with a unique identifier (like a pointer or a node in a linked list). But since Python doesn't have pointers, perhaps use a class with references to previous and next runs.

- Each run has a 'deleted' flag. When a run is merged into another, it's marked as deleted. So when we pop from the heap, we check if the run is still active. If not, we ignore it.

- The heap entries are tuples (-length, position, run_id), so that the largest length and smallest position are popped first.

So, the steps:

1. Preprocess the array into runs, each with their length, value, and a unique id.

2. Create a doubly linked list of these runs, so that each run knows its previous and next.

3. For each run, add it to the priority queue (heap).

4. Initialize the operation count to 0.

5. While the heap is not empty:

   a. Pop the top element (max length, leftmost). Check if the run is active (not deleted). If it's deleted, skip this element.

   b. If active, process it: increment operation count.

   c. Check the previous and next runs of the current run (before removal). Because when the current run is removed, the previous and next are now adjacent.

   d. Remove the current run from the linked list. Mark it as deleted.

   e. If previous and next exist and have the same value, merge them into a new run. Create a new run with value equal to theirs, length sum. The new run's previous is previous's previous, and next is next's next. Update the linked list accordingly. Then, add this new run to the heap and mark the previous and next as deleted.

6. Repeat until all runs are processed.

But how to track the position to break ties for leftmost? Because when runs are merged, their position in the original array is no longer contiguous. For example, merging two runs would create a new run that's in the position where the first run was. But for tie-breaking, the leftmost run is the one that comes earliest in the array. So the position of a run is the starting index of the original array where that run begins. But when runs are merged, the new run's starting position is the starting position of the earliest run in the merged runs.

Wait, but when runs are merged, the original array positions are not tracked. For example, after merging two adjacent runs, the new run's starting index is the same as the first merged run's starting index.

But perhaps, for the purposes of tie-breaking, the 'position' in the heap is the starting index in the original array. So, when two runs are merged, the new run's starting index is the earliest of the two merged runs. That way, in the heap, if two runs have the same length, the one with the smaller starting index is considered leftmost.

This way, when merging runs, the new run's starting index is the starting index of the leftmost run in the original array.

So, each run has a 'start' and 'end' index in the original array. But perhaps we can track just the start index. For example, when merging run A (start a, end b) and run B (start b+1, end c), the merged run's start is a, end c. So the start is a, which is the smaller of the two starts.

So the position used in the heap is the start index of the run. That way, when two runs have the same length, the one with the smaller start index (i.e., leftmost) is selected.

Therefore, in the priority queue, each entry is (-length, start, run_id). So the heap is a max-heap based on the length (since Python's heapq is a min-heap, we store the negative length). The start is used as the tie-breaker for runs of the same length.

This seems manageable.

Now, the challenge is to implement this efficiently in Python, given the constraints. Let's outline the steps:

1. Preprocess the input array into a list of runs. For each run, we track the start index, value, length, and unique id. For example, the array [10,10,50,10,50,50] is converted into runs:

   Run 0: start 0, value 10, length 2.

   Run 1: start 2, value 50, length 1.

   Run 2: start 3, value 10, length 1.

   Run 3: start 4, value 50, length 2.

   So the runs are stored as a list of objects. Each run also has prev and next pointers (indices into the runs list, or None if not present).

Wait, but the linked list of runs can't use indices if runs are added and removed dynamically. So perhaps we need to manage a linked list structure with each run having a prev and next reference. For example, each run is a node with:

- start: the original start index

- value: the value of the run

- length: the length of the run

- prev: reference to previous node (or None)

- next: reference to next node (or None)

- deleted: a flag indicating if the node is deleted.

So, for the initial list of runs, each node's prev and next are set appropriately.

Then, for each run, we add it to the heap with (-length, start, run's id).

Now, during processing:

When we pop a run from the heap, we check if it's deleted. If so, skip. Otherwise, process it.

Processing involves:

- Remove the run from the linked list. So, set the prev's next to the next's prev, and vice versa. 

- Check if prev and next exist and have the same value. If so, merge them.

Merging prev and next:

- Create a new run with value equal to prev.value (same as next.value), length prev.length + next.length, and start equal to prev.start.

- Update the linked list: the new run's prev is prev.prev, and next is next.next.

- Mark prev and next as deleted.

- Add the new run to the heap.

But in Python, how to represent the nodes? Since Python allows objects to have attributes, perhaps create a class for the runs.

But given the high n (up to 2e5), using classes may have some overhead, but perhaps manageable.

So, the steps in code:

1. Read the input array.

2. Preprocess into runs.

   For example:

   a = list of elements.

   runs = []

   current_val = a[0]

   current_length = 1

   start = 0

   for i in range(1, n):

       if a[i] == current_val:

           current_length +=1

       else:

           runs.append( Run(start, current_val, current_length) )

           current_val = a[i]

           start = i

           current_length =1

   runs.append( Run(start, current_val, current_length) )

3. Then, build the linked list for the runs. For each run in the list, set prev and next.

   For i in 0 to len(runs)-1:

       runs[i].prev = runs[i-1] if i>0 else None

       runs[i].next = runs[i+1] if i < len(runs)-1 else None

4. Then, create a priority queue (heap) containing each run's (-length, start, id). Wait, but how to track the id? Since each run is a unique object, perhaps use a unique identifier for each run, like an id assigned when the run is created.

Alternatively, since in Python, objects are hashable, but perhaps using a unique id is better. So when creating a run, assign a unique id (like a counter). Then, the heap entries are tuples of (-length, start, id). This allows us to check if the run has been deleted (since when a run is merged, it's marked as deleted, and even if it's still in the heap, when popped, the code can check if it's active or not).

But how to track which runs are active? Each run would have a 'deleted' attribute. So when a run is merged, we set deleted = True for the previous and next runs, and create a new run.

So, the steps during processing:

- The heap is initialized with all the initial runs.

- While the heap is not empty:

   - Pop the top element (smallest tuple, which corresponds to the largest length and leftmost start).

   - Get the run by id. If the run is deleted, skip.

   - If not deleted, process this run:

      - Increment the operation count.

      - Check the previous and next runs of this run.

      - Remove the current run from the linked list:

          prev_run = current_run.prev

          next_run = current_run.next

          current_run.deleted = True

          # Update prev and next's links

          if prev_run:

              prev_run.next = next_run

          if next_run:

              next_run.prev = prev_run

      - Check if prev_run and next_run exist and prev_run.value == next_run.value:

          # Merge them into a new run.

          new_run = Run(start=prev_run.start, value=prev_run.value, length=prev_run.length + next_run.length)

          new_run.prev = prev_run.prev

          new_run.next = next_run.next

          # Update the new_run's prev and next's links

          if new_run.prev:

              new_run.prev.next = new_run

          if new_run.next:

              new_run.next.prev = new_run

          # Mark prev_run and next_run as deleted.

          prev_run.deleted = True

          next_run.deleted = True

          # Add the new_run to the heap.

          heapq.heappush(heap, (-new_run.length, new_run.start, new_run.id))

So, in code, each run is a class instance with attributes: start, value, length, prev, next, deleted, id.

But in Python, handling a lot of objects (up to 2e5) is manageable, but the merging steps could add more runs. However, each merge reduces the number of runs by 1 (since two are merged into one), so the total number of runs added via merging is O(n), so the overall number of runs is O(n). So the heap can have O(n) entries.

But the problem is that the heap may have O(n) entries, but each merge adds a new entry. So the heap size could be up to O(n) in the worst case.

In the worst case, each operation adds a new run to the heap. For example, in the case where no merges are possible after any removal, then each removal is a single run, and no new runs are added. So the heap size is O(n).

But with the check for deleted runs when popping, the algorithm would process the heap entries, but some of them may be marked as deleted and skipped.

The key is that each run is pushed to the heap once. But when merged, the original runs are marked as deleted, so their entries in the heap are ignored.

The time complexity would depend on the number of operations (steps) and the number of heap operations. Each step requires popping from the heap until a valid run is found (O(1) per step if no invalid entries are present, but in the worst case, each step could pop O(k) entries where k is the number of invalid entries). So the worst case could be O(n log n) if the number of invalid entries is manageable.

But considering that each run is processed once (either as part of the initial runs or merged into a new run), and each merged run is created once, the total number of heap operations is O(n), leading to O(n log n) time overall.

So, the algorithm should be efficient enough for n up to 2e5.

Now, the code in Python:

But wait, in Python, using a class for the runs and maintaining a linked list with prev and next pointers could be a bit slow for 2e5 elements. So perhaps, a more optimized approach is needed.

Alternatively, can we model the problem using a list of runs, each represented as a tuple, and track their positions, and for each removal, track the current runs and their possible merges.

But that's not straightforward.

Another idea: since each step removes a segment, and the subsequent merges can affect the next steps, perhaps the process can be simulated using a priority queue where each entry is a run's start and length, and when a merge occurs, the old runs are marked as invalid and a new run is added.

But the challenge is to manage the runs' positions and their merging efficiently.

Alternatively, perhaps the problem can be viewed as a greedy approach, where the order of removals is determined by the leftmost longest runs, but the merging steps can affect the order.

But perhaps there's a way to model the entire process using a union-find (disjoint set) data structure, but I'm not sure.

Wait, perhaps we can model the runs as a list, and when a run is removed, check its neighbors and merge them if possible, then update the list. But this would involve splitting and merging the list, which could be done with a linked list. However, for large n, this would be O(n) time per operation, leading to O(n^2) time in the worst case, which is not feasible.

So back to the initial idea of using a heap with a linked list.

Now, the code structure in Python:

First, create a class for the runs:

class Run:
    def __init__(self, start, value, length, run_id):
        self.start = start
        self.value = value
        self.length = length
        self.prev = None
        self.next = None
        self.deleted = False
        self.run_id = run_id

But in Python, assigning unique IDs can be done with a counter.

Then, preprocess the array into runs.

Then, build the linked list.

Then, push all runs into the heap as (-length, start, run_id).

Then, process the heap:

count = 0

heap = [ ... ]

import heapq

heapq.heapify(heap)

id_to_run = { ... }  # maps run_id to the Run object.

But in Python, since each Run object has a run_id, the id_to_run can be a dictionary that is built during preprocessing.

Wait, but when a new run is created during merging, we need to assign it a unique id.

So, during preprocessing, we assign each initial run a unique id. Then, whenever a new run is created (due to merging), we assign a new unique id.

So, in code:

current_id = 0

runs = []

prev_run = None

for ... in ...:

    run = Run(start, value, length, current_id)

    runs.append(run)

    current_id +=1

Then, for merging:

when creating a new run, assign it current_id, then current_id +=1.

So, the code can be structured as follows.

But for the heap, each time a new run is created (due to merging), we push it into the heap.

Now, during processing:

Testing against sample input 1.

```python
import heapq


class Run:
    _id = 0  # class variable to track the next id

    def __init__(self, start, value, length):
        self.run_id = Run._id
        Run._id +=1
        self.start = start
        self.value = value
        self.length = length
        self.prev = None
        self.next = None
        self.deleted = False

def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    if n ==0:
        print(0, file=output_stream)
        return
    # Preprocess into runs
    runs = []
    current_val = a[0]
    current_length =1
    start =0
    for i in range(1, n):
        if a[i] == current_val:
            current_length +=1
        else:
            runs.append(Run(start, current_val, current_length))
            current_val = a[i]
            current_length =1
            start =i
    runs.append(Run(start, current_val, current_length))
    # Build linked list
    for i in range(len(runs)):
        if i >0:
            runs[i].prev = runs[i-1]
        if i < len(runs)-1:
            runs[i].next = runs[i+1]
    # Create heap and id_to_run map
    heap = []
    id_to_run = {}
    for run in runs:
        heapq.heappush(heap, (-run.length, run.start, run.run_id))
        id_to_run[run.run_id] = run
    count =0
    while heap:
        neg_len, start_pos, run_id = heapq.heappop(heap)
        current_run = id_to_run.get(run_id)
        if not current_run or current_run.deleted:
            continue
        # Process this run
        count +=1
        prev_run = current_run.prev
        next_run = current_run.next
        # Mark current run as deleted
        current_run.deleted = True
        # Update prev and next links
        if prev_run:
            prev_run.next = next_run
        if next_run:
            next_run.prev = prev_run
        # Check if prev and next can be merged
        if prev_run and next_run and prev_run.value == next_run.value:
            # Create new merged run
            new_run = Run(prev_run.start, prev_run.value, prev_run.length + next_run.length)
            # Set new_run's prev and next
            new_run.prev = prev_run.prev
            new_run.next = next_run.next
            # Update new_run's prev's next and next's prev
            if new_run.prev:
                new_run.prev.next = new_run
            if new_run.next:
                new_run.next.prev = new_run
            # Mark prev_run and next_run as deleted
            prev_run.deleted = True
            next_run.deleted = True
            # Add new_run to heap and id_to_run
            heapq.heappush(heap, (-new_run.length, new_run.start, new_run.run_id))
            id_to_run[new_run.run_id] = new_run
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
6 3 4 1 5
""",
            "output": \
"""\
5
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

Testing against sample input 3.

```python
import heapq


class Run:
    _id = 0  # class variable to track the next id

    def __init__(self, start, value, length):
        self.run_id = Run._id
        Run._id +=1
        self.start = start
        self.value = value
        self.length = length
        self.prev = None
        self.next = None
        self.deleted = False

def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    if n ==0:
        print(0, file=output_stream)
        return
    # Preprocess into runs
    runs = []
    current_val = a[0]
    current_length =1
    start =0
    for i in range(1, n):
        if a[i] == current_val:
            current_length +=1
        else:
            runs.append(Run(start, current_val, current_length))
            current_val = a[i]
            current_length =1
            start =i
    runs.append(Run(start, current_val, current_length))
    # Build linked list
    for i in range(len(runs)):
        if i >0:
            runs[i].prev = runs[i-1]
        if i < len(runs)-1:
            runs[i].next = runs[i+1]
    # Create heap and id_to_run map
    heap = []
    id_to_run = {}
    for run in runs:
        heapq.heappush(heap, (-run.length, run.start, run.run_id))
        id_to_run[run.run_id] = run
    count =0
    while heap:
        neg_len, start_pos, run_id = heapq.heappop(heap)
        current_run = id_to_run.get(run_id)
        if not current_run or current_run.deleted:
            continue
        # Process this run
        count +=1
        prev_run = current_run.prev
        next_run = current_run.next
        # Mark current run as deleted
        current_run.deleted = True
        # Update prev and next links
        if prev_run:
            prev_run.next = next_run
        if next_run:
            next_run.prev = prev_run
        # Check if prev and next can be merged
        if prev_run and next_run and prev_run.value == next_run.value:
            # Create new merged run
            new_run = Run(prev_run.start, prev_run.value, prev_run.length + next_run.length)
            # Set new_run's prev and next
            new_run.prev = prev_run.prev
            new_run.next = next_run.next
            # Update new_run's prev's next and next's prev
            if new_run.prev:
                new_run.prev.next = new_run
            if new_run.next:
                new_run.next.prev = new_run
            # Mark prev_run and next_run as deleted
            prev_run.deleted = True
            next_run.deleted = True
            # Add new_run to heap and id_to_run
            heapq.heappush(heap, (-new_run.length, new_run.start, new_run.run_id))
            id_to_run[new_run.run_id] = new_run
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
10 10 50 10 50 50
""",
            "output": \
"""\
4
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

So the code seems to handle these cases.

Now, considering the time and memory constraints.

The maximum number of runs is O(n) (each element is part of a run). The initial preprocessing is O(n).

The heap operations are O(n log n) since each run is added once, and each merge adds a new run. Each heap push is O(log n), and each pop is O(1) (amortized), but with possible pops of invalid entries.

In the worst case, each run is processed once, leading to O(n log n) time.

Memory-wise, each run has a few attributes. For 2e5 runs, this is manageable.

So the code should pass the constraints.

Now, the code may need some optimization. For example, using a class variable for the run ID counter. Also, ensuring that the linked list operations are handled correctly.

Another possible issue is that when merging runs, the new run's prev and next may be other runs that are already in the heap. But since those runs are part of the linked list, their next and prev are updated correctly.

Thus, the code should work.
</think>

```python
import sys
import heapq

class Run:
    _id = 0  # Class variable to generate unique IDs

    def __init__(self, start, value, length):
        self.run_id = Run._id
        Run._id += 1
        self.start = start
        self.value = value
        self.length = length
        self.prev = None
        self.next = None
        self.deleted = False

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    if n == 0:
        print(0)
        return
    a = list(map(int, input[1:n+1]))
    
    # Preprocess into runs
    runs = []
    current_val = a[0]
    current_length = 1
    start = 0
    for i in range(1, n):
        if a[i] == current_val:
            current_length += 1
        else:
            runs.append(Run(start, current_val, current_length))
            current_val = a[i]
            current_length = 1
            start = i
    runs.append(Run(start, current_val, current_length))
    
    # Build linked list
    for i in range(len(runs)):
        if i > 0:
            runs[i].prev = runs[i-1]
        if i < len(runs)-1:
            runs[i].next = runs[i+1]
    
    # Initialize heap and id_to_run map
    heap = []
    id_to_run = {}
    for run in runs:
        heapq.heappush(heap, (-run.length, run.start, run.run_id))
        id_to_run[run.run_id] = run
    
    count = 0
    while heap:
        neg_len, start_pos, run_id = heapq.heappop(heap)
        current_run = id_to_run.get(run_id)
        if not current_run or current_run.deleted:
            continue
        count += 1
        prev_run = current_run.prev
        next_run = current_run.next
        
        # Mark current run as deleted and update linked list pointers
        current_run.deleted = True
        if prev_run:
            prev_run.next = next_run
        if next_run:
            next_run.prev = prev_run
        
        # Check if previous and next can be merged
        if prev_run and next_run and prev_run.value == next_run.value:
            # Create new merged run
            new_run = Run(prev_run.start, prev_run.value, prev_run.length + next_run.length)
            new_run.prev = prev_run.prev
            new_run.next = next_run.next
            
            # Update new_run's neighbors
            if new_run.prev:
                new_run.prev.next = new_run
            if new_run.next:
                new_run.next.prev = new_run
            
            # Mark old runs as deleted and add new_run to heap
            prev_run.deleted = True
            next_run.deleted = True
            heapq.heappush(heap, (-new_run.length, new_run.start, new_run.run_id))
            id_to_run[new_run.run_id] = new_run
    
    print(count)

if __name__ == "__main__":
    main()
```
