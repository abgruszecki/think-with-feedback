<think>
Okay, let's tackle this problem. So the goal is to find the maximum possible length of a zebra, which is a contiguous sequence of alternating 'b' and 'w' characters. But before that, Grisha can perform some operations where he splits the string into two parts, reverses each, and then concatenates them. Hmm. Wait, the operation is splitting into two parts, reversing each part, and then sticking them together. So for example, if the original is s = a + b where a and b are two parts, then after the operation, it becomes reverse(a) + reverse(b). Or wait, is it reversed each part and then concatenated in the same order? Like, split into left and right, reverse left part, reverse right part, then combine. So the overall effect is that the new string is reverse(left_part) + reverse(right_part). So the entire string becomes (reverse of left) followed by (reverse of right). 

But since Grisha can perform this operation any number of times (including zero), the problem is to find the maximum possible zebra length possible in any string obtainable through these operations. But how do these operations affect the possible sequences? Because each operation allows certain transformations of the string.

Wait, but maybe there's a way to model all possible transformations that these operations allow, and then find the maximum zebra length possible in any of those transformed strings. But considering that the number of possible transformations is potentially infinite, we need a smarter approach.

Alternatively, maybe we can find that these operations allow certain rearrangements of the original string, and the maximum zebra can be found by considering cyclic shifts or something similar. Wait, perhaps not. Let me think.

Let's consider the possible transformations. Let's say the original string is split into two parts. Then each part is reversed. For example, if the original is ABCDEF, and we split into ABC | DEF. Then reverse each part to get CBA and FED, then concatenate to get CBAFED.

Alternatively, if we perform the same operation again on the new string. For example, split CBAFED into CB | AFED. Then reverse each part: BC and DEFA. Concatenate gives BCDEFA. Hmm. But each operation is a split at some position, reverse each part, then put them back. So each operation can be done at any split point.

But the key observation here might be that these operations allow us to create any possible rotation of the original string. Because by splitting and reversing, perhaps we can rotate the string. Wait, let's see.

Take the example: original is s = s1 s2 s3 ... sn. Suppose we split at position k, then reverse each part. The new string is reverse(s1...sk) + reverse(sk+1...sn). Let's see for some examples.

Original: ABCD. Split after B: AB|CD → reverse(AB) is BA, reverse(CD) is DC → BA + DC = BADC.

If we split again after the third character (BA D | C), reversing each part would give DAB and C → DAB C → DABC.

Hmm, not sure. But maybe there's a way to rearrange the characters into any possible order. But that's probably not the case. For example, if the original string is 'bb', then any operation would reverse the entire string (if split at 0 or 2) or parts. But since both parts are reversed and then concatenated, the string remains 'bb' in any split. So in that case, the maximum zebra length is 1. Wait, but if the original is 'bb', then each split would reverse parts. For example, split at position 1: 'b' and 'b'. Reverse each part gives 'b' and 'b' → concatenated as 'bb' again. So in this case, no operation can change the string. So the maximum zebra is 1 (since each 'b' is a single-length zebra, but the maximum consecutive alternation is 1).

So perhaps the allowed operations don't allow arbitrary permutations. So the problem reduces to finding, among all possible strings that can be formed through these operations, the maximum zebra length possible.

But how can we model all possible strings that can be formed through these operations? That seems tricky. Let's think differently.

Another approach: the maximum possible zebra length is the maximum length of a substring in the original string, or in the concatenation of the string with itself (since after some splits and reverses, maybe we can create a circular arrangement). Wait, perhaps the maximum zebra can be found by considering the string as a circular one, allowing the zebra to wrap around the end and the beginning.

Wait, for example, consider the string 'bwbbw' as in the problem statement. After some operations, like splitting and reversing, maybe the string can be transformed into a sequence that allows a longer zebra by wrapping around. But how?

Alternatively, let's think that each operation allows us to rotate the string. For example, splitting the string into two parts and reversing each part can lead to a rotation. Let's see:

Take 'abcd'. Split into 'ab' and 'cd', reverse each to get 'ba' and 'dc', concatenated as 'badc'. Then split again into 'ba' and 'dc', reverse each again to get 'ab' and 'cd', which gives 'abcd' again. Hmm, not helpful.

