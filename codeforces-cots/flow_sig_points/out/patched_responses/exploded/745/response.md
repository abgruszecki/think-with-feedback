<think>
Okay, let's see. So the problem is to find the number of triplets of points where the maximum distance between any two points in the triplet is at most d. The points are given in strictly increasing order. Hmm, right.

First, I need to think about how to approach this efficiently. The brute-force approach would be checking all possible triplets, but with n up to 1e5, that's O(n^3) which is way too slow. So we need a smarter method.

Since the points are sorted, maybe we can exploit that. For each point, find the farthest point that is within d distance from it. Then, for each such window, calculate how many triplets can be formed in that window.

Wait, but the points are sorted. So if the points are sorted in increasing order, then for any triplet, the two farthest points are the leftmost and rightmost. Because the points are in order. So the distance between the leftmost and rightmost in the triplet must be <=d. Because the points are sorted, if the left and right are within d, then all the middle points in between are within that range as well.

Oh right! So the problem reduces to finding all triplets where the rightmost and leftmost are within d. Because since the array is sorted, any three points in a window where the first and last are within d will satisfy the condition. So the triplet can consist of any three points in that window.

So the approach is: for each i, find the largest j such that x[j] - x[i] <=d. Then, all the points from i to j can form a group. The number of triplets in this group is the combination of (j - i +1) choose 3, but only if there are at least 3 points. But wait, no. Wait, for a given i, the maximum j is the farthest point where x[j] <=x[i] +d. So for each i, the window is from i to j. Then, within this window, how many triplets include x[i] as the left endpoint and x[j] as the right endpoint? No, wait. Because the triplet can be any three points in the window [i, j], not just those that include i. Because the window is the set of all points that can form a triplet where the left and right are within d. Wait, no. For example, suppose we have a window from i to j. Then, any triplet in this window will have their leftmost and rightmost points within the window. Since the entire window's left and right are within d, then any triplet within this window will have their left and right (the min and max of the triplet) also within d. So the problem becomes, for each possible window where the first and last elements are within d, count all possible triplets that can be formed within that window. But we have to avoid counting overlapping windows multiple times.

Wait, but how to count all possible triplets. Because a triplet can be part of multiple windows, so we need to find a way to count each triplet exactly once.

Alternatively, for each triplet, the leftmost point is some x[i], the rightmost is some x[k], and x[k] -x[i] <=d. Then, the triplet is i < j < k, where j can be any between i and k. So the triplet is i, j, k where i < j < k and x[k] -x[i] <=d.

So the problem is equivalent to finding all triplets (i, j, k) where i < j < k and x[k] -x[i] <=d. So how do we count these efficiently?

An efficient approach would be to, for each possible k (rightmost point), find the smallest i such that x[k] -x[i] <=d. Then, for each k, the number of possible triplets ending at k is the number of ways to choose two points from the elements between i and k-1, since j has to be between i and k-1. Wait, because in the triplet (i, j, k), j can be any between i and k-1. So for each k, we need to find the number of pairs (i, j) where i < j < k and x[k] -x[i] <=d.

But that seems a bit tricky. Let's think differently. For each k, the maximum possible i is the first point where x[k] -x[i] <=d. So for a given k, all the points from i_start to k-2 can form triplets with k. Wait, perhaps for each k, we can find the earliest i where x[k] -x[i] <=d. Then, the points from i to k-2 (since j must be at least i+1, and k must be j+1). Wait, maybe I'm getting confused here.

Alternatively, for each k, find the earliest i such that x[k] -x[i] <=d. Then, the number of triplets where the rightmost is x[k] is the combination of (k - i +1 -1) choose 2. Wait, because the number of points between i and k (inclusive) is (k -i +1). To form a triplet, we need any three points in this range, but the triplet must include the rightmost point (k) only if the leftmost is i. Wait, no. Because in this approach, the rightmost is k, and the leftmost can be any i' >=i (since x[k] -x[i'] <=d). But how does that relate to the triplet's leftmost and rightmost?

Wait, maybe for each k, the maximum number of triplets where the rightmost is k is the number of triplets that can be formed in the window [i, k], where i is the earliest index such that x[k] -x[i] <=d. Because for any triplet in that window, the rightmost point is k (since the array is sorted). Wait, no. Because a triplet within the window [i, k] can have their rightmost point as any of the points in that window. So that approach might not capture all possible triplets.

