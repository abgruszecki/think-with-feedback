<think>
Okay, let's try to figure out this problem. So the problem is about counting the number of valid sequences where the last occurrence of color i comes before the last occurrence of color i+1 for all i from 1 to k-1. And we have to compute this modulo 1e9+7. 

Hmm. Let's think about the constraints. The key here is the order of the last occurrences of each color. For the sequence to be valid, the last occurrence of color 1 must be before color 2's last, which must be before color 3's last, and so on until color k. So the order of the last elements of each color has to be exactly 1, 2, 3, ..., k. 

Wait, but how do we model this? Let's break it down. The total number of possible sequences without any constraints is the multinomial coefficient, since the balls of the same color are indistinct. So if there are c_1 balls of color 1, c_2 of color 2, etc., the total sequences are (total)! / (c_1! c_2! ... c_k!). But with the specific constraint on the order of the last occurrences.

So the problem is to compute the number of such sequences where the last of color 1 is before the last of color 2, etc. How can we model this?

Let me think recursively. Suppose we have all the colors except color k. Then, the last ball in the sequence must be the color k. Then, among the remaining positions (since the last one is fixed as color k), the next to last occurrence of color k-1 must be after the last of color k-2, and so on. Wait, maybe there's a combinatorial way to model this.

Alternatively, the problem can be approached by considering that the order of the last occurrences of the colors must form the sequence 1,2,...,k. So for each color, the last occurrence of that color must come after the last occurrences of all previous colors. Wait no, actually in the problem statement, the last of color i must come before the last of color i+1. So the order of the last occurrences is 1 < 2 < ... < k. So the last of color 1 is the earliest among all last occurrences, then color 2's last is after that, etc.

So how to compute this? Maybe the approach is to multiply the number of valid arrangements for each color step by step.

Let's consider the colors in the order they must appear in their last occurrence. So first, arrange the balls such that the last of color 1 is first, then color 2's last is after that, etc.

Let me think of the problem as building the sequence. The last occurrence of each color must form the order 1, 2, ..., k. So the very last ball in the entire sequence is the last ball of color k. Then, the last ball of color k-1 must be somewhere before that. Similarly, the last ball of color k-2 must be before the last of k-1, and so on until color 1.

So the structure is that the last of each color i is placed in such a way that their positions are ordered as 1's last < 2's last < ... <k's last. The total number of such sequences can be computed using a product of combinations, considering the insertion of each color's balls into the remaining positions.

Here's an approach inspired by dynamic programming. Let's process the colors in the order 1 to k. We can keep track of the total number of balls processed so far and the number of ways to arrange them under the given constraints.

For example, start with color 1. All of its balls except one (the last one) can be placed anywhere, but the last one must be the first in the sequence of last positions. Wait, no. Wait, color 1's last ball must come before color 2's last, which must come before color 3's last, etc. But in the initial step, when we process color 1, we need to fix that its last occurrence is the earliest among all. Then, when adding color 2, the last occurrence of color 2 must come after color 1's last, and so on.

Alternatively, the idea is to multiply the possible combinations for each color, considering the existing positions. Let's say we have already placed some colors, and we are adding the next color.

Let's think in reverse. The last ball in the entire sequence must be the last of color k. So the last ball is fixed. Then, the remaining balls are arranged such that the last of color k-1 is before that, and so on. 

Alternatively, let's process the colors in the order of their last occurrence. For color k, the last ball must be the last in the entire sequence. Then, the remaining balls of color k can be placed anywhere before that. For color k-1, its last occurrence must be placed before the last ball of color k. And so on for each color.

So the approach is to process the colors from k down to 1. For each color i, the last ball must be placed in the current sequence such that it is after all the last balls of colors 1 to i-1, but before the last balls of colors i+1 to k (but since we process in order, maybe this can be handled step by step).

Hmm. Let's see. Let's start with color k. We have c_k balls. The last one must be placed at the end. The remaining (c_k - 1) balls can be placed anywhere in the positions before the end. Then, when processing color k-1, we need to place its last ball before the last ball of color k. But since the last ball of color k is fixed at the end, the last ball of color k-1 can be placed in any position except after the end. Wait, perhaps the correct way is to arrange all the balls in such a way that the last occurrence of each color is in order.

