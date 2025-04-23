<think>
Okay, let's see. The problem is that Limak needs to have strictly more votes than all other candidates. And he can steal votes by giving candies. Each candy allows him to steal one vote from another candidate. We need to find the minimum number of candies he needs to spend to achieve this.

So, the input is the number of candidates n, and the list of a1, a2, ..., an. Limak is the first candidate. Our goal is to calculate the minimum number of votes he needs to steal.

First, let's think about the approach. The steps would be:

1. Limak's initial votes are a1. The other candidates are a2 to an.
2. For each of the other candidates, we need to make sure that Limak's votes are strictly greater than theirs.
3. So, for each candidate i (i>1), after stealing some votes, Limak's total (a1 + stolen) must be > a_i' where a_i' is the remaining votes of candidate i after losing some votes (stolen by Limak or others). Wait, no. Wait, when Limak steals a vote, that vote is added to his count. So, the original votes of the other candidates decrease by the amount stolen from them. So, for example, if we steal x votes from candidate 2, then Limak's total becomes a1 + x (assuming we only steal from candidate 2 here), and candidate 2's votes are a2 - x.

But the problem allows stealing from any candidates. So the idea is to maximize the votes for Limak (a1 + total_stolen) while minimizing the number of stolen votes. However, for each other candidate, their votes (after the stolen ones) must be less than Limak's final count.

Hmm. So the process would be:

We need to determine how many votes to steal from each of the other candidates so that after adding those to Limak's initial a1, all other candidates (after losing the stolen votes) have less than Limak's total.

But since stealing votes can be from any candidates, the optimal approach is to always steal from the candidate with the highest current value (after previous steals) in each step.

Wait, perhaps a greedy approach is best here. Let's think: each time, take the current maximum of the other candidates. If Limak's current votes (a1 + stolen) is already greater than all of them, we're done. Otherwise, we need to steal votes from the current maximum. Each stolen vote from that candidate increases Limak's count by 1, and decreases that candidate's count by 1. So stealing one vote from the max would reduce their count by 1 and increase Limak's by 1. So the difference between Limak and that candidate increases by 2.

But how do we model this optimally? Because we need to do this as efficiently as possible to minimize the number of stolen votes.

Let's think step by step. Initially, Limak has a1 votes. The other candidates are a2, a3, ..., an. We can process them in some order, but the optimal way is to always steal from the current largest.

So here's an approach:

1. While there exists a candidate (other than Limak) with votes >= Limak's current votes:

   a. Find the maximum among the other candidates.

   b. Steal one vote from that candidate (so Limak's votes increase by 1, that candidate's votes decrease by 1).

   c. Increment the count of stolen votes by 1.

This loop will continue until Limak's votes are strictly greater than all others. Each iteration handles the current biggest threat.

But how to implement this efficiently, especially when n can be up to 100 and each a_i can be up to 1000. For each iteration, the maximum can be found in O(n) time, and each iteration reduces some candidate's votes by 1. But in the worst case, how many iterations would there be?

For example, in the second test case:

Original a1 is 1. Others are 8,8,8. Limak needs to get more than all. So he starts at 1. The max is 8. Each steal from the 8 (so each steal from a max candidate) gives Limak 2, and the candidate becomes 7. Then next, the max is 7 (others are 8, 8). Wait, no. Wait, let's see: initial state is 1, 8,8,8.

First, Limak's votes are 1. The other candidates are 8,8,8. Max is 8. Steal one: Limak becomes 2, the candidate becomes 7. Now, the max is 8 (the other two are still 8). So next, steal from another 8. Limak becomes 3, candidate becomes 7. Next steal the third 8. Limak becomes 4, candidate 7. Now, the max is 7. So Limak's votes are 4, which is less than 7. So next, steal from that 7. Limak becomes 5, candidate 6. Now the max is 7 (the other 7). So steal from that. Limak 6, candidate 6. Now, the max is 6 (but Limak is 6). So need to steal again. Steal from one of the 6s. Limak becomes 7, that candidate becomes 5. Now, all others are 6,6,5. Wait, but after each step, the max is 6. So Limak has 7, which is more than all. So total steps is 6 (since he started at 1 and added 6).

So the greedy approach works here. Each step, take the current maximum and steal one vote from it.

But how do we model this in code efficiently?

The problem is that for each step, we need to find the current maximum, which is O(n), and each step is O(n). If the maximum possible steps is high (like when a1 is 1 and others are 1000), then the steps needed could be (1000 -1) * (n-1), but that's 999 * 99 = 98901 steps. For each step, O(n) time. So total time is O(n * steps), which for n=100 and steps up to 1e5 would be 1e7 operations. That's acceptable for Python in 1 second, since 1e8 is about a second, but 1e7 is manageable.

