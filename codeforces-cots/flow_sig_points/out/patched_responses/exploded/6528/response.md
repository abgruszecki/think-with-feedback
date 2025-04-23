<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about finding the maximum number of problems we can select from a given list such that each consecutive problem in the selected subset satisfies a condition. The condition is that the next problem's difficulty is at most twice the previous one. So for the subset a_i1, a_i2, ..., a_ip, for each j from 1 to p-1, a_ij+1 <= 2*a_ij. And we need to find the longest possible such subset.

The input is a list of sorted, distinct integers. So the list is already in increasing order. So the subset we select must be a subsequence (not necessarily contiguous) of the original list, but in order. But since the original list is sorted, the selected subset must also be in order, but we can skip elements.

The task is to find the maximum length of such a valid subsequence.

Hmm. So, how do I approach this? Let's think about possible algorithms.

The naive approach would be to check all possible subsequences and find the longest valid one. But that's obviously impossible for n up to 2e5. So we need a more efficient approach.

Since the list is sorted, maybe the optimal subsequence is a contiguous subsequence in the original list. Because if there's a subsequence that skips some elements, maybe adding those elements in between could create a longer valid sequence. Wait, no. Because the original list is sorted. For example, suppose you have elements A, B, C, D where B is between A and C. If the sequence A, C is valid (C <= 2A?), then perhaps inserting B between them could create a longer sequence. But if B is such that A <= B <= 2A and B <= C <= 2B, then A, B, C would be longer. But if B is such that B > 2A, then inserting B would break the condition. So maybe the optimal sequence is a contiguous block in the original list.

But wait, the problem says that the subset can be any subset (not necessarily contiguous) but in the same order. So the optimal solution could be a contiguous block, but perhaps not. However, given that the list is sorted, the optimal solution might be a contiguous block. Let me think about examples.

Take the first sample input:

10
1 2 5 6 7 10 21 23 24 49

The optimal subset is 5,6,7,10. That's a contiguous block in the original list. So in this case, the contiguous approach works.

Another example: suppose the list is 1, 3, 4. Then 1,3 has 3 > 2*1=2, so invalid. 1,4: 4>2*1, invalid. 3,4: 4<=6, so valid. So the longest is 2 elements, which is contiguous.

But what if the list is 1, 5, 6. Then 5 and 6 are valid. 1,5,6: 5>2*1=2, so 5 is allowed (since the next element must be <=2*current). Wait, no. The condition applies to each consecutive pair in the selected subset. So for 1,5,6:

5 is next after 1. So 5 must be <= 2*1. But 5>2, so this is invalid. So the subset [5,6] is valid with length 2. So the maximum is 2. So contiguous.

Hmm. So maybe the maximum valid subsequence is a contiguous block in the original array. Because any non-contiguous sequence would have gaps, and perhaps inserting the elements in the gaps could allow for a longer sequence.

But is that always the case?

Another example: Suppose the list is [2, 4, 5, 10]. The subset [2,4,5] is valid because 4 <= 2*2=4, and 5 <= 2*4=8. So length 3. Then 5 and 10: 10 <= 2*5=10, so valid. So the subset [2,4,5,10] is valid. So the entire list is a valid subset, which is contiguous. So again contiguous.

But what if the list is [1, 10, 11]. Then the subset [1,10] is invalid (10>2*1). [10,11] is valid (11 <= 20). So the maximum is 2. Which is contiguous.

Wait, but maybe there's a case where the optimal subset is not contiguous. Let's think:

Suppose the list is [1, 3, 4, 8]. Then:

- 1,3: 3>2 → invalid.
- 3,4: valid. 4 <=6. So subset [3,4] length 2.
- 4,8: 8 <=8 → valid. So [3,4,8] is valid, length 3. Which is contiguous.
But wait, is there a non-contiguous subset longer? For example, 1,3,4,8: no. Because 3>2*1, so can't include 1 and 3 in the same subset. So contiguous is better.

Another example: list [1, 2, 5, 11, 22]. The subset [2,5,11,22] is 5>2*2=4 (5>4), so 5 is invalid. So 2 and 5 can't be consecutive. So subset [5,11,22] is valid. 11<=10? No, 5*2 is 10, 11>10. So 5 and 11 are invalid. So [11,22] is valid. So maximum is 2. But maybe [1,2] is valid (length 2). So the maximum is 2. But in this case, the subset [1,2] is contiguous and of length 2.

So in all examples I can think of, the maximum subset is a contiguous block. Therefore, perhaps the optimal approach is to find the longest contiguous subarray where each consecutive pair in the subarray satisfies the condition. Then, the maximum length of such a contiguous subarray is the answer.

If that's the case, the problem simplifies to finding the longest contiguous subarray where each consecutive pair a[i], a[i+1] satisfies a[i+1] <= 2*a[i]. Because the entire contiguous subarray would form a valid subset, and since the list is sorted, any longer subset would have to be contiguous.

Wait, but the problem allows selecting any subset as long as consecutive elements in the subset satisfy the condition. But if the subset is not contiguous in the original array, but has elements that are spread out, maybe the consecutive elements in the subset could satisfy the condition even if the original array's consecutive elements don't. For example, let's say the array is [1, 3, 4, 7]. Then the subset [1,3,7] would have 3>2*1=2 (so invalid between 1 and 3). But [3,4,7] would be 4 <=6, 7 <=8 → valid. So that's a subset of length 3. But if the entire array is checked for contiguous blocks, the maximum contiguous would be 3 (3,4,7) or maybe longer.

