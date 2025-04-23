<think>
Okay, let's tackle this problem. So, the task is to determine which wrestler wins based on their points and some tiebreakers. Let's think about the steps needed here.

First, the problem says that the winner is the one with the most points. If they're equal, then we check the lexicographical order of their sequences. If that's the same, the one who performed the last technique wins.

So the steps are:

1. Calculate the total points for each wrestler.
2. If the totals are different, the higher one wins.
3. If totals are equal, compare their sequences lexicographically.
4. If sequences are identical, check who did the last move.

Let's break down each part.

Calculating the total points is straightforward. Sum all positive a_i for the first wrestler, sum the absolute of negative a_i for the second.

Now, for the lexicographical comparison. The lex order for sequences is defined as per the note. So we need to compare the sequences of points each wrestler earned in the order they performed the techniques. Wait, but the techniques are interleaved. So the sequence for each wrestler is the list of their a_i's in the order they occurred. For example, in the first example:

Input is 1, 2, -3, -4, 3.

The first's sequence is [1,2,3] (the third element is negative, so second wrestler's, but the first's sequence includes only positive numbers in order). Wait no. Wait, the input is a list of techniques. Each technique is either added to first's points (if ai is positive) or second's (if negative). So each ai is part of one wrestler's sequence. So for example, the first wrestler's sequence is all the a_i's where ai is positive, in the order they appear. The second's sequence is the absolute values of the a_i's where ai is negative, in the order they appear.

Wait no. Wait, the problem statement says: If ai is positive, the first wrestler performed a technique awarded ai points. If ai is negative, the second performed a technique awarded (-ai) points. So the sequences of points for each are:

First's sequence: list of all ai where ai is positive, in the order they appear in the input.

Second's sequence: list of (-ai) where ai is negative, in the order they appear in the input.

So the lexicographical comparison is between these two sequences.

So for the first example:

First's sequence is [1,2,3] (since the 5th element is 3). Wait no, wait the input is 1,2,-3,-4,3. So first's sequence is [1,2,3] (from index 0, 1, 4). Second's sequence is [3,4] (from index 2 and 3). Then, their totals are 1+2+3=6, and 3+4=7. Wait, no. Wait the first's sum is 1+2+3=6? The second's sum is 3+4=7. So the second's sum is higher, so he wins. Hence the first example's output is 'second'.

Yes, that's correct. So the sum is the first thing to check.

Now, if sums are equal, then compare the sequences lexicographically. How to do that? Let's think. Lex order for sequences is similar to dictionary order. We compare the elements one by one until they differ. The first sequence where a higher element is found is considered larger. If all elements up to the minimum length are equal, then the longer sequence is considered larger.

So for example, if first's sequence is [3,4], and second's is [3], then first's is longer and first's is lex larger. But if first's is [3], second's is [3,1], then first's is shorter but all elements up to the first are equal. So the second's sequence is longer, so second's is lex larger.

So to compare the two sequences, we need to iterate through both, element by element, and find the first position where they differ. If one sequence is longer and the other is a prefix of it, then the longer one is larger.

So, how do we compare these sequences efficiently, especially given that n can be up to 2e5?

Well, for each sequence, we can generate the list of points in order. But with 2e5 elements, it's manageable. But storing both sequences may take O(n) space, which is acceptable given the memory constraints (256MB). So for each wrestler, store their list of points.

Once we have the lists, compare them lexicographically. But what if one list is a prefix of the other? Then the longer one is considered larger.

Now, the third condition: if the sequences are identical (same elements in order and same length), then the winner is the one who did the last technique. So the last technique in the input. For example, if the last move was by the first wrestler (ai is positive), then first wins. Otherwise, second.

So the steps are:

1. Compute sum1 and sum2. sum1 is sum of all ai where ai>0. sum2 is sum of all -ai where ai<0.

   If sum1 > sum2: first wins.

   If sum2 > sum1: second wins.

   Else:

      Compare the sequences lex order.

      If first's sequence is lex larger: first wins.

      Else if second's is lex larger: second wins.

      Else:

          If the last technique was performed by first (ai in input is positive): first wins.

          Else: second wins.

So now, the main problem is to compute sum1 and sum2, collect the sequences for each, compare lex, and check the last technique.

Now, considering that n can be up to 2e5, we need to process this efficiently.

Storing the sequences for each is O(n) time and space, which is acceptable.

So the plan is:

- Iterate through each ai in the input.

- For each ai:

   if ai is positive, add to sum1, append to first_sequence.

   else, add to sum2, append (abs(ai)) to second_sequence.

   Also, track the last technique: if ai is positive, last_tech is 'first', else 'second'.

Then, compare sum1 and sum2. If unequal, output accordingly.

If sums are equal:

   Compare first_sequence and second_sequence lex.

   If first is lex larger: output 'first'

   else if second is lex larger: output 'second'

   else: output 'first' if last_tech is 'first', else 'second'

Now, comparing the sequences for lex order.

How to compare two lists lexicographically in Python.

