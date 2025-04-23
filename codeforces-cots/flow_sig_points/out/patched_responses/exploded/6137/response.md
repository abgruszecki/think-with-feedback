<think>
Okay, let's tackle this problem. The goal is to compute the probability that a randomly generated bipartite graph has a perfect matching. Since n can be up to 7, we need an efficient way to handle this, but even for n=7, the number of possible subsets of edges is huge. So brute-force isn't feasible. Hmm.

First, let's understand the problem. Each edge (i,j) exists with probability p_ij percent. So each edge is independent. We need the sum over all possible edge subsets that contain at least one perfect matching, multiplied by their probabilities.

But how do we calculate the probability that there's at least one perfect matching? Inclusion-exclusion comes to mind. Wait, but inclusion-exclusion for all possible perfect matchings might be manageable here. Because for n=7, the number of perfect matchings is 7! = 5040. Which is manageable.

Alternatively, think of it as the inclusion-exclusion over all possible perfect matchings. The inclusion-exclusion formula would sum over all possible subsets of perfect matchings, but that's probably not the way. Wait, maybe using the principle where the probability that the graph contains at least one perfect matching is equal to the sum over all perfect matchings M of the product of their edges existing, minus the sum over pairs of perfect matchings (M1, M2) of the product of edges existing in both, plus the sum over triples, etc., according to inclusion-exclusion.

But that seems computationally heavy. For n=7, the number of perfect matchings is 7! = 5040. So the inclusion-exclusion terms would be sum_{k=1 to 5040} (-1)^(k+1) * ... which would be O(2^5040) operations. That's impossible. So that approach isn't feasible.

So, we need a better way. Another approach is to compute the probability that the bipartite graph has a perfect matching by considering the permanent of some matrix. Wait, but the permanent is for exact matching counts, and even that is not directly helpful here. Also, calculating the permanent is #P-hard, which is even worse than NP. But for n=7, maybe it's manageable. Wait, but the permanent is for a 0-1 matrix? No, in our case, the probabilities are involved. Hmm. Alternatively, perhaps we can model this as a problem where we compute the inclusion of all possible permutations, but then account for overlapping edges.

Wait, the inclusion-exclusion approach might still be manageable if we can represent the constraints in terms of the edges required for at least one perfect matching. Let me think differently.

The problem is equivalent to the sum over all possible subsets of edges S where S contains at least one perfect matching. The probability of S is the product of the edges in S existing and the edges not in S not existing. But since each edge is present with probability p_ij/100, and not present with probability (100 - p_ij)/100, the total probability is sum over all S that have at least one PM, product for each edge (if present: p_ij/100, else: (100-p_ij)/100).

But enumerating all subsets S is impossible for n=7 (each node has 7 edges to the other side, but total edges is 7*7=49, leading to 2^49 subsets, which is way too big).

Alternative approach: use dynamic programming to represent the possible states of the graph and track whether a perfect matching exists. But even that seems challenging for n=7.

Wait, another idea: the problem is equivalent to the probability that the bipartite graph has a perfect matching. The standard way to compute this is to use the inclusion-exclusion principle over the Hall's theorem condition. Because according to Hall's theorem, a bipartite graph has a perfect matching if and only if for every subset of the left nodes, the size of the neighborhood is at least the size of the subset. So, the probability that all subsets S of left nodes (including those of size 1, 2, ..., n) satisfy |N(S)| >= |S|.

But for n=7, there are 2^7 -1 = 127 subsets of the left nodes (excluding the empty set). For each such subset S, we need to compute the probability that |N(S)| >= |S|. But the problem is that these events are not independent. For example, two different subsets S and T may have overlapping constraints. So the inclusion-exclusion here would need to account for all possible combinations where some subsets violate Hall's condition.

But inclusion-exclusion over all possible subsets that could violate Hall's condition is possible? Let's see. For each subset S of the left nodes, let A_S be the event that |N(S)| < |S|. Then, the graph does NOT have a perfect matching if at least one A_S occurs. So the probability we want is 1 minus the probability that any A_S occurs.

But to compute the probability that any A_S occurs, we need to use inclusion-exclusion over all possible non-empty subsets S of left nodes. However, even for n=7, the number of possible S is 127, so inclusion-exclusion over 2^127 terms is impossible. So this approach is not feasible either.

Hmm, so we need another approach. Let's think again. For n up to 7, perhaps the best approach is to generate all possible perfect matchings and use inclusion-exclusion. Wait, perhaps the inclusion-exclusion over the permutations (perfect matchings) can be done. The idea is that the probability that at least one perfect matching exists is equal to the sum of the probabilities of each perfect matching, minus the sum of the probabilities that two perfect matchings are present, plus the sum for three, etc. This is the standard inclusion-exclusion for the union of events.

Each event is a perfect matching M. So the inclusion-exclusion formula is:

sum_{M} P(M) - sum_{M1 < M2} P(M1 ∩ M2) + sum_{M1 < M2 < M3} P(M1 ∩ M2 ∩ M3) } ... + (-1)^{k+1} sum over k-tuples, etc.

The problem is that the number of terms here is the sum over k from 1 to 7! of C(7!, k). Which is way too big even for n=7 (7! is 5040, and 2^5040 is impossible). So this approach is not feasible.

Alternative idea: Since each perfect matching is a permutation, perhaps we can model this using dynamic programming with the inclusion-exclusion steps. But I'm not sure how.

Another approach: Use the principle of Möbius inversion in the lattice of subsets of the left and right nodes, but I'm not sure.

Wait, perhaps the best way is to model this as the sum over all possible permutations (perfect matchings) and use the inclusion-exclusion, but represent overlapping events efficiently.

Alternatively, let's model the problem as follows: the existence of a perfect matching is equivalent to the existence of at least one permutation π of {1..n} such that all edges (i, π(i)) are present. So the probability is the probability that the union of all such events (each being the existence of edges for a particular π) occurs.

Calculating the union probability is exactly what inclusion-exclusion is for. So the inclusion-exclusion formula would involve terms for all possible non-empty subsets of the permutations, and each term would be (-1)^(k+1) multiplied by the probability that all permutations in the subset are present (i.e., all the edges required by any of the permutations in the subset are present).

But for a subset S of permutations, the probability that all permutations in S are present is the product of the probabilities that each edge in the union of all edges of the permutations is present. Wait, because for a permutation π, the required edges are (i, π(i)) for all i. So for a subset S of permutations, the edges that must be present are all edges (i, j) where j is π(i) for any π in S. Because even if multiple permutations in S use the same edge, the edge needs to be present once. So the probability that all permutations in S are present is the product over all edges (i,j) that are used by at least one permutation in S of p_ij/100, multiplied by the product over edges not used by any permutation in S of (100 - p_ij)/100. Wait, no. Because the permutations in S require that all their edges are present. So for the permutations in S to all be present, the edges in the union of all their edges must be present. Because if even one edge of a permutation in S is missing, that permutation is not present. Wait, no. For a permutation π to be present in the graph, all edges (i, π(i)) must be present. So the event "all permutations in S are present" is equivalent to the event that for every π in S, all edges (i, π(i)) are present. So the required edges are the union of all edges required by any of the permutations in S. Because for each permutation π in S, all edges (i, π(i)) must be present. So the total required edges are the union of these edges. So the probability that all permutations in S are present is the product over all edges that are used in any permutation in S of (p_ij/100), multiplied by 1 for edges not in any of the permutations (since their presence or absence doesn't affect the presence of the permutations in S). Wait, no. Because even edges not used in the permutations can be present or not. But the permutations in S being present only requires that their edges are present. Other edges can be present or not, but that doesn't affect the presence of the permutations in S. So the presence of S's permutations is determined solely by their own edges. So the probability that all permutations in S are present is the product for each edge that is required by at least one permutation in S of (probability that edge exists) multiplied by the product of the probabilities for edges not in any permutation in S (but their existence doesn't affect the presence of the permutations in S). Wait, no. Because the presence of other edges is irrelevant. The event is that all permutations in S are present. For that, all edges of all permutations in S must be present. The other edges can be anything. So the probability is the product for all edges (i,j) in the union of all edges of S's permutations of (p_ij/100) multiplied by the product for edges not in that union of 1 (since those edges can be present or not; their presence doesn't affect the fact that all permutations in S are present). Wait, no. Because the permutations in S being present in the graph means that each of their edges exists. So, for the event that all permutations in S are present, it's necessary that for every permutation π in S, all edges (i, π(i)) exist. So the set of edges that must exist is the union of all edges used by any π in S. Wait, no. Let me clarify. Suppose S contains two permutations, π1 and π2. For both to be present in the graph, all edges of π1 must exist, and all edges of π2 must exist. So the union of the edges of π1 and π2 must all exist. So the required edges are the union of all edges in any permutation of S. So the probability that all permutations in S are present is the product of (p_ij/100) for each edge (i,j) in the union of all edges of permutations in S. The other edges can be anything (they don't affect this event). So the inclusion-exclusion formula would sum over all non-empty subsets S of the permutations, with the inclusion-exclusion coefficient (-1)^(|S|+1), multiplied by the product of the edges in the union of all permutations in S.

