<think>
Okay, let's see. The problem is about simulating a server processing queries with a queue of limited size. We need to determine when each query finishes processing or if it's rejected. The constraints are up to 200,000 queries, so any O(n) solution should be acceptable, but we need to make sure not to do anything that's O(n^2) because that would be too slow.

So the server can be in a state where it's busy until a certain time. The queue can hold up to b queries. Each new query comes in order, and their ti's are strictly increasing, which might help.

Let's think about the steps for each query:

1. When a query arrives at time ti, check if the server is free. If the server is free and the queue is empty, start processing it immediately. Its end time would be ti + di.

2. If the server is busy, check if the queue has space (less than b elements). If yes, add to the queue. If no, mark it as rejected (-1).

But how do we track the server's state and the queue?

Hmm. The server can be represented by when it becomes free next. Let's call that variable 'current_end_time'. The queue is a FIFO structure. For each query, we need to:

- Check if ti is after or equal to current_end_time. If so, the server is free. Then, the queue must be checked. If there are queries in the queue, they would have been processed by now. Wait, no. Because when the server finishes processing a query, it immediately takes the next from the queue. So maybe we need to process the queue before considering the new query.

Wait, here's the key: the server processes queries one after another. When a new query arrives, any queued queries are processed in order. But how to model this efficiently?

Maybe for each query, before handling it, we first check if the server has any pending work. Let's see: the server's current_end_time is the time it's currently busy until. When a new query arrives at ti, first we check if ti is after the current_end_time. If yes, then the server is free, and the queue must have been processed (since once the server is free, it processes the next in queue until it's empty). So any queries in the queue would have been processed before ti. Wait, no. Because when the server is free, it starts processing the next query in the queue immediately. So if the queue isn't empty when the server is free, the server would process the next query, which would end at some time, and then check the queue again, and so on.

But handling this for each query step-by-step might be computationally expensive if we have to check the queue each time. But perhaps we can model it by tracking the server's next available time and the queue.

So, the idea is:

- Maintain current_end_time: the time when the server will be free.

- A queue (a deque or a list) that holds the pending queries.

For each incoming query (ti, di):

1. First, process all possible queued queries that can be processed before ti. Wait, no. Because ti is when the new query arrives. So before adding the new query, any queued queries that can be processed up to ti may have been processed. Wait, but the server can't process anything during ti unless the current_end_time is <= ti.

Wait, the server is busy until current_end_time. If current_end_time <= ti, then the server is free, and can process any queued queries. But once the server is free, it starts processing the next query in the queue immediately. So for example, if current_end_time is 10, and a query arrives at ti=15, then between 10 and 15, the server is free. But since there's a queue, it would have processed any queued queries during that time. Wait, but the queue is empty in this case, right? Because when the server finishes at 10, if there's a queue, it would process the first in the queue, which would take di time, and so on. So, between the server becoming free and the new query arriving, the server could have processed some queued queries.

Wait, this seems tricky. Let's think of the steps:

When a new query arrives at ti:

- The server may be busy (current_end_time > ti) or free (current_end_time <= ti).

If the server is busy:

- Check if the queue's length is less than b. If yes, add to queue. If not, reject.

If the server is free:

- The queue must be empty, because once the server is free, it would have processed all queued queries. Wait, no. Wait, when the server is free, it can start processing the next query in the queue. So if there are queued queries, the server would process them in order, one after another, each starting immediately after the previous one ends. So, when the server is free (current_end_time <= ti), but there are queries in the queue, those would have been processed by the server in sequence before ti. But how can that be? Because the server can't process queries during the time when ti arrives unless ti is after the server's current_end_time.

Wait, perhaps the key is that when a query arrives at ti, first we need to process as much of the queue as possible up to ti. Let's see.

For example, if the server's current_end_time is 10, and the next query arrives at ti=15, then the server is free from 10 to 15, so during that time, any queued queries would have been processed. But if the queue was not empty when the server became free (current_end_time was 10), then the server would process the first in the queue, which would take di time, and so on until the queue is empty. So, between current_end_time (10) and ti (15), the server could process some or all of the queued queries.

Wait, but how can we model this without simulating every step? Because with n=2e5, we can't process each queued query one by one for each incoming query.

