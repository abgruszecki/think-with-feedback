<think>
Okay, let's tackle this problem. Hmm, the problem is about arranging numbers in a grid and then reading them in a different order. Let me try to understand it step by step.

So, originally, the numbers are placed in a grid with n rows and m columns. They are filled left to right, top to bottom. So the first row is 1 to m, second is m+1 to 2m, etc. Then, when writing them down, we take them column-wise, top to bottom, left to right. So first column's numbers are written first, then the second column, etc. We need to find the k-th number in this written sequence.

The example given: n=3, m=4, k=11. The original grid is:

1  2  3  4
5  6  7  8
9 10 11 12

When written column-wise, it's 1,5,9,2,6,10,3,7,11,4,8,12. The 11th element here is 8. Which matches the example output.

So the task is, given n, m, k, find the k-th number in the column-wise sequence.

The constraints are n and m up to 20000 each. So the maximum possible product is 20000*20000 = 4e8. If we try to build the grid, it's impossible for large n and m because that would require O(nm) memory, which for 4e8 elements is way beyond the memory limit. So we need a mathematical approach to compute the k-th element without constructing the grid.

Let's think about the problem. The written sequence is formed by taking each column from top to bottom. Each column in the original grid has n elements. But how many columns are there? m columns.

Wait, in the original grid, the number of columns is m. So when written column-wise, the first n elements are from column 1, next n from column 2, and so on. But each column has exactly n elements. So for any k, the position can be determined by finding which column and which row in that column the k-th element is located.

Wait, the written sequence is all the elements of the first column (n elements), then the second (another n), etc. So for k, the column index is (k-1) // n + 1. Because the first n elements are column 1, next n column 2, etc. But wait, what if m is such that some columns have less than n elements? No, the original grid has exactly m columns each with n rows, right? Because the numbers are arranged from 1 to n*m. So each column has exactly n elements. So the written sequence has exactly m columns, each contributing n elements. Therefore, the total number of elements is n*m, which matches.

So for example, with n=3 and m=4, each column has 3 elements. So for k=11, the 11th element is in column (11-1)//3 +1 = (10//3)+1 = 3+1=4th column? Wait, wait: 10//3 is 3, so 3+1=4. But in the example, the 11th element is in column 4 (the elements of column 4 are 4,8,12. Wait, no, the written sequence is columns 1,2,3,4. Each column has 3 elements. So columns 1: 3 elements (1,5,9), column 2: 3 elements (2,6,10), column 3: 3 elements (3,7,11), column4: 3 elements (4,8,12). So the 11th element is the 11- (3*3) = 11-9=2nd element of column4. So that's 8. Which is correct.

So the general approach is:

1. Determine which column the k-th element is in. Since each column contributes n elements, the column index is (k-1) // n. But wait, columns are 1-based in the original grid. Wait, in the code, the columns are 1-based. Wait, in the example, the first column is column 1. So for k=1, it's column 1. For k=3, it's column 1. For k=4, it's column 2. So the column index (1-based) is (k-1) // n + 1. The row within the column (the position in the column) is (k-1) % n + 1.

Once we know which column and row in the column, we need to find the original number in the grid at that position.

But how is the original grid structured? The original grid is filled row-wise. So the number at row i, column j is (i-1)*m + j.

Wait, original arrangement: first row is 1, 2, ..., m. Second row is m+1, m+2, ..., 2m. So row i (1-based) starts at (i-1)*m + 1. So the element at row i, column j is (i-1)*m + j.

In the written sequence, each column's elements are read top to bottom. So for column c, the elements are from row 1 to row n. So the elements in column c are (1-1)*m +c, (2-1)*m +c, ..., (n-1)*m +c. Which is c, m+c, 2m+c, ... (n-1)m +c.

So for column c, the elements are (i-1)*m + c for i from 1 to n.

But in the written sequence, the order is column 1, row 1, row 2, ..., row n; then column 2, same, etc. So for the k-th element, once we find the column c and the row r in the column (r is 1-based), then the number is (r-1)*m + c.

