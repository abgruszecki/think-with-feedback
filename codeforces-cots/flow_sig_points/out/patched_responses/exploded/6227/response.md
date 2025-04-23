<think>
Okay, let's see. We need to find the minimum number of operations to get at least k equal numbers in the array by dividing elements by two (flooring them). Each operation is a division by two, and we can choose any element any number of times.

Hmm. The idea is to track for each possible number, how many steps it would take to get other elements to reach that number. Then, for each possible number, collect the steps required from enough elements (at least k) and take the sum of the smallest k steps. The minimum among all such sums is the answer.

So the steps are as follows:

1. For each element in the array, generate all possible values it can take by dividing by two repeatedly, along with the number of steps taken to reach each value. For example, if the element is 5, the values would be 5 (0 steps), 2 (1 step), 1 (2 steps), 0 (3 steps), etc.

2. For each of these values, store the steps required in a dictionary or a list. Then, for each value, if there are at least k elements that can reach it, sum the k smallest steps and track the minimum such sum.

The challenge is to efficiently compute this for all possible values without exceeding time or memory limits, given that n can be up to 2e5.

Wait, how do we handle this efficiently? For each element, generating all possible values it can take would be O(log a_i) steps per element. Since a_i can be up to 2e5, log2(2e5) is around 18, so per element it's manageable. So for 2e5 elements, that's about 3.6e6 operations, which should be okay.

Once all possible values and their steps are generated, we can use a hash map (like a defaultdict(list)) where the key is the possible value, and the value is a list of steps needed for elements to reach that value. Then, for each key in the map, if the list's length is at least k, we sort the list, take the first k elements' sum, and keep track of the minimum such sum.

So the steps would be:

- Initialize a defaultdict(list) called counts.

