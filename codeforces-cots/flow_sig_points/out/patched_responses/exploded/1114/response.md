<think>
Okay, so I need to solve this problem where I have to find the maximum number possible from a set of digits that's divisible by 2, 3, and 5. Let's think about the constraints here. 

First, since the number has to be divisible by 2 and 5, it must end with 0. So the first thing I need to check is whether there's a 0 in the digits. If there's no 0, then it's impossible, so the answer is -1 right away.

But even if there's a 0, the sum of all digits must be divisible by 3 because the number also needs to be divisible by 3. So the steps I need to follow are:

1. Check if there's at least one 0. If not, return -1.
2. Calculate the sum of all digits.
3. If the sum is divisible by 3, then the largest number is all digits sorted descending, but ensuring that the last digit is 0 (since they need to end with 0). But since the digits are sorted descending, the 0 would already be at the end. So that's the best case.
4. If the sum isn't divisible by 3, then we need to remove some digits to make the sum divisible by 3. But we can't remove the 0, because we need at least one 0 at the end. Wait, but the 0 is part of the digits. So after removing some digits (other than all the 0s?), we need to have at least one 0 left.

So let's break it down.

First, collect all the digits. Then:

- If there are no zeros, return -1.
- Sum all the digits. Let's call this total_sum.
- Check if total_sum is divisible by 3. If yes, then proceed to form the maximum number by sorting the digits in descending order and ensuring that the last digit is 0. But wait, if there are multiple zeros, the rest can be arranged in descending order. However, leading zeros are not allowed, but if the only digit left is 0, then output 0.

Wait, for example, if the input is a single 0, then output is 0. If there are multiple digits including 0, but after removing some digits to make sum divisible by 3, the remaining digits are all zeros, then the output is 0. But in that case, the maximum possible is 0, which is allowed.

So here's the approach:

1. Count the frequency of each digit.
2. Check if there are any zeros. If not, return -1.
3. Compute the total sum of all digits.
4. If the sum is divisible by 3, then the number can be formed by all digits (sorted descending), but must end with 0. So sort the digits in descending order, but ensure that 0 is present. Then, after sorting, the 0(s) will be at the end. However, there must be at least one 0. But since we checked for presence of zero, that's okay.
5. If the sum is not divisible by 3, then we need to find a subset of digits (excluding some) such that the sum of the subset is divisible by 3, and the subset includes at least one 0.

But how to do this optimally?

The idea is to remove the smallest possible number of digits to make the sum divisible by 3. Because we want the maximum possible number, which means we want as many digits as possible, especially higher digits.

So, the possible cases when sum mod 3 is 1:

- Remove one digit with value 1 mod 3 (i.e., 1, 4, 7) such that the sum decreases by 1. Or,
- Remove two digits with value 2 mod 3 (2,5,8) such that sum decreases by 4, which mod 3 is 1 (since 4 mod 3 is 1). 

Similarly, if sum mod 3 is 2:

- Remove one digit with value 2 mod 3 (2,5,8), sum decreases by 2 → mod 3 becomes 0. Or,
- Remove two digits with value 1 mod 3 (1,4,7), sum decreases by 2 (1+1=2 → mod 3 2), which makes sum mod 3 0.

So first, calculate the remainder when the sum is divided by 3. Then, based on that remainder, try to remove digits to get a sum divisible by 3.

But after removing those digits, there must still be at least one 0 left, and the remaining digits (if any) should form the maximum possible number.

So steps after checking for zero presence and sum mod 3:

Case 1: sum mod 3 is 0. Then, the digits can be used as is (sorted descending, with 0 at the end). But if all digits are zero, output 0.

Case 2: sum mod 3 is 1. Then, try to remove one digit of 1 mod 3 (1,4,7), choosing the smallest such digit (to maximize the remaining digits). If no such digits are present, try to remove two digits of 2 mod 3. Then check if after removal, there is at least one 0 and the sum is divisible by 3.

Case 3: sum mod 3 is 2. Similarly, try to remove one digit of 2 mod 3, or two digits of 1 mod 3.

Once the digits are removed (if necessary), then check if there are any digits left (other than zero), but at least one zero. Also, if after removal, there are no digits except zero, then the output is 0.

But also, after removing, the digits left must form the maximum possible number. So when removing digits, we need to choose the smallest possible digits in their mod group to maximize the remaining digits. For example, if we need to remove one digit from mod 1 group, we should remove the smallest digit (so the largest digits remain). Wait, no. Wait, the digits are sorted in descending order. So for example, if the digits are 9,9,9,4,0. The sum is 9*3 +4 +0 = 31. 31 mod3 is 1. So sum mod3 is 1. We need to remove 1 mod3 digit. The digits in mod1 are 4. So remove the 4. Then digits are 9,9,9,0. Sum is 27, which is divisible by 3. So sorted as 9990.

But if we have digits like 7,7,7,1,0. Sum is 7*3 +1 +0 =22. 22 mod3 is 1. So remove the 1. Then digits are 7770. Sum 21. Correct.

Alternatively, if the sum is 10, mod3 is 1. But if there's no 1,4,7 digits, then we need to remove two digits of mod2. For example, digits are 8,5,5,0. Sum is 8+5+5+0=18. 18 mod3 is 0. So that's okay. Wait, maybe another example.

Another example: sum is 4. mod3 is 1. So need to remove one digit of mod1. Suppose the digits are 4,2,2,0. Sum is 4+2+2=8, mod3 is 2. Wait, maybe this example is not the best.

But the key point is, when you have to remove digits, you need to find the minimal number of digits to remove (so as to keep as many as possible) and also the digits removed should be the smallest possible (to leave larger digits in the number).

