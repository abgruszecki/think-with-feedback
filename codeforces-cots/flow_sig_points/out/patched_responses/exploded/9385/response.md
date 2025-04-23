<think>
Okay, so the problem is to count how many times we can form the word "Bulbasaur" from a given string. Each character can only be used once per Bulbasaur. The key here is that each Bulbasaur requires exactly one 'B', one 'u', two 'a's, one 's', one 'b', two 'r's, and one 'l'. Wait, wait, let me check the letters in "Bulbasaur". Let's spell it out: B, u, l, b, a, s, a, u, r. Wait, no, wait. Wait, the correct spelling is B U L B A S A U R? Wait no. Let me count each letter properly.

The word "Bulbasaur" is spelled as B, u, l, b, a, s, a, u, r. Let's count each character:

B: 1 (since the first letter is B)
u: 2 (positions 2 and 7)
l: 1
b: 1 (the fourth character is lowercase b)
a: 2 (positions 5 and 6)
s: 1
r: 1 (the last character)

Wait, wait, no. Let me write out the exact letters:

B (uppercase), u (lowercase), l (lowercase), b (lowercase?), a (lowercase), s (lowercase), a (lowercase), u (lowercase?), r (lowercase).

Wait, the problem statement says that the first letter must be uppercase and the rest lowercase. So the target word is "Bulbasaur" which is B followed by lowercase letters. Let's confirm:

The correct spelling of Bulbasaur as per the problem is: the first letter is 'B' uppercase, followed by 'u', 'l', 'b', 'a', 's', 'a', 'u', 'r' all lowercase. So each occurrence of the word requires exactly:

- 1 'B' (uppercase)
- 2 'u's (lowercase)
- 2 'a's (lowercase)
- 1 'l' (lowercase)
- 1 'b' (lowercase)
- 1 's' (lowercase)
- 2 'r's (lowercase)

Wait, wait. Let's recount the letters in "Bulbasaur". Let's spell the word:

B (1), u (1), l (1), b (1), a (1), s (1), a (1), u (1), r (1). Wait, that's 9 letters. So each occurrence requires:

B: 1 (uppercase)
u: 2 (lowercase) ? Because in the word 'Bulbasaur', how many u's are there? Let's check: B u l b a s a u r. So the letters are u (position 2) and u (position 7). So two u's. So in the target word, there are two u's. Similarly, a's are in positions 5 and 7? Wait, let's see:

Breaking down the letters:

B (1) - uppercase
u (1) - lowercase
l (1) - lowercase
b (1) - lowercase
a (1) - lowercase
s (1) - lowercase
a (1) - lowercase
u (1) - lowercase
r (1) - lowercase.

Wait no. Wait the word is "Bulbasaur". Let me write each character:

Positions:
0: B (uppercase)
1: u (lowercase)
2: l (lowercase)
3: b (lowercase)
4: a (lowercase)
5: s (lowercase)
6: a (lowercase)
7: u (lowercase)
8: r (lowercase).

Wait, so the total letters are:

B: 1
u: 2 (positions 1 and 7)
a: 2 (positions 4 and 6)
s: 1
l: 1
b: 1 (position 3, lowercase)
r: 1.

Wait, but wait, the word "Bulbasaur" has 9 letters. So the count is:

B:1
u:2
l:1
b:1
a:2
s:1
r:1.

So for each Bulbasaur, we need exactly those counts. So the approach is to count the frequency of each required character in the input string and then determine the maximum number of times we can form the word.

So first, we need to count how many of each required character are present in the input string.

Then, the maximum possible number of Bulbasaurs is the minimum between:

count('B') // 1,
count('u') // 2,
count('l') // 1,
count('b') // 1,
count('a') // 2,
count('s') //1,
count('r')//1.

Wait, no. Wait the required counts are:

B: 1 per Bulbasaur
u: 2 per
a: 2 per
others (l, b, s, r) are 1 each.

So for each required character, the maximum number is the minimum of the counts divided by their required number per Bulbasaur.

So the steps are:

1. Count the frequency of each character in the input string. Important: case-sensitive.

