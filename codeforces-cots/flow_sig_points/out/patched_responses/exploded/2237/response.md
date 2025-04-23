<think>
Okay, let's tackle this problem. So, the task is to count the number of ways to fill an n x n grid with integers from 1 to k such that every row has a minimum of 1 and every column also has a minimum of 1. And since the numbers can be up to 1e9, we need an efficient way to compute this without iterating through all possibilities directly.

Hmm, the constraints here are that each row and column must have at least one 1. So, the problem is similar to inclusion-exclusion problems where we have to avoid certain forbidden configurations. Let me think.

Let's model this with inclusion-exclusion. The total number of grids that satisfy the row conditions and the column conditions. Wait, no. The problem requires that both rows and columns have their minima as 1. So, the grid must have at least one 1 in each row and each column. So, the problem is to count the grids where all rows have a 1, and all columns have a 1. But how do these conditions interact?

Alternatively, perhaps it's easier to model this by considering the complement: subtract the cases where at least one row doesn't have a 1, or at least one column doesn't have a 1, but since both row and column conditions must be satisfied, maybe inclusion-exclusion is needed here.

Wait, the problem requires that all rows have at least one 1 and all columns have at least one 1. So the valid grids are those that are in the intersection of two sets: grids with all rows containing a 1, and grids with all columns containing a 1. So, the inclusion-exclusion approach would be needed here. But how to model this.

Alternatively, maybe we can compute the total number of grids that satisfy the row conditions, then subtract those that don't satisfy the column conditions. But I'm not sure. Let's think differently.

The total number of grids where all rows have a 1 is A. The total number of grids where all columns have a 1 is B. But we need the intersection of these two sets. So, using inclusion-exclusion, the total is A + B - (A ∪ B), but that's not helpful. Wait, no. The inclusion-exclusion formula for the intersection is not straightforward. Maybe another approach.

Alternatively, the problem can be approached by considering the inclusion-exclusion over rows and columns. Let's see. The problem is similar to ensuring that all rows and columns have at least one 1. So, the forbidden cases are when some row has no 1, or some column has no 1. But since the conditions are that all rows and all columns must have at least one 1, the inclusion-exclusion will consider all possible subsets of rows and columns that are excluded, and compute the inclusion-exclusion sum accordingly.

But combining rows and columns into inclusion-exclusion might get complicated. Let's think of it as the set of grids where every row has at least one 1 and every column has at least one 1. Let’s denote this as S. The total number of such grids is S.

The total number of possible grids without any restrictions (other than 1<=x<=k) is k^(n²). But we need to subtract those grids that miss at least one row's 1 or miss at least one column's 1.

So, S is equal to the inclusion-exclusion over all possible subsets of rows and columns that are forbidden. Hmm, perhaps the inclusion-exclusion formula will have terms for both rows and columns. Let's formalize this.

The inclusion-exclusion formula for S would be:

S = sum_{a=0 to n} sum_{b=0 to n} (-1)^(a+b) * C(n,a) * C(n,b) * f(a,b)

where a is the number of rows excluded (forbidden to not have a 1), and b is the number of columns excluded (forbidden to not have a 1). Wait, but how does this work? Let me think again.

Alternatively, the forbidden cases are grids that either (a) have at least one row without a 1, or (b) have at least one column without a 1. To compute S, we can use inclusion-exclusion to subtract the cases where any rows are missing 1's, add back the overlaps, etc., and similarly for the columns. But combining rows and columns in inclusion-exclusion is a bit tricky.

Wait, maybe it's better to model the forbidden events as follows: For each row i, let R_i be the set of grids where row i has no 1's. For each column j, let C_j be the set of grids where column j has no 1's. Then, the problem is to compute the total number of grids not in any R_i or C_j. So, S = total grids - (sum R_i + sum C_j) + (sum R_i ∩ R_j + sum R_i ∩ C_j) - ... and so on, following inclusion-exclusion.

But considering all possible subsets of R_i and C_j could be complicated. However, maybe we can model it as inclusion-exclusion over the rows and columns.

Alternatively, since the required condition is that all rows have at least one 1 and all columns have at least one 1, perhaps the inclusion-exclusion can be expressed as:

S = sum_{S subset of rows} sum_{T subset of columns} (-1)^(|S| + |T|) * f(S, T)

where f(S, T) is the number of grids where all rows in S have no 1's and all columns in T have no 1's. Because we are considering all grids that have no 1's in S rows and T columns, and using inclusion-exclusion to subtract and add accordingly.

But how do we compute f(S, T)? For a given set S of rows and T of columns, the grids that have no 1's in any of the S rows and no 1's in any of the T columns. So, each cell in S rows must have a value >= 2 (since they can't be 1). Similarly, each cell in T columns must have a value >=2. But wait, if a cell is in both a forbidden row and a forbidden column, then it's in S ∩ T, but the condition is that the cell must be >=2. So, the cells that are in S rows OR T columns must be >=2. Wait no, the condition is that cells in S rows (regardless of columns) and cells in T columns (regardless of rows) must be >=2. So, any cell that is in a forbidden row OR in a forbidden column must be >=2? Or is it in a forbidden row AND forbidden column?

Wait, the forbidden rows are S, so in those rows, all cells must not be 1. Similarly, forbidden columns T: in those columns, all cells must not be 1. But a cell that is in a forbidden row (so in S) must be >=2. Similarly, a cell in a forbidden column (T) must be >=2. So, if a cell is in both a forbidden row and a forbidden column, it's still required to be >=2.

So, the cells that must be >=2 are those in S rows or T columns. Because:

- For any row in S, all cells in that row cannot be 1 (so >=2).

- For any column in T, all cells in that column cannot be 1 (so >=2).

Therefore, the cells that are in S rows OR T columns must be >=2. The remaining cells (not in S rows and not in T columns) can be any value between 1 and k.

So, the number of such grids is:

f(S, T) = ( (k-1)^( |S| * n + |T| * n - |S| * |T| )) * (k) ^ ( (n - |S|) * (n - |T|) ) )

Wait, let's see:

The total number of cells is n².

The cells in S rows: each of these |S| rows has n cells, but some of them may also be in T columns. So, the cells in S rows OR T columns are:

Each cell that is in S rows (total |S| * n) plus the cells in T columns that are not in S rows (which is |T| * (n - |S|)).

So total cells that must be >=2 is |S| * n + |T| * (n - |S|) = |S|n + |T|n - |S||T| = n(|S| + |T|) - |S||T|.

Alternatively, |S| rows contribute |S| * n cells, |T| columns contribute |T| * (n - |S|) cells, because the rows in S are already accounted for, so the columns in T contribute their cells not in S rows.

So the total cells that must be >=2 is |S|*n + (n - |S|)*|T|.

Alternatively, the formula is (number of cells in S rows) + (number of cells in T columns not in S rows) = |S|*n + (n - |S|)* |T|.

Each of these cells can be filled in (k-1) ways (since they can't be 1). The remaining cells (which are not in S rows and not in T columns) can be filled with any of the k options.

So, the formula for f(S, T) would be (k-1)^( |S|*n + |T|*(n - |S|) ) ) * k^( (n - |S|)*(n - |T|) )

Alternatively, let's compute the number of cells that are in S rows OR T columns. That's the union of S rows and T columns. The size of the union is |S|*n + |T|*n - |S|*|T|. Because each S row has n cells, each T column has n cells, but the intersection (cells in S rows and T columns) is |S|*|T|, so subtract that once.

Therefore, the number of cells that must be >=2 is |S|*n + |T|*n - |S|*|T|.

Each of these cells has (k-1) choices. The remaining cells (those not in S rows and not in T columns) have k choices each.

So, the total for f(S, T) is (k-1)^( (|S| + |T|) * n - |S||T| ) ) * k^( (n - |S|) * (n - |T|) )

So, the inclusion-exclusion formula for S (the desired answer) is:

S = sum_{S subset of rows} sum_{T subset of columns} (-1)^(|S| + |T|) * C(n, |S|) * C(n, |T|) * (k-1)^( (|S| + |T|) * n - |S||T| ) * k^((n - |S|) (n - |T|)) )

But summing over all subsets S and T is computationally expensive. For n up to 250, even O(n^3) is feasible, but n can be 250, so S and T can be up to 250 each. So if we iterate over all possible a = |S| (from 0 to n) and b = |T| (from 0 to n), then for each a and b, compute the term as follows:

For each a, there are C(n, a) ways to choose S.

For each b, there are C(n, b) ways to choose T.

So the term for a and b is:

term = (-1)^(a + b) * C(n, a) * C(n, b) * (k-1)^( (a + b)*n - a*b ) * k^( (n - a) * (n - b) )

Then sum over all a and b.

Yes! Because for a given a and b, the number of S subsets of size a is C(n,a), same for T. Then for each such pair (S, T), the value of the term is as above. So the inclusion-exclusion sum can be rewritten as a double sum over a and b, each from 0 to n, with the term as above.

So the problem reduces to computing this double sum efficiently.

Now, the question is how to compute this sum modulo 1e9+7, given that n can be up to 250 and k up to 1e9.

The main challenges here are:

1. Precomputing binomial coefficients C(n, a) for a up to 250.

2. Efficiently computing exponents (k-1)^( (a + b)*n - a*b ) and k^( (n - a) * (n - b) ), modulo 1e9+7, for exponents that can be as large as (250 + 250)*250 - 250^2 = 250*(500) - 62500 = 125000 - 62500 = 62500. But (n -a) * (n -b) can be up to (250)^2 = 62500. So the exponents are up to 62500 + 62500 = 125000. So each term's exponents are up to 125,000. 

But k can be up to 1e9, so computing (k-1)^e mod MOD and k^e mod MOD for e up to 125,000. How to compute this efficiently?

We can precompute for each possible a and b, compute (k-1)^exp1 mod MOD and k^exp2 mod MOD, where exp1 = (a + b)*n - a*b, exp2 = (n -a) * (n -b). However, since k can be up to 1e9, and exponents up to 1e5, we can compute these exponents using fast exponentiation (binary exponentiation) for each term. But for n=250, the total terms are 251*251 = 63,000 terms. For each term, two exponentiations of exponents up to 1e5. Each exponentiation is O(log e), which is acceptable, since log2(1e5) is around 17. So 63k terms * 34 operations (two exponentiations) is about 2 million operations, which is manageable.

So the plan is:

- Precompute binomial coefficients C(n, a) for a from 0 to n.

- Iterate a from 0 to n:

   - For each a, compute C(n, a) once.

   - Iterate b from 0 to n:

      - Compute C(n, b).

      - Compute exponent1 = (a + b)*n - a*b.

      - Compute (k-1)^exponent1 mod MOD.

      - Compute exponent2 = (n -a) * (n -b).

      - Compute k^exponent2 mod MOD.

      - Multiply all these factors, along with (-1)^(a+b), and the binomial coefficients.

      - Sum all terms into the result.

But wait, the exponents can be very large. For example, (a + b)*n could be up to (250 + 250)*250 = 500*250=125,000. Then subtract a*b which can be up to 250*250=62500, so exponent1 could be 125,000 - 62500 = 62500. Similarly, exponent2 can be up to 250^2=62500.

So each term requires two exponentiations with exponents up to 62500. For each a and b, we can compute pow(k-1, exponent1, MOD) and pow(k, exponent2, MOD). Since Python's built-in pow can handle this efficiently with three arguments (base, exponent, mod), which uses binary exponentiation under the hood.

So the steps would be:

1. Precompute the binomial coefficients C(n, a) for a in 0..n. Since n is up to 250, this can be done with dynamic programming or using a combinatorial formula.

The binomial coefficient can be computed using the formula:

C(n, 0) = 1, C(n, a) = C(n, a-1) * (n - a + 1) / a. But since we need to compute this modulo 1e9+7, and 1e9+7 is a prime (I think?), then division can be handled via modular inverses.

But n is up to 250, so even precomputing using a 2D array is feasible. For each a in 0..n, compute C(n, a) mod MOD.

Once the binomial coefficients are precomputed, the rest is manageable.

Now, let's outline the code.

First, read n and k.

If k is 0, but the problem states k is >=1. So no. Wait, the constraints say 1 <=n <=250, 1 <=k <=1e9. So k is at least 1.

