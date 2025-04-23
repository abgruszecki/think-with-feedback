<think>
Okay, let's tackle this problem. So, the problem is about finding the minimum and maximum possible k after adding m people to the benches. The maximum k is straightforward, right? Because to maximize the maximum, we just add all m people to the bench that's already the most crowded. So first, we find the initial maximum bench, add m to it. That's the maximum possible k.

The tricky part is the minimum possible k. We need to distribute the m people in such a way that the largest bench is as small as possible. This sounds like a problem where we want to balance the numbers as much as possible. 

Let's think about how to compute the minimum k. The approach here is to try to level up the benches so that after adding the people, all benches are at or near the same number. So, for example, if all benches are at the same level, adding people would spread them out. 

Let's consider the initial list of a_i. The first step is to find the initial maximum. Then, we need to distribute the m people such that we increase the benches in a way that minimizes the maximum.

Wait, but how do we model this? Maybe we can think of the problem as trying to fill the benches to a certain level k, and check if m people are sufficient to reach that level. Then, we can binary search for the minimum possible k.

Alternatively, we can calculate the minimum possible k by first raising all benches to at least the current maximum. Then, distribute the remaining people equally.

Wait, perhaps the minimum k is determined as follows:

The initial maximum is max_initial. All the m people can be distributed to bring up other benches to at least max_initial, but if m is enough to do that. Then, the remaining people can be distributed by adding one to each bench until there are no more people left. So, the minimum k would be max_initial + (remaining_people) // n + ((remaining_people) % n != 0).

Wait, let's think step by step.

Suppose after initial steps, we have all benches at some level. Let's say the current maximum is current_max. For each bench with a_i less than current_max, we can add (current_max - a_i) to make it current_max. But maybe after that, we can distribute the remaining people. But perhaps the minimal k is determined by the initial maximum plus the ceiling of (m_remaining / n), where m_remaining is the m minus the sum of the required to bring all benches up to the initial maximum.

Wait, but maybe the initial maximum is not the limiting factor. For example, if after distributing some people to other benches, the current maximum increases, but it's possible to distribute the m in a way that allows a lower k.

Alternatively, let's take an example. Let's say the initial a_i are [1,1,1,1], m=6. The initial max is 1. To minimize the new max, we need to distribute 6 people. Each bench can get 1.5 more. But since people are integers, we can split them as evenly as possible. So adding 6 people to 4 benches: each gets 1.5, but since it's 6, each gets 1.5, but since we can't split, it's 2 added to two benches and 1 added to the other two. So the max would be 1+2=3. Which is the example given.

So the minimal possible k is the initial maximum plus the ceiling of (m_remaining / n), but only after ensuring that all benches are at least that initial maximum. Wait, but in that example, the initial max is 1. So the first step is to bring all benches up to 1 (which they already are). Then, the remaining 6 people can be distributed as 6 /4 = 1.5. So each bench gets 1 or 2. The total added is 6. So the maximum per bench is 1 + 2 = 3.

So the minimal possible k is the initial maximum plus (m // n) if m is exactly divisible by n, else (m//n) +1. Wait, but that's only if after bringing all benches up to the initial max, there's enough m to distribute. So in that example, m=6, after bringing all to 1 (they are already there), distribute 6 people. 6/4 is 1.5. So the ceiling is 2. So 1+2=3.

Another example: let's take the third input.

Input 3:

3 benches, 6 people.

Initial a_i: 1,6,5.

Initial max is 6. So the maximum possible k is 6+6=12 (since all m go to the 6 bench).

For the minimal k, we have to distribute the 6 people such that the maximum is as small as possible.

Wait, how?

The initial a_i are [1,6,5]. The current maximum is 6.

So to minimize the new maximum, perhaps we can first fill up the lower benches. The first bench is 1. We can add 5 people to bring it to 6 (so 5 added). Then the third bench is 5. Add 1 to make it 6. Now, all benches are at 6, and 5+1 =6 used. Wait, 5+1=6. So all m=6 are used. So the max is 6. Which is the sample output's minimum k.

So in this case, after bringing all benches up to the initial max (6), we need 5 (for the first bench) and 1 (for the third), sum 6. Which uses all m. So the new max is 6. 

So the minimal k here is 6.

But wait, in this case, the initial max is 6, and the m is exactly the sum needed to bring all benches to 6. So the minimal k is 6.

So how do we compute the minimal k?

The approach is:

The minimal possible k is the maximum between:

a) the initial maximum a_i (if all m can be used to fill the other benches to this level, and then there's some remaining, which would increase the max further), or 

b) the initial maximum plus the ceiling of (remaining_people / n) after filling all benches to the initial maximum.

