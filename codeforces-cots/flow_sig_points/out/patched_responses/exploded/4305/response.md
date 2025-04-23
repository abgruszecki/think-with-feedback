<think>
Okay, let's see. The problem is to find the minimal sum of numbers after replacing letters with digits. Each unique letter must correspond to a unique digit, and no number can have leading zero. So, how do I approach this?

First, I need to model the problem. Each character in the strings represents a digit, but the same character must map to the same digit. The challenge is to assign digits to letters such that the sum of all the numbers is minimized, considering the constraints.

Hmm. The key here is to determine which letters contribute the most to the total sum when assigned a higher digit. So, for each letter, the weight is determined by the positions it appears in across all numbers. For example, a letter that appears in the highest place (like the first character of a long number) has a higher weight.

Wait right. So, the idea is to calculate for each character the total contribution it would have based on its position. For example, if a character 'a' appears in the 1000's place in one number and the 10's place in another, the total weight is 1000 + 10 = 1010. Then, assign the highest digits (9,8,7...) to the letters with the lowest weights, and the lower digits (0,1,2...) to letters with higher weights. But wait, except for the letters that are the first character of any number. Those letters can't be assigned 0, because leading zeros are not allowed.

So, the steps should be:

1. For each character, compute its total weight (sum of 10^position for each occurrence in all numbers). The position is determined by the place in the string. For example, in the string "abc", 'a' is in position 2 (if we start from 0 as the least significant digit?), no wait. Wait, the leftmost digit is the highest place. So for the string "abc", which has length 3, 'a' is in the 100's place (10^2), 'b' in 10^1, 'c' in 10^0.

So, for each character in each string, the contribution to the weight is 10 raised to (length of string - position -1). For example, the first character of a 3-digit number contributes 100 (10^2), the next 10^1, and the last 10^0.

2. We need to collect all the characters and their total weights. Then, sort them in descending order of weight.

3. However, some characters cannot be zero. Specifically, any character that is the first character of any of the input strings. These letters must be assigned digits from 1-9. The rest can be 0-9, but each must be unique.

So, the plan is:

- Calculate for each character its total weight and whether it is a leading character (appears as the first character in any of the strings).

- Assign digits in a way that the highest weight characters get the smallest possible digits, but ensuring that leading characters are not zero.

Wait, but since the sum is minimized, higher weight characters should get smaller digits. Because each weight is multiplied by their assigned digit. So to minimize the total sum, for higher weight characters, we should assign the smallest possible digits, as long as constraints are satisfied.

Yes. So the approach is:

Sort all the characters in descending order of their total weight. Then assign digits starting from 0, but:

- The first character in this sorted list (highest weight) should get the smallest possible digit (0), but only if it's not a leading character. If it is a leading character, then it cannot be 0, so we have to choose the next available digit.

But wait, there's a catch here. Because some of the leading characters may have higher weights than others. So we need to first assign digits to all non-leading characters, then assign the leading ones, making sure they get digits from 1 to 9.

Alternatively, here's the correct approach:

- The characters are sorted by their weight in descending order.

- Assign digits in the order of the sorted list, but:

   - The first non-leading character in the sorted list can be assigned 0. Then, leading characters must be assigned the next available digits starting from 1.

But the problem is that some leading characters may have lower weights than non-leading characters. So for example, if a non-leading character has higher weight than a leading character, assigning 0 to the non-leading will help minimize the sum. But the leading character must be assigned a non-zero digit.

So the steps would be:

1. For each character, compute the total weight and track whether it is a leading character (i.e., appears as the first character in any string).

2. Sort all characters in descending order of their weight.

3. Assign digits starting from 0, but for leading characters, the digit must be at least 1. However, we need to select which characters get 0 to minimize the sum.

Wait, but how?

We need to select which non-leading character (if any) gets the 0, as that would allow the leading characters to take lower digits. Because the 0 can't be assigned to a leading character. So here's the plan:

- Among all characters, there are some that cannot be zero (the leading ones). The rest can be zero.

- We need to choose which of the non-leading characters (if any) will be assigned zero to minimize the total sum. But since higher weight characters contribute more, we want to assign the smallest possible digits to the highest weight characters. Except that one of the non-leading characters can be assigned zero, which is the smallest possible.

So here's the correct approach:

- Collect all characters, their total weight, and whether they are leading.

- Separate the characters into leading and non-leading.

- Sort all characters (leading and non-leading) in descending order of weight.

- Now, the first (highest weight) non-leading character in the sorted list can be assigned zero. But if all are leading, then that's impossible. But the problem statement says that a valid assignment exists.

Wait, but how to handle this.

Let me think. All the leading characters can't be zero. So, in the sorted list, among all the non-leading characters, the one with the highest weight should be assigned zero, because that gives the maximum possible saving (since their weight is highest, so multiplying by zero gives zero contribution).

But how to arrange this.

So, the process is:

Sort all characters in descending order of their weight. Then, assign digits in order. The first non-leading character in the sorted list gets 0, and the rest get digits in order, skipping 0 if necessary.