But when k=1, then the only possible grid is all 1s. So each row and column must have at least one 1. So that's valid. But the answer is 1 if n >=1. So for k=1, the answer is 1 only if the grid has at least one 1 in every row and column, which requires that every cell is 1. So if k=1, the answer is 1 if n is 1 (since the single cell is 1), but if n>1, then all rows and columns must have 1. But when k=1, all cells are 1. So the answer is 1 for any n. But let's see: in this case, the code would compute sum terms for a and b. But when k=1, (k-1) is 0, so in the term (k-1)^exponent1, unless exponent1 is zero, which occurs when a=0 and b=0. So perhaps the code handles that case automatically. But perhaps it's better to handle k=1 as a special case. But maybe the code as written will compute correctly.

But let's proceed.

Compute MOD = 1e9+7.

So code steps:

- Read n and k.

- Compute MOD = 10**9+7.

- Precompute C(n, a) for a from 0 to n.

Similarly, precompute C(n, b) for b from 0 to n. But since a and b are both up to n, the same precomputed array can be used.

How to compute C(n, a) mod MOD:

Use a 1D array where comb[a] represents C(n, a). Initialize comb[0] = 1. Then for each a from 1 to n, comb[a] = comb[a-1] * (n - a + 1) // a. But division modulo MOD is multiplication by the modular inverse.

Wait, but in Python, integers are involved. So the correct way is to compute the binomial coefficients mod MOD using the multiplicative inverses.

The iterative approach is:

comb = [0]*(n+1)

comb[0] = 1

for a in range(1, n+1):

    comb[a] = comb[a-1] * (n - a + 1) // a

But modulo MOD, division by a is equivalent to multiplying by the modular inverse of a mod MOD.

So to compute comb[a] mod MOD:

comb = [0]*(n+1)

comb[0] = 1

for a in range(1, n+1):

    numerator = comb[a-1] * (n - a + 1) % MOD

    denominator = a

    inverse_denominator = pow(denominator, MOD-2, MOD)

    comb[a] = numerator * inverse_denominator % MOD

Yes. So that's how to compute the binomial coefficients.

Once comb is computed, then for each a in 0..n, comb[a] is C(n,a) mod MOD.

Then, for each a and b in 0..n:

term = (-1)^(a + b) * comb[a] * comb[b] * ( (k-1) ** exponent1 ) * (k ** exponent2 ) mod MOD

But exponents can be up to 62500. So compute (k-1) mod MOD, then compute pow((k-1) % MOD, exponent1, MOD), and similarly for k.

But k can be up to 1e9, so we need to mod it first.

So:

base_k_minus_1 = (k-1) % MOD

base_k = k % MOD

Then, for each a and b:

exponent1 = (a + b) * n - a * b

exponent2 = (n - a) * (n - b)

pow1 = pow(base_k_minus_1, exponent1, MOD)

pow2 = pow(base_k, exponent2, MOD)

term = ((-1) ** (a + b)) * comb[a] * comb[b] % MOD

term = term * pow1 % MOD

term = term * pow2 % MOD

Then add this term to the answer, considering the sign.

But how to handle the (-1)^(a + b)?

Well, if a + b is even, it's +1; if odd, it's -1. So in mod MOD, -1 is MOD-1.

So, sign = 1 if (a + b) is even else -1. But in mod, (-1) ** (a + b) is equivalent to 1 if even, MOD-1 if odd.

So, in code:

sign = 1 if (a + b) % 2 == 0 else -1

But in Python, (-1) ** (a + b) can be computed as 1 if (a + b) even, else -1.

But when modding, to avoid negative numbers, we can compute it as (MOD-1) if (a + b) is odd, else 1.

So:

sign = (-1) ** (a + b) 

But in code, sign can be 1 or -1. Then, when multiplied by comb[a] and comb[b], which are modded, and then the entire term is modded, we can handle the sign as follows:

sign = 1 if (a + b) % 2 == 0 else -1

term = sign * comb[a] * comb[b] 

term %= MOD

But in Python, (-1) % MOD is MOD-1, so when a + b is odd, sign is -1, which is equivalent to MOD-1 mod MOD.

So, in code:

sign = 1 if (a + b) % 2 == 0 else MOD - 1

term = comb[a] * comb[b] % MOD

term = term * sign % MOD

term = term * pow1 % MOD

