<think>
Okay, let's see. I need to solve this problem where I have to replace certain characters in a string based on forbidden substrings. The goal is to maximize the number of a specific lucky letter, and if there are multiple options, choose the lex smallest one.

Hmm. So first, the problem says that all occurrences of the forbidden substrings (case-insensitive) in the original string w must be found. Then, for every character in w that is covered by any of these occurrences, we have to replace it with the lucky letter, but only if possible. Wait, no. Wait, the replacement can be any other character, but we want as many lucky letters as possible. Oh right! So for each character that needs to be replaced (i.e., is part of any forbidden substring occurrence), we can choose to replace it with the lucky letter, but only if that's allowed. Wait, but the problem says that Petya should replace them in such a way that the lucky letter occurs as much as possible. So for each replaceable position, if the original character is already the lucky letter (case-insensitive?), no, wait. Let me re-read the note.

The replacement process occurs once. So for all characters that are in any forbidden substring occurrence, they have to be replaced. But during replacement, the case of the original letter must remain the same. Wait, no: the note says that when replacing, the letter's case should remain the same. So for example, if the original character is uppercase, the replaced character must be uppercase. So, the replacement is done by changing the character, but keeping the case. So if the original character was uppercase, the replacement must be an uppercase letter.

But the goal is to choose, for each replaceable character, a replacement that is the lucky letter (same case?), but wait. Wait, the lucky letter is given as a lowercase letter. So for example, if the original character is uppercase and the lucky letter is 't', then to replace it with 'T' would be better. But maybe not. Let's see the problem statement.

The lucky letter is given as a lowercase letter. So, when replacing, if possible, we should choose the same case as the original. For example, if the original character is uppercase, the replacement should be the uppercase version of the lucky letter. If that's possible. Because that way, the count of the lucky letter increases. But if the original character was already the same as the lucky letter (case-insensitive?), then we have to replace it with another character. Wait, no: the problem says that the letters that must be replaced are those covered by any forbidden substring. So for those positions, we have to replace them. The replacement must be any other character. Wait, no. Let me read the problem statement again.

The replacement of all letters covered by the occurrences. So for each such letter, we can replace it with any other character (possibly the same?), but wait no. Wait, the problem says: "a letter in position i should be replaced by any other one if..." So the replacement is mandatory. So the original character is replaced with a different character. So for example, if the original character is 'a' and the lucky letter is 'a', then we can't keep it as 'a'. We have to replace it with some other character. But we want to maximize the number of lucky letters, so when possible, we choose the lucky letter (in the correct case) if that's allowed. Wait, but the problem says that the replacement must be a different character. So for example, if the original character is uppercase 'A', and the lucky letter is 'a', then the replacement would be 'A' only if the original character was not 'A', but that's not possible. Wait, no. Let me parse this again.