Wait, but the digits have to be unique. So, perhaps:

The idea is to assign digits starting from 0, but skip 0 for leading characters.

But how to decide which non-leading character gets 0.

Wait, here's an alternative approach:

We can compute for each character their weight. Then, sort all characters in descending order of weight. Then, among all the non-leading characters, pick the one with the highest weight (if any) and assign it 0. Then, assign digits 1-9 to the remaining characters in order of their weights.

Because that way, the highest weight non-leading character (which contributes the most to the sum) is assigned zero, which would give the maximum possible reduction in sum. The leading characters are assigned the smallest possible digits (starting from 1 upwards), and the other non-leading characters are assigned the next digits (since the highest non-leading is already 0).

Wait, but in the sorted list, the non-leading characters might not be the first in the list. For example, leading characters could have higher weights than non-leading ones.

So, here's the detailed algorithm:

1. Compute for each character the total weight and whether it is a leading character.

2. Collect all characters into a list.

3. Sort the list in descending order of weight.

4. Find the first (i.e., highest weight) non-leading character in the sorted list. Let's call this character X.

5. Assign 0 to X.

6. Assign the remaining digits (1-9) to the other characters in the sorted order, skipping X. But leading characters must be assigned digits >=1.

Wait, but how to handle this. Once X is assigned 0, the other characters are assigned digits in the order of their sorted list, but:

- For leading characters: the earliest (highest weight) leading characters get the next smallest available digits (starting from 1).

- For non-leading characters (other than X), they get the next available digits.

So the steps would be:

- After sorting all characters in descending order of weight, we need to:

   a. Find the first non-leading character in the sorted list. That's the one that can be assigned 0. But if there are no non-leading characters, which can't be the case because the problem says a valid assignment exists.

   b. Assign 0 to that character.

   c. Assign the digits 1, 2, 3, etc., to the rest of the characters in the sorted list, except for the one that was assigned 0. Leading characters must not be assigned 0, but since we've already handled that in step a, the remaining leading characters will be assigned digits starting from 1.

Wait, but the sorted list includes all characters. So, after X is chosen (the first non-leading in the sorted list), the rest are processed in order. So the digits are assigned in the order of the sorted list, except that X is given 0, and the others are assigned digits in order starting from 1, but skipping X.

Wait, perhaps the correct way is:

The sorted list is in order of highest weight to lowest. We need to assign digits as follows:

- The first non-leading character in the sorted list is assigned 0.

- Then, we assign digits starting from 1 to the remaining characters in the sorted list, excluding the X (the one assigned 0). But since the sorted list is in order of weight, we need to process them in order.

So the algorithm steps:

1. Compute weight and leading status for each character.

2. Sort all characters in descending order of weight.

3. Find the first non-leading character in the sorted list. Let's call its index 'zero_pos'.

4. Assign 0 to that character.

5. Assign the digits 1-9 to the other characters in the order of the sorted list, skipping the 'zero_pos' character.

Wait, but how to arrange this. For example, the sorted list is [A, B, X, C, D], where X is the first non-leading character. Then:

X is assigned 0.

Then, assign 1 to A, 2 to B, 3 to C, 4 to D.

But A, B, etc. could be leading characters. So their digits must be >=1, which they are in this case.

So this approach works.

Let me take the first example:

Sample Input 1:

3

ab

de

aj

The characters are a, b, d, e, j.

Leading characters: a, d, a (but a is the first in ab and aj). So leading characters are a, d.

Non-leading characters: b, e, j.

Compute weights:

For each number:

ab: length 2. a is in position 0 (10^1), b in position 1 (10^0). So a's weight += 10, b += 1.

de: d += 10, e += 1.

aj: a += 10, j += 1.

So total weights:

a: 10 + 10 = 20.

d: 10.

j: 1.

b: 1.

e: 1.

So the sorted list is a (20), d (10), j (1), b (1), e (1). Then, in the sorted list, the first non-leading character is j? Wait, j is not a leading character. Wait, leading characters are a and d.

So in the sorted list:

a (20, leading) → yes.

d (10, leading) → yes.

j (1, non-leading).

b (1, non-leading).

e (1, non-leading).

So the first non-leading in the sorted list is j. But j's weight is 1. Then, assign 0 to j. Then assign digits as follows:

a → 1 (since digits are assigned in order after skipping j). d → 2, j → 0, then the next digits are 3,4, etc. But wait, the sorted list is a, d, j, b, e. So after j is assigned 0, the remaining characters in order (excluding j) are a, d, b, e. So their digits are assigned 1,2,3,4, etc.

Wait, but in this case, the digits would be:

a → 1.

d → 2.

j → 0.

b → 3.

e →4.

But in the sample explanation, a is assigned 1, b is 0, d is 2, e is 3, j is 4. Hmm. That gives a sum of 10 (a=1, b=0) → 10, de → 23 (d=2, e=3), aj → 14 (a=1, j=4). Sum 10+23+14=47.

