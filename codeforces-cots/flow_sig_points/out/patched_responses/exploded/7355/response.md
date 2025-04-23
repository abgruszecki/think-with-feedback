<think>
Okay, let's tackle this problem step by step. The goal is to find the number of binary relations on a set of size n that are symmetric and transitive but not reflexive. And then return that number modulo 1e9+7.

First, I need to understand what's required here. Let's break down the conditions:

The relations must be symmetric and transitive. But they must not be reflexive. So, the key is that there's at least one element a where (a,a) is not in the relation.

But wait, Johnny's mistake was thinking that symmetry and transitivity imply reflexivity. But that's not the case. So, our task is to count all such relations that are symmetric and transitive but miss at least one (a,a) pair.

So, the approach would be to first calculate all symmetric and transitive relations, then subtract those that are reflexive (i.e., equivalence relations) to get the answer.

Wait, no. Because equivalence relations require all three properties: reflexive, symmetric, and transitive. So, the equivalence relations are exactly those that are reflexive, symmetric, and transitive. So, the problem wants the count of relations that are symmetric and transitive, but not reflexive. So, the answer is (number of symmetric and transitive relations) minus (number of equivalence relations).

But how many symmetric and transitive relations are there? And how many equivalence relations?

Alternatively, maybe there's a better way to model this.

Let's think about the structure of a symmetric and transitive relation.

If a relation is symmetric and transitive, then it's not necessarily reflexive. However, if (a,b) is in the relation, then (b,a) is also present (symmetry), and (a,a) and (b,b) must be present? Wait, no. Let me think.

Suppose we have (a,b) in the relation. By symmetry, (b,a) is also present. Then, by transitivity, since (a,b) and (b,a) are present, (a,a) must be present. Similarly, (b,b) must be present.

So, if a relation is symmetric and transitive, then for any elements a and b, if (a,b) is in the relation, then a and b must form a "clique" where all pairs (a,a), (a,b), (b,a), (b,b) are present. Wait, maybe not exactly. Let's see:

If (a,b) is present, then (b,a) is present (symmetry). Then, applying transitivity to (a,b) and (b,a), we get (a,a) must be present. Similarly, applying transitivity to (b,a) and (a,b) gives (b,b) must be present. So, any two elements in the same component must have their reflexive pairs. But if two elements are not connected, then their pairs aren't required.

Wait, this suggests that a symmetric and transitive relation is composed of equivalence classes where each class is a set of elements that are all connected via the relation. However, each equivalence class must be a clique (since any two elements in the class must have all possible pairs). But wait, in an equivalence relation, the equivalence classes are determined by the reflexive, symmetric, and transitive closure. But here, since the relation is symmetric and transitive, but not reflexive, the structure is a bit different.

Wait, maybe the symmetric and transitive relations can be represented as a partition of the set into some equivalence-like classes, but with the caveat that elements in the same class have all their pairs included. But wait, for such a relation, each equivalence class is a subset S where for any a and b in S, (a,b) is in the relation. Because if a and b are in S, then (a,b) is present, which requires (b,a) to be present, and then (a,a) and (b,b) must be present as well. Wait, no. Let's think again.

If a relation is symmetric and transitive, then for any a and b in the relation, (a,a) must be present. So, if you have any pair (a,b) in the relation, then both (a,a) and (b,b) must be present. But if you have a pair (a,c), then (a,a) and (c,c) must be present, etc.

So, the elements can be partitioned into groups where each group is a set of elements that are all connected via the relation. Each such group must form a clique (all possible pairs are present) and also include all reflexive pairs. However, elements not in any group (i.e., elements that are not related to anyone else, including themselves) do not have any pairs.

Wait, but for an element x that is not part of any group, (x,x) is not in the relation, and also x is not related to any other element. Because if x was related to itself, then (x,x) is in the relation, which would require that x is in a group (since the relation is symmetric and transitive).

So, the structure of a symmetric and transitive relation is as follows:

The elements are divided into two parts:

1. A collection of disjoint subsets S_1, S_2, ..., S_k, where each S_i is a non-empty subset. For each S_i, all pairs (a,b) where a and b are in S_i must be in the relation. Because if a and b are in S_i, then (a,b) is present (so (b,a) is present due to symmetry). Also, because the relation is transitive, any pairs (a,c) where a and c are in S_i are present. So, each S_i forms a clique.

2. The remaining elements (those not in any S_i) are singletons. For these elements x, (x,x) is not present in the relation, and x is not related to any other element.

So, the symmetric and transitive relations can be modeled by choosing a subset of elements to form cliques (each clique must have at least one element, and any two elements in the same clique are related), and the rest of the elements are not in any clique and have no relations.

But the key point is that any element in a clique must have (x,x) in the relation, but elements not in any clique do not have (x,x) in the relation.

Therefore, the total number of symmetric and transitive relations is equal to the number of ways to partition the set into any number of cliques (including none) and singletons (elements not in any clique). Wait, no. Because the cliques themselves can be any subsets. Wait, perhaps the correct way to model this is that each symmetric and transitive relation is equivalent to a collection of disjoint cliques (each clique can be any non-empty subset), and the elements not in any clique are singletons.

Wait, no. Because, for example, if two cliques are connected via a pair (a,b) where a is in one clique and b in another, then transitivity would require that all elements in both cliques are connected. So, the cliques must be mutually exclusive and exhaustive. So, the relation is formed by a partition of the set into some cliques (each clique being a subset), and the elements not in any clique are those that are not part of any clique and have no relations.

Wait, perhaps the cliques must form a partition of some subset of the elements, and the remaining elements are singletons. But how?

Alternatively, think of the relation as a graph where each node is an element. The edges are the pairs (a,b) in the relation. Since the relation is symmetric and transitive, the connected components of this graph must form cliques, and each node in a connected component has a self-loop (because (a,a) must be present if there's any edge in the component). But if a node is in a component (connected via edges), then all edges between nodes in the component must be present. So, the relation's graph is a collection of cliques (each being a connected component with all possible edges) and isolated nodes (nodes with no edges, including no self-loop).

So, the symmetric and transitive relations correspond to partitions of the set into some cliques (each clique is a subset of elements, all pairwise related) and the remaining elements are isolated (not part of any clique, no edges). The isolated elements have no edges, so (x,x) is not present.

Thus, to count the number of symmetric and transitive relations, we can model it as follows:

For each subset S of the elements, the elements in S form a collection of disjoint cliques (each clique is a non-empty subset), and the elements not in S are isolated. Wait, no. Because S would be the union of the cliques. So, the elements not in S are the isolated ones.

Wait, no. Because the cliques form a partition of a subset of the elements. So, the elements not in any clique are the isolated ones.

Thus, the problem reduces to choosing a subset of elements to form cliques (partitioned into one or more cliques) and the remaining elements are isolated. The total number of such possible configurations is the number of symmetric and transitive relations.

So, how do we model this combinatorially?

Each symmetric and transitive relation is determined by a partition of a subset of the elements into cliques. The remaining elements (those not in the subset) are isolated.

So, the number of such relations is the sum over all subsets S of the elements, where for each S, we count the number of ways to partition S into non-empty, mutually disjoint subsets (the cliques). The sum over all possible S of the Bell numbers of |S| multiplied by 2^(number of elements not in S choose 2) ??? Wait, perhaps not.

Wait, the cliques are the connected components in the graph. So for each element in S, it is part of exactly one clique. The elements not in S are isolated. So for the entire set, the process is:

Choose a subset S of elements. Then partition S into non-empty subsets (cliques). The elements not in S are isolated. So, the number of ways is equal to the sum over all possible S of B(|S|), where B(k) is the k-th Bell number (the number of ways to partition a k-element set into non-empty subsets). Because for each subset S, the number of ways to partition it into cliques is the Bell number B(|S|), and the elements not in S are isolated.

But wait, no. Because each element in S is part of a clique (so their cliques form a partition of S). The elements not in S are isolated. So the total number of symmetric and transitive relations is the sum_{k=0}^n [ C(n,k) * B(k) }, where B(k) is the Bell number for k elements.

Yes! Because for each k from 0 to n, we choose a subset of size k (there are C(n,k) ways), then partition that subset into cliques (B(k) ways). The remaining (n -k) elements are isolated, contributing nothing else to the structure.

So the total number of symmetric and transitive relations is sum_{k=0}^n (n choose k) * B(k).

But wait, the Bell numbers count the number of ways to partition a set into any number of non-empty subsets, which is exactly what we need here. So the sum over all possible subsets S (of any size) of the product of the number of ways to choose S (C(n, k) for size k) and the number of ways to partition S into cliques (B(k)).

So, the total symmetric and transitive relations is sum_{k=0}^n C(n, k) * B(k). Because for each possible size k of the subset S, we can choose S in C(n, k) ways, and then partition S into cliques (B(k) ways). The remaining elements are isolated.

So, that's the total number of symmetric and transitive relations.

Now, from this number, we need to subtract the number of equivalence relations (since those are the ones that are reflexive). Because an equivalence relation is a symmetric, transitive, and reflexive relation. So, an equivalence relation must include all (a,a) pairs. Which implies that in our model, all elements must be part of some clique. Because if an element is isolated, then (a,a) is not in the relation, which would make the relation not reflexive.

So, equivalence relations correspond to the case where S is the entire set (so all elements are part of some clique). The number of equivalence relations is exactly B(n), since each equivalence relation is a partition of the entire set into equivalence classes. Which is exactly what the Bell number B(n) represents.

So, the answer to the problem is:

Answer = (sum_{k=0}^n C(n,k) * B(k)) ) - B(n)

