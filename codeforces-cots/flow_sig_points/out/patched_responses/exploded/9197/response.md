<think>
Okay, let's tackle this problem. So, we need to find the number of ways to split the array into three contiguous parts where each part has the same sum. Hmm. Let me think about how to approach this.

First, the sum of the entire array must be divisible by 3. Otherwise, it's impossible, right? So the first step is to check if the total sum is a multiple of 3. If not, the answer is 0.

Wait, but even if it is divisible by 3, we need to find the correct splits. Let's say the total sum is 3S. Then each part must sum to S. So the first part is from the start up to i-1, the second from i to j, and the third from j+1 to end. All three should sum to S.

So, maybe the approach is to first compute the total sum. If it's not divisible by 3, return 0. Otherwise, S is total / 3.

But how to find the valid i and j pairs?

Let me think about the conditions. The first part's sum is the sum up to i-1. The second part is from i to j. The third part is from j+1 to the end. All these sums must be equal to S.

Alternatively, the sum of the first part is S, the sum of the first two parts is 2S, and the total is 3S.

Wait, maybe we can compute prefix sums. Let's compute the prefix sum array. The prefix sum up to index k is sum[0..k] (assuming 0-based here). Then, for the first part to be S, we need the prefix sum at i-1 (assuming 1-based array) to be S. Then, the sum from i to j must be S, which implies the prefix sum at j is 2S. Then, the remaining sum (from j+1 to n) must be S.

So, the problem reduces to finding all pairs (i, j) where the prefix sum at i-1 is S, the prefix sum at j is 2S, and i <= j < n.