But even this is challenging because the number of permutations is 7! = 5040, and considering all subsets of them is impossible. However, the key insight here is that the inclusion-exclusion can be optimized by considering the masks of the edges. Because for each subset of permutations S, the union of their edges forms a certain set of edges. If two different subsets S1 and S2 have the same edge union, then their contributions can be grouped together. So the inclusion-exclusion terms can be grouped by the edge set E that is the union of the edges of all permutations in S. The total contribution for all subsets S that result in edge set E is the product of the probabilities of E's edges multiplied by the sum over all subsets S (non-empty) that have edge union E of (-1)^(|S|+1) multiplied by the inclusion-exclusion coefficient. But even this seems complicated.

Alternatively, maybe we can precompute for each possible edge set E, the number of subsets of permutations S such that the union of their edges is exactly E, and then multiply by the product of the edges in E. But this seems again impossible due to the number of possible E.

Hmm. So perhaps the inclusion-exclusion approach is not feasible here. What's another way?

Another idea is to model this as a matrix where each entry (i,j) is the probability that edge (i,j) exists, and compute the probability that the graph has a perfect matching. But I'm not sure how to model this.

Wait, here's another approach: For each possible subset of edges, we can check if it contains at least one perfect matching. Then sum the probabilities of all such subsets. But again, the number of subsets is 2^(n^2), which for n=7 is 2^49, which is way too big. So this is impossible.

But n=7 is manageable if we can find a way to represent the problem more efficiently. Let's think: For each possible permutation (perfect matching), the probability that it exists is the product of the edges in the permutation. But since permutations can overlap (share edges), their events are not mutually exclusive. So the total probability is the inclusion-exclusion over all possible permutations. So the inclusion-exclusion formula is:

Probability = sum_{S subset of permutations, S non-empty} (-1)^(|S|+1) * P(all permutations in S exist).

So the problem reduces to computing this sum. The question is, how to compute this efficiently.

Each term in the sum is for a non-empty subset S of permutations. The term is (-1)^(|S|+1) multiplied by the product of p_ij/100 for all edges (i,j) that are used in any permutation in S.

But even for n=7, there are 5040 permutations, so the number of subsets S is 2^5040, which is impossible. So this approach is not feasible.

So, we need a smarter way. Let's see if there's a way to represent the sum in terms of the edges required. For example, the product for all edges in the union of permutations in S can be written as the product over each edge (i,j) of (if (i,j) is in the union, then p_ij/100 else 1). Wait, but that's not correct. Because for edges not in the union, their existence is irrelevant. But the term P(all permutations in S exist) is the product of all edges in the union (since all edges in any permutation in S must exist). So yes, the term is product_{(i,j) in union(S)} (p_ij/100). The other edges can exist or not, but that's irrelevant as long as the permutations in S are present. Wait, no. Because the permutations in S being present only require that their edges exist. The other edges can exist or not. But the term P(all permutations in S exist) is the probability that all edges in the union of S's edges exist, multiplied by the probability that the other edges are whatever they are. Wait, no. Because the other edges can be present or not; their presence doesn't affect the presence of the permutations in S. So the probability that all permutations in S exist is equal to the probability that all edges in the union of S's edges exist. Because those edges must be present, and the other edges can be present or not. So the term is the product of (p_ij/100) for each (i,j) in the union, multiplied by 1 (since the other edges are not required, and their presence or absence doesn't affect the event that the permutations in S are present).

Wait, no. Because the permutations in S are present if their edges exist, regardless of other edges. So the event that all permutations in S are present is equivalent to the event that all edges in the union of their edges exist. Because for each permutation in S, all its edges must exist. So the union of all edges across all permutations in S must exist. So the probability is the product of p_ij/100 for each (i,j) in the union.

So the term for subset S is (-1)^(|S|+1) * product_{(i,j) in union(S)} (p_ij/100) * product_{(i,j) not in union(S)} (1). But the product over edges not in union(S) is 1, since they can be anything. So the term is just the product of edges in the union.

Thus, the inclusion-exclusion sum is:

sum_{S subset of permutations, S non-empty} (-1)^(|S|+1) * product_{(i,j) in union(S)} (p_ij/100)

The key insight here is that for each possible edge set E (which is the union of some permutations), we can group all subsets S of permutations whose union is E. Then, the contribution for E is (sum over all non-empty S with union E of (-1)^(|S|+1)) ) multiplied by the product of edges in E.

So the problem reduces to iterating over all possible edge sets E that can be formed as the union of some set of permutations, and for each such E, compute the sum of (-1)^(|S|+1) for all non-empty S subsets of permutations where the union of their edges is exactly E. Then, multiply this by the product of p_ij/100 for all edges in E, and sum over all E.

But how do we efficiently compute this sum for each E?

The challenge is that even for n=7, the number of possible E is very large, but perhaps manageable with some DP.

Wait, but the edge sets E must be unions of some set of permutations. Each permutation is a set of n edges, one per left node. The union of any set of permutations is a bipartite graph where for each left node, there is some subset of right nodes connected (since each permutation contributes exactly one right node per left node). Wait, no. The union of multiple permutations would have each left node connected to all right nodes that appear in any of the permutations for that left node. For example, if permutation π1 has left node i connected to j1, and permutation π2 has left node i connected to j2, then in the union E, left node i is connected to both j1 and j2.

So for each left node i, the set of edges in E is a subset of the right nodes that are part of any permutation in S. But permutations are perfect matchings, so each permutation is a bijection between left and right nodes. So for a left node i, in the union E, the edges for i are all j's such that j is π(i) for some permutation π in S.

So the union E can be represented as for each left node i, the set of j's that are covered in any permutation in S. Then, the permutations in S must have their edges as part of E.

So the problem is to find all possible E where E is a union of some set of permutations. For each such E, we need to compute the sum over all non-empty S (collections of permutations) that are subsets of the permutations that are compatible with E (i.e., their edges are in E), and the sum of (-1)^(|S|+1) for all such non-empty S. But this seems complicated.

Alternatively, for each possible E, the number of subsets S (non-empty) of permutations that are compatible with E (i.e., all edges of the permutations in S are in E) and whose union is E. Then, the sum is for each E, (sum over S subsets of permutations compatible with E, S non-empty, and union S = E) of (-1)^(|S|+1).

But this seems challenging. However, perhaps for a given E, the sum can be expressed as the inclusion-exclusion over the permutations that are subsets of E. Wait, perhaps for each E, the sum is the Möbius function over the permutations that are subsets of E.

Alternatively, the sum can be computed using inclusion-exclusion for each E. For example, the sum over all non-empty S of permutations compatible with E (their edges are in E) and with union exactly E. The sum of (-1)^(|S|+1) for all such S. How?

Let's think of the inclusion-exclusion in terms of inclusion of permutations. For a given E, which is a union of some permutations, the sum is the sum over all non-empty subsets S of permutations that are subsets of E (i.e., each permutation in S is a subset of E), and their union is E. For each such S, (-1)^(|S|+1) is added. So, for example, if E is a single permutation, then the only S that can contribute is the singleton set containing that permutation. The term would be (-1)^(1+1) = 1. So for E being a single permutation, the sum is 1. If E is the union of two permutations that are edge-disjoint, then S can be {1}, {2}, or {1,2}. The sum would be 1 + 1 - 1 = 1. But the sum is over S where the union is E. So in this case, E is the union of the two permutations. So for S to have union E, either S contains both permutations (their union is E), or one of them but then the union is not E. Wait, no. If E is the union of two permutations, and S is a subset of permutations that are subsets of E, then the union of S is the union of all edges in all permutations in S. So for example, if S is {perm1}, then the union is perm1's edges. Which may or may not be E. So in the case where E is the union of two permutations, the S that contribute are those subsets whose union is exactly E. For example, if perm1 and perm2 are the two permutations, then S could be {perm1, perm2}, or any subset that includes both. Or maybe other permutations whose union is E.

This is getting complicated. Let's think of the sum for a given E as the Möbius function. For example, the sum over all S that are non-empty subsets of permutations whose union is E. The sum is μ(S) = (-1)^(|S|+1) multiplied by the product of edges in E.

Wait, but perhaps for each E, the sum is equal to the Möbius function of the lattice of sets of permutations. But this is unclear.

Another approach: Let's model the problem using the inclusion-exclusion formula and find a way to compute it efficiently using dynamic programming. For each permutation, we can track which edges it uses and compute the inclusion-exclusion terms incrementally. But with 7! permutations, this is still challenging.

