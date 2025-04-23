<think>
Okay, let's tackle this problem. The task is to find the maximum possible beauty of a string after changing up to k characters. The beauty is the maximum length of a substring consisting of the same character. Hmm.

So the problem is similar to those sliding window problems where we want the longest substring with at most k changes. Oh right! Like the "max consecutive ones" problem where you can flip k zeros. So maybe we can apply the sliding window approach here, but for both 'a's and 'b's.

Wait, the plan would be to find for each character (a and b), the maximum window where flipping the other characters in that window doesn't exceed k. Then take the maximum of the two.

Right. Let's think: For 'a's, we can slide a window and count the number of 'b's in the current window. If the count is <=k, then this window can be turned into all 'a's. Similarly for 'b's. The maximum window length for either case is the answer.

So the steps would be:

1. Iterate through the string once for 'a's, keeping track of the number of 'b's in the current window. If the count exceeds k, move the left pointer until it's within k.
2. Similarly, do the same for 'b's.
3. The maximum window size found in either of these passes is the answer.

Yes, this approach should work. The time complexity is O(n) for each pass, so overall O(n), which is acceptable for n up to 1e5.

Let's think about the example:

First example input: abba, k=2. For 'a's: The entire string has 2 'b's. So flipping them gives 4 a's. Similarly for 'b's, flipping the two a's (positions 0 and 3). So the maximum is 4.

Second example: aabaabaa, k=1. Let's check for 'a's. The maximum window where number of 'b's is <=1. Let's see. The string is a a b a a b a a. The original is a a b a a b a a. The 'b's are at positions 2 and 5. So the window from 0 to 5 has two 'b's. So with k=1, can't take that. But if we slide the window, maybe between positions 3 to 7: the 'b's here are only at position 5, so with one flip, that's 5 characters (positions 3-7 is length 5). Wait, but the example output is 5. Hmm. Or maybe another window. For 'b's, but the original string has only two 'b's. So flipping one 'a' to 'b' would give a maximum of 3 'b's. So the 'a' case is better.

So the algorithm should correctly capture that.

Now, how to implement this efficiently.

We can write a helper function that, given a target character (like 'a'), finds the maximum window length where the number of non-target characters is <=k. Then call this function for both 'a' and 'b'.

The helper function can use a sliding window approach:

Initialize left=0, max_len=0, count=0 (count of non-target chars in current window).

Loop over each right in 0 to n-1:

   if s[right] != target, increment count.

   while count > k:

       if s[left] != target, decrement count.

       left +=1

   update max_len as max(max_len, right - left +1)

So, this is O(n) time for each target.

So in code, for the given problem:

We can write two passes, one for 'a's and another for 'b's, and take the maximum.

Now, considering the string could be up to 1e5 characters, this approach is feasible.

Another point to consider: can we optimize by combining the two passes into a single loop? Probably not, but even two passes are manageable.

Now, let's code this.

The code steps:

Read n and k from input.

Read the string s.

Define a helper function to compute the maximum window for a given target.

Call the helper for 'a' and 'b', take the maximum.

Return that value.

Testing the examples:

First example:

n=4, k=2, s='abba'.

For 'a's:

The helper function checks each position.

At right=0 (a), count remains 0. window is 0-0, len 1. max_len=1.

right=1 (b): count=1. <=2. window 0-1, len 2. max_len=2.

right=2 (b): count=2. <=2. window 0-2, len3. max_len=3.

right=3 (a): count=2. window 0-3, len4. max_len=4.

So returns 4.

For 'b's:

At each position:

s is 'abba'.

right=0 (a): count=1. since target is 'b'. left moves to 0. So window is len 1 (but count is 1, which is <=k=2). So max_len is 1.

Wait, maybe I need to check again.

Wait, the helper function for target 'b':

left starts at 0.

right=0: s[0] is 'a' != 'b' → count=1. which is <=2. window is 0-0 → len1.

max_len is 1.

right=1: s[1] is 'b' → count remains 1. window 0-1 (len2). max_len=2.

right=2: s[2] is 'b' → count remains 1. window 0-2 (len3). max_len=3.

right=3: s[3] is 'a' → count=2. window 0-3, len4. So max_len=4.

So for 'b's, it's 4. So the maximum between 4 and 4 is 4. Correct.

Second example: n=8, k=1. s='aabaabaa'.

For target 'a's:

We need to count the number of 'b's in the window. We can have a window where the count is <=1.

Let's go through the string indices (0-based):

The string is a a b a a b a a.

Positions 2 and 5 are 'b's.

So for the helper function:

left starts at 0.

right=0: a → count=0. len 1.

right=1: a → count 0. len 2.

right=2: b → count=1. len3. (0-2, count 1).

max_len is 3.

right=3: a → count remains 1. len4. (0-3). max 4.

right=4: a → count 1. len5. (0-4). max5.

right=5: b → count=2. Now, count >1 (k=1). So we need to move left until count <=1.

Left starts at 0. s[0] is a, so not contributing to count. So left increments to 1. Check count: 2 (because the 'b's are at 2 and 5). Hmm, perhaps I need to track the count correctly.

Wait, when the current window is 0-5, count is 2 (positions 2 and 5). So we need to move left past the first 'b' to reduce the count.

Wait, in the helper function, when we have a window where the count exceeds k, we move the left pointer until the count is <=k.

So in this case, when right=5 (the second 'b'), count becomes 2. We need to move left until the count drops to 1.

So:

left is 0. s[0] is 'a' (not a 'b'), so decrementing count (from 2 to 2?), no. Wait, count is the number of non-target (for 'a's, the non-target is 'b's). So, for the helper function with target 'a', the non-target is 'b's.

