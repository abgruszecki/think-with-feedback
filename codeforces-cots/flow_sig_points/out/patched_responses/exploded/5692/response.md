<think>
Okay, let's tackle this problem. The goal is to find the maximum permutation of the digits of a that doesn't exceed b. Both numbers are given as positive integers without leading zeros, and the output must be a permutation of a's digits with the same length. Also, the answer is guaranteed to exist.

First, I need to understand the constraints. Both a and b can be up to 1e18, which means their digit counts can be up to 18. That's manageable for Python since 18 digits aren't too big, but we need to process permutations efficiently.

Wait, but generating all permutations would be O(n!) which is way too slow for n=18. So brute-force is out of the question. So we need a smarter approach.

Let's think about the problem step by step. The output must have the same number of digits as a. So first, check if the length of a and b are different. Wait, no. Wait, the problem statement says that the output must have exactly the same length as a. So if a's length is different from b's, then:

- If a's length is longer than b's, then it's impossible. But the problem says the answer exists, so in that case, a's length must be equal to b's. So first check: if len(a) < len(b), then the maximum permutation of a is just the digits sorted in descending order. Because a has fewer digits, any permutation would be smaller than b which has more digits. Wait, no. Wait, a's length must be same as output's length. But the problem states that the answer exists. So if a's length is less than b's, then the maximum permutation is the digits sorted in descending order, since that would be the maximum possible permutation and definitely less than b. For example, if a is 123 (3 digits) and b is 4000 (4 digits), then the answer would be 321.

Similarly, if a's length is greater than b's, then since the answer exists, perhaps that's impossible. Because the problem says the answer exists. So the input will have a and b with the same length. Because if a's length is different from b's, the only possible case where the answer exists is when a's length is less than b's. Because then the maximum permutation (sorted descending) would be less than b, which has more digits. Otherwise, if a's length is longer, then the permutation would have more digits than b, making it larger, which is invalid. But the problem states that the answer exists, so the input must satisfy that. So the first step is to check if the lengths of a and b are different.

Wait, the problem's input says that a and b are positive integers without leading zeros, and the answer is guaranteed to exist. So the first case to handle is when the lengths of a and b are different. For example, if len(a) < len(b), then the maximum permutation of a's digits (sorted in descending order) is acceptable. Because it's a permutation with len(a) digits, which is less than len(b), so any permutation would be smaller than b. For example, if a is 123 (len 3) and b is 2222 (len 4), then the answer is 321. So that's the first case.

So the algorithm can be structured as follows:

1. Compare the lengths of a and b:
   a. If the lengths are different:
      i. If len(a) < len(b): then the answer is the digits of a sorted in descending order.
      ii. If len(a) > len(b): but the problem says answer exists, which implies that this case is impossible. So according to input constraints, we don't have to handle this.
   b. If the lengths are the same: then we need to find the largest permutation of a's digits that is <= b.

So the first step is to check the lengths. If they are different, then proceed accordingly. Otherwise, proceed to generate the largest possible permutation that's <= b.

So the main challenge is the case where the lengths are the same. Let's focus on that.

For example, given a=123 and b=222. The digits of a are 1,2,3. The maximum permutation <=222 is 213. So how do we find this?

The approach here is similar to generating the maximum number possible, digit by digit, while ensuring that the remaining digits can form a number that doesn't exceed the remaining part of b.

This sounds like a backtracking or recursive approach where we try all possible digits in order (from highest possible) and check if the remaining digits can form a valid suffix.

But since the length can be up to 18 digits, a naive backtracking approach would be too slow. So we need a more efficient way.

Another idea is to generate the maximum possible permutation by choosing each digit step by step, ensuring that the current prefix is as large as possible but not exceeding the prefix of b.

For example, let's take the digits of a sorted in descending order, and try to build the number digit by digit, ensuring that:

- At each step, the current digit is as large as possible, but not exceeding the corresponding digit in b. However, once a digit is chosen that is smaller than the corresponding digit in b, the remaining digits can be sorted in descending order to maximize the number. If a digit is chosen equal to the corresponding digit in b, then the remaining digits must form a number that is <= the remaining part of b.

So the steps could be:

1. Sort the digits of a in descending order. Let's call this sorted_digits.

2. Compare the sorted_digits as a number to b. If it's <=b, return it. That's the maximum possible.

3. If not, then we need to find the largest possible number that's <=b by adjusting the digits.

But how?

Let's consider building the number digit by digit. For each position i:

- Try the largest possible digit available (from the remaining digits) that is <= the i-th digit of b.

Wait, but that's not correct. For example, if the current digit is less than the i-th digit of b, then the remaining digits can be set to maximum possible (sorted descending). But if the current digit is equal, then the remaining digits must form a number <= the remaining part of b.

So the algorithm would involve:

For each position from left to right:

- Select the next digit from the available digits (sorted in descending order) that is <= the current digit in b.

   - If such a digit exists:

      - If the selected digit is less than the current digit in b: then take this digit, and append the remaining digits in descending order. Return this number.

      - If the selected digit is equal to the current digit in b: then proceed to the next position, but with the remaining digits and the remaining part of b.

   - If no such digit exists (i.e., all available digits are higher than the current digit in b), then backtrack to the previous position, choose the next smaller digit that allows the remaining digits to form a number that can be <= the required part.

This seems like a backtracking approach, which for 18 digits could be manageable with some optimizations. But how to implement this efficiently?

