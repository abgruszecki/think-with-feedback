<think>
Okay, let's tackle this problem. The task is to check if a given fraction p/q is equal to a continued fraction represented by a sequence of a_1 to a_n. 

First, I need to understand how to compute the value of the continued fraction. The continued fraction is built from the bottom up. For example, in the first sample, the fraction is 2 + 1/4. So starting from the last term (a_n), we compute each step. 

Wait, right. To evaluate the continued fraction, we start from the innermost part. Like, for a sequence [a1, a2, ..., an], the value is a1 + 1/(a2 + 1/(... + 1/(an)...)). So to compute this, we can start from the last element and work backwards. 

So for each step, the current value is a_i plus the reciprocal of the next step's value. But since we're working with fractions, we need to represent this as numerator and denominator to avoid floating point inaccuracies. 

So the approach would be to process the continued fraction from the end to the beginning. Let's think about how to compute this. Let's say after processing the i-th element, we have a fraction num/den. Then, for the (i-1)-th element a_prev, the next step would be a_prev + 1/(num/den) = (a_prev * num + den) / num. So the new numerator is a_prev * num + den, and the new denominator is num. 

Wait, let's make sure. Suppose the current fraction is x = num/den. Then the previous step is a_prev + 1/x. So that's a_prev + den/num = (a_prev * num + den)/num. So yes, the new numerator becomes a_prev * num + den, and denominator is num. 

So the algorithm is to initialize the current numerator and denominator as a_n and 1, then for each step moving backwards (from n-1 down to 1), set the new numerator as a_i * current_num + current_den, and the new denominator as current_num. Then, after processing all terms, compare the resulting numerator and denominator with p/q (simplified). 

But wait, the input p and q may not be in their simplest form. So first, we need to simplify p/q by dividing both by their greatest common divisor (gcd). Similarly, the computed continued fraction's numerator and denominator must be simplified. 

So the steps are:

1. Compute the continued fraction's value as a reduced fraction (num, den). 
2. Simplify the given p/q by dividing both by their gcd. 
3. Check if num/den equals the simplified p/q. 

But how to compute the continued fraction's value efficiently, especially considering that a_i can be up to 1e18, and n up to 90. 

Wait, for each step, the numerator and denominator can get very large. For example, each step involves multiplying a_i (up to 1e18) with the current numerator (which could be up to 1e18^90), leading to numbers way beyond Python's integer handling capacity. Wait, but Python can handle big integers, right? So even if the numbers are extremely large, Python can manage them. However, the computation time might be an issue. But since n is up to 90, and each step is O(1) operations (even if those operations are on very large numbers), it's manageable. 

So the plan is:

- Start with the last a_i. So the initial numerator is a_n, denominator is 1. 
- For each i from n-1 down to 1:
   new_numerator = a_i * current_num + current_den
   new_denominator = current_num
   Then, set current_num and current_den to new_numerator and new_denominator. 
   Also, after each step, we can compute the gcd of new_numerator and new_denominator and divide both by that to keep the numbers as small as possible. Otherwise, the numbers could become extremely large, leading to slow operations. 

Wait, but simplifying after each step is crucial here. Because if we don't, the numbers can explode exponentially. For example, each step could multiply by 1e18, leading to 1e18^90, which is way beyond anything. But even Python can't handle that efficiently. So we need to reduce the numerator and denominator after each step to their simplest form. 

Yes. Because even if a_i is 1e18, if we add 1/(previous step), and each step is reduced, the numbers can be manageable. Let's see. 

So, the correct approach is to compute the continued fraction step by step, simplifying at each step. 

So let's model this. 

Initialize num = a_n, den = 1. Then, for each i from n-1 downto 1:

   next_num = a_i * num + den
   next_den = num
   Then, compute the gcd of next_num and next_den. 
   num, den = next_num // gcd, next_den // gcd

Then, after processing all a's, we have the numerator and denominator of the continued fraction. 

Compare this num/den with the given p/q, which should be simplified. 

So the steps for the code:

1. Read p, q. Compute the gcd of p and q, then simplify p and q by dividing by this gcd. 

2. Read n and the list a. 

   If n is 0, but according to the problem statement, n is at least 1. So no need to handle that. 

3. Check if the length of a is n. If not, it's a problem. But the input is given correctly, per the problem statement. 

4. Compute the continued fraction. 

   Start with num = a[-1], den = 1. 

   For each a_i in reversed(a[:-1]):

      next_num = a_i * num + den
      next_den = num 

      g = gcd(next_num, next_den)
      num, den = next_num // g, next_den // g

5. After all steps, compare the computed (num, den) with the simplified (p, q). 

   If equal, output YES. Else, NO. 

But wait, what if during the computation, the continued fraction's denominator becomes zero? But since all a_i are at least 1, each step's denominator (next_den) is the previous numerator. Since the initial num is a_n (>=1), then next_den (from the next step) is a_i * num + den. Wait no, in the first step (for a_{n-1}), next_num is a_{n-1} * a_n + 1, and next_den is a_n. So denominators are at least 1, and thus, no division by zero. 

So that's safe. 

Now, the challenge is to compute the gcd efficiently. Since Python's built-in math.gcd function works for non-negative integers, but returns a positive integer. However, since all denominators and numerators are positive (since a_i is positive and all steps involve addition and multiplication of positive numbers), we don't have to worry about negative values. 

Wait, but when we compute next_num and next_den, they are positive. Because a_i is at least 1, num and den are positive (since they start as 1 and a_n, which is >=1). So yes. 

So, for each step, after computing next_num and next_den, we can compute their gcd and reduce. 

But how to compute the gcd of two very large numbers? Python's math.gcd uses an efficient algorithm, but for very large numbers (like 1e18^90?), even that could be slow. However, given that n is up to 90, and each step reduces the numbers by their gcd, this approach should be manageable. 

