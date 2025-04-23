<think>
Okay, let's try to understand this problem. So Simon has this prime number x and an array of non-negative integers. He creates a sum of fractions where each term is 1/(x^a_i). Then he combines them into a single fraction s/t, where t is x raised to the sum of all a_i's. Now, we need to find the GCD of s and t modulo 1e9+7.

Hmm, right. So first, let's think about how to compute s and t. But since both can be very large, directly computing them is impossible. We need a smarter approach here.

Wait, but the problem is to find the GCD of s and t. Since x is prime, maybe we can find the exponents of x in s and t. Because the GCD will be x raised to the minimum of the exponents in s and t. Because x is prime, the GCD's prime factors can only include x. Because any other prime factor in s would not divide t, since t is a power of x.

Oh right! That's a crucial insight. So the GCD of s and t is x^k, where k is the minimum of the exponent of x in s and the exponent of x in t. But wait, the exponent of x in t is the sum of all a_i's. So what about the exponent of x in s?

Let's break it down. The sum s is the sum of all the fractions, after bringing to a common denominator. The common denominator is x^A, where A is the sum of all a_i's. Each numerator is x^(A - a_i). So s is the sum of x^(A - a_i) for all i. Then s is equal to sum(x^{A - a_i}) divided by x^A, but when written as s/t, t is x^A, so s is the sum of those numerators.

But how do we find the exponent of x in s? Because s is the sum of terms x^{A - a_i}. Let's think. Since x is prime, the sum's exponent of x will be the minimal exponent among the terms, but only if all other terms are multiples of x^k. Let's see.

For example, in the first sample: a1 and a2 are both 2. So A is 4. Each term in the sum is x^(4-2) = x^2. So sum is 2*x^2. So s is 2x^2, and the exponent of x in s is 2. The exponent in t is 4. So the GCD is x^2, which is 8 in the sample. That's correct.

Another example: if all a_i are zero, like the fourth sample. Then each term is x^0 =1, sum is 4. So s is 4. The exponent of x in s is zero (since x is prime, and 4 is not divisible by 5, which is the x in that case). So GCD is x^0=1.

So the key is to find the minimal exponent of x in the sum of the terms. The sum is S = sum(x^{A - a_i} for each i). The exponent of x in S is the minimal number of factors of x in each term. But wait, because when you add numbers, the minimal exponent among them is the exponent of x in the sum if there's a term that is not divisible by x^k+1. So for example, if you have terms like 3 + 3, sum is 6. If x=2, then the exponents are 0 for each term, sum is 6 which has exponent 1. Wait, no. Wait, 3 is not divisible by 2, so the exponent of 2 in 3 is 0. But 3+3=6, which is 2*3. So exponent is 1. So in this case, the exponent is the minimal exponent plus how much more you can take. Wait, this seems like a more complicated case.

Wait, perhaps the exponent of x in S is the minimal exponent of x in any term when all terms are divided by x^m, where m is the minimal exponent.

Wait, let me think. Let's say all terms are x^k * (some integers not divisible by x). Then when you sum them, if at least one of those integers is not divisible by x, then the sum's exponent of x is k. But if all the integers are divisible by x, then the sum would be x^k * (sum of terms divisible by x) = x^{k+1} * ... etc. So the exponent is k plus the exponent of the sum of the coefficients after dividing by x^k.

Hmm. So the approach is: find the minimal exponent m in all terms (since each term is x^{A - a_i}), but since the a_i's are sorted, the exponents A - a_i are in non-increasing order. Wait, no. Let's see. The array a1 is sorted in non-decreasing order. So a1 ≤ a2 ≤ ... ≤ an. So A is the sum of all a_i's. Then A - a_i is sum of a_j's (j≠i) plus a_i's contribution. Wait, maybe not. Let me see: For example, if the array is [a1, a2, a3], then A is a1 + a2 + a3. Then A - a_i would be (a1 + a2 + a3) - a_i = sum of a_j for j≠i. But that's not necessarily sorted. Wait, for example, if the array is [0,1,2], then A is 3. The terms are 3-0=3, 3-1=2, 3-2=1. So sorted in descending order, so the exponents are 3, 2, 1. So the sum would be x^3 + x^2 + x^1. The exponents of each term are 3,2,1. The minimal exponent here is 1, but the sum is x + x² + x³. The sum can be written as x(1 + x + x²), which is x multiplied by (x² + x +1), which is not divisible by x. So the exponent of x in the sum is 1. So the minimal exponent in the terms is 1, so the exponent in the sum is 1.