But we need to compute this modulo 1e9+7.

So, the problem reduces to:

Compute (sum_{k=0}^n C(n,k) * B(k)) - B(n) modulo 1e9+7.

Simplifying, this is sum_{k=0}^n C(n,k) * B(k) - B(n) = sum_{k=0}^{n-1} C(n,k) * B(k) + C(n,n)*B(n) - B(n) = sum_{k=0}^{n-1} C(n,k) * B(k) + B(n) - B(n) = sum_{k=0}^{n-1} C(n,k) * B(k).

So, the answer is sum_{k=0}^{n-1} C(n,k) * B(k).

But perhaps the first expression is easier to compute.

Now, the next step is to compute Bell numbers up to n, and combinations C(n, k) for all k, then compute the sum.

But given that n can be up to 4000, this requires efficient computation of Bell numbers up to 4000 and combinations.

First, let's think about how to compute Bell numbers. The Bell number B(n) is the sum of the Stirling numbers of the second kind for k from 0 to n. Or, more efficiently, Bell numbers can be computed using the recurrence:

B(n+1) = sum_{k=0}^n C(n, k) * B(k)

with B(0) = 1.

Wait, yes. The Bell numbers can be computed using the following recurrence:

B(0) = 1
B(n+1) = sum_{k=0}^n C(n, k) * B(k)

This is because to compute B(n+1), you consider the element (n+1)th and choose a subset of k elements from the first n elements to form a new partition block with (n+1)th element. For each subset of size k, the remaining elements can be partitioned in B(n -k) ways. Summing over k gives the formula. But perhaps a better way is to note that the recurrence is:

B(n+1) = sum_{k=0}^n C(n, k) * B(k)

So, to compute Bell numbers up to 4000, we can use this recurrence.

But for n up to 4000, and for each step up to 4000, this would be O(n^2) operations. Which is acceptable for n=4000 as 4000^2 is 16 million operations.

So, the plan is:

1. Precompute Bell numbers up to 4000 using the recurrence.

