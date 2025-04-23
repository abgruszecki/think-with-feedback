<think>
Okay, let's see. The problem is about Luba doing chores. Each chore takes a_i time, but she can replace up to k of them with x, which is smaller than all a_i. The goal is to find the minimum total time.

First, I need to understand how to choose which chores to replace. Since replacing a chore with x reduces the time by (a_i - x), to maximize the savings, we should replace the chores with the largest a_i values. Because the array is sorted in non-decreasing order, the largest elements are at the end. So the optimal strategy is to replace the last k elements. Wait, but what if k is larger than the number of elements? Wait, no, the problem says up to k chores. So we can replace min(k, n) chores. But since k can be up to n, which is allowed, as per constraints (k <= n).

So the approach should be:

Calculate the total time by replacing the last k elements with x. But wait, the array is sorted, so the largest a_i's are the last ones. So replacing those gives the maximum possible savings.

So the steps are:

1. Sum all a_i.
2. Subtract the sum of the a_i's for the k largest elements (which are the last k in the sorted array), and add k*x instead.

That's the idea. Because by replacing the largest elements, the difference (a_i -x) is maximized for each replaced element, leading to the maximum possible total savings.

So the algorithm is straightforward. Let's see the examples.

First example:
4 2 2
3 6 7 10
The sum is 3+6+7+10 =26. Replacing the last two (7 and 10) with 2 each. The savings would be (7-2)+(10-2)=5+8=13. So total becomes 26-13=13. Which matches the sample.

Second example:
5 2 1
All a_i are 100. The sum is 500. Replace two with 1. So subtract 2*(100-1) = 198, 500-198=302. Which matches the sample.

So the plan is to compute the total sum, then subtract the sum of the last k elements (since they are the largest), add k*x. The result is the minimal time.

Now, how to implement this.

First, read n, k, x. Then the list a. Since the list is sorted in non-decreasing order, the last k elements are the largest.

So the code can be:

sum_total = sum(a)
sum_replaceable = sum(a[-k:]) if k>0 else 0
saved = sum_replaceable - k*x
result = sum_total - saved

Wait, no. Because saved is sum_replaceable (the sum of the replaced a_i's) minus k*x (the sum after replacement). So the total after replacement is sum_total - (sum_replaceable - k*x) = sum_total - sum_replaceable + k*x.

Yes.

For example, sum_total is sum of all a. Then, sum_replaceable is the sum of the last k a's. So when we replace them with x, their new sum is k*x. So the total sum is sum_total - sum_replaceable + k*x.

So that's the formula.

So code steps:

Read n, k, x.

Read the list a.

sum_total = sum(a)

sum_replace = sum( a[ n - k : ] ) if k >0 else 0

result = sum_total - sum_replace + x * k

But wait, if k is zero? But according to the constraints, 1 ≤k ≤n, so k can't be zero. So no problem.

Wait, looking back at the input constraints: The first line has three integers n, k, x. Constraints are 1 ≤k ≤n ≤1e5? Wait, no, problem statement says:

Constraints:

Time limit per test: 2.0 seconds

Memory limit per test: 256MB

Input constraints:

n can be up to 1e5? Wait, no, the problem says:

Constraints for the input:

n is up to 1e5? Let me check the problem statement again.

Wait, the problem's input constraints are:

n: 1 ≤k ≤n ≤100,000? No, looking back:

Original problem constraints:

Wait, the user here pasted the problem statement, but the constraints here say:

Constraints:

In the problem statement, the user wrote:

Constraints

Time limit per test: 2.0 seconds

Memory limit per test: 256.0 megabytes

Input Format

The first line contains three integers n, k, x (1 ≤ k ≤ n ≤ 100, 1 ≤ x ≤ 99) — the number of chores...

Wait, wait, no. Looking at the problem statement:

In the input constraints section, the user wrote:

n, k, x (1 ≤k ≤n ≤100, 1 ≤x ≤99) — the number of chores...

Wait, no. Wait, the user's problem statement says:

The first line contains three integers n, k, x (1 ≤ k ≤ n ≤ 100, 1 ≤ x ≤ 99) — the number of chores Luba has to do, the number of chores she can do in x units of time, and the number x itself.

So n is up to 100? That's a very small number. So even O(n) solutions would work. But perhaps there's a mistake here, perhaps the original problem had higher constraints. But according to the problem statement given here, n is up to 100.

Wait, but the note in the first example shows that the sample input has n=4, which is within 100. So the constraints are indeed n up to 100.

But this is a bit confusing. Because for n up to 1e5, the solution would still be O(n) which is acceptable. But with n up to 100, even O(n^2) is acceptable.

So the code can just proceed as:

sum_total = sum(a)

sum_replace = sum(a[-k:]) 

result = sum_total - sum_replace + x *k

Yes.

So the code is straightforward.

Wait, but what if the array is not sorted? But the problem statement says that the array is given in non-decreasing order. So the largest elements are the last ones.

So the code is correct.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k, x = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = sum(a)
    replaced_sum = sum(a[-k:]) if k else 0
    print(total - replaced_sum + x * k, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 2 1
100 100 100 100 100
""",
            "output": \
"""\
302
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

Second example: a is [100,100,100,100,100], k=2. sum_replace is 100+100=200. sum_total 500. 500-200=300 +2*1=302.

Yes.

So the code should work.

Now, in code:

Read n, k, x.

Then read the list a as integers.

sum_total = sum(a)

sum_replace = sum(a[-k:])

result = sum_total - sum_replace + x *k

Print(result)

This is simple. So that's the code.

But in Python, when k is 0, but according to the constraints, k is at least 1. So no need to handle k=0.

But the problem statement says 1 ≤k ≤n. So we can assume that.

So the code is correct.

So implementing that.

Now, test case 2:

5 2 1

a is [100,100,100,100,100]

sum_total is 500.

sum_replace is 100+100=200.

result = 500-200 + 2*1 = 300 +2=302.

Yes.

Another test case: what if k is equal to n?

n=3, k=3, x=1, a=[2,3,4]. Then sum_replace is 2+3+4=9. sum_total 9. result is 9 -9 +3*1 =3.

Which is correct.

So the code works.

Thus, the optimal solution is O(n) time, which is acceptable even for n up to 1e5 (but here n is up to 100), so no problem.

Therefore, the code is correct.
</think>

```python
n, k, x = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
replaced_sum = sum(a[-k:]) if k else 0
print(total - replaced_sum + x * k)
```
