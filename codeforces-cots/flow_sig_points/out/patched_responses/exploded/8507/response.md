<think>
Okay, let's tackle this problem. Hmm, the problem is about finding the maximum number of commands the robot could have executed correctly so that it ends up back at (0,0). Oh right, some commands might have been ignored, so we need to choose a subset of the original commands (in order) that results in the robot returning to start, and find the largest possible such subset.

Wait, the robot starts at (0,0) and after executing the subset of commands (without reordering), it must end up at (0,0). So the key is to select a subset of the original sequence (possibly all of them) such that the net movement is zero in both x and y directions, and the subset is as large as possible.

So how to model this? Let's think. For each command, moving in a direction contributes to the total displacement. For the robot to end at (0,0), the sum of all U's minus D's must be zero (so net vertical movement is zero), and similarly for L and R (net horizontal movement is zero).

So, the problem reduces to selecting a subset of the commands where the total U - D equals zero, and total R - L equals zero. And we need to maximize the size of this subset.

But how do we compute this efficiently? Let's consider the maximum possible n is 100. So trying all possible subsets is impossible (2^100 is way too big). So we need a smarter approach.

Let me think. The net movement for x and y must be zero. So perhaps, for each possible number of commands k (starting from n down to 0), check if there exists a subset of k commands that when executed, the robot ends at (0,0). Once we find the largest k where this is possible, return it.

So the approach is to iterate k from n down to 0. For each k, check if there's a way to choose k commands from the original sequence (without reordering) such that the sum of the x and y movements is zero. The maximum k where this is possible is the answer.

But how to check for each k efficiently?

Wait, the robot must execute the commands in order. So the subset is a subsequence of the original commands. But even if we have a subsequence, the order is preserved. So the net movement is the sum of each selected command's effect. So for example, if the original sequence is LDUR, the subset could be all four commands, which sum to L (-1,0) + D (0,-1) + U (0,+1) + R (+1,0). The total is 0 in both x and y. So the answer is 4.

In the second example, RRRUU: the robot ends at (3,2). So even if we select all 5 commands, the sum is (3,2). So the maximum possible is 0. Because there's no subset of even size 0 (but wait, the robot has to execute some commands. Oh wait, the problem allows for zero commands if necessary. Wait no, the problem says 'the maximum possible number of commands that were performed correctly'. So if there's no subset (except possibly zero), then output zero.

Wait, but even zero is allowed. For example, if no commands are selected, the robot is at (0,0), but the output would be zero. So the second example's answer is zero because no subset (including all 5) makes it back to (0,0). So the output is zero.

So the approach is: for each possible k from n down to 0, check if there's a way to choose k commands such that the sum of their directions in x and y is zero. The first k for which this is possible is the answer.

The question is: how to compute for each k whether such a subset exists, and find the maximum possible k.

Now, the constraints are n up to 100. So for each k from 100 down to 0, we need to check if it's possible. For each k, we need to find a subsequence of length k where the sum of x and y is zero.

But even for k=50, trying all possible subsets is impossible. So we need a dynamic programming approach.

Hmm. Let's model this. Let's track the possible x and y displacements after i steps, using j steps (selected commands) up to i-th command.

Wait, but for each step, we can choose to include or exclude the command. For each possible selection, we track the current x and y displacement, and the number of commands selected so far. Then, for each possible step, we can update these values.

