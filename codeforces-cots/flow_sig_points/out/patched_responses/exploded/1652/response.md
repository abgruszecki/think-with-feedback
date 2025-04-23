<think>
Okay, let's try to tackle this problem. The problem is about counting the number of valid bridge configurations between three clusters of islands (red, blue, purple), such that any two islands of the same color are either disconnected or their shortest path is at least 3. Hmm, that sounds a bit complex. Let me break it down.

First, the constraints. For same-color islands, either they can't reach each other through bridges, or if they can, the shortest path between them is at least 3. So, what does that imply? Well, think about the bridges between different clusters. Because if two same-color islands are connected via bridges of other colors, their path must be long enough.

Wait, same-color islands can't have a bridge between them. Because if two same-color islands are connected directly (distance 1), that's invalid. So, bridges can only be between different colors. Oh right, because the problem says "between some (possibly all or none) of the islands" but the same-color ones can't be connected. So all bridges are between different clusters. So, the problem reduces to building bridges between red-blue, red-purple, blue-purple pairs, but ensuring that any two islands in the same cluster are not connected via a path that would create a distance less than 3.

Wait, no. The constraint is that for any two same-color islands, either they are not connected via bridges (i.e., no path), or if they are connected, their shortest path is at least 3. So the same-color islands can't be connected through a path of two bridges. For example, red1 connected to blue1, blue1 connected to red2. Then red1 and red2 have a path of length 2, which is invalid.

So the problem is to build bridges between different colors such that there are no such paths of length 2 between same-color islands. How can we model this?

Let me think of each cluster as a group. For the constraints to hold, there must be no two nodes in the same cluster that are connected via a two-edge path. So, for example, a red node can't be connected to two different blue nodes. Wait, no. Wait, if a red node is connected to a blue node and a purple node, that's allowed. But if two red nodes are connected through a blue node, then their shortest path is 2, which is invalid.

So, the key is that in the bipartite graph between any two different clusters, the graph must be such that no two nodes in the same cluster have a common neighbor in another cluster.

Wait, that makes sense. Because if two red nodes, r1 and r2, are both connected to a blue node b, then the path r1-b-r2 is length 2, which would make the distance between r1 and r2 equal to 2. Which violates the constraint. So, the same-color nodes cannot share any common neighbor in another cluster.

Similarly, if a red node r is connected to a blue node b, and that blue node is connected to a purple node p, then r and p are connected through a path of length 2, but since they are different colors, that's allowed. The constraints only apply to same-color pairs.

So, the problem reduces to building three bipartite graphs (red-blue, red-purple, blue-purple) such that for any two nodes in the same cluster, they have no common neighbors in any of the other clusters.

So, for example, in the red cluster, any two red nodes cannot have a common blue neighbor (from the red-blue graph) or a common purple neighbor (from the red-purple graph). Similarly, two blue nodes can't have a common red or purple neighbor, etc.

Therefore, for each pair of clusters (say red and blue), the bipartite graph between them must be such that each node in red is connected to a subset of blue nodes, and no two red nodes share any blue node. Wait, no. Wait, the problem is that if two red nodes share a blue node, that creates a path of length 2 between them, which is invalid. So in the red-blue bipartite graph, the adjacency must be such that no two red nodes are connected to the same blue node. Similarly, the red-purple graph must have no two reds connected to the same purple. And the blue-purple graph must have no two blues connected to the same purple, or two purples connected to the same blue.

Wait, but for the blue-purple graph, for example, if two blue nodes are connected to the same purple node, then those two blues are connected via a path of length 2 (through the purple), which would be invalid for the blue cluster. So yes, same logic applies here.

So, the constraints for the bipartite graphs between different clusters are that each edge set must form a matching. Because a matching is a set of edges where no two edges share a common node. But wait, in this problem, for a bipartite graph between red and blue, the edges form a matching on both sides. Wait, no. Let's think: For the red-blue graph, if two different red nodes are connected to the same blue node, that's a problem. So in the red-blue graph, each blue node can be connected to at most one red node. Similarly, each red node can be connected to at most one blue node? No, wait. Because if a red node is connected to multiple blue nodes, but none of those blue nodes are connected to other red nodes, that's allowed. Because the problem is that two red nodes can't share a blue neighbor. But a single red node connected to multiple blue nodes is okay as long as each blue is only connected to that red.

