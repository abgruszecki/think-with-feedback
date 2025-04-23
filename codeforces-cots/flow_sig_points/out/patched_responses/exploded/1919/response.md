<think>
Okay, let's see. The problem is to find out how many distinct photobooks can be made by inserting exactly one additional photo into the existing string. Each photobook is a string that's formed by inserting one character (from a to z) at any position in the original string, including the beginning and end. We need to count all unique possibilities.

Hmm. So the main thing here is to avoid counting duplicates. For example, if the original string has duplicate characters, inserting the same character in different positions might not always create a new unique string. Wait, no. Wait, even if the original string has duplicates, inserting a character in different positions could create new unique strings. Like, for example, the original is 'aa'. Inserting an 'a' at the beginning gives 'aaa', inserting it between the two a's gives 'a' 'a' 'a', same as inserting after the second. So in that case, inserting an 'a' in any position would result in the same string. So the key is to count all possible insertions, but subtract duplicates.

So the approach would be to generate all possible insertions and count the distinct ones. But since the original string can be up to 20 characters long, inserting a character in 21 possible positions (for each of the 26 letters) would result in 21*26 possibilities. But some of these might be the same. So the problem is to compute how many unique strings there are among all these possibilities.

Wait, but for small original strings, like length 1 (as in the first example), inserting a character gives a string of length 2. The total possible is 26*2 (positions), but some may be duplicates. But in the first example, the original is 'a'. So inserting any character at position 0 or 1. For example, inserting 'a' gives 'aa' in two ways (position 0 or 1). So the duplicates here would be when inserting the same character in adjacent positions. Wait, but when you insert 'a' before the original 'a' or after, the result is the same. So inserting 'a' into 'a' gives two possibilities (positions 0 and 1), but they result in the same string. So for each possible insertion of a character, we need to see how many unique strings are generated.

So the problem reduces to: for each possible insertion (character + position), how many unique strings are there.

The straightforward way would be to generate all possible insertions, add them to a set, and then return the size of the set. But for the maximum input size, the original string is 20 characters. So inserting each of 26 letters into 21 positions (positions 0 to 20 inclusive) gives 26*21 = 546 possibilities. For each of these 546 possibilities, we need to generate the string and track uniqueness.

But 546 is a very small number. So even generating all possibilities and putting them into a set would be feasible. Even for the largest possible input, 21*26=546 operations, each of which is creating a string of length up to 21 (original is 20, plus 1). So this is manageable within Python's time and memory constraints.

So the optimal approach here is to generate all possible insertions, add them to a set, and then output the size of the set. Since even for the maximum input, it's 546 elements, which is negligible.

Wait, but the original problem's constraints say the input can be up to length 20. So for each insertion, creating a new string would take O(n) time, but 546 * 21 is about 11k operations. That's nothing. So the set approach is perfectly acceptable.

Let's test this logic against the examples.

First example input is 'a'. The possible insertions are inserting any of 26 letters in position 0 or 1. So total 26*2 = 52 possibilities. But inserting 'a' in position 0 gives 'aa', inserting 'a' in position 1 also gives 'aa'. So how many unique strings? The correct answer is 51, which is 52 (total) minus 1 duplicate (the two 'aa's). So the set approach would correctly count this.

Similarly, the second example is 'hi'. The original length is 2, so inserting a character in 3 positions. 3*26=78 possible insertions. But some may be duplicates. The output is 76, so two duplicates. For example, inserting 'h' at position 0 gives 'hhi', inserting 'h' at position 1 gives 'hhi' as well? Or maybe inserting 'i' at position 2 or 1. Let's see:

Original 'hi'. Inserting 'h' at position 0: 'hhi'. Inserting 'h' at position 1: 'hhi' again. So those two insertions would result in the same string. Similarly for inserting 'i' at position 2, which would be 'hii', and inserting 'i' at position 1 gives 'hii' as well. So there are two duplicates here. So the set approach would capture that.

So the approach is correct.

So the plan is:

1. Read the input string s.

2. For each position i in 0 to len(s) inclusive (since you can insert before the first character, between characters, or after last).

3. For each character c in 'a' to 'z'.

