<think>
Okay, let's tackle this problem. So, the task is to track the number of unread notifications after each event. There are three types of events, and we need to process them efficiently given the constraints of up to 300,000 events. Hmm, right, because with such a high input size, we need an O(1) or O(log n) per operation approach to avoid timeouts.

Let me think about each event type:

Type 1: Add a notification to app x. So, we need to track each notification's state (read or unread). But tracking each individually could be expensive if there are a lot of them.

Type 2: Mark all notifications from app x as read. So, for app x, any existing notifications become read, and any new ones added after are still unread until marked.

Type 3: Mark the first t notifications (from all type 1 events) as read. Wait, this is the first t notifications ever generated. So even if some were already read before, this operation marks them again. So, for example, if a notification was read via type 2, then type 3 might re-read it. But the unread count is the total unread, so each notification can be read multiple times but only contributes to the count if it hasn't been read in any way.

Hmm. So each notification has to track whether it's been read by any of the three events.

Wait, no. Once a notification is read by any of the events, it's considered read. Because, for example, if a notification is in app x and type 2 event reads all of app x's notifications, then even if a type 3 event later includes that notification, it's already read. So, each notification's read state is a boolean: read or unread.

But the problem is, for each notification, we need to track whether it has been read by any of the operations. So the challenge is to efficiently track which notifications are read and which aren't.

But with up to 3e5 events, each of type 1 can generate a notification. So the total number of notifications can be up to 3e5. So we need an O(1) per operation approach for handling each event.

Let's think about how to model each notification.

Alternative approach: For each notification (each type 1 event), track when it was created. Then, for each app x, track the last time all notifications were read (type 2). Also, track the maximum t from type 3 events. Then, for a notification generated at time i (the i-th event of type 1), it is considered read if either:

- The app x's last read time (from type 2) is after i, OR

- The maximum t3 (from type 3) is >= i.

Wait, that's a clever way. Because for a notification created in the i-th type 1 event:

- If there's a type 3 event with t >= i, then this notification is marked as read.

- If there's a type 2 event for app x that happened after the notification was created (i.e., the app's last read time is >= i), then the notification is read.

Otherwise, it's unread.

So, the total unread is the number of notifications (type 1 events) that are not covered by any of these two conditions.

So, this approach avoids tracking each individual notification's read status. Instead, we can compute for each notification whether it's read based on the latest type 2 per app and the latest type 3.

