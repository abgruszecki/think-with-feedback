<think>
Okay, let's see. The problem is to find the minimum window in a row of flats where all unique Pokemon types are covered, but with the constraint that the window must be a contiguous path that can be walked in a straight line. Because the flats are arranged in a row, the path has to be a substring (a contiguous sequence) of the flat sequence, and the path must be such that you can start at one point and walk left or right, collecting all the types without revisiting any flats. Wait, but the way the flats are connected, you can only move to adjacent ones. So the path must be a contiguous segment of the row, because once you start moving, you can't go back. So the minimal path is the shortest contiguous substring that contains all unique characters. Because any such substring can be traversed by starting at one end and moving straight to the other end.

Wait, right! Because the path has to be a contiguous sequence of flats. So the problem reduces to finding the smallest window (contiguous subarray) that contains all unique characters present in the entire string. Then the answer is the length of the smallest such window.

So this problem is similar to the classic sliding window problem where we find the minimum window substring containing all unique characters. But in the classic problem, the target is all unique characters in the entire string, and we have to find the smallest window that includes all of them.

Yes. So the approach here is to compute the set of unique characters in the entire string, then find the minimal length of a contiguous substring that contains all of them. That's exactly what's needed here.

So the steps are:

1. Determine all unique characters in the string. Let's call the size of this set 'unique_count'.
2. Use a sliding window (two pointers) approach to find the minimal window that contains all 'unique_count' characters.

But wait, the constraints are n up to 1e5, so O(n) algorithms are acceptable. The sliding window approach is O(n) time, which is suitable.

So the plan is:

- Precompute the set of unique characters in the entire string.
- Then use two pointers, left and right, to track the current window. Expand right as much as possible, and then try to contract left to find the minimal window.

But in the sliding window technique, we need a way to track the count of each character in the current window, and check if all required characters are present.

So here's how to do it:

Initialize a frequency dictionary (could be a defaultdict or a regular dictionary) to keep track of counts of each character in the current window. Also, keep a counter for how many unique characters are present in the window (i.e., the number of unique characters whose count is at least one in the window).

Expand the right pointer, adding each character to the frequency dict. When the count of a character increases from zero to one, increment the unique_in_window counter. When unique_in_window equals unique_count, start moving the left pointer to try to minimize the window. For each step of moving left, decrease the frequency of the character being left. If the frequency drops to zero, decrement the unique_in_window counter. Keep track of the minimal window length encountered during this process.

That's the standard approach. So implementing this will give the correct answer.

Let's test this with the examples.

First example:

Input: 3, AaA

Unique characters are A, a. So unique_count=2.

The string is A a A. The possible windows:

- [0,1] (A, a) → length 2. This includes both, so it's a candidate.

So the minimal is 2.

Second example:

7, bcAAcbc → characters are b, c, A. So unique_count=3.

The string is b c A A c b c.

Looking for the minimal window that has all three. The sample output is 3. Let's see: positions 4-6 (indices 3 to 5, assuming 0-based) are A c b. But wait, maybe the correct window is from the fourth character (A) to the sixth (c), which is A c b. Wait, no. Let's see:

Looking for the minimal substring with all three. Let's see:

Looking at the sample explanation, starting at position 4 (1-based) and ending at 6 (1-based) gives 'A c b', which includes A, c, b. So the window length is 3.

Third example:

6, aaBCCe → unique characters are a, B, C, e. So unique_count=4.

The sample output is 5. The minimal window must be 5, which would be from position 2 (B) to 6 (e), which includes a (from position 0?), wait no. Wait, the input is "aaBCCe". Let's index as 0-based:

0:a, 1:a, 2:B, 3:C,4:C,5:e.

The required unique characters are a, B, C, e.

So the minimal window has to include B (position 2), C (3 or 4), and e (5), but also a. So the earliest a is at 0. So the window would need to include from 0 to 5, but that's length 6. But the sample output is 5.

Wait, according to the sample explanation, the correct path is starting from position 2 (B) and ending at 5 (e). But that window is from index 2 to 5 (length 4?), but that's B, C, C, e. Wait that doesn't include a. So I'm confused. Wait, maybe the sample input is different.

Wait the third example input is "aaBCCe". So the unique characters are a, B, C, e. So the window must include all four. So the minimal window is positions 1 to 5: a (from 1), B (2), C (3,4), e (5). So indices 1 to 5: 'aBCCe' → which is a, B, C, C, e. That includes all four types, and length 5. So that's why the answer is 5.

So the sliding window approach would find that window.

So the sliding window approach should work.

Now, the challenge is to implement this efficiently.

In Python, for n=1e5, the code must be efficient. The sliding window approach is O(n) time and O(k) space, where k is the number of unique characters. Since k can be up to 52 (letters and cases), the space is manageable.

So the steps for the code:

1. Read n and s.

2. Compute the unique_count as the number of unique characters in s.

