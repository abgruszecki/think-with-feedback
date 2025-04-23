<think>
Okay, let's tackle this problem. Hmm, the problem is about finding the number of temperatures in a given range [a, b] that are covered by at least k recipes. The constraints are tight: n and q can be up to 2e5. So we need an efficient solution.

First, I need to figure out for each temperature how many recipes include it. Once we have that, any query [a,b] can be answered by checking how many temperatures in that interval have a count >=k. But doing this naively for each query would be O(2e5) per query, which is way too slow for 2e5 queries. So we need a way to preprocess this data into a structure that allows O(1) or O(log n) per query.

So the steps are:

1. For all temperatures (from 1 to 2e5), compute the number of recipes that cover them.
2. Then, create a prefix sum array where each index i contains the count of temperatures from 1 to i that are admissible (i.e., their count >=k).
3. For a query [a, b], the answer is the prefix sum up to b minus the prefix sum up to a-1.

Yes, that makes sense. Because then each query can be answered in O(1) time.

Now, how to compute the count per temperature efficiently. Since each recipe is a range [li, ri], we can model this as a line sweep. The standard approach here is to use a difference array. For each recipe, we increment the start li and decrement ri+1. Then, after processing all recipes, we compute the prefix sum to get the count for each temperature.

Let me think. For example, if a recipe is from l to r, then in the difference array, we do +1 at l and -1 at r+1. Then, the prefix sum up to a position gives the number of active intervals covering that position.

Yes. So, steps:

- Initialize a difference array of size 2e5 + 2 (since the maximum temperature is 2e5, r+1 can be up to 2e5+1).
- For each recipe, add +1 to diff[l], subtract 1 from diff[r+1].
- Compute the prefix sum to get the count for each temperature. Let's call this 'counts' array.
- Then, create a 'valid' array where valid[i] is 1 if counts[i] >=k, else 0.
- Compute a prefix sum array of 'valid' to answer queries quickly.

But wait, the maximum temperature is 2e5, so all arrays can be size 2e5+2 or similar. Let's make sure the indices are handled correctly.

So:

1. Initialize a difference array (diff) of size 200002 (since max ri is 2e5, r+1 is 2e5+1, but in 0-based or 1-based? Let's use 1-based for temperatures. So temperatures are from 1 to 200000. So the diff array needs to cover up to 200001, because when a recipe ends at 200000, r+1 is 200001.

So the steps:

- Initialize diff array of size 200002 (indexes 0 to 200001, but probably starting from 1 for simplicity).

For each recipe l, r:

- diff[l] +=1
- diff[r+1] -=1

Then compute the prefix sum to get counts[i] (number of recipes covering temperature i), for i from 1 to 200000.

Once we have counts[i], create an array valid where valid[i] is 1 if counts[i] >=k, else 0.

Then compute the prefix sum of valid, let's call it prefix, where prefix[i] is the sum of valid[1..i]. So for a query a to b, the answer is prefix[b] - prefix[a-1].

Yes, this approach will work. And since all steps are O(n) or O(1) per query, it's feasible for the constraints.

Now, the implementation details.

In Python, creating an array of size 2e5+2 is manageable. Let's see: 2e5 elements are about 200,000, which is acceptable.

So code outline:

Read n, k, q.

Initialize diff array of size 200002 (all zeros).

Then read each of the n recipes, for each l, r:

diff[l] +=1

diff[r+1] -=1

Then compute the prefix sum for counts:

counts = [0] * (200001)

current = 0

for i in range(1, 200001):

current += diff[i]

counts[i] = current

Wait, but the prefix sum over the diff array gives the counts. So the counts array will hold the number of recipes covering each temperature.

Then, create valid array:

valid = [0] * (200001)

for i in range(1, 200001):

valid[i] = 1 if counts[i] >=k else 0

Then compute prefix sums:

prefix = [0] * (200001)

current_sum =0

for i in range(1, 200001):

current_sum += valid[i]

prefix[i] = current_sum

Then, for each query a, b:

if a > b: output 0 (but the problem states a <= b)

else:

result = prefix[b] - prefix[a-1]

print(result)

But wait, what if a is 1? Then prefix[a-1] is prefix[0], which is 0. So it's okay.

Testing the example.

First example input:

3 2 4

Recipes:

91 94

92 97

97 99

So:

For the first recipe, l=91, r=94.

diff[91] +=1, diff[95] -=1.

Second recipe, l=92, r=97: diff[92] +=1, diff[98] -=1.

Third recipe, l=97, r=99: diff[97] +=1, diff[100] -=1.

After processing all recipes, compute counts.

Then, counts for each temperature:

For example, 92: covered by first and second recipe. So count is 2, which is >=k (2), so valid.

Then, the valid array marks 1 for all such temperatures.

The prefix array sums these up.

In the first query, a=92, b=94. The valid temperatures here are 92,93,94. So 3.

In the second query, 93-97: 93,94 are covered by first and second recipe (count 2 each), 95-96: covered only by second (count 1), 97: covered by second and third (count 2). So valid temps are 93,94,97. Sum is 3.

Third query 95-96: 0.

Fourth query 90-100: 92,93,94,97. So 4.

Which matches the sample.

So this approach works.

Now, for Python, the steps are:

Initialize a list of 200002 zeros. Then process each recipe. Then compute counts, then valid, then prefix.

In Python, lists are 0-based. So when we process a recipe with l and r, we do:

diff[l] +=1

if r+1 <=200000:

diff[r+1] -=1

But since r can be 200000, r+1 is 200001, which is within the diff array (size 200002? Or maybe size 200001+1? Let's think. The maximum possible r+1 is 200000+1=200001. So the diff array needs to be of size 200001+1=200002 (since indices go from 0 to 200001). Because for a recipe with r=200000, r+1 is 200001, so diff[200001] is adjusted. Then, when computing the counts, for i from 1 to 200000, adding the diff[i] to current.

Yes.

Now, code:

Read n, k, q.

Then read n lines of l and r. For each, update diff[l] +=1, diff[r+1] -=1.

Then compute the counts array.

Then compute the valid array.

Then compute prefix.

Then process q queries, each a and b, output prefix[b] - (prefix[a-1] if a >1 else 0).

But in code, the prefix array can be built such that prefix[0] =0, prefix[1] is valid[1], prefix[2] = valid[1]+valid[2], etc.

So, code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, k, q = map(int, input_stream.readline().split())
    max_temp = 200000
    diff = [0] * (max_temp + 2)  # 1-based to 200001
    
    for _ in range(n):
        l, r = map(int, input_stream.readline().split())
        diff[l] += 1
        if r + 1 <= max_temp:
            diff[r + 1] -= 1
        else:
            # r is 200000, so r+1 is 200001, which is within diff's size (index up to 200001)
            diff[r + 1] -= 1
    
    # Compute counts for each temperature
    counts = [0] * (max_temp + 1)  # 1-based to 200000
    current = 0
    for i in range(1, max_temp + 1):
        current += diff[i]
        counts[i] = current
    
    # Compute prefix sums of admissible temperatures
    prefix = [0] * (max_temp + 1)
    current_sum = 0
    for i in range(1, max_temp + 1):
        if counts[i] >= k:
            current_sum += 1
        prefix[i] = current_sum
    
    # Process queries
    for _ in range(q):
        a, b = map(int, input_stream.readline().split())
        res = prefix[b] - (prefix[a - 1] if a > 1 else 0)
        print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 1 1
1 1
200000 200000
90 100
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

So the code is correct.

Now, in terms of Python's performance. For 2e5 recipes, the code loops 2e5 times for each recipe, which is manageable. Then, the counts loop is 2e5 iterations, same for prefix.

In Python, each iteration is O(1), so the code should pass within the time constraints. The time limit is 2.5 seconds. For 2e5*3 iterations (diff processing, counts, prefix), each is O(1), and 2e5 * 3 is 6e5 operations, which is acceptable.

So the code is correct and efficient.
</think>

```python
import sys

def main():
    n, k, q = map(int, sys.stdin.readline().split())
    max_temp = 200000
    diff = [0] * (max_temp + 2)  # 1-based to 200001
    
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        diff[l] += 1
        if r + 1 <= max_temp:
            diff[r + 1] -= 1
        else:
            # r is 200000, so r+1 is 200001, which is within diff's size (index up to 200001)
            diff[r + 1] -= 1
    
    # Compute counts for each temperature
    counts = [0] * (max_temp + 1)  # 1-based to 200000
    current = 0
    for i in range(1, max_temp + 1):
        current += diff[i]
        counts[i] = current
    
    # Compute prefix sums of admissible temperatures
    prefix = [0] * (max_temp + 1)
    current_sum = 0
    for i in range(1, max_temp + 1):
        if counts[i] >= k:
            current_sum += 1
        prefix[i] = current_sum
    
    # Process queries
    for _ in range(q):
        a, b = map(int, sys.stdin.readline().split())
        res = prefix[b] - (prefix[a - 1] if a > 1 else 0)
        print(res)

if __name__ == "__main__":
    main()
```
