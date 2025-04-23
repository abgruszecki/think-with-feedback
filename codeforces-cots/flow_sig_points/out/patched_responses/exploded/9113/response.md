<think>
Okay, let's tackle this problem. So, the task is to find the lexicographically next tolerable string after the given one. A tolerable string is one that doesn't have any palindromic contiguous substrings of length 2 or more. And each character must be among the first p letters of the alphabet.

First, I need to understand what the next lexicographical tolerable string is. The next string should be the smallest possible string that is larger than the given one and meets the tolerable conditions.

Let me think about how to approach generating the next string. The usual method for finding the next lex string is similar to incrementing a number. We start from the end, find the first position that can be incremented, increment it, and then set all following characters to the smallest possible values. But here, the constraints complicate things. After changing a character, we need to ensure that no two consecutive characters are the same (since that's a palindrome of length 2) and also check for longer palindromic substrings. Wait, wait, but the problem states that the string shouldn't have any contiguous palindrome of length 2 or more. So, the main constraints are:

1. No two consecutive characters can be the same. Because that's a palindrome of length 2.
2. Also, no longer palindromic substrings. For example, a three-character substring like aba is a palindrome of length 3, which is also invalid.

Wait, but wait, the problem says "contiguous substring of length 2 or more". So any contiguous substring of length ≥2 that is a palindrome. So even if it's longer than 2, like aba (3 characters), that's a palindrome and thus invalid. So the string must have no palindromic substrings of any length ≥2. Hmm, that's a bit more complicated.

So how to handle that? Because when building the next string, after changing a character, we need to check all possible palindromic substrings that might have been created.

Wait, but maybe there's a way to structure the problem such that checking for the two previous characters is sufficient. For example, if each new character added doesn't form a palindrome with the previous one or two. Because any longer palindrome would require that the current character matches one two steps back. Let's think: for example, in a string like 'abx...', when choosing x, we need to make sure that x is not equal to the previous character (b), and also not equal to the one before the previous (a), because then 'aba' would form a palindrome. Wait, no. 'abx'... if the current position is x, then if x is equal to a, then the substring 'aba' would be a palindrome. So in that case, when adding x, we have to check that x is not equal to the previous character (b) and not equal to the character two positions back (a). Because that would form a three-length palindrome.

Wait, but if we ensure that each character is not equal to the previous and the one before the previous, then all possible palindromic substrings longer than 2 would be avoided. Let me see:

Suppose for each position i >=2, the character at i is different from i-1 and i-2. Then, any substring of length 3 would be non-palindromic. Because the first and third characters would be different (since i-2 and i are different), so a 3-length substring can't be a palindrome. Similarly, for longer substrings, any palindrome of even length would require consecutive duplicates (like abba), but since consecutive characters can't be the same, those are already invalid. For odd lengths, say 5, the middle character would have to be the same as the ones symmetrically around it. But given that consecutive characters are all different, perhaps the checks for the previous two characters are sufficient.

So, perhaps the key here is that for each character in the string (after the first two), it must not be equal to the previous character (i-1) and also not equal to the character two positions back (i-2). Because if that's the case, then any possible palindrome of length ≥2 would be invalid. Let's verify:

If we have a substring of length 2: consecutive characters are not allowed to be the same. So that's handled by checking the previous character.

For a substring of length 3: to be a palindrome, the first and third characters must be the same. So if we ensure that each character is different from the one two positions back, then this can't happen.

For a substring of length 4: The entire substring must be a palindrome. For example, abba. But consecutive characters can't be the same, so the first two characters must be different. So abba can't exist. Similarly, any 4-length palindrome would require that the first two characters are the same as the last two in reverse. But since consecutive characters are all different, this is impossible. For example, abcd. To be a palindrome of length 4, it would need to be a d c b a, which can't happen because consecutive characters are different.

Therefore, the conditions for a tolerable string are:

For each position i (starting from 0):

- s[i] != s[i-1] (prevents 2-length palindromes)
- if i >= 2: s[i] != s[i-2] (prevents 3-length palindromes)

If these two conditions are met for all positions, then the string is tolerable.

Because:

- Any even-length palindrome would require at least two consecutive same characters (like in the middle), which is forbidden.
- Any odd-length palindrome of 5 would require that the third character (middle) is same as the first and fifth, but the first and third would have been checked when the third character was placed.

Wait, perhaps I need to think more carefully. Let's consider a 5-length substring. Suppose the string is abcba. Then, the middle character is c, first is a, fifth is a. But in this case, the fifth character is a, which would have to be different from the fourth (b) and the third (c). So the fifth a would have to not equal the fourth (b) which is okay, and not equal to the third (c). But in this case, the fifth a is equal to the third character two positions back (the third character is c, so fifth is a, which is okay). Wait, the fifth character is two positions back from the third. Wait, no: position i=4 (0-based) is the fifth character. The third character is i=2. So two positions back from i=4 is i=2, which is c. So the fifth character a is different from c. So this abcba string would be allowed? But the entire substring is a palindrome of length 5. Oh no! So the approach of checking only the previous two positions is insufficient in this case.

Wait, that's a problem. Because according to the previous checks, the fifth character a is different from the fourth (b) and different from the third (c), so it's allowed. But then, the substring positions 0-4 (abcba) is a palindrome of length 5. Which violates the problem's conditions.

So this approach is wrong. Therefore, the initial idea of checking only the previous two positions is not sufficient to prevent longer palindromic substrings.

Hmm, this complicates things. So how do we ensure that no such palindromic substrings exist?

Wait, the problem requires that there are no contiguous palindromic substrings of length ≥2. So even a 5-length palindrome is invalid. So how can we check for that?

But checking every possible substring is O(n^2), which for n up to 1000 would be 1e6 operations. But in the problem's solution, for each possible candidate string (when we increment characters), we need to verify that it's tolerable. But how?

But that's going to be time-consuming. So for the problem of generating the next string, perhaps we can find a way to build the next string incrementally, ensuring that each step's choices avoid creating palindromic substrings.

Alternatively, perhaps the only possible way to have a longer palindromic substring is if there's a three-character or two-character palindrome. So maybe the problem can be reduced to checking the two and three-length palindromes. Let's think: if there are no two or three-length palindromes, then there can't be longer ones.

Wait, for example, consider a four-length palindrome like abba. But since consecutive characters can't be the same, the first two letters (a and b) are different, but the third is b, which is same as the second. But that's a two-length palindrome (bb), which is invalid. So in the presence of the two and three-length checks, longer palindromes would automatically be invalid.

Wait, perhaps if all consecutive characters are different (so no two-length palindromes) and no three-length palindromes, then longer palindromes can't exist. Let's see.

Assume that in the string, all consecutive characters are different, and no three consecutive characters form a palindrome (i.e., for any three consecutive characters, the first and third are different). Then, can there be a four-length palindrome?

A four-length palindrome would have the form abba. But the third and fourth characters are 'b' and 'a', which are different, but the third and second characters are 'b' and 'b' which are the same. But that would be a two-length palindrome. Since consecutive characters are different, this can't happen. So the four-length palindrome can't exist.

Similarly, a five-length palindrome like abcba. The third character is c. The first and fifth are a. The second and fourth are b. So the consecutive characters are a, b, c, b, a. The consecutive pairs are all different. But the three-length substring 'bcb' is a palindrome. Wait, no: 'bcb' is a palindrome of length three. But according to our initial checks, each character must be different from the one two positions back. So in the third position (c), it's different from the first (a). In the fourth position (b), it's different from the second (b) — wait, no. The fourth position (b) is two positions back from the second (b). So the fourth character is b, which is same as the second (b). So that would be a problem. So 'b' in position 3 (zero-based) would have to check that it's not equal to position 1. So if our checks are that each character is different from the previous and the one before that, then this case would be prevented.

So, in order to form a five-length palindrome, we need that the third character is same as the first, but that would have been checked when the third character was added. So perhaps, as long as each character is different from the previous one and the one two positions back, then all palindromic substrings are avoided.

Wait, let's see. For the example of abcba:

Positions 0: a, 1: b, 2: c, 3: b, 4: a.

At position 3 (b), the previous character is c (position 2), which is different. The one two positions back is position 1 (b). So the third character (b) is equal to position 1's character. So when placing the third character, we check that it's not equal to position 1 (which it is), so this would be invalid. Therefore, the third character can't be placed as 'b' in this scenario.

Therefore, the approach of checking the previous character and the one two positions back for each character would prevent all possible palindromic substrings of length ≥2.

So the rules for a tolerable string are:

For each i (0-based) in the string:

1. i >= 1: s[i] != s[i-1]
2. i >= 2: s[i] != s[i-2]

If these two conditions are satisfied for all possible i, then the string is tolerable.

Because:

- No two consecutive characters are the same, so no two-length palindromes.
- No three-length palindromes because the first and third characters are different.
- For longer substrings: Any even-length palindrome would require that the middle two characters are the same (since even length). But consecutive characters are all different, so even-length palindromes can't exist.
- Any odd-length palindrome longer than 3 would require that the first and last characters are the same, but the characters two steps away would have to be same. But in the process of building the string, each character is checked against two positions back, so that would not be allowed.

Therefore, the two rules are sufficient to ensure that the string is tolerable.

So, the problem reduces to generating the next string that is larger than the given one, satisfies these two conditions, and uses the first p letters of the alphabet.

Now, how to generate the next string.

The approach is similar to incrementing a number, but with constraints. We need to find the smallest possible string that is larger than the given one and meets the conditions.

Let's think of the string as a list of characters. We can start from the end of the string and try to increment the character, ensuring that the new character doesn't conflict with the previous two characters. Once we find a position where we can increment the character, we set that character to the next possible value and then fill the remaining positions (to the right) with the smallest possible characters that satisfy the constraints.

The steps would be:

1. Iterate over each character from the end to the start of the string.
2. For each position i, try to find the smallest possible character greater than the current s[i], such that it is different from s[i-1] (if i>0) and s[i-2] (if i>1).
3. Once such a character is found, set s[i] to that character and then generate the smallest possible characters for the positions i+1 to n-1, ensuring that each of those characters is the smallest possible (to minimize lex order) and satisfies the two constraints (not equal to previous and two before).
4. If such a character is found and the remaining positions can be filled, return the resulting string. Otherwise, continue to the previous position.

The key is to find the earliest position where we can increment the character, then fill the rest with the minimal possible values under constraints.

But how to efficiently generate the remaining characters after position i.

For each position j > i, the character must be the smallest possible (to minimize lex order) such that it is not equal to s[j-1] (the previous character) and s[j-2] (if j >= 2). So for each j >= i+1:

- The character can be the smallest possible in the first p letters (a, b, ...), but not equal to the previous character (s[j-1]) and not equal to the character two positions back (s[j-2], if j-2 exists).

But since the minimal lex order is desired, we can iterate through the possible candidates for each position starting from 'a' and pick the first one that satisfies the constraints.

Let's consider an example.

Original string: cba, p=4 (as in the second example). The next possible is cbd.

So the process would be:

Check the last character 'a'. Try to find a character larger than 'a' (current is 'a'). The next possible is 'b', but check constraints. The previous character is 'b' (second character in 'cba'). So can't use 'b' (since it's same as previous). Next is 'c', which is allowed. But the previous character is 'b' (so 'c' is different), and two positions back (if applicable) is 'c' (third character in 'cba' is 'a', so j=2: two positions back is j-2=0, which is 'c'. So for j=2, the character must not be equal to s[0] (c) and s[1] (b). So possible options are a (but a is smaller than current a, but we need to find a character larger than the original. Wait, the original is 'a' in position 2. We are trying to increment it. So possible characters are b, c, d (since p=4). But the previous character is 'b', so cannot be b. Two positions back is 'c' (position 0). So the new character can't be c or b. So possible options are a (but a is the original, and we need larger) and d. So the next possible is d. So set position 2 to 'd'. So the new string is 'cbd', which is valid.

So this works.

Another example: abcd, p=4. The next string is abda.

Original string is a b c d. Check from the end. The last character is d. Try to find a larger character (but p=4, so the max is 'd'). So no. Move to position 3 (d). Can't change. Then position 2 (c). Try to find next character. The current is c. Next possible is d. Check constraints: previous character is b. So d is allowed. Also, two positions back is a. So d is allowed. So set position 2 to d. Then, for position 3 (previously d), we need to set the smallest possible character that is not equal to d (previous) and not equal to position 1 (b). So possible characters are a (since a is the smallest). Check: a is not equal to d (prev) and not equal to b (two positions back). So yes. So the new string is a b d a. Which is abda. Which is valid.

So the approach is:

For each position i starting from the end:

- Find the next possible character greater than s[i], such that it is not equal to s[i-1] (if i>0) and not equal to s[i-2] (if i>1).

Once such a character is found, set s[i] to that character, and then for positions i+1 to end, choose the smallest possible characters that satisfy the constraints.

If this is possible, return the new string. Otherwise, continue to the next position to the left.

The challenge is to efficiently find the next possible character for position i, and then generate the remaining characters.

So, let's outline the steps in code:

1. Convert the input string to a list for easy manipulation.

2. Iterate from the end of the list towards the start (from i = n-1 downto 0).

3. For each i, find the next possible character that is larger than the current s[i], and is within the first p letters. The next possible character should be the smallest possible that is larger than s[i], but not equal to s[i-1] (if i>0) and not equal to s[i-2] (if i>1).

4. For the found character, check if any of the previous positions (i-1 and i-2) exist. For example, if i is 0, then we only check that the new character is within p letters. Wait, no: for i=0, the new character can be any larger than current, as there's no i-1 or i-2. So for i=0, the new character just needs to be within the first p letters and larger than current. Then, the rest of the positions (from 1 to end) need to be filled with the minimal possible characters, ensuring that each is not equal to previous and two before.

Wait, but in the case of i=0, after changing it, the next positions (1, 2, etc.) need to be filled with minimal characters, ensuring that each position's character is not same as previous and two before.

So for example, if i=0 is changed to 'b', then for position 1, the character must be the smallest possible (a) but not equal to 'b' (previous). So a is allowed. For position 2, it must be different from position 1 (a) and position 0 (b). So the minimal is 'c', but perhaps 'a' is allowed if possible. Wait, no: for position 2, the constraints are:

- s[2] != s[1] (a)
- s[2] != s[0] (b)

So possible options are c, d, etc. The smallest possible is 'c'.

So the code for filling the remaining positions after i must generate each position's character as the smallest possible allowed by the constraints.

So, for each position j > i:

- The character must be as small as possible (starting from 'a').
- The character must not be equal to s[j-1] (previous character).
- If j >= 2, it must also not be equal to s[j-2].

So, the code for generating the remaining characters after i is:

for j in i+1 to n-1:
    for c in 'a' to p-1 (as a character):
        if c != s[j-1] and (j < 2 or c != s[j-2]):
            s[j] = c
            break
    else:
        # no possible character found, backtrack
        return failure

But how to handle this in code. For each j from i+1 to the end, we need to find the smallest possible character (starting from 'a') that is not equal to the previous character and (if j >= 2) not equal to the one two positions back.

If at any j, there is no such character, then the entire process fails, and we need to backtrack further.

So the steps in code would be:

Attempt to increment each possible position i from the end. Once an i is found where a new character can be chosen that is larger than the original and satisfies the constraints, then attempt to fill the remaining positions with the minimal possible characters. If filling is possible, return the new string. Otherwise, proceed to check previous positions.

But how to check if filling is possible. For example, after changing position i, can the rest of the positions be filled according to the constraints. Because if not, then even changing i might not lead to a valid solution.

But given that the original string is valid, and we're trying to find the next lex string, perhaps once i is found, the rest can be filled as the minimal possible. However, if during filling, for some j, there's no possible character that satisfies the constraints, then even after changing i, the rest of the string can't be filled, so this i is invalid, and we need to backtrack.

But how to handle this.

This suggests that when we find a possible candidate for i, we need to try to fill the rest of the string. If it's possible, then return the new string. If not, continue to check previous i's.

But for n=1000, this could be time-consuming if done naively, but given that the problem constraints allow n up to 1000, and each step is O(p) per character, it's manageable.

So, in code:

We loop i from the end to the start.

For each i:

- Determine the starting character to check. It should be the next character greater than s[i]. Also, when checking possible characters, they must be within the first p letters (so 'a' to 'a' + p -1).

But the current s[i] is a character. We need to find the smallest possible character c that is larger than s[i], and such that:

c != s[i-1] (if i > 0)

c != s[i-2] (if i > 1)

Additionally, for the new c, we need to check these constraints.

Once such a c is found, we set s[i] to c, and then proceed to fill the rest of the positions (i+1 to n-1) with the minimal possible characters.

To fill the rest:

For each j from i+1 to n-1:

- For each possible character starting from 'a' up to 'a' + p-1:

   - Check that it's not equal to s[j-1]

   - Check that if j >=2, it's not equal to s[j-2]

   - The first such character found is selected.

   - If none found, then this path is invalid, so break and continue to the next possible i.

If all positions are successfully filled, then return the new string.

Otherwise, proceed.

Now, the question is how to efficiently implement this.

First, the code will need to handle the original string as a list of characters. Let's see.

In Python, strings are immutable, so converting to a list is better.

So, s = list(input().strip())

Then, n and p are read.

The algorithm steps:

For i in reversed(range(n)):

   current_char = s[i]

   # Find the next possible character greater than current_char, within 'a' to 'a' + p-1.

   # Also, the new character must not conflict with previous characters.

   # Possible candidates are all characters > current_char, up to 'a' + p-1.

   # Check for each possible c in order from current_char + 1 to 'a' + p-1:

   for c_code in range(ord(current_char) + 1, ord('a') + p):

       c = chr(c_code)

       # Check constraints for i.

       # If i > 0, check that c != s[i-1]

       # If i > 1, check that c != s[i-2]

       valid = True

       if i > 0 and c == s[i-1]:

           valid = False

       if i > 1 and c == s[i-2]:

           valid = False

       if valid:

           # Now, we can set s[i] to c.

           # Now, try to fill the rest of the string from i+1 onwards.

           # For each j from i+1 to n-1, select the smallest possible character that satisfies constraints.

           new_s = s[:i] + [c]

           valid_fill = True

           for j in range(i+1, n):

               # For j, find the smallest possible character.

               # Constraints for j's character:

               # 1. Not equal to previous (new_s[j-1])

               # 2. If j >=2 (relative to new_s), not equal to new_s[j-2]

               # Because new_s is built up to j-1, we can check.

               prev1 = new_s[j-1] if (j-1) >=0 else None

               prev2 = new_s[j-2] if (j-2) >=0 else None

               for candidate_code in range(ord('a'), ord('a') + p):

                   candidate = chr(candidate_code)

                   # Check constraints.

                   # prev1 is new_s[j-1]

                   if candidate == prev1:

                       continue

                   if j >=2 and candidate == prev2:

                       continue

                   # valid candidate.

                   new_s.append(candidate)

                   break

               else:

                   # No candidate found.

                   valid_fill = False

                   break

           if valid_fill:

               # Now, check if the new string is valid.

               # Wait, but according to the filling process, each character is chosen to satisfy the constraints, so the entire string is valid.

               # So, return the new string.

               return ''.join(new_s)

   # If any of the c's were possible and filling succeeded, then we have already returned.

# After checking all i's, if none found, return 'NO'

But wait, after setting s[i] to c, the new_s is s[:i] + [c], and then for j from i+1 to n-1, we append the minimal possible characters. So after i, the rest of the positions are filled in a way that each new character is the smallest possible that meets the constraints.

But how to handle the case where after setting i to c, the next positions may have dependencies that are not just on the previous one and two steps back. For example, if j is i+1, then the previous characters are i and i-1 (if j is i+1 >=2, then j-2 is i-1). So in that case, the code above checks for j-1 (i) and j-2 (i-1) if applicable.

Yes. So the code for filling is correct.

But in the code above, when building new_s, for each j starting from i+1, we check the previous two characters (if applicable). So the code will generate the minimal possible characters for the rest of the positions, ensuring that each new character doesn't conflict with the previous one or two steps back.

Therefore, the filling process should generate a valid string.

But we need to make sure that during the filling, for each j, there's at least one possible character that can be chosen.

If during the filling, for some j, no character is possible (i.e., all p letters are invalid), then the current i is invalid, and we need to backtrack.

So, in code, the 'valid_fill' variable is set to False if any j can't find a valid candidate. Then, we proceed to check other possible c's for the current i.

But in the code above, for each i, once a valid c is found, and the filling process succeeds, we return the string immediately. Otherwise, continue.

Now, considering that the original string is valid, and we are looking for the next lex string, the code should work.

Now, let's test this approach against the sample inputs.

Sample Input 2:

3 4

cba

Original string is ['c', 'b', 'a'].

Loop i from 2 downto 0:

i=2:

current_char is 'a'. Next possible characters are 'b', 'c', 'd' (since p=4).

Check 'b':

i=2, which is >0. Check if 'b' != s[i-1] (s[1] is 'b'). So 'b' equals 'b' → invalid.

Check 'c' → i-1 is 'b', so 'c' is valid. i-2 is 0, s[0] is 'c'. So check if 'c' != 'c' → no. So 'c' is invalid.

Check 'd' → compare to s[i-1] (b) → valid. Compare to s[i-2] (c) → valid. So 'd' is valid.

Set new_s to ['c', 'b', 'd']? Wait, no. i is 2. So new_s is s[:i] + [c] → s[:2] is ['c', 'b'] → adding 'd' → ['c','b','d']. Then, for j=3? Wait, the original n is 3. So j starts at i+1 =3, which is beyond the list. So no more positions to fill. So the new string is 'cbd' → which is the correct sample output.

Another sample:

Input 3:

4 4

abcd → output abda.

Original string is ['a','b','c','d'].

Check i from 3 downto 0.

i=3: current_char is 'd'. p=4, so next possible is up to 'd' (since 'a' +4-1= 'a'+3= 'd'). No larger character. So move to i=2.

i=2: current_char is 'c'. Next possible characters: 'd' (since 'c' +1 is 'd').

Check 'd':

Constraints: i=2 >0. Check s[i-1] (s[1] is 'b') → 'd' is not equal to 'b'. Check s[i-2] (s[0] is 'a') → 'd' is not equal. So valid.

Set new_s to s[:2] + ['d'] → ['a','b','d'].

Now fill j=3:

j=3, new_s so far is ['a','b','d'].

Check for j=3 (index 3, 0-based). Previous character is 'd' (new_s[2]). Two positions back is new_s[1] ('b').

Find the smallest possible character (a) that is not equal to 'd' and not equal to 'b'.

a is allowed. So append 'a'. The new string is 'abda', which is the sample output.

So the code works.

Another sample where the output is NO:

Sample 1:

3 3 → cba.

Check i=2: current 'a' can be incremented to 'b' (but check constraints).

i=2, previous is 'b' (s[1] is 'b'). So 'b' is same as previous → invalid.

Next possible is 'c'. i-1 is 'b' → okay. i-2 is s[0] 'c'. So 'c' is same as s[i-2] (c) → invalid. So no possible c for i=2.

Then i=1: current is 'b'. Looking for next character > 'b' → 'c'.

Check constraints: i=1. Previous character is s[0] 'c'. So 'c' is same as previous → invalid. Next possible is 'd' → but p=3, so max is 'c'. So no options.

i=0: current 'c'. Looking for next character > 'c' → but p=3, 'a', 'b', 'c'. So no possible.

Thus, output is NO.

So the code works.

Now, the code's time complexity. For each position i, we check up to (p) possible characters. For each valid c, we then fill the rest of the string. Filling the rest takes O(n) steps, each with O(p) operations. So the total time is O(n * p + n * p * (n)). So for n=1000, and p=26, this would be 1000 * 26 * 1000 = 26,000,000 operations. Which is acceptable for 1 second (assuming Python can handle around 1e8 operations per second, which is not quite, but 2.6e7 is manageable).

But perhaps there's a way to optimize.

But given the constraints (n up to 1000), and the problem's time limit (1 sec), the code should pass.

Now, let's code this.

First, read n and p.

Then, read the string.

Convert to a list.

Then, iterate i from the end.

For each i, check possible characters.

Once a possible c is found, try to fill the rest.

If filling is possible, output the result.

Else, continue.

If no i found, output 'NO'.

Now, let's code this.

Handling the filling process correctly.

In the code:

For i in reversed(range(n)):

   original_char = s[i]

   for c in possible characters greater than original_char:

       check if c is allowed (i constraints).

       if allowed:

           temp list is s[:i] + [c]

           then fill from i+1 to end.

           for each j in i+1 to n-1:

               find the smallest possible character for j that is not equal to previous and two before.

               if found, add to temp list.

               else, break.

           if all filled:

               output the temp list as string.

               exit.

So, code in Python:

n, p = map(int, input().split())
s = list(input().strip())

found = False
for i in reversed(range(n)):
    current_char = s[i]
    # Generate possible next characters for this position.
    start = ord(current_char) + 1
    end = ord('a') + p -1
    for c_ord in range(start, end +1):
        c = chr(c_ord)
        # Check constraints for position i.
        # i must not be equal to i-1 and i-2.
        valid = True
        if i > 0 and c == s[i-1]:
            valid = False
        if i > 1 and c == s[i-2]:
            valid = False
        if valid:
            # Now, try to build the rest of the string.
            new_s = s[:i] + [c]
            # Fill the rest of the characters from i+1 to n-1.
            possible = True
            for j in range(i+1, n):
                # Find the smallest possible character for new_s[j].
                # prev1 is new_s[j-1], prev2 is new_s[j-2] if j >=2.
                prev1 = new_s[j-1]
                prev2 = new_s[j-2] if j-2 >=0 else None
                for candidate_ord in range(ord('a'), ord('a') + p):
                    candidate = chr(candidate_ord)
                    if candidate == prev1:
                        continue
                    if prev2 is not None and candidate == prev2:
                        continue
                    # Valid candidate.
                    new_s.append(candidate)
                    break
                else:
                    # No candidate found.
                    possible = False
                    break
            if possible:
                print(''.join(new_s))
                exit()
    # If any of the c's worked, we would have exited already.
# After all i's, no solution.
print("NO")

Let's test this code against the samples.

Sample 2:

3 4 → cba.

The code loops i=2:

current_char is 'a'. start is ord('a')+1=98, end is ord('a')+3=100 (i.e., 'd').

Check c_ord from 98 to 100:

c_ord 98: 'b'.

Check valid: i=2. i>0 → check if 'b' == s[1] ('b') → yes. So invalid.

c_ord 99: 'c' → check s[1] ('b') → okay. Check s[0] ('c') → 'c' == 'c' → invalid.

c_ord 100: 'd' → check s[1] ('b') → okay. Check s[0] ('c') → okay. So valid.

Now, new_s is s[:2] + ['d'] → s[:2] is ['c', 'b'] → new_s is ['c', 'b', 'd'].

Then, j starts from 3 (since n=3), so loop doesn't run. So possible is True.

Print 'cbd' → correct.

Sample 3:

4 4 → abcd.

i=3: current_char 'd' → next possible is none (max is 'd'). So move to i=2.

current_char 'c' → next possible is 'd'.

Check i=2:

s[1] is 'b' → 'd' != 'b' → okay.

s[0] is 'a' → 'd' != 'a' → okay. Valid.

new_s is ['a','b','d'].

Now fill j=3:

prev1 is 'd' (new_s[2]), prev2 is new_s[1] ('b').

Find the smallest candidate.

Check 'a' → not equal to 'd' and 'b' → valid. So append 'a'. new_s becomes ['a','b','d','a'].

Which is abda. Correct.

Sample 1:

3 3 → cba.

Check i=2:

possible characters after 'a' are 'b' and 'c' (p=3).

For 'b':

i=2, check s[1] ('b') → same as 'b' → invalid.

For 'c':

check s[1] ('b') → okay. check s[0] ('c') → same → invalid.

So no valid c for i=2.

i=1: current 'b'.

possible chars after 'b' are 'c'.

Check constraints: i=1.

Check s[0] ('c') → 'c' == 'c' → invalid.

So no valid c.

i=0: current 'c'. possible chars after 'c' → none (p=3 → 'a', 'b', 'c'). So no.

Thus, output 'NO'.

So code works.

Another test case:

n=1, p=1 → string 'a'. Output is NO, since no next character.

n=1, p=2 → string 'a' → next is 'b'.

But check constraints: no palindrome possible. So output 'b'.

Yes.

Another test case:

n=2, p=2 → s is 'ab'.

Possible next:

i=1: current 'b' → next is 'c' but p=2 → no. So next possible is none. So try i=0: current 'a' → next is 'b'. Then, fill i=1:

must be != 'b' (from i=0) → but p=2: possible is 'a'. So new string is 'ba' → but 'ba' is valid. So output 'ba'.

Yes.

Thus, the code should handle these cases.

So, the code seems correct.
</think>

```python
n, p = map(int, input().split())
s = list(input().strip())

for i in reversed(range(n)):
    current = ord(s[i])
    start = current + 1
    end = ord('a') + p - 1
    for c_ord in range(start, end + 1):
        c = chr(c_ord)
        valid = True
        if i > 0 and c == s[i-1]:
            valid = False
        if i > 1 and c == s[i-2]:
            valid = False
        if valid:
            new_s = s[:i] + [c]
            possible = True
            for j in range(i+1, n):
                prev1 = new_s[j-1]
                prev2 = new_s[j-2] if j >= 2 else None
                found_char = False
                for cand_ord in range(ord('a'), ord('a') + p):
                    cand = chr(cand_ord)
                    if cand != prev1 and (prev2 is None or cand != prev2):
                        new_s.append(cand)
                        found_char = True
                        break
                if not found_char:
                    possible = False
                    break
            if possible:
                print(''.join(new_s))
                exit()
print("NO")
```