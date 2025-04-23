<think>
Okay, let's see. The problem is about switches and lamps. So, each switch can turn on certain lamps. When a switch is pressed, any lamp connected to it (ai,j is 1) gets turned on, and stays on. The key here is that pressing multiple switches that affect the same lamp doesn't matter once it's already on. The main question is whether there's a switch that can be removed such that pressing all the others still leaves all lamps on.

Hmm. The input guarantees that pressing all n switches results in all m lamps being on. So for each lamp, there's at least one switch that turns it on. But when we remove one switch, we need to ensure that for every lamp, at least one of the remaining switches has a 1 in that column. Because if any lamp is covered only by the removed switch, then when that switch is excluded, that lamp would remain off.

So the problem reduces to: is there a switch such that for every lamp j, there exists at least one other switch (not the removed one) that has a 1 in column j?

So, how do we check this efficiently?

The straightforward approach would be for each switch i, check for each lamp j whether there's another switch that covers j. If for all j, such a switch exists when i is removed, then i is a candidate. If any such i exists, output YES, else NO.

But the problem is that n and m can be up to 2000. So a naive approach of checking each switch by iterating through all lamps and for each lamp, checking all other switches would be O(n^2 * m), which for 2000^2 * 2000 is 8e9 operations. That's way too slow. So we need a smarter approach.

Let's think of how to precompute for each lamp j, the number of switches that can turn it on. Then, for each switch i, we can check if there's any lamp j where the count (number of switches that turn on j) minus whether switch i was one of those is zero. If for any lamp j, the count is exactly 1 and that switch is i, then removing i would make that lamp not covered, so i can't be the one to remove.

So the steps could be:

1. For each lamp j, compute how many switches can turn it on. Let's call this cnt[j].

2. Then, for each switch i, check if all lamps j are covered by at least one other switch. That is, for every j, cnt[j] - (a[i][j] ? 1 : 0) >= 1.

If there exists a switch i where this is true for all j, then the answer is YES.

But how do we compute cnt[j] efficiently?

Yes. For each j, iterate through all switches and count how many have a 1 in column j.