But perhaps there's a smarter way. Let's think about for each candidate i>1, how many votes we need to steal from them so that after stealing, a_i - stolen_i < (a1 + total_stolen).

But the total_stolen is the sum of stolen_i for all i>1.

So, for each candidate i>1, we have:

stolen_i >= a_i - (a1 + total_stolen) + 1.

Wait, because (a1 + total_stolen) must be > (a_i - stolen_i). Rearranged:

a1 + sum(stolen_j) > a_i - stolen_i

=> a1 + sum(stolen_j) + stolen_i > a_i

But sum(stolen_j) + stolen_i = sum of all stolen votes (since stolen_i is part of the sum). Let total = sum(stolen_j) for j>1.

Wait, no. Let total_stolen = sum of all stolen votes. So total_stolen is the sum of stolen_2, stolen_3, ..., stolen_n. So Limak's votes are a1 + total_stolen.

For each candidate i>1:

a1 + total_stolen > (a_i - stolen_i)

So, a_i - stolen_i < a1 + total_stolen.

But stolen_i is the number of votes stolen from candidate i.

We need to find all stolen_i >=0 such that for each i>1:

stolen_i >= a_i - (a1 + total_stolen) + 1.

But this seems circular because total_stolen is the sum of all stolen_i. So this is a system of inequalities.

But perhaps there's a way to model this. Let's denote that for each i>1:

stolen_i >= max(0, a_i - (a1 + total_stolen) + 1)

But total_stolen is sum(stolen_j). So this is a system of equations.

Alternatively, let's think for each candidate i>1, how many votes need to be stolen from them. The required is that after stealing, their votes are <= limak's votes - 1.

So, for each i>1:

a_i - stolen_i <= limak_votes -1

But limak_votes = a1 + total_stolen.

So substituting:

a_i - stolen_i <= a1 + total_stolen -1

=> stolen_i >= a_i - (a1 + total_stolen -1)

But stolen_i must be >=0.

But this again includes the total_stolen in the equation, which is the sum of stolen_i.

This seems a bit tricky. Maybe the greedy approach is the way to go.

Alternatively, for each candidate i>1, the maximum possible a_i - stolen_i is a_i - x_i (x_i is stolen from i). So for each i>1, we need:

a_i - x_i < a1 + sum(x_j for j>1)

We need to find x_j >=0 such that this inequality holds for all i>1, and sum(x_j) is minimized.

Hmm. So for each i>1, x_i can be as low as possible. Let's consider that for each i>1, the minimum x_i is max(0, a_i - (a1 + sum(x_j) ) +1 )

But sum(x_j) is part of the equation. So this is interdependent.

Alternatively, perhaps we can model this as follows. Let's arrange the candidates in a certain order. For example, process the candidates in order of decreasing a_i. Let's say we process them in the order of candidates from highest a_i to lowest.

But even then, it's not straightforward. Let's think of the example where there are two candidates. Limak's a1 is 7, other is 6. So he doesn't need to steal any votes. Because 7 >6.

Another example: a1 is 5, others are 1, 11, 2, 8. So the initial maximum is 11. We need to steal until Limak's votes are greater than 11.

So, Limak starts at 5. The other candidate has 11. So he needs to get 12 votes. So he needs to steal 7 votes. But stealing from the 11: each steal gives Limak +1 and the other -1. So each steal reduces the required votes by 2. Wait, no. Let's see: current Limak is 5, other is 11. The difference is 6. To reach Limak > 11, he needs to be at least 12. So the required difference is 7 (12 -5=7). But each steal gives a +1 to Limak and -1 to the other. So each steal reduces the gap by 2. So 7/2 is 3.5, so 4 steals. Which is the sample's answer.

So for each candidate, the required number of steals is (a_i - a1 - sum_other_steals +1 +1) / 2? Not sure.

Alternatively, perhaps for each candidate i>1, the minimal x_i (stolen from i) is (a_i - (a1 + sum_x) + x_i +1). Wait, this is getting complicated.

Alternatively, let's model the problem as follows: the minimal total x (sum of x_i) such that for each i>1:

a1 + x >= a_i - x_i +1

Rearranged:

x_i + x >= a_i - a1 +1 - x_i ?

Wait, no. Let me think again. We need a1 + x (total stolen) > a_i - x_i. Because x_i is the number stolen from candidate i, which reduces their votes by x_i, and adds x_i to Limak's total. Wait, no: when you steal x_i votes from candidate i, that adds x_i to Limak's votes. So Limak's votes are a1 + sum(x_j). The votes of candidate i are a_i - x_i.

