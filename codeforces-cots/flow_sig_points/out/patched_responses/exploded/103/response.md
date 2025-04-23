<think>
Okay, I need to solve this problem where I have to check if a given number is quasi-palindromic. Let's understand the problem statement again. A quasi-palindromic number is one that can have some leading zeros added (maybe none) to form a palindrome. So the main idea is that when you add leading zeros, the resulting string becomes a palindrome.

Let's think about examples. The first example is 131. Adding nothing gives "131", which is a palindrome. The second example is 320. If you add leading zeros, like "00320", it's 00320, which reversed is 02300. That's not a palindrome. So the answer is NO. The third example is 2010200. Adding two zeros gives "002010200", which is a palindrome.

So the key is that when you add leading zeros, the resulting string must be a palindrome. So how can we model this?

The original number is given without leading zeros, but when we add leading zeros, the length of the string increases. The original digits plus some leading zeros must form a palindrome.

Wait, but how do leading zeros affect the palindrome structure? For example, if the number is 320, the digits are 3,2,0. If we add leading zeros, say two zeros, it becomes 00320. The palindrome check for this would require the first digit (0) to match the last (0), second (0) to match the fourth (2), third (3) to match the third. But here, 0 vs 0 (first and last) is okay, but second (0) vs fourth (2) is not. So that's why the example returns NO.

So the approach is to find if there exists a number of leading zeros to prepend such that the entire string is a palindrome.

But how to check this efficiently? Let's think about possible ways.

The original number's string is S. We can prepend any number of leading zeros to form a new string T. T must be a palindrome.

The string T will be a palindrome if, after adding leading zeros, the entire string reads the same forwards and backwards.

Let's consider that the original number is S. So T is a string of the form '0'*k + S. We need to check if this T is a palindrome for some k >= 0.

But how do we choose k?

Wait, for example, the original digits are S. Let's think of T as some string that starts with m zeros, followed by S. Then the entire string T must be a palindrome. So the length of T is m + len(S).

But how can we check for any m (including zero) whether such a T is a palindrome?

The problem is that m can be any non-negative integer. However, trying all possible m's up to some maximum isn't feasible, especially since S can be up to 10^9, which is a 9-digit number. But perhaps there's a smarter way.

Let's think about the palindrome structure. For T to be a palindrome, the first half of the string must mirror the second half. However, when leading zeros are added, they become part of the left side. So, the right part (the original digits plus some possible zeros) must mirror the left part (the leading zeros plus the original digits) in reverse.

Wait, perhaps the key insight is that the original digits, when combined with leading zeros, form a palindrome. So the original digits' suffix (the right part) must match the leading part (which can be zeros) when reversed.

Alternatively, let's model T as a palindrome. Let's imagine that T is a palindrome. Then, the left half is some combination of leading zeros and the original digits, and the right half is the mirror of the left.

But how can we model this? Let's consider that T is of the form '0...0' + S. So, for T to be a palindrome, the entire string must be symmetric. For example, if T is "002010200", then the first character is 0, the second 0, third 2, etc., and the last is 0. The mirror positions must be equal.

Another approach: the original digits S can be split into two parts. The leading part (after the leading zeros) and the trailing part. But perhaps this isn't the right way.

Alternatively, consider that when leading zeros are added, the rightmost digits of the palindrome must form S. Because S is given without leading zeros. Wait, but S could end with zeros, which would affect the palindrome structure.

Wait, let's think about the structure of T. Suppose T is a palindrome. Then, the first m digits are leading zeros, followed by S. But since T is a palindrome, the last digits must be the reverse of the first digits.

But S is the original number, which doesn't have leading zeros. So the original digits are at the end of T when leading zeros are added.

Wait, perhaps the correct way is to think that in the palindrome T, the original digits S form a suffix of T, but after some leading zeros. So T's structure is [leading zeros][... digits from S ...], and when reversed, this must be equal to the original.

Alternatively, T is a palindrome, so T = reverse(T). So the original digits S must form a part of the end of T, and the leading zeros plus some part of S must mirror the end of S.

Hmm, this is getting a bit abstract. Let's think of possible cases.

Case 1: The original number S is a palindrome by itself. Then, adding zero leading zeros (i.e., not adding any) makes T a palindrome. So in this case, the answer is YES.

But that's not the only case. For example, the third example, 2010200, when added two zeros becomes 002010200, which is a palindrome. The original S is 2010200, which is not a palindrome (since first digit is 2, last is 0), but adding leading zeros allows it to become a palindrome.