So the exponent of x in S is the minimal exponent m among all terms, unless all terms after dividing by x^m sum to a multiple of x, in which case the exponent is higher.

Wait, but how do we compute that?

So here's the process: Find the minimal exponent m in the terms. Then, count how many terms have this minimal exponent. If that count is not divisible by x, then the exponent of x in S is m. Otherwise, we have to add 1 to m and check if the count divided by x is divisible by x again, and so on.

Wait, that's the key. Because when you sum terms of x^m * c_i, where c_i is not divisible by x. Then the sum is x^m * sum(c_i). If sum(c_i) is divisible by x, then the total sum is x^{m+1} * (sum(c_i)/x). Then you check if that sum is divisible by x again, and so on. But since x is prime, the sum's exponent is m + k, where k is the exponent of x in sum(c_i).

So the steps are:

1. Find m, the minimal exponent in the exponents (A - a_i) for each term.

2. Collect all terms, which are x^{A - a_i} = x^{sum(a_j) - a_i} for each i.

Wait, but sum(a_j) is A. So each term is x^{A - a_i}.

But since the a_i are sorted in non-decreasing order, the exponents A - a_i are in non-increasing order. Because as a_i increases, A -a_i decreases.

Wait, no. For example, if the array is [1,2], then A is 3. The exponents are 3-1=2 and 3-2=1. So exponents are in decreasing order. But if the array is [1,1], then A=2, exponents are 1 and 1. So same. So the exponents are non-increasing.

But the array a is sorted in non-decreasing order. So for each i, a_i ≤ a_{i+1}. So A - a_i is sum of all a's (including a_i) minus a_i = sum of a_j for j≠i. But as i increases, a_i increases, so sum of a_j (excluding a_i) could be varying. Wait, no. Let's take array [a_1, a_2, ..., a_n], sorted in non-decreasing order. Then A is the sum of all a_i. For each term, exponent is A - a_i. So for i < j, since a_i ≤ a_j, A - a_i ≥ A - a_j. So the exponents are in non-increasing order.

So the exponents of the terms are in non-increasing order. So the first term (i=0) has the highest exponent, and the last term (i=n-1) has the smallest exponent.

So the minimal exponent m is the exponent of the last term. Or wait, wait, if all exponents are the same, then all terms have the same exponent. But in the first sample, all a_i are 2, so A=4. Each term is 4-2=2. So exponents are 2. So sum is 2x². So exponent is 2. Which is the minimal exponent. Then, since sum is 2x², which is not divisible by x³, the exponent is 2.

But how do we find the minimal exponent and the count of terms with that exponent?

Wait, the minimal exponent m is the minimal among all exponents. Since the array is sorted in non-decreasing order, a_1 ≤ a_2 ≤ ... ≤ a_n. So A is the sum, which is fixed. Then, for each i, the exponent is A - a_i. So the minimal exponent is A - a_n, since a_n is the largest.

Wait, yes! Because for each i, a_i ≤ a_n (since the array is sorted), so A - a_i ≥ A - a_n. So the minimal exponent is A - a_n, which is the exponent of the last term. So all terms with a_i = a_n will have exponent m = A - a_n. So first, we can find m = A - a_n.

Then, we need to count how many terms have exponent m. Those are the terms where a_i = a_n. Because a_i is sorted in non-decreasing order, all the terms from some index onwards will be equal to a_n. For example, in the first sample, the array is [2,2], so a_n = 2, and all terms have a_i = 2, so the count is 2. So the exponents are A - a_i = 4-2=2 for each term.

So the count is the number of elements in a that are equal to a_n.

But wait, a is sorted. So all elements from the first occurrence of a_n to the end are a_n. So for example, if the array is [0,0,1,1,1], then a_n is 1. The count is 3.

