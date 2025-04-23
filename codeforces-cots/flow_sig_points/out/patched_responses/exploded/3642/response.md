<think>
Okay, I need to solve this problem where I have to determine if a given triad is major, minor, or strange. Let's see what the problem says.

The notes are C, C#, D, D#, E, F, F#, G, G#, A, B, H. Oh right, and they cycle after H. So the order is important here. The distances between notes are based on their positions in this sequence. Each consecutive pair is 1 semitone apart. So the distance from C to C# is 1 semitone, C to D is 2, etc. But when calculating the distance between two notes, it's the minimal steps when moving upwards. Wait, wait. Wait, the problem says: the distance is taken from the lowest to the highest. So for example, C to E is 4 semitones (C to C# (1), C# to D (2), D to D# (3), D# to E (4)), so that's four steps. But if it's E to C, then the distance would be the other way around the circle. Wait, the problem says that between two consecutive notes there's exactly one semitone. So the notes are arranged in order, each next is +1 semitone. So the distance from X to Y is (Y's position - X's position) mod 12, but only if we go upwards. Wait, no. The problem says: the distance between X and Y is measured as the number of semitones when moving from X to Y upwards. So, for example, the distance from C to E is 4 semitones, because you go up through C#, D, D#, E (4 steps). But if Y is before X in the order, then the distance is (Y + 12 - X) % 12. Wait, perhaps the notes are arranged in a circle, and the distance is the minimal number of steps upward. Wait, the problem says the distance is from the lowest to the uppermost. So for example, E to C is considered. Since the order is cyclic, E to C would require moving past H and then to C. Let's see. The order is C, C#, D, D#, E, F, F#, G, G#, A, B, H, then back to C. So the distance from E to C would be (C comes after H. Let's list their positions:

Let's assign each note a position index starting from 0:

C: 0
C#: 1
D: 2
D#:3
E:4
F:5
F#:6
G:7
G#:8
A:9
B:10
H:11

Then, the distance from X to Y is (Y - X) mod 12, but only when moving upwards. Wait, the problem says that the distance is taken from the lowest to the uppermost. So X is considered lower than Y if it comes before in the sequence. So when calculating the distance between X and Y, if X comes before Y, the distance is Y's position minus X's position. If Y comes before X, then the distance is (12 - (X's position - Y's position)), because you loop around.

Wait, no. The problem says, "the distance is taken from the lowest tone to the uppest one". So the order is determined as the position in the list. So for example, C is lower than E, so the distance is 4. E is higher than C. But H is higher than B (since H is after B), but when you loop, H is followed by C. So the distance from H to C is 1 semitone (H to C is 1 step up). But the distance from C to H is (H's position - C's position) = 11-0=11 semitones. So that's 11 semitones. 

So, to compute the distance between X and Y, we take (Y_pos - X_pos) mod 12. Because if Y is after X, it's (Y-X) steps. If Y is before X, then mod 12 gives the correct number of steps when moving upwards. Wait, mod 12 will handle that. For example, if X is E (4) and Y is C (0), then (0-4) mod 12 is 8. Which is 8 semitones. But according to the problem statement, the distance from E to C is 8 semitones. So yes, the distance from X to Y is (Y - X) mod 12. Because when X is E (4) and Y is C (0), the distance is (0-4) mod12 = 8. So yes, that's correct.

Wait, but in the problem's example, C to E is 4, E to C is 8. So when Y is lower than X, the distance is (Y - X +12) %12. For example, (0-4 +12) mod12 is 8. Which is correct.

So the distance between X and Y is (Y_pos - X_pos) mod 12. Because when Y is after X, the mod is just their difference, but when Y is before X, the mod gives (Y_pos +12 - X_pos) mod12, which is correct.

So first, I need to create a mapping from note names to their positions. Like a dictionary. Then, given three notes, I can get their positions.

Then, the problem says that a major triad is when the three notes can be ordered such that X, Y, Z (after ordering) have distances X to Y =4, Y to Z=3. So X to Y is 4, Y to Z is 3. So the total X to Z is 7. For a major triad.