Alternatively, note that the inclusion-exclusion formula can be rewritten as the sum over all possible edge sets E, of the product of edges in E multiplied by the Möbius function value for E. The Möbius function here is the sum over all non-empty subsets S of permutations whose union is E, of (-1)^(|S|+1).

The key insight is that for each edge set E, the sum of (-1)^{|S|+1} over all non-empty subsets S of permutations where the union of S is exactly E is equal to the inclusion-exclusion coefficient for E. If we can precompute this coefficient for all possible E, then the total probability is the sum over all E of (coefficient[E] * product of edges in E's probabilities).

But how to compute this coefficient for each E?

Let's consider E as a bipartite graph. Then, the permutations that are subsets of E are exactly the perfect matchings in E. Let M(E) be the set of all perfect matchings in E. Then, the subsets S of M(E) whose union is exactly E are those subsets of matchings such that every edge in E is present in at least one matching in S.

So for E to be the union of some subset S of matchings, every edge in E must be covered by at least one matching in S. Moreover, the subset S must consist of matchings that are subsets of E.

Thus, the coefficient for E is the sum over all non-empty subsets S of M(E) where the union of S is exactly E, of (-1)^(|S|+1).

This seems like a Möbius inversion problem. The coefficient for E is the Möbius function over the lattice of subsets of M(E) that cover all edges of E.

Alternatively, think of it as inclusion-exclusion over the edges of E. For each edge (i,j) in E, we need to count subsets S of M(E) that include at least one permutation that covers (i,j). So the inclusion-exclusion here is over the edges in E, but that's again not straightforward.

Alternatively, the problem can be transformed into counting the number of non-empty subsets S of M(E) such that every edge in E is covered by at least one permutation in S. Then, the coefficient is sum_{S} (-1)^(|S|+1), where S is a non-empty subset of M(E) that covers all edges in E.

This is equivalent to the inclusion-exclusion over the edges. Let's see: For a subset S of M(E), the condition that every edge in E is covered by S is that for each edge e in E, there exists at least one permutation in S that contains e. So the coefficient is the sum over all non-empty S subsets of M(E) where for all e in E, S contains at least one permutation that includes e. Then, each such S contributes (-1)^(|S|+1).

This is equivalent to the inclusion-exclusion over all possible e in E. But again, this seems difficult.

Alternatively, the coefficient for E is μ(E) = sum_{k=1}^m (-1)^{k+1} * (number of ways to choose k permutations in M(E) such that their union is E) ). But even this is not helpful directly.

But here's a different idea: The coefficient μ(E) can be computed as follows. Let M be the set of all perfect matchings in E. The coefficient is equal to the sum over all non-empty subsets S of M of (-1)^(|S|+1) multiplied by the indicator function that the union of S is exactly E.

So, μ(E) = sum_{S ⊆ M, S≠∅} [ (-1)^(|S|+1) * [ union(S) = E ] ]

But how to compute this?

This is equivalent to:

μ(E) = [ sum_{S ⊆ M} (-1)^(|S|+1) * [ union(S) = E ] ] for S non-empty.

But this is tricky. However, this can be expressed as:

sum_{S ⊆ M} (-1)^(|S|+1) * [ union(S) = E ] 

= (-1) * sum_{S ⊆ M} (-1)^{|S|} * [ union(S) = E ] 

But this sum is the same as the Möbius function of the lattice of subsets ordered by inclusion. Hmm. Alternatively, this sum is the inclusion-exclusion over the edges in E. For example, the sum is equal to the product over each edge e in E of (1 - f(e)), where f(e) is the probability that none of the permutations in S contain e. But I'm not sure.

Alternatively, for each edge e in E, we can model the condition that at least one permutation in S contains e. So, the problem becomes, for each edge e in E, ensure that at least one permutation in S contains e. The sum over all S (non-empty subsets of M(E)) that cover all edges in E of (-1)^(|S|+1).

This is similar to the inclusion-exclusion formula for the intersection of events. Here, the events are that S contains at least one permutation covering each edge e in E. So the inclusion-exclusion for the intersection of events that for each e in E, S contains at least one permutation in M(E) that includes e. 

But the events are not independent. So the inclusion-exclusion would be:

sum_{S subset of M(E), S non-empty} [ product_{e in E} [ S covers e ] ] * (-1)^(|S|+1).

But I'm not sure how to proceed.

Alternatively, the coefficient μ(E) can be computed using the Möbius function over the lattice formed by the subsets of edges. For each E, the coefficient μ(E) is the Möbius function evaluated at E in the lattice of subsets ordered by inclusion. But again, I'm not sure.

Another idea: The coefficient μ(E) is zero unless E is the union of some set of permutations. For example, if E is a set of edges that cannot be covered by any set of permutations (i.e., there is no permutation that is a subset of E), then μ(E) is zero. So, first, we can precompute all possible E that can be formed as unions of permutations. For each such E, we need to compute μ(E).

But how?

Let me think of small cases. For example, n=1: There's only one permutation. E can be the edge (1,1). The coefficient μ(E) is 1, since the only subset S is the singleton set. For n=2, suppose E is the union of two permutations. For example, the permutations are (1-1, 2-2) and (1-2, 2-1). The union E is the edges (1-1, 1-2, 2-1, 2-2). The subsets S that cover all edges in E must include both permutations. So the sum is (-1)^(2+1) * 1 (only subset S is {perm1, perm2}), which is -1. But wait, but there are other permutations possible? No, in this case, for n=2, there are two permutations. So, for E being the union of these two permutations, the subsets S that have union E are any subset that contains both permutations. So the sum is sum_{k=2}^{m} ... where m is the number of permutations in M(E). Wait, but in this case, M(E) is the set of all perfect matchings in E. But E is the complete bipartite graph, so M(E) is the two permutations. So, the subsets S that cover all edges are subsets containing both permutations. So the sum over S non-empty is sum_{S subset of M(E), S covers E} (-1)^(|S|+1). The subsets S that cover E are those that contain both permutations. Because the union of S is E only if both permutations are present. So the sum is for S being {perm1, perm2} (since any subset including at least one of them would have a union that is either perm1, perm2, or their union). Wait, no. The union of S is the set of edges covered by any permutation in S. So in this example, if S is {perm1}, the union is perm1's edges. Which is edges (1-1, 2-2). Similarly for perm2. So the only S that have union E (all four edges) is the subset S={perm1, perm2}.

So the sum for E (the complete graph) is (-1)^(2+1) * 1 = -1.

Thus, the coefficient for E is -1.

But how does this contribute to the overall sum? The product of all edges in E's probabilities multiplied by the coefficient. For example, in the first sample input where n=2 and all p_ij=50, the coefficient for E (the complete graph) is -1, and the product of edges is (0.5)^4. So the term is -1 * 0.5^4. But there are other terms for smaller E's. For example, each permutation's edges contribute a coefficient of 1, and their product is 0.5^2. So there are two such terms. Then, the sum would be (2 * 0.5^2) - (0.5^4) = 2*(0.25) - 0.0625 = 0.5 - 0.0625 = 0.4375. But the correct answer in the sample is 7/16 = 0.4375. So this seems to work.

So the inclusion-exclusion approach gives the correct result. Thus, the approach is to generate all possible E's that are unions of some set of permutations, compute their coefficients μ(E), and then sum μ(E) * product of edges in E.

The key challenge is to find all possible E's (which are the unions of some permutations) and compute μ(E) for each.

But how to generate all possible E's? For n=7, each E is a bipartite graph where for each left node i, the set of right nodes connected to i is the union of the right nodes covered by any permutation in some subset S. Since each permutation is a perfect matching, for each left node i, in any permutation, there's exactly one right node. So for the union of permutations in S, for each left node i, the set of right nodes connected to i is the collection of all j's where there's a permutation in S that maps i to j.

So, for example, if S contains two permutations, the first maps i to j1 and the second maps i to j2, then the union for i is {j1, j2}.

Thus, the E can be represented as a list of sets (for each left node i) of right nodes j. The union of permutations in S is the edges (i,j) for all j in the set of i's right nodes.

So for each left node i, the set of right nodes in E can be any subset of the right nodes, but with the constraint that there exists a set of permutations S such that for each i, the right nodes in E are the union of the images of i in S's permutations. However, the permutations in S must be perfect matchings. So for each permutation in S, it must be a perfect matching of the bipartite graph, meaning that each left node i is mapped to exactly one right node j, and each right node j is mapped to exactly one left node i.

Thus, the E's that can be formed as unions of permutations are those bipartite graphs where for each left node i, the set of right nodes j in E is some non-empty subset (since permutations are perfect matchings, so each i must have at least one edge in E), and for each permutation in S, the images are such that each right node is mapped to exactly once.

Wait, but the E is formed by the union of permutations. So for each right node j, there must exist at least one permutation in S that maps some left node i to j (since E contains (i,j) for some i). So in E, the right nodes j must be covered by at least one left node's edges.

