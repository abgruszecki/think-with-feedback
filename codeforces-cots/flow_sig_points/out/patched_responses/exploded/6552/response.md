<think>
Okay, so I need to solve this problem where I have to determine if Arya can always figure out x mod k for any x, given that she knows the values of x mod c_i for some set of c_i's. Hmm, let me think about what the condition here is.

The problem says that Arya has a winning strategy if, no matter what x Pari chooses, knowing all the x mod c_i values allows her to uniquely determine x mod k. So, for any two x and y, if x ≡ y mod all c_i's, then they must also be congruent mod k. Otherwise, there's a case where she can't tell the difference, which means the answer is No.

Wait, right. So the key condition here is that the intersection (or maybe the least common multiple) of the moduli c_i must be such that their LCM divides k in some way. Wait, maybe not. Let's think in terms of equivalence relations.

If two numbers x and y are congruent modulo all c_i, then they must also be congruent modulo k. Because if that's the case, then knowing all the mod c_i gives enough information to determine mod k. Otherwise, there exists some pair x and y where they are the same mod all c_i but different mod k, making it impossible to determine x mod k.

So how to model this? The condition is that the intersection of the congruences (x ≡ y mod c_i for all i) implies x ≡ y mod k. Which, in algebraic terms, the equivalence relation defined by the c_i's must refine the equivalence relation modulo k. 

The intersection of congruences mod c_i is equivalent to congruence modulo the least common multiple (LCM) of all the c_i's. Because if x ≡ y mod LCM(c_i), then x ≡ y mod each c_i. And conversely, if x ≡ y mod each c_i, then x ≡ y mod LCM(c_i). So the LCM is the modulus of the combined congruence.

Therefore, the condition we need is that LCM(c_i) must be a multiple of k. Because if LCM(c_i) is a multiple of k, then x ≡ y mod LCM(c_i) implies x ≡ y mod k. Therefore, knowing x mod LCM(c_i) (which is equivalent to knowing all x mod c_i) allows us to determine x mod k. Wait, no. Wait, if LCM(c_i) is a multiple of k, then LCM(c_i) = m * k. Then any two numbers congruent mod LCM(c_i) will also be congruent mod k. So yes, that's the condition.

Wait, but the problem is to determine whether the LCM of the c_i's is a multiple of k. Because then, any x's mod LCM(c_i) would determine x mod k. So, if LCM(c_i) is divisible by k, then answer is Yes. Otherwise, No.

But wait, that's not exactly the case. Let me think again. Suppose the LCM of the c_i's is L. Then, if L and k are such that L and k have a GCD of g. Then, x ≡ y mod L implies x ≡ y mod g. Hmm, no, maybe not. Because L is the LCM of the c_i's. So, if L is a multiple of k, then yes. But if not, then even if L is not a multiple of k, perhaps there's a way that knowing all the c_i's moduli gives enough info. For example, if one of the c_i is k, then L is at least k (assuming c_i =k is present). Then, knowing x mod k directly gives the answer, so LCM is >=k, and includes k. So in that case, L is a multiple of k. So the condition would be that LCM(c_i) must be divisible by k. So if LCM(c_i) is divisible by k, then answer is Yes. Otherwise, No.

Wait, let's test this with the examples.

First example:

k=5, c = [2,3,5,12]. The LCM of the c's is LCM(2,3,5,12). Let's compute that. Factors are 2^2, 3, 5. So LCM is 60. 60 is divisible by 5. So the answer is Yes. Which matches the sample.

Second example: k=7, c = [2,3]. LCM(2,3) is 6. 6 is not divisible by 7. So the answer is No, which matches the sample.

Another test case: suppose k=4 and c has 2 and 4. LCM is 4, which is divisible by 4. So answer is Yes. Because knowing x mod 2 and mod 4 allows you to know x mod 4. Wait, but even if x mod 4 is known directly, then of course. Wait, in this case, if one of the c's is 4, then the LCM is 4, which is divisible by 4. So answer is yes. So the condition seems correct.