2. Precompute combinations C(n, k) for all k from 0 to n. However, for each n given as input, we need to compute C(n, k) for all k. Since the input is up to 4000, and n can be 4000, this can be done using dynamic programming or using a combinatorial formula.

Wait, but in the problem statement, the input is a single n. So, for each test case, given n, compute the sum over k=0 to n of C(n, k) * B(k) minus B(n).

But wait, the sum sum_{k=0}^n C(n,k) * B(k) is exactly the Bell number B(n+1), according to the recurrence. Because according to the recurrence, B(n+1) = sum_{k=0}^n C(n, k) * B(k).

Wait, yes! Because according to the recurrence:

B(n+1) = sum_{k=0}^n C(n, k) * B(k)

So, the sum sum_{k=0}^n C(n, k) * B(k) is equal to B(n+1).

So, then the answer is B(n+1) - B(n).

Wait, because the sum_{k=0}^n C(n, k) * B(k) = B(n+1). Then, the answer is B(n+1) - B(n).

Wow, that's a crucial insight. That simplifies the problem a lot. Because the answer becomes B(n+1) - B(n).

So, the answer is Bell(n+1) - Bell(n).

Let me verify this with the examples.

First example:

n=1.

Then, answer is B(2) - B(1).

Compute B(0) =1.

B(1) = sum_{k=0}^0 C(0,0)*B(0) = C(0,0)*1 =1. So B(1)=1.

B(2) = sum_{k=0}^1 C(1,k)*B(k) = C(1,0)*B(0) + C(1,1)*B(1) = 1*1 +1*1=2.

So, answer is 2-1=1. Which matches the first example.

Second example: n=2.

B(3) - B(2).

B(0)=1, B(1)=1, B(2)=2, B(3)= sum_{k=0}^2 C(2,k)*B(k) = C(2,0)*B(0) + C(2,1)*B(1) + C(2,2)*B(2) = 1*1 + 2*1 +1*2=1+2+2=5. So answer is 5-2=3. Which matches the second example.

Third example: n=3.

Answer is B(4) - B(3).

Compute B(4) = sum_{k=0}^3 C(3,k) B(k).

C(3,0) B(0) =1*1=1.

C(3,1) B(1) =3*1=3.

C(3,2) B(2)=3*2=6.

C(3,3) B(3)=1*5=5.

Total sum is 1+3+6+5=15. So B(4) is 15. B(3)=5. So answer is 15-5=10. Which matches the third example.

So, this formula holds. Therefore, the answer is Bell(n+1) - Bell(n).

Therefore, the problem reduces to computing Bell(n+1) - Bell(n) modulo 1e9+7.

Now, the task is to compute Bell numbers up to n+1=4001 (since n can be up to 4000).

So, the plan is:

1. Precompute Bell numbers up to 4001.

2. For a given n, compute (Bell(n+1) - Bell(n)) mod 1e9+7.

So, the key is to compute the Bell numbers efficiently.

The recurrence for Bell numbers is B(0) = 1, and for m >=0, B(m+1) = sum_{k=0}^m C(m, k) * B(k).

But how do we compute this sum efficiently?

Calculating C(m, k) for each m and k up to 4000.

But wait, for each m, when calculating B(m+1), we need the sum over k=0 to m of C(m, k) * B(k).

C(m, k) is the number of ways to choose k elements from m elements, which is m choose k.

But m can be up to 4000. So, for m up to 4000, and k up to m, this can be precomputed.

Alternatively, for each m, compute the sum as follows.

But calculating C(m, k) for each m and k can be done using a dynamic programming approach, building a Pascal's triangle. However, for m up to 4000, storing a 4001 x 4001 array for combinations mod 1e9+7 is feasible.

So, steps:

- Precompute a 2D array comb where comb[m][k] is C(m, k) mod MOD.

But m can be up to 4000. So, the maximum comb is 4000 choose 2000, which is manageable as a 4001 x 4001 array.

