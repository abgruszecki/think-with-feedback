<think>
Okay, let's see. The problem is to split the array into three parts such that the sum of the first and third parts are equal, and we need to maximize that sum. Hmm.

So, the maximum possible sum1 and sum3. The approach here is probably to find the largest possible sum where the sum from the left and the sum from the right can meet in the middle. Oh right, because the parts are contiguous. So maybe we can use two pointers, one starting at the beginning and the other at the end, accumulating sums and trying to find when they are equal.

Let's think. Let's have a left sum and a right sum. We start by adding elements from the left to sum1 and elements from the right to sum3. We want to find the maximum sum where these two are equal, and the pointers haven't crossed each other. Because once they cross, the parts would overlap, which isn't allowed.

So here's an idea: Initialize left pointer at 0 (sum1 is 0), right pointer at n-1 (sum3 is 0). Then, we start adding elements to sum1 and sum3. If sum1 is less than sum3, we move the left pointer forward. If sum3 is less than sum1, we move the right pointer backward. If they are equal, we record the sum and then move either pointer (but we need to check which one to move next). Wait, but once they are equal, we can check if that's the maximum so far, and then try to add more elements on both sides to see if a larger sum exists.

Wait, let's take the first example: [1,3,1,1,4]. The left starts adding 1, sum1 is 1. Right adds 4, sum3 is 4. Since sum1 < sum3, move left to add 3 (sum1 becomes 4). Now sum3 is 4, which is equal. So we record 4. Then, can we move both? Maybe. Then, sum1 becomes 4+1=5, sum3 is 4+1=5. Now they are equal again. So the maximum sum is 5. So the pointers would have to cross, but we need to check if the left pointer is still to the left of the right pointer. So in this case, when sum1 and sum3 are equal, we can take that sum as a candidate for maximum, and then continue by adding more elements to sum1 and sum3 again.

Wait, but once the sum1 and sum3 are equal, how do we proceed? Maybe in this case, we can add the next element from both ends. Let's think of the algorithm steps:

Initialize left = 0, right = n-1, sum1 = 0, sum3 = 0, max_sum = 0.

While left <= right:
    if sum1 < sum3:
        add d[left] to sum1, left += 1
    else:
        add d[right] to sum3, right -=1
    if sum1 == sum3:
        max_sum = sum1

But wait, this might not capture all possibilities. Let's test this with the first example.

Initial sum1=0, sum3=0. They are equal, so max_sum is 0. Then, since sum1 is equal to sum3, we can add from either side. But in the algorithm above, when sum1 and sum3 are equal, the code would add from the left because if sum1 <= sum3, it's handled by the 'else' clause. Wait, no. The code checks if sum1 < sum3. If not, then it adds to sum3. Wait, no, the code is:

If sum1 < sum3: add to sum1 (left), else: add to sum3 (right). Wait, no. The code is:

If sum1 < sum3:
    add to sum1 (left)
else:
    add to sum3 (right)

So when sum1 and sum3 are equal, the else clause is taken. So in the first step, sum1 and sum3 are both 0. So we go into the else clause, add d[right] (4) to sum3. sum3 becomes 4, right becomes 4-1=3. Now sum1=0, sum3=4. Now sum1 < sum3, so add left (1) to sum1 (sum1 becomes 1), left becomes 1. Then, sum1 is 1, sum3 4. So add left (3) to sum1 (sum1=4, left=2). Now sum1 equals sum3 (4). So set max_sum to 4. Then, since sum1 is not less than sum3, add the right element (d[3] =1) to sum3 (sum3=4+1=5). right becomes 2. Now sum1=4 < sum3=5. So add left (d[2]=1) to sum1 (sum1=5), left=3. Now sum1=5, sum3=5. So set max_sum to 5. Now left is 3, right is 2. Loop condition left <= right is false. Exit. So the max_sum is 5. Which is correct.

