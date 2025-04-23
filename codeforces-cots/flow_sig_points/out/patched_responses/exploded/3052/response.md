<think>
Okay, let's see. The problem is to find the maximum number of elements in a pretty set of positions in a given string. The pretty set has two conditions: all the letters at those positions are distinct lowercase letters, and there are no uppercase letters between any two selected positions. Hmm.

So first, I need to understand what the problem is really asking. Let's break it down. The positions in set A must all be lowercase and distinct. Also, between any two positions in A, there can't be any uppercase letters. Wait, the second condition says that there's no j that's between a1 and a2 (where a1 and a2 are in A) such that s[j] is uppercase. So the entire span between any two selected positions must be free of uppercase letters. But wait, the way the problem is phrased, for all pairs of positions in A, the interval between them must not contain any uppercase letters. Wait, no, because it says "there is no such j that s[j] is uppercase and a1 < j < a2 for some a1 and a2 from A". So if there's even one uppercase in any of the intervals between two selected positions, the entire set A is invalid.

So the set A must be such that all the positions are lowercase, unique in their characters, and the regions between any two positions in A (ordered by their positions) do not have any uppercase letters. Hmm. So how can we model this?

Alternatively, maybe the entire segment from the first to the last position in A must not contain any uppercase letters. Because if that's the case, then any two positions in A would have the entire range between them covered. Because if the entire span from the first to last element in A is free of uppercase letters, then between any two a1 and a2 in A, the part between them (which is within the entire span) would also have no uppercase letters.

Wait, maybe that's a key insight. Let me think. Suppose we select a subset A of positions where all the characters are distinct lowercase letters. Also, the entire interval from the minimum position in A to the maximum position in A must not contain any uppercase letters. Because if that's true, then there can't be any uppercase letters between any two positions in A. Because if there was a j between a1 and a2 in A, then j would be within the min and max of A, hence in the entire interval. So if the entire interval is uppercase-free, then between any two a1 and a2, there's no uppercase.

So the problem reduces to selecting a subset of positions with distinct lowercase letters, such that the entire range from the earliest to the latest in the subset contains no uppercase letters. And we need to maximize the size of such a subset.

Wait, but maybe the subset could consist of positions that are non-consecutive but their entire span is uppercase-free. For example, positions 1, 3, 5. If the entire span from 1 to 5 has no uppercase, then even though there's a position 2 and 4 (which are between some elements of A), but if those are lowercase, but not in A, then that's okay. Because the problem's second condition is only about uppercase letters in between.

So the correct approach is to find intervals in the original string where there are no uppercase letters. For each such interval, we can collect all the lowercase letters in that interval, and then select the maximum number of unique lowercase letters possible from that interval. Then, the answer is the maximum of these across all possible intervals.

Wait, that's a promising approach. Because each interval (a contiguous substring with no uppercase letters) can contribute some lowercase letters. For each such interval, the maximum possible distinct lowercase letters in it is the count. Then, the answer is the maximum count among all possible such intervals.

But how do we find all intervals with no uppercase letters? Because any substring that doesn't contain any uppercase letters can be considered. But since the letters in the set A must form a subset of positions within some interval that has no uppercase letters, the maximum possible size of A is the maximum number of distinct lowercase letters in any such interval.

So the problem reduces to: find all possible intervals [i,j] where all characters from i to j (inclusive) are lowercase, and then for each such interval, compute the number of unique lowercase letters in it. The maximum of these is the answer.

Wait, but that's not exactly correct. Because in the original problem, the set A can be any subset of the positions in the interval [i,j], but the letters must be distinct. So the maximum possible is the number of unique lowercase letters in the interval. So for each interval where the entire interval is uppercase-free, we count the number of distinct lowercase letters in it, and the maximum among all such intervals is the answer.

Yes! Because in such an interval, all the letters are lowercase, and the entire interval is uppercase-free. So selecting all distinct letters in this interval gives a valid set A, as there are no uppercase letters between any two positions in the interval (since the entire interval is uppercase-free). So the maximum size of such a set is the maximum number of distinct lowercase letters in any such interval.

So the problem now becomes: find the maximum number of distinct lowercase letters in any substring that is entirely composed of lowercase letters (i.e., no uppercase in it). Then, the answer is this maximum.

So the approach is:

1. Iterate through all possible intervals [i, j] in the string where all characters from i to j are lowercase letters (i.e., no uppercase letters in the substring s[i..j]).

2. For each such interval, compute the number of distinct lowercase letters in it.

3. The maximum of these values across all possible intervals is the answer.

If there are no such intervals (like in the third example where all are uppercase), then the answer is 0.

So how do we efficiently compute this?

The brute-force approach would be to check all possible intervals, which is O(n^2) for the intervals, and for each interval, count the distinct characters, which is O(n) time. So total O(n^3) time, which for n=200 is 200^3=8,000,000, which is acceptable. Because 8 million operations can be handled within 2 seconds in Python.

So the optimal approach is feasible even with O(n^3) time.

Alternatively, we can optimize it by precomputing the ranges and for each possible starting and ending point, track the unique characters.

But perhaps the simplest way is to generate all possible intervals and check for uppercase letters. Let's see.

So first, for each possible starting index i (0-based?), let's iterate through j from i to n-1. For each j, check if s[i..j] contains any uppercase letters. If not, then compute the number of distinct characters in s[i..j]. Keep track of the maximum.

So here's the steps:

For i in 0 to n-1:

   create a set to track the current distinct characters.

   for j in i to n-1:

      if s[j] is uppercase: break, because adding this j would make the interval invalid.

      else:

          add s[j] to the set.

          update the maximum if the size of the set is larger than current maximum.

