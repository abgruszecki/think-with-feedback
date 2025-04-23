<think>
Okay, let's see. The problem is about adding a rod of minimum possible length so that all rods (including the new one) can form a convex polygon with non-zero area. The initial set of rods can't form such a polygon.

Hmm, I remember that for a set of lengths to form a convex polygon, the sum of all other lengths must be greater than the maximum length. Wait, right! For a polygon, the sum of all sides except the longest one must be greater than the longest side. Otherwise, it's impossible. Because if the sum is <= the max, then the longest side is too long to form a closed polygon.

So the problem here is that initially, the sum of all rods except the maximum is <= the maximum. Because otherwise, they could form a polygon. But the problem states that they can't form a convex polygon, which implies that the initial condition must be sum of all except max <= max. Wait, but maybe there's another case. Like, when the sum of all except max is greater than the max, but some other arrangement of sides isn't allowed. Wait, no. For convex polygon, the sum of any n-1 sides must be greater than the nth. But that's not true. Wait, no. The polygon condition is that the sum of any (n-1) sides must be greater than the remaining side. Because for a triangle, it's the sum of two sides > third. For a quadrilateral, sum of three must be greater than the fourth. So for any convex polygon with n sides, each side must be less than the sum of all others.

So, the initial set of rods must have the sum of all lengths minus the maximum length <= the maximum length. Because otherwise, they could form a polygon, which contradicts the problem statement. So that's the starting condition.

Now, we need to add a new rod of length z such that when we add z to the set, the new set can form a convex polygon. We need to find the minimal possible z.

So, after adding z, the new set must satisfy the condition that the maximum length in the new set is less than the sum of all other lengths. Because then, the convex polygon can be formed by using all the rods as sides.

So, the problem reduces to finding the smallest z such that when added to the initial list, the sum of all elements (including z) minus the new maximum is greater than the new maximum.

Wait, let's formalize this. Let's denote the sum of the original rods as S, and their maximum as m. The initial condition is S - m <= m, so S <= 2m. Hence, adding a new rod z, the new sum is S + z. The new maximum is max(m, z). So there are two cases:

Case 1: z is the new maximum. Then, the condition becomes (S + z) - z > z → S > z. But since the original sum S <= 2m, and m is the original max. Wait, but if z is larger than m, then in this case, the new max is z. Then the sum of all other rods is S. So the condition is S > z. So z must be less than S. But since z is larger than m (case 1), this would require S > z. But the original sum S is <= 2m. So z must be less than S, which is possible if m < S. But S was originally S <= 2m. So if m < S, then S is between m and 2m. So for z to be the new maximum and satisfy S > z, z must be between m and S. But since S <= 2m, then m < z < S would require that m < S, which is possible only if S > m, which is possible when the original sum S - m <= m (i.e., S <= 2m) but S could be greater than m. Like, if S is m+1, then yes.

Wait, but the initial sum S is the sum of all rods. The maximum is m. The original S must be <= 2m. Because otherwise, the original rods could form a polygon, which is not allowed. So the initial condition is S <= 2m.

So in case 1, where z is the new maximum, the condition is S + z - z = S > z → z < S. But since z is the maximum (so z >= m), and S <= 2m, then for z to be < S and >= m, we need m <= z < S. But since S <= 2m, z can be up to S-1. The minimal z in this case would be when z is as small as possible. So the minimal possible z here is m, but only if m < S. But since S is the original sum which is S <= 2m. For example, if S is 2m, then S is 2m, so z must be less than 2m, and since z >= m (case1), the minimal z here is m. But in that case, the sum S + z would be 3m. The new sum is 3m. The new maximum is z = m. Then the sum of the other rods is 2m (original sum) → sum of others is 2m + m - m (since z is added)? Wait, maybe I need to re-calculate.

