<think>
Okay, let's see. The problem is to determine if the sum of factorials of the array elements is divisible by x!. Hmm.

First, I need to understand the mathematical condition here. So, the sum S = a1! + a2! + ... + an! must be divisible by x!. Let's think about the properties here.

For a number to be divisible by x!, all the prime factors in x! must be present in sufficient quantity in the sum. But directly computing factorials for large x (like 5e5) is impossible due to size. So, there's a smarter way here.

Wait, but since x! divides a number if that number is a multiple of x!, then perhaps the sum S modulo x! should be zero. But calculating factorials mod x! is possible. Wait, because any a_i >=x will have a_i! which is divisible by x! (since x! is a factor of a_i! when a_i >=x). But wait, the problem says a_i <= x. Oh right! The input constraints state that each a_i is <= x. So in that case, all a_i! are <= x! So, for any a_i, a_i! is a factor of x! only if a_i ==x. Wait, no. Wait, x! is x * (x-1) * ... * 1. So if a_i is less than x, then a_i! divides x! because x! = x * (x-1) * ... * (a_i + 1) * a_i! So yes, a_i! is a divisor of x!.

But then, when you sum multiple such terms, each of which is a divisor of x! (but smaller than x!), their sum must be divisible by x! for the sum to be divisible by x!.

Wait, but how? Let's take an example. Let's say x is 4. Then x! is 24. Suppose the sum is 3! + 2! + ... etc. Each term is a divisor of 24. But when you add them up, the total sum must be a multiple of 24.

Hmm. So for the sum to be divisible by x! (24 in this case), the sum of all the a_i! must be a multiple of 24.

But how to compute this efficiently given the constraints of n up to 5e5 and x up to 5e5.

Calculating each a_i! and adding them up is impossible because even for x=5e5, the factorial is way too large. So we need another approach.

Wait, but when considering modulo x!:

The sum S mod x! must be zero. So if we can compute the sum of each a_i! mod x!, and check if that sum is zero, then the answer is yes.

But x! is huge. Storing x! is impossible for x=5e5. So how to compute a_i! mod x! ?

Wait, but if a_i < x, then a_i! is less than x! (since x! is x*(x-1)*...*(a_i+1)*a_i! ), so a_i! mod x! is just a_i!.

If a_i == x, then a_i! is x! mod x! is zero. So for a_i == x, their factorial mod x! is zero.

Wait, but in the problem statement, the a_i's are all <=x. So:

For each a_i in the array:

If a_i ==x: then a_i! is x! → mod x! is 0. So adding this to the sum contributes 0.

If a_i <x: then a_i! is a number less than x! (since x! = x*(x-1)*...*(a_i+1) * a_i! ). So mod x! is a_i!.

Therefore, the sum S mod x! is equal to the sum of all a_i! where a_i <x, because the a_i=x terms contribute zero.

So the problem reduces to: check if the sum of a_i! for all a_i <x is divisible by x!.

Wait, but that sum is S = sum (a_i! for a_i <x). Because the a_i=x terms add 0.

So, if S mod x! ==0 → yes.

But x! is a very large number. How can we compute this?

But S is the sum of terms that are each a_i! where a_i <x. So each term is less than x!.

So the sum S can be up to n * (x-1)!. For example, if n is 5e5 and x is 5e5, then (x-1)! is (5e5-1)!, which is a gigantic number. So storing the sum directly is impossible.

So we need to compute the sum modulo x! and see if it is zero. But how?

But x! is x multiplied by (x-1)!. So x! = x * (x-1)!.

Wait, maybe there's a way to find the sum modulo x! by considering the sum modulo x and modulo (x-1)! ?

Alternatively, think about the sum S. For S to be divisible by x!, S must be divisible by x. Because x! divides S implies x divides S. Similarly, it must be divisible by (x-1), and so on. But that's not sufficient. So that approach probably won't work.

Another angle: For S to be divisible by x!, the sum must have all the prime factors of x! in sufficient counts. But this seems complicated to compute.

Wait, but notice that for each a_i < x, a_i! is a divisor of (x-1)! (since a_i <=x-1). So, (x-1)! is the product of all numbers up to x-1. So for a_i <x, a_i! divides (x-1)!.

Thus, each term a_i! is a divisor of (x-1)!.

Therefore, the sum S is equal to the sum of some terms each of which is a multiple of (x-1)! divided by some factors. Wait, perhaps not. Let's see: (x-1)! = (x-1)(x-2)...1. So for a_i <x, a_i! is a factor of (x-1)!. So, each a_i! can be written as (x-1)! divided by (x-1)(x-2)...(a_i+1). But how does that help?

Alternatively, since S is the sum of terms that are divisors of (x-1)!, then S is a multiple of (x-1)! only if each term is. But no, because the sum of multiples of (x-1)! is a multiple of (x-1)!. So if S is divisible by x! =x*(x-1)!, then S must be divisible by x and by (x-1)!.

But (x-1)! is part of x!.

Wait, so the sum S must be divisible by x! if and only if:

The sum S is divisible by x (since x! =x*(x-1)!) and S is divisible by (x-1)!.

But since each a_i! is divisible by (x-1)! only if a_i >= (x-1). Wait no, because if a_i is less than x-1, then a_i! is a factor of (x-1)! but not necessarily divisible by (x-1)!.

For example, if x is 4, (x-1)! is 6. Then a_i=3 (x-1=3) has a_i! =6, which is divisible by 6. But a_i=2 has a_i! =2, which is not divisible by 6. So the sum S would have terms that are 2, etc. So S could be a sum of terms that are not divisible by (x-1)!.

But how can S be divisible by x! in that case?

