<think>
Okay, I need to solve this problem where I have to find the fraction a/b that's closest to x/y, with b ≤ n. And if there are multiple fractions with the same minimal difference, choose the smallest denominator first, then the smallest numerator. 

Let me start by understanding the problem. The input is x, y, n. So for each possible denominator b from 1 to n, I need to find the best a such that a/b is as close as possible to x/y. Then compare all these possibilities to find the best one.

But checking every possible denominator up to n (which can be 1e5) might be computationally feasible, but how do I find the optimal a for each b efficiently?

For a given b, the closest a is the integer that's closest to (x/y)*b. Since a has to be non-negative. So for each b, compute a = round((x*b)/y). But since (x*b)/y might not be an integer, perhaps floor or ceiling? Wait, the optimal a is the one that makes a/b as close as possible to x/y. So for each b, the best a is either floor((x*b)/y) or ceil((x*b)/y), whichever gives a closer value.

Wait, but how to compute that correctly? Let's see. For a given b, the ideal a would be (x * b) / y. Since a must be an integer, we can take the integer closest to this value, which could be either floor or ceiling, depending on the fractional part. But a can't be negative, so if (x*b)/y is less than zero, but since x and y are positive, x/y is positive, so x*b/y is positive, so a is non-negative.

So for each b in 1 to n, compute the a that is closest to x/y * b. Then compute the absolute difference between a/b and x/y, and track the minimum difference. Also, when differences are equal, select the one with the smallest b, then smallest a.

But doing this for all b up to 1e5 might be O(n), which is acceptable since 1e5 operations are manageable in Python within the time limit. But wait, maybe there's a smarter way. Because 1e5 iterations are manageable. Let's think: each iteration would compute a for a given b, check the difference, and compare with the current best.

But wait, for each b from 1 to n, calculate the optimal a. Then compute the difference. Then track the best a/b pair.

So steps:

1. Iterate b from 1 to n.

2. For each b, compute a as the integer closest to (x*b)/y. Since a must be non-negative. So a = round(x*b / y). But since x, y, b are integers, maybe using integer division with some checks.

Wait, but how to compute the a that gives the minimal difference.

Let me think: for a given b, the best a is the one that minimizes | (a/b) - (x/y) |. Let's rewrite the difference:

| (a y - x b) / (b y) |. Since the denominator is the same for a given b, the minimal absolute numerator (|a y - x b|) gives the minimal difference.

So for each b, find a such that a y is as close as possible to x b. Because the denominator (b y) is fixed, the numerator's absolute value (|a y - x b|) determines the difference. So for each b, the a that minimizes this is the integer a closest to (x b) / y.

But since a must be non-negative, but (x b) is positive (x, b are positive), so a can't be negative here.

So for each b, compute a as the rounded value of (x * b) / y. Wait, but (x*b) may not be exactly divisible by y. So the best a is either floor((x*b)/y) or ceil((x*b)/y). Let's see.