This approach is O(n^2) time, which is better. Because for each i, j starts at i and moves forward. As soon as we encounter an uppercase, we break and move to the next i.

Yes, because once we find an uppercase in j for a particular i, any j beyond that will also include that uppercase (since the interval is i to j). So once an uppercase is found, all larger j's for that i are invalid, so we can break.

So this approach would be O(n^2) in the worst case. For n=200, 200*200=40,000 operations, which is very manageable.

So the algorithm is:

Initialize max_count = 0.

For each i from 0 to n-1:

    current_chars = set()

    for j from i to n-1:

        char = s[j]

        if char is uppercase:

            break

        if char not in current_chars:

            current_chars.add(char)

        current_count = len(current_chars)

        if current_count > max_count:

            max_count = current_count

So that's O(n^2) time and O(1) space per iteration (since the set is being maintained per i).

This seems efficient enough.

Let's test this approach against the examples.

First example:

Input: 11, "aaaaBaabAbA"

Looking for all intervals that are lowercase only.

So the string is: a a a a B a a b A b A

Wait, indexes 0 to 10.

The uppercase letters are at positions 4 (B), 8 (A), 10 (A).

So possible intervals:

i=0: j goes 0-3 (since s[4] is uppercase). The substring is 'aaaa' → distinct count is 1.

i=1: j can go 1-3. same as above.

i=4 is uppercase, so skip.

i=5: starts at 5. The substring s[5] to s[7] is 'aab' (positions 5,6,7). s[5] is 'a', s[6] is 'a', s[7] is 'b'. So distinct count is 2. Then j=8 is uppercase → break. So for i=5, the max is 2.

i=6: j=6 is a, j=7 is b → count 2. j=8 is uppercase → break.

i=7: j=7 is b → count 1. j=8 is uppercase → break.

i=8 is uppercase.

i=9 is 'b' (lowercase?), but s[9] is lowercase? The input is "aaaaBaabAbA". Let's parse:

Original input: "aaaaBaabAbA"

Breaking down each character:

Indices 0-10:

0: a

1: a

2: a

3: a

4: B (uppercase)

5: a

6: a

7: b (lowercase)

8: A (uppercase)

9: b (lowercase)

10: A (uppercase)

So i=5: j can go up to 7 (since 8 is uppercase). The substring is aab (positions 5,6,7). The set is {'a', 'b'}, size 2.

i=7: j=7 is 'b' → count 1.

i=9: starts at 9, which is 'b'. j=9: 'b' → count 1. j=10 is uppercase → break. So count 1.

So the maximum is 2, which matches the first example.

Second example:

Input 12, "zACaAbbaazzC"

The string is: z A C a A b b a a z z C

Wait, let's see:

Original input: "zACaAbbaazzC"

Indices 0-11:

0: z (lowercase)

1: A (uppercase)

2: C (uppercase)

3: a (lowercase)

4: A (uppercase)

5: b (lowercase)

6: b (lowercase)

7: a (lowercase)

8: a (lowercase)

9: z (lowercase)

10: z (lowercase)

11: C (uppercase)

So possible intervals:

Looking for intervals without uppercase.

Possible intervals:

- i=0: only j=0 (since j=1 is uppercase). So count 1 (z).

- i=3: s[3] is a. Check j=3: a. Then j=4 is uppercase → break. So count 1.

i=5: j from 5 to 10 (since j=11 is uppercase). The substring is b, b, a, a, z, z. The distinct letters are b, a, z → count 3. So that's one of the intervals that gives the maximum of 3.

Another interval could be 7-10: a, a, z, z → distinct a, z → count 2.

So the maximum is 3.

Third example: input 3, "ABC". All uppercase. So no intervals → answer 0.

So the approach works.

Thus, the code can be written as follows.

We need to:

Loop each i from 0 to n-1:

   if s[i] is uppercase → skip (since starting at i would include this uppercase, but in the code, the inner loop starts j at i. So for example, if i is uppercase, then j starts at i, and the first char is uppercase, so the inner loop breaks immediately. So the code would not process any i where s[i] is uppercase. So the code already handles that.

Wait, no. Let's see: when i is a position where s[i] is uppercase, then in the inner loop j starts at i. The first character is uppercase, so the code breaks out of the inner loop. So current_chars remains empty, and no updates to max_count. So correct.

So the code can proceed as described.

Now, in Python, the code would read n, then s. Then, loop through each i in range(n). For each i, initialize a set. Then, for j in range(i, n). Check if s[j] is uppercase: if so, break. Else, add to the set, and check if the current size is larger than the maximum.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()
    max_count = 0

    for i in range(n):
        current_chars = set()
        for j in range(i, n):
            c = s[j]
            if c.isupper():
                break
            current_chars.add(c)
            current_size = len(current_chars)
            if current_size > max_count:
                max_count = current_size

    print(max_count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
12
zACaAbbaazzC
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()
    max_count = 0

    for i in range(n):
        current_chars = set()
        for j in range(i, n):
            c = s[j]
            if c.isupper():
                break
            current_chars.add(c)
            current_size = len(current_chars)
            if current_size > max_count:
                max_count = current_size

    print(max_count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
ABC
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

Third example:

n=3, s='ABC'. All uppercase. So all i loops break immediately. So max remains 0.

Thus, the code works.
</think>

```python
n = int(input())
s = input().strip()
max_count = 0

for i in range(n):
    current_chars = set()
    for j in range(i, n):
        c = s[j]
        if c.isupper():
            break
        current_chars.add(c)
        current_size = len(current_chars)
        if current_size > max_count:
            max_count = current_size

print(max_count)
```
