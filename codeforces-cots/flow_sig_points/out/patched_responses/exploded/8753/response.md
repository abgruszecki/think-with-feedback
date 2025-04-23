<think>
Okay, let's tackle this problem. Hmm. So, the problem is about a knight tournament where each fight eliminates all knights in a certain range except the winner. We need to determine for each knight who defeated them, or 0 if they are the overall winner.

The key thing here is that each fight affects a range [li, ri], and only xi remains. So for any knight in that range (except xi), they get eliminated by xi in that fight. But once a knight is eliminated, they can't participate in future fights. So, we need to track for each knight, the earliest fight in which they are part of a range and thus get eliminated.

Wait, but how do we efficiently track which knights have been eliminated already? Because if a knight was eliminated in an earlier fight, they won't be part of later fights, even if the later fight's range includes them. So for each knight, the first fight that includes them (and isn't the one where they are the winner) determines their conqueror.

So the problem reduces to, for each knight i, find the earliest fight where i is in [l_j, r_j], and i is not the winner x_j. Then the conqueror of i is x_j. If there's no such fight (which is only possible if the knight is the overall winner x_m), then output 0.

But how do we compute this efficiently given the constraints (n and m up to 3e5)?

The naive approach would be for each fight, iterate through all knights in [l_j, r_j], and if they haven't been assigned a conqueror yet, set it to x_j. But this is O(m * (r_j - l_j + 1)), which is way too slow for m up to 3e5 and ranges that can be up to 3e5 in size each. So total operations could be up to 9e10, which is impossible.

So we need a smarter data structure that allows us to track which knights are still active (i.e., not yet eliminated) and can be assigned a conqueror in each fight.

Hmm. So the idea is that once a knight is eliminated, we don't process them again. So for each fight j, we need to assign x_j as the conqueror to all knights in [l_j, r_j] who haven't been assigned yet.

This sounds similar to the interval query problem where we need to mark ranges and track unmarked elements. The key here is to efficiently find the unmarked elements in a given range [l_j, r_j], mark them (assign their conqueror to x_j), and then skip those in future steps.

A data structure that can help with this is a Disjoint Set Union (DSU) structure, also known as Union-Find. The DSU can help keep track of the next available element that hasn't been processed yet. 

Wait, I remember a problem where you have to paint intervals and track which cells are unpainted. The approach there was to use a DSU where each node points to the next unpainted cell. So for example, when you process a range from l to r, you iterate through the cells starting from l, and for each cell, you assign the conqueror and then union it with the next cell. But that's O(alpha(n)) per operation, which is efficient.

So here's the plan: For each knight, we need to track whether they have been eliminated already. If not, when processing a fight [l_j, r_j], we need to assign x_j as the conqueror to all knights in [l, r] that are still active (excluding x_j itself). Then, mark those knights as eliminated.

But how to handle the exclusion of x_j? Because even if x_j is in the range, it's the winner, so it's not eliminated. So during the processing of the fight j, the conqueror for x_j is not set here. So for the fight j, the range [l_j, r_j] includes x_j, but we need to assign x_j to all other knights in this range that are active.

So, for the fight j, we process all knights in [l_j, r_j] except x_j. Those knights get their conqueror set to x_j (if not already set). Then, x_j's conqueror is determined by subsequent fights (if any) that include it and it loses, or it remains as the overall winner.

So, the DSU approach would need to find all active knights in [l_j, r_j], except x_j, and assign their conqueror to x_j. Then, mark those as inactive.

But how to do this efficiently?

Let me think. Let's maintain a DSU structure where for each node i, parent[i] is the next available node that hasn't been processed. Initially, parent[i] = i. When we process a range [l, r], we want to find all nodes in [l, r] (excluding x_j) that are still active. For each such node, we set conqueror[i] = x_j, and then we need to mark them as processed so that they are not considered in future fights.

But the DSU can help us find the next available node quickly. Here's how it works:

- The DSU's find function returns the next available node. For example, if we have processed node i, then parent[i] = i+1. Then, when we try to find nodes in a range, we can jump through the DSU structure to find nodes that are still available.

So, for each fight j (processing in order, since later fights can't affect the conqueror once it's set), we need to process the range [l_j, r_j], except x_j. The steps would be:

1. Start from l_j. Find the first available node >= l_j. While current node <= r_j:
   a. If current node is x_j, skip it (don't process it here).
   b. Else, set conqueror[current node] = x_j.
   c. Union current node with current node + 1 (so next find starts from the next node).
   d. Move to the next available node (using DSU's find function).

But wait, the DSU approach for the paint problem works as follows: when you process a range [a, b], you start from a, find the next available node (using find), if it's <= b, you process it, then union it with the next node. This way, each node is processed exactly once.

In our case, during each fight j, we need to process all nodes in [l_j, r_j] except x_j, and only those that haven't been processed yet.

So, for each fight j:

- We need to process all nodes in [l_j, r_j] that are still active (i.e., conqueror is 0), except x_j.

But how to efficiently find those nodes and mark them as processed.

So the DSU approach would be:

We have a parent array where parent[i] is the next node available. Initially, parent[i] = i.

When processing a fight with l, r, x:

- For the range [l, r], we want to find all nodes in this range (except x) that are unprocessed.

So, for each node in [l, r], except x, we check if it's unprocessed, and if so, set conqueror[i] = x.

But again, iterating through each node is O(r - l + 1), which is too slow.

Thus, we can use the DSU to find the next available node in the range.

Here's the approach:

1. For the current fight's [l, r], x:

   a. Find the first available node in l to r.

   b. For each such node, if it's not x, assign conqueror[node] = x, then union it with node+1.

   c. However, x might be in the range. So after processing all nodes except x, we have to make sure that x is still in the DSU as available (if it wasn't processed in this fight).

But wait, in a fight, x is the winner. So x remains in the tournament and can participate in future fights. So x's conqueror is not set here. So during processing this fight, x is not processed (only others are). So when handling the range [l, r], x is part of the range, but is skipped.

So, during processing this fight, the nodes to process are those in [l, r], but not x. So when using the DSU approach, how do we skip x?

Hmm. Let's think:

The DSU approach would process all available nodes in [l, r]. But x may be part of this range. So when we find a node that is x, we need to skip processing it (i.e., do not assign conqueror and do not mark it as processed).

But how?

So, when during processing, we find a node in [l, r], and it's available. We check if it's x. If not, process it. If it is x, we skip it (but leave it available for future fights).

But how to handle the DSU in this case?

Wait, the DSU is designed to track nodes that are available. So x is in the range, and if it's available (i.e., hasn't been processed before), we need to leave it available. So in this fight, when processing the range [l, r], we process all available nodes except x.

So, the algorithm would be:

For each fight in order:

   l, r, x = current fight's parameters.

   current_node = find(l)  # find the first available node >= l.

   while current_node <= r:

       if current_node != x:

           conqueror[current_node] = x

           # merge current_node with current_node + 1

           union(current_node, current_node + 1)

       else:

           # x is skipped. But need to process nodes after x?

           # So after x, the next node to process is x+1.

           # So we need to check if x+1 is in the range and available.

           # How? Maybe we can manually move to x+1.

           pass

       # After processing current_node (or skipping if it's x), find the next node.

       current_node = find(current_node + 1)

But wait, in the DSU, when we process a node, we merge it with current_node+1. So next time, find(current_node) would return current_node+1.

But for x, we don't process it. So x remains in the DSU. For example, if x was available, the next time when processing a fight that includes x, x will be considered again (unless it's processed in another fight where it's not the winner).

So the code would process the nodes in [l, r], and for each node in the range, if it's available and not x, it's processed (conqueror set to x), and marked as processed (merged into the next node). For x, even if it's available, it's skipped. So x remains in the DSU structure.

But how to handle the case where x is not in the current DSU (i.e., has already been processed in a previous fight)? Then, during this fight's processing, x would have already been marked as processed, so it's skipped here.

Wait, but x can't be processed in a previous fight. Because if x was part of a previous fight's range (and wasn't the winner of that fight), then he would have been processed and his conqueror set to that fight's winner. But if he was the winner of a previous fight, then he's still active, so in the DSU, he's still available.

So, the DSU structure tracks all knights that haven't been processed (i.e., their conqueror is not yet set). So, for each fight, when we process the nodes in [l, r], except x, the DSU allows us to find those nodes quickly.

But how to handle the case where x is in [l, r] but hasn't been processed yet. Then, during this fight, x is not processed. So in the next fights, x can still be part of other ranges.

But in this case, x is the winner of this fight. So he remains in the tournament. So in future fights, if he is part of a range, he might be processed (if he's not the winner of that fight).

So the DSU approach is correct. Let's outline the steps:

Initialize a conqueror array with 0s.

Initialize DSU parent array, where parent[i] = i for all i from 1 to n+1. (n+1 is a sentinel to avoid boundary checks.)

For each fight in order (from first to m-th):

   l, r, x = current fight.

   current = find(l)

   while current <= r:

       if current != x:

           conqueror[current] = x

           # Merge current with current + 1

           union(current, current + 1)

           current = find(current + 1)

       else:

           # Skip x, but need to find the next node after x.

           # So, set current to find(x + 1)

           current = find(x + 1)

So, in this approach, when current is x, we skip it and look for the next available node starting from x+1.

But how does the DSU's find work here? Let's see.

The DSU's find function is path compressed, so when you call find(x), it returns the root of x. For available nodes, the root is the next available node. So for example, if nodes 1, 2, 3 are available (parent[i] = i), then find(1) returns 1. After processing 1, union(1, 2), so parent[1] = 2. Next, find(1) returns 2. Then, processing 2 would set conqueror[2], then union(2,3), etc.

So in the code above, for each current node found in the loop, if it's not x, we process it (set conqueror) and merge it with the next node. If it is x, we skip it and jump to x+1.

But wait, the x could be part of the range [l, r], but even if x is in the DSU (available), we skip it. So x remains in the DSU, available for future fights.

But in this case, x is the winner of this fight. So he remains in the tournament. So in future fights, if x is in their ranges and is not the winner, then he will be processed (conqueror set to that fight's winner).

So this logic works.

Now, the key is implementing the DSU with path compression and union by rank (or similar) to make find and union operations O(alpha(n)) time.

But what about the size of the data structures? For n up to 3e5, we need a parent array of size n+2 (to handle up to n+1). This is manageable.

Now, let's test this approach against the sample input.

Sample input 1:

4 3

1 2 1

1 3 3

1 4 4

Conqueror array initialized to [0, 0, 0, 0]

First fight: l=1, r=2, x=1.

Processing the range [1,2].

current = find(1) → 1.

current is 1, which is x=1 → skip.

current becomes find(2).

find(2) returns 2 (since not processed yet).

2 is not x=1, so conqueror[2] =1.

Merge 2 and 3. Parent[2] =3.

current becomes find(3). 3 is >2 (r=2). So loop ends.

So after first fight, conqueror is [0,1,0,0].

Second fight: l=1, r=3, x=3.

current = find(1) →1.

1 is not x=3, so conqueror[1] =3. Merge 1 and 2.

Parent[1] =2. Then current becomes find(2) which is 3 (since parent[2] was set to 3 in the first step).

3 is <=3.

3 is x=3 → skip. current becomes find(4). 4>3 → loop ends.

So after second fight, conqueror is [3,1,0,0].

Third fight: l=1, r=4, x=4.

current = find(1). Let's see:

Parent[1] is 2. Parent[2] is 3. Parent[3] is 3 (since in first fight, 2 was merged with 3. Then, after second fight, after processing 1, parent[1] is 2, and 2's parent is 3. Then, when processing 3 in the third fight:

find(1) → find(2) → find(3) →3.

current =3.

3 is <=4, and not x=4.

So conqueror[3] =4. Merge 3 and 4.

current becomes find(4) →4.

4 is <=4.

4 is x=4 → skip. current becomes find(5) →5>4. loop ends.

So conqueror array is [3,1,4,0], which matches the sample output.

So the approach works for this case.

Now, the second sample input:

8 4

3 5 4 → fight 1: l=3, r=5, x=4.

3 7 6 → fight 2.

2 8 8 → fight 3.

1 8 1 → fight 4.

Output: 0 8 4 6 4 8 6 1.

Let's see how the code would process these.

Conqueror starts as all zeros.

Fight 1: l=3, r=5, x=4.

current = find(3) →3.

3 is not x=4 → conqueror[3] =4. merge 3 and4. parent[3] =4.

current becomes find(4) →4. 4 is x=4 → skip. current becomes find(5). 5 is in [3,5], 5 not x=4. conqueror[5] =4. merge 5 and6. current becomes find(6) →6>5 → loop ends.

So after fight1: conqueror for 3 and5 are 4.

Fight2: l=3, r=7, x=6.

current = find(3) →4 (since parent[3] was set to4 in fight1). 4 is in [3,7], and 4 !=6. So conqueror[4] =6. merge 4 into 5. parent[4] =5.

current becomes find(5) →5 (since parent[5] was set to6 in fight1's processing of 5). 5 is in [3,7], 5 !=6. conqueror[5] is already 4 (from fight1). Wait, no: in fight2, the current node is 5, which was processed in fight1 (conqueror set to4). So in DSU, 5's parent would be 6 (after fight1). So when fight2 processes, find(3) → find(4) → find(5) →6. Because:

After fight1:

parent[3] =4

parent[4] =5 (from fight2's processing of 4?)

Wait, perhaps I need to track the DSU steps more carefully.

But perhaps the code would process fight2 as follows:

After fight1, conqueror is [0,0,4,0,4,0,0,0].

DSU parent after fight1:

1:1, 2:2, 3:4, 4:4, 5:6, 6:6,7:7,8:8.

Fight2 is l=3, r=7, x=6.

current = find(3) → find(3's parent is4. find(4) is4. Then, 4 is in [3,7], 4 !=6. So conqueror[4] is set to6. Then, union(4,5). So parent[4] =5.

current becomes find(5) →5. 5 is in [3,7], 5 !=6. conqueror[5] is 4 (already set). Wait, but in fight2's processing, the current node is5, but in the DSU, after fight1, 5's parent is6. So when processing fight2:

current starts at find(3). Let's see:

parent[3] is4. So find(3) would go to4. Then, find(4) returns4 (since parent[4] is4). So current=4.

4 is in [3,7], and not x=6. So set conqueror[4] to6. Merge 4 and5 (parent[4] =5). Then, current becomes find(5) →5. parent[5] is6 (from fight1's processing). So current=5 is in [3,7], and not x=6. So set conqueror[5] to6. Wait, but in fight1, 5's conqueror was set to4. But here, during fight2, if 5 is still available (i.e., not processed before), then we would set it to6. But in fight1, during the first fight's processing, 5 was processed (conqueror set to4, merged with6). So during fight2's processing, find(5) would return6 (since parent[5] is6). So 5 is not available, so it's not processed again.

Ah, right. So after fight1, 5's conqueror is4, and in the DSU, 5's parent is6. So during fight2's processing, when current reaches5, the find(5) would return6. Because the DSU's find function returns the next available node. So if a node has been processed, its parent points to a higher node.

So let's re-examine fight2's processing:

current = find(3). 

After fight1, parent[3] is4, parent[4] is4 (since after fight1, 4 was not processed yet). So find(3) would return4.

current=4. 4 is in [3,7], and 4 is not x=6. So conqueror[4] =6. Merge 4 and5 (parent[4]=5). Then, current becomes find(5). parent[5]=6. find(5) returns6. 6 is in [3,7], and 6 is x=6 → skip. current becomes find(7). 7 is in [3,7], and not x=6. conqueror[7] =6. Merge 7 and8. current becomes find(8) →8>7 → loop ends.

So after fight2, conqueror[4] is6, 7 is6. Others in the range 3-7 that are available (like6 is x=6, so skipped. 5 is already processed in fight1, so DSU's find would point to6, which is in the range but is x=6, so skipped. Then, after 6, 7 is processed.

So after fight2, the conqueror array is:

[0,0,4,6,4,0,6,0].

Fight3: l=2, r=8, x=8.

current = find(2) →2. 2 is in [2,8], not x=8. So conqueror[2] =8. Merge 2 and3. current becomes find(3). parent[3] is4 (from fight1), then parent[4] is5 (from fight2's processing of4). So find(3) would return5. 5 is in [2,8], but parent[5] is6. find(5) is6. 6 is in [2,8], and x=8. So 6 is not x=8 → conqueror[6] =8. Merge6 and7. current becomes find(7) →7's parent is8. So 7 is in range. 7 not x=8 → conqueror[7] is6 (from fight2). Wait, no: in fight3, 7's conqueror is set to8. Wait, no. Let's re-examine.

Wait, during fight3's processing:

current = find(2) →2. conqueror[2] is set to8. merge 2 and3.

current becomes find(3) → find(3's parent is4 → parent[4] is5 → find(5) is6. So current=6.

6 is in [2,8], not x=8. So conqueror[6] is8. Merge6 and7. current becomes find(7) →7's parent is8 (from fight2's merge of7 and8). 7 is in [2,8], not x=8. So conqueror[7] is8. Merge7 and8. current becomes find(8) →8 is in range, but x=8. So skip. current becomes find(9) →9>8. Loop ends.

So after fight3:

conqueror[2] =8, 6=8, 7=8.

Fight4: l=1, r=8, x=1.

current = find(1) →1. x=1 → skip. current becomes find(2). parent[2] is3 (from fight3's processing). find(3) returns6 (from previous steps). 6 is in [1,8], not x=1. So conqueror[6] is8 (already set in fight3). So not processed again. Hmm, but wait, how?

Wait, during fight4:

current starts at find(1) →1. 1 is x=1, skip. current becomes find(2). find(2) → parent[2] is3. parent[3] is4. parent[4] is5. parent[5] is6. parent[6] is7 (after fight3's merge of6 and7). parent[7] is8. parent[8] is8.

So current becomes8. 8 is in [1,8], not x=1. So conqueror[8] is1. Merge8 into9. current becomes find(9) →9>8 → loop ends.

So after fight4, conqueror[8] is1.

The final array is:

0 (x=1 is the winner), 8,4,6,4,8,6,1.

Which matches the sample.

So the DSU approach works for the samples.

Now, the code.

Implementing this in Python:

We need a DSU with path compression and union to the right.

The DSU's parent array is 1-based up to n+1.

The conqueror array is initialized to 0s.

For each fight, process the range [l, r], and for each node found in the DSU:

   if node !=x, set conqueror[node] =x, and union(node, node+1).

So, the DSU's find function.

Implementing DSU:

We can represent the parent array as a list. Initially, parent[i] =i for all i from 1 to n+1.

The find function is path compressed.

def find(u):

    while parent[u] != u:

        parent[u] = parent[parent[u]]

        u = parent[u]

    return u

Union is simple: parent[u] =v.

But since we always union u to u+1, the union is straightforward. So when processing a node u, after setting conqueror[u] =x_j, we do union(u, u+1). So parent[u] =u+1.

So the code steps:

Read n and m.

Initialize parent as list from 0 to n+1 (since 1-based). parent[i] =i for 1<=i<=n+1.

Initialize conqueror array (1-based) as [0]*(n+1).

Process each of m fights in order:

   l, r, x = map(int, input().split())

   current = find(l)

   while current <= r:

       if current !=x:

           conqueror[current] =x

           # union current and current+1

           parent[current] = current +1

           # move to next

           current = find(current +1)

       else:

           # skip x, move to x+1

           current = find(x +1)

But wait, when current is x, we need to set current to find(x+1). Because x is in the range, but we don't process it. So after x, the next node to check is x+1.

So the loop continues until current exceeds r.

But how efficient is this? Each node is processed once, because once processed, their parent is set to current+1, so find will jump to the next available node. For m fights and n nodes, the time complexity is O(m + n*alpha(n)), which is acceptable for 3e5.

Now, in Python, using a list for parent. But for n up to 3e5, the parent list can be initialized as [i for i in range(n+2)].

But in Python, for 3e5 elements, this is manageable.

Now, the code.

But what about the DSU's find function? Implementing it as a function with path compression may be slow in Python for 3e5 elements. To optimize, perhaps we can use a recursive find with memoization. But recursion in Python is limited, so better to implement iteratively.

So, implement find as a loop:

def find(u):

    while parent[u] != u:

        parent[u] = parent[parent[u]]

        u = parent[u]

    return u

But in Python, we can't have a separate function for find because of the way variables are handled. So, we'll need to inline the find logic.

Alternatively, use a helper function. Let's proceed.

But in Python, for speed, the code must be optimized. So, for each 'current' in the loop, perform the find operation.

But how?

Let's code it.

Sample code:

n, m = map(int, input().split())

parent = list(range(n + 2))  # parent[i] for i from 0 to n+1

conqueror = [0]*(n+1)

for _ in range(m):

    l, r, x = map(int, input().split())

    current = l

    while True:

        # Find the next available node >= current

        # Find the root of current

        u = current

        while parent[u] != u:

            parent[u] = parent[parent[u]]

            u = parent[u]

        current_node = u

        if current_node > r:

            break

        if current_node != x:

            conqueror[current_node] = x

            # Union current_node with current_node +1

            parent[current_node] = current_node +1

            current = current_node +1

        else:

            # Skip x, move to x+1

            current = x +1

    # Alternative approach using find function.

Wait, perhaps using a helper function for find would be better. Let's implement find as a separate function.

But in Python, functions are allowed. Let's try.

Implementing find with path compression.

def find(u):

    while parent[u] != u:

        parent[u] = parent[parent[u]]

        u = parent[u]

    return u

But for large n, this function may be called many times, but with path compression, each find is O(alpha(n)).

So, the code would be:

n, m = map(int, input().split())

max_parent = n +1

parent = list(range(n +2))  # indexes 0 to n+1

conqueror = [0]*(n+1)

for _ in range(m):

    l, r, x = map(int, input().split())

    current = find(l)

    while current <= r:

        if current != x:

            conqueror[current] = x

            parent[current] = current +1

            current = find(current +1)

        else:

            current = find(x +1)

Finally, after all fights, output conqueror[1..n], with 0 for the winner.

But wait, the winner is x_m. So in the conqueror array, x_m has 0, which is correct.

But in the code, conqueror[x_m] is 0, unless it was part of a previous fight where it was not the winner.

But according to the problem statement, the input ensures that x_j is the winner of the j-th fight, and the last fight's x_m is the winner of the tournament.

Thus, the code correctly sets conqueror[x_m] to 0.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    import sys
    input = input_stream.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    parent = list(range(n + 2))  # parent[0] unused, 1..n+1
    conqueror = [0] * (n + 1)  # 1-based
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    for _ in range(m):
        l = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        x = int(data[idx])
        idx += 1
        
        current = find(l)
        while current <= r:
            if current != x:
                conqueror[current] = x
                parent[current] = current + 1
                current = find(current + 1)
            else:
                current = find(x + 1)
    
    print(' '.join(map(str, conqueror[1:n+1])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8 4
3 5 4
3 7 6
2 8 8
1 8 1
""",
            "output": \
"""\
0 8 4 6 4 8 6 1
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

Thus, the code should solve the problem.
</think>

```python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    parent = list(range(n + 2))  # parent[0] unused, 1..n+1
    conqueror = [0] * (n + 1)  # 1-based
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    for _ in range(m):
        l = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        x = int(data[idx])
        idx += 1
        
        current = find(l)
        while current <= r:
            if current != x:
                conqueror[current] = x
                parent[current] = current + 1
                current = find(current + 1)
            else:
                current = find(x + 1)
    
    print(' '.join(map(str, conqueror[1:n+1])))

if __name__ == "__main__":
    main()
```
