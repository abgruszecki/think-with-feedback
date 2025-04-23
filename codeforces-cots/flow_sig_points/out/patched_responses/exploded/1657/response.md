<think>
Okay, let's tackle this problem. So the question is, given the types of fish caught by Alice and Bob, can we assign weights to each species such that Alice's total is strictly larger than Bob's? And the weights have to be in non-decreasing order as per the species numbers. So species 1 has the smallest weight, species 2's weight is equal or larger than 1, and so on up to species k.

Hmm. Let's think about what conditions would make this possible. The key here is that the weights are non-decreasing. So, for any two species i and j where i < j, w_i ≤ w_j. But we can choose the actual weights as any positive numbers as long as they satisfy this condition.

So the problem reduces to determining whether there's a way to assign these weights so that the sum of Alice's fish is greater than Bob's. How can we model this?

First, we need to compare the counts of each species in Alice's and Bob's collections. Let's consider each species and see how Alice's count compares to Bob's. For species x, if Alice has a_x fishes and Bob has b_x. The contribution of species x to the total sum is (a_x - b_x) * w_x. So the total sum difference is sum over all x of (a_x - b_x) * w_x. We need this sum to be > 0.

But the constraints are that w_1 ≤ w_2 ≤ ... ≤ w_k. So we need to assign the weights in such a way that maximizes this sum difference. But how?

Wait, the problem isn't to find the maximum possible sum difference, but to determine if there exists any assignment of weights (satisfying the non-decreasing condition) where the sum difference is positive. So we need to see if there's at least one way.

Let's think of the optimal scenario for Alice. To maximize the sum difference, Alice should have as many as possible of higher species (since their weights can be larger) where a_x > b_x, and as few as possible of lower species where a_x < b_x. But the weights are constrained to be non-decreasing. So perhaps the best way is to assign the maximum possible weights to species where Alice has more, and minimal to those where she has less.

Alternatively, think of the problem in terms of choosing the weights in a way that maximizes the sum difference. Because if there's any possible assignment, then the maximum possible sum difference (under the constraints) must be positive. So the problem reduces to checking if the maximum possible sum difference is positive.

So how to model the maximum possible sum difference given the constraints on the weights?

Let's model the sum difference as S = sum_{x=1 to k} (a_x - b_x) * w_x. We need S > 0.

But the w's must satisfy 0 < w_1 <= w_2 <= ... <= w_k.

To maximize S, we need to assign the largest possible w's to the terms where (a_x - b_x) is positive, and the smallest possible to terms where (a_x - b_x) is negative.

But due to the non-decreasing constraint, we can't just assign arbitrary large values. For example, if a certain species x has a_x - b_x positive, and a higher species y has a_y - b_y negative, then the weight for y must be at least as large as x's. But if y's coefficient is negative, that's bad for S. So perhaps the optimal way is to group species into intervals where the coefficients are positive, then set all those species to the maximum possible weight, and the rest to the minimal possible.

Alternatively, here's an approach inspired by the problem's constraints. Let's arrange the species in order from 1 to k. For each species x, let’s compute (a_x - b_x). We can think of the sum S as a weighted sum of these coefficients, where the weights are non-decreasing.

To maximize S, we can greedily assign as much weight as possible to the coefficients that are positive, especially higher coefficients. But the non-decreasing condition complicates this.

Wait, let's think of this as variables w_1, w_2, ..., w_k, with w_i <= w_{i+1} for all i. We need to find values such that the sum (a_i - b_i)*w_i is positive.

So the problem is similar to a linear programming problem, but with constraints on the variables.

Alternatively, perhaps the maximum possible sum S is achieved when all the w_i are as large as possible for the species where (a_i - b_i) is positive, and as small as possible otherwise, subject to the non-decreasing constraints.

But how to model this.

