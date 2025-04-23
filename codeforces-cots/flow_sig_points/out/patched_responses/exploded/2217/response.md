<think>
Okay, let's see. The problem is to find the number of ways to cut a stripe into three parts such that each part has the same sum. Each part must have at least one square, so the cuts can't be at the very start or end. 

Hmm. So, first, the total sum of all elements must be divisible by 3. Because if the total sum S isn't divisible by three, then each part can't be S/3. So that's the first check. If the total sum isn't divisible by three, the answer is zero.

But even if the total is divisible by three, we need to find two cut points. Let's call the target sum for each part as total_sum / 3. Let's denote the target as s.

So, the first part must sum to s, the second part to s as well, and the third part will automatically be s because the total is 3s. 

Wait, but how do the cuts work? The stripe is split into three parts. So, for example, if the array is [a, b, c, d], then possible splits are after the first and second elements (cuts between a and b, and between b and c), resulting in parts [a], [b], [c,d] — no, wait wait. Wait, three parts. So the first cut is after i squares (so part 1 is 0..i), the second cut is after j squares (so part 2 is i+1..j, part3 is j+1..n-1). So both cuts have to be between elements. And each part must be non-empty, so i must be >=0, j must be >i, and j <n-1. Because part 3 has to have at least one element.

So, the sum of part 1 is sum(0..i) = s. The sum of part 2 is sum(i+1..j) = s. The sum of part3 is sum(j+1..n-1) = s. 

So, the approach is to find all possible pairs (i,j) where i < j, such that sum up to i is s, sum from i+1 to j is s, and the remaining sum is s. 

But calculating this directly for all possible i and j would be O(n^2), which is way too slow for n=1e5. So we need a smarter way.

Let's think about the prefix sums. Let's precompute the prefix sum array. Let prefix[i] be the sum of the first i elements (0-based). Then the total sum is prefix[-1]. So total_sum must be 3s. 

For the three parts to each have sum s, the first part's sum is s, which is prefix[i] = s. The second part's sum is s: prefix[j] - prefix[i] = s. The third part's sum is prefix[-1] - prefix[j] = s. 

But since the total sum is 3s, the third part's sum must be s. So if the first two parts are s each, the third is automatically s. So the conditions are:

1. prefix[i] = s
2. prefix[j] = 2s
3. i < j, and j < n-1 (since the third part needs at least one element)

Wait, because the third part is from j+1 to n-1, so j has to be at most n-2. So j can be from i+1 up to n-2.

So for all j where prefix[j] is 2s and j is <=n-2, and there exists some i < j where prefix[i] is s. So the problem reduces to: for each j (where prefix[j] = 2s and j < n-1), count the number of i's that are less than j where prefix[i] = s.

So the plan is:

1. Compute the total sum. If it's not divisible by 3, return 0.
2. Else, s = total_sum /3. Then 2s is 2/3 of the total sum.
3. Precompute the prefix sum array.
4. Iterate through the array, and for each j, if prefix[j] == 2s and j < n-1, then add the number of times s has occurred in the prefix sum up to j-1.

So the steps are:

- Compute the prefix sum array.
- For each j from 0 to n-2 (since j has to be at least such that j+1 <=n-1, so j can be up to n-2), check if prefix[j] is 2s. If yes, then add the count of s's in prefix[0..j-1].

But how to efficiently count the number of s's up to j-1? We can keep a running count. For example, as we iterate through the array, for each position i, we can track how many times s has been seen so far. Then, when we reach j, if prefix[j] is 2s, we can look up the count of s up to j-1.

Yes. So here's the approach:

- Compute prefix sum array.
- Check if total sum is not divisible by 3. If so, return 0.
- Else, s = total /3. 2s = 2 * s.
- Initialize a count variable to track the number of times s has been seen in the prefix sum up to current position.
- Also, initialize the result to 0.
- Iterate through the array from 0 to n-1 (but j can't be n-1 because j+1 has to exist). Wait, for j, the maximum possible is n-2. So during iteration, when j is from 0 to n-2 (inclusive), check if prefix[j] is 2s. If yes, add the count of s's in prefix up to j-1.

Wait, but how? Let's see. We need to process each j from 0 to n-1. But j must be at least 1, because the first part must have at least one element. For example, the first cut can't be at j=0, because then part 1 is 0 elements. So j has to be >=1. Wait, no. Wait, the first part is from 0 to i. So i can be 0 (if the first part is the first element). Then j has to be i+1. So i can be 0, j can be 1 (as long as the third part is from 2 to end, which requires that j+1 <=n-1. So j can be up to n-2.

But in the approach, for j in the prefix sum array, when prefix[j] is 2s, then the sum from 0 to i is s (so i is such that prefix[i] = s), and i must be less than j.

So for each j where prefix[j] = 2s and j < n-1, the number of valid i's is the number of times s appears in the prefix array up to j-1.

So the algorithm can be:

Compute the prefix array.

Check if total sum is 3s. If not, return 0.

Else, iterate through the prefix array, and for each j from 0 to n-2:

   if prefix[j] == 2s:

       count += number of times s occurred in prefix[0..j-1]

So to compute the number of times s occurred up to j-1, we can precompute a hash map (like a frequency dictionary) that tracks the number of times s has been seen up to each index. But that's O(n) space. Alternatively, as we iterate through each index, we can keep a running count of how many times s has been seen so far. Then, when j is processed, the count up to j-1 is the current count minus (1 if prefix[j] is s). Wait, no. Because the current count up to j includes prefix[j], but j-1 is up to j-1.

So here's a better way: as we iterate j from 0 to n-1:

- before checking if prefix[j] is 2s, we can check if j >=1 (since j-1 must exist for the i to be at least 0). Wait, j can be 0. If j is 0, then i has to be <0, which is impossible. So when j is 0, even if prefix[j] is 2s, there can be no i <0. So in that case, we can ignore it.

Wait, let's see. Let's suppose j is 0. Then 2s is prefix[j], which is sum up to j. So the sum of the first part is s, so i must satisfy prefix[i] = s. But i must be < j, which is 0, so i can be at most -1, which is invalid. So no possible i. So j can't be 0. So when j is 0, even if prefix[j] is 2s, the count is zero.

Similarly, j must be at least 1. So in our iteration, we can start from j=1 up to n-2.

Wait, but when j is 1, then the i can be up to 0. So for j=1, the count is the number of times s appears in prefix[0..0]. Which is whether prefix[0] is s.

So here's the plan:

We can iterate through each j in the array, and for each j, if j <n-1 and prefix[j] == 2s, then the number of valid i's is the number of times s appears in the prefix array from 0 to j-1.

So during iteration, as we go from left to right, for each j, before checking if prefix[j] is 2s, we can keep track of the count of s in the prefix array up to j-1.

So here's how:

Initialize a variable cnt_s = 0.

Initialize result =0.

Compute the prefix array.

Compute total sum. If not divisible by 3, return 0.

s = total_sum //3.

target_2s = 2*s.

Then iterate through each j from 0 to n-1:

   if j <n-1 and prefix[j] == target_2s:

       result += cnt_s

   if prefix[j] == s:

       cnt_s +=1

Wait, but here, when j is 0, and prefix[0] is s, then cnt_s is incremented. Then, when j increases, and if in the next steps, j is 1 and prefix[j] is target_2s, then the cnt_s would be 1 (if j=1 and prefix[j] is target_2s, then the cnt_s is the count up to j-1, which is 0, but in this case, after processing j=0, we added to cnt_s. So for j=1, when processing, we check if prefix[j] is target_2s. Then, add the current cnt_s (which is the count of s up to j-1).

Wait, no. Because when j=0, during processing j=0:

- check if j is <n-1. Yes. If prefix[0] is target_2s, then add cnt_s (which is 0 at that point, since cnt_s is incremented after checking). Then, if prefix[j] ==s (which it may not be), then cnt_s increases.

Wait, the order is: first, check if j is a candidate (prefix[j] == target_2s and j <n-1). If so, add the current cnt_s. Then, check if prefix[j] is s, and increment cnt_s if so.

So for j=0:

- Check if prefix[0] is target_2s and j <n-1. If yes, then add cnt_s (which is 0 here, because we haven't processed any previous elements). Then, if prefix[0] is s, increment cnt_s to 1.

So, for example, if j=1 is the index where prefix[j] is target_2s. Then when processing j=1, the cnt_s is the number of s's in prefix[0], which is 1 if prefix[0] is s.

Yes, because during j=0 processing, after the check, we added 1 to cnt_s (if prefix[0] is s). So for j=1, the cnt_s includes prefix[0] if it's s.

So the order is correct.

This approach allows us to count the number of s's before j. Because when we process j, the cnt_s holds the count of s's up to j-1. Because we check for j's condition (prefix[j] == target_2s) before updating the cnt_s. Because the cnt_s is updated only if prefix[j] is s, which is after checking for target_2s.

Yes. So this approach works.

So the steps in code would be:

Read n.

Read the array as list of integers.

Compute prefix sum array.

Compute total_sum = prefix[-1].

If total_sum %3 !=0, output 0.

Else:

s = total_sum //3

target_2s = 2*s

Initialize cnt_s =0

result =0

for j in range(n):

   if j <n-1 and prefix[j] == target_2s:

       result += cnt_s

   if prefix[j] == s:

       cnt_s +=1

Output result.

But wait, what about the cases where j is n-1? Since j must be <n-1. So in the loop, j can be up to n-1, but the first condition checks if j <n-1.

So for example, when j is n-1, even if prefix[j] is target_2s, but j is not <n-1 (since n-1 >=n-1), so no.

So the code should work.

Let's test this with the first example.

Sample Input 1:

4

1 2 3 3

prefix array is [1,3,6,9]

total_sum is 9, which is 3*3. So s=3, target_2s=6.

Now iterate through each j from 0 to 3 (indices 0,1,2,3):

j=0:

prefix[j] is 1. Check if j<3 (n-1 is 3). j=0 <3. Is prefix[0] 6? No. So result remains 0.

Then check if prefix[j] ==3. 1 !=3. cnt_s remains 0.

j=1:

prefix[j] is 3. Check if j<3. yes. Is 3 ==6? No. So no addition to result.

Check if prefix[1] is 3. Yes. cnt_s becomes 1.

j=2:

prefix[j] is 6. Check j<3. yes. 6 is target_2s. So add cnt_s (which is 1) to result. So result is 1.

Check if prefix[j] is 3. 6 !=3. cnt_s remains 1.

j=3:

prefix[j] is 9. j is not <3. So no addition.

Check if 9 ==3. No.

So the result is 1, which matches the sample.

Second sample:

5

1 2 3 4 5

prefix array is [1,3,6,10,15]

total_sum 15. 15/3=5. So s=5, target_2s=10.

Now iterate:

j=0: prefix[j] 1. Not target_2s. Check if equals s=5? No. cnt_s remains 0.

j=1: prefix 3. Not 10. Check equals 5? No.

j=2: prefix 6. Not 10. Check equals 5? No.

j=3: prefix 10. Check j<4 (since n-1=4). 10 is target_2s. So add cnt_s (0). result is 0.

Then check if prefix[j] is 5. No. cnt_s remains 0.

j=4: j >=4-1=3 (since n=5, j=4 is not <4). So no addition. Check if prefix[4] is 5. 15 !=5. So no change.

So result is 0.

Another test case: n=3, array [0,0,0]. Total sum is 0. s=0. target_2s=0.

prefix array is [0,0,0].

For j=0: j <2. prefix[j] is 0 (target_2s). So add cnt_s (0). Then, check if prefix[j] is s (0). So cnt_s becomes 1.

j=1: j<2. prefix[j] is 0 (target_2s). add cnt_s=1. result is 1. Then check prefix[j] is s (0). cnt_s becomes 2.

j=2: j >=2 (n-1=2). So no addition. Check if prefix[j] is 0. yes. cnt_s becomes 3.

So total result is 1 (from j=0 and j=1). Wait wait, j=0: when j=0, adding cnt_s (0). Then j=1 adds cnt_s=1 (from j=0's update). So total result is 0 +1 =1.

But the actual possible cuts are:

i=0, j=1: the three parts are [0], [0], [0]. So that's valid. So answer should be 1.

Which matches. So code works.

Another example: n=5, array [3, 0, 0, 0, 0]. Total sum is 3. So s=1. target_2s=2.

prefix sums: 3,3,3,3,3.

Check total sum 3, so s=1. So target_2s is 2. The code's loop:

for each j from 0 to 4:

At j=0: prefix is 3. Not 2. So no addition. Check if prefix is 1. No.

j=1: prefix 3. Not 2. Check s? No.

j=2: same.

j=3: same.

j=4: same.

So result is 0. Which is correct, because no way to split.

Another example: n=6, array [1, 2, 3, 0, 3, 3]. sum is 12. s=4, target_2s=8.

prefix array: 1,3,6,6,9,12.

Looking for j where prefix[j] =8. There are none. So result is 0. But sum is 12, which is 3*4. So need to split into three parts each sum 4.

Looking for possible splits. Let's see:

First part sum 4: possible at i=3 (sum 6 no). Wait, wait, prefix array is:

index 0:1, 1:3, 2:6, 3:6, 4:9, 5:12.

Wait, sum is 12. s=4. So first part sum 4. Looking for i where prefix[i] =4. There's none. So answer is 0.

So code correctly returns 0.

Another example where multiple j's contribute. Let's say array [1,1,1,0,0,0]. sum is 3. s=1, target_2s=2. prefix array is [1,2,3,3,3,3].

Looking for j where prefix[j] is 2. That's j=1. Then, j must be <5. So j=1. The cnt_s up to j-1 (0) is the number of s=1 in prefix[0..0]. prefix[0] is 1. So cnt_s is 1. So adds 1 to result. Then, for j=1, if prefix[j] is s (2 !=1), no. So cnt_s remains 1. Then for j=2, prefix is 3. not target. etc.

So result is 1. Is there a split? Let's see. j=1 (prefix[j] is 2). So first part sum is 1 (i=0), second part sum is 2-1=1, third part sum 1. So split after i=0 and j=1. So parts are [1], [1], [1,0,0,0]. Yes. So that's valid. So code works.

So the code seems correct.

Now, the code needs to be optimized for speed. Let's think about the prefix array. For n up to 1e5, it's O(n) time and space, which is acceptable. But in Python, using a list for prefix sums is manageable.

But perhaps we can compute the prefix sum on the fly, instead of storing the entire array. Because for each j, we only need the current sum to check for s and target_2s, and for the current prefix sum. Let's see.

Wait, but to compute the prefix sum for j, we need the sum up to j. So perhaps we can compute it incrementally. Let's see:

Initialize current_sum =0.

total_sum is sum(arr). So first, compute the total sum. But sum(arr) for 1e5 elements is O(n), which is acceptable.

Wait, but the problem is that the prefix sum for j is the sum of the first j+1 elements. So for the code to check for prefix[j] == s and target_2s, we can compute the cumulative sum on the fly.

Yes. Because in the code, when processing j, the current sum is the sum of the first j+1 elements. Because j is the index in 0..n-1, and the elements are 0-based.

Wait, let me clarify:

If the input array is [a0, a1, a2, ..., a(n-1)], then the prefix sum array is:

prefix[0] = a0

prefix[1] = a0 +a1

...

prefix[j] = sum_{0..j} a_i

But when processing j in 0 to n-1, the code for prefix sum can be computed incrementally.

So during the loop, we can keep track of current_sum, adding each element as we go.

Then, for each j, current_sum is prefix[j].

So in code:

current_sum =0

total_sum = sum(arr)

if total_sum %3 !=0: print(0); exit

s = total_sum //3

target_2s = 2*s

cnt_s=0

result=0

current_sum =0

for j in range(n):

   current_sum += arr[j]

   if j <n-1 and current_sum == target_2s:

       result += cnt_s

   if current_sum == s:

       cnt_s +=1

print(result)

Yes. Because for each j, current_sum is the sum up to the j-th element (inclusive). So this way, we don't need to store the entire prefix array. This saves memory, which is important for n=1e5. Storing a list of 1e5 integers is 1e5 * 4 bytes = ~400KB, which is manageable, but perhaps better to avoid it for the sake of memory optimization. But in Python, even 1e5 elements are manageable. But using this approach, we can compute the current sum on the fly, and save memory.

So the code can be optimized to not store the entire prefix array, but compute it step by step.

So the code would be as follows:

Read n.

Read the list of numbers.

Compute total_sum = sum(arr). If not divisible by 3, output 0.

Else, compute s and target_2s.

Initialize current_sum =0, cnt_s=0, result=0.

Loop through each element in the array, keeping track of current_sum:

for j in range(n):

   current_sum += arr[j]

   if j <n-1 and current_sum == target_2s:

       result += cnt_s

   if current_sum == s:

       cnt_s +=1

print(result)

Wait, but in this code, j is the index, and for each j, the current_sum is the sum of the first j+1 elements (since we start adding from arr[0], arr[1], etc.).

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    arr = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = sum(arr)
    if total % 3 != 0:
        print(0, file=output_stream)
    else:
        s = total // 3
        target_2s = 2 * s
        current_sum = 0
        cnt_s = 0
        result = 0
        for j in range(n):
            current_sum += arr[j]
            if j < n - 1 and current_sum == target_2s:
                result += cnt_s
            if current_sum == s:
                cnt_s += 1
        print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2 3 4 5
""",
            "output": \
"""\
0
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

Yes.

Another example: the [0,0,0] case.

n=3.

total_sum 0. s=0, target_2s=0.

current_sum:

j=0:

add 0 →0.

j <2 (yes). current_sum ==0. So add cnt_s (0). result 0.

current_sum ==0 → yes. cnt_s becomes 1.

j=1:

add 0 →0.

j<2 → yes. current_sum 0. So add cnt_s (1). result 1.

current_sum ==0 → yes. cnt_s becomes 2.

j=2:

add 0 →0.

j <2 → no (j=2, n-1=2). So no addition.

current_sum ==0 → yes. cnt_s becomes3.

Result is 1. Correct.

So this code works and is more memory efficient, as it doesn't store the entire prefix array. So it's better.

So the final code is as written above. It's O(n) time and O(1) space (apart from the input storage, but the problem allows us to read the input as a list, which is O(n) space). But since the code itself doesn't create any other data structures beyond the input list, it's optimal.

In Python, for n=1e5, this code will run in acceptable time. Also, sum(arr) is O(n), and the loop is O(n). So overall O(n) time.

So the code is correct and efficient.
</think>

```python
n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
if total % 3 != 0:
    print(0)
else:
    s = total // 3
    target_2s = 2 * s
    current_sum = 0
    cnt_s = 0
    result = 0
    for j in range(n):
        current_sum += arr[j]
        if j < n - 1 and current_sum == target_2s:
            result += cnt_s
        if current_sum == s:
            cnt_s += 1
    print(result)
```