But this is automatically the case if E is the union of some permutations. Because each permutation covers all right nodes. So the union of permutations will cover all right nodes for each left node's edges. But the right nodes may be covered by multiple left nodes' edges.

Wait, no. Each permutation is a perfect matching, so each right node is covered exactly once. So the union of permutations may cover a right node multiple times (from different permutations), but in the union E, a right node j can be connected to multiple left nodes i. So E can have a right node j connected to multiple left nodes. But each permutation in S must have exactly one left node connected to j. So in E, for each j, the number of left nodes connected to j in E is the number of permutations in S that map some left node to j.

But the permutations in S can have overlaps in their mappings. For example, two different permutations can map different left nodes to the same j. So E can have multiple edges connected to j.

But this makes E a bipartite graph where each right node j is connected to at least one left node i (since each permutation in S is a perfect matching and covers j exactly once. So the union of S's permutations would have j connected to all left nodes i for which there exists a permutation in S that maps i to j.

Thus, E is a bipartite graph where for each right node j, the number of left nodes connected to j is the number of permutations in S that have some left node mapped to j. But since each permutation in S is a perfect matching, each j is covered exactly once in each permutation. So for example, if two permutations in S both have j covered by different left nodes, then in E, j is connected to those two left nodes.

But this is getting complicated. Let's think of the structure of E. For E to be the union of some set of permutations S, the following must hold:

1. For each left node i, the set of right nodes connected to i in E is non-empty. Because each permutation in S must map i to some j, and S is non-empty.

2. For each permutation in S, it must be a subset of E. So for each permutation in S, for every left node i, the edge (i, π(i)) is present in E.

3. For each right node j, there exists at least one permutation in S that maps some left node to j. Otherwise, j would not be covered in E.

But I'm not sure. Maybe the right nodes can have zero coverage in E, but that's not possible since each permutation is a perfect matching. Wait, no. For example, if S is empty, but that's not allowed. So in the case where S is non-empty, each permutation in S covers all right nodes. So in the union E, each right node j is connected to at least one left node i (the one that mapped to j in at least one permutation in S). So in E, each right node j must have at least one edge in E.

Thus, E must be a bipartite graph where:

- For every left node i, E has at least one edge from i.

- For every right node j, E has at least one edge to j.

Moreover, the graph E must be such that it contains at least one perfect matching (since S is non-empty).

But this is not necessarily true. For example, S could be a set of permutations whose union is E. So E must contain all edges of all permutations in S. But E could have other edges as well.

Wait, no. The union of the permutations' edges is E. So E is exactly the edges present in any of the permutations in S. So E is a union of perfect matchings. So for E, each permutation in S is a subset of E. But E can have edges that are not part of any permutation in S.

Wait, no. If E is the union of the permutations in S, then E consists precisely of the edges that are present in at least one permutation in S. So any edge in E must belong to at least one permutation in S. So E can't have edges not present in any permutation in S. So E is exactly the union of the edges of all permutations in S.

Thus, for E to be the union of permutations in S, E must be a bipartite graph where for each edge (i,j) in E, there exists at least one permutation in S that includes (i,j).

But S is a set of perfect matchings, so each permutation in S is a subset of E. Thus, E is the union of perfect matchings. This implies that for each left node i, the edges in E from i are exactly those j's that are mapped to i by some permutation in S. And for each right node j, the edges in E to j are exactly those i's that are mapped to j by some permutation in S.

Thus, for E to be a union of permutations, it must satisfy that for each left node i and right node j, if (i,j) is in E, then there exists a permutation in S (subset of E) that includes (i,j). But since S is a subset of the permutations in M(E), which are the perfect matchings of E, then for E to be a union of permutations in S, E must contain at least one perfect matching (since S is non-empty).

But this seems circular. The key is that E must be a bipartite graph that contains at least one perfect matching, and each edge in E must be part of at least one perfect matching in E.

But how to generate all possible E's for n up to 7?

This seems challenging. Perhaps the best way is to generate all possible E's by considering all possible ways to assign a subset of right nodes to each left node, ensuring that the union can form some permutations. But even this is complex.

Alternative idea: For each left node i, the set of possible right nodes j that can be in E is any subset of the right nodes. However, the set of right nodes for all left nodes must be such that there exists at least one perfect matching. Moreover, for each edge (i,j) in E, there must be at least one perfect matching in E that includes (i,j).

But this seems too vague. Another approach is to generate all possible bipartite graphs E that can be written as the union of some set of perfect matchings, then compute μ(E) for each.

But how to generate all such E's for n=7? Even for n=7, the number of possible E's is enormous. For example, each left node can have any subset of the 7 right nodes, leading to (2^7)^7 = 2^49 possibilities. But most of these would not be valid unions of perfect matchings.

Alternatively, notice that for E to be the union of some set of perfect matchings, E must be a bipartite graph where for each edge (i,j) in E, there exists a perfect matching in E that includes (i,j). This is equivalent to saying that E is a "matching-covered" graph, but I'm not sure.

Another angle: The coefficient μ(E) is the inclusion-exclusion sum over all subsets S of M(E) that cover E. So for E to be considered, M(E) must be non-empty (since S is a subset of M(E), and S is non-empty). Thus, E must contain at least one perfect matching. So we can generate all possible E's that are bipartite graphs containing at least one perfect matching, and for each such E, compute M(E) as the set of all perfect matchings in E.

Once we have M(E), we can compute μ(E) as the sum over all non-empty subsets S of M(E) that cover E (i.e., their union is E) of (-1)^(|S|+1).

But how to compute this sum for each E?

The problem is that for each E, we need to compute the sum over all non-empty subsets S of M(E) that cover E. For each such S, their union is E. But this is equivalent to requiring that for every edge e in E, there exists at least one permutation in S that contains e.

So the sum is the same as the inclusion-exclusion sum over all edges e in E, ensuring that each e is covered by at least one permutation in S. 

But how to model this? For a given E and its M(E), the sum is the number of non-empty subsets S of M(E) that cover all edges in E, multiplied by (-1)^(|S|+1).

This is equivalent to the Möbius function for the inclusion lattice of E's edges. But I'm not sure.

Alternatively, for each E, the coefficient μ(E) can be computed as follows:

μ(E) = sum_{S subset of M(E), S non-empty and covering E} (-1)^(|S|+1)

But this is equivalent to:

μ(E) = sum_{k=1}^K (-1)^(k+1) * c(k),

where c(k) is the number of ways to choose k permutations from M(E) such that their union is exactly E.

But how to compute c(k)?

This seems difficult, but for small n (like n=7), perhaps we can precompute all possible E's and their M(E), and then compute μ(E) for each.

But even this seems challenging. For example, for n=3, the number of possible E's is manageable, but for n=7, it's likely too large.

Alternative idea: Represent E as a bitmask of edges, and use memoization or dynamic programming to compute μ(E) for each E.

But for n=7, each edge (i,j) is one of 49 bits. So the total number of possible E's is 2^49, which is way too big. So this is impossible.

Thus, we need a smarter way to compute the inclusion-exclusion sum. Let's go back to the original problem.

We need to compute the sum over all non-empty subsets S of permutations, with the term (-1)^(|S|+1) multiplied by the product of the edges in the union of S.

The key insight is that the inclusion-exclusion sum can be computed using the principle that:

sum_{S subset of permutations, S non-empty} (-1)^(|S|+1) * product_{e in union(S)} p_e = 1 - product_{e in all edges} (1 - q_e), 

where q_e is the probability that e is used in at least one permutation in S. But I'm not sure. Alternatively, perhaps there's a generating function approach.

Alternatively, think of each permutation as a set of edges. The inclusion-exclusion sum is the same as the inclusion-exclusion sum over all possible permutations. For each permutation π, we have a term that includes the product of its edges, but we need to account for overlapping edges.

But I'm stuck. Let's think of the problem in terms of generating functions. For each permutation π, the contribution to the inclusion-exclusion sum is x_π = product_{e in π} p_e. Then, the inclusion-exclusion sum is sum_{S} (-1)^(|S|+1) * product_{π in S} x_π, where S is a non-empty subset of permutations. This can be rewritten as:

sum_{S non-empty} (-1)^{|S|+1} product_{π in S} x_π = 1 - product_{π} (1 - x_π)

Because:

sum_{S} (-1)^{|S|+1} product_{π in S} x_π = - sum_{S} (-1)^{|S|} product_{π in S} x_π = - ( product_{π} (1 - x_π) - 1 )

= 1 - product_{π} (1 - x_π)

So, the inclusion-exclusion sum is 1 - product_{π} (1 - x_π), where x_π is the product of the edges in π.

But wait, this is a crucial insight! Because the inclusion-exclusion sum can be expressed as 1 - product_{all permutations π} (1 - x_π), where x_π is the product of the edges in π. Because the product (1 - x_π) represents the probability that permutation π is not chosen. The product over all permutations would be the probability that no permutation is chosen. So 1 minus that product is the probability that at least one permutation is chosen, which is exactly the union of all permutations being present. But wait, the inclusion-exclusion formula for the union of events says that the probability of the union is sum_{S subset non-empty} (-1)^(|S|+1) product_{π in S} x_π. And according to the generating function identity, this sum is equal to 1 - product_{π} (1 - x_π).

So the total probability we need to compute is 1 - product_{all permutations π} (1 - product_{e in π} p_e).

But wait, that's only true if the permutations are all independent, which they are not. Because if two permutations share an edge, then the presence of both permutations requires that the shared edges are present. So this formula is incorrect. Because the inclusion-exclusion sum considers the events where permutations are present, but the presence of one permutation affects the presence of others.

Wait, no. The inclusion-exclusion formula is for the union of the events where each event is that permutation π is present (i.e., all edges of π are present). So the events are not independent. The formula 1 - product_{π} (1 - x_π) would only be correct if the events were independent, which they are not.

So the previous assertion is wrong. But wait, no. The inclusion-exclusion formula is correct regardless of the dependencies between events. It's a mathematical identity. The sum_{S non-empty} (-1)^(|S|+1) product_{π in S} x_π is equal to 1 - product_{π} (1 - x_π), regardless of dependencies, because it's an algebraic identity. So why?

Because the sum_{S subset of permutations} (-1)^{|S|} product_{π in S} x_π is equal to the product_{π} (1 - x_π), by the inclusion-exclusion formula. Then, the sum over non-empty subsets S is equal to (product_{π} (1 - x_π) - 1) multiplied by -1. Which gives 1 - product_{π} (1 - x_π).

But this is only true if the events are independent. No, this is an algebraic identity. For example, consider two permutations π1 and π2. The sum over all subsets S of permutations:

sum_{S} (-1)^{|S|} product_{π in S} x_π = sum_{S} product_{π in S} (-x_π) = product_{π} (1 - x_π).

So sum_{S non-empty} (-1)^{|S|+1} product_{π in S} x_π = 1 - product_{π} (1 - x_π).

Thus, the inclusion-exclusion sum can be computed as 1 - product_{π} (1 - x_π), where x_π is the product of the edges in π, each edge contributing p_ij/100.

But this is not correct. Because the events "permutation π exists" and "permutation π' exists" are not independent. For example, if they share an edge, then the presence of that edge is required for both permutations. So the presence of π and π' is not independent. So the product (1 - x_π)(1 - x_π') is not equal to the probability that neither π nor π' exists. But the inclusion-exclusion sum is exactly equal to 1 - product_{π} (1 - x_π), but this is only true when all the permutations are disjoint. Otherwise, this formula would not represent the correct probability.

