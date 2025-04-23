<think>
Okay, let's try to figure out how to solve this problem. The problem is about transforming materials according to some rules and checking if we can get enough of each required material. 

So, the input gives us for each material i (starting from 2) a parent xi and a ki. The transformations are such that you can convert ki kg of xi into 1 kg of i, and vice versa, 1 kg of i can be converted back into 1 kg of xi. But the processing requires that the amounts after conversion are integers. Wait, no, the problem statement says the equipment allows only such transformations that the resulting amount is an integer. So when converting, you have to make sure that the quantities are such that after conversion, you get whole numbers. Hmm, but how does that affect the solution?

Wait, the key is that each transformation is bidirectional but with a ratio. For example, for material i, you can convert from xi to i using ki:1 ratio. So to get 1 kg of i, you need to spend ki kg of xi. Conversely, 1 kg of i can be transformed into 1 kg of xi. Wait, no: the problem statement says that 1 kg of i can be transformed into 1 kg of xi. Wait, that's the reverse. So the forward and backward transformations have different ratios. So the possible operations are:

- Convert x kg of xi into x / ki kg of i (but x must be a multiple of ki, because the resulting kg must be integer). Or wait, no: the problem states that the transformation is possible as long as the resulting amount is an integer. So when converting from xi to i, you can use any amount of xi, as long as when you multiply by 1/ki, the result is an integer. So for example, if ki is 2, then you can use 2 kg of xi to get 1 kg of i. Similarly, converting i to xi would take 1 kg of i to get 1 kg of xi. So the transformation is possible in both directions, but with different conversion factors.

So the problem is to model the exchange between materials. The challenge is to determine if, given the initial supplies (b_i), we can redistribute the materials via these transformations such that for each material i, we have a_i or more.

The approach here is to model the dependencies between materials. Since each material i (except 1) is connected to xi, which is a material with a lower number (since for i >=2, xi <= i-1), the entire structure forms a tree. The root of the tree is material 1. So all materials are connected in a hierarchy where each node's parent is a material with a lower index.

The idea is to process each material starting from the leaves and moving up to the root. Because each material can only be converted with its parent, and the hierarchy is a tree, we can compute the required or excess materials in a bottom-up manner.

Let's think recursively. For each node i, after handling all its children, we can compute the net required or excess material. For example, if after considering all children of i, we have a deficit in i, we need to convert some of the parent's (xi) material into i. But each conversion from xi to i requires ki units of xi for each unit of i. Conversely, if we have an excess of i, we can convert it back into xi (each unit of i gives 1 unit of xi), which can help with deficits higher up the tree.

So the algorithm would be:

1. Start from the leaves (materials with no children) and work our way up to the root (material 1). For each material, after handling all its children, compute how much more (or less) of that material is needed.

2. For each material i, the initial available is b_i. The required is a_i. But when considering its children, any excess in a child j (which is a child of i) can be converted back to i. Similarly, any deficit in j must be supplied by converting i into j, which would require i's material multiplied by k_j.

Wait, let's formalize this. Let's process each node in reverse order (starting from the highest index, moving down to 1). For each node i:

- Compute the required amount a_i. But any children of i may have contributed to the available or required amount of i.

Wait, perhaps for each node, the total needed is a_i minus the contributions from converting to/from its children. Wait, no. Let's think of each node's available resources.

For example, suppose we have a node i with children j. Each child j can either contribute to i's available resources (if j has excess) or require more from i (if j has deficit).

So for each node j (child of i), after processing j, we can determine how much of j's required a_j is covered. If after using the available b_j, j has a deficit, that deficit must be covered by converting i's material into j, which would consume i's material at a rate of k_j per unit j. Conversely, if j has an excess (b_j - a_j is positive), that excess can be converted back into i's material (since 1 unit of j gives 1 unit of i).

Wait, this is the key insight. For each node j, after processing all its children (which are higher in the tree), we can compute the effective available and required for j. Then, the excess or deficit of j must be handled by its parent.

So here's the approach:

For each node i (starting from the highest, down to 1):