But according to our algorithm:

In the sample input, j is the first non-leading in the sorted list. So assign 0 to j. Then a gets 1, d gets 2, b gets 3, e gets4.

So the numbers would be:

ab → a=1, b=3 → 13.

de → d=2, e=4 →24.

aj → a=1, j=0 →10. Sum is 13+24+10=47. Which matches the sample. So why is the sample solution different? Because there are multiple possibilities. Because in the sample solution, the non-leading characters are b and j and e. Wait, in the sample explanation, 'b' is assigned 0. So how does that fit into our algorithm.

Ah, in the sample explanation, 'b' is assigned 0, which is a non-leading character. So according to our algorithm, in the sorted list, which is a(20), d(10), j(1), b(1), e(1), the first non-leading character is j. Wait, no. Wait j is part of the first non-leading characters in the sorted list? Because in the sorted list, after a and d (leading), the next is j (non-leading), then b (non-leading), then e (non-leading). So the first non-leading in the sorted list is j. So according to our algorithm, j would be assigned 0. But in the sample explanation, j is assigned 4, and b is assigned 0. So this contradicts.

Wait, this suggests that my approach is incorrect. So what's wrong here?

Hmm. Let's think again. The sample solution assigns 0 to b. So why is that the case?

Because, perhaps, the algorithm needs to pick the non-leading character with the highest weight. But in this case, j's weight is 1, same as b and e. So perhaps when multiple non-leading characters have the same weight, the algorithm can choose any. But how to handle that.

Wait, in the first example:

The characters are a (20, leading), d (10, leading), j (1, non-leading), b (1, non-leading), e (1, non-leading). So sorted by weight in descending order:

a →20, d→10, j→1, b→1, e→1.

Now, the first non-leading character in the sorted list is j (since a and d are leading). But according to the sample solution, the non-leading character chosen is b. How does that happen?

Wait, maybe the algorithm is not just to pick the first non-leading in the sorted list, but to find the non-leading character with the highest weight. But in this case, j has the same weight as b and e. So the order in the sorted list depends on how they are sorted when their weights are equal. If in such a case, the order is arbitrary, then the algorithm might choose any of them. But in the sample, choosing b gives a better result.

Ah, so the problem is that when multiple non-leading characters have the same weight, the algorithm may need to choose the one which allows the leading characters to have lower digits, thereby reducing the overall sum.

Wait, but how?

In the first example, if the algorithm picks j as the non-leading to assign 0, then a gets 1, d gets 2, j gets 0, and then the next digits are 3 (b) and 4 (e). So the sum is:

ab → 13.

de → 24.

aj →10.

Sum is 47, which matches the sample.

But in the sample solution, j is 4. How is that possible? Because in that case, the algorithm must have assigned 0 to b. So the sum would be 10 (a=1, b=0) + 23 (d=2, e=3) + 14 (a=1, j=4) → sum 47. Same total.

So in this case, which non-leading character is chosen to be assigned 0 doesn't affect the sum, as long as the weight is the same. Because even though j is chosen first in the sorted list, but if the code processes the non-leading characters in a different order, the sum could be the same.

Wait, but in this case, when the weights are the same, the order in the sorted list determines which non-leading is chosen. So how are the characters sorted when their weights are equal? Since the problem statement doesn't specify, the code can process them in any order. But for the code to pass all test cases, we need to make sure that when multiple non-leading characters have the same highest weight, we pick the one that allows the minimal sum.

But how?

Wait, perhaps the code should pick the earliest non-leading character in the sorted list. But the sorted list is ordered by weight, and for characters with the same weight, their order is arbitrary. So, in the first example, j is the first non-leading character in the sorted list. But if the code's sorting puts j after b and e, then the first non-leading would be b.

Ah, the problem is how the code sorts the characters when their weights are equal. If two characters have the same weight, their order in the sorted list depends on the tie-breaker. For example, in Python, the sorted function is stable. So if two characters have the same weight, their order depends on their insertion order. But in this problem, the input order may not be the same as the sorted order.

So how can this be handled?

The answer is that in cases where multiple non-leading characters have the same maximum weight, the code must choose the one that allows the use of 0 for the highest possible weight. Since all these characters have the same weight, assigning 0 to any of them would have the same impact on the sum. However, the leading characters are assigned higher digits (like 1, 2, etc.), so to minimize the sum, it's better to assign 0 to one of the non-leading characters with the same highest weight, thus allowing the leading characters to be assigned the smallest possible digits (like 1, 2, etc.).

But how to choose which non-leading character to assign 0 when there are multiple with the same weight. The answer is that it doesn't matter. Because their weights are the same, so the total contribution would be 0 multiplied by the same weight. So regardless of which is chosen, the sum remains the same.

Therefore, the code should assign 0 to the first non-leading character in the sorted list. But how the sorted list is ordered when weights are equal?

In Python, when you sort a list of characters, for example, the default sort is lexicographical. But in our problem, the code can sort the characters in any order when their weights are equal. However, the code must handle this correctly. For example, in the first example, the code must assign 0 to a non-leading character. But which one?

