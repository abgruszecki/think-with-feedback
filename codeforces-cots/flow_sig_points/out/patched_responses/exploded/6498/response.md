<think>
Okay, let's tackle this problem. The task is to find the number at the nth position in a specific sequence. The sequence starts with 1, then 1,2, then 1,2,3, then 1,2,3,4, and so on. So each block k consists of numbers from 1 to k, and the blocks are arranged in increasing order of k. For example, the third block is [1,2,3], which adds 3 elements. 

First, I need to model the structure of the sequence. Let's think about how the blocks contribute to the total length. The first block (k=1) contributes 1 element. The second block (k=2) contributes 2 elements. The third block contributes 3, and so on. But wait, the way the sequence is built is a bit different. Wait, the problem says that first comes 1, then 1-2, then 1-3, then 1-4, etc. So the first block is k=1, which is [1], then k=2, which is [1,2], then k=3: [1,2,3], etc. Wait no. Wait the problem says the sequence is built as: first the number 1, then numbers 1 to 2, then 1 to 3, then 1 to 4, etc. So the entire sequence is:

1 (from k=1), then 1,2 (from k=2), then 1,2,3 (from k=3), then 1,2,3,4 (k=4), etc. So each block k has exactly k elements, and the total length up to block m is the sum of k from 1 to m. Wait no. Wait, wait: the first term is k=1 (sum 1), then the next block is k=2 (sum 2), then k=3 (sum 3), etc. So the total length up to block m is 1 + 2 + 3 + ... + m = m*(m+1)/2. Wait, but that's the sum of the first m natural numbers, which is m(m+1)/2. But wait, the sum of the first m blocks would be the sum of each block's length. Each block k has length k. So the total elements after m blocks is sum_{k=1}^m k} = m(m+1)/2. 

But in the problem statement, each block is the numbers from 1 up to k. So the entire sequence is arranged as a series of blocks. So to find the nth element, we need to determine which block the nth element is in and then the position within that block.

But how? Let's see. Let's say we have blocks arranged as follows:

Block 1: [1] → length 1. Total so far: 1.

Block 2: [1,2] → length 2. Total: 1+2=3.

Block 3: [1,2,3] → length 3. Total: 3+3=6.

Block 4: [1,2,3,4] → length 4. Total: 6+4=10.

And so on. So each block k adds k elements. The total number of elements after m blocks is S(m) = m(m+1)/2. 

But wait, the blocks here are 1, 2, 3, ..., m. Wait no. Wait, the problem says that the sequence is built as first the number 1 (block 1), then the numbers 1 to 2 (block 2), then 1-3 (block 3), etc. So each block is for k=1, k=2, k=3, etc. So each block k has length k. So the sum up to m blocks is S(m) = 1 + 2 + 3 + ... + m = m(m+1)/2.

But the problem is, given n, find which block contains the nth element, and then find the position within that block.

So first, we need to find the largest m such that S(m) ≤ n. Then, the position within the next block (m+1) is pos = n - S(m). But wait, no. Because S(m) is the sum up to m blocks. If n is in the (m+1)th block, then the position within that block is n - S(m). Because the next block (m+1) starts at S(m) + 1. So for example, if n is 3, then S(2) is 3, so it's exactly the end of block 2. So the next block is 3, but n=3 is the end of block 2. So if S(m) >= n, wait, no. Let me think again.

Wait, the sum up to m blocks is S(m) = m(m+1)/2. Let's say n is such that S(m-1) < n ≤ S(m). Then the nth element is in the m-th block. The position within the m-th block is n - S(m-1). Because S(m-1) is the sum up to (m-1) blocks, so the m-th block starts at S(m-1) + 1 and ends at S(m). So for example, m=3: S(2)=3. The third block starts at 4 (if m=3, S(2)=3, then S(3)=6. So third block is positions 4,5,6. So for n=5, S(2)=3 <5 <=6. So m=3. The position within the block is 5-3=2. The third block is [1,2,3], so the answer is 2.

So the approach is:

1. Find the largest m where S(m) < n. Then the block is m+1. Wait, no. Wait, let's rephrase. We need to find the smallest m such that S(m) >=n. Then the block is m. But perhaps not. Let's take an example.

Take n=3. S(2)=3. So S(m)=3. So m=2. So the block is 2. The position in the block is 3 - S(1) = 3-1=2. The block 2 has elements [1,2], so the answer is 2.

