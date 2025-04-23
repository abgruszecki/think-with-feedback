<think>
Okay, let's tackle this problem. So, the task is to find the number of subarrays (contiguous sequences) that have a negative product and those that have a positive product. The key here is to determine for each possible subarray whether the product is negative or positive. But calculating the product directly for every possible subarray is impossible because there are O(n²) subarrays, which is way too slow for n up to 2e5. So we need a smarter approach.

First, let's think about the product's sign. The product is negative if there's an odd number of negative elements in the subarray. Because each negative number flips the sign. So the problem reduces to counting the number of subarrays with an odd number of negatives (for the negative product count) and even number of negatives (for the positive count).

So the main idea is to track the number of negative elements encountered so far and determine how many subarrays ending at each position have even or odd counts of negatives. Then, we can accumulate these counts to get the total.

Hmm. Let's think about it. Suppose we keep a running count of the number of negatives. Let's say we have a variable that tracks the current number of negatives modulo 2. For each position i, we can compute the current parity (0 for even, 1 for odd). Then, the number of previous positions where the parity was the same as current (which would mean the subarray between those positions has even negatives) or different (for odd).

Wait, maybe using a hash to track the number of times each parity has occurred up to the current point. Let's see. For example, suppose we have a count of even and odd parities up to the current index. Then, when we process each element, we can update the current parity and use the counts to find how many subarrays ending here have even or odd negatives.

Wait, let's formalize this. Let's consider the prefix sum of negatives. Let's say we have an array where each element is 1 if the number is negative, 0 otherwise. The prefix sum S[i] is the number of negatives up to index i. Then, for a subarray (l, r), the number of negatives is S[r] - S[l-1]. The parity of this difference (even or odd) determines the sign of the product.

So, for a subarray (l, r) to have a negative product, (S[r] - S[l-1]) must be odd. Which implies that S[r] and S[l-1] have different parities. For even product, they must have the same parity.

So, the problem reduces to, for each r, count the number of l-1 (where l-1 < r) such that S[r] - S[l-1] is odd (for negative product) and even (for positive). So, for each r, we need the number of previous prefix sums with parity different from S[r] (for negative count) and same (for positive count).

But l can start at 0 (the empty prefix, which is S[0] = 0). Wait, but in this case, l ranges from 1 to r+1, since l-1 is from 0 to r. Because the subarray (l, r) corresponds to l ranging from 1 to r. So, the prefix sums S is 0-based, with S[0] = 0, S[1] = count of negatives in first element, etc.

So, for each r (the end of the subarray), the possible l-1 can be from 0 to r. So for each r, we can look at the current parity (S[r] mod 2) and find how many times each parity has been seen in the prefix up to index r.

But wait, how do we compute this? Let's think: the number of subarrays ending at r (i.e., the end is r) with even or odd counts is determined by the parity of S[r] and the parity of the previous prefixes. For each r, the number of subarrays ending at r with even negatives is the number of times the same parity has been seen before, plus one (for the case where the entire subarray is from l=0 to r, but wait, no, S[0] is the prefix sum before the first element. So for each r, the subarrays (l, r) where l ranges from 1 to r. So l-1 ranges from 0 to r-1. So when considering S[r], the difference S[r] - S[l-1] is for l-1 from 0 to r. Wait, no: the subarray (l, r) is from index l-1 (exclusive) to r (inclusive). So S[r] - S[l-1] gives the count of negatives in the subarray l to r.

So for each r, we need to count how many l-1 (from 0 to r) have S[r] - S[l-1] odd. Wait, no. Because the subarray (l, r) is from index l to index r (assuming 1-based indices). So l can be 1 to r. Then l-1 is 0 to r-1. So the difference S[r] - S[l-1] is the number of negatives in the subarray. So for the subarray (l, r) to have an odd number of negatives, S[r] - S[l-1] must be odd. So the parity of S[r] and S[l-1] must differ. So for each r, the number of such l-1 (from 0 to r-1) where S[l-1] has parity different from S[r] is the number of subarrays ending at r with negative product.

Similarly, the number of subarrays ending at r with even product is the number of l-1 (from 0 to r-1) where S[r] and S[l-1] have the same parity.

So the approach is:

- Precompute the prefix sum of negatives mod 2.
- For each position r, track the number of times each parity (0 and 1) has occurred in the prefix sum up to r-1.
- For the current parity (S[r] mod 2), the number of subarrays ending at r with even product is the count of previous parities equal to current parity. The number with odd product is the count of previous parities different from current parity.

But wait, the prefix sum array S is 0-based. For example, S[0] is 0 (no elements), S[1] is the count for the first element, etc. So for each r in 1..n, the parity is S[r] mod 2. Then, the number of l-1 in 0..r-1 (since l ranges from 1 to r) where S[l-1] mod 2 is equal to (current parity) is the count for even product, and different for odd.

