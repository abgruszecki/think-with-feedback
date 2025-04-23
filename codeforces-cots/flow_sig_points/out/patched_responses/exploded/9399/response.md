<think>
Okay, let's try to understand this problem. The task is to find the minimum number of distinct people that Polycarpus could have seen, given a sequence of '+' and '-' characters. Each '+' represents someone entering, and '-' someone exiting. The key here is that we don't know how many people were present when Polycarpus started and when he ended. But we need to model this in a way that the sequence is possible, and find the minimum possible number of people.

Hmm. So the main idea is that whenever there's a '-', if there's no possible person to exit (i.e., the current number of people is zero), then that implies that someone must have been present before the first event. So we need to track the possible number of people at each step, and see how many times we have to add people when a '-' occurs when there's no one left.

Wait, but to minimize the total number of people, we want to reuse the same people as much as possible. For example, in the first example "+-+-+", the output is 1. Let's see why:

The sequence is + - + - +. Let's track the possible current number of people and the required people.

Start with 0 people (assuming initial state is unknown, but to minimize, we can choose initial state as 0? Or maybe not. Wait, the problem says that the initial and final counts are unknown. So for the minimal people, maybe we can have some people present at the start, but that's part of the variables we can adjust.)

Wait, no. Let's think of the process. The minimal number of people is determined by how the sequence can be arranged such that whenever there's a '-', there's someone to leave, possibly by adding people at the start or during the sequence.

But here's the thing: each time there's a '-', if there's no one present, then we have to assume that there were some people before the first event. So we can model the current available people and the total number required.

Alternatively, maybe the approach is to track the current balance (number of '+' minus '-') up to each step. But the initial balance can be adjusted. The problem is to find the minimal maximum number of people that the balance (with some initial offset) never goes below zero.

Wait, here's a way to model it. Let's imagine that the initial number of people is some variable S. Then, for each step in the sequence, the current balance is S plus the sum of the previous operations (each '+' adds 1, '-' subtracts 1). But this balance must never drop below zero. The goal is to find the minimal possible maximum value of (S + balance up to that point), but also considering that S must be chosen such that the balance after each step is non-negative.

Wait, perhaps not. Let me think again. Let's model the sequence of events as a series of increments and decrements. Let's call the initial number of people as 'initial'. Then, as we process each character in the string, the current number of people is initial plus the sum of the first i characters (where '+' is +1, '-' is -1). For each step, this value must be >= 0. The minimal number of people is the maximum between (initial) and (initial plus the maximum sum encountered). Also, the initial can be chosen as any non-negative integer such that, for all steps, initial plus the cumulative sum up to that step is >=0.

But how do we find the minimal possible maximum number of people? Because the number of people at any time is (initial + cumulative_sum[i]), and the maximum of these is the total required. So the problem reduces to choosing initial such that all (initial + cumulative[i]) >=0, and the maximum (initial + cumulative[i]) is minimized.

Wait, that makes sense. Because the initial is the number of people present at the start. Then, each step's cumulative sum (sum of all previous steps) plus initial must be >=0. The maximum people at any time is initial + the maximum cumulative sum up to any point. We need to find the smallest possible value of that maximum.

Yes. So the problem is transformed into finding the minimal possible maximum of (initial + cumulative_sum[i]) for all i, where initial is chosen such that for all i, initial + cumulative_sum[i] >=0.

So how to find this initial?

Let's let cumulative_sum be an array where each element is the sum of the first j elements (each '+' is +1, each '-' is -1). For example, for the sequence "+-+", cumulative_sum would be [1, 0, 1].

Then, the constraints are:

initial + cumulative_sum[i] >=0 for all i.

But cumulative_sum can be negative. Let's find the minimal initial such that initial >= -min_cumulative.

Wait, no. Let's see: initial + cumulative_sum[i] >=0 → initial >= -cumulative_sum[i] for all i. The minimal initial that satisfies this is initial = max(0, - (min_cumulative)), where min_cumulative is the minimum cumulative_sum over all steps.

Wait, for example, if the cumulative_sum can go as low as -3, then initial must be at least 3. Then, the maximum (initial + cumulative_sum[i]) would be (3 + max_cumulative). So the minimal possible maximum is 3 + max_cumulative.

But the initial can't be negative. So if the min_cumulative is positive, then initial can be zero.

Wait, let's take the first example:

Input: "+-+-+"

The sequence of steps is:

Each character: +, -, +, -, +

The cumulative_sum array would be:

After first +: 1

After -, 1-1=0

After +, 0+1=1

After -, 1-1=0

After +, 0+1=1.

So the cumulative sum array is [1,0,1,0,1]. The min cumulative is 0. So initial needs to be >= 0. But wait, if initial is 0, then all the steps have initial + cumulative_sum[i] = 0+1=1, 0+0=0, 0+1=1, etc. Which is okay. Then the maximum is 1. So the minimal number of people is 1.

Which matches the sample.

Another example: input "---"

Each step is '-', so cumulative sum is -1, -2, -3. The min cumulative is -3. So initial must be >=3. Then, the maximum cumulative sum is initial + (sum of the steps). The sum of all steps is -3. So initial is 3, and the maximum is 3 + (-3) = 0. But wait, the sum of the entire sequence is -3. So the initial is 3, and the cumulative_sum after all steps is 3 + (-3) = 0. But the maximum of initial + cumulative_sum[i] is 3 + (-1) = 2 (after first '-'), 3 + (-2) = 1 (after second), 3 + (-3) =0. The maximum is 2. So the total number of people is 3? Wait, the sample output is 3. But according to this model, the initial is 3. Then the maximum during the steps is 3 (the initial) after first step? Wait, no. Because the initial is 3. The first step is '-', so cumulative sum is -1. So initial + cumulative_sum[0] is 3 -1 = 2. The maximum of all initial + cumulative_sum[i] would be 3 (initial) when there are no steps yet? Wait, the initial is 3, then the first step is a '-', so after first step, the count is 3-1=2. Then second step: 2-1=1. Third step: 1-1=0. So the maximum is the initial (3), but only when there are no steps. But in our model, the initial is part of the count. Wait, perhaps the model is that the initial is the starting count. Then each step is applied in sequence. So the maximum count is the maximum of (initial + cumulative_sum[i] for i in 0..n-1), where cumulative_sum[i] is the sum up to and including the i-th step.

Wait, in the example where the input is "---", the cumulative sums are:

After first '-', sum is -1.

After second '-', sum is -2.

After third '-', sum is -3.

So the array is [-1, -2, -3].

The initial must be >= 3 (since the minimum cumulative is -3 → initial >= 3).

Then initial + cumulative_sum[0] is 3 + (-1) = 2.

cumulative_sum[1] is -2 → 3 + (-2) =1.

cumulative_sum[2] is -3 → 0.

The maximum of these is 2. But wait, the initial is 3, which is the count before any steps. So the maximum count during the process is 3 (before any steps), then 2, 1, 0. So the maximum is 3. But according to our model, initial is 3. The cumulative sum for the initial is 0, but the steps are applied. Wait, maybe I'm misunderstanding how the cumulative sum is calculated.

Wait, the cumulative_sum[i] is the sum after processing the first i+1 characters. Wait, maybe the confusion is in how the cumulative sum is tracked.

Let me clarify: Let's suppose the input is a string s of length n.

We can precompute the prefix sums.

Let's create an array prefix where prefix[0] = 0, prefix[1] is the value after the first character, prefix[2] after the second, etc. Wait, perhaps not. Let's model it correctly.

The initial number of people is S. Then, after each event, the number of people is S plus the sum of the events up to that point.

Each event is +1 or -1.

So for the i-th event (0-based), the cumulative sum up to and including the i-th event is sum(events[0..i]).

Wait, but if the events are processed in order, then for each step i, the sum of the first (i+1) events. So for the first example, events are +, -, +, -, +. The cumulative sum after each step is:

After first event: +1 → sum is 1.

After second: 1 -1 → 0.

Third: 0 +1 →1.

Fourth:1-1→0.

Fifth:0+1→1.

So the array of cumulative sums after each step is [1,0,1,0,1].

So the initial S is the number of people before any events. Then, after each step, the number of people is S + sum up to that step.

So the constraints are that for each step i (from 0 to n-1), S + sum_up_to_i >=0.

The maximum number of people at any time is the maximum between S (initial) and S + sum_up_to_i for all i.

We need to find the minimal possible maximum.

So the problem is to find the minimal possible maximum of (S, S + sum_0, S + sum_1, ..., S + sum_{n-1} }), given that S + sum_i >=0 for all i.

