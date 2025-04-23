<think>
Okay, so I've got this programming problem to solve. Let's try to understand what it's about. 

The problem says we have a bunch of cities connected by roads, and the initial setup gives us a matrix of the shortest distances between every pair of cities. Then, we add new roads one by one, and after each addition, we need to compute the sum of all the shortest distances between every pair of cities. The key here is that each new road might potentially create shorter paths, so the sum could decrease each time.

The challenge is to efficiently update the distance matrix after each new road and compute the sum. The constraints are n up to 300 and k up to 300. So the straightforward approach of recomputing all pairs from scratch each time using something like Floyd-Warshall after each road addition would be O(k * n^3), which for n=300 and k=300 would be 300*300^3 = 300*27,000,000 = 8,100,000,000 operations. That's way too slow for a 2-second time limit. So we need a smarter approach.

Wait, but what's the alternative? Let's think. When we add a new road, say between a and b with length c, we can check if this new road provides a shorter path between a and b than what's already in the distance matrix. If not, then the new road doesn't affect any of the existing shortest paths, and the sum remains the same. But if it is shorter, then we need to update the distance matrix accordingly. How?

This sounds like the Floyd-Warshall algorithm, which is designed to compute all-pairs shortest paths incrementally by considering intermediate nodes. Maybe after adding a new edge, we can run a modified version of Floyd-Warshall that only considers the new possible paths through the new edge.

Alternatively, for each new edge (a, b) with length c, the new possible paths could be those that go through a to b via this new edge. So for every pair (i, j), the new distance could be min(current d[i][j], d[i][a] + c + d[b][j], d[i][b] + c + d[a][j]). Because the new road can be traversed in either direction, so we can go from a to b or b to a.

So the approach is:

1. Start with the initial distance matrix.
2. For each new road (a, b, c), consider the new edge. The effective new possible distance between a and b is the minimum of the existing distance and c. Then, for all pairs (i, j), we can check if using this new edge provides a shorter path.

But how to efficiently update the distance matrix? Let's think of it as adding a new edge and then running a relaxation step for all pairs. This is similar to the Floyd-Warshall approach, but instead of considering all intermediate nodes, we can treat the new edge as a possible intermediate step.

Wait, here's an idea. When a new edge (a, b, c) is added, we can check if c is less than the current distance between a and b. If not, nothing changes. If it is, then the new distance between a and b is updated to c. Then, for all other pairs (i, j), we can see if the path i -> a -> b -> j or i -> b -> a -> j provides a shorter path than the current one. So for each i and j, the new distance d[i][j] = min(d[i][j], d[i][a] + c + d[b][j], d[i][b] + c + d[a][j]).

Alternatively, since the new edge may offer new paths that pass through a and b, the way to update the matrix is to consider all pairs (i, j) and see if going via a or via b gives a better path.

But how to implement this efficiently?

Another approach: After adding the new edge, run the Floyd-Warshall algorithm again, but only using the new edge as a possible intermediate node. Wait, no, that's not exactly right. Because the new edge might allow for new paths that are shorter, but only if they pass through a and b. So perhaps we can run a variation where for all i and j, we check if the path i -> a -> b -> j or i -> b -> a -> j is shorter than the current path.

Alternatively, perhaps for each of the new edges, we can iterate over all possible pairs (i, j) and check if the new edge provides a shorter path. But even that would be O(n^2) per new edge. For n=300, that's 90,000 operations per edge. With k=300, that's 27 million operations, which is manageable.

Wait, let's think about the steps:

Initialize the distance matrix as given.

For each new road (a, b, c):

- First, check if the new edge's length c is less than the current distance between a and b. If not, then adding this road doesn't change anything, so the sum remains the same. So we can skip further processing for this road.

- If c is smaller than the current distance, then we update d[a][b] and d[b][a] to c (since the road is bidirectional). Then, for all pairs (i, j), the new distance could be improved by using the path i -> a -> b -> j or i -> b -> a -> j. So for all i and j, we compute d[i][a] + c + d[b][j] and d[i][b] + c + d[a][j], and take the minimum of those and the current d[i][j]. Then, we also need to propagate this improvement through all possible pairs. Because even if i and j's distance is updated, that might affect other pairs as well.

