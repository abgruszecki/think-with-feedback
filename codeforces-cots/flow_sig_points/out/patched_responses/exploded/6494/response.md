<think>
Okay, let's tackle this problem. Hmm, the problem is about ants moving on a grid according to certain rules. We need to find out how many ants end up at each queried position after all possible movements have happened. 

So the process is that every minute, any junction with at least four ants will have four ants leave, one in each direction. The remaining ants stay. This repeats until no junction has four or more ants. Then, we answer the queries.

The key here is to model the process efficiently. But given that the input n can be up to 30,000 and t up to 50,000, we can't simulate each step directly. That's way too slow. So we need a smarter approach.

Let me think about the properties here. Each time a node has enough ants (>=4), it splits four of them to the neighbors. But each split reduces the number of ants at the current node by four. So maybe we can model this in a way that tracks how many times each position contributes to its neighbors based on the number of splits it underwent.

Wait, maybe this is similar to BFS but in a way where each split propagates ants to adjacent cells. But how to compute the final counts without processing every possible split step by step.

Another idea: each split operation on a cell (x,y) contributes one ant to each of the four neighbors. But the splits can happen multiple times. So for a cell, if it splits k times, then each neighbor gets k ants. But the splits can be influenced by the splits of neighboring cells as well.

Wait, but the order in which splits happen might matter. For example, a split in (x,y) will add ants to (x+1,y), which might then split if those ants plus others reach four. So the problem is dynamic and depends on the order of processing splits.

But simulating this step by step is going to be O(number of splits), which could be very large. For n=30,000, even if each split generates four ants, the number of splits could be up to 30,000 /4, but then each of those splits adds ants to four positions, which might in turn split again, leading to a chain reaction. So the total number of splits could be O(n), but perhaps not. Wait, but each split removes four ants from a cell and adds four ants (total) to other cells, but those ants are added one per cell. So each split produces four ants in total, but each new ant is in a different cell. So the total number of ants in the system remains the same as the initial n. Because each split takes four ants and redistributes them as four. So the sum remains n.

But the problem is that the same cell can split multiple times. For example, after splitting once, maybe it accumulates enough ants again to split again. So the order in which splits are processed affects whether the same cell can split again.

Hmm, this complicates things. So how can we model this?

Alternative approach: model the problem as a BFS where each cell's splits are processed, and the ants are distributed. But this seems tricky because the splits can cascade. But perhaps we can model the splits in a breadth-first manner, processing cells in the order they reach a state where they have enough ants to split again.

Wait, maybe this is similar to a level order processing. For example, a cell (x,y) splits, which adds ants to neighboring cells. Each of those neighbors may accumulate enough ants to split once, but only after handling the current split.

But how to model this efficiently. Let's think of each split as generating a "wave" of ants. Each split from a cell contributes to its neighbors, which might then split in subsequent steps.

Alternatively, perhaps the number of splits a cell (x,y) can undergo is determined by the initial number of ants, and the splits of the cells that can contribute to (x,y). But this seems circular.

Wait, perhaps each cell can be processed in a certain order, and once processed, we can calculate how many times it splits, and how that affects its neighbors. For example, if a cell (x,y) has k splits, then each neighbor gets k ants. But then those neighbors' splits depend on their own initial ants plus the ants contributed by their neighbors.

Wait, but this could be modeled as a system where each cell's split count is determined by the total ants it receives, including from its own initial ants and the contributions from adjacent cells. But how?

Alternatively, perhaps the process can be viewed as each cell (x,y) having a certain number of ants that are processed in such a way that whenever the total ants in the cell is >=4, it splits once, subtracting 4 and adding 1 to each neighbor. But this process continues until all cells have <4 ants. The problem is to compute how many ants each cell ends up with.

But simulating this step by step would be O(n) steps, which for n=3e4 and t=5e4 might be manageable if the steps are optimized. But even then, for each split, we have to check the neighbors, which could be expensive.

Wait, but the maximum possible splits a single cell can have is (initial_ants) //4, but perhaps this is not the case. For example, a cell starts with 5 ants. Then, it splits once (5-4=1 left), which adds 1 to each neighbor. Then, the 1 ant remains. So no further splits. So for initial_ants =5, splits are 1.

If initial_ants is 6, then splits once (6-4=2), but the 2 left can't split again. So splits count is 1.

