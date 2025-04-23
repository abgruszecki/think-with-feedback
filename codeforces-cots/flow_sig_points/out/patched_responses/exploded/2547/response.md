<think>
Okay, let's see. The problem is that after a series of m swaps between pairs of characters, we need to find the final string. Each swap for a designer replaces all occurrences of xi with yi and vice versa in the current version of the name. But since the swaps are applied in sequence, each subsequent swap is based on the latest version of the string.

Hmm, the challenge here is to efficiently apply m swaps, each potentially affecting the entire string, but with m up to 200,000 and n up to 200,000, a naive approach of processing each swap by iterating through the entire string each time would be O(m*n), which would be 4e10 operations. That's way too slow. So we need a smarter way.

Wait, each swap is between two characters. But if we have a series of swaps, maybe we can track the mapping of each character through all the swaps, then apply the final mapping to the original string once.

Yes, that's the key. Because each swap is reversible. For example, if the first swap is a <-> b, then the second is b <-> c, the overall effect is that any original a would become b after the first swap, then that b becomes c in the second. But if we track the transformations in reverse order, perhaps we can compute the final mapping.

Wait, no. Because each swap affects all current characters. So the order matters. Let's think: For each character in the original string, after all swaps, what character does it become?

Wait, but each swap is a substitution of x and y. So for example, if we have a series of swaps like swap x1 and y1, then swap x2 and y2, etc. Each swap affects the current mapping. So perhaps we can model the transformations as a series of transpositions and track for each possible character what it ends up being after all swaps.

Let's model this as a permutation. For each character, we need to track through all the swaps. But since each swap is a transposition (swap x and y), we can represent the current mapping as a dictionary or array where for each character, we know what it's been transformed to after all swaps up to that point.

But how? Let's think. Let's say we start with a mapping that is identity: each character maps to itself. Then, for each swap between x and y in the order they are applied, we need to update the mapping. For example, if the current mapping is such that x is mapped to a and y is mapped to b, then swapping x and y would mean that any occurrence of x in the current name (which is the result of previous mappings) will become y, and vice versa. Wait, no. Let's clarify:

Each swap operation swaps the current x_i and y_i in the string. But the way the swaps are applied is that each subsequent swap is applied to the result of the previous swaps. So the order is important. So for the first swap, x1 and y1 are swapped. Then, in the resulting string, the second swap is applied, which swaps x2 and y2, but x2 and y2 refer to the characters as they are in the current string after the first swap.

But we need to model this as a transformation of the original characters. Let's think in terms of a mapping that represents for each original character, what it should be transformed into after all swaps. Then, when processing each swap, we adjust this mapping.

Wait, maybe not. Let's consider that the swap operations are applied in sequence. For each swap (xi, yi), we need to swap the current mapping for xi and yi. Because when a swap happens between xi and yi, any occurrence of xi (as per the current mapping) becomes yi, and vice versa. So the mapping after that swap would be such that, in the future swaps, the new xi and yi are considered based on the current mapping.

Wait, perhaps the correct approach is to maintain a mapping that tells, for each original character, what it's been transformed to through all swaps so far. Then, when a swap (x, y) is applied, we need to find which original characters would now map to x and y, and swap their mappings. Or wait, maybe not. Let's try with an example.