Wait, no. For example, if there are multiple candidates for removal, you want to remove the ones that are the smallest (so that the larger digits are kept in the number). Because the digits are sorted in descending order, so the earliest digits are the largest. So for example, if you have digits 7,4,1,0. Sum is 12. sum mod3 is 0. So that's okay. But if sum was 13, mod3 is 1. Then, you need to remove one mod1 digit. The digits are sorted as 7,4,1,0. So the mod1 digits are 7 (7 mod3 is 1), 4 (4 mod3 is 1), 1 (mod3 1). So you can choose to remove the smallest of them (the 1) first. Because that way, the remaining digits are larger. So after removing 1, the digits are 7,4,0. Sum 11, which mod3 is 2. Wait, no. Wait, sum was 13, removing 1 gives sum 12, which mod3 is 0. So that's correct. So yes, removing the smallest possible digits in their mod group allows the remaining digits to be as large as possible.

So the approach is:

For the case where sum mod3 is 1:

- Try to find the smallest digit in mod1 group (1,4,7). Remove that digit. If there are multiple, remove the smallest (so that the larger digits remain in the array). Wait, but when the digits are sorted in descending order, the digits in mod1 group would appear in the list in descending order. So for example, in a list sorted as 9,7,4,3,1,0. The mod1 digits here are 7,4,1. The smallest is 1. So in the list, the 1 is the last occurrence of a mod1 digit. So when removing, we want to remove the 1. But how to find that in the list.

Alternatively, perhaps the digits are stored in a sorted list (descending) and we can iterate through them to find the first occurrence of a mod1 digit (if the remainder is 1). Wait, no. Wait, when the digits are sorted in descending order, the digits are from largest to smallest. So when looking for the smallest mod1 digit, which is the rightmost mod1 digit. So in the list [7,4,1], the smallest mod1 digit is 1. So if we have the digits sorted as [7,4,3,2,1,0], the mod1 digits are 7,4,1. So the rightmost mod1 digit is 1. So in this case, we can traverse the digits from the end (right to left) to find the first mod1 digit. Wait, but the digits are sorted in descending order. So the rightmost mod1 digit is the smallest in the group. So by removing the rightmost mod1 digit (the smallest in the group), we can leave the rest of the digits as large as possible.

So the algorithm would be:

For the case when the remainder is 1:

1. Check if there are any digits in mod1. If yes, remove the smallest such digit (the rightmost in the sorted list). Then proceed.
2. If no digits in mod1, check if there are at least two digits in mod2. Remove the two smallest mod2 digits (the two rightmost in the sorted list). If there are not enough mod2 digits, then it's impossible.

Similarly, for remainder 2:

1. Check if there are any digits in mod2. Remove the smallest (rightmost) such digit.
2. Else, check if there are at least two digits in mod1. Remove the two smallest mod1 digits.

But after removing these digits, we need to ensure that there's at least one zero left, and that the remaining digits (if any) can form a valid number (i.e., not leading with zero, except for the case where the only digit left is zero).

But once the digits are processed, after removing the required digits, we need to check:

- At least one zero exists.
- The sum is divisible by 3.
- The digits are arranged in descending order, with all zeros at the end (but the sorted list will naturally have the zeros at the end).

Wait, but after removing the necessary digits, the remaining digits must include at least one zero. Otherwise, even if the sum is divisible by 3, the number can't end with zero.

So after processing the digits (removing the required digits to make sum divisible by 3), we must check that there is at least one zero. Otherwise, the number can't be formed.

So here's the overall plan:

1. Read the input digits, count the frequency of each digit.
2. If there's no zero in the digits, output -1.
3. Calculate the sum of all digits. If sum is zero (all digits are zero), output 0.
4. Else, check sum mod3.
   a. If mod3 is 0: proceed to form the largest number by using all digits except possibly some zeros, but wait, no. We need to use all digits except those that are removed. Wait, no. Wait, in this case, the sum is already divisible by 3, so all digits can be used. But since the number must end with zero, we need to have at least one zero. Which is already checked in step 2. So sort the digits in descending order, and then check if after sorting, the last digit is zero. Which it will be, since we have at least one zero, and the rest are sorted in descending order. So the maximum possible number is formed.
5. If mod3 is not 0, then need to remove some digits as per the rules. After removal, check:
   a. The sum of the remaining digits must be divisible by 3.
   b. The remaining digits must contain at least one zero.
   c. The remaining digits are not empty (since the zero is part of them).
6. Once the digits are processed, arrange them in descending order, ensuring that the last digit is zero. If after processing, all digits are zero, output 0. Else, output the digits in order.

But how to implement this.

Let's think about the steps again.

Implementation steps:

1. Read the input, split into a list of digits (strings, perhaps, but easier to process as integers).
2. Count the frequency of each digit, or more directly, sort the digits in descending order.
3. Check if there's at least one 0. If not, output -1.
4. Compute sum. If sum is 0 (i.e., all digits are zero), output 0.
5. If sum mod3 is 0: then proceed to form the number by using all digits (sorted in descending order) but ensuring that there's at least one zero. Since step 2 already checks for a zero, the digits after sorting will have 0(s) at the end. So the maximum possible is formed. So output the sorted digits, joined into a string. But note that if after sorting, the first digit is zero, then the output is 0. For example, if the digits are [0], output 0. If the digits are [0,0,0], output 0. So need to check if all remaining digits are zero.

Wait, but after processing, after removing digits, even if sum is zero (sum of digits is zero), but that's possible if all digits are zero. But in that case, the output is 0.

So in code:

After collecting the digits (sorted in descending order):

if sum of digits is 0 → output 0.

Else, after processing, if the digits are all zero → output 0.

Else, form the maximum number by joining the digits in sorted order.

So back to the steps.

So, for the case where sum mod3 is 0, we can proceed to form the number. But need to check if there's a zero. Which is already handled.

But let's see. For example, if the digits are [3,0], sum is 3. sum mod3 is 0, but the digits can be arranged as 30. So correct.

Now, for the case where sum mod3 is not zero.

Let's take the sum mod3 as r (r is 1 or 2). Then, we need to find the digits to remove.

The plan is:

- Create a list of digits sorted in descending order.
- For the given remainder r, try to find the digits to remove.

For example, if r is 1:

Option 1: find the smallest digit (rightmost in the sorted list) that is in mod1. Remove it.

Option 2: if there are no such digits, find two digits in mod2. Remove the two smallest (rightmost) in mod2.

