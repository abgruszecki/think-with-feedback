<think>
Okay, let's see. The problem is about distributing chips to walruses sitting in a circle. Each walrus in order gets a number of chips equal to their position in the sequence, which increases each time around. If the presenter can't give the required number, he takes the remaining and ends it.

So, given n and m, I need to find how many chips are left at the end.

Hmm. Let's think about the steps. Let's take the first example: n=4, m=11. The distribution goes 1,2,3,4, then 1 again. Summing those: 1+2+3+4 =10, then adding 1 makes 11. So exactly used, leaving 0. The output is 0.

Another example: n=3, m=8. The first round is 1+2+3=6. Then next is 1. So 6+1=7. Now remaining is 1. Next walrus is 2, needs 2 chips. But only 1 left. So presenter takes that 1, output is 1.

So the process is: each cycle, the walruses take 1,2,...n chips. Then again 1,2,...n, etc. Wait, no, wait. Wait, the problem says that the walrus number i gets i chips. But in the note for the first sample, after the first cycle (1,2,3,4) the next is 1. So it's like each step in the sequence is 1,2,3,4,1,2,3,4, etc. Each time the next walrus in the circle. But each walrus in the sequence gets their position in the current step. Or wait, no. Wait, the problem says: "the presenter ... starts giving the chips to the walruses starting from walrus number 1 and moving clockwise. The walrus number i gets i chips." Wait, maybe the problem is that the walrus i gets i chips each time it's their turn. Like, the first time around, each walrus 1 to n gets their respective i chips. Then, the next time around, same thing? Or does the required number increase each step?

Wait the problem statement says: "The walrus number i gets i chips." Wait, that's ambiguous. Wait, looking at the note for the first example. The first round gives 1,2,3,4. Then next round gives 1. So each time the presenter goes around, the same walruses get the same number of chips each time. So for each walrus in order 1,2,3,4,1,2,3,4, etc., each time the presenter gives that walrus's number in chips. Wait, that's how the note explains it. So in the first sample, after the first cycle (4 walruses), the next is walrus 1 again, and gives 1 chip. Then m is 11. So total given is 1+2+3+4 +1 = 11.

So each time the walrus is in order 1,2,3,...,n,1,2,3,...,n, etc. And each time the presenter gives i chips to the walrus i. So each time a walrus comes up in the sequence, they get their own number i of chips. So for example, the third sample: n=3, m=8. The sequence is 1 (1), 2 (2), 3 (3), then 1 (1), 2 (2), 3 (3), etc. So each walrus i gets i chips each time they are visited.

Wait, but in the note of the third sample, after 1+2+3=6, then the next is 1, which adds 1, making 7. Then the next is 2, which requires 2. But m is 8, so 7 + 2 would be 9, but m is 8. So after giving 1 to the first walrus in the next round, m is 8-7=1. Then the next walrus is 2, needs 2, but only 1 left. So presenter takes that 1.

So the key is that each walrus in the sequence requires i chips each time it's their turn. So the sequence is 1,2,3,4,1,2,3,4, etc., and each step the required is the walrus's number. So the sum is 1+2+3+4+1+2+3+4+1+... etc., until m is exhausted.

Wait, but that's a problem where the required sum could be very large. But given that m can be up to 1e4, how can we compute this efficiently?

Wait, n can be up to 50, and m up to 1e4. So for each step, the required number of chips is the current walrus's number. Let's model this as a loop. We can process each step, subtracting the required amount from m. But for m up to 1e4, and each step can be up to n (50), the maximum steps would be m/n steps. For m=1e4, n=50, that's 1e4 steps. Which is manageable. Because 1e4 is 10,000 steps, which is acceptable for Python in the given time constraints (2 seconds). So perhaps a simulation approach is feasible here.

But maybe there's a smarter way. Let's think.

The total sum of a full cycle is sum(1..n) = n*(n+1)/2. Let's call this S. Then, the number of full cycles is k, and the remaining chips after that is m_remaining = m - k*S. Then, we can distribute the remaining m_remaining chips in the next partial cycle.

But wait, each step in the cycle is the walrus i, which requires i chips. So the partial sum after full cycles is when we subtract all the full cycles first, then distribute the remaining chips step by step until we can't.

So the approach would be:

1. Compute S = n*(n+1)/2.

2. Find how many full cycles (k) can be done: the maximum k where k*S <= m.

   Then, m_remaining = m - k*S.

3. Now, distribute m_remaining in the next steps: for each walrus i from 1 to n, subtract i from m_remaining as long as m_remaining >= i. If m_remaining becomes less than i, return m_remaining.