Wait, let's formalize this.

Compute the sum needed to bring all benches up to the current maximum. For each a_i < current_max, sum += (current_max - a_i). Let's call this required.

If m <= required: then, even after distributing m people, the maximum remains the current maximum. But that's not possible. Because if the required is the sum to bring all benches to current_max, but m is less than required, then after distributing m people, some benches will be increased, but not all. The maximum could still be the current_max. Wait, but maybe some benches are increased but not to the current_max. Hmm, no. For example, initial max is 6. One bench is at 1. required is 5. If m is 3, then after adding 3 to that bench, it's 4. The max is 6. So even if m is less than required, the max remains the initial maximum. So the minimal k would be the initial maximum in that case.

Wait, but how?

Wait, the minimal k in this scenario would be the initial maximum, since even after distributing m people (as much as possible to the lower benches), the maximum remains the initial maximum.

So the minimal k is the maximum between the initial maximum and (the minimal possible when m is larger than required).

So the algorithm is:

1. Compute the initial maximum (max_initial).

2. Compute the required sum (required) to bring all benches up to max_initial. That is sum (max_initial - a_i for each a_i in a).

3. If m <= required:

   Then, we can distribute m people to the benches in a way that none of the benches exceed max_initial. Because even after adding all m people, we can't fill all the required spots (since m < required). So some benches would still be below max_initial, and the maximum remains max_initial. So the minimal possible k is max_initial.

   Wait, but is that possible? Let's say m is 5 and required is 6. We can add 5 to the bench that needs 5 (so it becomes 6), and then the other benches. But wait, maybe we can't distribute in a way that none of the benches exceed max_initial. Hmm, perhaps not. Wait, required is the sum needed to bring all benches up to max_initial. So if m is less than required, then even after distributing m people as much as possible to the lower benches, the maximum will still be max_initial, because no bench is filled beyond that.

So in this case, the minimal k is max_initial.

