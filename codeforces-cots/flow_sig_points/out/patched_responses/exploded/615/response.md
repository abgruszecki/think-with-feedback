<think>
Okay, let's tackle this problem. So, the task is to count the number of beautiful trees. A tree is beautiful if the distance between vertices a and b is exactly m. And each edge in the tree must have a weight between 1 and m, inclusive. Oh right, the trees are considered different if any edge's presence or weight is different. So the structure of the tree (the actual edges) and their weights both matter.

Hmm. Let's think about the constraints. The maximum n and m are up to 1e6, so any O(n) or O(m) algorithm might be acceptable, but anything higher like O(n^2) is definitely out. So we need an approach that's linear or logarithmic in terms of these variables.

First, I need to model the problem. The key is to find the number of trees where the path from a to b has sum exactly m, with each edge on that path contributing a weight between 1 and m. The other edges can have any weight between 1 and m, but their structure also depends on the tree.

Wait, but the structure of the tree matters. So first, we need to model all possible trees where a and b are connected in a way that their path sum is exactly m. But how?

Let me break this down. The problem can be split into two parts:

1. The structure of the tree (the edges) must form a tree where a and b are connected. But in any tree, there's exactly one path between any two nodes, so the path between a and b is unique. For the distance to be m, the sum of the weights along that path must equal m.

2. For the remaining edges (those not on the a-b path), their weights can be any value between 1 and m. But how do these edges contribute to the total count?

So the approach could be:

- Find all possible ways to choose the path between a and b such that the sum of their edges is exactly m. Then, multiply this by the number of possible ways to choose the remaining edges (structure and weights) such that the overall structure is a tree.

Wait, but the structure of the tree depends on the path between a and b. For example, if the path has k edges, then the rest of the tree must form a structure that connects all the other nodes without creating cycles.

Alternatively, perhaps the number of trees with a given path between a and b can be determined combinatorially. Let's think about the steps:

1. The path between a and b must consist of some edges. Let's call the edges on this path the 'main path'. The sum of their weights must be exactly m.

2. The rest of the tree must form a structure where all other nodes are connected to this main path through some edges. But since it's a tree, once the main path is fixed (the edges and their structure), the other edges can be arranged in a way that connects the remaining nodes as a forest attached to the main path.

Wait, perhaps we can model this as follows:

The main path between a and b is a simple path (since it's a tree, there's exactly one path). Let the length of this path (number of edges) be k. The sum of the weights of these k edges is m. The remaining (n - 1 - k) edges form a structure that connects the other nodes. Each of these edges can be placed anywhere else in the tree, as long as the overall structure remains a tree.

But how to count the possible structures and their weights for the remaining edges?

This seems complicated. Let's think of the problem in terms of combinatorics. The total number of trees where the a-b path has sum exactly m can be expressed as:

number_of_possible_main_paths * number_of_ways_to_choose_remaining_edges * product_of_possible_weights_for_remaining_edges

But how to model each part?

First, the main path. The main path between a and b must consist of some edges. But the structure of this path (the edges) depends on the tree. Wait, but the tree can have varying structures. For example, the path between a and b could be a direct edge (if they are connected by one edge), or it could go through other nodes (if the tree is structured such that a and b are further apart).

So perhaps the main path's length (number of edges) can vary from 1 to (n-1), but how? For example, in a tree, the maximum possible path length between two nodes is (n-1) edges, but that's only if the tree is a straight line from a to b, passing through all other nodes.

Wait, but in any tree, the path between a and b has a length of (distance in terms of edges) equal to the number of edges in their unique path. So, the first step is to consider all possible possible path lengths (k) for the a-b path. For each possible k, the sum of the weights of the edges in this path must be exactly m, and each edge weight is at least 1. Then, for each such k, we need to count the number of ways to arrange the tree structure (edges) such that the a-b path has exactly k edges, and then multiply by the number of possible weight combinations for those k edges (summing to m) and the number of possible ways to arrange the rest of the tree (with their own edge weights).

Hmm, this seems like a possible approach. So the problem splits into:

For each possible k (number of edges in the a-b path), compute:

- The number of possible weight assignments for the k edges that sum to m. This is equivalent to the number of compositions of m into k parts where each part is ≥1. Which is C(m-1, k-1). But wait, since each edge must have weight ≥1, the sum is m. So yes, for k edges, it's (m-1 choose k-1) ways.

Then, for each k, compute:

- The number of possible tree structures where the a-b path has exactly k edges. Let's call this S(k).

- Multiply by (m^{n-1 -k}) ), since the remaining edges (n-1 -k edges) can have any weight from 1 to m. For each such edge, there's m choices.

So the total for each k is S(k) * C(m-1, k-1) * m^{n-1 -k}.

The sum over all possible k gives the total number of beautiful trees.

So the problem reduces to:

Compute the sum over k=1 to k_max of (S(k) * C(m-1, k-1) * m^{n-1 -k}) ), modulo 1e9+7.

But what is S(k)? S(k) is the number of trees with n nodes where the path between a and b has exactly k edges.

Wait, but how to compute S(k)?

Hmm. Let's think. The path between a and b has k edges. So the path is a sequence of k edges connecting a sequence of (k+1) nodes. For example, if k=2, the path is a -> x -> b. The other nodes must be connected to this path in such a way that the entire structure is a tree.

But how to model S(k)?

An alternative approach is to model the problem using Prüfer sequences. But I'm not sure.

Alternatively, think of the tree as consisting of a path between a and b with exactly k edges, and the remaining nodes are attached to this path in some way. So the problem of counting S(k) is equivalent to the number of trees where the path between a and b has exactly k edges.

Alternatively, perhaps S(k) is equal to the number of ways to choose a path of length k edges between a and b and form a tree around it.

Wait, here's another approach. For the path between a and b to have exactly k edges, the number of such trees can be found by considering the path as a chain of k+1 nodes (a, v_1, v_2, ..., v_{k-1}, b). The remaining (n - (k+1)) nodes must be attached to the nodes in this chain. Each such node can be attached to any of the nodes in the chain, but in such a way that the overall structure is a tree. However, the chain itself can have any arrangement of nodes as long as the path between a and b is exactly k edges.

Wait, but the chain can have other nodes branching off. For example, the path a - x - y - b has k=3 edges. The nodes x and y are part of the path. The other nodes can be attached to a, x, y, or b.

So the problem is similar to forming a tree where the a-b path is fixed to have k edges. The number of such trees is the number of ways to form a tree with n nodes such that the a-b path has exactly k edges.

But how to compute this?

Hmm. Let's think combinatorially. Let’s imagine that the path between a and b has k edges. This forms a chain of length k+1 nodes. The remaining n - (k+1) nodes must be attached to this chain in some way. Each of these nodes can be attached to any node in the chain. Moreover, the chain itself can be any possible path between a and b of k edges. Wait, but the nodes in the chain can include other nodes not in the path. No, because the path between a and b is the unique path in the tree, so any node in the chain is part of that path.

Wait, perhaps this is a classic combinatorial problem. Let me think.

The number of trees where the a-b path has exactly k edges is equal to (k-1) * (n)^(n -k - 2) * C(n-2, k-1) )? Hmm, not sure. Alternatively, perhaps there's a formula here.

Alternatively, perhaps the number S(k) can be computed using the following approach:

The a-b path has k edges, so there are k+1 nodes on the path. Let's call these nodes v_0 = a, v_1, v_2, ..., v_{k} = b. The remaining n - (k+1) nodes are to be connected as subtrees to any of the nodes in this path. Each of these remaining nodes must be connected to exactly one node in the path, but in such a way that the entire structure is a tree.

Wait, but in that case, the structure is determined by:

- The choice of the path (i.e., the order of nodes between a and b, but that's fixed once the path is considered as a chain of nodes between a and b), and

- The way the remaining nodes are attached to the nodes in the path.

But how many ways are there to arrange the remaining nodes?

Alternatively, perhaps the number of such trees is (k+1)^(n -k -1) * C(n-2, k-1). Wait, not sure. Let me think of the problem in terms of choosing the nodes along the path.

Wait, the path between a and b has exactly k edges, so there are k+1 nodes. The nodes along the path must form a chain. The remaining n - (k+1) nodes can each be connected to any of the nodes in the chain, except that the path between a and b must remain the same. So each of the remaining nodes can be connected to any of the nodes in the chain. The number of ways to attach these nodes is similar to forming a rooted forest where each root is a node in the chain, and the total number of nodes is n - (k+1).

The number of such trees is (k+1)^(n -k -1) * (number of ways to choose the path's structure).

Wait, but the path's structure is fixed once we know the sequence of nodes. But how to count the number of possible paths of k edges between a and b.

Wait, the path is a sequence of nodes starting at a and ending at b, with exactly k edges. The number of such paths in a tree is 1, because in a tree, there's exactly one path between any two nodes. Wait, no. Wait, S(k) counts the number of trees where the a-b path is exactly k edges. So S(k) is the number of possible tree structures where the a and b are connected via a path of k edges.

Ah, perhaps S(k) is equal to the number of possible trees on n nodes where the distance between a and b is k edges. And this is a known value.

But how to compute this.

Let me think of the problem in terms of generating all possible trees where a and b are at distance k edges. How can this be counted?

Alternative approach: The number of such trees is equal to the number of ways to arrange the tree such that the path between a and b is exactly k edges, and the rest of the tree is built around this path.

The path between a and b has k edges. The nodes along this path are a, v_1, v_2, ..., v_{k-1}, b. Then, the remaining n - (k+1) nodes can be connected to any of the nodes in this path. The way to count this is similar to the problem of counting the number of trees where a certain subset forms a chain of length k+1.

Alternatively, perhaps we can model this as follows: the path between a and b must have k edges, and the remaining nodes can be connected to any node in the path. Each of the remaining n -k-1 nodes can choose their parent in the path or any of the existing nodes. Wait, but the tree must be connected.

Alternatively, think of the path as the backbone. The rest of the nodes can be attached to this backbone in any way, as long as the backbone remains the unique path between a and b. The number of ways to do this is (k+1)^(n -k -1) * (number of ways to choose the backbone's structure).

Wait, but how to choose the backbone's structure? Because the backbone is a path of k edges between a and b. The number of such paths is not straightforward. Because the nodes along the path can include other nodes besides a and b, but how?

Alternatively, perhaps the backbone is a path of k edges between a and b. The number of possible such backbones (i.e., the number of possible sequences of nodes forming a path of length k between a and b) is equal to the number of ways to choose the intermediate nodes. Wait, but the other nodes in the backbone must be new nodes. For example, if k=2, the path is a -> x -> b, where x is some other node. So the backbone includes a, x, b. The remaining nodes can be connected to a, x, or b. But how many ways are there to choose the backbone's intermediate nodes when k is given?

Wait, this approach seems complicated. Let's think differently.

Suppose that in the tree, the path between a and b has exactly k edges. Then, the structure of the tree can be considered as a path of k edges between a and b, with the rest of the nodes attached to this path. Each of the remaining (n -k-1) nodes can be attached to any of the nodes in the path, but the path must remain the unique path between a and b.

Wait, but the problem is that the path between a and b in the tree is the only path, so any subtree attached to the path can't connect to other nodes in the path, except through their parent. So the number of ways to attach the remaining nodes is (k+1) choices for each node (as they can be attached to any node along the path). However, the order in which they are attached doesn't matter, as each node can choose a parent from the path.

Wait, perhaps the number of ways to attach the remaining nodes is (k+1) raised to (n -k-1), because each of the (n -k-1) nodes can be attached to any of the (k+1) nodes in the path. But that would be (k+1)^(n -k-1) possibilities for the structure of the tree. But then, the backbone (the path between a and b) must have exactly k edges, and the way to arrange the backbone's nodes is another factor.

Wait, but the backbone's nodes are part of the path. Let's think: the path between a and b has k edges, which implies that there are k+1 nodes in the path. The first is a, the last is b, and the rest are k-1 internal nodes. But the intermediate nodes can be any of the other nodes in the tree. However, since the total number of nodes is n, and the path has k+1 nodes, the remaining nodes are (n - (k+1)), which can be attached to the path.

So the problem becomes: how many trees are there where the path between a and b has exactly k edges, and the rest of the nodes are connected to this path.

The number of such trees is:

(number of ways to choose the intermediate nodes in the path) × (number of ways to arrange the remaining nodes as children of the path's nodes) × (number of ways to arrange the edges of the path).

Wait, but the path between a and b is a sequence of nodes a → v1 → v2 → ... → v_{k-1} → b. The v1, v2, ..., v_{k-1} must be distinct nodes not including a and b. But wait, no, because the path can't have cycles, and since it's a tree, the nodes must be distinct. So the intermediate nodes (v1, ..., v_{k-1}) must be distinct and not equal to a or b. So the number of such nodes in the path is k-1. But the total number of nodes in the path is k+1 (including a and b). So, we need to choose k-1 distinct nodes from the remaining (n-2) nodes (since a and b are fixed). Once those are chosen, the path is determined (since the order is a → v1 → v2 → ... → v_{k-1} → b). Then, the remaining (n -k -1) nodes can each be attached to any of the (k+1) nodes in the path.

Wait, but the remaining nodes are n - (k+1) = (n -k -1) nodes. Each of these can be attached to any of the (k+1) nodes in the path, forming a tree. The number of ways to attach these nodes is (k+1) raised to (n -k -1). Because each node can choose any of the (k+1) parents.

So putting this together:

The number of trees where the a-b path has exactly k edges is:

C(n-2, k-1) × (k-1)! × (k+1)^(n -k -1)

Wait, wait. Let's break it down:

1. Choose the k-1 intermediate nodes from the remaining (n-2) nodes (since a and b are fixed). So C(n-2, k-1) ways.

2. Arrange these k-1 nodes in a sequence between a and b. The order of the intermediate nodes matters because the path must be a sequence of edges a → v1, v1 → v2, ..., v_{k-1} → b. So the number of permutations is (k-1)!.

3. The remaining (n -k -1) nodes each can be attached to any of the (k+1) nodes (a, v1, v2, ..., v_{k-1}, b). Each such node has (k+1) choices. So (k+1)^(n -k -1) ways.

So multiplying these factors gives the number of trees for a particular k.

But wait, the problem is that this approach assumes that the path's intermediate nodes are arranged in a particular order, which may not account for all possibilities. For example, if the path is a → v1 → v2 → b, and then another path a → v2 → v1 → b, but those are considered different paths even though the sum of edges would be the same. However, in the tree structure, the actual edges are different, so this is correct.

So combining these factors:

S(k) = C(n-2, k-1) * (k-1)! * (k+1)^(n -k -1)

Wait, but (k-1)! is the number of permutations of the k-1 intermediate nodes. So yes.

But wait, what if k=1? Then the intermediate nodes are 0, so we choose 0 nodes from n-2 (which is possible only if n-2 >=0, which it is when k=1 implies n >=2). Then the formula becomes C(n-2, 0) * 0! * (2)^(n-2). Which is 1 * 1 * 2^{n-2} = 2^{n-2}.

For example, in the second sample input:

n=3, m=1, a=1, b=2. So the path between a and b must be 1 edge (since k must be 1, because m=1 and sum is 1). So S(k=1) = C(1,0) * 0! * 2^(3-1-1) = 1 * 1 * 2^1 = 2. Which matches the sample output of 2. Then the number of ways for the path is C(m-1,0) (since k=1) which is 1. So the total is 2 * 1 * 1^{3-1-1} (since m=1, so m^{n-1 -k} =1^(3-1-1) =1^1=1). So 2*1*1=2, which matches the sample.

So this formula seems correct for the sample.

So S(k) = C(n-2, k-1) * (k-1)! * (k+1)^(n-k-1).

But let's simplify this.

C(n-2, k-1) * (k-1)! is equal to (n-2)! / ( (n-2 - (k-1))! (k-1)! )) ) * (k-1)! ) ) = (n-2)! / ( (n -k -1)! ) )

