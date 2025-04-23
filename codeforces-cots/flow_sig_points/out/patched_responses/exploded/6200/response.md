<think>
Okay, let's tackle this problem. So the task is to determine whether a sequence of four integers is either an arithmetic or geometric progression and then output the next term. If it's neither, or if the next term isn't an integer, we output 42. 

First, I need to understand what defines an arithmetic and geometric progression. 

For arithmetic progression (AP), the difference between consecutive terms should be constant. So for a sequence a, b, c, d, we check if b - a == c - b == d - c. If yes, then the next term is d + (d - c). But since the input is four numbers, the next term would be the fifth. But wait, the problem says four numbers. So given four elements, check if they form an AP. Then compute the fifth element.

For geometric progression (GP), the ratio between consecutive terms should be constant. So check if b/a == c/b == d/c. But since the numbers are integers, we need to handle division carefully. Also, the problem states that in a GP, the first term and ratio can't be zero, and the ratio can't be 1. Moreover, if the next term isn't an integer (like division with a remainder), we have to output 42.

So the steps are:

1. Check if the sequence is an AP.
   - Compute the differences between consecutive terms. If all equal, proceed.
   - Next term is last term + common difference.
   - Since all terms are integers, the next term will be integer. So no problem here.

2. If not AP, check if it's a GP.
   - But need to check ratios. However, division with integers can be tricky. For example, 2,4,8,16 is GP with ratio 2. But 8,4,2,1 is ratio 0.5. How to check if the ratios are equal?

Wait, the problem says that the input is four integers. So when checking for GP, the ratios must be the same. But since the terms are integers, the ratio might not be an integer. But the next term must be integer. So even if the four terms form a GP, if the next term (like multiplying by a fractional ratio) is not integer, then we output 42.

So for the GP case:

Check if all consecutive ratios are equal. But how?

Possible approach: For each pair (a, b), (b, c), (c, d), check that the ratio is the same. But since we're dealing with integers, division can result in fractions. So perhaps we can represent the ratio as a fraction (numerator and denominator) and check if all ratios are equal fractions.

Alternatively, cross-multiply. For example, check if b * c == a * d for consecutive terms, but that's maybe not sufficient. Wait, for a GP, the ratios between consecutive terms must be equal. So for terms a, b, c, d:

b/a = c/b = d/c = q.

So cross-multiplying, b^2 = a*c, c^2 = b*d, etc. But perhaps for four terms, we can check if the first three ratios are equal and then the third ratio is the same.

So for four terms, check if (b * c) == (a * d) and (c^2) == (b * d). Wait, maybe not. Let's see. Suppose the four terms form a GP. Then:

b = a * q

c = b * q = a * q²

d = c * q = a * q³

So checking that the ratios between consecutive terms are the same. So for the four terms, the ratios between each consecutive pair should be the same. So:

b / a == c / b --> b² = a c

c / b == d / c --> c² = b d

But for four terms, we need to check that all three consecutive ratios are equal. So check if the ratio between the first and second is the same as between second and third, and third and fourth.

But in code, how to handle that with integers?

One way is to represent the ratio as a fraction in reduced form. For example, between the first two terms, the ratio is (b/a). But if a and b are integers, we can represent this as a fraction (numerator and denominator). But for a GP, all consecutive terms must have the same ratio. So the ratio between the first and second term is (b/a), between second and third (c/b), and third and fourth (d/c). These three must be equal.

But comparing fractions for equality requires cross-multiplication. For example, check if (b * c) == (a * d) for consecutive terms. Wait, no. Let's think: For two consecutive ratios to be equal, like between first and second (b/a) and second and third (c/b), they are equal if and only if b/a = c/b → b² = a c. Similarly, between second and third (c/b) and third and fourth (d/c), c/b = d/c → c² = b d.

So for four terms to form a GP, both these conditions must hold: b² = a c and c² = b d. Then, the common ratio is (b/a) = (c/b) = (d/c), provided that none of the denominators are zero.

But wait, the problem states that in a GP, the first term can't be zero, and the ratio q can't be zero or 1. Also, the terms can't be zero in the sequence.

Wait the problem's note for GP: b1 ≠0, q≠0, q≠1.

So in the input sequence, all terms must be non-zero. Because if any term is zero (except the first?), but the GP definition says that the first term is non-zero, and q is non-zero. So all terms in a GP must be non-zero.