Another example: n=4. S(2) is 3 <4. S(3)=6 >=4. So the block is 3. The position within the block is 4-3=1. So element is 1.

Wait, but S(3) is sum up to 3 blocks: 1+2+3=6. So blocks 1,2,3 have 6 elements. So the fourth element is the first element of the third block. Wait no, the third block is 1,2,3. So the first element of the third block is the fourth element. So n=4 is 1, n=5 is 2, n=6 is 3.

So how to find m such that the block is m. Let's think in terms of the sum of blocks up to m-1. If the sum up to m-1 is less than n, then the block is m, and the position within the block is n - S(m-1).

So the steps would be:

- Find the maximum m where S(m) < n. Then the block is m+1. But wait, S(m) is sum from 1 to m. So if S(m) <n <=S(m+1), then the block is m+1.

Wait, S(m) is sum of first m blocks. The next block (m+1) has length m+1. So S(m+1) = S(m) + (m+1). So the block m+1 starts at S(m)+1 and ends at S(m+1). So if n is in this range, then it's in block m+1.

So the approach is to find m such that S(m) < n <= S(m+1). Then the position within the block is (n - S(m)), and the value is that position. Because the block is [1,2,...,m+1], and the position in the block is (n - S(m)), which is the number we return.

But how to find m given n. Because n can be up to 1e14, we need an efficient way to compute m.

Let's model S(m) = m(m+1)/2. We need the maximum m where S(m) <n. Let's denote the total sum up to m blocks as S(m) = m(m+1)/2. We need to find the largest m where S(m) <n. Then, the block is m+1, and the position is n - S(m).

So solving for m in S(m) <n: m(m+1)/2 <n. We can model this as a quadratic equation. Let's rearrange the inequality: m² +m - 2n <0. The roots of the equation m² +m -2n =0 are m = [-1 ± sqrt(1 +8n)]/2. Since m is positive, we take the positive root: m = [sqrt(8n +1) -1]/2. So the maximum integer m that satisfies S(m) <n is floor([sqrt(8n +1) -1]/2). Let's check.

For example, take n=3. 8n+1=25, sqrt(25)=5. (5-1)/2=2. So m=2. Which is correct. Then S(2)=3, which is equal to n=3. Wait, but the condition is S(m) <n. So in this case, S(2)=3 is not less than n=3. So perhaps the correct approach is to find the maximum m where S(m) <n. Then the block is m+1. Wait, but how?

Wait, let's see. For n=3, S(2) is 3. So S(m) <3 would be m where m(m+1)/2 <3. Let's compute m:

m=1: 1 <3 → yes.

m=2: 3 <3 → no. So the maximum m where S(m)<3 is 1. Then the block is m+1=2, and the position is 3 - S(1) = 3-1=2. Which is correct.

So in this case, the formula [sqrt(8n +1) -1]/2 gives (sqrt(25)-1)/2 = (5-1)/2=2. But m must be 1 here. So the correct approach is to take the floor of (sqrt(8n +1)-1)/2, but perhaps subtract 1 when the square is a perfect square.

Hmm. Let's think again. Let me compute the value of x = (sqrt(8n +1) -1)/2. Then m is the largest integer less than x.

Wait, for n=3, 8n+1=25. x=(5-1)/2=2. So m is the largest integer less than x? Wait x is exactly 2, so m would be 1. So yes.

Another example: n=6 (sum up to m=3 is 6). So 8n+1=49, sqrt(49)=7. x=(7-1)/2=3. So m is 3-1=2? Wait no. Because for n=6, the block is 3. Because S(3)=6. So if n=6 is in the block m=3. So m is such that S(m-1) <n <=S(m). So for n=6, S(3)=6. So m is 3. Then the position in the block is 6 - S(2)=6-3=3. So the element is 3.

So how does the formula work here. For n=6, x=(sqrt(8*6+1)-1)/2 = (sqrt(49)-1)/2= (7-1)/2=3. So m is the floor of x. But 3 is the m where S(m)=6. So if our condition is to find m where S(m) <n, then for n=6, m would be 2. Then the block is 3, and position is 6-3=3.

Yes. So the formula gives x=3, floor(x)=3. Wait, but S(3)=6. But n=6. So S(m) <n would be 6<6, which is false. So the maximum m where S(m) <6 is 2. Because S(2)=3 <6. So the formula gives x=3, but we need to take m= floor(x) -1 if x is integer.