Alternatively, we can model this as a recursive or backtracking process with pruning. For each step, we track the available digits, and the current position. We also track whether we have already chosen a digit that is less than the corresponding digit in b (which allows us to choose the remaining digits in any order, preferably sorted descending to maximize the number). If not, then we are still bound by the digits of b.

This approach can be implemented using a backtracking approach with memoization, but given that the digits are up to 18, the worst case could be O(18*18) steps, which is manageable.

Let's think of the algorithm in more detail.

Suppose we have a list of available digits (sorted in descending order), and for each step, we are trying to choose a digit for the current position such that:

- If we have already used a smaller digit in a previous position (i.e., the prefix is already less than the prefix of b up to this point), then the current digit can be the largest possible remaining digit.

- If we are still bound by the digits of b (i.e., the prefix up to current position is exactly the same as the prefix of b), then the current digit must be <= the current digit of b, and also, after choosing this digit, we need to make sure that the remaining digits can form a number <= the remaining part of b.

So this can be modeled as a recursive function with parameters:

- current position (index)

- list of available digits

- tight: a boolean indicating whether the current prefix is exactly the same as the prefix of b up to this point (so future choices are constrained)

- current number being built as a list.

At each step, for the current index, if tight is True, then we can only choose digits <= the corresponding digit in b. For each possible digit (in descending order), we check if it's present in the available digits. Then, if the digit is less than the current digit of b, we can take this digit and proceed with tight=False, allowing the remaining digits to be arranged in descending order. If the digit is equal, we proceed with tight=True, requiring the next digits to also be constrained.

If at any step, we can't find a valid digit (when tight is True and no digits are <= the current digit), then we backtrack.

But how do we efficiently implement this in Python?

Alternatively, for each position, we can try the available digits in descending order and see if it's possible to form a valid number.

Let me outline the steps for the case where len(a) == len(b):

Let's call the digits of b as b_digits, which is a list of integers.

We have a list of digits from a, which we can count (using a frequency map or a sorted list).

We can process each position from left to right.

At each step, we need to choose a digit from the remaining digits. The choice depends on whether we are still tight (i.e., the prefix so far is exactly the same as b's prefix up to this point).

If tight is True, then the digit we choose must be <= b_digits[i]. Additionally, after choosing the digit, if it is less than b_digits[i], then tight becomes False for the next positions, allowing us to take the largest possible remaining digits. If it is equal, tight remains True for the next positions.

We need to proceed recursively, but with backtracking. However, backtracking for 18 digits might not be feasible. So perhaps a greedy approach can be applied here.

Wait, but a greedy approach might not work in all cases. For example, in the first sample input:

a is 123, sorted digits are [3,2,1]. b is 222. So the first digit is 3, which is larger than 2 (the first digit of b). So we can't take that. Then we look for the next possible digit, which is 2. So first digit is 2. Then the remaining digits are 3 and 1. Since the first digit is 2 (equal to b's first digit), the next digits must be <= 2 (the next digit of b). The next digit of b is 2. So possible digits are 3 (no, since 3>2), 2 (not available), 1. So the next digit is 1. Then the remaining digit is 3, which is 3. But the third digit of b is 2. So 3 is larger than 2, which is invalid. So this path is invalid. So we backtrack.

Wait, that's not right. Because the example's answer is 213. Let me see. So after choosing the first digit as 2, the remaining digits are 3 and 1. The next digit must be <=2. So possible digits are 1. So the second digit is 1. Then the third digit is 3. But 3>2 (the third digit of b). So the total would be 213, which is 213 <= 222. Wait, but 213 is 213 which is less than 222. So in this case, after the first two digits are 2 and 1, the third digit can be 3, but that's 213 which is 213 <222. So why is this acceptable?

Ah, because once the first digit is 2 (equal to b's first digit), but the second digit is 1 (less than b's second digit which is 2), then tight becomes False. So the remaining digits can be in any order (maximized). Wait, no. Wait, tight is a boolean that indicates whether the current prefix is exactly matching the b's prefix up to that point. So when we choose a digit less than the current digit of b, then tight becomes False, and in the next steps, the digits can be arranged in descending order to maximize the number. So in the case where the first digit is 2, the second digit is 1 (which is less than b's second digit of 2), then tight is False. So the third digit can be 3. So the total is 213. Which is correct.

So the process is:

- For each position, in order, select the largest possible available digit that allows the remaining digits to form a valid suffix.

So how to model this?

An efficient way would be to try all possible digits in descending order for the current position, and for each, check if the remaining digits can form a suffix that, when combined with the current prefix, is <= b.

So the steps are:

For the current position i:

1. Generate a list of candidate digits (sorted in descending order) from the available digits.

2. If we're still tight (i.e., the prefix up to i-1 is exactly equal to the first i-1 digits of b), then the current digit can be at most b_digits[i].

3. For each candidate digit in the sorted list (from highest to lower):

   a. If the digit is higher than allowed (when tight), skip.

   b. If the digit is available (count >0):

      i. Check if choosing this digit allows the remaining digits to form a valid suffix.

      ii. If yes, proceed with this digit, reduce the count, and proceed to the next position.

The problem is determining whether the remaining digits can form a suffix that, when combined with the current prefix, is <= b.

But how to check this quickly?

If we are not tight (i.e., the current prefix is already less than the first i digits of b), then the remaining digits can be arranged in descending order (to maximize the number), and it's guaranteed to be <= b. So in this case, we can take the largest possible digits.

If we are still tight, then the current digit must be <= b_digits[i]. Then, after choosing the current digit, the remaining digits must form a suffix that is <= the suffix of b starting at position i+1.