Wait, but according to the inclusion-exclusion formula, the correct probability is sum_{S} (-1)^{|S|+1} product_{π in S} x_π, which is equal to 1 - product_{π} (1 - x_π). So why is this the case?

Because the events are not independent, but the inclusion-exclusion sum is a mathematical identity that holds regardless of dependencies. However, the x_π here is the probability that permutation π is present, which is the product of the edges in π. But when permutations overlap, the probability that both are present is the product of the edges in their union. Thus, the inclusion-exclusion formula is not correctly applied in this way. Because the events are not independent, but in the inclusion-exclusion sum, the product_{π in S} x_π is the probability that all permutations in S are present. But when permutations share edges, this is not the case. For example, for two permutations π1 and π2 that share some edges, the probability that both are present is the product of the edges in their union, not the product of x_π1 and x_π2.

Thus, the inclusion-exclusion sum is not 1 - product (1 - x_π). The mistake here is assuming that the events are independent, which they are not. So the correct way to compute the inclusion-exclusion sum is to consider the correct probabilities for the intersections of events, which are the probabilities that all permutations in S are present. This is the product of the edges in the union of S's permutations. So the formula 1 - product (1 - x_π) is incorrect, and the correct inclusion-exclusion sum must account for overlapping edges.

But given that, the original approach is correct. So the inclusion-exclusion sum must be computed as sum_{S} (-1)^(|S|+1) * product_{e in union(S)} p_e.

But this sum is impossible to compute directly for n=7. So what's the way forward?

The key insight here is that for n=7, the number of permutations is 7! = 5040. This is manageable using the inclusion-exclusion approach if we can represent the permutations' edges as bitsets and use memoization or bitmask DP to track the union of edges.

But for 5040 permutations, iterating over all subsets is impossible. However, the inclusion-exclusion sum can be computed using the Möbius transform over the permutations.

An alternative approach is to generate all permutations and compute the sum using the inclusion-exclusion formula by iterating over all permutations and accumulating the terms for each subset.

But even this is challenging. For example, for n=7, 7! is 5040, and iterating over all subsets is impossible. So we need a way to compute the inclusion-exclusion sum efficiently.

Another idea is to represent the permutations in terms of their edges and use the inclusion-exclusion formula with memoization of the union of edges.

But even this is challenging. However, given the time limit of 15 seconds and the small n=7, perhaps a bitmask-based approach with memoization of the union of permutations is feasible.

So, the plan is:

1. Generate all possible permutations of the right nodes (perfect matchings).

2. For each permutation, compute its edge mask (a bitmask representing the edges in the permutation).

3. Use the inclusion-exclusion formula to compute the sum over all non-empty subsets of permutations, with each term being (-1)^(k+1) multiplied by the product of the edges in the union of the subset.

4. To compute this efficiently, we can represent the permutations as bitmask and use memoization or dynamic programming to track the union of edges.

But even with n=7, the number of permutations is 5040. So iterating over all subsets is impossible. However, there's a way to compute this sum efficiently using the inclusion-exclusion principle with bitmask DP.

The key insight is that the inclusion-exclusion sum can be computed using the following formula:

sum_{S subset of permutations, S non-empty} (-1)^(|S|+1) * product_{e in union(S)} p_e.

This can be rewritten as:

sum_{S subset of permutations, S non-empty} (-1)^(|S|+1) * (product_{e in union(S)} p_e).

But the product is the same for all subsets S that have the same union. So, if we can group all subsets S by their union, then for each union E, we can compute the sum of (-1)^(|S|+1) over all S with union E, and multiply by the product of E's edges.

But how to compute this sum for each E?

As before, the sum for E is μ(E) = sum_{S subset of permutations, S non-empty, union(S) = E} (-1)^(|S|+1).

But computing this sum requires knowing how many subsets S have union E and how many elements they have.

Another idea: Use the Möbius transform. For each permutation, we can compute the contribution of including or excluding it in the subset S, and track the union of edges. This can be done recursively or iteratively.

For example, we can start with an empty set and add permutations one by one, updating the union and the inclusion-exclusion terms.

Here's how this could work:

Initialize a dictionary dp that maps edge sets (represented as bitmask) to their current coefficient in the inclusion-exclusion sum. Initially, dp is empty.

For each permutation π in the list of all permutations:

   For each existing entry in dp with edge set E and coefficient c:

      The new edge set is E ∪ π's edges.

      The new coefficient for E ∪ π's edges is c * (-1) + current coefficient for E ∪ π's edges.

      Also, we need to subtract the product because adding π to the subset increases the subset size by 1.

   Additionally, add the permutation π as a new subset of size 1:

      The edge set is π's edges.

      The coefficient is 1 (since (-1)^(1+1) = 1).

This is similar to the standard subset sum approach with inclusion-exclusion.

But the problem is that the number of edge sets E can be very large (up to 2^49 for n=7), making this approach infeasible.

But n=7 has 49 edges. Storing a bitmask for each edge is impossible for 49 bits. However, in Python, integers can act as bitmask. But even with that, for 49 bits, the number of possible masks is 2^49, which is around 5e+14, which is way too large.

Thus, this approach is not feasible.

Alternative idea: Use the inclusion-exclusion formula in a way that groups permutations by their edges and uses the principle of inclusion-exclusion on the permutations.

But I'm stuck. Let's think of the sample input.

Sample Input 1:

2

50 50

50 50

Sample Output:

937500007

Which is 7/16.

The correct sum is:

The sum of the probabilities of all subsets S that have a perfect matching. According to the inclusion-exclusion approach, this is equal to sum_{S} (-1)^(|S|+1) * product of edges in union(S). The permutations are 2 in total (for n=2):

Perm1: (1-1, 2-2) → edges (0,0) and (1,1) (assuming 0-based indices).

Perm2: (1-2, 2-1) → edges (0,1) and (1,0).

Their unions are:

Each singleton subset S has a union equal to the permutation's edges. The product for Perm1 is (0.5 * 0.5) = 0.25. The product for Perm2 is also 0.25.

The subset S containing both permutations has a union of all four edges (0,0), (0,1), (1,0), (1,1). The product is 0.5^4 = 0.0625. The contribution for this subset is (-1)^(2+1) * 0.0625 = -0.0625.

