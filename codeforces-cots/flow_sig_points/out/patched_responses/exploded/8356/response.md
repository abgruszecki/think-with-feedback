<think>
Okay, let's see. The problem is to determine how many distinct heights (number of floors) can be formed using exactly n cards. The rules for the house structure are a bit specific, so I need to model this correctly.

First, I need to understand how the cards are used per each possible floor configuration. Let's break down the requirements.

Each floor has a certain number of rooms. The rooms are arranged in a row, and each adjacent pair of rooms shares a ceiling. So for a floor with k rooms, how many cards does that take?

Each room is made of two cards. Then, the ceilings between them. Wait, the rooms are in a row. So for k rooms, there are (k-1) ceilings between them, each requiring a card. So per floor, the number of cards is 2k + (k-1) = 3k - 1. Because each room is two cards (so 2k) and the ceilings between them (k-1 cards). But wait, also, each floor has a ceiling. Wait, no. The problem statement says: each floor consists of a non-zero number of rooms and the ceiling. Oh right, so the ceiling is part of the floor. So maybe the formula is different.

Wait, let's read the problem statement again carefully.

Each floor has rooms and a ceiling. A room is two cards leaned towards each other. The rooms are in a row, and each two adjoining rooms share a ceiling made by another card. So, perhaps the ceiling here refers to the top part of the floor. Or maybe the ceiling of the floor is the part that's the top of the rooms, which is the cards that form the ceiling between the rooms.

Wait, maybe the per-floor calculation is as follows:

Each floor has a number of rooms, say k. Each room requires 2 cards. Then, between the rooms, there are (k-1) ceilings (each made by a card). Additionally, there's a ceiling for the entire floor. Wait, no. The problem statement says, "each floor consists of a non-zero number of rooms and the ceiling." So the ceiling is part of the floor. So perhaps the total cards per floor is 2k (rooms) + (k+1) (ceiling)? Or maybe the ceiling is (k+1) cards. Hmm, this part is unclear.

Wait, the example: the first sample input is 13. The note says that for 13 cards, the possible houses have two floors. Let's see what that implies.

Let's think of the structure of a house. For example, let's say the first floor (bottom floor) has a certain number of rooms, and the next floor has fewer.

For each floor i, the number of rooms is ki, and each subsequent floor must have fewer rooms than the previous. So k1 > k2 > ... > km, where m is the height (number of floors).

Now, for each floor, the number of cards used is 3ki + 1? Or 3ki - 1? Let's see:

The problem says each room is two cards. Then the rooms are arranged in a row. The ceiling part: perhaps for each room, there's a ceiling. Wait, the problem says, "each two adjoining rooms share a ceiling made by another card." So each adjacent pair of rooms uses one card for the ceiling. So for k rooms, there are (k-1) ceiling cards. Then, each room is two cards. So total per floor is 2k + (k-1) = 3k -1 cards. But the problem says the floor also includes the ceiling. Wait, maybe that's part of the next floor's structure? Or perhaps the ceiling is part of the current floor's structure. Wait, the problem says each floor has rooms and the ceiling. So perhaps each floor's ceiling is part of that floor's total cards. So perhaps the formula is indeed 3k -1 per floor.

Wait, let's take the first sample. The note says that with 13 cards, the answer is 1. So there's only one possible height. Let's see what that height is.

Suppose the height is 2. Then, there are two floors. Let's say the first floor has k1 rooms, the second has k2 < k1.

Total cards: sum_{i=1 to 2} (3k_i -1) = (3k1 -1) + (3k2 -1) = 3(k1 +k2) -2. This must equal 13.

So 3(k1 +k2) -2 =13 → 3(k1 +k2) =15 → k1 +k2 =5.

But k2 <k1, and both are positive integers.

Possible pairs:

k1=3, k2=2 → sum 5. Then total cards 3*(5) -2 =15-2=13. Yes. So that's valid.

