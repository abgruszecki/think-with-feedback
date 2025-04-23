<think>
Okay, I need to solve this problem where I have to find the maximum number of continuous hours Polycarp rests, considering that the schedule repeats daily. Let's see.

The problem says that the days repeat endlessly. So the rest periods could wrap around from the end of one day to the start of the next. For example, if the last hour is rest and the first hour is rest, combining those across days would make a longer rest period. 

Hmm, so the key is to check all possible sequences of rest hours, including those that wrap around. But how do I efficiently compute this?

First, the straightforward approach would be to check all possible consecutive 1s in the array. But since the array is circular (because days repeat), the maximum could be in the middle of the array, or it could be a combination of the end and the beginning.

But wait, the array's maximum might already be the answer if there are no wrap-around cases that give a longer sequence. For example, in the third sample input, the maximum is 3 consecutive 1s in the middle. But in the first sample, the maximum is 2 by combining the last hour (1) and the first hour (1) of the next day.

Wait, the first sample input is [1,0,1,0,1]. So the rest hours are at positions 0, 2, 4. The consecutive in the array are 1, then 1, then 1. But when the day repeats, the last hour (1) is followed by the first hour (1) of the next day. So that's two 1s in a row. So the maximum is 2.

So, how to model this?

I think the approach is to consider the array as a circular buffer, where after the last element comes the first again. But how to handle sequences that wrap around?

One way is to concatenate the array with itself, so that sequences that wrap around can be found as a continuous sequence in the doubled array. For example, the array [1,0,1,0,1] when doubled becomes [1,0,1,0,1,1,0,1,0,1]. Then, the maximum sequence of 1s would include the last 1 of the first part and the first 1 of the second part. But since the array is repeated twice, the maximum sequence that spans the boundary would be found here.

However, there's a catch. Since the days repeat endlessly, the maximum sequence could be longer than the array. For instance, if all elements are 1 except one 0. Then, the maximum sequence would be (n-1)*2? Wait, no. Wait, if all are 1 except one 0, then each day's rest is (n-1) 1s. But when days repeat, the maximum consecutive would be (n-1) *k, where k is any number of days. Wait, but the problem says to find the maximal number of continuous hours. So that's infinite? But no, the problem states that there is at least one 0 in the array. So the example given is when there's at least one 0. So that case where all are 1s is impossible.

So in our problem, since the array has at least one 0, the maximum possible consecutive 1s can't be infinite. So for example, if the array is [1,1,1,0], then the maximum is 3 (the three 1s) plus the three 1s from the next day, but the 0 breaks it. Wait, no. Because in the next day's array, after the 0 comes the 1s again. Wait, no. The array is [1,1,1,0], so each day starts with 1,1,1,0. So when the day ends with 0, the next day starts with 1 again. So the consecutive 1s would be 3 (from the start of the day), then 3 again. But between the days, the 0 and 1 are not consecutive. So the maximum is 3.

But if the array is [1,1,1,1], but the problem states that there's at least one 0, so that case is not possible.

So, how to model the maximum sequence considering the wrap-around? Let's think of the array as a circular arrangement. The maximum rest period could be either:

a) a sequence entirely within a single day (non-wrapping), like in the third example.

b) a sequence that starts near the end of the day and wraps around to the start of the next day.

But how do I compute the maximum possible length?

An approach could be:

- Compute all the sequences of consecutive 1s in the original array. Keep track of the maximum length.

- If the array starts and ends with 1s, then the maximum possible wrap-around sequence would be the sum of the leading and trailing 1s in the array, because those would be consecutive when days repeat. But since the days repeat endlessly, the wrap-around could also involve multiple days. Wait, no. Because the wrap-around can only connect the end of one day to the start of the next. So the maximum possible wrap-around sequence would be the sum of the trailing 1s of the array and the leading 1s. Because when days repeat, those are consecutive.

For example, if the array ends with k 1s and starts with m 1s, then combining these gives k + m consecutive 1s. But if the entire array is all 1s except for a single 0, then the maximum would be (n-1) * 2? Wait no, because the 0 is in between. Wait, no. Let's take an example: array is [1,1,0,1,1]. Then, the trailing 1s at the end are 2 (the last two elements). The leading 1s are 2 (the first two elements). So combining them gives 4. But in this array, the maximum sequence would be 2 (the two leading 1s plus the two trailing 1s from the next day) = 4. But if the array has a longer sequence in the middle, that might be bigger. But in this example, there's a 0 in between. So the maximum possible is 4.

Wait, but the array is [1,1,0,1,1], then the trailing 1s are 2, leading 1s are 2. So the wrap-around gives 4. The maximum non-wrap-around is 2. So the maximum is 4.

So the algorithm is:

- Compute all consecutive 1s in the original array, track the maximum length.

- Compute the leading 1s (number of 1s at the start of the array).

