<think>
Okay, let's try to figure out this problem. So the task is to find the minimal sum u + v + w such that all elements in the union of a, b, and c are covered by the first u elements of a, first v of b, and first w of c. Hmm.

First, I need to collect all unique elements from the three arrays. Then, for each element in this union, it must appear in at least one of the first u elements of a, first v of b, or first w of c. Our goal is to choose u, v, w such that this condition is satisfied, and their sum is minimized.

The approach here probably involves tracking the earliest occurrence of each element in each array. Then, for each element, we need to select the earliest position in one of the arrays where it appears. But how do we combine these choices across all elements to minimize the sum u + v + w?

Wait, maybe for each element x in the union, we can note the earliest positions in a, b, c where x appears. Then, the minimal u, v, w would have to cover all elements by choosing for each x the earliest possible in one of the arrays. But how to choose for all elements such that the maximum u, v, w required across all their choices is as small as possible in sum?

Alternatively, perhaps we can model this as choosing for each element x which array (a, b, or c) it will be covered by, such that for that array, the earliest occurrence of x in that array's prefix. Then, the required u is the maximum of all the positions chosen for elements in a, similarly for v and w. The sum of these three maxima would be the total sum we need to minimize.

Wait, that makes sense. For example, if we decide that all elements are covered by their earliest occurrence in a, then u would be the maximum of all their earliest positions in a. But then v and w can be 0. Similarly, if some elements are covered by a, some by b, some by c, then u is the max of the positions chosen for a's elements, v for b's, etc. The sum of these three maxima is the total. So the problem reduces to selecting for each element x a choice of which array (a, b, or c) to use, such that the sum of the three maxima (for each array) is minimized.

But how do we efficiently find such a selection?

This seems like a problem where we need to find, for each element, the best array to assign it to (the one where its earliest occurrence is as small as possible, but also considering how that affects the max for each array). However, since the sum of the maxima is what's being minimized, this might be tricky.

Another angle: For each element x, we can precompute the earliest occurrence in each array. Let's say for x, we have a_pos[x] as the earliest index (1-based or 0-based? Need to check) in a where x appears, and similarly b_pos and c_pos. If an element doesn't appear in an array, maybe we treat its position as infinity.

Wait, but the arrays a, b, c might have elements that are not present in other arrays. But the union is all elements that appear in any of the arrays. So for each element in the union, we need to find the earliest occurrence in any of the arrays. But the problem allows us to choose which array's prefix covers each element.

So for each element x, the earliest possible position where x appears in a is a_pos[x], which is the minimal index in a where x is found. Same for b and c. For example, if x is in a at index 2 and 3, a_pos[x] is 2 (assuming 0-based or 1-based? Need to clarify).

Wait, the problem says "the first u elements of a". So u is the number of elements considered. For example, u=3 means the first three elements. So if x is in the first u elements of a, then a's array up to u includes x. So for each x in a, the earliest occurrence is the first index (starting from 0 or 1) where x appears, but u has to be at least that position +1 (if 0-based) or the position (if 1-based). So for example, if a is [5, 3, 5], then the first occurrence of 5 is at index 0 (0-based), so u needs to be at least 1 (since the first 1 elements include index 0). Similarly, 3 is first at index 1, so u needs at least 2.

So for each array, we need to precompute for each element x in the union, the earliest position in that array (1-based) where x occurs. If x is not present in the array, then the position is infinity (or some large number). So for x in the union, the possible options are:

For a: earliest occurrence is the smallest index (1-based) in a where x appears, or infinity if not present.

Same for b and c.

Then, for each x in the union, we can choose which array (a, b, c) to take its earliest occurrence. The u is the maximum of all the a_pos[x] chosen for x's that are assigned to a. Similarly for v and w. The sum of u, v, w is what we need to minimize.

So the problem becomes: assign each x in the union to a, b, or c, such that for each array, the maximum of the positions of x's assigned to that array is the smallest possible sum when adding those three maxima.

Hmm. How can we model this? It's a bit like a resource allocation problem where each x can be assigned to one of three resources, and each resource's cost is the maximum of the positions of the x's assigned to it. The total cost is the sum of these three maxima, which needs to be minimized.

This seems like a problem where we need to consider all possible combinations of possible maxima for a, b, c. But with the size of n up to 1e5, this approach is not feasible.

Alternative idea: For each element x, we can choose the array where its earliest occurrence is the smallest. Then, for that array, the maximum of all such x's earliest occurrences would contribute to the sum, along with the others. But this may not be optimal. Because maybe choosing a slightly higher position for some x in another array allows the sum to be smaller overall.

Wait, for example, imagine two elements. The first element has a_pos=2, b_pos=3, c_pos=4. The second element has a_pos=4, b_pos=3, c_pos=2. If each is assigned to their minimal, then the first is a (max a is 2), second is c (max c is 2). Sum would be 2 (a) + 0 (b) + 2 (c) =4. But if we assign first to a (2), second to b (3). Then sum is max a=2, max b=3, max c=0. Sum is 5. So the initial approach gives a better sum. But maybe another example where the sum is better if some elements are assigned to non-minimal positions.

So the greedy approach of choosing the minimal earliest for each element may not lead to the optimal sum. Because the sum is the sum of the maxima. So maybe there's a way to balance the maxima across the three arrays.

This feels like a problem where we need to find for each possible candidate a_max, b_max, c_max, whether there exists a way to assign elements such that all elements assigned to a have their a_pos <= a_max, those to b <= b_max, etc., and a_max + b_max + c_max is minimized.

But how do we efficiently check this?

Alternatively, perhaps we can precompute for each array the possible thresholds (like a_max) and find the combination of a_max, b_max, c_max such that all elements can be covered by at least one array's threshold, and the sum a_max + b_max + c_max is minimized.

But even that seems challenging.

Alternative approach: For each element x, collect the three possible positions (a, b, c). Then, for each element x, the minimal possible contribution to the sum is the minimal of a_pos, b_pos, c_pos. But since the sum is the sum of the maximum for each array, perhaps we can model this as trying to select for each array the elements that will be covered by it, such that the maximum of their positions is as small as possible, but also the sum of the three maxima is minimized.

But how to model the interactions between these choices?

Alternatively, think of the problem as a three-dimensional space where each axis represents the maximum for a, b, c. We need to find the point (u, v, w) where for every element x in the union, x is covered by a's u, or b's v, or c's w. And the sum u + v + w is minimized.

The challenge is to find the minimal sum in this space.

But how to efficiently explore this space? The possible values of u, v, w could be up to 1e5 each, leading to a very large search space.

Alternative idea: For each element x, we can compute the minimal possible sum when x is covered by a, b, or c. But this seems too vague.

Another angle: Since the sum is to be minimized, perhaps the optimal solution would involve setting u, v, w such that they are as balanced as possible. For example, if one array's maximum is large and the others are small, perhaps a better balance can reduce the sum.

But how to find this balance.

Alternatively, for each possible a_max (from the earliest positions in a), compute the minimal possible b_max and c_max such that all elements not covered by a's a_max are covered by b's b_max and c's c_max. Then, the sum is a_max + b_max + c_max. Then, find the minimal sum over all possible a_max. Similarly, we can do the same for varying b_max and c_max.

But given that the arrays are up to 1e5 elements, trying all possible a_max is O(n), and for each a_max, we have to process all elements not covered by a's a_max and determine the minimal b_max and c_max. This might be feasible if we precompute the earliest positions and can quickly find the elements not covered by a_max.

But even that might be O(n) per a_max, leading to O(n^2) time, which is not feasible for n=1e5.

So this approach may not work.

Hmm. Let's think of another way. Maybe for each array, precompute all the positions in sorted order. For example, in array a, the elements are in order, and for each x in a, the first occurrence is the earliest. So for each array a, we can create a dictionary that maps x to the earliest position (1-based index) where it appears.

Similarly for b and c.

Once we have these dictionaries, for each x in the union, we can get the earliest positions in each array. Then, for each x, the possible choices are which array's earliest position to use. But since each x can be covered by any of the three, we need to choose which arrays' positions are considered.

Wait, but the problem is that the choice for x affects the maxima for a, b, c. So the sum is the sum of the maxima of the chosen positions for each array.

So the key is to assign each x to one of the arrays such that the sum of the maxima of each array's assigned x's positions is minimized.

This feels like a problem where dynamic programming might be possible, but I'm not seeing it.

Alternative idea: The minimal sum is achieved when for each x, we choose the array (a, b, or c) where x's earliest occurrence is the smallest possible. Then, for each array, the maximum of the chosen positions for that array is found, and their sum is computed. However, this might not give the minimal sum because the sum of the maxima could be larger than if some elements are assigned to non-optimal arrays to allow for a lower sum of maxima.

But perhaps this is the best starting point.

Let's take an example. Suppose x can be covered by a with position 3, or by b with position 2, or c with 5. The minimal individual is b (2). But if assigning x to a allows some other elements to have lower maxima in their respective arrays, perhaps leading to a lower sum overall.

But how to model this?

Alternatively, maybe the optimal solution is indeed to assign each x to the array where it's earliest possible. Let's see the first example:

Sample Input 1:
3
1 1 101
1 2 1
3 2 1

The union is {1, 101, 2, 3}.

