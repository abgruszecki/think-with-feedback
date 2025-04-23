<think>
Okay, let's tackle this problem. So, the task is to find the minimal possible number that satisfies certain conditions. Let's read the problem again carefully.

The number must be a positive integer with exactly p digits, no leading zeros. When we move the last digit to the front, the new number should be exactly x times the original. Also, we need the smallest such number possible. If none exists, output "Impossible".

Hmm. So, let's model this. Let's denote the original number as N. Let's say the last digit is d. Then, when we move d to the front, the new number M should be x * N.

The number N has p digits. Let's represent N as:

N = 10 * a + d, where a is the first p-1 digits. Then, moving the last digit to the front gives:

M = d * 10^{p-1} + a.

But M must equal x * N. So:

d * 10^{p-1} + a = x * (10a + d)

Let's rearrange this equation. Let's substitute M = x*N into the equation.

Expanding the right side:

d*10^{p-1} + a = x*10a + x*d

Let's rearrange terms to group like terms. Bring all terms to one side:

d*10^{p-1} - x*d = x*10a - a 

Factor:

d (10^{p-1} - x) = a (10x - 1)

Hmm. So, a = [d (10^{p-1} - x)] / (10x - 1)

But a must be an integer since it's part of the number. Also, d is a digit from 1 to 9 (since there are no leading zeros, the original number starts with a non-zero digit, so a can't have leading zeros either, implying that a must be a (p-1)-digit number possibly with leading zeros? Wait, no. Wait, N is a p-digit number with no leading zeros, so a is the first p-1 digits, so a can be between 10^{p-2} and 10^{p-1} - 1 (since the original number is of the form 10a + d, and a has p-1 digits). Wait, no. If N is a p-digit number, then a must be a (p-1)-digit number, but a can't have leading zeros. Wait, because the original number N is 10a + d. For example, if p=6, and a is 14285 (5 digits), then N is 14285*10 +7=142857. So a must be a (p-1)-digit number (so 10^{p-2} <= a < 10^{p-1}), but wait, no. Because a can be a number that's less than 10^{p-1}. For example, if N is 100000 (p=6), then a is 10000 (5 digits). So a must have exactly p-1 digits, meaning a >= 10^{p-2} when p>1, but for p=1, a is 0. Wait, but for p=1, the original number is a single digit d. Then moving the last digit (d) to the front gives the same number, so x must be 1. But in the sample input 2, when p=1 and x=2, it's impossible. So for p=1, the only possible x is 1, and the number is 1-9, but when you multiply by x (1), the rotated number (same as original) must equal x*N. So yes, x must be 1, and N is any digit from 1-9. But according to the problem, the number must be minimal. So for p=1 and x=1, the answer is 1. But the problem says that x can be up to 9, but in that case, for p=1, x must be 1. Otherwise, it's impossible.

