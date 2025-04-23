<think>
Okay, so I need to solve this problem where I have to calculate the sum of the weights of all possible partitions of a set into exactly k non-empty subsets. The weight of a partition is a sum over each subset S in the partition of |S| multiplied by the sum of the elements in S. And then I have to find the sum of all such possible partitions, modulo 1e9+7.

Hmm. Let's think about how to approach this. The constraints are up to 2e5 elements, which suggests that any O(n^2) solution is out of the question. So we need a linear or O(n) approach, possibly involving some combinatorial math and precomputed factorials or something like that.

Let me break down the problem. For each element, how does it contribute to the total sum? Because the sum is over all partitions, each element's contribution might be considered in some way multiplied by the number of times it's part of a subset of a certain size.

Wait, maybe the total sum can be expressed as the sum for each element w_i multiplied by some coefficient that depends on how many times it's counted in the subsets across all partitions. Then, the problem reduces to finding that coefficient for each w_i and summing all w_i * coefficient, then taking modulo.

But how to compute that coefficient?

Let me think. The weight of a partition is the sum for each subset S in the partition of |S| * sum(w_i for i in S). So for each subset S, each element in S contributes w_i multiplied by |S|, and this is summed over all subsets in the partition. So each element's contribution in a particular partition is w_i multiplied by the size of the subset it's in. Then, across all possible partitions, the total sum is the sum over all partitions, for each element, w_i * (size of subset containing it in that partition). So the total can be rewritten as the sum of w_i multiplied by the sum over all possible partitions of the size of the subset containing element i in that partition.

So, for each element i, let's compute C_i, which is the sum over all valid partitions (into k non-empty subsets) of the size of the subset that contains i. Then the answer is sum(w_i * C_i) mod 1e9+7.

So the problem reduces to calculating C_i for each element, then multiplying each by w_i and summing.

The key is to find C_i. Since all elements are treated symmetrically (since the subsets are unordered, but the elements are not, but their weights are arbitrary), perhaps C_i is the same for all elements. Wait, no. Because the elements are distinct, but the problem statement counts partitions where two elements are in the same subset in one partition and different in another as different. However, for the purpose of computing C_i, since each element is considered individually, perhaps the C_i depends on the structure of the partitions, but the coefficient might be the same for all elements. Wait, let's think.

Suppose all elements are identical except for their weights. Then, the C_i would be the same for all elements. But since the problem allows different partitions based on which elements are grouped together, but when considering C_i, we're summing over all possible partitions where the element i is in a subset of size s. So for the purposes of C_i, perhaps each element's contribution is independent of others except for their grouping. However, in reality, the structure of the partitions affects each element's contribution. But maybe due to symmetry, each element's C_i is the same. Because the problem is symmetric with respect to elements except for their weights. For example, swapping two elements would not change the total sum as their weights are multiplied by the same C_i. Therefore, all C_i are equal. So that C_i = C for all i, and the answer is C * sum(w_i).

Wait, that would make sense. Because in the first example, sum(w_i) is 2+3+2+3=10. The answer is 160, so C would be 160 / 10 = 16. Let's check the first sample. Yes, the answer is 160, which is 16*10. So that's correct. Similarly, in the second sample, sum is 1+2+3+4+5=15. The answer is 645, which is 43*15. Wait, 645 /15 is 43, yes. So this seems to hold.

So the key is that all elements have the same coefficient C. Therefore, the answer is C multiplied by the sum of all w_i. So now the problem reduces to calculating C.

So how to compute C? Let's model this.

Each element's C is the sum, over all possible partitions into k non-empty subsets, of the size of the subset that contains the element in that partition.

But since all elements are treated the same way (as the problem's answer is the same regardless of the elements' order, except for their weights), this sum must be the same for each element.

Therefore, C is equal to (number of partitions into k subsets) multiplied by the average size of the subset containing a particular element, multiplied by the average number of times that element's subset is size s. Wait, perhaps there's a combinatorial formula here.

Alternatively, let's think about the total sum of the sizes of the subsets containing each element over all possible partitions. Since all elements are equivalent, this sum is the same for each element. Let's denote the total number of valid partitions as S(n, k), which is the Stirling numbers of the second kind multiplied by k! (since the subsets are considered labeled here). Wait, in the problem statement, the subsets are part of a partition, and two partitions are considered different if any two elements are in different subsets. So the order of the subsets does not matter. Wait, no. Because the problem says that two partitions are different if there's a pair of elements that are in the same subset in one and different in another. So the order of the subsets in the partition doesn't matter. So for example, {A,B}, {C} is the same partition as {C}, {A,B}, but in the problem statement, are they considered different? Wait, no. Because the problem says "partitions R of the given set into exactly k non-empty subsets". So the order of the subsets in the partition R doesn't matter. Wait, but the problem's definition of partition is a set of subsets. Therefore, the order of the subsets in R does not affect the identity of the partition. So in the sample input, for example, the first case has 7 possible partitions. Let's see the first sample input where n=4, k=2. The number of partitions into exactly 2 subsets is S(4, 2) = 7. Then multiplied by the weight of each partition.

But in the problem statement, each partition is considered as a set of subsets, so the order of subsets doesn't matter. However, when the problem counts the partitions, each subset's order in the partition R is irrelevant. So the number of such partitions is equal to the Stirling numbers of the second kind, S(n, k). But wait, no. Wait, the Stirling numbers of the second kind count the number of ways to partition a set into k non-empty, unlabeled subsets. So that's exactly the case here. So the number of possible partitions is S(n, k).

But when calculating the weight of each partition, each subset's contribution is |S| * sum of elements. So the order of the subsets in R doesn't affect the weight. Therefore, the total sum of the weights is the same as S(n, k) multiplied by the average weight per partition. Wait, no. Because each individual partition contributes its own weight, so the total is the sum over all possible partitions (counted as S(n,k)) of the weight of that partition.

But how to model that.