But what if k is 6 and the c's are 4 and 3. LCM is 12. 12 is divisible by 6, so answer is yes. Because any two x and y congruent mod 12 will have x mod 6 = y mod 6. So knowing x mod 4 and 3 (which gives x mod 12) allows us to compute x mod 6.

So the conclusion is that the answer is Yes if and only if the LCM of all the c_i's is a multiple of k.

But wait, is there a case where the LCM of the c_i's is not a multiple of k, but the condition holds? Let's see. Suppose k=6, and c's are 4 and 6. Then the LCM is 12. Which is a multiple of 6, so condition holds. Answer yes.

Alternatively, k=6 and c_i's are 3 and 4. LCM is 12, which is a multiple of 6. So answer is yes.

But if k=5 and c_i's are 3 and 4. LCM is 12. 12 is not a multiple of 5. So answer is no. Because for x=5 and x=0, their mod 3 and 4 are 0 and 0, but mod 5 is 0 and 5 mod5 is 0? Wait, wait, no. Let me pick x=5 and x=10. x mod3 is 2 in both cases (5 mod3 is 2, 10 mod3 is 1. Wait, no. Wait, 5 mod3 is 2, 10 mod3 is 1. So that's different. Hmm. Maybe I need to find x and y that are congruent mod all c_i's but differ mod k.

If LCM(c_i) is not a multiple of k, then there exist x and y such that x ≡ y mod LCM(c_i), but x ≡ y + m*L mod k, where m is chosen such that (y + m*L) mod k is different. Wait, but if L and k are coprime, then adding L would cycle through residues mod k. So for example, take x=0 and y=L. Then x and y are congruent mod L. So their mod c_i's are same. But mod k, 0 mod k is 0, and L mod k could be (L mod k). If L mod k is not zero, then 0 and L would be different mod k. So in this case, the answer would be No.

So the condition is that LCM(c_i) must be a multiple of k. Therefore, the solution is to compute the LCM of all the c_i's and check if it's divisible by k.

But there's a catch: the LCM of the c_i's could be very large. For n up to 1e6, and each c_i up to 1e6, the LCM could be as big as (product of primes up to 1e6), which is way beyond what can be stored in a variable. So computing the LCM directly isn't feasible for large n and c_i's.

So how do we compute if the LCM of the c_i's is a multiple of k, without actually computing the LCM?

An alternative approach: factorize k into its prime factors. Then, for each prime in the factorization of k, check whether the maximum exponent in the c_i's is at least as large as in k. Because, the LCM of all c_i's must have, for each prime in k's factorization, at least the same exponent as in k.

Wait, that's correct. For example, if k is 12 = 2^2 * 3^1. Then the LCM of the c_i's must have at least 2^2 and 3^1. So if any c_i has 2^2, and another has 3^1, then their LCM will have those exponents.

So the approach would be:

1. Factorize k into its prime factors. For example, k = product (p^e_p).

2. For each prime p in k's factors, find the maximum exponent of p in all the c_i's. If for any p, the maximum exponent in the c_i's is less than e_p, then the answer is No. Otherwise, Yes.

Because if for all primes in k's factorization, the c_i's have at least the required exponents, then the LCM of the c_i's will have exponents >= those of k, making the LCM a multiple of k.

But if any prime in k's factorization is missing from all c_i's (so the max exponent is zero but required to be at least e_p >=1), then answer is No.

So the steps are:

- Check if the LCM of the c_i's is a multiple of k. But since k can be up to 1e6, and n up to 1e6, and c_i up to 1e6, factorizing k and checking each prime's maximum exponent in c_i's is feasible.

So the plan is:

1. If k is 1, then x mod 1 is always 0. So answer is Yes.

2. Otherwise, factorize k into primes. For each prime p in the factorization, note the exponent e.

3. For each such prime p, check if there exists a c_i that is divisible by p^e. Because the maximum exponent of p in the c_i's must be at least e. If even one p where this is not true, the answer is No.

