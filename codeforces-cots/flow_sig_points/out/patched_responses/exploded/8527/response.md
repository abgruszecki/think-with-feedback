<think>
Okay, let's see. The problem is about finding the number of interesting submissions based on certain timing conditions. Hmm. So, we need to model the testing process and track when a submission's test q aligns with the displayed percentage d, which is calculated as the rounded percentage of completed submissions at that moment.

First, let's understand the process. There are k testing processes. Each process picks the next submission in order when it's free. Each submission i has a_i tests, taking a_i seconds to complete. The testing for a submission starts as soon as a process is free. For example, if a process is free at time t, it starts testing submission i, and that submission will take from t to t+a_i seconds. During this time, the submission is being tested on test q (from 1 to a_i) at time t + q - 1 to t + q. So for each test q of submission i, the time interval is [t + q - 1, t + q).

The caption d is computed as the rounded (floor(x + 0.5)) of (m / n * 100), where m is the number of completed submissions by that moment. So, whenever during the testing of a submission's test q, the current d (as computed at that moment) equals q, then that submission is interesting.

Our goal is to count all such submissions.

So, the steps are:

1. Simulate the testing process to find for each submission i, the start time s_i when its testing begins.
   Then, for submission i, it will be processed from s_i to s_i + a_i. For each of its a_i tests, each test q (1-based?) runs from s_i + q-1 to s_i + q. During this interval, we need to check if there's any time t in that interval where the displayed percentage d (based on the number of completed submissions up to t) equals q.

2. For each submission i, check each of its a_i tests to see if during the time interval [s_i + q-1, s_i + q), the displayed d (computed as round(100 * m / n)) equals q. If yes, then the submission is interesting. We need to count all submissions that have at least one such test.

But how do we compute m, the number of completed submissions by time t?

Wait, m is the number of submissions that have been fully tested by time t. So for any time t, m is the count of submissions j where s_j + a_j <= t.

So for each submission i, during its test q (time interval [s_i + q-1, s_i + q)), we need to check if there exists a time t in this interval where round(100 * (m_t)/n) = q, where m_t is the number of submissions completed by time t.

But m_t can change during the interval. Because other submissions may finish during that interval.

This seems complicated. So, for each test q of submission i, we need to check if during [s_i + q-1, s_i + q), there's any moment where d equals q.

Hmm. Let's think about how to model this.

First, we need to determine for each submission i, its start time s_i. Then, for each test q in 1..a_i, the time interval for that test is [s_i + q-1, s_i + q). During this interval, m_t is the number of submissions that have finished by time t. So for each time t in this interval, m_t is the count of submissions j where s_j + a_j <= t.

But how do we track m_t? Because m_t increases as t increases, but not continuously. For example, when a submission j finishes at s_j + a_j, m increases by 1 at that time.

So, during the interval [s_i + q-1, s_i + q), m_t is the number of submissions that have finished by t. So m_t can change only at specific points in the interval, such as when some submission finishes.

But for each test q's interval, we need to check if there exists a t in that interval where 100*(m_t)/n rounds to q. Let's call that d(t) = q.

But how to compute this efficiently?

Alternative approach: For each submission i, during each of its tests q, check if there exists a t in [start, end) of the test such that d(t) = q. If yes, then i is interesting.

So, the problem breaks down into two parts:

1. Simulate the testing processes to find the start times s_i for each submission i.

2. For each submission i and each test q (from 1 to a_i), check if during the time interval [s_i + q-1, s_i + q) there exists a t where d(t) equals q.

Now, the first part requires simulating the processing of the submissions with k processes. Since the order is from 1 to n, each process takes the next submission in the queue as soon as it's free.

How to model this? We can use a priority queue (min-heap) where each element represents the time a process becomes free. Initially, all processes are free at time 0. For each submission in order, we pick the earliest available process (smallest available time), assign the submission to start at that time, then update the process's available time to start + a_i. Then, the next submission will take the next earliest available process, and so on.

Yes. That's the way to model the start times.

So for example, with k=2 processes:

The earliest available times are 0 and 0. Take the first submission (i=0?), assign it to process 0. Its start time is 0, and the process becomes available at 0 + a_0. Then the next submission is assigned to the next earliest available process (which is the other process, available at 0), start time 0. Then, for the third submission, the earliest available time is min of the two processes' available times. So the start time is the earliest available time.