To minimize this maximum, what is the optimal S?

Let's denote the minimal possible S as S_min. But how?

Let's see. The minimal maximum can be found by considering the minimal S that ensures all S + sum_i >=0, and then compute the maximum of S + sum_i and S.

Wait, but sum_i is the cumulative sum up to step i. So for the initial S, the maximum possible is the maximum between S and all (S + sum_i).

But since sum_0 is the first event's value, etc.

Wait, no. Let's think again. The initial count is S. Then after the first event, the count is S + sum_0 (sum_0 is the value of the first event). Then after the second event, it's S + sum_0 + sum_1, but wait, no. Wait, the sum_0 is the first event's value. Then sum_1 is the sum of first and second events. Wait, perhaps the sum array is built as cumulative sums.

Alternatively, the sum array is the cumulative sum after each step. For example, for the input "+-", the sum array is [1, 0].

So the sum array is built as follows:

sum[0] = value of first event.

sum[1] = sum[0] + value of second event.

sum[i] is the sum of the first (i+1) events.

Then, the number of people after processing the first (i+1) events is S + sum[i], where S is the initial count.

The constraints are S + sum[i] >=0 for all i.

The maximum number of people is the maximum of S (the initial) and S + sum[0], S + sum[1], etc. Because S is the initial count before any events, so that's part of the possible maximum.