But wait, that's not exactly right. Because after the full cycles, the next steps are in the sequence 1, 2, ..., n, but m_remaining might not be enough for all of them. So for example, in the first sample:

n=4, S=10. m=11. Then k=1 (since 1*10=10 <=11). m_remaining=1. Then distributing 1 (walrus 1) gives m_remaining=0. Then the next walrus is 2, which requires 2, but m_remaining is 0. So presenter takes 0.

But in this case, the remaining m_remaining is 1. So in the partial cycle, first walrus 1 takes 1, m_remaining becomes 0, then process ends. So the answer is 0.

In the third sample: n=3, S=6. m=8. k=1 (6*1=6 <=8). m_remaining=2. Then distribute 1 (walrus 1), m_remaining=1. Next walrus 2 requires 2, but 1<2, so the remaining is 1. So answer is 1.

So the steps after full cycles are:

For each i in 1 to n:

   if m_remaining >=i:

       m_remaining -=i

   else:

       return m_remaining

So yes, that's correct.

So the algorithm is:

Compute S = n*(n+1)/2.

k = m // S

remaining = m - k*S

Then, for i in 1..n:

   if remaining >=i:

       remaining -=i

   else:

       break

Then, the answer is remaining.

Wait, but let's test with the third example.

n=3, m=8.

S=6. k=8//6=1. remaining=8-6=2.

Then, first step i=1: 2 >=1 → subtract 1 → remaining 1.

Next i=2: 1 >=2? No. So break. So answer is 1. Which is correct.

Another example: input 17 107.

n=17, m=107. S=17*18/2=153. 107 <153 → k=0. remaining=107. Then iterate from i=1 to 17:

Check how much can be subtracted. Let's compute:

sum from 1 to x where sum <=107.

Find x such that sum_{i=1}^x i <=107.

The sum is x(x+1)/2.

Find x where x(x+1)/2 <=107.

Let's compute:

x=14: 14*15/2=105. 105 <=107. remaining 2. Then next i=15, which is 15. 2<15 → stop. So answer is 2. Which matches the sample.

So this approach works.

So the steps are:

1. Calculate S = sum of 1..n.

2. If S is 0 (n=0, but n>=1 per constraints), no. So S is at least 1.

3. Compute k = m // S. But if S > m, then k=0.

4. remaining = m - k*S.

5. Then, for each i from 1 to n:

   if remaining >=i:

       remaining -=i

   else:

       break

6. The answer is the remaining after this.

So the code can be written as follows:

Read n and m.

Compute S = n*(n+1)//2.

