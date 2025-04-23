<think>
Okay, let's see. The problem is about dividing a pizza (which is a circle cut into n pieces) into two continuous sectors such that the difference between their angles is minimized. Oh right, the sectors have to be continuous. So like, all the pieces in each sector must form a contiguous block. So the idea is to find two adjacent sectors that split the circle into two parts, right?

Wait, but how do we model this? The pizza is a circle, so the pieces are arranged in a circular manner. So any split would create two continuous sectors. For example, if the pieces are in a circle like 1, 2, 3, 4 (each 90 degrees), then splitting between 2 and 3 gives one sector as 1+2 and the other as 3+4. But splitting between 4 and 1 would give sectors like 4 and 1+2+3, etc. So we need to consider all possible starting points for the split and compute the sum of consecutive pieces until the split wraps around.

The minimal difference is the minimal possible absolute difference between the sum of one sector and the sum of the other. But since the total is 360, the other sector would be 360 minus the sum of the first. So the difference would be |a - (360 - a)| = |2a - 360|. Which simplifies to 2*|a - 180|. So to minimize the difference, we need to find the a (sum of a continuous sector) that is as close as possible to 180.

Wait, right. Because the minimal difference would be when a is 180, giving a difference of 0. So the problem reduces to finding the maximum possible sum of a continuous sector that does not exceed 180, and then compute the difference as 360 - 2*max_sum. Or wait, wait. Let me think again. The difference is |a - (360 -a)| = |2a -360|. To minimize this, we need a to be as close as possible to 180. So the minimal possible difference is 360 - 2*max_possible_sum if the max sum is <=180. Or if there's a sum exactly 180, then difference is zero.

So the approach is: find all possible continuous sectors (in the circular arrangement) and compute their sum. Then find the maximum sum that is <= 180. The minimal difference is 360 - 2 * this maximum sum. If any sum is exactly 180, then the answer is 0. Otherwise, the next best is the maximum sum less than 180, and the difference is 360 - 2*sum.

So the key is to find the maximum possible sum of a continuous arc (in the circular arrangement) that is <=180.

So how do we compute all possible continuous sectors in a circular array efficiently?

Hmm. The pizza is circular, so the array is circular. So for each possible starting index i, and for each possible length j (from 0 to n-1), compute the sum of j consecutive elements starting at i. Then check if any of those sums is 180. If yes, answer is 0. Else, the maximum sum less than or equal to 180, and then compute 360 - 2*sum.

But with n up to 360, doing this naively would be O(n^2) which is acceptable. Let's see: 360^2 is 129600 operations, which is manageable in Python within 1 second.

So the steps:

1. Generate all possible continuous segments in the circular array. For each possible starting index, and each possible number of consecutive elements (from 1 to n-1, since taking all n elements would sum to 360, which is the total, but 360-360 is 0, but since 360 is twice 180, the difference would be 360 - 2*360 = -360, absolute is 360. But that's not helpful. So perhaps the maximum sum is 180, so we need to check for segments of sum up to 180.

Wait, but the sum can't exceed 360. So for each possible continuous segment (in the circular array), compute the sum. Then, for each sum, if it's <=180, track the maximum. Then the minimal difference is 360 - 2*max_sum.

But how to compute all possible continuous segments efficiently.

Alternatively, since the array is circular, we can break it by doubling the array (like for circular buffer handling) and then compute all possible contiguous subarrays of length up to n-1.

For example, for a circular array of [a0, a1, a2], doubling it to [a0, a1, a2, a0, a1, a2], then for each start index from 0 to n-1, and for lengths from 1 to n-1, compute the sum. But this is O(n^2) time. Which for n=360 is 360*360=129600 operations. Each sum can be computed with a sliding window.

Alternatively, precompute a prefix sum array, then for each start and end, compute the sum.

Yes. So here's an approach:

Compute the prefix sum array of the doubled array. Then for each possible start index in 0 to n-1, and for each possible end index (start + 1 to start + n-1), compute the sum of elements from start to end-1 (assuming prefix sum is 0-based). Then check if the sum is <=180 and track the maximum.

But the doubled array approach would have a prefix sum array of size 2n. Let's see.

Alternatively, since the array is circular, for each possible starting index i (0-based), and for each possible number of elements k (from 1 to n-1), the sum is the sum of the elements starting at i, then i+1, ... (mod n) for k elements. So the sum can be computed by the sum of the elements from i to i +k -1 mod n.

But handling this with mod can be tricky, but perhaps using the prefix sum array for the original array (non-doubled), and then for any i and j (i < j) the sum is prefix[j] - prefix[i]. For circular segments where j > n, j mod n, but that's more complicated.

Alternatively, considering that the circular array can be represented as a linear array by considering that the starting index can be anywhere, and the elements wrap around. So to make it easier, we can create a list that is the original array concatenated with itself. Then for any starting index in the original array (0 to n-1), and for any length from 1 to n-1, we can take elements from the starting index up to start + length -1 in the doubled array. If the start + length exceeds n, then we can take modulo or whatever, but in the doubled array, this is straightforward.

So for example, the original array is [a0, a1, a2], doubled is [a0, a1, a2, a0, a1, a2]. Then for start index 2 (which is a2) and length 2, the elements are a2 and a0 (since 2 to 3 is a2, a0 in the doubled array). The sum is a2 +a0. So this would correctly handle the wrap-around.

So for each start in 0 to n-1, and for each length in 1 to n-1, the sum is the sum of elements from start to start + length -1 in the doubled array.

But how to compute this sum efficiently. The straightforward way is O(n^3) if for each start and length, we compute the sum by iterating. But that would be O(n^2) time. Wait, for each start in 0..n-1, and for each length 1..n-1, the sum is the sum of the next 'length' elements. So if we precompute the prefix sums, then for any start and length, the sum is prefix[start + length] - prefix[start]. But since the doubled array is length 2n, the start + length can be up to 2n.

So here's the plan:

1. Create a doubled array of 2n elements, which is the original array concatenated with itself.

2. Compute the prefix sum array of the doubled array. Let's call it prefix, where prefix[0] = 0, prefix[1] = a0, prefix[2] = a0 +a1, etc., up to prefix[2n] which is sum of 2n elements.

3. Then for each start in 0..n-1 (original array indices), and for each possible length from 1 to n-1:

   a. The end index in the doubled array is start + length.

   b. The sum is prefix[end] - prefix[start].

   c. Check if this sum is <=180. If yes, track the maximum.

4. After checking all possible start and length pairs, the maximum sum <=180 is found. The minimal difference is 360 - 2*max_sum.

But why do we need to consider all lengths up to n-1? Because taking all n elements would give sum 360, which when subtracted from 360 gives 0, but 360 is over 180, so the difference would be 360-0 = 360. But that's not better than any sum less than 180. For example, if all elements sum to 360, but that's the entire pizza. Then one sector is 360 (all pieces) and the other is 0. The difference is 360, which is the maximum possible. So in that case, the code would not consider length n, so the maximum sum would be the maximum sum of a sector with length up to n-1. Which could be, for example, 170, leading to difference 360 - 2*170=20. But if the entire pizza is 360 (n=1), then there's no other option. So in the case where n=1, the code would check all possible lengths up to 0 (since n-1=0) which is invalid. Wait, but in that case, how does it handle the case where one sector is all the pizza and the other is empty.

Wait, the problem says that one of the sectors can be empty. So when the pizza is split into two sectors, one can be empty and the other is the entire 360. But in that case, the difference is 360. But according to the problem's third sample, when n=1, the answer is 360. So how does the code handle that?

Ah, because in the code's approach, when n=1, the possible lengths to check are 1-1=0, but length starts from 1. So for n=1, the code would loop for start in 0 (n=1) and for length in 1 to 0, which is invalid. So no sums are considered. Then max_sum remains 0. Then the minimal difference is 360 - 2*0 = 360. Which matches the sample.

Wait, but the code would need to handle that case. Let's see: when n=1, the code's loop is:

for start in 0 to n-1 (0 to 0):

   for length in 1 to n-1 (1 to 0) → loop doesn't run.

So in this case, the code's maximum sum remains zero (since initial max_sum is initialized to 0). So 360 - 2*0 = 360. Which is correct.

So the code would handle the n=1 case correctly.

So how do we compute all possible possible sums of continuous segments (with length up to n-1). Then among those, find the maximum sum that is <=180. Then compute 360 - 2*max_sum.

But wait, what about the case where the maximum sum is exactly 180? Then the difference is zero, which is optimal.

Yes.

So the approach is:

- Precompute all possible continuous segments (with lengths from 1 to n-1) and compute their sum. Also, for the case where one of the sectors is empty (so sum is 0 or 360). But the code's approach automatically includes the sum of 0 (if allowed), but the code is looking for the maximum sum <=180. However, for the case where the sum is 360, which is the entire pizza, but since the code only considers lengths up to n-1, the code's loop doesn't include that. But the code's initial max_sum is 0, which would not capture the case where one sector is 360 (sum 360) and the other is 0. But according to the problem statement, when n=1, that's the only possibility. So how does the code handle it?

Wait, in the code's approach, when n=1, the loop for start in 0 (n-1=0) and length in 1 to 0 (n-1=0) → the inner loop doesn't run. So no sums are computed. So the max_sum remains 0. Then the code computes 360 - 2*0 = 360, which is correct. So that's okay.

But in the general case, if all possible sums are considered except the entire 360. Wait, but the entire pizza is not considered. So the code doesn't check the sum of all n elements (which would be 360). But when the code computes the maximum sum, the entire pizza's sum is 360, but since we are looking for sums <=180, 360 is not considered. So that's correct.

So the code's approach is correct.

Now, the steps:

1. Read n and the array a.

2. If n is 1, then the answer is 360. Wait, no. According to the sample input 3, when n=1, the output is 360, which is correct. Because the sum of one sector is 360 and the other is 0. The difference is 360-0=360. So the code's approach gives that.

3. Else, compute the doubled array, compute the prefix sums, then for each start in 0..n-1, and length 1..n-1:

   a. compute sum as prefix[start + length] - prefix[start]

   b. if sum <=180, track the maximum sum.

4. The minimal difference is 360 - 2 * max_sum.

So for example, in the first sample input:

4

90 90 90 90

The code would check all possible start and lengths. For start 0 and length 2, sum is 90+90=180. So the maximum sum is 180, difference is 0.

In the fourth sample input:

4

170 30 150 10

The array is 170,30,150,10. The sum of 170+10 (start=0, length 2? Wait, the doubled array is [170,30,150,10,170,30,150,10]. For start=3 (which is the original 10), and length=2. So start=3, end=5 (3+2=5). The sum is prefix[5] - prefix[3]. The prefix sums would be:

prefix[0] =0

prefix[1] =170

prefix[2] =200

prefix[3] =350 (170+30+150)

prefix[4] =360 (350+10)

prefix[5] =530 (360+170)

prefix[6] =560 (530+30)

prefix[7] =710 (560+150)

prefix[8] =720 (710+10)

So start=3 (original 10), length=2 → start=3, end=5. The sum is prefix[5] - prefix[3] = 530 - 350 = 180. So that's another way to get sum 180. So the code would output 0.

But wait, how does the code find that sum? Let's see. The original array is 170,30,150,10. The start can be index 3 (which is 10) in the original array, and length 2. So the elements are 10 (start=3) and 170 (start+1=4 in the doubled array). So sum is 10+170=180. Which is correct, and the code will find that sum, leading to difference 0.

So the code's approach works.

Now, how to implement this efficiently in Python.

First, read n and the array a.

Then, create the doubled array as a + a.

Compute the prefix sum array.

Then, for each start in 0 to n-1:

   for length in 1 to n-1:

       end = start + length

       sum = prefix[end] - prefix[start]

       if sum <=180, check if it's larger than current max_sum.

But for n up to 360, this is 360 * 359 = 129,240 iterations. Each iteration is a subtraction and a comparison. Which is manageable.

But perhaps we can optimize by precomputing the prefix sum once.

So the code steps:

Read n.

Read a as a list of integers.

If n == 0: impossible as per constraints.

Compute the doubled array: doubled = a + a.

Compute prefix sums. For example:

prefix = [0] * (len(doubled) +1)

for i in range(len(doubled)):

    prefix[i+1] = prefix[i] + doubled[i]

Then, max_sum = 0.

for start in range(n):

    for length in range(1, n):

        end = start + length

        current_sum = prefix[end] - prefix[start]

        if current_sum > 180:

            continue

        if current_sum > max_sum:

            max_sum = current_sum

        if max_sum == 180:

            break  # can't get better than this

    if max_sum ==180:

        break  # exit early

result = 360 - 2 * max_sum

print(result)

Wait, but in Python, breaking out of the inner loop once a sum of 180 is found can save some time. So once any sum of 180 is found, the code can break early and return 0 as the minimal difference.

Yes. So the code can check if current_sum is 180, and set max_sum to 180 and break out of all loops.

So the code can be optimized by breaking early once a sum of 180 is found.

Now, let's check for the fourth sample input. The sum is 180, so the code will find it quickly.

This approach should be efficient enough.

Now, let's code this.

But wait, in Python, list concatenation is easy. So a + a will create the doubled array. Then the prefix sum can be computed with a loop.

Let's code this.

Sample code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    if n == 1:
        print(360, file=output_stream)
        return

    doubled = a + a
    prefix = [0] * (len(doubled) + 1)
    for i in range(len(doubled)):
        prefix[i+1] = prefix[i] + doubled[i]

    max_sum = 0
    found_180 = False

    for start in range(n):
        for length in range(1, n):
            end = start + length
            current_sum = prefix[end] - prefix[start]
            if current_sum == 180:
                max_sum = 180
                found_180 = True
                break
            if current_sum < 180 and current_sum > max_sum:
                max_sum = current_sum
        if found_180:
            break

    print(360 - 2 * max_sum, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
100 100 160
""",
            "output": \
"""\
40
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

Sample 3:

n=1 → code prints 360.

Sample 4:

After creating the doubled array, the code checks start=3 (original index 3, which is 10). Then length=2: start+length=5. The prefix[5] is 170+30+150+10+170= 530. prefix[3] is 170+30+150=350. 530-350=180. So code breaks and returns 0.

Yes.

Another sample: input 3 → 100 100 160. The possible continuous segments:

For example, starting at 0, length 2: 100+100=200 → over 180. So no.

Check all possible starts and lengths.

The maximum sum <=180 would be 100+100=200 (but that's over), but wait. What's the correct answer here?

The sample input is 3, 100,100,160. The sum is 360. The optimal split is 100+100=200 (but that's over 180). So the code would look for the maximum sum <=180. Let's see:

Possible sums:

Each individual element:

100 → possible. 100, 100, 160. So max is 160.

Sum of two elements: 100+100=200 (over), 100+160=260 (over), 160+100=260 (over). So no.

Sum of three elements (but code only checks up to n-1=2 elements). So code only checks lengths up to 2.

Wait, in this case, the code will find the maximum sum as 160 (the third element). So the difference is 360-2*160=360-320=40, which matches the sample.

Yes. So code works.

Another case: sum of 180. So the code will return 0.

So the code seems correct.

Now, code the solution with the steps. Also, handle the case when n is 1.

So the code:

Read n.

Read list a.

If n ==1:

    print(360)

Else:

    proceed with the code.

Now, code in Python.

But let's see for n=2. For example, n=2, a=[180, 180]. Then possible sums are 180 (each single element). So the maximum sum is 180. Difference is 0.

Yes.

Another case: n=2, a=[170, 190]. Then possible sums are 170 (sum of first element) and 190 (sum of second element). But 190 is over 180, so max is 170. Difference is 360-2*170=20.

But since the array is circular, for start=1, length=1: sum is 190 (which is over 180, so not considered). So the code's approach works.

Yes.

Thus, the code should handle all cases correctly.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(360)
    exit()

doubled = a + a
prefix = [0] * (len(doubled) + 1)
for i in range(len(doubled)):
    prefix[i+1] = prefix[i] + doubled[i]

max_sum = 0
found_180 = False

for start in range(n):
    for length in range(1, n):
        end = start + length
        current_sum = prefix[end] - prefix[start]
        if current_sum == 180:
            max_sum = 180
            found_180 = True
            break
        if current_sum < 180 and current_sum > max_sum:
            max_sum = current_sum
    if found_180:
        break

print(360 - 2 * max_sum)
```