So, the problem reduces to:

Find the minimal possible value of max(S, S + sum[0], S + sum[1], ..., S + sum[n-1}) ), given that S >= -sum[i] for all i (since S + sum[i] >=0 → S >= -sum[i]).

But also S must be >=0, since initial count can't be negative.

Wait, but the initial count can't be negative. So S must be >=0 and S >= -sum[i] for all i.

But the minimal S that satisfies all these constraints is max(0, -min_sum), where min_sum is the minimal value in the sum array.

Once S is determined as max(0, -min_sum), then the maximum people is the maximum between S and S + sum[i] for all i.

So the maximum people is max(S, S + sum[0], S + sum[1], ..., S + sum[n-1}).

But sum[0], sum[1], etc. are the cumulative sums. Let's denote the maximum of all sum[i] as max_sum. Then, the maximum people is max(S, S + max_sum).

Wait, no. Because for each i, S + sum[i] could be higher than S. So the maximum of all S+sum[i] is S + max_sum (if max_sum is the maximum of the sum array).

But S is the initial count, which could be larger than S + max_sum. For example, if the sum array's maximum is negative, then S + max_sum is less than S, so the maximum is S.

So the maximum people is max(S, S + max_sum).

Therefore, the steps to compute the answer are:

1. Compute the cumulative sums array sum_list.

2. Find the minimal sum in sum_list: min_sum.

3. Compute S = max(0, -min_sum).

4. Find the maximum sum in sum_list: max_sum.

5. The result is the maximum between S and S + max_sum.

Wait, let's test this with the sample input 1.

Sample 1 input: "+-+-+"

sum_list is [1,0,1,0,1]. The min_sum is 0. So S = max(0, -0) → 0. The max_sum is 1. So S + max_sum is 0+1=1. The maximum between S (0) and 1 is 1. Which matches the sample.

Sample 2 input: "---"