- For each number in the array:
   - Initialize steps as 0.
   - While the current value is >=0:
      - Add steps to counts[value].
      - If current value is 0, break (since next division would still be 0, but steps would keep increasing, but adding those would be unnecessary as 0 can't be divided further).
      - Otherwise, divide by 2, steps +=1.

Wait, but when the value is 0, we can't divide anymore. So for each element, we generate all the values until we reach 0, but once it's 0, we stop. Because after that, each division would keep it at 0 but steps would increase, but those steps are unnecessary. So for example, if an element is 3, the steps would be:

3 (0 steps), 1 (1 step), 0 (2 steps). Then we stop. Because if we keep dividing 0 by 2, it's 0, but each step adds a step. So adding those steps would not be helpful, as 0 can be achieved in 2 steps. Any further steps would be more steps than necessary, so including them in the list for 0 would be adding higher steps, which are worse options. So, to avoid those, once we reach 0, we add it once (with the current step count) and break.

Wait, but for example, if the element is 0 initially (though according to the input constraints, a_i is at least 1?), the initial input has a_i >=1. Oh, right, the problem statement says that the input array elements are between 1 and 2e5. So the initial elements are all >=1. So in processing each element, we can generate all possible values until 0, but once it's 0, we add it once and break.

So for each element a_i:

current = a_i
steps = 0
while True:
   add (current, steps) to the map
   if current ==0:
       break
   current = current //2
   steps +=1

So this loop will process all possible values the element can take. For example, if a_i is 5:

5 (0 steps) → 2 (1) → 1 (2) → 0 (3 steps). Then stop.

So for each element, the loop runs log2(a_i) +1 times. For a_i up to 2e5, that's about 18 steps per element.

So total steps are O(n log a_i), which for n=2e5 is acceptable.

Once all these steps are stored in the map, for each key (possible target value) in the map, we check if the list of steps has at least k elements. If so, we sort that list, take the first k elements (smallest steps), sum them, and keep track of the minimum sum across all such keys.

The key part here is that for each possible target value, we need to collect all the steps that elements take to reach it, then sum the k smallest steps. The minimal sum across all possible target values is our answer.

Yes. That makes sense.

So the steps are:

1. Preprocess each element to generate all possible (value, steps) pairs.

2. For each possible value, collect all steps in a list.

3. For each value's list that has length >=k, compute the sum of the first k entries (sorted) and track the minimum.

So the time complexity is:

- O(n log a) for preprocessing.

- Then, for each possible value, sorting the list of steps. The number of possible values is O(n log a), but each steps list is of length O(n) in the worst case (if all elements generate the same value). But for each such list, sorting would take O(m log m) time, where m is the size of the list.

But considering that for n=2e5 and each element contributing up to 18 steps, the total number of entries in the map is O(n log a), which is about 3.6e6. Then, for each entry in the map, if the list has m elements, sorting m elements takes O(m log m) time. But for the worst case, if a value is generated by all elements (like 0), then m is 2e5. So sorting that would take O(m log m) = 2e5 * 18 ≈ 3.6e6 operations, which is acceptable. But for all other values, m is smaller.

So the total time for sorting is O(total entries log m), but perhaps it's manageable. The worst case would be if all elements have the same path towards 0, but that's unlikely. But even then, the total steps would be O(n log a) + O(n log n), which for 2e5 is acceptable.

But wait, the sum for each value's list is the sum of the first k elements. So for each list of steps, we can keep track of the steps as we add them, perhaps in a sorted manner. But since we add steps from each element in arbitrary order, it's easier to collect all steps for a value and then sort them when needed.

So the plan is:

- Use a dictionary to collect for each possible value the list of steps required to reach it.

- Once all elements are processed, iterate through each key in the dictionary.

- For each key, if the list's length is >=k, sort the list, sum the first k elements, and update the minimum.

So in Python, the code would look like:

Testing against sample input 1.

```python
from collections import defaultdict
import sys


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))

    counts = defaultdict(list)

    for num in a:
        current = num
        steps = 0
        while True:
            counts[current].append(steps)
            if current == 0:
                break
            current = current // 2
            steps += 1

    min_ops = float('inf')

    for key in counts:
        lst = counts[key]
        if len(lst) >= k:
            lst.sort()
            sum_ops = sum(lst[:k])
            if sum_ops < min_ops:
                min_ops = sum_ops

    print(min_ops, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
1 2 3 4 5
""",
            "output": \
"""\
2
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
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))
    
    counts = defaultdict(list)
    
    for num in a:
        current = num
        steps = 0
        while True:
            counts[current].append(steps)
            if current == 0:
                break
            current //= 2
            steps += 1
    
    min_ops = float('inf')
    
    for key in counts:
        lst = counts[key]
        if len(lst) >= k:
            lst.sort()
            current_sum = sum(lst[:k])
            if current_sum < min_ops:
                min_ops = current_sum
    
    print(min_ops, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
1 2 3 3 3
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

Edge case 3: k=3, elements 8, 8, 8. So steps for 8 is 0, so sum is 0.

Another case where elements can reach a value in varying steps.

But the code handles all these.

Now, about the time constraints. Let's calculate for n=2e5, each element generating 18 steps. So counts will have 3.6e6 entries in total. Then, for each entry, if the list's length is >=k, we sort it. The worst case is a key with 2e5 elements. Sorting that list takes O(2e5 log 2e5) steps, which is about 2e5 * 18 = 3.6e6 operations, which is acceptable. Then, for all keys, this would sum up to O(3.6e6 log m) steps. But since each list is sorted once, and the average list size is perhaps small (like log n), the total time is manageable.

In Python, the sort function is optimized, so even with 2e5 elements, it's acceptable.

Now, in Python, lists can handle 2e5 elements without issue. Memory-wise, each list stores integers. For 3.6e6 elements in total, each list's entries are integers. So 3.6e6 integers is about 28MB (since each int is 28 bytes in Python), but considering that for 2e5 elements, each with 18 steps, it's 3.6e6 entries. 3.6e6 * 28 bytes is about 100MB, which is within the memory limits (256MB). So the code is memory efficient.

Another possible optimization is that, when building the counts, for each number, we can collect the steps in reverse order, but that's not necessary.

In conclusion, the code is correct and efficient.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    counts = defaultdict(list)
    
    for num in a:
        current = num
        steps = 0
        while True:
            counts[current].append(steps)
            if current == 0:
                break
            current //= 2
            steps += 1
    
    min_ops = float('inf')
    
    for key in counts:
        lst = counts[key]
        if len(lst) >= k:
            lst.sort()
            current_sum = sum(lst[:k])
            if current_sum < min_ops:
                min_ops = current_sum
    
    print(min_ops)

if __name__ == "__main__":
    main()
```
