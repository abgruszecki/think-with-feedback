<think>
Okay, let's see. I need to find the number of pairs (l, r) such that within the substring s[l..r], there exists at least one triplet x, x+k, x+2k where all three characters are the same. Hmm.

First, the problem is to count all intervals [l, r] that contain at least one valid triplet. But how do I approach this efficiently, especially since the string can be up to 3e5 characters long?

The naive approach would be to check every possible l and r, but that's O(n^2) for n=3e5, which is 9e10 operations. That's way too slow. So we need a smarter way.

Wait, maybe instead of counting the valid intervals directly, we can find all possible intervals that are invalid (i.e., they don't contain any such triplet) and subtract their count from the total number of possible intervals. The total number of intervals is n*(n+1)/2, right? So if we can find the number of intervals that are 'bad' (no triplet), then the answer is total - bad.

That's a common inclusion-exclusion approach. So the problem reduces to finding the number of intervals [l, r] that do NOT contain any triplet x, x+k, x+2k where s[x] = s[x+k] = s[x+2k].

So how do we compute the number of bad intervals?

First, we need to find all possible triplets in the original string. Then, any interval [l, r] that includes at least one triplet is considered good. The bad intervals are those that do not include any triplet.

But finding all triplets and then checking which intervals avoid them seems difficult. Alternatively, perhaps the maximum possible bad intervals are those that are free of any triplets. So the idea is to find all maximal intervals where no triplet exists, and then compute the number of sub-intervals within them.

But how do we find these intervals?

Alternatively, the minimal forbidden structure is a triplet. So a string is bad (doesn't contain any triplet) if none of its substrings contain a triplet. So our task is to find all intervals [l, r] where the substring s[l..r] has no triplets.

So the problem becomes: count all intervals that are free of any triplet of the form x, x+k, x+2k with equal characters.

But how do we model this?

First, let's consider that a triplet occurs when three equally spaced characters are the same. For example, in the first example, the string is 010101. The possible triplets would be x=1, k=2 (positions 1,3,5: 0,0,0?), but in the first example's note, the answer is 3. Wait, the first example's input is 010101. Let's see: positions 1,3,5 are 0,0,0. So any interval that includes these positions would be considered good. But according to the first example's output, there are 3 such intervals. Wait, the total possible intervals for a string of length 6 is 6*7/2 = 21. The output is 3, so there are 21-3=18 bad intervals? But the first example's output is 3, which is the count of good intervals. Because the note says that there are three pairs (like [1,6], etc.) that do contain such a triplet. So the approach of subtracting the bad from total would work here.

So the key is to find all intervals that have no triplets and compute their count, then subtract from the total.

Now, the problem is to find the number of intervals that do not contain any triplet.

So how to find these intervals?

An important observation here is that in a string without any triplets, certain patterns must be followed. Let's think about the possible triplets. For a triplet to exist, there must be three consecutive elements in an arithmetic progression of step k, all equal. For example, for k=1, the triplet would be x, x+1, x+2. But in that case, the three consecutive characters must be the same. But the problem allows any k, not just k=1. So even if the string has three elements spaced by larger k, like x, x+3, x+6 (k=3), then that's a triplet as well.

But checking for all possible k's for all x's is O(n^2), which is not feasible for n=3e5.

So what's the minimal possible k for a triplet to exist?

Hmm. Let's think: For a triplet to exist, the three positions x, x+k, x+2k must all be within the string. So x+2k <= n. So k can be up to (n - x)/2. But for large n, that's still O(n^2) possible triplets. So iterating through all possible x and k is impossible.

But perhaps, the key insight here is that in a string that has no triplets, it must be such that for any possible x and k, the three elements x, x+k, x+2k are not all equal. How can we model that?

Alternatively, maybe such a string can't be too long. If the string is longer than a certain length, it must contain a triplet. So the maximum possible length of a 'bad' interval (one with no triplets) is bounded. Then, for each position, we can find the earliest x where a triplet starts in some interval, and then calculate the possible intervals that can be formed before that.

But what's the maximum possible length of a bad interval?

This seems like a problem related to the Erdos theorem in combinatorics, where avoiding arithmetic progressions limits the maximum length. However, I'm not familiar with the exact numbers here.

Alternatively, perhaps for a binary string to avoid any triplet, it can't be longer than some small number, like 8 or 9. Then, for each position, we can check all possible substrings of length up to that maximum and count those that are bad.

Wait, this would be a key insight. Let's suppose that any string longer than 8 characters must contain such a triplet. Then, the maximum possible length of a bad interval is 8, and for each starting position, we can check up to the next 8 characters to see if any triplet exists. If not, then the interval is bad, but only if it's of length <=8.

But how to verify this?

Let's think of possible binary strings that avoid any triplet. For example, the example input 11001100 has length 8 and output 0. So that string has no triplet. So the maximum possible length of a bad string is at least 8. But can there be a string of length 9 that has no triplet?

Let's see. Let's take the example input 11001100. Let's add a 0 to the end. So the string is 110011000. Now check for triplets.

Check x=1, k=1: positions 1,2,3: 1,1,0. Not all same.

x=1, k=2: positions 1,3,5: 1,0,1. No.

x=1, k=3: 1,4,7: 1,0,0. No.

x=2, k=1: 2,3,4: 1,0,0. No.

x=3, k=2: 3,5,7: 0,1,0.

But wait, perhaps there's a triplet in this longer string. Let's check:

For x=4, k=2: positions 4,6,8: 0,1,0. No.

But maybe another k. Let's see. What about x=7, k=1: 7,8,9: 0,0,0. Oh! Here's a triplet. So adding a 0 to the end of the example input creates a triplet. So the new string (length 9) must have a triplet. So the maximum possible bad string length is 8.

So perhaps any string of length >=9 must contain a triplet. Therefore, the maximum possible length of a bad interval is 8. So the problem reduces to, for each position in the original string, check all possible substrings starting at that position and of length up to 8. For each such substring, check if it's a bad interval (contains no triplet). Then, sum the number of such bad intervals.

If that's the case, then the algorithm is manageable.

So the steps would be:

1. Precompute all possible triplets (x, x+k, x+2k) in the original string.

But no, since checking all possible triplets for all possible intervals is O(n^3), which is not feasible. But if the maximum length of a bad interval is 8, then for each interval longer than 8, it's automatically a good interval. So the bad intervals can only be of length up to 8.

So the approach is:

- For all possible intervals [l, r] of length up to 8, check if they contain a triplet. If not, count them as bad intervals.

Then, the answer is total intervals (n*(n+1)/2) minus the number of bad intervals.

This is feasible because for each l, we check up to 8 possible r's (from l to l+7), giving O(n*8) operations, which is acceptable for n=3e5.

So, the steps are:

- Compute the total number of possible intervals: total = n*(n+1)//2.

- Compute the number of bad intervals, which are intervals of length up to 8 that do not contain any triplet.

- Subtract the bad count from the total to get the answer.

Now, how to check for each interval [l, r] (1-based) of length up to 8 whether it contains any triplet.

For a given interval [l, r], to check if there exists x, k such that x >= l, x+2k <= r, and s[x] == s[x+k] == s[x+2k].

So for each interval, we can check all possible x and k in that interval.

But since the interval is at most 8 characters long, the possible x and k values are limited.

For example, for an interval of length m (m <=8), the possible k can be up to (m-1)/2. For each possible x in l to r-2k, and k >=1.

So for each interval [l, r], which has length m = r - l + 1, we can loop through all possible k from 1 to (m-1)//2, and for each k, check all x in [l, r-2k], and see if s[x-1] == s[x-1 +k] == s[x-1 +2k] (since Python is 0-based).

But even better, for each interval of length m (from 1 to 8), we can generate all possible triplets (x, x+k, x+2k) that could fit in that interval, and check if any of them have equal values.

For example, for a length 3 interval, k can be 1. So check x= l, x+1, x+2.

For a length 4 interval, k can be 1 and 2.

For k=1: check x=l, l+1.

For k=2: x can be l, since x+2*2 = x+4, but the interval is length 4, so x+2k must be <= r. So x can be l if 4 <=4. So x=l, k=2: positions l, l+2, l+4. Wait, but the interval is [l, r], which is length 4 (so r = l+3). So x+2k <= r. So x+2k <= l+3. For k=2, x+4 <= l+3 → x <= l-1, which is impossible. So for length 4, k=2 is possible only if x + 2*2 <= r. So for example, if the interval is l=1, r=4 (positions 1,2,3,4), then x can be 1 and k=1: 1,2,3. Or k=1 and x=2: 2,3,4. For k=2, x can be 1: 1+2*2=5, which is beyond r=4. So for k=2 in a 4-length interval, no possible x.

So perhaps for each possible interval [l, r], we can check all possible triplets (x, x+k, x+2k) where x >= l, x+2k <= r, and k >=1.

But for intervals up to 8 in length, the number of possible triplets is manageable.

For example, for a length 8 interval:

Possible k can be up to (8-1)/2 = 3.5 → k up to 3.

For each k from 1 to 3:

- For k=1: x can range from l to r-2 (since x+2k = x+2 ≤ r → x ≤ r-2).

- For k=2: x must be ≤ r-4.

- For k=3: x must be ≤ r-6.

So for each interval, the number of possible triplets is:

k=1: (r - l +1 -2) → (m-2) possible x's.

But for m up to 8, this is manageable.

So for each interval [l, r] of length m (1 ≤ m ≤8), we can loop through all possible k and x in that interval and check if any triplet exists.

If none, then this interval is a bad interval and contributes to the bad count.

Otherwise, it's a good interval.

So the plan is:

- Precompute all possible intervals of length up to 8 in the input string.

- For each such interval, check if it contains any triplet (x, x+k, x+2k) with all three characters equal.

- If not, count it as a bad interval.

- The answer is total intervals (n*(n+1)/2) minus the number of bad intervals.

So the steps for the code are:

1. Read the input string.

2. Compute the total number of intervals: total = len(s) * (len(s)+1) // 2.

3. For each possible l in 0-based indices (0 to n-1), check for all possible r from l to min(l+7, n-1). So for each l, check intervals of length 1 to up to 8.

4. For each interval [l, r], check if there exists a triplet within this interval.

5. If no triplet is found, increment the bad count.

6. The answer is total - bad_count.

Now, the key part is efficiently checking if an interval [l, r] (0-based in Python) contains any triplet.

So for the code, for a given l and r (0-based, inclusive), how to check for any triplet.

Let's loop through all possible k in 1 to (r-l+1-1)//2 (since x+2k <= r → k <= (r - x)/2. For x >= l, the minimal x is l. So k can be up to (r - l) // 2. Because x+2k <= r → k <= (r - x)/2. Since x >= l, the maximum possible k is (r - l) // 2.

So for each possible k from 1 to (r - l) // 2:

Then, for each x from l to r - 2k (since x+2k <= r → x <= r - 2k), check if s[x] == s[x +k] == s[x + 2k].

If any such triplet is found, the interval is not bad, so we can break and move to the next interval.

Otherwise, if none are found, then the interval is bad.

But since the interval length is up to 8, the maximum possible k is up to 3 (for length 8). For k=3, x can be l, x+2k = l+6 → which must be <= r. For example, if l=0 and r=7 (length 8), then x can be 0, 1, 2.

But for k=3, x+2k = x +6. So x can be l (0) → 0+6=6 <=7. So yes.

So for k in 1 to 3.

So for each interval [l, r], loop over all possible k from 1 to (r-l)//2, and for each k, loop x from l to r-2k, and check the triplet.

But even this can be optimized. For example, for k=1, in an interval of length 3 (r-l+1=3), x can be l, l+0, and l+1 (since x+2k = x+2 <= r → x <= r-2 → l <= x <= r-2). So for length 3, x can be l and l+0 (if r-l >=2).

Wait, perhaps it's easier to code this as follows:

For each interval l to r (inclusive, 0-based):

for k in 1 to (r - l) // 2:

    for x in l to (r - 2*k):

        if s[x] == s[x + k] == s[x + 2*k]:

            return True (the interval is good)

return False (interval is bad)

But for code, we can loop k from 1 to (r - l) // 2, and x from l to (r - 2*k).

But for small intervals, this is manageable.

Let's code this.

Now, for example, in the first example input, '010101' (0-based indices 0-5):

The bad intervals would be all intervals except the three good ones mentioned. So for the code to compute the bad_count, it should compute 6*7/2 -3 = 21-3=18, which would be the bad_count. So the code should count 18 bad intervals. Then, the answer is 3.

But according to the note, the first example's output is 3. So if the code works, the code would return 3.

Now, let's think about the second example input: '11001100', which has length 8, and the output is 0. So all possible intervals are bad. Wait, but according to the note, there are no triplets in the entire string. So the code would check each interval of length up to 8. But since the entire string is 8 characters, and there are no triplets, then all intervals are considered. But wait, the total intervals for 8-length string is 8*9/2=36. So the code would compute bad_count=36, so the answer is 36 -36=0. Which matches the example.

But wait, in that example, the entire string is 8 characters. So the code checks all intervals up to length 8. But the entire string (length 8) is checked. If there are no triplets in it, then it's considered a bad interval. So the bad_count includes all 36 possible intervals, leading to the answer 36 -36=0.

So the code's approach works for these examples.

Now, the code steps:

Read the string.

Compute total = n*(n+1)//2.

Initialize bad_count to 0.

Loop over each l in 0 to n-1:

   for r in l to min(l+7, n-1):

       check if the interval [l, r] contains any triplet.

       if not, increment bad_count.

Finally, the answer is total - bad_count.

So the code for checking the triplet in an interval is crucial.

Implementing this in Python.

But for a string of length 3e5, and per l up to 3e5, and per r up to l+7 (so 8 steps per l), the total loops would be 3e5 *8=2.4e6 steps, which is manageable.

But in each step, for checking the interval, the code may take up to O(m^2) steps, where m is up to 8. For m=8, the maximum possible k is 3, and for each k, the x ranges could be up to (r - l - 2k +1) → for k=1, x can be l to r-2: r-l is 7 (for a length 8 interval), so r-2 - l +1 = 7-2 =5 → 5 steps. For k=2, x can be l to (r-4), which is l+3 steps. For k=3, x can be l to (r-6), which is l+0 steps if r-l >=6.

But for m=8, the maximum number of steps for all k and x is:

k=1: possible x from l to r-2 → (r-l-1) steps. For m=8, r-l=7 → 7-2 =5 → 5 steps.

k=2: x can be up to r-4 → r-l=7 → 7-4=3 → x can be l, l+1, l+2, l+3 (since l to l+3 is 4 numbers). Wait, r=l+7. So x can be from l to (l+7) -4 = l+3. So x can be l, l+1, l+2, l+3 → 4 steps.

k=3: x can be up to (l+7)-6 = l+1. So x can be l and l+1 → 2 steps.

k=4: (r - l) //2 = (7)//2=3. So k can be up to 3. So no k=4.

So total steps for m=8: 5+4+2=11 steps per interval.

For 2.4e6 intervals, that's 2.4e6 *11= 26.4e6 operations, which is acceptable.

So the code can handle this.

Now, coding this in Python:

First, read the string s.

n = len(s)

total = n*(n+1) //2

bad_count = 0

for l in range(n):

    for r in range(l, min(l+7, n-1)):

        # wait, wait. r should go up to l+7 (inclusive?), but the interval [l, r] has length r-l+1. So for max length 8, r can be up to l+7, since (l+7 - l +1) =8.

        # But in Python, for range(l, end), end is exclusive. So to include r = l+7, we need min(l+7, n-1). So:

        max_r = min(l+7, n-1)

        for r_curr in range(l, max_r +1):

            # Check interval [l, r_curr]

            is_bad = True

            # Check all possible triplets in this interval

            m = r_curr - l +1

            max_k = (m -1) //2

            for k in range(1, max_k +1):

                # x can be from l to r_curr - 2*k

                max_x = r_curr - 2*k

                if l > max_x:

                    continue

                for x in range(l, max_x +1):

                    if s[x] == s[x +k] == s[x + 2*k]:

                        is_bad = False

                        # break all loops

                        break

                if not is_bad:

                    break

            if is_bad:

                bad_count +=1

So this code would loop over all l and possible r_curr (up to 8 steps per l), and for each, check all possible k and x.

But in Python, breaking out of nested loops can be tricky. So once a triplet is found in the interval, we mark is_bad as False and break out of the loops.

Alternatively, for each interval, we can check all possible k and x in the interval and see if any triplet exists.

Now, code optimization: once a triplet is found in the interval, we can break early.

But the code seems manageable.

Let's test this code with the first example input '010101' (length 6).

The code would check for all intervals of length up to 8. For each l in 0-5:

For l=0:

r can be from 0 to min(0+7,5) → 0 to5. So all r from 0 to5. But wait, wait, the code loops r_curr in range(l, max_r +1). So l=0, max_r = min(0+7,5) =5. So range(0,5+1) → 0,1,2,3,4,5. So for each r_curr in 0-5 (6 steps).

Then, for each of these intervals [0,0], [0,1], ..., [0,5], check if there's a triplet.

But the first example's output is 3 good intervals, which are [0,5], [1,5], [0,4] (assuming 0-based). Wait, the note says 1-based:

In the first example, the good intervals are:

1-6 (the entire string), 2-6 (positions 2-6, 0-based is 1-5?), and 1-5 (0-based 0-4).

Wait, the note says:

"In the first example, there are three l, r pairs we need to count: 1,6; 2,6; and 1,5."

So the intervals are:

1-based: (1,6) → 0-based (0,5).

(2,6) → 1-based (2,6) → 0-based (1,5).

(1,5) → 0-based (0,4).

So these three intervals contain a triplet. The code must count all other intervals as bad. The total intervals for n=6 is 6*7/2=21. So the answer is 3, which implies that the bad_count is 18. So the code's bad_count must be 18.

So in the code, the code checks for each interval up to length 8. Since the entire string is 6 characters, but the code checks all intervals of length up to 8 (which would be for l=0, r=5 → length 6, l=0, r=5+7=5 (since n-1=5), so no problem.

Let's take the interval [0,5] (0-based). Check if there's a triplet.

k can be up to (5-0 +1 -1)/2 = (5)/2 → 2. So k=1 and 2.

For k=1:

x ranges from 0 to 5-2*1=3.

Check x=0: s[0] = '0', s[1] = '1', s[2] = '0' → not equal.

x=1: s[1]=1, s[2]=0, s[3]=1 → no.

x=2: 0,1,0 → no.

x=3:1,0,1 → no.

k=2:

max x =5-4=1.

x=0: s[0], s[2], s[4] → 0,0,0 → equal. So triplet found. So the interval [0,5] is not bad. So it's a good interval, not counted in bad_count.

Thus, for this interval, is_bad is False. So it's not added to bad_count.

Similarly, for interval [1,5], which is the 0-based version of 2-6 (since 1-based to 0-based is -1). So l=1, r=5. Check all possible triplets.

k can be up to (5-1+1-1)/2 = (4)/2=2. So k=1 and 2.

k=1: x from 1 to 5-2=3.

x=1: s[1] is 1, s[2] 0, s[3]1 → no.

x=2:0,1,0 → no.

x=3:1,0,1 → no.

k=2: x can be up to 5-4=1.

x=1: s[1], s[3], s[5] → 1,1,1 → all equal. So triplet found. So this interval is not bad.

So in code, it's not counted in bad_count.

Similarly for the interval [0,4] (0-based, which is 1-based 1-5):

Check for k=1 and 2.

k=1: x ranges 0 to 4-2=2.

x=0: 0,1,0 → no.

x=1:1,0,1 → no.

x=2:0,1,0 → no.

k=2: x up to 4-4=0.

x=0: s[0], s[2], s[4] → 0,0,0 → yes. So triplet found.

So the interval [0,4] is not bad.

Thus, the code will not count these three intervals as bad. All other intervals (21-3=18) are bad.

So bad_count=18, and the answer is 21-18=3, which is correct.

Now, code must handle this correctly.

Now, for the second example input, '11001100' (n=8), the code checks all possible intervals up to length 8.

Each interval of length up to 8 must be checked. But since the entire string has no triplets, all intervals are bad. So bad_count is 8*9/2=36, so answer is 0.

So code must return 0 for this case.

Thus, the code should work.

Now, the code in Python.

But the code can be optimized further. For example, in the innermost loop, once a triplet is found, break all loops for that interval.

In Python, the code can use flags and break loops with 'break' statements.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = len(s)

    total = n * (n + 1) // 2

    bad = 0

    for l in range(n):
        # For each l, check all r from l to min(l+7, n-1)
        max_r = min(l + 7, n - 1)
        for r in range(l, max_r + 1):
            has_triple = False
            # Check all possible k and x in [l, r]
            length = r - l + 1
            max_k = (length - 1) // 2
            for k in range(1, max_k + 1):
                # x can be from l to r - 2*k
                start_x = l
                end_x = r - 2 * k
                if start_x > end_x:
                    continue
                for x in range(start_x, end_x + 1):
                    if s[x] == s[x + k] == s[x + 2 * k]:
                        has_triple = True
                        break
                if has_triple:
                    break
            if not has_triple:
                bad += 1

    print(total - bad, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
11001100
""",
            "output": \
"""\
0
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

</think>

```python
s = input().strip()
n = len(s)
total = n * (n + 1) // 2
bad = 0

for l in range(n):
    max_r = min(l + 7, n - 1)
    for r in range(l, max_r + 1):
        has_triple = False
        max_k = (r - l) // 2
        for k in range(1, max_k + 1):
            end_x = r - 2 * k
            if l > end_x:
                continue
            for x in range(l, end_x + 1):
                if s[x] == s[x + k] == s[x + 2 * k]:
                    has_triple = True
                    break
            if has_triple:
                break
        if not has_triple:
            bad += 1

print(total - bad)
```
