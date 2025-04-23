<think>
Okay, so I need to solve this problem where I have to flip a subarray in a binary array exactly once to maximize the number of 1s. Hmm. Let's think about how to approach this.

The problem says that after flipping exactly one interval [i, j], we want the maximum possible 1s. Flipping here means changing 0 to 1 and 1 to 0 in that interval. So the goal is to choose the best possible subarray to flip such that the net gain in the number of 1s is maximized.

First, let's understand what flipping a subarray does. Each element in [i,j] is flipped. So for each position in that range, a 0 becomes 1 (which is good if it was 0 before) and a 1 becomes 0 (which is bad). The net gain for the subarray is (number of 0s in [i,j] minus number of 1s in [i,j]). Because flipping 0s gives us +1 each, and flipping 1s gives -1 each. So the total gain is (count0 - count1) for that interval.

The original number of 1s is the total_ones. Then, after flipping the interval, the total becomes total_ones + (count0 - count1) of the interval. So the problem reduces to finding the interval [i,j] where (count0 - count1) is maximized. Because adding that to the original total gives the maximum possible.

Alternatively, since count0 + count1 = (j - i + 1), the count0 - count1 can be written as (count0 - (j-i+1 - count0)) = 2*count0 - (j-i+1). But maybe it's easier to compute the difference as (count0 - count1) directly.

Wait, but how do I compute this for all possible intervals efficiently?

The straightforward approach is to check all possible intervals [i,j], compute the gain for each, and track the maximum. Since the array size is up to 100, the number of intervals is O(n^2) which is 100*100=10^4 operations. That's manageable. Even for n=100, 10^4 is small. So this approach would work within the time constraints.

So the plan is:

1. Compute the original total number of 1s in the array.
2. For every possible interval [i,j], compute the number of 0s and 1s in that interval.
3. Calculate the gain as (number of 0s - number of 1s) for that interval. The maximum gain possible.
4. The answer is original_ones + max_gain.

But how to efficiently calculate the number of 0s and 1s for all intervals?

We can precompute a prefix sum array for the number of 1s. Then for any interval [i,j], the number of 1s is prefix[j] - prefix[i-1], and the number of 0s is (j - i + 1) - (prefix[j] - prefix[i-1]). So the gain for the interval is [ (0s - 1s) ] = ( ( (j - i + 1) - ones ) - ones ) = (j - i +1 - 2*ones ). Which simplifies to ( (j -i +1) - 2*ones ) where ones is the count of 1s in the interval.

Alternatively, the gain can be calculated as (number of 0s - number of 1s) = ( (j -i +1 - ones) - ones ) = (j -i +1 - 2*ones).

So for each interval [i,j], compute the ones in that interval (using prefix sum), then compute the gain. Then track the maximum gain.

Once we have the maximum gain, the answer is original_ones + max_gain. But wait, what if the maximum gain is negative? Then flipping that interval would decrease the total. But the problem requires exactly one flip. So even if all possible intervals have a negative gain, we have to choose the one with the least loss. Because we have to flip exactly once.

So the maximum gain could be negative, but we have to add it to the original ones. For example, if all elements are 1. Then flipping any interval would reduce the total. But the problem requires exactly one flip, so the answer would be (original_ones - (j-i+1 - 0s)), but since all are 1s, 0s is zero. So flipping any interval of length k gives a gain of (0 - k) = -k. So the maximum gain is -1 (smallest possible loss). So the answer would be original_ones -1.

But in the problem statement's examples, sometimes flipping gives a positive gain. So the approach of finding the maximum possible gain (could be positive, zero, or negative) and adding to original_ones is correct.

So steps:

1. Compute original_ones = sum(array)
2. Compute prefix sum array of the array. Let prefix[0] = 0, prefix[1] = a[0], etc. (depends on 0-based or 1-based indexing)
3. For each possible i and j (i <= j), compute the number of 1s in [i..j] (using prefix[j+1] - prefix[i], assuming 0-based prefix)
4. The gain for this interval is ( (j -i +1) - 2 * ones_in_interval )
5. Track the maximum gain over all intervals.
6. The answer is original_ones + max_gain.

Yes, this should work.

Now, considering the array indices. Let's say the array is 0-based. The prefix sum array could be of size n+1, where prefix[0] =0, prefix[1] = a[0], prefix[2] = a[0]+a[1], etc. Then the sum from i to j (0-based) is prefix[j+1] - prefix[i].

So for each interval starting at i (0-based) and ending at j (0-based, i <= j), the number of 1s is prefix[j+1] - prefix[i].

The length of the interval is j -i +1.

So the gain is ( (j-i+1) - 2*(prefix[j+1] - prefix[i]) )

So the code can proceed as follows:

- Read n, read the array as a list of integers.
- Compute original_ones = sum(arr)
- Compute the prefix array.
- Initialize max_gain to -infinity.
- Iterate over all possible i from 0 to n-1:
   for each i, iterate j from i to n-1:
      ones = prefix[j+1] - prefix[i]
      gain = (j -i +1) - 2*ones
      if gain > max_gain:
          max_gain = gain
- The answer is original_ones + max_gain.

But wait, what if all possible intervals give a negative gain? Then adding that max_gain (which is the least negative) is the best possible.

Yes.

Now, let's test this approach against the examples.

First example:

Input array: 1 0 0 1 0