So, the code for computing s_i is:

- Initialize a min-heap with k zeros (available times for each process).
- For each submission i in 0..n-1:
   - Pop the smallest available time from the heap. That's s_i.
   - Push s_i + a_i back into the heap.
- So, s_i is the start time of submission i.

Yes. This is correct.

Once we have all s_i's, the next step is to check for each submission i and each test q (1 <= q <= a_i), whether there exists a time t in [s_i + q-1, s_i + q) where d(t) = q.

So how do we compute m_t, the number of submissions completed by time t?

m_t is the count of submissions j where s_j + a_j <= t.

So, m_t is a non-decreasing function. Each time a submission j finishes (at time s_j + a_j), m_t increases by 1.

So, during the interval [s_i + q-1, s_i + q), m_t can be calculated as the number of submissions whose finish time is <= t.

But how can we compute m_t for any t in this interval?

Alternatively, we can precompute all the finish times of the submissions (s_j + a_j for each j), sort them, and then for a given t, the number of submissions completed by t is the number of finish times <= t.

But even better: let's precompute all finish times, sort them, and then for any interval [a, b), we can compute the number of submissions completed before a, and how many are added during [a, b).

Wait, but for the interval [s_i + q-1, s_i + q), which is of length 1. So during this interval, t ranges from s_i + q-1 (inclusive) to s_i + q (exclusive). So m_t can be m_start, the number of submissions completed before s_i + q-1, plus the number of submissions that finish during [s_i + q-1, t).

But how do we model this?

Alternatively, for a given interval [start, end), m_t can be m_start (number of submissions finished by start) plus the number of submissions that finish between start and t (for t in [start, end)).

So, during this interval, m(t) can be m_start + the number of finish times in [start, t].

But how do we check if there exists a t in [start, end) such that round(100*(m(t)/n)) = q?

Hmm. Let's denote q as the desired percentage. So we need to check if there's any t in [start, end) where 100*(m(t)/n) is in [q - 0.5, q + 0.5), since round(x) is the nearest integer. For example, x in [q-0.5, q+0.5) rounds to q.

So, the condition is:

(q - 0.5)/100 * n <= m(t) < (q + 0.5)/100 * n

But since m(t) must be an integer between 0 and n, we need to find if there's a t in the interval such that m(t) is in this range.

So, the problem reduces to: for the interval [start, end), is there any t where m(t) (the number of submissions completed by t) is in [L, R], where L = ceil( (q - 0.5)/100 * n ), R = floor( (q + 0.5)/100 *n ) -1 ? Wait, no. Let me re-calculate.

Wait, the condition for d(t) = q is that 100*(m(t)/n) rounds to q. The rounding is done as per the function round(x) = floor(x + 0.5). So, for x being 100*(m(t)/n), the rounded value is q if x is in [q - 0.5, q + 0.5). So m(t)/n must be in [ (q - 0.5)/100, (q + 0.5)/100 ), multiply by 100 gives the x.

So, m(t) must be in [ (q - 0.5)/100 * n, (q + 0.5)/100 * n )

But m(t) is an integer. So the lower bound is (q - 0.5)/100 * n <= m(t) < (q + 0.5)/100 *n.

So, for each interval [start, end), check if there's a t in that interval where m(t) is within this range.

But how?

Let me think. For the given interval [start, end), we can precompute all finish times of submissions. Let's collect all finish times in a sorted list. Then, for a given interval, the number of submissions completed by time start is m_start = the number of finish times <= start. Then, during the interval, any submission with finish time in (start, end) will contribute to m(t) as t increases.

So, during the interval, the m(t) starts at m_start, and increases by 1 each time a submission's finish time is within [start, t). So, the m(t) increases step-wise.

But in the interval [start, end), there may be several submission finish times. Each such finish time increases m(t) by 1 at that exact time.

So, the m(t) can be:

- m_start for t in [start, f_0), where f_0 is the first finish time in the interval.

- m_start +1 for t in [f_0, f_1), etc.

So, for each submission i's test q's interval [s_i + q-1, s_i + q), we need to check if any of these steps in m(t) leads to d(t) = q.

