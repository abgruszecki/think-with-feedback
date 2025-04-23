<think>
Okay, let's tackle this problem. Hmm. The task is to find the longest substring of a given string that is not a palindrome. If all possible substrings are palindromes, then we output 0. Otherwise, the maximum length of such a substring.

First, I need to understand the problem. So, the key points are:

1. Find the longest possible substring of the input string that is not a palindrome.
2. If all possible substrings are palindromes, output 0.

Wait, but the note says that in the first example, "mew" isn't a palindrome, so the entire string is the answer. So, the maximum possible length is the entire string if it's not a palindrome. But if the entire string is a palindrome, then we have to look for the next longest possible substring.

So the approach would be:

Check if the entire string is a palindrome. If it's not, then the answer is its length. If it is a palindrome, then the longest possible non-palindromic substring would be of length (length of string - 1). But wait, not necessarily. Because even after removing one character, the substring could still be a palindrome.

For example, consider the input "aaaaa". The entire string is a palindrome. If we take a substring of length 4, say "aaaa", which is also a palindrome. Then maybe we need to check if all possible substrings of length (n-1) are palindromes. If any of them is not, then the answer is (n-1). Otherwise, check for (n-2), etc., down to 0.

Alternatively, if the entire string is a palindrome, the maximum possible non-palindromic substring is (n-1) if at least one substring of that length exists that's not a palindrome. Otherwise, it's 0.

But how do we efficiently determine this?

Wait, perhaps the optimal approach is as follows:

The maximum possible length of a substring that's not a palindrome is either the entire string's length (if it's not a palindrome) or (n-1) if there's any substring of length (n-1) that's not a palindrome. If even all (n-1) length substrings are palindromes, then check (n-2), etc.

But checking all possible substrings for each possible length from n down to 1 could be time-consuming. However, given that the maximum input length is 50, even an O(n^3) approach would be feasible.

But maybe there's a smarter way.

Let's think. If the entire string is not a palindrome, return its length. Otherwise, we need to check if there's a substring of length (n-1) that is not a palindrome. For example, take "wuffuw" from the second example. The entire string is a palindrome. The substrings of length 5 are "wuffu" and "uffuw". The first one is "wuffu" — let's see: w u f f u. Wait, that's not a palindrome. Because the first character is 'w' and the last is 'u'. So the answer for that example is 5.

So in this case, when the entire string is a palindrome, the maximum possible length is (n-1), provided that at least one substring of length (n-1) is not a palindrome. If all (n-1) length substrings are palindromes, then we check for (n-2), etc.

Wait, but how can all (n-1) length substrings of a palindrome be palindromes themselves? Let's see. Take the example "abba". The entire string is a palindrome. The possible (n-1) substrings are "abb" (positions 1-3) and "bba" (positions 2-4). "abb" is not a palindrome (first is 'a', last is 'b'). So the answer would be 3. But in this case, the entire string is a palindrome, but the substrings of length 3 are not. So the answer would be 3.

So the approach would be:

If the entire string is not a palindrome, return n.

Else, check if there's any substring of length (n-1) that is not a palindrome. If yes, return (n-1).

Else, check (n-2), etc. If all substrings are palindromes down to length 1 (but wait, all single characters are palindromes), then return 0.

But wait, even if the original string is a palindrome, perhaps some substrings of shorter lengths are not. But how?

Wait, for example, consider the string "aaaabaaaa". The entire string is a palindrome. Let's see:

The substring starting at index 0 and length (n-1) would be "aaaabaaa". Is this a palindrome? Let's check: first character is 'a', last is 'a' (so yes). Then check the second and second last: 'a' and 'a' again. Then third and third last: 'a' and 'b' — oh, wait no. Wait, the substring is 'aaaabaaa' — let's count the positions. Let's see, original string is a a a a b a a a a. Length 9. So the substring of length 8 would be positions 0-7: a a a a b a a a. Wait, the substring would be "aaaa b aaa"? Let me see:

Original string: indices 0-8 (assuming 0-based). Substring of length 8 would be either 0-7 or 1-8. Let's take 0-7: characters are a a a a b a a a. The first character is a, last is a. Then the second is a, the second last is a. Then third a and third last a. Then fourth a and fourth last a. Then fifth is b. The middle. So yes, this substring is a palindrome. The other substring of length 8 is 1-8: a a a b a a a a. Which is also a palindrome. So in this case, the maximum possible is 7? Wait, but perhaps there's a substring of length 8 that is not a palindrome. No. So in this case, the answer would be (n-1) is not possible. Then check for (n-2) which is 7.

Wait, but for (n-2) substrings (length 7), maybe there's one that's not a palindrome.

But this approach could be tedious. However, perhaps the optimal solution is:

If the entire string is not a palindrome, return its length.

Else, return (n-1) if not all characters are the same. Otherwise, return 0.

Wait, no. Because in the example "abba", the entire string is a palindrome. The possible (n-1) substrings are "abb" and "bba". Both are not palindromes. So the answer is 3. But according to the alternative approach, if the original string is a palindrome, then check if all characters are the same. If not, return (n-1). Because in "abba", the characters are not all the same, so return (n-1) which is 3.

Wait, but why would that be the case?

Wait, here's an insight: If the entire string is a palindrome, then the maximum possible non-palindromic substring is either (n-1) or 0. Because:

If the entire string is a palindrome and all characters are the same (like "aaaaa"), then all possible substrings are also palindromes. So the answer is 0.

But if the entire string is a palindrome but not all characters are the same, then there must exist a substring of length (n-1) that is not a palindrome.

Because, suppose the entire string is a palindrome. Let's take the first (n-1) characters. If this substring is not a palindrome, then that's the answer. But if it is a palindrome, then the substring from the second character to the nth character (assuming 1-based) would be considered.

Wait, let's take an example. Suppose the string is "abba". The entire string is a palindrome. The first (n-1) characters are "abb". This is not a palindrome. So the answer is 3. So in this case, the answer is (n-1).

Another example: the string "aaaabaaaa" is a palindrome. The first (n-1) characters are "aaaa b aaa" (assuming n is 9, so length 8). Wait, in this case, the first (n-1) characters would be "aaaaabaa" (indices 0-7). The first character is 'a', last is 'a'. So it's a palindrome. Then the substring from 1 to 8 (indices 1-8) would be "aaabaaaa", which is also a palindrome. Wait, so in this case, both (n-1) substrings are palindromes. Then the answer would be (n-2)?

But according to our previous logic, that's not possible. So perhaps the initial approach is not correct.

Hmm. So this suggests that the initial approach might not work. Then how to proceed?

Wait, perhaps the key is that if the entire string is a palindrome, and all characters are the same, then the answer is 0. Otherwise, the answer is (n-1) if possible. If not, then (n-2), etc. But how to check that.

But how can the entire string be a palindrome, but not all characters are the same, and yet all (n-1) length substrings are palindromes? Let's see.

Take the example of "aba". The entire string is a palindrome. The (n-1) substrings are "ab" (which is not a palindrome) and "ba" (also not a palindrome). So the answer is 2.

But consider the string "ababa". The entire string is a palindrome. The first (n-1) characters are "abab", which is not a palindrome. So the answer is 4.

Another example: "abcba". The entire string is a palindrome. The first (n-1) substring is "abcb", which is not a palindrome. So answer is 4.

But let's think of a case where the entire string is a palindrome, but all (n-1) substrings are also palindromes.

Wait, suppose the string is "aabaaa". Let's check if the entire string is a palindrome. The first character is 'a', last 'a'. Second 'a', second last 'a'. Third 'b' vs third last 'a'. Wait, that's not a palindrome. So the entire string is not a palindrome. So the answer would be 6.

Wait, perhaps another example: "abbaa". Wait, that's not a palindrome. The entire string is not a palindrome, so answer is 5.

Hmm. Maybe the only case where the entire string is a palindrome but all (n-1) substrings are palindromes is when all characters are the same except the middle one, but even then, perhaps not.

Wait, let's try "aaaabaaaa". The entire string is a palindrome. The first (n-1) characters are "aaaaabaaa". Let's check if this is a palindrome. Let's see:

Positions 0-8 (assuming 0-based indices, original string is 9 characters). The first character is 'a', last is 'a'. Then the second and penultimate: 'a' and 'a'. Third and third from end: 'a' and 'a'. Fourth and fifth: 'a' and 'b'? Wait, no. Wait, for the substring "aaaaabaaa", the middle is at position 4 (since length 8: 0-7). Wait, wait, length 8: the indices are 0 to 7. The middle positions are 3 and 4 (since even length). So check positions 3 and 4. Wait, in the substring "aaaaabaaa", the first four characters are 'a's, then 'a', then 'b', then 'a's? Wait, maybe I'm getting confused here.

Wait, the original string is "aaaabaaaa" (length 9). The substring from 0 to 7 is "aaaaabaa". Let's see: positions 0 is 'a', 1 'a', 2 'a', 3 'a', 4 'b', 5 'a', 6 'a', 7 'a'. So the substring is "aaaaabaa". To check if this is a palindrome, compare first and last characters: 'a' and 'a' (same). Then second and second last: 'a' and 'a'. Third and third last: 'a' and 'a'. Fourth and fourth last: 'a' and 'b' — not same. So this substring is not a palindrome. So the answer would be 8 (n-1). But in this case, the entire string was a palindrome, but not all characters the same, so the answer is (n-1).

So perhaps the initial approach is valid: if the entire string is not a palindrome, return n. Otherwise, if all characters are the same, return 0. Else, return (n-1).

Wait, wait. Let's think again. If the entire string is a palindrome and not all characters are the same, then the maximum possible non-palindromic substring is (n-1).

Because the entire string is a palindrome. So the first (n-1) characters would be the same as the last (n-1) characters. Wait, no. For example, "abba": the entire string is a palindrome. The first (n-1) characters are "abb", which is not a palindrome. The last (n-1) are "bba", which is also not a palindrome. So in that case, the answer is (n-1).

But in the case where the entire string is a palindrome, and all (n-1) substrings are palindromes, then the answer would have to be (n-2) or lower. But can such a case exist?

Let's consider a string like "abcba". The entire string is a palindrome. The (n-1) substrings are "abcb" and "bcba". "abcb" is not a palindrome (a vs b), so answer is 4.

Another example: "aabaa". The entire string is a palindrome. The (n-1) substrings are "aab a" (positions 0-3: 'a', 'a', 'b', 'a') — which is a palindrome. Or the substring from 1-4: 'a', 'b', 'a', 'a' — which is not a palindrome. So even if one of the (n-1) substrings is not a palindrome, the answer is (n-1).

So perhaps the only time when even (n-1) substrings are all palindromes is when the entire string is made up of all the same characters. Like "aaaaa". Then, any substring of length (n-1) is "aaaa", which is also a palindrome. Then, the answer would be 0, since all possible substrings are palindromes.

So putting this all together, the steps are:

1. Check if the entire string is a palindrome. If it's not, then the answer is its length.

2. If it is a palindrome, check if all characters are the same. If yes, return 0.

3. Otherwise, return (n-1), since there must exist at least one substring of length (n-1) that's not a palindrome.

Wait, but why is that?

Because if the entire string is a palindrome and not all characters are the same, then there exists at least two different characters. Let's say the first character is different from some other character. Since the entire string is a palindrome, the first and last characters are the same. So the first character can't be different from the last. But perhaps there's a character in the middle that is different. For example, "aabaa". The middle character is 'b'. So, if you take the substring from the second character to the fifth (assuming 1-based), you get "abaa", which is not a palindrome. Wait, but in the case of "aabaa", the first (n-1) characters are "aaba", which is a palindrome. Wait, no: "aaba" is 'a', 'a', 'b', 'a' — the first and last are 'a', the second and third are 'a' and 'b' — which are different. So "aaba" is not a palindrome. So in this case, the answer would be 4.

So according to the steps:

The entire string is a palindrome. Not all characters are the same, so return (n-1). Which is 4.

So according to the steps, that's correct.

Another example: "abba". The entire string is a palindrome, not all same. So return (n-1) 3.

Another example: "aaaabaaaa". The entire string is a palindrome. Not all same. So return 8.

But wait, in that case, the (n-1) substrings are "aaaaabaa" and "aaabaaaa". The first one is not a palindrome (since the fourth character from start is 'a', fourth from end is 'b'). So yes, the answer is 8.

So according to the steps, this is correct.

But why is step 3 correct? Because if the entire string is a palindrome, but not all characters are same, then removing the first character would create a substring that is not a palindrome.

Wait, let's think: the entire string is a palindrome. Suppose the first character is 'a', and the second character is 'b'. Then, since the string is a palindrome, the last character must be 'a', and the second last must be 'b'. So, the substring from the second character to the second last would form a palindrome. Wait, but perhaps the substring of length (n-1) that is not a palindrome is the one that starts at the first character and ends at the (n-1)th character. For example, in "abba", the first (n-1) characters are "abb". Which is not a palindrome.

So, in general, if the entire string is a palindrome and not all characters are same, then there exists at least one (n-1) length substring that is not a palindrome.

Because, since the entire string is a palindrome but not all same, there exists some position where the character is different. Let's say the middle character is different. Then, taking the first (n-1) characters would exclude the last character (which is same as the first). But perhaps the first (n-1) characters would now have a different start and end. Wait, no. Because the entire string is a palindrome, the first (n-1) characters would be the same as the last (n-1) characters, but reversed. So for example, "abcba" (length 5). The first (n-1) is "abcb". The last (n-1) is "bcba". The first substring is a palindrome? Let's see: 'a', 'b', 'c', 'b'. The first and last are 'a' and 'b' — not same. So not a palindrome. So answer is 4.

So, in this case, the first (n-1) substring is not a palindrome, hence the answer is (n-1). So the steps are correct.

Thus, the steps are:

1. Check if the entire string is a palindrome. If not, return n.

2. Else, check if all characters are same. If yes, return 0.

3. Else, return (n-1).

This logic seems to handle all test cases.

Let's verify with the examples:

First example: "mew". Entire string is not a palindrome. So return 3.

Second example: "wuffuw". Entire string is a palindrome (w u f f u w). Check if all characters are same — no. So return 5 (n-1=6-1=5).

Third example: "qqqqqqqq". All characters same. So return 0.

Another test case: "abba" — returns 3. Which is correct.

Another test case: "a" — since the entire string is a palindrome. All characters are same. So return 0.

Another test case: "ab" — not a palindrome, so return 2.

Another test case: "aaaabaaaa" — entire string is a palindrome (since first and last are 'a', second and second last are 'a', etc.). Not all characters same. So return 8.

So the code can be written as follows:

First, check if the entire string is a palindrome.

To check if a string is a palindrome, compare it with its reverse.

Then, check if all characters are the same. For example, check if all characters are equal to the first character.

So code steps:

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = len(s)

    if s != s[::-1]:
        print(n, file=output_stream)
    else:
        if all(c == s[0] for c in s):
            print(0, file=output_stream)
        else:
            print(n-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
wuffuw
""",
            "output": \
"""\
5
""",
        }, 
        {
            "input": \
"""\
qqqqqqqq
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

Sample3: "qqqqqqqq" — palindrome. All same. Output 0. Correct.

Yes. This code should work.

So the code is simple and efficient, O(n) time for checking palindrome and all same, which is acceptable for n up to 50.
</think>

```python
s = input().strip()
n = len(s)
if s != s[::-1]:
    print(n)
else:
    if all(c == s[0] for c in s):
        print(0)
    else:
        print(n-1)
```