Let me think of an example. Suppose species 1 has a coefficient of +1, species 2 has a coefficient of +2, and species 3 has a coefficient of -1. Then to maximize S, we want w_1 as large as possible, w_2 as large as possible, but since w_3 must be >= w_2, but its coefficient is negative, so we want w_3 as small as possible (i.e., equal to w_2). So in this case, the sum would be 1*w1 + 2*w2 -1*w3. Since w3 >= w2, this is <= 1w1 + 2w2 -w2 = 1w1 + w2. But w1 <= w2, so substituting w1= w2 (the maximum possible for w1 given w2), then it's w2 + w2 = 2w2. So this is positive as long as w2>0.

But wait, in this scenario, how do we model the constraints.

Alternatively, perhaps the optimal way to maximize S is to assign the minimal possible weight to all species up to a certain point, and then assign maximal possible weights to the rest. Wait, perhaps we can find a point where, for all species <= x, the coefficients are such that making their weight as small as possible, and for species >x, as large as possible.

But how to find this x.

Alternatively, the maximum possible sum S is achieved when the variables are chosen to be as large as possible where their coefficient (a_i - b_i) is positive, and as small as possible where the coefficient is negative. But under the constraints.

Let me think: For each species i, the contribution to S is (a_i - b_i) * w_i. So, for species where a_i -b_i is positive, we want w_i to be as large as possible, given the constraints. For those where a_i -b_i is negative, we want w_i as small as possible.

But the constraints are that the w_i are non-decreasing. So the maximum possible S would be when, for all i where a_i -b_i is positive, w_i is set to the maximum possible (which is the same as w_{i+1} if possible?), and for those where it's negative, w_i is set to the minimum possible (w_{i-1} if possible?).

Alternatively, perhaps the optimal way is to assign w_i = w_{i+1} for as many as possible species, so that we can "bundle" the coefficients into ranges where their effect is maximized.

Alternatively, here's a key insight: the optimal assignment of weights can be determined by grouping species into intervals where all species in the interval have the same weight. Because if we can find a way to split the species into groups, assign a single weight to each group (non-decreasing), and then compute the sum based on these groups.

But I'm not sure.

Alternatively, let's model this as follows. For each species, we can represent the contribution (a_i - b_i) as a coefficient. Let's compute the cumulative coefficient for each possible grouping of species where the weights are the same.

Wait, perhaps we can process the species in order and find for each possible split point, the maximum possible contribution.

Let me consider the problem in terms of the sum S. The sum can be written as sum (c_i * w_i), where c_i = a_i - b_i. We need to assign w_i such that w_1 <= w_2 <= ... <= w_k, and S >0.

To maximize S, given that the c_i can be positive or negative, what's the best way to assign the weights.

For species where c_i is positive, we want w_i to be as large as possible. For species where c_i is negative, we want w_i to be as small as possible. But since the weights are non-decreasing, the weight assigned to a species with c_i positive (and higher i) can't be lower than those before.

So the optimal strategy is to find the earliest possible species where the cumulative sum from that species onwards (with their coefficients multiplied by maximum possible weights) outweighs the contributions from the earlier species.

Wait, maybe another approach. Let's imagine that all species from x to k are assigned the same weight (the maximum possible for x). Then, the sum S can be calculated as:

sum_{i=1 to x-1} c_i * w_i + sum_{i=x}^k c_i * W, where W is the weight for species x and onwards, and W >= w_{x-1}.

