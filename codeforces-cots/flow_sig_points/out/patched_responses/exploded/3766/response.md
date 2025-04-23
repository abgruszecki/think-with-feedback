<think>
Okay, let's try to figure out how to solve this problem. The problem involves processing multiple queries on a list of integers, and each query can modify the numbers in a certain range [l, r] using bitwise operations (AND, OR, XOR) or count the distinct numbers in a range. The constraints are tight, with n up to 2e5 and q up to 1e5, so we need an efficient approach.

First, the naive approach of iterating through all elements for each query would be O(n) per query, which would be 2e5 * 1e5 = 2e10 operations. That's way too slow. We need a smarter data structure here.

Let me think about the operations. The key is that each operation applies to elements in a certain value range [l, r]. So we need a way to group elements by their current values and efficiently apply these operations to ranges of values. A frequency map that tracks how many times each value occurs comes to mind. Then, for each query, instead of iterating over all elements, we iterate over the current existing values and check if they fall into [l, r]. For those that do, we apply the operation and update the frequency map accordingly.

But even this might not be efficient enough. For example, if we have a lot of unique values, each query might involve iterating through many entries in the frequency map. However, since the possible values are up to 2^20 (about a million), but in practice, after some operations, the number of unique values might stay manageable, especially since AND/OR/XOR can reduce the number of bits set. So using a dictionary to track frequencies is feasible.

Let's outline the steps:

1. Maintain a frequency dictionary (like a Python defaultdict) that keeps track of how many times each value exists in the array.
2. For each query of type 1-3:
   a. Iterate through all current values in the frequency dict.
   b. For each value v in [l, r], apply the operation (AND, OR, XOR) with x, compute the new value, and update the frequency dict.
   c. Remove the old value from the frequency dict and add the new value with the appropriate count.
3. For a query of type 4:
   a. Sum the counts of all values in [l, r] and return the number of distinct such values.

Wait, but the problem for type 4 is to output the number of distinct integers in the range [l, r]. So we need to count how many unique values in the frequency dict are between l and r. So for that, we can iterate through all keys in the frequency dict and check if they are in [l, r], then count them. However, if the frequency dict has a lot of keys, even this could be O(M) per query, where M is the number of unique values. For M up to a million, and q up to 1e5, that's 1e11 operations, which is way too slow.

Hmm, this is a problem. So we need a way to efficiently count the number of distinct values in a certain interval [l, r]. A sorted list of the keys would allow binary search to find the lower and upper bounds. Then, the count would be the number of elements between those bounds. But maintaining a sorted list is possible, but when applying operations, inserting and removing elements could be O(1) per insertion if we use a balanced tree or something. But in Python, there's no built-in sorted list data structure with O(log n) insertions and deletions. Alternatively, we can use a TreeSet-like structure using the 'bisect' module. Let's see.

