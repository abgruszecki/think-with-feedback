<think>
Okay, let's see. The problem is about Vasya receiving messages over time and deciding when to read them to maximize his bank account. Hmm. So each message comes in at a certain time ti, and he can read it any time after ti but before or at T minutes. The goal is to find the maximum possible money he can have after T minutes.

Let me re-read the problem statement to make sure I get all the details right. 

Each message's cost starts at A and decreases by B each minute after it's received. So if a message is received at ti and read at time x (x >= ti), the value added to the bank is A - B*(x - ti). Additionally, each minute, Vasya's account gets C multiplied by the number of unread messages. So every minute from when the message arrives until it's read, that message contributes C each minute to the account. But once it's read, it stops contributing to the C part.

The problem says all messages must be read by T minutes. So for each message, we have to choose a read time x_i where ti <= x_i <= T. Then the total is the sum of each message's (A - B*(x_i - ti)) plus the sum of all the C * k for each minute from 1 to T, where k is the number of unread messages at that minute.

Wait, how does the C contribution work? For each minute, during that minute, the account increases by C multiplied by the number of received but unread messages at that time. So for example, if a message is received at ti=2 and read at x_i=5, then from minute 2 to 4 (inclusive?), the message is unread. Wait, the time units: the message is received after ti minutes. So the initial time is 0, and after each minute, ti is the time when it's received. Then, each minute from ti to T-1? Or up to T?

Wait, the problem says that the messages are received after ti minutes. So the timeline is minutes from 1 to T. For example, if ti is 1, the message arrives at the end of minute 1. Then, from minute 2 onwards, it can be read. Or maybe the messages arrive at the start of the minute. Hmm, maybe the exact timeline needs to be clarified.

Alternatively, perhaps the timeline is considered in the following way: during each minute, any messages that arrived at or before that minute can be read. Then, the C contribution for that minute is based on the number of unread messages at the start of the minute. Or maybe after processing reads during the minute. Because the problem states that Vasya can read messages after receiving them at any moment. So perhaps the reads can happen at any time during the minute, but the C contribution is calculated for each minute based on how many messages are unread during that entire minute.

This is a bit ambiguous, but perhaps the way to model it is to think of each minute as a unit. For each minute m (from 1 to T), the C contribution is C multiplied by the number of messages that were received before or at m, and not yet read before m. Because if a message is read during minute m, then in minute m, it's unread for part of the time. But since the problem says Vasya can read messages at any moment, maybe the C contribution for minute m is the number of messages that are unread at the start of the minute. Or maybe the C is added per minute, regardless of when during the minute the message is read.

Alternatively, perhaps the C is calculated for each minute (from 1 to T) as the number of messages that have been received (ti <= current time) and haven't been read yet (x_i > current time). So each minute m contributes C * (number of messages where ti <= m and x_i > m). Then, the sum over all m from 1 to T of C * (number of such messages for each m).