Alternatively, maybe the key is that after any number of operations, the possible strings are the same as the original string and the reverse of the original string. But that's not true. For example, take 'abc'. Split into 'a' and 'bc'. Reverse each to get 'a' and 'cb' → 'acb'. Then split into 'ac' and 'b', reverse each to get 'ca' and 'b' → 'cab'. So new strings are possible.

Hmm. So the operations can generate more than just the original and its reverse. So this approach is not straightforward.

Alternative idea: The problem allows us to perform any number of split and reverse operations. But each operation is equivalent to splitting the string into two parts, then reversing each part. But perhaps after a certain number of operations, the possible strings are equivalent to any possible split and reverse combinations. Wait, but how?

Alternatively, perhaps after some operations, the string can be transformed into any possible rotation. Let's see.

Suppose the original string is s = s1 s2 ... sn. Let's say I want to create a rotation where the string starts at sk and then continues from s1. For example, for s = abcd, rotation starting at c is cdab.

Is this possible through split and reverse operations?

For example, to get 'dabc' from 'abcd', can we do it?

Original: abcd → split into a|bcd → reverse each part to get a and dcb → concatenated as a dcb → adcb.

Then split adcb into ad|cb → reverse each part: da and bc → da bc → dabc. Yes! So here, after two operations, we rotated the string.

So in this case, the rotation is achieved. So perhaps the allowed operations allow any rotation of the original string.

Wait, but how?

If that's the case, then the maximum possible zebra length would be the maximum length of a sequence of alternating 'b's and 'w's in any rotation of the original string. Because after any number of split and reverse operations, we can create any rotation.

But how can we confirm this?

Alternatively, perhaps each split and reverse operation can be considered as a rotation. For example, let's see:

Suppose the original string is split into left and right. After reversing each part and concatenating, the new string is (reverse(left) + reverse(right)).

But if we split the original string into left and right, then reverse both parts and concatenate, perhaps this is equivalent to some rotation. Not sure.

But perhaps the key insight here is that by performing these operations, the string can be rotated in such a way that any starting point can be chosen, and then the string is arranged in some order. Thus, the maximum zebra is equivalent to the maximum possible in the original string or any of its rotations.

If that's the case, then the problem reduces to finding the maximum length of a zebra in all possible rotations of the original string. Because then, the allowed operations can produce any rotation.

But how to verify this?

Alternatively, consider that each split and reverse operation can be used to rotate the string. For example:

Let's take the string s = s0 s1 s2 ... s(n-1).

If we split at position k, then the reversed left part is s(k-1) s(k-2) ... s0, and the reversed right part is s(n-1) s(n-2) ... s(k). Then the new string is reversed left + reversed right = [s(k-1)...s0] [s(n-1)...s(k)].

Now, if we split again at position (n-k), then the left part is [s(k-1)...s0] and the right part is [s(n-1)...s(k)], but split into two parts. Hmm, perhaps this can be combined in a way to create a rotation.

Alternatively, perhaps after a split and reverse, the string can be considered as a reversed left part followed by a reversed right part. Then, by choosing the split points appropriately, the reversed left and right can form a rotation of the original string.

But I'm not sure. Maybe the key is that after a series of operations, the string can be transformed into any possible rotation. For example, the first split and reverse can be used to reverse the entire string, and then subsequent splits can allow rotations.

Alternatively, think of the string as a circular array. Each split and reverse operation allows us to reverse some prefix and suffix of the circular array. Wait, but how?

Alternatively, here's an observation: since the split can be at any position, including the beginning (split at 0) or the end (split at the entire length). Splitting at the beginning would result in the left part being empty, so reverse(left) is empty, and reverse(right) is the entire string reversed. So the new string is the reverse of the original. Similarly, splitting at the end would reverse the entire string (since right part is empty). So by doing that, we can reverse the entire string.

But then, after that, any split and reverse operations can be done again. So perhaps after reversing the entire string, and then splitting again, we can create any possible rotation.

But I'm not entirely sure. Let's think of an example.

Take the string 'abcd'. Let's split at 0 to reverse the entire string, resulting in 'dcba'. Then split again at 1: left is 'd', reversed is 'd'; right is 'cba', reversed is 'abc'. So new string is 'dabc'. That's a rotation of the original string. So here, after two operations, we achieved a rotation.

Similarly, if we split 'dcba' at 2, left is 'dc', reversed is 'cd'; right is 'ba', reversed is 'ab'. So concatenated as 'cdab', another rotation.

So perhaps, through these operations, we can generate any rotation of the original string, as well as any rotation of its reversed string.