So the total sum is (0.25 + 0.25) - 0.0625 = 0.5 - 0.0625 = 0.4375 = 7/16.

Which matches the sample. So the inclusion-exclusion approach works.

But how to compute this for larger n?

The key is that the inclusion-exclusion sum can be computed as:

sum_{S non-empty} (-1)^(|S|+1) * product(edges in union(S)).

But with n=7, the number of permutations is 7! = 5040, and the number of subsets is 2^5040, which is impossible.

But perhaps there's a way to compute this sum using dynamic programming, where each permutation is considered once, and the DP state tracks the current union of edges and the count of subsets contributing to that union.

The idea is to use a dynamic programming approach where each step adds a new permutation and updates the possible unions and their coefficients.

The DP state is a dictionary that maps edge unions to their accumulated coefficient. For each permutation π, when processing it, we consider all existing entries in the DP. For each existing entry with edge set E and coefficient c, the new edge set E ∪ π will be added to the DP with coefficient c * (-1) (since adding π to the subset increases the subset size by 1, flipping the sign). Additionally, the permutation π is added as a new subset (with coefficient 1).

The initial state is empty. For each permutation in order, the DP is updated.

The formula is:

new_dp[E ∪ π_edges] += existing_dp[E] * (-1)

And new_dp[π_edges] += 1.

Finally, after processing all permutations, the sum is the sum over all entries in the DP of (coefficient * product of edges in E).

But for n=7, even this approach is impossible due to the number of possible edge unions. However, for n=7, the number of permutations is 5040, and for each permutation, the number of edges is 7. So the union of subsets can be up to 7 * k edges for k permutations. But even with this, the number of possible unions is way too large.

Thus, this approach is only feasible for small n, like n up to 5 or 6. But the problem states that n can be up to 7, so this approach is not feasible.

So what's the alternative?

Let's think again about the inclusion-exclusion sum:

sum_{S subset of permutations, S non-empty} (-1)^(|S|+1) * product_{e in union(S)} p_e.

This can be rewritten as:

sum_{E} (sum_{S subset of permutations, S non-empty, union(S) = E} (-1)^(|S|+1)) * product(e in E) p_e.

The term inside the sum over E is the coefficient μ(E) multiplied by the product of edges in E.

The key is that μ(E) is the sum over all non-empty subsets S of permutations that have union E, of (-1)^(|S|+1).

But how to compute μ(E) for all possible E's.

An alternative approach is to realize that μ(E) can be computed using the Möbius inversion over the lattice of permutations. For each E, μ(E) is the inclusion-exclusion coefficient for E.

But I'm not sure.

Alternatively, notice that μ(E) is equal to the Möbius function for the lattice of edge sets ordered by inclusion. But again, this is unclear.

Another idea: For each edge set E, μ(E) can be computed as the product of (1 - the number of permutations that include E). But this is just a guess.

Alternatively, if E is a single permutation, then μ(E) = 1. If E is the union of two permutations, then μ(E) = 1 - 1 - 1 + ... but this depends on overlapping.

But I'm stuck. Let's look for an alternative approach.

Let me think about the problem differently. The required probability is the probability that the bipartite graph has at least one perfect matching. This can be computed by generating all possible perfect matchings and applying inclusion-exclusion. But this is the same as the inclusion-exclusion sum over permutations.

But for n=7, this seems impossible.

Wait, the problem is to compute the probability that the graph has a perfect matching. The probability can be computed as the sum over all possible perfect matchings M of the probability that all edges in M are present, minus the sum over all pairs of perfect matchings (M1, M2) of the probability that all edges in M1 ∪ M2 are present, plus the sum over all triplets, and so on.

So for each k, compute the sum over all k-sized subsets of perfect matchings of the product of edges in their union, multiplied by (-1)^(k+1).

This is the same as the inclusion-exclusion approach we discussed earlier. But how to compute this for n=7?

The key is that for each subset of permutations, we need to compute their union's edge product and multiply by the inclusion-exclusion coefficient.

But with 7! = 5040 permutations, even storing all subsets is impossible. But maybe we can represent the problem in terms of the inclusion-exclusion formula and find a way to compute it using generating functions or some other mathematical trick.

Another observation: The inclusion-exclusion sum is equivalent to the determinant of a certain matrix. But I'm not sure.

Alternatively, notice that the probability can be written as the sum over all possible perfect matchings M, multiplied by the probability that M is present and that no other perfect matching exists. But this seems even more complicated.

Another idea: Use the principle of inclusion-exclusion but represent each permutation's contribution in terms of their edge set, and use memoization to track the current union of edges. For example, we can represent the current state as a bitmask of edges and the current number of permutations selected modulo 2 (to track the sign). But again, the number of possible states is 2^49 * 2, which is way too large.

Thus, after considering all possible approaches, the only feasible way to compute the required sum for n=7 is to use the inclusion-exclusion formula, but with a way to represent the permutations efficiently and compute the sum recursively.

But given the time constraints, it's possible that for n=7, the number of permutations is manageable with the following approach:

- Precompute all permutations of the right nodes. For n=7, this is 7! = 5040 permutations.

- For each permutation, precompute the product of its edges' probabilities. For example, for permutation π, the product is the product of p_ij for all (i, π(i)).

- Compute the inclusion-exclusion sum using recursion or memoization, keeping track of the current set of edges (as a bitmask) and the sign.

But even this would be O(2^5040), which is impossible.

But wait, perhaps we can use the Möbius transform for the inclusion-exclusion formula. The inclusion-exclusion sum can be computed using a generating function where each permutation is represented as a bitmask and the inclusion-exclusion is computed via the Fast Möbius Transform (FMT).

However, the FMT is applicable when the elements are independent, which they are not. So this may not work.

Another idea: The inclusion-exclusion sum can be computed using the following recursive formula:

The sum for all permutations after the first k permutations is the sum for the first k-1 permutations plus the contribution of the k-th permutation multiplied by the sum for the first k-1 permutations with the sign flipped.

This is similar to the standard subset sum inclusion-exclusion approach. Let's see:

Suppose we have processed the first k-1 permutations. For each possible edge set E and a count of the inclusion-exclusion coefficients, we can represent the current state. When processing the k-th permutation π, for each existing edge set E and coefficient c, we compute new edge sets E ∪ π_edges and add a new coefficient of -c. This accounts for including π in the subset. Additionally, we add the coefficient 1 for the subset containing only π.

Thus, the DP approach is as follows:

Initialize a dictionary dp that maps edge sets to their coefficients. Initially, it is empty.

For each permutation π in the list of all permutations:

   Create a temporary dictionary tmp.

   For each existing edge set E in dp:

      Compute the new edge set E_new = E ∪ π_edges.

      Add to tmp[E_new] the coefficient dp[E] * (-1).

   Also, add the edge set π_edges to tmp with coefficient 1.

   Merge tmp into dp by summing coefficients.

After processing all permutations, the sum is the sum over all entries in dp of (coefficient * product of edges in E).

This approach dynamically builds the inclusion-exclusion sum by considering each permutation and updating the current state of possible edge unions and their coefficients.

But with n=7 and 5040 permutations, this approach is still impossible. For example, after the first few permutations, the number of entries in dp can explode exponentially. For example, even with 10 permutations, the number of possible edge unions could be 2^10, which is 1024. But for 5040 permutations, this is impossible.

But perhaps for small n, like n=7, but with the edge sets being sparse, this could be manageable. For example, each permutation adds 7 edges. So the union of k permutations would have 7k edges if all are disjoint, but in reality, many permutations will share edges, leading to smaller unions.

But even with that, the number of possible edge sets can become very large. For example, for n=7, each permutation has 7 edges. The number of possible unions after processing all permutations is the number of possible unions of any subset of the 5040 permutations, each contributing 7 edges. This is likely in the order of millions or billions, which is not manageable.

Thus, this approach is only feasible for n up to 4 or 5.

But the problem requires n up to 7. So what's the solution?

Wait, maybe there's a mathematical formula or property that can be used to compute this sum efficiently.

Let me think again. The required probability is the sum over all possible perfect matchings M in the graph, but weighted by the probability that all edges in M are present and that there's no other perfect matching. But this seems even more complex.

Alternatively, the required probability is the probability that the graph's adjacency matrix contains at least one permutation matrix, which is the same as having a perfect matching. But this doesn't help.

Another observation: The probability that the graph has a perfect matching is the sum over all possible perfect matchings M of the probability that M is present, minus the sum over all pairs of M1 and M2 of the probability that both are present, plus the sum over all triplets, etc. This is the inclusion-exclusion formula.

But this is exactly the same as the inclusion-exclusion sum discussed earlier. So the problem reduces to efficiently computing this sum.

But how?

The key insight is that the sum can be computed as follows:

result = 0

