<think>
Okay, let's see. The problem is to determine if all the intervals between successive 1s are equal. So, first, we need to check the positions of the 1s in the input string. Then, calculate the differences between consecutive 1s. All those differences should be the same for it to be considered a system.

So, steps I need to take:

1. Extract all the indices where the character is '1'. Let's call this list ones.
2. If there are less than two 1s, but wait, the problem says there are at least three 1s. Wait, no. Wait, the problem statement says that the input sequence has at least three 1s. Because the constraints say that. Oh right, the problem says "It’s guaranteed that the given record sequence contains at least three 1s." So no need to handle cases with less than three.

So for example, the first sample input is 00111000. The ones are at positions 2,3,4 (0-based?), or maybe 3,4,5 if it's 1-based. Wait, the input is a string of 0s and 1s. Let's think in terms of the indices of the string.

For example, the input "00111000" has 8 characters. The '1's are at positions 2,3,4 (0-based). The differences between consecutive positions are 1 and 1. So the gaps are all 1, which means equal intervals. So output is YES.

Another example: "1001011" which is 7 characters. The '1's are at 0, 3, 5, 6 (0-based). The gaps between them are 3-0=3, 5-3=2, 6-5=1. These are all different, so output NO.

Third example: "1010100" is 7 characters. '1's are at 0,2,4. The gaps are 2-0=2, 4-2=2. So all gaps are 2. So output YES.

So the approach is: collect the indices of 1s, compute the differences between consecutive indices, check if all differences are the same.

But wait, the problem statement says "intervals between successive signals are equal". So, the interval is the difference between the positions of consecutive 1s. So for a list of ones positions like [a, b, c, d], the differences (b-a), (c-b), (d-c) must all be equal.

So for the list of ones positions, if the differences are all the same, output YES, else NO.

So the steps:

1. Read n and the string s.
2. Find all the indices where s[i] is '1'.
3. If there are less than two differences (i.e., two or fewer 1s), but the problem says there's at least three 1s. Wait, no. Wait, the problem says the input has at least three 1s. So the list ones will have at least three elements. So the number of differences will be at least two. For example, three 1s give two differences. All of them must be equal.

Wait, if there are three 1s, two differences. Those two must be equal.

So the algorithm is:

- Collect the list of positions of 1s.
- Compute the differences between consecutive positions.
- Check if all differences are the same. If yes, output YES. Else, NO.

So that's straightforward.

Now, code in Python.

How to implement:

Read n from input, then s.

Then create a list ones by iterating through s and collecting indices where s[i] is '1'.

Then check the differences.

For example:

In code:

ones = [i for i, c in enumerate(s) if c == '1']

Then, compute the gaps:

gaps = [ones[i+1] - ones[i] for i in range(len(ones)-1)]

Then check if all elements in gaps are equal.

If the set of gaps has length 1, then yes.

But wait, when len(gaps) is zero? No, since the input has at least three 1s, len(ones) is at least 3. So len(gaps) is at least 2. For example, three 1s gives two gaps. So the code for checking if all elements are the same would be len(set(gaps)) == 1.

So the code would be:

if len(set(gaps)) == 1:
    print("YES")
else:
    print("NO")

That's it.

But let's test some cases.

Sample 1: ones are positions 2,3,4. gaps are 1 and 1. set is {1}, so YES.

Sample 2: ones are 0,3,5,6. gaps are 3, 2,1. set size 3, so NO.

Sample3: 0,2,4. gaps 2 and 2. set size 1, YES.

Another case: four 1s. Let's say positions 0,2,4,6. Gaps are 2,2,2. So set size 1. YES.

Another case: positions 0,2,4,5. Gaps 2,2,1. So set size 2. Output NO.

Yes, that works.

So the code seems straightforward.

Now, edge cases.

What about n=3 and input '111'? Then ones are [0,1,2]. gaps are 1 and 1. So set size 1: YES.

Another case: 1,3,5,7 (n=8). Gaps all 2: YES.

Another case: 1,3,6. gaps 2 and 3. So output NO.

So code handles these.

So this approach is correct.

Now, code:

Read n. Then s = input().strip()

Then process as above.

So the code:

n = int(input())
s = input().strip()

ones = [i for i, c in enumerate(s) if c == '1']
gaps = [ones[i+1] - ones[i] for i in range(len(ones)-1)]

if len(set(gaps)) == 1:
    print("YES")
else:
    print("NO")

That's simple. But wait, in Python, the input is read as input().strip(), which for the second line is correct.

Yes, because the second line is a sequence of n characters, possibly with leading and trailing 0s. But when we read s, we need to take the entire line. For example, if the input is 3 and 101, then s is '101'.

But the code uses enumerate(s) to get the correct indices.

So the code should work.

Testing the sample inputs.

Sample 1:

8

00111000

s is '00111000'

ones = [2,3,4]

gaps = [1,1]

set is {1}, output YES.

Sample2:

7

1001011

s is '1001011'

ones are positions 0,3,5,6.

gaps 3,2,1 → set size 3. Output NO.

Sample3:

7

1010100

ones are 0,2,4 → gaps 2,2 → set size 1. Output YES.

Yes.

Thus, the code works.

What about the case where the ones are spaced with varying gaps? For example, 0,2,4,6 → all gaps 2. Output YES.

Another example: 0,1,2,3 → gaps 1,1,1. YES.

Another example: 0, 2, 3,4 → gaps 2,1,1. set {1,2} → output NO.

Thus, code handles all cases.

So the code is correct.
</think>

```python
n = int(input())
s = input().strip()

ones = [i for i, c in enumerate(s) if c == '1']
gaps = [ones[i+1] - ones[i] for i in range(len(ones)-1)]

print("YES" if len(set(gaps)) == 1 else "NO")
```