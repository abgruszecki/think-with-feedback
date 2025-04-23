<think>
Okay, I need to solve this problem where I have to find the maximum number of non-overlapping substrings of length k, all consisting of the same character. And all these substrings must be made of the same character. Oh wait, wait. Wait, the problem says that all the x substrings must have the same character. So, for example, if we choose some 'a's and some 'b's, that's not allowed. All the selected substrings must be of the same character. So the level x is the maximum possible such x, considering all possible characters.

So the approach is: for each possible character (from 'a' to 'z'), compute the maximum number of non-overlapping k-length substrings of that character. Then, take the maximum among all characters. That will be the answer.

Ah right. So the steps are:

1. For each character c in 'a' to 'z':
   a. Find all positions in s where there are consecutive c's of length at least k.
   b. For each such run, determine how many non-overlapping k-length substrings can fit.
   c. Sum these counts for all runs of c to get the total possible for c.
2. The maximum total across all c is the answer.

So the key is, for each character, compute how many non-overlapping k-length blocks we can form.

But how do we efficiently compute this for each character?

Let's think about how to process a single character. Let's say the character is 'a'. We scan the string, find sequences of 'a's. For each such sequence, calculate how many non-overlapping k-length substrings can be made.

For example, if a sequence is of length 5, and k=2. Then we can have 5//2=2, but wait, 5 divided by 2 is 2 with remainder 1. So in a sequence of length 5, how many non-overlapping 2-length substrings? The first starts at 0, next starts at 2. So positions 0-1, 2-3. That's 2. The remaining 4th position is ignored. So for a sequence of length m, the number is floor( (m - k + 1) / k ) + 1? Wait, no. Wait, the maximum number of non-overlapping k-length substrings in a run of m consecutive c's is (m - k) // (k) + 1? Or maybe (m) // k. Hmm.

Wait, for m=5, k=2. The maximum is 2: the first substring starts at index 0, ends at 1. Then next starts at 2, ends at 3. The remaining 4 (index 4) can't form a substring. So total is 2. So (5 - 2) + 1 = 4, divided by k? Wait, (5 - 2 +1) =4, divided by k gives 2. So maybe (m -k +1) // k +1? Wait, no. Wait, in this case, m=5, k=2. m -k +1 is 4. 4//2 =2. So 2. Which matches.

Wait, for a run of length m, the maximum number of non-overlapping k-length substrings is (m -k +1) // k +1? No, wait, let's see:

Wait, the maximum number of non-overlapping substrings is floor( (m) / k ). Because in the best case, you can have as many as possible. Let's test:

If m=2: 1.

