<think>
Okay, so I need to solve this problem where I have to find the minimum number of operations to turn an array into a non-decreasing one. The operations allowed are choosing a range l to r and increasing each element in that range by 1. The goal is to minimize the number of such operations.

Let me start by understanding the problem. The key is that each operation can increment a contiguous subarray. So the challenge is figuring out how these operations can be arranged to reach the desired non-decreasing array with as few steps as possible.

Wait, but the problem doesn't specify that we need to reach a specific array. The array just needs to be non-decreasing. So the approach might involve modifying the original array to form a non-decreasing sequence in such a way that the required operations are minimized. Wait, no. Wait, the problem says we can convert array a into any arbitrary non-decreasing array. So we can choose what the target array is, as long as it's non-decreasing, and find the minimal steps to reach that target. But wait, no. Wait the problem statement says: "convert array a to an arbitrary array sorted in non-decreasing order". So the target is any non-decreasing array, and we need to find the minimal number of operations required to reach any such target.

Wait, but that's not correct. Because the problem allows the target array to be any non-decreasing array, so the minimal steps would be zero if the array is already non-decreasing. But the sample inputs show that the answer depends on how much we need to adjust the array. Wait, no. Wait, the problem is to find the minimal number of operations needed to turn the given array into a non-decreasing array. So the target is a non-decreasing array, but the problem allows any such array. So the problem is equivalent to finding the minimal number of operations required to make the array non-decreasing. But how do the operations work here? Because each operation can increment any range, but the increments are additive. So how can we model this?

Alternatively, maybe the problem requires us to find the minimal number of operations such that after applying them, the array is non-decreasing. Each operation is adding 1 to a subarray. So the minimal number of such operations.

Hmm. Let's think of the problem as similar to painting layers. Each operation corresponds to a certain range. The total number of layers (operations) covering each position i is the amount by which the original a[i] is increased. The sum of all the ranges' increments (each operation contributes 1 to each element in its range) must result in the final array being non-decreasing.

So the problem reduces to determining the minimal number of such ranges (operations) such that the sum of their contributions (each being 1 in their ranges) makes the array non-decreasing.

But since each operation can be any range, perhaps the minimal number of operations is determined by the differences between consecutive elements. Let's think in terms of the required increases for each element.

Suppose the original array is a[0], a[1], ..., a[n-1]. Let's imagine that the required target array is some non-decreasing array b[0] <= b[1] <= ... <= b[n-1], where each b[i] >= a[i], and the sum (b[i] - a[i]) is minimized. Wait, no, that's not necessarily the case. Because the problem allows the target array to be any non-decreasing array, not necessarily the one with minimal total increments. However, the problem is not to minimize the total increments, but the number of operations. So perhaps the minimal number of operations is achieved by having the target array as the minimal possible non-decreasing array (i.e., each element is as small as possible), but that's not obvious.

Alternatively, perhaps the problem can be approached by considering that each operation is a range increment. The minimal number of operations would be the sum of the "drops" in the required increments between consecutive elements.

Wait, let me think of the problem in terms of the required increments for each element. Let's say that for each element a[i], we need to add some value d[i] such that d[i] >=0 and the array (a[i] + d[i]) is non-decreasing. So, (a[i] + d[i]) <= (a[i+1] + d[i+1]) for all i.

The problem is to find the minimal number of operations (each being a range increment) such that the sum of the operations' ranges (each contributing 1) gives exactly the d[i] for each i.

But how can we model this? Because each operation is a contiguous range. So the d[i] array is the sum of all ranges that include i.

So, each operation is a range [l, r], and each such operation contributes +1 to each d[i] in l <= i <= r.

The minimal number of operations is the minimal number of such ranges that sum up to the required d array.

But how do we compute this minimal number?

Alternatively, perhaps the problem can be transformed into finding the required d array and then finding how many "steps" are required in the d array, similar to the way that in some problems, the number of operations is determined by the differences between adjacent elements.

Wait, let's consider the example given in the problem.

Sample 2:

3
3 2 1

The output is 2. The steps are:

First, increment positions 2-3 (0-based?), leading to [3,3,2]. Then increment position 3 to get [3,3,3]. So two operations.

The d array here is [0, 1, 2]. So the required increments are 0 for the first element, 1 for the second, and 2 for the third. So how do these increments translate into operations?

Each operation is a range that covers some elements. The sum of the ranges' contributions must equal the d array.

