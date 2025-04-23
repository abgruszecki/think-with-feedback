<think>
Okay, let's tackle this problem. Hmm. So the task is to compute the probability that S1 is lexicographically greater than S2, considering that some characters are erased (represented by 0) and can be replaced with any of the m symbols. We need to compute this probability modulo 1e9+7 as a fraction P/Q where Q is the modular inverse.

First, I need to understand how the probability is calculated. The key is to find all possible replacements of the 0s such that S1 becomes lex greater than S2.

Let's think about lex order. For two words of the same length, S1 is greater than S2 if at the first position where they differ, the character in S1 is larger than S2. So, we need to process the positions in order until we find such a position. If all positions are equal, then S1 is not greater.

So, the approach is to iterate through each character position from left to right. For each position i, we consider the possibilities of the characters in S1 and S2. Depending on whether the characters are fixed (non-zero) or variable (zero), we calculate the contribution to the probability.

At each position, we can have different scenarios:

1. Both S1[i] and S2[i] are fixed (non-zero). Then:
   a. If S1[i] > S2[i], then the result is definitely 1. Add the remaining possibilities (all previous positions were equal) multiplied by this case, and we can break.
   b. If S1[i] < S2[i], then the result is 0 for all possibilities where previous positions were equal. So we can break.
   c. If equal, proceed to the next position.

2. At least one of S1[i] or S2[i] is zero. Then, we need to compute the probability that, after replacing the zeros, the S1's character here is greater than S2's, given that all previous positions were equal. Multiply this by the product of probabilities that all previous positions were equal, and add to the total. Then, also compute the probability that the current position is equal, which contributes to the product for the next positions.

So the main idea is to process each position step by step, keeping track of the probability that all previous positions were equal (call this 'eq_prob'). For each position, compute two things:

- The probability that S1[i] > S2[i] given that all previous were equal. Multiply this by eq_prob and add to the result.
- The probability that S1[i] == S2[i] given that all previous were equal. Update eq_prob accordingly.

If at any step, the eq_prob becomes zero (because in a fixed position, the characters are not equal), we can break early.

So how do we compute the probability for each position?

For each position i, let's denote the possible values of a (S1's character) and b (S2's character):

Case 1: a is fixed (non-zero) and b is fixed (non-zero):

- If a > b: the contribution is eq_prob * 1 (since all previous were equal, and here a > b, so the total probability increases by eq_prob). Then, since the first differing position is found, we can break, as subsequent positions don't matter.
- If a < b: the contribution is 0, and since the previous positions were equal but this position is less, so no way. We can break.
- If a == b: the eq_prob remains the same, proceed.

Case 2: At least one is zero.

We need to compute the number of possible pairs (x, y) where x is the replacement for a (if a is zero) or a itself, y is the replacement for b (if b is zero) or b itself. Then, compute the probability that x > y, and the probability that x == y.

Let's model the possibilities:

For a zero in S1 (a is 0), the possible values are 1..m. Similarly for S2 (b is 0).

For example:

If a is 0 and b is 5: possible x is 1..m, y is 5. So the number of pairs where x > y is the number of x in [1..m] where x >5. So (m -5) if 5 < m, else 0. The total possible pairs is m (since x can be any of m, y is fixed).

If a is 3 and b is 0: possible y is 1..m. So the number of pairs where 3 > y is the count of y in 1..m where y <3. So (3-1) = 2, assuming m >=3. Otherwise, if m <3, then count is m (since all y would be less than 3). The total pairs is m (since y can be m options).

If both a and b are zero: possible x and y are both 1..m. The number of pairs where x > y is (m*(m-1))/2. Because for all possible pairs (x, y), exactly half of the non-equal pairs have x>y. The total pairs is m*m. The equal pairs are m (when x=y). So the count of x>y is (m^2 -m)/2. The probability here is (m^2 -m)/(2*m^2) = (m-1)/(2m). The equal probability is 1/m (since m pairs where x=y, out of m^2).

But wait, when both a and b are zero, the possible pairs are all possible (x, y) where x and y are 1..m. So:

Total pairs: m * m = m².

Number of pairs where x > y: sum_{x=1 to m} (x-1) ) → sum from 1 to m-1 → m*(m-1)/2.

Probability x > y: [m(m-1)/2] / m² = (m-1)/(2m).

Probability x == y: m / m² = 1/m.

So for each position, we need to calculate these probabilities.

Now, let's formalize this.

For each position i:

Compute prob_gt: the probability that a_i (after replacement) > b_i (after replacement).

Compute prob_eq: the probability that a_i == b_i.

The contribution to the answer is eq_prob * prob_gt.