Hmm. Maybe a better approach is to sort the points (they are already sorted, which is good) and for each i, find the farthest j where x[j] -x[i] <=d. Then, the number of elements in the window is m = j -i +1. For each window of m elements, the number of triplets is C(m,3) if m >=3. However, if we sum this for all i, we'll be overcounting. Because a triplet can be entirely contained in multiple windows. For example, if a triplet is in the window [i, j], and also in [i+1, j], then it will be counted twice.

So we can't just sum all the C(m,3) for each i. That's a problem. So that approach is not correct.

Alternative approach: for each triplet (i,j,k), the maximum x[k] -x[i] must be <=d. Since the array is sorted, x[k] is the largest, x[i] is the smallest. So for each triplet, the condition is x[k] -x[i] <=d.

So the total number of such triplets is the sum over all possible k, of the number of pairs (i,j) where i < j < k, and x[k] -x[i] <=d.

But how to compute this efficiently.

So for each k, find the earliest i where x[k] -x[i] <=d. Let's call this left_k. Then, all i in [left_k, k-2] can form a triplet with j (i < j <k). Wait, for a given k, the possible i's are those where i ranges from left_k to k-2 (since j has to be between i and k). Wait, no. Because j can be any between i and k-1, as long as j>i and j <k. So for a given i (<=k-2), the number of j's is (k-1 -i) possible j's. Because j can be i+1, i+2, ..., k-1. So for each i where x[k] -x[i] <=d, the number of triplets (i,j,k) is (k-1 -i) possible j's.

So for each k, the number of triplets is the sum over i from left_k to (k-2) of (k-1 -i). Because j has to be between i+1 and k-1.

Wait, sum_{i = a to b} (k-1 -i) = sum of (k-1 -i) for i from a to b.

This sum is equal to sum_{d=0}^{b-a} (k-1 - (a +d)) ) = sum ( (k-1 -a) - d ) for d from 0 to (b-a).

Which is ( (k-1 -a) * (b -a +1) ) - sum_{d=0}^{b-a} d )

Sum of d from 0 to m is m(m+1)/2.

So the sum is (k-1 -a) * (b - a +1) - ( (b -a) * (b -a +1) ) / 2 )

In this case, a is left_k, and b is k-2.

Wait, but for a given k, the i can range from left_k to k-2. Because j has to be between i and k-1, so i can be up to k-2 (since j must be at least i+1, which would be k-1). So the maximum i is k-2, because then j is k-1, and k is the third.

So for each k, the possible i's are left_k <= i <=k-2.

So for each k, the number of triplets is sum_{i = left_k}^{k-2} (k-1 -i).

This sum can be calculated as:

Let m = (k-2 - left_k +1) terms. The sum is sum_{x=1 to m} x, which is m*(m+1)/2. Wait, wait. Because (k-1 -i) when i is from left_k to k-2.

For example, i = left_k: term is (k-1 - left_k)
i = left_k+1: term is (k-1 - (left_k+1)) = (k-1 - left_k) -1
...
i = k-2: term is 1.

So the terms are (k-1 - left_k), (k-1 - left_k -1), ..., 1.

So the sum is the sum of consecutive integers from 1 to (k-1 - left_k). Wait, no. Wait, the first term is (k-1 - left_k), then subtract 1 each step, until 1. So the number of terms is (k-1 - left_k) terms. Wait, for example, if the first term is T, then the terms are T, T-1, ..., 1. The sum is T*(T+1)/2. So in this case, T is (k-1 - left_k) - 0 ?

Wait, for example, if left_k is 0 and k-1 is 3. Then the sum is 3 + 2 +1 = 6, which is 3*4/2 =6. So yes. So the sum is (T * (T+1)) / 2, where T is (k-1 - left_k).

But wait, how many terms are there? For example, if the i runs from left_k to k-2. The number of terms is (k-2 - left_k +1) = (k-1 - left_k) terms. And the sum is (T)(T+1)/2, where T is (k-1 - left_k) - 1 +1) ? Wait, no.

Wait, the sum starts with (k-1 - left_k) and decreases by 1 each term until 1. So it's the sum of the first (k-1 - left_k) numbers. Because if you have (k-1 - left_k) terms, starting from 1 and going up to (k-1 - left_k), the sum is (k-1 - left_k)(k- left_k)/2. So for example, if (k-1 - left_k) is 3, sum is 3*4/2=6.

But in our case, the terms are (k-1 - left_k), (k-1 - left_k -1), ..., 1. So that's the same as summing from 1 to (k-1 - left_k). So the sum is ( (k-1 - left_k) ) * (k - left_k) ) / 2.

Yes. So for each k, the number of triplets is ( ( (k-1 - left_k) ) * (k - left_k) ) ) // 2.

So the plan is:

1. Sort the array. (But input is already sorted in increasing order.)

2. For each k (starting from 2 to n-1, since triplets need 3 elements), find left_k as the smallest i where x[k] -x[i] <=d. Then compute the number of triplets for that k as ( (k - left_k -1) * (k - left_k) ) // 2. But wait, k here is the index in 0-based or 1-based?

Wait, the input is given as 0-based or 1-based? The problem says the next line contains x1, x2, ..., xn. So in the code, probably we'll read the list as 0-based in Python. But the code will be in Python, so the indexes are 0-based.

So for each k in 0-based indices (from 0 to n-1), but for a triplet to exist, there must be at least two elements before k, because j has to be <k. So for k >=2 (since i <j <k implies k must be at least 2). So for each k >=2, find left_k as the smallest index i such that x[k] -x[i] <=d. Then, the maximum number of i's is from i= left_k up to k-2. The number of elements in that range is (k-2 - left_k +1) = k-1 - left_k. But the sum is ( (k-1 - left_k) * (k - left_k) ) // 2.

Wait, but how to find left_k efficiently for each k?

Since the array is sorted, for each k, we can perform a binary search on the prefix of the array (0 to k) to find the smallest i where x[k] -x[i] <=d. Wait, no: wait, the left_k is the smallest i where x[k] -x[i] <=d. Because then, for i >= left_k, x[k] -x[i] <=d. So the range of i's for which x[k] -x[i] <=d is from left_k to k. So the earliest possible i is left_k.

But when considering triplets (i, j, k), j has to be between i and k. So for each k, the possible i's are left_k <=i <=k-2. Because j has to be at least i+1, and j <k. So i can be up to k-2.

So for each k, left_k is the first index i where x[k] -x[i] <=d. So the code would be for each k in 0..n-1:

if k < 2: continue.

left_k = binary search in 0..k for the smallest i where x[k] -x[i] <=d.

then, the count for k is sum over i from left_k to (k-2) of (k-1 -i).

But how to compute this sum efficiently.

Alternatively, the sum can be written as the sum of (k-1 -i) for i from a to b, where a is left_k and b is k-2.

Which is equal to sum_{i=a}^{b} (k-1 -i) = sum_{t= a}^{b} ( (k-1) - t )

= (k-1)*(b -a +1) - sum_{t=a}^b t 

sum_{t=a}^b t = (b*(b+1)//2) - ((a-1)*a//2)

So substituting:

sum = (k-1)*( (b -a +1) ) - ( (b*(b+1) - (a-1)*a) ) // 2 )

But in our case, a is left_k, and b is k-2.

So:

sum = (k-1)*( (k-2 - left_k +1) ) - ( ( (k-2)*(k-1) - (left_k -1)*left_k ) ) // 2 )

But this could be computationally heavy if done for each k. However, given that n is up to 1e5, and for each k, we can compute this in O(1) time (after binary search), this should be manageable.

But maybe there's a simpler way. Because the sum (k-1 -i) from i=a to b is equal to sum_{d=0}^{m} (m -d), where m = (k-1 -a) and m is the maximum term. The sum is (m*(m+1))//2.

Wait, when a is left_k and b is k-2. The sum is:

sum_{i = left_k}^{k-2} (k-1 -i) 

Let’s let i vary from left_k to k-2. Let’s substitute variable t = i - left_k. Then t ranges from 0 to (k-2 - left_k) = (k- left_k -2). 

So the sum becomes:

sum_{t=0}^{m} ( (k-1) - (left_k + t) )

where m = k-2 - left_k 

= sum_{t=0}^{m} ( (k-1 - left_k) - t )

= (m+1) * (k-1 - left_k) - sum_{t=0}^m t 

= (m+1)*(k-1 - left_k) - m(m+1)/2 

But m = (k-2 - left_k) 

So m+1 = (k -1 - left_k )

Thus:

sum = (k-1 - left_k) * (k-1 - left_k) ) - ( (k-1 - left_k -1 ) * (k-1 - left_k ) ) // 2 

Wait, substituting m = (k-1 - left_k -1) ?

Wait, m = (k-2 - left_k) = (k-1 - left_k) -1. So m+1 = (k-1 - left_k). So sum becomes (k-1 - left_k) * (k-1 - left_k) ) - ( ( (k-1 - left_k) -1 ) * (k-1 - left_k) ) // 2 )

= (k-1 - left_k) * [ (k-1 - left_k) - ( (k-1 - left_k -1) ) / 2 ) ]

But this seems more complicated. Alternatively, perhaps the sum can be written as ( (k-1 - left_k) * (k - left_k) ) // 2.

