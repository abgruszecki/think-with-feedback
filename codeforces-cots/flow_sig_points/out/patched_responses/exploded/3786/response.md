<think>
Okay, so I need to solve this problem where I have to determine if a given string can be split into two non-empty subsequences such that each of them is adorable. Hmm, let's start by understanding what an adorable string is. 

The problem says a string is adorable if its characters can be rearranged into two consecutive groups of the same character, but the two groups must be different. Wait, so for example, "aaab" is adorable because it's already in a form like aaab (which is three a's followed by a b). But "aaaa" wouldn't work because splitting into two groups would require two different characters, right? Wait, no. Wait, the two groups must be of different characters. So like, the rearranged string must have all of one character first, then all of another. And the two characters must be different. So the entire string must consist of exactly two distinct characters, and when rearranged, they form two consecutive blocks.

Wait, for example, "aabba" is adorable? Let's see. If we rearrange it as "aaa" followed by "bb", which is aaaab. Then yes, that's two groups. So the original string must have exactly two distinct characters, and when sorted, it's grouped into those two. So the adorable string's character counts must be such that all of one character are together, then all of the other. So the structure is like x^a y^b where x and y are distinct.

So, the adorable string must satisfy that when all occurrences of one character are grouped first, then all of another. So the total count of characters must be exactly two different types, and the counts can be anything as long as they are non-zero for both.

Wait, no. Wait, the problem says "two consequent groups of equal symbols". So the entire string is made of two runs of the same character each. Wait, no. Wait, the problem says two consecutive groups. So the entire string is made of two parts: all the same character in the first part, then all the same (different) character in the second part. So for example, "aaabbb" is adorable. But "aaabbb" can be split into two parts, but in the problem statement, the example given was "ababa" transformed to "aaabb". So the rearranged string is of the form aa...a followed by bb...b. So the original string can have any arrangement, but after rearrangement, it's two consecutive groups of two distinct characters.

So, the key is that the string, after rearrangement, must consist of exactly two different characters, each forming a single contiguous block. So the original string must have exactly two distinct characters, and when rearranged as two groups, each group is a different character. So, the counts of the two characters can be anything as long as both are present.

Wait, but the problem says "different groups must contain different symbols". So the two groups must be of different characters. So the entire string, when rearranged, must be of the form x^m y^n, where x != y, m and n are >=1.

So the original string must have exactly two distinct characters, and all their occurrences can be grouped into two runs.

So, for a string to be adorable, the count of distinct characters in it must be exactly two, and when sorted, the characters form two groups.

Wait, but if the string has exactly two distinct characters, any rearrangement would allow splitting into two groups. For example, "ababa" has two characters. So rearranged as "aaabbb" would be okay. So the first condition is that the string must have exactly two distinct characters, and their counts can be anything. Because you can rearrange them into two groups.

Wait, no. Wait, if a string has exactly two distinct characters, then no matter what their counts are, you can arrange them into two consecutive groups, each of a single character. So that string is adorable.

Wait, that's the case. For example, the string "aabb" is already adorable. But "abab" can be rearranged into "aaabbb", which is two groups. So, any string with exactly two distinct characters can be made into an adorable string by rearrangement. So the condition for a string to be adorable is that it has exactly two distinct characters, and each occurs at least once.

Wait, but what if the string has three distinct characters? Then it's impossible. Because after rearrangement, you can't form two consecutive groups of the same characters (there would be three different ones). So the conclusion is that a string is adorable if and only if it contains exactly two distinct characters, each occurring at least once.

Wait, but let me check the examples.

First example input is "ababa". The output is Yes. Because when split into two parts, each part must be adorable. Wait, no. The problem requires that the original string is split into two subsequences (so, each character is in one or the other, but not both), and each subsequence is adorable.

Wait, the problem says: the string can be split into two non-empty subsequences such that the two subsequences are adorable.

