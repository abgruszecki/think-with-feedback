<think>
Okay, let's see. So the problem is about Tanya climbing stairways and counting the steps. Each stairway starts at 1 and goes up to x steps. The sequence given is the numbers she spoke. We need to find out how many stairways there were and the number of steps in each.

Hmm. So the key here is that each time she starts a new stairway, the count starts at 1 again. So the stairways are sequences that start with 1 and each subsequent number increments by 1. But the next stairway's 1 comes after. So the problem is to split the given sequence into such stairway sequences.

For example, in the first sample input: 1 2 3 1 2 3 4. The first stairway is 1,2,3 (so steps 3), then the next is 1,2,3,4 (steps 4). So the output is two stairways with 3 and 4 steps.

Another example is four 1's. That means four stairways each of 1 step.

So the approach is to find all the points where a new stairway starts. Each time we see a 1 (except the very first element), that's the start of a new stairway. So the steps for each stairway are the numbers from the start up to before the next 1. Also, the last stairway ends at the end of the list.

Wait, right. So the steps are:

1. Iterate through the list, split the list into sub-sequences each starting with 1, except the first element which is the start of the first stairway.

So for example, the input sequence can be split whenever a 1 is encountered (after the first element). Then each of these splits is a stairway.

So the algorithm would be:

- Initialize a list to hold the stairways.
- The first element is the start of the first stairway.
- Then, for each element after the first, check if it is 1. If yes, then the current stairway ends at the previous element. Add that stairway to the list, and start a new stairway with this 1.
- After processing all elements, add the last stairway (which starts at the last 1 found) to the list.

Each stairway's step count is the last element of the sub-sequence. Because each stairway is a sequence 1,2,...,x. So the last element of each sub-sequence is the x.

So the steps are:

Collect all the indices where a 1 occurs, except the first element. Then split the original array into parts between these indices, each part starts with a 1 (except the first part, which starts with the first element which is 1 if there's only one stairway, but wait the first element can be 1 if there are multiple stairways. Wait, the first element is always part of the first stairway, which starts at 1. Because the problem states that the sequence is valid. So the first element must be 1, right? Because the first stairway starts with 1. Otherwise, the sequence would be invalid.

Wait the problem says that the given sequence is valid, so the first element must be 1. Because otherwise, if the first element is greater than 1, that would imply that the first stairway started before, which isn't possible.

Wait, for example, if the input is 2, then the sequence would have to start with 1, because she starts counting from 1. So any input sequence must start with 1. Because the first stairway's steps start at 1. So the first element in the input is always 1.

Wait the problem statement says "the given sequence will be a valid sequence". So we can safely assume that the first element is 1. So in our code, the first element is part of the first stairway. Then, whenever a 1 is found again, it's the start of a new stairway.

So the code can proceed as follows:

- Initialize a list called stairways.
- The first stairway starts at index 0.
- Then, iterate through the list from index 1 to end. For each element a[i], if a[i] == 1, then the current stairway is from the previous start to i-1, and a new stairway starts at i.
- After processing all elements, add the last stairway (from the last start to end).

Each stairway is the sequence from start to end (inclusive). The steps for that stairway is the last element of the sequence. So for each stairway, the step count is the last element.

So for example, the input 1,2,3,1,2,3,4:

The splits are at index 3 (element 1). So first stairway is 0-2 (elements 1,2,3) → step count 3. Then the next stairway is 3-6 (elements 1,2,3,4) → step count 4.

So how to code this:

We can collect all the indices where a 1 occurs. Then split the array into segments between these indices, each starting with a 1.

Wait, but the first element is 1, so the list of split points starts with 0. Then other split points are where a[i] == 1 and i > 0.

For example, in the case where all elements are 1, like 1,1,1,1, the split points are 0,1,2,3. Then the stairways are each of length 1. Because each split is from i to i.

Wait, but in that example, the splits would be [0,1,2,3]. Then the stairways are from 0 to 0 (element 1), then 1 to 1 (element 1), etc. So each stairway is a single element.

So the code steps:

Collect all positions where a[i] is 1. Then, split the array into parts between these positions. Each part starts at a split point and ends before the next split point.

Wait, but the split points are the indices of 1's. So for example, if the split points are 0,3,6, then the stairways are the elements from 0 to 2 (split point next is 3), then 3 to 5 (split point next is 6), then 6 to end.

Wait no. Wait the split points are the start indices of each stairway. So the first stairway starts at 0, next at 3, etc. So the stairways are:

stairway 1: from 0 to 2 (since next split is at 3)
stairway 2: from 3 to 5 (next split is 6)
stairway 3: from 6 to end.

So each stairway is from split_point[i] to split_point[i+1] - 1.

Except the last one, which is from split_point[-1] to end.

So in code:

split_points = [0] + [i for i in range(1, len(a)) if a[i] == 1]

Then, for each i in 0 to len(split_points)-1:

start = split_points[i]
end = split_points[i+1]-1 if i < len(split_points)-1 else len(a)-1

So stairways are a[start..end], and the step count is a[end]

So the code can be:

n = int(input())
a = list(map(int, input().split()))

split_points = []
for i in range(n):
    if a[i] == 1:
        split_points.append(i)

stairways = []
for i in range(len(split_points)):
    start = split_points[i]
    if i == len(split_points)-1:
        end = n-1
    else:
        end = split_points[i+1] -1
    stairways.append(a[end])

print(len(stairways))
print(' '.join(map(str, stairways)))

Wait, let's test this logic with sample inputs.

Sample 1:

7
1 2 3 1 2 3 4

split_points = [0,3]. Then len is 2.

Loop i from 0 to 1.

i=0:

start=0. since i is not last (1 is last index?), wait len(split_points) is 2. i ranges from 0 to 1.

Wait for i in 0 to len(split_points)-1:

split_points is [0,3]. len is 2. So indices are 0 and 1.

i=0: start=0. next split is 3. end = 3-1=2. So a[0..2] is [1,2,3]. step is 3.

i=1: start=3. since i is last, end is 6. a[3..6] is [1,2,3,4]. step is 4. So stairways are [3,4]. Correct.

Sample 2:

4
1 1 1 1

split_points is [0,1,2,3]

for i in 0..3:

i=0: start=0, end=0 (split_points[1]-1=1-1=0). step is 1.

i=1: start=1, end=2-1=1. step is 1.

i=2: start=2, end=3-1=2. step is 1.

i=3: start=3, end=3 (n-1=3). step is 1.

So stairways [1,1,1,1]. Correct.

Sample 3:

5
1 2 3 4 5

split_points is [0]. So in loop, i=0 (only one element in split_points). end is 4. step is 5. Correct.

Sample 4:

5
1 2 1 2 1

split_points is [0, 2,4].

i=0: start 0, next split is 2. end=1. a[0..1] is [1,2]. step 2.

i=1: start 2. next split is4. end=3. a[2..3] is [1,2]. step 2.

i=2: start 4. end=4. a[4] is 1. step 1.

So stairways [2,2,1]. Correct.

Yes, this seems to handle all the cases.

Now, time and memory considerations. The input is up to n=1000 elements, which is manageable.

The code runs in O(n) time. Because collecting split_points is O(n), then processing split_points is O(m) where m is the number of stairways. Since m can be up to 1000 (if all elements are 1), but 1000 is manageable. So overall O(n) time.

Space is O(n) for storing the split points and stairways. But since n is up to 1000, it's okay.

So the code is efficient.

Now, code:

Read n, then the list a.

Collect split_points as all indices where a[i] is 1.

Then, for each split in split_points, determine the end, then append a[end] to the stairways list.

Then output the length and the stairways.

Yes.

So the code in Python would be:

n = int(input())
a = list(map(int, input().split()))

split_points = []
for i in range(n):
    if a[i] == 1:
        split_points.append(i)

stairways = []
for i in range(len(split_points)):
    start_idx = split_points[i]
    if i < len(split_points) - 1:
        end_idx = split_points[i+1] - 1
    else:
        end_idx = n - 1
    stairways.append(a[end_idx])

print(len(stairways))
print(' '.join(map(str, stairways)))

Testing all the samples:

Sample 1:

Input:
7
1 2 3 1 2 3 4

split_points = [0,3], stairways are a[0-2] end 2 (3), then a[3-6] end 6 (4). Output is 2 followed by 3 4. Correct.

Sample 4:

Input:
5
1 2 1 2 1

split_points = [0, 2,4]. For i=0: end is 1 (split_points[1]-1=2-1=1) → a[1]=2. Then i=1: end is 3 (split_points[2]-1=4-1=3 → a[3]=2. i=2: end is 4 → a[4]=1. So [2,2,1]. Correct.

Sample 2:

Input 4 1s. split points 0,1,2,3. Each iteration:

i=0: end 0 → a[0]=1.

i=1: end 1 → a[1]=1.

i=2: end 2 → a[2]=1.

i=3: end 3 → a[3]=1. So all 1s. Correct.

Yes, the code works.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

split_points = []
for i in range(n):
    if a[i] == 1:
        split_points.append(i)

stairways = []
for i in range(len(split_points)):
    if i < len(split_points) - 1:
        end = split_points[i+1] - 1
    else:
        end = n - 1
    stairways.append(a[end])

print(len(stairways))
print(' '.join(map(str, stairways)))
```