The problem says: "replace the letter by any other one if ..." So the replacement must be a different character. So if the original character is 'A', and the lucky letter is 'A' (lowercase?), then the replacement cannot be 'A' (since it's the same). Wait, the problem says "the letter's case should remain the same". Wait, no: the replacement's case should remain the same. So, for example, if the original character is uppercase, the replacement must be uppercase. So when replacing, the replacement must be uppercase, but different from the original.

So for each replaceable character, we need to choose a character of the same case as the original. And we want as many as possible to be equal to the lucky letter (in the same case). But if the original character is already equal to the lucky letter (case-sensitive?), then we can't replace it with the same. Wait, the original character is replaced with a different one. So if the original character is uppercase 'A' and the lucky letter is 'a', then the uppercase lucky letter is 'A', but since we can't replace 'A' with 'A', we have to choose another uppercase letter, but that's not the lucky letter. So in that case, the best option is to pick the next best possible, which is another character that is as lex smallest as possible, but not the lucky letter.

So the approach is:

1. For each position in w, determine if it's part of any forbidden substring occurrence (case-insensitive). All such positions must be replaced.

2. For each such position, replace it with the lucky letter (matching the case) if possible. If the original character (case-insensitively) is the lucky letter, then we can't use it. So for example, original is 'A' (uppercase) and lucky is 'a'. So the lucky letter's uppercase is 'A', which is same as original. So we can't replace with that. So we need to choose another uppercase letter, which is not 'A', but preferably as lex smallest as possible (to get lex smallest string in case of multiple possibilities with same count of lucky letters).

So, the steps:

First, find all positions in w that need to be replaced. Then, for each such position, replace the character as follows:

If the original character's case is uppercase, then the replacement must be uppercase. So we can choose the uppercase version of the lucky letter only if that is different from the original. If possible, that's the best choice. If not, then choose another uppercase letter, preferably lex smallest possible (but not the original or the lucky uppercase). Wait, but the problem says that we want as many lucky letters as possible. So for each replaceable position:

Case 1: The original character (case-insensitive) is the same as the lucky letter.

E.g., original is 'A' (uppercase), lucky is 'a'. Then, uppercase version is 'A'. So replacing 'A' with 'A' is not allowed. So must choose another uppercase letter. So, the best option here is to pick the lex smallest possible uppercase letter that's not 'A'.

But since we can't use the lucky letter, we have to pick something else.

Case 2: The original character (case-insensitive) is different from the lucky letter.

Then, the replacement can be the uppercase (or lowercase) version of the lucky letter, provided it's different from the original.

So for example, original is 'B' (uppercase), lucky is 'a'. Then, we can replace 'B' with 'A' (uppercase), which is different from 'B'. So that's good. So in this case, the replacement is 'A', which counts as a lucky letter.

So for each replaceable character:

If the original is uppercase:

- The replacement should be uppercase.

- If the uppercase version of the lucky letter is different from the original character, then choose that.

- Otherwise (i.e., original is same as uppercase lucky letter), choose the lex smallest uppercase letter that's not the original and not the uppercase lucky (but in this case, the original is the uppercase lucky, so must choose something else).

Wait, but if original is uppercase and the uppercase lucky is the same as original, then when replacing, you can't choose that. So for example, original is 'A', lucky is 'a', so uppercase lucky is 'A'. So replacement can't be 'A'. So you have to choose another uppercase letter. But which one?

In this case, since we can't use the lucky letter, we need to choose the next best option. The problem says that if there are multiple options with the same number of lucky letters, choose the lex smallest one. So, for the characters that can't be replaced with the lucky letter (because it's the same as the original), we choose the lex smallest possible character that's not equal to the original and not equal to the lucky's uppercase (but since original is same as uppercase, so we just need the lex smallest possible that is not original).

Wait, but the replacement must be a different character. So for example, if original is 'A', and lucky is 'a' (so uppercase is 'A'), then the replacement must be an uppercase letter that's not 'A'. The lex smallest would be 'A' but that's not allowed, so next is 'B', then 'C', etc. So the lex smallest possible replacement is 'A' is not allowed, so next is 'B'.

Wait, but 'B' is lex greater than 'A' but in this scenario, the original is 'A' and replacement must be different. So the lex smallest possible replacement is 'B' only if we can't use 'A'. So in this case, the replacement is 'B', which is the lex smallest possible.

Wait, no. Wait, the lex order is determined by the entire string. So for a position where the original is 'A' (uppercase), and the replacement options are all uppercase letters except 'A', the lex smallest replacement would be 'A' is forbidden. So the next is 'B', 'C', etc. So to choose the lex smallest possible replacement, you pick 'A' if possible. But in this case, it's not. So the lex smallest is 'B'.

So the algorithm for each replaceable position is:

If the original is uppercase:

- desired_char = uppercase version of the lucky letter.

- if desired_char != original_char, replace with desired_char.

- else, replace with the lex smallest uppercase character that is not the original_char.

Similarly for lowercase.

If the original is lowercase:

- desired_char = lowercase version of the lucky letter.

- if desired_char != original_char, replace with desired_char.

- else, replace with the lex smallest lowercase character that is not original_char.

Wait, but in the problem statement, the lucky letter is given as a lowercase letter. So, the uppercase version is the uppercase of that letter. So, for example, if the lucky letter is 't', the uppercase is 'T'.

So, the steps are:

For each position in w:

If the position is not to be replaced, leave as is.

If it is to be replaced:

Check if the original character (case-insensitive) is the lucky letter.

Wait, no. Let's see: the original character is in the string w. So for example, if the original is 'A' (uppercase), and the lucky is 'a', then the uppercase version of the lucky letter is 'A'. So when replacing, if the original is 'A', and the desired replacement is 'A', but that's the same as original, so we can't do that. So in that case, we need to choose another character.

So for each replaceable character:

original_char = w[i]

desired_case_char = lucky.upper() if original_char is uppercase else lucky.lower()

if desired_case_char != original_char:

   replace with desired_case_char (since that's the lucky letter in the correct case, and different from original)

else:

   find the smallest possible character (in lex order) of the same case as original_char, that is not equal to original_char and not equal to desired_case_char (but since desired_case_char is same as original_char in this case, we just need the lex smallest possible not equal to original_char).

Wait, but in the else case, desired_case_char is equal to original_char, so we can't use that. So we have to find the lex smallest possible character of the same case as original_char, but not equal to original_char.

So, for example, original_char is 'A', desired_case_char is 'A' (since original is uppercase, lucky is 'a'). So replacement can't be 'A'. So possible options are 'B', 'C', ..., 'Z'. The lex smallest is 'A' is invalid. So the next is 'B'.

So, how to find that.

So the plan is:

For each replaceable character:

original_case = original_char.isupper()

desired_char = lucky.upper() if original_case else lucky.lower()

if desired_char != original_char:

   new_char = desired_char

else:

   find the lex smallest character in (all uppercase or lowercase letters) that is not original_char, and not desired_char (but since in this case, they are same, just not original_char).

So, for example, in this else case, desired_char is same as original_char, so we can't use it. So we have to pick the smallest possible character of the same case that is not original_char.

So for uppercase:

possible_chars = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if c != original_char]

sorted_chars = sorted(possible_chars)

new_char = sorted_chars[0]

Similarly for lowercase.

But wait, the lex order for uppercase letters is 'A' < 'B' < ... < 'Z'. So sorted(possible_chars) will be in order, and the first element is the smallest possible.

So for original_char 'A', possible_chars is 'B' to 'Z', so sorted gives 'B' first.

So new_char would be 'B'.

So the steps for replacement are clear.

Now, the next part is to find all the positions in the original string that are covered by any of the forbidden substrings (case-insensitive).

How to do that efficiently.

The approach here is:

We need to find all the start and end indices in w where any of the forbidden substrings occur (case-insensitive).

For example, for each forbidden substring s in the list, check all possible positions in w where s (case-insensitively) matches the substring. Then, for each such occurrence, mark all positions from start to end (inclusive) as needing replacement.

But the problem is, with the constraints.

The input constraints for n is up to 100, and each forbidden substring is up to 100 characters. The string w is up to 100 characters. So for each forbidden substring, checking all possible starting positions in w (for each possible substring of w of length equal to s's length) is feasible.

So for each forbidden substring s:

s_len = len(s)

for i in 0 to len(w) - s_len:

   substring = w[i:i+s_len]

   if substring.lower() == s.lower():

       then mark all positions from i to i + s_len -1 as needing replacement.

But since the forbidden substrings can have varying lengths, we need to check all possible substrings in w of all possible lengths equal to the forbidden substrings' lengths.

Once all forbidden substrings are processed, the positions marked for replacement are all the positions that are covered in any of the occurrences.

But this approach may have overlapping ranges. For example, two forbidden substrings overlapping in their ranges. But the problem says that any position covered by any occurrence must be replaced, regardless of how many times it's covered.

So the steps to find the replaceable positions are:

Initialize a list of booleans (mask) of the same length as w, all False.

For each forbidden substring s in the list:

   s_lower = s.lower()

   s_len = len(s)

   for i in 0 to len(w) - s_len:

       substring = w[i:i+s_len].lower()

       if substring == s_lower:

           for j in i to i + s_len -1:

               mask[j] = True

Once all forbidden substrings are processed, the mask is True for all positions that need to be replaced.

So, this approach is O(n * len(w) * len(s)). Since len(w) is up to 100, and n is up to 100, and len(s) is up to 100, the total operations are 100 * 100 * 100 = 1,000,000, which is acceptable for Python, even with 2 seconds.

So once the mask is built, we can iterate through each character in w and replace it according to the mask.

Now, the code steps:

Read n.

Read n lines of forbidden substrings.

Read the string w.

Read the lucky letter.

Build the mask.

Then, for each position in w:

if mask is True:

   replace according to the rules.

else:

   leave as is.

So, code steps in Python:

First, read the inputs.

Then build the mask.

Then process each character.

Now, code for building the mask:

n = int(input())

forbidden = [input().strip() for _ in range(n)]

w = input().strip()

letter = input().strip().lower()

mask = [False] * len(w)

for s in forbidden:

    s_len = len(s)

    s_lower = s.lower()

    for i in range(len(w) - s_len + 1):

        substring = w[i:i+s_len].lower()

        if substring == s_lower:

            for j in range(i, i + s_len):

                mask[j] = True

Then, process each character in w.

result = []

for i in range(len(w)):

    c = w[i]

    if mask[i]:

        # need to replace

        original = c

        # determine case

        is_upper = original.isupper()

        desired_char = letter.upper() if is_upper else letter

        # check if desired_char is same as original

        if desired_char != original:

            # can replace with desired_char

            result.append(desired_char)

        else:

            # need to find the lex smallest possible different from original and desired_char (which is same as original)

            # generate all possible letters of the same case, sorted, and pick the first one not equal to original.

            if is_upper:

                # iterate from 'A' to 'Z', pick first not equal to original

                for char_ord in range(ord('A'), ord('Z')+1):

                    candidate = chr(char_ord)

                    if candidate != original:

                        result.append(candidate)

                        break

            else:

                # iterate from 'a' to 'z'

                for char_ord in range(ord('a'), ord('z')+1):

                    candidate = chr(char_ord)

                    if candidate != original:

                        result.append(candidate)

                        break

    else:

        result.append(c)

Then, the result is joined into a string and output.

Wait, but in the case where desired_char is same as original, we have to pick the lex smallest possible character of the same case that is not original.

For example, original is 'A' (uppercase), desired_char is 'A' (since the lucky is 'a'). So replacement cannot be 'A'. So the code loops from 'A' to 'Z' and finds the first candidate that is not 'A', which is 'B' in this case. So that's correct.

But the code loops from 'A' to 'Z' and checks each in order. So for the uppercase case, the code finds the first character in lex order that is not original. So that's correct.

Similarly for lowercase.

This should handle all cases.

Let's test with sample inputs.

First sample input:

3

bers

ucky

elu

PetrLoveLuckyNumbers

t

The output is PetrLovtTttttNumtttt.

So let's see.

The forbidden substrings are "bers", "ucky", "elu".

The original string is "PetrLoveLuckyNumbers".

Processing each forbidden substring:

For "bers": lower is "bers". Look for substrings of length 4 in the original string.

Original is "PetrLoveLuckyNumbers" (let's see):

For example, "Petr" is the first 4 letters. Lowercase is "petr". Does it match "bers"? No.

Wait, "Love" is part of the string. But maybe in the original string, let's see:

Original string is "PetrLoveLuckyNumbers".

Wait, perhaps "Love" is part of the forbidden substrings? No, the forbidden substrings are "bers", "ucky", "elu".

So "bers" is looked for in all possible 4-letter substrings.

But perhaps in "Petr", the 'r' is part of a substring. Hmm, perhaps in the example, the forbidden substring "bers" occurs in the original string.

Wait, let's see the original string: PetrLoveLuckyNumbers.

Breaking it down into letters:

P e t r L o v e L u c k y N u m b e r s

Wait, perhaps the 'bers' occurs at the end of the string. The original string's last part is 'Numbers' — perhaps 'bers' is part of that. Let me see: "Numbers" is 'N', 'u', 'm', 'b', 'e', 'r', 's'. So the substring 'bers' would be positions 4-7 (assuming 0-based) of 'Numbers' part. But perhaps the original string is "PetrLoveLuckyNumbers" — the ending is 'Numbers', which is 'N', 'u', 'm', 'b', 'e', 'r', 's'. So the substring 'bers' would be 'b', 'e', 'r', 's' — positions 3-6 of 'Numbers' part. So the entire original string's length is 20 (assuming).

But perhaps the code correctly marks the positions.

But perhaps the key point is that the forbidden substrings are "bers", "ucky", "elu".

For "bers", looking for any occurrence in the original string (case-insensitive). The original string ends with 'Numbers', which in lowercase is 'numbers'. The last four letters are 's'? Wait, the substring 'bers' would require four letters. Let's see:

In 'Numbers' (length 7), the letters are N, U, M, B, E, R, S. So the substring 'BERS' is formed by B, E, R, S. So positions 3-6 (0-based) of the 'Numbers' part. So in the original string, this would be part of the 'LuckyNumbers' part.

Wait, the original string is 'PetrLoveLuckyNumbers', which is broken into parts like:

Petr (4), Love (4), Lucky (5), Numbers (7). So the 'Numbers' part starts at position 13 (assuming 0-based). So in the original string, the 'B' is at position 13 + 3 = 16 (since N is 13, U is 14, M is 15, B is 16, E is 17, R is 18, S is 19). So the substring 'Bers' is B E R S, which is positions 16-19. So in lowercase, that's 'bers', which matches the forbidden substring 'bers'. So mask positions 16-19 are marked as True.

Then, 'ucky' is another forbidden substring. Let's look for it. In the original string, the 'Lucky' part is 'L u c k y' (positions 8-12, assuming 0-based). So the substring 'ucky' is positions 9-12. Lowercase is 'ucky', which matches the forbidden substring 'ucky'. So mask positions 9-12 are marked.

The 'elu' forbidden substring is length 3. Looking for 'elu' in the original string. Perhaps in the 'PetrLove' part. 'PetrLove' — 'e' is at position 1, but 'e l o v e' — perhaps 'e l o' is one substring. Not sure. But in any case, the code would check all possible substrings of length 3.

Once the mask is built, the code replaces the characters in the mask positions.

For example, the 'Lucky' part (positions 8-12: 'L u c k y') — in the mask, positions 9-12 are marked (from 'ucky' forbidden substring). Then, each of those positions (9: u, 10: c, 11: k, 12: y) will be replaced.

The lucky letter is 't', so lowercase 't', uppercase 'T'.

So for position 9: original is 'u' (lowercase). Desired replacement is 't'. Since 'u' is not 't', replace with 't'. So becomes 't'.

Position 10: original 'c' (lowercase). Replace with 't'.

Position 11: 'k' → 't'.

Position 12: 'y' → 't'.

Similarly for the 'Bers' part (positions 16-19: B E R S). Each is uppercase. So replacement is 'T' (uppercase). So B becomes T, E becomes T, R → T, S → T. So those positions become 'TTTt' (assuming S is uppercase, so replaced with 'T' uppercase). Wait, 'B' (uppercase) is replaced with 'T' (uppercase), which is allowed.

So the resulting string has many 't's and 'T's.

The first sample's output is PetrLovtTttttNumtttt.

So in the original string, 'PetrLoveLuckyNumbers' becomes 'PetrLovtTttttNumtttt'.

Which makes sense.

Another test case is the third example:

Input:

2

aCa

cba

abAcaba

c

The forbidden substrings are 'aCa' and 'cba'. Let's process the mask.

Original string is 'abAcaba' (length 7). Let's process each forbidden substring.

For 'aCa' (length 3). Lowercase is 'aca'.

Looking for any substring of length 3 in 'abAcaba' that is 'aca' when lowercased.

Possible positions:

i=0: 'abA' → 'aba' → no.

i=1: 'bAc' → 'bac' → no.

i=2: 'Aca' → 'aca' → matches. So positions 2,3,4 are marked.

Wait, the substring starts at i=2 (0-based) in 'abAcaba' (characters 2,3,4 are 'Aca'? Let's see:

Original string: index 0: a, 1: b, 2: A, 3: c, 4: a, 5: b, 6: a.

So substring from i=2, length 3 is 'Aca' → lowercase 'aca' which matches the forbidden substring 'aca' (from 'aCa'). So positions 2,3,4 are marked as True.

For the forbidden substring 'cba' (length 3). Lowercase 'cba'. Check all possible substrings of length 3.

For example, i=4: 'aba' → no. i=3: 'cab' (lowercase) is 'cab' → no. Maybe another position. For instance, i=3: 'c a b' (from positions 3,4,5). Lowercase 'cab' → no. i=1: 'bAc' → 'bac' → no. So perhaps there are no occurrences of 'cba' in the original string. Or maybe I'm missing something.

Alternatively, maybe the 'cba' is found as a substring in the original. Let's check all possible positions.

Original string: a b A c a b a.

Looking for any 3-length substring that is 'cba' when lowercased.

Looking:

i=0: a b A → 'abA' → 'aba' → no.

i=1: b A c → 'bac' → no.

i=2: A c a → 'aca' → no.

i=3: c a b → 'cab' → no.

i=4: a b a → 'aba' → no.

No matches for 'cba' forbidden substring.

So the mask is positions 2,3,4 (from the 'aCa' forbidden substring), and any others?

Wait, the second forbidden substring is 'cba' (length 3). So in the original string, check all positions i where i+3 <=7. i can be 0-4.

For each i:

substring = w[i:i+3].lower() → compare to 'cba'.

i=0: 'abA' → 'aba' → not 'cba'.

i=1: 'bAc' → 'bac' → not.

i=2: 'Aca' → 'aca' → not.

i=3: 'cab' → 'cab' → not 'cba'.

i=4: 'aba' → 'aba' → no.

No matches. So the mask is only positions 2,3,4.

So the characters at positions 2,3,4 are replaced.

Original characters:

Position 2: 'A' (uppercase), position 3: 'c' (lowercase), position4: 'a' (lowercase).

The lucky letter is 'c' (lowercase).

So for each position:

Position 2 (uppercase A):

Desired_char is 'C' (uppercase).

Original is 'A', so 'C' != 'A' → replace with 'C'.

Position3 (lowercase c):

Desired_char is 'c' (lowercase). Original is 'c' → same. So must replace with 'a' (since 'a' is the next lex smallest lowercase letter that is not 'c').

Wait, no. The replacement must be the lex smallest possible character of the same case as original, not equal to original.

Original is 'c' (lowercase). So possible replacements are 'a', 'b', 'd', etc. The lex smallest is 'a'.

So position3 becomes 'a'.

Position4 (lowercase a):

Desired_char is 'c' (lowercase). Original is 'a' → different. So replace with 'c'.

So the original string 'abAcaba' (indices 0-6: a b A c a b a) becomes:

Original: a b A c a b a → after replacement:

position2 becomes 'C', position3 becomes 'a', position4 becomes 'c'.

So the new string is a b C a c b a → "abCacba", which matches the sample output.

So the code works.

Now, code for generating the replacement character.

In code:

For the else case (desired_char == original), the code loops through 'A' to 'Z' (if uppercase) and picks the first character not equal to original. Similarly for lowercase.

But in Python, generating the letters in order and checking for the first candidate.

But for uppercase, the code loops from 'A' to 'Z' in order. So for original_char 'A', the loop finds 'B' as the first candidate.

So the code should work.

Now, testing edge cases.

Edge case 1: original character is the same as desired_char.

E.g., original is 'T' (uppercase), lucky letter is 't'.

Then, desired_char is 'T', which is same as original. So replacement must be 'A' (the next lex smallest uppercase letter).

Another case: original is 'z' (lowercase), lucky is 'z'. So replacement is 'a' (the next lex smallest lowercase, 'a').

So code handles this.

Another edge case: when the original character is the first in the alphabet. For example, original is 'A' (uppercase). The next lex smallest is 'B'.

Another case: original is 'B' (uppercase). So in the loop, first candidate is 'A'.

So code would replace 'B' with 'A' (if lucky is 'B').

Wait, no. Let's see: if lucky is 'b', and original is 'B' (uppercase), desired_char is 'B' (uppercase). So desired_char is same as original. So code loops through 'A' to 'Z' in order. The first character not equal to 'B' is 'A', so replacement is 'A'.

So code would generate 'A'.

Which is correct.

Now, the code.

Putting it all together.

Read n, then read n forbidden substrings.

Then read w.

Then read the lucky letter.

Build the mask.

Then process each character.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    forbidden = [input_stream.readline().rstrip("\n").strip() for _ in range(n)]
    w = input_stream.readline().rstrip("\n").strip()
    letter = input_stream.readline().rstrip("\n").strip().lower()

    mask = [False] * len(w)

    for s in forbidden:
        s_len = len(s)
        s_lower = s.lower()
        for i in range(len(w) - s_len + 1):
            substring = w[i:i+s_len].lower()
            if substring == s_lower:
                for j in range(i, i + s_len):
                    if j < len(mask):
                        mask[j] = True

    result = []
    for i in range(len(w)):
        c = w[i]
        if mask[i]:
            original = c
            is_upper = original.isupper()
            desired = letter.upper() if is_upper else letter
            if desired != original:
                result.append(desired)
            else:
                if is_upper:
                    for ord_c in range(ord('A'), ord('Z') + 1):
                        candidate = chr(ord_c)
                        if candidate != original:
                            result.append(candidate)
                            break
                else:
                    for ord_c in range(ord('a'), ord('z') + 1):
                        candidate = chr(ord_c)
                        if candidate != original:
                            result.append(candidate)
                            break
        else:
            result.append(c)

    print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
hello
party
abefglghjdhfgj
IVan
petrsmatchwin
a
""",
            "output": \
"""\
petrsmatchwin
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

Another sample:

Input:

4

hello

party

abefglghjdhfgj

IVan

petrsmatchwin

a

Output:

petrsmatchwin

This is because none of the forbidden substrings occur in the original string. So mask is all False, no replacements. So the output is same as input.

Third sample:

Input:

2

aCa

cba

abAcaba

c

Output:

abCacba

Which the code handles as discussed.

Thus, the code should work.
</think>

```python
n = int(input())
forbidden = [input().strip() for _ in range(n)]
w = input().strip()
letter = input().strip().lower()

mask = [False] * len(w)

for s in forbidden:
    s_len = len(s)
    s_lower = s.lower()
    for i in range(len(w) - s_len + 1):
        if w[i:i+s_len].lower() == s_lower:
            for j in range(i, i + s_len):
                if j < len(mask):
                    mask[j] = True

result = []
for i, c in enumerate(w):
    if mask[i]:
        is_upper = c.isupper()
        desired = letter.upper() if is_upper else letter
        if desired != c:
            result.append(desired)
        else:
            if is_upper:
                for ord_c in range(ord('A'), ord('Z') + 1):
                    candidate = chr(ord_c)
                    if candidate != c:
                        result.append(candidate)
                        break
            else:
                for ord_c in range(ord('a'), ord('z') + 1):
                    candidate = chr(ord_c)
                    if candidate != c:
                        result.append(candidate)
                        break
    else:
        result.append(c)

print(''.join(result))
```