But how to model the minimal number of ranges. Let's see the d array for sample 2 is [0,1,2]. Let's think of the ranges as layers. For the second element (d[1] =1), it must be covered by 1 operation. The third element (d[2]=2) must be covered by two operations. The first element is covered by zero. So the ranges can be [1-2] (covering elements 1 and 2, adding 1 to each), then a range [2-2], adding 1 again. So two operations. Which matches the sample.

So the idea is that each time a higher d is needed than the previous element, we have to add some operations. The key is that the difference between consecutive elements in the d array (from right to left, perhaps) gives the number of new ranges needed.

Wait, let's think of the d array as follows. Let's process the array from left to right. The required d[i] can't be less than d[i-1] - (a[i] - a[i-1]). Wait, maybe this is getting complicated.

Alternatively, perhaps the minimal number of operations is equal to the sum of the positive differences between consecutive elements (from the original array) when processed from right to left.

Wait, for example, in sample 2: original array is [3,2,1]. Let's process from right to left. The third element is 1. The second is 2. To make 2 <= 1's target (which is 1), we need to increase the third element. But perhaps that's not the right way.

Wait, perhaps the required d array is such that (a[i] + d[i]) <= (a[i+1] + d[i+1]). So, the target array is non-decreasing. To find the minimal number of operations, we need to choose the d array such that it's as "smooth" as possible, allowing for the minimal number of operations.

But how?

Alternatively, the problem is similar to the problem where you have to paint the skyline with horizontal brush strokes. The minimal number of strokes is the sum of the differences in heights between adjacent columns, but only when the height increases. Wait, that's a different problem, but maybe a similar approach applies here.

In that problem, the minimal number of strokes is the sum of the positive differences between each column's height and the previous column. For example, if the heights are [3, 1, 2, 4, 3], the strokes would be 3 + (2-1) + (4-2) = 3+1+2=6. But how does that relate to our problem?

Wait, in the painting problem, each stroke is a horizontal line of a certain height. Each stroke can cover a consecutive sequence of columns, but you can't have gaps. So the minimal number of strokes is determined by the "peaks" that require new strokes.

In our current problem, each operation is a range increment, which is equivalent to adding a "layer" that covers a contiguous range. Each layer contributes 1 to each element in the range. The sum of these layers is the d array. The minimal number of layers (operations) required to achieve a certain d array.

So, how to model the layers. Let's think of the layers as being applied in a certain order. Each layer is a range [l, r]. The d array is the sum of all layers that include each position.

The key insight here is that the required d array must be such that the difference between consecutive elements in the d array can be used to determine how many new layers must start or end at each position.

Alternatively, perhaps the minimal number of operations is the sum of the differences between consecutive elements in the d array where the current element is higher than the next. Wait, maybe not. Let me think again.

Suppose that the required d array is non-decreasing. Then, each time the d increases, you need to add some layers. Wait, maybe not. Let's take the sample 2: the d array is [0,1,2]. This is increasing. The number of operations is 2, which is the sum of the differences between consecutive elements? No. The differences here are 1 and 1, sum is 2. Which matches the answer.

Another example: sample 3. The original array is [7,4,1,47]. The sample output is 6.

The d array for this sample would be [0, 3, 6, 0]. Because 7+0=7, 4+3=7, 1+6=7, 47+0=47. So the target array is [7,7,7,47], which is non-decreasing. The d array is [0,3,6,0]. Wait, but the third element's d is 6 (since 1+6=7), and the fourth's d is 0. Wait, but 7 <=47, so that's allowed. So the d array is [0,3,6,0]. But then, how to model the layers here.

To get the d array as [0,3,6,0], the layers need to add 3 to the second element, 6 to the third, and 0 to the fourth. So the layers would be:

Three operations covering positions 2 and 3 (elements 2 and 3 in 1-based, which are 4 and 1 in the original array). Then three operations covering just position 3.

So total 3 +3=6 operations. Which matches the sample.

So the d array here is [0,3,6,0]. The difference between the third and second element is 3 (6-3=3), which is the number of operations that start at position 3. The difference between the second and first is 3 (3-0=3), which is the number of operations that start at position 2. The difference between the fourth and third is -6 (0-6=-6), which would be the number of operations ending at position 3.

Hmm. Maybe the correct approach is to compute the required d array, then find the number of operations by looking at the differences between adjacent elements in the d array.