But wait, not exactly. Because the maximum exponent of p among all c_i's may be >= e. For example, if k=12=2^2*3^1. Then, any c_i that has 2^2 in its factors (e.g., 4, 8, etc.), and any c_i that has 3^1 (e.g., 3, 6, etc.), then the LCM will have 2^2 *3^1, which is 12, so LCM is a multiple of k.

But if one of the c_i's is 4 (2^2) and another is 6 (2^1 *3^1), then the maximum exponents are 2^2 and 3^1. So LCM is 12, which includes 2^2 and 3^1, sufficient for k=12.

So the key is for each prime p in k's factors, the maximum exponent in the c_i's for p must be >= the exponent in k.

Thus, the algorithm would be:

Factorize k into primes. For each prime p with exponent e in k, check that at least one c_i has p^e as a divisor. If all primes in k's factorization meet this condition, then answer is Yes. Otherwise, No.

But how to compute this efficiently?

First, factorize k. Then, for each prime p in the factors of k, compute e, which is the exponent of p in k.

Then, for each c_i, compute for each p in the factors of k, the maximum exponent of p in c_i. Then, for each p, track the maximum exponent across all c_i's. If any p's maximum exponent is < e, then answer is No.

But considering that n can be up to 1e6, and the number of primes in k's factorization is small (since k is up to 1e6), this is feasible.

So the steps:

1. Check if k is 1. If yes, output Yes.

2. Else, factorize k into primes. For example, k = p1^e1 * p2^e2 * ... pm^em.

3. For each prime pi in the factorization of k:

   a. Compute required exponent ei.

   b. For all c_i, compute the exponent of pi in their prime factors.

   c. Find the maximum exponent of pi among all c_i's.

   d. If the maximum is less than ei, output No.

4. If all primes in k's factorization have their max exponents >= required, output Yes.

This approach avoids computing the LCM of all c_i's, which could be impossible due to size. Instead, for each prime in k, we check whether there's a c_i that contributes enough exponents.

But how to compute for each c_i, the exponents of the primes in k's factorization?

For example, if k's prime factors are 2 and 3, then for each c_i, we can check how many times 2 divides into c_i, and how many times 3 divides into c_i. The maximum exponents for 2 and 3 across all c_i's must be at least the exponents in k.

So, here's the plan:

- For each prime p in the factorization of k:

   - Find the exponent e required.

   - Iterate through all the c_i's and compute how many times p divides into c_i (call this count).

   - Track the maximum count across all c_i's.

   - If this max is < e, return No.

So the code steps:

First, factorize k.

But factorizing k up to 1e6 is manageable. For example, trial division.

Once k is factorized, for each prime in its factors, we need to check if any c_i has at least the required exponent.

But for each c_i, we can check if p^e divides into c_i. Because if c_i is divisible by p^e, then the exponent of p in c_i is at least e.

Wait, but if we have a c_i that has p^e as a divisor, then the maximum exponent for p is at least e. So for each prime p in k's factors, if there exists at least one c_i that is divisible by p^e, where e is the exponent of p in k, then the maximum exponent for p is at least e.

So instead of checking all c_i's exponents for p, we can just check if any c_i is divisible by p^e. Because if even one c_i is divisible by p^e, then the maximum exponent of p is at least e, which is sufficient.

Wait, that's correct. Because the maximum exponent for p in the LCM is the maximum exponent of p in any c_i. So if any c_i has exponent >= e, then the maximum is >=e, which meets the requirement.

So the code can be optimized: for each prime p in k's factors with exponent e, check if any of the c_i's is divisible by p^e. If even one is found for all primes, answer is Yes. Otherwise, No.

This approach would be more efficient, as for each prime p and exponent e in k's factors, we can precompute p^e, then check if any c_i is divisible by this p^e.

But p can be up to 1e6, and e can be up to log2(1e6) ≈ 20. So p^e could be up to (1e6)^20, which is way beyond 64-bit integers. So calculating p^e for large exponents is not feasible.