A minor triad is when X to Y is 3, Y to Z is 4. So total X to Z is 7.

But the order can be any permutation. Because the set is unordered. So for any permutation of the three notes, after sorting, we need to check if any of the possible cyclic permutations of the three elements satisfies either major or minor conditions.

Wait, but the problem says "if we can order the notes so as the distance between X and Y is 4, Y and Z is 3, then it's major." So how to find such an order?

So for the three notes, the idea is to check all possible permutations, but not all permutations. Because the set is unordered, but the ordering for the triad could be any cyclic permutation. Wait, perhaps we can generate all possible cyclic permutations of the three notes and check for each if they form the required distances.

Alternatively, since there are three notes, perhaps the triad can be ordered in a circular way. So for all possible orderings (rotations) of the three notes, check if any of the sequences (A, B, C) have the first two distances as 4 and 3 (for major) or 3 and 4 (for minor). But since the notes form a cycle, perhaps we can arrange them in sorted order and check the possible intervals.

Wait, for example, given three notes, their order in the musical scale can be arranged in a cyclic permutation. So for example, if the notes are X, Y, Z sorted in order as per their positions, then the distances between X and Y, Y and Z, Z and X (wrapping around) could be considered. But for a triad to be major or minor, the three notes must form a sequence where consecutive distances are 4 and 3 (major) or 3 and 4 (minor). So the three notes must form a sequence of three consecutive steps where the sum is 7 semitones, split into 4+3 or 3+4.

Wait, but since the triad is a set of three notes, the problem allows any permutation. So to check whether any permutation of the three can form such a sequence. For example, let's take the three notes, and check all possible orderings. But since the order is cyclic, perhaps there's a smarter way.

Alternatively, consider all possible orderings (rotations) of the three notes. For example, for three notes A, B, C, the possible orderings as sequences in the circle are:

A, B, C (assuming sorted positions)

But the sequence could be B, C, A, or C, A, B. However, since the triad is unordered, perhaps the correct approach is to generate all permutations of the three notes, and for each permutation, check the three possible intervals (distance from first to second, second to third, and third to first). Wait, no. Because the triad is a set of three notes, but the major/minor conditions are based on a specific sequence of two steps (4 and 3, or 3 and 4).

Wait, the problem says: "If we can order the notes so as the distance between X and Y equals 4, and between Y and Z equals 3, then it's major." So the order of the three notes must form a sequence where the first two are 4 apart, the next two (Y to Z) are 3 apart. So the triad is major if any cyclic permutation of the three notes arranged in the right order satisfies this.

But how to check that.

Let's think of the three notes in sorted order. For example, sorted by their positions. Let's say their positions are a, b, c where a <= b <= c (mod 12). Then, the possible distances are:

b - a, c - b, (a +12 -c) mod12 (since after c comes a again). But since a is the smallest, the distance from c to a is 12 - (c - a) semitones.

But for a major triad, we need two consecutive distances that sum to 7 (4+3). So in the sorted order, perhaps the first two distances are 4 and 3. Or the last two and the first. Or the middle and last.

Alternatively, perhaps the correct approach is to generate all possible cyclic permutations of the sorted notes. For example, for the three sorted positions a, b, c, check the sequences (a, b, c), (b, c, a), (c, a, b). For each of these sequences, compute the distances between the first and second, and second and third. If any of these sequences has the first distance 4 and second 3, then major. Similarly for minor.

Wait, but the sorted order may not be the correct order for the triad. For example, if the notes are C, E, G, which are positions 0, 4, 7. The sorted order is 0,4,7. The distance between 0 and4 is 4 (correct), 4 to7 is 3 (correct). So this sequence would satisfy the major condition.

