<think>
Okay, so I have this programming problem to solve, and I need to figure out the best approach. Let's read the problem statement carefully.

The problem is about a set of functions that are piecewise linear. Each function y_i(x) is either k_i * x + b_i if that value is non-negative, otherwise zero. The task is to find the number of angles (corners) in the graph formed by the sum of all these functions. Importantly, the angles that are 180 degrees (i.e., straight lines, no actual corner) should not be counted, and we need the count of the remaining angles.

Hmm. So the sum of all these functions is a polyline, and each function contributes certain breakpoints where they switch from the linear part to zero. The sum's polyline will have corners at the x-coordinates where any of the individual functions switch their state (from active to inactive or vice versa). But when multiple functions switch at the same x-coordinate, it might create a corner, but if the slope changes add up in a way that the total sum's slope change is zero, then there's no actual angle there (since the overall slope would continue smoothly).

Wait, no. The sum's slope at a point x is the sum of the slopes of all active functions at x. Each function contributes k_i when active (i.e., when x >= -b_i/k_i if k_i is positive, or x <= ... if k_i is negative, etc.), depending on the function's parameters. So each function can have a critical x-value where it switches between active and inactive.

The key idea here is that each function's critical x is where k_i * x + b_i = 0. Solving for x gives x = -b_i / k_i. However, this is only valid if k_i is not zero. For k_i = 0, the function is either always active (if b_i >= 0) or always inactive (if b_i < 0). So for each function, if k_i is not zero, it contributes a critical x-value. But for k_i=0, if b_i >=0, the function is a constant b_i, so it never switches. If k_i is 0 and b_i < 0, the function is always 0, so no switches.

