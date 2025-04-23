<think>
Okay, let's tackle this problem. Hmm. The problem is about the Mancala game. So, the goal is to find the maximum score Resli can get after making one move. 

Let me read the problem again. So, each hole has some stones. When you choose a hole with stones, you take all of them and redistribute them one by one in the next holes counter-clockwise. Then, after redistributing, collect all even-numbered stones from all holes. The sum is the score. We need to find the maximum possible score after any single move.

The input gives 14 numbers, each a_i can be 0 or odd, and there's at least one stone. So the initial state is such that all holes have even numbers of stones? No, wait the problem says each a_i is either zero or odd. So initially, all non-zero a_i are odd. That's part of the input constraints.

So the approach is to simulate each possible move (each hole that has non-zero stones) and calculate the resulting score, then pick the maximum.

But since each a_i can be up to 1e9, we can't simulate each step naively by iterating each stone. That's way too slow. For example, if a hole has 1e9 stones, we can't loop 1e9 times. We need a mathematical way to compute the distribution of the stones.

So, the challenge is to efficiently compute, for each possible starting hole (i), the redistribution of s stones (where s is a_i, but since after taking all, the original hole becomes zero), and then compute how the stones are added to the next holes.

Let's think about how the stones are distributed. For a given hole i (1-based?), the next holes are i+1, i+2, ..., then wrap around after 14. The total stones s is the original a_i. So after taking all stones from hole i, the original hole is set to zero, then we distribute s stones, one per hole, starting from i+1.

Wait, but the problem statement says: when a player makes a move, he chooses a hole which contains a positive number of stones. He takes all the stones inside it and then redistributes these stones one by one in the next holes in a counter-clockwise direction. So the hole from which stones are taken is emptied first, then the redistribution starts from the next hole.

So for example, if the hole is 1 (assuming 1-based index), the next holes are 2,3,4,...14,1,2 etc. But since the original hole (hole 1) is emptied, the first stone is placed in hole 2, then 3, etc.

So for each possible starting hole i (from 0 to 13, if 0-based, but the problem uses 1-based in the input), if a_i is zero, we skip it. Otherwise, we take s = a_i stones, set the hole i to zero, then distribute s stones, each adding one to the next holes in order.

The key is to compute how many full cycles around the 14 holes the stones make, and how many are left after that.

So, for s stones, the number of full cycles is s // 14. Each hole (except the original hole i) will get s //14 stones added. Then, the remaining stones (s % 14) are distributed one by one in the next holes.

Wait, but wait: since we start distributing from the next hole, the initial holes after i will get s//14 plus 1 if they are in the first (s % 14) positions. But the original hole i is not part of the distribution. Because the stones are taken from i, and then placed in the next holes. So the original hole i is skipped.

Wait, but when you distribute the stones, after taking all from i, you start putting stones in i+1, i+2, etc. So the original hole i is not part of the distribution. So during the distribution, the stones are placed in holes (i+1), (i+2), ..., 14, 1, 2, etc. So in the code, when dealing with indices, perhaps we need to handle the 14 as a circular list.

So, for each possible move i (0-based indices for easier handling?), here's the plan:

1. Check if a[i] is zero. If yes, skip. Otherwise, s = a[i].

2. Create a copy of the array, and set copy[i] = 0.

3. Then, distribute s stones into the next holes. So the starting point is (i+1) % 14. Then, for each of the s stones, we increment the next hole each time.

But s can be up to 1e9. So iterating each stone is O(s), which is impossible. So we need a mathematical approach.

Each stone is placed in the next hole, so the total number of stones is s. The first stone goes to (i+1) mod 14, then (i+2) mod 14, etc., until s stones are placed.

So, the number of full cycles is s // 14. Each hole (except the original i) will get s//14 stones. Then, the remaining stones are s %14. These will be placed in the next (i+1), (i+2), ..., up to (i + remaining) mod 14.

