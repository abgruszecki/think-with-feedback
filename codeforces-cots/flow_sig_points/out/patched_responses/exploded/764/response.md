<think>
Okay, let's see. The problem is about converting text from one keyboard layout to another. So, the idea is that when a person types on the first layout, but the intended layout is the second, we need to find out what the resulting text would be.

Hmm. Let's break it down. The first two input lines are the two keyboard layouts. The third line is the text to convert. The output should be the text as if it was typed using the second layout, but the physical keys pressed are the same as in the first.

Wait, right. So for each character in the input text, if it's a letter (lower or uppercase), we need to find where it is in the first layout, then take the corresponding character from the second layout. Non-letters stay the same.

So, for example, in the first sample input, the first layout is 'qwerty...' and the second is 'veamhjs...'. So, the first character in the first layout is 'q', which corresponds to the first character in the second layout, 'v'. So any 'q' in the input (case-insensitive?) would be mapped to 'v', but preserving the case. Wait, no. The problem says that the capitalization should remain the same. So if the input is 'Q', then we look up where 'q' is in the first layout, take the corresponding character from the second layout, then apply the same case. For example, if the original is lowercase, the output is lowercase. If uppercase, the output is uppercase.

So steps:

1. Create a mapping from each character in the first layout to the second. But only for letters. So, for each lowercase letter in the first layout, map to the corresponding lowercase in the second. Then, when processing the input text, if the character is a letter, check if it's lowercase or uppercase. Find the corresponding lowercase in the first layout, get the mapped character from the second layout, then adjust the case to match the original.

Wait, the problem states that the input strings for the layouts are lowercase. So the first layout is all lowercase letters. So, to handle the case in the input text, for example, if the input text has a 'Q', we first convert it to lowercase to find its position in the first layout, then take the corresponding character from the second layout and uppercase it.

So the plan is:

- Create a dictionary that maps each character in the first layout to the corresponding character in the second. Since the layouts are given as lowercase, the keys in the dictionary will be the lowercase letters of the first layout, and the values are the lowercase letters of the second.

Then, for each character in the input text:

- If it's a lowercase letter: look it up in the dictionary, replace with the corresponding value.
- If it's an uppercase letter: convert to lowercase, look up in the dictionary, then uppercase the result.
- If it's a digit or other character (but problem says input is letters and digits), leave it as is.

So, the steps are:

Read first and second layout strings.

Build a mapping from first_layout[i] to second_layout[i] for each i from 0 to 25.

Then process each character in s:

For a lowercase c in s: output mapping.get(c, c) ? Well, but first_layout has all 26 letters, so every lowercase letter is present. So for letters, the mapping is always possible. For uppercase letters: convert to lowercase, map, then uppercase. For digits, leave as is.

Wait, the third line of input can have digits, but the problem says they should remain the same. So digits are not part of the keyboard layouts, so they are not changed.

So the code steps:

Read first_line, second_line, s.

Create a dictionary, maybe called mapping, where for each i, first_line[i] is mapped to second_line[i].

Then, for each character in s:

if it's a lowercase letter: replace with mapping[char]

if it's uppercase: convert to lowercase, find mapping, then uppercase the result.

else: leave as is.

So the code can be written as follows.

Now, for the implementation.

But how to handle the case conversion?

Let's see. Let's take an example. For the first sample input:

First layout is 'qwertyuiopasdfghjklzxcvbnm'

Second layout is 'veamhjsgqocnrbfxdtwkylupzi'

The input text is 'TwccpQZAvb2017'

So 'T' is uppercase. So we convert to 't', look up in first layout. What's the position of 't' in first_layout?

Looking at the first layout string:

Let's index from 0. Let's see:

First layout is 'qwertyuiopasdfghjklzxcvbnm'

Wait, that's 26 letters. Let's see:

q w e r t y u i o p a s d f g h j k l z x c v b n m

Wait, maybe the order is:

qwertyuiop (the first row of a QWERTY keyboard?), then asdfghjkl (second row?), then zxcvbnm (third row). So that's 10 + 9 + 7 = 26 letters. But the exact order may not matter, as the problem gives the two strings as the layouts.

