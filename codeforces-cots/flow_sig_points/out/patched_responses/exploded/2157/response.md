<think>
Okay, I need to solve this problem where I have to find the number of distinct cyclic shifts of a given string. Let's think about how to approach this.

First, the problem says that each cyclic shift moves the last character to the front. So for a string like "abcd", each shift would generate "dabc", then "cdab", then "bcda", and so on. But the question is how many unique strings we get after doing all possible shifts.

The key idea here is to generate all possible cyclic shifts by rotating the string and then count how many unique ones there are. But for a string of length n, there are n possible shifts (including the original). So for example, a string of length 4 would have 4 shifts. However, some of these might be duplicates, like in the case of "bbb", all shifts are the same.

The straightforward approach is to generate all possible rotations, add them to a set to automatically handle duplicates, and then return the size of the set. That should work because sets only store unique elements.

But wait, what's the time and space complexity here? For a string of length up to 50, each rotation is O(n) time. Generating all n rotations would be O(n^2) time, which for n=50 is 2500 operations. That's totally acceptable for Python even under tight time constraints. The space is also manageable since each string is 50 characters, and there's up to 50 of them. So the set will store up to 50 elements, each 50 characters. No problem with memory.

So the plan is:

1. Read the input string.
2. Generate all possible cyclic shifts by moving the last character to the front each time. For each rotation, we can create the new string by taking s[-1] + s[:-1], since the last character becomes the first.
3. Collect all these shifted strings into a set.
4. The answer is the size of the set.

Wait, but how many shifts do we need to generate? For example, the original string is the first element, then each shift after that. For a string of length n, there are exactly n possible distinct shifts. So the loop should run n times, generating each possible shift once.

Let me test this logic with the examples.

First example: "abcd" has 4 shifts, all unique. So the set size is 4. Correct.

Second example: "bbb". All shifts will be "bbb", so the set has size 1.

Third example: "yzyz". Let's see:

Original: yzyz.

Shift 1: zyzy (last char is z, move to front: z + yzy → zyzy?)

Wait, original is yzyz. The first shift would take the last character (z), move it to front, resulting in zyzy. Then another shift would take the last character (y) and move to front: yzyz. Wait, but that's the original again. So the shifts alternate between the two. So after generating all possible shifts, the set will have two elements. So the loop for generating all shifts would be for n=4 steps. Each step adds the current shifted string to the set.

Wait, but how to generate all possible shifts. Let's see:

For a string s of length n, each cyclic shift is equivalent to rotating right by 1 each time. So after n shifts, we get back to the original string. So for each of the n shifts, we can generate the rotated version and add it to the set. The set will automatically track the unique ones.

So the algorithm would be:

- Initialize a set.

- For each k in 0 to n-1:

   - Take the string, rotate it right by k steps. But rotating right by k steps is equivalent to moving the last k characters to the front.

Wait, no. Each individual shift is moving the last character to front. So after one shift, it's right rotation by 1. After two shifts, it's right rotation by 2. So for example, the original string is s. Then after each shift, the new string is s shifted once, then shifted again.

So the way to generate all possible shifts is to start with the original string, then apply the shift (last to front) once, add that, then again, etc., for n times. But wait, for each shift, the current string is modified. But perhaps a better way is to generate each possible rotation by taking the original string and moving the last i characters (for i from 0 to n-1) to the front.

Wait, for example, the original string is s = s0 s1 s2 ... sn-1.

After 0 shifts, it's s. After 1 shift: s[-1] + s[:-1]. After 2 shifts: the first shift gives s1 = s[-1] + s[:-1], then the second shift would be s1[-1] + s1[:-1] = (s[:-1][-1]) + s[-1] + s[:-2]. Hmm, perhaps it's easier to generate each possible rotation as s[i:] + s[:i], but wait, no. Wait, rotating right once is equivalent to moving the last character to front. So for each rotation step, it's a right rotation by 1. So after k steps, the rotated string is the original string rotated right by k steps.

So how do we compute a right rotation by k steps? For example, the original string is abcd. A right rotation by 1: dabc. By 2: cdab. By 3: bcda. By 4: abcd again. So for each k from 0 to n-1, the rotation right by k steps is the same as taking the last k characters and moving them to front. So for example, right rotation by k steps would be s[-k:] + s[:-k].

Wait, yes. Because for k=1, s[-1:] is the last character, and s[:-1] is the rest. So the rotated string is last character + rest. For k=2, s[-2:] is the last two characters, and s[:-2] is the first two. So the rotated string is last two characters + first two. So for each k in 0 to n-1, the rotated string is s[-k:] + s[:-k], where when k is 0, s[-0:] is empty, but in Python s[-0:] is the same as s[0:], which is the entire string. So for k=0, the rotated string is the original. So for all k from 0 to n-1, we can generate the rotated string as s[-k:] + s[:-k].

So, for each k in 0 to len(s)-1, compute rotated string as s shifted by k steps (right rotation). Then add all these to a set. The size of the set is the answer.