So, the minimal exponent m is (sum of a_i) - a_n. Because sum of a_i is A, so m = A - a_n.

Now, the sum S is the sum of x^{A - a_i} for all i. So all terms are x^m * x^{(A -a_i - m)}. Wait, because A -a_i is >= m. Because m is the minimal exponent. So A -a_i - m >=0.

Wait, m is the minimal exponent, so for each i, A -a_i >= m. So for terms where a_i < a_n, A -a_i would be larger than m. For terms where a_i = a_n, A -a_i is m.

So the sum can be written as x^m * (k + x^{d_1} + x^{d_2} + ...), where d_i are >=1, and k is the count of terms with exponent m. Because for those terms, x^{A -a_i} = x^m. For other terms, x^{A -a_i} = x^m * x^{(A -a_i - m)}. For example, if a term has A -a_i = m + 2, then x^{m+2} = x^m * x².

So the sum S = x^m * [k + x^{d_1} + x^{d_2} + ... ] where d_j are positive integers.

Now, the term inside the brackets is (k + sum of x^{d_j} for j). Let's call this value C. Then, the exponent of x in S is m + the exponent of x in C.

So to find the exponent of x in S, we need to compute the exponent of x in C. Since C is k plus some terms that are multiples of x (since d_j >=1), the sum of those terms is a multiple of x. So the sum of x^{d_j} is x multiplied by some integer. So, the sum of x^{d_j} is divisible by x. Then, k is the number of terms with exponent m. So C = k + (something divisible by x).

So if k is not divisible by x, then C mod x is k mod x, which is not zero, so x does not divide C. Hence, the exponent of x in C is 0. So the exponent of x in S is m.

If k is divisible by x, then C = x * (k/x + ... ), and we have to see if the new sum (k/x + ...) is divisible by x, and so on. So this becomes a process where we need to find how many times x divides into k.

Wait, but in this case, the sum of the x^{d_j} terms is divisible by x. So, the total sum C = k + (sum of x^{d_j} terms) = k + x * (sum of x^{d_j -1} terms). Since the sum of x^{d_j} terms is divisible by x, then if k is divisible by x, then C is divisible by x. So the exponent of x in C is 1 plus the exponent of x in (k/x + sum of x^{d_j -1} terms).

But this seems like a loop. Let's think of it as a process. Let's say we have C = k + D, where D is divisible by x. So if k is divisible by x, then C is divisible by x. Let's write C = x * (k/x + D/x). Let's call this new value C1. Then, we need to find how many times x divides into C1. So the exponent is m + 1 + the exponent of x in C1. But C1 is (k/x) + (D/x). Now, (D/x) is sum of x^{d_j - 1}, which is again divisible by x if d_j -1 >=1. But wait, the terms x^{d_j} are x^{A - a_i - m} for a_i < a_n. Since m = A - a_n, then for a_i < a_n, A -a_i -m = (sum a_j) - a_i - (sum a_j - a_n) = a_n - a_i. Since a_i < a_n, a_n -a_i is positive. So d_j = a_n - a_i. So for these terms, x^{d_j} is x^{a_n - a_i}, which is at least x^1 (since a_i < a_n). So their sum is divisible by x. So D/x is sum x^{d_j -1} which is sum x^{a_n - a_i -1 + 1}? Wait, perhaps not. Let's see: D is the sum of x^{a_n - a_i} for a_i < a_n. Then D/x is sum x^{a_n - a_i -1} for a_i < a_n. Each term is x^{ (a_n - a_i) -1 } = x^{ (a_n - a_i -1) }, which is x^(something >=0, since a_n - a_i >=1 (since a_i < a_n and a_i is integer)).

But those terms are x raised to exponents that could be 0 or higher. For example, if a_i is a_n -1, then the exponent is 0. Then x^0 is 1, which is not divisible by x. So D/x could include terms that are not divisible by x.

Wait, but in this case, for a_i < a_n, a_n - a_i can be as small as 1 (if a_i = a_n -1). So x^{a_n - a_i} is x^1, so D/x would be 1, which is not divisible by x. So in this case, D/x is sum of x^{d_j -1} where d_j = a_n - a_i. So for a_i varying from some lower values up to a_n -1.