But according to the sample input, the code's assignment must produce the minimal sum. So in the first example, the code's approach would work regardless of the order of the non-leading characters with equal weight. Because the sum would be the same.

Wait, let's calculate:

Case 1: assign 0 to j.

Digits:

a:1, d:2, j:0.

b:3, e:4.

Sum:

ab →13.

de →24.

aj →10.

Total 47.

Case 2: assign 0 to b.

Digits:

a:1, d:2, b:0.

j:3, e:4.

Sum:

ab →10.

de →24.

aj →13.

Total 10+24+13=47.

Same result.

Case 3: assign 0 to e.

Digits: a:1, d:2, e:0.

b:3, j:4.

Sum:

ab →13.

de →20.

aj →14.

Total 13+20+14=47.

Same sum.

So regardless of which non-leading character is assigned 0 (among those with same weight), the total sum remains the same. Therefore, the code can choose any of them and the sum will be correct.

Thus, the approach is correct.

Now, the steps to code this:

1. Read n.

2. Read n strings. For each string, note the first character (leading character).

3. For each character in each string, compute its weight contribution (10^(len(s)-i-1) where i is the position in the string, 0-based from left to right). Sum these contributions per character.

4. Track for each character whether it is a leading character (appears as the first character in any string).

5. Create a list of tuples (weight, char, is_leading). But perhaps, track per character their total weight and leading status.

6. Sort the list of characters in descending order of weight. For characters with the same weight, the order between them can be arbitrary.

7. Find the first non-leading character in the sorted list (since we need to assign 0 to the highest possible non-leading character to minimize the sum). Once found, assign 0 to that character.

8. Assign digits to the remaining characters in the sorted list (excluding the one assigned 0) in order, starting from 1. Leading characters must be assigned digits >=1, but since we're starting from 1, this is handled.

Wait, in the sorted list, after the first non-leading character (assigned 0), the rest of the characters are assigned digits in the order they appear in the sorted list (excluding the 0-assigned). So leading characters can be assigned digits 1, 2, etc., as they are processed in the order of the sorted list.

So code steps:

- Collect all characters, their total weight, and leading status.

- Sort the characters in descending order of weight.

- Iterate through the sorted list to find the first non-leading character (since leading can't be 0). Once found, note its index.

- Assign 0 to that character.

- Then, assign digits starting from 1 to the remaining characters in the sorted list (excluding the 0-assigned one), in the order of the sorted list. For example, for the sorted list, we create a list of characters in order. Then, we create a list of digits where the zero-assigned character is placed first, but then skipped in the digit assignment. Wait, perhaps the code can split the sorted list into two parts: the characters before the zero-assigned one (all leading?), then the zero-assigned, then the rest. Then, assign digits 1, 2, etc., to the characters in the sorted list, except for the zero-assigned, which gets 0.

Wait, perhaps the code can loop through the sorted list, and for each character, if it is the zero-assigned, skip it. Otherwise, assign digits starting from 1.

But how to manage the order.

Alternatively, after selecting the zero-assigned character, collect the remaining characters (in the sorted list, excluding the zero-assigned) in the same order. Then, assign digits to them in order, starting from 1.

But how to handle the order correctly.

Another approach:

The code will create a list of all characters sorted by weight (descending).

Then, find the first character in this list that is not a leading character.

Once found, that character is assigned 0.

The rest are assigned digits 1, 2, ... in the order of the sorted list, but skipping the zero-assigned character.

So, for example, if the sorted list is [A, B, C, D], and C is the first non-leading, then assign:

A:1, B:2, C:0, D:3.

Wait, no. Because after assigning C to 0, the rest are assigned in order. So the order is A, B, D. So they get 1, 2, 3.

But in the sorted list, the order is A, B, C, D. So the code would assign:

A →1.

B →2.

C →0.

D →3.

So the sum is (A's weight *1) + (B's weight *2) + (C's weight *0) + (D's weight *3).

Yes. So this approach works.

So code steps:

- Collect all characters, their total weight, leading status.

- Sort in descending order of weight. If weights are equal, the order doesn't matter.

- Iterate through the sorted list to find the first character that is not a leading character. Once found, note its index.

- Assign 0 to that character.

- For the remaining characters in the sorted list (excluding the zero-assigned one), assign digits in the order they appear, starting from 1.

Wait, but the remaining characters include all characters except the zero-assigned. So the code can create a list of the sorted characters, remove the zero-assigned character, then assign digits in order.

Wait, no. Because in the sorted list, the zero-assigned character is in position k. So the order is:

sorted_list = [c0, c1, ..., ck, ...]

After removing ck, the order for the remaining is c0, c1, ..., ck-1, ck+1, ... So the code needs to loop through the sorted list, and for each character, if it's not the zero-assigned, assign digits in order, starting from 1.

Wait, perhaps the code can create a list of all characters in the sorted order, and then create a list of digits. The digits are assigned as follows:

digit = 0 for the first non-leading character.

Then, for all characters in the sorted list (excluding the zero-assigned one), assign digits 1, 2, 3, etc., in order.

So, in code:

sorted_chars = sorted list.

zero_char = None

for i, char in enumerate(sorted_chars):

    if not char.is_leading:

        zero_char = char

        break

Then, create a mapping:

digits = {}

digits[zero_char] = 0

current_digit = 1

for char in sorted_chars:

    if char == zero_char:

        continue

    digits[char] = current_digit

    current_digit +=1

Then, compute the sum.

But wait, in this case, the code is looping through the sorted_chars in order, skipping the zero_char, and assigning digits in order. So the code is correct.

Now, the code needs to collect all the characters, their weights, and leading status.

Implementing this in Python:

First, collect the weights and leading status:

We can use a dictionary to track for each character its total weight. Another set to track leading characters.

For example:

from collections import defaultdict

weight = defaultdict(int)

leading = set()

n = int(input())

for _ in range(n):

    s = input().strip()

    # Add first character to leading set

    if len(s) > 0:

        leading.add(s[0])

    # Compute the weight for each character in s

    l = len(s)

    for i, c in enumerate(s):

        pos = l - i -1  # e.g., for "abc", index 0 is 'a' → position 2 (10^2), index 1 is 'b' → 1, etc.

        contribution = 10 ** pos

        weight[c] += contribution

Once all characters are processed, create a list of tuples for each character, sorted by weight.

Then, sort them in descending order. For the characters with same weight, the order can be arbitrary. So, in Python, the sorted function can be used with a key that is (-weight, c), so that higher weight comes first, and for same weights, the character's ASCII value is used (but this doesn't affect the sum).

