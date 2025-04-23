<think>
Okay, let's see. The problem is to find the minimum number of bills when Allen withdraws all his money. The denominations are 1, 5, 10, 20, 100. So, the goal is to use as few bills as possible by using the largest denominations first where possible.

Hmm. So the approach here is greedy. Because each larger denomination is a multiple of the smaller ones (except for the 20 which isn't a multiple of 10, but maybe that's handled by the higher denominations). Wait, let me think. The denominations are 1,5,10,20,100. So 100 is the largest, then 20, etc. 

The idea is to take as many of the largest possible bills first, then proceed to the next. So for example, for 125: 100 is used once, then 20 once (20), and 5 once. Total 3. Which matches the example.

So the plan is to start with the largest denomination (100), take as many as possible, subtract that from n, then move to the next largest (20), then 10, 5, and finally 1. But wait, maybe the order isn't exactly descending in the denominations. Let's list them in order from largest to smallest: 100, 20, 10, 5, 1.

Wait, but 20 is bigger than 10. So the order should be 100, 20, 10, 5, 1. So for each step, we take the maximum number of bills possible for the current denomination, then proceed.

So for a given n, the steps would be:

1. Divide n by 100, take the quotient (number of 100 bills), subtract that from n. Add to the count.
2. Take the remaining n, divide by 20, add quotient to count, subtract again.
3. Then 10, then 5, then 1.

But wait, in the second example, 43. Let's see:

100 is 43, no. So next is 20. 43 /20 is 2, 2*20=40. 43-40=3. Then 3 is handled by 3 ones. So total 2+3=5. Which is correct.

Yes, that's right. So the order is 100, 20, 10, 5, 1.

So the algorithm is straightforward: for each denomination in this order, take as many as possible. Because each higher denomination is a larger value than the next, and using as many as possible at each step will minimize the total number of bills.

Wait, but why is this approach optimal? For example, let's see: if I have 25. Using 20 and 5 gives 2 bills, which is better than 10+10+5 (3) or 5*5 (5), etc. So yes. But what if there's a case where taking a smaller number of a higher denomination allows more of a lower one, leading to a better total? Let's think. Let's take n=25. If we take one 20 and one 5: 2 bills. That's optimal. If you take two 10s and a 5: 3. So the greedy approach works here.

Another example: n= 30. 20 +10 would be 2 bills. Alternatively, three 10s: 3. So yes, the greedy approach works here. So the denominations are such that each higher one is a better choice. 

So the denominations are 100,20,10,5,1. The key point is that each denomination in this order is as large as possible, and that using the largest possible first leads to the minimal count. Since all denominations except 20 are multiples of the previous ones (like 100 is 5*20, 20 is 2*10, 10 is 2*5, etc.), but even with 20, the greedy approach works. Because once you subtract the maximum possible 100s, then 20s, etc., there's no better way. For example, if you have 25: taking one 20 and one 5 is better than 5*5. So the approach works.

Therefore, the solution is to process the denominations in the order 100,20,10,5,1, and for each, take as many as possible.

So the steps for the code:

Read n.

Initialize count to 0.

Denominations list: [100, 20, 10, 5, 1]

For each d in denominations:
    count += n // d
    n = n % d
    if n ==0, break

Return count.

Yes. So for example, n=43:

43//100 =0, count remains 0.

n remains 43.

20: 43//20=2 → count +=2 → 2. 43%20=3. n=3.

10: 3//10=0.

5: 3//5=0. 

1: 3 → count +=3. Total 5.

Which is correct.

Another example: 125:

100 → 1 (count 1), n=25.

20 → 1 (count 2), n=5.

5 →1 (count 3). Total 3.

Yes.

Third example: 1e9. 1e9//100 =10,000,000. So count is 1e7. Then n is 0. So output 1e7.

So the code should work.

Now, the code is straightforward. Read n as integer, process each denomination in order.

In Python, the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    denominations = [100, 20, 10, 5, 1]
    count = 0
    for d in denominations:
        count += n // d
        n = n % d
        if n ==0:
            break
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
43
""",
            "output": \
"""\
5
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
    n = int(input_stream.readline().rstrip("\n"))
    denominations = [100, 20, 10, 5, 1]
    count = 0
    for d in denominations:
        count += n // d
        n = n % d
        if n ==0:
            break
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1000000000
""",
            "output": \
"""\
10000000
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

Sample3: 1e9 → 1e9//100=1e8? Wait, 1e9 is 1,000,000,000. Divided by 100 is 10,000,000. So count is 10,000,000. Then remainder is 0. So output 10^7.

Yes.

So the code should work. Now, in Python, even for n up to 1e9, this is O(1) time, as the loop runs 5 times. So no problem with time constraints. Memory is also negligible.

Therefore, this is the optimal approach.
</think>

```python
n = int(input())
count = 0
for d in [100, 20, 10, 5, 1]:
    count += n // d
    n %= d
    if n == 0:
        break
print(count)
```