But in Python, for space, 4001 x 4001 is 16 million integers. Which is acceptable.

So, first precompute combinations mod MOD.

Then, using the recurrence B(m+1) = sum_{k=0}^m comb[m][k] * B[k], compute the Bell numbers.

Yes.

So, the code steps:

1. Precompute combinations C(n, k) mod MOD for all n up to 4000, and k up to n.

But wait, for B(m+1), the sum uses C(m, k) for m up to 4000. So, the maximum m is 4000. So, the combinations needed are for m from 0 to 4000, and k from 0 to m.

So, precompute comb up to (4000, 4000).

How to compute comb:

We can compute comb using Pascal's identity:

comb[n][k] = comb[n-1][k-1] + comb[n-1][k], with comb[n][0] = 1 and comb[n][n] = 1.

Initialize a 2D array comb where comb[n][k] is computed.

But for n up to 4000, this is manageable.

Once comb is precomputed, then compute Bell numbers.

Initialize Bell array of size 4001+1.

Bell[0] = 1.

For m from 0 to 4000:

Bell[m+1] = sum_{k=0}^m comb[m][k] * Bell[k], all mod MOD.

So, this way, we can compute Bell[0] to Bell[4001].

Then, for input n, the answer is (Bell[n+1] - Bell[n]) % MOD.

Now, let's verify for n=1:

Bell[2] - Bell[1] = 2-1=1.

Yes.

For n=2:

Bell[3] - Bell[2] =5-2=3.

Yes.

So, this approach works.

Now, the code.

First, precompute combinations mod MOD.

But for n up to 4000, we can compute comb using dynamic programming.

In Python, for speed, it's better to precompute a 2D list of comb.

But in Python, even with 4001x4001 elements, it's manageable. Each element is an integer mod 1e9+7.

Let's code this.

MOD = 10**9 +7

n_max = 4000

# Precompute comb up to 4000.

comb = [[0]*(n_max+1) for _ in range(n_max+1)]

for n in range(n_max+1):
    comb[n][0] = 1
    comb[n][n] = 1
    for k in range(1, n):
        comb[n][k] = (comb[n-1][k-1] + comb[n-1][k]) % MOD

Then, compute Bell numbers up to 4001.

Bell = [0]*(n_max +2)
Bell[0] =1

for m in range(0, n_max +1):
    # Compute Bell[m+1] = sum_{k=0}^m comb[m][k] * Bell[k] mod MOD
    s =0
    for k in range(0, m+1):
        s = (s + comb[m][k] * Bell[k]) % MOD
    if m+1 <= n_max+1:
        Bell[m+1] = s

Wait, but m ranges up to 4000. Because Bell has to be computed up to 4001 (since for n=4000, we need Bell[4001]).

So, the loop for m in 0 to 4000.

Each step m, compute Bell[m+1].

Yes.

Once Bell is computed, the answer for input n is (Bell[n+1] - Bell[n]) % MOD.

But in Python, subtraction modulo MOD can be handled as (a - b) % MOD.

So, now, putting it all together.

But wait, for n=4000, the code needs to compute comb[4000][k] for all k up to 4000. Which is feasible.

But in practice, in Python, precomputing the combination table for 4000 x 4000 can take some time, but should be manageable.

But for n up to 4000, the code will take O(n^2) time for combinations, which for n=4000 is 16 million steps, which is acceptable.

Then, computing Bell numbers up to 4001 is also O(n^2), which for 4000 steps (each step requiring m+1 terms) is 4001 * 4001 ~16 million steps. Which is manageable.

So, the code can be written as follows.

But wait, the input is a single n, so for each test case, precomputing everything up front is feasible. But since the code is for a single test case, but n can be up to 4000, the precomputing is done once, and then the answer is computed.

But for code submission, the code must read the input n, compute the answer, and output it.

So, the steps are:

1. Read n.

2. Precompute comb up to 4000.

