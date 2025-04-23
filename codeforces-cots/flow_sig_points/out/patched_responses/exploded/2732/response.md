<think>
Okay, let's tackle this problem. So, the goal is to find the minimum cost to make the list 'good', which means that the GCD of all elements is not 1. The operations allowed are deleting elements with cost x or increasing a number by 1 with cost y each time. 

Hmm, first, I need to understand what makes the list bad. The list is bad if the GCD of all elements is 1. So to make it good, we need to ensure that the GCD is at least 2. Because if the GCD is 2 or higher, then it's not 1, so the list is good. So the problem reduces to modifying the list (by deleting elements or increasing some numbers) such that the GCD of the remaining elements is >= 2, and the cost is minimized.

Wait, but how do we approach this? Because calculating all possible subsets and their GCDs is impossible for large n. So we need a smarter approach.

Let me think. To have a GCD greater than 1, all remaining elements must share a common divisor d >= 2. So maybe the approach is to find a d >= 2, and compute the minimal cost required to make all elements in the list (after possible deletions) divisible by d. Then, among all possible d's, choose the one with the minimal total cost.

But d can be up to the maximum possible value of (a_i + some increments). How do we handle that?

Wait, but the possible d's are factors of (a_i + k), where k is the number of increments. But considering all possible d's isn't feasible. However, maybe we can collect all possible primes from the numbers after some operations and check those primes. Because the minimal cost would likely be achieved with a prime d. Because if d is composite, say d = p*q, then using p or q might lead to a lower cost.

So perhaps we can generate all possible primes that are factors of any a_i or a_i +1, etc. Then for each of those primes, compute the minimal cost to make all elements in the list (possibly with deletions) divisible by d. Then take the minimum over all possible primes d.

Alternatively, considering that for a d to be a possible candidate, we can look for primes that are factors of some a_i or a_i +1, but even that might not capture all possibilities, but perhaps the optimal d is a prime in the vicinity of the a_i's.

Let me think: For each number in the list, there are a few possibilities: either delete it, or modify it (possibly) to make it divisible by d. For a given d, the cost for each element a_i is the minimum between the cost of deleting it (x) and the cost of modifying it (y multiplied by the number of increments needed to reach the next multiple of d). But if the minimal cost for a_i is to delete it, then that element is not part of the list. The GCD of the remaining elements (those not deleted and modified to be divisible by d) would be at least d, so if d >=2, then the list is good.

Wait, no. Because if all elements are divisible by d, then the GCD is at least d, which is >=2. So that's correct.

So the plan is:

1. Find all candidate primes d that could be the GCD. But how?

2. For each candidate d, compute the minimal cost to make all elements in the list (after possible deletion) divisible by d. The cost is sum over each element of min(delete cost x, modify cost (y * (ceil(a_i / d) * d - a_i )) ), but if all elements are deleted, then that's invalid (since the list must be non-empty). So for each d, we need to make sure that at least one element is not deleted.

Wait, but when we compute for a d, the sum is the sum of min(delete x, modify cost) for each element. But if all elements are deleted (sum of x for all), then that's not a valid solution. So for each d, we need to check if there's at least one element where the modify cost is <= x, because otherwise, all elements would be deleted, which is invalid. So for each d, we need to compute the sum of min(x, modify cost) for each element, and then subtract x and add the modify cost for the element with the smallest (modify cost - x) difference. Because if all elements are deleted, we have to select at least one to not delete. So that's a bit more complex.

Alternatively, for each d, compute the total cost as the sum of min(x, modify cost) for all elements. Then, if all elements are deleted (i.e., the sum is n * x), then this d is not a valid candidate. Otherwise, the total sum is the cost for that d. Wait, no: because the list must be non-empty. So even if for d=2, the minimal cost for each element is x, but you can't delete all elements. So for such a case, you have to keep at least one element. So the minimal cost is (sum of all x) - x + modify cost for that element. So you have to choose at least one element to not delete. So the cost for d would be (sum of min(x, cost_i) for all i) - (max(0, min(x - cost_i)) for all i where cost_i < x)).

Wait, perhaps the correct approach is:

For each d, compute for each element a_i the minimal cost between deleting it (x) or modifying it (y * (d - a_i % d) % d). Because the number of increments needed is (d - (a_i % d)) % d. For example, if a_i is 16 and d is 17, then 16 % 17 is 16, so increments needed is 1. So the cost is y * 1.

Then, the total cost for d is sum over all elements of min(x, y * (d - a_i % d) if a_i % d !=0 else 0). But there's a problem: if all elements are deleted (i.e., for each a_i, the min is x), then the list is empty, which is invalid. So in such cases, we have to select at least one element to not delete, even if it's more expensive. So for the case where all elements are min(x, ...), but sum is n*x, then we need to pick the element where the modify cost is the smallest, and subtract x and add that cost. For example, if all elements are cheaper to delete than modify, but we can't delete all. So we need to take the minimal modify cost (even if it's larger than x) for at least one element.

