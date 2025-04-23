<think>
Okay, let's see. The problem is to find the number of distinct OR values for all possible subarrays of a given array. Hmm. So for every possible subarray [l, r], compute the OR of all elements from l to r, and count how many unique values there are. The array can be up to 1e5 elements, so a brute-force approach of checking all possible subarrays is definitely out of the question—that would be O(n^2) time, which is way too slow for n=1e5.

So I need a smarter way to compute this. Let's think about how the OR operation works. Once you have a certain value, OR-ing another number can only keep the same bits or set more bits. So the OR of a subarray is a non-decreasing function as the subarray grows. But wait, when considering different starting points, how can we track the possible OR values efficiently?

An approach that I remember from similar problems is to track, for each position, the set of possible OR values that end at that position. Let's think: for each element in the array, the ORs of subarrays ending at that element can be derived from the previous elements' ORs. For example, when processing the i-th element, the possible ORs are the OR of a[i] with each of the ORs that ended at i-1, plus a[i] itself. Then, we can keep a set of all OR values encountered.

Let me elaborate. Suppose I have a list of OR values for subarrays ending at position i-1. For position i, each of those OR values can be combined with a[i] by OR-ing them, and then also a[i] itself. However, some of these combinations might result in the same value. For instance, if the previous ORs already include a value that, when OR'd with a[i], gives the same as a[i], then adding it again would be redundant. So, for each position i, we can maintain a set of current ORs, which is the union of a[i] and the OR of a[i] with each element from the previous set. Then, we add all elements of this current set to a global set that keeps track of all possible OR values.

This way, for each element in the array, we process O(k) elements, where k is the number of unique OR values generated so far. But what's the maximum possible k here? Since each OR operation can add bits but not remove them, the number of possible OR values for a position is limited by the number of bits in the maximum possible value. Since the maximum a[i] is 1e6, which is about 20 bits. So for each position, the number of possible ORs is at most 20. Because each step can add some bits, but once all bits are set, adding more elements doesn't change the OR.

