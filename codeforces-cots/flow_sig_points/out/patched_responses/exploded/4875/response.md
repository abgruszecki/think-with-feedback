<think>
Okay, I need to solve this problem where given an encrypted string t, I have to find the original string s. Let's think about how the encryption process works so I can reverse it.

The encryption process for s is done step by step. For each character in s, starting from the first, the position decides whether to append or prepend. The steps are like this: the first character is just written down. The second is appended to the right. The third is prepended to the left. The fourth is appended again, and so on. So for each character s_i, if i is 1, it's added as the first character. Then for i>1, if the position is even (like 2,4,6), it's appended to the right. If it's odd (but greater than 1, like 3,5,7), it's prepended to the left.

Wait, the positions are 1-based. Let's see the example. For "techno", which is 6 letters. The steps are:
i=1: add 't' → "t"
i=2: append 'e' → "te"
i=3: prepend 'c' → "cte"
i=4: append 'h' → "cteh"
i=5: prepend 'n' → "ncteh"
i=6: append 'o' → "ncteho".

So the encryption builds the string by alternating between appending and prepending starting from the third character. The pattern is that for each i (starting from 1), the direction alternates. Let's see the direction for each i:
i=1: first character, no direction. Just starts the string.
i=2: append (even index)
i=3: prepend (odd index)
i=4: append (even)
i=5: prepend (odd)
i=6: append (even)
So for i >=2, even indices (i%2 ==0) → append. Odd indices (i%2 ==1) → prepend. Wait, but i starts from 1. Wait, the positions in the original s are 1-based. The second character (i=2) is appended. Third (i=3) is prepended. Fourth (i=4) appended. So for each i in s (starting from 1), the direction is: if i is even (i%2 ==0), then append (right), else if i is odd and >=3, prepend (left). Wait, but the first i is 1, which is the start. Then for i=2, it's even → append. i=3 is odd (3%2=1) → prepend. So the general rule for the encryption is:

For each character s_i (i starting at 1):
- if i is 1: add as the first character.
- if i is even: append to the right.
- if i is odd and i>1: prepend to the left.

So the encryption process builds the encrypted string by alternately adding characters to the left or right, starting from the third character (i=3) as prepend.

Now, given the encrypted string t, we need to reverse this process. So we have to find the original s such that when we apply the encryption steps, we get t.

The problem is to reverse the encryption steps. Let's think about how the original s was built into t, and how to reconstruct s from t.

Let's consider the example where t is "ncteho". The original s is "techno". The encryption steps build the encrypted string by adding each character in s in order, with the direction determined by their position.

To reverse this process, we need to find the order in which characters were added. Let's think about the encrypted string. Each step in the encryption adds a character either to the front or the back. So, the first character in the encrypted string is the last character added to the front. Wait, no. Let's see:

For example, in the encryption steps of "techno", the encrypted string after each step is:

t → te → cte → cteh → ncteh → ncteho.

The order of adding is s1, s2, s3, s4, s5, s6.

So s1 is added first (as 't'), then s2 is appended (te), then s3 is prepended (cte), then s4 is appended (cteh), then s5 is prepended (ncteh), then s6 is appended (ncteho).

So when decrypting, the order of operations is reversed. The original s has length n, and the encryption steps are s1, s2, ..., sn. So the encrypted string is built by these steps. To decrypt, we need to reverse these steps: starting from the encrypted string, and for each step (from the last character added back to the first), undo the operation.

But how to model this? Let's think: the encrypted string is built by a sequence of appends and prepends. The order of the steps is s1 added, then s2 appended, s3 prepended, s4 appended, etc. So the order of adding is s1, s2, s3, s4, s5, s6, etc. So when decrypting, the order in which the characters were added is s1, then s2, then s3, ... So to get s, we need to collect these characters in order.

But how to find the order in which the characters were added to the encrypted string. Let's imagine that each character in s is added in a certain position (left or right) in the encrypted string.

If we can reverse this process, starting from the encrypted string t and working backward, we can reconstruct the original s.

The approach is to reverse the steps of encryption. Let's think of the encrypted string as being built step by step. To reverse this, we need to step through the encryption steps in reverse order, removing the characters in reverse order of their addition.

For example, in the first example, the encrypted string is 'ncteho' of length 6. The original s is 6 characters long. The encryption steps are:

1. s1 added → length 1
2. s2 appended → length 2
3. s3 prepended → length 3
4. s4 appended → length4
5. s5 prepended → length5
6. s6 appended → length6

To reverse, we start with the encrypted string of length6. We need to find the order of removal to get each character.

The last step was appending s6. So the last character in t is s6. So the sixth character in s is the last character of the encrypted string. Wait, no. Let's see. When s6 is appended, it's added to the end. So in the encrypted string, the last character is s6. So in the first example, t is 'ncteho', so s6 is 'o'. So the sixth character in s is 'o'.

Then, before that step, the string was 'ncteh'. The fifth step was prepending s5 (which is 'n'). So the fifth character in s is 'n'.