4. Generate the new string by inserting c at position i.

5. Add all these generated strings to a set.

6. The answer is the size of the set.

Yes, this will work.

So in Python code:

Read s.

Initialize a set.

For i in range(len(s)+1):

   for each c in 'abcdefghijklmnopqrstuvwxyz':

       new_str = s[:i] + c + s[i:]

       add new_str to the set.

The size of the set is the answer.

Yes. Let's code that.

But how to loop through all lowercase letters? We can use a loop from 'a' to 'z', or generate all 26 letters. For Python, the easiest way is to import string and use string.ascii_lowercase, but since the code must not have any imports (assuming that the code can use the default available modules, but the problem says nothing about that), but since 'a' to 'z' can be generated by using a loop with chr(ord('a') + i) for i in 0 to 25.

Alternatively, just iterate through each character in 'abcdefghijklmnopqrstuvwxyz'.

But in code, writing the entire string is acceptable.

So code:

s = input().strip()

unique = set()

n = len(s)

for i in range(n + 1):

    for c in 'abcdefghijklmnopqrstuvwxyz':

        new_s = s[:i] + c + s[i:]

        unique.add(new_s)

print(len(unique))

Yes. This code will handle all cases correctly.

Let's test the first example:

Input is 'a'. For i in 0 and 1:

When i=0:

new_s is '' + c + 'a' → c + 'a'

For c from a to z. So all possible two-letter strings starting with the character c, followed by 'a'. Wait, no: when inserting at position 0, the original string is 'a', so inserting c at 0 gives c followed by a. So for example, c is 'a' → 'aa'.

When i=1, inserting at the end: 'a' + c. So inserting 'a' here gives 'aa' again.

So for all c, inserting at i=0 and i=1 gives c followed by 'a' and 'a' followed by c. So for c != 'a', these are different. But for c='a', both insertions result in 'aa'. So in the set, there's only one 'aa'.

So the total is 26 letters for each insertion position, but duplicates when c is inserted in multiple positions and creates the same string.

In the first example, inserting 'a' in positions 0 and 1 gives same string. So for 'a', the two possibilities are duplicates. All other letters have insertions in two positions that create different strings. For example, inserting 'b' at 0 gives 'ba', inserting at 1 gives 'ab' → two distinct strings.

So the total is (25 letters * 2 insertions) + 1 (for 'a' inserted once in the set). 25*2=50, plus 1 → 51. Which matches the example.

So the code works.

Another example: 'hi' → output 76. Let's see.

Original string is 'h' 'i'. Possible insertions at positions 0,1,2.

For each position and each character:

For example, inserting 'h' at position 0: 'hhi' → inserting at 0. Inserting 'h' at position 1: 'hhi' again. So these two insertions (c='h', positions 0 and 1) result in same string. So adding 'h' in these two positions gives one entry in the set.

Similarly, inserting 'i' at position 1: 'hii' (inserting between h and i), and inserting 'i' at position 2 (after i) → 'hii' again. So two insertions for 'i' in positions 1 and 2 give same string. So those two contribute one entry.

So total possible insertions: 3 positions * 26 letters = 78. But two duplicates (each from 'h' and 'i'), so 78 - 2 =76. Which matches the example.

So the code works.

Thus, the approach is correct. The code is straightforward and efficient enough for the problem's constraints. Even for the maximum input (s of length 20), the code generates 21 * 26 = 546 strings, each of length 21, and stores them in a set. The time is O(21*26 * 21) → 21*26 is 546, multiplied by 21 (for each string concatenation, which in Python is O(n) time). So 546 *21 = 11,466 operations, which is very manageable. The set insertion and lookups are O(1) on average. So even with the worst case, this is well within the time limit of 2 seconds.

Memory-wise, the set stores 546 strings of length up to 21. Each character is one byte, so each string is 21 bytes. So 546 * 21 is around 11,466 bytes, which is negligible compared to the memory limit (256MB).

Thus, this approach is optimal and correct.
</think>

```python
s = input().strip()
unique = set()
n = len(s)
for i in range(n + 1):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        new_s = s[:i] + c + s[i:]
        unique.add(new_s)
print(len(unique))
```