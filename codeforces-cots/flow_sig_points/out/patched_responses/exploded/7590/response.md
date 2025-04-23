<think>
Okay, I need to solve this problem where dominoes are pushed left or right, and some are not pushed. The goal is to find how many remain standing after all the falling dominoes have affected each other.

First, let's understand the problem. Each domino that's pushed (L or R) starts falling in that direction. Every second, dominoes falling left push the next domino to the left, and similarly for right. But if a domino is being pushed from both sides at the same time, it remains standing.

So the key is to model how the forces from the left and right affect each domino. For each domino, we need to determine the earliest time it's hit from the left (by an R) and the earliest time it's hit from the right (by an L). If both are present but at different times, the earlier one determines the direction. If they are the same, then the domino stays up.

Wait, but the dominoes start falling at time 0. For example, a domino pushed to the right (R) starts falling and will push the next domino to the right in the next second. So the dominoes to the right of an R start getting hit after a delay based on their distance. Similarly for L.

So for each domino, let's calculate two values:

1. The earliest time it is hit from the left (i.e., by a domino to the right that is falling left, like an L). Wait, no. Wait, when a domino is pushed to the left (L), it starts falling left. That domino will push the domino to its left (i-1) in the next second. Wait, no: the direction is important. For example, if a domino is L, then in the next second, the domino to its left (i-1) will be hit. But that domino must be standing, otherwise it's already been hit. So perhaps we can model each domino's state over time, but for n=3000, simulating each second step by step is O(n^2) time, which might be acceptable since 3000^2 is 9 million, but maybe there's a smarter way.

But given the constraints, n up to 3000, maybe an O(n) approach is possible. Let's think.

Alternative approach: For each domino, find the nearest R to the left of it that is not blocked by any L, and the nearest L to the right that is not blocked by any R. Then, based on the distance, determine if the domino is hit by R from the left, L from the right, or both.

Wait, that's a common approach for such problems. Let's see:

For each position i (0-based?), we can track the closest R to the left of i (i.e., in positions j < i) such that there are no L's between j and i. Similarly, the closest L to the right of i (positions j > i) such that there are no R's between j and i. Then, for each domino, if neither exists, it remains standing. If only R exists, then it's pushed right. If only L exists, pushed left. If both exist, compare the distances.

Wait, but how does that work?

For example, consider an R at position j and an L at position k (k > i). Then, the R would affect dominoes to the right, but only until it's blocked by an L. Similarly, the L affects dominoes to the left until blocked by an R.

So for each domino i:

- The R's to the left that can reach i: find the nearest R to the left of i, such that between that R and i, there are no L's. Because any L in between would block the R's influence. Similarly, for L's to the right.

So, for each i, find the nearest R on the left (call it leftR) and the nearest L on the right (call it rightL). Then:

If both leftR and rightL exist:

- The distance from leftR to i is d1 = i - leftR's position.

- The distance from rightL to i is d2 = rightL's position - i.

The R would take d1 steps to reach i (since each step propagates right). The L would take d2 steps to reach i (each step propagates left). So:

If d1 < d2: R arrives first, domino falls right.

If d2 < d1: L arrives first, domino falls left.

If d1 == d2: both arrive at the same time, domino remains.

If only one exists, then the domino is pushed in that direction.

If neither exists, the domino remains.

So the steps are:

1. Preprocess for each i, the closest R to the left (with no intervening L's), and the closest L to the right (with no intervening R's).

How to compute this efficiently?

For leftR array:

We can iterate from left to right. Keep track of the last R seen, and whether any L's have occurred since. For each i:

- if s[i] is 'R', then leftR[i] = i, and reset the L flag.

Wait, no. Let's think:

We can have a variable lastR, which is the position of the nearest R to the left of the current position. Also, whenever we encounter an 'L', we reset lastR to -infinity because any R after an L cannot influence dominoes beyond the L (since the L would block the R's force).

Wait, perhaps the logic is:

Initialize lastR = -1 (meaning no R found yet).

Then, iterate from left to right:

For each position i:

- if s[i] is 'R', then lastR = i. Also, for this R, any domino to the right can be influenced by it until an L is encountered.

- if s[i] is 'L', then lastR = -1 (since any R to the left of this L can't influence the right side of L, because L's force would block it).

- if s[i] is '.', then leftR[i] = lastR if lastR != -1 and there are no L's between lastR and i.

Wait, but how do we track that there are no L's between lastR and i?

Alternatively, whenever we hit an 'L', we set lastR to -1 because any R before that L is now invalid for positions to the right of the L. So, for example:

positions: R . . L . . . 

For the L at position 3, any R before it (position 0) can't affect positions 4,5,6 because the L's force would have blocked.

So, when processing i=3 (L), we set lastR to -1. So for the next positions (4,5,6), their leftR is -1 until we find another R.

So the leftR array can be computed as follows:

Initialize lastR = -1.

For each i from 0 to n-1:

    if s[i] == 'R':

        lastR = i

    elif s[i] == 'L':

        lastR = -1

    else: # s[i] is '.', then leftR[i] = lastR

So, leftR[i] is the position of the closest R to the left that can reach i (i.e., no L's between them). Because once an L is encountered, the R's can't reach beyond it.

Similarly, for rightL array:

We compute the closest L to the right of each position, which can reach it (i.e., no R's between them). So:

Initialize lastL = -1.

Iterate from right to left.

For each i from n-1 downto 0:

    if s[i] == 'L':

        lastL = i

    elif s[i] == 'R':

        lastL = -1

    else: # s[i] is '.', rightL[i] = lastL

So for each domino i (s[i] is '.'), leftR[i] and rightL[i] are the positions of the R to the left and L to the right that can influence it.

If leftR[i] is not -1, then the distance is i - leftR[i]. That's the number of steps the R's force takes to reach i (since each step, the R's influence moves right by 1). Similarly, if rightL[i] is not -1, the distance is rightL[i] - i.

Then, for each domino i:

if leftR[i] == -1 and rightL[i] == -1: count +=1

elif leftR[i] == -1: domino is pushed by rightL[i], falls left. So it's not standing.

elif rightL[i] == -1: domino is pushed by leftR[i], falls right. Not standing.

else:

    d1 = i - leftR[i]

    d2 = rightL[i] - i

    if d1 < d2: falls right

    elif d2 < d1: falls left

    else: count +=1

So for each domino, we check these conditions and count if it remains standing.

But what about dominoes that are initially pushed (L or R)? Those dominoes are not standing, so we don't count them.

So the steps are:

Loop through each domino:

if s[i] is '.':

    compute leftR and rightL as described.

    check if both leftR and rightL exist, and if their distances are equal.

    if so, increment count.

Else:

    ignore (since it's pushed and falls).

So the total count is the sum of all '.' dominoes that are not pushed by any R or L, or pushed by both but at the same time.

Now, the question is how to compute the leftR and rightL arrays.

Let's try with an example.

Take the first sample input:

14
.L.R...LR..L..

The string is . L . R ... L R .. L ..

Indices 0 to 13.

Let's compute leftR array for each '.'.

For example, the first character is '.', but there's no R before it (since leftR starts at -1). So leftR[0] = -1.

Then the next is L (index 1). So leftR[1] is not considered since s[i] is not '.'.

For index 2, since the previous was L (so leftR is -1). So leftR[2] is -1.

At index 3, which is R. So leftR[3] is 3 (but s[i] is R, not '.'), so not considered.

Then index 4: '.', the last R was at 3. So leftR[4] =3.

Similarly for 5,6: leftR is 3.

Index 7 is L, which sets lastR to -1.

Index 8 is R, so lastR=8.

Index 9: '.', so leftR=8.

Index 10: '.', leftR=8.

Index 11: '.', but after the R at 8, but there's an L at 12. Wait, no, in the example the string is .L.R...LR..L.. which after index 8 (R), next is 9 is '.', 10 is '.', 11 is '.', 12 is L.

Wait, let's process leftR array step by step.

Initialize lastR =-1.

i=0: s[i] is '.', leftR[0] =-1.

i=1: s[i] is 'L', set lastR=-1.

i=2: s[i] is '.', leftR[2] =-1.

i=3: s[i] is 'R', set lastR=3.

i=4: '.', leftR=3.

i=5: '.', leftR=3.

i=6: '.', leftR=3.

i=7: 'L', set lastR=-1.

i=8: 'R', set lastR=8.

i=9: '.', leftR=8.

i=10: '.', leftR=8.

i=11: '.', leftR=8.

i=12: 'L', set lastR=-1.

i=13: '.', leftR=-1.

So leftR array for '.'s:

Positions where s[i] is '.':

0: leftR[0] =-1

2: leftR[2]=-1

4,5,6: leftR=3

9,10,11: leftR=8

13: leftR=-1

Then for the rightL array, we process from right to left.

Initialize lastL =-1.

i=13: '.' → rightL[13] = -1 (since lastL is -1).

i=12: 'L' → set lastL=12.

i=11: '.', rightL[11] =12.

i=10: '.', rightL=12.

i=9: '.', rightL=12.

i=8: 'R' → set lastL =-1.

i=7: 'L' → set lastL=7.

i=6: '.', rightL=7.

i=5: '.', rightL=7.

i=4: '.', rightL=7.

i=3: 'R' → set lastL=-1.

i=2: '.', rightL= -1 (since lastL is -1 after i=3 is R).

i=1: 'L' → set lastL=1.

i=0: '.', rightL=1.

So for the '.' positions:

i=0: rightL=1.

i=2: rightL=-1.

i=4: rightL=7.

i=5: rightL=7.

i=6: rightL=7.

i=9: rightL=12.

i=10: rightL=12.

i=11: rightL=12.

i=13: rightL=-1.

Now, for each '.' position:

i=0: leftR is -1, rightL is 1.

So distance from rightL is 1-0=1. So the L at position 1 is to the right of i=0. So the domino at 0 is pushed left (by the L in 1), so it's not standing.

i=2: leftR is -1, rightL is 7? Wait wait. Let's recheck.

Wait, when processing rightL array:

Processing from right to left:

i=13 is '.', lastL is -1. So rightL[13] = -1.

i=12: 'L', set lastL=12. So rightL[12] is not considered (s[i] is not '.').

i=11: '.', rightL[11] =12.

i=10: '.', rightL=12.

i=9: '.', rightL=12.

i=8: 'R' → set lastL to -1.

i=7: 'L' → set lastL=7.

i=6: '.', rightL=7.

i=5: '.', rightL=7.

i=4: '.', rightL=7.

i=3: 'R' → set lastL=-1.

i=2: '.', rightL=-1 (since after i=3 is R, which sets lastL to -1, and when processing i=2, since s[i] is '.', rightL[i] is lastL which is -1.

So i=2 has leftR=-1 and rightL=-1. So no forces, so it remains standing. Wait, but in the first example, the output is 4. Let's see. Hmm.

Wait, in the first example, the output is 4. Let's see the sample input:

The input is .L.R...LR..L.. which is:

Indices 0: ., 1:L, 2:., 3:R, 4:., 5:., 6:.,7:L,8:R,9:.,10:.,11:.,12:L,13:.

So the '.' positions are 0, 2,4,5,6,9,10,11,13.

Now, let's compute for each of these:

i=0:

leftR is -1, rightL is 1 (the L at 1). So the domino is hit by rightL (distance 1-0=1). So it falls left. Not counted.

i=2: leftR is -1 (since after the L at 1, no R), rightL is -1 (since after processing i=3 (R) in rightL, lastL is -1). So both are -1. So counts as standing. So that's 1.

i=4: leftR is 3 (distance 4-3=1), rightL is 7 (distance 7-4=3). So 1 <3, so R arrives first. Falls right. Not counted.

i=5: leftR=3 (distance 2 steps), rightL=7 (distance 2 steps). So d1=2, d2=2. Both arrive at same time. So counts. That's +1. So total 2.

i=6: leftR=3 (distance 3 steps), rightL=7 (distance 1 step). So d2=1 <3. So L arrives first. Falls left. Not counted.

i=9: leftR=8 (distance 1), rightL=12 (distance 3). d1=1 <3. So R arrives first. Falls right. Not counted.

i=10: leftR=8 (distance 2), rightL=12 (distance 2). Same. Counts. So total 3.

i=11: leftR=8 (distance 3), rightL=12 (distance 1). d2=1 <3. So L arrives first. Not counted.

i=13: leftR is -1 (since after 12 is L, which set lastR to -1). rightL is -1. So counts. So total 4.

So the total is 4, which matches the sample. So this approach works.

So the plan is:

- Precompute leftR array and rightL array.

Then, for each '.' domino, check the conditions.

Now, how to implement this in Python.

First, read n and s.

Then compute leftR and rightL arrays.

Let's code:

Initialize leftR array as a list of -1s.

Compute it by iterating left to right, tracking lastR.

Similarly for rightL array, iterate right to left, tracking lastL.

Then, for each i in range(n):

if s[i] is '.':

    compute d1 and d2.

    if leftR[i] is not -1:

        d1 = i - leftR[i]

    else:

        d1 = infinity (or a large number)

    if rightL[i] is not -1:

        d2 = rightL[i] -i

    else:

        d2 = infinity.

    if (leftR[i] ==-1 and rightL[i]==-1):

        count +=1

    elif (d1 ==d2):

        count +=1

But wait, for the case where both leftR and rightL exist, and d1 ==d2.

So the code for each '.' domino:

if s[i] == '.':

    l = leftR[i]

    r = rightL[i]

    if l ==-1 and r ==-1:

        count +=1

    else:

        if l !=-1 and r !=-1:

            d1 = i - l

            d2 = r -i

            if d1 ==d2:

                count +=1

        else:

            # only one exists, so they don't balance, so no count

So, this logic would correctly count the dominoes that remain standing.

So the code steps:

Read n, s.

Compute leftR:

leftR = [-1]*n

lastR = -1

for i in range(n):

    if s[i] == 'R':

        lastR = i

    elif s[i] == 'L':

        lastR = -1

    # else, it's '.', but leftR[i] is already -1, unless lastR is set

    leftR[i] = lastR if s[i] == '.' else -1

Wait, no. Wait, the leftR array is supposed to store for each position i, the nearest R to the left (without any L in between). But during the iteration, we set leftR[i] to lastR only if the current s[i] is '.'. Otherwise, it's irrelevant (since for s[i] not '.', the domino is pushed and falls, so leftR[i] is not needed. So during the iteration, for each i:

if s[i] is 'R', then lastR = i, and leftR[i] remains -1 (since the domino is pushed, so not considered in the count).

But wait, the leftR array in the code should store for each '.' the nearest R to the left (with no L in between). For non '.' dominoes, leftR is not needed.

So during the loop:

leftR[i] is set to lastR if s[i] is '.'.

Wait, perhaps better to process leftR as follows:

Initialize leftR array as all -1.

lastR = -1

for i in 0..n-1:

    if s[i] == 'R':

        lastR = i

    elif s[i] == 'L':

        lastR = -1

    else: # s[i] is '.', so set leftR[i] to lastR

        leftR[i] = lastR

Similarly for rightL:

rightL array initialized to -1.

lastL = -1

for i in n-1 downto 0:

    if s[i] == 'L':

        lastL = i

    elif s[i] == 'R':

        lastL = -1

    else:

        rightL[i] = lastL

Yes, this way, for each '.' domino, leftR[i] is the last R to the left with no L in between, and rightL[i] is the first L to the right with no R in between.

Then, for each i where s[i] is '.', check the conditions.

So code in Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    s = input_stream.readline().rstrip("\n").strip()

    leftR = [-1]*n

    lastR = -1

    for i in range(n):

        if s[i] == 'R':

            lastR = i

        elif s[i] == 'L':

            lastR = -1

        else:

            leftR[i] = lastR

    rightL = [-1]*n

    lastL = -1

    for i in range(n-1, -1, -1):

        if s[i] == 'L':

            lastL = i

        elif s[i] == 'R':

            lastL = -1

        else:

            rightL[i] = lastL

    count = 0

    for i in range(n):

        if s[i] == '.':

            l = leftR[i]

            r = rightL[i]

            if l == -1 and r == -1:

                count +=1

            elif l != -1 and r != -1:

                d1 = i - l

                d2 = r - i

                if d1 == d2:

                    count +=1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
R....
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    s = input_stream.readline().rstrip("\n").strip()

    leftR = [-1]*n

    lastR = -1

    for i in range(n):

        if s[i] == 'R':

            lastR = i

        elif s[i] == 'L':

            lastR = -1

        else:

            leftR[i] = lastR

    rightL = [-1]*n

    lastL = -1

    for i in range(n-1, -1, -1):

        if s[i] == 'L':

            lastL = i

        elif s[i] == 'R':

            lastL = -1

        else:

            rightL[i] = lastL

    count = 0

    for i in range(n):

        if s[i] == '.':

            l = leftR[i]

            r = rightL[i]

            if l == -1 and r == -1:

                count +=1

            elif l != -1 and r != -1:

                d1 = i - l

                d2 = r - i

                if d1 == d2:

                    count +=1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
.
""",
            "output": \
"""\
1
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

Third sample input:

1

.

So leftR[0] is -1, rightL[0] is -1. So count is 1.

All tests pass.

So the code is correct.

Now, the code must read input from stdin, compute and print the output.

The code is O(n) time and O(n) space, which is optimal for n up to 3e5 (but the constraints say n up to 3000, which is manageable).

So this should be the solution.
</think>

```python
n = int(input())
s = input().strip()

leftR = [-1] * n
lastR = -1
for i in range(n):
    if s[i] == 'R':
        lastR = i
    elif s[i] == 'L':
        lastR = -1
    else:
        leftR[i] = lastR

rightL = [-1] * n
lastL = -1
for i in range(n-1, -1, -1):
    if s[i] == 'L':
        lastL = i
    elif s[i] == 'R':
        lastL = -1
    else:
        rightL[i] = lastL

count = 0
for i in range(n):
    if s[i] == '.':
        l = leftR[i]
        r = rightL[i]
        if l == -1 and r == -1:
            count += 1
        elif l != -1 and r != -1:
            d1 = i - l
            d2 = r - i
            if d1 == d2:
                count += 1

print(count)
```