In the first sample input, the first layout's first character is 'q', second is 'w', etc.

In the sample input, the text is 'TwccpQZAvb2017'.

Processing each character:

Take 'T' → lowercase 't' → find in first layout. Let's find the index of 't' in first_layout. Let's look at the first layout string. The first layout's first 5 letters are q, w, e, r, t. So index 4. Then the second layout's index 4 is 'm' (since second layout is 'veamhjsgqocnrbfxdtwkylupzi').

Wait, let's check:

Second layout is given as: 'veamhjsgqocnrbfxdtwkylupzi'

Let me count the characters:

0: v

1: e

2: a

3: m

4: h

5: j

6: s

7: g

8: q

9: o

10: c

11: n

12: r

13: b

14: f

15: x

16: d

17: t

18: w

19: k

20: y

21: l

22: u

23: p

24: z

25: i

So the first_layout is 'qwertyuiopasdfghjklzxcvbnm' (the original layout).

Looking for 't' in first_layout:

Looking at the first layout string:

Indices:

0: q

1: w

2: e

3: r

4: t → so index 4. So the corresponding second layout character is index 4, which is 'h'.

So 't' in the first layout maps to 'h' in the second. So the uppercase 'T' becomes 'H'.

In the sample input, the output for 'T' is 'H' as part of 'HelloVKCup2017'.

So that's correct.

So the code would take each character:

For 'T' → lowercase 't' → mapped to 'h' → uppercase to 'H'.

Another example: 'w' in first layout is at index 1. The second layout at index 1 is 'e' → so 'w' becomes 'e'.

So in the input text, 'w' would be replaced with 'e'.

So the code seems correct.

Now, implementing this.

In Python, we can create a dictionary that maps each character in the first layout to the second.

So:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    first = input_stream.readline().rstrip("\n").strip()
    second = input_stream.readline().rstrip("\n").strip()
    s = input_stream.readline().rstrip("\n").strip()

    mapping = {}
    for f, se in zip(first, second):
        mapping[f] = se

    result = []
    for c in s:
        if c.islower():
            result.append(mapping[c])
        elif c.isupper():
            lower_c = c.lower()
            mapped = mapping[lower_c]
            result.append(mapped.upper())
        else:
            result.append(c)

    print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
mnbvcxzlkjhgfdsapoiuytrewq
asdfghjklqwertyuiopzxcvbnm
7abaCABAABAcaba7
""",
            "output": \
"""\
7uduGUDUUDUgudu7
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

