<think>
Okay, let's see. I need to solve this problem where given n, k, and t, I have to find the array of ai values that form the progress bar according to the given rules. Hmm, let me think about how the progress bar is structured.

From the problem statement, the progress bar has some initial squares at k, then possibly one square that's between 0 and k, and the rest at 0. So, for example, if i is the position where the transition happens, then all squares before i are k, square i is some value a_i (0 <= a_i <=k), and the rest are 0. But wait, maybe there's a case where all squares are k (like 100% completion) or all are 0 (0% completion).

The sum of all ai divided by (n*k) gives a value that's used to compute t. The formula given is that t is such that sum(ai)/(n*k) ≤ t/100 < (sum(ai)+1)/(n*k). So the sum S of the ai's must satisfy S ≤ t*n*k/100 and S+1 > t*n*k/100. But wait, maybe that's equivalent to S being the floor of (t * n *k) / 100, but I'm not sure. Let me rephrase the inequality.

Let me denote t as t. The sum S = sum(ai). The inequality is S <= (t/100)*n*k < S +1. So S is the maximum integer less than or equal to (t/100)*n*k. So S is the floor of t*n*k / 100. But wait, because (t/100)*n*k could be a fractional value. So S is the integer part. For example, if t is 54, n=10, k=10, then (54 * 10 *10)/100 = 54. So sum(ai) must be 54. That's exactly the first example, which gives a sum of 5*10 +4 = 54. So yeah, the sum S is floor(t*n*k /100), but perhaps we have to be careful with fractional parts.

Wait, wait. Let me compute (t * n * k) /100. For example, in the first example, 54 *10*10 = 5400, divided by 100 is 54. So S is exactly 54. So in that case, sum(ai) is 54. The output is 10,10,10,10,10,4,0,0,0,0. Summing those: 5*10=50 +4=54. Correct.

Another example: input 11 13 37. So 37 *11*13 /100. Let's compute that. 37 * 143 = 5291. Divided by 100 is 52.91. So sum S is 52. So the sum of ai's must be 52. How? The output is 13,13,13,13,0 followed by zeros. That's 4*13 =52. So yes.

So the sum S is the floor of (t * n *k)/100. Wait, wait. Let's check. For example, if t is 100%, then S = (100 *n*k)/100 =n*k. So sum is n*k. Which would mean all ai's are k. That's correct.

If t is 0, sum is 0. So all ai's are 0. So the sum S is indeed the integer part of (t *n *k)/100. So the first step is to compute S as (t *n *k) // 100. Wait, but maybe we need to compute it as floor(t *n*k /100). For example, when the product is an integer, it's straightforward. Otherwise, when fractional, we take the integer part.

Once we have S, the next step is to construct the array of ai's. The structure is that there are some full k's, then one possible partial, then zeros. So the number of full k's is m = S // k. Then the remaining part is r = S %k. For example, S=54, k=10: m=5 (5*10=50), r=4. So the first 5 elements are 10, then the sixth is 4, rest zeros.

But wait, in some cases, S could be exactly m*k. Then r is zero, and the m elements are k, and the next element (m+1) would be zero, but since the sum is exactly m*k, the rest are zero. So the array would have m elements of k, then all zeros.

So the steps are:

1. Compute S = (t *n*k) // 100. Because (t/100)*n*k is the upper bound, and S must be <= that. So integer division.

2. Then compute m = S //k. The number of full k's. Then r = S %k. So the first m elements are k, then (m+1)th is r, and the rest are 0.

But wait, let's check that. For example, in the first example, S=54. m=54//10=5, r=4. So first 5 elements 10, next (6th) 4, rest zero.

In the second example, S=52. 52//13 is 3 (13*3=39, 52-39=13? Wait 3*13=39, 52-39=13, which is equal to k (13). So m=4? Because 4*13=52. Wait, 52 divided by 13 is exactly 4. So m=4, r=0. Then first 4 elements are 13, then the fifth is 0 (since r is 0), and the rest are zeros. Wait but the example output shows four 13s and then 0. Let's see the example input 2:

n=11, k=13, t=37. S= (37*11*13)/100 = 37*143=5291. 5291/100 is 52.91. So floor is 52. So S=52. 52 divided by 13 is 4, since 4*13=52. So m=4, r=0. So the first four elements are 13, and the fifth is 0, and the rest 7 elements are 0. So output would be 13,13,13,13,0,0,0,0,0,0,0. Which matches the second example.

Ah, right. So in that case, there are exactly m=4 full k's (since 4*13=52), and the fifth element is zero (r=0), but according to the problem statement, the transition is that there's at most one square with a value between 0 and k. So when r is zero, that fifth element is zero, but the first four are k. So the structure is: the first m elements are k, and the m+1-th element is r. If r is zero, then all after m are zero. So even if m is 4, the fifth element is zero.

So the array would be: for the first m elements, k; the (m+1)th element is r (which could be zero); the rest are zero.