3. If unique_count is 0 (but n can't be 0), then return 0. But since each flat has a Pokemon, n is at least 1, and unique_count is at least 1. But if all characters are same, then the answer is 1.

4. Initialize left=0, min_length = infinity, current_unique = 0, freq = defaultdict(int).

5. Iterate right from 0 to n-1:

   a. Add s[right] to freq. If it's the first occurrence in the current window (freq becomes 1), increment current_unique.

   b. While current_unique == unique_count:

       i. Update min_length if (right - left +1) is smaller.

       ii. Try to move left forward:

           - subtract s[left] from freq. If its count drops to 0, decrement current_unique.

           - left +=1.

6. After processing all right, return min_length.

This should work.

Let's code this.

But in Python, for efficiency, using a Counter or a defaultdict is acceptable. However, for even better speed, since the possible characters are limited (uppercase and lowercase letters), we can use a fixed-size array of size 128 (ASCII values) to track counts. That's probably faster than a dictionary.

But in practice, for Python, using a dictionary is acceptable for 1e5 elements.

But let's code it with a dictionary.

Now, code:

Read n, s.

unique = set(s)

unique_count = len(unique)

if unique_count == 0:
    print(0)
else:
    left = 0
    min_len = n  # maximum possible
    current_count = 0
    freq = {}

    for right in range(n):
        char = s[right]
        if char not in freq or freq[char] == 0:
            current_count +=1
            freq[char] = 1
        else:
            freq[char] +=1

        # Now check if current_count == unique_count
        while current_count == unique_count:
            # Update min_len
            window_len = right - left +1
            if window_len < min_len:
                min_len = window_len

            # Try to move left
            left_char = s[left]
            freq[left_char] -=1
            if freq[left_char] ==0:
                current_count -=1
            left +=1

    print(min_len)

Wait, but when we subtract, we have to check if after decrementing, the count is zero. For example, if a character's count was 1, and we subtract 1, it becomes zero, so we need to decrease current_count.

Yes.

Wait, but in the code above, when adding a character to the frequency, we check if it's not in freq or its count is zero. But for existing entries, we have to increment the count. But perhaps a better approach is to initialize all possible characters to zero, but in a defaultdict(int), so that accessing them is possible.

Wait, the code as written may have a problem. For example, when we first encounter a character, we check if it's not in freq or freq[char] is 0. However, if it's not in freq, then adding it to freq and setting to 1. Else, if it's in freq but was zero (like after being decremented), then current_count is incremented.

But perhaps a better approach is to use a defaultdict(int), and each time a character is added to the window, increment its count. If the previous count was zero, then current_count increases.

So, in code:

from collections import defaultdict

n = int(input())
s = input().strip()

unique = set(s)
unique_count = len(unique)

if unique_count == 0:
    print(0)
else:
    min_len = n
    left = 0
    freq = defaultdict(int)
    current_unique = 0

    for right in range(n):
        char = s[right]
        freq[char] +=1
        if freq[char] ==1:
            current_unique +=1

        # Now try to minimize the window
        while current_unique == unique_count:
            window_size = right - left +1
            if window_size < min_len:
                min_len = window_size

            # Move left pointer
            left_char = s[left]
            freq[left_char] -=1
            if freq[left_char] ==0:
                current_unique -=1
            left +=1

    print(min_len)

Yes, this code should handle all cases.

Testing the first example:

Input:

3

AaA

unique_count is 2 (A and a).

The loop:

right=0: char is 'A', freq becomes 1. current_unique=1. Not equal to 2, loop continues.

right=1: char 'a', freq becomes 1. current_unique=2. Now enter the while loop.

window_size is 2. min_len is set to 2.

Then, subtract left_char (A), freq[A] becomes 0. current_unique reduces to 1. left becomes 1. exit loop.

right=2: char 'A'. freq[A] was 0, so adding 1. current_unique becomes 2 again. enter loop.

window_size is 2 (right=2, left=1: 2-1+1=2). min_len remains 2.

Then, subtract left_char (a) → freq[a] is 0. current_unique becomes 1. left=2. exit loop.

Loop ends. print 2. Correct.

Second example:

7

bcAAcbc

unique_count is 3 (b, c, A).

Looking for the minimal window. Let's see:

At some point, the window from index 3 (A) to 5 (c) would have all three?

Wait the string is 'bcAAcbc'.

Indices 0-based: 0: b, 1:c, 2:A, 3:A, 4:c, 5:b, 6:c.

The unique characters are b, c, A. The code's sliding window would find the minimal window. Let's see when right=2 (A), current_unique becomes 3. Then the window is 0-2 (b, c, A). size 3. Then, left moves to 1 (c), but the window now is 1-2 (c, A), which lacks 'b'. So current_unique becomes 2. Then the code proceeds.

But perhaps in another iteration, when right is 4 (c), the current_unique is 3 again. Let's see.

But perhaps the code finds the window from index 3 to 5. Let's see:

For example, when right=5 (b):

At this point, the code would have added the b. The current_unique would be 3 (A, c, b). The left pointer would start moving from 0 to find the minimal window.

But perhaps the code's logic would capture the window of size 3.

Well, the code would correctly find the minimal window.

Third example:

6

aaBCCe

unique_count is 4 (a, B, C, e).

The code would look for the minimal window containing all four. The sample expects 5.

The window is from index 1 (a) to 5 (e). That's a, B, C, C, e. So it includes a (from index 1), B (2), C (3,4), e (5). So all four types are present.

So in code, when right=5, the code would add e. Then current_unique is 4. Then the code enters the loop. The window is from left=0 to 5. The window size is 6. Then, move left to 1: subtract a (freq[a] becomes 1, which is still >=1. So current_unique remains 4. Now the window is 1-5 (size 5). Which is the minimal. So the code would update min_len to 5.

Thus, the code works.

Now, what about the edge case when n=1. Then the answer is 1.

Another edge case when all characters are same. Then the answer is 1.

The code handles these.

So the code should work.
</think>

```python
from collections import defaultdict

n = int(input())
s = input().strip()

unique_count = len(set(s))
if unique_count == 0:
    print(0)
else:
    min_len = n
    left = 0
    freq = defaultdict(int)
    current_unique = 0

    for right in range(n):
        char = s[right]
        freq[char] += 1
        if freq[char] == 1:
            current_unique += 1

        while current_unique == unique_count:
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                current_unique -= 1
            left += 1

    print(min_len)
```