But since W can be as large as possible (since there's no upper limit), if the sum from x to k of c_i is positive, then we can choose W to be sufficiently large to make the entire sum positive.

Because for the sum S = (sum_{x}^k c_i) * W + sum_{1}^{x-1} c_i * w_i. If sum_{x}^k c_i is positive, then as W increases, this term can dominate, making S positive. Because W can be made as large as needed, even if the sum from 1 to x-1 is negative, as long as sum from x to k is positive and W is large enough, the total will be positive.

So, the key is to find the earliest x where the suffix sum (sum from x to k of c_i) is positive. Because then, by setting all species from x to k to a very large W (much larger than the previous weights), the sum will be dominated by the positive term.

Wait, this makes sense. Because the sum from x to k is the sum of c_i multiplied by W. If that sum is positive, then as W approaches infinity, the total sum will approach positive infinity, thus making S positive. So regardless of the contributions from the earlier species, we can always choose a W large enough to make the total sum positive.

Therefore, the problem reduces to checking if there exists some x such that the sum of c_i from x to k is positive. If such an x exists, then the answer is YES. Otherwise, it's NO.

But how do we compute this efficiently?

Let's think about the cumulative sum. Let's compute the suffix sums for each x. If any of those suffix sums is positive, then the answer is YES. Otherwise, it's NO.

Wait, but why? Let's see. Let's suppose for some x, the sum of c_i from x to k is S'. If S' >0, then we can set the weights for species x to k to be a very large value (same for all, since the sum is S' * W). Then, even if the sum from 1 to x-1 is negative, but since W can be made arbitrarily large, the total sum would be positive. So in this case, the answer is YES.

But how do the weights before x affect this? Because the weights for x must be >= those of x-1. But if we set the weights for x to be W, and all previous species to be some minimal value, but since W can be as large as needed, even if their contributions are negative, the overall sum can still be positive.

Wait, for example, let's say x=3. So species 1 and 2 are before x. Suppose sum from 3 to k is 5. Then, if we set w_3 = w_4 = ... = W. Then sum from 3 to k is 5*W. For species 1 and 2, their weights can be as small as possible (since their c_i could be negative). For example, if species 1 has c_i = -2, and species 2 c_i = -1. Then, their contribution would be (-2)*w1 + (-1)*w2. Since w1 <= w2 <= W. But even if we set w1 and w2 to their minimal possible values (say, w1=w2=0.5), then their contribution is -2*0.5 -1*0.5 = -1.5. Then, 5*W -1.5 >0 when W>0.3, which is possible. So the total sum would be positive.

Therefore, as long as there exists a suffix x where the sum of c_i from x to k is positive, then we can choose W large enough to make the entire sum positive.

But wait, what if the sum of c_i from x to k is positive, but there's a species y < x where c_y is positive? Then, perhaps combining their contributions could yield a better sum. But even then, the previous approach would already work. Because if there's a suffix sum positive, then the answer is YES. The existence of other positive c_i's in lower x's could also contribute positively if their weights are allowed to be high enough.

But in this problem, the goal is to find if there's any possible way. So, if even one such x exists, then the answer is YES.

Therefore, the problem reduces to checking whether the maximum suffix sum (over all x) is positive.

So the steps are:

1. For each species, compute the count for Alice (a_i) and Bob (b_i). So for each species i, c_i = a_i - b_i.

2. Compute the suffix sums of c_i from species x to k. If any of these suffix sums is positive, then the answer is YES.

Wait, but how? Because species are numbered up to k, which can be up to 1e9. So we can't process each species individually.

Ah, right. The problem says that the input gives the lists of fish caught by Alice and Bob. So, for species not present in either list, their a_i and b_i are zero. For species present in either list, their counts are as per the input.

But k can be up to 1e9, which means that there are possibly a lot of species not present in either list. For those species, c_i = 0 (since a_i = b_i =0). So their contribution to any suffix sum is zero.

Therefore, the key is to find if there exists a suffix sum (starting at some x) where the sum of c_i for x to k is positive.

But since species with c_i=0 can be ignored (they contribute nothing), the problem is to compute the suffix sums of the non-zero c_i's, and see if any of them is positive.

But even that is not directly possible. Because the list of species in the input can be up to 1e5 for Alice and 1e5 for Bob, so up to 2e5 unique species. So the maximum number of species with non-zero c_i is O(2e5).

So the approach is:

- Collect all species that appear in either Alice's or Bob's list. For each such species, compute c_i = a_i - b_i.

- Sort these species in increasing order (since they are numbered 1 to k, and need to be processed in order).

- Now, compute the suffix sums starting from each possible species in this sorted list, and see if any of them is positive.

Additionally, we need to account for the species that are not present in either list. Since their c_i is zero, the suffix sum from x to k would include all those species, but since their contribution is zero, the sum remains the same as the sum of the non-zero species up to x.

Wait, let's clarify.

Suppose we have a species x in the list. The suffix sum starting at x would include all species from x to k. But any species between x and the next existing species (say y) in the list would have c_i=0. So their contribution is zero, so the sum from x to y-1 is the same as the sum of x's c_i. Then, the sum from x to y would be sum from x to y-1 (which is sum of x's c_i) plus y's c_i.

So perhaps the key is that when we process the sorted list of species (sorted in order), the suffix sum for any x is the sum of all c_i for species >= x. Since species not in the list contribute zero, the sum is the sum of all c_i in the list that are >=x.

But how to compute this?

Let me think of the sorted list of species with non-zero c_i. Let's call them s_1, s_2, ..., s_m, sorted in increasing order. For each s_i, the sum of c_j for j >= s_i is the sum of c_{s_i}, c_{s_{i+1}}, ..., c_{s_m}}.

Because any species between s_i and s_{i+1} has c_j=0, so they don't contribute. So the sum for x = s_i is sum_{j=i}^m c_{s_j}.

If any of these sums is positive, then the answer is YES.

But also, what about x values that are not in the list? For example, x could be a species between s_{i-1} and s_i. For such x, the sum from x to k would include all species >=x. But since there are no species in the list between x and s_i, the sum would be sum_{j=i}^m c_{s_j}.

Wait, for example, if the list is [3,5,7], and x is 4. Then the sum from x=4 to k is sum of species 5, 7, etc. So the sum is sum(c_5 + c_7 + ...). So the suffix sum for x=4 is the same as for x=5.

Therefore, the possible suffix sums that could be positive are only the ones starting at the species in the sorted list, or between them. But the maximum suffix sum would be the maximum among the suffix sums starting at each s_i, or in the ranges between s_i and s_{i+1}.

Wait, for example, consider species sorted as s_1, s_2, s_3. Then, the possible x values where the suffix sum can be positive are:

- any x <= s_1: sum from x to k is sum of all c's (s_1's sum + s_2's sum + s_3's sum).