2. For each character needed in the target word, compute how many times it can contribute to forming a Bulbasaur. For example, the 'u' appears twice per Bulbasaur, so the number of Bulbasaurs possible from 'u's is (count of 'u's) // 2.

3. The overall maximum possible is the minimum of all these values across all required characters.

So the required counts are:

- 'B' → 1 per → count_B // 1
- 'u' → 2 → count_u // 2
- 'l' → 1 → count_l // 1
- 'b' → 1 → count_b // 1
- 'a' → 2 → count_a // 2
- 's' → 1 → count_s //1
- 'r' → 1 → count_r//1

Then the answer is the minimum of these seven values.

So, the plan is:

- Iterate through the input string, count each character (case-sensitive).

- Then for each of the required characters, compute the divisor (based on how many are needed per Bulbasaur).

- Take the minimum of those.

So, in code, first, we can create a dictionary to count the occurrences.

Then, for each of the required characters, check their counts.

So for example, if the input string is 'Bulbbasaur', which is the first example:

Input: Bulbbasaur → let's see:

Breaking it down:

Letters are:

B (uppercase)
u (lowercase)
l (lowercase)
b (lowercase)
b (lowercase)
a (lowercase)
s (lowercase)
a (lowercase)
u (lowercase)
r (lowercase).

Wait, wait, the input is 'Bulbbasaur'. Let's list each character:

B, u, l, b, b, a, s, a, u, r.

So counts:

B:1
u:2
l:1
b:3
a:2
s:1
r:1.

So for each required:

B:1 → 1//1 =1
u:2 →2//2=1
l:1 →1//1=1
b:3 →3//1=3
a:2 →2//2=1
s:1 →1//1=1
r:1 →1//1=1.

The minimum of all these is 1, which matches the first example's output.

Another example: input 'aBddulbasaurrgndgbualdBdsagaurrgndbb' (third example). Let's see:

But maybe in code, it's easier.

So the code steps:

Read the input string.

Count the frequency of each character.

Then, for each of the required characters, compute their counts divided by their required per Bulbasaur.

Take the minimum.

So, the required characters and their per-Bulbasaur count are:

{
    'B':1,
    'u':2,
    'l':1,
    'b':1,
    'a':2,
    's':1,
    'r':1
}

Wait, no. The target is "Bulbasaur", which is spelled with:

B (1, uppercase)
u (2, lowercase)
l (1, lowercase)
b (1, lowercase)
a (2, lowercase)
s (1, lowercase)
r (1, lowercase).

So in the code, we need to count:

count_B = number of 'B's in the input.

count_u = number of 'u's (lowercase).

count_l = number of 'l's lowercase.

count_b = number of 'b's lowercase.

count_a = number of 'a's lowercase.

count_s = number of 's's lowercase.

count_r = number of 'r's lowercase.

So, for example, in the third sample input:

The output is 2. Let's see why. The counts must be:

B: 2 (since two 'B's in the input? Let me check the input.

Third example input: aBddulbasaurrgndgbualdBdsagaurrgndbb.

Wait, perhaps in the input there are two 'B's. Let's see:

Looking for uppercase B's. The input is:

aBddulbasaurrgndgbualdBdsagaurrgndbb.

Breaking down the letters:

The letters are:

a (lowercase)
B (uppercase)
d, d, u, l, b, a, s, a, u, r, r, g, n, d, g, b, u, a, l, d, B (uppercase), d, s, a, g, a, u, r, r, g, n, d, b, b.

So uppercase B's: two occurrences.

Then the lowercase letters:

u: Let's count:

Looking at the input:

There's u in the 4th position (after B?), then u again, etc. Let me count:

But perhaps in code, the counts are as follows.

But the code would:

count the number of 'B's (uppercase), which is 2.

count the number of 'u's (lowercase) in the input.

In the third example, the output is 2. So the code would find that all required counts are at least as required for two Bulbasaurs.

So, for example:

Each Bulbasaur needs 2 u's. So for two Bulbasaurs, we need 4 u's. Are there at least 4 in the input?

Similarly, each requires 2 a's. So two * 2 =4 a's needed. And so on.

So the code would compute the required counts.

Thus, the code can be structured as follows.

In Python:

Read the input string.

Create a frequency dictionary (using collections.Counter).

Then for each required character, compute the available count divided by the required per Bulbasaur.

The minimum of these is the answer.

So code steps:

Testing against sample input 1.

```python
import collections


def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    count = collections.Counter(s)

    required = {
        'B': 1,
        'u': 2,
        'l': 1,
        'b': 1,
        'a': 2,
        's': 1,
        'r': 1
    }

    max_bulb = float('inf')

    for char in required:
        # Get the required count for this character per Bulbasaur
        req = required[char]
        # Get the available count in the input
        avail = count.get(char, 0)
        # How many times can we take req from avail?
        max_possible = avail // req
        if max_possible < max_bulb:
            max_bulb = max_possible

    print(max_bulb, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
F
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

Third example input gives 2, which implies that all required characters' counts allow for 2. For example:

B: 2 (from two uppercase B's) → 2/1=2.

u: 4? Because 4//2=2.

Similarly, a: 4 →4//2=2.

Other characters:

l: at least 2.

b: at least 2.

s: at least 2.

r: at least 2.

So all of them are 2 or more.

So the code returns 2.

Yes.

What about the second example input 'F'? The required characters all have count zero except 'F' which is not required. So the code will check 'B' first. count.get('B') returns 0. 0//1=0. So max_bulb is 0.

Yes.

So the code should work.

Now, considering the constraints. The input string can be up to 1e5 characters. The Counter will process it in O(n) time, which is acceptable. Then for each of the 7 required characters, we check their counts. So overall time is O(n) + O(1), which is acceptable for 1e5.

Space is O(1) for the Counter, as there are at most 52 possible characters (26 lowercase and 26 uppercase), but in practice, the code only uses counts for the required characters. Wait, no: the Counter will store all characters in the input. But for n=1e5, even if all characters are unique, the Counter would have O(n) entries, but in practice, in Python, it's manageable.

Wait, but the input can have up to 1e5 characters. The Counter will count all of them, which is O(n) time and O(k) space, where k is the number of distinct characters. Since each character is a letter (upper or lower), k can be up to 52. So the space is acceptable.

So the code should work efficiently.

Now, possible optimizations: since we only need the counts for 7 specific characters, perhaps we can avoid counting all characters. Instead, we can iterate through the string once and count only the required characters.

This would save memory and time, especially in cases where the input is very large but has many characters not part of the required set. For example, in a string of 1e5 characters, all of which are 'Z's. Then the code would count all 'Z's but they are irrelevant. However, in practice, the Counter is efficient, but perhaps for the problem's constraints, it's better to optimize.

So, modifying the code to count only the required characters.

The required characters are 'B', 'u', 'l', 'b', 'a', 's', 'r' (all lowercase except 'B'). So, in code:

Initialize a dictionary with keys as these seven characters, and counts initialized to zero. Then, iterate through each character in the input string. For each character, if it is in the required keys, increment the count.

This would reduce the number of characters being counted, thus saving memory and time.

Yes, that's a good optimization.

So code:

Third example input gives 2, which implies that all required characters' counts allow for 2. For example:

B: 2 (from two uppercase B's) → 2/1=2.

u: 4? Because 4//2=2.

Similarly, a: 4 →4//2=2.

Other characters:

l: at least 2.

b: at least 2.

s: at least 2.

r: at least 2.

So all of them are 2 or more.

So the code returns 2.

Yes.

What about the second example input 'F'? The required characters all have count zero except 'F' which is not required. So the code will check 'B' first. count.get('B') returns 0. 0//1=0. So max_bulb is 0.

Yes.

So the code should work.

Now, considering the constraints. The input string can be up to 1e5 characters. The Counter will process it in O(n) time, which is acceptable. Then for each of the 7 required characters, we check their counts. So overall time is O(n) + O(1), which is acceptable for 1e5.

Space is O(1) for the Counter, as there are at most 52 possible characters (26 lowercase and 26 uppercase), but in practice, the code only uses counts for the required characters. Wait, no: the Counter will store all characters in the input. But for n=1e5, even if all characters are unique, the Counter would have O(n) entries, but in practice, in Python, it's manageable.

Wait, but the input can have up to 1e5 characters. The Counter will count all of them, which is O(n) time and O(k) space, where k is the number of distinct characters. Since each character is a letter (upper or lower), k can be up to 52. So the space is acceptable.

So the code should work efficiently.

Now, possible optimizations: since we only need the counts for 7 specific characters, perhaps we can avoid counting all characters. Instead, we can iterate through the string once and count only the required characters.

This would save memory and time, especially in cases where the input is very large but has many characters not part of the required set. For example, in a string of 1e5 characters, all of which are 'Z's. Then the code would count all 'Z's but they are irrelevant. However, in practice, the Counter is efficient, but perhaps for the problem's constraints, it's better to optimize.

So, modifying the code to count only the required characters.

The required characters are 'B', 'u', 'l', 'b', 'a', 's', 'r' (all lowercase except 'B'). So, in code:

Initialize a dictionary with keys as these seven characters, and counts initialized to zero. Then, iterate through each character in the input string. For each character, if it is in the required keys, increment the count.

This would reduce the number of characters being counted, thus saving memory and time.

Yes, that's a good optimization.

So code:

s = input().strip()

required_counts = {
    'B': 0,
    'u': 0,
    'l': 0,
    'b': 0,
    'a': 0,
    's': 0,
    'r': 0
}

for c in s:
    if c in required_counts:
        required_counts[c] += 1

max_bulb = float('inf')

# Now, check each required character and their required per bulb
bulb_requirements = {
    'B': 1,
    'u': 2,
    'l': 1,
    'b': 1,
    'a': 2,
    's': 1,
    'r': 1
}

for char in bulb_requirements:
    req = bulb_requirements[char]
    avail = required_counts[char]
    max_possible = avail // req
    if max_possible < max_bulb:
        max_bulb = max_possible

print(max_bulb)

This approach iterates through the string once, and for each character, checks if it's one of the seven required. Since checking for membership in a small set (7 elements) is O(1) in Python (using a dictionary). So this approach would be more efficient, especially for large inputs with many irrelevant characters.

This is better because, for example, in a string with 1e5 characters, but none of them are in the required set, the code would do 1e5 checks (each O(1)), and then proceed. But in this case, the answer is zero. But in the worst case, where all characters are part of the required set, it's the same as before.

This approach uses a fixed-size dictionary (7 entries) which is better for memory.

Thus, this code should be more efficient, both in time and memory.

Testing this code against the examples:

First example input 'Bulbbasaur':

Loop through each character:

B: in required_counts → count['B'] =1
u: count['u']=1 → then another u? Let's see the string 'Bulbbasaur' is B u l b b a s a u r.

So:

Character breakdown:

B → count B →1
u → count u →1 → then later another u → count u becomes 2.
l → count l →1
b → count b →1, then another b → count becomes 2, then another? Let's see:

Original input: 'Bulbbasaur' → B, u, l, b, b, a, s, a, u, r.

So:

B: count becomes 1
u: first occurrence (count 1), then later another u (count 2)
l: 1
b: two times → count 2
a: two times → count 2
s: 1
r: 1.

So required_counts would be:

B:1
u:2
l:1
b:2
a:2
s:1
r:1.

Then bulb_requirements:

For each, calculate avail//req:

B:1//1=1

u:2//2=1

l:1//1=1

b:2//1=2

a:2//2=1

s:1//1=1

r:1//1=1.

Minimum is 1. Correct.

Third example input: the code would count the required characters correctly.

This approach should work.

Thus, this code is optimized for speed and memory, as it only counts the necessary characters and uses minimal data structures.
</think>

```python
s = input().strip()

required = {'B': 0, 'u': 0, 'l': 0, 'b': 0, 'a': 0, 's': 0, 'r': 0}

for c in s:
    if c in required:
        required[c] += 1

bulb_needs = {'B': 1, 'u': 2, 'l': 1, 'b': 1, 'a': 2, 's': 1, 'r': 1}
max_count = float('inf')

for char, need in bulb_needs.items():
    count = required[char] // need
    if count < max_count:
        max_count = count

print(max_count)
```