Alternatively, let's model the total sum as follows. Since each element's contribution to the total sum is w_i multiplied by the sum over all partitions of the size of the subset containing i in that partition, then the total is sum(w_i) * C, where C is the sum over all partitions of the size of the subset containing a particular element in that partition.

So how to compute C.

Let's fix an element, say element 1. For all possible partitions into k subsets, we need to find the sum over all such partitions of the size of the subset that contains element 1.

So for each partition, the subset containing element 1 has some size s, which is at least 1. The sum is s multiplied by the number of partitions where element 1 is in a subset of size s, for all s from 1 to n -k +1 (since each subset must be non-empty and there are k subsets, so the maximum possible size of a subset is n - (k-1)*1 = n -k +1).

So the problem is to compute sum_{s=1 to ...} s * f(s), where f(s) is the number of partitions of the set into k subsets where the subset containing element 1 has size s.

Then, C is equal to this sum.

So how to compute f(s). Let's think. For each s, the subset containing element 1 has exactly s elements. So we choose s-1 elements from the remaining n-1 elements to be in the same subset as element 1. Then, the remaining (n-1 - (s-1)) = n-s elements must be partitioned into k-1 non-empty subsets. The number of ways to do this is C(n-1, s-1) multiplied by S(n - s, k-1), where S(n-s, k-1) is the Stirling number of the second kind for n-s elements and k-1 subsets.

So f(s) = C(n-1, s-1) * S(n-s, k-1).

Therefore, the sum C is sum_{s=1}^{n - (k-1)+1} s * C(n-1, s-1) * S(n-s, k-1).

But wait, when s is such that n-s >= k-1, since S(n-s, k-1) is zero if n-s < k-1. So s can range from 1 to n - (k-1) + 1? Let's see. The maximum possible s is when the subset with element 1 has as many elements as possible, leaving the remaining n-s elements to be partitioned into k-1 subsets, each of size at least 1. So n-s >= k-1 => s <= n - (k-1). So the maximum s is n -k +1.

So the sum is for s from 1 to (n -k +1), but only those s where n-s >= k-1. So s can range up to n -k +1.

But how to compute this sum. The problem is that n can be up to 2e5, so we need an O(n) approach.

But calculating Stirling numbers for S(n-s, k-1) for all possible s is expensive. Wait, but maybe we can find a combinatorial formula that allows this sum to be expressed in a closed form.

Alternatively, perhaps there's a way to express C in terms of some other combinatorial numbers.

Alternatively, let's think of the sum C as the sum over s of s * C(n-1, s-1) * S(n-s, k-1).

But we can split s into C(n-1, s-1) multiplied by S(n-s, k-1), and then multiplied by s.

Hmm. Let's think of C(n-1, s-1) * s. That's equal to C(n-1, s-1) * s = (n-1 choose s-1) * s = (n-1)! / ( (s-1)! (n-s)! )) * s = n * (n-1 choose s-1) / (n-s +1 - (s-1 - (s-1)) )? Wait, maybe not. Wait, s * C(n-1, s-1) = s * (n-1 choose s-1) = (n-1 choose s-1) * s = (n-1)! * s / ( (s-1)! (n-s)! )) ) = (n-1)! * s / ( (s-1)! (n-s)! )) = (n-1)! * s / ( (s-1)! (n-s)! ) )

s = (s) = (s) = (s-1 + 1). So (s) = (s-1) +1.

But (s-1)! * s = s! So:

s * (n-1 choose s-1) = (n-1)! * s / ( (s-1)! (n-s)! )) ) = n * (n-1)! * 1 / ( (s-1)! (n-s)! )) ) * s /n.

Wait, not sure. Alternatively:

s * C(n-1, s-1) = s * (n-1 choose s-1) = (n choose s) * (s) * (s) / n? Not sure. Let's compute:

s * C(n-1, s-1) = s * (n-1)! / ( (s-1)! (n-s)! )) = (n-1)! * s / ( (s-1)! (n-s)! )) = (n-1)! * s / ( (s-1)! (n-s)! )) ) 

s/(s-1)! ) = 1/(s-2)! ) when s >=2. Wait, no. s/(s-1)! = s/( (s-1) * (s-2)! )) = 1/( (s-2)! ) * (s/(s-1)) ). Not sure.

Alternatively, let's note that s * C(n-1, s-1) = n * C(n-1, s-1) * (s/n) ). Hmm. Not helpful.

Alternatively, perhaps express s * C(n-1, s-1) as n * C(n-1, s-1) * (s/(n)). Not sure.

Alternatively, note that s * C(n-1, s-1) = n * C(n-2, s-2) + C(n-1, s-1). Let's see: C(n-1, s-1) = (n-1 choose s-1). s * C(n-1, s-1) = (s) * (n-1 choose s-1). Let's expand this:

(n-1 choose s-1) * s = (n-1)! * s / ( (s-1)! (n-s)! )) ) 

= (n-1)! * s / ( (s-1)! (n-s)! )) 

= (n)! / ( (s-1)! (n-s)! )) * s /n 

Wait, not sure.

Alternatively, (n-1 choose s-1) * s = n * (n-2 choose s-2) ) + (n-1 choose s-1). Not sure.

Alternatively, perhaps this is not the right path. Let's think of the sum as:

sum_{s=1 to m} s * C(n-1, s-1) * S(n-s, k-1)

where m = n - (k-1).

Hmm. Let's substitute t = s-1. Then s = t+1, and the sum becomes sum_{t=0 to m-1} (t+1) * C(n-1, t) * S(n - (t+1), k-1) 

= sum_{t=0}^{m-1} (t+1) * C(n-1, t) * S( (n-1 - t), k-1 )

Hmm. Not sure if that helps.

Wait, perhaps using generating functions. The Stirling numbers of the second kind have generating functions, and perhaps there's a generating function approach here.

Alternatively, perhaps there's a combinatorial identity that allows this sum to be expressed in terms of other known quantities. Let's think.

