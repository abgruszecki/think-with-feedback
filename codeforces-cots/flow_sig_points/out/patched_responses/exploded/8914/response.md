<think>
Okay, I need to solve this problem where I have to check if a new login is similar to any existing ones based on certain transformation rules. Let's see the problem statement again to make sure I understand it correctly.

The problem says two logins are similar if you can transform one into the other using a sequence of operations. The allowed operations are:

1. Changing lowercase to uppercase and vice versa. So case doesn't matter here. For example, 'a' and 'A' are considered the same in this context.
2. 'O' and '0' can be interchanged. So any 'O' in the string can be replaced with '0' and vice versa.
3. '1', 'l' (lowercase L), and 'I' (uppercase i) can be interchanged. So any of these three characters can be replaced with any of the others.

So, the main idea is that when comparing two logins, each character in one must be compatible with the corresponding character in the other, considering these transformations. Also, the lengths must be the same, because transformations don't add or remove characters.

So the approach is: for the new login, generate a normalized version where each character is replaced with a canonical form based on the transformation rules. Then, check if any existing login's normalized form matches the new one's. If any do, then the answer is "No"; otherwise, "Yes".

But how to normalize each character? Let's think:

For each character in the login, we need to map it to a base character that represents all possible variations. For example:

- For case insensitivity: convert all letters to lowercase (or uppercase).
- For 'o' and '0', map both to the same base (maybe '0'? Or 'o'? Maybe choose one as the canonical form.)
- For '1', 'i', 'l', map all to the same base.

So the steps for normalization would be:

1. Convert all characters to lowercase (to handle case insensitivity).
2. Replace 'o' with '0' (or vice versa, but which one? Maybe replace 'o' with '0' since 'O' was part of the original problem's example).
Wait, but in the problem statement, the allowed transformations are between 'O' (uppercase) and '0'. Wait, does the case matter for the 'O' here? Because the first transformation allows changing lowercase and uppercase letters. So for example, if the original is 'o' (lowercase), it can be changed to 'O' (uppercase), which can then be changed to '0'. So perhaps all 'o's (regardless of case) and '0's should be mapped to the same character in the normalized form.

Wait, the first transformation allows changing any lowercase letters to uppercase and vice versa. So case is irrelevant. So during normalization, we can first convert all letters to lowercase. Then, in the normalized form, 'o' (lowercase) would be converted to '0'. Wait, but according to the transformation rules, 'O' (uppercase) can be transformed into '0' and vice versa. So when we normalize, all 'O's (after case conversion to lowercase) become 'o's, but then need to be mapped to '0's. Hmm. Or maybe when converting to lowercase, we first make all letters lowercase. Then, in the normalized string, replace any 'o' (lowercase) with '0', and any '0's stay as '0's. Then, for '1's, 'i's (lowercase?), and 'l's (lowercase), replace them all with a single base character, like 'l' or '1'.

Wait, the third transformation allows changing '1' to 'l' (lowercase) or 'I' (uppercase), and vice versa. So for normalization, after converting to lowercase, 'i' becomes 'i', but since 'I' becomes 'i' (after lowercasing), but according to the rules, 'i' (uppercase) can be transformed into '1' or 'l'. Wait, no: the third rule says that '1' can be changed to any of 'l' (lowercase L), 'I' (uppercase i), and vice versa. So the allowed transformations are between '1', 'l', and 'I'. So when normalizing, any of these three characters (regardless of case?) should be mapped to a single base.

Wait, but let's clarify:

The third transformation allows changing digit '1' to any of the letters 'l' (lowercase), 'I' (uppercase), and vice versa. So for example, if a character is 'l' (lowercase), it can be changed to '1' or 'I' (uppercase), etc. So during normalization, we need to treat all of these as the same. So, in the normalized form, any of '1', 'i', 'l' (regardless of case?) are replaced with the same character.

Wait, but when we lower the case, 'I' becomes 'i', which is different from 'l' lowercase. So maybe during normalization, after converting to lowercase, replace 'i' and 'l' to '1'? Or maybe replace all occurrences of '1', 'i', 'l' (lowercase) with a single base character, say '1'.

Wait, perhaps the steps for normalization are:

1. Convert all characters to lowercase.

2. For each character:
   a. if it is 'o', replace with '0'.
   b. if it is 'i' or 'l', replace with '1'.
   c. leave other characters as is.

So, after this process, any two characters that are considered equivalent under the transformation rules would map to the same normalized character.

Let me test this with some examples.

For example, the first sample input:

Existing logins are '2_wat' and 'wat_1'. The new login is '1_wat'.

Normalize the new login '1_wat':

Each character:

'1' → becomes '1' (since 1 is already in the set of 1, i, l). So '1' → '1'.

'_' remains.

'w' → lowercase, remains.

'a' → lowercase, remains.

't' → lowercase, remains.

So normalized is '1_wat'.

Existing logins:

First existing is '2_wat' → normalized as '2_wat' (since no o, 0, i, l, 1).

Second existing is 'wat_1' → normalize each character:

'w' → 'w', 'a' → 'a', 't' → 't', '_', '1' → '1'. So normalized 'wat_1'.

So the new login's normalized is '1_wat', which doesn't match any existing's normalized forms (which are '2_wat' and 'wat_1'). So output is yes.

Which matches the first sample.

Another example: third sample input.

New login is '_i_'.

Existing logins include '_1_'.

Normalizing '_i_': after step 1, lowercase all letters. The 'i' is lowercase. So step 2b replaces 'i' with '1'. So normalized is '_1_'.

Existing login '_1_' → normalized is '_1_'. So they match. So output no.

Yes, which matches the third sample.

Another example: the second sample input. New login is '000' (three zeros). Existing includes 'oOo' (third existing login). Let's normalize 'oOo':

Convert to lowercase: 'ooo'. Then replace 'o's with '0's → '000'. So the normalized version is '000', same as the new login's normalized (since new login is '000', which becomes '000' after normalization). So they match. Hence output is no.

Which matches the second sample.

So the plan is:

For each existing login, and the new login, generate their normalized versions. Then check if any existing normalized matches the new's normalized.

If any do, output 'No'; else, 'Yes'.

So the steps for the code:

1. Read the new login s.

2. Read n existing logins.

3. For each existing login, normalize it and store in a set.

4. Normalize the new login s and check if it's present in the set. If yes, output 'No'; else, 'Yes'.

But wait, the problem says that existing logins are already not similar to each other. So each existing login's normalized version must be unique. Because the problem states that no two existing logins are similar. So when we normalize all existing logins, their normalized versions must all be distinct. But in our code, we can ignore that, as we just need to check the new normalized against all existing normalized.

So the code structure will be:

Read s.

Read n.

existing = set()

for each of the n logins:

    normalized = normalize(login)

    add to existing set.

normalize the new s and check if it's in existing.

If yes, output No; else Yes.

So the key part is the normalize function.

Implementing the normalize function.

Let's define the normalization steps:

For each character in the input string:

- Convert to lowercase.

- Then:

   if the character is 'o' → replace with '0'.

   else if the character is 'i' or 'l' → replace with '1'.

   else if the character is '1' → leave as '1'.

   else, leave as is.

Wait, but after converting to lowercase, any uppercase letters are lowercase. Then:

For example, 'O' becomes 'o', which is then replaced with '0'.

Similarly, 'I' becomes 'i', which is then replaced with '1'.

'L' becomes 'l', which is replaced with '1'.

'1' remains '1'.

Other characters (like digits 2-9, '_', letters not in o, i, l) remain as is.

So the normalize function can be implemented as follows:

def normalize(s):

    res = []

    for c in s:

        lower_c = c.lower()

        if lower_c == 'o':

            res.append('0')

        elif lower_c in ['i', 'l']:

            res.append('1')

        else:

            res.append(lower_c)

    # Then handle '1'?

Wait wait. Wait, after converting to lowercase, the code checks if the character is 'o', in which case it becomes '0'. Then, if it's 'i' or 'l', becomes '1'. Otherwise, append the lowercase character. But wait, what about the original '1'? For example, if the character is '1', after lowercasing (it's already a digit, so lowercasing does nothing), then since it's not 'o', nor 'i' or 'l', we just append '1' as is. So that's correct.