So S(k) = (n-2)! / (n -k -1)! ) ) * (k+1)^(n -k-1)

But how to compute this for large n up to 1e6?

This might be challenging. Let's see.

But the problem requires us to compute the sum over k from 1 to (n-1) (since the maximum possible path length between a and b is n-1 edges, when the tree is a chain). However, when k is such that m-1 choose k-1 is zero (like when m-1 <k-1, which makes the combination zero), those terms can be skipped.

So the steps for solving the problem would be:

1. Precompute factorials up to max(n, m) + some buffer, modulo 1e9+7.

2. Precompute inverse factorials for the same range.

3. Precompute powers of m for exponents up to (n-1 -k) for varying k. But perhaps we can compute m^exponent on the fly, using precomputed exponents.

But for n up to 1e6, and m up to 1e6, and k varying from 1 to min(m, n-1), the exponents can be up to (n-1 -1) =n-2.

But for each k, the term is:

term = ( (n-2)! / ( (n -k -1)! )) ) * (k+1)^(n-k-1) * C(m-1, k-1) * m^{n-1 -k} )

mod 1e9+7.

But let's combine terms:

term = ( (n-2)! / ( (n -k -1)! )) ) * (k+1)^(n-k-1) * C(m-1, k-1) * m^{n-1 -k} )

