<think>
Okay, I need to solve this problem where I have to find the number of contiguous subarrays in a given array whose sum is a power of k. Let's think about how to approach this.

First, the problem states that a valid segment's sum must be a non-negative power of k. So possible sums are k^0, k^1, k^2, etc. But wait, k can be negative. Oh right, the note mentions that k^0 is 1, regardless of k. So for example, if k is -3, then possible exponents are like (-3)^0=1, (-3)^1=-3, (-3)^2=9, etc. But wait, what if k is 1 or -1? Then there might be multiple exponents leading to the same value. Hmm, but the problem says non-negative exponents, so exponents are 0,1,2,...

So the first step is to generate all possible target sums that are powers of k. Then, for each possible target, find the number of subarrays whose sum equals that target.

But how do I efficiently compute this? Because for each possible target, checking all possible subarrays would be O(n^2), which is too slow for n=1e5.

The standard approach for counting subarrays with a specific sum is to use a prefix sum array and a hash map to track the counts of prefix sums. For example, for a target sum T, we can iterate through the prefix sums and for each current prefix sum s, check how many times (s - T) has occurred before. That's the idea from the two-sum problem.

But here, the targets are all the possible k^m values. So first, we need to generate all possible k^m values that could be achievable as the sum of some subarray. However, the sum can be as large as the sum of all elements (which could be up to 1e5 * 1e9 = 1e14) or as low as negative numbers. So generating all possible powers up to that sum is necessary.

But this could be a problem because if k is 1, then 1^m is always 1. So the number of possible targets is 1. Similarly, if k is -1, then the possible targets alternate between -1 and 1, but for exponents 0,1,2, etc. So if the sum can be large in magnitude, but for k=1 or -1, how do we handle that?

Wait, but the sum can be any possible value. So if k is 1, then the target sum must be 1. So we need to count all subarrays whose sum is 1. Similarly, if k is -1, then the targets are 1, -1, 1, -1, etc. But when the exponent is even, it's 1, when odd, it's -1. But since the exponents can be up to any value, but the sum can be as big as 1e14, but for k=-1, the possible targets are only 1 and -1. So for each of those, we can check.

So the plan is:

1. Generate all possible target sums that are k^m for m >=0. But need to handle cases where k is 0? Wait, the input says |k| >=1. Because the constraints say 1 ≤ |k| ≤10. Wait no, the input can have k=0? No, because the constraints say 1 ≤ |k| ≤10. So k is between -10 and 10, excluding 0. So k can be -10 to 10, but not zero.

So k can't be zero. So the possible exponents are for m >=0.

So the first step is to generate all possible target sums that are k^m, where m is a non-negative integer (0,1,2,...), and that could be a possible sum of a subarray.

But how do we generate all such possible targets, considering that the sum can be up to 1e14 in magnitude (but even that may be manageable for exponents)?

Let's think about the possible exponents:

For example, if k is 2, then the possible exponents start at 1, 2,4,8, etc. The maximum possible sum is 1e14. So the maximum m would be up to log2(1e14) which is around 46. So even for k=2, the number of possible targets is manageable.

But if k is 10, then 10^14 is 1e14, so exponents up to 14 would suffice.

But for k=1, the exponent can be 0 (k^0=1), but for m=1, it's 1 again. So for k=1, the only possible target is 1. Similarly, for k=-1, the possible targets are 1 and -1 alternately for each exponent.

Wait, but the exponents are non-negative. So for k=-1, m can be 0 (1), m=1 (-1), m=2 (1), etc. So the possible targets are 1 and -1. But since exponents can be up to any number, but the same values repeat. So for k=-1, the possible targets are 1 and -1. So when generating the targets, for k=-1, we can collect 1 and -1. But need to be careful because 1 can appear infinitely, but we can just collect each possible value once.

Wait, but the sum can be any of these. So for example, if a subarray sum is 1, then it can be either k^0 (if k is -1) or k^2 (since (-1)^2 is 1), etc. But the problem counts the sum as valid if it is any of the exponents, not just the minimal m. So for example, if the sum is 1, then any m where k^m =1 is allowed, which for k=-1 includes m=0,2,4,... So the sum 1 is valid. So for k=-1, the target sums are 1 and -1.

