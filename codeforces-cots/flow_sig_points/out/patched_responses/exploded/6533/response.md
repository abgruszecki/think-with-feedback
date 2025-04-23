<think>
Okay, let's see. We need to find the minimum number of moves to make two strings equal by deleting the first character from either of them. Each move reduces the length of one string by one. The goal is to have both strings equal with as few deletions as possible.

Hmm. So the key is to find the longest possible common suffix between the two strings. Because the more characters they share at the end, the fewer deletions we need. Because for each matching character at the end, we can leave those and delete the preceding ones.

Wait, right. For example, if the original strings are s and t, then the maximum number of characters that match from the end is the length of their common suffix. Then, the minimal moves required would be (len(s) - k) + (len(t) - k), where k is the length of the longest common suffix.

Yes. So the problem reduces to finding the maximum k where the last k characters of s and t are the same. Then the answer is the sum of their lengths minus twice k.

So how do we find this k efficiently?

The maximum possible k is the minimum of the lengths of s and t. So first, we can check from the end of both strings. Compare the characters starting from the end. For each position, if they match, we increment k. Once a mismatch is found, we stop.

But wait, what if one string is longer than the other? For example, s is "abc", t is "xyzabc". Then the common suffix is "abc", which has length 3. So even if t is longer, the common suffix is determined by the overlapping parts.

So the approach would be:

1. Initialize k = 0.
2. Start comparing characters from the end of both strings.
3. While the current indices are valid (i >=0 and j >=0), check if s[i] == t[j].
4. If yes, increment k, decrement i and j.
5. If no, break the loop.
6. The result is (len(s) + len(t)) - 2*k.

That's correct. Because for each matching character in the suffix, we save two moves (since we don't have to delete those characters from either string). So the total required moves are the sum of the lengths minus twice the length of the common suffix.

So the main task is to compute this k efficiently.

Now, considering the constraints. The strings can be up to 2e5 characters each. So iterating from the end up to the first mismatch is O(k), which is O(n) in the worst case, but acceptable since 2e5 is manageable.

So the algorithm is linear time, which should be okay for the time constraints.

Let me think about some test cases.

Take the first example:

s = "test", t = "west".

s's characters from end: t, s, e, t (reverse order). Wait, no. Wait, s is 't','e','s','t'. So the end is 't', then 's', then 'e', then 't'.

t is 'w','e','s','t'. So the end is 't', then 's', then 'e', then 'w'.

Comparing from the end:

s's last character is 't', t's last is 't' → match. k=1. Then next (s's index 2, t's index 2: 's' and 's' → match. k=2. Next, s's index 1: 'e', t's index 1: 'e' → match. k=3. Then s's index 0: 't', t's index 0: 'w' → no match. So k is 3. Then the answer is (4+4) - 2*3 = 8-6=2. Which matches the example.

Another example: codeforces and yes.

s is codeforces, which ends with 'es' (since codeforces is 'c o d e f o r c e s'). t is 'yes', which ends with 's', then 'e', then 'y'. The common suffix is 'es' (since codeforces ends with 'es', and 'yes' ends with 's'? Wait wait, wait:

s: 'codeforces' → length 10. So the last two characters are 'e' and 's' (positions 9 and 8 in zero-based?), wait no. Wait, the last character is s (index 9), then e (index 8), then c (7), etc.

t is 'yes' → length 3. Last character is 's' (index 2), then 'e' (1), then 'y' (0).

Compare s[9] = 's' and t[2] = 's' → match. Then s[8] = 'e' and t[1] = 'e' → match. Then s[7] = 'c' and t[0] = 'y' → no match. So k is 2. So answer is (10 +3) - 2*2 =13-4=9. Which matches the example.

Third example: test and yes. s is test (ends with t s e t?), wait no. Wait, 'test' is t-e-s-t. So indexes 0 to 3. So last character is t (index 3), then s (2), e (1), t (0). 'yes' is y-e-s. Last character is s (index 2), e (1), y (0). So comparing:

s's index 3 (t) vs t's index 2 (s) → no. So k starts as 0. So answer is 4+3 -0 =7. Which matches the third example.

Fourth example: s is 'b', t is 'ab'. So s is 'b' (length 1), t is 'a','b' (length 2). Compare s[0] (b) with t[1] (b) → match. Then s is at -1, t is at 0. So k is 1. Answer is 1 + 2 - 2*1 = 3-2=1. Which is correct.

So the approach works for all these cases.

So the steps are:

- Get the lengths of s and t.

- Initialize i to len(s)-1, j to len(t)-1.

- Initialize k=0.

- While i >=0 and j >=0:

   if s[i] == t[j], then k +=1, i -=1, j -=1.

   else, break.

- The answer is (len(s) + len(t)) - 2*k.

Yes.

So in Python, this can be implemented efficiently.

But how to handle the strings? Since in Python, strings are zero-based. So s = input().strip(), t = input().strip().

Then i = len(s)-1, j = len(t)-1.

Loop:

while i >=0 and j >=0 and s[i] == t[j]:

   k +=1

   i -=1

   j -=1

Then the answer is (len(s) + len(t) - 2*k).

This is straightforward.

Now, considering the time constraints: for two strings of 2e5 characters each, the loop could run up to 2e5 steps. But in Python, this is acceptable because each step is a simple comparison and arithmetic. The total time should be within 1 second.

Yes. So the code should be efficient.

So the code will be:

Read s and t.

i = len(s)-1

j = len(t)-1

k=0

while i >=0 and j >=0 and s[i] == t[j]:

    k +=1

    i -=1

    j -=1

print(len(s) + len(t) - 2*k)

Yes.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    t = input_stream.readline().rstrip("\n").strip()

    i, j = len(s) - 1, len(t) - 1
    k = 0

    while i >= 0 and j >= 0 and s[i] == t[j]:
        k += 1
        i -= 1
        j -= 1

    print(len(s) + len(t) - 2 * k, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
codeforces
yes
""",
            "output": \
"""\
9
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
    t = input_stream.readline().rstrip("\n").strip()

    i, j = len(s) - 1, len(t) - 1
    k = 0

    while i >= 0 and j >= 0 and s[i] == t[j]:
        k += 1
        i -= 1
        j -= 1

    print(len(s) + len(t) - 2 * k, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
test
yes
""",
            "output": \
"""\
7
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    t = input_stream.readline().rstrip("\n").strip()

    i, j = len(s) - 1, len(t) - 1
    k = 0

    while i >= 0 and j >= 0 and s[i] == t[j]:
        k += 1
        i -= 1
        j -= 1

    print(len(s) + len(t) - 2 * k, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
b
ab
""",
            "output": \
"""\
1
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

Fourth example: s='b' (len1), t='ab' (len2). i=0, j=1. s[0] is 'b' vs t[1] 'b' → yes. k=1. i becomes -1, j=0. loop ends. Answer 1+2-2=1. Correct.

So this code works for all the examples. The code is optimal because it runs in O(k) time, where k is the length of the common suffix, which is O(n) in worst case. But since n is 2e5, this is manageable.

No data structures are needed beyond the input strings. The variables i and j are pointers moving from the end towards the start, comparing characters. So the code is both time and memory efficient.
</think>

```python
s = input().strip()
t = input().strip()

i, j = len(s) - 1, len(t) - 1
k = 0

while i >= 0 and j >= 0 and s[i] == t[j]:
    k += 1
    i -= 1
    j -= 1

print(len(s) + len(t) - 2 * k)
```