Which can be written as:

term = ( (n-2)! / ( (n -k -1)! )) ) * ( (k+1) * m )^{n-k-1} * C(m-1, k-1) )

Because (k+1)^(n-k-1) * m^{n-1 -k} = m^{n-1 -k} * (k+1)^{n-k-1} } = (m (k+1) )^{n-k-1} * m^{- (n-k-1) - (n-1 -k)}? Wait, no. Wait, (k+1)^(n-k-1) * m^{n-1 -k} = m^{n-1 -k} * (k+1)^{n-k-1} } = (k+1 * m )^{n-k-1} }? No, because the exponents are the same. Wait, (n-k-1) is the exponent for (k+1) and (n-1 -k) is the exponent for m. But (n-1 -k) = (n-k-1). So exponents are equal.

So (k+1) * m raised to (n-k-1) is equal to (k+1)^(n-k-1) * m^{n-k-1}.

But in our case, we have (k+1)^(n-k-1) multiplied by m^{n-1 -k} which is m^{(n-1 -k)} = m^{(n-k-1)}. So yes, so (k+1 * m) raised to the power (n-k-1).

So term can be written as:

term = ( (n-2)! / ( (n -k -1)! )) ) * ( (k+1)*m )^{n-k-1} * C(m-1, k-1) )

This simplifies the calculation.

So the problem now reduces to:

For each valid k (from 1 to min(m, n-1)), compute the term as above, sum all terms modulo 1e9+7.

But how to compute this efficiently.

Let's outline the steps:

1. Precompute factorial up to (n-2) and inverse factorial up to (n-2), modulo MOD=1e9+7. But since n can be up to 1e6, this is manageable.