That's a key insight! Because this way, we don't need to process each notification for each query. We can just track for each app the last time (type 2) all notifications were read, and track the maximum t3 (type 3's t) so far.

So, let's formalize this:

Each type 1 event adds a notification. Let's assign each notification a global index, say, in the order they are added. For example, the first type 1 event is notification 1, the second is 2, etc. Then, for each type 3 event with t=ti, all notifications with index <= ti are considered read (but only if ti is larger than the previous max t3). So, the maximum t3 is the largest t seen in any type 3 event.

For type 2 events, each app x has a last_read_time (the maximum between its previous last_read_time and the current event's position). Wait, no. Because when you process a type 2 event, all notifications for app x up to that point are marked as read. So, the last_read_time for app x would be the current global time (the total number of type 1 events so far). Wait, no. Because the type 2 events can happen at any time. For example, a type 2 event on app x when there are 5 type 1 events so far would mark all notifications in app x (those added before or at event 5) as read. So, the last_read_time for app x is updated to the current count of type 1 events at that moment.

Wait, perhaps not. Because type 1 events are the only ones that generate notifications. Let's track the number of notifications generated so far. Let's call this variable 'current_notification_count'. Each time a type 1 event is processed, current_notification_count increases by 1, and that notification is assigned an index of current_notification_count.

Then, when a type 2 event (for app x) occurs, the last_read for app x is set to current_notification_count. Because any notification in app x with index <= last_read[x] is considered read.

Similarly, when a type 3 event occurs with t=ti, we need to track the maximum t3 so far. Because any notification with index <= t3 is considered read.

So, for each notification i (1-based), the notification is considered read if:

- i <= max_t3 OR

- i <= last_read[app_x], where app_x is the app that generated notification i.

If either of these is true, then it's read; else, unread.

So, the total unread is the total number of notifications minus the number of notifications that are read (i.e., those that satisfy either condition).

But how do we compute the number of read notifications efficiently?

Let's break it down into two parts:

1. Notifications read by type 3 events: all notifications with index <= max_t3.

2. Notifications read by type 2 events: for each app x, all notifications in x with index > max_t3 (since those <= max_t3 are already covered) and index <= last_read[x].

Wait, but type 3's max_t3 could be larger than the last_read[x] for some apps, which would already include those notifications. So, the correct way is:

A notification is read if:

i <= max_t3 OR (i's app x has last_read[x] >= i).

So, the total read is the count of notifications where i <= max_t3, plus the count of notifications where i > max_t3 and i <= last_read[x] (where x is the app of notification i).

But how can we compute this efficiently?

Because for each notification, we need to know which app it belongs to and its index.

Hmm. Let's model the problem as follows:

We can precompute all type 1 events and keep a list for each app x of the notifications it has generated. However, this might be memory-intensive if each app has many notifications. But with 3e5 total notifications, and each stored once, this is manageable.

Wait, but perhaps we can track for each app x:

The number of notifications in x that are beyond max_t3 and are <= last_read[x].

But how?

Alternatively, for each app x, the number of notifications in x that are > max_t3 and <= last_read[x] is the number of notifications in x that were added after max_t3 but before or at last_read[x].

But max_t3 can change over time. So, when max_t3 increases, some of these notifications may be moved into the max_t3 coverage.

This seems complicated.

Alternatively, for each app x, let's track:

- The total number of notifications in x (count[x]).

- The number of notifications in x that are <= max_t3. This can be computed by the number of notifications in x with index <= max_t3. Which is the same as the number of notifications in x up to max_t3.

Wait, but each notification has an index. For each app x, perhaps we can track all the indices of notifications in x. Then, given max_t3, the number of notifications in x that are <= max_t3 is the upper_bound of max_t3 in x's list of indices.

But that's O(log k) for each app x. However, when we need to compute the total unread for each event, this could be O(n), which is 3e5 per query, leading to O(3e5 * 3e5) operations which is 9e10, which is way too slow.

So, this approach is not feasible.

Hmm. So we need a way to compute the total unread efficiently.

Let me think again.

The total unread is the total number of notifications generated so far (current_notification_count) minus the number of read notifications.

The read notifications are those that are either:

- Covered by max_t3 (i <= max_t3), OR

- Covered by their app's last_read (i > max_t3 and i <= last_read[x]).

So, the count of read notifications is:

number of notifications <= max_t3 (let's call this A) + number of notifications where i > max_t3 and i <= last_read[x] (call this B).

So, the problem reduces to computing A and B.

A is the number of notifications generated in the first max_t3 type 1 events. So, if max_t3 is 5, then A is 5 (assuming all type 1 events up to the 5th are part of the count). Wait, no. Because each type 1 event adds exactly one notification. So, max_t3 is the number of notifications that are covered by type 3 events. So, A is simply the value of max_t3. Because each type 1 event adds a notification with index 1, 2, 3, etc. So, if max_t3 is t, then there are t notifications covered by type 3.

Wait, but in a type 3 event, the t is the number of type 1 events that occurred before. For example, if the first three events are type 1, then a type 3 with t=3 would mark all three notifications. If then another type 1 happens (4th notification), then a type 3 with t=3 would still mark the first three.

So yes, A is the minimum between max_t3 and current_notification_count (but since type 3 events are only processed when there were at least t type 1 events before, so t can't be larger than the current_notification_count at that time. So when processing a type 3 event, t is <= current_notification_count. But after that, more type 1 events can occur. So, when the max_t3 is, say, 5, and current_notification_count is 10, then A is 5.

So, A is the value of max_t3 (since it's always <= current_notification_count).

Wait, no. Because if current_notification_count is 10, and max_t3 is 5, then there are 5 notifications covered by type 3. So A is 5.

So A is simply the maximum between 0 and the current max_t3. Because max_t3 could be 0 if no type 3 events have occurred.

So, A is the max_t3.

Then B is the sum over all apps x of the number of notifications in x that are > max_t3 and <= last_read[x].

But how to compute B efficiently?

Hmm.

Each app x has last_read[x], which is the last time (notification count) when all notifications in x were marked as read (type 2). So for app x, any notification in x with index <= last_read[x] is considered read. But if the notification is <= max_t3, it's already counted in A. So the notifications counted in B are those in app x where index > max_t3 and <= last_read[x].

So for app x, the number of such notifications is the number of notifications in x with index in (max_t3, last_read[x]].

So for each app x, we need to know how many notifications it has generated that fall into this interval.

But how?

We can track for each app x, the list of indices of its notifications, sorted in order (since they are generated sequentially). Then, for each x, the number is the upper_bound of last_read[x] in x's list minus the upper_bound of max_t3 in x's list.

But with 3e5 apps and 3e5 notifications, this would take O(q) time per query, which is not feasible.

Alternative idea: For each app x, keep track of the total number of notifications in x, and the number of notifications in x that are <= max_t3. Then, the number of notifications in x that are > max_t3 and <= last_read[x] is max(0, min(last_read[x], count[x]) - max_t3_count[x]).

Wait, maybe not. Let's think.

Suppose app x has generated m notifications. The number of notifications in x that are <= max_t3 is the number of notifications in x with index <= max_t3. Let's denote this as cnt_3[x].

Similarly, the number of notifications in x that are <= last_read[x] is the number of notifications in x with index <= last_read[x], which is the number of notifications in x with index <= min(last_read[x], current_notification_count). Let's denote this as cnt_2[x].

But how to track cnt_3[x] and cnt_2[x]?

Alternatively, for each app x, the count of notifications that are > max_t3 and <= last_read[x] is max(0, min(last_read[x], current_notification_count) - max_t3) if the app x's notifications in that range are all present.

Wait, no. Because the app x's notifications may have some indices between max_t3 and last_read[x], but not all. For example, app x could have notifications with indices 1,3,5. max_t3 is 2, last_read[x] is 4. Then, the indices between 2 and 4 are 3 and 4. But app x's notifications in this range are 3 (since 4 is not present). So the count is 1.

But how to track this?

This seems complicated. So perhaps we need to pre-process for each app x, the list of notification indices, sorted, and for each query, compute for each app x the number of notifications in x that are in (max_t3, last_read[x]] by using binary search. However, with 3e5 apps and 3e5 queries, this would be O(n) per query which is O(9e10) operations.

So this approach is not feasible.

Alternative approach:

Let’s precompute for each app x the number of notifications it has up to each possible index.

But since the index can be up to 3e5, this would require a lot of memory.

Hmm. Let's think of the problem differently. Let's track for each app x:

- The total number of notifications in x: count[x].

- The earliest notification in x that is after max_t3 and after the app's last_read[x].

Wait, perhaps not.

Alternatively, let's track for each app x, the last_read[x]. Then, for app x, the number of notifications that are > max_t3 and <= last_read[x] is the number of notifications in x that are in the range (max_t3, last_read[x]].

This can be computed as the number of notifications in x that are <= last_read[x] minus the number of notifications in x that are <= max_t3.

So, for each app x:

number = (number of notifications in x <= last_read[x]) - (number of notifications in x <= max_t3).

The sum of this over all apps is B.

Then, total unread is current_notification_count - (A + B).

So the problem reduces to efficiently calculating (sum over x [ (number of notifications in x <= last_read[x]) - (number of notifications in x <= max_t3) ]) for B.

But how to compute this sum?

Let’s think of two separate sums:

sum1 = sum over x (number of notifications in x <= last_read[x])

sum2 = sum over x (number of notifications in x <= max_t3)

Then B = sum1 - sum2.

So total read is A + B = max_t3 + (sum1 - sum2).

Then, total unread is current_notification_count - (max_t3 + sum1 - sum2).

So the problem becomes how to compute sum1 and sum2 efficiently.

sum1: sum over all apps x of the number of notifications in x <= last_read[x].

But last_read[x] is the last time a type 2 event was applied to x, and it's possible that last_read[x] could be greater than the number of notifications in x. For example, if x has 5 notifications, and then a type 2 event is processed, last_read[x] is set to the current_notification_count at that time (say, 10). Then, the number of notifications in x <= last_read[x] is 5 (since x only has 5 notifications, all are <= 10).

So, for sum1, for each x, it's min(count[x], last_read[x]).

But how to track sum1?

sum1 is the sum of min(count[x], last_read[x]) for all x.

But how to track this in O(1) per query. Because each time a type 2 event occurs, last_read[x] is set to current_notification_count (the number of type 1 events so far at that time). So for each x, sum1's contribution is min(count[x], last_read[x]).

But sum1 can't be computed on the fly each time, because that's O(n) per query. So we need a way to track sum1 efficiently.

Similarly, sum2 is the sum over x of the number of notifications in x with index <= max_t3. Which is the sum for each x of the number of notifications in x that were generated in the first max_t3 type 1 events.

But how to track this?

Hmm. Let's think of sum2 as the sum over x of the count of notifications in x up to index max_t3.

But how is this possible? For example, max_t3 is 5. For app x, which has notifications at indices 1,3,5. Then, the count would be 3. For another app y with indices 2,4,6, the count is 2 (indices 2,4 <=5). So sum2 is the sum of these counts across all apps.

But how to compute this efficiently?

This seems challenging. Because for each app x, the notifications are generated in order, and their indices are sequential. So for each x, the number of notifications in x with index <= max_t3 is the number of such notifications. Since the notifications for x are added in order, their indices are in the order of their creation. So for x, the count is the upper_bound of max_t3 in the list of indices for x.

But again, for 3e5 apps, this is O(n) per query, which is not feasible.

Alternative idea: Since all notifications are generated in order, the indices are consecutive. For each app x, the list of notification indices is a list of the positions where type 1 events for x occurred. For example, if app x had type 1 events at the 3rd, 5th, and 7th type 1 events, then their indices are 3,5,7.

So for app x, the count of notifications with index <= max_t3 is the number of indices in x's list that are <= max_t3.

But how to track this across all apps?

We can't track this for each app in O(1) time. So perhaps we need a global array that tracks for each type 1 event (each notification) which app it belongs to. Then, sum2 is the number of notifications in this array up to max_t3, but grouped by app x. But this is O(max_t3) to compute sum2, which is O(3e5) per query. Again, not feasible.

Hmm. So this approach is leading to a dead end.

Alternative approach: Let's precompute for each app x a list of the number of notifications added up to each type 1 event. For example, for app x, each time a notification is added, we can track the cumulative count. But this would require O(n) space per app, which is not feasible.

Alternatively, since notifications are added in order, perhaps for each app x, the notifications are added in the order of their indices. So, for app x, the list of indices is sorted. So, for a given max_t3, the number of notifications in x with index <= max_t3 is the upper_bound in x's list of indices for max_t3.

But how to compute the sum over all x of this upper_bound?

This seems impossible unless we can find a way to compute this sum incrementally.

Wait, but max_t3 is only updated during type 3 events. So when a type 3 event occurs, we can compute the new sum2 once and store it. But sum2 would need to be stored and updated only when max_t3 changes. For other events (type 1 or 2), sum2 remains the same.

Similarly, sum1 is only updated when a type 2 event occurs for some x, which changes last_read[x], thus affecting sum1's contribution from x.

So perhaps we can track sum1 and sum2 as variables, and update them incrementally.

Let's see:

For sum1:

Each time a type 2 event occurs on app x:

- The previous contribution of x to sum1 was min(count[x], old_last_read[x]).

- The new contribution is min(count[x], new_last_read[x]).

sum1 is updated by (new_contribution - old_contribution).

For example, if x had 5 notifications and old_last_read[x] was 3 (contribution 3), and a type 2 event sets last_read[x] to 10, then new contribution is 5. So sum1 increases by 2.

So sum1 can be tracked incrementally. Whenever a type 2 event occurs on app x, compute the delta (new_contribution - old_contribution) and add it to sum1.

This way, sum1 can be maintained with O(1) per type 2 event.

For sum2:

sum2 is the sum over all x of the number of notifications in x with index <= max_t3. But max_t3 is updated only during type 3 events. So whenever a type 3 event occurs (and increases max_t3), sum2 needs to be recomputed.

But how to recompute sum2 efficiently.

Wait, sum2 is equal to the number of notifications generated in the first max_t3 type 1 events. Because each type 1 event contributes exactly one notification. So, sum2 is max_t3. Because each notification in the first max_t3 events is counted once in their respective app. So sum of all x's count of notifications in the first max_t3 events is exactly max_t3.

Wait, no. Because sum over x of (number of notifications in x with index <= max_t3) is equal to the number of notifications with index <= max_t3. Which is exactly max_t3. Because each notification in the first max_t3 type 1 events is counted once, and they are all part of the sum. So sum2 is equal to max_t3.

Wait, this is a key insight! Because the first max_t3 type 1 events generate exactly max_t3 notifications, each with indices 1 to max_t3. So sum2, which is the sum over x of the number of notifications in x with index <= max_t3, is exactly the number of such notifications. Which is max_t3. Because each of these notifications belongs to some app, and in sum2, we're counting all of them once. So sum2 is exactly max_t3.

So sum2 = max_t3.

Oh! That's brilliant. So sum2 is simply the value of max_t3. So B = sum1 - sum2 = sum1 - max_t3.

So the total read is A + B = max_t3 + (sum1 - max_t3) = sum1.

Wait, that can't be right. Because A is the number of notifications read via type 3 (max_t3), and B is the sum1 - max_t3 (the notifications read via type 2 that are not covered by type 3). So the total read is A + B = max_t3 + (sum1 - max_t3) = sum1.

But sum1 is the sum over x of min(count[x], last_read[x]). Which is the number of notifications read via type 2 events, but only those that are beyond max_t3.

Wait, but this seems to be conflicting with the previous approach. But according to this new insight, sum2 is equal to max_t3, which simplifies everything.

So this changes everything. So the total read is sum1 (sum1 = sum over x of min(count[x], last_read[x])).

Wait, no. Because sum1 is the sum of min(count[x], last_read[x]), which counts all notifications in x that are <= last_read[x]. But any notification that is <= max_t3 is already counted in max_t3. So sum1 is the sum of notifications read by type 2, but including those that are also covered by type 3. Then, B is sum1 - max_t3, which is the notifications read by type 2 that are not in type 3. So total read is A + B = max_t3 + (sum1 - max_t3) = sum1. But how?

Wait, no. Let me re-express:

A = max_t3 (number of notifications covered by type 3)

B = sum1 - sum2 = sum1 - max_t3 (since sum2 = max_t3)

So total read is A + B = max_t3 + (sum1 - max_t3) = sum1.

But sum1 is the sum of min(count[x], last_read[x]) for all x. But last_read[x] is the value set by type 2 events. So sum1 is the total number of notifications that have been marked as read by type 2 events, regardless of whether they were already read by type 3 events.

But if a notification was covered by type 3 (i <= max_t3), then it's already counted in A. But when calculating sum1, we include it again in sum1. So B would subtract those notifications (sum2 = max_t3), resulting in B being sum1 - sum2.

But this would mean that A + B equals sum1, but sum1 could be larger than the actual total read. Because sum1 counts all notifications read by type 2 events, including those already covered by type 3.

This can't be right. So there must be a mistake in this reasoning.

Wait, let's think of a concrete example.

Suppose there is a notification with index 1, app x.

Then, a type 3 event with t=1 (max_t3 =1), which marks it as read.

Then a type 2 event on app x, which sets last_read[x] =1 (assuming current_notification_count is 1 at that time).

sum1 would be min(1,1) =1.

sum2 is max_t3 =1.

B = sum1 - sum2 =0.

A + B = 1 +0=1.

Total read is 1, which is correct.

Another example: notification 1 is app x. Type 2 event on x sets last_read[x] =1. Then, type 3 event with t=0 (which is not allowed, but suppose it's allowed). Then max_t3 is 0.

sum1 is 1, sum2 is 0. B=1-0=1. A=0. So total read is 0+1=1.

Which is correct.

Another example: notification 1 (x), notification 2 (y).

Type 3 event t=2 (max_t3=2). So all notifications are read (A=2).

Type 2 event on x: last_read[x] =2. sum1 becomes min(1,2) + min(1,0) for y (assuming y's last_read is 0). So sum1 is 1 +0 =1.

sum2=2.

B=1-2= -1. A+B=2 + (-1) =1. But the total read is 2, not 1.

Wait, this shows that the previous reasoning is flawed.

Wait, in this example:

After type 3 event with t=2, both notifications are read.

Then, type 2 event on x, which has count[x]=1. last_read[x] is set to 2 (current_notification_count is 2).

sum1 for x is min(1,2) =1. For y, last_read[y] is 0 (assuming no type 2 event), sum1 for y is min(1,0) =0. sum1 is 1+0=1.

sum2 is max_t3=2.

B= sum1 - sum2 =1-2=-1.

A is 2. So total read is 2-1=1. But in reality, all notifications are already read by type 3 event. So the sum1's contribution here is incorrect.

This indicates that the approach is wrong.

So where is the mistake?

Ah, the mistake is that sum1 is the sum of min(count[x], last_read[x]) for all x, which is the total number of notifications that would be read by type 2 events if there were no type 3 events. But when type 3 events are present, notifications that are already covered by type 3 are already counted in A, and type 2 events on x can also mark them as read again, which doesn't change their status.

But according to the problem statement, a notification is read if either of the conditions is true. So if a notification is covered by type 3, then even if the type 2 event's last_read[x] is less than the notification's index, it's still read.

So the total read is the number of notifications where (i <= max_t3) OR (i > max_t3 and i <= last_read[x]).

So the total read is:

number of notifications <= max_t3 (A) + number of notifications > max_t3 and <= last_read[x] (B).

Which is A + B.

But according to this new insight, sum2 (sum over x of notifications in x <= max_t3) is equal to A (max_t3), since all notifications up to max_t3 are counted once.

So sum2 = A.

Then B is sum over x of (number of notifications in x where i > max_t3 and i <= last_read[x]).

But how to compute B?

This is the sum over x of max(0, min(last_read[x], count[x]) - max_t3) if the app's notifications have indices in this range.

But again, this requires knowing for each app x how many of their notifications are in the range (max_t3, last_read[x]].

So this can be written as:

B = sum over x ( min( count[x], last_read[x] ) - max_t3 ) if min(...) > max_t3, else 0.

Which is equivalent to:

B = sum over x ( max( 0, min( count[x], last_read[x] ) - max_t3 ) )

But how to compute this sum efficiently.

Hmm. Let's reorganize this:

sum over x ( max( 0, min( count[x], last_read[x] ) - max_t3 ) )

= sum over x ( min( count[x], last_read[x] ) - max_t3 ) when min(...) > max_t3, else 0.

= sum over x ( max( min( count[x], last_read[x] ), max_t3 ) - max_t3 )

So this can be rewritten as:

sum over x ( ( min(count[x], last_read[x] ) >= max_t3 ) ? ( min(count[x], last_read[x] ) - max_t3 ) : 0 )

But how to compute this?

This is equivalent to sum over x ( min(count[x], last_read[x] ) - max_t3 ) where min(...) >= max_t3.

Which is sum over x ( min(count[x], last_read[x] ) - max_t3 ) if min(...) >= max_t3, else 0.

But this is the same as sum over x ( max(0, min(count[x], last_read[x] ) - max_t3 ) )

This sum is B.

So total read is A + B = max_t3 + B.

The total unread is current_notification_count - (max_t3 + B).

But how to compute B efficiently.

Ah, but sum1 is sum over x ( min(count[x], last_read[x] ) ).

So B is sum1 minus sum over x ( max_t3 if min(count[x], last_read[x] ) >= max_t3 else min(count[x], last_read[x] ) )

Wait, no. Let's see:

B = sum over x ( max(0, min(count[x], last_read[x] ) - max_t3 ) )

= sum over x ( min(count[x], last_read[x] ) - max_t3 ) when min(...) >= max_t3.

So B = sum over x ( (min(...) >= max_t3 ) ? (min(...) - max_t3) : 0 )

Which can be rewritten as sum over x ( min(...) >= max_t3 ) * ( min(...) - max_t3 )

But this still doesn't help us compute it efficiently.

Alternative Idea: For each app x, track min(count[x], last_read[x]). Let's call this value s[x]. So sum1 is sum(s[x] for all x).

B is sum(max(s[x] - max_t3, 0) for all x).

But sum(max(s[x] - max_t3, 0)) can be written as sum(s[x] for s[x] > max_t3) - max_t3 * (number of x where s[x] > max_t3).

But how to compute this sum?

This seems difficult unless we can find a data structure that can track all s[x] and allow us to query the sum of s[x] where s[x] > K, for a varying K (where K is max_t3).

But maintaining such a data structure for 3e5 elements is challenging.

Alternatively, since max_t3 can only increase over time (because each type 3 event has t >= previous max_t3?), no. Wait, no. For example, there can be two type 3 events: first with t=5, then with t=3. Then max_t3 would be 5. Because each type 3 event's t is the number of type 1 events before the event. But when a type 3 event is processed, t must be <= current_notification_count. But the previous max_t3 could be larger than the current event's t. For example, if there was a type 3 event with t=5 when current_notification_count was 5, then another type 3 event with t=3. The max_t3 would remain 5. So max_t3 is the maximum of all t from type 3 events processed so far.

So max_t3 is non-decreasing. Because each new type 3 event's t can be larger or smaller than the previous, but max_t3 is updated to the maximum between current max_t3 and t. So, once max_t3 increases, it never decreases.

This is a crucial observation. Because max_t3 is non-decreasing, we can exploit this property.

So, max_t3 starts at 0. Whenever a type 3 event occurs, we set max_t3 to max(max_t3, t).

Thus, max_t3 is a non-decreasing variable.

This implies that when we process events, the max_t3 can only stay the same or increase. So, for B, since max_t3 is non-decreasing, the sum B can be computed incrementally.

But how?

Let’s think again. B is sum over x ( max(s[x] - max_t3, 0) ).

Since max_t3 can only increase, each time max_t3 increases, the B sum can decrease or stay the same.

But maintaining this sum would require knowing, for each x, whether s[x] is greater than max_t3.

But again, without a way to track this, it's challenging.

Alternative Idea: We can track the sum B for the current max_t3. Each time max_t3 increases, we subtract the difference between the new max_t3 and old max_t3 multiplied by the number of x where s[x] >= new max_t3.

Wait, this is getting complicated.

Alternatively, since max_t3 is non-decreasing, when it increases from prev_max to new_max, the delta is new_max - prev_max. For each x where s[x] >= prev_max, the contribution to B is reduced by delta. But for x where s[x] >= new_max, the contribution is max(s[x] - new_max, 0) = (s[x] - new_max). For those where s[x] is between prev_max and new_max, their contribution becomes zero.

So, when max_t3 increases to new_max, B becomes sum( max(s[x] - new_max, 0) for all x ).

But how to compute this sum efficiently.

This seems like a problem that can be addressed with a binary indexed tree or a segment tree that can track the sum of s[x] where s[x] > K, and the count of x where s[x] > K.

But given that n and q are up to 3e5, and each operation must be O(log n), this is feasible.

So, the plan is:

- For each app x, track s[x] = min(count[x], last_read[x]).

- Maintain a frequency array (or a binary indexed tree) that allows us to query:

   a) The number of x where s[x] >= K.

   b) The sum of s[x] where s[x] >= K.

These two values can be used to compute B for a given max_t3:

B = sum(s[x] >= max_t3) ? (sum_s_ge_k - max_t3 * count_ge_k) : 0.

Thus, each time max_t3 increases to new_max, B can be computed as (sum_s_ge_new_max - new_max * count_ge_new_max).

But how to maintain the frequency array.

This requires maintaining a sorted list of s[x] values, and being able to query the sum of all s[x] >= K and the count.

This can be done with a binary indexed tree (Fenwick tree) or a segment tree, but since s[x] can be up to 3e5 (since current_notification_count can be up to q which is 3e5), the range is manageable.

So, the steps are:

Initialize all s[x] = 0 (since initially, no notifications and last_read[x] is 0, so min(count[x]=0, last_read[x]=0) is 0).

Maintain a Fenwick tree that tracks the frequency of each s[x] value, and another Fenwick tree that tracks the sum of s[x] for each possible value.

Alternatively, a single Fenwick tree that for each possible s[x] value, stores the count and the sum.

So, for example, when s[x] changes from old_value to new_value, we subtract old_value from the sum and add new_value. Similarly, decrement the count for old_value and increment for new_value.

But implementing this would require a Fenwick tree that can handle these operations.

Alternatively, since the possible s[x] values can be up to 3e5, we can use a Fenwick tree (or a segment tree) that is capable of range sum and range count queries.

For example:

- Whenever s[x] changes, we first remove the old value from the data structure and add the new value.

Then, when we need to compute sum_s_ge_k and count_ge_k, we can query the sum of all entries >= k and the count of entries >=k.

This can be done using a binary indexed tree with coordinate compression, but since the s[x] can be up to 3e5, we can use a Fenwick tree in the following way:

The Fenwick tree will have indexes up to 3e5 + 1. For each s[x], we update the tree at position s[x]. The tree can support prefix sums and counts. To find the sum and count of s[x] >= k, we can compute the total sum minus the prefix sum up to k-1, and similarly for the count.

So, here's how it would work:

- The sum of s[x] >=k is sum_total - prefix_sum(k-1).

- The count of s[x] >=k is count_total - prefix_count(k-1).

But maintaining a Fenwick tree for sum and another for count would be needed.

So, let's proceed.

We'll have two Fenwick trees:

1. A sum_tree that tracks the sum of s[x] for each value.

2. A count_tree that tracks the number of s[x] for each value.

When s[x] changes from old to new:

- Decrement sum_tree at old by old.

- Decrement count_tree at old by 1.

- Increment sum_tree at new by new.

- Increment count_tree at new by 1.

When querying for a given k:

sum_ge_k = sum_tree.query_range(k, max_possible)

count_ge_k = count_tree.query_range(k, max_possible)

Then B = sum_ge_k - k * count_ge_k.

So, this way, whenever max_t3 changes, we can compute B in O(log max_possible) time.

Now, let's outline the steps for each event type:

Type 1 (add notification to x):

- Increment current_notification_count by 1.

- count[x] +=1.

- s[x] is min(count[x], last_read[x]).

   Since count[x] has increased by 1, s[x] could be min(prev_count+1, last_read[x]).

   So, if last_read[x] >= prev_count+1, then s[x] increases by 1.

   Else, s[x] remains at prev_count.

   So, we need to check whether last_read[x] >= new count[x].

   If yes, then s[x] increases to count[x].

   Else, s[x] remains at last_read[x].

   So, the new s[x] is min(count[x], last_read[x]).

So, whenever a type 1 event occurs, we need to:

   prev_s = s[x]

   new_s = min(count[x], last_read[x])

   if new_s != prev_s:

       update the Fenwick trees: subtract prev_s, add new_s.

       s[x] = new_s

Then, after this, for the current event, the unread is current_notification_count - (max_t3 + B), where B is sum_ge_k - k*count_ge_k, with k = max_t3.

But wait, the current_notification_count is the number of type 1 events processed so far. So, each type 1 event increases it by 1.

Type 2 (read all notifications in x):

   prev_s = s[x]

   last_read[x] = current_notification_count (the number of type 1 events so far)

   new_s = min(count[x], last_read[x])

   if new_s != prev_s:

       update the Fenwick trees: subtract prev_s, add new_s.

       s[x] = new_s

Type 3 (read first t notifications):

   new_max_t3 = max(max_t3, t)

   if new_max_t3 > max_t3:

       max_t3 = new_max_t3

   Then, B is computed as sum_ge_k - k*count_ge_k, where k is max_t3.

But how to compute sum_ge_k and count_ge_k:

   sum_ge_k = sum_tree.get_sum_ge(k)

   count_ge_k = count_tree.get_count_ge(k)

   B = sum_ge_k - k * count_ge_k

Then, the total unread is current_notification_count - (max_t3 + B)

So, for each event, after processing it, we compute:

unread = current_notification_count - (max_t3 + (sum_ge_k - max_t3 * count_ge_k))

= current_notification_count - max_t3 - sum_ge_k + max_t3 * count_ge_k

= current_notification_count - sum_ge_k + max_t3 * (count_ge_k - 1)

Wait, but this may not be the case. Let's re-express:

unread = current_notification_count - (max_t3 + B)

But B = sum_ge_k - max_t3 * count_ge_k.

So:

unread = current_notification_count - max_t3 - (sum_ge_k - max_t3 * count_ge_k)

= current_notification_count - sum_ge_k + max_t3 * (count_ge_k - 1)

But I think it's easier to compute B as (sum_ge_k - max_t3 * count_ge_k) and then calculate current_notification_count - (max_t3 + B).

Now, the problem is to implement this efficiently.

Now, the steps:

Implement Fenwick trees for sum and count.

For each app x, track count[x], last_read[x], and s[x] = min(count[x], last_read[x]).

For each event:

- Process the event.

   For type 1:

      current_notification_count +=1.

      app x is given.

      count[x] +=1.

      new_s = min(count[x], last_read[x]).

      if new_s != s[x]:

          update Fenwick trees.

          s[x] = new_s.

   For type 2:

      app x is given.

      last_read[x] = current_notification_count.

      new_s = min(count[x], last_read[x]).

      if new_s != s[x]:

          update Fenwick trees.

          s[x] = new_s.

   For type 3:

      t is given.

      new_max_t3 = max(max_t3, t).

      if new_max_t3 > max_t3:

          max_t3 = new_max_t3.

   After processing the event, compute B = sum_ge_k - max_t3 * count_ge_k, where k = max_t3.

   Then, unread = current_notification_count - (max_t3 + B).

   Print unread.

Now, the key is to implement the Fenwick trees to support efficient sum and count queries for s[x] >= k.

Implementing the Fenwick tree:

The sum and count trees are separate Fenwick trees. Each Fenwick tree will support point updates and prefix sum queries.

For example, to get the sum of all s[x] >= k, we can compute the total sum minus the prefix sum up to k-1.

Similarly for count.

So, the Fenwick tree for sum would have the sum of s[x] entries, and the Fenwick tree for count would have the count of s[x] entries.

The maximum possible s[x] can be up to current_notification_count, which can be up to 3e5. So the Fenwick trees need to handle indices up to 3e5 + 1.

Implementing the Fenwick tree for sum and count:

Each Fenwick tree is initialized with size 3e5 + 2.

For a query of sum >= k:

sum_ge_k = sum_tree.query(MAX_INDEX) - sum_tree.query(k-1)

Similarly for count_ge_k.

Thus, each query is O(log MAX_INDEX).

Now, let's test this approach against the sample inputs.

Sample Input 1:

3 4

1 3

1 1

1 2

2 3

Processing:

Initially, count = [0,0,0], last_read = [0,0,0], s = [0,0,0]. Fenwick trees sum is 0, count is 3 zeros.

Event 1: Type 1, x=3 (1-based).

current_notification_count =1.

count[3] becomes 1.

last_read[3] is 0.

new_s = min(1, 0) =0. So no change in s[3].

So, Fenwick trees remain the same.

B is sum_ge_k where k=0.

sum_ge_0 is sum_tree.total - sum_tree.query(-1) which is sum_tree.total (0).

count_ge_0 is count_tree.total (3). So B = 0 - 0*3=0.

unread =1 - (0+0) =1.

Output 1.

Event 2: Type 1, x=1.

current_notification_count=2.

count[1] =1.

last_read[1]=0.

new_s = min(1,0)=0. No change.

B remains same. max_t3=0.

unread=2 -0-0=2.

Output 2.

Event3: Type1, x=2.

count[2] =1.

new_s = min(1,0)=0. No change.

current_notification_count=3.

B=0.

unread=3-0-0=3. Output3.

Event4: Type2, x=3.

last_read[3] is set to current_notification_count=3.

count[3] is 1.

new_s = min(1,3) =1.

prev_s was 0.

So, subtract 0 from sum and count trees, add 1.

sum_tree now has 1.

count_tree has 1 (for x=3).

Now, B is sum_ge_0 (sum=1, count=1 + others s[x]=0, which count_ge_0 is 3).

Wait, after updating x=3's s to 1:

sum_tree has:

sum of all s[x] =1 (x=3) + 0 (x=1, 2) =1.

count_tree has 1 (s=1) and 2 (s=0).

When k=0 (max_t3 is 0):

sum_ge_0 =1 + 0 +0=1.

count_ge_0=3 (1 for s=1, 2 for s=0).

So B=1 -0*3=1.

unread=3 - (0 +1) =2. Output2.

Which matches the sample.

Another sample:

Sample Input 2:

4 6

1 2

1 4

1 2

3 3

1 3

1 3

Let's walk through this:

Initial: count[1-4]=0, last_read=0 for all.

current_notification_count=0.

max_t3=0.

Fenwick trees sum=0, count=4 (s=0 for all 4 apps).

Event1: Type1, x=2.

count[2]=1.

s[x=2] = min(1, 0) =0.

No change. Fenwick trees remain sum=0.

current_notification_count=1.

B is sum_ge_0 - 0 * count_ge_0 =0 -0*4=0.

unread=1-0-0=1. Output1.

Event2: Type1, x=4.

count[4]=1.

s[x=4] =0. No change.

current_notification_count=2.

B=0.

unread=2-0=2. Output2.

Event3: Type1, x=2.

count[2] becomes 2.

s[x=2] = min(2, 0) =0. No change.

current_notification_count=3.

unread=3-0=3. Output3.

Event4: Type3, t=3.

max_t3 is max(0,3) =3.

B is sum_ge_3 -3 * count_ge_3.

current_notification_count=3.

sum_ge_3: sum of s[x] >=3. All s[x] are 0 except x=2 and 4, which are 0. So sum_ge_3 is 0.

count_ge_3 is 0.

B=0 -3*0=0.

unread=3 - (3 +0) =0. Output0.

Event5: Type1, x=3.

count[3] =1.

s[x=3] = min(1,0) =0. No change.

current_notification_count=4.

max_t3=3.

B= sum_ge_3 (0) -3*0=0.

unread=4 -3=1. Output1.

Event6: Type1, x=3.

count[3] =2.

s[x=3] =0. No change.

current_notification_count=5.

unread=5-3=2. Output2.

This matches the sample.

So the approach works for the samples.

Now, the code.

We need to:

- Read n and q.

- Initialize for each app x (from 1 to n), count[x] =0, last_read[x]=0, s[x]=0.

- Initialize Fenwick trees for sum and count. The initial s[x] for all apps is 0, so the count_tree has n entries at 0, and sum_tree has 0 * n.

But wait, initial s[x] is 0 for all apps, so the count_tree for 0 is n, sum_tree for 0 is 0 * n =0.

So, during initialization:

sum_tree.add(0, 0 *n) ?

No. Wait, each s[x] is initially 0. So for each of the n apps, we have s[x]=0. So the sum is 0 *n =0. So sum_tree initially has 0 at position 0, added n times. But no, Fenwick tree for sum is initially empty. So we need to perform n updates of adding 0.

But that would take O(n) time, which is 3e5 steps. That's acceptable.

But for n up to 3e5, that's manageable.

But that's O(n) time, which is feasible for Python.

Alternatively, since all apps start with s[x]=0, the sum is 0 *n, and count_tree has count 0 is n.

So, the Fenwick trees can be initialized by adding 0, n times.

But for n up to 3e5, this is manageable.

So, the code outline:

Read n, q.

Initialize:

current_notification_count =0

max_t3=0

count = [0]*(n+1)  # apps are 1-based.

last_read = [0]*(n+1)

s = [0]*(n+1)

sum_tree = FenwickTree(max_possible)

count_tree = FenwickTree(max_possible)

for x in range(1, n+1):

    sum_tree.add(0, 0)  # each x's s[x] is 0.

    count_tree.add(0, 1)

But wait, no. Adding 0 to sum_tree and 1 to count_tree for each x.

Yes, because each x contributes 0 to sum and 1 to count.

But Fenwick trees are 1-based or 0-based?

We need to decide. Let's assume that the Fenwick trees are 1-based, and indices are from 1 to max_possible.

But s[x] can be zero. So, to handle s[x] =0, we need to shift the indices by 1. For example, store s[x] +1 in the Fenwick tree, so that 0 becomes 1, and max_possible becomes 3e5+1.

Alternatively, allow s[x] to be stored as is, with 0 as a valid index.

But Fenwick trees can be implemented with 0-based or 1-based indices. Let's choose 1-based.

So, for a value v, the index in the Fenwick tree is v +1. So, for s[x] =0, we use index 1; for 1, index 2, etc. This way, we can handle s[x] up to 3e5, with indices up to 3e5+1.

But this depends on the Fenwick tree implementation.

Alternatively, use a Fenwick tree that supports 0-based indices.

But for now, let's assume that the Fenwick tree can handle 0 as a valid index.

Implementing a Fenwick tree that can handle queries and updates at 0.

But in Python, lists are 0-based, but Fenwick trees are usually implemented with 1-based indices. So perhaps we can shift the indices by 1.

But this is getting a bit complicated. Alternatively, set the Fenwick tree's size to max_possible +2, where max_possible is the maximum possible s[x], which is 3e5.

But perhaps in practice, the maximum possible s[x] is up to the current_notification_count, which can be up to 3e5.

So, the Fenwick trees can be initialized with a maximum index of 3e5 +1.

Implementing the Fenwick tree:

class FenwickTree:

    def __init__(self, size):

        self.n = size

        self.tree = [0] * (self.n +1)

    def add(self, idx, delta):

        # 1-based index

        idx +=1  # shift from 0-based to 1-based

        while idx <= self.n +1:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        # sum [0..idx] (original indices)

        res =0

        idx +=1  # convert to 1-based

        while idx >0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

    def query_range(self, l, r):

        # sum [l..r]

        return self.query(r) - self.query(l-1)

Wait, but in this code, the 'size' is the maximum possible index (0-based). For example, if the maximum index is 3e5, then the Fenwick tree is initialized with size=3e5, and indices can be from 0 to 3e5.

The 'add' method takes the 0-based index, adds 1 to make it 1-based, and updates the Fenwick tree.

The 'query' method returns the sum from 0 to idx (original 0-based).

So, for example, to get the sum of all elements >= k, we can compute:

sum_ge_k = sum_tree.query_range(k, max_index)

which is sum_tree.query(max_index) - sum_tree.query(k-1)

But how?

Wait, the query_range(l, r) function computes the sum of elements from l to r (inclusive) in the 0-based index.

So, sum_ge_k is sum from k to max_index.

Thus, sum_ge_k = sum_tree.query(max_index) - sum_tree.query(k-1)

Similarly for count_ge_k.

So, the code for sum_ge_k and count_ge_k is:

sum_ge_k = sum_tree.query(max_possible) - sum_tree.query(k-1)

count_ge_k = count_tree.query(max_possible) - count_tree.query(k-1)

B = sum_ge_k - max_t3 * count_ge_k

unread = current_notification_count - (max_t3 + B)

Now, implementing this.

So, the code steps are:

Initialize Fenwick trees with max_possible=3e5 (since current_notification_count can be up to q=3e5).

For each app x in 1..n:

   s[x] = 0.

   sum_tree.add(0, 0)

   count_tree.add(0, 1)

Processing each event:

For each event line:

   read the type and the parameter.

   if type is 1:

      x = parameter.

      current_notification_count +=1

      count[x] +=1

      new_s = min(count[x], last_read[x])

      if new_s != s[x]:

          sum_tree.add(s[x], -s[x])

          count_tree.add(s[x], -1)

          sum_tree.add(new_s, new_s)

          count_tree.add(new_s, 1)

          s[x] = new_s

   elif type is 2:

      x = parameter.

      last_read[x] = current_notification_count

      new_s = min(count[x], last_read[x])

      if new_s != s[x]:

          sum_tree.add(s[x], -s[x])

          count_tree.add(s[x], -1)

          sum_tree.add(new_s, new_s)

          count_tree.add(new_s, 1)

          s[x] = new_s

   elif type is 3:

      t = parameter.

      if t > max_t3:

          max_t3 = t

   # After processing the event, compute B and unread.

   k = max_t3

   max_possible = 3e5  # or current_notification_count, but current_notification_count can be up to 3e5.

   sum_ge_k = sum_tree.query(max_possible) - sum_tree.query(k-1)

   count_ge_k = count_tree.query(max_possible) - count_tree.query(k-1)

   B = sum_ge_k - k * count_ge_k

   unread = current_notification_count - (k + B)

   print(unread)

But wait, the max_possible for the Fenwick trees is set to 3e5. But current_notification_count can be up to 3e5, and new_s can be up to current_notification_count.

So, in the Fenwick tree, the maximum index is 3e5.

But for events where current_notification_count exceeds 3e5 (but q is up to 3e5, so current_notification_count can be up to 3e5).

Thus, the Fenwick trees are initialized with size 3e5.

But what if during processing, new_s exceeds 3e5? For example, type 3 events with t=3e5 and type 2 events could make s[x] up to 3e5.

But according to the problem statement, each type 3 event's t is guaranteed to be <= current_notification_count at the time of the event. So max_t3 can be up to 3e5.

Thus, the Fenwick tree size is sufficient.

Now, the code:

But in Python, for 3e5 elements, the Fenwick tree will need O(3e5) space, which is manageable.

Now, the code:

But let's implement the Fenwick tree properly.

class FenwickTree:

    def __init__(self, max_size):

        self.max_size = max_size

        self.tree = [0]*(self.max_size +2)  # 1-based indexing

    def update(self, idx, delta):

        # idx is 0-based, can be up to max_size.

        idx +=1  # convert to 1-based

        while idx <= self.max_size +1:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        # returns sum from 0 to idx (0-based)

        res =0

        idx +=1  # convert to 1-based

        while idx >0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

    def range_query(self, l, r):

        # returns sum from l to r (inclusive, 0-based)

        if l > r:

            return 0

        return self.query(r) - self.query(l-1)

But for sum_ge_k, we need sum_tree.range_query(k, max_size).

Similarly for count_ge_k.

Now, the code:

Read n and q.

max_possible = 3e5+1

sum_tree = FenwickTree(max_possible)

count_tree = FenwickTree(max_possible)

But wait, the max_size is 3e5+1? Or what?

Wait, the maximum s[x] can be up to current_notification_count, which is up to 3e5. So s[x] can be up to 3e5.

So, the max_size should be 3e5.

So:

MAX_SIZE = 300000

sum_tree = FenwickTree(MAX_SIZE)

count_tree = FenwickTree(MAX_SIZE)

Then, for all s[x], which are up to current_notification_count (up to 3e5), we can store them in the Fenwick tree.

Thus, during initialization, for each app x, we add s[x] =0.

So:

for x in range(1, n+1):

    sum_tree.update(0, 0)  # adding 0 to the sum tree.

    count_tree.update(0, 1)

But this is not correct. Because sum_tree should track the sum of s[x] values, and count_tree tracks the count of each s[x]. For example, each app x starts with s[x] =0. So sum_tree should have 0 added n times, which sum to 0. But adding 0 to sum_tree via update(0, 0) will add 0 each time. So for n apps, sum_tree will have 0 added n times, resulting in sum 0.

Yes.

So, the code for initialization is correct.

Now, processing events.

But what about when s[x] becomes larger than MAX_SIZE? For example, if current_notification_count exceeds 3e5 (but q is up to 3e5, so current_notification_count can be up to 3e5).

Thus, s[x] can be up to current_notification_count, which is up to 3e5. So the Fenwick tree can handle it.

Thus, the code should work.

Now, let's write the code.

But in Python, we need to read input efficiently. Since n and q can be up to 3e5, using input() and split() can be slow. So we need to read all input at once.

But for the problem constraints, even using input() should work, but to be safe, we can read from sys.stdin.

Testing against sample input 1.

```python
import sys


class FenwickTree:

    def __init__(self, max_size):

        self.max_size = max_size

        self.tree = [0] * (self.max_size + 2)  # 1-based

    def update(self, idx, delta):

        idx += 1  # convert to 1-based

        while idx <= self.max_size + 1:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        res = 0

        idx += 1  # convert to 1-based

        while idx > 0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

    def range_query(self, l, r):

        if l > r:

            return 0

        return self.query(r) - self.query(l-1)

def main(input_stream, output_stream):
    import sys

    input = input_stream.read().split()

    ptr = 0

    n = int(input[ptr])

    ptr +=1

    q = int(input[ptr])

    ptr +=1

    MAX_SIZE = 300000

    sum_tree = FenwickTree(MAX_SIZE)

    count_tree = FenwickTree(MAX_SIZE)

    # Initialize s[x] =0 for all x.

    for x in range(n):

        sum_tree.update(0, 0)

        count_tree.update(0, 1)

    current_notification_count =0

    max_t3 =0

    count = [0]*(n+2)  # 1-based

    last_read = [0]*(n+2)

    s = [0]*(n+2)

    for _ in range(q):

        type_ = int(input[ptr])

        ptr +=1

        if type_ ==1 or type_ ==2:

            x = int(input[ptr])

            ptr +=1

            if type_ ==1:

                current_notification_count +=1

                count[x] +=1

                new_s = min(count[x], last_read[x])

                if new_s != s[x]:

                    sum_tree.update(s[x], -s[x])

                    count_tree.update(s[x], -1)

                    sum_tree.update(new_s, new_s)

                    count_tree.update(new_s, 1)

                    s[x] = new_s

            else:  # type 2

                last_read[x] = current_notification_count

                new_s = min(count[x], last_read[x])

                if new_s != s[x]:

                    sum_tree.update(s[x], -s[x])

                    count_tree.update(s[x], -1)

                    sum_tree.update(new_s, new_s)

                    count_tree.update(new_s, 1)

                    s[x] = new_s

        else:  # type 3

            t = int(input[ptr])

            ptr +=1

            if t > max_t3:

                max_t3 = t

        # Compute B = sum_ge_k - k * count_ge_k, where k =max_t3

        k = max_t3

        sum_ge_k = sum_tree.range_query(k, MAX_SIZE)

        count_ge_k = count_tree.range_query(k, MAX_SIZE)

        B = sum_ge_k - k * count_ge_k

        unread = current_notification_count - (max_t3 + B)

        print(unread, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 6
1 2
1 4
1 2
3 3
1 3
1 3
""",
            "output": \
"""\
1
2
3
0
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

</think>

```python
import sys

class FenwickTree:
    def __init__(self, max_size):
        self.max_size = max_size
        self.tree = [0] * (self.max_size + 2)  # 1-based indexing

    def update(self, idx, delta):
        idx += 1  # Convert to 1-based index
        while idx <= self.max_size + 1:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        res = 0
        idx += 1  # Convert to 1-based index
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def range_query(self, l, r):
        if l > r:
            return 0
        return self.query(r) - self.query(l - 1)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    q = int(input[ptr])
    ptr += 1

    MAX_SIZE = 300000
    sum_tree = FenwickTree(MAX_SIZE)
    count_tree = FenwickTree(MAX_SIZE)

    # Initialize all apps with s[x] = 0
    for _ in range(n):
        sum_tree.update(0, 0)
        count_tree.update(0, 1)

    current_notification_count = 0
    max_t3 = 0
    count = [0] * (n + 2)  # 1-based indexing
    last_read = [0] * (n + 2)
    s = [0] * (n + 2)

    for _ in range(q):
        event_type = int(input[ptr])
        ptr += 1
        if event_type in (1, 2):
            x = int(input[ptr])
            ptr += 1
            if event_type == 1:
                current_notification_count += 1
                count[x] += 1
                new_s = min(count[x], last_read[x])
            else:
                last_read[x] = current_notification_count
                new_s = min(count[x], last_read[x])

            if new_s != s[x]:
                sum_tree.update(s[x], -s[x])
                count_tree.update(s[x], -1)
                sum_tree.update(new_s, new_s)
                count_tree.update(new_s, 1)
                s[x] = new_s
        else:
            t = int(input[ptr])
            ptr += 1
            if t > max_t3:
                max_t3 = t

        k = max_t3
        sum_ge_k = sum_tree.range_query(k, MAX_SIZE)
        count_ge_k = count_tree.range_query(k, MAX_SIZE)
        B = sum_ge_k - k * count_ge_k
        unread = current_notification_count - (k + B)
        print(unread)

if __name__ == "__main__":
    main()
```