Suppose the initial mapping is identity. Then we apply a swap between a and b. So after this swap, the mapping for a becomes b, and the mapping for b becomes a. Then, the next swap is between b and c. Now, what's the current state? The mapping is a → b, b → a, others → same. So in the current string, any a in the original string is now b, and any b is a. So when we swap current b and c, it's equivalent to swapping the original a and c. Because current b is original a. So after the second swap, the mapping becomes a → c (because original a was mapped to b, then in the second swap, current b (original a) is swapped with current c (original c). So now, original a would map to c. Similarly, original c maps to a. And original b maps to a, but after swapping current b (original a) and current c (original c), so after the second swap, the mappings for original a and c are swapped.

So, the key idea is that when processing a swap (x, y), we need to find in the current mapping which original characters are mapped to x and y, and then swap their mappings. So that after the swap, any occurrence of x in the current string (which is the result of the previous mappings) would be replaced with y, and vice versa.

Wait, but how to represent this. Let's think of the mapping as a list where for each character c, mapping[c] is the character that c has been transformed into after all previous swaps. Then, when a new swap (xi, yi) comes in, we need to swap the mappings of the original characters that currently map to xi and yi.

No, wait. Because xi and yi in the swap are the current characters in the string. So, for example, if after previous swaps, the original 'a' is mapped to 'b', and the original 'c' is mapped to 'd', then a swap between 'b' and 'd' would swap the current 'b's (original 'a's) and current 'd's (original 'c's). So the new mapping would be 'a' → 'd' and 'c' → 'b'.

So, each swap between x and y is equivalent to swapping the current mappings of the original characters that are mapped to x and y.

Therefore, the way to model this is to maintain a mapping from original characters to their current transformed values. Then, for each swap between x and y, we need to find all original characters whose current mapping is x or y, and swap their mappings. Wait, no. Because the current mapping is the result of previous swaps. So, in the current mapping, for each original character c, mapping[c] is the current character. So when a swap between x and y happens, in the current string, all instances of x are replaced with y and vice versa. But to model this, we need to adjust the mapping so that any original character that was mapped to x now maps to y, and any original character that was mapped to y now maps to x.

Wait, that's right. Because when you swap x and y in the current string, each x becomes y and each y becomes x. So for the mapping, any original character that was mapped to x (so that in the current string, it's x) will now be mapped to y, and vice versa.

So, for each swap (x, y), we need to go through all original characters and check if their current mapping is x or y, and swap their mappings. But that's O(26) operations per swap, which is acceptable even for m=2e5. Because 2e5 * 26 is 5.2e6 operations.

Wait, but how? Let me think again. Let's say the current mapping is stored as a list or a dictionary. For each swap (x, y), we need to find all original characters c where mapping[c] == x, and set mapping[c] = y, and vice versa for those where mapping[c] == y, set to x. But that's O(26) per swap, since there are only 26 letters. Because for each character, we can check what their current mapping is and swap x and y.

Alternatively, since each character's mapping is independent, perhaps we can model the current mapping as a permutation. For each swap (x, y), the effect is to swap the current x and y in the permutation. Wait, no. Because the permutation is the mapping from original to current. Hmm.

Wait, perhaps the correct way is to model the mapping as a list where for each character c in 'a' to 'z', mapping[c] represents what it is transformed to after all swaps. Then, when processing a swap between x and y, we can just swap the entries in the mapping for x and y. Wait, no. Because in that case, the mapping represents that, for example, when a character was x in the current string, it will be replaced by y. But that's not the case. Wait, perhaps not. Let's see.

Wait, maybe the correct approach is to track a transformation that, given the original character, tells us what it should be replaced with after all swaps. Initially, the transformation is identity: each character maps to itself. Then, when we have a swap between x and y, all future transformations will see that swap. For example, the first swap is x and y. So any original character that was mapped to x will now be mapped to y, and vice versa. So after the swap, the transformation is such that any occurrence of x in the current string (before this swap) is replaced by y, and vice versa.

But how to model that. Let's think: Each swap (x, y) is equivalent to exchanging the mappings of x and y in the transformation. Wait, perhaps the correct model is to have a list (or array) where for each character, we track what it is currently mapped to. So, for each swap (x, y), we need to swap the values of the mapping for x and y.

Wait, let's take an example. Suppose initially, mapping is identity:

mapping = {'a': 'a', 'b': 'b', ..., 'z': 'z'}

Then, a swap between 'a' and 'b' occurs. So, the new mapping would be:

mapping['a'] = 'b', mapping['b'] = 'a', others remain the same.

So, after this swap, any original 'a' is replaced with 'b', and original 'b' becomes 'a'.

Then, another swap between 'b' and 'c' is processed. So, we need to swap the current mappings of 'b' and 'c'. But the current mapping for 'b' is 'a' (since after the first swap, 'b' maps to 'a'), and 'c' maps to 'c'. So after swapping, 'b' will map to 'c', and 'c' will map to 'a'.

