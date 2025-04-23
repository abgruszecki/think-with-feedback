<think>
Okay, let's see. The problem is that we have a binary number, and we need to delete exactly one digit to make the remaining number as large as possible. The output should be in binary without leading zeros.

Hmm, the key here is to find which digit to delete to maximize the value. Since binary is base 2, each higher bit is worth more. So, the leftmost digits have more weight. So, the strategy should be to delete the first occurrence where a digit is followed by a higher digit. Wait, wait. Because in binary, digits can only be 0 or 1. So higher digit here would mean a 1 comes after a 0. Because 1 is higher than 0.

Wait right. So, if we have a 0 followed by a 1, deleting the 0 would allow the 1 to move left, increasing the overall value. So the optimal approach is to find the first occurrence where a digit is 0 and the next digit is 1. Deleting that 0 would give a larger number. Because that 0 is followed by a higher digit, removing it would allow the higher digits to shift left, increasing the value.

But if there's no such occurrence (like all 1's followed by 0's, or all 1's), then we should delete the last occurrence. Because in that case, all digits are non-increasing. For example, if the number is '111', then deleting any of the first two 1's would leave '11', same as deleting the last one. But wait, no: '111' has three digits. Deleting any of them gives two 1's. So all options are same. But maybe if the number is '110', then deleting the third 0 would result in '11' which is better than deleting the second 1, which would leave '10'. So here, the optimal is to delete the first 0 possible, but if there's no such 0 followed by 1, then delete the last digit.

Wait, let's think. The general approach is: find the leftmost occurrence where a digit is followed by a larger digit. Then delete the first such digit. Because that would maximize the higher bits.

For example, in the first sample input '101'. Let's see each digit:

Index 0: '1', next is '0'. So no. The next digit is lower. So deleting index 0 would leave '01' which is 1, but leading zero, so output is '1'. But in the sample, the correct answer is deleting index 1 (the 0), leaving '11' which is 3. So how does that fit?

Ah right. The first example is '1' followed by '0' followed by '1'. So the digits are 1, 0, 1. So, the first occurrence where a digit is less than the next is the second digit (0), which is followed by 1. So deleting that 0 gives the maximum number. So the strategy is to find the first occurrence where a digit is followed by a higher digit, and delete that digit. If there is no such occurrence (like all digits are 1 followed by 0s), then delete the last digit.

Wait, but in a binary string, digits are 0 and 1. So when would a digit be followed by a higher one? Only when a 0 is followed by a 1. Because 0 < 1. So in the entire binary string, the first 0 that is followed by a 1 is the one we should delete. Because deleting that 0 allows the subsequent 1s to move left, increasing the value.

So the algorithm would be:

1. Iterate through each character in the binary string from left to right.
2. For each position i, check if the current character is '0' and the next character is '1'. Wait no, that's not right. Wait, if we have a '1' followed by a '0', then deleting the 1 would leave the 0, but maybe deleting the 0 later would be better. Hmm, perhaps the correct approach is to find the first occurrence where a digit is followed by a higher digit. Since in binary, the only possible case where a digit is followed by a higher one is when the current is 0 and the next is 1.

Wait, because 0 is followed by 1. So, for example, in the binary string '101', the digits are 1, 0, 1. The first occurrence where a digit is followed by a higher one is the 0 (digit 1) followed by 1 (digit 2). So deleting the 0 here gives '11', which is the maximum.

Another example: '110010' (the second sample input). Let's see. The string is 1,1,0,0,1,0. Looking for the first 0 followed by a 1. Let's see:

Positions:

0: 1 followed by 1. Not higher.

1: 1 followed by 0. Not higher.

2: 0 followed by 0. Not higher.

