<think>
Okay, let's see. So Valera has to take n exams. For each exam, he can choose to take it either on day bi or ai. But the order in which the exams are recorded in the book must have non-decreasing ai. The problem is to find the earliest possible day when the last exam is taken, such that the a_i's are non-decreasing in the order he takes them.

Wait, the a_i's are the dates written in the book. So when he takes an exam, the a_i is fixed. But he can take the exam on bi or ai. The order of the exams in the record book must be such that the a_i's are in non-decreasing order. So Valera must choose an order of taking the exams where each subsequent exam's a_i is >= the previous one's a_i. And for each exam in this sequence, he picks either bi or ai as the actual day he takes it. The goal is to minimize the maximum of the days he takes each exam (since the last day is the maximum of all chosen days).

Hmm. So the problem is twofold: choose an order of the exams such that their a_i's are non-decreasing, and for each exam in that order, choose either bi or ai, such that when you process them in order, each exam is taken on a day (bi or ai) that is as early as possible, but also such that the sequence of a_i's is non-decreasing. Then, find the minimal possible last day.

Wait, but the order of the exams is crucial here. Because the a_i's must be non-decreasing in the order taken. So, the first step is to arrange the exams in an order where their a_i's are non-decreasing. Because if they are taken in any order where a_i's are not non-decreasing, it's invalid. So the exams must be ordered such that a_1 <= a_2 <= ... <= a_n (assuming the order is chosen as such). But each exam's a_i is fixed, but their order in the sequence can be any permutation that is non-decreasing in a_i. Wait no— the order in which Valera takes the exams must be such that the a_i's are non-decreasing. So for example, if he takes exam 1 first, then exam 2, then a_1 must be <= a_2.

So the first thing is that the exams must be sorted by their a_i's. Because if they are not sorted, the sequence would have a higher a_i followed by a lower one, which violates the non-decreasing condition. So Valera must arrange the exams in the order of their a_i's in non-decreasing order. But wait, maybe not. Wait, no. For example, the first sample input has exams with a_i's 5,3,4. The sorted order would be 3,4,5, which is what the sample uses. Because then the a_i's are in order. So the correct order must be sorted by a_i. Because otherwise, if you take exams in a different order, their a_i's would not be non-decreasing.

So the first step is to sort the exams in non-decreasing order of a_i. Then, for each exam in this sorted order, decide whether to take it on b_i or a_i, such that the day chosen (b_i or a_i) is as early as possible, but also ensures that the sequence of days chosen is such that each subsequent exam is taken on a day >= the previous exam's day. Wait, no. The days when the exams are taken (bi or ai) can be in any order, but the a_i's of the exams in the order taken must be non-decreasing. The actual days when the exams are taken (bi or ai) don't directly affect the a_i's sequence. Wait, no. The a_i's are part of the exam's data. So the order of the exams must be such that their a_i's are non-decreasing. But the actual day chosen (bi or ai) for each exam is the day Valera takes it. But when he takes an exam, the a_i is the date written in the book, which must be non-decreasing. So the order in which the exams are taken must have their a_i's non-decreasing. So the exams must be ordered in non-decreasing a_i's. Because if you take exam X first, then exam Y, then a_X must be <= a_Y. Therefore, the exams must be sorted in non-decreasing order of a_i. So the first step is to sort the exams by a_i.

Once the exams are sorted, the problem reduces to, for each exam in this sorted order, choosing whether to take it on bi or ai, such that the day chosen for each exam is >= the day chosen for the previous exam. And we want to minimize the maximum day (which is the last day).

Wait, but we need to ensure that the sequence of days when the exams are taken is non-decreasing. Because Valera takes exams in a certain order. For example, if the first exam is taken on day 3, the next must be taken on day >=3. So the days must form a non-decreasing sequence. Because each exam is taken on a day (bi or ai) which can be earlier or later than the previous day. But since the order of taking exams is fixed once the a_i's are sorted, the problem becomes: for each exam in the sorted order, choose bi or ai, such that the choice for each exam is >= the previous choice, and the maximum (the last choice) is as small as possible.

Yes. So the problem becomes dynamic programming. Because for each exam in the sorted list, the choice of taking it on bi or ai depends on the previous choice's day.

Let's model this with dynamic programming. For each position i in the sorted list, and a possible previous day, we track the earliest possible day for the i-th exam.

But with n up to 5000, a naive DP approach might be O(n^2), but that's manageable if each state is small.

Let me think. Let's sort the exams by a_i. Let's consider the sorted list of exams as (a_1, b_1), (a_2, b_2), ..., (a_n, b_n), where a_1 <= a_2 <= ... <= a_n.