sorted_chars = sorted(weight.keys(), key=lambda x: (-weight[x], x))

Then, find the first non-leading character in sorted_chars:

zero_char = None

for c in sorted_chars:

    if c not in leading:

        zero_char = c

        break

But wait, leading is a set of characters that are leading. So 'c not in leading' means it's a non-leading character.

Once zero_char is found, assign 0 to it.

Then, assign the rest digits in order, starting from 1.

digit_map = {}

digit_map[zero_char] = 0

current = 1

for c in sorted_chars:

    if c == zero_char:

        continue

    digit_map[c] = current

    current +=1

Now, compute the sum:

sum_total =0

for c in weight:

    sum_total += weight[c] * digit_map[c]

But wait, how to process all the numbers. Wait, the sum is the sum of all the numbers, each of which is the digits assigned to the characters in their order. But each number's value is the sum of (digit of c) * 10^pos for each position. But the code's approach of summing the weight of each character multiplied by their assigned digit is equivalent. Because the sum of all numbers is equal to the sum for each character c: (assigned digit) multiplied by the sum of 10^pos for each occurrence in the numbers. Which is exactly the weight. So the code can directly multiply the digit_map[c] by the weight[c] for each character and sum all.

Yes. Because each occurrence of character c contributes digit_map[c] * (10^pos) to the sum. Summing over all characters and all their occurrences is the same as sum (digit_map[c] * sum(10^pos) for each occurrence) → which is sum (digit_map[c] * weight[c]).

So this approach works.

Now, handling the leading characters.

But what if all characters are leading? The problem statement says that a valid assignment exists, so there must be at least one non-leading character. Because leading characters can't be assigned 0, but the code must assign 0 to a non-leading character.

Wait, but the problem statement says that the restored numbers must be positive and without leading zeros. So the first character of each number must be non-zero. So in the input, the first character of each string is a leading character, and thus can't be zero. But the code checks if any character is leading (i.e., appears as first character in any string). So the leading set contains all characters that are first characters of any input string.

Thus, the code will find a non-leading character in the sorted list. Because the problem says that a valid assignment exists. So the code can safely proceed.

Now, let's test the first sample:

Sample Input 1:

3

ab

de

aj

Leading characters are a, d.

sorted_chars: sorted by descending weight.

a (weight 20), d (10), j (1), b (1), e (1). The order of j, b, e may vary, but sorted by -weight and then by the character.

But in Python, when sorted with key (-weight, x), the characters are ordered first by weight descending, then by the character. So for the three characters with weight 1 (j, b, e), their order depends on their ASCII values. 'b' comes before 'e', which comes before 'j'.

Wait, 'b' is ASCII 98, 'e' 101, 'j' 106. So sorted list would be:

a (20), d(10), b (1), e (1), j (1).

In this case, the first non-leading is b (since a and d are leading, next is b which is not leading). So zero_char is b. Assign 0 to b. Then the digits are a:1, d:2, e:3, j:4. Then sum:

a:20*1 =20.

d:10*2=20.

b:1*0=0.

e:1*3=3.

j:1*4=4.

Total sum: 20+20+0+3+4=47. Which matches the sample.

So code would work.

Another example: Sample Input 3:

3

aa

jj

aa

The leading characters are a (from first and third string), j (from second string).

