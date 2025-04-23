<think>
Okay, let's try to figure out this problem. So, the problem is about selecting one digit from each of b blocks, and the concatenated number mod x should equal k. We need to find the number of ways to do this, considering that each occurrence of a digit in a block counts as a separate way.

Hmm, the constraints are big here. Let's look at the input sizes. The number of blocks b can be up to 1e9, which is huge. And x can be up to 100. So, we need a solution that's efficient even when b is that large. The other variables like n (number of digits per block) is up to 50,000, which is manageable, but not trivial.

First, let's think about the modulus properties. When you concatenate digits, each step is like multiplying the current number by 10 and adding the new digit. But since we're dealing with mod x, maybe we can model this using dynamic programming where each state is the current remainder modulo x. Because the order of the blocks matters (since each is a digit in a higher position), but since all blocks are the same, maybe we can find a pattern or matrix exponentiation approach.

Wait, but each block is the same. So, the transitions between remainders after each block can be represented in a matrix. Then, using matrix exponentiation would allow us to handle the exponentiation in O(x^3 * log b) time, which is feasible since x is up to 100.

Let me break this down. Let's consider the digits in each block. For each possible digit d in the block, when processing a block, each current remainder r transitions to (r * 10 + d) mod x. But since all blocks are processed in sequence, the multiplicative factor for each step is 10. However, each block is the same. So, the transition for each block is the same.

Wait, but the first block is the most significant digit. For example, with two blocks, the first digit is multiplied by 10^1, the second by 10^0. Wait, no. If you have two blocks, the first digit is the first one selected, then the second. So the number is d1 * 10^(b-1) + d2 * 10^(b-2) + ... + db * 10^0. So each step, the multiplier for the digits depends on their position.

But when dealing with modulus, this can be simplified. Because 10^m mod x can be precomputed for each exponent m. But since there are b blocks, the exponents would be from 0 to b-1. However, since x can be up to 100, the exponents cycle after some period due to Euler's theorem. But when b is up to 1e9, we need a way to compute the cumulative effect of all the blocks.

Alternatively, perhaps we can model the transitions between the remainders for each block. Let's think in terms of dynamic programming:

The state after processing i blocks is a remainder r. For each next block, we choose a digit d, and the new remainder becomes (current_r * 10^{b-i} + d) mod x. Wait, but the exponents here depend on the position of the block. So for the first block, the multiplier is 10^{b-1} mod x, then 10^{b-2}, etc. But this seems complicated because each block has a different multiplier.

Wait, but since all blocks are the same, perhaps the order in which we process them can be adjusted. Alternatively, perhaps we can model the problem in reverse, starting from the least significant digit. Let's think: each digit contributes d * 10^power, where power depends on its position. But if we process the digits in the order they are chosen, each step would multiply the current value by 10 and add the new digit. Wait, that's exactly how modular arithmetic works. For example:

Suppose we have a number formed by digits d1, d2, d3. Then the value mod x is (((d1 * 10) + d2) * 10 + d3) mod x. So each step, the remainder is (current_remainder * 10 + d) mod x. So regardless of the position, each block is processed as multiplying the current remainder by 10 and adding the digit. But wait, that would be the case if each digit is added as the next least significant digit. Wait, no. Let's see:

If you have digits d1, d2, d3 in order, then the number is d1 * 100 + d2 * 10 + d3. So the first step is d1, then multiply by 10 and add d2, then multiply by 10 again and add d3. So the processing order is correct. So for each block, processing in order, the current remainder is multiplied by 10 and then added the digit, mod x.

But in this problem, each block is processed in order. So the first block's digit is the first digit (most significant), so when processing it, you multiply by 10^{b-1} mod x. Wait, but that's not the case. Because, for example, in the first step (block 1), the digit contributes d * 10^{b-1}, the next block's digit contributes d * 10^{b-2}, etc. So the exponents decrease as we process each block.