Wait, the way to model the layers is that each time the required d increases, you start a new set of operations. For example, in the sample where the d array is [0,1,2], the first element is 0, then 1 (difference +1), then 2 (difference +1). So each of these increases requires adding a new layer that starts at that position and continues until the end. So the first layer would be from position 2 to 3 (since 0 to 1 is +1), and the second layer from position 3 to 3 (since 1 to 2 is +1). So two operations.

Wait, but how does that model the layers. Let's see:

For the sample 2:

d array is [0,1,2].

The difference between d[1] and d[0] is +1. So that means we need to add 1 operation that starts at position 1 and extends to the end. Then, the difference between d[2] and d[1] is +1, which requires adding 1 operation that starts at position 2 and extends to the end. So total 2 operations.

So the layers are [1,3] (covers elements 1, 2, 3 in 1-based), but wait that's not possible. Wait, no. The first operation starts at position 2 (second element) and goes to the end. Wait, perhaps the approach is to process the array from left to right, and for each position, compute the required number of new layers as the difference between current d[i] and d[i-1].

Wait, let's think of it as follows. The required d[i] for each position. The minimal number of operations is equal to the sum of all the increases in the d array as we go from left to right. Because each time the required d[i] is higher than d[i-1], we need to add (d[i] - d[i-1]) new layers that start at i and cover to the end. Because each of those layers will contribute 1 to all positions from i onwards. So, for each position i, the number of new layers added is (d[i] - d[i-1]). The sum of all these positive differences gives the total number of operations.

Yes, that makes sense. Let's test this with the samples.

Sample 2: d array is [0,1,2]. The differences from left to right are 0 (from d[0] to d[1] is 1-0=1), then 1 (d[2]-d[1] =1). Sum is 1+1=2. Which matches the sample.

Sample 3: d array is [0,3,6,0]. The differences from left to right are 3-0=3, then 6-3=3, then 0-6= -6 (but we ignore negative differences). So the sum is 3+3=6. Which matches the sample.

Another example: if the array is already non-decreasing, then the d array would be all zeros, so the sum of differences is zero. Which matches the first sample.

So this approach seems to work.

So the steps to solve the problem would be:

1. Compute the required d array such that the array (a[i] + d[i]) is non-decreasing. The d array is the minimal increments needed, but how?

Wait, but the problem allows any non-decreasing target array. So the choice of d array can vary as long as (a[i]+d[i]) is non-decreasing. However, the minimal number of operations depends on how we choose the d array. For instance, perhaps a certain d array would result in a lower sum of increases than another, leading to fewer operations. So the problem is to choose the d array such that the sum of (d[i] - d[i-1]) for all i where d[i] > d[i-1] is minimized.

Wait, but how to compute such a d array.

Ah, but here's the key: the minimal number of operations is achieved by choosing the d array such that each d[i] is exactly the maximum between (d[i-1] - (a[i] - a[i-1])) and 0). Because this ensures that (a[i] + d[i]) >= (a[i-1] + d[i-1]), making the array non-decreasing. Wait, let's think about that.

Let me formalize. The target array must satisfy:

a[i] + d[i] >= a[i-1] + d[i-1] for all i >=1.

Rearranging:

d[i] >= (a[i-1] + d[i-1]) - a[i].

But since d[i] >=0, the minimal possible d[i] is max( (a[i-1] + d[i-1] - a[i]), 0 ). Because if (a[i] >= a[i-1] +d[i-1]), then d[i] can be zero. Otherwise, d[i] must be (a[i-1] +d[i-1] - a[i]).

Wait, perhaps not. Let's see:

Let me re-arrange the inequality:

a[i] + d[i] >= a[i-1] + d[i-1]

=> d[i] >= (a[i-1] - a[i]) + d[i-1]

But (a[i-1] - a[i]) could be negative. For example, if a[i] > a[i-1], then (a[i-1] - a[i]) is negative. So d[i] can be as low as (a[i-1] - a[i] + d[i-1]), but since d[i] can't be negative, the minimal possible d[i] is max( (a[i-1] + d[i-1] - a[i]), 0 ). This ensures that the target array is non-decreasing, and the d array is as small as possible to allow for minimal operations.

But how does this affect the sum of the (d[i] - d[i-1]) increments?

Wait, the sum is the sum of the increases in d[i] over d[i-1], which is exactly the minimal number of operations. So by choosing the d array in this way, we can compute the minimal possible sum.

So the algorithm is:

Compute the d array as follows:

Initialize d[0] = 0.

For each i from 1 to n-1:

required_prev = a[i-1] + d[i-1]

current_required = required_prev - a[i]

if current_required > 0:

d[i] = current_required

else:

d[i] = 0

Wait, no. Wait, let's see:

The target array must satisfy:

a[i] + d[i] >= a[i-1] + d[i-1]

=> d[i] >= (a[i-1] + d[i-1] - a[i])

But since d[i] can't be negative, so d[i] is the maximum between 0 and (a[i-1] + d[i-1] - a[i]).

Wait, but that's not correct. Because (a[i-1] +d[i-1] - a[i]) can be negative, so the minimal d[i] is zero.

Wait, for example, if a[i] is larger than a[i-1] +d[i-1], then even with d[i] =0, the target array would have a[i] +d[i] = a[i] >= a[i-1] +d[i-1], which is allowed.

So in this case, d[i] can be zero. But if a[i] is less than a[i-1] +d[i-1], then d[i] must be (a[i-1]+d[i-1] -a[i]).

So the correct way to compute d[i] is:

d[i] = max( (a[i-1] + d[i-1] - a[i]), 0 )

So that's how the d array is built. Then, the number of operations is the sum of the differences (d[i] - d[i-1]) for all i where d[i] > d[i-1]. Wait, but how?

Wait, the d array is built in a way that ensures that each d[i] is as small as possible. Then, the sum of the positive differences between consecutive d[i]s (from left to right) gives the number of operations.

Wait, for example:

Sample 2:

Original a is [3,2,1]

Compute d array:

d[0] =0.

For i=1 (second element, a[1] =2):

required_prev =3 +0 =3.

current_required =3-2 =1. So d[1] =1.

For i=2 (third element, a[2]=1):

required_prev =2 +1 =3.

current_required =3-1 =2. So d[2] =2.

d array is [0,1,2]. The sum of positive differences (1-0=1, 2-1=1) gives 2 operations.

Sample3:

Original a is [7,4,1,47].

Compute d array:

d[0] =0.

i=1 (a[1]=4):

required_prev =7+0=7.

current_required =7-4=3. So d[1] =3.

i=2 (a[2]=1):

required_prev =4+3=7.

current_required=7-1=6. So d[2]=6.

i=3 (a[3]=47):

required_prev=1+6=7.

current_required=7-47= -40. So d[3]=0.

d array is [0,3,6,0].

The differences are 3-0=3, 6-3=3, 0-6= -6. Sum of positive differences is 3+3=6.

Which matches the sample.

Another test case:

Sample1:

Original a is [1,2,3]. d array is [0,0,0]. Sum of differences is 0. Correct.

So the algorithm is:

- Compute the d array as follows:

   d[0] =0

   for each i from 1 to n-1:

       d[i] = max( a[i-1] + d[i-1] - a[i], 0 )

- Then, compute the sum of (d[i] - d[i-1]) for all i where d[i] > d[i-1].

But wait, how does this sum equal the minimal number of operations?

Because each time d[i] is larger than d[i-1], the difference (d[i] -d[i-1]) is the number of new operations that must start at position i and cover the range from i to the end. Because each such operation will add 1 to all elements from i onwards. For example, if d[i] is d[i-1] + k, then k operations must start at i. Each of these operations covers the range i to n-1. Thus, each of these k operations contributes 1 to the d values of i, i+1, ..., n-1. So the sum of these k operations is accounted for in the d array.

This approach works because each operation's contribution is a contiguous range. The minimal number of operations is achieved by starting as many operations as needed at the earliest possible position (i.e., when the required d increases).

So the steps are:

1. Compute the d array as per the formula.

2. Sum all (d[i] - d[i-1]) for i where d[i] > d[i-1].

Thus, the code can be written as follows.

Now, considering the constraints. The maximum n is 1e5, so the code must be O(n) time and O(n) space. However, since the d array can be computed in a single pass, and we can keep track of the previous d value, we can do this in O(1) space, except for storing the array a.

Wait, but the code needs to compute the d array, but since each d[i] depends only on the previous d[i-1], we can compute it in a single variable, keeping track of the current d. Let's see.

Initialize prev_d =0.

sum_operations =0

for each i from 1 to n-1:

    required_prev = a[i-1] + prev_d

    current_d = max( required_prev - a[i], 0 )

    if current_d > prev_d:

        sum_operations += (current_d - prev_d)

    else:

        pass

    prev_d = current_d

Wait, no. Wait, the code should compute the sum of (current_d - previous_d) only when current_d is larger than the previous d. Because the d array is being built in a way that each element depends on the previous, but the previous is the d[i-1], not the previous element in the array.