But wait, the original hole i is not part of the distribution. So during the distribution, the original hole is skipped. Wait, no. The original hole is emptied and then the next stones start from i+1. So the original hole i is not part of the redistribution. So during the distribution, the holes after i are filled, but the original hole is set to zero and not touched again. So when distributing s stones, none of them go back into the original hole i.

So when distributing, the sequence of holes is i+1, i+2, ..., 14, 1, 2, ... etc., but not i.

So for each move starting at i (0-based), the next hole is (i+1) mod 14. Wait, but 14 is the total number of holes. So for example, if i is 13 (the 14th hole, 0-based?), then next is (13+1) mod 14 = 0. So that's correct.

So, to compute the distribution:

- total stones to distribute: s = a[i]

- the first hole is (i +1) mod 14

We can compute how many full cycles there are. Each cycle adds 1 to each of the 14 holes (since there are 14 holes in total). But wait, no. Because each cycle is placing 14 stones: one in each of the 14 holes. So s = cycles *14 + remainder. So each of the 14 holes (including the original hole i?) No, because the original hole i is not part of the distribution.

Wait, no. When you distribute s stones, each stone is placed in the next hole. So after the first 14 stones, you'd have placed one in each of the 14 holes, except the original hole i. Wait, no. Let's see: the original hole i is excluded from the distribution. Because after taking all stones from i, you start placing stones in i+1. So the distribution sequence includes all holes except the original i. So the total number of holes in the loop is 13? No, no. Wait, no. The distribution sequence includes all 14 holes, but the original hole i is part of the sequence. Wait, no. Let's take an example. Suppose i is 0 (the first hole). After taking all stones, you start placing stones in 1, 2, 3, ..., 13, 0, 1, 2, etc. Wait, but i is 0. So after the first 14 stones, you have placed one in each hole from 1 to 13, then 0 (the original hole). Then again 1, etc.

Wait, this is conflicting. So the original hole i is part of the distribution path. Oh, right. Because when you start at i+1, you distribute in all subsequent holes, including the original hole i. For example, if i is 0, you start at 1, 2, ..., 13, 0, 1, etc. So the original hole i is part of the path. Wait, but the problem statement says that after taking the stones from i, the redistribution starts from the next hole. So the original hole is emptied, and then the next stones are placed starting from i+1. So in the example where i is 0, after taking stones, the redistribution starts at 1, then 2, ..., up to 13, then 0 (hole 0?), then 1 again. So hole 0 (original) is part of the redistribution path. So, when you have s stones, you distribute them in the next holes, which includes the original hole. But the original hole is set to zero, but can be filled again by the redistribution.

So the key is that the original hole i is not skipped in the redistribution. For example, if you take stones from i=0, and have 14 stones to distribute, you place one in each hole from 1 to 13 (holes 1-13), then one in 0 (hole 0). Then you've placed all 14 stones. So in this case, the original hole i=0 will get 1 stone. So, after that, when you collect even-numbered stones, the original hole could be even.

So when we compute the distribution for each move, the original hole can receive stones again.

So, the steps for a move:

- Make a copy of the array.

- Take s = original[i] stones. Set copy[i] = 0.

- Now, distribute s stones into the next holes, starting from (i+1) mod 14. Each stone is placed in the next hole in sequence. So, for each stone, you increment the current position, wrap around after 14.

But how to compute the distribution efficiently?

Each stone is placed in a position. The positions are (i+1), (i+2), ..., (i+1 + s-1) mod 14.

But for s up to 1e9, we can't loop through each stone. So we need a mathematical approach.

Let's model the distribution as follows:

- The first position is (i+1) mod 14.

- The distribution proceeds in a sequence of positions, each one after the previous, wrapping around as necessary.

- The total number of stones is s.