Wait, this is getting complicated. Because after updating d[i][j], other pairs might have their distances improved by going through i or j.

So this seems like a problem that's best handled by running the Floyd-Warshall algorithm again, but that's O(n^3) per iteration. For n=300 and k=300, that's 300 * 300^3 = 8,100,000,000 operations. Which is way too slow for Python, given that even a million operations take about a second.

So we need a better way.

Wait, but the Floyd-Warshall algorithm works by considering each node k as an intermediate node and updating all pairs i, j with the path i -> k -> j. So when we add a new edge between a and b, maybe we can run the Floyd-Warshall algorithm but only using a and b as intermediate nodes. Because the new edge's addition can only affect paths that go through a or b. But how?

Alternatively, perhaps we can run a modified version where for each new edge (a, b), we consider all possible i and j, and check if using the new edge (either a to b or b to a) gives a shorter path.

But even that is O(n^2) for each new edge. Then, perhaps we need to run this process multiple times until no more updates are possible. But how many times would that take? In the worst case, each update could propagate through the entire graph, leading to O(n) passes over O(n^2) elements. But that's O(n^3) again.

Alternatively, maybe there's a smarter way. Let's think: after adding the new edge (a, b), the only possible way that a path between i and j can be improved is if it can take advantage of the new edge. So, perhaps the following steps:

1. Check if the new edge (a, b) is better than the existing path. If not, do nothing.

2. If the new edge is better, then for all i and j, the new path i -> a -> b -> j or i -> b -> a -> j could be shorter than the current path. So, for each i and j, the new distance is min(d[i][j], d[i][a] + c + d[b][j], d[i][b] + c + d[a][j]).

But after that, the updated distances could allow for even shorter paths. For example, if after updating i and j's distance, another pair (i, k) could be updated using this new distance. So this approach might not capture all possible improvements.

Hmm. So perhaps the correct way is to run the Floyd-Warshall algorithm again, but optimized to only process the necessary parts. However, that's not feasible for large n.

Wait, but maybe there's a smarter way. Let's consider that the new edge (a, b) allows for paths that use a or b as intermediaries. So, perhaps we can iterate over all pairs (i, j) and check if using a or b as an intermediate node improves the distance.

Alternatively, here's an approach inspired by the Floyd-Warshall algorithm:

After adding the new edge (a, b, c), which could potentially reduce the distance between a and b, we can perform the following steps:

- Update the distance between a and b (and b and a) to be the minimum of their current distance and c.

- Then, for each node k in {a, b}, perform a relaxation step for all pairs (i, j). The relaxation step for node k is: d[i][j] = min(d[i][j], d[i][k] + d[k][j]).

But wait, since a and b are the only nodes affected by the new edge, perhaps iterating over all pairs and considering these two nodes as intermediaries can capture all possible improvements.

Wait, here's the idea: when you add a new edge between a and b, the shortest paths that can be improved are those that pass through a or b. So perhaps, we need to update all pairs (i, j) by considering paths that go through a or b. This is similar to the way Floyd-Warshall considers each intermediate node, but here, we are only considering a and b as possible intermediates.

So the steps would be:

For the new edge (a, b, c):

1. Check if c < d[a][b]. If not, do nothing.

2. Else, update d[a][b] and d[b][a] to c.

3. Then, for each node k in {a, b}, run a loop over all i and j to check if i -> k -> j is a shorter path. So for all i and j, d[i][j] = min(d[i][j], d[i][k] + d[k][j}).

4. However, this might not be sufficient. Because when you process a, the paths through a could affect paths through b. So maybe we need to run the loop multiple times until no more updates happen. But that's time-consuming.

Alternatively, perhaps considering a and b as intermediates and doing the relaxation for all pairs. Then, after that, considering that these new paths could allow for other intermediates to be used. But that's getting back into O(n^3) territory.

