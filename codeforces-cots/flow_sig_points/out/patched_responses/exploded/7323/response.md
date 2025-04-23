<think>
Okay, let's tackle this problem. So the task is to compute the sum of f(l, r) over all possible subsegments of the array a. And each f(l, r) is the sum of the elements in the subarray when sorted, each multiplied by their 1-based index in the sorted array. Since the array can be up to 5e5 elements, we need a really efficient algorithm here. Brute-forcing all possible subarrays and sorting each would be O(n^2 log n), which is way too slow for n=5e5. So we need a smarter approach.

Hmm. Let's think about each element's contribution to the total sum. Since all elements are distinct, each element will be part of some sorted subarrays where it is in a certain position. So for each a_i, we need to find out in how many subarrays it appears as the k-th smallest element, and multiply that by a_i * k. Then sum all these contributions.

So the key is to find, for each element a_i, the number of subarrays where a_i is the m-th smallest (for various m), and multiply by m*a_i, then sum all these.

But how do we compute that efficiently?

Let's consider a single element x in the array. We want to find for how many intervals [l, r] that x is the k-th smallest element in the subarray a_l to a_r. Then the total contribution of x is x multiplied by the sum of k multiplied by the number of such intervals for all possible k.

But how to find that sum for each x?

Alternatively, maybe we can model the problem by considering each element x and determine how many times it contributes to the sum as the j-th element in the sorted subarray. For each occurrence of x in a sorted subarray, it contributes x * j, where j is its position in that sorted subarray.

So for each x, the total contribution is x multiplied by the sum over all possible j (positions in sorted subarrays) where x is in position j, multiplied by j, multiplied by the number of such subarrays where x is the j-th element.

So the problem reduces to, for each x in the array, compute the sum over j of (j * count_j) where count_j is the number of subarrays where x is the j-th smallest element. Then multiply each x by that sum and add all together.

But how to compute this sum for each x?

This seems challenging. Let's think differently. Let's sort all elements. Since all elements are distinct, their order is fixed. Suppose we process elements in sorted order. For each element x, we can find how many subarrays where x is the maximum element. Then for those subarrays, x contributes x multiplied by their length. Then, for elements that are not the maximum, their contribution would be in their respective positions. But perhaps there's a way to model this using the sorted order.

Wait, maybe for each element x, the total contribution can be determined by the number of intervals where x is included and is the k-th smallest in that interval. Then, the contribution is x multiplied by k multiplied by the number of such intervals.

But how to compute this for all x and all k?

Alternative approach: For each element x, find the number of subarrays where x is the m-th smallest element. Then sum over all x and all m, x * m * count. So the total sum is sum_{x} x * sum_{m} (m * c_{x,m}), where c_{x,m} is the count of subarrays where x is the m-th smallest.

The problem is how to compute c_{x,m} efficiently.

Hmm, perhaps using a monotonic stack approach similar to the problem of finding the sum of minimums over all subarrays. In that problem, for each element, you find how many subarrays where it is the minimum, which can be done by finding the next smaller and previous smaller elements. Then the count is (left * right) where left is the distance to the previous smaller element, and right to the next smaller.

But here, we need to track the m-th position. That seems more complex.

Wait, maybe we can model for each x, the number of subarrays where x is the k-th smallest, and then sum k * x * the count for each x and k. But how?

Another idea: For a given x, when it's part of a subarray, the sorted array will have x in some position. Let's consider all possible subarrays that include x and where x is the m-th smallest. To find how many such subarrays there are, perhaps we can look at the elements smaller than x and larger than x in the vicinity.

Wait, here's a possible approach inspired by the contribution of each element in sum over all subarrays. Let's process the elements in sorted order. For each element x, we can find the number of subarrays where x is the maximum. Then, since in the sorted subarray, x would be the last element, contributing x multiplied by the length of the subarray. Similarly, for each x, when it's the second maximum, the contribution would be x multiplied by (length - 1), but the count of such subarrays. But this approach only considers the maximum, not arbitrary positions.

Alternatively, perhaps each element's contribution can be calculated by considering how many times it is the k-th smallest in a subarray, for all k. But how?