But how can we model this using dynamic programming? Because each step's multiplier is different. However, if we process the digits in reverse order (from the least significant digit to the most), each step would multiply by 10^1. Let's think: if the digits are processed in reverse order (the last block first), then each step's contribution is (digit * 10^0) + (previous sum * 10^1). So for example, the digits d3, d2, d1 would be processed as:

Initial state 0. Then add d3 (since it's the last digit, 10^0). Then multiply by 10 and add d2 (so total is d3 *10 + d2), then multiply by 10 and add d1 (so total is (d3 *10 + d2)*10 +d1 = d3*100 + d2*10 +d1). Which is the same as the original number. So processing in reverse order allows us to model each step as multiplying by 10 and adding the new digit. So the modulus can be computed step by step, each time (current_remainder * 10 + new_digit) mod x.

But in this problem, all blocks are the same. So processing them in reverse order or original order may not matter. Wait, but each block is processed once, and all are the same. So perhaps we can model the transitions for a single block, and then use matrix exponentiation to compute the effect of applying this transition b times.

Yes, that's the key. Because each block contributes a digit, and the processing can be modeled as for each block, the current remainder is updated as (current_remainder * 10 + digit) mod x. But since each block is the same, and all digits in each block are the same (no, each block is a copy of the same digits, but each time you can choose any digit from the block), so the transition depends on the digits available in the block.

Wait, each block is the same in the sense that the digits available in each block are the same as the others. So for each block, when you process it (choosing a digit from that block), the possible transitions from a remainder r to (r*10 + d) mod x for each possible d in the block, multiplied by the count of d in the block.

So the approach would be:

- For each possible digit d in the block, compute the possible transitions. Then, model the entire process as a state transition, where each state is the current remainder mod x, and each step (block) transitions according to the possible digits in the block.

But since there are b blocks, and each block is processed once, we need to compute the transitions for each block. However, since all blocks are the same, the transitions are the same for each step. So, the overall transition is the same for each block, and we can model the entire process as raising the transition matrix to the b-th power.

But how to model the transitions. Let's think in terms of dynamic programming:

We can represent the state as the remainder mod x. For each block, the state transitions are based on selecting a digit d in the current block. So, for each possible current remainder r, after processing a block, the new remainder s is (r * 10 + d) mod x. The number of ways to reach s from r is the sum over all d in the block of (count of d in the block) multiplied by the number of ways to reach r before this block.

So, the transition can be represented as a matrix where the entry T[r][s] is the number of ways to transition from r to s in a single block. Then, after applying this matrix b times, the initial state (0, because before any blocks are processed, the remainder is 0) would have the answer in the state k.

Wait, but the initial state is before any blocks. For the first block, the remainder is (0 * 10 + d) mod x = d mod x. So after the first block, the remainder is d mod x. Then, for the second block, it's (d1 * 10 + d2) mod x, and so on.

So the initial state is 0. Then, each block is processed, updating the state as (current_state * 10 + d) mod x.

So the DP approach is:

dp[i][r] = number of ways to get remainder r after i blocks.

The base case is dp[0][0] = 1.

For each block, we update the dp as follows:

For each possible remainder r in dp[i-1], and for each digit d in the block, compute the new remainder s = (r * 10 + d) mod x. Add the count of d multiplied by dp[i-1][r] to dp[i][s].

But with b up to 1e9, this approach is impossible to compute directly. So we need a way to compute this efficiently, using matrix exponentiation or some other method.

Each transition from r to s can be modeled as a transition matrix. Since x can be up to 100, the matrix is 100 x 100, which is manageable. Then, raising this matrix to the power of b and multiplying by the initial state (vector) gives the final counts.

But first, we need to construct the transition matrix for a single block. The transition matrix M is such that M[r][s] is the number of ways to transition from remainder r to s by selecting a digit from the block.

So, for each r in 0..x-1, and for each d in the digits of the block, compute s = (r * 10 + d) mod x. Then, for each such s, add the count of d to M[r][s].

So, first, we precompute the counts of each digit in the given block. For example, if the digits are [3,5,5,1], then the counts are 3:1, 5:2, 1:1.

Once we have the counts, for each digit d and its frequency f, we can compute for each possible remainder r, the new remainder s = (r * 10 + d) mod x, and accumulate f * the current count for r into s.

Once the transition matrix M is built, the total transitions after b blocks is M^b. Then, the answer is the entry in the initial state (0) transitioned to state k.

Wait, the initial state is a vector where all entries are 0 except dp[0] = 1. After multiplying by M^b, the resulting vector's entry at position k is the answer.

Yes. So this seems manageable.

So the steps are:

1. Preprocess the counts of each digit in the given block.

2. Build the transition matrix M where M[r][s] is the sum of frequencies of digits d such that (r * 10 + d) mod x == s.

3. Compute the matrix M raised to the power of b.

4. Multiply the initial vector (which is [1, 0, ..., 0] if x is not 0, but wait, initial remainder is 0 before any blocks. So after zero blocks, the remainder is 0. Then, after each block, we process the transition.

Yes. So the initial vector is a 1 in the 0 position. Then, applying M once gives the state after one block. Applying M b times gives after b blocks.

So the process is:

result_vector = initial_vector * (M)^b

The answer is result_vector[k]

So the key steps are building the transition matrix M, then exponentiating it to the bth power.

Now, how to implement matrix exponentiation efficiently. Since the matrix is x by x, which is up to 100x100, even with exponentiation via binary exponentiation, it's feasible. The time complexity would be O(x^3 * log b), which for x=100 is 1e6 operations per log b step (since 100^3 is 1e6). log2(1e9) is about 30, so total operations would be 3e7, which is acceptable.

But how to represent the matrix. Since the transitions are multiplicative and additive, we can use a list of lists, where each entry is a list of integers mod 1e9+7.

But wait, the entries in the matrix represent the number of transitions, so when multiplying matrices, it's a matter of combining transitions. For example, matrix multiplication here is similar to counting paths: for each step, the number of ways to go from r to s via t is the product of the ways from r to t in the first matrix and from t to s in the second matrix, summed over all t. So matrix multiplication here is standard, but using addition and multiplication modulo 1e9+7.

So the matrix exponentiation part is standard.

So the steps for code:

- Read n, b, k, x.

- Read the list of digits a.

- Count the frequency of each digit in a. So, for each d in a, count[d] += 1.

- Precompute the transition matrix M. For each possible current remainder r (from 0 to x-1), and for each digit d with frequency f, compute s = (r * 10 + d) % x. Then, M[r][s] += f. All operations are mod 1e9+7.

Wait, but the matrix M is for transitions after processing one block. So for each possible r, and each d in the block, the next remainder is (r * 10 + d) mod x, and since each d can be chosen in f ways, M[r][s] accumulates f for each (r, d) pair.

Once the matrix M is built, we can compute M^b. Then, the initial vector is [1, 0, ..., 0], and multiplying this vector by M^b gives the number of ways to reach each remainder after processing b blocks. The answer is the entry at position k.

But wait, the initial remainder is 0. So for each block, the transition is applied. So yes.

But there's a catch here. Because each block contributes a digit that is multiplied by 10^ (the number of remaining blocks after it). Wait, no. Because when processing in the order of the blocks (each step is a block), the way the remainder is calculated is as follows:

For example, after the first block, the remainder is (d1) mod x.

After the second block, it's (d1 * 10 + d2) mod x.

After the third, (d1 * 100 + d2 * 10 + d3) mod x.

But when processing each block as a step, the calculation is (current_remainder * 10 + d) mod x. But that's equivalent to building the number digit by digit, with each new digit added to the right (the least significant digit). Which would be correct for the order of the blocks.

Wait, but the problem says that each digit comes from a block. The order of the blocks is such that the first block's digit is the first digit (most significant), and the last block's digit is the least significant.

But when processing each block step by step, the current remainder is multiplied by 10 and added to the new digit. This would correspond to the new digit being added to the right (less significant). But that's the reverse of the actual digit positions.

For example:

blocks are processed in order block1, block2, block3. The digits are d1, d2, d3. The number is d1*10^2 + d2*10^1 + d3*10^0. But when processing each block, the first step is d1, then (d1 *10 +d2), then ((d1*10 +d2)*10 +d3). Which is d1*10^2 +d2*10 +d3. So the order is correct. So the way of processing each block as multiplying the current remainder by 10 and adding the digit is correct.

So the model is correct.

Therefore, the approach with matrix exponentiation is correct.

Now, the code steps:

First, count the frequencies of each digit in the given block. So for the input digits, create a frequency dictionary.

Then, build the transition matrix M. For each r in 0..x-1, and for each digit d with frequency f, compute s = (r * 10 + d) % x. Then, M[r][s] += f, modulo 1e9+7.

Once M is built, compute the matrix exponentiation to the power of b.

The initial state is a vector where the 0th position is 1, others are 0. Then, multiply this vector by M^b, and the result at position k is the answer.

But how to handle matrix exponentiation. Let's think about representing the matrix as a list of lists. The multiplication is done as follows:

Given two matrices A and B, their product C is such that C[i][j] = sum_{k=0 to x-1} A[i][k] * B[k][j] mod MOD.

The identity matrix is such that identity[i][j] is 1 if i == j, else 0.

The matrix exponentiation can be done via binary exponentiation.

But in code, since the matrices can be up to 100x100, it's manageable.

But wait, the transition is multiplicative. So perhaps there's a better way. For example, for each block, the transition is the same, so after exponentiation, we get the combined transition after all blocks.

So the code outline is:

Read n, b, k, x.

Read the digits, count the frequencies.

If x == 1, then everything mod 1 is 0. But since k is 0 mod x, if x is 1, then the problem requires the sum of all possibilities (since any number mod 1 is 0). But according to the constraints, x >=2. So x is at least 2, so no need to handle x=1.

But code should handle x=1 correctly, but according to input constraints, x >=2.

So build the transition matrix.

Then compute M^b.

Then multiply the initial vector (with 1 at 0) with M^b.

The code needs to handle matrix exponentiation.

But for the vector multiplication, since the initial vector is a single row, we can model it as a vector and then multiply by the matrix.

Alternatively, since matrices are applied as linear transformations, the order is important. So the initial vector is a row vector. Each matrix multiplication is done on the right. So the code should handle this.

Wait, in matrix terms, the state is represented as a row vector. When you multiply by a matrix, it's a row vector multiplied by the matrix. So the order is:

new_state = current_state * matrix.

So the code should implement matrix multiplication in that order.

So the code for matrix multiplication:

def multiply(a, b):
    result = [[0]*x for _ in range(x)]
    for i in range(x):
        for k in range(x):
            if a[i][k] == 0:
                continue
            for j in range(x):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
    return result

Wait, but in matrix multiplication, the element (i,j) is sum over k of a[i][k] * b[k][j]. So the code for multiplying two matrices should compute this. So the above code is correct.

But for exponentiation, we can implement it with a helper function.

But let's proceed.

So the code steps:

Read the input.

Handle the case where x is 1 (but according to the problem statement, x is at least 2, so perhaps not needed).

Compute the frequency of each digit.

Build the transition matrix M.

Compute M^b.

Multiply the initial vector (0's except 1 at 0) by M^b.

Output the result at position k.

So the code outline:

MOD = 10**9 +7

n, b, k, x = map(int, input().split())
digits = list(map(int, input().split()))

from collections import defaultdict
freq = defaultdict(int)
for d in digits:
    freq[d] +=1

# build transition matrix
x_size = x
matrix = [[0]*x_size for _ in range(x_size)]
for r in range(x_size):
    for d, cnt in freq.items():
        s = (r *10 + d) %x
        matrix[r][s] = (matrix[r][s] + cnt) % MOD

# function to multiply two matrices
def mat_mult(a, b):
    res = [[0]*x_size for _ in range(x_size)]
    for i in range(x_size):
        for k in range(x_size):
            if a[i][k] ==0:
                continue
            for j in range(x_size):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    return res

# function to compute matrix^power using binary exponentiation
def mat_pow(mat, power):
    # Initialize result as identity matrix
    result = [[0]*x_size for _ in range(x_size)]
    for i in range(x_size):
        result[i][i] = 1
    current = mat
    while power >0:
        if power %2 ==1:
            result = mat_mult(result, current)
        current = mat_mult(current, current)
        power = power //2
    return result

# Compute matrix^b
matrix_b = mat_pow(matrix, b)

# initial vector is [1, 0, 0, ..., 0]
# multiply the initial vector by matrix_b
# the result is the sum over all r of initial[r] * matrix_b[r][k]
# but initial is only 1 at position 0, so the answer is matrix_b[0][k]

ans = matrix_b[0][k] % MOD
print(ans)

Wait, no. Because the initial vector is a row vector [1, 0, 0, ... 0], and the matrix is applied as a row vector multiplied by the matrix. So the result is the sum over each entry in the row multiplied by the matrix's columns.

So the initial vector is a row vector. So after multiplying by matrix_b, which is the result of M^b, the resulting row vector gives the counts for each remainder. So the entry at position k is the answer.

But in the code above, the matrix is stored as a 2D list where matrix[i][j] is the number of ways to go from i to j in one step. So, when you multiply the matrices, the resulting matrix is the transitions after two steps. So the matrix exponentiation gives the transitions after b steps.

Thus, the initial vector is [0, 0, ..., 1 (at position 0), ... 0], and when multiplied by matrix_b, the result is the sum of matrix_b[0][k], which is indeed the answer.

Wait, no. The matrix represents the transitions. The initial vector is [1, 0, 0, ... 0], and matrix_b[0][k] is the number of ways to go from 0 to k in b steps. So the answer is exactly matrix_b[0][k].

So in the code above, after computing matrix_b, the answer is matrix_b[0][k], modded by MOD.

But in the code, the matrix_b is built as mat_pow(matrix, b), which represents the transitions after b steps. So the code is correct.

Testing the sample inputs:

First sample:

Input:
12 1 5 10
3 5 6 7 8 9 5 1 1 1 1 5

The digits are [3,5,6,7,8,9,5,1,1,1,1,5]. The frequency counts for digits:

3:1,5:3,6:1,7:1,8:1,9:1,1:4.

x=10, so the transition matrix M is for each r in 0-9, and each digit d.

For example, for r=0:

Each digit d, the next remainder is (0*10 +d) mod 10 = d mod 10.

So for each digit d, the frequency is added to M[0][d%10]. So for d=3, 5, etc.

So after building M, M[0][3] +=1 (from digit 3), M[0][5] +=3 (from the three 5's), etc. Then, the initial state is [1,0,0,...0]. After one block (b=1), the result is the sum of all transitions from 0. So the answer is the sum of frequencies of digits where d mod 10 ==k. Which in this case k=5. So digits 5 mod10=5 (frequency 3), and 5's frequency is 3. So answer is 3. Which matches the first sample.

Second sample:

Input:

3 2 1 2

6 2 2

Digits are [6,2,2]. So frequencies:6:1, 2:2. x=2.

Each block contributes transitions. For each r in 0-1, and digits 6,2,2.

For each r, s = (r*10 + d) mod 2. Since 10 mod 2 is 0. So (r*0 +d) mod2 = d mod2.

So for any r, the next s is d mod2.

So for the digits 6 (mod2 is 0), 2 (mod2 0), 2 (mod2 0). So frequency for d mod2 0 is 3 (1+2=3), and no 1's.

So transition matrix M for r=0: s=0 is 3, s=1 is 0. For r=1: same as for r=0.

So after two blocks, the matrix M^2 is computed as M multiplied by M.

But let's compute M:

For all r (0 and 1), M[r][0] =3, M[r][1] =0.

So M^2 is:

For any row r, each entry is sum over k of M[r][k] * M[k][s].

For M^2, each entry for row r and column s is:

For s=0: M[r][0]*M[0][0] + M[r][1]*M[1][0] = 3*3 +0*3=9.

s=1: 3*0 +0*0=0.

So after two blocks, the transition from 0 to 0 is 9. So the answer is 0 for k=1. Which matches sample 2.

Third sample:

Input:

3 2 1 2

3 1 2

Digits are 3,1,2. So frequencies:3:1,1:1,2:1. x=2.

Each digit's mod2 is 1,1,0.

So for any r, the next s is (r*10 +d) mod2. 10 mod2 is 0. So s = (0*r +d) mod2 = d mod2.

So for each r, M[r][s] is sum of digits d with d mod2 = s. So for all r, M[r][1] is 2 (digits 3 and 1 mod2=1), and M[r][0] is 1 (digit 2 mod2=0).

So M is for all r:

M[r][0] =1, M[r][1]=2.

But then, after two blocks, the transitions would be:

M squared is:

For each entry (i,j):

sum_{k} M[i][k] * M[k][j].

For i=0, j=0:

M[0][0]*M[0][0] + M[0][1]*M[1][0] = 1*1 +2*1 =3.

j=1: 1*2 +2*2= 2 +4=6.

But since x=2, the matrix for M is:

row 0: [1, 2]

row 1: [1, 2]

So M^2 would be:

row 0: [ (1*1 +2*1) mod MOD, (1*2 +2*2) mod MOD ] → [3, 6]

row 1: same as row 0, since all rows are the same.

So the matrix after two blocks is M^2, and the initial vector is [1,0]. The product is:

[1*3 +0*3, 1*6 +0*6] → [3,6].

But wait, initial vector is [1,0], multiplied by M^2 (which is the same as M multiplied by M):

But wait, the initial vector is [1,0], and the matrix is M^2. So the result is:

sum over k of initial[k] * M^2[k][s].

So for s=0: initial[0] * M^2[0][0] + initial[1] * M^2[1][0] → 1*3 +0*3 =3.

s=1: 1*6 +0*6=6.

So the total is 3 ways for remainder 0, 6 for remainder 1. Since k is 1, the answer is 6. Which matches the third sample.

Thus, the code should work.

So, the code is correct. Now, to handle the case where x=1, but according to the problem statement, x is at least 2, so no need. But the code would handle it.

Now, implement the code.

But wait, in Python, for large x=100, building the matrices and performing matrix multiplications could be time-consuming. However, since the matrix size is small (100x100), it's manageable.

Potential optimizations:

- Precompute the (10 mod x) once, but in the code, each step is (r*10 +d) mod x. But since in the transition matrix, the 10 is multiplied by r mod x, which is r. So (r*10) mod x is (r * (10 mod x)) mod x. So precomputing 10 mod x once, then using that for all transitions.

But in the code, for each r and d, the calculation is (r *10 +d) mod x. So for each r in 0..x-1, compute (r *10) mod x, which can be precomputed once as (10 mod x) * r mod x.

But in code, it's the same as (r *10) %x +d) %x. So perhaps precomputing 10 mod x once and then using that.

Yes. So for each r, (r * 10) mod x is equal to (r * (10 mod x)) mod x. So let's compute 10_pow = 10 %x. Then, for each r, compute (r *10_pow + d) %x.

This can save some computation, especially for x larger than 10. But in code, the original approach is to compute (r *10 +d) mod x. But in code, 10 can be up to 1e9, but mod x is handled automatically.

So in the code, replace:

s = (r *10 +d) %x

with:

s = (r * pow(10, 1, x) + d) %x

But in practice, this is the same as (r*10 +d) modx. So no change is needed.

But perhaps precompute 10 mod x and multiply by r. That's better.

So:

mod_10 = 10 %x

for r in range(x):
    term = (r * mod_10) %x
    for d, cnt in freq.items():
        s = (term + d) %x
        matrix[r][s] = (matrix[r][s] + cnt) % MOD

This way, we compute 10 mod x once, and then for each r, compute (r*mod_10) modx. Which is the same as (r*10) modx.

This is a minor optimization but correct.

So the code can be adjusted accordingly.

But for the sample input 3, when x=2, mod_10 is 0. So for any r, (r*0) mod 2 is 0, then adding d mod2 gives d mod2, as before.

So this optimization is correct.

Thus, the code can be modified to precompute 10 mod x.

Another possible optimization is to precompute for all possible (r, d) pairs, but given x is up to 100 and digits up to 9, it's manageable.

So, the code:

mod_10 = 10 % x

for r in range(x):
    term = (r * mod_10) % x
    for d, cnt in freq.items():
        s = (term + d) % x
        matrix[r][s] = (matrix[r][s] + cnt) % MOD

This will compute the same s as before.

So the code is adjusted.

So the final code should include this optimization.

Another thing to note: in the matrix multiplication function, it's possible to precompute mod once, but the code already includes modulo MOD.

Now, testing the code with the samples.

Sample 1:

n=12, b=1, k=5, x=10.

mod_10 is 10%10=0.

Each r in 0..9:

term is (r *0) mod10=0.

s=0 +d mod10.

Thus, for each digit d, s is d mod10.

Thus, for the digits in sample1, the frequency counts are:

3:1,5:3,6:1,7:1,8:1,9:1,1:4.

So for s=5, the sum is 3 (from d=5, frequency 3).

Thus, matrix[0][5] =3. So after exponentiation, the answer is 3.

Sample 3:

x=2, mod_10 is 0.

For any r, term is 0. So s = (0 +d) mod2.

Thus, for digits 3,1,2:

d mod2: 1,1,0. So frequencies for mod2 0 is 1 (digit 2), mod2 1 is 2 (digits 3 and 1).

Thus, for any r, M[r][0] =1 (digit 2), M[r][1] =2 (digits 3 and 1).

After two blocks, matrix squared:

Each entry for M^2 is:

For row i, column j:

sum over k of M[i][k] * M[k][j].

For i=0 (row 0):

M[0][0] =1, M[0][1] =2.

So for column 0:

1 * M[0][0] (which is 1) + 2 * M[1][0] (which is 1) → 1*1 +2*1=3.

Column 1:

1*2 +2*2=2+4=6.

So matrix_b is M squared. So matrix_b[0][1] is 6.

Thus, answer is 6.

So code is correct.

Thus, the code should work.
</think>

```python
MOD = 10**9 + 7

n, b, k, x = map(int, input().split())
digits = list(map(int, input().split()))

from collections import defaultdict
freq = defaultdict(int)
for d in digits:
    freq[d] += 1

# Precompute 10 mod x
mod_10 = 10 % x

# Build transition matrix
x_size = x
matrix = [[0] * x_size for _ in range(x_size)]
for r in range(x_size):
    term = (r * mod_10) % x
    for d, cnt in freq.items():
        s = (term + d) % x
        matrix[r][s] = (matrix[r][s] + cnt) % MOD

def mat_mult(a, b):
    res = [[0] * x_size for _ in range(x_size)]
    for i in range(x_size):
        for k in range(x_size):
            if a[i][k]:
                for j in range(x_size):
                    res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
    return res

def mat_pow(mat, power):
    result = [[0] * x_size for _ in range(x_size)]
    for i in range(x_size):
        result[i][i] = 1
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, mat)
        mat = mat_mult(mat, mat)
        power //= 2
    return result

matrix_b = mat_pow(matrix, b)

print(matrix_b[0][k] % MOD)
```