<think>
Okay, I need to solve this problem where I have to find the maximum possible length of a string that meets two conditions: each letter's count is at most ai, and all counts are distinct. Let's think about how to approach this.

First, the problem requires that for each letter used in the string, the number of times it appears must be unique. So even if a letter's allowed count is high, we might have to reduce it to make sure all counts are distinct.

Hmm. The goal is to maximize the sum of the counts, but with all counts being distinct. Each count can't exceed its ai, and all counts must be different.

So the approach might be to select a subset of letters, assign each a distinct count (starting from the highest possible), and sum them up. The challenge is to choose which letters to include and what counts to assign to maximize the sum.

Let me think. For example, if I sort the ai in descending order. Then, for each position, the maximum possible count for that letter is the minimum between the ai and the previous count minus one. Because each next letter's count must be strictly less than the previous.

Wait, that makes sense. Like, if I have a sorted list of ai, then starting from the largest, each next element's allowed count is min(ai, previous count - 1). Because we need the counts to be strictly decreasing.

For example, take the first sample input: [5,5,2] after sorting in descending order. The sorted list is 5,5,2. Then, the first element is 5. The second is min(5, 5-1) =4. Third is min(2,4-1=3) which is 2. Sum 5+4+2=11, which matches the sample output.

Another example: [2,1,1] sorted is 2,1,1. First is 2, second is min(1,2-1)=1. But since the second can't be 1 (same as the next?), wait. Wait, the counts have to be distinct. So after the first is 2, the next can be at most 1. But then the third would have to be 0, which is not allowed (since we can only include letters with count >=1). So in that case, maybe the optimal is to take two letters: 2 and 1, sum 3.

Wait, but the second sample input is 1,1,2. Sorting in descending order gives 2,1,1. Then the first is 2, second is min(1, 2-1=1) which is 1. But the third would be min(1, 1-1=0) which is 0. So sum is 2+1+0=3. But in the sample output, the sum is 3, which matches. However, the third letter is 0, but in the solution, the third letter (c) has a count of 0, but in the actual sample output, the third character is included. Wait, no. Wait, the sample input is 3 letters with a1=1, a2=1, a3=2. The sorted list would be 2,1,1. Then, the first count is 2. The second is min(1, 2-1) =1. The third is min(1, 1-1=0) → 0. So sum is 2+1+0=3, which is correct. But the third letter's count is 0, so it's not included. So the actual counts are 2 (for the third letter) and 1 for one of the first two. But wait, how does that work?

Wait, maybe the sorted list is not the original letters. Let me see. The original a's are 1,1,2. So when sorted in descending order, it's 2,1,1. So the third letter here (original third, which has a_i=2) is assigned 2. Then the next is min(1, 2-1=1) →1. Then the third is min(1,1-1=0) →0. So the sum is 2+1+0=3. But in the actual solution, the counts are 1,1,2. But that's not allowed because the counts are not distinct. So the correct approach is to take the third letter (count 2), and two others each with count 1. But that's a problem because the counts are same. So why is the sample output 3?

Ah, right. Because in the sample input, the correct counts are 2,1,0 (sum 3). But how? Because the third letter is allowed up to 2. So the first letter in the sorted list (original third) is allowed 2. Then the next (original first) has a_i=1, which is min(1, 2-1=1). So that's 1. Then the third (original second) is min(1, 1-1=0) →0. So sum 2+1+0=3. So the letters used are the first and second, but wait, no. The counts for the third and first letters are 2 and 1. The second is 0. So the letters in the string are the third (count 2) and first (count 1) and second (count 0, so not included). So the counts are 2 and 1, which are distinct. So the total is 3. Which matches the sample.

So the algorithm seems to work. So the approach is:

1. Sort the array of ai in descending order.
2. For each element in the sorted array, starting from the first, assign the maximum possible value that is <= the previous value minus 1 (if it's not the first), but also not exceeding the ai of that element.
3. Sum all the assigned values.

So the steps are:

Sort the ai in non-increasing order.

Initialize prev = a[0], sum = prev.

Then for each next element a_i in the sorted list (from index 1):

current_max = min(a_i, prev -1)

if current_max <=0, then we can't take this element (since the count must be at least 0, but if it's 0, then we don't include the letter). Wait, but the problem says that the letters that occurred in the string at least once. So if a letter's count is 0, it's not included, so it doesn't need a distinct count.

So, when processing the sorted array, we can stop once the current_max becomes 0, since all remaining elements would also be 0 (as the array is sorted).

Wait, but the sorted array is in descending order, so once a certain element's current_max is 0, all elements after it would have a_i <= current element, which is already 0.

So in the algorithm, after sorting, for each element in order, compute the current_max as min(a_i, prev-1). If current_max <=0, we skip it (add 0 to the sum, but since it's not included, the sum is not increased). So the steps would be:

prev = sorted_a[0]

sum = prev

for i from 1 to n-1:

   current_max = min( sorted_a[i], prev -1 )

   if current_max <=0:

       break

   sum += current_max

   prev = current_max

So the loop stops as soon as current_max is <=0, since all subsequent elements are <= sorted_a[i], which is <= current_max, so they would also be 0.

Wait, but sorted_a is in descending order. So if sorted_a[i] is 5,5,2. For the second element (5), the current_max is min(5, 5-1=4) →4. So added. The third element (2) is min(2,4-1=3) →2. So added. So the sum is 5+4+2=11.

Another example: sorted array is 2,1,1. Then first element is 2. Next is min(1, 2-1=1) →1. Sum is 3. Then third element is min(1, 1-1=0) →0. So sum is 3.

So the algorithm seems to work.

But wait, what if after processing some elements, the current_max is higher than the a_i of a later element, but due to the previous step, it's allowed. Because we process in the order of sorted a_i, which is in descending order, so for elements after i, their a_i is less than or equal to the previous elements. So once we process them in order, the algorithm correctly caps them.

So the steps are:

Sort the array in non-increasing order.

Initialize sum as the first element.

prev = first element.

Then for each subsequent element:

current_max = min(a_i, prev -1)

if current_max <=0, break.

sum += current_max

prev = current_max.

So the code would be:

Sort the a list in descending order.

If the list is empty, return 0.

sum = a[0]

prev = a[0]

for i in 1 to len(a)-1:

    current = min(a[i], prev - 1)

    if current <=0:

        break

    sum += current

    prev = current

return sum

Yes, this seems correct.

So the algorithm is O(n log n) for sorting, which is acceptable since n is up to 26.

So in Python, the code would be:

Read n.

Read the list of a_i.

Sort them in reverse order.

if n is 0, output 0 (but n >=2 in constraints).

sum = a[0]

prev = a[0]

for i in range(1, n):

    current = min(a[i], prev -1)

    if current <=0:

        break

    sum += current

    prev = current

print(sum)

Wait, but what about the case where the next element's a_i is higher than prev-1, but the prev-1 is higher than the a_i of the next element. Wait, no. Because the list is sorted in descending order, so a[i] <= a[i-1]. So for example, if a[i] is 5, and prev-1 is 4, then current is 4. But if a[i] is 3, and prev-1 is 4, then current is 3. So in any case, current is the minimum between a[i] and prev-1.

This approach ensures that the counts are strictly decreasing and each is as large as possible.

This should handle all cases.

Let's test the first sample input:

3

2 5 5 → sorted as 5,5,2.

sum =5.

i=1: current = min(5,5-1=4) →4. sum=5+4=9. prev=4.

i=2: current = min(2,4-1=3) →2. sum=11. prev=2.

Loop ends. Output 11. Correct.

Second sample input:

3

1 1 2 → sorted as 2,1,1.

sum=2.

i=1: current = min(1, 2-1=1) →1. sum=3. prev=1.

i=2: current = min(1, 1-1=0) →0. So break. sum remains 3. Correct.

Another test case: input is 2, a = [3,3]. Sorted as 3,3.

sum=3. i=1: min(3, 3-1=2) →2. sum=5. So output 5.

Yes, counts 3 and 2, which are distinct.

Another test case: input 3, a = [5,4,3]. Sorted as 5,4,3.

sum=5. i=1: min(4,4) →4. sum 9. i=2: min(3,3) →3. sum 12. All counts 5,4,3. Which is okay.

What if a has a very big number, but after previous steps it's reduced. Like a = [10^9, 10^9, ...]. Then the sum is 10^9 + (10^9-1) + (10^9-2) + ... until it's possible.

But the code handles that as well.

So the code seems correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
if not a:
    print(0)
else:
    total = a[0]
    prev = a[0]
    for i in range(1, n):
        current = min(a[i], prev - 1)
        if current <= 0:
            break
        total += current
        prev = current
    print(total)
```