Wait, perhaps the correct approach is to compute m as the floor of (sqrt(8n+1)-1)/2), then check whether S(m) <n. Because sometimes (sqrt(8n+1) -1) could be even, leading to x being an integer. So for example, when n=3, x=2. Then S(2)=3 ==3, which is not less than n. So we need to subtract 1 in such cases.

Alternatively, we can compute m using binary search. Let's think about binary search. For example, the sum S(m) = m(m+1)/2. We need to find the largest m such that S(m) <n. The binary search can be between low=0 and high= some value (like 1e8, but since n can be up to 1e14, the maximum possible m is about sqrt(2e14) which is ~1e7). Wait, 1e14 *2= 2e14. sqrt(2e14) is around ~1.4e7. So binary search would take around 25 steps, which is acceptable.

But using the mathematical formula is more efficient. Let's see. Let's compute x = (sqrt(8n +1) -1)/2. Then m is the floor of x. But wait, when x is an integer, that would mean that S(m) = m(m+1)/2 = x*(x+1)/2. Let's see. For example, when x=2, S(m) is 3. So if n=3, x is 2. Then S(m)=3, which is equal to n. So we need to take m =x-1. But how to handle that.

Alternatively, the correct m is the floor of (sqrt(8n +1) -1)/2, but subtract 1 if (m*(m+1))/2 >=n.

Wait, perhaps the correct way is to compute m as the integer part of (sqrt(8n +1) -1)/2), then check if S(m) >=n. If yes, subtract 1. Otherwise, m is correct.

But perhaps a better approach is to use the formula and then adjust m accordingly.

Alternatively, we can compute m as the largest integer where m(m+1)/2 <n. So let's compute m using the formula m = floor( (sqrt(8n +1) -1)/2 ). Then, check if (m+1)*(m+2)/2 <=n. Wait, no. Let's think: For m computed as floor( (sqrt(8n+1)-1)/2 ), S(m) is m(m+1)/2. We need to find the maximum m where S(m) <n.

So for example:

If n=3, 8n+1=25, sqrt is 5. (5-1)/2=2. So m=2. But S(2)=3 which is not less than 3. So we need to subtract 1. So m=1.

If n=4: 8*4+1=33. sqrt(33)≈5.744. (5.744-1)/2≈2.372. So floor is 2. S(2)=3 <4. So m=2. Then the block is m+1=3. So position is 4-3=1. So element is 1. Which is correct.

So the formula gives m=2, which is correct here.

Another example: n=55. The sample input says the output is 10. Let's compute.

Compute m: 8*55+1=441. sqrt(441)=21. (21-1)/2=10. So m=10. Then S(10)=10*11/2=55. So S(m)=55, which is equal to n. So this is a problem because m is supposed to be the maximum where S(m) <n. But in this case, S(10)=55, which is equal to n=55. So m should be 9. So the formula gives m=10, but S(m)=55 is not less than n=55. So we need to adjust m to 9.

So the formula here gives m=10, but S(10)=55 is not less than n=55. So the correct m is 9.

So how to adjust for this? The way to compute m is to take the floor of (sqrt(8n +1) -1)/2), then check if (m+1)(m+2)/2 <=n. If not, then m is correct. Wait, perhaps not. Let's think again.

The formula (sqrt(8n +1) -1)/2 gives the solution to m(m+1)/2 =n. If that's an integer, then m is exactly that. But we need m where m(m+1)/2 <n. So if m is such that m(m+1)/2 <n, then the next m+1 may be such that (m+1)(m+2)/2 <=n.

Wait, perhaps the correct way is to compute m as the floor of (sqrt(8n +1) -1)/2). Then, if (m*(m+1))/2 >=n, subtract 1 from m.

Wait, let's test this approach with the examples.

For n=3:

m = floor( (sqrt(25) -1)/2 ) = floor( (5-1)/2 )=2. Then check if 2*3/2=3 >=3 → yes. So subtract 1 → m=1. Correct.

For n=55:

m= (sqrt(441)-1)/2 = (21-1)/2=10. Check if 10*11/2=55 >=55 → yes. So subtract 1 → m=9. Correct.

For n=56:

m = (sqrt(8*56 +1)-1)/2. 8*56=448+1=449. sqrt(449)≈21.2. (21.2-1)/2 ≈10.1 → floor is 10. Check if 10*11/2=55 >=56 → no. So m remains 10. So S(10)=55 <56. So the block is m+1=11. The position is 56-55=1. So the element is 1. Which matches the sample.

So the approach is:

Compute m = floor( (sqrt(8n +1)-1)/2 )

Check if m*(m+1)/2 >=n. If yes, subtract 1 from m.

Else, keep m.

Wait, but why? Because in cases where the formula gives m such that S(m) >=n, then we need to take m-1. Because the formula is derived from solving m(m+1)/2 =n, but we need m where S(m) <n.

Wait, let's see. The formula (sqrt(8n+1)-1)/2 gives the m where S(m) is the maximum possible m such that S(m) <=n. Because when you solve m^2 +m -2n=0, the positive root is the exact m where S(m) =n. But since m must be integer, floor of that root gives the maximum m where S(m) <=n. However, we need the maximum m where S(m) <n. So if S(m) ==n, then m must be reduced by 1.

So the steps would be:

Compute m = floor( (sqrt(8n +1) -1)/2 )

if S(m) >=n → then m is m-1. Because when S(m) equals n, then the actual block is m, but we need the sum of previous blocks. For example, when n=55, m=10, S(m)=55. So the block is m+1=11? No. Wait, the block m+1 is 11, but S(10)=55. So for n=55, the position is in the 10th block. Because the 10th block is the numbers 1-10. So the sum up to 10 blocks is 55. So the 55th element is the last element of the 10th block, which is 10.

Ah, so here's the confusion. The blocks are numbered as m=1, m=2, etc. Each block m has length m. So the sum up to block m is S(m) = 1+2+...+m = m(m+1)/2.

So, for a given n, to find the block m that contains it:

We need to find the minimal m such that S(m) >=n.

Wait, no. Because the blocks are added as 1, 1-2, 1-3, etc. So the first block is m=1 (sum 1), the second block is m=2 (sum 3 after two blocks), etc. So for n=55, it's exactly the sum after m=10, so the 10th block's last element. So the block is m=10. So the position in the block is n - S(m-1) =55 - S(9) =55 -45=10.

So the steps are:

1. Find the largest m such that S(m-1) <n <= S(m). Then the block is m.

Because S(m-1) is the sum of the first m-1 blocks. The m-th block starts at S(m-1)+1 and ends at S(m).

So for example, m=10: S(9)=45, S(10)=55. So block 10 is positions 46-55 (inclusive). So for n=55, it's in block 10, position 10 (55-45=10). The element is 10.

So the problem is to find m such that S(m-1) <n <= S(m).

But how to compute m.

So the approach is:

We can compute m as the value where S(m) >=n, and S(m-1) <n.

But how?

We can model it as finding the minimal m where S(m) >=n.

Because then, S(m-1) must be <n.

So to find m, we can compute the minimal m where m(m+1)/2 >=n.

This can be found via binary search.

Alternatively, solving for m in m(m+1)/2 >=n.

The minimal m satisfying this is the ceiling of the solution to m^2 +m -2n=0.

But perhaps binary search is easier to implement correctly.

Let's proceed with binary search.

The binary search will find the minimal m such that m(m+1)/2 >=n.

Once m is found, then the position in the block is pos =n - (m-1)*m/2.

The element is then pos.

For example:

n=3.

Find minimal m where m(m+1)/2 >=3.

Check m=2: 2*3/2=3 >=3. So m=2. pos=3 -1*2/2=3-1=2. So element is 2.

Which is correct.

n=55: m=10 (10*11/2=55 >=55). pos=55 -9*10/2=55-45=10. So element is10.

n=56: m=11 (11*12/2=66 >=56). pos=56 -10*11/2=56-55=1. So element is1.

Another example: n=5. Let's see.

We need minimal m where m(m+1)/2 >=5.

Check m=3: 3*4/2=6 >=5. So m=3. pos=5 -2*3/2=5-3=2. So element is2. Which matches the sample.

So this approach works.

So the steps are:

1. Find m such that m is the minimal integer where m(m+1)/2 >=n.

2. Compute pos =n - (m-1)*m/2.

3. Output pos.

So how to find m.

The binary search approach would be:

low=1, high= some upper bound (like 2e8, since for n=1e14, m is about sqrt(2e14)≈1.4e7).