So the total contribution from C is C multiplied by the sum over all minutes m from 1 to T of the number of messages that are unread during minute m. For each message i, the time it's unread during is from ti to x_i - 1. Because if the message is read at x_i, then it's unread during all minutes starting from ti up to x_i - 1. So for each message i, the number of minutes it contributes to the C part is (x_i - ti) if x_i >= ti. Wait no: if ti is 1 and x_i is 3, then the message is unread during minute 1 (if x_i is read at 3, which is after minute 3? Or during minute 3? Hmm, perhaps the time steps are considered as points. Let's re-express the problem.

Each message is received at time ti. Then, Vasya can read it at any time x >= ti (exact moment, perhaps x can be up to T). For each message, the time between ti and x (exclusive?) is when it's unread and contributes to the C per minute.

Wait, the problem says that each minute Vasya's account receives C*k, where k is the number of received but unread messages. So for each minute m (from 1 to T), how many messages are unread during that minute. A message is unread during minute m if it was received at or before m, and hasn't been read yet. So the time when the message is considered unread is from the minute after it's received until the minute before it's read. Or maybe including the minute it's read. Wait, no: if the message is read at time x, then up to and including x, is it unread? Let's think:

Suppose a message is received at ti=2. If it's read at x=5, then during minutes 2, 3, 4, and 5, the message is unread during those minutes. Wait, but when you read it at x=5, does that mean during minute 5 the message is unread for the entire minute, and then after reading it at the end of minute 5, it's no longer unread? Or is the read happening at the start of minute 5, making it unread only up to minute 4?

This is critical because it affects the C contribution. For example, in the first sample input:

4 5 5 3 5

ti's are [1,5,5,4]. So T=5. The sample says that reading all messages immediately gives 4*5=20. So in this case, all messages are read at their ti. So for message 1 (ti=1), read at x=1. So the unread time is from 1 to 0? No. So for each message read at x=ti, the number of minutes they contribute to the C is (x_i - ti) = 0. So the C contribution is 0. Then the total is 4*5 (from the message values) plus 0*C, which equals 20, matching the sample.

But in the third sample, when all messages are read at T=5:

Each message i has ti from 1 to 5. For message 5, ti=5, x_i=5. So it's unread for 0 minutes. For message 4, ti=4, x_i=5: contributes 1 minute (minute 4 to 4). Wait, how?

Let me see the third sample's note:

He reads all messages at T=5. So for each message:

Message 1 (ti=1, x=5): unread from ti=1 to x-1=4. So 4 minutes. So C contribution is 4*C per message. But the note says that during each minute, the number of unread messages is 1,2,3,4,5, etc. Wait, the note says:

"In the third sample messages must be read at the moment T. This way Vasya has 1, 2, 3, 4 and 0 unread messages at the corresponding minutes, he gets 40 points for them. When reading messages, he receives (5 -4*3) + ... = -5. Total 35."

Wait, the C part contributes 40. Let's calculate how that happens.

Each message is read at x_i=5. So for each message i with ti:

The time between ti and x_i (5) is 5 - ti. For each such message, the number of minutes where it's unread is (5 - ti) minutes. Because from ti to 5-1 =4? Or to 5?

Wait, the note says that during the first minute (time 1?), the number of unread messages is 1, then 2, etc. So for example:

Take message 1 (ti=1): it is unread during minutes 1,2,3,4. Because x_i=5. So in minute 5, when he reads it, it's part of the unread during that minute? Or not?

But according to the note, the sum of C*k is 40. Let's compute:

C=4, T=5.

In each minute m from 1 to 5:

At minute m=1: messages received at ti <=1: just the first one (ti=1). It's unread (since x_i=5). So k=1. Contribution 4*1 =4.

m=2: messages ti<=2 are first and second. But according to the input, the third sample's ti's are [1,2,3,4,5]. So in m=2, the first two messages are unread. So k=2. Contribution 4*2=8.

m=3: three messages unread. Contribution 12.

m=4: four messages. Contribution 16.

m=5: five messages (ti=5 is received at m=5, and x_i=5, so during minute 5, it's unread for the entire minute?), but when he reads it in m=5, does that count?

Wait, the note says that during the corresponding minutes (like m=5) he has 0 unread messages. But according to the note, the sum is 40. Let's compute:

Sum of C*k per minute:

For m=1: 1 unread messages (ti=1).

m=2: 2 (ti=1,2).

m=3: 3 (ti=1,2,3).

m=4:4 (1,2,3,4).

m=5:5 (all 5 messages, including ti=5, since they are read at x_i=5, which is at T=5. So during m=5, they are unread until he reads them. So for the entire minute, they are unread. So k=5 for m=5.

So the sum is 1+2+3+4+5 =15. Multiply by C=4 gives 60. But the note says 40. Hmm, this contradicts. Wait, the note says:

"In the third sample messages must be read at the moment T. This way Vasya has 1, 2, 3,4 and 0 unread messages at the corresponding minutes, he gets 40 points for them. When reading messages, he receives ... -5 points. This is 35 in total."

Wait, the sum of the C parts is 40. How?

Hmm. Let's compute the sum again. The note says that during the corresponding minutes (1,2,3,4,5), the unread messages are 1,2,3,4,0. Wait, that can't be. Because if all messages are read at T=5, then during minute 5, all messages are unread until they are read. So during minute 5, for each message received at ti <=5, they are unread until they are read at x_i=5. So during minute 5, all messages are unread (since x_i=5 is the time when they are read, so during that minute, before being read, they are unread). Wait, but how many messages are received by minute m=5? All 5, since ti=5. So during m=5, all 5 messages are unread. But the note says that for the fifth minute, the k is 0. That suggests that the messages are read before minute 5 starts. Or perhaps the read is done at the very beginning of the minute.

This suggests that the C contribution for minute m is based on the state of the messages after processing reads during that minute. So perhaps when a message is read at time x, it's considered as being read at the start of minute x, so that during minute x, it's no longer unread.

In that case:

For example, message received at ti, read at x. Then, the number of minutes it contributes to C is (x - ti) minutes. Because during minutes ti to x-1 inclusive, the message is unread. Then, in minute x, it's already read, so doesn't contribute.

So the C contribution for a message i is C multiplied by (x_i - ti). So for each message, the total contribution from C is C*(x_i - ti). Because each day from ti to x_i-1, the message contributes 1 to k. So sum over all m from 1 to T of C*k is equal to C multiplied by the sum over all messages of (x_i - ti) * 1, because each day between ti and x_i-1 (inclusive) the message is part of k.

Wait, that's a key insight. Let's model it:

For each message i, the C contribution is C multiplied by the number of minutes between ti and x_i-1, inclusive, where the message is unread. The total for all messages is sum over i of C*(x_i - ti). Because each such day adds 1 to k for that message. So the total C contribution is C multiplied by sum (x_i - ti) for all i.

But wait, this is only true if the messages are read at x_i, and during x_i's minute, they are considered read, so they don't contribute to that minute's k. So the sum for each message is (x_i - ti) * C. Because each day from ti to x_i-1, the message is unread. If x_i is the time when it's read, then during those days, the message contributes 1 to k each day.

So the total C contribution is C * sum_{i} (x_i - ti).

So that's a crucial simplification. Instead of having to track each minute's k, which can be complicated, the total C contribution is simply C multiplied by the sum of (x_i - ti) for all messages.

But wait, what if x_i is equal to ti? Then (x_i - ti) is zero, so the message contributes nothing to the C part. Which aligns with the first sample's explanation.

So the total bank account is:

sum_{i=1 to n} [A - B*(x_i - ti)] + C * sum_{i=1 to n} (x_i - ti).

But we can combine these terms. Let's write the total as sum for each message i:

(A) - B*(x_i - ti) + C*(x_i - ti) = A + (C - B) * (x_i - ti).

So the total is sum over all messages [A + (C - B)*(x_i - ti)].

So each message's contribution is A + (C - B) * (x_i - ti), and x_i can be chosen between ti and T, inclusive.

So to maximize the total, we need to maximize the sum of (C - B) * (x_i - ti) for each message, plus the sum of A (since A is fixed per message, the sum of A is n*A, so the variable part is the sum of (C-B)*(x_i - ti).

Therefore, the problem reduces to selecting for each message i, x_i (ti <= x_i <= T) such that the sum of (C-B)*(x_i - ti) is maximized.

But this depends on the sign of (C - B).

If (C - B) is positive, then for each message, we want x_i to be as large as possible (since increasing x_i increases the term). So set x_i = T for all i. That would maximize each term.

If (C - B) is negative, then we want to minimize x_i - ti. So set x_i = ti for all i.

If (C - B) is zero, then each term contributes zero, so it doesn't matter when we read the messages; the total is fixed as n*A.

So the optimal strategy is:

- For each message i, if C > B: read it as late as possible (x_i = T) to maximize (x_i - ti).

- If C < B: read it as early as possible (x_i = ti).

- If C == B: any choice, since the terms sum to zero. So read them whenever, but the sum is fixed as n*A.

So the maximum total is sum for all messages of A + (C - B) * (x_i - ti), where x_i is T if C > B, else ti.

But wait, the C and B are per the problem's variables. So this is a key insight. The solution can be determined by checking whether C is greater than B. 

So the steps are:

1. Compute (C - B). 

   a. If (C - B) > 0: for each message, maximize (x_i - ti) → set x_i = T. Sum (C-B)*(T - ti) for all messages.

   b. If (C - B) < 0: set x_i = ti for all messages. Sum (C-B)*0 → 0. So total is n*A.

   c. If (C - B) ==0: sum 0, total is n*A.

So the maximum possible is:

sum (A) + max(0, (C - B) * sum (T - ti) for all messages).

Wait, no. Because for each message, (C-B) can be positive or not. So the sum for each message is (C-B)*(x_i - ti). For each message, if C-B is positive, x_i is T. If C-B is negative, x_i is ti. So the total is:

sum (A) + sum for each message (max( (C-B)*(T - ti), (C-B)*0 )) )

But (C-B)*(T - ti) is positive if (C-B) is positive. Because (T - ti) is >=0 (since ti <= T). So for each message, if C-B is positive, add (C-B)*(T - ti). Otherwise, add zero.

So the total is n*A + max(0, C-B) * sum_{i}(T - ti) for all i where C-B >0.

Wait, but if C-B is positive for the entire sum. So the formula simplifies to:

total = n*A + max(0, (C - B)) * sum_{i}(T - ti)

But only if (C-B) is positive. If (C-B) is negative or zero, the sum is n*A.

So the maximum total is:

n*A + max(0, (C - B)) * sum_{i=1 to n} (T - ti)

But wait, is that correct? Let's test the sample inputs.

First sample:

Input 1:

4 5 5 3 5 → C=3, B=5. So C-B = -2. So we choose x_i=ti. So total is 4*5 =20. Which matches the sample.

Second sample:

5 3 1 1 3 → C=1, B=1 → C-B=0. So sum is 5*3=15. Which matches the sample's output.

Third sample:

5 5 3 4 5 → C=4, B=3 → C-B=1. So sum of (T - ti) for ti=[1,2,3,4,5]. T is5.

So 5-1=4, 5-2=3, 5-3=2,5-4=1,5-5=0. Sum is 4+3+2+1+0=10. So (C-B)*sum is 1*10=10. So total is 5*5 +10=25+10=35, which matches the sample.

So yes, this formula works.

So the problem reduces to:

Compute the sum of (T - ti) for all messages when C > B. Otherwise, the sum is zero. Then, the total is n*A plus (C - B)*sum, if C > B.

So the steps are:

1. Read n, A, B, C, T.

2. Read the list of ti's.

3. If C > B:

   compute sum_delays = sum (T - ti) for each ti in the list.

   total = n*A + (C - B) * sum_delays

4. Else:

   total = n*A

So the code can be written as:

Read n, A, B, C, T.

Read list ti.

if C > B:

   sum_d = sum(T - ti for ti in ti_list)

   total = n * A + (C - B) * sum_d

else:

   total = n * A

print(total)

This is a very efficient solution, as it runs in O(n) time, which is acceptable for n up to 1000, even with tight constraints.

So why is this the case? Because the optimal choice is to read all messages as late as possible (if C>B) or as early as possible (if C<=B). The individual messages' ti's are irrelevant except for the sum of (T - ti) when C>B.

This approach is optimal in time and space, as no data structures are needed beyond a list to read the ti's, and a simple sum.

So the code can be written as:

Read the input, compute the sum, then apply the formula.

Now, let's test this approach against the samples.

First sample:

n=4, A=5, B=5, C=3, T=5. ti's are [1,5,5,4].

C-B= -2. So code chooses else case. Total is 4*5=20. Correct.

Second sample:

n=5, A=3, B=1, C=1. C-B=0. So else case. Total 15. Correct.

Third sample:

n=5, A=5, B=3, C=4. C-B=1. So sum of (5-1)+(5-2)+(5-3)+(5-4)+(5-5) =4+3+2+1+0=10. 5*5 +1*10=35. Correct.

So the code works for these cases.

Therefore, the optimal solution is to compute this sum and apply the formula. The code is straightforward and efficient.
</think>

```python
n, A, B, C, T = map(int, input().split())
ti = list(map(int, input().split()))
if C > B:
    total = n * A + (C - B) * sum(T - t for t in ti)
else:
    total = n * A
print(total)
```