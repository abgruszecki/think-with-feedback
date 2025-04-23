<think>
Okay, let's see. So the problem is about finding the minimum number of steps Wilbur needs to take to turn an array of zeros into a target array. Each step allows him to either add 1 or subtract 1 to a suffix starting at some index i. So for each step, he picks an i and a direction (add or subtract) and applies it to the suffix.

Hmm. The key here is to model how each step affects the array and find the minimal steps required. Let's think about the operations. Each operation affects a suffix. So, for example, adding 1 to the suffix starting at i will increment all elements from i to the end by 1. Similarly for subtraction.

Let's think of the problem in terms of differences between consecutive elements. Because each operation changes a suffix, the difference between adjacent elements can give us insight into how many operations are needed.

Wait, maybe considering the differences between consecutive elements in the target array. Let's take an example. Suppose the target array is [1,2,3,4,5]. The differences between consecutive elements are 1,1,1,1. Each of these differences would correspond to the number of operations needed starting at each position. Wait, in the first example, the answer is 5. Each step is adding 1 starting at position 1, then 2, etc. So the sum of the absolute differences between consecutive elements, but maybe starting from the first element.

Wait another example: the second sample input is [1,2,2,1]. The differences are 1 (2-1), 0 (2-2), -1 (1-2). The sum of absolute values is 1 + 0 + 1 = 2. But the answer is 3. Hmm, maybe that approach isn't correct.

Wait, perhaps I need to model the required steps as a series of changes that accumulate. Let's consider how each step affects the required deltas.

Let me think about the problem differently. Let's model the required increments as a sequence of operations. Each operation affects a certain range. The total steps would be the sum of the absolute differences between consecutive elements when considering the required target array.

Wait, perhaps the minimal steps required is equal to the sum of the absolute differences between consecutive elements, plus the absolute value of the first element. Let me test this.

Take the first example: the target array is [1,2,3,4,5]. The differences between consecutive elements are 1,1,1,1. Summing their absolute values gives 4. Adding the absolute value of the first element (1) gives 1 +4=5, which matches the sample output. 

In the second example, the target array is [1,2,2,1]. The differences are 1,0,-1. Sum of absolute values is 1+0+1=2. The first element is 1, so 1+2=3, which matches the sample output. 

So that seems to fit. So the formula is the sum of absolute differences between consecutive elements, plus the absolute value of the first element. Wait, but why?

Because each step affects a suffix. Let's think of building the array from left to right. The first element can only be changed by operations that start at index 1. The difference between the first and second element (b1 and b2) is determined by the number of operations that start at index 2. Because once you start at index 2, you don't affect the first element anymore.

So the initial value is zero. Let's model the process as the difference between the current array and the target array. Let's imagine the required changes as a series of steps. Each step adjusts a suffix.

Let’s represent the target array as a sequence of differences from the initial array (which is all zeros). For example, for the first sample, the target is [1,2,3,4,5]. The required steps would be adding 1 at position 1, which affects all elements. Then adding 1 at position 2, which affects elements 2-5. Then 3, 4, 5. Each step contributes to the difference between consecutive elements.

Alternatively, the problem can be transformed into considering the required changes as a series of steps, where each step corresponds to a certain position. The total number of steps is the sum of the absolute differences between consecutive elements in the target array, plus the absolute value of the first element.

Wait, let's model the problem in terms of the required increments. Let's define d_i as the difference between the target array's i-th element and the (i-1)-th element, for i >= 1 (with the 0-th element being 0). So for the first element, d_1 = b_1 - 0 = b_1. For i>1, d_i = b_i - b_{i-1}.

Wait, perhaps that's the right approach. Because each operation at position i affects the current and all subsequent elements. So, the number of times you need to perform an operation starting at position i is exactly the difference between the desired change at position i and the previous positions.

So, the total number of steps is the sum of the absolute values of all d_i. Because each d_i represents the net number of operations that must start at position i. For example, if d_1 is 5, that's 5 operations starting at 1, either adding or subtracting. Then d_2 would be the difference between the desired b_2 and b_1, which must be achieved by operations starting at position 2. Because any operation before that (started at 1) would affect both positions. So each d_i is the required change that can only be achieved by starting operations at position i.

Yes, this makes sense. So the minimal steps is the sum of the absolute values of d_i for all i from 1 to n, where d_1 = b_1, and d_i = b_i - b_{i-1} for i>1.

Let's test this with the sample inputs.

First sample: b is [1,2,3,4,5]. So d_1=1, d_2=1, d_3=1, d_4=1, d_5=1. Sum of absolute values is 1+1+1+1+1=5. Correct.

Second sample: [1,2,2,1]. d_1=1, d_2=1 (2-1), d_3=0 (2-2), d_4=-1 (1-2). Sum of absolute values: 1+1+0+1=3. Correct.

So this formula works. Therefore, the solution is to compute the differences d_i as described and sum their absolute values.

So the approach is:

1. Compute the differences between consecutive elements in the target array. The first element is the difference from zero (since initial array is all zeros). Then each subsequent element is the difference from the previous element in the target array.

2. Sum the absolute values of all these differences. This sum is the minimal number of steps required.

Now, considering the constraints. The input can be up to 200,000 elements. So the algorithm must be O(n), which is manageable.

For the implementation:

- Read n.

- Read the list of b elements.

- Compute the differences. Start with previous = 0. For each element in b, compute current difference as b[i] - previous. Add the absolute value to the total. Then set previous to b[i].

So, in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))
    prev = 0
    steps = 0
    for num in b:
        diff = num - prev
        steps += abs(diff)
        prev = num
    print(steps, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 2 2 1
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

Second sample input:

4

1 2 2 1

prev=0. first diff is 1. steps 1.

prev=1. next is 2, diff 1. steps 2.

prev=2. next is 2. diff 0. steps 2.

prev=2. next is 1. diff -1. steps 3. Correct.

So this code works for the samples. Therefore, this approach is correct.

The algorithm runs in O(n) time and uses O(1) additional memory, which is optimal for the constraints.
</think>

```python
n = int(input())
b = list(map(int, input().split()))
prev = 0
total = 0
for num in b:
    diff = num - prev
    total += abs(diff)
    prev = num
print(total)
```