So 'c' is in the third part. The third part starts at index 19 (z), 20 (x), 21 (c). So 'c' is at index 21. So in the second layout, index 21 is 'l' (from the second layout given in sample 1: veamhjsgqocnrbfxdtwkylupzi. Let's index that:

0: v

1: e

2: a

3: m

4: h

5: j

6: s

7: g

8: q

9: o

10: c

11: n

12: r

13: b

14: f

15: x

16: d

17: t

18: w

19: k

20: y

21: l

22: u

23: p

24: z

25: i

So index 21 is 'l'. So the 'c' in the first layout (index 21) maps to 'l' in the second.

Wait, but first layout's 'c' is at position 21. Then the second layout's position 21 is 'l'?

Wait in the first sample, first layout is 'qwertyuiopasdfghjklzxcvbnm' → let's list all the letters:

Indices 0-9: q w e r t y u i o p

Indices 10-18: a s d f g h j k l

Indices 19-25: z x c v b n m

So index 0: q, 1: w, 2: e, 3: r, 4: t, 5: y, 6: u, 7: i, 8: o, 9: p, 10: a, 11: s, 12: d, 13: f, 14: g, 15: h, 16: j, 17: k, 18: l, 19: z, 20: x, 21: c, 22: v, 23: b, 24: n, 25: m.

Wait, that's 26 letters. So for 'c', in the first layout, it's at index 21.

In the second layout, index 21 is 'l' (as per the earlier list). So 'c' in the first maps to 'l' in the second. So in the input text, the third character is 'c' → becomes 'l' → which would make the first part of the output 'H' 'e' 'l' 'l' 'o' etc.

Yes. So the code works.

Another example: the 'Q' in the input. Q is uppercase. Convert to lowercase 'q'. In the first layout, 'q' is at index 0. The second layout's index 0 is 'v'. So uppercase 'V' → which is part of 'VKCup' in the output.

Yes.

So the code seems to handle all cases correctly.

Now, checking the second sample input.

Sample input 2:

mnbvcxzlkjhgfdsapoiuytrewq

asdfghjklqwertyuiopzxcvbnm

7abaCABAABAcaba7

The first layout is 'mnbvcxzlkjhgfdsapoiuytrewq'

Second layout is 'asdfghjklqwertyuiopzxcvbnm'

So let's see. The first layout's first character is 'm', second is 'n', etc.

In the input text, the first character is '7', which is left as is.

The next characters are 'aba' → lowercase. So for 'a' in the first layout: find its index, then get the second layout's character.

First layout's 'a' is at position ... let's look.

First layout: m n b v c x z l k j h g f d s a p o i u y t r e w q.

Wait, wait, maybe split the first_layout into parts. Let's list all characters:

Indices 0-25 of first_layout:

0: m

1: n

2: b

3: v

4: c

5: x

6: z

7: l

8: k

9: j

10: h

11: g

12: f

13: d

14: s

15: a

16: p

17: o

18: i

19: u

20: y

21: t

22: r

23: e

24: w

25: q

So 'a' is at index 15. So the second layout's index 15 is 'd' (since second_layout is 'asdfghjklqwertyuiopzxcvbnm').

Second_layout's indexes:

0: a

1: s

2: d

3: f

4: g

5: h

6: j

7: k

8: l

9: q

10: w

11: e

12: r

13: t

14: y

15: u

16: i

17: o

18: p

19: z

20: x

21: c

22: v

23: b

24: n

25: m

So index 15 of second_layout is 'u'.

Wait, no. Wait second_layout is 'asdfghjklqwertyuiopzxcvbnm'.

Breaking it down:

a s d f g h j k l → indexes 0-8.

q w e r t y → indexes 9-14.

u i o p → indexes 15-18.

z x c v b n m → indexes 19-25.

So index 15 is 'u'.

So the first layout's 'a' (index 15) maps to 'u' in the second layout.

So the input 'a' in the text would become 'u'.

Similarly, 'C' in the input is uppercase. Convert to lowercase 'c'. In first layout, 'c' is at index4. Second layout's index4 is 'g'. So uppercase 'C' becomes 'G'.

So the input '7abaCABAABAcaba7' → after processing:

Each 'a' becomes 'u', 'b' becomes ... let's see. 'b' in first layout is index2. Second layout's index2 is 'd'. So 'b' → 'd'.

But let's see:

Original input: '7abaCABAABAcaba7'

Breaking down:

For each character:

7 → remains.

a → lowercase → 'a' maps to 'u'.

b → index2 in first, maps to 'd'.

a → 'u'

C → lowercase 'c' → first layout index4 → second layout index4 is 'g' → uppercase 'G'.

A → lowercase 'a' → maps to 'u' → uppercase 'U'.

B → lowercase 'b' → maps to 'd' → uppercase 'D'.

A → 'U'

A → 'U'

B → 'D'

A → 'U'

c → index4 → 'g' lowercase.

a → 'u'

b → 'd'

a → 'u'

7 → remains.

So putting it all together:

7 u d u G U D U U D U g u d u 7 → which is '7uduGUDUUDUgudu7' which matches the sample output.

Yes.

So the code works.

Now, the code is correct. Now, considering efficiency. The maximum input for s is 1000 characters, which is trivial. So even a O(n) approach is acceptable. The code is O(n) where n is the length of s, which is 1000. So no problem with time constraints.

Memory-wise, the mapping is a dictionary with 26 entries. So negligible. So the code is optimal.

So the code as written should be correct.
</think>

```python
first = input().strip()
second = input().strip()
s = input().strip()

mapping = {f: s for f, s in zip(first, second)}

result = []
for char in s:
    if char.islower():
        result.append(mapping[char])
    elif char.isupper():
        lower_char = char.lower()
        result.append(mapping[lower_char].upper())
    else:
        result.append(char)

print(''.join(result))
```
