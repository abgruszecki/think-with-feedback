<think>
Okay, let's see. The problem is to find the number of valid n-length DNA chains where certain pairs of consecutive nucleotides are forbidden. The constraints are quite tight, especially since n can be up to 1e15. So, we need an efficient way to compute this, probably using matrix exponentiation for fast computation of the recurrence.

Hmm. The first thing that comes to mind is that for each position in the DNA chain, the choice of the next nucleotide depends only on the previous one. That's a classic transition state problem. So, the total number of valid sequences can be represented as a state transition matrix, where each state is the last nucleotide used, and transitions are allowed if the pair isn't forbidden. Then, the problem reduces to finding the number of paths of length n-1 in this transition graph, starting from any possible nucleotide (since the first nucleotide can be any of the m options).

Wait, right. Because for n=1, the answer is m. For n>1, each step depends on the previous nucleotide. So, the recurrence can be modeled using a matrix where the entry (i,j) is 1 if j can follow i, and 0 otherwise. The total number of sequences after n steps (which is n-1 transitions) would be the sum of all possible transitions from each starting state.

So the approach would be:

1. Create a transition matrix where allowed transitions are 1, forbidden are 0.
2. Compute the (n-1)th power of this matrix.
3. Multiply the initial state vector (which is a vector of all 1s, since each starting nucleotide is allowed) with this matrix, sum the results, and take modulo 1e9+7.

But since m can be up to 52, the matrix size is 52x52. Matrix exponentiation for exponents up to 1e15 is feasible here because the exponentiation by squaring method has O(log n) steps, and each step involves matrix multiplication of 52x52 matrices, which is O(m^3) per step. For m=52, m^3 is about 140,000, which multiplied by log2(1e15) (~50 steps) gives around 7 million operations. That's manageable within the time constraints.

So the steps are:

- Read the forbidden pairs and build the adjacency matrix (allowed transitions).
- The initial state is a vector of size m, each entry 1 (since each nucleotide can be the first).
- The transition matrix T is such that T[i][j] is 1 if j can follow i, 0 otherwise.
- The total number of sequences is the sum of all entries in T^(n-1) multiplied by the initial vector. Since the initial vector is all ones, the result is the sum of all entries in the matrix T^(n-1) multiplied by 1 for each starting state. Wait, actually, when you raise the matrix to the (n-1)th power, each entry (i,j) in the matrix represents the number of ways to go from i to j in (n-1) steps. So the sum of all the entries in the matrix after exponentiation multiplied by the initial vector (which is 1 for each state) gives the total sum. Because the initial count for each state is 1 (since the first character is each possible nucleotide), then after exponentiation, each entry (i,j) gives the ways to transition from i to j in (n-1) steps. So the total is sum over all i (initial states) and j (final states) of the matrix[i][j]. So the sum of all elements in the matrix is the answer when n >=1. Wait, no. Wait, the initial vector is a row vector [1, 1, ..., 1], and the matrix is multiplied as T^(n-1). Then, the resulting vector after multiplying would give the sum for each j of the number of paths of length n-1 ending at j. The sum of this vector would be the total number of sequences. But how does the matrix exponentiation work here?

Alternatively, the transition matrix is a m x m matrix. The initial state vector is a row vector with all 1s. After each step, the vector is multiplied by the transition matrix. So after (n-1) steps, the vector's entries sum up to the total number of valid sequences. Therefore, the total is the sum of the entries in the vector (initial vector) multiplied by T^(n-1).

Wait, correct. Let's think for n=1: the answer is m. For n=2, the answer is sum over all i of the allowed transitions from i. For n=3, it's sum over i, j, k where i can transition to j, j can transition to k. Which is equivalent to the sum over all i of (sum_j T[i][j] * sum_k T[j][k}) ), which is the same as (initial vector) * T^2, and then sum the entries.

So the approach is correct. The answer for n >=1 is the sum of all elements in the matrix T^(n-1), multiplied by the initial vector (all ones). But since the initial vector is all ones, the product is the sum of all entries in the matrix T^(n-1). So for each n >=1, the answer is the sum of all elements in the matrix T^(n-1) multiplied by the initial vector. Wait, no. Let me clarify.

