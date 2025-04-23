<think>
Okay, let's see. The problem is about finding the number of possible original strings that could have been transformed into the given string s by Constanze's machine. The machine replaces 'w' with 'uu' and 'm' with 'nn'. All other characters are left as is. So, if the received string contains a 'w' or 'm', then it's invalid because those characters can't be produced by the machine. Because the original can't have them. Wait, no. Wait, the machine replaces 'w' and 'm' when they are pronounced. So if the original string had a 'w', the machine would output 'uu' instead. So, in the received string, if there's a 'w' or 'm', that's impossible. Because the machine would have replaced them. So the first thing to check is: if the input string s has any 'w' or 'm', then the answer is 0.

So first step: check if s contains 'm' or 'w'. If yes, output 0.

Otherwise, we need to look for sequences of 'u's and 'n's. Because these are the only letters that can have multiple possibilities. For example, a 'u' in the original would produce a 'u' in the output. But if the original had a 'w', which is replaced by 'uu', then in the output, two 'u's would appear. Wait no: no, the original can't have 'w' or 'm', because if it did, the machine would replace them. So the original can't have 'w' or 'm'—because the received string is produced by the machine, which replaces those letters. So any occurrence of 'w' or 'm' in the received string must be invalid, since the machine would have replaced them. So, if the received string has any 'w' or 'm', then answer is 0.

So the first step is to check the input string. If any character is 'w' or 'm', return 0.

Otherwise, the other letters can be part of the original, but for sequences of 'u's and 'n's, each consecutive pair could have been formed by a single 'w' or 'm' in the original. Wait, no. Let's think again. The original can have 'u's and 'n's, which would be written as is. But when the original has a 'w', the machine writes 'uu', and a 'm' writes 'nn'. So, in the received string, any occurrence of 'uu' could have been from a 'w' in the original, or from two 'u's in the original. Similarly for 'nn'—could be from 'm' or from two 'n's.

So for sequences of consecutive 'u's or 'n's, the number of possibilities depends on how many ways we can split that sequence into single 'u's or 'n's, or pairs that come from 'w's or 'm's. Wait, but the letters 'u' and 'n' can't be part of such pairs unless they are in the original. Hmm. Let's think.

Let me rephrase: the original string cannot contain 'w' or 'm'. Because when you pronounce those, the machine writes 'uu' or 'nn' instead. So the original string is made up of letters other than 'w' and 'm'. So the received string is the result of replacing each 'w' in the original with 'uu' and each 'm' with 'nn'. So the received string can't have any 'w's or 'm's. So the first check is correct.

So for the remaining cases (no 'w' or 'm' in s), the problem is to compute the product of the possibilities for each consecutive sequence of 'u's and 'n's.

Each consecutive group of same characters (only 'u' and 'n' can have such groups) contributes a certain number of possibilities. For example:

- For a group of 'u's of length k: each 'u' in the original contributes a 'u' in the received string, but each 'w' in the original contributes two 'u's. So the group in the received string must be made by a combination of 'u's and 'w's. But the original can't have 'w's. Wait, wait. No. Wait, the original can have 'w's and 'm's, but those are replaced by the machine. So if the original had a 'w', the machine writes 'uu'. So in the received string, any occurrence of 'uu' can be either from a 'w' or two 'u's. But the original can have 'w's. Wait, no! Wait, the original is the string that was pronounced. When you pronounce a 'w', the machine writes 'uu'. So the original can have 'w's and 'm's. Wait, but the original is the string that was input into the machine, which then produces the received string. So the original can have 'w's and 'm's, but those are replaced by 'uu' and 'nn' respectively. So, the received string is the transformed version. So, if the received string has a 'w' or 'm', then it's impossible, because the original can't have those letters (since the machine would have replaced them). Wait no: the original can have 'w's and 'm's. But when the machine is given those letters, it replaces them. So in the received string, those letters would not appear. So the presence of 'w' or 'm' in the received string implies that the original could not have produced them. Hence, output 0.

So, the original can have 'w's and 'm's. But their presence in the original will result in 'uu' or 'nn' in the received string. So the received string cannot have 'w' or 'm', which would make the answer 0.

So the problem now is to find the number of possible original strings that, when passed through the machine, produce the received string s. So, the original string can contain any letters except those that would generate 'w' or 'm' in the received string, which is impossible. Wait, no. The original can have any letters, including 'w' and 'm'. But when processed by the machine, each 'w' becomes 'uu', and each 'm' becomes 'nn'. So the received string is the transformed string. So the original is a string composed of letters (including 'w' and 'm') that, when transformed, gives s. So, s is the transformed string. So the original can have 'w' and 'm', but in the transformed string, those letters are replaced. Therefore, the received string (s) can't have 'w' or 'm' in it. So first check: if s contains 'w' or 'm', answer is 0.