The problem is that the x and y displacements can be up to 100 steps in either direction (since each command adds ±1 to x or y). So for n=100, the maximum x displacement possible is 100 (all R's, for example). Similarly for y. So the possible x ranges from -100 to 100, y from -100 to 100, and the number of selected steps up to 100.

So the state for dynamic programming can be:

dp[i][x][y][k] = possible to have x and y displacement after first i commands, using exactly k selected commands, leading to (x, y). But this is a 4-dimensional DP, which would be 100 (i) * 200 (x) * 200 (y) * 100 (k) = 100 * 200 * 200 * 100 = 400 million states. That's way too much.

Alternative approach: for each possible k (from n down to 0), check if there's a way to choose exactly k commands such that sum of x and y is zero. So for each k, we can model the problem as: select a subset of k commands, in order, such that the sum of their x and y movements is (0,0). The maximum such k is the answer.

So, for each k, we can check if such a subset exists.

How to check this for a given k?

We can model this as a problem where we have to select exactly k commands, and the sum of their movements is (0,0). So for a given k, the sum of the x movements must be 0, and the sum of the y movements must be 0.

So let's model this with a DP that tracks, for each step i in the command sequence, the possible (x, y) displacements that can be achieved by selecting exactly m commands up to step i, where m ranges from 0 to k.

Wait, but for a given k, the maximum possible steps is n, and for each step, we track the possible x and y displacements for m steps selected (m <= k). So for each k, we can create a DP table where dp[i][x][y][m] is True/False indicating whether after i commands, selecting m commands, the displacement is (x,y). But for k up to 100, and i up to 100, x and y can be up to 100 each. So the state is i (100) * x (200) * y (200) * m (100). For each k, this is 100 * 200 * 200 * k. But for k=100, that's 100 * 200*200 *100 = 400 million per k. That's way too slow.

Alternative idea: for a given k, the sum of x steps must be even (since total x movement must be zero)? No, for example, two R's and two L's would sum to zero. But even the number of steps in x direction may be even or odd. So that's not helpful.

Alternatively, for a given k, the sum of x and sum of y must be zero. So the sum of all selected x moves (R and L) must be (R - L) equal to zero. Similarly for U and D.

But the problem is that the x and y are handled by the commands. For each command, it's either x or y. For example, a 'U' adds +1 to y, 'D' subtracts 1 from y. 'R' adds +1 to x, 'L' subtracts 1 from x.

So, for each command, depending on its type, it contributes to x or y.

So, for a given k, we need to select a subset of k commands (in order) such that:

sum of x movements (R and L) is 0.

sum of y movements (U and D) is 0.

So, perhaps we can model this with a DP that tracks for each step i, the possible x, y, and the number of selected commands m, and the sum of x and sum of y.

But even this is tricky because the sum of x and sum of y can be large.

Alternative approach: precompute for all possible k, the maximum possible even split between x and y.

Wait, for the selected commands, some are in x direction (L or R) and others in y (U or D). So for the sum of x to be zero, the number of R's minus L's must be zero. Similarly, the number of U's minus D's must be zero.

But how?

Wait, in the selected subset, the number of R commands minus L commands must be zero. Because each R is +1, L is -1. So net x is (R_count - L_count) = 0. Similarly, U_count - D_count = 0.

So the sum x is zero iff R_count = L_count, and sum y is zero iff U_count = D_count.

But the total number of selected commands is R_count + L_count + U_count + D_count = k.

So for a subset of k commands, the sum is zero if:

R = L (x direction) and U = D (y direction), and R + L + U + D = k.

So, R + L must be even (since R = L → R + L = 2R), and U + D must be even as well. But even if R + L is even, that's not necessarily the case. Wait, R and L are the counts. For example, R=2, L=2: R+L=4 (even). R=3, L=3: R+L=6 (even). So yes, R+L must be even. Similarly for U and D.

So the sum x is zero only if R + L is even, and R = L. So for x direction, the total number of x moves (R + L) must be even, and the same for y.

But how does this help us?

Wait, but perhaps for a given k, we can split it into x_moves (R and L) and y_moves (U and D). The sum x is zero only if x_moves is even and R = L. So x_moves must be even. Similarly for y_moves. So total x_moves + y_moves = k.

So for a given k, the possible x_moves can be even, and y_moves can be even, but their sum is k.

But how to model this.

Alternatively, for a given k, we can iterate over possible x_moves (even numbers) and y_moves (even numbers) such that x_moves + y_moves = k. Then, check if it's possible to select x_moves / 2 R and x_moves / 2 L commands in the sequence, and y_moves / 2 U and D commands.

Wait, but that's not possible. Because the sequence is ordered, and we can't reorder. So the selected commands must form a subsequence where the order is preserved.

So even if there are enough R, L, U, D commands, their positions in the sequence may not allow a subset of x_moves (R and L) and y_moves (U and D) with the required counts.

So, this approach seems challenging.

Another idea: For each possible k (starting from largest possible), iterate over all possible possible x_moves (even) and y_moves (even) where x_moves + y_moves = k, and x_moves >=0, y_moves >=0.

For each such x_moves and y_moves, check if the sequence contains at least x_moves/2 R and x_moves/2 L, and y_moves/2 U and y_moves/2 D. Then, check if it's possible to select these commands in order.

But even if there are enough R, L, U, D, the order might not allow selecting them in a way that forms a subsequence.

For example, if the sequence is R R L L, then x_moves=4 (2 R and 2 L) is possible. But if the sequence is R L R L, same counts.

But in a sequence like R R R L L L, x_moves=4 would require 2 R and 2 L, which can be selected as the first two R's and the first two L's, but perhaps not in a way that they are in order.

Wait, the subsequence must preserve the order. So in the sequence R R R L L L, selecting the first two R's and the last two L's would form a valid subsequence. So the order is R R L L (positions 0,1,3,4). That's allowed.

So, perhaps the order doesn't matter as long as there are enough R and L, and similarly for U and D.

Wait, no. For example, the sequence is R L R L. To select two R and two L, you can choose positions 0,2 (R) and 1,3 (L), which is allowed as a subsequence.

So, as long as the total counts of R and L are at least x_moves/2 each, and same for U and D, then it's possible to find a subsequence with those counts. Because you can select the earliest x_moves/2 R's and earliest x_moves/2 L's. Wait, no. For example, if the sequence is R L R L R L, and you need to select 3 R and 3 L. But there are 3 R's and 3 L's. So it's possible. But what if the sequence is R R R L L. Then, to select 2 R and 2 L, you can take the first two R's and the first two L's. So even if there are more R's than needed, as long as the counts are sufficient, the order allows selection.

So perhaps the minimal approach is: for a given k, check all possible x_moves (even) and y_moves (even) that sum to k. For each such pair (x_moves, y_moves), check if the original sequence contains at least (x_moves/2) R and (x_moves/2) L, and (y_moves/2) U and (y_moves/2) D. If any such pair exists, then the answer is at least k.

But this is not correct. Because even if the counts are sufficient, the positions may not allow selecting them in order. For example, consider a sequence like R R R R R R L L L L L L. Suppose x_moves is 4 (so 2 R and 2 L). The first two R's are early, and the first two L's are after all R's. So the subsequence would be R R (from first two) and L L (from first two L's). The order is preserved, so that's allowed. So in this case, counts are sufficient.

