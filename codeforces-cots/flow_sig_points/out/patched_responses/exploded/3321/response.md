<think>
Okay, let's tackle this problem. Hmm. The task is to check if the given text matches the verse pattern. Each line's syllables must equal the corresponding pi. 

First, I need to understand how to count the syllables in each line. The key is to process each word, split it into syllables, and sum the counts per line. But wait, words with no vowels are ignored. So, for each word in a line, if it has at least one vowel, we need to count how many syllables it contributes, otherwise zero.

Wait, how do syllables split? A syllable is a substring with exactly one vowel. So each syllable must contain exactly one vowel. The entire word is split into syllables such that all characters are used once. So the number of syllables in a word is equal to the number of vowels in it. Because each syllable must have exactly one vowel. So each vowel in the word contributes exactly one syllable. So for a word, the syllable count is the number of vowels it contains. But wait, what about consecutive vowels? For example, "aaa" would have 3 syllables. But according to the problem's example, the first sample includes "ch" which has no vowels, so it's ignored. Let's see the first sample's third line: "ch allenge". "ch" is ignored. "allenge" has vowels. Let's count the vowels in "allenge": a, e, e? Wait 'a' and 'e's. So 3 vowels. But the third line's pi is 3, which matches. Wait the sample input's third line's pattern is 3. So that makes sense. So each vowel in the word contributes a syllable. But wait, the problem says that the syllable must have exactly one vowel, but consonants can be any. So splitting the word into syllables requires each syllable to have exactly one vowel. So the number of syllables per word is equal to the number of vowels in the word. Because each vowel must be part of exactly one syllable. So for example, the word "mamma" has two vowels (a and a?), so two syllables. That's how the note explains it.

So the key insight is: for each word, count the number of vowels. The syllable count for the word is that number. But only if the word has at least one vowel. Otherwise, it contributes 0. So the total syllables per line is the sum of the syllable counts of each word in that line.

Wait, but the problem says that words with only consonants are ignored. So those words contribute 0. So, for each line, we need to split the line into words, process each word by counting the number of vowels (but only if the count is >=1, otherwise 0), sum all those, and check if it equals pi for that line.

So the steps are:

1. For each line in the text:
   a. Split into words.
   b. For each word:
      i. Count the number of vowels (a, e, i, o, u, y). Wait wait, wait! The problem says that 'y' is considered a vowel? Oh right, the note says the vowels are those letters, including y. So 'y' is considered a vowel here. So when checking each character, if it's a vowel (including y), count it. 
      ii. If the count is >=1, add the count to the line's total. Else, add 0.
   c. Compare the total to the corresponding pi. If any line's total is not equal to pi, output NO. Otherwise, if all lines match, output YES.

Wait, but what's the exact definition of a syllable? Let me re-read the problem statement. A syllable contains exactly one vowel. So each vowel in the word is part of exactly one syllable, and each syllable has exactly one vowel. Therefore, the number of syllables per word is exactly the number of vowels in that word. So for a word like 'y', which is a vowel, it has 1 syllable. For 'xyz', which has no vowels (assuming x and z are consonants and y is considered a vowel here), wait no. Wait in the problem statement, vowels are a, e, i, o, u, y. So 'y' is a vowel. So the word 'xyz' has 'y' as a vowel, so count is 1. So the syllables would be 'xy' and 'z'? Wait no. Wait the word is 'xyz'. The vowels are 'y'. So the syllable must have exactly one vowel. So the syllables could be 'x y z'? But each syllable must have exactly one vowel. So 'y' is a vowel. Then the entire word is split into a single syllable 'xyz' because it contains exactly one vowel. Or maybe split into 'x' 'yz' as two syllables, but that's not possible because each syllable must have exactly one vowel. Wait no. Because each syllable must have exactly one vowel, so for the word 'xyz' (assuming 'y' is a vowel), there's exactly one vowel. So the entire word is one syllable. So the syllable count is 1. So the word contributes 1.

So the key is, for each word, the syllable count is the number of vowels in the word, provided that the word has at least one vowel. So the process is to count the vowels in the word, and if the count is at least 1, add that count to the line's total. Otherwise, add 0.

So the plan is:

Loop over each line of text and the corresponding pi.

For each line:

sum = 0

split into words.

for each word in words:

count the number of vowels (including y). 

if count >= 1, add count to sum.

then check if sum equals pi.

If all lines match, output YES, else NO.

So the problem reduces to, for each word, count the number of vowels (including y), sum those counts per line, and compare with the pattern.

So the code steps are:

Read n.

Read p1, p2, ..., pn as a list.

Then read n lines of text.

For each line in the text:

split into words.

sum the vowels per word (if count >=1).

Check if sum equals the corresponding p.

If any line's sum doesn't match, output NO.

Else, output YES.

So now, how to implement this efficiently.

Constraints are n up to 100, lines up to 100 characters. So even a straightforward approach is acceptable.

But let's think about the possible edge cases.

Edge case 1: a word with all consonants. E.g., 'bcdfg' (no vowels). So it's ignored.