But when generating the possible targets, for a given k, we need to generate all possible k^m that could be a possible sum. However, for some k, like k=-1, the same value can be achieved with different m's. So in such cases, we can just collect unique values of k^m. Because if a sum S equals k^m for any m >=0, then S is valid. So even if the same S is achieved by multiple m's, we just need to count the sum once.

Thus, the first step is to generate all possible unique values of k^m for m >=0, but up to a certain maximum m where |k^m| is not exceeding the possible maximum sum (or minimum sum, since sums can be negative).

But how do we determine when to stop generating exponents?

For example, suppose k is 2. The maximum possible sum is up to 1e5 * 1e9 = 1e14. The largest exponent m where 2^m <= 1e14 is m=46 (since 2^46 is around 7e13, 2^47 is 1.4e14). So we can generate all exponents until k^m exceeds the possible maximum sum.

But the sum can also be negative. So for example, if k is negative and m is even, then k^m is positive, but m odd gives negative. So when generating the targets, we need to generate all possible exponents until the absolute value of k^m is beyond the possible sum's absolute value.

But how do we compute the possible sum's maximum and minimum?

The sum of a subarray can range from the sum of all negative elements (if the array is all negatives) to the sum of all positive elements. But given that individual elements can be up to 1e9 in magnitude, the maximum possible sum (absolute value) is 1e14 (1e5 * 1e9). So for any k, we can generate all possible exponents until |k^m| exceeds this maximum possible sum.

So for each k, generate all possible k^m where m is >=0 and |k^m| <= 1e14. But also, we have to avoid infinite loops when k is 1 or -1.

Wait, for example, when k=1, then 1^m is 1 for all m. So after m=0, we get 1 again. So we can stop generating once we get the same value again. Similarly, k=-1: (-1)^0=1, (-1)^1=-1, (-1)^2=1, etc. So the same values cycle. So for k=1, the only possible targets are 1. For k=-1, possible targets are 1 and -1.

So the approach for generating the targets is:

- Generate all possible k^m, m >=0, until |k^m| exceeds the maximum possible sum (1e14), or until we start repeating values (for k=1 or -1).

So, the steps are:

1. Generate all possible target values (unique) that are equal to k^m for some m >=0.

2. For each target value in this list, compute the number of subarrays whose sum equals this target.

3. Sum all these counts to get the total answer.

But how to compute the sum for each target efficiently?

For each target T, we can compute the number of subarrays with sum T using the prefix sum method. We can do this by maintaining a hash map (like a dictionary) that counts the occurrences of each prefix sum. For each current prefix sum s, the number of previous prefix sums equal to (s - T) is added to the count.

So the overall approach is:

- Compute the prefix sums array.

- For each target T in the generated list:

   - Reset the hash map (or use a cumulative approach)

   - Iterate through the prefix sums and count how many times (current prefix sum - T) has been seen before.

But the problem is that for each target T, this process would take O(n) time, which for multiple targets could be O(n * number_of_targets). For n=1e5 and number_of_targets=60 (like for k=2), this would be 6e6 operations, which is manageable. But for cases like k=1 (only one target), it's O(n). For k=-1 (two targets), it's 2*O(n). So overall, this approach is feasible.

But how to manage the prefix sums and the hash map efficiently.

Wait, but the prefix sum array is the same for all targets. So the main idea is that for each target T, we can compute the count using the same prefix sums. So perhaps we can precompute all the prefix sums once, and then for each target T, process them in a single pass through the prefix sums, tracking the counts.

But the way the hash map works for each target is independent. So for each T, we need to process the prefix sums again, keeping track of how many times each (current sum - T) has been seen.

But if the number of targets is small, say up to 60, then for each T, doing a pass through the prefix sums (1e5 elements) would take 6e6 operations, which is acceptable for the time constraints (2.5 seconds).

But for each target T, we need to process the prefix sum array once. Let's see:

The standard way to compute the count of subarrays with sum T is:

Initialize a hash map (dictionary) called count_map, which starts with {0:1} (since a prefix sum of 0 occurs once before starting).

current_sum = 0

result = 0

