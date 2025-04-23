<think>
Okay, let's try to solve this problem. Hmm. So the problem is to find the number of pairs (p, q) such that LCM(p, q) is X and GCD(p, q) is Y. And we have X and Y given in their prime factorizations. The answer needs to be modulo 998244353.

First, I remember that there's a relationship between LCM and GCD. Oh right, for any two numbers p and q, LCM(p, q) * GCD(p, q) = p * q. So using that, we can derive some conditions here.

But wait, given that LCM(p, q) is X and GCD is Y, then X * Y must equal p * q. But also, Y must divide both p and q. Because the GCD is Y, so both p and q are multiples of Y. Let's think about that.

Let me restructure p and q in terms of Y. Let’s say p = Y * a and q = Y * b. Then, since Y is their GCD, the GCD of a and b must be 1. Because any common divisor of a and b would multiply with Y to give a larger GCD than Y otherwise.

Now, substituting into LCM(p, q) = X. The LCM of Y*a and Y*b is Y * LCM(a, b) because LCM(k*m, k*n) = k * LCM(m,n) when k is a common factor. So the LCM of p and q is Y * LCM(a, b). And this must equal X. So Y * LCM(a, b) = X. Which implies that X must be a multiple of Y. So first, we need to check if Y divides X. If not, the answer is zero.

But how do Y and X relate in terms of their prime factors? Because Y's primes must be a subset of X's primes, right? Because X has LCM(p, q), and Y is the GCD. So all primes in Y must be present in X. Otherwise, if Y has a prime not in X, then since Y divides X, X must have that prime, but it's not present. So that's a contradiction. So the first step is to check that all primes in Y are present in X. Also, for each prime in Y, the exponent in Y must be less than or equal to the exponent in X. Wait, no. Wait, Y is the GCD of p and q. Let's think again.

Wait, Y divides both p and q. So for each prime in Y, the exponent in Y is the minimum of the exponents in p and q. But X is the LCM of p and q, so for each prime in X, the exponent is the maximum of the exponents in p and q. But since Y is part of the problem, perhaps the exponents in Y must be the minimum of the exponents in p and q, and the exponents in X must be the maximum. But how does that relate to the given X and Y?

So here's the approach: Let's merge the primes of X and Y. But Y's primes must be a subset of X's primes. Otherwise, if Y has a prime that X doesn't, then since Y divides X (as X is the LCM of p and q, and Y is their GCD, then Y must divide X). Wait, X must be a multiple of Y. Because Y divides both p and q, so Y divides their LCM, which is X. So X must be divisible by Y. So, all primes in Y must be present in X. Otherwise, if Y has a prime not in X, then X is not a multiple of Y, which is impossible. So first, check if Y's primes are a subset of X's primes. If not, return 0.

Also, for each prime in Y, the exponent in Y (D_j) must be less than or equal to the exponent in X (the corresponding B_i for that prime). Wait, no. Because X is the LCM of p and q, which is the maximum of their exponents. So for a prime that's in Y, let's say Y has exponent d. Then, in X, that same prime has exponent which is the maximum of the exponents in p and q. But since Y is the GCD, the exponents in p and q must be at least d (since Y's exponent is the minimum of p and q). But the maximum of p and q's exponents would then be the exponent in X. So for each prime that's in Y, the exponent in X (X's exponent) must be at least the exponent in Y. Wait, but in X's factorization, the exponents are the maximum between p and q's exponents. So for a prime that is in Y (so present in both p and q), the exponent in X must be >= the exponent in Y. Because, for example, if Y's exponent is d (the min of p and q's exponents), then the max would be at least d. So X's exponent for that prime must be >= Y's exponent. So if any prime in Y has an exponent in Y (D_j) greater than the exponent in X (B_i for that prime), then it's impossible. So we need to check for that. If any such prime exists, the answer is 0.

