<think>
Okay, let's tackle this problem. So the task is to construct a string s with exactly k occurrences of the substring t, and s should be as short as possible. Hmm. The examples give some clues. Like the first example where t is "aba" and k is 4. The output is "ababababa". Let's see why. Each occurrence of "aba" here overlaps with the next. For example, positions 0-2, then 1-3, then 2-4, etc. So each added 'a' might contribute to a new occurrence. So maybe the key is to find overlapping possibilities where adding a part of t can create multiple new occurrences.

Wait, the goal is to minimize the length of s. So we want to maximize overlaps between the occurrences of t. So the first occurrence is t itself. Then each subsequent occurrence might share as much as possible with the previous one. But how much can they overlap?

For example, in the first example, t is "aba". The maximum possible overlap between two instances is when the suffix of the first matches the prefix of the second. Let's see the prefix function here. The prefix function for the string t (used in KMP algorithm) helps find the longest proper prefix which is also a suffix. For "aba", the prefix array is [0, 0, 1]. So the maximum overlap is 1 character. So when building the string, after the first "aba", adding "ba" would create a new occurrence. Wait, no. Let's see:

Original s starts as "aba". Then adding a 'b' and 'a' each time. Wait, maybe when you add the next part of t after the overlapping part.

Wait, the maximum possible overlap is the length of the longest prefix which is also a suffix. Let's call this value 'p'. Then, each new occurrence can be added by appending t[p:] each time. Because that way, the new occurrence starts after the first (length of t - p) characters. For example, for "aba", p is 1. So each additional occurrence adds t[1:] which is 'ba'. So adding 'ba' each time. So the first time, s is 'aba' (1 occurrence). Then adding 'ba' gives 'ababa' (two occurrences: positions 0-2 and 2-4). Then adding another 'ba' gives 'abababa' (3 occurrences?), but maybe I'm getting the count wrong. Let's see. Each 'ba' added adds a new occurrence. So if the initial is 'aba' (length 3, 1 occurrence), then each 'ba' adds 2 characters and increases the count by one. Wait, maybe each new addition of t[p:] adds a new occurrence. So in the first example, after the initial t, each addition of 'ba' (length 2) adds 1 occurrence. So for k=4, we need to add 3 more 'ba's. So total length is 3 + 3*2 = 9, which is the example's output.

So the general approach is:

1. Find the maximum possible overlap (p) between consecutive t's. This is determined by the longest prefix which is also a suffix of t.

2. Then, the initial string is t. Then, for each additional occurrence needed (k-1 times), append the substring t[p:] to s. Because each of these appends adds a new occurrence of t.

This way, the total length is n + (k-1)*(n - p). Because the first t contributes n characters, and each of the remaining (k-1) parts contributes (n - p) characters.

So the steps would be:

- Compute the maximum possible overlap p for t. That's the value of the last element in the prefix array of t.

- Then, the minimal s is t followed by (k-1) copies of t[p:].

So the problem reduces to calculating this p and constructing the string accordingly.

Let's see the second example. The input is "cat" with k=2. The prefix array for "cat" is [0,0,0], since there's no prefix that's also a suffix except the empty string. So p=0. So each additional occurrence requires appending the entire t. So the result is "cat" + "cat" (since k=2, so 1 addition). Which matches the example.

So how do we compute the prefix function for t?

The prefix function for a string t is an array pi where pi[i] is the length of the longest prefix (other than the entire substring) of the substring t[0...i] which is also a suffix. For example, for "aba", the pi array is [0,0,1]. For "abab", pi[3] is 2.

So to compute this, we can implement the standard KMP prefix function algorithm.

Once we have the maximum overlap p (which is pi[-1]), the rest is straightforward.

So the algorithm would be:

Compute p = pi[-1] of t.

s = t + (t[p:]) * (k-1)

This way, the initial occurrence is 1, and each of the (k-1) additions adds one occurrence.

So the code steps:

Read n, k and t.

Compute the prefix function for t, get p.

Construct s as t concatenated with (k-1) copies of t[p:].

Output s.

So the main task is to implement the prefix function correctly.

Let's test with the first example. t = 'aba', p is 1. So t[p:] is 'ba'. So s is 'aba' followed by 3 (since k=4) copies of 'ba', which is 'ababababa', which is correct.

Another example: if t is 'ababa', then the prefix array would have pi[-1] = 3. So t[p:] is 'aba'. So each additional occurrence adds 'aba', and the next occurrence would be overlapping.