So to reverse, for each step from n down to 1, we have to determine whether the character was added to the front or back, then extract it and add it to the original s in reverse order.

Wait, let's think. The original s has length m. The encryption steps are m steps. Each step adds a character. So the encrypted string is built in m steps. So to reverse the process, we can process the steps from the last step to the first. For each step i from m down to 1, we check whether in the encryption step i, the character was added to the front or the end of the current string. Then, the character in the encrypted string at that step's position (front or end) is the s_i. We remove that character and proceed.

But how to determine for each i whether it was added to front or end.

In encryption step i (1-based):

- i=1: added as the first character. So when reversing, for i=1, the current string is of length 1. So in the reverse process, when m is the original length, the steps start from m down to 1. For each i in the original s's position, the reverse step would be to determine whether the character was added to front or end, then take the character from the current encrypted string (after previous steps) and add it to the beginning of the original s (since we're working backwards).

Wait, maybe the correct approach is:

The encrypted string is built by the encryption steps. So to reverse the process, we can start with the encrypted string and undo each step in reverse order.

For example, for the encrypted string t of length m (the original s has length m). The steps in reverse order would be m, m-1, ..., 1.

For each step i (from m downto 1):

- For i=1: the encrypted string is just the first character. So in reverse, the original s's first character is the entire string.

- For i>1: we need to determine whether in the encryption step i, the character was added to the front or end.

Wait, but the step i in the encryption is when the original s's i-th character is added. So for i=2, it's appended; i=3 is prepended; i=4 appended, etc.

