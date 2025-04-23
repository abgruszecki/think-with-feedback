<think>
Okay, let's see. The problem is about figuring out how many words remain on the screen after ZS finishes typing all the words. The rule is that if the time between consecutive words is more than c seconds, the screen resets. Otherwise, the words accumulate. 

Hmm, so the key here is to determine for each word whether the difference between it and the previous word is more than c. If so, then the current group resets. Otherwise, the group continues. The answer is the size of the last group.

Wait, right. Because each time the time between two consecutive words is greater than c, the previous words are cleared, and the new word starts a new group. So the total words remaining is the number of words in the last consecutive group where all adjacent differences are <= c.

So how do I find the last such group? Let's think. The words are given in strictly increasing order. So we can iterate through the list, tracking the start of the current group. Once we find a ti where ti - t_{i-1} > c, the current group ends at i-1, and the new group starts at i. The last group is the one that includes the last word. The size of that group is the answer.

So the approach is to find the rightmost position where the group starts. Let's see. For example, in the first sample input: the times are 1,3,8,14,19,20. Let's look at the differences between consecutive elements:

3-1=2 <=5: same group. 8-3=5 <=5: same. Then 14-8=6>5. So group up to 8 ends. Then 19-14=5 <=5, same group. 20-19=1 <=5. So the last group is from 14,19,20: three words. So the answer is 3.

So the algorithm can be:

Start from the end and check how far back we can go such that each consecutive pair in that range has a difference <=c. Wait, but that's not exactly right. Because if we have a series of consecutive steps where each is <=c, then they form a group. So the last group is the longest possible ending at the last element where all consecutive differences in that group are <=c.

Wait, the group must consist of consecutive elements where each adjacent pair has difference <=c. So the last group is the maximal possible group starting from some index k to the end (n-1) where between k and k+1, etc., the difference is <=c.

Wait, but maybe it's better to process from the end. Let's think: the last word is always in the group. Then, we can check the previous words in reverse order until we find a pair that's more than c. The first such occurrence (when going backward) marks the start of the last group. So, for example, in the second sample input:

6 1
1 3 5 7 9 10

Looking at the differences between consecutive elements:

3-1=2>1: group ends at 1. Next, 5-3=2>1: group ends at 3. 7-5=2>1, etc. Then 10-9=1 <=1. So the last group is 9 and 10. So the answer is 2.

So the approach is to start from the end and go backward, checking if the current word and the previous one have a difference greater than c. Once we find such a point, the last group starts from the next index.

Wait, let's think in reverse. The last group must include the last word. Let's traverse the list from the end to the beginning. We need to find the earliest index i (starting from the end) where t_{i+1} - t_i > c. Then the last group starts at i+1 and goes to the end. The number of elements in this group is (n-1) - (i+1) +1 = n - i -1. Wait, perhaps not. Let's see.

Alternatively, the last group is a consecutive sequence ending at the last element. The start of the group is the first element in the sequence where all consecutive elements from start to end are within c.

Wait, maybe the correct approach is to iterate from the end backwards and find the first index where t[i+1] - t[i] > c. Once found, then the last group is from i+1 to the end. The size is (n-1) - (i+1) + 1 +1 (since adding 1 for the start element). Wait, perhaps an example will help.

In the first sample, the times are 1,3,8,14,19,20. So when going backward:

Check 20-19=1 <=5. Then 19-14=5 <=5. Then 14-8=6>5. So the first occurrence (from end) where the difference is >c is at i=2 (t[3] - t[2] =14-8=6>5). So the group starts from i+1=3, which is the 14,19,20. So the count is 3 words.

So the idea is that the group starts at i+1, and includes all elements from there to the end. So the number of words is (n-1) - (i+1) +1 +1? Wait, the index in the array starts from 0. Let's see.

For the first sample, the array indices are 0 to 5 (n=6). The i where t[i+1]-t[i]>c is i=2 (t[3]-t[2]=6>5). Then the group is from i+1=3 to 5, which is 14,19,20. The count is 5-3+1=3. So yes, that's correct.

So the algorithm is:

Initialize the group start as the last index (n-1). Then, traverse backward from the second last element to the first. For each element at index i, check if t[i+1] - t[i] > c. If yes, then the group starts at i+1. So the group is from i+1 to the end. Once we find the earliest such i (from the end), then the group is from i+1 to end, and the answer is the count of elements from i+1 to end.

But wait, the way to find the start is to find the first place (starting from the end) where the difference is larger than c. All elements after that (from i+1 onwards) are part of the group.

So for example, if all consecutive elements have differences <=c, then the group is the entire array, and the answer is n.

