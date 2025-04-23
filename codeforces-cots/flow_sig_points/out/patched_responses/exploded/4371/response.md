<think>
Okay, I need to solve this problem where I have to compute the sum of happiness for all permutations of length n, modulo m. The constraints are up to n=250,000, which is pretty big. So, a brute force approach is definitely out of the question. I need to find a mathematical formula or some pattern that can be computed efficiently.

Let me start by understanding what a framed segment is. From the problem statement, a framed segment [l, r] is one where the maximum element minus the minimum in the subsegment equals r-l. Since the permutation has distinct elements from 1 to n, the max and min in any subsegment are part of that permutation.

Wait, for a subsegment of length 1, max - min is 0, which equals r-l (since r=l, so 0). So all single-element subsegments are framed. That contributes exactly n*(n+1)/2 to each permutation's happiness? Wait, no. Wait, each permutation has n elements, and each has exactly n subsegments of length 1 (each [i,i] for i from 1 to n). So each permutation contributes n such segments. But the sum over all permutations would be n! * n, because every permutation has n single-element framed segments. But wait, the first sample input is n=1, output 1. Which fits: 1! *1 =1. So that part is correct. So that's a starting point.

Then, the problem is about the other subsegments of length >=2. So the total happiness for all permutations is equal to the sum for all permutations of the number of framed segments. Each framed segment of length >=2 contributes 1 to the happiness of the permutation.

So the total sum is (number of permutations) * (number of single-element segments) + sum over all permutations of the number of framed segments of length >=2.

Wait, but the single-element segments are always present. So the total sum is n! * n (from single elements) plus the sum over all permutations of the count of framed segments of length >=2.

So the key part is to compute the sum over all permutations of the count of framed segments of length >=2. Then add n! * n, then take modulo m.

So how do I compute that sum?

Let's think for a given subsegment [l, r] (l < r), how many permutations have this subsegment as a framed segment. Then multiply that by the number of permutations where this is true, and sum over all possible l and r (with l <= r). For l=r, each contributes 1 per permutation, so sum of l<=r is n! * n as we said.

So for the l < r case, each [l, r] contributes to the sum the number of permutations where [l, r] is a framed segment, multiplied by 1. So the total sum is sum_{l=1 to n} sum_{r=l to n} (number of permutations where [l, r] is framed).

So for each interval [l, r], compute the number of permutations where that interval is a framed segment, then sum all those numbers, and add n!*n (since for l=r, each contributes exactly 1 per permutation).

So the problem reduces to, for each interval [l, r], compute how many permutations of size n have that interval as a framed segment, then sum all those and add n!*n.

But for n up to 250,000, iterating over all possible O(n^2) intervals is impossible. So we need a smarter approach.

Let me think: For a given interval [l, r], the condition for being a framed segment is max - min = r - l. Since the permutation is of distinct elements, the max and min are unique in the interval.

Wait, for a framed segment [l, r], the max and min must be exactly the endpoints of the interval. Because, suppose the interval has length k = r - l + 1. Then the max and min of the interval must be such that max - min = k-1 (since r-l is (k-1)). Since all elements are distinct, the elements in the interval must form a consecutive sequence of integers. Because the maximum and minimum are consecutive with the length. For example, if the interval has elements 3, 1, 2. The max is 3, min is 1, difference is 2, which is equal to 3-1 =2 (since r-l=2, so difference is r-l). So this interval would be a framed segment. So the elements in the interval [l, r] must form a consecutive set of integers, but arranged in any order. But how?