- x between s_1 and s_2: sum is sum of s_2 and s_3.

- x between s_2 and s_3: sum is sum of s_3.

- x >= s_3: sum is sum of s_3's c.

But the sum from x to k for x in [s_i, s_{i+1}) is the same as the sum from s_{i} to k. So the maximum possible suffix sum is the maximum among all suffix sums of the sorted list.

So, to find the maximum possible suffix sum, we can compute the suffix sums of the sorted list of c_i's. For each i in the sorted list, compute the sum of c_i, c_{i+1}, ..., c_m. The maximum of these sums is the maximum possible suffix sum. If this maximum is positive, then answer is YES.

But wait, no. Because when x is less than the smallest species in the list, the sum from x to k includes all species in the list. So the sum is the sum of all c_i's. So this is another possible suffix sum that we need to consider.

So the maximum suffix sum could be the maximum between the sum of all c_i's (when x is 1), or the suffix sums starting at each s_i.

So the steps to compute the maximum suffix sum are:

1. Collect all species present in either list. Sort them in increasing order.

2. For each such species, compute c_i = a_i - b_i.

3. Compute the sum of all c_i's. Let's call this total_sum.

4. Compute the suffix sums starting at each s_i. For example, for the sorted list s_1, s_2, ..., s_m, the suffix sum at s_i is sum_{j=i}^m c_j.

5. The maximum suffix sum is the maximum between total_sum and all the suffix sums computed in step 4.

If this maximum is positive, output YES. Otherwise, NO.

