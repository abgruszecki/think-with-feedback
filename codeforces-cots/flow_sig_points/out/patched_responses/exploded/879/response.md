<think>
Okay, let's tackle this problem. So the task is to process a string by repeatedly removing vowels that are preceded by another vowel. The process continues until there are no two consecutive vowels left. Hmm, wait, but how exactly does the removal work? Let me re-read the problem statement.

The rule says: as long as there are two consecutive vowels, delete the first vowel in the word such that there's another vowel right before it. Oh right, so whenever there's a pair of consecutive vowels, you look for the first occurrence where a vowel is preceded by another, and remove that first vowel. Then repeat this process until no consecutive vowels are left.

Wait, but the order of removal matters here. For example, in the third test case, the input is 'aaeaa', which becomes 'aeaa' after deleting the first 'a' (the second character) because 'a' is preceded by 'a'. Then again, check for consecutive vowels. Now 'aeaa' has 'aa' at positions 3 and 4. So the first occurrence is the 'e' preceded by 'a'? Wait, no. Wait, in 'aeaa', the first pair of consecutive vowels is 'a' followed by 'e'? Or wait, vowels are a, e, i, o, u, y. So 'ae' are two consecutive vowels. So the first occurrence is the 'a' followed by 'e'? So the first vowel (the 'a') that is preceded by a vowel? Wait, no. Wait, the problem says: delete the first vowel in the word such that there is another vowel right before it. So for each step, we scan the word from left to right, find the first vowel that has a vowel immediately before it. Then delete that vowel. Then repeat until no such vowels exist.

So for example, in the third test case:

Original: a a e a a → 'aaeaa'

First step: look for the first vowel that has a vowel before it. The first two letters are 'a' followed by 'a'. The second 'a' is the first vowel that has a vowel before it. So delete that second 'a' (the one at index 1). The string becomes 'a e a a' → 'aeaa'.

Now, check again. The string is 'aeaa'. Now, scan from left to right. The first occurrence is 'a' followed by 'e' (both vowels). The 'e' is preceded by 'a', so the 'e' is the vowel that has a vowel before it? Wait no. Wait, the problem says "delete the first vowel in a word such that there is another vowel right before it". So the vowel to delete is the one that comes after another. So for the pair 'ae', the first vowel that is preceded by a vowel is the 'e' (since the first character is 'a', which has no preceding character). Wait, the first occurrence in the word where a vowel is immediately after another is the first two characters. Wait, perhaps I need to find the first occurrence of two consecutive vowels. Then, in that pair, delete the first vowel. Or wait, wait the problem statement says:

"delete the first vowel in a word such that there is another vowel right before it."

Ah, so the first vowel (in the entire word) that is preceded by a vowel. So, the index i where s[i] is a vowel, and s[i-1] is a vowel, and i is the smallest such index. Then, we remove s[i], and repeat the process.

Wait, no. Because when you delete s[i], the next step would have to check again the entire string for any pair. Let me think with the third example.

Original input is 'aaeaa' (indices 0 to 4). Let's list the steps:

Initial string: a a e a a → indexes 0,1,2,3,4.

Check for any vowel followed by another. The first pair is 0 and 1. So the vowel at index 1 (the second 'a') is preceded by a vowel. So delete index 1. Now the string is a, e, a, a → indexes 0,1,2,3 (length 4). Now the string is 'aeaa'.

Now check again. The first pair where s[i] is a vowel and s[i-1] is a vowel. Let's look through each position:

At index 1: s[0] is 'a', s[1] is 'e' → both vowels. So the first occurrence is i=1. So we delete index 1. Now the string becomes 'aaa' (indexes 0,2,3 from original after the first deletion: wait, after the first deletion, the string was 'a e a a' → after deleting index 1, the string is 'a e a a'? Wait, no. Wait, when you delete index 1 in the original string 'a a e a a', the string becomes 'a e a a' (since indices 0,2,3,4 are kept). Then, in the next step, the string is 'aeaa', and looking for vowels preceded by vowels.

In 'aeaa', the first occurrence is index 1 (e) preceded by a. So the vowel at index 1 (e) is the first vowel that has a vowel before it. So we delete index 1. The string becomes 'aaa' → 'aaa' (indices 0, 2, 3,4 → after deleting index 1, then the string is 'a' followed by 'e' and then 'a a', then deleting the 'e' gives 'a a a').

Now the string is 'aaa'. Check again. The first occurrence is index 0 and 1 (a and a). The vowel at index 1 is preceded by a vowel. So delete index 1. The string becomes 'aa'. Now check again: the two a's. Delete index 1 again. Now the string is 'a'.

So the output is 'a'.

So the process is, in each step, find the first occurrence of a vowel that is preceded by another vowel, delete that vowel, and repeat until no such occurrences.

So how to model this efficiently?

The naive approach would be to simulate each deletion step. But for large n (like 1e5), this could be O(n^2), which is too slow. But according to the problem constraints, n is up to 100. So even O(n^2) would be acceptable. But let's see the constraints again. Oh, the input n is up to 100, so for n=100, even O(n^2) is manageable. So perhaps a straightforward simulation is possible.

But let's think about the steps. For each step, we need to scan the string to find the first occurrence of two consecutive vowels. Then delete the second vowel (because the problem says to delete the first vowel that has a vowel before it. Wait, wait: if two vowels are consecutive, like at positions i-1 and i, then the vowel at i is the one that has a vowel before it. So we need to delete the i-th character. For example, in the first step of the third example, the two a's are at 0 and 1. So the first occurrence is at i=1. Delete that. So in each step, when you find two consecutive vowels, you delete the second one (the one that is preceded by a vowel). Wait, wait: the problem says to delete the first vowel in the word that has a vowel before it. So the first occurrence where a vowel is preceded by another is the one we delete.

So for example, the string is 'aei', which has a at 0, e at 1, i at 2. The first occurrence is e (position 1) preceded by a. So delete e. Then the string becomes 'ai', which has a followed by i. Delete i. Then the string is 'a', which is correct.

But how to model this in code.

One approach is to iterate through the string, checking each character (starting from index 1) to see if it's a vowel and the previous character is a vowel. Once we find the first such occurrence, we remove that character, and then restart the process.

So for example, the steps would be:

current_string = s

loop:

   for i in 1 to len(current_string)-1:

       if current_string[i] is a vowel and current_string[i-1] is a vowel:

           current_string = current_string[:i] + current_string[i+1:]

           break

   else:

       break

So this is O(n^2) in the worst case. But since n is up to 100, even in the worst case (like all vowels), each step deletes one character, requiring up to 100 steps, each with O(n) time. So 100 * 100 = 10,000 operations. Which is acceptable.

So this approach should be feasible.

But how to implement this in Python efficiently.

Let's think about how to code this.

First, we need a helper function to check if a character is a vowel. The vowels are a, e, i, o, u, y.

We can create a set vowels = {'a', 'e', 'i', 'o', 'u', 'y'}.

Then, for the current string, we iterate through each index from 1 to len(current_string)-1, and check if current_char is in vowels and previous_char is in vowels. Once found, we remove the current_char (i-th index) and restart the loop.

But in Python, strings are immutable, so each time we create a new string. But for n=100, even with multiple steps, it's manageable.

Let's test this approach with the third example.

Original string: 'aaeaa'

Step 1: check indices 1, 2, 3, 4.

At index 1: previous is 'a', current is 'a' → both vowels. So remove index 1. New string is 'aeaa'.

Step 2: check indices 1 (since the string is now 'aeaa' → length 4. Check indices 1, 2, 3.

At index 1: previous is 'a', current is 'e' → vowels. So remove index 1. New string is 'aaa'.

Step 3: check indices 1,2 (string is 'aaa').

At index 1: previous 'a', current 'a' → remove index 1 → 'aa'.

Step 4: check index 1 → 'a' and 'a' → remove index 1 → 'a'.

Now no more consecutive vowels.

So the code would process this correctly.

Another example: 'weird' → 'w e i r d'.

Wait, the input is 'weird' which is w e i r d. Let's see:

Check for consecutive vowels. The e is at index 1, then i at index 2. So e and i are consecutive vowels. So the code would find index 2 (i) as the first occurrence. Then delete it. So the string becomes 'werd', which has no consecutive vowels. So output is 'werd'.

Wait, but according to the first example's note, the correct output is 'werd', which is achieved by deleting the 'i' here. So the code's approach is correct.

So the algorithm is correct.

Now, how to implement this.

In Python:

Read n, then s. Then process s as per the algorithm.

So the code would look like this:

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

s = input().strip()

current = list(s)  # convert to list for easier manipulation?

Wait, but for strings, slicing would create new strings each time. But for small n, it's manageable.

Alternatively, use a list for easier deletions. Because for each step, when we find the index to delete, we can just remove that element from the list.

Wait, but building the list once and modifying it in place would be more efficient.

So let's try using a list.

But for each step, we need to check for the first occurrence of consecutive vowels.

Wait, here's the code:

current = list(s)

modified = True

while modified:

    modified = False

    for i in range(1, len(current)):

        if current[i] in vowels and current[i-1] in vowels:

            del current[i]

            modified = True

            break

    # if not modified, break

So the loop continues as long as deletions happen.

In each iteration, we scan from i=1 to len(current)-1. For each i, check if current[i] and current[i-1] are vowels. If found, delete current[i], set modified to True, break the loop and restart the scan.

This approach works because once a deletion happens, the next scan starts from the beginning again.

Let's test with the third example:

Original current is ['a', 'a', 'e', 'a', 'a']

First iteration:

i=1: current[0] is 'a', current[1] is 'a' → both vowels. Delete current[1]. current becomes ['a', 'e', 'a', 'a']. modified is True. break.

Next loop: check len(current) is 4.

i ranges from 1 to 3.

i=1: current[0] is 'a', current[1] is 'e' → both vowels. Delete current[1]. current becomes ['a', 'a', 'a']. modified is True.

Next loop: len is 3.

i=1: current[0] is 'a', current[1] is 'a' → delete current[1]. current is ['a', 'a'].

Next loop: i=1. current[0] and current[1] are vowels. Delete current[1]. current is ['a'].

No more steps. Output 'a'.

Which is correct.

Another example: 'weird' → ['w','e','i','r','d'].

First iteration: check i=1 (e), i=2 (i). At i=1: previous is 'w' (not vowel). At i=2: previous is 'e' (vowel). So current[i] is 'i' (vowel). So delete i=2. List becomes ['w','e','r','d']. Then modified is True. Next loop: check len 4. i ranges 1-3. Check each i:

i=1: 'e' and 'r' → no.

i=2: 'r' and 'd' → no. So modified remains False. Exit loop. The result is 'werd'.

Which is correct.

Another example: 'aaeaa' processed as earlier.

So the code works.

But using a list and deleting elements is O(n) per deletion, but since each step deletes one character, and there are O(n) steps, it's O(n^2) time, which is acceptable for n=100.

So the code should be efficient enough.

Now, the code in Python:

Read n, then s. But in the problem statement, the input is:

First line is n (1<=n<=100).

Second line is the string s, exactly n letters.

So the code would read:

n = int(input())
s = input().strip()

But the code can ignore n, as len(s) would be n. But according to the problem statement, the input is guaranteed to have a string of length n.

Then process the string as per the algorithm.

So here's the code:

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

current = list(s)
modified = True

while modified:
    modified = False
    for i in range(1, len(current)):
        if current[i] in vowels and current[i-1] in vowels:
            del current[i]
            modified = True
            break

print(''.join(current))

Wait, but in the first step, after deleting the element at i, the list becomes shorter. So the next iteration of the loop will start from the beginning again.

Yes. For example, after deleting i=1, the next scan starts from i=1 again (since the list is now shorter).

So this code correctly finds the first occurrence each time.

Testing the code with the examples.

First example:

Input:

5

weird

After processing, the code deletes the 'i' (index 2 in the original list). So output 'werd'.

Second example:

4

word → no consecutive vowels. The code doesn't modify anything. Output is 'word'.

Third example: 'aaeaa' → output is 'a'.

All correct.

So this should be the correct solution.
</think>

```python
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
s = input().strip()
current = list(s)
modified = True
while modified:
    modified = False
    for i in range(1, len(current)):
        if current[i] in vowels and current[i-1] in vowels:
            del current[i]
            modified = True
            break
print(''.join(current))
```