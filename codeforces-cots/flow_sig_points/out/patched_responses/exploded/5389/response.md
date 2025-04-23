<think>
Okay, let's tackle this problem. So, the task is to find the minimum time Vasya needs to wait when choosing a cashier. Let's see how to approach this.

Hmm, each cashier has a queue of people. Vasya is going to join one of these queues. So for each cashier, we need to calculate the total time it takes until Vasya is done. Then pick the minimum among all cashiers.

Wait, right. So for each cashier i, the total time is the sum of the time taken by all people already in the queue, plus the time Vasya takes once he's added to the end. Because he's the last person in the queue after joining.

Let me break it down. For each cashier, there are k_i people already in the queue. Each of these people contributes their items * 5 seconds (for scanning) plus 15 seconds (the per-person handling time). Then, Vasya's own items contribute 5*mi_vasya (but wait, wait, in the problem statement, Vasya's items are not given. Oh wait, no. Wait, the problem says that he is adding himself to the queue. So when he chooses a cashier, he is the new last person in that queue. So the existing queue is the k_i people, and Vasya is the k_i+1-th person. Wait, no. Wait, the problem says that the cashier's queue already has ki people. Then Vasya joins the end of the queue, so he's after all of them. So the total time is the sum of the time for all existing people, plus his own time.

So for each cashier, calculate the sum for each existing person's (items *5 +15) seconds. Then add Vasya's items *5 +15. Wait, but wait, the 15 seconds per customer is the time after scanning all their items. So each person's processing is (items *5) +15. So for each cashier's current queue, the total time is sum over all (m_ij *5 +15) for each existing customer. Then Vasya adds his own m_vasya *5 +15. So the total time for that cashier is sum_existing + (m_vasya *5 +15). Wait, but wait, the problem says that the input gives the current queues. So Vasya's own items aren't part of the input. Wait, no. Wait, looking at the problem statement again. Oh, wait! Oh right, the problem statement says that the j-th person in the queue has m_ij items. Vasya's items are not given here. Wait, that's confusing. Wait, the problem says that Vasya is choosing a queue. So he's adding himself to the end of the queue. But his own items are part of the calculation. Wait, but the input doesn't include his items. Wait, looking back at the problem statement:

Wait, the problem says:

Help him write a program that displays the minimum number of seconds after which Vasya can get to one of the cashiers.

Wait, but how much items does Vasya have? The problem statement says nothing about that. That's a problem. Wait, maybe I misread.

Wait, the problem's input is:

The first line is n. Second line has k_1, ... k_n. Then for each cashier, we have k_i numbers: the m_i,j for each person in the queue.

Wait, but Vasya is adding himself to the queue. So the existing queues are the given ones. When he joins a cashier, he is adding himself to the end of that queue. So the total time for that cashier is the sum of the existing people's time plus his own time.

But the problem's input doesn't specify Vasya's m. Oh, wait, that's impossible. Wait, no. Let's re-examine the problem statement.

Wait, in the first example input:

1

1

1

The output is 20. Let's see: the cashier has 1 person with 1 item. Then Vasya adds himself. Wait, but the output is 20. Let's compute. The existing person's time is 1*5 +15 =20. Then Vasya's time is ... but wait, the output is 20. That implies that the total time is the existing sum plus Vasya's time. Wait, but in the first example, the output is 20. Wait, that's the time when Vasya joins the queue. Oh, wait no. Wait, the output is the time after which Vasya can get to the cashier. So the time until the cashier finishes processing all previous people, then processes Vasya. So the existing queue is processed first, then Vasya's own processing.

So, the total time for a cashier is the sum of all existing customers' (m*5 +15) plus (Vasya's m *5 +15). But wait, the first example has:

Cashier 1 has 1 person with 1 item. So existing sum is 1*5 +15 =20. Then Vasya adds himself. So his items must be 1? But how? Because in the first example, the input gives for the cashier's queue the 1 person with 1 item. The output is 20. But according to the calculation, if Vasya's items are 1, then sum is 20 (existing) + 1*5+15= 20+20=40. But the sample output is 20. So that's impossible.

