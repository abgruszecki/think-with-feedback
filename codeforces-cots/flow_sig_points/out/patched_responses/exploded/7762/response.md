<think>
Okay, let's see. The problem is to find the maximum number of "VK" substrings possible after changing at most one character in the given string. Hmm. So the steps I need to take are:

First, I need to calculate the original number of "VK" occurrences. Then, I need to consider all possible single changes (or none) to see which one gives the maximum increase in the count. But changing a character might affect overlapping parts. So how do I approach this?

Let me think. The initial count is straightforward: iterate through the string and count every "VK". Then, for each possible position in the string, try changing it to 'V' or 'K' and see how the count changes. But doing this naively for each position and each possible change (V to K or K to V) might be manageable since the string's maximum length is 100. So 100 positions, each with two possible changes (but maybe sometimes the same as original, so we can skip those). But even 100*2 is 200 possibilities, which is acceptable for the time constraints.

But wait, changing a character can affect not just the original VKs but also create new ones. For example, if the original string is "VV", changing the second V to K makes "VK". Or if the string is "KV", changing K to V gives "VV", which doesn't help. But changing the first K to V would make "VV", which also doesn't help. So the key is to find positions where changing the character could create a new "VK" in adjacent positions or break existing ones.

Wait, but changing a character might affect up to two possible VK pairs: the pair that includes the previous character and the current one (like i-1 and i), and the pair that includes the current character and the next one (i and i+1). So when we change s[i], we need to check the original VK count, then subtract any existing VKs that are now invalid, and add any new ones that are created by the change.

Alternatively, perhaps a better way is: for each possible change (each position and possible new character), create the modified string and then compute the number of VKs. Then take the maximum of all these possibilities. However, the original string (with no changes) is also a candidate.

But the original approach might be time-consuming for large strings, but since the maximum length is 100, even 100 * 2 possibilities (changing each position to either V or K, if different) is manageable. Let's confirm:

For a string of length 100, the number of possible modifications is 100 positions, each can be changed to V or K (if not already that). So for each position, up to 2 possibilities. But sometimes, changing a character to the same as it is would be a waste. So for each position, only 1 possible change (if original is V, then change to K; if K, change to V). Wait, but maybe changing to the same character would not help. For example, in the original string, maybe there's a position where changing to the same character (like a V to V) doesn't do anything, but this is not useful. So perhaps, for each position, try changing it to the other character. If it's V, try changing to K. If K, try to V. And also, the original string (no change) is another possibility.

Wait, but changing a character to the same as it is won't affect the count. So for example, if a position is V, changing it to V again doesn't do anything. So those cases can be skipped. So for each position, the possible changes are: to 'V' if it was 'K', and to 'K' if it was 'V'. So for each position, there's exactly one possible change (unless the character is already V or K, which they all are in the input). So per position, one possible change. Then, the total possible modified strings would be N (number of positions) plus the original. Wait, no: the original is one case. Then for each position, we can check the modified string where that position is flipped. So the total possibilities are 1 (original) + N (each position changed once). So for N=100, that's 101 possibilities. For each possibility, compute the number of VK's. Then take the maximum.

But wait, in some cases, changing a character might not just affect the immediate pairs. For example, if you have a sequence like "VKVVV", changing the third 'V' to 'K' would create a new VK at positions 3-4 (assuming the original is 'V'). Wait, no. Let's see: Original third character is 'V'. If we change it to 'K', then the new string is "VKKVVV". Then the pairs are VK (0-1), KK (1-2), KV (2-3), VV (3-4). So only the original VK exists. So changing that third character didn't help. Hmm.

But the point is that when you change a character, you need to check the neighboring positions. For example, changing position i from V to K would check the pairs i-1 and i (if i>0), and i and i+1 (if i < len(s)-1). So in the modified string, the VK count can be computed by first subtracting the original contributions from those pairs and adding the new contributions.

But this seems complicated. Maybe the easier way is to generate the modified string (for each possible change) and then count the VK's in it.

But for a string of length 100, generating a modified string (as a list) and then counting the VK's would be O(n) for each possibility. So 101 possibilities (original plus 100 changes) times 100 steps (counting VK's) would be 101*100 = 10100 operations. Which is acceptable.

So the plan is:

1. Compute the original count of VK's.

2. For each position in the string, try changing it to the other character (V becomes K, K becomes V), generate the new string, compute the count, and track the maximum.

3. The answer is the maximum between the original count and all these modified counts.

But wait, changing a character may not always be better. For example, the original count might already be the maximum possible. So the maximum of all possibilities is the answer.

