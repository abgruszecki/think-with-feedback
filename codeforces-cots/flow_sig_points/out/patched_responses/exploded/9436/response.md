<think>
Okay, so I need to solve this problem where Vasya can change up to k letters in his character's name to maximize the euphony, which is based on adjacent pairs of letters. Hmm. Let's think about how to approach this.

First, the problem is to maximize the sum of c(x,y) for each consecutive pair in the modified string. The constraints are that the string can be changed by replacing at most k characters. The string's length can be up to 100, and k can be up to 100. Oh right, and each replacement counts as changing a single character, regardless of what it was before.

So, the key here is dynamic programming. Because for each position in the string, the choice of which character to put there (possibly changing the original) depends on the previous character and how many changes we've made so far. So the state needs to track the current position, the last character used, and the number of changes made.

Let's model the DP. Let's say dp[i][c][k] represents the maximum euphony achievable up to the i-th character, where the i-th character is 'c', and we've used 'k' changes so far. Then, for each position, we consider all possible characters that the current position can be, and for each possible previous character, we add the bonus from the previous to current. We also track the number of changes used (if the original character is different from 'c', we increment the change count by 1, but only if it's within the allowed k).

Wait, but the original string's characters are given. So for each position i (0-based), the original character is s[i]. When we choose a different character for position i, that uses up a change. So the transitions would be: for each possible previous character (from the previous step), and for each possible current character (could be the original or any other, if we have changes left), we calculate the cost of changing (if needed) and update the DP accordingly.

The base case would be the first character. For the first character (position 0), we can choose any character. The cost here is the number of changes: if the original is different from the chosen character, we subtract 1 from k (if k allows it). For each possible chosen first character, we can track the initial state.

Then, for each subsequent position (i from 1 to len(s)-1), we look at all possible previous characters (from the DP state of i-1), and all possible current characters. For each combination, we calculate the new number of changes (previous changes + whether current character is changed), and if it's within the allowed k, we update the DP[i][current_char][new_changes] to be the maximum possible value.

The final answer is the maximum value in the DP for the last position, considering all possible characters and all possible change counts up to k.

But considering the constraints: the length of the string can be up to 100, and each position can have 26 possible characters, and k can be up to 100. So for each position, the DP state is 26 * 101 possibilities. For 100 positions, that's 100 * 26 * 101 = 262,600 states. Each state transition would involve 26 possible previous characters and 26 possible current characters. So for each state, 26 transitions. So the total operations would be 100 * 26 * 101 * 26 = 100 * 26^2 * 101. Let's compute that: 26^2 is 676. So 100 * 676 * 101 = 6,760,000 * 101? Wait 6,760,000 * 100 is 676,000,000, plus 6,760,000 *1, total 682,760,000. That's about 680 million operations. Wait, but that's a lot. Wait, but Python can handle around 1e8 operations in a second. So 680 million is 0.68e9, which would take about 6.8 seconds. But the time limit is 2 seconds. Hmm, that's a problem. So maybe we need to optimize this.

Wait, perhaps there's a way to make it more efficient. Let's see. Let's think about the transitions. For each position i, for each possible previous character (prev_char), and for each possible current character (curr_char), and for each possible number of changes used so far (prev_k), we can compute the transition.