So how to compute the prefix function?

The code for the prefix function is standard. Let's write a function to compute it.

The prefix function for a string s is computed as follows:

Initialize an array pi of the same length as s, with all zeros.

For i from 1 to len(s)-1:

   j = pi[i-1]

   while j > 0 and s[i] != s[j]:
       j = pi[j-1]

   if s[i] == s[j]:
       j += 1

   pi[i] = j

So that's the standard algorithm.

Once we have p = pi[-1], then we can proceed.

Now, for the code:

Read n and k from input.

Read t.

Compute the prefix function for t.

p = pi[-1]

result = t + (t[p:]) * (k-1)

Print result.

That's the code. Let's see if this handles all cases.

Another test case: if t is 'aaaaa', and k=3. The prefix function will have p=4 (since the maximum prefix-suffix is 4). So t[p:] is 'a'. So the result is 'aaaaa' followed by two 'a's. So the total is 5 + 2*1=7 characters. The occurrences would be 5 (initial) + 2 (each added 'a' adds one occurrence). Wait, let's see:

The initial string is 'aaaaa' (5 a's). Each added 'a' would add a new occurrence. Because when you add 'a' to the end, the last 5 characters are 'aaaaa' again. So for k=3, the initial 'aaaaa' is 1 occurrence. Adding one 'a' gives 6 a's. The substrings are 0-4, 1-5. So 2 occurrences. Wait, this approach may not be correct here. Wait, maybe the code would generate the correct answer.

Wait, the code for t='aaaaa', k=3. p is 4. So the code would produce 'aaaaa' + (k-1) * 'a' → 'aaaaa' + 'a' + 'a' → 'aaaaaaa' (7 a's). Now, how many occurrences of 'aaaaa' are there?

In 'aaaaaaa', the possible substrings are:

indices 0-4 → 'aaaaa'

1-5 → 'aaaaa'

2-6 → 'aaaaa'

So 3 occurrences. Which matches k=3. So the code works here.

Another example: t='abcabx'. Let's compute the prefix function. The pi array would be:

At index 0: 0.

index 1: 0 (a vs b).

index 2: 0 (a vs c).

index 3: 'a' matches, so 1.

index4: 'b' matches, so 2.

index5: check for x. The previous pi was 2. j=2. Compare s[5] (x) with s[2] (c). No match. j becomes pi[1] =0. Compare s[5] and s[0] (a). Not equal. So pi[5] is 0.

So p is 0. So adding the entire t each time. So for k=3, the code would produce 'abcabxabcabxabcabx'. Each occurrence is non-overlapping.

So that's correct.

Thus, the approach seems correct.

So the code steps are:

Implement the prefix function.

Compute p.

Construct s as t + (t[p:])*(k-1).

Thus, the code is straightforward.

Now, the code in Python.

Read n and k.

Then read t.

Compute the prefix function.

Then construct the result.

Let's code the prefix function.

In Python:

def compute_prefix(s):
    n = len(s)
    pi = [0]*n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

So for example, 'aba' gives [0,0,1].

Then p = pi[-1].

Then the answer is t + (t[p:] * (k-1)).

So putting it all together.

Now, code:

n, k = map(int, input().split())
t = input().strip()

# Compute prefix function
pi = [0] * n
for i in range(1, n):
    j = pi[i-1]
    while j > 0 and t[i] != t[j]:
        j = pi[j-1]
    if t[i] == t[j]:
        j += 1
    pi[i] = j

p = pi[-1]
result = t + t[p:] * (k-1)
print(result)

Testing this code with the first example:

Input:
3 4
aba

pi is [0,0,1]. p=1. t[p:] is 'ba'. So result is 'aba' + 'ba'*3 → 'ababababa' → correct.

Second example: 3 2, cat. p is 0. result is 'cat' + 'cat' → 'catcat'.

Another test case: t='aaaaa', k=3. code produces 'aaaaa' + 'a' *2 → 'aaaaaaa', which has 3 occurrences. Correct.

Thus, the code should work.
</think>

```python
n, k = map(int, input().split())
t = input().strip()

# Compute the prefix function for the string t
pi = [0] * n
for i in range(1, n):
    j = pi[i-1]
    while j > 0 and t[i] != t[j]:
        j = pi[j-1]
    if t[i] == t[j]:
        j += 1
    pi[i] = j

p = pi[-1]
result = t + t[p:] * (k-1)
print(result)
```