Another approach is to model this as a product of combinations. Let's consider that the total number of positions is the sum of all c_i. Let's denote this sum as total. The last ball of color k must be placed at position total. Then, the remaining (c_k -1) balls of color k can be placed anywhere in the first (total-1) positions. But we need to then place the last ball of color k-1 in the remaining positions (excluding the ones after the last color k's position, which is fixed). Wait, perhaps this can be thought of as inserting each color's balls step by step, considering the constraints.

So here's an idea inspired by combinatorics. The total number of valid sequences is the product for each color i of the combination (sum of the balls processed so far plus (c_i -1)) choose (c_i -1), multiplied by the product of factorials in some way.

Wait, let's think step by step. Let's process the colors in the order of their last occurrence. So first, we process color 1, then color 2, etc. Wait, no, the order in which their last positions are arranged is 1 < 2 < ... < k. So the earliest last is color 1, then color 2's last comes after, etc. So the order in which we process the colors could be 1, 2, ..., k. For each color i, when we add its balls, we need to place the last one after all the last ones of previous colors. But how?

Alternatively, process the colors in the order of their last occurrence, which is 1 first, then 2, up to k. Wait, no. Because the last occurrence of color k is the very end of the sequence. So perhaps processing the colors from k down to 1 is better. Let's try that.

Let's start with color k. The last ball of color k must be the last in the entire sequence. So among all c_k balls, one is fixed at the end. The remaining (c_k - 1) balls can be placed in the first (total_balls - 1) positions. Wait, but when processing other colors, their positions will affect how these are arranged. Hmm.

Alternatively, the problem can be broken down by considering the order in which the last occurrence of each color is placed. Let's think of the problem as building the sequence by inserting the colors in reverse order. For example:

1. Start with color k. Place all its c_k balls. The last one must be at the end. The rest can be anywhere before that. So the number of ways to arrange color k is (sum_{i=1 to k} c_i - 1) choose (c_k - 1). Because there are (total-1) positions before the last one, and we need to place (c_k -1) balls there.

But wait, the total number of positions is S = sum(c_i). When placing color k's balls, one is fixed at position S. The remaining (c_k-1) can be placed in the first (S-1) positions. So the number of ways is C(S-1, c_k-1).

Then, for color k-1, we have to arrange its c_{k-1} balls such that the last one is placed before the last of color k (which is at position S). So the last of color k-1 can be placed anywhere in the first (S-1) positions. But after placing color k's (c_k-1) balls in the first (S-1) positions, those positions are already partially filled.

Wait, maybe this approach isn't correct. Let me think again.

Alternatively, after processing color k, the total number of positions allocated is S. For color k-1, the last of its balls must be placed before the last of color k. So when adding color k-1's balls, the last of them must be placed in the existing positions minus the ones occupied by the last of the higher colors.

Wait, perhaps the correct approach is to process the colors in the order of their last occurrence. So starting with the color that has the earliest last occurrence (color 1), then color 2, etc., up to color k. For each color i, we have to place all their balls such that their last occurrence is after the previous ones but before the next ones.

But this seems tricky. Alternatively, here's a standard approach for such problems: the number of valid sequences is equal to the product of the multinomial coefficients, multiplied by the probability that the last occurrences are in the correct order.

Wait, but that might not be straightforward. Another idea is that the order of the last occurrences of the colors can be any permutation of the colors. The problem requires exactly one specific permutation (1, 2, ..., k). So the total number of valid sequences is the total possible sequences (multinomial) multiplied by the probability that the last occurrences are in the correct order. The probability is 1/(k!) if all possible permutations are equally likely. But is that the case?

No. For example, if there's only one ball of each color, then the order of the last occurrences is exactly the order of the colors in the sequence. So the probability is 1/k! in that case. But in general, when some colors have more balls, the probability might vary. So this approach might not work.

Hmm. Let's think of a different way.

Suppose we have to arrange all the balls such that the last occurrence of color i is before the last occurrence of color i+1 for each i. Let's model this step by step. Let's say we have colors 1 to k. The last occurrence of each color must form the sequence 1 < 2 < ... <k. 

So the last of color 1 is the earliest among all last occurrences, then color 2's comes after, etc. The key is that the last of color k is the very last in the entire sequence.

So here's a possible approach:

The process can be broken down into steps, each time adding the next color in the sequence. For each color i from 1 to k, we have to arrange their balls such that the last of color i is placed after the last of color i-1 and before the last of color i+1. But this seems vague.

Another approach: the problem can be viewed as a dynamic programming problem where we track the positions and the last occurrence times. However, given that the sum of all ci can be up to 1000 and k up to 1000, a DP approach with O(k^3) or similar might be feasible, but perhaps we need a smarter combinatorial formula.

Let me think again. Let's process the colors in order of their last occurrence. The correct order is 1, 2, ..., k. So the last ball in the entire sequence is color k. Then, the last ball of color k-1 must be placed before that. Then, the last ball of color k-2 before that, etc.

So here's a step-by-step plan:

1. Start with the last color, k. The last ball is fixed at the end. The remaining (c_k-1) balls can be placed anywhere in the first (sum(c_i) -1) positions.

But then, for the next color (k-1), the last ball must be placed before the last ball of color k. But since the last ball of color k is fixed at the end, the last ball of color k-1 can be placed anywhere in the first (sum(c_i) -1) positions. Then, the remaining c_{k-1} -1 balls are placed in the remaining positions.

Wait, but how to model this.

Let's consider the positions as being built in reverse order. For each color from k down to 1:

- For color i, the last occurrence must be placed after all previous colors' last occurrences (but since we're processing in reverse, perhaps this is easier).