Similarly for r=2.

So, how to implement this.

In code, perhaps, iterate through the digits (sorted in descending order) and track the digits that can be removed.

But perhaps a better way is to create a list of digits, and then for the given remainder, generate possible candidates for removal.

For example:

For r=1:

We need to remove digits whose sum mod3 is 1, either by removing one digit of mod1 or two digits of mod2.

We can generate all possible candidates for removal and choose the one that results in the maximum possible number.

But how to find the optimal candidates.

Let me think. For example:

If we need to remove one mod1 digit, we should remove the smallest possible mod1 digit (the rightmost occurrence in the sorted list) to maximize the remaining digits.

Similarly, if we need to remove two mod2 digits, we should remove the two smallest mod2 digits (the two rightmost occurrences in the sorted list).

So in code:

For r=1:

Check if there are any mod1 digits. If yes:

Loop through the digits from the end (i.e., from smallest to largest) and find the first occurrence of a mod1 digit. Remove that digit.

If no mod1 digits found, check if there are at least two mod2 digits. If yes, loop through the digits from the end to find two mod2 digits and remove them. If there are not two mod2 digits, then it's impossible.

For r=2:

Check if there are any mod2 digits. If yes, remove the smallest mod2 digit.

Else, check if there are at least two mod1 digits. Remove the two smallest mod1 digits.

Once the digits are removed, check if there's at least one zero left. If not, then output -1. Also, the sum of the remaining digits must be divisible by 3.

But after removal, how to check.

Alternatively, after removing the required digits, check if the remaining digits include at least one zero and that their sum is divisible by 3.

But in code, how to handle this.

Let's think of the digits as a list sorted in descending order.

So first, after removing the digits, we need to check:

- Are there any zeros left?
- Is the sum of the remaining digits divisible by 3?

But since we removed the digits according to the rules, the sum should be divisible by 3.

Wait, for example, if the sum was 1 mod3 and we remove one mod1 digit, the new sum is 0 mod3. So sum is divisible by 3. Similarly for other cases.

So perhaps after removing the digits, the sum is guaranteed to be divisible by3.

But wait, let's verify.

Original sum: S.

Case r=1.

If we remove one digit d where d mod3 =1. Then S_new = S - d. Since S mod3 was 1, (S -d) mod3 = (1 - (d mod3)) mod3 = (1 -1) mod3 = 0. Correct.

If we remove two digits d1 and d2, both mod2. Then (d1 +d2) mod3 is (2+2) mod3 = 1. So S_new = S - (d1+d2) → mod3 is (1 -1) mod3 =0. Correct.

Case r=2.

If we remove one digit d mod3=2. Then S_new = S -d → (2 -2) mod3=0. Correct.

If we remove two digits d1 and d2 mod3=1. Sum (d1+d2) mod3 is 2. So S_new mod3 is (2 -2) mod3=0. Correct.

So after removal, sum is divisible by3.

So in code, after removal, the sum is okay. But we need to check if the digits after removal have at least one zero and are not empty.

So steps after removal:

1. Check if the remaining digits (after removal) have at least one zero. If not, output -1.

2. Check if the remaining digits are empty (but zero is there, so perhaps not possible). But after removal, if all digits were removed except zero, then it's allowed.

Wait, for example, if after removal, the digits left are [0], then output 0.

So after removal:

- If the list is empty → impossible. But since we have at least one zero, this can't happen.

Wait, no. Because we have at least one zero in the original list, and in the process of removal, how can all digits be removed except the zero? Let's see.

Original digits include at least one zero.