For each element:
1: a's earliest is 1 (since first element is 1, 1-based), b's earliest is 1, c's earliest is 3 (array c is [3,2,1], first occurrence of 1 is at index 3 (1-based? Wait, array c is third line: 3 2 1. So in 1-based indices, positions are 1:3, 2:2, 3:1. So the earliest occurrence of 1 in c is position 3. So for x=1, the earliest positions are a=1, b=1, c=3. So choosing a or b would give position 1. Then, in the sample solution, u=3, v=0, w=2. Wait, how does that work?

Wait, in the sample input, the optimal choice is u=3 (all elements of a), v=0 (none of b), w=2. So for each element in the union:

- 1 is covered by a (since a's first u=3 elements include all a's elements, which includes 1's earliest occurrence at 1. So 1 is covered by a.

- 101 is in a's array. So u=3 covers all of a, so 101 is covered.

- 2 is in the first v=0 elements of b? No. Wait, perhaps it's covered by c's first w=2 elements. The c array is [3, 2, 1]. So the first 2 elements are 3 and 2. So 2 is in c's first 2 elements (position 2, 1-based). So 2 is covered by c's w=2.

- 3 is covered by c's first 2 elements (position 1). So 3 is covered.

So the sum is 3+0+2=5.

In this case, for element 1, it's covered by a (earliest 1), but perhaps in the optimal solution, some elements are not assigned to their earliest array to allow lower maxima in other arrays. Wait, in the sample, element 1 is covered by a's u=3, but a's earliest is 1. So u is 3 because another element (101) requires u to be 3. So even though 1 is covered by a's u=1, the 101 requires u=3. So the maximum of all the a's positions is 3. So when we assign x=1 to a (earliest 1) and x=101 to a (earliest 3), the a_max becomes 3.

So the sum is a_max (3) + b_max (0) + c_max (2) =5.

In this case, the minimal possible sum is achieved by considering the maximum of each array's required positions.

So the key is that for each array, the maximum of the positions of elements assigned to that array is the required u, v, or w.

So to minimize the sum of these maxima, we need to distribute the elements among the arrays such that the maxima are as small as possible.

But how?

An alternative approach: For each possible a_max, find the minimal b_max + c_max such that all elements not covered by a's a_max are covered by either b's b_max or c's c_max. Then, the sum would be a_max + b_max + c_max. We can iterate through all possible a_max, compute the minimal (b_max + c_max) for that a_max, and take the overall minimum. Similarly, we can do this for varying a_max, b_max, or c_max.

But how to efficiently compute the minimal (b_max + c_max) for each a_max?

Alternatively, for each element x, if we have to choose between a, b, or c, the a_max must be at least x's a_pos if x is assigned to a. Similarly for the others. So the problem is to choose for each x which array to assign to, such that for each array, the maximum of the assigned x's positions is as small as possible, and the sum of these maxima is minimal.

This seems like a problem that can be modeled as a graph where each node represents a possible a_max, b_max, c_max, but that's not feasible due to the size.

Alternative idea: Since each x can be assigned to a, b, or c, the optimal assignment for x is the array where x's earliest occurrence is minimal. However, the sum of the maxima may not be the minimal possible. But perhaps this is the best we can do.

Wait, but if all elements are assigned to their earliest possible array, then the sum of the maxima would be the sum of the maximum positions in each array. Let's think:

For each array, the maximum position is the maximum of all x's earliest positions in that array where x was assigned to it.

But this may not be the minimal sum. For example, if some elements in a's array have high positions, but moving some of them to other arrays (even if their earliest positions in those arrays are higher) may lower the sum.

But how to find such a scenario?

Let's take an example where:

Array a has elements [10, 20, 30], array b has [20, 30, 10], array c has [30, 10, 20]. So for each element:

- 10: a's earliest is 1, b's is 3, c's is 2.

- 20: a's earliest is 2, b's is 1, c's is 3.

- 30: a's earliest is 3, b's is 2, c's is 1.

If we assign each element to their earliest array:

- 10 → a (1), 20 → b (1), 30 → c (1). Then, a_max is 1, b_max is 1, c_max is 1. Sum is 3. Which is great.

But what if the elements were different. Suppose:

x's a_pos is 100, b_pos is 50, c_pos is 50.

y's a_pos is 50, b_pos is 100, c_pos is 50.

If we assign x to b (50), y to a (50). Then the sum is max(b's assignments: 50) + max(a's assignments:50) + c's 0. Sum is 50+50=100. But if we assign x to c (50), y to c (50), then sum is c_max 50 + a_max 0 + b_max 0. Sum is 50. Which is better.

So in this case, even though each element's earliest is in different arrays, assigning them to a single array's earliest (even though the individual positions are same) gives a better sum.

So the problem requires considering that sometimes, assigning elements to a common array, even if it's not their earliest, can lead to a lower sum.

So the key is to find a way to balance the maxima across the three arrays.

This suggests that the optimal solution may involve some trade-offs between the three arrays.

But how to compute this efficiently.

Alternative approach: For each element x, note the three possible contributions to the sum. For example, if x is assigned to a, it contributes a_pos[x] to a_max. Similarly for b and c.

The total sum is the sum of the maxima of each array's assigned positions.

But the problem is to choose for each x which array to assign to, such that the sum of the maxima is minimized.

This seems like an optimization problem with a lot of variables. However, the solution might have the following properties:

The sum is minimized when each array's maximum is the maximum of the assigned positions in that array, and the sum of these three maxima is as small as possible.

But how to model this.

Another idea: The minimal possible sum is the minimal possible value of (A + B + C) where:

A is the maximum of a positions of elements assigned to a,

B is the maximum of b positions of elements assigned to b,

C is the maximum of c positions of elements assigned to c,

and all elements are covered (each is in at least one of a's first A, b's first B, or c's first C).

So the problem reduces to finding the minimal A + B + C such that for every element x in the union, x is present in the first A elements of a, OR the first B of b, OR the first C of c.

The variables here are A, B, C. How do we find the minimal sum of these three variables such that all elements are covered by at least one of the arrays' prefixes.

This seems like a problem where we can perform a three-dimensional binary search, but that's probably not feasible.

Alternative approach: For each possible A, find the minimal B and C such that for all x in the union, x is in a's first A, or b's first B, or c's first C. Then, the sum A + B + C can be minimized over all possible A.

Similarly, we can iterate over possible values of A (from 0 to maximum possible a's earliest position), and for each A, compute the minimal B and C required. Then, take the minimal sum.

But how to compute B and C for a given A?

Once A is fixed, for each x not covered by a's A (i.e., a's earliest position of x is >A), then x must be covered by either B >= b's earliest position of x, or C >= c's earliest position of x.

So for these x's, the minimal B and C would need to cover them. So B must be at least the maximum of the b's earliest positions of x's not covered by A, and C must be at least the maximum of the c's earliest positions of x's not covered by A and B. Wait, but this is a bit more complicated.

Alternatively, for x not covered by A, x must be covered by B or C. So for these x's, we can choose to cover them by B or C. So the minimal B + C would be the minimal sum of B and C such that for each x not covered by A, either B >= x's b_pos or C >= x's c_pos.

The problem then becomes, for the remaining x's (those not covered by A), find the minimal B and C such that for each x in this subset, x is covered by B or C. The sum B + C should be as small as possible.

This seems like a two-dimensional optimization problem, but perhaps we can find B and C efficiently.

To find the minimal B + C for the remaining x's:

Each x in the remaining set must be covered by either B >= x's b_pos or C >= x's c_pos.

We need to choose B and C such that for all x in the set, x's b_pos <= B or x's c_pos <= C. And B + C is minimized.

How can we find such B and C?

This is similar to the problem where we have a set of pairs (b_x, c_x), and we need to choose B and C such that for each pair, either B >= b_x or C >= c_x. We need to find B and C with minimal sum.

This is a classic problem, and the solution is as follows:

The minimal sum B + C is the minimal value where for all x, max(B, required B's) + max(C, required C's) is minimized, but the constraints are that for each x, B >= b_x or C >= c_x.

To find this, we can note that for a given B, the minimal C required is the maximum of (c_x for x where b_x > B). Similarly, for a given C, the minimal B is the maximum of (b_x for x where c_x > C). So the optimal solution is to choose B and C such that B is the maximum of some subset of the b_x's, and C is the maximum of the remaining c_x's. So the sum B + C must be minimized.

The optimal B and C can be found by considering all possible B candidates from the sorted list of b_x's and c_x's. For each possible B, compute C as the maximum of c_x where b_x > B. Then compute B + C and find the minimal sum.

Similarly, we can do the same for varying C, but perhaps B is the main variable here.

To compute this efficiently, we can:

1. Sort the remaining x's by their b_pos in ascending order, and track the maximum c_pos in the suffix. So for each possible B (from the sorted list of possible b_pos's), the maximum c_pos for x's with b_pos > B is known.

2. For each possible B in the sorted list of b_pos's (including 0), compute C as the maximum of c_pos for x's where b_pos > B. The sum B + C is a candidate for the minimal sum.

3. The minimal sum over all these candidates is the minimal possible B + C for the remaining x's.

Additionally, we need to consider the case where B is set to 0. Then, C must be the maximum of all c_x's.

Similarly, if C is set to 0, B must be the maximum of all b_x's.

So, the steps for a fixed A are:

- Compute all x's not covered by A (a's earliest position for x is >A).

- For these x's, collect their b_pos and c_pos.

- If there are no such x's, then B and C can be 0, sum is A + 0 + 0 = A.

- Else, find the minimal B and C such that for each x in the subset, B >= b_pos or C >= c_pos. The minimal B + C is found as described.