Wait, but if e is such that p^e is larger than 1e6 (the maximum c_i), then since c_i is at most 1e6, none of the c_i's can be divisible by p^e. So in that case, we can immediately return No.

So for each prime p in k's factors:

- Compute e (the exponent in k's factorization).

- Compute p^e. If p^e exceeds 1e6, then since all c_i's are <=1e6, none can be divisible by p^e, so answer is No.

Else, check if any c_i is divisible by p^e.

So the steps:

For each prime p in the factorization of k:

   e = exponent of p in k.

   compute p^e. If p^e > 1e6:

       return No.

   else, check if any c_i is divisible by p^e. If none are, return No.

If all primes pass this check, return Yes.

But how to compute p^e without overflow? Well, since p is a prime factor of k, which is up to 1e6. The maximum possible e for p=2 is 19 (since 2^20 is 1,048,576 which is over 1e6). So for p=2, e can be up to 19. So for p^e, we can compute it as an integer, but we have to check if it exceeds 1e6. Let's see:

For example, for k=1e6, which is 2^6 *5^6. So p=2, e=6: 2^6=64. p^e=64 <=1e6. So for primes in k's factors, p^e can be up to (1e6) in the case where k is a prime (like 1e6 is not prime, but 1e6 is 10^6 = (2*5)^6, etc. Wait, no. 1e6 is 1,000,000 = 2^6 *5^6. So for each prime in its factors (2 and5), e is 6. So 2^6 is 64, 5^6 is 15625. Both are <=1e6. So for primes in k's factors, p^e could be up to 1e6 (like if k is a prime and e=1, then p^e is up to 1e6). So when e=1, p can be up to 1e6. So p^e could be up to 1e6.

But if k has a prime p with e such that p^e >1e6, then none of the c_i's can be divisible by p^e (since c_i's are up to 1e6). So for such primes, the answer is automatically No.

Therefore, the algorithm can proceed as:

For each (p, e) in the prime factors of k:

   if p^e >1e6 → answer is No.

   else:

      check if any c_i is divisible by p^e. If none → answer is No.

If all (p,e) pass, answer Yes.

So how do we compute p^e for each (p, e) and check if it exceeds 1e6?

But since p is a factor of k, and k is up to 1e6, p can be up to 1e6. e is up to log2(1e6) ≈20. So p^e can be as big as (1e6)^20, but that's way beyond 1e6. So when e is such that even p^e >1e6, then no c_i can be divisible by it, since c_i's are up to 1e6.

Wait, but how do we compute whether p^e exceeds 1e6 without actual computation? Well, we can compute p^e step by step, and check if it exceeds 1e6 during the computation. For example, multiply p by itself e-1 times, and each time check if the product exceeds 1e6. If at any step it does, we can break and return that p^e is larger than 1e6.

But wait, this could take O(e) time per prime. Since e can be up to log2(1e6) which is 20, this is manageable.

Alternatively, using logarithms, but that could introduce floating point inaccuracies. So better to compute step by step.

So, code steps for each (p, e):

Compute p^e:

Initialize val =1.

For i in 1 to e:

   val *=p

   if val >1e6:

       break and return that it's larger than 1e6.

After all iterations, if val <=1e6, then check if any c_i is divisible by val.

So this is feasible.

So the code outline:

Read n and k.

Read list of c_i.

If k is 1:

   print Yes.

Else:

   factorize k into primes with exponents.

   for each (p, e) in factors:

       compute p^e:

           val =1

           for _ in range(e):

               val *=p

               if val >1e6:

                   break

           if val >1e6:

               print No and exit.

           else:

               check if any c_i is divisible by val.

               if none found:

                   print No and exit.

   if all primes passed, print Yes.

But how to factorize k?

Implement trial division for k up to sqrt(k). For each possible divisor.

But since k can be up to 1e6, trial division is manageable.

Alternatively, use a sieve to precompute primes up to 1e6, but for factorization, trial division is acceptable here.

So code for factorization:

def factorize(k):

    factors = {}

    i=2

    while i*i <=k:

        while k%i ==0:

            factors[i] = factors.get(i,0)+1

            k =k//i

        i +=1

    if k>1:

        factors[k] =1

    return factors

So for example, factorize(12) gives {2:2,3:1}

Then, for each (p,e) in factors.items():

compute p^e.

So in code:

for p, e in factors.items():

    val = 1

    for _ in range(e):

        val *= p

        if val > 1e6:

            break

    if val >1e6:

        print("No")

        exit()

    found = False

    for c in c_list:

        if c % val ==0:

            found = True

            break

    if not found:

        print("No")

        exit()

print("Yes")

But wait, this code could have a problem when multiple exponents. For example, p=2, e=3: val=8. We check if any c_i is divisible by 8. If yes, then the maximum exponent of 2 in the c_i's is at least 3. But suppose the max exponent is 4. Then 8 divides that c_i, but 16 (2^4) also divides it. So the code would correctly detect that 8 divides it. So even though the max exponent is higher than required, the code correctly returns yes.

But in the code, if p^e is 8 and a c_i is 8, 16, etc., then 8 divides them. So the code works.

So this approach is correct.

Now, let's test some cases.

Test case 1:

n=4, k=5.

c = [2,3,5,12]

k=5's factors are {5:1}

Compute 5^1 =5. 5 is <=1e6.

Check if any c_i is divisible by 5. Yes, the third c_i is 5. So answer is yes.

Test case 2:

n=2, k=7.

c = [2,3]

factors of 7: {7:1}

compute 7^1=7. Check if any c_i is divisible by 7. 2 and 3 are not. So answer is no.

Another test case:

k=12, c=[4,3]

factors of 12 are 2^2, 3^1.

Check for 2^2=4:

Check if any c_i is divisible by 4. The first c_i is 4 → yes.

Check for 3^1=3: the second c_i is 3 → yes. So answer is yes.

Another test case: k=8, c=[4, 6].

Factors of 8: 2^3.

Compute 2^3=8. Check if any c_i is divisible by 8. 4 and 6 are not. So answer is no.

So code would output No.

Another test case: k=6, factors 2^1,3^1.

c = [6, 4].

For 2^1=2: check if any c_i is divisible by 2. Both 6 and 4 are → yes.

For 3^1=3: check if any c_i is divisible by 3. 6 is yes. So answer is yes.

Another test case: k=9 (3^2), and c has 3 and 6.

For 3^2=9. Check if any c_i is divisible by 9. 3 and 6 are not. So answer is no.

But wait, 3's exponent in 3 is 1, which is less than 2. So the code would find that there's no c_i divisible by 9, so output no.

So code works.