1. Calculate the net available for i: (b_i - a_i). If this is positive, it's an excess; if negative, a deficit.

But wait, no. The initial available is b_i, but we can also receive excess from children converted into i. But according to the tree structure, children are higher in the hierarchy. Wait, no. The parent of j is x_j, which is less than j. So the tree is built such that parents have lower indices than their children. So when processing in reverse order (from n down to 1), we process each node after all its children (since children have higher indices than their parents).

So for each node i (starting from the largest index, n, then n-1, etc.):

- We first process all of its children (if any). Wait, no. Since in the tree, the children are the nodes that have i as their parent. For example, if j is a child of i, then j's parent is i. So when i is being processed, all j that have x_j = i and j > i have already been processed (since j is higher than i, and we're processing in order from n down to 1). So when processing i, we can collect all the excess or deficits from its children (those j where x_j = i).

Wait, but how do we track which nodes are children of i? Since each node j (j >=2) has x_j as their parent, which is < j. So the children of i are all j where x_j = i. So to process each node i, we need to know all its children j. So we can build a tree structure where each node i has a list of children. Then, for each node i, after processing all children j, we can compute the net requirement for i.

So the steps would be:

1. Build a tree where each node i (from 2 to n) has a parent x_i. So for each i, we can store its children.

2. Process the nodes in reverse order (starting from n down to 1). For each node i, after processing all its children, compute how much extra or deficit is there.

3. For each child j of i:

   a. When processing j, any deficit in j must be covered by converting i's material into j. The deficit for j is (a_j - (b_j + converted from children)). Wait, perhaps not. Let's think again.

Wait, let's model each node j. The node j has a required a_j. The available is b_j plus any conversions from children (children can contribute to j via converting their excess into j, but according to the problem statement, j's children can be converted into j via their own conversion rules. Wait, no. The conversion between j and its parent is j can be converted to x_j (its parent) and vice versa. So the children of j (if any) would have their own conversion steps with their parents. Wait, no. The children of j are those nodes k where x_k = j. So each node's parent is in the tree. So the conversion for j's children is between the child and j. So when processing j's children (which are higher in the hierarchy), their excess or deficit would have been converted into j's material.

So for example, when processing node j (after all its children are processed), any excess in j's children (like k, which is a child of j) would have been converted into j's available, and any deficit in the children would require j to provide material.

So for node j, when processing it, we can take into account the surplus or deficit from its children. 

Wait, perhaps the processing order is such that for each node, after all its children have been processed, we can compute how much the children require from the parent, or how much they can contribute to the parent.