So for each function, we need to compute its critical x (if it exists), and collect all these x-values. Then, the sum function's polyline will have possible corners at these x-values, but only if the sum of the functions' slopes changes as we cross x. So when we process all the critical points, for each x in the sorted list of critical points, we need to check if the left and right slopes (sum of active functions' k_i) differ. If they do, then that x is a corner. Otherwise, not.

But the problem is that there could be up to 1e5 functions, each contributing up to one critical x. So the total number of critical points is up to 1e5. So we need to process them efficiently.

The steps to solve the problem would be:

1. Collect all the critical x values where any function switches state. But for functions where k_i is zero, we can ignore them if they don't switch (since their state is fixed).

2. For each critical x, compute the change in the total slope when passing through x. If the change is non-zero, then this x contributes a corner. Otherwise, it's a smooth transition and doesn't count.

3. Count all such x's where the slope change is non-zero. The number of such x's is the answer, plus possibly the initial segments if needed (wait, maybe not. Let's think.)

Wait, the initial sum function is a polyline. The graph starts from x = -infinity. But when we process all the critical x's, sorted in order, each between adjacent x's is a line segment. The corners are the points where the slope changes. So for each x in the sorted list of critical points, we need to check if the slope before and after x is different.

But how do we compute the slope change at each x?

Approach:

- First, collect all critical x values where a function can switch. For each function, compute x0 where k_i*x0 +b_i=0. But only for functions where k_i is not zero. Also, we need to check if the function actually switches. For example, if k_i is positive, then the function is active when x >= x0. If k_i is negative, then active when x <= x0. Wait, no. Let me think.

Wait, for a function y_i(x) = max(0, k_i x + b_i). So the function is active (non-zero) when k_i x + b_i >=0. Solving for x, if k_i is positive, then x >= (-b_i)/k_i. If k_i is negative, then x <= (-b_i)/k_i. If k_i is zero, then if b_i >=0, the function is always active (constant b_i), else always zero.

So for each function with k_i !=0, there is a critical x0 = (-b_i)/k_i. Depending on the sign of k_i, the function is active when x is on one side of x0. So for example, if k_i is positive, the function is active for x >=x0, and zero otherwise. So the switch happens at x0. For a function with k_i negative, the function is active when x <=x0, and zero otherwise. So again, the switch is at x0.

But wait, what if x0 is such that, say, k_i is positive, but for x < x0, the function is zero. For x >= x0, the function is active. So at x0, the function starts contributing. Similarly for k_i negative: function is active for x <=x0, zero otherwise. So each such function contributes a critical x0, and when x crosses x0, the function's contribution to the sum changes (either starts contributing or stops contributing).

So for each such x0, the sum's slope (the sum of all active functions' k_i) changes by the k_i of that function. Because when x is just below x0 (for k_i positive), the function is not active. When x is just above x0, the function becomes active. So the slope increases by k_i. Similarly, for k_i negative: when x is just below x0, the function is active. When x is just above x0, the function is inactive. So the slope decreases by k_i. Wait, no. Wait, if k_i is negative, then the function is active when x <= x0. So at x0, when x increases beyond x0, the function becomes zero, so the slope decreases by k_i (since the function's slope was part of the sum before, and is subtracted now).

So for each critical x0, the change in slope is delta = (if k_i positive, then +k_i) when crossing x0 from left to right, or delta = -k_i if k_i is negative (because the function stops contributing when x is above x0). Wait, no. Let's think again.

For a function with k_i positive: x0 is (-b_i)/k_i. For x < x0, the function is zero. For x >= x0, the function is active. So when crossing x0 from left to right, the slope increases by k_i. So delta is +k_i.

For a function with k_i negative: x0 is (-b_i)/k_i. For x <= x0, the function is active. For x >x0, it's zero. So when crossing x0 from left to right, the function becomes inactive. So the slope decreases by k_i (since before, the function was contributing k_i to the sum). So delta is -k_i.

So for each critical x0, the delta is equal to (if k_i is positive: +k_i, else if k_i is negative: -k_i). Wait, but k_i can be zero. But for the functions contributing a critical x0, k_i is not zero. So for each critical x0, the delta is k_i * sign(k_i) ?

Alternatively, for a function with k_i !=0, when crossing x0, the delta in the sum's slope is (if the function was not active before x0 and becomes active after x0, then +k_i; if the function was active before and becomes inactive after, then -k_i). So how do we model this?

Alternatively, for each function, when you cross x0 (if k_i is positive), you add k_i to the slope. If k_i is negative, when you cross x0, you subtract k_i (because the function was active before and becomes inactive after). So the delta is k_i if the function is added (i.e., k_i positive) and -k_i if the function is removed (k_i negative). So in general, the delta for x0 is the sign of k_i multiplied by k_i? Wait, that's not possible.

Wait, for k_i positive, crossing x0 from left to right adds k_i to the slope. So delta is +k_i.

For k_i negative, crossing x0 from left to right removes k_i from the slope. So delta is -k_i.

So the delta is k_i if k_i is positive, and -k_i if k_i is negative. Wait, but that's the same as abs(k_i) if k_i is positive, but for k_i negative, delta is -k_i (which is positive). Wait, no. For example, if k_i is -2, then delta is - (-2) = +2. So for a function with k_i negative, when you cross x0, the slope decreases by k_i (since the function was active before and now is inactive). So the slope change is -k_i.

Wait, let's take an example:

Suppose k_i is -2, and x0 is some value. For x <=x0, the function is active (since k_i is negative). So the slope includes -2. For x >x0, the function is inactive, so the slope doesn't include -2. So when moving from x just below x0 to x just above x0, the slope decreases by 2 (because the function's contribution of -2 is removed). So the delta is (-2) when the function is removed. So delta = - ( -2 ) = 2? Wait, no.

Wait, the slope before x0 (left) is sum of all active functions' k_i. After x0 (right), the slope is sum minus (-2). Because the function was active before x0 and is inactive after. So delta = (sum after) - (sum before) = (sum before - (-2)) - sum before) = +2. So delta is +2.

Wait, that's a bit confusing. Let's see:

sum_before = sum (k_j for j in active functions before x0)

sum_after = sum (k_j for j in active functions after x0)

So for a function with k_i negative, when we cross x0 (moving left to right), the function is active before but not after. So sum_after = sum_before - k_i.

So delta = sum_after - sum_before = -k_i.

Ah, right. Because delta is (sum_after - sum_before) = (sum_before - k_i) - sum_before) = -k_i.