Alternatively, we can model the possible m(t) values during the interval and see if any of them falls into the desired range for q.

So, steps for each test q of submission i:

1. Compute the start and end times of the test: test_start = s_i + q -1, test_end = s_i + q.

2. Find all submissions j (including i) whose finish time f_j = s_j + a_j is in the interval [test_start, test_end). These are the submissions that finish during this test's interval. Each such f_j will cause m(t) to increase by 1 at time f_j.

3. The initial m at test_start is m_start = the number of submissions finished before test_start.

4. Then, during the interval [test_start, test_end), the m(t) will be m_start plus the number of submissions j with f_j <= t.

5. We need to check if there's any time t in [test_start, test_end) where m(t) is in the required range for q.

Let's model the possible m values during this interval. The m starts as m_start and increases by 1 each time a submission's finish time is reached.

So, during the interval, the possible values of m(t) are:

- m_start, until the first f_j in [test_start, test_end).

- m_start + 1, until the next f_j.

- etc., up to m_start + k, where k is the number of submissions finishing during this interval.

So, the possible m values are m_start, m_start +1, ..., m_start + k.

For each of these m values, we need to check if (100 * m /n) is in [q -0.5, q +0.5). Because during the time between f_j and f_{j+1}, m(t) is m_start + j, and for any t in that interval, the d(t) will be the same. So, if any of these m values (including the initial m_start) falls into the required range for q, then this submission i is interesting.

Additionally, we need to check if during the interval, the required m is within [lower, upper), where:

lower = (q - 0.5) * n / 100

upper = (q + 0.5) * n / 100

But m must be an integer. So, m must be >= lower and < upper.

But lower and upper can be real numbers. So, for each possible m in m_start to m_start + k (inclusive), check if m >= lower and m < upper.

Wait, but m has to be an integer, so the condition is:

Does there exist an integer m in [ceil(lower), floor(upper - 1e-9)] ?

Wait, no. The original condition is that (m/n)*100 is in [q-0.5, q+0.5). So, solving for m:

q - 0.5 <= (m /n ) * 100 < q + 0.5

Multiply all terms by n/100:

m >= (q -0.5) * n / 100

m < (q +0.5) * n / 100

But m must be an integer. So, the possible m values are integers in the interval [A, B), where:

A = ceiling( (q-0.5)*n / 100 )

B = floor( (q+0.5)*n /100 )

But wait, m must be >= (q-0.5)*n/100 and < (q+0.5)*n/100. So the integer m must satisfy A <= m < B.

But how to compute A and B?

For example, for (q-0.5)*n/100 could be a fractional value. The smallest integer m that is >= this value is the ceiling of that value. Similarly, the largest integer m that is < (q+0.5)*n/100 is the floor of that value minus 1? Wait, no.

Wait, for example, if (q+0.5)*n/100 is 5.2, then m must be <5.2. So the maximum possible m is 5. So B is 5. So, A is the ceiling of (q-0.5)*n/100. So m must be in [A, B] where B is floor( (q+0.5)*n/100 - 1e-9 ), to avoid floating point errors.

Alternatively, compute A as the smallest integer >= (q-0.5)*n/100.

Compute B as the largest integer < (q+0.5)*n/100.

So, B = floor( (q+0.5)*n/100 - 1e-9 )

But handling this correctly is tricky because of floating point precision. So perhaps, for a given q and n, compute the lower and upper bounds as:

lower = (q - 0.5) * n / 100

upper = (q + 0.5) * n / 100

Then, the required m is the integer m such that lower <= m < upper.

So, m can be in the integer interval [ceil(lower), floor(upper - 1e-9)].

But how to compute this?

Alternatively, for a given m, check if (m * 100) is within [ (q-0.5)*n, (q+0.5)*n ). Then, m is valid if (q-0.5)*n <= m*100 < (q+0.5)*n.

But perhaps, to avoid floating points, we can compute m must satisfy:

(q-0.5)*n <= m*100 < (q+0.5)*n

Multiply all terms by 2 to eliminate the decimal:

(2q -1)*n <= 200m < (2q +1)*n

But this may not help. Hmm.

Alternatively, m must satisfy:

m >= (q - 0.5) * n / 100

m < (q +0.5) *n /100

So, for each m in the possible range during the test's interval, we can compute whether it's in the required range.

But this requires checking for each possible m during the interval whether it's in that range.

So, during the test q's interval, the possible m values are m_start, m_start+1, ..., m_start + count (where count is the number of submissions finishing during this interval).

For each of these m values, check if m is in the required range. If any is, then submission i is interesting for this q.

Additionally, the m can also be in between the steps. For example, if during the interval, m increases from m_start to m_start +1, but the required m is a value between m_start and m_start+1. Wait, no, m can't be between integers because m is the count of submissions that have been completed. So m is an integer. So during the interval, m can only take integer values. Thus, the possible m values are the ones in the steps.

Wait, no. For example, during the interval, if a submission j finishes at time f_j = test_start + 0.5. Then, for t < f_j, m(t) is m_start. For t >=f_j, m(t) is m_start+1. So during the interval, m can be m_start, m_start+1, ..., m_start + k, where k is the number of submissions that finish in this interval.

So, the possible m values are the initial m_start, and then each time a submission finishes, m increments by 1.

So, for each test q's interval, the m(t) can take m_start, m_start+1, ..., m_start + k, where k is the number of submissions j with f_j in [test_start, test_end).

Therefore, during the interval, the possible m values are m_start, m_start +1, ..., m_start + k.

If any of these values is in the required range for q, then the submission i is interesting.

Additionally, we need to check if even the initial m_start is in the range. Because at the start of the interval (test_start), m(t) is m_start. So, during the time from test_start to the first finish time (if any), m remains m_start. If during that time, m_start is in the required range, then there's a t (like test_start) where d(t) is q. Similarly, between finish times.

So, the approach is:

For each submission i and each test q:

1. Compute test_start = s_i + q-1, test_end = s_i + q.

2. Compute m_start = number of submissions with f_j <= test_start.

3. Compute the number of submissions that finish during [test_start, test_end): these are the submissions with f_j >= test_start and f_j < test_end. Let this count be k. The possible m values during the interval are m_start, m_start+1, ..., m_start + k.

4. For each possible m in this list, check if m is in the required range for q.

5. If any of these m's is in the range, then submission i is interesting (for this q). But since we need to count each submission once (if any of its tests meet the condition), we can break early once a q for submission i is found to be valid.

So, the steps for each submission i:

For each q from 1 to a_i:

   compute test_start and test_end.

   compute m_start: how many f_j <= test_start.

   compute the list of f_j in [test_start, test_end). Sort them? Well, maybe precompute all f_j and sort them once.

   Then, the possible m values are m_start, m_start+1, ..., m_start + k, where k is the number of f_j in [test_start, test_end).

   For each m in this sequence, check if (q-0.5)*n/100 <= m < (q+0.5)*n/100.

   If any m in this sequence satisfies the condition, then submission i is interesting. So we can mark it and break out of the loop for this i.

So, how to compute m_start and the number of f_j in [test_start, test_end)?

This can be done efficiently by first sorting all f_j. Then, for a given test interval [A, B), m_start is the number of f_j <= A (which can be found via binary search). The number of f_j in [A, B) is the number of elements in the sorted list between the lower and upper bounds.

So, pre-sort the list of f_j. For example, after computing all s_i and f_i, collect all f_j into a sorted list.

Then, for each test's interval [A, B):

   m_start = bisect_right(f_list, A) - 1? Or wait, how?

Wait, f_list is sorted in ascending order. The number of elements <= A is the index of the first element > A. So, using bisect_right.

So, m_start = bisect.bisect_right(f_list, A) - 0? No, bisect_right returns the insertion point which gives the number of elements <= A. Wait, no: bisect_right returns the first index where the element is greater than A. So, the number of elements <= A is bisect_right(f_list, A).

Wait, for example, if the list is [1,3,5], and A=3. bisect_right returns 2 (since elements at indices 0 and 1 are <=3). So m_start would be 2.

Yes. So, m_start = bisect.bisect_right(f_list, A) where A is test_start.

Wait, no. Wait, m_start is the count of submissions finished by test_start. Because a submission is finished by time t if f_j <= t. So, for t = test_start, the count is the number of f_j <= test_start. Which is exactly bisect_right(f_list, test_start).