But wait, why total_sum? Because when x is 1, the suffix sum is the sum of all c_i's. Because for x=1, the sum includes all species >=1. Which includes all the s_i's, plus any other species (which have c_i=0). So the sum from x=1 is the sum of all s_i's c_i's.

Yes, that's correct.

So the algorithm is:

- Compute a frequency map for Alice and Bob.

- For all species in either's list, compute c_i = a_i - b_i.

- Collect these species in a sorted list.

- Compute the total_sum (sum of all c_i's).

- Then compute the suffix sums for the sorted list, in order. For example, for the sorted list s_1, s_2, ..., s_m, compute the suffix sum starting at s_1, which is sum of all c_i's. Then the suffix sum starting at s_2 is sum of c_{s_2} + ... + c_{s_m}, etc.

Wait, no. Wait, the sorted list is [s_1, s_2, ..., s_m], in increasing order. The suffix sum starting at s_1's position is sum of c_{s_1} + c_{s_2} + ... + c_{s_m} } = total_sum.

The suffix sum starting at s_2 is c_{s_2} + ... + c_{s_m} }.

But the sum from x = s_2 is the same as the sum from x = s_1 +1 (if s_2 is s_1 +1) but if s_2 is larger than s_1 +1, then the sum from x = s_1 +1 to s_2 -1 is the same as the sum from x = s_2, because all species in between have c_i=0.

So, to compute the maximum possible suffix sum, we need to consider:

- The sum of all c_i's (x=1).

- The suffix sums starting at each s_i in the sorted list.

Additionally, after the last species s_m, the sum from x = s_m +1 is zero (since all species >=x have c_i=0). So the maximum can't come from there.

So the steps are:

1. Compute all species with non-zero c_i.

2. Sort them in increasing order.

3. Compute the total_sum = sum of all c_i's.

4. Compute the maximum suffix sum from the sorted list.

The maximum suffix sum is the maximum between total_sum and the maximum of the suffix sums starting at each s_i in the sorted list.

Wait, no. Because the suffix sum starting at s_i is sum_{j=i}^m c_j. But when you start at x = s_i, the sum is sum of all c_j where j >= s_i, which is exactly the sum of the c_j's from s_i to s_m. Because the species after s_i in the list are higher.

So, for example, if the sorted list is [2,3,5], then the suffix sum for x=2 is sum of 2,3,5's c_i's. The suffix sum for x=3 is sum of 3 and 5's c_i's. The suffix sum for x=5 is sum of 5's c_i.

Thus, the maximum suffix sum is the maximum between total_sum and the suffix sums starting at each s_i. But wait, total_sum is the same as the suffix sum starting at s_1 (since the list is sorted). So the maximum is just the maximum of the suffix sums of the sorted list, which includes the total_sum.

So the steps are:

- Compute the list of (s_i, c_i), sorted by s_i in increasing order.

- Compute the array of c_i's in the order of s_i.

- Compute the suffix sums of this array, and find the maximum.

But why? Because for any x <= s_1, the sum is the total_sum. For x between s_1 and s_2, the sum is the sum of c_2, c_3, etc. Which is the same as the suffix sum starting at s_2. And so on.

Thus, the maximum possible suffix sum is the maximum among all suffix sums of the sorted array, including the sum of all elements (which is the first suffix sum).

So, in code:

We can compute the list of c_i's sorted by species. Then compute the maximum suffix sum of this list, including the entire list (sum of all elements) as the first suffix.

If the maximum is positive, output YES. Otherwise, NO.

But wait, there's another case: if there are species with c_i positive after some species with c_i negative, but the sum of those higher species is positive.

For example:

Alice's counts: species 3: 2, species 5: 1.

Bob's counts: species 3: 1, species 5: 0.

Then c_3=1, c_5=1. The sorted list is [3,5]. The suffix sums are 2 (3+5) and 1 (5). So maximum is 2. So answer is YES.

