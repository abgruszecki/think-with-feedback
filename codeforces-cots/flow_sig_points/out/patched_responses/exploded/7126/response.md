<think>
Okay, let's tackle this problem. Hmm. So the task is to find the earliest day where the sum of problems up to that day is at least half of the total sum of all days. Wait, wait. Wait, more precisely, half or more of the total. Because the equator is the first day where the cumulative sum up to and including that day is >= half of the total sum of all days. Oh right, because the equator is when you've passed the halfway point. So once that day is reached, he'll celebrate that evening.

So first, I need to compute the total sum of all a_i. Then, find the smallest index k such that the sum of the first k elements is >= total_sum / 2. But wait, since division could be fractional, like if the total is odd. For example, if total is 7, half is 3.5, so the sum needs to be >=3.5. So the first day where the sum reaches 4 would be the one. So in the first example, sum is 1+3+2+1=7. Half is 3.5. The sum after day 1 is 1, which is less. After day 2, sum is 4, which is >=3.5. So output day 2.

So the approach would be:

1. Compute the total sum of all a_i.
2. Iterate through the days, accumulating the sum as we go. The first day where the accumulated sum is >= (total_sum +1 ) // 2? Wait, no. Wait, if total_sum is even, then half is total_sum /2. But if it's odd, then half is (total_sum +1)/2. For example, 7 is 3.5. So to capture that, perhaps compute the required sum as (total_sum +1) // 2. Because in integer division, for even numbers, (7+1)//2 is 4, which is correct. Wait, no. Wait, 7//2 is 3.5. So to get the minimal sum that is >= half, we need to take the ceiling of total_sum / 2. Which can be computed as (total_sum +1) // 2. Because for even numbers, like 6: (6 +1)/2 = 3.5, integer division gives 3. But 6/2 is 3. So the ceiling is 3. So (6 +1)//2 is 3.5 → 3 in integer division. Wait, no. Wait, in Python, (7 +1)//2 is 4. (6 +1)//2 is 3.5, but since it's integer division, it's 3. So yes, that's correct. So required_sum is (total_sum +1) // 2.

So steps:

Calculate total_sum = sum(a)
required = (total_sum +1) // 2

Then iterate through the array, accumulating the sum. Once the accumulated sum reaches or exceeds required, return the current index (1-based).

Yes. That makes sense.

Now, the question is about handling the input efficiently and processing it. Since the constraints are up to 200,000 elements, we need to read the input efficiently.

In Python, reading input with input().split() can be slow if the array is big, but for 2e5 elements, it's manageable as long as we read it properly. So, for the second line, we can read all the elements as a list of integers.

So the plan is:

Read n.

Read the array a as a list of integers.

Compute total_sum = sum(a). Then required = (total_sum +1) // 2.

Then iterate through the array, accumulating the sum. Once the accumulated sum >= required, return the index (i+1, since days are 1-based).

But wait, what if the sum reaches exactly half? For example, total sum is 12, required is 6. So in the second example, sum after day 3 is 6, which is exactly required. So that's the correct day.

Yes.

So the code structure would be:

Read n.

Read list a.

Compute total_sum and required.

Initialize current_sum =0.

Loop through each element in a, with index i (0-based).

Add the current element to current_sum.

If current_sum >= required:

   return i+1 (since days are 1-based) and break.

This should work.

Now, let's test with the examples.

First example:

Input:

4

1 3 2 1

sum is 7, required is (7+1)//2 =4.

The accumulated sum after day 1 is 1 <4. After day 2, 4 >=4 → return 2. Correct.

Second example:

6

2 2 2 2 2 2 → sum 12, required is (12+1)//2 =6.5 → 6.5 is 6.5, but since it's integer division, (12+1)//2 is 13//2=6. So required is 6. The sum after 3 days is 2+2+2=6 → equals required. So return 3.

Yes.

Another example: if the sum is 3, required is 2. So the first element >=2 would be day 1 if a1 is 2 or more. Otherwise, check cumulative.

So the code seems correct.

Now, in terms of efficiency: the code is O(n) time, which is acceptable for n up to 2e5. It's optimal because we need to process each element once. There's no way to do better than O(n), since all elements contribute to the sum.

Space-wise, the code uses O(n) space to store the array, which is acceptable. But wait, since we're just accumulating the sum, maybe we can process the elements as we read them, without storing the entire array. That would save space. Oh right! Because once we read each a_i, we can accumulate the sum and check immediately. So, for example, read the array elements one by one, and accumulate the sum, and check if it's >= required. Once it is, output the current index and exit.