Weight for a: in each string "aa", length 2. So each 'a' contributes 10 and 1. For the two "aa" strings: each 'a' has 10+1 per occurrence. But each occurrence of a in the strings contributes to the weight.

Wait, let's compute:

First string "aa": length 2.

First 'a' (position 0) contributes 10^1 =10.

Second 'a' (position 1) contributes 10^0=1.

Third string "aa" is the same: each 'a' contributes 10 and 1.

So for the first and third strings:

each 'a' in first string: 10 +1.

third string: same.

Total a's weight is (10+1) *2 (since two a's per string, two strings → 2*2 a's? No, wait each string has two a's.

First string: two a's → sum 10 +1 =11.

Third string: two a's → sum 10+1=11. So total for a is 11+11=22.

For jj: length 2. Each j contributes 10 and 1. So j's weight is 10+1=11 for each occurrence. Two j's in this string → 11 *2 =22?

No, wait, each occurrence of j in the string contributes to the weight. So jj has two j's: first contributes 10, second contributes 1. So total for jj is 10+1=11. So j's weight is 11.

So sorted list: a (22), j (11), a's from the other strings (but they are the same character). So the sorted list is [a, j].

Wait, the code's sorted_chars list would be sorted by weight descending. So a (22), j (11). Then, in the code, leading characters are a and j. The first non-leading character in the sorted list: but all characters in the list are leading (a is leading because it's the first character of some string, j is leading because it's the first of another string).

Wait, but this sample input has 3 strings:

3

aa → leading is 'a'.

jj → leading is 'j'.

aa → leading is 'a'.

So leading is {'a', 'j'}.

The sorted list is [a (22), j (11)]. So the code will loop through sorted_chars (a and j) looking for a non-leading character. But both are leading. So code can't find a non-leading character, which contradicts the problem statement's guarantee.

But sample input 3's output is 44, which implies that the code can assign digits such that the leading characters are assigned 1 and 2, and some non-leading character (but all characters in the strings are leading).

Wait, this is a problem. Wait, in sample input 3, the strings are "aa", "jj", "aa". So all characters are a's and j's. But a is leading (appears as first character in "aa" and "aa"), j is leading (appears as first character in "jj"). The other characters in the strings are also a's and j's, but they are not the first characters. For example, the second 'a' in "aa" is not a leading character. So the code's leading set is {'a', 'j'}.

So for the code, when processing the characters, the leading set is {'a', 'j'}, but the characters in the code's weight dictionary are a and j.

Wait, no. The code's leading set is a set of all characters that are the first character of any string. For example:

In sample input 3:

Each of the three strings starts with a or j. So leading is {'a', 'j'}.

The code's weight dictionary will have:

For 'a' in the first "aa": first 'a' contributes 10^1 =10, second contributes 1 → total 11.

Third "aa" is same → another 11. So total weight for a is 22.

For 'j' in "jj": first 'j' contributes 10^1=10, second contributes 1 → 11. So total weight for j is 11.

So sorted_chars will be [a, j].

Then, the code will loop through sorted_chars to find the first non-leading character. But a and j are in the leading set. So code cannot find a non-leading character. But the problem statement says that a valid assignment exists. So this is a contradiction.

But sample input 3's output is 44. Let's see.

Sample Input 3:

3

aa

jj

aa

Possible assignment: a=1, j=2. Then:

aa → 11.

jj → 22.

aa →11.

Sum 11+22+11=44.

But according to the code's approach, since a and j are leading, the code would not find a non-leading character. How is that possible?

Wait, there's a mistake here. Because the code's leading set is the first character of each string. So in the first and third strings, the first character is a. In the second string, the first character is j. So leading set is {'a', 'j'}, as per the code.

But in the code's sorted list, a and j are the only characters. So the code would iterate through the sorted list (a, j) and look for a non-leading character. But both are in leading set. So the code would not find any, which is impossible because the problem says a valid assignment exists.

Ah! This is a problem. So what's wrong here?

Ah, because in the code, the leading set is all characters that are first in any string. So in the third sample input, 'a' and 'j' are in the leading set. However, the code's sorted list contains 'a' and 'j' (since those are the only characters in the input). So, the code's for loop will not find any non-leading character. But the problem says a valid assignment exists.

So what's the mistake here?

Ah! Oh wait, in the third sample input, the code's leading set is {'a', 'j'}, which are both leading. But the code's approach requires that a non-leading character exists. But in this case, there are no non-leading characters. Because all characters in the input are either 'a' or 'j', which are leading characters.

But this is impossible, because in the third sample input, the code's code would fail to find a non-leading character, but the problem says a valid assignment exists.

This suggests that there's a mistake in the code's approach.

Wait, but the third sample input's output is 44. Let's think about it.

In the third sample input, all characters in the strings are 'a' and 'j', but in some positions other than first. For example, the second 'a' in the first "aa" is not a leading character, but it is the same 'a' as the first character. So the code's leading set includes 'a' because it is the first character of some string. But the second 'a' in "aa" is not a leading character. So the code's leading set is {'a', 'j'}, but 'a' can appear in non-leading positions. So the code's leading set is correct.

