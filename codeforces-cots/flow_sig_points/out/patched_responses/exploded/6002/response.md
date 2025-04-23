<think>
Okay, let's see. The problem is about finding the minimum number of people that the conductor needs to persuade so that after swapping, every compartment with students has either 3 or 4 students. So each compartment's student count must be 0, 3, or 4. But since the students can't move among themselves, the swaps involve students moving with non-students. Wait, no. Wait, the problem says that the students want to swap with other people. So the other people are non-students. So when we swap, a student leaves their seat and a non-student comes in, or vice versa? Or maybe, the conductor can swap any student with any non-student. Hmm. Let me read the problem statement again.

The students can swap with other people. The conductor can persuade any passenger to switch places with some student. So each swap involves a student and a non-student exchanging seats. So when a student leaves their compartment (to swap with a non-student), their compartment's count decreases by one. The non-student's original compartment (if any) would have their count increased by one, but since the non-student is moving into a student's seat, maybe that's not part of the problem. Wait, maybe the compartments are only for students. Or perhaps the initial setup is that each compartment has ai students (the rest are non-students). So each compartment has 4 seats. The ai is the number of students in that compartment. The rest (4 - ai) are non-students.

So the problem is that after swapping, all compartments must have 0, 3, or 4 students. And each swap is between a student and a non-student. But how do the swaps affect the counts? Let's think: when a student moves out of a compartment (to swap with a non-student), the ai of that compartment decreases by 1. The non-student moves into another compartment (the one where the student was), but since they are a non-student, that compartment's ai increases by 1. Wait, no. Wait, the non-student is taking the student's seat. So the student's compartment loses a student (ai decreases by 1), and the non-student's original compartment (if they were in another compartment) loses a non-student (but ai is about students). So maybe the non-student is from some other compartment where they were a non-student. So when they swap, the student leaves their compartment (so ai decreases by 1), and the non-student joins the other compartment (so that compartment's ai increases by 1. Because in their original position, they were a non-student (so in some compartment, they were part of the 4-ai non-students). Wait, perhaps this is getting complicated.

Alternatively, perhaps the process is that each swap is moving a student from their compartment to some other compartment (replacing a non-student there), but that's not clear. Maybe the problem is that the conductor can choose any two people (student and non-student) to swap. So each swap can be thought of as: take a student from compartment A (ai decreases by 1) and a non-student from compartment B (ai increases by 1 if the non-student moves to A, or maybe they just swap seats. So when they swap seats, the student leaves their compartment (ai decreases by 1), and the non-student leaves their compartment (so ai for their compartment decreases by 0, because they were a non-student. Then the student is placed into the non-student's compartment (so ai increases by 1). Similarly, the non-student is placed into the student's compartment, so ai decreases by 1 (since a non-student is added there). Wait, this seems a bit confusing.

Alternatively, maybe each swap is moving a student to a non-student's seat. So the student leaves their compartment (ai decreases by 1) and the non-student leaves their seat (which may be in any compartment) and takes the student's seat. But in that case, the non-student's original compartment's ai remains the same (since they were a non-student). The student's new seat is in the non-student's original compartment, so that compartment's ai increases by 1. So each swap affects two compartments: the student's original compartment (ai decreases by 1) and the non-student's original compartment (ai increases by 1).

But how can we model this? The problem is to find the minimum number of swaps (people to persuade) such that after all swaps, each compartment's ai is 0, 3, or 4.

But perhaps there's a simpler way to model the problem. Let's think of the possible desired ai values. For each compartment, after all swaps, the ai must be 0, 3, or 4. But the students can't be in a compartment with 1 or 2 students.

So the idea is to redistribute the students into compartments such that each non-zero compartment has 3 or 4 students. The minimal number of swaps needed to achieve this.

But how do the swaps affect the counts?

Each swap involves a student leaving their compartment (ai decreases by 1) and a non-student entering a compartment (ai increases by 1). So each swap effectively allows us to move a student from one compartment to another. But since the non-student's original compartment is not tracked (as they are non-students), perhaps the swap allows us to subtract 1 from some ai and add 1 to another ai. So each swap is a transfer of a student from one compartment to another. Because each swap moves a student from compartment X (ai decreases by 1) and adds a student to compartment Y (ai increases by 1). So the net effect is moving one student from X to Y.

