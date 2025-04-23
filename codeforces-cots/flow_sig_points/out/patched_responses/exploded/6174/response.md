<think>
Okay, let's see. The problem is about counting how many dragons up to d are divisible by at least one of the numbers k, l, m, n. So each dragon is numbered from 1 to d. For each of these, if the number is divisible by k, l, m, or n, then it's considered damaged. We need to count how many such numbers there are.

Hmm, the straightforward approach would be to iterate through each number from 1 to d and check if it's divisible by any of the four numbers. But wait, when d is up to 1e5, which is 100,000, then this approach would be O(d) time, which is acceptable because 1e5 operations are manageable within Python's speed for time limits. Like, even 1e6 is manageable, but 1e5 is definitely okay. So maybe that's the way to go.

But let's think about the constraints. Each of k, l, m, n can be up to 10, and d up to 1e5. So for each number from 1 to d, check divisibility by any of the four. The maximum operations would be 1e5 *4, which is 4e5. That's very manageable.

So the plan is: iterate each number from 1 to d. For each, check if it is divisible by k, l, m, or n. If yes, count it.

But wait, maybe there's a smarter way using inclusion-exclusion principle. That could reduce the computation time by not having to check each number. Let's think. The inclusion-exclusion would calculate the count as the sum of the counts for each individual divisor, minus the sum for each pair's LCM, plus the sum for each triplet's LCM, and so on.

So for four divisors a, b, c, d, the formula is:

count = (divisible by a) + (divisible by b) + ... 
        - (divisible by LCM(a,b) for all pairs) 
        + (divisible by LCM(a,b,c) for all triples)
        - (divisible by LCM of all four)

But calculating all possible subsets of the four numbers and their LCMs could be tedious. Since there are 4 numbers, the number of subsets is 2^4 -1 =15 (non-empty subsets). For each subset, compute the LCM, then add or subtract based on the inclusion-exclusion principle. But how many terms would that be?

Inclusion-exclusion for 4 variables:

Total = sum_single - sum_pairs + sum_triples - sum_quadruples.