So now, for the rest of the cases, we need to process the s and find possible splits into parts that could have come from the original's letters. For each group of consecutive 'u's or 'n's, we can have multiple possibilities. For example, a group of two 'u's could have come from a single 'w' in the original, or two 'u's. So each such group contributes a certain number of possibilities, which we multiply together for the total.

So, the key is to process each run of consecutive 'u's or 'n's and compute the number of ways to split them into possible original letters.

For example, consider a run of 'u's of length k. How many ways can this run be formed from the original string? Each 'u' in the original contributes 1 'u' to the string, and each 'w' contributes two 'u's. So the problem is similar to tiling a row of length k with tiles of size 1 or 2. The number of ways is the (k)th Fibonacci number, but with a twist. Wait, let's think. For a run of 'u's of length k: the original could have a combination of 'u's (each contributing 1) and 'w's (each contributing 2). So the number of ways is the number of ways to split the run into 1's and 2's, which is the Fibonacci sequence. For example:

k=1: only 1 way (one 'u')
k=2: two ways (two 'u's or one 'w')
k=3: three ways (three 'u's, or 'u' followed by 'w', or 'w' followed by 'u')
k=4: five ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
So for each group of 'u's of length k, the number of possibilities is the (k)th Fibonacci number, where F(1) = 1, F(2) = 2, F(3) = 3, etc. Similarly for groups of 'n's (since 'm' in the original gives two 'n's).

So for each group of consecutive 'u's or 'n's, if the length is l, then the number of possibilities is fib(l), where fib is a Fibonacci-like sequence where fib(1) = 1, fib(2) = 2, fib(3) = 3, fib(4) = 5, etc. So fib(n) = fib(n-1) + fib(n-2), with base cases fib(1)=1, fib(2)=2.

Wait, let's check:

fib(1) = 1 (only 1 way: 'u')
fib(2) = 2 (two 'u's or 'w')
fib(3) = 3: 1+1+1, 1+2, 2+1 → 3 ways.
fib(4) = 5: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 → 5 ways.

Yes. So the recurrence is fib(n) = fib(n-1) + fib(n-2), with fib(1)=1, fib(2)=2.

Similarly for groups of 'n's, since 'm' in the original gives two 'n's. So for each consecutive run of 'u's or 'n's, we calculate this Fibonacci value based on the length, and multiply all these values together. If the string has no such runs (like in the banana example, which has no runs of 'u's or 'n's longer than 1), then the total is 1.

So the approach is:

1. Check if s contains 'w' or 'm'. If yes, return 0.

2. Otherwise, split the string into runs of consecutive identical characters. For each run, if the character is 'u' or 'n', compute the number of possibilities for that run (using the fib sequence), and multiply all these possibilities together.

3. The result is the product modulo 1e9+7.

Now, the challenge is to compute the fib numbers efficiently, especially since the runs can be up to 1e5 in length. So precomputing a fib array up to 1e5+1 using dynamic programming would be feasible.

But since the input can have runs up to 1e5, but for each run we need to compute fib(k) where k is the length. So, for example, if the entire string is 'u's of length 1e5, then we need fib(1e5), which is a huge number, but since we need it modulo 1e9+7, we can compute it using a precomputed array.

So the plan is:

- Precompute a list of fib numbers up to 1e5, mod 1e9+7.

- Iterate through the input string, grouping consecutive characters.

- For each group, if the character is 'u' or 'n', compute the fib value of the group's length and multiply it into the result.

- All other characters (non 'u' or 'n') contribute a factor of 1, since they can't be part of any substitution (they were present as is in the original).

So the steps for code:

First, precompute the fib array. Let's initialize a list dp where dp[i] is the number of ways to split a run of length i. The recurrence is:

dp[0] = 1 (base case, but maybe not needed)
dp[1] = 1
dp[2] = 2
dp[i] = (dp[i-1] + dp[i-2]) % MOD for i >=3.

But wait, for a run of length k, the number of ways is dp[k], where dp[1] = 1, dp[2] = 2, etc. So we can precompute this up to 1e5.

Then, process the string:

Initialize result = 1.

Iterate through the string, tracking the current character and the length of the current run.

When the current character is 'u' or 'n', and the next character is the same, increment the length. When a different character is found, calculate the number of ways for that run (if the character is 'u' or 'n'), multiply the result by dp[length], then mod by MOD.