But how to read the elements as a list in Python efficiently? Wait, but for the sum, we need to compute the total sum first. So that's the problem. Because the code needs to first compute the total_sum, which is sum of all elements, and then compute required. Then iterate again through the elements to accumulate until we reach required.

But if n is 2e5, then storing the array is 2e5 integers. Which in Python is acceptable, as each integer is about 28 bytes (for small ints), but 2e5*28 is about 5.6MB, which is way below the memory limit.

Alternatively, can we compute the total sum in a first pass, then process the elements again? That would require two passes. But if the input is read as a list, that's manageable. But if the input is very large, perhaps we can read the elements in a generator, but in practice, for Python, reading the entire list at once is manageable.

But given that the problem allows for 256MB per test case, and even 2e5 integers would take maybe 1.6MB (since in Python, each integer is stored as a pointer, which depends on the system, but 2e5 * 4 bytes (for 32-bit) would be 0.8MB. But in reality, Python's integers are objects, so it's more. But even so, 2e5 elements are manageable.

So the approach would be:

Read the entire list, compute the sum. Then iterate through the list again, accumulating until the required sum is reached.

Alternatively, read the list once, sum it, then iterate again. But that's O(n) time for sum and O(n) time for processing. Still O(n) overall.

Alternatively, read the elements, store them in a list, compute sum, then iterate through the list. So code steps:

Read n.

Read the list a.

total_sum = sum(a)

required = (total_sum +1)//2

current_sum =0

for i in range(n):

   current_sum += a[i]

   if current_sum >= required:

       print(i+1)

       exit()

But this code would work. Now, in terms of memory, storing a list of 2e5 elements is manageable.

But wait, can we do this without storing the list? Like, read the elements, compute sum in a first pass, then read the elements again (but that's not possible because once you read from stdin, you can't re-read). So perhaps, the only way is to read the elements once, store them, compute the sum, then process them again. But that's O(n) memory.

Alternatively, when reading the elements, store them in a list. So no problem.

Another approach: read the elements as a string, split into a list of strings, convert to integers, sum them. Then process the list again.

So the code is straightforward.

In Python, using input().split() for the second line can read all the elements. So for example:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    sum_total = sum(a)

    required = (sum_total +1) // 2

    current = 0

    for i in range(n):

        current += a[i]

        if current >= required:

            print(i+1, file=output_stream)

            break



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
2 2 2 2 2 2
""",
            "output": \
"""\
3
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

Second example: sum 12 → required 6.

i=0: 2 → current 2 <6.

i=1: 4 <6.

i=2: 6 → equals required. print 3.

Yes.

Another test case: n=1. Then required is (a1 +1)//2. For a1=1, required is 1. So sum after day 1 is 1. Output 1.

For a1=3: sum is 3. required is (3+1)/2=2. sum after day 1 is 3 >=2 → output 1.

So code handles that.

Edge Cases:

All elements are 1, n=200000. The required sum is (200000 +1)//2 = 100000.5 → 100000.5 → but integer division in Python is (200000)//2 + (1)//2 → 100000. So sum up to 100000 elements would be 100000. So the 100000th day would be the one.

But if the required is 100000.5, then sum must be >=100000.5. So 100000 would not be enough, but 100001 is required. So if the elements are all 1, then the sum after k days is k. So when does k >= (sum_total +1)/2?

sum_total = 200000 → required (200000+1)//2 = 200001//2=100000.5 → 100000.5. So the sum needed is 100001. So the 100001st day would be the answer. But in the code, required is (200000+1)//2 → 200001//2=100000.5 → but integer division in Python truncates, so 100000.5 becomes 100000. So required is 100000. Wait, no: (200000 +1) is 200001, divided by 2 using integer division gives 100000.5 → but in Python 3, it's 100000. So required is 100000. Then the sum after 100000 days is 100000, which meets required. So code would output 100000. But wait, sum_total is 200000, required is 100000. So the code would return 100000. But according to the problem statement, the required is half or more. 100000 is exactly half. So it's correct. So code works.

Wait, but in this case, sum_total is even. (sum_total=200000). So required is 200000/2 =100000. So the code's approach of (sum_total +1)//2 is (200000+1)//2=200001//2=100000.5 → 100000 in integer division. So code uses required=100000. So the first day where sum reaches 100000 is day 100000, which is correct.

So code works.

Another edge case: all elements are zero. But according to the constraints, a_i >=1. So no, that's impossible.

Another case: sum is zero. But sum is sum of a_i, which are all >=1. So sum is at least n >=1.

So code handles all cases.

In terms of Python's efficiency, for n=2e5, the code runs in O(n) time, which is acceptable.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
required = (total + 1) // 2
current = 0
for i in range(n):
    current += a[i]
    if current >= required:
        print(i + 1)
        break
```