Wait, this is confusing. Let me re-examine the first sample.

Sample Input 1:

1

1

1

Sample Output:20.

So according to the explanation in the note, the first sample must be when Vasya is the first in the queue. Wait, but according to the input, the queue already has 1 person. Then he adds himself. Wait, that's impossible. Wait, maybe I'm misunderstanding the problem.

Ah! Oh! Wait, perhaps I have the problem wrong. Maybe Vasya is not adding himself to the queue. Maybe he can choose to go to any cashier, and the cashier's queue is the existing queue, and he is served after all the existing people. So the time is the sum of all existing people's processing times, plus his own. But the problem's note says in the first example, the output is 20.

Wait, in the first example's note, when Vasya chooses the first queue (the only one), he gets to the cashier in 100*5 +15=515 seconds. So that implies that the existing queue is 1 person (since the input has k1=1), and that person's m is 100. So the sum for existing people is 100*5 +15=515. Then Vasya's own time is 0? No, that can't be. Or maybe the problem statement is different. Wait, perhaps the problem is that the cashiers' queues are the ones given, and Vasya is the next person in the queue. So he is added to the queue, and the time is the sum of all people's processing times (including his own). Wait, but in the first sample, the existing queue is 1 person with 1 item. So the time is (1*5 +15) + (Vasya's items *5 +15). But the sample output is 20. So that would mean that Vasya's items are zero? That can't be. So I'm clearly misunderstanding the problem.

Wait, perhaps the problem statement is that Vasya is choosing a cashier, and the existing queue is as given. The time is the time until the cashier finishes all people in the queue, and then Vasya. But how much items does Vasya have? The problem statement doesn't mention that. This is a critical error in understanding.

Wait, looking back at the problem statement:

The j-th person in the queue for the i-th cash has mi,j items. Vasya wants to choose a cashier such that he can be processed as soon as possible.

But wait, Vasya is not part of the queue. So when he chooses a cashier, he joins the queue as the next person. But the problem's input includes all the existing people in the queue. So when he chooses a cashier, he becomes the (ki +1)-th person in that queue.

But then, the problem's input must include the data for each existing person, but not Vasya's. So how is Vasya's items determined?

Wait, this is a problem. The problem statement says nothing about Vasya's own items. So perhaps the problem is written incorrectly. Alternatively, perhaps there's a misunderstanding. Let's re-examine the problem statement.

The problem's note says:

In the first sample, if Vasya goes to the first queue, he gets to the cashier in 100·5 +15 = 515 seconds. Wait, the first sample's input is:

1

1

1

So according to this, the cashier's queue has 1 person with 1 item. Then, according to the note, the time is 100*5 +15. Wait, that's 515. But how does that match the input?

Ah, wait, maybe the problem statement has a mistake. Or perhaps the note is for a different example. Let me check the sample input.

Wait, the second sample input is:

4

1 4 3 2

100

1 2 2 3

1 9 1

7 8

The output is 100.

In the note, when he chooses the second queue, the calculation is 1·5 + 2·5 + 2·5 +3·5 (which sums to (1+2+2+3)*5 =8*5=40) plus 4*15 (since there are 4 existing people, then Vasya adds himself as the 5th). So the 4 existing people contribute 4*15, plus their items*5. Wait, no. Wait, each person in the existing queue contributes (items*5 +15). Then Vasya's own time is (his items *5 +15). But the note says that for the second queue, the existing queue has 4 people. So sum is 1*5+15 + 2*5+15 + 2*5+15 +3*5+15 = (5+30) + (10+15) + (10+15) + (15+15). Wait, maybe not. Let's compute the sum for the existing 4 people in the second queue:

Each person's time is m_i *5 + 15. So for the four people in the second queue's input (1,2,2,3):

Sum = (1*5 +15) + (2*5 +15) + (2*5 +15) + (3*5 +15) 

= (5+15)+(10+15)+(10+15)+(15+15)

= 20 +25 +25 +30 = 100.

Then Vasya's time is his items *5 +15. But according to the note, the total is 100 seconds. So 100 + (Vasya's items *5 +15) = 100. Which would require Vasya's items to be negative, which is impossible. Therefore, this approach must be incorrect.

