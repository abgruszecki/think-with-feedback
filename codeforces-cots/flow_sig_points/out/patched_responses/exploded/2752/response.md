<think>
Okay, I need to solve this problem where I have to find the number of bad days. A day is bad if there are at least two days before it with strictly greater visits. Let's think about how to approach this.

First, let's understand the problem. For each day i (starting from 1), we need to check if there are at least two days before i (so days j and k where j < k < i) such that a_j and a_k are both greater than a_i. And these two days must be before the current day.

So for each day i, we need to check the previous days to see if there are two days that are both higher than a_i. But checking all previous days for each i would be O(n^2), which is way too slow for n up to 2e5. So we need a more efficient way.

Hmm. Let's think of the structure of the data. For each position i, we need to track the maximum two values in the prefix up to i-1. Wait, no. Because maybe the two largest values are not both greater than a_i. So maybe for each i, we need to know if there are at least two elements in the prefix before i that are strictly greater than a_i.

But how to track that efficiently.

Alternative approach: For each element, we can track the two largest elements encountered so far. But wait, that's not sufficient. Because even if the two largest elements are larger than a_i, but maybe there are other elements that are larger. But perhaps maintaining the two largest elements in the prefix would suffice. Because if those two are greater than a_i, then there are definitely two days before i that are greater. Otherwise, if one or none of them are greater, then the answer is no.

Wait, yes! Because the two maximum elements before i are the first and second maximum. If both are greater than a_i, then those two days are the required ones. If not, then there can't be two days that are both greater than a_i. Because even the top two are not both bigger, so there's no way.

So for each i, we can check if the current a_i is less than both the first and second maximum in the previous days.

But how to track the first and second maximum as we iterate through the array.

Let's think: for each i starting from the third day (since the first two days can't have two previous days), we need to track the two largest elements in the array up to i-1.

Wait, but for each i, the first maximum is the maximum of a_1 to a_{i-1}, and the second maximum is the second largest in that range.

So for each i >=3, we check if a_i is less than both the first and second maximum of the previous days. If yes, then it's a bad day. Otherwise, it's not.

This approach would work because if the first two maxima are both greater than a_i, then those two days are before i and have higher values. Otherwise, there's no two days.

But how to compute the first and second maximum efficiently as we process each element.

Let's think of maintaining two variables: max1 and max2. As we iterate through each element, after processing it, we update max1 and max2.

Wait, but for each element a_j (from j=1 to n), when we process a_j, the max1 and max2 up to j will be updated. But for the purpose of checking a_i, we need the max1 and max2 up to i-1.

So as we process each element i, the max1 and max2 before processing i would be the max1 and max2 up to i-1. So for i >=3, after processing the first i-1 elements, we can check if a_i is less than both max1 and max2. If yes, increment the count.

But wait, how to compute the second maximum correctly.

The problem is maintaining the two largest values up to the previous elements. So for example, when we process each element, we have to track the two largest in the current state.

Wait, here's an idea. We can initialize max1 and max2 to the first two elements in sorted order. Then, as we process each new element starting from the third element, before checking if the current element is a bad day (which would be the third element's case), we check if a_i is less than both the current max1 and max2. But wait, the max1 and max2 up to i-1 would be the ones before processing the i-th element. So for each element i (starting from 3), the max1 and max2 are the maximums from the first i-1 elements. So the approach would be:

Initialize:

- For the first two elements, there's no possible bad day. So count starts at 0.

We need to track the max1 and max2 as we go. For each element i (starting from 3 to n), we check if a_i is less than both the current max1 and max2. If yes, increment the count. Then, we update the max1 and max2 with a_i.

Wait, but how to maintain the max1 and max2 correctly as we process each element. Let's think step by step.

For example, let's process the elements in order. Let's say we have up to element j. We need to track the two largest elements in the first j elements. So as we process each new element a_j, we compare it with the current max1 and max2. If a_j is larger than max1, then new max1 is a_j, and new max2 is the old max1. If a_j is between max2 and max1, then new max2 is a_j. Otherwise, no change.

So, the process is:

max1, max2 = first two elements sorted in descending order. For example, if a1 is 3 and a2 is 1, then max1 is 3, max2 is 1. Then, for each a_i starting from i=3 (third element), we check if a_i is less than max1 and max2. If yes, increment count. Then, we need to update max1 and max2 based on a_i.

