<think>
Okay, so I need to solve this problem where I have to find the number of distinct Aramic objects in a list of words. Let's think about what defines an object here. The root is the key here. Each word's root is the set of unique characters in it, sorted in some order? Wait, no. Wait, the root is the word that contains all the letters that appear in the original word, each once. But permutations of the root are considered the same object. So for example, "ab" and "ba" would have the same root, which is either "ab" or "ba", but since the root is considered the same regardless of permutation, the actual root can be represented in a way that uniquely identifies the set of characters.

So the root is the set of unique characters in the word. Because, for example, "aabb" and "ab" both have the same set of characters {'a','b'}, so their roots are the same. But permutations of the root's characters are considered the same, so the actual order doesn't matter. Therefore, the way to represent the root uniquely is by the sorted string of its characters. Or maybe just the set of characters, but since sets are not hashable in Python, we can represent the root as a sorted string of the unique characters.

So for each word, I need to:

1. Find all the unique characters in it.
2. Sort those characters to form a string. For example, the word "bab" becomes {'a','b'}, sorted as "ab".
3. Then, the number of distinct objects is the number of distinct sorted unique character strings.

Yes. Because two words will be in the same object category if their sorted unique character strings are the same. For instance, in the second example, all three words "amer", "arem", "mrea" have the same set of unique characters (a, m, e, r), sorted as "aemr" (assuming the order is alphabetical). Wait, but the order of letters when sorted is alphabetical. So regardless of the permutation, the sorted string will be the same. So that's how we can represent the root uniquely.

So the plan is:

- For each word in the input, process it to get its unique characters, sort them, and then add to a set.
- The size of the set is the answer.

Yes. That makes sense.

Now, let's think about the steps in code.

First, read n. Then read the next line of n words.

For each word, process it as follows:

- Take the set of characters in the word. This gives all unique characters.
- Sort the characters. Since sets are unordered, when we sort, the order will be based on the character values (like alphabetical order).
- Convert the sorted list of characters into a string. For example, the set {'b','a'} becomes ['a','b'], then "ab".

Then, collect all these strings into a set, and the answer is the length of that set.

So the code steps:

Read n.

Read the next line as a list of words.

Initialize a set.

For each word in the list:

   unique_chars = sorted(list(set(word)))

   unique_str = ''.join(unique_chars)

   add unique_str to the set.

The answer is the size of the set.

Wait, but wait. Wait, the word "aab" has characters a and b. So the unique_chars is {'a','b'}, sorted as 'ab'. So the unique_str is "ab".

For the word "ab", sorted(set(word)) would be ['a','b'], same as before.

So yes, this correctly captures the root.

But wait, the set is of the characters in the word. So for any word, the root is the sorted string of its unique characters.

Yes.

So the code can be written as:

n = int(input())
words = input().split()

roots = set()

for word in words:
    unique_chars = sorted(list(set(word)))
    root = ''.join(unique_chars)
    roots.add(root)

print(len(roots))

Wait, but wait, let's test this against the examples.

First example input:

5
a aa aaa ab abb

Processing each word:

"a": unique is {'a'}, sorted is ['a'], joined as "a".

"aa": same as above.

"aaa": same.

"ab": unique {'a','b'}, sorted as "ab".

"abb": same as "ab".

So the roots are "a" and "ab", so the answer is 2. Correct.

Second example:

3
amer arem mrea

Each word:

"amer": unique chars are a, m, e, r. Sorted as a, e, m, r. So "aemr".

"arem": same set, sorted to "aemr".

"mrea": same set. So all three roots are the same. So the set has size 1. Correct.

So the code works for the examples.

Now, what about the constraints?

n can be up to 1e3, and each word can be up to 1e3 characters. So total processing is 1e6 characters, which is manageable.

For each word, we process O(k) where k is the length of the word, but since we have to create a set of the characters, which takes O(k) time. Then sorting the characters, which is O(m log m), where m is the number of unique characters in the word (m can be up to 26, since it's lowercase letters). So for each word, the time is O(k + m log m), but since m is at most 26, the sorting is negligible. So overall time is acceptable.

So the code should work within the time constraints.

In Python, creating a set from the characters is O(k) time, but in Python, the set is created by iterating through each character and adding to the set. So for each word, the code is efficient.

So the code as written should be correct and efficient.

Now, testing for edge cases. For example:

Input with all words having same unique characters but different permutations.

But in the code, the sorted unique characters will be same, so they are considered same.

Another edge case: all words are empty. But according to the problem statement, each word is part of the input. But the problem says, "the length of each string does not exceed 1e3". So possible for a word to be empty? Wait, the problem says "words" in the input. Are the words allowed to be empty?

Looking at the problem statement's input constraints:

The second line contains n words s_1 ... s_n. The length of each string does not exceed 1e3. So a word can be empty? But according to the problem's description, words in Aramic are root if they have no duplicates. But an empty word's root is an empty string. So if two empty words are present, they contribute to the same root.

But according to the problem's sample inputs, there are no empty words. However, according to the code, if the input has empty strings, then their root is an empty string, which would be considered as a distinct object.

But the problem's note says that the root is the word that contains all letters in y once. So if the word is empty, then the root is empty.

So the code handles that correctly.

Another test case: n=0? But according to the input constraints, n is 1<=n<=1e3. So no, n is at least 1.

So the code should be correct.
</think>

```python
n = int(input())
words = input().split()
roots = set()
for word in words:
    unique = ''.join(sorted(set(word)))
    roots.add(unique)
print(len(roots))
```