Hmm, this suggests that my understanding of the problem is wrong. Let me read the problem statement again.

The problem says:

Vasya wants to select a queue so that he can leave as soon as possible. The time is the time after which he can get to the cashier.

Ah! Oh! Wait, perhaps the cashier is processing the existing queue, and Vasya is waiting until the cashier is free. So the time is the sum of all existing customers' processing times, plus the time to process Vasya. But Vasya's own processing time is his items*5 +15. But the problem does not mention how many items Vasya has. So this is a problem. Unless, perhaps, the problem assumes that Vasya has zero items, which makes no sense. Alternatively, maybe the problem statement has a mistake, and the input includes Vasya's items as the last in each queue.

Wait, no. Let's recheck the problem statement's input.

The input gives for each cashier:

The ki numbers for the people in the queue.

So, in the first example, the queue has 1 person with 1 item. So the existing queue's processing time is 1*5 +15 =20. Then Vasya adds himself to the queue. So the total time is 20 (existing) plus his own items' processing. But in the sample output, the answer is 20. So this suggests that the existing queue's processing time plus his own time equals 20. But how?

Wait, maybe the problem is that Vasya is not added to the queue. He chooses which cashier to go to, and the cashier is currently processing the existing queue. So the time is the time until the cashier finishes the existing queue. Then, Vasya can approach the cashier. But that would make no sense. Because then he would have to wait until the cashier is done, but then he can be processed. But the problem says he must wait until the cashier processes all existing customers, and then process himself.

So the time is the sum of the existing queue's processing time, plus his own processing time.

But in the first sample, the output is 20. So sum existing (1*5 +15=20) plus his own time (m*5+15) must be 20. So 20 + (5m +15) =20 => m must be -3. Which is impossible.

Therefore, there must be a misunderstanding.

Wait, perhaps the cashier's processing time for a customer is (items *5) +15, and Vasya is the next customer. So for each cashier, the time is the sum of all existing customers' processing time plus his own processing time.

But then the first sample's input must have the answer 20 + (Vasya's processing time). But the output is 20, which would imply that Vasya's processing time is zero. Which again, doesn't make sense.

Wait, maybe I'm misunderstanding the problem. Let's read the problem statement again.

Problem statement:

Each cashier needs 5 seconds per item, and after scanning each item of a customer, he needs 15 seconds to take the money and give change.

Ah! So per customer, the processing time is (number of items)*5 +15 seconds. So each customer's processing time is (mi_j *5) +15.

The cashiers process each customer in their queue one by one. When Vasya chooses a cashier, he is added to the end of the queue. So the time he has to wait is the sum of all processing times of the customers before him (the existing ones) plus his own processing time.

But how many items does Vasya have? The problem statement does not mention this. Wait, this must be a mistake in the problem statement. But the sample input and output suggests that Vasya's items are not part of the input. For example, in the first sample, the cashier has 1 person with 1 item. The answer is 20. That would mean that the sum of existing processing times (1*5 +15=20) plus Vasya's processing time (0*5+15=15) would be 35. But the output is 20. So that's impossible.

So this indicates that perhaps the problem statement is different. Oh! Wait, perhaps the problem is that Vasya is going to choose a cashier and immediately go to the cashier (without adding to the queue). But that's not possible. Alternatively, perhaps the cashier can process Vasya first, ignoring the existing queue. Which is not the case.

Alternatively, perhaps the problem statement is that the existing queue is processed first, and Vasya's processing time is zero. But that's impossible.

Wait, perhaps the problem statement is that Vasya is replacing the entire queue. But that's not indicated.

Alternatively, perhaps the problem is that the cashier's queue is empty, and the given queues are not the existing ones. But that's contradicted by the sample.

Wait, perhaps the problem statement is written incorrectly, and the actual problem is that Vasya is a customer in the queue. For example, the queues given are including him, but he can choose any cashier and his position in the queue. But that also doesn't make sense.