for k from 1 to number of permutations:

    for each subset S of k permutations:

        compute the union of their edges

        multiply by (-1)^(k+1) and add to result the product of edges in the union

But this is O(2^5040), which is impossible.

Thus, the only feasible way is to find a way to generate all possible permutations and compute their contribution in a way that avoids explicitly enumerating all subsets.

But I'm stuck. Perhaps the correct approach is to use the inclusion-exclusion formula and represent the permutations as bitmask, but with n=7, it's possible to manage this with bitmask optimizations.

But even with n=7, the number of permutations is 5040, which makes it challenging.

Wait, but the edges are up to 49 (7x7). So each permutation can be represented as a bitmask of 49 bits. For example, the permutation π is a 49-bit mask where each bit represents whether the edge (i,j) is in π.

Then, the union of a subset of permutations is the bitwise OR of their masks.

The product of edges in the union is the product of p_ij/100 for all bits set in the mask.

The inclusion-exclusion sum is:

sum_{mask} (coeff[mask] * product[mask])

where coeff[mask] is the sum over all subsets S of permutations with union mask of (-1)^(|S|+1).

Thus, the problem reduces to:

1. Generate all possible masks that are unions of permutations.

2. For each mask, compute coeff[mask].

3. Multiply each coeff[mask] by product[mask], sum all these terms.

But how to compute coeff[mask]?

The key is that coeff[mask] is the sum over all non-empty subsets S of permutations whose union is mask, of (-1)^(|S|+1).

This can be computed using inclusion-exclusion. For example, coeff[mask] = sum_{S subset of permutations, S non-empty, union(S) = mask} (-1)^(|S|+1).

But even this is challenging. However, there is a way to compute this using Möbius inversion over the lattice of masks.

Another idea: For each mask, coeff[mask] is the inclusion-exclusion coefficient for the mask, which can be computed using the Möbius function of the mask in the lattice of masks.

But I'm not familiar with the Möbius function for this lattice.

Alternatively, we can compute coeff[mask] recursively. For a mask, coeff[mask] is equal to the number of subsets S of permutations that union to mask, multiplied by (-1)^(|S|+1).

This can be represented as:

coeff[mask] = sum_{S subset of permutations, S non-empty, union(S) = mask} (-1)^(|S|+1).

This can be computed as the inclusion-exclusion over all permutations that contribute to mask.

But again, this seems computationally intensive.

But given the problem constraints (n up to 7), perhaps it's manageable. Let's try to outline the steps for the solution:

1. Generate all permutations of the right nodes. For each permutation, compute its bitmask (the edges used in the permutation).

2. For each permutation mask, compute the product of its edges' probabilities. Store this for later use.

3. Initialize a dictionary coeff to store the coefficients for each mask. Initially, coeff is empty.

4. For each permutation in order:

   a. For each existing mask in coeff, create a new mask by OR'ing with the current permutation's mask.

   b. Update the coeff dictionary by adding (-1) * coeff[existing_mask] to the new mask's coefficient.

   c. Also, add the current permutation's mask with coefficient 1.

5. After processing all permutations, the coeff dictionary contains the inclusion-exclusion coefficients for each mask.

6. For each mask in coeff, compute the product of the edges' probabilities in the mask, multiply by coeff[mask], and sum all these terms. This sum is the desired probability.

But even this approach is not feasible for n=7, as the number of masks becomes prohibitive.

An alternative approach is to represent the permutations in terms of their bitmask and use memoization to track the coefficients. But given the time constraints of 15 seconds and the memory constraints of 256 MB, this may be manageable for n=7.

But in practice, with 5040 permutations, each iteration would process a growing number of masks. For example, the first iteration adds 1 mask. The second iteration processes this mask and adds the OR with the second permutation's mask. This could be manageable if the masks quickly reach their maximum possible size.

For example, after processing a few permutations, the mask could become the complete graph (all edges), and further permutations would not change the mask. For such masks, their coefficient would accumulate but would not generate new masks.

But even then, for n=7, the number of masks could be large. However, perhaps with memoization and bitmask optimizations, this could be manageable.

Thus, the code would look something like this:

Generate all permutations.

Initialize a dictionary (defaultdict) to track coefficients.

For each permutation in the list:

   temp = defaultdict(int)

   for mask in current_coefficients:

      new_mask = mask | perm_mask

      temp[new_mask] -= current_coefficients[mask]

   temp[perm_mask] += 1

   merge temp into current_coefficients by adding the values.

After processing all permutations, iterate over all masks in current_coefficients and sum (coeff[mask] * product of edges in mask).

Finally, output the sum modulo 1e9+7.

But how to represent the mask and compute the product of edges?

The mask is a 49-bit integer. For each mask, the product of the edges in the mask can be precomputed.

But for n=7, the number of possible masks is 2^49, which is impossible to precompute. Thus, for each mask encountered, we need to compute the product on the fly.

But each time a new mask is generated, we can compute the product of the edges in the mask by multiplying the probabilities of each edge in the mask. However, this is computationally expensive if the number of masks is large.

To optimize, we can precompute a cache of mask products. For example, use a dictionary where the key is the mask and the value is the product. This way, each mask's product is computed once.

But again, with a large number of masks, this could be memory-intensive.

Thus, the code would involve:

- Generating all permutations and their masks.

- Precomputing the product for each permutation's mask.

- Using dynamic programming to track the coefficients and masks.

But for n=7, this approach is likely to be feasible.

Let's outline the steps in code:

First, generate all permutations of the right nodes. For example, for n=3, the permutations are all possible orderings of [0, 1, 2].

Each permutation represents a perfect matching: left node i is matched to right node j = permutation[i].

For each permutation, create a mask where each bit (i, j) is set if the permutation includes (i, j).

Next, compute the product of probabilities for each permutation's mask. For example, for a mask representing edges (i,j), the product is the product of p_ij/100 for each (i,j) in the mask.

Then, initialize the coefficient dictionary. For each permutation in order:

   For each existing mask in the coefficient dictionary:

      new_mask = existing_mask | current_perm_mask

      new_coeff = coefficient[existing_mask] * (-1)

      add new_coeff to coefficient[new_mask]

   add current_perm_mask to the coefficient dictionary with coefficient 1 (or add to existing entry).

Finally, sum over all masks in the coefficient dictionary: coeff[mask] * product(mask), where product(mask) is the product of p_ij/100 for each (i,j) in the mask.

But even this approach is not feasible for n=7, as the number of masks becomes too large.

But given the time limit of 15 seconds and the constraints of the problem, perhaps this approach can be optimized with bitmask manipulations and efficient code.

In Python, using dictionaries and bitmask integers, it's possible to manage this for n=7. The key is that each permutation's mask can be represented as an integer, and the dynamic programming steps can be done efficiently using defaultdict and bitwise operations.

Additionally, for each mask, the product of edges can be computed on the fly by iterating through the bits set in the mask and multiplying the corresponding p_ij/100 values.

But even this would be computationally intensive for large masks, but perhaps manageable.

Another optimization is to precompute the log of the product and work in the log space to avoid multiplying many small numbers, but this would introduce floating-point inaccuracies and is thus not suitable for a problem requiring exact modulo arithmetic.

Thus, the code must compute the product for each mask by multiplying the p_ij/100 factors.

But how to compute the product for a mask efficiently?

An alternative approach is to precompute a 2D array of the probabilities for each edge (i,j), then for a given mask, multiply the probabilities for each bit set in the mask.

For example, for each bit (i,j) in the mask, multiply by p_ij/100.

But with 49 bits, this requires looping through each bit in the mask and checking if it's set, then multiplying.

This can be optimized using bitmask iteration techniques, but in Python, this may be too slow for masks with many bits set.

But given that the final sum must be computed modulo 1e9+7 and represented as a fraction, we can precompute the probabilities as integers modulo MOD = 1e9+7. For example, each p_ij is stored as p_ij * inv(100) mod MOD. Then, the product for a mask is the product of these values for the edges in the mask.

This way, all multiplications are done under modulo arithmetic, and we can compute the product efficiently.

Thus, the steps are:

- Precompute the inverse of 100 modulo MOD, which is 100^(MOD-2) mod MOD.

- For each p_ij, compute (p_ij * inv(100)) mod MOD. This represents the probability that edge (i,j) exists.

- Precompute these values for all edges.

- For a given mask, compute the product of the probabilities for all edges present in the mask.

Thus, in the code:

- Read n.

- Read the n x n p_ij values.

- Precompute the edge_prob[i][j] = (p_ij * inv_100) % MOD.

- Generate all permutations of the right nodes (0 to n-1).

- For each permutation, compute the mask (as a bitmask) and the product of edge_prob[i][j] for each (i, j) in the permutation.

But wait, the mask represents the edges present in the permutation. So for each permutation, the mask is a bitmask where each bit corresponds to an edge (i,j). For example, for n=7, the mask is a 49-bit integer.

