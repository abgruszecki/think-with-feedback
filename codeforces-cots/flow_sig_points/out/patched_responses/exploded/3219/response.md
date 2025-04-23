<think>
Okay, let's see. We need to find the minimum number of operations to make the cockroach colors alternate. The operations allowed are either swapping any two cockroaches or repainting a single cockroach. Hmm, wait, but swapping two cockroaches takes one operation, and repainting also one. So the question is, which combination of swaps and repaints gives the least steps.

Wait, but wait. Swapping might allow us to fix two positions at once. For example, if two cockroaches are in the wrong positions, swapping them would fix both in one move. However, considering that the problem allows any swaps, maybe the optimal approach is to first consider the color arrangement and then figure out the minimal steps needed.

But perhaps there's a smarter way. Let's think about the possible target patterns. The sequence must alternate, so there are two possible valid patterns:

1. Starts with 'r' and alternates (r, b, r, b, ...)
2. Starts with 'b' and alternates (b, r, b, r, ...)

So the minimal steps would be the minimum between the steps needed to convert the string into each of these two patterns, and then take the lower of the two.

But how do we compute the steps for each pattern?

Let's think for each target pattern. For example, for the first pattern (starting with 'r'):

Each even index (0-based) should be 'r', and each odd index should be 'b'. Wait, no. Wait, the first character is position 0 (if 0-based), then even positions (0, 2, 4, ...) are 'r', and odd positions (1,3,5,...) are 'b'.

So for each position in the string, we check what the expected color is for the two possible patterns, and see how many changes are needed if we repaint.

But swapping could allow us to rearrange the cockroaches. But wait, since swapping can permute the cockroaches any way we like, perhaps it's optimal to arrange them in the target pattern with the minimal number of repaints, and then use swaps to arrange them, but the problem is that each swap is a separate operation.

Wait, no. Because swapping two cockroaches can correct two positions in one move. For example, if we have a 'b' in position 0 and 'r' in position 1, swapping them would fix both in one move. So perhaps it's better to count the number of positions where the current character doesn't match the target pattern, and then see how many of those can be fixed by swaps (each swap fixing two mismatches), and the rest by repaints.

But how to model this. Let's think: when you have a target pattern, you can count the number of positions where the current color is wrong. Let's call these "mismatches". For each of these mismatches, the color needs to be changed, either via a repaint (1 operation) or via a swap with another cockroach (if possible).

Wait, but swapping two cockroaches can fix two mismatches if they are in positions that are each other's target. For example, if in the target pattern, position i should be 'r' and position j should be 'b', but the current characters are 'b' and 'r' respectively. Swapping them would fix both in one move.

So for each target pattern, the minimal number of operations would be:

number of mismatches - number of such pairs (each pair reduces the count by 2, but takes 1 swap) + the remaining mismatches that need to be repainted.

Wait, but how to compute this. Let's say for a target pattern, there are R mismatches. The maximum number of swap pairs possible is the number of mismatched 'r's and 'b's. For example, if in the target, there are x positions where the current is 'b' but should be 'r', and y positions where the current is 'r' but should be 'b'. Then the number of possible swaps is the minimum of x and y. Each swap handles two mismatches (one from each category). So the total operations would be (the number of swaps) (each swap takes 1 operation) plus the remaining mismatches after swaps (each requires a repaint, 1 per operation). So the total would be (swaps) + (remaining) = min(x,y) + (x + y - 2*min(x,y)) ) → which is max(x,y). Because min(x,y) + (x + y - 2*min(x,y)) = x + y - min(x,y) = max(x,y). Wait, no. Let's compute:

min(x,y) is the number of swaps possible.

Each swap reduces x and y by 1. So after swapping, the remaining x' is x - swaps, y' is y - swaps. The remaining x' + y' is (x + y) - 2*swaps. Then the remaining can be handled by repainting, which is x' + y' operations. So total operations is swaps + (x + y - 2*swaps) = x + y - swaps.

But swaps is min(x, y). So total is x + y - min(x, y) = max(x, y).

Wait, that's interesting. So for a target pattern, the minimal number of operations required would be the maximum between x and y. Because each swap reduces both x and y by 1. So for example, if x is 5 and y is 3, then we can do 3 swaps (handling 3*2=6 mismatches), and then 5-3=2 x's left, which are 2 repaints. So 3 + 2 =5, which is max(5,3). So yes, in that case the total is max(x, y).

But wait, this is only if we can swap any two cockroaches. So perhaps for each target pattern, the minimal steps is the maximum of the two counts (number of 'r's needed and 'b's needed in the wrong positions). But how do we get these x and y?

