<think>
Okay, so I have this problem where I need to find the maximum length of a non-decreasing subsegment in a given array. Let me think about how to approach this.

Hmm, the problem is similar to finding the longest non-decreasing consecutive sequence. Oh right, because the subsegment has to be contiguous. So each element in the subsegment should be greater than or equal to the previous one.

The constraints are n up to 1e5. So whatever algorithm I use has to be O(n) time. Because if it's O(n^2), like checking every possible subsegment, that would be 1e10 operations which is way too slow. So I need an efficient approach.

Let me think of the optimal approach. The standard way for this kind of problem is to track the current length of the non-decreasing sequence as we iterate through the array.

For example, we can iterate from the first element to the last. For each position i, we check if a[i] >= a[i-1]. If yes, then the current length increases by 1. If not, then the current length resets to 1 (since the element itself is a subsegment of length 1). While doing this, we keep track of the maximum length encountered.

Yes, that sounds right. Let's see an example.

Take the first sample input: 2, 2, 1, 3, 4, 1. Let's see:

Start with the first element, current_length =1, max_length=1.

Second element 2 >= 2 → current_length=2, max becomes 2.

Third element 1 < 2 → reset to 1. Max remains 2.

Fourth element 3 >=1 → current_length=2. Now max is 2.

Fifth element 4 >=3 → current_length=3. Now max is 3.

Sixth element 1 <4 → reset to 1. Max stays 3.

So the answer is 3, which matches the sample.

Another example: 2,2,9. The current_length increases each step, so the maximum is 3. Correct.

So this approach should work. The time complexity is O(n), which is acceptable for n=1e5.

Now, how to implement this in Python.

The steps would be:

1. Read n.

2. Read the list of a's.

3. Initialize current_length and max_length to 1.

4. Iterate from index 1 to n-1:

   a. If a[i] >= a[i-1], increment current_length.

   b. Else, reset current_length to 1.

   c. Update max_length if current_length is larger.

5. After processing all elements, output max_length.

Yes. That's straightforward.

Now, edge cases:

- n=1 → output 1.

- All elements are strictly increasing → output n.

- All elements are same → output n.

- The longest sequence is at the end. E.g., 5,4,3,2,1,2,3 → the last two elements would give a sequence of 3, but after the 1, 2, 3. So the code would capture that.

What about a case where the maximum is found in the middle? Like 1,2,3,2,2,3. The first three give 3, then the 2,2,3 gives another 3. So the code would track the maximum correctly.

So this approach should handle all cases.

Now, code in Python.

Read n, then the list. Then iterate.

But wait, for large n, reading the input efficiently is important. So using input().split() can be a problem if the input is very large, but in Python, for 1e5 elements, it's manageable.

So code:

n = int(input())
a = list(map(int, input().split()))

if n ==0:
    print(0)
else:
    max_len = 1
    current =1
    for i in range(1, n):
        if a[i] >=a[i-1]:
            current +=1
            if current > max_len:
                max_len = current
        else:
            current =1
    print(max_len)

Wait, but in the code above, for each i, after incrementing current, we check if it's larger than max_len. That's correct. But what if the maximum is the last element in the array? Like the last elements form the longest sequence. For example, in the first sample, after the third element, the current is 1, then increases to 2, then 3, which is the max. So the code correctly captures that.

Yes. So this code should work.

Testing the first sample:

Input: 6 elements: 2 2 1 3 4 1

Process:

i=1 (a[1] =2 >=2 → current becomes 2, max is 2.

i=2: 1 <2 → current 1. max remains 2.

i=3: 3 >=1 → current 2. max not updated.

i=4:4 >=3 → current 3 → max becomes 3.

i=5:1 <4 → current 1. So output is 3.

Which is correct.

Second sample: 2 2 9.

i=1: 2 >=2 → current 2, max 2.

i=2:9 >=2 → current 3, max 3. So output is 3.

So all test cases pass.

So this code should work.

Now, considering the constraints. For n=1e5, this loop will run 1e5 times, which is acceptable in Python. The code uses O(1) space except the list a, which is necessary.

So the code is optimal.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_len = current = 1
for i in range(1, n):
    if a[i] >= a[i-1]:
        current += 1
        if current > max_len:
            max_len = current
    else:
        current = 1
print(max_len)
```