The initial vector is a row vector of size m, with each entry 1. The matrix is m x m. The product after one step (n=2) would be the vector [sum_{i} T[i][0], sum_{i} T[i][1}, ...], which is the sum of each column. Wait, no. Matrix multiplication for a row vector V (1x m) multiplied by matrix T (m x m) gives a row vector (1 x m) where each entry j is sum_{k} V[k] * T[k][j]. So for the initial vector V = [1,1,...,1], after multiplying by T, each entry j is the sum of T[k][j] for all k. Which is the sum of the j-th column. But the total sequences for n=2 is sum over all possible transitions from any first nucleotide. So that's correct.

For example, in the first test case:

Sample Input 1:

3 3 2

ab

ba

So the forbidden transitions are a followed by b, and b followed by a.

The transition matrix T is 3x3 (nucleotides 1,2,3). So:

T[1][2] = 0 (a to b is forbidden)

T[2][1] = 0 (b to a is forbidden)

All other transitions are allowed.

So the matrix T has 1s except for those two positions.

The initial vector is [1,1,1].

For n=3 (n-1=2 steps), we compute T squared.

T squared's entry (i,j) is the number of ways to go from i to j in two steps.

The sum of all entries in T squared will be the total number of sequences for n=3. Let's see:

Each entry in T^2[i][j] is sum_{k} T[i][k] * T[k][j]. So for example, if i=1 (a), then T[i][k] is 1 for all k except 2. Then, for each j, the entry is sum of T[1][k] * T[k][j], but T[1][2] is 0.

So for the first sample:

Original T:

Row 1 (a's transitions): [1,0,1] (since a can go to a, b is forbidden, c is allowed)

Row 2 (b's transitions): [0,1,1] (b can't go to a)

Row 3 (c's transitions): [1,1,1] (no forbidden transitions from c)

So T squared:

For each cell (i,j), sum over k of T[i][k] * T[k][j].

Let's compute the first row of T^2:

i=1 (a). For each j:

j=1: T[1][1] * T[1][1] + T[1][2] * T[2][1] + T[1][3] * T[3][1] = 1*1 + 0*0 + 1*1 = 2

j=2: 1*0 + 0*1 +1*1 = 0 +0 +1 =1

j=3: 1*1 +0*1 +1*1 =1+0+1=2

So first row is [2,1,2], sum is 5.

Second row (i=2):

j=1: T[2][1]*T[1][1] + T[2][2] * T[2][1] + T[2][3]*T[3][1] → 0*1 +1*0 +1*1 → 1.

j=2: 0*0 +1*1 +1*1 → 0+1+1=2.

j=3: 0*1 +1*1 +1*1 → 0+1+1=2. Sum is 1+2+2=5.

Third row (i=3):

Each j is sum of T[3][k] * T[k][j], for all k.

T[3][k] is 1 for all k. So:

j=1: T[1][1] + T[2][1] + T[3][1] → 1 +0 +1=2.

j=2: T[1][2] (0) + T[2][2] (1) + T[3][2] (1) → 0+1+1=2.

j=3: T[1][3] (1) + T[2][3] (1) + T[3][3] (1) → 3.

So third row is [2,2,3], sum is 7.

So total sum of all entries in T^2 is 5 (row 1) +5 (row 2) +7 (row3) =17, which matches the sample output.

So yes, the approach is correct.

Now, the steps to implement this:

1. Convert the nucleotide characters to their corresponding indices. For example, 'a' is 0 (since 1 becomes index 0?), or maybe 1-based. Wait, in the problem statement, nucleotides are numbered from 1 to m, but for code, it's easier to have them 0-based. So 'a' corresponds to 0, up to 'z' (25). 'A' is 26 (since 27-1=26), up to 'Z' (51 for m=52). So need a helper function to convert a character to the index (0-based up to m-1).

Wait, the problem says nucleotides 1-26 are a-z, 27-52 are A-Z. So for example, 'a' is 1, 'b' is 2, ..., 'z' is 26. 'A' is 27, etc. So when m is 52, all letters are allowed.

But when m is less than 52, say m=3, then only a, b, c are allowed (as per first sample where m=3). So in the code, the forbidden pairs are given as two characters. So for each pair, we need to convert each character to their respective nucleotide number, but then check if the number exceeds m. But the problem statement says that all forbidden pairs' nucleotides are ≤m. So we can ignore any pairs where the characters represent numbers beyond m. But according to the problem statement, the input is guaranteed to have all forbidden pair nucleotides ≤m.

So in code, the steps are:

- Read n, m, k.

- Read the next k lines. For each line, parse the two characters.

- For each character, convert to its number (1-52). Then subtract 1 to make it 0-based (since it's easier for array indices).

But wait, the code needs to map each character to its corresponding number. So 'a' is 1, 'b' is 2, ..., 'z' is 26. 'A' is 27, ..., 'Z' is 52. So for a character c, if it's lowercase, the number is ord(c) - ord('a') +1. If uppercase, it's 26 + (ord(c) - ord('A') +1) → 26 + 1-26 is 27-52. So for example, 'A' is 27.

But since the code uses 0-based indices (for building the transition matrix), we subtract 1. So 'a' (1) becomes 0, 'b' (2) becomes 1, ..., 'A' (27) becomes 26, etc.

But the problem says that the forbidden pairs' nucleotides cannot be more than m. So after converting a character to its number, we check if it's ≤m. But according to the input constraints, it's guaranteed that all forbidden pairs' nucleotides are ≤m. So we can safely proceed.

Once we have the forbidden pairs (as 0-based indices), we can build a transition matrix. The transition matrix is a m x m matrix, where allowed[i][j] is 1 if the transition from i to j is allowed. Initially, all transitions are allowed (1), then for each forbidden pair (a, b), we set allowed[a][b] = 0.

Once the matrix is built, the problem becomes finding the sum of all entries in the matrix exponentiated to (n-1) steps, multiplied by the initial vector. But wait, the initial vector is [1,1,...,1], so when multiplied by T^(n-1), the result is a vector where each element j is the number of sequences ending with j. Summing these gives the total.

Alternatively, since the initial vector is [1, 1, ..., 1], the total is the sum of all entries in T^(n-1) multiplied by 1 for each starting i. Wait, no. The initial vector is a row vector of size m. So the product after exponentiating the matrix to the (n-1)th power is:

result_vector = initial_vector * matrix_power

Each entry j in result_vector is the number of sequences of length n that start with any nucleotide (since initial is all 1s) and end with j, after (n-1) transitions.

So the total is the sum of the entries in the result_vector. Which is the same as the initial_vector multiplied by the matrix_power and summed.

But how to compute this efficiently?

The matrix exponentiation approach is to compute the matrix T^(n-1), and then multiply the initial vector (all 1s) with this matrix, then sum the entries.

But matrix exponentiation can be done, and then the sum can be computed.

However, for efficiency, perhaps we can represent the matrix exponentiation in a way that tracks the sum. Alternatively, since the initial vector is all 1s, the sum after exponentiation is equal to the sum of all entries in the matrix, but multiplied by the initial vector. Wait, no. Let's think again.

Suppose n=1: T^0 is identity matrix. The sum of the initial vector (all 1s) multiplied by identity matrix is m.

n=2: sum of entries in T^1 (original matrix) is the total.

n=3: sum of entries in T^2 matrix.

Wait, no. Because the initial vector is [1,1,1], the product of the initial vector with the matrix T^(n-1) gives a row vector where each entry j is the sum of the j-th column of T^(n-1). Then summing all entries in this row vector gives the sum of all columns, which is the same as the sum of all entries in T^(n-1).

Wait, no. Because for a matrix M, when you multiply a row vector of ones [1,1,...,1] with M, each entry j is the sum of column j of M. Then the sum of the row vector entries is the sum of all elements in M. So yes. Therefore, the sum of the entries in the matrix T^(n-1) is the same as the sum of the entries in the row vector [1,1,...1] * T^(n-1), which is the total number of sequences.

So the answer is the sum of all elements in T^(n-1).

Therefore, the code can compute the matrix exponentiation, then sum all the entries in the resulting matrix.

So the steps are:

- Read n, m, k.

- If n is 0, output 0? But according to the constraints, n ≥1. Because the input constraints are 1 ≤n ≤1e15.

So n is at least 1. So for n=1, the answer is m.

For n>1, the answer is the sum of all entries in T^(n-1), modulo 1e9+7.

So the problem reduces to:

1. Create the adjacency matrix T, which is m x m, where T[i][j] = 1 if the transition from i to j is allowed (i.e., the pair (i+1, j+1) is not forbidden). Wait, no. Because in the code, the indices are 0-based. So if a forbidden pair is 'ab', which corresponds to a=1, b=2. So in code, the indices are 0 and 1. So the forbidden transition is from 0 to 1. So T[0][1] =0.

So for each forbidden pair, after converting the two characters to their 0-based indices a and b, we set T[a][b] =0. All other transitions are allowed initially (set to 1).

So the code needs to:

- Initialize a m x m matrix with all 1s.

- For each forbidden pair, set T[a][b] =0.

Once the matrix is built, compute T^(n-1), then sum all its entries.

The key is to compute the matrix exponentiation efficiently.

In Python, implementing matrix exponentiation for 52x52 matrices can be done with standard methods. However, considering the constraints (n up to 1e15), and each matrix multiplication being O(m^3), for m=52, m^3 is 140,608 operations. Log2(1e15) is about 50 steps, so 50 * 140,608 = ~7 million operations. Python can handle that.

But the code must be optimized. So, for matrix multiplication, using lists of lists, and pre-allocating the result matrices.

The modulus is 1e9+7, so all operations are done modulo this number.

So, code outline:

- Read n, m, k.

- If n ==0, output 0 (but n ≥1).

- If n==1, output m % MOD.

- Else, build the transition matrix.

- Compute the matrix exponent (n-1) steps.

- Sum all elements in the matrix mod MOD.

But wait, the matrix exponent is T^(n-1), and the sum is the sum of all its elements. So the code will compute that.

Now, for converting the characters to indices:

For a character c:

if it's lowercase: index = ord(c) - ord('a') → 0-25. Then add 0, since the original number is 1-26. So the code should compute the number as (ord(c) - ord('a') + 1) if lowercase, or (26 + ord(c) - ord('A') +1) for uppercase. Then subtract 1 to get 0-based index.

Wait, for example, 'a' is 1 in the problem, so code:

if c is lowercase: num = ord(c) - ord('a') +1 → 'a' →1, 'b'→2, etc.

if uppercase: num = 26 + (ord(c) - ord('A') +1) → 'A' gives 27, etc.

Then, subtract 1 to get 0-based index (so 'a' becomes 0, 'A' becomes 26, etc.)

So the code for converting a character to index:

def char_to_index(c):

    if c.islower():

        num = ord(c) - ord('a') +1

    else:

        num = 26 + ord(c) - ord('A') +1

    return num -1  # 0-based

But need to ensure that the converted index is less than m. But according to the problem statement, the forbidden pairs' nucleotides are <=m, so the code can proceed.

So, code steps:

Read n, m, k.

If m ==0: impossible, but according to input constraints, m ≥1.

If k>0:

for each of k lines:

   read a string of two characters, a and b.

   a and b are converted to their 0-based indices.

   if a and b are within 0 to m-1:

       transition_matrix[a][b] =0

Else:

   (but input is guaranteed that all forbidden pairs are within m, so no need to check)

Once the transition matrix is built, compute the matrix raised to (n-1)th power.

Sum all elements of the resulting matrix mod 1e9+7.

So, now the code.

Implementing matrix exponentiation in Python:

The matrix will be a list of lists. For each step in exponentiation, we multiply matrices using modulo.

But for large exponents, exponentiation by squaring is the way to go.

First, write a matrix multiplication function that takes two matrices A and B, returns their product mod MOD.

Then, the identity matrix for exponentiation (when the exponent is zero). But since in our case, the exponent is (n-1), which can be zero (if n=1). But when n=1, the answer is m, so the code can handle that case separately.

So the code:

Read n, m, k.

if n ==1:

    print(m % MOD)

else:

    build transition matrix.

    compute matrix^(n-1)

    sum all elements mod MOD.

So code steps.

Now, the matrix exponentiation.

Let's implement matrix multiplication.

def multiply(A, B, m, mod):

    result = [[0]*m for _ in range(m)]

    for i in range(m):

        for k in range(m):

            if A[i][k] ==0:

                continue

            for j in range(m):

                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod

    return result

But this is O(m^3). For m=52, 52*52*52 is 140k. For 50 steps, 7 million operations. Should be manageable.

But in Python, even this can be slow. Wait, but 7 million operations per test case. Python can handle that. Let's proceed.

The exponentiation function:

def matrix_pow(mat, power, m, mod):

    # Initialize result as identity matrix

    result = [[0]*m for _ in range(m)]

    for i in range(m):

        result[i][i] =1

    current = mat

    while power >0:

        if power %2 ==1:

            result = multiply(result, current, m, mod)

        current = multiply(current, current, m, mod)

        power = power //2

    return result

But for large matrices (m=52), each multiply is O(m^3) steps. So for 50 steps, each step may have up to two multiplies (if the power bit is set), but on average log2(1e15) steps. So this would be O(50 * m^3) operations.

Yes, but in Python, this may be tight for the time limit. Let's see.

Alternative optimizations for matrix multiplication:

Using nested lists and loops with precomputed ranges, perhaps using for loops in a way that is as efficient as possible.

Alternatively, represent the matrix as a list of rows, each row is a list of integers. The multiply function as above.

Another approach is to precompute the transpose of B to make the multiplication more cache-friendly, but in Python, this may not help much.

Alternatively, use numpy for matrix operations. But since the code is to be written in Python and the problem says to avoid using any external libraries, numpy is not allowed.

So proceed with the initial approach.

Now, code for the problem.

First, read the input.

Sample Input 1:

3 3 2

ab

ba

The forbidden pairs are 'ab' (a followed by b) and 'ba' (b followed by a). So the transition matrix after forbidden pairs is:

Row 0 (a) can't go to 1 (b). So row 0 has 0 in column 1.

Row 1 (b) can't go to 0 (a). So row 1 has 0 in column 0.

Other entries are 1.

Now, code steps:

Read n, m, k.

If n ==1, output m % MOD.

Else:

Initialize a matrix of size m x m with all 1s.

For each forbidden pair:

   read the two characters.

   a = first character, converted to index.

   b = second character, converted to index.

   matrix[a][b] =0

Compute mat_power = matrix^(n-1).

sum all elements of mat_power.

Output sum mod 1e9+7.

So code:

MOD = 10**9 +7

n, m, k = map(int, input().split())

if n ==0:

    print(0)

elif n ==1:

    print(m % MOD)

else:

    # build transition matrix

    matrix = [[1]*m for _ in range(m)]

    for _ in range(k):

        s = input().strip()

        a_char = s[0]

        b_char = s[1]

        # convert to indices

        if a_char.islower():

            a = ord(a_char) - ord('a')

        else:

            a = 26 + ord(a_char) - ord('A')

        if b_char.islower():

            b = ord(b_char) - ord('a')

        else:

            b = 26 + ord(b_char) - ord('A')

        # check if a and b are within 0 to m-1 (but input is guaranteed)

        if a < m and b <m:

            matrix[a][b] =0

    # Compute matrix^(n-1)

    def multiply(A, B, m, mod):

        res = [[0]*m for _ in range(m)]

        for i in range(m):

            for k in range(m):

                if A[i][k] ==0:

                    continue

                for j in range(m):

                    res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % mod

        return res

    def matrix_pow(mat, power, m, mod):

        result = [[0]*m for _ in range(m)]

        for i in range(m):

            result[i][i] =1

        while power >0:

            if power %2 ==1:

                result = multiply(result, mat, m, mod)

            mat = multiply(mat, mat, m, mod)

            power = power //2

        return result

    power = n-1

    mat_power = matrix_pow(matrix, power, m, MOD)

    total =0

    for row in mat_power:

        total = (total + sum(row)) % MOD

    print(total % MOD)

Wait, but in the code for converting a_char and b_char to indices, there's a mistake. Because the problem says that the nucleotides are numbered from 1 to m. So 'a' is 1, 'b' is 2, etc. So the code for converting a_char to the index is:

For a lowercase c:

number = ord(c) - ord('a') +1

But the code currently does:

if a_char.islower():

    a = ord(a_char) - ord('a') → which is 0-based, but corresponds to 0 for 'a', which is 1 in the problem.

Wait, this is wrong. For example, 'a' in the problem is nucleotide 1. So to convert to 0-based index, subtract 1. So the code should be:

For a lowercase character c:

number = ord(c) - ord('a') +1 → 'a' →1, then subtract 1 to get 0.

But the current code for a_char:

if a_char.islower():

    a = ord(a_char) - ord('a') → which is 0-based. But this would give 0 for 'a' (correct), 1 for 'b', etc. Which is correct. Because 'a' is 1 in the problem, which becomes 0-based index 0. So the code is correct.

Wait, no. Let's see:

In the problem, 'a' represents 1, 'b' represents 2, ..., 'z' represents 26.

So for 'a', the code's code does ord('a') - ord('a') →0. Then the index is 0. Which is correct (since 1-1=0).

Yes. So the code's current conversion is correct. Similarly, for uppercase: 'A' is 27 in the problem, which is 26 when 0-based. So code:

ord(c) - ord('A') →0 for 'A', add 26 to get 26, which is correct.

Yes. So the code's conversion is correct.

So, that's correct.

Testing the sample input 1:

n=3, m=3, k=2.

Forbidden pairs are 'ab' and 'ba'.

After conversion:

a_char is 'a' →0.

b_char is 'b' →1.

So matrix[0][1] =0.

Next forbidden pair is 'ba' → a_char 'b' is 1, b_char 'a' is 0. So matrix[1][0] =0.

So matrix is:

row 0: [1,0,1]

row 1: [0,1,1]

row 2: [1,1,1]

n-1=2. So matrix squared.

As before, the code computes matrix_power as matrix^2.

Summing all entries gives 17, which matches the sample.

Sample 3:

input:

2 1 1

aa

n=2, m=1. Forbidden pair is 'aa' →0-based indices (0,0). So matrix[0][0] =0.

matrix is [[0]].

n-1=1. matrix^1 is [[0]].

sum is 0.

Sample 3's output is 0. Correct.

Sample 2:

n=3, m=3, k=0. All transitions allowed.

matrix is all 1s.

matrix^2 (since n-1=2) is:

each entry (i,j) is sum_{k} T[i][k] * T[k][j}. T[i][k] is 1 for all i,k. So for each i,j, sum is 3. So each entry is 3. The matrix is 3x3, sum is 3*3*3=27.

Which matches the sample.

So the code should work.

Now, the code needs to be optimized for speed. The current code uses triple loops, which for m=52 is 140k per multiply. But in Python, even that may be acceptable. However, there's a possible optimization.

Alternative approach: Represent the matrices as lists of rows, and for each row in the result, precompute the sum for each cell. But perhaps using a more optimized way.

Another optimization is to precompute the transpose of B when multiplying A and B. Because matrix multiplication can be optimized by switching the order of j and k loops to improve cache performance, but in Python, this may not have a significant effect. Alternatively, using list comprehensions and avoiding loops as much as possible.

But given the time constraints, perhaps the code as written is sufficient.

Another possible optimization is to use bitmask representations for the matrix. But with m up to 52, that's not feasible.

Alternatively, note that the matrix is a square matrix, and when raising it to the power, the code can represent the matrix in a way that's more efficient. However, given the time, proceed with the code as written.

Another possible optimization is to precompute all the matrix multiplications modulo 1e9+7 at each step.

Yes, the current code does that.

So, the code should pass all test cases.

Now, code:

Make sure that when converting the characters, the code correctly handles lowercase and uppercase.

The code reads the forbidden pairs and sets matrix[a][b] =0.

Test case 3: m=1, forbidden pair is 'aa' → a and b are 0 and 0. So matrix[0][0] becomes 0. For n=2, matrix is [[0]]. The sum is 0.

Yes.

So the code should be correct.
</think>

To solve this problem, we need to determine the number of valid n-length DNA chains on Mars, where certain consecutive nucleotide pairs are forbidden. Given the constraints, an efficient solution using matrix exponentiation is required to handle very large values of n (up to \(10^{15}\)).

### Approach
1. **Problem Analysis**:
   - Each valid DNA chain of length n can be represented as a sequence of transitions between nucleotides, where each transition is allowed unless specified as forbidden.
   - The problem can be modeled using a transition matrix where each entry indicates whether a transition from one nucleotide to another is allowed.

2. **Matrix Representation**:
   - Construct a transition matrix `T` of size m x m, where `T[i][j]` is 1 if transitioning from nucleotide i to j is allowed, and 0 otherwise.

3. **Matrix Exponentiation**:
   - To compute the number of valid sequences of length n efficiently, we use matrix exponentiation. The matrix `T` raised to the power (n-1) gives the number of valid transitions for sequences of length n.

4. **Summing the Result**:
   - The sum of all elements in the matrix `T^(n-1)` gives the total number of valid sequences of length n, as each entry in the matrix represents the number of valid paths from one nucleotide to another after (n-1) transitions.

### Solution Code
```python
MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1
    
    if n == 1:
        print(m % MOD)
        return
    
    # Initialize transition matrix with all 1s
    matrix = [[1] * m for _ in range(m)]
    
    # Process forbidden pairs
    for _ in range(k):
        s = input[ptr]
        ptr += 1
        a_char, b_char = s[0], s[1]
        
        # Convert characters to 0-based indices
        if a_char.islower():
            a = ord(a_char) - ord('a')
        else:
            a = 26 + (ord(a_char) - ord('A'))
        
        if b_char.islower():
            b = ord(b_char) - ord('a')
        else:
            b = 26 + (ord(b_char) - ord('A'))
        
        if a < m and b < m:
            matrix[a][b] = 0
    
    # Matrix exponentiation functions
    def multiply(A, B, m, mod):
        result = [[0] * m for _ in range(m)]
        for i in range(m):
            for k in range(m):
                if A[i][k] == 0:
                    continue
                for j in range(m):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
        return result
    
    def matrix_power(mat, power, m, mod):
        result = [[0] * m for _ in range(m)]
        for i in range(m):
            result[i][i] = 1
        current = mat
        while power > 0:
            if power % 2 == 1:
                result = multiply(result, current, m, mod)
            current = multiply(current, current, m, mod)
            power //= 2
        return result
    
    # Compute matrix^(n-1)
    power = n - 1
    mat_pow = matrix_power(matrix, power, m, MOD)
    
    # Sum all elements in the matrix
    total = 0
    for row in mat_pow:
        total = (total + sum(row)) % MOD
    print(total % MOD)

if __name__ == "__main__":
    main()
```

### Explanation
1. **Reading Input**: The input is read and parsed to extract the values of n, m, and k, followed by the forbidden pairs.
2. **Transition Matrix**: A matrix of size m x m is initialized with all elements set to 1. Forbidden transitions are then set to 0 based on the input.
3. **Matrix Multiplication and Exponentiation**: The matrix is exponentiated to the power (n-1) using a helper function, which efficiently computes the power using exponentiation by squaring.
4. **Result Calculation**: The sum of all elements in the resulting matrix gives the total number of valid sequences, which is then printed modulo \(10^9 + 7\).

This approach ensures that we handle very large values of n efficiently using matrix exponentiation, making the solution both optimal and scalable.