3: 0 followed by 1. Yes. So delete this 0 (position 3). The result is '11010' which is the sample output. Or wait, in the sample input, the correct answer is to delete either the third or fourth digit (0's) and get '11010'. Let's see. The input is 110010. So the digits are indices 0-5:

0:1, 1:1, 2:0, 3:0, 4:1, 5:0.

Looking for the first 0 followed by a 1. The first occurrence is position 2 (0) followed by 0 (no). Then position 3 (0) followed by 1 (position4). So delete position3. The result is 11010.

Alternatively, if the code deletes the first occurrence where a digit is less than the next, which is the first 0 followed by 1. So in the sample, the first occurrence is index3.

So the algorithm is:

Loop through the binary string from left to right.

Find the first occurrence where s[i] < s[i+1]. Then delete s[i].

If no such occurrence exists (like the string is non-increasing), then delete the last character.

Because in that case, all digits are 1 followed by 0s, but in a non-increasing order. So deleting the last character would remove the smallest possible.

Wait, for example, '1110'. The digits are 1,1,1,0. Here, there's no occurrence of a digit followed by a higher one. So we delete the last digit (0), resulting in '111'.

Another example: '1000'. Here, the digits are 1,0,0,0. The first occurrence is 1 followed by 0 (no). Then 0 followed by 0, etc. So no occurrence. So delete the last 0, resulting in '100'.

But another case: '1101'. Here, the digits are 1,1,0,1. The first occurrence where s[i] < s[i+1] is at index 2 (0 < 1). Deleting index2 gives '111' which is better than any other deletion. So yes.

So the approach is:

- Iterate through the string from left to right. For each index i from 0 to len(s)-2:

   if s[i] < s[i+1], then delete s[i], return the string after deletion.

- If no such i found, delete the last character.

So how to implement this efficiently?

The input can be up to 1e5 characters, so we need an O(n) solution.

So steps:

1. Convert the input string into a list for easier manipulation? But in Python, strings are immutable, so creating a new string each time is O(n) time. So perhaps better to iterate through the characters and find the index to delete, then construct the new string by skipping that index.

So first, find the index to delete.

Initialize found = False.

Loop i from 0 to len(s)-2:

   if s[i] < s[i+1], then mark to delete i, break.

If found, then delete i. Otherwise, delete len(s)-1.

Then construct the result by omitting that index.

For example, in '101' (indices 0,1,2):

Check i=0: s[0] is '1', s[1] is '0' → 1 < 0? No.

i=1: s[1] is '0', s[2] is '1' → 0 < 1 → yes. Delete index1. Result is '11'.

In '110010', check each i:

i=0: s[0] =1, s[1] =1 → no.

i=1: s[1]=1, s[2]=0 → no.

i=2: s[2]=0, s[3]=0 → no.

i=3: s[3]=0, s[4]=1 → yes. Delete index3. So the result is s[:3] + s[4:] → '110' + '10' → '11010'.

Which matches the sample.

Another example: '111' → loop through i=0 and 1. No s[i] < s[i+1]. So delete last character. Result '11'.

Another example: '10' → s[0] is 1, s[1] is 0. No occurrence. So delete last character. Result '1'.

Wait, but in '10', the best is to delete '0', giving '1', which is correct.

Another example: '1000' → loop through. At i=0, 1 vs 0: no. i=1: 0 vs 0: no. i=2: 0 vs 0: no. So delete last character. Result '100'.

So yes.

So the algorithm seems correct.

Now, implement this.

Now, code steps:

Read the input string s.

Loop over each i from 0 to len(s)-2:

   if s[i] < s[i+1], then delete i and return s[:i] + s[i+1:].

If no such i found, return s[:-1].

But in Python, string concatenation is O(n). So for a string of 1e5 characters, creating a new string would take O(n) time. But since we're only creating the new string once, the time should be manageable.

But how to find the index i efficiently.

So, code:

s = input().strip()

n = len(s)

index_to_delete = n-1  # default to last character

for i in range(n-1):

    if s[i] < s[i+1]:

        index_to_delete = i

        break

result = s[:index_to_delete] + s[index_to_delete+1:]

print(result)

Wait, but in the loop, once we find the first occurrence where s[i] < s[i+1], we break. So that gives the first such index. Then we delete it.

Yes. Let's test with the first sample:

Input '101' → n=3.

Loop i=0 to 1.

i=0: s[0] is '1', s[1] is '0' → not less.

i=1: '0' < '1' → yes. index_to_delete=1. break.

result is s[:1] + s[2:] → '1' + '1' → '11'. Correct.

Second sample: '110010' → i goes up to 4.

Check i=0: 1 <1 → no.

i=1: 1<0 → no.

i=2: 0<0 → no.

i=3: 0<1 → yes. index_to_delete=3. break.

result is s[:3] + s[4:] → '110' + '10' → '11010'. Correct.

Another test case: '1110' → index_to_delete is 3 (since no s[i]<s[i+1] in 0,1,2. So default to 3 (n-1=3). result is s[:3] → '111'.

Another test case: '10' → i=0: 1 <0 → no. So delete index 1 (n-1=1). result is s[:1] → '1'.

Yes.

Another test case: '011' → but the input can't have leading zeros. So input is given without leading zeros. So the code doesn't have to handle that.

So the code seems correct.

Now, about the performance. The loop is O(n), which for 1e5 is acceptable. The string concatenation is O(n) time. So overall O(n) time.

Space-wise, the input is stored as a string, and the result is built by concatenating two substrings. For 1e5 characters, that's acceptable.

But in Python, string concatenation can be optimized. But in this case, since we're only doing two slices and then combining, it's O(n) time.

Thus, the code should work efficiently for the constraints.
</think>

```python
s = input().strip()
n = len(s)
index = n - 1  # default to last character
for i in range(n - 1):
    if s[i] < s[i + 1]:
        index = i
        break
print(s[:index] + s[index + 1:])
```