Wait, let's take an example. Suppose left_k is 0 and k is 3 (0-based), so k=3 (which is 4th element in 1-based). Then, the sum is (3-1-0) * (3-0) ) //2 → (2)*3//2 =3. Which is correct, since the terms are 2,1 → sum 3.

Another example: left_k=0, k=4 (0-based). The sum is i from 0 to 2 (k-2=2). Terms are 3 (4-1 -0=3?), wait no. Wait, k is 4, so (k-1 - left_k) is 4-1 -0=3. So (3 *4)/2 =6. The terms are 3,2,1 → sum 6. Yes. So this formula works.

So the sum is ( ( (k-1 - left_k) ) * (k-1 - left_k +1) ) ) //2.

Because the sum of 1+2+...+n is n*(n+1)/2. Here, n is (k-1 - left_k). Because the terms are (k-1 - left_k), (k-1 - left_k -1), ...,1. Which sums to ( (k-1 - left_k) * (k-1 - left_k +1) ) // 2.

Yes! So for each k, the number of triplets where the rightmost is k is ( ( (k-1 - left_k) ) * (k-1 - left_k +1) ) // 2. But only if (k-1 - left_k) >=1. Because if left_k is >=k-1, then there's no possible j between i and k-1.

So, the formula is:

count += max(0, ( ( (k-1 - left_k) ) * (k-1 - left_k +1) ) // 2 )

But how to find left_k for each k?

We can perform a binary search on the array from 0 to k (inclusive) to find the first index i where x[k] -x[i] <=d. Because the array is sorted, binary search is possible.

In Python, the bisect module can help here. For each k, we need the minimal i such that x[k] -x[i] <=d. Alternatively, for each k, the maximum x[i] >=x[k]-d. So we can find the first i where x[i] >=x[k]-d. Then, all points from i to k have x[k]-x[i] <=d.

Wait, no. Because x is sorted in increasing order. So x[k] -x[i] <=d → x[i] >=x[k]-d.

So the first i where x[i] >=x[k]-d. So left_k is this i. Because all points from i to k will satisfy x[k] -x[i'] <=d (since x[i'] >=x[i] >=x[k]-d).

So the correct approach is for each k, find the smallest i where x[i] >=x[k]-d. Then, left_k =i. So the number of points between i and k is (k -i +1). But wait, the i can be up to k. But in that case, the triplet would have only one point (i=k) which is not possible.

Wait, but for the triplet (i, j, k), i must be <=k-2. Because j must be between i and k-1.

So for each k, after finding left_k (the first i where x[i] >=x[k]-d), the possible i's are from left_k to k-2. Because j must be in i+1 to k-1.

So the number of valid i's is (k-2 - left_k +1) =k-1 -left_k. Only if left_k <=k-2. Otherwise, there are 0 triplets for this k.

Thus, for each k >=2, compute left_k as the first i where x[i] >=x[k] -d. Then, if left_k <=k-2, the count is ( (k-1 -left_k) * (k -left_k) ) //2. Else 0.

So the steps are:

Initialize total =0.

Sort the array (though input is already sorted).

For each k in 0..n-1:

   if k <2: continue.

   target =x[k] -d.

   left_k = bisect.bisect_left(x, target, 0, k+1)

   # since x is sorted, x[left_k] is the first >= target.

   # Now, the possible i's are left_k to k-2.

   # So if left_k >k-2: no triplet.

   # else: the number of i's is (k-2 -left_k +1) =k-1 -left_k.

   # The sum is (m*(m+1))//2 where m =k-1 -left_k.

   m =k-1 -left_k

   if m <=0:

       continue

   total += m*(m+1)//2

So that's the plan.

Now, test this against the examples.

First example:

Input: 4 3

x = [1,2,3,4]

For k=2 (0-based, x=3):

x[k]-d=0. Find the first i where x[i]>=0. All i. So left_k=0.

m=2-1 -0 =1.

sum is 1*2/2=1.

For k=3 (x=4):

x[k]-d=4-3=1. Find first i where x[i]>=1. That's 0. left_k=0.

m=3-1-0=2.

sum is 2*3/2=3.

Total is 1+3=4. Which matches the sample.

Second example:

Input:4 2

x =[-3,-2,-1,0]

For k=2 (x=-1):

x[k] -d =-3. Find first i >=-3. left_k=0.

m=2-1-0=1. sum 1*2/2=1.

For k=3 (x=0):

x[k]-d= -2. Find first i >=-2. The x array is [-3,-2,-1,0]. x[1] is -2. So left_k=1.

