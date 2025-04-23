<think>
Okay, let's see. We need to find the minimum number of moves to make all elements in the matrix equal by adding or subtracting d each time. And if it's impossible, output -1. Hmm.

First, let's think about the conditions for it to be possible. All elements in the matrix must have the same remainder when divided by d, right? Because each move changes the element by d, so their remainder modulo d has to be the same. Otherwise, it's impossible. So the first step is to check all elements. If even one element has a different remainder mod d than the others, return -1.

Once that's confirmed, we need to find the target value such that converting all elements to it requires the least moves. But wait, how do we choose the target? It can't be any arbitrary number. Because each element can only be adjusted by adding or subtracting multiples of d. So all elements must be congruent modulo d. So the target must have the same remainder mod d as all the elements.

But the target can be any number that is congruent to the common remainder. However, since we want to minimize the total steps, the optimal target is the median of the sorted list of possible values. Wait, right. Because the median minimizes the absolute differences. But since all elements must be adjusted to a value that's a multiple of d away from their current value, perhaps the median of the sorted list of adjusted values (divided by d?) would be the best choice.

Wait, let's think. Let's say we have all elements adjusted to their possible values. For example, each element a can be adjusted to a + k*d or a - k*d. But once the target is fixed, the number of steps for each element is (|target - a|)/d. Because each step is adding or subtracting d. So the total steps is sum (|target - a_ij|)/d for all elements. So to minimize this sum, the target should be the median of all the a_ij's. Because the sum of absolute differences is minimized at the median.

Wait, but all elements must be adjusted to a number that is congruent to a_ij mod d. Wait, no. Wait, the target has to have the same remainder mod d as all elements. So all elements after adjustment must equal to target. So target can be any number that is congruent to the common remainder. For example, suppose all elements mod d are r. Then target can be r, r + d, r - d, etc. But since the elements are in the matrix, their possible values after adjustment can be represented as (current value) + k*d or -k*d. So when considering possible targets, they all have to be congruent to r mod d. So the target must be in the same congruence class as all elements.

But to find the minimal steps, perhaps we can collect all the elements, sort them, and then take the median. But wait, when we collect all elements, they all have the same remainder mod d. So when we divide each element by d, the quotient may vary, but the remainder is fixed. So let's consider the elements as (a_i - r)/d. Let me explain. Suppose all elements have remainder r. So a_i = r + k_i*d. So (a_i - r)/d = k_i. So the problem reduces to choosing a target k such that each element's k_i is adjusted to k (since target is r + k*d). Then the number of steps is sum |k - k_i| for each element. Then the minimal sum is achieved when k is the median of the k_i's. So this approach would work.

So the steps are:

1. Check if all elements have the same remainder mod d. If not, return -1.
2. Otherwise, collect all elements, subtract r (the common remainder) from each, divide by d. Get a list of integers k_i.
3. Find the median of this list. The sum of absolute differences to the median gives the minimal steps.
4. The total steps is this sum, which is then the answer.

So the plan is:

- Check the remainder of each element modulo d. If any differ, output -1.
- Else, for each element, compute (a_ij - r) // d. Collect all these into a list.
- Sort this list, find the median (the middle element in the sorted list), then compute the sum of absolute differences between each element and the median.
- Return that sum.

Wait, but why the median? Because the sum of absolute deviations is minimized at the median. That's a well-known statistical fact. So yes.

So, for example, in the first sample input:

Sample 1:
2 2 2
2 4
6 8

All elements are even, so mod 2 is 0. So r is 0.

Each element minus r (0) divided by d (2) gives:

2/2 =1, 4/2=2, 6/2=3, 8/2=4. So the list is [1,2,3,4]. The median can be 2.5, but since the list is even length, the median can be either of the middle elements (2 or 3). Let's see.

If median is 2: sum is (1-2)=1, 0, 1, 2 → sum is 1+0+1+2=4. That's the sample's output. If median is 3: sum is 2+1+0+1=4. So same result. So taking either gives the same sum. So in the code, we can choose either median.

So in code:

Once we have all elements converted to (a - r) // d, we collect them into a list. Sort the list. Then take the middle element (for even lengths, any of the two middle elements is okay, but in code, choosing the one at position len//2 or len//2 -1 will give the same sum because the sum of absolute differences between elements and the median is the same for even-length lists between the two middle elements).

Wait, for even-length lists, the minimal sum is achieved when the median is between the two middle elements. But since our k's must be integers (because the original a_ij's are integers and d is an integer, so (a_ij - r) is divisible by d, and thus (a_ij - r)/d is an integer), then the list is a list of integers. So when the list has even length, there are two middle elements. But the sum of absolute differences will be the same for any k between those two. So in code, taking either of the two middle elements will give the same sum.

For example, in the sample, the sorted list is [1,2,3,4]. The middle elements are 2 and 3. The sum for 2 is (1-2)+(2-2)+(3-2)+(4-2) → 1 +0 +1+2=4. For 3, it's 2+1+0+1=4. Same sum. So in code, choosing either is okay.

So in code, after sorting the list, the median is at the position len//2. So for even lengths, it takes the element at index len//2.

So the steps in code are:

Read n, m, d.

Read the matrix. Check all elements modulo d. If any element % d is not equal to the first element's %d, then return -1.

Else, collect all elements. Compute r = a_11 %d.

For each element, compute (element - r) //d. Collect these into a list.

Sort the list.

Find the median (the middle element).

Compute the sum of absolute differences between each element and the median.

Output that sum.

So now, code.

But how to handle the elements. Let's see.

In code:

First, read n, m, d.

Then read n lines, each with m numbers.

Then check all elements for their mod d.

So:

elements = []
for _ in range(n):
    row = list(map(int, input().split()))
    elements.extend(row)

Then check if all have the same remainder mod d.

r = elements[0] % d

for num in elements:
    if num %d != r:
        print(-1)
        exit()

Then compute the list of (num - r) //d for each.

k_list = [(num - r) //d for num in elements]

Sort k_list.

Compute the median.

sorted_k = sorted(k_list)
median = sorted_k[len(sorted_k) // 2]

sum_steps = sum(abs(k - median) for k in sorted_k)

print(sum_steps)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m, d = map(int, input_stream.readline().rstrip("\n").split())
    elements = []
    for _ in range(n):
        elements.extend(map(int, input_stream.readline().rstrip("\n").split()))

    # Check if all elements have the same remainder modulo d
    remainder = elements[0] % d
    for num in elements:
        if num % d != remainder:
            print(-1, file=output_stream)
            return

    # Convert elements to their adjusted values
    adjusted = [(num - remainder) // d for num in elements]
    adjusted.sort()

    # Find the median and calculate total moves
    median = adjusted[len(adjusted) // 2]
    total = sum(abs(x - median) for x in adjusted)
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2 7
6 7
""",
            "output": \
"""\
-1
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

Wait but earlier example where median is 2 gives sum 4. So regardless of which median is chosen, the sum is the same. So in code, choosing the element at len//2 is correct.

Another sample: second input.

1 2 7

6 7

elements are 6 and 7. 6 mod7 is 6, 7 mod7 is 0. So remainders are different. So output is -1. Correct.

Another test case: what if the list is [1,3], even length. The median would be 3. Sum is 2. If the median is 1, sum is 2. So same sum.

So code is correct.

So this approach should work. The time complexity is O(n*m log(nm)), which for n and m up to 100 (so 1e4 elements) is acceptable. Sorting 1e4 elements is manageable in Python, even with 2 seconds time limit.

Memory-wise, storing all elements in a list is also acceptable. 1e4 integers take negligible space.

So this should be the correct approach.
</think>

```python
n, m, d = map(int, input().split())
elements = []
for _ in range(n):
    elements.extend(map(int, input().split()))

# Check if all elements have the same remainder modulo d
remainder = elements[0] % d
for num in elements:
    if num % d != remainder:
        print(-1)
        exit()

# Convert elements to their adjusted values
adjusted = [(num - remainder) // d for num in elements]
adjusted.sort()

# Find the median and calculate total moves
median = adjusted[len(adjusted) // 2]
total = sum(abs(x - median) for x in adjusted)
print(total)
```
