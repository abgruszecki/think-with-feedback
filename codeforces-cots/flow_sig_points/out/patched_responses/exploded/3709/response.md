<think>
Okay, let's see. The problem is to find the alphabetically earliest possible login by taking a prefix of the first name and a prefix of the last name. Both prefixes must be non-empty. So for example, in the first example, 'harry' and 'potter' give 'hap' because the earliest possible is taking 'ha' (the first two letters of 'h' a, wait, wait. Wait, the first name's prefix can be any length starting from 1. So for 'harry', possible prefixes are h, ha, har, harr, harry. Similarly for potter: p, po, pot, etc. We need to choose one from first and one from last, concatenated, and find the lex smallest possible.

The key is to find the smallest possible combination. How to approach this?

Hmm. So the lex order compares the two strings character by character. The earliest string is the one that has the smallest possible first character. If the first characters are the same, then compare the second, etc.

So the optimal strategy would be to take the smallest possible prefix of the first name and then the smallest possible prefix of the last name. But wait, maybe combining a longer prefix of the first name with a smaller prefix of the last could result in a smaller overall string. Or maybe not. Let's think.

For example, suppose first name is 'ab', last name is 'a'. Then possible logins are aa (a + a), aba (ab + a), ab + a is 'aba', but 'aa' is lex smaller. So the optimal is to take the shortest possible first prefix (1 character) and the shortest possible last prefix (1 character). But what if the first name's first character is the same but the next characters are even smaller?

Wait, let's think of another example. Suppose first name is 'aab' and last name is 'b'. The possible options are 'ab', 'aab'+'b' is 'aabb', 'aab' + 'b' is 'aabb' which is longer. The smallest is 'ab'. So here, the first prefix is 'a', last is 'b'. So the approach of taking the smallest possible first prefix (i.e., the first character) and then the smallest possible last prefix (first character) gives the lex smallest.

Wait, but what if the first name starts with a character that's the same but longer? Like first name is 'abc', last name is 'def'. The earliest possible is 'ad' (a from first, d from last). But if the first name's first character is 'a', then even if we take longer prefixes of the first name, the first character remains 'a', so the next step would be to compare the second character. Wait, but the second character of the combined login depends on the first name's prefix and the last name's prefix.

So perhaps the lex smallest login is formed by taking the lex smallest possible first name prefix, and then the lex smallest possible last name prefix. Because any longer first prefix would start with the same first character, but then might have a second character that is larger. Wait, but the first prefix is a prefix, which is built by adding characters. So the lex order of the first prefixes is determined by their own lex order. For example, the prefixes of 'ab' are 'a', 'ab'. 'a' is lex smaller than 'ab' because it's shorter and the same up to that point. Similarly, if the first name is 'aab', then its prefixes are 'a', 'aa', 'aab'. The lex order of these is 'a' is the smallest, then 'aa', then 'aab'.

So the lex smallest first name prefix is the single first character. Then, for the last name prefix, the lex smallest is the first character. So the combination would be first_char + last_char. But wait, maybe taking a longer first name prefix and a shorter last name prefix could result in a lex smaller string? No, because the first part is the first name's prefix. For example, if first name is 'ab', last name is 'a'. The possible logins are 'aa' (a + a), 'aba' (ab + a), 'ab' + 'a' is 'aba'. 'aa' is lex smaller than 'aba'. So taking the first prefix as 'a' and the last as 'a' gives a better result. So the minimal first prefix and minimal last prefix seems to be the way.

Wait, but what if the first name's first character is 'a', and the last name's first character is 'a' as well. Then the combination is 'aa', but maybe taking a longer first prefix and a longer last prefix could result in a lex smaller string. For example, first name is 'aa', last name is 'aa'. Then 'aa' (a + a) is same as 'aaaaa' in terms of lex order. Wait, no. Wait, the lex order compares strings character by character. So 'aa' is lex smaller than 'aaaaa' because the third character of the latter is 'a' but the former is shorter. Wait, no: the lex order is determined first by the first differing character. If one is a prefix of the other, then the shorter one is considered smaller. So for example, 'a' is smaller than 'aa', because 'a' is a prefix of 'aa' and is shorter. So in the case where the first name is 'a' and the last name is 'a', the login is 'aa'. But if the first name is 'aa' and last is 'aa', then the minimal is 'aa' (a from first, a from last) which is 'aa', but the longer prefixes would give 'aaaaa' which is longer but not lex smaller. So the minimal is indeed 'aa'.

