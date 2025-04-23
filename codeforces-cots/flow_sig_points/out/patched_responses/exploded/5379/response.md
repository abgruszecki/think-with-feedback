<think>
Okay, I need to solve this programming problem. Let's read the problem carefully and understand what's required.

So, the problem is about a restaurant serving different types of food. Each customer orders a certain number of dishes of a specific type. The way they are served depends on the remaining dishes. The main challenge is to efficiently process a large number of customers (up to 1e5) with each order possibly being up to 1e7 dishes. The constraints are tight, so we need an optimal approach.

Let me break down the problem:

For each customer j:
- They order d_j dishes of type t_j.
- The serving process is as follows for each dish they order:
   1. First, check if the remaining dishes of type t_j are available. If yes, take one.
   2. If not, find the cheapest available dish (smallest c_i, then smallest index if there's a tie), take one.
   3. If no dishes left anywhere, the customer pays 0 and leaves, regardless of how many were served before.

The total cost for the customer is the sum of the costs of all dishes served, but only if all d_j dishes were served. Otherwise, it's 0.

Wait, no. Wait the third condition says that if at any point there are no more dishes left, the customer leaves angrily. So even if they served some dishes, if the remaining dishes can't fulfill the entire d_j, the cost is 0. Wait, no. Let me re-read the problem statement.

Ah, the note says: "If the customer doesn't leave after the d_j dishes are served, the cost is the sum..." So, the customer's cost is 0 if they couldn't serve all d_j dishes. Otherwise, the sum of the costs for those dishes.

Wait, the third point says: "if there are no more dishes at all, the customer leaves angrily. Therefore, no matter how many dishes are served previously, the cost is 0."

So, if during serving the customer's order, at any point you can't serve a dish (because all remaining dishes are zero), then even if you served some dishes before, the cost for that customer is 0.

So, the customer's order must be served in full (exactly d_j dishes) to have a non-zero cost. If during the process, you can't serve even one of the dishes needed, the entire cost is zero.

Therefore, for each customer, we need to check if we can serve all d_j dishes. If yes, sum the costs. Otherwise, output 0.

This complicates things because we need to track whether all d_j can be served. If any step during serving the d_j dishes results in a situation where no dishes are left, then the entire cost is 0.

So the problem is to process each customer's d_j dishes, trying to take them either from their preferred type or from the cheapest available, and calculate the total cost only if all d_j are served. Otherwise, output 0.

But with m up to 1e5 and each d_j up to 1e7, a naive approach where we process each dish one by one is impossible. So we need an efficient way to batch process these orders.

First, let's think about the data structures needed.

We need to track for each type, the remaining count (a_i). Initially, a_i is given, but we need to update it as orders are processed.

Additionally, when the preferred type is exhausted, we need to find the next available type with the smallest cost and smallest index. So, we need a priority queue (or a min-heap) that keeps track of available types sorted by their cost and index.

Wait, but the available types are those with a_i > 0. So whenever a type's a_i becomes zero, it's removed from consideration.

But maintaining this in a heap can be tricky. Because when a type's a_i is decremented, but it's still positive, it's still in the heap. Only when a_i becomes zero, it's removed.

But the heap needs to have the current minimum cost types. So, perhaps the heap is a min-heap that contains all types with a_i > 0, ordered by (c_i, index). But how do we handle cases where the same type is added multiple times to the heap?

Wait, no. The heap should always have the available types. So, once a type is in the heap, and if after some operation its a_i is reduced but still positive, it's still in the heap. But if we process the same type again, how do we know if it's still available?

Ah, perhaps we can have a heap that contains entries for each type. But when a type's a_i becomes zero, we mark it as unavailable and ignore any entries in the heap that are for that type.

But this could lead to having stale entries in the heap. So, we need a way to efficiently manage the available types.

Alternative approach:

We can have a priority queue (min-heap) that contains all the available food types, ordered by (c_i, index). Each entry in the heap is a tuple (c_i, index). But we need to keep track of the current a_i for each type.

But when a type's a_i is reduced to zero, it's no longer available and should be removed from consideration.

The problem is that the heap might have entries for a type that is already exhausted. So when we extract the minimum from the heap, we need to check if that type still has a_i > 0. If not, we pop it and continue until we find a type that is available.

So the heap could have multiple entries for the same type, but we have to process them carefully.

Wait, no. The heap should only have each available type once. Because once a type is in the heap, and its a_i is positive, it's considered. But if after processing some order, the type's a_i is still positive, it remains in the heap. However, when the a_i of a type in the heap is reduced to zero, the next time we try to extract it from the heap, we check and skip it.

But the heap will not automatically remove those entries. So this approach could lead to O(n) time in the worst case, but perhaps in practice, since each entry is processed once, the total time is manageable.

So, the steps for processing each customer's order would be:

For each customer j with t_j and d_j:

1. Try to take as many dishes as possible from t_j.

   a. The available dishes in t_j are a[t_j-1]. Let's say current_available = a[t_j-1].

   b. We can take min(current_available, d_j) dishes from t_j. Subtract this from a[t_j-1], add to the cost.

   c. Update d_j to d_j - taken.

   d. If d_j is now zero, proceed to the next customer. The cost is summed and output.

   e. If d_j remains, then we need to take the remaining dishes from the cheapest available types.

2. For the remaining d_j dishes:

   a. While d_j > 0 and there are available dishes:

      i. Find the cheapest available type (smallest c_i, then index).

      ii. Take as many dishes as possible from this type, up to d_j.

      iii. Subtract the taken from a[type], add to the cost.

      iv. If the type's a becomes zero, remove it from the heap.

      v. d_j is reduced by the taken amount.

   b. If during this process d_j becomes zero, output the sum.

   c. If there are no available dishes and d_j is still positive, output 0.

But how do we efficiently find the cheapest available type?

The idea is to use a priority queue (min-heap) that contains all the available types. But when a type's a_i is reduced to zero, we can ignore it when we extract it from the heap.

But the problem is that when a type is in the heap but has a_i > 0, but when we process it again, the a_i might be lower. However, in the heap, each entry is (c_i, index) and once a type is in the heap, we don't need to re-add it again. Because once it's in the heap, and we process it, we take as much as possible from it (the maximum possible given d_j and a_i).

Wait, but suppose a type is still in the heap (because it was not popped when a_i was reduced to zero). But after some steps, it's possible that the a_i was increased again. Wait no, because once a dish is taken, a_i can only decrease.

So each time we process a customer, we take dishes from the preferred type first. Then, for the remaining, we take from the cheapest available.

But the heap needs to track the current available types. So, whenever a type's a_i is positive, it's in the heap. But how?

Wait, perhaps the heap is initialized with all the types that have a_i > 0, ordered by (c_i, index). Then, whenever we take dishes from a type (either the preferred type or the cheapest type), if after taking, the type's a_i becomes zero, we don't need to do anything with the heap, except that when it's extracted again from the heap, we check if a_i is still positive. If not, we skip it.

So the algorithm would proceed as:

Initialize a min-heap with all types (i) where a_i > 0, sorted by (c_i, i). But since the heap is built once and then modified as we process orders.

Wait, but when a type is taken from the heap (e.g., the cheapest), and after taking some dishes, the a_i might be zero, so the next time we extract the same type from the heap, we check and skip.

But the heap still contains entries for all types that were ever added. So, this could lead to O(1) for each extraction, but in practice, we might have to extract a lot of entries that are already empty.

But for large m and d_j, this could lead to O(m * k) where k is the number of heap operations per customer, which could be too slow.

So, this approach is not feasible for large d_j (up to 1e7). Because for each customer, if we have to process each dish step by step, even in batches, but with d_j up to 1e7, it's impossible.

Therefore, we need a way to process the entire d_j dishes in O(1) or O(log n) time per customer, not O(d_j) time.

The key insight here is that when taking dishes from a type, we can take as many as possible in one batch.

So, for the preferred type:

- Take min(d_j, a[t_j-1]) dishes. Subtract this from a[t_j-1], add to the cost. If after this, a[t_j-1] becomes zero, we need to remove it from the heap (if it's present). But how?

Wait, the heap contains all available types (with a_i >0). When the preferred type was in the heap, but after taking some dishes and a_i becomes zero, we need to remove it from the heap.

But the heap is a priority queue, and we can't directly remove elements. So perhaps the way to handle this is to check when we take from the preferred type first. Then, if after that, the a_i of the preferred type is zero, we can leave it in the heap, but when it's extracted again, we check a_i and skip if it's zero.

But that's not efficient. So perhaps the preferred type is not part of the heap once it's processed. Wait, but the preferred type's a_i could be non-zero even after processing the first part. For example, if the customer's order is d_j=5, and the preferred type has 3 available. So 3 are taken, and the remaining 2 are taken from the heap. The preferred type's a_i is now zero, so it's removed from the heap. But how?

Alternatively, perhaps the heap only contains the available types except for the preferred type when processing the initial part. But that's not feasible because other customers might have different preferred types.

Alternatively, the heap should contain all available types (a_i>0) except those that are processed in the first part.

No, that's not possible. So the problem is that the preferred type could still be part of the heap. For example, after processing the initial part of the customer's order, the preferred type's a_i is reduced but still positive. So it remains in the heap.

But when the next customer's order is processed, if the preferred type is another type, then the heap still has the previous type.

So the heap needs to manage all available types except those that have a_i=0.

But the problem is how to efficiently manage the heap when a type's a_i is reduced to zero. The answer is that whenever we take some dishes from a type (either in the first part or the second part), if after that the a_i becomes zero, we can note that this type is no longer available and the next time we try to take from the heap, we skip any types that have a_i=0.

So, the heap can have entries that are no longer valid (i.e., a_i=0). But when we pop from the heap, we check if the type is still available (a_i>0). If not, we skip it and pop the next one. This is known as the "lazy deletion" approach.

So the steps are:

For each customer:

1. Check the preferred type t_j.

   a. Take the minimum between d_j and a[t_j-1]. Let this be take = min(d_j, a[t_j-1]).

   b. Subtract take from a[t_j-1]. Add take * c[t_j-1] to the current customer's cost.

   c. Update d_j = d_j - take.

   d. If a[t_j-1] becomes zero, we need to note that this type is now unavailable (but it's already in the heap? Or was it in the heap?)

Wait, the preferred type might not be in the heap. Because the heap is supposed to contain all available types except those processed in the first part. Or maybe the heap contains all available types.

Wait, when the heap is initialized, it contains all types with a_i>0, ordered by (c_i, index). So, if the preferred type has a_i>0, it's in the heap. But when we process the first part of the customer's order, we take as much as possible from the preferred type. If after that, the preferred type's a_i is zero, then we need to remove it from the heap. But since the heap is a separate structure, and the preferred type's entry might still be in the heap, we need a way to mark it as invalid.

So, perhaps the heap entries are (c_i, index) and when processing, after taking the preferred type's dishes, if it's now zero, we can leave it in the heap, but when someone tries to extract it, they check the current a_i and if it's zero, they ignore that entry.

This lazy deletion approach allows us to avoid updating the heap when a type's a_i becomes zero. The heap may have stale entries, but when they are popped, we check the current a_i and proceed accordingly.

But how do we handle the case where the preferred type's a_i is not zero after the first part? For example, a customer orders 5 dishes of type 2, which has 10 available. So after the first part, 5 are taken, a_i becomes 5, which is still in the heap. The next time the heap is accessed, this type is still available.

So, the main steps are:

For each customer:

sum = 0

d = d_j

t = t_j - 1 (assuming 0-based index)

take = min(a[t], d)

sum += take * c[t]

a[t] -= take

d -= take

if a[t] == 0 and t is in the heap (but how?), then remove it. But we can't directly modify the heap.

So, perhaps after taking from the preferred type, if a[t] is now zero, but this type is in the heap, then when the heap is processed next, it's skipped.

So, after handling the preferred type, if there's still d > 0, we need to take from the heap.

But here's the problem: the preferred type may have a_i>0, but after taking some dishes, the a_i may be positive. So, when the heap is processed next, the preferred type may still be in the heap. But if the preferred type's a_i was reduced but not to zero, then it's still in the heap. However, when the next customer has a different preferred type, the heap may still have this type, which is valid.

So, the heap remains as a min-heap of (c_i, index) for all types that were ever added, but when we pop from it, we check if the a_i is >0. If not, we skip that entry.

So, for the remaining d dishes:

We need to process them by taking as much as possible from the current cheapest type.

But the problem is that when we take from the cheapest type, we can take min(d, a_i) dishes. So, this is a batch operation. So, for each step:

current_cheapest = get the next valid type from the heap.

if no valid type left, output 0 for this customer.

else:

take = min(d, a[i])

sum += take * c[i]

a[i] -= take

d -= take

if a[i] == 0:

   remove from the heap (but we can't do this directly)

But again, the heap isn't updated. So when the next time we extract the same (c_i, i) from the heap, we check if a[i] is still >0. If not, we skip.

But in the next customer's processing, when we take from the heap, the same entries can be present.

So the algorithm for handling the remaining d dishes is:

while d > 0:

   get the next candidate from the heap.

   while the heap is not empty and a[heap's current top's index] == 0:

       pop it.

   if heap is empty:

       sum = 0

       break

   current_c, current_i = heappop(heap) ??

Wait, no. Because the heap is a priority queue, and each time we pop the minimum (c_i, index). But how do we check if a[i] is still positive?

Wait, the heap is a min-heap of (c_i, index) entries. But when we pop an entry, we first check if a[i] is positive. If not, we ignore this entry and proceed to the next one.

So, the process is:

while d > 0:

   while the heap is not empty:

       current_c, current_i = heappop(heap)

       if a[current_i] > 0:

           break

   else:

       sum = 0

       break

   take = min(d, a[current_i])

   sum += take * current_c

   a[current_i] -= take

   d -= take

   if a[current_i] > 0:

       heappush(heap, (current_c, current_i))

So, in this approach, after taking as much as possible from the current_i, if there are remaining a[current_i], we push it back into the heap.

But this can lead to multiple entries of the same type in the heap. Because after taking some dishes, but not all, the type is pushed back into the heap. So, for example, a type with c_i=2, a_i=5. If a customer takes 3 dishes, then a_i becomes 2. We push (2, i) back into the heap. The next time this type is popped, it's checked again.

But this approach is correct. Because when a type is processed, the maximum possible is taken in one batch. And after processing, if there's remaining a_i, it's added back into the heap.

This way, each time we process a customer's order, the steps are:

1. Take as much as possible from the preferred type.

2. Then, take the remaining from the cheapest available type (using the heap), taking as much as possible each time, and pushing the type back into the heap if there's remaining a_i.

This way, each customer is processed in O(1) (for step 1) plus O(k log n) for step 2, where k is the number of heap operations needed. Since each heap operation is O(log n), and for each customer, k is the number of different types they take from step 2. For example, if the remaining dishes are all taken from a single type, then k is O(1). So in the worst case, for a customer that takes from O(1) types in step 2, each customer is O(log n) time.

But how does this handle d_j up to 1e7? Because the processing is done in batches, not per dish. So even if a customer orders 1e7 dishes, but all are taken from a single type (preferred or cheapest), the processing is O(1) for step 1 and O(1) heap operations for step 2.

This is manageable.

Now, let's think about the data structures.

The heap is a min-heap, ordered by (c_i, index). We need to initialize it once, but as the a_i's change, the heap is dynamically updated.

But initializing the heap with all (c_i, i) where a_i >0. So, for all i from 0 to n-1, if a[i] >0, push (c[i], i) into the heap.

Wait, but when a[i] is zero, we don't push it. So the initial heap contains all available types.

Then, during processing:

For each customer:

   process the preferred type.

   if any remaining d, process via the heap.

So the code steps:

Read n and m.

Read a as list.

Read c as list.

heap = []

for i in 0..n-1:

   if a[i] >0:

       heapq.heappush(heap, (c[i], i))

Then, for each customer:

   t, d = map(int, input().split())

   t -= 1  # convert to 0-based.

   current_sum = 0

   # Step 1: take from preferred type.

   take = min(a[t], d)

   current_sum += take * c[t]

   a[t] -= take

   d -= take

   if d == 0:

       print(current_sum)

       continue

   # Step 2: take from the heap.

   while d >0:

       # Get the next valid entry from the heap.

       valid = False

       while heap:

           current_c, current_i = heapq.heappop(heap)

           if a[current_i] >0:

               valid = True

               break

       if not valid:

           current_sum = 0

           break

       take = min(d, a[current_i])

       current_sum += take * current_c

       a[current_i] -= take

       d -= take

       # Push back into heap if remaining.

       if a[current_i] >0:

           heapq.heappush(heap, (current_c, current_i))

   print(current_sum if d ==0 else 0)

Wait, but in this code, after taking from the heap, if there's a remaining a[current_i], we push it back. This allows the next customers to possibly take from it again.

But this code has an issue. The heap may have multiple entries for the same type. For example, when a type is popped, processed, and then pushed back into the heap if a_i>0. But since the heap is a priority queue, this entry will be placed in the correct position based on its (c_i, i).

This should be correct. Because each time, the next smallest (c_i, i) is processed.

But there's a problem here. When a type is processed (either in step 1 or step 2) and a_i is reduced but not to zero, the heap may not have that type's entry. For example, if the preferred type is processed in step 1, and after processing, a_i is still positive. But the preferred type's entry was not in the heap. Because the heap is not automatically updated when the preferred type's a_i is modified.

Wait, the heap contains entries for all available types (a_i>0) except those that were added to it. So, if the preferred type's a_i was positive before step 1, but after processing step 1, a_i is still positive, but the heap has the entry (c_i, i) for the preferred type. But in reality, the preferred type's a_i has decreased. However, the heap entry is still (c_i, i) and the a_i is now less than before.

But the heap's priority is based on (c_i, i), which hasn't changed. So even though the a_i has decreased, the priority remains the same. So the entry is still valid in the heap, but the a_i may have been modified. So when processing the heap, after popping (c_i, i), we check if a_i is >0, which it may or may not be.

But in the code above, the preferred type is not pushed into the heap again. So, after step 1, the preferred type's a_i may still be positive, but it's not in the heap. So the next time the heap is processed, the preferred type's entry is not present, even if it's available.

Wait, that's a problem.

Let me clarify:

The heap is initialized with all types that have a_i>0. So, for example, if the preferred type (t) has a_i>0, it is in the heap. But during step 1, we take some dishes from t. If after this, a[t] is still >0, then the heap may have an entry for t (since it was in the heap before step 1). But after step 1, we didn't modify the heap. So the heap still contains (c[t], t) as an entry. However, when we process the heap, we might pop this entry again, even though a[t] is still >0.

Wait, no. Because during step 1, the code doesn't modify the heap. So the heap still contains the entry (c[t], t), but after step 1, a[t] is now a[t] - take. So, if a[t] is now zero, then the entry (c[t], t) is in the heap, but when popped, it will check a[t] and see it's zero and skip.

But if a[t] is still positive, then when the heap is processed, the entry (c[t], t) is popped, but since a[t] is positive, it's considered valid and processed.

But in reality, after step 1, the preferred type's a_i may have been reduced. So the heap has an entry for it, which is correct. Because after step 1, the a_i could still be positive. So the heap entry is valid.

But during step 1, the code does not modify the heap. So the entry for the preferred type is still in the heap. But when we process step 2, we may take from it again if it's the cheapest option.

But that's incorrect. Because during step 1, we took from the preferred type, but the code didn't add it back to the heap. So the heap may have entries that are no longer available.

Wait, for example:

Initially, a[0] = 5, c[0] = 10. The heap contains (10, 0).

A customer orders type 1 (0-based index 0) with d_j=3.

Step 1: take 3 from type 0. a[0] becomes 2. The heap still has (10, 0) in it.

Then, in step 2, the code processes the heap. It pops (10, 0), checks a[0] which is 2>0, takes all 2 (if d is larger than 2), adds 2*10 to sum, subtracts 2 from a[0], and since a[0] becomes zero, it's not pushed back into the heap.

So the code works correctly.

But in this case, the preferred type was processed in step 1, and the heap still has the entry. But in step 2, the code processes it again, which is correct.

But what if another customer orders a different type, and during step 2, the heap contains the preferred type from a previous customer's step 1 processing?

This is correct. Because that type is still available (a_i>0), so the heap entry is valid.

So the code is correct.

But in the code, after step 1, the code does not push the preferred type back into the heap if a[t] is still positive. Because the code only pushes types into the heap when they are processed during step 2. So, the preferred type's entry is already in the heap if it was there initially. So, even after step 1, the heap entry is still there.

So for example, if a customer orders type t which has a_i=10 initially, and after step 1, a_i is 5, the heap entry is still (c[t], t), which is correct. Because the type is still available, and the heap entry is valid.

So, the code is correct.

Now, let's think about the test cases.

First sample input:

8 5

a = [8,6,2,1,4,5,7,5]

c = [6,3,3,2,6,2,3,2]

Heap initially contains all 8 types since a_i>0. The heap is ordered by c_i and index.

The first customer orders type 2 (0-based index 1?), wait wait, in the input, the first customer's line is "2 8", which is t_j=2 (1-based), so t becomes 1 (0-based).

So step 1: take min(6, 8) =6. sum +=6*3=18. a[1] becomes 0. d becomes 8-6=2.

Then, step 2:

Process the heap. The heap's entries are all initial types except those that have a_i=0. Wait, no. The heap was initialized with all types where a_i>0. After step 1, a[1] is 0, but the heap still has the entry (3,1). So when processing the heap:

We pop entries until we find one with a_i>0.

The first entries in the heap (after some pops) may be (2,3) (type 4, a=1) or (2,5) (type 6, a=5).

Wait, the initial heap is built with all 8 entries. Let's list them:

Indices (0-based):

0: a=8, c=6 → (6,0)

1: a=6, c=3 → (3,1)

2: a=2, c=3 → (3,2)

3: a=1, c=2 → (2,3)

4: a=4, c=6 → (6,4)

5: a=5, c=2 → (2,5)

6: a=7, c=3 → (3,6)

7: a=5, c=2 → (2,7)

So the heap will be ordered as:

The smallest c is 2, and the indices 3,5,7.

So the first entry in the heap is (2,3). When we process step 2 for the first customer:

After step 1, the remaining d is 2.

We enter the loop:

d=2>0.

We pop from the heap until we find a valid entry.

The first popped entry is (2,3). Check a[3] (which was 1 before step 1). But after step 1, a[3] is 1 (since it wasn't modified). So take min(2,1) =1. sum +=1*2=2. a[3] becomes 0. d=1. Now, since a[3] is 0, we don't push it back into the heap.

Next, we need to process d=1. Pop next entry from heap. Let's see the next smallest is (2,5) (type 5). Check a[5] =5. Take min(1,5) =1. sum +=1*2=2. a[5] becomes 4. d=0. Since a[5] is now 4>0, push (2,5) back into heap.

So total sum is 18+2+2=22. Which matches the sample.

So code works for this case.

But now, after step 1, the preferred type (type 1) has a_i=0. The heap had the entry (3,1), which is now popped in subsequent steps. But since a[1] is 0, when popped, it is skipped.

But how is the heap maintained?

In the code, after step 1, the heap still has (3,1), but a[1] is 0. So during step 2 processing, when that entry is popped, it's checked and skipped.

Thus, the code correctly skips any invalid entries.

Another example: the second customer in the first sample orders type 1 (0-based 0), d=4.

Step 1: a[0] is 8. take min(8,4) =4. sum +=4*6=24. a[0] becomes 4. d=0. So output 24.

The heap is not processed here. But after step 1, a[0] is 4>0, but the heap entry (6,0) is still present. So for future customers, this type can be processed again.

Thus, the code works.

So the code should handle all cases correctly.

Now, let's think about the data structures and time constraints.

The heap operations are O(log n) per push and pop. For each customer, in the worst case, we may have to process O(k) heap operations, where k is the number of types we process in step 2. For example, if a customer's order requires taking from multiple types in step 2, each time popping a type, taking some dishes, and pushing it back if remaining.

But in practice, since each type is pushed back into the heap only once per extraction (and after some dishes are taken), the total number of heap operations per customer is O(1) on average.

But for the worst case, suppose each customer's step 2 requires popping all types in the heap. But this is unlikely given the constraints.

The code's time complexity is O(n log n) for the initial heap building, and O(m * k log n), where k is the number of heap operations per customer. If k is small (like O(1) or O(2)), then for m=1e5, this is manageable.

But in the worst case, m=1e5 customers and each requires O(n) heap operations, this would be O(1e5 * 1e5) which is 1e10, which is way over the time limit.

So, this approach may not be efficient enough.

Wait, but in practice, each time we process a customer's step 2, the number of heap operations is O(1) per type processed. Because for each type, after taking some dishes, the remaining a_i is pushed back into the heap. So each type is processed once per step 2 for a customer.

But in the worst case, for each customer, we have to process all the types in the heap. Which would be O(n) per customer, leading to O(mn) time, which is 1e10 operations (n=1e5, m=1e5). This is way too slow.

Therefore, this approach is not feasible for the problem's constraints.

So, we need a more efficient way to handle the step 2 processing.

Alternative idea: track the current cheapest type, and for each customer, if the remaining d is large, we can directly compute how many dishes can be taken from the cheapest available type, which has the smallest c_i and smallest index.

But how to efficiently track the current cheapest type.

We can maintain a priority queue, but in a way that allows us to take the minimum (c_i, index) quickly, and when the type's a_i is zero, we remove it from consideration.

But the problem is that the priority queue (heap) approach can't handle this efficiently when there are a large number of elements.

Another approach: since the cheapest available type is the one with the smallest c_i, then the smallest index among them. So, perhaps we can track the current minimum in O(1) time.

But how?

If we can keep track of the current minimum, then for each customer's step 2, we can take as much as possible from it in O(1) time.

But maintaining the current minimum when a_i changes requires an efficient data structure.

Alternative idea: the minimum will only change when the current minimum's a_i is reduced to zero. Then, the next minimum can be found.

But how to track this.

Alternatively, we can have a structure that tracks all available types (a_i>0) sorted by c_i and index. The minimum is the first element.

This sounds like a priority queue again, but the problem is the same as before. So perhaps we need a different data structure.

Alternatively, we can maintain a list of available types sorted by (c_i, index), and for each step 2 processing, we can take as much as possible from the first element in this list.

But inserting and maintaining this sorted list is expensive for large n.

Wait, but what's the alternative?

An alternative approach is to realize that when a type is processed (either in step 1 or step 2), the remaining a_i may be zero. So, the available types are those with a_i>0.

We can maintain a pointer to the current minimum available type. But when the current minimum is exhausted, we need to find the next minimum.

But this requires O(n) time each time the current minimum is exhausted, which is not feasible.

So, the problem is that we need an efficient way to track the current minimum.

The priority queue approach is the correct way, but the problem is the time complexity.

Let's think again about the time constraints.

Each customer can have a d_j up to 1e7. But in our current approach, even if d_j is 1e7, we process it in batches, taking the maximum possible from the current minimum type. So for each customer, step 2 may require O(1) heap operations, if the remaining d_j can be taken from the current minimum type in one batch.

For example:

current_min_type has a_i=1e7, and customer's d_j=1e7. Then, take all 1e7 in one batch, sum +=1e7 * c_i. a_i becomes zero, and this type is removed from the heap.

So, for such a customer, step 2 is O(1) heap operations.

Another example: a customer's d_j=1e7, and the current minimum type has a_i=5e6. Then, take 5e6, sum increases, and the type is removed from the heap. Then, take the next minimum type, and so on. So for each customer, the number of heap operations is O(k), where k is the number of different types used in step 2. For large d_j, this could be O(1), like taking from a few types.

Thus, the average case could be manageable.

But for the worst case where each customer takes one dish from the current minimum type, leading to O(d_j) heap operations per customer, this is impossible.

But given that d_j can be up to 1e7, this approach would be O(m * d_j) time, which is way beyond 2 seconds for m=1e5 and d_j=1e7.

Thus, we need a smarter way to process the batch of dishes from the current minimum type.

But how?

The key insight is that when we take from the current minimum type, we can take min(d_j, a_i) dishes in one step, which requires O(1) time.

Thus, the total number of heap operations per customer is O(k), where k is the number of types processed in step 2.

But for each type, each time it is processed in step 2, it is removed from the heap and pushed back only once (if a_i>0 after taking). So, for a customer that takes d_j=1e7 dishes, but from a single type, this is O(1) heap operations.

So, for the first sample, the first customer's step 2 requires two heap operations: one for type 4 (a_i=1) and one for type 6 (a_i=5). But since the code takes the entire a_i of type 4 (1 dish) and part of type 6 (1 dish), it's two heap operations.

But for a customer with d_j=1e7 and a single type with a_i=1e7, step 2 requires one heap operation.

Thus, the code's time complexity is O(m * k * log n), where k is the number of heap operations per customer. If k is small (which it is for most cases), then it's acceptable.

But for the worst case where each customer requires k= O(log n) heap operations, then it's O(m log n log n), which for m=1e5 is manageable.

But how to verify this.

Let's see:

- The initial heap is built in O(n log n) time.

- Each customer's step 1 is O(1) time.

- For step 2, each heap pop is O(log n) time. Each push is O(log n) time.

- For each customer, the number of heap operations is the number of types processed in step 2. For example, if the customer takes from k types in step 2, then it's k pops and k pushes (if the type is not exhausted).

But the worst case is k= O(log n) per customer. For example, each step 2 customer takes one dish from the current minimum type. Then, each time, a type is popped, one dish is taken, and pushed back (if a_i >0). For d_j=1e7, this would require 1e7 heap operations, which is impossible.

But this is not possible because for each such step, you take all possible dishes from the current minimum type, not just one.

Wait, no. The code takes min(d, a_i) dishes from the current minimum type. So for example, if d_j=1e7 and a_i=1e7, then take all in one step, O(1) heap operations.

If d_j=1e7 and the current minimum type has a_i=5e5, then after taking 5e5 dishes, d_j is 9.5e6. Then, the next minimum type is popped, and so on.

The number of heap operations per customer is O(k), where k is the number of types processed in step 2. For example, if the customer's d_j is 1e7 and the available types have a total of 1e7 dishes, and each type has a_i=1, then k=1e7, which is impossible.

But such a scenario is unlikely given the problem constraints, but possible.

But given that a_i can be up to 1e7, and m up to 1e5, this code would not pass within the time constraints.

Thus, the code as proposed will not work for the problem's constraints.

We need a better approach.

Alternative approach:

The problem requires that during step 2, for the remaining dishes, the customer takes them from the cheapest available types. So, the order is to take from the current minimum available type, and so on.

So, the key is to track the current minimum available type.

We can represent the available types as a priority queue (min-heap), but we need to process each customer's step 2 in O(1) or O(1) per operation.

But how?

Let me think differently. Let's track the current minimum type.

Suppose we have a variable that holds the current minimum type. When we take dishes from this type, we can subtract as much as possible. If the type is exhausted, we find the next minimum.

But how to efficiently find the next minimum.

This approach would require maintaining a data structure that allows us to track the current minimum and update it when the current minimum is exhausted.

This is similar to using a priority queue but with lazy deletion.

But perhaps we can optimize by always keeping track of the current minimum.

Let's see:

Initially, the current minimum is the minimum (c_i, i) among all a_i>0.

When we take dishes from the current minimum:

- Take min(d, a_i) dishes.

- Subtract from a_i.

- If a_i becomes zero, we need to find the next minimum.

The next minimum is the new minimum among all a_i>0.

But finding the next minimum requires O(n) time, which is not feasible.

Thus, this approach is not feasible.

Alternative idea: use a pointer to the current minimum type. When the current minimum is exhausted, find the next minimum by scanning all types.

But this is O(n) per exhaustion, which is not feasible.

So, the only feasible data structure is the priority queue (heap), but with lazy deletion.

But the problem is that for large d_j, the code may take O(d_j) heap operations. But this is impossible.

Wait, no. Because the code takes min(d_j, a_i) dishes in one step. So, for a customer with d_j=1e7 and a current minimum type with a_i=1e7, this is O(1) heap operations. If a_i=5e6, then after taking 5e6 dishes, d_j is reduced by 5e6. The current minimum is then the next type, and so on.

Thus, the number of heap operations per customer is O(k), where k is the number of different types processed in step 2. For example, if a customer takes from 3 types in step 2, then k=3.

For the worst case, k could be O(n), but given that the sum of a_i is up to 1e7 * 1e5 = 1e12 (but each customer's d_j is up to 1e7), it's unlikely that each customer processes many types in step 2.

But even so, with m=1e5 and k=3 per customer, the total heap operations are 3e5, which is manageable.

Thus, the code should work within the time constraints.

So, the code is correct and efficient enough for the given problem.

Now, let's proceed to code.

But wait, in Python, the heap is a min-heap. Each heappop is O(log n), and heappush is O(log n).

The code steps are as described.

So, the code would be:

import heapq

n, m = map(int, input().split())

a = list(map(int, input().split()))

c = list(map(int, input().split()))

heap = []

for i in range(n):

    if a[i] >0:

        heapq.heappush(heap, (c[i], i))

for _ in range(m):

    t, d = map(int, input().split())

    t -=1

    total =0

    # Step 1: take from preferred type.

    take = min(a[t], d)

    total += take * c[t]

    a[t] -= take

    d -= take

    if d ==0:

        print(total)

        continue

    # Step 2: take from the heap.

    while d>0:

        # Find the next valid entry.

        while heap:

            current_c, current_i = heapq.heappop(heap)

            if a[current_i] >0:

                # found a valid entry.

                break

        else:

            # No more valid entries.

            total =0

            break

        take = min(d, a[current_i])

        total += take * current_c

        a[current_i] -= take

        d -= take

        # Push back if remaining.

        if a[current_i] >0:

            heapq.heappush(heap, (current_c, current_i))

    # After processing, if d==0, output total. else 0.

    print(total if d ==0 else 0)

Wait, but in the code, after processing step 2, if d==0, then output total. Else, output 0.

But in the code, during step 2 processing:

If the heap is exhausted, then total is set to 0 and break. So, d will still be >0, and the code prints 0.

Else, after taking from the heap, d is reduced by take. So, the loop continues until d is 0.

So, the code correctly outputs 0 if after step 2, d>0.

This code should handle all cases.

But in Python, the heapq module is efficient enough for large inputs?

But for m=1e5, and each customer requiring a few heap operations, yes.

Now, let's test it against the sample inputs.

First sample input:

After initial processing, the heap is built with all 8 entries.

First customer: t=2 (0-based 1) d=8.

Step 1: take 6 (a[1] is 6), total becomes 6*3=18. d=2.

Step 2: process the heap.

Heap entries after initial step 1 are all 8 types except a[1] is 0. So, when the heap is processed:

The first popped entry is (2,3) (type 4, a=1). take 1 dish. total becomes 18+2=20. a[3] becomes 0.

Then, d=1. Next popped entry is (2,5) (type 5, a=5). take 1, total becomes 22. a[5] becomes 4. Push back (2,5) into heap.

d=0. So output 22.

Which matches the sample.

Second customer: t=1 (0-based 0), d=4.

a[0] is 8. take 4. a[0] becomes 4. total is 4*6=24. output 24.

Third customer: t=4 (0-based 3) which has a_i=0. So step 1 takes 0. Then step 2:

The remaining d=7.

Process heap:

Popped entries until find a valid one.

The current heap has entries like (2,5), (2,7), etc.

First valid entry is (2,5) (type 5, a=4). take min(7,4)=4. total +=4*2=8. d=3. a[5] becomes 0. Push nothing.

Next popped entry is (2,7) (type 8, a=5). take 3. total +=3*2=6. a[7] becomes 2. Push back (2,7) into heap. d=0. total is 14.

Which matches the sample.

Fourth customer: t=3 (0-based 2), d=4.

a[2] is 2. step 1 takes 2. total +=2*3=6. d=2.

step 2: process heap.

Heap entries include (2,7) (a=2), (3,2) (a=0), etc.

Next valid entry is (2,7). take 2. total +=2*2=4. a[7] becomes 0. d=0. total is 10.

Fifth customer: t=6 (0-based 5) which is a_i=0. step 1 takes 0.

step 2: process heap.

Current available types are type 0 (a=4), type 6 (a=7), type 4 (a=4), and others.

The first valid entry is (2,5) is gone. The next valid entries:

The heap may have (3,6) (type 7, c=3, a=7). Wait, after previous steps, let's see.

But in the fifth customer's step 2, the code process:

The current heap is built from the previous steps. For example, after the fourth customer, the heap has (3,6) (type 7, a=7), and (6,0) (type 1, a=4), etc.

When processing step 2:

The first popped entry is (3,6) (type 7, a=7). take 7 dishes. sum +=7*3=21. a[6] becomes 0. d is now 10-7=3.

Then, popped next entries until valid.

Next valid entry is (6,0) (type 0, a=4). take 3. sum +=3*6=18. a[0] becomes 1. Push back (6,0) into heap. d=0. total is 21+18=39.

Which matches the sample.

Thus, the code works.

Now, edge cases.

Second sample input:

6 6

a = [6,6,6,6,6,6]

c = [6,66,666,6666,66666,666666]

Each customer orders their own type. The first five customers order 6 dishes each. The sixth orders 66.

The first five customers take all their preferred type's dishes (6 each), sum is 6*6=36, 6*66=396, etc. The sixth customer has d=66, but after the first five customers, the sixth type has a=6. So step 1 takes 6. d becomes 60. Step 2: no more dishes (all types are exhausted). sum is 0.

So code outputs 36, 396, 3996, 39996, 399996, 0.

Which matches the sample.

Third sample input:

The code should handle cases where a customer takes from multiple types in step 2.

For example, the second customer orders 13 dishes. After taking 6 from type 2 (66*6=396), they have 7 remaining. The next types are type 3 (666*6=3996), then type 4 (6666*1=6666). sum 396+3996+6666=11058.

The code should correctly process this.

Thus, the code should handle all cases correctly.

Therefore, the code provided is correct and efficient enough.
</think>

```python
import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
heap = []
for i in range(n):
    if a[i] > 0:
        heapq.heappush(heap, (c[i], i))

for _ in range(m):
    t, d = map(int, input().split())
    t -= 1  # convert to 0-based index
    total = 0
    # Step 1: Try to take from the preferred type
    take = min(a[t], d)
    total += take * c[t]
    a[t] -= take
    d -= take
    if d == 0:
        print(total)
        continue
    # Step 2: Take from the cheapest available
    while d > 0:
        # Find the next valid entry in the heap
        valid = False
        while heap:
            current_c, current_i = heapq.heappop(heap)
            if a[current_i] > 0:
                valid = True
                break
        if not valid:
            total = 0
            break
        take = min(d, a[current_i])
        total += take * current_c
        a[current_i] -= take
        d -= take
        if a[current_i] > 0:
            heapq.heappush(heap, (current_c, current_i))
    print(total if d == 0 else 0)
```