If that's the case, then the maximum possible zebra can be found by considering the original string and all possible rotations of it, as well as rotations of the reversed string. But since the reversed string's rotations are just the rotations of the original string's reverse, perhaps we can model this by considering the original string concatenated with itself (so that any rotation is a substring of length n of this doubled string), and the same for the reversed string.

So the approach would be:

1. Generate all possible rotations of the original string and its reverse. But since n can be up to 1e5, generating all rotations is not feasible.

But, for the purpose of finding the maximum zebra length, perhaps the maximum is either in the original string, or in the original string concatenated with itself (to account for rotations), or in the reversed string concatenated with itself. So, for example, the maximum zebra can be found by looking for the longest alternating sequence in s + s, but considering only sequences of length up to n. Because a rotation would allow the sequence to wrap around the end and the beginning.

Similarly, the reversed string's concatenation may also be considered.

But why?

Well, because the allowed operations can generate any rotation of the original or reversed string, the maximum zebra must be in one of these rotations. So by considering the doubled strings (original + original, reversed + reversed), we can find all possible rotations' contiguous substrings.

Wait, but how? For example, the string 'abcd' when concatenated with itself becomes 'abcdabcd'. Any rotation of 'abcd' is a substring of length 4 in this concatenated string. For example, rotation by 1 is 'bcda' which is the substring starting at index 1. So, by looking at the original string concatenated with itself, we can process all possible rotations as substrings of length n.

So, the approach would be:

- Compute the maximum zebra length in the original string.

- Compute the maximum zebra length in the original string concatenated with itself (for rotations).

- Compute the maximum zebra length in the reversed string concatenated with itself.

Take the maximum of all these.

Wait, but the reversed string can be generated by splitting at the start (as discussed earlier). So rotations of the reversed string are also allowed.

So, to cover all possible rotations of the original and reversed strings, perhaps the maximum zebra can be found by checking the original string and its reversed, each concatenated with themselves, and find the maximum possible zebra in any of those, but considering that the maximum length cannot exceed n.

So the steps would be:

1. Generate s_rot = s + s

2. Generate s_rev_rot = reversed(s) + reversed(s)

3. For each of these four strings (original s, s_rot, reversed(s), s_rev_rot), compute the maximum zebra length, but limiting the maximum to the original length n.

Wait, but why four? Maybe not. Let's think: the original s is part of s_rot. The reversed s is part of s_rev_rot. So perhaps the maximum can be found by processing s_rot and s_rev_rot.

But perhaps the reversed string's rotations can be covered by processing the reversed(s) concatenated with reversed(s), but that's the same as s_rev_rot.

So the plan is:

- Compute the maximum zebra length in s_rot (original string concatenated with itself), but considering substrings of length up to n.

- Compute the maximum zebra length in s_rev_rot (reversed string concatenated with itself), same as above.

- Take the maximum of these two values.

But why include the original and reversed? Because s_rot includes all rotations of the original string. For example, the original s is a rotation of zero shifts, which is part of s_rot.

Similarly, s_rev_rot includes all rotations of the reversed string, which can be generated via the allowed operations.

So, by considering s_rot and s_rev_rot, we can find the maximum possible zebra length.

Then, the solution is to compute the maximum possible zebra length in s_rot and in s_rev_rot, and then take the maximum of those.

Wait, but what about the reversed string concatenated with itself? For example, if the original is 'bwbbw', then reversed is 'wbbwb'. Then s_rev_rot is 'wbbwbwbbwb'. Processing this for maximum zebra in any substring of up to 5 characters.

But how?

Alternatively, perhaps the maximum zebra can be found by considering all possible starting positions in s_rot and s_rev_rot, and finding the longest possible alternating sequence.

But how to compute that efficiently.

So, the algorithm would be:

For each string in [s_rot, s_rev_rot], compute the maximum length of a contiguous substring of alternating characters. Then, the overall maximum is the maximum between these two, but also considering that the maximum cannot exceed the original length n.

Wait, but in s_rot, which is s + s, the maximum possible zebra in a substring of length up to n.

Because, the allowed operations can create any rotation of the original string, which is a substring of length n in s_rot. Similarly for reversed rotations.

So, the problem reduces to finding the maximum zebra length in s_rot and s_rev_rot, but considering only substrings up to length n.

But how to compute this.