Another example: C#, B, F. The notes are C# (1), B (10), F (5). Their positions are 1,10,5. If sorted, perhaps we need to arrange them in order. Wait, sorted order would be 5 (F), 10 (B), 1 (C#). Because 1 comes after 10? Wait no, the positions are 0 to 11. So 5 is F, 10 is B, 1 is C#. The sorted order would be 1 (C#), 5 (F), 10 (B). Wait, no, 1 is less than 5, which is less than 10. So sorted order is C# (1), F (5), B (10). The distances between them are 5-1=4, 10-5=5. Then, the distance from B to C# is 1-10 +12 = (1-10) mod12 = (1+12-10) =3. So the sequence B, C#, F would have distances 3 and 4 (since B is 10, C# is 1. 1-10 mod12 is (1-10) = -9 mod12 =3, and F is 5, so 5-1=4. So the sequence (B, C#, F) would have distances 3 and4, which is minor. So in this case, the sorted order of the original notes may not give the correct sequence, but a different permutation would.

So the approach is to generate all possible permutations of the three notes and check each possible triplet for the required distances. However, since the order in the triad is a sequence (since the distances are in a specific order), but the set is unordered, perhaps there are 6 possible permutations (all possible orderings of the three notes). For each of these permutations, check if the first to second distance is 4 and second to third is3 (major), or first to second is3 and second to third is4 (minor). But wait, the triad must be ordered such that X, Y, Z form the required distances. So for example, if the three notes are A, B, C in some order, then for each permutation (A,B,C), (A,C,B), etc., check if the first two are 4 apart and next two are3, etc.

But that's 6 permutations, which is manageable. However, perhaps there's a smarter way. Let's think: For a major triad, the three notes must have two intervals of 4 and 3, which sum to 7. The third interval would be 7 (since 4+3=7, but in a cycle of 12, the total sum of all three intervals would be 12). Wait, the sum of the three intervals (assuming the notes are arranged in order) would be 12. Because if you have a, b, c sorted, then (b-a) + (c -b) + (a - c +12) = (b-a + c -b + a -c +12) = 12. So the sum of all three intervals is 12. So for a major triad, two intervals sum to 7, which leaves the third interval as 5. But maybe that's not helpful.

Alternatively, the problem requires that the triad can be ordered in a way that the first two notes are 4 apart, and the next two are 3. So for the three notes, there must exist an ordering where the first two are 4 apart, the next two are3. So for example, the three notes are X, Y, Z. Then, in some permutation, X to Y is4, Y to Z is3. The third interval (Z to X) would be 12 -4-3=5 semitones. So for the triad to be major, the sum of the two required intervals is7, which leaves the third interval as5.

But how to check for any permutation of the three notes whether such a pair exists.

Another approach: For each possible combination of two intervals (4 and3), check if any of the three possible pairs (X-Y, Y-Z), (Y-Z, Z-X), (Z-X, X-Y) in any permutation equals (4,3) or (3,4). Wait, but for each permutation, the order is important.

Alternatively, let's take the three notes as a, b, c. For each possible permutation of these three, check the distances between consecutive elements (mod12) and see if they match the major or minor conditions.

But with three notes, there are 6 possible permutations. For each permutation, we need to check the first two distances (distance between first and second note) and the next two (distance between second and third note). Wait, but the third note to the first note's distance isn't part of the check. Because the condition for major is that there exists an ordering where two consecutive distances are 4 and3. So in the permutation (X, Y, Z), the first two steps (X to Y) is4, and Y to Z is3. Then the triad is major. Similarly, if in permutation (Y, Z, X), the distances Y to Z is4, Z to X is3, then it's also major. But in this case, the sum of those two steps is7, and the third step is5. But the problem only requires that two consecutive steps sum to7 (4+3). So how?

Let me think. For any permutation of the three notes, if in the ordered sequence (X, Y, Z), X to Y is4, Y to Z is3, then it's major. Or, perhaps, in the ordered sequence, the first two steps are 4 and3. But considering that the triad is a set, perhaps the order can be any permutation. So for example, the three notes could be X, Z, Y. Then, the first two steps would be X to Z (7), which doesn't help. But if you arrange them as X, Y, Z, then the steps are correct. So for each permutation of the three notes, check if the first two steps (distance between first and second) is4 and the next (distance between second and third) is3. If any permutation satisfies this, it's major. Similarly for minor.

But this could be time-consuming for three elements. Let's see. For three elements, there are 6 possible permutations. For each permutation, check the first two distances and the next. For example:

notes are a, b, c.

Check permutation (a, b, c):

distance a to b: (b -a) mod12.

distance b to c: (c -b) mod12.

If (a to b) is4 and (b to c) is3 → major.

If (a to b) is3 and (b to c) is4 → minor.

If any permutation meets this condition, then return the respective result.

So how many permutations do we need to check? All 6? Or perhaps some of them can be skipped.

Alternatively, since the order of the three notes can be any permutation, but the triad is a set, perhaps we can generate all possible permutations of the three notes and check the first two steps in each. So for each permutation, the first two steps and the next step.

But for three notes, there are 6 permutations. Let's code that.

So the plan is:

1. Create a dictionary mapping note names to their positions (0 to 11).

2. Read the three input notes and get their positions.

3. Generate all possible permutations of the three positions.

4. For each permutation (x, y, z), compute the distance between x and y (d1), then between y and z (d2). Check if d1 is4 and d2 is3 → major. Else if d1 is3 and d2 is4 → minor.

5. If any permutation satisfies either condition, return the corresponding result. Else, return 'strange'.

But wait, the problem says that the answer is always unambiguous. So there is no case where the triad is both major and minor. So if any permutation meets the major condition, we return 'major'. Similarly for minor. But if none meet either, then 'strange'.

Wait, but in the problem statement, it's possible that some permutations could lead to a major and others to minor. But the problem says that such cases do not exist, so we don't have to handle them. So once any permutation meets the major condition, we can return 'major' immediately. Same for minor. But we need to check all permutations to see if any meet either condition.

So the steps are:

For each permutation of the three notes:

   compute d1 = (y -x) mod12

   compute d2 = (z -y) mod12

   if d1 ==4 and d2 ==3 → it's a major. return 'major'

   if d1 ==3 and d2 ==4 → it's minor. return 'minor'

If after checking all permutations, neither condition is met, return 'strange'.

Yes, that makes sense.

So the code would generate all permutations of the three notes, and for each permutation, check the two distances.

Now, how to generate all permutations. In Python, we can use itertools.permutations. For three elements, there are 6 permutations, which is manageable.

But since the input can be up to three elements, and permutations are 6, it's feasible.

So code outline:

notes = input().split()

