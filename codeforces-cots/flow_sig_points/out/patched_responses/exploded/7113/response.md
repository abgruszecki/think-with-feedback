<think>
Okay, let's tackle this problem. So, the task is to find the number of pairs (x, y) where x is between 1 and n, y is between 1 and m, and their sum is divisible by 5. Hmm. Right, the key here is to figure out for each possible x mod 5, what y mod 5 would make the sum mod 5 zero. Because if x mod 5 is a, then y mod 5 needs to be (5 - a) mod 5. That way, when you add them, you get 0 mod 5.

So the plan is: count how many numbers in x's range (1 to n) have each possible remainder when divided by 5. Then do the same for y. Then, for each remainder a in x's counts, multiply it by the count of remainder (5 - a) mod 5 in y's counts. Sum all those products, and that's the total pairs.

Wait, but how do we compute the counts efficiently? Let's think. For a given remainder r, the count in the x array is (n + (5 - r) %5) //5? Or maybe for each possible remainder from 0 to 4, calculate how many numbers in 1..n have that remainder.

For example, take n=6. The remainders are:
1 mod5=1, 2 mod5=2, 3 mod5=3,4 mod5=4,5 mod5=0,6 mod5=1. So counts are 0:1, 1:2, 2:1,3:1,4:1.

Wait, so for remainder 0: floor((n) /5). Then for other remainders, it's floor((n - r)/5) +1. Wait, maybe there's a pattern here. For a remainder a (from 0 to 4), the count is how many numbers x in 1..n have x mod5 ==a.

Alternatively, for remainder a, the numbers are a, a+5, a+10, etc., up to n. So the count for a is equal to (n - a + 5) //5 if a <=n, else 0.

Wait, for example, a=0: the numbers are 5,10,15,... up to n. So the count is n//5 if n>=5, else 0. Wait, n=5: 1 number. n=6: 1 (5). So (5-0)/5 is 1. For a=0, the count is (n) //5.

For a=1, the numbers are 1,6,11,... So the count is (n -1 +5) //5. Wait, (n -1) //5 +1. For example, n=6: (6-1) //5 =1, +1=2. Which matches the example.

So for each a in 0-4:

count_x[a] = (n - a +5) //5 if a <=n else 0. But wait, when a is 0, we can't subtract 0? Wait, a=0. So (n -0 +5) //5? That would be (n+5)/5, which is (n//5) +1. But for a=0, the numbers are 5,10,... So when n=5, (5+5)/5=2, but the actual count is 1. So that's not correct.

Hmm, perhaps another approach. The count for a remainder a (0<=a<=4) is equal to the number of integers x in 1..n where x mod5 =a. So for a=0, it's the count of numbers divisible by 5. Which is floor(n/5). For a>0, the first number is a, then a+5, etc. So the count is floor( (n -a)/5 ) +1 if a <=n. Otherwise, zero.

So for example:

n=6, a=0: floor(6/5)=1.

a=1: (6-1)/5 =1 → 1+1=2. Correct.

a=5: wait, a can't be 5. Oh right, a is from 0-4.

So general formula:

For each a in 0..4:

if a ==0: count = n//5

else: count = (n -a) //5 +1 if a <=n else 0.

Wait, but when a is larger than n, then (n -a) is negative, and divided by 5 gives negative, adding 1 could be 0. For example, n=3 and a=4: 3-4 =-1, -1//5 is -1, +1=0. Which is correct because 4>3.

So the formula can be written as:

count_x[a] = (n - a) //5 +1 if a >0 and a <=n else 0. But wait, if a=0, then count is n//5.

Wait, maybe it's better to handle a=0 separately.

Alternatively, for all a in 0-4:

count_x[a] = (n + (5 - a) %5 ) //5

Wait, not sure. Maybe that's not the right way.

Alternatively, perhaps the formula can be written as:

count_x[a] = (n + (5 - a)) //5 if a >0 else n//5.

But let's test for a=1, n=6. 6+5-1=10 →10//5=2. Which is correct. For a=0, n//5=1. For n=5, a=0 →5//5=1. Correct.

But for a=0 and n=4: 4//5=0. Correct.

For a=3 and n=3: (3 +5-3) //5 →5//5=1. Which is correct because 3 is counted once.

For a=4 and n=4: (4+5-4)/5 →5//5=1. Correct.

So yes, the formula for a>0 is (n + (5 -a))//5, which simplifies to (n -a +5)//5. So (n -a +5) //5 = (n +5 -a) //5.

