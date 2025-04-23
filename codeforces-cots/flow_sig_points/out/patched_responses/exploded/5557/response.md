<think>
Okay, I need to solve this problem where I have to find all pairs (n, m) such that the total number of squares in an n x m grid is exactly x. Let's think about how to approach this.

First, I remember that the formula for the number of squares in an n x m grid (assuming n ≤ m) is the sum for k from 1 to n of (n - k + 1) * (m - k + 1). Because for each square of size k x k, there are (n - k + 1) possible rows and (m - k + 1) possible columns. But if n is not the smaller dimension, then we can swap n and m. So the pairs are ordered, but the problem considers (n, m) and (m, n) as distinct unless n equals m. But the output requires them to be ordered with increasing n and then m, so in the solution, when we find a pair (a, b) where a ≤ b, we also include (b, a) unless a == b.

Wait, but how do we compute this efficiently for large x (up to 1e18)? Brute force is impossible here because x can be really big. So we need a mathematical approach to find all possible (n, m) pairs that satisfy the sum equal to x.

Let's first consider the case where n <= m. For this case, the sum is sum_{k=1 to n} (n -k +1)(m -k +1) = x. Let's let a = n, then m >= a, and we can compute the sum as sum_{k=1 to a} (a -k +1)(m -k +1). Let's substitute d = a -k +1. Wait, maybe another substitution. Let's change the variable. Let k run from 1 to a. Let i = k-1. Then k = i+1. So the term becomes (a - (i+1) +1) * (m - (i+1) +1) = (a -i) * (m -i). The sum from i=0 to a-1 of (a -i) * (m -i). Hmm. Not sure if that's helpful.

Alternatively, for a given a (n = a), the sum can be written as sum_{d=1 to a} d * ( (m - (a - d) ) ), where d is (a -k +1) when k ranges from 1 to a. Wait, when k=1, d = a. When k=2, d = a-1. So d runs from 1 to a. Then for each d, the term is d * (m - (a - d) + 1 -1 +1)? Wait, maybe I'm getting confused here.

Wait, when k is the side length of the square, then the number of squares in that size is (a -k +1) * (m -k +1). But m >= a. So for each k from 1 to a, the term is (a -k +1) * (m -k +1). Let's make a substitution of i = k-1. So for i from 0 to a-1, the term is (a - i) * (m -i). Sum from i=0 to a-1: (a -i)(m -i) = sum_{i=0}^{a-1} (a m - (a + m)i + i²). But this might not help directly. 

Alternatively, the sum can be written as sum_{k=1}^a (a -k +1) * (m -k +1) = sum_{k=1}^a (a -k +1) * (m -k +1). Let's make t = a -k +1. Then when k = 1, t = a. When k = a, t = 1. So the sum becomes sum_{t=1}^a t * (m - (a - t +1) +1) = sum_{t=1}^a t * (m - a + t). Because when k = a - t +1, then m -k +1 = m - (a - t +1) +1 = m - a + t. So the sum is sum_{t=1}^a t*(m -a + t) = sum t*( (m -a) + t ) = (m -a) sum t + sum t². The sum of t from 1 to a is a(a+1)/2, and the sum of t² is a(a+1)(2a+1)/6. So the total sum is (m -a) * a(a+1)/2 + a(a+1)(2a+1)/6. 

So the total sum S for n=a and m >= a is equal to:

S = (m -a) * (a(a+1)/2) + (a(a+1)(2a+1))/6

So, setting S = x, we can solve for m in terms of a. Let's rearrange the equation:

(m -a) * (a(a+1)/2) = x - (a(a+1)(2a+1)/6)

So m -a = [ 2 (x - (a(a+1)(2a+1)/6 )) ] / [ a(a+1) ]

Then m = a + [ 2 (x - term) ] / [ a(a+1) ]

But m has to be >=a (since we assumed n <= m, so a is n and m is the larger or equal dimension). Also, the expression on the right must be an integer, and the denominator must divide the numerator.