So first, let's check if all primes in Y are present in X. And that for each such prime, the exponent in Y (D_j) is <= the exponent in X (B_i). If any of these conditions fail, output 0.

Next, for primes that are in X but not in Y. Let's consider a prime that's in X but not in Y. Since Y is the GCD of p and q, that prime cannot be present in both p and q. Because if it were, then the GCD would have that prime. Wait, no. The GCD is the product of primes that are present in both p and q, each raised to the minimum exponent. So if a prime is present in X (so in either p or q), but not in Y, that implies that this prime is present in exactly one of p or q. Because if it were present in both, then the GCD would have it. So for primes in X but not in Y, they must appear in exactly one of p or q, and their exponent must be equal to the exponent in X (since the LCM is X, which is the maximum of p and q's exponents for that prime). So for such primes, each can be assigned to either p or q. But since it's present in exactly one, the exponent in X is the maximum. So for example, if X has a prime a with exponent b, and this prime is not in Y, then in p and q, one of them has exponent b (for a), and the other has exponent 0 (since a is not present in Y, which is the GCD, so both p and q can't have a. Wait, no. Wait, Y is the GCD of p and q, so all primes in Y must be present in both p and q. But primes not in Y can be present in at most one of p or q. Because if a prime is present in both p and q, then the GCD would have that prime. So primes not in Y must appear in exactly one of p or q. 

Wait, that's a key insight. So for primes in X but not in Y, each such prime's exponent in X is the maximum of p and q's exponents. But since the prime is not in Y, the GCD (which is Y) doesn't have it, so that prime can't be present in both p and q. So the prime can be present in exactly one of p or q, with exponent equal to X's exponent (since the LCM is X, which is the maximum). So for such primes, there are two choices: assign the exponent to p, or to q. So each such prime contributes a factor of 2 to the total number of pairs.

Now, for primes that are in Y (so present in both p and q). Let's consider such a prime. Let Y has exponent d, X has exponent b. Then, since Y is the GCD of p and q, the exponents in p and q for this prime must be at least d. But since X is the LCM of p and q, the maximum of their exponents must be exactly b.

So for this prime, let's denote:

p's exponent: x

q's exponent: y

Then, the GCD of p and q for this prime is min(x, y) = d.

The LCM for this prime is max(x, y) = b.

So we have that:

min(x, y) = d

max(x, y) = b

Additionally, since d is the GCD's exponent, which is the min of x and y. And the LCM's exponent is the max of x and y, which is b.

So combining these two equations, what possible values can x and y take?

Let's see. For example, if x <= y, then min(x, y) = x = d, and max(x, y) = y = b. So x = d, y = b.

But then, since min(x, y) is d, we must have x = d and y = b, but only if d <= b.

But wait, according to the problem statement, Y's exponents are D_j, which for this prime is d. And X's exponents for this prime is b. We have already checked that d <= b. Because in the earlier step, we checked that all primes in Y have exponents in Y <= exponents in X.

So, possible cases:

Either x = d and y = b, or x = b and y = d. But wait, no. Wait, min(x, y) must be d. So the smaller of the two exponents must be d, and the larger must be b.

So possible scenarios:

Case 1: x <= y. Then x = d, y = b. But since x <= y, this requires that d <= b. Which it is, because we checked that.

Case 2: y <= x. Then y = d, x = b. Which would require d <= b, which again is true.

Wait, but in either case, one of x or y is d, the other is b. But that's only if d <= b, which is already the case.

Wait, for example, if d is 2 and b is 5. Then possible pairs are (2,5) or (5,2). But wait, no. Because in case (5,2), the min is 2 and the max is 5, which matches. So the exponents can be (d, b) or (b, d), but in either case, as long as d <= b, which it is. Wait, but in this case, when you take min(5, 2) that's 2, which is d. And max(5,2) is 5, which is b. So yes. So for this case, the possible pairs (x,y) are (d, b) or (b, d). But wait, no, in this case, if x is 5 and y is 2, then min is 2, which is d. So that's acceptable. So the possible pairs for x and y are (d, b) and (b, d) as long as d <= b. But wait, in (b, d), min is d (since d <= b). So that's allowed.

So for each prime in Y, there are two possibilities: either x is d and y is b, or x is b and y is d. But wait, no. Because x and y must satisfy min(x,y) = d and max(x,y) = b. So possible pairs are (d, b) or (b, d). But since d <= b, the min is d in both cases. So for each such prime, there are two possibilities. However, there's a catch: if d == b. Then, (d, b) and (b, d) are the same. So in that case, x and y must both be equal to d (since d = b). So in that case, there's only one possibility: x = y = d. Because min(d, d) is d, max(d, d) is d. So when d = b, then the only possible exponents are x = y = d. So in that case, there's only 1 possibility.

So for primes in Y, if the exponent in Y (d) is equal to the exponent in X (b), then there's 1 possibility. Otherwise (d < b), there are 2 possibilities.

Therefore, for each prime in Y:

if d < b → contributes 2 possibilities.

if d == b → contributes 1 possibility.

So the total number of pairs is the product of the possibilities for each prime in Y multiplied by the product of 2^k, where k is the number of primes in X that are not in Y (since each such prime contributes 2 possibilities).

But wait, also, the primes in X that are not in Y must be present in exactly one of p or q. But how does that fit into the exponents?

For example, suppose X has a prime a with exponent 3, and Y does not have a. Then in p and q, one of them must have exponent 3 (for a), and the other must have exponent 0. So for each such prime, there are two choices: assign it to p or to q. Hence, each such prime contributes a factor of 2 to the total.

So the overall approach is:

1. Check if Y is a divisor of X. This means:

   a. All primes in Y are present in X.

   b. For each prime in Y, the exponent in Y (D_j) is ≤ exponent in X (B_i).

   If any of these conditions are not met, the answer is 0.

2. Check that for primes in X that are not in Y, they are not present in Y. Wait, no, Y's primes must be a subset of X's, so X's primes not in Y are allowed. So after step 1, primes not in Y but in X are okay.

3. Then, for each prime in Y:

   - Let the exponent in Y be d, in X be b.

   - If d > b → impossible (already checked in step 1).

   - If d == b → this prime contributes 1 way (x = y = d).

   - If d < b → contributes 2 ways (x = d, y = b or x = b, y = d).

4. For primes in X not in Y:

   - Each contributes 2 ways (assign the exponent to p or to q).

   - But these primes must not be present in Y. So the count of such primes is (number of primes in X) - (number of primes in Y that are in X). Wait, but since Y's primes are a subset of X's, the count is N (number of primes in X) minus M (number of primes in Y). So for primes in X that are not in Y, each contributes 2 options.

So the total number of pairs is (product for primes in Y of (1 if d == b else 2)) multiplied by (2^ (number of primes in X not in Y)).

But wait, wait. Let's see. Suppose X has primes A, B, C, D. Y has primes B and D. Then, the primes in X not in Y are A and C. Each contributes 2 options. So 2^2. Then for Y's primes, each contributes 1 or 2 based on whether d equals b.

So the formula is (product over all primes in Y of (2 if (d < b) else 1)) ) * (2^ (number of primes in X not in Y)).

But then, what about primes in Y that are not present in X? Oh, but step 1 already checks that all primes in Y are present in X. So Y's primes are a subset of X's primes.

So, how to compute this?

Let me outline the steps:

First, for Y to divide X, all primes in Y must be present in X, and for each such prime, D_j <= B_i (where B_i is the exponent in X for that prime).

So, the first thing is to check for each prime in Y's list whether it exists in X's list, and if so, compare D_j to B_i. If any prime in Y is not in X, or D_j > B_i, then the answer is 0.

Once that is done, for each prime in X:

If it is present in Y:

   Check if D_j (from Y) equals B_i (from X). If not, multiply the result by 2.

If it is not present in Y:

   Multiply the result by 2.

Wait, no. Wait, for primes present in Y:

   The contribution is 1 if D_j == B_i, else 2.

For primes not present in Y (but present in X):

   The contribution is 2.

So the total is product( (1 if D_j == B_i else 2) for primes in Y) * (2^k), where k is the number of primes in X not in Y.

So how to compute this?

We need to:

- Merge the primes of X and Y.

But since Y's primes are a subset of X's, we can process X's primes, and check for each whether it's in Y.

But how to efficiently check this? Since the primes in X and Y are sorted, perhaps we can merge the two lists.

So here's the plan:

1. Read X's primes and their exponents. Let's store X's primes in a list, and also create a dictionary (like a hash map) that maps each prime to its exponent. Since the primes are given in order and sorted, but for O(1) lookups, a hash map is better.

2. Read Y's primes and their exponents. For each prime in Y, check if it exists in X's primes (using the hash map). If any prime in Y is not present in X, return 0.

3. For each prime in Y, check if Y's exponent (D_j) is <= X's exponent (B_i). If any D_j > B_i, return 0.

4. Then, for all primes in X, for each:

   a. If the prime is in Y:

      i. If X's exponent B_i == Y's exponent D_j: multiply the result by 1.

      ii. Else: multiply the result by 2.

   b. Else (prime is in X but not Y): multiply the result by 2.

Wait, but in X's primes, the primes are all in the list. So for each prime in X, we check if it's present in Y. If it is, then we check whether B_i (from X) is greater than D_j (from Y). Since in step 3, we already checked that D_j <= B_i, so B_i >= D_j.

But for primes in X that are in Y, the contribution is 1 if B_i == D_j, else 2. For primes not in Y, the contribution is 2.

So the total is the product of (for each prime in X) 1 if (prime is in Y and B_i == D_j) else 2.

But how to compute this?

We can:

- Iterate through all primes in X.

   For each prime in X:

   if it's in Y:

      get D_j from Y's exponents.

      if B_i (X's exponent) == D_j: multiply by 1.

      else: multiply by 2.

   else:

      multiply by 2.

So the steps:

Compute the product of 2^(number of primes in X not in Y) multiplied by the product over primes in Y of (2 if B_i != D_j else 1).

Wait, no. Because primes in X not in Y contribute 2 each. So that's 2^k, where k is the count. For primes in X that are in Y, each contributes 1 or 2 depending on whether B_i == D_j.

So the total is (product for primes in Y: 2 if B_i > D_j else 1) * (2^(number of primes in X not in Y)).

So to compute this:

Initialize the answer as 1.

Compute the product over all primes in Y:

   for each such prime, if B_i (from X) > D_j → multiply by 2.

Then, compute the count of primes in X that are not in Y. Let this be k. Multiply the answer by 2^k.

So how to compute k?

k is N (number of primes in X) minus the number of primes in Y that are present in X (which is M, since Y's primes are all present in X, as checked earlier? Wait, no. Because Y's primes are all present in X. So the primes in Y are exactly M primes, all present in X. So the primes in X that are not in Y is N - M.

Wait, no. Because X can have more primes than Y. So if Y has M primes, all present in X, then the number of primes in X not in Y is (N - M). So yes.

So after all the checks, the number of primes in X not in Y is N - M.

Wait, no. For example, X may have primes [2,3,5], Y has primes [2,5], then M=2, N=3. So N-M=1, which is correct. So yes.

But wait, X's primes are sorted, Y's primes are sorted. So the primes in Y are a subset of X's primes, but how to confirm that they are all present? Because during step 1, we check that all primes in Y are present in X.

So once the initial checks are done, Y's primes are a subset of X's. So the count of primes in X not in Y is N - M.

Wait, no. Because X's primes may have duplicates with Y's? No. Because X's primes are sorted and distinct. Y's primes are sorted and distinct. So the primes in Y are all present in X, but X can have other primes. So the count is N - M.

Wait, no. For example, X has primes [2,3,5,7], Y has primes [3,5]. Then M=2, N=4. The primes in Y are in X. The primes in X not in Y are 2 and 7: count is 2. Which is N-M=4-2=2. So yes.

So the number of primes in X not in Y is N - M.

So the answer is:

product over Y's primes (if X's exponent > Y's exponent, multiply by 2) * (2^(N-M)).

But how to handle the product for Y's primes. Let's see.

But wait, for each prime in Y, X's exponent is B_i (the exponent in X for that prime). Y's exponent is D_j (exponent in Y for that prime). Since during the initial checks, we have already ensured that D_j <= B_i for all primes in Y.

So for each Y's prime:

if B_i == D_j → contributes 1 to the product.

if B_i > D_j → contributes 2 to the product.

So the product is 2^t, where t is the number of Y's primes where B_i > D_j.

So the total answer is (2^t) * (2^(N-M)) ) mod MOD.

Which is equal to 2^(t + (N-M)) mod MOD.

But wait, let's see. For each prime in Y that has B_i > D_j, we multiply by 2. So t is the number of such primes.

So the product for Y's primes is 2^t. Then, the primes in X not in Y contribute 2^(N-M). So total is 2^t * 2^(N-M) = 2^(t + N-M).

Thus, the answer is 2^(k), where k = t + (N-M).

But how to compute t?

t is the number of primes in Y where B_i (X's exponent) > D_j (Y's exponent).

So steps:

1. Check if all primes in Y are present in X. If not, return 0.

2. For each prime in Y, check if D_j > X's exponent (B_i). If any, return 0.

3. Then, compute t = number of primes in Y where B_i > D_j.

4. Compute k = t + (N - M).

5. The answer is 2^k mod MOD, but if any of the initial conditions are not met, return 0.

Wait, but why?

Because:

Each prime in Y where B_i > D_j contributes a factor of 2. So t is the count of such primes. Then, the primes in X not in Y contribute (N-M) factors of 2. So total is 2^(t + (N-M)).

So the answer is 2^(t + (N-M)) mod 998244353.

But wait, this is only possible if all the initial conditions are met. Otherwise, the answer is 0.

So how to compute t?

We need to iterate through each prime in Y, and check if X's exponent for that prime is greater than Y's exponent.

But how to get X's exponent for a prime in Y? Since X's primes are stored in a list, but we need to find the exponent for each Y's prime.

But since X's primes are stored in a sorted list, but we can use a dictionary (hash map) to map primes to their exponents.

So for example, when processing X, we can create a dictionary where the key is the prime and the value is its exponent.

Then, when processing Y's primes, for each prime C_j in Y, look it up in the dictionary. If not present, return 0. Else, compare D_j (Y's exponent) to the exponent from X (B_i). If D_j > B_i, return 0.

Also, for each such prime, if B_i > D_j, increment t by 1.

Thus, the steps in code would be:

Read N.

Read X's primes A = list.

Read X's exponents B = list.

Read M.

Read Y's primes C = list.

Read Y's exponents D = list.

Create a dictionary for X's primes: x_prime_to_exp = {A[i]: B[i] for i in range(N)}.

Check if all C_j are in x_prime_to_exp. If any C_j not in x_prime_to_exp, output 0.

For each j in 0..M-1:

   c_j = C[j]

   d_j = D[j]

   b_i = x_prime_to_exp[c_j]

   if d_j > b_i:

       output 0.

   if d_j < b_i:

       t += 1

k = t + (N - M)

The answer is pow(2, k, 998244353) if all conditions are met, else 0.

But wait, what about the case where Y has primes not present in X? The code checks for that. For example, in step where for each C_j in Y, we check if it is in X's primes. So that's handled.

So for the third example in the problem statement:

Input:

2

2 5

1 1

2

2 3

1 1

Y's primes are 2 and 3. But 3 is not in X's primes. So the code will output 0.

Another example: if Y has a prime present in X, but with exponent D_j > B_i. For example, X has prime 2 with exponent 3, Y has prime 2 with exponent 4. Then step 2 will detect this and output 0.

Another example: the second sample input.

X's primes are 1299721 and 1999993. Y's primes are same. Their exponents are same. So t = 0, N-M=0. So answer is 1.

So the code should handle all cases correctly.

Thus, the code can be written as follows:

Read N.

Read A list.

Read B list.

Create x_prime_to_exp.

Read M.

Read C list.

Read D list.

Check if M > N: since Y's primes must be subset of X's, but if M > N, then there's no way. Wait, for example, X has N=2 primes, Y has M=3 primes. Then Y's primes can't all be in X's primes. So code can first check if M > N → output 0.

But in code, the code would check each C_j in Y's primes whether they are present in X's. So even if M > N, but all C_j are present in X's primes (but X's primes may have duplicates?), but since X's primes are given in sorted order and are distinct, and same for Y's primes. So if M > N, then Y's primes can't all be in X's primes, so the code would detect that.

