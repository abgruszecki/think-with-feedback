<think>
Okay, let's see. The problem is about a time-traveling multiset. We need to handle three types of operations (add, remove, count) at various times, and each query is processed in the order they are given, but each affects the state of the multiset at a specific time. Then, when a count query is made, it's based on the state of the multiset as of that particular time, considering all operations up to that moment in the timeline.

Hmm. So the key here is that the timeline is not processed in the order of their actual times. Instead, each operation is applied at a certain time ti, and when we process the queries (in the order given), we need to track the state of the multiset at various times. For example, adding an element at time t=5, then a count at t=6 would include that addition. But if someone later goes back and adds an operation at t=3, that would affect all future count queries after that operation, but only for times after t=3.

Wait, no. The problem says that Artem is applying these operations in the given order. So each query is executed in the order of the input lines. Each such operation is a modification (add or remove) or a query (count) that's applied to the timeline. So the timeline is built incrementally as we process each input line. Each add or remove affects the state of the multiset at time ti. Then, when a count query comes, it's for the state at time ti, considering all previous operations (from the input order) that have time <= ti. But since each new operation may have a time that's earlier than some previous times, the challenge is to efficiently handle these time-based queries.

So the problem reduces to, for each count query (ai=3) at time ti, we need to find out how many adds and removes of xi have been processed up to that point in the input sequence, which have time <= ti. But since each add or remove in the input could have a time that's in any order, we need a way to track, for each xi, all the add and remove events, sorted by their time, so that we can quickly compute the net count (adds - removes) up to a certain time.

So, for each xi, we can maintain two sorted lists (or perhaps a combined list with markers for add or remove) ordered by time. Then, for a count query on xi and time ti, we perform a binary search in these lists to find how many adds and removes have time <= ti, subtract the two, and that's the count.

But how to efficiently manage this for all possible xi? Since xi can be up to 1e9, we can't preallocate for all possible xi. So a dictionary where the keys are the xi values, and each value is a structure that holds the adds and removes for that xi.

For each xi, we can keep a list of events (adds and removes) sorted by time. Wait, but the events (adds and removes) for a given xi can be processed in the order of their occurrence in the input. However, the time of the events may not be in order. So, when a new add or remove comes in for xi, we need to insert it into the correct position in a sorted list. But inserting into a list can be O(n), which is bad if there are many operations for the same xi. So, for each xi, we need to maintain the list of events sorted by their time. But inserting into a sorted list is O(n) time unless we use a data structure that allows for efficient insertion, like a balanced binary search tree. However, in Python, the standard data structures don't include such a structure. So perhaps we can instead keep a list that's always kept sorted, and use the bisect module to find the insertion point. But inserting into a list is O(n) time, which would be too slow for 1e5 operations.

Wait, but each event (add or remove) for a given xi is unique in time, since the problem states that all ti are distinct. So for each xi, the events are added in the order they appear in the input, but their times can be in any order. Therefore, to maintain a sorted list for each xi's events, when a new event comes, we can use bisect to find where to insert it in O(log k) time, where k is the number of events for that xi. Then, inserting into the list would require O(k) time, which is not feasible if k is large. For example, if a particular xi has 1e5 operations, each insertion would take O(1e5) time, leading to O(1e10) operations total.

This is a problem. So we need a data structure that allows us to maintain a sorted list of events (sorted by time) for each xi, and allows for efficient insertion and querying. Since in Python, lists are not efficient for this, perhaps we can use a binary indexed tree (Fenwick tree) or a segment tree. Alternatively, since the events are inserted in arbitrary time order but need to be sorted for queries, maybe we can use a list and append all events, and then sort them once, but since events are processed incrementally, that's not possible.

Wait, but the events are processed in the order given. For example, the first event could have ti=100, the next ti=50, and so on. So for each xi, the events are added in the order of the input lines, but their ti's can be in any order. However, each event must be inserted into the sorted list of ti's for that xi. So for each xi, when processing an add or remove, we need to insert the ti into the correct position in the list. But inserting into a list is O(k) time. Which would be O(n^2) time in the worst case, which is not acceptable for n=1e5.

Hmm. So we need a better way. Let's think: For each xi, we can maintain two separate sorted lists: one for add events, and one for remove events. Because for a count query, the number of adds up to time ti is the number of add events with time <= ti, minus the number of remove events with time <= ti. So for each xi, we can track all the add and remove times in sorted order. Then, for a query, we can compute the number of adds and removes up to ti, subtract them.

Yes. So for each xi, when an add (ai=1) comes in, we insert ti into the adds list, maintaining it in sorted order. Similarly, for a remove (ai=2), insert ti into the removes list. Then, for a count query (ai=3), we need to find the number of adds up to ti and subtract the number of removes up to ti. Since the lists are sorted, we can perform binary search to find the counts quickly.

But how do we maintain the adds and removes lists in sorted order as we process each event, given that the ti's can come in any order?

Ah, for each xi, when a new add event comes, we can use the bisect module to find the insertion point in the adds list (which is kept sorted), and then insert it. Similarly for removes. Since inserting into a list is O(k), where k is the length of the list for that xi, this approach would be O(n) per insertion in the worst case (if all events are for the same xi), leading to O(n^2) time, which is too slow for n=1e5.

So this approach isn't feasible. Need a better way.