This approach for each A would take O(m log m) time, where m is the number of x's not covered by A. But since n can be up to 1e5, and A can be up to 1e5, this approach would be O(n^2 log n), which is not feasible.

So, this approach is not efficient enough.

Alternative idea: Precompute for each array the earliest occurrence of each element. Then, for all elements x, collect the minimal possible a_pos, b_pos, c_pos.

But how to proceed.

Alternatively, let's precompute for each element x the possible candidates for a, b, c. For example, for x, the minimal a_pos, minimal b_pos, and minimal c_pos.

Then, for each element x, the minimal possible contribution to the sum is min(a_pos, b_pos, c_pos). But the problem is that these minima are for each individual x, but the sum is the sum of the maxima for each array.

Hmm. Let's think differently. Suppose that we have to choose for each x which array to cover it with. The sum is the sum of the maximum a_pos among x's covered by a, plus the maximum b_pos among x's covered by b, plus the maximum c_pos among x's covered by c.

We need to minimize this sum.

This is equivalent to partitioning the set of elements into three subsets (could be empty) S_a, S_b, S_c, such that every x is in at least one subset. The cost is (max_a(S_a) + max_b(S_b) + max_c(S_c)), where max_a(S_a) is the maximum a_pos of x in S_a (0 if S_a is empty), and similarly for others. We need to find the partition with the minimal cost.

This is the problem's core.

So how to model this?

This seems like a problem that requires considering all possible ways to split the elements into three groups. But with n up to 1e5, this is impossible.

Another approach: Since the sum is the sum of three maxima, perhaps the optimal solution will have the three maxima as small as possible, but balanced.

But how?

Perhaps the optimal solution is to choose for each x the array that gives the minimal position, but then adjust for overlapping maxima.

But again, this is not necessarily optimal.

Another angle: For each possible maximum of a, say a_max, what's the minimal sum of b_max and c_max required to cover all elements not covered by a_max. Then, the total sum would be a_max + b_max + c_max. We can then find the minimal sum over all possible a_max.

But how to find a_max in a manageable way.

The a_max can be any of the a_pos of the elements in a's array. Also, a_max could be 0 (cover none) but then all elements must be covered by b and c.

So, to find all possible a_max candidates, we can collect all the a_pos values of all elements in the union, plus zero.

But for large n, this could be up to O(n) candidates. But n is 1e5, and for each candidate, we need to process the remaining elements, which is O(n) per candidate. This leads to O(n^2), which is too slow.

But perhaps we can find that the optimal a_max is one of the a_pos values of the elements that are covered by a. So, maybe we can sort all possible a_max candidates in increasing order and use a sliding window approach.

Alternatively, what if we sort all elements by their a_pos in ascending order. Then, for each possible a_max in the sorted a_pos list, compute the required b_max and c_max for the remaining elements.

But even this would require O(n) time per a_max, leading to O(n^2) time.

This seems challenging.

Alternative idea: For the remaining elements when a_max is fixed, the minimal b_max + c_max is the same as the earlier problem. So perhaps we can precompute for all elements the minimal b_pos and c_pos for each possible a_max.

But I'm not sure.

Alternatively, note that the minimal sum for the remaining elements is the minimal B + C such that for all x not covered by a_max, B >= b_pos[x] or C >= c_pos[x].

The minimal B + C can be found as follows:

Let's collect for each x not covered by a_max, the pair (b_pos[x], c_pos[x]). We need to choose B and C such that for each pair, B >= b_pos[x] or C >= c_pos[x]. B and C must be >=0.

The minimal sum B + C for this set of pairs can be computed by considering the following:

The optimal B and C are determined by the maximum of certain values. For example, B must be at least the maximum of all b_pos[x] where c_pos[x] > C. But since C is unknown, this is a two-variable optimization problem.

But how to compute this efficiently.

An efficient way to find the minimal B + C is as follows:

We can collect all the pairs (b_x, c_x) for the remaining x's.

The minimal B and C must satisfy:

B >= max (b_x where c_x > C)

and

C >= max (c_x where b_x > B)

But this is a bit of a chicken and egg problem.

An alternative approach is to consider the possible candidates for B and C. Since each B is the maximum of a subset of the b_x's, and similarly for C, perhaps the optimal B and C are determined by the maximum of certain subsets.

The minimal B + C is the minimal of:

max_b, max_c (when all are covered by B and C)

max_b + max_c (when some are covered by B and others by C)

But this is not straightforward.

Wait, perhaps the optimal B and C are such that one of them is the maximum of their respective positions. For example, if B is the maximum of all b_x's, then C can be zero, sum is B. Or if C is the maximum of all c_x's, sum is C. Or, B is the maximum of some subset and C is the maximum of others.

Alternatively, the minimal B + C is the minimum between:

1. max_b_x (C is zero)

2. max_c_x (B is zero)

3. max (b_x) for x where c_x < some value plus max (c_x) for x where b_x < some value.

But I'm not seeing a way to compute this efficiently.

Alternatively, for each pair (b_x, c_x), we can model it as requiring B >= b_x or C >= c_x. The minimal B + C is the minimal sum where for all pairs, at least one of the two inequalities holds.

This problem is known and can be solved as follows:

The minimal B + C is the minimal of:

- max_b_x + 0 (all pairs are covered by B, C=0)

- 0 + max_c_x (B=0, all covered by C)

- For each x, min(b_x + max_c_x for all y where c_y > b_x)

But I'm not sure.

Alternatively, consider all possible possible B values. For each B, compute the minimal C needed as the maximum of c_x for all x where b_x > B. Then, the sum B + C is a candidate. The minimal such sum across all possible B is the answer.

So to compute this, we can:

- Collect all possible B candidates, which are the b_x's, plus 0 and max_b_x.

- For each B candidate, compute C as the maximum of c_x for x where b_x > B.

- The sum B + C is computed and the minimal sum is kept.

Additionally, we need to consider the case where B is zero, which is already included.

But this approach can be done efficiently by sorting the pairs.

Here's how:

1. Sort all the (b_x, c_x) pairs in decreasing order of b_x.

2. Precompute a suffix maximum array for the c_x's. For example, after sorting the pairs in descending order of b_x, for each position i, the suffix_max_c[i] is the maximum c_x from i to the end.

3. Iterate through all possible B candidates, which are the sorted b_x's and zero. For each B candidate (say, B = current_b), find all pairs where b_x > B. The maximum c_x among these pairs is the required C. The sum is current_B + C.

4. The minimal sum among all these candidates is the answer.

For example:

Pairs sorted in decreasing order of b_x:

(b1, c1), (b2, c2), ..., (bn, cn), where b1 >= b2 >= ... >= bn.

The suffix_max_c array is precomputed. For each i from 0 to n-1, suffix_max_c[i] is max(c_i, c_{i+1}, ..., c_{n-1} }.

Then, for a given B, find the first i where b_x <= B. All pairs before i have b_x > B. The maximum c_x among those is suffix_max_c[0 ... i-1].

But since the pairs are sorted in descending order of b_x, for B, the pairs with b_x > B are the first k pairs where b_k > B. The maximum c_x in these pairs is suffix_max_c[0] up to k-1.

Wait, the suffix_max_c array would start from the first pair (max b_x) to the end. So for the sorted list in descending order of b_x, the suffix_max_c[i] is the maximum of c_x from i to end.

So for B = current_b, the pairs with b_x > current_b are the first i where b_x > current_b. For example, if current_b is B, then the pairs are split into those with b_x > B and those <= B. For those with b_x > B, their indices are 0 to j-1, where j is the first index where b_x <= B.

The maximum c_x in those pairs is suffix_max_c[0] (since the suffix_max_c for 0 is the maximum of all c_x in the list). Wait, no. Because the suffix_max_c is computed as the maximum from position i to the end.

Wait, when we have the pairs sorted in descending order of b_x, the suffix_max_c for position i is the maximum of c_x from i to the end. So for the first j pairs (with b_x > B), the maximum c_x is the maximum of c_x in positions 0 to j-1. But the suffix_max_c[0] would be the maximum of all c_x from position 0 to end. So if j is the first index where b_x <= B, then the pairs 0 to j-1 have b_x > B, and the maximum c_x among them is the maximum of c_x[0..j-1]. But since the pairs are sorted in descending order of b_x, the suffix_max_c for position 0 is the maximum of all c_x. But that's only true if j is 0. Hmm, perhaps this approach isn't correct.

Alternatively, when the pairs are sorted in descending order of b_x, the suffix_max_c array can be precomputed by iterating from the end to the beginning.

For example:

suffix_max_c[i] = max(c_x[i], suffix_max_c[i+1]).

This way, suffix_max_c[i] is the maximum of c_x from i to the end.

So, for a given B, the j is the first index where b_x <= B. All pairs before j have b_x > B. The maximum c_x among them is the maximum of c_x[0..j-1], which is suffix_max_c[0] if j is 0 (but j=0 implies no pairs have b_x > B), but that's not possible. Wait, j is the first index where b_x <= B. So for example, if B is 5, and the pairs sorted in descending order are (10,3), (8,5), (6,2), (4,7), (3,1), then j would be 3, since the first three pairs have b_x >5. So the maximum c_x in these three pairs is max(3,5,2) =5. Which is suffix_max_c[0] =5 (since the suffix_max_c for index 0 is the max of c_x from 0 to end, which is 7). Wait, no. Because the suffix_max_c[0] would be the maximum of all c_x. So in this case, the maximum for j=3 is the maximum of the first 3 elements (3,5,2), which is 5, but the suffix_max_c[0] is 7. So this approach is incorrect.

