<think>
Okay, let's see. The problem is to find the minimum number of operations needed to convert some substring of the given string into "ACTG". Each operation can change a character to the next or previous in a circular way. So, for example, A can go to Z (previous) or B (next), each costing 1 operation.

Hmm. The first thing that comes to mind is that for every possible 4-length substring in the input string, we need to compute how many operations are required to turn it into "ACTG". Then, pick the minimum among all those.

But wait, the input's maximum n is 50. So there are 50 - 3 = 47 possible starting positions for 4-length substrings. For each of these 47 substrings, we need to compare each of the four characters to the target "ACTG" and calculate the minimal steps for each character, then sum them up. The total possible substrings to check are up to 47, each with 4 characters. So that's manageable even if n is 50. The total operations would be 47 * 4 = 188 steps, which is trivial.

So the approach is:

1. Iterate through all possible starting indices in the input string where a 4-length substring can be formed.
2. For each such substring (s[i], s[i+1], s[i+2], s[i+3]), compute the cost for each character to convert to 'A', 'C', 'T', 'G' respectively.
3. Sum the costs for the four characters. Keep track of the minimum sum across all substrings.
4. The answer is the smallest sum found.

Now, the key part is calculating the minimal steps between two characters. For a given current character c and target character t, what's the minimal steps?

The alphabet is circular, so for example, from A to Z is 1 step (previous), but from A to Y would be 2 steps (previous twice). But for each pair, the minimal steps can be calculated as the minimum of moving forward or backward.

Wait, how to compute that. Let's think of the alphabet as a circle with 26 letters. The steps can be either clockwise or counter-clockwise. For any two characters, the minimal steps between them is the minimum of ( (ord(t) - ord(c)) % 26, (ord(c) - ord(t)) % 26 ), but since moving forward or backward can be optimized. Wait, perhaps another approach: the minimal steps between c and t is min( (d), 26 - d ), where d is the absolute difference between their positions. Because moving forward d steps, or backward (26 - d) steps, whichever is smaller.

Yes. For example, if c is 'A' (0) and t is 'Z' (25), d is 25. So min(25, 1) is 1. That's correct. So the formula is:

d = abs(ord(c) - ord(t))

min(d, 26 - d)

So for each character in the substring, compute this value for the corresponding target character, sum all four, and find the minimal sum.

So the plan is solid.

Now, let's think of possible optimizations. Since the input is small, there's no need for any optimizations here, but the approach is already optimal. Because the maximum possible number of substrings is 47 (for n=50), and each substring's cost is O(4) operations, the total computation is negligible. So the code will be straightforward.

So, in Python:

- Read n and s.
- The target is "ACTG".
- For each i from 0 to len(s)-4 inclusive:
   - Take substring s[i:i+4]
   - For each of the four positions, compute the minimal steps between the current char and target[j] (j=0 to 3)
   - Sum them and keep track of the minimum.

Yes. So the code structure would be:

n = int(input())
s = input().strip()
target = 'ACTG'
min_ops = float('inf')

for i in range(len(s) - 3):
    current_sub = s[i:i+4]
    total = 0
    for j in range(4):
        c = current_sub[j]
        t = target[j]
        # compute steps between c and t
        c_ord = ord(c)
        t_ord = ord(t)
        diff = abs(c_ord - t_ord)
        total += min(diff, 26 - diff)
    if total < min_ops:
        min_ops = total

print(min_ops)

Wait, that's the code. Let's test the first example:

Input:
4
ZCTH

The substring is Z C T H.

Compare to ACTG:

Z -> A: ord('Z') is 90, ord('A') is 65. diff is 25. min(25, 1) → 1.
C is already C → 0.
T is already T → 0.
H → G: diff is 1, so 1. Total is 1+0+0+1=2. Which matches the example.

Second example:

Input:
5
ZDATG