m=3: 1 (if k=2, then 3-2+1=2, 2//2=1. So yes.

Wait, for m=4, k=2: 2.

Yes, 4/2=2.

So the formula is m // k? Wait, no. Wait, m=5, k=2: 5//2=2. Which matches.

So yes. For a run of m consecutive characters c, the number of non-overlapping k-length substrings is floor(m /k). Wait, wait. Let's see:

Another example: m=6, k=2: 3. 6//2=3. Correct.

m=5, k=3: 5//3=1. Which is correct. The first substring takes 0-2, then 3-5 is m=5, so 3-5 is positions 3,4,5? But m is 5, indices 0-4. So 5//3=1 (since 3*1=3 <=5). So yes.

Wait, but wait. Suppose the run is of length m. To find the maximum number of non-overlapping k-length substrings, you can have as many as possible, spaced every k characters. So the first substring starts at position 0, then next at k, then next at 2k, etc. The maximum number is (m) //k ?

Wait, no. Let's think again. For example, if m=5, k=2. Then the maximum is 2. Because you can have 2 substrings of length 2 (positions 0-1 and 2-3). Then 4 is left. So 5//2 is 2, which matches.

Yes, the formula for the number of non-overlapping substrings in a run is (m -k +1) // (k - (k-1)) ? Wait, not sure. Maybe it's (m) //k. Let's see:

Another example. m=3, k=1. Then 3//1=3. Which is correct. For each position, a substring of length 1. So 3.

So the formula is m // k.

Yes. So for a run of m consecutive c's, the maximum number of k-length substrings is m // k.

Wait, but when k is 2 and m is 5, 5//2=2. Which is correct.

So that's the formula.

So the plan is:

For each character c:

   Iterate through the string, find all consecutive runs of c's, and for each run of length m, compute m //k. Sum all those numbers for c. Then take the maximum over all c.

Wait, but this approach is O(n) time, which is acceptable for n up to 2e5.

Because for each character in the string, we process it once. So for all 26 letters, total time is O(26n) = 5e6, which is manageable.

But how do we compute the runs for each character efficiently?

Alternatively, we can process the string once, and for each run, note the character and the length. Then, for each character, accumulate the sum of (m //k) across all runs.

Yes. That's better.

Because processing the string once, grouping consecutive characters, and then for each group, add to the character's total the (length //k). Then, the maximum of all these totals is the answer.

This way, the time is O(n) for processing the string, plus O(26) to check all characters. So overall O(n).

Yes, this is efficient.

So the steps are:

1. Split the string into consecutive runs of the same character. For example, 'aaacaabb' becomes [ (a,3), (c,1), (a,2), (b,2) ].

2. For each run (c, m), compute m //k and add it to the total for c.

3. After processing all runs, the answer is the maximum total among all 26 letters.

Wait, but the problem states that the x substrings are non-overlapping. Wait, but the runs are non-overlapping. So if a run has multiple k-length substrings, they are non-overlapping. But when two runs of the same character are separated by other characters, then the substrings from the two runs are non-overlapping. So, in this approach, for each c, we are summing all (m//k) across all runs of c. Because the runs of c are non-overlapping (since they are consecutive runs, but separated by other characters), the k-length substrings from different runs of c are automatically non-overlapping.

But wait, imagine two runs of c separated by other characters. For example, ccc...ccc ... other ... ccc...ccc. Then, the k-length substrings from the first run and the second run are non-overlapping. So summing (m//k) for each run gives the maximum possible for that character.

So the approach is correct.

So the code can be structured as follows:

- Read the input: n, k, s.

- If k > n, output 0 (but since k is between 1 and n per the problem statement, perhaps this is not needed).

- Process the string into runs.

- For each run (c, m), add m//k to a dictionary or array for c.

- The maximum of the totals for all c is the answer.

But what about when k=1? Then, each run of c contributes m//1 = m. So for example, the input where n=2, k=1, s=ab. Then for 'a' and 'b', each contributes 1. So the total for each is 1. So the answer is 1. Which matches the second sample.

Yes.

Another sample: first example input:

s = 'aaacaabb', which is runs: a:3, c:1, a:2, b:2. k=2.

For 'a', the sum is 3//2=1 (from first run) + 2//2=1 (third run) → total 2. Which is the answer.

For 'b', 2//2=1. So 'a' is maximum, answer 2.

Yes.

Another sample: input is 4 2, abab. Each run is length 1. So for each character a and b, 1//2=0. So total is 0.

Which matches the third sample.

So the approach works.

So the code steps:

Read n, k.

s = input string.

Then process the string into runs.

Initialize a list for each character, 0.

current_char = first character of s.

count = 1.

Then for each next character in s[1:]:

   if same as current_char: increment count.

   else:

       add (current_char, count) to runs.

       current_char = current character.

       count = 1.

After the loop, add the last run.

Then, for each run (c, m):

   add (m //k) to the total for c.

The answer is the maximum of these totals.

Yes.

So code:

In Python:

Read n, k.

s = input().strip()

Then process runs.

Initialize a dictionary (or array for 26 letters) to track counts.

current_char = s[0]

count = 1

for char in s[1:]:

    if char == current_char:

        count +=1

    else:

        # process the run

        runs.append( (current_char, count) )

        current_char = char

        count = 1

runs.append( (current_char, count) )

Then, for each run in runs:

    c, m = run

    totals[c] += m //k

Then find the maximum value in totals.

But in code, how to represent totals? A dictionary with default 0.

Alternatively, use a list of 26 integers, index 0 for 'a', 25 for 'z'.

So:

totals = [0] * 26

for c, m in runs:

    idx = ord(c) - ord('a')

    totals[idx] += m //k

ans = max(totals)

print(ans)

Yes.

This will work.

Now, what about time constraints?

Processing the runs is O(n). Then processing the runs again to compute totals is O(n), but since the number of runs is O(n), but in practice, for each run, it's O(1) per run.

But for n up to 2e5, this is manageable.

So code:

n, k = map(int, input().split())

s = input().strip()

if k > n:

    print(0)

    exit()

# process runs

runs = []

if not s:

    print(0)

    exit()

current = s[0]

count = 1

for c in s[1:]:

    if c == current:

        count +=1

    else:

        runs.append( (current, count) )

        current = c

        count = 1

runs.append( (current, count) )

# compute totals

max_total = 0

totals = [0] * 26

for char, m in runs:

    idx = ord(char) - ord('a')

    totals[idx] += m // k

max_total = max(totals)

print(max_total)

This should handle all cases.

Testing the sample inputs:

First sample input:

8 2

aaacaabb

runs are a:3, c:1, a:2, b:2.

For 'a', 3//2=1 (first run), 2//2=1 (third run) → total 2.

For 'b', 2//2=1. So maximum is 2. Correct.

Second sample:

2 1

ab → runs a:1, b:1.

For a:1//1=1. For b:1//1=1. So maximum is 1.

Third sample:

4 2

abab → runs a:1, b:1, a:1, b:1. Each 1//2=0. So sum for each is 0.

So output 0.

All samples handled.

So code should be correct.
</think>

```python
n, k = map(int, input().split())
s = input().strip()

current = s[0] if n > 0 else ''
count = 1
runs = []

for c in s[1:]:
    if c == current:
        count += 1
    else:
        runs.append((current, count))
        current = c
        count = 1
if current:
    runs.append((current, count))

max_total = 0
totals = [0] * 26

for char, m in runs:
    idx = ord(char) - ord('a')
    totals[idx] += m // k

print(max(totals))
```