But in the code's approach, the characters in the weight dictionary are 'a' and 'j'. But they are both leading (since they are in the leading set). So the code would not find any non-leading character, but that's a contradiction. Because 'a' appears in non-leading positions. For example, the second 'a' in "aa" is not leading. So in the code's weight dictionary, 'a' has a weight that includes contributions from both leading and non-leading positions. But in terms of the code's leading set, 'a' is considered a leading character (because it appears as the first character of at least one string).

Ah, but the code's leading set is the set of characters that are first in any string. So even if 'a' appears in non-leading positions in other strings, it is marked as a leading character. So in the third sample input, 'a' and 'j' are in the leading set, even though 'a' appears in non-leading positions. So the code's code will loop through the sorted list (a and j) and fail to find any non-leading character, leading to an error.

But the sample input 3's correct solution requires that 'a' is assigned 1 and 'j' is assigned 2, which are both allowed. But in this case, the code's code would not find any non-leading character, and thus the code would crash.

So this indicates a flaw in the code's approach.

What's the mistake here?

The mistake is that in the code's approach, the code looks for the first non-leading character in the sorted list of characters (those that appear in the input). But in the third sample input, all characters in the input (a and j) are leading characters (because they are first characters of some string). However, in this case, all occurrences of a and j in non-leading positions (like the second 'a' in "aa") are still considered leading characters because they are part of the leading set. But this is incorrect. Because a character can be a leading character (appears as the first character of some string), but can also appear in non-leading positions. However, the code's approach marks all such characters as leading. Thus, the code's code would think that there are no non-leading characters, which is not the case.

Wait no. The code's leading set is the set of characters that are the first character of any string. So if a character is the first character of any string, it is marked as leading. But this doesn't prevent that character from appearing in other positions in other strings. However, the code's code is trying to find a character that is not in the leading set (i.e., not the first character of any string). But in the third sample input, the only characters are a and j, which are in the leading set. So there are no characters in the input that are not in the leading set. But this can't be possible, because the sample input 3's correct assignment uses a and j. How does that work?

Wait, the problem statement says that the restored numbers must not have leading zeros. But in the third sample input, all strings start with a or j. So in the code's approach, any character that is the first character of any string is considered leading. So a and j are leading. But in the third sample input, there are no other characters. So according to the code's approach, there are no non-leading characters. But this contradicts the problem's guarantee that a valid assignment exists.

But according to the sample input 3's explanation, the numbers after restoration are [11, 22, 11], sum 44. In this case, a is assigned 1 and j is assigned 2. The leading characters are a and j, but the code's code would not have any non-leading characters to assign 0, which is required.

But how is this possible?

Ah, here's the key. The code's approach is incorrect. Because the code's code is trying to assign 0 to a non-leading character. But in this case, there are no non-leading characters. But the problem's third sample input is possible because the code doesn't need to assign 0 to any character. All digits can be 1, 2, etc., but no 0.

But how can that be possible? Because the code's approach requires that at least one character is assigned 0. But in this case, there are no non-leading characters. So how can a valid assignment exist?

This suggests that the code's approach is wrong, and the correct approach is different.

Wait, but the problem says that the sum must be minimal. So perhaps when all characters are leading, then all digits must be assigned from 1 to 9. But this requires that no character is assigned 0. But how can that be possible when there are more than 9 characters?

But the problem allows this as long as it's guaranteed that a valid assignment exists. But in sample input 3, there are only two characters, a and j. So digits can be assigned 1 and 2, and sum is 1+2=3 per a and j's contribution. But how does this fit with the code's approach.

Ah! The problem is that the code's approach assumes that there must be a non-leading character to assign 0. But this is not necessarily true. For example, if all characters are leading, then the code's approach would fail, but the problem says that a valid assignment exists.

So the code's approach is incorrect. This indicates a flaw in the initial reasoning.

So where is the mistake?

The mistake is that the code's approach requires that there is at least one non-leading character to assign 0. But in cases where all characters are leading, this is impossible. However, the problem statement says that a valid assignment exists for all test cases, but how?

The answer is that the code's approach is incorrect. The correct approach is:

If all characters are leading, then we cannot assign 0 to any character. But that's impossible, since all digits are distinct. However, this is only possible if there are at most 9 characters (since digits 1-9 can be assigned). For example, in sample input 3, there are two characters, a and j. So digits can be 1 and 2. Sum is (1*22) + (2*11) = 22 + 22=44.

But according to the code's approach, we would not find any non-leading character. So the code would crash.

So the code's approach must handle this case. How?

Ah! The code's approach is to assign 0 to a non-leading character. But if all characters are leading, then this is impossible. But the problem says that a valid assignment exists. So in this case, the code must assign digits 1-9 to the leading characters, but that's possible only if the number of leading characters is <=9. But how can there be a valid assignment in this case?

