<think>
Okay, let's see. The problem is about finding the smallest possible k such that Awruk's total votes are strictly more than Elodreip's. And k has to be at least the maximum a_i in the list. Hmm.

So, first, the total votes Elodreip gets is the sum of all a_i. Let's call that sum_elodreip. Then, Awruk's total is the sum of (k - a_i) for each student. So sum_awruk = n*k - sum_elodreip. We need sum_awruk > sum_elodreip. Let's write that inequality.

n*k - sum_elodreip > sum_elodreip
=> n*k > 2 * sum_elodreip
=> k > (2 * sum_elodreip) / n

But k has to be an integer, and also k must be at least the maximum a_i. So the minimal k is the maximum between the ceiling of (2*sum_elodreip +1)/n (since (2sum)/n could be fractional) and the maximum a_i. Wait, let's think.

Let me re-arrange the inequality. We need k > (sum_elodreip * 2) / n. Since k must be an integer, the minimal possible k is floor((2sum_elodreip)/n) + 1. But also, k must be >= max_a. So the answer is the maximum between max_a and that value.

Wait, let's take example 1. Sum_elodreip is 1+1+1+5+1=9. n=5. So 2*9=18, divided by 5 is 3.6. So k needs to be >3.6, so 4. But in the first example, the output is 5. Because the max_a is 5. So the maximum between 4 and 5 is 5. Which matches the example.

Another example: input 2 is 5 students with a sum of 2+2+3+2+2=11. 2*11=22. 22/5=4.4. So k needs to be at least 5. The max a_i is 3, but 5 is larger. So the answer is 5, which matches the example.

So the formula seems to be: compute the minimal k as the ceiling of (2*sum_elodreip +1)/n. Wait, wait. Let's see. Let me compute (sum_elodreip * 2 +1) // n, but maybe that's not right.

Wait, the formula for the minimal k that satisfies k > S*2 /n is ceil(S*2 /n + epsilon), but since k has to be an integer, the minimal k is floor(S*2 /n) +1. Because, for example, if S*2 is exactly divisible by n, then k must be (S*2/n)+1. Otherwise, it's the next integer after S*2/n.

So the minimal k required based on the sum is (2*S + n -1) // n. Because that's the formula for ceiling division. For example, (a + b -1) // b gives the ceiling of a/b.

Wait, ceiling(a/b) is equal to (a +b -1) // b. So in this case, the required k is ceiling( (2*S) /n ) if 2*S is not exactly divisible by n, but since the condition is k> (2S)/n, then the minimal k is (2S +n -1) //n. Let me see.

Wait, (2S)/n may not be an integer. Let's say (2S) = q*n + r, where 0 <= r <n. Then ceiling( (2S)/n ) is q+1 if r>0. So if 2S divided by n is not an integer, then the minimal k is q+1. If it is an integer, then k must be q+1 (since k must be strictly larger than 2S/n). Wait, wait. Wait, 2S/n is an integer. Then, the inequality is k > x, where x is integer. So the minimal k is x+1.

So in both cases, the minimal k is ceiling( (2S +1)/n ), wait no. Wait, if 2S is exactly divisible by n, then 2S/n is x, and the required k is x+1. So for example, 2S=10, n=5. Then x=2, k must be 3.

But if 2S=9, n=5, then 9/5=1.8, so k must be 2.

So the formula for the required k is (2S +n) // (n +1)? No. Let's think again.

Wait, the required k is the minimal integer such that k > (2S)/n.

Which is equivalent to k >= floor((2S)/n) +1.

But floor((2S)/n) is the integer part. So for example, 2S=9, n=5: 9/5 is 1.8, floor is 1. So k is 2.

If 2S=10, n=5: floor is 2. So k is 3.

So the formula for the required k is (2S +n -1) //n.

Wait, let's check:

For 2S=9, n=5: (9 +5-1)/5 =13/5=2.6, floor is 2. So yes.

For 2S=10, n=5: (10+5-1)/5=14/5=2.8, floor is 2. Hmm, that's not right. Wait, because 2S is 10, which is exactly divisible by 5, so required k is 10/5 +1= 2+1=3.

But (2S +n -1)/n = (10 +5-1)/5 =14/5=2.8 → floor is 2. So that's not correct. Hmm. So maybe my formula is wrong.

Ah, wait. The problem is that (2S +n -1) //n gives ceiling(2S/n). But in the case where 2S is divisible by n, the ceiling is exactly 2S/n. But our required k is 2S/n +1. So the formula (2S +n -1) //n gives 2S/n when 2S is divisible by n, which is not sufficient. So that formula gives the ceiling of (2S)/n, but we need k to be strictly greater than (2S)/n. So when 2S/n is an integer, the required k is (2S/n) +1. So the correct way is to compute the minimal k as the maximum between max_a and (2S +1) //n.

Wait, let's see. Let's compute (2S +1) //n. For example, when 2S=10, n=5. (10+1)/5=11//5=2. So k would be 2, which is not enough. So that approach is incorrect.

Hmm, perhaps I need to adjust the formula. Let's think again.