Wait, but if m is 4 and r is zero, then the fifth element is zero, but according to the problem statement, the bar can have all the first i-1 squares as k and the i-th square can be zero (but that's allowed since 0 <= a_i <=k). So even if r is zero, we can have the m-th element as k, the (m+1)th as zero, and the rest as zero. But this would imply that i is m+1, and a_i is zero. But according to the problem statement, the i-th square can have any value from 0 to k. So that's allowed.

So the algorithm is:

Compute S = floor(t * n *k / 100).

Then m = S // k.

r = S %k.

Then:

The first m elements are k.

The (m+1)th element is r.

The remaining elements are zero.

But wait, what if m is larger than n? For example, if n=3, k=10, t=100. Then S= (100*3*10)/100 =30. m=30//10=3. Which is equal to n. So the first 3 elements are 10, r=0. Then the m+1 is 4, which is beyond the array. So in that case, we have to make sure that m+1 does not exceed n.

So in code, we can have:

Construct the array as follows:

- For each position from 1 to n:

   - if index <= m: k

   - elif index == m+1: r

   - else: 0

But wait, m can be up to S//k. S is at most n*k (when t=100). So S//k is at most n. Because S <= n*k. For example, when t=100, S= n*k. So S//k is (n*k)/k =n. So m =n. Then m+1 is n+1, which is beyond the array. So in that case, the (m+1)th element is beyond the array, so we ignore it, and set all elements up to m as k.

So for example, when m =n, then r= S%k. But S =n*k, so r=0. So the first n elements are k. So that's correct.

So the code steps:

Compute S = (t *n *k) // 100.

m = S // k

r = S % k

Then:

ai is k for the first m elements.

If m < n, then the (m+1)th element is r.

The rest are zero.

So code-wise:

We can loop through each index from 0 to n-1 (assuming 0-based). For each i:

if i < m: ai =k

elif i ==m: ai =r

else: 0

Wait, but m could be up to S//k. If S is 54, k=10, m=5. Then, the first 5 elements are 10, the 6th (i=5 in 0-based) is 4, others 0.

Yes.

So in code, for Python:

n, k, t = map(int, input().split())

s = (t * n * k) // 100

m = s // k

r = s % k

result = []

for i in range(n):

    if i < m:

        result.append(k)

    elif i == m:

        result.append(r)

    else:

        result.append(0)

# Now, handle the case where m exceeds n?

Wait, but m is s//k, and s is at most (100 *n *k)//100 =n*k. So s//k is <= n*k //k =n. So m can be at most n. So when m is n, then i can go up to n-1.

In that case, the code would add k for the first m elements (i < m), but m is n. So in 0-based, the first n elements (i from 0 to n-1) are all k. So the second part (i ==m) would never execute because m is n, which is beyond the range. So that's correct.

For example, if n=3, k=10, t=100. s= 3*10*100//100=30. m=30//10=3. So in the loop, i <3 (0,1,2) are set to 10. Then for i=3 (which is m), but n=3, the loop runs from 0 to 2. So all elements are 10. Correct.

Another example: when s is 0 (t=0), m=0. Then, first part (i<0) is none, then i==0 (m=0) adds r=0, then others. But if s is 0, r is 0. So all elements are 0, which is correct.

So this code should handle all cases.

Testing the first example:

Input: 10 10 54.

s= (54 *10*10)//100=5400//100=54.

m=54//10=5. r=54%10=4.

So for i=0-4 (0-based, 5 elements) → k=10. i=5 (6th element) → r=4. The rest 0. So output is [10,10,10,10,10,4,0,0,0,0], which matches.

Second example: input 11 13 37.

s=37*11*13= 37*143=5291. 5291//100=52. s=52.

m=52//13=4 (13*4=52). r=0.

So elements 0-3 (1st to 4th) are 13. i=4 (5th element) → r=0. The rest 0. So output is [13,13,13,13,0,0,0,0,0,0,0], which matches.

Another test case: n=3, k=10, t=100. s=3*10*100//100=30. m=30//10=3. So all 3 elements are 10. Output 10 10 10.

Another test case: n=5, k=5, t=50.

s= (50 *5*5)/100 = 12.5 → floor is 12. m=12//5=2, r=2. So first 2 elements 5, third 2, rest 0. Output:5 5 2 0 0.

Yes, sum is 5+5+2=12. 12/(5*5) = 12/25 = 0.48 → 48% → but t is 50. Wait, but 12.5 is 50% of 25. So S is 12, which is less than 12.5. So the sum is 12. So the output would be 5,5,2,0,0. But according to the problem's formula, (sum)/(n*k) ≤ t/100. Here sum=12, nk=25. 12/25=0.48 ≤ 0.5. Then sum+1=13. 13/25=0.52 >0.5. So t=50% is correct.

Thus, the code seems correct.

So the Python code would be straightforward.
</think>

```python
n, k, t = map(int, input().split())
s = (t * n * k) // 100
m = s // k
r = s % k
result = []
for i in range(n):
    if i < m:
        result.append(str(k))
    elif i == m:
        result.append(str(r))
    else:
        result.append('0')
print(' '.join(result))
```