3. Precompute Bell up to 4001.

4. Compute (Bell[n+1] - Bell[n]) mod MOD.

But precomputing comb and Bell for each input would be time-consuming. However, since the constraints allow up to 1.5 seconds, and for n=4000, the code would need to handle that.

But in Python, precomputing the comb and Bell for n=4000 is manageable.

Let's see.

The code:

MOD = 10**9 +7

n = int(input())

max_bell = n +1

# Precompute combinations up to (max_bell-1) choose k, since for Bell(max_bell), the maximum m is max_bell-1.

max_m = max_bell -1

# Compute comb up to max_m.

comb = [[0]*(max_m +1) for _ in range(max_m +1)]

for m in range(max_m +1):
    comb[m][0] = 1
    if m >=1:
        comb[m][m] =1
    for k in range(1, m):
        comb[m][k] = (comb[m-1][k-1] + comb[m-1][k]) % MOD

# Now compute Bell numbers up to max_bell.

Bell = [0]*(max_bell +1)
Bell[0] =1

for m in range(0, max_bell):
    # Compute Bell[m+1]
    s =0
    for k in range(0, m+1):
        if k > m:
            c =0
        else:
            c = comb[m][k]
        s = (s + c * Bell[k]) % MOD
    Bell[m+1] = s

ans = (Bell[n+1] - Bell[n]) % MOD
print(ans)

Wait, but when m is up to max_bell-1. Let's see.

max_bell is n+1.

We need to compute Bell[0] to Bell[n+1].

So, the loop for m in 0 to (n+1-1) =n.

But in code:

for m in range(0, max_bell):

max_bell is n+1. So the loop runs m from 0 to (n+1-1) =n.

Which is correct.

But let's test for n=1.

max_bell =2.

So m runs from 0 to 1 (since max_bell is 2, range(0, max_bell) is 0,1).

For m=0:

Bell[1] = sum_{k=0}^0 comb[0][0] * Bell[0} =1*1=1.

For m=1:

sum_{k=0}^1 comb[1][k] * Bell[k}.

comb[1][0] =1, comb[1][1}=1.

So sum is 1*1 (k=0) +1*1 (k=1) =2 → Bell[2] =2.

So, correct.

But the code may need to precompute comb up to m=1.

Yes, because for m=1, comb is needed up to m=1.

But the code's max_m is max_bell-1 = (n+1) -1 =n.

So, when n=4000, max_m is 4000.

So, the comb is precomputed up to 4000, which is correct.

Yes.

But in the code above, when m is up to max_m (which is 4000 for n=4000), then for m=4000, the code computes Bell[4001], which is needed.

So, the code is correct.

Now, let's check the memory. For n=4000, the comb array is (4001 x 4001) integers, which is 16 million integers. Each integer is 4 bytes (in CPython, but in Python, integers can take more memory). However, 16 million integers in Python may take up a lot of memory, but given the 256 MB limit, perhaps it's manageable. Alternatively, perhaps there's a way to optimize.

But for Python, using a list of lists for comb may be memory-intensive. So, perhaps, using a 1D array and updating it in place.

Alternatively, since in the Bell recurrence, for each m, when calculating Bell[m+1], we need comb[m][k] for k up to m. So, perhaps compute comb on the fly for each m.

Wait, but that would not save time, as we need to compute comb for all m up to 4000.

Alternatively, perhaps we can compute the combination C(m, k) as the binomial coefficient, but for m up to 4000 and k up to m, but this would require a different approach.

Alternatively, note that the recurrence for Bell numbers can be rewritten using the formula:

Bell[m+1] = sum_{k=0}^m C(m, k) * Bell[k]

Which can be rewritten as sum_{k=0}^m (m choose k) * Bell[k}.

But perhaps using generating functions or other methods to compute this sum.