The required condition is n*k > 2*S. So k must be greater than 2S/n. The minimal integer k satisfying this is floor(2S/n) +1.

Yes. Because floor(2S/n) is the largest integer less than or equal to 2S/n. Adding 1 gives the smallest integer greater than 2S/n.

So the formula is k_min = (2S //n) +1 if 2S is not divisible by n, otherwise k_min = (2S//n) +1.

Wait, regardless of whether 2S is divisible by n. Let's take 2S=10, n=5. 2S//n is 2. So k_min is 3. Which is correct.

For 2S=9, n=5: 9//5=1. So k_min is 2. Correct.

So the minimal k based on the sum is (2S //n) +1. But wait, (2S +n -1) //n is the same as (2S -1) //n +1. Let's see:

Wait, (2S +n -1) //n is equivalent to ceiling(2S /n). For example, 9/5=1.8, ceiling is 2. So (9 +5-1)/5=13/5=2.6, floor is 2. Which is ceiling(9/5)=2. For 10/5=2, ceiling is 2. (10 +5-1)/5=14/5=2.8, floor is 2. So ceiling is 2, but required k is 3 in that case. So the ceiling is not sufficient. So the correct minimal k is (2S //n) +1.

Wait, in the case where 2S is divisible by n, the required k is (2S//n) +1. For example, 2S=10, n=5: 10//5=2. 2+1=3. Which is correct. So the formula is:

k_min_sum = (2S // n) +1

But then, in the case where 2S is not divisible by n, (2S//n) gives the floor. For example, 9//5=1, +1=2. Which is correct.

So the minimal k that satisfies the sum condition is k_min_sum = (2S //n) +1.

So the answer is the maximum between k_min_sum and max_a.

Yes. So the steps are:

1. Compute sum_elodreip = sum(a)

2. Compute max_a = max(a)

3. Compute k_min_sum = (2 * sum_elodreip // n) + 1

4. The answer is max(k_min_sum, max_a)

Wait, but wait. Let's test with the first sample input.

Sample 1:

n=5, a=[1,1,1,5,1]

sum_elodreip=9

k_min_sum = (2*9 //5) +1 = 18//5=3, +1=4. So max between 4 and 5 (max_a is 5) is 5. Correct.

Sample 2:

sum_elodreip=2+2+3+2+2=11.

k_min_sum = (22//5) +1=4+1=5. max_a is 3. So max(5,3)=5. Correct.

Another test case: suppose sum_elodreip is 6, n=3. Then 2*6=12. 12//3=4, +1=5. So k_min_sum is 5. Max_a is, say, 4. Then answer is 5. If max_a is 6, then answer is 6.

Another test case: sum=3, n=2. Then 2*3=6. 6//2=3, +1=4. So if max_a is 3, answer is 4. Because with k=4, sum_awruk is 2*4 -3 =5, sum_elodreip is 3. 5>3. So yes.

So the formula seems to work.

Therefore, the approach is to calculate sum_elodreip, find max_a, compute k_min_sum as (2*sum_elodreip //n) +1, then the answer is the maximum between k_min_sum and max_a.

So in code:

Read n.

Read list a.

sum_elodreip = sum(a)

max_a = max(a)

k_min_sum = (2 * sum_elodreip // n) +1

k = max(k_min_sum, max_a)

print(k)

Wait, but let's check the case where 2*sum_elodreip is not divisible by n.

For example, sum_elodreip=5, n=3. 2*5=10. 10//3 is 3. So k_min_sum is 4. So 3*4=12 >10. So sum_awruk is 12-5=7. sum_elodreip is 5. 7>5: correct.

Yes.

Another example: sum_elodreip=4, n=3. 8//3=2. k_min_sum is 3. So sum_awruk is 3*3 -4=5>4.

Yes.

So the code should work.

Now, considering the constraints. n is up to 100, a_i up to 100, so sum_elodreip can be up to 100*100=10^4. So 2*sum_elodreip is up to 2e4. All operations are O(n), which is acceptable.

So the code should be straightforward.

Now, test the sample input 1:

5

1 1 1 5 1

sum is 9.

k_min_sum = (18//5)+1 =3+1=4. Max_a is 5. So max(4,5)=5. Correct.

Sample input 2:

5

2 2 3 2 2

sum is 11.

k_min_sum= (22//5)+1=4+1=5. Max_a is 3. So 5. Correct.

Another test case: n=1.

If a is [1], then sum is 1. k must be >=1.

sum_awruk is k-1. Need k-1>1 →k>2. So minimal k is 3. So code gives (2*1//1)+1=2+1=3. Max_a is 1. So 3.

Another example: n=1, a=100. sum_elodreip=100. k must be >=100. sum_awruk is k-100. Need k-100>100 →k>200. So minimal k is 201. Code gives (200//1)+1=200+1=201. Which is correct.

So the code works.

Therefore, the solution is to compute sum, max_a, compute (2*sum//n)+1, take the maximum between that and max_a.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
max_a = max(a)
required = (2 * s // n) + 1
k = max(required, max_a)
print(k)
```