Wait, let's take an example. Suppose all a_i are 1. Then the continued fraction becomes 1 + 1/(1 + 1/(1 + ... )). For n steps, the fraction is the n-th Fibonacci number divided by the (n-1)-th. But each step's reduction would keep the numerator and denominator as Fibonacci numbers, which are coprime. So the gcd is 1 each time. So in that case, the numbers would grow exponentially (like Fibonacci numbers), but since Python can handle big integers, even for 90 steps, it's manageable. 

But for a_i being 1e18, then each step would multiply by 1e18 and add. Let's see for the first few steps. Let's say n=90. The last step is a_90, which is 1e18. Then a_89 is 1e18. So next_num is 1e18 * 1e18 + 1 (since den is 1). That's 1e36 + 1. The denominator is 1e18. The gcd of 1e36 +1 and 1e18 is ... since 1e36 +1 and 1e18 share a gcd of 1 (since 1e18 is even, but 1e36+1 is odd). So the gcd is 1. So next_num is 1e36+1, next_den is 1e18. Then for a_88=1e18, the next_num would be 1e18 * (1e36 +1) + 1e18 = 1e18*(1e36 +1 +1) = 1e18*(1e36+2). The denominator is 1e36 +1. Then compute the gcd of 1e18*(1e36+2) and 1e36 +1. Since 1e36+2 and 1e36+1 are consecutive numbers (difference 1), their gcd is 1. So again, the gcd is 1. So each step's numbers are getting multiplied by 1e18, leading to very large numbers. For 90 steps, the numbers would be on the order of (1e18)^90, which is way beyond even Python's ability to handle efficiently. 

Wait, but 1e18^90 is 1e1620. Python can handle integers that big, but operations on them would be very slow. For example, adding two numbers of that size would take O(1) time for the digits, which is 1e1620 digits. That's impossible. So for n=90, this approach would not be feasible because the numbers would become way too big, leading to timeouts. 

So the problem is that, even with reducing the fractions after each step, when a_i's are large (like 1e18), the numerator and denominator can become extremely large, leading to each step taking a lot of time. 

Hmm. So the approach of computing the continued fraction by reducing after each step may not be feasible for n=90 and a_i=1e18. 

But wait, the constraints on n is 90, and each a_i can be up to 1e18. So how can we handle that? Because even after reducing, the numbers could be as large as 1e18^90. Which is impossible to handle. 

Wait, but the problem says to compare the resulting fraction with p/q. So maybe there's a smarter way to compute this without having to compute the entire fraction. Like, perhaps using the fact that the continued fraction can be built incrementally, and at each step, check if the intermediate fractions match p/q. But I don't see how that would work. 

Alternatively, perhaps there's a way to model this as a continued fraction and compute the convergents, but even then, the numbers could be very large. 

Alternatively, perhaps we can model the process in reverse, starting from p/q, and seeing if it can be decomposed into a continued fraction that matches the given a_i sequence. 

This approach is similar to the way we convert a fraction into a continued fraction. Let's think about that. 

The standard algorithm for converting a fraction into a continued fraction is to take the integer part as a_1, then invert the remaining fractional part, and repeat. 

For example, to convert 9/4 into a continued fraction:

9/4 = 2 + 1/ (4/1) → a1=2, then 4/1 is 4, so a2=4. So the continued fraction is [2,4]. Which matches the first sample. 

In the second sample, 9/4 is [2, 3, 1]. Let's see:

Wait, 9/4 is 2 + 1/ (4/1). But how does that become [2,3,1]? Oh, no. Wait, the second sample's continued fraction is 2 + 1/(3 + 1/1) = 2 + 1/4 = 9/4. So how is the continued fraction [2,3,1]? Because when you write 9/4 as a continued fraction, the algorithm would take a1=2 (since 2 is the integer part of 9/4). Then the remainder is 1/4. Then invert to get 4, which is a2=4. So [2,4]. But the sample input has [2,3,1]. Hmm. So there's a discrepancy here. 

Wait, but the continued fraction representation is not unique. For example, the continued fraction can end with a 1. For example, 4 can be written as 3 + 1/1. So the algorithm gives [2,4], but another representation is [2,3,1]. So the problem allows any representation that equals the given fraction, but the input's a_i sequence is given, and we have to check if that specific sequence evaluates to p/q. 

So for the problem, we have to compute the exact value of the given a_i sequence and compare it to p/q. 

But back to the idea of converting p/q into a continued fraction and then checking if it matches the given a_i sequence. However, the given a_i sequence may have a different form than the standard continued fraction. For example, the first sample's [2,4] versus the second sample's [2,3,1]. So even if the value is the same, the sequence can vary. 

So that approach is not directly applicable. 

So perhaps the original approach of computing the continued fraction's value is the only way. But how to handle the big numbers. 

Wait, but even if we don't simplify the fractions after each step, the problem is that the numbers can get too big. Let's see. For each step, the numerator and denominator can be stored as pairs. But with a_i up to 1e18 and n up to 90, the numbers could be up to 1e18^90, which is way beyond even Python's ability to handle in a reasonable time. For example, even for 90 steps, multiplying a 1e18 each step would lead to 1e18^90, which is 1 followed by 1620 zeros. That's a number with 1620 digits. Operations on such numbers would take O(digits) time, which for 1e3 digits is manageable, but 1e3 is 1000, but 1e1620 is way beyond. So for 90 steps, the time would be way beyond the 2-second limit. 

So, this approach of building the fraction step-by-step and simplifying each time is the only way. Because simplifying the fractions after each step reduces the size of the numerator and denominator. For example, if after each step the gcd is 1, then the numbers are as small as possible, but even then, for some sequences, they can still get very large. 