So during removal, we are removing digits other than zero (since zero mod3 is 0, so in the case where sum mod3 is 1 or 2, the digits to be removed are from mod1 or mod2 groups. The zero is in mod0. So during removal, zero is not removed. So after removal, the zero must still be present. Wait, is that correct?

Wait, in the case where the sum mod3 is 1, we need to remove a mod1 digit. So if the zero is present, it's mod0. So when we remove a mod1 digit, the zero is not removed. So after removal, the zero is still present. Similarly for other cases.

Wait, no. Wait, the zero is part of the original digits. But during the removal process, we might have to remove some digits. For example, suppose the digits are [0], sum is 0. So mod3 is 0. Then output 0. But if the digits are [0,1], sum is 1. mod3 is1. Need to remove one mod1 digit (the 1). Then the remaining digits are [0], which is allowed. So in this case, after removal, the zero is present.

But suppose the digits are [0,2], sum is 2. mod3 is2. Need to remove one mod2 digit (2). Then remaining digits are [0], which is allowed.

So during the removal process, the zero is not removed. Because the digits being removed are mod1 or mod2, and the zero is mod0. So after removal, the zero is still present.

Thus, after removal, the remaining digits must have at least one zero.

Thus, in code, after the removal steps, we can proceed to check if the remaining digits are empty (only possible if all were removed except zero? No. Because the zero is part of the digits. So after removal, the digits must include at least the zero. So the remaining list can't be empty. For example, if the original digits are [0,1], sum is1 mod3=1. Remove 1, digits left [0]. So output 0.

But in code, after removal, the digits list may be just [0], which is allowed. Or if there are other digits plus zero.

Thus, after the removal steps, the digits are the ones to form the maximum number. So:

- Sort the remaining digits in descending order (but they were already sorted, but after removal of some digits, need to re-sort? Or when the digits are stored as a list, and we remove certain elements, then we can sort again?)

Wait, no. Suppose the digits were initially sorted in descending order. Then when we remove some digits (e.g., the rightmost mod1 digit), the list after removal is already in order (since we removed elements from the end). So the list remains sorted. Wait, but when you remove elements from the middle, the list is no longer sorted. Wait, no. Because in the initial list, the digits are sorted in descending order. So when you remove a digit from the list, the list is still sorted in descending order. Wait, no. For example, the list is [9,7,5,4,3,0]. If you remove the 3 (which is a mod0 digit), the list becomes [9,7,5,4,0], which is still sorted. So if you remove digits from anywhere in the list, as long as the list is sorted in descending order and the removal is of the correct digits (smallest in their mod group), then the remaining digits are sorted.

Wait, but how to find the right digits to remove. For example, if the digits are [9,8,7,4,3,0], sum is 9+8+7+4+3+0=31 mod3 is 1. So need to remove a mod1 digit.

Mod1 digits are 7 (7 mod3=1),4 (4 mod3=1). The smallest mod1 digit is 4, which is at index 3. So we remove that digit, and the list becomes [9,8,7,3,0]. Which is still sorted in descending order.

So the approach is to find the rightmost (smallest) mod1 digit, or the two rightmost mod2 digits, etc.

Thus, in code:

After sorting the digits in descending order, we can process them as follows:

For the case where sum mod3 is 1:

- Iterate from the end of the list (smallest digits) to find the first mod1 digit. Remove it.

- If no mod1 digits, find two mod2 digits (again, the two rightmost) and remove them.

For mod3=2:

- Iterate from the end to find the first mod2 digit and remove.

- Else, find two mod1 digits (rightmost two) and remove.

So how to implement this.

First, let's collect the digits in a list sorted in descending order.

Then, for each case:

We can loop through the list in reverse order (from the end) to find the required digits.

For example, for mod1 digits in case r=1:

for i in reversed(range(len(digits))):

   if digits[i] %3 ==1:

      remove digits[i]

      break

If not found, then look for two mod2 digits:

count =0

to_remove = []

for i in reversed(range(len(digits))):

   if digits[i] %3 ==2:

      to_remove.append(i)

      count +=1

      if count ==2:

          break

if len(to_remove) ==2:

   remove the digits at to_remove[0] and to_remove[1] (since reversed order, the indexes are higher first)

But when you remove from the list, you have to be careful with the indexes.

Wait, in Python, if you have a list and you remove elements from higher indexes first, the lower indexes are not affected. For example, if a list is [a, b, c, d], indexes 0-3. If you remove element at index 3 (d), then the list is [a,b,c]. Then remove element at index 2 (c) → [a,b].

So if you have to remove two elements, you can collect their indexes in a list sorted in descending order (so that when you remove them in that order, the indexes remain valid).

So for example, in the case where you need to remove two mod2 digits, collect their indexes in reversed order (from the end of the list). Then sort those indexes in reverse order (so highest first), then remove them in that order.

Alternatively, in the code:

after finding the indexes in reversed order, we can collect them as a list, then sort in reverse order (so that when we remove from the list, the higher indexes are removed first, so lower indexes are not shifted before processing).

Alternatively, collect the indices in a list, and then iterate over them in reverse order.

Wait, perhaps the code would look like this:

For r=1, and need to find two mod2 digits:

digits_sorted = sorted(digits, reverse=True)

indices = []

for i in reversed(range(len(digits_sorted))):

   if digits_sorted[i] %3 ==2:

      indices.append(i)

      if len(indices) ==2:

          break

if len(indices) <2:

   return -1

else:

   # remove the two indices, but since they are in reversed order, indices are from higher to lower.

   # to remove them in order, we can sort them in reverse order and delete.

   # but since the indices were collected in reversed order, the first in the list is the rightmost (smallest) digit.

   # wait, reversed(range(len(digits_sorted))) gives the indices from len-1 down to 0.

   # So for example, in a list [9,8,5,4,3,0], the digits are 9,8,5,4,3,0. Reversed indices are 5,4,3,2,1,0.

   # So when iterating over reversed(range(len)), i starts at 5 (0), then 4 (3), etc.

   # Suppose digits_sorted[i] is 5 → i=2 (since 5 is at index 2 in the list [9,8,5,4,3,0]). Wait, no.

Wait, the code is:

digits_sorted = sorted(digits, reverse=True)

Then, in the loop:

for i in reversed(range(len(digits_sorted))):

   # i starts from len-1, len-2, ..., 0

   if digits_sorted[i] %3 ==2:

      indices.append(i)

      if len(indices) ==2:

          break

So for example, if the list is [9,8,5,4,3,0], sorted in descending order.

digits_sorted[i] for i in reversed(range(6)) → i=5 (0), i=4 (3), i=3 (4), i=2 (5), i=1 (8), i=0 (9).

So in this case, the code loops from i=5 (digit 0) down to 0 (digit 9).

But mod3 of 0 is 0, 3 mod3 is 0, 4 mod3 is 1,5 mod3 is 2,8 mod3 is 2,9 mod3 is 0.

So mod2 digits are 5 and 8. Their indexes in digits_sorted are 2 (5) and 1 (8).

So when we loop over i in reversed(range(6)) → 5,4,3,2,1,0:

At i=5: digits_sorted[5] is 0 → mod0. Not collected.

i=4: 3 → mod0.

i=3:4 → mod1.

i=2:5 → mod2. Add i=2 to indices.

i=1:8 → mod2. Add i=1. Now indices has 2,1. Break loop.

Then, indices is [2,1]. Now, we need to remove these two digits.

But when you remove elements from the list, the indices shift. So if you remove index 2 first, then the list is [9,8,4,3,0]. Then, the next index is 1 (which was originally 8, but after removing index 2, the list becomes [9,8,4,3,0]. Then removing index 1 (8) gives [9,4,3,0].

Wait, but in the code, the digits_sorted list is a list in memory, and when we collect the indices, we can delete them in reverse order. For example, in the indices list [2,1], which are the two digits to remove. But in the original list, the indices are 2 and 1. So if we delete index 2 first, the list becomes [9,8,4,3,0]. Then, index 1 is now 8 (which is mod2). So after deleting both, the digits are 9,4,3,0. Sum is 9+4+3+0=16. Wait, but original sum was 9+8+5+4+3+0 = 29. 29 mod3 is 2. Then sum after removing 5 and 8 (sum 29-5-8=16 → 16 mod3 is 1. Hmm, this seems incorrect. So maybe there's a mistake here.

Wait, original sum is 9+8+5+4+3+0 = 29. 29 mod3 is 29 /3 is 9*3=27, 29-27=2 → mod3 is 2.

But the code is for sum mod3 is 1. So this example may not fit.

Let's take another example where sum mod3 is 1.

Example: digits are [9,4,4,0]. sum is 9+4+4+0=17. 17 mod3 is 2 (since 3*5=15, 17-15=2). So sum mod3 is 2, not 1. Hmm. Let's find an example where sum mod3 is 1.

Another example: digits are [7, 4, 0]. sum is 11. mod3 is 2. No. Or [5,5,0]. sum 10 mod3 1. So mod3 is 1.

So in this case, the code would need to remove a mod1 digit.

Looking for mod1 digits: 5 mod3 is 2. 5 mod3 is 2. So sum mod3 is (5+5) =10 mod3=1. So sum mod3=1.

Digits sorted descending: [5,5,0]. sum 10 mod3=1. So need to remove a mod1 digit. But there are no mod1 digits here. So code would look for two mod2 digits.

The mod2 digits are 5 and 5. So code would remove the two smallest mod2 digits, which are the two 5s. After removal, digits are [0]. So output is 0.

But sum after removal is 0, which is divisible by3. And there's a zero. So correct.

So code would proceed as follows.

So in code:

We need to process the digits as a list sorted in descending order. Then, for the given remainder, find the digits to remove.

So here's the plan for code:

1. Read n, then read the list of digits as integers.

2. Check if there's no zero → output -1.

3. Sort the digits in descending order.

4. Compute sum_total = sum(digits).

5. If sum_total ==0 → output 0.

6. Else, compute remainder = sum_total %3.

7. If remainder ==0:

   → check if there is a zero (already ensured). Then, check if all digits are zero (sum is zero → already handled). So output the digits as sorted, joined. But if the digits after sorted start with zero (e.g., [0,0,0]), output 0.

   So in code: after joining, if the first character is '0', then output '0'. Else, output the joined string.

   For example, digits [3,0] → sorted as ['3','0'] → '30' → output 30.

   Digits [0,0,0] → sum is zero → output 0.

8. Else:

   → handle the remainder.

   So for remainder in [1,2]:

      a. Create a list of digits (sorted in descending order).

      b. Attempt to remove digits as per the remainder.

      c. Check if after removal, the digits have at least one zero.

      d. If no possible way to remove → output -1.

      e. Else, form the number and output.

So code steps for remainder !=0:

For remainder=1:

- Look for a mod1 digit (digit%3 ==1).

   - Find the smallest such digit (rightmost in the sorted list).

   - Remove it.

   - If no such digit, look for two mod2 digits.

For remainder=2:

- Look for a mod2 digit.

   - Remove the smallest (rightmost).

   - If none, look for two mod1 digits.

Once the digits are removed, check if the remaining digits have at least one zero (which is guaranteed as per earlier steps). But also, the sum must be divisible by 3.

But after the removal steps, sum is divisible by3.

So code:

Implement the removal steps.

But how to find and remove the digits.

Implementation steps for remainder=1:

digits_sorted = sorted(digits, reverse=True) → list of integers.

removed = False

found = False

# Try to remove one mod1 digit.

for i in reversed(range(len(digits_sorted))):

   if digits_sorted[i] %3 ==1:

      del digits_sorted[i]

      removed = True

      break

if not removed:

   # Try to remove two mod2 digits.

   indices = []

   for i in reversed(range(len(digits_sorted))):

      if digits_sorted[i] %3 ==2:

         indices.append(i)

         if len(indices) ==2:

             break

   if len(indices) <2:

       # Can't form the number.

       print(-1)

       exit()

   else:

       # Remove the two indices in reverse order (so higher indices first)

       for i in sorted(indices, reverse=True):

           del digits_sorted[i]

       # Check if after removal, there are digits left and at least one zero.

       # But since original digits have at least one zero, and we are removing mod2 digits, which do not include zero, the zero remains.

So after removal, digits_sorted contains the remaining digits.

But after removal, the digits may be empty except for zero? Like [0], which is allowed.

So after removal, check if the digits_sorted is not empty and contains at least one zero.

But since the original digits contained at least one zero, and we are not removing any zero, the remaining digits will have at least one zero.

So digits_sorted can be [0], which is allowed.

So after removal, proceed to form the number.

Then, check if digits_sorted is empty. But no, because we have at least one zero.

But digits_sorted can be [0], which is allowed.

So after processing, digits_sorted is formed. Now, we need to check:

- If all remaining digits are zero → output 0.

- Else, output the digits joined as a string.

But how to check if all digits are zero.

sum_new = sum(digits_sorted)

if sum_new ==0:

   print(0)

else:

   # check if the first digit is zero (which can only happen if all are zero, but sum_new is zero).

   # but sum_new is zero, which is handled.

So after processing, digits_sorted is the list of remaining digits.

sum_new = sum(digits_sorted)

if sum_new ==0:

   print(0)

else:

   # check if digits_sorted is empty. Not possible, since we have zero.

   # then, form the number.

   # but the digits are already sorted in descending order.

   # join them as strings.

   # but need to avoid leading zeros. So if the first digit is zero, then sum_new must be zero → already handled.

   print(''.join(map(str, digits_sorted)))

Wait, but in the case where sum_new is not zero, but digits_sorted has a leading zero.

But sum_new is not zero, which implies that digits_sorted contains non-zero digits. So the first digit can't be zero.

For example, digits_sorted is [0,3,0]. But sorted in descending order → [3,0,0]. So sum is 3. So sum_new is 3, which is not zero. So the code outputs '300'.

But the sum is 3, which is divisible by3. So the number 300 is valid.

Thus, after processing, the code can join the digits and output.

Thus, the code steps are:

After the removal steps:

sum_new = sum(digits_sorted)

if sum_new ==0:

   print(0)

else:

   print(''.join(map(str, digits_sorted)))

But wait, what if the digits_sorted is [0,3,0], sorted in descending order would be [3,0,0], which is correct.

So in code:

Now, implement this.

But also, after the removal steps, we have to ensure that digits_sorted is not empty.

But since original digits had at least one zero and the removal steps don't remove zeros, digits_sorted will have at least one zero. So if after removal, all other digits are removed, digits_sorted will be [0], sum_new is zero → output 0.

But in cases where after removal, there are non-zero digits and zero(s), sum_new is not zero → output the digits in sorted order.

So the code is:

Now, let's put it all together.

The code:

Read n.

Read the list of digits as integers.

Check if 0 not in the list → output -1.

Sort the digits in descending order.

sum_total = sum(digits)

If sum_total ==0 → output 0.

Else:

   remainder = sum_total %3.

   if remainder ==0:

      # check if all digits are zero → handled by sum_total ==0.

      # proceed to output.

      # but digits are sorted in descending order.

      # check if after joining, the first character is '0' → implies all digits are zero.

      # but sum_total is not zero (sum_total was handled earlier). So digits must have non-zero digits.

      # but sum_total is non-zero and remainder is zero, so sum is at least 3.

      # So digits_sorted must have non-zero digits.

      # So the first character is not zero.

      # So output the joined digits.

      # but wait, for example, digits are [0,0,3]. sorted descending is [3,0,0]. sum is 3 → remainder 0. So output '300'.

      # which is correct.

      # So code can proceed.

      # but need to check if sum_new is zero.

      # but sum_total is not zero, so sum_new is sum_total → which is non-zero.

      # So no problem.

      # So output the digits joined.

      # but digits_sorted is already sorted in descending order.

      print(''.join(map(str, digits)))

   else:

      # handle remainder 1 or 2.

      digits_sorted = digits.copy() → no, in Python, need to create a new list.

      Wait, the original digits list is sorted in descending order.

      digits_sorted = sorted(digits, reverse=True) → no, because digits is already sorted.

      Wait, no: digits is read from input, then sorted in descending order.

      So after step 3 (sorting), digits is sorted in descending order.

      So in code:

      digits = sorted(digits, reverse=True)

      Then, for remainder 1:

      code to process.

      So in the code:

      if remainder == 1:

          # try to remove one mod1 digit.

          removed = False

          for i in reversed(range(len(digits))):

              if digits[i] %3 ==1:

                  del digits[i]

                  removed = True

                  break

          if not removed:

              # remove two mod2 digits.

              indices = []

              for i in reversed(range(len(digits))):

                  if digits[i] %3 ==2:

                      indices.append(i)

                      if len(indices) ==2:

                          break

              if len(indices) <2:

                  print(-1)

                  exit()

              else:

                  for i in sorted(indices, reverse=True):

                      del digits[i]

          # check if digits is empty. But digits must contain at least one zero.

          # so no.

      elif remainder ==2:

          # similar logic.

          removed = False

          for i in reversed(range(len(digits))):

              if digits[i] %3 ==2:

                  del digits[i]

                  removed = True

                  break

          if not removed:

              # remove two mod1 digits.

              indices = []

              for i in reversed(range(len(digits))):

                  if digits[i] %3 ==1:

                      indices.append(i)

                      if len(indices) ==2:

                          break

              if len(indices) <2:

                  print(-1)

                  exit()

              else:

                  for i in sorted(indices, reverse=True):

                      del digits[i]

      # Now, after processing, digits has at least one zero.

      # Check sum.

      sum_new = sum(digits)

      if sum_new ==0:

          print(0)

      else:

          # check if digits is empty.

          # digits has at least one zero.

          # but can't be empty.

          # output the digits sorted in descending order.

          # but digits is already sorted, except that after deletions, the list may not be sorted.

          # Wait, digits are initially sorted in descending order.

          # When we remove elements, the remaining elements are still in order.

          # For example, [9,8,7,4,3,0] → remove 4 (at index 3) → [9,8,7,3,0], which is still sorted.

          # But if we remove elements from other positions, but in the initial sorted list, the digits are in order.

          # So after deletions, the remaining elements are in order.

          # So no need to re-sort.

          # So join the digits.

          # Also, check if all digits are zero (sum_new is zero → handled).

          # So proceed.

          print(''.join(map(str, digits)))

But wait, after deletion, the digits may not be in sorted order. For example:

Original digits: [7,4,1,0]. sum is 12 → mod3 0. So output 7410. But if sum was 13, mod3 is1. Need to remove a mod1 digit.

In this case, digits are sorted as [7,4,1,0]. Sum is 12. mod3 is 0. So no. But if sum was 13 (like adding a 1), then the digits are sorted as [7,4,1,1,0]. sum 13 mod3 1. Remove the rightmost mod1 digit (the 1 at index 3). digits becomes [7,4,1,0]. Which is sorted as 7,4,1,0. But 1 is less than 4. So the list is no longer in descending order.

Wait, this is a problem.

So the code's approach of deleting certain elements from the sorted list can lead to the remaining list not being sorted in descending order.

So this is a critical mistake.

Ah, this is a major flaw in the approach.

For example, the digits are [7,4,1,0], sum is 12. mod3 is 0. So output is 7410.

But suppose sum is 13 (like adding a 1 → digits [7,4,1,1,0]. sum is 13 mod3=1. Then, code removes the rightmost mod1 digit, which is the 1 at index 3. The remaining digits are [7,4,1,0]. Which is sorted as [7,4,1,0]. But 1 comes after 4, which is not descending order.

So the code will output '7410', but this is not sorted in descending order. So the digits are 7,4,1,0 → which is 7410. But the maximum possible number would be 7410, which is correct. Because the digits after deletion are [7,4,1,0], which is not sorted, but the code assumes that the list is still sorted. But in reality, after deletion, the list may not be sorted.

Wait, but when the code initially sorts the digits in descending order, then when we remove a digit from the list, which is in the middle, the list is no longer sorted. For example, in the example [7,4,1,0], after removing 1 (index 2), the list becomes [7,4,0], which is sorted.

Wait, no. Original list is [7,4,1,0]. The digits are sorted in descending order. So after deleting the 1 (index 2), the list becomes [7,4,0], which is sorted in descending order.

Ah, right. Because in the original sorted list, the digits are in descending order. So when you remove a digit, the remaining digits are still in order. Because the digits are sorted in descending order, and you remove a digit. For example, digits are [7,4,1,0], sorted. Removing 4 → list becomes [7,1,0], which is not sorted. Wait, this is a problem.

Wait, no. Original list is [7,4,1,0]. If I remove 4 (index 1), the list becomes [7,1,0]. Which is 7,1,0 → not sorted. So the code's approach of deleting elements from the list after sorting will leave the list unsorted.

So this is a major problem. The code's assumption that the remaining list is sorted is incorrect.

This means that after deleting elements, the digits_sorted list may no longer be sorted, leading to an incorrect output (not maximum possible number).

So the code approach is flawed. The mistake is that after deleting elements, the list is no longer sorted, so the code outputs the digits in the order they are in the list (which may not be sorted), resulting in a non-maximal number.

Thus, the code needs to re-sort the digits after deletion, but this would require handling the digits again.

But how to resolve this.

Alternative approach:

After deletion, the remaining digits should be sorted again in descending order.

But how to do this.

Because when you delete some digits, the remaining digits may not be in sorted order. So after deletion, you need to re-sort them.

But then, in the code:

After deletion, the code will have a list of digits that may not be sorted, so we need to sort them in descending order again.

For example, in the case where we remove digits from the middle of the list:

Original sorted list: [7,4,1,0]. Delete the 4 (index 1) → list becomes [7,1,0]. Then re-sort in descending order → [7,1,0] → sorted as [7,1,0] → no, sorted in descending order would be [7,1,0]. Wait, but 1 is less than 7 but higher than 0. So after deletion, the list is already in descending order.

Wait, no. Let's see.

If the original list is sorted in descending order, and we delete an element that is not at the end, the remaining elements are still in descending order.

Because the original list is in non-increasing order. Removing any element leaves a list that is still in non-increasing order.

Wait, let's see.

Take example list: [9,7,5,4,3,0].

If we delete 7 (index 1), the new list is [9,5,4,3,0]. Which is still in descending order.

If we delete 5 (index 2), new list is [9,7,4,3,0] → descending.

If we delete 3 (index 4), new list is [9,7,5,4,0] → descending.

Thus, deleting any element from a sorted list (in descending order) leaves the list still sorted in descending order.

Because the elements before the deleted element are >= the deleted element, and the elements after are <= the deleted element. So when we delete an element, the elements before are >= the elements after.

Thus, the list remains sorted.

Thus, the code's approach of deleting elements and not re-sorting is valid.

But wait, in the example where the list is [7,4,1,0], and we delete the 4 (index 1):

Original list: 7,4,1,0.

After deleting 4, the list is [7,1,0]. Which is in descending order? 7>1>0. Yes.

So yes, the remaining list is still sorted.

Another example: [7,4,3,0]. Delete 4 → [7,3,0] → sorted.

So yes, deleting any element from a sorted list (descending) leaves the list sorted.

Thus, the code's approach of not re-sorting after deletion is correct.

Thus, the code's previous logic is correct.

Thus, in the code, after deletion, the digits list is still sorted in descending order.

Thus, the code can proceed to output the digits as they are, joined into a string.

Thus, the code will work.

Now, let's test the code with the examples.

Example 1:

Input:

1

0

Processing:

digits = [0]. sum is 0 → output 0.

Example 2:

Input:

11

3 4 5 4 5 3 5 3 4 4 0

Digits after sorting: [5,5,5,4,4,4,4,3,3,3,0]

sum_total = 3+4+5+4+5+3+5+3+4+4+0 → Let's compute:

3+4=7, +5=12, +4=16, +5=21, +3=24, +5=29, +3=32, +4=36, +4=40, +0=40. sum_total=40 → mod3 is 40 mod3 = 1 (3*13=39, 40-39=1).

So remainder is 1.

Processing remainder=1:

Try to remove one mod1 digit.

mod1 digits are digits where digit%3 ==1.

Digits sorted: [5,5,5,4,4,4,4,3,3,3,0]

Check each digit's mod3:

5 mod3 = 2.

5 mod3=2.

5 mod3=2.

4 mod3=1.

4 mod3=1.

4 mod3=1.

4 mod3=1.

3 mod3=0.

3 mod3=0.

3 mod3=0.

0 mod3=0.

So mod1 digits are the 4's at indices 3,4,5,6.

The code loops from the end (i=10 down to 0):

Check digits_sorted[i]%3 ==1.

i=10: 0 → mod0.

i=9:3 → mod0.

i=8:3 → mod0.

i=7:3 → mod0.

i=6:4 → mod1. So delete index 6. The digits_sorted becomes:

[5,5,5,4,4,4,3,3,3,0]

Wait, the original list was [5,5,5,4,4,4,4,3,3,3,0]. After deleting index 6 (the fourth 4), the list becomes:

[5,5,5,4,4,4,3,3,3,0]. Which is sorted.

sum_new = 40 -4=36 → mod3 0.

Thus, the code outputs 5554443330.

Which matches the example.

Another example:

Input:

8

3 2 5 1 5 2 2 3

Digits after sorting: [5,5,3,3,2,2,2,1]

sum is 5+5+3+3+2+2+2+1 = 23. 23 mod3 = 2.

So remainder=2.

Processing:

Need to remove one mod2 digit.

mod2 digits are digits%3 ==2 → 5,5,2,2,2.

In sorted list, these are the 5s and 2s.

Look for the rightmost mod2 digit → digits sorted list:

5,5,3,3,2,2,2,1.

Looping from the end (i=7 down to 0):

i=7:1 mod3=1 → no.

i=6:2 mod3=2 → yes. Delete index6. The digits become [5,5,3,3,2,2,1].

sum_new = 23-2=21 → mod3 0.

Check if there's a zero. But in this case, the original digits had no zero. Wait, no. Wait, original input is:

8

3 2 5 1 5 2 2 3

Which digits include 0? No. So the code would have already output -1 at step 2.

Wait, in this example, the input is the third example in the problem statement, which outputs -1. So according to the code, since there's no zero in the input, code outputs -1.

Ah, right. So the code would correctly output -1 for this example.

So the code's step 2 is to check if there's any zero in the input. Since there is none in this case, the code outputs -1, which matches the example.

Thus, the code handles all cases.

Now, code implementation in Python.

But need to handle the digits as a list, sorted in descending order.

Read the input:

n = int(input())

digits = list(map(int, input().split()))

Check if 0 not in digits → print -1.

Else:

sum_total = sum(digits)

if sum_total ==0 → print 0.

Else:

remainder = sum_total %3.

process accordingly.

So code:

n = int(input())
digits = list(map(int, input().split()))

if 0 not in digits:
    print(-1)
    exit()

digits.sort(reverse=True)
sum_total = sum(digits)

if sum_total ==0:
    print(0)
    exit()

remainder = sum_total %3

if remainder ==0:
    # Check if all are zero, but sum_total is non-zero. Impossible, since sum_total is sum of digits which includes 0 and others.
    # So output the digits joined.
    print(''.join(map(str, digits)))
else:
    # Handle remainder 1 or 2.
    # Make a copy of digits, as we need to modify it.
    digits_list = digits.copy()
    if remainder ==1:
        # Try to remove one mod1 digit.
        removed = False
        for i in reversed(range(len(digits_list))):
            if digits_list[i] %3 ==1:
                del digits_list[i]
                removed = True
                break
        if not removed:
            # Remove two mod2 digits.
            indices = []
            for i in reversed(range(len(digits_list))):
                if digits_list[i] %3 ==2:
                    indices.append(i)
                    if len(indices) ==2:
                        break
            if len(indices) <2:
                print(-1)
                exit()
            else:
                # Delete in reverse order.
                for idx in sorted(indices, reverse=True):
                    del digits_list[idx]
    else: # remainder ==2
        removed = False
        for i in reversed(range(len(digits_list))):
            if digits_list[i] %3 ==2:
                del digits_list[i]
                removed = True
                break
        if not removed:
            # Remove two mod1 digits.
            indices = []
            for i in reversed(range(len(digits_list))):
                if digits_list[i] %3 ==1:
                    indices.append(i)
                    if len(indices) ==2:
                        break
            if len(indices) <2:
                print(-1)
                exit()
            else:
                for idx in sorted(indices, reverse=True):
                    del digits_list[idx]
    # Check if digits_list is empty.
    # But since original list has 0, and we didn't remove it.
    # Now, check if there's at least one zero.
    # Also, sum_new is sum(digits_list).
    sum_new = sum(digits_list)
    if sum_new ==0:
        print(0)
    else:
        # Check if digits_list is not empty.
        # The digits_list is sorted in descending order.
        # Check if there's a zero.
        # But since original digits had at least one zero and we didn't remove any zeros (since mod3 is 0), there must be at least one zero.
        # So output the joined string.
        print(''.join(map(str, digits_list)))

But wait, after processing, the digits_list is modified. But in the code, digits_list is a copy of the sorted digits.

Wait, no. In the code:

digits_list = digits.copy()

digits is sorted in reverse order. So digits_list is a copy of that sorted list.

Yes.

But in Python, the list.copy() method creates a shallow copy.

Thus, the code for remainder 1 and 2 modifies the digits_list, which is a copy of the original sorted digits.

Thus, after processing, digits_list is the remaining digits, sorted in descending order.

Thus, the code should work.

But let's test the second example:

Input:

11

3 4 5 4 5 3 5 3 4 4 0

After sorting: [5,5,5,4,4,4,4,3,3,3,0]

sum_total is 40 → remainder 1.

Processing remainder 1:

Loop through digits_list in reversed order to find mod1 digit.

digits_list[6] is 4 → mod1. So delete index 6.

digits_list becomes [5,5,5,4,4,4,3,3,3,0].

sum_new is 40-4=36 → divisible by3.

sum_new !=0 → output digits_list joined as '5554443330'.

Which matches the example.

Thus, the code works.

Another test case:

Input:

3 2 5 1 5 2 2 3 → no 0 → output -1.

Another test case:

Input:

1

0 → output 0.

Another test case:

Input:

3 0 → digits sorted as [3,0]. sum 3 mod3 0 → output 30.

Thus, the code should handle all cases correctly.
</think>

```python
n = int(input())
digits = list(map(int, input().split()))

if 0 not in digits:
    print(-1)
    exit()

digits.sort(reverse=True)
total = sum(digits)

if total == 0:
    print(0)
    exit()

remainder = total % 3

if remainder == 0:
    print(''.join(map(str, digits)))
else:
    # Process for remainder 1 or 2
    processed = digits.copy()
    if remainder == 1:
        removed = False
        # Try to remove one mod 1 digit
        for i in reversed(range(len(processed))):
            if processed[i] % 3 == 1:
                del processed[i]
                removed = True
                break
        if not removed:
            # Remove two mod 2 digits
            indices = []
            for i in reversed(range(len(processed))):
                if processed[i] % 3 == 2:
                    indices.append(i)
                    if len(indices) == 2:
                        break
            if len(indices) < 2:
                print(-1)
                exit()
            for idx in sorted(indices, reverse=True):
                del processed[idx]
    else:
        # remainder == 2
        removed = False
        # Try to remove one mod 2 digit
        for i in reversed(range(len(processed))):
            if processed[i] % 3 == 2:
                del processed[i]
                removed = True
                break
        if not removed:
            # Remove two mod 1 digits
            indices = []
            for i in reversed(range(len(processed))):
                if processed[i] % 3 == 1:
                    indices.append(i)
                    if len(indices) == 2:
                        break
            if len(indices) < 2:
                print(-1)
                exit()
            for idx in sorted(indices, reverse=True):
                del processed[idx]
    
    # Check if there's at least one zero and non-empty
    if 0 not in processed:
        print(-1)
        exit()
    new_total = sum(processed)
    if new_total == 0:
        print(0)
    else:
        print(''.join(map(str, processed)))
```