Alternatively, perhaps for each element x, the total contribution is x multiplied by the sum over all subarrays that include x of the position of x in the sorted version of that subarray. Let's denote S(x) as the sum of the positions of x in all such subarrays. Then the answer is sum(x * S(x)).

So the problem reduces to computing S(x) for each x, then multiplying by x and summing.

So the key is to find S(x) for each x. How?

Let's think about how the position of x in a sorted subarray depends on the elements in that subarray. For a particular subarray [L, R] containing x (so L <= pos <= R, where pos is the index of x in the array), when we sort this subarray, x's position is equal to the number of elements in the subarray that are less than x plus 1. So for the subarray [L, R], the position of x is (k + 1), where k is the number of elements in [L, R] that are less than x. Therefore, S(x) is the sum over all [L, R] containing x of (k + 1), where k is the number of elements less than x in [L, R].

So S(x) = sum_{L <= pos <= R} ( (number of elements less than x in [L, R] ) + 1 )

Which can be split into two parts: sum (number of elements less than x in [L, R]) for all [L, R] containing x, plus the number of such [L, R] (since each contributes 1).

The number of subarrays containing x is the number of possible L (from 1 to pos) and R (from pos to n). So that's pos * (n - pos + 1). So the second part is pos * (n - pos + 1).

The first part is the sum over all subarrays [L, R] that include x of the number of elements less than x in [L, R].

So the total contribution for x is x * (sum_less + pos * (n - pos + 1)), where sum_less is the sum of the count of elements less than x in each subarray that includes x.

Now, the problem is to compute sum_less for each x.

But how to compute sum_less efficiently?

Let's consider that for each x, sum_less is equal to the sum over all elements y < x of the number of subarrays [L, R] that include x's position and y's position. Because each y < x in the subarray contributes 1 to the count of elements less than x.

So for each x, sum_less is the sum over all y < x of the number of subarrays [L, R] that include both x and y.

But since the array elements are all distinct, each y is either less than x or greater. So for a given x, the sum_less can be computed as the sum for all y < x of the number of subarrays that include both x and y.

Now, the number of subarrays that include both x and y is equal to (number of possible L choices) multiplied by (number of possible R choices). Let's say x is at position i, y is at position j. Then the subarray must have L <= min(i, j) and R >= max(i, j). So the number of L choices is min(i, j), and the number of R choices is (n - max(i, j) + 1). So the total for a particular y is min(i, j) * (n - max(i, j) + 1).

Wait, but for all pairs (x, y) where y < x, we need to sum min(x's pos, y's pos) * (n - max(x's pos, y's pos) + 1).

So for each x, sum_less is the sum over all y < x (y's value) of (left) * (right), where left is the minimum of x's and y's positions, and right is (n - maximum + 1).

But how to compute this efficiently for all x?

But if we can process the elements in sorted order, then for each x, after processing all smaller elements, we can keep track of their positions and compute this sum.

Wait, for example, sort the elements in increasing order. Then, for each x in this sorted list, when processing x, all elements processed so far are y < x. So for each such x, sum_less is the sum over all positions j of y (which are already known) of min(i, j) * (n - max(i, j) + 1), where i is the position of x.

So the problem reduces to, for each x at position i, compute the sum of min(i, j) * (n - max(i, j) + 1) for all j in a set S (the positions of elements y < x).

But how to compute this sum efficiently for all j in S?

Let's break down min(i, j) * (n - max(i, j) + 1):

Case 1: j <= i.

Then min(i,j) = j, max(i,j) = i. So the term is j * (n - i + 1).

Case 2: j > i.

Then min(i,j) = i, max(i,j) = j. The term is i * (n - j + 1).

So for each j in S, the contribution is:

if j <= i: j * (n - i + 1)

else: i * (n - j + 1)

So sum_less for x is (sum over j <= i in S of j*(n -i +1 )) + (sum over j > i in S of i*(n -j +1)).

Let's separate this into two parts:

sum_{j <= i} j * (n - i + 1) = (n -i +1) * sum_j_le_i j.

sum_{j > i} i * (n -j +1) = i * sum_{j >i} (n -j +1).

But n -j +1 is equal to (n+1 - j), so sum_{j >i} (n+1 -j) = sum_{k=1}^{n - i} k} where k = n+1 -j. For j >i, j ranges from i+1 to n. So k ranges from (n+1 - (i+1)) = (n -i) down to (n+1 -n) = 1. But the sum is the same as sum_{k=1}^{n -i} k} = (n -i)(n -i +1)/2.

