<think>
Okay, let's see. I need to solve this problem where I have to track the changes in citizens' money after a series of events. The events can be either a receipt that directly sets a person's money to a value, or a payout that brings all people below a certain x up to x. The challenge is to process these events efficiently given the constraints of up to 2e5 events and 2e5 citizens. Processing each payout by iterating through all citizens every time would be O(n) per payout, which is way too slow for 2e5 events. So we need a smarter approach.

Hmm. So the key is to handle the payout events efficiently. Let's think about how payouts affect the current state. Each payout with x sets all elements less than x to x. But if there's a subsequent payout with a higher x, that might override previous ones. So maybe we can track the maximum x value from all payout operations. Because once there's a payout with a higher x than previous ones, those previous payouts are irrelevant for the people who were raised to that higher x.

Wait, but receipts can interfere with this. For example, if a person has a receipt after a payout, their value is set to x, but then subsequent payouts would affect them again if their value is lower. So we need to track for each individual whether they've been modified by a receipt after the latest payout that would have affected them.

So here's the idea: we can track two things. First, the current maximum payout value (let's call it base). Then, for each individual, we track their last receipt's value and the time (or the base at the time of the receipt). Wait, maybe not exactly time, but whether their last operation was a receipt that came after the last payout. For example, if a person's last update was a receipt, then their value is fixed unless a subsequent payout has a higher x than that receipt's value. Otherwise, if their last update was a payout, then their current value is the maximum between their original value (after all receipts) and the base.

Wait, perhaps not. Let me think again. Let's model each person's current value as the maximum between their last receipt's x and the current base. Wait, no. Because each payout sets their value to x if their current value is less than x. So the payout x is applied only once. Then receipts can overwrite that. So perhaps for each person, we can store their individual value, but also track the maximum of all payout x's. Then, a person's final value is the maximum between their individual value (from receipts) and the maximum payout x.

But how do we manage this efficiently? Because when a payout occurs, instead of updating all the people, we can just track the maximum x so far. Then, for each person, their current value is the maximum between their individual value (from receipts) and the maximum payout x.

Wait, that's a possible approach. Let's think: the maximum payout x is stored as a variable. For each person, if they have a receipt (i.e., their individual value is set after the last payout), then their current value is the maximum between their individual value and the maximum payout. Otherwise, their value is the maximum payout. Wait, but how do we track whether their individual value is set after the last payout?

Alternatively, whenever a payout occurs with x, we can just keep track of the maximum x. Then, whenever a receipt is processed (type 1 event), we update the individual's value to x (but this x could be lower than the current maximum payout, which would mean that after all events, this individual's value is the maximum between x and the maximum payout). Wait, no. Because if a receipt sets x to a value lower than the current maximum payout, then the payout's x is higher, so the individual's final value would be the maximum between x and the maximum payout. But if a receipt sets x to a higher value than the current maximum payout, then the individual's value is x, and any subsequent payout with x lower than this would not affect them.

So perhaps the solution is to track for each person their last set value via receipts, and track the global maximum payout x. Then, the final value for each person is the maximum between their last set value and the global maximum payout x.