Wait, but in the Floyd-Warshall algorithm, the order of processing intermediates matters. So if we add a new edge and then run the Floyd-Warshall algorithm again, but only for the nodes a and b as intermediates, maybe that would capture all possible improvements. Let's think:

After adding the edge (a, b, c), the minimal path between a and b is now c. Then, any other pair i, j could have their path improved by going through a or through b. So, for each node k in {a, b}, we need to check all i and j for possible improvements via k. So the steps would be:

for k in [a, b]:
    for i in 1..n:
        for j in 1..n:
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

But why would this work? Because adding the edge a-b allows for paths through a or b. But perhaps after considering these two nodes as intermediates, all possible improvements are captured. 

Wait, but in Floyd-Warshall, you process all intermediates. So if the new edge allows for a path that uses a and then b as intermediates, then considering a and b as intermediates in sequence would capture that. For example, the path i -> a -> b -> j can be considered by first relaxing via a (i to a, then a to j), but if a to j's distance is already updated via the new edge, then the next relaxation via b would capture it. 

Alternatively, maybe the correct approach is to run the Floyd-Warshall algorithm with all nodes as intermediates, but only once. Wait, no, that's O(n^3) again. So perhaps this approach is not feasible.

Alternatively, maybe after adding the new edge, we can run three iterations of the Floyd-Warshall steps: once for a, once for b, and once for all other nodes. But I'm not sure.

Wait, here's a possible approach inspired by the paper "Dynamic shortest paths and transitive closure: algorithmic techniques and data structures" by Camil Demetrescu and Giuseppe F. Italiano. They discuss dynamic algorithms for maintaining all-pairs shortest paths. However, implementing those would be complex, and given the problem constraints, perhaps there's a simpler approach.

Let me think again. The initial matrix is already a valid all-pairs shortest path matrix. So when we add a new edge, we can model this as an edge with a certain length. If this edge's length is shorter than the existing distance between a and b, then adding it could reduce some of the paths.

So the steps would be:

For each new edge (a, b, c):

1. Check if c < d[a][b]. If not, the sum remains the same. So we just output the same sum as before. No changes needed.

2. If c is smaller, then we need to update the distance between a and b to c, and then check for all pairs (i, j) whether their distance can be improved by going through a or through b.

But how to efficiently compute all the possible improvements?

Another idea: for each pair (i, j), the new possible distance is min(d[i][j], d[i][a] + c + d[b][j], d[i][b] + c + d[a][j]). So after updating a and b's distance, we can iterate over all pairs (i, j) and check these three possibilities.

But then, after this initial update, there might be more improvements. For example, if i and j's distance is updated, then other pairs that go through i or j could also be updated.

But handling all possible such updates would require a full Floyd-Warshall pass, which is O(n^3), which is too slow.

Wait, but perhaps when we add a new edge (a, b), the only way that the shortest paths can change is if there's a path that goes through a and/or b. So, the shortest paths that can be affected are those that can be improved by going through a or b. So, maybe we can perform three steps:

- Update the distance between a and b to c if it's better.

- Then, for all i and j, check if the path i -> a -> b -> j is better than current.

- Then, check if the path i -> b -> a -> j is better than current.

But after that, maybe there's a path that uses a and then another node, but perhaps that's already captured by the Floyd-Warshall steps. Hmm.

Alternatively, perhaps the correct approach is to run the Floyd-Warshall algorithm but only for the nodes a and b. Let me think.

The Floyd-Warshall algorithm works by considering each node k as an intermediate. For each k, it checks if going through k can provide a shorter path between i and j. So after adding the new edge (a, b), the only intermediates that could have changed are a and b. So, we can re-run the Floyd-Warshall algorithm but only for k = a and k = b. 

Let's see: 

When we add the new edge, the distance between a and b is updated. Then, for each i and j, considering a as an intermediate (k=a), we check if i->a->j is better. Similarly for k=b.