sum_list is [-1, -2, -3]. min_sum is -3. So S = max(0, 3) → 3. max_sum is -1. S + max_sum is 3-1=2. The maximum between 3 and 2 is 3. Which matches the sample output.

Another example: input "+--", which would have sum_list [1,0,-1]. The min_sum is -1. S = max(0, 1) →1. max_sum is 1. So S + max_sum is 2. The maximum between 1 and 2 is 2. So the answer is 2.

Another test case: input "+". sum_list is [1]. min_sum is 1. So S = max(0, -1) →0. max_sum is 1. So S+max_sum is 1. The maximum is 1. Correct.

Another test case: input "-". sum_list is [-1]. min_sum is -1. S = 1. max_sum is -1. So maximum is max(1, 1-1=0) →1. Correct.

So this approach seems correct.

So the steps for the code are:

1. Read the input string.

2. Compute the cumulative sum array.

3. Find the minimum and maximum of the cumulative sums.

4. Compute S as max(0, -min_sum).

5. The answer is the maximum between S and S + max_sum.

Therefore, the code can be written as follows:

First, process the input string to compute the cumulative sums. Then compute min and max of those sums. Then compute S and the result.

Let's code this.

But wait, how to compute the cumulative sums:

Initialize current_sum as 0.

Wait, no. For each character in the string:

The first step is the first character. For each step i (0-based), the sum after that step is sum of the first i+1 characters.

Wait, for example, if the input is "+-+", the characters are [ '+', '-', '+'].

sum_list would be:

After first '+': 1

After '-': 0

After '+': 1.

So the code can build the sum_list by iterating through each character, adding +1 or -1 to a running total, and appending that total to sum_list.

Yes.

So code steps:

s = input().strip()

current = 0

sum_list = []

for c in s:

    current += 1 if c == '+' else -1

    sum_list.append(current)

Then find min_sum = min(sum_list)

max_sum = max(sum_list)

S = max(0, -min_sum)

result = max(S, S + max_sum)

print(result)

Wait, but wait: the maximum of S and S + max_sum. Because S is the initial count, which is part of the possible maximum. Because the initial count could be higher than any of the sum steps. For example, if all the sum steps are negative, then the initial S is the maximum.

But when you compute S + max_sum, which would be S + (the maximum sum). If the maximum sum is positive, then S + max_sum could be higher than S.

But for example, if the sum_list is [3, 2, 5], then min_sum is 2 (wait, no: in this case, the sum_list is 3, 2, 5? No, the steps would be each character adding. For example, if the input is "+++", then sum_list would be [1, 2, 3]. So max_sum is 3. min_sum is 1. S would be max(0, -1) →0. Then S + max_sum is 3. The maximum between 0 and 3 is 3. Which is correct.

Another example: input is "++-". sum_list is [1,2,1]. min_sum is 1. So S is 0. S + max_sum is 0 +2=2. The maximum is 2. Correct.

So the code seems to handle all cases correctly.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    current_sum = 0
    min_sum = 0
    max_sum = 0
    for c in s:
        current_sum += 1 if c == '+' else -1
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum
    s_val = max(0, -min_sum)
    result = max(s_val, s_val + max_sum)
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
---
""",
            "output": \
"""\
3
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

Sample 2: input "---", sum_list [-1,-2,-3]. min_sum=-3 →S=3. max_sum=-1. S+max_sum=2. max(3,2)=3. Correct.

So the code works.

Thus, the optimal approach is O(n) time and O(n) space, but since n can be up to 300, this is acceptable.

But in Python, even for n=300, the code runs quickly. So no problem.

So the final code is as described.
</think>

```python
s = input().strip()
current_sum = 0
min_sum = 0
max_sum = 0
for c in s:
    current_sum += 1 if c == '+' else -1
    if current_sum < min_sum:
        min_sum = current_sum
    if current_sum > max_sum:
        max_sum = current_sum
s_val = max(0, -min_sum)
result = max(s_val, s_val + max_sum)
print(result)
```
