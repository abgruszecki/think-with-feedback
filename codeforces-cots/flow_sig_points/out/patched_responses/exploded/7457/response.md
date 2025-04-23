<think>
Okay, let's see. I need to solve this problem where Liss moves on stones based on instructions. Hmm, the problem says that each instruction in the string t corresponds to a step. For each instruction, if the color of the current stone matches the instruction, she moves forward by one. Otherwise, she stays. So the initial position is 1 (the first stone), and after all instructions, we have to find where she ends up.

Let me think about the approach. The straightforward way is to simulate each step. Start at position 0 (if we use 0-based indices) or 1 (1-based). Then, for each character in t, check if the current stone's color matches the instruction. If yes, increment the position. Otherwise, do nothing. But wait, the stones are 1-based in the problem statement. So the first stone is index 0 in a string? Or maybe the string s is 0-based in the code. Hmm, the problem says the i-th (1-based) character of s is the color of the i-th stone. So if the string s is "RGB", then stone 1 is 'R', stone 2 is 'G', etc. So when we represent the string s in code, the index is 0-based. So stone 1 is s[0], stone 2 is s[1], etc. So the position starts at 0 (since initial position is 1st stone) in 0-based terms. Wait, no. Let me clarify:

Initial position is 1st stone (position 1 in 1-based). So in code, the index would be 0. So for each step, if the current position is p (0-based index of s), then check if s[p] equals the current instruction. If yes, p increases by 1. But after moving, p must not exceed len(s)-1. But the problem states that it's guaranteed she won't move out of the sequence, so no need to handle that.

So the steps are:

1. Initialize current_position to 0 (since it's 0-based index for s, corresponding to the 1st stone).
2. Iterate over each character in t:
   a. For each instruction_char in t:
      i. Check if s[current_position] == instruction_char.
      ii. If yes, current_position += 1.
      iii. Else, do nothing.
3. After all instructions, the final position is current_position + 1 (converting back to 1-based for output).

Yes, that makes sense.

So the code needs to read two lines: s and t. Then process each character in t in order, updating the current position as per the rules.

Let's look at the first example:

Input:
RGB
RRR

s is "RGB", so stones are R, G, B (indices 0,1,2).

t is "RRR".

Initial position is 0 (1-based 1).

First instruction R: current stone is R (index 0), so move to 1 (index 1). Now position is 1 (1-based 2).

Second instruction R: current stone is G (s[1] is 'G') which doesn't match R. So no move.

Third instruction R: again, current stone is G, no move.

Final position is 1 (index), so output 1+1=2. Which matches the sample.

So the simulation approach works. Since the maximum size of s and t is 50 each, this is O(50) operations, which is trivial. So even with the largest possible inputs (both strings of length 50), 50 steps are needed, which is no problem for Python.

So the code is straightforward. Read s and t, iterate over each character in t, update the current position as necessary.

Now, code steps:

Read s from input().strip()

Read t from input().strip()

current_pos = 0 (0-based index in s)

for c in t:

    if current_pos >= len(s):  # but the problem says it's guaranteed not to move out, so this check is unnecessary.

    if s[current_pos] == c:

        current_pos +=1

At the end, output current_pos +1.

Yes. That's the code.

Testing the first sample:

s = 'RGB', t='RRR'

current_pos starts at 0.

First 'R' in t: s[0] is 'R' → move to 1.

Second 'R' in t: s[1] is 'G' → no move.

Third 'R' → same as above.

Final position is 1 → 1+1=2. Correct.

Second sample:

Input:

RRRBGBRBBB

BBBRR

s is "RRRBGBRBBB" → positions 0-based 0 to 10 (since length is 10). The stones are R, R, R, B, G, B, R, B, B, B.

t is "BBBRR".

Initial position is 0.

Processing 'B' → current stone is R (s[0] is R). No move.

Second 'B' → same. Still position 0.

Third 'B' → same. Still 0.

Fourth 'R' → current stone is R (s[0] is R). Move to 1.

Fifth 'R' → current stone is s[1] (R). Move to 2.

Final position is 2 (0-based) → 3. Which matches the sample.

So the code works for that.

Third sample's code would process all steps and compute the correct position.

Thus, the code is correct. The constraints are small, so no need for optimization. The code is O(m) where m is the length of t, which is up to 50 steps. So it's efficient enough.

So the code is as follows.
</think>

```python
s = input().strip()
t = input().strip()
pos = 0  # 0-based index
for c in t:
    if pos < len(s) and s[pos] == c:
        pos += 1
print(pos + 1)
```