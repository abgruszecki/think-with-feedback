<think>
Okay, so I need to solve this problem where given a number n, I have to find all possible x such that x plus the sum of its digits equals n. And then output them in order. Let's think about how to approach this.

First, let's understand the problem. For a given n, find all x where x + sum_digits(x) = n. The sum_digits(x) is the sum of each digit in x. For example, if x is 15, sum is 1+5=6, so 15+6=21. So when n is 21, x=15 is a solution.

Now, how do I find all possible x's efficiently?

The straightforward approach would be to check every possible x from 1 up to n-1 and see if x plus sum_digits(x) equals n. But if n is up to 1e9, this approach is O(n), which is way too slow. For n=1e9, this would be a billion iterations, which would take way longer than a second. So we need a smarter way.

Hmm. Let's think about the possible range of x. Since x must be less than n (because sum_digits(x) is at least 1, so x must be less than n). But even that's too large for checking each possible x.

Wait, but sum_digits(x) can't be larger than the number of digits in x times 9. For example, if x is a 3-digit number, the maximum sum is 27. So for x to satisfy x + sum_digits(x) = n, x must be at least n - (number of digits in x)*9. But how can we use this to limit the possible x's?

Alternatively, for a given x, the sum is x plus sum_digits(x). Let's say x is some number. Let's consider that sum_digits(x) can't be more than 9 * number_of_digits_in_x. So x must be in the range [n - 9*d, n), where d is the number of digits in x. But since the number of digits in x depends on x, maybe we can find a way to iterate over possible x's in a much smaller range.

Another idea: For a given n, the maximum possible sum_digits(x) for x <n is when x is 999...999. The sum_digits would be 9 * digits. For example, if n is 1e9, which has 9 digits, then the maximum sum is 9*9=81. So x must be at least n - 81. So instead of checking all x from 1 to n-1, we can check from max(1, n - 100) up to n-1, since 100 is more than the maximum possible sum_digits for even large numbers.

Wait, let's see. For any x, sum_digits(x) <= 9*d, where d is the number of digits in x. But x must be such that x + s(x) = n. So x = n - s(x). Since s(x) is positive, x <n. But how large can s(x) be? For x to be a positive integer, s(x) can be as big as, for example, 9*9=81 when x is 999,999,999 (but in that case, x is 999,999,999, which is up to 1e9). Wait, but for x in the range of 1e9, s(x) would be up to 9*9=81. So x = n - s(x), which would mean x is at least n-81. So instead of checking all x up to n-1, we can check x from max(1, n-100) down to n-100, but wait, maybe n-100 could be negative if n is small, but for n >=1, we can just take the lower bound as 1.

Wait, but how do we compute the maximum possible s(x) for x <n? For example, x can be as large as n-1. The maximum sum_digits for x in that case would be sum_digits(n-1). But that's not helpful. However, the key insight here is that for x to be a solution, x must be in the range [n - 9*d, n), where d is the number of digits in x. But since x could vary, perhaps we can iterate for x starting from max(1, n - 100) up to n-1, since 100 is a safe upper bound (since for n up to 1e9, the maximum sum_digits(x) for x <n is 9*9=81, so n-81 would be the lower bound). So even for n=1e9, we need to check from 1e9-81 to 1e9-1, which is 81 numbers. That's manageable.

Wait, but wait. For example, if n is 21, as in the first example, the solution is x=15. Then, sum_digits(15) is 6. So x is 21-6=15. So x is in the range 21-6*2 (since 15 has two digits) = 21-12=9. Wait, but that's not correct. The approach of using the number of digits in x to compute the lower bound is a bit tricky because x isn't known. However, for a given n, the maximum possible sum_digits for any x that could satisfy x + s(x) =n is the sum_digits of x where x is n-1. But even that might not be the maximum. Alternatively, the maximum sum_digits for x is when x is all 9's. For example, if n is 1000, then x could be 999 (sum_digits=27), so x would be 1000-27=973. But in that case, 973 is x, and 973 + sum(9+7+3) = 973 +19=992, which is less than 1000. Hmm, maybe not. So perhaps the correct approach is to generate all x's in the range [max(1, n-100), n-1], check each x, and collect those that satisfy x + sum_digits(x) =n. Because 100 is a safe upper bound for sum_digits(x). Because even for a very large x, sum_digits(x) can't be more than, say, 100. Wait, for x with 10 digits, sum_digits(x) is up to 9*10=90, so n-90 would be the lower bound. So for n up to 1e9, sum_digits can be up to 81 (for 9 digits). So the maximum possible s(x) is 9*9=81. So the lower bound for x would be n - 81. So for any n, the possible x's are in the range [max(1, n-100), n-1]. Because 100 is larger than 81, so even for the worst case, 100 numbers need to be checked, which is acceptable.

So the algorithm would be:

1. Iterate x from max(1, n-100) to n-1 inclusive.

2. For each x, compute s = x + sum of digits of x.

3. If s equals n, collect x.

4. After checking all x's in that range, collect all valid x's, sort them, and output the count and the list.

This approach is O(100) per test case, which is acceptable even for n up to 1e9.

Let's test this approach against the examples.

First example: n=21.

Check x from 21-100= -79, but max with 1, so start at 1 to 20.

For x=15: 15 +1+5=21. So that's a valid x.

Other x's in that range may not sum to 21. So the code would find 15.

Second example: n=20.

Check x from max(1, 20-100)=1 up to 19.

For each x in 1-19, check x + sum_digits(x). Let's see:

x=19: 19 + 1+9=29>20.

x=15: 15+6=21>20.

So none of these x's will sum to 20. So output is 0.

Another test case: n=3.

Check x from max(1, 3-100)=1 to 2.

