<think>
Okay, let's try to figure out this problem. So the task is to find the minimal number of copy operations needed so that every row from table A and every row from table B ends up in the same partition. The key here is to ensure that for each pair of rows (a from A, b from B), there's at least one partition that contains both a and b. 

Hmm. Let's think about what's required. The partitions can be from either cluster. Wait, no. Wait, the problem statement says that table A is distributed on the first cluster (with m partitions) and table B is on the second cluster (n partitions). So the rows from A are in the first cluster's partitions, and the rows from B are in the second cluster's. But when performing operations, you can copy a row from any partition to any other. So, the final arrangement can have rows from both tables in any partitions, but the main thing is that every a and every b must coexist in at least one partition.

Wait, but the problem says: "At the end, for each row from A and each row from B there should be a partition that has both rows." So every a_i (a row from A) and every b_j (a row from B) must coexist in some partition. But the rows can be copied to multiple partitions. So the challenge is to arrange the copies such that this condition is met with the least number of copy operations.

So each copy operation is moving a single row from its current partition to another. The original rows are in their respective partitions. So for example, if a row from A's partition is copied to another partition, that counts as one operation. Similarly for B's rows.

The minimal number of operations would be the sum of all the copies made for A's rows and B's rows.

Wait, but how does the arrangement work? Let's think of it as follows. For each row in A and each row in B, they must be present in at least one common partition. So, for a particular partition, if it contains some a's and some b's, then all pairs of a's and b's in that partition are covered. But rows can be copied to multiple partitions. So the optimal way is to find for each row in A and B which partition(s) to copy them to, such that the coverage is complete, and the total copies are minimized.

Hmm. Let's model this. Let's say for each row a in A, we choose to copy it to some set of partitions (possibly including its original one), and similarly for each row b in B. Then, for every a and b, there must be at least one partition where a's copy and b's copy are both present.

Wait, but perhaps the original partitions can be used. Like, if a row is left in its original partition, then maybe that's part of the solution.

Alternatively, maybe the optimal approach is to choose a single partition for all rows. For example, if we copy all rows of A and B into one partition, then all pairs are covered, but that could be expensive. Or maybe there's a way to split the copies between the two clusters to minimize the total operations.

Let's look at the examples.

First example:
Input:
2 2
2 6 (A partitions)
3 100 (B partitions)

Output is 11. Explanation: move all A rows to B's second partition (so 2+6 =8 operations for A's rows), and move B's first partition's 3 rows to the same partition. So total 8+3=11. The B's second partition already has 100 rows, so no need to copy them. Then, all a's and b's are in the second B partition, so all pairs are covered.