But how can we compute the gcd of two very large numbers efficiently? 

Python's built-in math.gcd function is implemented in C and uses the Euclidean algorithm, which is O(log min(a,b)) steps. Each step involves modulus operations. But for numbers as large as 1e1000, even the modulus operation would take O(1) time, but with a very large constant. 

Wait, but in practice, for numbers up to 1e18, the Euclidean algorithm is very fast. But for numbers with 1e1000 digits, the modulus operations would take longer. However, in Python, big integers are stored as arrays of digits, and modulus operations are O(n) where n is the number of digits. So for a number with 1e3 digits, modulus is manageable, but for 1e1000 digits, it's O(1e3) steps, which is okay. But for numbers with 1e1620 digits, even a single modulus operation would take 1e1620 steps, which is impossible. 

So this approach is only feasible if the simplification after each step keeps the numbers manageable. 

But how can that be? For example, if all a_i are 1, then each step's numerator and denominator are Fibonacci numbers. The 90th Fibonacci number is about 2.8e18, which is manageable. So for that case, the numbers are manageable. But if a_i are 1e18, then after each step, the numbers could be multiplied by 1e18 each step, leading to 1e18^90, which is way too big. 

So the problem is that for some test cases, the numbers become so large that even the gcd computation becomes impossible within the time constraints. 

But given the constraints on n being up to 90, and the time limit of 2 seconds per test case, perhaps the approach is still feasible. 

Alternatively, perhaps there's a mathematical insight that allows us to avoid handling big numbers. 

Let me think differently. The continued fraction can be represented as a sequence of operations. Each step adds a_i and then takes reciprocal. But the order is reversed. 

But perhaps we can model the computation using pairs (numerator, denominator) and process each a_i in reverse order. 

Wait, the way to compute the continued fraction is:

The value is a1 + 1/(a2 + 1/(a3 + ... + 1/(a_n) ... )). 

So when processing in reverse order, we start from a_n, then each step i (from n-1 down to 1) adds a_i and inverts. 

But inversion is part of the process. 

Alternatively, perhaps we can model the process as a continued fraction in reverse. Let's see:

Let me think about the steps. For example, in the first sample:

a1=2, a2=4. 

Start with a2: 4 → 4/1. 

Then a1: 2 + 1/(4/1) = (2*4 +1)/4 = 9/4. 

So each step is a_i + 1/(prev_value). 

But this is equivalent to (a_i * prev_numerator + prev_denominator) / prev_numerator. 

So when processing a_i, the new numerator is a_i * prev_numerator + prev_denominator, new denominator is prev_numerator. 

So each step's numerator and denominator are determined by the previous. 

The key is that after each step, we can compute the gcd of the new numerator and denominator and reduce them. 

But when a_i is 1e18, and after processing, the new numerator is 1e18 * prev_num + prev_den. 

If prev_num and prev_den are, say, 1 and 1 (after some steps), then the new numerator is 1e18 * 1 +1 = 1e18 +1, denominator 1. 

But when processing another a_i=1e18, the new numerator is 1e18 * (1e18 +1) +1 → 1e18*(1e18+1) +1. 