Let me think with an example. Suppose node j is a child of i (so x_j = i). When we process j (since we're processing from n down to 1), j's children (if any) have already been processed. So when processing j, we can calculate how much surplus or deficit j has after considering its children.

For j's initial available, it's b_j. Then, any children of j (nodes k where x_k = j) can contribute their excess to j (since converting 1 unit of k to j gives 1 unit of j). Or if a child k has a deficit, j must provide some of its own material to cover that deficit (each unit of deficit in k requires k's conversion rate (which is k's ki) units of j's material).

Wait, no. Because when converting j to k (since k's parent is j), converting j into k requires ki (which is the conversion rate of k) units of j to make 1 unit of k. Conversely, converting k into j gives 1 unit of j per 1 unit of k.

So for a child k of j:

If after processing k, k has a deficit (required a_k exceeds available b_k plus any conversions from its own children), then j must supply some of its own material to cover this deficit. For example, each unit of deficit in k requires j to spend (k's conversion rate) units of j's material.

If after processing k, k has a surplus (available exceeds required), then that surplus can be converted into j's material. Each unit of surplus in k gives 1 unit of j.

So when processing j, we need to account for all children of j. For each child k:

- Let surplus_k = available_k - a_k. If surplus_k >=0, then j can gain surplus_k units from k (since each unit of k's surplus can be converted to j's material).

- If surplus_k <0, then j must supply (k's conversion rate) * (-surplus_k) units to cover the deficit. 

So for j, the effective available is:

b_j (original) + sum over all children k of (surplus_k if surplus_k >=0 else 0) 

But then, j must subtract the deficit in each child k, which is (-surplus_k) * k_conversion_rate.

So after accounting for all children, the effective available for j is:

effective_available = b_j + sum (child_surplus) - sum (child_deficit * k_conversion_rate)

But the required a_j is fixed. So the net surplus for j is:

effective_available - a_j

If this is positive, then j can contribute the surplus to its parent (x_j). If it's negative, then j's parent (x_j) must supply some material to j, which would require x_j to spend (j's conversion rate) * deficit_j units.

So the plan is:

For each node j in reverse order (from n down to 1):

1. Compute the surplus or deficit from each child k of j.

   For each child k:

   - If the surplus_k (after processing k) is positive: add it to j's available.

   - If surplus_k is negative: subtract (deficit_k * k_conversion) from j's available.

2. Then, compute the effective available for j as (b_j + sum of child_surplus - sum (deficit_k * conversion_k)).

3. The required is a_j. So the surplus/deficit for j is effective_available - a_j.

4. If the surplus is negative (i.e., deficit), then j's parent (x_j) must supply (deficit_j) * conversion_j (j's conversion rate) units. So this deficit is passed up to the parent.

5. If the surplus is positive, then this can be added to the parent's available when processing x_j.

So the key is to process the nodes in reverse order, for each node calculate the effective surplus/deficit, and pass that up to the parent.

But wait, how do we track the conversion rates? For each node j (except root), when converting between j and x_j, the conversion from x_j to j requires k_j units of x_j per 1 j. But when converting j back to x_j, each j gives 1 x_j. So when j has a deficit, each deficit unit requires x_j to spend k_j units. When j has a surplus, each surplus unit gives x_j 1 unit.

So, during processing:

For each node j (starting from n down to 1):

- Collect all the surplus from children (k) that can contribute to j's available.

- Subtract the deficits from children (k) multiplied by their conversion rates.

- Then, compute j's effective available (b_j + sum of surplus from children - sum (deficit_k * k_conversion)).

- Compare this to a_j. If effective_available >= a_j: surplus is (effective_available - a_j). This surplus can be converted into x_j (j's parent) by adding 1 unit of x_j per surplus unit.

- If effective_available < a_j: deficit is (a_j - effective_available). This deficit must be covered by x_j, which requires x_j to provide (deficit_j) * j_conversion units.

So, the steps are:

Initialize for each node j:

   children = list of nodes where x_j is the parent.

   conversion_rate = k_j (the conversion rate from x_j to j)

Process from j = n downto 1:

   sum_surplus = 0

   sum_deficit = 0

   for each child in children[j]:

       child_surplus = processed_surplus_or_deficit_for_child

       if child_surplus >=0:

           sum_surplus += child_surplus

       else:

           sum_deficit += (-child_surplus) * child_conversion_rate

   effective_available = b[j] + sum_surplus - sum_deficit

   required = a[j]

   if effective_available >= required:

       surplus = effective_available - required

       pass this surplus to the parent (x_j) when processing x_j.

   else:

       deficit = required - effective_available

       pass this deficit multiplied by j's conversion rate to the parent.

But how do we track this? For each node j, after processing, we store whether it has a surplus or deficit. Then, when processing its parent x_j, we look at j's surplus or deficit and apply the conversions.

So, for each node j:

   after processing, store the surplus/deficit.

Then, when processing x_j, sum all the surpluses and deficits from its children (which are all nodes j where x_j is their parent).

So the algorithm can be:

1. Read n.

2. Read the array b, then a.

3. Read the next n-1 lines to get x_j and k_j for j=2 to n.

4. Build the tree structure: for each node j, store its parent x_j and conversion rate k_j. Also, for each parent, keep a list of children.

5. Process nodes in order from n down to 1.

6. For each node j:

   a. Compute the sum_surplus and sum_deficit from all its children.

   b. Compute effective_available = b[j-1] (since Python uses 0-based indices) + sum_surplus - sum_deficit.

   c. required = a[j-1]

   d. If effective_available < required: then the deficit is (required - effective_available). This deficit must be covered by the parent. So, the deficit is multiplied by j's conversion rate (k_j) and added to the parent's sum_deficit.

   e. Else, the surplus is (effective_available - required), which can be added to the parent's sum_surplus.

7. After processing all nodes, check the root (node 1). If after all processing, the root's effective_available (after considering children's contributions and deficits) is >= a[0], then output YES, else NO.

Wait, but node 1 (the root) doesn't have a parent. So after processing node 1, we have to check if the effective_available (after considering all children) is >= a[0], otherwise it's impossible.

So let's see:

For example, for node 1, when processing it:

sum_surplus is the sum of surpluses from its children (nodes j where x_j=1).

sum_deficit is the sum of (deficit_j * k_j) from children j where x_j=1.

effective_available = b[0] + sum_surplus - sum_deficit.

Then, required is a[0].

If effective_available >= a[0], then yes. Else, no.

So the algorithm is correct.

Now, how to implement this efficiently.

Constraints are n up to 1e5, so O(n) is acceptable.

We need to build a tree where each node's children are stored. For each node j (from 2 to n), we add j to the children list of x_j.

Processing in reverse order (from n down to 1). For each j in this order:

- Check if j is in the children list of any node. For each node's children, collect their surplus/deficit.

But since we process j after all its children (since j is processed in reverse order), each node's children are processed before the node itself.

So for each node j, when processing, all of its children (which have higher indices) have already been processed, so their surplus/deficit is known.

So during processing, for each node j:

   sum_surplus = sum of child_surplus for children of j where child_surplus >=0.

   sum_deficit = sum of (child_surplus * (-1) * k_child) for children of j where child_surplus <0.

Wait, no. Wait, for a child k of j, when processing k, the surplus is (effective_available_k - a_k). If this is >=0, then that's a surplus, which can be added to j's available (each unit of surplus k can be converted into 1 unit of j). If it's <0, then j has to supply (k's conversion rate) * deficit_k (deficit_k is a_k - effective_available_k).

Wait, for example, child k of j:

If after processing k, the surplus of k is s_k = effective_available_k - a_k.

If s_k >=0: then j can take s_k units from k (since each unit of k's surplus can be converted to j).

If s_k <0: then j must provide (k.conversion_rate) * ( -s_k ) units of j's material to cover k's deficit.

So for each child k of j:

sum_surplus += max(s_k, 0)

sum_deficit += max( -s_k, 0 ) * k.conversion_rate 

So, the sum_deficit is the sum of (deficit in k) multiplied by k's conversion rate.

Then, effective_available_j = b_j + sum_surplus - sum_deficit.

required_j = a_j.

If effective_available_j >= required_j: surplus is (effective_available_j - required_j). This can be passed to j's parent (x_j).

Else: deficit is (required_j - effective_available_j), which is multiplied by j's conversion rate and passed to j's parent.

So for each node j, we need to compute s_j (the surplus/deficit after processing its children), and then for j's parent, add to sum_surplus or sum_deficit accordingly.

But how do we store the s_j for each node?

We can use an array to track s_j for each node. Initially, all s_j are 0.

Wait, no. For each node j, after processing, s_j is computed as effective_available_j - a_j. So if s_j >=0, it's a surplus. Else, it's a deficit (which is passed as a positive value multiplied by conversion rate).

Wait, for j, after processing:

s_j = effective_available_j - a_j.

If s_j >=0: surplus, which can be added to x_j's sum_surplus.

If s_j <0: deficit, which is ( -s_j ) * k_j, which is added to x_j's sum_deficit.

So for each j, after processing, we compute s_j, then:

if j is not the root (x_j exists), then:

   if s_j >=0:

       add s_j to x_j's sum_surplus

   else:

       add ( -s_j ) * k_j to x_j's sum_deficit

Thus, during processing, for each j, we can compute s_j, and then if j is not root, update x_j's sum_surplus or sum_deficit.

But how to track sum_surplus and sum_deficit for each node? Because for a node j, the sum_surplus and sum_deficit are the sum of contributions from its children.

But perhaps, during processing, for each node j, we can:

- Iterate over all its children (which are stored in a list).

But wait, when we process j, the children of j have already been processed, so their s values are known.

So for each child k in children[j], we check if s_k >=0: add to sum_surplus, else add ( -s_k ) * k's conversion rate to sum_deficit.

But how do we get the conversion rate for k?

Each child k has its own conversion rate, which is the k_j that was given when the node was created.

Wait, each node j (except 1) has x_j and k_j. So when building the tree, for each node j >=2, we can store x_j and k_j.

So, for the processing:

Initialize an array s of size n, where s[i] represents the surplus/deficit for node i+1 (since Python uses 0-based indices).

Wait, perhaps nodes are 1-based. So, for j from 1 to n:

children[j] is a list of nodes that have x_j as their parent.

For j from 1 to n, we can track x_j (for j >=2) and k_j.

So in code:

children is a list of lists. children[x] contains all nodes j where x is the parent of j.

Then, processing from j = n down to 1:

sum_surplus = 0

sum_deficit = 0

for child in children[j]:

    if s[child-1] >=0:

        sum_surplus += s[child-1]

    else:

        sum_deficit += (-s[child-1]) * (k_j of the child)

Then, effective_available = b[j-1] + sum_surplus - sum_deficit

required = a[j-1]

s_j = effective_available - required

But wait, the k_j for the child is the conversion rate from the parent (x_j) to j. So for child k, which is part of children[j], the parent of k is j, and k's conversion rate is k_k (the k given when k was read).

Wait, yes. Because for each child k in children[j], x_k = j, and their conversion rate is k_k (as per the input).

So for example, for k (the child), when we need to compute the deficit, it's (deficit) * k's conversion rate (k_k).

Thus, when building the tree:

Each node j >=2 has x_j and k_j. So when processing j's children (k), each child has their own k_k.

So during processing j, for each child k in children[j], when s_k is negative (deficit), we need to multiply by k_k (the conversion rate for k), which is the conversion from x_k (which is j) to k. Because converting j's material to k requires k's conversion rate (k_k) per unit.

So, for each child k in children[j], we have:

k's x is j, and k's k is k_k.

So, for the code, we need to store for each node j (>=2), x_j (its parent) and k_j (the conversion rate).

Thus, in code:

We can create two arrays, x and k, where x[j] is the parent of j+1 (since for j from 0 to n-2, each corresponds to node 2 to n). Wait, perhaps it's easier to have 1-based indices. Let's adjust.

Wait, for node j (1-based), for j from 2 to n, we have x_j and k_j. So for j in 1-based:

children is a list of lists. children[parent] contains all j where x_j = parent.

x and k are arrays of size n+1 (indexes 1..n). For j=1, x_j is undefined. For j=2..n, x_j is the parent (<=j-1), and k_j is the conversion rate.

So in code:

n = int(input())

b = list(map(int, input().split())) # 0-based, corresponds to 1-based nodes.

a = list(map(int, input().split()))

children = [[] for _ in range(n+1)] # 1-based

x = [0]*(n+1) # x[j] for j from 2 to n is parent.

k = [0]*(n+1) # k[j] for j from 2 to n.

for j in range(2, n+1):

    x_j, k_j = map(int, input().split())

    x[j] = x_j

    k[j] = k_j

    children[x_j].append(j)

Then, process each node from j =n down to 1.

We need an array s where s[j] represents the surplus/deficit after processing node j.

s = [0]*(n+1) # 1-based.

for j in range(n, 0, -1):

    sum_surplus = 0

    sum_deficit = 0

    # for each child of j:

    for child in children[j]:

        child_s = s[child]

        if child_s >=0:

            sum_surplus += child_s

        else:

            sum_deficit += (-child_s) * k[child] # k[child] is the conversion rate for the child.

    effective_available = b[j-1] + sum_surplus - sum_deficit

    required = a[j-1]

    s_j = effective_available - required

    s[j] = s_j

# After processing all nodes, check node 1's s[1]

if s[1] >=0:

    print("YES")

else:

    print("NO")

Wait, but this code has a problem: for node 1, after processing, its effective_available is b[0] + sum_surplus - sum_deficit. Then, the required is a[0]. So if s[1] = effective_available - a[0] >=0, then yes.

Yes. So the code seems correct.

But let's test it against the examples.

First example:

Input:

3

1 2 3

3 2 1

1 1

1 1

So nodes 2 and 3.

For node 2: x is 1, k is 1.

For node3: x is 1, k is 1.

children[1] = [2,3]

Processing nodes 3, 2, 1.

Processing node3:

children[3] is empty. So sum_surplus and sum_deficit are 0.

effective_available = b[3-1] = 3. required is a[3-1] =1.

s[3] =3-1=2 (surplus).

Processing node2:

children[2] is empty.

effective_available =2. required a[1] is 2. s[2] =0.

Processing node1:

children are 2 and3.

sum_surplus = s[2] (0) + s[3] (2) =2.

sum_deficit is 0.

effective_available =1 (b[0]) +2 -0 =3. required a[0]=3. s[1] =0 >=0. So YES.

Which matches the first example.

Second example:

Input:

3

3 2 1

1 2 3

1 1

1 2

So nodes 2 and3.

node2: x=1, k=1.

node3: x=1, k=2.

children[1] = [2,3].

Processing node3:

children empty. effective_available =1. required 3. s[3] =1-3 =-2.

Processing node2:

children empty. effective_available =2. required 2. s=0.

Processing node1:

sum_surplus: from 2 (0) and 3's s is -2. So for child3, since s is -2, sum_deficit += (- (-2)) *k[3]. k[3] is 2. So sum_deficit += 2*2=4.

sum_surplus is 0 (from node2).

effective_available =3 (b[0]) +0 -4= -1. required a[0] is1. s[1] =-1 -1? Wait no. Wait, required a[0] is 1. So effective_available is -1. So s[1] = (-1) -1 =-2?

Wait no. Wait, for node1:

effective_available =3 (b[0]) + sum_surplus (0) - sum_deficit (4) =3-4= -1.

required a[0] is1.

s[1] = -1 -1 = -2. So less than zero. Output NO.

Which matches the example.

So the code works for the sample inputs.

Now, considering the constraints. n up to 1e5. The code is O(n) because each node is processed once, and each child is processed once in the loop. The sum over all children is O(n) in total.

The data structures are manageable. For the children list, since each node (except root) has exactly one parent, the total number of children is n-1, so the children list has O(n) elements.

Now, for handling very large numbers (up to 1e12), but in Python, integers can handle that.

The only thing to watch out for is that when sum_deficit becomes a very large negative, but the code handles that correctly.

But when sum_surplus is added and sum_deficit subtracted, if the sum_surplus is not enough to cover sum_deficit, the effective_available could be negative, leading to a deficit in the node.

But in the code, that's handled properly.

So the code should work.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))
    
    # Initialize children, x, k arrays (1-based)
    children = [[] for _ in range(n + 1)]
    x = [0] * (n + 1)
    k = [0] * (n + 1)
    
    for j in range(2, n + 1):
        xj, kj = map(int, sys.stdin.readline().split())
        x[j] = xj
        k[j] = kj
        children[xj].append(j)
    
    s = [0] * (n + 1)  # s[j] is the surplus/deficit for node j
    
    # Process nodes in reverse order
    for j in range(n, 0, -1):
        sum_surplus = 0
        sum_deficit = 0
        
        for child in children[j]:
            cs = s[child]
            if cs >= 0:
                sum_surplus += cs
            else:
                sum_deficit += (-cs) * k[child]
        
        effective = b[j-1] + sum_surplus - sum_deficit
        required = a[j-1]
        s[j] = effective - required
    
    print("YES" if s[1] >= 0 else "NO")

if __name__ == "__main__":
    main()
```