The straightforward way is to iterate through the elements pairwise until a difference is found. For sequences of different lengths, the longer one is lex larger only if the shorter is a prefix of the longer.

So for example, list1 is [1,2], list2 is [1,2,3]. Then list2 is longer and list1 is a prefix, so list2 is larger.

So the algorithm for lex comparison:

Compare the two sequences element-wise up to the minimum of the two lengths. If at any position i, the elements differ, the sequence with the higher element at i is larger. If all elements up to min(len) are the same, then the longer sequence is larger.

So in code, perhaps:

def compare_lex(s1, s2):

   min_len = min(len(s1), len(s2))

   for i in range(min_len):

       if s1[i] > s2[i]:

           return 'first'

       elif s1[i] < s2[i]:

           return 'second'

   # All elements up to min_len are equal

   if len(s1) > len(s2):

       return 'first'

   elif len(s2) > len(s1):

       return 'second'

   else:

       return 'equal'

Then, if the result is 'equal', then the sequences are the same, so we check the last technique.

Now, the problem is handling the lex comparison efficiently for large sequences. Since each element can be up to 1e9 in size, but in Python, comparing integers is O(1), so the loop is O(min(len(s1), len(s2))), which in the worst case is O(n). But n is 2e5, which is manageable since 2e5 operations are acceptable in Python for the time constraints (given that 2e5 operations take about 0.2 seconds or so, but the problem allows 2 seconds per test case).

So this approach should be feasible.

Now, handling the data:

For the sequences, we need to collect all the positive a_i in order for the first's sequence, and all the absolute values of the negative a_i in order for the second's sequence.

So for each ai in the input:

If ai > 0: add to first_sequence and sum1 += ai

Else: add abs(ai) to second_sequence and sum2 += abs(ai)

Also, track the last technique.

So, code outline:

n = int(input())

sum1 = 0

sum2 = 0

first_seq = []

second_seq = []

last_tech = ''

for _ in range(n):

    ai = int(input())

    if ai > 0:

        sum1 += ai

        first_seq.append(ai)

        last_tech = 'first'

    else:

        val = -ai

        sum2 += val

        second_seq.append(val)

        last_tech = 'second'

Then, compare sum1 and sum2.

If sum1 != sum2:

    print('first' if sum1 > sum2 else 'second')

else:

    # compare lex order

    # compare the sequences

    # code the compare_lex function as above.

    # in Python, list comparison does exactly this lexicographical comparison.

    # So, in Python, comparing first_seq and second_seq using list's default comparison.

    # For example, first_seq > second_seq is equivalent to the lex order.

    # So, in Python, the lists can be compared directly.

    if first_seq > second_seq:

        print('first')

    elif second_seq > first_seq:

        print('second')

    else:

        # sequences are equal. Check last_tech

        print(last_tech)

Wait, that's a good point. Python's list comparison does exactly the lexicographical check we need.

For example:

[1, 2] > [1, 1] → True.

[1, 2] > [1, 2, 3] → False (since the second is longer and first is a prefix).

So comparing the two lists directly would give the correct lex order.

So, the code can be simplified by comparing first_seq and second_seq using Python's list comparison operators.

So in the case where sum1 == sum2, the code can check:

if first_seq > second_seq:

    print('first')

elif first_seq < second_seq:

    print('second')

else:

    print('first' if last_tech == 'first' else 'second')

Yes. That's a much cleaner approach.

So, that's the plan.

Now, let's test with the sample inputs.

First sample:

Input:

5

1 → first_seq adds 1

2 → adds 2, sum1=3

-3 → second adds 3, sum2=3

-4 → second adds 4, sum2=7

3 → first adds 3, sum1=6.

sum1=6, sum2=7 → sum2 is larger. So output 'second' → which matches the sample.

Second sample:

3

-1 → sum2=1

-2 → sum2=3

3 → sum1=3. sum1 and sum2 are 3 each. Now sequences are:

first_seq is [3], second_seq is [1,2]. Compare [3] and [1,2]. Python's list comparison: [3] > [1,2] → True (since first element 3>1). So first_seq is larger. So output 'first', matches the sample.

Third sample:

2

4 → sum1=4

-4 → sum2=4.

sum1 == sum2. Sequences are [4] vs [4]. They are equal. So check last_tech: the last is -4, which is second's. So output 'second' → matches the sample.

So the code works for the samples.

Now, edge cases.

Case where sum is equal, sequences are same, last tech is first. Then output first.

Another case where sum equal, sequences same, last is second → output second.

Another case where sequences are same length and elements, but one longer. For example, first_seq [1,2], second_seq [1]. Then first_seq is longer and is lex larger.

But according to Python's list comparison, [1,2] > [1] → True.

Yes.

So the code should handle all cases correctly.

Now, considering the constraints. For n=2e5, the code will have to read 2e5 lines. But in Python, using input() in a loop for 2e5 lines can be slow. So for handling large inputs, it's better to read all the data at once.