Now, the code needs to process up to 1e6 c_i's. For each (p,e) pair, iterate through all c_i's and check if any is divisible by p^e. But for n=1e6 and multiple primes, this would be O(n * number of primes in k's factors). For example, if k has 2 primes (like 2 and 3), then each check is O(n) for each prime. So for 1e6 n and 2 primes, 2e6 operations. Which is manageable.

But for n=1e6 and say 5 primes, 5e6 operations. Still manageable.

But wait, the code as written would loop through all c_i's for each (p,e) pair. So for each (p,e), in the worst case, it's O(n) steps. For example, if k is 1, which is handled early. Otherwise, for a k with m primes, each check is O(n) steps.

But 1e6 * 1e6 would be 1e12 steps, which is way too slow. Wait, no. Wait, n is 1e6 and m (number of primes in k's factors) is up to O(log k). For example, k up to 1e6, the maximum number of distinct primes is limited. For example, 2 * 3 *5 *7 *11 *13 etc. Let's see: 2*3*5*7*11*13*17=510510, which is under 1e6. Adding next prime (19) would make it 510510 *19 =9,699,690, which is over 1e6. So maximum distinct primes is 7. So m is up to 7.

So for each (p,e), the code would loop through all n c_i's. So for m=7 and n=1e6, that's 7e6 operations. Which is acceptable.

But if k is a prime number, then m=1, and it's O(n) steps.

But 1e6 steps per test case is acceptable.

But in the code, the code loops through the entire list of c_i's for each (p,e) pair. This could be optimized by pre-processing all primes in k's factors and checking for each c_i if it's divisible by any of the required p^e's. But perhaps it's not necessary. Let's see.

Alternative approach: for each c_i, check for all (p,e) in factors whether p^e divides c_i. But how?

But the code as written is O(m*n), which for m=7 and n=1e6 is manageable.

But in Python, 1e6 iterations per (p,e) could take time, but the code needs to be efficient.

Wait, but in Python, a loop of 1e6 elements is manageable. For example, a list of 1e6 elements, iterating through them and checking modulo is O(n) per (p,e) pair.

But for each (p,e), how to check if any c_i is divisible by val=p^e.

An alternative is to use a set for the c_i's. Then, for each val=p^e, check if any multiple of val exists in the set. But this would be O(1) per check. But that's not correct, since for example, the set may not have a multiple, but a number that is divisible by val. For example, val=4. c_i=8. 8 is divisible by 4, so it's in the set. But if the set contains 8, then yes.

Wait, but if the set is built as the set of all c_i's, then to check if any element is divisible by val, we can iterate through multiples of val and see if any of them are in the set.

But for val up to 1e6, the maximum multiple is 1e6. So the multiples are val, 2*val, ... up to <=1e6.

But this could take up to 1e6 / val steps, which for val=1 is 1e6 steps, which is worse than O(n).

So this approach may not be better.

Alternatively, using a frequency array. Create an array of size 1e6+1, where freq[v] is True if v is present in the c_i's, else False.

Then, for val=p^e, check if any multiple of val (val, 2*val, ...) exists in the array.

But building the frequency array takes O(n) time. Then, for each val, checking for multiples is O(1e6/val) steps.

If val is small (like 2), then 1e6/2 = 5e5 steps. Which is more than O(n) steps. So for val=2, this approach is worse.

So the original approach of iterating through all c_i's for each (p,e) is better.

But how to make this efficient in Python?

In Python, list comprehensions and built-in functions are faster. So, perhaps for each (p,e), we can compute val and then check if any element in the list is divisible by val.

But how?

In code:

found = any(c % val == 0 for c in c_list)

This is a generator expression that will short-circuit (stop as soon as a True is found).

In Python, this is efficient, because the loop stops as soon as a True is found.

So, for each (p,e), the code checks each c in c_list until one is found that is divisible by val.

In the best case, the first element of the list is divisible by val, so O(1) per (p,e). In the worst case, no elements are divisible, so O(n) per (p,e).

But in the worst case, which is when the answer is No, the code will process all elements for at least one (p,e) pair.

But given that n is 1e6, and for each (p,e) pair, each check is O(1) modulo operation, it's manageable.

So the code can be written as follows.

But let's think about possible optimizations.

If the list of c_i's is preprocessed into a set, then for each val, we can check if any of the c_i's is a multiple of val. But that requires checking all multiples of val up to 1e6, which may be slow for small val.

But for example, if val=2, then numbers in the set that are even. So, if the set has any even numbers, then val=2 divides them. So in that case, it's sufficient to check if the set contains any even numbers, which can be determined by checking the presence of any even number. But that's not straightforward.

Alternatively, for each val, we can check if there's any c_i in the set that is >= val and divisible by val. But again, the set doesn't help here; we have to iterate through all c_i's.

So the initial approach is the best possible.

Now, let's code this.

The steps:

Read n and k.

If k is 1, output Yes.

Else, factorize k.

For each prime p in factors:

   compute e.

   compute p^e, checking for overflow beyond 1e6.

   if overflow, output No.

   else, check if any c_i is divisible by val.

   if not found, output No.

If all primes are covered, output Yes.

Now, code:

But note that the code must process very large inputs. For n=1e6 and each c_i up to 1e6.

In Python, reading a million numbers with input().split() can be slow. So, it's better to read from stdin as a buffer.

But the problem statement says that the code must read from input() and write to print(). So, perhaps for large inputs, the code must be efficient.

But in practice, using sys.stdin.read() is faster.

But according to the problem statement, the code should read from standard input via input(), but the problem says "read input from standard input (input()), write output to standard output (print())".

So, for handling large input, it's better to read via sys.stdin.

But the code will need to read two lines.

In Python, for large inputs, the following code can be used:

import sys

n, k = map(int, sys.stdin.readline().split())

c = list(map(int, sys.stdin.readline().split()))

But this is the standard way.

So, let's proceed.

Now, the code:

First, handle k=1:

if k ==1:

    print("Yes")

    exit()

Else:

Factorize k.

Then, for each (p,e) in factors:

Compute p^e.

But for exponents e where p^e exceeds 1e6 → output No.

Else, check if any c_i is divisible by p^e.

If not → output No.

So, code:

import sys

def factorize(k):

    factors = {}

    while k % 2 ==0:

        factors[2] = factors.get(2,0) +1

        k =k //2

    i=3

    while i*i <=k:

        while k %i ==0:

            factors[i] = factors.get(i,0)+1

            k =k//i

        i +=2

    if k>1:

        factors[k] =1

    return factors

n, k = map(int, sys.stdin.readline().split())

c = list(map(int, sys.stdin.readline().split()))

if k ==1:

    print("Yes")

    exit()

factors = factorize(k)

for p, e in factors.items():

    # Compute p^e, check if it exceeds 1e6

    val = 1

    over = False

    for _ in range(e):

        val *=p

        if val > 10**6:

            over = True

            break

    if over:

        print("No")

        exit()

    # Check if any c_i is divisible by val

    found = False

    for num in c:

        if num % val ==0:

            found = True

            break

    if not found:

        print("No")

        exit()

print("Yes")

This code should handle all cases.

But let's test with the first sample:

Sample 1:

4 5

2 3 5 12

factors of 5: {5:1}

val=5.

Check c_i's: 5 is in the list. So found is true. Proceed. Output yes.

Sample 2:

2 7

2 3

factors of7: {7:1}

val=7. Check if any c_i is divisible by 7. 2 and3 no. So output No.

Another test case where k=12 (factors 2^2,3^1). c_i=[4,3]. val for 2 is 4. 4 is in c_i. val for 3 is3, which is in c_i. So output yes.

Another test case where k=8 (2^3). c_i=[4,6]. val=8. 4 and6 are not divisible by8. So output No.

Thus, code works.

But what about when val=1e6?

For example, k=1e6, which factors into 2^6 *5^6.

Each val is 2^6=64 and 5^6=15625.

If c_i includes 64 and 15625, then yes. Else, no.

So code would correctly compute.

But let's see if the code can compute 5^6.

The loop:

for e=6:

initial val=1.

Multiply by 5 each time:

1*5=5 → e=1.

5*5=25 → e=2.

25*5=125 →e=3.

125*5=625 →e=4.

625*5=3125 →e=5.

3125*5=15625 →e=6.

No overflow.

So val=15625.

Check if any c_i is divisible by 15625. If yes, then ok.

Otherwise, output no.

Thus code works.

Now, the code is written correctly. So this should handle all cases.
</think>

```python
import sys

def factorize(k):
    factors = {}
    while k % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        k = k // 2
    i = 3
    while i * i <= k:
        while k % i == 0:
            factors[i] = factors.get(i, 0) + 1
            k = k // i
        i += 2
    if k > 1:
        factors[k] = 1
    return factors

n, k = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))

if k == 1:
    print("Yes")
    sys.exit()

factors = factorize(k)

for p, e in factors.items():
    val = 1
    over = False
    for _ in range(e):
        val *= p
        if val > 10**6:
            over = True
            break
    if over:
        print("No")
        sys.exit()
    found = any(num % val == 0 for num in c)
    if not found:
        print("No")
        sys.exit()

print("Yes")
```