Second example:
2 3
10 10 (A's partitions)
1 1 1 (B's partitions)
Output is 6. Here, each B row is copied to both A partitions. So each B's row is copied twice (since originally they are in their own partitions, which are in cluster B). So 3 B rows * 2 copies each = 6. Then, each A's partitions have all B rows. So all pairs are covered.

So what's the pattern here? It seems that for the minimal total operations, we need to choose a way to cover all pairs by having rows from A and B in certain partitions, such that the sum of copies is minimized.

Let's think of it in terms of selecting which partitions (from either cluster) will serve as the "meeting points" for the A and B rows. For each such partition, the rows from A and B that are copied here can cover all pairs between them. However, since pairs can be covered in different partitions, perhaps the optimal approach is to have all A rows copied to a certain set of partitions, and all B rows copied to another set, such that for each A partition and B partition in their respective sets, there's at least one common partition where they are both copied. Hmm, not sure.

Alternatively, the key is to model this as a bipartite graph where the rows of A and B are nodes, and edges represent the need for them to coexist in some partition. But that's probably not helpful for large m and n.

Wait, but the problem is not about individual rows but about the sum. Because all rows in a partition can be treated as a group. For example, all a_i rows in partition i of A can be handled as a single entity. Similarly for B.

So perhaps the solution can be found by considering the sum of the rows in A and B. Let's see:

For all rows in A, the minimal copies needed is sum_A = sum(a_i) * x, where x is the number of copies each row in A must make. Wait, no. Wait, each row in A's original partition must be copied to some number of partitions. But this might vary per group. For example, if all a_i are copied to k partitions, then each contributes a_i * (k-1) operations (since original is already there). Wait, no: each a_i is in its original partition. So if you need to copy a_i's rows to another partition, each copy is one operation. So if a partition's a_i is copied to k partitions (including original?), then the number of operations is a_i * (k) (if original is not counted). Or wait, the original partition is part of the first cluster (for A), so the rows are already there. So when you copy a row from A's partition to another (could be in any cluster), each copy counts as one operation. So for a_i, if you need to copy them to x partitions (other than their original?), the cost is a_i * x. Or maybe the original can be used as a target for B's rows. So perhaps the rows from A can stay in their original partitions, but B's rows need to be copied to some of the A's partitions, or vice versa.

Alternatively, here's an approach. Let's say that for each row in A, we choose to copy it to some partitions. For each row in B, same. But the condition is that for every a_i (original in A's cluster) and every b_j (original in B's cluster), there must be at least one partition where both a_i's copy and b_j's copy exist.

So, the problem reduces to choosing for each a_i a set of partitions S_Ai, and for each b_j a set of partitions S_Bj, such that S_Ai ∩ S_Bj is non-empty for all i, j. And the total cost is sum over all a_i * (|S_Ai| - 1) (since original is already present) plus sum over all b_j * (|S_Bj| - 1). Wait, no. Because the original partitions are part of the clusters. Wait, no. Wait, the original a_i is in a partition of cluster A, which is in the first cluster. The original b_j is in a partition of cluster B. So for the rows to be in the same partition, they must be copied to some partition (could be any, including original ones). So, for example, if a_i remains in its original partition and b_j is copied there, then that's okay. Similarly, if a_i is copied to a partition in B's cluster and b_j remains there, etc.

But the cost is the total number of copies. Each copy of a row from A's original partition to another (could be same cluster or other) counts as a copy. Similarly for B's rows. So, for each a_i, if you have it in k partitions (including original?), then the copies made are (k-1) times a_i, because original is already present. Similarly for b_j.

But the problem statement says that you can copy a row from any partition to any other. So if a row is in multiple partitions, each copy (except the original) is an operation.

So, the initial setup is that each a_i is in their original partition (A's cluster), and each b_j is in their original partition (B's cluster). The copies are required to have, for every a_i and every b_j, at least one partition where both a_i and b_j are present. 

So the problem is to find for each a_i and b_j, a set of partitions such that their intersection is non-empty. But the way to minimize the total copies.

Hmm. Let's model this as a bipartite graph between the A partitions and B partitions. Each edge represents a possible partition where a copy from A and B can meet. For example, if a_i's copies are in some partitions, and b_j's copies are in some partitions, then their sets must have at least one common partition.

But how to model this for all possible a_i and b_j pairs. Wait, but the a_i and b_j are grouped by their original partitions. For example, all a_i rows in partition x of A can be handled as a group. Similarly for B.

Wait, but maybe the optimal solution is to have all a_i's copied to a certain set of B's partitions, and all b_j's copied to a certain set of A's partitions. Or perhaps the other way around.

Alternatively, perhaps the minimal cost is achieved by choosing one partition from A and one from B, and then merging them in some way. Or perhaps it's better to copy all A rows to one B partition, and all B rows to one A partition. Wait, let's think.

For instance, in the first example:

A partitions are 2 and 6. B partitions are 3 and 100.

The optimal solution is to copy all A rows to B's second partition (which has 100). Then, copy B's first partition (3) to B's second. So all A and B rows are in B's second partition. The cost is (2 +6) copies for A's rows (each row is moved once to B's second partition) plus 3 copies for B's first partition. B's second partition is already present, so no cost. So total 8 +3=11.

But why not choose a different approach. For example, copy all B's rows to A's second partition. Let's see. B's 3 and 100 rows would be copied to A's second partition. That would cost 3+100 = 103. Then, the A's first partition (2) would need to be copied to that same partition, adding 2. So total 103 +2 +6 (since A's second is already there). Wait, no: original A's second has 6 rows. If we copy all B's rows to A's second, then for all a_i and b_j, they meet in A's second partition. The cost would be (3+100) for B's rows (each copied once) plus for A's first partition (2), which must be copied to A's second partition (cost 2). So total 3+100 +2 +6 (since original A's second is already there). Wait, no: the original A's rows are in their own partitions. So for the 6 rows in A's second partition, they are already present. So the cost for A's rows is 2 (copied to A's second) and 0 for the 6. So total A cost is 2. B cost is 3+100=103. Total 105, which is worse than the example's solution of 11.

So clearly, choosing which partitions to copy to can have a huge impact. So the key is to find the best way to arrange the copies such that the total cost is minimized.

Hmm. Let's think of the problem in terms of selecting a subset of partitions (from either cluster) where all A and B rows must be present. Wait, no. Because rows can be in multiple subsets. For example, in the second example, the solution was to copy all B's rows to both A's partitions. So each B's row is copied to two partitions. So the A's rows (10 and 10) are in their original partitions, and the B's rows are copied to both. So for any a_i (from A) and any b_j (from B), they meet in the a_i's original partition, since B's row is copied there.

So the problem is to find, for each a_i (original partition in A) and each b_j (original in B), a common partition where both are present. So for each a_i and b_j pair, there's at least one partition where a_i is present (either original or copied) and b_j is present (original or copied).

But considering that each a_i and b_j is part of multiple pairs, how can we model this efficiently?

Alternative approach: Let’s model this as choosing a set of partitions where certain A and B rows are copied. The minimal total cost is to find for each A partition, how many copies of its rows to make, and for each B partition, how many copies to make, such that for each pair of A and B partitions (original), there exists at least one partition where both the A's and B's copies are present.

Wait, but each original A partition has a certain number of rows. For example, suppose we have A partition x with a_x rows. These rows can be copied to any number of partitions (including zero, which would mean they are only in their original). Similarly for B's partitions. The problem is that for each original A partition x and original B partition y, there must be at least one partition where at least one copy of x's rows and one copy of y's rows are present.

So the problem is equivalent to ensuring that for every x in 1..m and y in 1..n, the sets of partitions that x's rows are copied to and y's rows are copied to have a non-empty intersection.

The total cost is sum over x (a_x * (k_x - 1)) + sum over y (b_y * (l_y - 1)), where k_x is the number of copies (including original) for a_x's rows, and l_y is the number of copies for b_y's rows. Because each copy after the original costs one per row.

So the goal is to choose k_x and l_y for all x and y, such that for each x and y, the intersection between the set of partitions where a_x's rows are present and the set where b_y's rows are present is non-empty. And the sum is minimized.

Hmm. But how to model this. This seems very abstract. Let's think of possible strategies.

One possible strategy is to choose a single partition where all a_x's rows are copied to, and all b_y's rows are copied to. Then, all pairs (x,y) are covered because they meet in that partition. The cost in this case would be (sum a_x) * (1) (since each a_x is copied once to this partition, except for the one that's already there if the partition is from A) plus sum b_y * (1) (copied once to this partition, except if the partition is from B). Wait, but the choice of the partition (whether it's from A or B) affects the cost.

For example, suppose the chosen partition is from A. Then, for all a_x's (including the one in the chosen partition), they need to be copied to that partition. So the cost for a_x's is sum (a_x) * (0 if x is the chosen partition, else 1). For the B's rows, they all need to be copied to that partition, so each contributes 1 * b_y. So total cost is sum (a_x * (x != chosen)) + sum (b_y * 1).

Alternatively, if the chosen partition is from B, then the a_x's must be copied to that partition (each a_x contributes 1 * a_x), and the b_y's are copied once except for the chosen one. So sum (a_x) * 1 + sum (b_y) * (y != chosen).

So which is better depends on the sums of a and b. For example, if sum(a) is much smaller than sum(b), then choosing a B partition where the sum of b is minimized would be better.

Wait, but the minimal sum in this strategy is the minimum between (sum_a - a_x) + sum_b (if x is a A partition) and sum_a + (sum_b - b_y) (if y is a B partition). Because, for example, if the chosen partition is x in A, then the a_x doesn't need to be copied (since it's already there), so the cost is sum_a - a_x (for the other a's) plus sum_b (since all B's must be copied to x). 

So the minimal possible with this strategy is min( (sum_a - max_a) + sum_b, sum_a + (sum_b - max_b) ). Where max_a is the maximum a_x, and max_b is the maximum b_y.

So the first term is when we select the A partition with maximum a_x. The sum_a - max_a is the cost for copying all other A partitions to it, plus sum_b (copying all B partitions to it). The second term is when selecting the B partition with maximum b_y, so sum_b - max_b is saved, but sum_a is copied to it.

So comparing these two options gives a candidate for the minimal cost.

But perhaps there's a better strategy. For example, in the second example, the solution wasn't to choose a single partition, but to have each B row copied to two partitions (both A's partitions). So the total cost was 3 rows * 2 copies each = 6. The A's partitions didn't need to be copied. So the sum_a *0 (since they are all in original) plus sum_b * (2) (each copied twice). But in this case, the sum of a is 20 (10+10), sum of b is 3 (1+1+1). So the strategy of selecting a single partition would have a cost of (20) + (3 - max_b). But max_b is 1, so 20 + 2 = 22, which is worse than 6. So this strategy is better.

So the previous approach of choosing a single partition isn't sufficient. So what's the better strategy here?

The second example's solution is that each B's row is copied to both A's partitions. So for each B row, two copies (original in B's partition, so 2 copies (copied to two A's partitions) -> cost 2 per row). So for all B rows, 3 rows * 2 copies each = 6. The A's rows are in their original partitions, so no copies. Thus, for any pair of A's partition and B's row, since B's row is copied to both A's partitions, the A's rows (original in their partitions) and B's copies are present. So all pairs are covered.

So this strategy is better than the single partition approach. So in this case, the cost depends on the number of B rows and the number of A partitions. Because each B row must be copied to all A partitions. So the cost is sum_b * m (number of A partitions) - sum_b (since each B row was originally in their own partitions, and now copied to m partitions (A's m partitions)). Wait, no. The original B rows are in their own partitions, so to copy them to all m A partitions, each B row must be copied m times. So for each B row, m copies, leading to sum_b * m.

But in the second example, sum_b is 3 (1+1+1), m=2. So 3*2=6, which matches the example. But in that case, the cost is sum_b * m. The A's rows are not copied, so their cost is zero. So total cost is 6. Which is better than the single partition approach.

So this suggests another possible strategy: copy all B's rows to all A's partitions. Then, the cost is sum_b * m. Then, since all A's rows are in their original partitions, and B's rows are copied to all of them, all pairs are covered. Similarly, another possible strategy is to copy all A's rows to all B's partitions. The cost here would be sum_a * n. Then, all B's rows are in their original partitions, and A's are copied to all B's partitions. So which of these strategies is better?

For the second example, sum_b * m is 3*2=6, which is the correct answer. Sum_a *n is 20*3=60, which is worse. So the first strategy is better.

But how do we choose between these possible strategies?

So possible strategies to consider are:

1. Choose a single partition (A or B) and copy all other rows to it.
   - Cost is (sum_a - max_a) + sum_b (if A partition is chosen)
   - Or sum_a + (sum_b - max_b) (if B partition is chosen)
2. Copy all B's rows to all A's partitions. Cost is sum_b * m.
   - This ensures that for each A partition, all B rows are present. So pairs are covered.
3. Copy all A's rows to all B's partitions. Cost is sum_a * n.
4. Find some combination of these strategies. For example, copy all B's rows to some A partitions, and copy some A's rows to some B partitions.

But how to find the minimal sum among all possible options.

So, the minimal cost is the minimum among the following four options:

Option1: Choose a single A partition (the one with maximum a_x) and copy all other A's to it, and all B's to it. Cost = (sum_a - max_a) + sum_b.

Option2: Choose a single B partition (the one with maximum b_y) and copy all other B's to it, and all A's to it. Cost = sum_a + (sum_b - max_b).

Option3: Copy all B's to all A's partitions. Cost = sum_b * m.

Option4: Copy all A's to all B's partitions. Cost = sum_a * n.

Then, the minimal of these four options is the answer.

But why are these the only options? Because there might be other possibilities. For example, maybe copy some B's to some A's partitions, and some A's to some B's partitions. But in that case, the cost could be sum_b * k + sum_a * l, where k is the average number of copies per B row, and l is the average for A rows. But how to ensure that all pairs are covered.

Alternatively, perhaps the minimal cost is the minimum between the four options above.

Let's test this hypothesis with the examples.

First example:

Option1: sum_a is 8 (2+6), max_a is6. So cost (8-6) + sum_b (103) = 2+103=105. Option1 is 105.

Option2: sum_b is 103, max_b is100. So cost is sum_a (8) + (103-100) = 8+3=11. Which matches the example's answer.

Option3: sum_b * m =103*2=206.

Option4: sum_a *n=8*2=16.

So the minimal is 11.

Which is correct.

Second example:

Option1: sum_a=20, max_a=10. cost (20-10) + sum_b(3) =10+3=13. Which is higher than the example's answer.

Option2: sum_b=3, max_b=1. cost sum_a (20) + (3-1) =20+2=22.

Option3: sum_b *m=3*2=6. Which matches the example.

Option4: sum_a *n=20*3=60.

So minimal is 6.

Thus, the answer is indeed the minimum of these four options.

Another test case: Let's say m=1, n=1. Then, the required is zero copies because the single A and B partitions are already in the same place? Wait, no. Wait, in this case, the A's rows are in their own partition (in cluster A), and B's rows are in their own partition (cluster B). So to have all pairs covered, we need to have at least one partition where both are present. So either copy the A's to B's partition, or B's to A's. So cost is min( a *1 + b*0, a*0 + b*1 ) = min(a, b). For example, if a=5 and b=3, then option is to copy B to A's partition, cost 3.

So according to the four options:

Option1: (sum_a - max_a) + sum_b. sum_a is 5, max_a is5. So 0 +3=3.

Option2: sum_a + (sum_b - max_b). sum_a=5, sum_b=3, max_b=3. 5+0=5.

Option3: sum_b * m=3 *1=3.

Option4: sum_a *n=5*1=5.

So the minimal is min(3,5,3,5) =3. Which is correct.

So in this case, options1 and3 are same. So the minimal is 3.

So the approach of taking the minimal of the four options seems to work.

Another test case: m=1, n=2. A has sum a=10. B has two partitions, 1 and 1.

Possible options:

Option1: max_a is10. So cost (10-10) + sum_b (2) = 0+2=2.

But that requires copying all B's to the single A partition. Because in option1, when we choose the A partition, all B's are copied to it. So sum_b (1+1) =2. So cost 2.

Option3: sum_b * m =2*1=2.

So same as option1 and3.

Thus, the answer is 2.

So this seems to hold.

So the conclusion is that the minimal possible cost is the minimum among the four options:

1. (sum_a - max_a) + sum_b: choose the A partition with largest a_i, copy all other A's to it, and all B's to it.

2. sum_a + (sum_b - max_b): choose the B partition with largest b_i, copy all other B's to it, and all A's to it.

3. sum_b * m: copy all B's to each A partition.

4. sum_a *n: copy all A's to each B partition.

So the answer is the minimum of these four values.

So the steps to solve the problem are:

1. Calculate sum_a and sum_b.

2. Find the maximum a_i (max_a) and maximum b_i (max_b).

3. Compute the four options:

   a. option1 = (sum_a - max_a) + sum_b.

   b. option2 = sum_a + (sum_b - max_b).

   c. option3 = sum_b * m.

   d. option4 = sum_a *n.

4. The minimal of these four is the answer.

So the code can be structured as follows:

- Read m and n.

- Read list a, compute sum_a, max_a.

- Read list b, compute sum_b, max_b.

- Compute the four options and choose the minimal.

But wait, in the first example, option2 was sum_a (8) + (sum_b (103) - max_b (100)) =8 +3=11.

Yes.

But let's check what if sum_b - max_b is zero, like if all b are same. For example, m=2, n=2. a = [5,5], b=[5,5]. Then sum_a=10, sum_b=10. max_a=5, max_b=5. option1= (10-5)+10=15. option2=10 + (10-5)=15. option3=10*2=20. option4=10*2=20. The minimal is 15. But is there a better way?

But according to the problem, the correct approach is to copy all other a's to the largest a partition (but all a's are same here) and all B's. Or perhaps copy all B's to the largest B. But perhaps the minimal is indeed 15.

But perhaps the best approach is to choose one partition from A and one from B, and copy all A's and B's to those two. But that might not be allowed. Wait, no. Because the requirement is that for each a and b pair, there's at least one common partition. If we copy all A's to partition A1 and all B's to partition B1, then pairs (a in A1 and B in B1) would not have a common partition. Unless there's a third partition where both are copied. So the previous four options cover all possible minimal scenarios.

Thus, the code can proceed by calculating the four options and output the minimum.

So in code:

Read m, n.

Read a list, sum_a = sum(a), max_a = max(a).

Read b list, sum_b = sum(b), max_b = max(b).

Compute the four options:

option1 = (sum_a - max_a) + sum_b.

option2 = sum_a + (sum_b - max_b).

option3 = sum_b * m.

option4 = sum_a * n.

result = min(option1, option2, option3, option4).

Print result.

Yes. Let's test the first example:

option1: (8-6) +103 = 2+103=105.

option2:8 + (103-100) = 11.

option3:103*2=206.

option4:8*2=16.

min is 11. Correct.

Second example:

option1: (20-10) +3 =13.

option2:20 + (3-1)=22.

option3:3*2=6.

option4:20*3=60. min is 6.

Another test case: m=1, n=1.

sum_a = a, sum_b = b.

option1: (a -a) +b= b.

option2: a + (b -b) =a.

option3: b*1 =b.

option4: a*1 =a.

min is min(a, b). Which is correct.

Another case: m=3, n=2.

sum_a=5, sum_b=7.

max_a=3, max_b=5.

option1= (5-3) +7=2+7=9.

option2=5 + (7-5)=5+2=7.

option3=7 *3=21.

option4=5*2=10.

The minimal is 7.

But what is the actual approach here? According to option2, sum_a (5) plus sum_b -max_b (7-5=2) is 7. So copying all B's to the max_b partition (which has 5), and all A's to that partition. So cost sum_a (since all are copied to B's partition) plus (sum_b -max_b) (other B's are copied to it). So total 5 +2=7. Which would mean that all A's are copied to the B's max partition, and all B's except the max are copied to it. Then, the pairs between A and other B's would be covered in that partition.

Yes.

Thus, the code seems to correctly compute the minimal.

Thus, the code can be written as follows.
</think>

```python
def main():
    import sys
    input = sys.stdin.read().split()
    m, n = map(int, input[:2])
    a = list(map(int, input[2:2+m]))
    b = list(map(int, input[2+m:2+m+n]))
    
    sum_a = sum(a)
    sum_b = sum(b)
    max_a = max(a)
    max_b = max(b)
    
    option1 = (sum_a - max_a) + sum_b
    option2 = sum_a + (sum_b - max_b)
    option3 = sum_b * m
    option4 = sum_a * n
    
    print(min(option1, option2, option3, option4))
    
if __name__ == "__main__":
    main()
```