Another possible pair: k1=4, k2=1 → sum 5. Also valid.

So for the height of 2, there are two possible configurations (but the height is 2 in both cases). So the answer counts each distinct height once. So for 13, the output is 1, which is correct.

So the formula for the total cards for a house of m floors is sum_{i=1 to m} (3ki -1) = 3 * sum(ki) - m, where k1 >k2> ...>km ≥1.

So the total cards required for a certain sequence of ki's is 3*(sum of ki's) - m.

We need to find all possible m (heights) such that there exists a sequence of m floors with k1>k2>...>km ≥1, and 3*(sum ki) - m =n. Then the answer is the number of such m's.

So the problem reduces to finding all possible integers m ≥1 for which there exists a sequence of m integers k1 >k2>...>km ≥1, and 3*(sum ki) - m =n.

But how can we compute this for a given n?

The approach is to find all m such that there exists a sum S of m distinct positive integers in decreasing order (each less than the previous), and 3S -m =n. Then S must be (n +m)/3. Also, S must be an integer, so (n +m) must be divisible by 3.

So for each possible m, check if (n +m) is divisible by 3, and then check whether there exists a sequence of m distinct integers (each less than the previous) that sum to S = (n +m)/3.

Wait, but the condition is that the sequence is strictly decreasing (k1>k2>...>km). Each term is a positive integer. So the minimal sum for m terms is when the sequence is m, m-1, ..., 1. Because that's the maximal possible sum for m terms with all terms distinct and decreasing. Wait, no. Wait, the minimal sum for m distinct positive integers in decreasing order is when the sequence is m + (m-1) + ... +1. Wait, no. Wait, for example, m=2, the minimal sum is 1+1. But wait, the terms must be strictly decreasing. Oh right, no. Because for m=2, k1 must be >k2, and both ≥1. So the minimal sum is 2+1=3. For m=3, it's 3+2+1=6, etc. So the minimal sum for m terms is the sum of the first m positive integers, but in reverse order. So the minimal possible sum S for m terms is m*(m+1)/2. Because sum 1+2+...+m = m(m+1)/2. But since the sequence is decreasing, the sum is same.

Wait, but the sum of the first m integers is m(m+1)/2, which is the minimal sum possible for m terms when they are 1, 2, ..., m arranged in any order. Wait, no. Wait, the minimal sum possible for m distinct positive integers is when they are 1, 2, 3, ..., m. The sum is m(m+1)/2. But in our case, the sequence must be strictly decreasing, but each term can be any value as long as they are in decreasing order and positive. So the minimal sum is when the sequence is m, m-1, ..., 1. The sum is the same as 1+2+...+m = m(m+1)/2. So yes.

Wait, for example, m=3: 3+2+1 =6. So the minimal sum S is 6. So any valid sequence of 3 terms will have sum ≥6.

But in our problem, S must be equal to (n +m)/3. So for each m, we need (n +m) divisible by 3, and then S = (n +m)/3 must be ≥ m(m+1)/2.

Because the minimal possible sum for m terms is m(m+1)/2, and the actual sum S must be at least that. So (n +m)/3 ≥ m(m+1)/2 → n +m ≥ 3m(m+1)/2 → n ≥ (3m(m+1)/2) -m → n ≥ m*(3(m+1)/2 -1) → ?

So for each m, if (n +m) is divisible by 3, and S = (n +m)/3 ≥ m(m+1)/2, then it's possible to have a house of height m.

But why is that sufficient? Because if S is ≥ the minimal sum, then there exists a sequence of m terms that sum to S. Because once the sum is >= the minimal sum, we can adjust the terms by adding 1 to the largest terms. For example, for m=2, minimal sum is 3 (2+1). If S=4, then possible sequence is 3+1. Wait, but 3 is larger than 1. So yes. So for any S >= the minimal sum, it's possible to find a sequence.