But back to the general case. So for the equation a = [d (10^{p-1} - x)] / (10x - 1), a must be an integer. Also, since a is a (p-1)-digit number (so between 10^{p-2} and 10^{p-1} - 1), and d is a digit from 1 to 9 (since N has no leading zeros, and d is part of the last digit, which could be 0? Wait, N is 10a +d. Since N is a p-digit number, a must be a (p-1)-digit number (so a >= 10^{p-2} when p>1). But for p=1, a is zero. But when p=1, the original number is d. Then moving the last digit (d) to the front gives the same number, so x must be 1. So for p=1, the only possible x is 1, and the number is any d from 1-9. But since we need the minimal possible number, the answer would be 1.

But in the sample input 2, p=1 and x=2, the output is impossible.

So, for the general case where p >= 2.

We need to find d (1<=d<=9) such that:

- (10^{p-1} -x) must be divisible by (10x-1) multiplied by some factors, but in the equation, a is [d*(10^{p-1} -x)] / (10x-1). So for a to be an integer, (10x-1) must divide d*(10^{p-1} -x). Since d can vary from 1 to 9, perhaps for each possible d, we check if (10x-1) divides d*(10^{p-1} -x). Then, a must be equal to that quotient, and then a must be a (p-1)-digit number. Also, the resulting N must be a p-digit number (so a must be such that 10a +d is a p-digit number, i.e., a >= 10^{p-2} when p>1).

But how to compute this efficiently, especially for p up to 1e6? Because 10^{p-1} is a huge number when p is 1e6. So we can't compute 10^{p-1} directly as a number. So we need to compute (10^{p-1} mod (10x-1)), perhaps? Wait, but 10^{p-1} -x is being multiplied by d and then divided by (10x-1). Let me think.

Wait, the equation is:

d*(10^{p-1} -x) ≡ 0 mod (10x-1)

So for each d, 10^{p-1} ≡ x mod (10x-1) ?

Wait, 10^{p-1} -x must be congruent to 0 modulo (10x-1), multiplied by d. Wait, no. Let me see.

The equation is d*(10^{p-1} -x) must be divisible by (10x-1). So (10x-1) must divide d*(10^{p-1} -x). Let's denote k = 10x-1. So k must divide d*(10^{p-1} -x).

So for each possible d (1-9), we need k divides d*(10^{p-1} -x). Let's see.

Alternatively, since k is 10x-1, which is fixed once x is known. So for each d, we can compute whether 10^{p-1} ≡ x mod (k / gcd(k, d)).

But this approach might be complicated. Let's think differently.

Let me rearrange the equation:

We can write 10^{p-1} ≡ x mod (k / gcd(k, d)), where k=10x-1.

But perhaps a better approach is to find 10^{p-1} ≡ x mod (k) because:

We need k divides d*(10^{p-1} -x). Let's factor k into its prime factors. Then, the gcd of k and d is some g. Let g = gcd(k, d). Then, since d/g and k/g are coprime, the condition becomes (k/g) divides (10^{p-1} -x).

So (10^{p-1} -x) ≡ 0 mod (k/g).

But how to compute this for each d?

Alternatively, for each possible d (1-9), compute the required value of 10^{p-1} mod (k) and see if (d*(10^{p-1} -x)) is divisible by k.

Wait, perhaps not. Let me think.

The condition is that k divides d*(10^{p-1} -x). So d*(10^{p-1} -x) mod k must be zero. Which is equivalent to (10^{p-1} -x) mod (k/gcd(k,d)) == 0. Because:

d*(10^{p-1} -x) mod k =0 → (10^{p-1} -x) mod (k/gcd(d, k)) =0.

So for each d in 1-9, compute g = gcd(k, d). Then, check if (10^{p-1} -x) mod (k/g) ==0. If this is true, then possible. Then, a is equal to [d*(10^{p-1} -x)] / k. Then, check if a is a (p-1)-digit number (i.e., 10^{p-2} <= a <= 10^{p-1} -1) and that the resulting N = 10a +d is a p-digit number (which is already ensured by a being (p-1) digits and d being non-zero, since a can't have leading zeros).

Wait, but a is the first (p-1) digits. So if a is less than 10^{p-2}, then the original number would have less than p digits. For example, p=3, a=9 (single digit), d=5. Then N is 95, which is 2 digits, which is invalid. So a must be between 10^{p-2} and 10^{p-1} -1.

So the approach is:

For each d from 1 to 9:

1. Compute k = 10x -1.

2. Compute g = gcd(k, d).

3. Check if (10^{p-1} -x) mod (k/g) ==0. If not, skip this d.

4. If yes, then compute the required a as [d*(10^{p-1} -x)] / k.

5. Check if a is a (p-1)-digit number (i.e., 10^{p-2} <= a <= 10^{p-1}-1).

6. Also, check that when we form N = 10a +d, moving the last digit to the front gives x*N. Because maybe there are cases where the division is possible, but the actual rotation doesn't multiply by x. But perhaps the equation is derived in such a way that this is guaranteed once a is computed as per the equation. So maybe this step is redundant.

But for very large p, we can't compute 10^{p-1} directly. So how to compute 10^{p-1} mod (k/g) efficiently?

Ah, right. Because for each d, we need to compute (10^{p-1} -x) mod (k/g). Which is equivalent to (10^{p-1} mod m) -x mod m, where m = k/g. So if m is k/g, which could be up to (10x-1)/1 (if d and k are coprime). For x up to 9, k can be up to 89. So m can be up to 89. So for each d, m is manageable.

But how to compute 10^{p-1} mod m? That's easy with modular exponentiation. So for each d in 1-9:

Compute g = gcd(k, d), m = k/g.

Compute rem = pow(10, p-1, m).

Then, (rem - x) mod m must be 0. So (rem -x) mod m ==0 → rem ≡x mod m.

If this is true, then proceed.

Once that's confirmed, then a = [d*(10^{p-1} -x)] /k.

But how to compute a, given that 10^{p-1} can be very large? Because p can be up to 1e6, which would make 10^{p-1} a number with a million digits. Storing that is impossible. So how to compute a in a way that we can check if a has p-1 digits?

Wait, but a is equal to [d*(10^{p-1} -x)] /k. Let's see:

But when m divides (10^{p-1} -x), then (10^{p-1} -x) is equal to t*m for some integer t. Then, a = d * t * m / k. Wait, since m is k/g, then a = d * t * (k/g) /k = (d * t) /g.

But since g is gcd(k, d), then d/g and k/g (which is m) are coprime. So perhaps there's a way to compute a without dealing with 10^{p-1} directly. But how?

Alternatively, perhaps the formula for a can be written as a = [d*(10^{p-1} -x)] / (10x -1). But 10x-1 is k. So, when (10^{p-1} -x) is congruent to 0 mod (k/g), then (10^{p-1} -x) is divisible by k/g. So d*(10^{p-1} -x) is divisible by k, since (k/g) *d/g * ...? Hmm, perhaps I need to think differently.

But the key is that once the condition rem ≡x mod m is satisfied, then (10^{p-1} -x) is divisible by m, which is k/g. So the term [d*(10^{p-1} -x)] is equal to d * ( (10^{p-1} -x) ). Since (10^{p-1} -x) is divisible by m = k/g, then d * ( ... ) is divisible by m * d / (d, m). Wait, this is getting a bit messy. Let's think in terms of divisibility.

Once the condition holds, (10^{p-1} -x) is congruent to 0 mod (k/g), so (10^{p-1} -x) = s*(k/g) for some integer s. Then, substituting into a:

a = [d * s*(k/g)] / k = d*s*(k/g) /k = (d*s) /g.

So a must be (d*s)/g. Since g is the gcd(k, d), then d/g and k/g (m) are coprime. So s must be such that (d*s)/g is an integer. But since s is an integer, and (d/g) and (k/g) are coprimes, perhaps s can be written in terms of s = t * (k/g) ?

Not sure. But the main problem is that s is (10^{p-1} -x) / (k/g) = s = (10^{p-1} -x) / m.

But 10^{p-1} is a huge number. So how can we compute s and check if a is a (p-1)-digit number?

Wait, a is (d * (10^{p-1} -x )) /k. Let's see:

But 10^{p-1} -x is equal to s * m (since m = k/g). So:

a = (d * s * m ) / k = (d * s * (k/g) ) / k = (d * s ) / g.

So a must be (d*s)/g.

But how to compute s? Because s = (10^{p-1} -x)/m. But 10^{p-1} is a huge number. However, m is k/g, and k is 10x-1 (up to 89 when x=9). So m can be up to 89, which is manageable.

But (10^{p-1} -x)/m can be written as (10^{p-1} -x) = s*m. So s = [10^{p-1} -x]/m. But how to compute s? We can't compute 10^{p-1} directly, but perhaps s can be written as (10^{p-1}/m) - (x/m), but that doesn't help.

Alternatively, since 10^{p-1} mod m is known (we computed rem = pow(10, p-1, m)), then 10^{p-1} = q * m + rem. So s = (q * m + rem -x)/m = q + (rem -x)/m. But (rem -x) mod m is zero (since rem ≡x mod m), so rem -x = t*m for some integer t. So rem -x = t*m → s = q + t.

But q is 10^{p-1} // m. Which is a huge number. So s would be q + t, but again, we can't compute that directly.

Hmm. So this approach may not work because we can't compute s directly. So how to find a way to compute a's length?

Wait, the number a must be a (p-1)-digit number, so 10^{p-2} <= a < 10^{p-1}.

But a is [d*(10^{p-1} -x)] / k.

Wait, but 10^{p-1} is approximately equal to k * a / d + x. So perhaps for a to be (p-1) digits, the term (10^{p-1} -x) must be roughly k*a/d, which is of the order 10^{p-1} * (a/(d*k)).

But this is getting a bit abstract. Maybe there's another approach.

Alternatively, perhaps we can model N as a string. Then, moving the last digit to the front gives x*N. But for large p (up to 1e6), building the entire number as a string is impossible due to memory constraints. So we need a way to represent N's digits in a way that doesn't require storing all of them, but can generate them on the fly.

But the problem requires outputting the minimal possible number. So the minimal possible N would be the one with the smallest possible leading digit. So perhaps we can check for each possible d (from 1 to 9) in order, and once we find the smallest possible d that satisfies the conditions, we can compute a and then the number N=10a +d.

So the plan is:

For d in 1..9:

   Check if (10^{p-1} -x) is divisible by (k/gcd(k, d)), where k=10x-1.

   If yes, compute a = [d*(10^{p-1} -x)] /k.

   Check if a is a (p-1)-digit number (i.e., 10^{p-2} <= a < 10^{p-1}).

   Also, since N = 10a +d must be a p-digit number, and a is (p-1) digits, this is ensured as long as a >= 10^{p-2} (since d is >=1, 10a +d >= 10*(10^{p-2}) +1 = 10^{p-1}+1, which is a p-digit number. But 10^{p-1} is a 1 followed by p-1 zeros, so 10a is 10^{p-1} ... but if a is 10^{p-2}, then 10a is 10^{p-1}, which is a p-digit number starting with 1 followed by zeros. Adding d (1-9) gives 10^{p-1} +d, which is 1 followed by p-2 zeros and d. So yes, that's a p-digit number.

So the key steps are:

1. For each d from 1 to 9:

   a. Compute k = 10x -1.

   b. Compute g = gcd(k, d).

   c. m = k / g.

   d. Check if 10^{p-1} ≡x mod m. This can be done via modular exponentiation.

   e. If yes, then compute s = (10^{p-1} -x) / m. Since m divides 10^{p-1} -x, this is an integer.

   f. a = (d * s) / g. Since m = k/g, and s = (10^{p-1} -x)/m, then substituting into a's formula:

      a = [d * (10^{p-1} -x)] /k → since k = g * m, and m = (10^{p-1} -x)/s → wait, no. Let me re-express:

      The original a is [d*(10^{p-1} -x)] /k.

      Since 10^{p-1} -x = s * m, and m =k/g, then 10^{p-1} -x = s*(k/g).

      So substituting, a = d * s * (k/g) /k → a = d * s /g.

      So a = (d*s) /g.

      Now, since g is the gcd of k and d, then d/g and k/g are coprime. So s must be divisible by g / g' (where g' is gcd(g, s)), but perhaps this is not necessary. Wait, but a must be an integer, so d*s must be divisible by g. But since g is gcd(k, d), then g divides d, so d = g * d', where d' is integer. Then, a = (g*d' * s) /g = d' * s. So s must be an integer, which it is because (10^{p-1} -x) is divisible by m.

      So a is d' * s, where d' = d/g.

      Now, s is (10^{p-1} -x)/m. But m is k/g = (10x-1)/g. So s = (10^{p-1} -x) * g/(10x-1).

      Hmm. Not sure if that helps.

      But the problem is that s is (10^{p-1} -x)/m. Since 10^{p-1} is a very large number, how can we compute s?

      But s is equal to (10^{p-1} -x)/m. But m is up to 89 (since x can be up to 9, k=10x-1 up to 89, so m=k/gcd(k,d) could be up to 89). So for each d, m is a small number. So s is (10^{p-1} -x)/m. But 10^{p-1} is a 1 followed by p-1 zeros. So for example, when p=6, x=5, m=49 (since k=5*10-1=49, d=7, gcd(49,7)=7, m=49/7=7). Then s = (10^5 -5)/7 = (99995)/7 = 14285. Then a = (7 * 14285)/7 =14285. Then N=10a+7=142857, which matches the first sample.

      So how to compute s when p is up to 1e6?

      Well, 10^{p-1} -x is equal to (10^{p-1} -1) - (x-1). But 10^{p-1} -1 is a number consisting of p-1 9's. So subtracting (x-1) gives a number like 999... (p-1 times) minus x-1. For example, x=5 and p=6: 10^5-1=99999, subtract 4 (x-1=5-1=4) → 99995, which is 5 9's minus 4.

      But how to compute this number divided by m when m is small? For very large p (like 1e6), the number has 1e6 digits, which is impossible to handle directly.

      So the problem is to compute a = [d*(10^{p-1} -x)] /k, but how?

      Wait, but a must be a (p-1)-digit number. So a has exactly p-1 digits. So the value of [d*(10^{p-1} -x)] must be divisible by k, and the quotient must be a (p-1)-digit number.

      But given that p can be up to 1e6, we can't compute 10^{p-1} directly. So how can we compute a's digits?

      Wait, but a can be represented as a string. For example, when we divide a very large number (like 10^{p-1} -x) by k, using school method division. But for p up to 1e6, this would take O(p) time, which is manageable if optimized.

      So here's the plan:

      For each d from 1 to 9:

         Check if the modular condition holds (pow(10, p-1, m) ≡ x mod m).

         If yes, compute the number (10^{p-1} -x)/m, then multiply by d, divide by gcd(k, d) to get a.

         Then check if a has exactly p-1 digits.

      But how to compute (10^{p-1} -x)/m when p is up to 1e6?

      Let's think of (10^{p-1} -x) as a number with p-1 digits. For example, if x is 5 and p=6, then 10^5 is 100000, so 10^5-5=99995. But for p=1e6, this number has 1e6-1 digits, which is 999...9995 (1e6-1 digits).

      So how to divide this number by m (a small number, up to 89) and multiply by d/g?

      Well, perhaps perform the division as a string. Let's denote the number as S, which is 10^{p-1} -x. So S is a number with (p-1) digits. For example, when x is 5, S is 999...995 (with p-1 digits). For x=1, S is 999...999 (p-1 digits). For x=9, S is 999...9991 (since 10^{p-1} -9 is 999...9991).

      But how to compute S/m, and then multiply by d and divide by g, which is the gcd(k, d)?

      The division of a large number by m can be done digit by digit, similar to the way long division is done. For example, for each digit in S, we compute the current remainder and carry over. This would take O(p) time, which is acceptable for p up to 1e6.

      So here's the plan for each candidate d:

      1. Check the modular condition.

      2. If satisfied, proceed.

      3. Generate S as a string of digits: (10^{p-1} -x) → which is 1 followed by p-1 zeros minus x. But 10^{p-1} is a 1 followed by p-1 zeros. So subtracting x gives:

         For example, p-1=5, x=5: 100000 -5 = 99995.

         So for general case:

         S is 10^{p-1} -x. So S has p-1 digits. If x is less than 10, then S is 999... (p-1 times) minus (x-1). Wait, no. Wait:

         10^{n} is 1 followed by n zeros. So 10^{p-1} -x is:

         For example, p-1=5, x=5: 100000 -5 = 99995.

         So the first digit is 9, except for the last digit which is 10 -x.

         So the number S has p-1 digits, where all digits are 9 except the last digit, which is 10 -x. Wait, no. Wait, 10^{p-1} is 1 followed by (p-1) zeros. Subtracting x from this gives a number that is 999...999 (p-1 times) if x=1, but for x=5, it's 999...9995 (p-1 digits). So the number S is (10^{p-1} -1) - (x-1) = 999...999 (p-1 9's) minus (x-1). So if x-1 is subtracted from 999..999, the result is 999... (9 - (x-1)) in the last digit, but with possible borrow.

         Wait, no. Let's see:

         10^{p-1} is 1 followed by p-1 zeros. So 10^{p-1} -x is 999...999 (how many 9's?) Let's see:

         10^3 = 1000. 1000 -5=995. So 3 digits (p-1=3). So 1000-5=995 → 3 digits. So the first digit is 9, then 9, then 5.

         So 10^{p-1} is 1 followed by p-1 zeros. So subtracting x (<=9) from that gives a (p-1)-digit number. For example, p-1=5, x=5: 100000 -5 = 99995 (5 digits).

         So the first (p-2) digits are 9, and the last digit is 10 -x (if x !=0). Wait, no. For x=5, last digit is 0-5? No, 100000-5=99995. So the last digit is 5 (10-5=5?), but in this case it's 100000-5=99995. So last digit is 5. So the last digit is 10 -x, but when x=5, it's 5. Hmm, 10-5=5. So yes.

         So the last digit is 10 -x. But if x is 0, then 10 -0=10, but that would be a carry. But x is at least 1 (since the problem says the number is strictly positive and x is between 1 and 9).

         So the structure of S is:

         For x from 1 to 9:

            S is 999... (p-2 times) followed by (10-x).

         So S has p-1 digits: all 9's except the last digit, which is 10-x.

         For example, x=5, p-1=5 → S is 99995 (5 digits).

         So to generate S as a string, it's (p-2) '9's followed by (10-x). But since x can be up to 9, 10-x is between 1 and 9.

         So generating S as a string is easy: '9'*(p-2) + str(10 -x).

         Wait, but when p-1 is 1 (p=2), then S is 10 -x. For example, p=2, x=5: S is 10^1 -5=5, which is a single digit (5). Which is correct.

         So, S is a (p-1)-digit number consisting of (p-2) 9's followed by (10-x). So generating S as a string is straightforward.

         Now, the division of S by m (which is k/g) can be done as a string-based division. Then multiply by d and divide by g to get a. Then check if a is a (p-1)-digit number.

         But how to perform division of a large number represented as a string by a small integer m?

         Yes, this is manageable. For example, we can process each digit of S, keeping track of the remainder, and building the quotient digit by digit.

         For example:

         Divide 99995 by 7:

         9 ÷7 = 1, remainder 2.

         29 ÷7=4, remainder 1.

         19 ÷7=2, remainder 5.

         59 ÷7=8, remainder 3.

         35 ÷7=5, remainder 0. So the quotient is 14285.

         So this can be done digit by digit.

         So the steps are:

         For the current d, once we have S as a string, compute S divided by m. Let's call this quotient_part. Then multiply by d and divide by g (since a = d*quotient_part /g).

         But since quotient_part is (10^{p-1} -x)/m, then a = (d * quotient_part)/g.

         So how to compute this? Since quotient_part is a number with (p-1) digits divided by m (a small number), it can be up to (10^{p-1} -x)/m, which is a number up to (10^{p-1} -1)/1 → 10^{p-1}-1 digits. So quotient_part can be up to (p-1) digits. So multiplying by d (up to 9) gives a number up to (p) digits, then dividing by g (up to 89) gives a number up to (p) digits again.

         But this may be a problem for p=1e6, as handling a string of 1e6 digits is possible in Python if done efficiently.

         So here's the plan:

         For each d in 1..9:

            1. Compute k =10x-1.

            2. g = gcd(k, d).

            3. m =k/g.

            4. Check if 10^{p-1} mod m == x mod m.

                Compute rem = pow(10, p-1, m). Check if (rem -x) %m ==0.

            5. If not, continue.

            6. Else:

                Generate S as a string: '9'*(p-2) + str(10-x).

                Now, divide S by m using string division to get quotient_part (as a string).

                Then, multiply by d (as a string multiplication) → temp = quotient_part *d.

                Then divide temp by g (as a string division) → a (as a string).

                Check if a has exactly p-1 digits and no leading zeros.

                If yes, then form N by appending d to a (since N is 10a +d → a is the first p-1 digits, d is last digit).

                Check if N is valid (i.e., when rotated, equals x*N).

                Keep track of the minimal such N.

         But this approach may be too slow for p=1e6, as string-based division and multiplication for numbers of 1e6 digits can be O(p) time. However, since we have to process 9 possible d's, and for each d, perform O(p) operations, the total time is O(9p), which for p=1e6 is 9e6 steps. Python can handle this within the time constraints (as per time limits of 1 second, which is about 1e8 operations).

         But let's think about the steps:

         For example, when dividing S (as a string) by m:

         We can process each character in S, keeping track of the remainder. This is O(p) time.

         Similarly, multiplying the quotient_part (a string) by d (a single digit) can be done in O(p) time, as each digit is processed, multiplied by d, and carry is tracked.

         Then dividing by g (a small number, up to 89) is also O(p) time.

         So all steps are O(p), which is acceptable.

         Now, the steps in code:

         For each d from 1 to 9:

            compute k =10x -1.

            compute g = gcd(k, d).

            m =k //g.

            if m ==0: skip (but k is at least 9, since x >=1, 10x-1 >=9, so m can't be zero).

            compute rem = pow(10, p-1, m).

            if (rem -x) % m !=0 → skip.

            else:

                generate S as a string of (p-1) digits: '9'*(p-2) + str(10 -x).

                divide S by m → quotient_part_str.

                multiply quotient_part_str by d → temp_str.

                divide temp_str by g → a_str.

                check if len(a_str) == p-1 and a_str[0] != '0'.

                if yes:

                    N_str = a_str + str(d)

                    check if rotating N_str's last digit to front equals x*N_str.

                    (But verifying this for very large p is impossible directly, but since the equation is derived to ensure this, perhaps this step is redundant.)

                    add N_str to possible candidates.

         Then, among all valid candidates, choose the minimal one.

         But generating all possible candidates and then choosing the minimal is not feasible for p=1e6, since the string can be very large. So, the minimal candidate is the one with the smallest possible d (since we iterate d from 1 to 9) and the smallest a for that d (since a is minimal when the quotient is smallest). However, since a is computed as (d * s)/g, and s is fixed once d is chosen, the first valid d (smallest d) would give the smallest possible N.

         So, we can iterate d from 1 to 9 and return the first valid N_str (since it's the smallest possible).

         For example, in the first sample input, d=7 is the correct digit, but wait sample input 1's output is 142857. Let's see:

         For p=6, x=5:

         k=5*10-1=49.

         For each d from 1 to 9:

             compute g = gcd(49, d).

             m=49/g.

             check if 10^5 mod m ==5 mod m.

             Let's see for d=7:

                g = gcd(49,7)=7.

                m=49/7=7.

                rem = pow(10,5,7). 10^5 mod 7: 10 mod7=3. 3^5 mod7: 3^2=9 mod7=2, 3^3=6 mod7=6, 3^4=18 mod7=4, 3^5=12 mod7=5. So rem=5.

                (5 -5) mod7=0 → condition satisfied.

                S is 10^5 -5 =99995. So S is '99995'.

                divide 99995 by m=7 → 99995 /7=14285 → quotient_part_str is '14285'.

                multiply by d=7 →14285 *7= 99995.

                divide by g=7 →99995 /7= 14285. a_str is '14285', which is 5 digits (p-1=5), and starts with 1.

                So N_str is '142857', which is the correct answer.

         Since we iterate d from 1 to 9, and check for validity, the first valid d (smallest d) would give the minimal N. So in code, we can break early and return the first valid candidate.

         So in code:

         Iterate d from 1 to 9:

             for each d:

                 perform steps as above.

                 if a is valid (length p-1, no leading zeros), then compute N_str.

                 keep track of the minimal N_str.

         Once a valid N_str is found, return it. Otherwise, output 'Impossible'.

         Now, the problem is to implement the division and multiplication of large numbers represented as strings.

         Let's think about implementing the division of a large number (S) by m.

         Function to divide a number string by m:

         def divide(s, m):

             q = []  # quotient digits.

             rem =0

             for ch in s:

                 num = rem *10 + int(ch)

                 q_digit = num //m

                 rem = num %m

                 q.append(str(q_digit))

             # remove leading zeros

             q_str = ''.join(q).lstrip('0')

             if not q_str:

                 q_str = '0'

             return q_str, rem

         But wait, in our case, we have already checked that S is divisible by m. So the remainder should be zero. So the quotient_part_str is the result of S/m.

         So in code, after dividing, the remainder is zero, and the quotient is the quotient_part_str.

         But when S is a string like '99995', dividing by 7 gives '14285' with remainder zero.

         So the function returns the quotient as a string. But leading zeros may occur. For example, if S is 00123, but in our case S is a (p-1)-digit number with leading 9's. So S has no leading zeros. So the division of S by m will not have leading zeros except when S is 000...0 divided by m.

         But in our case, S is generated as (p-1) digits with the first (p-2) digits being 9's and the last digit being (10-x). So S is a non-zero number with no leading zeros.

         So the quotient_part_str is a number with (p-1 - log10(m)) digits, perhaps.

         Then, multiply by d (a digit). For example, '14285' multiplied by 7 is '99995'.

         Function to multiply a number string by a single digit:

         def multiply(s, d):

             res = []

             carry =0

             for ch in reversed(s):

                 num = int(ch)*d + carry

                 res.append( num%10 )

                 carry = num //10

             if carry >0:

                 res.append(carry)

             res_str = ''.join(map(str, reversed(res)))

             return res_str

         Then, divide by g (a small number). Again, we can use the division function.

         So, after dividing S by m to get quotient_part_str, then multiply by d to get temp_str, then divide temp_str by g to get a_str.

         But since the steps are derived from the equation, the division by g should have no remainder.

         So, for example, multiply quotient_part_str (14285) by d (7) → 99995. Then divide by g=7 → 14285.

         So the code steps would be:

         quotient_part_str = divide(S_str, m) → returns '14285'.

         temp_str = multiply(quotient_part_str, d) → '99995'.

         a_str = divide(temp_str, g) → '14285'.

         Then check if a_str has length (p-1) and no leading zeros.

         Once a_str is valid, then N_str is a_str + str(d). For example, a_str is '14285', d is 7 → '142857'.

         Now, the code must also handle the case where p=1. Let's see:

         For p=1, the number is a single digit d. Rotating gives the same number. So x must be 1, and the minimal number is 1. But in the input, if x is not 1, then output is impossible.

         So for p=1:

         if x !=1 → output impossible.

         else → minimal number is 1.

         So in code, handle p=1 as a special case.

         Putting it all together:

         The code will:

         Read p and x.

         If p ==1:

             if x ==1:

                 output '1'

             else:

                 output 'Impossible'

         Else:

             For each d from 1 to 9:

                 compute k =10x -1.

                 g = gcd(k, d).

                 m =k //g.

                 rem = pow(10, p-1, m)

                 if (rem -x) %m !=0 → skip.

                 else:

                     generate S_str as '9'*(p-2) + str(10 -x).

                     divide S_str by m → quotient_part_str.

                     multiply quotient_part_str by d → temp_str.

                     divide temp_str by g → a_str.

                     if len(a_str) == p-1 and a_str[0] != '0':

                         N_str = a_str + str(d)

                         return N_str (since we are checking in order of d from 1 to 9, and taking the first valid, which is the smallest possible)

             if no valid d found:

                 output 'Impossible'

         Now, the functions for division and multiplication need to be implemented.

         Also, for the case when S_str is empty (like p-1=0, which is p=1), but p=1 is handled as a special case.

         Let's implement the divide function:

         def divide(number_str, divisor):

             # returns the quotient as a string, and remainder.

             # assumes divisor is a positive integer.

             quotient = []
             carry =0

             for digit in number_str:

                 current = carry *10 + int(digit)
                 q = current // divisor
                 carry = current % divisor
                 quotient.append(str(q))

             # The quotient may have leading zeros. Need to remove them.

             quotient_str = ''.join(quotient).lstrip('0')

             if not quotient_str:  # all zeros
                 quotient_str = '0'

             return quotient_str, carry

         But since we know that S is divisible by m, the remainder is zero. So when we call divide(S_str, m), the remainder is zero.

         Similarly, when we call divide(temp_str, g), since a must be integer, the remainder is zero.

         So, in code, after dividing, we can assert that the remainder is zero.

         But in practice, we can proceed assuming that, because we have already checked the modular conditions.

         So for S_str division by m:

             quotient_part_str, rem = divide(S_str, m)

             assert rem ==0

         Similarly for temp_str divided by g.

         Now, let's test this logic with sample input 1:

         Sample input 1:

         p=6, x=5.

         p is not 1.

         For d=7:

             k=5*10-1=49.

             g = gcd(49,7)=7.

             m=49//7=7.

             rem = pow(10,5,7) → as computed earlier, 10^5 mod7 is 5. So rem=5.

             (rem -x) mod m → (5-5) mod7 →0. Condition satisfied.

             S_str is '9'*(6-1-1) + str(10-5) → '9'*4 + '5' → '99995'.

             divide '99995' by 7:

                 quotient is '14285', remainder 0.

             multiply by d=7: 14285 *7= 99995 → '99995'.

             divide by g=7: 99995 /7=14285 → '14285'.

             a_str is '14285' → len is 5 (p-1=5), no leading zeros.

             So N_str is '142857'.

         So the code would output this.

         Another sample input is 6 4:

         Output is 102564.

         Let's see:

         For d=4, perhaps?

         p=6, x=4.

         k=10*4-1=39.

         d=4.

         g = gcd(39,4)=1.

         m=39/1=39.

         rem = pow(10,5,39).

         10^5 mod39:

         10 mod39=10.

         10^2 mod39= (10*10)=100 mod39=100-2*39=22.

         10^3=10*22=220 mod39: 220-5*39=220-195=25.

         10^4=25*10=250 mod39: 250-6*39=250-234=16.

         10^5=16*10=160 mod39. 160-4*39=160-156=4. So rem=4.

         (rem -x) mod39 = (4-4) mod39=0 → condition satisfied.

         S_str is '9'*(6-2) + str(10-4) → '99996'.

         divide '99996' by 39 → 99996 /39 = 2564 → but let's compute:

         '9' '9' '9' '9' '6'

         division by 39:

         first digit:9 →9/39=0, carry 9.

         99 →99/39=2 (2*39=78, remainder 21).

         219 →219/39=5 (5*39=195, rem 24).

         249 →249/39=6 (6*39=234, rem15).

         156 →156/39=4 (rem0).

         So quotient_part_str is 02564 → stripped to 2564.

         multiply by d=4 →2564 *4=10256.

         divide by g=1 →10256. len is 5 (p-1=5), no leading zeros.

         N_str is 10256 + '4' →102564. Which matches the sample.

         So the code would generate this.

         Now, the code needs to handle large p, like p=1e6. For such cases, generating S_str as '9'*(p-2) + str(10-x) would create a very large string. However, in Python, creating such a string with 1e6-1 characters is possible, but may use a lot of memory. For example, a string of 1e6 characters is about 1MB (since each character is a byte in Python), which is manageable within memory constraints (256MB).

         But for p=1e6, the S_str is '9' repeated 999,998 times followed by 'something'. Creating such a string would take O(p) time and memory, but for Python, this is manageable.

         However, there's a smarter way to perform the division without generating the entire S_str. Because the S_str consists of (p-2) 9's followed by (10-x) as a digit.

         So, during the division, we can process the digits of S_str without explicitly creating the string. Because the digits are (p-2) 9's followed by (10-x). So, for example, we can generate the digits on the fly: first (p-2) digits are '9', then the last digit is (10-x).

         This way, we don't need to create a huge string, which would save memory for large p.

         So the division function can be modified to take into account that S is made of (p-2) '9's followed by a digit (10-x).

         This is a critical optimization for handling large p.

         So, the code can be adjusted as follows:

         When dividing S by m, instead of creating the entire S_str, we can generate the digits on the fly. For example:

         The first (p-2) digits are '9's, and the last digit is (10-x).

         So during the division process, for each digit in S:

             for i in range(p-2):

                 process '9'

             process (10-x) as a character.

         This way, even for p=1e6, the code doesn't need to allocate memory for the entire string. This will reduce memory usage significantly.

         Similarly, when multiplying quotient_part_str by d and then dividing by g, the quotient_part_str can be generated as a string, but for p=1e6, this would be a string of length up to (p-1) digits, which is 1e6 digits. This requires about 1MB of memory, which is manageable.

         But if p is 1e6, the quotient_part_str is obtained by dividing a (1e6-1)-digit S_str by m (which is small). The quotient_part_str would be of length (1e6-1) - log10(m) + ... but for m up to 89, log10(m) is about 2 digits. So quotient_part_str has about 1e6 digits. Storing such a string would use about 1e6 bytes (1MB), which is acceptable.

         So, the code can be optimized by generating S on the fly during the division step.

         Let's adjust the divide function to handle this case.

         So, the code for dividing S (without explicitly creating the string) would be:

         def divide_large(p_minus_1, last_digit, divisor):

             # p_minus_1 is the number of digits of S.

             # the first (p_minus_1 -1) digits are 9, followed by last_digit.

             # perform division of S by divisor.

             quotient = []
             carry =0

             # process the (p_minus_1 -1) 9's
             for _ in range(p_minus_1 -1):
                 current = carry *10 +9
                 q = current // divisor
                 carry = current % divisor
                 quotient.append(str(q))

             # process the last digit
             current = carry *10 + last_digit
             q = current // divisor
             carry = current % divisor
             quotient.append(str(q))

             quotient_str = ''.join(quotient).lstrip('0')
             if not quotient_str:
                 quotient_str = '0'
             return quotient_str, carry

         This function generates the quotient by processing each digit of S without explicitly creating the entire string.

         For example, when p=6 and x=5, p_minus_1=5, last_digit=5 (since 10-x=5). The first 4 digits are 9's, last digit is 5.

         So, the function processes 4 9's and then 5.

         So this function is O(p) time but O(p) space for the quotient_str. But for p=1e6, this is manageable.

         So, integrating this into the code:

         For each d in 1-9:

             ...

             # Generate S as a string: '9'*(p-2) + str(10-x). But for large p, generate on the fly.

             last_digit = 10 -x

             # p_minus_1 is (p-1)

             quotient_part_str, rem = divide_large(p_minus_1=p-1, last_digit=last_digit, divisor=m)

             if rem !=0 → skip (but according to earlier checks, this won't happen).

             then multiply quotient_part_str by d → temp_str.

             then divide temp_str by g → a_str.

             check a_str's length and leading zeros.

         So this approach is more memory-efficient.

         Now, the multiply function also needs to handle very large quotient_part_str (up to 1e6 digits). So the multiply function must be efficient.

         def multiply_large(number_str, d):

             # multiply a large number_str by a single digit d.

             res = []
             carry =0

             for ch in reversed(number_str):
                 num = int(ch) * d + carry
                 res.append(num %10)
                 carry = num //10

             if carry !=0:
                 res.append(carry)

             # reverse to get the correct order
             res.reverse()

             return ''.join(map(str, res)) if res else '0'

         This function is O(n) time, which is acceptable.

         Similarly, the divide function for temp_str by g can be done using the divide_large function, but temp_str is the result of multiply_large, which may have leading zeros. So in code:

         temp_str = multiply_large(quotient_part_str, d)

         a_str, rem = divide_large(temp_str, divisor=g) → but wait, no. temp_str is a string, and needs to be divided by g.

         So here, we need to divide a string temp_str by g. We can use the divide function that processes a string:

         def divide_string(number_str, divisor):

             quotient = []
             carry =0

             for digit in number_str:

                 current = carry *10 + int(digit)
                 q = current // divisor
                 carry = current % divisor
                 quotient.append(str(q))

             quotient_str = ''.join(quotient).lstrip('0')

             if not quotient_str:
                 quotient_str = '0'

             return quotient_str, carry

         So in code, after multiplying, we have temp_str, which is quotient_part_str *d.

         Then, divide temp_str by g using divide_string:

         a_str, rem = divide_string(temp_str, g)

         if rem !=0 → skip (but according to earlier conditions, this should not happen).

         Now, the code should handle all steps efficiently.

         Now, putting it all together.

         Also, note that when x >=10, but according to the input constraints, x is between 1 and 9.

         Now, handling p=1.

         For p=1:

             if x ==1:

                 output is '1' (since minimal possible is 1).

             else:

                 output 'Impossible'.

         Now, the code:

         So, let's write the code.

         First, handle p=1.

         Then, for p>=2:

             Iterate d from 1 to 9.

             For each d:

                 compute k=10x-1.

                 g=math.gcd(k,d).

                 m=k//g.

                 compute rem=pow(10, p-1, m).

                 if (rem -x) %m !=0 → skip.

                 else:

                     last_digit=10 -x.

                     quotient_part_str, rem = divide_large(p-1, last_digit, m).

                     assert rem ==0.

                     temp_str = multiply_large(quotient_part_str, d).

                     a_str, rem = divide_string(temp_str, g).

                     if rem !=0 → skip.

                     if len(a_str) == p-1 and a_str[0] != '0':

                         N_str = a_str + str(d)

                         print(N_str)

                         exit()

             after all d's:

                 print("Impossible")

         Now, let's test this code with sample inputs.

         Sample input 2: p=1, x=2 → output impossible.

         Sample input 1: p=6, x=5 → output 142857.

         Sample input 3: p=6, x=4 → output 102564.

         Now, code implementation.

         Also, the functions divide_large and multiply_large need to be implemented.

         But wait, in the code, divide_large is the function that processes the digits of S (the first p-1-1 9's and last digit 10-x), and returns the quotient_part_str.

         Now, the code in Python:

Testing against sample input 1.

```python
import sys
import math


def main(input_stream, output_stream):
    def divide_large(p_minus_1, last_digit, divisor):
        quotient = []
        carry = 0
        # Process (p_minus_1 -1) 9's
        for _ in range(p_minus_1 - 1):
            current = carry * 10 + 9
            q = current // divisor
            carry = current % divisor
            quotient.append(str(q))
        # Process last digit
        current = carry * 10 + last_digit
        q = current // divisor
        carry = current % divisor
        quotient.append(str(q))
        quotient_str = ''.join(quotient).lstrip('0')
        if not quotient_str:
            quotient_str = '0'
        return quotient_str, carry

    def multiply_large(number_str, d):
        res = []
        carry = 0
        for ch in reversed(number_str):
            num = int(ch) * d + carry
            res.append(num % 10)
            carry = num // 10
        if carry:
            res.append(carry)
        res_str = ''.join(map(str, reversed(res))) if res else '0'
        return res_str

    def divide_string(number_str, divisor):
        quotient = []
        carry = 0
        for ch in number_str:
            current = carry * 10 + int(ch)
            q = current // divisor
            carry = current % divisor
            quotient.append(str(q))
        quotient_str = ''.join(quotient).lstrip('0')
        if not quotient_str:
            quotient_str = '0'
        return quotient_str, carry

    p, x = map(int, input_stream.readline().split())

    if p == 1:
        if x == 1:
            print(1, file=output_stream)
        else:
            print("Impossible", file=output_stream)
        sys.exit()

    found = False
    min_n = None

    for d in range(1, 10):
        k = 10 * x - 1
        if k == 0:
            continue  # x=0, but x >=1 per problem constraints
        g = math.gcd(k, d)
        m = k // g
        # Compute 10^(p-1) mod m
        if m == 0:
            continue
        rem = pow(10, p-1, m)
        # Check if (rem -x) % m ==0
        if (rem - x) % m != 0:
            continue
        last_digit = 10 - x
        if last_digit < 0 or last_digit > 9:
            continue
        # Divide S by m
        quotient_part_str, rem = divide_large(p-1, last_digit, m)
        if rem !=0:
            continue  # shouldn't happen
        # Multiply by d
        temp_str = multiply_large(quotient_part_str, d)
        # Divide by g
        a_str, rem = divide_string(temp_str, g)
        if rem !=0:
            continue
        if len(a_str) != p-1 or a_str[0] == '0':
            continue
        # Found a candidate
        N_str = a_str + str(d)
        if not found or N_str < min_n:
            min_n = N_str
            found = True

    if found:
        print(min_n, file=output_stream)
    else:
        print("Impossible", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2
""",
            "output": \
"""\
Impossible
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

```

         Sample 3:

         Input 6 4.

         Output 102564.

         Let's see for d=4:

             k=10*4-1=39.

             g = gcd(39,4)=1 → m=39.

             rem=pow(10,5,39) → compute as before:

             But how?

             pow(10,5,39):

             Compute 10^5 mod39.

             10 mod39=10.

             10^2 mod39: (10*10)=100 mod39 →100-2*39=22.

             10^3 mod39: (22*10) mod39=220 mod39 →220-5*39=220-195=25.

             10^4 mod39: (25*10) mod39=250 mod39 →250-6*39=250-234=16.

             10^5 mod39: (16*10) mod39=160 mod39 →160-4*39=160-156=4.

             rem=4. (4-4) mod39=0 → condition satisfied.

             last_digit=10-4=6.

             divide_large(p-1=5, last_digit=6, divisor=39):

                 process 4 9's and last digit 6.

                 Initial carry=0.

                 first 9: current=9 →9//39=0 → append '0', carry=9.

                 second 9: current=9*10 +9=99 →99//39=2, rem 99-78=21 → append '2', carry=21.

                 third 9: current=21*10 +9=219 →219//39=5 (5*39=195), rem 24 → append '5', carry=24.

                 fourth 9: current=24*10 +9=249 →249//39=6 (6*39=234), rem 15 → append '6', carry=15.

                 last digit 6: current=15*10 +6=156 →156//39=4, rem 0 → append '4'.

                 quotient_part_str is '02564' → stripped to '2564'.

                 Wait, no. The quotient_part_str is the list ['0','2','5','6','4'], joined as '02564', which after lstrip('0') is '2564'.

             multiply by d=4 →2564 *4=10256 → temp_str is '10256'.

             divide by g=1 →10256 remains.

             a_str is '10256', length 5 (p-1=5), starts with 1.

             N_str is '10256'+'4' → '102564'.

             So this is a valid candidate.

             Since d=4 is checked before higher digits, this is the minimal.

         Thus, the code works for this case.

         Now, the code should handle large p efficiently.

         For example, p=1e6, x=5, d=7. The code will generate the required quotient_part_str and a_str.

         Now, for the code to be optimized, it's essential that the functions for division and multiplication are efficient. For large p, the divide_large function is O(p) time, which is manageable.

         Also, in Python, handling large strings is possible, but for p=1e6, the quotient_part_str is a string of around 1e6 digits, which is manageable as Python's string handling is efficient.

         Thus, this code should work within the time and memory constraints.
</think>

```python
import sys
import math

def divide_large(p_minus_1, last_digit, divisor):
    quotient = []
    carry = 0
    for _ in range(p_minus_1 - 1):
        current = carry * 10 + 9
        q = current // divisor
        carry = current % divisor
        quotient.append(str(q))
    current = carry * 10 + last_digit
    q = current // divisor
    carry = current % divisor
    quotient.append(str(q))
    quotient_str = ''.join(quotient).lstrip('0')
    if not quotient_str:
        quotient_str = '0'
    return quotient_str, carry

def multiply_large(number_str, d):
    res = []
    carry = 0
    for ch in reversed(number_str):
        num = int(ch) * d + carry
        res.append(num % 10)
        carry = num // 10
    if carry:
        res.append(carry)
    res_str = ''.join(map(str, reversed(res))) if res else '0'
    return res_str

def divide_string(number_str, divisor):
    quotient = []
    carry = 0
    for ch in number_str:
        current = carry * 10 + int(ch)
        q = current // divisor
        carry = current % divisor
        quotient.append(str(q))
    quotient_str = ''.join(quotient).lstrip('0')
    if not quotient_str:
        quotient_str = '0'
    return quotient_str, carry

p, x = map(int, sys.stdin.readline().split())

if p == 1:
    print(1 if x == 1 else "Impossible")
    sys.exit()

found = False
min_n = None

for d in range(1, 10):
    k = 10 * x - 1
    if k == 0:
        continue
    g = math.gcd(k, d)
    m = k // g
    if m == 0:
        continue
    rem = pow(10, p-1, m)
    if (rem - x) % m != 0:
        continue
    last_digit = 10 - x
    if not (0 <= last_digit <= 9):
        continue
    quotient_part_str, rem = divide_large(p-1, last_digit, m)
    if rem != 0:
        continue
    temp_str = multiply_large(quotient_part_str, d)
    a_str, rem = divide_string(temp_str, g)
    if rem != 0:
        continue
    if len(a_str) != p-1 or a_str[0] == '0':
        continue
    N_str = a_str + str(d)
    if not found or N_str < min_n:
        min_n = N_str
        found = True

print(min_n if found else "Impossible")
```