Alternative idea: since all ti are distinct and can be up to 1e9, but for each xi, the adds and removes are processed in the order of the input lines. However, each new event's ti can be in any order. So perhaps using a binary search tree data structure for each xi's adds and removes. But in Python, there's no built-in sorted list or tree structure that allows for O(log k) insertion and O(log k) queries.

Wait, but maybe there's a way to use a list and keep it sorted, but for each insertion, use bisect.insort, which inserts in O(k) time. But for n=1e5 and each insertion taking O(k) time, this would be O(n^2) time in the worst case, which is not feasible. So this approach is not efficient enough.

Hmm. So what's the alternative? Let's think of the problem differently. For each xi, we can track all the events (add and remove) in a sorted list. Then, for a count query, we need to process all events up to the given time ti, but in the order of their actual times.

Wait, but the events are applied in the order of their insertion. Wait no: the problem states that each operation is applied at a certain time. So the actual timeline is the collection of all events (adds and removes) sorted by ti. Then, when a count query comes for time ti, it's the sum of all adds with ti <= query_time minus all removes with ti <= query_time.

But since the events are added in arbitrary order (the input order), but the ti's are unique and can be in any order, the key is that for each xi, the adds and removes are a collection of times, and for a query on ti, we need the number of adds <= ti and subtract the number of removes <= ti.

So for each xi, we can have a list of adds (sorted) and a list of removes (sorted). Then, for a query ti, the count is (bisect_right(adds, ti) - bisect_right(removes, ti)).

But to maintain the adds and removes lists as sorted, each insertion (for add or remove) must be inserted in the correct position.

But the problem is that inserting into a list is O(k), which is expensive for large k. So this approach would be O(n^2) time in the worst case.

So for this problem, the constraints are n up to 1e5, so O(n log n) per operation is acceptable, but O(n) per operation is not.

So what's another approach?

Alternative idea: use a dictionary for each xi, where for each xi, we have a list of events (add or remove) sorted by ti. Since we can process events for a xi in any order, but we need to maintain the list sorted, perhaps when we process an event (add or remove) for xi, we can insert it into the list in O(1) time if the list is being maintained in a way that allows for that. But that's only possible if the events are processed in order of ti, which they are not.

So this seems like a dead end.

Wait, perhaps the key insight here is that when the count query is made, the current state of the multiset as of time ti is determined by all add and remove events for xi that have a time <= ti. But since these events can be processed in any order (because the input order is arbitrary), but each add or remove is processed in the input order, the problem is to manage for each xi the adds and removes sorted by their ti.

But how to do that efficiently.

Another idea: for all events (add and remove), we can track them in a global list sorted by ti, but for each xi, track the indices where the events for xi are. But that's not helpful for per-xi queries.

Wait, perhaps a better approach is to use a dictionary where for each xi, we have two arrays: adds and removes, which are kept sorted. Each time we add an event (add or remove), we use bisect.insort to insert the ti into the respective array. Then, for a count query, we perform a bisect on each array to find the number of events <= ti.

The problem with this approach is that bisect.insort is O(k) time per insertion, which is not acceptable for large k. For example, if there are 1e5 add events for the same xi, each insertion is O(1e5), leading to O(1e10) operations, which is way too slow.

So this approach won't work.

So, we need a data structure that allows for O(log k) insertions and O(log k) queries for the number of elements <= a given value.

In Python, the only way to do this is to use a list that's kept sorted and use binary search for insertions and lookups. But as discussed earlier, this leads to O(k) insertion time.

Alternative approach: Since the ti's are unique and can be up to 1e9, perhaps we can use a Binary Indexed Tree (Fenwick Tree) or a Segment Tree for each xi. But since xi can be up to 1e9, it's impossible to preallocate a Fenwick Tree for each xi. So the alternative is to dynamically manage the Fenwick Trees for each xi as needed.

But even then, for each xi, we need to manage two Fenwick Trees: one for adds and one for removes. However, the ti's are up to 1e9, so we can't directly index them. So we need to coordinate compress the ti's for each xi. But since each xi can have a different set of ti's, this is not feasible.

Wait, but for each xi, the adds and removes have their own ti's. So for each xi, when processing the events, the ti's are unique. But when xi is different, ti's can overlap. For example, xi=5 and xi=3 can both have events at ti=10.

Hmm. So for a given xi, the adds and removes have ti's that are unique for that xi. Wait no, because different xi's can have events at the same ti. But for a particular xi, the events (add or remove) can have ti's that are in any order. However, for a specific xi, the same ti can't appear more than once because all ti in the input are distinct. So for each xi, all events (add or remove) have unique ti's.

Therefore, for each xi, the ti's in the add and remove events are unique. So for a given xi, when inserting a new ti into the add or remove list, we can manage the ti's as a sorted list, but again, insertion is O(k) time.

Alternative idea: For each xi, maintain a list of events (add and remove) in the order they are processed, and for count queries, process all events for that xi up to the query time ti. But since events can be added in any time order, and the count query requires that we consider all events with ti <= query ti, regardless of the order in which they were processed, this is not feasible. For example, if an event with a small ti is added after some events with larger ti's, the count query for a time between those would need to consider it.

So, this brings us back to the original problem: how to efficiently maintain a sorted list of events for each xi.

So, perhaps the solution is to use a data structure that allows for O(log k) insertion and O(log k) queries. In Python, since we don't have a built-in sorted list, perhaps we can use a treap or a balanced BST, but implementing such a structure from scratch is time-consuming and may not be feasible under time constraints.

