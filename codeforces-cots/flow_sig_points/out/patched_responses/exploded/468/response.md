<think>
Okay, let's try to understand this problem. So Grandma Laura sold apples to n buyers. Each time a buyer comes, they take half of the apples she has, and if the number was odd, she gives an additional half as a gift. The cost per apple is p (which is even), and we need to calculate the total money she should have. 

The key here is to reverse the process. Because starting from the end, when she has zero apples, we can work backwards to find out how many apples she had before each transaction. Then, for each step, calculate how much money was earned and sum it all up.

Let me think about the example. The first example has n=2, p=10. The buyers are 'half' and 'halfplus'. The output is 15. Let's see:

Start with 2 apples. First buyer takes half (1 apple), pays 10*1 =10. Then the next buyer takes half (0.5 apple) but since it's odd (1 apple before sale?), wait, maybe I'm confused. Wait, the first example's note says she started with two apples. The first buyer took half (1 apple), paid for 1, then the second took half (0.5 of the remaining 1). But since after the first sale, there was 1 apple left. For the second buyer, since the current apples were 1 (odd), she gives a half as a gift. Wait, wait. The process is: for each buyer, she has a certain number of apples. Then, the buyer takes half of them, and if the original number was odd, she gives an extra half (which makes the total taken by the buyer half plus 0.5). But the original number must be such that after taking half (rounded down?) plus maybe the half, she ends up with zero?

Wait, the problem statement says that each buyer took some integral positive number of apples. Wait, but the problem says that after selling, she has zero. So maybe the way it works is:

For each step:

Let x be the number of apples before the buyer.

If x is even: the buyer takes x/2 apples. She has x/2 left.

If x is odd: the buyer takes x//2 + 0.5 (since she gives a half as a gift). But how can that be an integer? Because the note says in the first example, the second buyer took half (0.5) and the gift half. But maybe the way it's modeled is that the actual apples are handled in such a way that after each step, the number is divided by 2, but if odd, you subtract (x+1)/2, leading to (x-1)/2 left?

Hmm, perhaps the correct way is to model the process backwards. Let's think in reverse. Let's say that after the last buyer, she has 0 apples. We can work backwards step by step to find the initial number of apples. Then, for each step, we can compute the money earned.

Because when you reverse the steps, each step's previous state can be determined based on the current state and whether there was a 'halfplus' in the current step.

Let me see. For each buyer, starting from the last to the first:

If the current buyer's action is 'halfplus', then before she sold to this buyer, the number of apples (let's call it prev) must be odd. Because when she sells to this buyer, she gives halfplus. So when reversed, the next step after this transaction is the current state. For example, suppose after selling to a buyer, she has zero apples. Then, before selling, she had x apples. When the buyer took half, plus a half (if x was odd), leading to zero. So for 'halfplus' in the last step, x must be 1, because (1 // 2) gives 0.5 (assuming integer division), but since x was odd, she gave halfplus. Wait, maybe the way to model it is:

Suppose after a transaction, she has y apples. Then, the previous number of apples (before this transaction) is x.

If the transaction was 'half', then x must be even, and y = x/2. Because the buyer took x/2, leaving y = x/2.

If the transaction was 'halfplus', then x must be odd. The buyer took (x+1)/2 (because x is odd, so (x//2) is (x-1)/2, but then she gives a half, so total taken is (x-1)/2 + 0.5 = (x)/2. But wait, this is confusing. Let me think again.

Wait, when she sells to a buyer, the buyer takes half of the apples, but if the number of apples is odd, then she gives an extra half as a gift. So the total apples taken by the buyer is (x + 1) / 2, and the apples remaining are (x - (x + 1)/2) = (x-1)/2. But (x must be odd here). Because (x +1)/2 is an integer only when x is odd. For example, x=3: (3+1)/2=2. So she gives 2 apples to the buyer, and has 1 left. Wait, but the problem says that she ends up with zero. So in the last step, after selling to the last buyer, she has zero. So for the last buyer, the transaction must result in zero.

Wait, let's model the process forwards. Let's take the first example:

n=2, p=10.

Buyer 1: 'half' → she had x apples. She sold x/2, so remaining x/2. Then buyer 2: 'halfplus' → she had x/2 apples. Since it's a halfplus, x/2 must be odd. So she sold (x/2 +1)/2 (because x/2 is odd). The remaining is (x/2 - (x/2 +1)/2 ) = (x/2 -1)/2. But after that, she has zero. So:

(x/2 -1)/2 = 0 → x/2 -1 =0 → x/2 =1 → x=2. So initial apples were 2.

So buyer 1 took 1 (2/2), paid 1 * p/2? Wait, no. Wait, the cost per apple is p. But each buyer pays for the apples they took, not including the gift. So in the first step, the buyer took 1 apple (half of 2), paid 1 * p. Then in the second step, the buyer took (1 apple (since 1 is odd) → he takes (1+1)/2 = 1 apple (half of 1 is 0.5, but she gives an extra half as a gift. So total taken is 0.5 + 0.5 = 1 apple. But since the problem says that each buyer took an integral positive number, that's correct. So the buyer paid for 0.5 apples (the half), but the total is 1 apple (0.5 +0.5 gift). Wait, no. Wait, the problem says:

each of them bought exactly half of the apples she had at the moment of the purchase and also she gave a half of an apple to some of them as a gift (if the number of apples at the moment of purchase was odd). 

So the payment is for the exact half. The gift is an extra half. So the buyer pays for (x/2) apples. But if x was odd, then x/2 is not an integer. Wait, but the problem says that each buyer took some integral positive number. So perhaps the way to model this is that x must be even for 'half' transactions, and odd for 'halfplus' transactions. Because for example, if x is even, then half is x/2, which is integral, and the remaining is x/2. If x is odd, then the buyer takes (x-1)/2 (the floor of x/2) apples, and then the remaining is (x-1)/2. But she gives an extra half, so the total taken by the buyer is (x-1)/2 + 0.5 = x/2. So the amount paid is (x-1)/2 + 0.5 (the half given as a gift?) Wait, no. The problem says the buyer bought exactly half of the apples, and then maybe gave a gift. So the amount paid is for the half. The gift is an extra half. But the problem says that each buyer took some integral positive number of apples. So the total apples taken by the buyer (paid + gift) must be an integer. Let's think:

If x is even: the buyer takes x/2 apples. Paid for x/2. So that's integral. So the money is (x/2)*p.

If x is odd: the buyer takes (x//2) apples (floor division), which is (x-1)/2, and then the gift adds 0.5, so total is (x-1)/2 + 0.5 = x/2. So the total apples taken is x/2. But since x is odd, x/2 is a half-integer, but adding the gift makes it integer. Wait, this seems contradictory. For example, x=3. Then, the buyer takes 1 (3//2=1) apples, and the gift is 0.5. So total taken is 1.5 apples. But the problem says that each buyer took an integral positive number. That can't be. So perhaps the model is:

When the number of apples is even, the buyer takes half, which is integer. Remaining is half. When the number is odd, the buyer takes (x+1)/2 apples (so that after taking, the remaining is (x-1)/2, which is integer). But how?

Wait, perhaps the correct way to model it is:

Let x be the current number of apples.

For a 'halfplus' transaction:

The buyer takes (x + 1)/2 apples, and the remaining is (x - (x + 1)/2) = (x -1)/2.

But (x +1)/2 is integer only when x is odd. So 'halfplus' indicates that x was odd, and the buyer took (x +1)/2. The money paid is (x/2) apples, because the half is x/2 (but x is odd, x/2 is 0.5, and the gift is 0.5). So the total paid is (x//2) * p + (0.5)*p? No, because p is the price per apple, so she is paid for half an apple when x is odd. But that's not possible, as money can't be a fraction. Wait, but the problem says the total money should be an integer. For example, in the first sample, the total is 15. Let's see:

First buyer takes half of 2 apples (1 apple), pays 1 * 10 =10. Second buyer takes half of 1 apple (0.5) plus 0.5 as a gift. So paid 0.5 *10 =5. Total 15. So the money is summed as the sum of (x_i/2) * p for each step, where x_i is the number of apples before each transaction.

But x_i/2 can be a fraction. But in the first sample, 10 + 5 =15, which is allowed. So the total money can be a sum of fractional p multiplied by the respective halfs, but since p is even, each term is (x_i/2)*p is an integer. Because p is even, (x_i/2) can be integer (if x_i is even) or a half-integer (if x_i is odd). But when multiplied by even p, (half-integer * even) is integer. For example, 0.5 * 10 =5, which is integer. So all the terms in the sum are integers, and the total sum is also an integer.

So the approach is: for each step, calculate how much money was paid (x_i /2 * p), sum all these amounts.

So the problem reduces to:

We need to find the initial number of apples, then for each step, compute x_i, add x_i/2 * p to the total, and then proceed.

But how do we compute x_i for each step?

The key is that after processing all buyers, the number of apples is zero. So we can model this backwards. Starting from the end (after last buyer, x_{n} =0), compute the x_{n-1}, x_{n-2}, ..., x_0 (initial).

Let me model this:

Let's process the transactions in reverse order.

We start with the last transaction. After this transaction, apples are zero. So before the last transaction (x), the number of apples must have been x, and after selling to the buyer, the apples are zero.

So for the last buyer's action:

If the action is 'halfplus', then x must have been odd. Because the buyer took (x+1)/2 apples. After that, the remaining is (x - (x+1)/2) = (x-1)/2. But after the last transaction, the remaining is zero. So (x-1)/2 must equal zero → x-1=0 → x=1. So in this case, x was 1. The money contributed is (1/2)*p = 0.5 * p, but since p is even, this is p/2, which is integer. For example, p=10 → 5.

If the last action is 'half', then x must have been even, and after selling, x/2 apples remain. But since after the last step there are zero apples, x/2 must be zero → x=0. But that's impossible because the buyer must have taken half of x (which would be zero, but the buyer must take a positive integer). So the last action cannot be 'half' because that would imply x was zero before the transaction. So the last action must be 'halfplus', which gives x=1. Which makes sense, because the first example ends with a halfplus.

So for each step in reverse:

We can model the previous x as follows. Let current x be the number of apples after the transaction. So for each transaction in reverse order (starting from the end), we compute the x before the transaction.

For example, processing the transactions from the end to the start:

If the current transaction is 'halfplus', then the x_before (before the transaction) must be 2 * current_x +1. Because:

After the transaction, x_after = (x_before -1)/2 (since x_before was odd, and the buyer took (x_before +1)/2).

So x_after = (x_before -1)/2 → x_before = 2 * x_after +1.

If the transaction is 'half', then x_before is even, and x_after = x_before /2 → x_before = 2 * x_after.

So, starting from x=0 (after the last transaction), we process each transaction in reverse order, updating x to x_before.

Then, once we have all x_i (the apples before each transaction), we can calculate for each transaction the money contributed, which is (x_i / 2) * p. Sum all these to get the total.

Yes, this seems like the correct approach. So the steps are:

1. Reverse the list of buyers' actions.

2. Initialize x =0 (after last transaction).

3. For each action in reversed list:

   a. if action is 'halfplus', then x_before = 2 * x +1.

   b. if action is 'half', x_before = 2 * x.

   c. add (x_before // 2) * p to the total (since for 'halfplus' x_before is odd, so x_before//2 is (x_before-1)/2, but the money is (x_before / 2) * p. Because for x_before odd, (x_before /2) is (x_before-1)/2 + 0.5, which when multiplied by even p gives (x_before-1)/2 * p + 0.5*p. Since p is even, 0.5*p is integer. So (x_before//2) * p is (x_before-1)/2 * p. Then adding 0.5*p (from the 0.5 of x_before/2) gives (x_before//2)*p + (p//2). Wait, maybe I'm getting confused here.

Wait, the money for each transaction is (number of apples the buyer paid for) multiplied by p. The buyer paid for exactly half of the apples available before the transaction. So the money is (x_i / 2) * p. But x_i could be even or odd.

But since x_i is computed in reverse, let's see:

For example, when action is 'halfplus', x_before is odd. So x_before /2 is (x_before-1)/2 + 0.5. So the money is (x_before/2) * p = ( (x_before-1)/2 + 0.5 ) * p = (x_before-1)/2 * p + 0.5p. Since p is even, 0.5p is an integer (as p is even, say p=10 → 5). So the total for this step is an integer.

Alternatively, when processing in reverse, for each step, the money is (x_before / 2) * p. But when processing in reverse, x_before is the number of apples before the transaction. So for each transaction, the money is (x_before // 2) * p + (if 'halfplus', add p//2).

Wait, perhaps not. Let's take the first example. The reversed list of actions is ['halfplus', 'half'].

Start with x=0.

First action (originally the last) is 'halfplus' → x_before = 2*0 +1=1. Money for this transaction is (1/2)*10=5. Then x becomes 1.

Next action is 'half' → x_before = 2*1=2. Money is (2/2)*10=10. Sum is 5+10=15. Correct.

So when processing each step in reverse, the x_before is the apples before the transaction, and the money is (x_before / 2) * p, which can be a half-integer multiplied by even p, but the result is integer.

So, during the reverse processing, for each transaction, after computing x_before, we can compute (x_before * p) // 2. Because x_before can be even or odd. For example, x_before=1 → 1*10//2=5. x_before=2 → 2*10//2=10.

So the algorithm is:

Initialize total=0, x=0.

Process the actions in reverse order:

for action in reversed(actions):

   if action is 'halfplus':

       x_before = 2*x +1

       money = (x_before * p) // 2

   else:

       x_before = 2*x

       money = (x_before * p) // 2

   total += money

   x = x_before

At the end, the total is the answer.

Yes, this seems correct. Because in each step, x_before is the number of apples before the transaction, and the money is (x_before /2)*p. Since x_before can be even or odd, but (x_before *p) is even (if x_before is even, then even * p (even) is even. If x_before is odd, then p is even, so odd * even is even. So (x_before *p) is even, divided by 2 gives integer.

So this approach works.

Now, let's test the first example.

Sample 1:

n=2, p=10.

actions are ['half', 'halfplus'].

Reversed actions are ['halfplus', 'half'].

Processing:

x starts at 0.

First action is 'halfplus':

x_before = 2*0 +1=1. money = (1 *10)//2=5. total=5. x becomes 1.

Second action is 'half':

x_before=2*1=2. money= (2*10)//2=10. total=15. x becomes 2. 

Sum is 15. Correct.

Sample 2:

n=3, p=10.

All actions are 'halfplus'.

Reversed actions are ['halfplus', 'halfplus', 'halfplus'].

Processing:

x=0.

First action (third in original) is 'halfplus' → x_before=1 → money 5. total=5. x=1.

Second action (second in original) → x_before=2*1+1=3 → money (3*10)/2=15 → total 20. x=3.

Third action (first in original) → x_before=2*3+1=7 → money (7*10)/2=35 → total 55. x=7.

Sum 5+15+35=55. Correct.

So this approach works.

Now, the code.

We can read n and p. Then read n lines, store them in a list. Reverse the list. Then process each action in the reversed list, tracking x and total.

In Python, since n can be up to 40, and each step doubles x (or so), the maximum x can be up to 2^40, which is manageable as Python's integers can handle arbitrary sizes.

The code steps:

Read n and p.

Read the next n lines, collect in a list.

Reverse the list.

Initialize x =0, total=0.

For each action in reversed list:

   if action is 'halfplus':

       x = 2*x +1

   else:

       x = 2*x

   total += (x * p) //2

Wait, no. Because x_before is computed as 2x +1 (for 'halfplus') or 2x (for 'half'). Wait, no. Wait, the code steps for reverse processing are:

For each action in the reversed list (i.e., processing from last to first):

   current_x = x (which is the state after the transaction, which is the previous state in the original order).

   compute x_before based on the action and current_x.

   add (x_before * p) //2 to total.

   set x to x_before (because in the next step, this x_before is the x_after of the previous transaction in original order).

Wait, let's think again. Let's say the reversed actions are [a_n, a_{n-1}, ..., a_1]. The original order is a_1, a_2, ..., a_n.

Processing in reverse order, we start with x=0 (after a_n). Then, for each a_i in reversed list (starting with a_n), compute x_before (the x before a_i's transaction). Then, for the next a_i, which is a_{n-1} in reversed list, the x is x_before (the x after a_{n-1} transaction in original order).

Wait, perhaps the code steps are:

Initialize x_after =0.

For each action in reversed list (original last to first):

   compute x_before based on action and x_after.

   compute the money from this transaction: (x_before * p) // 2.

   add to total.

   x_after = x_before.

So, code:

actions = list of n strings, reversed.

total =0

x =0

for action in reversed_actions:

   if action == 'halfplus':

       x_before = 2 * x +1

   else:

       x_before = 2 *x

   total += (x_before * p) //2

   x = x_before

Yes. Because the first iteration (for the last action in original order) computes x_before as the apples before the last transaction. Then, the next iteration handles the previous transaction (original order), etc.

So in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, p = map(int, input_stream.readline().rstrip("\n").split())

    actions = [input_stream.readline().rstrip("\n").strip() for _ in range(n)]

    actions_reversed = reversed(actions)

    total =0

    x =0

    for action in actions_reversed:

        if action == 'halfplus':

            x_before = 2 * x +1

        else:

            x_before = 2 *x

        total += (x_before * p) //2

        x = x_before

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 10
halfplus
halfplus
halfplus
""",
            "output": \
"""\
55
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

Sample 2:

Reversed actions are 3 'halfplus's.

First iteration:

action is 'halfplus', x=0 → x_before=1. total += (1*10)/2=5. x=1.

Second iteration: action 'halfplus', x=1 → x_before=3. total += 15 → total 20. x=3.

Third iteration: action 'halfplus', x=3 → x_before=7. total += 35 → total 55. x=7.

Yes, correct.

So the code is correct.
</think>

```python
n, p = map(int, input().split())
actions = [input().strip() for _ in range(n)]
total = 0
x = 0
for action in reversed(actions):
    if action == 'halfplus':
        x = 2 * x + 1
    else:
        x = 2 * x
    total += (x * p) // 2
print(total)
```