But when a=0, it's n//5.

So how do we compute this for each a?

So for each a from 0 to4:

if a ==0: count is n//5

else: count is (n -a +5) //5 if (n >=a) else 0.

Wait, but (n -a +5) //5 is the same as (n +5 -a)//5. For example, a=1 and n=6: (6+5-1)/5=10/5=2. Correct.

So perhaps for a in 0-4:

count_x[a] = (n + (5 - a)) //5 if a !=0 else n//5.

Wait, but when a=0:

(n +5 -0)/5 = (n+5)/5 → which is (n//5) +1 if n%5 !=0, or n//5 otherwise. Which is different from the correct n//5. So that's not correct. So the formula for a=0 is different.

Therefore, perhaps it's better to split into two cases.

So for a in 0-4:

count_x[a] = (n -a) //5 +1 if a !=0 and a <=n else 0 (for a!=0). And for a=0, count_x[0] = n//5.

Wait, but for a=0:

Yes, the count is the number of multiples of 5 up to n. Which is n//5.

For a !=0:

The numbers are a, a+5, a+10, ..., up to the maximum x <=n.

The first term is a, then each term increases by 5. The number of terms is ((n -a) //5) +1. But only if a <=n. Otherwise, zero.

So the formula is:

count_x[a] = ( (n >=a) ) ? ( (n -a) //5 +1 ) : 0.

So for a=0, count is n//5.

So for each a in 0-4, compute that.

Once we have the counts for x's remainders and y's remainders, the total pairs is sum over a in 0-4 of count_x[a] * count_y[(5 -a) mod5 ].

Wait, because (a + b) mod5 =0 → b = (5 -a) mod5.

Wait, for example, a=2. Then b should be 3, since 2+3=5. Which mod5 is 0.

So for a in 0-4:

The required b is (5 -a) mod5.

So for a=0: (5-0) mod5=0. So pairs are x's with 0 mod5 multiplied by y's with 0 mod5.

Similarly for other a's.

So the plan is:

1. Compute for x's, the count for each remainder 0-4.

2. Compute for y's, the count for each remainder 0-4.

3. For each a in 0-4, multiply count_x[a] by count_y[(5-a)%5], and sum all these products.

So the total is the sum of count_x[a] * count_y[(5 -a) %5] for a=0,1,2,3,4.

Now, the question is how to compute these counts efficiently.

Let's see. For each of x's remainders:

count_x[0] = n //5

count_x[1] = (n >=1) ? ((n-1) //5 +1) :0

count_x[2] = (n >=2) ? ((n-2) //5 +1) :0

count_x[3] = (n >=3) ? ((n-3) //5 +1) :0

count_x[4] = (n >=4) ? ((n-4) //5 +1) :0

Similarly for y's.

So, for example, n=6:

count_x[0] =6//5=1

count_x[1] = (6-1)/5 +1 →5/5=1 +1=2

count_x[2]=(6-2)/5 +1 →4/5=0 +1=1

count_x[3]=(6-3)/5 +1 →3/5=0 +1=1

count_x[4]=(6-4)/5 +1 →2/5=0 +1=1

Which matches the sample where for x=6, the counts are [1,2,1,1,1].

Then for y=12:

count_y[0] =12//5=2 (5,10)

count_y[1] = (12-1)/5 +1 →11/5=2 +1=3 (1,6,11)

count_y[2] = (12-2)/5 +1 →10/5=2 +1=3 (2,7,12)

count_y[3] = (12-3)/5 +1 →9/5=1 +1=2 (3,8)

count_y[4] = (12-4)/5 +1 →8/5=1 +1=2 (4,9)

So count_y is [2,3,3,2,2].

Now for each a in x's remainders:

For a=0: (5-0) mod5=0 → count_x[0] * count_y[0] →1 *2=2

a=1: (5-1)=4 mod5 → count_x[1] (2) * count_y[4] (2) →4

a=2: (5-2)=3 → count_x[2] (1) * count_y[3] (2) →2

a=3: (5-3)=2 →1 *3 →3

a=4: (5-4)=1 →1 *3 →3

Total sum:2+4+2+3+3=14, which matches the first sample.

So the approach is correct.

Now, how to compute this in code.

First, for n and m, compute their counts for each remainder.

We can compute the x_counts and y_counts arrays.

In Python, for a in 0-4:

x_counts[a] = (n //5) if a ==0 else ((n -a) //5 +1) if (n >=a) else 0.

Similarly for m and y_counts.

But wait, for a in 1-4, if n < a, then (n -a) is negative, so (n -a) //5 would be -1, adding 1 gives 0. So the formula ((n -a) //5 +1) works even when n <a.

Wait, let's test.

For example, n=3 and a=4:

n -a =3-4= -1 → -1//5 is -1 (since in Python, integer division truncates towards negative infinity). So -1 //5 is -1. Adding 1 gives 0. So yes, correct.

Another example: n=4 and a=4: (4-4)//5=0 →0+1=1. Correct.

So the formula ((n -a) //5 +1) works for all a >=1, regardless of whether a >n or not.

So, in code:

x_counts = [0]*5

x_counts[0] = n //5

for a in 1,2,3,4:

    x_counts[a] = (n - a) //5 +1

Similarly for y_counts.

Then, sum x_counts[a] * y_counts[ (5 -a) %5 ] for a in 0..4.

So in code:

total =0

for a in range(5):

    b = (5 -a) %5

    total += x_counts[a] * y_counts[b]

print(total)

This should give the correct answer.

Now, what's the time and space complexity?

Time is O(1) because we loop 5 times for each count, and then 5 times for the sum. So regardless of n and m, the code runs in constant time. Which is acceptable even for n and m up to 1e6.

Space is O(1), as we're storing 5 elements for each count array.

So this approach is optimal.

Now, testing some examples.

Take third sample input:1 5.

n=1, m=5.

x_counts:

0: 1//5=0

1: (1-1)//5 +1 =0//5 +1=0+1=1.

2: (1-2) is -1 →-1//5= -1 +1=0.

Similarly 3 and 4: 0.

y_counts[0] =5//5=1.

y_counts[1] = (5-1)/5 +1=4//5=0 +1=1.

y_counts[2] = (5-2)/5 +1=3//5=0 +1=1.

y_counts[3] = (5-3)/5 +1=2//5=0 +1=1.

y_counts[4] = (5-4)/5 +1=1//5=0 +1=1.

So y_counts is [1,1,1,1,1].

Now, for each a in x_counts:

a=0: x_counts[0]=0 → multiply by y_counts[0] →0*1=0.

a=1: x_counts[1]=1 → multiply by y_counts[4] (1) →1*1=1.

a=2: x_counts[2]=0 →0* y_counts[3]=0.

a=3:0*...

a=4:0*...

Total sum is 0+1+0+0+0=1. Which matches the third sample.

Another sample: input 5 7. Output 7.

x_counts for n=5:

a=0:5//5=1.

a=1: (5-1)/5 +1 =4/5=0 +1=1.

a=2:5-2=3 →3/5=0 +1=1.

a=3:5-3=2 →0 +1=1.

a=4:5-4=1 →0 +1=1.

So x_counts = [1,1,1,1,1]

y_counts for m=7:

a=0:7//5=1.

a=1:7-1=6 →6//5=1 →1+1=2.

a=2:7-2=5 →5//5=1 +1=2.

a=3:7-3=4 →4//5=0 +1=1.

a=4:7-4=3 →3//5=0 +1=1.

So y_counts = [1,2,2,1,1].

Now sum:

a=0: 1 * y_counts[0] →1*1=1.

a=1:1 * y_counts[4] →1*1=1.

a=2:1 * y_counts[3] →1*1=1.

a=3:1 * y_counts[2] →1*2=2.

a=4:1 * y_counts[1] →1*2=2.

Sum is 1+1+1+2+2=7. Correct.

So the code works.

Now, implement this in Python.

Read n and m.

Compute x_counts and y_counts.

Compute the total sum.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    def compute_counts(num):
        counts = [0]*5
        counts[0] = num //5
        for a in range(1,5):
            counts[a] = (num - a) //5 +1
        return counts

    x_counts = compute_counts(n)
    y_counts = compute_counts(m)

    total =0
    for a in range(5):
        b = (5 - a) %5
        total += x_counts[a] * y_counts[b]

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
11 14
""",
            "output": \
"""\
31
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

So the code works.
</think>

```python
n, m = map(int, input().split())

def compute_counts(num):
    counts = [0] * 5
    counts[0] = num // 5
    for a in range(1, 5):
        counts[a] = (num - a) // 5 + 1
    return counts

x_counts = compute_counts(n)
y_counts = compute_counts(m)

total = 0
for a in range(5):
    b = (5 - a) % 5
    total += x_counts[a] * y_counts[b]

print(total)
```
