<think>
Okay, let's see. The problem is to find the minimum cost for Ann to make n subway rides, given the options of buying single-ride tickets or m-ride tickets which might be cheaper per ride. Hmm.

So the inputs are n, m, a, b. The goal is to compute the minimum cost. Let's think about possible scenarios here.

First, the straightforward approach would be to compare the cost of buying all single tickets versus a combination of m-ride tickets and some single tickets if needed. But maybe there's a smarter way.

Let me break it down. For each possible number of m-ride tickets she buys, we can calculate how many rides are left and then compute the cost for those. Then pick the minimum among all possibilities.

Wait, but how many m-ride tickets can there be? Well, if Ann needs n rides, then the number of m-ride tickets could be from 0 up to (n // m) + 1. Because even if n is not a multiple of m, buying one extra m-ride ticket might be cheaper than buying the remaining single tickets.

For example, in the first sample input: 6 rides, m=2. Buying 3 m-tickets (each 2 rides) gives 3*2=6 rubles, which is the same as buying 6 singles (6*1=6). So in that case, both options are possible.

Another example: suppose n=5, m=3. Then if she buys 1 m-ticket (3 rides), she has 2 left. So the cost is b + 2*a. But maybe buying 2 m-tickets (6 rides) would cost 2*b, which might be cheaper than b + 2a. So we need to compare these possibilities.

So the approach here is to consider all possible numbers of m-ride tickets. For each possible k, where k can be 0, 1, ..., up to (n + m -1) // m (ceiling division). Because if n is not exactly divisible by m, then the ceiling of n/m would give the number of m-ride tickets needed if we take that approach. For example, n=5 and m=2: 5/2=2.5, ceiling is 3. So buying 3 m-ride tickets covers 6 rides, which is more than enough, but maybe cheaper.

Wait, but how to compute k. Let's see: the required number of m-ride tickets to cover exactly the remaining rides would be (n // m), and then possibly one more if there's a remainder.

Wait, but for each possible k, the total rides covered by m-ride tickets would be k * m. The remaining rides would be max(0, n - k*m). Wait, no. Because if k*m >=n, then the remaining is 0. Otherwise, it's n -k*m. Wait, but if you have k m-ride tickets, they can be used for up to k*m rides. So the total rides would be the minimum between k*m and n? No, perhaps not. Because the m-ride tickets can be used for any rides, even if you have more tickets than needed. For example, if you have 5 rides and buy 3 m-ride tickets (m=2), then you can use 3*2=6 rides, but you only need 5. So the cost is 3*b. Which might be better than 2*b + 1*a (if 3b < 2b +a).

So the steps would be:

1. Calculate the maximum possible number of m-tickets that could be considered. That would be (n + m -1) // m. Because if n is not divisible by m, (n//m) gives the integer division, but adding m-1 and then dividing by m gives the ceiling. For example, 5/2=2.5 → (5 +2-1)/2=6/2=3.

But perhaps considering k up to that maximum is sufficient. For each k from 0 to that maximum, compute the cost as k*b + max(0, n -k*m)*a. Wait, no. Because if k*m is larger than n, then the remaining rides are zero. So the cost is k*b. So the formula would be k*b + max(0, (n - k*m)) * a. Wait, no. Because if k*m >=n, then the remaining is zero. But if k*m <n, then you need (n -k*m) single rides.

So the cost for each k is (k * b) + (max(0, n -k*m) * a). But wait, if k is such that k*m >=n, then the second term is zero. So the total is k*b.

So for each possible k (from 0 up to the ceiling of n/m), compute the cost and choose the minimum.

But also, there's another case. Suppose it's cheaper to buy some m-ride tickets plus some single tickets. For example, if a single ride is cheaper per ride than the m-ride ticket, then buying the m-ride tickets when possible and then singles for the remainder would be optimal.

Wait, but the m-ride ticket's per-ride cost is b/m. If that's cheaper than a, then it's better to buy as many m-ride tickets as possible. But if a is cheaper than b/m, then it's better to buy single tickets.

But there's a middle case. For example, if the m-ride ticket is cheaper than buying m single tickets (i.e., b < m*a), then it's better to buy m-ride tickets. But if the remaining rides after k full m-ride tickets is r, then you can either buy one more m-ride ticket (costing b) or buy r single tickets (costing r*a). So which is cheaper?

So the approach would be:

Compute how many full m-ride tickets you can buy (k = n // m), and then handle the remainder r = n % m.

Then the possible options for the remainder are:

- Buy k m-tickets and r singles. Total cost: k*b + r*a.

- Buy k+1 m-tickets. Total cost: (k+1)*b.

Compare these two and choose the cheaper one. Then compare this with the option of buying all singles (n*a) and also with the option of buying all m-tickets (ceil(n/m)*b).

Wait, but maybe there's an even better approach. Let's see.

Alternatively, the optimal strategy is to buy as many m-ride tickets as possible when the m-ride is cheaper per ride than the single. Otherwise, buy singles. But this is not necessarily the case. For example, maybe the m-ride is cheaper than m singles (so per ride it's better), but the remainder's cost could be higher. Like if n = m +1. Then buying one m-ride ticket and one single would cost b +a. Or buying two m-ride tickets would cost 2b. Depending on which is cheaper.

So the correct approach is to compute all possible k from 0 to the maximum possible (ceil(n/m)), compute the cost for each, and select the minimum.

But how to compute the maximum possible k? For example, if n is 5 and m is 3. Then ceil(5/3) is 2. So k can be 0,1,2. Let's see:

For k=0: cost is 5a.

k=1: cost is b + 2a (since 5-3=2).

k=2: cost is 2b (since 2*3=6 >=5, so no singles needed).

So the possible options are 5a, 3a +b, 2b. Which is the minimum depends on the values.

So to cover all possibilities, we need to consider all k from 0 to ceil(n/m). Then for each k, compute the cost as (k * b) + (max(0, n -k*m) *a) if k*m <n. Otherwise, the cost is k*b. But wait, when k is larger than the required (like k=2 in the example where n=5 and m=3), the cost is 2*b, which could be better than k=1's cost if 2b is less than (b + 2a).

Therefore, the algorithm is:

Calculate the minimum between:

- The cost of buying all single tickets (n * a)

- The cost of buying (n // m) m-ride tickets plus (n % m) single tickets

- The cost of buying (n // m + 1) m-ride tickets

But wait, maybe even buying more than that could be cheaper. For example, if m is 2, and n=6. Then n//m=3, and 3*2=6, so the remainder is zero. So the options are 3*b, 6*a, etc. But in the first sample, a=1 and b=2. 3*2=6, which is the same as 6*1. So either way, same cost.

Another example: n=5, m=2, a=2, b=3. So per m-ride is 3/2=1.5 per ride. Which is cheaper than a=2. So buying as many m-ride as possible. n//m=2, which gives 2*2=4 rides. Remaining 1. So cost is 2*3 +1*2=8. But if we buy 3 m-rides, 3*3=9. But 9 is more than 8. So in this case, the optimal is 2 m-rides plus 1 single.

So the code needs to calculate all possible k values from 0 to ceil(n/m). But for large n and m, that could be manageable. Since the constraints are up to 1000, even in the worst case, the loop would run up to 1000/1 +1 = 1001 times, which is trivial.

So the steps to solve the problem are:

1. Compute the maximum possible k, which is ceil(n/m). But in Python, how to compute that? Well, (n + m -1) // m gives the ceiling.

But another approach is to iterate k from 0 to (n + m -1) // m, inclusive. For each k, compute the cost.

Wait, for example, if n=5, m=2: (5+2-1)//2 =6//2=3. So k can be 0,1,2,3. Let's see:

k=3: m*k=6 >=5. So cost is 3*b.

So for each k in 0 to max_k (inclusive), compute the cost as k*b + max(0, n -k*m)*a if k*m <n, else k*b.

Wait, but for any k, the cost is min(k*b + max(0, n -k*m)*a, (k+1)*b, ...). No. Wait, the formula for the cost when considering k m-ride tickets is:

If k*m >=n → cost is k*b.

Else → cost is k*b + (n -k*m)*a.

So for each k in 0 to max_k, compute that cost. Then take the minimum over all possible k.

But since max_k is up to (1000 +1000-1)/1000 = 2, which is manageable.

Wait, but the constraints are n and m up to 1000. For example, if n=1000 and m=1. Then max_k is (1000 +1-1)/1 =1000. So looping from 0 to 1000 is 1001 iterations. Which is okay.

So the code can compute all possible k in that range, compute the cost for each, and take the minimum.

So in code:

Read n, m, a, b.

Compute max_k = (n + m -1) // m. Because that's the maximum number of m-ride tickets needed to cover n rides. Then iterate k from 0 to max_k, compute for each k:

rides_covered = k * m

if rides_covered >=n: cost = k*b

else: cost = k*b + (n - rides_covered)*a

Find the minimum cost across all k.

That's the approach. Because even if buying more m-ride tickets than needed (like in the case where the remainder is small but buying another m-ride is cheaper than buying the remainder's singles), this approach will capture that.

For example, suppose n=5, m=2, a=3, b=4. Then m-ride is 4/2=2 per ride, which is cheaper than a=3. So the optimal is to buy as many m-ride as possible. So for k=2, rides_covered=4. Remaining 1 ride. Cost 2*4 +1*3= 11. Or buy k=3 m-rides: 3*4=12. So 12 is worse than 11. So in this case, the minimum would be 11.

Wait, but if a=5 and b=4. Then for the remaining 1 ride, 5 is more expensive than 4 (the cost of another m-ride). So in that case, the optimal is to buy 3 m-rides, cost 12, which is better than 2*4 +5*1= 13.

So by considering k up to max_k, which in this case is (5+2-1)//2=3, we can check all possibilities and find the minimum.

So this approach covers all possible scenarios.

Therefore, the code can be structured as follows:

Read n, m, a, b.

max_k = (n + m -1) // m

min_cost = infinity

for k in 0 to max_k:

    rides_covered = k * m

    if rides_covered >=n:

        cost = k * b

    else:

        cost = k * b + (n - rides_covered) * a

    if cost < min_cost:

        min_cost = cost

return min_cost

But also, what about the case where the m-ride tickets are more expensive than a single ride? For example, if a is 1, and m is 2, b is 3. Then each m-ride is 1.5 per ride, which is more expensive than a single. So it's better to buy all single tickets. But the code would check k=0, which gives n*a= n*1. Which would be the minimum.

Yes. So in all cases, the code works.

Now, some edge cases.

Test case 1: n=6, m=2, a=1, b=2.

Possible k from 0 to (6+2-1)//2 = (7//2)=3.

k=0: 6*1=6.

k=1: 1*2 + (6-2)*1 = 2 +4=6.

k=2: 2*2 + 2*1=4+2=6.

k=3: 3*2=6.

All options give 6, so the min is 6.

Another test case: 5,2,2,3.

Sample input 2: output 8.

Possible k values up to (5+2-1)//2=3.

k=0: 5*2=10.

k=1: 3 + (5-2)*2=3+6=9.

k=2: 2*3 + (5-4)*2=6+2=8.

k=3: 3*3=9.

So the minimum is 8.

Which matches the sample.

Another example where buying more m-rides than needed is better:

n=5, m=3, a=3, b=4.

b is 4 for 3 rides. So per ride 4/3 ~1.33. a is 3. So m-rides are better.

But:

k=1: 4 + (5-3)*3=4 +6=10.

k=2: 8. (covers 6 rides, which is more than 5). So 8 is cheaper.

So the code will check k=2, and that's the minimum.

So the code works.

So the approach is correct.

Now, implementing this in Python.

Read the input line, split into four integers.

Compute max_k as (n + m -1) // m.

Loop k from 0 to max_k inclusive.

Compute the cost as described.

Keep track of the minimum.

Finally, print the minimum.

Now, code.

But in Python, loops can be a bit slow if n is large, but given the constraints (n up to 1000, m up to 1000), max_k can be up to 1000 (if m=1, n=1000, max_k is 1000). So loop 1001 times is acceptable.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m, a, b = map(int, input_stream.readline().rstrip("\n").split())

    max_k = (n + m -1) // m

    min_cost = float('inf')

    for k in range(max_k +1):

        rides_covered = k * m

        if rides_covered >=n:

            cost = k * b

        else:

            cost = k * b + (n - rides_covered) * a

        if cost < min_cost:

            min_cost = cost

    print(min_cost, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 2 2 3
""",
            "output": \
"""\
8
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

5 2 2 3.

max_k = (5+2-1)//2=6//2=3.

k=0 →5*2=10.

k=1 →3 +3*2=3+6=9.

k=2 →6 +1*2=8.

k=3 →9.

So output is 8.

Another test case where buying more than needed m-rides is better.

n=5, m=3, a=5, b=4.

max_k= (5+3-1)//3 =7//3=2.

k=0: 5*5=25.

k=1:4 +2*5=4+10=14.

k=2:8 (covers 6 rides). Cost is 8. Which is cheaper than 14.

So the code returns 8.

Yes.

So the code should work correctly.
</think>

```python
n, m, a, b = map(int, input().split())
max_k = (n + m - 1) // m
min_cost = float('inf')
for k in range(max_k + 1):
    rides = k * m
    if rides >= n:
        cost = k * b
    else:
        cost = k * b + (n - rides) * a
    if cost < min_cost:
        min_cost = cost
print(min_cost)
```