So first, when checking for GP, if any of the four input terms is zero, then it can't be a GP. Because the first term is zero (which is invalid), or during the progression, a term becomes zero (but q is non-zero, so all terms must be non-zero). So if any of the four terms is zero, it's not a GP.

So the steps for checking GP:

1. Check that none of the four terms is zero. If any is zero, skip GP check.

2. Check that all consecutive ratios are equal. To do this:

   a. For the first three terms, check if b^2 == a * c.

   b. For the second and third terms, check if c^2 == b * d.

   c. Also, check that the ratio is not 1. Because if the ratio is 1, then it's a GP with q=1, which is invalid. Wait, the problem statement says in the GP definition that q != 1. So even if all consecutive ratios are 1 (so all terms are same), it's not considered a GP.

So after checking that all consecutive ratios are equal (i.e., b² = a c and c² = b d), and the ratio is not 1.

Wait, but how do we check the ratio is not 1? Because if the ratio is 1, then all terms are same. For example, 5,5,5,5. Then, in this case, the ratios between terms are 1. So according to the problem statement, this is not a GP because q=1. So even though the ratios are same, if q is 1, it's invalid.

So for the GP check:

After ensuring that all consecutive ratios are same, check if the ratio is 1. If so, then it's not a valid GP.

So the steps for GP check are:

- All terms are non-zero.

- Check that the ratios between consecutive terms are same. How?

We can represent the ratios as fractions and check if all are equal. But in code, to avoid floating points (which can lead to precision errors), perhaps using cross multiplication.

So for a, b, c, d:

Check that b * b == a * c (so first two ratios are same: b/a = c/b → b² = a c).

Check that c * c == b * d (so next ratios are same: c/b = d/c → c² = b d).

If both conditions are true, then the consecutive ratios are equal.

Then, the ratio is (b / a). But since we're dealing with integers, this could be a fraction. So the ratio is represented as a reduced fraction.

But to check if the ratio is 1, we can see if a == b. Because if a != 0, then ratio is b/a. If ratio is 1, then a = b. But since the terms are a, b, c, d, if a = b, then all terms must be equal (since in a GP with ratio 1, each term is same as previous). So in that case, the ratios would all be 1, but since q can't be 1, it's not a valid GP.

Wait, but if all terms are same, then it's an arithmetic progression with d=0. So in such a case, the AP check would have passed, because the differences between terms are zero, so it's an AP. So in this case, the AP check would take precedence, and the code would output the next term (same as before), but since the problem says that in the case of AP, output next term regardless.

But in the example where all terms are same, the AP check would pass (since all differences are zero). So the code would output the next term (same as previous), which is an integer, so no problem. Then, the GP check is not even considered.

So in code:

First check for AP. If yes, compute next term. Then proceed. Else, check for GP. Else, output 42.

So the order matters: check AP first. Because, a sequence with all terms same is both AP and GP (but the GP would be invalid because q=1). But since the problem says that GP is only valid when q != 1, so the all-same sequence is AP, and thus handled by the AP check.

Therefore, the code should check AP first.

So, the steps for the code:

1. Read four integers as a list.

2. Check if the sequence is an arithmetic progression.

   a. Compute the differences between consecutive terms. Check if all differences are equal.

   b. If yes, compute next term as last term + common difference. Since all terms are integers, this next term is integer. So output it.