So the order isn't a problem as long as the counts are sufficient. Because the selected commands are in order, but you can skip the intermediate ones. So even if the required R's and L's are all in the beginning and end, you can still select them.

Therefore, the minimal way to check for a given k is to see if there exists an x_moves (even) and y_moves (even) such that x_moves + y_moves = k, and the total R's in the sequence is >= x_moves / 2, L's >= x_moves / 2, U's >= y_moves / 2, D's >= y_moves / 2.

If such a pair (x_moves, y_moves) exists, then the answer could be k.

So the approach would be:

For each k from n down to 0:

   For all possible x_moves in 0, 2, 4,... up to min(k, even steps):

      y_moves = k - x_moves

      if y_moves is even and >=0:

          required_R = x_moves // 2

          required_L = x_moves // 2

          required_U = y_moves // 2

          required_D = y_moves // 2

          check if the original sequence has at least required_R R's, required_L L's, required_U U's, required_D D's.

          If yes, then return k as the answer.

So the first k (starting from n) where such a split exists is the maximum possible.

But wait, even if the counts are sufficient, the actual commands may not form a valid subsequence. For example, suppose the sequence is "UUUUDDDDLLL". Suppose x_moves is 2 (1 R and 1 L). But there are no R's. So required_R is 1, but the count of R is zero, so this split is invalid.

But in this case, the code would not select that split.

So this approach is correct only if the counts of R, L, U, D in the original sequence are sufficient. Because the code checks whether the required counts are present.

But the problem is that the actual commands may not have the required number of R, L, U, D. So the code checks for that.

But how about the order? For example, suppose the sequence is R L R L. If x_moves is 4 (2 R and 2 L), then required_R and required_L are 2 each. The code would check if the count of R is >= 2 and count of L >=2. If yes, then it's possible to select 2 R and 2 L in order, which it is.

But if the sequence is R R L R, required_R is 2 and L is 2. Then the counts would be R:3, L:1. So required_L is 2, but available is 1. So the code would not consider this split.

So, the code's approach is correct in that it only considers splits where the required counts are available. But even when the required counts are available, the order of the commands may allow selecting the required R, L, U, D in the sequence as a subsequence. Which is always possible as long as the counts are sufficient.

Wait, because the commands are in a sequence. So, for example, to select required_R R's and required_L L's, you can just take the first required_R R's and the first required_L L's. But what if the R's are after the L's? For example, the sequence is LLL RRR. To select 2 L's and 2 R's, you can choose the first two L's and the first two R's, which are in order. So the subsequence would be L L R R. Which is allowed.

But what if the required_L is 2 and the sequence has 3 L's and 2 R's? For example, the sequence is L L L R R. To select 2 L's and 2 R's, you can take the first two L's and first two R's. So even if the R's come after the L's, you can take them.

