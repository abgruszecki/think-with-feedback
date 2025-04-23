<think>
Okay, let's try to figure out this problem. So, we need to find the minimum cost to convert string a into string b using swap and flip operations. Hmm.

First, let's understand the operations. Swapping two bits costs the distance between their indices. Flipping a single bit costs 1. So, sometimes it's cheaper to flip two adjacent bits rather than swap them. For example, if two adjacent bits are different from the target, flipping both costs 2, but swapping them costs 1. Wait, but maybe flipping is better in some cases. Wait, for example: if in a, two consecutive bits are '0' and '1', and in b they need to be '1' and '0', swapping them would cost 1 (since they're adjacent), which is better than flipping both (cost 2). So swapping is better here.

But what if the differing bits are not adjacent? Like, if two bits are separated by several positions. Then swapping might cost more than flipping. But then, when to choose which option?

So the problem reduces to handling each position where a and b differ and deciding whether to flip those bits or swap adjacent ones when possible.

Wait, but how do we model this? Let's think about the differences between a and b. Let's create a list of indices where a[i] != b[i]. Then, for consecutive differences, we can decide whether to swap or flip.

Wait, let's go through the example. For the first sample input:

a is 100, b is 001. The differing positions are 0 (a is '1', b is '0') and 2 (a is '0', b is '1'). So two flips would cost 2, which is the same as swapping positions 0 and 2, which costs 2. So both options are equal here.

In the second example: a is 0101, b is 0011. The differing positions are index 1 (a is '1', b is '0') and index 2 (a is '0', b is '1'). Swapping them costs 1, which is better than flipping both (cost 2). So the optimal is to swap.

So the key is to look for consecutive differing positions and see if swapping is cheaper than flipping. But how?

Let's think of processing the differences from left to right. For each position where a and b differ, we can check if the next position also differs, but in a way that swapping would resolve both. For example, if position i and i+1 differ and swapping them would resolve both differences, then the cost is min(2 (flipping both), 1 (swap cost)). So for consecutive differing positions, it's better to swap if possible.

So here's the plan: Iterate through each bit from left to right. When we find a difference at position i, check if the next position i+1 also has a difference, but in a way that a[i] and a[i+1] are the opposite of each other. If so, then swapping them would fix both differences. The cost for this would be 1 (swap cost) versus flipping both (cost 2). So we can choose the swap here, increment the total by 1, and skip the next position. Otherwise, flip the current bit (cost 1).

Wait, but how do we determine if the next position's difference is such that swapping would resolve both? Let's see. Suppose at position i, a[i] != b[i], and at position i+1, a[i+1] != b[i+1]. For swapping to fix both, swapping a[i] and a[i+1] would make both positions match b. So, after swapping, a[i] becomes a[i+1], which must equal b[i], and a[i+1] becomes a[i], which must equal b[i+1]. So that requires that a[i+1] = b[i] and a[i] = b[i+1]. Which is equivalent to (a[i] != a[i+1]) and (b[i] != b[i+1]). Wait, not exactly. Let me think:

Original a at i and i+1: a_i and a_j (j = i+1).
After swap, they are a_j and a_i.
We need a_j == b_i and a_i == b_j. So the required condition is:

a_j == b_i AND a_i == b_j.

But since the original positions i and j (i+1) are in a, and the desired b's positions are i and j.

But this may not always be the case. For example, maybe a_i is 0, a_j is 1. Then after swap, the a becomes 1,0. So if b's i and j are 1 and 0, then swapping works. So in this case, the original a_i and a_j must be the reverse of what's needed for their positions.

So for the current and next positions, if the required bits for b are the reverse of the current a's bits (i.e., a[i] is the value needed for b[i+1], and a[i+1] is the value needed for b[i]), then swapping would resolve both differences. Otherwise, flipping is better.

Wait, but how do we check this? Let's see:

At position i, a[i] != b[i], so desired is to have a[i] changed to b[i]. Similarly for position i+1. So the problem is that these two positions are mismatched. Now, if swapping them would make both positions correct, that's a better option.

So the condition for swap being better is:

a[i] == b[i+1] and a[i+1] == b[i]

In this case, swapping the two bits will fix both positions. Otherwise, flipping is better.

But how do we check this efficiently?

Alternatively, perhaps the problem can be rephrased as: when you have two consecutive differing positions, and the a's bits at those positions are the reverse of what the corresponding b's bits are (i.e., a[i] is supposed to be b[i], but is wrong, and a[i+1] is supposed to be b[i+1], but is wrong, and swapping would make a[i] equal to b[i] and a[i+1] equal to b[i+1]).

So in that case, swapping is better. So for two consecutive differing positions i and i+1, if a[i] != a[i+1], then swapping would cost 1, which is better than flipping both (cost 2). So whenever we have two consecutive differing positions where a[i] and a[i+1] are different, we can handle them with a swap. Otherwise, if a[i] and a[i+1] are the same (both 0 or both 1), then swapping would not help because after swapping, both positions would still be the same as before. So in that case, flipping is required.

Wait, but how? Let's think with an example.

Case 1: a = 01, b = 10. The two positions differ. a[i] is 0 and a[i+1] is 1. Swapping them gives a[i] = 1, a[i+1] = 0, which matches b. So the cost is 1, better than flipping both (cost 2).

Case 2: a = 00, b = 11. Both positions differ. But a[i] and a[i+1] are same. Swapping them doesn't change anything. So you have to flip both, cost 2.

So the key is: when two consecutive differing positions exist, and a[i] != a[i+1], then swapping can be done for cost 1. Otherwise, flipping both (cost 2) is required.

So the algorithm would be:

Initialize total cost to 0.

Iterate over each position i from 0 to n-1:

- If a[i] == b[i], do nothing. Proceed to next i.

- Else (current position i is a mismatch):

   - Check if i+1 is also a mismatch and a[i] != a[i+1].

   - If so, add 1 to the cost, and skip the next position (i += 1).

   - Else, add 1 to the cost, and proceed.

This way, consecutive mismatches where a's bits differ are handled with a swap (cost 1). Otherwise, each is a flip (cost 1 each, but for two consecutive same bits, we add 2).

So for example, in the second sample input:

a is 0101 (indices 0,1,2,3), b is 0011.

Comparing each position:

0: a[0] = 0 == b[0] = 0 → no problem.

1: a[1] = 1 != b[1] = 0. Check next position i+1=2. a[2] is 0 != b[2] (1). So both i and i+1 are mismatches. Check if a[i] != a[i+1]. a[1] is 1, a[2] is 0. So yes. So add 1 to cost, and skip i=2. Then proceed to i=3. a[3] is 1 != b[3] (1) → no. So total cost is 1.

In the first sample:

a=100 (indices 0,1,2), b=001.

i=0: a is 1 != b 0 → mismatch. Check i+1=1. a[1] is 0 which equals b[0] (0). Wait, but after swapping 0 and 2? Oh wait, in the first sample, the code would check i=0. a[0] is 1, which is a mismatch. Then check i+1=1. a[1] is 0. So a[i] (1) and a[i+1] (0) are different. But i+1's a is 0, which is supposed to be 0 (since b[1] is 0). So i+1 is not a mismatch. So the code would not process the next i. So the current i is a single mismatch, add 1 to cost, then proceed to i=1.

At i=1: a is 0, b is 0 → okay. Proceed.

i=2: a is 0 != b's 1 → add 1. Total cost 2.

Which matches the example.

Wait, but according to the code's logic, the two mismatched positions are 0 and 2, which are not consecutive, so each is handled as a flip, cost 1+1=2.

So the code works for that case.

Another example where two consecutive mismatches with a[i] != a[i+1]:

a is 01, b is 10. The code would process i=0, see that a[0] != a[1], so add 1 and skip i=1. Total cost 1.

Another example where a=00, b=11. The code processes i=0 as a mismatch, checks i+1. a[0] is 0, a[1] is 0. So same. So add 1. Then i increments to 1, which is a mismatch again, add another 1. Total cost 2.

So the code seems to handle all cases.

So the plan is:

Loop through each index i. For each i:

If current a[i] == b[i], skip.

Else:

   If i+1 is within bounds and a[i] != a[i+1], and a[i+1] != b[i+1], then:

      add 1 to cost, increment i by 2.

   Else:

      add 1 to cost, increment i by 1.

Wait, but how do we check if i+1 is a mismatch? Because if the next position is not a mismatch, then swapping would not help.

Wait, in the code logic, when we have a mismatch at i, we check if i+1 is also a mismatch and a[i] and a[i+1] are different. Because in that case, swapping would resolve both.

So the code would:

For i in range(n):

   if a[i] == b[i]:

       continue

   else:

       # check if next position exists and is a mismatch and a[i] != a[i+1]

       if i+1 < n and a[i] != a[i+1] and a[i+1] != b[i+1]:

           cost +=1

           i +=1  # skip next position

       else:

           cost +=1

       i +=1

Wait, but when you have a for loop with i in range(n), you can't increment i inside. So perhaps a while loop is better.

So the correct approach would be to use a while loop, starting from i=0, and incrementing i by 1 or 2 depending on whether we process the next position.

So the code would look like:

i = 0

cost = 0

while i < n:

    if a[i] == b[i]:

        i +=1

        continue

    # else, current is a mismatch

    # check if next position is also a mismatch and a[i] != a[i+1]

    if i+1 < n and a[i] != a[i+1] and a[i+1] != b[i+1]:

        cost +=1

        i +=2

    else:

        cost +=1

        i +=1

This way, for each position, we handle it as a single flip or pair with a swap.

But wait, the condition for the next position is that a[i] != a[i+1], and that the next position is also a mismatch. So for example, if a[i] is 0, a[i+1] is 1, and both are mismatched. Then swapping them would resolve both, cost 1.

So this logic should cover all cases.

Now, let's test this logic against the examples.

First example:

n=3

a = 100 → indexes 0:1, 1:0, 2:0

b = 001 → indexes 0:0, 1:0, 2:1

Processing:

i=0: a[0] (1) != b[0] (0). Check i+1 (1) is in range. a[i+1] is 0. So a[i] != a[i+1] (1 vs 0). But a[i+1] (0) equals b[i+1] (0). So the next position is not a mismatch. So the condition (a[i+1] != b[i+1]) is false. So we do not take the swap path. So add 1 to cost (now cost=1), increment i to 1.

i=1: a[1] == b[1]. Skip, i becomes 2.

i=2: a[2] (0) != b[2] (1). Check i+1 (3) is out of range. So add 1 (cost=2). Increment to 3, loop ends.

Total cost 2. Correct.

Second example:

n=4

a=0101 → indexes 0:0,1:1,2:0,3:1

b=0011 → indexes 0:0,1:0,2:1,3:1.

Processing:

i=0: a[0] is 0 == b[0], so i increments to 1.

i=1: a[1] (1) != b[1] (0). Check i+1=2. a[i+1] is 0, which is different from a[i] (1). Also, check if a[i+1] (0) != b[i+1] (1). Yes. So the condition is met. Add 1 to cost (now 1), increment i to 3.

i=3: a[3] is 1 == b[3]. So i becomes 4. Loop ends. Total cost 1. Correct.

Another test case: a=01 → b=10. i=0: a[0] is 0 != 1. i+1=1: a[1] is 1 != 0. a[0] and a[1] are different. So add 1, i becomes 2. Total cost 1. Correct.

Another test case: a=00, b=11. i=0: a[0] is 0 != 1. Check i+1=1. a[1] is 0 != 1. a[i] == a[i+1] (0 ==0). So condition (a[i] !=a[i+1]) is false. So process current as a flip. cost becomes 1, i increments to 1. Now, a[1] is 0 !=1. Check i+1=2 (out of range). Add 1. Total cost 2.

Yes.

So the logic works.

Now, how to implement this efficiently in Python?

The constraints are up to 1e6 characters, so the code must process this in O(n) time and O(1) space (since we can process the strings as we read them, without storing anything else except the current and next positions).

But in Python, strings are immutable, so we can process them by iterating through each character using indices.

So the code would read n, then a and b. Then process the two strings as per the logic.

So code steps:

Read n.

Read a and b.

Initialize cost to 0.

Loop through i from 0 to n-1:

   if a[i] == b[i], continue.

   else:

       if i+1 < n and a[i] != a[i+1] and a[i+1] != b[i+1]:

           cost +=1

           i +=1

       else:

           cost +=1

So the code would use a while loop with i starting at 0, and incrementing by 1 or 2.

Yes.

So the code in Python would look like this:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = input_stream.readline().rstrip("\n").strip()
    b = input_stream.readline().rstrip("\n").strip()

    cost = 0
    i = 0
    while i < n:
        if a[i] == b[i]:
            i += 1
            continue
        # Current is a mismatch
        if i + 1 < n and a[i] != a[i+1] and a[i+1] != b[i+1]:
            cost += 1
            i += 2
        else:
            cost += 1
            i += 1
    print(cost, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
0101
0011
""",
            "output": \
"""\
1
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

Second sample:

4

0101

0011

Processing:

i=0: a[0] == b[0] → i becomes 1.

i=1: a[1] is '1' != '0'. Check i+1=2. a[2] is '0' (a[i] is 1, a[i+1] is 0 → different). a[i+1] (0) != b[i+1] (1). So condition met. cost +=1 (1). i becomes 3.

i=3: a[3] is '1' == '1' → i becomes 4. Done. Output 1.

Yes.

Another test case where two consecutive mismatches but a[i] == a[i+1]:

a=00, b=11.

Processing:

i=0: a[0] is 0 != 1. Check i+1=1. a[1] is 0 (so a[i] == a[i+1]). So condition fails. cost +=1 (1), i becomes 1.

i=1: a[1] is 0 !=1. Check i+1=2 (out of bounds). cost +=1 (2). i becomes 2. Output 2.

Another test case where two consecutive mismatches but a[i] != a[i+1], but the next position's a is correct:

a=01, b=00.

Processing:

i=0: a[0] is 0 == 0. i becomes 1.

i=1: a[1] is 1 != 0. Check i+1=2 (out of bounds). cost +=1. Output 1.

So the code handles that.

So this code should be correct.
</think>

```python
n = int(input())
a = input().strip()
b = input().strip()

cost = 0
i = 0
while i < n:
    if a[i] == b[i]:
        i += 1
        continue
    if i + 1 < n and a[i] != a[i+1] and a[i+1] != b[i+1]:
        cost += 1
        i += 2
    else:
        cost += 1
        i += 1
print(cost)
```
