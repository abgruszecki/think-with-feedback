<think>
Okay, I need to solve this programming problem. Let's read the problem statement carefully.

The problem is about Vlad's visits to cafes. We have a list of the order in which he visited the cafes. We need to find the cafe whose last visit occurred before the last visits of all other cafes. So the goal is to find the cafe with the earliest possible last visit. But wait, no, wait: the problem says "the cafe that he hasn't been there for as long as possible." Oh right, so that's the same as the cafe whose last visit was the earliest possible. Because the longer he hasn't visited, the earlier the last visit was compared to others.

So, for each cafe, we need to track the index (position) of its last occurrence in the list. Then, among all the cafes, we need to find the one with the smallest last occurrence index. Wait, no: the cafe with the earliest last occurrence. Because if a cafe's last occurrence is at position 3, and another's is at 5, then the first hasn't been visited after position 3, so between the two, the first is the one that hasn't been visited for longer.

Wait, the problem says "he hasn't been there for as long as possible." So the time since his last visit is the current time (after all visits) minus the time of the last visit. So for each cafe, the time since last visit is (n - last_occurrence_pos). Because if the last visit was at position k (0-based?), then the number of steps since then is n-1 - k +1? Wait, let me think about the positions.

Wait, the input is a1 to an, which are the cafes visited in order. So the first visit is a1, then a2, up to an. The last occurrence of each cafe is the last position where it appears. For example, in the first sample input:

5
1 3 2 1 2

The last occurrence of 1 is position 3 (0-based index 3, which is 4th element), of 3 is position 1 (second element), of 2 is position 4 (fifth element). The last occurrence times (positions) are: 3 →1, 1→3, 2→4. The earliest last occurrence is 3's, which is position 1. So the answer is 3.

So the problem reduces to:

For each unique cafe in the list, find the last position where it appears. Then among all these positions, find the cafe with the smallest position. That cafe's last visit was earliest, so it's the answer.

Wait, no. Wait, the earliest last occurrence would be the one with the earliest position. So the cafe whose last occurrence is at the earliest position in the list. So for example, if a cafe's last occurrence is at position 5, and another's at position 3, then the second has a last occurrence earlier, so it's the answer.

So the steps are:

1. Iterate through the list of cafes and record the last occurrence index of each unique cafe.

2. Find the cafe with the minimum last occurrence index.

3. If there are multiple cafes with the same minimum last occurrence index, which one to choose? The problem statement says "print one integer"—so perhaps there's only one possible answer. But according to the sample inputs, there's a unique answer.

Wait, but in a case where two cafes have the same last occurrence index, which one is the answer? For example, if two cafes have their last occurrence at the same earliest position. Then, according to the problem statement, we need to pick either. But how does that happen? Because for example, in the list [1,2], both have last occurrence at positions 0 and 1. If the list is [1,1,2,2], then the last occurrences are 1 (for 1) and 3 (for 2). But if another example is [3,3,3], then the last occurrence is 2 for 3. So in that case, the answer is 3.

But the problem requires that we find the one with the earliest last occurrence. So the minimum of all the last occurrence indices. If there are multiple, then perhaps the cafe with the smallest index (numerically) is chosen? Or is there guaranteed to be a unique one?

Wait, the problem statement says: "help Vlad to find that cafe". So in cases where multiple cafes have the same earliest last occurrence, the problem must have a unique answer. But how?

Wait, let's think: suppose the list is [1,2]. The last occurrences are 0 for 1, 1 for 2. The earliest last occurrence is 0 (for 1), so answer is 1.

If the list is [2,1], the last occurrences are 0 and 1. So answer is 2.

Another example: list is [1,2,1,2]. The last occurrence of 1 is 2, of 2 is 3. The earliest last occurrence is 2 (for 1). So answer is 1.

Another case: list is [3,4,3,4]. Then last occurrences are 2 (3) and 3 (4). Answer is 3.

But what if the list is [5,5,5]. The last occurrence is 2. Only one cafe, so answer is 5.

So the algorithm is:

- For each cafe, find the last occurrence's index (0-based or 1-based?) Let's check the sample input.

First sample:

Input is 1 3 2 1 2. The positions are 0,1,2,3,4 (0-based). The last occurrence of 1 is 3, 3 is 1, 2 is 4. The minimum is 1, so the cafe is 3. Which matches the sample.