But even with reducing, if the gcd of the new numerator and denominator is 1 (since 1e18*(1e18+1) +1 and 1e18+1 may have a gcd. Let's see: 

Denominator is 1e18+1. 

New numerator is (1e18 * (1e18+1)) + 1. 

= (1e36 +1e18) +1 = 1e36 +1e18 +1. 

The denominator is 1e18+1. 

We need to find the gcd of these two numbers. 

But 1e36 +1e18 +1 divided by 1e18+1. Let's see: 

Let x = 1e18. Then the denominator is x+1. 

Numerator is x² + x + 1. 

x² + x + 1 divided by x+1: 

x² +x +1 = (x+1)(x) + 1. So remainder is 1. 

So gcd(denominator, remainder) is gcd(x+1, 1) = 1. 

So the new fraction is (x² +x +1) / (x+1), which can't be reduced. So even after reduction, the numbers are x² +x +1 and x+1. For x=1e18, this is 1e36 +1e18 +1 and 1e18+1. 

So after two steps, the numbers are already 1e36, which is manageable in Python. 

But with 90 steps, each step multiplying by 1e18, the numbers would be 1e18^90, which is 1e1620. That's a huge number. 

So for n=90 steps, each a_i=1e18, the numbers would have 1e1620 digits. Which is impossible to handle. So even if Python can handle big integers, processing such large numbers would take way too much time. 

So the problem is that for certain test cases, this approach would be too slow. 

But the problem statement allows a_i up to 1e18 and n up to 90. So how can we manage this? 

Wait, but maybe there's a way to represent the numerator and denominator as fractions in a way that avoids dealing with the entire numbers. 

Alternatively, perhaps we can perform the comparison without computing the full fraction. 

Let's think: the problem is to check if the continued fraction equals p/q. 

We can model this by working backwards. 

Let me think: 

Suppose after processing all a_i, the result is x = num/den. We need to check if num/den equals p/q. 

But p and q can be simplified. So first, we can simplify p and q by dividing by their gcd. 

Then, we need to check if num * q == den * p. 

But how can we compute this equation without computing num and den explicitly? 

Because in some cases, num and den are very large. 

But the problem is that the continued fraction's value is x = num/den. So we need to find if x equals p/q. 

But x can be computed step by step, and at each step, it's possible that the intermediate fractions could be compared with p/q. However, since the steps are cumulative, this might not be feasible. 

Alternatively, perhaps we can model the problem using matrix multiplication. Each step of the continued fraction can be represented as a matrix. 

For example, the continued fraction can be represented as a series of steps. Let me see: 

The value of the continued fraction is a1 + 1/(a2 + 1/(a3 + ... )). 

Alternatively, we can model this as a sequence of matrices. 

Each step a_i can be represented by a matrix [[a_i, 1], [1, 0]]. The product of these matrices gives the continued fraction. 

Wait, perhaps the continued fraction can be represented as the product of matrices. 

For example, the continued fraction [a1, a2, a3] can be written as a1 + 1/(a2 +1/(a3)). 

This can be represented as the product of matrices: 

M = M(a1) * M(a2) * M(a3), where each M(ai) is [[ai, 1], [1, 0]]. 

Then, the resulting fraction is (M[0][0], M[1][0]). 

Wait, let's see. 

Let me compute for the first sample [2,4]. 

M1 = [[2,1], [1,0]]
M2 = [[4,1], [1,0]]
Product M1 * M2 = [[2*4 +1*1, 2*1 +1*0], [1*4 +0*1, 1*1 +0*0]] → [[9,2], [4,1]]. 

The resulting fraction is (9,4), which matches the sample. 

Another example: [2,3,1]. 

M1 = [[2,1], [1,0]]
M2 = [[3,1], [1,0]]
M3 = [[1,1], [1,0]]
Product M1 * M2 * M3: 

First compute M2*M3: 

[[3*1 +1*1, 3*1 +1*0], [1*1 +0*1, 1*1 +0*0]] → [[4,3], [1,1]]. 

Then M1 * that: 

[[2*4 +1*1, 2*3 +1*1], [1*4 +0*1, 1*3 +0*1]] → [[9,7], [4,3]]. 

So the resulting fraction is 9/4. 

Yes. 

So the product of the matrices gives us a numerator and denominator. The numerator is the top-left element divided by the bottom-left element. Wait, no. Wait, the product matrix M will have the numerator as M[0][0] and denominator as M[1][0]. Because when the product is [[n, ...], [d, ...]], then the value is n/d. 

So in the first sample, the product is [[9, 2], [4, 1]], so the value is 9/4. 

So the matrix approach is valid. 

But the problem is that each matrix multiplication can be represented as a pair of numerator and denominator. 

But the matrix elements can be very large. 

But perhaps we can represent each matrix as a pair of fractions. 

Wait, but matrix multiplication involves multiplying and adding terms. 

Alternatively, perhaps we can compute the numerator and denominator as pairs (n, d) and (n', d'), but this may not help. 

Alternatively, perhaps we can perform the matrix multiplication in a way that tracks the numerator and denominator of the current fraction, and simplifies them at each step. 

But this seems similar to the previous approach. 

So back to the matrix approach. Each step's matrix is [[a_i, 1], [1, 0]]. 

The product of the matrices from a1 to an is a matrix [[A, B], [C, D]], where the resulting fraction is A/C (assuming C is not zero). 

But how to compute this product efficiently. 

But even with matrices, the elements can become very large. So this approach may not help. 

So, perhaps the only way is to proceed with the initial approach but with the following optimizations:

- After each step, compute the gcd of the new numerator and denominator and divide them by it. This will keep the numbers as small as possible. 

But even then, for certain test cases, the numbers will be too big, leading to slow computations. 

But given the constraints, perhaps it's manageable. Let's think. 

For each of the 90 steps, we have to perform:

num = a_i * prev_num + prev_den 

den = prev_num 

Then compute the gcd of num and den. 

Even if the numbers are large, the gcd is computed using the Euclidean algorithm, which is O(log min(num, den)) steps. But if the numbers are very large, each step could take a lot of time. 

But perhaps in practice, Python can handle this. Let's see. 

For example, in the worst case where a_i is 1e18 and each step's gcd is 1. 

But for n=90, each step:

num = 1e18 * prev_num + prev_den 

den = prev_num 

Assuming that after each step, the numbers are not reduced (since gcd is 1), then after 90 steps, the num would be on the order of (1e18)^90. 

But even with Python's big integers, multiplying 1e18 with a number of 1e18^89 digits would take O(1e18^89) time, which is impossible. 

So this approach is not feasible for such cases. 

Thus, there's a problem. 

But the problem has the time limit of 2 seconds. So we need to find a way to compute this efficiently. 

Alternative idea: the continued fraction is built from the end. So perhaps we can model the computation using a pair of numerator and denominator as fractions, but instead of storing them as separate integers, we can represent them as a pair of coprime integers, and keep track of them in reverse order. 

But I'm not sure. 

Alternatively, perhaps we can compute the continued fraction in reverse order, using the given a_i, and check if at any step the fraction equals p/q. But that seems unlikely. 

Another idea: perhaps we can compare the fractions during the computation and bail out early if possible. But how?

For example, if during the computation, the current fraction exceeds p/q, then we can return NO. But continued fractions can oscillate around the true value, so this might not work. 

Alternatively, if the fractions become larger than p/q, but it's possible that subsequent steps could bring it back. 

So this seems not feasible. 

Hmm. 

Alternative approach: given that the problem is to compare two fractions, perhaps we can compute the continued fraction as a fraction and then compare cross products. 

But the problem is the cross products could be very large. 

But perhaps we can use modular arithmetic to check if the cross products are equal modulo several primes. But this is a probabilistic approach and could lead to false positives. 

The problem requires an exact check, so this approach isn't suitable. 

So, back to the original approach. 

But how to handle the very large numbers? 

Wait, let's think again about the process. For each step i from n-1 downto 1, the current num and den are used to compute the next step. 

But the way num and den are computed is:

new_num = a_i * num + den 

new_den = num 

But after this, we reduce new_num and new_den by their gcd. 

So, the key is that after each step, the new_num and new_den are coprime. 

But even if they are coprime, they can be very large. 

So, the code would have to handle very large numbers, which could be time-consuming. 

But perhaps the problem has constraints that the answer is NO in most cases, and we can find a way to exit early. 

For example, during the computation, if at any step the denominator becomes larger than q (after reducing), then perhaps the final denominator will be larger than q, leading to a NO. 

But this isn't necessarily the case, because subsequent steps can invert the fraction. 

For example, let's say after some step, the denominator is 1e20, but then the next step a_i is 1, leading to new_num = 1 * 1e20 +1 (denominator is 1e20). Then the new_num/denominator is (1e20+1)/1e20, which is 1 + 1e-20. Then the next step could multiply by a very large a_i. 

So this line of thought isn't helpful. 

Alternative idea: the problem allows the a_i to be up to 1e18, but the simplified p and q can be up to 1e18. So perhaps, during the computation of the continued fraction, if the current num or den exceeds p or q by a certain amount, then the final fraction can't equal p/q. 

But how to determine that? 

For example, if after some steps, the current denominator is already larger than q, and the subsequent steps multiply by a_i (which is at least 1), then the denominator can only increase. So in that case, the final denominator will be larger than q, and since q is part of the simplified fraction, the comparison would fail. 

But this is only true if the current denominator is larger than q and subsequent steps can't decrease it. 

But in the continued fraction computation, each step's new denominator is the current num (from the previous step). 

So, the denominator in each step is the num of the previous step. 

So, if during the computation, the denominator becomes larger than q, but the new a_i is 1e18, then the new num is a_i * num + den, which is very large, leading to a new denominator (current num) which is even larger. 

So, once the denominator exceeds q, and given that all a_i are at least 1, the denominator will keep increasing. So if the current denominator is already larger than q, then the final denominator will be larger than q, and thus the fraction can't be equal to p/q. 

Thus, during the computation, if at any step the denominator (after reduction) becomes larger than q, we can immediately return NO. 

Similarly, if the numerator exceeds p, but this depends on the a_i and steps. 

This could allow us to exit early in some cases. 

So, this is a possible optimization. 

So, the steps would be:

While processing the a_i in reverse order:

   compute new_num and new_den 

   reduce new_num and new_den by their gcd 

   check if new_den > q → if yes, output NO 

   else, proceed 

This way, in cases where the denominator exceeds q early, the code can exit early. 

But this depends on the a_i and the current p and q. 

For example, if the continued fraction's denominator after some steps is larger than q, then the code can return NO. 

But this is only valid if the denominator can't decrease in subsequent steps. 

Wait, but in the continued fraction computation, each step's denominator is the previous step's numerator. 

So, the denominator in step i is the new_den, which is equal to the previous step's num. 

So, if in step i, new_den is greater than q, then in the next step i-1, the denominator will be new_num (from step i), which is a_i * num + den. Since a_i is at least 1, and num and den are positive, new_num will be at least num + den. 

But if new_den is already greater than q, then in the next step, the denominator (new_num) will be larger than new_den, which was larger than q. So the denominator will keep increasing. 

Thus, once the denominator exceeds q in any step, the final denominator will be larger than q, leading to a NO. 

So, this is a valid optimization. 

Similarly, if during the computation, the numerator exceeds p (after reduction) and the denominator is not exceeding q yet, but the fraction is larger than p/q, then the final fraction will be larger than p/q, leading to a NO. 

But how to check this? 

For example, after step i, the current fraction is num/den. If this is larger than p/q, then in the next steps, adding a positive value (a_{i-1} etc.) will only increase the fraction. So the final fraction will be even larger than p/q. 

Wait, but the steps are computed in reverse. Let's think: 

The continued fraction is built from the end towards the beginning. So each step adds a_i to the reciprocal of the current fraction. 

So, during the processing (in reverse order), the current fraction is the value of the sub-fraction starting from a_i to a_n. 

As we process each a_i from the end, the value of the fraction increases with each a_i. 

For example, processing a_i = x makes the current fraction x + 1/(prev_fraction). So the larger x is, the larger the current fraction. 

So, during the computation in reverse, each step's a_i increases the current fraction. 

So, during the processing, the current fraction is the value of the continued fraction from a_i to a_n. 

So, as we process a_i from n-1 down to 1, the current fraction increases. 

Thus, if at any step, the current fraction exceeds p/q, then adding a_{i-1} (which is at least 1) will make the next fraction even larger. 

So, once the current fraction is larger than p/q, we can output NO. 

Similarly, if during the processing, the current fraction is less than p/q, then adding a_{i-1} (which is at least 1) will increase the current fraction. So there's a possibility that it could reach p/q. 

But this is not necessarily the case, but it's possible. 

But in the case where the current fraction is less than p/q, but after adding a_{i-1}, it could overshoot or not. 

But this seems like a possible optimization. 

So the plan is:

During each step of the continued fraction computation, after simplifying:

- If current den > q: output NO 

- Else, compute the cross product of current fraction and p/q. 

   If num * q > den * p: then even adding a_{i-1} (which is at least 1) will make the next fraction larger. So since a_{i-1} >=1, the next fraction is current a_i + 1/current_fraction. 

Wait, no. Because during the processing in reverse, each step adds a_i to the reciprocal of the previous fraction. 

Wait, perhaps I'm getting confused. Let's think again. 

Let me think of the steps again. 

We start from a_n: which is a_n/1. 

Then, for a_{n-1}, the new fraction is a_{n-1} + 1/(a_n/1) = (a_{n-1} * a_n +1) / a_n. 

Then for a_{n-2}, the new fraction is a_{n-2} + 1/(prev_fraction). 

So each step increases the current fraction. 

Because adding a positive number (a_{n-2} >=1) to 1/(prev_fraction) increases the value. 

So the current fraction is a_{i} + 1/(prev_fraction). 

So, during the processing (from the end), each step adds a_i (>=1) to the reciprocal of the previous fraction. 

But the reciprocal of the previous fraction is 1/(prev_fraction), which is a positive number. 

So, each step's current fraction is larger than a_i, which is >=1. 

So, as we process each a_i, the current fraction grows. 

So, during the processing, once the current fraction exceeds p/q, any further steps will only increase it. So the answer would be NO. 

Similarly, if during processing, the current fraction is equal to p/q, but there are still more steps (a_i's) to process, then adding a_i's will increase the current fraction beyond p/q. So, the answer would be NO. 

Thus, the only case when the answer is YES is when after processing all a_i's, the current fraction equals p/q. 

Thus, during the computation, if at any step the current fraction exceeds p/q, we can return NO immediately. 

Also, if after processing all steps, the current fraction is not equal to p/q, return NO. 

So, this is another optimization. 

Thus, during the computation, after each step, we can check:

- If den > q → return NO 

- Else, check if current fraction (num/den) is equal to p/q. If yes, but there are steps remaining → no, because the steps continue. 

Wait, no. Because the steps are processed in reverse order. For example, if the current fraction after processing a_i to a_n is equal to p/q, but there are i-1 more steps to process, then adding those steps will increase the fraction. 

So, the current fraction can only be equal to p/q after processing all steps. 

Thus, during the processing, even if the current fraction equals p/q, but there are more steps to process, we must continue. 

But during processing, the current fraction is the value of the continued fraction from a_i to a_n. So, if the code is processing a_i (from the end), and after processing a_2, the current fraction equals p/q, but then there is a_1 to process, which will add a_1 to the reciprocal of the current fraction. So the final fraction will be a_1 + 1/(current fraction) = a_1 + den/(num), which is (a_1 * num + den) / num. 

So, the only time when the current fraction equals p/q is after processing all a_i's. 

Thus, during the computation, we can't return YES early. 

But during the processing, we can check if the current fraction exceeds p/q. If so, return NO. 

Thus, the optimized steps are:

For each step in the continued fraction computation:

   compute new_num and new_den 

   reduce them by gcd 

   if new_den > q → output NO 

   else, check if new_num * q > new_den * p → if yes, output NO 

   else, proceed 

This way, if the current fraction is already larger than p/q, we can return NO immediately. 

But how to check if new_num * q > new_den * p? 

Because new_num and new_den can be very large, multiplying them by q and p respectively could lead to very large numbers. 

But in Python, even if the numbers are very large, comparisons are efficient. 

So, for example, comparing 1e1000 and 1e999 is done by looking at the length of the numbers first, so it's O(1). 

Thus, comparing new_num * q > new_den * p can be done efficiently, even for very large numbers. 

So, the steps during processing each a_i would be:

   compute new_num and new_den 

   compute g = gcd(new_num, new_den) 

   new_num //= g 

   new_den //= g 

   if new_den > q: 

      return NO 

   if new_num * q > new_den * p: 

      return NO 

   else: 

      proceed to next step 

This can save us from processing many steps in cases where the fraction becomes larger than p/q. 

Let's test this idea with the first sample:

p=9, q=4 (simplified). 

Processing the a_i [2,4], n=2. 

Step 1: a_n is 4 → num=4, den=1. 

Check den=1 <=4 → ok. 

Check 4 *4 =16, 1 *9=9 → 16>9 → 4/1 >9/4. So return NO? 

But this is incorrect. Because after this step, there is another a_i=2 to process. 

Wait, no. Because the steps are processed from the end. So in the first sample, the steps are:

Processing a2=4 (n=2). 

Then processing a1=2. 

So the steps are:

Initial step: a=4 → num=4, den=1. 

Check den=1 <=4 → yes. 

Check 4 *4 (q=4) → 4*4=16; den*p is 1*9=9. So 16>9 → condition new_num*q > new_den*p → 16>9 is true. So return NO. 

But this is wrong, because after processing a1=2, the fraction becomes 9/4. 

But according to the code, after processing a2=4 (which is the first step in reverse order), the current fraction is 4/1, which is 4. Since 4>9/4 (2.25), the code would return NO immediately, which is incorrect. 

Ah! So this optimization is flawed. 

Because during the processing in reverse order, the steps are a_n, a_{n-1}, ... a1. 

Thus, the initial step is a_n, and each step adds a_i (which is a_{n-1}, a_{n-2}, etc.) to the reciprocal of the previous fraction. 

Thus, the first step's fraction is a_n/1. 

Then, processing a_{n-1} gives (a_{n-1}*a_n +1)/a_n. 

Then, processing a_{n-2} gives (a_{n-2} * (a_{n-1}*a_n +1) + a_n) / (a_{n-1}*a_n +1). 

So the code processes a_i in reverse order, starting from a_n, then a_{n-1}, etc. 

But in the first sample, the a_i are [2,4], n=2. So the steps are:

Step 1: a=4 → num=4, den=1. 

Check den=1 <=4 → yes. 

Check 4*4=16 > 1*9=9 → yes. So returns NO. But this is wrong. 

So the optimization is incorrect. 

Thus, this approach of checking if the current fraction is larger than p/q is not valid. 

So why is this? 

Because the current fraction is the value of the continued fraction from a_i to a_n. 

Thus, during processing, the current fraction is part of the entire continued fraction. 

But the steps are building the continued fraction from the end. So each step adds a new a_i to the beginning of the continued fraction. 

Thus, the current fraction after processing a_i is the value of the continued fraction starting at a_i and ending at a_n. 

Thus, the current fraction is not the entire continued fraction until all steps are processed. 

But the optimization checks if the current fraction is larger than p/q, but that current fraction is part of the entire continued fraction, not the entire one. 

Thus, this optimization is incorrect. 

So, this idea is not valid. 

Thus, we have to process all steps, and only at the end compare the current fraction with p/q. 

Thus, we have to find another way to handle large numbers. 

But how? 

Alternative idea: use the fact that after each step, the new_num and new_den are a_i * num + den and num. 

But when computing new_num and new_den, even if they are very large, but after simplification, they could be manageable. 

But for some cases, like a_i=1e18 and n=90, even after simplifying, the numbers would be 1e18^90, which is impossible to handle. 

So, perhaps this problem is designed such that the maximum possible numbers after simplification are manageable. 

But how? 

For example, even with a_i=1e18 and n=90, after each step's simplification, if the gcd is 1, the numbers would be 1e18, 1e18+1, ... but this depends on the sequence. 

Alternatively, perhaps the problem is designed with the assumption that the code will process all steps and handle the large numbers, and that Python's big integers can handle it within the time constraints. 

But in practice, for 90 steps, each involving multiplying a_i (1e18) with the current numerator (which could be 1e18^k), and adding the denominator (1e18^(k-1)), this leads to numbers that are 1e18^90. But even for k=90, that's 1e18^90, which is a number with 90 * 18 = 1620 zeros. 

But in Python, even with such large numbers, multiplying and adding takes time. For example, adding two numbers of 1e3 digits takes O(1e3) time. For 1e1620 digits, it's O(1e1620) time, which is way beyond the time limit. 

Thus, the code would not pass the time constraints for such test cases. 

But the problem's constraints allow a time limit of 2 seconds. So for Python, which is relatively slow, we need to find a way to handle this. 

But how? 

Ah! Perhaps the key is that the continued fraction can be represented as a fraction in its simplest form, and when comparing to p/q, the cross product (num * q) must equal (den * p). 

But even if the numbers are large, comparing the cross products (num * q vs den * p) is possible in Python, but the multiplication could take a lot of time. 

Thus, the code must compute num and den after all steps, then check if num * q == den * p. 

But for very large numbers, this multiplication is impossible. 

Thus, this approach is not feasible. 

Alternative idea: 

The problem requires that the continued fraction equals p/q. 

So, after processing all steps, the final num and den must be such that num * q == den * p. 

But p and q are up to 1e18. 

If the final num and den are such that num / den = p / q → num * q = den * p. 

But if the numbers are very large, but p and q are up to 1e18, then perhaps we can compute the remainder of num * q - den * p. 

But even this may not help. 

Alternative approach: 

The continued fraction can be computed step by step, and each step's new_num and new_den can be represented in terms of p and q. 

But I don't see how that helps. 

Another idea: since we need to check if the continued fraction equals p/q, perhaps during the computation, we can track the value as a fraction and reduce it modulo some number. But this is a probabilistic approach and may not give an exact answer. 

But the problem requires an exact answer. 

So, this approach is not suitable. 

At this point, it seems that the only feasible way is to proceed with the initial approach, compute the continued fraction step by step, reduce after each step, and hope that the numbers stay manageable. 

But how to handle the cases where the numbers are very large. 

Wait, but in Python, even if the numbers are very large, as long as the steps are O(n) where n is 90, and each step involves a few arithmetic operations and a gcd computation, perhaps it's manageable. 

For example, each step has:

- new_num = a_i * current_num + current_den 

- new_den = current_num 

- compute gcd(new_num, new_den) 

- divide by gcd 

But the gcd computation is the most expensive part. 

But the Euclidean algorithm for gcd is O(log min(new_num, new_den)) steps. 

But for numbers like 1e18, log min is about 60. But for numbers with 1e18 digits, this is impossible. 

But in practice, for numbers with up to 1e18, the gcd is computed quickly. 

But when the numbers are up to 1e18^90, their log is 90 * log(1e18) = 90 * 60 = 5400 steps. For each step, the modulus is computed. 

But modulus of two very large numbers is O(1) in Python's internals, but in practice, it's O(n) where n is the number of digits. 

Thus, this approach may not be feasible for the worst-case scenarios. 

But considering the problem's constraints, perhaps the intended solution is to proceed with this approach. 

So, perhaps the code is supposed to compute the continued fraction step by step, reducing each time, and then compare with p/q. 

Thus, the code would be as follows:

Read p, q. 

Compute the gcd of p and q, then simplify p and q. 

Read n and the list a. 

If n is 0, output NO. 

If the length of a is not n, output NO. 

Compute the continued fraction:

current_num = a[-1]

current_den = 1

for i in range(n-2, -1, -1):

    a_i = a[i]

    new_num = a_i * current_num + current_den

    new_den = current_num

    g = math.gcd(new_num, new_den)

    current_num, current_den = new_num // g, new_den // g

After processing all steps, check if current_num * q == current_den * p. 

If yes, output YES, else NO. 

But the code must handle very large numbers. 

But in Python, this is possible. 

Let's test the first sample:

Sample 1:

p=9, q=4. 

gcd(9,4) is 1. 

a = [2,4], n=2. 

Process a[1] (4) → current_num=4, den=1. 

Then process a[0] (2):

new_num = 2 *4 +1 =9

new_den=4 

gcd(9,4)=1 → current_num=9, den=4. 

Compare 9*4 ==4*9 → 36=36 → YES. 

Sample 2:

p=9/4, a=[2,3,1]. 

Processing a[2]=1 → current_num=1, den=1. 

Then a[1]=3:

new_num=3*1 +1 =4, new_den=1. gcd 4,1 → 4/1. 

Then a[0]=2:

new_num=2*4 +1=9, new_den=4. 

Compare 9*4=4*9 → YES. 

Sample 3:

p=9/4. a=[1,2,4]. 

Process a[2]=4 → current_num=4, den=1. 

Then a[1]=2 → new_num=2*4 +1 =9, new_den=4. 

Then a[0]=1 → new_num=1*9 +4=13, new_den=9. 

Compare 13*4=9*9 → 52=81 → NO. 

Which matches the samples. 

Thus, the code works for these samples. 

Now, what about a test case where the numbers are very large. 

For example, a_i =1e18 for n=90 steps. 

In this case, the code would process each step, multiply a_i=1e18 by the current_num, add current_den, then compute the gcd. 

But after each step, the current_num and current_den would be (1e18 * current_num + current_den) // g and current_num // g. 

But if the gcd is 1 each time, then current_num grows exponentially. 

But for n=90 steps, this is impossible to handle. 

But how can the code pass within the time limit? 

Perhaps the problem's constraints are designed such that the maximum possible numbers after reduction are manageable. 

But even if the numbers are 1e18, after 90 steps, the numbers would be 1e18^90, which is impossible. 

So, the code would not pass such test cases. 

But why the problem's constraints allow n up to 90 and a_i up to 1e18? 

Perhaps there's an alternative approach that I'm missing. 

Wait, perhaps there's a mathematical way to compute the continued fraction's numerator and denominator without explicitly computing them. 

Another idea: the cross product between the continued fraction and p/q is num * q == den * p. 

We can compute this cross product incrementally, using modular arithmetic. 

For example, compute (num * q - den * p) modulo some primes. If any modulo is not zero, return NO. But if it's zero for multiple primes, then return YES. 

But this is a probabilistic approach and can lead to false positives. 

The problem requires an exact answer, so this approach is not suitable. 

Another idea: during the computation, track the numerator and denominator as floating-point numbers. But this is impossible due to precision issues. 

For example, even if a_i is 1e18, the floating-point representation would lose precision after a few steps. 

Thus, this is not feasible. 

So, it seems that the only way is to proceed with the initial approach, and hope that the numbers are manageable. 

But how to handle cases where the numbers are extremely large. 

Perhaps in practice, the code will work for the given constraints, even for large a_i, because Python's big integers are optimized. 

But when a_i is 1e18 and n=90, the numbers are 1e18^90, which is 1e1620, and even if each step takes 1e-6 seconds, 90 steps would take 9e-5 seconds. But with big integers, each step's operations take longer. 

But in practice, this is impossible. 

Thus, I'm missing something. 

Wait, maybe the problem has a hidden constraint that the continued fraction's denominator after all steps is equal to q. 

But no, the problem allows any denominator. 

Alternative idea: the continued fraction's numerator and denominator can be represented as a pair of integers, and during the steps, we can keep track of whether they are equivalent to p/q without explicitly storing the large numbers. 

But how? 

For example, the equation we need to check is (current_num / current_den) == (p/q). 

Which is equivalent to current_num * q == current_den * p. 

But during each step, we can represent current_num and current_den in terms of p and q. 

But I'm not sure. 

Alternatively, we can represent the equation as current_num * q - current_den * p = 0. 

During each step, this difference can be computed. 

But again, for very large numbers, this difference would be a very large number. 

Thus, this approach is not feasible. 

At this point, I'm stuck. 

Given that the problem's constraints allow n up to 90 and a_i up to 1e18, and the time limit of 2 seconds, the intended solution is likely the initial approach. 

Thus, the code would be as described, but with the step-by-step computation and reduction. 

So, here's the Python code:

Read p and q. 

Simplify p and q by dividing by their gcd. 

Read n and a. 

If len(a) is not n, output NO. 

Compute the continued fraction:

current_num = a[-1]

current_den = 1

for i in range(n-2, -1, -1):

    a_i = a[i]

    new_num = a_i * current_num + current_den

    new_den = current_num

    g = math.gcd(new_num, new_den)

    current_num, current_den = new_num // g, new_den // g

Compare current_num * q == current_den * p. 

Output YES or NO accordingly. 

But wait, the code must read a from the third line. 

Let me see. 

The input is:

First line: p q 

Second line: n 

Third line: a1 a2 ... an 

So, the code must read these correctly. 

In Python:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    p, q = map(int, input_stream.readline().rstrip("\n").split())

    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if len(a) != n:

        print("NO", file=output_stream)

        return

    # Simplify p and q

    g = math.gcd(p, q)

    p_simplified = p // g

    q_simplified = q // g

    current_num = a[-1]

    current_den = 1

    for i in range(n-2, -1, -1):

        a_i = a[i]

        new_num = a_i * current_num + current_den

        new_den = current_num

        g = math.gcd(new_num, new_den)

        current_num = new_num // g

        current_den = new_den // g

    if current_num == p_simplified and current_den == q_simplified:

        print("YES", file=output_stream)

    else:

        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9 4
3
2 3 1
""",
            "output": \
"""\
YES
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

Second sample: current_num=9, current_den=4 → YES. 

Third sample: current_num=13, current_den=9. p_simplified=9/4 → 9 and 4. Not equal. 

Thus, code is correct. 

Thus, this should be the correct approach. 

Now, the only thing left is to handle very large numbers. 

But given that Python can handle arbitrarily large integers, and the steps are O(n), which is 90, this code should work within the time constraints. 

For example, even if each step involves very large numbers, the code would process them. 

Thus, this is the correct solution.
</think>

```python
import math

p, q = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

if len(a) != n:
    print("NO")
    exit()

# Simplify p and q by their gcd
g_pq = math.gcd(p, q)
p_simplified = p // g_pq
q_simplified = q // g_pq

current_num = a[-1]
current_den = 1

for i in range(n-2, -1, -1):
    ai = a[i]
    new_num = ai * current_num + current_den
    new_den = current_num
    g = math.gcd(new_num, new_den)
    current_num = new_num // g
    current_den = new_den // g

if current_num == p_simplified and current_den == q_simplified:
    print("YES")
else:
    print("NO")
```