So the steps for each candidate d are:

1. Compute for each element a_i the cost to delete (x) or modify (y * k, where k is the steps needed to reach a multiple of d).

2. For all elements, compute the min between x and modify cost. Sum these. Also, track whether there are any elements where the modify cost is less than x. Because if all elements have modify cost >=x, then the sum would be n*x, but we cannot delete all elements. So in that case, we have to replace one of the elements' delete cost with modify cost, which would be the minimal possible (i.e., the minimal modify cost among all elements, which may be larger than x but we have to choose it).

Wait, but if all elements are modified, then the list is non-empty, but the cost is sum of min(x, ...). If all elements are deleted (sum is n*x), then the list is empty, which is invalid. So in that case, we have to pick at least one element to modify. So for the candidate d, the total cost would be (sum of min costs) - x + (modify cost for that element). Because initially, we considered deleting that element (cost x), but now we have to not delete it, so subtract x and add the modify cost.

So the algorithm for a candidate d is:

sum_cost = sum( min(x, y * k_i) for each a_i )

count_deleted = number of elements where x < y*k_i (so they are deleted)

But if count_deleted == n, then sum_cost is n*x, which is invalid. So in that case, we need to find the element with the minimal (y*k_i - x), and subtract x and add y*k_i. Because that element is forced to be kept. But since y*k_i may be larger than x, this would increase the cost. But this is the only way to have a non-empty list.

Wait, but in the case where all elements are better to delete (x < y*k_i for all), then modifying any of them would be more expensive. So the sum for d would be (n-1)*x + (y*k_i) for some i where y*k_i is minimal. But this might be worse than other d's.

So for each candidate d, we need to compute sum_cost as:

sum_min = sum( min(x, y*k_i) for each a_i )

count_deleted = sum( 1 for each a_i if x < y*k_i )

if count_deleted == n:

   then we need to replace the delete cost of one element with the modify cost. So the new sum would be sum_min - x + (y*k_i for the element where y*k_i - x is minimal). So the minimal possible sum in this scenario is sum_min - x + (min(y*k_i for all a_i))

But this is only necessary when all elements are deleted. Otherwise, there's at least one element not deleted, so sum_min is valid.

So the process for each d is:

Compute sum_min as the sum of min(x, modify cost) for all elements.

If sum_min is n * x (all elements are deleted), then find the minimal modify cost among all elements (even if it's larger than x). Then the actual cost is (sum_min - x) + minimal_modify_cost.

Otherwise, the cost is sum_min.

Then, we select the minimal cost over all possible d's.

But how do we find the candidate d's?

Because d can be any integer >=2, but checking all possible d's is impossible. So we need to collect possible candidates d that can potentially be the GCD after modifications.

So the idea is to collect all possible primes that are factors of (a_i + k) for some i, where k is up to some small value, since the cost of adding k steps is y *k. Since y can be up to 1e9, adding even a few steps can be expensive, so the optimal d's are likely to be factors of a_i or a_i+1, or a_i+2, etc., up to some small limit. For example, in the first sample input, 17 is a prime, and 16+1=17. So the optimal d is 17.

So the approach would be:

- Generate all primes that are factors of a_i, a_i+1, a_i-1 (if a_i >1), etc. But for the problem's constraints (n up to 5e5, a_i up to 1e6), generating all possible primes from these candidates is manageable.

So here's the plan:

1. Collect all possible primes from the factors of each a_i and a_i+1 (since adding 1 to a_i can make it a multiple of a prime). For example, if a_i is 16, then a_i +1 is 17 (prime). So d=17 would be a candidate.

2. Also, collect primes from a_i-1 (if a_i-1 >=2). Because modifying a_i down (but the problem says we can only increase a_i). Wait, no. The problem allows only to increase a_i. So modifying a_i to reach a multiple of d would require adding some steps. So for example, if a_i is 15 and d is 5, then 15 is already a multiple of 5, so no steps needed. But if a_i is 16, then d=5 would require adding 4 steps (to reach 20). So the possible candidates d are factors of (a_i + k), where k is the steps added. But since k can be up to (d-1), which could be large, how do we choose which d's to check?

This seems tricky. Let's think differently. For each a_i, the possible d's that could be considered are those that are divisors of (a_i + k) where k is between 0 and ... perhaps up to some maximum possible k. But what's the maximum possible k we can afford? Because each step costs y. So for example, if the cost of adding k steps is y*k, which must be <= x (the delete cost), then k can't exceed x/y. Because if y*k >x, then it's better to delete the element.

So for a given element a_i, the possible d's that could be considered (i.e., where modifying is cheaper than deleting) must satisfy:

y * k <= x --> k <= x/y.

But k is the number of steps needed to reach the next multiple of d. So for a given a_i, the d's that are possible to consider are those where there exists a multiple of d that is >=a_i and <= a_i + (x//y). Because if you have to add more than (x//y) steps, then it's cheaper to delete the element instead.

Therefore, for each a_i, the d's that could contribute to the minimal cost are the divisors of (a_i + k), where k ranges from 0 to (x//y). But even this could be a lot. For example, x=1e9, y=1, then k can be up to 1e9, which is impossible.

So this approach is not feasible. So we need a better way to collect candidate primes.

Alternative approach:

The optimal d is likely to be a prime number that divides at least one of the a_i's after adding a small number of steps. So for each a_i, we can collect primes that are factors of a_i + k, where k is 0, 1, or possibly up to some small number (like 10). Then, all such primes are candidates. Then, for each candidate prime, compute the minimal cost as discussed.

This is manageable, because for each a_i, even checking up to k=10, the number of primes generated would be manageable. For example, for each a_i, we generate primes from a_i, a_i+1, a_i+2, ..., a_i+10, which would give a manageable number of candidates, especially since we can collect all unique primes.

But how to compute the primes from a_i +k for small k. For example, for a_i up to 1e6 + 10, the primes can be precomputed, but factorization for each number in this range is possible on the fly.

Wait, but the candidate primes would be factors of a_i +k for some i and k in 0..max_k. So for each a_i, for k in 0 to max_k, we can factor a_i +k and collect all primes from their factors.

But max_k is determined by the maximum steps we can add without exceeding the delete cost. But in cases where y is very small (like y=1), then x/y can be up to 1e9, but that's impossible. So perhaps we need to limit k to a small number, like up to 20. But how?

Alternatively, since the problem requires a solution that works within the time constraints, perhaps we can collect all primes that are factors of any a_i or a_i+1, and also some other nearby numbers. Because even if the optimal d is a prime that is a factor of a_i +k for larger k, but the cost of adding k steps would be high, so it's not considered. So perhaps considering primes in the vicinity of the a_i's (like a_i, a_i+1, a_i-1) would capture the optimal d.

But how?

Another idea: for each a_i, the possible d's that can be achieved by modifying a_i are those that are factors of a_i + k, where k is the number of steps added, and the cost y *k is <=x (since otherwise, it's better to delete). So for each a_i, the maximum possible k is x//y. Therefore, the maximum a_i +k is a_i + (x//y). So for each a_i, we can collect all primes that divide any number in the range [a_i, a_i + (x//y)], but this can be a large range if x//y is large.