But the remaining digits can be arranged in any order. So the maximum possible arrangement would be the largest permutation of the remaining digits that is <= the remaining suffix of b.

But how to compute that? This seems like a recursive problem.

Alternatively, for the current position, once we choose a digit that is less than the current digit of b, then the rest can be arranged in descending order (max possible). So in that case, we can proceed.

If the digit is equal to the current digit of b, then the remaining digits must form a number <= the remaining part of b.

So the algorithm can be structured as follows:

At position i:

   For each candidate digit d in sorted (descending) order:

      if tight and d > b_digits[i]: skip.

      if d not available: skip.

      new_tight = tight and (d == b_digits[i])

      if new_tight is False:

          then the remaining digits can be arranged in descending order. The combined number will be current_prefix + [d] + sorted(remaining_digits, reverse=True)

          which is the maximum possible. Check if this number is <= b.

          if yes: return this number.

      else:

          check if the remaining digits can form a number that is <= the remaining part of b.

          if yes: proceed with d, subtract from available digits, and recurse on i+1 with new_tight.

So for the case when new_tight is False (i.e., the prefix up to i is already less than the prefix up to i of b), then the rest can be sorted in descending order, which is the maximum possible. So that's the best possible choice once we choose a d less than b_digits[i].

So for each possible d in descending order:

   if tight and d > b_digits[i], skip.

   check if d is available.

   then:

      if d < current_b_digit:

          take d, then append the remaining digits sorted in reverse. Check if this number is <= b. If yes, return this.

      else:

          check if the remaining digits (after taking d) can form a number <= the remaining part of b.

          if yes, proceed.

But how to check if the remaining digits can form a number <= the remaining part of b?

Wait, the remaining part of b is from i+1 to the end. The length of the remaining digits is the same as the length of this remaining part.

So for example, if the current position is i, then the remaining part of b is b's digits from i+1 onwards.

The remaining digits (after choosing d) must be arranged in a way that the suffix (from i+1) is <= the remaining part of b.

But the maximum possible suffix is the largest permutation of the remaining digits, which is sorted in descending order. So if even the maximum possible suffix is <= the remaining part of b, then it's possible.

