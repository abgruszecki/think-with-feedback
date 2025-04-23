<think>
Okay, let's see. The problem is to take a string of even length and perform some manipulations. So the steps are: split into two halves, reverse each half, then concatenate them in the order first reversed half followed by the second reversed half. Oh right, wait. Wait the steps are:

Divide into two halves: first half is s1 to sn, second is sn+1 to s2n. Then reverse each of them. So first reversed half becomes sn..s1, second becomes s2n..sn+1. Then concatenate these two reversed halves.

So for example, the first test case 'codeforces' has length 10. So split into first 5 and next 5. The first part is 'codef' (wait no, wait original string is codeforces. Let's check. 'codeforces' is spelled c o d e f o r c e s. Wait length 10. So first half is 5 characters: c o d e f (indices 0-4?), then the next 5 is o r c e s (indices 5-9). Wait wait, when split into two halves, the first half is s1..sn. For a string of length 2n, so n is half. So for 'codeforces', n is 5. So first half is first 5 characters, which are c o d e f. Then the second half is o r c e s. Then reverse each half. Reversed first half would be f e d o c. Reversed second half is s e c r o. Then concatenate them: fedoc + secro → fedocsecro, which matches the example output.

So the steps are clear. Now, how to implement this efficiently.

The input is a string of even length between 2 and 20. So the maximum size is 20 characters. So even for the largest input, any approach would work since the operations are O(n) which is negligible for n=20.

But since the problem is straightforward, the optimal approach is to split the string into two parts, reverse each, and concatenate.

So steps in code:

Read the input string s.

Compute n = len(s) // 2.

First_half = s[0:n], reversed → s[0:n][::-1]

Second_half = s[n:], reversed → s[n:][::-1]

Result is first_half_reversed + second_half_reversed.

So code would be something like:

s = input().strip()

n = len(s) // 2

first = s[:n][::-1]

second = s[n:][::-1]

print(first + second)

Yes. That's all. For example, in the second test case 'qwertyasdfgh' which is length 12. So n is 6. The first half is 'qwerty' → reversed is 'ytrewq'. The second half is 'asdfgh' → reversed is 'hgfdsa'. So concatenated gives 'ytrewqhgfdsa', which matches the sample.

So the code is straightforward. There's no need for any complex data structures here. Since the string operations are O(n) and n is up to 20, it's very efficient. So this approach is optimal.

Now, the code in Python:

Read the input, split into two parts, reverse each, concatenate and print.

Testing the code with the examples. Let's check the first example:

Input: codeforces → len 10. n=5. s[:5] is 'codef', reversed is 'fedoc'. s[5:] is 'orces' (assuming the original split is correct). Wait 'codeforces' is spelled as c o d e f o r c e s. So the first 5 letters are c o d e f → indices 0-4. Then the next 5 are o (5), r (6), c (7), e (8), s (9). So reversed second half would be s e c r o. So when reversed, the second part is 'secro'. So concatenated is 'fedoc' + 'secro' = 'fedocsecro' which is correct.

Yes. So the code works.

Another test case: input 'ab', output is 'ba' → split into 'a' and 'b', reverse each to get 'a' and 'b', concatenate 'ab' → wait no. Wait split into first half 'a' (n=1), reversed is 'a'. Second half 'b' reversed is 'b'. So concatenated is 'ab'? Wait but the problem says the output after reversing each part. Wait wait no: original string 'ab' split into 'a' and 'b', reversed each → 'a' and 'b', concatenated gives 'ab'? But according to the problem statement, the manipulations would take the two halves, reverse each, then concatenate. So for 'ab', the result is 'ab' reversed each half → 'a' and 'b' → 'ab'. So code returns 'ab' as output. So if input is 'ab', the output is 'ab'. But maybe another test case like 'abcd' → split into 'ab' and 'cd'. Reverse each: 'ba' and 'dc', concatenated as 'badc'. Let's see code would output s[:2][::-1] → 'ab' reversed is 'ba', s[2:] is 'cd' reversed is 'dc'. So 'ba'+'dc' → 'badc'.

Yes. So code is correct.

Therefore, this code should handle all cases correctly.
</think>

```python
s = input().strip()
n = len(s) // 2
print(s[:n][::-1] + s[n:][::-1])
```