Suppose we have a set of n elements, and we want to partition into k subsets. For each element x, the sum of the sizes of the subsets that contain x in all such partitions is C. So, the total sum over all elements is n*C. But this total can be computed another way. For each partition, the sum over all subsets S in the partition of |S| * sum(w_i) is equivalent to sum_{S} |S| * sum_{x in S} w_x = sum_{x} w_x * sum_{S containing x} |S|. So for each partition, the sum of the |S| for each subset S is sum_{x} |S_x|, where S_x is the subset containing x. But since each subset S contributes |S| once for each of its elements, the sum is sum_{S} |S|^2. So the total sum across all partitions is sum_{partitions} sum_{S in partition} |S|^2 * sum_{x in S} w_x. Wait, no. Wait, no, the original weight for a partition is sum_S (|S| * sum_{x in S} w_x). Which is the same as sum_{x} w_x * |S_x|, where S_x is the subset containing x. So the total sum across all partitions is sum_{partitions} sum_{x} w_x |S_x|. Which is sum_x w_x * sum_{partitions} |S_x|. Which is what we have: sum_x w_x * C.

So the total sum is (sum w_x) * C, since each x contributes C.

But the total sum can also be calculated as sum over all partitions, sum_{S} |S| * sum_{x in S} w_x. Which is equal to sum_{S} |S| * sum_{x in S} w_x summed over all partitions. But this is the same as sum_{x} w_x sum_{partitions where x is in some S} |S|. So again, same as sum w_x * C.

But how to find C.

Alternatively, the sum over all partitions of sum_{S} |S|^2 is equal to the sum over all elements of sum over partitions of |S_x| (since each subset contributes |S| once for each of its elements, leading to sum_S |S|^2). So this is equivalent to sum_{x} C_x. But since all C_x are equal, this sum is n * C. So the total sum for all partitions of sum_S |S|^2 is n * C.

But how to compute that. Wait, perhaps we can find a formula for this sum.

The sum over all partitions into k subsets of sum_S |S|^2.

Alternatively, perhaps this sum can be expressed as S(n, k) * something, but I'm not sure.

Alternatively, let's model this sum. Let's consider all possible partitions into exactly k subsets, and for each such partition, sum the squares of the sizes of the subsets. Then, the total is the sum over all such partitions of sum_S |S|^2.

To compute this sum, perhaps there's a combinatorial approach. Let's think about each pair of elements. For a given pair (i, j), in how many partitions are they in the same subset? Because when they are in the same subset, that subset's size contributes (i and j) to the sum of squares. For example, if a subset has size s, then in the sum of squares, it contributes s^2. Each pair of elements in that subset contributes 2 (since sum_{i < j} 1 if in same subset) plus the individual terms (each element's own 1 in the square). Wait, the sum of squares can be written as sum_S ( sum_{x in S} 1 )^2 = sum_S ( sum_{x in S} 1 + 2 sum_{x < y in S} 1 ) ). So sum_S |S|^2 = sum_S |S| + 2 sum_S sum_{x < y in S} 1. So overall sum over all partitions of sum_S |S|^2 is equal to sum over all partitions of (sum_S |S|) + 2 sum_{x < y} [x and y are in the same subset in the partition]. But sum_S |S| is equal to n for each partition (since it's a partition into subsets). So the first term is S(n, k) * n. The second term is 2 * sum_{x < y} the number of partitions into k subsets where x and y are in the same subset.

So total sum over all partitions of sum_S |S|^2 is S(n, k) * n + 2 * sum_{x < y} f(x,y), where f(x,y) is the number of partitions into k subsets where x and y are in the same subset.

But this sum is equal to n*C, as each element's contribution is C, and there are n elements.

So:

n * C = S(n, k) * n + 2 * sum_{x < y} f(x,y)

But how to find sum_{x < y} f(x,y).

Let's compute f(x,y) for a fixed x and y. How many partitions into k subsets have x and y in the same subset?

Well, to compute f(x,y), we can think that x and y are in the same subset. So we can merge x and y into a single "element", then we need to partition the remaining n-1 elements (the merged element plus the remaining n-2) into k-1 subsets, but wait. No: merging x and y into a single element would leave us with n-1 elements. The number of partitions into k subsets is S(n-1, k). So f(x,y) = S(n-1, k). But wait, that's not correct. Because merging x and y and partitioning into k subsets would require that the merged element is in a subset. So the number of partitions where x and y are in the same subset is S(n-1, k). Because when you group x and y together, you have n-1 elements (the merged group, and the others). Then, the number of ways to split into k subsets is S(n-1, k). But wait, the original problem requires the partitions into exactly k subsets. So if merging x and y into one element, the merged element plus the remaining n-2 elements must be partitioned into k subsets. So the number of partitions where x and y are in the same subset is S(n-1, k) (since the merged element is part of one subset, and the rest are split into k-1 subsets). Wait, maybe not. Let me think again.

Suppose x and y are in the same subset. Then, the rest of the elements are partitioned into k-1 subsets. So the entire partition is formed by the subset containing x and y, and the k-1 other subsets. The subset containing x and y can have any size >=2, and the rest must form k-1 subsets. So the number of such partitions is S(n-1, k-1). Because merging x and y into a single element, then the number of ways to partition the merged element plus the remaining n-2 elements into k-1 subsets. Wait, no. Wait, the merged element (x and y) is one element. So the problem reduces to partitioning n-1 elements (original elements except x and y, plus the merged element) into k subsets. So the number of partitions where x and y are in the same subset is S(n-1, k). Because the merged element is treated as a single element. For example, when we merge two elements, the number of partitions into k subsets is S(n-1, k). So f(x,y) = S(n-1, k).

So sum_{x < y} f(x,y) = C(n, 2) * S(n-1, k).

Wait, but in that case:

nC = S(n,k) * n + 2 * C(n, 2) * S(n-1, k)

So solving for C:

C = [ S(n,k) * n + 2 * C(n,2) * S(n-1, k) ] / n

= S(n,k) + (2 * C(n,2) * S(n-1, k)) /n 

But 2*C(n,2)/n = (2*(n(n-1)/2)) )/n = (n(n-1)) /n ) = (n-1)