Alternatively, perhaps using a bisect module and a list, but accept that the time complexity may be O(n log n) on average. Let's consider the worst case. Suppose for each xi, all events are processed in increasing order of ti. Then inserting each event is O(1) (appending to the end). But if events are processed in reverse order (highest ti first), each insertion is O(k) for the first insert (since inserting into the beginning). So for n events, this would be O(n^2) time, which is not acceptable.

But given that the problem constraints are tight (n=1e5), this approach is not feasible. So, what's the alternative?

Wait, perhaps we can represent the adds and removes for each xi as a list, but not keep them sorted. Instead, when processing a count query for ti, we can collect all the add and remove events for xi, sort them, and then compute the count. But this would require O(k log k) time per query, which is again not feasible for k up to 1e5 and queries up to 1e5.

Hmm. So this approach is also not feasible.

Another idea: The problem requires that for each count query, we process all previous events (add and remove) for xi, regardless of their ti's, and compute the number of adds and removes with ti <= query ti. So, for each xi, the events (add and remove) are processed in the order of the input lines. For each xi, we can track all events in the order they are added, but when a count query is made, we have to go through all events for that xi, check their ti's, and count how many adds and removes are <= the query ti. But this would be O(k) per query, which is again O(n^2) in the worst case.

So this is not feasible.

Alternative approach: Since all ti's are unique and the events are processed in the order of input, which is arbitrary, but for each count query, we need to find the number of adds and removes for a specific xi with ti <= query ti. So, for each xi, we need to track all adds and removes, and for each, their ti's. Then, for a query, we can perform a binary search to find the count.

But the problem is inserting into a sorted list is O(k) time. So perhaps the solution is to use a list for each xi's add and remove events, and when inserting a new ti, append it to the list and then sort the list once. But sorting after every insertion is O(k log k) time, which is way too slow.

Alternatively, we can keep the lists unsorted, and for each query, we have to sort them, then perform a binary search. But that's O(k log k) per query, which is also not feasible.

Hmm. So perhaps the only way to handle this efficiently is to use a binary indexed tree (Fenwick Tree) for each xi's add and remove events. But how?

Wait, for each xi, we can map the ti's to their rank in a sorted list of ti's. For example, for all add events of xi, we can maintain a sorted list. Then, when inserting a new ti, we can find its position using bisect.insort. But inserting into the list is O(k). However, if we also have a Fenwick Tree that tracks the counts, then for each insertion, we can update the Fenwick Tree. But the problem is that the Fenwick Tree's indices need to correspond to the sorted order.

Alternatively, for each xi, when we process an add event with ti, we can insert it into a Fenwick Tree for xi's adds, where the Fenwick Tree is built on the sorted list of ti's. Similarly for removes.

But how to do this dynamically. Let's think.

For example, for a given xi, when the first add event comes with ti=5, we can create a Fenwick Tree of size 1. Then, when another add event comes with ti=3, which is inserted before 5 in the sorted list. The Fenwick Tree needs to be able to handle this. But dynamically building a Fenwick Tree is challenging. Fenwick Trees are static data structures that work on a fixed range of indices. So this approach may not be feasible.

Alternative idea: use a treap (tree + heap) structure, which allows for O(log n) insertion and query operations. But implementing a treap in Python is possible but time-consuming and may be too slow for the problem's constraints.

Alternatively, use a SortedList from the 'bisect' module, but I recall that there's a third-party library called 'sortedcontainers' which provides a SortedList data structure with O(log n) insertion and O(log n) indexing. However, the problem's code must not use any external libraries. So this is not allowed.

Thus, we need a Python solution using only standard libraries.

Hmm. So, perhaps the only feasible approach is to use a list and bisect.insort, but accept that in the worst case this will be O(n^2), but hope that in practice, with the given test cases, it will pass within the time constraints.

But with n up to 1e5, and each insertion being O(k) time, where k is the number of events for a particular xi, this is only feasible if the average k is small. For example, if each xi is unique, then k=1 for all events, leading to O(n log n) total time. But if there's a test case where all events are for the same xi, then each insertion would take O(1) (if inserted in order) or O(k) (if inserted in reverse order). Wait, if all events are inserted in reverse order (ti in descending order), then each insertion would be at the beginning of the list, which is O(1) for a linked list. But Python's list.insert(0, ...) is O(k) time. So inserting 1e5 elements in reverse order would take O(1 + 2 + 3 + ... + 1e5) = O(5e9) operations, which is way beyond the time limit.

So this approach is not feasible.

Alternative idea: can we process all queries first, collect all ti's for each xi's adds and removes, sort them, and then perform coordinate compression?

Yes, but how?

Let me think. For each xi, collect all the ti's for adds and removes. Then, for each xi, sort the list of ti's for adds and removes. Then, when processing a count query, we can perform a binary search on the sorted list. But since the events are processed in the input order, which may not be in time order, how can we process them incrementally?

Wait, the problem is that we need to process the events (add/remove) in the order they are given, and each count query is part of the input sequence and must be processed after all previous events (from the input) that have ti <= the query's ti.

Wait, no. The count query is processed as part of the input sequence. So each query (whether add, remove, or count) is processed in the input order, and each can affect the state of the multiset. For example, adding an event at ti=5, then a count at ti=6, then adding an event at ti=3. The count at ti=6 would initially return 1 (from the first add), but after the second add at ti=3, which is inserted before the first add, subsequent count queries at ti=4 would return 1, but the count queries that were processed before the second add are not affected.