Wait, but how? Let's think of it as the sum being S, which is the sum of m distinct terms in decreasing order. The minimal sum is m(m+1)/2. So if S ≥ m(m+1)/2, then there exists a way to distribute the "extra" (S - minimal sum) into the terms. For example, adding to the largest terms first.

For example, m=2, minimal sum 3. If S=4, then we can have 3 +1 +0 (but no, the terms have to be distinct and in decreasing order). Wait, maybe another approach. Let's think of the sequence as starting with m, m-1, ..., 1. The sum is S0 = m(m+1)/2. Then, for any additional amount, we can distribute it to the terms in such a way that the sequence remains strictly decreasing. For example, adding 1 to the first term, then 1 to the second, etc. But ensuring that each term is larger than the next.

Alternatively, perhaps the maximal sum is unbounded, but since the problem allows any m terms as long as they are in decreasing order, the sum can be as large as possible. So for a given m, any sum S >= m(m+1)/2 is possible.

Thus, the necessary and sufficient conditions for a valid m are:

1. (n +m) is divisible by 3.

2. S = (n + m)/3 ≥ m(m+1)/2.

So for each m, check if these two conditions are satisfied. If yes, then m is a possible height. The number of such m's is the answer.

So the approach is to iterate over possible m's and check these two conditions.

Now, the question is: how to efficiently compute this for large n (up to 1e12).

The steps for solving the problem:

1. Iterate over possible m values where (n +m) is divisible by 3.

2. For each such m, compute S = (n +m)/3.

3. Check if S >= m(m+1)/2.

4. If yes, count m as a valid height.

But how to find all m's that satisfy these conditions efficiently?

First, note that m must be such that n +m ≡ 0 mod 3. So m ≡ (-n) mod 3. So for each possible m ≡ r mod 3, where r is (3 - n mod 3) mod 3.

For example, if n mod 3 is 0, then m must be ≡0 mod 3.

If n mod3 is 1, then m must be ≡2 mod3.

If n mod3 is 2, then m must be ≡1 mod3.

So possible m's can be generated by starting from a base and incrementing by 3.

But how to find the possible range of m's?

The minimal possible m is 1. The maximal possible m can be found by considering that even for the minimal sum per m, S must be >= m(m+1)/2. And since S = (n +m)/3, we can solve for m:

(n +m)/3 ≥ m(m+1)/2 → 2(n +m) ≥3 m(m+1)

Rearranged: 3m² +3m -2m -2n ≤0 → 3m² +m -2n ≤0 → solving for m in this quadratic equation.

The roots of 3m² +m -2n =0 can be found using the quadratic formula:

m = [-1 ± sqrt(1 +24n)]/(6)

The positive root is [ -1 + sqrt(1+24n) ] /6

So the maximal m possible is floor( [ -1 + sqrt(1+24n) ] /6 )

Wait, but perhaps this is the upper bound for m? Because for m beyond this value, 3m² +m -2n would be positive, so the inequality 3m² +m -2n ≤0 would not hold. Thus, the maximum possible m is the floor of (sqrt(1+24n) -1)/6.

Wait, but let's test with the sample inputs.

First sample: n=13.

sqrt(1 +24*13) = sqrt(313) ≈17.6918.

So (17.6918 -1)/6 ≈16.6918/6≈2.78. So floor is 2. So maximum possible m is 2. Which matches the sample.

In the first sample, the valid m is 2. So the code would check m=2.

Another sample: n=6.

sqrt(1+24*6)=sqrt(145)=12.041..., subtract 1 →11.041, divided by6 → ~1.84. So m can be up to 1.

So possible m's are 1.

Check m=1: n +m =7, 7/3 is not integer. So no. So output is 0.

Which matches the sample.

So the plan is:

Compute the maximum possible m as floor( (sqrt(24n +1) -1)/6 )

Then, iterate m from 1 to this upper limit, checking for each m whether (n +m) is divisible by 3 and S = (n+m)/3 >= m(m+1)/2.