Wait, in case 1, when z is the new maximum, the sum of the other rods is S (original sum). So the condition is S > z → z < S. So the minimal z in this case is when z is the minimal possible value that is >= m (since it's the max in case 1) and also < S. The minimal such z is m, provided that m < S. But S is the original sum. Since original S = sum of rods, which includes m, so S = m + sum of others. The sum of others is sum_others = S_initial - m. The initial condition is sum_others <= m → S_initial - m <= m → S_initial <= 2m. So sum_others is <= m. Therefore, S_initial = m + sum_others = m + (<=m) → S_initial <= 2m. So in case 1, the sum S_initial is <= 2m. So the condition for case 1 is z < S_initial. But since S_initial can be up to 2m, and z >= m, then possible z in case 1 would be m <= z < S_initial. The minimal possible z here is m. But wait, let's check if adding z = m would satisfy the condition.

So in case 1, if z is m, and S_initial is <= 2m. Then the sum after adding z is S_initial + m. The new maximum is m (since original m is in the rods, and z is m). So the sum of all other rods (sum_initial) is sum_initial = S_initial. Because sum_initial is sum of original rods. The new sum after adding z is S_initial + z. The new maximum is max(m, z) = m (since z = m). So the sum of all other rods (excluding the new maximum) is S_initial. But the condition is sum_others > new_max. sum_others here is S_initial + z - new_max. Wait, maybe I'm getting confused here. Let me think again.

When you add the new rod z, the new list has n+1 rods. The new sum is S_new = S + z. The maximum of the new list is max(m, z). Let's denote this as m_new = max(m, z). To form a convex polygon, the sum of all rods except m_new must be greater than m_new.

So the condition is (S + z) - m_new > m_new.

So S + z - m_new > m_new → S + z > 2 * m_new.

So the condition is S + z > 2 * m_new.

Now, in case 1 where z is the new maximum (z >= m), then m_new = z. So condition becomes S + z > 2z → S > z.

So z must be less than S. But z is >= m. So the minimal possible z here is z = m, but only if m < S. Because if m >= S, then even z = m would not satisfy z < S. Wait, but S is sum of all original rods, including m. So S = m + sum_others. sum_others <= m (since the original sum_others is sum_initial - m, and sum_initial <= 2m → sum_others <= m). So S = m + sum_others <= 2m.

So, in case 1, the condition is z < S. But z must be >= m. So the possible z is from m up to S-1 (since z must be integer). So the minimal z in case 1 is m, but only if m < S. Because if m is equal to S, then z can't be less than S. Wait, but S is m + sum_others. Since sum_others <= m, S can be up to 2m. For example, if sum_others is m, S is 2m.

So, in case 1, the minimal z would be m, but this requires that m < S. But S is sum of all original rods. So sum_others = S_initial - m. So S_initial = m + sum_others. sum_others can be up to m (since the original sum_others <= m). So S_initial can be up to 2m. So for case 1 to be possible, z >= m and z < S_initial. So if S_initial > m, then there exists z in that range. But if S_initial == m (which is possible only if sum_others = 0, but since n >=3, sum_others can't be zero because all l_i are >=1). Wait, no. For example, if n=3 and the rods are 1, 1, 1. Then sum_initial is 3, m=1. sum_others is 2, which is > m. But that contradicts the problem's initial condition that they can't form a polygon. Wait, but in that case, the sum of other rods (2) is greater than m (1). So sum_others = 2 > 1. So the original rods can form a triangle. But the problem states that the initial set cannot form a convex polygon, so the example must have sum_others <= m. Wait, that's the key. So the initial sum_others (sum of all except the original max) must be <= m. Because otherwise, the original rods can form a polygon, which contradicts the problem statement. So in the problem's input, sum_others (sum of all rods except the original max) <= m. Because otherwise, the original set would satisfy the polygon condition, which is not allowed.

So sum_others = S_initial - m <= m → S_initial = m + sum_others <= m + m = 2m.

So, in case 1, when z is the new maximum (z >= m), the condition is S_initial + z > 2z → S_initial > z. But since S_initial <= 2m, then z must be < S_initial. And since z >= m, the possible z is m <= z < S_initial. But since S_initial can be up to 2m, the minimal z in this case is m. But S_initial can be as high as 2m. So if S_initial is 2m, then for z to be >=m and < 2m, the minimal z is m. So in that case, adding z = m would make the new sum 2m + m = 3m, and the new maximum is m. Then the sum of all others (sum_initial + z - m_new) is 2m + m - m = 2m. And 2m > m? Yes. So condition is satisfied. So that's valid.

But wait, if S_initial is 2m, then adding z = m gives the new sum 3m. The maximum in the new set is m (since original max was m and z is m). So sum of all other rods is 3m - m = 2m. So 2m > m → yes. So the condition is satisfied.

So in this case, adding z = m works, and it's the minimal possible in case 1.

But then there's case 2: when the original maximum m remains the maximum after adding z. So z <= m. Then, the new maximum is m. The condition is (S_initial + z) - m > m. So S_initial + z - m > m → S_initial + z > 2m → z > 2m - S_initial.

Since z must be >=1 (as per the problem statement, z is a positive integer), and also z <= m (case 2). So the minimal z in this case is the minimal integer z such that z > (2m - S_initial), and z <=m.

If (2m - S_initial) < 1, then z can be 1. Else, z must be at least (2m - S_initial + 1).

Wait, but we need to find the minimal z in this case. So the minimal z here is max( (2m - S_initial +1), 1 ). Because z must be an integer. But since z has to be positive.

Wait, let's see. The condition for case 2 is:

sum_new = S_initial + z

sum_new - m > m → S_initial + z - m > m → z > 2m - S_initial.

But since z is an integer, the minimal z is (2m - S_initial) + 1, but only if this value is <= m. Otherwise, case 2 is not possible.

So in case 2, the minimal possible z is max( (2m - S_initial + 1), 1 ), but this must be <= m.

So, for case 2 to be possible, the required z must be <=m and >= (2m - S_initial +1). So if (2m - S_initial +1) <= m → which rearranges to S_initial >= m +1. But S_initial is sum_initial = sum of all original rods. Since sum_initial = m + sum_others, and sum_others <= m (from problem's initial condition), sum_initial can be up to 2m. So for S_initial >= m+1, 2m - S_initial +1 would be <= m.

For example, if S_initial is m+1, then 2m - (m+1) +1 = m. So z must be >= m and <=m. So z =m.

But if S_initial is 2m, then 2m - S_initial +1 is 1. So z >=1 and <=m. So the minimal z is 1.

So in case 2, the minimal z possible is (2m - S_initial +1). But since z can't be zero, and must be at least 1, we take the maximum between that and 1.

So the overall approach is to compute the minimal z between case 1 and case 2, and choose the smallest possible.

So the steps are:

1. Find the original sum S_initial and the maximum m in the original list.

2. Compute sum_others = S_initial - m. Since the initial condition is sum_others <= m, which is given.

3. We need to find the minimal z such that either:

   a. case 1: z >= m and z < S_initial. The minimal z here is m (if possible). Because z must be >=m, and as small as possible.

   b. case 2: z <=m and z > (2m - S_initial). The minimal z here is (2m - S_initial) +1, but at least 1.

4. Compute both possible candidates and choose the minimal.

Wait, but how do we know which case gives a valid z?

For case 1 to be possible: z must be >=m and < S_initial.

But S_initial is sum_initial = m + sum_others. sum_others <= m, so sum_initial <= 2m.

So for case 1 to have possible solutions, m < sum_initial. Because z must be >=m and < sum_initial.

But sum_initial = m + sum_others. sum_others <=m. So sum_initial <= 2m. So m < sum_initial implies sum_initial > m → sum_others >0. Which is possible.

For example, sum_others can be m (sum_initial=2m), then sum_initial > m (m >0). So m < sum_initial.

So in that case, z can be m, which is >=m and < sum_initial (since sum_initial is 2m, m < 2m).

So in case 1, the minimal z is m.

But in case 2, the required z is (2m - sum_initial +1), but this must be <=m.

But let's compute both possibilities and take the minimal.

Wait, for example, consider the first sample input:

Sample 1:

3

1 2 1

Original sum S_initial = 1+2+1=4. m=2.

sum_others = 4-2 =2, which equals m (2). So sum_others is equal to m, which is allowed (since sum_others <= m).

The initial condition is sum_others <= m → 2<=2.

Now, the required z is the minimal that can be added.

Case 1: z >=m (2). So minimal possible z is 2. Then, sum_new =4+2=6. The new maximum is 2. sum_others_new =6-2=4. 4>2 → yes. So adding z=2 would allow forming a polygon. But sample output is 1.

Wait, why?

Wait the sample output is 1. Let's see. The sample input is 3 rods of 1,2,1. The output is 1.

Wait after adding z=1, the new rods are 1,2,1,1. Sum is 5. The maximum is 2. So sum_others_new is 5-2=3. Which is 3>2 → yes. So the sum of others (3) is greater than the maximum (2). So the required condition is satisfied. So adding z=1 is possible and minimal.

But according to case 1 and case 2:

In the first sample:

sum_initial =4, m=2.

Case 1: minimal z is 2. sum_initial + z =6. sum_others_new =6 -2=4>2 → valid.

Case 2: z > (2m - sum_initial) → 2*2 -4=0 → z>0. So minimal z is 1. sum_initial +1=5. sum_others_new=5-2=3>2 → valid.

So case 2 gives a smaller z (1), so the answer is 1.

Ah, right. So the minimal z can be from either case, and we need to consider both.

So the correct approach is to compute the possible candidates from both cases and pick the minimal.

So for case 1:

The minimal possible z is m (since z >=m and z < sum_initial). But sum_initial must be >m. If sum_initial <=m, then case 1 is not possible. Wait, sum_initial is m + sum_others. sum_others <=m. So sum_initial <= 2m. So sum_initial can be larger than m (if sum_others >0). So for case 1 to be possible, sum_initial must be >m. For example, sum_initial = m + sum_others. sum_others can be up to m. So sum_initial can be up to 2m, which is larger than m. So in that case, case 1's minimal z is m.

But when sum_initial is m + sum_others, sum_initial can be as low as m +1 (if sum_others is 1 and m is >=1). So sum_initial can be greater than m.

So in case 1, the possible z is m, but only if sum_initial > m. Otherwise, sum_initial is m (if sum_others is 0, but sum_others can't be zero because the problem states that the initial set can't form a polygon. For example, if sum_others is zero, then all other rods are zero. But the input constraints say l_i >=1. So sum_others is sum of n-1 rods, each >=1. So sum_others >=n-1 >=2 (since n >=3). So sum_initial is m + sum_others >= m +2. But m is the maximum of the original rods, which is >=1. So sum_initial >=3. But sum_initial is m + sum_others. sum_others can be up to m.

Wait, maybe sum_initial is 2m. Then sum_initial is larger than m (since m >=1).

So in any case, sum_initial is >= m +1 (since sum_others >=1 when n >=3). Because sum_others is sum of n-1 rods, each of which is at least 1 (since l_i >=1). So sum_others >= (n-1)*1. n-1 >=2. So sum_others >=2.

So sum_initial = m + sum_others >= m +2. So sum_initial is definitely larger than m. So case 1's condition (sum_initial >m) is always satisfied. So case 1's minimal z is m.

But in the first sample, the minimal z is 1, which is from case 2.

So how do we decide between the two options?

So, the answer is the minimal between the candidate from case 1 (m) and the candidate from case 2 (max(2m - sum_initial +1, 1)).

So the steps are:

1. Compute sum_initial = sum of all rods.

2. Find m = max(rods).

3. sum_others = sum_initial - m.

4. case1_candidate = m. But only if case1 is possible (sum_initial > m → which it is always true since sum_initial >= m + 2).

5. case2_candidate = max( (2m - sum_initial) + 1, 1 )

But case2_candidate must be <=m. Otherwise, it's not valid. But since sum_initial >= m + sum_others, sum_initial >= m +1. So 2m - sum_initial +1 = 2m - (m + sum_others) +1 = m - sum_others +1. But sum_others <=m (from problem's initial condition), so m - sum_others >=0. So case2_candidate is at least 1. But also, since sum_initial >= m +1, 2m - sum_initial +1 <= m.

Wait, let's see:

sum_initial = m + sum_others.

sum_others <= m.

so 2m - sum_initial +1 = 2m - (m + sum_others) +1 = m - sum_others +1.

sum_others can be from 2 to m (since sum_others >= n-1 >=2 when n >=3, and sum_others <=m).

So m - sum_others +1 can be from (m - m +1) =1 (if sum_others =m) up to (m - 2 +1) = m-1 (if sum_others=2 and m is large).

So case2_candidate is in 1 to m-1.

So case2_candidate is between 1 and m-1. So it's <=m.

So case2_candidate is valid for case 2.

So the minimal z is the minimum between case1_candidate (m) and case2_candidate (max(2m - sum_initial +1, 1)).

So in the first sample:

sum_initial=4, m=2.

case1_candidate=2.

case2_candidate= (2*2 -4) +1 = (4-4)+1=1.

max(1, 1) is 1.

so the minimal z is min(2,1) → 1.

Which matches the sample.

Another sample:

Sample 2:

5

20 4 3 2 1 → sum_initial =20+4+3+2+1=30. m=20.

sum_others=10 (30-20=10) which is <=20.

case1_candidate =20.

case2_candidate= (2*20 -30) +1 =40-30+1=11. So max(11,1)=11.

So min(20,11)=11 → which matches the sample.

So the correct approach is to compute both candidates and choose the minimum between them.

So the algorithm is:

Compute sum_initial and m.

Compute candidate1 = m.

Compute candidate2 = max( (2*m - sum_initial) +1, 1 )

Then, z = min(candidate1, candidate2).

But why is this the case?

Because the candidate1 is the minimal possible for case1, and candidate2 is the minimal possible for case2. The minimal z is the smaller of the two.

So, the code steps are:

Read n.

Read list of l.

sum_initial = sum(l).

m = max(l).

candidate1 = m.

required_in_case2 = (2*m - sum_initial) + 1

candidate2 = max(required_in_case2, 1)

z = min(candidate1, candidate2).

Wait, but is that sufficient? Let's test some edge cases.

Test case where adding z in case2 is better.

Another example:

n=3, rods [3,1,1]. sum_initial=5, m=3. sum_others=2 <=3.

case1 candidate is 3. case2 candidate is (2*3 -5)+1=6-5+1=2. So min(3,2) is 2. Let's see:

Adding z=2. sum_new=5+2=7. max is 3. sum_others_new=7-3=4>3 → yes.

So correct.

Another example:

n=3, rods [5,1,1]. sum_initial=7. m=5. sum_others=2 <=5.

case1 candidate=5. case2 candidate= (2*5 -7)+1=10-7+1=4. So min(5,4)=4.

sum_new=7+4=11. max is 5. sum_others_new=11-5=6>5 → yes.

So correct.

But wait, what if the case2 candidate is 1.

For example:

sum_initial = 2m-1.

sum_initial = 2m-1.

case2 candidate: (2m - (2m-1)) +1 → (1) +1=2. So candidate2 is 2. But sum_initial is 2m-1.

Wait, let's see:

sum_initial is 2m-1.

case2 candidate is (2m - sum_initial) +1 → (2m - (2m-1)) +1 → (1) +1=2.

But sum_initial is 2m-1. m is the max.

So when adding z=2 (case2 candidate), sum_new=2m-1+2=2m+1. The new max is m. sum_new - m = 2m+1 -m = m+1. Which must be > m → m+1>m → yes.

So correct.

Another test case where case2 candidate is 1.

sum_initial=2m. m is the max. sum_others =m.

case2 candidate: (2m -2m)+1=1. So z=1.

sum_new=2m+1. max is m. sum_new -m =m+1>m → correct.

Yes.

So the code would work.

But wait, what if candidate2 is larger than candidate1? Then the minimal would be candidate1.

For example, sum_initial=3, m=2. sum_initial=3, m=2. sum_others=1 (3-2=1). So case1 candidate is 2. case2 candidate is (4-3)+1=2. So min(2,2) is 2. So adding 2. sum_new=5. sum_others_new=5-2=3>2 → yes.

Yes.

So the code seems correct.

Now, the implementation.

We need to read n, then the list of l. Compute sum_initial and m.

Then compute candidate1 and candidate2, then output the minimal.

But wait, the constraints are n up to 1e5 and l_i up to 1e9. So sum_initial can be up to 1e5*1e9=1e14, which is manageable in Python.

So code:

Read n.

Read list l as integers.

sum_initial = sum(l)

m = max(l)

candidate1 = m

required_in_case2 = 2*m - sum_initial +1

candidate2 = max(required_in_case2, 1)

z = min(candidate1, candidate2)

print(z)

But wait, let's test the sample input 1.

Sample 1: sum=4, m=2.

required_in_case2= (2*2-4)+1 = (4-4)+1=1 → candidate2=1.

candidate1=2. min is 1.

Sample 2: sum=30, m=20. required_in_case2=40-30+1=11 → candidate2=11. candidate1=20. min is 11.

Yes.

Another test case:

n=3, l=[5,5,5]. sum_initial=15. m=5. sum_others=10, which is greater than m. But the problem states that the initial set can't form a polygon. So this case is invalid and won't be part of the input. So the code can assume that the initial sum_others (sum_initial -m) <=m.

But in code, we don't need to check that.

So code works.

So the code is as above.
</think>

```python
n = int(input())
l = list(map(int, input().split()))
sum_initial = sum(l)
m = max(l)
case1 = m
case2 = max(2 * m - sum_initial + 1, 1)
print(min(case1, case2))
```