Wait, but count queries are processed in the input order and depend on all previous events (add/remove) that have been processed before them in the input order, but not the ones after. Because each query (count) is processed immediately as part of the input sequence.

So the count query at time ti must account for all add and remove events that have been processed up to that point (in the input order) with ti <= the query's ti.

So the order in which the events are processed (input order) matters. So, for example, if the input has an add at ti=5, then a count query at ti=6 (which returns 1), then an add at ti=3, then a count at ti=4 (which returns 1), then the two count queries are processed in the order of the input, and the second count query (after the add at ti=3) now includes that add.

Therefore, the count queries are influenced by all previous events (add/remove) in the input order, regardless of their ti's. So, to process each query, we need to consider all events that came before it in the input, but only those with ti <= the query's ti.

So, for each xi, the adds and removes are processed in the input order, but their ti's can be in any order. Therefore, for a count query, we need to sum all adds for xi with ti <= query ti that have been processed before the query in the input order, minus all removes for xi with ti <= query ti that have been processed before the query.

Thus, the events are processed in the input order. For each count query, it's processed after all previous add/remove events (in the input order), and the count is computed based on those events (but only those with ti <= query ti).

So, the problem reduces to, for each xi, maintaining a list of add and remove events in the order they were processed, and for a count query, we need to iterate through all events for xi processed before the query and compute how many adds and removes have ti <= query ti.

But this is O(k) per query, which is not feasible for large k.

So, this approach would be O(nk) time, which is O(n^2) in the worst case.

Thus, this is not feasible.

Hmm. So what's the correct approach here?

Let me think again. For each xi, all adds and removes are events with unique ti's. When a count query is made, the count is the number of adds with ti <= query ti minus the number of removes with ti <= query ti. So for each xi, the count can be computed as (number of adds <= ti) - (number of removes <= ti).

So, for each xi, we need to maintain two sorted lists (adds and removes) of ti's. Then, for each count query, we perform a binary search on each list to find the count.

The problem is maintaining those lists in sorted order as events are added in arbitrary order. The key is to find a way to maintain the sorted lists efficiently for each xi.

In Python, the only way to do this is to use a list and bisect.insort, but that's O(n) time per insertion in the worst case.

But maybe there's a smarter way. Let's consider that all ti's are distinct and can be up to 1e9. For each xi, we can keep the adds and removes in a list, and when inserting, use bisect.insort to insert into the list. For example:

For each add event, insert ti into the adds list for xi using bisect.insort. Similarly for removes.

For a count query, bisect.bisect_right the adds list to find the number of elements <= ti, and the same for removes.

But the insertion time is O(k) for each add/remove, which is O(n^2) time in the worst case. But maybe in practice, for the problem's test cases, this approach can pass.

But for n=1e5, and each insertion being O(k), it's possible that in the worst case where all events are for the same xi, it's 1e5 insertions into the same list. For each insertion, the list is kept sorted. So inserting elements in reverse order (ti=1e5, then 1e5-1, etc.) would require inserting each new element at position 0, which for a Python list is O(k) time. So the total time would be O(1+2+3+...+1e5) = O(5e9) operations. Which is way too slow.

So this approach is not feasible.

Hmm. So perhaps we need a different approach. Let's think about the following:

We can process all events in the order of their ti's. But since the input order is not sorted by ti, this requires sorting the events first. But each query is part of the input sequence, and count queries must be processed in the input order. So this approach is not applicable.

Alternatively, perhaps we can use a global timeline. For each xi, track the events as they are added (in input order), but for each count query, we need to process all events (add/remove) that have been added before it (in input order) and have ti <= query ti.

This brings us back to the same problem: how to track events for each xi and answer the count queries efficiently.

Wait, but perhaps we can use a binary indexed tree (Fenwick Tree) for each xi. But xi can be up to 1e9, so we need a way to map xi's to their Fenwick Trees. Also, each Fenwick Tree would need to be built on the ti's for that xi. But ti's are up to 1e9, which is too large. So coordinate compression is needed for each xi's Fenwick Tree.

But coordinate compression requires knowing all ti's for that xi in advance, which we don't have since the events are processed incrementally.

So this approach is not feasible.

Alternative idea: For each xi, maintain a dynamic prefix sum structure. For example, use a binary indexed tree that can dynamically add new elements. But in Python, implementing such a structure is challenging.

Wait, perhaps the problem can be viewed as a 2D problem where for each xi and each ti, we track the number of adds and removes. But this is again not feasible due to the large possible ranges of xi and ti.

Another idea: Since the ti's are unique and can be processed in any order, but the count queries need to know the number of events <= ti, perhaps we can represent the ti's as a sorted list, and for each xi, track the adds and removes in a way that allows for efficient queries. But again, this brings us back to the same issue of maintaining a sorted list.

Wait, here's a different approach. Since all ti's are unique and globally distinct, we can use a binary indexed tree or a segment tree that covers all possible ti's. But since ti can be up to 1e9, this is not feasible. So coordinate compression is needed. But how?

If we collect all ti's from all events (add, remove, count) first, then we can sort and assign compressed indices. But the problem is that the events are processed incrementally, and each count query must be processed after all previous events in the input order.