term = term * pow2 % MOD

So, putting it all together:

Compute the answer as follows:

ans = 0

for a in 0...n:

    for b in 0...n:

        sign = 1 if (a + b) even else MOD-1

        c = comb[a] * comb[b] % MOD

        c = c * sign % MOD

        exponent1 = (a + b)*n - a*b

        pow1 = pow(base_k_minus_1, exponent1, MOD)

        exponent2 = (n - a)*(n - b)

        pow2 = pow(base_k, exponent2, MOD)

        term = c * pow1 % MOD

        term = term * pow2 % MOD

        ans = (ans + term) % MOD

So, this is manageable.

Now, what about the cases when k=1?

In that case, base_k_minus_1 is 0, so exponent1 is (a + b)*n - a*b.

If a or b are positive, then exponent1 could be positive. So pow(0, exponent1, MOD) is 0.

But for the term to be non-zero, exponent1 must be zero. Because if base_k_minus_1 is 0 (k=1), then (k-1) is 0. So any term where exponent1 >0 will have pow1 =0, so the entire term becomes zero. So only the terms where exponent1=0 will contribute.

exponent1 is (a + b)*n - a*b =0.

But when k=1, the code will compute the sum only for a and b where (a + b)*n -a*b =0. Let's see:

But for k=1, the answer is 1 if all rows and columns have 1s. But when k=1, all cells are 1, so all rows and columns have 1. So the answer is 1. But let's see what the code computes.

For k=1:

base_k_minus_1 =0

base_k =1.

Then, exponent1 is (a + b)*n -a*b.

For a term to contribute, exponent1 must be zero, and exponent2 can be anything, but pow1 would be 0^0=1 (since exponent1=0) and pow2=1^exponent2=1.

So the term is:

sign * comb[a] * comb[b] * 1 * 1.

But when exponent1 is zero, (a + b)*n -a*b=0.

Let's see for a=0, b=0:

exponent1 =0.

So that term contributes sign=1, comb[0]^2=1. So term=1*1*1*1=1.

Other terms where (a + b)*n = a*b.

But for example, a=1, b=1:

exponent1 = (1+1)*n -1*1 = 2n -1.

For this to be zero: 2n -1=0 → n=0.5, but n>=1. So no such terms. So only the a=0, b=0 term contributes 1. All other terms have exponent1>0, so pow1=0.

Thus, when k=1, the code returns 1, which is correct.

So the code handles all cases correctly.

Another test case: the first sample input is n=2, k=2.

The code should compute the sum over a and b from 0 to 2.

We can compute each term:

For a=0, b=0:

exponent1=0*2 + 0*2 - 0*0=0. So pow1=1^0=1.

exponent2=(2-0)*(2-0) =4. pow2=2^4=16 mod MOD.

sign is 0 → even → 1.

term = C(2,0)*C(2,0) *1 * 16 → 1*1 *16=16.

But then multiplied by 1 (sign) →16.

a=0, b=1:

exponent1=(0+1)*2 -0*1=2. pow1=1^2=1.

exponent2=(2-0)*(2-1) =2*1=2. pow2=2^2=4.

sign is 0+1=1 → odd → MOD-1.

term = C(2,0)*C(2,1) * (MOD-1) *1 *4 →1*2 * (MOD-1) *4 → 8 * (MOD-1) → mod MOD → -8.

So the term is -8.

Similarly, for all a and b, sum all terms.

But let's compute the sample:

Sample input 2 2:

The code should compute the sum of terms for a in 0-2 and b in 0-2.

The correct answer is 7.

But according to the inclusion-exclusion sum, let's see:

Each term is as follows.

But perhaps it's easier to note that for n=2, the code's calculation is:

sum a from 0 to 2:

sum b from 0 to 2:

term = (-1)^(a + b) * C(2,a)*C(2,b) * 1^( (a + b)*2 - a*b ) * 2^((2-a)*(2-b)) )

Wait, k=2. So base_k_minus_1 =1, base_k=2.

So pow1 is 1^exponent1, which is 1.

So term is (-1)^(a + b) * C(2,a) * C(2,b) * 1 * 2^((2-a)(2-b)).

So the term simplifies to (-1)^(a+b) * C(2,a) * C(2,b) * 2^{(2-a)(2-b)}.