Wait, no. For j >i, j can be from i+1 to n. Then (n+1 -j) for j from i+1 to n is (n - (i+1) +1) = n -i terms, starting from (n -i) down to 1. So sum (n+1 -j) from j=i+1 to n is sum_{k=1 to n -i} k} = (n-i)(n -i +1)/2.

So for the second part, sum_{j >i} (n -j +1) is (n-i)(n -i +1)/2.

Therefore, the second part sum becomes i * (n-i)(n-i+1)/2.

But wait, this is only when j is in S. So if S contains some j's <=i and some j's >i, but the j's in S are the positions of elements y <x. So when processing x, the elements y <x can be in any positions. So the sum_less is:

sum_{y <x} [ if j <=i then j*(n -i +1) else i*(n -j +1) ]

But this depends on j's positions relative to i.

So, for each x at position i, the sum_less is equal to:

sum_j_le_i (j) * (n -i +1) + sum_j_gt_i (n -j +1) * i.

But how to compute this for all j in S (the positions of elements less than x)?

If we can keep track of the sum of j for j in S where j <=i, and the sum of (n-j+1) for j in S where j>i, then for each x, we can compute the sum_less as:

sum_j_le_i = sum of j's in S and <=i.

sum_part1 = sum_j_le_i * (n -i +1)

sum_part2 = sum_{j_gt_i} (n -j +1) * i = i * sum_{j_gt_i} (n -j +1)

But sum_{j_gt_i} (n-j+1) is sum_{k=1 to (n-j)} where j starts from i+1. Wait, perhaps it's easier to precompute for each i.

Alternatively, when we process elements in sorted order, we can maintain two Fenwick trees (or prefix sums) for the positions. For example, for all j in S, we can track j (the positions) and compute sum_j_le_i and sum (n-j+1) for j >i.

Wait, perhaps we can split this into two parts:

For j <=i, j is added to sum_j_le_i.

For j >i, (n-j+1) is added to another sum.

So, for each x in sorted order (processing from smallest to largest), we can maintain two structures:

- a list of all j in S (positions of elements processed so far, which are <x).

Then, for each x at position i:

sum_j_le_i is the sum of all j in S where j <=i.

sum_gt_part is the sum of (n -j +1) for all j in S where j >i.

sum_part1 = sum_j_le_i * (n -i +1)

sum_part2 = i * sum_gt_part

sum_less = sum_part1 + sum_part2

So, how to efficiently compute sum_j_le_i and sum_gt_part?

This looks like a problem that can be solved with a Binary Indexed Tree (Fenwick Tree) or a Segment Tree. Since elements are processed in sorted order, their positions can be added to the data structure incrementally.

So, for each x in sorted order, when processing x, we can:

1. Query the sum of j where j <=i (i is x's position).

2. Query the sum of (n -j +1) where j >i.

Then compute sum_part1 and sum_part2.

But how to structure the Fenwick Tree to track these sums.

Alternatively, since we can precompute all the positions, we can represent the elements in a Fenwick Tree that tracks two values for each position j: j and (n-j+1).

But since the elements are processed in sorted order, and we need to process their positions, perhaps we can use two Fenwick Trees:

- One Fenwick Tree (FT1) that tracks for positions j: the count of j's (if they are in S), and the sum of j's. So for a query on sum of j's <=i, we can query the prefix sum up to i.

- Another Fenwick Tree (FT2) that tracks for positions j: the sum of (n-j+1) for positions j >i. To compute this sum for j >i, which is the same as the sum from j =i+1 to n of (n-j+1) if j is in S.

But how to compute the sum over j >i of (n-j+1) for j in S. This is equivalent to sum_{j in S, j >i} (n-j+1) = sum_{j in S} (n-j+1) if j>i.

But (n-j+1) can be rewritten as (n+1 -j). So sum_{j>i} (n+1 -j) = (n+1) * count_gt_i - sum_{j>i} j.

Where count_gt_i is the number of elements in S with j>i.

So if we can track the sum of j for j>i and the count of elements j>i, then sum_gt_part can be calculated as (n+1)*count_gt_i - sum_j_gt_i.

But how?

Alternatively, since (n-j+1) is (n+1 -j), we can track the sum of (n+1 -j) for j in S and j>i. This is equal to sum_{j in S, j>i} (n+1 -j) = sum (n+1) for j in S and j>i) - sum j for j in S and j>i.