So, this approach is not possible because the events are processed in the order given in the input. We can't pre-process all ti's before processing the queries.

Hmm. So, the problem seems to require a data structure that allows for dynamic insertion of ti's and efficient querying of the number of elements <= ti. This is exactly what a binary indexed tree can do if the ti's are compressed. But without knowing all ti's in advance, it's challenging to perform coordinate compression.

But perhaps for each xi, we can maintain a dynamic coordinate compression. For example, when a new ti is added for xi, we add it to a list, sort the list, and assign a rank. Then, for each subsequent insertion, we can find the appropriate rank and update the BIT. But this would require maintaining a sorted list and recompressing every time a new ti is added, which is not feasible.

Alternatively, use a balanced binary search tree to manage the ti's for each xi. For each xi, we have two trees (adds and removes) which are kept sorted. Then, inserting a new ti into the tree is O(log k) time, and querying the number of elements <= ti is also O(log k) time. But implementing a balanced BST in Python is difficult and time-consuming.

So, perhaps the only feasible way is to use a list and bisect.insort for each xi's adds and removes, but hope that the test cases do not have many events for the same xi with ti's in reverse order.

But given that the problem statement allows for n up to 1e5, this approach may not pass the time constraints for some test cases.

But how else can we handle this?

Another idea: Since all events are given in the input, but we can process them in any order, but each count query must be processed in the input order, we can pre-process all events and for each xi, collect all the add and remove ti's, sort them, and then answer queries using binary search. But this requires that the count queries are processed after all add/remove events for that xi. But this is not the case. For example, a count query can come before some add/remove events in the input order. So, this approach is not feasible.

Wait, but the count queries must be processed in the order of the input. So, for example, if a count query is the first event in the input, it will have no previous add/remove events to consider, and the answer will be 0.

So, this suggests that the count queries must be answered based on the events that have been processed up to that point in the input order.

Therefore, the only way to handle this is to process each event (add/remove/count) in the order of the input. For each add/remove, we must record it in a way that allows future count queries (which may come after in the input order) to efficiently compute the count based on their ti.

So, for each xi, we must maintain a data structure that allows for insertion of ti's in any order and efficient querying of the number of ti's <= query ti.

The only way to do this in Python within time constraints is to use a list and bisect.insort for each xi's adds and removes, and accept that in the worst case, the time is O(n^2), but hope that in practice, the average case is acceptable.

But given the problem's constraints, this approach may not be feasible for the largest test cases. So, what's the correct approach here?

Wait, perhaps there's a smarter way to model this. For each event (add, remove, count), the ti is unique. So, for each xi, the adds and removes can be stored in a list, and when a new event is added, we can store it in the list, and keep the list unsorted. Then, for a count query, we can process all events for xi up to that point in the input order, and count how many adds and removes have ti <= query ti.

But this would require O(k) time per query, which is O(n^2) in the worst case.

But with n=1e5, this is not feasible.

So, this brings us back to the original problem.

Alternative approach: The problem allows for offline processing. That is, can we process all queries in a way that allows us to answer all count queries in a batch?

But the problem requires that each query is processed in the input order, and that the result of each count query depends on all previous add/remove events in the input order. So, offline processing may not be possible unless the order of processing can be modified, which is not the case here.

Thus, the solution must process each event incrementally, in the order of input, and for each count query, compute the result based on the current state of the multiset as of that query's ti.

So, the only feasible way is to use a sorted list per xi for adds and removes, and use bisect.insort to insert new events, then use bisect.bisect_right to count.

But in Python, bisect.insort is O(n) time per insertion. So, for 1e5 events, each requiring O(n) time, it's O(1e10) operations, which is way beyond the time limit.

But perhaps there's a way to optimize this. For example, if we can find that the events are processed in ti order. But the problem states that ti's are distinct but can be in any order.

So, this suggests that the problem is not solvable with a straightforward approach in Python. But perhaps there's a smarter way.

Wait, another observation: the count query's answer is the number of adds up to ti minus the number of removes up to ti. So, for a given xi, if we can keep track of all the events (add and remove) sorted by ti, then each count query is O(log k) time. But inserting events is O(k) time, which is not feasible.

But how else can we model this? What if we use a global list of events, sorted by ti, and for each xi, track the events that affect it. But this approach would not allow us to efficiently find the events for xi and ti <= query ti.

Alternatively, for each xi, maintain two variables: the current count of adds and removes. But this doesn't work because the count depends on the ti's. For example, adding an event at ti=5 and then another at ti=3. The count query at ti=4 should include the event at ti=3 but not the one at ti=5.

So, this approach won't work.

Hmm. So, after all this thinking, perhaps the correct approach is to use a sorted list for each xi's adds and removes, and use bisect.insort to insert them, and for count queries, use bisect.bisect_right. But how to handle the time constraints.

But in practice, for the problem's test cases, if the events for each xi are added in roughly increasing order of ti, then bisect.insort is O(1) per insertion. For example, if we append to the end of the list, then inserting is O(1). So, if the events are added in increasing order of ti for each xi, the total time for inserts is O(n log n), which is acceptable.

But if the events are added in random order, then the average time per insertion would be O(log k), which would be acceptable for n=1e5. But this is not the case, because in Python, list.insert is O(k) time for each insertion. So, the time depends on the position where the insertion happens.