But how to efficiently generate all these possibilities?

Let's think about the code.

First, the original count is easy. Then, for each position i in the string, create a new string where s[i] is flipped (V to K or K to V), then compute the count for this new string.

But in Python, strings are immutable. So each time, we can convert the string to a list, change the character, then convert back to a string. Or perhaps process the characters directly.

Alternatively, for each possible modification, loop through the characters and when at position i, check what the modified character would be.

But perhaps the easiest way is:

original = list(s)

max_count = count_vk(original)

for i in range(len(s)):

    # create a copy of original

    modified = original.copy()

    # flip the character at i

    modified[i] = 'K' if modified[i] == 'V' else 'V'

    # count VK in modified

    current = count_vk(modified)

    if current > max_count:

        max_count = current

return max_count

But since the original could be the best, we start with that. Then check all possible single flips.

Yes. That's manageable.

Now, how to implement count_vk efficiently.

The count_vk function can be implemented by iterating through the list from index 0 to len(s)-2, and checking if s[j] is 'V' and s[j+1] is 'K'. Each such occurrence increments the count.

So:

def count_vk(s):

    count = 0

    for j in range(len(s)-1):

        if s[j] == 'V' and s[j+1] == 'K':

            count +=1

    return count

So this is O(n) time per call.

So the total time is O(n) for the original count, plus O(n) * n for the modified possibilities. For n=100, that's 100 + 100*100 = 10100 operations. Which is well within time constraints.

But can we optimize this further?

Well, perhaps. Because when we flip a character at position i, the only possible changes in the count are in the pairs (i-1, i) and (i, i+1). So maybe instead of recomputing the entire count for each modification, we can compute the delta based on the original count.

This would reduce the time per modification from O(n) to O(1), which is better for large n. But since n is 100, even 100^2 is manageable, but for the sake of practice, let's think about this.

Original count is C.

For each modification at position i:

- The original character is c = s[i]. The new character is c' (flipped).

We need to check how this affects the count.

The affected pairs are:

- Pair (i-1, i): if i >0

- Pair (i, i+1): if i < len(s)-1

So in the original string, those pairs may have contributed to the count. In the modified string, those pairs may change.

So the steps for each modification:

1. Compute the original contribution of these two pairs.

2. Compute the new contribution after modification.

3. The new total count is C - original_contribution + new_contribution.

But we also need to check for other parts of the string. Wait, no. Because the modification only affects the pairs that include position i and their adjacent positions. So for example, changing s[i] will only affect the pairs (i-1, i) and (i, i+1). All other pairs are the same as before.

Therefore, the delta can be computed as follows:

original_contribution = 0

if i > 0:

    original_contribution += 1 if s[i-1] == 'V' and s[i] == 'K' else 0

if i < len(s)-1:

    original_contribution += 1 if s[i] == 'V' and s[i+1] == 'K' else 0

new_contribution = 0

new_char = 'V' if c == 'K' else 'K'

if i >0:

    new_contribution += 1 if s[i-1] == 'V' and new_char == 'K' else 0

if i < len(s)-1:

    new_contribution += 1 if new_char == 'V' and s[i+1] == 'K' else 0

delta = (new_contribution - original_contribution)

new_count = C + delta

So, this way, we can compute the new count in O(1) time per modification.

This would be better for larger n, but even for n=100, it's better.

So this approach would be more efficient.

So how to proceed:

1. Compute the original count C.

2. For each position i:

    a. Determine the original contribution of the pairs (i-1,i) and (i,i+1).

    b. Compute the new contribution after flipping s[i].

    c. Compute delta = new_contribution - original_contribution.

    d. The possible new count is C + delta.

    e. Keep track of the maximum possible new count.

3. The answer is the maximum between C and all the possible new counts from each i.

But wait, what about other possible changes in the string when we flip i? Like, for example, if flipping i creates a new VK in a different part of the string. Wait no, flipping i can only affect the pairs (i-1,i) and (i,i+1). Other pairs are not affected.

So this approach is correct.

So this way, the time complexity is O(n) for the original count, then O(n) for each modification, each in O(1) time.

So overall O(n) time.

This would be better for very large n, but even for n=100, it's negligible. But since in code it's easy to implement, perhaps this approach is better.

So, how to implement this.

First, compute the original count.

Then, for each i in 0..n-1:

Compute the original contribution of (i-1, i) and (i, i+1).

original_contribution = 0

if i > 0:

    original_contribution += 1 if s[i-1] == 'V' and s[i] == 'K' else 0

if i < len(s)-1:

    original_contribution += 1 if s[i] == 'V' and s[i+1] == 'K' else 0