Wait, perhaps the correct way is to consider that each color's last occurrence must come after all colors before it. So processing the colors in the order 1 to k, each time adding their balls such that their last is after the previous ones.

Wait, here's a possible approach from the editorial of a similar problem:

The number of valid sequences is the product for each i from 1 to k of (sum_{j=1 to i} c_j - 1 choose c_i -1) ), multiplied by the product of the factorials of (c_i -1) for each i. Wait, not sure.

Alternatively, when considering the colors in the order 1 to k, each time inserting their balls such that the last one is placed in the current sequence. Let's see:

- Initially, for color 1, there are c_1 balls. The last must be the earliest among all last occurrences. So the last ball of color 1 can be placed anywhere, but when adding other colors, their last balls must come after this. Hmm.

Alternatively, the problem can be viewed as building the sequence by inserting the colors one by one, ensuring that the last occurrence is placed correctly. Here's a possible way:

Suppose we have already processed the first i colors (1 to i) and have a partial sequence. Now, when adding the (i+1)th color, the last ball of color i+1 must come after all the last balls of the previous colors. So, for color i+1, the last ball must be placed in the remaining positions, which are after all the previous last balls.

But how to model this?

Another idea: the total number of valid sequences can be computed as follows. The last occurrence of each color must form the order 1 < 2 < ... <k. So the positions of the last occurrences are a1 < a2 < ... < ak, where ai is the position of the last occurrence of color i. The rest of the balls of each color can be placed anywhere before their last occurrence.

But how to count this?

For each color i, the last occurrence is at position ai, which must be after a_{i-1}. The remaining (c_i - 1) balls must be placed in the first (ai - 1) positions. However, ai must also be before a_{i+1}.

Wait, this seems complicated. But perhaps we can model the problem by considering the positions of the last occurrences and then arranging the remaining balls.

Here's a possible approach:

The steps are:

1. Choose positions for the last occurrence of each color in such a way that a1 < a2 < ... < ak. The last occurrence of color k is at position S (sum of all c_i). Then, a_{k} = S. a_{k-1} is between 1 and S-1, a_{k-2} between 1 and a_{k-1} -1, etc. But this seems like it would involve nested loops, which is not feasible for S up to 1000 and k up to 1000.

But perhaps there's a combinatorial formula that can compute this without enumerating all possibilities.

Another idea: the number of ways to arrange the last occurrences is the product of combinations. Let's say after placing the last occurrences of the first i colors, the total number of positions used is s_i. Then, for color i+1, the last occurrence must be placed after s_i. The remaining (c_{i+1} -1) balls can be placed anywhere in the first (s_{i} + ... ) positions. Wait, perhaps not.

Alternatively, the problem can be thought of as follows. The last occurrences of the colors must be ordered as 1, 2, ..., k. For each color i, after the last occurrence of color i-1, there must be at least one occurrence of color i.

But how to model the placement of the last occurrences. Let's consider that for each color i, the last occurrence is placed in the sequence such that it's after all the last occurrences of colors j < i and before all the last occurrences of colors j > i.

But since the order is fixed as 1 < 2 < ... <k, the last occurrence of color i is placed at some position a_i where a_1 < a_2 < ... < a_k = S.