Wait, no. The bisect.insort function uses list.insert, which for Python lists is O(k) time, because inserting into the middle of the list requires shifting all subsequent elements. So, even if the insertion is in the middle of the list, it's O(k) time.

Therefore, this approach is not feasible for large k.

So, given that, perhaps the correct solution is to use a different data structure, like a binary indexed tree, but manage it dynamically.

But in Python, there's no built-in way to do this.

But here's an alternative idea: for each xi, instead of maintaining a sorted list of adds and removes, we can maintain a list of events in the order they are added and keep track of the sorted indices. But this is not possible.

Alternatively, for each xi, maintain a list of events in the order they are added, and when a count query is made, we can use a binary search on a sorted list, but this sorted list is built when the query is made. For example, when a count query is made for xi and ti, we can take all the adds and removes for xi that have been added up to that point, sort them, and compute the count. But sorting for each query is O(k log k), which is not feasible for large k.

Hmm. So this brings us to a dead end.

Wait, but maybe the problem allows us to use a different approach. Let's think about the count query: the answer is the number of adds with ti <= query_time minus the number of removes with ti <= query_time for the same xi.

Each add and remove for xi can be considered as a point in time. For a count query, we need to count the number of points in the adds set that are <= query_time and subtract the number in the removes set.

So, the problem reduces to, for each xi, we have two dynamic sets (adds and removes) and need to support insert and count <= query_time operations.

The data structure that can do this efficiently is a balanced binary search tree, which allows insertions and rank queries in O(log n) time. But Python doesn't have a built-in sorted list or tree.

But we can implement a binary indexed tree (Fenwick Tree) for each xi's adds and removes, but how?

Let me think: for each xi, when we add a new ti to adds, we need to track all adds and their ti's. We can assign a unique index to each ti based on their order when sorted. But since ti's are added dynamically, this is challenging.

Alternatively, we can use a Fenwick Tree with dynamic indices. But this is not straightforward.

Another idea: Since all ti's are unique, we can treat them as a set and use a binary indexed tree for each xi. For example, when a new ti is added for xi's adds, we can insert it into a Fenwick Tree, and the tree's index is based on the sorted order of ti's. But this requires keeping track of the sorted order.

Wait, here's a possible approach:

For each xi, maintain a sorted list of adds and removes. When a new ti is added, insert it into the sorted list using bisect.insort. Then, for each xi's adds and removes, maintain a Fenwick Tree that tracks the count of events. Each time a new event is added, we can find its position in the sorted list (using bisect.bisect_left), and update the Fenwick Tree at that position. For example, the Fenwick Tree for adds of xi will have a size equal to the number of adds for xi, and each position represents a ti in sorted order. Then, when a count query is made for ti, we find the position in the sorted list where ti would be inserted (using bisect.bisect_right), and query the Fenwick Tree up to that position to get the count.

This approach would allow O(log k) insertions and O(log k) queries for each event. But maintaining the Fenwick Tree for each xi's adds and removes is feasible.

But in Python, creating a Fenwick Tree for each xi is possible. For example, we can have a dictionary that maps xi to two Fenwick Trees (for adds and removes). Each Fenwick Tree is dynamically created as needed.

But how to implement this?

The steps would be:

1. For each xi, when an add event is processed:
   a. If xi is not in the adds dictionary, create a new Fenwick Tree for it.
   b. Insert the ti into the sorted list for xi's adds.
   c. Update the Fenwick Tree by adding 1 at the index corresponding to the ti's position in the sorted list.

But this requires maintaining the sorted list and the Fenwick Tree in sync. However, since we're using bisect.insort to insert into the sorted list, the list remains sorted. Then, the position where the ti is inserted into the list is the same as the index in the Fenwick Tree. But each time a new ti is inserted, the Fenwick Tree for xi's adds must be updated at that position.

But this approach has a problem: inserting into the sorted list shifts the positions of subsequent elements, which would invalidate the Fenwick Tree's indices. For example, if we have a sorted list [3,5,7], and insert 4 into position 1, the new list is [3,4,5,7]. The Fenwick Tree, which was initially tracking indices 0, 1, 2, now needs to track 0, 1, 2, 3. But inserting at position 1 would require shifting the existing elements, which would require the Fenwick Tree to be updated accordingly. This is not feasible, as the Fenwick Tree's indices are static once created.

Thus, this approach is not feasible.

Alternative idea: Use a coordinate compression for the ti's. But this requires knowing all ti's in advance, which we do not.

So, this approach is not feasible.

Hmm. So, after all this thinking, it seems that the only feasible way in Python is to use bisect.insort and lists for each xi's adds and removes, and hope that the test cases do not have worst-case scenarios for insertion.

But given that the problem constraints are tight, this approach may pass within the time limits for most cases, but may not for some.

But let's proceed with this approach, as it's the only way to handle it in Python without external libraries.

So, the plan is:

- Use a dictionary, where each key is xi, and each value is a tuple of (adds_list, removes_list), where adds_list is a sorted list of ti's for adds, and removes_list is a sorted list of ti's for removes.

- For each add event (ai=1), insert ti into the adds_list of xi using bisect.insort.

- For each remove event (ai=2), insert ti into the removes_list of xi using bisect.insort.

- For each count event (ai=3), retrieve the adds_list and removes_list for xi. Compute the number of adds <= ti by bisect.bisect_right(adds_list, ti). Compute the number of removes <= ti by bisect.bisect_right(removes_list, ti). The count is adds_count - removes_count.