But for the time being, the initial approach is correct, but the problem is that for n=4000, the comb array requires 4001 x 4001 entries. Which in Python would be 4001 lists, each of size 4001. Each entry is a 4-byte integer (but in Python, integers are objects and take more memory). However, 4001 *4001 is ~16 million entries. Even if each takes 8 bytes, it's 128MB, which is under the memory limit (256MB). So it's manageable.

But let's check the code with the sample inputs.

Sample input 1:

n=1.

max_bell=2.

precompute comb up to m=1.

comb[0][0] =1.

comb[1][0] =1, comb[1][1]=1.

Then, compute Bell[0] =1.

m=0:

compute Bell[1] = sum_{k=0}^0 comb[0][0] * Bell[0} =1 → Bell[1]=1.

m=1:

compute Bell[2} = sum_{k=0}^1 comb[1][k} * Bell[k}.

comb[1][0}=1 → 1*1=1.

comb[1][1}=1 → 1*1=1.

Sum is 2 → Bell[2}=2.

answer is (2-1) mod MOD =1. Correct.

Sample input 2: n=2.

max_bell=3.

precompute comb up to m=2.

comb[2][0} =1, comb[2][1}=2, comb[2][2}=1.

Bell[3} is computed as sum_{k=0}^2 comb[2][k} * Bell[k}.

Bell[0}=1, Bell[1}=1, Bell[2}=2.

sum = comb[2][0} *1 + comb[2][1} *1 + comb[2][2} *2 → 1*1 + 2*1 +1*2 =1+2+2=5.

So Bell[3}=5.

answer is 5-2=3.

Yes.

So code works.

But the problem is that for n=4000, precomputing the comb array may take a lot of time and memory.

Alternative approach: compute the combinations C(m, k) on the fly using a formula.

But for each m and k, C(m, k) can be computed as factorial(m) / ( factorial(k) * factorial(m-k) ) mod MOD.

But factorials up to 4000 are needed.

Precomputing factorials and inverse factorials mod MOD is another approach.

Let me think:

Compute fact = [1]*(max_m +1)

fact[i] = i! mod MOD.

Compute inv_fact = [1]*(max_m +1)

inv_fact[i] = inverse(fact[i]) mod MOD.

Once these are precomputed, then C(m, k) can be computed as fact[m] * inv_fact[k] * inv_fact[m-k] mod MOD.

This would allow us to compute C(m, k) on the fly for any m and k.

But this approach requires precomputing factorials and inverse factorials up to 4000.

This is more memory-efficient as it uses two arrays of size 4001 each, instead of a 4001x4001 matrix.

Let's see:

For precomputing factorials:

fact[0] =1.

for i in 1 to 4000:

fact[i] = fact[i-1] * i % MOD.

Inverse factorials:

inv_fact[4000] = pow(fact[4000], MOD-2, MOD)

for i in 3999 down to 0:

inv_fact[i] = inv_fact[i+1] * (i+1) % MOD.

Once this is done, C(m, k) can be computed as:

if k <0 or k>m: 0

else: (fact[m] * inv_fact[k] % MOD) * inv_fact[m -k] % MOD.

So, this approach uses O(n) memory for factorials and inverse factorials, and O(1) per C(m, k) query.

Thus, for each m in 0..4000, and k in 0..m, we can compute C(m, k) on the fly.

This would save memory, which is important for n=4000.

So, modifying the code to use this approach.

Steps:

1. Precompute fact and inv_fact up to 4000.

2. For each m in 0 to (n+1-1) =n:

   compute Bell[m+1] as sum_{k=0}^m C(m, k)*Bell[k} mod MOD.

But to compute C(m, k), use the formula.

This would eliminate the need for the comb array, saving memory.

This is better for Python, which has memory constraints for large 2D arrays.

So, the code would be:

MOD = 10**9 +7

n = int(input())

max_m = n  # since m ranges up to (n) for Bell(n+1)

# Precompute factorial and inverse factorial up to max_m.