If initial_ants is 8: 8-4=4, split again (another 4 subtracted). So splits count is 2. So for initial_ants, the number of splits is floor((initial_ants - s)/4), where s is the number of splits. Wait, that's recursive. Hmm, maybe the total splits for a cell with initial_ants a is floor(a /4) + floor( (a - 4*floor(a/4))/4 ) ... no, that's not right. Wait, maybe once a cell splits once, it has a-4 ants. If after that, it's still >=4, it will split again. So the total number of splits is a//4? No, because after each split, the count decreases by 4. For example, a=5: splits once. a=8: 8//4=2 splits. Yes. So the maximum splits a cell can have is (a //4) + (a mod4)//4? Wait, no. Wait, a=7: first split leaves 3, so only one split. a=8: two splits. So the total splits is a //4 when a is a multiple of 4. Otherwise, a//4.

Wait, no. For a=4: splits once, leaves 0. So split count is 1. a=5: 5//4=1. So split once. a=7: 7//4=1. So split once. So the split count for a cell with initial ants a is a //4? No, because for a=4, split count is 1, which is 4//4=1. For a=5, 5//4=1. Yes. For a=8, 8//4=2. So that seems correct.

But how does the split count get influenced by ants coming from neighboring splits?

Ah, this is the crux of the problem. Because when a cell (x,y) splits, it sends one ant to each neighbor. Those neighbors may then have their total ants increased, leading them to split, which in turn send more ants. So the split count of a cell depends on the ants it receives from neighboring splits. So the split counts are interdependent.

This makes the problem tricky. So the initial approach of considering only the initial ants is insufficient. Because splits in neighboring cells can add ants to a cell, which may cause it to split again.

So the problem requires us to model the propagation of splits through the grid.

So how can we model this efficiently?

Let me think of this as a BFS-like process. Each time a cell splits, it contributes to the neighbors. Each neighbor's ants are increased, and if that neighbor now has >=4 ants, it will split as well. But each split reduces the ants in the cell by 4, so the process can be modeled as:

For each cell (x,y), the number of times it splits is equal to the total number of ants (initial plus contributions from neighbors) divided by 4, considering that splits happen as soon as possible. But the order in which splits are processed affects how ants are distributed.

Wait, perhaps not. Because whenever a cell has >=4 ants, it splits. So the split count for a cell is floor((total_ants) /4), but the order in which splits are processed might not affect the final count. Because each split reduces the ants by 4, so the total number of splits is the total_ants //4, regardless of the order.

Wait, but suppose a cell has 5 ants. It splits once (leaves 1), then even if another ant arrives from a neighbor, making it 2, which is less than 4. So no more splits. So the total splits are 1. If another split from a neighbor arrives later, adding 2 ants, making total 3 (1+2=3), still no split.

So the order of splits in other cells doesn't affect how many splits a cell undergoes. Because each split in the cell reduces the ants by 4, and splits can only happen when the current count is >=4. So the maximum possible splits a cell can have is the total ants (including contributions from other splits) divided by 4, with integer division. Because each split removes 4 ants, and after that, any remaining ants (including new contributions) can only cause more splits if their sum is >=4.

But how do we model the total_ants for each cell, considering that ants can arrive from splits in neighboring cells after the initial split?

Hmm, perhaps we can model this using a priority queue or BFS approach. Let's think of it as a grid where each cell's split count contributes to their neighbors. But each time a cell splits, it sends ants to the neighbors, which may then require their own splits. So we need to process splits in a way that whenever a cell's ants reach >=4, it splits, and this is processed in a certain order.

But how to track the ants in each cell, and process splits efficiently.

Alternative idea: represent the number of ants in each cell as a value that can be incremented by splits from neighboring cells, and track which cells have enough ants to split again. This sounds like BFS.

So here's a possible approach:

- We maintain a dictionary (or a hash map) that tracks the number of ants in each cell. Initially, the cell (0,0) has n ants. All others have 0.

- We also maintain a queue of cells that have >=4 ants and need to split. Initially, if (0,0) has >=4 ants, it's added to the queue.

