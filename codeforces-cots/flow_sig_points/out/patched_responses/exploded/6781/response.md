<think>
Okay, let's see. The problem is to find the number of magical subarrays in a given array. A magical subarray is one where all elements are the same because the minimum and maximum must be equal. So essentially, we need to count all the subarrays where all elements are equal.

Hmm, right. So the approach here is to look for consecutive runs of the same number. Because any subarray within a run is magical. For example, if there's a run of length k, then the number of subarrays in that run is k*(k+1)/2. Like, for a run of 3 elements, the subarrays are 3 of length 1, 2 of length 2, and 1 of length 3, total 6 which is 3*4/2 = 6.

So the plan is to traverse the array, group consecutive identical elements into runs, calculate the contribution for each run, and sum them all.

Let's think about the steps:

1. Iterate through the array and identify all consecutive runs of the same value.
2. For each run of length l, add l*(l+1)/2 to the total count.
3. Sum all these to get the answer.

Wait, yes. That's the way. Because each run contributes exactly l*(l+1)/2 subarrays. So for example, in the first sample input:

The array is 2,1,1,4.

The runs are:
- 2 (length 1) → 1
- 1 (length 2) → 2*3/2 = 3
- 4 (length 1) → 1

Total 1+3+1 =5. Which matches the sample output.

Another example, the second input has runs:
- -2, -2, -2 → length 3 → 3*4/2=6
- 0 → 1
- 1 →1
So 6+1+1=8? Wait, but the sample output is 8. Wait the second sample's output is 8, but according to the note, there are 8 magical subarrays, which includes the three runs plus the individual elements. Wait, the runs for the second sample are -2 three times, 0 once, 1 once. So 3*4/2=6 (from the first run) +1 (0) +1 (1) → 6+1+1=8. Which matches the sample. So this approach works.

So the key is to group the consecutive elements and compute the sum of their contributions.

So the algorithm is O(n) time, which is acceptable for n up to 1e5.

Now, how to implement this efficiently.

The steps in code:

Initialize total to 0.

Traverse the array, keeping track of the current run's value and length.

Start with the first element. current_value is a[0], current_length is 1.

Then, for each element from index 1 to n-1:

If the element is equal to current_value, increment current_length.

Else, add current_length*(current_length +1)/2 to the total. Then reset current_value and current_length to the new element (current_value = a[i], current_length=1).

At the end of the loop, don't forget to add the last run's contribution.

So, code outline:

n = int(input())
a = list(map(int, input().split()))
if n ==0:
    print(0)
else:
    total =0
    current = a[0]
    count =1
    for i in range(1, n):
        if a[i] == current:
            count +=1
        else:
            total += count*(count +1)//2
            current = a[i]
            count =1
    # add the last run
    total += count*(count+1)//2
    print(total)

Yes, this should work.

Testing the first sample:

Input array is [2,1,1,4].

Run 1: 2 (count=1) → added as 1*2//2=1.

Next element is 1: different. So add 1, then current becomes 1, count=1.

Then next element is 1 again → count becomes 2.

Then next is 4. Different. Add 2*3//2=3. Now total is 1+3=4. Then current is 4, count=1.

After loop, add 1 → total becomes 4+1=5. Correct.

Second sample input:

array is [-2,-2,-2,0,1].

First run: three -2's. count=3. Then when 0 is hit, add 3*4//2=6. Then 0 is count=1. Then 1 is different. Add 1*2//2=1. Then add 1 for 1. So total 6+1+1=8. Correct.

This should handle all cases. So the code is straightforward and efficient, O(n) time and O(1) space. Which is optimal.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
if not a:
    print(0)
else:
    total = 0
    current = a[0]
    count = 1
    for num in a[1:]:
        if num == current:
            count += 1
        else:
            total += count * (count + 1) // 2
            current = num
            count = 1
    total += count * (count + 1) // 2
    print(total)
```