Ah, I see the problem. The suffix_max_c is the maximum from position i to the end of the entire list, not just up to j-1. So if B is 5, the first three pairs (j=3) are considered, but the suffix_max_c[0] is the maximum of all c_x, which includes those beyond j-1. So this approach would not work.

Thus, this idea is flawed.

Alternative approach: Precompute for each pair in the sorted list (sorted by b_x descending), the maximum c_x up to that point. For example, prefix_max_c[i] = max(c_x[0..i]).

Then, for B equal to some value, the pairs with b_x > B are the first j pairs. The maximum c_x among them is prefix_max_c[j-1].

But how to compute j efficiently for each B.

This can be done using binary search. For each B, j is the number of pairs with b_x > B, which can be found using binary search in O(log m) time, where m is the number of pairs.

Then, the maximum c_x in those j pairs is prefix_max_c[j-1], if j>0. Otherwise, it's zero.

Thus, for each B candidate, the required C is max(prefix_max_c[j-1], max_c_rest), where max_c_rest is the maximum of c_x for pairs where b_x <= B. Wait, no. Because for pairs where b_x <= B, they can be covered by either B or C. So if C is >= c_x, then those pairs are covered. But in the case where B is set to a certain value, the C needs to be at least the maximum c_x of pairs not covered by B. But pairs not covered by B are those where b_x > B? No. Wait, pairs are covered by B if B >= b_x. So for a pair (b_x, c_x), if B >= b_x, then it is covered by B. If not, then it must be covered by C >= c_x.

Thus, for a given B, the required C is the maximum of c_x for all pairs where b_x > B. Because for those pairs, they are not covered by B and must be covered by C.

The pairs with b_x <= B are covered by B (since B >= b_x), so their c_x is irrelevant. So for a given B, the required C is the maximum c_x among all pairs where b_x > B.

Thus, to compute the required C for a given B:

C = max{ c_x | (b_x, c_x) in pairs and b_x > B }

If there are no such pairs, then C can be 0.

Thus, for each B candidate, we can compute C as follows:

- Use binary search to find the largest index j where b_x > B. All pairs before j have b_x > B.

- The maximum c_x among those pairs is the prefix_max_c[j] (assuming prefix_max_c is built as the maximum up to each index).

Wait, the prefix_max_c would be the maximum of the first i+1 elements. So for pairs sorted in descending order of b_x, the prefix_max_c array would be:

prefix_max_c[0] = c_x[0]

prefix_max_c[i] = max(prefix_max_c[i-1], c_x[i])

So for pairs 0 to j-1, the maximum c_x is prefix_max_c[j-1].

Thus, for B, the required C is prefix_max_c[j-1], where j is the number of pairs with b_x > B.

So how to find j for a given B.

Since the pairs are sorted in descending order of b_x, we can use binary search to find the first pair where b_x <= B. The number of pairs before that is j.

Thus, the steps are:

1. For the remaining elements after a_max is fixed, collect their (b_pos, c_pos) pairs.

2. Sort these pairs in descending order of b_pos.

3. Compute the prefix_max_c array.

4. For each possible B candidate (which can be any of the b_pos in the pairs plus 0 and the maximum of b_pos), compute j via binary search, find the required C as prefix_max_c[j-1] (if j>0) else 0.

5. Compute B + C and keep track of the minimal sum.

The candidates for B can be all possible b_pos values in the pairs, plus zero. But to avoid redundant candidates, we can take the sorted unique b_pos values.

This way, the number of B candidates is O(m), where m is the number of pairs. But m can be up to 1e5, which makes this approach O(m log m) for each a_max. For a_max candidates up to 1e5, this is O(n^2 log n), which is not feasible.

Thus, this approach is not suitable for large n.

Hmm. So what's the alternative?

Alternative Idea: Precompute for each element x, the earliest positions in a, b, and c. Then, the optimal solution is to choose for each array the maximum of the earliest positions of the elements assigned to that array, such that the sum of these maxima is minimized.

This is the same as the problem of partitioning elements into three groups with each group's maximum being as small as possible, and the sum of the three maxima being minimized.

This problem is similar to scheduling jobs on three machines, where each job can be assigned to any machine, and the processing time for the job is its earliest occurrence in the respective array. The makespan is the sum of the maxima of each machine's assigned jobs. But finding the minimal sum of maxima is not a standard scheduling problem.

But how to model this.

Alternative Idea: Let's consider that the optimal sum is the minimal possible sum of three numbers A, B, C such that for every x in the union:

A >= a_pos[x] OR B >= b_pos[x] OR C >= c_pos[x]

The minimal sum of A + B + C.

We need to find the minimal A + B + C where the above condition holds for all x.

This is the crux of the problem.

Now, the question is how to find such A, B, C efficiently.

Given that each of A, B, C can be up to 1e5, this seems challenging.

But perhaps we can find candidates for A, B, C by considering the a_pos, b_pos, c_pos of the elements.

For example, possible candidates for A are the a_pos of all elements, plus zero. Similarly for B and C.

But even this leads to O(n^3) possibilities, which is impossible.

Alternative Idea: Find the minimal A + B + C such that for all x:

a_pos[x] <= A OR b_pos[x] <= B OR c_pos[x] <= C.

We can model this as a problem of finding the minimal sum where A is the maximum a_pos of some subset, B is the maximum b_pos of some subset, and C is the maximum c_pos of another subset. All x must be in at least one of these subsets.

But again, this is not straightforward.

Another Idea: Let's precompute for each element x the minimal values of A, B, C such that x is covered. For example, for x, the minimal possible A is a_pos[x], the minimal B is b_pos[x], minimal C is c_pos[x]. So for x to be covered, at least one of these must be part of the solution.

But how to combine all elements' conditions.

Perhaps the optimal solution is to choose A, B, C as the minimal possible maximum values across the elements assigned to each array.

But again, this is vague.

Alternative Idea: The minimal sum of A + B + C is the minimal sum of the three maxima, which can be found by considering all possible combinations of the three maxima.

But given the size, this seems impossible.

Alternative Idea: Let's try to find all possible candidate triplets (A, B, C) where each of A, B, C is the a_pos, b_pos, or c_pos of some element. Then, for each such triplet, check if all elements are covered. This is O(n^3), which is not feasible.

But perhaps we can find that the optimal triplet consists of the a_pos, b_pos, and c_pos of certain elements.

Alternatively, perhaps we can consider the following:

For each element x, the minimal possible contribution to the sum when x is covered by a, b, or c is a_pos[x], b_pos[x], c_pos[x]. So the optimal triplet must have A >= a_pos[x], B >= b_pos[x], or C >= c_pos[x].

The sum A + B + C is the sum of the maxima of the three arrays.

But how to find the minimal sum.

Another Idea: Let's consider that the optimal solution must satisfy A is the maximum of a_pos of the elements assigned to a, B is the maximum of b_pos assigned to b, and C is the maximum of c_pos assigned to c. The sum A + B + C is minimized.

This is the same as before.

But how to assign elements to the arrays.

Perhaps the optimal solution is to assign each element x to the array where its a_pos, b_pos, or c_pos is the smallest. Then, the sum will be the sum of the maxima of each array's assigned elements.

But as we saw earlier, this may not be optimal.

But maybe this is a good starting point.

Let's compute for each element x the array (a, b, or c) where its earliest position is minimal. Assign x to that array. Then, compute the maxima for each array and sum them. This is a candidate solution.

But this may not be optimal.

Another candidate solution could be to assign some elements to a different array to reduce the sum of the maxima.

But how to find these cases.

For example, if two elements are assigned to a, and their a_pos are 100 and 1. Then, the maximum a is 100. But if one of them is assigned to b (which has b_pos 50), then the maximum a becomes 1, and the maximum b becomes 50. The sum becomes 1 +50 + ... which may be better.

But how to model this.

This seems like a problem that requires dynamic programming, but with the high constraints, it's not feasible.

Thus, perhaps the optimal solution is to try all possible combinations of the three maxima and find the minimal sum.

But this is not feasible for large n.

Alternative Idea: The minimal sum is achieved when two of the three maxima are as small as possible, and the third is as small as possible given the first two.

So perhaps we can compute the minimal sum by considering all possible pairs of two arrays, and compute the third's required maximum.

But this is still not clear.

Another Idea: Let's precompute for each element x the three possible earliest positions. Then, for the entire set of elements, the minimal sum would be the minimal sum of the three maxima when each x is assigned to one of the three arrays.

This is the same as the original problem.

But given the size, the only way to solve this is to find an O(n) or O(n log n) algorithm.

Let's think differently. Suppose we iterate through all possible combinations of the three maxima:

- For each possible A (a_max), B (b_max), C (c_max), check if all elements are covered. But this is not feasible.

But perhaps we can find the optimal solution by considering the following:

The optimal triplet (A, B, C) must be such that A is the maximum a_pos of some subset of elements, B is the maximum b_pos of some subset, and C is the maximum c_pos of another subset. And all elements must be in at least one subset.

Thus, the candidate values for A are the a_pos of some elements, B are the b_pos of some elements, and C are the c_pos of some elements.

But with n up to 1e5, this is still not feasible.

Alternative Idea: The minimal possible sum is the minimal of the following:

- a_max + b_max + c_max, where a_max is the maximum a_pos of all elements, b_max is the maximum b_pos of all elements, c_max is the maximum c_pos of all elements. (This is the worst case scenario where all elements are covered by their respective arrays. Sum is a_max + b_max + c_max.)

- Other cases where some elements are covered by other arrays.

But this is not helpful.

Alternatively, the minimal sum is the minimal sum of the three maxima, where each element's earliest position in at least one array is <= the corresponding maximum.

Thus, the minimal sum is the minimal sum of three numbers A, B, C such that for every element x, A >= a_pos[x], or B >= b_pos[x], or C >= c_pos[x].

This is a three-dimensional problem. To find the minimal sum of A + B + C satisfying these conditions.

But how to find this efficiently.

An alternative approach is to consider the problem as follows:

For each element x, the earliest possible coverage is to choose the array where x's earliest position is minimal. Let's call this min_pos[x] = min(a_pos[x], b_pos[x], c_pos[x]). The sum of the maxima if each x is assigned to the array with min_pos[x] would be the sum of the three maxima of the arrays.

But this sum might not be minimal, as the maxima could be overlapping in a way that some elements can be reassigned to reduce the sum.

But perhaps this sum is a good starting point and could be the minimal possible.

So let's compute this sum and see.

For each array a, collect the elements assigned to it (those where a_pos[x] is the minimal among a, b, c). The a_max is the maximum a_pos[x] of these elements. Similarly for b and c. The sum of these three maxima is a candidate.

But there might be other assignments that yield a smaller sum.

For example, if an element x has a_pos[x] = 100, b_pos[x] = 50, c_pos[x] = 60. It is assigned to b. If the current b_max is 50. But if we assign x to c (60), the b_max may decrease, but the c_max increases. But the sum may be lower or higher.

This suggests that the initial assignment may not be optimal.

But given the time constraints, perhaps this is the best approach.

But how to compute this.

Steps:

1. For each element x in the union, compute a_pos[x], b_pos[x], c_pos[x].

2. For each x, determine which array (a, b, c) has the minimal earliest position.

3. Assign x to that array.

4. Compute the maximum a_pos among x's assigned to a, similarly for b and c.

5. Sum the three maxima.

This gives a candidate sum. But there may be other assignments that lead to a lower sum.

But how to find such assignments.

Alternatively, the optimal sum is the minimal of the following candidates:

a. Assign all elements to a, sum is a_max (sum of a_max + 0 + 0).

b. Assign all to b, sum is b_max.

c. Assign all to c, sum is c_max.

d. Assign to their minimal array.

e. Other combinations.

But this is not guaranteed to find the optimal solution.

Another Idea: For each possible pair of arrays, compute the sum when all elements are covered by those two arrays, and find the minimal sum.

For example:

For each x, choose between a and b. The required a_max is the maximum a_pos[x] of elements assigned to a, and b_max is the maximum b_pos[x] of elements assigned to b. The sum is a_max + b_max.

We can compute this for each possible pair.

Then, take the minimal sum among all possible pairs and the three individual arrays.

But this may not consider the cases where some elements are assigned to other arrays.

But again, this approach may not find the optimal solution.

But let's try to see how this could be done.

For example, considering pair a and b:

Each x must be covered by a or b. The sum is a_max + b_max.

The minimal sum would be the maximum a_pos[x] of all x's (if all are assigned to a) plus zero, or zero plus maximum b_pos[x], or some combination in between.

But again, this is not feasible for large n.

Alternatively, for pair a and b, the minimal sum is the minimal a_max + b_max such that for every x, a_pos[x] <= a_max or b_pos[x] <= b_max.

This is a two-dimensional problem, but perhaps we can find the minimal sum using the same approach as before.

But with three pairs to consider (a and b, a and c, b and c), and then compare with the individual arrays and the minimal array approach.

But even this would be time-consuming.

At this point, I'm struggling to find an efficient algorithm that can handle the problem within the constraints.

Let's look at the problem's sample input to see if we can find a pattern.

Sample Input 1:

n=3

a: [1, 1, 101]

b: [1, 2, 1]

c: [3, 2, 1]

Union elements: 1, 101, 2, 3.

For each element:

1:

a_pos=1 (earliest in a is first element).

b_pos=1 (earliest in b is first element).

c_pos=3 (earliest in c is third element).

So minimal is a or b (pos 1).

101:

a_pos=3.

b_pos=inf (does 101 appear in b? No. So b_pos is infinity).

c_pos=inf.

So minimal is a's 3.

2:

a_pos=inf.

b_pos=2 (second element).

c_pos=2 (second element).

So minimal is b or c (pos 2).

3:

a_pos=inf.

b_pos=inf.

c_pos=1 (first element).

So minimal is c's 1.

So when assigning each element to the minimal array:

1 → a (pos 1).

101 → a (pos3).

2 → b or c (pos2).

3 → c (pos1).

Then, a_max is 3 (from 101), b_max is 2 (if 2 is assigned to b), c_max is 1 (from 3). Sum is 3+2+1=6. But the sample output is 5.

Ah, so this approach gives a sum of 6, but the sample's optimal sum is 5.

So the initial approach of assigning each element to its minimal array is not optimal.

In the sample's optimal solution, 2 is assigned to c's earliest position (2), and 3 is assigned to c's earliest (1). So c_max is 2. Then, a_max is 3 (for 101 and 1), v_max is 0, w_max is 2. Sum is 3+0+2=5.

So in this case, the element 2 is assigned to c's position 2, even though its minimal is 2 in both b and c. But by assigning it to c, b_max can be zero (since no elements are assigned to b), allowing the sum to be lower.

Thus, the initial approach of assigning elements to their minimal array is not sufficient. We need a smarter way.

This suggests that the optimal solution requires considering that some elements are better assigned to a non-minimal array to allow other arrays' maxima to be lower.

But how to model this.

Alternative Idea: The optimal solution's sum is the minimal sum of the three maxima, which can be found by considering all possible combinations of the three maxima. However, given the time constraints, we need a way to generate these candidates efficiently.

Let's think about the possible candidates for A, B, C.

A can be any of the a_pos values of the elements, or zero.

B can be any of the b_pos values, or zero.

C can be any of the c_pos values, or zero.

But the number of candidates is still too large.

But perhaps the optimal solution is formed by the following:

A is the maximum a_pos of some subset S_a, B is the maximum b_pos of subset S_b, and C is the maximum c_pos of subset S_c, where S_a, S_b, S_c form a partition of the elements.

Thus, the sum A + B + C is the sum of the three maxima.

But to find the minimal sum, we can generate all possible combinations of these maxima and check if all elements are covered.

But this is computationally expensive.

Alternatively, the optimal solution must have A, B, C such that each is the earliest position of at least one element. Because if A is not the earliest position of any element, then we can reduce A to the maximum a_pos of the elements assigned to a, which would be less than or equal to the previous A. This would result in a smaller sum.

Thus, the optimal solution's A must be the a_pos of some element in S_a. Similarly for B and C.

Thus, the possible candidates for A are the a_pos of the elements, plus zero.

Similarly for B and C.

But even this, the number of candidates is O(n^3), which is not feasible.

Alternative Idea: Let's precompute for each element x, the minimal possible sum of A + B + C when x is covered by a, b, or c. But this isn't directly useful.

Another Idea: Let's precompute for each element x the three possible earliest positions (a_pos, b_pos, c_pos). Then, for the entire set, the minimal sum is the minimal possible sum of the three maxima, which can be found by considering all possible combinations of these positions.

But again, this is computationally expensive.

Given the time constraints, perhaps the only feasible way is to precompute for each element x the three possible positions, and then compute all possible combinations of these positions to find the minimal sum.

But even this would take O(n^3) time, which is not feasible.

Thus, I'm stuck. I need to find a way to model this problem that allows for an O(n log n) solution.

Alternative Idea: Let's think of the problem in terms of the following: for each element x, the earliest possible coverage is the minimal of a_pos[x], b_pos[x], c_pos[x]. The sum of these minima for all x is a lower bound on the sum of the three maxima.

But this is not directly helpful, as the sum of the three maxima is different from the sum of the minimal positions.

But perhaps, if we can find a way to distribute the elements into the three arrays such that the sum of the maxima is as close as possible to the sum of the minimal positions.

Another Idea: The problem is similar to the three-set cover problem, where each element can be covered by any of the three sets, and the cost of each set is the maximum element in it. The goal is to cover all elements and minimize the sum of the costs of the three sets.

This problem is NP-hard, but given the constraints, there must be an efficient approach.

Wait, but if the problem is NP-hard, then there's no way to solve it for n=1e5 in O(n) or O(n log n) time. So the problem must have a greedy solution.

But what's the greedy approach?

Perhaps, for each element, assign it to the array where it has the earliest position, but also consider the current maxima of the arrays and see if assigning to a different array could lead to a lower sum.

For example, if assigning an element to array a would increase a's current max from 5 to 10, but assigning it to array b where its position is 6 (but the current max of b is 5), then the sum would increase by 6-5 =1, whereas a's sum increases by 5. So it's better to assign to b.

But how to implement this in an efficient manner.

This suggests a greedy algorithm where elements are processed in some order, and each element is assigned to the array that would result in the minimal possible sum.

But the order in which elements are processed can affect the outcome. For example, processing elements with larger positions first.

But even this is not trivial.