Wait, let's clarify. For the red-blue bipartite graph, the condition is that each blue node can be connected to at most one red node. Because if a blue node is connected to two different red nodes, those two reds are connected via a path of length 2 (through the blue), which is invalid. So, in the red-blue graph, each blue node can have at most one red neighbor. Similarly, each red node can have multiple blue neighbors, but each blue can have only one red.

Wait, no. Because suppose red node r1 is connected to blue nodes b1 and b2. But if none of those blue nodes are connected to other red nodes, then r1's connections are okay. The problem arises when two different reds share a blue. So the constraint is that the bipartite graph between red and blue must be such that no two reds share a blue. Similarly, for the blue and purple graph, no two blues share a purple.

Wait, but in the red-blue graph, each blue can be connected to at most one red. But each red can be connected to any number of blues, as long as those blues are not connected to any other reds. So, the bipartition must form a graph where each node on the blue side has degree at most 1. So the red-blue graph is a collection of edges where each blue is in at most one edge. But the reds can have multiple edges, as long as each blue they connect to is not connected to any other red.

Alternatively, the bipartition between red and blue is such that the edges form a set of stars where each star's center is a red node and the leaves are blue nodes, but each blue can only be in one star. Wait, no. Because if a blue is in a star (connected to a red), then no other red can connect to it.

So, the red-blue bipartition can be thought of as a collection of edges where each blue is in at most one edge. But the reds can have any number of edges, as long as the blues they are connected to are not connected to any other reds.

Similarly, for the red-purple bipartition, each purple can be connected to at most one red. And for the blue-purple bipartition, each purple can be connected to at most one blue.

Wait, but the problem also requires that in the blue-purple graph, each blue can be connected to multiple purples, but each purple can be connected to at most one blue. Because if two blues are connected to the same purple, then those two blues are connected via a path of length 2, which is invalid.

So, for each bipartition between two clusters, the edges must form a graph where the nodes from the third cluster (i.e., the other cluster) have degree at most 1. Wait, no. Let's take the red and blue clusters. The edges between them can form any bipartite graph, but with the constraint that no two reds share a blue, and no two blues share a red. Wait, no. Because if two blues share a red, that's allowed? Wait, no. Let's see. Suppose blue1 and blue2 are connected to red1. Then blue1 and blue2 have a path of length 2 (through red1), which would violate the constraint for the blue cluster. Because blue1 and blue2 are same-color, their shortest path would be 2, which is invalid.

Oh right! So the same applies to the blue cluster. So for the blue cluster, any two blue nodes cannot have a common neighbor (in any other cluster). So in the red-blue bipartition, each red can be connected to at most one blue. Similarly, each blue can be connected to at most one red. Because if a red is connected to two blues, then those blues are connected through that red, which would be a path of length 2. Which is invalid for the blue cluster.

Ah! So the bipartition between any two clusters must be a matching. Because a matching is a set of edges where no two edges share a node on either side. So between red and blue, the edges must form a matching: each red is connected to at most one blue, and each blue is connected to at most one red. Because if any red is connected to two blues, that creates a path of length 2 between those two blues, which is invalid. Similarly, if a blue is connected to two reds, that's invalid for the reds.

So, all three bipartitions (red-blue, red-purple, blue-purple) must be matchings. Because any edge in those bipartitions can't have multiple edges from either side. Because otherwise, two nodes in the same cluster would be connected via a path of length 2.

Wait, but wait. Let's take the red-purple bipartition. Suppose two red nodes are connected to the same purple node. Then those two reds have a path of length 2 (through the purple). So, the red-purple graph must also be a matching. So, all three bipartitions must be matchings.

So, the problem reduces to counting the number of possible triplets of matchings (M_ab, M_ac, M_bc), where:

- M_ab is a matching between red and blue clusters (i.e., each red is connected to at most one blue and vice versa)
- M_ac is a matching between red and purple clusters (each red connected to at most one purple and vice versa)
- M_bc is a matching between blue and purple clusters (each blue connected to at most one purple and vice versa)

But there's an additional constraint: the combination of these matchings must not create any paths of length 2 between nodes in the same cluster through any combination of edges. Wait, but earlier analysis suggests that if each bipartition is a matching, then such paths are impossible. Because for example, if two red nodes are connected via a blue and a purple node (like red1 - blue1 - purple1 - red2), that's a path of length 3. But the problem allows that, as the shortest path between red1 and red2 is 3, which is allowed. So the only forbidden paths are those of length exactly 2.