x=1: 1+1=2 !=3.

x=2:2+2=4 !=3.

So output is 0.

Another case: n=1. Then possible x's are from 1-100 (but since x must be <1, the range is empty. So output is 0.

Wait, n is 1. So possible x is 0, but x must be a positive integer. So output is 0.

Wait, the problem statement says "certain positive integer x". So x must be positive. So x starts from 1.

So in code, x starts from max(1, n-100) up to n-1.

Wait, but when n is 1, n-1 is 0, so the loop doesn't run. So no x's, correct.

Another example: n=3. x could be 2, sum is 2+2=4>3. So no solution.

Another example: n=2. x can be 1. sum is 1+1=2. So x=1 is a solution.

So code would check x=1. sum is 2, which equals n. So output is 1, 1.

So this approach works for these cases.

So the plan is:

- Generate all x in the range [max(1, n - 100), n-1]

- For each x, compute sum of digits and check if x + sum equals n.

- Collect all such x's, sort them, and output.

Now, how to compute the sum of digits of x efficiently in Python.

In Python, converting x to a string and summing the digits is straightforward.

But for speed, perhaps using integer operations is faster. But for small x's (since the loop runs 100 times), even converting to string is acceptable.

So for x in the loop:

sum_digits = sum(map(int, str(x)))

But for numbers up to 1e9, converting to string is manageable.

So code steps:

Read n from input.

Compute start = max(1, n-100)

end = n-1

collect all x in start..end where x + sum of digits(x) ==n.

Sort them, then output count and list.

So the code would be something like:

n = int(input())

res = []

start = max(1, n - 100)

for x in range(start, n):

    s = x + sum(int(d) for d in str(x))

    if s == n:

        res.append(x)

res.sort()

print(len(res))

for num in res:

    print(num)

Wait, but why do we need to sort res? Because the x's are iterated in increasing order, so the res list is already in order. Wait, no. Because the loop runs from start to end, which is from start (which could be, say, 5) to n-1. So x increases. So the res list is built in order of x's, which is increasing. So the collected x's are in order, so no need to sort. But wait, what if n-100 is less than 1? For example, n=50. Then start is 1. The loop runs from 1 to 49. So x increases. So any x's found are added to res in order, so res is already sorted. So the output can be printed directly. Therefore, the code can avoid the sort step, which would save some time.

So code can be optimized by removing the sort.

Wait, let's see. For example, n=21. The start is 21-100= -79, but max with 1. So x runs from 1 to 20. The correct x is 15, which is in the middle. So when the loop reaches x=15, it's added to res, which is in order. So the res list is in order because the loop runs in increasing x. So the list is sorted. So no need to sort again. Therefore, the code can proceed without sorting.

So the code can be written as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    result = []

    start = max(1, n - 100)

    for x in range(start, n):

        if x + sum(int(d) for d in str(x)) == n:

            result.append(x)

    print(len(result), file=output_stream)

    for x in result:

        print(x, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20
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

Second example: input 20.

Loop runs from 20-100= -80 → start 1, up to 19.

Check each x. None will sum to 20.

Output 0.

Another test case: n=2. start is max(1, 2-100)=1. x runs from 1 to 1. Check x=1: 1+1=2. So added. Output is 1 and 1.

Another test case: n=3. x ranges 1-2.

x=1: sum is 2 → 3? 1+2=3? 1+1=2 !=3.

x=2: 2+2=4 !=3. So output 0.

Another test case: n=100. The start is 100-100=0 → max(1, 0) →1. Check x from 1 to 99.

Suppose x=86: 86 +8+6=100. So 86 is a solution.

Is there any other x? Let's see.

x=95: 95+9+5=109>100.

x=85:85+8+5=98.

x=86: yes. So code will find 86. Are there others?

Another possible x could be 92:92+9+2=103. No.

x=89: 89+17=106. No.

Hmm, but 86 is one solution. Let's see, are there others?

Wait, x=91: 91+9+1=101.

x=83:83+11=94. No.

Wait, 86 is the correct solution. So code should find 86.

But according to the code, the code would check x from 1 to 99.

So in this case, the code would find 86. So code works.

Another test case: n=19. Let's see.

x=14:14+1+4=19 → yes.

x=17:17+1+7=25. No.

So code would find x=14 as a solution.

So code works.

So the code seems correct.

Now, let's think about possible edge cases.

Case where n=1: output is 0.

n=2: output 1.

n=1000000000 (1e9). Then the code checks x from 1e9-100 to 999,999,999. For each x in that range, compute sum_digits. Then check if x + sum_digits equals 1e9. But the sum_digits for x in 999,999,900 (for example) would be 9*8 + 0*2 =72. So x would be 1e9 -72 = 999,999,928. Then check if 999999928 + sum_digits(999999928) is 1e9. Let's compute sum_digits(999999928): 9+9+9+9+9+9+9+2+8 = 9*7 + 2+8 =63 +10=73. So x=1e9 -73 = 999999927. Then x + sum_digits(x) would be 999999927 + 9*7 + 2+7 = 999999927 +63+9= 999999927+72=999999999. Not 1e9. So perhaps there's no solution here.

But regardless, the code will check all x in 1e9-100 to 1e9-1. So even for large n, the code runs quickly.

So the code is correct and efficient.

Now, implement it in Python.

The code reads n, computes start, loops x from start to n-1 inclusive, checks if x + sum of digits is n. Collects those x's, outputs count and the list.

Yes, that's the code.
</think>

```python
n = int(input())
result = []
start = max(1, n - 100)
for x in range(start, n):
    if x + sum(map(int, str(x))) == n:
        result.append(x)
print(len(result))
for x in result:
    print(x)
```
