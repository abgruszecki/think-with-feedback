<think>
Okay, let's see. I need to find the maximum length of an increasing subarray where the elements are strictly increasing. And a subarray has to be consecutive, right? So the problem is about consecutive elements where each is larger than the previous. 

Hmm, the constraints say n can be up to 1e5. So any O(n) solution would work, but O(n^2) is definitely out of the question. So the approach needs to be linear time.

What's the optimal way here? Oh right, I remember that this is a classic problem. The idea is to iterate through the array and keep track of the current increasing subarray length. Whenever the current element is larger than the previous, we increment the current length. Otherwise, we reset it to 1 (since a single element is a subarray of length 1). Then, we just keep track of the maximum length found so far.

Wait, let's think about that. Let's take the first example: 1,7,2,11,15. 

Let's break it down:

Start at index 0 (1). Current length is 1, max is 1.

Index 1 (7): 7 >1 → current becomes 2. Max is 2.

Index 2 (2): 2 is not >7 → reset to 1. Max remains 2.

Index3 (11): 11>2 → current is 2. Max is 2, now current is 2, which is less than max. Wait, but then next index 4 (15) is larger than 11 → current becomes 3. So max becomes 3. Which matches the example output.

Yes, so this approach works. So the steps are:

Initialize max_len and current_len to 1.

Then iterate from the second element (index 1) to the end:

If a[i] > a[i-1], then current_len +=1, else reset to 1.

Update max_len each time.

This is O(n) time, O(1) space. Exactly what we need for the constraints.

Let's test the second example where all are 100. Each step, since a[i] is not greater than previous, current_len stays 1. So max remains 1. Correct.

Third example: 1,2,3. Each step increments current_len. So after first step current is 2, max 2. Then current becomes 3, max 3. Output is 3. Correct.

So the algorithm is straightforward.

Now, how to implement this in Python.

Read n, then the list.

Handle edge case where n is 0, but according to constraints, n is at least 1. So no problem.

Initialize max_length and current_length to 1.

Loop from 1 to n-1:

Compare a[i] and a[i-1].

If a[i] > a[i-1], increment current_length. Else, reset to 1.

Update max_length if current is larger.

Yes.

Now, for the code.

Read n as int(input()). Then read the next line as a list of integers.

Then the loop.

Now, code:

n = int(input())
a = list(map(int, input().split()))
if n ==0:
    print(0)
    exit()
max_len = 1
current =1
for i in range(1, n):
    if a[i] > a[i-1]:
        current +=1
        if current > max_len:
            max_len = current
    else:
        current =1
print(max_len)

Wait, but in the code, when we increment current, we have to check if it's the new maximum each time, not just in the else. Because maybe the current could be increasing and reach a new max. For example, in the case where the entire array is increasing. So in the code above, when a[i] is larger than previous, current increases. Then, after incrementing, we check if it's larger than max_len. Wait, no. The code as written only updates the max_len if current is larger than max_len. But in the code I wrote, after incrementing current, we check if current is larger than max_len. Wait, in the code:

current +=1 → then we check if current > max_len → if yes, update. But in the code, this check is done every time after incrementing. Because the code inside the 'if' clause is:

current +=1

if current > max_len:

    max_len = current

Wait, no. The code as written in the code I proposed earlier is:

if a[i] > a[i-1]:

    current +=1

    if current > max_len:

        max_len = current

Else:

    current =1

Wait, but that would check for max_len only when the current is increasing. But perhaps, after several increments, the current might have already passed the max_len. For example, consider a sequence where after a reset, the current increases again but not surpassing the previous max. Then, the code would not check after each increment.

Wait, no. Because in the code as written, after each increment, the code immediately checks if the current is larger than max_len. For example:

current is 2, max is 2.

Then, next element is larger: current becomes 3. Then, check if 3>2 → yes. Update max to 3.

So that's correct.

But what if the code didn't check after each increment? Let's see.

Alternative approach: in each iteration where the current increases, after incrementing, compare and update the max. So, for example:

current +=1

if current > max_len:

    max_len = current

That's what the code does. So this is correct.

But in other code structures, sometimes people update max_len in every iteration. Like:

current = current +1 if a[i] > a[i-1] else 1

then, compare current to max_len and update.

But in the code I wrote, the check is only when the current is incremented. Which is correct. Because when the current is reset to 1, that's smaller than the current max_len (since max_len is at least 1). So in that case, the code only needs to check when current is increased.

Wait, but suppose the current is 3, and the max_len is 3. Then, next element is larger: current becomes 4. So max_len is updated to 4.

Yes. So in this code, whenever the current increases, it's checked against the max. So no problem.

So the code should work correctly.

Testing the examples:

First example: 1,7,2,11,15.

i=1:7>1 → current=2 → max becomes 2.

i=2:2>7? No. current becomes 1. Max remains 2.

i=3:11>2 → current=2. Current is 2, which is not larger than max (2). So max stays 2. Wait, but in the code, after current increments to 2, the code checks if 2 > current max (2). No. So max remains 2. Then i=4:15>11 → current becomes 3. Then check if 3>2 → yes. Max becomes 3. So output is 3. Correct.

So the code is correct.

Another example: all 100s. For each i starting from 1, 100 is not >100 → current resets to 1. So max remains 1. Correct.

Third example: 1,2,3. For i=1, current becomes 2, max 2. i=2, current becomes 3, which is >2 → max 3. Correct.

So the code works.

Now, in terms of speed and memory.

The code reads the entire list at once. For n=1e5, that's acceptable.

The loop is O(n). So the code should handle the maximum constraints.

In Python, even for 1e5 elements, it's manageable.

So the code is optimal.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_len = current = 1
for i in range(1, n):
    if a[i] > a[i-1]:
        current += 1
        if current > max_len:
            max_len = current
    else:
        current = 1
print(max_len)
```