2. Precompute the combination C(m-1, k-1) for all possible k. However, for k-1 to be <= m-1, which implies k <= m. Also, since k can be up to n-1 (as the path between a and b can't have more than n-1 edges), the valid k is from 1 to min(m, n-1). For k > m, C(m-1, k-1) is zero, so those terms can be skipped.

3. For each k in 1..min(m, n-1):

   a. Compute comb = C(m-1, k-1).

   b. Compute the term factorial(n-2) * inv_fact(n -k -1) mod MOD. Because (n-2)! / ( (n-k-1)! ) is equal to fact[n-2] * inv_fact[n-k-1] mod MOD.

   c. Compute pow((k+1)*m, n-k-1, MOD). This is the (k+1)*m term raised to the exponent (n-k-1).

   d. Multiply all these factors (comb, term, pow_val) together and add to the sum.

So the steps are manageable.

Now, the key is to precompute fact and inv_fact arrays.

But let's think about possible edge cases.

For example, when k = n-1. Then the path between a and b has n-1 edges, which is possible only if the entire tree is a straight line from a to b, passing through all other nodes. So the term would have (n -k -1) = n - (n-1) -1 = 0, so the (k+1)*m term raised to 0 is 1. The factorial term would be (n-2)! / ( (n - (n-1) -1) ! ) = (n-2)! / (0! ) = (n-2)!.

But when k =n-1, this requires that the path has n-1 edges. The combination C(m-1, k-1) is C(m-1, n-2). So this term is valid only if m-1 >=n-2, i.e., m >=n-1.

If m <n-1, then for k >=m+1, the combination is zero.

So in code, the loop over k should run from 1 to min(m, n-1), because for k >m, C(m-1, k-1) is zero.

So the code will need to:

- Precompute fact and inv_fact up to max(n-2, m-1).

Wait, fact needs to be up to (n-2) because the factorial term is (n-2)!.

But when m-1 is larger than (n-2), then to compute C(m-1, k-1) for k-1 up to (m-1), but when k is up to min(m, n-1), then k-1 can be up to min(m-1, n-2). So for example, if n-1 <=m, then k can be up to n-1, so k-1 up to (n-2). So the combinations C(m-1, n-2) would require m-1 >=n-2. Otherwise, it's zero.

But how to compute combinations where m can be up to 1e6 and n up to 1e6.

Hmm. Let's think. The combination C(m-1, k-1) is (m-1 choose k-1). So for each k in the loop, we need to compute this combination.

But when m is up to 1e6 and k up to 1e6, precomputing all combinations is not feasible. So we need a way to compute C(m-1, k-1) on the fly.

The combination C(a, b) can be computed as (fact[a] * inv_fact[b] * inv_fact[a -b]) mod MOD, when a >=b >=0. Otherwise, it's zero.

So for each k in 1..min(m, n-1), compute a = m-1, b =k-1. If a >=b, then C(a, b) is (fact[a] * inv_fact[b] * inv_fact[a -b]) mod MOD. Else, zero.

So the code can compute this for each k.

So the steps in code are:

1. Precompute fact and inv_fact arrays up to max(n-2, m-1).

   For example, max_fact = max(n-2, m-1).

   If n-2 is 0 (n=2), and m-1 is up to 1e6-1, then max_fact is up to 1e6-1.

   So precompute fact and inv_fact up to max_fact.

2. Precompute (k+1)*m modulo MOD for all k up to min(m, n-1).

   Wait, but for each k, we need to compute pow( ( (k+1)*m ), (n-k-1), MOD ). For exponents up to 1e6 (since n can be up to 1e6, and n-k-1 can be up to 1e6-1 -1).

   But exponentiating for each k is O(log exponent) time. For each k, exponent is (n-k-1) which can be up to 1e6. But log2(1e6) is about 20, so for each k, 20 operations. For k up to 1e6, this would be 20e6 operations, which is acceptable.

   So for each k in the loop:

   a. Check if k-1 <= m-1. If not, comb is zero.

   b. Else, compute comb as C(m-1, k-1) = fact[m-1] * inv_fact[k-1] * inv_fact[ (m-1)-(k-1) ] mod MOD.

   c. Compute term1 = fact[n-2] * inv_fact[ n -k -1 ] mod MOD. But when n-k-1 is negative, which can happen when k >=n. But since k is up to min(m, n-1), n-k-1 is >= 0 (since k <=n-1 → n-k-1 >=0).

   d. Compute exponent = n -k -1.

   e. Compute base = ( (k+1) * m ) mod MOD.

   f. Compute pow_val = pow(base, exponent, MOD).

   g. Multiply comb * term1 * pow_val mod MOD, and add to the sum.

So the code needs to handle these steps.

Now, let's think about the precomputation of fact and inv_fact.

In Python, for n up to 1e6, this is manageable. We can compute fact up to 1e6+.

But when n is up to 1e6, m is up to 1e6, the maximum required fact is max(n-2, m-1). For example, when n is 1e6, m is 1e6, then max_fact is max(1e6-2, 1e6-1) = 1e6-1. So precomputing up to 1e6 is sufficient.

So, steps in code:

Read n, m, a, b.

Compute MOD = 1e9+7.

max_fact = max(n-2, m-1)

if max_fact <0: (e.g., when n=2 and m=1, then n-2=0 and m-1=0 → max_fact=0)

precompute fact and inv_fact arrays up to max_fact.

But for cases where max_fact is zero, but n is 2 and m is 1:

fact[0] = 1, inv_fact[0] =1.

Then, for each k in 1..min(m, n-1):

If m=1, min(m, n-1) is 1 (since n is at least 2, n-1 is at least 1).

So k=1.

Check if k-1 <= m-1 → 0 <=0 → yes.

So comb = C(0, 0) =1.

term1 = fact[n-2] * inv_fact[n -k -1] → fact[0] * inv_fact[2-1-1] = 1 * inv_fact[0] →1*1=1.

exponent = 2-1-1 =0 → pow_val = 1.

Multiply all terms: 1 *1 *1 =1.

But sum would be 1, but according to the sample input 2, when m=1, the answer is 2. Wait, sample input 2 is n=3, m=1, a=1, b=2. Then:

Wait in that case, the code would compute:

k can be up to min(1, 3-1)=1.

k=1.

term1: n-2 =1, fact[1] (if precomputed up to max_fact=1). Wait, n=3, so n-2=1. So fact[1] is 1! =1.

inv_fact[n-k-1] = inv_fact[3-1-1=1-1=0? 3-1-1 =1 → inv_fact[1-1=0? Wait, 3-1-1 =1. So n-k-1 =3-1-1=1. So inv_fact[1] ?

Wait, no. Let me recalculate:

n=3, k=1.

term1 is (3-2)! / (3-1-1)! ) = 1! / (1)! = 1.

pow_val is (1+1)*1=2 → exponent is 3-1-1=1 → 2^1=2.

So term is 1 (comb) * 1 (term1) * 2 (pow_val) → 2. Then multiply by m^{n-1 -k} → m is 1, n-1-k=3-1-1=1 → 1^1=1. Wait, but earlier steps indicated that pow_val is (k+1)*m to the exponent (n-k-1). So in this case, (1+1)*1=2, exponent 1 →2^1=2.

Wait, but in the code steps, the pow_val is ((k+1)*m) raised to (n-k-1) → which in this case is 2^1=2.

So term is 1 (comb) * term1 (1) * 2 → 2. So sum is 2, which matches the sample input 2.

But according to the code steps, the formula would be:

term = comb * term1 * pow_val.

But in this case, comb is C(m-1, k-1) → m=1, k=1 → C(0,0)=1.

term1 is (3-2)! / (3-1-1)! → 1! /1! =1.

pow_val is (1+1)*1=2, exponent 1 →2^1=2.

So term is 1 *1 *2 =2. Then sum is 2. Which matches the sample.

So the code steps are correct.

But in the previous thinking, when k=1, the pow_val is (k+1)*m raised to (n-k-1). Which is (2*1)^1=2. So the code steps are correct.

Now, the code must compute all these terms correctly.

So the code outline:

Read n, m, a, b.

MOD = 1e9+7.

Compute max_fact = max(n-2, m-1)

precompute fact and inv_fact up to max_fact.

sum_result =0

for k in 1..min(m, n-1):

   if (k-1) > (m-1):

       continue

   comb = C(m-1, k-1) → compute using fact and inv_fact.

   term1 = fact[n-2] * inv_fact[ n-k-1 ] % MOD

   exponent = n -k -1

   base = ( (k+1) * m ) % MOD

   pow_val = pow(base, exponent, MOD)

   total = comb * term1 % MOD

   total = total * pow_val % MOD

   sum_result = (sum_result + total) % MOD

sum_result is the answer.

But wait, what about when n is 2, k is 1:

term1 is fact[0] * inv_fact[2-1-1] → fact[0] is 1, 2-1-1=0 → inv_fact[0]=1. So term1=1.

exponent is 0 → pow_val=1.

comb is C(m-1, 0) =1 if m>=1.

So in this case, for m=2, the term is 1*1* ( (1+1)*2 )^0 → 1*1*1 =1. Then multiplied by comb C(1,0)=1. So term is 1*1*1=1. Sum is 1. But for n=2, a and b are connected by one edge. The sum of that edge's weight must be m. The other edges (there are none, since n-1=1 edge). So the count is C(m-1, 0) * (2 *1)^0 →1 *1 =1 multiplied by S(k=1).

Wait, for n=2, S(k=1) is:

C(n-2, 0) * 0! * (k+1)^(n-k-1) → C(0,0)*1 * (2)^(0) →1*1*1=1. So term is 1 * C(m-1, 0) * m^{0} →1*1*1=1.

So the code would return 1. But when m=2, the edge must have weight 2. So the number of trees is 1. Which is correct.

So the code steps seem correct.

Now, let's think about the precomputation of fact and inv_fact.

In Python, for max_fact up to 1e6, precomputing fact and inv_fact is feasible.

The code:

Compute fact = [1]*(max_fact +1)

for i in 2..max_fact:

   fact[i] = fact[i-1] *i % MOD.

Then compute inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)

for i in max_fact-1 downto 0:

   inv_fact[i] = inv_fact[i+1] * (i+1) % MOD.

But what if max_fact is 0? Then the loop for i in 2..max_fact is skipped, and fact remains [1].

Similarly for inv_fact.

Now, let's code this.

But there's a case where n=2, and m is up to 1e6. For example, when n=2, m=1e6.

In that case, max_fact is max(0, 1e6-1) → 999999.

So precompute fact up to 999999.

But for n=2, fact[n-2] = fact[0] =1.

So code steps are manageable.

Now, let's handle the case when n=1. But according to constraints, n>=2. So no need to worry.

Now, code:

Implement the steps.

But for precomputing fact and inv_fact when max_fact is zero, we can handle it.

Now, code:

Read n, m, a, b.

MOD = 10**9 +7.

if n ==1:

   impossible, since a != b and n >=2.

Compute max_fact = max(n-2, m-1)

if max_fact <0: # when n=2 and m=1, max_fact is 0.

   pass.

But precompute fact and inv_fact up to max_fact.

Then, for each k in 1 to min(m, n-1):

   if k-1 > m-1 → C(m-1, k-1) is zero.

   else:

       compute comb.

       compute term1.

       compute exponent.

       compute base.

       compute pow_val.

       add to sum.

Let's test the first sample input:

Sample Input 1:

3 2 1 3

Sample Output:5.

Let's see.

n=3, m=2.

max_fact = max(3-2=1, 2-1=1) →1.

precompute fact[0..1] = [1, 1]

inv_fact[0..1] = [1, 1], since inv_fact[1] = pow(1, MOD-2) →1, and inv_fact[0] = inv_fact[1] *1 →1.

Loop k from 1 to min(2, 3-1=2) →k=1,2.

For k=1:

comb = C(1, 0) =1.

term1 = fact[1] * inv_fact[3-1-1=1] →1 * inv_fact[1] =1*1=1.

exponent=3-1-1=1.

base=(1+1)*2=4.

pow_val=4^1=4.

term=1 *1 *4=4.

For k=2:

comb = C(1,1) =1.

term1 = fact[1] * inv_fact[3-2-1=0] →1 * inv_fact[0] →1*1=1.

exponent=3-2-1=0 →pow_val=1.

base=(2+1)*2=6 →6^0=1.

term=1 *1 *1=1.

sum =4+1=5. Which matches the sample.

So the code works for the first sample.

Thus, the code should be correct.
</think>

```python
MOD = 10**9 + 7

n, m, a, b = map(int, input().split())

if n < 2:
    print(0)
    exit()

max_fact = max(n-2, m-1)
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
if max_fact >= 0:
    inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
    for i in range(max_fact - 1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

max_k = min(m, n-1)
result = 0

for k in range(1, max_k + 1):
    c_denominator = k-1
    if c_denominator > m-1:
        continue
    if m-1 < 0:
        comb = 0
    else:
        comb = fact[m-1] * inv_fact[c_denominator] % MOD
        comb = comb * inv_fact[m-1 - c_denominator] % MOD
    
    term_denom = n - k -1
    if term_denom < 0:
        term1 = 0
    else:
        if n-2 < 0:
            term1 = 0
        else:
            term1 = fact[n-2] * inv_fact[term_denom] % MOD
    
    exponent = n - k -1
    base = (k + 1) * m % MOD
    pow_val = pow(base, exponent, MOD) if exponent >=0 else 0
    
    term = comb * term1 % MOD
    term = term * pow_val % MOD
    result = (result + term) % MOD

print(result)
```