Now, for each exam i in this list, we can choose to take it on day d_i, which is either b_i or a_i. But the day d_i must be >= d_{i-1}.

The goal is to choose all d_i such that d_i >= d_{i-1}, and the maximum d_i is minimized.

Wait, no. The maximum is the last day, but since each d_i must be >= the previous, the maximum is just the last d_i. So we need to minimize d_n.

But how?

So for each position i, the choice is between b_i and a_i. But the choice must be >= the previous day.

We can model this with dynamic programming. Let's define dp[i][x] as the earliest possible day for the i-th exam, where x can be 0 (taking b_i) or 1 (taking a_i). But for each step, we need to track the previous day.

Wait, perhaps more precisely, for each i, we can track the earliest possible day that we can choose for the i-th exam, given the previous choice. But since the previous choice can be up to the previous a_{i-1} or b_{i-1}, but in the sorted list, a_{i} >= a_{i-1}, perhaps we can model this with a state that represents the last day chosen.

So for the i-th exam, the last day is some value. The state is the last day chosen. For each i, we can track the possible last days and choose the minimal possible.

But with n=5000, and possible days up to 1e9, this seems impossible. So we need a way to model the state efficiently.

Alternatively, since each exam has two choices, maybe for each step i, the possible last days are either the previous day's choice (either a_{i-1} or b_{i-1} or something else) but perhaps it's manageable.

Wait, but after each step, the last day can be either the chosen day of the current exam. So for each i, when processing the i-th exam, the previous day is known, and we can choose between b_i and a_i, but must be >= previous day.

So the DP state can be represented as the last day chosen after i exams. For the i-th exam, the possible options are:

- Take b_i, if b_i >= previous day. Then the new last day is max(prev_day, b_i) ?

Wait, no. The new day would be the day chosen for the i-th exam, which must be >= previous day.

So when processing the i-th exam, the previous day is d_prev. For the i-th exam, we can choose:

Option 1: Take it on b_i, but only if b_i >= d_prev. The new d_prev becomes b_i.

Option 2: Take it on a_i, but only if a_i >= d_prev. The new d_prev becomes a_i.

But what if both options are possible? Then we choose the one that leads to the minimal maximum day.

Wait, but since we want to minimize the final day, perhaps we need to choose the earliest possible day for each step, as long as it's feasible.

But how?

At each step i, the earliest possible day we can take the i-th exam is the minimal between b_i and a_i, provided that it's >= the previous day.

So for each step i, given the previous day d_prev, the possible choices are:

If we can take b_i (since b_i >= d_prev), then that's better than taking a_i (since b_i is smaller than a_i). So we would choose b_i if possible.

But if taking b_i is possible (b_i >= d_prev), then we take it. Because that gives a lower d_prev for future steps, which allows more flexibility.

Alternatively, if taking a_i is possible (a_i >= d_prev), but b_i is not (b_i < d_prev), then we have to take a_i.

But there might be cases where taking a_i even when b_i is possible could lead to a better overall result. Wait, no. Because if we take b_i now, the next exams can choose earlier days, leading to a smaller final day. So it's better to choose the earliest possible day for each exam, as long as it's feasible.

So the greedy approach would be: after sorting the exams by a_i, for each exam in order, choose the earliest possible day (either b_i or a_i) that is >= the previous day. So for each exam, first try to choose b_i if possible (i.e., if b_i >= previous day). If not possible, choose a_i if possible. If neither is possible, then it's impossible? But according to the problem statement, Valera can take the exams on a_i, which is >= previous a_i, since the exams are sorted. But a_i is >= previous a_{i-1}, which in turn is >= the previous day (since in the sorted order, the previous a_{i-1} is part of the previous day's choice). Wait, no. Because the previous day could have been a_{i-1} or b_{i-1}.

Wait, let's think again. The exams are sorted by a_i. So a_1 <= a_2 <= ... <= a_n.

We process them in this order.