So the key idea is that the lex smallest possible login is the combination of the lex smallest possible first name prefix and the lex smallest possible last name prefix. Because any longer prefixes of the first name would start with the same character (the first character) but have longer length, which would make the combination longer but not lex smaller. For example, the first character of the first name's prefix is the earliest possible; if you take a longer prefix, the first character is the same, but the second character may be higher than the first character of the last name's prefix, leading to a worse lex order.

Wait, but maybe there's a scenario where taking a longer prefix of the first name allows a shorter prefix of the last name, but the combination is lex smaller. Let's think of such a case.

Suppose first name is 'ab', last name is 'c'.

The minimal login would be 'ac' (a + c). But if we take 'ab' from the first name and 'c' from the last, the login is 'abc', which is lex larger than 'ac'. So in this case, the minimal is indeed the combination of the minimal first and last.

Another example: first name is 'a', last name is 'ba'. The minimal login would be 'ab' (a + b). But if we take 'a' from first and 'ba' from last, the login is 'ab', which is same as the first case. Wait, but the first part is 'a' and the last is 'b' (the first character of the last name). So the login is 'ab' which is the same as taking 'a' and 'ba' (since the last's prefix is 'b', which is the first character). Wait, no. The last name's prefixes are 'b', 'ba', 'baa', etc. So the minimal prefix for the last name is 'b', so the login is 'ab'. But if you take the last's prefix as 'ba', then the login is 'abba' which is lex larger than 'ab' because 'ab' is shorter. So the minimal is 'ab'.

So perhaps the optimal solution is to take the lex smallest prefix of the first name and the lex smallest prefix of the last name. Because any longer prefixes would have the same starting character (for the first name) but potentially add characters that could make the combination lex larger.

So the steps would be:

1. Find the lex smallest possible prefix of the first name. Since all prefixes are non-empty, the lex smallest is the first character. For example, for 'harry', the lex smallest prefix is 'h'. For 'aab', it's 'a'.

Wait, but wait. The lex order of the prefixes of the first name is determined by their own lex order. The prefixes are all possible prefixes of the first name. The lex order of the prefixes is such that the shortest possible is the lex smallest. Because any longer prefix will start with the same characters as the shorter ones, but have more. So, for example, 'h' is lex smaller than 'ha', because 'h' is a prefix of 'ha' and shorter. Similarly, 'a' is lex smaller than 'aa', etc.

Thus, the lex smallest prefix of the first name is the single first character.

Similarly, the lex smallest prefix of the last name is the first character.

Thus, the optimal login would be the first character of the first name concatenated with the first character of the last name.

Wait, but that's not the case in the first example. Let's look at the first sample:

Input: harry potter.

The first character of the first name is 'h', the first character of the last is 'p'. So the login would be 'hp'. But the sample output is 'hap'. Wait, this is conflicting.

Wait, the first sample's output is 'hap'. Hmm. So how does that happen?

Wait, the first sample's input is 'harry potter'. So the first name is 'harry', last name 'potter'. The possible login is formed by taking a prefix of the first and a prefix of the last. The output is 'hap'. So 'ha' from 'harry' (the first two letters) and 'p' from 'potter' (the first letter). So the combination is 'hap'.

But according to the previous reasoning, the minimal would be 'h' + 'p' = 'hp', which is lex smaller than 'hap'. Because 'h' is the first prefix of 'harry', and 'p' is the first of 'potter'. So why is the sample output 'hap'?

Wait, that's a problem. Because according to the sample input, the correct output is 'hap', which is longer than 'hp'. So our initial reasoning must be wrong.

Ah, I see. So my initial approach is incorrect. That's a big mistake. So why is the sample output 'hap' instead of 'hp'?

Wait, let's compare the two strings 'hp' and 'hap'. Which is lex smaller? Let's compare character by character.

First character: 'h' vs 'h' → same.

Second character: 'p' vs 'a' → 'a' is smaller than 'p'. So 'ha' (the first two letters of the first name) plus 'p' (the first of the last) gives 'hap', which is lex smaller than 'hp' because 'ha' is the first part. Wait, no. Wait, 'hp' is two characters, 'hap' is three. So how do they compare?

Compare them step by step. 'h' vs 'h' → same. Then 'p' (second character of 'hp') vs 'a' (second character of 'hap'). 'a' is smaller than 'p', so 'hap' is lex smaller. So even though 'hp' is shorter, the second character is 'a' in 'hap' which makes it lex smaller. So 'hap' is lex smaller than 'hp'.

Ah, right! So the initial approach of taking the first character of each is not sufficient. Because in this case, taking a longer prefix of the first name (but still as small as possible) leads to a better result.

So what's the correct approach here?

We need to find the combination of a prefix of the first name and a prefix of the last name such that the concatenated string is lex smallest possible.

To find the lex smallest possible, the algorithm must consider all possible prefixes of the first name and all possible prefixes of the last name, generate all possible combinations, and choose the lex smallest one.

But with the constraints of the problem (each string up to 10 characters), the total number of possibilities is (len(first) * len(last)) which is 10*10=100 at maximum. So even a brute-force approach would be acceptable here.

So the approach would be:

Generate all possible prefixes of the first name (from 1 to len(first)), generate all possible prefixes of the last name (from 1 to len(last)), concatenate them, and then pick the lex smallest one.

That's feasible since the maximum possible combinations are 10*10=100, and comparing 100 strings of up to 20 characters each is negligible in terms of computation time.

So the steps are:

1. For each possible prefix of the first name (length 1 to len(first)), collect all possible prefixes.

2. For each possible prefix of the last name (same), collect all.

3. For every combination of first_prefix and last_prefix, compute the concatenated string.

4. Find the lex smallest among all these concatenated strings.

That's straightforward, and given the small constraints, it's efficient.

So the code would generate all possible first and last prefixes, create all possible combinations, and select the minimum.

So let's see the first sample. The first name is 'harry', which has prefixes h, ha, har, harr, harry. The last name 'potter' has prefixes p, po, pot, pott, potte, potter. For each combination of first_prefix and last_prefix, we generate the concatenated string. For example:

h + p → hp

h + po → hpo

ha + p → hap

ha + po → hapo

har + p → harp

etc.

Now, compare all these strings. The lex smallest would be 'hap' (ha + p), which is indeed the sample output.

So the brute-force approach works here. Let's see why.

Because even though the first name's first character is 'h', taking 'ha' gives a longer first part but the second character in the concatenated string (a) is smaller than the second character of the other options (like 'hp' which has 'p' as second character). So the key is that the combination of first and last prefixes may have a longer first part, which allows earlier characters in the concatenated string to be smaller.

Thus, the correct approach is to generate all possible combinations and find the minimum.

So the plan is:

Generate all possible first_prefixes (from 1 to len(first)), same for last_prefixes.

Generate all possible combinations (first_p, last_p), concatenate them, and select the lex smallest.

Now, the code.

In Python, we can generate the prefixes for each name as follows.

For a given string s, the prefixes are s[0:i] for i in 1 to len(s).

Then, for each possible first_p in first_prefixes and last_p in last_prefixes, create the string first_p + last_p.

Collect all these strings, then return the minimum.

This is O(n*m) where n and m are up to 10, so 100 iterations, which is trivial.

Thus, the code can be written as:

Read first and last names.

Generate all possible first_prefixes and last_prefixes.

Generate all possible combinations and compute their concatenation.

Find the minimum of all these concatenations.

Thus, the code will look something like:

first, last = input().split()

first_prefixes = [first[:i] for i in range(1, len(first)+1)]

last_prefixes = [last[:i] for i in range(1, len(last)+1)]

min_login = min(f + l for f in first_prefixes for l in last_prefixes)

print(min_login)

That's the code. Let's test it against the sample.

Sample 1: 'harry potter' → first_prefixes are h, ha, har, harr, harry. last_prefixes p, po, pot, pott, potte, potter.

The concatenations:

h + p → 'hp'

h + po → 'hpo' → 'hp' is shorter and lex smaller than 'hpo' (since 'hp' is prefix and shorter, so 'hp' is lex smaller than 'hpo').

But wait, 'hap' (ha + p) is 'hap', which when compared to 'hp':

Compare 'h' vs 'h' → same. Then second character 'a' vs 'p' → 'a' is smaller. So 'hap' is lex smaller than 'hp'.

So the code would generate all possible combinations and choose the lex smallest, which is correct.

Sample 2: 'tom riddle' → output is 'tomr'.

Let's see. first_prefixes are t, to, tom. last_prefixes are r, ri, rid, ridd, riddl, riddle.

Combinations include:

t + r → 'tr'

t + ri → 'tri' → 'tr' is lex smaller than 'tri' (since shorter). So the minimum would be 'tr'? But the sample output is 'tomr'.

Wait, but what's happening here. Wait, the sample input is 'tom riddle'. The first name is 'tom', possible first_prefixes are 't', 'to', 'tom'. The last name is 'riddle', possible prefixes are 'r', 'ri', 'rid', 'ridd', 'riddl', 'riddle'.

Now, let's generate some combinations:

t + r → 'tr'

to + r → 'tor'

tom + r → 'tomr'

t + ri → 'tri' → 'tr' is smaller than 'tri'.

to + ri → 'tori' → but 'tr' is smaller.

tom + ri → 'tomri' → etc.

So among all possible combinations, which is the lex smallest?

Wait, let's compare 'tr' and 'tomr'. 

Compare 't' vs 't' → same.

Then 'r' (second character of 'tr') vs 'o' (second character of 'tomr'). 'o' is smaller than 'r', so 'tomr' is lex smaller than 'tr'? Wait no: 'tr' is length 2, 'tomr' is length 4. So the first two characters of 'tr' are 't' and 'r', while the first two of 'tomr' are 't' and 'o'. Since 'o' is lex smaller than 'r', the 'to' part is better. Wait, no. Wait, 'tr' is 'tr', 'tomr' is 't' + 'omr' → 'tomr'.

So comparing 'tr' vs 'tomr':

The first character is 't' in both.

Second character: 'r' vs 'o' → 'o' is smaller. So 'tomr' is lex smaller than 'tr'.

Thus, 'tomr' is the correct output.

So the code would generate all possible combinations, including 'tomr' (tom + r) which is 'tomr' and is lex smaller than 'tr' (t + r) because the second character is 'o' which is smaller than 'r'.

So the code's approach of checking all possible combinations and selecting the minimum is correct.

Thus, the code is correct.

Now, considering the code's efficiency, even for maximum input sizes (each name is 10 characters), there are 10 * 10 = 100 possible combinations. Generating all and finding the minimum is acceptable.

Therefore, the code provided as:

first, last = input().split()

f_p = [first[:i] for i in range(1, len(first)+1)]

l_p = [last[:i] for i in range(1, len(last)+1)]

min_login = min(f + l for f in f_p for l in l_p)

print(min_login)

But wait, in Python, when you compute the min of the generated list, it will compare all possible combinations. So this code will work.

Testing the code against the samples:

Sample 1:

Input: harry potter.

f_p is ['h', 'ha', 'har', 'harr', 'harry'].

l_p is ['p', 'po', 'pot', 'pott', 'potte', 'potter'].

The combinations would include:

h + p → 'hp'.

ha + p → 'hap'.

har + p → 'harp'.

...

The minimal among all is 'hap'.

Sample 2:

Input: tom riddle.

f_p is ['t', 'to', 'tom'].

l_p is ['r', 'ri', 'rid', 'ridd', 'riddl', 'riddle'].

The combinations include:

t + r → 'tr'.

to + r → 'tor'.

tom + r → 'tomr'.

t + ri → 'tri'.

to + ri → 'tori'.

etc.

The minimal is 'tomr' because comparing all combinations:

Looking for the lex smallest. For example, 'tomr' is formed by 'tom' (first_prefix) and 'r' (last_prefix). When compared to 'tor' (to + r), 'tomr' is 't o m r', while 'tor' is 't o r'. Comparing the first two characters: same. Third character 'm' (in 'tomr') vs 'r' (in 'tor'): 'm' is smaller. So 'tomr' is lex smaller than 'tor'.

But wait, 'tomr' is longer than 'tor'? So when comparing 'tomr' and 'tor', the first three characters are 't o m' vs 't o r'. The third character 'm' is smaller than 'r', so 'tomr' is lex smaller than 'tor'.

Thus, the code will find the correct 'tomr' as the minimal.

Therefore, the code works for the samples.

Thus, the code is correct and efficient.
</think>

```python
first, last = input().split()
first_prefixes = [first[:i] for i in range(1, len(first)+1)]
last_prefixes = [last[:i] for i in range(1, len(last)+1)]
min_login = min(f + l for f in first_prefixes for l in last_prefixes)
print(min_login)
```