But if we process a and b as intermediates, then all pairs i and j would have their distances checked via a and via b. This could capture all possible improvements due to the new edge.

Yes, this makes sense. Because the new edge's addition can only affect paths that go through a or b. So by running the Floyd-Warshall steps for k=a and k=b, we can propagate all possible improvements.

So the algorithm would be:

For each new road (ai, bi, ci):

1. a = ai, b = bi, c = ci.

2. current_dist = d[a][b]

3. if c >= current_dist: do nothing.

4. else:

   a. Update d[a][b] = c

   b. Update d[b][a] = c

   c. For each k in [a, b]:

       i. For all i in 1..n:

           j. For all j in 1..n:

               if d[i][j] > d[i][k] + d[k][j]:

                   d[i][j] = d[i][k] + d[k][j]

                   d[j][i] = d[i][j]  # since the graph is undirected

So this would take O(2 * n^2) operations per new edge. For n=300, 2 * 300^2 = 180,000 per edge, and for k=300 edges, 54,000,000 operations. Which should be manageable in Python under 2 seconds.

Let's verify with the first example:

Sample Input 1:

2

0 5

5 0

1

1 2 3

After adding the edge between 1 and 2 with length 3, the distance between 1 and 2 is updated to 3. Then, since k is 1 and 2 (the new a and b), we process them as intermediates.

Processing k=1: for all i and j, check if d[i][1] + d[1][j] < d[i][j]. But since there are only two nodes, the only pair (1,2) would have d[1][2] = 3, which is already the minimum.

Processing k=2: same as above.

So the sum is 3, which is correct.

Sample Input 2:

3

0 4 5

4 0 9

5 9 0

Adding the first new road (2,3,8). The existing distance between 2 and 3 is 9, which is longer than 8. So update d[2][3] and d[3][2] to 8.

Then, process k=2 and 3 as intermediates.

For k=2:

Check all i and j.

i=1, j=3:

d[1][3] is 5. Check d[1][2] + d[2][3] = 4 +8=12. No improvement.

i=2, j=1: already 4.

i=3, j=2: 8.

For other pairs, no changes.

Then process k=3:

Check i=1, j=2: current d[1][2] is 4. Check d[1][3] + d[3][2] =5 +8=13. So no improvement.

i=2, j=1: same.

So after adding the first road, the sum is 4 (1-2) +5 (1-3) +8 (2-3) = 17. Which matches the sample output.

Then adding the second road (1,2,1). The existing distance between 1 and 2 is 4. The new road has c=1, which is shorter. So update d[1][2] and d[2][1] to 1.

Then process k=1 and k=2.

For k=1:

Check all pairs.

For i=1, j=2: 1.

i=1, j=3: current is 5. Check d[1][1] + d[1][3] = 0+5=5. No change.

For i=2, j=3: current is 8. Check d[2][1] + d[1][3} =1+5=6. So this updates d[2][3} to 6. Then d[3][2} also becomes 6.

For i=3, j=2: same as above.

Then for k=2:

Check all pairs again.

i=1, j=3: current is 5. Check d[1][2} +d[2][3} =1+6=7. No change.

i=2, j=3: 6.

i=3, j=1: Check d[3][2} + d[2][1} =6 +1=7. Which is worse than current 5.

So after processing k=1 and k=2, the distances are:

1-2:1, 1-3:5, 2-3:6.

Sum is 1+5+6 =12, which matches the sample.

So this approach works for the sample.

So the plan is:

- Read the initial distance matrix.

- Compute the initial sum of all pairs (i < j) distances.

- For each new road:

   a. Check if the new road's length is shorter than the current distance between a and b. If not, the sum remains the same.

   b. If it is shorter, update d[a][b] and d[b][a] to c.

   c. Then, for k in [a, b], perform a Floyd-Warshall-style relaxation step for all pairs (i, j), checking if using k as an intermediate node gives a shorter path.

   d. Recompute the sum after each addition.

Now, the key is to implement this efficiently.