Wait, the array is sorted. So if we have a subset that skips some elements, the elements in the subset are in order. For example, if the original array is [1, 2, 5, 6, 7, 10], then the subset [5,6,7,10] is contiguous. But if there was a subset like [5,6,10], that's non-contiguous but in order. However, 6 to 10: 10 <= 2*6=12 → yes. So 5,6,10 is a valid subset of length 3. But the contiguous subset 5,6,7,10 has length 4, which is longer. So the optimal is contiguous.

So perhaps the optimal solution is indeed the longest contiguous subarray where each consecutive pair satisfies a[i+1] <= 2*a[i]. Because if you can find such a contiguous subarray of length L, then any non-contiguous subset can't have a longer length. Because the contiguous subarray's consecutive elements are all valid, thus forming a valid subset of length L, which is the maximum possible.

So the problem reduces to finding the maximum length of a contiguous subarray in the given sorted array where each consecutive pair in the subarray satisfies a[i+1] <= 2*a[i].

If this is true, then the solution is straightforward: iterate through the array and track the current length of the contiguous subarray where the condition holds. For each element from index 1 to n-1, check if a[i] <= 2*a[i-1]. If yes, increase the current length; else, reset current length to 1 (since the current element starts a new possible subarray). Keep track of the maximum length found.

Wait, but the current element can't start a new subarray on its own. Wait, when you reset, you start the current length as 1 (the previous element is not part of the current subarray anymore). Wait, perhaps the approach is:

Initialize max_length and current_length to 1.

Loop from i = 1 to n-1:

   if a[i] <= 2 * a[i-1]:

       current_length +=1

   else:

       current_length = 1

   update max_length if current_length is larger.

At the end, max_length is the answer.

Because, the maximum contiguous subarray where each consecutive pair satisfies the condition is exactly the maximum possible subset length. Because any such subarray forms a valid subset, and there's no longer subset possible even if we allow non-contiguous.

So for example, in the first sample input:

The array is 1,2,5,6,7,10,21,23,24,49.

Check consecutive pairs:

2 <= 2*1 → yes. So current_length becomes 2.

Then 5: check 5 <= 2*2=4 → no. So reset to 1.

So current_length is now 1 (for 5). Then next element 6: check 6 <= 2*5=10 → yes. current_length becomes 2.

7: 7 <= 2*6=12 → yes. current_length 3.

10: 10 <= 2*7=14 → yes. current_length 4. So max is 4.

Then 21: check 21 <= 2*10=20 → no. reset to 1. Then 23: 23 <= 2*21=42 → yes. current_length 2. Then 24: yes. current_length 3. Then 49: 49 <= 2*24=48 → no. So current_length resets to 1. So the max remains 4.

Which matches the sample output.

The second sample:

5
2 10 50 110 250.

Check each consecutive pair:

10 <= 2*2=4 → no. So after first step, current_length is 1 (since 2 and 10: no. So current_length becomes 1 again). Then 50 and 10: 50 <= 20 → no. current_length 1. And so on. So the maximum is 1.

Third sample:

6
4 7 12 100 150 199.

Check consecutive pairs:

7 <= 8 → yes. current_length 2.

12 <= 14 → yes. current_length 3. So this gives a sequence of 4,7,12 → valid. So current_length 3. Then 100: 100 <= 24 → no. reset. Then 150 <= 200 → yes. current_length 2. Then 199: 199 <= 300 → yes. current_length 3. So the maximum is max(3,3) =3.

Which matches the sample.

So this approach works for the sample cases.

So the algorithm is O(n) time, which is acceptable for n up to 2e5.

So the optimal solution is to find the longest contiguous subarray where each consecutive element is <= 2 * previous. The maximum length of such a subarray is the answer.

Now, let's code this.

The steps are:

Read n.

Read the list a.

Initialize max_length = 1, current_length = 1.

Loop from i=1 to n-1:

   if a[i] <= 2*a[i-1]:

       current_length +=1

   else:

       current_length = 1

   max_length = max(max_length, current_length)

At the end, print max_length.

That's straightforward.

So code in Python:

n = int(input())

a = list(map(int, input().split()))

max_len = 1

current = 1

for i in range(1, n):

    if a[i] <= 2 * a[i-1]:

        current +=1

    else:

        current = 1

    if current > max_len:

        max_len = current

print(max_len)

Wait, let's test this with the third sample:

Input is 4,7,12,100,150,199.

Loop:

i=1: 7 <= 8 → yes. current 2 → max 2.

i=2: 12 <= 14 → yes. current 3 → max 3.

i=3: 100 <= 24? No. current becomes 1. max remains 3.

i=4: 150 <= 200 → yes. current 2. max still 3.

i=5: 199 <= 300 → yes. current 3 → max remains 3.

So output 3. Correct.

Second sample: all pairs after 2,10 are invalid. So the maximum is 1.

Yes.

So the code works for the samples.

What about edge cases?

Case n=1: output 1.

Case where all pairs are valid. For example, a list where each a[i] is exactly 2*a[i-1]. Then the code returns n. Which is correct.

Another case where the list is 1,3,6,12,24. Each step is valid. So the code returns 5. Which is correct.

Another case: a list where the maximum is in the middle.

E.g., [1,2,4,8,16,32,17]. Here, the first 6 elements are valid, but the 7th is 17 ≤ 2*32=64 → yes. So current_length becomes 7. So the code returns 7.

Wait, but 17 is <= 2*32 → yes. So the contiguous subarray is the entire array. So the code returns 7.

So code works.

So this code should be correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_len = current = 1
for i in range(1, n):
    if a[i] <= 2 * a[i-1]:
        current += 1
    else:
        current = 1
    if current > max_len:
        max_len = current
print(max_len)
```