Wait, yes. For example, in the first example, column 4, row 2: (2-1)*4 +4= 4+4=8. Which matches the example.

So the formula is:

c = (k-1) // n + 1

r = (k-1) % n + 1

number = (r-1)*m + c

But wait, wait. Let's re-express this. The written sequence is all columns in order. Each column has n elements. So column c has elements at positions (c-1)*n + 1 to c*n in the written sequence. For a given k, c is the column index (1-based) such that (c-1)*n < k <= c*n. So solving for c:

c = ceil(k / n) → but since k can be up to n*m, c ranges from 1 to m.

But (k-1) //n gives the (c-1) part. For example, if k is 4, n=3: (4-1)//3=3//3=1 → c=1+1=2. Which is correct.

Once c is known, the position within the column is (k-1) %n +1. For k=4: (4-1)%3=0 → r=1. So element is (1-1)*m +c → 0*m +2=2. But in the example, column 2's first element is 2. Yes.

So the formula holds.

Therefore, the problem reduces to calculating c and r as above, then computing (r-1)*m + c.

But wait, the example 2: n=20000, m=10000, k=200000000. Let's see:

n=20000, m=10000. So columns are 10000 in number. Each has 20000 elements. The k is 200000000.

Compute c = (200000000 -1) // 20000 +1 → (199999999) // 20000 = 199999999 /20000 = 9999.99995 → which is 9999. So c= 9999 +1= 10000. Then r = (200000000-1) % 20000 +1 → 199999999 mod 20000 is 199999999 - 20000*9999= 199999999 - 199980000=19999. So r=19999+1=20000.

So the number is (20000-1)*10000 +10000 → 19999*10000 +10000 = 199990000 +10000 = 200000000. Which matches the example.

So the formula works.

So the steps are:

1. Calculate column c = (k-1) // n + 1. But wait, m is the maximum column. What if (k-1)//n +1 exceeds m? For example, n=3, m=4, k=12. Then (12-1)//3=11//3=3 → c=4. Which is okay. Because m is 4. So when k is up to n*m, which is m columns each of n elements, the maximum c is m. So in code, we need to ensure that c does not exceed m. But since k is given to be up to nm, (k-1)//n can be at most (nm-1)//n = m-1. Because nm-1 divided by n is m -1. So (k-1)//n is (m-1) when k=nm. Then c = m-1+1= m. Which is correct. So no problem.

So in code:

c = (k-1) // n + 1

r = (k-1) % n + 1

result = (r-1)*m + c

That's all.

This is O(1) time and space, which is optimal. Because for n and m up to 2e4, even 1e8 operations would take time, but this is O(1).

So the code can be written as:

Read n, m, k.

Compute c = (k-1) //n +1

r = (k-1) %n +1

result = (r-1)*m +c

Print(result)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().rstrip("\n").split())
    c = (k - 1) // n + 1
    r = (k - 1) % n + 1
    print((r - 1) * m + c, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20000 10000 200000000
""",
            "output": \
"""\
200000000
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

Second example: 20000,10000,2e8. As discussed, correct.

What about when k is exactly n*m. Then c= (n*m-1)//n +1= (n*m-1)//n= m-1 + ( (n*m-1) mod n )/n. But (n*m-1) =n*(m-1) + (n-1). So (n*m-1)//n= m-1. So c= m-1+1= m. r= (n*m-1) %n +1 = (n-1) +1= n. So result is (n-1)*m +m= nm. Which is correct.

Another test case: k=1. c= (0//n)+1=0+1=1. r=0%n +1=0+1=1. (0)*m +1=1. Correct.

So the formula works.

So this approach is optimal and handles all constraints. The code is straightforward and runs in O(1) time, which is perfect for the given constraints.
</think>

```python
n, m, k = map(int, input().split())
c = (k - 1) // n + 1
r = (k - 1) % n + 1
print((r - 1) * m + c)
```