Alternatively, for each position i, when considering the current character, the number of changes used so far can be up to min(k, i+1). Because at each position, you can change up to one character. So for position i, the maximum changes possible are i+1 (since the first position is index 0). So for the DP state, when processing position i, the possible k values are up to min(k, i+1). So for the first position, k can be 0 or 1. For the second, up to 2, etc. This reduces the number of states. For example, when the string is 100 characters long, but k is 100, then for position 0, the max k is 1, but for position 99, the max k is 100. So for each i, the max possible k is min(k, i+1). So the total number of states is sum_{i=0 to len(s)-1} 26 * (min(k, i+1)+1). Hmm, but I'm not sure if this reduces the operations enough. Let's compute for len(s) = 100, k=100. Then for each i from 0 to 99, min(k, i+1) is i+1, up to i=99 (min(100, 100) = 100). So sum from i=0 to 99 of 26*(i+2) (since the number of possible k values for each i is i+1 +1 (since k can be from 0 to i+1)). Wait, for each i, the number of possible k is min(k, i+1) + 1. Because for example, if i=0, and k=4, then possible k after position 0 is 0 or 1. So 2 possibilities. So sum from i=0 to 99 (26 * (i+1 +1)) ), but since k is 100, min(k, i+1) is i+1 for all i up to 99. So sum becomes 26 * sum (i+2) from i=0 to 99. Sum (i+2) is sum from 2 to 101, which is (101*102/2) - 1. So (101*102/2) - 1 = 5151 -1=5150? Wait, sum from 1 to n is n(n+1)/2. So sum from 2 to 101 is sum 1 to 101 minus 1. Which is 101*102/2 -1 = 5151 -1=5150. Then 26*5150 = 133,900. But that's the total number of possible states. But transitions between them? For each state (i, prev_char, prev_k), we need to consider all possible curr_char and the new_k. So for each state, we have 26 possibilities for curr_char, and for each, check if changing the original character (s[i]) to curr_char costs a change. So the new_k is prev_k + (curr_char != original_char). So for each transition, the new_k must be <=k. So per state, 26 transitions. So the total number of transitions would be 26 * 133,900 = 3,481,400. Which is manageable, right? Because 3 million operations in Python should be okay within 2 seconds. So perhaps this approach is feasible.

So the plan is to model the DP with state (position, last_char, changes_used), and track the maximum euphony possible. Let's outline the steps:

1. Preprocess the bonus pairs into a dictionary for O(1) lookups. The bonus between x and y is stored as a 2D array or a dictionary of dictionaries. For example, bonus[x][y] = c.