Wait, that's not right. Let's see: the second swap is between 'b' and 'c'. But after the first swap, original 'a' maps to 'b', original 'b' maps to 'a'. So, in the current string, any 'a's in the original string are 'b's, and 'b's are 'a's. Now, the swap is between 'b' (current 'a') and 'c' (current 'c'). So, after this swap, any occurrence of 'b' (current 'a') becomes 'c', and 'c' (current 'c') becomes 'b'.

So the mapping would need to be adjusted such that:

Original 'a' was mapped to 'b', but after the second swap, which swaps current 'b' and 'c', which are 'a' and 'c' in the original. So the new mapping for original 'a' is 'c', and for original 'c' is 'a'.

Wait, perhaps the way to model this is to maintain a reverse mapping. Or perhaps the initial approach of maintaining a forward mapping is the right way.

Alternatively, think of the transformation as a sequence of transpositions. Each swap (x, y) adds a transposition (swap) between the current x and y. So, the order of swaps is important, and each swap affects the current state.

So the idea is to track, for each original character, what it becomes after all swaps. To do this efficiently, we can model the swaps as a series of transpositions applied in reverse order. Wait, no. Because each swap is applied in the order given, so processing from first to last.

Alternatively, when processing each swap, we can track the current mapping. For example, for each character in the original string, after processing the first swap, their transformed value is known. Then, each subsequent swap modifies the mapping.

Wait, perhaps the correct approach is to have a mapping array where for each character c, map[c] is the current character it is transformed into. Then, when a swap between x and y occurs, we swap map[x] and map[y]. But wait, no. Because the swap is between the current x and y in the current transformed string. Wait, let me think again.

If the current mapping is such that original 'a' is mapped to 'b', original 'b' is mapped to 'a', and others are same. Then, the current string's 'a's are the original 'b's, and 'b's are original 'a's. Now, a swap between 'a' and 'c' occurs. This swap would swap all 'a's (original 'b's) and 'c's (original 'c's) in the current string. So after this swap, original 'b's become 'c's, original 'c's become 'a's.

So the mapping after this swap would be: 'a' → 'a' (since original 'a' was mapped to 'b', then swapped with 'c's), no, wait. Let me think in terms of the mapping.

Wait, the swap is between the current x and y. So, after the swap, any occurrence of x in the current string becomes y, and vice versa. So, the mapping for the original characters that were mapped to x or y should be swapped.

So, for example, after the current mapping, some original characters are mapped to x and some to y. The swap (x, y) will make those original characters now mapped to y and x, respectively.

So, the way to model this is: for each swap (x, y), we look into the current mapping and find all original characters that are mapped to x or y, and swap their mappings. Wait, no. Because the original characters mapped to x would now be mapped to y, and those mapped to y would be mapped to x.

Wait, perhaps the correct approach is to invert the current mapping. Let's say we have a mapping from original characters to current. Then, for the swap (x, y), we need to swap the values of x and y in the current mapping. Because in the current string, x and y are the current representations, so swapping them in the current string is equivalent to swapping their positions in the mapping. Wait, maybe not. Let's see.

Wait, perhaps the mapping should be a reverse one. Suppose we have a function f(c) that gives the current character of the original character c. So, the current string is built by applying f to each character in the original string.

Then, when we perform a swap between x and y, the effect is that all occurrences of x in the current string (which are the original characters c where f(c) == x) will be replaced by y, and vice versa. So, after the swap, for all c where f(c) was x, now f(c) becomes y. And for all c where f(c) was y, now f(c) becomes x.

So the way to handle a swap between x and y is to swap all the original characters that were mapped to x and y. But how to do that efficiently.

Ah, right! Because in this model, the swap between x and y affects all original characters whose current mapping is x or y. So for each swap (x, y), we need to iterate through all 26 letters and check if their current mapping is x or y, then swap their mappings. Wait, but that's O(26) per swap. For m=2e5, that's 5.2e6 operations, which is acceptable.

Wait, no. Let's think again. For each swap (x, y), we need to go through all possible original characters and check if their current mapping is x or y, then swap those.