Each time we add a new value, we can insert it into a sorted list (using bisect.insort). When removing a value, we can remove it from the list (using list.remove, which is O(n), but that's not acceptable). Wait, no, bisect can find the index, and then delete by index, which is O(1) if we use a list, but deleting from a list is O(n) because elements have to be shifted. So for example, if we have a sorted list and we need to delete an element, we can find its index via bisect_left and then delete it. But if the list has a million elements, each insertion and deletion would take O(n) time, which is 1e6 operations per query. For 1e5 queries, that's 1e11 operations again. Not feasible.

Alternative idea: use a binary indexed tree (Fenwick Tree) or a segment tree to track the presence of values. Since the maximum possible value is 2^20 (about a million), we can preallocate a BIT where each index represents a value. For each value v, the BIT will store 1 if the value exists (i.e., frequency > 0), else 0. Then, a query of type 4 is a range sum query from l to r. However, even 2^20 is 1,048,576, which is manageable for a Fenwick Tree. The Fenwick Tree would support point updates and range sum queries in O(log M) time, where M is the maximum possible value (2^20 here). This seems promising.

So here's the plan:

- Maintain a frequency dictionary (freq) that maps each value to its count.
- Maintain a Fenwick Tree (or BIT) that tracks for each value v whether it exists (i.e., if freq[v] > 0, then 1; else 0). The BIT is used to answer the count of distinct elements in [l, r] quickly.
- For each query:
   - If it's type 1, 2, or 3: process all values in freq that are within [l, r], apply the operation, compute the new value, update freq, and update the BIT as needed.
   - If it's type 4: perform a range sum query on the BIT from l to r and return the sum.

But how do we efficiently find all values in [l, r] to process for the update operations (types 1-3)?

If we have a sorted list of keys (values present in the array), then for each update query, we can find the subset of keys in [l, r] using binary search. For example, sorted_keys is a list that's maintained in sorted order. Using bisect.bisect_left and bisect.bisect_right, we can find the indices of l and r. Then, iterate over the keys in that sublist.

But maintaining a sorted list and modifying it (inserting and deleting elements) efficiently is tricky. For each update operation, when we process a value v in [l, r], applying the operation (like AND x, OR x, XOR x) will change it to a new value. So for each such v, we need to:

1. Remove v from the frequency dict and the sorted list (if after decrementing the count, it becomes zero).
2. Compute new_v = v OP x (OP being AND, OR, XOR).
3. Add new_v to the frequency dict and update the sorted list (if it wasn't present before).

Wait, but when processing the values in the [l, r] range, for each v in that range, we have to:

- Subtract the current count of v from the frequency dict. If the count becomes zero, we need to remove it from the BIT.
- Compute new_v = v OP x.
- Add the count to new_v in the frequency dict. If new_v wasn't present before, add it to the BIT.

But the problem is that for each v in the current keys that are in [l, r], we need to process them, but modifying the sorted list while iterating could cause issues. So perhaps the sorted list should be a separate structure, like a TreeSet, which allows efficient range queries. However, Python's standard library doesn't have such a data structure. Therefore, perhaps using a sorted list and bisect module is the way to go, but with some optimizations.

Alternatively, when processing a query, we can collect all the keys in [l, r] by using the bisect module to find the start and end indices in the sorted list. Then, we can process each of those keys. However, if the sorted list is a Python list, deleting elements from it while iterating can be expensive. For example, if there are 1e5 elements in a certain range, each deletion is O(n), which would be O(1e10) operations for 1e5 queries. That's way too slow.

So this approach is not feasible. Hmm. So perhaps we need a way to track the current keys in a way that allows efficient range queries. Let's think again.

Another approach: since the possible values are up to 2^20 (about a million), but the number of existing keys is dynamic, maybe we can use a segment tree that tracks which ranges have existing keys, and allows us to iterate over all keys in [l, r]. But building such a segment tree would be complex and time-consuming. However, considering that each query of type 1-3 requires processing all keys in [l, r], and each such key can generate up to one new key, the worst case is O(k) per query where k is the number of keys in the range. For example, if each query adds as many new keys as it processes, this could explode the number of keys, leading to O(k) per query and O(qk) total time, which could be up to 1e5 * 1e6 = 1e11 operations. That's too slow.

Wait, but the operations (AND, OR, XOR) can sometimes reduce the number of bits. For example, applying an AND with x can only set bits to 0. Similarly, OR can only set bits to 1. XOR toggles bits. So, perhaps after several operations, the number of unique values can't be too large. For example, after a few AND operations, the numbers might have a lot of zeros in their bits, leading to fewer possible distinct values. But this is not guaranteed, so we can't rely on that.

So, this suggests that the approach of maintaining a frequency dictionary and a sorted list to process the range queries is not efficient enough for the worst case. So what's another way?

Alternative idea: For each query, when you have to apply the operation to all elements in [l, r], instead of processing each element individually, can you represent the elements in a way that allows batch processing? For example, using a binary trie or some other structure that allows applying the operation to a range of values.

Alternatively, maybe for each bit position, track the count of elements that have that bit set. But how would that help with range queries and applying bitwise operations?

Alternatively, consider that the operations can be represented as transformations on the values. For example, AND x, OR x, XOR x can be combined. But since the operations are applied to a subset of elements (those in [l, r]), this might not be feasible.

Another idea: Instead of tracking all elements, group elements based on their current value and apply the operations to those groups. But again, when applying an operation to a group in a range [l, r], we have to check each group's value against l and r.

Let me think again about the data structures. The main challenges are:

1. For queries of type 1-3, efficiently find all existing values in [l, r], process them, and update their counts and the BIT.
2. For queries of type 4, quickly find the number of distinct values in [l, r].

For the second part, the BIT approach seems good. For each value, we can track whether it exists (i.e., count >0). The range query can be answered in O(log M) time, where M is the max value (2^20 here, so log2(M) is 20). That's acceptable.

For the first part, the problem is how to efficiently find all existing values in [l, r]. The sorted list of keys can be used with binary search to get the range. So for each update query, we can get the start and end indices in the sorted list where the values are in [l, r]. Then, we can iterate through those values. However, when we process each such value v, applying the operation (like AND x) would generate a new value. The key is that during this iteration, the list is being modified. So for example, if we have a list of sorted keys and we process each v in the range [l, r], for each v, we need to:

- Remove v from the freq dict and the BIT (if count becomes zero).
- Compute new_v = v OP x.
- Add new_v to the freq dict and the BIT (if it wasn't present before).

But modifying the sorted list while iterating over it can lead to issues, like skipping elements or processing elements that are no longer in the list. So perhaps, during the processing of a query, we need to collect all the existing values in [l, r] first, and then process them one by one. Because once we remove them from the freq dict, they won't be considered in future queries unless added back.

But how do we collect these values? If the sorted list is maintained, then for each query, we can use bisect to find the start and end indices, and collect all the values in that sublist. However, if during the processing, the sorted list changes (because some values are removed and others are added), this could affect the iteration. For example, adding a new value that's within the current [l, r] range might cause it to be processed again in the same query. But that's not correct. Because the new value is the result of the operation applied to an element that was already in the [l, r] range. Wait, but after applying the operation, the new value is generated. For example, if the operation is AND x, and the original v is in [l, r], then new_v is v & x. But if x is such that new_v is still in [l, r], then when we process the next iteration, we may process it again, leading to an infinite loop. Wait, that's a problem.

For example, suppose we have a query that applies AND 3 to the range [0, 3]. Suppose one of the values is 3. Applying AND 3 to 3 gives 3. So the value remains 3, which is in [0,3]. So when we process it again in the same query, we'd apply the operation again, leading to an infinite loop. But that's not possible because during the processing, once we collect all the original values in [l, r], we process them once. The new values (even if they are in [l, r]) are not processed again in the same query. Because the query is to replace the elements that were in [l, r] before the operation. So the correct approach is to process all the original elements in [l, r], apply the operation, and the new values (even if in [l, r]) are not processed again in this query.

Therefore, to correctly process the query, we need to collect all the current values in [l, r] at the start of the query and process those. Any new values added during the processing (from the same query) are not considered in this query's processing.

So, the steps for processing a query of type 1-3 are:

1. Collect all current values in [l, r]. This is done by finding the range in the sorted list using bisect.
2. For each such value v in this list:
   a. Get the count of v (count = freq[v]).
   b. Remove v from the freq dict and from the BIT (if count was 1, then we delete it; else decrement count).
   c. Compute new_v based on the operation (AND, OR, XOR with x).
   d. Add new_v to the freq dict (increment count if exists, else set to count).
   e. Update the BIT: if new_v wasn't present before, add it (if freq[new_v] becomes 1, set BIT at new_v to 1). If v's count becomes zero, remove from BIT.
3. After processing all original v in [l, r], the query is done.

So, the key here is to collect all the original v in [l, r] first, then process them. Any new values added during processing (new_v) are not processed again in this query, even if they are in [l, r].

This approach ensures that each original v in [l, r] is processed once. The new_v may or may not be in [l, r], but they are not processed again in this query.

Now, the challenge is how to collect all the original v in [l, r] efficiently. If the sorted list is maintained, then using bisect to find the indices where the values are between l and r is possible. Then, we can collect those values in a list (say, to_process), which is a copy of the slice of the sorted list. Then, process each v in to_process.

But maintaining the sorted list is expensive in Python because inserting and deleting elements is O(n) per operation. For example, if the sorted list is a standard list and we use bisect.insort to add elements, each insertion is O(n) time. For 1e5 queries, each inserting/deleting up to 1e5 elements, this would be O(1e10) operations, which is way too slow.

So, this approach is not feasible. Therefore, we need an alternative data structure that allows for efficient insertion, deletion, and range queries. In Python, one possible solution is to use a balanced binary search tree, but Python doesn't have a built-in implementation. However, there's a third-party library called 'sortedcontainers' which provides a SortedList data structure with O(log n) insertion and deletion. But since we can't use external libraries in a programming competition, we need to find a way to implement this ourselves or find an alternative approach.

But assuming that we can't use external libraries, we have to find another way. Let's think again.

Alternative approach:

Instead of maintaining a sorted list, we can process the current frequency dictionary's keys each time. For each query of type 1-3, iterate through all keys in the frequency dict and check if they are within [l, r]. For each such key, process it as described before.

But the problem is that the frequency dict can have up to 1e6 keys (since the maximum possible value is 1e6). For each query, this would be O(M) time, where M is the number of keys in the frequency dict. If M is up to 1e6 and there are 1e5 queries, this is 1e11 operations, which is way too slow.

So this approach is also not feasible.

Hmm. So what else can we do?

Let's think about the properties of the operations. For each query, the operation (AND, OR, XOR) is applied to elements in a certain value range. So, perhaps, for each possible bit, we can track the number of elements that have that bit set. But I'm not sure how to use that for the operations. For example, applying AND x would clear certain bits in the elements in the range. But how does that affect the counts of the elements? It's not straightforward.

Alternatively, consider that each operation modifies the elements in a certain way. For example:

- AND x: for each element v in [l, r], v becomes v & x. So any bit set in v that is not set in x will be cleared.
- OR x: any bit set in x will be set in v.
- XOR x: each bit in v is toggled if the corresponding bit in x is set.

But applying these operations to elements in a range [l, r] is challenging. However, perhaps we can model the possible values and track their frequencies using a segment tree or binary indexed tree. But I'm not seeing how.

Another Idea: Note that after applying AND, OR, or XOR, the new value can be represented as a function of the original value. For example, applying AND x to v gives new_v = v & x. Similarly for the other operations. So, when processing a query, for all elements in [l, r], their new values are determined by their original values and x.

But the problem is that the range [l, r] is based on the original value, not the new value. So for each element v in the original array, if v is in [l, r], then it is transformed. Otherwise, it remains the same.

But for the BIT-based approach for query type 4, we need to track the existence of values after all operations. So, perhaps the frequency dictionary approach is necessary, but we need to find a way to process the range [l, r] in O(k) time, where k is the number of elements in the range, but in a way that k is manageable.

Wait, but for each query, the number of elements processed is the number of unique values in [l, r] at the time of the query. Let's call this K. For example, if the frequency dict has K keys in [l, r], then each query of type 1-3 will process K entries. The total time for all such queries is the sum of K across all queries. If K is small on average, then this approach could work. For example, if each query processes K=100 keys, then 1e5 queries would be 1e7 operations, which is manageable. However, in the worst case, K could be up to 1e6 for each query, leading to 1e11 operations. So this depends on the problem constraints.

But given that the time limit is 4 seconds (around 4e8 operations), we need an approach that can handle up to 4e8 operations. So if the sum of K across all queries is around 4e8, it's manageable. But what's the worst-case scenario for K?

For example, if each query is type 1, and x is 0xfffff (all bits set), then AND x will leave the values unchanged. So if the original values are in [l, r], they will remain, leading to processing them again in the next query. But this is a problem because each time the query processes the same values again. But in this case, the new values are the same as the old, so after the first processing, the counts are not modified. So in the next query, the same K elements are processed again. This would be O(K) per query, which could be 1e6 * 1e5 = 1e11 operations.

Thus, this approach is not feasible in the worst case.

Alternative Idea: Use a binary trie structure to track the values and allow efficient range queries. A binary trie (or a binary indexed tree) can help in quickly finding the counts for a range, but it's unclear how to apply the bitwise operations to ranges of values.

Alternatively, since the maximum possible value is 2^20, which is manageable, perhaps we can precompute the ranges for each possible value and track them. But this also seems challenging.

Wait, another Idea: Since the possible values are up to 2^20, which is about a million, maybe we can use a segment tree that tracks the frequency of each value. Each node in the segment tree represents a range of values and stores the count of numbers in that range. For query type 4, we can query the segment tree for the sum in [l, r], but to count distinct values, the sum would need to be the number of distinct values in [l, r]. But a regular segment tree for sum would not track the distinct count. So this approach isn't directly applicable.

Alternatively, the segment tree can track for each leaf node (value) whether it's present (1 if present, 0 otherwise), and each internal node stores the sum of its children. Then, a query for type 4 is a sum over [l, r], which gives the number of distinct values in that range. This is exactly the same as the BIT approach. The segment tree can handle this in O(log M) time, same as BIT. So perhaps using a segment tree here is an alternative.

But the main problem is handling the queries of types 1-3. For these, we need to process all values in [l, r], apply the operation, and update the frequency dict and the segment tree.

So the main issue remains: how to process all values in [l, r] efficiently for each query.

Another Idea: Since the values are up to 2^20, for each query of type 1-3, we can iterate through all possible values in [l, r] and check if they are present in the frequency dict. But this is O(r-l+1) per query, which could be up to 2^20 (a million) operations per query. For 1e5 queries, this is 1e11 operations, which is way too slow.

No, that's not feasible.

Alternative Idea: Use a binary search on the sorted list of keys to find the subset [l, r], but in a way that doesn't require maintaining a sorted list. For example, whenever we add or remove a key from the frequency dict, we also maintain a list that is kept sorted. This is possible, but as discussed earlier, the insertion and deletion are O(n) operations, which is not feasible.

So what's the solution?

Perhaps the key is to realize that the number of unique values after applying the operations is not too large. For example, each bitwise operation can reduce the number of unique values. For instance:

- AND x: for a given x, this operation can merge multiple values into the same new value. For example, if x has a certain bit pattern, applying AND will set some bits to 0, which can cause multiple different values to become the same.
- OR x: similar logic.
- XOR x: this can increase the number of unique values, but only if applied to different ranges. However, in some cases, applying XOR to a range might not create too many new values.

If we can rely on the number of unique values K being small, then iterating through the keys in [l, r] for each query is manageable. But the problem statement allows for up to 2^20 possible values, which is 1 million. So this approach is not guaranteed to work.

Another Idea: Maybe the problem can be handled using a binary search approach. For each query of type 1-3, we can precompute the possible new values based on the operation and x. For example, AND x will only decrease the value, OR x will increase, etc. But I'm not sure how this helps.

Alternatively, think about the possible operations and their effects:

- AND x: new_v = v & x. This can only leave the bits of x set. So, for example, if x is 5 (binary 101), then any new_v after AND with x will have bits only where x has bits. So the new_v is a subset of x's bits.

- OR x: new_v = v | x. This can set bits in x, so new_v will have at least the bits set in x.

- XOR x: new_v = v ^ x. This toggles the bits where x has bits set. So the new value depends on the original v and x.

But how can we exploit this?

Maybe for certain operations, we can track the possible values more efficiently. For example, if we apply AND x multiple times, the values will eventually stabilize. But this requires tracking the current state of each value.

Alternatively, use a binary decision diagram or similar structure to track the possible values. But this seems complicated.

Another Idea: For each value v in the frequency dict, we can track it in a way that allows us to quickly apply the operation. For example, if we have a bitmask that represents which bits are allowed to be modified. But I'm not sure.

Alternatively, we can model the current set of values as a collection of intervals. For example, after certain operations, the values might form intervals that can be represented efficiently. But this depends on the type of operations and their sequence.

But in the worst case, this approach could still require many intervals, leading to O(k) per query processing.

Hmm. I'm stuck. Let's look for hints in the problem statement.

The constraints are that each a_i is up to 2^20 (so 1 million possible values). The queries are up to 1e5, and the time limit is 4 seconds. So per query, we can afford up to around 4e4 operations (4e8 total).

Wait, 1e5 queries * 4e3 operations per query is 4e8. So if the per-query processing time is O(K), where K is the number of unique values in [l, r], then as long as K is up to 4e3 on average, this would fit.

But how can K be kept small? Because the operations can create new values, which may or may not be merged.

For example, if you apply AND x to a range of values, the new values are v & x. If x has a lot of 0 bits, this reduces the possible values. So, for example, if x is 3 (binary 11), then applying AND x to any value v will result in v & 3, which has only 4 possible values (0, 1, 2, 3). So after this operation, the number of unique values in the array could reduce significantly.

Similarly, OR x with x being large will set many bits, leading to possibly fewer unique values.

XOR x is more unpredictable, but if x has a pattern, it can lead to new values that may or may not merge.

Therefore, perhaps in practice, after several operations, the number of unique values K remains manageable. However, in the worst case, K could still be up to 1e6, leading to O(1e6 * 1e5) = 1e11 operations, which is way too slow.

So, given this, the only viable approach is to find a way to process each query in O(1) or O(log M) time. But how?

Let me think of the problem differently. For each query of type 1-3, we need to apply a bitwise operation to all values in [l, r]. Suppose we can find a way to represent these operations as transformations on the entire array. For example, using a binary mask that tracks how the current values are transformed.

But the problem is that the transformations are applied only to elements that are in a certain range of their values, not their indices. This makes it challenging.

Wait, but the elements are static in terms of their positions. No, the problem statement says that the operations apply to the elements based on their values, not their indices. So after the operations, the elements can change their values, but their indices are irrelevant. So the elements are just a multiset of values.

So, the key insight here is that the elements are treated as a multiset, and the operations are applied to subsets of this multiset based on their values. So the problem is to track this multiset and perform these updates efficiently.

Another Idea: For each possible value v, track how many times it appears. Then, for a query that affects [l, r], iterate through all v in [l, r] and apply the operation to each. But again, this is O(M) per query, which is not feasible.

Alternative Idea: Precompute for each possible operation and x, the mapping from v to new_v, and track the counts in a way that allows bulk processing. For example, when applying AND x to all v in [l, r], the new_v is v & x. So for each v in [l, r], the count for v decreases by its frequency, and the count for v & x increases by the same amount. So, for each query, we need to find all v in [l, r] and compute new_v = v OP x, then update the counts.

But again, this requires iterating through all v in [l, r], which can be up to 1e6 per query.

So, perhaps the only way is to proceed with this approach and hope that in practice, the number of unique values in [l, r] per query is small. Let's proceed with this approach and see if it can pass within the time constraints.

So, the steps are:

1. Maintain a frequency dictionary (freq) that maps each value to its count.
2. Maintain a sorted list (sorted_values) of the unique values in ascending order. This is maintained using bisect.insort and bisect to find indices.
3. For each query of type 1-3:
   a. Use bisect to find the indices of l and r in sorted_values.
   b. Extract the slice of sorted_values that contains values between l and r.
   c. For each value v in this slice:
      i. Get the current count (cnt) of v.
      ii. Remove v from freq. If the count becomes zero, remove it from sorted_values and update the BIT.
      iii. Compute new_v based on the operation.
      iv. Add new_v to freq. If it wasn't there before, add it to sorted_values and update the BIT.
4. For queries of type 4, perform a range sum on the BIT from l to r.

The main problem is maintaining the sorted_values list. Each insertion and deletion is O(n) time, which is too slow for large n. But if the number of unique values K is small, this could be manageable.

But in Python, even for K=1e4, inserting into a list using bisect.insort would take 1e4 * 1e5 = 1e9 operations (since each insertion is O(K)), which is way too slow.

Therefore, this approach is not feasible.

So, what's the alternative?

Perhaps, we can represent the sorted_values list as a binary search tree. But without using external libraries, implementing a balanced BST is very time-consuming and error-prone. However, given the time constraints of the competition, perhaps this is the way to go.

Alternatively, perhaps we can use a treap or a skip list. But again, implementing this from scratch is not trivial.

Another Idea: Since the possible values are up to 2^20, we can use a binary indexed tree (BIT) or a segment tree to track which values are present. Then, to find the next value in the range [l, r], we can perform a binary search using the BIT. For example, to find the smallest value >= l, we can use binary search. However, this requires a way to find the next present value in the range.

This approach is possible. Let's think about it.

The BIT can track the count of present values. For example, the BIT is of size 2^20. Each position is 1 if the value is present, 0 otherwise. Then, the sum from 0 to x gives the number of present values up to x.

To find all values in [l, r], we can use a technique where we find the first value >= l, then find the next value, and so on until we exceed r.

How to find the first value >= l:

This can be done using a binary search approach. For example, we can start with low = l and high = 2^20 -1. Then, check if there is any value in [l, mid]. If yes, adjust high, else adjust low. But this is O(log M) per step.

Alternatively, we can use a binary search on the BIT to find the first value >= l. For example, this can be done using the standard algorithm for finding the smallest index with a cumulative sum >= a certain value.

Once we find the first value >= l, we can iterate through the values using the same method until we exceed r.

This way, each query of type 1-3 can iterate through the values in [l, r] using the BIT's structure, without needing to maintain a separate sorted list.

So, the steps for processing a query of type 1-3 would be:

1. Find all values in the BIT within [l, r].
2. For each such value v:
   a. Get the count from freq.
   b. Remove v from freq and the BIT.
   c. Compute new_v.
   d. Add new_v to freq and the BIT.
3. Repeat until all such v are processed.

The key is to efficiently iterate through all values in [l, r] using the BIT.

But how to find all values in [l, r] using the BIT? For this, we can use a method to find the next value after a given position. For example, starting from l, find the smallest value >= l. Then, find the next value after that, and so on, until we exceed r.

To find the next value, we can use a binary search approach. For example, the function to find the first occurrence >= a certain index can be implemented.

But how to efficiently find all values in [l, r]?

I found a way to find the smallest value >= l using a binary search on the BIT. Here's how:

The standard approach to find the smallest index >= l where the value is present (BIT has a 1) can be done by using the BIT's prefix sums. We can check if there's any value in [l, r] by querying the BIT's range sum from l to r. If the sum is zero, skip processing. Otherwise, we can proceed to find each value in the range.

For each value v in [l, r], once it's processed, we can find the next value by checking the next position after v. This can be done using a binary search again. But this could lead to O(k log M) time per query, where k is the number of values in [l, r]. For example, if k is 1e5 and log M is 20, this is 2e6 operations per query. For 1e5 queries, this is 2e8 operations, which is manageable.

So, this approach seems feasible.

Let me outline the steps for finding the next value >= current:

function find_next(v, start):
   low = start
   high = M
   while low <= high:
       mid = (low + high) // 2
       sum = bit.query(mid) - bit.query(start-1)
       if sum > 0:
           high = mid - 1
       else:
           low = mid + 1
   return low if low <= M and bit.get(low) else None

But I'm not sure about the exact implementation. Alternatively, there's a standard algorithm for finding the k-th smallest element using a BIT, which could be adapted here.

Alternatively, the following approach can be used:

To find the first value >= l, start from l and check if it's present (bit.get(l) is 1). If yes, return l. Else, use binary search to find the next present value.

But this could be time-consuming. Alternatively, we can use a binary search on the prefix sum. For example, we want the smallest index >= l where the prefix sum up to that index is greater than the prefix sum up to l-1. If the prefix sum up to l-1 is S, then the first index where the prefix sum exceeds S is the first value >= l.

So, the code would look something like:

def find_first(l):
    s = bit.query(l-1)
    low = l
    high = MAX_VAL
    res = -1
    while low <= high:
        mid = (low + high) // 2
        current_s = bit.query(mid)
        if current_s > s:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res if res != -1 and res <= MAX_VAL else None

This function finds the smallest value >= l by checking where the prefix sum increases beyond the sum up to l-1. If such a value exists, it returns it.

Once we have the first value >= l, we can then find the next value by calling find_first(v+1), and so on, until we exceed r.

So, for each query of type 1-3:

- current_v = find_first(l)
- while current_v != None and current_v <= r:
   process current_v
   current_v = find_first(current_v + 1)

This way, we iterate through all values in [l, r], but each step requires O(log M) time.

For each such current_v:

- Retrieve its count from the freq dict.
- Remove current_v from the freq dict (if count is 1, delete it from freq and update the BIT by setting current_v to 0).
- Compute new_v based on the operation and x.
- Add new_v to the freq dict (increment count if exists, else set to 1 and update the BIT by setting new_v to 1 if it wasn't present before).

This approach would have a time complexity of O(k log M) per query, where k is the number of values in [l, r]. For each value, we spend O(log M) time to find it and then process it. Processing it involves updating the BIT and freq dict, which are O(1) (for the freq dict) and O(log M) for the BIT updates (since adding or removing a value requires updating the BIT at that position).

So for each value in [l, r], we spend O(log M) time to find it, and O(log M) time to process it (updating the BIT twice: once to remove the old value and once to add the new value). So total time per query is O(k * log M).

If k is up to 1e5 per query, then for 1e5 queries, this would be 1e5 * 1e5 * 20 = 2e9 operations, which is too slow for 4 seconds (4e9 operations possible). However, in practice, k may be much smaller, especially after applying AND/OR operations that reduce the number of unique values.

So, this approach could work.

Now, let's think about the implementation details.

The BIT will be of size 2^20 (1,048,576). Each update (add or remove) is O(log M). The find_first function is O(log M) per call.

The freq dict is a normal dictionary that maps values to their counts.

For each query of type 1-3:

- Iterate through all values in [l, r] using the find_first method.
- For each value v in this range:
   - Get the count from freq[v].
   - Decrement the count. If it becomes zero, delete v from freq and update the BIT by setting v to 0.
   - Compute new_v = v OP x (based on the query type).
   - If new_v is not in freq, add it with count 1 and update the BIT by adding 1 at new_v. Else, increment the count in freq.

Wait, no. Because when processing a value v, we need to remove all its occurrences (since the operation is applied to all elements in [l, r] that are equal to v). So, for example, if the frequency of v is 5, then all 5 elements are transformed to new_v. So, the count for v is reduced by 5, and new_v's count is increased by 5.

So, for each v in [l, r], we:

1. Remove all occurrences of v (since the query applies to all a_i with value in [l, r]).
2. Add new_v for each occurrence.

So, for each v in [l, r] and frequency cnt:

- Subtract cnt from freq[v]. If the result is zero, remove v from freq and update the BIT (set to 0).
- Compute new_v = v OP x.
- Add cnt to freq[new_v]. If new_v wasn't in freq before, add it to the BIT (set to 1).

Thus, the steps are:

For each query of type 1-3:

current_v = find_first(l)
while current_v is not None and current_v <= r:
    cnt = freq[current_v]
    del freq[current_v]
    # Remove current_v from BIT
    if BIT.get_sum(current_v, current_v) == 1:
        BIT.update(current_v, -1)
    new_v = compute_new_v(current_v, op, x)
    if new_v in freq:
        freq[new_v] += cnt
    else:
        freq[new_v] = cnt
        # Add new_v to BIT
        if BIT.get_sum(new_v, new_v) == 0:
            BIT.update(new_v, 1)
    # Find next current_v
    current_v = find_first(current_v + 1)

Wait, but the BIT is tracking whether a value is present (1) or not (0). So, when we remove all instances of current_v, we need to check if current_v's frequency is zero. If so, we set the BIT at current_v to 0. Similarly, when adding new_v, if it wasn't present before (frequency was zero), we set the BIT at new_v to 1.

So, for each current_v processed:

- Decrement the frequency. If it becomes zero, we need to check if the BIT should be updated.
   - However, since we are processing all occurrences of current_v (because the query applies to all elements in [l, r], which includes all instances of current_v), we can directly remove current_v from the freq dict and update the BIT.

For example:

current_v is in [l, r]. All cnt elements of current_v are being transformed to new_v. So, current_v's frequency becomes zero (since all are removed), so we must set the BIT at current_v to 0.

Similarly, new_v's frequency increases by cnt. If new_v wasn't present before (freq[new_v] was zero), then we must set the BIT at new_v to 1.

Thus, the code for processing a value v would be:

cnt = freq[v]
del freq[v]
BIT.update(v, -1)  # since v is no longer present

new_v = compute op
if new_v in freq:
    freq[new_v] += cnt
else:
    freq[new_v] = cnt
    BIT.update(new_v, 1)  # since new_v is now present

But how do we check if v was present before updating? Well, since we're processing all occurrences of v in the query, after deleting v from freq, its count is zero, so the BIT is updated to 0.

Then, when adding new_v, if it's not in freq, we add it and update the BIT to 1.

So, the steps are correct.

Now, the BIT needs to support:

- Updating a single position (adding 1 or -1).
- Querying the sum from 0 to x (for find_first function).

The standard BIT implementation can do this. However, the find_first function requires a binary search over the BIT.

Thus, the overall plan is feasible.

Now, let's proceed to code this.

First, implement the BIT:

The BIT will have the following operations:

- update(pos, delta): adds delta to the BIT at position pos.
- query(pos): returns the sum from 0 to pos.

The BIT is 1-based or 0-based? Since the possible values are 0 to 2^20 -1, which is 0-based, the BIT should be 0-based.

Wait, the BIT is typically 1-based. So to handle 0-based indexes, we'll add 1 to each value. For example, the value 0 is stored at index 1 in the BIT, value 1 at index 2, etc. This way, the BIT can handle values up to 2^20 -1 (which is 1,048,575). So the BIT size is 2^20 +1.

The query function returns the sum up to a given value (inclusive). For example, query(v) gives the sum from 0 to v.

The find_first function uses the query to find the smallest value >= l where the sum increases.

Implementing find_first(l) as described.

Now, for each query of type 1-3, we iterate through all values in [l, r] using the find_first method, process each value, and update the BIT and freq dict.

For type 4 queries, we compute the sum from l to r using the BIT's query(r) - query(l-1).

Now, code outline:

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0]*(size + 2)  # 1-based indexing

    def update(self, idx, delta):
        # idx is 0-based, so add 1
        idx += 1
        while idx <= self.size + 1:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        # returns sum from 0 to idx (inclusive)
        idx += 1
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

Then, the find_first function:

def find_first(bit, l):
    max_val = (1 << 20) - 1
    if l > max_val:
        return None
    sum_l_minus_1 = bit.query(l-1) if l > 0 else 0
    low = l
    high = max_val
    res = None
    while low <= high:
        mid = (low + high) // 2
        current_sum = bit.query(mid)
        if current_sum > sum_l_minus_1:
            res = mid
            high = mid -1
        else:
            low = mid + 1
    if res is not None and res <= max_val and bit.query(res) - bit.query(res-1) > 0:
        return res
    return None

But wait, after finding the 'res', we need to check if it's actually present. Because the query might return a position where the sum increased, but that could be due to a previous value. So the binary search finds the first position where the prefix sum increases, but we need to verify that the value at that position is indeed present.

Alternatively, the BIT's query(res) - query(res-1) gives the presence of res. If it's 1, then res is present.

Thus, after finding res, check if it's present. If not, return None.

But this could add some overhead. However, the binary search should find the correct position, but perhaps due to the way the BIT works, it might not. So this check is necessary.

Alternatively, during the binary search, ensure that the res is indeed present.

But this is getting complicated. Let's proceed with the code as outlined.

Now, implementing the query processing:

Read n and q.

Read the initial array.

Initialize freq as a defaultdict(int), and populate it with the counts of each a_i.

Initialize the BIT. For each value in the initial array, if freq[v] > 0, update the BIT with +1 for v.

Wait, no: the BIT tracks whether a value is present (i.e., has a count > 0). So, during initialization:

for v in a:
    freq[v] += 1

Then, for each key v in freq:
    bit.update(v, 1)

But since a can have multiple instances of the same v, but we need to set the BIT once per unique v.

Alternatively, during the initial processing, for each v in a, we can update the frequency and then update the BIT accordingly. But to avoid multiple updates for the same v, perhaps first build the freq dict, then for each key in freq, update the BIT with 1.

Yes, that's better.

So code:

from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))
freq = defaultdict(int)
for num in a:
    freq[num] += 1

max_val = (1 << 20) - 1
bit = BIT(max_val)

for v in freq:
    bit.update(v, 1)

Then, process each query:

Testing against sample input 1.

```python
from collections import defaultdict


class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)  # 1-based indexing

    def update(self, idx, delta):
        idx += 1  # convert to 1-based
        while idx <= self.size + 1:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        idx += 1  # convert to 1-based
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def find_first(bit, l):
    max_val = (1 << 20) - 1
    if l > max_val:
        return None
    sum_l_minus_1 = bit.query(l - 1) if l > 0 else 0
    low = l
    high = max_val
    res = None
    while low <= high:
        mid = (low + high) // 2
        current_sum = bit.query(mid)
        if current_sum > sum_l_minus_1:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    if res is not None and res <= max_val:
        # Check if res is actually present
        check = bit.query(res) - (bit.query(res - 1) if res > 0 else 0)
        if check > 0:
            return res
    return None

def main(input_stream, output_stream):
    import sys
    input = input_stream.read
    data = input().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    q = int(data[ptr])
    ptr += 1

    a = list(map(int, data[ptr:ptr + n]))
    ptr += n

    freq = defaultdict(int)
    for num in a:
        freq[num] += 1

    max_val = (1 << 20) - 1
    bit = BIT(max_val)
    for v in freq:
        bit.update(v, 1)

    for _ in range(q):
        t = int(data[ptr])
        ptr += 1
        if t in {1, 2, 3}:
            l = int(data[ptr])
            ptr += 1
            r = int(data[ptr])
            ptr += 1
            x = int(data[ptr])
            ptr += 1

            current_v = find_first(bit, l)
            while current_v is not None and current_v <= r:
                cnt = freq[current_v]
                del freq[current_v]
                bit.update(current_v, -1)

                if t == 1:
                    new_v = current_v & x
                elif t == 2:
                    new_v = current_v | x
                else:
                    new_v = current_v ^ x

                if new_v in freq:
                    freq[new_v] += cnt
                else:
                    freq[new_v] = cnt
                    bit.update(new_v, 1)

                current_v = find_first(bit, current_v + 1)
        else:
            l = int(data[ptr])
            ptr += 1
            r = int(data[ptr])
            ptr += 1

            if l == 0:
                total = bit.query(r)
            else:
                total = bit.query(r) - bit.query(l - 1)
            print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 7
6 0 2 3 2 7
1 0 4 3
2 6 8 4
4 0 7
3 2 5 3
1 0 1 2
4 0 3
4 2 7
""",
            "output": \
"""\
5
1
2
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

Case 2: BIT contains 3.

Looking for l=2.

sum_l_minus_1 is query(1) =0.

low=2, high=3.

mid=2. query(2) is 0. So low=3.

mid=3. query(3) is 1. Res=3.

Yes.

Thus, the find_first function works.

Another case: BIT has values 1,2,4,5.

Looking for l=2.

sum_l_minus_1 = query(1) =1.

The code checks mid between 2 and 5. query(2) is 2. 2>1 → res=2.

High is adjusted to 1. Loop ends. res=2 is correct.

Thus, the code should correctly find the first value.

Therefore, the code should work.

Finally, the code needs to read the input and process the queries correctly. Also, the BIT's update and query functions must be correctly implemented.

But in Python, for the BIT's size of 1e6, the array size is manageable.

Now, let's write the code.
</think>

```python
from collections import defaultdict

class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)  # 1-based indexing

    def update(self, idx, delta):
        idx += 1  # convert to 1-based
        while idx <= self.size + 1:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        idx += 1  # convert to 1-based
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def find_first(bit, l):
    max_val = (1 << 20) - 1
    if l > max_val:
        return None
    sum_l_minus_1 = bit.query(l - 1) if l > 0 else 0
    low = l
    high = max_val
    res = None
    while low <= high:
        mid = (low + high) // 2
        current_sum = bit.query(mid)
        if current_sum > sum_l_minus_1:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    if res is not None and res <= max_val:
        # Check if res is actually present
        check = bit.query(res) - (bit.query(res - 1) if res > 0 else 0)
        if check > 0:
            return res
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    q = int(data[ptr])
    ptr += 1

    a = list(map(int, data[ptr:ptr + n]))
    ptr += n

    freq = defaultdict(int)
    for num in a:
        freq[num] += 1

    max_val = (1 << 20) - 1
    bit = BIT(max_val)
    for v in freq:
        bit.update(v, 1)

    for _ in range(q):
        t = int(data[ptr])
        ptr += 1
        if t in {1, 2, 3}:
            l = int(data[ptr])
            ptr += 1
            r = int(data[ptr])
            ptr += 1
            x = int(data[ptr])
            ptr += 1

            current_v = find_first(bit, l)
            while current_v is not None and current_v <= r:
                cnt = freq[current_v]
                del freq[current_v]
                bit.update(current_v, -1)

                if t == 1:
                    new_v = current_v & x
                elif t == 2:
                    new_v = current_v | x
                else:
                    new_v = current_v ^ x

                if new_v in freq:
                    freq[new_v] += cnt
                else:
                    freq[new_v] = cnt
                    bit.update(new_v, 1)

                current_v = find_first(bit, current_v + 1)
        else:
            l = int(data[ptr])
            ptr += 1
            r = int(data[ptr])
            ptr += 1

            if l == 0:
                total = bit.query(r)
            else:
                total = bit.query(r) - bit.query(l - 1)
            print(total)

if __name__ == "__main__":
    main()
```