m=3-1-1=1. sum 1*2/2=1. So total is 1+1=2. Which matches the sample.

Third example:

5 19

x = [1,10,20,30,50]

For k=2 (20), x[k]-d=1. left_k=0 (x[0]=1).

m=2-1-0=1. sum 1.

k=3 (30): x[k]-d=11. Find first i where x[i]>=11. x[2]=20 >=11. left_k=2.

m=3-1-2=0. no sum.

k=4 (50): x[k]-d=31. x[3]=30 <31. x[4]=50 >=31. So left_k=4. m=4-1-4= -1. So 0.

Total sum is 1.

Which matches the sample.

So the approach works.

Now, the code.

In Python, for each k from 0 to n-1, but only process when k>=2.

We can use bisect.bisect_left from the bisect module.

But note that the input array is 0-based. So the code steps:

Read n and d.

Read the list x as a list of integers.

Sort x (but input is already strictly increasing, so perhaps not needed, but the problem states that the input is sorted. So no need to sort.)

Initialize total =0.

For each k in range(n):

   if k <2: continue

   target =x[k] -d

   left_k = bisect.bisect_left(x, target, 0, k+1)

   # because we are checking up to k (inclusive).

   m = (k-1) - left_k

   if m >0:

       total += m*(m+1)//2

   else:

       pass

Wait, but in the code, the indices are 0-based. For example, for k=2, the third element (0-based 2). Then, the possible i's are from left_k to 0 (k-2=0). So for left_k <=0.

So the code should handle that.

Testing code for the first sample:

k=2 (index 2, x=3). target 3-3=0. bisect_left looks for first i where x[i] >=0. x[0] is 1. So left_k=0. m= (2-1) -0 =1. sum += 1*2//2=1.

k=3 (x=4). target 4-3=1. x[0]=1. left_k=0. m=(3-1)-0=2. sum 2*3//2=3. total 4.

Yes.

So code should work.

Now, edge cases.

Case where n=3: the only possible triplet. If x[2]-x[0] <=d, then count is 1.

Another case: all points are within d. So for each k >=2, left_k=0. So for k=2, m=1. sum 1. For k=3, m=2. sum 3. For k=4, m=3. sum 6. Total 1+3+6=10. Which is C(5,3) =10. So correct.

So the code will correctly sum all possible triplets.

Now, time complexity.

Each binary search is O(log k) time, for k up to 1e5. So for 1e5 iterations, each O(log 1e5) steps. Which is acceptable. Because 1e5 * 20 is 2e6 operations, which is manageable.

Space complexity is O(n) for the x array.

So the code should work within the time and memory constraints.

Now, implement this.

In Python:

Import bisect.

Read n, d.

Read x as list.

Initialize total=0.

Loop over each k in 0 to n-1:

   if k <2: continue

   target = x[k] -d

   left_k = bisect.bisect_left(x, target, 0, k+1)

   m = (k-1) - left_k

   if m >0:

       total += m*(m+1)//2

Return total.

Yes.

So that's the code.

Testing the samples.

Sample 1:

4 3 → x = [1,2,3,4]

k=2 (x=3) → target 0. bisect_left returns 0 (x[0] is 1 >=0). m=2-1 -0=1. sum 1.

k=3 → target 4-3=1. x[0] is 1. left_k=0. m=3-1-0=2. sum 3. total 4.

Sample 2:

4 2 → x = [-3,-2,-1,0]

k=2 (x=-1) → target -3. bisect_left returns 0. m=1-0=1. sum 1.

k=3 (x=0 → target-2. bisect_left for -2 in array [ -3, -2, -1, 0 ] → index 1. m=3-1-1=1. sum +=1. total 2.

Sample3:

5 19 → x= [1,10,20,30,50]

k=2 → target 20-19=1. x[0]=1. left_k=0. m= (2-1) -0 =1. sum 1.

k=3 → x=30. target 30-19=11. bisect_left finds first x >=11. x[2]=20 >=11. So left_k=2. m= (3-1) -2=0. no addition.

k=4 → target 50-19=31. x[3] =30 <31. x[4]=50 >=31. left_k=4. m=4-1 -4= -1. no addition.

So total 1.

All correct.

Thus, the code should work.
</think>

```python
import bisect

n, d = map(int, input().split())
x = list(map(int, input().split()))
total = 0

for k in range(n):
    if k < 2:
        continue
    target = x[k] - d
    left_k = bisect.bisect_left(x, target, 0, k+1)
    m = (k - 1) - left_k
    if m > 0:
        total += m * (m + 1) // 2

print(total)
```