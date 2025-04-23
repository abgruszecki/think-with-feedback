<think>
Okay, let's try to solve this problem. The problem is about counting the number of ways to pack presents into boxes under certain conditions. Let's read the problem statement carefully.

So, the problem says that there are n kinds of presents, each with infinite supply. We have m distinct boxes. The rules are:
1. Each box can contain at most one present of each kind. So for each kind, you can choose to put it in any subset of boxes, but each box can have at most one of that kind. Wait, no, more precisely, each box can't have more than one of the same kind. But the rule is that a box can't have more than one of the same kind. So for a particular kind, each box can either have 0 or 1 present of that kind. But since the presents are of the same kind, putting one in a box is a yes/no choice for each box. However, the second condition is that each kind must be packed into at least one box.

So for each kind of present, we need to select a non-empty subset of boxes where that present is placed. But since each box can only contain 0 or 1 of that kind, the total options for each kind is the number of non-empty subsets of the m boxes. Wait, no. Because for a particular kind, the subset of boxes that include it can be any non-empty subset. Because the presents are of the same kind, the choice is which boxes include that present. Since each box can have at most one of that kind, the selection for that kind is a subset of boxes (non-empty) where it's included. Because if you put the present in multiple boxes, each box gets exactly one, but since they are the same kind, the arrangement is determined by the subset chosen.

So for each kind, the number of choices is the number of non-empty subsets of the m boxes. Because for a kind, you have to choose a subset (non-empty) of boxes to include that present. Each subset represents that the present is placed in exactly those boxes. Since the present is of the same kind, putting it in a box once is the only option, and you can't put more than one in a box.

So the total number of ways is (number of possible subsets for each kind) raised to the power of n, since each kind is independent. But wait, the problem requires that each kind is used in at least one box. So for each kind, the subset must be non-empty. So the number of choices per kind is (2^m - 1), because each subset is possible except the empty subset. But wait, no. Wait, for each kind, how many subsets are allowed? For each kind, you select a subset of boxes where exactly that present is placed. But since each present is of a kind, and different boxes are distinct, the selection for each kind is a subset of boxes (non-empty) where the present is placed. For example, in the first sample input, n=1, m=3. The possible subsets for the single present are all non-empty subsets of 3 boxes. The subsets can be any of the 7 possible (since 2^3-1=7), which matches the sample output.

Wait, but in the first sample, the answer is 7, which is exactly 2^3 -1. But when n=1, the total is (2^3 -1)^1 =7. So that's correct.

The second sample input is n=2, m=2. So each of the two presents can choose any non-empty subset of the two boxes, but the total is (2^2-1)^2 =3^2=9, which matches the sample output. So the problem reduces to computing ( (2^m -1)^n ) mod 1e9+7.

Wait, that seems to be the case. So the answer is ( (2^m -1) )^n mod MOD, where MOD is 1e9+7.

But wait, let's think again. For each kind, the number of possible choices is the number of non-empty subsets of boxes. Each subset for the kind indicates which boxes contain that present. Since each box can have any number of different kinds, as long as each kind is in at least one box. So yes, each kind is independent, and the choices multiply. So for n kinds, it's ( (2^m -1) )^n.

So the problem reduces to calculating ( (2^m -1)^n ) mod 1e9+7.

But since n and m can be up to 1e9, we need to compute exponents efficiently. We can compute 2^m mod MOD, subtract 1, then compute the result raised to the power of n, all modulo MOD.

But wait, when m is up to 1e9, calculating 2^m mod MOD can be done using fast exponentiation. Similarly, raising (2^m-1) to the power n can be done with fast exponentiation.

So the steps are:

1. Compute a = pow(2, m, MOD). But since 2^m could be up to 2^1e9, which is way larger than MOD. So we compute 2^m mod MOD.

2. Subtract 1 from a, mod MOD. So (a -1) mod MOD. But wait, if a is 0 (which happens when MOD divides 2^m, but since MOD is 1e9+7 which is a prime, and 2 is not a multiple of MOD, so 2^m mod MOD can't be zero. So a can't be zero. So (a-1) mod MOD is safe.

3. Then compute b = pow( (a-1) mod MOD, n, MOD )

So the result is b.

Wait, let's test the samples.

First sample: n=1, m=3.

Compute a = 2^3 mod 1e9+7 =8. a-1=7. 7^1=7. Correct.

Second sample: n=2, m=2.

a=4 mod 1e9+7. a-1=3. 3^2=9. Correct.

So yes, this approach works.

Now, the problem is to compute this. But the constraints are that n and m can be up to 1e9, which is manageable with fast exponentiation. So in Python, we can use the built-in pow function with three arguments, which is optimized for this.

So the code would be:

Read n and m.

Compute pow(2, m, MOD) → a.

Compute (a -1) mod MOD → base.

Compute pow(base, n, MOD) → result.

Print result.

But wait, when m is 0, but according to the problem constraints, m is at least 1. Because in the input constraints, m is >=1? Let's check the problem statement.

The input constraints say 1<=n, m <=1e9. So m is at least 1. So when m is 1, 2^1 is 2. 2-1=1. So (1)^n is 1.

But for example, if n=5, m=1: each present must be put into the single box. There's exactly 1 way per present, so 1^5=1. Which is correct.

So the code is straightforward. Now, code in Python.

But wait, what about when m is 0? The problem says m >=1, so we don't have to handle that.

So the code:

MOD = 10**9 +7

n, m = map(int, input().split())

a = pow(2, m, MOD)

base = (a -1) % MOD

ans = pow(base, n, MOD)

print(ans)

That's it. The code handles all cases. Let's test the first sample:

Input 1 3:

a = 8, base=7. ans=7^1 mod 1e9+7=7. Correct.

Second sample: 2 2.

a=4, base=3. 3^2=9. Correct.

Another test case: n=5, m=1. The answer is 1.

Yes.

Another test case: n=3, m=2.

Each present can be in either box 1, box 2, or both. So (2^2-1) =3 per present. 3^3=27.

So code returns 27.

Yes.

So the code is correct.
</think>

```python
MOD = 10**9 + 7
n, m = map(int, input().split())
base = (pow(2, m, MOD) - 1) % MOD
print(pow(base, n, MOD))
```