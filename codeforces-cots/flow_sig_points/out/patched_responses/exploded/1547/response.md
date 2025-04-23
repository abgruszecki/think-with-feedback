<think>
Okay, let's see. The problem is to find the minimal possible number of stones in the pile after n operations, given that each '-' operation (taking a stone) requires the pile to be non-empty before the operation. So, the initial pile size must be such that after each '-', the pile isn't negative. We need to track the minimal initial stones that allow all operations, then compute the final stones based on that initial value.

Hmm, right. So the key is to determine the minimal initial count, then apply all operations to get the final count. But how do we find that initial count?

Let's think of it like this: For the pile to be non-empty before each '-', the balance after each step must not drop below zero. But the initial value plus the cumulative operations up to each step must be >=1 (since before taking a stone, the pile must have at least 1 stone). Wait, no. Wait, the pile is non-empty before each '-' operation. So for a '-' at step i, the initial stones plus the sum of operations up to i-1 (before the current step) must be at least 1, because after the previous steps, just before this operation, the pile has some stones, and we subtract one.

Wait, maybe we need to model the problem as the initial number of stones plus the cumulative sum up to step i (after i operations) must be >=0 at all steps. Wait, no. Let's think again.

Each operation is either '+' or '-'. Let's model the process:

Suppose the initial number of stones is x. Then, for each operation in the string s (from left to right):

- If the operation is '+', x becomes x + 1.
- If it's '-', x must be >=1 before the operation, so after subtracting 1, x becomes x - 1.

But the problem says that before each operation of taking a stone, the pile was non-empty. So before each '-', the current x (before the operation) must be >=1. So during the process, after each operation, the x can be zero (if the operation was '-', and x was 1 before, then after it becomes 0). But before the next operation, if it's '-', then the x must be >=1 again. So the problem is to track the minimal possible initial x such that all the constraints are satisfied. Then, compute the final x (after all operations) and find the minimal possible final x.

So to model this, the initial x must be such that, when we simulate each operation, the x before each '-' is at least 1. So the question is to find the minimal possible x such that during the process, after each step (before the operation), the x is at least 1 if the operation is '-'.

Wait, no. Because the operations are processed in sequence. For example, for the first operation, if it's '-', then the initial x must be >=1. Then, after subtracting 1, x becomes x-1. Then, the next operation is processed. So for each '-' in the sequence, the x before that operation must be >=1.

So the way to model this is to track the cumulative effect of the operations and find the minimal initial x that ensures that, after each step, before any '-', the x is at least 1.

Wait, perhaps another approach: Let's model the process as a sequence of steps. Let's track the required minimum initial stones. Let's think in terms of the minimum possible x.

Let’s process the operations step by step and track the required constraints on x.

At each step, before processing the i-th operation (s[i]), if the operation is '-', then the current value of x (after previous operations) must be >=1. So x plus the sum of previous operations (before the current step) must be >=1. Because the initial x plus the sum up to i-1 steps (since the current step is i-th) is the value before the i-th operation.

Wait, perhaps we can model the process as follows:

Let’s define a variable current_balance, which starts at 0. For each step, the current_balance is the sum of the operations up to that step. But since the operations are '+' or '-', which can be represented as +1 or -1. Wait, but in terms of the initial x, the actual stones after each step is x + sum of operations up to that step. But before each '-', the sum up to that step (excluding the current step) must be x + sum_so_far >=1.

