<think>
Okay, let's see. The problem is about finding the minimum number of nodes required to create a p-reachable graph, and then among those graphs with the minimum nodes, find the maximum number of unidirectional pairs. Hmm.

So, a p-reachable graph has exactly p ordered pairs (u, v) where u < v and u and v are reachable from each other. Wait, so these are the pairs that form mutual reachability. Because reachable from each other and u < v. So for each such pair, it's counted once. So the problem is to model how many such pairs exist based on the structure of the graph.

The key idea here is probably to model the graph using strongly connected components (SCCs). Because in a directed graph, nodes within the same SCC are mutually reachable. So the number of such pairs (u < v) where u and v are in the same SCC would be the sum over each SCC of (size choose 2). So the total p is the sum over all SCCs of (s choose 2), where s is the size of the component.

So the first part of the problem reduces to finding a set of integers (s_1, s_2, ..., s_k) such that the sum of s_i choose 2 is exactly p, and the sum of s_i is minimized. Because each SCC contributes (s_i * (s_i -1)/2) pairs. And the total number of nodes is the sum of s_i. So to minimize the number of nodes, we need to have as large as possible components, since larger components contribute more to p with fewer nodes.

For example, if p=3, then the best way is to have one component of 3 nodes. 3C2 is 3, which gives exactly p=3. So the sum is 3 nodes. Which matches the first sample input.

In the second sample, p=4. Let's see: 3C2 is 3, which is less than 4. So adding another component. If we have 3+2, sum is 5 nodes. 3C2 + 2C2 = 3 +1=4. So sum is 5 nodes. Which matches the second sample's output.

So the first part of the problem is to find the minimal sum of s_i such that the sum of s_i*(s_i-1)/2 = p. And the approach here is to take the maximum possible s_i for each step. So start with the largest possible component that doesn't exceed the remaining p. So this is similar to the problem of expressing p as a sum of triangular numbers (the maximum possible each time), and the minimal number of terms.

So for example, for p=3, the largest possible is 3C2=3. For p=4, the largest is 3C2=3, then 2C2=1. So sum is 3+2=5.

So the first part is to compute the minimal number of nodes, which is the sum of the sizes of components chosen in this way.

Once we have the minimal sum of nodes, the second part is to find the maximum number of unidirectional pairs possible. So what's a unidirectional pair? It's a pair (u, v) where u !=v, there's a path from u to v, but not vice versa. And we need to count all such pairs, regardless of order (since u and v are ordered here). Wait, no: the problem statement says (u, v) is an ordered pair where u !=v, there's a path from u to v, and no path from v to u. So it's ordered, but the count includes all possible such pairs, not just u < v.

But for the problem's first part, the p is the number of pairs (u, v) with u < v and mutual reachability. So the first part's p is based on mutual reachability for u < v, while the second part's count is based on ordered pairs (u, v) where u≠v and unidirectional.

But for the second part, the maximum number of unidirectional pairs depends on the structure of the graph. How to model this.

Once the SCCs are arranged in a linear order (a DAG of components), then for any two components, all edges go from earlier to later components. Then, between two components, say S and T, where S is before T in the order, all nodes in S can reach all nodes in T, but T nodes can't reach S nodes. So for each pair (u in S, v in T), there's a unidirectional edge. Similarly, (v in T, u in S) would not have a path. So the unidirectional pairs between S and T are all possible ordered pairs where u is in S and v in T (since u can reach v, but not vice versa). So the number is |S| * |T|.

Additionally, within a component, all pairs are mutually reachable, so no unidirectional pairs there. So the total unidirectional pairs is the sum over all pairs of components S and T (S ≠ T) where S is before T in the component order, multiplied by |S| * |T|.

So to maximize the number of unidirectional pairs, the components should be arranged in a linear chain, such that each component can reach all the ones after it, but not before. Then, the total unidirectional pairs would be the sum for all i < j of s_i * s_j.

Wait, yes. Because for components ordered as C1, C2, ..., Ck, then for each i < j, all pairs from Ci to Cj are unidirectional. So the total is sum_{i<j} s_i * s_j.

So the maximum possible unidirectional pairs is the sum over all pairs i < j of s_i * s_j. Which is (sum s_i)^2 - sum s_i^2 all divided by 2. Because sum s_i * sum s_j = sum s_i^2 + 2*sum_{i<j} s_i s_j. So sum_{i<j} s_i s_j = (S^2 - sum s_i^2)/2, where S is the total sum of s_i.