Wait, no. For example, in the d array [0,1,2], the current_d for i=1 (second element) is 1. prev_d is 0. So sum_operations increases by 1. For i=2, current_d is 2, which is larger than prev_d (1). So sum increases by 1. Total 2.

But in the code above, the previous_d for each step is the current_d of the previous element. So for i=1, the previous_d is 0 (from i=0). Then, after i=1, previous_d becomes 1. For i=2, current_d is 2. So sum += 2-1=1. Which is correct.

So the code would compute the sum correctly.

But wait, the code as written would process the elements starting from index 1 (assuming 0-based a array). Let's see.

But in the problem statement, the array is 1-based. But in code, it's 0-based.

Let me rephrase:

Suppose the input is n elements, stored as a list (0-based) a[0..n-1].

We need to compute d for each element from 0 to n-1.

But the first element (a[0]) can have d[0] =0, since there's no element before it. The target is a non-decreasing array, so the first element can stay as is.

Then for each i from 1 to n-1:

d[i] = max( a[i-1] + d[i-1] - a[i], 0 )

So the code can compute d as follows:

prev_d =0

sum_ops =0

for i in range(1, n):

    required_prev = a[i-1] + prev_d

    current_d = max( required_prev - a[i], 0 )

    sum_ops += max( current_d - prev_d, 0 )

    prev_d = current_d

Wait, but in the first step, when i=1, prev_d is 0. current_d is computed as a[0] +0 -a[1], if that's >=0. Then sum_ops increases by current_d -0, but only if current_d > prev_d (0).

Wait, but in sample 3:

After processing i=1 (second element, a[1] =4), current_d is 3. prev_d was 0. sum_ops +=3.

Then i=2, a[2]=1. required_prev =4 +3 =7. current_d =7-1=6. sum_ops +=6-3=3. sum is now 6.

i=3, a[3]=47. required_prev=1+6=7. current_d=7-47= -40 → 0. sum_ops +=0-6 → no, but we take max(0-6,0) → 0. So sum remains 6.

Which is correct.

So the code would work as follows.

Thus, the steps are:

Read n.

Read the array a.

Initialize prev_d =0.

sum_ops =0.

Loop from i=1 to n-1:

   required_prev = a[i-1] + prev_d

   current_d = max( required_prev - a[i], 0 )

   sum_ops += max( current_d - prev_d, 0 )

   prev_d = current_d

Finally, print sum_ops.

This is O(n) time and O(1) space, which is acceptable for n=1e5.

So the code can be written as:

Read n.

Read list a.

prev_d =0

res=0

for i in range(1, n):

    required_prev = a[i-1] + prev_d

    current_d = max( required_prev - a[i], 0 )

    res += max(current_d - prev_d, 0)

    prev_d = current_d

print(res)

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    prev_d = 0
    result = 0
    for i in range(1, n):
        required_prev = a[i-1] + prev_d
        current_d = max(required_prev - a[i], 0)
        result += max(current_d - prev_d, 0)
        prev_d = current_d
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
7 4 1 47
""",
            "output": \
"""\
6
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

Sample3:

n=4.

a = [7,4,1,47].

i=1: a[0] =7.

required_prev =7+0=7. current_d=7-4=3. res +=3-0=3.

i=2: a[1] is4. required_prev=4+3=7. current_d=7-1=6. res +=6-3=3 → sum is6.

i=3: a[2]=1. required_prev=1+6=7. current_d=7-47= -40 →0. res +=0-6 → no, because current_d is0, prev_d is6. 0-6 is -6. max( -6,0) is 0. So res remains6.

So code returns 6. Correct.

Another test case: sample1. a = [1,2,3].

i=1: required_prev =1+0=1. a[1] is2. current_d=1-2 =-1 →0. res +=0-0=0.

i=2: required_prev =2+0=2. a[2] is3. current_d=2-3 =-1→0. res +=0-0=0. So sum is0. Correct.

Another test case: let's say a is [5,4,3,2,1]. The required d array would be [0,1,2,3,4]. The sum of the differences is (1)+(1)+(1)+(1) =4. So the code would output4.

Each operation would be adding a new layer starting at each position.

So, the code seems correct.

Thus, the solution is to compute the sum of the positive differences between consecutive d values as computed by the formula.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
prev_d = 0
result = 0
for i in range(1, n):
    required_prev = a[i-1] + prev_d
    current_d = max(required_prev - a[i], 0)
    result += max(current_d - prev_d, 0)
    prev_d = current_d
print(result)
```
