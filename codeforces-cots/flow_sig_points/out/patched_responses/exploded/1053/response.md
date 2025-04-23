<think>
Okay, let's see. The problem is to find the number of ways to buy exactly n liters of cola using a combination of 0.5L, 1L, and 2L bottles. The constraints are on the maximum number of each type of bottle available (a for 0.5L, b for 1L, c for 2L). And we need to count all possible triples (x, y, z) where x is the number of 0.5L bottles, y is 1L, z is 2L. The sum 0.5x + y + 2z should equal n. Also, x can't exceed a, y can't exceed b, z can't exceed c.

Hmm. So first, the variables are x, y, z. Let's think about the equation:

0.5x + y + 2z = n

But dealing with fractions might complicate things. Let's multiply both sides by 2 to eliminate the decimal:

x + 2y + 4z = 2n

That's better. Now x must be even? Wait, no. Because x is the number of 0.5L bottles. Each contributes 0.5L, so x must be an even number? Wait, no. Let's see. For example, if x is 1, that's 0.5 liters. So when multiplied by 0.5, x can be any non-negative integer. But when we rewrite the equation as x + 2y +4z = 2n, then x must be even? Because 0.5x is n - y - 2z. So 0.5x must be an integer. So x must be even. Wait, no. Because 0.5x must be an integer. So x has to be even. Because if x is even, then 0.5x is integer. But if x is odd, then 0.5x is a half-integer. So when we sum 0.5x + y + 2z, which must be an integer n, the x must be even. Otherwise, the sum would have a fractional part of 0.5, which can't equal an integer. So x must be even. So that's a key insight. So for x to contribute 0.5 liters each, the number of x has to be even. Otherwise, the total liters would have a 0.5 part, which can't sum to an integer n.

So this implies that x must be even. Wait, no. Let's think again. Let's say n is 3. Then 0.5x + y + 2z = 3. For example, x could be 2 (1 liter) plus y=1 (1L) and z=0.5*2=1. Wait, z has to be an integer. So the equation must sum to exactly n, which is an integer. So 0.5x must be an integer. So x must be even.

Ah right! Because 0.5x must be an integer. So x has to be even. So x can be written as 2k, where k is an integer >=0, and k must be <= a/2 (since x is up to a). Wait, no. Because x is up to a. So k can be from 0 up to a//2 (if a is even) or (a-1)/2 if a is odd. Wait, but x can't exceed a. So for example, if a is 5, then x can be 0,2,4. So k can be 0,1,2. Because 2k <= a. So the maximum k is floor(a/2). Because 2k can't exceed a. So for a=5, 2*2=4 <=5, so maximum k is 2. So x can be 0,2,4.

So, substituting x=2k, the equation becomes:

2k + 2y +4z = 2n

Divide both sides by 2:

k + y + 2z = n

Now, the variables are k, y, z. The constraints are:

k can be 0 to min(a, 2*10^4) // 2, but wait, k can't exceed a/2 since x=2k ≤ a. So k_max = a // 1 (since x is up to a) but wait, no. Wait, x is 2k, which must be ≤a. So 2k ≤a → k ≤ a/2. So the maximum possible k is floor(a/2). For example, a=5 → 5//2=2, which is correct (x=4 is 2*2=4 ≤5). So k can range from 0 to min( a // 2, ... ) but the maximum possible k is a//2. But a can be up to 5000. So k can be up to 2500.

Now the equation is k + y + 2z = n.

We need to find all possible non-negative integers k, y, z such that:

k + y + 2z = n

And:

k ≤ a//2

y ≤ b

z ≤ c

So the problem now reduces to counting the number of (k, y, z) triples satisfying these conditions.

So the approach is to iterate through possible z and k values, then compute y, check if it's within the constraints.

Wait, let's see. For each possible z (up to min(c, (n - ... )) ), and for each possible k (up to min(a//2, n - 2z)), then compute y = n -k -2z. Then check if y is between 0 and b, inclusive. If yes, then this combination is valid.

So the steps are:

For z in 0 to min(c, (n) //2):

Wait, no. Because 2z can be up to n. But the sum k + y + 2z =n. Since k and y are non-negative, 2z can't exceed n. So z can be at most n//2. But also, z can't exceed c. So the maximum z is min(c, n//2). Wait, no. Because k and y could be zero, but 2z can be up to n. So 2z ≤n → z ≤n//2. So z ranges from 0 to min(c, n//2). But also, when considering the equation: for a given z, the remaining sum is k + y = n - 2z. So for each z, the possible z must be such that 2z ≤n. So z can be from 0 to min(c, floor(n/2)). But wait, 2z can be up to n, because if z is n/2, then 2z is exactly n. So that's correct.

So for each possible z (0 ≤ z ≤ min(c, n//2)), then:

remaining = n - 2z

Then for this z, we need to find the number of (k, y) pairs such that:

k + y = remaining

k ≤ a//2 (since k is up to a//2)

y ≤ b

and y ≥0.

So for each z, compute the possible k and y.

The sum k + y = remaining. So for each possible k in 0 ≤k ≤ min( a//2, remaining ), then y = remaining -k. Then check if y is between 0 and b, inclusive.

But how to efficiently calculate the number of valid (k, y) pairs for a given z?

Let's think for a fixed z:

remaining = n - 2z.

We need k to be between 0 and min( a//2, remaining ), and y = remaining -k must be between 0 and b.

So y = remaining -k ≥0 → k ≤ remaining.

So k can be from max(0, remaining - b) to min( a//2, remaining ). Because y must be ≤b → remaining -k ≤b → k ≥ remaining -b.

So the valid k's are those in the range [max(0, remaining -b), min( a//2, remaining ) ].

If the lower bound is greater than the upper bound, then there are zero possibilities for this z.

So for a given z, the number of valid k's is the count of integers in this interval.

So the steps would be:

For each z in 0 to min(c, n//2):

   if 2z >n → skip (since remaining would be negative, but z is up to n//2, so 2z is ≤n)

   remaining = n - 2z

   if remaining <0 → skip (but z is up to n//2, so 2z <=n, so remaining >=0)

   k_min = max(0, remaining - b )

   k_max = min( a//2, remaining )

   if k_min >k_max → continue

   possible_ks = k_max - k_min + 1

   sum += possible_ks

But wait, when remaining - b could be negative. So k_min is 0 in that case.

Wait, let's take an example. Suppose remaining is 5, b is 3. Then y =5 -k must be ≤3 → k ≥5-3=2. So k can be from 2 to min( a//2, 5 ). So possible_ks is 5-2 +1=4 if a//2 is >=5.

But if a//2 is 3, then k_max is 3. So 3-2+1=2.

So yes, the formula is correct.

So the algorithm is:

Initialize the count to 0.

Loop over z from 0 to min(c, n//2):

   if z exceeds c → continue (but since loop is up to min(c, ... ), this is already handled)

   compute remaining = n - 2*z

   if remaining <0 → skip (but z is up to n//2, so 2z <=n → remaining >=0)

   k_min = max(0, remaining - b)

   k_max = min( a//2, remaining )

   if k_min >k_max → continue

   possible_ks = k_max -k_min +1

   add possible_ks to the count.

So this seems manageable.

Now, considering the constraints:

n can be up to 10,000.

c can be up to 5000. So for z in 0 to min(c, 10^4//2)=5000 (if n is 10^4). So for each z, the loop runs 5000 times in the worst case. But 5000 iterations are manageable, as each iteration is O(1).

So the time complexity is O(c_max), where c_max is up to 5000. Which is acceptable for Python, even with 2 seconds time limit.

But let's check for n=10000 and c=5000, then z can be up to 5000 (since 2*5000=10000 equals n). So z ranges 0..5000: 5001 iterations. Each iteration does a few arithmetic operations. So 5000 iterations is manageable.

So the algorithm should be efficient enough.

Now, let's check some examples.

First example:

Input:

10 5 5 5

n=10, a=5, b=5, c=5.

The equation after substitution:

k + y + 2z =10

We loop z from 0 to min(5, 10//2=5) → z 0-5.

For each z:

Let's compute for each z:

z can be 0 to 5.

For z=0:

remaining =10-0=10.

k_min = max(0, 10 -5=5) →5

k_max = min(5//2=2, 10) →2.

So k_min=5 >k_max=2 → possible_ks is zero. So no contribution.

z=0 → 0.

z=1:

2z=2 → remaining=8.

k_min = max(0, 8-5=3) →3

k_max = min(5//2=2,8) →2. Again 3>2 → no.

z=1: 0.

z=2: 2*2=4 → remaining=6.

k_min =6-5=1. k_max=min(2,6) →2.

so k ranges from 1 to2. 2-1+1=2. So possible_ks is 2.

So add 2.

z=3: 2*3=6 → remaining=4.

k_min =4-5= -1 → 0.

k_max= min(2,4) →2.

k can be 0-2 (since 0<=k<=2 and <=4). So possible_ks=3 (0,1,2). But y=4 -k must be <=5. Since 4-k is between 4 and 2 (when k is 0, y=4; k=2, y=2). All are ≤5. So 3 possibilities.

So add 3.

z=3 contributes 3.

z=4: 2*4=8 → remaining=2.

k_min=2-5= -3 →0.

k_max=2.

So k can be 0,1,2. y=2 -k. y must be >=0 and <=5.

So for k=0 → y=2 → valid.

k=1 → y=1.

k=2 → y=0.

All valid. So possible_ks=3. Add 3.

z=4: +3.

z=5: 2*5=10 → remaining=0.

k_min=0-5=-5 →0.

k_max=0.

So k can be 0. y=0-0=0.

Check y <=5: yes. So possible_ks=1. Add 1.

So total contributions:

z=2: 2

z=3:3

z=4:3

z=5:1

Sum: 2+3+3+1=9. Which matches the first example.

So the code works here.

Another example: input 3 0 0 2.

n=3. a=0, b=0, c=2.

So equation is k + y +2z=3.

But a=0 →k must be 0 (since x=2k <=0 →k=0). So k=0.

Then y +2z=3.

But y must be <=0 (since b=0). So y=0. So 2z=3 →z=1.5, which is invalid. So no solution. Output is 0. Which matches the second example.

So the code should handle that.

So the plan is to loop z from 0 to min(c, n//2), then for each z, compute remaining, and compute the possible k's.

Now, how to implement this in Python.

First, read the input: n, a, b, c.

But note that the a here is the maximum number of 0.5L bottles. So in the equation, x = 2k, which can be up to a. So k can be up to a//2 (since 2k <=a). So for a=5 →a//2=2 (since 5//2 is 2). So correct.

So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    count =0

    max_z = min(c, n//2)

    for z in range(0, max_z +1):

        # since z can be up to max_z inclusive

        remaining = n - 2*z

        if remaining <0:

            continue  # but z is <=n//2 → remaining >=0, so this is redundant

        max_k = a //2

        # k can be up to min(max_k, remaining)

        k_max = min(max_k, remaining)

        # y must be remaining -k <=b → k >= remaining -b

        k_min = max(0, remaining - b)

        if k_min > k_max:

            continue

        possible = k_max - k_min +1

        count += possible

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 0 0 2
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

Yes.

Another test case: input 3 0 0 2.

max_z is min(2, 3//2=1) →1.

z can be 0 or 1.

For z=0:

remaining=3-0=3.

max_k=0//2=0.

k_max=0.

k_min=3-0=3. So 3>0 → no contribution.

z=1: remaining=3-2*1=1.

max_k=0//2=0.

k_min=1-0=1. which is >0 → no.

So total 0. Correct.

Another test case: n=1, a=2 (so x can be 0,2 → 0 and 2 bottles of 0.5L → 0L and 1L).

So possible combinations:

z can be 0 (since 2z <=1 → z=0).

remaining =1-0=1.

max_k =2//2=1.

k_min =1- b.

Assuming b is given. Let's say for example, if b is 1.

Then:

k_min =1-1=0.

k_max=1.

So possible_ks=1-0+1=2. So k=0 and 1.

Then y =1-0=1 (valid if b>=1), and y=1-1=0 (valid if b>=0).

So for a=2, b=1, c=0: output is 2.

So code would output 2.

So code works.

Thus, this approach should be correct.
</think>

```python
n, a, b, c = map(int, input().split())
count = 0
max_z = min(c, n // 2)
for z in range(max_z + 1):
    remaining = n - 2 * z
    max_k = a // 2
    k_max = min(max_k, remaining)
    k_min = max(0, remaining - b)
    if k_min > k_max:
        continue
    count += k_max - k_min + 1
print(count)
```