Wait, but in this case, when we process the third element, the max1 and max2 are the first two elements. So for the third element, we check if a_3 is less than both max1 and max2. If yes, count increases. Then, we update max1 and max2 to include a_3.

But this approach might miss some scenarios. Let's take an example.

Suppose the first three elements are 5, 4, 6. Then, the first two elements have max1=5, max2=4. Then the third element is 6. So when processing i=3 (element 6), the code would check if 6 is less than 5 and 4. No, so no count. Then, update max1 to 6, max2 to 5. Now, the next element (i=4) would check against max1=6 and max2=5. So if a_4 is 3, then yes, count increases. But if a_4 is 5, then 5 is not less than max2 (5), so no count.

This seems correct. So the algorithm would track the two largest elements up to the previous day for each i.

Wait, but when processing i, the max1 and max2 are the two largest elements up to i-1. Because for each i, after processing i-1 elements, we have the max1 and max2. Then, for the i-th element (the current element in the loop), we check if it's a bad day (i.e., a_i is less than both max1 and max2). Then, after checking, we update the max1 and max2 with a_i.

Yes, because the next elements would need to have the previous max1 and max2 include the current a_i.

So the steps would be:

Initialize:

if n < 3, then return 0.

max1 and max2 are the first two elements, sorted in descending order.

count = 0.

Then, for each i from 2 to n-1 (assuming 0-based or 1-based?), let's see.

Wait, in Python, if the array is 0-based, then the first two elements are index 0 and 1. Then, starting from index 2 (third element), check against max1 and max2 (which are the first two elements). Then, update max1 and max2 with the current a[i].

So code outline:

n = int(input())
a = list(map(int, input().split()))
if n < 3:
    print(0)
    exit()

count = 0
max1, max2 = sorted([a[0], a[1]], reverse=True)
# Wait, but what if a[0] is less than a[1]? sorted in reverse gives max1 = a[1], max2 = a[0]

for i in range(2, n):
    current = a[i]
    if current < max1 and current < max2:
        count +=1
    # Now update max1 and max2 with current
    if current > max1:
        max2 = max1
        max1 = current
    elif current > max2:
        max2 = current

print(count)

Wait, but this might not work. Let's test with the first example:

Sample input 1:
8
3 1 4 1 5 9 2 6

The days are 1-8. The bad days are day 4 (a=1) and day7 (a=2). So the count should be 2.

Let's see how the code processes this.

Initial a is [3,1,4,1,5,9,2,6]

First, max1 and max2 are sorted([3,1], reverse=True) => 3,1.

Now, process i=2 (third element, value 4):

Check 4 < 3 and 1? No. So count remains 0. Then, 4 is larger than max1 (3). So max1 becomes 4, max2 becomes 3.

Next, i=3 (fourth element, value 1):

Check 1 < 4 and 3? Yes. So count becomes 1. Then, 1 is not larger than max1 or max2. So no change.

i=4 (fifth element, value 5):

Check 5 <4 and 3? No. Update max1 to 5, max2 to4.

i=5 (sixth element, value 9):

Check 9 <5 and4? No. Update max1 to9, max2 to5.

i=6 (seventh element, value2):

Check 2 <9 and5? Yes. count becomes 2. Then, 2 is not larger than any.

i=7 (eighth element, value6): check 6 <9 and5? 6 is not less than 5. So no. Update max2 to6 (since 6>5). So new max1=9, max2=6.

Final count is 2. Which matches the sample. So code works here.

Another sample: input 5 all 1s. Then max1 and max2 are 1 and1. For each i >=2 (third element), check if 1 <1 and1? No. So count remains 0. Correct.

Third sample:

Input: 13 elements: 2,7,1,8,2,8,1,8,2,8,4,5,9. The output is 6.

Let's see. Let's walk through the code.

Initial array is [2,7,1,8,2,8,1,8,2,8,4,5,9]

First two elements: 2 and7. sorted in reverse gives max1=7, max2=2.

i=2 (element 1): 1 <7 and 2 → yes. count becomes 1. Then, 1 is not larger than any, so no change.

i=3 (element8): check 8 <7 and 2? No. Update: 8>7 → new max1=8, max2=7.

i=4 (element2): check 2 <8 and7 → yes. count becomes2. No change in max.

i=5 (element8): 8 <8 is false. So no. Compare with current max1=8. 8 is equal to max1, so not greater. So no update. So max1 and max2 remain 8 and7.