So, the order doesn't matter as long as there are enough R, L, U, D. Because the subsequence can be formed by selecting the required number of each type, regardless of their positions in the original sequence, as long as they appear in order.

Therefore, the code's approach is correct. Because as long as the counts of R, L, U, D in the original sequence are >= the required, then a valid subsequence exists.

Thus, the maximum possible k is the largest k where there exists x_moves and y_moves (both even, sum to k) such that the required counts of R, L, U, D are present in the original sequence.

So the steps for the solution are:

1. Precompute the counts of R, L, U, D in the input string.

2. For k from n down to 0:

   a. For each possible x_moves in even numbers from 0 to min(k, ...):

      i. x_moves must be even, and <= k.

      ii. y_moves = k - x_moves. Must be even and >=0.

   b. For each possible x_moves and y_moves pair (both even, sum k):

      i. Check if R count >= x_moves / 2.

      ii. Check if L count >= x_moves / 2.

      iii. Check if U count >= y_moves / 2.

      iv. Check if D count >= y_moves / 2.

      v. If all conditions are met, return k as the answer.

3. If no such k is found (even for k=0), return 0. Wait, but k=0 is allowed, but the problem says 1<=n<=100, but in the sample input 5, the answer is 0, which implies that when k=0, the robot is at (0,0). So for k=0, the conditions are x_moves=0 and y_moves=0. So required_R=0, required_L=0, required_U=0, required_D=0. Which are always satisfied. So the code would return k=0 if no larger k is found.

So the code can check all k from n down to 0, and return the first possible k where a split exists.

Now, how to generate all possible x_moves and y_moves pairs for a given k.

For a given k, x_moves can be 0, 2, 4, ..., up to min(k, even number). For each x_moves, y_moves is k - x_moves. But y_moves must also be even and >=0.

So for example, if k is even:

   x_moves can be 0, 2, 4, ..., k.

   Then y_moves = k - x_moves must be even and >=0.

But since k is even, x_moves and y_moves are both even.

If k is odd:

   Then x_moves and y_moves must sum to an odd k, but since they are both even, their sum is even. So when k is odd, there's no possible x_moves and y_moves. So for odd k, we can skip checking.

So the code can iterate k from n down to 0. For each k:

   if k is even:

      iterate x_moves from 0 to min(k, 2*R, 2*L) (but in code, just check x_moves in even steps up to k, and y_moves even steps).

      for each x_moves in 0, 2, 4, ..., k:

          y_moves = k - x_moves

          if y_moves <0: skip

          if y_moves is even:

              check required_R = x_moves//2, required_L same, required_U and D = y_moves//2.

              if R >= required_R and L >= required_L and U >= required_U and D >= required_D:

                  return k.

   else (k is odd):

      skip.

So in code:

For k in range(n, -1, -1):

   if k %2 !=0:

       continue

   # k is even, split into x_moves and y_moves

   max_x = min(k, 2*min(r_count, l_count)) 

   # but this may not be necessary, just iterate x_moves from 0 to k in steps of 2.

   for x_moves in range(0, k+1, 2):

       y_moves = k - x_moves

       if y_moves <0:

           continue

       if y_moves %2 !=0:

           continue

       # now check if required counts are satisfied.

       req_r = x_moves //2

       req_l = x_moves //2

       req_u = y_moves //2

       req_d = y_moves //2

       if (r_count >= req_r and l_count >= req_l and u_count >= req_u and d_count >= req_d):

           print(k)

           exit()

print(0)

Wait, but what about the cases where even though x_moves and y_moves are even and sum to k, but there's no combination of R, L, U, D that satisfies the required counts?

But the code checks for that. For example, req_r = x_moves /2. So if x_moves is 4, req_r is 2. So the code checks if the original count of R is >=2, etc.

So this code should work.

Let's test it against the examples.

First example:

Input 4, LDUR.

The counts:

L:1, D:1, U:1, R:1.

For k=4:

It's even.

We need to split into x_moves and y_moves, both even.

Possible x_moves can be 0,2,4.

Check for x_moves=4:

y_moves=0.

req_r =4/2=2. But R count is 1. So no.

x_moves=2:

y_moves=2.

req_r=1 (x_moves/2=1). R count is 1 >=1.

L count is 1 >=1.

U count is 1 >=1 (y_moves/2=1).

D count is 1 >=1.