So:

C = S(n, k) + (n-1) * S(n-1, k)

Ah! So this is a key insight. Therefore, C can be expressed as S(n, k) + (n-1) * S(n-1, k).

But wait, this is a neat formula. So we can compute C as S(n, k) + (n-1)*S(n-1, k).

So now, the problem reduces to calculating S(n, k) and S(n-1, k), multiply the latter by (n-1), add to the former, multiply by the sum of the w_i's, and then take modulo 1e9+7.

But wait, this is for the sum over all partitions of the sum of the squares of the subset sizes. But according to the previous equation:

nC = S(n,k) * n + 2 * C(n,2) S(n-1, k)

so C = S(n,k) + (n-1) S(n-1, k)

So that's the formula for C. So now, the answer is sum(w_i) * (S(n, k) + (n-1) * S(n-1, k)) mod 1e9+7.

Therefore, the problem now is to compute S(n, k) and S(n-1, k).

But how to compute Stirling numbers of the second kind for large n (up to 2e5).

Wait, Stirling numbers of the second kind S(n, k) can be computed using the recurrence S(n, k) = k*S(n-1, k) + S(n-1, k-1), with base cases S(0, 0) = 1, S(n, 0) = 0 for n>0, S(0, k) =0 for k>0.

But for n up to 2e5 and k up to 2e5, computing this directly using DP is impossible because it's O(nk) time and space.

So we need a way to compute S(n, k) mod 1e9+7 for n up to 2e5 and k up to 2e5.

But there's an inclusion-exclusion formula for Stirling numbers of the second kind. The formula is:

S(n, k) = (1/k!) ) sum_{i=0}^k (-1)^(k-i) * C(k, i) * i^n 

This formula is derived from the inclusion-exclusion principle. So, for each k, S(n, k) can be computed as sum_{i=0 to k} (-1)^i * C(k, i) * (k -i)^n } divided by k! ?

Wait, no. Let me check the correct formula. The explicit formula is:

S(n, k) = (1/k! ) * sum_{i=0}^k (-1)^{k-i} * C(k, i) * i^n }

Yes. Because the inclusion-exclusion approach counts the number of onto functions from an n-element set to a k-element set, and then divides by k! to account for the labeling of the subsets.

But in our case, the partitions are unordered, so S(n, k) is exactly this value. So the formula holds.

So for S(n, k), the formula is sum_{i=0 to k} (-1)^i * C(k, i) * (k -i)^n } / (k! ) ?

Wait, let me recheck.

The standard formula for S(n, k) is:

S(n, k) = (1/k! ) sum_{i=0}^k (-1)^{k-i} C(k, i) i^n 

Yes. Because for each i from 0 to k, we subtract and add accordingly. So this formula allows us to compute S(n, k) in O(k) time per call, which is manageable for k up to 2e5.

So for the problem, we need to compute S(n, k) and S(n-1, k), each with k up to 2e5.

But wait, when k is up to 2e5 and n up to 2e5, then the sum over i from 0 to k of (-1)^{i} * C(k, i) * (k-i)^n mod MOD.

So how to compute this sum.

Let's precompute factorials and inverse factorials up to 2e5, and then compute the sum for each case.

But for each S(n, k) computation, we need to compute the sum for i from 0 to k of (-1)^i * C(k, i) * (k -i)^n.

Wait, no. Wait, the formula is sum_{i=0}^k (-1)^{k-i} C(k, i) i^n } / k! ?

Wait, the correct formula is:

S(n, k) = (1/k!) * sum_{i=0}^k (-1)^{k-i} * C(k, i) * i^n } 

Alternatively, replacing i with k - j:

sum_{j=0}^k (-1)^j * C(k, j) * (k -j)^n 

divided by k! ?

Yes. Because substituting j = k -i. Then i runs from 0 to k, j =k-i, which runs from k to 0. So the sum can be rewritten as sum_{j=0}^k (-1)^{j} C(k, j) (k-j)^n. 

So yes, the formula is:

S(n, k) = (sum_{j=0}^k (-1)^j * C(k, j) * (k-j)^n ) / (k! )

Therefore, for each S(n, k), we need to compute this sum.

The problem is to compute this sum for two values: n and n-1.

So for each of S(n, k) and S(n-1, k), compute the sum and divide by k! modulo MOD.

But how to compute this sum efficiently.

Given that k can be up to 2e5, and for each term in the sum, we need to compute C(k, j) * (-1)^j * (k-j)^n.

But for j from 0 to k, (k-j) can vary from k down to 0. So (k-j)^n mod MOD can be computed as (k-j)^n mod MOD. But for large n, we can compute this using fast exponentiation (binary exponentiation), but j ranges up to 2e5, which is a problem. Because for each j, we have to compute (k-j)^n mod MOD. For j up to 2e5, this is O(k) per S(n, k) calculation. But since we need to compute this for two different n (n and n-1), the total time for each j would be O(k) for each of the two exponents.

But for n up to 2e5 and k up to 2e5, this would be O(k) per S(n, k), which would be 2e5 operations for each S(n, k). Since we need to compute two such S values, this would be 4e5 operations, which is acceptable for Python's time constraints (2 seconds can handle around 2e8 operations, but this is 4e5, which is manageable).

But wait, exponentiating for each j is O(log n) time. So for each j, (k-j)^n is computed in O(log n) time. But for k=2e5, this would be O(2e5 * log n) operations. For n=2e5, log2(n) is around 18, so 2e5 * 18 = 3.6e6 operations per S(n, k). For two S values, this would be 7.2e6 operations. Which is manageable.

So the plan is:

1. Precompute factorials and inverse factorials up to 2e5.

2. For S(n, k) and S(n-1, k):

   a. Compute sum_j [ (-1)^j * C(k, j) * (k-j)^n ] for j from 0 to k.

   b. Divide the sum by k! modulo MOD.