Wait, but in the code:

If current > max1: update max1 and max2.

Else if current > max2: update max2.

So when current is equal to max1 or max2, nothing is done. So in this case, when the element is 8 (same as max1), no changes. So for i=5, the element is 8. Then, when processing i=5 (element8), check 8 <8? No. So count not increased.

Then, the code proceeds. Let's see how the third sample is handled.

Let's list all elements:

Indices 0:2, 1:7, 2:1,3:8,4:2,5:8,6:1,7:8,8:2,9:8,10:4,11:5,12:9.

Processing from i=2 (element1) up to i=12.

After processing first two elements (0 and1):

max1=7, max2=2.

i=2 (element1):

Check 1 <7 and2 → yes. count=1.

Update: 1 is not >7 or 2 → no change. max remains 7, 2.

i=3 (element8):

Check 8 <7 → no. So count remains. Update: 8>7 → max1 becomes8, max2=7.

i=4 (element2): check 2 <8 and7 → yes. count=2. Update: no.

i=5 (element8): check 8 <8 → no. update: 8 is not >8, so check if >7. yes. So max2 becomes8.

Now, max1=8, max2=8.

i=6 (element1): check 1 <8 and8 → yes. count=3. Update: no.

i=7 (element8): check 8 <8 → no. check if 8>max1 (8)? no. check if >max2 (8). no. So no update.

max1 and max2 remain 8 and8.

i=8 (element2): check 2 <8 and8 → yes. count=4. Update: no.

i=9 (element8): same as before. no count. no update.

i=10 (element4): check 4 <8 and8 → yes. count=5. Update: no.

i=11 (element5): check 5 <8 and8 → yes. count=6. Update: no.

i=12 (element9): check 9 <8 → no. Update: 9>8 → max1 becomes9, max2=8.

So total count is6. Which matches the sample. So the code works here.

Thus, this approach seems correct. The time complexity is O(n), which is acceptable for n=2e5.

Now, let's think about possible edge cases.

Edge case where the initial two elements are same. Like input [5,5,5], n=3. For the third element (5), check if 5 is less than max1=5 and max2=5. No. So count is 0. Correct.

Another case: initial two elements are in reverse order, but the third is smaller than both. For example, input [5,3,2]. The third element (2) is less than 5 and 3 → count 1. Correct.

Another case: initial two elements are [3,5]. So sorted in reverse gives max1=5, max2=3. Third element 4. Check 4 <5 and3 → no. So count remains 0. Then update: 4 is greater than3, so max2 becomes4. So for next elements, if they are 3, then 3 is less than5 and4 → yes. So this is handled correctly.

So the code seems correct.

So the plan is:

- Handle n <3 → output 0.

- For n >=3:

   - Initialize max1 and max2 as the first two elements sorted in descending order.

   - For each element from index 2 (third element) to end:

      - if current element < both max1 and max2 → increment count.

      - then update max1 and max2 as needed.

This approach is O(n) time and O(1) space. Which is optimal for the constraints.

Now, implement this in Python.

Wait, but in Python, how do we handle the first two elements correctly?

In code:

n = int(input())
a = list(map(int, input().split()))
if n <3:
    print(0)
    exit()

max1, max2 = sorted(a[:2], reverse=True)

count =0

for i in range(2, n):
    current = a[i]
    if current < max1 and current < max2:
        count +=1
    # update max1 and max2
    if current > max1:
        max2 = max1
        max1 = current
    elif current > max2:
        max2 = current

print(count)

Yes.

Wait, but what if the first two elements are equal?

For example, a[:2] is [5,5]. sorted in reverse is [5,5]. Then, for the third element, say 4. 4 <5 and5 → yes. Then, count increases. Then, since 4 is not larger than either, no update. Then, next elements.

But in this case, any element less than5 will be counted.

But in reality, the first two elements are 5 and5. So any element after that which is less than both (5 and5) will be considered a bad day.

Which is correct, because there are two days (the first two) with higher values. So the code correctly counts them.

Another edge case: n=2. Output 0.

All test cases should be covered.

Thus, this code should be correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
if n < 3:
    print(0)
    exit()
max1, max2 = sorted(a[:2], reverse=True)
count = 0
for num in a[2:]:
    if num < max1 and num < max2:
        count += 1
    if num > max1:
        max2, max1 = max1, num
    elif num > max2:
        max2 = num
print(count)
```