Wait, m(m+1)/2 >=n → m^2 ~2n → m≈sqrt(2n). So for n=1e14, sqrt(2e14) is about 1.4e7. So binary search from low=1 to high=2e14 would work, but even better to use the formula and compute an approximate upper bound.

But binary search is straightforward.

So let's proceed with binary search.

Initialize low=1, high= 2e8 (a value larger than possible m for n=1e14). Because 1e14's m is about sqrt(2e14)= ~1.414e7. So high can be 2e14 to cover all possibilities.

Wait, for n=1e14:

m^2 ~ 2e14 → m ~ 1.414e7. So even high=2e8 is more than enough.

But binary search steps would be O(log(high)), which is manageable.

So the code for binary search:

def find_m(n):
    low =1
    high= 2e18  # since n can be up to 1e14, 2e18 is way larger than needed.
    # but to avoid using floating points, perhaps use high as 2e18.

    while low <=high:
        mid= (low +high)//2
        s=mid*(mid+1)//2
        if s >=n:
            high=mid-1
        else:
            low=mid+1
    return low

Wait, the logic here is to find the minimal m where s >=n.

Initially, low=1, high= some big value.

In each step, compute mid. If s >=n, then we need to check smaller values. So set high=mid-1.

Else, set low=mid+1.

At the end, low will be the minimal m where s >=n.

Let's test this for n=3:

Initial low=1, high=2e18.

mid= (1+2e18)//2. But for small n, let's see:

Wait, perhaps for n=3, the binary search would proceed as follows:

low=1, high=2e18 (but let's think for n=3).

Wait, perhaps it's easier to test with n=3.

Let's run through the steps.

n=3.

Initialize low=1, high= some value, say 3.

mid= (1+3)/2=2. s=2*3/2=3. s >=3 → set high=1.

Now low=1, high=1. mid=1. s=1*2/2=1 <3. So set low=2.

Now low=2, high=1 → loop exits. Return low=2. Which is correct.

Another test: n=55.

binary search:

Looking for m where m(m+1)/2 >=55.

The correct m is 10.

Let's see:

low=1, high= 1e18.

mid= (1+1e18)/2 (very large), but eventually the loop will narrow down.

Alternatively, perhaps it's better to compute via the formula and then adjust.

So, using the formula m = (sqrt(8n+1)-1)/2. Then m is the ceiling of that.

But perhaps the binary search is more straightforward.

Now, code-wise, the binary search can be implemented as follows.

Once m is found, compute pos= n - (m-1)*m//2.

So the code would be:

n = int(input())

left, right = 1, 2 * 10**18

m = 0

while left <= right:
    mid = (left + right) // 2
    s = mid * (mid +1) //2
    if s >=n:
        m = mid
        right = mid -1
    else:
        left = mid +1

pos = n - (m-1)*m//2

print(pos)

Let's test this with the sample inputs.

Sample 1:

Input 3 → output 2.

Compute m:

Binary search:

Looking for minimal m where m(m+1)/2 >=3.

Possible m=2. Because 2*3/2=3.

So m=2. pos=3- (1*2/2)=3-1=2. Correct.

Sample 5:

Input 5 → output 2.

Find m where m(m+1)/2 >=5.

m=3: 3*4/2=6 >=5. So pos=5 - (2*3/2)=5-3=2. Correct.

Sample 10:

Input 10 → output4.

Find m where m(m+1)/2 >=10.

m=4: 4*5/2=10 → yes. pos=10- (3*4/2)=10-6=4. Correct.

Sample 55 → output10.

m=10, 10*11/2=55. pos=55 - (9*10/2) →55-45=10. Correct.

Sample 56 → output1.

m=11. 11*12/2=66 >=56. pos=56 - (10*11/2)=56-55=1. Correct.

So this code works for all the samples.

Now, for handling very large n (up to 1e14), the binary search is O(log(2e18)), which is about 60 steps. So it's acceptable for time constraints.

In Python, the code should run quickly even for large n.

Regarding memory usage: the variables are all integers, and no additional data structures are used, so memory is O(1). So this approach is optimal.

Thus, this approach is correct and efficient.
</think>

```python
n = int(input())
left, right = 1, 2 * 10**18
m = 0

while left <= right:
    mid = (left + right) // 2
    s = mid * (mid + 1) // 2
    if s >= n:
        m = mid
        right = mid - 1
    else:
        left = mid + 1

pos = n - (m - 1) * m // 2
print(pos)
```