In Python, for n=300, n^2 is 90,000 operations. For each new road, two passes (for a and b) over all pairs. So 2 * 90,000 = 180,000 operations per road. For 300 roads, that's 54 million operations. Which should be manageable.

Also, the initial sum can be computed once. Then, after each road addition, the sum can be computed by re-calculating all pairs. But recomputing the sum each time would take O(n^2) time, which for n=300 is 90,000 operations per road. So for 300 roads, that's 27 million operations, which is acceptable.

Wait, but the sum is the sum of all d[i][j] for i < j. So after each road addition, even if we don't change the matrix, we need to compute this sum again.

Wait, no. Because for each new road, after processing it, the sum is the sum of the updated matrix. So even if the new road doesn't change any distances (because c was larger than existing d[a][b]), the sum remains the same as before.

So the steps are:

- Compute the initial sum.

- For each road:

   - If the new road is not better than existing a-b, output the current sum and continue.

   - Else, process the updates to the matrix, then compute the new sum.

But recomputing the sum each time from scratch would be O(n^2), which is acceptable. However, for n=300, 300^2 = 90,000 elements. For 300 roads, that's 300 * 90,000 = 27,000,000 operations, which is manageable.

But maybe there's a way to compute the sum incrementally. However, given that the sum can be computed in O(n^2) time and that 27 million is manageable, perhaps it's better to just compute it each time.

So the steps in code would be:

Read n.

Read n lines, each with n integers. Store as a 2D list (d).

Compute the initial sum as sum(d[i][j] for i in range(n) for j in range(i+1, n)).

Read k.

For each of the k roads:

   Read a, b, c. Convert to zero-based or one-based indices (the input uses 1-based, so need to subtract 1 if code uses zero-based).

   a -= 1

   b -= 1

   if d[a][b] > c:

       update d[a][b] and d[b][a] to c.

       for k in [a, b]:

           for i in range(n):

               for j in range(n):

                   new_dist = d[i][k] + d[k][j]

                   if new_dist < d[i][j]:

                       d[i][j] = new_dist

                       d[j][i] = new_dist  # since the graph is undirected

       # Now compute the new sum

   current_sum = sum(d[i][j] for i in range(n) for j in range(i+1, n))

   add current_sum to the output list.

Wait, but in Python, for loops are slower than in C++. So for n=300, the inner loops for i and j (each up to 300) would be 300*300 = 90,000 iterations. For two k's (a and b), that's 180,000 per road, multiplied by 300 roads is 54 million. Which in Python might be tight, but perhaps manageable.

Alternatively, perhaps precompute a list of all pairs (i, j) where i < j, and then sum d[i][j] for each of those. But in Python, even that may take some time.

Let me think about the code structure.

The initial sum is sum of d[i][j] for all i < j.

In code:

n = int(input())

d = []

for _ in range(n):

    row = list(map(int, input().split()))

    d.append(row)

current_sum = 0

for i in range(n):

    for j in range(i+1, n):

        current_sum += d[i][j]

Then, for each new road:

a, b, c = map(int, input().split())

a -= 1

b -= 1

if d[a][b] > c:

    d[a][b] = c

    d[b][a] = c

    # Now, perform Floyd-Warshall steps for k = a and k = b

    for k in [a, b]:

        for i in range(n):

            for j in range(n):

                if d[i][k] + d[k][j] < d[i][j]:

                    d[i][j] = d[i][k] + d[k][j]

                    d[j][i] = d[i][j]  # since it's undirected

    # compute new sum

    current_sum = 0

    for i in range(n):

        for j in range(i+1, n):

            current_sum += d[i][j]

output.append(current_sum)

else:

    output.append(current_sum)

But in Python, even with n=300, the sum computation is O(n^2), which is 90,000 per iteration. For 300 roads, that's 27,000,000 operations. Which is acceptable. But perhaps we can optimize the sum computation.

Wait, but in the code above, even when the new road doesn't change the matrix, the sum is not recomputed. So for each road, the code appends the current sum (which is either the same as before if the road didn't help, or recomputed if it did).