The approach to find the maximum length of a zebra (alternating characters) in a string is to traverse the string and track the current run length. Whenever the next character is different from the previous, increment the current run. Otherwise, reset the current run to 1. Keep track of the maximum encountered.

But for the rotated cases, the maximum can be in the middle of s_rot, which represents a rotation. For example, in the first example input:

Input is 'bwwwbwwbw'. The s_rot would be 'bwwwbwwbwbwwwbwwbw'. In this case, the maximum zebra is 5, which is part of a rotation. So, when processing s_rot, the code would find that.

But how to handle the wrapping around? For example, the maximum zebra could start near the end of s and wrap around to the beginning. That is, in s_rot, the substring might start at position n-2 and extend into the concatenated part.

So, processing s_rot as a single string and looking for the maximum alternating sequence (of any length, but up to n) would capture this.

So, the steps are:

1. For the original string s, compute the maximum zebra length.

2. For s concatenated with s, compute the maximum zebra length.

3. For the reversed s concatenated with reversed s, compute the maximum zebra length.

Take the maximum of all these.

But wait, maybe the maximum in the original s is already captured in the s_rot, so perhaps steps 1 and 2 can be merged.

So, perhaps it's sufficient to compute the maximum in s_rot and s_rev_rot, and take the maximum between them. But also, perhaps the reversed s_rot would include the same possibilities as s_rev_rot, but I'm not sure.

Alternatively, maybe the maximum zebra can be found by checking s_rot and s_rev_rot, and the original s and reversed s. But given that s_rot includes the original s, and s_rev_rot includes the reversed s, perhaps the maximum of s_rot and s_rev_rot is sufficient.

So, the code would be:

s = input().strip()

max_len = 0

def compute_max(s):
    max_zebra = 1
    current = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            current += 1
            if current > max_zebra:
                max_zebra = current
        else:
            current = 1
    return max_zebra

s_rot = s + s
s_rev_rot = s[::-1] + s[::-1]

max1 = compute_max(s_rot)
max2 = compute_max(s_rev_rot)

# The maximum possible in s_rot or s_rev_rot could be up to 2n, but the actual maximum allowed is n.
result = max(max1, max2, 1)  # at least 1

# But since the maximum possible zebra in the original or reversed rotations is up to n, we cap it at n.
result = min(result, len(s))

# Wait, but for example, if the entire s_rot has a zebra of length 2n (all alternating), then the maximum possible is n (since the original string's rotations can't have longer than n). So the code would cap it to n.

But how to handle cases where the maximum zebra is in the middle of s_rot and longer than n. For example, if s is 'wbwb', then s_rot is 'wbwbwbwb'. The maximum zebra is 4 (the original is already a perfect alternation). So in this case, compute_max(s_rot) would return 4, which is n. So the code would return 4, which is correct.

Another example: if s is 'bw', then s_rot is 'bwbw'. compute_max would return 2, which is correct.

So the code would take the maximum of the two computed max values (from s_rot and s_rev_rot), but then cap it to the length of s. Because even if s_rot's maximum is 2n (if the entire string is a perfect alternation), the actual maximum allowed is n, as any rotation is a substring of s_rot of length n.

Wait, but how? For example, if s is 'wb' which is length 2. s_rot is 'wbwb'. compute_max would return 4, but the maximum possible zebra is 2 (since the original length is 2). So by capping the result to len(s), the code would return 2, which is correct.

So, the code should take the maximum of the two computed values (max1, max2) and then take the minimum between that and len(s).

But wait, maybe the maximum zebra in s_rot is 5 for a string of length 5 (like in the first example). Then min(5, 5) would return 5, which is correct.

So the code would proceed as follows:

Compute the maximum zebra in s_rot and s_rev_rot, then take the maximum between them, and finally cap it at len(s).

So the code would be:

s = input().strip()

n = len(s)
if n == 0:
    print(0)
else:
    def compute_max(s):
        max_zebra = 1
        current = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                current +=1
                if current > max_zebra:
                    max_zebra = current
            else:
                current = 1
        return max_zebra

    s_rot = s + s
    s_rev_rot = s[::-1] + s[::-1]

    max_rot = compute_max(s_rot)
    max_rev_rot = compute_max(s_rev_rot)

    result = max(max_rot, max_rev_rot, 1)  # at least 1
    result = min(result, n)  # can't be longer than the original string length

    print(result)