This approach is better because generating each rotation directly from the original string, instead of applying shifts multiple times. Because applying shifts multiple times can lead to the same string as some rotation. For example, rotating once and then again gives the same as rotating twice from the original. So generating all possible rotations via this formula would be O(n) steps, each step O(n) time (since slicing and concatenating strings of length up to 50). Then adding to a set would take O(n) per insertion (since the string is up to 50 characters), but for n up to 50, this is manageable.

So the code would be:

s = input().strip()

n = len(s)

unique = set()

for k in range(n):

    rotated = s[-k:] + s[:-k] if k !=0 else s

    # Alternatively, for k=0, s[-0:] is the entire string, and s[:-0] is also entire string. So rotated = s.

    # So for all k in 0..n-1, rotated can be written as s[-k:] + s[:-k]

    unique.add( rotated )

print( len(unique) )

Wait, but in Python, s[-0:] is the same as s[0:], which is the entire string. Because negative indices wrap around. So when k=0, s[-0:] is the entire string. So for k=0, the rotated string would be s[-0:] (entire string) + s[:-0] (entire string), but s[:-0] is also the entire string. Wait, no. s[:-0] is the same as s[:0], which is empty. Because in Python, s[a:b] includes from a up to but not including b. So if k=0, then s[-k:] is s[0:], which is the entire string, and s[:-k] is s[:0], which is empty. So for k=0, rotated is s[-0:] + s[:-0] = s + "" = s. Which is correct.

Wait, for example:

s = "abcd"

k=0:

s[-0:] is "abcd", s[:-0] is empty. So rotated is "abcd" + "" = "abcd".

k=1:

s[-1:] is "d", s[:-1] is "abc" → rotated is "dabc".

k=2:

s[-2:] is "cd", s[:-2] is "ab" → rotated is "cdab".

k=3:

s[-3:] is "bcd", s[:-3] is "a" → rotated is "bcda".

k=4:

s[-4:] is "abcd", s[:-4] is empty → rotated is "abcd". So for k=4, which is len(s), it's same as k=0. But in our loop, we are running k from 0 to n-1. So n=4, k ranges 0,1,2,3. So all possible rotations are considered.

Yes, so the code can be written as:

s = input().strip()

n = len(s)

unique = set()

for k in range(n):

    rotated = s[-k:] + s[:-k]

    unique.add(rotated)

print(len(unique))

Wait, but when k=0, s[-0:] is the entire string (since -0 is 0). So s[-0:] is the same as s[0:], which is the entire string. Then s[:-k] is s[:-0], which is s[:0], which is the empty string. So rotated is entire string + empty, which is the original string. Correct.

So this code would correctly generate all possible rotations, including the original. Then add them to the set. The size of the set is the answer.

Testing the examples:

First example:

Input "abcd". For k=0: abcd. k=1: d + abc → dabc. k=2: cd + ab → cdab. k=3: bcd + a → bcda. So four unique entries. Set size 4. Correct.

Second example: "bbb". For all k, rotated will be "bbb". So set size 1.

Third example: "yzyz". Length 4.

k=0 → yzyz.

k=1 → z + yzy → zyzy.

k=2 → yz + yz → yzyz (since the string is "yzyz". Last two chars are yz, first two are yz. So rotated is yz + yz → yzyz. But wait, original is yzyz. So for k=2, the rotated string is s[-2:] + s[:-2]. s[-2:] is "yz", s[:-2] is "yz". So rotated is "yzyz" again. Then for k=3: s[-3:] is "zyz", s[:-3] is "y". So rotated is "zyz" + "y" → "zyzy".

So the set will have:

k=0 → yzyz

k=1 → zyzy

k=2 → yzyz (same as k=0)

k=3 → zyzy (same as k=1?)

Wait, no. Let me compute the rotations for "yzyz".

Original string is "yzyz".

k=0: rotated is "yzyz".

k=1: last character is z. rotated is z + yzy → zyzy.

k=2: last two characters are "z" and ""? Wait, no. The string is y z y z. So for k=2, the last two characters are the last two elements: "y" (index 3) and "z" (index 2? Wait, no. Let me think. Python uses 0-based indices. So for a string s = s[0], s[1], s[2], s[3]. So for "yzyz", indices 0: y, 1: z, 2: y, 3: z.

So s[-k:] when k=2 is s[-2:] → elements from index 2 to end → s[2], s[3] → 'y' and 'z' → "yz". Then s[:-k] is s[:2] → s[0], s[1] → "yz". So rotated is "yz" + "yz" → "yzyz".

k=3: s[-3:] is s[1:4] → z, y, z → "zyz". s[:-3] is s[:1] → "y". So rotated is "zyz" + "y" → "zyzy".

k=4 is not in the loop (n=4, loop is 0-3). So the generated rotated strings are:

k=0 → yzyz

k=1 → zyzy

k=2 → yzyz

k=3 → zyzy

So the set contains two elements. So the code would output 2, which matches the sample. So the code works.

Therefore, this approach should work.

Now, in terms of code optimization. Since the input can be up to 50 characters, and the code loops 50 times, each time creating a rotated string of up to 50 characters, this is O(n^2) time. Which is acceptable. The code is already efficient enough.

So the final code is as written above.
</think>

```python
s = input().strip()
n = len(s)
unique = set()
for k in range(n):
    unique.add(s[-k:] + s[:-k])
print(len(unique))
```