for num in array:

    current_sum += num

    if (current_sum - T) in count_map:

        result += count_map[current_sum - T]

    if current_sum in count_map:

        count_map[current_sum] +=1

    else:

        count_map[current_sum] =1

So for each T, we can process the array in O(n) time.

But doing this for each T would be O(n * m), where m is the number of targets. So for m=60, n=1e5, this is 6e6 operations. That's acceptable.

But how to generate the targets?

So let's think about generating the targets:

For k=1, the possible targets are 1, 1, 1, etc. So after m=0 (1), m=1 (1), so we can generate it once and stop.

Similarly, for k=-1: (-1)^0=1, (-1)^1=-1, (-1)^2=1, etc. So after m=0 and m=1, the values start repeating. So the unique targets are 1 and -1.

For other k:

For example, k=2: generate 1, 2,4,8,... until the value exceeds 1e14 (sum's max possible).

For k=3: 1,3,9,27, etc.

For k=-2: 1, -2,4,-8,16, etc. until the absolute value exceeds 1e14.

So the code for generating the targets can be as follows:

Initialize a set to store the targets.

Initialize current = 1 (k^0) and add to the set.

Then, multiply by k each step and add to the set, as long as the absolute value of the current is <= 1e14 (since the sum can't exceed 1e14 in absolute value). Also, we need to check if adding the next exponent would result in a new value or a repeated one. For example, if k=1, after the first step, the next step would also be 1. So once we see that the next value is already in the set, we break.

So the code for generating the targets:

targets = set()

current = 1

targets.add(current)

while True:

    next_val = current * k

    if abs(next_val) > 1e14:

        break

    if next_val in targets:

        break

    targets.add(next_val)

    current = next_val

Wait, but this may not capture all possible exponents. For example, in the case of k=-1:

After current is 1, next_val is -1. Then next next_val is 1. So next_val is already in the targets, so the loop breaks. So targets are 1 and -1. Which is correct.

Another example: k=2:

current starts at 1 (m=0), next is 2 (m=1), then 4 (m=2), etc. until it's larger than 1e14.

So this logic should generate all possible unique exponents up to the maximum possible sum.

But wait, what if the sum can be up to 1e14 in absolute value? For example, for k=2, the code would generate exponents until 2^m exceeds 1e14. But 2^46 is about 7e13, 2^47 is 1.4e14. So the loop would stop when next_val is 1.4e14, which is larger than 1e14. So the maximum m is 46 (so exponents 0 to 46, 47 terms). But wait, when current is 1, next_val is 2 (m=1). Then current becomes 2, next_val is 4 (m=2), etc. The loop stops when next_val's absolute value exceeds 1e14. So the code adds next_val as long as it's within the limit.

Wait no. Let's see:

The initial current is 1 (m=0). The code adds 1 to targets.

Then compute next_val = 1 * k. For k=2, next_val is 2 (m=1). Then check if abs(2) <=1e14? Yes. Then check if 2 is in targets. No. So add 2 to targets. Current becomes 2.

Next iteration: next_val = 2 * 2 =4. Check if 4 is <=1e14? Yes. Add to set. Current becomes 4.

This continues until next_val exceeds 1e14. For example, when current is 2^46 (which is 7e13), next_val is 2^47 (1.4e14) which is larger than 1e14. So the loop breaks. So the maximum exponent included is m=46 (current is 2^46, but next_val is 2^47 which is over the limit). So the code would generate all exponents from m=0 to m=46. So 47 elements for k=2.

But how about when k is 3 and m=3, etc.?

This logic seems correct. So the code for generating targets is:

Compute all possible k^m for m>=0, such that |k^m| <= 1e14. But once a generated value is already in the set, we break (for cases like k=1 or -1).

But wait, the condition is to check if next_val is already in the set, which would break the loop. For example, for k=1, after adding 1, next_val is 1, which is already in the set, so the loop breaks. For k=-1, after adding 1 and -1, then next_val would be 1 again (since -1 * -1 is 1). So the loop adds -1, then tries to compute next_val = -1 * (-1) =1, which is already in the set, so the loop breaks. So the targets are 1 and -1.

So this code correctly generates all possible unique targets.

Once we have the set of targets, we need to compute for each target T, the number of subarrays with sum T.

But the problem is that the array elements can be negative, so the prefix sums can decrease and increase. So the standard approach is needed.

But how to compute the counts for all targets efficiently?

The naive approach would be for each target T in the set:

   Initialize a count_map with {0: 1}

   current_sum = 0

   count = 0

   for num in array:

       current_sum += num

       if (current_sum - T) in count_map:

           count += count_map[current_sum - T]

       if current_sum in count_map:

           count_map[current_sum] +=1

       else:

           count_map[current_sum] =1

   add count to the total.

But if the number of targets is up to 60, then this would be O(n * 60) time, which is acceptable for n=1e5 (6e6 operations). But for n=1e5, and 60 targets, 6e6 is manageable.

But for Python, using a dictionary for each target may be slow. So perhaps, precompute all the prefix sums first, and then for each target, process them with the same logic.

But in Python, even 1e6 operations are manageable in 0.1 seconds. So 6e6 would take 0.6 seconds, which is acceptable.

But let's check with the sample input.

Sample 1:

n=4, k=2, array is [2,2,2,2]

Possible targets: 1, 2,4,8,16, etc. But generated up to 8 (since sum can be up to 8). So targets are 1,2,4,8,16, etc. But wait, the code will generate 1 (k^0), then 2 (k^1), 4 (k^2), 8 (k^3), 16 (k^4=16), etc. until 16 is 16 <= 1e14. But in the sample, the sum of the entire array is 8. So for the code, the targets would include 1,2,4,8,16, etc. But when processing the array, the actual sums can be 2,4,6,8. So for target 1, there are no subarrays. For target 2, there are 4 subarrays. For target4, 3, etc. So the code will process all the targets, but for those that are not present in the possible sums, the count would be zero.

But wait, in the sample, the answer is 8. The valid targets are 2,4,8.

The code would generate all targets up to 1e14. For example, 1,2,4,8,16,32,... etc. But when checking the sum of subarrays, the code for each target would count how many times (current_sum - T) is in the map.

But in the sample, the code for target 2 would find 4 subarrays (each single element), for target4, 3 subarrays (each pair), for target8, 1 subarray (the entire array). But in the sample, the code's output is 4+3+1=8. Wait, but the sample says that 2,4,8 are the valid targets. So the code would process all possible targets, including 1, which isn't achieved. So the code would loop through all targets, but for those that are not present in any subarray sum, their count is zero, so they don't contribute.

But how do we handle cases where the same sum is a power of k in multiple ways? For example, if sum is 4, and k=2, then 4 is 2^2. But for k=-2, sum 4 could be (-2)^2, etc. But the code would generate the target 4 once, and count all subarrays that sum to 4, regardless of how they are expressed as a power.

But the problem says that the sum must be equal to any non-negative power of k. So the code is correct in generating all possible k^m and check if the sum equals any of them.

Thus, the approach is:

Generate all possible targets (unique) that are k^m for some m >=0, up to the maximum possible sum (1e14 in absolute value).

For each target T in this set, compute the number of subarrays whose sum is T, using the prefix sum and hash map approach.

Sum all these counts to get the answer.

Now, the code in Python:

But there's a possible issue with the order of processing the targets and handling the same sum for different T. However, the problem counts a subarray once for each T it matches. Wait, no. The problem counts each valid subarray once, regardless of how many times it matches a target. Wait, the problem says "a contiguous segment of chemicals [...] with total [...] as a non-negative integer power of k". So the sum must be a power of k. So for a sum S, if S is a power of k (i.e., S is in the generated targets set), then the subarray is valid. So each subarray that has a sum in the targets set is counted once.

Therefore, the code's approach of generating all possible targets and summing their counts is correct.

But wait, no. Because for example, if a sum S is a power of k in multiple ways (like for k=-1, sum 1 can be achieved as (-1)^0, (-1)^2, etc.), but the code's generated targets set would have 1 once. So the code counts each subarray once if S is in the targets set, regardless of how many exponents m generate S.

Thus, the code's approach is correct.

So now, code steps:

Read n and k.

Read the array a.

Generate the targets set.

Compute the total count by processing each target T in the targets set.

So the code:

But first, generate the targets. For example, if k is 2, the targets are 1, 2,4,8,... up to 1e14.

But for the code, the initial current is 1 (k^0). Then multiply by k each time. So for k=2:

current starts at 1.

next_val is 2. Add to set.

current becomes 2. next_val is 4. Add.

And so on.

Now, handling k=1 and k=-1 correctly.

Now, code in Python:

Read n, k.

a = list of integers.

Generate targets:

targets = set()

current = 1

targets.add(current)

max_abs_sum = 1e14  # Or 10**14 ?

But wait, the maximum possible sum is n * 1e9 = 1e5 *1e9=1e14. So if we set max_abs to 1e14, then any target with absolute value greater than that can be ignored.

So the code for generating targets:

max_abs = 10**14 * 10  # Hmm, but the maximum possible sum is 1e14. Wait, but the sum can be up to 1e14. So any target T with |T| >1e14 cannot be achieved. So during generation of targets, once |current *k| exceeds 1e14, we stop.

Wait, during the code:

current starts at 1.

In the loop:

next_val = current *k.

Check if abs(next_val) > max_abs (1e14). If yes, break.

Else, check if next_val is already in the targets. If yes, break. Else, add to targets.

So the code:

max_abs_sum = 10**14

targets = set()

current =1

targets.add(current)

while True:

    next_val = current * k

    if abs(next_val) > max_abs_sum:

        break

    if next_val in targets:

        break

    targets.add(next_val)

    current = next_val

But wait, what if next_val is already in the targets, but not due to a cycle? For example, if k=3, and next_val is 3 (current is 1). Then current becomes 3. Next next_val is 9. Then 27, etc. But in this case, next_val is not in the targets. So the loop will proceed.

But for k=2, next_val is 2, then 4, etc., until next_val exceeds 1e14.

Now, after generating the targets, process each T in targets.

But note that some T's could be 0. But since k can't be zero, the code for generating T's will not generate 0. Because for any k in [-10, 10], but not zero, and exponents m >=0, k^m can't be zero.

But the array elements can have negative values, so the sum can be zero. But if zero is not in the targets, then such subarrays are not counted.

So the code proceeds.

Now, for each T in the targets set, compute the number of subarrays that sum to T.

But how to compute that?

Implement the standard two-sum approach for each T.

But in Python, using a defaultdict for count_map would be efficient.

But for large n=1e5, and multiple T's, this could be time-consuming.

But let's see. For each T, the code would loop through all elements once, maintaining a count_map and accumulating the count.

But in Python, even with n=1e5, each loop is O(n), which for 60 targets would be 6e6 operations. But in Python, each loop iteration is a bit slow. So perhaps for n=1e5 and 60 targets, this would take 6e6 steps, each with a few operations. But in practice, Python can handle 1e6 operations in about 0.1 seconds. So 6e6 would be 0.6 seconds, which is acceptable.

But the problem is that the code would loop through each target and each element, leading to O(n * m) time. Let's see:

For each T:

   count_map is initialized to {0:1}

   current_sum =0

   count =0

   for num in a:

       current_sum += num

       required = current_sum - T

       if required in count_map:

           count += count_map[required]

       if current_sum in count_map:

           count_map[current_sum] +=1

       else:

           count_map[current_sum] =1

   total += count

But for each T, this is O(n) time.

But in Python, for n=1e5 and m=60, 6e6 steps. But perhaps using a defaultdict would help here.

But in Python, the code for a single T would be:

from collections import defaultdict

count =0

count_map = defaultdict(int)

count_map[0] =1

current_sum =0

for num in a:

    current_sum += num

    required = current_sum - T

    count += count_map.get(required, 0)

    count_map[current_sum] +=1

But defaultdict is more efficient than using a regular dict and checking for presence.

But in code, for each T, the code must process the array. So this could be slow in Python.

Alternative approach: Precompute all possible prefix sums once, then for each T, compute how many times (current_sum - T) occurs in the prefix sums up to that point.

But the problem is that for each T, the count_map starts fresh. So for each T, you have to process the array from the beginning, keeping track of the count_map as you go.

So this seems unavoidable.

But perhaps, in Python, using a regular dict and checking for keys would be slower than using a defaultdict. So using a defaultdict for count_map would be better.

But how to structure the code.

So the plan:

Generate all targets.

For each target T in the targets:

   initialize count_map as defaultdict(int)

   count_map[0] =1

   current_sum =0

   res =0

   for num in a:

       current_sum += num

       res += count_map.get(current_sum - T, 0)

       count_map[current_sum] +=1

   total += res

But in Python, for each T, this loop is O(n), but for 1e5 elements, each iteration is a few steps. Let's see:

Each iteration:

current_sum += num → O(1)

res += count_map.get(...) → O(1)

count_map[current_sum] +=1 → O(1)

But defaultdict's __getitem__ is O(1), and so is __setitem__.

So for 1e5 elements, this is O(n) per target.

Now, in the first sample input:

n=4, targets are 1,2,4,8, etc. up to 8 (since 16 is 16, which is larger than the sum of the array (8)).

So for target 2:

count_map starts with {0:1}

current_sum after each step:

0+2=2 → required=2-2=0. count += count_map[0] (1) → res=1. Then count_map[2] becomes 1.

Then next num is 2 → current_sum=4. required=4-2=2. count_map has 2:1. So res +=1 → res=2. Then count_map[4] becomes 1.

Next num is 2 → current_sum=6. required=6-2=4. count_map has 4:1. res +=1 → res=3. count_map[6] becomes 1.

Next num is 2 → current_sum=8. required=8-2=6. count_map has 6:1 → res +=1 → res=4. count_map[8] becomes 1.

So for target 2, res is 4. Which is correct (the four single elements).

For target 4:

count_map starts with {0:1}

current_sum after each step:

2 → required=2-4 =-2 → not present. res=0. count_map[2] =1.

Then 4 → required=4-4=0. count_map[0:1] → res +=1 → res=1. count_map[4] =1.

Then 6 → required=6-4=2 → count_map[2:1] → res +=1 → res=2. count_map[6] =1.

Then 8 → required=8-4=4 → count_map[4:1 → res +=1 → res=3. count_map[8] =1.

So for target 4, res=3. Which corresponds to the three pairs.

For target 8:

current_sum steps:

2 → required 2-8 =-6 → no. res 0. count_map[2] =1.

4 → required 4-8=-4 → no. count_map[4] =1.

6 → required 6-8=-2 → no. count_map[6] =1.

8 → required 8-8=0 → count_map[0:1 → res +=1. So res=1.

So for target 8, res=1. Which is the entire array.

So the total is 4+3+1=8, which matches the sample.

Thus, the code works.

Now, code:

But in Python, when k is 1, the code adds 1 to the targets. Then, when k=1, multiplying 1 by k gives 1 again. So the loop breaks. So targets is {1}.

So for the code, in the case where the sum is 1, the code will count all subarrays whose sum is 1.

Similarly for k=-1.

Now, code:

Read n and k.

Read the array.

Generate the targets.

Compute the sum of counts for each target.

But code steps:

Read n, k = map(int, input().split())

a = list(map(int, input().split()))

Then generate the targets.

Then for each target in the targets, compute the count.

But code:

But for k=1:

targets = {1}

For k=-1:

targets = {1, -1}

So code for generating the targets:

max_abs_sum = 10**14

targets = set()

current = 1

targets.add(current)

while True:

    next_val = current * k

    if abs(next_val) > max_abs_sum:

        break

    if next_val in targets:

        break

    targets.add(next_val)

    current = next_val

But wait, what if k=1? Then next_val is 1*1=1. So in the first iteration, next_val is 1, which is in the targets, so break. So the targets set is {1}.

For k=3:

current starts at 1, next_val=3. Add. Then next_val=9. Add. Until next_val exceeds 1e14.

Now, code:

Now, after generating the targets, we need to process each T in the targets.

But the code for each T is:

from collections import defaultdict

total =0

for T in targets:

    count_map = defaultdict(int)

    count_map[0] =1

    current_sum =0

    res =0

    for num in a:

        current_sum += num

        res += count_map.get(current_sum - T, 0)

        count_map[current_sum] +=1

    total += res

print(total)

But in Python, using a defaultdict for each T may be time-consuming for multiple Ts. So perhaps using a normal dict and handling it with get.

But the code seems correct.

Testing the first sample:

Sample input 1:

4 2

2 2 2 2

targets are 1,2,4,8,16, etc. until 8 is included. Wait, no. Let's see:

current starts at 1 (m=0). next_val is 2 (m=1). Added.

next_val =2*2=4 (m=2). Added.

next_val=4*2=8 (m=3). Added.

next_val=8*2=16 (m=4). Check if 16 >1e14? No, but sum of array is 8, so 16 is allowed. So code adds 16. Then next_val=32, etc. until 1e14.

But the sum of the entire array is 8, but the code will process all targets up to 1e14. So for target 16, the code will look for subarrays summing to 16, which are not present. So for that target, the code will contribute 0.

But the code will generate all possible targets up to 1e14. So for k=2, the code generates 1, 2,4,8,16,32,..., up to 2^46 (since 2^47 is 1.4e14, which is over 1e14). But for the sample input, only the targets 2,4,8 are present in the possible subarray sums. So for the other targets (like 1,16, etc.), the code will add 0 to the total.

But in the sample, the total is 8. The code for T=1, T=2, T=4, T=8, etc. would compute:

T=1: no subarrays sum to 1 → 0.

T=2: 4 subarrays → adds 4.

T=4: 3 subarrays → adds 3.

T=8: 1 subarray → adds 1.

The other targets (16, 32, etc.) add 0.

Total 4+3+1=8.

Which is correct.

Thus, the code is correct.

Now, code:

But in Python, for n=1e5 and m=60, this code may be slow. Because for each T, the code loops through all elements and uses a defaultdict which can be slow in Python.

Alternative optimizations:

1. Precompute the prefix sums array once, and for each T, compute the required values.

But even then, for each T, you need to track the count of (current_sum - T) in the prefix sums up to the current point. This is similar to the original approach.

Alternative idea: precompute the list of prefix sums, then for each T, use a hash map to track the occurrences of (current_sum - T) as you iterate through the prefix sums. But this is the same as the original approach.

Thus, there's no way to avoid O(n * m) time.

But in Python, perhaps using a standard dictionary and get() is faster than defaultdict.

So modifying the code for each T to use a normal dict:

For each T:

count_map = {0:1}

current_sum =0

res=0

for num in a:

    current_sum += num

    req = current_sum - T

    res += count_map.get(req, 0)

    # Update count_map for current_sum

    count_map[current_sum] = count_map.get(current_sum, 0) +1

This may be slightly faster than using defaultdict.

But let's see:

In the code:

count_map = defaultdict(int)

count_map[0] =1

But defaultdict will create entries for missing keys, but when using get, it's the same as a normal dict.

Alternatively, using a normal dict:

count_map = {0:1}

Then, for req:

res += count_map.get(req, 0)

Then, for current_sum:

count_map[current_sum] = count_map.get(current_sum, 0) +1

But this is O(1) per operation.

So perhaps using a normal dict is better.

Thus, modifying the code for each T:

count_map = {0: 1}

current_sum =0

res=0

for num in a:

    current_sum += num

    req = current_sum - T

    res += count_map.get(req, 0)

    if current_sum in count_map:

        count_map[current_sum] +=1

    else:

        count_map[current_sum] =1

This may be more efficient.

But for large n, checking for key existence and updating the dict may take more time. But perhaps in Python, using a normal dict and get is faster.

Alternatively, using a Counter.

But in any case, for Python, the code should be optimized.

Another optimization: precompute all prefix sums once and store them in a list. Then, for each T, process the prefix sums.

But the code would look like:

prefix = [0]

for num in a:

    prefix.append(prefix[-1] + num)

Then for each T in targets:

count_map = {0:1}

res=0

for s in prefix[1:]:  # since prefix[0] is 0, and the first element is prefix[1] = a[0]

    req = s - T

    res += count_map.get(req, 0)

    count_map[s] = count_map.get(s, 0) + 1

total += res

This way, the prefix is computed once, and for each T, we process the prefix sums.

But this approach may be more efficient as the loop is over the precomputed prefix sums. But in practice, the difference is minimal.

But for the code, perhaps this approach is better.

Thus, code steps:

Compute prefix sums.

For each T:

   count_map starts with {0:1}

   res=0

   for s in prefix[1:]:

       req = s - T

       res += count_map.get(req, 0)

       count_map[s] = count_map.get(s, 0) +1

   total += res

But prefix is a list of n+1 elements.

But for Python, appending to a list is O(1) per element, so building the prefix sum is O(n).

Thus, the code becomes:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    prefix = [0]

    for num in a:

        prefix.append(prefix[-1] + num)

    max_abs_sum = 10**14

    targets = set()

    current = 1

    targets.add(current)

    while True:

        next_val = current * k

        if abs(next_val) > max_abs_sum:

            break

        if next_val in targets:

            break

        targets.add(next_val)

        current = next_val

    total =0

    for T in targets:

        count_map = {0:1}

        res =0

        for s in prefix[1:]:  # s is the sum up to current element

            req = s - T

            res += count_map.get(req, 0)

            # Update count_map for s

            count_map[s] = count_map.get(s, 0) +1

        total += res

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 -3
3 -6 -3 12
""",
            "output": \
"""\
3
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

Sample input 2:

4 -3

3 -6 -3 12

The output is 3.

The possible targets are:

current starts as 1 (k^0).

next_val is 1 * (-3) =-3. Add to targets.

next_val is -3 * (-3) =9. Add.

next_val is 9*(-3) =-27. Add.

next_val is -27 * (-3) =81. Add.

etc., until the absolute value exceeds 1e14.

But the sum of the array elements:

prefix sums are [0,3, -3, -6,6]

Looking for which T's are in the targets and present in the sums.

The targets are 1, -3,9,-27,81,..., up to 1e14.

Now, the valid subarrays are:

[1,2] (elements 3 and -6, sum is -3 → T=-3 is in targets.

[3,3] (element -3 → sum is -3. But T=-3 is a target. So this subarray is counted.

[3,4]: sum is -3 +12=9 → T=9 is a target.

So total three.

So the code for each T:

For T=1:

look for subarrays with sum 1. None.

For T=-3:

count the number of times (s - (-3)) is in count_map. Which is s+3.

prefix sums:

3, -3, -6, 6.

Processing:

count_map starts with {0:1}.

s=3: req=3+3=6 → not in count_map (count_map is {0:1}) → res +=0.

count_map[3] =1.

s=-3: req=-3 +3=0 → count_map[0] is 1 → res +=1. count_map[-3] =1.

s=-6: req=-6+3 =-3 → count_map[-3] is 1 → res +=1. count_map[-6] =1.

s=6: req=6+3=9 → count_map has no 9. res remains 2. count_map[6] =1.

So T=-3 contributes 2.

For T=9:

req = s -9.

count_map starts with {0:1}.

s=3: req=3-9=-6 → not present. res=0. count_map[3] =1.

s=-3: req=-3-9=-12 → no. count_map[-3] =1.

s=-6: req=-6-9=-15 → no. count_map[-6] =1.

s=6: req=6-9 =-3 → count_map[-3] is 1 → res +=1. count_map[6] =1.

So T=9 contributes 1.

Total is 2 (from T=-3) + 1 (from T=9) =3. Which matches the sample.

Thus, the code works.

Now, the code should be correct.

But what about when the sum is zero? For example, if there's a subarray with sum zero, but zero is not a power of k. Then it's not counted. But the code correctly ignores it.

Another test case: k=1. Targets are {1}. So any subarray with sum 1 is counted.

In code, the code will process T=1.

Now, what about when k=0? But the constraints say 1 ≤ |k| ≤10, so k can't be zero.

Thus, the code is correct.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0]
for num in a:
    prefix.append(prefix[-1] + num)

max_abs_sum = 10**14
targets = set()
current = 1
targets.add(current)
while True:
    next_val = current * k
    if abs(next_val) > max_abs_sum:
        break
    if next_val in targets:
        break
    targets.add(next_val)
    current = next_val

total = 0
for T in targets:
    count_map = {0: 1}
    res = 0
    for s in prefix[1:]:
        req = s - T
        res += count_map.get(req, 0)
        count_map[s] = count_map.get(s, 0) + 1
    total += res

print(total)
```