Wait, no. Because the suffix is from i+1 onwards. So when tight is True (after choosing d equal to b's digit at i), the suffix must be <= the remaining part of b.

So the maximum possible suffix (sorted descending) must be <= the remaining part of b. If that's true, then it's possible. So the check can be:

After taking d (equal to b's digit at i), the remaining digits can be arranged in a way that the suffix is <= the remaining part of b. The best way to do this is to arrange the remaining digits in the largest possible order that is <= the remaining part of b.

But how do we check if there exists such a permutation?

This is the same problem as the original problem, but for the suffix.

So this becomes a recursive problem. For example, for the remaining digits and the remaining part of b, can we arrange them into a number that is <= that part?

So the algorithm can be implemented recursively. For each step, the available digits and the current position are tracked. But for 18 digits, this could be feasible if we optimize.

But how to implement this in Python efficiently?

Alternative approach: For each position, iterate through the digits in descending order. For each digit, check if it's possible to proceed. If possible, proceed and return the first valid path.

This is a backtracking approach with pruning. Since we process digits in descending order, the first valid path found is the maximum possible number.

So the steps for the code would be:

1. Check if the lengths of a and b are different. If len(a) < len(b), return the digits sorted in descending order.

2. Else, proceed:

   a. Check if the sorted digits of a (descending) is <= b. If yes, return that.

   b. Else, perform the backtracking approach to find the maximum possible permutation.

So for the code:

First, handle the case where lengths differ.

Then, when lengths are the same, proceed as follows.

Now, let's think about how to represent the digits. We can represent a's digits as a sorted list (descending), and as a frequency map (count of each digit). But perhaps using a list and a Counter or a frequency array.

Let's outline the code.

First, read a and b as strings.

a = input().strip()
b = input().strip()

if len(a) < len(b):
    # return sorted a in descending order
    sorted_a = sorted(a, reverse=True)
    print(''.join(sorted_a))
    exit()

elif len(a) > len(b):
    # according to problem statement, answer exists, but this case can't happen?
    # since answer must have the same length as a, but a's length is longer than b's, so any permutation of a's digits would have len(a) digits, which is longer than b's. Thus, such permutation would be larger than b, but the problem says answer exists. So this case is impossible. So the input would not have this case.

else:
    # lengths are equal. Proceed to find the max permutation of a <=b.

    a_digits = sorted(a, reverse=True)
    max_candidate = ''.join(a_digits)
    if max_candidate <= b:
        print(max_candidate)
        exit()
    else:
        # need to find the correct permutation.

        # digits of a and b are of same length.
        # proceed with backtracking approach.

        # digits of a as a list (sorted), and a frequency map.

        # So let's represent the digits as a frequency map.

        from collections import Counter

        a_counter = Counter(a)
        b_digits = list(b)

        # Now, generate the number digit by digit.

        # We can use a recursive function with backtracking.

        # But recursion may not be efficient. So perhaps use a backtracking approach with loops.

        # Let's try building the number step by step.

        # The approach is to try all possible digits in sorted order (descending) for each position.

        # For each digit in the current available digits:

        #   if the digit is larger than the current b's digit and tight is True, skip.

        #   else:

        #       if after choosing this digit, the remaining digits can form a valid number.

        #       if yes, proceed.

        # So the key is, for each choice, check if the remaining digits can form a valid suffix.

        # Let's implement this.

        n = len(a)

        result = []

        def backtrack(pos, counter, tight, current):

            if pos == n:
                # check if current <= b
                num = ''.join(current)
                if num <= b:
                    return num
                else:
                    return None

            # Try each possible digit in sorted order (descending)
            max_digit = b_digits[pos] if tight else '9'

            digits = sorted(counter.elements(), reverse=True)
            seen = set()
            for d in digits:
                if d in seen:
                    continue
                seen.add(d)
                if d > max_digit:
                    continue
                if counter[d] == 0:
                    continue

                # Check if we can take this digit.
                new_counter = counter.copy()
                new_counter[d] -=1
                if new_counter[d] ==0:
                    del new_counter[d]

                new_tight = tight and (d == max_digit)

                # If new_tight is False, then the remaining digits can be arranged in descending order.
                if not new_tight:
                    # collect remaining digits in sorted order and append.
                    remaining = sorted(new_counter.elements(), reverse=True, key=lambda x: x)
                    # flatten the list (since elements() returns (digit, count) tuples)
                    # Wait, no. new_counter is a Counter, and elements() gives each element as per their counts. But in Python's Counter, elements() returns all elements, including duplicates based on counts. For example, if '3' has count 2, elements() will yield '3', '3'.

                    # So to get the list of remaining digits, we can generate them from the Counter.
                    remaining_digits = []
                    for digit, cnt in new_counter.items():
                        remaining_digits.extend([digit]*cnt)
                    remaining_digits = sorted(remaining_digits, reverse=True)
                    candidate = current + [d] + remaining_digits
                    candidate_num = ''.join(candidate)
                    if candidate_num <= b:
                        return candidate_num
                else:
                    # proceed to next position.
                    next_num = backtrack(pos+1, new_counter, new_tight, current + [d])
                    if next_num is not None:
                        return next_num

            # Tried all digits and none worked.
            return None

        # Now, call the backtrack function starting from position 0, with the initial counter, tight=True, and current empty.

        ans = backtrack(0, a_counter, True, [])
        print(ans)

But wait, the 'backtrack' function as written may not work correctly because when new_tight is False, the code appends the remaining digits in sorted order and checks if the entire candidate number is <=b. But when new_tight is False, the candidate is current + [d] + sorted(remaining, reverse=True). Then, we check if this candidate is <=b. If yes, return it. Otherwise, proceed to try other digits.

But this approach might work. However, the code has several issues.

First, the code may not generate the correct candidate_num when new_tight is False. For example, when building the candidate, the remaining digits are sorted in reverse, but in the code, the candidate is current (a list) + [d] (a string) + remaining_digits (sorted in reverse). Then, the candidate_num is ''.join(candidate), which is the current digits plus d plus the remaining in sorted order. Then, check if this is <=b.

If yes, then this is the maximum possible number (since we are trying digits in descending order). So returning this candidate_num is correct.

But in the code, the way remaining_digits is generated is wrong. For example, new_counter is a Counter, which has (digit, count) pairs. The code loops over new_counter.items() and appends [digit]*cnt for each. Then, sorted in reverse. So that part is correct.

But in the code, when new_tight is False, the code constructs the candidate and checks if it is <=b. If yes, return it. Otherwise, proceed to the next digit.

But this might not be correct. Because the code returns the first candidate that meets the condition, which is the largest possible.

Wait, but we are iterating the digits in sorted order (descending). So for the first d that allows the candidate_num to be <=b, we return it. Since digits are processed in descending order, this will be the largest possible.

So this approach should work.

But in the code, the digits in the for loop are generated by sorted(counter.elements(), reverse=True). However, counter.elements() in Python returns elements with multiplicity, but sorted will sort each element, considering their multiplicity. For example, if the Counter is {'2': 2, '1':1}, elements() would yield '2', '2', '1', and sorted in reverse would be ['2', '2', '1']. But when generating the digits to try, we need to consider unique digits in the Counter, not including multiplicity. Because choosing a digit that has multiple counts is possible, but the code's 'seen' set ensures that each unique digit is tried once, but with the available count.

Wait, in the code:

digits = sorted(counter.elements(), reverse=True)

But 'counter.elements()' returns each element as many times as their count. So if a digit '3' has count 2, elements() returns '3' twice. So sorted in reverse would have ['3', '3', ...]. But then, the 'seen' set is used to skip duplicates. So for each d in digits, if it's in seen, skip. Then add to seen. So this way, even if the elements are repeated, they are considered once. So the code is trying each unique digit in the Counter, sorted in descending order.

But wait, if a digit '3' is present twice, then in the sorted list, it would appear as '3' multiple times. The 'seen' set will check if d has been processed, so for the first '3' in the list, it's added to the set, and subsequent '3's are skipped. So the code processes each unique digit once, sorted in descending order.

But the code needs to process all possible digits in the Counter, sorted in descending order. However, the code skips digits that have been seen (even if their count is more than one). So this is incorrect. Because the code is not considering digits with multiple counts. For example, if the Counter has two '3's, then the code would process '3' once, but there are two '3's available. So the code would only try using one '3', but perhaps there's a scenario where using two '3's is necessary.

Wait, but the code is handling this through the Counter. For example, when trying 'd' (e.g., '3'), the code checks the counter for 'd's count, subtracts one, and proceeds. So even if there are two '3's, the code will try using one '3' and decrement the count, allowing the next step to use another '3' if needed.

But the way the code is structured, the 'digits' list is generated by sorted(counter.elements(), reverse=True), which for a Counter with two '3's would produce ['3', '3', ...]. Then, the for loop iterates over these elements. However, the 'seen' set is used to skip duplicates. So the first '3' is processed, added to the seen set, and subsequent '3's are skipped. So in the for loop, even if there are two '3's available, the code would only try the first '3' once, but in reality, the code should try to use '3' as many times as possible (based on the count).

But the code's approach is incorrect here. Because the 'digits' list includes each digit as many times as their count. But using the 'seen' set to process each unique digit once per iteration is wrong. Because we need to try using a digit even if it's present multiple times. For example, if the Counter has two '3's, then choosing '3' is possible, and the code should try it. But with the 'seen' set, it's processed once, and the code proceeds with the first '3' in the list, then skips the others. But in reality, the code should process '3' once, and the remaining count is handled by the Counter.

Wait, perhaps the 'seen' set is unnecessary here. Because the code is generating the digits list as the elements of the Counter (with multiplicity), sorted in reverse order. For example, if the Counter is {'3':2, '2':1}, then sorted(counter.elements(), reverse=True) would be ['3','3','2'].

The for loop would iterate over each element in this list. However, the code uses 'seen' to track which digits have been processed. For example, when processing the first '3', 'd' is '3', which is added to 'seen'. The next '3' is in the loop, but since 'd' is '3' again, and it's in 'seen', the code skips it. So in this case, the code would process '3' once, even though there are two available.

But this is incorrect, because the code may need to use the same digit multiple times, but the 'seen' set prevents that.

So the problem is that the code is trying to process each digit once (per available digit in the Counter), but the way it's done is incorrect because the elements() function includes multiple instances of the same digit, which are then filtered out by the 'seen' set.

So the correct approach would be to iterate over the unique digits in the Counter, sorted in descending order, and then for each digit, check if it's available (count >0) and process it.

Thus, the code should generate the unique digits in sorted order, not the elements() list. For example, in the case where the Counter has {'3':2, '2':1}, the unique digits are ['3', '2'], sorted in descending order.

Then, for each digit in that sorted list, check if it's available (count >0).

So to fix the code:

Instead of:

digits = sorted(counter.elements(), reverse=True)
seen = set()
for d in digits:
    if d in seen:
        continue
    seen.add(d)
    ...

We should:

digits_sorted = sorted(counter.keys(), reverse=True, key=lambda x: int(x))
for d in digits_sorted:
    if counter[d] ==0:
        continue
    ...

Wait, but the Counter's keys() are the unique digits. So for each digit in sorted order, check if it's available (count >0). Then, proceed to use it.

So the corrected code would be:

digits_sorted = sorted(counter.keys(), reverse=True, key=lambda x: x)
for d in digits_sorted:
    if counter[d] ==0:
        continue
    if tight and d > max_digit:
        continue
    ...

But wait, the digits are strings, so comparing them as strings would compare their ASCII values. For example, '9' has a higher ASCII value than '8', etc. So sorted in reverse order would be correct.

So the code should generate the digits_sorted as the unique digits in the counter, sorted in descending order.

Thus, in the code:

digits_sorted = sorted(counter.keys(), reverse=True)

for d in digits_sorted:

    if counter[d] ==0:
        continue

    if tight and d > b_digits[pos]:
        continue

    # proceed with this digit.

So in this case, the code will try all unique digits in the counter, in descending order, and for each, check if available and allowed.

Then, proceed to use this digit.

This is correct.

So the code's for loop is incorrect in the current setup. It's generating the elements with multiplicity and using the 'seen' set to avoid processing the same digit multiple times, but this approach is wrong. The correct way is to process each unique digit once, sorted in descending order, and check if it's available.

So the corrected code would have:

digits_sorted = sorted(counter.keys(), reverse=True)
for d in digits_sorted:
    if counter[d] == 0:
        continue
    if tight and d > b_digits[pos]:
        continue
    # then, proceed as before.

Thus, the code can be adjusted.

Let's correct that part of the code.

Another issue is the handling of the Counter. For example, when we create a new_counter as a copy of the current counter, and decrement the count of d by 1. If the count becomes zero, we delete the key.

So for the code:

new_counter = counter.copy()
new_counter[d] -=1
if new_counter[d] ==0:
    del new_counter[d]

This part is correct.

Then, when new_tight is False, the code appends the remaining digits sorted in reverse order. This is done by:

remaining_digits = []
for digit, cnt in new_counter.items():
    remaining_digits.extend([digit]*cnt)
remaining_digits = sorted(remaining_digits, reverse=True)
candidate = current + [d] + remaining_digits
candidate_num = ''.join(candidate)
if candidate_num <= b:
    return candidate_num

This should generate the candidate number correctly.

If the candidate_num is <=b, then return it. Since we are trying digits in descending order, the first such candidate is the maximum possible.

Else, proceed to the next digit.

Now, let's test this logic with the first example:

a is '123' (digits 1,2,3), sorted is '321', which is 321 > 222.

So need to find the maximum permutation <=222.

The code starts with a_counter = {'1':1, '2':1, '3':1}.

pos=0, tight=True.

max_digit is '2' (b_digits[0]).

digits_sorted is ['3','2','1'].

First, d='3' (counter[d] is 1). tight is True, so check if d > max_digit (3>2). Yes, so skip.

Next, d='2' (counter[d] is 1). d <=2.

new_counter: after decrementing '2' becomes 0, so removed. new_counter is {'1':1, '3':1}.

new_tight is tight (True) and d == max_digit (2 ==2) → new_tight=True.

So proceed to pos=1, new_counter is {'1':1, '3':1}, tight=True.

pos=1:

b_digits[1] is '2'.

digits_sorted in new_counter are ['3', '1'].

Check d='3':

counter[d] is 1. tight=True → d='3' > '2' → skip.

Next, d='1' → allowed (1<=2).

new_counter becomes {'3':1}.

new_tight = True and (1 == '2') → false. So new_tight=False.

So, since new_tight is False, the remaining digits (after d=1) are ['3'], sorted reverse → ['3'].

candidate is current (['2','1']) + ['3'] → '213'.

Check if '213' <= '222' → yes. So return '213'.

Thus, the code returns the correct result.

Another example: a=3921, b=10000. The output should be 9321.

But len(a) is 4, len(b) is 5. So len(a) < len(b), so the code returns sorted a digits in descending order. Which is 9321. Which matches the example.

Another example: a=4940, b=5000. len(a) is 4, len(b) is4. sorted a is 9940, which is >5000. So need to find the correct permutation.

The code will try digits in order.

pos=0, tight=True. max_digit is '5'.

digits_sorted is ['9','4','4','0'] → wait, no. a's digits are 4,9,4,0 → sorted descending is ['9','4','4','0'].

Wait, a=4940 → digits are '4','9','4','0'. So when sorted in descending order, it's '9','4','4','0' → 9440. But b is 5000. 9440>5000. So the code proceeds to backtracking.

In the backtracking function:

At pos=0, tight is True. b_digits[0] is '5'.

digits_sorted in a_counter is ['9','4','0'] (since Counter has '9':1, '4':2, '0':1).

So for d in ['9','4','0']:

d=9: 9>5 → skip.

d=4: allowed. new_tight is True and (4 ==5 → false). So new_tight is False.

Then, remaining digits after taking 4 are ['9','4','0'] (since Counter is {'9':1, '4':1, '0':1}).

sorted in reverse → ['9','4','0'].

candidate_num is '4' followed by '9','4','0' → 4940. Which is <=5000. So return 4940.

Which is the correct output.

Thus, the code works for this case.

Now, the code needs to handle cases where the digits are not unique, and when the remaining digits can form the required suffix.

But implementing this correctly requires that the code iterates over the unique digits in descending order, and for each, proceeds as described.

Another test case is when a=121 and b=211. The maximum permutation is 211 (digits sorted as 211). But let's see:

sorted a is 211. Which is equal to b. So code returns 211.

Another test case: a=121, b=200. sorted a is 211>200.

So need to backtrack. pos=0, tight=True. max_digit is '2'.

digits_sorted for a's counter (1:2, 2:1) → ['2','1'].

At pos=0, try d=2. new_tight = True and (2 ==2 → True). Proceed to pos=1.

remaining digits: {'1':2}.

pos=1, tight=True. max_digit is '0' (b is 200, pos 1 is '0').

digits_sorted is ['1']. d=1 >0 → allowed? No. So no possible digits. Backtrack.

So backtrack to pos=0. Next d is '1'.

So pos=0: d=1. new_tight = True and 1 <2 → new_tight is False.

remaining digits: {'2':1, '1':1}.

sorted in reverse → '21'.

candidate_num is '1' + '21' → 121 <=200. So return 121. But is there a better option?

Wait, the maximum possible number is 112 (sorted a is 211, which is 211>200. The next best option is 121, but 112 is smaller than 121. Wait, but code returns 121 which is correct.

But in this case, the code chooses d=1 at pos=0, then appends remaining digits sorted as 2 and 1. So 1 +2+1 = 121. Which is allowed.

But wait, the candidate_num is 121, which is <=200, so it's acceptable.

But there is another permutation: 112, which is also <=200, but smaller than 121. But the code returns 121 as the maximum possible.

Which is correct.

Thus, the code seems to handle this case correctly.

Now, the code needs to be written in Python, with the corrections.

But implementing the backtrack function as a recursive function may have stack issues for n=18, but since the recursion depth is up to 18, which is manageable in Python.

But in Python, recursion for 18 levels is okay.

Thus, the code can be written as follows:

Read a and b as strings.

Check len(a) < len(b) → output sorted descending.

Else, if len(a) == len(b):

   if sorted a descending <=b → output that.

   else:

       proceed with the backtracking approach.

Implement the backtracking function with the correct handling of digits.

Now, the code can be written.

But in Python, for the backtracking function, the code should pass the current state (counter, tight, current path) and return the first valid candidate.

Now, let's code this.

Also, note that the digits are processed as strings, and the comparison is done lexicographically, which works correctly for numbers of the same length.

Thus, the code can be:

Implementing the corrected approach:

So the code will be:

Read a and b.

If len(a) < len(b): output sorted descending.

Else:

   if sorted a descending is <= b: output that.

   else:

       proceed to backtracking.

Now, for the backtracking function:

Use a function that tries each digit in sorted order (descending), and for each, checks if possible.

Implement the function as follows:

from collections import Counter

def main():
    a = input().strip()
    b = input().strip()
    
    if len(a) < len(b):
        # output sorted descending
        print(''.join(sorted(a, reverse=True)))
        return
    
    # len(a) == len(b)
    a_sorted = ''.join(sorted(a, reverse=True))
    if a_sorted <= b:
        print(a_sorted)
        return
    
    # need to find the maximum permutation <= b
    a_counter = Counter(a)
    b_digits = list(b)
    n = len(a)
    
    def backtrack(pos, counter, tight):
        if pos == n:
            return ''.join([])  # this will not be called as previous check a_sorted <=b failed
        
        max_digit = b_digits[pos] if tight else '9'
        # get sorted unique digits in counter in descending order
        digits_sorted = sorted(counter.keys(), key=lambda x: -ord(x))
        for d in digits_sorted:
            if counter[d] == 0:
                continue
            if d > max_digit:
                continue
            new_counter = counter.copy()
            new_counter[d] -= 1
            if new_counter[d] == 0:
                del new_counter[d]
            new_tight = tight and (d == max_digit)
            if not new_tight:
                # build the candidate with remaining digits in descending order
                remaining = []
                for digit, cnt in sorted(new_counter.items(), key=lambda x: (-ord(x[0]), x[0])):
                    remaining.append(digit * cnt)
                remaining_str = ''.join(remaining)
                candidate = (''.join(prev) if prev else '') + d + remaining_str
                if len(candidate) < n:
                    # this shouldn't happen
                    continue
                if candidate <= b:
                    return candidate
            else:
                res = backtrack(pos + 1, new_counter, new_tight)
                if res is not None:
                    return d + res
        return None
    
    # build the result step by step
    result = backtrack(0, a_counter, True)
    print(result)

if __name__ == "__main__":
    main()

But wait, this code has some issues. For example, the 'prev' variable is not defined in the candidate creation. Also, the code uses prev as ''.join(prev), which is not correct. The current path is not tracked in the backtrack function. So the candidate is built by d + remaining_str, but the current digits before pos are not considered.

So this approach is incorrect. Because the current digits (from pos=0 to pos-1) are not tracked.

Thus, the code needs to track the current digits built so far.

The earlier version of the backtrack function was passing 'current' as a list, but the code was not written correctly.

Alternatively, the code can track the current digits as a string, and pass them along.

But in the recursive function, building the candidate requires knowing the current digits up to pos.

So perhaps the backtrack function should return the best possible suffix starting at pos, given the current state.

The function backtrack(pos, counter, tight) returns the maximum possible suffix starting at pos, given the available digits in counter and the tight constraint.

In this case, the function builds the number from pos to the end.

Thus, when tight is True, the digits chosen must be <= the corresponding digits in b.

The code can be written as follows:

The backtrack function returns the maximum possible suffix starting at pos, given the current counter and tight constraint.

At each step:

For each digit d in sorted order (descending):

   if tight, d must be <= b_digits[pos]

   if d is available in counter:

      create new_counter with d's count decremented.

      new_tight = tight and (d == b_digits[pos]).

      if new_tight is False:

          the remaining digits can be arranged in descending order. Check if the formed number is <= b.

          if yes, return d followed by the sorted remaining digits.

      else:

          recursively call backtrack for pos+1.

          if the recursive call returns a valid suffix, return d + suffix.

Thus, the code can be:

def backtrack(pos, counter, tight):

    if pos == n:

        return ''

    max_digit = b_digits[pos] if tight else '9'

    digits_sorted = sorted(counter.keys(), key=lambda x: -ord(x))

    for d in digits_sorted:

        if counter[d] == 0:

            continue

        if d > max_digit:

            continue

        new_counter = counter.copy()

        new_counter[d] -=1

        if new_counter[d] ==0:

            del new_counter[d]

        new_tight = tight and (d == max_digit)

        if not new_tight:

            # build the remaining digits in descending order

            remaining = []

            for digit in sorted(new_counter.keys(), reverse=True):

                remaining.append( digit * new_counter[digit] )

            remaining_str = ''.join(remaining)

            current_suffix = d + remaining_str

            # check if current_suffix is <= b's suffix starting at pos

            # compare the current_suffix to b's substring from pos onward.

            # but since the tight is False, the entire suffix must be <= b's suffix.

            # but since the tight is False, the prefix up to pos is already less than b's prefix up to pos. So the suffix can be anything (maximized) but the overall number must be <=b.

            # So the candidate is the prefix up to pos-1 (not tracked here) followed by current_suffix.

            # But since the function is called from the root (pos=0), the candidate is current_suffix.

            # Wait, no. This function is supposed to return the suffix from pos onwards. So to check if the entire number formed by this suffix (starting from pos) is <=b's suffix from pos.

            # So when new_tight is False, the suffix is built as current_suffix, which is the largest possible. We need to check if the entire number from pos to end is <= b's pos to end.

            # For example, if pos is 0, then current_suffix must be <=b.

            # So the code can compare current_suffix <= b.

            # But how?

            # The candidate number is the current_suffix. So the entire number is current_suffix. But since we are at pos, the current_suffix is the digits from pos to the end. But wait, the prefix is not tracked here.

            # This approach is incorrect.

            # Because the function is supposed to return the suffix from pos, but the actual full number is the prefix up to pos-1 plus the suffix.

            # However, the function doesn't track the prefix, so how can we compare the entire number?

            # This is a problem.

            # Thus, the previous approach where the current prefix is tracked as a list (current) is needed.

            # So the backtrack function must track the current digits built so far.

Thus, the code needs to track the current prefix. So the backtrack function should take parameters pos, counter, tight, and current_prefix.

This way, when new_tight is False, the current_prefix + [d] + remaining_digits can be formed into a candidate_num and compared to b.

But passing current_prefix around can be done.

Thus, the correct backtrack function would need to track the current prefix.

This complicates the code, but is necessary.

So the code can be rewritten as follows:

def backtrack(pos, counter, tight, current_prefix):

    if pos == n:

        num = ''.join(current_prefix)

        return num if num <= b else None

    max_digit = b_digits[pos] if tight else '9'

    digits_sorted = sorted(counter.keys(), reverse=True)

    for d in digits_sorted:

        if counter[d] == 0:

            continue

        if d > max_digit:

            continue

        new_counter = counter.copy()

        new_counter[d] -= 1

        if new_counter[d] ==0:

            del new_counter[d]

        new_tight = tight and (d == max_digit)

        new_prefix = current_prefix + [d]

        if not new_tight:

            # build the remaining digits in descending order

            remaining = []

            for digit in sorted(new_counter.keys(), reverse=True):

                remaining.append( digit * new_counter[digit] )

            remaining_str = ''.join(remaining)

            candidate = ''.join(new_prefix) + remaining_str

            if candidate <= b:

                return candidate

        else:

            res = backtrack(pos+1, new_counter, new_tight, new_prefix)

            if res is not None:

                return res

    return None

This way, the current_prefix is built step by step, and when new_tight is False, the candidate is formed by appending the remaining digits sorted in reverse order.

This approach should work.

Thus, the code can be written as:

from collections import Counter

def main():

    a = input().strip()

    b = input().strip()

    if len(a) < len(b):

        # output sorted in descending order

        print(''.join(sorted(a, reverse=True)))

        return

    # len(a) == len(b)

    a_sorted = ''.join(sorted(a, reverse=True))

    if a_sorted <= b:

        print(a_sorted)

        return

    a_counter = Counter(a)

    b_digits = list(b)

    n = len(a)

    def backtrack(pos, counter, tight, current_prefix):

        if pos == n:

            candidate = ''.join(current_prefix)

            return candidate if candidate <= b else None

        max_digit = b_digits[pos] if tight else '9'

        digits_sorted = sorted(counter.keys(), reverse=True)

        for d in digits_sorted:

            if counter[d] == 0:

                continue

            if d > max_digit:

                continue

            new_counter = counter.copy()

            new_counter[d] -= 1

            if new_counter[d] == 0:

                del new_counter[d]

            new_tight = tight and (d == max_digit)

            new_prefix = current_prefix + [d]

            if not new_tight:

                # build the remaining digits in descending order

                remaining = []

                for digit in sorted(new_counter.keys(), reverse=True):

                    remaining.append(digit * new_counter[digit])

                remaining_str = ''.join(remaining)

                candidate = ''.join(new_prefix) + remaining_str

                if candidate <= b:

                    return candidate

            else:

                res = backtrack(pos + 1, new_counter, new_tight, new_prefix)

                if res is not None:

                    return res

        return None

    result = backtrack(0, a_counter, True, [])

    print(result)

if __name__ == '__main__':

    main()

This code should handle the cases correctly.

Testing with the first sample:

a=123, b=222.

a_sorted is '321' > '222'.

So backtracking starts.

pos=0, current_prefix is [], tight=True.

max_digit is '2'.

digits_sorted are ['3','2','1'].

d='3' is skipped (3>2).

d='2' is considered.

new_counter is {'1':1, '3':1}.

new_tight is True (2 ==2).

new_prefix is ['2'].

Proceed to pos=1.

At pos=1:

max_digit is '2' (b_digits[1]).

digits_sorted are ['3', '1'].

d='3' is skipped (3>2).

d='1' is considered.

new_counter is {'3':1}.

new_tight is False (1 <2).

new_prefix is ['2','1'].

new_tight is False → build candidate.

remaining digits: ['3'].

candidate is '21' + '3' → '213' which is <= '222'. So returns '213'.

Thus, the correct result.

Another test case: a=3921, b=10000. Since len(a) is4, len(b) is5. So output is sorted a descending: 9321.

Third test case: a=4940, b=5000.

sorted a is '9440' which is >5000.

Backtracking:

pos=0, max_digit='5'.

digits_sorted are '9','4','0'.

d='9' >5 → skipped.

d='4' is considered.

new_counter is {'9':1, '4':1, '0':1}.

new_tight is False (4 <5).

build candidate:

current_prefix is ['4'].

remaining digits are ['9','4','0'] sorted → '940'.

candidate is '4940' which is <=5000 → returns '4940'.

Thus, correct.

Thus, this code should work.
</think>

```python
from collections import Counter

def main():
    a = input().strip()
    b = input().strip()
    
    if len(a) < len(b):
        print(''.join(sorted(a, reverse=True)))
        return
    
    a_sorted = ''.join(sorted(a, reverse=True))
    if a_sorted <= b:
        print(a_sorted)
        return
    
    a_counter = Counter(a)
    b_digits = list(b)
    n = len(a)
    
    def backtrack(pos, counter, tight, current_prefix):
        if pos == n:
            candidate = ''.join(current_prefix)
            return candidate if candidate <= b else None
        
        max_digit = b_digits[pos] if tight else '9'
        digits_sorted = sorted(counter.keys(), reverse=True)
        
        for d in digits_sorted:
            if counter[d] == 0:
                continue
            if d > max_digit:
                continue
            
            new_counter = counter.copy()
            new_counter[d] -= 1
            if new_counter[d] == 0:
                del new_counter[d]
            
            new_tight = tight and (d == max_digit)
            new_prefix = current_prefix + [d]
            
            if not new_tight:
                remaining = []
                for digit in sorted(new_counter.keys(), reverse=True):
                    remaining.append(digit * new_counter[digit])
                remaining_str = ''.join(remaining)
                candidate = ''.join(new_prefix) + remaining_str
                if candidate <= b:
                    return candidate
            else:
                res = backtrack(pos + 1, new_counter, new_tight, new_prefix)
                if res is not None:
                    return res
        
        return None
    
    result = backtrack(0, a_counter, True, [])
    print(result)

if __name__ == '__main__':
    main()
```