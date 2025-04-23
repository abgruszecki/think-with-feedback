<think>
Okay, let's see. The problem is to find the number of ways n people can form two round dances, each consisting of exactly n/2 people. And we have to account for the fact that the order in a round dance is considered the same if rotated. So for example, [1,2,3] is the same as [2,3,1]. 

Hmm. Let's think about the steps needed here. 

First, we need to split the n people into two groups of size k = n/2 each. Then, for each group, we calculate the number of distinct ways to arrange them into a round dance. Then multiply those two numbers and sum over all possible splits. But wait, splitting into two groups might involve some overcounting if the groups are considered as two different groups (like group A and group B) but the problem might treat the two round dances as indistinct. Wait, the problem statement says that the two round dances are separate. So each split into group 1 and group 2 is considered a distinct arrangement unless maybe when swapping the two groups. Wait, but the problem says that each person must be in exactly one of the two dances, so the two groups are separate. But when considering the total number of ways, do we count the order of the two groups as different or not? For example, if group A is first and group B second, is that considered the same as group B first and group A second?

Looking at the examples. For n=4, the sample output is 3. Let's see how that comes. Let's think: possible splits into two groups of 2 each. The number of ways to split 4 people into two groups of 2 is C(4,2)/2. Because choosing which 2 go into the first group, but since the two groups are indistinct (swapping them gives the same configuration), we divide by 2. So for n=4, C(4,2) is 6, divided by 2 gives 3. Then for each group, how many round dances are possible. For a group of size k, the number of distinct round dances is (k-1)! because rotations are considered the same. So for each group of size 2, the number is (2-1)! = 1. So the total is 3 * (1 * 1) =3, which matches the sample. So that makes sense.

So the general approach would be:

1. Choose how to split the n people into two groups of size k each (where k is n/2). Since the two groups are considered as two separate round dances, but the order between the two groups doesn't matter? Wait, in the example where n=4, the answer is 3. Let's see: the split into group [1,2] and [3,4] is considered the same as split into [3,4] and [1,2], right? Because the two round dances are two groups, but the problem counts them as a pair. So when calculating the number of ways, choosing which group is first doesn't matter. So the number of splits is combination(n, k) divided by 2. Because the groups are indistinct. 

So the formula would be:

Number of ways = (C(n, k) / 2) * ( (k-1)! ) * ( (k-1)! )

Where C(n, k) is the combination of choosing k elements from n, which gives the number of ways to split into two groups when order matters. But since the two groups are considered the same (swapping them gives the same total configuration), we divide by 2. Then multiply by the number of arrangements for each group.

Wait, but let's test with n=4. C(4,2) is 6. Divided by 2 gives 3. Then multiply by (1! * 1!) which is 1. So total 3, which matches the sample. For n=2, k=1. C(2,1) is 2, divided by 2 gives 1. Multiply by (0! * 0!) = 1*1 =1. So that's correct.

Another example: n=8. Then k=4. C(8,4) is 70. Divided by 2 gives 35. Multiply by (3! *3! )=6*6=36. 35*36=1260, which matches the sample. So this formula works. 

So the general formula is:

number_of_ways = (C(n, n/2) / 2) * ( ( (n/2 -1)! )^2 )

So now, the problem reduces to computing this formula for a given even n.

Now, how to compute this.

But for n up to 20, even the maximum n is 20, which is manageable. Let's compute combinations.

But let's compute C(n, k) where k is n/2. For example, n=20, k=10. C(20,10) is 184756. Divided by 2 gives 92378. Multiply by (9! )^2. Let's compute 9! is 362880. 362880 squared is 131681894400. Multiply by 92378 gives 12164510040883200, which matches the sample.

So the formula is correct.

So the steps to compute the answer are:

1. Compute combination(n, k), where k = n/2. Then divide by 2.

2. Compute factorial(k-1), then square it.

3. Multiply the two results.

So the problem now is to compute these values efficiently.