The sum of these terms is the answer.

Let's compute all terms:

Possible a and b:

a=0, b=0:

sign=1. C(2,0)^2=1. 2^{2*2}=16. term=1*16=16.

a=0, b=1:

sign=-1. C(2,0)*C(2,1)=1*2=2. 2^{(2-0)(2-1)} =2^(2*1)=2. term= -2*2= -4.

a=0, b=2:

sign=1. C(2,0)*C(2,2) =1*1=1. 2^{(2-0)(2-2)}=2^(2*0)=1. term=1*1*1=1.

a=1, b=0:

sign=-1. C(2,1)*C(2,0) =2*1=2. 2^{(2-1)(2-0)}=2^(1*2)=4. term= -2*4 =-8.

a=1, b=1:

sign=1. C(2,1)*C(2,1)=2*2=4. 2^{(2-1)(2-1)}=2^(1*1)=2. term=4*2=8.

a=1, b=2:

sign=-1. C(2,1)*C(2,2)=2*1=2. 2^{(2-1)(2-2)}=2^0=1. term= -2*1 =-2.

a=2, b=0:

sign=1. C(2,2)*C(2,0)=1*1=1. 2^{(2-2)(2-0)}=2^(0*2)=1. term=1*1=1.

a=2, b=1:

sign=-1. C(2,2)*C(2,1)=1*2=2. 2^{(2-2)(2-1)}=2^(0*1)=1. term= -2*1 =-2.

a=2, b=2:

sign=1. C(2,2)*C(2,2)=1*1=1. 2^{(2-2)(2-2)}=2^0=1. term=1*1=1.

Now, sum all these terms:

16 -4 +1 -8 +8 -2 +1 -2 +1 

Let's compute step by step:

16 → 16

-4 →12

+1 →13

-8 →5

+8 →13

-2 →11

+1 →12

-2 →10

+1 →11.

Wait but the sample output is 7. What's wrong here?

Ah, but I must have made a mistake in calculation. Let's re-calculate each term.

Wait the exponents for the terms are (2-a)(2-b).

Let me re-calculate each term properly.

Wait when a=0 and b=0:

(2-a)(2-b) =2*2=4. 2^4=16. So term is 1*1*1 *16 =16.

a=0, b=1:

(2-0)(2-1)=2*1=2. 2^2=4. term is (-1)^(1) * 1*2 *4 → (-1)*2*4= -8.

a=0, b=2:

(2-0)(2-2)=2*0=0. 2^0=1. term is (+1) *1*1 *1=1.

a=1, b=0:

(2-1)(2-0)=1*2=2 → 2^2=4. term is (-1) *2*1 *4 → -8.

a=1, b=1:

(2-1)(2-1)=1*1=1 → 2^1=2. term is (+1)*2*2*2 → 8.

a=1, b=2:

(2-1)(2-2)=1*0=0 → 2^0=1. term is (-1)*2*1 *1 → -2.

a=2, b=0:

(2-2)(2-0)=0*2=0 → 2^0=1. term is (+1)*1*1*1=1.

a=2, b=1:

(2-2)(2-1)=0*1=0 →2^0=1. term is (-1)*1*2*1 →-2.

a=2, b=2:

(2-2)(2-2)=0*0=0 →2^0=1. term is (+1)*1*1*1=1.

Now sum all terms:

16 (a0b0)

-8 (a0b1) →8

+1 (a0b2) →9

-8 (a1b0) →1

+8 (a1b1) →9

-2 (a1b2) →7

+1 (a2b0) →8

-2 (a2b1) →6

+1 (a2b2) →7.

Yes! So the sum is 7, which matches the sample. So the code works.

So the code will correctly compute the sample answer.

Now, the code steps:

Implement the precomputation of the binomial coefficients, then loop through a and b, compute each term, and sum.

Now, code in Python:

Read n and k.

Compute the binomial coefficients modulo MOD.

Precompute comb for a from 0 to n.

Then, for each a and b, compute the term as described.