So the code is correct.

But in Python, the code needs to be as efficient as possible. So perhaps we can precompute all the pairs (i, j) where i < j and store them in a list, and then iterate through that list each time. But I'm not sure if that's faster.

Alternatively, for the sum computation, use a generator expression:

current_sum = sum(d[i][j] for i in range(n) for j in range(i+1, n))

But in Python, for loops are generally slower than list comprehensions or generator expressions, but in this case, perhaps it's better to use the generator expression since it's more concise and may be optimized.

But for n=300, this would generate (300*299)/2 = 44850 elements. Summing over 44k elements per iteration. For 300 iterations, that's 13,455,000 elements. Which is manageable.

But how does this compare to nested loops?

In Python, generator expressions are usually efficient. Let's see:

sum(d[i][j] for i in range(n) for j in range(i+1, n))

This is a generator expression that loops i from 0 to n-1, and for each i, j from i+1 to n-1, and sums d[i][j].

Yes, this is correct and efficient.

So in code, after the road processing, we can compute current_sum as such.

But when the road is processed and the matrix is updated, we have to recompute the sum.

So the code's structure would be:

Read n.

Read the distance matrix.

Compute initial sum.

Read k.

Process each of the k roads:

   a, b, c = read input.

   adjust a and b to zero-based.

   if the current distance between a and b is > c:

       update the distance.

       run the two Floyd-Warshall steps for k = a and k = b.

       recompute the sum.

   append the current sum to the output.

Finally, print the output list as space-separated values.

Now, testing this approach.

Sample Input 1:

2

0 5

5 0

Initial sum is 5.

Add road 1-2 (after conversion, 0 and 1) with c=3. Since 5>3, update d[0][1] and d[1][0] to 3.

Then run for k in [0, 1]:

For k=0:

   for all i and j:

      check if d[i][0] + d[0][j] is less than d[i][j]

   For i=0, j=1: 0 + 3 =3, which is already the current value. No change.

For k=1:

   same as above.

So the sum is 3.

Sample Input 2:

After adding the first road (2-3, 8), which is better than 9.

Update d[1][2] and d[2][1] to 8.

Then run for k=1 and 2.

