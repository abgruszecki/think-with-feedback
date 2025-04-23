<think>
Okay, let's see. So the problem is about organizing elimination rounds to get enough people into the finals while using the least number of problems. Hmm. Let's parse the problem statement carefully.

The goal is to determine the minimal total number of problems used in all rounds (main and additional) such that the total number of people (from rounds plus pre-chosen) is at least n*m. And we need to minimize the total problems.

Let me break down the inputs. We have c and d as the number of problems in each main and additional round, respectively. Each main round produces n winners (since each main round's winners are the first n in the rating). Each additional round gives 1 winner. Also, there are k pre-chosen winners who are already in.

So the required number of people is at least required = max(0, n*m - k). If the pre-chosen k is already >= n*m, then no rounds needed. Otherwise, we need to find how many main and additional rounds to use.

The problem reduces to finding the number of main rounds (x) and additional rounds (y) such that:

x * n + y >= required

And the total problems is x*c + y*d, which we need to minimize.

So the variables x and y are non-negative integers. We need to find all possible combinations of x and y that satisfy x*n + y >= required, then compute x*c + y*d and find the minimum.

But considering that the possible values for x and y can be up to a certain point. Let's think about the constraints.

First, the required is up to (n*m -k) which could be up to 100*100 - 1 = 9999, but if k is 100, then maybe even up to 100*100-100=9900. So required can be up to 100*100 -1=9999.

But how do we approach this? Trying all possible x and y up to the maximum possible needed.

For example, x can be up to required / n + 1, because each x contributes n people. So for required = 9999, x can go up to (9999)/n +1. Since n can be as low as 1, x can be up to 9999 +1 = 10000. But even that is manageable in a loop.

But 10000 iterations might be acceptable in Python for a problem with time constraints of 1 second. Because even 1e6 operations are manageable.

Wait, but if x can be up to 10000, and for each x we compute the minimal y, then the total iterations are 10000 steps, which is manageable.

Alternatively, for each possible x from 0 to max_x, compute the minimal y needed, and then calculate the total problems. Then take the minimum over all x and y.

Yes. Let's formalize this.

The required people is req = max(0, n*m -k). If req <=0, then output is 0.

Otherwise:

We need to choose x (number of main rounds) and y (number of additional rounds) such that x*n + y >= req.

The total cost is x*c + y*d.

We need to find the minimal cost.

For each possible x (from 0 up to (req +n-1)//n), since x*n can't be larger than req + some value (because y can take care of the rest), but perhaps x can be up to (req) // n + some.

Wait, but for x, the maximum possible x is when we take all possible main rounds. For example, x can be up to req // n + 1. Because even if x is req//n +1, that's more than needed. Let's see.

Suppose req is 10, n=3. Then x can be 0 to 4 (since 3*3=9 <10, but 4*3=12 >=10). Wait, but if x is 4, then y can be 0. So for x, the maximum possible is ceil(req /n), but perhaps even higher? Like, maybe taking more main rounds than necessary and then y is negative (but y can't be negative). So no, x can't be more than (req + y)/n, but y can be zero. Wait, perhaps x can be any value up to some upper bound, but higher x would require y to be possibly lower, but it's possible that adding more main rounds (x) and using negative y (which isn't allowed) would not help. So the maximum x to consider is when all the required people come from main rounds. So x_max can be (req + (n-1)) // n (rounded up). For example, if req is 10, n=3: (10+2)//3=12//3=4. So x_max is 4. Then, for x up to x_max, we can compute the minimal y needed.

But also, x can be higher than that. For example, if x is 5, then x*n is 15, which is more than req=10. Then y can be 0. But this would cost 5*c +0*d. So, perhaps it's better to check up to x_max plus some possible x values beyond that. Wait, but when x increases beyond x_max, the total people from main rounds is x*n, which is >= req. So for x >= x_max, y can be 0. The cost would be x*c. So the minimal for x >= x_max is the minimal between x_max*c, (x_max +1)*c, etc. But that's possible only if c is such that adding more main rounds is cheaper than using x_max rounds and some additional.

For example, if c is cheaper than d, then it's better to use more main rounds and no additional. So in this case, the minimal x is x_max, and y=0. Because adding more main rounds (x_max +1) would cost more, but maybe x_max is the minimal x where x*n >= req.

Wait, but if x is x_max, then x_max *n >= req, so y can be 0. So for x >= x_max, y can be zero. So the minimal cost for x >= x_max is x*c. To find the minimal in this case, it's the minimal between x_max * c, (x_max+1)*c, etc. But since x increases, the cost increases as well (since c is positive). So the minimal is x_max *c.

Thus, when x is >= x_max, the minimal cost for that x is x*c, and the minimal in this region is x_max *c. So we can calculate x_max as ceil(req /n). So the minimal cost when x >=x_max is x_max *c. But how do we compare this with other possibilities (like using x less than x_max and adding some additional rounds)?

So, the approach could be:

1. Compute req = max(0, n*m -k). If req <=0, output 0.

2. Else, for x in 0 to x_max (inclusive), where x_max is ceil(req /n) + some buffer (maybe up to x_max plus some upper limit?), but in practice, x can be up to (req + 1e5) but that's not feasible. So, perhaps x can be up to x_max + (d//c) or something. But perhaps not. Let's think.

Wait, the maximum possible x is such that even if adding more x's (main rounds) would be better than using some additional rounds. For example, if c is 1, d is 100. So each main round gives n people (cost 1), each additional gives 1 (cost 100). So for each person needed, it's better to use main rounds. So the optimal x is ceil(req /n), and y=0.

Alternatively, if d is cheaper than c per person. For example, if c is 100, d is 1, and n is 1. Then, using additional rounds is better. So for x=0 and y=req, the cost is req*d.

But in general, for each x from 0 up to some maximum, we can compute the minimal y needed, and calculate the cost.

So the plan is:

For each possible x (number of main rounds) from 0 up to a certain maximum (like x_max_upper), compute the minimal y required. Then compute the total cost.

What's x_max_upper? Well, the minimal possible x where x*c + y*d is better than any other x. But since x can be up to req (since even if n=1, x can be req), but that's too big (up to 1e4 for x, but in Python, looping up to 1e4 is okay, right? Because 1e4 is manageable. So perhaps for x in 0 to (req +1), then for each x, compute the minimal y.

But req can be up to 1e4 (since n and m are up to 100, so n*m is 1e4, and k can be 1, so req can be 9999). So x can be up to 1e4. For each x, compute the minimal y as max(0, req - x*n). Then y must be >=0. So the minimal y is max(0, req -x*n). But then, the total cost is x*c + y*d. So for each x in 0 to (req +1), compute that.

But maybe we can find a smarter upper bound for x. For example, the maximum x that we need to consider is when adding another main round would not improve the cost. But perhaps that's hard. So instead, loop x from 0 to (req //n) + (d * req) // (c * 1) +1. Hmm, not sure. Alternatively, the maximum x can be up to (req + (d//c)*something). Wait, perhaps x can't be larger than (req + (d * req)/c)/n. Not sure. Maybe it's easier to loop x up to (req + d) //1 or something.

Alternatively, considering that for x beyond a certain point, the cost x*c would be higher than other possible combinations. For example, if x is larger than (req *d)/c, then adding x main rounds (each contributing n people) may not be optimal. But I'm not sure.

Alternatively, since for x in 0 to req (since each main round can give at least 1 person, assuming n>=1), but even if n is 1, the maximum x can be up to req (since x=req, y=0 gives req*1 >= req). So x can loop from 0 to req. But req is up to 1e4. So 1e4 iterations. For each x, compute y = max(0, req - x*n). Then total cost is x*c + y*d. Find the minimal such cost.

Yes, that's manageable. So the steps are:

Compute req = max(0, n*m -k). If req <=0, output 0.

Else:

Initialize min_problems to a very large number.

For x in 0 to (req//n + 1) * 2 (or just up to some upper limit, say req + 1e4, but that's not efficient). Wait, but what's the maximum x that could possibly contribute to a minimal cost?

Well, the maximum x that could be considered is when even if x is very high, but the cost x*c is lower than other options. But for x to be part of the minimal solution, x must be such that adding a main round (x) plus some y is better than not adding it. For example, if c is 1 and d is 100, then x can be as high as possible. But in that case, the minimal x is ceil(req /n), and higher x would have higher cost.

So, to cover all possible x that could be part of the minimal solution, we can loop x from 0 to (req + n) //n. Because if x is (req//n) + 1, then x*n is req +n, which is more than req, so y=0.

But perhaps even x can be higher. For example, if req is 10, n=3. Then x_max_ceil is 4 (since 3*4=12 >=10). So x can be up to 4, and higher x (like 5, 6, etc.) would have y=0. So for x=5, the cost is 5*c. But maybe 5*c is larger than 4*c, so the minimal is 4*c. So checking x up to x_max_ceil is sufficient.

Wait, but if c is 1, then 5*c=5 is worse than 4*c=4. So the minimal for x >=4 is 4*c.

So in that case, x can be up to x_max_ceil. So the upper limit for x can be x_max_ceil, which is (req +n -1) //n.

So for x in 0 to x_max_ceil, compute the minimal y for each x and calculate the cost. Also, check x_max_ceil +1, etc., but in those cases, the cost will be higher than x_max_ceil's cost. So perhaps it's sufficient to loop x from 0 to x_max_ceil.

But what about cases where using x higher than x_max_ceil could be better? For example, suppose c is 5, d is 3. And x_max_ceil is 4 (c=5, x=4 gives 20 cost). Then, suppose x=5, which gives x*c=25, which is higher than 20. So it's worse.

So, no. The minimal cost for x >=x_max_ceil is x_max_ceil *c, and higher x's have higher cost.

Thus, to find the minimal possible cost, it's sufficient to consider all x from 0 up to x_max_ceil, where x_max_ceil = (req +n-1) //n.

So, the plan is:

Calculate req.

If req <=0: output 0.

Else:

Initialize min_cost to a large number.

x_max = (req +n -1) //n

For x in 0 to x_max:

   y_needed = max(0, req - x*n)

   y_min = y_needed

   # but each additional round gives 1 person. So to get y_min people, we need y rounds.

   total = x*c + y_min *d

   if total < min_cost:

       min_cost = total

So, check all x from 0 to x_max, including x_max.

Wait, but what if x exceeds x_max_ceil? Like x is x_max_ceil +1. Then x*n would be >= req, and y_min is 0. The cost would be (x_max_ceil +1)*c. Which is higher than x_max_ceil *c. So considering x up to x_max_ceil is sufficient.

So the loop can be for x in 0 to x_max.

But what about cases where even higher x could give a lower cost? For example, if c is 2 and d is 3. Then, for req =5, n=2. x_max_ceil is (5+2-1)//2 = 6//2=3. So x_max_ceil=3, x*n=6. So y=0. cost=3*2=6. Alternatively, x=4: 4*2=8 cost. So higher x is worse.

But if c is 1, d is 100. Then x_max_ceil is 5//2=3 (req=5, n=2: 3*2=6 >=5). x=3: cost 3*1=3. x=4: cost 4*1=4. So higher x is worse.

So yes, the loop from x=0 to x_max_ceil is sufficient.

Thus, the algorithm is:

Calculate req.

If req <=0: output 0.

Else:

Compute x_max = ceil(req /n) = (req +n -1) //n

Initialize min_cost to a very high value (like infinity).

Loop x from 0 to x_max:

   y_needed = max(0, req - x*n)

   total = x*c + y_needed *d

   if total < min_cost:

       min_cost = total

Also, perhaps in some cases, even though x is less than x_max, but combining with some additional rounds could be cheaper than x_max's cost.

For example, let's take sample input 1:

Input:

1 10

7 2 → n=7, m=2 → 7*2=14. k=1. So req=14-1=13.

x_max_ceil = (13 +7-1)/7 = (19)//7 = 2. So x can be up to 2.

For x=2: 2*7=14 >=13 → y=0. cost=2*1 +0*10=2. Which matches the sample output.

Another example:

Sample input 2:

2 2

2 1 → req=2*1 -2=0. So output is 0.

So the code correctly handles that.

Another example: if req=5, n=3, c=3, d=1.

x_max_ceil is (5+3-1)//3 =7//3=2. So x can be 0,1,2.

x=0 → y=5 → cost 0*3 +5*1=5.

x=1 → 3 people, y=2 → cost 3 +2=5.

x=2 → 6 people, cost 6 → higher.

So the minimal is 5.

But if d=1, then for x=0, y=5 → 5.

x=1, y=2 →5.

So same cost.

Thus, the code will find the minimal.

Now, what's the possible maximum x_max_ceil?

req can be up to 100*100 -1=9999, n=1. So x_max_ceil is (9999 +1-1)/1 =9999. So loop runs 10,000 times. Which is acceptable in Python.

So the code should be:

Read c, d.

Read n, m.

Read k.

req = max(0, n*m -k).

if req ==0:

    print(0)

else:

    x_max = (req +n -1) //n

    min_total = float('inf')

    for x in range(0, x_max +1):

        y_needed = max(0, req - x*n)

        total = x*c + y_needed*d

        if total < min_total:

            min_total = total

    print(min_total)

Wait, but what about cases where even after x rounds of main, and y rounds of additional, but maybe using more additional rounds is better than adding main rounds?

For example, in a case where c is higher than d. Like, c=10, d=1. So each main round gives 3 people (n=3), and each additional gives 1 person at cost 1. So for req=4:

x can be 0: y=4 → cost 4*1=4.

x=1: 3 people, y=1 → cost 10 +1=11.

x=2: 6 >=4 → cost 20 → worse.

So minimal is 4. So the code would check x from 0 to (4+3-1)/3= (6)/3=2. So x=0,1,2. For x=0, total 4, which is correct.

So yes.

Another test case where the minimal is achieved by a combination of x and y where x is not the maximum possible.

Another example: c=3, d=1. n=3, req=5. x can be up to 2 (5/3 rounded up is 2).

x=1: 3 people, y needed=2. cost 3*1 +2*1=5.

x=0: y=5 → cost 5*1=5.

x=2: 6 >=5 → cost 6*3=18. So the minimal is 5.

So code works.

Thus, the code is correct.

Now, implement this in Python.

Edge cases:

1. k >=n*m → output 0.

2. req is 0 → output 0.

3. When combining main and additional rounds is better.

4. When main rounds are better.

5. When additional rounds are better.

Now, code.

Read the inputs:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    c, d = map(int, input_stream.readline().rstrip("\n").split())

    n, m = map(int, input_stream.readline().rstrip("\n").split())

    k = int(input_stream.readline().rstrip("\n"))

    req = max(0, n*m -k)

    if req ==0:

        print(0, file=output_stream)

    else:

        x_max = (req +n -1) //n

        min_total = float('inf')

        for x in range(x_max +1):

            y = max(0, req - x *n)

            total = x *c + y *d

            if total < min_total:

                min_total = total

        print(min_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 2
2 1
2
""",
            "output": \
"""\
0
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

2 2

2 1 → req=2*1 -2=0 → output 0.

Another test case where c=3, d=1, n=3, req=5.

x_max = (5+3-1)/3 →7//3=2.

x=0: total 5*1=5.

x=1: 3+2 →3+2=5.

x=2: 6 →3*2=6 →5 is better.

Thus, code works.

So this should be the correct code.
</think>

```python
c, d = map(int, input().split())
n, m = map(int, input().split())
k = int(input())
required = max(0, n * m - k)
if required == 0:
    print(0)
else:
    max_main_rounds = (required + n - 1) // n
    min_problems = float('inf')
    for x in range(max_main_rounds + 1):
        y = max(0, required - x * n)
        total = x * c + y * d
        if total < min_problems:
            min_problems = total
    print(min_problems)
```