So for a function with k_i positive: when crossing x0 (left to right), the function becomes active. So sum_after = sum_before + k_i. delta is k_i.

For a function with k_i negative: when crossing x0 (left to right), the function becomes inactive. So sum_after = sum_before - k_i. So delta is -k_i.

So the delta is k_i if k_i is positive, delta is -k_i if k_i is negative.

Alternatively, delta is (sign of k_i) * k_i. Because for positive k_i, delta is +k_i. For negative, delta is -k_i (which is positive, since k_i is negative). So for example, if k_i is -5, delta is 5.

So each critical x0 contributes a delta of (k_i if k_i >0 else -k_i) to the slope change at x0.

But how does this affect the total number of angles? Each x0 where the delta is non-zero contributes a corner. So for each x0, if the sum of all deltas at x0 is non-zero, then there is a corner. But wait, no. Because multiple functions can have the same critical x0. So when x0 is the same for several functions, their deltas are summed. The total delta for x0 is the sum of all individual deltas (k_i or -k_i) for all functions that switch at x0. If the total delta is non-zero, then the sum's slope changes at x0, leading to a corner. If the total delta is zero, then the slope doesn't change, so no corner.

So the plan is:

- Collect all critical x0's, each with their delta (k_i if k_i is positive, else -k_i).

- For functions where k_i is zero: if b_i >=0, they contribute a constant term (their slope is zero, so they don't affect the sum's slope). If b_i <0, they contribute zero. So these functions don't contribute any critical x0's and don't affect the slope. So we can ignore them in terms of delta.

So the steps:

1. For each function:

   a. If k_i is zero: check if b_i >=0. If yes, this function contributes a constant to the sum, but doesn't affect the slope. If no, contributes nothing. So ignore for delta and x0.

   b. Else (k_i not zero): compute x0 = (-b_i)/k_i. Then, depending on the sign of k_i, the delta is k_i (if k_i positive) or -k_i (if k_i negative). So for each x0, we add a delta of (k_i if k_i >0 else -k_i).

But wait, for a function with k_i positive, when x increases past x0, the function becomes active. So delta is +k_i. For a function with k_i negative, when x increases past x0, the function becomes inactive. So delta is -k_i. But for a function with k_i negative, x0 is the point where the function's value is zero. For x <=x0, the function is active (since k_i is negative, so for x <=x0, k_i x +b_i >=0). For x >x0, it's inactive.

So yes, the delta is -k_i. So for each such function, the delta is (k_i if k_i>0 else -k_i). Because for k_i negative, delta is -k_i (which is positive).

So all critical x0's are the points where some functions switch, and each x0 has a total delta which is the sum of all individual deltas for functions switching at x0.

Now, the key is to collect all x0's and their delta sums. Then, for each x0, if the delta sum is not zero, then that x0 contributes a corner.

So the steps to solve the problem:

- Iterate through all functions, collect x0's (for non-zero k_i) and their delta contributions.

- Group x0's by their value, summing the deltas for the same x0.

- Then, for each x0 in the sorted list of unique x0's, if the sum of deltas is not zero, then this x0 contributes a corner.

- The count of such x0's is the answer.

Wait, but why? Because the sum's slope changes at x0 by the delta sum. If the delta sum is non-zero, the slope changes, creating a corner. So each such x0 is a corner. The initial and final slopes don't matter as they are part of the same line segments.

Wait, but the initial state (x approaching -infinity) would have a certain slope. Then, as x increases, each x0 in the sorted list (sorted in increasing order) is a point where the slope changes. The number of times the slope changes (i.e., delta sum is not zero) is the number of corners. Because each such change in slope introduces a new line segment, which meets the previous at an angle (if the slope is different).

So the answer is the number of x0's where the sum of deltas is non-zero.

But how to handle x0's that are the same? For example, if two functions have the same x0, their deltas are added. So if the sum is zero, then even though both functions switch at x0, their combined effect cancels out the slope change, so no corner.

So the algorithm becomes:

1. For each function with k_i !=0:

   a. Compute x0 = (-b_i) / k_i. But we need to represent this as a fraction to avoid precision errors. Because using floating points can lead to errors when comparing x0's. For example, if two x0's are equal but computed differently, they might end up as different due to floating point precision. So to avoid this, we can represent x0 as a fraction (numerator, denominator) in reduced form.

But handling fractions can be tricky. Let's think. For each x0 = (-b_i)/k_i, we can represent it as a pair (-b_i, k_i) but reduced to their simplest form, ensuring that the denominator is positive. Wait, no. Because for example, if k_i is negative, then the denominator would be negative, which could lead to different representations for the same x0. So how to correctly group x0's?

Yes, this is a crucial point. If we compute x0 as a floating point number, we can't compare them accurately. So to avoid this, we need to represent x0 as a fraction in reduced form, stored as a pair of numerator and denominator. Then, two x0's are equal if their numerator and denominator are the same.

But how to do that properly?

Each x0 is (-b_i) / k_i. Let's write this as (-b_i) divided by k_i. To reduce this fraction, we can compute the greatest common divisor (gcd) of (-b_i) and k_i, then divide both by the gcd. But we also need to ensure that the denominator is positive. So:

For each function with k_i !=0:

x0 = (-b_i) / k_i.

We can represent x0 as a fraction (numerator, denominator), where:

gcd = gcd of (-b_i) and k_i.

numerator = (-b_i) / gcd.

denominator = k_i / gcd.

But if denominator is negative, we can multiply both numerator and denominator by -1 to make denominator positive.

So for example, if k_i is -3 and b_i is 5, then x0 is (-5)/(-3) = 5/3. So numerator is 5, denominator is 3.

But if k_i is 3 and b_i is -5, x0 is (5)/3, same as before.

But if k_i is -3 and b_i is 5, then:

numerator = (-5) [because (-b_i) is -5] divided by gcd(-5, -3). The gcd of -5 and -3 is 1. So numerator is -5, denominator is -3. Then, since denominator is negative, multiply both by -1: numerator 5, denominator 3.

So the process is:

For each x0, compute numerator and denominator as follows:

numerator = -b_i

denominator = k_i

Compute the gcd of numerator and denominator. But since denominator can be negative, perhaps it's better to take absolute values.

Wait, perhaps the correct way is:

numerator = -b_i

denominator = k_i

Then, compute the greatest common divisor of numerator and denominator, but considering the signs. Wait, no. Because the gcd is a positive integer. So the sign is irrelevant for the gcd.

So, we can compute the gcd of abs(numerator) and abs(denominator). Then, we divide numerator and denominator by this gcd. Then, ensure that the denominator is positive. If denominator is negative after division, multiply both numerator and denominator by -1 to make denominator positive.

So for example:

numerator = -b_i = 5, denominator = -3.

gcd(5,3) = 1.

so numerator/gcd is 5, denominator/gcd is -3.

But denominator is negative. So multiply numerator and denominator by -1: numerator becomes -5, denominator becomes 3.

So the fraction is -5/3.

Wait, but that's the same as 5/-3. But how to represent it correctly as a fraction in reduced form with denominator positive.

So the steps are:

Compute the gcd of abs(numerator) and abs(denominator).

d = gcd(abs(n), abs(d)).

n' = n / d

d' = denominator / d

if d' <0, then multiply both by -1.

So, for the example where numerator is 5, denominator is -3:

gcd(5,3)=1.

n' =5 /1=5

d' =-3/1 =-3.

Since d' is negative, multiply both by -1: n' = -5, d'=3.

So the reduced fraction is (-5,3).

Wait, but that's equivalent to 5/-3. But how to represent x0 as a fraction correctly.

Wait, x0 is (5)/(-3) = -5/3. So the reduced fraction would have numerator -5, denominator 3. But when we do that, the actual x0 is -5/3.

But perhaps the way to represent the fraction is as (a, b) where x0 = a / b, and b is positive. So that when two x0's have the same (a, b) pair, they are the same.

So the approach is:

For each x0, compute the reduced fraction (a, b) where a is the numerator, b is the denominator (positive), and gcd(a, b) is 1.

So, the process is:

For a function with k_i !=0:

x0 = (-b_i)/k_i.