- While the queue is not empty:

   - Dequeue a cell (x,y).

   - Determine how many splits can be done. The number of splits is (current_ants //4). Because each split removes 4 ants and adds 1 to each neighbor.

   - So, for the current cell (x,y), the number of splits is s = current_ants //4.

   - Subtract s *4 from the ants in (x,y). The remaining ants are current_ants %4.

   - For each neighbor (x±1, y) and (x, y±1), add s ants. So each neighbor's count increases by s.

   - For each neighbor, after adding s ants, check if their new count is >=4. If so, add them to the queue (if not already in the queue).

But wait, this approach may not be correct. Because processing the splits in this way (calculating s as the current_ants//4) might not account for the fact that the ants in the cell could have been increased by other splits in the meantime.

Wait, for example, suppose a cell (x,y) has 5 ants. So s=1. Subtract 4, leaving 1. Then, the neighbor cells get 1 each. But if another split from another cell adds 3 ants to (x,y), making it 4. Then, (x,y) should split again. So the queue approach needs to process cells multiple times as their ant counts reach >=4 again.

But in the approach above, when (x,y) is processed, it's removed from the queue, and the ants are adjusted. However, after other splits contribute to (x,y), it may reach >=4 again, and need to be re-enqueued.

So the correct approach is:

Each time a cell's ant count is increased, check if the new total (after previous splits) is >=4, and if so, add it to the queue (if not already there). Then, process the queue until it's empty.

But how to model this.

Wait, here's the correct algorithm:

Initialize the ants dictionary with (0,0) having n ants.

Create a queue and add (0,0) to it if ants[(0,0)] >=4.

While the queue is not empty:

   Dequeue a cell (x,y).

   If the current_ants <4, skip processing (since it's possible that while the cell was in the queue, other splits added ants to it, but when dequeued, the count is already reduced).

   Otherwise, compute how many times it can split. But since we process each cell only once, perhaps this approach is not correct.

Wait, no. Because when we process a cell, we can split as many times as possible, given the current_ants. For example, if the cell has 9 ants, then we can split twice (taking 8 ants), leaving 1. Then, the neighbors get 2 each. So processing the cell once, even if it could split multiple times, is more efficient.

Wait, but that's the key! Because when processing a cell, the number of splits is current_ants //4. So for a cell with 9 ants, we can split twice (9//4=2), subtract 8, leave 1. Then, each neighbor gets 2 ants. So this way, the cell is processed once, and all possible splits at that moment are handled.

But how does this account for new ants arriving later from neighbors?

For example, suppose cell (x,y) has 9 ants, splits into 2 times, leaves 1. Then, neighbors get 2 each. Now, later, some neighbor splits and sends 1 ant to (x,y). Now, (x,y) has 2 ants. Still <4, so no split. So no problem.

But if (x,y) after splitting (leaving 1) receives 3 ants from neighbors, making 4. Then, (x,y) should split again. But according to the algorithm, how is this handled?

In the algorithm as described earlier, after processing (x,y), the cell's ants are 1. Then, if another split from a neighbor adds 3 ants, the total becomes 4. So the neighbor's split processing (when they split) would add ants to (x,y). Then, when adding those ants, we check if (x,y)'s total is >=4. If yes, add it to the queue.

So the algorithm must, whenever adding ants to a neighbor (like (x,y) in this case), check if the new total is >=4, and if so, add it to the queue if it's not already in.

Wait, but how to track this. For example, when a neighbor adds s ants to (x,y), we need to check if (x,y) was previously not in the queue, and now after adding s ants, its total is >=4. If so, add to queue.

But how to track whether (x,y) is already in the queue or not. Because if (x,y) is already in the queue, then when we process it, we'll process all possible splits at that moment, but maybe after adding s ants, the current count is now higher, and the existing queue entry for (x,y) would process all the splits possible at that time.

So the problem is that if a cell is already in the queue, but in the meantime, more ants are added, then when it's processed, it can process all possible splits at that time (since the split count is current_ants//4).

So the correct approach is:

- Whenever ants are added to a cell (x,y), if after adding, the ants >=4 and the cell is not already in the queue, then add it to the queue.

Wait, but how do we track whether a cell is already in the queue. Because if a cell is in the queue multiple times, processing it once would process all possible splits, so having it multiple times in the queue would be redundant.

So to avoid processing the same cell multiple times, perhaps we can have a visited flag, but that's not feasible because a cell can be added to the queue again after being processed if new ants are added later.

Wait, but when a cell is processed, it's possible that after processing, the ants are still >=4. For example, suppose a cell has 8 ants. When processed, it splits twice (8//4=2), subtracts 8, leaves 0. So after processing, it's 0. But suppose the cell had 5 ants. When processed, splits once (5-4=1). So after processing, ants are 1. So when a cell is processed, after splits, it's ants are (current_ants %4). So when a cell is dequeued and processed, after the splits, the remaining ants are (current_ants %4). So the cell's count is (current_ants //4) *4 subtracted from the current_ants.

So, during processing:

current_ants = ants[(x,y)]

s = current_ants //4

if s ==0:

   skip processing

else:

   ants[(x,y)] = current_ants %4

   for each neighbor:

       ants[neighbor] += s

       if ants[neighbor] >=4 and neighbor not in queue:

           add neighbor to queue

So the key is that after processing a cell, the remaining ants are current_ants %4. So once a cell is processed, even if more ants are added later (from other splits), those ants will be added to the existing count (current_ants %4 + new ants). So if the new total is >=4, the cell must be added to the queue again.

But how to track whether the cell is already in the queue. Because the queue could have multiple entries for the same cell. For example, a cell is processed once, then another split adds ants to it, making its count >=4 again. It's added to the queue again. Then, when dequeued again, processed again.

So the algorithm must allow a cell to be added to the queue multiple times, but only when necessary (i.e., when after adding ants, the total is >=4 and the cell is not already in the queue). Wait, no. Because the queue may have multiple entries for the same cell. But when processing a cell, all possible splits (current_ants//4) are handled at once. So even if multiple entries exist, processing the cell once would process all possible splits up to that point.

Wait, for example:

Suppose a cell (x,y) is in the queue. Then, before it's processed, another split adds more ants to it, and it's added to the queue again. Now the queue has two entries for (x,y). When the first entry is processed, the current_ants is current_ants (original) plus the new ants. Because the splits are calculated as current_ants //4, which includes all the added ants. So even if there are multiple entries, processing once would handle all possible splits.

But in the algorithm as described, when a cell is added to the queue, it's checked whether it's already in the queue. If not, then it's added. This is necessary to avoid multiple entries for the same cell, which would lead to redundant processing.

But how to track if a cell is already in the queue. Because in the BFS approach, once a cell is dequeued, it's processed, and then any subsequent additions of ants to it may require adding it to the queue again.

So the queue can have a cell processed multiple times. So we can't have a 'in_queue' flag. Instead, the queue is allowed to have multiple entries, but when a cell is processed, all possible splits at that moment are done.

Wait, but this could lead to the same cell being processed multiple times, which would be inefficient.

Alternatively, when a cell is dequeued, we check if after all possible splits (current_ants//4) it's possible. For example:

current_ants = ants[(x,y)]

s = current_ants //4

if s ==0:

   skip

else:

   process the splits.

But even if after processing, the ants remaining is 0, but then more ants are added later. So the algorithm must re-add the cell to the queue when those ants are added.

But in the case where a cell is processed, and after processing, the remaining ants is 1. Then, some other split adds 3 ants to it, making it 4. So when those 3 are added, the ants is now 4. The code must check if the cell is already in the queue. If not, add it. So how to track that.

Hmm, this is getting complicated. Let's think of using a standard BFS approach with a queue, but allow cells to be added multiple times. However, processing a cell multiple times may not be efficient.

But given the problem constraints, perhaps this is manageable.

Let's outline the steps:

Initialize ants as a dictionary with (0,0):n.

Initialize a queue. If (0,0) has ants >=4, add to the queue.

Also, use a visited set to track whether a cell is already in the queue. Because if a cell is already in the queue, we shouldn't add it again. Wait, but once it's dequeued, the set is updated. So:

Wait, perhaps use a dictionary called 'in_queue' to track whether a cell is currently in the queue. When a cell is added to the queue, 'in_queue' is set to True. When it's dequeued, 'in_queue' is set to False. Then, whenever ants are added to a neighbor, if the neighbor's ants >=4 and not in_queue, add to the queue and mark in_queue as True.

This way, each cell is in the queue at most once. So when the cell is dequeued, it's processed, and any subsequent ants added to it can trigger adding it to the queue again.

But the problem is that while the cell is in the queue (but not yet processed), other ants can be added to it. But since the cell is marked as in_queue, those new ants won't trigger another addition. But when the cell is processed, the code checks the current_ants (including all ants added up to that point) and processes all possible splits.

So this should handle all possible splits.

So the algorithm steps:

Initialize ants as a dictionary. ants[(0,0)] = n.

Create a queue and add (0,0) if ants[(0,0)] >=4.

Create a 'in_queue' set or dictionary to track cells currently in the queue.

While queue is not empty:

   Dequeue (x,y).

   Mark (x,y) as not in_queue.

   current_ants = ants.get((x,y), 0)

   s = current_ants //4

   if s ==0:

       continue

   ants[(x,y)] = current_ants %4  # remaining ants after splits

   for each neighbor in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:

       ants[neighbor] = ants.get(neighbor, 0) + s

       if ants[neighbor] >=4 and (neighbor not in in_queue or not in_queue[neighbor]):

           add neighbor to queue

           in_queue[neighbor] = True

So in this approach, whenever ants are added to a neighbor, we check if the neighbor is already in the queue. If not, add it.

This way, each cell is processed only when it has >=4 ants, and after processing, any further additions may add it to the queue again if needed.

This should handle all splits correctly.

Now, for the data structures:

The ants can be stored in a dictionary, since the coordinates can be up to 1e9 in absolute value. So a hash map is needed. But given that each split can generate new cells, but the number of splits is limited by n (since each split consumes 4 ants, but each split produces 4 ants, but distributed to four cells. But the sum remains n. So the number of cells with ants is O(n) in the worst case. Because each split from a cell (x,y) contributes 1 ant to each of four neighbors, but each of those neighbors can split only if their total ants >=4. So the number of splits is O(n), but each split can generate up to four new cells. But in the worst case, the number of cells could be O(n), but for n up to 3e4, that's manageable.

The queue can be a deque, which allows O(1) appends and pops.

The 'in_queue' can be a dictionary that maps (x,y) to a boolean indicating whether it's in the queue.

Now, after processing all splits, the ants dictionary contains the final counts for each cell. Then, for each query (x_i, y_i), we just return ants.get((x_i, y_i), 0).

So the approach is feasible.

Now, let's test this with the sample input.

First sample:

n=1, t=3. The initial ants is 1. Since 1<4, the queue is empty. So no processing. All queries return 0 except (0,0) which returns 1.

Second sample:

n=6. Initial ants at (0,0) is 6. So s=6//4=1. So after processing, (0,0) has 6%4=2. Each neighbor (0,1), (0,-1), (1,0), (-1,0) gets 1 ant. So (0,1) has 1, (0,-1) has 1, (1,0) has 1, (-1,0) has 1. Each of these has 1 ant, which is less than 4, so no more splits. So the queries:

0 -2: 0 ants (it's two steps down from (0,-1), but (0,-1) only has 1 ant, so no splits. So the answer is 0.

0 -1: after the split, (0,-1) has 1 ant. So query here is 1.

0 0: 2 ants.

0 1: 1 ant.

0 2: 0.

Which matches the sample.

So the algorithm works.

Now, the code.

But in code, how to represent the ants, queue, and in_queue.

In Python, using a defaultdict for ants would be useful, but for memory efficiency, a regular dictionary is better.

But for speed, using a normal dict and get methods.

The code steps:

Read n and t.

Initialize ants as a dictionary. ants = {(0,0):n} if n>0 else empty.

Initialize queue: from collections import deque.

queue = deque()

in_queue = a dictionary (could be a set, but using a set may be slower for checking membership). So using a dict for in_queue, where keys are tuples (x,y).

Then, process the queue as per the algorithm.

After processing, answer the queries.

Now, for the code.

But for handling large n and t (n up to 3e4, t up to 5e4), we need to process the queue efficiently.

But in Python, using a deque and dictionaries should be manageable.

But let's think about possible optimizations. For example, when a cell (x,y) is processed, and s is 0, we can skip processing.

Now, code:

Read n, t. Then read t queries.

But the code must read the queries even if n is 0.

But if n is 0, then all ants are zero. So all queries return 0.

So code outline:

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    n, t = map(int, input_stream.readline().split())
    queries = [tuple(map(int, input_stream.readline().split())) for _ in range(t)]

    ants = {}
    if n >0:
        ants[(0,0)] = n

    queue = deque()
    in_queue = {}

    if (0,0) in ants and ants[(0,0)] >=4:
        queue.append( (0,0) )
        in_queue[ (0,0) ] = True

    while queue:
        x, y = queue.popleft()
        del in_queue[ (x,y) ]

        current = ants.get( (x,y), 0 )
        s = current //4

        if s ==0:
            continue

        # update current cell's ants
        ants[ (x,y) ] = current %4

        # distribute to neighbors
        deltas = [ (1,0), (-1,0), (0,1), (0,-1) ]
        for dx, dy in deltas:
            nx = x + dx
            ny = y + dy

            # add s to neighbor
            neighbor = (nx, ny)
            ants[neighbor] = ants.get(neighbor, 0) + s

            # check if neighbor should be added to queue
            if ants[neighbor] >=4 and (neighbor not in in_queue or not in_queue.get(neighbor, False)):
                queue.append( neighbor )
                in_queue[ neighbor ] = True

    # process queries
    for x, y in queries:
        print( ants.get( (x,y), 0 ) , file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 5
0 -2
0 -1
0 0
0 1
0 2
""",
            "output": \
"""\
0
1
2
1
0
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

n=6. Initial ants[(0,0)] =6. Queue starts with (0,0). Processing:

Dequeue (0,0). current is 6. s=1. ants[(0,0)] becomes 6%4=2.

Neighbors:

(1,0) +=1 → 1. Not >=4. (0,1) +=1 →1. Not >=4. (-1,0) +=1 →1. (0,-1) +=1 →1.

So none of the neighbors are added to the queue. So queue is empty. Processing stops.

So ants at (0,0) is 2. (0,1) is 1. (0,-1) is 1. The queries in sample 2 are 0-2 (0), 0-1 (1), 0-0 (2), 0+1 (1), 0+2 (0). Which matches the sample.

So code works for samples.

But what about cases where a cell is added multiple times. For example, after processing a cell, some splits add ants to it, making it >=4 again.

But in the code, after processing (x,y), the ants are reduced to 2. Then, suppose another split from a neighbor adds 2 ants, making it 4. Then, when adding to the neighbor (x,y) in that split, the code checks if ants[(x,y)] is >=4 (4) and not in the queue. Since (x,y) was dequeued, in_queue is False. So it's added again.

Thus, the code handles that.

Now, the code must read all queries and output the ants.get( (x,y), 0 ) for each.

But for large inputs, this code may be efficient enough. Let's think about the time complexity.

Each split of a cell (x,y) contributes s=current_ants//4 ants to each neighbor. The number of splits per cell is O(1) on average, since each split reduces the ants by 4. The total number of splits across all cells is O(n), since each split takes 4 ants from the system (but adds 4 ants to the neighbors). Wait, no: each split subtracts 4 ants from the current cell, but adds 4 ants (s *4, but s is splits per cell). Wait, each split for a cell (x,y) takes 4 ants from (x,y) and adds 1 ant to each of four neighbors, totaling 4 ants added. So the total number of ants in the system remains the same. But each split consumes 4 ants from a cell and creates 4 ants (one per neighbor). So the total number of splits is sum over all cells (s_i), where s_i is the number of splits for cell i. But the sum of 4*s_i across all cells is equal to the initial ants minus the final ants (which is sum (a_i %4) for all cells). Since the initial ants is n, and sum a_i %4 < 4* number of cells. So sum s_i is O(n/4). So the total number of splits is O(n).

Each split processed in the queue involves dequeuing a cell, processing it, and enqueueing up to four neighbors (but each enqueue is O(1)).

Thus, the total time complexity is O(n + t), which for n=3e4 and t=5e4 is manageable.

The memory usage is storing the ants dictionary, which for n=3e4, each split contributes up to 4 new cells, but each split is O(1). So the number of cells is O(n). So memory is manageable.

Thus, the code should work within the time and memory constraints.

Now, the code must read input via input(), but using sys.stdin.readline() is faster, which is better for handling large inputs.

But the code as written uses sys.stdin, which is correct.

Another possible optimization is pre-processing all queries and then processing them, but in this case, the code processes each query as a lookup in the ants dictionary. Since the ants dictionary is built during processing, and queries are processed after all splits are done.

Thus, the code should be correct.
</think>

```python
import sys
from collections import deque

def main():
    n, t = map(int, sys.stdin.readline().split())
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(t)]
    
    ants = {}
    if n > 0:
        ants[(0, 0)] = n
    
    queue = deque()
    in_queue = {}
    
    if (0, 0) in ants and ants[(0, 0)] >= 4:
        queue.append((0, 0))
        in_queue[(0, 0)] = True
    
    while queue:
        x, y = queue.popleft()
        if (x, y) in in_queue:
            del in_queue[(x, y)]
        
        current = ants.get((x, y), 0)
        s = current // 4
        if s == 0:
            continue
        
        ants[(x, y)] = current % 4
        
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            ants[neighbor] = ants.get(neighbor, 0) + s
            
            if ants[neighbor] >= 4 and not in_queue.get(neighbor, False):
                queue.append(neighbor)
                in_queue[neighbor] = True
    
    for x, y in queries:
        print(ants.get((x, y), 0))

if __name__ == "__main__":
    main()
```