So each subsequence must be adorable. So for each subsequence, the characters in it must consist of exactly two distinct characters (wait, no. Wait, each subsequence is a string that can be rearranged into two groups of same characters. So each subsequence must have exactly two distinct characters, each at least once.

Wait, no. Wait, the subsequence's letters can be rearranged into two consecutive groups. So the subsequence can have, for example, two a's and one b. Then when rearranged as aab, that's two a's followed by a b. So that's acceptable. So the subsequence must have exactly two distinct characters, each appearing at least once.

So each subsequence must have exactly two distinct characters. Wait, no. Wait, the rearranged string must have two consecutive groups. So the entire subsequence can be of a single character. Wait, no. Because the two groups need to be different. For example, if the subsequence is "aaa", then you can't split it into two groups of different symbols. So in that case, it's not adorable.

Ah, right. The definition says that the two groups must be different. So each subsequence must consist of exactly two distinct characters. So, for a subsequence to be adorable, it must have exactly two distinct characters, each occurring at least once, and when rearranged, form two consecutive groups. So the subsequence can be any string that has exactly two distinct characters, each occurring at least once.

Therefore, the problem reduces to: can we split the original string into two non-empty subsets, such that each subset has exactly two distinct characters, each subset's characters are exactly two distinct types, and each has at least one of each.

Wait, but perhaps the two subsets can share characters? Like, the first subset has a and b, and the second subset has a and c. So the original string must have at least two characters, but how?

Wait, the original string's problem is to split into two subsequences. Each subsequence must have exactly two distinct characters. So the original string must have at least two distinct characters. Because each subsequence must have two. But perhaps the original can have more than two.

For example, consider the input "abc". Then, can we split it into two subsequences? Let's see. Suppose the first subsequence is "ab" (two distinct), and the second is "c". But the second has only one distinct character. So it's not possible. So "abc" can't be split. So the answer is No.

So the problem is to split the original string into two parts, each part has exactly two distinct characters. Wait, no. Because each part must be adorable. Which requires that each part has exactly two distinct characters.

So the original string's set of characters must be such that when split into two parts, each part has exactly two distinct characters. So the original string can have up to four distinct characters (each part contributes two, and they can be different). But perhaps it's possible for the original to have three or four characters.

Wait, but how can each part have exactly two distinct characters? Let's think. For example, the original string has three distinct characters: a, b, c. How can we split it into two parts?

Part1 could be a and b, part2 could be a and c. But the original string must have all three characters. So, for example, the string is "aabbcc". Then split part1 as "aab" (a and b), part2 as "bcc" (b and c). Then each part has two distinct characters, so each is adorable. Then the answer would be Yes.

But wait, the problem states that each subsequence must be non-empty. So the original string must be split into two parts, each with at least one character, and each part's characters are exactly two distinct.

So how do we approach this problem?

We need to find a way to split the original string's characters into two subsets such that each subset has exactly two distinct characters. But how?

Alternative approach: For each possible pair of subsets (s1, s2) of the original string, check if each subset has exactly two distinct characters and is non-empty. However, this is impossible for large n (since n can be up to 1e5). So we need an efficient way to check possible splits.

So, the problem reduces to:

Find two subsets S1 and S2 of the characters in s, such that:

1. S1 and S2 are non-empty.

2. S1 ∪ S2 = all characters in s.

3. The characters in S1 have exactly two distinct types.

4. The characters in S2 have exactly two distinct types.

But how to model this.

Alternatively, perhaps the original string must have:

Either:

a) The original string has exactly two distinct characters, and each subset can be split into parts with those two. But then each subset would have exactly two characters, so that's possible. For example, the first example: "ababa". The entire string has a and b. So split into any two subsets. Then each subset has a and b, so each is adorable. So the answer is Yes.

But wait, the problem allows splitting into any two non-empty subsets as long as each has exactly two distinct characters. So in this case, any split would work. So the answer is Yes. But how does the first example split? The example says that "ababa" can be split into two parts. So perhaps when the original has two characters, the answer is always Yes, as long as each subset is non-empty and has at least two characters. Wait, but each subset must have both characters. For example, if the original is "aabb", and we split into "aa" and "bb", then each subset has only one character. So that's invalid. So each subset must have both a and b.