Now, for n up to 20, even with precomputed factorials and combinations, it's easy.

But how to compute combinations here?

The formula for combination is n!/(k! * (n-k)! ). Since n is even and k is n/2, n-k is k. So combination(n, k) = n!/(k! *k! )

But then, the formula becomes:

(n! / (k! *k! )) / 2 * ( (k-1)! )^2 )

Simplify this:

n! / (k! *k! ) /2 * ( (k-1)! )^2 )

The k! is k*(k-1)!, so k! =k*(k-1)!.

So substituting:

n! / ( [k*(k-1)!] * [k*(k-1)!] ) / 2 * ( (k-1)! )^2 )

Simplify denominator:

k^2 * (k-1)!^2.

So:

n! * (k-1)!^2 * 1/(k^2 (k-1)!^2 ) ) * 1/2 * ( (k-1)! )^2 )

Wait, perhaps simplifying the expression will make it easier.

Let me re-express the formula.

Original formula:

number_of_ways = [ C(n, k) / 2 ] * ( ( (k-1)! )^2 )

But C(n, k) = n!/(k! * (n -k)! ). Since n is even, k = n/2, n -k = k. So C(n, k) = n!/(k! *k! )

So substituting:

number_of_ways = [ n!/(k! *k! ) /2 ] * ( (k-1)! )^2 )

Simplify the terms:

n! / (k!^2 * 2 ) * (k-1)!^2 )

k! =k*(k-1)!.

So k!^2 =k² * (k-1)!².

So substituting:

n! / (k² * (k-1)!² ) * 2 ) * (k-1)!² )

The (k-1)!² terms in denominator and numerator cancel.

So we get:

n! / (k² * 2 )

So the entire formula simplifies to n!/( 2 * k² ), where k = n/2.

Wait, that's a huge simplification. Let's check with the examples.

For n=4, k=2. So 4! / (2*2²) = 24/(2*4) =24/8=3. Which matches the sample.

n=8, 8! is 40320. 40320/(2*4²) =40320/(2*16)=40320/(32)=1260. Which matches the sample.

n=20: 20! is a big number. 20!/(2*(10^2)) = 20!/(200). Let's compute 20! is 2432902008176640000. Divided by 200 gives 2432902008176640000 / 200 =12164510040883200, which matches the sample.

Wow, so the formula simplifies to (n! ) / ( 2 * (k)^2 ), where k is n/2. So for n=2, k=1. 2!/(2*1^2) = 2/(2*1) =1. Which matches the sample.

So the problem reduces to computing n!/( 2*( (n/2) )^2 )

But wait, let's check:

Yes, because when we substituted all the steps, that's the simplified formula.

So that's the formula. So the answer is (n! ) / ( 2 * ( (n/2) )^2 )

But how to compute this for given n.

In code, for n up to 20, even 20! is 2432902008176640000, which is a 64-bit integer (since 2^64 is about 1.8e19, but 20! is 2.4e18, which is under 1e19, so 64-bit integers can hold it. Python's integers are arbitrary precision, so no problem.

So the steps in code:

1. Compute factorial of n.

2. Compute k = n//2.

3. Compute denominator = 2 * k *k.

4. Divide the factorial by denominator.

So the code is straightforward.

But wait, let's confirm the formula again.

Yes, for n=4, 4! is 24, 2*2*2=8. 24/8=3. Correct.

So in code, the steps are:

Read n.

Compute fact = factorial(n)

k = n//2

result = fact // (2 * k * k )

Print result.

So this is the code.

Now, in Python, how to compute the factorial. Since n is up to 20, even with iterative approach.

But Python's math module has a factorial function. So for code:

Testing against sample input 2.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    k = n // 2

    result = math.factorial(n) // (2 * k * k)

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
""",
            "output": \
"""\
1260
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

</think>

```python
import math

n = int(input())
k = n // 2
print(math.factorial(n) // (2 * k * k))
```