The rest of the balls of color i can be placed in any of the positions before a_i, except that their positions must not conflict with other balls.

But how to count this? Let's see:

The total number of ways is the product over i from 1 to k of ( (a_i -1 - sum_{j < i} (c_j -1)) choose (c_i -1) ), multiplied by the multinomial coefficient for the remaining positions.

Alternatively, the problem can be transformed into a dynamic programming problem where we track the current sum of balls and the last position allocated. However, with k up to 1000 and sum of c_i up to 1000, this might not be feasible.

Wait, here's a possible solution approach:

The key observation is that the problem can be broken down into a product of combinations. Let's process the colors in the order of their last occurrence (1, 2, ..., k). For each color i, after placing the last occurrence of colors 1 to i-1, the last occurrence of color i must be placed after all of them. The remaining (c_i - 1) balls of color i can be placed in the remaining positions.

Wait, perhaps the solution is to multiply the combinations for each color step by step. Let's see:

Initialize the total number of ways as 1.

We start with color 1. The total positions available before considering any other colors are such that the last of color 1 must be placed somewhere. Wait, perhaps the order is not 1 to k but k to 1. Let's think again.

Let's process the colors in reverse order. Starting from color k, then color k-1, down to color 1.

For color k, the last occurrence is at the end (position S). The remaining c_k-1 balls can be placed anywhere in the first S-1 positions. So the number of ways is C(S-1, c_k-1).