So in the process:

Original C is k + D, where D is divisible by x.

If k is divisible by x, then C is divisible by x, and we can proceed to compute C1 = (k/x) + (D/x).

But in C1, (k/x) is the number of terms with exponent m, divided by x. And (D/x) is the sum of x^{d_j -1}, which includes terms that may not be divisible by x.

So in the next step, the exponent of x in C1 would depend on the sum of (k/x) and the sum of terms in D/x.

But this seems complex, but perhaps there's a pattern here.

Let me consider an example. Suppose x=2, and the exponents are all 3. So m=3. The count k is 4. So the sum of x^{m} for each term is 4*2^3. So S = 4*2^3 = 2^3 * 4. Now, 4 is 2^2, so S is 2^(3+2) = 2^5. So the exponent of x in S is 3+2=5.

But according to the earlier approach, the minimal exponent m is 3. The count k is 4. Since 4 is divisible by 2, we divide k by x and add the D/x (which is zero here, since D is zero? Because in this case, all terms are of exponent m, so D is sum of x^{d_j} where d_j is zero. Wait, no. Wait, D is the sum of the terms that are exponents higher than m, which in this case, there are none. So D is zero. So C is k + D = 4 + 0 =4. So C is 4. Then, since 4 is divisible by 2, we proceed. C1 = 4/2 = 2. Now, check if 2 is divisible by 2. Yes. So C1 becomes 2/2 =1. Now, no more division. So the exponent is m (3) plus the number of times x divides into C. Which in this case is 2 times. So total exponent is 3+2=5. Which matches.

So the algorithm here is: we need to find the minimal exponent m (A - a_n), then count the number of terms with a_i = a_n (k). Then, compute how many times x divides into k. Let's call that count 'cnt'. The exponent in S is m + cnt. Then, the GCD is x^ (min(m + cnt, A)) ). But wait, t is x^A, so the exponent in t is A. So the GCD is x^ (min(m + cnt, A) ). But wait, m is A - a_n. So, if m + cnt is >= A, then the GCD is x^A. But since m = A - a_n, and cnt can be up to log_x(k) (since each time we divide by x), but a_n can be up to 1e9, so A can be up to 1e14 (since n is 1e5). But how?

Wait, but the problem states that the answer should be computed modulo 1e9+7. So we need to compute x raised to the power of the minimum of (m + cnt) and A), then take that modulo 1e9+7.

But how do we compute m + cnt and compare it to A?

Wait, m is A - a_n. So m can be written as (sum a_i) - a_n. But sum a_i is sum of all a_i, and a_n is the maximum. So m is sum of a_1 to a_{n-1}.

But how?

Wait, for example, sum of a_i is A. Then m = A -a_n = sum_{i=1 to n-1} a_i. Because A = sum a_i = sum_{i=1 to n-1} a_i + a_n. So m = sum_{i=1 to n-1} a_i.

Then, a_n can be as big as 1e9, and sum of the first n-1 a_i could be up to (1e5-1)*1e9 = 1e14. So m can be up to 1e14.

Now, the exponent in S is m + cnt. The exponent in t is A = sum a_i = m + a_n. So the minimal of (m + cnt) and (m + a_n) is either m + cnt (if cnt < a_n) or m + a_n otherwise.

So the GCD is x^ (min(m + cnt, m + a_n) ) = x^ (m + min(cnt, a_n) ).

So to compute the answer, we need to compute x raised to the power of (m + min(cnt, a_n)), modulo 1e9+7.

But how to compute cnt?

cnt is the maximum number of times x divides k. For example, k is the count of a_i equal to a_n. So k is the number of terms in a that are equal to a_n. Since the array is sorted in non-decreasing order, this is the number of trailing elements equal to a_n.

Once we have k, cnt is the maximum exponent such that x^cnt divides k. Wait, no. Because in the example where k is 4 and x is 2, cnt is 2. Because 4 is 2^2. So the exponent is 2.

So cnt is the largest e where x^e divides k. So how to compute that?