Which is (n+1)*count_gt_i - sum_j_gt_i.

So if we can track sum_j_gt_i and count_gt_i, that would suffice.

Alternatively, perhaps we can precompute all the (n+1 -j) for all j, and then track the sum of those values for j in S and j>i. This sum can be computed using a Fenwick Tree that is built for the (n+1 -j) values.

But since j can be up to 5e5, it's feasible. Let's think:

We can use two Fenwick Trees (Fenwick Tree for sum of j's <=i and another Fenwick Tree for sum of (n+1 -j) for j>i.

Wait, here's a plan:

- For all elements, sorted in increasing order.

- For each element x in sorted order, with position i:

   sum_j_le_i = query FT_j.sum(1, i)

   sum_gt_part = query FT_ngt.sum(i+1, n)

   Then sum_part1 = sum_j_le_i * (n -i +1)

   sum_part2 = i * sum_gt_part

   sum_less = sum_part1 + sum_part2

   Then, S(x) = sum_less + (i * (n -i +1)), and the contribution is x * S(x).

   Then, add x's position i to both Fenwick Trees:

   - FT_j adds i to position i.

   - FT_ngt adds (n+1 -i) to position i.

So, the Fenwick Trees are:

- FT_j: keeps track of the sum of j's (positions) for elements processed so far (elements less than x).

- FT_ngt: keeps track of the sum of (n+1 -j) for elements processed so far (elements less than x).

When we process x, which is the next in the sorted order, all previous elements are smaller than x, so their positions are in S.

So, for each x at position i:

sum_j_le_i is the sum of all j in S (processed elements) where j <=i. That's FT_j's query up to i.

sum_gt_part is the sum of (n+1 -j) for all j in S where j >i. Which is FT_ngt's query from i+1 to n.

So sum_gt_part is the sum of (n+1 -j) for j >i. So sum_gt_part = FT_ngt.query(i+1, n).

So the sum_part2 is i * sum_gt_part.

Then, after processing x, we add i to FT_j and (n+1 -i) to FT_ngt.

This seems manageable.

So the steps are:

1. Sort the array elements along with their original indices (positions).

2. For each element in the sorted order:

   a. Get the position i of x.

   b. Query FT_j for sum of elements <=i → sum_j_le_i.

   c. Query FT_ngt for sum of elements in the range i+1 to n → sum_gt_part.

   d. sum_less = sum_j_le_i * (n -i +1) + i * sum_gt_part.

   e. The contribution for x is x * (sum_less + i*(n -i +1)).

   f. Update FT_j and FT_ngt by adding i and (n+1 -i), respectively.

3. Sum all contributions and take modulo 1e9+7.

This approach should be O(n log n), which is acceptable for n=5e5.

Now, let's verify this with the first example.

First example:

Input array is [5,2,4,7]. So positions are 1,2,3,4.

Sorted elements are 2 (pos 2),4 (pos3),5 (pos1),7 (pos4).

Processing each in order.

Processing 2 (pos=2):

FT_j and FT_ngt are empty. So sum_j_le_i is 0. sum_gt_part is 0. sum_less=0.

contribution is 2 * (0 + 2*(4-2+1)) → 2*(0 + 2*3) → 2*6=12. But wait, in the first example, the total for all f(l,r) is 167. Let's see:

But according to the first example, the answer is 167. Let's see how this approach would compute it.

Wait, for each x:

For x=2 (pos=2):

sum_less is 0. So S(x) is 0 + 2*3=6. Contribution is 2*6=12.

Then, adding pos 2 to FT_j and (4+1 -2) =3 to FT_ngt.

Processing 4 (pos=3):

sum_j_le_i (i=3): FT_j has 2. sum_j_le_i=2.

sum_gt_part: FT_ngt has 3 (from j=2). We query from 4? Wait, i is 3. So j>3. So in FT_ngt, query i+1=4 to 4. But the current j in S is 2, which is <3. So sum_gt_part is 0.

sum_part1 = 2*(4-3+1) → 2*2=4.

sum_part2 =3*0=0.

sum_less=4+0=4.

S(x)=4 + 3*(4-3+1) → 4 +3*2=10.

Contribution is 4*10=40. Total so far is 12+40=52.

Then, add pos 3 to FT_j (sum now 2+3=5) and (4+1-3)=2 to FT_ngt (sum now 3+2=5).

Processing 5 (pos=1):

sum_j_le_i (i=1): FT_j has elements 2 and3. But their positions are 2 and3, which are both >1. So sum_j_le_i is 0.

sum_gt_part: FT_ngt has entries for j=2 (3) and j=3 (2). i=1, so j>1 → sum from 2 to4. So sum_gt_part is 3+2=5.

sum_part1 =0 * (4-1+1) →0.

sum_part2=1*5=5.

sum_less=0+5=5.

S(x)=5 + 1*(4-1+1) =5 +1*4=9.

Contribution is5*9=45. Total now 52+45=97.

Then, add pos 1 to FT_j (sum now 1) and (4+1-1)=4 to FT_ngt (sum now 5+4=9).

Processing 7 (pos=4):

sum_j_le_i (i=4). FT_j has 2,3,1 → sum is 2+3+1=6.

sum_gt_part: FT_ngt has entries for j=2 (3), j=3 (2), j=1 (4). i=4, so j>4 is none. sum_gt_part is 0.

sum_part1=6*(4-4+1)=6*1=6.

sum_part2=4*0=0.

sum_less=6+0=6.

S(x)=6 +4*(4-4+1) →6 +4*1=10.

Contribution is7*10=70. Total sum is 97+70=167, which matches the example.

Yes! So the approach works for the first example.

Now, the next step is to implement this with Fenwick Trees.

Implementing Fenwick Trees that can compute prefix sums and ranges.

Each Fenwick Tree needs to support:

- update: add a value to a position.

- query: sum from 1 to x.

For the FT_ngt, which is used to compute sum from i+1 to n of (n+1 -j). This is equivalent to querying the sum in the range [i+1, n] in the Fenwick Tree. To compute this, since the Fenwick Tree can give sum up to x, sum from a to b is sum up to b minus sum up to a-1. So for i+1 to n, it's sum up to n (the entire tree's sum) minus sum up to i.