So the code for normalize would process each character as:

For each character in the input string:

1. Convert to lowercase.

2. If it's 'o', replace with '0'.

3. Else if it's 'i' or 'l', replace with '1'.

4. Else, leave as is.

So the function would correctly map 'O', 'o' to '0'; 'I', 'i', 'L', 'l' to '1'; and '1' remains as '1'.

So the normalize function is correct.

Once that's done, the code can proceed as:

Read the new login s.

Compute s_normalized = normalize(s).

Then read n existing logins, compute their normalized versions, and collect them into a set. Then check if s_normalized is in the set.

If yes → output 'No', else 'Yes'.

Now, for the code structure.

Read s:

s = input().strip()

n = int(input())

existing = set()

for _ in range(n):

    login = input().strip()

    normalized = normalize(login)

    existing.add(normalized)

s_norm = normalize(s)

if s_norm in existing:

    print("No")

else:

    print("Yes")

Now, implement the normalize function.

In Python, the normalize function can be written as a helper function.

But how to make it efficient? The constraints are n up to 1000, and each login up to length 50, which is manageable.

So code for normalize:

def normalize(s):

    normalized = []

    for c in s:

        lower_c = c.lower()

        if lower_c == 'o':

            normalized.append('0')

        elif lower_c in ('i', 'l'):

            normalized.append('1')

        else:

            normalized.append(lower_c)

    return ''.join(normalized)

Testing this function:

Test case 1: 'Codeforces' → normalize:

Each character:

C → c (lowercase) → not o, i, l → append 'c'

o → o → becomes '0'

d → d → append 'd'

etc. So 'Codeforces' becomes 'c0def0rces' ?

Wait, let's see:

Original 'Codeforces' is C O D E F O R C E S.

Lowercase each: c o d e f o r c e s.

Then:

o → 0, o → 0.

So normalized becomes c0d e f 0 r c e s → 'c0def0rces'.