But since m can be up to O(sqrt(n)), which for n=1e12 would be about sqrt(1e12) = 1e6. But even that's manageable, as 1e6 iterations are acceptable in Python for a 1s time limit.

Wait, let's compute for n=1e12:

sqrt(24*1e12 +1) = sqrt(24,000,000,000,000 +1) ≈ sqrt(2.4e13) which is around 4.9e6. Then (4.9e6 -1)/6 ≈ 816,666. So the upper limit is ~8e5. So iterating up to 8e5 steps is feasible.

But how to generate all possible m's in the range [1, max_m] that are congruent to (r) mod 3, where r is (3 - n mod3) mod3.

Alternatively, for each possible m in 1 to max_m, check if (n + m) mod3 is 0, and then check if S >= m(m+1)/2.

But even for m up to 8e5, this is manageable.

So the steps are:

1. Compute max_m = floor( (sqrt(24n +1) -1)/6 )

2. For each m in 1 to max_m:

   a. Check if (n +m) mod3 ==0.

   b. If yes, compute S = (n +m)//3.

   c. Check if S >= m*(m+1)//2.

   d. If both conditions are met, increment the count.

3. The count is the answer.

But how to compute max_m accurately?

In code, compute sqrt(24n +1) as a floating point, subtract 1, divide by 6, take the floor.

But for very large n, 24n can be up to 2.4e13 +1, so sqrt(2.4e13 +1) is about 4.9e6.

In Python, using math.isqrt (which returns the integer square root) might be better for accuracy.

Wait, for example, for n=13:

24*13+1=313. sqrt(313) is approx 17.6918. So integer square root is 17.

Then (17-1)/6 =16/6=2.666..., floor is 2. So max_m is 2.

Which is correct.

Another example, n=6: 24*6 +1=145. sqrt(145) is ~12.041, integer square root is 12. (12-1)/6=11/6=1.833, floor is 1.

Yes.

So in code:

max_m = (math.isqrt(24 * n + 1) -1) // 6

But need to handle the case where 24n +1 is a perfect square.

So the steps in code would be:

import math

n = int(input())

count = 0

if n < 3: # since for m=1, sum is 3*1 -1=2, but 2 cards. But n=2: 3(k1) -1=2 →k1=1. sum is 3*1 -1 =2. So yes, but then S = (2+1)/3=1. So S must be >=1*(2)/2 =1. So S=1 >=1. So yes. But wait, m=1: check if (n +m) is divisible by 3. So 2 +1=3, yes. S=1. Then check if S >= m(m+1)/2 →1 >= (1*2)/2 →1 >=1 →yes. So for n=2, m=1 is valid. So the code would count it.

But the sample input where n=6: for m=1, check (6+1) mod3 is 7 mod3=1, which is not 0.

So code would proceed.

So the code:

We compute max_m as (sqrt(24n +1) -1)//6.

Then for each m from 1 to max_m:

Check if (n +m) mod3 ==0. If yes, compute S = (n+m)//3.

Check if S >= m*(m+1)//2.

If both conditions, increment count.

Now, let's test for n=13:

max_m = (sqrt(313) -1)//6 → (17-1)/6=16/6=2.666... → floor 2. So m can be 1 or 2.

For m=1: (13 +1) =14 mod3= 14%3=2 → no.

For m=2: 13+2=15 →15 mod3=0. S=15//3=5. Check if 5 >= (2*3)/2 →5 >=3 →yes. So count increases by 1. So the answer is 1.

Which is correct.

Another test case: n=2. max_m is (sqrt(49) -1)/6 → (7-1)/6=1. So m=1. Check (2+1) mod3=0. S=1. Check 1 >=1 → yes. So count is 1. So output 1.

But according to the problem statement, the sample with n=6 outputs 0. Let's see:

n=6. max_m is (sqrt(24*6+1)-1)/6 → sqrt(145)=12.041... integer sqrt is 12. (12-1)/6=11/6=1.833 → max_m=1.