Handle MOD correctly.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, k = map(int, input_stream.readline().rstrip("\n").split())

    # Precompute binomial coefficients C(n, a) mod MOD for a in 0..n
    comb = [0]*(n+1)
    comb[0] = 1
    for a in range(1, n+1):
        numerator = comb[a-1] * (n - a + 1) % MOD
        denominator = a
        inv_denominator = pow(denominator, MOD-2, MOD)
        comb[a] = numerator * inv_denominator % MOD

    base_k_minus_1 = (k-1) % MOD
    base_k = k % MOD

    ans = 0
    for a in range(n+1):
        for b in range(n+1):
            sign = 1 if (a + b) %2 ==0 else MOD-1
            c = comb[a] * comb[b] % MOD
            c = c * sign % MOD
            
            exponent1 = (a + b)*n - a*b
            pow1 = pow(base_k_minus_1, exponent1, MOD)
            
            exponent2 = (n -a) * (n -b)
            pow2 = pow(base_k, exponent2, MOD)
            
            term = c * pow1 % MOD
            term = term * pow2 % MOD
            
            ans = (ans + term) % MOD

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
123 456789
""",
            "output": \
"""\
689974806
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

Another test case: n=1, k=1. The answer is 1.

n=1, k=2.

The code should compute the sum over a=0 and 1, and b=0 and 1.

But let's see:

For a=0, b=0:

exponent1 =0 → pow1=1^(0) =1.

exponent2=1*1=1 → pow2=2^1=2.

term = 1*1 *1 *2 =2.

a=0, b=1: exponent1 = (0+1)*1 -0*1=1. pow1=1^1=1. exponent2= (1-0)*(1-1)=1*0=0 → pow2=2^0=1. sign is 1 → (a+b=1 is odd → MOD-1. term is comb[0] (1) * comb[1] (1) →1*1 → multiply by MOD-1 → MOD-1. Multiply by 1 and 1 → term is MOD-1.

a=1, b=0: similar to a=0, b=1. term is MOD-1.

a=1, b=1: exponent1 = (2*1) -1*1=1. pow1=1^1=1. exponent2=(0*0) →0. pow2=2^0=1. sign is even (a+b=2) →1. term is comb[1] (1) * comb[1] (1) →1*1=1. multiply by 1, 1, 1 →1. So term is 1.

So sum is 2 - (MOD-1) - (MOD-1) +1 → but since all operations are mod MOD:

2 + (MOD-1) * (-2) +1 mod MOD → 3 - 2*(MOD-1) mod MOD. Wait, this is getting complicated. Alternatively, let's compute each term:

a=0, b=0 → term=2.

a=0, b=1 → term=-1 (since MOD-1 is -1 mod MOD).

a=1, b=0 → term=-1.

a=1, b=1 → term=1.

Sum: 2-1-1+1 =1.

So the answer is 1. But what's the actual number of valid grids for n=1, k=2. The grid must have a 1 (since row 1 must have min 1 and column 1 must have min 1. So the only valid grid is [1]. So answer is 1. Which matches.

Thus, code works.

Now, for the second sample input, which is n=123, k=456789. The code will compute the sum for a and b up to 123. This is 124*124=15376 iterations. For each iteration, two pow operations. Since Python's pow is efficient, this should work within the time constraints.

Thus, the code should be correct.
</think>

```python
MOD = 10**9 + 7

n, k = map(int, input().split())

# Precompute binomial coefficients C(n, a) mod MOD
comb = [0] * (n + 1)
comb[0] = 1
for a in range(1, n + 1):
    numerator = comb[a-1] * (n - a + 1) % MOD
    denominator_inv = pow(a, MOD-2, MOD)
    comb[a] = numerator * denominator_inv % MOD

base_k_minus_1 = (k - 1) % MOD
base_k = k % MOD

ans = 0
for a in range(n + 1):
    for b in range(n + 1):
        sign = 1 if (a + b) % 2 == 0 else MOD - 1
        c = comb[a] * comb[b] % MOD
        c = c * sign % MOD
        
        exponent1 = (a + b) * n - a * b
        pow1 = pow(base_k_minus_1, exponent1, MOD)
        
        exponent2 = (n - a) * (n - b)
        pow2 = pow(base_k, exponent2, MOD)
        
        term = c * pow1 % MOD
        term = term * pow2 % MOD
        
        ans = (ans + term) % MOD

print(ans)
```