So here's the problem: each time a new query arrives, we need to process all possible queued queries that can be processed before or at ti, but how?

Alternative approach: the server's current_end_time is when the server is next available. The queue holds the pending queries. For each new query (ti, di):

1. While the queue is not empty and current_end_time <= ti:

   a. The server processes the first query in the queue. So, the end time becomes current_end_time += di (where di is the duration of the first query in the queue).

But wait, no. Because the server can only process queries in the queue when it's free. So if current_end_time is <= ti, then the server has been free since current_end_time. So any queued queries would have been processed as soon as possible. So between current_end_time and ti, the server could process some queries.

So when a new query arrives at ti, first we need to process as many queued queries as possible up to ti. How?

The steps would be:

Check if current_end_time <= ti. If so, process all queued queries until either the queue is empty or the next queued query would make current_end_time exceed ti.

Wait, but how? Because each queued query takes di time. So if the server is free, it starts processing the first in the queue immediately. So the first queued query starts at current_end_time, ends at current_end_time + di. Then the next starts at that end time, and so on.

But ti is the arrival time of the new query. So when the new query arrives, the server may be in the process of handling queued queries.

But since the server processes queued queries in order, and the arrival of the new query is at ti, which is after all previous queries (since ti's are strictly increasing), maybe we can pre-calculate how much of the queue can be processed before ti.

Wait, here's an idea. The server's current_end_time is the time when it becomes free. Let's say current_end_time is 10. The new query arrives at ti=15.

If the queue is not empty, then after 10, the server starts processing the first query in the queue. Let's say that query has duration 3: ends at 13. Then the next in queue (if any) is processed next, starts at 13, etc. This continues until the server's current_end_time exceeds ti (15) or the queue is empty.

So when the new query arrives at ti=15, the server might have processed some queued queries between 10 and 15.

So the process when a new query arrives is:

- Before handling the new query, check if the server's current_end_time is <= ti. If yes, process the queued queries until current_end_time exceeds ti or the queue is empty.

Wait, but how can we model this efficiently?

For example, suppose the server's current_end_time is 10. The queue has 3 queries: durations 2, 3, 4. The new query arrives at ti=15.

Processing the first in queue (duration 2): ends at 12. Then, next (3) ends at 15. Then next (4) would start at 15, but 15 is equal to ti. Wait, according to the problem statement, when the server finishes processing a query at exactly x (15), and a new query arrives at x (15), the server picks from the queue first, then the new query is considered. So in this case:

The server finishes at 15. The new query arrives at 15. So first, the server processes the next in queue (if any). So in the scenario where current_end_time is 15 and ti is 15, the server would process the next in the queue (if any) before considering the new query.

So back to the example: current_end_time is 10. The queue has 3 queries (durations 2,3,4). ti is 15.

Processing the first query (duration 2): ends at 12. Now, current_end_time is 12 <=15. Process next (3): ends at 15. Now current_end_time is 15 <=15. Process next (4): ends at 19. Now current_end_time is 19. Now, ti is 15, which is less than 19. So the server is busy when the new query arrives. So the new query is added to the queue if possible.

Wait, but in this case, when the new query arrives at 15, the server is processing the third queued query, which started at 15 and ends at 19. So when the new query arrives at 15 (same time as the server starts processing the third queued query), according to the problem statement, the server is considered busy when the new query arrives. Because the server finishes the previous query at 15 (the third query starts at 15), so the server is busy from 15 to 19. So the new query arrives while the server is busy.

Wait, this is a bit confusing. Let me re-read the problem statement.

The problem says:

When a new query comes at x, and the server finishes processing another query at exactly x, we consider that first the query is picked from the queue (if any), then the new query appears.

So if the server's current_end_time is x (same as the new query's ti), then the server is considered to have finished processing the previous query. So the server is free. Then, the server will process any queued queries first, and then the new query is handled.

So in the example where current_end_time is 15 and ti is 15:

- The server is free (current_end_time is 15). Then, the server checks the queue. If there are queued queries, the server processes them. Only after processing all possible queued queries (until the queue is empty or the next query's processing would take current_end_time beyond ti?), then the new query is handled.

Wait, but the new query arrives at ti=15. So when the server is free (current_end_time <= ti), the server will process all queued queries that can be processed before the new query arrives. But the new query arrives at ti. So during the time up to ti, the server can process queued queries. But ti is the arrival time of the new query. So the server can process queued queries until current_end_time <= ti.

So, for example, if current_end_time is 10, and ti is 15, then the server can process queued queries starting at 10, 10+2=12, then 12+3=15, then 15+4=19. But ti is 15. So processing the first two queued queries (durations 2 and 3) would end at 15. Now, current_end_time is 15. Since ti is 15, the new query is arriving at this time. So the server is free (current_end_time <= ti), but the queue still has one more query (duration 4). So the server would process that query next. But since ti is 15, which is the current_end_time, the server would start processing that queued query, which takes 4 units, so current_end_time becomes 19. Then, the new query arrives (at ti=15), but the server is busy until 19. So the new query is added to the queue if there's space.

Wait, this seems contradictory. Let's look at the problem statement again.

The note in the problem says:

In the first sample, at moment 19, two events happen: the server finishes processing the second query (so current_end_time is 19), and the fifth query arrives. The server first picks the next query (the fourth) from the queue (which was added at 15), starts processing it (ends at 21). Then, the fifth query is added to the queue, which is empty now, so it's processed immediately.

So the server's current_end_time is 19. The fifth query arrives at 19.

The processing steps are:

- Server finishes previous query at 19. Then, the queue has the fourth query (ti=15, di=2). So the server starts processing it at 19, ends at 21. Then, the fifth query is considered. Since the server is busy (current_end_time is 21, which is after 19), and the queue is empty (the fourth was processed), the fifth can be added to the queue (since queue size is 0 <1). So it's added. The server is busy until 21, so after processing the fourth query, the server picks the fifth, starts at 21, ends at 22.

Ah, so when the server's current_end_time is 19, and a new query arrives at 19, the server first checks the queue. The queue has the fourth query. So it processes that, then the fifth is added.

So, the key is that when the new query arrives at the same time as the server's current_end_time, the server first processes any queued queries (if possible) before handling the new query.

Thus, when handling a new query at ti, the steps are:

1. Process as many queued queries as possible that can be started at or before ti. Because the server can process them before the new query arrives.

But how to model this efficiently.

Alternative approach: for each new query (ti, di):

- First, check if the server can process any queued queries before ti. So, while the server's current_end_time <= ti and there are queued queries, process them. Wait, but each queued query takes time. For example, if current_end_time is 10 and ti is 15, and the queue has a query with di=3. The server processes it, ends at 13, which is <=15. Then, process next queued query (if any). And so on until current_end_time exceeds ti or the queue is empty.

Wait, no. Because processing a query in the queue takes di time. So, the server can process as many queries as possible as long as the start time of each is <= ti.

Wait, the server starts processing a queued query at current_end_time. If current_end_time <= ti, then that query will be processed, but the server's new current_end_time is current_end_time + di. But the next queued query can only be processed if current_end_time (after the previous processing) is <= ti.

So, to process the queued queries as much as possible before the new query arrives, we need to process them until current_end_time + next query's di > ti.

But this could take O(n) time in total, but for each query, we might process multiple queued queries. But with n up to 2e5, we need to make sure that the total operations are O(n).

So here's the plan:

We maintain a queue (deque) of pending queries, each stored with their di and index (to track their end time). We also track the server's current_end_time.

For each incoming query (ti, di):

1. Before handling the new query, process as many queued queries as possible that can be started before ti. So:

   a. While the queue is not empty and current_end_time <= ti:

       i. Take the first query from the queue.

       ii. current_end_time += di of that query. Record the end time for that query as the new current_end_time.

   Wait, no. Because each queued query is processed sequentially, starting when the server is free. So, for example, if current_end_time is 10, and ti is 15, and the queue has two queries with di=3 and di=4:

   - The first query starts at 10, ends at 13. Then, the next query starts at 13, ends at 17. Now, current_end_time is 17, which is greater than ti=15. So the server stops processing queued queries here. The new query arrives at 15. Since current_end_time (17) >15, the server is busy, so the new query is added to the queue if possible.

But according to the problem statement, any queued queries are processed before the new query arrives. So the server will process as many as possible before the new query arrives.

So the correct approach is:

When handling a new query (ti, di):

- While the queue is not empty and current_end_time <= ti:

   Take the first query from the queue. current_end_time = current_end_time + di. (This represents the server processing that query.)

But wait, even if current_end_time + di > ti, the server still processes that query. Because once the server starts processing a query, it can't stop. So, for example, if current_end_time is 10 and ti is 15, and the first queued query has di=10. Then, server starts processing it at 10, ends at 20. But 20 >15. But the server will still process this query, even though the new query arrives at 15. So the processing of the queued query is done, and the server's current_end_time becomes 20. Then the new query arrives at 15, but the server is busy until 20.

So the correct approach is:

Process all queued queries until the queue is empty, even if the current_end_time exceeds ti. Because once the server is free (current_end_time <= ti), it starts processing the queued queries, regardless of whether their processing would end after ti.

Wait, no. Because the server can't process queued queries if their processing starts after ti. For example, if the server's current_end_time is 10, and ti is 15, and the queued query has di=6. Then processing that query starts at 10, ends at 16. So the server is busy until 16. The new query arrives at ti=15. Since the server is busy (16>15), the new query is added to the queue if possible.

But how do we model this?

The server is processing queued queries only when it's free. So when the server's current_end_time is <= ti, the server is free. So it can start processing the next queued query. That query's processing starts at current_end_time. But even if current_end_time + di > ti, the server is busy from current_end_time to current_end_time + di. So the server will process that query regardless.

Thus, the correct approach is:

For each new query (ti, di):

1. Process all queued queries that can be processed before the new query arrives. But how? Because once the server starts processing a queued query, it will finish it even if the end time is after ti.

Wait, no. The server starts processing the queued query at current_end_time, which is <= ti. But after processing that query, current_end_time becomes current_end_time + di. So even if this new current_end_time is > ti, the server is now busy. So when the new query arrives at ti, the server is busy (current_end_time > ti), and the new query is added to the queue if possible.

So the correct steps are:

For each new query (ti, di):

- While the server is free (current_end_time <= ti) and the queue is not empty:

   a. Process the first queued query. Update current_end_time += di of that query.

   b. This may make current_end_time > ti, but we still process all queued queries until the server is busy (current_end_time > ti) or the queue is empty.

Wait, no. Because once the server is free (current_end_time <= ti), it will process the next queued query, even if the processing ends after ti. So for example, current_end_time is 10, ti is 15. Queue has a query with di=10. Server starts processing it at 10, ends at 20. Now current_end_time is 20, which is >15. So the server is busy. So the new query arrives at 15, but the server is busy until 20. So the new query is added to the queue if possible.

So the server processes queued queries until the queue is empty or current_end_time > ti.

Wait, no. Because once the server is free (current_end_time <= ti), it can process queued queries one by one, even if each individual processing takes the current_end_time beyond ti.

For example, current_end_time is 10, ti is 15. Queue has queries with di 3, 5. 

First query: current_end_time becomes 13 (<=15). Next query: starts at 13, ends at 18 (>15). Now, current_end_time is 18. So the server is busy. So the new query arrives at 15. Since the server is busy (current_end_time 18 >15), the new query is added to the queue if possible.

Thus, the processing of queued queries happens even if their processing takes the server's current_end_time beyond ti. Because the server starts processing them when it's free (current_end_time <= ti), even if their processing ends after ti.

Thus, the steps for handling a new query (ti, di) are:

1. While the server's current_end_time <= ti and there are queued queries:

   a. Take the first query from the queue.

   b. Set its end time to current_end_time + di.

   c. Update current_end_time to this new value.

So, even if current_end_time + di > ti, we process that queued query. Because the server is free (current_end_time <= ti), so it starts processing the queued query.

Thus, the server will process all queued queries until the queue is empty, regardless of whether their processing ends after ti. Because as long as current_end_time <= ti, the server is free and processes the next queued query. The new query arrives at ti, but queued queries are processed in order, regardless of their duration.

Wait, but in the example where current_end_time is 10, and the queue has one query with di=100. ti is 15.

Processing that queued query would take current_end_time to 110. So when the new query arrives at 15, the server is busy until 110. Thus, the new query is added to the queue if possible.

But according to the problem statement, when a query arrives, if the server is busy and the queue is full, it's rejected.

So the key steps for each new query are:

- Before handling the new query, process as many queued queries as possible. This is done by checking if the server is free (current_end_time <= ti), and processing queued queries until the queue is empty or the server becomes busy (current_end_time > ti).

Wait, no. Because even if the server starts processing a queued query that makes current_end_time > ti, it's still processed. So the steps are:

When a new query arrives at ti:

1. Process all queued queries that can be processed starting from current_end_time <= ti. That is, while current_end_time <= ti and the queue is not empty:

   a. Dequeue the first query.

   b. Set its end time to current_end_time + di.

   c. current_end_time += di.

   (This loop continues until the queue is empty or current_end_time > ti.)

But in this case, even if after processing one queued query, current_end_time becomes > ti, the loop stops. So any remaining queued queries stay in the queue.

But no, the server processes queued queries one by one as long as it's free (current_end_time <= ti). So for example, if current_end_time is 10, ti is 15. Queue has three queries: 2, 3, 4. 

Processing first: current_end_time becomes 12 (<=15). Process next: current_end_time becomes 15 (<=15). Process next: current_end_time becomes 19 (>15). So the loop stops. Now, the server is busy until 19, and the new query arrives at 15. Since the server is busy, the new query is added to the queue if possible.

Thus, the steps are:

When a new query arrives:

- Process as many queued queries as possible while current_end_time <= ti. Each queued query is processed in order, even if it makes current_end_time exceed ti.

So the loop is:

while queue is not empty and current_end_time <= ti:

   process the first query in the queue.

So after this loop, the server is either busy (current_end_time > ti) or the queue is empty (current_end_time <= ti).

Now, handle the new query:

If the server is free (current_end_time <= ti) and queue is empty:

   process the new query immediately. current_end_time = ti + di. Set its end time.

Else:

   if queue has space (size < b):

      add to queue.

   else:

      reject.

So, the algorithm in code would be:

Initialize current_end_time = 0.

queue = deque()

results = array of -1 for each query.

for each i in 0..n-1:

   ti, di = queries[i]

   # process queued queries as much as possible before ti

   while queue and current_end_time <= ti:

       # process first in queue

       first_di, first_idx = queue.popleft()

       current_end_time += first_di

       results[first_idx] = current_end_time

   # now handle the new query

   if current_end_time <= ti and not queue:

       # server is free and queue is empty. process immediately.

       current_end_time = ti + di

       results[i] = current_end_time

   else:

       # server is busy (current_end_time > ti) or queue is not empty.

       # check if queue has space.

       if len(queue) < b:

           queue.append( (di, i) )

       else:

           results[i] = -1

But wait, what if after processing the queued queries, current_end_time <= ti and the queue is empty? Then the new query can be processed immediately.

But after processing the queued queries, the queue is empty only if all queued queries were processed. For example, if current_end_time is 10, ti is 15, and queue has two queries (di=3, di=5). The loop processes both, current_end_time becomes 10+3=13, then 13+5=18. Since 18 >15, the loop stops. But the queue is now empty. Wait, no. The loop would process each query as long as current_end_time <= ti.

Wait, let's re-examine the loop:

Processing the first query (di=3):

current_end_time becomes 10+3=13. 13 <=15: continue.

Process next query (di=5):

current_end_time becomes 13+5=18. 18 >15: loop stops.

So the queue is now empty? No, because after dequeuing the first two queries (assuming there were only those two), the queue is empty. Wait, no. The queue starts with two queries. After processing first (dequeued), queue has one. Then processed the second (dequeued), queue is empty. So the loop continues until queue is empty or current_end_time > ti.

In this example, after processing both queries, the queue is empty. So the loop stops because the queue is empty.

Thus, after processing queued queries, the queue is empty. Then, current_end_time is 18, which is >15. So the server is busy when the new query arrives. So the new query is added to the queue if possible.

But in this scenario, after processing the queued queries, the server's current_end_time is 18, which is >15. So the new query is handled as follows: since the server is busy, check if the queue has space (since the queue is empty, len(queue) is 0 <b). So add the new query to the queue.

But wait, after processing the queued queries, the queue is empty. So the server's current_end_time is 18, which is >15. So the new query arrives at ti=15. The server is busy (current_end_time=18>15). The queue is empty. So the queue's length is 0, which is less than b. So the new query is added to the queue.

But when the server is busy, the queue can have up to b elements. So in this case, the new query is added to the queue. But when will it be processed?

The server is busy until 18. After that, it will process the queue (including the new query added here). So the next time the server is free (after current_end_time), it will process the queue.

Thus, the code seems to handle this correctly.

Another example: the first sample input.

Sample Input 1:

5 1

2 9 → query 0

4 8 → query 1

10 9 → query 2

15 2 → query3

19 1 → query4

Processing step by step:

Initially, current_end_time = 0.

Process query 0 (ti=2, di=9):

At i=0:

Loop to process queued queries: queue is empty.

current_end_time <= ti (0 <=2). Server is free and queue is empty. So process immediately. current_end_time becomes 2+9=11. results[0] =11.

Now, next query (i=1, ti=4, di=8).

Check loop: current_end_time=11. 11>4 → loop doesn't run.

Server is busy (11>4). Queue is empty. Check if queue has space (size 0 <1). Add to queue. So queue now has (8,1). results[1] is set later.

Next query (i=2, ti=10, di=9).

current_end_time=11. 11 <=10? No (11>10). So loop doesn't run.

Server is busy. Queue has one element (max b=1). So new query is rejected (results[2]=-1.

Next query (i=3, ti=15, di=2).

current_end_time=11. Process queued queries:

current_end_time (11) <=15. Queue is not empty (contains (8,1)).

Dequeue (8,1). current_end_time +=8 → 19. Now, current_end_time=19>15. Loop stops. Set results[1] =19.

Now, handle query3: ti=15, di=2.

current_end_time=19>15. Server is busy. Queue is now empty. So check if queue has space (0 <1). Add to queue. So queue has (2,3). results[3] is pending.

Next query (i=4, ti=19, di=1).

Process queued queries first. current_end_time=19 <=19. Queue has (2,3). Dequeue, process. current_end_time becomes 19+2=21. Now, current_end_time=21>19. Loop stops. results[3] =21.

Handle new query (ti=19). current_end_time=21>19. Server is busy. Queue is empty. So check if queue has space (0 <1). Add to queue. So queue now has (1,4). results[4] pending.

At this point, after all queries are processed, the queue has (1,4). The server's current_end_time is 21. So after processing, when there are no more new queries, the server will process the queued queries.

But in the code, after all queries are processed, the queue may have pending queries. But since there are no more new queries, those queued queries will not be processed. Wait, no. Because in the code, during the processing of each new query, we process queued queries up to the current ti. But after the last query, any remaining queued queries are not processed. So this is a problem.

Wait, in the code, for the last query (i=4, ti=19), the queue after processing queued queries is empty. Then, the new query is added to the queue. But after that, there are no more queries. So the server's current_end_time is 21, and the queue has (1,4). These are not processed because there are no new queries to trigger the processing.

Thus, the code as described would miss the processing of the queued query (1,4). But according to the first sample, the fifth query (i=4) is processed and ends at 22.

Ah, this is a problem. So the code as described doesn't handle the remaining queued queries after all new queries are processed.

So the code needs to process all queued queries after all new queries are handled. But how?

Thus, the current code approach is incorrect. Because after all the queries have been processed (the for loop has completed), there may be queued queries that need to be processed. But the code only processes queued queries when new queries arrive.

So how to handle the remaining queued queries after all new queries are processed?

The answer is that after the for loop (processing all new queries), we need to process all remaining queued queries.

Thus, the correct code approach should be:

After processing all new queries, process all remaining queued queries.

But how to do this in the code.

So the steps are:

For all queries in the input:

   process them as per the code above.

Then, after all queries are processed, process the remaining queued queries.

But the problem is that the output must be in the order of the input queries. So each queued query must have their end time stored in the results array.

Thus, the code needs to process all queued queries even after all new queries have been handled.

So the code structure should be:

Initialize current_end_time =0.

queue = deque()

results = [-1]*n

for each query i in 0..n-1:

   ti, di = queries[i]

   process queued queries (current_end_time <= ti)

   handle new query.

After all queries are processed, process remaining queued queries.

But how to process the remaining queued queries after the loop?

Because there are no more new queries, the server will process all queued queries in order, one after another. So after the for loop, we need to process all queued queries.

So after the for loop:

   while queue is not empty:

       di, idx = queue.popleft()

       current_end_time += di

       results[idx] = current_end_time

But wait, in the code during the for loop, when a new query is added to the queue, the code doesn't process queued queries until the next new query arrives. But if there are no more new queries, then the queued queries will never be processed unless we handle them after the loop.

Thus, this is a critical missing step.

So in the first sample, after processing all five queries, the queue has (1,4). The code's for loop has ended, but we need to process this queued query.

So the code should, after the loop, process all remaining queued queries.

Thus, the code structure should be:

Read all queries.

Process each in order:

   for each query:

       process queued queries up to ti.

       handle the new query.

After all queries are processed:

   process all remaining queued queries.

This way, any queued queries left after all new queries are processed will be handled.

This is a crucial part that I missed earlier.

So adding this step will ensure that all queued queries are processed.

Thus, the code should be:

current_end_time = 0

queue = deque()

results = [-1] * n

for i in range(n):

   ti, di = queries[i]

   # Process queued queries as much as possible before ti

   while queue and current_end_time <= ti:

       q_di, q_idx = queue.popleft()

       current_end_time += q_di

       results[q_idx] = current_end_time

   # handle new query

   if current_end_time <= ti and not queue:

       # process immediately

       current_end_time = ti + di

       results[i] = current_end_time

   else:

       # check if can be added to queue

       if len(queue) < b:

           queue.append( (di, i) )

       else:

           results[i] = -1

# after all queries are processed, process remaining queued queries

while queue:

   q_di, q_idx = queue.popleft()

   current_end_time += q_di

   results[q_idx] = current_end_time

Thus, in the first sample, after processing all five queries, the queue has the fifth query (added at ti=19). The code's for loop has already handled queued queries up to ti=19. But after the loop, the code processes the remaining queued queries.

So the fifth query is in the queue after the for loop. So the while loop at the end processes it:

current_end_time is 21. Adding di=1 → current_end_time=22. So results[4] =22.

Thus, the code now correctly handles all queued queries.

Now, what about the data structures? Since n is up to 2e5, using a deque for the queue is efficient, as appending and popping from both ends are O(1) operations.

Now, let's test this approach against the first sample.

Sample Input 1:

5 1

Queries:

0: ti=2, di=9 → processed immediately. results[0] = 2+9=11.

1: ti=4, di=8. Server is busy (current_end_time=11>4). Queue is empty. Added to queue. results[1] = -1 (initially), but later when processed.

2: ti=10, di=9. Server is busy (11>10). Queue has size 1 (max 1). So rejected. results[2] =-1.

3: ti=15, di=2. Server is busy (11>15? No. 11 <=15). So process queued queries:

current_end_time is 11. ti=15. Queue has query1 (di=8). Process it. current_end_time becomes 11+8=19. 19>15. So loop stops. results[1] =19. Now, handle query3: server is busy (19>15). Queue is empty. So add to queue. results[3] is set later.

4: ti=19, di=1. Process queued queries up to ti=19:

current_end_time is 19. Queue has query3 (di=2). Process it. current_end_time becomes 19+2=21. 21>19. So loop stops. results[3] =21. Handle query4: server is busy (21>19). Queue is empty. Add to queue. results[4] =-1 (for now).

After for loop ends, process remaining queue:

Queue has (1,4). current_end_time=21. Process it. current_end_time becomes 22. results[4] =22.

Thus, the outputs are 11,19,-1,21,22 → correct.

Another sample: input 2.

Sample Input 2:

4 1

2 8 → query0

4 8 → query1

10 9 → query2

15 2 → query3

Sample Output:10 18 27 -1.

Let's trace.

current_end_time starts at 0.

query0: ti=2, di=8. Process immediately. current_end_time=2+8=10. results[0]=10.

query1: ti=4. current_end_time=10>4. Server busy. Queue is empty. Add to queue. results[1] =-1 (initially).

query2: ti=10. Process queued queries:

current_end_time=10 <=10. Queue has query1 (di=8). Process it. current_end_time becomes 18. results[1]=18. Now, handle query2: server is busy (18>10). Queue is empty. Add to queue. results[2] =-1 (initially).

query3: ti=15. Process queued queries up to 15:

current_end_time=18>15. So loop doesn't run. Server is busy. Queue has query2 (di=9). Queue is full (size1). So query3 is rejected. results[3]=-1.

After for loop, process remaining queue:

Queue has query2 (di=9). current_end_time=18. Process it. current_end_time becomes 27. results[2] =27.

Thus, outputs are 10,18,27,-1 → correct.

Thus, the code with the post-processing of the queue seems to handle the samples correctly.

Now, regarding the efficiency:

- Each query is processed exactly once in the for loop. The while loop during each query may process multiple queued queries, but each queued query is processed exactly once. The post-processing loop also processes each queued query once. So total operations are O(n), which is acceptable for n=2e5.

Thus, the code should be efficient.

Now, let's code this in Python.

The code will read n and b. Then read n lines of ti and di, in order. For each query, process as per above. Use a deque for the queue. Finally, process remaining queries in the queue.

Now, edge cases to consider:

- All queries are rejected. For example, b=0. Then, whenever the server is busy (which is always after the first query), new queries are added to the queue, but since b=0, they are rejected.

Wait, if b=0, then the queue can have 0 elements. So after the first query is processed, any new query when the server is busy is rejected. So if n=5, b=0. First query processed. Each subsequent query arrives when the server is busy (current_end_time > ti). So queue is full (size 0). So all are rejected.

Another case: when the server is free, but the queue is empty. The new query is processed immediately.

Another case: when the server is free, but the queue is not empty. Wait, no. If the server is free (current_end_time <= ti), then the queued queries would have been processed in the loop. So after the loop, the queue is empty.

Thus, the code should handle all cases correctly.

Thus, the code is:

Read n and b.

Read the next n lines into a list.

Initialize current_end_time to 0.

Use deque for the queue.

Process each query as per the steps.

Then process the remaining queue.

Now, implement this in Python.

But note that in Python, for large n (2e5), using input() for each line may be slow. So it's better to read all input at once.

Thus, the code will:

import sys from sys import stdin.

Read all lines at once.

But the code should work with:

import sys
from collections import deque

n, b = map(int, sys.stdin.readline().split())

queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

current_end = 0

queue = deque()

results = [-1] * n

for i in range(n):

    ti, di = queries[i]

    # process queue until current_end > ti or queue is empty

    while queue and current_end <= ti:

        q_di, q_idx = queue.popleft()

        current_end += q_di

        results[q_idx] = current_end

    # handle new query

    if current_end <= ti and not queue:

        # process immediately

        current_end = ti + di

        results[i] = current_end

    else:

        # check if queue is not full

        if len(queue) < b:

            queue.append( (di, i) )

        else:

            results[i] = -1

# process remaining queries in the queue

while queue:

    q_di, q_idx = queue.popleft()

    current_end += q_di

    results[q_idx] = current_end

print(' '.join(map(str, results)))

Yes, this should work.

Testing the first sample:

After processing query4 (ti=19), the queue has (1,4). The for loop ends, then the while loop processes it: current_end becomes 21+1=22. So results[4] =22.

Which matches the sample.

Thus, the code should be correct.
</think>

```python
import sys
from collections import deque

def main():
    n, b = map(int, sys.stdin.readline().split())
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    current_end = 0
    queue = deque()
    results = [-1] * n

    for i in range(n):
        ti, di = queries[i]
        while queue and current_end <= ti:
            q_di, q_idx = queue.popleft()
            current_end += q_di
            results[q_idx] = current_end
        if current_end <= ti and not queue:
            current_end = ti + di
            results[i] = current_end
        else:
            if len(queue) < b:
                queue.append((di, i))
            else:
                results[i] = -1

    while queue:
        q_di, q_idx = queue.popleft()
        current_end += q_di
        results[q_idx] = current_end

    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()
```