In the first example, the sum was 24 (which is 4! *1). So sum is 24, x! is 24. So 24 is divisible by 24.

But in that example, (x-1)! is 6. The sum is 24, which is 4*6. So divisible by 6, and 24/6=4, which is divisible by x=4. So in that case, S is divisible by x! =4*6=24.

So the idea is that S must be divisible by (x-1)! and also by x. Because x! =x * (x-1)!, and (x-1)! and x are coprime (since x is a prime or not, but for x >=2, x and (x-1)! are coprime only if x is prime. Wait, no. If x is 4, (x-1)! is 6, which is divisible by 2 and 3. x is 4, which is 2^2. So 4 and 6 have a GCD of 2. So they are not coprime. So perhaps this approach is not correct.

Hmm. Maybe we need to think of the sum S in terms of (x-1)! multiplied by some coefficient.

Since each a_i! divides (x-1)! (because a_i <x), we can express each a_i! as (x-1)! / (product of (x-1)(x-2)...(a_i+1)).

But this seems complicated. Alternatively, perhaps factorials can be represented in terms of their exponents in the prime factors. But that might be computationally intensive for x up to 5e5.

Alternative approach: Let's note that x! divides S if and only if for every prime p and exponent e in x!'s prime factorization, S has at least e exponents of p.

But calculating the exponents of primes in x! and in S would be time-consuming for large x. But perhaps we can find a way to compute the exponents in S and check if they are at least those in x!.

But x is up to 5e5. Let's see. How many primes are there up to 5e5? It's about 41538 primes (approximate). For each prime, compute the exponents in x! and in S.

But for each prime p, the exponent in x! is given by the sum floor(x/p) + floor(x/p^2) + ... until p^k >x.

Then, for the sum S, each term a_i! contributes exponents for each prime. But S is the sum of all a_i! terms, so the exponents of primes in S are the minimum exponents from all terms? No, that's not correct. For example, sum 2 + 2 =4. Each term 2 has exponent 1 for prime 2, but the sum 4 has exponent 2. So exponents in a sum are not straightforward.

This approach might not work because the sum's exponents can't be directly determined from individual terms. For example, adding 2 and 2 gives 4, which has more exponents of 2. But adding 2 and 3 gives 5, which has exponents 0 for 2 and 3.

So this approach seems unmanageable.

Alternative idea: Since all a_i <=x, and x! is the product of all primes up to x in their respective exponents, perhaps there is a way to find that S must be divisible by x! by checking if for each a_i, the sum includes enough multiples of x!.

Wait, but a_i <x, so their factorials are factors of (x-1)! and do not include x as a factor. So the sum S is sum of terms (a_i! where a_i <x) plus 0 for a_i=x. But x! is x*(x-1)!. So S is sum of terms that are all factors of (x-1)!. So the sum S can be written as (x-1)! * k, where k is the sum of (a_i! / (x-1)!) for each a_i <x. But a_i! / (x-1)! is 1/( (x-1)(x-2)...(a_i+1) ) ) if a_i <x-1. So for example, if a_i =x-2, then a_i! = (x-2)! = (x-1)!/(x-1). So a_i!/(x-1)! = 1/(x-1). Similarly, for a_i =x-3, it's 1/( (x-1)(x-2) ), etc.

So the sum S is (x-1)! * sum (1/( (x-1)(x-2)...(a_i+1) )) for a_i <x.

Then, x! is x*(x-1)!.

So S is divisible by x! if and only if sum (1/( (x-1)(x-2)...(a_i+1) )) is divisible by x. Because S = (x-1)! * sum, and x! =x*(x-1)!.

So, the sum must be divisible by x.

So, the problem reduces to: compute the sum of 1/( (x-1)(x-2)...(a_i+1) ) for all a_i <x, and check if this sum is divisible by x.

But how to compute this sum? Because even for x=5e5, the denominators could be very large. But since we need the sum modulo x (since divisibility by x is required), perhaps we can compute each term as the modular inverse of the product (x-1)(x-2)...(a_i+1) modulo x, and sum them modulo x. Then check if the sum is 0 mod x.

Wait, yes. Because:

sum = sum_{a_i <x} [ 1/( (x-1)(x-2)...(a_i+1) ) ]

This is equivalent to sum_{k=1 to x-1} [ count[k] * 1/( (x-1)(x-2)...(k+1) ) ]

Because a_i can be from 1 to x-1.

So, for each a_i <x, the term is 1 divided by the product of integers from a_i+1 to x-1. Let's denote for a given a_i =k, the product is (x-1)*(x-2)*...*(k+1). Let's call this product P(k). Then the term is 1/P(k).

So sum all such terms for each a_i in the array (if a_i <x) and check if the sum is divisible by x.

But how to compute 1/P(k) mod x. Because x can be up to 5e5.

Wait, but x can be up to 5e5, which is manageable.

Let me think. For each a_i =k <x, we need to compute the inverse of P(k) modulo x. Then sum all these inverses multiplied by the count of k in the array. If the total sum mod x is zero, then the answer is yes.

So the steps would be:

1. Precompute for each k (from 1 to x-1) the product P(k) = (x-1)*(x-2)*...*(k+1). Then compute the modular inverse of P(k) mod x.

But x can be up to 5e5. How to compute P(k) mod x and their inverses efficiently.

But wait, for k from 1 to x-1:

P(k) is the product of all integers from k+1 to x-1. So P(k) = (x-1)! / (k! )

But (x-1)! /k! is the product from k+1 to x-1.

So, for each k, P(k) = (x-1)! / (k! )

But modulo x.