Wait, the condition max - min = r-l. Because for the interval [l, r], the length is (r - l +1). So the difference between max and min in the interval must be (r-l). So for example, if the interval has elements {3,4,5}, then max is 5, min is 3, difference is 2, which equals 3-1=2 (r-l=3-1=2? Wait, wait no. The length is 3 elements, l and r here would be indices, but perhaps that's a confusion. Let's clarify.

Wait, the interval [l, r] refers to the elements from position l to position r (inclusive). The length of the interval is (r - l + 1) elements. For this interval to be a framed segment, the max - min must equal (r - l). So for example, if the interval has length 3 (elements at positions 1,2,3), then the max minus min must be 2. Which implies that the elements form a consecutive sequence. Because in a consecutive sequence of three elements, the max and min differ by 2.

So the elements in the interval [l, r] must be a set of consecutive integers. So the key is that the interval [l, r] in the permutation is a set of consecutive integers arranged in any order, and the rest of the permutation can be anything as long as the entire permutation is a permutation of 1..n.

So, for a given interval [l, r], how many permutations have exactly the elements in positions l to r forming a set of consecutive integers. But note that in the permutation, those elements can be arranged in any order, as long as their min and max differ by (r-l). Which is equivalent to them being a consecutive set.

So for a given interval of length k (k = r-l+1), the number of permutations where the elements in positions l to r are exactly some consecutive k integers (but arranged in any order), and the rest of the permutation can be any permutation of the remaining numbers, with the positions outside [l, r] filled with those numbers.

Wait, but the elements in [l, r] can be any consecutive sequence of k integers. So first, we need to choose which consecutive sequence they are. For example, the possible min of the interval can be from 1 to (n - k + 1). Because if the interval has elements with min m, then the max is m + (k-1). So m can be from 1 to (n - (k-1)).

So for a given interval [l, r] of length k, the number of possible consecutive sequences is (n - k + 1). For each such sequence, we can arrange the elements in the interval in any order (k! ways), and arrange the remaining elements in the other positions in any order ((n -k)! ways). So the total for a fixed interval [l, r] is (n -k +1) * k! * (n -k)!.

But wait, this is under the assumption that the elements in the interval [l, r] are exactly those consecutive numbers, and the rest of the permutation is filled with the remaining numbers. However, this would count the permutations where the interval [l, r] is a consecutive sequence of integers, but we also need to ensure that in the permutation, the interval [l, r] is a framed segment. But since the elements in the interval are a consecutive sequence, their max and min differ by (k-1) (since k is the length). So the condition max - min = (r-l) (since the interval is from l to r, which has length k, so r-l = k-1). So yes, this satisfies the condition.

Therefore, for each interval [l, r], the number of permutations where [l, r] is a framed segment is (n -k +1) * k! * (n -k)!, where k is the length of the interval (k = r-l+1).

But wait, this is only true if the interval [l, r] in the permutation is exactly a set of consecutive integers, but the rest of the permutation is filled with the remaining numbers. However, this counts all such possibilities, regardless of other framed segments. So this is correct for the contribution of the specific interval [l, r].

But then, when summing over all intervals, we have to consider that a permutation can have multiple intervals. However, the problem asks for the sum over all permutations of the number of framed segments. So each permutation contributes 1 for each framed segment it has, and the total sum is the sum of all such contributions. So the approach of summing over all intervals the number of permutations where that interval is a framed segment is correct. Because each interval's contribution is added once for each permutation that includes it as a framed segment.

So this approach is valid.

Therefore, the sum over all permutations of the number of framed segments (excluding the single-element ones) is equal to the sum over all intervals [l, r] (l <= r) of (n -k +1) * k! * (n -k)!, where k is the length of the interval.

But wait, for intervals of length 1 (k=1), this formula gives (n -1 +1) *1! * (n-1)! )=n *1*(n-1)! )=n! ), which is the same as the single-element contributions. But we already accounted for that in the initial part (n!*n). Wait, the initial part is for all single-element intervals. So each [i,i] contributes n! (since for each permutation, the single element is a framed segment). But there are n such intervals (each single position), so the sum for all single-element intervals is n * n!.

But according to the formula, for k=1, each interval [i,i] contributes (n -1 +1) *1! * (n-1)! )=n *1*(n-1)! )=n! ). So summing over all n intervals of length 1 gives n * n! ), which is exactly the same as the initial part.

So the total sum S is equal to sum_{k=1}^n [ (number of intervals of length k) * (n -k +1) * k! * (n -k)! ) ].

But wait, the formula (n -k +1) * k! * (n -k)! ) is for each interval of length k. But the number of intervals of length k is (n -k +1). Because for each possible start position l, the interval [l, l +k-1] is of length k, and l can range from 1 to n -k +1. So the number of such intervals is (n -k +1). So for each k from 1 to n, the contribution to the sum is (n -k +1) * (n -k +1) * k! * (n -k)! ) ?

Wait, no. Wait, for each interval of length k, the contribution is (n -k +1) * k! * (n -k)! ). But the number of intervals of length k is (n -k +1). So for each k, the total contribution is (number of intervals) * (per-interval contribution).