Other characters contribute nothing (since their runs are of length 1, and their contribution is 1).

Now, code structure:

Read s.

Check if 'w' or 'm' are in s. If yes, print 0.

Else:

Precompute dp.

Then, split into runs:

current_char = s[0], count = 1.

for i from 1 to len(s)-1:

if s[i] == current_char:

count +=1

else:

process the current run.

current_char = s[i], count=1.

At the end of loop, process the last run.

Processing a run: if current_char is 'u' or 'n', multiply the result by dp[count].

Now, the precomputation of dp:

MOD = 1e9 +7.

max_run_length can be up to len(s), which is 1e5.

So precompute dp up to 1e5.

Initialize dp[0] = 1 (maybe not needed, but for indices starting at 1).

Wait, for a run of length 1: dp[1] =1.

For length 2: dp[2] =2.

For length 3: 1+2=3.

So dp can be initialized as a list where dp[i] is the number of ways for a run of i characters.

So code:

MOD = 10**9 +7

max_len = 10**5

dp = [0]*(max_len +2)

dp[1] =1

if max_len >=2:

    dp[2] =2

for i in range(3, max_len +1):

    dp[i] = (dp[i-1] + dp[i-2]) % MOD

But for a string with a run of length 1e5, this would work.

But what if the input is 1e5 characters of 'u's? Then we need dp[1e5], which is computed.

But in Python, creating a list of 1e5 elements is manageable.

So, the code steps:

Read s.

Check for 'w' or 'm' in s. If found, output 0.

Else:

precompute dp.

then process each run.

Compute the product.

Output the product mod MOD.

Now, for the example input "ouuokarinn":

The runs are:

o (length 1, not u/n: factor 1)

u (length 2: factor 2)

o (1: factor 1)

k (1:1)

a (1:1)

r (1:1)

i (1:1)

n (2: factor 2)

So total is 2*2 =4, which matches the example.

Another example: "nnn" is a run of 3 'n's. The possible splits are:

- three 'n's (original has three 'n's: 1 way)