We represent this as a fraction (numerator, denominator) where:

numerator = (-b_i) * sign(denominator_initial)

denominator = |k_i| / gcd, where gcd is the gcd of |-b_i| and |k_i|.

Wait, perhaps not. Let me think again.

Let's take the original numerator as -b_i and denominator as k_i.

We need to reduce this fraction to its simplest form, ensuring that the denominator is positive.

Compute gcd = gcd(abs(-b_i), abs(k_i)) = gcd(abs(b_i), abs(k_i)).

Then, divide both numerator and denominator by gcd:

numerator_reduced = (-b_i) / gcd.

denominator_reduced = k_i / gcd.

Now, if denominator_reduced is negative, multiply both numerator_reduced and denominator_reduced by -1 to make denominator positive.

So for example:

b_i = 5, k_i = -3.

numerator_initial = -5.

denominator_initial = -3.

gcd = gcd(5,3) =1.

numerator_reduced = -5/1 = -5.

denominator_reduced = -3/1 = -3.

Since denominator_reduced is negative, multiply numerator and denominator by -1: numerator becomes 5, denominator becomes 3.

So the fraction is 5/3. But x0 is (-5)/ (-3) = 5/3. So this is correct.

Another example:

b_i = 5, k_i =3.

numerator_initial = -5.

denominator_initial =3.

gcd=1.

denominator is positive. So fraction is (-5,3). But x0 is -5/3.

Wait, but how is this handled? So if two x0's have fractions (a, b) and (c, d), and a/b == c/d, then they are considered the same x0.

But to ensure that, we need to represent the fraction in reduced form with denominator positive.

Yes. So, the code can process each x0 as a tuple (numerator, denominator) where denominator is positive, and the fraction is in reduced form. Then, two x0's are considered equal if their numerator and denominator are equal.

So in code, how can we compute this?

In Python, for each function with k_i !=0:

Compute numerator = -b_i

denominator = k_i

gcd = math.gcd(abs(numerator), abs(denominator))

if gcd ==0:  # but denominator is k_i, which is non-zero here, so gcd can't be zero.

numerator //= gcd

denominator //= gcd

if denominator <0:

    numerator *= -1

    denominator *= -1

So after this, denominator is positive, and numerator and denominator are coprime.