Yes. For example, if k=12 and x=3, then 3^1 divides 12, 3^2=9 does not divide 12. So cnt=1.

So to compute cnt, we can compute the maximum e where x^e divides k. To find this, we can count how many times we can divide k by x until it's no longer divisible.

But since x can be up to 1e9, and k can be up to 1e5 (since n is up to 1e5), this can be done in O(log k) time.

So the steps are:

1. Find a_n, the last element of the array (since array is sorted).

2. Compute k: the number of elements in the array equal to a_n.

3. Compute m = sum of all a_i - a_n. Which is sum of a_1 to a_{n-1} (since a_n is the last element and all elements are up to a_n).

Wait, sum of all a_i is sum_a = sum(a_i). Then m = sum_a - a_n = sum(a_1 to a_{n-1}).

But how to compute sum_a? Well, we can read all a_i, sum them up. But given that n can be up to 1e5 and a_i up to 1e9, sum_a can be up to 1e14, which is manageable in Python.

But then m can be up to 1e14 - 1e9, which is okay.

But to compute sum_a, we need to sum all a_i. Let's proceed.

4. Compute sum_a = sum(a_i). Then m = sum_a - a_n.

5. Compute cnt as the maximum e where x^e divides k. How?

We can compute cnt by initializing e=0 and looping while k is divisible by x. Increment e and divide k by x each time.

For example, k=8, x=2: e=0 → 8%2=0 → e=1, k=4 → 4%2=0 → e=2, k=2 → e=3, k=1 → loop ends. So cnt=3.

Yes.

6. Then compute the exponent as m + min(cnt, a_n). Because:

- The exponent in S is m + cnt.

- The exponent in t is m + a_n.

So the GCD exponent is the minimum of the two.

So the answer is x^(min(m + cnt, m + a_n)) mod 1e9+7.

But wait, what if x is 1e9 and the exponent is up to 1e14 + log_x(1e5). That's a very big exponent. So we need to compute x^e mod 1e9+7 efficiently.

Yes, using fast exponentiation (binary exponentiation).

So the plan is:

- Read n and x.

- Read the array a (sorted non-decreasingly).

- Find a_n = a[-1].