This is the straightforward approach.

But in Python, for each insertion into a list, bisect.insort is O(k) time. So, if all events are for the same xi, this would be O(n^2) time.

But perhaps the problem's test cases are designed to have many different xi's, leading to small k for each xi, making this approach feasible.

Let's test this with the sample input.

Sample input 1:

6
1 1 5
3 5 5
1 2 5
3 6 5
2 3 5
3 7 5

For xi=5:

Adds are at times 1, 2.

Removes are at time 3.

Count queries are at times 5 (counts adds <=5: 1, removes <=5:0 → 1-0=1), 6 (adds 2, removes 0 → 2), and 7 (adds 2, removes 1 → 1).

So, the adds_list for 5 would be [1,2], removes_list [3].

Each insertion is done with bisect.insort, which for adding 1 (empty list → inserted at 0), 2 (appended), and 3 (appended).

So, these insertions are O(1) each, as they are added in order.

Sample input 2:

3
1 1 1
2 2 1
3 3 1

For xi=1, adds_list has [1], removes_list [2].

Count query at 3: adds_count is 1, removes_count 1 → 0.

But the problem's second sample has output 0.

But according to the events, the count is at ti=3. The add is at 1, remove at 2. So 1-1=0.

Yes.

But when inserting the add and remove, they are inserted into the sorted list. For the add, inserting 1 is added to the adds_list. Then, the remove is inserted into the removes_list.

So, this approach works.

But again, the time complexity depends on the order of insertion.

So, given that the problem's time limit is 2 seconds and n is up to 1e5, this approach may work for most test cases.

In Python, inserting into a list using bisect.insort for each add and remove is O(k) per insertion. For n=1e5, the worst case is O(1e10) operations, which is way too slow. However, if the ti's are inserted in increasing order for each xi, then each insertion is O(1) (appending to the list), and the total time is O(n log n), which is acceptable.

But the problem states that the ti's are distinct and may be in any order. So, if the ti's are added in random order, the average insertion time is O(k/2) per insertion, leading to O(n^2) time.

But how can the problem's constraints be handled?

The problem's time limit is 2 seconds. Python can handle about 1e8 operations in that time. For n=1e5, and each insertion taking O(1), it's 1e5 operations. But if each insertion takes O(k), and for a xi with k=1e5, it's O(1e5 * 1e5) = 1e10 operations, which is way too slow.

So, this suggests that this approach is not feasible for the problem's constraints. Therefore, there must be a more efficient approach.

Wait, here's a different angle. The problem requires that after each operation, all remove operations are applied to elements that are present. So, for example, after each remove, the multiset must have at least as many instances of the element as required. So, the sequence of add and remove events for each xi must be such that the net count (adds - removes) is non-negative at all times after each operation.

But how does this help in the solution? It ensures that removes can't exceed adds for any xi. But I'm not sure how to leverage this for optimization.

Another observation: the count queries are based on the state of the multiset as of a certain time ti. But the multiset's state is the cumulative result of all adds and removes with ti <= the query's ti. So, the order of events in the input doesn't matter for the count query. Only the ti's of the events and their type (add/remove) matter.

So, the count query's answer depends on all events (add and remove) for xi with ti <= the query's ti, regardless of the order in which they were processed in the input.

This is a key insight. Because it means that the order in which the events are processed (input order) does not affect the count query's answer. Only the events' ti's and their types.

Therefore, we can process all events (add/remove) in any order, as long as we track for each xi the adds and removes with their ti's. Then, when a count query is made, we can compute the count based on the events' ti's and types, regardless of the input order.

Wait, but the problem states that the events are processed in the input order, and the count queries are processed in the input order. For example, if a count query is made before an add event for the same xi and ti, the count query won't include that add event.

But according to the problem statement, each event (including count queries) is processed in the order they appear in the input. So, when a count query is processed, it must only consider the add and remove events that have been processed before it in the input order.

But the problem's example shows that the order in which events are processed (in the input) affects the state of the multiset. For example, adding an event at a later time and then adding an event at an earlier time. The count query after that would include the earlier event.

So, the order of processing events in the input is crucial, but their ti's determine the state of the multiset at various times.

But when processing events in the input order, the events' ti's can be in any order, and each event's ti is considered part of the timeline. So, the multiset's state at a time ti is the cumulative effect of all events (add/remove) processed up to that point in the input order with ti <= query ti.

So, the count query's answer depends on the events processed before it in the input order, but their ti's are not necessarily processed in order.

This suggests that the input order of events is not important for the count query's answer, except that it determines which events have been processed before the query.

But the actual ti's of the events determine the multiset's state at the query's time.

So, for each xi, the adds and removes events that have been processed before the count query (in input order) are the ones that contribute to the answer. For these events, their ti's are considered in sorted order when calculating the count.

Thus, for each xi, the adds and removes that are processed before the count query (in input order) can be stored in sorted lists. Then, the count query can binary search these lists to find the number of events <= query ti.

But the problem is that inserting into these sorted lists is O(k) time per insertion.

So, this brings us back to the same issue.

But wait, another observation: the count queries only require the number of events <= ti. So, if we can maintain for each xi a dynamic frequency array where we can add a new ti and query the number of elements <= ti, then this would suffice.