So for each possible combination, compute the LCM, then check if the subset has even or odd size (even being pairs, quadruples, etc. if the step is subtraction for even steps? Wait, inclusion-exclusion alternates signs: for subsets of size 1: add, size 2: subtract, size3: add, size4: subtract.

Wait, inclusion-exclusion formula for the union of four sets A, B, C, D is:

|A ∪ B ∪ C ∪ D| = |A| + |B| + |C| + |D| 
                  - |A ∩ B| - |A ∩ C| - |A ∩ D| - |B ∩ C| - |B ∩ D| - |C ∩ D|
                  + |A ∩ B ∩ C| + |A ∩ B ∩ D| + |A ∩ C ∩ D| + |B ∩ C ∩ D|
                  - |A ∩ B ∩ C ∩ D|

So the number of terms is:

4 (single) 
+ 6 (pairs) with subtraction 
+ 4 (triples) addition 
+ 1 (quadruple) subtraction.

So total 15 terms.

But for each of these subsets, we need to compute the LCM of their elements, then calculate how many numbers up to d are divisible by that LCM. Then multiply by +1 or -1 depending on the subset size's parity.

For example, for a subset of size 1 (like {k}), add the count. For a subset of size 2 (like {k,l}), subtract the count of numbers divisible by LCM(k,l), etc.

This approach could be more efficient than checking each number individually. Because for d=1e5, checking each number would take O(d) time, which is 1e5 steps. Whereas with inclusion-exclusion, there's 15 subsets, each requiring calculating LCM and then d divided by LCM. Each of those steps is O(1), so 15 steps. So this would be O(1) per subset, which is way faster.

So for large d (like 1e5), the inclusion-exclusion approach is way better.

But wait, when the numbers k, l, m, n are small (up to 10), the LCMs could be up to 10*9*8*7=5040 (if all four are 10,9,8,7?), but perhaps even higher. Wait, no. For example, if the numbers are 2,4, then LCM is 4. So for subsets, their LCM can be up to 10*9*8*7=5040? Not sure. But when calculating d divided by that LCM, it's O(1).

So the inclusion-exclusion approach is definitely better. But how to implement it correctly?

So the steps would be:

1. Generate all non-empty subsets of the four divisors (k, l, m, n). For each subset, compute the LCM of its elements.

2. For each subset, if the LCM is larger than d, then it contributes 0 to the count. Otherwise, the count is d // LCM.

3. Then, based on the subset's size (even or odd?), add or subtract this count from the total. Wait, the sign depends on the size of the subset. For subsets of size s, the sign is (-1)^(s+1). For example, subsets of size 1 contribute +count (since (-1)^(1+1) = 1). Subsets of size 2 contribute -count (since (-1)^(2+1) = -1). Subsets of size 3 contribute +count, and so on.

Wait, in inclusion-exclusion:

The formula alternates signs based on the size of the subset. For the union of n sets, the term for a subset of size m is multiplied by (-1)^(m+1) when m is from 1 to n. Wait, let me see:

The inclusion-exclusion formula for the union is sum_{S subset, S non-empty} (-1)^(|S|+1) * |intersection of S|.

Wait, for each subset S of the sets A1, A2, etc., the term is (-1)^(|S| -1) multiplied by the intersection. So for a subset of size 1, it's +A_i. For subsets of size 2, subtract the pairwise intersections. So the sign is (-1)^(m-1), where m is the subset size.

So for a subset of size m, the coefficient is (-1)^(m-1). So the term is added if m is odd, subtracted if even.

So in code, for each subset, the sign is +1 if the size is odd, -1 if even.

Wait, for a subset of size m:

coefficient = 1 if m is odd, -1 if even.

Wait, let's see:

For m=1: coefficient is (-1)^(1-1) = 1 → +1.

m=2: (-1)^(2-1) = -1 → -1.

m=3: (-1)^(3-1) = 1 → +1.

m=4: (-1)^(4-1) = -1.

So the coefficient is multiplied by (-1)^(m-1).

So the total is the sum over all non-empty subsets S of [ (-1)^(|S| - 1) * (d // LCM(S)) ].

So the plan is:

- Generate all non-empty subsets of the four divisors.

- For each subset, compute the LCM of the elements in the subset.

- For each subset's LCM, compute how many numbers up to d are divisible by LCM (if LCM is zero, which can't happen here because k, l, m, n are all >=1). So it's d // LCM, but only if LCM <=d. Else zero.

- Multiply this count by the coefficient ( (-1)^(m-1), where m is the subset size).

- Sum all these terms to get the total.

So this approach would have O(15) steps, each requiring to compute LCM and the count.

Now, the key is to generate all possible non-empty subsets of the four numbers. However, note that the four numbers could have duplicates. For example, if k equals l, then subsets that include both would have LCM as the same as just including one of them, but the code should still process them. But inclusion-exclusion handles duplicates automatically.

Wait, for example, if two of the divisors are the same, say k = l =2. Then a subset {k, l} would be {2,2}, and the LCM is 2. So in the inclusion-exclusion, the subset {k, l} would contribute - (d // 2), but since the individual k and l contribute 2*(d//2), but when they are the same, the pairwise terms would subtract (d//2). But since the subsets must be considered even if they have duplicate elements. Wait, but in reality, the input is given as four numbers, which may or may not be duplicates. For example, if two of them are 2, then their pairwise LCM is 2. So the code should process them as per their actual values, even if duplicates.

So in the code, when generating subsets, duplicates are allowed. For example, if the input includes two 2s, then a subset containing both would be processed, but the LCM would be 2, etc. However, in the problem statement, the four divisors are k, l, m, n. So even if they are the same, each is considered a separate divisor. For example, if all four are 1, then any dragon is divisible by all four. So the inclusion-exclusion approach must process all subsets, even those that have duplicates.

So the code must generate all possible non-empty subsets of the four divisors, but considering each divisor as distinct. For example, if k=2, l=2, then subsets {k} and {l} are considered separate, even though their LCM is the same.

Wait, no. Wait, in the problem statement, the four divisors are four separate variables. So for example, if k=2, l=2, then the dragons are damaged if divisible by k OR l. But since both are 2, it's equivalent to just divisibility by 2. But in inclusion-exclusion, the code would generate subsets {k}, {l}, {k,l}, etc. For {k}, the LCM is 2. For {l}, also 2. For {k,l}, LCM is 2.

So when adding these subsets:

The single subsets {k} and {l} would each contribute + (d//2), but their sum is 2*(d//2). Then the pair {k,l} contributes -(d//2). So the net effect for the subsets would be 2*(d//2) - (d//2) = (d//2). Which is correct because the union of the two sets (divisible by k or l) is just the set of numbers divisible by 2, which is (d//2). So the inclusion-exclusion approach would correctly handle this.

But in reality, in the problem statement, the four divisors can be duplicates, so the code must treat each as a separate element. So the code must generate all possible non-empty subsets of the four elements (k, l, m, n), even if some elements are the same.

Wait, but when generating subsets, the elements are considered distinct. So for example, the subsets {k} and {l} are considered different even if k and l are the same. But in reality, their LCM is the same, so the code would end up adding (d//k) + (d//l) which would be 2*(d//k) if k=l. But the inclusion-exclusion would then subtract (d//lcm(k,l)) which is d//k, leading to a total of 2*(d//k) - (d//k) = d//k, which is correct.

So even if the divisors are duplicates, the inclusion-exclusion approach handles it correctly.

Therefore, the code should generate all non-empty subsets of the four divisors (k, l, m, n), considering each as a separate element (even if their values are the same).

So the next step is to generate all possible non-empty subsets of the four elements. The four elements are in a list, say divisors = [k, l, m, n]. For each subset, we need to compute the LCM of the elements in the subset.

But how to generate all possible non-empty subsets? There are 4 elements, so each subset can be represented by a bitmask from 1 to 15 (since 2^4 -1 =15). For each bitmask, check which bits are set, and collect the corresponding elements.

For example, for the four elements at indices 0,1,2,3:

bitmask 0001 (1 in decimal) represents the subset {0}, which is the first element (k).

bitmask 0010 (2) represents {1} (l), etc.

Then for each subset (non-empty), collect the elements, compute their LCM, and then compute the count.

But if a subset contains elements that have a zero LCM (which can't happen here since all divisors are >=1), but in our case, since all elements are >=1, the LCM will be >=1.

So the code steps:

Read k, l, m, n, d.

divisors = [k, l, m, n]

Initialize total = 0

For each subset in all non-empty subsets of divisors:

   compute the LCM of the subset's elements.

   if LCM > d: continue, since no numbers are divisible by it.

   else:

       count = d // LCM

       m = len(subset)

       if m is odd: add count to total

       else: subtract count from total

But wait, how to generate all non-empty subsets? Each subset is a combination of 1 to 4 elements, with all possible combinations.

Wait, the code should generate all possible non-empty subsets of the four divisors. Each subset is a collection of one or more of the four elements. But since the elements can be duplicates, the code must generate subsets that may have the same elements but different combinations.

But perhaps the code can generate all possible subsets (non-empty) by generating all possible bitmask from 1 to 15 (since 4 elements), and for each bitmask, collect the elements where the bit is set.

But in code, for each bitmask in 1..15:

   elements_in_subset = [divisors[i] for i in 0..3 if bitmask has the i-th bit set]

   compute LCM of elements_in_subset

Then proceed as before.

But wait, for example, the subset {k, l} is considered, which is different from {l, k}, but the order doesn't affect the LCM. So the code is correct.

So the code for generating subsets would iterate over all possible bitmask from 1 to 15 (since 4 elements, 2^4 -1 =15).

But in Python, how to generate the bitmask and check which bits are set?

For example, for each mask in range(1, 1 << 4):

   then, for each bit position (0 to 3), check if the bit is set.

So:

divisors = [k, l, m, n]

for mask in 1 to 15 (inclusive):

   elements = []

   for i in 0 to 3:

       if mask & (1 << i):

           elements.append(divisors[i])

   compute LCM of elements.

Then compute the count.

But this approach would generate all possible subsets, including those with multiple elements. However, for each subset, even if the same elements are selected in a different order, the LCM is the same, so the code will process each subset correctly.

But some subsets may have the same elements. For example, if k and l are the same, then subsets {k} and {l} are considered as separate subsets. However, their LCM is the same. So the code will process them as separate subsets. For example, mask 0001 (k) and 0010 (l) would each contribute their own count. But when they are processed, the inclusion-exclusion would add their counts, then subtract the pairwise subset {k, l} (mask 0011), whose LCM is LCM(k,l) = k (if k=l). So in the end, the code would compute the correct union.

But the problem is that when subsets have the same LCM, but are generated as different subsets, the code may be adding and subtracting multiple terms, but inclusion-exclusion requires each subset to be considered once. Wait, no. For example, if we have two subsets S and T that are different (like {k} and {l} where k=l), but their LCM is the same. Then inclusion-exclusion would process them as two separate subsets. For example, the code would add their individual counts (each contributing d//k), and then subtract the subset {k,l}, which is d//k. So the net effect would be (d//k + d//k) - d//k = d//k, which is correct. Because the union of the two sets {k} and {l} is just the set {k}, since k=l.

So the code handles this correctly.

So the code can proceed with generating all possible non-empty subsets of the four divisors, regardless of their values, and process them all with the inclusion-exclusion approach.

Now, the next challenge is to compute the LCM of a subset of numbers.

The LCM of a list of numbers can be computed by iteratively computing the LCM of pairs.

The formula for LCM(a, b) is (a * b) // GCD(a, b). For a list of numbers, the LCM can be computed by taking the LCM of the first two, then the LCM of the result with the third number, and so on.

So for a subset of elements, say [x1, x2, x3], compute LCM(x1, x2, x3) as LCM(LCM(x1, x2), x3).

So in code, for a subset's elements, compute the LCM step by step.

But how to handle empty subsets? Since we are generating non-empty subsets (all subsets have at least one element), the elements list is non-empty.

So for each subset, the LCM is computed as follows:

current_lcm = elements[0]

for num in elements[1:]:

   current_lcm = lcm(current_lcm, num)

If at any point current_lcm exceeds d, we can break early, since further elements will only increase the LCM (since LCM(a,b) is >= max(a,b)). So once current_lcm exceeds d, adding more elements won't make it smaller, so the LCM of the subset is larger than d, and thus the subset contributes 0. So we can break early.

This optimization can help speed up the code for subsets where the elements' LCM is already larger than d.

So the steps for LCM calculation:

current_lcm = 1

for num in elements:

   current_lcm = lcm(current_lcm, num)

   if current_lcm > d:

       break

if after processing all elements, current_lcm >d: then the subset's count is zero.

Else: count is d // current_lcm.

But how to compute LCM in Python?

Python's math library has gcd, but for Python 3.5 and above, math.gcd exists. However, gcd returns the absolute value, but since our inputs are all positive, that's fine.

So LCM(a, b) can be computed as (a * b) // gcd(a, b).

But for a list of numbers, the LCM is computed step by step.

So in code:

from math import gcd

def lcm(a, b):

    return a * b // gcd(a, b)

Then, for a list of numbers:

current_lcm = 1

for num in elements:

    current_lcm = lcm(current_lcm, num)

    if current_lcm > d:

        break

But wait, in the code, if the subset is [x], then current_lcm is x. So that's correct.

But initial current_lcm should be set to the first element. Wait, no. For example, elements = [x], then:

current_lcm starts at 1.

Then, for the first element:

current_lcm = lcm(1, x) = x.

So that's correct.

So the code can be written as:

current_lcm = 1

for num in elements:

    current_lcm = lcm(current_lcm, num)

    if current_lcm > d:

        break

So for each subset, after generating elements, compute the current_lcm as the LCM of all elements, and check if it exceeds d. If yes, break early and contribute 0.

So putting it all together.

Now, code steps:

Read k, l, m, n, d.

divisors = [k, l, m, n]

total = 0

for mask in 1 to 15 (binary 0001 to 1111):

    elements = list of divisors where the corresponding bit in mask is set

    compute the LCM of elements:

        current_lcm = 1

        for num in elements:

            current_lcm = lcm(current_lcm, num)

            if current_lcm >d:

                break

        if current_lcm >d:

            continue

        else:

            count = d // current_lcm

    subset_size = len(elements)

    sign = (-1) ** (subset_size +1) 

    # since for subset size m, the term is (+1) if m is odd, (-1) if even.

    # because (-1)^(m-1) is same as (-1)**(m+1) ?

Wait, let's see:

(-1) ** (m-1) is the correct coefficient.

For m=1: (-1)^0 = 1 → correct.

For m=2: (-1)^1 = -1 → correct.

So, the coefficient is (-1) ** (m-1).

So in code:

sign = (-1) ** (subset_size -1)

then total += sign * count.

So the code would be:

from math import gcd

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

divisors = [k, l, m, n]

total = 0

def lcm(a, b):
    return a * b // gcd(a, b)

for mask in range(1, 1 << 4):  # 1 to 15 inclusive
    elements = []
    for i in range(4):
        if mask & (1 << i):
            elements.append(divisors[i])
    # Compute LCM of elements
    current_lcm = 1
    for num in elements:
        current_lcm = lcm(current_lcm, num)
        if current_lcm > d:
            break
    if current_lcm > d:
        continue
    count = d // current_lcm
    subset_size = len(elements)
    sign = (-1) ** (subset_size - 1)
    total += sign * count

print(total)

Wait, but wait. Let's test the code against the sample input.

First sample input:

1

2

3

4

12

divisors are [1,2,3,4]

All subsets:

We need to generate all non-empty subsets. For each subset, compute LCM and apply inclusion-exclusion.

But let's see.

The correct answer is 12. Because every number from 1 to 12 is divisible by 1. So all 12 dragons are damaged.

But according to inclusion-exclusion:

All subsets where any element is 1. Because any subset that includes 1 would have an LCM of LCM(1, others) which is LCM of others. For example, subsets {1} → LCM is 1. Subsets {1,2} → LCM is 2, etc.

But let's see how the code works.

For mask 0001 (binary) → elements [1], subset size 1. LCM is 1. count is 12 // 1 =12. sign is (-1)^(0) =1. So total +=12.

Other subsets:

For example, mask 0010 (elements [2]): subset size 1. LCM is 2. count 6. sign +1. So total increases by 6.

But wait, according to the problem statement, since 1 is in the divisors, any number divisible by 1 is counted, which is all numbers. But according to the code, how does it account for that?

Because when the subset {1} is considered, the code adds 12. Then for other subsets, they are also processed, but the inclusion-exclusion subtracts overlapping counts. Wait, but the inclusion-exclusion is for the union of all four divisors. So when the divisors include 1, the code will include all numbers, but other subsets may subtract some counts. Wait, perhaps the code is not correct.

Wait, let's take the first sample input. The divisors are 1,2,3,4. The code would generate all subsets. Let's see:

The total is sum over all subsets of [ sign * count ].

But since 1 is present, any subset that includes 1 will have LCM which divides 1. For example, subset {1} has LCM 1. So all 12 numbers are counted here. Then any subset that includes 1 and another number, like {1,2}, will have LCM 2. So in inclusion-exclusion, {1,2} is a subset of size 2. So sign is (-1)^(2-1) = -1. The count is 12//2 =6. So the code subtracts 6. Similarly, subsets like {1,3} subtract 4 (12//3=4), {1,4} subtract 3 (12//4=3), {1,2,3} adds 2 (12//6=2), etc.

But this seems to complicate. However, when all four divisors are present, the code's inclusion-exclusion calculation would process all possible combinations. But in the first sample input, the correct answer is 12. So how does the code calculate this?

Let's see. The code's total after all subsets would be 12.

But how? Let's compute for the first sample:

divisors = [1,2,3,4]

Subsets that include 1:

Any subset that includes 1 will have LCM equal to the LCM of the other elements. Because LCM(1, x) is x.

But processing all subsets:

For example, the subset {1} → sign is +1, count=12. So adds 12.

Then subsets that include 1 and other elements:

For example, {1,2}: size 2 → sign -1. count=6 → subtract 6.

{1,3}: subtract 4.

{1,4}: subtract 3.

{1,2,3}: size3 → sign +1. count= 12//6=2 → add 2.

{1,2,4}: LCM(1,2,4)=4 → count=3 → sign +1 → add3.

{1,3,4}: LCM(3,4)=12 → count=1 → add 1.

{1,2,3,4}: LCM(12) → count=1 → sign is (-1)^(4-1) = -1 → subtract 1.

Other subsets that do not include 1: like {2}, {3}, {4}, {2,3}, etc.

For example:

{2}: size1 → add 6.

{3}: size1 → add4.

{4}: size1 → add3.

{2,3}: size2 → subtract 2 (12//6=2).

{2,4}: subtract 3//4's LCM is 4 → 12//4=3.

{3,4}: LCM 12 → subtract 1.

{2,3,4}: LCM 12 → add1.

{2,3,4} and others.

So summing all these is complicated.

But in reality, since 1 is present, any number is divisible by 1, so all numbers are damaged. So the code should return 12. Let's see if that's the case.

But according to inclusion-exclusion, the code's calculation for subsets including 1 and others may cancel out.

Alternatively, perhaps when 1 is part of any subset, the inclusion-exclusion is correctly handled, but perhaps the code's calculation for the first sample is 12.

Wait, let's compute the code's process step by step.

The code iterates through all 15 masks.

For each mask:

1. Mask 1 (0001): elements [1]

   LCM is 1. count=12. subset_size=1 → sign=1 → total +=12 → total=12.

2. Mask 2 (0010): elements [2]

   LCM is 2. count=6. sign=1 → total +=6 → total=18.

3. Mask 3 (0011): elements [1,2]

   LCM is 2. count=6. subset_size=2 → sign=-1 → total -=6 → 12.

4. Mask 4 (0100): elements [3]

   LCM 3 → count=4. sign=1 → total +=4 → 16.

5. Mask5 (0101): elements [1,3]

   LCM is 3. count=4. subset_size=2 → sign=-1 → total -=4 → 12.

6. Mask6 (0110): [2,3]

   LCM 6 → count=2 → sign=-1 → total -=2 → 10.

7. Mask7 (0111): [1,2,3] → LCM 6. count=2 → subset_size=3 → sign=1 → total +=2 → 12.

8. Mask8 (1000): [4] → count=3 → sign=1 → total +=3 → 15.

9. Mask9 (1001): [1,4] → LCM4 → count=3 → subset_size=2 → sign=-1 → total -=3 → 12.

10. Mask10 (1010): [2,4] → LCM4 → count=3 → subset_size=2 → sign=-1 → total -=3 →9.

11. Mask11 (1011): [1,2,4] → LCM4 → count=3 → subset_size=3 → sign=1 → total +=3 →12.

12. Mask12 (1100): [3,4] → LCM12 → count=1 → subset_size=2 → sign=-1 → total -=1 →11.

13. Mask13 (1101): [1,3,4] → LCM12 → count=1 → subset_size=3 → sign=1 → total +=1 →12.

14. Mask14 (1110): [2,3,4] → LCM12 → count=1 → subset_size=3 → sign=1 → total +=1 →13.

15. Mask15 (1111): [1,2,3,4] → LCM12 → count=1 → subset_size=4 → sign=-1 → total -=1 →12.

So after all masks, the total is 12. Which is correct.

So the code works for the first sample.

The second sample input:

2

3

4

5

24

divisors = [2,3,4,5]

The code should process all subsets and compute 17.

Let's see if the code can handle this.

But calculating all 15 subsets would be tedious. However, the code should correctly compute 17.

But given that the code passed the first sample, and the inclusion-exclusion approach is correct, the code should work.

Now, let's check the code's efficiency.

For d up to 1e5, and 15 subsets, each subset's LCM is computed in O(k) time, where k is the number of elements in the subset (up to 4). So total operations are 15 *4 =60 operations. Which is negligible.

Thus, the code is optimal and should pass all test cases within the time limits.

So the code is correct.
</think>

```python
import math
from math import gcd

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

divisors = [k, l, m, n]

total = 0

def lcm(a, b):
    return a * b // gcd(a, b)

for mask in range(1, 1 << 4):
    elements = []
    for i in range(4):
        if mask & (1 << i):
            elements.append(divisors[i])
    current_lcm = 1
    for num in elements:
        current_lcm = lcm(current_lcm, num)
        if current_lcm > d:
            break
    if current_lcm > d:
        continue
    count = d // current_lcm
    subset_size = len(elements)
    sign = (-1) ** (subset_size - 1)
    total += sign * count

print(total)
```