3. Else, check if the sequence is a geometric progression.

   a. Check if any term is zero. If yes, skip (can't be GP).

   b. Else, check if b² == a*c and c² == b*d.

   c. If both conditions are met, check if the ratio (b/a) is not 1. Because if ratio is 1, it's invalid.

   d. If all conditions are satisfied, compute next term as d * ratio. But ratio is (b/a). Wait, but how to compute that ratio correctly? Because a, b are integers, and the ratio could be a fraction.

   e. For example, if the terms are 2, 6, 18, 54. Then ratio is 3. Next term is 54*3=162.

   But if the terms are 8,4,2,1: ratio is 0.5. So next term is 1 * 0.5 = 0.5, which is not integer. So in this case, the code should output 42.

   So when checking for GP, after confirming that the four terms form a GP, compute the next term as last term * ratio. But ratio is (b/a). However, since the ratio may be a fraction, even if the first four terms are integers, the next term may not be.

   So the code needs to compute next_term = d * (b // a) ? No, that's not correct. Because the ratio could be a fraction. For example, a=2, b=4, ratio is 2. Then next term is 8. But if a=4, b=2, then ratio is 0.5, which is 1/2. So next term is 1 (since 1 * 0.5 = 0.5, but wait, the terms are 4, 2, 1, 0.5? No, but in the input, the four terms are integers, so for the code to accept a GP, the four terms must form a GP. But the input is given as four integers. Wait, the input is four integers. So if the four terms are 8,4,2,1: they are all integers. So the code would check if they form a GP. Let's see:

Check if any term is zero: all are non-zero.

Check b² = a * c → 4² = 8*2 → 16=16 → yes.

c² = b * d → 2² =4*1 →4=4 → yes.

So the ratios are same. The ratio is 4/8 = 0.5, 2/4=0.5, 1/2=0.5. So the ratio is 0.5. Then, the next term is 1 * 0.5 = 0.5, which is not integer. So in this case, the code would output 42.

So the code must check whether the next term is integer. So after confirming that the sequence is a GP, compute next term as (d * ratio) and check if it's integer. If yes, output it. Otherwise, output 42.

But how to compute the ratio accurately? Because ratio is (b/a). But since the code is in Python, and the input terms are integers, the ratio can be represented as a fraction. So to compute next_term = d * (b/a). But since in the code, the terms are integers, and the ratio is (b/a), which is a rational number, then d * (b/a) must be computed as (d * b) / a. But this may result in a non-integer.

So the code can compute numerator = d * b, denominator = a. Then check if numerator is divisible by denominator. If yes, then next term is numerator // denominator. Else, output 42.

Wait, but the ratio is (b/a), which is same for all consecutive terms. Since the GP is valid, the ratio between each pair is the same. So for the next term, which is d * ratio, that is d * (b/a). But this can be represented as (d * b) // a only if a divides d*b.

So, for the code:

After confirming that the sequence is a GP (with all the checks including ratio !=1):

Compute next_term = d * (b // a) → no, that's not correct. Because if the ratio is 0.5 (as in the example), then (b/a) is 4/8 = 0.5. So d * (b/a) is 1 * 0.5 = 0.5. But since the input is integers, but the next term is not, the code must output 42.

So in code, when dealing with GP and calculating next_term, we need to compute (d * b) divided by a. But since the terms are in GP, the ratio is (b/a) = (c/b) = (d/c). So (d * b) must be equal to a * c (from the first check b² = a c → c = b²/a. Then, c² = b d → (b²/a)^2 = b d → b^4 / a² = b d → d = b^3 / a². So when calculating next term, which is d * (b/a) = (b^3 / a²) * (b/a) = b^4 / a^3. So in code, the next term is (d * b) // a if (d * b) is divisible by a.

Wait, but wait: next term is d multiplied by ratio. The ratio is (b/a). So next_term = d * (b/a). So the code should compute (d * b) / a, and check if this is an integer. So in code:

numerator = d * b

denominator = a

if denominator == 0: impossible (since we checked that all terms are non-zero)

if numerator % denominator == 0:

   next_term = numerator // denominator

else:

   output 42

But how?

For example, in the case where a=8, b=4, c=2, d=1:

numerator = 1 *4 =4, denominator =8. 4/8=0.5. So 4 mod 8 is 4, which is not zero. So output 42.

In the case where a=2, b=4, c=8, d=16:

numerator=16 *4=64, denominator=2. 64//2=32. So next term is 32. Correct.

Another example: input 836 624 412 200. Let's check the first sample.

Wait, the first sample input is 836, 624, 412, 200. The output is -12. Let's see: check AP.

Differences: 624-836= -212, 412-624= -212, 200-412= -212. So all differences same. So it's AP. Next term is 200-212 = -12. So correct.

So the code would process that as AP.

Another sample: input 1 334 667 1000.

Check AP differences: 334-1=333, 667-334=333, 1000-667=333. So all differences same. Next term is 1000+333=1333. So output is 1333.

So code is correct in those cases.

So the code steps:

Read four integers into a list.

Check for AP:

Check if (b - a) == (c - b) == (d - c). If yes, compute next term as d + (d - c). Output it.

Else, check for GP:

Check all terms are non-zero.

Check if (b * b == a * c) and (c * c == b * d). If yes, then check if the ratio is not 1 (i.e., a != b). Because if a == b, then all terms are same (since it's a GP with ratio 1), which is invalid.

If all conditions met, compute next term as (d * b) // a. But first check if (d * b) is divisible by a. If yes, output next term. Else, output 42.

If GP checks are not met, output 42.

But wait, when checking for ratio !=1, the code can check whether (b/a) is not 1. But since in code, the ratio is (b/a), which can be a fraction. For example, if a=2, b=4, then ratio is 2. So the ratio is not 1. So the code can check if a != b. Because if a == b, then all terms would be same (since ratio is 1), but that's invalid.

Wait, but in a GP with a=3, b=3, ratio is 1. So a == b. So the code must check that the ratio is not 1. But how?

Because in the GP check, after checking the cross products (b² = a c and c² = b d), then the ratio is (b/a). But to check if the ratio is 1, we can check if b == a. Because in that case, if a = b, then the ratio is 1. But the problem says that the ratio cannot be 1. So even if the four terms form a GP with ratio 1, it's invalid. So in such a case, the code must not consider it a GP.

But in that case, since all terms are same (a = b = c = d), the code would have passed the AP check. Because the differences between terms are zero, which is an AP. So the AP code would have been triggered first.

So when the code checks for GP, it's only after the AP check has failed. So, if the code is checking GP, and a == b, then (b² == a c) → a² = a c → c = a. Similarly, (c² = b d) → a² = a d → d = a. So all terms are a. But this is a GP with ratio 1. But since the code checks for GP after AP, and in this case, the AP check would have succeeded (differences are zero), so the code would have output the next term as a. So the GP code is only reached if the AP check failed, which would not be the case here.

So in code, when checking GP, a == b implies that ratio is 1, which is invalid. So during GP check, the code must ensure that the ratio is not 1, which can be done by checking if a != b.

But how?

For example, if a=2, b=4, c=8, d=16 → ratio is 2. So a != b → ratio is not 1. So valid.

Another example: a=3, b=6, c=12, d=24. So ratio is 2. Valid.

Another example: a=5, b=5. Then in the code, the AP check would have already passed, since all differences are zero.

So during GP check, the code only proceeds if the AP check failed. So in the case where the sequence is all same terms, the AP check is triggered, and GP is not considered.

Therefore, during GP check, after checking the cross products, the code must check that a != b. Because if a == b, then the ratio is 1, which is invalid.

So steps for GP check:

1. All terms are non-zero.

2. Check (b² == a c) and (c² == b d).

3. Check that a != b. Because if a == b, then the ratio is 1, which is invalid.

If all three conditions are met, then proceed to compute next term as (d * b) / a. Check if this is integer.

So in code:

if any of the four numbers is zero: skip.

else:

   if (b*b == a*c) and (c*c == b*d) and (a != b):

       numerator = d * b

       denominator = a

       if denominator ==0: impossible (since a is non-zero)

       if numerator % denominator ==0:

           next_term = numerator // denominator

           print(next_term)

       else:

           print(42)

   else:

       print(42)

But wait, what if a=0? Well, during the GP check, the code first checks that all terms are non-zero. So a can't be zero. So denominator is a, which is non-zero.

So in code:

def is_geometric_progression(a, b, c, d):

    if a ==0 or b ==0 or c ==0 or d ==0:

        return False

    if b*b != a * c:

        return False

    if c*c != b * d:

        return False

    if a == b:

        return False

    return True

If this returns True, then compute next term.

But the code must first check whether the four terms are a GP. Then compute next term as (d * b) // a if possible.

Now, the order of checking AP and GP is important. For example, consider the sequence 1,2,3,4. AP check would pass (difference 1), next term 5. So correct. But if code checked GP first, which would not pass, so code would proceed.

Another example: sequence 2,4,8,16. AP check: differences 2,4,8 → no. So check GP. Which would pass. Compute next term 32.

Another example: 4,2,1,0.5 → but input is four integers, so this can't be part of the input. So code would not process such a case.

Now, code steps:

Read four integers as list.

Check AP:

differences between consecutive terms. All same?

If yes, output last term + difference.

Else:

Check GP:

Check all terms non-zero.

Check cross products (b² == a*c and c² == b*d) and a !=b.

If yes:

Compute next_term = (d * b) / a. Check if divisible.

If divisible, output next_term. Else, output 42.

Else, output 42.

Now, code.

Implementing this in Python.

Read the four integers from input. Let's say:

a, b, c, d = map(int, input().split())

Then check AP:

diff = b - a

if (c - b) == diff and (d - c) == diff:

    print(d + diff)

else:

    # Check GP.

    # Check if any term is zero.

    if a ==0 or b ==0 or c ==0 or d ==0:

        print(42)

    else:

        # Check cross products.

        if (b*b == a * c) and (c*c == b * d) and (a != b):

            numerator = d * b

            denominator = a

            if numerator % denominator ==0:

                print(numerator // denominator)

            else:

                print(42)

        else:

            print(42)

Wait, but what about cases where the cross products are equal but the ratio is 1? For example, a=3, b=3, c=3, d=3. But in this case, the AP check would have passed (differences are zero). So the code would output next term 3. So the code would not even check GP for this case.

Another case: a=2, b=2, c=2, d=2. AP check passes, next term is 2. Output 2.

But for a=2, b=2, c=2, d=3: AP check fails (differences 0,0,1). Then check GP. All terms are non-zero. Check cross products: (2²=2*2 →4=4) and (2²=2*3 →4=6 →false). So GP check fails. So output 42.

Another example: a=1, b=2, c=4, d=8. AP check: differences 1,2,4 → no. GP check:

all terms non-zero. Check (2²=1*4 →4=4) and (4²=2*8 →16=16. a !=b (1 !=2). So yes.

Compute next term: d*b = 8*2=16. denominator a=1. 16//1=16. So output 16.

So code would output 16. Correct.

Another example: a=8, b=4, c=2, d=1. AP check: differences -4, -2, -1 → no. GP check: all non-zero. Check 4²=8*2 →16=16. 2²=4*1 →4=4. a !=b (8 !=4). So yes. Compute next term: d*b=1*4=4. denominator a=8. 4/8=0.5. So 4 mod8 is 4, not zero. So output 42.

Thus code handles this correctly.

So the code seems to handle all cases.

But wait, what about when the GP ratio is a fraction that allows the next term to be integer? Like 4, 2, 1, 0.5. But since input must be four integers, this can't happen. The code will not process such input as the input must have four integers.

So code is correct.

Now, testing edge cases.

Edge case 1: All same terms. Input 5 5 5 5. AP check: differences zero. Output 5.

Edge case 2: Input 0,0,0,0. AP check passes. Output 0. But according to the problem statement, the input is between 1 and 1000. Oh, wait the problem's input constraints say that the four numbers are between 1 and 1000 inclusive. So the input can have zero? Wait, no. Wait the problem says:

"Constraints

Time limit per test: 1.0 seconds

Memory limit per test: 256.0 megabytes

Input Format

The first line contains exactly four integer numbers between 1 and 1000, inclusively."

Wait, the input numbers are between 1 and 1000. So all terms are at least 1. So the code can assume that the input has four integers between 1 and 1000. Therefore, in code, the GP check for zero terms is redundant. Because the input can't have zero.

But wait the problem says:

"Input Format

The first line contains exactly four integer numbers between 1 and 1000, inclusively."

So the input numbers are between 1 and 1000. So in code, the GP check for zero terms is unnecessary, but perhaps the problem's examples include numbers like 836 624 412 200, which are all positive.

But according to the problem statement, the input numbers can be between 1 and 1000. So zero is not allowed. Wait, but the first sample input is 836 624 412 200. All are >= 200. So all are >=1.

Wait, but the problem says the input numbers are between 1 and 1000 inclusive. So in code, the code can assume that all terms are non-zero. So the check for any term being zero in the GP check is redundant. But according to the problem statement, the input numbers are between 1 and 1000. So the code can skip checking for zeros in the GP check.

But wait, the problem statement says: "You will be given a competitive programming problem. Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits."

But according to the problem's Input Format, the four integers are between 1 and 1000 inclusive. So in code, we can assume that all four terms are >=1 and <=1000. So zero is not part of the input. Therefore, in the GP check, there's no need to check for any terms being zero. So the code can skip that check.

Wait, but looking back, the problem says:

"Constraints

The first line contains exactly four integer numbers between 1 and 1000, inclusively."

So the input numbers are 1-1000. So during the GP check, all terms are non-zero. So the code can remove the check for zero terms.

So modifying the code:

Else:

    # Check GP.

    # Since input is 1-1000, terms are non-zero.

    if (b*b == a * c) and (c*c == b * d) and (a != b):

        numerator = d * b

        denominator = a

        if numerator % denominator ==0:

            print(numerator // denominator)

        else:

            print(42)

    else:

        print(42)

But this depends on the input constraints. Because according to the problem statement, the input is four integers between 1 and 1000, so they can't be zero. So the code can skip the check for zero.

So the code becomes:

Read a, b, c, d.

Check if AP. If yes, output next term.

Else:

   Check if (b^2 == a*c) and (c^2 == b*d) and (a !=b). If yes:

       compute next term as (d*b) //a, but check divisibility first.

       if divisible, output else 42.

   else:

       output 42.

This simplifies the code.

But wait, let's recheck the problem statement's input constraints. The problem says: "exactly four integer numbers between 1 and 1000, inclusively." So all four numbers are between 1 and 1000. So all are >=1, no zero.

So in code, the code can proceed without checking for zero terms in the GP check.

Thus, code can be written as:

a, b, c, d = map(int, input().split())

# Check AP

diff = b - a

if (c - b) == diff and (d - c) == diff:

    print(d + diff)

else:

    # Check GP

    if (b*b == a * c) and (c*c == b * d) and (a != b):

        numerator = d * b

        denominator = a

        if numerator % denominator == 0:

            print(numerator // denominator)

        else:

            print(42)

    else:

        print(42)

But wait, in the GP check, the code has to check that the ratio is not 1. The code checks that a !=b. Because if a ==b, then the ratio is 1, which is invalid. But in that case, since the code is in the else block (AP check failed), if a ==b, then the first two terms are same, but if the AP check failed, then the next terms must not be same. For example:

If the four terms are 5,5,5,6. Then AP check would fail (differences 0,0,1). Then GP check: (5^2 ==5*5 → yes), (5^2 ==5*6 →25=30? No. So GP check fails. So code outputs 42.

But if a ==b, and the GP conditions are met, then a ==b implies ratio is 1. So the code checks (a !=b) in the GP condition. So the code is correct.

So with this code, all cases are handled.

Testing the first sample input:

836 624 412 200 → AP check:

diff = 624-836 = -212.

Check c -b: 412-624= -212. d-c=200-412= -212. All same. So output 200-212= -12.

Second sample input:

1 334 667 1000 → AP check: differences 333, 333, 333. So output 1000+333=1333.

Another test case: input 2 4 8 16 → GP check.

AP check: differences 2,4,8 → not same. So proceed to GP check.

Check b²=4²=16. a*c=2*8=16. So first condition holds. c²=8^2=64. b*d=4*16=64. So second condition holds. a=2, b=4. a !=b. So yes.

numerator =16*4=64. denominator=2. 64%2=0. So output 32.

Another test case: 8,4,2,1. Input can't have 1 (as per the problem's input constraints?), wait no. The input can be 1 to 1000. So 8,4,2,1 are all between 1 and 1000. So code processes them.

AP check: differences are -4, -2, -1 → no. GP check:

b²=4²=16. a*c=8*2=16. Yes. c²=2²=4. b*d=4*1=4. Yes. a=8 !=b=4. So yes.

numerator=1*4=4. denominator=8. 4%8=4. So not divisible. Output 42.

Which is correct.

Another test case: 3,6,12,24. AP check: differences 3,6,12 → no. GP check: 6²=3*12 →36=36. 12²=6*24 →144=144. a=3, b=6. a !=b. So yes. next term is (24 *6)/3 → 144/3=48. Output 48.

So code is correct.

Another test case: 1,2,4,8. AP check fails. GP check: 2²=1*4 → yes. 4²=2*8 →16=16. a=1 !=b=2. So yes. next term: 8 *2=16. denominator 1. 16/1=16. Output 16.

Another test case: 1,3,9,27. AP check no. GP yes. next term 81.

Another case: 5, 10, 20, 40. AP check no. GP yes. next term 80.

So code handles all these cases.

Thus, the code seems correct.
</think>

```python
a, b, c, d = map(int, input().split())

# Check arithmetic progression
diff = b - a
if (c - b) == diff and (d - c) == diff:
    print(d + diff)
else:
    # Check geometric progression
    if b * b == a * c and c * c == b * d and a != b:
        numerator = d * b
        denominator = a
        if numerator % denominator == 0:
            print(numerator // denominator)
        else:
            print(42)
    else:
        print(42)
```