So, proceed as follows.

So, code outline:

MOD = 998244353

n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

x_dict = {}

for ai, bi in zip(a, b):

    x_dict[ai] = bi

m = int(input())

c = list(map(int, input().split()))

d = list(map(int, input().split()))

t = 0

valid = True

# Check if all C primes are in X's primes.

for cj in c:

    if cj not in x_dict:

        valid = False

        break

if not valid:

    print(0)

    exit()

# Now check each Y's prime's exponent.

for j in range(m):

    cj = c[j]

    dj = d[j]

    bi = x_dict[cj]

    if dj > bi:

        valid = False

        break

    if dj < bi:

        t +=1

if not valid:

    print(0)

    exit()

# Compute k = t + (n - m)

k = t + (n - m)

ans = pow(2, k, MOD)

print(ans)

Yes, this should handle all cases. Let's test this code against the examples.

First example:

Input:

4

2 3 5 7

2 1 1 2

2

3 7

1 1

So X's primes are 2,3,5,7. Y's primes are 3 and7.

Check all C_j in X: yes.

For Y's primes:

3: D_j=1 vs X's exponent 1. So equals. t +=0.

7: D_j=1 vs X's exponent 2. So 1 <2 → t +=1. So t is 1.

n - m =4-2=2.

k=1+2=3 → 2^3=8. Which matches the first example.

