<think>
Okay, let's tackle this problem. So, the problem is about children lining up and getting candies until they have enough. The last child to leave is the one we need to find. Hmm.

First, I need to understand the process. The algorithm steps are: give m candies to the first child in the line. If after that, the child has enough (i.e., their ai is satisfied), they leave. Otherwise, they go to the end of the line. Repeat until the line is empty. The last child to leave is the answer.

The constraints are n up to 100, m up to 100, and each ai up to 100. So with n=100, even if each step takes O(n) time, the total steps would be manageable. But maybe there's a smarter way than simulating each step.

Wait, but even if we simulate, for each child, how many times would they go through the line? Let's see. Each time a child is at the front, they get m candies. So for a child with ai, the number of times they need to be at the front is ceil(ai / m). Each time, they get m, so after k times, they have k*m. So the first k where k*m >= ai is the number of times they need to receive m candies. Then, the order in which they leave depends on when their required number of m's is completed.

Wait, but the process is that each time a child is processed, if they get enough, they leave. Otherwise, they go to the end. So the order in which the children leave is determined by how many full m increments they need. For example, a child with ai=5 and m=2 would need 3 steps (2, 2, 1). Wait no, because each time they get 2. Wait, the first time they get 2 (total 2, which is less than 5), so they go to the end. Second time, they get another 2 (total 4), still less. Third time, they get 2 (total 6). Now 6 >=5, so they leave. So that's 3 steps. So for ai=5, m=2: (5 + m -1) // m = (5+2-1)/2=6/2=3. So the number of rounds is ceil(ai / m). But how does that determine the order in which they leave?

Each time a child completes their required steps (k steps), they leave. The child who has the maximum k (ceil(ai/m)) will be processed last. But if multiple children have the same maximum k, then the last among them in the original order (or in the line processing) will be the last.

So, the solution is to compute for each child the number of times they need to receive m candies (k_i = ceil(a_i/m)), and then find the child with the maximum k_i. If there's a tie, the last such child in the original order is the answer.

Wait, let's test this with the first example.

Sample Input 1:

5 2

1 3 1 4 2

The a_i are 1,3,1,4,2.

Calculating k_i for each:

a_i=1: ceil(1/2) = 1. So after 1 step, done.

a_i=3: 3/2=1.5 → ceil is 2. So 2 steps.

a_i=1: 1.

a_i=4: 4/2=2 → 2 steps.

a_i=2: 2/2=1 → 1 step.

So the k_i are [1,2,1,2,1]. The maximum is 2. Which children have k=2? Children 2 and 4. The original order is 1,2,3,4,5. So among children 2 and 4, which one is processed last?

In the sample explanation, the last child was 4. So according to the approach, since 4 is the last among the ones with maximum k_i (children 2 and 4), that's the answer.

In sample 2:

Input:

6 4

1 1 2 2 3 3

So m=4. Each a_i divided by 4:

1: ceil(1/4)=1

1: 1

2:1 (ceil(2/4=0.5) is 1)

2:1

3: ceil(3/4) is 1.

3:1.

All k_i are 1. So the maximum is 1, and all have the same. So the last child in the original order (6) is the answer. Which matches the sample.

So this approach seems to work.

Thus, the algorithm would be:

1. For each child, compute k_i = ceil(a_i / m).

2. Find the maximum k among all k_i.

3. Among all children with k_i equal to the maximum, select the one with the highest index (original position) because that's the one which would be processed last in their group.

So, in code:

Read n, m.

Read a list.

Compute for each element a_i in the list, the k_i = (a_i + m -1) // m.

Find the maximum k.

Then iterate through the list from the end to the beginning, and find the first (i.e., last in original order) index where k_i equals the maximum. The index+1 (since children are numbered from 1) is the answer.

This approach is O(n) time, which is very efficient even for n up to 1e5, but here n is 100. So this is optimal.

So, the code steps:

Read n, m.

Read list a.

Compute max_k = maximum of ( (a[i] + m -1) // m for i in 0..n-1 )

Then, loop through the list from end to start, find the first i where (a[i] + m -1) // m == max_k. Return i+1.

Yes. Because among all children with the maximum k_i, the last one in the original list is the one that will be processed last. Because during the simulation, children with higher k_i require more rounds, and if two children have the same k_i, the one that appears later in the original list will be the one that is last to complete their rounds. Wait, perhaps not. Let's think.

Wait, for example, suppose two children have same k_i. Which one will be processed last?

Suppose child A has k=2 and is first in the original order. Child B has k=2 and is second.

In the first round, A gets m, but after the first m, since k=2, A needs another round. So they go to the end. Then B is processed. B gets m, and their k=2, so they go to the end. Then next, the line would be [ ... , A, B]. Then when they come around again, A gets m again, which satisfies their total. Then B would get their second m, and leave. So between A and B with same k_i, the one who was earlier in the original order would leave first. Because B was added after A in the first step. Wait, but during the first processing:

Original line is A, B.

A gets m, but since k=2, he needs to go to the end. Now line is B, A.

Then B gets m, same k=2, so line is A, B.

Then A gets m again (total 2*m), leaves. Then B gets m again, leaves. So B leaves after A.

Wait, so for two children with same k_i, the one that is later in the original order would be the last to leave. Because in the first pass, A (original first) gets processed first. Then after going to the end, B is processed, and goes to the end. Then in the next cycle, A is processed again, leaving. Then B is processed again, leaving. So B is last.

Wait, but the original order is A (i=1), B (i=2). So their k_i are same. So according to our code approach, the one with higher index (i=2) would be chosen as the last. Which matches the simulation.

So the code approach is correct.

Thus, the code can be written as:

Read n, m.

a = list of ai's.

Compute for each ai, k_i.

Find max_k.

Loop from the end of the list to the start, find the first (i.e., last) index where k_i == max_k. Return index + 1.

This is O(n) time and O(1) space. So for n=100, it's optimal.

So the code is straightforward.

Testing the first sample:

Sample 1:

n=5, m=2.

a = [1,3,1,4,2]

Compute k_i:

1: (1+2-1)//2 = 2//2=1

3: (3+2-1)/2=4/2=2

1: 1.

4: (4+2-1)/2=5//2=2.5 → 2.5 floored to 2? Wait, no. (4+1)/2 is 5/2=2.5, integer division in Python gives 2. So ceil(4/2) is 2. So yes.

Wait, (a_i + m -1) // m is the formula for ceil(a_i / m). So for 4, (4+1) //2 =5//2=2. Which is correct.

So k_i's are [1,2,1,2,1]. max_k=2.

Looking from the end, the first occurrence of 2 is at index 3 (0-based), which is child 4. So correct.

Sample 2:

n=6, m=4.

a = [1,1,2,2,3,3]

Each a_i +3 (4-1) divided by4:

(1+3)/4=1 → 1.

Same for all others. So max_k=1.

Looking from the end, the last child (index 5, which is 6th) is the answer.

Yes.

Another test case: if all have same k_i, then the last one in the list is the answer.

So code works.

Thus, the code is as follows.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
max_k = 0
last_idx = 0
for i in range(n):
    k = (a[i] + m - 1) // m
    if k >= max_k:
        max_k = k
        last_idx = i
print(last_idx + 1)
```