But since x can be a prime or composite. If x is prime, then (x-1)! mod x is x-1 (Wilson's theorem). But if x is composite, then (x-1)! mod x can be zero. For example, x=4: 3! mod 4 is 6 mod4=2. But 6 is not zero.

Wait, but (x-1)! mod x is zero if x is a composite number with at least two distinct prime factors. For example, x=6: 5! =120 mod6=0. But x=4 (which is 2^2) 3! mod4= 6 mod4=2. So Wilson's theorem says that if x is prime, (x-1)! ≡-1 modx. So for x prime, (x-1)! ≡-1 modx.

But in our problem, x can be anything up to 5e5.

So, for each k <x, P(k) is (x-1)! /k! → which modulo x can be written as [(x-1)! modx] * [ (k! )^{-1} modx ].

Because division in mod x is multiplication by the modular inverse.

But (x-1)! modx can be either -1 (if x is prime) or some other value (if x is composite). Let's denote (x-1)! modx as F. Then P(k) modx is F * inv(k! modx) modx.

But inv(k! modx) is the inverse of k! modx in modx.

So, the inverse of P(k) modx is inv( F * inv(k! ) modx ) modx → which is inv(F) * k! modx.

Because the inverse of a product is the product of inverses in reverse order.

Wait, let's see:

P(k) = F * inv(k! ) modx → so inv(P(k)) = inv(F) * k! modx.

Because P(k) * inv(P(k)) ≡1 modx.

So:

inv(P(k)) = inv(F) * k! modx.

Thus, for each k, the inverse of P(k) modx is equal to inv(F) multiplied by k! modx, all modx.

So, to compute inv(P(k)) modx for each k, we can precompute F = (x-1)! modx. Then compute inv_F = modular inverse of F modx. Then for each k, inv_Pk = inv_F * (k! modx) modx.

But how to compute k! modx for all k up to x-1?

This can be done with a precomputed factorial array modulo x.

But x can be up to 5e5. So for x up to 5e5, precomputing factorial modx up to x-1 is feasible.

Once we have inv_Pk for each k, then the sum is sum over all a_i <x of inv_Pk, multiplied by the count of each a_i in the array.

Then, this sum modulo x must be zero for the answer to be Yes.

So the steps are:

1. Compute F = (x-1)! modx.

2. Compute inv_F, the inverse of F modx. If F and x are coprime, the inverse exists. If F is zero, then inv_F does not exist, but in that case, the sum must also be zero modx. Wait, but how?

Wait, F is (x-1)! modx. So if x is a prime, then F is x-1 modx. Which is -1 modx, so inv_F is -1 modx (since -1 * -1 =1 modx). So in that case, inv_F exists.

But if x is composite, F could be zero. For example, x=6, (x-1)! =5! =120 mod6=0. So F is zero. Then inv_F doesn't exist. But how does this affect the sum?

In such cases, when F is zero, then P(k) = F * inv(k! ) modx is zero. So each term inv_Pk is inv(0) modx, which is undefined. But in reality, P(k) is (x-1)! /k! → which for x=6, (5! ) /k! = 120 /k! → but when x=6, which is composite, and k! is 1!, 2!, etc. But when x=6 is composite, (x-1)! is 5! =120, which is 0 mod6. So P(k) mod6 is (0 * inv(k! mod6 )) mod6. But inv(k! mod6) exists only if k! and 6 are coprime.

But for example, if k=3, then k! =6 mod6=0. So inv(k! mod6) is undefined. So this approach might not work when x is composite.

But wait, perhaps there's a smarter way.

Let me consider when x is composite. Let's say x=4.

Then, (x-1)! is 3! =6 mod4=2.

So F=2. inv_F is 3 mod4 (since 2*3=6 mod4=2*3=6 mod4=2, which is not 1. Wait, this is a problem. Wait, 2 mod4. The inverse of 2 mod4 should exist only if gcd(2,4)=1. But gcd(2,4) is 2. So inverse does not exist. So inv_F is undefined. So how to proceed in that case.

Hmm. So in this case, when x is composite, F could be non-zero and not coprime with x. So inv_F may not exist. So this approach may not work.

But in the example where x=4, which is composite, F=2. Since gcd(2,4)=2, the inverse of 2 mod4 does not exist. So our approach breaks here.

But let's look at the problem again. For x=4, the sum S is sum of a_i! where a_i <4 (since a_i <=x). Then, the sum must be divisible by 4! =24. Let's take the first example, where sum is 24, which is divisible by 24 → yes.

But according to our earlier approach, the sum of 1/( (3)(2)(1) ) for each a_i. Wait, no. For each a_i <x, which is 4, the a_i can be 3, 2, 1, etc.

Wait, in the first example, the array is [3,2,2,2,3,3]. The x is 4. So a_i <x are all the elements here (since they are 3,2,2,2,3,3). For each a_i, the term is 1/( (4-1)(4-2)...(a_i+1) ). Let's compute for a_i=3. Then the product is (3) → since a_i+1 is 4, which is x. So P(3) is the product from 4-1 down to 3+1, but 3+1 is 4, which is x. So the product is (3) (since from 3 to 3+1 is 3+1=4, but x is 4, so (x-1) is 3. So for a_i=3, the product is 3 (since a_i+1=4, which is x, so the product from 4-1 down to a_i+1 is 3 to 4. Wait, but no. The product is (x-1) * (x-2) * ... * (a_i+1). So for a_i=3, a_i+1=4. So the product is terms from (x-1)=3 down to (a_i+1)=4. But 3 is less than 4. So there are no terms. So the product is 1 (empty product). So P(3) is 1.

Similarly, for a_i=2: product is (3) * (2+1) =3*3? Wait, no. Wait, x is 4. a_i=2. a_i+1=3. So product is (x-1)(x-2)...(a_i+1) =3 (since 3 is the next term after a_i+1=3). So for a_i=2, product is 3.

For a_i=1, product is 3*2* ... *2 → no, a_i+1=2. So product is 3*2 (since a_i+1=2, x-1=3, x-2=2. So product is 3*2=6.

So for each a_i:

a_i=3 → P(k)=1 → 1/P(k) =1.

a_i=2 → P(k)=3 → 1/3 mod4. But 3 and 4 are coprime, so inverse is 3 mod4 (since 3*3=9 mod4=1). So 1/3 mod4 is 3.

a_i=1 → P(k)=3*2=6 → mod4 is 2. 1/2 mod4 does not exist (since 2 and 4 are not coprime). So this approach would fail here.

But in the first example, the sum of terms is:

Number of 3s: 3 elements (a_i=3) → 3*1=3.

Number of 2s: 3 elements → 3*3 (since 1/3 mod4 is 3) → 9 mod4=1. So total sum is 3 +1 =4 mod4=0. So the sum is 0 mod4, which implies yes.

But for a_i=1, if there were any, the term would be 1/(6) mod4 → but 6 mod4=2. So inverse of 2 mod4 does not exist. So how to handle those cases?

So, in this case, when x is composite and F is not coprime with x, the approach breaks. So perhaps there's a mistake in the initial reasoning.

Wait, perhaps the sum S must be zero mod x! → but how?

Alternatively, perhaps the sum must be a multiple of x, but when x is composite, and some terms in the sum cannot be computed modulo x (because the denominator is not coprime with x), then the sum can't be a multiple of x, leading to the answer No. But that's not necessarily the case.

Wait, the original sum S is the sum of a_i! for a_i <x, and we want this sum to be divisible by x!.

But x! =x*(x-1)!.

Since all a_i! are <= (x-1)!, the sum S is the sum of terms each of which is <= (x-1)!.

So for S to be divisible by x*(x-1)!, the sum must be a multiple of x.

Because (x-1)! is a common factor of all terms. So sum S is (x-1)! * K, where K is the sum of 1/( (x-1)(x-2)...(a_i+1) ) for each a_i.

So S = (x-1)! * K.

Then x! divides S → x! | (x-1)! * K → x divides K.

So K must be divisible by x.

So the problem reduces to whether K is divisible by x. But K is sum of 1/( (x-1)(x-2)...(a_i+1) ) for each a_i <x.

But how to compute K modulo x?

In the case where x is composite and F = (x-1)! modx is not coprime with x, then the approach involving inverses may not work. But maybe there's another way.

Alternatively, note that if x is composite and not a prime power, then (x-1)! is divisible by x. For example, x=4 is 2^2. (x-1)! is 6, which mod4 is 2. But x=6, (x-1)! is 120 mod6=0. So in some cases, F=0, and the sum may or may not be divisible by x.

But when F=0, then K = sum of [ (x-1)! / (k! ) ]^{-1} modx → but (x-1)! is divisible by x, so (x-1)! /k! is divisible by x / (k! )? Not sure.

Wait, but in this case, when x is composite and F=0, then (x-1)! is divisible by x.

So (x-1)! = m *x for some integer m.

Then, for each a_i <x, a_i! is a divisor of (x-1)! → which is divisible by x. So, for each a_i <x, (x-1)! /a_i! is divisible by x/(gcd(a_i!, x)).

But I'm not sure.

Alternatively, when x is composite and x divides (x-1)!, which is the case when x is not a prime and not a square of a prime. For example, x=4: 3! =6 not divisible by4. x=6:5! is 120, divisible by6.

So for x=4, (x-1)! is not divisible byx. But for x=6, yes.

So in cases where x is composite and (x-1)! is divisible byx, then K is sum of ( (x-1)! /a_i! ) / (x-1)! ), which is sum of 1/a_i! (but no, that's not correct).

Alternatively, let's think of K = sum of 1/( (x-1)(x-2)...(a_i+1) ), which is the same as sum of 1/( product from (a_i+1) to (x-1) )

But how can we compute this sum mod x when x is composite.

Alternatively, perhaps K is zero modx.

Wait, if x is composite and (x-1)! is divisible by x, then for any a_i <x, (x-1)! /a_i! is divisible by x / (a_i! / gcd(x, a_i! )).

Not sure.

Alternatively, perhaps the sum K can be written as sum of terms of 1/( (x-1)(x-2)...(a_i+1) ), and since (x-1)(x-2)...(a_i+1) is the product of numbers greater than a_i, but how.

This seems like a dead end.

Alternative approach: for each a_i <x, the term is a_i! So the sum S is the sum of a_i! for a_i <x.

We need to check if S is divisible by x!.

But since x! is x*(x-1)!, and all a_i! divide (x-1)!, then S is a multiple of (x-1)!.

So S = (x-1)! * k.

Thus, x! divides S iff x divides k.

Because S = (x-1)! *k, and x! =x*(x-1)! → x! divides S → x divides k.

So, k is the sum of (a_i!)/(x-1)! for each a_i <x.

So, k = sum_{a_i <x} [ a_i!/(x-1)! ]

So, to check if x divides k.

Thus, the problem reduces to computing k and checking if k modx is zero.

But a_i!/(x-1)! = 1/( (x-1)(x-2)...(a_i+1) )

So k is the sum of 1/( (x-1)(x-2)...(a_i+1) ) for each a_i <x.

So, again, we need to compute this sum modx.

But how to compute this sum modx when x can be up to 5e5.

Hmm. Let's think of each term as the product of the inverses of the numbers from a_i+1 to x-1.

For example, if a_i is k, then the term is 1/( (k+1) * (k+2) * ... * (x-1) )

The product can be computed as the product from k+1 to x-1, which is (x-1)!/(k! )

Thus, the term is 1/( (x-1)! /k! ) ) → k!/(x-1)! → but we need to compute this modulo x.

But (x-1)! modulo x is F. So the term is (k! / (x-1)! ) modx → (k! * inv(F) ) modx.

But inv(F) exists only if F and x are coprime.

If F and x are coprime, then inv(F) exists, and the term can be computed as k! * inv(F) modx.

But if F and x are not coprime, then inv(F) does not exist, which implies that F and x have a common divisor. But in that case, k! must also share that common divisor. So maybe the product k! * inv(F) is not an integer.

But this is getting complicated.

Alternative idea: precompute for each k, the product from k+1 to x-1 modulo x. Then the term for a_i=k is the inverse of that product modulo x. Sum all these terms multiplied by their frequencies and check if the sum modx is zero.

But how to compute the product from k+1 to x-1 modulo x for each k.

Let's note that the product from k+1 to x-1 can be computed as the product from 1 to x-1 divided by the product from 1 to k. So, if we precompute prefix products modulo x for all numbers up to x-1, then the product from k+1 to x-1 is (prefix_product[x-1] * inv(prefix_product[k])) modx.

But prefix_product[x-1] is (x-1)! modx, which is F.

So, for each k, product(k+1, x-1) modx is (F * inv(prefix_product[k])) modx.

Thus, for each a_i=k, the term is inv( product(k+1, x-1) ) modx → which is inv( F * inv(prefix_product[k] ) ) modx → which is inv(F) * prefix_product[k] modx.

But again, inv(F) exists only if F and x are coprime.

If F is zero modx, then product(k+1, x-1) modx is zero * inv(prefix_product[k]) → which is zero. So the inverse does not exist. So any a_i=k where product(k+1, x-1) is zero modx would have an undefined inverse, making the sum undefined modx. But in such cases, the sum would have terms that are undefined, implying that it's impossible for the sum to be zero modx. But this may not be the case.

For example, consider x=4. F =3! mod4=6 mod4=2. So F is 2, which is coprime with 4 (since gcd(2,4)=2). So inv(F) does not exist. Thus, the approach fails here.

But in the first example, the sum of terms modx=4 is 0. So how is that possible?

Hmm. So perhaps there's a way to handle cases where F and x are not coprime.

Let me re-examine the first example:

n=6, x=4, array [3,2,2,2,3,3]. All a_i <4.

For each a_i=3, the product from 3+1=4 to x-1=3 is empty → product is 1. So term is 1/1 mod4 =1.

For a_i=2: product is from 3 to 3 → 3 mod4=3. So inverse is 3^{-1} mod4 → 3, since 3*3=9 mod4=1.

So term is 3.

The sum is 3 terms of 3 (each a_i=3 contributes 1) and 3 terms of 2 (each contributes 3). So sum is 3*1 +3*3 =3+9=12 mod4=0. So sum mod4 is 0 → yes.

But according to the previous approach, F=3! mod4=6 mod4=2. inv(F) doesn't exist. So how is the sum computed?

But the product from k+1 to x-1 for a_i=3 is product of 4 to 3 → which is 1. So the term is 1/1 → 1 mod4. Which is correct.

For a_i=2, product from 3 to 3 is 3. So term is 1/3 mod4 → 3 mod4.

So the sum is (3*1) + (3*3) =3+9=12 mod4=0.

But according to the approach where inv(F) is needed, what happens?

F=2. So inv(F) does not exist. But the product for a_i=2 is 3. The inverse of 3 mod4 is 3. Which is correct.

So the product from 3 to 3 is 3. So the term is 1/3 mod4 =3.

So the approach of directly computing the product for each a_i and taking its inverse modx works even when F and x are not coprime. Because the product for each a_i might have a multiplicative inverse even if F does not.

So perhaps the correct approach is:

For each a_i <x:

Compute the product of (k+1) to (x-1) modx.

If this product is zero modx → then the inverse doesn't exist. So the sum is undefined and thus cannot be zero → answer is No.

If the product is non-zero modx → compute its inverse and add to the sum.

If any a_i has a product that is zero modx, then their inverse doesn't exist → sum can't be zero → answer is No.

So the steps are:

1. For each a_i in the array, if a_i ==x → ignore.

2. For a_i <x:

   a. Compute the product P of (a_i+1) to (x-1) modx.

   b. If P modx is zero → the inverse doesn't exist → the sum can't be zero → answer No.

   c. Otherwise, compute inv_P = inverse of P modx.

   d. Sum += count[a_i] * inv_P modx.

3. After processing all a_i, if the sum modx is zero → answer Yes. Else, No.

So this approach requires:

- Precomputing for each possible a_i (1 <=a_i <x) the product P of (a_i+1) to (x-1) modx.

But for x up to 5e5 and n up to 5e5, this is feasible.

But how to compute P for each a_i efficiently.

The product from a+1 to x-1 can be computed as the product from 1 to x-1 divided by the product from 1 to a.

But since we are working modulo x, division is multiplication by the inverse.

But the product from 1 to x-1 is F = (x-1)! modx.

The product from 1 to a is prefix_product[a] modx.

So for a given a, the product from a+1 to x-1 is (F * inv(prefix_product[a])) modx.

So, we can precompute prefix_product array modx for 1 to x-1.

Then, for each a, P = (F * inv(prefix_product[a])) modx.

But inv(prefix_product[a]) exists only if prefix_product[a] and x are coprime.

If prefix_product[a] and x are not coprime, then the product (F * inv(...)) may be zero or not.

But this approach requires that for each a, compute inv(prefix_product[a]) modx. Which may not exist.

If for any a, inv(prefix_product[a]) does not exist, then the product P is (F * inv(prefix_product[a])) modx, but since inv(prefix_product[a]) doesn't exist, this implies that prefix_product[a] and x are not coprime. So F must have a common factor with x. But this is getting too complicated.

Alternative idea: For each a, compute the product from a+1 to x-1 modx directly.

But for x up to 5e5, and a up to x-1, this would be O(x) time, which is acceptable.

But for x=5e5, this would be O(5e5) time to precompute all possible a.

But for each a, the product is the product of (a+1) to (x-1). So for a=x-1, the product is 1 (empty product). For a=x-2, product is x-1 modx. For a=x-3, product is (x-1)*(x-2) modx, etc.

So, we can compute this product for each a in reverse order.

We can precompute an array prod where prod[a] is the product from a+1 to x-1 modx.

prod can be computed as follows:

prod[x-1] =1 (since there are no terms).

prod[a] = ( (a+1) * prod[a+1] ) modx, for a from x-2 down to 0.

Wait, no. For example, a= x-2:

prod[a] = product from a+1 to x-1 → which is x-1 modx.

prod[x-3] = (x-2) * (x-1) modx → etc.

So starting from x-1, which has prod[x-1] =1.

Then for a=x-2, prod[x-2] = (x-1) * prod[x-1] modx = (x-1) *1 modx.

For a=x-3, prod[x-3] = (x-2) * prod[x-2] modx = (x-2) * (x-1) modx.

So this approach can precompute the prod array in O(x) time.

Yes! So this is feasible.

So steps:

1. Compute the prod array where prod[a] is the product of (a+1) to (x-1) modx.

   a. Initialize prod[x-1] =1.

   b. For a in x-2 downto 0:

      i. prod[a] = ( (a+1) * prod[a+1] ) %x.

But wait, since a can be as low as 0 (but a_i >=1). So for a=0, the product is 1*2*...*(x-1) modx.

But the array will be computed for a from 0 tox-1.

But in the problem, a_i is >=1. So when a_i=0, which is not possible according to the input constraints (a_i >=1). So we don't have to worry about a=0.

But in the code, we need to process a_i from 1 to x-1.

So, for each a_i in the array (which are >=1 and <x), compute prod[a_i] as the product from a_i+1 to x-1 modx.

Then, for each such a_i, check if prod[a_i] is zero modx. If it is, then the inverse doesn't exist, so the answer is No.

Otherwise, compute the inverse of prod[a_i] modx and multiply by the count of a_i, adding to the sum.

After processing all a_i, check if sum modx is zero.

So the code steps:

Read n and x.

Read the array a.

count = frequency count of each a_i that is <x.

For all a in count:

   if a >=x: continue.

   compute product = prod[a]

   if product ==0 modx → answer is No.

   else:

       inv = modular inverse of product modulo x.

       sum += count[a] * inv

       sum %=x

If after processing all a, sum ==0 → Yes else No.

But how to compute the product array.

Let's see for x=4:

prod[3] =1.

prod[2] =4-1=3 (since a=2, a+1=3 → 3 * prod[3] =3*1=3 mod4=3.

prod[1] =2 * prod[2] → 2*3=6 mod4=2.

prod[0] =1 * prod[1] →1*2=2 mod4=2.

For a=3 (a_i=3), product is 1 → inverse is 1 mod4.

For a=2 (a_i=2), product is3 → inverse is3.

For a=1 (a_i=1), product is2 → inverse is 2 (since 2*2=4 mod4=0 → no. Wait, 2 and 4 are not coprime. So inv does not exist. So if any a_i=1 in x=4, then product is 2 mod4=2. So inverse is needed, but 2 and 4 are not coprime. So the inverse does not exist, so answer is No.

But in the first example, the a_i are 3 and 2. So their products are 1 and 3, inverses are 1 and3. So sum is 3*1 + 3*3=3+9=12 mod4=0 → yes.

So this approach works.

Another example: x=3.

prod[2] =1.

prod[1] =2*1=2 mod3=2.

prod[0] =1*2=2 mod3=2.

For a=2: product is1 → inverse 1.

a=1: product=2 → inverse is 2 mod3 (since 2*2=4 mod3=1).

So for the second example:

array is 3, 2, 2, 2, 2, 2, 1, 1. x=3. So a_i <3: 2,2,2,2,2,1,1.

For a=2: product is1 → inv is1. count=5: 5*1=5 mod3=2.

For a=1: product is2 mod3. So inv is 2. count=2: 2*2=4 mod3=1.

Sum is2+1=3 mod3=0 → yes.

This matches the sample.

Third example: x=8, array contains seven 7's. a_i=7 <8. So product from 8-1=7 to 7+1=8. So product is empty → 1. So inv is1. Sum is7*1=7 mod8=7 → not zero → answer is no. Which matches the sample.

Fourth example: x=5.

The array has elements 4,3,2,1,4,3,2,4,3,4. So a_i <5 are 4,3,2,1,4,3,2,4,3,4.

Count:

4 appears 4 times.

3 appears 3 times.

2 appears 2 times.

1 appears 1 time.

x=5.

prod array for x=5:

prod[4] =1.

prod[3] =4+1=5 mod5=0.

prod[2] =3 * prod[3] → 3*0=0 mod5=0.

prod[1] =2 * prod[2] → 0.

prod[0] =1 * prod[1] →0.

So for a=4: product is1 → inv is1.

a=3: product is0 mod5 → inv doesn't exist → answer is No.

So in this example, there are elements with a_i=3. So product is0 mod5. Hence, answer is No. Which matches the sample.

Another sample: input 2 500000 499999 499999. x=5e5.

prod for a=499999:

product is 5e5-1 +1 =5e5. So product is 5e5 mod5e5=0. So inv doesn't exist → answer is No.

Which matches the sample.

So this approach works.

Thus, the steps are:

1. Precompute the product from a+1 to x-1 modx for all a in 0 to x-1.

   This is done by starting from a=x-1 and moving backwards.

2. For each a in the array, if a >=x → ignore.

   Else, check if prod[a] is zero modx. If yes → answer is No.

   Else, compute the inverse of prod[a] modx.

3. Sum the count[a] * inverse modx for all a.

4. If the sum is zero modx → answer Yes, else No.

Now, code-wise:

We need to:

- Read n and x.

- Read the array and count the frequencies of each a_i where a_i <x.

- Precompute the prod array.

- For each a in the count:

   if prod[a] is zero → answer is No.

   else, compute inv.

   accumulate the sum.

- Check sum modx.

Now, in code:

In Python, for x=0, but according to constraints x>=1.

Precompute the prod array:

x can be up to 5e5. So precomputing prod for 0 to x-1 can be done.

But for x=5e5, the array would be of size 5e5, which is manageable.

But if x is 1, then x-1 is 0. But according to input constraints, a_i can be 1 if x=1? No, because in the input constraints, a_i <=x. If x=1, a_i can be 1. So for x=1:

prod array is computed for a from 0 to 0.

prod[0] = product from 0+1 to 1-1=0 → product from 1 to 0 → empty product, which is 1 mod1=0.

But x=1, so the sum of a_i! for a_i <x is sum of a_i=0 (but a_i can't be <x=1 since a_i >=1). So sum is zero. So sum is zero, and x! is 1. So 0 is divisible by 1 → answer is Yes.

But according to the code:

if x=1:

the array a must consist of 1's, which are a_i >=x. So count of a_i <x is zero. So sum is zero → sum modx=0 → answer is yes.

So code will handle this case.

Now, code:

Read n, x.

a = list of integers.

frequency = defaultdict(int)

for num in a:

    if num <x:

        frequency[num] +=1

if x ==0:

    # not possible since x >=1.

compute prod array.

prod = [1]*(x)

prod[x-1] =1

for a in range(x-2, -1, -1):

    prod[a] = ( (a+1) * prod[a+1] ) %x

But wait, x can be 1. Then x-1=0. So the loop runs for a from x-2 =-1 downto 0 → no iterations. So prod[0] is initialized to 1. Which for x=1, a=0:

prod[0] =1.

But for x=1, a_i can't be <x=1. So frequency is empty. sum is zero mod1=0 → yes.

But let's proceed.

Then:

sum_total =0

for a in frequency:

    if a >=x:

        continue

    p = prod[a]

    if p %x ==0:

        print("No")

        exit()

    try:

        inv = pow(p, -1, x)

    except ValueError:

        # inverse doesn't exist.

        print("No")

        exit()

    sum_total += frequency[a] * inv

    sum_total %=x

if sum_total %x ==0:

    print("Yes")

else:

    print("No")

But wait, in Python, pow(a, -1, x) will raise a ValueError if the inverse doesn't exist. However, in our code, before calling pow, we check if p modx is zero. Because if p modx is zero, then the inverse doesn't exist. But p is computed as (a+1)*prod[a+1] modx. So when x is composite, some a's may have p modx=0.

But in the code, for each a in frequency, we check if p is zero. If yes, print No and exit. Else, compute inv.

But when p is not zero modx, it may still not be coprime with x. For example, x=4, p=2. pow(2, -1,4) → error.

So the code would crash.

Ah, here's a problem. For example, x=4, a=1.

prod[a] =2.

pow(2, -1,4) raises an error because 2 and4 are not coprimes.

So the code would exit with ValueError.

But in that case, when p modx is not zero, but p andx are not coprimes, the inverse doesn't exist. So we need to check whether p andx are coprimes.

So the code needs to handle that.

But how?

The code will crash in such cases.

So in the code, after checking if p is zero modx, we need to check if p and x are coprime. If not, then the inverse doesn't exist, and the answer is No.

But checking gcd(p, x) ==1 for each a.

But x can be up to 5e5, and n up to 5e5. So for each a in frequency, this would add O( log x ) time per a.

But for 5e5 elements, this is manageable.

So the code should:

For each a in frequency:

   if a >=x: continue

   p = prod[a]

   if p ==0 modx → answer No.

   g = gcd(p, x)

   if g !=1 → answer No.

   inv = pow(p //g, -1, x//g) → but this is complicated.

Wait, no. If p andx are not coprimes, then inverse of p modx does not exist. So in such case, even if p is non-zero, the inverse doesn't exist. Hence, sum can't be computed, and answer is No.

Thus, the code needs to check whether p and x are coprimes. If not, answer is No.

So in the code:

for a in frequency:

    if a >=x:

        continue

    p = prod[a]

    if p ==0:

        print("No")

        exit()

    g = math.gcd(p, x)

    if g !=1:

        print("No")

        exit()

    inv = pow(p, -1, x)

    sum_total += frequency[a] * inv

    sum_total %=x

But this adds O( log x ) per a. Which is manageable.

But this can be optimized.

Wait, x is fixed. So compute the gcd(p, x) for each p.

But in practice, when x is prime, then all p are coprimes with x (since x is prime, and p modx is not zero, so gcd(p, x)=1).

But when x is composite, p modx can be non-zero but not coprime.

So the code must include this check.

So the steps are:

For each a in frequency:

   p = prod[a]

   if p ==0 modx → answer No.

   compute gcd(p, x). If not 1 → answer No.

   else, compute inv and add to sum.

Thus, the code must check this.

So in code:

import math

n, x = map(int, input().split())

a = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)

for num in a:

    if num < x:

        freq[num] +=1

if not freq:

    print("Yes" if 0 % x ==0 else "No")

    exit()

if x ==1:

    # All a_i are 1 (>=x=1), so sum is 0. 0 mod1 is 0 → Yes.

    print("Yes")

    exit()

# Precompute prod array.

prod = [1]*(x)

for a_i in range(x-2, -1, -1):

    prod[a_i] = ( (a_i +1) * prod[a_i +1] ) %x

sum_total =0

for num, cnt in freq.items():

    current_a = num

    if current_a >=x:

        continue

    p = prod[current_a]

    if p %x ==0:

        print("No")

        exit()

    g = math.gcd(p, x)

    if g !=1:

        print("No")

        exit()

    inv = pow(p, -1, x)

    sum_total = (sum_total + cnt * inv) %x

print("Yes" if sum_total %x ==0 else "No")

But let's test this code against the samples.

First sample:

Input:

6 4

3 2 2 2 3 3

x=4.

prod array:

prod[3] =1.

prod[2] =3*1 =3 mod4=3.

prod[1] =2*3=6 mod4=2.

prod[0] =1*2=2 mod4=2.

For a=3:

p=prod[3]=1. gcd(1,4)=1 → inv=1. sum +=3*1=3 mod4=3.

For a=2:

p=prod[2]=3. gcd(3,4)=1 → inv=3. sum +=3*3=9 mod4=1 → sum_total=3+1=4 mod4=0.

So sum is 0 → yes.

Second sample:

8 3

3 2 2 2 2 2 1 1

x=3.

prod array:

prod[2] =1.

prod[1] =2*1=2 mod3=2.

prod[0] =1*2=2 mod3=2.

For a=2: p=1, gcd(1,3)=1 → inv=1. sum +=5*1=5 mod3=2.

For a=1: p=prod[1]=2. gcd(2,3)=1 → inv=2. sum +=2*2=4 mod3=1 → sum_total=2+1=3 mod3=0 → yes.

Third sample:

7 8

7 7 7 7 7 7 7 → all a_i=7 <8.

x=8.

prod[7] =1.

prod[6] =7*1=7 mod8=7.

prod[5] =6*7=42 mod8=2.

prod[4] =5*2=10 mod8=2.

prod[3] =4*2=8 mod8=0.

prod[2] =3*0=0.

prod[1] =2*0=0.

prod[0] =1*0=0.

a=7: current_a=7. p=prod[7] =1. gcd(1,8)=1 → inv=1. sum=7*1=7 mod8=7. Not zero → answer is No.

Which matches the sample.

Fourth sample:

10 5

4 3 2 1 4 3 2 4 3 4 → a_i <5 are 4,3,2,1,4,3,2,4,3,4.

x=5.

prod array:

prod[4] =1.

prod[3] =4*1=4 mod5=4.

prod[2] =3*4=12 mod5=2.

prod[1] =2*2=4 mod5=4.

prod[0] =1*4=4 mod5=4.

For a=4:

p=prod[4]=1 → inv=1. sum +=4*1=4 mod5=4.

For a=3:

p=prod[3]=4. gcd(4,5)=1 → inv=4 (4*4=16 mod5=1). sum +=3*4=12 mod5=2 → 4+2=6 mod5=1.

For a=2:

p=prod[2]=2. gcd(2,5)=1 → inv=3 (2*3=6 mod5=1). sum +=2*3=6 mod5=1 → 1+6=7 mod5=2.

For a=1:

p=prod[1]=4. gcd(4,5)=1 → inv=4. sum +=1*4=4 mod5=2+4=6 mod5=1.

Total sum mod5=1 → not zero → answer is No.

Which matches the sample.

Fifth sample:

2 500000

499999 499999.

x=5e5.

prod array:

For a=499999 (current_a), p=prod[499999] = (499999+1) * prod[500000-1] → but x=5e5, a=499999 is x-1. So prod[499999] =1.

prod[499998] =499999 * prod[499999] → 499999 *1 mod5e5.

But 499,999 mod500,000 is 499,999. So prod[499998] =499,999.

But for a=499999, p=1. But x=5e5. 1 and x are coprimes. inv=1. sum +=2*1=2 mod5e5. So sum is 2 mod5e5 !=0 → answer is No.

Which matches the sample.

Thus, the code works.
</think>

```python
import math
import sys
from collections import defaultdict

def main():
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    freq = defaultdict(int)
    for num in a:
        if num < x:
            freq[num] += 1
    
    if not freq:
        print("Yes")
        return
    
    if x == 1:
        print("Yes")
        return
    
    # Precompute product array
    prod = [1] * x
    for a_i in range(x-2, -1, -1):
        prod[a_i] = ((a_i + 1) * prod[a_i + 1]) % x
    
    sum_total = 0
    for num, cnt in freq.items():
        current_a = num
        if current_a >= x:
            continue
        
        p = prod[current_a]
        if p % x == 0:
            print("No")
            return
        
        g = math.gcd(p, x)
        if g != 1:
            print("No")
            return
        
        inv = pow(p, -1, x)
        sum_total = (sum_total + cnt * inv) % x
    
    print("Yes" if sum_total % x == 0 else "No")

if __name__ == "__main__":
    main()
```