<think>
Okay, let's see. The problem is to find the number of unordered pairs of two different monitors where, after possibly rotating each (so choosing either width as height or vice versa), they have the same height. 

Hmm. So for each pair of monitors, we need to check if there's a way to rotate each such that their heights are equal. How to approach this efficiently?

Let's think about each monitor. For a given monitor, there are two possible heights after rotation: h1 = max(w_i, h_i) and h2 = min(w_i, h_i)? Wait, wait. Wait, no. Because when you rotate, the height can be either the original width or the original height, depending on how you rotate. For example, if a monitor is 3x2, then rotating it would make it 2x3. So the height can be either 2 or 3, depending on the rotation. So for each monitor, the possible heights are h_i and w_i. But since we can choose either orientation, the height of the monitor after rotation is either the original height or the original width, whichever we choose. So for each monitor, the possible heights are two possibilities. But wait, if the original width and height are the same (like 5x5), then rotating doesn't change anything, so the possible height is just one value.

So for each pair of monitors (i, j), there are two possibilities for i's height and two possibilities for j's height. We need to check if any combination of these possibilities results in their heights being equal. If yes, then the pair is counted.

So the problem reduces to checking, for each pair, if the set {h_i, w_i} and {h_j, w_j} have any intersection. Because if there's at least one common value between the two sets, then we can rotate each monitor such that their heights are that common value. 

Wait, yes! Because for monitor i, if one of h_i or w_i is in the intersection, then rotate it to have that as the height. Similarly for monitor j. Then their heights are equal. So the condition for a pair (i,j) to be valid is that the intersection of {h_i, w_i} and {h_j, w_j} is non-empty.

So the problem simplifies to counting the number of pairs where the two monitors share at least one common dimension (either h_i or w_i) as either of their dimensions. 