Another Idea: Sort all elements in descending order of their minimal earliest positions (min(a_pos, b_pos, c_pos)). Process each element in this order. Assign each element to the array where its position is the minimal, and track the current max for each array. This way, elements with larger minimal positions are processed first, and their assignment is less likely to affect the sum.

For example, elements with larger minimal positions are assigned first, and their assignment sets the current max. Smaller elements can then be assigned to other arrays without increasing the current max.

But how to implement this.

But this is just a heuristic and may not lead to the optimal solution.

But perhaps it's worth trying.

Let's take the first sample:

Elements and their minimal positions:

1 → 1 (a or b)

101 → 3 (a)

2 → 2 (b or c)

3 → 1 (c)

Sorted in descending order of minimal positions: 3 (101, 3), 2 (2, 2), 1 (1, 1), 3 (1 in c).

Processing in order:

101 is assigned to a, a_max is 3.

2 is assigned to b or c. If assigned to b, b_max is 2. If to c, c_max is 2.

1 is assigned to a or b. Current a_max is 3. Assigning to a doesn't change it. Assigning to b would set b_max to 1.

3 is assigned to c, c_max is 1.

So the sum would be 3 (a) + 2 (b) + 1 (c) =6. But the sample's optimal sum is 5.

So this approach does not find the optimal solution.

Thus, this greedy approach may not work.

At this point, I'm out of ideas. Perhaps I need to look for a different approach.

Wait, perhaps the key is to realize that the sum of the three maxima can be minimized by considering for each array the elements that contribute to its maximum, and ensuring that the sum is balanced.

Let's consider that each array's maximum is determined by at least one element assigned to it. So for array a, the maximum is a_pos of some element x. For array b, the maximum is b_pos of some element y. For array c, the maximum is c_pos of some element z.

The minimal sum would be the sum of these three positions, provided that all other elements are covered by at least one array.

Thus, the optimal sum is the minimal sum of a_pos[x] + b_pos[y] + c_pos[z], where x, y, z are elements in the union, and all elements are covered by at least one of a's a_pos[x], b's b_pos[y], or c's c_pos[z].

This seems like a promising approach.

So the problem reduces to finding three elements x, y, z in the union such that:

- a_pos[x] is the maximum a_pos of elements assigned to a.

- b_pos[y] is the maximum b_pos of elements assigned to b.

- c_pos[z] is the maximum c_pos of elements assigned to c.

- For every element e in the union, at least one of a_pos[e] <= a_pos[x], b_pos[e] <= b_pos[y], or c_pos[e] <= c_pos[z] is true.

- The sum a_pos[x] + b_pos[y] + c_pos[z] is minimized.

Thus, the problem is to find the triple (x, y, z) that satisfies the above conditions and has the minimal sum.

But how to find such a triple.

One way is to consider all possible triples (x, y, z) and check if they cover all elements. But this is O(n^3), which is impossible.

Alternative Idea: For each element x, compute the minimal possible sum when x is chosen as the a_max. Then, find the minimal b_max + c_max required to cover the remaining elements. The total sum is a_max + (b_max + c_max). The minimal sum over all x would be the answer.

This is similar to the earlier approach where we iterate over a_max candidates and compute the minimal sum for b and c.

But how to compute this efficiently.

Let's try to formalize this.

For a fixed a_max (a_pos[x] for some x), the remaining elements are those where a_pos[e] > a_max. For these elements, they must be covered by either b_pos[e] <= B or c_pos[e] <= C. We need to find B and C such that for all such e, B >= b_pos[e] or C >= c_pos[e]. The sum B + C is to be minimized.

The minimal B + C for this scenario is the minimal sum of the maxima of b and c for the remaining elements.

To compute this, we can use the approach of considering all possible B candidates and compute the required C for each.

But with the optimized approach of sorted pairs and prefix maxima, this can be done in O(m log m) per a_max, where m is the number of remaining elements.

But for n=1e5, and m=1e5, this would be O(n^2 log n), which is not feasible.

Thus, this approach is not suitable.

Alternative Idea: Precompute for all elements their a_pos, b_pos, c_pos. For each element x, compute the a_pos[x], and collect the b_pos and c_pos of elements not covered by a_pos[x].

Then, the minimal B + C for each a_pos[x] is the minimal sum of B and C such that for all elements not covered by a_max, they are covered by B or C.

But again, this requires O(n^2) time.

At this point, given time constraints and the problem's difficulty, perhaps the intended solution is to precompute the earliest positions for each element in the three arrays, then for each element, compute the minimal possible contribution to the sum when assigned to a, b, or c, and find the combination that gives the minimal sum.

But how.

Another Idea: The minimal sum is the minimal value of the maximum of a's positions plus the maximum of b's positions plus the maximum of c's positions, but each element is allowed to be covered by any of the three.

But this is the same as the problem's statement.

Thus, the solution is to precompute the earliest positions for each element in the three arrays, then for each element, note the earliest positions. Then, the problem is to choose for each element which array to assign it to, such that the sum of the three maxima is minimal.

This seems to require an O(n) solution, but I'm not sure.

Another Idea: The minimal sum is the sum of the three maxima, where the maxima are chosen such that for each array, its maximum is the largest a_pos (or b_pos, c_pos) of the elements assigned to it.

But how to select these maxima.

Perhaps the optimal solution is to assign the element with the largest a_pos to a, the element with the largest b_pos to b, and the element with the largest c_pos to c. But this may not cover all elements.

For example, if an element has a_pos = 100, b_pos = 50, c_pos = 50, then assigning it to a would require a_max=100, but assigning it to b or c would require b_max=50 or c_max=50. But other elements may have larger positions in b or c.

This is getting too vague.

Another Idea: Let's consider that the minimal sum is the sum of the three largest minima among all elements' earliest positions.

But this doesn't make sense.

Alternatively, think of each element as contributing the minimal of a_pos, b_pos, c_pos. The sum of these minima is a lower bound for the total sum. But the actual sum is the sum of the maxima of the three arrays, which is likely higher than this lower bound.

But how to relate this.

At this point, I think I need to look for a different approach. Let's consider the problem in terms of the earliest positions.

For each element x, we have three possible positions: a_pos[x], b_pos[x], c_pos[x]. The element x must be covered by at least one of these positions in their respective arrays. We need to select one position for each x (from the three options) such that the sum of the maximum a_pos selected, maximum b_pos selected, and maximum c_pos selected is minimized.

So the problem is to choose for each x one of the three options (a_pos[x], b_pos[x], c_pos[x]), and then compute the sum of the maxima of each array's selected positions.

The goal is to choose these options such that the sum is minimized.

This is equivalent to the problem of assigning each element to one of the three arrays, and the sum is the sum of the maxima of the assigned positions for each array.

This is a well-known problem, but I'm not sure of the solution.

The key insight is that the sum is determined by the maximum of each array's assignments. Thus, for each array, the maximum is the largest position of any element assigned to it. The sum of these maxima is to be minimized.

This problem is similar to scheduling jobs on three machines, where each job can be assigned to any machine, and the makespan is the sum of the maximum processing times on each machine. We need to minimize the sum.

But this is a different problem from the standard scheduling problem.

The solution to this problem is to find for each element the array that contributes the least to the sum of the maxima.

But how to model this.

Let's think of it as follows: each element x can be assigned to a, b, or c. The cost is the sum of the maxima of each array's assignments. We need to assign each element to one array to minimize this cost.

This is a dynamic programming problem, but with three dimensions (current a_max, current b_max, current c_max), which is not feasible for n=1e5.

Thus, this approach is not feasible.

Alternative Idea: For each array, track the current maximum. For each element x, choose the array where adding x's position results in the minimal possible increase to the current sum of maxima.

This is a greedy approach where each element is assigned to the array that causes the least increase in the sum.

For example:

Initially, all maxima are zero.

For each element x:

Compute for each array the new maximum if x is assigned to it. The new sum is (max(a_max, x_a) + max(b_max, x_b) + max(c_max, x_c)).

Assign x to the array which results in the minimal new sum.

But this is a greedy approach and may not find the optimal solution.

Let's test this with the first sample.

Sample 1:

Elements in order: 1, 101, 2, 3.

Initial sum is 0.

Element 1:

Options:

Assign to a: new sum is max(1) + 0 + 0 = 1. Sum 1.

Assign to b: sum is 0 + 1 + 0 =1. Sum 1.

Assign to c: sum is 0+0+3=3. So choose a or b.

Let's choose a.

Current a_max=1, sum=1.

Element 101:

Options:

Assign to a: new a_max=3. Sum is 3 + 0 +0=3.

Assign to b: new b_max=101's b_pos (infinite?), but wait, 101 is not in b. So b_pos is infinity. Assigning to b would require B to be infinity, which is not possible. So this is not an option.

Wait, no. If 101 is not present in b, then its b_pos is infinity. So the only way to cover 101 is through a or c.

Since 101 is in a, a_pos is 3. Assigning to a gives a_max=3, sum=3+0+0=3.

If assigned to c, c_pos is infinity (not present in c), which is not possible. So must assign to a.

Current sum is 3.

Element 2:

Options:

Assign to a: a_max remains 3. sum 3 + 0 +0=3.

Assign to b: b_max=2. sum 3+2+0=5.

Assign to c: c_max=2. sum 3+0+2=5.

The minimal sum is 3, so assign to a.

Current a_max=3.

Element 3:

Options:

Assign to a: a_max=3. sum 3+0+0=3.

Assign to c: c_max=1. sum 3+0+1=4.

So assign to a. Sum remains 3.