So the problem is to check if S, when possibly padded with leading zeros, becomes a palindrome. How can we model this?

Another approach: the entire T must be a palindrome. Let's imagine that T has length L. Then, for any i in 0..L-1, T[i] must equal T[L-1 - i].

But T is composed of some leading zeros followed by S. Let's denote the original string S as s. The original s has no leading zeros. The T string is a sequence of k leading zeros followed by s.

So T = '0'*k + s.

We need to find any k >=0 such that T is a palindrome.

But how can we check for all possible k? Since k can be any value from 0 upwards, but for the palindrome to hold, the length of T must be compatible. For example, if k is 3, then T is '000...s'.

But perhaps the maximum possible k we need to check is limited. Because when you add leading zeros, the left part of the palindrome would have those zeros, which must match the right part. So the right part must have those zeros as well.

Wait, for example, let's say T is of length L. The first k characters are zeros. The rest are s.

In order for T to be a palindrome, the first character (0) must equal the last character (s's last digit). The second character (0) must equal the second last, and so on.

So for the first k characters (all zeros), their corresponding mirrored positions must also be zero. But the right end of T is s, which is of length len(s). So the positions from k to k+len(s)-1 in T are the digits of s.

So for T to be a palindrome, the first k characters (all zeros) must match the last k characters of T, which are the last k characters of s.

Wait, that's an important point. Let's see:

Suppose T has length m = k + len(s). For T to be a palindrome, the first k characters (all zeros) must equal the reversed last k characters of T. Because T is a palindrome, T[i] = T[m-1 -i] for all i.

So for i from 0 to k-1, T[i] is 0. So T[m-1 -i] must also be 0. But T[m-1 -i] is part of the original s, except when m-1 -i >=k (since the first k are zeros, the rest are s). Wait, m-1 -i is the position from the end. Let's see for the first k positions (i <k):

For each i in 0..k-1, T[i] = 0. So T[m-1 -i] must also be 0. Since T is s with k leading zeros, the position m-1 -i can be in the s part only if m-1 -i >=k. Because T has k leading zeros followed by s. So m-1 -i >=k => len(s) +k -1 -i >=k => len(s)-1 -i >=0 => i <= len(s)-1.

But i is in 0..k-1, so this can only be true if k-1 <= len(s)-1 → k <= len(s).

Wait, perhaps I'm getting stuck here. Let's think with an example.

Take the example where s is 2010200. The original s is 7 digits. When adding two leading zeros (k=2), the T becomes 002010200 (9 digits). The first two digits are 0. The last two digits (positions 8 and 7 in 0-based) must be 0. The original s ends with 0,0. So the last two digits are 0,0. So in this case, the leading zeros (2) are matched by the trailing two zeros in s.

So for the first k positions (0 and 1 in T), the corresponding mirrored positions (8 and 7) must be 0, which they are. Then, the remaining digits (from position 2 to 8 - k = 8 -2 =6) must form a palindrome. Wait, but T's length is 9 (2+7). So positions 0-8.

For T to be a palindrome, the middle is position 4. The first part is 0,0,2,0,1,0,2,0,0. Wait, no. Wait T is 002010200. Let's index each character:

0:0, 1:0, 2:2, 3:0, 4:1, 5:0, 6:2, 7:0, 8:0.

So for each i, T[i] should equal T[8-i].

Check for i=0: 0 vs 0 → ok.

i=1: 0 vs 0 → ok.

i=2: 2 vs 0 (T[8-2=6] is 2). Wait 8-2=6? T[6] is 2. So 2 ==2 → ok.

Wait, that's correct. So in this case, the leading two zeros (positions 0 and1) are matched by the trailing two zeros (positions 7 and 8). Then, the middle part is 2,0,1,0,2. Which is a palindrome.

So the approach is that when we add k leading zeros, the first k digits are 0s, and the last k digits must also be 0s. Then, the remaining part (the original s minus the last k digits) must be a palindrome.

Wait, that seems like a possible approach.

So here's the plan: for any possible k (number of leading zeros to add), the following must hold:

- The last k digits of s must all be 0. Because when you add k leading zeros, the first k digits are zeros, and their mirror positions (the last k digits of T) must also be zeros. But the last k digits of T are the last k digits of s, since the leading zeros are added before s. So the last k digits of s must be zeros.

Then, after removing those k trailing zeros from s, the remaining part of s (prefix) must be a palindrome.

But wait, the remaining part of s (after removing the trailing k zeros) must form a palindrome when prepended by the leading k zeros. Or maybe not. Let's think.

Once the trailing k digits are zeros, the leading k zeros in T are mirrored by those zeros. Then, the middle part of T (after leading k zeros and before the trailing k zeros) is the s without the trailing k zeros. So this middle part must form a palindrome on its own. Because the leading zeros and trailing zeros are already matched, the middle part must itself be a palindrome.

So for example, in the third example, s is 2010200. The trailing two digits are 00. So k=2. The remaining prefix is 20102. Is 20102 a palindrome? Let's see: 2 vs 2 (ends), 0 vs 0 (middle), 1 in the center. Yes. So the middle part is a palindrome.

So the steps are:

1. For each possible k (number of trailing zeros in s), check if:

   a. The last k digits of s are all zeros. 

   b. The remaining prefix (s without the last k zeros) is a palindrome.

2. If any k (including k=0) satisfies these two conditions, then the answer is YES.

Additionally, k can be 0. In that case, we just need the entire s to be a palindrome. Which is the first case I thought of.

So the algorithm would be:

- Iterate possible k from 0 to the number of trailing zeros in s.

   For each k:

   - Check if the last k digits of s are all zeros.

   - Then, take the prefix (s without the last k digits) and check if it is a palindrome.

   - If any such k exists, return YES.

But how do we determine the possible k's?

The maximum possible k is the number of trailing zeros in s. Because the last k digits of s must be zeros.

So first, find all possible k values: 0, 1, ..., m, where m is the number of trailing zeros in s.

Wait, no. For example, s could be 320, which has zero trailing zeros. So possible k's are only 0. Then check if s is a palindrome.

But in that case, since s is 320, which is not a palindrome, the answer is NO.

Another example: s is 2010200, which has two trailing zeros. So possible k's are 0,1,2.

For k=0: check if the entire s is a palindrome. 2010200 → first digit is 2, last is 0 → not a palindrome. So no.

k=1: last digit is 0. Check the prefix 201020. Check if it's a palindrome. 201020 → first is 2, last is 0 → no.

k=2: last two digits are 0. Prefix is 20102 → which is a palindrome. So answer yes.

So the approach is to generate all possible k's from 0 up to the maximum possible (number of trailing zeros in s), and check for each.

So the steps for the code:

1. Convert the input x to a string s.

2. Find all possible k values (number of trailing zeros in s can be up to the count of trailing zeros). For example, if s is '2000', the possible k's are 0,1,2,3.

3. For each k in 0 to len(trailing zeros), inclusive:

   a. Check if the last k digits are all zeros.

   b. Check if the prefix (s[0: len(s)-k]) is a palindrome.

   c. If any k satisfies both, return YES.

4. If none of the k's work, return NO.

But how to implement this efficiently?

First, how to find the number of trailing zeros in s. For example, s is '2010200', trailing zeros are 2. Let's code that:

trailing_zeros = 0

i = len(s)-1

while i >=0 and s[i] == '0':

   trailing_zeros +=1

   i -=1

So for s = '320', trailing_zeros is 0.

Once we have the trailing_zeros count, possible k's are 0,1,...,trailing_zeros.

For each k in 0 to trailing_zeros:

   Take the prefix as s[0: len(s) -k]

   Check if this prefix is a palindrome.

If any of these checks passes, return YES.

Else, return NO.

Yes, this seems manageable.

So let's code this.

First, handle the case where k can be up to the trailing zeros.

But wait, for example, if s is '0', trailing zeros is 1. But len(s) is 1. So possible k's are 0 and 1. But when k is 1, len(s)-k = 0, so prefix is empty. But that's not possible because the original number is given without leading zeros. Wait, but in this problem, the original x is >=1, so s is at least '1'. So no problem.

Wait, no. The input x can be 1 ≤ x ≤1e9, which can be 1. So s can't be empty.

So for each k in 0 to trailing_zeros:

   The prefix is s[0: len(s) -k]

   If len(prefix) is 0: then it's invalid. Because the original s is not empty. But since k can't be larger than len(s), because trailing_zeros can't be larger than len(s). For example, if s is '0000', then trailing_zeros is 4. But then len(s) is 4, and len(s) -k can be 0 when k=4. But in that case, the prefix is empty, but that's possible only if the original s is all zeros. But according to the problem statement, the input x is given without leading zeros. So s cannot start with zero. So if s is '0000', that's invalid input. So the problem's input x is given without leading zeros. So the input s has no leading zeros. So the only way len(prefix) can be zero is if s is all zeros, but that's impossible because x is >=1.

So we can safely proceed.

So the steps:

For each k in 0 to trailing_zeros:

   Check if the last k digits are all zeros (which they are, since we're iterating up to the count of trailing zeros). Wait, no. Because trailing_zeros is the maximum possible trailing zeros. So for any k <= trailing_zeros, the last k digits are zeros. So step 3a is automatically satisfied. So perhaps step a can be skipped.

Because if the maximum possible trailing zeros is m, then for any k <= m, the last k digits are zeros.

For example, if s is '2010200', trailing_zeros is 2. So for k=1, the last 1 digit is '0'; for k=2, last 2 digits are '00'.

So in this case, the code can iterate k from 0 to m, and for each k, the last k digits are zeros. So step 3a is redundant and can be skipped.

Therefore, the algorithm can be optimized as follows:

Compute the maximum possible trailing zeros (m). For each k in 0 to m:

   Take the prefix s[0: len(s) -k]

   Check if this prefix is a palindrome.

If any such prefix is a palindrome, return YES. Else, NO.

This is correct.

So how to compute the number of trailing zeros.

Then, for each k in 0 to m, check if the prefix is a palindrome.

Now, the code steps:

Read x as a string.

Compute m, the number of trailing zeros in s.

Loop k from 0 to m (inclusive):

   prefix = s[: len(s) -k]

   if prefix is palindrome:

      return YES.

After all k's checked, return NO.

So, for example, the third test case (2010200) has m=2.

Check k=0: prefix is '2010200' → not a palindrome.

k=1: prefix is '201020' → ends with 0, starts with 2 → not a palindrome.

k=2: prefix is '20102' → '20102' is a palindrome (since 2 vs 2, 0 vs 0, 1 in the middle). So return YES.

Another example: input 320. trailing_zeros is 0. So k can be 0. Check if '320' is a palindrome. '320' reversed is '023', which is not the same. So output NO.

Another test case: 131. trailing_zeros is 0. Check if '131' is a palindrome. Yes. So output YES.

Another example: x=200. s='200'. trailing_zeros is 2. So possible k=0,1,2.

k=0: check '200' → reversed is '002' → not same. So no.

k=1: prefix is '20' → check if '20' is a palindrome. No.

k=2: prefix is '2' → yes. So output YES.

So the code would correctly return YES for x=200.

So this approach works.

Now, the code:

Read x as a string.

Compute m by counting trailing zeros.

Loop k in 0 to m:

   prefix = s[: len(s)-k]

   if prefix == prefix[::-1]:

      print("YES")

      exit.

After all loops, print "NO".

This is O(m * len(s)), but since m can be up to len(s) (like in the case of x=2000, m is 3, len(s) is 4), the worst case is O(len(s)^2). But len(s) can be up to 10 digits (x is 1e9 → 10 digits). So even in the worst case, 10*10=100 operations, which is manageable.

So the code is efficient.

Now, coding this in Python.

The code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    m = 0

    n = len(s)

    i = n-1

    while i >=0 and s[i] == '0':

       m +=1

       i -=1

    for k in range(0, m+1):

       prefix = s[:n -k]

       if prefix == prefix[::-1]:

          print("YES", file=output_stream)

          return

    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
320
""",
            "output": \
"""\
NO
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
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    m = 0

    n = len(s)

    i = n-1

    while i >=0 and s[i] == '0':

       m +=1

       i -=1

    for k in range(0, m+1):

       prefix = s[:n -k]

       if prefix == prefix[::-1]:

          print("YES", file=output_stream)

          return

    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2010200
""",
            "output": \
"""\
YES
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

Example 3: input 2010200 → s='2010200'

trailing zeros are 2 (last two digits 0).

Check k=0: '2010200' → not palindrome.

k=1: '201020' → no.

k=2: '20102' → yes. → YES.

Another test case: x=200 → s='200' → m=2.

Check k=0: '200' no.

k=1: '20' no.

k=2: '2' → yes. → YES.

Another test case: x=2000 → s='2000', m=3.

Check k=0: '2000' no.

k=1: '200' → no.

k=2: '20' → no.

k=3: '2' → yes. → YES.

So the code works.

Thus, this approach is correct and efficient.
</think>

```python
s = input().strip()
n = len(s)
m = 0
i = n - 1
while i >= 0 and s[i] == '0':
    m += 1
    i -= 1
for k in range(m + 1):
    prefix = s[:n - k]
    if prefix == prefix[::-1]:
        print("YES")
        exit()
print("NO")
```