So all conditions are met. So return k=4. Which matches the first example.

Second example: 5 RRRUU.

n=5, k can be 4, but 5 is odd.

Check k=5: odd, skip.

k=4: even.

x_moves can be 0,2,4.

x_moves=0: y_moves=4. req_u=2, req_d=2. But in the input, D is 0, so no.

x_moves=2: y_moves=2. req_r=1, req_l=1. R count is3 >=1, L count 0 <1. So no.

x_moves=4: req_r=2, req_l=2. L count is 0 <2. So no.

So for k=4: no.

k=3: odd.

k=2: even.

x_moves 0,2.

x_moves=0: y_moves=2. req_u=1, req_d=1. D count is0 <1. No.

x_moves=2: req_r=1, req_l=1. L count 0 <1. No.

k=0: possible. So code returns 0.

Third example: 6 LLRRRR.

counts:

L:2, R:4.

U:0, D:0.

So for k=6 (even).

x_moves can be 0,2,4,6.

y_moves must be 6-x_moves and even.

Check x_moves=6, y_moves=0:

req_r=3, req_l=3. R count is4 >=3, L count is2 >=3? No. So no.

x_moves=4, y_moves=2. But y_moves requires U and D counts. But here U and D are 0, so req_u=1, req_d=1. So no.

x_moves=2: y_moves=4. same problem.

x_moves=0: y_moves=6. req_u=3, req_d=3. U and D counts are 0.

So no for k=6.

Next, check k=4 (even).

x_moves can be 0,2,4.

x_moves=4: req_r=2, req_l=2. R count 4 >=2, L count 2 >=2. Y_moves=0. So yes. So code returns 4.

Which matches the third example.

So the code works.

Now, code steps:

Read n, s.

Compute counts for R, L, U, D.

Loop k from n down to 0.

For each even k:

   for x_moves in 0 to k, step 2:

       y_moves =k -x_moves.

       if y_moves is even and >=0:

           check required counts.

           if all are met, return k.

Return 0.

So the code can be written as:

Read n, s.

r = s.count('R')

l = s.count('L')

u = s.count('U')

d = s.count('D')

for k in range(n, -1, -1):

    if k %2 !=0:

        continue

    # even k.

    # check all possible x_moves (even) and y_moves (even) that sum to k.

    found = False

    for x_moves in range(0, k+1, 2):

        y_moves = k - x_moves

        if y_moves <0 or (y_moves %2)!=0:

            continue

        req_r = x_moves //2

        req_l = x_moves //2

        req_u = y_moves //2

        req_d = y_moves //2

        if r >= req_r and l >= req_l and u >= req_u and d >= req_d:

            print(k)

            exit()

print(0)

Yes. This code should work.

Testing the second example: 5 RRRUU.

r=3, l=0, u=2, d=0.

For k=5: odd, skip.

k=4:

x_moves can be 0, 2,4.

x_moves=0: y_moves=4. req_u=2, req_d=2. d is 0 <2. No.

x_moves=2: y_moves=2. req_u=1, req_d=1. d is 0 <1.

x_moves=4: y_moves=0. req_r=2, l=0 <2. No.

No solutions. So k=4 no.

k=3: odd.

k=2:

x_moves 0: y_moves=2. req_u=1, d=0 <1.

x_moves 2: req_r=1, l=0 <1.

k=0: returns 0.

Yes.

So the code works.

This approach is O(n^2) in the worst case. For n=100, it's 100 iterations (k from 100 to 0). For each even k, the inner loop runs up to k/2 steps. For k=100, that's 50 steps. So total steps are around sum_{k even} (k/2 +1) ) for k from 0 to 100. Which is sum 0, 2 steps (k=2), ..., 50 steps (k=100). So total steps is sum_{i=0 to 50} (i*2 steps) → sum from i=0 to 50 of i*2 → 2*(50*51)/2 = 2550 steps. Which is acceptable.

Thus, the code is efficient enough for n up to 100.
</think>

```python
n = int(input())
s = input().strip()
r = s.count('R')
l = s.count('L')
u = s.count('U')
d = s.count('D')

for k in range(n, -1, -1):
    if k % 2 != 0:
        continue
    for x in range(0, k + 1, 2):
        y = k - x
        if y < 0 or y % 2 != 0:
            continue
        req_r = x // 2
        req_l = req_r
        req_u = y // 2
        req_d = req_u
        if r >= req_r and l >= req_l and u >= req_u and d >= req_d:
            print(k)
            exit()
print(0)
```