- Compute the trailing 1s (number of 1s at the end of the array).

- If leading + trailing is greater than the current maximum, update the maximum. However, this is only possible if leading + trailing is a valid sequence. For example, if the entire array is all 1s (but the problem states that there's at least one 0, so this case isn't possible). But when the array starts and ends with 1s, then the wrap-around gives a possible longer sequence.

But how?

So, the steps would be:

1. Find all the runs of consecutive 1s in the array.

2. Find the maximum length among these runs.

3. Check if the array starts with 1s and ends with 1s. If so, then the sum of leading and trailing 1s could be a candidate for maximum.

4. The maximum between step 2 and step 3 is the answer.

But why?

Because the wrap-around scenario is when the last part of the array and the first part are both 1s. So, if the array is like [1,1, ... ,1,1], but since there is at least one 0, that's not possible. So, when the array starts and ends with 1, then those two runs (leading and trailing) can be combined when days repeat. For example, array is [1,0,1,1], trailing 2, leading 1. So the sum is 3. But in the array, the maximum is 2. So the answer would be 3.

But if the array is [1,1,0,1], trailing 1, leading 2. Sum is 3. So the maximum is 3.

So, the algorithm needs to take into account this leading and trailing sum.

So, the plan is:

- Compute the maximum run of 1s in the array.

- Compute the leading count (left) and trailing count (right).

- If left + right is larger than the current max, and the array has runs at both ends (i.e., leading and trailing are non-zero), then the max is left + right.

But why? Because in that case, when the days repeat, those leading and trailing 1s would be contiguous.

But what if the array is all 1s except one 0? Wait, but the problem says that there's at least one 0. Suppose the array is [1,1,0,1,1]. Then, the leading is 2, trailing is 2. Sum is 4. The max run in the array is 2. So the answer is 4. But in the original array, the runs are 2, 0, 2. The maximum is 2. So the correct answer would be 4.

So yes, adding leading and trailing would give the correct answer in that case.

But another example: array is [1,0,1]. Then leading is 1, trailing is 1. Sum is 2. The max in the array is 1. So answer is 2.

So this approach works.

So, the steps are:

1. Check if the array is all 0s. But the problem says there's at least one 0, but the array can have all 0s except that. Wait, no. The problem says that the array has at least one 0, but it can have all 0s except for some 1s. Wait, no. Wait, the problem says: it's guaranteed that a_i=0 for at least one i. So there's at least one 0. So in the array, there's at least one 0. So if all a_i are 0 except some, but there's at least one 0. Wait, but in that case, all a_i are 0. Then the answer is 0, since all are working hours. But according to the problem statement, the array has at least one 0. So that's possible. For example, the fourth sample input is all 0s, and the output is 0.

So, in the code, first, let's handle all 0s. If the array has all 0s, then the answer is 0. But the problem says that there's at least one 0, but the code can proceed.

But in any case, the code must handle that.

So, code steps:

Read n.

Read the array.

Compute the maximum run of 1s in the array.

Compute leading_ones: count leading 1s.

Compute trailing_ones: count trailing 1s.

If leading_ones + trailing_ones > max_run and (leading_ones >0 and trailing_ones >0), then the answer is the maximum between max_run and (leading_ones + trailing_ones). Otherwise, the answer is max_run.

Wait, but why the condition that leading and trailing are >0? Because if one of them is zero, then their sum is zero or the same as the other. So for example, if the array starts with 0, then leading_ones is zero, and sum would be trailing_ones. But trailing_ones is already considered in the runs, so adding leading_ones (zero) doesn't help.

So the condition is that the array starts and ends with 1s, which is equivalent to leading_ones >0 and trailing_ones >0.

So in code:

if leading_ones > 0 and trailing_ones > 0:

    candidate = leading_ones + trailing_ones

    if candidate > max_run:

        max_run = candidate

So, after computing the maximum of the runs and the candidate, that's the answer.

But how to compute the runs of 1s in the array?

We can iterate through the array, keeping track of the current run. Whenever we encounter a 1, increment current_run. Otherwise, reset current_run to 0. Keep track of the maximum during this process.

Yes.

So, code steps:

Initialize current_run = 0, max_run = 0.

for num in a:

    if num == 1:

        current_run +=1

        if current_run > max_run:

            max_run = current_run

    else:

        current_run =0

Then, compute leading_ones and trailing_ones.

leading_ones is computed by counting from the start until the first 0.

trailing_ones is computed by counting from the end until the first 0.

So code for leading_ones:

i =0

while i < n and a[i] ==1:

    leading_ones +=1

    i +=1

Similarly for trailing_ones:

j = n-1

while j >=0 and a[j] ==1:

    trailing_ones +=1

    j -=1

Then, check if leading_ones and trailing_ones are both positive. If so, compute the sum and compare with max_run.

