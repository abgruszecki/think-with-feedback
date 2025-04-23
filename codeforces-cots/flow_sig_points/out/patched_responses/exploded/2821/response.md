<think>
Okay, let's see. The problem is about Sereja's restaurant and the coat hooks. So, the task is to calculate the profit he makes based on the guests using the hooks and any fines incurred. Hmm.

The input gives n hooks, each with a cost ai. Then m guests come. Each guest picks the cheapest available hook. If there's no hook available when a guest arrives, Sereja has to pay d rubles as a fine. The profit is the sum of the used hooks' costs minus the fines from guests who couldn't get a hook.

Wait, the key points are:

1. Guests arrive one by one, each time picking the smallest available ai.
2. Once a hook is used, it's no longer available for later guests.
3. If there are no available hooks when a guest comes, add a fine of d.

So the steps to solve this:

First, process the m guests. For each guest:
- If there's at least one hook available, take the smallest ai from the available ones, add it to the profit, and mark that hook as used.
- If no hooks are available, subtract d from the profit.

But how to efficiently get the smallest available ai each time? Since n is up to 100 and m up to 100, even a straightforward approach would work here. Because even if we sort the hooks once and then pick the first m, but considering that after each use, the next smallest is taken. Wait, but the initial order of the hooks isn't the issue. The guests always choose the smallest available. So if we sort the hooks in ascending order, then the first m guests would take the first min(n, m) hooks. Any guests beyond n would each cost d rubles.

Wait, that's a crucial insight. Because all guests arrive at different times. Each guest will take the smallest available hook. So once the hooks are sorted in increasing order, the first m guests would take the first m hooks in order. But if m exceeds n, then the first n guests take the hooks, and the remaining (m-n) guests each add a penalty of d.

So the steps are:

1. Sort the array a in ascending order.
2. Sum the first k elements, where k is the minimum of m and n. That's the total income from the hooks used.
3. For the remaining (m - k) guests, each contributes a penalty of d. So subtract (m - k)*d from the total.

Wait, that's right! Because the first m guests (if m <= n) take the first m smallest hooks. But if m is larger than n, then the first n take the hooks, and the rest (m-n) pay penalties.

So the solution can be broken down into:

Sort the hooks in ascending order.

sum = sum of the first min(m, n) hooks.

penalty = max(0, m - n) * d

profit = sum - penalty

That's it! Because the order in which the guests take the hooks doesn't matter as long as each guest takes the smallest available. Since the first min(m,n) hooks are the smallest ones, their sum is the maximum possible income (since Sereja wants to minimize the penalty but the guests take the smallest available).

So for example, in the first test case:

n=2, d=1, a=[2,1], m=2.

Sort a becomes [1,2]. Sum is 1+2=3. No penalty. Profit is 3.

In the second test case, m=10. So sum the first 2 hooks (1+2=3), then subtract (10-2)*1=8. 3-8 = -5. Which matches the sample.

So this approach works, and it's very efficient. Sorting the array takes O(n log n) time, which is negligible for n up to 100. The rest is O(1) operations.

So the steps for code:

Read n and d.

Read the array a.

Sort a in non-decreasing order.

Compute k = min(m, n). Sum the first k elements.

Compute the penalty: max(0, m - n) * d.

Profit is sum - penalty.

So code in Python would be straightforward.

Wait, but the third input line is m. Let's check the input format.

The first line is n and d.

Second line has a list of n integers.

Third line is m.

So in code:

n, d = map(int, input().split())

a = list(map(int, input().split()))

m = int(input())

Then sort a.

sum_hooks = sum(a[:min(m, n)])

penalty = max(0, m - n) * d

print(sum_hooks - penalty)

Wait, but a has exactly n elements. When m is larger than n, sum the first n elements. For m less than n, sum first m elements. So that's correct.

Yes. So this code should work for all cases.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, d = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    m = int(input_stream.readline().rstrip("\n"))
    a.sort()
    k = min(m, n)
    total = sum(a[:k]) - max(0, m - n) * d
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 1
2 1
10
""",
            "output": \
"""\
-5
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

n=2, m=10. sum first 2 elements (1+2=3). m-n=8. 8*1=8. 3-8=-5. Correct.

Another test case where m is 3, n=3. Sum all 3 elements, no penalty.

Another case: n=3, m=5. Sum 3 elements, penalty (5-3)*d.

So the code is correct. And since the constraints are small (n, m up to 100), this code is efficient enough. Time and memory are not an issue here.

Thus, this approach is optimal. The sorting is O(n log n), but even for n=1e5, that's manageable, but here n is 100. So the code is optimal.
</think>

```python
n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
a.sort()
k = min(m, n)
total = sum(a[:k]) - max(0, m - n) * d
print(total)
```
