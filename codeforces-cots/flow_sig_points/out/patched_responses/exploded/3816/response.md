<think>
Okay, let's see. The problem is to sort an array of integers in non-descending order. The constraints are n up to 100, and each element is between 1 and 100. Hmm. So the input size is really small here, even for Python. But the question is, what's the most efficient way to do this?

Wait, since the elements are in a small range (1-100), maybe counting sort would be the optimal approach. Because with counting sort, we can sort in O(n + k) time, where k is the range of possible values. Here k is 100, so even if n is 100, it's O(200) which is super fast. That's better than comparison-based sorts like quicksort or mergesort which are O(n log n) and for n=100, log2(100) is like 7, so 100*7=700. But even so, for such small n, maybe any algorithm would work. But counting sort could be more efficient here.

So the steps for counting sort would be:

1. Create a frequency array of size 101 (since elements can be up to 100). Initialize all counts to zero.
2. Iterate through each element in the input array and increment the corresponding index in the frequency array.
3. Then, iterate through the frequency array from 1 to 100, and for each count, add the element that many times to the result array.

This would give us a sorted array in linear time. That's probably the best approach here.

But in Python, since the input is read as individual lines, first we need to read n, then read n lines of integers.

So the steps for the code:

Read n. Then read n integers, one per line. Then count the frequency of each number. Then build the sorted list by iterating from 1 to 100 and appending each number as many times as it occurs.

Yes. That should be straightforward.

Now, considering the memory constraints. Since n is up to 100, and the frequency array is 101 elements, that's negligible. So even for the largest test case, this is manageable.

Let's think about the example input. For the first example, the array is 5 elements: 7,1,9,7,3. The frequency array would have 1:1, 3:1,7:2,9:1. Then building the sorted array would be [1,3,7,7,9], which matches the sample output.

Another example input has a lot of 1s and 100s. Counting sort would handle duplicates easily.

So implementing this in Python:

Read n. Then read n lines, each as an integer. Then create a list counts of 101 zeros. For each number, increment counts[number]. Then iterate from 1 to 100, and for each i, add [i] * counts[i] to the result list. Then join the result into a space-separated string and print.

That's the plan.

Now, for reading input. Since n can be up to 100, reading lines via a loop is fine. In Python, using a list comprehension might be efficient. Like, [int(input()) for _ in range(n)].

But since the elements are read one per line, yes. So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    arr = [int(input_stream.readline().rstrip("\n")) for _ in range(n)]
    counts = [0] * 101
    for num in arr:
        counts[num] +=1
    result = []
    for i in range(1, 101):
        result.extend([i] * counts[i])
    print(' '.join(map(str, result)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
100
1
100
1
100
1
100
1
100
1
""",
            "output": \
"""\
1 1 1 1 1 100 100 100 100 100
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

Second example: 10 numbers, alternating 100 and 1. The counts for 1 would be 5, and 100 would be 5. So the sorted array is five 1s followed by five 100s.

Yes. So this code should work.

Now, considering that in Python, even for n=100, this code is very fast. It's O(n) time. The most efficient possible approach here.

Alternative approaches like using the built-in sort function (sorted(arr)) would also work. For n=100, that's O(n log n) which is negligible. But for the problem's constraints, both approaches are acceptable. However, counting sort is O(n) and more optimal in theory, but in practice, for such a small n, it might not make a noticeable difference. But since the problem asks for the optimal approach, the counting sort is better here.

So the code using counting sort is the best approach.
</think>

```python
n = int(input())
counts = [0] * 101
for _ in range(n):
    num = int(input())
    counts[num] += 1
sorted_list = []
for i in range(1, 101):
    sorted_list.extend([i] * counts[i])
print(' '.join(map(str, sorted_list)))
```