Wait, no. For each interval of length k, the per-interval contribution is (n -k +1) *k! * (n -k)! )? Wait, that's not right. For each interval of length k (like [l, r] where r-l+1 =k), the per-interval contribution is (n -k +1) * k! * (n -k)! ), because for each such interval, the number of permutations where the interval is framed is (n -k +1) *k! * (n -k)! ) ?

No, I think I made a mistake here. Let me re-express:

For a fixed interval [l, r] of length k (r-l+1 =k), the number of permutations where [l, r] is a framed segment is:

possible consecutive sequences (choose the min m, then the max is m +k-1). The number of possible m is (n - (m +k-1) +1) +1? Wait, no. The min can be from 1 to (n -k +1). Because if the consecutive sequence is of length k, the min can be as low as 1, and as high as (n -k +1), since the max would be m +k-1 <=n. So the number of possible consecutive sequences is (n -k +1).

Then, for each such consecutive sequence, the elements in [l, r] must be a permutation of the consecutive numbers, and the rest of the elements can be any permutation of the remaining numbers.

But the elements in the interval can be arranged in k! ways, and the remaining elements can be arranged in (n -k)! ways. Also, the consecutive sequence can be any of the (n -k +1) possible sequences. So for a fixed interval [l, r], the number of permutations where [l, r] is a framed segment is (n -k +1) * k! * (n -k)! ).

Therefore, for each interval [l, r], the contribution is (n -k +1)*k!*(n -k)! ). The number of such intervals of length k is (n -k +1). So the total contribution for all intervals of length k is (n -k +1) * (n -k +1) * k! * (n -k)! ) = (n -k +1)^2 * k! * (n -k)! ).

But wait, the sum S is the sum over all intervals (all l <= r) of the per-interval contribution. So S = sum_{k=1 to n} [ (n -k +1) * (n -k +1) * k! * (n -k)! ) ].

But wait, that's not correct. Because for each k, the number of intervals of length k is (n -k +1), and each contributes (n -k +1)*k!*(n -k)! ). So the total contribution for all intervals of length k is (n -k +1) * (n -k +1) *k! * (n -k)! ). So for each k, we have (n -k +1)^2 * k! * (n -k)! ) summed over all k from 1 to n.

But this would make the sum S = sum_{k=1 to n} (n -k +1)^2 *k! * (n -k)! )

But this seems computationally expensive for n up to 250,000. How can we compute this efficiently?

Let's note that (n -k +1) is equal to (n - (k-1)), since k is the length. Let me reindex the sum.

Let's let i = k-1. Then k = i+1. So for k from 1 to n, i ranges from 0 to n-1. But perhaps this isn't helpful. Alternatively, let's set m = n -k +1. Then for k from 1 to n, m ranges from n (when k=1) down to 0 (when k=n+1, but k can't exceed n). Wait, for k=1, m =n -1 +1 =n. For k=2, m =n-2+1 =n-1. So m decreases by 1 as k increases by 1.

So the sum can be rewritten as sum_{m=1 to n} m^2 * ( (n -m +1)! ) * (m-1)! ) )

Wait, no. Let's substitute m = n -k +1. Then k = n -m +1. But then when k is varying from 1 to n, m ranges from n down to 1 (when k=1, m =n; when k=n, m=1). Then the sum becomes sum_{m=1 to n} m^2 * ( (n -m +1)! ) * (m-1)! ) ). Wait, how?

Because for each m in 1..n, the term is m^2 (since (n -k +1) =m) multiplied by k! (k =n -m +1) and (n -k)! = (m-1)! (since n -k = m-1). Because k = n -m +1, so n -k = m-1.

So for each m from 1 to n, the term is m^2 * (n -m +1)! * (m-1)! )

But sum_{k=1 to n} (n -k +1)^2 * k! * (n -k)! ) is equivalent to sum_{m=1 to n} m^2 * (n -m +1)! * (m-1)! ), where m = (n -k +1). Wait, perhaps not. Let me check for k=1:

For k=1, m =n -1 +1 =n. So the term is n^2 *1! * (n-1)! ). Which is n^2 *1 * (n-1)! ) = n^2 (n-1)! ) = n *n! )

But according to the original formula, for each k=1, the term is (n -k +1)^2 *k! * (n-k)! ) = n^2 *1! * (n-1)! ), which matches.

So the sum can be written as sum_{m=1}^n m^2 * ( (n -m +1)! ) * (m-1)! )