So the condition is:

a1 + sum(x_j) > a_i - x_i

for all i>1.

So for each i>1:

sum(x_j) + x_i > a_i - a1 - sum(x_j) + sum(x_j) ?

Wait, no. Let's rearrange the inequality:

a1 + sum(x_j) > (a_i - x_i)

sum(x_j) here is the sum of all x_j, including x_i. So sum(x_j) = x_2 + x_3 + ... + x_n.

So the inequality is:

a1 + sum(x_j) > a_i - x_i

We can rearrange this as:

sum(x_j) + x_i > a_i - a1

But sum(x_j) is the sum of all x_j. So sum(x_j) + x_i = sum(x_j) + x_i (since x_i is part of sum(x_j)). Wait, no. sum(x_j) includes x_i. So sum(x_j) = x_2 + ... + x_i + ... +x_n. So sum(x_j) + x_i is x_2 + ... + x_i + ... +x_n + x_i. Which is sum(x_j) + x_i. That's not correct. Wait, perhaps I made a mistake in rearrangement.

Wait, the original inequality is:

a1 + sum(x_j) > a_i - x_i.

Let's subtract a1 from both sides:

sum(x_j) > (a_i - x_i) - a1.

But sum(x_j) is the total stolen votes. So, for each i>1, the condition is sum(x_j) + a1 > (a_i - x_i).

Alternatively, sum(x_j) + x_i > a_i - a1.

Because sum(x_j) + x_i is the total sum plus x_i again. Wait, that's not correct. Because sum(x_j) already includes x_i.

Hmm, perhaps this approach isn't leading me anywhere.

Let me think again. The problem is to find the minimal sum of x_i, such that for each i>1:

a1 + sum(x_j) > (a_i - x_i).

We can rearrange this as:

sum(x_j) + x_i > (a_i - a1).

Because sum(x_j) is the total sum. So sum(x_j) + x_i is sum(x_1, x_2, ..., x_n) + x_i. Wait, no. Because sum(x_j) is x_2 + x_3 + ... + x_n. So sum(x_j) + x_i is sum(x_2 ... x_n) + x_i. Which is x_i plus the sum of all x_j except x_i. So that's equal to sum(x_j) + x_i = sum(x_j) + x_i, but sum(x_j) includes x_i. Wait, no. If sum(x_j) is the sum of all x_j (i>1), then sum(x_j) is x_2 + x_3 + ... + x_n. So adding x_i (which is part of that sum) gives x_2 + ... + x_i + ... + x_n + x_i = sum(x_j) + x_i. Which is sum(x_j) = x_2 + ... + x_n. Then sum(x_j) + x_i is x_2 + ... + x_i + ... + x_n + x_i.

Wait, this is confusing.

Alternatively, perhaps the problem can be modeled by considering each candidate i>1. We can find the minimal number of votes that need to be stolen from them and others such that after stealing, their votes are <= (a1 + total_stolen) - 1.

But how?

Alternative approach: let's imagine that we can process each candidate i>1, and compute the minimal number of votes needed to be stolen from them. But the problem is that stealing from one candidate affects the required steals from others.

But perhaps the optimal way is to greedily steal votes from the largest candidate first. Because each vote stolen from the largest candidate reduces their count and increases Limak's, which could potentially make other candidates' required steals less.

So, here's an algorithm:

1. Create a max heap of the other candidates' votes.