For k=1 (assuming zero-based, the road is between 1 and 2 (since the input is 2 3 8, but after conversion, 1 and 2):

So k=1:

   for all i and j:

      check if d[i][1] + d[1][j] < d[i][j]

   For example:

i=0, j=2 (original d[0][2] is 5):

d[0][1] is 4, d[1][2] is 8. 4+8=12 >5. So no change.

i=1, j=2: 8.

i=2, j=0: same as before.

But after processing k=1, maybe some other pairs are updated.

Then k=2:

for all i and j:

   check if d[i][2] + d[2][j] < d[i][j]

i=1, j=0:

d[1][2] is 8, d[2][0] is 5. 8+5=13. d[1][0] is 4. So no change.

i=0, j=2:

d[0][2] is 5, d[0][2] (i=0, k=2) is 5, d[2][j=2] is 0. So 5+0=5. No change.

So the sum becomes 4 (0-1) +5 (0-2) +8 (1-2) = 17.

Then add the next road (1-2, 1). Which in zero-based is 0 and 1. The current distance is 4, which is greater than 1. So update d[0][1] and d[1][0] to 1.

Then run for k=0 and 1.

Processing k=0:

for all i and j:

i=0, j=2: d[i][0] (1) + d[0][j] (5) = 6. Which is larger than current d[0][2] (5). No change.

i=1, j=2: d[1][0] (1) + d[0][2] (5) =6. Which is less than current 8. So update d[1][2] to 6.

Also, since the matrix is symmetric, d[2][1] is also updated to 6.

Then, processing k=1:

for all i and j:

i=0, j=2: d[0][1] (1) + d[1][2] (6) =7 >5. No change.

i=2, j=1: already 6.

So after processing both k=0 and 1, the distances are:

0-1:1, 0-2:5, 1-2:6. Sum is 1+5+6=12.

Which matches the sample.

Thus, the approach works.

Now, to code this in Python.

But we need to be careful with zero-based indices.

Another thing to note: when reading the initial distance matrix, the input is given as a matrix where di,j is the distance between i and j. Since the graph is undirected, the matrix is symmetric, which is already handled by the problem.

So the code steps are:

Read n.

Read n lines, each with n integers. Append each line to the d list.

Compute the initial sum as the sum of d[i][j] for all i < j.

Read k.

Process each of the k roads:

   Read ai, bi, ci. ai and bi are 1-based, so convert to zero-based by subtracting 1.

   a, b = ai-1, bi-1.

   if d[a][b] > ci:

       d[a][b] = ci

       d[b][a] = ci

       for k in [a, b]:

           for i in range(n):

               for j in range(n):

                   new_dist = d[i][k] + d[k][j]

                   if new_dist < d[i][j]:

                       d[i][j] = new_dist

                       d[j][i] = new_dist  # since the graph is undirected

       # Recompute the sum.

       current_sum = sum(d[i][j] for i in range(n) for j in range(i+1, n))

   else:

       # No change, current_sum remains as before.

   append current_sum to the output list.

At the end, print the output list as space-separated integers.

Now, let's test the code with sample input 2.

Sample Input 2:

3

0 4 5

4 0 9

5 9 0

After reading, the distance matrix is:

d[0][0] =0, d[0][1]=4, d[0][2]=5

d[1][0]=4, d[1][1]=0, d[1][2}=9

d[2][0}=5, d[2][1}=9, d[2][2}=0

Initial sum is 4 (0-1) +5 (0-2) +9 (1-2) = 18? Wait, but the sample output is 17 after the first road. Oh, sample input 2's initial matrix is:

First line: 0 4 5 → [0,4,5]

Second line:4 0 9 → [4,0,9]

Third line:5 9 0 → [5,9,0]

The sum is (0<1:4) + (0<2:5) + (1<2:9) → 4+5+9=18. But the first new road is (2,3,8) which is 1-based, so a=1, b=2 (zero-based). The existing distance is 9. So after adding this road, the new distance between 1 and 2 is 8. So the sum becomes 4 (0-1) +5 (0-2) +8 (1-2) →4+5+8=17. Which matches the sample output.

So the code seems correct.

Potential optimizations:

In the code, when updating the distance matrix during the Floyd-Warshall steps, for each k (a or b), we iterate over all i and j. For each i and j, we compute new_dist = d[i][k] + d[k][j], and if it's less than d[i][j], we update d[i][j] and d[j][i].

But in Python, loops are slow. So perhaps we can find a way to vectorize or optimize this step.

But given the constraints, it's manageable.

Another possible optimization is to precompute the pairs (i, j) for i < j and sum them, but the code as written uses a generator expression which is efficient.

Now, for the code:

Read n.

Read n lines.

Compute the sum.

Read k.

Process each road.

Now, code:

n = int(input())
d = []
for _ in range(n):
    row = list(map(int, input().split()))
    d.append(row)
current_sum = sum(d[i][j] for i in range(n) for j in range(i + 1, n))
k = int(input())
output = []
for _ in range(k):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if d[a][b] > c:
        # Update the direct distance
        d[a][b] = c
        d[b][a] = c
        # Run Floyd-Warshall for k in [a, b]
        for k_node in [a, b]:
            for i in range(n):
                for j in range(n):
                    new_dist = d[i][k_node] + d[k_node][j]
                    if new_dist < d[i][j]:
                        d[i][j] = new_dist
                        d[j][i] = new_dist  # since undirected
        # Recompute the sum
        current_sum = sum(d[i][j] for i in range(n) for j in range(i + 1, n))
    output.append(str(current_sum))
print(' '.join(output))

Wait, but in Python, the loop variables can't be named 'k' because there's a variable named k (the number of roads). So in the code above, the loop variable is named k_node.

Yes, that's correct.

Testing this code with sample input 1:

Sample Input 1:

2

0 5

5 0

1

1 2 3 → a=0, b=1, c=3.

d[a][b] is 5 >3 → update to 3.

Then run for k_node in [0, 1].

For k_node=0:

Loop i from 0 to 1.

i=0:

j=0: d[0][0] +d[0][0] →0+0=0 → no change.

j=1: d[0][0] (0) + d[0][1] (3) =3 → current d[0][1] is 3 → no change.

i=1:

j=0: d[1][0] (3) + d[0][0] (0) =3 → current d[1][0] is 3 → no change.

j=1: no change.

k_node=1:

Same as k_node=0. No changes.

Sum is 3.

Which is correct.

Sample input 2:

After the first road (2 3 8 → a=1, b=2 in zero-based):

current distance between a and b is 9>8 → update to 8.

Then run for k_node=1 and 2.

Processing k_node=1:

for all i and j.

For i=0:

j=0: d[0][1] (4) +d[1][0] (4) →8 → d[0][0] is 0. No change.

j=1: 4+0=4 → no change.

j=2: 4+8=12 → current d[0][2] is5. 12>5 → no change.

For i=1:

j=0: 0+4=4 → no change.

j=2: 0+8=8 → current d[1][2] is8 → no change.

For i=2:

j=0: d[2][1] (8) +d[1][0] (4) →12 → current d[2][0] is5 → no change.

Processing k_node=2:

for i=0:

j=0: 5+5=10 → no change.

j=1: d[0][2] (5) + d[2][1] (8) →13 → current d[0][1] is4 → no change.

j=2: 5+0=5 → no change.

i=1:

j=0: d[1][2] (8) + d[2][0] (5) →13 → no change.

j=2: 8+0=8 → no change.

i=2:

j=0: 0+5=5 → no change.

j=1:0+8=8 → no change.

So after processing both k_node=1 and 2, the distance matrix is:

0 4 5

4 0 8

5 8 0

The sum is 4+5+8=17.

Then, adding the second road (1 2 1 → a=0, b=1 in zero-based, c=1). Current d[a][b] is 4>1 → update to 1.

Then process k_node=0 and 1.

Processing k_node=0:

For all i and j.

i=0:

j=0:0+0=0 → no change.

j=1:1 → no change.

j=2:0+5=5 → no change.

i=1:

j=0:1 → no change.

j=1:0 → no change.

j=2:1+5=6 → current d[1][2] is8 → update to6.

i=2:

j=0:5 → no change.

j=1:5+1=6 → current d[2][1] is8 → update to6.

j=2:0 → no change.

So after processing k_node=0, the matrix is:

0 1 5

1 0 6

5 6 0

Then process k_node=1:

For all i and j.

i=0:

j=0:1+1=2 → no.

j=1:1 → no.

j=2:1+6=7 → current d[0][2] is5 → no change.

i=1:

j=0:0+1=1 → no change.

j=2:0+6=6 → no change.

i=2:

j=0:6+1=7 → current d[2][0] is5 → no change.

j=1:6 → no change.

So after processing k_node=1, the matrix remains the same.

Sum is (0-1:1) + (0-2:5) + (1-2:6) → sum is 12.

Which is correct.

Thus, the code works.
</think>

```python
n = int(input())
d = []
for _ in range(n):
    row = list(map(int, input().split()))
    d.append(row)
current_sum = sum(d[i][j] for i in range(n) for j in range(i + 1, n))
k = int(input())
output = []
for _ in range(k):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if d[a][b] > c:
        d[a][b] = d[b][a] = c
        for k_node in (a, b):
            for i in range(n):
                for j in range(n):
                    new_dist = d[i][k_node] + d[k_node][j]
                    if new_dist < d[i][j]:
                        d[i][j] = d[j][i] = new_dist
        current_sum = sum(d[i][j] for i in range(n) for j in range(i + 1, n))
    output.append(str(current_sum))
print(' '.join(output))
```