So for the FT_ngt, sum_gt_part = FT_ngt.query(n) - FT_ngt.query(i).

Thus, for each x at position i, sum_gt_part is FT_ngt.get_total() - FT_ngt.query(i).

Wait, but in the code, for the Fenwick Tree, the maximum index is n. So to get the sum from i+1 to n, it's query(n) - query(i).

So during processing:

sum_gt_part = ft_ngt.query(n) - ft_ngt.query(i).

So the Fenwick Trees need to support:

- update(pos, val): add val to the pos.

- query(x): sum from 1 to x.

Implementing Fenwick Tree in Python.

Now, for the elements, we need to sort them along with their original positions.

Once that's done, for each element in sorted order, process as per the steps.

So the code steps:

Read n.

Read the array a as a list.

Create a list of tuples (value, index), sorted by value.

Initialize two Fenwick Trees, ft_j and ft_ngt, each with size n.

Initialize the answer to 0.

MOD = 1e9+7.

For each (val, pos) in the sorted list:

   i = pos (since in Python, indices are 0-based or 1-based? Wait, the problem statement says the array is a_1, a_2, ... a_n, so positions are 1-based.)

Wait, the input's array is 1-based? Or in the code, the input is read as 0-based? Wait, the code will read the array as 0-based. Wait, no. The input is given as a_1, a_2, ..., a_n, which in the code would be read as a list, say, a[0], a[1], ... a[n-1], if using 0-based. But when the problem says position 1 refers to the first element, then in the code, the positions are 1-based.

So for the elements, the original positions are 1-based.

Thus, when creating the list of (value, pos), pos ranges from 1 to n.

So for example, the first example's input is 5, 2, 4,7. The positions are 1,2,3,4.