Possible substrings are indexes 0-4 (ZDATG) and 1-4 (DAT... but length 5, so possible substrings are indices 0-3 (ZDAT) and 1-4 (DAT G). Let's see.

Looking for the best one. The second example's output is 5.

The optimal is changing the substring starting at index 1: DATG → but need to get ACTG.

Wait, the sample input is ZDATG. The substring that becomes ACTG is "DATG" → indexes 1-4. Let's see:

D → A: D is 68, A is 65. diff is 3. min(3, 23) → 3 steps. (since 3 steps back: D→C→B→A)
A → C: A to C is +2, so 2 steps.
T is T: 0.
G is G: 0. Sum is 3+2+0+0=5. Which matches the sample.

So the code should capture that.

Third example: AFBAKC → substring positions are 0-3 (AFBA), 1-4 (FB AK), 2-5 (BAKC). Let's see the example output is 16.

Wait, the input is AFBAKC. The correct answer is 16. Let's see which substring gives this.

Looking for each 4-length substring:

First substring: A F B A → target A C T G.

A → A: 0 steps.

F → C: F is 70, C is 67. diff is 3. Steps: 3 (since 70-67=3, so forward? Wait, no. The difference is 3, so steps can be min(3, 23) → 3. So F to C requires 3 steps. But how? Let's see: F can go backward 3 steps (F→E→D→C), which is 3 steps. Yes.

Then B → T: B is 66, T is 84. The difference is 84-66=18. So min(18, 8) → 8 steps. Because 26-18=8. So B can go forward 18 steps (which is same as backward 8 steps). So 8 steps.

A → G: A is 65, G is 71. 71-65=6 → min(6, 20) → 6 steps. Sum is 0+3+8+6=17. Not the answer.

Another substring: AFBAKC's possible substrings:

But let's check all possibilities.

But in the third example, the output is 16. So maybe another substring.

For example, the substring is FBAK: check F→A (difference 5 (F to A is 5 steps back), so min(5, 21) →5). B→C: difference is 1 (B to C is +1 →1). A→T: A to T is 19 steps (A→T is 19 steps forward, or 7 steps backward. So min(19,7) →7. K→G: K is 75, G is 71. 75-71=4. So 4 steps. Sum 5+1+7+4=17. No.

Alternatively, the substring might be BA KC (but indexes 2-5: BA K C? Wait, the input is AFBAKC. Let's index as follows:

Indices 0: A, 1:F, 2:B, 3:A, 4:K, 5:C.

Possible substrings are:

0-3: A F B A → sum 0+3+8+6=17.

1-4: F B A K → target A C T G.

F → A: diff is 5 →5 steps.

B → C: 1 step.

A → T: 19 steps vs 7. 7 steps.

K → G: K is 75, G is 71. 4 steps. Sum is 5+1+7+4=17.

Another substring is 2-5: B A K C → target A C T G.

B → A: 1 step (backwards).

A → C: 2 steps.

K → T: K (75) to T (84). 84-75=9. min(9, 17) →9.

C → G: C is 67, G is 71. 4 steps. Sum 1+2+9+4=16. Oh right! So this is the substring that gives 16. So in the code, when i=2, the substring is BAKC. Wait, no. Wait, substring from index 2 to 5 (since 2,3,4,5). So the substring is B A K C. So each character in the substring is B, A, K, C.

The target is A, C, T, G.

So:

B (66) → A (65). diff is 1. So 1 step.

A (65) → C (67). diff is 2. So 2 steps.

K (75) → T (84). diff is 9. min(9, 17) →9 steps.

C (67) → G (71). diff is 4. 4 steps. Sum 1+2+9+4=16. Which is the correct answer.

So the code would capture this by checking all possible substrings.

So the code is correct.

Now, in Python, the code reads the input, loops through each possible starting index (from 0 to len(s)-4), then for each of the four characters in the substring, computes the minimal steps, sums them, and keeps the minimum.

Yes.

Now, code-wise, the code is straightforward and should handle all cases correctly.

Now, for edge cases:

What if the string is exactly "ACTG"? Then the answer is 0.

Another case: a string where multiple substrings have different costs. The code correctly picks the minimal.

Another test case: let's say the string is "ZCTH" (as the first example). The code checks the only possible substring (the entire string) and computes 1+0+0+1=2.

So the code seems correct.

Therefore, this approach is optimal and the code should work.
</think>

```python
n = int(input())
s = input().strip()
target = 'ACTG'
min_ops = float('inf')

for i in range(len(s) - 3):
    total = 0
    for j in range(4):
        c = s[i + j]
        t = target[j]
        diff = abs(ord(c) - ord(t))
        total += min(diff, 26 - diff)
    if total < min_ops:
        min_ops = total

print(min_ops)
```