3. Compute C = (S(n, k) + (n-1) * S(n-1, k)) mod MOD.

4. Multiply C by the sum of the w_i's mod MOD.

5. Output the result.

Now, let's see how to implement this.

First, precompute factorials and inverse factorials up to 2e5.

We need to compute C(k, j) for j from 0 to k. C(k, j) can be computed as fact[k] * inv_fact[j] * inv_fact[k-j] mod MOD.

So for each j in 0..k, C(k, j) is fact[k] * inv_fact[j] * inv_fact[k-j] mod MOD.

So, for each j, compute term = (-1)^j * C(k,j) * (k-j)^n.

Sum all these terms for j from 0 to k.

But how to compute (k-j)^n mod MOD?

But when k-j is 0, (k-j)^n is 0^n. So when j =k, then (k-j) is 0. So for j=k, (0)^n is 0, unless n=0, which is not our case (n >=k >=1). So j=k term is 0. So the sum can be computed for j from 0 to k-1, and then j=k term is zero.

So, for j in 0 to k:

term = (-1)^j * C(k,j) * (k-j)^n mod MOD.

But when k-j is zero, the term is zero, so we can ignore j=k.

So for j from 0 to k-1:

sum += (-1)^j * C(k,j) * pow(k-j, n, MOD).

So, in code, for each j in 0 to k:

if j > k: continue (but j is up to k).

But wait, j can be up to k. But when j=k, k-j=0, so (k-j)^n=0. So we can loop j from 0 to k, but for j=k, the term is zero. So in practice, loop j from 0 to k, but in code, when j=k, the term is zero and can be skipped.

But for code, perhaps loop j from 0 to min(k, k), but j=k can be included, but since (k-j) is zero, the term is zero. So, no problem.

So the steps are:

Compute S(n, k) as follows:

sum = 0

for j in 0 to k:

   c = comb(k, j) = fact[k] * inv_fact[j] * inv_fact[k-j] mod MOD

   term = (-1)^j * c * pow(k-j, n, MOD)

   sum = (sum + term) % MOD

sum = sum * inv_fact[k] mod MOD

Similarly for S(n-1, k), replace n with n-1.

But how to compute (-1)^j?

In code, we can represent (-1)^j as 1 if j is even, -1 otherwise. But in mod arithmetic, -1 is equivalent to MOD-1. So, for each j:

sign = 1 if j is even else -1.

But since we're working mod MOD, which is 1e9+7, we can precompute the sign as follows: sign = (MOD - 1) * (j % 2) ? No. Wait, for even j: sign is 1. For odd j: sign is -1 mod MOD.

So for j even: sign is 1. For j odd: sign is MOD-1.

So in code:

sign = 1 if j % 2 == 0 else MOD - 1

So the term becomes (sign * c * pow(k-j, n, MOD)) % MOD.

But when j is even, sign is 1. When j is odd, sign is MOD-1.

Now, the key is to precompute fact and inv_fact up to 2e5.

So, let's code this.

First, precompute fact and inv_fact up to 2e5.

MOD = 10**9+7.

Max_n is 2e5.

fact = [1] * (max_n +1)

for i in 2 to max_n:

   fact[i] = fact[i-1] * i % MOD.

inv_fact = [1]*(max_n+1)

inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

for i in max_n-1 downto 0:

   inv_fact[i] = inv_fact[i+1] * (i+1) % MOD.

Then, to compute C(k, j):

if j <0 or j >k: 0.

else: fact[k] * inv_fact[j] * inv_fact[k-j] % MOD.

So, in code, for each j in 0..k:

c = fact[k] * inv_fact[j] % MOD

c = c * inv_fact[k-j] % MOD.

Then, compute term as (sign * c * pow(k-j, n, MOD)) % MOD.

But pow(k-j, n, MOD) can be computed as pow(k-j, n, MOD). For exponents up to 2e5, this is feasible.

But for large exponents, like 2e5, pow in Python is optimized and should be fast.

So putting this all together.

So the steps are:

Read n, k.

Read list of w_i.

Compute sum_w = sum(w_i) mod MOD.

If k ==0: not possible (since k >=1 per constraints).

But according to the problem statement, 1<=k <=n.

So compute S(n, k) and S(n-1, k) using the formula.

Compute C = (S(n, k) + (n-1)*S(n-1, k)) % MOD.

Answer is (sum_w * C) % MOD.

Now, what if k=0? According to the constraints, k is at least 1.

So now, the code.

But wait, when k >n, then S(n, k) is zero. But per problem constraints, k <=n.

So we can proceed.

So the code:

But let's handle cases where k=0, but the input constraints say 1<=k<=n.

So the code steps:

Read n, k.

Read w list.

sum_w = sum(w_i) % MOD.

if sum_w is negative, adjust mod.

Compute S(n,k):

sum_stir = 0.

for j in 0 to k:

   c = comb(k, j) = fact[k] * inv_fact[j] * inv_fact[k-j] % MOD.

   sign = 1 if j%2 ==0 else MOD-1.

   term = sign * c % MOD.

   base = (k-j) if (k-j) >=0 else 0.

   power = pow(base, n, MOD).

   term = term * power % MOD.

   sum_stir = (sum_stir + term) % MOD.

sum_stir = sum_stir * inv_fact[k] % MOD.

Similarly for S(n-1, k):

sum_stir_nm1 =0.

for j in 0 to k:

   c = comb(k, j) ... same as before.

   sign = same.

   base = k-j.

   power = pow(base, n-1, MOD).

   term = sign * c * power % MOD.

   sum_stir_nm1 = (sum_stir_nm1 + term) % MOD.

sum_stir_nm1 = sum_stir_nm1 * inv_fact[k] % MOD.

Then compute C = (sum_stir + (n-1)*sum_stir_nm1) % MOD.

ans = (sum_w * C) % MOD.

But wait, the formula for S(n,k) is sum_stir = sum / k!.