So when processing each element, we need to use 1-based positions.

Thus, in the code:

When reading the array, we can create a list of tuples (value, i+1) for i in range(n), since the input is 0-based in code, but the problem's positions are 1-based.

Now, the Fenwick Trees need to handle 1-based indices up to n.

So for each (val, pos) in the sorted list:

sum_j_le_i = ft_j.query(pos)

sum_gt_part = ft_ngt.query(n) - ft_ngt.query(pos)

sum_less = sum_j_le_i * (n - pos +1) + val * sum_gt_part * pos ?

Wait, no. Wait, sum_part2 is i * sum_gt_part. But i is the current position. So sum_part2 = pos * sum_gt_part.

sum_less = sum_j_le_i * (n - pos +1) + pos * sum_gt_part.

Then, S(x) = sum_less + (pos * (n - pos +1)).

Then, contribution is val * S(x).

So yes.

So in code:

sum_j_le_i = ft_j.query(pos)

sum_gt_part = ft_ngt.query(n) - ft_ngt.query(pos)

sum_less = sum_j_le_i * (n - pos +1) + pos * sum_gt_part

total_contribution = val * (sum_less + pos * (n - pos +1))

ans += total_contribution

Then, update the Fenwick Trees:

ft_j.update(pos, pos)  # because we need to add j (the position) to FT_j.

ft_ngt.update(pos, (n +1 - pos))  # add (n+1 -j) to FT_ngt.

But wait, the Fenwick Trees are initialized to 0. For each position j (the position of the current element being processed), we need to add j to FT_j, and (n+1 -j) to FT_ngt. So for each element in sorted order, when processing its position pos, we do:

ft_j.add(pos, pos)

ft_ngt.add(pos, (n +1 - pos))

Wait, but in the Fenwick Tree's update, perhaps the 'add' function is used to add a value to a position.

Thus, the code for the Fenwick Tree should support:

class FenwickTree:

    def __init__(self, size):

        self.n = size

        self.tree = [0] * (self.n + 1)

    def update(self, idx, delta):

        while idx <= self.n:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        res = 0

        while idx >0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

But wait, in Python, the indices for the Fenwick Tree are 1-based.

Thus, for a Fenwick Tree of size n, the valid indices are 1..n.

So in the code, when adding a position pos (which is 1-based), the code uses:

ft_j.update(pos, pos)

ft_ngt.update(pos, (n+1 - pos))

Yes.

So putting it all together:

Read n.

Read array a.

Sort a's elements with their original positions (1-based).

Initialize FenwickTree ft_j and ft_ngt with size n.

ans = 0

MOD = 10**9 +7

for val, pos in sorted list:

    sum_j_le_i = ft_j.query(pos)

    sum_gt_part = ft_ngt.query(n) - ft_ngt.query(pos)

    sum_less = sum_j_le_i * (n - pos +1) + pos * sum_gt_part

    s_x = sum_less + pos * (n - pos +1)

    contribution = val * s_x

    ans = (ans + contribution) % MOD

    ft_j.update(pos, pos)

    ft_ngt.update(pos, (n +1 - pos))

print(ans % MOD)

Now, test with the first example:

n=4, a = [5,2,4,7]

sorted list would be [(2,2), (4,3), (5,1), (7,4)]

Processing (2,2):

sum_j_le_i = ft_j.query(2) → 0.

sum_gt_part = ft_ngt.query(4) - ft_ngt.query(2) → 0 -0=0.

sum_less = 0*(4-2+1) + 2*0 =0.

s_x=0 + 2*(4-2+1) → 2*3=6 → contribution 2*6=12.

Then add pos 2 to ft_j (adds 2), and (4+1-2=3) to ft_ngt.

Processing (4,3):

sum_j_le_i = ft_j.query(3) → 2.

sum_gt_part = ft_ngt.query(4) - ft_ngt.query(3) → (3) - (3) →0. Because in ft_ngt, after first step, the entry at 2 is 3. For query(4) returns 3 (since all elements up to 4 are 2 and 3 is added). Wait, no. Let me see:

After processing (2,2):

ft_ngt has pos=2 added with 3. So ft_ngt's tree has 3 in position 2.