Wait, for example, if a[i] is 0, then the current ORs would just be 0. But if the previous ORs include multiple values, OR-ing with 0 would leave them unchanged. So for that case, the current OR set would be the same as the previous set plus 0 (but if 0 is already present, it's not added). Hmm. So in general, for each i, the current set can be built by taking the previous set, OR each element with a[i], then add a[i] itself. Then, eliminate duplicates.

But how to efficiently track this? Let's see. For each i, the current set can be built as follows:

current = set()
current.add(a[i])
prev = previous set
for x in prev:
    current.add(x | a[i])

Then, merge these into the current set, and add all elements of current to the global set.

The key point here is that the size of current is bounded. Because each time you OR with a[i], the values can only have bits set that were in a[i] or in the previous values. For a 20-bit number, the maximum possible unique ORs per step is O(20). Because each new OR can add at least one bit, but once all bits are set, it's fixed.

So for each of the n elements, we process up to 20 elements (the size of the previous set). Thus, the total time complexity is O(n * 20) = O(n), which is acceptable for n=1e5.

Yes, this seems manageable. So the plan is:

- Initialize a global set to track all OR values.
- For each element in the array:
   - Create a new temporary set for the current position.
   - Add the current element a[i] to the temporary set.
   - Take the previous set (from the previous element) and OR each of its elements with a[i], adding the results to the temporary set.
   - Replace the previous set with the temporary set for the next iteration.
   - Add all elements of the temporary set to the global set.
- After processing all elements, the size of the global set is the answer.

Let's test this logic against the sample input.

Sample 1:
Input: 3 elements [1, 2, 0]

Processing first element (1):
Current set is {1}.
Add 1 to global. Global now {1}.

Second element (2):
Take previous set {1}, OR with 2: 1|2=3. So current set is {2, 3}.
Add 2 and 3 to global. Now global {1,2,3}.

Third element (0):
Previous set is {2,3}.
OR each with 0: 2|0=2, 3|0=3. So new current set is {0,2,3} (since adding 0, then OR results). Wait, no. Wait, the new current set is built by adding a[i] (0) and OR-ing each element of the previous set (which was {2,3}) with 0. So:

Add 0 to current set.
Then, for each x in previous set (2 and 3), compute x |0, which is x. So add 2 and 3 to current set. But current set now is {0,2,3}. However, when you add those, but since 2 and 3 are already present, the current set for the third element is {0,2,3}.

Then, add 0,2,3 to the global set. The global was {1,2,3}, adding 0 gives {0,1,2,3}. So the total is 4, which matches the sample.

Yes, that works.

Another sample: the second input gives 11. Let's see.

But maybe we can skip that for now.

So the steps in code would be:

Initialize a set called prev_set and a global_set.

Initially, prev_set is empty. For each element in a:

current_set = set()
current_element = a[i]
current_set.add(current_element)
for x in prev_set:
    current_set.add(x | current_element)
global_set.update(current_set)
prev_set = current_set

At the end, the size of global_set is the answer.

This approach should work, and the time is O(n * k), where k is the average size of prev_set. Since k is at most 20, this is acceptable.

Now, considering the data structures. In Python, using a set for prev_set and current_set is feasible. But since each step requires iterating through the previous set and adding new elements, it's important to make this as efficient as possible.

But for n=1e5 and each step with 20 elements, it's manageable.

So the code would be something like:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    global_set = set()
    prev_set = set()

    for num in a:
        current_set = set()
        current_set.add(num)
        for x in prev_set:
            current_set.add(x | num)
        prev_set = current_set
        global_set.update(prev_set)

    print(len(global_set), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
1 2 3 4 5 6 1 2 9 10
""",
            "output": \
"""\
11
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

Another test case:

Suppose a = [0,0,0]. All possible ORs are 0. So the answer is 1.

The code would process each 0. For the first, current_set is {0}, added to global. Then next 0: current_set starts with 0, then OR with previous elements (0 → 0). So current_set is {0}. Then same for the third. The global has size 1.

Another test case: a = [1, 3]. Let's see.

First iteration: current_set {1}, added to global. Global: {1}.

Second iteration: current_set starts with 3. Then OR previous (1) with 3 → 3. So current_set is {3, 3}? Wait, no. Wait, initial current_set is {3}. Then for each x in prev_set (which is {1}), add x | 3 = 3. So current_set after adding is {3} (since 3 is already present). So prev_set becomes {3}, and global becomes {1,3}.

The possible ORs for subarrays:

[1] →1

[1,3] → 3

[3] →3.

So total 2, which is correct. The code returns 2.

Yes, that's correct.

So the code seems to handle these cases.

Now, the code as written uses Python's set operations, which should be efficient enough. But for n=1e5, and each step handling up to 20 elements, this is O(2e6) operations, which is acceptable.

But in Python, creating new sets for each iteration may have some overhead. Let's see. For each element, we create a new current_set as a set. Then, for each x in the previous set, we compute x | num and add to current_set. Then, assign prev_set to current_set.

An alternative to using a set for current_set is to use a list, but since OR operations can produce duplicates, using a set is better to avoid redundant entries. For example, if the previous set has elements that when OR'ed with the current number give the same result, then a set will automatically deduplicate them.

But in Python, adding elements to a set is O(1) on average, so it's manageable.

But perhaps even better to use a list and then convert to a set, but I think the current approach is already efficient enough.

Another optimization: since the OR operation is associative and commutative, but the order doesn't matter here. So perhaps for each current_set, we can process the elements in any order.

But the code as written should work.

Therefore, the code should be as follows.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

result = set()
prev = set()

for num in a:
    current = {num}
    for x in prev:
        current.add(x | num)
    prev = current
    result.update(prev)

print(len(result))
```