note_order = {'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4, 'F':5, 'F#':6, 'G':7, 'G#':8, 'A':9, 'B':10, 'H':11}

positions = [note_order[n] for n in notes]

from itertools import permutations

for perm in permutations(positions):

   x, y, z = perm

   d1 = (y -x) %12

   d2 = (z - y) %12

   if d1 ==4 and d2 ==3:

       print("major")

       exit()

   if d1 ==3 and d2 ==4:

       print("minor")

       exit()

print("strange")

Wait, but for the permutation (x, y, z), we are checking the distances between x and y, and y and z. But in the problem statement, the major triad requires that the two distances are 4 and3. So if in any permutation, the first two steps (x to y) and (y to z) are 4 and3, then it's major. Similarly for minor.

But what about the third step (z to x)? Do we need to check that? The problem says that the triad is three notes, and the condition is that two consecutive steps sum to 7 (4+3 or 3+4). The third step's distance is not part of the condition. So yes, the code as outlined should work.

Let's test the examples.

First example:

Input: C E G

Notes: C (0), E (4), G (7)

Permutations:

One permutation is (0,4,7). Then d1 is 4-0=4, d2=7-4=3. So 4 and3 → major. So code outputs 'major'.

Another permutation could be (4,7,0). Then d1 is7-4=3, d2=0-7 mod12=5. Not matching.

So the code would find the first permutation and return 'major'.

Second example:

Input: C# B F → positions 1,10,5.

Looking for a permutation where d1 is3 and d2 is4.

The permutation (10,1,5) → d1 is (1-10) mod12 = (1-10 is -9 → mod12 is 3). So d1 is3. d2 is5-1=4. So this permutation meets the minor condition. So code would output 'minor'.

Third example:

Input: A B H → positions 9,10,11.

Check all permutations.

For permutation (9,10,11): d1=1, d2=1 → no.

For permutation (9,11,10): d1=2, d2= (10-11) mod12= ( -1 → 11) → 2 and11 → no.

Another permutation (10,9,11): d1=(9-10) mod12=11. d2=11-9=2 → no.

Wait, perhaps all permutations won't meet the conditions. So code returns 'strange'.

So the code works for these examples.

Now, considering the possible notes and their order.

What about a case where the triad is not in sorted order but after permutation meets the condition.

So code should handle that.

Now, in Python, the code would generate all permutations of the three elements, including all possible orderings.

So the code seems correct.

Now, the code uses itertools.permutations. But for three elements, it's 6 permutations. Each iteration is fast.

But what about the same note being present multiple times? But according to the problem statement, the input is three notes, but perhaps duplicates are allowed? Wait, the problem says the input is three space-separated notes. But chords are sets of three notes. Wait, the problem says "unordered set of no less than three notes", but for the problem, it's exactly three. So the input will have three distinct notes. Because a triad is three distinct notes. So in the code, the positions will be three distinct elements, but permutations can have same elements if the input has duplicate notes. But according to the problem statement, the input is three notes, but are they allowed to be the same? The problem statement says "triad is exactly three notes". So perhaps the input can have duplicates, but in that case, the triad would not form a major or minor chord. For example, C C C → impossible to form the required intervals. But the problem says the input is three space-separated notes, but nothing about duplicates. So the code should handle that.

But according to the problem's examples, it's possible that the input has three distinct notes. So the code's logic would work regardless.

Now, the code uses the 'exit()' function to exit as soon as a condition is met. Which is efficient.

So the code is correct.

So the final code would:

- Read the input notes.

- Create the positions.

- Generate all permutations.

- Check each permutation for the two conditions.

Now, implement this in Python.

But note that in Python, importing itertools.permutations is needed, but for code submission, the code should read from stdin and write to stdout, and not have any debug prints.

So the code would look like:

Read the three notes.

Map them to positions.

Generate all permutations.

Check each permutation.

If any permutation meets major or minor condition, output and exit.

Else output strange.

So the code:

But first, the note_order dictionary is needed.

note_order = {'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4, 'F':5, 'F#':6, 'G':7, 'G#':8, 'A':9, 'B':10, 'H':11}

Then, read the input:

notes = input().split()

Then, positions = [note_order[note] for note in notes]

But what if a note is not in the dictionary? According to the problem statement, the input is correct.

So no need for error checking.

Then, generate all permutations.

import itertools

for perm in itertools.permutations(positions):

    x, y, z = perm

    d1 = (y - x) % 12

    d2 = (z - y) % 12

    if d1 ==4 and d2 ==3:

        print("major")

        exit()

    if d1 ==3 and d2 ==4:

        print("minor")

        exit()

print("strange")

Wait, but in Python, the 'exit()' function is exit(), but in code, perhaps we can return after printing. But using exit() after printing will terminate the program immediately.

But in code submission, it's better to break out of the loop once a condition is met.

Alternatively, the code can check all permutations and collect the results, but that's not efficient. However, given that there are only 6 permutations, it's better to check each and exit as soon as a condition is met.

But in code, once a permutation meets a condition, the code prints the result and exits.

Yes.

So the code is correct.

Testing the examples:

First example: prints 'major' correctly.

Second example: in one permutation (B, C#, F) → positions 10,1,5.

d1 is (1-10) mod12 → -9 mod12 is 3. d2 is (5-1)=4. So 3 and4 → minor.

Third example: permutations of 9,10,11. All permutations have d1 and d2 values that don't meet 4 and3 or 3 and4.

So code outputs 'strange'.

Thus, the code should work.
</think>

```python
import itertools

note_order = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'B': 10, 'H': 11}
notes = input().split()
positions = [note_order[note] for note in notes]

for perm in itertools.permutations(positions):
    x, y, z = perm
    d1 = (y - x) % 12
    d2 = (z - y) % 12
    if d1 == 4 and d2 == 3:
        print("major")
        exit()
    elif d1 == 3 and d2 == 4:
        print("minor")
        exit()

print("strange")
```