Wait, but why do we need to compute the maximum of max_rot and max_rev_rot? Because the allowed operations can generate any rotation of the original and the reversed string. So the maximum zebra could be in either of those.

But let's test this code against the examples.

First example:

Input: bwwwbwwbw → output is 5.

The original string is 'bwwwbwwbw' (length 9).

s_rot is the original concatenated with itself. Let's see what the compute_max would find.

But the maximum in s_rot would be 5. Similarly, the reversed string is 'wbwwbwwwb', then reversed_rot is that concatenated with itself. compute_max on that would also find 5.

So the code would return 5.

Second example: input is bwwbwwb → output 3.

Original length is 7.

s_rot would be 'bwwbwwbbwwbwwb'. compute_max finds the maximum in this. Let's see:

Original string: 'b w w b w w b'

Looking for alternating sequences:

The original string has sequences like 'b' (1), 'w' (1), etc. The maximum is 3 (like 'bwwb' → but no, the alternation is b, w, w, which is invalid. Wait the example's output is 3, which comes from 'b w w b' but no. The second example's note says that the answer is 3, which may be 'b w w' → no. Wait, perhaps in the original string, there's a sequence of 'b w w b w w b', so the maximum is 3 (like 'b w b').

But according to the code, when processing s_rot, which is 'bwwbwwbbwwbwwb' (original plus original), the code would check for the maximum alternating sequence. Let's see:

In the original s, the maximum is 3 (like the substring 'bwwb' gives 'b w w b' → which has alternating only in the first two steps. Wait, maybe the code is correct.

But in any case, according to the code, the maximum in s_rot would be 3. The reversed s is 'bwwbwwb' reversed → 'bwwbwwb' → same as original? Wait, original is 'bwwbwwb' (length 7). Reversed is 'bwwbwwb' → same as original. So s_rev_rot is same as s_rot. So compute_max on s_rev_rot would also return 3. So code returns 3, which matches the example.

So the code seems to handle the examples correctly.

But wait, what about the case where the maximum zebra is obtained by a rotation of the reversed string? For example, the original is 'bwbbw', and the reversed is 'wbbwb'. Maybe a rotation of the reversed string gives a longer zebra. So the code's approach would check that.

But the code's approach of considering both s_rot and s_rev_rot covers that.

Now, time and space constraints.

The code constructs s_rot and s_rev_rot, each of length 2n, where n can be up to 1e5. So 2e5 each, which is manageable in terms of memory.

The compute_max function is O(2n) for each of the two strings. So overall O(n) time.

Thus, for n up to 1e5, the code would run in O(n) time, which is acceptable.

Another test case: the string is all 'b's. Then the maximum zebra is 1. The code would compute compute_max for s_rot as 1 (since all are 'b's). Then, the code returns min(1, n) → 1. Correct.

Another test case: 'wbwb', which has a maximum zebra of 4. s_rot is 'wbwbwbwb'. compute_max returns 4. min(4,4) → 4. Correct.

Another case: 'wbw' → maximum zebra is 3. s_rot is 'wbwwbw'. compute_max would find 3 (the entire original is 'wbw', which is 3 alternating), and the code returns 3.

But what about a case where the maximum is in a rotation. For example, 'wwwb', original maximum is 2 (the 'wb' part). But when rotated, say 'bwww' → but that's same as original. Wait, perhaps another example. Take 'bwwwb'. Original has a zebra of 2 (b w, or w b). But after rotating to 'wwwbb', which is not a rotation. Hmm, perhaps the example is not good.

Alternatively, consider 'bwbww'. The original's maximum zebra is 3 (b w b). But after rotation to 'wbbww', the maximum is 3 (w b b → no, that's not alternating. Hmm, maybe not. So perhaps the code is correct.

So, in conclusion, the approach is to compute the maximum zebra length in s_rot and s_rev_rot, then take the minimum between that maximum and the original string length. This works because the allowed operations can generate any rotation of the original and reversed strings, and the maximum possible zebra is found in those rotations.

Therefore, the code should look like this.
</think>

```python
s = input().strip()
n = len(s)
if n == 0:
    print(0)
else:
    def max_zebra(s):
        max_len = current = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                current += 1
                if current > max_len:
                    max_len = current
            else:
                current = 1
        return max_len

    s_rot = s + s
    s_rev_rot = s[::-1] + s[::-1]
    max_val = max(max_zebra(s_rot), max_zebra(s_rev_rot))
    print(min(max_val, n))
```