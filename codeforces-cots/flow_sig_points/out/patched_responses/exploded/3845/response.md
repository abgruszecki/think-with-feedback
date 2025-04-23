<think>
Okay, let's see. The problem is to sort an array of integers in non-descending order. The input is a single line where the first number is the size n, followed by n elements. The output should be the sorted array.

First, I need to read the input correctly. The input is a line of space-separated integers. So, I can split the input line into a list of integers. The first element is n, and the rest are the array elements. For example, if the input is "3 3 1 2", then n is 3, and the array is [3,1,2]. Wait, no. Wait, the first number is n. Then the next n numbers are the array. So in that case, the example input is split into [3,3,1,2], so n is 3, and the array is [3,1,2]? Wait, no, wait. Wait, the input line is "3 3 1 2". The first number is n=3. Then the next 3 numbers are the array elements: 3, 1, 2. So the array is [3,1,2], which after sorting becomes [1,2,3].

So the first step is to read the entire line, split into integers, take the first as n, then the next n as the array. Then sort the array and output the elements space-separated.

Now, considering the constraints. The maximum n is 10. So even a O(n²) algorithm like bubble sort would be acceptable here. But in Python, the easiest way is to read the array, sort it using the built-in sort function, which is O(n log n) and more than efficient enough for n up to 10.

So the steps are:

1. Read the input line.
2. Split into parts as integers.
3. The first element is n. Check that the following elements are exactly n in number.
4. Slice the array from the second element to n+1, since the first is n.
5. Sort the array.
6. Print the elements separated by spaces.

But in the example input given, the first example input is "3 3 1 2". So after splitting, the list is [3,3,1,2]. So the array is the elements [3,1,2], which after sorting is [1,2,3].

So for the code, the steps would be:

Read the entire line using input(). Split into parts as integers.

Then, n is the first element. The array is the elements from index 1 to 1 + n (exclusive?), because after the first element (index 0), the next n elements are the array.

Wait, for example, in the first case, the list after split is [3,3,1,2]. So elements 1 to 4 (since 1+3=4). So indexes 1, 2, 3. That gives [3,1,2].

So in code:

data = list(map(int, input().split()))
n = data[0]
arr = data[1:1 + n]

Then sort arr.

Then print ' '.join(map(str, sorted_arr)).

But wait, what if the input has more elements than n? According to the problem statement, the input is correct. So perhaps the problem ensures that. So we can safely take the first n elements after the first one.

So the code is straightforward.

Now, considering the constraints. Since n is up to 10, and each element up to 100, even the most basic approach is acceptable.

But in Python, the fastest way is to read the input, split, process, sort, and output.

So the code would be:

Read the input line, split into integers.

n is first element.

array is next n elements.

sort the array.

print space-separated elements.

So the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    data = list(map(int, input_stream.readline().rstrip("\n").split()))
    n = data[0]
    arr = data[1:n+1]
    arr.sort()
    print(' '.join(map(str, arr)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 12 2 3 44 5 60 2
""",
            "output": \
"""\
2 2 3 5 12 44 60
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

Second example input: "7 12 2 3 44 5 60 2". data is [7, 12,2,3,44,5,60,2]. So arr is elements from index 1 to 8 (7+1=8), so indexes 1 to 7 inclusive. That gives [12,2,3,44,5,60,2]. After sorting: [2,2,3,5,12,44,60], which matches the output.

So the code should work.

Now, considering edge cases. For example, n=1. Input is "1 5". Output is "5".

Another case: all elements the same. Like input "4 5 5 5 5" → sorted as 5 5 5 5.

So the code seems to handle these cases.

Now, about reading input. Using input().split() is fine. For very large inputs, but here n is up to 10, which is trivial.

So this code should work.
</think>

```python
data = list(map(int, input().split()))
n = data[0]
arr = data[1:n+1]
arr.sort()
print(' '.join(map(str, arr)))
```