So the key is to find for each monitor, the set {h_i, w_i}, and then for each possible value in that set, track how many monitors have that value in their set. Then, for each monitor, the number of other monitors that share at least one of their values is the count, but we have to subtract duplicates (since a monitor could share two values with another, but it's still counted once per pair).

Wait, but how to compute this efficiently?

Alternative approach: For each monitor, compute all possible values (h_i, w_i) and add their sorted pair (so that h and w are sorted, but since the order doesn't matter, perhaps just using a set). Then, for each possible value in the union of all possible dimensions, count how many monitors include that value in their set. Then, the total number of pairs is the sum over all values v of (count[v] choose 2), but this would overcount pairs that share more than one value.

Because if two monitors have two common values, like {2,3} and {2,3}, they would be counted in both the count for 2 and the count for 3. So adding all the combinations would count the pair (i,j) once for each common value. So the total would be the sum over v of C(c_v, 2), but since some pairs are counted multiple times in this sum, the actual answer is the sum minus the overcount. But this seems tricky.

For example, consider two monitors with {2,3} and {2,3}. They share both 2 and 3. So in the sum, they would be included in the count for 2 (contributing 1) and for 3 (contributing 1). So the sum would add 2 for this pair, but the correct contribution is 1. So the total sum would overcount such pairs.

So this approach would require inclusion-exclusion, which complicates things. Therefore, perhaps the straightforward approach of checking all pairs is feasible given the constraints.

Wait, the constraints say n is up to 1e3. So the total number of pairs is 1e3 * 1e3 / 2 ≈ 5e5. That's manageable. So for each pair of monitors, we can check if their sets have any intersection. If yes, add 1 to the answer.

But how to check that for each pair? For each monitor, store the set of {h, w}. For each pair, compute the intersection of their two sets, and see if it's non-empty.

But for two monitors, say their sets are s1 and s2. The intersection is non-empty if either h1 is in s2, or w1 is in s2. But since s2 is {h2, w2}, that's equivalent to checking if either h1 == h2, or h1 == w2, or w1 == h2, or w1 == w2. Wait no. Because s1 is {h_i, w_i}, and s2 is {h_j, w_j}. The intersection is non-empty if any of h_i, w_i is in s2. So for each pair (i,j), the condition is whether (h_i is h_j or h_i is w_j) OR (w_i is h_j or w_i is w_j).

Wait, but h_i could be equal to w_i. For example, if monitor i is square (h_i = w_i), then s_i has only one element. So in that case, the condition is whether that element is present in s_j.

But for the general case, for each pair i and j, the condition is:

if (h_i == h_j) or (h_i == w_j) or (w_i == h_j) or (w_i == w_j). 

Because for monitor i, possible heights are h_i or w_i. For monitor j, possible heights are h_j or w_j. So the possible pairs of chosen heights are (h_i, h_j), (h_i, w_j), (w_i, h_j), (w_i, w_j). We need any of these pairs to be equal. 

So, the condition is if any of these four possibilities is true.

Therefore, for each pair of monitors i and j (i < j), check if h_i == h_j, h_i == w_j, w_i == h_j, or w_i == w_j. If any of those is true, then the pair is counted.

So the straightforward approach is O(n^2), which for n=1e3 is 1e6 operations, which is acceptable. Even for 1e3 * 1e3 = 1e6, which is manageable.

Therefore, the solution can be as follows:

- Read all n monitors.

- For each pair (i,j) where i < j, check if any of the four conditions is met.

- Count the number of such pairs.

But wait, perhaps some optimizations can be made. For example, precompute for each monitor a sorted pair (min, max) so that h_i <= w_i, but perhaps that's not necessary. Let's see.

But in the code, for each pair, we can just check the four possibilities. Let's see the sample input.

First example:

5 monitors:

3 2 → possible heights are 3 or 2 (but when rotated, the height can be 2 or 3). Wait, the dimensions are width and height. So when rotated, the height becomes the original width. So for a monitor with w=3, h=2, rotating would swap them, making height 3 or 2? Wait, when you rotate 90 degrees, the width and height are swapped. So the original height is 2. If you rotate, the width becomes 2, the height becomes 3. So the height can be either 2 (original) or 3 (rotated). So for each monitor, the possible heights are h_i and w_i. So the code should check if any of h_i, w_i is equal to any of h_j, w_j. So the four possibilities.

So for each pair i, j, check if h_i is in {h_j, w_j} OR w_i is in {h_j, w_j}.

Which can be written as (h_i == h_j) or (h_i == w_j) or (w_i == h_j) or (w_i == w_j). 

Alternatively, we can precompute a set for each monitor, like s_i = {h_i, w_i}, and then check if s_i and s_j have any intersection. The set approach might be faster in code, but in Python, checking set intersections for small sets might be efficient. But since each set has at most two elements, perhaps the explicit checks are faster.

But for code clarity and efficiency, perhaps the explicit checks are better.

So the code can loop over all i < j, and for each, check the four conditions. If any is true, increment the count.

But how to store the monitors? As a list of tuples. For each monitor, store (h, w) or (w, h)? Wait, no. Because for each monitor, when rotated, the height can be either of the two. So for each monitor, we have two possible heights. So in the code, for each monitor i, h_i and w_i can be swapped. But when checking against another monitor j, we need to consider all possible combinations.

But for the code, when given a monitor, we can just keep the original h and w as per input. Because when we check for a pair (i,j), whether i is rotated or not is irrelevant; we're checking all possible combinations of their possible heights.

So the code would proceed as:

Read n.

monitors = [tuple(map(int, input().split())) for _ in range(n)]

count = 0

for i in range(n):
    for j in range(i+1, n):
        h_i, w_i = monitors[i]
        h_j, w_j = monitors[j]
        # Check if any of the possible combinations matches
        if (h_i == h_j) or (h_i == w_j) or (w_i == h_j) or (w_i == w_j):
            count += 1

print(count)

Yes. That should work.

Testing this code against the first sample input.

Sample 1:

5

3 2 → h=3, w=2.

2 2 → h=2, w=2.

5 5 → h=5, w=5.

3 5 → h=3, w=5.

4 3 → h=4, w=3.

Pairs:

(0,1): check 3 ==2? 3==2? (w_i is 2). 3 vs j's h=2 and w=2. So h_i is 3, which equals neither 2 nor 2. w_i is 2, which is equal to j's h (2) and w (2). So 2 is in the j's set. So condition met. So count +=1.

But according to the first sample note, pair (1,2) is counted. Wait in the first sample, the output is 5. Let's see.

The code would process all pairs:

Total possible pairs for n=5 is 5*4/2=10.

But according to the first sample, 5 are valid.

The code should count correctly. Let's see:

So the code works for that pair.

Similarly, all other pairs would be checked. So the code should correctly compute the count.

In the second sample input, all pairs are valid. For n=7, the output is 21, which is 7 choose 2 (21). So all pairs are counted. So the code would return 21 for that case. Let's see why: all the monitors are such that their sets have at least one common element. For example, all of them have either 10 or 20 in their dimensions, so for any pair, there's a common value.

So the code would return the correct count.

So the code seems correct. Now, considering the constraints. For n=1e3, the number of pairs is (1000 * 999)/2 = 499,500. For each pair, we perform up to four comparisons. So total operations are around 4 * 5e5 = 2e6 operations, which is acceptable for Python, even with tight time limits.

But what about the data types? The problem states that the dimensions can be up to 1e9, but in Python, comparing integers is O(1) time.

So this approach is feasible. Therefore, the code as written should work.

Now, let's check possible optimizations. For example, precomputing for each monitor a set and checking for intersection. But in Python, checking if a set has any elements in common is O(1) for small sets. So for each monitor, store s_i = {h_i, w_i}. Then, for each pair (i,j), check if s_i & s_j is non-empty.

But in code:

s = [ {h, w} for h, w in monitors ]

count = 0

for i in range(n):
    for j in range(i+1, n):
        if s[i] & s[j]:
            count +=1

But this would also work, and perhaps be more concise. Let's see. However, in Python, the '&' operator for sets returns the intersection. So checking if the intersection is non-empty would be equivalent to checking if len(s[i] & s[j]) > 0.

But for each pair, creating the intersection set may have some overhead. Alternatively, since the sets have at most two elements each, perhaps the code can check if any element of s_i is in s_j. Which is O(1) time, since checking membership in a set of size two is O(1).

But how does this compare to the explicit four checks? Let's see.

In the original approach, for each pair, we do four comparisons. In the set approach, for each pair, we check if h_i is in s_j, or w_i is in s_j. Because s_i is {h_i, w_i}, but for j's set, we can check for either of the elements of s_i in j's set.

Wait, no. For pair (i,j), we can check if s_i and s_j have a non-empty intersection. Which can be done by checking if any element in s_i is present in s_j. So for s_i, which has h_i and w_i, check if either is in s_j. Since s_j is {h_j, w_j}, this is equivalent to checking the four possibilities.

But perhaps using sets is more efficient in code. Let's see. Let's compare:

Original code:

if (h_i == h_j) or (h_i == w_j) or (w_i == h_j) or (w_i == w_j):

Set-based code for i and j:

if (h_i in s_j) or (w_i in s_j):

Because s_j is {h_j, w_j}, so checking if h_i is in s_j is equivalent to h_i == h_j or h_i == w_j. Similarly, checking w_i in s_j is equivalent to w_i == h_j or w_i == w_j. So the condition (h_i in s_j) or (w_i in s_j) is exactly the same as the original four conditions.

Therefore, the code can be written as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    monitors = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(n)]
    count = 0
    for i in range(n):
        h_i, w_i = monitors[i]
        for j in range(i + 1, n):
            h_j, w_j = monitors[j]
            if h_i == h_j or h_i == w_j or w_i == h_j or w_i == w_j:
                count += 1
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
10 10
10 20
20 10
10 20
10 20
10 10
20 10
""",
            "output": \
"""\
21
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

Wait, but according to the sample note, pair (1,2) is not in the valid pairs. Wait sample note says the valid pairs are (1,2), (1,4), (1,5), (3,4), (4,5). Wait, perhaps the sample numbering is 1-based. So the first pair in the note is (1,2), which in 0-based indices would be (0,1). So in the sample note's first example, the pairs are:

(1,2) → 0 and 1 (0-based), which is counted.

Wait the sample note's first example says:

Valid pairs are (1,2), (1,4), (1,5), (3,4), (4,5). But in the code's 0-based indices, perhaps:

Wait the input is:

5 monitors:

1. 3 2 → index 0

2. 2 2 → index 1

3.5 5 → index 2

4.3 5 → index3

5.4 3 → index4.

So pair (1,2) in the note refers to index 0 and 1 (since the first two monitors). Which is counted as in the code.

The pair (3,4) in the note is index3 and4. Let's see.

Monitor 3 (3,5) and 4 (4,3). 

Check h_i=3, w_i=5. j=4's h=4, w=3.

Check 3 ==4? No. 3 ==3 → yes. So condition met. So pair (3,4) is counted. So code counts that.

So the code would correctly count all five pairs.

Thus, the code works.

Therefore, the code is as follows.
</think>

```python
n = int(input())
monitors = [tuple(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    h_i, w_i = monitors[i]
    for j in range(i + 1, n):
        h_j, w_j = monitors[j]
        if h_i == h_j or h_i == w_j or w_i == h_j or w_i == w_j:
            count += 1
print(count)
```