Edge case 2: a word with multiple vowels. E.g., 'aeiouy' → 6 syllables.

Edge case 3: a word with a mix of vowels and consonants, but exactly one vowel. Like 'hello' → has e and o? Wait 'h' is consonant, e is vowel, l is consonant, l is consonant, o is vowel. So two vowels. So syllable count is 2.

Wait, the problem's first example: the third line is "ch allenge". The word "ch" has no vowels (since 'h' is consonant, 'c' consonant). So contributes 0. The word "allenge" → let's see: a, l, l, e, n, g, e. So the vowels are a, e, e. So count is 3. So sum is 0 +3 =3. Which matches the pi of 3 in that line. So the third line's pi is 3. Which is why the sample output is YES.

So the code needs to process each word, count the vowels (including y) in it. If the count is zero, contributes 0. Else, the count.

So, the steps are:

Read n.

Read the second line as a list of integers p.

Then read n lines of text.

For each line, split into words.

For each word in the line:

count = number of vowels in the word (vowels are 'a', 'e', 'i', 'o', 'u', 'y').

if count > 0 → add count to line's total.

Then compare line's total with the p[i].

If all match, output YES else NO.

So in code:

Read n.

p = list(map(int, input().split()))

Then read n lines.

for each i in 0..n-1:

   line = input().strip()

   words = line.split()

   total = 0

   for word in words:

       vowels = sum(1 for c in word if c in {'a','e','i','o','u','y'})

       if vowels >0:

           total += vowels

   if total != p[i]:

       print("NO")

       exit()

print("YES")

Wait, but in the second sample input:

4

1 2 3 1

a → vowels: 1. sum is 1. pi is 1. okay.

bcdefghi → letters: b c d e f g h i → vowels are e and i. count 2. So sum is 2. pi is 2. okay.

jklmnopqrstu → check vowels: j k l m n o p q r s t u → o and u. count 2. So sum is 2. pi is 3 → no match. So output is NO. Which matches the sample.

So code correctly handles that.

Another edge case: word with all vowels. Like 'y' → count is 1.

So code should count it.

Another edge case: word like 'yyy' → 3 syllables.

So code works.

So the code seems correct.

Now, let's code this in Python.

But need to read n lines. For example, the third sample input:

4

13 11 15 15

The lines are:

to be or not to be that is the question

whether tis nobler in the mind to suffer

the slings and arrows of outrageous fortune

or to take arms against a sea of troubles

Each line's sum is the sum of vowels in each word, ignoring words with zero vowels.

For example, first line: each word:

to → t (consonant?), o → vowels: 1.

be: e →1.

or: o →1.

not: o →1.

to →1.

be →1.

that: a →1.

is: i →1.

the: e →1.

question: u, e, i →3?

So sum of all these words' vowel counts: 1+1+1+1+1+1+1+1+1+3 → 11? Wait but the pi for first line is 13. Wait maybe I'm miscalculating.

Wait sample 3's output is YES. So perhaps the code correctly counts. So the code is correct.

In any case, the code is straightforward. So the code should handle all cases.

Now, code:

Read n.

Then read the second line as list p.

Then read n lines of text.

Loop over each line and p_i.

In code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    p = list(map(int, input_stream.readline().rstrip("\n").split()))
    if len(p) != n:
        print("NO", file=output_stream)
        return

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    for i in range(n):
        line = input_stream.readline().rstrip("\n").strip()
        words = line.split()
        total = 0
        for word in words:
            cnt = 0
            for c in word:
                if c in vowels:
                    cnt +=1
            if cnt >0:
                total += cnt
        if total != p[i]:
            print("NO", file=output_stream)
            return
    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 2 3 1
a
bcdefghi
jklmnopqrstu
vwxyz
""",
            "output": \
"""\
NO
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
    p = list(map(int, input_stream.readline().rstrip("\n").split()))
    if len(p) != n:
        print("NO", file=output_stream)
        return

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    for i in range(n):
        line = input_stream.readline().rstrip("\n").strip()
        words = line.split()
        total = 0
        for word in words:
            cnt = 0
            for c in word:
                if c in vowels:
                    cnt +=1
            if cnt >0:
                total += cnt
        if total != p[i]:
            print("NO", file=output_stream)
            return
    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
13 11 15 15
to be or not to be that is the question
whether tis nobler in the mind to suffer
the slings and arrows of outrageous fortune
or to take arms against a sea of troubles
""",
            "output": \
"""\
YES
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

Third sample:

4 lines. The code correctly sums all the vowels per line, leading to the pi values. Since output is YES, the code works.

So this should handle all cases.
</think>

```python
n = int(input())
p = list(map(int, input().split()))
if len(p) != n:
    print("NO")
    exit()

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for i in range(n):
    line = input().strip()
    words = line.split()
    total = 0
    for word in words:
        cnt = sum(1 for c in word if c in vowels)
        if cnt > 0:
            total += cnt
    if total != p[i]:
        print("NO")
        exit()
print("YES")
```