But how can we compute this sum efficiently for n up to 250,000?

Hmm, but wait, for each m in 1..n, the term is m² * (n -m +1)! * (m-1)! )

But this seems tricky. Let's see if we can find a pattern or a way to precompute factorials and combine terms.

Alternatively, let's think about the term for each possible k (the length of the interval). For each k, the term is (n -k +1)^2 * k! * (n -k)! )

So for example, when k=1: (n)^2 *1! * (n-1)! ) =n² * (n-1)! )

But 1! * (n-1)! ) = (n-1)! ), so the term is n² * (n-1)! ) =n *n! )

Similarly, when k=2: (n-1)^2 * 2! * (n-2)! ) = 2 (n-1)^2 (n-2)! )

But 2 (n-2)! ) * (n-1)^2 = 2 (n-1)^2 (n-2)! )

But (n-1) * (n-2)! ) = (n-1)! ), so this term is 2 (n-1) * (n-1)! )

Which can be rewritten as 2 (n-1) * (n-1)! ) = 2 (n! ) / (n/(n-1))? Not sure.

Alternatively, perhaps there's a way to find a pattern here.

Wait, let's consider that the sum is S = sum_{k=1}^n (n -k +1)^2 *k! * (n -k)! )

Let me try to find a recurrence relation for S(n). For example, can we express S(n) in terms of S(n-1)?

Not sure. Let's compute S for small n.

For n=1:

k can be 1. The term is (1)^2 *1! *0! =1*1*1=1. So S=1.

Which matches the first sample input (sum is 1! *1 (single element) plus sum of other terms (0)). But according to the initial approach, the total sum is S= sum over all intervals of their contribution, including single elements. So in this case, the sum is 1, which is correct.

Sample input n=2:

The sum S would be:

k=1: (2)^2 *1! *1! =4*1*1=4 (but for two intervals of length 1, each contributes 2^2 *1! *1! ? Wait, no, the sum over k=1 would have (n -k +1) terms. For n=2, k=1, the number of intervals is 2. Each contributes (2-1+1)^2 *1! * (2-1)! )? No, wait for k=1, each interval of length 1 is [1,1] and [2,2], which are two intervals. The per-interval contribution is (n -k +1) =2 for each. Wait, no. Wait, for k=1, the per-interval contribution is (n -k +1) *k! * (n -k)! ). But n -k +1 here is 2-1+1=2. So for each interval of length 1, the contribution is 2 *1! * (2-1)! )=2 *1 *1=2. Since there are two intervals of length 1 (each single element), their total contribution is 2*2=4.

For k=2: the interval is [1,2]. The contribution is (2-2+1)^2 *2! * (2-2)! ) = (1)^2 *2 *1 =2. So the total sum S is 4 +2=6. But the sample input n=2 output is 6. Which matches the second sample. So yes, this formula gives S=6 for n=2.

Wait, but according to the problem statement, the total sum is n!*n (for single elements) plus the sum of framed segments of length >=2. But according to the sample input n=2, the output is 6, which is exactly this sum. Because for n=2, the sum of all permutations' happiness is 6. Which is S=6. So yes, the formula S is indeed the correct sum.

So the formula seems correct.

Now, the problem is to compute S mod m, where S is the sum of the terms (n -k +1)^2 *k! * (n -k)! for k from 1 to n.

But for n up to 250,000, how can we compute this efficiently?

First, note that factorials up to n are needed, and perhaps their inverses. But since m is a prime (as per input constraints), and up to 1e9, perhaps we can precompute the factorials modulo m.

Wait, but the modulus m can be up to 1e9, and n up to 250,000. So 250,000! is way larger than 1e9, so we need to compute each factorial modulo m. But 250,000! mod m can be zero if m is a prime less than or equal to 250,000. However, m can be as small as 1e8, which is larger than 250,000. For example, for n=250,000, if m is 1e8 + 3 (a prime), then 250,000! mod m would not be zero. So we need to compute all factorials modulo m.

So the steps to compute S mod m are:

1. Precompute factorial up to n, mod m: fact[i] = i! mod m.

2. Precompute (n -k +1) for all k from 1 to n. (n -k +1) is (n+1 -k).

3. For each k from 1 to n, compute term = (n+1 -k)^2 * fact[k] * fact[n -k] mod m.

4. Sum all terms, then mod m.