Wait, no: sum_{i} s_i * sum_{j} s_j = sum_{i} sum_{j} s_i s_j = sum_{i=j} s_i s_j + sum_{i<j} s_i s_j + sum_{i>j} s_i s_j. Which equals sum s_i^2 + 2 * sum_{i<j} s_i s_j. So sum_{i<j} s_i s_j = ( (sum s_i)^2 - sum s_i^2 ) / 2.

So the maximum number of unidirectional pairs is (sum s_i)^2 - sum s_i^2 all divided by 2.

But sum s_i is the total number of nodes (n), and sum s_i^2 is the sum of squares of the component sizes.

So the formula for the maximum unidirectional pairs is (n^2 - sum_sq) // 2.

Wait, but the sum of s_i^2 is the sum of squares of the component sizes. So for example, in the first sample input, components are [3], sum_sq is 9, n is 3. So (3^2 -9)/2 = (9-9)/2=0. Which matches the sample output.

In the second sample, components are [3,2], sum_sq is 9+4=13. n=5. (25-13)/2 = 12/2=6. Which matches the sample.

So yes. So the problem's second part can be computed as (n^2 - sum_sq) // 2.

Therefore, once we have the list of component sizes (s_i) that sum to n (the minimal sum), and the sum of s_i^2 is sum_sq, then the answer is (n^2 - sum_sq) // 2.

So the steps are:

1. Find the decomposition of p into triangular numbers, with the largest possible triangles first, to minimize the number of nodes.

   For example, for p, decompose it into the sum of t_k = k*(k-1)/2, choosing the largest possible k each time. So for each step, take the largest k such that t_k <= remaining p. Subtract t_k from remaining p, and proceed until p is zero.

   The component sizes are the k's chosen, sorted in some order (but order doesn't matter for sum, but in terms of the unidirectional pairs, the order affects the sum of s_i*s_j, but according to the formula, the order doesn't matter. Because sum s_i * s_j for i < j is the same as sum s_j * s_i for j < i, so the total is (sum s_i)^2 - sum s_i^2 divided by 2. So the order of the components doesn't matter. So the maximum possible unidirectional pairs is determined by the component sizes, not their order. So the way to maximize the sum is to arrange the components in a way that all possible cross-component pairs are unidirectional, which is achieved by the DAG structure. So the formula holds regardless of the component sizes. Therefore, the sum of s_i^2 and the total n is sufficient.

Therefore, the steps are:

a. Decompose p into a list of component sizes (s_1, s_2, ..., s_k) such that sum (s_i choose 2) = p, and sum s_i is minimized. This is done by taking the largest possible s_i each step.

b. Compute sum_sq as the sum of s_i squared.

c. Then, the second part of the answer is (n^2 - sum_sq) // 2, where n is the sum of s_i.

So the problem reduces to:

For part 1: find the minimal sum of s_i such that sum (s_i choose 2) = p. For part 2: compute (sum s_i)^2 - sum s_i^2 all over 2.

Now, the challenge is to compute this decomposition efficiently, given that p can be up to 2e5.

Let's think about how to decompose p into the sum of triangular numbers (each term is k*(k-1)/2) with as few terms as possible, and the sum of the k's is minimized.

Wait, no. Wait, the sum of (k choose 2) terms is p. The sum of the k's is the minimal possible, which would require that each term is as large as possible, because larger k's contribute more per unit k. For example, for a given (k choose 2), which is k*(k-1)/2, the ratio of (k choose 2) per k is (k-1)/2. So larger k's give a higher ratio, which means that using larger k's allows us to cover more p per unit of k added. Therefore, to minimize the sum of the k's, we need to select the largest possible (k choose 2) <= remaining p, subtract it from p, and proceed.

So the approach is:

Initialize remaining_p = p.

sum_nodes = 0

sum_sq = 0

while remaining_p > 0:

   find the largest k such that (k choose 2) <= remaining_p.

   add k to sum_nodes.

   add k*k to sum_sq.

   subtract (k choose 2) from remaining_p.

So how to find the largest k for a given remaining_p?

The maximum possible k can be found via binary search. For example, for a given value of remaining_p, we can compute the largest k where k*(k-1)/2 <= remaining_p.

The equation is k^2 -k - 2*remaining_p <=0. The solution to this is k = [1 + sqrt(1 +8*remaining_p)] / 2. Taking the floor of that value.

So for example, if remaining_p is 3:

sqrt(25) is 5, (1+5)/2=3. So k=3.

For remaining_p=4: sqrt(33) is ~5.744, (1+5.744)/2=3.372, floor is 3. So k=3. 3C2 is 3, subtract from 4, remaining_p=1. Then next k is 2 (since 2C2 is 1).

So the code can compute k as floor((sqrt(8*remaining_p +1) +1)/2).

