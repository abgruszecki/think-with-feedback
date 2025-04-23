<think>
Okay, let's see. The problem is about selecting words from a list such that all the selected words can be written using at most two distinct letters. The goal is to maximize the total length of these words. Hmm.

So first, I need to figure out for each possible pair of letters, which words can be formed using only those two letters. Then, for each pair, sum the lengths of all such words, and find the maximum sum over all possible pairs.

Wait, but the pair could also be a single letter. Because maybe the best is to take all words that use only one letter, like 'a's. But since the problem allows up to two distinct letters, the optimal could be a pair (like a and b) or a single (like a only). So I need to consider all possible pairs, including pairs where the two letters are the same, but that's redundant. Wait no, pairs are combinations. Wait, no. Because if you have a pair (a, a), that's not a valid pair. Because pairs are two distinct letters. Wait, but the problem says "no more than two distinct letters". Oh right, so the article can use one or two distinct letters. So the allowed words are those that have all their characters in the chosen set of one or two letters.

Wait, but when considering possible pairs, maybe we need to consider all possible combinations of 1 or 2 letters. Because for example, if all words are made of a single letter, then the best is to take all of them. Or if there's a word that uses two letters, like 'ab', then the allowed set could be those words that use a and/or b.

So the approach should be:

1. Generate all possible pairs of letters (including single letters, treated as a pair with themselves?), but perhaps considering all possible pairs of two distinct letters and all single letters.

Wait, but how to model this. For example, for the case where the selected letters are a and b, all words that use any combination of a and b (including only a, only b, or both) are allowed. Also, if the selected letters are just a single letter, then all words composed of only that letter are allowed.

So the optimal solution is the maximum between:

- The maximum sum when selecting a single letter (i.e., all words using only that letter), and

- The maximum sum when selecting a pair of distinct letters (i.e., all words using only those two letters).

Therefore, the plan is:

- For each possible single letter (a-z), compute the sum of lengths of words that consist only of that letter.

- For each possible pair of distinct letters (like a and b), compute the sum of lengths of words that consist only of those two letters.

- The answer is the maximum value among all these possibilities.

But considering all possible pairs is manageable since there are 26 letters, so there are 26 + 26*25/2 = 26 + 325 = 351 possible combinations. For each combination, we check all n words (n up to 100) whether their characters are a subset of the pair.

Since n is 100 and each word's length is up to 1000 (but total 1000), the total processing is manageable.

So steps for the code:

1. Read all the words and pre-process each word to check which letters it uses.

For example, for each word, we can store the set of unique characters in it. Then, for a given candidate pair (c1, c2), we check if the word's character set is a subset of {c1, c2}.

But how to generate all possible candidate pairs.

So the steps would be:

- Precompute for each word the set of unique letters it uses. For example, for a word 'abb', the set is {'a', 'b'}, and for 'aaa', it's {'a'}.

- For each possible candidate pair (which can be a single letter or two distinct letters):

   a. Iterate through all words, and for each, check if its character set is a subset of the candidate pair's letters.

   b. Sum the lengths of the words that meet this condition.

- The maximum sum over all candidates is the answer.