Another example: Alice has species 1:1, Bob has species 2:1. Then c_1=1, c_2=-1. The sorted list is [1,2]. The suffix sums are 0 (1-1=0) and -1. So the maximum is 0, which is not positive. So answer is NO. But wait, can we assign weights such that Alice's total is larger?

For example, w1=1, w2=1. Then Alice's sum is 1*1 =1. Bob's sum is 1*1=1. So it's equal. Not larger.

If w1=1, w2=2. Then Alice's sum is 1*1=1. Bob's sum is 1*2=2. Alice is smaller.

So no possible way. Hence, answer is NO.

So the algorithm works.

Another example: Alice has species 2:3, Bob has species 1:2 and 3:1. So:

c_1 = 0-2 = -2 (since Alice has 0, Bob has 2).

c_2=3-0=3.

c_3=0-1=-1.

So the sorted list is [1,2,3]. c values are [-2,3,-1].

The suffix sums are:

sum(1,2,3) → -2 +3 -1=0.

sum(2,3) →3-1=2.

sum(3) →-1.

The maximum is 2, which is positive. So answer is YES.

Indeed, choosing w1=1, w2=2, w3=2. Then Alice's sum is 3*2=6. Bob's sum is 2*1 +1*2=4. 6>4. So yes.

So the algorithm works.

So the steps are:

1. For each species in Alice and Bob's lists, compute the counts.

2. For each such species, compute c_i = a_i - b_i.

3. Sort these species in increasing order.

4. Compute the list of c_i's in the sorted order.

5. Compute the suffix sums of this list. The maximum suffix sum is the maximum of all possible suffix sums. If it's positive, output YES; else, NO.

But how to compute the suffix sums efficiently.

In code:

We can process the list in reverse order, accumulating the sum. For each position i in the sorted list, the suffix sum starting at i is the sum of c_i, c_{i+1}, ..., c_{n-1}.

We can compute this in O(m) time, where m is the number of species in the sorted list.

So the plan is:

- Use dictionaries to count Alice's and Bob's species.

- Collect all unique species from both.

- For each species in this set, compute c_i = a_count - b_count.

- Sort the species in increasing order.

- Create a list of c_i's in this sorted order.

- Compute the maximum suffix sum of this list.

- If the maximum is >0, output YES; else, NO.

Now, let's handle the edge cases.

For example, when there are no species in the lists (n=0 and m=0). But according to the constraints, n and m are at least 1. Wait, the problem says 1<=n, m <=1e5. So no. The input will always have n and m >=1.

Wait, no. Wait the input constraints for n and m are 1<=n, m <=1e5. So Alice and Bob must have caught at least one fish each. So the lists are non-empty.

So in code, we can ignore the case where there are no species in the lists.

Another edge case: if all c_i's are zero. Then the sum is zero. So answer is NO.

If the maximum suffix sum is zero, then answer is NO.

Otherwise, if it's positive, answer is YES.

So the code steps:

Read n, m, k.

Read Alice's list: a list of n integers.

Read Bob's list: m integers.

Count frequencies for Alice: a_counts.

Count frequencies for Bob: b_counts.

Collect all unique species in either a_counts or b_counts.

Sort the species in increasing order.

For each species in the sorted list, compute c_i = a_counts.get(s, 0) - b_counts.get(s, 0).

Make a list c of these values.

Compute the suffix sums. Initialize current_sum =0, max_suffix = -infinity.

Traverse the list c from the end to the beginning:

current_sum += c[i]

max_suffix = max(max_suffix, current_sum)

At the end, the maximum suffix sum is max_suffix.

But wait, the initial current_sum is 0, and for each element starting from the end, we add it. So after processing all elements, current_sum is the sum of all elements. So the maximum_suffix is the maximum of all possible suffix sums, including the sum of all elements.

So yes, this approach works.

For example, if the list is [c1, c2, c3], then:

i=2 (third element) → current_sum =c3 → max is c3.

i=1 → current_sum +=c2 → c2 +c3 → compare to max.