Original_ones = 1 + 0 + 0 +1 +0 = 2? Wait, wait. Wait the input is 1,0,0,1,0. So sum is 1+0+0+1+0 = 2. So original_ones is 2.

Now, the optimal flip is from index 2 to 5 (assuming 1-based indices, but in the code, the array is 0-based). Let's see.

In the code, the code would check all intervals. Let's see for the interval i=1 to j=4 (0-based). Because in the array, indexes 0 to 4. So the interval [1,4] (0-based) is elements 0,1,0 (positions 1,2,3,4? Wait wait, i=1, j=4 (0-based) is the elements from index 1 to 4, which are 0,0,1,0. So flipping those would turn 0s into 1s and 1s into 0. So the original elements are 0,0,1,0. Flipping gives 1,1,0,1. So in the original array, the elements after flipping would be:

Original array: [1,0,0,1,0]

After flipping i=1 to j=4 (0-based, so elements indexes 1,2,3,4): the elements become 1,1,1,0,1. Sum is 4. Which is original_ones (2) + (0s in interval - 1s in interval).

The interval has elements 0,0,1,0. So 0s: 3, 1s:1. So gain is 3-1=2. So 2+2=4. Which matches.

In the code, for this interval i=1, j=4 (0-based). The ones_in_interval is the sum of those elements: 0+0+1+0=1. So gain is (4 - 2*1) = 4-2=2. So original_ones (2) +2=4.

So that's correct.

Second example:

Input array: 1 0 0 1

Original_ones: 1+1=2. Wait 1,0,0,1. Sum is 1+0+0+1=2. Flipping the interval from index 1 to 2 (0-based) which are 0 and 0. Flipping gives 1 and 1. So the array becomes 1,1,1,1. Sum is 4. So gain is 2.

The code would compute for i=1, j=2. The length is 2. ones_in_interval is 0+0=0. gain is 2 - 2*0 =2. original_ones (2) +2=4. Correct.

So the code works for these cases.

Another test case: all 1s. Suppose n=3, array is [1,1,1]. Original_ones=3.

Flipping any interval. Let's say i=0, j=0 (flip first element). The gain is (1 - 2*1) = -1. The best gain is -1. So answer is 3 + (-1) = 2. Which is correct.

So the code would handle that.

So the approach seems solid.

Now, the code implementation in Python.

Read n, then the array. Compute prefix sums.

Implement the prefix sum as a list where prefix[0] is 0, prefix[1] is a[0], prefix[2] is a[0]+a[1], etc.

Then for each i in 0..n-1, j in i..n-1.

Compute the ones in [i, j] as prefix[j+1] - prefix[i].

Compute gain as (j -i +1) - 2 * ones.

Track the maximum gain.

Finally, answer is original_ones + max_gain.

This should work.

Now, code.

But wait, how to read the array? The input is given as a second line of n integers. So:

n = int(input())
arr = list(map(int, input().split()))
assert len(arr) == n

Then compute the prefix sum.

prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

Then compute max_gain.

max_gain = float('-inf')

for i in range(n):
    for j in range(i, n):
        ones = prefix[j+1] - prefix[i]
        length = j -i +1
        gain = length - 2*ones
        if gain > max_gain:
            max_gain = gain

ans = sum(arr) + max_gain

print(ans)

Yes. That's the code.

Testing the first example:

Input:

5

1 0 0 1 0

sum(arr) is 1+0+0+1+0=2.

max_gain is 2 (from the interval [1,4]).

In code, the code loops i from 0 to 4.

For i=1, j=4:

prefix[5] - prefix[1] = (1+0+0+1+0) - (1) → 2-1=1? Wait, wait, let's compute the prefix array for this input.

The array is [1,0,0,1,0].

prefix[0] =0.

prefix[1] =1.

prefix[2] =1+0=1.

prefix[3] =1+0=1.

prefix[4] =1+0+0+1=2.

prefix[5] =2+0=2.

So for i=1, j=4:

prefix[5] - prefix[1] = 2 -1=1.

Which is the sum of the elements from index 1 to 4 (0,0,1,0), sum is 1. So the ones_in_interval is 1.

gain = (4) (since j-i+1 is 4 (j=4, i=1 → 4-1+1=4) → 4 - 2*1 =2. So gain is 2. Which is correct.

So the code would correctly capture that.

Another example:

n=4, array [1,0,0,1]

sum is 2.

i=1, j=2 (0-based). The interval is [0,0]. ones_in_interval is 0+0=0. So gain is (2) - 2*0=2. So sum + gain=4.

Which matches the example.

So the code works.

Now, considering all possible cases. Edge cases like n=1. For example, input n=1 and array [0]. Then flipping it would turn to 1. So gain is 1 (0->1: 1-0=1). So answer is 1. Code would compute sum(arr) is 0, max_gain is 1, so 0+1=1.

Another edge case: n=1, array [1]. Then flipping is mandatory. So the gain is -1. So answer is 1-1=0.

Yes.

So the code is correct.
</think>

```python
n = int(input())
arr = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]
max_gain = float('-inf')
for i in range(n):
    for j in range(i, n):
        ones = prefix[j+1] - prefix[i]
        gain = (j - i + 1) - 2 * ones
        if gain > max_gain:
            max_gain = gain
print(sum(arr) + max_gain)
```