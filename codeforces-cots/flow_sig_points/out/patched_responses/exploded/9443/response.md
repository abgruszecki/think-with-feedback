<think>
Okay, let's see the problem here. Mike has a string and he wants to change exactly one character to make it a palindrome. We have to determine if that's possible. Hmm.

First, I need to understand what a palindrome is. Oh right, it's a string that reads the same forwards and backwards. So for each position i, the character at i should equal the character at the corresponding position from the end.

The key here is that exactly one character must be changed. So even if the string is already a palindrome, changing exactly one character would break it. Wait, but maybe in some cases the original string is a palindrome, but changing a character in such a way that it's still a palindrome but with exactly one change. Wait, no. For example, take "aaa". If we change one 'a' to 'a', then it's still a palindrome, but we didn't change anything. Oh, wait, but the problem says change exactly one character. So even if the original is a palindrome, Mike has to change one character. So the modified string must be a palindrome, but exactly one change must be made. So in the original case, if the string is a palindrome already, then changing one character would make it not a palindrome unless that character's pair is also changed. Wait, but if the string length is even, then each character has a pair. If it's odd, then the middle character can be changed to any other, but then the string would no longer be a palindrome unless the middle character is symmetrical.

Wait, this is getting a bit confusing. Let me think through examples.

Take the first example input: "abccaa". The output is "YES". Let's see. The original string is a, b, c, c, a, a. Wait, the length is 6. To check if it's a palindrome, we compare index 0 and 5. 'a' vs 'a' → same. Index 1 and 4: 'b' vs 'a' → different. Index 2 and 3: 'c' vs 'c' → same. So original string is not a palindrome. Now, when we change exactly one character to make it a palindrome. Let's see. The first example's output is YES. So there's a way. How?

In the first example, maybe changing the 4th character (index 4) from 'a' to 'b' would make the string "abccba", which is a palindrome. So that's one change. So in that case, the answer is yes.

So the problem is: after exactly one change, the string becomes a palindrome.

So the approach is to find how many mismatches there are in the current string. For each pair of characters (i, n-1 -i), if they are different, that's a potential spot where a change can be made. Each such pair contributes one possible mismatch. Because if two characters in a pair are different, then to fix the palindrome, you can either change the left one to the right, or the right to the left. But since we can make exactly one change, we need to find a scenario where after making exactly one change (in some pair), all pairs are matched.

Alternatively, maybe the total number of mismatched pairs is exactly one. Then, changing one character in that pair would fix it, and the number of changes would be one. But what if there are more mismatched pairs?

Wait, but each mismatch requires that two characters differ. So for each such pair, we need to make a change. For example, if there are two mismatched pairs, then to make the string a palindrome, we need to fix each pair. But each fix requires changing at least one character. The minimal number of changes required is the number of mismatched pairs. Because for each pair that's mismatched, you can change one of the two characters to make them equal. So for example, if there are k mismatched pairs, the minimal number of changes is k. But Mike can change exactly one character. So for the modified string to be a palindrome, the number of required changes (the minimal changes) must be exactly one. Because Mike's change of exactly one character must be sufficient to reach that state.

Wait, no. Because Mike can change exactly one character. So the resulting string must be a palindrome, and the total number of changes made (exactly one) must be sufficient to make the string a palindrome.

So, for example:

If the original string has k mismatched pairs. The minimal number of changes required to make it a palindrome is k. But Mike can only change one character. So he can make one change that reduces the number of mismatched pairs by one (if possible) but that's only possible if changing one character can fix a pair.

Wait, perhaps the way to think about this is:

We need to find a position i where changing s[i] or s[n-1 -i] to match the other would result in the entire string being a palindrome. But since we can only change one character, how does that affect the other pairs?

Alternatively, maybe the correct approach is to count the number of mismatched pairs. Let's call this count 'diff'. Then:

If diff is 0: Then the original string is already a palindrome. But we need to change exactly one character. Changing any character would break the palindrome. So the new string would not be a palindrome. So in this case, the answer is only YES if the length is odd. Wait, wait. Wait, if the string is a palindrome already, but has an odd length. For example, "aba". If we change the middle 'b' to 'c', then the new string is "abca", which is not a palindrome. So even if the original is a palindrome with odd length, changing exactly one character would result in a non-palindrome. So in this case, the answer is NO. Because changing exactly one character would make it not a palindrome. So when the original string is a palindrome (diff is 0), the answer is NO. Because you have to change exactly one character, but that will create a palindrome only if the length is 1. Wait, for example, if the original string is "a". Then changing the only character to something else will result in a single character, which is a palindrome. Wait, because a single character is always a palindrome. So in this case, if the original is a palindrome of length 1, changing it to any other character would result in a palindrome, but that's still a palindrome. Wait, but the problem says that Mike changes exactly one character, and the resulting string must be a palindrome. So for example, if the original string is "a", then changing it to "b" (exactly one change) would result in "b", which is a palindrome. So in this case, the answer is YES. Because Mike can change exactly one character (the only one) and it's a palindrome. So the case when diff is 0 and the length is 1: answer is YES. Wait, but the problem says to change exactly one character. So for a length 1 string, there's only one character. So changing that one character will result in another single character, which is a palindrome. So for a length 1 string, the answer is always YES, because any single character is a palindrome. But wait, the problem requires exactly one change. So if the original string is "a", then changing it to "a" (no change) would not count. But the problem says exactly one character must be changed. So in this case, the modified string must be a different character. So for example, if the original is "a", then Mike can change it to "b", which is a palindrome. So answer is YES. But if the original is a palindrome of length greater than 1, then changing any character would create a mismatch. So for example, "aa": change one 'a' to 'b' → "ba", which is not a palindrome. So answer is NO.

So when the original string is a palindrome (diff is 0), the answer depends on the length. If the length is 1: YES. Else: NO. Because changing exactly one character would break the palindrome.

So in the case of diff = 0:

- If len(s) is 1 → YES (because after changing the only character, it's still a palindrome of length 1. Wait no. Wait, the problem requires exactly one character to be changed. So if the original is "a", then changing it to "b" (exactly one change) makes "b", which is a palindrome. So answer is YES.

But for length 3 and original is a palindrome, changing exactly one character (like the middle one) would break the palindrome. So the answer is NO.

So when diff is zero, the answer is YES only if the length is 1, otherwise NO.

But wait, what if the length is 1? Then the original string is a palindrome. Changing exactly one character would result in another single character, which is a palindrome. So the answer is YES.

So in code, when diff is zero:

if len(s) is 1 → YES

else, check if the number of changes required is exactly one. But for a palindrome with len >1, changing any character (exactly one) will result in a non-palindrome, unless the length is 1. So answer is NO.

So that's one case.

Now, if the diff is 1: Then the minimal number of changes required is 1. So if we can change exactly one character to fix the one mismatched pair, then the resulting string would be a palindrome. So in this case, the answer is YES. Because Mike can change exactly one character (like changing one of the two in the mismatched pair), which would fix that pair. Then the total number of changes is exactly one, and the string becomes a palindrome.

Wait, but if the pair has two different characters, then changing one of them would fix the pair. For example, pair is (a, b). Change a to b → pair becomes (b, b). So this counts as one change, and the entire string is a palindrome (assuming other pairs are okay). So in this case, when the diff is 1, changing one character (either of the two in the pair) would fix the entire palindrome. So answer is YES.

But what if the diff is more than one? Like diff is 2. Then the minimal changes required are two. So Mike can change exactly one character, which is not enough. So the answer is NO. Because even after changing one character, there's still at least one pair mismatched.

Wait, but maybe in some cases, changing one character could fix two pairs. How? Like, if there's a pair (a, b) and another pair (b, a). But I don't think that's possible. Because each pair is symmetric. So when you have a pair (i, j), then (j, i) is the same pair. So no, changing one character can only affect one pair.

Wait, for example, consider a string of length 4: "abba". The pairs are (0,3), (1,2). Both pairs are a and b. Suppose the string is "abca". Then the pairs are (0,3) a and a → okay. (1,2) b and c → mismatch. So diff is 1. So changing c to b would fix it, which is one change. So answer is YES.

But if the diff is 2, like the string is "abcd" (length 4). Pairs (a, d) and (b, c). Both are mismatched. So minimal changes needed are 2. But Mike can only change one character, so that's not enough. So answer is NO.

So the general approach is:

- Count the number of mismatched pairs (diff).

- Then:

Case 1: diff == 1 → YES.

Case 2: diff == 0 → check if the length is 1. If yes → YES. Else, can't make a palindrome with exactly one change (since changing any character would introduce a mismatch). So answer is NO.

Case 3: diff >1 → answer is NO.

Wait, but wait. What if diff is exactly 1, but the pair is in the middle (for odd length). Wait, no, pairs are for i from 0 to (n-1)/2. So for odd length, the middle character is not part of any pair.

Wait, for example, length 5. The middle index is 2. So pairs are (0,4), (1,3). The middle character (index 2) is not compared to anyone. So changing that character doesn't affect any pair. So if the string has no mismatched pairs (diff is 0), but the middle character can be changed. But in that case, the string is already a palindrome. So changing the middle character would create a string that's still a palindrome. But Mike must make exactly one change. So the original is a palindrome (diff 0). Changing the middle character would make the new string also a palindrome, but the change count is one. So in this case, the answer would be YES.

Wait, wait. Let's take an example. Original string is "abcba" (length 5, a palindrome). If Mike changes the middle character 'c' to 'd', the new string is "abdba", which is also a palindrome. So changing exactly one character (the middle one) would result in a palindrome. So in this case, the answer is YES. So the original diff is 0, but the length is odd. So in this case, the answer is YES.

So this complicates things. So the previous approach is incorrect.

So the problem is that when the original string is a palindrome (diff is 0), but the length is odd, then changing the middle character (exactly one change) results in a palindrome. So in this case, the answer is YES.

But if the original string is a palindrome with even length, then any change (exactly one) would break the palindrome, so answer is NO.

So in case of diff 0:

If the length is odd → answer is YES. Because changing the middle character (exactly one change) would leave the string as a palindrome.

If the length is even → answer is NO. Because changing any character would break the palindrome.

Wait, let's think:

Original string is "abba" (even length, palindrome). Changing one character, say first 'a' to 'b', the string becomes "bbba". Then the pairs are (0,3) → 'b' and 'a' (mismatch). (1,2) → 'b' and 'b' → okay. So the string is not a palindrome. So answer is NO.

Original string is "abcba" (length 5, odd). Changing the middle character to 'd' gives "abdba", which is a palindrome. So answer is YES.

So when diff is 0, the answer depends on whether the length is odd (then YES) or even (NO). But wait, the problem says to change exactly one character. So if the original is a palindrome, and the length is odd, then changing the middle character to any other character (exactly one change) would result in a palindrome. Because the middle character's pair is itself. So changing it doesn't affect the pairs. So the new string is still a palindrome.

So in that case, the answer is YES.

So the previous approach for the diff=0 case was wrong. So the correct approach is:

If diff is 0:

   if the length is odd → YES (since changing the middle character is allowed)

   else → NO (even length, any change would break the palindrome)

Wait, but what if the original string is of length 1, which is odd. For example, "a". Changing it to "b" → which is a palindrome. So answer is YES. So the case when diff is 0 and length is 1 is covered by the same logic.

So the revised cases are:

Compute the number of mismatched pairs (diff).

If:

- diff is 1 → YES. Because changing one character in the mismatched pair will fix that pair, and the entire string becomes a palindrome with exactly one change.

- diff is 0 → check if the length is odd. If yes → YES (change the middle character). Else → NO.

- else (diff >1) → NO.

But wait, what about the case where diff is 1, but the length is odd and the mismatched pair is the middle character?

No, the middle character isn't part of any pair. For example, in "abcaa" (length 5), the pairs are (0,4) → 'a' and 'a' (okay), (1,3) → 'b' and 'a' (mismatch). So diff is 1. Changing one of them would fix the pair, making the entire string a palindrome. So answer is YES.

Another example: original string is "abcca" (length 5). The pairs are (0,4) → 'a' and 'a', (1,3) → 'b' and 'c' → mismatch. So diff is 1. Changing the 'b' to 'c' would make (1,3) → 'c' and 'c', making the entire string a palindrome with exactly one change. So answer is YES.

Another example: if the original string is "abcba" (diff 0, length 5). Changing the middle character to any other would still leave it a palindrome, so answer is YES.

So the approach is:

Compute the number of mismatched pairs. For each pair (i, n-1 -i), check if the characters are the same. Count how many pairs are mismatched.

If the count is exactly 1, then answer is YES.

If the count is 0, then answer is YES if the length is odd, else NO.

Otherwise, answer is NO.

So how to implement this.

First, iterate over the pairs. Let n be the length of the string.

For i from 0 to (n-1)//2:

   if s[i] != s[n-1 -i], increment diff count.

Once we have the diff count, check:

if diff == 1 → YES.

elif diff == 0 → YES if n is odd, else NO.

else → NO.

Wait, wait. Let's test the sample inputs.

Sample 1:

Input: abccaa (length 6)

The pairs are:

0 and 5: a and a → same.

1 and 4: b and a → different → diff +=1.

2 and 3: c and c → same.

So diff is 1. So answer is YES. Which matches the sample.

Sample 2:

Input: abbcca (length 6)

Check pairs:

0 and 5: a and a → same.

1 and 4: b and c → different → diff +=1.

2 and 3: b and c → different → diff +=1. So diff is 2. So answer is NO. Which matches the sample.

Sample3:

Input: abcda (length 5).

Pairs:

0 and 4: a and a → same.

1 and 3: b and d → different → diff +=1.

So diff is 1 → answer is YES. Which matches the sample.

Another example: original string is "a" → diff is 0, length 1 (odd) → answer YES.

Original string "aaa" → diff 0, length 3 (odd) → answer YES. Because changing the middle 'a' to 'b' gives "aba", which is a palindrome. So exactly one change.

Original string "aaaa" → diff 0, even length → answer NO. Because changing any character would break the palindrome.

Another example: "abba" → diff 0. Even length. So answer is NO. Because changing any character would result in a non-palindrome.

Another example: "abcba" (diff 0, length 5). Answer is YES. Because changing the middle character is allowed.

So the code needs to:

- Calculate the number of differing pairs (diff).

- Then:

   if diff == 1 → YES.

   elif diff == 0:

      if len(s) is odd → YES.

      else → NO.

   else → NO.

So code steps:

Read the input string s.

n = len(s).

diff = 0

for i in 0 to (n//2 -1):

   if s[i] != s[n-1 -i]:

       diff +=1

if diff ==1:

   print("YES")

elif diff ==0:

   if n %2 ==1:

       print("YES")

   else:

       print("NO")

else:

   print("NO")

Wait, but in the loop, the range should be from 0 to (n//2 -1). For example, for n=5, (n//2) is 2, so the loop runs i=0 and 1. Because the pairs are (0,4), (1,3). Middle character is 2.

Yes.

So code in Python:

s = input().strip()

n = len(s)

diff = 0

for i in range(n//2):

    if s[i] != s[n-1 -i]:

        diff +=1

if diff ==1:

    print("YES")

elif diff ==0:

    if n %2 ==1:

        print("YES")

    else:

        print("NO")

else:

    print("NO")

Testing sample inputs:

Sample1: abccaa → loop i=0,1,2 (since n=6, n//2=3 → i runs 0,1,2). Check:

i=0: a and a → same.

i=1: b and a → different → diff=1.

i=2: c and c → same. So diff is 1 → YES.

Sample2: abbcca → n=6. i=0: a and a → same. i=1: b and c → different (diff=1). i=2: b and c → different (diff=2). So answer NO.

Sample3: abcda → n=5. loop runs for i=0,1,2 (but n//2 is 2). Wait, wait for n=5, n//2 is 2 (5//2=2 in integer division). So for i in 0,1,2? Wait, no. Because n//2 is 2 for n=5. So the loop runs for i in 0,1,2? But the pairs are (0,4), (1,3). The middle index is 2. So the loop should run for i from 0 to (n//2 -1) ?

Wait, for n=5, the number of pairs is 2. So for i in 0 and 1. Because n//2 is 2, but range(n//2) gives 0,1. Wait, yes. Because in Python, range(n//2) is 0 to (n//2 -1). Because for example, when n=5, n//2 is 2. So range(2) is 0,1. So the loop runs for i=0 and 1. Which checks the first two pairs. So in the code, the loop is correctly written as for i in range(n//2).

So for n=5, the code checks i=0 and 1. Which are the pairs (0,4) and (1,3).

So in the sample3 case, i=0: a and a → same. i=1: b and d → different → diff=1. So code outputs YES.

So the code works for the sample cases.

Another test case: "a" → n=1. Loop runs 0 times. diff=0. n is odd → output YES.

Another test case: "aa" → loop runs 1 time (i=0). s[0] and s[1] are same. diff=0. n even → output NO.

Another test case: "abba" → loop runs 2 times. i=0 and 1. Both pairs are same. diff=0. n even → NO.

Another test case: "abcba" → loop runs 2 times (n//2=2 for n=5). i=0: a and a → same. i=1: b and b → same. So diff=0. n is odd → output YES.

So the code should handle all cases.

Thus, the code is correct.
</think>

```python
s = input().strip()
n = len(s)
diff = 0
for i in range(n // 2):
    if s[i] != s[-1 - i]:
        diff += 1
if diff == 1:
    print("YES")
elif diff == 0:
    print("YES" if n % 2 else "NO")
else:
    print("NO")
```