i=0 → current_sum +=c1 → c1 +c2 +c3.

So the maximum is the maximum of c3, c2+c3, c1+c2+c3. Which is the maximum suffix sum.

Thus, in code:

Compute the list of c_i's in sorted order.

Compute the suffix sums, keeping track of the maximum.

If the maximum is >0 → YES, else NO.

So the code can be written as follows.

Now, considering the input constraints:

n and m can be up to 1e5 each. So the total number of unique species is up to 2e5. So the sorted list can have up to 2e5 elements. Processing them is O(m log m) for the sort, which is acceptable.

The code steps:

Read n, m, k.

Read a list: list_a = list(map(int, ...)).

Read list_b = list(map(int, ...)).

Create a_count as a Counter for list_a.

Create b_count as a Counter for list_b.

species = set(a_count.keys()).union(b_count.keys())

sorted_species = sorted(species)

c_list = [a_count.get(s, 0) - b_count.get(s, 0) for s in sorted_species]

Compute suffix sums:

current_sum = 0

max_suffix = -inf

for c in reversed(c_list):

    current_sum += c

    if current_sum > max_suffix:

        max_suffix = current_sum

if max_suffix >0:

    print("YES")

else:

    print("NO")

Yes. This should work.

Testing against sample input 1.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))
    b = list(map(int, input_stream.readline().split()))
    
    a_count = defaultdict(int)
    for x in a:
        a_count[x] += 1
    b_count = defaultdict(int)
    for x in b:
        b_count[x] += 1
    
    species = set(a_count.keys()).union(b_count.keys())
    sorted_species = sorted(species)
    c_list = []
    for s in sorted_species:
        c = a_count.get(s, 0) - b_count.get(s, 0)
        c_list.append(c)
    
    current_sum = 0
    max_suffix = -float('inf')
    for c in reversed(c_list):
        current_sum += c
        if current_sum > max_suffix:
            max_suffix = current_sum
    
    print("YES" if max_suffix > 0 else "NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 7 9
5 2 7 3
3 5 2 7 3 8 7
""",
            "output": \
"""\
NO
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

Sample 2:

4 7 9

5 2 7 3 → a_counts: 5:1, 2:1,7:1,3:1.

3 5 2 7 3 8 7 → b_counts:3:2,5:1,2:1,7:2,8:1.

species: 2,3,5,7,8.

sorted: [2,3,5,7,8].

c_list:

2:1 (a) -1 (b) → 0.

3:1 (a) -2 (b) → -1.

5:1 (a) -1 (b) →0.

7:1 (a) -2 (b) →-1.

8:0 (a) -1 (b) →-1.

So c_list is [0, -1, 0, -1, -1].

Processing reversed:

-1 → current_sum =-1. max is -1.

-1 → sum is -2. max remains -1.

0 → sum -2. Still no.

-1 → sum -3.

0 → sum-3.

The maximum suffix sum is -1. Which is not positive. So output is NO.

Which matches the sample.

Another test case where the answer is NO when the total_sum is zero. For example:

Alice has species 1:1, Bob has species 2:1.

c_list is [1, -1]. Suffix sums: 1-1=0 (sum of all), then -1. So maximum is 0 → answer is NO.

Thus, the code should handle all cases correctly.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    
    a_count = defaultdict(int)
    for x in a:
        a_count[x] += 1
    b_count = defaultdict(int)
    for x in b:
        b_count[x] += 1
    
    species = set(a_count.keys()).union(b_count.keys())
    sorted_species = sorted(species)
    c_list = []
    for s in sorted_species:
        c = a_count.get(s, 0) - b_count.get(s, 0)
        c_list.append(c)
    
    current_sum = 0
    max_suffix = -float('inf')
    for c in reversed(c_list):
        current_sum += c
        if current_sum > max_suffix:
            max_suffix = current_sum
    
    print("YES" if max_suffix > 0 else "NO")

if __name__ == "__main__":
    main()
```