- Compute k as the count of elements equal to a_n (find the first index from the end where it's not equal to a_n, then k = n - that index).

But since the array is sorted, all elements from the first occurrence of a_n to the end are a_n. Wait, no. Because the array is non-decreasing, so if the last element is a_n, all elements from the first occurrence of a_n to the end are a_n. So for example, the array could be [1,2,3,3,3], then a_n is 3, and k is 3.

But to compute k, we can loop from the end and count how many elements are equal to a_n. Since the array is sorted, once we hit an element less than a_n, we can stop.

In Python, for efficiency, perhaps we can use bisect to find the first occurrence of a_n. But since the array is sorted, the last occurrence is n-1, and we can loop backward.

But for n up to 1e5, even a linear scan is acceptable.

So:

k = 0

i = n-1

while i >=0 and a[i] == a_n:

    k +=1

    i -=1

Once the loop ends, k is the count.

But since the array is sorted in non-decreasing order, once we find a[i] < a_n, all previous elements are <= a[i], so no need to check further.

So this loop is O(k) time, which is O(n) in the worst case. But given that n is up to 1e5, and per test case, it's manageable.

But perhaps a more efficient way is to use bisect to find the first index where a_i == a_n. Then the count is n - first index.

But since the array is non-decreasing, the elements equal to a_n are all at the end. So using bisect.bisect_left and bisect.bisect_right.

Wait, in Python, the bisect module can help. Let's see.

We can use bisect.bisect_left(a, a_n) → gives the first occurrence of a_n. But wait, a is sorted in non-decreasing order. So to find the first index where a_i == a_n, we can use bisect_left. Then, the last index is n-1, so the number of elements is n - bisect.bisect_left(a, a_n).

Wait, for example:

a = [2,2], a_n is 2. bisect_left returns 0. So count is 2 -0 =2.

Another example: a = [1,2,3,3,3], a_n is 3. bisect_left returns index 2. n is 5. count is 5-2=3.

Yes. So using bisect_left is O(log n) time, which is better than O(k).

So in Python code:

import bisect

k = n - bisect.bisect_left(a, a_n)

But wait, in the problem statement, the array is given as a list of integers. So, for example, in the first sample input:

The array is [2,2]. bisect.bisect_left returns 0. So k is 2-0=2. Which is correct.

Yes.

So this is a better approach for large k.

So steps to compute k:

a_n = a[-1]

k = n - bisect.bisect_left(a, a_n)

Then compute sum_a = sum(a).

m = sum_a - a_n

Then compute cnt:

We need to find how many times x divides into k. So:

cnt =0

current = k

while current % x ==0:

    cnt +=1

    current = current //x

So for example, k=0 → but since a is non-empty, and x >=2, but in the problem statement, x is a prime, and the array elements are non-negative. But k is the count of a_i equal to a_n, which is >=1 (since the array has at least one element, and a_n is the last element). So k is at least 1. So current starts as k >=1.

Wait, a is non-empty (n >=1). So a_n is the last element. So k is the number of elements equal to a_n, which is at least 1.

So current is at least 1. So the loop can proceed.

Once cnt is computed, the exponent in S is m + cnt.

The exponent in t is sum_a (since t is x^sum_a). So the GCD's exponent is the minimum of (m + cnt) and sum_a.

Wait, sum_a is m + a_n (since m = sum_a - a_n). So the exponents are:

s_exponent = m + cnt

t_exponent = m + a_n

So the GCD exponent is min(s_exponent, t_exponent) = m + min(cnt, a_n).

Because m + cnt and m +a_n: the minimum is m plus the minimum of cnt and a_n.

Because m is added to both.

So min(m + cnt, m + a_n) = m + min(cnt, a_n).

Yes. Because cnt and a_n are non-negative, adding m to both doesn't affect which is smaller.

So the final exponent is m + min(cnt, a_n).

Thus, the GCD is x^(m + min(cnt, a_n)) mod 1e9+7.

So the problem reduces to:

Compute x^(m + min(cnt, a_n)) mod MOD, where MOD is 1e9+7.

Now, m can be up to 1e5 * 1e9 = 1e14. min(cnt, a_n) can be up to a_n, which is 1e9. So the exponent can be up to 1e14 + 1e9 = 1e14 (approx). So exponent is up to 1e14.

Computing x^e mod MOD where e is 1e14 is feasible with binary exponentiation, which is O(log e) steps. Since log2(1e14) is around 47 steps, this is manageable.

So the steps are:

Read n and x.

Read array a (sorted in non-decreasing order).

Compute a_n = a[-1].

Compute sum_a = sum(a).

Compute m = sum_a - a_n.

Compute k = n - bisect.bisect_left(a, a_n).

Compute cnt:

cnt = 0

current = k

while current % x ==0:

    cnt +=1

    current = current //x

Compute min_cnt_an = min(cnt, a_n)

exponent = m + min_cnt_an

Compute ans = pow(x, exponent, MOD)

But wait, what if exponent is zero? For example, in the fourth sample where all a_i are 0.

In that case, sum_a = 0. a_n is 0. So m = 0 -0 =0. Wait, no:

sum_a = sum of a_i = 0+0+0+0=4*0=0. a_n is 0.

m = sum_a - a_n = 0 -0=0.

k is the number of elements equal to 0, which is 4.

cnt is computed as the number of times x divides 4.

In the fourth sample, x is 5. 4 is not divisible by 5. So cnt=0. min(0, 0) =0. exponent is 0+0=0. So x^0=1. Which matches the sample.

Yes.

Another example: first sample.

a = [2,2], sum_a=4. a_n=2.

m =4-2=2.

k=2. x=2.

current=2, which is divisible by 2. cnt becomes 1, current=1. loop stops. cnt=1.

a_n=2. min(1,2)=1. exponent=2+1=3. So x^3 =8. Which is correct.

Wait, but in the first sample, the answer is 8, which is 2^3. So yes.

But according to the code, the exponent is 3, which is correct.

But wait, what's sum_a? sum_a is 4. The exponent in t is 4. So the GCD exponent is min(3,4) =3. So code is correct.

Yes.

Another example: third sample input.

Input is 2 2 with a=[29,29]. sum_a=58. a_n=29.

m=58-29=29.

k=2. x=2.

current=2: divisible by 2 → cnt=1, current=1. loop stops. cnt=1.

a_n=29. min(1,29) is 1. exponent=29+1=30.

x=2. 2^30 is 1073741824. mod 1e9+7 is 73741817.

Which matches the sample.

Yes.

So the code seems correct.

Now, let's code this.

We need to:

- Read n and x.

- Read the array a as a list of integers.

- Sort check: the array is already sorted in non-decreasing order. According to the problem statement, the input array is given in non-decreasing order. So we can proceed.

But the problem statement says that the array is given as space-separated integers in the second line, sorted in non-decreasing order. So we can read them as a list and assume that they are sorted.

So code steps:

Read n and x.

Read the array a (sorted in non-decreasing order).

Compute a_n = a[-1]

sum_a = sum(a)

m = sum_a - a_n

Compute k using bisect.

Compute cnt.

Compute min_cnt_an = min(cnt, a_n)

exponent = m + min_cnt_an

Compute the result as pow(x, exponent, MOD), where MOD=1e9+7.

Now, code:

But wait, in Python, the bisect module's bisect_left function returns the first position where a_n can be inserted. Since the array is sorted in non-decreasing order, all elements from that position onwards are >=a_n. But since a_n is the last element, which is the largest, the elements from the bisect_left position are exactly equal to a_n.

But since the array is sorted, and a[-1] is the largest element, all elements from the first occurrence of a_n to the end are equal to a_n.

So, using bisect_left:

k = n - bisect.bisect_left(a, a_n)

Yes.

So the code would look like:

Testing against sample input 3.

```python
import bisect


def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, x = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    a_n = a[-1]

    sum_a = sum(a)

    m = sum_a - a_n

    k = n - bisect.bisect_left(a, a_n)

    current = k

    cnt =0

    while current % x ==0:

        cnt +=1

        current = current //x

    min_val = min(cnt, a_n)

    exponent = m + min_val

    print(pow(x, exponent, MOD), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 5
0 0 0 0
""",
            "output": \
"""\
1
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
import bisect


def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, x = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    a_n = a[-1]

    sum_a = sum(a)

    m = sum_a - a_n

    k = n - bisect.bisect_left(a, a_n)

    current = k

    cnt =0

    while current % x ==0:

        cnt +=1

        current = current //x

    min_val = min(cnt, a_n)

    exponent = m + min_val

    print(pow(x, exponent, MOD), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 2
29 29
""",
            "output": \
"""\
73741817
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

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, x = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    a_n = a[-1]

    sum_a = sum(a)

    m = sum_a - a_n

    k = n - bisect.bisect_left(a, a_n)

    current = k

    cnt =0

    while current % x ==0:

        cnt +=1

        current = current //x

    min_val = min(cnt, a_n)

    exponent = m + min_val

    print(pow(x, exponent, MOD), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
1 2 3
""",
            "output": \
"""\
27
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

Another test case:

n=3, x=2.

a = [3,3,3]. sum_a=9. a_n=3.

m=9-3=6.

k=3.

current=3. 3%2=1 → cnt=0. min_val=0. exponent=6+0=6. GCD is 2^6=64.

But let's see:

sum is 3 terms of 1/(2^3) → sum is 3/(2^3). Common denominator is 2^9 (sum of a_i is 9). So s is sum x^{9-3} * 1 → x^6 * 3. So s=3x^6. t=x^9.

So the GCD is x^6. Which is correct.

Yes.

So the code seems to handle all cases correctly.
</think>

```python
import bisect

MOD = 10**9 + 7

n, x = map(int, input().split())
a = list(map(int, input().split()))
a_n = a[-1]
sum_a = sum(a)
m = sum_a - a_n
k = n - bisect.bisect_left(a, a_n)

current = k
cnt = 0
while current % x == 0 and current > 0:
    cnt += 1
    current = current // x

min_val = min(cnt, a_n)
exponent = m + min_val

print(pow(x, exponent, MOD))
```