If m is greater than required:

   Then, after filling all benches to max_initial, we have m_remaining = m - required.

   These m_remaining people must be distributed as evenly as possible among all benches (since adding them to any bench will increase the max). So the minimal possible k is max_initial + (m_remaining // n) + (1 if m_remaining % n != 0 else 0).

So, in code:

min_k = max(max_initial, (max_initial + (m_remaining + n - 1) // n)) if m > required else max_initial.

Wait, no. Let's think again.

If m <= required: min_k is max_initial.

Else:

sum_needed = required.

m_remaining = m - sum_needed.

each of the n benches will get m_remaining // n people. But since we can distribute the m_remaining people equally, the minimal possible maximum is max_initial + (m_remaining // n) plus 1 if there's a remainder.

So min_k = max_initial + (m_remaining // n) + (1 if m_remaining % n else 0).

So the minimal possible k is the maximum between the initial maximum and this value, but since after distributing sum_needed, the initial maximum is already the same, adding m_remaining people will spread them, but the new max will be the initial max plus (m_remaining//n + (1 if remainder else 0)).

So the code steps:

Compute max_initial = max(a)

required = sum(max_initial - x for x in a)

if m <= required:

   min_k = max_initial

else:

   m_remaining = m - required

   min_k = max_initial + (m_remaining // n) + (1 if m_remaining % n !=0 else 0)

So that's the formula for the minimal k.

And the maximum possible k is max_initial + m (since all m are added to the initial max bench).

Wait, not exactly. Because the initial max may not be the only one. Suppose there are two benches with a_i=5. The initial max is 5. So adding m=10 people to any of them. So the maximum possible k is 5 + 10=15. But if you add 5 to each, each becomes 10, which is same. But the maximum possible is when all 10 are added to one bench: 5+10=15.

So yes, the maximum possible k is (initial max) + m.

So the code for maximum k is max_initial + m.

Wait, but wait. Suppose in the input, the initial a_i's maximum is 6. Then adding m=7. So the max possible is 6+7=13.

Yes, like in the third example:

Third sample input:

3

6

1

6

5

The initial max is 6. So max possible is 6+6=12. Which matches the output.

So the max possible is indeed (initial max) + m.

So, putting it all together.

Now, how to code this.

First, read n, m.

Then read the a_i list.

Compute max_initial = max(a_i).

Compute required = sum(max_initial - x for x in a_i).

Then:

max_k = max_initial + m

if m <= required:

   min_k = max_initial

else:

   m_remaining = m - required

   min_k = max_initial + (m_remaining // n) + (1 if m_remaining % n else 0)

Then output min_k and max_k.

But wait, let's test this with some examples.

First example:

Input:

4

6

1 1 1 1

max_initial is 1.

required is sum(1-1 for each, which is 0).

So m is 6 > required (0). So m_remaining =6.

min_k = 1 + (6 //4) + (1 if 6%4 !=0 else 0) → 6//4=1, 6%4=2, so +1. So 1+1+1=3. Which is correct.

Second example:

1

10

5

max_initial =5. required=0. m_remaining=10. 10//1=10. 5+10=15. Which is correct.

Third example:

3

6

1,6,5.

max_initial is 6. required is (6-1)+(6-6)+(6-5) =5+0+1=6. m=6 equals required. So min_k is 6. Max_k is 6+6=12. Correct.

Fourth example:

3

7

1,6,5.

max_initial=6. required=5+0+1=6. m=7>6. m_remaining=1.

So min_k=6 + (1//3) + (1 if 1%3 else 0). 1//3=0, 1%3=1. So 6+0+1=7. Which is correct.

Another test case: let's say n=3, m=5, a = [3,3,3]. So required is 0. m_remaining=5. 5//3=1, remainder 2. So min_k=3 +1 +1=5. Because adding 5 people: two benches get 2, one gets 1. So max is 3+2=5. Correct.

Another example: n=2, m=3, a=[1, 2]. initial max is 2. required= (2-1)+(2-2) =1. m=3>1. m_remaining=2. So 2//2=1, no remainder. So min_k=2 +1=3. So distribute the 3: first, required 1 (to bring first bench to 2). Then 2 more people. Add 1 to each bench. Now benches are 3 and 3. Max is 3.

So code seems correct.

So the code steps are:

Read n.

Read m.

Read n lines of a_i.

Compute max_initial.

Compute required.

Then compute min_k and max_k as per the logic.

So code in Python:

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    m = int(input_stream.readline().rstrip("\n"))
    a = [int(input_stream.readline().rstrip("\n")) for _ in range(n)]
    max_initial = max(a)
    required = sum(max_initial - x for x in a)

    if m <= required:
        min_k = max_initial
    else:
        remaining = m - required
        min_k = max_initial + (remaining // n) + (1 if remaining % n !=0 else 0)

    max_k = max_initial + m

    print(f"{min_k} {max_k}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
7
1
6
5
""",
            "output": \
"""\
7 13
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

Yes.

Another test case: n=2, m=3, a=[2,3]. initial max is 3. required =3-2 +3-3 =1. m=3>1. remaining=2. 2//2=1. no remainder. min_k=3 +1=4. Then the max is 3+3=6. Output 4 6. Which is correct.

Yes.

So the code should work.

Now, considering the constraints. n can be up to 100, which is manageable. m up to 1e4. The code runs in O(n) time, which is acceptable.

Memory usage is minimal. So this code should pass all test cases.
</think>

```python
n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
max_initial = max(a)
required = sum(max_initial - x for x in a)

if m <= required:
    min_k = max_initial
else:
    remaining = m - required
    min_k = max_initial + (remaining // n) + (1 if remaining % n else 0)

max_k = max_initial + m

print(f"{min_k} {max_k}")
```