Similarly, the number of submissions finishing in [test_start, test_end) is bisect.bisect_left(f_list, test_end) - bisect.bisect_left(f_list, test_start).

Wait, no. Because [test_start, test_end) is the interval. So the count is the number of f_j >= test_start and < test_end. So using bisect_left and bisect_right.

Wait, the bisect module can be used as follows:

count = bisect.bisect_left(f_list, test_end) - bisect.bisect_left(f_list, test_start)

Because bisect_left finds the first position where the element is >= test_start. And bisect_left for test_end is the first position >= test_end. So, the difference is the number of elements >= test_start and < test_end.

Yes.

So, for the given interval [A, B):

number of submissions finishing in this interval is:

bisect.bisect_left(f_list, B) - bisect.bisect_left(f_list, A)

So, the possible m values are m_start, m_start+1, ..., m_start + k, where k is the count computed as above.

But wait, m_start is the number of submissions finished by A (test_start). So during the interval, the initial m is m_start, and each submission finishing during the interval adds 1 to m. So the possible m values are m_start, m_start +1, ..., m_start + k.

So, for each of these m values (from m_start to m_start +k), check if m is in the required range for q.

But how to compute the required range?

For a given q and n:

lower = (q -0.5) * n / 100

upper = (q +0.5) * n / 100

If any m in [m_start, m_start +k] is >= lower and < upper, then submission i is interesting.

But since m must be an integer, perhaps it's better to compute the integer bounds and check for overlapping ranges.

Alternatively, for each m in the possible values, check:

lower <= m < upper.

So, code-wise:

For each m in m_start to m_start + k:

   if (q -0.5)*n <= 100*m < (q +0.5)*n:

       return True

But note that 100*m must be in [ (q-0.5)*n, (q+0.5)*n )

Wait, no. Wait, the original condition is:

(q-0.5) <= (m /n ) * 100 < (q+0.5)

Multiply both sides by 1:

(q-0.5) * n <= 100 * m < (q+0.5) *n

So yes.

But since m can be up to m_start +k, which is up to m_start + (number of submissions finishing in the interval), which could be up to n.

But how do we handle this for all possible m in that range.

So, steps for each test q of submission i:

Compute test_start = s_i + q-1

test_end = s_i + q

m_start = bisect.bisect_right(f_list, test_start)

k = bisect.bisect_left(f_list, test_end) - bisect.bisect_left(f_list, test_start)

possible_m = range(m_start, m_start +k +1) ?

Wait, because if there are k submissions finishing in the interval, then during the interval, each of these submissions adds 1 to m. So, when all k have been added, m would be m_start +k. But what if k is zero? Then possible_m is [m_start], and during the interval, m remains m_start.

Wait, the number of submissions finishing in the interval is k. So during the interval, m_start starts as m_start, then increases by 1 for each submission that finishes. So, after all k submissions have finished, m is m_start +k.

So the possible m values are m_start, m_start+1, ..., m_start +k.

So the possible m's are from m_start to m_start +k, inclusive.

Wait, for example, if k=3, then possible m values are m_start, m_start+1, m_start+2, m_start+3.

So the count is k+1 possible m values.

Yes.

So, possible_m is from m_start to m_start +k.

So, the code for checking is:

if any m in [m_start, m_start +k] satisfies (q-0.5)*n <= 100*m < (q+0.5)*n:

   then submission i is interesting.

But how do we compute this efficiently?

We can compute the lower and upper bounds:

lower = (q - 0.5) * n

upper = (q + 0.5) * n

then, for each m in possible_m:

check if 100*m >= lower and 100*m < upper.

If yes, then return True.

But since m can be up to m_start +k, which could be up to m_start + (n - m_start), which is n, but m can't exceed n.

But since m is the number of submissions completed by t (which is <=n), that's okay.

So, code-wise:

for each i in 0..n-1:

   interesting = False

   for q in 1..a_i:

       test_start = s_i + q -1

       test_end = s_i + q

       m_start = bisect.bisect_right(f_list, test_start)

       a = bisect.bisect_left(f_list, test_start)

       b = bisect.bisect_left(f_list, test_end)

       k = b - a

       # possible m is m_start, m_start +1, ..., m_start +k

       # check if any of these m in [lower, upper)

       lower = (q -0.5)*n

       upper = (q +0.5)*n

       # for each m in m_start ... m_start +k:

       # check if 100*m >= lower and 100*m < upper

       min_m = m_start

       max_m = m_start +k

       # find if there's any m in [min_m, max_m] where 100*m is in [lower, upper)

       # which is equivalent to m >= lower /100 and m < upper /100.

       # but since m is integer, we can compute:

       min_required = math.ceil( lower / 100 )

       max_required = math.floor( (upper - 1e-9)/ 100 )

       # if the ranges [min_m, max_m] and [min_required, max_required] intersect, then yes.

       # check overlap between [min_m, max_m] and [min_required, max_required]

       # if (min_required <= max_m) and (min_m <= max_required):

       #   there's overlap.

       #   So, possible.

       # Also, check if any m in the possible range is between lower/100 and upper/100.

       # Compute the lower and upper in terms of m:

       # m >= (lower) /100 --> m >= (q-0.5)*n /100

       # m < upper /100 --> m < (q+0.5)*n /100

       # So, m must be an integer >= (q-0.5)*n /100 and < (q+0.5)*n /100.

       # So, possible if:

       # the minimal possible m in [min_m, max_m] is <= max possible m in the required range.

       # Let's compute:

       required_min_m = math.ceil( (q -0.5)*n /100 )

       required_max_m = math.floor( (q +0.5)*n /100 - 1e-9 )

       # check if [min_m, max_m] overlaps with [required_min_m, required_max_m]

       if max_m < required_min_m:

           continue

       if min_m > required_max_m:

           continue

       # there is overlap.

       interesting = True

       break

   if interesting:

       result +=1

This would be an efficient way to check, avoiding iterating through all possible m in the range.

So, for each possible m in the possible range, check if the required range overlaps. If yes, then the submission is interesting for this q.

So, the steps are:

- Precompute s_i for each submission using the priority queue.

- Collect all f_i = s_i +a_i, sort them.

- For each submission i and each q in 1..a_i:

   compute test_start and test_end.

   compute m_start as the number of submissions finished by test_start.

   compute k as the number of submissions finishing in [test_start, test_end).

   compute possible m range: min_m = m_start, max_m = m_start +k.

   compute required_min_m and required_max_m.

   if the ranges [min_m, max_m] and [required_min_m, required_max_m] overlap, then submission i is interesting.

   if any q meets this, count the submission.

This approach avoids having to check each possible m in the possible range. Instead, it checks if there's any overlap between the possible m's and the required m's.

This is efficient, especially since n can be up to 1000, and a_i up to 150, leading to 1000 * 150 = 150,000 iterations, each with O(1) operations using the sorted list and bisect.

Now, let's test this approach against the examples.

First example:

Input:

2 2

49 100

The s_i's for submission 0 is 0, submission 1 is 0.

f_list is [49, 100].

sorted f_list is [49, 100].

n=2.

For submission 1 (i=1), a_i=100. Let's check q=50.

test_start = 0 +50-1 =49, test_end=0+50=50.