So the code for S(n,k) is sum_stir = sum_terms * inv_fact[k] mod MOD.

Yes.

So in code:

But we need to precompute fact and inv_fact up to 2e5.

But for n up to 2e5, and k up to 2e5, that's manageable.

But in the problem, n can be up to 2e5, and k up to 2e5. So precompute fact and inv_fact up to 2e5.

So code outline:

MOD = 10**9 +7

n, k = map(int, input().split())

w = list(map(int, input().split()))

sum_w = sum(w) % MOD

max_fact = max(k, n) # ?

But if k can be up to 2e5, and n can be up to 2e5, then precompute up to 2e5.

max_n = 2e5 → 200000.

But in Python, precomputing up to 2e5 is manageable.

But wait, in code, let's generate fact and inv_fact up to 2e5.

But 2e5 is 200,000. Precomputing that.

So:

MOD = 10**9 +7

n, k = map(int, input().split())

w = list(map(int, input().split()))

sum_w = sum(w) % MOD

# Precompute factorial and inverse factorial up to 2e5.

max_fact = 2 * 10**5

fact = [1] * (max_fact +1)

for i in range(1, max_fact+1):

    fact[i] = fact[i-1] * i % MOD

inv_fact = [1]*(max_fact +1)

inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)

for i in range(max_fact-1, -1, -1):

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

Then, compute S(n, k):

def compute_S(m, k_val):

    if k_val ==0:

        return 0 if m ==0 else 0

    sum_terms =0

    for j in range(0, k_val+1):

        # compute C(k_val, j)

        if j > k_val or j <0:

            continue

        c = fact[k_val] * inv_fact[j] % MOD

        c = c * inv_fact[k_val -j] % MOD

        sign = 1 if j%2 ==0 else MOD -1

        base = (k_val -j)

        power = pow(base, m, MOD)

        term = sign * c % MOD

        term = term * power % MOD

        sum_terms = (sum_terms + term) % MOD

    inv_k_fact = inv_fact[k_val]

    res = sum_terms * inv_k_fact % MOD

    return res

S_n_k = compute_S(n, k)

S_nm1_k = compute_S(n-1, k)

C = (S_n_k + (n-1) * S_nm1_k) % MOD

ans = sum_w * C % MOD

print(ans)

Wait, but in the case where k=1, then S(n, 1) is 1, S(n-1, 1) is 1.

So C = 1 + (n-1)*1 = n.

sum_w *n → sum of all subset's weights. Which makes sense, because when k=1, there's only one partition (the entire set). The weight is |S|*sum(w_i) = n*sum(w_i). So the sum is n*sum(w_i). Which matches.

So this formula works.

Another test case. First sample input:

n=4, k=2.

Compute S(4,2):

Using the formula:

sum_{j=0}^2 (-1)^j * C(2,j) * (2-j)^4.

But 2-j can be 2,1,0.

j=0: C(2,0)=1. sign=1. term=1*1*2^4=16.

j=1: C(2,1)=2. sign=-1. term= (-1)*2*1^4= -2.

j=2: C(2,2)=1. sign=1. term=1*1*0^4=0.

sum_terms =16-2=14.

Divide by 2! (2) → 14/2=7. So S(4,2)=7.

Then S(n-1=3, 2):

sum j=0 to 2:

j=0: C(2,0)=1. sign=1. (2-0)^3=8 → 8*1*1=8.

j=1: C(2,1)=2. sign=-1. (2-1)^3=1. term= (-1)*2*1= -2.

j=2: 0^3=0. term=0.

sum_terms=8-2=6. Divided by 2 → 3. So S(3,2)=3.

C=7 + (4-1)*3 =7 +9=16.

sum_w=10 → 16*10=160. Which matches the first sample.

So the code works.

But what about cases where k=2 and n=5, like the second sample.

Sample input 2:

5 2.

sum_w=15.

S(5,2) is 15.

S(4,2) is 7.

C=15 + 4*7=15+28=43.

43 *15=645, which matches the second sample.

So code works.

But how to optimize the code to handle large k and n.

The code precomputes factorials up to 2e5. For each S(m, k), it loops from j=0 to j=k, which can be up to 2e5 steps. But for each j, the calculation is O(1), except for the pow operation, which is O(log m) time. But in Python, the pow function is optimized and very fast, especially for exponents that are 2e5.

But when m is 2e5 and j is 2e5, then (k-j) could be negative. Wait, no. Because j ranges up to k, and k <=n. So if j is up to k, then (k-j) is >=0. For example, when j=0, (k-j) is k. When j=k, (k-j)=0.

So base is always non-negative.

So code is correct.

Now, the code must be written, and in Python, but with the precomputation of fact and inv_fact up to 2e5.

But wait, for the problem constraints, n can be up to 2e5, but k can be up to n, so up to 2e5. So the precomputed fact up to 2e5 is sufficient.

But the code may need to precompute fact up to k, which could be up to 2e5.

Yes, because in the code, when k is up to 2e5, the fact and inv_fact arrays up to 2e5 are sufficient.

So the code should work.

But in Python, for n up to 2e5, precomputing the factorials is feasible.

So the code is:

But the code as written would have functions compute_S(m, k_val) that loops from j=0 to k_val, which can be up to 2e5 iterations. Each iteration involves a few modular operations and a pow call.

But for two compute_S calls (for m =n and m =n-1), that's 2*2e5 =4e5 iterations, which is acceptable.

But in practice, when k is 2e5, each compute_S call would loop 2e5+1 times. Which is 2e5+1 iterations. But for 2e5+1, that's 2e5 steps.

So for two S calculations, that's 4e5 steps, each with O(1) operations except for the pow. The pow for (k-j) to the m-th power. For m up to 2e5, and (k-j) up to 2e5, but in Python, pow is optimized. So for each term, pow(base, m, MOD) is O(log m) time. For each j in 0..k, this is O(k log m) per S call. For k=2e5 and log m=18, that's 2e5 * 18 =3.6e6 operations per S call, which multiplied by two gives 7.2e6 operations. Which is acceptable for Python in 2 seconds.