- a 'n' followed by 'm' (original has 'n' and 'm', but 'm' would generate 'nn', so the total length is 1+2=3. So the run would be 'n' + 'm' → 'n' followed by 'nn' gives total of 3 'n's. So in this case, the original would be 'nm' → which the machine would turn into 'n' + 'nn' → 'nnn'.

Wait, no. Original is 'nm' → the machine would write 'n' (from 'n') and 'nn' (from 'm'), resulting in 'nnn' → which is the input.

So for a run of 3 'n's, the possible originals are:

- 'nnn' (three 'n's) → contributes 1 way.

- 'nm' → 'n' followed by 'm' → 'n' + 'nn' → 'nnn'

- 'mn' → 'm' (gives 'nn') followed by 'n' → 'nnn'

Wait, no. Because original can't have 'm's. Wait no, the original can have 'm's. Because when the original has a 'm', the machine writes 'nn'. So the original can have 'm's. But the transformed string is the received s. So in the example input 'nnn', the original could be:

Case 1: three 'n's → transformed into 'nnn' (each 'n' is written as is).

Case 2: one 'm' and one 'n': 'mn' → 'nn' (from m) + 'n' → 'nnn'.

Case 3: one 'n' and one 'm': 'nm' → 'n' + 'nn' → 'nnn'.

Case 4: a 'm' and another 'n'? Wait, no. Wait, the original can be 'mmm' → but that would generate 'nnnnnn', which is longer than 3. So for a run of 3 'n's, possible originals are:

How can the original generate 3 'n's?

Each 'm' in the original produces two 'n's. So the sum of the counts (each 'n' in the original contributes 1, each 'm' contributes 2) must equal 3.

Let me see: Let x be the number of 'n's in the original, y the number of 'm's. Then x + 2y = 3.

Possible solutions:

y=0 → x=3 → 3 'n's → one way.

y=1 → x =1 → x + 2*1=3 → total x + y = 2 characters (1 'n' and 1 'm'). The 'n's and 'm's can be arranged in any order. So there are 2 possibilities: 'nm' and 'mn'.

So total possibilities for this case: 1 (all 'n's) + 2 (one 'n' and one 'm') → total 3 ways. Which matches the sample input where the answer is 3.

But according to our approach, the fib sequence for a run of 3 'n's is fib(3)=3. So yes, the code would correctly compute 3.

So the approach is correct.

Now, code:

We can precompute the dp array up to 1e5. Let's see.

But in Python, initializing a list of 1e5+1 elements is manageable.

Now, code steps:

Read s.

if any c in s is 'w' or 'm', print 0.

else:

precompute dp array.

then process each run.

Now, code:

MOD = 10**9 +7

s = input().strip()

if 'w' in s or 'm' in s:

    print(0)

else:

    max_len = len(s)

    # Precompute dp up to max possible run length, which is len(s)

    dp = [0]*(max_len +2)  # since run can be up to len(s) in length

    if max_len >=1:

        dp[1] =1

    if max_len >=2:

        dp[2] =2

    for i in range(3, max_len+1):

        dp[i] = (dp[i-1] + dp[i-2]) % MOD

    res =1

    n = len(s)

    if n ==0:

        print(0)

        exit()

    current_char = s[0]

    count =1

    for i in range(1, n):

        if s[i] == current_char:

            count +=1

        else:

            # process the current run

            if current_char in ['u', 'n']:

                res = res * dp[count] % MOD

            current_char = s[i]

            count =1

    # process the last run

    if current_char in ['u', 'n']:

        res = res * dp[count] % MOD

    print(res)

Wait, but what if the maximum run length is longer than the precomputed dp array? For example, if the input is a run of 1e5 'u's. Then, in the code above, when the code precomputes dp up to max_len, which is len(s) (which could be 1e5). So when len(s) is 1e5, the loop runs from 3 to max_len (1e5). So the dp array is correctly filled.

But in the code above, the code precomputes dp up to max_len, which is the length of the input. But the actual runs can't be longer than len(s), so the maximum possible run length is len(s). So precomputing up to max_len is sufficient.

But for example, if the input is a run of 1e5 'u's, the code will compute dp[1e5], which is the correct value.

Yes.

Testing the code against the examples.

First example:

Input: 'ouuokarinn'

Runs:

o (1, not u/n → factor 1)

u (2, which is 2 → factor 2)

o (1)

k (1)

a (1)

r (1)

i (1)

n (2 → factor 2)

Total 2*2=4 → correct.

Second example: 'banana' → no runs of u or n longer than 1. So product is 1 → correct.

Third example: 'nnn' → run of 3 'n's. dp[3] =3 → correct.

Fourth example: 'amanda' → contains 'm' → output 0.

So the code should work.

But wait, in the code, the precomputation for dp is done for up to max_len = len(s). But len(s) can be up to 1e5. So the code will create a dp array of len(s) +2 elements. For example, if the input is 1e5 characters, the code creates a dp array of size 1e5+2. So when i runs up to 1e5, which is okay.

But what if the input has runs that are longer than the precomputed dp array? For example, if the input is a single run of 1e5 'u's. Then the code precomputes dp up to 1e5, which is needed for that run.

Yes, so the code is correct.

But what about when the input has a run of length, say, 5. Let's see.

For example, for run length 5:

dp[1] =1

dp[2] =2

dp[3] = 3

dp[4] = 5

dp[5] = 8.

So 8 possibilities. Which is correct.

Another example: 'uuu' → run of 3. So 3 possibilities.

Yes.

So the code should be correct.

Now, code optimization. Precomputing the dp for each test case. But in this problem, each test case is handled once. So for each input, we precompute dp up to the maximum possible run length, which is len(s). Since len(s) can be 1e5, and each test case's code is separate, this is acceptable.

But precomputing for each test case may take O(n) time. But for n up to 1e5, and with each test case, the time is acceptable.

But perhaps we can precompute the dp array once up to 1e5, even if the actual runs are shorter, but that's not possible because the maximum possible run length is up to the input's length, which can be 1e5. But if we precompute up to 1e5 for every test case, it's O(1e5) per test case, but there's only one test case. So it's manageable.

But in Python, even for 1e5 iterations, it's acceptable.

Thus, the code should work correctly and efficiently.

Another possible optimization is to compute the dp array on the fly, as we process the runs, but that's more complicated and not necessary here. Precomputing once per test case is acceptable.

Thus, the code is correct.
</think>

```python
MOD = 10**9 + 7

s = input().strip()

if 'w' in s or 'm' in s:
    print(0)
else:
    n = len(s)
    if n == 0:
        print(0)
        exit()
    
    max_run = n
    dp = [0] * (max_run + 2)
    if max_run >= 1:
        dp[1] = 1
    if max_run >= 2:
        dp[2] = 2
    for i in range(3, max_run + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    result = 1
    current_char = s[0]
    count = 1
    
    for i in range(1, n):
        if s[i] == current_char:
            count += 1
        else:
            if current_char in ('u', 'n'):
                result = result * dp[count] % MOD
            current_char = s[i]
            count = 1
    if current_char in ('u', 'n'):
        result = result * dp[count] % MOD
    
    print(result)
```