Wait, let's see:

The quadratic equation k² -k - 2*C <=0.

The roots are [1 ± sqrt(1 +8C)]/2. The positive root is [1 + sqrt(1+8C)]/2.

So the maximum integer k satisfying k² -k - 2C <=0 is the floor of [1 + sqrt(1 +8C)]/2.

Yes.

So for each step:

k = int( (1 + sqrt(1 + 8*remaining_p)) // 2 )

But we need to check if k*(k-1)/2 <= remaining_p, and also (k+1)*k/2 > remaining_p.

But using the formula, it should give the correct k.

So code steps:

sum_nodes = 0

sum_sq =0

remaining_p = p

while remaining_p >0:

    compute k as the maximum possible where (k choose 2) <= remaining_p.

    sum_nodes +=k

    sum_sq +=k*k

    remaining_p -= (k*(k-1)//2)

So for example, when p=4:

First, remaining_p=4.

k = floor( (1+sqrt(33))/2 ) = (1+5.744)/2 ~3.372 →3.

Check 3*2/2=3 <=4. So subtract 3, remaining_p=1.

Next, remaining_p=1.

k= floor( (1+sqrt(9))/2 )= (1+3)/2=2. So subtract 1, remaining_p=0.

sum_nodes is 3+2=5. sum_sq is 9+4=13.

Then the maximum unidirectional pairs is (5^2 -13)/2 = (25-13)/2=6.

Which matches the sample.

So this approach works.

Now, the edge cases:

If p=0, then sum_nodes is 0. Because the only way to have sum (s_i choose 2) =0 is to have all s_i <2. Since (s_i choose 2) is zero for s_i <2. So possible component sizes are zero or ones. But to have sum (s_i choose 2) =0, but the sum of the s_i's is minimized. So the minimal sum is zero. Which is correct. So output 0 0.

Another example: p=1. The decomposition is [2]. Because (2 choose 2)=1. sum_nodes=2. sum_sq=4. So (2^2 -4)/2=0. So output 2 0.

Wait, but for two nodes in the same component, there are no unidirectional pairs. So yes.

So code seems correct.

So the plan is:

Read p.

If p is zero, output 0 0.

Else, compute the decomposition into the sum of (k choose 2) terms as described, collect the sum_nodes and sum_sq.

Then, compute the answer as (sum_nodes^2 - sum_sq) // 2.

But wait, sum_nodes is the sum of the k's (the component sizes), and sum_sq is sum of k².

So the code for that part is straightforward.

Now, for handling p=0, which is a special case. Because when p is zero, there are no pairs (u <v) with mutual reachability. So the graph must have all nodes in components of size 1. Because if any component has size >=2, then (u <v) in that component would contribute to p. So for p=0, all components are size 1 or 0. But the minimal sum is zero nodes. Because zero nodes would have zero pairs. So the sample input where p=0 gives 0 0.

So the code needs to handle p=0.

So the code steps:

Read p.

if p ==0:

    print(0 0)

else:

    compute sum_nodes, sum_sq as per decomposition.

    compute max_uni = (sum_nodes * sum_nodes - sum_sq) // 2

    print(sum_nodes, max_uni)

But wait, what if the decomposition requires components of size 1? For example, when p=0, but that's handled by the initial case.

But in the code, for p=0, the loop would not run, and sum_nodes is zero. So the code for p=0 is handled by the initial check.

So let's code that.

Now, the code.

But how to compute k in Python?

In Python, we can compute the integer part using math.sqrt, but since floating point precision could be an issue, perhaps using binary search is better. However, for the constraints (p up to 2e5), even binary search would be O(1) per iteration.

But let's see. The formula is:

k = floor( (1 + sqrt(1 +8 * remaining_p)) / 2 )

But in Python, math.sqrt returns a float, and we can compute this.

Let me test:

For example, remaining_p=3:

sqrt(1+8*3) = sqrt(25) =5. So (1+5)/2=3 →k=3.

remaining_p=4:

sqrt(1+8*4) = sqrt(33) ~5.744. (1+5.744)/2=3.372 →floor 3.

remaining_p=1: sqrt(9)=3. (1+3)/2=2 →k=2.

Yes.

So code can use:

import math

def find_max_k(remaining_p):

    if remaining_p ==0:

        return 0

    sqrt_val = math.sqrt(1 + 8*remaining_p)

    k = int( (1 + sqrt_val) //2 )

    # check if (k+1 choose 2) is <= remaining_p?

    # no, because the formula gives the maximum possible k.

    # but sometimes due to floating point errors, it could be off.

    # So we need to verify.

    # For example, if the sqrt is slightly lower than actual.

    while (k+1)*k //2 <= remaining_p:

        k +=1

    while k*(k-1)//2 > remaining_p:

        k -=1

    return k

But perhaps this is redundant. Let's see.

Wait, the formula gives k as the floor of (1 + sqrt(1+8*remaining_p))/2. So for example:

If remaining_p is 2:

sqrt(17) ~4.123. (1+4.123)/2 ~2.56 →k=2. 2*1/2=1 <=2. Then (3 choose 2)=3>2. So correct.

But let's test with code.

Alternatively, perhaps the formula is sufficient, but in code, after computing k, we need to make sure that k*(k-1)/2 <= remaining_p and (k+1)*k/2 > remaining_p.

But perhaps using binary search would be better.

Another approach: binary search for the maximum k where k*(k-1)/2 <= remaining_p.

The binary search can be done as follows:

low =1, high = 2*1e5 (since p can be up to 2e5. For p=2e5, maximum k is when k*(k-1)/2 =2e5. Solving k^2 ~4e5 →k ~632. So high can be up to 2e5, but even better, we can set high to something like 2e5 initially.

But for each step, binary search would be O(log k), which is manageable.

But given that for each step, the code runs in O(1) time (since the maximum possible steps is O(sqrt(p)), which for p=2e5 is about 632 steps), even for the worst case.

But for code efficiency, perhaps using the formula is better.

But in code, due to possible floating point inaccuracies, perhaps the formula might not give the exact k.

For example, if 1+8*remaining_p is a perfect square, then the formula gives exact. But if not, perhaps the formula gives floor(k), but perhaps due to rounding errors, the code might need to adjust.

Alternatively, compute k using the formula, then check.

But let's proceed with code.

Implementing the formula:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    p = int(input_stream.readline().rstrip("\n"))

    if p == 0:
        print(0, 0, file=output_stream)
    else:
        sum_nodes = 0
        sum_sq = 0
        remaining_p = p
        while remaining_p > 0:
            sqrt_val = math.sqrt(1 + 8 * remaining_p)
            k = int((1 + sqrt_val) // 2)
            # Adjust k upwards if necessary
            while (k + 1) * k // 2 <= remaining_p:
                k += 1
            # Adjust k downwards if necessary
            while k * (k - 1) // 2 > remaining_p:
                k -= 1
            sum_nodes += k
            sum_sq += k * k
            remaining_p -= k * (k - 1) // 2
        max_uni = (sum_nodes * sum_nodes - sum_sq) // 2
        print(sum_nodes, max_uni, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
""",
            "output": \
"""\
5 6
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
import math


def main(input_stream, output_stream):
    p = int(input_stream.readline().rstrip("\n"))

    if p == 0:
        print(0, 0, file=output_stream)
    else:
        sum_nodes = 0
        sum_sq = 0
        remaining_p = p
        while remaining_p > 0:
            sqrt_val = math.sqrt(1 + 8 * remaining_p)
            k = int((1 + sqrt_val) // 2)
            # Adjust k upwards if necessary
            while (k + 1) * k // 2 <= remaining_p:
                k += 1
            # Adjust k downwards if necessary
            while k * (k - 1) // 2 > remaining_p:
                k -= 1
            sum_nodes += k
            sum_sq += k * k
            remaining_p -= k * (k - 1) // 2
        max_uni = (sum_nodes * sum_nodes - sum_sq) // 2
        print(sum_nodes, max_uni, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
0
""",
            "output": \
"""\
0 0
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

Sample 3:

input 0. Output 0 0.

Another test case: p=5.

As above, output 7 16. Let's see.

But the code would output 7 and 16.

But perhaps there's a better decomposition. For example, 3C2 (3) + 3C2 (3) is 6>5. So no. So decomposition must be 3+1+1 (but 1C2 is zero). So that's not possible. So the code's decomposition is correct.

So the code should be correct.
</think>

```python
import math

p = int(input())

if p == 0:
    print(0, 0)
else:
    sum_nodes = 0
    sum_sq = 0
    remaining_p = p
    while remaining_p > 0:
        sqrt_val = math.sqrt(1 + 8 * remaining_p)
        k = int((1 + sqrt_val) // 2)
        # Adjust k upwards if necessary
        while (k + 1) * k // 2 <= remaining_p:
            k += 1
        # Adjust k downwards if necessary
        while k * (k - 1) // 2 > remaining_p:
            k -= 1
        sum_nodes += k
        sum_sq += k * k
        remaining_p -= k * (k - 1) // 2
    max_uni = (sum_nodes * sum_nodes - sum_sq) // 2
    print(sum_nodes, max_uni)
```