Alternatively, we can maintain a reverse mapping. For each current character, track which original characters map to it. Then, when a swap between x and y occurs, the reverse mappings of x and y can be swapped. But maintaining reverse mappings would be more complicated.

Alternatively, the forward mapping can be maintained as a list where for each original character c, mapping[c] is the current character. Then, for each swap between x and y in the current string, we can find all original characters that map to x or y and swap their mappings. But that would require O(26) checks per swap, which is feasible.

Wait, but how to find which original characters are mapped to x or y. Because the forward mapping is from original to current. So for each swap between x and y, we can loop through all 26 letters and check if their current mapping is x or y, and swap those. So, for example:

For each swap (xi, yi):

- For all original characters c in 'a' to 'z':

   - if mapping[c] == xi:

       - set mapping[c] = yi

   - elif mapping[c] == yi:

       - set mapping[c] = xi

But that would take O(26) time per swap. Since there are 26 letters, this is manageable.

Yes. So the steps are:

1. Initialize the mapping as the identity: for each character c in 'a'-'z', mapping[c] = c.

2. For each swap (xi, yi) in the order they are given:

   a. For each original character c in 'a'-'z':

       i. if mapping[c] == xi:

           swap it to yi.

       ii. else if mapping[c] == yi:

           swap it to xi.

3. After processing all swaps, for each character in the original string, replace it with mapping[c].

But wait, no. Because the order of the swaps is important. Let's take the example from the second sample input:

Sample Input 2:

11 6

abacabadaba

a b

b c

a d

e g

f a

b b

Sample Output: cdcbcdcfcdc

Let's see how the mapping would be built.

Initial mapping: a→a, b→b, c→c, d→d, e→e, f→f, others same.

After first swap (a, b):

We loop through all 26 letters. For each c, if mapping[c] is a, change to b; if mapping[c] is b, change to a.

So after this swap, the mapping becomes:

a → b

b → a

others remain same.

Then, the second swap (b, c):

Again, loop through all letters. For each c in mapping:

current mappings are a→b, b→a, others same.

Now, we check if mapping[c] is b → change to c.

Check for each original character:

For original a: mapping is b. So change to c.

For original b: mapping is a. Not b or c (since swap is between b and c). So no change.

For original c: mapping is c. So change to b.

Others: no changes.

So after this swap:

a → c

b → a

c → b

others same.

Third swap (a, d):

Check all original characters. Current mapping:

a → c

b → a

c → b

d → d

others same.

So, for each original c:

if mapping[c] is a (original b's mapping is a, original a's is c, original c is b, etc.):

So:

Original a's mapping is c → not a or d. Original d's mapping is d. So swap a and d. Wait, the swap is between a and d in the current string. So the current a and d in the string are determined by the current mapping.

Wait, the swap is between xi and yi in the current string, which is the result of the mapping. So, the current xi is the value that characters are mapped to. So the swap is between the current xi and current yi.

So for the third swap, which is (a, d), we need to swap all original characters that are mapped to a or d. Because in the current string, any occurrence of a would be characters that are mapped to a, and any occurrence of d would be characters mapped to d.

So, for the third swap (a, d):

We loop through all original characters c. If mapping[c] is a, set to d. If mapping[c] is d, set to a.

But what's the current mapping before this swap? Let's see:

Original a → c

Original b → a

Original c → b

Original d → d

Others remain same.

So, in the current mappings, which original characters are mapped to a or d?

Original b is mapped to a. Original d is mapped to d. So:

For original b: mapping is a → set to d.

Original d: mapping is d → set to a.

Other characters: no change.

So after this swap, the mapping becomes:

a → c

b → d

c → b

d → a

others same.

So after this swap, the third swap (a, d) affects original b and d.

So the mapping after third swap is:

a: c

b: d

c: b

d: a

others same.

Continuing this way, but perhaps this approach is correct.

So, the algorithm is:

Initialize a list (or array) of size 26, where mapping[c] is the character that the original c is transformed to.