Alternatively, perhaps the problem statement is that the queues given are the ones after Vasya has joined. But that's also not supported by the sample input.

Wait, the first sample's input is:

1 cashier.

Cashier's queue has 1 person with 1 item.

The output is 20. So the total time must be 20. Which is exactly the time for the existing queue. So that implies that Vasya's processing time is zero. But that's impossible.

This suggests that the problem statement is missing a key piece of information: the number of items Vasya has. But there's no mention of that in the input.

Alternatively, perhaps the problem is that the cashier's queue is processed in parallel. Like, the cashier can process all customers in parallel, but that's not indicated.

Wait, perhaps the problem is that the cashier's time is the sum of the items in the queue multiplied by 5, plus 15 multiplied by the number of customers (including Vasya). So for each cashier i, the time is (sum of all m_ij for j=1..k_i +1) *5 + (k_i +1)*15. But where does the '+1' come from? Because Vasya is added as a new customer.

But then, in the first sample:

sum of m_ij is 1 (existing) +0 (Vasya's items?), but that would give 1*5 + (1+1)*15=5 +30=35. Not 20.

No.

Alternatively, maybe the problem is that Vasya's items are 0. So for each cashier, the total time is sum of existing (m_ij *5 +15) + (0*5 +15) = sum +15. But in the first sample, sum is 1*5+15=20, plus 15=35. Not 20.

So that can't be.

Alternatively, maybe the problem is that the cashier's queue includes Vasya. So the input lines for each cashier's queue include Vasya's items, but he can choose to join any cashier. But that's not possible, because the input is given once.

Alternatively, maybe the problem is that Vasya is choosing a cashier, and the cashier's queue is the given one, and he is served after all of them. But the problem statement does not provide the number of items that Vasya has. So how is this possible?

This is a critical problem. Without knowing Vasya's items, we can't compute his processing time. So the problem must have a mistake in the description, or the problem has a different interpretation.

Looking back at the sample input:

First sample:

Input:

1

1

1

The output is 20. So the time is 20.

Which is 1*5 +15 =20. So this suggests that the time is just the existing queue's time. But where is Vasya's time?

Ah! Maybe the problem is that the cashier processes the existing queue, and then Vasya can proceed immediately. But that would mean that Vasya's time is zero. But that's not possible.

Alternatively, perhaps Vasya's items are considered to be zero. Then the sum would be 20 (existing) +0*5 +15=35. But sample output is 20.

So there's a contradiction here.

Wait, perhaps the problem statement is that the cashier can process all items in the queue, including Vasya's, but the input's queues are the queues after Vasya has joined. But that's not possible, as the sample input shows.

Alternatively, perhaps the problem statement's note is incorrect, but that's unlikely.

Wait, let's look at the note in the second sample:

If he chooses the second queue, he will need 1·5 + 2·5 + 2·5 +3·5 +4·15 = 100 seconds.

Wait, the sum of the items is 1+2+2+3=8, multiplied by 5 is 40. 4·15 is 60. Total 100. So (sum of items)*5 + (number of customers)*15.

Ah! So each customer's processing is items*5 +15. So for the existing queue, the sum is (sum of items) *5 + (number of existing customers) *15. Then adding Vasya's items (m) *5 +15. So the total is (sum_existing + m)*5 + (k_i +1)*15.

But where does Vasya's items come from? The problem's input does not include them. So this suggests that there's a mistake in the problem statement.

Wait, but looking back at the note in the second sample:

If Vasya chooses the first queue (which has 1 person with 100 items), the time is 100*5 +15 = 515. Which is (sum of existing items (100) *5) + (1 customer *15) + (Vasya's items *5 +15). But in the sample output, the answer is 100. So the second queue's time is 100. So according to the note, the second queue's sum is 1+2+2+3 =8 items. 8*5=40, plus 4 existing customers *15=60. 40+60=100. Then Vasya's items contribute 0*5 +15. But that would make total 100+15=115, but the note says the answer is 100. So this can't be.

Alternatively, the note says that when he chooses the second queue, the time is 100. But according to the calculation, the existing queue's sum is 1+2+2+3=8 items. So 8*5=40, plus 4 customers *15=60. Total 100. So why is that the total time? That would imply that Vasya's items are zero and that he's not part of the queue. So the time is the sum of the existing queue's processing time. But then why would he be able to go to the cashier once the existing queue is processed?

This suggests that the problem is not requiring Vasya to wait for his own processing. But that contradicts the problem statement.

Alternatively, perhaps the problem is that Vasya's time is just the sum of the existing queue's processing time, and he is not part of the queue. So he can go to the cashier immediately after the existing queue is processed. But then why is the time sum of existing queue's processing time? Because that's when the cashier becomes available. But then the problem is to find the earliest time when a cashier becomes available. But that's different from the problem statement.

In this case, the problem would be to compute for each cashier, the sum of (m_ij *5 +15) for all j in 1..k_i. Then choose the minimum of these sums. But in the first sample, the sum is 1*5 +15=20. Which matches the sample output. In the second sample's note, the first cashier's sum is 100*5 +15=515, which is the sum of the existing queue. The second cashier's sum is 1*5 +2*5 +2*5 +3*5 +4*15= 5+10+10+15 +60= 100. Which matches the sample output.

So perhaps the problem statement is that Vasya is not part of the queue, but he can choose a cashier that becomes available the earliest. The cashier's processing time for their existing queue is the sum of (m_ij *5 +15) for each customer. The minimum of these sums is the answer. But then, how does that make sense? Because after the existing queue is processed, the cashier is free, and Vasya can go to him. So he would not need to wait for any processing of himself. But that doesn't make sense, because he must have some items to process.

But according to the sample input, that's the case. The first sample's output is 20, which is exactly the sum of the existing queue. The second sample's output is 100, which is the sum of the second cashier's existing queue.

So the conclusion is that the problem statement is incorrect. The correct approach is to compute for each cashier the sum of (m_ij *5 + 15) for all existing customers, and choose the minimum of these sums. Vasya's own processing time is not considered, which contradicts the problem statement.

Alternatively, perhaps the problem statement intended that Vasya's own items are zero. So for each cashier, the time is sum of existing processing times plus (0 *5 +15) =15. But in the first sample, 20 +15=35, which doesn't match the output of 20.

So this is not possible.

Another possibility is that the problem's note in the second sample is wrong. But that's unlikely.

Wait, the note in the second sample says that when he chooses the second queue, the time is 100. Which is the sum of the existing queue's processing times. So the note's calculation is 1·5 +2·5 +2·5 +3·5 +4·15 = 100. But 4·15 is 60. The sum of the items is 1+2+2+3=8. 8*5 is 40. 40 +60=100. So the sum is for the existing queue. So Vasya's own items are not part of the calculation. So the problem is, perhaps, that the cashier's existing queue is processed, and Vasya can use the cashier immediately after. So the time is the sum of the existing queue's processing time. Which would make the problem to compute for each cashier the sum of (m_ij *5 +15) for their existing customers, then take the minimum.

But in that case, the problem statement is wrong. Because the note in the first sample says that the output is 20, which is indeed the sum of the existing queue.

So perhaps the problem statement is incorrect, and the actual task is to compute the sum of the existing queue's processing times for each cashier, and output the minimum. Then Vasya's own processing time is not considered. But why would the problem's note in the second sample mention the 4·15 as part of the sum? Because that's the number of existing customers.

But then why would the problem's sample input 2's output be 100, which is the sum of the second cashier's existing queue's processing time (sum is 1+2+2+3=8 items, 8*5=40, 4*15=60, total 100). So according to this approach, the correct answer is indeed 100.

So this suggests that the problem is not requiring Vasya to add himself to the queue. But how? That contradicts the problem statement.

Alternatively, perhaps the problem statement is written in a way that the queues given are after Vasya has joined. So, for example, the first sample's input is:

n=1.

k1=1.

That queue has 1 person, which is Vasya. So his processing time is 1*5 +15=20. Which explains the sample output. But how would the input indicate that?

In that case, the problem's input is the queues after Vasya has joined. But that's not how the problem is described.

Alternatively, perhaps the problem statement is wrong, and the correct approach is to compute for each cashier the sum of (m_ij *5 +15) for their existing customers, and select the minimum. So, the code would be: for each cashier, calculate the sum of (each customer's items *5 +15), then choose the minimum sum.

Let's see if that works for the samples.

First sample:

Cashier 1 has 1 customer with 1 item. Sum is 1*5+15=20. Output 20. Correct.

Second sample:

Cashier 1: 1 customer with 100. Sum is 100*5 +15= 515.

Cashier 2: 4 customers with 1,2,2,3. Sum is (1*5+15) + (2*5+15) + (2*5+15) + (3*5+15) = 20 +25 +25 +30 = 100.

Cashier 3: 3 customers with 1,9,1. Sum is (1*5+15)+(9*5+15)+(1*5+15)=20+60+20=100.

Cashier4:2 customers with7 and8. Sum is7*5+15 +8*5+15=35+15+40+15= 105. So minimum is 100. Correct.

So this approach gives the correct answers for the samples.

But according to the problem statement, Vasya is choosing a queue (adding himself to the end of it), and the time is until he is processed. So his processing time should be added. But according to the samples, that's not the case.

This suggests that the problem statement has a mistake. So the correct approach is to compute the sum of the existing queues' processing times, and choose the minimum. Which is what the samples indicate.

So the problem's actual requirement is to compute, for each cashier, the sum of (m_ij *5 +15) for all existing customers in the queue, and choose the minimum among these sums.

But how to reconcile this with the problem statement?

The problem statement says:

"the cashier needs 5 seconds to scan one item; after the cashier scans each item of some customer, he needs 15 seconds to take the customer's money and give him the change."

So for each customer, it's 5 * items +15 seconds. So the total processing time for a queue is sum of each customer's processing time.

The problem says that Vasya wants to choose a queue so that he can get to the cashier as soon as possible. So the time when the cashier becomes available (after processing the existing queue) is the answer. Because Vasya can go to the cashier once it's free. But in that case, his own processing time is not considered. Which doesn't make sense. Because he needs to be processed.

So this is confusing. But according to the samples, the correct approach is to compute the sum of the existing queue's processing times. So the problem statement may have an error, but the intended solution is to compute that sum.

So the code should process each cashier's queue, calculate the sum of (m *5 +15) for each person in the queue, then output the minimum of those sums.

So the code will be:

Read n.

Read the list of k_i for each cashier.

For each cashier:

   Read k_i integers m_ij.

   sum_time = sum( m *5 +15 for m in m_ij )

find the minimum sum_time among all cashiers.

Output that minimum.

This matches the samples.

So the problem statement's description must be incorrect, and the correct approach is to compute the sum of the existing queue's processing times. So the code is straightforward.

So the code would be:

Read n.

Read list k.

For each of the n cashiers:

   read list m_list (length k_i).

   compute sum(5*m +15 for m in m_list).

Find the minimum sum.

Print it.

Yes. Let's test this against the samples.

First sample:

n=1, k=[1], then cashier's m_list is [1].

sum is 5*1 +15 =20. Output 20. Correct.

Second sample:

n=4, k = [1,4,3,2].

Cashier 1: m_list [100]. sum is 5*100+15=515.

Cashier2: m_list [1,2,2,3]. sum is (1*5+15) + (2*5+15) + (2*5+15) + (3*5+15) → 20+25+25+30=100.

Cashier3: m_list [1,9,1]. sum is (5+15)+(45+15)+(5+15) → 20+60+20=100.

Cashier4: [7,8]. sum is (35+15)+(40+15)=50+55=105.

The minimum is 100. Correct.

So the code is correct.

Thus, the problem statement must have an error, and the correct approach is to compute the sum of the processing times of each cashier's existing queue. The code is simple.
</think>

```python
n = int(input())
k_list = list(map(int, input().split()))
min_time = float('inf')

for i in range(n):
    m = list(map(int, input().split()))
    total = sum(5 * x + 15 for x in m)
    if total < min_time:
        min_time = total

print(min_time)
```