So for each i (original s's position), the direction is:

- For i=1: the character is added as the first. So when reversing, if m is 1, then s is the same as t.

- For i even: the direction is append (right). So during encryption, the i-th character is added to the right. So during decryption, when we undo step i, the character would have been the last character in the encrypted string at that step.

- For i odd and >1: the direction is prepend (left). So during encryption, the i-th character was added to the left. So during decryption, the character would be the first character in the encrypted string at that step.

But how does this work when we reverse the steps?

Let's think step by step. Let's say we have the encrypted string t of length m. The original s is of length m.

We need to reconstruct s by considering each step in reverse order (from step m down to 1). For each step i (from m downto 1):

- If i is 1: take the remaining string (which is length 1) and add to s as the first character.

- If i is even: during encryption, this step was appending to the right. So during decryption, the character added here is the last character of the current encrypted string. We remove it and prepend it to the s (since we are building s in reverse order of steps).

Wait, maybe not. Let's clarify:

Let me think of the decryption process. We need to build s by finding the order in which characters were added. But the original s is s1, s2, s3, ..., sm. So during encryption, s1 was first, then s2, s3, etc. To decrypt, we need to get these characters in order. However, when undoing the steps, the last step (m) would be s_m. So when decrypting, the first character we get is s_m, then s_{m-1}, etc. So to reconstruct s, we need to collect the characters in reverse order of the steps and then reverse them.

Wait, perhaps not. Let's see:

Suppose during encryption, the steps are s1, s2, s3, ..., sm. The encrypted string is built in this order. To reverse, we process each step from m downto 1. For each step i:

In encryption step i, the direction depends on i's parity. So for each i in m downto 1:

- if i is 1: the encrypted string is just s1. So in decryption, when i=1, the current string is s1, so we take it as the first character.

- if i is even: during encryption, the character was appended. So during decryption, this character is the last character of the current encrypted string. So we take it out (as s_i) and remove it from the encrypted string.

- if i is odd and >1: during encryption, the character was prepended. So during decryption, this character is the first character of the current encrypted string. So we take it out (as s_i) and remove it from the encrypted string.

But wait, the order of steps is reversed. Let's take the first example. The encrypted string is "ncteho" (length 6). The original s is "techno" (s1-t, s2-e, s3-c, s4-h, s5-n, s6-o).

In reverse steps, we start with the encrypted string and process steps 6,5,4,3,2,1.

Step 6: i=6 (even). So during encryption, this was an append. So during decryption, the s6 is the last character of the current encrypted string. So take 'o' as s6. Remove it from the string. Now the string is 'ncteh'.

Step 5: i=5 (odd). During encryption, this was a prepend. So s5 is the first character of the current string. Take 'n' as s5. Remove it. Now the string is 'cteh'.

Step4: i=4 (even). During encryption, this was an append. Take 'h' as s4. Remove it. String is 'cte'.

Step3: i=3 (odd). Take 'c' as s3. Remove, string becomes 'te'.

Step2: i=2 (even). Take 'e' as s2. Remove, string is 't'.

Step1: i=1. Take 't' as s1.

So the collected s is [o, n, h, c, e, t]. But we need to reverse this order to get s1 to s6. Because when processing in reverse steps (from 6 downto 1), we collect s6, s5, s4, s3, s2, s1. Then the original s is the reverse of this list. So [o, n, h, c, e, t] reversed is 'techno'.

Ah, so the correct approach is:

- Initialize a list to collect the characters of s in reverse order (from s_m downto s1).

- For each step i from m downto 1:

   - if i is even: take the last character of t (since during encryption, s_i was appended to the end).

   - if i is odd and i>1: take the first character of t (since during encryption, s_i was prepended to the front).

   - if i is 1: take the remaining character.

   - add this character to the list.

- After processing all steps, reverse the list to get the original s.

So, for example, in the first example, after processing steps 6 downto 1, the collected list is [o, n, h, c, e, t], which reversed gives 'techno'.

This makes sense. So the algorithm is:

1. Start with the encrypted string t.

2. For i from len(t) down to 1:

   a. If i is even: take the last character from the current string.

   b. If i is odd and i > 1: take the first character from the current string.

   c. If i is 1: take the remaining character.

3. Collect these characters in a list in the order of i from m downto 1 (so the list is [s_m, s_{m-1}, ..., s_1]).

4. Reverse this list to get the original s.

So the steps for decrypting are:

- For each i from m downto 1:

   if i is even → take from end

   if i is odd and i>1 → take from start

   collect these characters in a list, then reverse the list.

Now, how to implement this efficiently in Python.

The encrypted string can be represented as a deque for efficient popping from both ends. For each step i in m downto 1:

   if i is even: pop from the right.

   if i is odd and i>1: pop from the left.

   collect the popped character.

After collecting all characters in reverse order, reverse the list to get s.

So, for example, for the encrypted string "erfdcoeocs" (second test case), the output is "codeforces". Let's see:

Length is 10.

Processing steps from 10 downto 1.

i=10 (even) → pop last character: 's' → list becomes [s]

i=9 (odd>1) → pop first character: 'e' → list now starts from 'r' → add 'e' → list now [s,e]

i=8 (even) → pop last: 'c' → list [s,e,c]

i=7 (odd>1) → pop first: 'r' → list [s,e,c, r]

Wait, perhaps this example is better handled step by step.

But in code, using a deque allows popping from both ends.

So the plan is:

- Read the input string t.

- Initialize a deque with t's characters.

- Initialize a list to collect the characters in reverse order (s_m, s_{m-1}, ..., s_1).

- For i in range(len(t), 0, -1):

   if i == 1:

       char = deque.popleft() (since it's the only character left)

   elif i % 2 == 0:

       char = deque.pop()

   else:

       char = deque.popleft()

   append char to the list.

- Reverse the list to get s.

Wait, for i=1, since the deque has only one character left, we can just take it. But in the loop, when i=1, the code will check if i is even (no), then check if i is odd and >1 (no, i=1). So it will fall into the else clause for i=1. So maybe the code can be written as:

for i in range(m, 0, -1):

    if i % 2 == 0:

        c = d.pop()

    else:

        if i == 1:

            c = d.popleft()  # since there's only one left

        else:

            c = d.popleft()

    res.append(c)

But since when i is 1, the deque has only one element, and regardless of popping from left or right, it's the same. So perhaps the code can be written as:

for each i from m downto 1:

    if i is even: take from end.

    else: take from start (but only for i>1. Wait, when i is 1, it's taken from start as well.)

But in the encryption step, i=1 is the first character added. So during decryption, when i=1, the deque has only one character left, which is s1.

So for example, when m=1, the code will process i=1. It's odd, so take from start. The deque has one character. So c is that character. Then append to res. Then reverse res, which is [c], reversed becomes [c], so s is [c].

Which is correct.

So the code can be structured as:

Testing against sample input 1.

```python
from collections import deque


def main(input_stream, output_stream):
    t = input_stream.readline().rstrip("\n").strip()

    d = deque(t)

    res = []

    m = len(t)

    for i in range(m, 0, -1):

        if i % 2 == 0:

            # even, take from end

            c = d.pop()

        else:

            # odd, take from start (even for i=1)

            c = d.popleft()

        res.append(c)

    # reverse the res to get s in order

    s = ''.join(reversed(res))

    print(s, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
erfdcoeocs
""",
            "output": \
"""\
codeforces
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
from collections import deque


def main(input_stream, output_stream):
    t = input_stream.readline().rstrip("\n").strip()

    d = deque(t)

    res = []

    m = len(t)

    for i in range(m, 0, -1):

        if i % 2 == 0:

            # even, take from end

            c = d.pop()

        else:

            # odd, take from start (even for i=1)

            c = d.popleft()

        res.append(c)

    # reverse the res to get s in order

    s = ''.join(reversed(res))

    print(s, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
z
""",
            "output": \
"""\
z
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

So the code works for this case.

Thus, the code seems to handle all cases correctly. The key idea is to reverse the steps of the encryption by processing each character's position in reverse order and building the original string by reversing the collected characters.

Now, in terms of time and space constraints, the input size is up to 50 characters, so even with O(n) operations, it's acceptable. Using a deque allows popping from both ends in O(1) time. The code is efficient for the constraints given.
</think>

```python
from collections import deque

t = input().strip()
d = deque(t)
res = []
m = len(t)
for i in range(m, 0, -1):
    if i % 2 == 0:
        res.append(d.pop())
    else:
        res.append(d.popleft())
print(''.join(reversed(res)))
```