2. While Limak's votes (initial a1 + stolen) is not greater than the max in the heap:

   a. Take the maximum element (current_max) from the heap.

   b. Steal one vote: increment stolen count by 1.

   c. Add current_max - 1 back into the heap (since the candidate's votes are now current_max -1).

   d. Limak's votes are now a1 + stolen.

3. Once the heap's maximum is less than Limak's votes, return the stolen count.

This approach is greedy and should work. Because each time, we steal from the current largest candidate, which is the one that requires immediate attention.

Let's test this approach against the sample inputs.

Sample 1:

n=5, a1=5, others [1, 11, 2, 8]

Initial heap is [11,8,2,1]. Max is 11.

Limak's votes are 5. 5 <=11. So steal one.

Stolen becomes 1. Limak is 6. Heap now has 10,8,2,1.

6 <=10. Steal again. Stolen 2. Limak 7. Heap 9,8,2,1.

7 <=9. Steal. Stolen 3. Limak 8. Heap 8,8,2,1.

Now, max is 8. Limak's votes is 8. So 8 is not greater than 8. Need to steal again.

Stolen 4. Limak 9. Heap 8,7,2,1. Now, the max is 8. 9>8. So we're done.

So stolen count is 4. Which matches the sample.

Sample 2:

n=4, a1=1, others [8,8,8]. Initial heap [8,8,8]. Limak's votes is 1.

Steal from 8. Each steal reduces it by 1, increases stolen by 1. Let's see:

Stolen count increments each time.

After 6 steals:

Limak's votes are 1+6=7. The heap would have 6,6,6. So 7>6, so done.

Which matches the sample.

Third sample:

a1=7, a2=6. Initial max is 6. 7>6, so no steals needed. Correct.

So the algorithm works for these samples.

Now, how to implement this efficiently in Python.

In Python, a max heap can be implemented using the heapq module, which is a min-heap, but we can invert the values.

So for each candidate i>1, we push -a_i into the heap, so that the smallest (most negative) corresponds to the largest a_i.

Then, each step:

- pop the smallest (most negative) which is the largest a_i.

- check if Limak's current votes (a1 + stolen) > (-current_max).

If not, then steal one vote: increment stolen by 1, and push (current_max +1) (since the candidate's a_i is now (current_max +1 -1?) Wait, no. Wait, the stored value is negative. Let's think again.

Original a_i is 8. We stored -8 in the heap. When we pop it, we get -8, which is the max. Then, after stealing one vote, the new a_i is 8-1=7. So we push -7 into the heap.

So the steps:

current_max = -heapq.heappop(heap)

if current_max >= limak_votes (a1 + stolen):

   we need to steal. stolen +=1. limak_votes +=1.

   new_value = current_max -1

   heapq.heappush(heap, -new_value)

Else:

   break.

Wait, no. Because the condition is: limak_votes (a1 + stolen) must be > current_max. So:

While the current_max (the current maximum in the heap) >= limak_votes:

   steal.

So in code:

limak_votes = a1

stolen =0

heap = ... (other candidates as negatives)

heapq.heapify(heap)

while True:

   if not heap:

       break  # no other candidates, no need.

   current_max = -heap[0]  # peek the maximum

   if limak_votes > current_max:

       break

   # else, steal one

   stolen +=1

   limak_votes +=1

   # update the max in the heap

   popped = -heapq.heappop(heap)

   popped -=1  # stolen one vote

   heapq.heappush(heap, -popped)

So the loop continues until the max in the heap is less than limak_votes.

Each iteration, we steal one vote from the current maximum.

This approach is correct and efficient.

In terms of time complexity: each steal operation is O(log k) time, where k is the number of other candidates. Since k is up to 99 (since n is up to 100), each heap operation is O(log 99) which is negligible. The number of steals can be up to (max_ai - a1) * (n-1). For example, if a1 is 1, and other candidates have 1000 votes each, then each candidate would need (1000 -1) steals. For 99 candidates, that's 99 * 999 = 98901 steals. Each steal takes O(log 99) time. So total steps are around 1e5 * 7 (since log2(99) is ~7) which is 7e5 operations, which is acceptable.

So this approach is efficient enough.

Now, let's code this.

First, read input:

n = int(input())

a = list(map(int, input().split()))

a1 = a[0]

others = a[1:]

if len(others) ==0:

   # but problem says n>=2. So no need.

We need to handle the case where others is empty. But the constraints say n>=2.

So create a max heap (using min-heap with negatives).

heap = [-x for x in others]

heapq.heapify(heap)

stolen =0

limak_votes = a1

while heap:

   current_max = -heap[0]  # peek

   if limak_votes > current_max:

       break

   # steal one

   stolen +=1

   limak_votes +=1

   # remove the max, subtract 1, add back

   max_val = -heapq.heappop(heap)

   max_val -=1

   heapq.heappush(heap, -max_val)

print(stolen)

Yes, this code should work.

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    a1 = a[0]
    others = a[1:]

    heap = [-x for x in others]
    heapq.heapify(heap)

    stolen = 0
    limak_votes = a1

    while heap:
        current_max = -heap[0]
        if limak_votes > current_max:
            break
        stolen += 1
        limak_votes += 1
        max_val = -heapq.heappop(heap)
        max_val -= 1
        heapq.heappush(heap, -max_val)

    print(stolen, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 8 8 8
""",
            "output": \
"""\
6
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
import heapq

n = int(input())
a = list(map(int, input().split()))
a1 = a[0]
others = a[1:]

heap = [-x for x in others]
heapq.heapify(heap)

stolen = 0
limak_votes = a1

while heap:
    current_max = -heap[0]
    if limak_votes > current_max:
        break
    stolen += 1
    limak_votes += 1
    max_val = -heapq.heappop(heap)
    max_val -= 1
    heapq.heappush(heap, -max_val)

print(stolen)
```