Wait, but the problem says that the original numbers had no leading zeros. So the first character of each string must be mapped to a non-zero digit. But if all characters are leading (i.e., appear as the first character of at least one string), then all of them must be assigned non-zero digits. So in this case, the code cannot assign 0 to any character. Therefore, the code must assign digits 1-9 to the leading characters, but the number of leading characters must be <=9.

But the code's approach is to assign 0 to a non-leading character, but in this case, there are none. So the code's approach must be modified to handle this case.

So what's the correct approach?

The correct approach is:

- The code should assign 0 to a non-leading character (if exists), which allows the leading characters to get lower digits.

- If there are no non-leading characters (all characters are leading), then all digits must be assigned from 1 to 9. But since there are 10 possible digits (0-9), but the leading characters can't be 0. But wait, how many characters can there be? If all characters are leading, the number of characters must be <=9. Because digits 1-9 are available. For example, sample input 3 has two leading characters, which is manageable.

So the code's approach must be adjusted to handle the case where there are no non-leading characters.

So the algorithm should be:

After sorting the characters in descending order of weight:

- Check if there exists a non-leading character. If yes, assign 0 to the highest weight non-leading character, then assign digits 1-9 to the rest in order.

- If there are no non-leading characters, assign digits 1-9 to the characters in order of their sorted weights. (But this can only happen if the number of characters <=9, which is guaranteed by the problem's input constraints.)

So the code needs to handle both cases.

So the steps are:

1. Compute weights and leading status.

2. Sort the characters in descending order of weight.

3. Check if there is any non-leading character.

   a. If yes:

      i. Assign 0 to the first non-leading in the sorted list.

      ii. Assign digits 1-9 to the remaining characters in sorted order.

   b. If no:

      i. Assign digits 1-9 to the characters in sorted order.

Thus, the code needs to check whether there are any non-leading characters.

So in code:

sorted_chars = sorted(weight.keys(), key=lambda x: (-weight[x], x))

has_non_leading = any(c not in leading for c in sorted_chars)

if has_non_leading:

    zero_char = next(c for c in sorted_chars if c not in leading)

    digit_map = {zero_char: 0}

    current = 1

    for c in sorted_chars:

        if c == zero_char:

            continue

        digit_map[c] = current

        current +=1

else:

    # all are leading, assign 1-...

    current = 1

    digit_map = {}

    for c in sorted_chars:

        digit_map[c] = current

        current +=1

This way, in the third sample input, the code enters the else clause. sorted_chars is [a, j]. Assign 1 and 2.

So sum is 22*1 + 11*2 = 22 +22=44.

Which matches the sample.

So the code must include this check.

Ah, this was the missing part in the initial approach. So the code must first check if there are any non-leading characters. If yes, proceed as before. If no, assign digits 1-9 in order.

Thus, the code will now handle all cases.

Now, let's test sample input 3.

Sample input 3:

3

aa

jj

aa

Leading characters: {'a', 'j'}

sorted_chars: [a, j]

has_non_leading = any(c not in leading for c in sorted_chars) → 'a' is in leading, 'j' is in leading. So no. Thus, code enters else clause.

digit_map is:

a:1, j:2.

sum = 22*1 + 11*2 = 22 + 22=44.

Correct.

Another example, sample input 2:

5

abcdef

ghij

bdef

accbd

g

Leading characters: a, g, b, a, g.

Wait, first characters of each string:

- "abcdef" → a.

- "ghij" → g.

- "bdef" → b.

- "accbd" → a.

- "g" → g.

So leading set is {a, g, b}.

The characters in the sorted list would be those with highest weight.

But let's not go into details. The code's approach will handle this.

Thus, the code now handles all cases.

So the final code in Python would be:

Read n.

Read n strings.

For each string, add the first character to leading.

For each character in each string, compute the weight.

Sort characters in descending order of weight, breaking ties by character.

Check if any character is non-leading.

If yes, assign 0 to the first such character.

Else, assign 1-9 to all characters.

Compute the sum.

Now, the code.
</think>

```python
from collections import defaultdict

n = int(input())
weight = defaultdict(int)
leading = set()

for _ in range(n):
    s = input().strip()
    if s:
        leading.add(s[0])
    l = len(s)
    for i, c in enumerate(s):
        contribution = 10 ** (l - i - 1)
        weight[c] += contribution

sorted_chars = sorted(weight.keys(), key=lambda x: (-weight[x], x))
has_non_leading = any(c not in leading for c in sorted_chars)

digit_map = {}
if has_non_leading:
    # Find the first non-leading character in sorted_chars
    zero_char = next(c for c in sorted_chars if c not in leading)
    digit_map[zero_char] = 0
    current = 1
    for c in sorted_chars:
        if c != zero_char:
            digit_map[c] = current
            current += 1
else:
    # All are leading, assign 1 to 9
    current = 1
    for c in sorted_chars:
        digit_map[c] = current
        current += 1

total_sum = 0
for char in weight:
    total_sum += weight[char] * digit_map[char]

print(total_sum)
```