Wait, because j has to be at least i (since the second part is from i to j), and j has to be less than n (since the third part must have at least one element). So j can be up to n-1 (assuming 0-based or 1-based indices? Let's clarify.)

Let me think in terms of 1-based indices. The array has elements from a[1] to a[n]. The split is into:

- part1: 1..i-1
- part2: i..j
- part3: j+1..n

Each part's sum is S. So sum(1..i-1) = S, sum(i..j) = S, sum(j+1..n) = S. The total sum is 3S.

So the prefix sum up to i-1 is S. The prefix sum up to j is 2S (since sum 1..j = sum 1..i-1 + sum i..j = S + S = 2S). Then the sum j+1..n is S, which is the same as the total sum (3S) minus prefix[j] (which is 2S) = S.

So the conditions are:

1. The total sum must be divisible by 3.
2. We need to find all pairs (i, j) where:
   a. prefix[i-1] = S
   b. prefix[j] = 2S
   c. i <= j (so that part2 is non-empty)
   d. j < n (so that part3 is non-empty)

But how to efficiently count these pairs?

The key is that for each j where prefix[j] is 2S, we can count the number of i's where i-1 < j and prefix[i-1] = S. Wait, but i must be <= j. So i-1 can be up to j-1. Wait, i can be from 2 to j (since i-1 must be at least 1, so i >=2), and j must be at least i, so j can be from i to n-1. Hmm, perhaps not. Let me re-express:

Each j where prefix[j] = 2S can potentially form valid pairs with i's such that i-1 <= j-1 (i.e., i <= j) and prefix[i-1] = S. So for each j where prefix[j] = 2S, the number of valid i's is the number of times S appears in the prefix sum array before j (i.e., in positions 1 to j-1). Because i-1 must be at least 1 (since i >=2), but j can be up to n-1 (since j+1 <=n implies j <=n-1).

Wait, but i can be as small as 2 (so i-1=1), and j can be as big as n-1 (since j+1 is n). So the j's that are valid are those where prefix[j] is 2S and j <n. Because j has to be less than n for the third part to exist.

So the plan is:

1. Compute the total sum. If not divisible by 3, return 0.
2. Compute S = total_sum /3.
3. Compute the prefix sum array.
4. For each j where j <n and prefix[j] = 2S, count the number of i's where prefix[i-1] = S and i-1 <j (since i-1 can be up to j-1). So for each such j, add the count of S in prefix sum array up to index j-1.

So the steps are:

- Precompute all the positions where prefix sum is S (call these positions candidates for i-1).
- Then, iterate through each j where j <n and prefix[j] = 2S, and add the count of S's in the prefix sum array up to j-1.

But how to efficiently compute the count of S's up to j-1?

We can create a frequency dictionary that keeps track of the number of times each prefix sum has occurred up to each index. For example, as we compute the prefix sums, we can keep a hash map that maps the sum value to the list of indices where it occurred. Then, for each j, we can look up how many times S has appeared in the prefix sums before j (i.e., up to j-1).

But considering the constraints (n up to 5e5), we need an O(n) solution.

So here's the approach:

- Compute the total sum. If not divisible by 3, return 0. Else S = sum/3.
- Compute the prefix sum array as we iterate through the array.
- As we iterate, we track the number of times S has been seen in the prefix sums up to the current index (but not including the current index, since for j, we need counts up to j-1).
- Also, for each index j where prefix[j] is 2S and j <n, we add the count of S occurrences up to j-1.

Wait, here's a possible way:

We can iterate through the array once, keeping track of the current prefix sum. We also maintain a counter that tracks how many times the prefix sum equals S. For each position j (from 1 to n), if j is not the last element (since j+1 must exist) and the current prefix sum is 2S, then we can add the number of times S has occurred in the prefix sums up to j-1. Because those are the possible i-1 positions.

Wait, let's see. Let's process each element step by step:

Initialize prefix_sum =0, count_s=0, result=0.

For each index in 0..n-1 (assuming 0-based array):

   prefix_sum += a[index]

   if index == n-1: break (since j can't be n-1, because j+1 would be n, which is beyond the array? Wait, no. The original problem states j can be up to n-1, because the third part is from j+1 to n. So j can be n-1, but then j+1 is n, which is the end of the array. So for j =n-1, the third part is from n to n (since j+1 is n). So for example, if the array is 3 elements, j can be 1 (assuming 0-based), then third part is index 2.

Wait, perhaps the 1-based vs 0-based confusion is causing issues here. Let's re-express in 1-based indices.

In the problem statement, the array is 1-based. So j can be up to n-1. Because j+1 must be <=n. So j's maximum value is n-1.

So in 1-based terms, j ranges from 2 to n-1 (since i has to be <=j, and i must be >=2, as per 2 ≤ i ≤ j ≤ n-1).

But perhaps the approach is better handled with 0-based arrays.

Let me think in 0-based indices.

The array is 0-based: a[0] to a[n-1]. The split is into three parts:

- part1: from 0 to i-1 (inclusive)
- part2: from i to j (inclusive)
- part3: from j+1 to n-1 (inclusive)

Each part must have sum S.

So total sum is 3S.

Then the prefix sum up to i-1 must be S, prefix sum up to j must be 2S, and the sum from j+1 to end must be S.

So for each j in 0..n-2 (because j+1 must be <=n-1), if prefix[j] is 2S, then the number of i's is the number of times S has occurred in the prefix sum array up to j-1 (since i-1 can be from 0 up to j-1, and part1 is 0..i-1, part2 is i..j. So i can be from 0+1=1 to j's index. So i-1 ranges up to j-1).

Wait, perhaps not. Let me re-express:

For part1 sum to be S: sum(0..i-1) = S.

i can range from 1 to j (since part2 is i..j). So i-1 can be 0 to j-1.

But j must be >= i, so j can be from i to n-2 (since part3 is j+1 to n-1, which requires j+1 <=n-1 => j <=n-2).

So, the steps:

Compute the total sum. If not divisible by 3, return 0.

Compute S = sum /3.

Compute the prefix sum array.

Then, for each j from 0 to n-2:

   if prefix[j] == 2S, then the number of valid i's is the number of times S appeared in prefix[0..j-1].

So the approach is:

We can traverse the array once, keeping track of the count of S in the prefix sum as we go. For each j, when we check if prefix[j] is 2S, we add the count of S that we've accumulated up to j-1.

But how to track the count of S up to j-1 as we process each j?

Because as we process each element, for j, we need the count of S in the prefix sums up to j-1.

So for example, when processing j=2, the count of S up to j-1 (j=1) is the number of times S has been seen in prefix[0] and prefix[1].

So here's the plan:

Initialize variables:

- total = sum of array.

if total %3 !=0: return 0.

S = total//3.

Then:

current_sum =0

count =0

result=0

We need to track the number of times the prefix sum equals S. For each j, after adding the current element to current_sum, we check if j is <=n-2 (since j can be up to n-2) and if current_sum is 2S. If so, then we add the count of S occurrences up to j-1.

But the problem is that when processing j, the current_sum is the prefix sum up to j. So for j to be in 0..n-2, and when current_sum is 2S, we need to add the count of S occurrences up to j-1 (since the prefix sum up to j-1 is the sum before adding a[j]).

Wait, no. Because current_sum after processing j is prefix[j], which is sum up to j. So when processing j, to check if prefix[j] is 2S, then we need to add the number of times S has appeared in the prefix sums up to j-1.

But how to track that? Because when we are at j, the count variable may include the current j's sum if it's equal to S. But we need to exclude j for the case where current_sum is 2S.

Wait, let's think step by step.

For each element in the array, we process them in order. For each index j (0-based), after adding a[j] to current_sum, which is the prefix sum up to j.

Then, if j is not the last element (since j can be up to n-2), and current_sum is 2S, then the number of valid i's is the number of times S has been seen in the prefix sums up to j-1. Because i-1 can be from 0 to j-1.

But how do we track the count of S up to j-1?

If we update the count before checking for 2S, then the count includes S in prefix[j]. But we need the count up to j-1.

Wait, perhaps we can track the count as follows:

We process the elements in order, keeping track of current_sum.

At each step j (0-based), after adding a[j] to current_sum, we first check if j is not the last element (i.e., j <n-1). If current_sum is 2S, then the number of valid i's is the number of times S has been seen in the prefix sum up to j-1. Then, we check if current_sum (after adding a[j]) is equal to S, and if so, increment the count. Because for the next j+1, when we check, the count will include S up to j.

Wait, maybe the correct order is:

For each j from 0 to n-1:

   current_sum += a[j]

   if j <n-1 and current_sum == 2S:

       result += count

   if current_sum == S:

       count +=1

So this way, for j=0 to n-2:

   after adding a[j], if current_sum is 2S, then the count includes the number of times S has been seen up to j-1. Because when we check for current_sum == 2S, the count hasn't been updated yet for the current j's sum. Wait, no.

Wait, when j is processed, current_sum is sum up to j. Then, if current_sum is 2S and j is not the last element, we add the count of S. But the count variable is tracking the number of times S has been seen in the prefix sums up to j-1. Because the count is incremented after checking for 2S.

Wait, here's the flow:

At step j (0-based):

1. Add a[j] to current_sum. So current_sum is sum[0..j].

2. Check if j is not the last element (j <n-1). If current_sum is 2S, then add the count (number of S occurrences up to j-1) to result.

3. Check if current_sum is S. If yes, increment count.

Because step 3 is after step 2, the count for j's current_sum (S) is added to the count for the next j's steps.

So for example:

- For j=0:

   current_sum is a[0]. 

   if a[0] is 2S and j <n-1, then add count (0, since count hasn't been incremented yet) to result.

   if a[0] is S, increment count to 1.

Then j=1:

   current_sum +=a[1]. Now sum is sum[0..1].

   if sum is 2S and j <n-1: then add count (which is the number of S in sum[0..0], which is the previous count). 

   then check if sum is S: if yes, increment count.

So in this way, when we process j, the count variable contains the number of times S has occurred in the prefix sums up to j-1. Because the count is only updated after checking for 2S.

Yes, this seems correct.

So, for each j, when we check if current_sum is 2S (and j is not the last element), the count variable holds the number of times S has occurred in the prefix sums up to j-1. Because the count is incremented after processing j's sum.

For example, for j=2:

current_sum is sum[0..2]. Check if it's 2S. If yes, add the count (number of times S occurred in sum[0..1]). Then, check if sum[0..2] is S: if yes, count increases by 1.

So the logic is correct.

Therefore, the code can be written as:

sum_total = sum of array.

if sum_total %3 !=0: return 0.

s = sum_total //3

current_sum =0

count=0

result=0

for j in 0 to n-1:

    current_sum += a[j]

    if j <n-1:

        if current_sum == 2*s:

            result += count

    if current_sum == s:

        count +=1

return result

But wait, let's test this with the first example.

First example input:

5

1 2 3 0 3

sum is 1+2+3+0+3=9. 9/3=3. So s=3.

The array in 0-based:

indexes 0:1, 1:2, 2:3, 3:0, 4:3.

Processing each j:

j=0: current_sum=1.

Check j <4 (yes). current_sum is 1, not 6 (2*3=6). So no addition.

Check if sum is 3: no. count remains 0.

j=1: current_sum=1+2=3.

Check j<4 (yes). sum is 3, not 6. So no addition.

sum is 3: yes. count becomes 1.

j=2: current_sum=3+3=6.

Check j=2 <4. sum is 6 (2*3). So add count (1) to result. result becomes 1.

sum is 6 !=3. count remains 1.

j=3: current_sum=6+0=6.

Check j=3 <4. sum is 6 again. add count (1) to result. result is 2.

sum is 6 !=3. count remains 1.

j=4: sum +=3 =9. j=4 is not less than 4 (since n-1 is 4). So no check.

sum is 9, which is not s=3. So no change to count.

So the total result is 2, which matches the example.

Yes, this works.

Another example:

Input 4

0 1 -1 0

sum is 0. 0/3=0. So s=0.

array: 0,1,-1,0.

0-based:

j=0: sum=0.

j <3 (yes). sum=0. 2*s is 0. So check if sum is 0, which is 0, so add count (0) to result. result=0.

Then, check if sum is s=0: yes. count becomes 1.

j=1: sum +=1 =1.

j <3: sum=1. 2*s=0. no.

sum is 1 !=0. count remains 1.

j=2: sum +=-1=0.

j<3. sum=0 == 0 (2*s). add count (1) to result. result=1.

sum is 0 ==0: count becomes 2.

j=3: sum +=0=0. j=3 is not <3. So no addition.

sum is 0 ==0: count becomes3.

result is 1. Which matches the example.

So the code works here.

Third example:

input 2, 4 1. sum is5. 5 not divisible by3. return 0.

Which is correct.

So the code seems to handle all the examples correctly.

Now, considering the constraints:

n can be up to 5e5. The code does a single pass through the array, with O(n) time. Space is O(1), as we are not storing the prefix sum array, just the current sum. So this is optimal.

Thus, this approach is correct and efficient.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

total = sum(a)
if total % 3 != 0:
    print(0)
else:
    s = total // 3
    current_sum = 0
    count = 0
    result = 0
    for j in range(n):
        current_sum += a[j]
        if j < n - 1:
            if current_sum == 2 * s:
                result += count
        if current_sum == s:
            count += 1
    print(result)
```