So, in order for a split to be possible when the original has two distinct characters, each subset must contain both characters. So each subset must have at least one a and at least one b.

So, in the original string, the count of a must be at least 2, and the count of b must be at least 2. Because each subset needs at least one a and one b.

Wait, no. Because for example, if the original string is "ab", which has one a and one b. Then splitting into two subsets: the first subset is "a", the second is "b". Each has one character, which is not allowed. So that's invalid. So the answer would be No.

But if the original string has two distinct characters and each occurs at least twice, then splitting into two subsets each containing at least one a and one b is possible. For example, "aabb". Split into "aaab" (wait, that's not possible. Wait, perhaps split into "ab" and "ab". Each has a and b, so each is adorable. So that's possible.

Wait, but the original is "aabb" (a:2, b:2). Split into first subset as first a and first b (counts a=1, b=1), second subset as the remaining a and b. Each subset has a and b. So each is adorable. So the answer is Yes.

So for a string with two distinct characters, the answer is Yes if and only if each character occurs at least two times. Because each subset must contain at least one of each character.

Wait, but that's not necessarily the case. Suppose the original string has a counts of 3 and b counts of 1. Then splitting into two subsets may not be possible. For example:

Original string is "aaab". The counts are a:3, b:1.

If we split into two subsets, each must have both a and b.

But the second subset must have at least one b, but there is only one b. So the second subset can't have a b. So the split is impossible.

So in this case, even though the original string has two distinct characters, the answer is No.

So the problem is more complex than that.

So the approach for the case where the original has two distinct characters:

Each subset must have at least one of each character.

But how?

So for the original to be split into two parts where each part has at least one of each character.

So the counts of each character must be >= 2? No. Because suppose a has 3, b has 2.

Then one subset could have a=2 and b=1, the other subset has a=1 and b=1. So each has at least one of each. So that's possible.

But if a has 1 and b has 1, then each subset can't have both. So the answer is No.

So the condition when the original has two distinct characters is that each character occurs at least once in both subsets. Which implies that the count of each character in the original is >= 2? No. Wait, for example, original a has 2, b has 2. Then each subset can have 1 a and 1 b. So possible.

If original a has 3, b has 2: then subset1 could have a=2, b=1, subset2 a=1, b=1. So possible.

So the actual condition is that the count of each character in the original is >= 2? Or that each character has count >=1 (since you can split them into the subsets). Wait, no. Because if a character has count 1 in the original, then you can't split into two subsets each having at least one of that character.

So the necessary conditions for the original to have exactly two distinct characters are:

- Each of the two characters must appear at least two times.

Wait, no. Wait, the original has two characters, a and b. Suppose a has count 1 and b has count 3. Then it's impossible to split into two subsets. Because the a must appear in both subsets, but it's only present once. So the answer would be No.

So when the original has exactly two distinct characters, the answer is Yes if and only if both characters have counts >=2.

Wait, but the example given in the problem:

Sample input 2: zzcxx.

The output is Yes.

Looking at the input: zzcxx.

The characters are z, z, c, x, x. So the original string has three distinct characters: z, c, x.

So in this case, how to split into two parts, each with exactly two distinct characters.

For example, split into subsequences "zc" (z and c) and "zxx" (z and x). Each has exactly two distinct characters. So each is adorable. So the answer is Yes.

So this shows that the original can have three distinct characters, but split into two subsets such that each has two distinct.

So, the approach must also consider cases where the original has more than two distinct characters.

So, the possible scenarios where the answer is Yes are:

1. The original has exactly two distinct characters, each with count >= 2.

OR

2. The original has three distinct characters, and there exists a way to split the characters such that each subset has exactly two distinct.

OR

3. The original has four distinct characters, and each subset has exactly two distinct, and there's some way to split the characters into two groups of two each.

But how to check these possibilities.

So, to model this, perhaps the steps are:

- Check if the original can be split into two subsets, each having exactly two distinct characters.

But how?

An alternative approach is:

For the original string, collect the frequency of each character.

If the total number of distinct characters is more than 4, then it's impossible. Because each subset can contribute two, but 2*2=4. So for example, if the original has 5 distinct characters, then each subset would need two, but that's 4 total, which is impossible.

So first, if the original has more than 4 distinct characters, the answer is No.

Else:

Check possible cases:

Case 1: original has exactly two distinct characters. Then, each character's count must be >=2.

Case 2: original has exactly three distinct characters.

In this case, the two subsets must each have two distinct. So, the three distinct characters must be partitioned into two groups. For example, one subset has two of the three, and the other subset has two (possibly overlapping).

Wait, for three distinct characters (a, b, c), one subset could have a and b, the other a and c. But that would require that the original has a, b, c. But how to split the characters such that:

In the first subset, the characters are a and b (so the subset must contain at least one a and one b).

In the second subset, the characters are a and c (so must contain at least one a and one c).

So the original must have at least two a's (since both subsets need a), and at least one b and c.

So, if the original has a's count >=2, then possible.

So for the case of three distinct characters, the answer is Yes if there exists a way to assign the three characters into two subsets such that:

- Each subset has exactly two distinct characters.

This can be done if one of the characters is present in both subsets. For example, for the three characters a, b, c:

subset1 has a and b.

subset2 has a and c.

In this case, the original must have at least two a's (since subset1 and subset2 each have at least one a), and at least one b and c.

So, in this scenario, the answer is Yes if the original contains at least two of one of the characters (say a), and at least one of the other two (b and c).

So, for three distinct characters, possible scenarios where the answer is Yes:

Find a character that appears at least two times, and the other two characters appear at least once each.

For example, the sample input 2 is "zzcxx". The characters are z (2), c (1), x (2). So the three distinct are z, c, x.

Looking for a character that appears at least twice: z (2), x (2).

Take z as the common character. Then subset1 could be z and c (needs z >=1 and c >=1). subset2 is z and x (needs z >=1 and x >=1). The original has z:2. So split into z=1 and z=1. Then subset1 has 1 z and 1 c, subset2 has 1 z and 2 x. So possible. So answer is Yes.

Another example: if the original is aabc (a:2, b:1, c:1). Then, the answer is Yes. Split into subsets with a and b (needs a >=1 and b >=1), and a and c (a >=1, c >=1). But the original a is 2. So possible.

So, for three distinct characters, the answer is Yes if at least one of the characters occurs at least twice, and the other two occur at least once.

So, the condition for three distinct characters is:

There exists a character x such that count[x] >=2, and the counts of the other two characters are >=1.

Case 3: original has four distinct characters.

In this case, the two subsets must each have exactly two distinct characters. So the four characters must be partitioned into two pairs. For example, subset1 has a and b, subset2 has c and d. So the original must have all four, and each subset must have two distinct.

In this case, each subset must have at least one occurrence of each of its two characters.

So, for four distinct characters, the answer is Yes if the original string can be split into two pairs of characters, where each pair has at least one occurrence.

For example, if the original has a, b, c, d each appearing once. Then, it's possible to split into a and b (but each needs to have at least one occurrence, so subset1 would have a and b, subset2 has c and d. But in the original, each of a, b, c, d appears once. So subset1 would take a and b (so each of their counts in the original is 1, but how? If the original is "abcd", then split into "ab" and "cd". Then subset1 is ab (two distinct), subset2 is cd (two distinct). So each is adorable. So answer is Yes.

So, for four distinct characters, the answer is Yes if each character occurs at least once. Because you can split them into two pairs, each with two distinct characters, each appearing once.

But wait, the original must have four distinct characters, each with count >=1. Then, split into two subsets where each subset takes exactly two of the characters. For example, subset1 has a and b (each count 1 in the original), subset2 has c and d (each count 1). So each subset is adorable. So the answer is Yes.

So, for four distinct characters, the answer is Yes if all four are present (since each has count >=1), and you can split them into two pairs.

Wait, but the four distinct characters must be present. So if the original has four distinct characters, each with count >=1, then the answer is Yes.

Wait, but the example would be "abcd". Split into "ab" and "cd". Each has two distinct characters. So Yes.

So for four distinct characters, the answer is always Yes.

So, putting it all together:

The answer is Yes if:

Either:

1. The original has exactly two distinct characters, and both counts are >=2.

OR

2. The original has exactly three distinct characters, and there exists at least one character with count >=2, and the other two have counts >=1.

OR

3. The original has exactly four distinct characters.

Wait, but what if the original has three distinct characters, but one of them has count >=2, and the other two have counts >=1. For example, a:2, b:1, c:1. Then answer is Yes.

Yes.

So, the steps to solve the problem:

1. Count the frequency of each character in the string.

2. Determine the number of distinct characters (let's call it K).

3. Based on K, check the conditions:

- If K > 4: answer is No.

- If K == 4: answer is Yes.

- If K == 3: check if any character has count >=2. If yes, and the other two have counts >=1, then answer is Yes. Else, No.

Wait, but for K=3, the other two counts are already >=1 (since K is 3, each has at least 1). So the condition is that any of the three characters has count >=2. Because if all three are present once, then no, but if any has count >=2, then yes.

Wait, for K=3, each character must have count >=1. Because K is 3. So for K=3, the answer is Yes if any character has count >=2.

Because if you have a character with count >=2, then you can split the original into subsets as follows:

Take one occurrence of that character and assign it to subset1, and the remaining occurrences can be split between subsets. Then, the other two characters (each count >=1) can be assigned to each subset.

For example, in sample input 2: zzcxx has z (2), c (1), x (2). K=3. Since z has count >=2, and the others have counts >=1, the answer is Yes.

Another example: a, b, c each appearing once. K=3, but all counts are 1. So no character has count >=2. So answer is No.

So, for K=3, the answer is Yes if and only if at least one character's count is >=2.

Because then, that character can be split between the two subsets (each subset gets at least one), and the other two characters can be assigned to each subset.

So the condition for K=3 is: any of the three characters has count >=2.

So:

If K is 3, then check if the maximum count among the three is >=2. If yes, answer is Yes. Else, No.

Then, K=2: check if each character's count is >=2. Because to split into two subsets, each must have at least one of each.

For example, if original is a:2, b:2. Then answer is Yes. Split into a:1 and b:1 for each subset.

If original is a:3, b:1. Then no. Because one subset would need to have a and b. But the b count is 1, so only one subset can have it.

So, K=2, answer is Yes only if both counts are >=2.

Wait, no. Wait, in the case of a:3, b:1. The subsets are:

subset1: a:2 and b:1.

subset2: a:1 and b:0. But subset2 can't have a and b. So subset2 has only a. So no.

So, for K=2, each subset must have both a and b. So each subset must have at least one a and one b. So the original counts of a and b must be >=2.

Because, for example, if a has count 3 and b has count 3, then you can split into subset1: a:2, b:1. subset2: a:1, b:2. Each has both a and b.

But if a has count 2 and b count 2, then split into two subsets each with a:1 and b:1. That works.

But if a has count 2 and b has count 1, then subset1 must have at least one of each. Then subset1 uses 1 a and 1 b. subset2 has 1 a and 0 b. But subset2 has only a. So not allowed.

So for K=2, the answer is Yes only if both counts are >=2.

So, the conditions are:

Check the distinct count K:

- K >4: No.

- K ==4: Yes.

- K ==3: check if any character has count >=2. If yes, Yes. Else No.

- K ==2: check if both counts are >=2. If yes, Yes. Else No.

- K ==1: No. Because the two subsets would each have the same character, but each subset must have exactly two distinct characters. So impossible.

Wait, K=1. For example, the original is "aaaaa". Then each subset would have a's only, which can't form two consecutive groups of different characters. So each subset would have only one character. So answer is No.

So, putting it all together:

The code steps:

1. Count the frequency of each character in the input string.

2. Determine the number of distinct characters (K).

3. Based on K:

   a. K >4: output No.

   b. K ==4: output Yes.

   c. K ==3: if any of the frequencies is >=2, output Yes. Else No.

   d. K ==2: if both frequencies are >=2, output Yes. Else No.

   e. K ==1: output No.

So, now let's test the examples.

First example input: ababa.

The frequencies are a:3, b:2. K=2. Both counts >=2. So answer is Yes.

Second example: zzcxx.

The characters are z:2, c:1, x:2. K=3. There are characters with count >=2 (z and x). So answer is Yes.

Third example: yeee.

Characters are y:1, e:3. K=2. e's count is 3 >=2, but y's count is 1 <2. So answer is No. Which matches the sample.

Another test case: "abcd". K=4. Answer is Yes.

Test case "aabb" (K=2, counts 2 and 2: answer Yes).

Test case "aab": K=2, a:2, b:1. Answer No.

Test case "abc": K=3. All counts 1. So answer No.

Test case "abcc": K=3. a:1, b:1, c:2. Answer Yes.

So this approach seems correct.

Now, how to implement this efficiently.

In Python, for the input string s:

We can count the frequencies using a Counter.

Then:

counts = list(Counter(s).values())

k = len(counts)

if k >4: print No.

elif k ==4: print Yes.

elif k ==3:

   if any(c >=2 for c in counts):

      print Yes.

   else:

      print No.

elif k ==2:

   if all(c >=2 for c in counts):

      print Yes.

   else:

      print No.

else: # k ==1:

   print No.

Yes, that's the code.

So the code would look like:

Testing against sample input 1.

```python
from collections import Counter


def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    freq = Counter(s)

    counts = list(freq.values())

    k = len(counts)

    if k >4:

        print("No", file=output_stream)

    elif k ==4:

        print("Yes", file=output_stream)

    elif k ==3:

        if any(c >=2 for c in counts):

            print("Yes", file=output_stream)

        else:

            print("No", file=output_stream)

    elif k ==2:

        if all(c >=2 for c in counts):

            print("Yes", file=output_stream)

        else:

            print("No", file=output_stream)

    else:

        print("No", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
zzcxx
""",
            "output": \
"""\
Yes
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
from collections import Counter


def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    freq = Counter(s)

    counts = list(freq.values())

    k = len(counts)

    if k >4:

        print("No", file=output_stream)

    elif k ==4:

        print("Yes", file=output_stream)

    elif k ==3:

        if any(c >=2 for c in counts):

            print("Yes", file=output_stream)

        else:

            print("No", file=output_stream)

    elif k ==2:

        if all(c >=2 for c in counts):

            print("Yes", file=output_stream)

        else:

            print("No", file=output_stream)

    else:

        print("No", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
yeee
""",
            "output": \
"""\
No
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

Sample3: yeee → counts y:1, e:3 → k=2. all(c >=2 → 1 <2 → No.

Which matches the samples.

Another test case: "abcd" → k=4 → Yes.

Test case "aab" → k=2. counts 2 and 1. all >=2 → no. So output No.

Test case "aabbcc" → k=3. counts a:2, b:2, c:2 → any >=2 → yes. Output Yes.

Thus, the code should work.

Now, let's implement it in Python.

But note that for large input (up to 1e5 characters), the code needs to be efficient. However, the code is O(n) time (for Counter), which is acceptable.

So the code is as follows.
</think>

```python
from collections import Counter
import sys

s = sys.stdin.read().strip()
freq = Counter(s)
counts = list(freq.values())
k = len(counts)

if k > 4:
    print("No")
elif k == 4:
    print("Yes")
elif k == 3:
    print("Yes" if any(c >= 2 for c in counts) else "No")
elif k == 2:
    print("Yes" if all(c >= 2 for c in counts) else "No")
else:
    print("No")
```