Second example:

X's primes are 1299721 and 1999993. Y's same. Exponents are same. So t=0. n-m=0. 2^0=1.

Third example: Y's primes are 2 and 3. X's primes are 2 and5. So C includes 3 which is not in X's primes. So code outputs 0.

Yes. So the code works for the examples.

Now, handling large inputs:

The code reads N up to 1e5, and M up to 1e5. For the dictionary, it's O(N) to build. Then checking M entries. So overall time is O(N + M), which should be acceptable.

Space-wise, the dictionary for X is O(N), which is acceptable for 1e5 primes.

So this code should work correctly and efficiently.
</think>

```python
MOD = 998244353

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x_dict = {}
for ai, bi in zip(a, b):
    x_dict[ai] = bi

m = int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))

valid = True
# Check if all Y primes are in X
for prime in c:
    if prime not in x_dict:
        valid = False
        break
if not valid:
    print(0)
    exit()

t = 0
# Check exponents in Y and count t
for i in range(m):
    y_prime = c[i]
    y_exp = d[i]
    x_exp = x_dict[y_prime]
    if y_exp > x_exp:
        valid = False
        break
    if y_exp < x_exp:
        t += 1

if not valid:
    print(0)
    exit()

k = t + (n - m)
ans = pow(2, k, MOD)
print(ans)
```