Then, for color k-1, the last occurrence must be placed in the remaining positions (after placing color k's c_k-1 balls and the last of color k). Wait, but after color k's processing, we have S-1 positions filled (excluding the last position). Then, for color k-1, the last occurrence must be placed in the first (S - 1) positions, but also, after all previous colors (which are not processed yet? No, because we're processing in reverse order. Hmm, maybe this approach is not correct.

Alternatively, the correct order to process the colors is from the first color to the k-th color. Let's think of building the sequence by ensuring that the last occurrence of each color is after the previous ones.

For example:

Start with color 1. All c_1 balls must be placed in the sequence, with their last occurrence being the first among all colors. So the last occurrence of color 1 is placed somewhere. Then, the remaining c_1-1 balls are placed before that.

Then, for color 2, we need to insert its c_2 balls such that the last occurrence is after color 1's last. So the last of color 2 is placed in the sequence after the last of color 1. The remaining c_2-1 balls are placed before that.

But how to model the number of ways for each step.

Here's a way to model this:

The total number of ways is the product for each color i of ( (sum_{j=1 to i} c_j -1) choose (c_i -1) ), multiplied by the product of 1/(c_1! c_2! ... c_k! ), but I'm not sure.

Alternatively, after processing the first i colors, the sum of their balls is s_i. The next color i+1 has c_{i+1} balls. The last of color i+1 must be placed after the last of color i, which is at position s_i. So the last of color i+1 is placed in one of the s_i + 1 to s_i + c_{i+1} positions. Wait, but this seems unclear.

Wait, here's a key idea: for each color i, after placing the first i-1 colors, there are s = sum_{j=1 to i-1} c_j balls placed. The color i's last ball must be placed after all s positions, and the remaining (c_i -1) balls can be placed anywhere in the first (s + c_i -1) positions. So the number of ways to arrange color i's balls is C(s + c_i -1, c_i -1). Then, multiply these together for all colors.

Wait, that makes sense. Let's see:

Suppose we process the colors in order 1 to k. For color 1, we have s = 0 (sum of previous colors), so we need to place c_1 balls. The last of color 1 must be after all previous (which is none). So the last of color 1 can be in any position. Wait, but how does this model the last occurrence?

Wait, perhaps the correct way is to think that when adding color i, the last ball of color i must be placed after all balls of the previous colors. So the last ball of color i is the last ball in the current combined sequence of the first i colors.

So, when adding color i to the sequence of the first i-1 colors, the last ball of color i is placed at the end of the new combined sequence. The remaining (c_i -1) balls are placed among the previous positions (which are the sum of the first i-1 colors plus the (c_i -1) balls of color i). 

For example:

Processing color 1:

The first color's balls. The last one must be the last in the sequence. The other (c_1-1) balls are placed before. So the number of ways is 1 (since all the (c_1-1) balls are placed in the first (c_1-1) positions, and the last is at position c_1). So the combination is C(c_1-1, c_1-1) = 1.

Processing color 2:

The sum of previous colors is s = c_1. We need to insert c_2 balls. The last of color 2 must come after the last of color 1. So the last of color 2 is placed at the end of the new sequence (s + c_2). The remaining (c_2 -1) balls can be placed anywhere in the first (s + c_2 -1) positions. But those positions include the s positions from the previous colors and the (c_2 -1) balls. So the number of ways is C(s + c_2 -1, c_2 -1).

Then, the total number of ways up to color 2 is 1 * C(c1 + c2 -1, c2-1).

Continuing this way, for each color i, the number of ways is the product of C(s + c_i -1, c_i-1), where s is the sum of previous colors. 

Then, the total number of valid sequences is the product of these combinations for each i from 1 to k.

But wait, let's test this with the first example:

Sample input 1:

3

2

2

1

Processing colors 1, 2, 3.

Color 1: c1=2. s_prev=0. ways for color1: C(0 +2-1, 2-1) = C(1,1) =1.

sum becomes 0+2=2.

Color 2: c2=2. s_prev=2. ways: C(2 +2-1, 2-1) = C(3,1) =3.

sum becomes 2+2=4.

Color3: c3=1. s_prev=4. ways: C(4 +1-1,1-1) = C(4,0) =1.

Total ways: 1 * 3 *1 =3. Which matches the sample. So this seems correct.

Another sample: input 2:

4

1

2

3

4

Processing in order 1,2,3,4.

Color1: c1=1. ways: C(0+1-1, 0) = C(0,0)=1. sum becomes 1.

Color2: c=2. ways: C(1+2-1, 1) = C(2,1)=2. sum becomes 3.

Color3: c=3. ways: C(3+3-1, 2) = C(5,2)=10. sum becomes 6.

Color4: c=4. ways: C(6+4-1, 3) = C(9,3)=84. 

Total product: 1*2*10*84= 1680. Which matches the second sample.

So this formula seems to work. 

So the algorithm is:

1. Sort the colors in the order 1 to k. (But according to the problem statement, the colors are given as 1 to k, so no need to sort.)

2. For each color i from 1 to k:

   a. Compute the current sum of previous colors s_prev = sum_{j=1 to i-1} c_j.

   b. Compute the combination C(s_prev + c_i -1, c_i-1).

   c. Multiply this combination into the result.

3. The result is the product of all these combinations, modulo 1e9+7.

Now, the key challenge is to compute these combinations efficiently. The maximum s_prev + c_i -1 can be up to 1000 (since the total sum is up to 1000). So precomputing factorials and inverse factorials up to 1000 is feasible.

So the plan is to precompute factorial mod 1e9+7, inverse factorial mod 1e9+7, and then for each combination C(n, k) = fact[n] * inv_fact[k] * inv_fact[n-k] mod MOD.

But we need to compute combinations where n can be up to 1000, which is manageable.

So steps to implement:

- Precompute factorial up to 1000, inverse factorial up to 1000.

- Read k, then c1, c2, ..., ck.

- Compute the cumulative sum s as we process each color, and for each color compute the combination.

Multiply all combinations together mod 1e9+7.

Now, code-wise, here's how to proceed:

First, precompute the fact and inv_fact arrays up to 2000 (since sum_prev + c_i -1 can be up to sum_prev is up to 999 (sum of previous colors), and c_i can be up to 1000. So sum_prev + c_i-1 can be up to 999 + 1000-1= 1998. So precomputing up to 2000 should be sufficient.

Wait, but the maximum sum_prev is the sum of all previous c_j. Since the total sum is up to 1000, sum_prev can be up to (1000 - c_i). For example, the last color can have c_i up to 1000, sum_prev could be up to 0, but in that case, sum_prev + c_i-1 is 1000-1=999.

Wait, no. Suppose sum of all c_j is S, which is <=1000. For the i-th color, sum_prev is the sum of the first i-1 colors, which is S_prev. Then sum_prev + c_i -1 = S_prev + (c_i -1) = (sum_prev + c_i) -1. But sum_prev + c_i is part of the total S. So sum_prev + c_i <= S. So sum_prev + c_i -1 <= S-1. Since S<=1000, the maximum n is 999. So precomputing up to 1000 is sufficient.

So precompute factorial and inverse factorial up to 1000.

Wait, but 999 could be possible. So the maximum n for C(n, k) is 1000-1= 999.

Wait, no. For example, if sum_prev is 999 (sum of first i-1 colors is 999), and c_i is 1 (so c_i-1=0). Then the combination is C(999 +0, 0) =1. So n can be up to 999.

So precompute up to 1000 elements (indices 0 to 1000).

So code steps:

- Precompute fact, inv_fact.

- Read k, then read list c.

- Initialize res=1, s_prev=0.

- For each x in c:

   - n = s_prev + x -1

   - k_choose = x-1

   - if k_choose <0: 0 (but x is at least 1 according to input constraints, so x-1 is >=0).

   - compute comb = fact[n] * inv_fact[k_choose] * inv_fact[n - k_choose] % MOD

   - res = res * comb % MOD

   - s_prev += x

- Print res.

So now, precomputing fact and inv_fact up to 1000 is sufficient.

Now, how to precompute factorials modulo MOD=1e9+7.

In Python, this is straightforward. Precompute fact as:

fact[0] = 1

fact[i] = fact[i-1] * i % MOD for i >=1.

For inv_fact, compute inv_fact[1000] = pow(fact[1000], MOD-2, MOD), then go down to 0:

inv_fact[i] = inv_fact[i+1] * (i+1) % MOD.

This is efficient.

So the code would look like:

MOD = 10**9+7

max_n = 1000  # since sum_prev + x -1 can be up to 999+1000-1=1998? Wait, no. Wait, if sum_prev is up to 1000 (sum of previous c_i's), and x can be up to 1000. So sum_prev + x-1 could be up to 1000 + 1000-1 = 1999. Oh right! So my previous assumption was wrong. Because sum_prev can be up to (sum of first i-1 colors), and sum of all colors can be up to 1000. So sum_prev can be up to 1000, and then x can be up to 1000. So sum_prev + x-1 can be up to 1000 + 1000-1= 1999. So precomputing up to 2000 is necessary.

Wait, that's a mistake. So for example, the i-th color can be the first color, sum_prev is 0, and x can be 1000. So n =0+1000-1=999. But if sum_prev is 1000 (sum of previous colors is 1000), and x is 1, then sum_prev + x-1=1000+0=1000. But if sum_prev is 999, and x is 1000, then sum_prev +x-1=999+999=1998.

Wait, the maximum possible sum_prev is 1000-1 (since the sum of all c_i is up to 1000). Then, x can be up to 1000. So sum_prev can be 0 (if i is the first color), x can be up to 1000. Then sum_prev + x-1= 1000-1=999. Or if sum_prev is 500, x=500, sum_prev + x-1= 500+499=999. Wait, no. sum_prev is the sum of previous colors. So sum_prev + x <=1000. So sum_prev +x-1 = (sum_prev +x) -1 <=1000-1=999.

Wait, no. Because sum_prev is the sum of the first i-1 colors, and x is the i-th color's count. The total sum_prev +x can be up to 1000. So sum_prev + x-1= (sum_prev +x) -1 <=1000-1=999. So n can be up to 999. So precomputing up to 1000 is enough.

Ah! Because sum_prev +x = s_prev + x is the sum of the first i colors. Since the total sum is up to 1000, sum_prev +x <=1000. So sum_prev +x -1 <=999. Therefore, the maximum n is 999. So precomputing up to 1000 is sufficient.

So the code can precompute fact and inv_fact up to 1000.

But let me verify:

In the second sample input, when processing color4 with c=4:

sum_prev is 1+2+3=6, c=4. sum_prev +4-1=6+3=9. So n=9. The combination C(9,3) is 84.

But 9 is larger than 1000? No, 9 is way below 1000. So precomputing up to 1000 is okay.

Wait, sum_prev can be 1000- x, where x is the current color's count. For example, if sum_prev is 999 (sum of previous colors is 999), and x is 1. Then sum_prev +x-1=999+0=999. So the maximum n is 999.

So, precomputing up to 1000 is sufficient. So the code should precompute fact and inv_fact up to 1000.

Thus, the code would precompute fact and inv_fact up to 10^3.

So the code steps:

MOD = 10^9+7

max_fact = 1000

Compute fact up to max_fact, then inv_fact.

But wait, in the second sample, the combination for color3 is C(3 +3-1, 3-1) = C(5,2)=10. So 5 is within 1000. So no problem.

Thus, the code can proceed.

Now, let's code this.

Read k, then read k numbers.

Then, compute the product of combinations as per the steps.

Now, code:

Implement precompute:

MOD = 10**9 +7

max_n = 10**3

fact = [1]*(max_n+1)

for i in range(1, max_n+1):

    fact[i] = fact[i-1] *i % MOD

inv_fact = [1]*(max_n+1)

inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

for i in range(max_n-1, -1, -1):

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

Then, read k, then read c1, c2, ... ck.

Initialize res=1, s_prev=0.

for x in c:

    n = s_prev +x -1

    k_choose =x-1

    if n <0 or k_choose <0 or k_choose >n:

        comb=0

    else:

        comb = fact[n] * inv_fact[k_choose] % MOD

        comb = comb * inv_fact[n -k_choose] % MOD

    res = res * comb % MOD

    s_prev +=x

print(res)

But wait, in the case where x is 0? But according to the problem statement, ci >=1, so x is at least 1. So k_choose =x-1 >=0, and n= s_prev +x-1 >=s_prev >=0 (since s_prev is the sum of previous ci's which are all >=1, so s_prev starts at 0 and increases by each ci).

So the code is safe.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 + 7
    max_fact = 1000

    # Precompute factorial and inverse factorial modulo MOD
    fact = [1] * (max_fact + 1)
    for i in range(1, max_fact + 1):
        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1] * (max_fact + 1)
    inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
    for i in range(max_fact -1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    k = int(input_stream.readline().rstrip("\n"))
    c = [int(input_stream.readline().rstrip("\n")) for _ in range(k)]

    result = 1
    s_prev = 0

    for x in c:
        n = s_prev + x - 1
        k_comb = x - 1
        if n < 0 or k_comb < 0 or k_comb > n:
            comb = 0
        else:
            comb = fact[n] * inv_fact[k_comb] % MOD
            comb = comb * inv_fact[n - k_comb] % MOD
        result = result * comb % MOD
        s_prev += x

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1
2
3
4
""",
            "output": \
"""\
1680
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

Sample 2:

4

1

2

3

4.

Processing:

x=1: n=0+1-1=0. C(0,0)=1. res=1. s_prev=1.

x=2: n=1+2-1=2. C(2,1)=2. res=2. s_prev=3.

x=3: n=3+3-1=5. C(5,2)=10. res=20. s_prev=6.

x=4: n=6+4-1=9. C(9,3)=84. res=20*84=1680. Correct.

Thus, the code should work.

Now, check for edge cases.

Case when k=1: all balls are one color. The condition is automatically satisfied. The answer is 1.

Test case:

k=1

ci=5.

Output: 1. Because the last occurrence is the last element, but since it's the only color, the condition is satisfied. The code computes C(0+5-1,4) =C(4,4)=1. So correct.

Another test case: k=2, c1=1, c2=1.

The valid sequences are those where color1 comes before color2. There's only 1 way (since the last of color1 is first, last of color2 is second). The code computes:

For x=1: C(0,0)=1. res=1. s_prev=1.

For x=1: n=1+1-1=1. C(1,0)=1. res=1. So total 1. Which is correct.

Another test case: k=2, c1=1, c2=2.

The code:

x=1: C(0,0)=1. s_prev=1.

x=2: n=1+2-1=2. C(2,1)=2. So res=2.

The valid sequences are sequences where the last of color1 is before the last of color2.

The total possible sequences is (1+2)!/(1!2! )= 3. But how many are valid?

The valid sequences are those where the last color2 ball is after the color1's last ball (which is the first ball). So the last ball is color2. The possible sequences:

1: color1, color2, color2 → valid.

2: color2, color1, color2 → valid.

3: color2, color2, color1 → invalid (last of color1 is after last of color2).

So valid count is 2. Which matches the code's output.

Thus, the code works.
</think>

```python
MOD = 10**9 + 7
max_fact = 1000

# Precompute factorial and inverse factorial modulo MOD
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
for i in range(max_fact -1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

k = int(input())
c = [int(input()) for _ in range(k)]

result = 1
s_prev = 0

for x in c:
    n = s_prev + x - 1
    k_comb = x - 1
    if n < 0 or k_comb < 0 or k_comb > n:
        comb = 0
    else:
        comb = fact[n] * inv_fact[k_comb] % MOD
        comb = comb * inv_fact[n - k_comb] % MOD
    result = result * comb % MOD
    s_prev += x

print(result)
```