Another example: third input [4,1,2]. The algorithm would start with sum1=0, sum3=0. Else clause is taken. Add 2 to sum3 (sum3=2, right=1). sum1=0 < sum3=2, add left (4) to sum1 (sum1=4, left=1). Now sum1=4 > sum3=2. So add right (1) to sum3 (sum3=3, right=0). Now sum1=4 > sum3=3. Add right (4?) Wait, right is 0. Then, the loop ends. So the max_sum is 0, which is correct.

So this approach seems to handle the test cases. Let's see the second example: [1,3,2,1,4]. The steps:

sum1=0, sum3=0. Else clause. Add 4 to sum3 (sum3=4, right=3). sum1 < sum3 (0 <4). Add 1 to sum1 (sum1=1, left=1). sum1 < sum3 (1 <4). Add 3 to sum1 (sum1=4, left=2). Now sum1=4 == sum3=4. So max_sum is 4. Then, else clause. Add d[3] (1) to sum3 (sum3=5, right=2). Now sum1=4 < sum3=5. Add d[2] (2) to sum1 (sum1=6, left=3). Now sum1=6 > sum3=5. Add right (d[2] =2, but right is 2. So add it to sum3 (sum3=5+2=7? Wait, no. Right is 3 at first. Then after adding 4, right becomes 3. Then when adding sum3 again, right is 3. So in the second example:

Wait, let's re-examine step by step.

Initial array: 1,3,2,1,4. n=5.

Step 1:

sum1=0, sum3=0. sum1 == sum3. So else clause: add d[right] (4) to sum3. sum3 becomes 4. right is now 3 (indexes 0-4). Then, sum1 < sum3 (0 <4). Add d[left] (1) to sum1. sum1=1. left=1.

sum1=1 < sum3=4. Add d[1]=3. sum1=4. left=2. sum1=4 == sum3=4. So max_sum becomes 4. Then, else clause: add d[right] (d[3]=1) to sum3. sum3=5. right=2. Now sum1=4 <5. So add d[left=2] (2) to sum1. sum1=6. left=3. sum1=6 > sum3=5. Add d[right=2] (2) to sum3. sum3=7. right=1. Now left=3, right=1. Loop ends. Max sum is 4. Which is correct.

Yes, this algorithm seems to work. So the approach is to use two pointers, accumulating the sums from left and right, and moving the pointers based on which sum is smaller. Whenever the sums are equal, we record the current sum if it's larger than the previous maximum. The maximum possible sum is the answer.

Now, what about the time complexity? Since each element is added at most once (each pointer moves from 0 to n-1), the algorithm runs in O(n) time, which is acceptable for n up to 2e5.

Space complexity is O(1) as we don't need to store any arrays except the input, which is read once.

So the steps to implement:

Read n, read the array. Initialize left=0, right =n-1, sum1=0, sum3=0, max_sum=0. Then loop while left <= right:

- if sum1 < sum3: add d[left] to sum1, left +=1
- else: add d[right] to sum3, right -=1
- if sum1 == sum3: update max_sum to sum1 if it's larger.

Once the loop ends, output max_sum.

But wait, in the first example, when sum1 and sum3 are equal, we need to check if it's possible to add elements from both sides. Like when sum1 and sum3 are equal, maybe adding the next element on both sides gives a higher sum. So the algorithm as described will handle that because after updating the max_sum, it will proceed to move the pointers again. For example, in the first case, after sum1=4 and sum3=4, the code will move to add d[right], which is 1 (sum3 becomes 5), then since sum1=4 <5, add the next left (sum1 becomes 5). Then sum1=5 equals sum3=5, so max_sum is updated to 5.

So the algorithm correctly captures this case.

Now, let's test the third example: [4,1,2]. The code will:

sum1=0, sum3=0. sum1 == sum3. So add to sum3 (d[2] =2). sum3=2, right=1. Now sum1=0 <2. Add d[0]=4. sum1=4, left=1. sum1=4 > sum3=2. So add d[1] (1) to sum3. sum3=3, right=0. Now sum1=4 >3. Add to sum3 (d[0] =4?), but right is 0. So adding d[0] would be 4. sum3 becomes 3+4=7. sum3=7. But right becomes -1. Now left is 1, right is -1. Loop ends. The max_sum is 0 (from the initial sum1 and sum3=0). But in this case, the correct answer is 0. Which is correct.

So the algorithm works here.

Another test case: when all elements are the same. For example, [5,5,5,5]. Then sum1 and sum3 would be 5, 10, 15, 20. Let's see:

Left starts at 0, right at 3.

sum1=0, sum3=0. sum equal. add right (5). sum3=5. right=2. sum1 < sum3. add left (5). sum1=5. sum1=5 == sum3=5. max_sum=5. Then, else clause: add d[2] (5) to sum3. sum3=10. right=1. sum1=5 <10. add left (5). sum1=10. sum1=10 == sum3=10. max_sum=10. Then else clause: add d[1] (5) to sum3. sum3=15. right=0. sum1=10 <15. add left (5). sum1=15. left=3. sum1=15 > sum3=15. sum1 == sum3. max_sum=15. Then add d[right] (d[0] =5) to sum3. sum3=20. right=-1. loop ends. So the maximum is 15. Which is correct because the first three elements (sum 15) and the last element (sum 5). Wait no. Wait, how is that possible? Because the array is split into three parts.

Wait, maybe in this case, the split is a=3 (sum 5+5+5=15), then the third part would have zero elements. Wait no. Wait, the third part is from a + b + 1 to a + b + c. So in this case, the first three elements sum to 15, and the third part (c=0) sum is 0. Wait, that can't be. So maybe the algorithm's approach isn't correct here. Wait, what's the actual correct answer here?

Wait, the array is [5,5,5,5]. The maximum sum where sum1 equals sum3. Let's think. The possible splits could be:

a=0, c=0: sum1=0, sum3=0. Sum is 0.

a=1, c=1: sum1=5, sum3=5 (third part is last element). So sum1=5.

a=2, c=2: sum1=10 (first two), sum3=10 (last two). But the array is of size 4. So a=2, c=2: positions 0 and 1 for first part, positions 2 and 3 for third part. But then the middle part is empty. But the middle can be empty. So sum1=10, sum3=10. That's possible. So the maximum sum is 10.

But according to the algorithm's steps, the maximum sum would be 15. How?

Wait, the algorithm's steps:

sum1=0, sum3=0. equal. max_sum=0. add to sum3 (5). sum3=5, right=2. sum1=0 <5. add left (5). sum1=5. sum1=5 == sum3=5. max_sum=5. Then add to sum3 (5, right=2. sum3=5+5=10. right=1. sum1=5 <10. add left (5). sum1=10. sum1=10 == sum3=10. max_sum=10. Then add sum3 (d[1]=5). sum3=15. right=0. sum1=10 <15. add left (5). sum1=15. left=3. sum1=15 == sum3=15. max_sum=15. Then add sum3 (d[0]=5). sum3=20. right=-1. loop ends. So the algorithm returns 15, which is incorrect. Wait, why?

Because in this case, the sum1 is 15 (sum of first three elements) and sum3 is 20 (sum of the last element, but that's not possible. Wait, the sum3 in the algorithm's code is built from the right. So when sum3 is 15, that's the sum of elements from the right. So the third part's sum is 15. But how?

Wait, let's see. The code's sum3 is the sum of the elements added from the right. Each time, we add d[right], then right decreases by 1. So the elements added to sum3 are d[right], d[right-1], etc. So for the array [5,5,5,5], when sum3 is 15, the elements added are 5 (d[3]), 5 (d[2]), 5 (d[1]). So the third part would consist of elements d[3], d[2], d[1], which are the last three elements. But the first part is the sum of the first three elements (d[0], d[1], d[2]). So the two parts would overlap, which is invalid. Because the first part is elements 0-2 (a=3), the third part is elements 1-3 (c=3), but a + b + c can't exceed n. So in this case, the split is invalid because the first and third parts overlap.

Ah, this is a problem. The algorithm's approach allows the sum1 and sum3 to include overlapping elements, which is invalid. Because in the code's logic, the sum1 is the sum of elements from the left (0 to left-1), and sum3 is the sum of elements from the right (right+1 to n-1). So in the case where left and right cross, but the code adds elements until left > right, then the sum1 and sum3 would include overlapping elements. So the algorithm's approach is incorrect.

Wait, but in the algorithm, the loop runs while left <= right. So during the loop, left and right are valid. But the code continues to add elements to sum1 or sum3 even when left and right are overlapping.

Wait, in the example where the array is [5,5,5,5], the code's steps are:

sum1=0, sum3=0. equal. add to sum3 (d[3]=5). sum3=5. right=2.

sum1 < sum3 (0 <5). add d[0]=5. sum1=5. left=1.

sum1=5 < sum3=5? No, equal. So add to sum3 (d[2]=5). sum3=10. right=1.

sum1=5 < sum3=10. add d[1]=5. sum1=10. left=2.

sum1=10 == sum3=10. add to sum3 (d[1]=5). sum3=15. right=0.

sum1=10 <15. add d[2]=5. sum1=15. left=3.

sum1=15 == sum3=15. add to sum3 (d[0]=5). sum3=20. right=-1.

Now, the max_sum is 15. But how does this correspond to the split?

sum1 is the sum of elements 0,1,2 (sum 15). sum3 is the sum of elements 3, 2, 1, 0? No. Because each time sum3 is added from the right, which is the element at index 'right' before it is decremented.

Wait, let's think: sum3 is the sum of elements from the end. So when we add d[right], which is the current right index. For example:

Initially, right is 3 (element 5). Then right becomes 2. So sum3 is 5 (from index 3). Then, when adding again from the right, we take d[2] (5), and right becomes 1. So sum3 is 5+5=10. Then adding d[1], sum3 becomes 15, right becomes 0. Then adding d[0], sum3 becomes 20, right becomes -1. So the sum3 is the sum of elements at indices 3, 2, 1, 0. But in this case, the third part would be all elements, which would require the first part to be empty and the third part to be the entire array, but sum1 and sum3 are 15 and 20 respectively. Wait, this is getting confusing.

So the problem is that the algorithm allows sum1 and sum3 to include overlapping elements. For instance, when the left pointer is at 3 and the right is at 0, but they have crossed. So the first part would be elements 0 to 2 (sum1=15), and the third part would be elements 3, 2, 1, 0 (sum3=20). But the third part is elements from a + b +1 to a + b + c. But a is 3 (since the first part has 3 elements). Then, a + b + c must be <= n. But in this case, a is 3, c is 4 (since sum3 includes 4 elements). So a + b + c must be 3 + b +4 <=4. Which implies b is negative. Which is impossible. So this split is invalid.

Thus, the algorithm's approach is incorrect because it allows sum1 and sum3 to be sums of overlapping elements, which is not allowed. So how to fix this?

Ah, right. So in the algorithm, whenever sum1 and sum3 are equal, we need to ensure that the elements taken from the left and right do not overlap. That is, the left pointer (the number of elements in the first part) plus the elements in the third part (c) must be <=n, and the first part is before the third part.

So in the code's current approach, when sum1 and sum3 are equal, the left pointer is the index of the next element in the first part. The third part's elements are from right+1 to n-1. So the elements in the first part are 0 to left-1. The elements in the third part are right+1 to n-1. For these two ranges to be non-overlapping, left-1 must be <= right. Because otherwise, the first part's elements would end at left-1, which is >= right+1 (since left > right+1). So the condition for a valid split when sum1 and sum3 are equal is that left <= right +1. Wait, not sure.

Wait, the first part is from 0 to a-1. The third part is from a + b to a + b + c -1. But since the array is split into three consecutive parts, the third part starts after the second part. So the entire array is first part, then second, then third. So the third part starts after the first two. Thus, the third part's starting index must be after the first part's ending index. So the first part's ending index is a-1. The third part starts at a + b. So a + b must be >=a. Which is always true as b >=0. So the third part is after the second part. So the third part can't overlap with the first part. But the sum3 in the algorithm is the sum of elements added from the right. So the third part's elements are the rightmost ones. For example, if we have added elements from the right until right is at index r, then the third part's elements are from r+1 to n-1. So the first part is 0 to left-1, third part is r+1 to n-1. So for these two parts to not overlap, left-1 < r+1. Which is equivalent to left <= r +1.

But in the algorithm, when sum1 and sum3 are equal, the current left and right may have crossed. So when left > right, the first part and third part would overlap. So in that case, even though sum1 equals sum3, the split is invalid.

Therefore, the algorithm's current approach may record a sum1 and sum3 when left > right, which is invalid. So we need to adjust the code to only consider cases where left <= right +1. Because if left <= right, then the first part ends at left-1, and the third part starts at right+1. So left-1 < right+1 → left <= right +1. Which is equivalent to left <= right +1. So when left is <= right +1, the first and third parts are non-overlapping. So in the code, when sum1 == sum3, we need to check if left <= right +1. Because if left > right +1, then the parts overlap and the split is invalid.

So the correct approach is to track the maximum sum only when sum1 == sum3 and left <= right +1. Because otherwise, even if sum1 equals sum3, the split is invalid.

So modifying the code to:

when sum1 == sum3, check if left <= right +1. If yes, then update the max_sum.

Ah, this is crucial. So the previous code would have cases where sum1 and sum3 are equal, but the split is invalid. So adding this check is necessary.

So how to adjust the code?

Inside the loop, after moving the pointers and adding to sum1 or sum3:

if sum1 == sum3:

    if left <= right +1:

        max_sum = max(max_sum, sum1)

But how to know when left and right are in a state where the split is possible?

Let me think. After adding to sum1 or sum3, the current left and right are the next elements to be added. So the first part is 0..left-1. The third part is right+1..n-1. So the split is valid when left-1 < right+1. Which is left <= right +1. So as long as left <= right +1, the first and third parts do not overlap.

So in the code, whenever sum1 == sum3, we check if left <= right +1. If yes, then the split is possible, and we can update the max_sum.

So in the algorithm, after adding to sum1 or sum3, when sum1 and sum3 are equal, check if left <= right +1.

So in the code:

In each iteration:

after adding to sum1 or sum3:

if sum1 == sum3 and left <= right +1:

    max_sum = max(max_sum, sum1)

So let's test this with the previous example where the array is [5,5,5,5]. The steps would be:

sum1=0, sum3=0. sum1 == sum3. Check left (0) <= right (3) +1 → 0 <=4 → yes. So max_sum becomes 0. Then, add to sum3 (d[3] =5. sum3=5. right=2. sum1=0 <5. Add d[0] → sum1=5. left=1. sum1=5. sum3=5. left (1) <= right (2)+1 → 1 <=3 → yes. So max_sum becomes 5. Then add to sum3 (d[2] → sum3=10. right=1. sum1=5 <10. Add d[1] → sum1=10. left=2. sum1=10 == sum3=10. left (2) <= right (1)+1 → 2 <=2 → yes. So max_sum becomes 10. Then add to sum3 (d[1] → sum3=15. right=0. sum1=10 <15. Add d[2] → sum1=15. left=3. sum1=15 == sum3=15. Check left (3) <= right (0)+1 →3 <=1 → no. So don't update max_sum. Then add to sum3 (d[0] → sum3=20. right=-1. loop ends. So the max_sum is 10. Which is the correct answer.

So adding this condition fixes the problem.

Thus, the correct approach is to use the two pointers but only update the max_sum when sum1 == sum3 and left <= right +1.

So modifying the code to include this condition is essential.

So the code will now look like this:

Read n and array.

Initialize left=0, right =n-1, sum1=0, sum3=0, max_sum=0.

Loop while left <= right:

    if sum1 < sum3:

        sum1 += d[left]

        left +=1

    else:

        sum3 += d[right]

        right -=1

    if sum1 == sum3:

        if left <= right +1:

            if sum1 > max_sum:

                max_sum = sum1

Output max_sum.

Wait, but when sum1 and sum3 are equal, and the condition left <= right +1 is satisfied, then the current sum can be considered. Let's see.

In the first example, after sum1 and sum3 become 5:

left is 3, right is 2. sum1 == sum3. left (3) <= right (2)+1 →3 <=3 → yes. So we can update the max_sum to 5.

Yes, because the first part is 0-2 (3 elements), third part is 3-4 (right+1 is 3, n-1 is4). So the split is valid.

So this approach works.

Another example: [5,5,5,5], the code now gives 10, which is correct.

So the code needs to check this condition whenever sum1 == sum3.

Thus, the correct implementation is to include the check left <= right +1.

So this is the key point that was missing in the initial algorithm.

Now, the code should handle all cases correctly.

Let's test the third example again:

Input 3 [4,1,2].

After initial steps:

sum1=0, sum3=0. left=0, right=2. sum equal. check left <= right+1 →0 <=3 → yes. max_sum=0.

Then, add to sum3 (d[2]=2). sum3=2. right=1.

sum1=0 < sum3=2. Add d[0]=4. sum1=4. left=1.

sum1=4 > sum3=2. add to sum3 (d[1]=1). sum3=3. right=0.

sum1=4 > sum3=3. add to sum3 (d[0]=4). sum3=7. right=-1.

sum1=4, sum3=7. sum1 != sum3. loop ends. max_sum remains 0. Correct.

So the code now works.

Thus, the correct code is:

Read n, read the list.

Initialize left=0, right=n-1, sum1=0, sum3=0, max_sum=0.

loop while left <= right:

    if sum1 < sum3:

        sum1 += d[left]

        left +=1

    else:

        sum3 += d[right]

        right -=1

    if sum1 == sum3:

        if left <= right +1:

            max_sum = max(max_sum, sum1)

return max_sum.

Yes, this should handle all cases.

Now, implementing this in Python.

We need to read n and the array. Then process as described.

For Python, for handling large input, it's better to read via sys.stdin. So:

import sys

n = int(sys.stdin.readline())

d = list(map(int, sys.stdin.readline().split()))

But since n can be up to 2e5, and each d_i can be up to 1e9, but Python can handle this.

Then, the code proceeds with the algorithm.

Test case 1:

input:

5

1 3 1 1 4

sum1 and sum3 steps:

sum1=0, sum3=0 → check left (0) <= 4 +1 → yes. max_sum=0.

sum3 +=4 → sum3=4. right=3.

sum1=0 <4 → sum1 +=1 → sum1=1. left=1.

sum1=1 <4 → sum1 +=3 → sum1=4. left=2.

sum1=4 == sum3=4. check left=2 <=3+1 →2<=4 → yes. max_sum=4.

sum3 +=1 → sum3=5. right=2.

sum1=4 <5 → sum1 +=1 → sum1=5. left=3.

sum1=5 == sum3=5. check left=3 <=2+1 →3<=3 → yes. max_sum=5.

sum3 += (d[right=2] is 1 → sum3=6. right=1.

loop ends.

output 5. Correct.

Thus, the code works.

So the code is correct.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    left = 0
    right = n - 1
    sum1 = 0
    sum3 = 0
    max_sum = 0
    while left <= right:
        if sum1 < sum3:
            sum1 += d[left]
            left += 1
        else:
            sum3 += d[right]
            right -= 1
        if sum1 == sum3:
            if left <= right + 1:
                max_sum = sum1
    print(max_sum)

if __name__ == "__main__":
    main()
```