For example, if x=1e9 and y=1, then x//y is 1e9, which is impossible to check for each a_i.

This suggests that this approach is not feasible for all cases. So perhaps we need a different strategy.

Alternative approach:

If the optimal d is a prime, then we can precompute all primes up to the maximum possible a_i + (x//y), but again, if x//y is 1e9, this is impossible.

Alternatively, note that in the case where y is very small, then x may be large. For example, if x is 1e9 and y is 1. Then, for an element a_i, adding up to x//y =1e9 steps is allowed. But even so, the cost for adding k steps is k*1. So for a_i, the possible d's are factors of a_i +k, where k can be up to 1e9. But this is not feasible.

So how else can we approach this?

Perhaps the optimal d is a prime that divides at least one of the a_i's after adding some steps, and the minimal cost for that d is lower than other possibilities.

But even this is vague.

Another observation: For the list to have a GCD >=2, it's sufficient that all remaining elements are even. So d=2 is a candidate. The cost for d=2 would be sum over each element of min(x, y*( (2 - (a_i %2)) %2 ) ). Then check if all elements are deleted (sum is n*x) and adjust accordingly.

Similarly, d=3, etc. So perhaps the optimal d is a small prime.

But in some cases, the optimal d may be a larger prime. For example, in the first sample input, the optimal d is 17.

So perhaps the way forward is to collect all primes that are factors of any a_i, a_i+1, or a_i-1 (if a_i>1), and also primes from some small numbers. Then, for each of those primes, compute the cost and take the minimal.

But how many primes would that be? For each a_i, factoring a_i, a_i+1, a_i-1 would give a number of primes. Then, considering all unique primes from all such a_i's, and for each of those, compute the cost.

This approach could be feasible. Because even if n is 5e5, each a_i can have up to log(1e6) factors, but since we are considering only primes, the total number of unique primes across all a_i's, a_i+1, a_i-1 would be manageable.

So the steps would be:

1. Collect all primes that are factors of any a_i, a_i+1, or a_i-1 (if a_i >1). Also, for each a_i, check a_i +1 and a_i -1 (if applicable) and collect their prime factors.

2. For each unique prime d from this collection, compute the minimal cost as described earlier.

3. Additionally, consider d=2, even if not in the collection (but this is redundant if the collection includes all primes from the a_i's).

4. The minimal cost among all these d's is the answer.

But why would this work? Because modifying an element a_i to a multiple of d requires that a_i +k is divisible by d. The possible d's could be factors of a_i, a_i+1, a_i-1, etc. For example, in the first sample input, 16 +1=17 is a prime, and d=17 is considered. For this d, the cost is 23 (delete 1) + 17 (modify 16 to 17) + 0 (17 is already 17) + 0 (17 is already 17). So total 40.

This approach would capture that.

But what if the optimal d is not a prime factor of any a_i, a_i+1, or a_i-1? For example, consider a list where the elements are all 14. The GCD is 14, which is already good. But if one of the elements is 15, and we have to modify it. Suppose the optimal d is 7, which is a factor of 14. Then, modifying 15 to 21 (cost y*6) would be needed, but perhaps deleting is cheaper. So in this case, d=7 is considered because it's a factor of 14 (which is in the list) and of 21 (the modified 15).

But if the optimal d is a composite number, like 4, then perhaps it's better to check d=2 instead, which is a prime factor. Because making all elements even (d=2) may be cheaper than making them multiples of 4. So checking primes is sufficient.

Thus, the approach of checking all primes that are factors of any a_i, a_i+1, a_i-1 is sufficient to find the optimal d.

So the steps are:

1. Generate all candidate primes d by checking the factors of a_i, a_i+1, a_i-1 for all i.

2. For each candidate d (prime), compute the minimal cost to make all elements divisible by d (with possible deletions, ensuring the list is non-empty).

3. The minimal cost among all these d's is the answer.

Now, the problem is to implement this efficiently.

So first, let's code the steps:

First, collect all the a_i, a_i+1, a_i-1, and for each of them, find all primes in their factors. Then collect all unique primes from these factors. Also, ensure that the primes are >=2.

Then, for each such prime d, compute the cost.

Now, how to collect the primes.

We can process each number in the list (a_i, a_i+1, a_i-1) and for each of these numbers, factorize them and collect their prime factors. Then, all these primes are the candidates.

For example, for a_i=16, we factor 16 (primes: 2), 17 (primes:17), and 15 (primes:3,5). So the primes for this a_i are 2,3,5,17.

So for all a_i, we process a_i, a_i+1, a_i-1 (if a_i-1 >=1) and collect their prime factors.

Once we have all the primes, we can iterate through them, compute the cost for each, and find the minimal one.

Now, factorization for numbers up to 1e6 +1 is manageable. Because each number up to 1e6 can be factorized by trial division quickly. Alternatively, we can precompute primes up to 1e6+1 using sieve of Eratosthenes, but even trial division for each number is manageable.

So let's proceed.

Now, the code steps:

Read n, x, y.

Read the list a.

Generate all possible numbers as a_i, a_i+1, a_i-1 for each a_i in a.

For each number in this collection, compute its prime factors.

Collect all unique primes from these factors.

Also, ensure that we consider 2 even if no a_i is even. Because if all a_i are odd, then we can check d=2.

But in the code, the primes collected would include 2 if any of a_i, a_i+1, a_i-1 have 2 as a factor.

So for example, if all a_i are odd, then a_i-1 may be even (if a_i is even, then a_i is even, but if a_i is odd, then a_i-1 is even). So the primes would include 2.

But in the case where all a_i are even, then their a_i-1 would be odd, so perhaps 2 is not in the a_i-1's factors. But the a_i's are even, so their factors include 2.

So the code will collect 2 as a candidate.

So after collecting all primes from these numbers, we have our candidate d's.

Then, for each d in the candidates, compute the cost.

Now, the code for factorization.

We can write a function to factor a number into primes. For example:

def get_primes(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //=2
    i =3
    while i*i <=n:
        while n%i ==0:
            factors.add(i)
            n//=i
        i +=2
    if n>1:
        factors.add(n)
    return factors

This function returns the set of prime factors of n.

Then, for each number in the list (a_i, a_i+1, a_i-1), collect all primes.

Once we have all the primes, for each prime d, compute the cost.

Now, the cost computation for a d:

For each element a_j in a:

Compute the minimal steps needed to make a_j +k divisible by d. Since we can only add steps, k is (d - (a_j %d)) %d. Because if a_j %d is 0, then k is 0. Otherwise, it's d - (a_j %d). For example, a_j=5, d=3: 5%3=2, so k=1 (5+1=6, which is divisible by 3).

The cost for modifying is y *k.

The cost for deleting is x.

So for each a_j, we take the minimum between x and y*k.

Sum all these minima.

But then, we have to ensure that not all elements are deleted. So if all elements are deleted (sum is n*x), then we need to find the element where (y*k - x) is minimal (i.e., the element where even though deleting is cheaper, but we have to keep it modified to avoid an empty list).

So for each d:

Compute for each a_j:

modify_cost = y * ((d - (a_j %d)) %d)

delete_or_modify = min(x, modify_cost)

sum_cost += delete_or_modify

Also, track the minimal (modify_cost - x). Because if sum_cost is n*x, then we have to subtract x for one element and add modify_cost, which is the minimal (modify_cost -x) over all elements. The minimal (modify_cost -x) would be the minimal increase in cost needed to keep that element.

So during the loop, for each a_j, compute modify_cost. Then, if modify_cost <x, then there's no problem. But if all modify_cost >=x, then sum_cost is n*x, and we have to find the minimal modify_cost (since x is subtracted and modify_cost is added, the cost becomes (n*x -x + modify_cost) = (n-1)x + modify_cost. We need to choose the modify_cost that is minimal among all a_j's.

So during processing each d, we can:

- Keep track of the sum of min(x, modify_cost).

- Keep track of whether there is at least one a_j where modify_cost <=x.

If there is at least one such a_j, then the sum is valid.

If not, then sum is n*x, and we need to find the minimal modify_cost, and adjust the sum.

So the code for each d is:

sum_cost =0

all_deleted = True

min_extra = infinity

for each a_j in a:

    rem = a_j %d

    if rem ==0:

        k =0

    else:

        k =d - rem

    modify_cost = y *k

    if modify_cost <x:

        sum_cost += modify_cost

        all_deleted = False

    else:

        sum_cost +=x

        current_extra = modify_cost -x

        if current_extra < min_extra:

            min_extra = current_extra

if all_deleted:

    # all elements are deleted. So need to replace one.

    sum_cost = sum_cost -x + (x + min_extra)  # because sum was n*x, subtract x, add x + min_extra (since modify_cost = x + (modify_cost -x) = x + min_extra)

    # which is sum_cost -x + (x + min_extra) = sum_cost + min_extra. Wait, sum_cost is n*x. So sum_cost =n*x.

    # So new sum_cost = (n-1)*x + (x + min_extra) = n*x + min_extra. Wait, that can't be right.

    Wait, no:

Original sum is n*x (all elements are deleted). So for each element, min(x, modify_cost) =x.

But when all are deleted, the list is empty. So to make it non-empty, at least one element must be modified. So for one element, instead of x, we take modify_cost. The sum becomes (n-1)*x + modify_cost.

modify_cost =x + (modify_cost -x) =x + current_extra.

So the new sum is (n-1)*x + x + current_extra = n*x + current_extra.

But current_extra is (modify_cost -x). So the new sum is sum_cost (n*x) + current_extra -x (no, wait: sum_cost is n*x. After replacing one x with modify_cost, the sum is (n-1)*x + modify_cost. Which is sum_cost -x + modify_cost. Since modify_cost =x + current_extra, sum is sum_cost -x + x + current_extra = sum_cost + current_extra. Since sum_cost was n*x, the new sum is n*x + current_extra.

But current_extra could be positive or negative? No. Because in this case, all modify_cost >=x. So current_extra =modify_cost -x >=0.

So the new sum is n*x + current_extra. But current_extra is the minimal possible (modify_cost -x). So the minimal possible sum is (n*x) + minimal_extra.

Thus, during the loop, for each element, if we choose to delete it, but then have to replace one delete with modify, we track the minimal_extra (which is the minimal (modify_cost -x) across all elements).

So, in code:

sum_cost =0

all_deleted = True

min_extra = infinity

for a_j in a:

    rem = a_j %d

    if rem ==0:

        k=0

    else:

        k =d - rem

    modify_cost = y *k

    if modify_cost <x:

        sum_cost += modify_cost

        all_deleted = False

    else:

        sum_cost +=x

        current_extra = modify_cost -x

        if current_extra < min_extra:

            min_extra = current_extra

if all_deleted:

    # all elements are deleted

    if min_extra == infinity:

        # no elements (but this is possible? Because all elements have modify_cost >=x. So current_extra is computed.

        # But a_j is in the list, so at least one element exists. So min_extra is not infinity.

        pass

    sum_cost = sum_cost -x + (x + min_extra)  # which is sum_cost + min_extra

So for example, if sum_cost was 4*x (n=4), and min_extra is 17, then the new sum is 4x +17.

But x is given as per input. For the first sample input, let's see:

Sample input 1:

4 23 17

1 17 17 16

For d=17:

For a_j=1:

rem =1%17=1. k=16. modify_cost=17*16=272. x is 23. 272>23, so cost is 23. current_extra=272-23=249.

For a_j=17: rem=0, modify_cost=0. 0 <23. So cost is 0. all_deleted becomes False.

For the other 17s: same.

For 16: rem=16%17=16. k=1. modify_cost=17*1=17. 17 <23. So cost 17. sum_cost is 23+0+0+17=40. all_deleted is False. So no adjustment needed. Hence, sum is 40.

Which matches the sample output.

So the code works.

Now, after collecting all primes, compute this sum for each and select the minimal.

Now, what if there are no candidate primes (like all a_i=1)? Then, we have to create a d. For example, if all a_i=1, then the only way is to increase one of them to 2 (cost y*1) and delete the rest (cost x*(n-1)). Or delete all but one, but the remaining one is 1, which has GCD 1. So you have to modify at least one element.

But this case is handled automatically by the code. Because for a_j=1, we have a_j+1=2, which factors into primes [2]. So d=2 is considered.

So for all a_j=1, a_j+1=2. So the primes collected would include 2. Then, for d=2, each a_j=1 would have to be modified by adding 1 (k=1), cost y*1. So for each element, the cost is min(x, y). If y <x, then it's cheaper to modify. So for example, if all elements are 1, x=3, y=2. Then for d=2, each element's cost is 2. Sum is 2*n. Which is better than deleting (3*n). So the code would choose d=2.

Now, what about when the list is already good? For example, a list with elements all even. Then, the sum for d=2 would be 0, because all elements are already even. So the code would select d=2 with cost 0.

But wait, the code will compute sum_cost for d=2, which is sum of min(x, 0) for all elements. So sum is 0. So this is the correct answer.

So the code should handle all cases.

Now, the code structure in Python:

Read n, x, y.

Read a list.

Collect all candidate primes:

Initialize a set.

For each a_i in a:

   for num in [a_i, a_i+1, a_i-1]:

       if num <2: continue

       primes = get_primes(num)

       add to the candidate set.

Once all primes are collected.

If no primes are found (unlikely, since a_i can be 1, leading to 2 in a_i+1):

But in that case, perhaps the code will have d=2 in the candidates.

So proceed.

Now, for each d in the candidate primes:

compute the cost as discussed.

Keep track of the minimal cost.

Finally, output the minimal cost.

If there are no candidates (but this can't happen), the answer would be to delete all but one element and modify that one, but I think the code will handle it because in such a case, the candidate primes would include 2.

Now, the code.

But what about the case where the list is already good? For example, the GCD is already >=2. Then, the code would find that the cost is 0.

But the problem requires that the list is not empty. So if the original list's GCD is >=2, the answer is 0. So how does the code handle this?

For example, the list is [2,4,6]. The GCD is 2. So the list is already good. So the code would compute for d=2. For each element, modify_cost is 0. So sum is 0. Which is correct.

Another example: list is [3,6]. GCD is 3. So sum for d=3 is 0.

Thus, the code handles this case.

Now, let's code.

But in Python, for the case of 5e5 elements, and for each element, factorizing 3 numbers (a_i, a_i+1, a_i-1), which can be up to 1e6+1, the code must be efficient.

But trial division for each number up to 1e6 is manageable. For example, 1e6 is sqrt(1e6) =1e3. So trial division up to 1e3 for each number. For 5e5 elements, each with 3 numbers, that's 1.5e6 numbers. For each, trial division up to 1e3 steps. So 1.5e9 steps, which is way too much. That would be a problem.

Wait, but 1e6 is 1,000,000. So sqrt(1e6) is 1000. So for each number, the trial division would take O(sqrt(n)) steps. For numbers up to 1e6, this is O(1e3) steps per number. For 1.5e6 numbers, that's 1.5e6 * 1e3 =1.5e9 operations, which is way too slow for Python. So this would cause a TLE.

So this approach is not feasible. We need a faster way to factor the numbers.

Alternative approach: Precompute the smallest prime factor (SPF) for numbers up to 1e6 +2. Then, for each number, we can factor it by dividing by its SPF repeatedly. This would allow us to factor each number in O(log n) steps.

So let's precompute the SPF.

The maximum possible a_i is 1e6. So a_i+1 can be up to 1e6 +1, and a_i-1 can be up to 1e6-1. So the maximum number we need to factor is 1e6+1.

So precompute SPF up to 1e6+2.

Then, for each number, factorization is quick.

So the code would:

Compute the SPF array up to 1e6+2.

Then, for each number in a_i, a_i+1, a_i-1, use the SPF array to find its prime factors.

This will make the factorization step O(log n) per number.

So the code steps:

precompute SPF.

collect all primes from a_i, a_i+1, a_i-1.

Now, let's implement this.

First, precompute the SPF.

max_num = 1e6 +2

But in code, we can compute it as follows:

max_num = 0

for each a_j in a:

    for num in [a_j, a_j+1, a_j-1]:

        if num > max_num:

            max_num = num

so find the maximum number across all a_j, a_j+1, a_j-1.

Then, compute the SPF up to max_num.

But if the a_i are up to 1e6, then a_i+1 can be up to 1e6+1. So precomputing SPF up to 1e6+2 is sufficient.

But if the a_i are up to 1e6, then the max_num would be 1e6+1.

So the code:

Read the list a.

Compute all the numbers in the candidates (a_j, a_j+1, a_j-1) for all a_j in a.

Find the maximum number among these.

If the maximum number is 0 (but a_j >=1, so a_j-1 can be 0, but we skip numbers <2).

But to be safe, compute SPF up to max(2, max_num).

Once SPF is computed, for each number in the candidates (a_j, a_j+1, a_j-1), factorize it using SPF.

So code:

Read n, x, y.

a = list of integers.

candidates = set()

for num in a:

    for delta in [0, 1, -1]:

        temp = num + delta

        if temp <2:

            continue

        candidates.add(temp)

max_num = max(candidates) if candidates else 0

if max_num <2:

    # no possible primes. So no candidate d's. But in this case, the list must be modified.

    # For example, all a_j are 1. Then, a_j+1 is 2, which would be in the candidates.

    # So this case is not possible.

    pass

But wait, candidates is built from a_j+delta, which for a_j=1, delta=0 is 1, delta=1 is 2, delta=-1 is 0. So for a_j=1, the candidates added are 1+0=1 (temp=1, but <2, so not added), 1+1=2, 1-1=0 (ignored). So 2 is added.

So the candidates set will contain 2.

So the code proceeds.

Now, compute SPF up to max_num.

Once SPF is computed, for each number in candidates, factorize into primes.

So code:

# Precompute smallest prime factors up to max_num

spf = list(range(max_num +1))

for i in range(2, int(max_num**0.5)+1):

    if spf[i] ==i:

        for j in range(i*i, max_num+1, i):

            if spf[j] ==j:

                spf[j] =i

Then, for each number in candidates:

def get_primes_spf(n):

    primes = set()

    if n <2:

        return primes

    while n !=1:

        p = spf[n]

        primes.add(p)

        while n %p ==0:

            n //=p

    return primes

So for each number in candidates, get its primes using get_primes_spf.

Collect all these primes into a set of candidate d's.

Now, the code.

So the code for this part:

candidate_primes = set()

for num in candidates:

    primes = get_primes_spf(num)

    candidate_primes.update(primes)

if not candidate_primes:

    # no primes found. But this is impossible because 2 must be in the candidates.

    # So proceed.

Now, for each d in candidate_primes:

compute the cost.

Then select the minimal cost.

Now, the code.

But even with this optimization, for large max_num (like 1e6+1), precomputing the SPF array takes O(n log log n) time. For n=1e6+2, this is manageable in Python.

But the SPF array is built in O(n log log n) time.

Now, code:

So, putting it all together.

Read input.

Process the a list to collect all candidate numbers (a_i, a_i+1, a_i-1).

Compute the SPF array for the maximum number.

Collect all primes from these candidate numbers.

For each prime d, compute the cost.

Choose the minimal cost.

Now, code:

But in Python, the SPF array for 1e6+2 is manageable.

Now, code.

Testing the first sample:

Sample input 1:

4 23 17

1 17 17 16

The candidate numbers are:

1+0=1 (ignored), 1+1=2, 1-1=0 (ignored).

17+0=17, 17+1=18, 17-1=16.

17 same as above.

16+0=16, 16+1=17, 16-1=15.

So the candidate numbers are 2,17,18,16,15,17.

The primes in these numbers are:

2's factors: 2.

17: 17.

18: 2,3.

16: 2.

15:3,5.

So the candidate_primes are {2,3,5,17}.

For each of these primes:

d=2:

For each a_j:

1: need to add 1 (k=1). cost 17*1=17. min(23,17)=17.

17: 17%2=1. k=1. cost 17. min(23,17)=17. So sum is 17*4=68. But since not all are deleted, the sum is 68. Which is higher than the sample's answer.

d=17:

For a_j=1: k=16. cost 17*16=272. min(23,272) → 23.

17: 0. cost 0.

16: k=1. cost 17. 17 <23.

Sum is 23 (for 1) +0+0 +17 =40. Which is the sample's answer.

So this is chosen as minimal.

Thus, the code works.

Another sample:

Sample input 2:

10 6 2

100 49 71 73 66 96 8 60 41 63

The output is 10.

What's the optimal d here?

The output is 10. Let's see.

The optimal d could be 7. Because in the note, the output is 10. Let's see.

But perhaps the optimal approach is to delete one element and others are okay.

But without knowing, the code should handle it.

Now, the code.

Now, the code:

Implementing all this in Python.

But in Python, for n=5e5 and candidates up to say 1e6, the code must be efficient.

Now, the code:

Read n, x, y.

Read the a list.

Collect all numbers in candidates.

Compute max_num.

Precompute SPF.

Collect primes.

For each prime d, compute the cost.

Now, code:

But code for SPF:

The code for SPF in Python:

def compute_spf(max_num):
    spf = list(range(max_num + 1))
    for i in range(2, int(max_num**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i*i, max_num+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

But when max_num is 0 or 1, but in such cases, there are no primes.

But the candidates should have at least 2.

Now, the code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, x, y = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))
    
    # Collect all numbers: a_j, a_j+1, a_j-1
    candidates = set()
    for num in a:
        for delta in [0, 1, -1]:
            temp = num + delta
            if temp >=2:
                candidates.add(temp)
    
    if not candidates:
        # All elements are 1, then the candidates would include 2
        # So this case is not possible
        print(0, file=output_stream)
        return
    
    max_num = max(candidates)
    # Compute SPF up to max_num
    spf = list(range(max_num +1))
    for i in range(2, int(max_num**0.5) +1):
        if spf[i] == i:
            for j in range(i*i, max_num+1, i):
                if spf[j] == j:
                    spf[j] = i
    
    def get_primes(n):
        primes = set()
        if n <2:
            return primes
        while n !=1:
            p = spf[n]
            primes.add(p)
            while n %p ==0:
                n //=p
        return primes
    
    candidate_primes = set()
    for num in candidates:
        primes = get_primes(num)
        candidate_primes.update(primes)
    
    if not candidate_primes:
        # All candidates are 1, which is impossible
        print(0, file=output_stream)
        return
    
    min_total = float('inf')
    
    for d in candidate_primes:
        total =0
        all_deleted = True
        min_extra = float('inf')
        for aj in a:
            rem = aj %d
            if rem ==0:
                cost_mod =0
            else:
                k = d - rem
                cost_mod = y *k
            if cost_mod <x:
                total += cost_mod
                all_deleted = False
            else:
                total +=x
                extra = cost_mod -x
                if extra < min_extra:
                    min_extra = extra
        if all_deleted:
            # Need to choose one element to keep
            if min_extra == float('inf'):
                # impossible, since all elements are deleted but aj exists
                continue
            total += min_extra  # because total was n*x, now it's (n-1)*x + (x + min_extra) = total + min_extra
        if total < min_total:
            min_total = total
    
    print(min_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 6 2
100 49 71 73 66 96 8 60 41 63
""",
            "output": \
"""\
10
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

Sample input 2:

10 6 2

100 49 71 73 66 96 8 60 41 63

The output is 10.

The code would collect primes from a_i, a_i+1, a_i-1. For example, 100: factors 2,5. 49:7. 71:71. 73:73. 66: 2,3, 11. etc.

The optimal d could be 7.

But let's see:

For d=7.

For each element:

100: 100%7= 100-7*14= 100-98=2. So k=5. cost_mod=2*5=10. Which is higher than x=6. So delete cost is 6.

49: 49%7=0. cost_mod=0. So add 0.

71: 71%7= 71-7*10=71-70=1. k=6. cost_mod=2*6=12>6 → delete cost 6.

73%7=73-7*10=3 → k=4. cost_mod=8>6 → delete.

66%7=66-7*9=66-63=3 →k=4 → cost 8>6 → delete.

96%7=5 →k=2 → cost 4 → <6 → cost 4.

8%7=1 →k=6 → cost 12>6 → delete.

60%7=60-7*8=60-56=4 →k=3 → cost 6. Which is equal to x=6. So min is 6. But since cost_mod is 6 and x is 6, choose either.

If choose x, then it's added to the sum. But need to check if all are deleted.

But 49's cost is 0, so all_deleted is False.

So the sum for d=7 would be:

100:6

49:0

71:6

73:6

66:6

96:4

8:6

60:6

41:41%7=41-7*5=41-35=6 →k=1 → cost 2. Which is <6 → added as 2.

63:63%7=0 →0.

So sum is 6+0+6+6+6+4+6+6 +2 +0 = 42. But this can't be the answer. But the sample output is 10. So there must be a better d.

Alternatively, perhaps the optimal d is 2.

For d=2:

Each even number requires no cost. Odd numbers require adding 1 (cost 2).

For the elements:

100 even →0.

49 odd →2.

71 →2.

73→2.

66 even→0.

96→0.

8→0.

60→0.

41→2.

63→2+1=odd →2.

So sum for each element:

For 49,71,73,41,63: cost_mod is 2 each. x=6. So min(6,2) is 2 each. Sum 2*5=10. Other elements are 0. So total sum is 10. Since there are elements not deleted (the even ones), the sum is 10. So this is the minimal.

So the code would choose d=2, sum is 10.

Thus, the code works.

Thus, the code should handle all test cases correctly.
</think>

```python
import sys

def main():
    n, x, y = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    candidates = set()
    for num in a:
        for delta in [0, 1, -1]:
            temp = num + delta
            if temp >= 2:
                candidates.add(temp)
    
    if not candidates:
        print(0)
        return
    
    max_num = max(candidates)
    spf = list(range(max_num + 1))
    for i in range(2, int(max_num**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_num + 1, i):
                if spf[j] == j:
                    spf[j] = i
    
    def get_primes(n):
        primes = set()
        if n < 2:
            return primes
        while n != 1:
            p = spf[n]
            primes.add(p)
            while n % p == 0:
                n //= p
        return primes
    
    candidate_primes = set()
    for num in candidates:
        candidate_primes.update(get_primes(num))
    
    if not candidate_primes:
        print(0)
        return
    
    min_total = float('inf')
    
    for d in candidate_primes:
        total = 0
        all_deleted = True
        min_extra = float('inf')
        for aj in a:
            rem = aj % d
            if rem == 0:
                cost_mod = 0
            else:
                k = d - rem
                cost_mod = y * k
            if cost_mod < x:
                total += cost_mod
                all_deleted = False
            else:
                total += x
                extra = cost_mod - x
                if extra < min_extra:
                    min_extra = extra
        if all_deleted:
            if min_extra != float('inf'):
                total += min_extra
        if total < min_total:
            min_total = total
    
    print(min_total)

if __name__ == "__main__":
    main()
```