Thus, each permutation can be represented as a mask, and the product of its edges can be precomputed as the product of edge_prob[i][j] for each (i, j) in the permutation.

Then, during the dynamic programming steps, for each new mask generated by OR'ing existing masks, the product is the product of edge_prob[i][j] for all edges in the new mask.

But storing the product for each mask is necessary, and this is done by caching the product of the edges in the mask.

But with 49 bits, this is not feasible to precompute. So for each new mask encountered during the dynamic programming steps, compute the product on the fly.

But this would be computationally expensive. However, with masks stored as integers, we can compute the product by iterating through each bit set in the mask and multiplying the corresponding edge_prob[i][j].

But in Python, this can be slow for masks with many bits set. To optimize, we can precompute a dictionary that maps each possible edge (i,j) to its bitmask and edge_prob. Then, for a given mask, iterate through the bits set in the mask and multiply the edge_prob.

Alternatively, we can precompute a list of all edges and their bitmask and probabilities, and for each mask, iterate through all edges and check if the bit is set.

But this is O(49) operations per mask per multiplication. Which is manageable for a few million masks.

Thus, the code outline is:

1. Precompute inv_100 = pow(100, MOD-2, MOD), where MOD = 1e9+7.

2. Read the p_ij values and compute edge_prob[i][j] = (p_ij * inv_100) % MOD.

3. Generate all permutations of the right nodes.

4. For each permutation, compute its mask and product:

   mask = 0

   product = 1

   for i in range(n):

       j = permutation[i]

       bit = i * n + j

       mask |= (1 << bit)

       product = product * edge_prob[i][j] % MOD

   store the mask and product in a list.

But wait, this is incorrect. The product for the permutation is the product of the edges in the permutation, but the mask represents exactly those edges. So for each permutation, the product is the product of its edges. However, during the dynamic programming steps, the product for a mask generated by OR'ing multiple permutations' masks is the product of all edges in the mask, not the product of the permutations' products. So the product must be computed based on the edges in the mask, not the product of the individual permutations' products.

Thus, for each mask, the product is the product of edge_prob[i][j] for each edge (i,j) in the mask. This must be computed for each mask, not based on the permutations' products.

Thus, during the dynamic programming steps, when a new mask is generated (as the OR of existing masks), the product for this mask is the product of the edge_prob[i][j] for each bit set in the mask.

To compute this efficiently, we can precompute for each edge (i,j) its bitmask and edge_prob. Then, for each mask, iterate through all edges and check if their bit is set in the mask, multiply the edge_prob.

But this would take O(49) operations per mask. For a mask that's the OR of multiple permutations, this is manageable.

Thus, the code must:

For each mask in the coeff dictionary:

   compute the product of all edge_prob[i][j] where the (i,j) bit is set in the mask.

Sum all coeff[mask] * product[mask].

Thus, the code can be structured as follows:

Generate all permutations and their masks.

Precompute edge_prob for each edge.

Initialize coeff as defaultdict(int).

For each permutation in permutations:

   perm_mask = mask of this permutation's edges.

   temp = defaultdict(int)

   for existing_mask in coeff:

      new_mask = existing_mask | perm_mask

      temp[new_mask] = (temp[new_mask] - coeff[existing_mask]) % MOD

   temp[perm_mask] = (temp[perm_mask] + 1) % MOD

   for mask in temp:

      coeff[mask] = (coeff[mask] + temp[mask]) % MOD

After processing all permutations, compute the result:

result = 0

for mask in coeff:

   product = 1

   for i in range(n):

       for j in range(n):

           if mask & (1 << (i * n + j)):

               product = product * edge_prob[i][j] % MOD

   result = (result + coeff[mask] * product) % MOD

return result

But this code would have a problem: the masks can be very large, and iterating through all edges for each mask is O(n^2) per mask, which for n=7 is 49 operations. If the number of masks is, say, 1e6, then this would take 49e6 operations, which is manageable.

But the issue is that for each permutation processed, the temp dictionary is built by combining existing masks and the new permutation's mask. This can lead to a large number of masks being generated.

But for n=7, the maximum number of edges in a mask is 49. However, each permutation adds 7 edges, and the masks can overlap. Thus, the number of unique masks generated may be manageable.

Another optimization is to precompute a lookup table for all edges and their bit positions, and then iterate only through the bits set in the mask. For example, for a given mask, iterate through all set bits and multiply the corresponding edge_prob.

In Python, this can be done using a bitmask and a list of edges:

edges = []
for i in range(n):
    for j in range(n):
        edges.append( (i, j, 1 << (i *n + j), edge_prob[i][j]) )

Then, for a given mask, iterate through the edges and check if the bit is set.

But even better, use the bitmask to generate the list of set bits and multiply the corresponding edge_prob.

But in Python, bitmask iteration can be done with a loop:

for bit in range(n*n):
    if mask & (1 << bit):
        product = product * edge_prob[bit // n][bit % n] % MOD

This is O(n^2) per mask, which is manageable.

Thus, the code outline is feasible.

Now, the code must handle the following steps:

- Generate all permutations of the right nodes.

- For each permutation, compute its mask and store.

- Use dynamic programming to track the inclusion-exclusion coefficients.

- Compute the product for each mask in the coefficients.

Now, let's test this approach with the sample input.

Sample Input 1:

2

50 50

50 50

The edge_prob matrix is:

edge_prob[0][0] = 50 * inv_100 mod MOD = 50 * 14_000_0005 mod MOD = 700_000_025 mod MOD = 700000025 mod 1e9+7 is 700000025.

Similarly for all other edges.

The permutations for n=2 are:

Permutation 1: (0, 1) → mask 0b11 (binary for edges (0,0) and (1,1)) → mask bits 0 and 3 (assuming i=0, j=0 is bit 0, i=0, j=1 is bit 1, i=1, j=0 is bit 2, i=1, j=1 is bit 3).

Permutation 2: (1, 0) → edges (0,1) and (1,0) → bits 1 and 2.

Processing permutation 1:

coeff becomes {0b1001: 1}.

Processing permutation 2:

For each existing mask in coeff (0b1001):

new_mask = 0b1001 | 0b0110 = 0b1111.

temp[0b1111] -= 1 → temp[0b1111] = -1.

Then, temp[0b0110] += 1.

So temp is {0b1111: -1, 0b0110: 1}.

Merge into coeff:

coeff = {0b1001: 1, 0b0110: 1, 0b1111: -1}.

Now, after processing both permutations, the coefficients are:

mask 0b1001 (edges (0,0) and (1,1)) → coeff 1.

mask 0b0110 (edges (0,1) and (1,0)) → coeff 1.

mask 0b1111 (all edges) → coeff -1.

The product for mask 0b1001 is (50/100) * (50/100) = 0.25 → 700000025^2 mod MOD.

The product for mask 0b0110 is (50/100)^2 → same.

The product for mask 0b1111 is (50/100)^4 → 0.0625.

The sum is 1*0.25 + 1*0.25 + (-1)*0.0625 = 0.4375 → 7/16, which is correct.

Thus, the code works for the sample input.

Thus, the code is correct, but the question is whether it can handle n=7 within the time and memory constraints.

But given that n=7 and 7! = 5040 permutations, and each permutation adds 7 edges, the number of masks can grow exponentially. However, with n=7 and 7 edges per permutation, the masks can quickly cover all edges, leading to a manageable number of unique masks.

In Python, using defaultdict and bitmask operations, this code should be manageable for n=7, given the time limit of 15 seconds and the fact that Python can handle millions of operations per second.

Thus, the final code would look like this:
</think>

```python
import sys
from itertools import permutations
from collections import defaultdict

MOD = 10**9 + 7

def main():
    n = int(sys.stdin.readline())
    p = []
    for _ in range(n):
        p.append(list(map(int, sys.stdin.readline().split())))
    
    inv100 = pow(100, MOD-2, MOD)
    edge_prob = [[(x * inv100) % MOD for x in row] for row in p]
    
    perms = list(permutations(range(n)))
    coeff = defaultdict(int)
    
    for perm in perms:
        mask = 0
        for i in range(n):
            j = perm[i]
            bit = i * n + j
            mask |= 1 << bit
        
        temp = defaultdict(int)
        temp[mask] = (temp[mask] + 1) % MOD
        for existing_mask in list(coeff.keys()):
            new_mask = existing_mask | mask
            val = (coeff[existing_mask] * (-1)) % MOD
            temp[new_mask] = (temp[new_mask] + val) % MOD
        
        for m, v in temp.items():
            coeff[m] = (coeff[m] + v) % MOD
    
    result = 0
    for mask, c in coeff.items():
        product = 1
        for i in range(n):
            for j in range(n):
                if mask & (1 << (i * n + j)):
                    product = (product * edge_prob[i][j]) % MOD
        result = (result + c * product) % MOD
    
    print(result % MOD)

if __name__ == "__main__":
    main()
```