For each swap (x, y), loop through all 26 characters. For each c in 'a'-'z', check if mapping[c] is x. If yes, set to y. Else, if mapping[c] is y, set to x. This way, after the swap, all original characters that were mapped to x will now be mapped to y, and those mapped to y will be mapped to x. This correctly models the swap between x and y in the current string.

Yes, this approach should work. Because for each swap (x, y), we are effectively swapping all instances of x and y in the current mappings, which corresponds to swapping x and y in the current string.

Once all swaps are processed, we can apply the final mapping to each character in the original string to get the final result.

This approach is O(m * 26) time, which for m=2e5 is 5.2e6 operations, which is acceptable. And since n can be up to 2e5, building the output string is O(n), which is also acceptable.

So the plan is:

- Read the original string.

- Initialize the mapping as {c: c for c in 'a' to 'z'}.

- Process each swap (x, y) in order. For each swap, loop through all 26 characters and update the mapping as per the swap.

- Then, for each character in the original string, replace it with mapping[c].

Now, to implement this in Python:

We can represent the mapping as a list of 26 elements, where index 0 is 'a', 1 is 'b', etc. So for a character c, its index is ord(c) - ord('a').

Initially, mapping[i] = i for all i from 0 to 25.

For each swap (x, y):

   x_ord = ord(x) - ord('a')

   y_ord = ord(y) - ord('a')

   Then, loop through all 26 characters (i from 0 to 25):

       if mapping[i] == x_ord:

           mapping[i] = y_ord

       elif mapping[i] == y_ord:

           mapping[i] = x_ord

Wait, no. Because mapping[i] represents the current code (ord) of the character that original character i is mapped to. So for example, if mapping[i] is x_ord, then the original character i is now mapped to x. When we swap x and y, then original i's mapping (which was x) becomes y. Similarly for those mapped to y.

But the way to do this is to loop through all original characters (i from 0 to 25) and check if their current mapping (mapping[i]) is x_ord or y_ord. If yes, swap them.

So, for each swap (x, y), x and y are characters. So their ordinals are x_ord = ord(x) - ord('a'), y_ord = ord(y) - ord('a').

Then, for each i in 0..25:

if mapping[i] == x_ord:

   mapping[i] = y_ord

elif mapping[i] == y_ord:

   mapping[i] = x_ord

So this will swap all original characters that are currently mapped to x or y.

Yes. So, in code:

We can represent the mapping as a list of integers, where each element is the current code (0-25) of the transformed character.

Then, for each swap:

x, y = input().split()

x_ord = ord(x) - ord('a')

y_ord = ord(y) - ord('a')

for i in range(26):

   if mapping[i] == x_ord:

       mapping[i] = y_ord

   elif mapping[i] == y_ord:

       mapping[i] = x_ord

Wait, no. Because mapping[i] is the current code that the original character i is mapped to. So for example, if after processing some swaps, original character 'a' (i=0) is mapped to x_ord (say, 0 if x is 'a'), then during the swap, if x_ord is 0 and y_ord is 1, then all original characters that are mapped to 0 (x) will become 1 (y), and those mapped to 1 will become 0.

Yes, this logic is correct.

Once all swaps are processed, for each character in the original string, we take its original code, look up mapping[original_code], then convert it back to a character.

For example, original character is 'a' (code 0). If mapping[0] is 2 (c), then the transformed character is 'c'.

So, the code steps:

Read n and m.

Read the original string.

Initialize mapping as a list from 0 to 25.

Process m swaps:

   for each swap line:

       x, y = input().split()

       x_ord = ord(x) - ord('a')

       y_ord = ord(y) - ord('a')

       for i in range(26):

           if mapping[i] == x_ord:

               mapping[i] = y_ord

           elif mapping[i] == y_ord:

               mapping[i] = x_ord

Then, build the output string by converting each character in the original string:

output = []

for c in original_str:

   code = ord(c) - ord('a')

   new_code = mapping[code]

   output.append(chr(new_code + ord('a')))

Then, print(''.join(output)).

This should work.

Testing on the first sample input:

Sample Input 1:

6 1

police

p m

Original string is 'police'.

Processing swap 'p' and 'm'.