For the first exam, the previous day is 0 (since there's no previous). So for the first exam, we can choose between b_1 and a_1. We should choose the earliest possible day, which is b_1. So the first day is min(b_1, a_1) → which is b_1, since b_i < a_i. So first day is b_1.

Then, for the second exam, the previous day is b_1. We can choose between b_2 and a_2. But they have to be >= b_1. So if b_2 >= b_1, we take b_2. Else, take a_2. Since a_2 >= a_1 >= b_1. Because a_2 >= a_1 (sorted) and a_1 >= b_1 (since b_1 < a_1). So a_2 >= b_1. So for the second exam, a_2 is always >= previous day. So if b_2 >= previous day, take it. Else, take a_2.

So this seems to form a greedy approach. For each exam in the sorted order, choose the earliest possible day (b_i if possible, else a_i), given that it's >= previous day.

But wait, maybe not. Let's look at the first sample:

Sample 1:

3 exams.

After sorting by a_i, the order is:

3 1 (a=3, b=1)

4 2 (a=4, b=2)

5 2 (a=5, b=2)

Processing:

First exam: choose 1 (b_i). previous day is 1.

Second exam: can choose 2 (b_i) since 2 >=1. previous day becomes 2.

Third exam: can choose 2 (b_i) since 2 >=2. previous day is 2. But a_i is 5, but since b_i is 2, which is <= previous day. So no, wait. Wait, the third exam is (5,2). The previous day is 2. So for this exam, the choices are 2 (b_i) and 5 (a_i). 2 is >=2 → yes. So we take 2. Then the last day is 2, which is correct.

So the greedy approach works here.

Sample 2:

3 exams.

After sorting by a_i:

4 3 (a=4, b=3)

5 2 (a=5, b=2)

6 1 (a=6, b=1)

Processing:

First exam: choose 3 (b_i). previous day is 3.

Second exam: can choose 2 (b_i), but 2 <3. So not possible. So must choose a_i=5. previous day becomes 5.

Third exam: can choose b_i=1 <5 → no. So choose a_i=6. Last day 6. Which matches the sample.

So the greedy approach works here.

Another test case: what if choosing a_i earlier allows more options for later exams?

For example, let's say we have two exams:

Exam1: a=5, b=3

Exam2: a=6, b=4

In sorted order: exam1, exam2.

Greedy approach: exam1 is taken on day 3. Then exam2 can take b_i=4 >=3 → day 4. So last day is 4.

But if we took exam1 on day 5 (a_i), then exam2 can take b_i=4, which is less than 5 → so must take a_i=6. Last day 6. So the greedy approach is better here.

Another test case where the greedy approach is not optimal. Wait, can that happen?

Suppose:

Exam1: a=10, b=2

Exam2: a=20, b=5

Exam3: a=30, b=15

Sorted order: exam1, exam2, exam3.

Greedy approach:

Exam1: take 2. previous day 2.

Exam2: can take b=5 >=2 → take 5. previous day 5.

Exam3: can take b=15 >=5 → take 15. last day 15.

Alternative approach:

Exam1: take a_i=10.

Exam2: take b=5 (but 5 <10 → not possible. So take a_i=20.

Exam3: take b=15 <20 → must take a_i=30. Last day 30.

So the greedy approach is better.

Another example where taking a_i earlier might be better? Let me think.

Exam1: a=3, b=1.

Exam2: a=5, b=3.

Exam3: a=6, b=4.

Sorted order.

Greedy:

Day1: 1 → exam1.

Day2: 3 (b_i) → exam2.

Day3: 4 (b_i) → exam3. Last day 4.

Alternatively, if exam2 is taken on a_i=5, then exam3 can take b_i=4 (but 4 <5 → not allowed. So must take a_i=6. Last day 6.

So the greedy approach is better.

Another example where not taking the earliest possible day might lead to a better overall result. Let's see:

Exam1: a=5, b=1.

Exam2: a=10, b=3.

Exam3: a=15, b=6.

Greedy approach:

Exam1: day 1.

Exam2: can take 3 >=1 → day3.

Exam3: can take 6 >=3 → day6. Last day 6.

But if we take exam1 on day1, exam2 on day3, exam3 on day6. All a_i's are 5,10,15, which is sorted. So all is good.

Another scenario: exam1: a=5, b=1.

Exam2: a=10, b=6.

Exam3: a=15, b=7.

Greedy approach:

Exam1: day1.

Exam2: take b=6 >=1 → day6.

Exam3: take b=7 >=6 → day7. Last day 7.

Alternatively, for exam2, if we take a_i=10, then exam3's b_i=7 <10 → must take a_i=15. So last day 15. So worse.

So again, the greedy approach works.

Wait, but is there any case where taking a_i instead of b_i (when possible) leads to a better result?

Suppose:

Exam1: a=4, b=1.

Exam2: a=5, b=3.

Exam3: a=6, b=5.

Greedy approach:

Exam1: day1.

Exam2: can take 3 → day3.

Exam3: can take 5 → day5. Last day 5.

Alternative approach:

If exam2 is taken on a_i=5 (since 5 >=1), then exam3 can take b_i=5 (5 >=5). So day5. Same result.

So in this case, choosing either option for exam2 gives same last day.

But what if:

Exam1: a=4, b=1.

Exam2: a=5, b=3.

Exam3: a=7, b=5.

Greedy approach:

Exam1: day1.

Exam2: take3 → day3.

Exam3: take5 → day5. Last day5.

Alternative approach for exam2: take a_i=5. Then exam3 can take5 (b_i=5 >=5). So same last day.

So in this case, same result.

Another scenario where taking a_i might lead to better result. Let's see:

Exam1: a=3, b=1.

Exam2: a=5, b=4.

Exam3: a=6, b=2.

Sorted order.

Greedy approach:

Exam1: day1.

Exam2: take4 → day4.

Exam3: can take2 <4 → no. So take a_i=6 → day6. Last day6.

Alternative approach: For exam2, take a_i=5. Then exam3 can take b_i=2 <5 → no. Must take a_i=6. So last day6. Same result.

Hmm. So in all these examples, the greedy approach seems to work.

So perhaps the greedy approach is correct. The idea is:

Sort the exams in non-decreasing order of a_i.

For each exam in this order, choose the earliest possible day (b_i if possible, else a_i) that is >= the previous day.

If that's correct, then the solution is straightforward.

But how to prove that this approach is correct?

Proof sketch:

Assume that the exams are sorted in non-decreasing a_i order.

We need to choose for each exam i, d_i (either b_i or a_i) such that d_i >= d_{i-1}, and the sequence of a_i's is non-decreasing (which is ensured by the sorted order).

The goal is to minimize the last d_i.

At each step i, choosing the earliest possible d_i (i.e., the minimal possible d_i that is >= d_{i-1}) gives the best possible choice, because it allows more flexibility for future steps (i.e., choosing smaller days for subsequent exams).

Choosing a higher d_i now might force subsequent exams to choose higher days, leading to a higher last day.

Thus, the greedy approach of choosing the earliest possible d_i at each step is optimal.

Therefore, the solution is to:

1. Sort the exams in non-decreasing order of a_i.

2. For each exam in this order, choose d_i as the earliest possible (b_i if possible, else a_i) such that d_i >= previous day.

So the code can be written as:

Sort the exams by a_i.

Initialize prev_day = 0.

For each exam in sorted order:

    if b_i >= prev_day:

        take b_i, prev_day = b_i

    else:

        take a_i, prev_day = a_i

The final prev_day is the answer.

Wait, but let's test this against the sample inputs.

First sample input:

3

5 2

3 1

4 2

Sorted by a_i: 3,4,5.

Processing:

prev_day =0.

First exam (a=3, b=1). Since 1 >=0 → take 1. prev_day=1.

Second exam (a=4, b=2). 2 >=1 → take 2. prev_day=2.

Third exam (a=5, b=2). 2 >=2 → take2. prev_day=2.

Output is 2. Which matches.

Second sample:

3

6 1

5 2

4 3

Sorted by a_i:4,5,6.

Processing:

prev_day=0.

First exam: a=4, b=3. 3 >=0 → take3. prev_day=3.

Second exam: a=5, b=2. 2 <3 → take5. prev_day=5.

Third exam: a=6, b=1. 1 <5 → take6. prev_day=6. Output 6. Correct.

Another example where the previous day is a_i of previous exam.

Another example:

n=2

a1=3, b1=1

a2=5, b2=4.

prev_day after first exam:1. Second exam: b=4 >=1 → take4. prev_day=4.

But if the second exam's a_i=5, then 4 is better.

Another case where taking a_i is better. But according to the logic, the code would take b_i.

Wait, but what if:

Exam1: a=3, b=2.

Exam2: a=5, b=1.

Sorted by a_i.

Processing:

prev_day=0.

Exam1: take2 (b_i). prev_day=2.

Exam2: b_i=1 <2. So take a_i=5. prev_day=5.

So output 5.

But if for exam1, we took a_i=3, then exam2 can take b_i=1 <3 → take a_i=5. So same result. So the code gives the same result.

So the code seems correct.

Thus, the approach is to sort the exams by a_i, then for each in order, choose the earliest possible day (b_i if >= prev_day, else a_i).

So the code can be written as:

Read n.

Read the n pairs (a_i, b_i).

Sort the list by a_i in non-decreasing order.

Initialize prev_day = 0.

For each (a, b) in the sorted list:

    if b >= prev_day:

        take b. prev_day = b.

    else:

        take a. prev_day = a.

Output prev_day.

Yes. That's the code.

Wait, but in the first example, after taking the first exam's b_i=1, the next exam's b_i=2 is taken. Then the third exam's b_i=2 is taken. So the code works.

Thus, the code is simple and efficient. The sorting is O(n log n), and the loop is O(n), which is acceptable for n up to 5e3.

So this is the optimal approach.
</think>

```python
n = int(input())
exams = []
for _ in range(n):
    a, b = map(int, input().split())
    exams.append((a, b))
exams.sort()
prev_day = 0
for a, b in exams:
    if b >= prev_day:
        prev_day = b
    else:
        prev_day = a
print(prev_day)
```