Wait, maybe we can model the problem by tracking the minimal required initial x such that for every prefix up to index i (exclusive) where s[i] is '-', the sum of the first i operations (but wait, no. Let's think again.

Alternatively, for each i-th operation (0-based?), suppose the operation is '-'. Then, before this operation, the number of stones must be >=1. The number of stones before this operation is equal to the initial x plus the sum of the first (i) operations (since each operation before i-th has been applied). Wait, no. Because the i-th operation hasn't been applied yet. Let's index the operations from 0 to n-1. Let's say before processing the i-th operation, the sum of the operations up to i-1 is sum_so_far. Then, the initial x plus sum_so_far is the current number of stones. If the i-th operation is '-', then x + sum_so_far >=1 must hold. Because that's the number of stones before processing the i-th operation (since the sum_so_far is the sum of the first i operations? Wait, no. Let's clarify:

The initial number is x. Then, each operation is applied in sequence. So after the first i operations (0-based?), the sum of the operations is sum_0_to_i. So the number of stones after i operations is x + sum_0_to_i. But before the i-th operation, the sum of operations up to i-1 is sum_0_to_i-1, and the number of stones is x + sum_0_to_i-1. If the i-th operation is '-', then x + sum_0_to_i-1 must be >=1. Because that's the number of stones before the i-th operation. So for each i where s[i] is '-', the condition x + sum_0_to_{i-1} >=1 must hold.

So, the problem reduces to finding the minimal x such that for all positions i where s[i] is '-', x >= 1 - sum_0_to_{i-1}.

The minimal x is the maximum value of (1 - sum_0_to_{i-1}) for all such i. Because x must be >= each of these values, so the minimal x is the maximum of these.

Once x is determined, the final number of stones is x plus the total sum of all operations.

So the steps to solve the problem are:

1. Precompute the prefix sums of the operations, where each '+' is +1, '-' is -1.

2. For each position i where the operation is '-', compute 1 - (sum of first i terms, since sum_0 to i-1 is the sum after i-1 steps). Wait, no. Let's think again:

Suppose the operations are s[0], s[1], ..., s[n-1].

The prefix sum after k operations is sum_0_to_k = sum(s[0..k]). For each i where s[i] is '-', the sum before the i-th operation is sum_0_to_{i-1} (since sum_0_to_{i-1} is the sum after i-1 operations). The initial x plus sum_0_to_{i-1} must be >=1. So x >= 1 - sum_0_to_{i-1}.

So for each '-', the required x is at least (1 - sum_0_to_{i-1}).

We need to compute the maximum of these values. Then, the minimal x is the maximum between 0 (since x can't be negative) and this value. Wait, because x can't be negative. For example, if all the required values for x are negative, then x can be 0 (the minimal possible), but only if it satisfies all constraints. Wait, no. Wait, in cases where all the (1 - sum_0_to_{i-1}) are negative, then x can be 0, as it's greater than all those required values. So x is the maximum between 0 and the maximum of (1 - sum_0_to_{i-1}) for all '-' in s.

Once x is determined, the final answer is x plus the total sum of all operations.

But how do we compute the sum_0_to_{i-1} for each i where s[i] is '-'?

So here's the plan:

Initialize a variable current_sum = 0.

We need to track, for each '-', the sum up to the previous step.

So for each i in 0..n-1:

   if s[i] is '-', then we need to compute 1 - (current_sum_before_this_operation).

   So the current_sum_before_this_operation is the sum of all operations before i. So for the first operation (i=0), the sum before is 0.

Wait, let's index each operation as 0-based. So for each i-th operation (from 0 to n-1):

   sum_before = sum of s[0..i-1]. So for i=0, sum_before is 0.

So to compute sum_before for each '-', we can track the prefix sum step by step.

Let's see:

Initialize prefix_sum = 0.

For each i from 0 to n-1:

   before processing s[i], sum_before is prefix_sum.

   then, process s[i], which is either '+' or '-'.

   if s[i] is '-', then sum_before (prefix_sum) must satisfy x + sum_before >=1. So x >= 1 - sum_before.

   then, after processing s[i], prefix_sum increases or decreases by 1.

So, the approach is:

- Iterate through each character in the string s, keeping track of the prefix sum up to the current step (before processing the operation).

- For each '-', calculate 1 - (current prefix_sum). Add this to a list of required x values.

- The maximum required x is the maximum of all these (1 - sum_before) values, and possibly 0 (if all are negative, then x can be 0).

Once x is determined, the final answer is x + total_sum, where total_sum is the sum of all operations (each '+' is +1, each '-' is -1).

But wait, the total_sum is the sum of all operations. Because after x initial stones, each operation adds or subtracts 1, so the final stones are x + total_sum.

So the steps are:

1. Compute all the positions where the operation is '-', and for each, compute 1 - (sum_before). Sum_before is the sum of the operations up to, but not including, the current position.

2. The required x is the maximum between 0 and the maximum of these values.

3. The final answer is x + sum_operations.

So let's take the first example:

Input:

3

---

sum_before for each '-':
First '-': i=0, sum_before is 0. So 1 - 0 =1.

Second '-': i=1, sum_before is -1 (since after first '-'). So 1 - (-1) =2.

Third '-': i=2, sum_before is -2. So 1 - (-2) =3.

So the maximum of 1,2,3 is 3. So x is 3. sum_operations is -3. 3 + (-3) =0. Which matches the example.

Another example:

Input 4: "++++"

All operations are '+', so there are no '-'. So the list of required x values is empty. So x is 0. sum_operations is 4. 0+4=4. Which matches the second example.

Third example: input 2, "-+"

The first operation is '-', sum_before is 0. 1-0=1. The second is '+', no constraint. So x must be 1. sum_operations is 0. 1 + 0 =1. Which matches.

Fourth example: 5, "++-++"

Operations: +, +, -, +, +.

Let's track each '-' (only the third operation, i=2):

sum_before for i=2 is sum of first two '+' (each +1). sum_before is 2.

1 - sum_before = 1-2 = -1. So the required x is the maximum of 0 and -1, which is 0. sum_operations is 1+1-1+1+1=3. 0+3=3. Which matches the fourth example.

So this approach seems to work.

So the plan is:

- Initialize prefix_sum =0.

- Initialize required_x as 0.

- For each character in s:

   if the character is '-', compute 1 - (prefix_sum). If this is greater than the current required_x, update required_x.

   then, update prefix_sum: +=1 if '+', else -1.

- After processing all characters, the required x is max(0, required_x).

- The total_sum is prefix_sum (since after processing all characters, prefix_sum is sum of all operations).

- The final answer is x + total_sum.

Wait, because during processing, after the character is processed, we add to prefix_sum. So for example, for the first '-', when we process it, prefix_sum is 0 (sum_before), then we subtract 1. So the sum_after is -1. So yes, the total_sum is the sum of all operations, which is the final prefix_sum.

So the code can be structured as follows:

Read n.

Read s.

Initialize prefix_sum =0, required_x =0.

total_sum will be computed as the sum of all operations, but since we are tracking prefix_sum during processing, the final prefix_sum is the total_sum.

Wait, no. Let's see: for each character in s, we process in order.

Initialize prefix_sum =0.

But wait, no. Because the first character is the first operation. For example, for i=0:

sum_before is prefix_sum (0), then we process the operation. If it's '-', then sum_after is -1.

So during processing, for each character, we first check if it's '-', then add the required x constraint, then update prefix_sum.

So the code steps:

required_x starts at 0.

prefix_sum starts at 0.

Wait, no. Because sum_before is the sum before processing the current character.

Wait, here's the correct approach:

Initialize prefix_sum_before_operation = 0.

Then, for each character in s:

   if the character is '-', then required_x is max(required_x, 1 - prefix_sum_before_operation).

   then, update prefix_sum_before_operation by adding +1 or -1, depending on the operation.

So prefix_sum_before_operation is the sum before processing the next operation.

Wait, for example, for the first operation:

sum_before is 0.

If it's '-', then required_x becomes max(0, 1-0) =1.

Then, sum_before becomes 0 -1 = -1 (after processing the first '-').

Then, the next operation's sum_before is -1.

So in code:

sum_before =0

required_x =0

for each op in s:

   if op == '-': 

      candidate = 1 - sum_before

      if candidate > required_x:

          required_x = candidate

   # then, apply the operation to sum_before

   if op == '+':

       sum_before +=1

   else:

       sum_before -=1

So after processing all operations, sum_before is the sum of all operations.

Wait, no. Because sum_before starts at 0. For the first operation, the sum_before is 0 (sum before processing it). Then after processing the first op, sum_before becomes 0 + (op's effect). For example, if the first op is '-', sum_before becomes 0 -1 = -1.

But the sum of all operations is the sum of each op. So after processing all, sum_before is equal to the total sum of operations.

Yes. Because each op is applied once. So sum_before starts at 0, then after processing the first op, it's 0 + (op's value), which is the sum of the first op. Then after processing the second op, it's sum of first two, etc.

So sum_before after processing all operations is the total sum.

So the code can be written as:

n = int(input())

s = input().strip()

sum_before =0

required_x =0

for op in s:

    if op == '-':

        # calculate 1 - sum_before

        candidate = 1 - sum_before

        if candidate > required_x:

            required_x = candidate

    # update sum_before with current op's effect

    if op == '+':

        sum_before +=1

    else:

        sum_before -=1

# required_x is the maximum of all 1 - sum_before for '-'

x = max(0, required_x)

final = x + sum_before

print(final)

Wait, let's test this code with the examples.

First example:

Input 3, s = '---'

Processing each op:

Op1: '-'

sum_before starts at 0. Since op is '-', candidate is 1-0=1. required_x becomes 1. Then sum_before becomes -1.

Op2: '-'

sum_before is -1. candidate is 1 - (-1) =2. required_x is 2. sum becomes -2.

Op3: '-'

sum_before is -2. candidate is 1 - (-2) =3. required_x is 3. sum becomes -3.

x is max(0,3) =3. sum_before is -3. final =3 + (-3) =0. Correct.

Second example: 4 '++++'

each op is '+'. No '-'s. So required_x remains 0.

sum_before after each op:

0+1=1, then 2, 3,4. sum_before is4.

x is 0. final is 0+4=4. Correct.

Third example: 2 '-+'

Processing first op '-': sum_before 0. candidate 1. required_x=1. sum becomes -1.

Second op '+', sum becomes 0.

x is 1. sum_before is 0. 1+0=1. Correct.

Fourth example:5 '++-++'

Processing each op:

sum_before starts at 0.

Op1 '+': not '-', sum becomes 1.

Op2 '+': sum becomes 2.

Op3 '-': check candidate 1-2= -1. required_x is max(0, -1) remains 0. Then sum becomes 1.

Op4 '+': sum becomes 2.

Op5 '+': sum becomes 3.

sum_before is 3.

x is 0. final 0+3=3. Correct.

So the code works for all examples.

This should handle all cases.

What about the third example:

Input 2 '-+'

sum_before starts at 0.

First op is '-': candidate 1-0=1. required_x=1. sum becomes -1.

Second op is '+': sum becomes 0.

x=1. sum_before 0. final is 1+0=1. Correct.

Another test case where some required_x is negative.

For example, if the sequence is '+-+'.

The '-' is at position 1. sum_before for that op is 1 (sum of first op '+'). So 1-1=0. required_x is 0. sum_before after processing all ops is 1+(-1)+1=1. x=0. final 0+1=1. So initial x is 0, which is allowed. But during the '-' operation, sum_before was 1 (x=0, so 0 + 1 >=1. Correct).

Yes.

So the code is correct.
</think>

```python
n = int(input())
s = input().strip()

sum_before = 0
required_x = 0

for op in s:
    if op == '-':
        candidate = 1 - sum_before
        if candidate > required_x:
            required_x = candidate
    sum_before += 1 if op == '+' else -1

x = max(required_x, 0)
print(x + sum_before)
```