Then, compute new_char as 'V' if s[i] is 'K' else 'K'.

new_contribution = 0

if i >0:

    new_contribution += 1 if s[i-1] == 'V' and new_char == 'K' else 0

if i < len(s)-1:

    new_contribution +=1 if new_char == 'V' and s[i+1] == 'K' else 0

delta = new_contribution - original_contribution

max_count = max(max_count, original_count + delta)

But wait, original_count is the original count. But when we flip i, the delta is the change in the count, so original_count + delta is the new count after flipping i.

So this approach would work.

Now, the original_count is the count of all VK pairs. When we flip i, the only pairs that change are the two adjacent pairs. So the delta is the difference in those pairs.

Thus, for each flip, the code can calculate the delta and see if it improves the count.

But we also need to consider that flipping i could potentially create new VK pairs elsewhere. Wait, no. Because flipping i only affects the pairs (i-1, i) and (i, i+1). So the delta correctly captures the change.

For example, consider the string "VVV". The original count is 0. If we flip the third V to K, making "VVK", then the count is 1 (from VVK, VK at positions 1 and 2). The delta here would be 1 (original contribution for the third character: when i=2 (0-based), the pairs are (1,2) and (2,3) (but 3 is out of bounds). So original contribution is 0 (since s[2] is V, and pair (1,2) is VV which contributes 0. Then new_char is K. So pair (1,2) becomes VK, contributing 1. So delta is 1. Original count is 0, so new count is 1. Which is correct.

Another example: original string is "VK". The original count is 1. If we flip the first character to K (resulting "KK"), the delta would be:

original contribution for i=0:

pair (0,1): original contributes 1 (since VK is present). Then new_char is K. Pair (0,1) is KK. So new_contribution is 0. So delta is 0 -1 = -1. So new count is 1 -1 = 0.

Similarly, if we flip the second character to V (resulting "VV"), the delta for i=1:

original contribution: pair (0,1) is VK (contributes 1), pair (1,2) is out of bounds. So original_contribution is 1. new_char is V. pair (0,1) is VV (contribution 0). So delta is 0-1 = -1. new count is 1-1=0.

Thus, the code would correctly capture that flipping either character would reduce the count.

So this approach is correct.

Thus, the code can be written as:

Compute original_count.

Compute the maximum possible as original_count, then check for each i:

compute delta as (new_contribution - original_contribution) for flipping s[i], and see if original_count + delta is larger.

So, the code can be optimized as follows.

But first, let's handle the original_count.

Now, the code steps:

Read the string s.

original_count = 0

n = len(s)

for j in range(n-1):

    if s[j] == 'V' and s[j+1] == 'K':

        original_count +=1

max_count = original_count

for i in range(n):

    original_contribution = 0

    # check left pair (i-1, i)

    if i >0:

        if s[i-1] == 'V' and s[i] == 'K':

            original_contribution +=1

    # check right pair (i, i+1)

    if i < n-1:

        if s[i] == 'V' and s[i+1] == 'K':

            original_contribution +=1

    # new character

    new_char = 'K' if s[i] == 'V' else 'V'

    new_contribution =0

    # check left pair with new_char

    if i >0:

        if s[i-1] == 'V' and new_char == 'K':

            new_contribution +=1

    # check right pair with new_char

    if i <n-1:

        if new_char == 'V' and s[i+1] == 'K':

            new_contribution +=1

    delta = new_contribution - original_contribution

    current = original_count + delta

    if current > max_count:

        max_count = current

print(max_count)

Yes, that's the code. Let's test with some examples.

First example: input 'VK' (length 2). Original count is 1. For each position:

i=0:

original_contribution is left pair (i-1= -1, no) and right pair (0,1) which is VK: contributes 1. So original_contribution =1.

new_char is K (since s[0] is V). new_contribution: left pair (no), right pair (i=0, i+1=1: new_char is K, s[1] is K. So pair is KK. No contribution. So new_contribution is 0. delta is -1. current is 1-1=0. max remains 1.

i=1:

original_contribution: left pair (0,1) is VK (contributes 1). right pair (1,2) is no. So original_contribution=1.

new_char is V (since s[1] is K). new_contribution: left pair (0,1): s[0] is V, new_char is V: VV. 0. right pair (1,2): no. new_contribution=0. delta -1. current 0. max remains 1.

Thus, the maximum is 1. Correct.

Second example: 'VV'. Original count is 0.

i=0:

original_contribution: left pair is no. right pair (0,1) is VV: 0. original_contribution=0.

new_char is K. new_contribution: right pair (0,1) is K and V: KV. So 0. So delta 0. current count remains 0.

But wait, changing first V to K would make 'KV'. Then the count is 0.

But i=1:

original_contribution: left pair (0,1) is VV: 0. right pair is no. original_contribution=0.

new_char is K. new_contribution: left pair (0,1) is V and K: VK. So contributes 1. So new_contribution=1. delta=1-0=1. current is 0+1=1. So max becomes 1. Correct.

Thus, code works.

Another example: input is 'V'. Only one character, so original count is 0. All possible modifications (change to K). Then, no pairs. So maximum remains 0.

Fourth example: "VKKKKKKKKKVVVVVVVVVK".

Original count: let's see.

Looking for 'VK's.

Original string:

V K K K K K K K K K V V V V V V V V V K

So the VK's are:

At positions (0,1) VK. Then K's follow. Then when V starts again, V followed by V, so no. Then the last V followed by K (positions 18 and 19?), so that's another VK. So original count is 2?

Wait, the example's output after modification is 3. Hmm.

But according to the code, when we flip a certain position, the delta is considered.

But perhaps the code will correctly calculate that flipping a K to V creates a new VK.

But regardless, the code is supposed to handle all possibilities.

But in the code's approach, for each possible flip, the delta is computed correctly.

Thus, the code should work for all cases.

So this approach is correct and efficient. The code will run in O(n) time, which is optimal for the problem's constraints.

Now, implement this in Python.

So the code is:

Read s.

Compute original_count.

Iterate through each i to compute possible delta.

Take the maximum.

So the code:

s = input().strip()

n = len(s)

original_count = 0

for j in range(n-1):

    if s[j] == 'V' and s[j+1] == 'K':

        original_count +=1

max_count = original_count

for i in range(n):

    original_contribution = 0

    if i > 0:

        if s[i-1] == 'V' and s[i] == 'K':

            original_contribution +=1

    if i < n-1:

        if s[i] == 'V' and s[i+1] == 'K':

            original_contribution +=1

    new_char = 'K' if s[i] == 'V' else 'V'

    new_contribution = 0

    if i > 0:

        if s[i-1] == 'V' and new_char == 'K':

            new_contribution +=1

    if i < n-1:

        if new_char == 'V' and s[i+1] == 'K':

            new_contribution +=1

    delta = new_contribution - original_contribution

    current = original_count + delta

    if current > max_count:

        max_count = current

print(max_count)

Yes. Let's test this code with the sample inputs.

Sample 2 input: "VV".

original_count is 0.

For i=0:

original_contribution: left is none. right is VV: 0. so original_contribution=0.

new_char is K. right pair (0,1) becomes KV. contribution 0. delta is 0. current 0.

For i=1:

original_contribution: left pair (0,1) is VV: 0. right none. original_contribution=0.

new_char is K. left pair (0,1) becomes VK: contribution 1. delta is 1. current 0+1=1. So max becomes 1.

Thus, output is 1. Correct.

Sample input 4: the code will find that changing a certain position gives delta 1, leading to 3.

Sample input 5: "KVKV". Original string is K V K V. The original count is 1 (positions 1-2: VK). After flipping each position:

For example, flipping the first K to V gives VVKV. Then VV has no, VK (positions 1-2: VK), and KV (positions 2-3). So count is 1. Flipping the second V to K gives KKKV: no VK. Flipping third K to V: KV K becomes V. So the string becomes KV V V. The pairs are K V (0-1), V V (1-2), V V (2-3). Count is 1. Flipping fourth V to K: KVKK. The pairs are K V, V K (positions 1-2: VK? No, position 1 is V, position 2 is K? So VK at 1-2. So count is 1. So the maximum is 1. Correct.

Thus, the code seems to handle all cases.
</think>

```python
s = input().strip()
n = len(s)
original_count = 0

for j in range(n - 1):
    if s[j] == 'V' and s[j+1] == 'K':
        original_count += 1

max_count = original_count

for i in range(n):
    original_contribution = 0
    if i > 0:
        original_contribution += (s[i-1] == 'V' and s[i] == 'K')
    if i < n - 1:
        original_contribution += (s[i] == 'V' and s[i+1] == 'K')
    
    new_char = 'K' if s[i] == 'V' else 'V'
    new_contribution = 0
    if i > 0:
        new_contribution += (s[i-1] == 'V' and new_char == 'K')
    if i < n - 1:
        new_contribution += (new_char == 'V' and s[i+1] == 'K')
    
    current = original_count + (new_contribution - original_contribution)
    if current > max_count:
        max_count = current

print(max_count)
```