if S ==0: (but n can't be 0).

k = m // S

remaining = m % S → no, because m -k*S is same as m % S only when S divides m. Wait, no. For example, m=11, S=10 → k=1, 11 -1*10=1 → remaining is 1, which is 11%10=1. So yes, remaining is m % S. But wait, if S is 0, which is not possible here.

So remaining = m % S.

Wait, but when S is 0, but n can't be 0. So S is at least 1.

Wait, m % S is the same as m - (m//S)*S. So remaining is indeed m % S.

So in code:

remaining = m % S.

But then, we need to process the remaining as sum 1+2+...+x where sum <= remaining. The remaining after that is the leftover.

Wait, but in the code, how do we process the steps? For example, in the third sample, remaining is 2 (after 107 %153=107). Then, process i from 1 to 17:

We subtract 1 (remaining becomes 1), then i=2: 1 <2 → break. So remaining is 1. So answer is 1. But the sample output is 2. Wait no, the third sample's n=3 and m=8. Oh, wait, in that case, the code would compute S=6, remaining=8%6=2. Then process i from 1 to 3:

i=1: 2>=1 → subtract → 1 left.

i=2: 1 >=2? No → break. So answer is 1, which is correct.

But in the second sample, n=17, m=107. S=153. 107 <153, so remaining=107.

Then, process i from 1 to 17:

sum 1+2+...+14 = 105. remaining is 107-105=2. Then i=15: 2<15 → break. So answer is 2. Which matches the sample.

So yes, this approach works.

But how to compute the sum up to x where sum_{i=1}^x} <= remaining.

So the remaining is m % S. Then, the sum of 1 to x is x*(x+1)/2 ≤ remaining.

We need to find the maximum x where x(x+1)/2 ≤ remaining.

But then, the sum of 1 to x is the maximum possible sum ≤ remaining. Then, subtract that sum from remaining, and the leftover is the answer.

Wait, no. Because in the process, each step is walrus 1, then 2, etc., up to x, and the next walrus x+1 can't be fully given.

So, the remaining after k cycles is m_remaining = m -k*S. Then, in the next steps, we subtract 1, then 2, etc., until we can't subtract more. So the leftover is m_remaining minus the sum of the first x terms where sum is <= m_remaining.

But the sum of the first x terms is x*(x+1)/2. So the maximum x where x*(x+1)/2 ≤ m_remaining. Then, if sum is exactly equal to m_remaining, then answer is 0. Otherwise, the answer is m_remaining - sum.

Wait, but how do we compute x quickly?

Yes. So for example, m_remaining is known, and x is the integer such that x(x+1)/2 ≤ m_remaining < (x+1)(x+2)/2.

So x can be found by solving the quadratic equation x² +x - 2*remaining =0 → x = [-1 + sqrt(1 +8*remaining)] /2. Take the floor.

Once x is found, then the sum is x*(x+1)/2. If the sum equals m_remaining, then the answer is 0. Otherwise, the answer is m_remaining - sum.

But then, after x steps (walruses 1 to x), the next walrus is x+1. So the required amount is x+1. If m_remaining - sum >=x+1 → no, because x is the maximum where sum <= m_remaining. So m_remaining - sum is less than x+1. So the answer is m_remaining - sum.

So the code can be optimized by computing x directly, rather than looping through each i from 1 to n. This is crucial for large n, but given that n is up to 50, and m_remaining can be up to 1e4 (since m is up to 1e4), but even with n=50, the sum after x steps can be up to 50*51/2=1275. Which for m_remaining up to 1e4, x can be up to sqrt(2*1e4) ≈ 141. So x can be up to 140. But since n is up to 50, after x steps, if x is larger than n, but in that case, the sum is sum_{i=1}^x} which is x(x+1)/2. But wait, the process is in the order 1,2,...n, then 1,2,...n again, etc. Wait, no. Wait, no. Because after the full cycles (k), the remaining is distributed in the next round, which is the same as the first cycle. So the next steps are 1, 2, ..., n. So even if x exceeds n, but in the next cycle, after the full cycle of 1 to n, the next steps would be 1 again, but in our problem's context, after the full cycles (k), the remaining is m_remaining = m % S, which is less than S. So when distributing the remaining, we only go through the first cycle's steps (1,2,...n) once. So in the remaining m_remaining, we can distribute to walruses 1, 2, ..., up to x steps where x <=n.

Wait, that's a crucial point. Because the sum of the first cycle is S. The remaining is m_remaining, which is less than S. So during the distribution of m_remaining, the walruses are processed in the order 1, 2, ..., n. So the maximum number of steps is n steps, each step i requires i chips. So x can't exceed n. So in the code, after the full cycles, the remaining m_remaining is processed in the order 1 to n, and stops when the next step's required chips can't be given.

So in this case, for the code, after computing m_remaining = m % S, we can loop i from 1 to n, and subtract each i from m_remaining as long as possible.

But since n is up to 50, this loop is O(n), which for 50 steps is negligible. So even for m_remaining up to 1e4, this loop would take at most 50 iterations. So this is acceptable.

Therefore, the code can be written as follows:

Read n and m.

Compute S = n*(n+1)//2.

remaining = m

if S !=0:

   # Compute how many full cycles: k = remaining // S

   # remaining = remaining % S

   # but since in each cycle, sum S is subtracted.

   # So remaining after full cycles is m % S.

   remaining = m % S

else:

   # S is 0 only when n=0, but n >=1 per constraints.

   pass

Then, for i in 1..n:

   if remaining >=i:

       remaining -=i

   else:

       break

The answer is remaining.

So the code can be written as:

n, m = map(int, input().split())

s = n * (n + 1) // 2

remaining = m % s if s !=0 else m

for i in range(1, n+1):

    if remaining >= i:

        remaining -= i

    else:

        break

print(remaining)

Wait, but when s is 0, which can't happen because n >=1. So s is at least 1. So the code is:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    s = n * (n + 1) // 2

    remaining = m % s

    for i in range(1, n+1):

        if remaining >= i:

            remaining -= i

        else:

            break

    print(remaining, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
17 107
""",
            "output": \
"""\
2
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    s = n * (n + 1) // 2

    remaining = m % s

    for i in range(1, n+1):

        if remaining >= i:

            remaining -= i

        else:

            break

    print(remaining, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 8
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

So the code is correct and efficient.
</think>

```python
n, m = map(int, input().split())
s = n * (n + 1) // 2
remaining = m % s
for i in range(1, n + 1):
    if remaining >= i:
        remaining -= i
    else:
        break
print(remaining)
```