So for a given a, compute the term (a(a+1)(2a+1))/6. Then check if x >= term. If not, then there's no solution for this a. If yes, then compute the numerator as 2*(x - term). The denominator is a*(a+1). The numerator must be divisible by the denominator. Let's denote this numerator divided by denominator as d. Then m = a + d. But since m must be >=a, then d must be >=0.

Wait, but in this case, m = a + (2 (x - term)) / (a(a+1)). For this to be possible, 2*(x - term) must be non-negative and divisible by a(a+1). Also, after computing m, we need to check that m >= a, which would be the case since d is non-negative.

So the approach is:

1. Enumerate possible a (n) values, for each a, compute term = a(a+1)(2a+1)/6. If term > x, then no solution for this a. Otherwise, compute the numerator as 2*(x - term), denominator is a*(a+1). Check if numerator is divisible by denominator. If yes, then d = (numerator) / denominator. Then m = a + d. But since m must be >= a, but d can be zero or positive. Wait, but if d is negative, that would imply m <a, which is invalid, but since term is the sum when m=a (since when m =a, the sum is a(a+1)(2a+1)/6 + (a -a)* ... which is zero, so term is the sum when m =a. So when m =a, sum is term. So if x = term, then m must be a. Then in that case, d would be zero, and m =a. So that's valid.

So for a given a, the possible m's are those where m = a + d, where d is a non-negative integer such that 2*(x - term) must be equal to a*(a+1)*d, and x >= term. So:

We can compute d = (2*(x - term)) / (a*(a+1)), and if this is an integer, then m = a + d. Also, d must be >=0. Then (a, m) is a valid pair, and since m >=a, we can then add (a, m) and (m, a) unless a =m, which would be the case when d=0 (since m =a +0 =a). 

So the steps are:

Loop through possible a's. For each a:

- Compute term = a(a+1)(2a+1)/6. If term >x, then break (since for higher a's, term would be even larger, since a is increasing, so once term exceeds x, no need to check larger a's).

Wait, but a can't be larger than the cube root of 6x, perhaps. Let's see: term is approximately (a^3)/3 when a is large. So term <=x implies a^3 <=3x, so a <= cube_root(3x). So for x up to 1e18, cube root is up to 1e6 (since (1e6)^3 is 1e18, so cube_root(3e18) is around 1.44e6). So the maximum a we need to check is up to cube_root(6x) or something. But even if x is 1e18, cube_root(6*1e18) is cube_root(6)*1e6 ≈ 1.817e6, which is manageable. So the loop over a can run up to around 2e6 for x up to 1e18, which is feasible.

But how do I compute the upper bound for a? Let's find the maximum a where term <=x. So term = a(a+1)(2a+1)/6 <=x. The maximum a is when a^3 ~ 3x. So for x up to 1e18, a could be up to around 1e6. So iterating a from 1 up to that upper limit is feasible.

So the steps are:

1. Precompute all possible a's up to cube_root(6x) (but compute a until term exceeds x, then break). For each a:

   a. Compute term = a(a+1)(2a+1)//6.

   b. If term >x, break the loop. Because as a increases, term increases.

   c. Else, compute delta =x - term. If delta <0, skip.

   d. Compute numerator = 2*delta. denominator =a*(a+1). So d must be numerator / denominator.

   e. If numerator is divisible by denominator and d >=0:

      i. Then m = a +d. Since m >=a, and d is >=0.

      ii. Check if m >=a (since d is non-negative, this is automatically true).

      iii. Then the pair (a, m) is valid.

      iv. Also, if m !=a, then add (m, a) as another pair. But wait, the problem requires all pairs (n, m) where the sum equals x. So in the case when a <=m, the pair (a, m) is one solution, and (m, a) is another solution unless a=m.

      Wait, but in our approach, when a <=m, but m >=a, then the pair (a, m) is considered when a is the smaller dimension. But for the pair (m, a), when m >a, then when a is the smaller dimension (since m is larger than a), so when processing a, we have m =a +d. But then when we process a'=m, then that may not generate the same pair. Or perhaps not. So maybe the way to generate all possible pairs is to process all a's (from 1 to upper limit), compute m for each a, then collect (a, m) and (m, a) if a !=m.

Wait, but when a is the smaller dimension, the pair (a, m) is one solution. Then (m, a) is another solution only if the sum for m x a grid is also x. But in that case, if (m, a) is a valid pair, then when a' = a, m' =m, but a' must be the smaller dimension. So for (m, a) to be valid, m must be <= a. But since m >=a (from the initial condition), this can only happen if m ==a. So in this case, (a, m) and (m, a) are the same pair. So, perhaps the correct approach is that when (a, m) is a valid pair with a <=m, then (m, a) is also a valid pair only if m <= a. But m >=a by construction, so m <=a implies m =a. So the only time when (a, m) and (m, a) are both valid is when a =m.

Wait, this is confusing. Let's think differently. The sum for (a, m) and (m, a) is the same. Because the formula for the sum is symmetric in n and m. For example, if n=3 and m=5, the sum is 26. If n=5 and m=3, the sum is the same. Because for each square size k, the number is (n -k +1)(m -k +1) regardless of which is larger. So if (a, m) is a valid pair with a <=m, then (m, a) is also a valid pair. Therefore, when we find (a, m) with a <=m, we can add both (a, m) and (m, a) to the list unless a ==m. But in the code, when processing a, we find m >=a, so (a, m) is a valid pair. Then (m, a) is another valid pair. So the code needs to add both when a !=m.

Wait, no. Because when a is processed, and m is found to be a +d (>=a), then (a, m) is a solution. But (m, a) would be a solution only if when you process a'=a, and compute m'=a, but that's not how the code is structured. Because when a'=m, which is larger than a, the code for a' would not process that. Because the code loops a from 1 up to the maximum possible, but if a' is m and m is larger than a, then when the code reaches a' in the loop, it will process it. So perhaps the code would find both (a, m) and (m, a) in different iterations.

But this might not be the case. For example, in the first test case input 26, the valid pairs include (3,5) and (5,3). How do they get generated?

Let's see: when a=3, term =3*4*7 /6 = 84/6=14. So delta=26-14=12. numerator=24. denominator=3*4=12. 24/12=2. So m=3+2=5. So (3,5) is added. Then when a=5, term is 5*6*11/6=5*11=55. Which is larger than 26. So a=5 is not processed. So the code would not process a=5. But (5,3) would be generated because when a=3, m=5, and since 5>3, the code adds (3,5) and (5,3). Wait, no. Wait, the code for a=3 generates (3,5). Then, the code should also add (5,3) if possible.

But according to the formula, when a=3 and m=5 is found, the sum is x. Then the sum for m=5 and a=3 (but wait, no, when you swap them, n=5 and m=3. Then the sum is the same as (3,5). So (5,3) is also a valid pair. So in the code, when we find (a, m) with a <m, we need to add both (a, m) and (m, a) to the list. So in the code, after finding a pair (a, m) where a <m, we add two entries. If a ==m, add one.

So in the code, for each a, when we compute m as a +d, and if m >=a, then:

- If m >a, then add (a, m) and (m, a) to the list.

- If m ==a, add (a, a) once.

But how do we generate (m, a) when m is larger than a? Because for m, when the code processes a' =m, it may not generate a solution. But perhaps when a is the initial a, and the code finds m, then (m, a) is a solution, but the code needs to check if (m, a) is a valid pair. But the code would not process a' =m unless m is <= cube_root(3x). So how do we ensure that all possible pairs are covered.

Alternatively, perhaps the approach is to generate all (a, m) pairs where a <=m, and for each such pair, include (a, m) and (m, a) unless a ==m. But how do I generate those pairs where a >m, but they are valid? Because in those cases, when a >m, the code would have processed the m as the a in the loop, leading to the same (m, a) pair.

For example, the pair (5,3) is the same as (3,5) in terms of sum. So when a=3 is processed, and m=5 is found, the code adds (3,5) and (5,3). But when a=5 is processed, the term is 5*6*11/6 = 55, which is larger than 26, so no solution.

So the code can generate all pairs by considering each a in 1..max_a, and for each valid (a, m) found (a <=m), add both (a, m) and (m, a) unless a ==m. Wait, but how can (m, a) be a valid pair when m >a? Because when m >a, then m is a possible a' in the loop. So when a' =a2, the code would process m' =a2 +d. But for a'=m, which is larger than the max_a (since a'=m is larger than a, but a was already up to max_a). So perhaps the code needs to add both (a, m) and (m, a) when a <m, but only if m is allowed.

But in reality, the sum is symmetric. So for any pair (n, m), the sum is equal to (m, n). So if (a, m) is a valid pair, then (m, a) is also valid. So in the code, for each a, when we find a valid (a, m) with a <=m, we can add (a, m) to the list. Then, if a !=m, also add (m, a). However, this would generate duplicates if the code processes a'=m and finds m'=a. So to avoid that, perhaps in the code, we can collect all pairs (a, m) with a <=m, and then for each such pair, if a !=m, also add (m, a) to the list.

Wait, but that approach would cause duplicates. For example, if (3,5) is added when a=3, then (5,3) is added as well. But when the code processes a=5, since the term for a=5 is 55 (for x=26), which is larger than x, the code does not process a=5. So the code would generate (3,5) and (5,3) as two separate pairs. Then, when collecting all pairs, they would be included. Then, in the output, we need to print all pairs sorted by n then m.

So the code would need to collect all possible (a, m) pairs where a <=m, and also (m, a) if a !=m. But how to avoid processing a=m cases and duplicates.

Alternatively, perhaps the code should generate all possible (a, m) pairs where a <=m, then add (a, m) and (m, a) if a !=m. But this approach would generate (m, a) pairs which may not have a <=m. So perhaps the code should collect all (a, m) pairs where a <=m, then for each such pair, add (a, m) to the list, and if a !=m, add (m, a) to the list. Then, when all such pairs are collected, the list will have all possible pairs, but in the end, we need to sort them by n then m.

Wait, but in the first sample input, the pairs generated when a=1 would be (1,26) and (26,1). When a=2, (2,9) and (9,2). When a=3, (3,5) and (5,3). Then a=5 would not generate anything because term is 55>26. So the total pairs are 6. Which matches the sample.

So the approach is:

- For each a from 1 to max_a:

   - Compute term. If term >x, break.

   - Compute delta =x - term. If delta <0, skip.

   - Compute d = 2*delta / (a*(a+1)). If 2*delta is not divisible by a*(a+1), then skip.

   - Then m =a +d. Check if m >=a (since d is non-negative). Because delta can be 0, leading to m=a.

   - If m >=a, then (a, m) is a valid pair. Now:

      - If a ==m, add (a, m) once.

      - Else, add (a, m) and (m, a).

But wait, when a=3 and m=5, adding both (3,5) and (5,3) even though a=5 may not be processed (since term would be higher than x). So the code should add both pairs even if m is larger than the current a's max.

But in the code's loop, when a is 3, m=5 is found, so (3,5) and (5,3) are added. Then when a increases to 5, the term is 5*6*11//6 = (5*6*11)/6 = 5*11 =55 >26. So the loop breaks. So the code will have added all possible pairs.

So the code can proceed as:

Collect all pairs (a, m) where a <=m and the sum is x. Then for each such pair, add (a, m) and (m, a) if a !=m.

But how to avoid duplicates when a and m are swapped. For example, when processing a=3 and m=5, adding (3,5) and (5,3). Then when processing a=5 and m=3 (if possible), but in that case, the code would process a=5, but m would be a +d, which would have to be >=5, which can't be 3. So the code would not generate (5,3) again. So the code's method of generating both pairs when a <m is correct.

So the code can proceed by:

Initialize a list.

For each a in 1..max_a:

   compute term = a*(a+1)*(2a+1)//6.

   if term >x: break.

   delta =x - term.

   if delta <0: continue.

   numerator = 2*delta.

   denominator =a*(a+1).

   if numerator % denominator !=0: continue.

   d = numerator // denominator.

   m =a +d.

   if m <a: continue (since m must be >=a).

   then the sum for a and m is x.

   add (a, m) to the list.

   if a !=m: add (m, a) to the list.

But wait, adding (m, a) would add a pair where the first element is m and the second is a, which could have m >a. For example, when a=3 and m=5, adding (5,3) as a pair. Then when processing a=3, m=5 is allowed. Then (5,3) is added. But when the code processes a=5, m=5 would have term 55 >26, so no pairs added. So the code correctly adds (3,5) and (5,3) when a=3.

But this approach would add pairs (m, a) where m is larger than a. But when the code processes a' =m, which is larger than the current a, but in the loop, a is increasing. Once a exceeds cube_root(3x), the loop breaks. So the code would add (m, a) even if m is larger than the current a's maximum. But since the code breaks the loop once term exceeds x, the code may miss some pairs where a is larger than the max_a computed, but m is small.

Wait, this is a problem. For example, consider a pair (m, a) where m is large (but a is small). How do we capture that? For example, in the sample input x=26, the pair (26,1) is present. How is this generated?

Let's see:

For a=1:

term =1*2*3//6 =6//6=1.

delta=26-1=25.

numerator=50.

denominator=1*2=2.

50 /2 =25. So d=25. m=1+25=26. So (1,26) is added, and (26,1) is added.

So for a=1, the code adds (1,26) and (26,1). So even though 26 is larger than the cube_root(3*26)= cube_root(78) ~4, the code can process a=1 and generate m=26. So this is handled correctly.

But when a=26 is processed, the term is 26*27*53//6. Let's compute that:

26*27 = 702. 702 *53 = 37206. 37206 /6= 6201. Which is way larger than x=26. So the loop for a=1 to max_a would break after a=3 (since for a=3, term=14; for a=4: term=4*5*9//6= 180//6=30>26, so break). So the code would process a up to 3, but also a=1,2,3.

So the code correctly captures (1,26) and (26,1) when a=1.

Thus, the code's approach of processing all a's up to the maximum possible (where term <=x) and generating all possible pairs (a, m) and (m, a) when a !=m is correct.

But how to avoid duplicate pairs. For example, when a=3, m=5, we add (3,5) and (5,3). Then when a=5, which is larger than max_a, the code does not process it, so no duplicate pairs are added.

So the code can proceed as follows:

- Iterate a from 1 to a_max, where a_max is the maximum a such that term <=x. Compute a_max as the maximum a where a(a+1)(2a+1)/6 <=x.

But to compute a_max, we can use binary search. For example, find the largest a where a^3 <=3x. But since x can be up to 1e18, a can be up to about 1e6. So even iterating a up to 2e6 is feasible. So perhaps in the code, we can loop a from 1 to a_max, which is found by incrementing a until term exceeds x.

So in code:

x = int(input())

res = set()

a = 1

while True:

    term = a * (a +1) * (2*a +1) //6

    if term > x:

        break

    delta = x - term

    if delta <0:

        a +=1

        continue

    numerator = 2 * delta

    denominator = a * (a+1)

    if denominator ==0:

        a +=1

        continue

    if numerator % denominator !=0:

        a +=1

        continue

    d = numerator // denominator

    m = a + d

    if m <a:

        a +=1

        continue

    res.add( (a, m) )

    if a != m:

        res.add( (m, a) )

    a +=1

But wait, this code loops a starting from 1 and increments by 1 each time. But when a is 1, 2, 3, etc. For x=26, a=1, term=1. Then a=2: term=2*3*5//6=30//6=5. a=3:3*4*7//6=84//6=14. a=4:4*5*9//6= 180//6=30>26. So the loop breaks. So a runs 1,2,3.

For each a, compute m. For a=1, delta=25. numerator=50. denominator=2. 50/2=25. m=26. So add (1,26) and (26,1).

For a=2: term=5. delta=21. numerator=42. denominator=2*3=6. 42/6=7. m=2+7=9. So add (2,9) and (9,2).

For a=3: term=14. delta=12. numerator=24. denominator=3*4=12. 24/12=2. m=3+2=5. Add (3,5) and (5,3).

Then a=4 is processed. term=30>26, loop breaks.

So the res set includes (1,26), (26,1), (2,9), (9,2), (3,5), (5,3). Then there's another case: when m =a. For example, x=2.

Sample input 2: x=2. Output is 2 pairs: (1,2) and (2,1).

Let's see. For a=1:

term=1*2*3//6=1. delta=1. numerator=2. denominator=2. d=1. m=1+1=2. So (1,2) and (2,1) are added.

a=2: term=2*3*5//6=30//6=5>2. So loop breaks.

Thus, the code would collect those pairs.

Another sample: x=8. The output is 4 pairs: (1,8), (8,1), (2,3), (3,2).

For a=1:

term=1. delta=7. numerator=14. denominator=2. 14/2=7. m=8. Add (1,8) and (8,1).

a=2: term=5. delta=3. numerator=6. denominator=6. 6/6=1. m=2+1=3. Add (2,3) and (3,2).

a=3: term=14>8. Loop breaks.

So code works.

But now, after collecting all possible pairs, the code must sort them in the order of increasing n and then m. So the code can collect all the pairs in a set (to avoid duplicates), then sort them as per the problem's requirement.

Wait, but in the code above, when a=3 and m=5, the code adds (3,5) and (5,3). Then when processing a=5, which is beyond the loop's limit, the code does nothing. But when processing a=5, if term is too large, the code would not process. So there's no possibility of duplicate pairs. Thus, the set 'res' will have all unique pairs.

Once all a's are processed, the code needs to output the number of pairs, followed by the pairs sorted by n, then m.

So the code can collect all the pairs in a list, sort them, and then output.

But since the code uses a set, the pairs are stored in arbitrary order, but when converted to a list, they can be sorted.

So in code:

sorted_pairs = sorted(res)

But the pairs are tuples (n, m). The sorting key is first n, then m.

But when the code adds (a, m) and (m, a) when a !=m, these pairs would be in the set. For example, (3,5) and (5,3) are two distinct pairs and will be present in the set.

Thus, the code's approach is correct.

But now, there's another possible case: when m is computed as a +d, but m is less than a. But since d is non-negative, m can't be less than a. So that check is redundant.

But in the code, after computing m =a +d, since d is non-negative (because delta is non-negative, and denominator is positive), m is always >=a.

Thus, the code can skip the check m >=a.

Thus, in code:

...

m = a +d

res.add( (a, m) )

if a !=m:

    res.add( (m, a) )

...

Thus, the code can be optimized.

Another thing to consider is that the code may generate (a, m) where a >m. For example, when adding (m, a) where m is larger than a. Wait, no. For example, when a=3 and m=5, adding (3,5) and (5,3). The pair (5,3) has a=5 and m=3. But in the code, when a is 5, the term is 5*6*11//6=55>26 (if x=26). So the code breaks the loop. Thus, the code will only generate (5,3) when a=3, but when a=5 is processed, nothing is added. So the code correctly adds all pairs.

Now, the code's code:

But in Python, the code may have a problem with a being up to 1e6, which for x=1e18, a_max is about 1e6. So looping up to a_max is acceptable.

But wait, for x=1e18, a_max is about cube_root(6x). Let's compute cube_root(6 *1e18) = cube_root(6e18) ≈ 1.817e6. So the loop would run 1.8e6 times. Each iteration is O(1). For Python, 1e6 iterations are manageable in the given time limit (2 seconds). So this approach should be feasible.

So the code is:

Read x.

Initialize a set to hold the pairs.

Initialize a=1.

Loop:

   compute term.

   if term >x, break.

   compute delta.

   compute numerator and denominator.

   check if divisible.

   compute d.

   compute m.

   add (a, m) and (m, a) if a !=m.

   increment a by 1.

Once loop is done, sort the pairs in the set.

Print the count and the pairs.

Now, let's test some edge cases.

Test case x=1.

The sum must be 1. Only possible when n=1 and m=1. The sum is 1*1=1.

So output is 1 pair (1,1). 

But according to the code:

a=1:

term=1*2*3//6=6//6=1. delta=0. numerator=0. denominator=2. 0%2=0. d=0. m=1+0=1.

Add (1,1) once.

Then a=2: term=2*3*5//6=30//6=5>1. Loop breaks.

So code outputs [(1,1)] → correct.

Another test case x=2. The output is two pairs (1,2) and (2,1). The code correctly adds both.

Another edge case: x=3. Let's see. What pairs are possible?

Possible pairs:

Looking for (n, m) where sum of squares is 3.

Let's see:

If n=1, m=3. The sum is 3 squares of 1x1. So yes.

If n=2, m=2: sum is 2x2 for k=1 →4 squares. Which is larger than 3.

So possible pairs are (1,3) and (3,1).

Wait, but let's compute.

For a=1:

term=1. delta=3-1=2. numerator=4. denominator=2. 4/2=2. m=1+2=3. So add (1,3) and (3,1).

a=2: term=5>3. So loop breaks. So code outputs two pairs. So for x=3, output is 2 pairs: (1,3) and (3,1).

Yes.

But according to the code:

delta =3-1=2. numerator=4, denominator=2 →d=2. m=3. So adds (1,3) and (3,1). Correct.

Now, let's proceed to implement the code.

But in code, the set is used to collect all pairs, which ensures that there are no duplicates. For example, if a=2 and m=2 (if x=5), then adding (2,2) once.

So the code is correct.

Now, let's code this.

But in Python, the code must read x, loop a from 1 upwards until term >x. For each a, compute term. Then compute delta, check, etc.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    x = int(input_stream.readline().rstrip("\n"))

    result = set()

    a = 1

    while True:

        term = a * (a + 1) * (2 * a + 1) // 6

        if term > x:

            break

        delta = x - term

        if delta < 0:

            a += 1

            continue

        denominator = a * (a + 1)

        if denominator == 0:

            a += 1

            continue

        numerator = 2 * delta

        if numerator % denominator != 0:

            a += 1

            continue

        d = numerator // denominator

        m = a + d

        # m must be >= a, which it is since d >=0

        result.add( (a, m) )

        if a != m:

            result.add( (m, a) )

        a += 1

    sorted_pairs = sorted(result)

    print(len(sorted_pairs), file=output_stream)

    for pair in sorted_pairs:

        print(pair[0], pair[1], file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
""",
            "output": \
"""\
2
1 2
2 1
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

Thus, the code should be correct.
</think>

```python
x = int(input())
result = set()
a = 1

while True:
    term = a * (a + 1) * (2 * a + 1) // 6
    if term > x:
        break
    delta = x - term
    if delta >= 0:
        denominator = a * (a + 1)
        numerator = 2 * delta
        if denominator != 0 and numerator % denominator == 0:
            d = numerator // denominator
            m = a + d
            result.add((a, m))
            if a != m:
                result.add((m, a))
    a += 1

sorted_pairs = sorted(result)
print(len(sorted_pairs))
for pair in sorted_pairs:
    print(pair[0], pair[1])
```
