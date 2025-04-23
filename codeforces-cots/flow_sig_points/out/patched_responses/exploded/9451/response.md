<think>
Okay, I need to solve this problem where I have to check if three lines form a haiku based on the syllable counts. Let's see. The syllables are counted as the number of vowels (a, e, i, o, u) in each phrase. The first line should have 5, the second 7, and the third 5 again.

First, I need to process each line. For each line, split into words, but the input might have leading or trailing spaces, and words are separated by one or more spaces. So, for each line, I should split the line into words, trimming any leading or trailing spaces, and splitting on any number of spaces. Then, for each word in the line, count the number of vowels. Sum all those counts for each line to get the syllable count for that line.

So the steps are:

1. Read three lines from input.
2. For each line:
   a. Trim leading/trailing whitespace.
   b. Split into words (split on whitespace, which automatically handles multiple spaces).
   c. For each word, count the vowels (a, e, i, o, u), case-insensitive but the input is lowercase anyway.
3. Check if the counts are 5,7,5 in order. If all three lines match, output YES, else NO.

But wait, how do I process each line? Let's think about possible edge cases. For example, a line with multiple spaces between words, or leading/trailing spaces. The split method in Python's split() function with default parameters will split on any whitespace, including multiple spaces, and leading/trailing are ignored. So for example, '  a  b  ' split would be ['a', 'b'].

So for each line, I can do line.strip() to remove leading and trailing spaces, then split into words. Wait, no. Because if the line is split into words using split() without stripping, but perhaps leading or trailing spaces would lead to empty strings. Wait, no. For example, '   a   b   '.split() would automatically split into ['a','b'], because the split() method without arguments splits on any whitespace, and ignores leading and trailing. So perhaps the correct way is to use split().

So processing each line:

For each line in the input, after stripping leading/trailing spaces (but the split() function would handle that automatically?), but maybe stripping first to avoid empty strings in the split. Wait, no. Because even if there are leading or trailing spaces, the split() method will ignore them. So for example:

line = '   hello world   '
words = line.split() → ['hello', 'world']

So splitting the line with split() is sufficient to get the list of words, regardless of leading or trailing spaces. So for each line, we can just split() it, which gives a list of words (non-empty).

Once we have the list of words, we need to count the vowels in each word and sum for the line.

So for each word in words, count the number of vowels. How to do that? For each character in the word, check if it is in {'a','e','i','o','u'}, and sum those.

So for a line, syllables = sum( sum(1 for c in word if c in vowels) for word in words )

Once we have the counts for the three lines, check if they are 5,7,5 in order.

Now, let's think about possible mistakes. What if a word is empty? But according to the problem statement, each word is a non-empty sequence of lowercase letters, so the input lines are such that after splitting, words are non-empty.

But since the input lines are guaranteed to have at least one word (as per constraints), we don't need to worry about empty lists.

So the plan is:

- vowels = {'a', 'e', 'i', 'o', 'u'}
- For each of the three lines:
   - split into words using split()
   - compute sum of vowels in each word, sum all to get the syllable count
- Check if the counts are [5,7,5]. If yes, output YES else NO.

Now, code-wise, in Python:

Read three lines. For each line, process as above.

Implementing this:

Read line1 = input().strip() → but wait, input().strip() is not necessary because split() will handle leading and trailing spaces. So, for each line, words = input().split()

But sometimes, when the user inputs a line with leading or trailing spaces, split() will ignore them. So line processing is correct.

Then, for each word in words:

sum(1 for c in word if c in vowels) → sum all these per word, then sum for the line.

So code:

vowels = {'a', 'e', 'i', 'o', 'u'}

counts = []
for _ in range(3):
    line = input().split()
    total = 0
    for word in line:
        total += sum(1 for c in word if c in vowels)
    counts.append(total)

if counts == [5,7,5]:
    print("YES")
else:
    print("NO")

Wait, but what if the lines have leading/trailing spaces? For example, the first sample input:

Sample Input 1:

on  codeforces
beta round is running
a rustling of keys

Each line may have leading or trailing spaces, but split() handles that. So the code would correctly process the words.

Testing sample input 1:

First line: 'on  codeforces' → split into ['on', 'codeforces'] → 'on' has two vowels (o), 'codeforces' has o, e, o, e → 4. Total 6? Wait, but sample output says YES. Wait wait, what's the problem here.

Wait, wait, the first sample's first line is 'on codeforces' → 'on' has two vowels (o). codeforces: 'codeforces' → let's see: c o d e f o r c e s. The vowels are o, e, o, e → four. So total 2+4=6. But according to the sample output, the first line's count is 5. So that can't be right. Wait, maybe I made a mistake.

Wait, the sample input 1's first line is written as:

on  codeforces

But according to the sample output, the first line's syllables sum to 5. So perhaps my code is wrong.

Wait, perhaps the first line's words are 'on', 'codeforces' → let's count vowels in 'codeforces':

c o d e f o r c e s → o, e, o, e. So four vowels.

Wait, but 2+4=6. But sample output is YES, so the first line's count must be 5. Therefore, my code must be incorrect here.

Hmm, this suggests that there's a mistake in my approach. Wait, perhaps the line is not split into two words. Let's see the actual sample input.

Sample Input 1:

on  codeforces
beta round is running
a rustling of keys

