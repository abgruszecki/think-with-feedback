<think>
Okay, so I need to solve this problem where I compare two strings lexicographically, ignoring case. Let's see. The problem says that the output should be -1, 1, or 0 based on the comparison. The key points here are that the comparison is case-insensitive.

First, I need to think about how to compare each corresponding character of the two strings. For each pair of characters, regardless of their case, I should convert them to the same case (like lowercase or uppercase) and then compare. So for example, 'a' and 'A' are considered equal. Then, once I find a position where the characters differ, I can determine the result based on which one is smaller.

The steps would be:

1. Iterate over each character pair from both strings.
2. For each pair, convert both to lowercase (or uppercase) and compare.
3. If they are different, return -1 or 1 depending on which is smaller.
4. If all characters are equal, return 0.

Now, considering the input constraints: the maximum length is 100, which is very small. So even a straightforward approach would work here. There's no need for any complex optimizations in terms of time complexity.

But how do I implement this in Python efficiently?

Let's think about converting the entire strings to lowercase (or uppercase) first, then comparing. But comparing the entire transformed strings might be more efficient than comparing character by character. Wait, but the problem requires a lexicographical comparison. So if we convert both strings to the same case, then compare them using the standard string comparison, that would work.

Yes! Because the lexicographical order when both are in the same case (like lowercase) would directly give the correct result. For example, if the first string in lowercase is 'abc' and the second is 'abd', then 'abc' < 'abd' so the result is -1. Exactly what we need.

So the plan is:

- Convert both input strings to lowercase (or uppercase, doesn't matter).
- Compare the two lowercase strings lexicographically.
- Return -1 if str1 < str2, 1 if str1 > str2, else 0.

Wait, but the problem statement says that the case does not matter. So converting both to lowercase (or uppercase) and then comparing lex order would give the correct result.

Yes. So for example, in the first sample input:

aaaa vs aaaA. Both become aaaa and aaaa, compare equal, output 0. Correct.

Second example: abs vs Abz. Lowercase becomes abs vs abz. Compare each character. The first two are a and a (same), then b and b (same), then s vs z. s comes before z, so the first string is smaller. So output -1. Which matches the sample.

Third example: abcdefg vs AbCdEfF. Lowercase: abcdefg vs abcdefff. Compare each character. At the sixth position (index 5), 'f' vs 'f' (same), then the seventh (index 6) 'g' vs 'f'. So the first string's character is higher, so output 1. Correct.

So this approach works. So the code would be:

Read the two input strings, convert them both to lowercase, compare, then return -1, 0, or 1 based on the comparison.

But wait, how does Python handle string comparisons? It does compare lex order. So if s1_lower < s2_lower, then output -1, else if s1_lower > s2_lower, output 1, else 0.

So code steps:

Read s1 and s2.

s1_lower = s1.lower()
s2_lower = s2.lower()

if s1_lower < s2_lower:
    print(-1)
elif s1_lower > s2_lower:
    print(1)
else:
    print(0)

That's all. This is the simplest and most efficient approach.

But wait, is there any edge case where this approach might not work? Let's think. The problem states that the strings are of the same length, so comparing directly is safe. Because in Python, if two strings have the same characters up to the length of the shorter, then the longer is considered larger. But here, the problem says the two strings are the same length, so converting to lowercase and comparing the entire string is safe.

So the code is straightforward.

Testing the sample cases:

Sample 1:

Input:
aaaa
aaaA

Converted to lowercase: aaaa and aaaa. Equal. Output 0.

Sample 2:

abs vs Abz. Lowercase: abs vs abz. 'abs' is less than 'abz' (since s < z). So output -1.

Sample3:

abcdefg vs AbCdEfF. Lowercase: abcdefg vs abcdefff. Compare each character:

a a: same
b b: same
c c: same
d d: same
e e: same
f f: same
g vs f: g is after f, so the first string is larger. So output 1. Correct.

So the code works for these cases.

What about when the strings are like 'A' and 'b'? Lowercase 'a' vs 'b' → 'a' is smaller, so output -1.

Another test case: 'Apple' vs 'apple' → both lowercase same → 0.

So the code is correct.

In terms of efficiency, converting the strings to lowercase is O(n) time, which for n=100 is trivial. The comparison is O(n) as well, but again, no problem. So this approach is optimal for the given constraints.

So this code should work.
</think>

```python
s1 = input().strip().lower()
s2 = input().strip().lower()
if s1 < s2:
    print(-1)
elif s1 > s2:
    print(1)
else:
    print(0)
```