Wait, but that's not exactly right. Because the non-student's original compartment is where the student is moving to. So when the student leaves X (ai decreases by 1), and the non-student from Y's compartment (which has 4 - aY non-students) leaves, and the student takes their place. So Y's ai increases by 1 (since a student is added). So each swap transfers one student from X to Y. So each swap can be considered as a transfer of one student from X to Y. So each such transfer requires one swap (since the conductor needs to persuade two people: the student and the non-student). So each transfer of a student from X to Y requires one swap. Therefore, the total number of swaps needed is equal to the number of such transfers.

So the problem reduces to: find a way to redistribute the students among the compartments (possibly moving students between compartments) such that each compartment's ai is 0, 3, or 4. The cost is the number of students moved (since each movement is a swap). We need to find the minimal total cost (number of swaps) required to achieve this.

Wait, but moving a student from X to Y requires one swap, regardless of the direction. So the total number of swaps is equal to the total number of students moved (since each movement of a student from X to Y is one swap).

So the problem is now equivalent to redistributing the students into compartments (each with 0,3,4), using as few student movements as possible.

The sum of all ai (total students) must be adjusted such that the sum can be partitioned into compartments of 3 or 4. But wait, the sum S must be equal to sum( (3 or 4)*k ), where k is the number of non-zero compartments. Wait, no. Because the sum can be any sum that can be represented as a sum of 3s and 4s, possibly with some zeros.

Wait, for example, if there are 3 compartments, the sum could be 3 + 4 + 0 = 7. So the total sum S must be a sum of 3s and 4s. But how? For example, the total sum after redistribution must be equal to some combination of 3 and 4. Because each non-zero compartment contributes 3 or 4. So S must be a sum of 3's and 4's. So first, the total sum of the original ai's (call it total) must be such that total can be written as 3x + 4y for some non-negative integers x and y. Because after redistribution, the sum of students is the same (since we are moving students between compartments, not adding or removing them). Wait, no. Wait, no. Because when we swap a student with a non-student, the total number of students in the train remains the same. Because each swap is a student leaving (so total decreases by 1) and a non-student coming in (so the total increases by 1). Wait, this is where I was getting confused earlier. Because a swap is between a student and a non-student, so when they swap seats, the total number of students in the train remains the same. Because the student is leaving (count decreases by 1), and the non-student becomes a student (count increases by 1). So the total remains the same. Therefore, the sum of ai after the swaps must equal the original sum. So if the original sum is not possible to be represented as a sum of 3's and 4's (since each non-zero compartment contributes 3 or 4), then it's impossible, so the answer is -1.

So first, the problem requires that the original sum of ai must be possible to be expressed as a sum of 3's and 4's. Otherwise, output is -1.

For example, in the first sample input:

5 compartments, ai = 1 2 2 4 3. Sum is 1+2+2+4+3 = 12. 12 can be 3*4, so possible.

In the second example:

3 compartments: 4+1+1=6. 6 can be 3+3, so possible.

Third example: 0+3+0+4=7. 3+4=7. So yes.

But if the sum is 5, then no: 5 can't be expressed as a sum of 3 and 4. So output is -1.