But according to the sample, the optimal sum is 5. This approach gives a sum of 3, which is incorrect. This suggests that the greedy approach is flawed.

But in reality, the element 2 is not present in a. So when assigned to a, it's impossible. So the previous approach is incorrect.

Ah, right! I forgot that each array's position is only available if the element is present in that array.

So for element x, the a_pos[x] is infinity if x is not present in array a.

Thus, for element 2, a_pos[x] is infinity. So in the sample input, element 2 is not in a, so a_pos is infinity. So the option of assigning to a is not possible.

Thus, the previous analysis was incorrect.

So, for element 2:

a_pos is infinity (not in a), so can only be assigned to b or c.

Thus, when processing element 2:

Options:

Assign to b: b_pos[x] = 2 (earliest in b is position 2). Current b_max was 0. New b_max is 2. sum is 3 (a) + 2 (b) + 0 (c) =5.

Assign to c: c_pos[x] = 2 (earliest in c is position 2). Current c_max is 0. New c_max is 2. sum is 3 +0 +2=5.

So both options give sum 5. The greedy approach would choose either.

Then, processing element 3:

a_pos is infinity (not in a).

 options are to assign to c. c_pos[x] is 1.

 sum is 3 (a) + 2 (b) + max(2,1) =3+2+2=7.

 Or assign to b: b_pos[x] is infinity (not in b). So must assign to c.

 sum becomes 3 + 2 + 2 =7.

But the sample's optimal sum is 5. So this approach is not working.

