<think>
Okay, let's see. The problem is to decode a binary string according to Polycarp's encoding method. So first, I need to understand how the encoding works so that I can reverse it.

From the description, each digit in the original number is converted to a number of '1's equal to the digit's value. Then, the digits are separated by a single '0'. Except for zero, which is zero '1's followed by a '0'. Wait, but zero as a digit would be represented by zero '1's, but then followed by a 0. But the problem says the encoded string represents a positive integer. So the original number can't have leading zeros, but individual digits can be zero? Wait, wait. Wait, the original number is a positive decimal number. So the digits are from 0 to 9, except that the first digit can't be zero. Because if the original number is 0, it's not positive. So the input string encodes a number where each digit is represented by that many 1's, then separated by 0's. Except that the last digit's separator might not be there. Because, for example, the first sample input is '111' which is 3. So the encoding for 3 is three 1's. But according to the algorithm, each digit is written with '1's equal to the digit, then separated by a '0'. So for a single digit, there's no separator. Because the separator is between digits. So the overall structure is that the encoded string is a sequence of groups of 1's, separated by 0's, but the number of groups would correspond to the number of digits. Because each digit is followed by a 0, except the last one. Wait, no. Let's think again.

For example, take the number 2031. Let's see the encoding. Each digit is converted as follows:

2 → '11', then add a 0.
0 → zero '1's, then add a 0.
3 → '111', then add a 0.
1 → '1'. But since it's the last digit, no 0 is added.

Wait, no. Wait, according to the problem statement, the algorithm is: each digit is represented by that many 1's. Then, digits are written one by one, separated by a single 0. So the separator comes between the digits. So for the example 2031:

Digits are 2, 0, 3, 1.

So:

2 → two 1's (11), followed by a 0 (so '110').

0 → zero 1's (so nothing), followed by a 0 (so '0').

3 → three 1's (111), followed by a 0 (so '1110').

1 → one 1 (1), no 0 because it's the last digit.

So the entire string is '110' (from 2) + '0' (from 0) + '1110' (from 3) + '1' (from 1). Let's see:

'110' + '0' is '1100', then + '1110' is '110001110', then + '1' → '1100011101'. The sample input 9 has string '110011101' which is length 9 and output 2031. Wait, perhaps the example is for 2031. Let me check the second sample:

Sample input 2:
9
110011101
Output: 2031.

Breaking down the input string: 11 0 0 111 0 1.

Wait, maybe the string is split into groups of 1's separated by 0's. So the encoded string is split by the 0's into parts. Each part (except maybe the last) is the 1's of a digit, followed by a 0. Wait, but the 0's are the separators between digits. So between two digits, there is exactly one 0. For example, the first example is 3 → encoded as '111' (no 0s, since it's a single digit). The second sample's string is 110011101. Let's split on 0s. Let's see:

The string is '11' followed by '0', then another '0' (so the next split would be between the two 0s?), but the splitting on 0s would create parts. Let's see:

Breaking '110011101' into parts separated by 0s:

- The first part is '11' (before the first 0)
- Then the next is '' (because after the first 0, there's another 0, so between the two 0s is nothing)
- Then the next part is '111' (after the second 0, up to the next 0)
- Then '1' (after the third 0, but there's no more 0s after that).

Wait, perhaps the encoded string is split by each 0 into the parts representing the digits. But since each digit (except the last) is followed by a 0, the splitting would split the string into parts where the first k-1 parts (for a k-digit number) are the digits, and the last part is the last digit. Wait, no. Because the digits are separated by 0s, so between digits there is a 0. So the 0s are the separators. So the encoded string can be split into groups of 1's separated by 0s. However, the last group does not have a 0 after it. So for example, in the first sample (111), there's no 0, so the entire string is the first (and only) digit, which is three 1's → 3.

In the second sample, the string is '11 0 0 111 0 1' → wait, perhaps splitting on 0s gives:

Looking at the string '110011101', the 0s are at positions 2, 3, and 6 (assuming the string is indices 0-8):

Indices 0: '1', 1: '1', 2: '0' → first split.
Then index 3 is '0' → next split.
Then indices 4-6: '1','1','1' followed by a 0 at index 6.
Then after index 6, index 7 is '1', and index 8 is '1'?

Wait, the string is '110011101' → let's see:

Breaking down the string:

Indices 0-8:

0:1, 1:1 → '11' followed by 0 at 2.

Then index 3 is 0 → next 0.

Then index 4:1, 5:1, 6:1 → '111' followed by 0 at 7? Wait, no. Wait the string is 110011101: let's write the characters:

1 1 0 0 1 1 1 0 1.

So the 0s are at positions 2, 3, and 7.

So splitting on 0s:

First part: '11' (positions 0-1).

Then split at 2 → next part is positions 3 (but position 3 is 0 → so next split is here. So the parts would be:

After the first 0 (position 2), the next 0 is at position 3. So the second part is from position 2+1=3 to position3-1=3 (since the 0 is at 3). So the part is from 3 to 2 → which is nothing. So the second part is empty. Then the next 0 is at 7.

So the parts after splitting on 0s would be:

'11', '', '111', '1'.

But how to process this.

Wait, the split on 0s would generate all the groups of 1's between the 0s. So each group is between the 0s.

But in this case, the original string has 0s as separators between digits. So each 0 in the encoded string is a separator between two digits, except possibly after the last digit. Wait, but the encoded string may end with a 0? But according to the problem statement, the input string is guaranteed to correspond to a positive number. So the original number's digits cannot have leading zeros, but individual digits can be zero.

Wait, for example, the digit zero is represented by zero '1's followed by a 0. But when a zero digit is the last digit, then the encoding would end with a 0. Because the zero's encoding is zero '1's followed by a 0. But the problem says the input string is guaranteed to correspond to a positive number. So the encoded string could end with a 0 only if the last digit is zero, but that would make the original number have a zero as the last digit, which is allowed. For example, the number 20 would be encoded as '11' (for 2) followed by '0' (the separator), followed by zero '1's (for 0) followed by a '0' (the separator). Wait, no. Wait, according to the encoding rules:

Each digit is written as '1's equal to its value, followed by a single '0' as a separator between digits. So for the number 20:

Digit 2: two '1's → '11', followed by a '0' (so '110').

Digit 0: zero '1's, followed by a '0' (since it's not the last digit? Wait, but if 0 is the last digit, then no '0' is added. But in the case of 20, the digits are 2 and 0. So after the 2's encoding (110), the 0's encoding is zero '1's, followed by a '0' (since it's not the last digit?), but wait, 0 is the second digit (the last one). So for the digit 0 in the number 20, since it's the last digit, we do not add the 0. So the encoding would be '110' (from 2) followed by a '0' (the separator?), but wait, that's not right. Wait, the algorithm says that digits are written one by one in order, separated by a single '0' character. So each digit's '1's are followed by a '0' if there is another digit after. So for the digits 2 and 0:

After 2's '11', we add a '0' (separator). Then the 0 is represented by zero '1's. Since there are no more digits after, we don't add another '0'. So the entire encoding would be '1100' → because 2's part is '11' + '0' (separator), then 0's part is zero '1's, no separator. So the total is '1100'? But that would be for the number 20. Then the decoding of '1100' would be 2 and 0. But wait, the separator is between digits. So between the 2 and 0, there's a single '0'. Then the 0's part has zero '1's, so nothing. So the encoded string would be '110' followed by nothing. Wait, no. Let me think again.

Wait, when you have two digits, the first digit's '1's are followed by a '0' (separator), then the second digit's '1's. So for 20, the first digit is 2 (11) followed by a 0 (separator), then the second digit is 0 (zero '1's). So the encoded string is '1100' → the two digits are 2 and 0, separated by a 0. But the second digit's part has zero '1's, so the separator between the digits is the 0. So the entire string is '110' (from 2 and separator) followed by the 0's part, which is zero '1's. But since there's no separator after the last digit, the encoded string would be '1100' → but that's 11 followed by 00. Wait, perhaps the separator is between digits. So for two digits, there is one separator. So for 2 followed by 0, it's 11 (digit 2) + 0 (separator) + 0 (digit 0). Wait, but the digit 0 has zero '1's, so after the separator, there's nothing. So the encoded string is '1100'? But then when decoding, how to split it into digits?

So for '1100', the split would be:

Groups separated by 0s: first '11', then the next group is after the first 0. So the split would be '11', '0' (the part after the first 0 is between index 2 and index 3, which is '0'). So the groups are '11', '0', and then nothing. Wait, but the string is '1100', so splitting on 0 gives ['11', '0', ''].

But how to interpret that. Each group between the 0s (including the parts before the first 0 and after the last 0) would represent the digits.

Hmm. This is a bit confusing. So perhaps the correct way to split the encoded string into digits is to split the entire string into runs of 1's and 0's, and process them accordingly.

Alternatively, perhaps the approach is to split the string into the digits by looking at the 0's as separators. However, since the 0's are between the digits, the number of digits would be the number of 0's plus one. Wait, no. Because between k digits, there are k-1 separators. So for example, two digits have one 0 separator. So the number of 0's in the encoded string is (number of digits -1) plus any 0's that are part of the digits (like in the case of a 0 digit). Wait, no. Because according to the encoding rules, the digits are written with their 1's, followed by a 0 only if there's another digit after. So the 0's in the encoded string are exactly (number of digits - 1), because each separator is between two digits. But how about when a digit is 0? For example, the digit 0 is encoded as zero 1's followed by a 0 only if it's not the last digit. So if the digit 0 is followed by another digit, then the separator 0 is present. If it's the last digit, then no separator. But in that case, the digit 0's encoding is zero 1's, and no 0. So the encoded string would have a 0 separator between the previous digit and the 0, but the 0 digit itself contributes nothing except the separator (if it's not the last digit).

Wait, this is getting complicated. Let's think of the encoding process step by step.

Take the digits as a list d_1, d_2, ..., d_k.

For each digit d_i (i from 1 to k-1):

- append (d_i) '1's followed by a '0'.

For the last digit d_k:

- append (d_k) '1's.

So the encoded string is the concatenation of these parts.

So for example, the digits 2, 0, 3, 1:

First three digits (2,0,3) are each followed by a 0. The last digit (1) is not.

So encoding:

2 → '11' + '0' → '110'

0 → '' (zero 1's) + '0' → '0'

3 → '111' + '0' → '1110'

1 → '1'

So concatenated: '110' + '0' + '1110' + '1' → '110011101' → which matches the second sample input. And the output is 2031, which is correct.

So, in the encoded string, the 0's are the separators between digits. Each separator is part of the encoding of the previous digit, except for the last digit. So to split the encoded string into digits, we need to split the string into parts where each part is a group of '1's followed by a '0' (for non-last digits) or a group of '1's (for the last digit). But how to do this.

Alternatively, the encoded string can be viewed as a sequence of groups, each being a run of '1's followed by a '0' (except the last group, which is a run of '1's with no '0' after). So to split the string into digits, we need to split the string into these groups. Each group (except the last) is a run of '1's followed by a '0'. The last group is a run of '1's.

But how to split the string into these groups.

Another approach is to traverse the string and split it into these groups. For example:

Start with the first character. Read as many '1's as possible until a '0' is encountered. That's the first digit (the number of '1's). Then, the '0' is the separator. Then, continue reading the next group of '1's until the next '0', and so on. The last group is when there are no more '0's after it.

But wait, the problem is that the 0's are part of the separators between digits. So each group (except the last) is a run of '1's followed by a '0'. So the encoded string is a sequence of (run of 1's + '0') pairs, except the last group which is a run of 1's with no '0'.

So for example, in the second sample input '110011101', the groups are:

11 followed by 0 (first group → digit 2)

0 followed by 0 (but after that, the next part is 111 followed by 0 → but wait, this is getting a bit messy.

Alternatively, the groups are formed by splitting the string after each '0' that serves as a separator. So each group is a run of '1's, followed by a '0' (except the last group, which is a run of '1's with no '0').

But how to split the string into these groups.

Let's think of the string as being constructed by the digits' groups. Each non-last digit's group is (1's) followed by a 0. The last digit's group is (1's). So the entire string is a concatenation of these groups. So the split points are after each 0 that is part of a separator.

So for example, in '110011101', the groups are:

- '11' followed by a 0 → first group, digit 2.

Then, the next group starts. But the next character is 0. So according to the encoding, this 0 is the separator for the next digit (0). So after the first group (11 followed by 0), the next group is the 0 (separator) between 2 and 0. Wait, no. Wait, the first group is the 2's 11 followed by a 0 (separator). Then the next group is for the 0 digit: since 0 is a digit, it is followed by a 0 only if there's another digit after. So for 0 as the next digit (in 20, for example), the 0's encoding would be zero 1's followed by a 0 (if there's another digit after). But in the case of 2031 (second sample), the 0 is followed by 3 and 1.

So for the group after the first 0 (separator), the 0 is part of the separator between digits 2 and 0. So the next group is for digit 0. But since digit 0 has zero 1's, the group would be zero 1's followed by a 0 (since there's another digit after). So the next group is the 0 separator (between 0 and 3). Then, the group for 3 is 111 followed by a 0 (since there's another digit after). Then the group for 1 is 1 with no 0.

So the encoded string is built as:

Group for 2: '11' + '0' → '110'

Group for 0: '' (zero 1's) + '0' (since next digit is 3) → '0'

Group for 3: '111' + '0' → '1110'

Group for 1: '1' → '1'

Combined: '110' + '0' + '1110' + '1' → '110011101', which is the sample input.

So, to split the string into these groups, each group is a run of 1's followed by a 0 (if not the last group), or a run of 1's (if the last group).

But the problem is that the 0's in the string can be part of the separators, but the 0's are part of the group of the previous digit.

So, the approach would be:

- Split the encoded string into groups where each group (except the last) is a run of 1's followed by a 0. The last group is a run of 1's.

But how to split the string into these groups.

An alternative approach is to traverse the string and collect these groups:

Initialize a list to hold the digits.

Start at the beginning of the string.

While there are characters left:

   Read all consecutive '1's until a '0' is found or the end of the string.

   The count of '1's is the current digit.

   Add this digit to the list.

   Then, if there is a '0' after the '1's, skip over it (as it's the separator).

   If there's no '0', then it's the last digit.

So, in code:

Initialize i=0.

digits = []

n is the length of the string.

s is the string.

while i < n:

   count_ones = 0

   while i < n and s[i] == '1':

       count_ones +=1

       i +=1

   digits.append( count_ones )

   # Now, skip over the separator (0), if any.

   if i < n and s[i] == '0':

       i +=1

So, for example, the first sample input '111':

i starts at 0.

Read three '1's, count_ones=3 → digits becomes [3].

Then, since i is now 3, which is equal to n (n=3), exit loop.

Digits is [3], output 3.

For the second sample input '110011101':

i starts at 0.

Read '11' → count_ones=2 → digits [2].

i is now 2, s[2] is '0', so skip over → i becomes 3.

Next, at i=3: s[3] is '0', but the code first looks for '1's. Since there are no '1's here, count_ones is 0 → digits becomes [2,0]. Then, check if current character is '0' → yes, so i becomes 4.

At i=4: read '111' (indices 4,5,6) → count_ones=3 → digits [2,0,3]. Then, i=7, s[7] is '0' → skip to 8.

At i=8: read '1' → count_ones=1 → digits [2,0,3,1]. Then, i=9, which is n=9 → exit.

So digits are [2,0,3,1], which is 2031. Correct.

Another example: the encoded string for 20 would be '1100'.

Processing:

i=0: read '11' → count=2 → digits [2]. Then, skip '0' (i becomes 3). Now i=3, which is '0' → read '1's: none. So count=0 → digits [2,0]. Then, check if current character is '0' → but i=3 is '0', but after that, i becomes 4 (n=4). So digits are [2,0], which is 20. Correct.

So this approach correctly handles leading zeros in the digits (like the 0 in 2031) and trailing zeros (like 20).

So the algorithm is:

- Split the string into groups of '1's, each followed by a '0' (except the last group).

Each group's '1's count is the digit. So even if a group has zero '1's (like the second group in '1100' which is 0 '1's → digit 0), that's valid.

But wait, according to the problem statement, the original number is positive. So the first digit cannot be zero. The code will automatically handle this because the problem says the input is always a valid encoding of a positive number. So we don't have to worry about leading zeros in the digits list.

So the steps to solve the problem are:

1. Split the encoded string into groups of '1's followed by a '0' (for all groups except the last).

2. For each group, the number of '1's is the digit. The last group's '1's count is the last digit.

3. Concatenate all the digits into a string and output it.

So the code can be written as follows:

Read the input: n and s.

Initialize i = 0.

digits = empty list.

Loop:

   while i < len(s) and s[i] is '1', count how many '1's → count_ones.

   append count_ones to digits.

   if current i is within s and s[i] is '0', then i +=1 (skip the separator).

   else, break (since it's the last group).

Then, after processing all, check that digits is not empty (since the problem says the number is positive). Then, output the digits as a concatenated string.

But wait, the code should handle cases where a group has zero '1's. For example, in the case where a digit is zero, the group is zero '1's followed by a '0' (if not last digit), or zero '1's (if last digit). But how does the code capture that?

In the code above, when processing a group, after moving past the previous separator (if any), the code reads the '1's. So for a group with zero '1's (like the second group in the example '1100'), the code would read zero '1's, append 0 to digits, then check if current character is '0' (which it is), then skip it.

So in the case of '1100' (the encoded string for 20):

i starts at 0. Read two '1's → append 2. Then, i is 2, which is '0' → skip to 3.

i is 3, which is '0'. Now, the code tries to read '1's. But s[3] is '0' → count_ones is 0. Append 0 to digits. Then check if i < len(s) (3 <4 → yes). s[3] is '0', so i becomes 4. Now i >= len(s) (4 ==4), loop ends.

Digits are [2,0] → output 20. Correct.

Another example: '0' as a group. Wait, but according to the problem statement, the input string starts with '1'. So there are no leading 0's. But the code must handle the case where a group has zero '1's (digit 0) in between.

But how can a group have zero '1's? For example, the digit 0 is represented by zero '1's, followed by a separator if not last. So, for the encoded string '0', that's not possible, since the string starts with '0', which would be invalid (since the problem says the input starts with '1'). So the code can handle groups with zero '1's as long as they are in the middle.

So the code logic works.

Now, code implementation.

In Python:

Read n, then s.

i = 0

digits = []

while i < len(s):

   count = 0

   while i < len(s) and s[i] == '1':

       count +=1

       i +=1

   digits.append(str(count))

   # Now, check if there's a '0' to skip

   if i < len(s) and s[i] == '0':

       i +=1

   else:

       # no more separators, last digit

       pass

# Now, join the digits and output.

print(''.join(digits))

Wait, but in the case where after reading the '1's, the next character is not '0', it's the end of the string. So that's the last digit.

Testing the sample input:

Sample 1:

3

111

Processing:

i starts at 0.

Read 3 '1's → count=3. digits is ['3'].

i is now 3 (len(s)=3). So loop ends.

Output '3' → correct.

Sample 2:

9

110011101 → s is '110011101'.

i=0:

Read '1's at 0 and 1 → count=2. digits ['2']. Then check s[2] is '0' → i becomes 3.

i=3:

Check s[3] is '0' (current character). Then, code reads '1's → none (count=0). digits becomes ['2','0'].

Then check s[3] is '0', so i becomes4.

i=4: read '1's at 4,5,6 → count=3 → digits ['2','0','3']. i becomes7.

Check s[7] is '0' → i becomes8.

i=8: read '1' → count=1 → digits ['2','0','3','1'].

i becomes9 → loop ends.

Output '2031' → correct.

Another test case: '1100' → digits [2,0]. Output 20.

Another case: '0' → but input can't have this as the string starts with 0. So code is safe.

What about a string that ends with 0? For example, '1110' → which represents 3 followed by a separator. But according to the code, after reading '111', count is 3 → digits ['3']. Then check s[3] is '0', i becomes4. Now, i is4 which is beyond len(s)=4. So loop ends. So digits is ['3'], output '3' → correct.

But what if the original number ends with 0? Like 30. Then the encoding would be '1110' (for 3) followed by a separator '0' (since after 3 comes 0). Then the 0's part is zero '1's → followed by no separator. So the encoded string is '11100' → digits would be read as:

i=0: read 3 '1's → count=3. i becomes3. Check s[3] is '0' → i=4.

i=4: read s[4] is '0' → no '1's, count=0. digits becomes [3,0]. Then check s[4] is '0' → i=5 (length is5). So output '30'.

Which is correct.

So the code correctly handles digits that are zero and the last digit.

So the code should work correctly for all cases.

Now, edge cases.

Case 1: digits with zero in the middle.

Input: '10' → digits [1,0]. Output '10'.

Case 2: leading zero? Not possible since input starts with '1'.

Case3: a single zero digit → encoded as '0'? But input must start with '1'. So no.

Another case: the digit 9 is encoded as '111111111' (nine '1's) → code reads 9, outputs '9'.

So code handles all possible digits.

Therefore, the code is correct.
</think>

```python
n = int(input())
s = input().strip()
i = 0
digits = []
while i < len(s):
    cnt = 0
    while i < len(s) and s[i] == '1':
        cnt += 1
        i += 1
    digits.append(str(cnt))
    if i < len(s) and s[i] == '0':
        i += 1
print(''.join(digits))
```