Alternatively, perhaps for each target pattern, the number of 'r's that are in even positions (for the first pattern) plus the 'b's in odd positions would need to be considered. Wait, let's think again.

For example, for the first pattern (starts with 'r'):

Each even index (0, 2, 4, ...) must be 'r', and each odd index must be 'b'.

So for the current string, count the number of positions where:

- Even index but 'b' (needs to be 'r') → x1
- Odd index but 'r' (needs to be 'b') → y1

Then x1 is the number of 'b's in even positions, and y1 is the number of 'r's in odd positions.

The minimal steps for this pattern would be the maximum of x1 and y1.

Similarly, for the second pattern (starts with 'b'):

Each even index must be 'b', and each odd index must be 'r'.

So count:

x2: number of 'r's in even positions (should be 'b's)
y2: number of 'b's in odd positions (should be 'r's)

Then the steps for this pattern is max(x2, y2).

Then the answer is the minimum between the steps for pattern 1 and pattern 2.

But wait, why is this the case?

Because for each pattern, the number of required swaps is the maximum of x and y. But why?

Because each swap can fix one x and one y. So the number of swaps possible is the minimum of x and y, and then the remaining are repaints. So for example, if x is 3 and y is 5: min is 3 swaps (3 operations), which fixes 3 x's and 3 y's, leaving 2 y's. Then we need 2 repaints, total 3+2=5, which is max(3,5) =5.

Yes. So the minimal steps for each pattern is the maximum between x and y.

So, for each of the two possible patterns, we compute x and y as the counts of mismatched 'b's in even positions and 'r's in odd positions (for pattern starting with 'r'), or 'r's in even and 'b's in odd (for pattern starting with 'b').

Then the minimal steps for each pattern is max(x, y). The overall answer is the minimum between the two patterns.

Wait, but let's test this with the examples.

First example:

Input: 5, rbbrr → the string is r b b r r.

For pattern 1 (r starts):

Even indices (0,2,4) must be 'r'. Let's check:

0: 'r' → ok. 2: 'b' → x1 increases by 1. 4: 'r' → ok.

Odd indices (1,3) must be 'b'. 1 is 'b' → ok. 3 is 'r' → y1 increases by 1.

So x1=1, y1=1 → max is 1. So steps needed for pattern1 is 1.

Pattern2 (b starts):

Even indices (0,2,4) must be 'b'. Check:

0: 'r' → x2 increases by 1. 2: 'b' → ok. 4: 'r' → x2 +=1 → x2=2.

Odd indices (1,3) must be 'r'. 1 is 'b' → y2 increases by1. 3 is 'r' → ok. So y2=1.

max(2,1) is 2.

So overall answer is min(1,2) → 1. Which matches the sample.

Second example:

Input: 5, bbbbb → all 'b's.

Pattern1: even must be 'r', odd must be 'b'.

Even indices (0,2,4) are 'b's → x1=3.

Odd indices (1,3) are 'b's → which is correct. So y1=0.

max(3,0) →3 steps for pattern1.

Pattern2: even must be 'b', odd must be 'r'.

x2 is the number of 'r's in even positions (0,2,4), which are all 'b's → x2=0.

y2 is the number of 'b's in odd positions (1,3), which are 'b's. So y2=2.

max(0,2) →2 steps. So answer is min(3,2) = 2. Which matches the sample.

Third example:

3, rbr → r b r.

Pattern1: even (0,2) must be 'r', which they are. Odd (1) must be 'b' → yes. So x1=0, y1=0 → max 0.

Pattern2: even must be 'b'. 0 is 'r' → x2=1. 2 is 'r' → x2=2. Odd (1) must be 'r', but is 'b' → y2=1. max(2,1) →2. So answer is 0. Correct.

So this approach seems to work.

Therefore, the algorithm is:

Compute for the two possible target patterns the required x and y counts, calculate max(x, y) for each pattern, then take the minimum between the two.

So the steps for the code would be:

1. Read n and the string.

2. For each pattern (starting with 'r' and 'b'):

   a. Count how many even positions are not 'r' (for pattern 1) → x.

   b. Count how many odd positions are not 'b' (for pattern1) → y.

   c. steps1 = max(x, y)

   d. For pattern2, even positions must be 'b' → count the number of even positions that are not 'b' → x.

      Odd positions must be 'r' → count the number of odd positions not 'r' → y.

   e. steps2 = max(x, y)

3. The answer is the minimum between steps1 and steps2.

So the code can be written as:

Read n, s.

Initialize for both patterns:

For pattern1:

x1 = number of even indices where s[i] != 'r'

y1 = number of odd indices where s[i] != 'b'

steps1 = max(x1, y1)

For pattern2:

x2 = number of even indices where s[i] != 'b'

y2 = number of odd indices where s[i] != 'r'

steps2 = max(x2, y2)

ans = min(steps1, steps2)

Print ans.

Yes. This would be O(n) time, which is acceptable for n up to 1e5.

Let's code this.

But how to efficiently compute x1, y1, x2, y2.

We can loop through each character in the string, check if the index is even or odd, and for each position, update the counts accordingly.

For example:

Initialize x1 = 0, y1 = 0, x2=0, y2=0.

For each i in 0..n-1:

   char = s[i]

   if i is even:

      if char != 'r': x1 +=1

      if char != 'b': x2 +=1

   else:

      if char != 'b': y1 +=1

      if char != 'r': y2 +=1

So for each i, we check whether it's even or odd, and update the counts for both patterns in the same loop.

This way, we process each character once, and compute all four variables.

Then compute steps1 = max(x1, y1), steps2 = max(x2, y2), answer is min(steps1, steps2).

Yes. That's O(n) time and O(1) space (since we don't need to store the string if we process it on the fly, but in Python, reading it as a string is acceptable).

Testing this approach with the sample inputs:

Sample 1:

Input: 5, 'rbbrr'

Indices 0: 'r' (even, matches 'r' → x1 no change. x2 checks 'b', not → x2 +=0? Wait:

Wait for pattern1, even indices must be 'r'. So for even i:

if char is not 'r', x1 increases. For 'r' → no.

For pattern2, even indices must be 'b'. So for even i, if char is not 'b', x2 increases.

So for index 0:

char is 'r' → even. For pattern1: ok. x1 remains 0. For pattern2: 'r' != 'b' → x2 +=1.

Index 1: odd. For pattern1: must be 'b'. 'b' → no increment to y1. For pattern2: must be 'r'. 'b' → y2 +=1.

Index 2: even. char is 'b'. For pattern1: 'b' != 'r' → x1 +=1. For pattern2: 'b' is ok → x2 remains 1 (from index 0).

Index3: odd. char is 'r'. For pattern1: must be 'b' → yes, so y1 +=1. For pattern2: must be 'r' → ok → y2 remains 1 (from index1).

Index4: even. char 'r' → x1 remains 1 (since even and 'r'). For pattern2: 'r' != 'b' → x2 +=1 (now x2 is 2).

So for pattern1:

x1=1 (index2), y1=1 (index3). steps1 = max(1,1) →1.

For pattern2:

x2=2 (index0 and 4?), let's see:

Wait, index0 is even, 'r' → x2 +=1.

Index2 is even, 'b' → ok → x2 remains 1 (from index0). Wait, no. For pattern2, even indices must be 'b'. So:

index0: 'r' → x2 +=1.

index2: 'b' → ok. x2 is 1.

index4: 'r' → x2 +=1. So x2 is 2.

So for pattern2:

x2=2, y2=1 (from index1 and 3? Let's check:

y2 is the count of odd indices not 'r'.

index1: 'b' → not 'r' → y2 +=1.

index3: 'r' → ok. So y2 is 1.

So steps2 is max(2,1) →2. So the minimum is 1. Correct.

Yes.

Sample2:

input 5, 'bbbbb'

pattern1:

even indices (0,2,4) must be 'r' → all are 'b's → x1=3.

odd indices (1,3) must be 'b' → all are 'b's → y1=0. steps1=3.

pattern2:

even indices must be 'b' → x2=0.

odd indices must be 'r' → both are 'b's → y2=2. steps2=2. min is 2.

Sample3:

input3, 'rbr'

pattern1:

even indices (0,2) → 'r' and 'r' → x1=0.

odd index (1) → 'b' → y1=0. steps1=0.

pattern2:

even indices must be 'b' → index0: 'r' → x2=1. index2: 'r' → x2=2.

odd index (1) must be 'r' → 'b' → y2=1. steps2=2. min is 0.

So the code seems correct.

Therefore, the code is straightforward.
</think>

```python
n = int(input())
s = input().strip()

x1 = x2 = y1 = y2 = 0
for i in range(n):
    c = s[i]
    if i % 2 == 0:
        if c != 'r':
            x1 += 1
        if c != 'b':
            x2 += 1
    else:
        if c != 'b':
            y1 += 1
        if c != 'r':
            y2 += 1

steps1 = max(x1, y1)
steps2 = max(x2, y2)
print(min(steps1, steps2))
```