2. Initialize the DP for the first character. For the first character (position 0), we can choose any character. The number of changes used is 0 if we keep the original, or 1 (but only if k >=1). Then, the DP[0][c][changes] will be the maximum value (which for the first position is zero, since there's no previous character). Wait, no. The first character has no pairs before it, so the first character's choice only affects the next pairs. So the initial state is for the first character, and the value is 0, since there's no pair yet. Then, when we process the second character (position 1), the bonus is between the first and second character.

So the DP[i][c][k] represents the maximum total euphony up to position i, ending with character c and having used k changes. Then, when processing position i+1, we look at all possible previous characters (for DP[i][prev_c][prev_k]), and for each possible current character (curr_c), compute the bonus between prev_c and curr_c. Then, add that bonus to the previous total, and update DP[i+1][curr_c][new_k] if the new total is higher than the existing value.

So the steps are:

Initialize DP for position 0. For each possible character c that can be in position 0:

- If the original character (s[0]) is c, then changes_used is 0. So if 0 <=k, then DP[0][c][0] = 0.

- Else, if we change it to c, then changes_used is 1. So if 1 <=k, then DP[0][c][1] =0.

Then, for each position i starting from 1 up to len(s)-1:

For each possible previous character (prev_c) and previous change count (prev_k):

For each possible current character (curr_c):

Compute the bonus between prev_c and curr_c.

Compute the number of changes needed for curr_c: if curr_c is the original s[i], then 0. Else, 1. So new_k = prev_k + (curr_c != s[i] ? 1 : 0). If new_k >k, skip.

If new_k <=k, then the new DP state for i, curr_c, new_k is the maximum between its current value and (DP[i-1][prev_c][prev_k] + bonus_value).

So the key is to precompute all possible transitions, keeping track of the maximum possible sum.

Now, the bonus values: if a pair x y is not present in the input, then c(x,y) is 0. So the bonus dictionary should default to 0 for any pair not present.

So for the bonus structure, we can initialize a 26x26 array (since there are 26 letters) with all zeros. Then, for each pair in the input, we update the corresponding entry.

Now, considering that the letters are from 'a' to 'z', we can map each character to 0-25 for easier indexing.

So, for example, 'a' is 0, 'b' is 1, ..., 'z' is 25.

So, first, in code:

- Read s and k.

- Read n, then read n lines of x, y, c. For each, compute the indices (x_ord = ord(x) - ord('a'), etc.), and set bonus[x_ord][y_ord] = c.

Then, the DP array can be represented as a list of dictionaries, or as a 3D array. But given that in Python, 3D arrays can be memory-heavy, but the state sizes are manageable (as discussed earlier), perhaps using a dictionary for each step, or using a list of lists of dictionaries.

Wait, in Python, the maximum possible size is len(s) = 100, each with 26 possible characters, and 101 possible k (since k can be up to 100). So a 3D array of size 100 x26 x101. Each cell is an integer. So 100 *26 *101 = 262600 entries. Each being a 4-byte integer, that's about 1MB, which is manageable.

But perhaps using a 2D array for each step (since for each position, we can discard the previous step's data). Because when processing position i, we only need the data from position i-1. So we can optimize space by using two 2D arrays: previous and current.

Yes, that's a good idea. Because for each position i, we can compute the current DP based on the previous position's DP.

So, for each step i, we can have a 2D array (current) of size 26 x (k+1), which holds the maximum possible sum up to position i for each character and change count.

But since k can be up to 100, for each step, the possible change counts are up to min(k, i+1). So for each step, we can iterate through possible previous change counts and current changes.

So here's the plan for the code:

- Precompute the bonus matrix as a 26x26 array.

- Initialize the DP for position 0. For each possible character c (0-25):

   - original_char = ord(s[0]) - ord('a')

   - changes_needed = 0 if c == original_char else 1

   - if changes_needed > k: skip (since can't use that character)

   - else: set previous_dp[c][changes_needed] = 0 (since no pairs yet)

- For each position i from 1 to len(s)-1:

   - create a new current_dp 2D array initialized to -infinity (or some minimal value)

   - original_char = ord(s[i]) - ord('a')

   - for each possible prev_char in 0..25:

      - for each possible prev_k in 0..k:

         - if previous_dp[prev_char][prev_k] is -infinity: skip (no path to this state)

         - for each possible curr_char in 0..25:

             - changes_needed = 0 if curr_char == original_char else 1

             - new_k = prev_k + changes_needed

             - if new_k >k: skip

             - bonus_value = bonus[prev_char][curr_char]

             - total = previous_dp[prev_char][prev_k] + bonus_value

             - if total > current_dp[curr_char][new_k]:

                 update current_dp[curr_char][new_k] = total

   - set previous_dp = current_dp

- After processing all positions, the maximum value is the maximum over all characters and all possible k (up to min(k, len(s))) in the last previous_dp array.

But how to handle the initial step? For position 0, the previous_dp is initialized for the first character.

Wait, for the first character, the sum is 0 (no pairs). So after processing the first character, the sum remains 0. Then, when processing the second character (position 1), we add the bonus between the first and second character.

So the code steps are:

Initialize previous_dp as a 26 x (k+1) array filled with -infinity.

For the first character (i=0):

   original_char = ord(s[0]) - ord('a')

   for each possible c in 0..25:

      changes_needed = 0 if c == original_char else 1

      if changes_needed > k: continue

      if previous_dp[c][changes_needed] < 0:

          previous_dp[c][changes_needed] = 0

Then, for each subsequent position:

   create a current_dp filled with -infinity.

   original_char = ord(s[i]) - ord('a')

   iterate over all possible prev_char, prev_k:

       if previous_dp[prev_char][prev_k] is -infinity: skip

       for curr_char in 0..25:

           changes = 0 if curr_char == original_char else 1

           new_k = prev_k + changes

           if new_k >k: continue

           bonus_val = bonus[prev_char][curr_char]

           new_total = previous_dp[prev_char][prev_k] + bonus_val

           if new_total > current_dp[curr_char][new_k]:

               current_dp[curr_char][new_k] = new_total

   previous_dp = current_dp

After all positions are processed, the answer is the maximum value in previous_dp across all characters and all possible k up to k.

Wait, but in the first step, for i=0, the previous_dp for c and changes_needed is 0 (since no pairs yet). Then, when i=1 (second character), for each possible prev_char (from i=0) and curr_char (i=1), the bonus between prev_char and curr_char is added once.

Yes. So the code should work.

Now, in terms of data structures, for previous_dp and current_dp, using a 2D array for each is manageable. But in Python, using a list of lists would be efficient.

But for each step, we need to reset current_dp to -infinity for all possible (c, k). But given that k can be up to 100, and 26 characters, each current_dp would be 26 x 101 elements, which is manageable.

So for each step:

current_dp = [[-infinity] * (k+1) for _ in range(26)]

Then, for each possible prev_char, prev_k, and curr_char, compute new_k and update current_dp accordingly.

Now, optimizing for speed in Python:

- Precompute the original characters for each position as a list of integers (0-25).

- Precompute the bonus matrix as a list of lists (26x26, default to 0).

- Use loops for the prev_char and curr_char, using integers 0-25.

- Precompute for each position i, the original character.

So in code:

s, k = input().split()
k = int(k)
n = int(input())
bonus = [[0]*26 for _ in range(26)]
for _ in range(n):
    x, y, c = input().split()
    x = ord(x) - ord('a')
    y = ord(y) - ord('a')
    bonus[x][y] = int(c)

original = [ord(c) - ord('a') for c in s]

Then, proceed with the DP.

Now, the DP for position 0:

prev_dp = [[-inf]*(k+1) for _ in range(26)]
original_char = original[0]
for c in range(26):
    changes = 0 if c == original_char else 1
    if changes > k:
        continue
    prev_dp[c][changes] = 0

Then, for each position i from 1 to len(s)-1:

current_dp = [[-inf]*(k+1) for _ in range(26)]
original_char = original[i]
for prev_char in range(26):
    for prev_k in range(k+1):
        if prev_dp[prev_char][prev_k] == -inf:
            continue
        for curr_char in range(26):
            changes = 0 if curr_char == original_char else 1
            new_k = prev_k + changes
            if new_k > k:
                continue
            current_sum = prev_dp[prev_char][prev_k] + bonus[prev_char][curr_char]
            if current_sum > current_dp[curr_char][new_k]:
                current_dp[curr_char][new_k] = current_sum
prev_dp = current_dp

Wait, but for each position, we have to loop through all possible prev_char (0-25), prev_k (0 to k), and curr_char (0-25). For each, check if new_k exceeds k. So for len(s) = 100, this is 100 steps. For each step, 26 * (k+1) * 26 operations. But k can be up to 100, so for each step, 26 * 101 *26 = 26^2 * 101 = 676 * 101 = 68,276 operations per step. For 100 steps, that's 6,827,600 operations, which is acceptable in Python for 2 seconds.

But wait, when the string is of length 1, then there are no pairs. So the sum is 0. So in that case, the code should output 0.

So, after processing all positions, the maximum value is the maximum among all prev_dp[c][k_used], where k_used ranges from 0 to k.

So, finally:

max_sum = -inf
for c in range(26):
    for used in range(k+1):
        if prev_dp[c][used] > max_sum:
            max_sum = prev_dp[c][used]
print(max_sum)

But what if the string is empty? The problem says the string is non-empty, so we don't need to handle that.

Testing the first example:

Input:
winner 4
4
s e 7
o s 8
l o 13
o o 8

Original string is 'winner' (len 6). So after processing each position:

The first character is 'w' (index 22). For the first position, possible options are to change it to 'l' (index 11) with changes=1, etc. But according to the example, the best is to change the first character to 'l', and others as needed.

But in code, the DP would track all possibilities.

Let's see for the first example:

The modified string is 'looser'. So the pairs are 'l o', 'o o', 'o s', 's e', 'e r'. The bonuses are:

l o: 13, o o:8, o s:8 (but the input gives 's e' as 7. Wait, original input lines for the first example:

The input lines after n=4 are:

s e 7

o s 8

l o 13

o o 8

So the bonus for o o is 8. So the pairs in 'looser' are:

l o (13), o o (8), o s (8), s e (7). The 'e r' pair is not present, so contributes 0.

So the sum is 13 +8 +8 +7 +0 = 36. Which matches the sample.

So the code should correctly track these transitions.

But how?

In the first position (i=0), the original character is 'w' (22). For the first step, changing to 'l' (11) requires 1 change. So prev_dp[11][1] =0. Then, for position 1 (original 'i' (8)), changing to 'o' (14) requires changes=1 (since original is 'i'). So new_k is 1+1=2. Then, the bonus for 'l' and 'o' is 13.

So in position 1, the current_dp for 'o' and k=2 would be 13. Then, proceed to position 2 (original 'n' (13)), and so on.

So the code should accumulate these values.

Now, the code seems correct.

Another test case is the second example:

Input:
abcdef 1
5
a b -10
b c 5
c d 5
d e 5
e f 5

So the original string is 'abcdef'. The optimal is to change the 'b' to 'c' (uses 1 change), making the string 'accdef'. The pairs are a c (bonus 0), c c (0), c d (5), d e (5), e f (5). Wait, no. Wait, changing 'b' to 'c' gives the pairs 'a c' (bonus 0, since not in the list), 'c c' (0), 'c d' (5), 'd e' (5), 'e f' (5). So sum is 0+0+5+5+5=15. Wait, but the sample output is 20. Hmm, maybe I'm misunderstanding the example.

Wait the sample output is 20. Let's see.

Wait the input's allowed k is 1.

The notes say that the output is 20. Let's think. The optimal is to change 'a' to 'c', which uses 1 change. Then the string becomes 'cbcd ef'. The pairs are 'cb' (c and b: but no bonus, but wait, the original string after modification would be 'c bcdef'? Wait, maybe I'm missing something. Wait, the original string is 'abcdef', and with k=1.

If we change 'b' to 'c', the string becomes 'accdef'. The pairs are a-c (0), c-c (0), c-d (5), d-e (5), e-f (5). Total is 15. But sample output is 20.

Hmm, maybe the optimal is to change 'a' to 'b'. Wait, but that's allowed. Let's see:

Original string is a b c d e f.

If we change a to b (using 1 change), the string becomes 'b b c d e f'. The pairs are b-b (bonus 0), then b-c (5), c-d (5), d-e (5), e-f (5). Sum is 0+5+5+5+5=20. Which matches the sample output. So the code needs to track this possibility.

So the code must consider changing the first character. How?

In the code, for the first character (a), changing to 'b' (1) would require a change of 1 (since a != b). So for the first position, prev_dp[1][1] =0.

Then, for the second character (original 'b'), the code can either leave it as 'b' (no changes), or change it. But since we have k=1, if we change the first character, then in the second position, we can't make any more changes.

So for the second position (i=1, original 'b'):

prev_char is 'b' (from changing first character), prev_k is 1.

For curr_char, if it's 'b', then changes_needed is 0. new_k is 1+0=1 <=1.

The bonus between 'b' (prev_char) and 'b' (curr_char) is 0. So the sum is 0 (from previous step) +0 (bonus) =0. But the previous step's sum after first position is 0 (since no pairs yet). Then, for the second position, the pair is 'b' and 'b', which contributes 0. So the sum for position 1 (i=1) is 0+0=0.

But then, the third position (original 'c') can be 'c', contributing bonus between 'b' and 'c' (5). So sum becomes 0 +5. Then, each subsequent pair contributes 5. So total is 0 (from first two steps) +5 (third step) +5 (fourth) +5 (fifth) +5 (sixth) → total 20.

Yes. So the code would track this path.

Thus, the code should correctly compute this case.

Now, the code uses a dynamic programming approach with O(len(s) * 26 * k) time and O(26 *k) space, which is feasible for the problem's constraints.

So, the final code should implement this logic.

Another possible optimization is to use the min(k, i+1) for the possible k in each step, but in the code, since new_k is checked against k, it's automatically handled. So when prev_k is up to min(k, i), then new_k (after i+1 steps) can be up to min(k, i+1). So no need to track that explicitly.

Now, code in Python:

We need to handle the initial case when the string has length 1 (so no pairs, sum is 0 regardless of changes, but only allowed up to k changes).

But the code should handle it.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    import sys
    from math import inf

    # Read input
    s, k = input_stream.readline().split()
    k = int(k)
    n = int(input_stream.readline())
    bonus = [[0]*26 for _ in range(26)]
    for _ in range(n):
        x, y, c = input_stream.readline().split()
        x_ord = ord(x) - ord('a')
        y_ord = ord(y) - ord('a')
        bonus[x_ord][y_ord] = int(c)

    original = [ord(c) - ord('a') for c in s]
    length = len(original)
    if length == 0:
        print(0, file=output_stream)
        return

    # Initialize DP for the first character
    prev_dp = [[-inf]*(k+1) for _ in range(26)]
    first_char = original[0]
    for c in range(26):
        changes = 0 if c == first_char else 1
        if changes > k:
            continue
        prev_dp[c][changes] = 0

    # Process remaining characters
    for i in range(1, length):
        current_dp = [[-inf]*(k+1) for _ in range(26)]
        current_char_orig = original[i]
        for prev_c in range(26):
            for prev_used in range(k+1):
                if prev_dp[prev_c][prev_used] == -inf:
                    continue
                for curr_c in range(26):
                    changes = 0 if curr_c == current_char_orig else 1
                    new_used = prev_used + changes
                    if new_used > k:
                        continue
                    current_sum = prev_dp[prev_c][prev_used] + bonus[prev_c][curr_c]
                    if current_sum > current_dp[curr_c][new_used]:
                        current_dp[curr_c][new_used] = current_sum
        prev_dp = current_dp

    # Find the maximum sum across all possibilities
    max_sum = -inf
    for c in range(26):
        for used in range(k+1):
            if prev_dp[c][used] > max_sum:
                max_sum = prev_dp[c][used]
    print(max_sum, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
abcdef 1
5
a b -10
b c 5
c d 5
d e 5
e f 5
""",
            "output": \
"""\
20
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

s='abcdef' (len 6), k=1.

After changing the first character to 'b', the sum is 0 (for the first pair, but there are no pairs for the first character). Wait, no. The first pair is between the first and second character.

Wait, the modified string is 'b bcdef' → no, the modified string after changing 'a' to 'b' is 'bbcdef'. So the pairs are b-b, b-c, c-d, d-e, e-f. The bonuses are 0 (for b-b, no bonus), 5 (b-c), 5 (c-d), 5 (d-e),5 (e-f). Sum is 0+5+5+5+5=20.

Yes. So the code must find this path.

In code:

In the first step (i=0), original_char is 'a' (0). The possible curr_char can be 'b' (1), with changes_needed=1. So prev_dp[1][1] =0.

For i=1 (original 'b'), prev_char=1 (b), prev_k=1.

current_char can be 'b' (changes_needed=0), new_k=1+0=1 ≤1.

bonus between 'b' and 'b' is 0. So sum is 0+0=0. So current_dp[1][1] is 0.

For i=2 (original 'c'), curr_char can be 'c' (changes_needed=0), new_k=1+0=1. The prev_char is 'b' (1). The bonus between 'b' and 'c' is 5. So sum is 0+5=5.

For i=3 (original 'd'), curr_char 'd' (changes 0), new_k=1. bonus between 'c' and 'd' is5. sum 5+5=10.

And so on. So the code accumulates the 5's, leading to a total of 20.

Thus, the code should be correct.

Now, coding this in Python with the necessary steps.
</think>

```python
def main():
    import sys
    from math import inf

    # Read input
    s, k = sys.stdin.readline().split()
    k = int(k)
    n = int(sys.stdin.readline())
    bonus = [[0]*26 for _ in range(26)]
    for _ in range(n):
        x, y, c = sys.stdin.readline().split()
        x_ord = ord(x) - ord('a')
        y_ord = ord(y) - ord('a')
        bonus[x_ord][y_ord] = int(c)

    original = [ord(c) - ord('a') for c in s]
    length = len(original)
    if length == 0:
        print(0)
        return

    # Initialize DP for the first character
    prev_dp = [[-inf]*(k+1) for _ in range(26)]
    first_char = original[0]
    for c in range(26):
        changes = 0 if c == first_char else 1
        if changes > k:
            continue
        prev_dp[c][changes] = 0

    # Process remaining characters
    for i in range(1, length):
        current_dp = [[-inf]*(k+1) for _ in range(26)]
        current_char_orig = original[i]
        for prev_c in range(26):
            for prev_used in range(k+1):
                if prev_dp[prev_c][prev_used] == -inf:
                    continue
                for curr_c in range(26):
                    changes = 0 if curr_c == current_char_orig else 1
                    new_used = prev_used + changes
                    if new_used > k:
                        continue
                    current_sum = prev_dp[prev_c][prev_used] + bonus[prev_c][curr_c]
                    if current_sum > current_dp[curr_c][new_used]:
                        current_dp[curr_c][new_used] = current_sum
        prev_dp = current_dp

    # Find the maximum sum across all possibilities
    max_sum = -inf
    for c in range(26):
        for used in range(k+1):
            if prev_dp[c][used] > max_sum:
                max_sum = prev_dp[c][used]
    print(max_sum)

if __name__ == "__main__":
    main()
```