So in the window 0-5, the 'b's are at 2 and 5. So count is 2. Since k=1, we have to move left until the count becomes 1.

So when we move left from 0 to 1, the window is 1-5. The 'b's are still 2 and 5 → count is still 2.

Moving left to 2: s[2] is 'b', so count decreases by 1 → count is 1. Now left is 3.

Now the window is 3-5. The count is 1 (only the 'b' at 5). So the window length is 3 (right - left +1 =5-3+1=3). So current max is max(5,3)=5.

Then, right=6: 'a' → count remains 1. Window is 3-6 (len4). max becomes 5.

right=7: 'a' → window 3-7 (len5). max remains 5.

So for the 'a's case, the maximum is 5.

For the 'b's case: the helper function would look for the maximum window where the number of 'a's is <=1. Let's see.

The original string has 6 'a's and 2 'b's. So flipping up to 1 'a's to 'b's.

Looking for the longest substring of 'b's with at most 1 'a's. Let's see:

The possible windows would be the positions where there is 0 or 1 'a's.

But the original string has 'a's in most positions. For example, the window from 2 to 5 (which is 'baab') has two 'a's. So even if we flip one 'a' to 'b', that's 3 'b's and 1 'a'. But the count of 'a's in the window would be 2 (original) minus 1 (flip). So if the window has two 'a's, but k is 1, that's not allowed.

So the helper function for 'b's would track the number of 'a's in the window. Let's see.

The maximum possible would be maybe a window with one 'a' (so flipping it gives all 'b's).

But given the original string has two 'b's, perhaps the maximum possible is 3 (the two original 'b's plus one flipped 'a').

But the helper function would find this.

But in the example, the answer is 5, which comes from the 'a's case. So the 'b's case may not contribute.

Thus, the code should correctly take the maximum of 5 and whatever the 'b's case gives, which in this case is lower.

So the code will output 5.

So the approach seems correct.

Now, code in Python.

Implement the helper function.

The code structure:

Read n, k.

s = input().strip()

Compute max_a = helper(s, 'a', k)

Compute max_b = helper(s, 'b', k)

print(max(max_a, max_b))

Implement helper function.

But in Python, functions are easy. Alternatively, code can be written inline.

Wait, but to avoid repetition, writing a helper function is better.

So:

def max_length(s, target, k):
    left = 0
    max_len = 0
    count = 0  # number of changes needed (non-target characters)
    for right in range(len(s)):
        if s[right] != target:
            count +=1
        # If count exceeds k, move left to reduce
        while count > k:
            if s[left] != target:
                count -=1
            left +=1
        current_len = right - left +1
        if current_len > max_len:
            max_len = current_len
    return max_len

Then:

max_a = max_length(s, 'a', k)

max_b = max_length(s, 'b', k)

print(max(max_a, max_b))

Testing this code on the examples.

First example:

n=4, k=2, s=abba.

max_length for 'a' gives 4. For 'b' also 4. Output 4.

Second example:

s='aabaabaa' (indices 0-7). For 'a' case:

The function will process each right. Let's see:

At right=2 (s[2] is 'b'), count increments to 1. current window is 0-2 (len3). Since k=1, this is allowed. max_len=3.

At right=5 (s[5] is 'b'), count becomes 2. Then, enter the while loop. Left is 0. s[0] is 'a' (same as target), so left moves to 1. Now, count is still 2. s[1] is 'a', left moves to 2. Now, check s[2] is 'b', which is non-target. count decremented to 1. left becomes 3. Now, current window is 3-5 (len3). max remains 5 (from previous steps).

Wait, maybe I should walk through the code step by step for the second example.

Wait, let's recheck.

The string is 'aabaabaa' → indexes 0-7:

0: a

1: a

2: b

3: a

4: a

5: b

6: a

7: a

For target 'a' and k=1.

left starts at 0. count=0.

right=0: a → count remains 0. len=1. max=1.

right=1: a → count 0. len=2. max=2.

right=2: b → count=1. len=3 (0-2). max=3.

right=3: a → count remains 1. len=4 (0-3). max=4.

right=4: a → len=5 (0-4). max=5.

right=5: b → count becomes 2. Now, enter loop:

count is 2>1. So check s[left] (s[0] is 'a') → not contributing. left increments to 1. count remains 2. s[1] is 'a' → left increments to 2. s[2] is 'b', so count decreases to 1. left becomes 3. Now, count is 1. loop ends. current len is 5-3 +1 =3. max remains 5.

right=6: a → len=3-6 →4. max remains5.

right=7: a → len=3-7 →5. same as current max. so overall, returns5.

Which matches the example.

So code works.

Now, for the code: what about edge cases?

Case when k is 0: we can't change anything. So the answer is the maximum consecutive a's or b's.

Another case: all a's. Then changing to a's would have n.

Another case: when the entire string can be flipped. Like when k is n. Then the maximum is n (all a's or all b's).

The code should handle these.

In Python, strings are handled as immutable, but for n up to 1e5, the code is acceptable.

Time complexity is O(n) for each helper call, so O(2n) which is O(n).

Space is O(1) for variables, so it's acceptable.

Thus, the code should pass all test cases.
</think>

```python
def max_length(s, target, k):
    left = 0
    max_len = 0
    count = 0  # Number of non-target characters in the current window
    for right in range(len(s)):
        if s[right] != target:
            count += 1
        # If the number of changes needed exceeds k, move left pointer
        while count > k:
            if s[left] != target:
                count -= 1
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len

n, k = map(int, input().split())
s = input().strip()

max_a = max_length(s, 'a', k)
max_b = max_length(s, 'b', k)

print(max(max_a, max_b))
```