So, for example, (5, -3) becomes (5//1, -3//1) → (5,-3). Then, since denominator is negative, multiply numerator and denominator by -1 → (-5,3).

Wait, no. Let me see:

Original denominator after division is -3. So:

denominator = (k_i // gcd) → suppose k_i was -3, gcd is 1. Then denominator is -3.

Then, since denominator is negative, multiply numerator and denominator by -1. So:

numerator becomes 5 * -1 = -5.

denominator becomes -3 * -1 = 3.

So the fraction is -5/3. Which is correct.

So the code would generate the tuple (numerator, denominator) as (-5, 3), which is correct as x0 is (-b_i)/k_i = (5)/ (-3) → x0 is -5/3, but represented as numerator -5 and denominator 3.

Wait, but x0 is 5/ (-3) → which is -5/3. So the tuple is (-5,3) which represents -5/3. Which is the correct x0.

So yes, this approach correctly captures x0 as a fraction in reduced terms with denominator positive.

Once all x0's are processed into such tuples, we can group them and sum their deltas (which are k_i if k_i is positive, else -k_i).

Wait, no. The delta is k_i if k_i is positive, else -k_i.

So for each function, the delta is:

if k_i >0: delta is k_i

else: delta is -k_i (since for k_i <0, delta is -k_i)

So delta is abs(k_i) ?

Wait, no. For k_i positive: delta is +k_i. For k_i negative: delta is -k_i. But for example, if k_i is -2, delta is 2. So delta is the absolute value of k_i.

Yes. Because delta is k_i if k_i is positive, and (-k_i) if k_i is negative. So delta is abs(k_i) for all k_i.

Wait, no. Wait:

For k_i positive:

delta is k_i. So if k_i is 5, delta is 5.

For k_i negative:

delta is -k_i. For example, k_i =-5, delta is 5.

So yes, delta is abs(k_i) for all k_i.

So for each function, delta is abs(k_i).

So regardless of the sign of k_i, the delta is the absolute value of k_i.

Wait, this can't be right. Let me re-examine:

For k_i positive, when crossing x0, the function becomes active, adding k_i to the slope. So delta is +k_i.

For k_i negative, when crossing x0, the function becomes inactive, subtracting k_i from the slope (since it was active before). So delta is sum_after - sum_before = (sum_before -k_i) - sum_before = -k_i.

But k_i is negative. So delta is -k_i (which is a positive value). So for k_i = -5, delta is 5.

So yes, delta is abs(k_i) for all functions with k_i !=0.

So for each function with k_i !=0, delta is abs(k_i).

So for each x0 in the tuple (numerator, denominator), we can compute the delta as abs(k_i).

So when multiple functions have the same x0 (same tuple), their deltas are summed. So the total delta for x0 is the sum of abs(k_i) for all functions contributing to that x0.

Then, after processing all functions, for each x0, if the sum of deltas (sum_abs_k) is non-zero, then this x0 is a corner point. The total number of such x0's is the answer.

So the steps in code are:

- Read n.

- For each of the n lines:

   read k_i, b_i.

   if k_i ==0:

       if b_i >=0: sum all their constants (but since the output is the number of corners, not the sum, this doesn't affect the answer). So we can ignore these functions.

   else:

       compute x0 as (-b_i)/k_i, represented as a fraction (numerator, denominator) in reduced form, denominator positive.

       delta = abs(k_i)

       add to a dictionary: key is the (numerator, denominator) tuple, value is the sum of deltas.

- After processing all functions, collect all keys (x0's) in the dictionary where the sum of deltas is non-zero.

- The number of such keys is the answer.

Wait, but how to sort the x0's? Because the order of x0's is not required here. Because each x0 is a critical point where the slope could change. But the problem is that when multiple functions have the same x0, their deltas are summed, and if the sum is non-zero, it's a corner. So the code can proceed by just counting the number of x0's in the dictionary where the sum is non-zero.

But why don't we need to sort the x0's?

Because each x0 is a unique point (represented by the fraction (numerator, denominator)), and for each such x0, the sum of deltas is the total change in slope. If that sum is non-zero, it's a corner. The order of x0's doesn't affect the count of corners. So regardless of their order, each x0 with non-zero sum contributes exactly one corner.

So the code can process all x0's, group them by their (numerator, denominator) key, sum their deltas (abs(k_i)), and count how many keys have a sum not equal to zero.

Thus, the answer is the number of entries in the dictionary where the sum of deltas is non-zero.

Wait, that's correct? Because each x0 is a point where the slope changes by sum_deltas. If sum_deltas is non-zero, then the slope changes, leading to a corner. So each such x0 contributes one corner.

Yes.

So the code steps:

Read n.

Initialize a defaultdict (or a normal dictionary) to keep track of sum_deltas for each x0.

For each function:

   k, b = map(int, input().split())

   if k ==0:

       continue (since they don't contribute any x0 and delta)

   else:

       compute numerator = -b

       denominator = k

       # reduce the fraction

       g = math.gcd(abs(numerator), abs(denominator))

       numerator //= g

       denominator //= g

       if denominator <0:

           numerator *= -1

           denominator *= -1

       # now denominator is positive.

       key = (numerator, denominator)

       delta = abs(k)

       # add delta to the key's sum

       sum_deltas[key] += delta

Once all functions are processed:

count the number of keys where sum_deltas[key] is not zero.

Print that count.

Wait, but wait. The sum of deltas is sum of abs(k_i) for all functions that have x0 as this key. So for example, if two functions have the same x0, and their deltas are 3 and 5, then the sum is 8. So the slope changes by 8 at x0, hence a corner.

But if sum is zero (like two functions with deltas 5 and -5?), but no, delta is always positive (since it's abs(k_i)), so sum can't be zero unless there are no functions contributing to that x0. Wait, no. Because for each function, delta is abs(k_i), which is non-negative. So the sum is the sum of absolute values of k_i's for functions contributing to that x0. So the sum can only be zero if no functions contribute to that x0, which can't happen.

Wait, no. For example, if a function has k_i =0, but we skipped those. For other functions, delta is abs(k_i), which is positive. So each x0 in the dictionary is contributed by at least one function, and sum_deltas is the sum of positive numbers. So sum_deltas can never be zero. So the answer is the total number of entries in the dictionary.

Wait, that's not possible. Because how can sum of positive numbers be zero?

Yes, because each delta is the absolute value of k_i. And k_i is non-zero (since we only process functions where k_i !=0). So delta is positive. So for any x0 in the dictionary, sum_deltas is the sum of positive integers, hence >= delta (which is >=1, since k_i is integer and non-zero, so abs(k_i) >=1). So sum_deltas is at least 1. So every entry in the dictionary contributes a sum_deltas >=1, hence every x0 in the dictionary contributes a corner. So the answer is simply the number of entries in the dictionary.

Wait, that can't be right. Let's look at the examples.

First example:

Input:
1
1 0

So k_i=1, b_i=0. So x0 = (0)/1 → 0. So the key is (0,1). delta is 1. Sum is 1, which is non-zero. So the answer is 1. Which matches the first example.

Second example:

3
1 0 → x0=0, delta 1.

0 2 → k=0, so ignored.

-1 1 → x0 = (-1)/ (-1) = 1. So denominator is 1. So key is (1,1). delta is abs(-1) =1. So sum_deltas has two entries: (0,1) with sum 1, (1,1) with sum 1. So total entries 2 → which matches the second example's output of 2.

Wait, but the sample input 2's output is 2. So the code would output 2, which is correct.

Third example:

3
-2 -4 → x0 = (4)/ (-2) → -2. So represented as (4, -2) → after reduction: gcd(4, 2) is 2. numerator 4/2=2. denominator -2/2= -1. Since denominator is negative, multiply by -1: numerator -2, denominator 1. So key (-2,1). delta is 2.

1 7 → x0 = (-7)/1. So key (-7,1). delta 1.

-5 1 → x0 = (-1)/ (-5) → 1/5. So numerator 1, denominator 5. delta 5.

So sum_deltas has three entries: (-2,1) → sum 2, (-7,1) → sum 1, (1,5) → sum5. All non-zero. So count is 3. Which matches the third example.

So the code's approach works for all examples.

But wait, the third example's output is 3. So the code would return 3.

So according to this, the code would count all x0's, since sum_deltas is always positive, hence each x0 in the dictionary contributes a corner.

But then, why are the steps involving summing deltas? Because sum_deltas is the sum of abs(k_i) for all functions contributing to that x0. Since each abs(k_i) is positive, the sum is positive. Hence, all entries in the dictionary are counted.

So the answer is simply the number of entries in the dictionary.

But this seems to contradict the initial analysis. Because earlier I thought that the sum_deltas for a particular x0 can be zero. But according to this, sum_deltas is the sum of absolute values of k_i's for all functions that switch at x0, which can't be zero.

But how is that possible?

Because each function with k_i !=0 contributes a delta of abs(k_i) (since delta is k_i if k_i positive, -k_i if k_i negative, but in both cases, delta is the absolute value). So, for functions contributing to the same x0, their deltas are summed. For example, if two functions contribute to x0, their deltas are 3 and 5. So sum is 8. So the code would count this x0 once.

But in this case, the sum is 8, which is non-zero, so it's a corner.

But in another scenario, if two functions contribute deltas of 3 and -3. But no, because delta is the absolute value of k_i. So delta can't be negative. So sum is 3+3=6.

So sum_deltas can't be zero. Hence, all entries in the dictionary must have sum_deltas >=1, and the answer is the size of the dictionary.

So the code can be written as:

- For each function with k_i !=0, compute x0 as a reduced fraction, add delta=abs(k_i) to the sum for that x0.

- The answer is the number of keys in the dictionary (since all sums are non-zero).

But wait, in the code, when a function's x0 is computed, even if multiple functions have the same x0, their deltas (abs(k_i)) are summed. So the sum is the sum of their absolute values. So yes, each x0 in the dictionary has a sum >=1.

Thus, the answer is the number of x0's (the number of entries in the dictionary).

But wait, how can multiple functions contribute to the same x0? Because each function's x0 is (-b_i)/k_i, and if two different functions have the same (-b_i)/k_i, then their x0's are the same.

For example:

Function 1: k=2, b=4 → x0 = (-4)/2 = -2 → fraction (-4,2) reduces to (-2,1) → becomes (2, -1) → wait, no. Let's compute:

numerator = -b_i → -4.

denominator = 2.

gcd(4, 2) is 2.

numerator_reduced = -4 /2 = -2.

denominator_reduced = 2/2=1.

Since denominator is positive, key is (-2, 1).

Function 2: k=1, b=2 → x0 = (-2)/1 = -2 → key (-2,1).

So both functions contribute to the same x0. Their deltas are 2 and 1. Sum is 3. So the code counts this x0 once. So the answer would be 1 (since the other functions are processed as well, but assuming these are the only ones).

So the code's approach is correct.

Thus, the code can be written as follows:

Read n.

For each function, if k_i is not zero, compute x0's fraction (numerator, denominator) as described. Add delta=abs(k_i) to the sum for that key.

The answer is the number of keys in the sum_deltas dictionary.

But wait, in the code, when we process a function, we add delta as abs(k_i) to the sum for that key. So the sum is sum of abs(k_i) for all functions with that x0. But in reality, the delta for that x0 is the sum of the individual deltas (k_i for positive k_i, -k_i for negative), but in our code, we are adding abs(k_i), which is equivalent.

Wait, no. Because the actual delta is the sum of individual deltas, which for each function is k_i if k_i positive, else -k_i. So the total delta is sum (k_i if k_i>0 else -k_i).

But in code, we're adding abs(k_i) for each function, which is the same as sum (k_i if k_i>0 else -k_i). Because for k_i positive, abs(k_i) =k_i. For k_i negative, abs(k_i) =-k_i. So sum_deltas is the same as the total delta.

So the code is correct.

Therefore, the code can be written as:

Testing against sample inputs 1, 2.

```python
import math
from collections import defaultdict


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    sum_deltas = defaultdict(int)

    for _ in range(n):
        k, b = map(int, input_stream.readline().rstrip("\n").split())
        if k == 0:
            continue
        # compute x0 = (-b)/k as a reduced fraction
        numerator = -b
        denominator = k
        g = math.gcd(abs(numerator), abs(denominator))
        numerator //= g
        denominator //= g
        if denominator <0:
            numerator *= -1
            denominator *= -1
        # delta is abs(k)
        sum_deltas[(numerator, denominator)] += abs(k)

    # the answer is the number of entries in sum_deltas with sum !=0
    # but since all sums are >=1 (abs(k) is at least 1, since k is not zero)
    # So all entries are valid.
    print(len(sum_deltas), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 0
0 2
-1 1
""",
            "output": \
"""\
2
""",
        }, 
        {
            "input": \
"""\
3
-2 -4
1 7
-5 1
""",
            "output": \
"""\
3
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

Third example:

3 functions:

-2 -4 → x0 is (4)/-2 =-2. Reduced fraction (4, -2) → gcd 2. numerator 4/2=2, denominator -2/2=-1 → denominator negative. Multiply by -1: numerator -2, denominator 1 → key (-2,1). sum_deltas adds 2.

1 7 → x0 is (-7)/1 → key (-7,1). sum adds 1.

-5 1 → x0 is (-1)/-5 =1/5. key (1,5). sum adds 5. So three entries → output 3.

All examples are correct.

Thus, the code is correct.
</think>

```python
import math
from collections import defaultdict

n = int(input())
sum_deltas = defaultdict(int)

for _ in range(n):
    k, b = map(int, input().split())
    if k == 0:
        continue
    numerator = -b
    denominator = k
    g = math.gcd(abs(numerator), abs(denominator))
    numerator //= g
    denominator //= g
    if denominator < 0:
        numerator *= -1
        denominator *= -1
    sum_deltas[(numerator, denominator)] += abs(k)

print(len(sum_deltas))
```