But how to read the inputs efficiently?

The standard way to handle this is to read from sys.stdin for faster input. So, using sys.stdin.read() and splitting into lines.

So, the code can be optimized for speed by reading all the input at once.

But the code should read n, then read n lines.

In Python, the code:

import sys

n = int(sys.stdin.readline())

sum1 = 0

sum2 = 0

first_seq = []

second_seq = []

last_tech = ''

for _ in range(n):

    ai = int(sys.stdin.readline())

    if ai >0:

        sum1 += ai

        first_seq.append(ai)

        last_tech = 'first'

    else:

        val = -ai

        sum2 += val

        second_seq.append(val)

        last_tech = 'second'

Then proceed.

But even with 2e5 lines, using sys.stdin.readline() in a loop can be slow. Because each call to sys.stdin.readline() for 2e5 lines is O(n), but in practice, for Python, this can take up some time.

Alternative approach: read all data at once.

data = sys.stdin.read().split()

But then, the first element is n, followed by n elements.

But the code would be:

import sys

data = sys.stdin.read().split()

n = int(data[0])

sum1 = 0

sum2 = 0

first_seq = []

second_seq = []

last_tech = ''

for ai in data[1:1+n]:

    ai = int(ai)

    if ai >0:

        sum1 += ai

        first_seq.append(ai)

        last_tech = 'first'

    else:

        val = -ai

        sum2 += val

        second_seq.append(val)

        last_tech = 'second'

But this would read all the data in one go, which is faster. Especially for large n. Because reading via sys.stdin.read() is a single system call, which is more efficient.

So this is the optimized way.

Now, considering that for n=2e5, the list first_seq and second_seq can have up to 2e5 elements each. But in Python, appending to a list is O(1) amortized, so that's acceptable.

Memory-wise, each list can take up O(n) space. For 2e5 elements, each being an integer (which in Python is about 28 bytes per int), 2e5 * 28 bytes is 5.6 million bytes, which is about 5MB per list, which is acceptable.

So the code should work within memory constraints.

Thus, the code is optimized for speed by reading the input in one go, and for memory by using lists.

Now, the code in Python would look like this:

Read the entire data, split into tokens.

Process each ai.

Compare the sums, then the sequences, then the last tech.

So the code:

import sys

def main():

    data = sys.stdin.read().split()

    n = int(data[0])

    sum1 = 0

    sum2 = 0

    first_seq = []

    second_seq = []

    last_tech = ''

    for num in data[1:n+1]:

        ai = int(num)

        if ai > 0:

            sum1 += ai

            first_seq.append(ai)

            last_tech = 'first'

        else:

            val = -ai

            sum2 += val

            second_seq.append(val)

            last_tech = 'second'

    if sum1 > sum2:

        print("first")

    elif sum2 > sum1:

        print("second")

    else:

        if first_seq > second_seq:

            print("first")

        elif first_seq < second_seq:

            print("second")

        else:

            print("first" if last_tech == 'first' else "second")

if __name__ == "__main__":

    main()

This should handle all cases efficiently.

Testing the sample inputs:

First sample input:

5

1

2

-3

-4

3 → data is ['5', '1', '2', '-3', '-4', '3']

sum1 is 1+2+3=6, sum2 is 3+4=7. sum2>sum1 → output 'second'.

Second sample:

3

-1

-2

3 → data is ['3', '-1', '-2', '3']

sum1 is 3, sum2 is 1+2=3. sequences are [3] vs [1,2]. [3] is compared to [1,2]. First element 3>1 → first_seq is larger. So output 'first'.

Third sample:

2

4

-4 → sum1=4, sum2=4. sequences [4] and [4] are equal. last_tech is 'second' → output 'second'.

So the code works.

Edge case where sum is equal, sequences are same, but last_tech is first. For example:

n=1, ai=5 → sum1=5, sum2=0. sum1>sum2 → first wins. But if sum1=5 and sum2=5 (like n=2, 5 and -5), then sequences are [5] and [5]. last_tech is 'second' → output 'second'.

Another case: n=3, 1, -1, 1. sum1=2, sum2=1. So sum1>sum2 → first wins.

Another case where sequences are same length but differ in one element. For example, first_seq [2,3], second_seq [2,1]. Then first_seq is larger.

Thus, the code should handle all cases correctly.
</think>

```python
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sum1 = 0
    sum2 = 0
    first_seq = []
    second_seq = []
    last_tech = ''
    
    for num in data[1:n+1]:
        ai = int(num)
        if ai > 0:
            sum1 += ai
            first_seq.append(ai)
            last_tech = 'first'
        else:
            val = -ai
            sum2 += val
            second_seq.append(val)
            last_tech = 'second'
    
    if sum1 > sum2:
        print("first")
    elif sum2 > sum1:
        print("second")
    else:
        if first_seq > second_seq:
            print("first")
        elif first_seq < second_seq:
            print("second")
        else:
            print("first" if last_tech == 'first' else "second")

if __name__ == "__main__":
    main()
```