So in this case, the code should track the last occurrence index as 1 (0-based) for cafe 3. So the algorithm uses 0-based indices.

So the steps are:

1. Iterate through the list, and for each element, store the last index where it was found.

2. Among all the stored last indices, find the minimum value.

3. The corresponding cafe(s) with that minimum last index are the answers.

But what if multiple cafes have the same minimal last index? Then which one to output?

The problem statement's note in the second example:

Input is 6

2 1 2 2 4 1

The sequence is 2,1,2,2,4,1.

The last occurrences:

2: index 3 (value 2 in the list is at positions 0,2,3. Last is 3)

Wait no: positions are 0-based. The input is [2,1,2,2,4,1]. Let's list the indexes:

0:2

1:1

2:2

3:2

4:4

5:1

So last occurrence of 2 is index 3 (value 2). Last occurrence of 1 is index 5. Last of 4 is 4. So the last indices are:

2 →3

1 →5

4 →4

So the minimal last index is 3 (for 2) and 4 (for 4). Wait, no. 3 is the minimal here. So the answer is 2. Which matches the sample.

Wait, but according to the sample input, the output is 2. So in that case, the last occurrence of 2 is at index 3, which is the earliest among all the last occurrences.

So the algorithm is: for each cafe, track the last occurrence index, then among all those, find the one with the smallest last index, and output that cafe.

So the steps are:

- Iterate through the list once, and for each cafe, record the last index it was found.

- Then, among all the cafes, find the one with the smallest last index.

- If there are multiple cafes with the same smallest last index, which one to choose? The problem statement's second example indicates that in the case where there are multiple such cafes, the one with the earliest occurrence in the list? Or perhaps the first encountered in the list when processing? Or perhaps the smallest cafe index?

Wait, in the problem statement's second example, the answer is 2. Let's see: the last occurrence of 2 is index 3, of 4 is index 4, of 1 is index 5. So the minimal is 3. The cafe with that is 2. So it's unique. So the algorithm can safely assume that there is exactly one cafe with the minimal last occurrence index. But is that the case?

Let me think of a case where two cafes have the same last occurrence index. For example:

Input:

3

1 2 3

Then the last occurrences are 0 (1), 1 (2), 2 (3). The minimal is 0. So the answer is 1.

Another example:

Input: 4

1 2 2 1

Then last occurrences: 3 (1), 2 (2). The minimal is 2 (for 2). Answer is 2.

Another example where two cafes have same last occurrence index:

Input: 5

3 4 3 4 5

The last occurrences are 2 (3), 3 (4), 4 (5). The minimal is 2 (3). Answer is 3.

Another example where two cafes have same last occurrence:

Input: 2

5 5

Only one cafe, so answer is 5.

But suppose we have:

Input: 4

1 0 1 0

So the last occurrence of 1 is index 2, 0 is index 3. The minimal is 2 (1). Answer is 1.

Wait, but what if the input is:

3

1 0 1

Then the last occurrence of 1 is index 2, 0 is index 1. So answer is 0.

Another example where two cafes have same last occurrence:

Wait, can that happen?

Input: 4

0 1 0 1

Last occurrence of 0 is 2, 1 is 3. So the minimal is 2 (0). Answer is 0.

But what if the list is:

0,1,2,0,1,2

Then last occurrences are 3 (0), 4 (1), 5 (2). So minimal is 3 (0). Answer is 0.

But what if we have:

Input: 5

3 4 3 4 5

Then last occurrences are 3 (3 and 4). Wait, 3's last occurrence is index 2 (third element?), wait:

Wait, the list is [3,4,3,4,5]. The indexes are 0-based.

Indices:

0:3

1:4

2:3

3:4

4:5

So the last occurrence of 3 is index 2, 4 is index 3, 5 is index 4.

So minimal is 2 (3). Answer is 3.

But how about:

Input: 6

1 2 1 2 1 2

Then last occurrences are 4 (1), 5 (2). So minimal is 4 (1). Answer is 1.

So in all cases, the answer is unique because two different cafes can't have their last occurrence at the same index. Because each occurrence in the list is of a single cafe. So in the list, each position is assigned to exactly one cafe. So the last occurrence of a cafe is a unique index. So two different cafes cannot have their last occurrence at the same index. Because the index can only belong to one of them. For example, if two cafes have their last occurrence at the same index, that would mean that at that index, both are present. Which is impossible. So each index has exactly one cafe. Therefore, each last occurrence index is unique to a cafe. Therefore, there's exactly one cafe with the minimal last occurrence index.