Which would match 'codef0rces' (from the first sample's example) when normalized. Let's see.

Original 'codef0rces' → lowercase is same as original (since it's lowercase except 0). Then, o is 0, but in this case, the original is codef0rces. So when normalized, 'c o d e f 0 r c e s' → the 'o' becomes '0', but the '0' is already 0. So the normalized would be 'c0def0rces' → same as the other. So the two are considered similar.

Yes, which matches the first example's explanation.

Another example: 'La0' (from one of the test cases). Let's normalize it.

Original is 'La0'.

Lowercase each: 'l a 0'.

Then:

'l' → '1'

'a' → 'a'

'0' → '0' (since lower_c is '0' → not o, etc.

So normalized becomes '1a0'.

Now, existing logins in the sample include 'La1' → normalized as '1a1' (La1 → lowercase is 'la1'; l becomes 1, a is a, 1 is 1. So '1a1'.

But the new login's normalized is '1a0', which doesn't match any of the existing normalized versions. Wait, but the sample input 4's output is 'No'. Let me check:

Sample input 4:

New login is 'La0'.

Existing logins are '2a0', 'La1', '1a0'.

Normalizing each:

- '2a0' → 2a0 → 2a0 (no o, i, l). So normalized is '2a0'.

- 'La1' → la1 → l becomes 1, a is a, 1 is 1 → '1a1'.

- '1a0' → 1a0 → 1 is 1, a is a, 0 is 0 → '1a0'.

So the new login's normalized is '1a0', which exists in existing (third login). So output is 'No'.

Which matches the sample input 4's output.

So the code handles that correctly.

Another sample: input 5 where the new login is 'abc' and the existing is 'aBc'. The normalized version of 'aBc' is 'abc' (lowercase → 'abc', no o, i, l → same as original. So new login's normalized is 'abc' which is same as existing's normalized. So output is 'No'.

Which matches sample 5.

So the code works.

Now, let's code this.

But in Python, the function needs to be efficient, but given the constraints (n=1000, each string 50 chars), even O(n*m) is manageable.

So the code:

Read s, then read n, then read n logins, normalize each and add to set. Then check if normalized s is in the set.

The code should be straightforward.

Now, let's code the normalize function.

Wait, but the code should not have any debug prints. So the code will be:

def normalize(s):
    normalized = []
    for c in s:
        lower_c = c.lower()
        if lower_c == 'o':
            normalized.append('0')
        elif lower_c in ('i', 'l'):
            normalized.append('1')
        else:
            normalized.append(lower_c)
    return ''.join(normalized)

s = input().strip()
n = int(input())
existing = set()
for _ in range(n):
    login = input().strip()
    existing.add(normalize(login))
s_norm = normalize(s)
print("No" if s_norm in existing else "Yes")

Testing this code against the samples:

Sample 1:

Input:
1_wat
2
2_wat
wat_1

Normalize new s: '1_wat' → 1 (lowercase is '1', not o, i, l → remains 1? Wait, the first character is '1', which is a digit. So in the code:

c is '1' → lower_c is '1' (since digits don't have cases). Then, check if it's o → no. Else if it's in i or l → no. So append lower_c → '1'. So the normalized is '1_wat'.

Existing logins:

2_wat → normalized is '2_wat' (all characters except 2, w, a, t, which are not o, i, l. So '2_wat' is added.

wat_1 → normalized: 'wat_1' → each character. 'w' → 'w', 'a' → 'a', 't' → 't', '_' → '_', '1' → '1'. So normalized is 'wat_1'. The existing set has '2_wat' and 'wat_1'. The new s's normalized is '1_wat' → not in existing → output Yes. Which matches sample 1.

Sample 2:

Input:
000
3
00
ooA
oOo

Existing logins:

First, '00' → normalized is '00'.

Second, 'ooA' → lowercase is 'ooa'. Then o's become 0's → '00a'.

Third, 'oOo' → lowercase 'oo o' → o's become 0's → '000'.

So existing set has '00', '00a', '000'.

New s is '000' → normalized is '000' → which is in the set. So output No.

Sample 3:

Input:
_i_
3
__i_
_1_
I

Existing logins:

__i_ → lowercase is '__i_'. i becomes 1 → '__1_'.

_1_ → '_1_'.

I → lowercase is 'i' → becomes '1'.

So existing set has '__1_', '_1_', '1'.

New login is '_i_' → lowercase is '_i_'. i becomes 1 → '_1_'. So normalized is '_1_', which is in existing set. So output No.

All the samples are handled correctly.

Thus, the code should work.
</think>

```python
def normalize(s):
    normalized = []
    for c in s:
        lower_c = c.lower()
        if lower_c == 'o':
            normalized.append('0')
        elif lower_c in ('i', 'l'):
            normalized.append('1')
        else:
            normalized.append(lower_c)
    return ''.join(normalized)

s = input().strip()
n = int(input())
existing = set()
for _ in range(n):
    login = input().strip()
    existing.add(normalize(login))
s_norm = normalize(s)
print("No" if s_norm in existing else "Yes")
```