This is exactly what a Binary Indexed Tree (Fenwick Tree) or a Segment Tree can do. But again, the challenge is dynamically handling ti's without knowing them in advance.

So, here's the plan:

For each xi, maintain two dynamic structures (one for adds, one for removes) that allow the following operations:

1. Insert a ti.
2. Query the number of ti's <= given value.

In Python, a way to implement this is to use a sorted list and bisect's bisect_right function. But the insertion into the sorted list is O(k) time.

Alternatively, we can use a Binary Indexed Tree with dynamic coordinate compression.

Here's how it can be done:

For each xi, when the first add or remove event occurs, initialize two lists (add_ti_list and remove_ti_list) and two BITs (add_bit and remove_bit). As each new ti is added, we insert it into the appropriate list, sort it, and assign a rank (coordinate compression). The BIT is then updated to reflect this new ti.

But inserting into the list and sorting it each time is O(k log k) time per insertion, which is not feasible.

Alternatively, we can maintain a sorted list for each xi's add and remove ti's, and when inserting a new ti, use bisect.insort. Then, the rank is the position where the ti is inserted, and the BIT can be updated using that rank. But this requires that the BIT's size is equal to the current number of elements, which can be done dynamically.

For example:

For a given xi's add events:

- When inserting a new ti, use bisect.insort to add it to the sorted list.
- The rank of ti is its index in the sorted list.
- The BIT for adds is size len(add_list). Each insertion increases the size by 1.
- When inserting ti, we update the BIT at rank+1 (BIT is 1-indexed) with +1.

Then, to query the number of adds <= query_ti, we use bisect.bisect_right(add_list, query_ti) to get the count. This is the same as the number of elements in the add_list <= query_ti.

But the BIT is not needed in this case, because the count can be obtained directly from the bisect function. So why use a BIT?

Ah, because if the BIT is maintained, then each insertion is O(log k) time, and each query is O(log k) time. But this approach requires that the BIT is updated each time a new ti is inserted. However, the problem is that the BIT's indices are based on the sorted list, which changes with each insertion. So, the BIT would need to be dynamically resized, which is not feasible.

So, this approach is not feasible.

Thus, the only way to handle this in Python is to use bisect.insort for each insertion and bisect.bisect_right for each query.

But given the time constraints, this approach may not pass for some test cases. However, considering the problem's constraints and the fact that Python is generally slower than C++ or Java, this is the only feasible approach.

So, let's proceed with the code.

The code will be:

- Read all events in order.
- For each event, process it as follows:
   - If it's add (ai=1), insert the ti into the adds list for xi, maintaining sorted order.
   - If it's remove (ai=2), insert the ti into the removes list for xi, maintaining sorted order.
   - If it's count (ai=3), find the number of adds <= ti and subtract the number of removes <= ti.

Implementing this in Python:

We can use a defaultdict to map each xi to a tuple of (adds, removes), where adds and removes are lists maintained in sorted order.

For each add or remove event, use bisect.insort to insert the ti into the respective list.

For each count query, use bisect.bisect_right to find the count.

So, the code would look like:

Testing against sample input 1.

```python
import bisect
from collections import defaultdict


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    data = defaultdict(lambda: {'adds': [], 'removes': []})

    for _ in range(n):
        a, t, x = map(int, input_stream.readline().rstrip("\n").split())
        if a == 1:
            bisect.insort(data[x]['adds'], t)
        elif a == 2:
            bisect.insort(data[x]['removes'], t)
        else:
            adds = data[x]['adds']
            removes = data[x]['removes']
            add_count = bisect.bisect_right(adds, t)
            remove_count = bisect.bisect_right(removes, t)
            print(add_count - remove_count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 1 1
2 2 1
3 3 1
""",
            "output": \
"""\
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

The sample input's first three queries:

The first query is a count at time 5 (third line of input):

1 1 5 → add 5 at time 1.

Then the next query is 3 5 5 → count 5's instances at time 5. adds has [1], so add_count=1, removes is empty → 1-0=1.

Then add another 5 at time 2 (now adds are [1,2]).

Count at time 6 → adds are [1,2] → bisect_right(6) is 2, removes is empty → 2-0=2.

Then remove 5 at time 3: adds are [1,2], removes now [3].

Count at time 7: adds has 1,2 <=7 → 2, removes has 3 <=7 →1. 2-1=1.

Which matches the sample output.

So, the code works for the sample.

Sample 2:

Input:
3
1 1 1
2 2 1
3 3 1

adds for 1 is [1], removes [2]. Count at 3: adds has 1 <=3 →1, removes 2 <=3 →1. 1-1=0. Output is 0.

Which matches.

Thus, the code works for the samples.

But for large cases, the code may time out. However, given the problem's constraints and the available data structures in Python, this is the best possible solution.
</think>

```python
import bisect
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    data = defaultdict(lambda: {'adds': [], 'removes': []})
    for _ in range(n):
        a = int(input[ptr])
        t = int(input[ptr+1])
        x = int(input[ptr+2])
        ptr +=3
        if a == 1:
            bisect.insort(data[x]['adds'], t)
        elif a == 2:
            bisect.insort(data[x]['removes'], t)
        else:
            adds = data[x]['adds']
            removes = data[x]['removes']
            add_count = bisect.bisect_right(adds, t)
            remove_count = bisect.bisect_right(removes, t)
            print(add_count - remove_count)

if __name__ == "__main__":
    main()
```