Now, when processing (4,3):

ft_ngt.query(4) is the sum up to 4. But only position 2 is filled. So sum up to 4 is 3.

sum_gt_part = 3 - ft_ngt.query(3) (sum up to 3, which is sum of pos 2 and 3. pos 3 is not added yet. So sum up to 3 is 3 (only pos 2 is in). So sum_gt_part=3-3=0.

sum_less = 2 * (4-3+1) → 2*2=4. + 3*0=0 → sum_less=4.

s_x=4 + 3*(4-3+1) →4 +3*2=10. Contribution 4*10=40. ans=12+40=52.

Add pos 3 to ft_j (add 3) and (4+1-3=2) to ft_ngt. Now ft_ngt has pos=2 (3) and pos=3 (2). So sum up to 4 is 3+2=5.

Processing (5,1):

sum_j_le_i = ft_j.query(1) → 0, since ft_j has 2 and 3 added. So sum up to 1 is 0.

sum_gt_part = ft_ngt.query(4) (5) - ft_ngt.query(1) (0) →5-0=5.

sum_less = 0*(4-1+1) →0*4=0. +1 *5 →5. sum_less=5.

s_x=5 +1*(4-1+1) →5 +4=9. Contribution 5*9=45. ans=52+45=97.

Add pos 1 to ft_j (adding 1) and (4+1-1=4) to ft_ngt. Now ft_ngt has positions 1 (4), 2 (3),3(2). sum up to 4 is 4+3+2=9.

Processing (7,4):

sum_j_le_i = ft_j.query(4). ft_j has 2,3,1. sum up to 4 is 2+3+1=6.

sum_gt_part = ft_ngt.query(4) (9) - ft_ngt.query(4) (9) → 0.

sum_less=6*(4-4+1) →6*1=6 +4*0=0 → sum_less=6.

s_x=6 +4*(1) →10. contribution 7*10=70. ans=97+70=167.

Which matches the first example.

Thus, the code works for the first example.

Now, test with the second example:

Input:

3

123456789 214365879 987654321

Sorted list would be [(123456789, 1), (214365879,2), (987654321,3)]

Processing each:

Processing 123456789 (pos=1):

sum_j_le_i is 0.

sum_gt_part is 0.

s_x=0 +1*(3-1+1) →1*3=3. contribution 123456789 *3.

Then add 1 to ft_j (sum_j now 1), and (3+1-1)=3 to ft_ngt.

Processing 214365879 (pos=2):

sum_j_le_i = ft_j.query(2) →1 (since pos=1 is in).

sum_gt_part = ft_ngt.query(3) (3) - ft_ngt.query(2) (3) →0.

sum_less=1*(3-2+1) →1*2=2. + 2*0=0 → sum_less=2.

s_x=2 +2*(3-2+1) →2+2*2=6. contribution 214365879*6.

Add pos=2 (j=2) to ft_j (sum_j now 1+2=3), and (3+1-2=2) to ft_ngt. Now ft_ngt has 3 (from pos1) and 2 (pos2).

Processing 987654321 (pos=3):

sum_j_le_i = ft_j.query(3) →1+2=3.

sum_gt_part = ft_ngt.query(3) (3+2) →5 - ft_ngt.query(3) (5) →5-5=0.

sum_less=3*(3-3+1) →3*1=3. +3*0=0 → sum_less=3.

s_x=3 +3*(3-3+1) →3+3*1=6. contribution 987654321 *6.

Total contribution:

123456789 *3 + 214365879 *6 + 987654321 *6.

But the sample output is 582491518.

But how does this calculation work modulo 1e9+7?

But perhaps the code handles it correctly.

So the code is correct.

Now, implement this in Python.

But for n up to 5e5, the Fenwick Tree must be efficient. Python's implementation should handle it, but we have to be careful with the code.

So the code steps:

Read n.

Read a list.

Create a list of (value, pos), where pos is 1-based.

Sort this list by value.

Initialize two Fenwick Trees of size n.

Process each element in order, compute the contribution as explained, and accumulate the answer.

Now, code:

Implement the FenwickTree class.

But in Python, for large n (5e5), the FenwickTree needs to be efficient.

But the code for FenwickTree is O(log n) per operation, which is acceptable.

Now, code:

MOD = 10**9 +7

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0]*(self.n +1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res =0
        while idx >0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

n = int(input())
a = list(map(int, input().split()))
elements = sorted( [(a[i], i+1) for i in range(n)] , key=lambda x: x[0])

ft_j = FenwickTree(n)
ft_ngt = FenwickTree(n)
ans =0

for val, pos in elements:
    sum_j_le_i = ft_j.query(pos)
    sum_gt_part = ft_ngt.query(n) - ft_ngt.query(pos)
    sum_less = sum_j_le_i * (n - pos +1) + pos * sum_gt_part
    s_x = sum_less + pos * (n - pos +1)
    contribution = val * s_x
    ans = (ans + contribution) % MOD
    ft_j.update(pos, pos)
    ft_ngt.update(pos, (n +1 - pos))

print(ans % MOD)

Yes, this should work.

Testing for the first sample input:

Input:

4

5 2 4 7

elements sorted are [(2,2), (4,3), (5,1), (7,4)]

Processing:

Each step as before.

The code should output 167.

Another sample input:

3

123456789 214365879 987654321

elements sorted by value:

123456789, 214365879, 987654321.

Their positions are 1,2,3.

Processing:

First element (123456789,1):

sum_j_le_i=0, sum_gt_part=0. s_x=0+1*(3) →3. contribution is 123456789*3 →370370367.

Then add pos 1 to ft_j and 3 to ft_ngt.

Second element (214365879,2):

sum_j_le_i= ft_j.query(2) →1 (since pos 1 is in ft_j). sum_gt_part= ft_ngt.query(3) - ft_ngt.query(2) →3 (from pos1) -3 (sum up to 2 is 3) →0. sum_less=1*(3-2+1) →1*2=2. s_x=2 +2*(2) →6. contribution 214365879*6 = 1286195274. sum ans is 370370367 +1286195274= 1656565641 mod 1e9+7 is 656565640+ 1e9+7= 656565640 + 1,000,000,007= 1,656,565,647 mod 1e9+7 is 656,565,640? Wait, maybe the code's calculation is correct.

Third element (987654321,3):

sum_j_le_i= ft_j.query(3) →1+2=3 (pos1 and pos2 added). sum_gt_part= ft_ngt.query(3) (3+2=5) - ft_ngt.query(3) →5-5=0. sum_less=3*(1) +3*0=3. s_x=3 +3*1=6. contribution 987654321 *6 =5,925,925,926 → mod 1e9+7.

Compute 5,925,925,926 mod 1e9+7.

1e9+7 is 1,000,000,007.

5,925,925,926 divided by 1e9+7:

5,925,925,926 = 5 * 1e9+7*5=5,000,000,035. Wait, 5,925,925,926 -5 *1e9+7=5*1e9+7=5,000,000,035. 5,925,925,926 -5,000,000,035= 925,925,891.

But 925,925,891 is less than 1e9+7. So contribution is 925,925,891.

So total ans is 370,370,367 + 1,286,195,274 = 1,656,565,641. Then adding 925,925,891 gives 2,582,491,532. Mod 1e9+7: 2,582,491,532 /1e9+7 is 2*1e9+7=2,000,000,014. Subtract that from 2,582,491,532 gives 582,491,518 → which matches the sample output.

Thus, the code works.
</think>

```python
MOD = 10**9 + 7

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

n = int(input())
a = list(map(int, input().split()))
elements = sorted([(val, i + 1) for i, val in enumerate(a)], key=lambda x: x[0])

ft_j = FenwickTree(n)
ft_ngt = FenwickTree(n)
ans = 0

for val, pos in elements:
    sum_j_le_i = ft_j.query(pos)
    total_ngt = ft_ngt.query(n)
    sum_gt_part = total_ngt - ft_ngt.query(pos)
    sum_less = sum_j_le_i * (n - pos + 1) + pos * sum_gt_part
    s_x = sum_less + pos * (n - pos + 1)
    contribution = val * s_x
    ans = (ans + contribution) % MOD
    ft_j.update(pos, pos)
    ft_ngt.update(pos, (n + 1 - pos))

print(ans % MOD)
```