But if all three bipartitions are matchings, then any two nodes in the same cluster cannot have a common neighbor in any bipartition. Because in the bipartition between their cluster and another, each node can only be connected to at most one node in the other cluster. So, for example, two red nodes can't share a blue or a purple neighbor. Because in M_ab, each blue can have at most one red neighbor, and in M_ac, each purple can have at most one red neighbor. So, any two reds can't have a common neighbor in any bipartition.

Therefore, if all three bipartitions are matchings, then the constraints are satisfied. Because any two nodes in the same cluster can't have a path of length 2. Because such a path would require that they share a neighbor in some bipartition, which isn't allowed. So the problem reduces to counting the number of possible triplets of matchings between the three pairs of clusters.

Therefore, the total number of valid configurations is the product of the number of possible matchings between each pair of clusters, but with the caveat that the edges in different bipartitions are independent. Wait, no. Because the matchings between red-blue, red-purple, and blue-purple are all independent. So the total number of valid configurations is the product of the number of matchings in each bipartition.

Wait, that can't be right. For example, the first sample input is a=1, b=1, c=1. Let's compute for each bipartition the number of possible matchings.

For red-blue: since there is 1 red and 1 blue. A matching can have 0 or 1 edges. So 2 possibilities.

Similarly for red-purple: 2 possibilities. And blue-purple: 2 possibilities. So product is 2*2*2=8, which matches the first sample. So yes, that works.

Another example: input 1 2 2. Let's see:

Red has 1 node. Blue has 2, purple has 2.

For red-blue bipartition: the possible matchings are all subsets where the red is connected to 0 or 1 of the blues. So 1 + 2 = 3 options (since the red can choose none, blue1, or blue2).

Similarly, red-purple bipartition: 3 options.

Blue-purple bipartition: the bipartition is between 2 blue and 2 purple. The number of possible matchings here is the sum over k (number of edges in the matching) from 0 to 2. For k=0: 1. For k=1: 2*2=4 (choose a blue and a purple). For k=2: 2 possibilities (each blue matched to a distinct purple). So total is 1+4+2=7.

So the product is 3 * 3 * 7 = 63, which matches the second sample.

So this approach seems correct. Therefore, the problem reduces to computing the product of the number of possible matchings between each pair of clusters. Each of the three pairs (a and b, a and c, b and c) contributes a factor equal to the number of possible matchings between their nodes, under the constraints that each node is in at most one edge in the matching.

So the problem is to compute for each of the three pairs (red-blue, red-purple, blue-purple) the number of possible matchings, then multiply all three numbers modulo 998244353.

So now, the problem reduces to calculating, for each pair (x, y), the number of possible matchings between x and y, where a matching is a set of edges such that each node in x and y is part of at most one edge.

How to compute the number of matchings between two groups of size x and y?

This is a standard combinatorial problem. The number of matchings between two sets of sizes n and m is the sum over k from 0 to min(n, m) of (n choose k) * (m choose k) * k! ), multiplied by 2^k if we consider directed edges. Wait, but in our case, each edge is bidirectional (it's an undirected edge), but the matching is a set of edges where each node appears at most once. So for each k, we choose k nodes from the first set, k from the second set, and match them in k! ways. So the total for a bipartition between sizes n and m is the sum_{k=0}^min(n,m)} [ C(n, k) * C(m, k) * k! ]

So the formula for the number of matchings between n and m nodes is f(n, m) = sum_{k=0}^{min(n,m)} [ (n choose k) * (m choose k) * k! } ]

Yes. Because for each possible k (number of edges in the matching), we choose k nodes from the first group, k nodes from the second group, and then match them in k! ways (permutations of the second group's k nodes). So the total for each k is (n choose k) * (m choose k) * k!.

So, for example, when n=1 and m=1, min is 1. The sum is for k=0 and k=1. For k=0: 1. For k=1: (1 choose 1) * (1 choose 1) * 1! = 1*1*1 = 1. So total is 1+1=2.

Which matches the first part of the first sample.

So the problem is to compute this sum for each of the three pairs (a and b, a and c, b and c), then multiply them modulo 998244353.

Now, the challenge is to compute this sum efficiently, given that a, b, c can be up to 5000. So for each pair (n, m), we need to compute the sum from k=0 to min(n,m) of (C(n, k) * C(m, k) * k! ), mod 998244353.

But how to compute this efficiently for large n and m?

First, let's precompute factorials and inverse factorials modulo 998244353 up to 5000, so that we can compute C(n, k) quickly.

But for each (n, m), the sum can be up to 5000 terms. For n and m up to 5000, this would be O(5000) per pair, and three pairs per test case. So 3*5000 = 15,000 operations per test case, which is manageable.

But perhaps there's a smarter way. Let's think.

Wait, for each pair (n, m), the sum S(n, m) is sum_{k=0}^k_max [ C(n, k) * C(m, k) * k! }

But note that C(n, k) * k! = P(n, k) (the number of permutations of k elements from n), which is n!/( (n-k)! ) ). Similarly, C(m, k) * k! = P(m, k).

