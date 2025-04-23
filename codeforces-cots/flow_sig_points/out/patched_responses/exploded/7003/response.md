<think>
Okay, I need to solve this problem where Pasha has to solve all his programming contest problems and submit them during the available time periods. The goal is to find the earliest possible time he can finish all submissions, or return -1 if it's impossible.

Let me first understand the problem. So, Pasha can't work on two problems at the same time. He solves them one by one, each taking a_i time. The submission can only happen during the given time periods. The website is available in non-overlapping, chronologically ordered intervals. So, he has to schedule solving the problems and then submit them during any of these intervals. But he can submit any number of solutions at the same time, as long as it's within one of the intervals.

The key is to arrange the order of solving the problems and the intervals to submit them in such a way that the total time is minimized.

Hmm, so how to approach this? Let's think.

First, the total time Pasha spends solving all problems is the sum of all a_i. But since he can't submit during the intervals, the submission times have to fit into the available periods. Also, the time when he finishes solving a problem determines when he can submit it. But he can submit all solved problems at the same time as long as that time is within a period.

Wait, but the submission is done at the end of solving. For example, suppose he solves problem A first, which takes 3 units. Then he starts solving problem B, which takes 4 units. He can only submit A after he finishes solving B if the submission time is after the 3+4=7 units. Wait, no. Wait, no. Wait, he can submit A any time after he finishes solving it, but he can't do anything else while solving a problem. So during the solving of problem B, he can't submit A again. But once he finishes solving B, he can submit both A and B (if the current time is within a website period). Or wait, no. Because once he starts solving B, he's busy until he finishes. So the submission of A can only happen either during the solving time (but during that time he's solving A, so he can't submit then), or after he finishes A. Wait, no. Let me think again.

When solving a problem, he's occupied. So, for example:

If he solves problem A from time 0 to 3, then during that time, he can't submit anything. Once he's done with A at time 3, he can immediately submit it if there's an available period. Then he can start solving B. But if he chooses to submit later, he can. But the submission must be during a period. So after solving A, he can submit A at any time during any of the periods. But he can't start solving the next problem until after he submits. Wait, no. Wait, the problem statement says that the time he spends sending solutions is negligible, and he can send any number at the same moment. So after solving a problem, he can send all pending submissions at the earliest possible time. So maybe the optimal way is to batch submissions into the earliest possible intervals.

Wait, but how does the submission timing work? Let me think with the first example.

In the first example:

Problems take 3 and 4. The intervals are [1,4] and [7,9].

If he solves the second problem (4 units) first, then at time 4, he can submit it. But the first interval ends at 4. So 4 is included. So he can submit at time 4. Then he starts solving the first problem, which takes 3 units, ending at 7. Now, the next interval starts at 7, so he can submit at 7. So total time is 7. Which is the sample output.

So the order here matters. Solving the longer problem first allows both submissions to fit into their intervals.

So the approach must consider the order of solving the problems. Because the order affects when each problem's submission can be scheduled.

But with n up to 1000, trying all permutations is impossible. So we need a dynamic programming approach.

Alternatively, perhaps the optimal approach is to arrange the problem solving order such that the submission times can fit into the intervals optimally.

But how?

Another idea: The earliest possible time that all submissions can be made is determined by the latest submission time among all problems. So for each problem, its submission time must be <= the final answer. And all these submission times must be within some interval. The total solving time plus the submission scheduling must fit into the intervals.

Wait, but the submission of each problem can be done at different times. For example, problem A is submitted during interval X, problem B during interval Y, etc. As long as all are submitted by the answer time, which is the maximum of their submission times.

So the problem reduces to finding a schedule where for each problem, its submission time is within some interval, the sum of solving times (in some order) plus any waiting time between intervals must be such that each submission can be placed in some interval.

But this seems complex. Let me think of the steps needed.

Suppose we fix the order in which the problems are solved. Then, for each problem in that order, we can track the earliest possible time when the submission can happen, considering the available intervals.

But with n up to 1000, trying all possible orders is impossible. So we need a way to model the problem such that the order can be optimized without considering all permutations.

Wait, perhaps the optimal order is to sort the problems in a particular way, such that the submission times can be arranged optimally. For example, solving longer problems first.

Alternatively, perhaps the problem can be viewed as finding the minimal time T where T is the maximum of the submission times of each problem, such that the sum of the a_i's (in any order) plus the necessary waiting times (due to intervals) allows the submission times to fit into the intervals.

But how to model this?

Alternatively, maybe the key is to model the intervals as available time slots where submissions can be made, and the solving of the problems must be arranged in such a way that the cumulative solving time allows the submission of all problems in the intervals.

Hmm, but when you solve a problem, you can choose to submit it in any of the intervals that are after the time when you finish solving it. But since solving problems takes time, the order in which you solve them affects when each problem's submission is possible.

Wait, here's a better way to model the problem:

Each problem i, when solved at time S_i (the time when it's completed), must be submitted at a time T_i >= S_i, and T_i must lie within one of the intervals.

The total time required is the maximum of all T_i. We need to arrange the solving order and choose the T_i such that this maximum is minimized.

But how to model S_i. Because the solving order affects the S_i. For example, the first problem solved has S_1 = a_1. The second has S_2 = a_1 + a_2, and so on. Wait, no. The solving order is a permutation of the problems. So for a permutation p_1, p_2, ..., p_n, the S_i for problem p_j is sum_{k=1 to j} a_{p_k}.

But then, each S_pj is the time when the problem p_j is finished. Then, for each p_j, we need to find a T_j >= S_pj that is within some interval, and the maximum T_j is the answer for that permutation.

Our goal is to find the permutation and the T_j's such that the maximum T_j is minimized.

But with n up to 1000, generating all permutations is impossible. So we need a smarter approach.

This seems like a problem that can be modeled with dynamic programming. The state would represent the current time (sum of a_i's solved so far), and the current interval being considered, and track the maximum T_j so far.

But even that might be too slow. Let's think about the constraints.

n can be up to 1000, and m up to 1000.

Alternative approach:

We can model the problem as follows:

We need to assign each problem to a submission time in an interval, such that the sum of their solving times (in order) allows the submission times to be after the cumulative solving time. The maximum submission time is the minimal possible.

Alternatively, for each problem i, after solving it, we can choose any interval that starts after or during the time when it was solved, and assign its submission time to the earliest possible within that interval.

But again, the order matters.

This feels like a problem that can be optimized by greedily choosing the order and the submission times.

Wait, perhaps the optimal strategy is to solve the problems in non-decreasing order of a_i, or non-increasing. Let's think about the first example. The a_i's are 3 and 4. Solving the larger one first allowed the submission to fit into the earlier interval.

But maybe that's not the case. Let's think of another example. Suppose we have two intervals: first from 0 to 5, second from 10 to 15. Suppose the problems are 3 and 4. If we solve the 3 first (sum 3), then the 4 (sum 7). The submission for the first can be done at 3 (during first interval), submission for the second can be done at 10 (the start of the second interval). The total max is 10. If we reverse the order: solving 4 first (sum 4), submission at 4 (first interval), then solve 3 (sum 7), submission at 10. Max is 10. Same result. Hmm, so in this case, order may not matter. Maybe the order of solving affects the sum of the a_i's and thus the earliest possible submission times.

But perhaps the order of solving the problems affects the cumulative sum and thus which intervals are available for submission.

But how to model this?

Alternative idea: The total sum of a_i's is fixed. Wait, no. The sum depends on the order? No, the sum is the same regardless of the order. Oh right! Because addition is commutative. So the total time spent solving all the problems is fixed, equal to the sum of all a_i. But the order in which the a_i's are summed affects the cumulative sum after each problem. For example, solving a large a_i early can lead to a larger cumulative sum earlier, which may cause the submission time to be pushed into a later interval.

So the order of solving the problems determines the times when each problem is finished (S_i), which in turn determine the earliest possible submission time (the earliest interval that starts after S_i).

Wait, but the submission can be in any interval that is after S_i. So for each problem, the submission time is the earliest possible time >= S_i that is in any interval.

Thus, the maximum submission time is the maximum of all submission times. Our goal is to arrange the order of solving the problems such that this maximum is as small as possible.

So how to model the problem to find the minimal possible maximum submission time.

Let's think about this: For a given order of solving the problems, the cumulative sum after the first k problems is S_k = a_1 + a_2 + ... + a_k. For each problem k, the submission time is the earliest time T_k >= S_k that is in any interval. The maximum of all T_k is the answer for that order.

We need to find the order of the problems that minimizes this maximum.

This seems like a scheduling problem where the processing order affects the due dates.

But how to find the optimal order?

This problem resembles scheduling jobs to minimize the maximum deadline, where each job's deadline is the earliest possible submission time.

Wait, each job (problem) has a deadline of T_k, which depends on the cumulative time up to that job. So the problem is to arrange the order of the jobs such that the maximum T_k is minimized.

This feels similar to scheduling with the goal of minimizing the maximum completion time, where each job's completion time is determined by the cumulative sum and the intervals.

But I'm not aware of a standard algorithm for this problem.

Alternative approach: Since the submission time for each problem is the earliest possible in the intervals after its completion time, perhaps we can model this as follows.

For each problem i, when solved in some position in the order, its cumulative sum S is the sum of all a_j processed before it plus a_i. Then, the submission time T_i is the earliest time >= S in the intervals.

The maximum T_i across all i is the total answer for this order.

We need to arrange the order of the a_i's such that this maximum is minimized.

This seems like a problem where greedy approaches could be applied. For example, arrange the a_i's in an order that allows their S_i to be as early as possible, thereby allowing T_i to be as early as possible.

But how?

Wait, maybe the problem can be transformed. For each a_i, the submission time is determined by the cumulative sum up to its position. So the order in which we process the a_i's affects the cumulative sums, and thus the submission times.

To minimize the maximum submission time, perhaps we should arrange the a_i's such that the ones that have the earliest possible submission times are processed first. But since the submission times are dependent on the cumulative sums, this is not straightforward.

Alternatively, the problem is to arrange the a_i's such that the cumulative sums are as small as possible when possible to fit into earlier intervals. So processing smaller a_i first could lead to lower cumulative sums, allowing their submission times to be in earlier intervals. However, this might not always be the case. For example, a large a_i processed later may have a cumulative sum that pushes it into a later interval.

Alternatively, if we process the largest a_i first, then their cumulative sum is as large as possible early, but perhaps their submission can be done in a later interval, allowing smaller a_i to be processed later with lower cumulative sums.

Wait, in the first example, processing the larger a_i (4) first allows the submission to be in the first interval (since cumulative sum is 4, and the first interval ends at 4). Then the next cumulative sum is 4+3=7, which fits into the second interval starting at 7. So both submissions are in their respective intervals, and the maximum is 7.

If we processed the smaller a_i first, then the cumulative sum after the first problem is 3, which is in the first interval. Submission time is 3. The second cumulative sum is 7, which is in the second interval. The submission time is 7. So the maximum is 7. Same as before.

Wait, so in this case, the order does not affect the maximum submission time. But the submission times for the first problem are different. Hmm.

But in this example, the maximum is 7 regardless of order. So why is the sample output 7? Because both orders result in the same maximum.

So perhaps the order doesn't matter in some cases. But why in the first sample output, the order is mentioned as the second problem first? Because that's how the submission times are arranged.

But perhaps the order can affect whether the cumulative sum S_i for a problem is in a certain interval. For example:

Suppose intervals are [1, 5], [10, 15]. Problems are 6 and 3.

If we process 6 first: cumulative sum is 6. The earliest interval after 6 is [10,15]. So submission time is 10. Then processing 3, cumulative sum is 6+3=9. The earliest interval is [10,15]. Submission time is 10. Max is 10.

If we process 3 first: cumulative sum is 3. Submission is in [1,5] at 3. Then cumulative sum is 3+6=9. The earliest interval is [10,15]. Submission at 10. Max is 10. So same result.

But in this case, the order doesn't affect the maximum. So perhaps the order is not important as long as the sum is fixed. But this is not always the case.

Wait, another example. Intervals [1,4], [5,8], [9,10]. Problems 2 and 3.

Processing 2 first:

sum after first problem is 2 (submission in [1,4] at 2). Then sum 5 (after second problem). Submission in [5,8] at 5. Max is 5.

Processing 3 first:

sum after first problem is 3 (submission in [1,4] at 3). sum after second is 5 (submission in [5,8] at 5). Max is 5. Same result.

So again, order doesn't matter.

Hmm. So perhaps the order of solving the problems doesn't affect the maximum submission time. Because the sum of all a_i is fixed. So the total time taken is the sum, and the submission times are determined by the earliest possible intervals after each cumulative sum.

Wait, but the cumulative sums are different in different orders. For example, if the order is a1, a2, ..., an, the cumulative sum after the first problem is a1, after the second is a1+a2, etc. If the order is reversed, the cumulative sums are a_n, a_n + a_{n-1}, etc.

So for each problem, the cumulative sum when it's processed depends on its position in the order. Thus, the submission time for each problem depends on the order.

But how can we find an order that minimizes the maximum submission time?

This feels like a problem that can be transformed into scheduling with deadlines. Each job has a processing time, and the deadline is the earliest possible submission time based on the cumulative processing time up to that job. We want to arrange the jobs such that all deadlines are met, and the maximum deadline is minimized.

But the deadlines are not fixed; they depend on the order of processing.

This seems complicated.

Alternative idea: For a given order, the maximum submission time is the maximum of all the earliest possible submission times for each problem. The earliest possible submission time for a problem is the earliest time in any interval that is >= the cumulative sum up to that problem in the order.

Thus, the problem reduces to finding the permutation of the a_i's such that the maximum of these earliest submission times is minimized.

But with n=1000, checking all permutations is impossible. So we need a way to model this optimally without considering all permutations.

Perhaps we can model the problem with dynamic programming, where the state is the current cumulative sum and the set of problems solved so far. But this is not feasible for n=1000.

Alternatively, perhaps the problem can be viewed as finding the minimal possible maximum submission time, and then checking whether there's a way to arrange the order of solving the problems such that all submission times are <= that maximum.

This suggests a binary search approach. Let's say we want to check if a certain time T is possible. To check, we need to arrange the order of solving the problems such that each problem's submission time (earliest possible >= its cumulative sum) is <= T. Moreover, all submission times must be in some interval.

But how to model this check?

Alternatively, for a given T, we can compute for each problem the latest possible cumulative sum (S_i) such that the submission time (earliest >= S_i and <= T) exists. Then, arrange the problems in such an order that the sum of their a_i's plus any necessary waiting times allows their cumulative sums to be <= their latest possible S_i.

This seems vague. Let's think differently.

The binary search approach would have us guess a value T, and check whether all a_i's can be arranged in some order such that for each problem i, the cumulative sum up to that problem is <= the latest possible time S where the submission can be done by T. The S for each problem would be the maximum possible cumulative sum such that the submission time (earliest possible >= S) is <= T.

But how to find S for each a_i and T?

Alternatively, for each a_i, the cumulative sum S_i must be <= the latest possible time such that the submission time (the earliest time >= S_i in the intervals) is <= T.

But this depends on the intervals. For each a_i, the latest possible S_i is the largest time such that the earliest possible submission time (after S_i) is <= T.

This seems possible to compute for each a_i. For a given T, the latest possible S_i that allows submission by T is the latest S_i <= x, where x is the latest start time such that there's an interval covering x to T.

Wait, perhaps for each a_i, the latest possible S_i is the latest time S such that there exists an interval [l, r] where l <= S and S <= r, and r <= T. Or wait, the submission time can be any time >= S_i that is in an interval. So the submission time can be as small as the earliest interval after S_i. But to have submission time <= T, that earliest interval must have some overlap with [S_i, T].

So for a given T, the submission time for a problem completed at S_i is the earliest possible time >= S_i that is in an interval and <= T.

If no such interval exists (i.e., all intervals after S_i are after T), then T is invalid.

Thus, for each a_i, the latest possible S_i is the maximum S_i such that there exists an interval [l, r] with l <= r <= T, and S_i <= r. Because the submission time can be at l, but we need S_i <= r (since submission time >= S_i and <= r).

Wait, no. For example, if S_i is 5, and the next interval is [7, 10], and T is 10. Then the submission time is 7, which is >=5 and <=10. So in this case, S_i can be up to 10 (if the interval is [10, 10], which is impossible as per the problem's input constraints). Wait, the intervals are given such that lj < rj. So the latest possible S_i for that interval would be 7, but that's not correct. Wait, no. If S_i is 8, then the submission time is 8 (if it's within the interval). But the submission time must be in an interval. So for S_i, the submission time is the smallest possible T_j >= S_i such that T_j is in some interval.

So for a given T (the candidate maximum submission time), for each problem, the latest possible S_i (the cumulative sum up to that problem) is the largest S_i such that the earliest possible submission time for S_i is <= T.

But how to compute this for each a_i and T?

Alternatively, for a given T, the submission time of a problem solved at time S_i is the earliest time in any interval that is >= S_i and <= T. If there is no such time, then T is invalid.

So for each a_i, we need to find the latest possible S_i where the earliest possible submission time (based on S_i) is <= T.

To find this, for each a_i, the latest S_i is the maximum S_i such that there exists an interval where l_j <= S_i' <= r_j, and S_i' is the earliest possible submission time >= S_i.

Wait, this is getting complicated.

Alternatively, for each interval [l, r], we can note that if S_i is <= r, then the submission time for this problem can be at max(r, S_i) if S_i <= r. But wait, if S_i is during the interval [l, r], then submission can happen at S_i. If S_i is before the interval, but the interval starts after S_i (but before T), then submission can happen at l_j. But if the interval starts after S_i but ends before T, then the submission can be at l_j. Otherwise, if the interval starts after T, then it's not possible.

So for a given T, the submission time of S_i is the earliest time >= S_i in any interval and <= T.

Thus, for each S_i, we can check whether there exists an interval that starts after S_i and <= T. The earliest such interval's l_j would be the submission time, provided that l_j <= T.

So for a given T, the maximum possible S_i for which the submission time is <= T is the maximum S_i such that the submission time is found.

But how to compute this?

Alternatively, for each interval [l_j, r_j] where r_j <= T, the submission time can be in this interval. So, for S_i to have submission time in this interval, S_i must be <= r_j, and the submission time is max(S_i, l_j).

But to have submission time <= T, the interval must have r_j <= T.

So, for T to be a valid candidate, all intervals that are used must have r_j <= T.

So first, for a candidate T, all the intervals after T are irrelevant. So we can ignore any intervals where l_j > T.

So, for each candidate T, we can find all intervals [l_j, r_j] where r_j <= T. Then, for each problem's S_i, we need to find the earliest interval that can accommodate S_i.

So, the steps for binary search would be:

1. Compute the sum of all a_i's. The minimal possible T is the sum of all a_i's, but only if the sum is covered by an interval. Otherwise, it's higher.

2. Binary search on possible T values. For each T, check whether all a_i's can be scheduled in such a way that their cumulative sum (in some order) allows their submission time (earliest >= S_i) to be <= T.

But how to model this check?

The check would involve determining if there's an order of the a_i's such that, when processed in that order, each cumulative sum S_1, S_1 + S_2, ..., S_1+..+S_n can be submitted by time T.

But how to arrange the order of the a_i's to meet this.

An alternative idea is to arrange the a_i's in such a way that the cumulative sums are as small as possible, thus allowing them to fit into earlier intervals. But again, how to model this.

Wait, here's another approach. For a given T, the latest possible cumulative sum is the sum of all a_i's. If this sum is larger than the latest interval's r_j, then even if all submission times are in the latest possible interval, it's impossible.

But perhaps the sum of a_i's is S. If the latest interval's r_j is >= S, then maybe it's possible.

But this is not necessarily the case, because the submission for each problem can be in any interval. For example, if the sum is 10, and the latest interval is [9, 15], then the sum is 10 which is within this interval. But each individual cumulative sum may be earlier. But the sum could be 10, but individual cumulative sums could be 5, 10. So the submission of the first problem could be in an earlier interval, and the second in [9,15].

But if the sum is 10, but the earliest possible submission time for the cumulative sum of 5 is in an interval [1,4], and the sum of 10 is in [9,15], then T would be 10 (the submission time for the second problem).

So the sum is 10, which is <= T. So T can be 10.

But in this case, the sum is 10, and T is 10.

So perhaps the minimal T is the maximum between the sum of a_i's and the earliest possible submission time for the sum.

But this depends on the intervals.

Alternatively, the minimal possible T is the maximum of:

1. The sum of all a_i's.

2. The earliest submission time for the sum of all a_i's (i.e., the earliest interval that contains or is after the sum).

But this may not account for the individual submission times of each problem.

Wait, but in the problem, the submission of each problem must be done after it's solved, but not necessarily immediately. So the submission can be at any time >= the cumulative sum of the problems solved up to that point.

But if the sum of all a_i's is S, then all the cumulative sums are <= S. So if there's an interval that covers S, then all problems can be submitted at S. So the maximum submission time is S.

But if the sum S is not covered by any interval, then we have to find the earliest interval after S. The submission time for all problems would be the start of that interval, which is >= S.

But this is only possible if we can submit all problems at that interval. But the problem allows submitting all solutions at the same time.

Wait, here's a key insight. Once all problems are solved (after S = sum of a_i's), all submissions can be made at the earliest possible interval that starts at or after S. So if that interval exists, then the submission time is the start of that interval (if it's after S) or S itself (if S is within the interval). The maximum submission time for all problems is this time.

In this case, the order of solving the problems does not matter. Because the sum S is fixed. So the submission times for all problems can be at the same time, which is the earliest possible time >= S in any interval.

In this case, the problem reduces to checking whether there's an interval that starts at or after S, or contains S. If yes, then the answer is max(S, l_j), where l_j is the start of the earliest such interval. Otherwise, it's impossible.

But wait, the sample input 3 has sum 5, and the interval [1,5]. So submission time is 5. Which is the sum. So the maximum submission time is 5.

Another example: sum 7. The intervals are [1,4], [7,9]. The sum is 7, which is the start of the second interval. So submission time is 7.

In this case, the order of solving the problems is irrelevant. Because after solving all, the submission can be done at 7.

So the conclusion is that if the sum of a_i's is S, and there exists an interval that covers S (i.e., l_j <= S <= r_j) or starts at S (since the next interval may start at S), then the answer is S. Otherwise, it's the start of the earliest interval after S.

But what if the submission for individual problems can be done in earlier intervals, thereby allowing the maximum submission time to be less than S?

For example, sum S is 10. But during solving, some cumulative sums are in intervals, allowing their submission times to be earlier than 10. But the sum S is in an interval. So the maximum submission time is S (10).

But another case: sum is 10, but there is no interval that includes 10. The earliest interval after 10 starts at 15. So the submission time is 15. But for individual problems, their cumulative sums may be in earlier intervals. But the submission for those can be done at 15, but that's the maximum. So the answer is 15.

But what if some problems have cumulative sums that are in earlier intervals, and their submission times can be in those intervals, leading to a lower maximum submission time?

For example:

sum is 10. Intervals are [1,5], [6,7], [9, 12].

The earliest interval after 10 is [9, 12], since 10 is within it. So the submission can be done at 10. So the answer is 10.

But suppose there's a problem order where the cumulative sum after first problem is 3 (submitted at 3 in [1,5]). Then the next cumulative sum is 3+7=10, submitted at 10. So the maximum submission time is 10.

Alternatively, if the order is 7,3: cumulative sums 7 and 10. The first submission can be in [6,7] at 7. The second submission at 10. So maximum is 10.

So in this case, the order doesn't affect the maximum submission time. It's determined by the sum of the a_i's.

So this suggests that the minimal possible T is the earliest possible submission time for the sum S of all a_i's. But if that's possible, then that's the answer. Otherwise, the answer is the earliest submission time after S.

But then why does the first sample have a sum of 7 and the answer is 7?

Because the sum is 7, and the interval starts at 7. So the submission can be made at 7.

But in the first sample, the sum is 3+4=7. The submission times for both problems can be made at 7. So the maximum is 7.

But the sample explanation says that the first problem is submitted at 7, but that's because after solving it, the cumulative sum is 7. But in that case, the sum is 7. So the submission can be made at 7.

So, perhaps the minimal possible T is the earliest possible submission time after the sum S. So regardless of the order of solving the problems, the maximum submission time is determined by the sum of all a_i's and the intervals.

Thus, the solution is to compute the sum S of all a_i's. Then, find the earliest interval that includes S, or starts after S. The earliest possible submission time for S is the earliest possible time >= S in any interval.

If such an interval exists, the answer is the submission time of S. Otherwise, return -1.

But this would ignore the individual submission times of each problem. For example, if some cumulative sums are in earlier intervals, allowing their submission times to be earlier than the submission time of the sum S.

But in such cases, the maximum submission time would still be the submission time of the sum S, because that's the latest submission time.

So, the maximum submission time is the submission time of the sum S. So the order of solving the problems doesn't matter. The maximum submission time is determined solely by the sum of all a_i's and the intervals.

Wait, but this contradicts the first sample. In the first sample, the sum is 3+4=7. The submission time for the sum is 7 (the start of the interval [7,9]). So the answer is 7.

But according to the sample explanation, the submission for the first problem (which takes 3 time units) is done at 7. But the sum is 7. So the submission of the first problem is at 7, which is after its cumulative sum (4). Wait, wait, the sample's explanation says:

Pasha solves the second problem (4) first, then the first problem (3). So cumulative sum after first problem is 4, submission at 4. Then after second problem, cumulative sum is 7, submission at 7. So maximum is 7. But according to the sum-based approach, the submission time would be 7. So the maximum is 7.

But according to the sum-based approach, the answer would be the submission time of the sum (7) which is 7. Which matches the sample.

Another sample where the sum is 5 and the interval is [1,5]. Then the submission time is 5, which is the sum. So answer is 5.

But what if the sum is 5, and there's an interval [1,4], and another [6, 10]. Then the submission time for the sum would be 6, but perhaps some individual submissions can be made in [1,4]. But the latest submission is 6. So the answer is 6.

So regardless of the order, the answer is 6.

So the sum-based approach seems to work. But why?

Because even if some problems are submitted earlier, the latest submission time is when the sum is submitted, which is the earliest possible after S.

So, the problem reduces to finding the earliest possible submission time for the sum S of all a_i's, and the answer is that time if it exists. Otherwise, -1.

This would greatly simplify the problem. But is this correct?

Let's test the second sample:

Input:

1

5

1

1 4

The sum is 5. The intervals are [1,4]. The earliest possible submission time after 5 is none. So answer is -1. Which matches the sample.

Another test case where sum is 5, intervals are [1,5]. Sum is 5. So submission time is 5. Correct.

Another test case: sum is 5, intervals [3,6]. Submission time is 5 (since 5 is in the interval). Answer is 5.

Another test case: sum is 5, intervals [6,7]. Submission time is 6. Answer is 6.

But what if the sum is 6, but there's an interval [5,7] which includes 6. Then the submission time is 6.

So, according to this approach, the steps are:

1. Compute the sum S of all a_i.

2. Find the earliest interval where l_j <= r_j and r_j >= S. For such intervals, the submission time is max(S, l_j). If S is within the interval, submission time is S. Otherwise, if the interval starts after S, submission time is l_j.

3. If there are no such intervals, return -1.

4. Among all intervals that can include S or start after S, find the one with the smallest submission time (i.e., the earliest possible interval that can cover S).

Wait, but how to find this.

For example, if S is 7, and there are intervals [1,4], [5,7], [7,9], then the submission time can be 7 (from the second interval) or 7 (from the third interval's l_j). So the earliest possible submission time is 7.

If the intervals are [5,6], [7,10], then S is 7. The submission time would be 7 (the start of the second interval).

So the approach is to find the earliest interval that starts <= S and ends >= S. If there are none, find the earliest interval that starts after S. The submission time is the minimum between:

- S (if S is in some interval)

- the earliest l_j after S (if no interval contains S)

But wait, there could be a case where S is in interval A, but there's another interval B that starts after S. But we have to choose the submission time as S, since it's earlier than any l_j after S.

So the correct way is to find the earliest possible submission time >= S.

Which is the minimum between:

a) the smallest interval that contains S (i.e., l_j <= S <= r_j). In this case, submission time is S.

b) the earliest interval where l_j >= S. submission time is l_j.

If either a or b exists, the answer is the minimum between them. If both exist, take the minimum of the two. If neither exists, answer is -1.

So how to compute this?

We need to find:

- The minimal T such that T >= S and T is in some interval.

So T is the earliest possible time >= S that is covered by any interval.

This can be computed by:

1. For all intervals, check if S is within the interval. If yes, then T is S.

2. If not, check intervals that start after S. Among those, find the one with the earliest l_j. T is that l_j.

3. If no such interval exists, return -1.

So the steps are:

Compute S = sum(a_i).

Check if there exists an interval that contains S (l_j <= S <= r_j). If yes, then the answer is S.

If not, check if there's an interval with l_j >= S. Among those, find the minimal l_j. The answer is that l_j.

If neither exists, return -1.

Wait, but what about an interval that starts before S and ends after S but doesn't include S? For example, interval [5, 10], S is 7. Then S is within the interval, so submission time is 7.

Yes.

So this approach seems correct.

Thus, the solution is:

Calculate the total sum S of all a_i.

Check all intervals:

- If any interval has l_j <= S <= r_j: then the answer is S.

- Else, check all intervals with l_j >= S. Among them, pick the one with the smallest l_j. The answer is that l_j.

- If no such intervals, return -1.

But why did the first sample work with this approach?

Sample 1: sum is 7.

Intervals are [1,4], [7,9]. The sum 7 is covered by the second interval (7 <=7 <=9). So the answer is 7.

Sample 2: sum is 5. intervals [1,4]. No interval covers 5. Intervals after 5: none. So answer is -1.

Sample 3: sum is 5. intervals [1,5]. 5 is in the interval, answer is 5.

Another example:

sum is 6. intervals [5,7], [8,10]. sum 6 is in the first interval. answer is 6.

sum is 6. intervals [3,5], [7,10]. sum 6 not covered. The earliest interval after 6 is [7,10]. answer is 7.

sum is 6. intervals [3,5], [6,6]. but the input constraints say l_j < r_j. So [6,6] is invalid. So intervals must be given with l_j < r_j.

sum is 6. intervals [5,7], [6,8]. Both contain 6. So answer is 6.

Thus, this approach works.

So the problem reduces to finding the minimal possible submission time of the sum S.

Thus, the steps to solve the problem are:

1. Compute the sum S of all a_i.

2. Check if there's any interval that covers S (l_j <= S <= r_j). If yes, the answer is S.

3. Else, check for the earliest interval that starts after S. The answer is the l_j of that interval.

4. If neither exists, return -1.

This seems much simpler than considering the order of solving the problems. But why is that the case?

Because the latest submission time for any problem is the sum S. Because after solving all problems, the sum is S, and the submission for the last problem is S. But according to the problem statement, all problems can be submitted at the same time. So the submission time for all of them can be the earliest possible time >= S in the intervals. Thus, the maximum submission time is this time.

But wait, in the first sample, the submission time for the first problem is 4 (after solving the second problem) and the sum is 7. But according to this approach, the submission time is 7 for all problems. So why is the first submission at 4 possible?

Ah, because the submission of the first problem can be done in the first interval, but the submission of the second problem is done in the second interval. The maximum of these is 7. So according to the sum-based approach, the answer is 7, which is correct.

But according to the sum-based approach, the submission time is 7 for all problems. However, the sum-based approach is considering the submission time of the sum (7), which is the latest possible submission time. Even if some submissions are done earlier, the maximum is the latest.

So the sum-based approach works because the maximum submission time is determined by the submission time of the sum S, which is the earliest possible time >= S in the intervals. All other submissions can be done at this time, but some may have been possible earlier. However, their submission times do not affect the maximum, which is determined by the submission of the sum.

Thus, the order of solving the problems does not affect the maximum submission time. The maximum submission time is determined by the sum S and the intervals.

Thus, the correct solution is to compute the sum S and find the earliest possible submission time for S.

Therefore, the code can be written as follows:

- Read n, a list of a_i.

- Compute S = sum(a_i).

- Read m intervals, store them as a list.

- Check for any interval where l_j <= S <= r_j. If found, return S.

- Else, check for intervals where l_j > S. Find the minimal l_j among them. The answer is that l_j.

- If no such interval exists, return -1.

But wait, the intervals are given in chronological order and are non-overlapping and non-intersecting. So we can process them in order.

For example, to check if S is in any interval, we can loop through the intervals and check if l_j <= S <= r_j.

For the intervals after S, we can look for intervals where l_j > S. Since the intervals are sorted in chronological order, once we find the first interval with l_j > S, it's the earliest possible interval after S.

But since the intervals are sorted, the earliest possible l_j after S would be the first interval in the list where l_j > S. Because the intervals are in order and non-overlapping.

Wait, no. Because the intervals are sorted in increasing order of l_j and are non-overlapping. So, for example, if S is 6, and there are intervals [1,2], [3,5], [7,8], [9,10], then the earliest interval after S is [7,8].

But if the intervals are [3,5], [7,8], [10, 15], and S is 6, then the first interval with l_j >6 is [7,8], which is the earliest possible.

So, to find the earliest interval after S, we can iterate through the intervals in order and find the first interval where l_j > S. Once found, that interval's l_j is the earliest possible.

Alternatively, since the intervals are sorted, we can perform a binary search for the first interval where l_j > S.

For example, for each interval in the list, check if l_j > S. The first such interval is the earliest possible.

Once found, that interval's l_j is the earliest possible submission time.

But the code can be optimized for this.

Thus, the code steps:

Compute S.

Check if any interval contains S. If yes, return S.

Else, find the earliest interval where l_j > S. If such an interval exists, return l_j.

Else, return -1.

But how to check if S is in any interval.

This can be done with a loop:

for l, r in intervals:

    if l <= S <= r:

        return S

Then, find the earliest interval with l > S.

If there are such intervals, the first one in the list (since the intervals are sorted) is the earliest.

So, for the intervals:

We can loop through them again, and find the first interval where l > S.

If found, return l.

Else, return -1.

This would handle all cases.

Let's test this against the samples.

Sample 1:

sum S is 7.

Check intervals:

[1,4] -> 7 is not in here.

[7,9] -> l=7 <=7 <=9. So return 7.

Sample 2:

sum is 5.

Intervals: [1,4]. 5 not in. Check for intervals with l>5. None. Return -1.

Sample 3:

sum is5. interval [1,5]. 5 is in. Return 5.

Another test case: sum 6. intervals [3,5], [7,8]. 6 is not in any interval. The first interval with l>6 is [7,8]. return 7.

Another case: sum is6. intervals [5,7], [8,9]. 6 is in [5,7]. return 6.

Thus, this approach works.

So, the code can be written as follows.

First, read n, the a_i list, compute S.

Read m, then read m intervals as a list.

Check each interval for l <= S <= r.

If found, output S.

Else, iterate through the intervals to find the first interval where l > S.

If found, output l.

Else, output -1.

But wait, the intervals are given in chronological order, which implies that l_j is increasing. So once we find the first interval with l_j > S, that's the earliest possible l_j.

Thus, the code can be written in Python as:

n = int(input())

a = list(map(int, input().split()))

S = sum(a)

m = int(input())

intervals = [tuple(map(int, input().split())) for _ in range(m)]

found = False

for l, r in intervals:

    if l <= S <= r:

        print(S)

        exit()

# Now find the earliest interval with l > S

earliest = None

for l, r in intervals:

    if l > S:

        if earliest is None or l < earliest:

            earliest = l

if earliest is not None:

    print(earliest)

else:

    print(-1)

Wait, but since the intervals are sorted in chronological order, once we find the first interval with l > S, that's the earliest. So we can break the loop once we find it.

So the code can be optimized to:

for l, r in intervals:

    if l > S:

        earliest = l

        break

But no. Because there may be intervals with l > S but not in the first one. For example, if the intervals are [5,6], [7,8], [9,10], and S is 6. So the first interval after S is [7,8].

But in the code above, the first interval with l > S is [7,8], which is correct.

Thus, the code can be written as:

after_sum = None

for l, r in intervals:

    if l > S:

        after_sum = l

        break

if after_sum is not None:

    print(after_sum)

else:

    print(-1)

Wait, but this is incorrect. Because the first interval with l > S may not be the earliest.

Wait, no. Since the intervals are sorted in chronological order, each subsequent interval has a larger l. So the first interval in the list with l > S is the earliest possible.

Yes, because the intervals are given in chronological order, so each l_j is larger than the previous r_{j-1}. So the intervals are strictly increasing. So, for example, intervals are in order, and l_j increases.

Thus, the first interval with l_j > S is the earliest possible interval after S.

So the code can be written as:

for l, r in intervals:

    if l > S:

        earliest = l

        print(earliest)

        exit()

print(-1)

So combining all steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    S = sum(a)

    m = int(input_stream.readline().rstrip("\n"))

    intervals = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(m)]

    for l, r in intervals:

        if l <= S <= r:

            print(S, file=output_stream)

            return

    for l, r in intervals:

        if l > S:

            print(l, file=output_stream)

            return

    print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
5
1
1 4
""",
            "output": \
"""\
-1
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    S = sum(a)

    m = int(input_stream.readline().rstrip("\n"))

    intervals = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(m)]

    for l, r in intervals:

        if l <= S <= r:

            print(S, file=output_stream)

            return

    for l, r in intervals:

        if l > S:

            print(l, file=output_stream)

            return

    print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
5
1
1 5
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

Third sample: sum 5, interval [1,5]. Check first loop: 5 is in. Print 5.

Another example: sum 6, intervals [3,5], [7,8]. First loop: no. Second loop: [7,8] is first l>6. Print 7.

Yes.

Thus, this code should work.

But wait, what if there are intervals after S but their l is not the earliest? For example, intervals [1,2], [5,6], [7,8]. S is 3. The first interval after S is [5,6], which l=5>3. So the code would print 5, which is correct.

Thus, the code is correct.

Thus, the correct solution is to compute the sum of all a_i's and check if there's an interval containing the sum, else check for the earliest interval after the sum.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
m = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(m)]

# Check if total is within any interval
for l, r in intervals:
    if l <= total <= r:
        print(total)
        exit()

# Find the earliest interval starting after total
for l, r in intervals:
    if l > total:
        print(l)
        exit()

print(-1)
```