But what if the entire array is 1s? According to the problem statement, that's impossible. So the code doesn't need to handle that case.

So, after all these steps, the maximum is the answer.

Let's test this approach against the samples.

First sample:

5

1 0 1 0 1

The runs are:

1 (run ends at index 0)

0 (run ends)

1 (run starts at 2, length 1)

0 (run ends)

1 (run starts at 4, length 1)

So max_run is 1.

Leading_ones is 1 (starts with 1, then 0).

Trailing_ones is 1 (ends with 1, then 0 before that).

So sum is 1 +1 =2. Since both are >0, candidate is 2. So the max becomes 2.

Which matches the first sample's output.

Second sample:

6

0 1 0 1 1 0

The runs are:

0 (run 0)

1 (length 1)

0 (run 0)

1 (length 2)

0 (run 0)

So max_run is 2.

Leading_ones is 0 (since first element is 0).

Trailing_ones is 0 (last element is 0). So no candidate. So answer is 2. Which matches the sample.

Third sample:

7

1 0 1 1 1 0 1

Runs:

1 (run length 1)

0 

1,1,1 (run length 3)

0 

1 (run length 1)

max_run is 3.

Leading_ones is 1 (starts with 1, then 0).

Trailing_ones is 1 (ends with 1, previous is 0).

Sum is 2. So candidate is 2. So the max remains 3. Which matches the sample.

Fourth sample:

3

0 0 0

max_run is 0.

leading and trailing are 0. So candidate is 0. Answer is 0.

Another test case: array [1,1,0,1,1]

Runs are 2, then 0, then 2. max_run is 2.

Leading is 2, trailing is 2. sum is 4. So candidate is 4. So answer is 4.

Yes.

Another case: [1,1,1,0,1,1,1]. So the runs are 3, 0, 3. max_run is 3. leading is 3, trailing is 3. sum is 6. So answer is 6. Which is correct, because when days repeat, those 3 at the end and 3 at the start would form 6 consecutive 1s.

So the code should work.

Now, how to implement this efficiently for large n (up to 2e5)?

The code I described is O(n) time and O(1) space (assuming the array is read as a list). So it's acceptable.

So, the code steps:

Read n.

Read the array as a list of integers.

Compute max_run by iterating through the array once.

Compute leading_ones and trailing_ones.

Check if leading and trailing are both >0. If so, compute the sum and compare with max_run.

Print the maximum between max_run and the sum (if applicable).

Now, code:

In Python, the input can be read via input().split(), but for large n, we need to read it efficiently. So for n up to 2e5, using list(map(int, input().split())) is okay.

But the code must handle leading and trailing 1s.

So code:

n = int(input())

a = list(map(int, input().split()))

# Compute max run of 1s

max_run = 0

current = 0

for num in a:

    if num ==1:

        current +=1

        if current > max_run:

            max_run = current

    else:

        current =0

# Compute leading_ones

leading =0

i =0

while i <n and a[i]==1:

    leading +=1

    i +=1

# Compute trailing_ones

trailing =0

j =n-1

while j >=0 and a[j]==1:

    trailing +=1

    j -=1

# Check if leading and trailing are both >0

if leading >0 and trailing >0:

    candidate = leading + trailing

    if candidate > max_run:

        max_run = candidate

print(max_run)

Wait, but what if the entire array is 1s? Well, the problem states that the array has at least one 0. So this case is impossible, so the code is safe.

Testing this code on the samples:

Sample 1:

5

1 0 1 0 1

max_run is 1 (each 1 is isolated).

leading is 1, trailing is 1. sum is 2. So answer is 2. Correct.

Sample 2:

6

0 1 0 1 1 0

max_run is 2. leading and trailing are 0. So answer is 2. Correct.

Sample 3:

7

1 0 1 1 1 0 1

max_run is 3. leading is 1, trailing is 1. sum is 2. So answer remains 3. Correct.

Sample 4:

3

0 0 0

max_run is 0. leading and trailing are 0. So answer is 0. Correct.

Another test case [1,1,0,1,1]. max_run is 2. leading 2, trailing 2. sum 4. Answer is 4.

Another test case [1,0,1,1]. leading 1, trailing 2. sum 3. max_run in array is 2. So answer is 3.

So code works.

Now, the code is O(n) time and O(n) space (since it stores the array). For n=2e5, it's acceptable.

So, this should be the correct approach.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

max_run = current = 0
for num in a:
    if num == 1:
        current += 1
        if current > max_run:
            max_run = current
    else:
        current = 0

leading, trailing = 0, 0
i = 0
while i < n and a[i] == 1:
    leading += 1
    i += 1

j = n - 1
while j >= 0 and a[j] == 1:
    trailing += 1
    j -= 1

if leading > 0 and trailing > 0:
    candidate = leading + trailing
    if candidate > max_run:
        max_run = candidate

print(max_run)
```