Then, for each switch i, check for each j: if a[i][j] is 1, then cnt[j] must be >=2 (because after removing i, there's at least one other). If a[i][j] is 0, then cnt[j] must be >=1 (since removing i doesn't affect it, and the original cnt[j] is at least 1, but the problem's condition says that all lamps are on when all switches are pressed).

Wait, the problem says it's guaranteed that pressing all switches turns all lamps on. So for each lamp j, cnt[j] is at least 1. Because the initial all-switches case covers all lamps.

So when we remove switch i, the condition is: for each j, if the lamp j was covered by i (a[i][j] is 1), then there must be at least one other switch that covers j (cnt[j] >= 2). If the lamp j was not covered by i (a[i][j] is 0), then as long as cnt[j] >=1 (which it is), it's okay.

So for a switch i to be removable, for every j where a[i][j] is 1, cnt[j] must be >=2.

So the steps can be:

1. Precompute cnt[j] for each lamp j.

2. For each switch i:

   a. Iterate through all j where a[i][j] is 1.

   b. Check if for all those j, cnt[j] >=2.

   c. If all such j have cnt[j] >=2, then this switch can be removed. Return YES.

If any switch i passes this check, output YES, else NO.

This approach would be O(n*m) time, which for n=2000 and m=2000 is 4e6 operations. That's manageable.

But how do we efficiently iterate through all j where a[i][j] is 1? Because for each switch i, we need to check all the positions where it has a 1, and for those positions, check if cnt[j] is at least 2.

So for each switch, the set of j's where a[i][j] is 1. For each such j, cnt[j] must be >=2.

So the plan is:

Compute cnt[j] for each j. Then, for each switch i, check if all the j where a[i][j] is 1 have cnt[j] >=2.

If there exists a switch where this is true, then output YES.

So how to implement this.

First, we need to read the matrix a. Each row is a string of 0s and 1s. For each column j, count the number of 1s.

Then, for each switch i, collect all the j where a[i][j] is 1, and check if all of their cnt[j] are >=2.

If any switch i satisfies this condition, output YES.

Yes.

Now, how to represent the matrix. Since each row is a string, perhaps for each switch i, we can precompute the list of j's where it has a 1. Then, for each i, iterate over that list and check cnt[j] >=2.

But storing for each i a list of j's could take O(nm) space, which is acceptable (2000*2000 is 4e6 entries). But for m=2000, each list can be up to 2000 elements. So 2000*2000 = 4e6 elements in total. That's manageable.

So the steps:

Read n and m.

Read n rows, each of length m.

Compute cnt[j] for each j (0-based or 1-based? Need to be careful).

For each j in 0..m-1:

   cnt[j] = sum of a[i][j] for all i in 0..n-1.

Then, for each switch i (0..n-1):

   For all j where a[i][j] is 1:

      if cnt[j] < 2 → this i cannot be removed. Break and check next i.

   If all j's in this i's 1s have cnt[j] >=2 → return YES.

If none found, return NO.

So that's the approach.

Now, let's think about the sample inputs.

First sample:

4 5

10101 → row 0: j=0,2,4.

01000 → row 1: j=1.

00111 → row 2: j=2,3,4.

10000 → row3: j=0.

The cnt array:

j=0: rows 0,3 → cnt[0] = 2.

j=1: row1 → cnt[1] =1.

j=2: rows0,2 → cnt[2] =2.

j=3: row2 → cnt[3] =1.

j=4: rows0,2 → cnt[4] =2.

Now, check each switch i.

For i=0: the j's where a[i][j] is 1 are 0,2,4. Check their cnt:

j=0: cnt is 2 → ok.

j=2: cnt 2 → ok.

j=4: cnt 2 → ok.

So for i=0, all required j's have cnt >=2. So this switch can be removed. So answer is YES.

In the first sample, that's why the output is YES.

Second sample:

4 5

10100 → row0: j=0,2.

01000 → row1: j=1.

00110 → row2: j=2,3.

00101 → row3: j=2,4.

cnt array:

j=0: rows0 → cnt 1.

j=1: rows1 → cnt 1.

j=2: rows0,2,3 → cnt 3.

j=3: row2 → cnt1.

j=4: row3 → cnt1.

Now, for each switch i:

Check all j where a[i][j] is 1.

i=0: j=0,2.

cnt[0] is 1. So when i is removed, cnt[j] -1 becomes 0. So this is a problem. So i=0 can't be removed.

i=1: j=1. cnt[j] is 1. So removing i=1 would leave cnt[j] 0. So no.

i=2: j=2,3. For j=2, cnt is 3, so even after removing i=2, cnt is 2. For j=3, cnt is 1. So when i=2 is removed, cnt[j=3] becomes 0. So i=2 can't be removed.

i=3: j=2,4. For j=2, cnt is 3-1=2 (but wait, the original cnt[j=2] is 3. So even after removing i=3, the cnt would be 3-1=2. So that's okay. For j=4, original cnt is 1. So when i=3 is removed, cnt[j=4] becomes 0. So i=3 can't be removed.

Thus, no switch can be removed, so answer is NO.

So the approach works for the sample.

Now, the code.

We need to process the input.

First, read n and m. Then read n lines, each of m characters.

We can represent each row as a list or a string, but for checking which j's are 1, perhaps for each row, precompute a set or a list of the indices where the character is '1'.

Then, compute cnt for each j.

Then, for each row i, iterate through its '1's j's and check if all cnt[j] >=2.

Once any row passes, output YES.

So in Python:

Read n, m.

Then, read n lines. For each line, collect the indices j where the character is '1'.

Store this as a list of lists or sets.

Compute cnt as a list where cnt[j] is the number of switches that have '1' in column j.

Then, for each i in 0..n-1:

   for all j in the '1's of i's row:

      if cnt[j] < 2 → break.

   else → return YES.

If all i checked and none pass, return NO.

In code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    rows = []
    for _ in range(n):
        s = input_stream.readline().rstrip("\n").strip()
        ones = [j for j, c in enumerate(s) if c == '1']
        rows.append(ones)

    cnt = [0] * m
    for i in range(n):
        for j in rows[i]:
            cnt[j] += 1

    for i in range(n):
        valid = True
        for j in rows[i]:
            if cnt[j] < 2:
                valid = False
                break
        if valid:
            print("YES", file=output_stream)
            return

    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 5
10100
01000
00110
00101
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

Second sample:

rows[0] = [0,2]

rows[1] = [1]

rows[2] = [2,3]

rows[3] = [2,4]

cnt[j=0] is 1 (only row0).

cnt[j=1] is 1 (row1).

cnt[j=2] is 3 (rows0,2,3).

cnt[j=3] is 1 (row2).

cnt[j=4] is 1 (row3).

For i=0, ones are 0 and 2.

Check j=0: cnt is 1 <2 → invalid. So i=0 is skipped.

For i=1, j=1: cnt is 1 <2 → invalid.

For i=2, j=2 (cnt 3 >=2), j=3 (cnt 1). So for j=3, cnt is 1, which when i=2 is removed (since the original cnt is 1), then after removal, cnt[j=3] would be 0. So for i=2, j=3's cnt is 1, which is <2. So valid becomes False.

So code correctly skips all i's and outputs NO.

The code seems correct.

Now, considering the constraints. For n and m up to 2000, the code's time and space should be acceptable.

Each row's ones are stored as a list. The cnt array is O(m) space. For each row, processing the ones in O(k) time, where k is the number of 1's in the row. So total O(nm) time for building rows and cnt.

Then, for each i, checking O(k) elements, where k is the number of 1's in the row. So overall O(nm) time.

In Python, this should handle 2000x2000 in under 3 seconds. Let's see.

But in Python, for 2000 rows, each with 2000 elements, the code is manageable.

Another thing to note is that when a switch has no 1's in its row, then removing it doesn't affect anything. Because for all j, a[i][j] is 0, so the check is automatically true. Because for the code, the loop over j in rows[i] would have zero iterations. So valid remains True. So in that case, the code would output YES.

But according to the problem statement, when all switches are pressed, all lamps are on. So for a switch i that has no 1's, then pressing all switches except i would still press all n-1 switches (including i's not being pressed). But since i's row is all 0's, removing it doesn't change anything. So if all the other switches can cover all lamps, then i can be removed. But since in that case, for all j, the other switches must cover the lamps. So the code would correctly return YES.

For example, if there's a switch with all 0's. Then, since the code would process that row as having no j's, the loop over j's would not run, and 'valid' remains True. So that switch can be removed, but the other switches must cover all lamps. Since the problem states that all switches pressed cover all lamps, removing a switch with no 1's would not affect anything. So the code correctly allows that.

So the code is correct.
</think>

```python
n, m = map(int, input().split())
rows = []
for _ in range(n):
    s = input().strip()
    ones = [j for j, c in enumerate(s) if c == '1']
    rows.append(ones)

cnt = [0] * m
for row in rows:
    for j in row:
        cnt[j] += 1

for row in rows:
    valid = True
    for j in row:
        if cnt[j] < 2:
            valid = False
            break
    if valid:
        print("YES")
        exit()

print("NO")
```