The new eq_prob is eq_prob * prob_eq.

But we need to accumulate the answer as we go through each position.

So the algorithm steps:

Initialize answer = 0, eq_prob = 1.

For each position i from 0 to n-1:

   compute a = S1[i], b = S2[i]

   compute possible x and y options based on a and b.

   compute the number of possible pairs where x > y (count_gt), the number where x == y (count_eq), and total possible pairs (total).

   if total is 0 (but that can't happen since at least one is variable?)

   prob_gt = count_gt / total

   prob_eq = count_eq / total

   answer += eq_prob * prob_gt

   eq_prob = eq_prob * prob_eq

   if eq_prob becomes 0, break the loop (no more contribution possible)

So the main challenge is to compute count_gt, count_eq, and total for each a and b in S1 and S2.

Let's think about all possible cases for a and b.

Case 1: a is fixed (a != 0) and b is fixed (b != 0):

   if a > b: count_gt = 1 (since only possible x=a, y=b. So if a > b, prob_gt is 1. So answer += eq_prob * 1, and after that, the remaining positions don't matter. So we can break the loop here.

   elif a < b: count_gt =0. So answer += eq_prob *0 (no contribution). Then, the eq_prob becomes 0 (since a and b are fixed and unequal). So we break the loop.

   else (a == b): count_gt=0, count_eq=1. So answer += 0, and eq_prob remains same. So proceed.

Case 2: a is fixed, b is 0:

   x is a, y can be 1..m.

   total = m (since y can be m possibilities).

   count_gt is the number of y in 1..m where a > y.

   So count_gt = max(0, a -1) → since y can be 1, 2, ..., a-1. If a-1 >=1, else 0.

   For example, a=3, m=5: y can be 1,2 → count_gt=2.

   a=1: count_gt=0.

   count_eq is 1 if a is in 1..m (since y can be a). So count_eq=1.

   So prob_gt = count_gt / m.

   prob_eq = 1 / m.

Case 3: a is 0, b is fixed:

   x can be 1..m, y is b.

   total = m.

   count_gt is the number of x in 1..m where x > b.

   So count_gt = max(0, m - b).

   For example, b=3, m=5: x can be 4,5 → count_gt=2.

   If b >=m: count_gt=0.

   count_eq is 1 if x is equal to b → x can be in 1..m, so count_eq is 1 if b is in 1..m (since x is allowed). Since b is fixed and non-zero (since case 3 is when a is 0 and b is fixed), then b is between 1 and m. So count_eq=1.

   prob_gt = count_gt / m.

   prob_eq = 1/m.

Case 4: a is 0 and b is 0:

   x and y can be 1..m.

   total = m * m.

   count_gt = (m*(m-1))//2 → as earlier.

   count_eq = m.

   prob_gt = count_gt / (m*m) → (m-1)/(2m).

   prob_eq = 1/m.

So for each of these cases, we can compute count_gt, count_eq, and total.

Once we have prob_gt and prob_eq for the current position, multiply the current eq_prob by prob_gt and add to the answer. Then, update eq_prob by multiplying by prob_eq.

But how to handle the fractions? Since n can be up to 1e5 and m up to 1e5, we can't compute fractions directly. Instead, we need to perform modular arithmetic with the probabilities. But since all operations are multiplicative and additive, we can represent probabilities as fractions under modulo 1e9+7, using modular inverses.

So the key is to represent all probabilities as numbers in the modular field. For example, when we have a probability of (count_gt / total), this is equivalent to (count_gt * inverse(total)) mod MOD.

So the plan is to precompute the modular inverses where necessary, and for each position, compute the required terms.

Let's think about the steps in code:

We need to process each position in order, keeping track of the current eq_prob (product of probabilities that all previous positions were equal). For each position, compute the contribution to the answer as eq_prob multiplied by the probability that this position is the first differing one with a > b.

So for each position:

Compute the contribution (eq_prob * prob_gt) and add to the answer.

Update eq_prob as eq_prob * prob_eq.

If at any step, the current a and b (after handling) make eq_prob zero (like fixed a < fixed b), then break early.

Now, the modular inverses. The MOD is 1e9+7. So when we need to compute fractions like (a / b) mod MOD, it's equal to (a * inverse(b)) mod MOD, where inverse(b) is the modular inverse of b modulo MOD.

We can precompute inverses up to 2e5 (since m can be up to 1e5, and m^2 could be up to 1e10, but perhaps in practice, the inverses can be computed on the fly using pow(b, MOD-2, MOD) when needed, as 1e5 is manageable with the pow function in Python.

But in Python, pow(b, MOD-2, MOD) is efficient even for large exponents because it uses exponentiation by squaring.

So for each case, we need to compute:

prob_gt = (count_gt * inv_total) % MOD

prob_eq = (count_eq * inv_total) % MOD

where inv_total is the inverse of the total possible pairs for that position.

So let's code each case.

First, let's handle all possible cases for a_i and b_i.

For each a_i and b_i:

If a_i is 0, then x can be any of 1..m. If not 0, x is fixed.

Similarly for b_i.

Let's code this.

Now, let's think about the code structure.

Read n and m.

Read S1 as a list (a list of integers).

Read S2 as a list.

Initialize answer = 0

eq_prob = 1 (modular 1, which is 1 mod MOD)

MOD = 1e9 +7.

For each i in 0 to n-1:

   a = S1[i]

   b = S2[i]

   if a !=0 and b !=0:

       if a > b:

           answer += eq_prob (since this position is the first where a> b, all previous equal. So the probability contribution is eq_prob * 1).

           answer %= MOD

           eq_prob = 0

           break

       elif a < b:

           eq_prob =0

           break

       else:

           continue (prob_gt is 0, prob_eq is 1. So no change to answer or eq_prob)

   else:

       compute count_gt, count_eq, total.

       inv_total = pow(total, MOD-2, MOD)

       prob_gt = (count_gt * inv_total) % MOD

       prob_eq = (count_eq * inv_total) % MOD

       contribution = (eq_prob * prob_gt) % MOD

       answer = (answer + contribution) % MOD

       eq_prob = (eq_prob * prob_eq) % MOD

       if eq_prob ==0:

           break

After processing all positions, return answer.

So the key is to compute count_gt, count_eq, and total for each a and b that are not both fixed (since that case is handled first).

Let's code each possible scenario.

Case 1: a and b are both fixed (non-zero). Handled as described.

Case 2: a is fixed, b is 0.

Then, x is a, y can be 1..m.

count_gt is the number of y in 1..m where a > y → a-1.

But if a is 1, then count_gt is 0.

count_eq is 1 (y must be a). But if a is not in 1..m, but wait, in the problem statement, the symbols are 1..m, so a and b are either 0 or in 1..m. So if a is non-zero, it's between 1 and m.

So count_gt = a-1.

count_eq =1.

total = m.

Case 3: b is fixed, a is 0.

Then, y is b, x can be 1..m.

count_gt is the number of x where x > b → m - b.

count_eq=1.

total =m.

Case 4: both a and b are 0.

count_gt = m*(m-1) // 2.

count_eq = m.

total = m*m.

So now, let's code these cases.

But in code, for each a and b:

if a ==0 and b ==0:

   total = m * m

   count_gt = m*(m-1) //2

   count_eq = m

elif a ==0 and b !=0:

   total = m

   count_gt = max(0, m - b)

   count_eq = 1 if 1 <= b <=m else 0 (but since b is in S2, which is 0 or in 1..m, and here it's not zero, so 1)

elif a !=0 and b ==0:

   total = m

   count_gt = a -1

   count_eq =1

Wait, but for a in S1, which is 0 or 1..m. So when a is not zero, it's in 1..m.

So for a non-zero, count_gt is (a-1) because for S1's a and S2's y (since S2's b is zero), x is a, and we need y < a. So the count is a-1.

But if m < a-1? No, since a is in 1..m. Wait, a is fixed to 1..m, so for a non-zero, a is in 1..m. So when S2's b is zero, then the count_gt is (a-1) possible y values (since y can be 1,2,..., a-1). So yes.

For example, a=3, m=5: y can be 1,2 → count_gt=2.

But if a=5 and m=3, then a is invalid (since m is 3, a can't be 5). But according to the problem statement, S1 and S2's elements are 0 <= ai <=m. So if a is non-zero, it's in 1..m. So in code, the input is given such that a and b are 0 or in 1..m.

So for case where a is non-zero and b is zero:

count_gt = a-1.

But if a is 1, then count_gt is 0.

So that's correct.

Similarly, when a is zero and b is non-zero:

count_gt = m - b.

Because x can be any of 1..m, and y is fixed to b. So x has to be greater than b. So how many x's are there? max(0, m - b) if b is in 1..m.

But since b is non-zero, and part of S2, which is 0 or 1..m, then here b is in 1..m. So m -b can be up to m-1.

For example, b=3, m=5: m -3 =2 (x=4,5).

So code:

if a and b are both non-zero: handle as first case.

Else, for the current a and b:

if a is non-zero (fixed), and b is zero:

count_gt = a-1

total = m

prob_gt = (a-1) * inv(m) mod MOD.

prob_eq = 1/m.

Else if a is zero, and b is non-zero:

count_gt = m - b

prob_gt = (m -b) * inv(m) mod MOD.

Else (both zero):

count_gt = m*(m-1)//2

prob_gt = (m*(m-1)//2) * inv(m*m) mod MOD.

So in code, for each position i:

We can have code like:

if a !=0 and b !=0:

   if a > b:

       answer = (answer + eq_prob) % MOD

       break

   elif a < b:

       break

   else:

       continue

else:

   compute count_gt, count_eq, total.

   inv_total = pow(total, MOD-2, MOD)

   prob_gt = (count_gt * inv_total) % MOD

   prob_eq = (count_eq * inv_total) % MOD

   answer = (answer + eq_prob * prob_gt) % MOD

   eq_prob = (eq_prob * prob_eq) % MOD

   if eq_prob ==0:

       break

So that's the code structure.

Now, what about possible integer overflows? For m up to 1e5, m*(m-1) can be up to 1e10, which is manageable in Python's integers.

But for m up to 1e5, m*(m-1)//2 is 5e9, which when multiplied by inv(m^2) can be handled modulo 1e9+7.

So the code should handle that.

Now, let's test the sample inputs.

Sample 1:

Input:

1 2

0

1

So n=1, m=2.

S1 is [0], S2 is [1].

Processing position 0:

a=0, b=1 (non-zero).

So a is zero, b is non-zero.

count_gt = m -b = 2 -1 =1.

count_eq = 1.

total = m =2.

prob_gt = 1 / 2.

prob_eq = 1/2.

So contribution is eq_prob (1) * 1/2 → 1/2.

So answer is 1/2.

Which is 500000004 mod 1e9+7.

Sample 2:

Input:

1 2

1

0

So a is 1, b is 0.

So count_gt is a-1 =0. So prob_gt is 0. Contribution is 1 *0 →0.

prob_eq is 1/m = 1/2. So eq_prob becomes 1 * 1/2 →1/2.

But since n=1, after processing, the answer is 0. Which matches the sample.

Sample 3: a longer input. Let's not test here.

So code seems correct.

Now, let's code this.

But first, precompute MOD = 1e9+7.

Now, code:

Read n, m.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s1 = list(map(int, input_stream.readline().rstrip("\n").split()))

    s2 = list(map(int, input_stream.readline().rstrip("\n").split()))

    MOD = 10**9 +7

    answer =0

    eq_prob =1

    for a, b in zip(s1, s2):

        if a !=0 and b !=0:

            if a >b:

                answer = (answer + eq_prob) % MOD

                eq_prob =0

                break

            elif a <b:

                eq_prob =0

                break

            else:

                continue

        else:

            # compute count_gt, count_eq, total

            if a ==0 and b ==0:

                total = m * m

                count_gt = m * (m-1) //2

                count_eq =m

            elif a ==0:

                # b is non-zero

                count_gt = m - b

                total = m

                count_eq =1

            else:

                # a is non-zero, b is zero

                count_gt = a -1

                total =m

                count_eq =1

            inv_total = pow(total, MOD-2, MOD)

            prob_gt = (count_gt * inv_total) % MOD

            prob_eq = (count_eq * inv_total) % MOD

            answer = (answer + eq_prob * prob_gt) % MOD

            eq_prob = (eq_prob * prob_eq) % MOD

            if eq_prob ==0:

                break

    print(answer % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2
1
0
""",
            "output": \
"""\
0
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

</think>

```python
MOD = 10**9 + 7

n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

answer = 0
eq_prob = 1  # Probability that all previous characters were equal

for a, b in zip(s1, s2):
    if a != 0 and b != 0:
        if a > b:
            answer = (answer + eq_prob) % MOD
            eq_prob = 0
            break
        elif a < b:
            eq_prob = 0
            break
        # else: continue, as a == b
    else:
        if a == 0 and b == 0:
            total = m * m
            count_gt = m * (m - 1) // 2
            count_eq = m
        elif a == 0:
            # b is non-zero and in 1..m
            total = m
            count_gt = max(0, m - b)
            count_eq = 1
        else:  # b == 0, a is non-zero and in 1..m
            total = m
            count_gt = a - 1
            count_eq = 1
        
        inv_total = pow(total, MOD-2, MOD)
        prob_gt = (count_gt * inv_total) % MOD
        prob_eq = (count_eq * inv_total) % MOD
        
        answer = (answer + eq_prob * prob_gt) % MOD
        eq_prob = (eq_prob * prob_eq) % MOD
        
        if eq_prob == 0:
            break

print(answer % MOD)
```