But perhaps we can precompute the powers (k-j) for j from 0 to k, and m and m-1. But not sure.

Alternatively, for each j, compute (k-j)^n and (k-j)^{n-1} in the same loop.

But that would save some computation time.

In the code above, when we compute S(n, k) and S(n-1, k), we can compute both in a single loop over j. But since they are separate functions, perhaps not. But perhaps merging the two computations can save time.

Alternatively, precompute all (k-j)^n and (k-j)^{n-1} for j from 0 to k.

But in code, perhaps for each j in 0 to k:

base = k-j

pow_n = pow(base, n, MOD)

pow_nm1 = pow(base, n-1, MOD)

then for S(n,k) use pow_n, and S(n-1,k) use pow_nm1.

But this would require looping j once, and calculating both exponents.

But this would save time as the loop is done once instead of twice.

Yes. So the code can be optimized by combining the two S computations into a single loop over j.

But how?

Let me think.

We need to compute sum_terms for S(n, k) and sum_terms for S(n-1, k).

In the current code, the code calls compute_S(n, k) and compute_S(n-1, k) separately, which would loop j twice.

But perhaps in a single loop over j, compute both terms.

So:

sum_stir =0

sum_stir_nm1=0

for j in 0 to k:

   compute C(k,j)

   sign is 1 if j even else MOD-1

   base =k-j

   pow_n = pow(base, n, MOD)

   pow_nm1 = pow(base, n-1, MOD) if base !=0 else 0

   term_n = sign * C(k,j) * pow_n % MOD

   sum_stir += term_n

   if base !=0:

       term_nm1 = sign * C(k,j) * pow_nm1 % MOD

   else:

       term_nm1 =0

   sum_stir_nm1 += term_nm1

sum_stir = sum_stir * inv_fact[k] % MOD

sum_stir_nm1 = sum_stir_nm1 * inv_fact[k] % MOD

This would save one loop over j, which for k=2e5 is 2e5 steps.

So this would be more efficient.

So modifying the code:

def compute_S_both(m, m_minus1, k_val):

    sum_terms_m =0

    sum_terms_m_minus1 =0

    for j in range(0, k_val+1):

        if j > k_val:

            continue

        c = fact[k_val] * inv_fact[j] % MOD

        c = c * inv_fact[k_val -j] % MOD

        sign = 1 if j%2 ==0 else MOD -1

        base = k_val -j

        if base ==0:

            pow_m =0

            pow_m_minus1 =0

        else:

            pow_m = pow(base, m, MOD)

            if m_minus1 >=0:

                pow_m_minus1 = pow(base, m_minus1, MOD)

            else:

                # but m_minus1 is n-1, which is >=k-1 >=0 since k <=n.

                # So m_minus1 is >=0.

                pow_m_minus1 =0

        term_m = sign * c % MOD

        term_m = term_m * pow_m % MOD

        sum_terms_m = (sum_terms_m + term_m) % MOD

        term_m_minus1 = sign * c % MOD

        term_m_minus1 = term_m_minus1 * pow_m_minus1 % MOD

        sum_terms_m_minus1 = (sum_terms_m_minus1 + term_m_minus1) % MOD

    inv_k_fact = inv_fact[k_val]

    res_m = sum_terms_m * inv_k_fact % MOD

    res_m_minus1 = sum_terms_m_minus1 * inv_k_fact % MOD

    return res_m, res_m_minus1

Then, in the main code:

S_n_k, S_nm1_k = compute_S_both(n, n-1, k)

But wait, m is n, m_minus1 is n-1. But in the code, for S(n, k) and S(n-1, k), we need to compute for m and m-1.

Yes. So the code would compute both sums in one loop.

This would halve the number of iterations, which is a significant optimization.

So the code can be modified to compute both S(n, k) and S(n-1, k) in a single loop.

This is the optimized approach.

So, integrating this into the code:

MOD = 10**9 +7

n, k = map(int, input().split())

w = list(map(int, input().split()))

sum_w = sum(w) % MOD

max_fact = 2 * 10**5

fact = [1] * (max_fact +1)

for i in range(1, max_fact+1):

    fact[i] = fact[i-1] * i % MOD

inv_fact = [1]*(max_fact +1)

inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)

for i in range(max_fact-1, -1, -1):

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def compute_S_both(k_val):

    sum_terms_m =0

    sum_terms_m_minus1 =0

    for j in range(0, k_val+1):

        if j > k_val:

            continue

        c = fact[k_val] * inv_fact[j] % MOD

        c = c * inv_fact[k_val -j] % MOD

        sign = 1 if j%2 ==0 else MOD -1

        base = k_val -j

        if base ==0:

            pow_n =0

            pow_nm1 =0

        else:

            pow_n = pow(base, n, MOD)

            pow_nm1 = pow(base, n-1, MOD)

        term_n = sign * c % MOD

        term_n = term_n * pow_n % MOD

        sum_terms_m = (sum_terms_m + term_n) % MOD

        term_nm1 = sign * c % MOD

        term_nm1 = term_nm1 * pow_nm1 % MOD

        sum_terms_m_minus1 = (sum_terms_m_minus1 + term_nm1) % MOD

    inv_k_fact = inv_fact[k_val]

    res_m = sum_terms_m * inv_k_fact % MOD

    res_m_minus1 = sum_terms_m_minus1 * inv_k_fact % MOD

    return res_m, res_m_minus1

if k ==0:

    print(0)

else:

    S_n_k, S_nm1_k = compute_S_both(k)

    C = (S_n_k + (n-1)*S_nm1_k) % MOD

    ans = sum_w * C % MOD

    print(ans)

This should work.

But what about when k=0? According to the problem constraints, k is at least 1. So the code can omit handling k=0.

But in the code, the 'if k==0' part can be removed.

So the final code is:

MOD = 10**9 +7

n, k = map(int, input().split())

w = list(map(int, input().split()))