So the first check is: compute the sum of ai. If sum is 0 (but the problem says it's guaranteed that at least one student is present), so sum >=1. So sum must be possible to be divided into some combination of 3s and 4s. So first, check if sum is 0 mod 3 or 0 mod 4, or can be expressed as 3a +4b for a,b >=0. If not, output is -1.

So how to check this? For example, for a sum S, find if there's a way to write S = 3a +4b. Let's see:

The possible sums are all numbers except 1, 2, 5. For example:

3 → 3.

4 →4.

6=3+3.

7=3+4.

8=4*2.

9=3*3.

10=3*2 +4*1 (6+4=10).

Wait, 5 can't be written as such. So for S >=3, except for 5, 7, etc. Wait, perhaps the general way is:

After S >=3:

- S mod 3 can be 0,1,2.

If S mod 3 is 0: then possible (all 3s).

If S mod3 is 1: then we need to subtract 4 (since 4 mod3 is 1) once. So for example, S=7: 3*1 +4*1=7.

But for S=4, 4 mod3 is 1. So 4 can be written as 4.

So the rule is: for S, the possible is if S can be written as 3k +4m.

The steps to check:

We can iterate over possible numbers of 4s (from 0 to S//4), and see if (S -4m) is divisible by 3 and non-negative.

Alternatively, find the minimal number of 4s such that (S -4m) is divisible by 3 and >=0.

But since we need to check if any m exists, regardless of the number, we can compute this.

But for the problem, the first thing is to check if the sum S is possible to be written as sum of 3s and4s.

So first step: compute the sum of all ai. If the sum is not possible to be expressed as 3a +4b, then output -1.

Otherwise, proceed.

Now, the next step is to find the minimal number of swaps (students moved) to redistribute the ai into compartments such that each is 0,3,4, and the sum is S.

So how to model this?

Each swap moves a student from one compartment to another, which takes one swap per move. So the total number of swaps is the sum of the absolute differences between the original ai and the target configuration, divided by 2 (since moving a student from A to B counts as one swap, and reduces A by 1 and increases B by 1. So the total number of moves is the sum of (ai - target_i) for all i where ai > target_i, divided by 1. Because each surplus in a compartment requires moving that many students out (each such move is a swap), and each deficit requires moving that many students in (each of which is a swap from another compartment).

Wait, maybe not. Let's think: For example, if a compartment has ai=5 (but this can't happen per input constraints, but just as example) and the target is 3, then we need to move 2 students out. Each movement is one swap. Similarly, if a compartment has ai=2, and the target is 3, we need to move 1 student in. So the total number of swaps is the sum of the absolute differences between the original and target ai, divided by 2. Because for each student moved from a compartment with surplus to a compartment with deficit, the total changes by 2 (since one compartment's surplus decreases by 1, the deficit's deficit decreases by 1). So the sum of (ai - target_i) for all i where ai > target_i is equal to the sum of (target_i - ai) for all i where ai < target_i. And the total number of swaps is equal to the sum of surplus (which is equal to sum of deficits), so each swap accounts for moving one unit of surplus to one unit of deficit. Therefore, the total swaps needed is the sum of surplus (or deficits) divided by 1. Because each movement is a single swap.

Wait, for example, suppose a compartment has a surplus of 2 (ai=5, target=3), and another has a deficit of 2 (ai=1, target=3). Then moving two students from the first to the second would require 2 swaps. So the total is 2. Which is the sum of surplus (2) or deficit (2) divided by 1. So yes, the total number of swaps is the sum of all surplus (which equals the sum of all deficits) and that sum is the total number of swaps.

So the problem now is to find a target configuration (each compartment 0,3,4) with sum equal to S (the original sum), and the sum of (ai - target_i) for surplus compartments (ai > target_i) must be equal to the sum of (target_i - ai) for deficit compartments (ai < target_i), and this sum is the minimal possible.

So how to model this?

The key steps are:

1. Check if the sum S can be written as a combination of 3's and 4's.

   - If not, output -1.

2. For all possible target configurations (compartment counts of 0,3,4) that sum to S, compute the minimal number of swaps required (sum of |ai - target_i| / 2, because for each swap, the movement reduces surplus and deficit by 1 each. So the total is (sum of surplus) = sum of deficits, so sum of surplus is (sum of |ai - target_i|)/2. So the total swaps is sum of surplus.

Wait, perhaps I'm getting confused here. Let me think again.

Suppose for a target configuration, the sum of (ai - target_i) over all compartments is zero (since sum of ai is S, sum of target_i is also S). So the surplus (sum of ai - target_i for ai >= target_i) must equal the deficit (sum of target_i - ai for ai < target_i). The total swaps needed is the surplus, which is the same as the deficit.

So the total number of swaps is the sum of (ai - target_i) for all compartments where ai > target_i.

Therefore, for each possible target configuration, compute this sum and find the minimal one.

But how can we model this efficiently?

The problem is that n can be up to 1e6, so any O(n) per candidate approach is feasible, but generating all possible target configurations is not possible.

So we need to find a way to model the target configuration optimally.

But what's the target configuration? For each compartment, the target can be 0, 3, or 4.

But the sum of the targets must equal S, which is the original sum.

But S must be expressible as a combination of 3 and 4, so the sum is S = 3x +4y, where x and y are the number of compartments with 3 and 4 students, respectively. The remaining compartments (n -x -y) must be 0.

But wait, the problem allows compartments to be 0, 3, or 4. So x is the number of compartments with 3 students, y is the number with 4 students, and z is the number with 0, such that x + y + z = n.

But the sum S = 3x +4y.

So for a given S, we can find all possible pairs (x, y) such that 3x +4y = S and x >=0, y >=0, and x + y <=n (since z = n -x -y >=0).

So the possible (x,y) pairs are those that satisfy 3x +4y = S and x + y <=n.

Once we have such a pair (x,y), the number of compartments set to 0 is z = n -x -y.

Our task is to choose which compartments are set to 0, 3, or 4, such that x are 3, y are 4, and the rest are 0. Then compute the minimal sum of (ai - target_i) over all compartments where ai > target_i (since those are the surpluses). The sum of surpluses is the required number of swaps.

But the problem is how to choose which compartments to assign 0,3,4 to minimize the sum of surpluses.

But since the compartments are given in the input, the optimal assignment is to assign the highest possible target values to the compartments with the largest ai, and 0 to the compartments with the smallest ai. Because that way, the surpluses are minimized.

Wait, perhaps the optimal approach is to assign the targets in such a way that:

- For compartments that are to be set to 4, we choose those with the highest ai. Because if their ai is 4, no surplus. If it's higher, then we have surplus, but perhaps it's unavoidable.

Wait, but this is getting complicated.

Alternatively, for a given (x,y), where we have x compartments set to 3, y set to 4, and the rest set to 0, the best way to minimize the sum of surpluses is to assign the largest possible targets to the compartments with the largest ai.

So for example:

- All compartments that will be set to 4 must be the ones with the highest ai.

- Then, compartments set to 3 are the next highest.

- The rest are set to 0.

This way, the ai's are matched as closely as possible to their targets, minimizing the surpluses.

So the plan is:

For each possible (x,y) pair that satisfies 3x +4y = S and x + y <=n:

   - Assign the top (y) ai's to be 4, next (x) to 3, rest to 0.

   - Compute the sum of surpluses (ai - target_i for those where ai > target_i).

   - The minimal sum across all valid (x,y) pairs is the answer.

So the steps are:

1. Compute the sum S of ai.

2. Check if S can be written as 3x +4y. If not, return -1.

3. Generate all possible (x,y) pairs that satisfy 3x +4y = S and x >=0, y >=0, x + y <=n.

4. For each (x,y) pair:

   a. Sort the ai in descending order.

   b. The first y compartments are assigned target 4.

   c. The next x compartments are assigned target 3.

   d. The rest (n -x -y) are assigned target 0.

   e. Compute the sum of (ai - target) where ai > target.

5. Find the minimal sum across all valid (x,y) pairs.

The minimal sum found in step 5 is the answer. If there are no valid (x,y) pairs, return -1.

But how to generate all possible (x,y) pairs efficiently?

The possible (x,y) pairs can be generated by iterating over possible values of y (number of 4's) and checking if (S -4y) is divisible by 3, and x = (S -4y)/3, then check x >=0 and x + y <=n.

But since S can be up to 4*1e6 (since n is up to 1e6, and each ai up to 4), the loop for y can be up to S//4.

But for S up to 4e6, this loop can take up to 1e6 iterations, which is manageable.

But considering that for each (x,y) pair, we need to sort the ai array (which is 1e6 elements), this would be O(n log n) for each pair, leading to 1e6 * 1e6 log n operations, which is way too slow.

Wait, that's a problem. Because n is up to 1e6, sorting the array each time for each (x,y) pair would be O(n log n) per pair, which is not feasible.

So, we need a way to preprocess the ai array such that for any y and x, we can compute the sum of (ai -4) for the top y compartments (if ai >4), sum of (ai -3) for the next x compartments (if ai>3), and sum (ai -0) for the rest (if ai>0). But since the rest are set to 0, but their ai may be positive (so their surplus is ai -0 = ai).

Wait, but if the target is 0, then any ai in those compartments must be reduced to 0. So the surplus is ai (since ai must be >0 to be a surplus). For example, if a compartment is assigned 0, and ai is 2, then we need to move 2 students out (each movement is a swap). So the surplus here is 2.

So the sum for a given (x,y) is:

sum_{i=0 to y-1} max(0, a_sorted[i] -4) +

sum_{i=y to y+x-1} max(0, a_sorted[i] -3) +

sum_{i=y+x to n-1} a_sorted[i]

Where a_sorted is the sorted array in descending order.

But how to compute this sum efficiently for different x and y?

We can pre-sort the array in descending order once, then precompute prefix sums.

Additionally, precompute prefix sums for:

- The sum of max(0, a_i -4) for the first k compartments.

- The sum of max(0, a_i -3) for compartments from position l to r.

Wait, but this may not be straightforward. Let's think:

For the top y compartments (sorted in descending order), each is assigned to 4. The surplus is the sum of (a_i -4) if a_i >4. Otherwise, zero.

For the next x compartments, assigned to 3. The surplus is sum of (a_i -3) if a_i >3.

For the remaining compartments (n -x -y), assigned to 0. The surplus is sum of a_i (since they must be moved out).

So the total surplus is:

sum_4 = sum_{i=0 to y-1} max(a_i -4, 0)

sum_3 = sum_{i=y to y +x -1} max(a_i -3, 0)

sum_0 = sum_{i= y +x to n-1} a_i

Total swaps = sum_4 + sum_3 + sum_0

We need to compute this for each (x,y) pair and find the minimal one.

But how to compute these sums quickly for all possible (x,y) pairs?

We can pre-sort the array in descending order.

Then precompute three prefix sums:

1. prefix_max4: for each position i, the sum of max(a_j -4, 0) for the first i elements.

2. prefix_max3: for each position i, the sum of max(a_j -3, 0) for the first i elements.

3. prefix_sum: the sum of a_j for the first i elements.

But let's think:

For a given y, the sum_4 is prefix_max4[y].

sum_3 is (prefix_max3[y + x] - prefix_max3[y])

sum_0 is (prefix_sum[n] - prefix_sum[y + x])

Wait, no. Because prefix_sum[n] is the sum of all a_i. So sum_0 is the sum of a_i from y+x to end. So sum_0 = prefix_sum[n] - prefix_sum[y +x].

Similarly, sum_3 is the sum of max(a_i -3, 0) from i = y to y +x-1. Since the array is sorted, the first y elements are the top y elements. The next x elements are from y to y +x-1.

So for sum_3, it would be prefix_max3[y +x] - prefix_max3[y].

sum_4 is prefix_max4[y].

sum_0 is (prefix_sum[n] - prefix_sum[y +x]).

So, given these precomputed prefix arrays, for any (x,y), we can compute the sum in O(1) time.

Thus, the steps are:

1. Sort the array in non-increasing order.

2. Precompute prefix_max4 array: prefix_max4[i] = sum_{j=0 to i-1} max(a[j] -4, 0).

3. Precompute prefix_max3 array: prefix_max3[i] = sum_{j=0 to i-1} max(a[j] -3, 0).

4. Precompute prefix_sum array: prefix_sum[i] = sum_{j=0 to i-1} a[j].

Then, for each possible (x,y) pair:

   a. Check that x = (S -4y)/3, x >=0, y >=0, x + y <=n.

   b. Then, check that y +x <=n.

   c. Then, compute:

      sum_4 = prefix_max4[y]

      sum_3 = prefix_max3[y + x] - prefix_max3[y]

      sum_0 = (prefix_sum[n] - prefix_sum[y +x])

      total = sum_4 + sum_3 + sum_0

   d. Keep track of the minimal total.

The minimal total is the answer.

So the crux is to precompute these prefix sums once, then iterate over all possible (x,y) pairs and compute the sum quickly.

Now, the steps to implement:

First, sort the array in descending order.

Compute the prefix sums.

Then, iterate over possible y values (number of 4s):

For each possible y (from 0 to min(S//4, n)), check if (S -4y) is divisible by 3.

If yes, compute x = (S -4y)/3.

Check if x is >=0 and x + y <=n.

If all conditions are met, compute the sum as above.

Keep track of the minimal sum.

Finally, return the minimal sum if any valid (x,y) exists. Otherwise, -1.

But how to generate all possible y values?

Let's see. Since 3x +4y = S, and x >=0, y >=0.

So y can be at most S//4.

But since S can be up to 4e6 (n up to 1e6, each ai up to 4), this would be up to 1e6 iterations, which is manageable.

So in code:

Compute S = sum(ai).

Sort the array in descending order.

Compute the three prefix arrays.

Initialize the minimal sum to a large value (infinity).

Loop y from 0 to min(S//4, n):

   if (S -4y) is negative, break.

   if (S -4y) is not divisible by 3, continue.

   x = (S -4y) //3.

   if x is negative, continue.

   if x + y >n, continue.

   Then, check if x >=0.

   Now, check if the sum x + y is <=n.

   Then, compute the sum as per the prefix arrays.

   Update the minimal sum.

So in code:

But wait, x can be (S -4y)/3. So for each y in 0 <= y <= (S)//4, and (S -4y) must be >=0 and divisible by 3.

So the code would generate all possible y and x pairs.

Once x and y are determined, check x + y <=n.

If yes, proceed to compute the sum.

So for each such valid (x,y), compute sum_4, sum_3, sum_0, and add them up.

Now, let's test this approach with the sample inputs.

Sample input 1:

5

1 2 2 4 3

sum is 1+2+2+4+3=12.

sorted array: 4,3,2,2,1.

prefix_max4:

For each element:

4 →4-4=0 → sum 0.

3 →0.

2 →0.

2 →0.

1 →0.

prefix_max4 is [0,0,0,0,0,0].

prefix_max3:

4 →4-3=1.

3 →3-3=0.

2 →0.

2 →0.

1 →0.

prefix_max3 is [0,1,1,1,1,1].

prefix_sum is [0,4,7,9,11,12].

So for each possible (x,y):

We need to find x and y such that 3x +4y=12.

Possible y can be 0, 1, 2, 3.

y=0: x=4. Check x+y=4+0=4 <=5. sum_4=0 (y=0). sum_3 is prefix_max3[4] - prefix_max3[0] = 1 (prefix_max3[4] is 1, since the first 4 elements are 4,3,2,2. The sum is 1 (from 4-3) + 0 (3-3) + 0 (2-3) + 0 (2-3) → sum is 1. So sum_3=1. sum_0 is prefix_sum[5] - prefix_sum[4] = 12-11=1. So total=0+1+1=2. Which matches the sample output.

y=3: 4*3=12 → S-4y=0 →x=0. x+y=3 <=5. sum_4 is prefix_max4[3] = sum of first 3 elements (4,3,2) → max(4-4,0) is 0, 3-4 is -1 →0, 2-4 is -2 →0. sum_4=0. sum_3 is prefix_max3[3] - prefix_max3[3] → 0. sum_0 is prefix_sum[5] - prefix_sum[3] =12-9=3. Total=0+0+3=3. Which is higher than 2.

Other y's:

y=1 →4*1=4 →S-4=8 →x=8/3 → not integer.

y=2 →4*2=8 → S-8=4 →x=4/3 → not integer.

y=3 → as before.

y=0 is the only valid with x=4.

So the minimal sum is 2.

Which matches the sample.

Sample input 2:

3

4 1 1 → sum 6.

sorted array:4,1,1.

prefix_max4: [0,0,0,0].

prefix_max3: [0,1 (4-3=1), 1 (1-3 is 0), 1 (1-3 is 0)].

prefix_sum: [0,4,5,6].

Possible (x,y):

6=3x +4y.

Possible y can be 0,1.

y=0: x=2 → x+y=2 <=3. sum_4=0 (y=0). sum_3 is prefix_max3[2] - prefix_max3[0] = 1 (from 4-3) + (1-3=0) → sum is 1. sum_0 is prefix_sum[3] - prefix_sum[2] →6-5=1. Total=1+1=2.

y=1: 4*1=4 →6-4=2 →x=2/3 → not integer.

y=1.5: no.

So only y=0, x=2 is valid. Sum is 1+1=2. Which matches the sample.

Another sample input:

4

0 3 0 4 → sum is 7.

sorted array:4,3,0,0.

prefix_max4: sum of max(a_i -4,0) for first y elements.

y can be 0,1.

sum=7. So possible (x,y):

7=3x+4y.

Possible y=1 →4 →7-4=3 →x=1. x+y=2 <=4.

sum_4: prefix_max4[1] →4-4=0 → sum_4=0.

sum_3: next x=1 elements (3). max(3-3,0)=0. sum_3=0.

sum_0: the rest 4-1-1=2 elements (0,0). sum is 0.

Total is 0+0+0=0.

Which matches the sample.

So the approach works.

Now, the code:

First, read n.

Then read the list of ai.

Compute sum S = sum(ai).

Sort the ai in descending order.

Precompute the prefix_max4, prefix_max3, prefix_sum arrays.

Then iterate over y from 0 to S//4.

For each y, compute if (S-4y) is divisible by 3. If not, skip.

Else x = (S-4y)/3. Check x >=0 and x+y <=n.

If valid, compute the sum_4, sum_3, sum_0.

Update the minimal sum.

Finally, output the minimal sum if found, else -1.

Edge cases:

For S=0 (but the problem says at least one student is present).

Another case where sum S can be formed as 3x +4y, but x +y >n. So no possible assignment (since x+y compartments are required to be 3 or 4, but the total compartments is n. So x+y must be <=n. So in such case, this (x,y) is invalid.

So in code, after computing x and y, check x +y <=n.

Now, code implementation.

Let's code this step by step.

First, read n and the list:

n = int(input())

a = list(map(int, input().split()))

S = sum(a)

Sort the list in descending order.

a.sort(reverse=True)

Compute prefix_max4, prefix_max3, prefix_sum.

prefix_max4 = [0]*(n+1)

prefix_max3 = [0]*(n+1)

prefix_sum = [0]*(n+1)

for i in range(1, n+1):

    prefix_max4[i] = prefix_max4[i-1] + max(a[i-1] -4, 0)

    prefix_max3[i] = prefix_max3[i-1] + max(a[i-1] -3, 0)

    prefix_sum[i] = prefix_sum[i-1] + a[i-1]

Then, iterate over possible y.

Initialize min_swaps to a large value.

min_swaps = float('inf')

for y in range(0, S//4 +1):

    remaining = S -4*y

    if remaining <0:

        continue

    if remaining %3 !=0:

        continue

    x = remaining //3

    if x <0:

        continue

    if x + y >n:

        continue

    # Now compute sum_4, sum_3, sum_0

    sum_4 = prefix_max4[y]

    sum_3 = prefix_max3[y +x] - prefix_max3[y]

    sum_0 = prefix_sum[n] - prefix_sum[y +x]

    total = sum_4 + sum_3 + sum_0

    if total < min_swaps:

        min_swaps = total

if min_swaps != float('inf'):

    print(min_swaps)

else:

    print(-1)

But wait, when x is (S-4y)/3, and x can be up to S//3. Also, we have to make sure that the sum x + y is <=n.

But how to generate y?

For example, y can be up to min(S//4, n). But in the code, y is up to S//4. Then, after x is computed, we check if x + y <=n. So even if y is up to S//4, but x +y may exceed n. So that check is necessary.

But in the code, the loop runs y from 0 to S//4. So for large S, this could be up to 1e6 iterations.

But given that S can be up to 4e6, this is 1e6 iterations, which is manageable.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    S = sum(a)
    a.sort(reverse=True)

    prefix_max4 = [0] * (n + 1)
    prefix_max3 = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_max4[i] = prefix_max4[i - 1] + max(a[i - 1] - 4, 0)
        prefix_max3[i] = prefix_max3[i - 1] + max(a[i - 1] - 3, 0)
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    min_swaps = float('inf')
    max_y = S // 4
    for y in range(0, max_y + 1):
        remaining = S - 4 * y
        if remaining < 0:
            continue
        if remaining % 3 != 0:
            continue
        x = remaining // 3
        if x < 0 or x + y > n:
            continue
        total = prefix_max4[y]
        if y + x <= n:
            total += prefix_max3[y + x] - prefix_max3[y]
            total += prefix_sum[n] - prefix_sum[y + x]
        else:
            continue
        if total < min_swaps:
            min_swaps = total

    if min_swaps != float('inf'):
        print(min_swaps, file=output_stream)
    else:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
4 1 1
""",
            "output": \
"""\
2
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
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    S = sum(a)
    a.sort(reverse=True)

    prefix_max4 = [0] * (n + 1)
    prefix_max3 = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_max4[i] = prefix_max4[i - 1] + max(a[i - 1] - 4, 0)
        prefix_max3[i] = prefix_max3[i - 1] + max(a[i - 1] - 3, 0)
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    min_swaps = float('inf')
    max_y = S // 4
    for y in range(0, max_y + 1):
        remaining = S - 4 * y
        if remaining < 0:
            continue
        if remaining % 3 != 0:
            continue
        x = remaining // 3
        if x < 0 or x + y > n:
            continue
        total = prefix_max4[y]
        if y + x <= n:
            total += prefix_max3[y + x] - prefix_max3[y]
            total += prefix_sum[n] - prefix_sum[y + x]
        else:
            continue
        if total < min_swaps:
            min_swaps = total

    if min_swaps != float('inf'):
        print(min_swaps, file=output_stream)
    else:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
0 3 0 4
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

Sample3:

4

0 3 0 4 → sum 7.

sorted as 4,3,0,0.

y can be up to 7//4=1.

y=1:

4*1=4 → remaining=3 →x=1. x+y=2 <=4.

sum_4: first element 4-4=0. sum_4=0.

sum_3: next x=1 element (3). 3-3=0. sum_3=0.

sum_0: sum of elements from index 2 onwards (0,0). sum_0=0.

Total 0. Which is correct.

Another case: sum is 5.

Which is not possible. So output -1.

Another case: sum=7, n=1.

y=1:4*1=4. remaining 3. x=1. x+y=2>1. invalid. So no solution. So output -1.

So code handles that.

So the code should work.

Now, code in Python:

But in Python, for large n (up to 1e6), we need to handle the input efficiently.

But the code uses input().split() which is acceptable.

But for n=1e6, reading the list is possible.

But in practice, for Python, when reading a large list, using sys.stdin is faster.

But the problem states that the code must read input using input(), so we'll proceed.

But let's think about the code for n=1e6. The code sorts the list in O(n log n) time, which is acceptable.

The prefix arrays are O(n) each.

Then, the loop is O(S//4) steps, which for S up to 4e6 is 1e6 steps. Each step is O(1), so acceptable.

So overall, the code should work within the time constraints.

Now, the code:
</think>

```python
n = int(input())
a = list(map(int, input().split()))
S = sum(a)
a.sort(reverse=True)

prefix_max4 = [0] * (n + 1)
prefix_max3 = [0] * (n + 1)
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_max4[i] = prefix_max4[i - 1] + max(a[i - 1] - 4, 0)
    prefix_max3[i] = prefix_max3[i - 1] + max(a[i - 1] - 3, 0)
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

min_swaps = float('inf')
max_y = S // 4
for y in range(0, max_y + 1):
    remaining = S - 4 * y
    if remaining < 0:
        continue
    if remaining % 3 != 0:
        continue
    x = remaining // 3
    if x < 0 or x + y > n:
        continue
    total = prefix_max4[y]
    if y + x <= n:
        total += prefix_max3[y + x] - prefix_max3[y]
        total += prefix_sum[n] - prefix_sum[y + x]
    else:
        continue
    if total < min_swaps:
        min_swaps = total

if min_swaps != float('inf'):
    print(min_swaps)
else:
    print(-1)
```