So S(n, m) = sum_{k=0}^k_max P(n, k) * C(m, k).

Wait, but that's not helpful. Alternatively, perhaps we can find a generating function for this sum.

Alternatively, note that for each k, the term is (n choose k) * (m choose k) * k! = (n! / (k! (n-k)! )) ) * (m! / (k! (m-k)! )) ) * k! ) = (n! m! ) / (k! (n-k)! (m-k)! )) )

But that's complicated. Not sure if that helps.

Alternatively, perhaps precompute for each possible n and m (up to 5000) the sum S(n, m). But with 5000 possible n and 5000 possible m, that's 25 million entries. For each entry, we need to compute the sum in O(k_max) steps. That's 25 million * 5000 operations, which is 125 billion. That's way too much.

But since the input has only three pairs (a and b, a and c, b and c), perhaps we can compute the sum for each of these three pairs on the fly, given a, b, c.

But for each pair (n, m), the sum is O(k_max), where k_max is min(n, m), which is up to 5000. So for each pair, the sum is computed in 5000 steps, which is acceptable.

So the plan is:

1. Precompute factorial and inverse factorial up to 5000, modulo 998244353.

2. For each pair (x, y), compute the sum S(x, y) = sum_{k=0}^min(x,y) [ C(x, k) * C(y, k) * k! ] mod 998244353.

3. Multiply S(a, b) * S(a, c) * S(b, c) mod 998244353.

So the main steps are to compute these three sums and multiply them.

Now, how to compute C(n, k) for given n and k?

C(n, k) = factorial[n] * inv_fact[k] * inv_fact[n -k] mod MOD.

So, for each term in the sum, compute C(x, k) * C(y, k) * k! = [C(x, k) * k! ] * C(y, k) = P(x, k) * C(y, k).

But that's not necessary. Just compute each term as C(x, k) * C(y, k) * fact[k], where fact[k] is the factorial of k.

Wait, since C(x, k) * C(y, k) * k! = (x choose k) * (y choose k) * k! So if we have precomputed factorial up to 5000, and inv_fact up to 5000, then for each k, compute:

term = (C(x, k) * C(y, k) ) * fact[k]

But C(x, k) is (x! )/(k! (x -k)! )) → so the term becomes (x!/(k! (x -k)! )) * (y!/(k! (y -k)! )) ) * k! → simplifying:

(x! y! ) / ( (k! (x -k)! ) (k! (y -k)! )) ) * k! → 

= (x! y! ) / (k! (x -k)! (y -k)! )) 

But for the purposes of code, perhaps it's easier to compute C(x, k) and C(y, k) as combinations, multiply them, multiply by fact[k], and add to the sum.

So in code, precompute fact and inv_fact arrays.

Then, for each pair (n, m), compute the sum as follows:

sum = 0

for k in 0 to min(n, m):

    term = C(n, k) * C(m, k) % MOD

    term = term * fact[k] % MOD

    sum = (sum + term) % MOD

So the key steps are precomputing fact and inv_fact, then for each pair, loop k from 0 to min(n, m), compute the term as the product of combinations and factorial.

Now, the precomputation:

fact[0] = 1

for i in 1..5000:

    fact[i] = fact[i-1] * i % MOD

inv_fact[5000] = pow(fact[5000], MOD-2, MOD)

for i in 4999 down to 0:

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

Then, C(n, k) is computed as fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD.

So, the code structure would be:

- Precompute fact and inv_fact.

- Read a, b, c.

- Compute S(a, b), S(a, c), S(b, c).

- Multiply them mod MOD.

So, for example, for the first sample input:

a=1, b=1, c=1.

Compute S(a, b) = sum for k=0 to 1.

k=0: C(1,0)*C(1,0)*0! = 1*1*1 =1.