So in code, we can start from the end and go backward until we find the first i where t[i+1] - t[i] > c. The group is from i+1 to the end, which has (n-1) - (i+1) +1 +1 = n - i -1 elements. Wait, (n-1) - (i+1) +1 = (n-1 -i-1 +1) =n -i -1. Then add 1 because the elements are from i+1 to n-1 inclusive. For example, in first sample, i=2. The group is 3 elements (indices 3,4,5): 5-3+1=3.

Yes. So the code can be written as:

Initialize the group length as 1 (since the last word is always present). Then, iterate from the second last element (i = n-2) down to 0:

For each i, check if t[i+1] - t[i] > c. If yes, then the group length is reset to 1. But wait, no. Because the group is the last contiguous sequence where all consecutive differences are <=c. So once a difference >c is found, the group before that is broken. So the correct approach is to start from the end and find the earliest position where a break (difference >c) occurs. Then the group is the elements after that break.

Alternatively, the group starts at the last element, and we check each previous element. If the next element (current element's next) minus current is <=c, then the group can be extended backward. Wait, no. Because the group must consist of consecutive elements where each adjacent pair is <=c. So the longest possible such group ending at the last element. So for example, if the last two elements are 19 and 20 (diff 1 <=5), then 14 and 19 (diff5 <=5), but 8 and 14 (diff6>5). So the group is from 14,19,20. So the group starts at 14, which is index 3 in the array.

So how to find the start of the group? We can iterate from the end and track the earliest start where all consecutive differences up to the end are <=c.

Wait, perhaps the correct way is:

The group must include the last element. Let's find the earliest index k such that t[k], t[k+1], ..., t[n-1] all have consecutive differences <=c. Then the answer is n -k.

So how to find k?

We can start from the end. Initialize k as n-1 (the last index). Then, for i from n-2 down to 0:

If t[i+1] - t[i] <=c, then the current i can be part of the group. So k is updated to i. Because the group can be extended backward as long as the difference between i and i+1 is <=c. Wait, no. Because for consecutive elements, all differences between i and i+1 must be <=c. But if we have a sequence like ... a, b, c, where b -a <=c, c -b <=c, then all are in the same group. But if during iteration, we check each step and track the earliest point where the next step is allowed.

Wait, perhaps the correct approach is to start from the end and work backwards. The last element is part of the group. Then, check the previous element (n-2) and see if t[n-1] - t[n-2] <=c. If yes, then include that element. Then check t[n-2] - t[n-3], etc. The first time we encounter a pair where the difference is >c, we stop. All elements after that (i+1 to end) are part of the group. So the group starts at i+1.

For example, in the first sample:

Check 20-19=1 <=5: yes. So group includes 19 and 20. Then check 19-14=5 <=5: yes. Group includes 14,19,20. Then check 14-8=6>5: no. So the group starts at 14 (index 3). So the answer is 3 elements.

In code, how to compute this? Let's think in terms of a loop.

We can iterate from the end (i = n-2) down to 0. For each i, compute t[i+1] - t[i]. If the difference is >c, then the group starts at i+1. So the answer is (n-1) - (i+1) +1 +1? Wait, (n-1) is the last index. (i+1) is the starting index. The number of elements is (n-1 - (i+1) +1) =n -i-1. For example, in the first sample, i=2 (since i+1=3), the count is 6-2-1=3, which is correct.

So the code can be written as:

Initialize the answer as 1 (the last element). Then, iterate from the second last element (i =n-2) down to 0. For each i:

If t[i+1] - t[i] >c, then break. The group starts at i+1. The answer is (n-1 - (i+1) +1) +1 =n -i -1. Because from i+1 to n-1, there are (n-1 - (i+1) +1) =n -i -1 elements. Wait, but when we break, the i is the index where the difference is >c. So the group starts at i+1. So the count is (n-1) - (i+1) +1 +1? Or is it (n-1) - (i+1) +1 +1?

Wait, no. The number of elements from i+1 to n-1 inclusive is (n-1) - (i+1) +1 =n -i -1. So if we break at i, then the group is from i+1 to end, which is n -i -1 elements. So the answer is n - i -1.

If we loop through all elements and never break (all differences <=c), then the answer is n.

So the algorithm can be implemented as:

Start with the answer as 1. Then, for i from n-2 down to 0:

if t[i+1] - t[i] >c:

   answer is n-1 - (i+1) +1 =n-1 -i -1 +1= n -i -1. Then break the loop.

else:

   increment the answer.

Wait, no. Because if all differences are <=c, then the answer would be n. Because each step increments the answer. Wait, initial answer is 1 (the last element). Then, for each previous element, if the next element (i+1) is within c, then the current element is part of the group. So the answer increases by 1. For example, in the first sample:

i=4 (element 19):

t[5]-t[4] =20-19=1 <=5: answer becomes 2.

i=3 (14):

t[4]-t[3]=5 <=5: answer becomes 3.

i=2 (8):

t[3]-t[2] =6>5: break. answer is 3. Which is correct.

Another example: if all elements are consecutive and differences <=c.

n=3, c=10, times 1,2,3.

Initialize answer=1.

i=1: t[2]-t[1]=1<=10: answer=2.

i=0: t[1]-t[0]=1<=10: answer=3.

Loop ends. answer is 3.

So the code would be:

answer =1

for i in reversed(range(n-1)):

   if t[i+1] - t[i] >c:

       break

   answer +=1

So this loop starts from the second last element (i=n-2) and checks each previous. If the difference is <=c, then the answer is increased by 1. Otherwise, break.

This approach seems correct and efficient. Because for n up to 1e5, iterating from the end once is O(n) time, which is acceptable.

So the plan is:

Read n and c.

Read the list of t's.

Initialize answer=1.

Iterate from i =n-2 downto 0:

   if t[i+1]-t[i] >c:

       break

   answer +=1

Print answer.

Yes. That's straightforward. Let's test this with the sample inputs.

Sample 1:

6 5

1 3 8 14 19 20.

Loop starts with i=4 (19):

t[5] -t[4] =1 <=5. answer becomes 2.

i=3 (14): t[4]-t[3] =5 <=5. answer 3.

i=2 (8): t[3]-t[2] =6>5. break.

answer is 3. Correct.

Sample 2:

6 1

1 3 5 7 9 10.

answer=1.

i=4 (9): t[5]-t[4]=1 <=1. answer=2.

i=3 (7): t[4]-t[3] =2>1. break.

answer is 2. Correct.

Another test case where all are within c:

n=3, c=5. times 1,2,3. answer is 3.

Yes.

Another case where only the last element is present. For example, n=1. Then answer is 1.

Yes.

So this approach works.

Now, considering the constraints: n can be up to 1e5, so iterating through all elements is O(n), which is acceptable. The code is efficient and straightforward.

So the Python code would be:

Read n, c.

t = list of integers.

ans =1.

for i in range(n-2, -1, -1):

    if t[i+1] - t[i] >c:

        break

    ans +=1

print(ans)

Yes.

This should handle all cases. For example, when there's a break early, like in the second sample, the code breaks when i=3 (since i is 4,3,2,...?) Wait, in the second sample, the elements are 1,3,5,7,9,10. n=6. i starts from 4 (n-2=4) down to 0.

i=4: t[5]-t[4] =1 <=1. ans becomes 2.

i=3: t[4]-t[3] =9-7=2>1. So break. ans remains 2.

So the code breaks here, returns 2.

Yes.

So the code is correct.

Now, considering the input constraints, the code is efficient. In Python, even with 1e5 elements, this loop will run in acceptable time. The input reading part is important. We need to read the list efficiently.

In Python, for large n, reading input via input().split() can be slow if not handled properly. So using sys.stdin to read the entire line is better. But given that n is up to 1e5, and the times are given as a list of integers, splitting the input properly is crucial.

So the code can be written as:

Read n and c from the first line.

Then read the next line as a list of integers.

Implement the loop.

So the code:

import sys

n, c = map(int, sys.stdin.readline().split())

t = list(map(int, sys.stdin.readline().split()))

ans = 1

for i in range(n-2, -1, -1):

    if t[i+1] - t[i] > c:

        break

    ans +=1

print(ans)

Yes. This should work.

Testing the code against the samples.

Sample 1:

Input:

6 5

1 3 8 14 19 20

The code reads the t as [1,3,8,14,19,20]. ans starts at 1.

Loop:

i=4: t[5]-t[4] =1 <=5 → ans=2.

i=3: t[4]-t[3] =5 → ans=3.

i=2: t[3]-t[2]=6>5 → break. So ans is 3. Correct.

Sample 2:

6 1

1 3 5 7 9 10

Loop:

i=4: t[5]-t[4]=1 → ans=2.

i=3: t[4]-t[3] =2>1 → break. ans=2. Correct.

Another test case: n=1 → ans=1.

Yes.

Another case where all differences are <=c. For example, n=4, c=5, times 1,2,3,4. ans=4.

Yes.

So the code works.
</think>

```python
import sys

n, c = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
ans = 1
for i in range(n-2, -1, -1):
    if t[i+1] - t[i] > c:
        break
    ans += 1
print(ans)
```