But how to generate all possible candidate pairs. Let's think: The candidate can be any subset of 1 or 2 letters from the 26 letters. So for the 1-letter candidates, each is one of the 26 letters. For 2-letter candidates, it's combinations (since the order doesn't matter; for example, a and b is the same as b and a for this purpose). So for two distinct letters, there are 26 * 25 / 2 possible pairs.

So total candidates are 26 (single letters) + 325 (pairs) = 351. That's manageable.

So the code can generate all possible pairs (including single letters), then for each, check all words.

But how to represent the candidate pairs. For a single letter, the candidate is (c, c) or (c), but perhaps to represent it as a set of one or two letters. Wait, perhaps for each candidate pair, the set of allowed letters is {c1, c2}, where c1 and c2 can be the same (for the single-letter case). Wait, but for the single-letter case, the allowed letters are just {c}, so the candidate pair could be (c, c). Then, the code can treat all candidates as pairs, even if they are the same. Then, for each candidate pair (c1, c2), the allowed letters are the union of c1 and c2. But if c1 == c2, then it's a single-letter set. So this way, all possible candidate pairs are considered.

Wait, but how to generate all possible pairs (including same letters). Because 26 letters for each of the two positions, but that would generate 26*26=676 possible pairs, including (a,a), (a,b), (a,c), etc. But in reality, the pair (a,a) is equivalent to the single-letter candidate a, and (a,b) is equivalent to (b,a). So perhaps it's better to generate all possible pairs where the two letters are the same (i.e., 26 possibilities) and all possible pairs where the two letters are different (i.e., 26*25/2 = 325). But generating all possible ordered pairs (like (a,a), (a,b), (b,a), etc.) would result in redundant checks. For example, (a,b) and (b,a) are the same candidate pair. So to avoid redundant checks, it's better to generate each unique pair once.

So here's the plan:

Generate all possible candidate pairs as follows:

- For single-letter candidates: generate (a, a) for each a in a-z.

- For two distinct letters: generate all pairs (a, b) where a < b. So for each pair of distinct letters, we generate them once in sorted order.

This way, each candidate pair is considered once. For example, (a, b) and (b, a) are treated as the same pair, so we generate them once as (a, b) where a < b.

But wait, when generating the candidates, the order doesn't matter. So for each pair (a, b) where a < b, we can consider the set {a, b} as the allowed letters. So the code will generate 26 (single-letter) + 325 (two-letter) = 351 candidates, which is manageable.

But how to generate all these pairs in code.

In Python, for the single-letter candidates, we can loop through each letter from 'a' to 'z' and create a pair (c, c). For the two-letter candidates, loop through all combinations of two distinct letters where the first is less than the second (to avoid duplicates).

Alternatively, for all possible pairs (c1, c2) where c1 <= c2. Because if c1 == c2, then it's a single-letter candidate. Otherwise, it's a two-letter pair. Then, for each pair (c1, c2), the allowed letters are {c1, c2}.

But how to generate these pairs. Let's think:

For c1 in 'a' to 'z':

   for c2 in c1 to 'z':

       add (c1, c2) as a candidate pair.

So for example, when c1 is 'a', c2 ranges from 'a' to 'z'. So for 'a', 'a' (single), then 'a', 'b', etc. For 'b', 'b' (single), 'b', 'c', etc. This way, each possible candidate pair is generated once. The number of such pairs is 26 (for c1 from a to z, each with c2 = c1) plus 25 for c1= a, c2 from a+1 to z, etc. So the total is 26 + 25 + 24 + ... + 1 = 26*27/2 = 351, which matches the earlier count.

So this way, all possible candidate pairs (single and two-letter) are generated once. Then, for each candidate pair (c1, c2), the code checks for each word whether the set of characters in the word is a subset of {c1, c2}.

So the code will:

- Precompute for each word the set of unique characters.

Then, for each candidate pair (c1, c2):

   allowed = {c1, c2}

   total = 0

   for each word in words:

       if the word's character set is a subset of allowed:

           total += len(word)

   max_total = max(max_total, total)

So that's the approach.

Now, the next step is to implement this.

First, how to generate the candidate pairs.

In Python, for c1 and c2 in lowercase letters, but ordered such that c1 <= c2.

So perhaps:

from itertools import combinations_with_replacement

for pair in combinations_with_replacement('abcdefghijklmnopqrstuvwxyz', 2):

But combinations_with_replacement('abc', 2) would generate pairs (a,a), (a,b), (a,c), (b,b), (b,c), (c,c). So that's exactly what we need. So using combinations_with_replacement for r=2 would generate all possible pairs (c1, c2) where c1 <= c2. So that's perfect.

Wait, but for the letters in order. Let's see. The string 'abcdefghijklmnopqrstuvwxyz' is ordered correctly, so combinations_with_replacement would generate all pairs (c1, c2) where c1 <= c2. So that's exactly what we need.

So the code can generate all candidate pairs using combinations_with_replacement of length 2.

But wait, the code is going to generate all possible pairs where c1 and c2 are in the 26 letters, and c1 <= c2. So this will generate all 351 candidate pairs (including 26 single-letter pairs where c1 = c2). So that's exactly the needed candidates.

So for each candidate pair (c1, c2), which may be the same or different, we need to check if the word's characters are all in {c1, c2}.

Now, for each word, we can precompute the set of unique characters. So for example, for a word 'aab', the set is {'a', 'b'}. For a word 'aaa', the set is {'a'}.

Then, for a candidate pair (c1, c2), the allowed set is {c1, c2}.

So for a word to be included, the word's set must be a subset of the allowed set.

So the code can precompute for each word its set of unique characters. Then, for each candidate pair, sum the lengths of all words whose set is a subset of the pair's set.

So the code steps:

1. Read n.

2. Read n words, storing each word and its set of characters. Also, store the length of each word.

But in code, perhaps for each word, compute the set of unique characters once, then for each candidate pair, check if that set is a subset of the pair's set.

So code outline:

n = int(input())
words = []
for _ in range(n):
    word = input().strip()
    chars = set(word)
    words.append( (word, chars) )

max_total = 0
from itertools import combinations_with_replacement

for c1, c2 in combinations_with_replacement('abcdefghijklmnopqrstuvwxyz', 2):
    allowed = {c1, c2}
    current_sum = 0
    for word, chars in words:
        if chars.issubset(allowed):
            current_sum += len(word)
    if current_sum > max_total:
        max_total = current_sum

print(max_total)

Wait, but for the pair (c1, c2), allowed is {c1, c2}. But if c1 and c2 are the same (like (a,a)), then allowed is a singleton set {a}.

Yes. So for a candidate pair (a,a), allowed is {a}, so any word whose characters are all a's will be included.

Yes.

This code should handle all possible cases. Let's test it against the examples.

First example:

Input:
4
abb
cacc
aaa
bbb

Processing:

Each word's char sets:

abb -> {'a', 'b'}
cacc -> {'c', 'a'}
aaa -> {'a'}
bbb -> {'b'}

Now, the candidate pairs:

Check all possible pairs.

The optimal pair is (a, b). Because:

allowed set {a, b}.

Words that are subsets:

abb (yes), aaa (yes), bbb (yes). cacc's set is {'c', 'a'}, which is not subset of {a, b}, so not included. So sum is 3 (abb) + 3 (aaa) +3 (bbb) = 9.

Which matches the sample output.

Another possible candidate pair is (a, a), which would include aaa, but also check words whose characters are a only. So that would sum len(aaa) + any other words that are a-only. But in the sample, only aaa is a-only. So sum is 3. But (a,b) gives 9.

Similarly, candidate (a, c) would have sum of abb (no, because c not allowed?), but cacc's set is {c,a} which is allowed. But words that are subsets of {a,c} are cacc (4), aaa (3). So sum is 4+3=7. Which is less than 9.

So the code would correctly choose 9.

Second example:

Input:
5
a
a
bcbcb
cdecdecdecdecdecde
aaaa

Words and their sets:

a: {'a'}
a: {'a'}
bcbcb: {'b','c'}
cdecdecdecdecdecde: {'c','d','e'}
aaaa: {'a'}

The candidate pairs:

Looking for the best pair.

The best single-letter is 'a', sum is len(a) + len(a) + len(aaaa) = 1+1+4=6.

Another candidate pair: (c,d) would have the third word (bcbcb's set is {b,c}, which is not subset of {c,d}, so no. The fourth word's set is {c,d,e}, which has three letters, so can't be included. So sum for (c,d) is 0.

So the maximum is 6, which matches the sample.

So the code works for the samples.

Now, what about the time constraints?

The code has to process 351 candidate pairs, each with 100 words. For each word, the check is whether the word's character set is a subset of allowed. Each such check is O(1) in practice, because the size of the word's character set is up to 26, but for each candidate pair, the allowed set is at most 2 elements. So subset checking can be done quickly.

But in Python, the subset check is O(k), where k is the size of the word's character set. However, since each word's character set is up to 26 elements (but in practice, for many words it's 1 or 2), the subset check is manageable.

Given that n is up to 100, and 351 iterations, total operations are 351 * 100 = 35,100 operations. Each operation is a subset check (say, up to 26 elements), but even if each check takes 26 steps, that's 35,100 * 26 = 912,600 steps. Which is well within the time constraints for Python (even with 2 seconds, which is about 2e8 operations allowed, this is way under).

So the code is efficient enough.

Now, possible optimizations. For example, precompute all possible candidate pairs and precompute the sum for each candidate pair. But the code as written is already efficient.

Another optimization: for each candidate pair, when allowed is a single letter (c1 == c2), the allowed set is {c1}. So for words to be included, their set must be a subset of {c1}, which is equivalent to the word's set being {c1} (since the word's set can't be empty). But in code, the subset check is sufficient.

Another thing to note: words with zero characters? But the input constraints say each word is non-empty, since the problem says "words consist only of lowercase letters" and in the examples, all words have at least one character. So no empty words.

So the code is correct.

Now, the code as written reads the words, precomputes their sets, and then for each candidate pair (generated as combinations_with_replacement) computes the sum.

So that's the code. Now, in Python, the code will be:

Read n.

Read n lines, each line is a word.

For each word, compute the set of characters.

Then generate all combinations_with_replacement of two letters from 'a' to 'z'.

For each pair in these combinations:

   allowed = {c1, c2}

   sum the lengths of words whose char set is subset of allowed.

   keep the maximum.

Finally, print the maximum.

Yes.

Now, the code may need to generate all the combinations. But 'itertools.combinations_with_replacement' is part of the standard library and efficient.

But in Python, creating a string of all lowercase letters as 'abcdefghijklmnopqrstuvwxyz' and then generating the combinations is straightforward.

So the code should work. Let's write it.

Testing the first sample:

n=4, words are 'abb', 'cacc', 'aaa', 'bbb'.

For the pair (a, b), allowed is {'a','b'}.

Check each word:

abb's set {'a','b'} is subset of allowed? Yes. Add 3.

cacc's set {'c','a'} is not subset (c not in allowed). So no.

aaa's set {'a'}: yes. Add 3.

bbb's set {'b'}: yes. Add 3.

Sum is 3+3+3=9.

Which is correct.

The code would select this sum.

Thus, the code works.

Another test case: the second example.

The code for candidate pair (a,a) allowed set {'a'}.

Sum is 1+1+4=6.

Other pairs may have lower sums.

Thus, code outputs 6.

Thus, the code should work.

Now, the code uses combinations_with_replacement. Let's make sure that in Python, the 'combinations_with_replacement' is called correctly.

Yes: combinations_with_replacement('abcdefghijklmnopqrstuvwxyz', 2) would generate all possible pairs where the two letters are ordered and possibly the same.

Yes.

So the code is correct.
</think>

```python
import itertools

n = int(input())
words = []
for _ in range(n):
    word = input().strip()
    chars = set(word)
    words.append((word, chars))

max_total = 0
letters = 'abcdefghijklmnopqrstuvwxyz'

for c1, c2 in itertools.combinations_with_replacement(letters, 2):
    allowed = {c1, c2}
    current_sum = 0
    for word, chars in words:
        if chars.issubset(allowed):
            current_sum += len(word)
    if current_sum > max_total:
        max_total = current_sum

print(max_total)
```