So, each of the 14 positions (including the original i's position) can receive some stones.

The number of times each position is filled is equal to the number of times it is hit during the s steps.

But how to compute this for each position?

Alternatively, note that the stones are distributed in a circular manner, starting at (i+1) mod 14. So, the first stone is at (i+1) mod 14, the second at (i+2) mod 14, ..., the k-th stone at (i+1 + k-1) mod 14.

So, the positions are (i+1 + k) mod 14 for k from 0 to s-1.

We can model the distribution as:

full_cycles = s // 14

remainder = s % 14

So, each position will receive full_cycles stones. Then, the first 'remainder' positions (starting from (i+1) mod 14) will receive an additional 1 stone each.

Wait, that's a way to compute it. Because for each full cycle (14 stones), each position (all 14) gets exactly one stone. Then, the remaining 'remainder' stones are placed in the next 'remainder' positions, each getting one more.

So for all positions, the total added is full_cycles. And the positions from (i+1) mod 14 to (i+1 + remainder -1) mod 14 get an additional 1.

So, in code:

start = (i + 1) % 14

for each position in 0..13:

    added = full_cycles

    # compute if this position is in the first 'remainder' positions after start

    # the remainder positions are start, start+1, ..., start + remainder -1 (mod 14)

    # but how to check if position is in that range.

Alternatively, the positions that receive the extra stones are:

positions (start + k) % 14 for k in 0..remainder-1.

So for each position j in 0..13:

    if (j - start) mod 14 < remainder:

        added += 1

So, the total added to j is full_cycles + 1 if j is among the first remainder positions starting from start.

So, the steps are:

1. For each move i (0-based), if original[i] == 0, skip.

2. Create a copy of the original array, set copy[i] to 0.

3. s = original[i]

4. Compute full_cycles = s //14, remainder = s %14.

5. start = (i +1) %14.

6. For each j in 0..13:

    copy[j] += full_cycles

    if (j - start) %14 < remainder:

        copy[j] +=1

7. Now, after distributing, collect all even-numbered stones in the copy array. Sum them up.

8. The maximum of all possible such sums is the answer.

Wait, but what about the original hole i? After step 2, copy[i] is 0. Then, during the distribution, is copy[i] being added to? Because start could be i's position. For example, if i is 13 (0-based?), then start is (13+1) mod14 = 0. So if remainder is 14, but wait, remainder can be up to 13. So in any case, during the distribution, the original hole i is included in the distribution. So after setting copy[i] to 0, the code adds full_cycles to each j (including i) and possibly 1 if in the remainder positions. So the original hole i could get stones added to it.

But that's correct, as per the problem statement. The original hole is emptied, then the stones are distributed, which may include adding stones back to it.

So the steps are correct.

Once the copy array is built, we need to compute the sum of all even numbers in the array.

So, the approach is:

- For each possible i (0-13) where a[i] > 0:

   - compute the new array after taking all stones from i and redistributing.

   - compute the sum of even numbers in this new array.

- The maximum sum across all these possibilities is the answer.

Now, considering that each a[i] can be up to 1e9, but the code for each i is O(14) operations, this approach is feasible, as there are 14 possible i's, each processed in O(14) time, so total O(14*14) = 196 operations, which is very fast.

So, the code can be structured as follows:

Read the 14 numbers into a list.

Initialize max_score to 0.

For each i in 0 to 13:

   if a[i] == 0: continue

   s = a[i]

   # create a copy of a, but set the i-th element to 0

   new_a = a.copy()

   new_a[i] = 0

   full_cycles = s //14

   remainder = s %14

   start = (i +1) %14

   for j in range(14):

       new_a[j] += full_cycles

   # add the remainder stones

   for k in range(remainder):

       pos = (start +k) %14

       new_a[pos] +=1

   # compute the sum of even stones in new_a

   current = sum(x for x in new_a if x %2 ==0)

   if current > max_score:

       max_score = current

Return max_score

Wait, but wait: creating a copy of the array each time is possible, but in Python, since lists are mutable, for each i, we can create a new list by adding a[i] to the new array.

But the initial array is given. For each move i, the new array is the original array, but the i-th element is set to zero, and then s stones are distributed.

But the original array is not modified. So for each i, the new array is:

original array, set the i-th position to zero, then add full_cycles to all elements, then add 1 to remainder elements starting from (i+1) mod14.

Alternatively, for each i, we can compute the new array as follows:

new_a = [x for x in original array]

new_a[i] = 0

s = original[i]

full_cycles = s //14

remainder = s %14

start = (i+1) %14

for j in 0..13:

   new_a[j] += full_cycles

   if j is in the next remainder positions after start:

       new_a[j] +=1

But in code, how to check if j is in the next remainder positions starting from start?

Well, the positions are (start +k) mod14 for k in 0..remainder-1. So for each j, we can compute (j - start) mod14. If this value is less than remainder, then add 1.

But in code:

for j in range(14):

   delta = (j - start) %14

   if delta < remainder:

       new_a[j] +=1

This way, we don't have to loop through remainder times. This is O(14) per i, which is acceptable.

So in code:

original = list of input numbers

max_score = 0

for i in range(14):

   if original[i] ==0:

       continue

   s = original[i]

   new_a = original.copy()  # wait no: the original array is modified for each i. Wait no, because original.copy() creates a copy. Wait, but original is the initial array. For each i, the new array is original array with i-th set to zero, then add the distributed stones.

Wait, no. Wait, original is the input array. For each i, the starting point is original array, then:

new_a is a copy of original, but with new_a[i] =0. Then, add full_cycles to all positions, then add 1 to the positions covered by remainder.

But original is the input array, which is not modified. So for each i, the new_a is created as:

new_a = [x for x in original]

new_a[i] = 0

Then, add full_cycles to all new_a elements, then add 1 to the ones in the remainder positions.

Wait, but in that approach, we are adding full_cycles to all 14 elements. But the original array already had some values. So after setting new_a[i] to zero, adding full_cycles to all elements, including new_a[i], which was set to zero. So new_a[i] becomes zero + full_cycles. Then, if the remainder includes the position i, add 1.

But that's correct, because during the distribution, the original hole i is part of the distribution. So the code is correct.

Wait, but when we take the stones from i, we set new_a[i] to zero, then add full_cycles to all positions (including i). So the i's position now has full_cycles stones, plus maybe 1 if in the remainder.

But in the original approach, when you take all stones from i, you set it to zero. Then, during the distribution, you add full_cycles to all 14 positions (including i), then add 1 to the remainder positions (which may include i). So the code is correct.

Yes. For example, in the first sample input:

0 1 1 0 0 0 0 0 0 7 0 0 0 0

In 0-based indices, the 10th element (index 9) is 7. So when i=9:

s=7

full_cycles = 0 (7//14=0), remainder=7.

start = (9+1) mod14 = 10.

remainder is 7, so positions 10,11,12,13,0,1,2.

So new_a after setting i=9 to 0:

[0,1,1,0,0,0,0,0,0,0,0,0,0,0]

Then add full_cycles (0) to all positions. So no change.

Then add 1 to positions 10,11,12,13,0,1,2.

So:

pos 10: 0+1=1

pos 11: 0+1=1

pos12:0+1=1

pos13:0+1=1

pos0:0+1=1

pos1:1+1=2

pos2:1+1=2

others remain.

So new_a becomes:

[1, 2, 2, 0, 0, 0, 0, 0, 0,0,1,1,1,1]

Wait, but original a[0] was 0, so after adding 1, it's 1.

But after setting new_a[9] to zero, the new array is [0,1,1,0,0,0,0,0,0,0,0,0,0,0]. Then, adding 1 to positions 10,11,12,13,0,1,2:

After adding 1 to each:

pos0:0+1=1

pos1:1+1=2

pos2:1+1=2

pos10:0+1=1

pos11:0+1=1

pos12:0+1=1

pos13:0+1=1

So the new array is:

[1,2,2,0,0,0,0,0,0,0,1,1,1,1]

Then sum the even numbers: 2 (pos1) +2 (pos2) =4, which matches the sample.

So the code works.

So the code needs to process each possible i, compute the new array, then compute the sum of even numbers.

Now, handling the input. The input is 14 integers. So in Python, we can read them as a list.

So, the code structure is:

Read the input line as a list of integers.

Initialize max_score to 0.

Loop over each i from 0 to 13:

   if original[i] ==0: skip.

   s = original[i]

   create new_a as a copy of original.

   new_a[i] = 0

   full_cycles = s //14

   remainder = s %14

   start = (i +1) %14

   # add full_cycles to all positions

   for j in range(14):

       new_a[j] += full_cycles

   # add remainder stones

   # for j in 0..13, check if (j - start) mod14 < remainder

   for j in range(14):

       delta = (j - start) %14

       if delta < remainder:

           new_a[j] +=1

   # compute sum of even stones

   current = sum(x for x in new_a if x %2 ==0)

   if current > max_score:

       max_score = current

After processing all i, print max_score.

But wait, in Python, the list copy. If we do new_a = original.copy(), but original is a list. So yes.

Wait, but in Python, for a list, .copy() is a method. So original.copy() creates a shallow copy. So for a list of integers, that's correct.

So the code should work.

But let's test with the first sample input.

Sample Input 1:

0 1 1 0 0 0 0 0 0 7 0 0 0 0

Original list in 0-based indices:

[0,1,1,0,0,0,0,0,0,7,0,0,0,0]

For i=9 (the 7), s=7.

new_a is original.copy(), then new_a[9] =0.

So new_a is:

[0,1,1,0,0,0,0,0,0,0,0,0,0,0]

Then full_cycles =7//14=0, remainder=7.

start =9+1=10 mod14 is 10.

Then add full_cycles (0) to all positions: no change.

Then for each j in 0..13, delta = (j -10) mod14.

If delta <7, add 1.

For j=0:

delta = (0-10) mod14 = ( -10 ) mod14 = 4? Because 14*1=14, -10 +14=4.

So delta=4 <7: yes. So new_a[0] +=1 → becomes 1.

For j=1:

delta = (1-10) mod14 = ( -9 ) mod14 =5 → 5 <7: yes. So new_a[1] becomes 1+1=2.

j=2: (2-10) mod14= ( -8 ) mod14=6 →6 <7: yes. new_a[2] becomes 1+1=2.

j=3: (3-10) mod14= -7 mod14=7 →7 is not <7. So no.

j=4: (4-10) mod14= -6 →8 mod14=8 >=7 → no.

Similarly, j=10: (10-10)=0 <7 → yes. So new_a[10] +=1 →0+1=1.

j=11: delta=1 <7 → +1 →1.

j=12: delta=2 <7 →1.

j=13: delta=3 <7 →1.

Then j=0,1,2,10,11,12,13 →7 positions.

So the sum of even numbers is 2 (j=1) + 2 (j=2) →4.

Which is correct.

Another sample input:

5 1 1 1 1 0 0 0 0 0 0 0 0 0 → which is 5 in position 0 (0-based).

s=5.

full_cycles =5//14=0, remainder=5.

start =0+1=1.

The remainder is 5, so positions 1,2,3,4,5.

So new_a is original.copy(), set new_a[0] to 0.

Then, add 0 full_cycles.

Add 1 to positions 1,2,3,4,5.

Original a[0] was 5, set to 0. Then:

After adding 1 to positions 1,2,3,4,5:

new_a[1] (original 1) →1+1=2.

new_a[2] (original 1) →2.

new_a[3] →1+1=2.

new_a[4] →1+1=2.

new_a[5] →0+1=1.

The new array is:

0,2,2,2,2,1,0,0,0,0,0,0,0,0.

Sum of even numbers: 2+2+2+2 +0+0+0+0+0+0+0+0 →8. Which matches the sample.

So the code works.

Now, code implementation:

In Python, the code would read the input as a list of integers.

Then loop through each possible i (0-13), check if a[i] is non-zero.

For each i, create a new array, process as above.

Now, in Python, to create a copy of the list, we can use new_a = a.copy() if a is a list. But in Python, lists have a copy method if they are of the same type. Alternatively, new_a = list(a), or new_a = a[:].

So, for example:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    original = list(map(int, input_stream.readline().rstrip("\n").split()))

    max_score =0

    for i in range(14):

       if original[i] ==0:

           continue

       s = original[i]

       new_a = original.copy()

       new_a[i] =0

       full_cycles = s //14

       remainder = s %14

       start = (i+1) %14

       # add full_cycles to all positions

       for j in range(14):

           new_a[j] += full_cycles

       # add remainder stones

       for j in range(14):

           delta = (j - start) %14

           if delta < remainder:

               new_a[j] +=1

       # sum even

       current =0

       for num in new_a:

           if num %2 ==0:

               current +=num

       if current > max_score:

           max_score = current

    print(max_score, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 1 1 1 1 0 0 0 0 0 0 0 0 0
""",
            "output": \
"""\
8
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

Sample 2:

Input:

5 1 1 1 1 0 0 0 0 0 0 0 0 0

Processing i=0 (original a[0] is5):

new_a[0] is 0.

s=5. full_cycles=0, remainder=5.

start=1.

Then, for j in 0-13:

add 0.

Then, for j:

delta = (j-1) mod14 <5?

For j=1: 0 <5 → yes. j=2:1 <5, j=3:2, j=4:3, j=5:4 → all <5. j=6:5 →5 is not less than 5. So positions 1-5 get +1.

So new_a[1] becomes 1+1=2, etc. Sum even numbers is 2+2+2+2 =8.

So code works.

Now, edge cases. For example, a hole i has s=0. But the input ensures that a_i is either 0 or odd. So in the code, for a[i] ==0, the code skips.

Another edge case: when s is exactly divisible by 14. For example, s=14. Then full_cycles=1, remainder=0. So all positions get full_cycles (1), and no remainder. So each position j is added 1, including i. So after new_a[i] is set to 0, then add 1. So new_a[i] is 1, which is even. So sum would include it if even.

Wait, for example:

Original a[i] is 14. So when you take all 14 stones, set new_a[i] to 0.

Then, full_cycles=14//14=1, remainder=0.

So for each j in new_a, new_a[j] +=1 (because full_cycles is 1). So new_a[i] is 0 +1 =1 (odd). So when you sum even numbers, it's 0.

Wait, but all other positions j (original a[j] +1) may be even or odd, depending on their original values.

So the code correctly processes such cases.

Another example: if the original a[i] is 1e9. Then full_cycles=1e9//14, which is 71428571 (since 14*71428571= 999999994, remainder 6). So adding 71428571 to each of the 14 holes (including i's position, which is zero plus 71428571), then remainder 6 stones added starting from (i+1).

But the code handles that efficiently.

Thus, the code should be correct.
</think>

```python
original = list(map(int, input().split()))
max_score = 0

for i in range(14):
    if original[i] == 0:
        continue
    s = original[i]
    new_a = original.copy()
    new_a[i] = 0
    full_cycles, remainder = divmod(s, 14)
    start = (i + 1) % 14
    
    for j in range(14):
        new_a[j] += full_cycles
    
    for j in range(14):
        delta = (j - start) % 14
        if delta < remainder:
            new_a[j] += 1
    
    current = sum(num for num in new_a if num % 2 == 0)
    if current > max_score:
        max_score = current

print(max_score)
```