Wait, but that's not necessarily the case. Wait, for example, suppose the list is [a, b, c]. Each cafe's last occurrence is at different indexes. But if the list is [a, b, a], then the last occurrence of a is index 2, of b is index 1. So again, unique.

But what about a list like [a, a, a]. Then the last occurrence of a is index 2. So only one cafe.

So it's impossible for two different cafes to have their last occurrence at the same index. Because each index is associated with exactly one cafe. So the last occurrence of a cafe is the last index where that cafe appears. So two different cafes can't have their last occurrence at the same index. Because if that were the case, then that index would have to be the last occurrence for both, which is impossible because the index can only hold one cafe. So each last occurrence index is unique to a single cafe. Therefore, when processing all the last occurrences, there will be exactly one cafe with the minimal last index.

Therefore, the problem is always solvable with a unique answer.

So the algorithm is:

1. Iterate through the list once, keeping track of the last occurrence index of each cafe.

2. Find the cafe with the minimal last occurrence index.

3. Output that cafe's index.

Now, the steps to code this.

In Python, for n up to 2e5, we can process this efficiently.

So the steps in code:

Read n.

Read the list of a's.

Create a dictionary to store the last occurrence index for each cafe.

Loop through the list in order. For each i in 0..n-1:

   update the dictionary entry for a[i] to be i.

Then, for all keys in the dictionary, find the one with the smallest value (last index).

Output that key.

Yes.

So for example, in the first sample:

a = [1,3,2,1,2]

Processing each index:

0:1 → last_occurrence[1] =0

1:3 → last_occurrence[3]=1

2:2 → last_occurrence[2] =2

3:1 → update to 3

4:2 → update to4.

Then, the last_occurrence dict is {1:3, 3:1, 2:4}.

The values are 3,1,4. The minimal is 1, so the key is 3. Output 3.

In the second sample:

a = [2,1,2,2,4,1]

Processing:

0:2 → 0

1:1 →1

2:2 →2

3:2 →3

4:4 →4

5:1 →5

The dict is {2:3, 1:5,4:4}. The minimal is 3 → key 2. Output 2.

So the code works.

Now, in Python, how to implement this efficiently.

For n up to 2e5, this is O(n) time, which is acceptable.

The code can read the input as follows:

Read n.

Then read the next line as a list of integers.

Then create a dictionary.

Loop through each element in the list, keeping track of the index.

For each index i, and element a, we update the dict entry for a to i.

Once the dict is built, find the key with the smallest value.

Then output that key.

In Python, the code can be written as:

n = int(input())

a = list(map(int, input().split()))

last = {}

for idx, num in enumerate(a):

    last[num] = idx

# Now find the key with minimal value in last.

# To find the key with the minimum value, we can loop through the items.

min_index = n  # initializing to a value larger than possible (since indices are 0-based, max is n-1)

result = -1

for cafe, idx in last.items():

    if idx < min_index:

        min_index = idx

        result = cafe

print(result)

Wait, but what if the list is empty? But according to the constraints, n is at least 1, so the list has at least one element, and the dict is non-empty. So the code is safe.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    last_occurrence = {}
    for idx, cafe in enumerate(a):
        last_occurrence[cafe] = idx
    min_index = n
    result = -1
    for cafe, idx in last_occurrence.items():
        if idx < min_index:
            min_index = idx
            result = cafe
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
2 1 2 2 4 1
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

Sample 2:

6

2 1 2 2 4 1

The dict entries are 2:3, 1:5,4:4. The min index is 3, so result is 2. Correct.

Another test case: input 3, 1 2 3 → last indexes are 0,1,2. The minimal is 0 → output 1.

Another test case: input 4, 1 0 1 0 → last indexes 1:2, 0:3. minimal is 2 → output 1.

Yes.

So this code should work.

Now, what about space constraints? The dict can have up to O(n) entries if all elements are unique, but in practice, for 2e5 elements, Python can handle that. So the memory is acceptable.

Time-wise, it's O(n) time, which is acceptable for n=2e5.

Thus, this code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
last_occurrence = {}
for idx, cafe in enumerate(a):
    last_occurrence[cafe] = idx
min_index = n
result = -1
for cafe, idx in last_occurrence.items():
    if idx < min_index:
        min_index = idx
        result = cafe
print(result)
```