fact = [1]*(max_m +1)
for i in range(1, max_m+1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1]*(max_m +1)
inv_fact[max_m] = pow(fact[max_m], MOD-2, MOD)
for i in range(max_m-1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(m, k):
    if k <0 or k >m:
        return 0
    return fact[m] * inv_fact[k] % MOD * inv_fact[m -k] % MOD

# Compute Bell numbers up to Bell(n+1)

max_bell = n+1

Bell = [0]*(max_bell +1)
Bell[0] =1

for m in range(0, max_bell):
    # Compute Bell[m+1] = sum_{k=0}^m comb(m, k)*Bell[k]
    s=0
    for k in range(0, m+1):
        c = comb(m, k)
        s = (s + c * Bell[k]) % MOD
    Bell[m+1] = s

ans = (Bell[n+1] - Bell[n]) % MOD
print(ans)

This approach uses O(max_m) memory for factorials and inverse factorials, which is 4000+1 elements for n=4000.

The code for each Bell number is O(m) time per m. So for m up to 4000, it's O(n^2) time.

But for Python, this should be manageable.

Let's test this code for the samples.

Sample 1: n=1.

max_m =1.

precompute fact up to 1:

fact[0] =1, fact[1]=1.

inv_fact[1] =1^-1 mod MOD =1.

Then, for m=0, Bell[1} = comb(0,0)*Bell[0} =1*1=1.

For m=1, compute Bell[2} = sum_{k=0}^1 comb(1, k)*Bell[k}.

comb(1,0) =1 *1 * inv_fact[1} → wait, wait, let's see:

fact[1] =1, inv_fact[0} is computed as follows:

inv_fact[1] =1.

Then, inv_fact[0} = inv_fact[1} *1 mod MOD → 1 *1 =1.

So, comb(1,0) = fact[1] * inv_fact[0} * inv_fact[1-0} → fact[1}=1, inv_fact[0}=1, inv_fact[1}=1. So 1*1*1 =1.

comb(1,1) = fact[1} * inv_fact[1} * inv_fact[0} → 1*1*1=1.

So sum is 1*1 (k=0) +1*1 (k=1) → sum=2. So Bell[2}=2.

answer is 2-1=1.

Sample 2: n=2.

max_m=2.

fact[2} =2.

inv_fact[2} = 2^{-1} mod MOD. Since MOD is 1e9+7, which is a prime, inv(2) is 500000004.

But for Bell[3}, when m=2, we compute sum_{k=0}^2 comb(2, k)*Bell[k}.

comb(2,0} is 1.

comb(2,1}=2.

comb(2,2} =1.

Bell[0}=1, Bell[1}=1, Bell[2}=2.

sum is 1*1 + 2*1 +1*2 → 1+2+2=5. So Bell[3}=5.

answer is5-2=3.

Yes.

So this approach works.

The key is that using factorials and inverse factorials allows us to compute combinations on the fly, avoiding the 2D array, which saves memory.

This code should work for n up to 4000.

Thus, the final code is as follows.
</think>

```python
MOD = 10**9 + 7

n = int(input())

if n == 0:
    print(0)
    exit()

max_m = n  # Bell(n+1) requires combinations up to C(n, k)

# Precompute factorial and inverse factorial up to max_m
fact = [1] * (max_m + 1)
for i in range(1, max_m + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_m + 1)
inv_fact[max_m] = pow(fact[max_m], MOD-2, MOD)
for i in range(max_m - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(m, k):
    if k < 0 or k > m:
        return 0
    return fact[m] * inv_fact[k] % MOD * inv_fact[m - k] % MOD

# Compute Bell numbers up to Bell(n+1)
max_bell = n + 1
Bell = [0] * (max_bell + 1)
Bell[0] = 1

for m in range(0, max_bell):
    s = 0
    for k in range(m + 1):
        c = comb(m, k)
        s = (s + c * Bell[k]) % MOD
    Bell[m + 1] = s

ans = (Bell[n + 1] - Bell[n]) % MOD
print(ans)
```