Ah, no. Because the sample's optimal solution assigns 3 to c with w=2. But the element 3's earliest position in c is 1. So the c_max is 2 (from element 2's assignment to c, which has position 2). So the sum is a_max=3 (covers 1 and 101), b_max=0, c_max=2. Sum is 5.

But according to the greedy approach, when processing element 3, it's assigned to c's earliest position 1. But the previous elements (2) was assigned to b or c. If 2 was assigned to c, then c_max is 2, and element 3's assignment to c's position 1 does not increase the c_max. So the sum remains 3 (a) +0 (b) +2 (c) =5.

Ah, right! So the assignment of element 3 to c does not increase the c_max, because the c_max is already 2 from element 2. So the sum remains 5.

But the greedy approach would have processed elements in some order. So perhaps the order in which elements are processed is crucial.

In the sample input, the elements are:

1 (a_pos=1, b_pos=1, c_pos=3)

101 (a_pos=3, b_pos=inf, c_pos=inf)

2 (a_pos=inf, b_pos=2, c_pos=2)

3 (a_pos=inf, b_pos=inf, c_pos=1)

Processing order: 1, 101, 2, 3.

Processing 1: assign to a or b. Let's choose a. a_max=1.

Processing 101: must assign to a. a_max=3.

Processing 2: assign to b or c. Assign to b. b_max=2. sum is 3+2+0=5.

Processing 3: assign to c. c_max=1. sum is 3+2+1=6. But in the sample, the sum is 5.

Ah, so this approach gives sum 6, which is worse than the sample's solution.

Thus, the order in which elements are processed matters. If the elements are processed in a different order, perhaps the sum can be lower.

For example, processing 3 first.

Processing 3: assign to c. c_max=1.

Processing 1: assign to a. a_max=1.

Processing 101: assign to a. a_max=3.

Processing 2: assign to c. c_max= max(1, 2) =2.

Sum is 3+0+2=5.

Which is the sample's solution.

Thus, the order of processing elements is crucial. Processing elements with earlier positions first may lead to a better sum.

Thus, the greedy approach of processing elements in ascending order of their minimal positions may lead to a better sum.

Let's try this.

Sort the elements in ascending order of their minimal positions:

3 (min 1), 1 (min 1), 2 (min 2), 101 (min 3).

Processing in this order:

3: assign to c. c_max=1.

1: assign to a. a_max=1.

2: assign to c. c_max=2.

101: assign to a. a_max=3.

Sum is 3 (a) + 0 (b) + 2 (c) =5. Which is correct.

Thus, the processing order is important. Processing elements with smaller minimal positions first allows their assignment to arrays without increasing the current maxima.

Thus, the algorithm could be:

1. Precompute for each element x, the minimal of a_pos[x], b_pos[x], c_pos[x].

2. Sort the elements in ascending order of this minimal value.

3. For each element in this order, assign it to the array (a, b, or c) where its position is the minimal, and where adding it to that array does not increase the current maximum of that array beyond the minimal possible.

Wait, no. For example, element x has a_pos=5, but the current a_max is 3. Assigning x to a would increase a_max to 5, which could be worse than assigning to another array with a position of 4.

Thus, the assignment should choose the array where the element's position is the minimal possible, but also considering the current maxima of the arrays.

But how to model this.

The algorithm would be:

Initialize a_max = 0, b_max = 0, c_max = 0.

Sort elements in ascending order of their minimal earliest positions.

For each element x in this order:

   Check the three possible options:

   if a_pos[x] is the minimal and a_pos[x] <= current a_max:

       assign to a (doesn't increase a_max)

   else:

       choose the array where the new max (max(current array max, x's pos)) leads to the minimal new sum.

But how to decide this.

Alternatively, for each element x, compute for each array the new max if assigned to that array. The new sum is new_a_max + new_b_max + new_c_max. Choose the array that gives the minimal new sum.

But this requires, for each element, evaluating three possibilities and choosing the best.

But for n=1e5, this would be O(n) time.

Let's see how this works with the sample.

Sample 1:

Elements sorted by minimal pos:

3 (min 1), 1 (min 1), 2 (min 2), 101 (min 3).

Initial a_max=0, b_max=0, c_max=0.

Processing 3:

Options:

a_pos is inf, can't assign.

b_pos is inf, can't assign.

c_pos is 1. new c_max = max(0,1) =1. new sum is 0+0+1=1.

Assign to c. sum=1. c_max=1.

Processing 1:

Options:

a_pos=1. new a_max=1. sum=1+0+1=2.

b_pos=1. new b_max=1. sum=0+1+1=2.

c_pos=3. new c_max=3. sum=0+0+3=3.

Choose between a and b. Both give sum 2. Let's choose a.

a_max=1. sum=2.

Processing 2:

Options:

a_pos=inf.

b_pos=2. new b_max=2. sum=1+2+1=4.

c_pos=2. new c_max=2. sum=1+0+2=3.

Choose c. sum=3. c_max=2.

Processing 101:

Options:

a_pos=3. new a_max=3. sum=3+0+2=5.

b_pos=inf. can't assign.

c_pos=inf. can't assign.

Assign to a. sum=5.

This gives the correct sum of 5.

Thus, this greedy approach seems to work.

Thus, the algorithm is:

Sort the elements in ascending order of their minimal a_pos, b_pos, c_pos.

For each element in this order:

   For each array (a, b, c) where x has a valid position (not infinity):

       compute the new maximum if x is assigned to that array.

   For each possible array (a, b, c) where x can be assigned:

       calculate the new sum of maxima.

   Assign x to the array that results in the minimal new sum.

   Update the current maxima.

This approach is O(n) time (assuming each element has up to three valid arrays), which is feasible for n=1e5.

This seems promising.

Thus, the steps are:

1. For each element x in the union of a, b, c:

   a. Compute a_pos[x] = earliest position in a (or infinity if not present).

   b. Compute b_pos[x], c_pos[x].

   c. Compute the minimal_pos[x] = min(a_pos[x], b_pos[x], c_pos[x]).

2. Sort the elements in ascending order of minimal_pos[x].

3. Initialize current_a_max = 0, current_b_max = 0, current_c_max = 0.

4. For each element x in sorted order:

   a. For each array (a, b, c):

       if x's pos in the array is not infinity:

           new_a_max = max(current_a_max, a_pos[x])

           new_b_max = current_b_max if array is not b, else max(current_b_max, b_pos[x])

           etc.

           compute new_sum = new_a_max + new_b_max + new_c_max.

   b. Choose the array (a, b, or c) where x can be assigned (i.e., pos in array is not infinity) and the new_sum is minimized.

   c. Assign x to that array and update the current maxima.

This would ensure that elements are processed in order of their minimal possible contribution and that each element is assigned to the array that leads to the minimal possible sum.

This approach should work for the sample and other cases.

Now, let's think about implementing this.

First, we need to read the three arrays and compute the earliest occurrence of each element in each array.

For each array a, we can create a dictionary that maps each element to its earliest (first) occurrence index (1-based).

Similarly for b and c.

Then, for each element in the union of a, b, c, we can compute a_pos, b_pos, c_pos.

The union can be found by taking the set of all elements in a, b, and c.

Once we have the three dictionaries, we can proceed.

Now, for each element x in the union:

a_pos[x] = the earliest index in a where x appears, or infinity if not present.

Similarly for b and c.

Then, minimal_pos[x] is the minimum of a_pos[x], b_pos[x], c_pos[x].

Sort the elements in ascending order of minimal_pos[x].

Then, for each element in this order, compute the possible new sums if assigned to a, b, or c (if possible), and choose the assignment that gives the minimal new sum.

This requires checking all three possible arrays for each x, but considering that some arrays may not have x (pos is infinity).

Thus, for each x, we can generate a list of possible arrays where x is present (i.e., pos is not infinity).

For example, if x is in a and b, but not in c, then we can assign x to a or b.

For each possible array (a, b, or c) that x can be assigned to, compute the new sum of maxima if x is assigned to that array.

Choose the array with the minimal new sum.

Update the current maxima accordingly.

This approach should work.

Let's test this with the second sample input.

Sample 2:

Input:

5

a: [1,1,2,2,3]

b: [2,2,4,3,3]

c: [3,3,1,1,1]

Union elements: 1, 2, 3,4.

For each element:

1:

a_pos: 1 (first occurrence at index 1, 1-based).

b_pos: infinity (1 not in b).

c_pos: 3 (first occurrence at index 3).

minimal_pos: 1.

2:

a_pos: 3 (first occurrence at index 3).

b_pos: 1 (first occurrence at index 1).

c_pos: infinity.

minimal_pos: 1.

3:

a_pos:5 (first occurrence at index 5).

b_pos:4 (first occurrence at index 4).

c_pos:1 (first occurrence at index 1).

minimal_pos:1.

4:

a_pos:infinity.

b_pos:3 (index 3).

c_pos:infinity.

minimal_pos:3.

Sorted order of elements by minimal_pos:

1, 2, 3,4.

Processing order: 1, 2, 3,4.

Initial maxima: 0,0,0. Sum 0.

Processing element 1:

Possible arrays: a and c.

For a:

new_a_max = max(0, 1) =1.

sum: 1+0+0=1.

For c:

new_c_max = max(0,3) =3.

sum:0+0+3=3.

Choose a. sum=1. current_a_max=1.

Processing element 2:

Possible arrays: a, b.

For a:

new_a_max = max(1,3)=3. sum=3 + current_b_max (0) + current_c_max (0) =3.

For b:

new_b_max = max(0,1)=1. sum=1 (a) +1 +0=2.

Choose b. sum=2. current_b_max=1.

Processing element 3:

Possible arrays: a, b, c.

For a: new_a_max=5. sum=5 +1 +0=6.

For b: new_b_max=4. sum=1+4 +0=5.

For c: new_c_max=1. sum=1+1+1=3.

Choose c. sum=3. current_c_max=1.

Processing element4:

Possible arrays: b.

new_b_max = max(1,3) =3. sum=1 (a) +3 +1=5.

Assign to b. sum=5.

Final sum is5, which matches the sample.

Thus, this approach works for the sample.

Thus, the algorithm is:

- For each element x in the union, compute a_pos, b_pos, c_pos.

- Sort the elements in ascending order of minimal_pos.

- Initialize current_a_max, current_b_max, current_c_max to 0.

- For each x in sorted order:

   For each array in [a, b, c] where x's pos is not infinity:

       compute the new max for that array.

       compute the new sum.

   Assign x to the array that gives the minimal new sum.

   Update the current max for that array.

Thus, this approach should work.

Now, the code.

Implementing this in Python:

We need to:

1. Read the three arrays.

2. For each array, create a dictionary mapping element to its first occurrence (1-based).

3. Compute the union of elements from all three arrays.

4. For each element in the union, get a_pos, b_pos, c_pos.

5. Compute minimal_pos for each element.

6. Sort the elements in ascending order of minimal_pos.

7. For each element in this order, compute the possible new sums for each valid array and choose the best.

8. Track current_a_max, current_b_max, current_c_max.

Now, for step 2, creating the dictionaries:

For array a:

traverse the array from left to right, record the first occurrence of each element.

Same for b and c.

For example, for a = [1,1,101], the first occurrences are:

1: 1 (1-based index)

101:3.

For array b = [1,2,1], the first occurrence of 1 is 1, 2 is 2.

For array c = [3,2,1], the first occurrence of 3 is 1, 2 is 2, 1 is 3.

Thus, the code for creating the dictionaries:

def build_first_pos(arr):

    pos = {}

    for idx, num in enumerate(arr, 1):

        if num not in pos:

            pos[num] = idx

    return pos

Then, a_pos = build_first_pos(a), etc.

For elements not present in a, their a_pos is infinity (we can represent this with a large number, like 1e18).

Then, for each element in the union:

a_p = a_pos.get(x, 1e18)

Similarly for b_p and c_p.

Then, minimal_pos = min(a_p, b_p, c_p).

Then, sort the elements in increasing order of minimal_pos.

Once sorted, for each x, we process it and choose the best array.

Thus, the code:

import sys

def main():

    import sys

    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))

    b = list(map(int, sys.stdin.readline().split()))

    c = list(map(int, sys.stdin.readline().split()))

    def build_first_pos(arr):

        pos = {}

        for i, num in enumerate(arr, 1):

            if num not in pos:

                pos[num] = i

        return pos

    a_pos = build_first_pos(a)

    b_pos = build_first_pos(b)

    c_pos = build_first_pos(c)

    # Compute the union of elements

    union = set()

    union.update(a)

    union.update(b)

    union.update(c)

    elements = list(union)

    # For each element, compute a_p, b_p, c_p, and minimal_p

    element_info = []

    for x in elements:

        a_p = a_pos.get(x, 10**18)

        b_p = b_pos.get(x, 10**18)

        c_p = c_pos.get(x, 10**18)

        minimal_p = min(a_p, b_p, c_p)

        element_info.append( (minimal_p, x, a_p, b_p, c_p) )

    # Sort elements by minimal_p

    element_info.sort()

    current_a_max = 0

    current_b_max = 0

    current_c_max = 0

    for _, x, a_p, b_p, c_p in element_info:

        # Check possible assignments

        options = []

        # a

        if a_p != 10**18:

            new_a = max(current_a_max, a_p)

            new_sum = new_a + current_b_max + current_c_max

            options.append( (new_sum, 'a', new_a) )

        # b

        if b_p != 10**18:

            new_b = max(current_b_max, b_p)

            new_sum = current_a_max + new_b + current_c_max

            options.append( (new_sum, 'b', new_b) )

        # c

        if c_p != 10**18:

            new_c = max(current_c_max, c_p)

            new_sum = current_a_max + current_b_max + new_c

            options.append( (new_sum, 'c', new_c) )

        if not options:

            # This element has no possible assignments, which is impossible since it's in the union.

            pass

        # choose the option with minimal new_sum

        options.sort()

        best = options[0]

        if best[1] == 'a':

            current_a_max = best[2]

        elif best[1] == 'b':

            current_b_max = best[2]

        else:

            current_c_max = best[2]

    total = current_a_max + current_b_max + current_c_max

    print(total)

if __name__ == '__main__':

    main()

This code should handle the problem correctly.

Let's test the first sample:

Sample 1:

After processing element 3 (x=3, a_p=inf, b_p=inf, c_p=1):

Options are to assign to c. new_c_max=1. sum is 1.

Then x=1, a_p=1, b_p=1, c_p=3.

Options:

assign to a: new_a_max=1. sum 1+0+0=1.

assign to b: new_sum 0+1+0=1.

assign to c: sum 0+0+3=3.

Choose a or b. The code chooses the first option (sorted by sum, then by the array name). For example, if two options have the same sum, the code will pick 'a' because 'a' comes before 'b' in the options list. In this case, the code will assign x=1 to a, and the sum becomes 1.

Then x=2 (a_p=inf, b_p=2, c_p=2).

Options:

assign to b: sum 1+2+0=3.

assign to c: sum 1+0+2=3.

The code will choose the first option (b), but according to the sample, assigning to c gives a better sum.

Wait, no. In the sample's optimal solution, x=2 is assigned to c. But according to the code's processing, x=2 is processed after x=3 and x=1.

Let's see:

current_a_max=1, current_b_max=0, current_c_max=1.

x=2's a_p is inf, so options are b and c.

For b:

new_b_max=2. sum 1+2+1=4.

For c:

new_c_max=2. sum 1+0+2=3.

Thus, options are (4, 'b'), (3, 'c').

The code will choose c, since 3 is less than 4.

Thus, current_c_max becomes 2.

Then, processing x=101 (a_p=3, b_p=inf, c_p=inf). Only option is a.

new_a_max=3. sum 3+0+2=5.

Thus, the final sum is 5.

Thus, the code works for the first sample.

The code will also work for the second sample.

Thus, this approach should be correct.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    def build_first_pos(arr):
        pos = {}
        for idx, num in enumerate(arr, 1):
            if num not in pos:
                pos[num] = idx
        return pos

    a_pos = build_first_pos(a)
    b_pos = build_first_pos(b)
    c_pos = build_first_pos(c)

    union = set(a) | set(b) | set(c)
    elements = list(union)

    element_info = []
    for x in elements:
        ap = a_pos.get(x, 10**18)
        bp = b_pos.get(x, 10**18)
        cp = c_pos.get(x, 10**18)
        min_p = min(ap, bp, cp)
        element_info.append((min_p, x, ap, bp, cp))

    element_info.sort()

    current_a = current_b = current_c = 0

    for _, x, ap, bp, cp in element_info:
        options = []
        if ap != 10**18:
            new_a = max(current_a, ap)
            options.append((new_a + current_b + current_c, 'a', new_a))
        if bp != 10**18:
            new_b = max(current_b, bp)
            options.append((current_a + new_b + current_c, 'b', new_b))
        if cp != 10**18:
            new_c_val = max(current_c, cp)
            options.append((current_a + current_b + new_c_val, 'c', new_c_val))
        if options:
            options.sort()
            min_sum, array, new_max = options[0]
            if array == 'a':
                current_a = new_max
            elif array == 'b':
                current_b = new_max
            else:
                current_c = new_max

    print(current_a + current_b + current_c)

if __name__ == '__main__':
    main()
```