sum_w = sum(w) % MOD

max_fact = 2 * 10**5

fact = [1] * (max_fact +1)

for i in range(1, max_fact+1):

    fact[i] = fact[i-1] * i % MOD

inv_fact = [1]*(max_fact +1)

inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)

for i in range(max_fact-1, -1, -1):

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def compute_S_both(k_val):

    sum_terms_m =0

    sum_terms_m_minus1 =0

    for j in range(k_val+1):

        c = fact[k_val] * inv_fact[j] % MOD

        c = c * inv_fact[k_val -j] % MOD

        sign = 1 if j %2 ==0 else MOD-1

        base = k_val -j

        if base ==0:

            pow_n =0

            pow_nm1 =0

        else:

            pow_n = pow(base, n, MOD)

            pow_nm1 = pow(base, n-1, MOD)

        term_n = (sign * c) % MOD

        term_n = term_n * pow_n % MOD

        sum_terms_m = (sum_terms_m + term_n) % MOD

        term_nm1 = (sign * c) % MOD

        term_nm1 = term_nm1 * pow_nm1 % MOD

        sum_terms_m_minus1 = (sum_terms_m_minus1 + term_nm1) % MOD

    inv_k_fact = inv_fact[k_val]

    res_m = sum_terms_m * inv_k_fact % MOD

    res_m_minus1 = sum_terms_m_minus1 * inv_k_fact % MOD

    return res_m, res_m_minus1

S_n_k, S_nm1_k = compute_S_both(k)

C = (S_n_k + (n-1) * S_nm1_k) % MOD

ans = sum_w * C % MOD

print(ans)

This should handle all cases correctly.

Now, let's test the sample inputs.

First sample input:

4 2

2 3 2 3 → sum_w is 10.

In code, compute_S_both(2):

loop j=0,1,2.

j=0:

c = 2! * inv_fact[0] * inv_fact[2-0} → 2 * 1 * 1/2! → 2! is 2, inv_fact[0] is 1, inv_fact[2] is 500000004 (since 2! =2, inv 2 mod 1e9+7 is 500000004).

Wait, no: inv_fact[2] is 500000004.

So C(2,0) = fact[2] * inv_fact[0] * inv_fact[2] → 2 *1 * 500000004 = 2 * 500000004 mod MOD → 1.

sign is 1.

base=2.

pow_n = 2^4 =16 mod MOD.

pow_nm1=2^3=8.

term_n = 1 * 1 *16 =16.

term_nm1 = 1*1*8=8.

sum_terms_m =16.

sum_terms_m_minus1=8.

j=1:

c= C(2,1) = 2 choose 1 → 2.

sign is MOD-1 → -1 mod MOD.

base=2-1=1.

pow_n =1^4=1.

term_n = (-1) * 2 *1 → -2 mod MOD → 1e9+6 -1 = 1e9+6-1= 1e9+5.

sum_terms_m = 16 + (MOD-2) =14.

sum_terms_m_minus1: term_nm1 is (-1)*2 *1^3= -2. sum is 8-2=6.

j=2:

base=0 → pow_n =0, pow_nm1=0.

terms are zero.

sum_terms_m is 14.

sum_terms_m_minus1 is6.

Then multiply by inv_fact[2] → 500000004.

So S(n,k) =14 * 500000004 mod MOD → 14/2=7.

S(n-1, k) is 6 * 500000004 → 6/2=3.

C=7 +3*(4-1)=7+9=16.

sum_w *16 =10*16=160.

Which matches the first sample.

Second sample:

n=5, k=2.

sum_w=15.

compute_S_both(2):

j ranges 0-2.

j=0:

c=1.

sign=1.

base=2.

pow_n=2^5=32.

term_n=32.

pow_nm1=2^4=16.

sum_terms_m=32.

sum_terms_m_minus1=16.

j=1:

c=2.

sign=-1.

base=1.

pow_n=1.

term_n= -2*1 =-2.

sum_terms_m=32-2=30.

pow_nm1=1.

term_nm1= -2*1=-2. sum_terms_m_minus1=16-2=14.

j=2: base=0. terms are 0.

sum_terms_m=30, sum_terms_m_minus1=14.

inv_fact[2] is 500000004.

S(n,k) =30 *500000004 mod MOD → 15.

S(n-1,k) =14 *500000004 mod MOD →7.

C=15 +4*7=15+28=43.

sum_w=15 → 15*43=645.

Which matches the second sample.

So the code works.

Thus, the final code is as written.
</think>

```python
MOD = 10**9 + 7

n, k = map(int, input().split())
w = list(map(int, input().split()))
sum_w = sum(w) % MOD

max_fact = 200000
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
for i in range(max_fact - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def compute_S_both(k_val):
    sum_terms_m = 0
    sum_terms_m_minus1 = 0
    for j in range(k_val + 1):
        c = fact[k_val] * inv_fact[j] % MOD
        c = c * inv_fact[k_val - j] % MOD
        sign = 1 if j % 2 == 0 else MOD - 1
        base = k_val - j
        if base == 0:
            pow_n = 0
            pow_nm1 = 0
        else:
            pow_n = pow(base, n, MOD)
            pow_nm1 = pow(base, n-1, MOD)
        term_n = (sign * c) % MOD
        term_n = term_n * pow_n % MOD
        sum_terms_m = (sum_terms_m + term_n) % MOD
        term_nm1 = (sign * c) % MOD
        term_nm1 = term_nm1 * pow_nm1 % MOD
        sum_terms_m_minus1 = (sum_terms_m_minus1 + term_nm1) % MOD
    inv_k_fact = inv_fact[k_val]
    res_m = sum_terms_m * inv_k_fact % MOD
    res_m_minus1 = sum_terms_m_minus1 * inv_k_fact % MOD
    return res_m, res_m_minus1

S_n_k, S_nm1_k = compute_S_both(k)
C = (S_n_k + (n-1) * S_nm1_k) % MOD
ans = sum_w * C % MOD
print(ans)
```