But the issue is that (n+1 -k) is up to 250,000, so (n+1 -k)^2 can be up to (250,000)^2 =6.25e10. So when multiplied by fact[k] and fact[n -k], which are mod m, but even before mod, the product can be very large. So we need to compute each term modulo m, avoiding overflow.

But in Python, integers can be arbitrarily large, so as long as each step is computed modulo m, it's manageable.

So the steps are:

Compute fact[0..n], where fact[i] = i! mod m.

Then for each k in 1..n:

term = ( ( (n+1 -k) ** 2 ) % m ) * ( fact[k] ) % m * ( fact[n -k] ) % m 

Sum all these terms mod m.

But for n=250,000, this would require O(n) time, which is acceptable.

But wait, how to compute fact[i] mod m for i up to 250,000?

Yes. We can compute fact[0] =1, fact[i] = fact[i-1] * i mod m.

So the code can be structured as follows:

Read n and m.

Compute fact as an array where fact[0] =1, fact[i] = (fact[i-1] * i) % m for i from 1 to n.

Then, sum over k from 1 to n of ( (n+1 -k)^2 * fact[k] * fact[n -k] ) mod m.

Then, output sum mod m.

Wait, but let's test with the sample inputs.

Sample 1: n=1, m=...

sum for k=1:

term = (1+1 -1)^2 * fact[1] * fact[0] = (1)^2 * 1 *1 =1. Sum is 1. Output 1. Correct.

Sample 2: n=2.

k=1: term is (2+1-1)^2 * fact[1] * fact[2-1] → (2)^2 *1 *1 →4*1*1=4.

k=2: term is (2+1-2)^2 * fact[2] * fact[0] →1^2 *2 *1 →1*2*1=2.

Sum 4+2=6. Correct.

Sample 3: n=3.

sum over k=1,2,3.

k=1: (3+1-1)^2 *1! * (3-1)! =3^2 *1 *2=9*2=18.

k=2: (3+1-2)^2 *2! * (3-2)! →(2)^2 *2 *1=4*2=8.

k=3: (3+1-3)^2 *3! *0! →1^2 *6 *1=6.

Total sum 18+8+6=32. Which matches the third sample. So yes, the formula is correct.

So the code can be written as follows.

But how to handle fact[n -k] when n -k can be up to n-1. For example, when k=1, n-k =n-1. So when precomputing fact up to n, fact[n -k] is available.

Yes.

So the code steps:

Read n and m.

Compute fact array.

Initialize sum as 0.

For k in 1 to n:

    a = (n+1 -k) % m

    a_sq = (a * a) % m

    term = (a_sq * fact[k]) % m

    term = (term * fact[n -k]) % m

    sum = (sum + term) % m

Output sum mod m.

Yes.

Now, the edge cases.

For n=0, but according to constraints n>=1.

For m up to 1e9, but in Python, handling large exponents is manageable.

But for (n+1 -k) squared, even for n=250,000, (250,001 -k)^2 can be up to 250,000^2 =6.25e10. But when mod m, this is ( (n+1 -k) mod m )^2 mod m. Which can be computed correctly.

So the code is correct.

Thus, the solution is to compute the sum as described and output it mod m.

Now, let's implement this in Python.

The code:

Read n and m.

Precompute fact array.

Compute the sum.

But for n up to 250,000, precomputing the factorial array is O(n), which is acceptable.

Sample 3:

n=3.

fact[0]=1

fact[1]=1*1 mod m.

fact[2]=1*2 mod m.

fact[3]=2*3 mod m.

So for k=1, fact[1]=1, fact[3-1]=fact[2]=2 mod m.

Thus, for k=1: (3+1 -1)=3 → 3²=9 mod m. Then 9*1*2=18 mod m.

Similarly for other terms.

Yes.

So the code should work.

Testing sample 3:

n=3, m=993244853.

sum is 18 +8 +6=32 → 32 mod m is 32. Which matches the sample.

So the code is correct.

Now, implement this in Python.
</think>

```python
n, m = map(int, input().split())

if n == 0:
    print(0 % m)
    exit()

# Precompute factorial modulo m
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i-1] * i % m

total = 0
for k in range(1, n + 1):
    a = (n + 1 - k) % m
    a_sq = a * a % m
    term = a_sq * fact[k] % m
    term = term * fact[n - k] % m
    total = (total + term) % m

print(total % m)
```