p is 'p' - ord('a') = 15. m is 12.

So x_ord = 15, y_ord = 12.

Loop through all 26 i:

For i=0 (a), mapping[i] is 0. Not 15 or 12.

For i=15 (p), original mapping is 15. So set to 12.

For i=12 (m), original mapping is 12. So set to 15.

Other characters remain same.

So, after the swap:

Original 'p' (i=15) is mapped to 12 (m), original 'm' (i=12) is mapped to 15 (p). Others are same.

So, in the original string 'p' is replaced with 'm', and 'm' would be replaced with 'p'. But in the original string, there's a 'p' (in 'police'), which becomes 'm'. The rest are unchanged. So the output is 'molice', which matches the sample.

The second sample is more complex, but following the same logic should work.

Now, for the code:

We need to read m lines of swaps. Since m can be up to 2e5, reading with input() for each line can be slow in Python. So, to read the input efficiently, we can read all input at once using sys.stdin.read().

But in the problem statement, the code must read input via input(), not sys.stdin. However, in practice, for m=2e5, using a loop with input() can be slow in Python. So, for speed, it's better to read the input using sys.stdin.

So, the code will be:

import sys

n, m = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().strip()

mapping = list(range(26))  # 0 to 25

for _ in range(m):

   x, y = sys.stdin.readline().split()

   x_ord = ord(x) - ord('a')

   y_ord = ord(y) - ord('a')

   for i in range(26):

       if mapping[i] == x_ord:

           mapping[i] = y_ord

       elif mapping[i] == y_ord:

           mapping[i] = x_ord

result = []

for c in s:

   code = ord(c) - ord('a')

   result.append(chr(mapping[code] + ord('a')))

print(''.join(result))

But what if the input lines for swaps have leading/trailing whitespaces? Probably not, as per the problem statement. Also, for each swap line, x and y are two lowercase letters, space-separated.

But in some cases, when reading via sys.stdin, after reading the first two lines, the remaining lines may include lines with empty strings if the input is not properly formatted. However, the problem says that there are exactly m lines.

But using sys.stdin.readline() in a loop for m swaps can be slow. Because for m=2e5, each readline() is O(1) but in practice, it's better to read all the lines at once.

Alternatively, read the entire input first.

But in Python, the code above should be acceptable. Because even for 2e5 swaps, each loop is O(26) per swap. 2e5 * 26 is 5.2e6 operations, which is manageable.

But in practice, for Python, even 1e8 operations can be slow, but 5e6 is okay.

Now, let's test the code against the sample inputs.

Sample 1:

Input:

6 1

police

p m

Processing:

mapping starts as [0..25].

Swap p (15) and m (12):

Loop i from 0 to 25:

At i=15 (p), mapping[15] was 15 → becomes 12.

At i=12 (m), mapping[12] was 12 → becomes 15.

Other i's are unchanged.

So after swap, mapping[15] is 12 (m), mapping[12] is 15 (p).

So for the original 'p' (code 15), mapped to 12 → 'm'.

Other letters are unchanged.

So the output is 'molice', which is correct.

Sample 2:

After processing all swaps, the output is 'cdcbcdcfcdc'.

But verifying that would take time, but the code should handle that.

Now, about the code's efficiency. For m=2e5, each loop of 26 steps is acceptable. But in Python, even 5e6 steps is manageable.

Regarding memory: The mapping list is 26 integers. The result list is built by processing each character of the original string (n=2e5). So the code uses O(n) space for the result, which is acceptable.

So the code should be correct and efficient.
</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    mapping = list(range(26))
    for _ in range(m):
        x, y = sys.stdin.readline().split()
        x_ord = ord(x) - ord('a')
        y_ord = ord(y) - ord('a')
        for i in range(26):
            if mapping[i] == x_ord:
                mapping[i] = y_ord
            elif mapping[i] == y_ord:
                mapping[i] = x_ord
    result = []
    for c in s:
        code = ord(c) - ord('a')
        result.append(chr(mapping[code] + ord('a')))
    print(''.join(result))

if __name__ == "__main__":
    main()
```