Yes, this makes sense. Because each payout sets x as the new minimum for all people. So any receipt after that can override the value for a specific person, but if the global maximum payout is higher than their receipt's value, then the person's value is the higher of the two. So the key insight is to track the maximum payout x (let's call it 'global_x') and for each person, track the last receipt's x (call it 'individual_x'). Then the final value for each person is max(individual_x, global_x).

But wait, the order of events matters. Let's consider some scenarios:

1. Suppose a payout x1 is applied. Then, the global_x is set to x1. Then a receipt for a person sets their individual_x to x2. If x2 > global_x, then the person's value is x2. If another payout x3 (x3 < x2) is applied, the global_x becomes x3. The person's value is max(x2, x3) = x2. If x3 is higher than x2, then global_x is x3 and the person's value is x3.

So, by tracking individual_x for each person (which is the last receipt's x, or the initial a_i if no receipt), and the global_x (the maximum of all payout x's), each person's final value is max(individual_x, global_x).

That seems correct. Because each payout increases the global_x (or leaves it the same if the new x is lower than current global_x). Wait, no. Because if a payout is with x less than the current global_x, then applying it doesn't do anything. So the global_x should be the maximum of all payout x's. So whenever a payout is processed, we set global_x to max(global_x, x).

Yes. So:

global_x starts at 0 (or maybe the maximum of all initial a_i's? No, the initial a_i's are their individual_x. The payouts are applied after the initial setup.)

Wait, no. The initial a_i's are the initial individual_x values. So each person's individual_x is initialized to a_i. Then, any receipts (type 1 events) update their individual_x. The payouts (type 2 events) set global_x to the maximum between current global_x and x. So the final value for each person is max(individual_x, global_x).

Yes! Because whenever a payout occurs, all people with individual_x less than x are set to x. But since global_x is the maximum of all payout x's, the final check is whether individual_x is below the maximum payout x. If so, the person's value is the maximum x. Otherwise, they keep their individual_x.

So the approach is:

- Maintain an array individual_x for each person, initialized to their a_i.

- Maintain a variable global_x, which starts at 0 (since no payouts have been processed yet).

- For each event:

   - If it's a type 1 (receipt), update individual_x[p-1] to x.

   - If it's a type 2 (payout), update global_x to the maximum of global_x and x.

- After all events, for each person, output max(individual_x[i], global_x).

Wait, but this can't be right. Let's test with the first example:

First example input:

4

1 2 3 4

3

2 3 → type 2, x=3. global_x becomes 3.

1 2 2 → type 1, person 2's individual_x is set to 2.

2 1 → type 2, x=1. global_x remains 3.

Final individual_x is [1,2,3,4], global_x is 3. So max for each is [3,2,3,4]. Which matches the example's output.

Yes. So this approach works for the first example.

Second example:

Initial a: [3,50,2,1,10]

global_x starts at 0.

Events:

1 2 0 → receipt for person 2 (0-based index 1). individual_x becomes [3,0,2,1,10].

2 8 → type 2, x=8. global_x is max(0,8) → 8.

1 3 20 → receipt for person 3 (0-based index 2). individual_x becomes 20.

Final global_x is 8.

So each person's final value is max(individual, 8):

3 → 3 vs 8 → 8

0 vs 8 → 8

20 vs 8 →20 

1 vs 8 →8 

10 vs 8 →10 

Which gives [8,8,20,8,10]. Which matches the example.

So this approach works.

So the key insight is that the final value for each person is the maximum between their last receipt (or initial) value and the maximum x of all payout events.

But wait, what if a payout x is lower than the previous global_x. For example, after a payout of x=5, then a payout of x=3. The global_x would stay at 5. So any receipt that sets a person's value to 4 would then be overridden by the global_x of 5, but a receipt that sets to 6 would not be.

So the approach is correct.

So the steps are:

- Read n.

- Read the initial a_i as individual_x array.

- Read q events.

- For each event, update either individual_x or global_x.

- After all events, output each individual_x[i] if it's >= global_x, else global_x.

This approach is O(n + q) time and O(n) space, which is acceptable for n and q up to 2e5.

So the code in Python would be:

Read n.

Read a list as individual_x.

global_x = 0

Process q events:

For each line in next q lines:

   split into parts.

   if the first part is 1, then update individual_x[p-1] to x.

   else, it's 2 x. Update global_x to max(global_x, x)

Then, for each individual in individual_x, output max(individual, global_x)

Yes. That's straightforward.

So the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    q = int(input_stream.readline().rstrip("\n"))

    global_x = 0

    for _ in range(q):

        parts = input_stream.readline().rstrip("\n").split()

        if parts[0] == '1':

            p = int(parts[1]) -1

            x = int(parts[2])

            a[p] = x

        else:

            x = int(parts[1])

            if x > global_x:

                global_x = x

    # Now compute the final values.

    result = [max(num, global_x) for num in a]

    print(' '.join(map(str, result)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
3 50 2 1 10
3
1 2 0
2 8
1 3 20
""",
            "output": \
"""\
8 8 20 8 10
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

Wait, in the first example, after the three events:

The events are:

1. Payout x=3 → all people with less than 3 get set to 3. So initial a is [1,2,3,4]. After payout, becomes [3,3,3,4].

2. Receipt for person 2 (second person) to set to 2 → a becomes [3,2,3,4].

3. Payout x=1. So global_x is max(3,1)=3. So no change.

So the final a is [3,2,3,4]. So when we compute max(3,3) →3 for first, max(2,3)=3 for second, etc. But according to the code, the code's a is [3,2,3,4] (because the receipt updated the second person to 2). Then the global_x is 3. So the code would output max(3,3) =3, max(2,3)=3, etc. Which gives [3,3,3,4], which is not matching the sample output.

But the sample output is 3 2 3 4. So the code's approach is wrong.

Wait, what's wrong here? Oh! Because the receipt in step 2 overwrites the person's value. But according to the problem statement, when a receipt is processed (type 1 event), the person's value is set to x. Then, any subsequent payout (type 2) with higher x would affect them again.

Wait, the code's approach tracks the maximum payout x, and for each receipt, sets the individual_x. Then, the final value is the maximum between individual_x and global_x. But in the first example, after the receipt sets the person's value to 2, the next payout (x=1) does not change anything. So the code's approach would set global_x to 3 (from the first payout) and then the receipt sets the person to 2. So during the final calculation, the max(2, 3) is 3. But the correct sample output is 2 for that person.

So the code's approach is incorrect.

Ah, I see the mistake. Because the receipt (type 1 event) overwrites the person's value to x, regardless of the current global_x. So if a receipt is processed after a payout, the person's value is x. Then, if there are no more payouts, then the final value is x. But if there's a payout after the receipt, then the person's value is max(x, the new payout's x). Wait, no. Because the payout is applied to all people with current value less than x. So, suppose after the receipt, the person's value is 2. Then a payout of x=1 is done. Since 2 is greater than 1, the payout doesn't affect them. So their value remains 2. But according to the code's approach, the global_x is 3 (from the first payout). So the code would output 3, which is wrong.

So the code's approach is not correct because the global_x is the maximum of all payout x's, but some receipts may have happened after a payout. For example, the receipt in the first example after the first payout (x=3) sets the person's value to 2. Then, the code's approach would set their final value to max(2, 3) =3. But in reality, the person's value is 2 because there are no further payouts that affect them.

Wait, no. Let's re-examine the first example's events:

Original a is [1,2,3,4].

First event: payout x=3. So all a[i] <3 are set to 3. So a becomes [3,3,3,4]. Global_x is 3.

Second event: receipt for person 2 (index 1) to x=2. So a[1] is set to 2. So a is [3,2,3,4]. The global_x remains 3.

Third event: payout x=1. The code's approach would set global_x to max(3,1) =3. So no change. Then, during the final step, each a[i] is max(their value, 3). So for person 1 (index 0) →3, 3. For person 2 (index 1) →2 vs 3 →3. But in the sample output, it's 2. So the code's approach is wrong.

So the code's logic is incorrect. What's the problem here?

Ah! The code's approach treats the global_x as the maximum of all payout x's, but after a receipt, the individual's value is set to x, and subsequent payouts (even if they have x lower than the current global_x) do not affect that individual. But according to the problem statement, a payout with x would set the individual's value to x if their current value is less than x. So, if after a receipt, their value is lower than a new payout x, their value would be updated. But in the code's approach, the global_x is the maximum of all payout x's, which is correct only if the payouts are applied in such a way that each subsequent payout is higher than the previous.

Wait, let's re-examine. The code's approach assumes that the global_x is the maximum of all payout x's. Thus, any receipt's x that is lower than the global_x would be overridden to global_x. But in reality, the receipt's x could be lower than some previous payout x, but higher than a later payout x. For example:

Suppose:

Initial a: [0].

Event 1: payout x=5 → global_x is 5. a is 5.

Event 2: receipt x=3 → a becomes 3.

Event3: payout x=4 → this would not change a (since 3 <4 → set to 4). So after this, a is 4.

So according to the code's approach:

global_x after event1:5. event3's x=4 → global_x remains 5. So final value is max(3,5) →5. But actual result should be 4.

So the code's approach is incorrect here.

Thus, the code's approach is wrong. The reason is that the code assumes that the maximum payout x is the only one that matters. But in reality, later payouts with lower x can affect some individuals if their current value (after receipts) is less than x. For example, in the scenario above, the receipt sets the a to 3. Then a payout x=4 would raise it to 4. But according to the code, the global_x is 5 (from event1), so the final value is 5. But the correct result is 4.

So the code's approach is wrong. Thus, the initial idea is incorrect.

So what's the correct approach here?

Hmm. So the problem is that the payout x could be lower than previous payouts but higher than some individual's current value (due to receipts after those previous payouts). So in that case, the payout would increase that individual's value to x.

Thus, the code's approach of tracking the maximum payout x is not sufficient. Because a later payout x (which is lower than the current maximum) can still affect some individuals.

So how to model this?

Alternative approach: we need to track for each individual, the last receipt's x and the last payout that was applied after that receipt. Because when a payout occurs, it affects all individuals whose last receipt's x is less than the payout's x and who have not received a receipt after that payout.

But tracking this for each individual is not feasible for large n and q.

Alternative idea: For each payout, the x is applied to all individuals whose current value is less than x. So, after a payout x, all individuals' values are at least x, but only if their value was less than x. So, the next time a payout occurs with x', it will affect those with current value less than x'.

Thus, the challenge is to track the current x that each individual must be at least.

But for receipts, when you set a person's value to x, their effective value is x. Then, any subsequent payout with x' higher than x will set them to x'.

So the problem is that receipts can reset the person's value, making them susceptible to later payouts with higher x's.

So the correct way to model this is:

Each individual's current value is the maximum between their last receipt's x and the maximum payout x that occurred after their last receipt.

Ah! So, for each individual, their value depends on:

- The x from the last receipt (or initial value).

- The maximum payout x that happened after their last receipt.

If the maximum payout x after their last receipt is higher than their last receipt's x, then their value is that maximum. Otherwise, it's their last receipt's x.

So how to model this?

We can track for each individual, the time (order) of their last receipt, and track all the payout events and their x values. Then, for each individual, the maximum x in the payout events that occurred after their last receipt.

But this would require, for each individual, to know all payouts after their last receipt. Storing all payouts and for each individual querying the maximum x in payouts after their last receipt's time would be computationally expensive for large n and q.

Alternatively, we can track the maximum payout x in a global variable, and track the time (or step) when the maximum payout x was increased. For each individual, when they have a receipt, we note the current maximum payout x. Then, their final value is the maximum between their last receipt x and the maximum payout x since their last receipt.

Wait, perhaps not. Let's think: the maximum payout x is stored in a variable. Whenever a payout is processed, if the x is higher than the current maximum, we update the maximum. So, the global maximum payout x is the highest x ever seen.

But in the scenario where a receipt is processed after some payouts, then any subsequent payouts (even with lower x than the current maximum) can't affect this individual unless the x is higher than the receipt's x.

Wait, no. Let's take an example:

Suppose:

global_max starts at 0.

Receipt for individual A sets x to 3. So their last receipt x is 3, and the current global_max is 0. So their current value is max(3, 0) =3.

Then a payout x=5 is processed. global_max becomes 5. So individual A's value is max(3,5) =5.

Then a payout x=4 is processed. global_max remains 5. So individual A's value is max(3,5) =5.

But if after the receipt, a payout x=2 is processed. Then global_max remains 5, so individual A's value is 5.

So in this case, the maximum payout x is 5, and the receipt's x is 3. So the individual's value is 5.

But suppose:

Individual has a receipt x=3. Then a payout x=2 (global_max remains 5). Then a payout x=4 (global_max remains 5). So individual's value is max(3,5) =5.

So the code's initial approach (max between last receipt x and global_max) would work here.

But what about the case where a receipt is made after a payout, and then a lower payout is made. For example:

Initial a: 0.

Event 1: payout x=5 → global_max becomes 5. a is 5.

Event 2: receipt x=3 → a is 3. Now, the individual's last receipt is 3, and the global_max is 5. So their value is max(3,5) =5.

Event 3: payout x=4 → global_max remains 5. So their value is 5.

But according to the problem statement, after event 3 (payout x=4), since 3 <4, the individual's value should be set to 4. Then, the final value would be 4, but the code's approach would output 5.

So the code's approach is incorrect here.

Ah, this shows that the initial approach is wrong. Because the code's approach of max(individual_x, global_max) is not correct. Because in this scenario, after event 3, the individual's value is 3, which is less than x=4. So the payout sets it to 4. So the final value should be 4. But according to the code's approach, global_max is 5 (from event1), so max(3,5) is 5. Which is incorrect.

Thus, the code's approach is incorrect.

So the problem is that the code's approach treats all payout events as if they have been the maximum x, but some payout events with x lower than the current maximum x but higher than some individual's last receipt x can still affect that individual's value.

So what's the solution here?

Alternative approach: track for each individual the last receipt's x and the time when it happened. For the payout events, track all x's and their times. Then, for each individual, find the maximum x in the payout events that happened after the last receipt.

But storing all payout x's and their times is O(q) space. For each individual, when their last receipt was at time T, we need to find the maximum x in all payout events with time > T.

This can be done with a segment tree or a prefix maximum array.

Wait, here's an idea:

We can keep a list of all payout x's in the order they are processed. Then, for each payout, we can track the maximum x up to that point. For example, we can have an array max_payout where max_payout[i] is the maximum x in the first i payout events. Then, when a receipt happens at time T, which corresponds to the K-th event (among all events), we can note how many payout events have occurred up to that point. Then, any payout events after that would have higher indices in the payout list, and we can compute the maximum x in those events.

Wait, perhaps not. Let's think about all events. For example, events can be a mix of receipts and payouts. So the payout events are not contiguous. So perhaps we need to track for each payout event, the time step when it occurred. Then, for an individual's last receipt time step, we can find all payout events that happened after that time step and find the maximum x among them.

But storing all payout x's with their time steps would allow us to query the maximum x in payouts after a certain time.

This can be done using a segment tree or a binary indexed tree (Fenwick tree) with the events stored in order, and for each payout, record its x. Then, when querying for the maximum x after a certain time, we can query the segment tree from that time index to the end.

But how to manage this?

Alternatively, for all events, we can track a list of the payout x's and their positions in the event sequence. For example, when processing each event, if it's a payout, we add its x to a list along with the event's index (from 0 to q-1). Then, for each receipt event, when it occurs at event index t, we need to find the maximum x in all payout events that have an event index greater than t. Because those payout events happened after the receipt.

Wait, this is getting complicated, but let's think through an example.

In the previous example where the code's approach failed:

Events:

Event 0: payout x=5 (event index 0)

Event 1: receipt (event index 1)

Event 2: payout x=4 (event index 2)

So, the list of payout events is [(0,5), (2,4)].

For the receipt at event index 1, the max payout after event 1 is the maximum x in events with index >1. In this case, event 2 is x=4. So the max is 4. So the individual's final value is max(3,4) =4.

Which is correct.

So, the approach is:

- For each payout event, record its x and the event index (the order in which it was processed among all events).

- Also, maintain a data structure that allows us to query the maximum x in payout events with event index > T, where T is the event index of the last receipt for an individual.

- For each receipt, record the event index when it occurred and the x.

- For each individual, their final value is the maximum between their last receipt x and the maximum payout x in payout events that occurred after the receipt's event index.

This would correctly capture all payout events that could affect the individual after their last receipt.

But how to efficiently compute the maximum x in payout events after a certain event index?

We can preprocess the list of payout events into a structure that allows for range maximum queries. For example:

We can create an array payout_x that contains the x's of all payout events in the order they were processed, and an array payout_indices that contains their event indices.

Then, for a given T (event index), we need to find all elements in payout_indices where the event index is > T. For those elements, we find the maximum x in payout_x.

But this is equivalent to finding the first payout event in the list that has an event index > T and then finding the maximum x from that point onwards.

To do this efficiently, we can build a suffix maximum array. For each position i in the payout_x array, the suffix_max[i] is the maximum x from payout_x[i] to the end.

Then, when given T, we can perform a binary search to find the first payout event in payout_indices with event index > T. Let's say this is found at position k. Then the maximum x is suffix_max[k].

But how to find k?

The payout_indices array is sorted in increasing order, since payout events are processed in the order of their occurrence, and their event indices are strictly increasing.

For example, if there are three payout events at event indices 0, 2, and 5, the payout_indices array is [0,2,5].

So, for a given T, we can binary search the payout_indices array to find the first index where the event index is > T. The number of elements after that is the number of payout events after T.

If there are none, then the maximum is 0. Otherwise, we take the suffix_max from that position.

So, the steps to preprocess are:

1. Collect all payout events in order, storing their x and event index.

2. Build a list payout_x and payout_indices.

3. Build a suffix_max array, where suffix_max[i] is the maximum of payout_x[i...end].

Then, for each receipt event, when it occurs at event index t, the maximum payout x after t is:

   find the first index k in payout_indices where event index > t.

   if k is found, then the maximum is suffix_max[k].

   else, the maximum is 0.

So, the final value for the individual is max(receipt_x, max_payout_after_receipt).

For individuals who have never received a receipt (i.e., their initial a_i), their last receipt event is considered to have occurred at event index -1. So we need to find all payout events (event indices >=0), and compute the max payout x, which is the suffix_max[0], which is the maximum of all payout x's.

This approach should correctly handle all cases.

So, the plan is:

- For all events, track payout events and their event indices.

- Build a suffix_max array for the payout_x.

- For each individual:

   if they have a receipt, track the event index of that receipt and the x.

   else, the event index is -1 (initial value).

   compute the maximum payout x after their receipt event index.

   their final value is max(x, max_payout_after).

So, the steps for the code:

Read n.

Read the initial a list.

Read q events.

Process each event, and for each payout event, record x and event index (t, which is the 0-based count of all events processed so far).

For example, for each event in the input:

   if it's a payout, add to payout_x the x, and to payout_indices the current event index (starting from 0).

   else, it's a receipt. For the receipt, track for the individual p-1: their last receipt x and the event index (t).

Then, after all events:

   build the suffix_max array for payout_x.

   for each individual:

      if they have receipts:

          last_receipt_t = their last receipt's event index.

          last_receipt_x = their x.

      else:

          last_receipt_t = -1.

          last_receipt_x = a[i].

      find the maximum payout x that occurred after last_receipt_t.

      final value is max(last_receipt_x, max_payout_x_after).

So, implementing this in Python.

But how to efficiently build the suffix_max array and perform the binary search?

First, collect all payout events. Let's say we have a list of payout entries, each with their event index and x. Then, we can create two lists:

payout_indices = list of event indices for payout events.

payout_x = list of x's for those events.

Then, the suffix_max array can be built as follows:

suffix_max = [0] * len(payout_x)

if len(payout_x) > 0:

   suffix_max[-1] = payout_x[-1]

   for i in range(len(payout_x)-2, -1, -1):

       suffix_max[i] = max(payout_x[i], suffix_max[i+1])

This way, suffix_max[i] is the maximum x from i to end.

Then, for a given last_receipt_t, to find the first payout event after it:

We need to find the smallest index k in payout_indices where payout_indices[k] > last_receipt_t.

We can use bisect.bisect_right for this.

For example, in Python:

from bisect import bisect_right

k = bisect_right(payout_indices, last_receipt_t)

if k < len(payout_indices):

   max_payout = suffix_max[k]

else:

   max_payout = 0

Then, the final value is max(last_receipt_x, max_payout).

This approach should work.

Now, the code structure:

Read n.

Another test case: the previous example where the code's approach failed.

Events:

Event0: payout x=5 → payout_indices [0], payout_x [5].

Event1: receipt x=3 → receipts[p=0] = (1,3).

Event2: payout x=4 → payout_indices [0,2], payout_x [5,4]. suffix_max is [5,4].

For individual 0:

last_event is 1.

Find payout_indices >1. payout_indices are [0,2]. bisect_right([0,2], 1) → index 1 (since 0 <=1 <2). So k=1. suffix_max[1] is4. final is max(3,4)=4. Correct.

Thus, this approach works.

So the code should be correct.
</think>

```python
import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())

payout_indices = []
payout_x = []
receipts = {}

for event_idx in range(q):
    parts = input().split()
    if parts[0] == '1':
        p = int(parts[1]) - 1
        x = int(parts[2])
        receipts[p] = (event_idx, x)
    else:
        x = int(parts[1])
        payout_indices.append(event_idx)
        payout_x.append(x)

# Build suffix max array for payouts
suffix_max = []
if payout_x:
    m = len(payout_x)
    suffix_max = [0] * m
    suffix_max[-1] = payout_x[-1]
    for i in range(m - 2, -1, -1):
        suffix_max[i] = max(payout_x[i], suffix_max[i + 1])

result = []
for i in range(n):
    if i in receipts:
        last_event, x = receipts[i]
    else:
        last_event = -1
        x = a[i]
    
    # Find the first payout index after last_event
    k = bisect.bisect_right(payout_indices, last_event)
    current_max = suffix_max[k] if k < len(payout_x) else 0
    final = max(x, current_max)
    result.append(str(final))

print(' '.join(result))
```