k=1: C(1,1)*C(1,1)*1! =1*1*1=1. Sum is 2.

Similarly for S(a,c) and S(b,c), all 2. 2*2*2=8.

Which matches.

For the second sample input: a=1, b=2, c=2.

S(a, b) is sum for k=0 to 1.

k=0: 1.

k=1: C(1,1)*C(2,1)*1! → 1 * 2 * 1 =2. Sum 1+2=3.

Same for S(a,c) (3). S(b,c) is sum over k up to 2.

k=0:1.

k=1: C(2,1) * C(2,1) * 1! → 2*2*1=4.

k=2: C(2,2)*C(2,2)*2! → 1*1*2=2.

Sum is 1+4+2=7.

3*3*7=63.

Which matches.

So the approach is correct.

Now, the code. First, precompute fact and inv_fact.

But since the constraints are up to 5000, the maximum possible value for n and m is 5000, so precomputing up to 5000 is sufficient.

Now, code steps:

Read a, b, c.

Compute the three sums S(a,b), S(a,c), S(b,c).

Multiply them mod 998244353.

So, the code in Python would be:

First, precompute fact and inv_fact up to 5000.

Then, for each pair (n, m), compute the sum as described.

But in Python, even for 5000 elements, precomputing is manageable.

Now, the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    max_n = 5000

    fact = [1] * (max_n + 1)

    for i in range(1, max_n + 1):

        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1] * (max_n + 1)

    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

    for i in range(max_n-1, -1, -1):

        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(n, k):

        if k <0 or k >n:

            return 0

        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    def compute_sum(n, m):

        min_k = min(n, m)

        total = 0

        for k in range(0, min_k +1):

            c_nk = comb(n, k)

            c_mk = comb(m, k)

            term = c_nk * c_mk % MOD

            term = term * fact[k] % MOD

            total = (total + term) % MOD

        return total

    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    s_ab = compute_sum(a, b)

    s_ac = compute_sum(a, c)

    s_bc = compute_sum(b, c)

    result = s_ab * s_ac % MOD

    result = result * s_bc % MOD

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2 2
""",
            "output": \
"""\
63
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
    MOD = 998244353

    max_n = 5000

    fact = [1] * (max_n + 1)

    for i in range(1, max_n + 1):

        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1] * (max_n + 1)

    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

    for i in range(max_n-1, -1, -1):

        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(n, k):

        if k <0 or k >n:

            return 0

        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    def compute_sum(n, m):

        min_k = min(n, m)

        total = 0

        for k in range(0, min_k +1):

            c_nk = comb(n, k)

            c_mk = comb(m, k)

            term = c_nk * c_mk % MOD

            term = term * fact[k] % MOD

            total = (total + term) % MOD

        return total

    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    s_ab = compute_sum(a, b)

    s_ac = compute_sum(a, c)

    s_bc = compute_sum(b, c)

    result = s_ab * s_ac % MOD

    result = result * s_bc % MOD

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 3 5
""",
            "output": \
"""\
3264
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    max_n = 5000

    fact = [1] * (max_n + 1)

    for i in range(1, max_n + 1):

        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1] * (max_n + 1)

    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

    for i in range(max_n-1, -1, -1):

        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(n, k):

        if k <0 or k >n:

            return 0

        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    def compute_sum(n, m):

        min_k = min(n, m)

        total = 0

        for k in range(0, min_k +1):

            c_nk = comb(n, k)

            c_mk = comb(m, k)

            term = c_nk * c_mk % MOD

            term = term * fact[k] % MOD

            total = (total + term) % MOD

        return total

    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    s_ab = compute_sum(a, b)

    s_ac = compute_sum(a, c)

    s_bc = compute_sum(b, c)

    result = s_ab * s_ac % MOD

    result = result * s_bc % MOD

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 2 9
""",
            "output": \
"""\
813023575
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

</think>

```python
MOD = 998244353
max_n = 5000

fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_n + 1)
inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

def compute_sum(n, m):
    min_k = min(n, m)
    total = 0
    for k in range(min_k + 1):
        c_nk = comb(n, k)
        c_mk = comb(m, k)
        term = c_nk * c_mk % MOD
        term = term * fact[k] % MOD
        total = (total + term) % MOD
    return total

a, b, c = map(int, input().split())
ab = compute_sum(a, b)
ac = compute_sum(a, c)
bc = compute_sum(b, c)
result = ab * ac % MOD
result = result * bc % MOD
print(result)
```
