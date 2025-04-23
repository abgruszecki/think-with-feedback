<think>
Okay, let's see. The problem is to find the minimum number of changes needed to make a string "fancy", which means all uppercase letters are on the left of any lowercase ones. So, the string should have some uppercase letters first (maybe zero), then some lowercase letters (maybe zero). 

So for each position in the string, we need to decide where the split between uppercase and lowercase happens. The split could be at any point, including the beginning (all lowercase) or the end (all uppercase). For each possible split point, calculate how many characters to the left are lowercase (they need to be changed to uppercase) and how many to the right are uppercase (they need to be changed to lowercase). The total for that split is the sum of those two counts, and we need the minimum total over all possible split points.

Hmm, right. So the approach is to precompute the number of lowercase letters to the left of each position and the number of uppercase letters to the right. Then, for each possible split (including before the first character and after the last), sum the left lowercase and right uppercase counts for that split, and take the minimum.

Wait, but how do we compute that efficiently?

Let's think. Let's say we have a string of length n. For each position i (0-based), the split is after i. Wait, no. Wait, the split is the point where everything to the left (including i) is uppercase, and everything to the right (i+1 onwards) is lowercase. Wait, no. Wait, the split could be between index i-1 and i, meaning that all characters before i are uppercase, and i onwards are lowercase. So for a split at position i (ranging from 0 to n, where 0 means all are lowercase, and n means all are uppercase), we need:

Number of uppercase to the left of i that are lowercase (so we need to change them to uppercase? Wait no. Wait, the split is after the uppercase part. So for the split at i, the left part is 0 to i-1 (all uppercase), and the right part is i to n-1 (all lowercase). Wait, maybe I'm mixing the indices here. Let me clarify.

The split can be thought of as a point in the string where everything before it must be uppercase, and everything after (including the split point) must be lowercase. Or wait, maybe the split is between two characters. For example, if the split is after k characters, then the first k are uppercase, and the rest are lowercase. So for split at position k (0 <= k <= n), the first k characters are uppercase, the remaining n -k are lowercase.

Yes. So for each possible k (from 0 to n), the cost is the number of lowercase letters in the first k characters (they need to be changed to uppercase) plus the number of uppercase letters in the last n-k characters (they need to be changed to lowercase). Then, find the k where this sum is minimized.

So the problem reduces to precomputing two arrays:

- For each k, the number of lowercase letters in the first k characters (prefix sum).
- For each k, the number of uppercase letters in the characters from k to n-1 (suffix sum).

Then, the total cost for split k is (prefix_lower[k] + suffix_upper[k]).

Wait, wait. Let's think about the split as after the first k characters. So the first k characters must be uppercase. So any lowercase letters in the first k need to be changed. Then, the remaining (n -k) characters must be lowercase. So any uppercase in those (n -k) characters need to be changed.

So for each k from 0 to n (inclusive), compute the sum of:

lower_in_first_k = number of lowercase letters in the first k characters (since each needs to be changed to uppercase: 1 change each)
upper_in_last_n_minus_k = number of uppercase letters in the last (n -k) characters (each needs to be changed to lowercase: 1 change each)
sum these two numbers. The minimum of all these sums is the answer.

So the steps are:

1. Precompute a prefix array where prefix[k] is the number of lowercase letters in the first k characters (0 <= k <= n). So for example, prefix[0] is 0, prefix[1] is 0 if the first character is uppercase, else 1, etc. So this is a standard prefix sum where each character contributes 1 if it's lowercase.

2. Precompute a suffix array where suffix[k] is the number of uppercase letters from position k to end. So suffix[0] is the total number of uppercase letters in the entire string. suffix[1] is the number from position 1 onwards, etc. So for each k, suffix[k] is the count of uppercase letters in s[k:].

Once these two arrays are computed, then for each possible split k (0 <=k <=n), compute prefix[k] + suffix[k], and find the minimum value.

Yes. That seems right.

So the question is how to compute these prefix and suffix arrays efficiently.

The prefix array can be built by iterating through the string once, keeping a running total. Similarly, the suffix array can be built by iterating from the end backwards.

For example:

s = "PRuvetSTAaYA"

n = len(s) = 12 (assuming example 1 input is length 12, but let's check. The input example 1 is "PRuvetSTAaYA" which is 12 characters: let's see.

Wait, the first example input is "PRuvetSTAaYA". Let's count the letters:

P R v e t S T A a Y A --> let me count again. Let's see:

P (1), R (2), v (3, lowercase), e (4, lc), t (5, lc), S (6, uppercase), T (7, up), A (8, up), a (9, lc), Y (10, up), A (11, up). Wait, maybe I'm miscounting, but the example's output is 5. So according to their solution, the minimal changes are 5.

But regardless, the approach is correct.

So for the prefix sum:

prefix[0] = 0 (0 characters)
prefix[1] = 0 if s[0] is uppercase, else 1.
prefix[2] = prefix[1] + 0 or 1 depending on s[1], etc.

For the suffix sum:

suffix[k] is the number of uppercase letters in s[k:].

So for example, suffix[0] is the total uppercase letters in the entire string.

suffix[n] = 0 (since s[n:] is empty).

We can compute the suffix array by starting from the end. For example, for position i, suffix[i] = suffix[i+1] + (1 if s[i] is uppercase else 0). But since we need suffix[k], which counts the number of uppercase letters in positions k, k+1, ..., n-1, we can compute this by iterating from the end.

So for the example input:

Let's take the first example, input "PRuvetSTAaYA" (assuming that's the correct string). Let's compute the prefix and suffix arrays.

But maybe the code will handle that.

Now, the code steps:

Read the string.

Compute the prefix array of lowercase counts.

Compute the suffix array of uppercase counts.

Then iterate over each possible k (0 to n) and compute prefix[k] + suffix[k], find the minimum.

Now, the time complexity is O(n), which is acceptable for n up to 1e5.

Space complexity is O(n), which is also acceptable.

But can we optimize the space? Let's think. The prefix array can be built in O(n) time and O(n) space. Similarly for the suffix array. For n=1e5, each array is 1e5+1 elements. That's 2*1e5+2 elements, which is manageable in Python (each is an integer, so around 800KB for 1e5 elements, which is acceptable given the 256MB memory limit).

So code steps in Python:

Read s.

n = len(s)

Compute prefix_lower: a list where prefix_lower[k] is the number of lowercase letters in s[0..k-1] (since for split k, the first k characters are considered). Wait, wait. Let's clarify.

Wait, when split is k, the first k characters (indices 0 to k-1) must be uppercase, and the rest (k to n-1) must be lowercase. So for split k, the number of lowercase letters in the first k characters is the number of changes needed for the first part. Then, the number of uppercase letters in the remaining (n -k) characters is the number of changes needed for the second part.

So the prefix_lower array should have prefix_lower[k] = number of lowercase letters in the first k characters (indices 0 to k-1). So for k=0, there are 0 characters, so prefix_lower[0] = 0. For k=1, it's 0 if s[0] is uppercase, else 1. For k=2, it's the sum of s[0] and s[1] being lowercase. And so on.

Similarly, the suffix_upper array for k is the number of uppercase letters in the substring starting at k (inclusive) to the end (indices k to n-1). So for k=0, it's the total uppercase letters in the entire string. For k =n, it's zero.

So the code steps would be:

Compute prefix_lower:

prefix_lower = [0] * (n+1)
for i in range(n):
    prefix_lower[i+1] = prefix_lower[i] + (1 if s[i].islower() else 0)

Compute suffix_upper:

suffix_upper = [0] * (n+1)
for i in range(n-1, -1, -1):
    suffix_upper[i] = suffix_upper[i+1] + (1 if s[i].isupper() else 0)

Then, for each k in 0..n:

current = prefix_lower[k] + (suffix_upper[k] ) 

Wait, because suffix_upper[k] is the number of uppercase letters from k to n-1. So if the split is at k, the characters from k to n-1 must be lowercase. So each uppercase in those positions must be changed. So the number of changes is the count of uppercase letters in those positions.

So the total changes for split k is prefix_lower[k] (the lowercase letters in the first k characters) + suffix_upper[k] (uppercase letters in the remaining n -k characters).

Yes.

So, the code would then compute the minimum over all possible k of prefix_lower[k] + suffix_upper[k].

This is O(n) time and O(n) space, which is acceptable.

Let's test with the first example:

Input: "PRuvetSTAaYA"

Let's list each character and their case (uppercase or lowercase):

Indices 0-:

0: P (upper)
1: R (upper)
2: v (lower)
3: e (lower)
4: t (lower)
5: S (upper)
6: T (upper)
7: A (upper)
8: a (lower)
9: Y (upper)
10: A (upper)

So n is 11.

Compute prefix_lower:

prefix_lower[0] = 0

k=1 (s[0] is upper) --> 0.

k=2 (s[0], s[1] are upper) --> 0.

k=3: s[2] is lower --> add 1. prefix_lower[3] = 1.

k=4: s[3] is lower --> +1. prefix_lower[4] = 2.

k=5: s[4] is lower --> +1. prefix_lower[5] =3.

k=6: s[5] is upper --> no. prefix_lower[6] =3.

k=7: s[6] is upper --> same. prefix_lower[7] =3.

k=8: s[7] is upper --> same. prefix_lower[8] =3.

k=9: s[8] is lower --> +1. prefix_lower[9] =4.

k=10: s[9] is upper --> same. prefix_lower[10] =4.

k=11: s[10] is upper --> same. prefix_lower[11] =4.

So prefix_lower array is [0,0,0,1,2,3,3,3,3,4,4,4].

Wait, but the split k can be from 0 to 11 (since n=11). So for each k in 0..11:

split k=0: the first 0 characters (none) must be uppercase (no changes), and all characters must be lowercase. So we need to count the uppercase letters in the entire string. 

split k=5: first 5 characters (indices 0-4) must be uppercase. Then the rest (5-10) must be lowercase.

So let's compute suffix_upper:

suffix_upper[k] for k=0 to 11.

Starting from the end.

suffix_upper[11] =0.

k=10: s[10] is upper --> 1 + suffix_upper[11] =1.

k=9: s[9] is upper --> 1 + suffix_upper[10] (1) =2.

k=8: s[8] is lower --> 0 + suffix_upper[9] (2) =2.

k=7: s[7] is upper -->1 + suffix_upper[8] (2) =3.

k=6: s[6] is upper -->1 + suffix_upper[7] (3) =4.

k=5: s[5] is upper -->1 + suffix_upper[6] (4) =5.

k=4: s[4] is lower -->0 + suffix_upper[5] (5) =5.

k=3: s[3] is lower -->0 + suffix_upper[4] (5) =5.

k=2: s[2] is lower -->0 + suffix_upper[3] (5) =5.

k=1: s[1] is upper -->1 + suffix_upper[2] (5) =6.

k=0: s[0] is upper -->1 + suffix_upper[1] (6) =7.

So suffix_upper array is:

suffix_upper[0] =7 (total uppercase letters in the entire string), then for k=1 it's 6, k=2 is 5, etc.

Wait, for k=5:

s[5] is S (upper), and from k=5 to 10, the uppercase letters are S, T, A, Y, A. So 5 uppercase letters. So suffix_upper[5] is 5. Which matches.

Now, for each split k:

For example, let's take k=3. Then:

prefix_lower[3] is 1 (the first 3 characters are P, R, v. The lowercase is v, so 1 change).

suffix_upper[3] is 5 (from e, t, S, T, A, a, Y, A. Wait, k=3 is index 3 onwards? So the substring starts at index 3 (e) to 10 (A). The uppercase letters in this substring are S (index5), T (6), A (7), Y (9), A (10) --> 5 uppercase letters. So suffix_upper[3] is 5.

So for k=3, the cost is 1 +5=6. But the example's output is 5. So maybe there's a better split.

Wait, let's compute for all possible k.

We need to find the minimum sum of prefix_lower[k] + suffix_upper[k].

Let's compute all possible k values for the first example.

The possible k values are from 0 to 11 (n=11).

For each k:

k=0:

prefix_lower[0] =0.

suffix_upper[0] =7. Sum is 7.

k=1:

prefix_lower[1] =0 (since first character is uppercase). suffix_upper[1] =6. Sum 6.

k=2:

prefix_lower[2] =0. suffix_upper[2] =5. Sum 5.

Wait, wait, maybe that's the minimum? Because the example's output is 5.

Wait, let's see:

At k=2, the split is after the first 2 characters (indices 0 and 1). The first two are P and R (both uppercase, so no changes needed). The remaining 9 characters (indices 2-10) must be lowercase. 

In the remaining part (indices 2-10), how many uppercase letters are there?

Looking at the original string:

v (lc), e (lc), t (lc), S (up), T (up), A (up), a (lc), Y (up), A (up). So uppercase letters: S, T, A, Y, A --> 5. So suffix_upper[2] is 5. So sum is 0+5=5. Which matches the example's output of 5.

So yes, that's the correct split.

So the code would correctly find this split.

Thus, the approach is correct.

Now, coding this in Python.

Edge cases:

1. All lowercase: output is 0. Because split at 0, which requires all characters to be lowercase, which they already are. So prefix_lower[0] is 0 (since there are no characters to check), suffix_upper[0] is the number of uppercase letters in the entire string (which is 0). So sum is 0.

Wait, wait. Wait, split at k=0: the first 0 characters (none) must be uppercase, and the entire string must be lowercase. So if the entire string is lowercase, then the sum is prefix_lower[0] (0) + suffix_upper[0] (number of uppercase in entire string, which is 0) → 0. So correct.

Another edge case: all uppercase. Split at k=n (so all are uppercase, nothing to change. sum is 0.

Another case: mix.

So the code seems to handle all cases.

Now, code:

Read s.

n = len(s)

Compute prefix_lower and suffix_upper.

Then compute min(prefix_lower[k] + suffix_upper[k] for all k in 0..n).

But wait, the code for suffix_upper in Python can be built as follows:

Initialize a list of n+1 elements. suffix_upper[n] =0.

Then, loop i from n-1 downto 0:

suffix_upper[i] = suffix_upper[i+1] + (1 if s[i] is upper else 0)

Yes.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = len(s)

    prefix_lower = [0]*(n+1)
    for i in range(n):
        prefix_lower[i+1] = prefix_lower[i] + (1 if s[i].islower() else 0)

    suffix_upper = [0]*(n+1)
    for i in range(n-1, -1, -1):
        suffix_upper[i] = suffix_upper[i+1] + (1 if s[i].isupper() else 0)

    min_changes = float('inf')
    for k in range(n+1):
        current = prefix_lower[k] + suffix_upper[k]
        if current < min_changes:
            min_changes = current

    print(min_changes, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
OYPROSTIYAOPECHATALSYAPRIVETSTASYA
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = len(s)

    prefix_lower = [0]*(n+1)
    for i in range(n):
        prefix_lower[i+1] = prefix_lower[i] + (1 if s[i].islower() else 0)

    suffix_upper = [0]*(n+1)
    for i in range(n-1, -1, -1):
        suffix_upper[i] = suffix_upper[i+1] + (1 if s[i].isupper() else 0)

    min_changes = float('inf')
    for k in range(n+1):
        current = prefix_lower[k] + suffix_upper[k]
        if current < min_changes:
            min_changes = current

    print(min_changes, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
helloworld
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

Sample Input 3:

helloworld → output 0.

Because split at 0, the entire string is lowercase. So sum 0 + 0 =0.

Thus, the code works.

Now, check for time and space constraints.

n is up to 1e5. All loops are O(n). The three arrays (prefix_lower, suffix_upper) are O(n), but in Python, list comprehensions are efficient.

So the code should handle 1e5 characters quickly.

Therefore, this is the optimal approach.
</think>

```python
s = input().strip()
n = len(s)

prefix_lower = [0] * (n + 1)
for i in range(n):
    prefix_lower[i+1] = prefix_lower[i] + (s[i].islower())

suffix_upper = [0] * (n + 1)
for i in range(n-1, -1, -1):
    suffix_upper[i] = suffix_upper[i+1] + (s[i].isupper())

min_changes = min(prefix_lower[k] + suffix_upper[k] for k in range(n+1))
print(min_changes)
```