So the idea is to keep a frequency map that tracks how many times each parity (0 or 1) has occurred in the prefix sums up to the previous index. As we iterate through each index r (from 1 to n), we:

1. Compute the current parity (current_prefix_mod_2).
2. The number of even subarrays ending at r is the frequency of current_prefix_mod_2.
3. The number of odd subarrays ending at r is the frequency of (1 - current_prefix_mod_2).
4. Then, we add these numbers to the total even and odd counts.
5. Update the frequency map by incrementing the count for current_prefix_mod_2.

Wait, but the frequency map starts with S[0] mod 2, which is 0. So for the first element (r=1), the current_prefix_mod_2 is S[1] mod 2. The previous prefixes are S[0] mod 2 (which is 0). So for the first element, the even count is if current_prefix mod 2 is 0 (since S[1] - S[0] is even), which would contribute 1 subarray (the entire first element) to even count if current parity is 0, else to odd count.

Wait, let's take an example. Let's say the first element is negative. Then S[1] = 1, mod 2 is 1. The previous prefixes are S[0] mod 2 is 0. So the number of subarrays ending at r=1 with even product is the number of previous prefixes with parity 1. But the previous prefixes (only S[0] mod 2=0) have different parity. So the even count here is 0, and the odd count is 1. Which makes sense: the subarray (1,1) has product negative.

So for each r, the current prefix is S[r], and the previous prefixes are S[0] to S[r-1]. So the frequency map should track the counts of parities in S[0] to S[r-1]. For each step, we process the current S[r], compute the counts based on the previous frequencies, then add the current S[r]'s parity to the frequency map for the next steps.

Wait, no. Wait, when processing r, the current prefix is S[r]. The l-1 can be from 0 to r. So the l ranges from 1 to r+1. Wait, this is getting a bit confusing. Let's clarify.

The prefix sum array is S[0] = 0, S[1] = a_1's sign (1 if negative), S[2] = S[1] + a_2's sign, etc. For a subarray (l, r) (1-based l and r), the number of negatives is S[r] - S[l-1]. So when considering all subarrays that end at r (i.e., all l from 1 to r), then l-1 ranges from 0 to r-1. So for each r, the current parity is S[r] mod 2. Then, the number of subarrays ending at r with even product (even number of negatives) is the number of l-1 in 0..r-1 where S[l-1] mod 2 equals S[r] mod 2. Similarly for odd product.

So the initial frequency map starts with S[0] mod 2 (which is 0). Then, for each r starting from 1 to n:

- The current parity is S[r] mod 2.
- The number of even subarrays ending at r is the count of previous parities (in S[0] to S[r-1]) that are equal to current parity.
- The number of odd subarrays ending at r is the count of previous parities that are different from current parity.
- Then, we add the current parity to the frequency map (for future r's to consider).

Wait, but for the next r, the current parity (S[r]) will be part of the l-1 prefixes for the next elements. So yes, after processing r, we add the current parity to the frequency map. Because when we process r+1, the l-1 can be up to r, which includes S[r] mod 2.

But wait, for r=1, the l-1 can be 0. So during processing r=1, the previous parities are S[0], which is 0. So the frequency map starts with S[0] mod 2 (count 1 for parity 0). Then, when processing r=1:

current_parity = S[1] mod 2.
even_count += freq[current_parity]
odd_count += freq[1 - current_parity]
Then, add current_parity to freq (so that for r=2, we have S[0], S[1] in the frequency).

Yes, that makes sense. So the steps are:

Initialize a frequency dictionary with {0: 1} (since S[0] mod 2 is 0).

Initialize even_total and odd_total to 0.

current_prefix_negatives = 0 (since S[0] is 0).

For each number in the array:

- Check if it's negative. If yes, increment current_prefix_negatives by 1.
- current_parity = current_prefix_negatives % 2.
- even_subarrays = freq.get(current_parity, 0)
- odd_subarrays = freq.get(1 - current_parity, 0)
- even_total += even_subarrays
- odd_total += odd_subarrays
- Update freq by incrementing the count for current_parity by 1.

Wait, wait. Wait, the current_parity here is S[r], but in the code above, after processing each element, the current_prefix_negatives is the sum up to the current element. For example, after the first element (i=0 in the array, but first element in the sequence), current_prefix_negatives is 1 if it's negative, 0 otherwise. Then current_parity is S[1] mod 2.

But the frequency map starts with S[0] mod 2 (count 1). Then, for each element in the array, after updating current_prefix_negatives, we compute current_parity (which is S[r] mod 2, where r is the current index in 1-based). Then, the even_subarrays for subarrays ending at r is the number of previous S[l-1] mod 2 equal to current_parity. Because those would be l-1 from 0 to r-1. So yes, the code logic is correct.

So this approach is O(n) time and O(1) space (since the frequency map only has two possible keys, 0 and 1).

So this seems like the optimal approach. Now, let's test this with the first example.

First example input:

5
5 -3 3 -1 1

Let's process each element step by step.

Initialize freq = {0:1}, even_total = 0, odd_total = 0, current_prefix_negatives = 0.

Element 1: 5 (positive). So current_prefix_negatives remains 0. current_parity = 0 mod 2 = 0.

even_subarrays = freq[0] = 1. So even_total +=1 → 1.

odd_subarrays = freq[1 - 0] = 0. So odd_total +=0 → 0.

Update freq: freq[0] becomes 2.

Element 2: -3 (negative). current_prefix_negatives becomes 1. current_parity =1.

even_subarrays = freq[1] → which is 0. So even_total remains 1.

odd_subarrays = freq[0] →2. So odd_total becomes 0+2=2.

Update freq: add 1 → freq is {0:2, 1:1}.

Element3:3 (positive). current_prefix_negatives remains 1. parity 1.

even_subarrays: freq[1] is 1 → even_total becomes 1+1=2.

odd_subarrays: freq[0] is 2 → odd_total becomes 2+2=4.

Update freq: 1's count becomes 2.

Element4: -1 (negative). current_prefix_negatives becomes 2. parity 0.

even_subarrays: freq[0] is 2 → even_total +=2 → 2+2=4.

odd_subarrays: freq[1] is 2 →4+2=6.

Update freq: 0's count becomes 3.

Element5:1 (positive). current_prefix_negatives remains 2. parity 0.

even_subarrays: freq[0] is 3 →4+3=7.

odd_subarrays: freq[1] is 2 →6+2=8.

Update freq: 0's count becomes 4.

So after processing all elements, even_total is 7, odd_total is 8. Wait, but the sample output is 8 for negative and 7 for positive. But according to this, even_total is the number of subarrays with even number of negatives (positive product) and odd_total is the number of subarrays with odd number of negatives (negative product). So the output should be odd_total and even_total. Wait, the first number in the output is the count of negative products (which is odd_total), and the second is positive (even_total). So in the first sample, our code would compute 8 and 7, which matches the sample. So this approach works.

Another sample: the third input:

5
-1 -2 -3 -4 -5

All elements are negative. So the prefix_negatives after each step are 1, 2,3,4,5. Their parities are 1,0,1,0,1.

Let's step through:

Initial freq {0:1}, even=0, odd=0.

Element1: -1. current_prefix=1. parity 1.

even_subarrays: freq[1] →0. even remains 0.

odd_subarrays: freq[0] →1. odd +=1.

Update freq: {0:1, 1:1}.

Element2: -2. current_prefix=2. parity 0.

even_subarrays: freq[0] →1 (from S[0] parity 0). even +=1 →1.

odd_subarrays: freq[1] →1. odd +=1 →2.

Update freq: {0:2, 1:1}.

Element3: -3. current_prefix=3 →parity 1.

even_subarrays: freq[1] →1. even becomes 1+1=2.

odd_subarrays: freq[0] →2. odd becomes 2+2=4.

Update freq: 1's count becomes 2.

Element4: -4. parity 0 (current_prefix=4).

even_subarrays: freq[0] →2. even=2+2=4.

odd_subarrays: freq[1] →2. odd=4+2=6.

Update freq: 0's count becomes 3.

Element5: -5. parity 1 (current_prefix=5).

even_subarrays: freq[1] →2. even=4+2=6.

odd_subarrays: freq[0] →3. odd=6+3=9.

So even_total is 6, odd_total is9. Which matches the third sample's output of 9 6. So the code works here.

So the approach is correct.

Now, the code can be implemented in Python. Since the frequency map only tracks two possible values, we can use a list of size 2. Let's index 0 and 1.

Initialize counts = [1, 0], since the initial frequency is {0:1}.

Wait, no. The initial frequency is that parity 0 has been seen once. So counts[0] =1, counts[1]=0.

Then, for each element:

current_parity = (current_prefix_negatives) %2.

even_subarrays = counts[current_parity]

odd_subarrays = counts[1 - current_parity]

Then, we add even_subarrays to the even_total, and odd_subarrays to the odd_total.

Wait, no. Wait, the code as per the previous analysis:

For each element, the even_subarrays (positive product) is the number of previous parities equal to current_parity. The odd_subarrays (negative product) is the number of previous parities not equal to current_parity.

But wait, no. Wait, even_subarrays are the ones where the product is even, which is when the number of negatives is even, i.e., even number of negatives. But the even_subarrays here are the ones where S[r] - S[l-1] is even. Which is when S[r] and S[l-1] have the same parity. So for current_parity, even_subarrays is the count of previous parities equal to current_parity.

But the even_subarrays correspond to positive products, which is the count of even_subarrays. The odd_subarrays correspond to negative products, which is the count of odd_subarrays.

So the code should accumulate:

negative_count += odd_subarrays

positive_count += even_subarrays

Wait, yes. Because:

If current_parity is the parity of S[r], then the even_subarrays (counted as the number of previous S[l-1] with same parity as current_parity) gives the number of subarrays ending at r with even product (positive), and the odd_subarrays (previous S[l-1] with different parity) gives the number of subarrays ending at r with negative product.

So, the code's variables even_total and odd_total should be:

positive_count = sum of even_subarrays for each r.

negative_count = sum of odd_subarrays for each r.

Wait, right. So the code will:

Initialize positive_count and negative_count to 0.

counts = [1, 0] (since initial parity is 0, which is counts[0] =1).

current_prefix_negatives =0.

Then, for each element in the array:

if the element is negative, current_prefix_negatives +=1.

current_parity = current_prefix_negatives %2.

positive_increment = counts[current_parity]

negative_increment = counts[1 - current_parity]

positive_count += positive_increment

negative_count += negative_increment

counts[current_parity] +=1

Wait, no. Let's see:

For each element, after determining current_parity (which is S[r] mod 2), the number of subarrays ending at r with even product (positive) is the counts[current_parity], because those are the previous parities (from S[0] to S[r-1]) that match current_parity, leading to even product.

Similarly, the number of subarrays ending at r with odd product (negative) is counts[1 - current_parity], since those are the previous parities that are different.

So yes, positive_count accumulates the sum of even_subarrays (same parity) and negative_count the sum of odd_subarrays (different parity).

So the code in Python would look something like:

n = int(input())
a = list(map(int, input().split()))

counts = [1, 0]  # counts[0] is the initial S[0] parity 0
current_neg = 0
positive = 0
negative = 0

for num in a:
    if num <0:
        current_neg +=1
    current_parity = current_neg %2
    positive += counts[current_parity]
    negative += counts[1 - current_parity]
    counts[current_parity] +=1

print(negative, positive)

Wait, let's test this code with the first sample input.

Sample 1:

5
5 -3 3 -1 1

Processing each element:

Element 5: positive. current_neg remains 0. current_parity 0.

positive += counts[0] (1). So positive=1.

negative += counts[1-0=1] (0). So negative=0.

counts[0] becomes 2.

counts is [2,0]

Element -3: current_neg=1. parity 1.

positive += counts[1] (0) →1+0=1.

negative += counts[0] (2) →0+2=2.

counts[1] becomes 1.

counts [2,1]

Element 3: current_neg remains 1. parity 1.

positive += counts[1] (1) →1+1=2.

negative += counts[0] (2) →2+2=4.

counts[1] becomes 2.

counts [2,2]

Element -1: current_neg=2. parity 0.

positive += counts[0] (2) →2+2=4.

negative += counts[1] (2) →4+2=6.

counts[0] becomes 3.

counts [3,2]

Element 1: current_neg remains 2. parity 0.

positive += counts[0] (3) →4+3=7.

negative += counts[1] (2) →6+2=8.

counts[0] becomes 4.

So the code outputs 8 7, which is correct.

Third sample:

5
-1 -2 -3 -4 -5

Processing:

element -1: current_neg=1 →parity 1.

positive += counts[1] (0) →0.

negative += counts[0] (1) →1.

counts[1] becomes 1.

element -2: current_neg=2 →parity 0.

positive += counts[0] (1) →1.

negative += counts[1] (1) →2.

counts[0] becomes 2.

element -3: current_neg=3 →parity 1.

positive += counts[1] (1) →1+1=2.

negative += counts[0] (2) →2+2=4.

counts[1] becomes 2.

element -4: current_neg=4 →parity 0.

positive += counts[0] (2) →2+2=4.

negative += counts[1] (2) →4+2=6.

counts[0] becomes 3.

element -5: current_neg=5 →parity 1.

positive += counts[1] (2) →4+2=6.

negative += counts[0] (3) →6+3=9.

counts[1] becomes 3.

So output is 9 6, which matches the sample.

So the code works.

Now, for the constraints. The code runs in O(n) time, which is acceptable for n up to 2e5. The space is O(1), using only a list of two integers. So this should work within the time and memory limits.

Thus, the code is correct and optimal.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

counts = [1, 0]
current_neg = 0
positive = 0
negative = 0

for num in a:
    if num < 0:
        current_neg += 1
    parity = current_neg % 2
    positive += counts[parity]
    negative += counts[1 - parity]
    counts[parity] += 1

print(negative, positive)
```