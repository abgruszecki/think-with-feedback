<think>
Okay, I need to solve this problem where I have to determine if two genomes can be made equal by swapping exactly two characters. Let's think through the problem.

First, the problem statement says that two dwarves are of the same race if swapping two characters in the first genome results in the second. So the first thing that comes to mind is that the two genomes must be permutations of each other. But wait, not exactly. Because swapping two characters can only change two positions. So the actual condition is that the two strings are exactly the same except for two positions where the characters are swapped. Wait, no. Because the problem says that you can swap two characters in the first genome to get the second. So the correct condition is:

The two strings must be of the same length. Otherwise, it's impossible. So the first check is to see if the lengths are equal. If not, immediately output NO.

Then, check if the two strings are already permutations of each other. But wait, no. Wait, for example, if the two strings are permutations but differ in more than two positions, then swapping two characters won't make them equal. Wait, no. Because the problem allows swapping any two characters (not necessarily adjacent), but the result after swapping must be exactly the second string. So the correct approach is:

The two strings must be the same length. Then, the number of positions where they differ must be exactly two. Moreover, the two differing characters must be each other's counterparts. For example, in the first example, the first string is 'ab', the second is 'ba'. The differing positions are 0 and 1. So the characters are 'a' and 'b' in the first, and 'b' and 'a' in the second. So swapping these two would make them equal.

Additionally, the two strings must have the same frequency of each character. Because if one has a character that the other doesn't, then even if the differing positions are two, they can't be swapped. Wait, but if the lengths are the same but the character counts are different, then even after swapping two, they can't be equal. So the first check is:

Check if the two strings are of the same length. If not, output NO.

Then, check if the two strings have the same multiset of characters. For example, if one has two 'a's and another has one 'a' and one 'b', then even if they differ in two positions, swapping two characters in the first won't make the second.

So the steps I need to do are:

1. Check if the two strings have the same length. If not, output NO.
2. Check if the two strings have the same character counts (i.e., are anagrams). If not, output NO.
3. Now, check how many positions are different between the two strings. If the count is exactly two, then output YES. Otherwise, output NO.

Wait, but what if the count is exactly two but the characters in those positions are not the same when swapped? For example, first string is 'ab', second is 'cd'. Then, the count is two, but swapping the two in the first would result in 'ba', which is not equal to 'cd'. So the third check is not sufficient. Oh right! Because even if there are exactly two differing positions, the characters in those positions must be each other's counterpart. So for those two differing positions i and j, the first string's i-th character must equal the second's j-th character, and the first's j-th must equal the second's i-th. Otherwise, even after swapping, they won't match.

So the steps should be:

1. Check lengths. If different, output NO.
2. Check if they are already equal (but the problem states that the input strings are different, so this case is excluded. But according to the problem statement, the input genomes are different. So we don't need to handle that case. Wait, the problem says "it is guaranteed that the strings are different". So the output can't be YES if the two are same (since the problem says that the input is different), but in our code, if the two are same, but according to the problem, that input is not possible. So we can ignore that case.

Wait, but the input could have the same string? No, the problem says that the two genomes are different. So in our code, the input will have two different strings. So we don't have to handle the case where they are the same.

So back to the steps:

After steps 1 and 2 (same length and same character counts), we need to check two things:

a. The number of differing positions is exactly two.

b. The two differing positions i and j must satisfy s1[i] = s2[j] and s1[j] = s2[i].

But how do we check this efficiently?

Alternatively, after step 2 (same character counts), the condition for being possible is that there are exactly two differing positions, and those two are a swap. So for example, the two differing positions must have characters that are swapped between the two strings.

So let's think: for all pairs of differing positions, check if the two in the first string are a and b, and the corresponding positions in the second are b and a.

So how to proceed:

First, check if the two strings are same length. If not, return NO.

Then, check if the character counts are the same. If not, return NO.

Then, collect all the indices where the two strings differ.

If the number of differing indices is exactly 2, then check if s1[i] == s2[j] and s1[j] == s2[i], where i and j are the two differing indices.

If that's the case, return YES. Else, NO.

But even if the number of differing indices is two, but the characters are not swapped, then it's impossible.

So, the steps are:

Check length.

Check character counts.

If any of those are false, return NO.

Else, collect the list of differing indices.

If the length of this list is not exactly 2, return NO.

Else, check if the two positions have swapped characters.

If yes, return YES, else NO.

Another scenario: what if the two strings have exactly two differing positions, but their characters are the same. For example, s1 is 'aab', s2 is 'aba'. Then, the differing positions are 1 and 2. s1 has 'a' and 'b' there, s2 has 'b' and 'a'. So swapping them would work. But wait, in this example, the two strings are 'aab' and 'aba'. The differing positions are index 1 and 2. So s1[1] is 'a', s2[1] is 'b'; s1[2] is 'b', s2[2] is 'a'. So after swapping 1 and 2 in s1, you get 'aba', which matches s2. So this would be a YES.

Another example: s1 is 'abc', s2 is 'abd'. The differing positions are index 2. So count is 1, so output is NO.

Another case: s1 is 'ab', s2 is 'ab'. But according to problem, input will have different strings, so this case is not possible.

So the algorithm is:

- Check if the two strings have the same length. If not, output NO.

- Check if the character counts are the same. If not, output NO.

- Collect all positions where the characters differ.

- If the count is not exactly 2, output NO.

- Else, check if the two differing characters are each other's swap. That is, s1[i] == s2[j] and s1[j] == s2[i]. If yes, output YES, else NO.

Now, how to implement this efficiently.

First, the character counts can be checked by using a frequency dictionary. For Python, we can use collections.Counter for both strings. But since the strings can be up to 1e5 characters, we need an efficient way. Counter is O(n), which is acceptable.

Then, for the differing positions: we can iterate through each character in the two strings, collect the indices where they differ. If during this iteration, the count exceeds 2, we can break early.

So, for example, as we iterate through each index, compare s1[i] and s2[i]. If they differ, add to a list. If the list's length exceeds 2, we can break and return NO.

This would be O(n) time, which is acceptable for n up to 1e5.

So the steps in code:

Read s1 and s2.

if len(s1) != len(s2):

    print("NO")

else:

    if Counter(s1) != Counter(s2):

        print("NO")

    else:

        diff = []

        for i in range(len(s1)):

            if s1[i] != s2[i]:

                diff.append(i)

                if len(diff) > 2:

                    break

        if len(diff) != 2:

            print("NO")

        else:

            i, j = diff

            if s1[i] == s2[j] and s1[j] == s2[i]:

                print("YES")

            else:

                print("NO")

Wait, but what about the case where the number of differing positions is 2, but the two characters are not a swap? For example, s1 is 'abc', s2 is 'axc'. Then, differing positions are index 1. So that's only one, so code would correctly return NO.

Wait, in code, after checking that the count is 2, then check if the two positions can be swapped.

Yes.

But what if the two differing positions are same in their respective strings? Like, s1 is 'aab', s2 is 'abb'. Then, the differing positions are index 1 and 2. s1[1] is 'a', s2[1] is 'b'; s1[2] is 'b', s2[2] is 'b'. So, wait, no, that's not. Wait, in that example, s1 is 'aab', s2 is 'abb'. Comparing each position:

index 0: 'a' vs 'a' → same.

index 1: 'a' vs 'b' → different.

index 2: 'b' vs 'b' → same.

So the differing indices are only index 1. So count is 1. So code would output NO.

Another example: s1 = 'abcd', s2 = 'abdc'. Then, the differing positions are 2 and 3. s1[2] = 'c', s2[2] = 'd'; s1[3] = 'd', s2[3] = 'c'. So swapping 2 and 3 in s1 gives 'abdc', which matches s2. So code would check if s1[2] == s2[3] (c == c → yes) and s1[3] == s2[2] (d == d → yes). So code outputs YES.

Yes.

Now, the code's steps:

Check same length.

Check same character counts. If not, output NO.

If they are same, check the differing indices.

If there are exactly two differing indices, and the characters at those positions are swapped in the two strings, output YES. Else, NO.

So this code should handle all cases.

Now, considering the constraints. The maximum input is 1e5 per string. So using Counter is O(n) time and O(26) space (since there are 26 letters). But comparing two Counters might be O(26) operations (if the code is optimized). Or maybe in Python, comparing Counter objects is O(n) time. Wait, no. The Counter is a dictionary. Comparing two dictionaries in Python checks if all key-value pairs are equal. So if the two Counters have the same keys and the same counts for each key, then they are equal. So comparing two Counters would take O(k) time, where k is the number of unique keys. But since the keys are lowercase letters, k is at most 26. So this check is O(26) time.

So for large n, this is acceptable.

Alternatively, we can check the frequency counts manually. For example, for each of the 26 letters, count how many times they appear in both strings, and compare. That would be O(n) for counting, but perhaps more efficient than creating two Counter objects. But in Python, for code brevity, using Counter is easier.

But considering that for n up to 1e5, creating two Counter objects is manageable.

But perhaps using a list of counts is more efficient.

Alternatively, create a frequency array for each string.

So for s1 and s2:

count1 = [0] * 26

count2 = [0] * 26

for c in s1:

    count1[ord(c) - ord('a')] +=1

for c in s2:

    count2[ord(c) - ord('a')] +=1

if count1 != count2:

    print("NO")

This is O(n) time and O(1) space (26 elements per count array). So for very large n, this is better.

So perhaps using this approach is better for time and space.

But for code brevity, using Counter is easier. But given the problem's constraints, both approaches are acceptable.

So in code:

In the case where len(s1) != len(s2), output NO.

Else, proceed to check the frequency counts.

Then, collect the differing positions.

Now, let's test the sample input.

Sample 1:

Input:

ab

ba

len is same (2). Counter of s1 is {'a':1, 'b':1}, same for s2. Then, differing positions are 0 and 1. So i=0, j=1. Check s1[0] is 'a', s2[1] is 'a'? s2 is 'ba', so s2[1] is 'a'. Wait no: s2 is 'ba'. So s2[0] is 'b', s2[1] is 'a'. So in the code:

s1[i] = s1[0] → 'a', s2[j] is s2[1] → 'a'.

s1[j] is s1[1] → 'b', s2[i] is s2[0] → 'b'.

So the code checks if s1[i] == s2[j] (a == a → yes) and s1[j] == s2[i] (b == b → yes). So outputs YES.

Sample 2:

Input:

aa

ab

len is same (2). Counts for s1: a:2, counts for s2: a:1, b:1 → counts differ. So output NO.

Another test case where counts are same but number of differing positions is not 2. For example:

s1 = 'abc', s2 = 'acb'. Then, differing positions are 1 and 2. So code would check s1[1] is 'b', s2[2] is 'b'; s1[2] is 'c', s2[1] is 'c'. So code outputs YES.

Another test case where counts are same but differing positions are 2, but the characters are not swapped. For example:

s1 = 'abcd', s2 = 'abce'. Then, differing positions are 3. So code outputs NO.

Another test case: s1 = 'abcd', s2 = 'abdc'. Differing positions are 2 and 3. Check s1[2] is 'c', s2[3] is 'c'; s1[3] is 'd', s2[2] is 'd'. So code outputs YES.

Another test case: s1 = 'aabb', s2 = 'abab'. The differing positions are 1 and 3. s1[1] is 'a', s2[3] is 'b'; s1[3] is 'b', s2[1] is 'a'. So code checks s1[i] (a) == s2[j] (b)? No. So code returns NO. Because even though the counts are the same, the two differing positions cannot be swapped to make the strings equal. So this would output NO.

So in this case, the code works.

Thus, the code seems correct.

Now, in Python, for handling large inputs, using a loop to check the differing indices is manageable. For n up to 1e5, the loop is O(n), which is acceptable.

Now, code structure.

Read s1 and s2.

Check len(s1) == len(s2). If not, print NO.

Else, check if the character counts are the same.

To check the counts, using two arrays of size 26.

Then, collect the differing indices.

If the number of differing indices is not 2, print NO.

Else, check the two positions.

Now, code:

In Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s1 = input_stream.readline().rstrip("\n").strip()

    s2 = input_stream.readline().rstrip("\n").strip()

    if len(s1) != len(s2):

        print("NO", file=output_stream)

    else:

        # Check character counts

        count1 = [0] * 26

        count2 = [0] * 26

        for c in s1:

            count1[ord(c) - ord('a')] += 1

        for c in s2:

            count2[ord(c) - ord('a')] += 1

        if count1 != count2:

            print("NO", file=output_stream)

        else:

            # Collect differing positions

            diff = []

            for i in range(len(s1)):

                if s1[i] != s2[i]:

                    diff.append(i)

                    if len(diff) > 2:

                        break

            if len(diff) != 2:

                print("NO", file=output_stream)

            else:

                i, j = diff

                if s1[i] == s2[j] and s1[j] == s2[i]:

                    print("YES", file=output_stream)

                else:

                    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
aa
ab
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

Sample 2:

Input:

aa

ab

len same 2.

count1: a:2.

count2: a:1, b:1 → not equal. Output NO.

Another test case:

s1 = 'aab', s2 = 'aba'.

count1: a:2, b:1.

count2: same.

Differing positions: 1 and 2.

s1[1] is 'a', s2[2] is 'a'; s1[2] is 'b', s2[1] is 'b'. So code outputs YES.

Another test case where the counts are same but differing positions are 2, but swap not possible.

s1 = 'abcd', s2 = 'abce'.

Differing position is index 3 (d vs e). So len(diff) is 1 → output NO.

Another case where counts are same, but three differing positions. So code breaks early once diff exceeds 2. For example, s1 = 'abc', s2 = 'ade'. Differing positions: 1 and 2. Then, len(diff) is 2. But s1[1] is 'b', s2[1] is 'd'; s1[2] is 'c', s2[2] is 'e'. So code checks if 'b' == 'e' (no), so outputs NO.

Thus, the code seems correct.
</think>

```python
s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    count1 = [0] * 26
    count2 = [0] * 26
    for c in s1:
        count1[ord(c) - ord('a')] += 1
    for c in s2:
        count2[ord(c) - ord('a')] += 1
    if count1 != count2:
        print("NO")
    else:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2:
                    break
        if len(diff) != 2:
            print("NO")
        else:
            i, j = diff
            if s1[i] == s2[j] and s1[j] == s2[i]:
                print("YES")
            else:
                print("NO")
```