m_start is bisect_right(f_list, 49) =1 (since 49 is in the list and is the first element. bisect_right returns the index after the last occurrence of 49. So f_list is [49,100], bisect_right(49) is 1. So m_start=1.

k = bisect_left(f_list,50) - bisect_left(f_list,49) ?

Wait, test_start is 49, test_end is 50.

bisect_left(f_list,49) is 0. bisect_left(f_list,50) is 1. So k=1-0=1.

So possible m is m_start (1) to m_start +k = 1+1=2.

required_min_m = ceil( (50-0.5)*2 /100 ) = ceil(49.5*2/100) = ceil(99/100) = 1.

required_max_m = floor( (50+0.5)*2 /100 -1e-9 ) = floor(50.5*2/100 -1e-9) = floor(101/100 -1e-9) = 1.

So the required m is 1.

possible m is 1,2.

So there's overlap: 1 is in the possible range. So yes, submission 1 is interesting.

Thus, the answer is 1, which matches the first example.

Another example: second input.

But maybe this approach works.

Now, code steps:

Implement the code.

First, read n and k, and a list.

Then, compute the s_i's using a min-heap.

Then, compute f_list = [s_i + a_i for each i], then sort it.

Then, for each submission i in 0..n-1:

   for each q in 1..a_i:

       test_start = s_i + q-1

       test_end = s_i + q

       m_start = bisect.bisect_right(f_list, test_start)

       a_pos = bisect.bisect_left(f_list, test_start)

       b_pos = bisect.bisect_left(f_list, test_end)

       k = b_pos - a_pos

       possible_min_m = m_start

       possible_max_m = m_start +k

       # compute required_min_m and required_max_m

       lower = (q -0.5)*n

       upper = (q +0.5)*n

       required_min_m = math.ceil(lower / 100)

       required_max_m = math.floor( (upper - 1e-9) / 100 )

       # check overlap

       if possible_max_m < required_min_m:

           continue

       if possible_min_m > required_max_m:

           continue

       # there is overlap

       interesting = True

       break

   if interesting:

       result +=1

So, code:

But wait, required_min_m and required_max_m are computed as:

required_min_m = ceil( (q -0.5)*n /100 )

required_max_m = floor( ( (q +0.5)*n -1e-9 ) /100 )

Because upper is (q+0.5)*n, so the upper limit is m < upper /100. So the maximum m is floor( (upper -1e-9)/100 )

Yes.

Now, code:

Testing against sample input 1.

```python
import heapq
import bisect
import math


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    # Compute start times s_i
    heap = []
    for _ in range(k):
        heapq.heappush(heap, 0)

    s = []
    for ai in a:
        t = heapq.heappop(heap)
        s.append(t)
        heapq.heappush(heap, t + ai)

    f = [s[i] + a[i] for i in range(n)]
    f.sort()

    result = 0

    for i in range(n):
        ai = a[i]
        s_i = s[i]
        found = False
        for q in range(1, ai +1):
            test_start = s_i + q -1
            test_end = s_i + q

            m_start = bisect.bisect_right(f, test_start)

            a_pos = bisect.bisect_left(f, test_start)
            b_pos = bisect.bisect_left(f, test_end)
            k_count = b_pos - a_pos

            possible_max_m = m_start + k_count
            possible_min_m = m_start

            # compute required m range
            lower = (q -0.5) * n
            upper = (q +0.5) * n

            required_min_m = math.ceil( lower / 100 )
            required_max_m = math.floor( (upper - 1e-9) / 100 )

            # check overlap
            if possible_min_m > required_max_m:
                continue
            if possible_max_m < required_min_m:
                continue

            found = True
            break
        if found:
            result +=1

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 2
32 100 33 1
""",
            "output": \
"""\
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

Another example: the second sample input:

4 2

32 100 33 1

s will be computed as:

Process:

Heap starts with [0,0].

Submission 0 (a=32): popped 0, s[0] =0. Push 0+32=32. Heap is [0,32].

Submission 1 (a=100): popped 0, s[1]=0. Push 0+100=100. Heap now [32,100].

Submission 2 (a=33): popped 32. s[2]=32. Push 32+33=65. Heap now [65,100].

Submission 3 (a=1): popped 65. s[3]=65. Push 65+1=66. Heap now [66,100].

So f is [0+32=32, 0+100=100, 32+33=65, 65+1=66]. Sorted f is [32,65,66,100].

Now, for submission 2 (i=2, a_i=33), let's see for q=25.

test_start =32 +24=56, test_end=57.

m_start is bisect_right(f,56) =2 (since 32 and 65 are in f. 56 is between 32 and 65. bisect_right(f,56) returns 2 (as 65 is the first element >56).

k_count is the number of f_j in [56,57). Which would be none. So possible_max_m=2+0=2.

required_min_m and required_max_m for q=25:

(q-0.5)*n =24.5 *4 =98. 98 /100 =0.98. required_min_m =ceil(0.98)=1.

(q+0.5)*n =25.5*4=102. 102/100=1.02. required_max_m is floor(1.02 -1e-9)=1.

So required m is 1.

possible m is 2. 2 is not in [1,1]. So no.

Wait, but according to the note in the second example, submission 3 (i=3) is not part of the interesting ones. Let's see.

In the note, submission 3's test 25 is at time 32 +24.5=56.5, where the caption is 25% (m=1 submission out of 4, which is 25%). So why does the code capture this?

Wait, submission 3 is the third submission (i=2) with a_i=33. So q=25.

test_start =32 +24=56, test_end=57.

m_start is the number of submissions finished by 56. Looking at f sorted as [32,65,66,100], the submissions finished by 56 are the ones with f_j <=56. Those are 32 and 65? No. 65 is 65, which is >56. So the submissions finished by 56 are 32. So m_start is 1.

Wait, but bisect_right(f,56) on [32,65,66,100] would return 1, because 32 is <=56, and 65>56. So m_start=1.

k_count: submissions with f_j in [56,57) are those with 56 <= f_j <57. Looking at the f_list, the next is 65, which is >57. So k_count is 0.

So possible_m is 1 to 1+0=1.

required_min_m for q=25 is 1, required_max_m is 1.

So possible_m is 1. So 1 is in the required range. So submission 2 is marked as interesting.

Yes, this matches the note.

So, code should count submission 2's test 25 as valid.

Thus, the code works.

Therefore, the code should handle the examples correctly.

Now, for the code, we need to use the bisect module correctly, and compute all the required variables.

Edge cases to consider:

- q=0%: but q is at least 1 since a_i >=1.

- q=100%: but 100% would require m= n. But m can't exceed n.

- Cases where the required m is exactly n.

But since m is the number of submissions completed, which can't exceed n. So when q=100%, required m is in [99.5, 100.5) *n/100.

But 100.5%n/100 = (100.5 /100)*n = 1.005n, which for n=1000 would be 1005. But since m can't exceed n, the maximum possible required m is n.

So for q=100, required m is in [ (99.5/100)*n, (100.5/100)*n ). For n=100, this is 99.5 <= m < 100.5. So m can be 100.

But m can't be 100 unless n=100. So in this case, if n=100, q=100, and m=100, then yes.

But in code, when n=100 and q=100, the required_min_m is ceil( (100-0.5)*100 /100 )= ceil(99.5) =100. required_max_m is floor( (100.5)*100 /100 -1e-9 )= floor(100.5 -1e-9)=100. So m=100 is required. But m can't exceed n=100, so if all submissions have finished, then m=100, which is allowed.

So code would capture this.

Another case: when the required m is zero. But q can't be zero. So no.

So the code should handle all cases.

Now, considering time and memory constraints.

n is up to 1000, a_i up to 150. So for each submission, up to 150 tests.

Total number of tests is 1000 *150=150,000.

Each test requires some bisect operations, which are O(log n), which for n=1000 is acceptable.

The heap operations for computing s_i are O(n log k), which is acceptable.

The sorting of f_list is O(n log n), which is acceptable.

Thus, the code should be efficient enough.

Regarding memory: storing the s and f lists of size 1000 each is acceptable.

Thus, the code should work within the constraints.
</think>

```python
import heapq
import bisect
import math

n, k = map(int, input().split())
a = list(map(int, input().split()))

# Compute start times using a min-heap
heap = []
for _ in range(k):
    heapq.heappush(heap, 0)

s = []
for ai in a:
    t = heapq.heappop(heap)
    s.append(t)
    heapq.heappush(heap, t + ai)

# Calculate finish times and sort them
f = [s[i] + a[i] for i in range(n)]
f.sort()

result = 0

for i in range(n):
    ai = a[i]
    s_i = s[i]
    found = False
    for q in range(1, ai + 1):
        test_start = s_i + q - 1
        test_end = s_i + q

        m_start = bisect.bisect_right(f, test_start)
        a_pos = bisect.bisect_left(f, test_start)
        b_pos = bisect.bisect_left(f, test_end)
        k_count = b_pos - a_pos

        possible_min_m = m_start
        possible_max_m = m_start + k_count

        lower = (q - 0.5) * n
        upper = (q + 0.5) * n

        required_min_m = math.ceil(lower / 100)
        required_max_m = math.floor((upper - 1e-9) / 100)

        if possible_max_m < required_min_m or possible_min_m > required_max_m:
            continue

        found = True
        break
    if found:
        result += 1

print(result)
```