The first line is "on  codeforces". When split into words, that's ['on', 'codeforces'].

But according to the sample output, the first line's count is 5. So perhaps 'codeforces' has 3 vowels. Let's count again.

Wait, codeforces: codeforces → letters are c, o, d, e, f, o, r, c, e, s.

The vowels are o, e, o, e → that's four vowels. So 2+4=6. But sample output is YES. So why is this?

This indicates that my code would fail this test case. So there's a problem. So why is the sample output YES?

Wait, the sample's first line must have a total of 5 syllables. So where is the mistake here?

Alternatively, perhaps I'm miscounting the vowels in codeforces.

Wait, codeforces:

c o d e f o r c e s → the vowels are o, e, o, e. Yes, four. Then 2+4=6. So sample input's first line would have 6 syllables, which would make the output NO, but the sample output is YES. So there's a problem here. So my approach is wrong.

Wait, what's the actual count of vowels in the first line of sample input 1?

Looking at the sample input:

The first line is "on codeforces" (assuming that in the input, the first line is "on codeforces" with two spaces between 'on' and 'codeforces'). But when split, the words are 'on' and 'codeforces'.

Wait, perhaps the codeforces word is 'codeforces'? Let's check the letters again.

Wait, codeforces is spelled c o d e f o r c e s. So o, e, o, e. So four vowels. So 2+4=6. But according to sample output, this line contributes 5 syllables. So there's a discrepancy here. That suggests that either my code is wrong, or I'm missing something.

Alternatively, perhaps the line is split into more words. For example, if the first line is "on codeforces" with two spaces, but perhaps there are leading spaces. Let me see.

Wait, the problem's first sample input is given as:

on  codeforces
beta round is running
a rustling of keys

So the first line's input is "on  codeforces" (two spaces between on and codeforces). So when split, that becomes two words. So the code's approach counts 2+4=6. So according to that, the output would be NO, but the sample says YES. So why is that?

Wait, perhaps the problem's example is wrong? Or maybe I have a misunderstanding of the problem statement.

Wait, let's re-examine the problem statement. The problem says that a haiku requires the three phrases to have 5,7,5 syllables. The sample's first input must have these counts. So let's see:

Sample Input 1:

Line 1: 'on  codeforces' → split into two words. 'on' has o → 1 vowel? Or 'on' is 'o' and 'n' → two letters. 'o' is a vowel. So 'on' has 1 vowel. 'codeforces' has o, e, o, e → 4. So total 5. Oh! Wait, maybe I made a mistake in counting the vowels in 'on'?

Wait 'on' is o and n. So 'o' is a vowel. So 'on' has 1 vowel. Then codeforces has four vowels, so total 1+4=5. Then the first line is 5. Then the code would correctly output YES.

Ah! So that's the mistake. I thought 'on' had two vowels. But no. 'on' has one vowel: 'o'. The second letter is 'n' which is not a vowel. So 'on' contributes 1, codeforces contributes 4 → total 5. Which is correct.

So in that case, the code was correct. But why did I think 'on' had two vowels earlier?

Ah, because I confused 'o' as a single vowel, but 'on' is o followed by n. So 'on' has one vowel. So the code's approach is correct.

So the code would process the first line correctly.

So the code's code for 'on codeforces' would calculate:

word 'on' → 1 vowel.

word 'codeforces' → 4 vowels.

Total 5. So the first line is 5.

The second line is 'beta round is running' → split into words: 'beta', 'round', 'is', 'running'.

beta: e, a → 2.

round: o, u → 2.

is: i → 1.

running: u, i → 2.

Total 2+2+1+2=7. So second line is 7.

Third line: 'a rustling of keys' → split into words: 'a', 'rustling', 'of', 'keys'.

a: 1.

rustling: u, i → 2.

of: o → 1.

keys: e → 1.

Total 1+2+1+1 =5. So third line is 5. So 5,7,5 → YES.

So the code would work.

Therefore, the code is correct.

Another test case: the second sample input:

how many gallons
of edo s rain did you drink
cuckoo

First line: 'how many gallons' → split into 3 words.

how → o →1.

many → a →1.

gallons → a, o →2.

Total 1+1+2=4. So first line is 4. So no.

Second line: 'of edo s rain did you drink' → split into words:

of → o →1.

edo → e, o →2.

s → 0.

rain → a, i →2.

did → i →1.

you → o, u →2.

drink → i →1.

Sum: 1+2+0+2+1+2+1=9. So second line is 9. Third line: 'cuckoo' → split into one word. 'cuckoo' has u, o, o →3. So third line is 3. So counts [4,9,3] → output is NO. Which matches the sample.

So code works.

Now, code seems correct.

But let's think about possible edge cases. For example:

- A word with all vowels: 'aeiou' → 5 syllables.

- Lines with leading and trailing spaces.

Another case: line is '   a e i o u   ' → split into ['a','e','i','o','u'] → 5 syllables. So that line would contribute 5.

Another case: a line with multiple spaces between words, but words are correctly split.

So the code's approach is correct.

Thus, the code as written should be correct.
</think>

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
counts = []
for _ in range(3):
    words = input().split()
    total = sum(sum(1 for c in word if c in vowels) for word in words)
    counts.append(total)
print("YES" if counts == [5,7,5] else "NO")
```