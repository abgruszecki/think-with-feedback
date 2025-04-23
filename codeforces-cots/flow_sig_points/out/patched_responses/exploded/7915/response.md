<think>
Okay, I need to solve this problem where I have to check if a given number l is a power of k, and then determine the exponent. But wait, according to the problem statement, the petriciumus cifera numbers are of the form k^m, where m is the number of "la" articles. So the importance is m-1, right? Because the example shows for input 5 and 25 (which is 5^2), the output is YES and importance 1. Oh right, because the first "la" comes after the first petricium. Like "petricium la petricium" is k^2, so two petriciums connected by one "la". So the importance is the number of "la", which is m-1, where m is the exponent.

So the problem reduces to: find if there exists an integer m ≥ 1 such that l = k^m. And then output m-1 as the importance. Wait no, wait. Wait the first example: 25 is 5^2. So the title is "petricium la petricium", which has one "la", so importance 1. So m is 2, importance is 1. So the exponent is m, which is the number of petriciums in the title. So the importance is m-1. So to find m where l = k^m. So we need to find m such that k^m = l, and m must be at least 1 (since k >=2, and l >=2). Then, if such m exists, output YES and m-1. Otherwise, NO.

So the approach is to check if l is a power of k, and if so, compute the exponent m. Then output m-1 as the importance.

But how to compute m efficiently?

Let's think about possible ways. Since k and l can be up to 2^31-1, we need an O(1) or O(log m) approach. Otherwise, for big exponents, looping might be slow.

For example, if k is 2 and l is 2^30, then m would be 30. But looping 30 times is manageable. But what if k is 1? Wait, but the constraints say k and l are at least 2, so no. So k starts from 2.

So the steps would be:

1. Check if l is divisible by k. If not, then it's not a power, so output NO.

2. Otherwise, divide l by k as many times as possible, counting the number of times. If after dividing until l becomes 1, and all divisions were exact, then it's a power. Otherwise, not.

But wait, there's a problem. For example, when l is 1. But l is given as at least 2, so that's not possible. So for l= k^m.

But for example, if k is 4, and l is 16, then 4^2=16. So m is 2, importance 1. So the steps would be: divide 16 by 4, get 4. Divide again by 4, get 1. So count is 2. So yes.

Another example: k=5, l=25. Divide 25 by 5 → 5, then again by 5 →1. Count is 2. So importance is 1. Correct.

But what if k is 6 and l is 6. Then count is 1. Importance 0.

But another approach is to compute m as the logarithm of l to base k, and check if it's an integer. However, due to floating-point inaccuracies, this might not be reliable. For example, log(8)/log(2) is exactly 3, but in floating-point operations, sometimes precision errors occur. So better to avoid that method.

So the loop approach is better. Let's outline the steps:

Initialize m = 0.

While l is divisible by k:

Divide l by k.

m +=1.

If after division, l becomes 1, then return m.

Else, after division, if l is not 1 and not divisible by k anymore, then return -1 (invalid).

So the algorithm is:

m = 0

current = l

while current % k == 0:

    current = current // k

    m +=1

if current == 1 and m >=1:

    return m

else:

    return -1

Then, if the returned m is >=1, then l is k^m, so importance is m-1. Else, no.

Wait, but m starts at 0, and for each division, m increases by 1. So for l=25, k=5:

current is 25. divisible by 5 → current becomes 5, m=1.

Again divisible by 5 → current becomes 1, m=2.

Loop ends. current is 1. So m=2. So importance is 1.

Yes.

So in code, we can implement this loop.

But what about cases where k is 1? But according to the constraints, k is >=2, so we don't need to worry.

Another case: k=2, l=8. The loop would divide 8 by 2 three times (m=3). current becomes 1. So m=3, importance 2.

Which is correct.

Another example: k=3, l=8. The first division gives 8/3=2.666... but since we are using integer division, 8//3 is 2. But 8%3 is 2 !=0. So the loop would exit. current is 8, which mod 3 is 2. So loop doesn't run. m remains 0. So current is 8, which is not 1. So return -1. So output is NO. Which matches the second example.

So the code should work.

Now, the code steps:

Read k and l from input.

Compute m by dividing l by k as long as possible.

Check if after all divisions, the remaining current is 1. If so, and m >=1, then output YES and m-1.

Else, output NO.

But wait, since l must be at least 2, and k is at least 2. So for l=2 and k=2: m=1, current becomes 1. So output YES, importance 0.

Yes.

Now, coding this in Python.

But how to handle big numbers?

For example, if k is 2^30 and l is (2^30)^2 = 2^60. Then in Python, the division would be handled as integers. So even if l is very big, as long as it's a multiple of k, the code will proceed.

So the code would be something like:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    k = int(input_stream.readline().rstrip("\n"))

    l = int(input_stream.readline().rstrip("\n"))

    current = l

    m = 0

    while current % k == 0:

        current = current // k

        m +=1

    if current ==1 and m >=1:

        print("YES", file=output_stream)

        print(m-1, file=output_stream)

    else:

        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
8
""",
            "output": \
"""\
NO
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

Second example:

k=3, l=8.

current=8. 8%3=2 !=0. So loop doesn't run. m remains 0. current is 8 !=1. So output NO.

Another test case: k=2, l=8. m=3. YES 2.

Another case: k=4, l=16. m=2. YES 1.

Another case: k=2, l=6. 6 is divisible by 2 once (6//2=3). m=1. current is 3, which is not divisible by 2. So current isn't 1. So output NO.

So the code works.

What about when l is 1? But according to the input constraints, l is >=2, so no.

Another edge case: k=2, l=2. m=1. Output YES 0.

Another case where k=2 and l=1 is impossible per the input constraints.

So this code should handle all cases correctly.
</think>

```python
k = int(input())
l = int(input())
current = l
m = 0
while current % k == 0:
    current = current // k
    m += 1
if current == 1 and m >= 1:
    print("YES")
    print(m - 1)
else:
    print("NO")
```