Alternatively, the optimal a is the one that makes a = floor((x*b + y/2)/y), which is like rounding. Wait, perhaps for a given x*b, the closest a is (x*b + y//2) // y. But I need to confirm.

Wait, for example, suppose x=3, y=7, b=5. Then x*b = 15. 15/y is 15/7 ≈2.142. So the closest a is 2. Which gives 2/5. Which is the sample input's correct answer.

So in this case, (3*5 + 7/2) //7 → (15 +3.5) =18.5 → floor(18.5/7) is 2. Correct.

Another example: x=7, y=2, b=4. 7*4=28. 28 / 2 is 14. So a is 14. 14/4=3.5. But 7/2 is 3.5. So difference is zero. So output is 14/4, but wait the sample input 7/2 and n=4. The output is 7/2, which is allowed because denominator 2 is ≤4. Wait, the problem says "find the nearest fraction to x/y whose denominator is no more than n". So in this case, the original fraction is 7/2, which has denominator 2 which is ≤4. So the answer is 7/2. So in this case, when the given x/y is already a valid candidate (b=2 ≤4), then that's the best possible. So the code must check this scenario.

So for each b, compute a as the closest possible. Then compute the difference. But for each b, the best a is either floor((x*b)/y) or ceil((x*b)/y). So perhaps, for each b, compute the a that is the floor or the ceiling of (x*b/y), whichever gives a better approximation.

But since a can't be negative, we can compute a as the maximum between 0 and the floor value. Wait, but x and y are positive, so x*b is positive, so x*b/y is positive, so a must be at least zero. So a can be zero. But the problem statement says a is a non-negative integer, so yes.

Wait, but the problem requires 1 ≤ b ≤n, and a is non-negative (0 ≤a). So a can be zero. For example, if x/y is very small. So for example, if x=1, y=1000, n=5. Then the best a/b could be 0/1, 0/2, etc. So need to handle a=0.

So the steps for each b:

Compute the ideal a_float = (x * b) / y. Then a can be floor(a_float) or ceil(a_float). Also, check if a_float is an integer. Then the best a is that integer.

But since we want the minimal |a y - x b|, we can compute a_floor = (x*b) // y. Then a_ceil = a_floor +1. Then check which of a_floor or a_ceil gives the minimal difference.

But maybe a_floor is the closest. For example, if x*b/y is 2.3, then a_floor is 2, a_ceil is 3. The difference would be |2y - xb| vs |3y - xb|. Since 2.3 is closer to 2 than 3, a_floor is better. If x*b/y is 2.6, then a_ceil is better.

So for each b, compute a_floor = (x*b) // y. Then a_candidate can be a_floor-1, a_floor, a_floor+1. Wait, but maybe a_floor-1 could be better? For example, when x*b is very close to (a_floor-1)*y. Let me think. Suppose x=1, y=3, b=1. Then x*b/y = 1/3. So a_floor is 0. Then a can be 0 or 1. The difference between 0/1 and 1/3 is 1/3, between 1/1 and 1/3 is 2/3. So 0 is better. So in this case, a_floor is 0, and that's correct.

Another example: x=4, y=3, b=2. Then x*b=8, divided by y=3 is 2.666. So a_floor is 2. Then a_floor is 2, a_ceil is 3. So 2/2 is 1, 3/2 is 1.5. The target is 4/3 ≈1.333. So 3/2 is 1.5, which is 0.1667 away, while 2/2=1 is 0.333 away. So the ceil gives a better result. So in this case, a should be 3.

So the correct approach is for each b, compute a_floor = (x*b) // y. Then check a_floor and a_floor+1. Because a_floor-1 would only be possible if a_floor is at least 1. Wait, but a_floor is (x*b)//y. Since x and b are positive, (x*b) can be zero (if x=0, but according to problem statement x is positive). So x is positive, so x*b is positive, so (x*b)//y is at least zero.

So for each b, the candidates for a are:

a_floor = (x*b) // y

a_ceil = a_floor + 1

But perhaps there's another candidate a_floor -1. For example, when x=1, y=3, b=2. Then x*b=2. So a_floor = 0 (since 2//3 is 0). So a_ceil is 1. The candidates are 0 and 1. But 0/2 is 0, 1/2 is 0.5. The target is 1/3 ≈0.333. So 1/2 is 0.5, which is 0.1667 away. 0 is 0.333 away. So a_ceil gives a better difference. So in this case, a_ceil is better.

So perhaps, for each b, the minimal |a y - x b| is achieved by either a_floor or a_ceil. So for each b, we need to compare the two candidates a_floor and a_ceil, and pick the one with the minimal difference. Then, among those, if there's a tie, pick the smaller a.

Wait, but in the problem statement, when multiple a/b have the same minimal difference, the rules are: first pick the smallest denominator, then the smallest a. Wait, but for a given b, the denominator is fixed. So for each b, we pick the best a for that b, which is either a_floor or a_ceil. Then among all possible b's, select the one with the minimal difference, and in case of ties, the smallest b, then smallest a.

So, for each b, compute the best possible a (either floor or ceil) and calculate the difference, then compare across all b's.

But how do I efficiently compute this for each b?

Let me outline the steps:

Initialize best_a and best_b as None, with a minimal difference of infinity.

For each b in 1 to n:

    target = x * b / y

    a_floor = (x * b) // y

    candidates = [a_floor, a_floor + 1]

    for a in candidates:

        if a <0:

            continue  # a must be non-negative

        current_diff = abs(a*y - x*b)

        # compute the current difference as |a/b - x/y| = current_diff / (b*y)

        # but since comparing current_diff/(b y) between different b's, but since b y is positive, the comparison can be based on current_diff and (b y) inversely. However, this complicates. Alternatively, for each candidate, compute the actual difference as a fraction.

        # but comparing fractions can be done via cross-multiplying. However, for the purpose of selecting the minimal difference, perhaps it's sufficient to track current_diff, and the denominator b.

        # Wait, but the actual difference is current_diff / (y*b). So for comparing two differences (for two different b's), the one with the smaller (current_diff / (y*b)) is better.

        # However, storing current_diff and b allows us to compute this: for two pairs (diff1, b1) and (diff2, b2), the actual difference is (diff1)/(y*b1) vs (diff2)/(y*b2). But since y is the same for all comparisons, we can ignore it. So compare (diff1)/(b1) vs (diff2)/(b2). The smaller one is better.

        # So for each candidate a, compute the key as (diff, b, a), where diff is |a y - x b|. Then, when comparing two candidates, the one with smaller key (diff / b) is better.

        # So, for each candidate a, compute the key = (diff, b, a). Then, the best candidate is the one with the smallest key, where the key is considered as (diff, b, a), and the comparison is first by diff/(b*y), then by b, then a. But since y is fixed, we can ignore it and compare based on (diff / b).

        # So the key for comparison is (diff, b, a), and the order is:

        # 1. the minimal (diff / (b * y)) → same as minimal (diff / b)

        # 2. if equal, smaller b

        # 3. if equal, smaller a

        # So, for each candidate a, compute diff = abs(a * y - x * b). Then, we can represent the 'score' as (diff, b, a). Then, the candidate with the smallest score in lex order (comparing diff, then b, then a) is better.

        # So, for each candidate a (floor and ceil), check if a is non-negative. Then compute the diff. Then compare to the current best.

        # So, for this candidate (a, b):

        # compute the difference metric as (diff, b, a)

        # compare to the current best.

    Then, among the two candidates (a_floor and a_floor+1), select the one with the minimal difference. If they have the same difference, pick the smaller a.

    So for each b, between a_floor and a_floor+1, choose the a that gives the smallest difference. If they are equal, pick the smaller a.

    Then, compare this best a for b with the global best.

Wait, but for a given b, between a_floor and a_floor+1, which one is better? We can compute the difference for both and pick the better one.

But perhaps there's a case where a_floor-1 is better. For example, if x=1, y=4, b=3. Then x*b=3, divided by 4 is 0.75. So a_floor is 0. So a_floor is 0 (0/3), a_floor+1 is 1 (1/3). The target is 0.25. So 0/3 is 0.25 away (0.25), 1/3 is 0.0833 away. So a_floor+1 is better.

Another example: x=5, y=2, b=3. Then x*b=15, divided by y=2 is 7.5. So a_floor is 7. So 7/3 is 2.333, x/y is 2.5. The difference is 0.1667. a_floor+1 is 8/3 ≈2.6667, which is 0.1667 away. So both a_floor and a_floor+1 give the same difference. Then, according to the problem's tiebreaker rules, for the same denominator, choose the smallest a. So in this case, between 7 and 8, the a would be 7. Because 7/3 and 8/3 are equally distant from 5/2 (2.5). So for this b, the best a is 7.

Wait, but how? The difference for a=7 is |7*2 -5*3| = |14-15|=1. For a=8, |16-15|=1. So same difference. So, according to the problem's criteria, for the same b, if two a's have the same difference, the one with the smaller a is chosen. So for each b, among possible a's, select the one with minimal a in case of ties.

So for each b, the candidates are a_floor and a_floor+1. Compute their differences, and pick the a with the minimal difference. If they are equal, pick the smaller a.

So for each b, we can calculate both a_floor and a_floor+1, compute their differences, and pick the best a for that b.

So the steps for each b:

1. Compute a_floor = (x * b) // y.

2. Generate a_floor and a_floor + 1 as candidates. But a_floor+1 may be 0 if a_floor is -1, but since x is positive, a_floor can't be negative. Because x and b are positive, so x*b is positive. Divided by y (positive) gives a positive value, so a_floor is at least 0.

3. For each candidate a in [a_floor, a_floor+1], compute the difference |a * y - x * b|. The a with the smaller difference is better. If they are equal, pick the smaller a.

Then, once we have the best a for this b, compute the difference and compare it with the global best.

But how do we track the global best?

The global best is the pair (a, b) that has the minimal difference. If two pairs have the same difference, choose the one with smaller b. If same difference and same b, choose the smaller a.

So the key to compare is the tuple (difference, b, a). We want the tuple with the smallest lex order.

Wait, but the difference is |a/b - x/y|. To compare two pairs (a1, b1) and (a2, b2), compute their actual differences. The one with the smaller difference is better. If the differences are equal, the one with the smaller b is better. If both are same, the one with smaller a is better.

So the comparison key is (difference, b, a), sorted in ascending order.

But computing the actual difference (as a float) could lead to precision errors. Instead, we can compare the fractions exactly by cross-multiplication. But for the purposes of code, perhaps it's easier to compute the absolute difference of the two fractions.

But to avoid floating points, perhaps we can represent the difference as a pair (dx, dy), where dx is |a y - x b| and dy is b*y. So the actual difference is dx/dy. Comparing two such fractions can be done by comparing dx1 * dy2 vs dx2 * dy1. If dx1 * dy2 < dx2 * dy1, then the first is smaller.

But perhaps, for code purposes, since the problem requires the minimal |(a/b) - (x/y)|, which is equivalent to |(a y - x b)| / (b y). So the actual value is |a y - x b| / (b y). To compare two (a1, b1) and (a2, b2), compare (|a1 y -x b1|) * (b2 y) versus (|a2 y -x b2|) * (b1 y). Since y is positive, we can divide both sides by y, so compare (|a1 y -x b1|)*b2 versus (|a2 y -x b2|)*b1.

But this might be computationally expensive if done for every pair. However, given that n is up to 1e5, and for each b we have two candidates, this approach is feasible.

Alternatively, for each candidate (a, b), compute the difference in terms of (dx, dy) where dx = |a y - x b|, dy = b. Then, when comparing two candidates (dx1, b1) and (dx2, b2), the first is better if dx1 * b2 < dx2 * b1, or if they are equal and b1 is smaller, etc.

Wait, because dx is |a y - x b|, which is the numerator of the difference |a/b - x/y| multiplied by b y. So the actual difference is dx / (b y). So when comparing two differences dx1/(b1 y) and dx2/(b2 y), it's equivalent to comparing dx1 * b2 vs dx2 * b1. If dx1 * b2 < dx2 * b1, then the first is smaller.

Thus, for two candidates (dx1, b1) and (dx2, b2), the first is better if dx1 * b2 < dx2 * b1, or if equal and b1 is smaller, etc.

So in code, for each candidate (a, b), we can compute dx = abs(a * y - x * b). Then, when comparing two candidates, their keys are (dx1, b1, a1) and (dx2, b2, a2). The first candidate is better than the second if:

dx1 * b2 < dx2 * b1 → because dx1/(b1 y) < dx2/(b2 y) → multiply both sides by b1 b2 y (positive), so dx1 b2 < dx2 b1.

If dx1*b2 == dx2*b1, then compare b1 and b2. The smaller b is better. If same b, compare a1 and a2. The smaller a is better.

So the key for comparison can be represented as (dx, b, a), and when comparing two keys key1 and key2, we first compare key1[0] * key2[1] with key2[0] * key1[1]. If key1[0]*key2[1] < key2[0]*key1[1], then key1 is better. If equal, then compare key1[1] (b) versus key2[1]. Then compare a.

So the code needs to track the best (dx, b, a) so far. For each candidate (a, b), compute dx and check if it's better than the current best.

But implementing this comparison could be a bit tedious. So perhaps, for each candidate (a, b), compute dx and then compare it with the current best using the key as described.

So here's the plan:

Initialize best_key as (infinity, infinity, infinity) or None.

For each b in 1 to n:

    a_floor = (x * b) // y

    candidates = [a_floor, a_floor + 1]

    for a in candidates:

        if a <0: continue

        dx = abs(a * y - x * b)

        current_key = (dx, b, a)

        # compare current_key with best_key

        if best_key is None or is_better(current_key, best_key):

            best_key = current_key

        elif current_key and best_key are equal in terms of dx and b, etc.:

            # check if current_key has same dx and b as best_key, then compare a

            # but the comparison is handled in the key's order.

    So the is_better function would return True if current_key is better than best_key.

But how to implement this in code?

An alternative approach is to precompute for all possible b's, the best a, then compute their key, and track the minimal key.

But in Python, how to handle the comparison between two keys.

Alternatively, for each candidate, we can compute the key, and then compare it to the current best. For each candidate (a, b), compute the key as (dx, b, a). The minimal key is the one that comes first in a lexicographical order, but not exactly. Because the primary comparison is based on dx * other.b vs other.dx * this.b. Wait, no. The key is (dx, b, a), but the actual comparison is dx * other.b < other.dx * this.b. So the order is not directly lexicographical.

So perhaps, for each candidate, compute dx and b, and compare with the current best's dx and b using cross multiplication.

So here's the code logic:

Initialize best_dx, best_b, best_a as None.

For each b in 1 to n:

    a_floor = (x * b) // y

    for a in [a_floor, a_floor + 1]:

        if a < 0:

            continue

        dx = abs(a * y - x * b)

        # compare (dx, b, a) with the best so far (best_dx, best_b, best_a)

        if best_dx is None:

            best_dx, best_b, best_a = dx, b, a

        else:

            # compare dx / b with best_dx / best_b

            # which is equivalent to compare dx * best_b vs best_dx * b

            current_val = dx * best_b

            best_val = best_dx * b

            if current_val < best_val:

                # current is better

                best_dx, best_b, best_a = dx, b, a

            elif current_val == best_val:

                # same difference per comparison, check b

                if b < best_b:

                    best_dx, best_b, best_a = dx, b, a

                elif b == best_b:

                    if a < best_a:

                        best_dx, best_b, best_a = dx, b, a

So this way, for each candidate (a, b), compute dx and compare with the current best using cross-multiplication to avoid floating points.

But how about the case where two candidates have the same dx * best_b and best_dx * b, but different b? For example, if dx1 * b2 == dx2 * b1, but b1 != b2. Then we pick the smaller b.

But in the code above, when current_val == best_val (dx * best_b == best_dx * b), then we check if the current b is smaller than the best_b. If yes, update. Else, if same b, check a.

Yes, that's correct.

This approach avoids floating points and uses only integer operations, which is better for precision and speed.

So now, the code steps are:

Read x, y, n.

Handle the case where y is zero? No, since input constraints say y is positive.

Now, for each b in 1 to n:

    a_floor = (x*b) // y

    generate a_floor and a_floor+1 as candidates.

    for each a in these candidates:

        compute dx = abs(a*y - x*b)

        compare with the current best, as per the key.

But wait, when a_floor is (x*b) // y, then a_floor+1 could be (x*b) // y +1. So for example, if (x*b)/y is exactly an integer, then a_floor is that integer, and a_floor+1 is one more, but then dx for a_floor+1 would be y (since (a_floor+1)*y - x*b = y). Which is larger than the dx for a_floor (which is zero). So in that case, the candidate a_floor is better. So in code, for each candidate a, we need to generate a_floor and a_floor+1, but only if they are better.

But in code, even if a_floor is the optimal, generating both and comparing is acceptable. Because for example, if a_floor is the exact value (dx=0), then a_floor+1 will have a larger dx, so when comparing, the code will not select it.

But wait, for example, if a_floor is exactly (x*b)/y, then a_floor is the best possible a. So in that case, a_floor+1 would give a worse dx. So for this case, the code would compare both and select the one with dx=0 (a_floor).

So generating both candidates is safe.

But generating a_floor-1 is not necessary. Let's see: when a_floor is (x*b)//y, then a_floor could be 0. So a_floor-1 would be -1, which is invalid. So in code, we can skip a_floor-1. But for cases where a_floor is positive, is a_floor-1 a possible better candidate?

For example, if x=5, y=2, b=3. Then x*b=15. 15//2=7. So a_floor=7. Then a_floor-1=6. Let's compute dx for a=7 and a=6. 

a=7: dx = |7*2 -5*3|= |14-15|=1.

a=6: dx= |12-15|=3. So a=7 is better. So a_floor-1 is not better.

Another example: x=3, y=7, b=5. Then a_floor=(3*5)//7=2. dx for a=2 is |14-15|=1. a=3 gives dx= |21-15|=6. So a=2 is better.

But wait, perhaps in some cases, a_floor-1 is better. Let me think of such a case.

Suppose x=4, y=7, b=5. Then x*b=20. 20//7=2. So a_floor=2. a_floor-1=1.

dx for a=2: |14-20|=6. 

dx for a=1: |7-20|=13.

So worse. 

Another example: x=5, y=3, b=4. x*b=20. 20//3=6. a_floor=6. dx= |6*3 -5*4| = |18-20|=2. a_floor-1=5: |15-20|=5. Worse. a_floor+1=7: |21-20|=1. So better. So for this case, a_floor+1 is better.

So in this case, a_floor+1 is better. So generating a_floor and a_floor+1 as candidates covers all possible better options.

So the code can generate a_floor and a_floor+1 as candidates, and compare both.

But what if the optimal a is a_floor-1? For example:

x=5, y=2, b=3. Then x*b=15. a_floor=7. a_floor-1=6. But a=7 gives dx=1, a=6 gives dx=3. So no.

Another example: x=1, y=3, b=2. x*b=2. a_floor=0. a_floor+1=1. So a=0 gives dx= |0 -2|=2, a=1 gives dx= |3-2|=1. So better.

Another example: x=2, y=5, b=3. x*b=6. a_floor=1 (6//5=1). a_floor+1=2. a=1: dx= |5-6|=1. a=2: dx=|10-6|=4. So a_floor is better.

So in all these examples, the optimal a is either a_floor or a_floor+1. Hence, generating these two candidates for each b is sufficient.

Thus, the code can proceed by considering a_floor and a_floor+1 for each b.

So the code steps:

Read x, y, n.

Compute the initial best as (dx=infinity, b=0, a=0). Or None.

Loop over each b from 1 to n inclusive.

For each b:

    a_floor = (x*b) // y

    candidates = [a_floor, a_floor + 1]

    for a in candidates:

        compute dx = abs(a * y - x * b)

        compare with the current best.

So in code:

x, y, n = map(int, input().split())

best = None

for b in range(1, n+1):
    a_floor = (x * b) // y
    for delta in [0, 1]:
        a = a_floor + delta
        dx = abs(a * y - x * b)
        # Compare with best
        if best is None:
            best = (dx, b, a)
        else:
            # Compute comparison based on dx * best_b and best_dx * current_b
            current_key = (dx, b, a)
            best_dx, best_b, best_a = best

            # Check if current is better than best
            if dx * best_b < best_dx * b:
                best = current_key
            elif dx * best_b == best_dx * b:
                if b < best_b:
                    best = current_key
                elif b == best_b and a < best_a:
                    best = current_key

So after processing all b's, the best a and b are best[2] and best[1], respectively.

But wait, the code in the loop for delta in [0, 1], which represents a_floor and a_floor+1.

But what if a_floor+1 is a negative number? For example, if a_floor is (x*b)//y, which is 0, and delta is 1, then a becomes 1, which is positive. So no problem.

Wait, x is positive, y is positive. x*b is positive, so (x*b)//y is non-negative. So a_floor is >=0. So a_floor+1 >=0 +0 or 1. So a is always non-negative.

So the code doesn't need to check for a <0.

So this covers all possible candidates.

But wait, what if a_floor is 0 and delta is 0, then a=0. Which is allowed.

Now, let's test the sample input.

Sample 1:

Input: 3 7 6.

x=3, y=7, n=6.

We need to find a/b closest to 3/7 (~0.42857).

Looping b from 1 to 6:

For each b:

Compute a_floor and a_floor +1.

For example, when b=5:

a_floor = (3*5) //7 →15//7=2. So candidates are 2 and 3.

a=2: 2/5=0.4 → dx= |2*7 -3*5|= |14-15|=1.

a=3: 3/5=0.6 → dx= |21-15|=6. So 1 is better.

So for b=5, the best a is 2, with dx=1.

Compare this to other b's.

In the sample, the correct output is 2/5. So the code should pick that.

Another sample:

Input:7 2 4. x=7, y=2, n=4.

The original fraction is 7/2, which has denominator 2 <=4. So the best is 7/2, so the code should pick a=7, b=2.

But how does the code handle this?

For b=2:

a_floor = (7*2)//2=7. candidates are 7 and 8.

a=7: dx= |7*2 -7*2|=0 → difference is zero.

a=8: dx= |8*2 -7*2|=2. So the best for b=2 is a=7, dx=0.

Thus, in the code, this candidate (dx=0, b=2, a=7) is better than any other candidates, so it will be selected.

Thus, the code works.

Now, edge cases.

Case where x=0. But according to constraints, x is positive, so not possible.

Case where x=1, y=1e5, n=1e5. Then x/y is 0.00001. So the best is 0/1, but for b=1e5, a_floor= (1*1e5)/1e5=1. So a=1 gives 1/(1e5) which is 0.00001, difference zero. So the best is a=1, b=1e5.

Another edge case: n=1. Then a can be (x*1)//y and (x*1//y)+1. Compare those two.

For example, x=5, y=3, n=1. a_floor=1, a=1 and 2. 1/1=1 (diff 2/3), 2/1=2 (diff 5/3). So best is 1/1.

But x=5, y=3 is 1.666... So 2 is 0.333 away. 1 is 0.666 away. So the best is 2/1? Wait, wait no. Wait, a_floor = (5*1)/3=1. So candidates are 1 and 2. For a=1: 1/1 is 1, difference 0.666. For a=2: 2/1 is 2, difference 0.333. So the code would select a=2, which is better. Because the difference is 0.333, which is smaller than 0.666.

So the code would pick 2/1. But according to the problem statement, a can be any non-negative integer. So this is allowed. So the code works.

Another edge case: when x/y is a fraction with a denominator larger than n. For example, x=3, y=7, n=6. Which is the first sample, and the code correctly picks 2/5.

Now, the code seems correct.

But what about the initial best being None?

In the first iteration, for b=1, the code will generate a_floor = (x*1)//y. Then candidates are a_floor and a_floor+1. Then compute dx. Since best is None, the first candidate becomes the best.

So the code should handle that.

Now, time complexity. For n up to 1e5, and for each b, two candidates, that's 2e5 iterations. For each iteration, some arithmetic operations and comparisons. So O(n) time, which is acceptable for Python even for 1e5.

Now, check the code.

But in Python, for n=1e5, the loop runs 1e5 times. Each iteration is O(1). So 1e5 iterations are manageable in 2 seconds.

Now, possible optimizations.

But for some cases, the best is already found (like when dx=0), but the code continues to check all possible b's. However, since x and y can be up to 1e5, and in the case of x=1e5, y=1, and n=1e5, the code would process all 1e5 b's, but the best is already found at b=1 (a=1e5, dx=0). So perhaps, once a candidate with dx=0 is found, the code can break early. But there may be multiple candidates with dx=0. For example, x=4, y=2, n=5. The original fraction is 2/1. So for any b that is a divisor of x*b, like b=1,2,3 (wait, x is 4, y=2. So x/y=2. So for any b, a=2*b. For example, b=3, a=6. Then 6/3=2. So dx= |6*2 -4*3|= |12-12|=0. So for all b, a=2*b would give dx=0. So in such cases, the code would find multiple candidates with dx=0. But according to the problem's tiebreaker rules, the smallest denominator, then smallest a.

So once the code finds a candidate with dx=0 and the smallest possible b, it can break early. Because any larger b's would have a higher denominator and thus not be better. But how to detect this.

But in the code, the best candidate is updated as the code proceeds. So once a candidate with dx=0 is found, and if that b is the smallest possible (1), then no further candidates can be better. For example, if x=4, y=2, then x/y=2. So the best is a=2, b=1. So once b=1 is processed, the best is (dx=0, b=1, a=2). For any other b, even if they have dx=0, since their b is larger, they won't replace the current best.

So in the code, after processing b=1, any other b with dx=0 would have a higher b and thus not be better. So the code can safely process all other b's, but they will not change the best.

Thus, adding a check for dx=0 and breaking early is possible but may not save much time. Because in the general case, the code may not find any dx=0. So it's better to proceed with the O(n) approach.

So the code as written should be correct.

Now, code testing.

Sample 1:

Input:3 7 6 → output 2/5.

Let's see what the code does.

Loop from b=1 to 6.

b=1:

a_floor = (3*1)//7 =0 → candidates 0 and 1.

a=0: dx= |0*7 -3*1| =3.

a=1: dx=|7-3|=4. So best is (3,1,0).

current best is (3,1,0).

b=2:

a_floor=6//7=0 → candidates 0,1.

a=0: dx=6-6=0? Wait, 3*2=6. 0*7 =0. 0-6= -6 → dx=6.

a=1: 7-6=1 → dx=1. So for a=1, dx=1.

Compare with current best (3,1,0):

current_val for a=0 is 6 * 1 (current dx=6, best_b=1) →6*1=6. Best_dx=3* current_b=3*2=6 → 6*1=6. So 6=6. So compare b. current b=2 is larger than 1. So no change.

For a=1, dx=1. current_val=1 *1=1. Best_val=3*2=6. So 1<6 → update best. Now best is (1,2,1).

b=3:

a_floor=9//7=1 → candidates 1 and 2.

a=1: dx=7*1 -3*3 =7-9= -2 → dx=2.

a=2:14-9=5 →dx=5.

Compare with best (1,2,1).

a=1: dx=2. current_val=2*2=4. Best_val=1*3=3. 4>3 → no.

a=2: dx=5. 5*2=10>3*3=9 → no. So no change.

So best remains (1,2,1).

b=4:

a_floor=12//7=1 → candidates 1,2.

a=1: dx=7*1 -3*4=7-12=5 →dx=5.

a=2:14-12=2 →dx=2.

Compare:

a=2:

dx=2. current_val=2*2=4 (best_b is 2). best_val is 1*4=4 → same. So check b. current b is4>2 → no.

So no change.

b=5:

a_floor=15//7=2 → candidates 2,3.

a=2: dx=14-15=1 → dx=1.

a=3:21-15=6 →dx=6.

Compare:

current_val (dx=1) * best_b (2) →1*2=2.

best_val (current best's dx is 1, best_b is2, current b=5 → best_val=1*5=5.

So 2 <5 → so current a=2, b=5 is better. So best becomes (1,5,2).

b=6:

a_floor=18//7=2 → candidates 2,3.

a=2: dx=14-18=4 →dx=4.

a=3:21-18=3 →dx=3.

Compare with best (1,5,2).

a=2: current_val=4 *5=20. best_val=1*6=6. 20>6 → no.

a=3:3*5=15>6 → no.

So best remains (1,5,2).

At the end, best_a=2, best_b=5. So output 2/5. Correct.

So the code works.

Sample 2:

Input:7 2 4 → output7/2.

Let's see:

x=7, y=2, n=4.

Loop b from 1 to4.

b=2:

a_floor=7*2 //2=7 → candidates 7 and8.

a=7: dx=7*2 -7*2=0 → best is (0, 2,7).

For any other b, even if they have dx=0, their b is larger than 2. So no.

Thus, the best is 7/2.

So code is correct.

Another test case: x=5, y=3, n=3.

x/y=1.666666...

Possible b's:

b=1: candidates a_floor=5*1/3=1. So a=1 (dx= |3-5| =2), a=2 (dx=6-5=1). So best for b=1 is a=2, dx=1.

b=2: a_floor=10/3=3. So candidates 3 and4. 

a=3: 3/2=1.5 → dx= |6-10|=4.

a=4: 4/2=2 →dx=8-10=2. So best for b=2 is a=4, dx=2.

Compare to current best (dx=1, b=1, a=2). So no change.

b=3: a_floor=15/3=5 → candidates 5 and6.

a=5: 5/3 ~1.666 → dx= |15-15|=0 → best becomes (0,3,5).

So output is5/3.

But wait, wait. For x=5, y=3, and n=3.

The optimal a is5/3, which is x/y itself. So the code should output5/3.

But wait, denominator is3, which is allowed. So the code will choose that.

Thus, the code works.

Now, code implementation:

The code reads x, y, n. Then loops through each b in 1..n. For each b, compute a_floor and two candidates. For each candidate, compute dx and compare with the current best.

The code uses integers and compares using cross products to avoid floating points.

Now, code:

Read x, y, n.

Initialize best as (dx, b, a) → initially None.

Loop b from 1 to n:

    a_floor = (x*b) // y

    for delta in 0, 1:

        a = a_floor + delta

        dx = abs(a*y - x*b)

        compare with best.

The code then selects the best.

So here's the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    x, y, n = map(int, input_stream.readline().rstrip("\n").split())

    best_dx = None
    best_b = None
    best_a = None

    for b in range(1, n + 1):
        a_floor = (x * b) // y
        for delta in (0, 1):
            a = a_floor + delta
            dx = abs(a * y - x * b)
            if best_dx is None:
                best_dx, best_b, best_a = dx, b, a
            else:
                # Compare using cross multiplication
                current_cmp = dx * best_b
                best_cmp = best_dx * b
                if current_cmp < best_cmp:
                    best_dx, best_b, best_a = dx, b, a
                elif current_cmp == best_cmp:
                    if b < best_b:
                        best_dx, best_b, best_a = dx, b, a
                    elif b == best_b and a < best_a:
                        best_dx, best_b, best_a = dx, b, a

    print(f"{best_a}/{best_b}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 2 4
""",
            "output": \
"""\
7/2
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

Test case 2:

Input:7 2 4 → code selects a=7, b=2.

Another test case: x=5, y=3, n=3. Output 5/3.

But when b=3, a_floor=5*3//3=5. So a=5 and 6.

a=5: dx=0. So best is (0,3,5).

So code outputs5/3.

Another test case: x=1, y=2, n=1. What's the best?

b=1.

a_floor=1*1//2=0. Candidates 0 and1.

a=0: dx=0*2 -1*1= -1 → dx=1.

a=1: dx=2-1=1. So both candidates have dx=1.

But same dx, so compare a. So best a is 0, then 1.

But in code, since dx is same and b is same, then smaller a is better.

Thus, the code would select a=0.

But 0/1 is 0, and the target is 0.5. The difference is 0.5. But a=1/1=1, difference is 0.5. So same difference. So code chooses a=0.

But according to problem statement, if multiple a's for the same b have the same difference, choose the smallest a.

Thus, code correctly outputs0/1.

But wait, the problem requires a to be non-negative. So 0 is allowed.

But the code's logic for selecting between a_floor and a_floor+1 may not have covered a_floor-1, but in this case, the a_floor is 0. So a_floor-1 is -1, which is invalid.

So the code works.

Thus, the code seems correct.
</think>

```python
x, y, n = map(int, input().split())

best_dx = None
best_b = None
best_a = None

for b in range(1, n + 1):
    a_floor = (x * b) // y
    for delta in (0, 1):
        a = a_floor + delta
        dx = abs(a * y - x * b)
        if best_dx is None:
            best_dx, best_b, best_a = dx, b, a
        else:
            current_cmp = dx * best_b
            best_cmp = best_dx * b
            if current_cmp < best_cmp:
                best_dx, best_b, best_a = dx, b, a
            elif current_cmp == best_cmp:
                if b < best_b:
                    best_dx, best_b, best_a = dx, b, a
                elif b == best_b and a < best_a:
                    best_dx, best_b, best_a = dx, b, a

print(f"{best_a}/{best_b}")
```
