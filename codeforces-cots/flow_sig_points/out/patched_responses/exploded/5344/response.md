<think>
Okay, let's try to figure out this problem. So, the task is to find the minimum number of shovels Polycarp needs to buy so that he can pay exactly using some combination of 10-burle coins and his single r-burle coin. And he can't have any change left over. 

Hmm. So the total cost for n shovels is k * n. We need this total to be equal to a multiple of 10 plus r, but wait no. Wait, because he can use any number of 10-burle coins and exactly one r-burle coin. Wait, no. Wait, the problem says that he has an unlimited number of 10-burle coins and exactly one coin of r burles. So he can pay the total amount by using some 10s and possibly that r. So the total cost must satisfy total = 10 * a + r * b, where b is 0 or 1. Because he can choose not to use the r-burle coin. Wait, but the problem states that he must pay without any change. So the total must be exactly equal to a sum of some 10s and the r (if he uses it). So possible cases are:

Either the total is a multiple of 10 (so he uses zero coins of r), or the total is a multiple of 10 plus r (so he uses exactly one r coin). Because he can't use more than one r coin since he only has one. 

So for each possible n (starting from 1 upwards), we need to check if (k * n) mod 10 is either 0 or r. Because (k * n) mod 10 gives the last digit. And the total cost can be split into 10-burles and possibly the r. For example, if the last digit is 0, then he can pay with just 10s. If the last digit is r, then he can use the r coin and 10s for the rest.

So the plan is: iterate n starting from 1, check if (k * n) mod 10 is either 0 or r. The first such n is the answer.

But since n can be up to what? Let's see. For k=1000, r=9. Then for n=1, 1000*1=1000, mod10 is 0. So answer is 1. So worst case, how high can n go? Let's think. For k and r such that k and 10 are coprime. For example, k=3, r=7. Then 3n mod 10 must be 0 or 7. Let's see:

n=1: 3 → no.

n=2: 6 → no.

n=3:9 → no.

n=4:12 mod10=2 → no.

n=5:15 mod10=5 → no.

n=6:18 mod10=8 → no.

n=7:21 mod10=1 → no.

n=8:24 mod10=4 → no.

n=9:27 mod10=7 → yes. So answer is 9.

So in the worst case, the loop can go up to 10 steps. Because the possible residues mod10 are 0-9, and after 10 steps, the residues will repeat. So if within 10 steps we don't find a valid n, then it's impossible? But the problem says that he can buy 10 shovels (since 10 is possible, as per the example given). Wait, but the problem says that the answer is always possible. Because even if all else fails, when you buy 10 shovels, then 10k. So 10k mod10 is 0. So he can pay with 10s. So for n=10, the mod is 0, which is acceptable. So the answer will be at most 10.

Wait, but let's see. For example, if k is 9 and r is 1. Then n=1: 9 mod10 is9. Not 0 or 1. n=2: 18 mod10 is 8. No. ... up to n=9: 81 mod10 is1. So yes. So answer is9. Then for n=10, it's 90 mod10 is0. So the answer is min between 9 and 10, which is9. So the maximum possible n we need to check is up to 10. Because if none of the first 10 n (1-10) gives a valid mod, then n=10 will be the answer. But in reality, since 10k is divisible by 10, n=10 is always a candidate. So the answer will be the minimal n in 1-10 where (k*n mod10) is either 0 or r. Because after n=10, you can have n=11, but maybe there's a smaller n.

So the algorithm can be: loop n from 1 to 10, check if (k * n) mod10 is 0 or equal to r. The first such n is the answer.

Because the possible residues when multiplied by k mod10 for n from 1 to 10 must cover all possibilities. Because 10 is the modulus. For example, if k mod10 is 3, then the possible residues as n increases are 3,6,9,2,5,8,1,4,7,0 for n=1 to 10. So in this case, the loop will check all possibilities. So the minimal n is found within 10 steps.

So the steps are:

1. For each n from 1 to 10, compute (k * n) mod10.

2. Check if the mod is 0 or r.

3. The first n where this is true is the answer.

Because once you find the first occurrence, you can return it immediately.

So for example, in the first sample input:

k=117, r=3.

k mod10 is 7.

So for n=1: 7 mod10=7. Not 0 or 3. No.

n=2: 14 mod10=4. No.

n=3: 21 mod10=1. No.

n=4:28 mod10=8. No.

n=5:35 mod10=5. No.

n=6:42 mod10=2. No.

n=7:49 mod10=9. No.

n=8:56 mod10=6. No.

n=9:63 mod10=3. Yes. So answer is9.

In the second example:

k=237, r=7.

k mod10 is7.

n=1:7 mod10=7, which is r. So answer is1.

Third example:

k=15, r=2.

k mod10=5.

n=1:5 mod10=5. Not 0 or2.

n=2:10 mod10=0. Yes. So answer is2.

So the algorithm works for these examples.

So the code can be written as:

Read k and r.

Compute k_mod10 = k %10.

Then for n in 1 to 10:

   if ( (k_mod10 * n) %10 ) in {0, r}:

       return n.

But wait, because k*n mod10 is (k mod10) *n mod10. So yes.

So the code would be:

k, r = map(int, input().split())

mod = k % 10

for n in range(1, 11):

    total_mod = (mod * n) %10

    if total_mod ==0 or total_mod == r:

        print(n)

        exit()

So this should work.

But wait, what if r is 0? Wait, the problem states that r is between 1 and 9. So no.

So the code is safe.

Testing the first sample input:

k=117 mod10=7. r=3.

Check n from1-10:

n=1:7*1=7 mod10=7. Not 3 or0.

n=9:7*9=63 mod10=3. So yes. Output 9.

Third example: k=15 mod10=5. r=2. n=2:5*2=10 mod10=0. So yes.

Second example: k=237 mod10=7. r=7. n=1:7*1 mod10=7. So yes.

Another example: k=9, r=1.

mod is9.

n=9:9*9=81 mod10=1. So yes. So code would return9.

So the code is correct.

This approach is O(1) time and space, which is optimal since the maximum iterations are 10. So for any input, the code runs in constant time, which is well within the time constraints.
</think>

```python
k, r = map(int, input().split())
mod = k % 10
for n in range(1, 11):
    if (mod * n) % 10 in {0, r}:
        print(n)
        break
```