Check m=1: 6+1=7 mod3=1. So no. So count remains 0. Correct.

Another test case: n=3. Let's see.

max_m: 24*3+1=73. sqrt(73)≈8.544 → isqrt is 8. (8-1)/6=7/6=1.166 → max_m=1.

m=1: 3+1=4 mod3=1. Not divisible. So count 0. So output is 0.

But wait, what about m=1. 3k1 -1 =3 →3k1=4 →k1=4/3, which is not an integer. So no. Correct.

Another example: n=8.

Check possible m's.

max_m is (sqrt(24*8 +1) -1)/6 → sqrt(193)=13.89, isqrt=13. (13-1)/6=12/6=2. So m up to 2.

m=1: 8+1=9 mod3=0. S=9/3=3. Check 3 >=1*2/2 →3≥1 → yes. So valid. So m=1 is possible.

So the house has 1 floor. Which would be 3k1 -1 =8 →3k1=9 →k1=3. So sum is 3. So yes.

Thus, the answer would be 1. But according to code, let's see:

For m=1:

(n+m) =9 → divisible by3. S=3. Check S >=1*2/2 →3 >=1 → yes. So count is 1.

Thus, the code counts this case.

So code seems correct.

Now, implement this in Python.

But wait, for very large n (up to 1e12), the loop from 1 to max_m must be efficient.

But for n=1e12, max_m is (sqrt(24e12 +1)-1)/6 → sqrt(24e12) is sqrt(2.4e13) → ~4.9e6. So 4.9e6 iterations. In Python, that's acceptable.

So code steps:

Read n.

Compute max_m.

Initialize count=0.

For m in 1 to max_m:

   if (n + m) mod3 !=0 → skip.

   else:

      s = (n +m)//3

      if s >= m*(m+1)//2 → count +=1.

Return count.

Yes.

So code:

import math

n = int(input())

max_m = (math.isqrt(24 * n + 1) - 1) // 6

count = 0

for m in range(1, max_m + 1):

    if (n + m) % 3 != 0:

        continue

    s = (n + m) // 3

    required = m * (m + 1) // 2

    if s >= required:

        count +=1

print(count)

Wait, but what if (n +m) is not divisible by 3? Then m is skipped.

Yes.

Testing sample input 13:

n=13.

max_m=2.

m=1: 13+1=14 →14%3=2 → skip.

m=2:13+2=15 →15%3=0 → s=5.

required =2*3//2=3. 5>=3 → yes. count becomes 1.

So output is 1. Correct.

Sample input 6:

max_m=1.

m=1:6+1=7 →7%3=1→ skip. count remains 0. Correct.

Another test case: n=2.

max_m=(sqrt(49)-1)/6 → (7-1)/6=1.

m=1: (2+1)=3 →3%3=0 →s=1. required 1*2//2=1. 1 >=1 → yes. count=1. So output 1.

But what about n=2?

The house would have m=1 floor. The sum is 3k -1 =2 →3k=3 →k=1. So yes. So one floor, which is valid. So output is 1.

Another test case: n=8. As before, code returns 1.

Yes.

Another test case: n=3 → code returns 0.

Another example: n=5.

max_m = (sqrt(24*5 +1) -1)/6 → sqrt(121)=11 → (11-1)/6=10/6=1.666 → max_m=1.

m=1:5+1=6 →6%3=0 →s=2. required 1. 2>=1 → yes. count is 1.

So output is 1. But what is the possible house?

It's one floor: 3k1-1=5 →3k1=6 →k1=2. So yes. So valid.

Thus, the code is correct.
</think>

```python
import math

n = int(input())
max_m = (math.isqrt(24 * n + 1) - 1) // 6
count = 0

for m in range(1, max_m + 1):
    if (n + m) % 3 != 0:
        continue
    s = (n + m) // 3
    required = m * (m + 1) // 2
    if s >= required:
        count += 1

print(count)
```