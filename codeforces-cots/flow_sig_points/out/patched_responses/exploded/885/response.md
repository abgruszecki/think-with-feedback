<think>
Okay, so I need to solve this problem where I have to find the number of pairs of bracket sequences such that when concatenated, they form a regular bracket sequence. Hmm. Let's think about how to approach this.

First, let's understand what a regular bracket sequence (RBS) is. A RBS is balanced and properly nested. So, for a concatenated string s_i + s_j to be RBS, the total number of opening and closing brackets must be equal. Also, during the traversal, the number of closing brackets can't exceed the opening ones at any point.

So, the first thing is that the total number of '(' in s_i and s_j must equal the total number of ')'. So, for each s_i, we can compute the balance (number of '(' minus ')'). Let's call this balance for a string as 'total'. Then, for two strings to form a RBS when concatenated, the sum of their balances must be zero. Because (total_i + total_j) = 0.

Wait, but that's necessary but not sufficient. For example, two strings each with balance zero could have a concatenation that's not balanced. Like ")( " and "()". Their concatenation would be ")()(", which has balance zero but isn't a regular sequence.

But maybe the key insight here is to model the possible left and right contributions of each string. Let's think about each string's deficit and surplus.

Another approach: For a string s, compute two values:

- left: the minimum balance encountered while processing the string. This represents how much the string starts with a deficit. For example, a string like ")(" would have a left of -1. If the left is negative, then any string that comes before it must compensate for that.

- right: the balance after processing the entire string. So right = total number of '(' - total number of ')'.

So when concatenating s_i and s_j, the combined string's balance must be zero (so right_i + right_j = 0). Also, the left of s_i must be such that when combined with the right of s_i and the left of s_j, the entire sequence doesn't dip below zero.

Wait, perhaps the correct condition is:

For s_i + s_j to be a RBS, the following must hold:

1. The total balance of s_i and s_j must be zero. So right_i + right_j = 0.

2. The combined string must never have a negative balance at any point. 

But how to model this? Let's think about the possible contributions.

The first string s_i has a certain balance. Let's say s_i has a right value of a. Then, when we process s_i, the balance goes from 0 to a. Then, when processing s_j, the balance starts at a and must not drop below zero at any point. Also, the sum a + right_j must be zero (so a must be -right_j, but since the sum is zero, right_j = -a. So right_i is a, and right_j must be -a).

Wait, no. Because the sum of the two right values must be zero. So right_i + right_j = 0. So right_j = -right_i.

So, for two strings to be compatible, their right values must sum to zero. So, for a given string s_i with right = a, we need to find all strings s_j with right = -a. 

But even that's not enough. Because even if their sum is zero, the concatenation could have a negative balance in between. So, for example, s_i is "))((", which has right = 0. s_j is "()()", right is 0. But their concatenation is "))((" + "()()" which is "))(()()", which is not a regular sequence.

So, the sum of the right values is zero, but the concatenation is invalid. Therefore, we need more conditions.

So, let's model each string with three parameters:

- left: the minimum balance in the entire string. For example, for s = "())", the balance steps are 1, 0, -1. So left is -1.

- right: the total balance (number of '(' minus ')'). For s = "())", right is 1-3= -1 (wait wait, no: each '(' is +1, each ')' is -1. So for "())", the balance is +1 (after first '('), then 0 after ')', then -1 after the third ')'. So right is -1.

Wait, no. The right is the final balance, which is the sum of all '(' minus all ')'. So for a string like "(()", right is 3-1=2? Or wait, each '(' is +1, each ')' is -1. So the total balance is sum of all the characters. So for "(()", it's +1 +1 + (-1) = 1. So right is 1.

Ah right. So for a string, the right is the total balance. So for example, "()", the right is 0. For "(()", the right is 1. For ")(", right is 0.

So, the two conditions for s_i + s_j to be RBS are:

1. The sum of their right values is zero (so right_i + right_j = 0).

2. The combined sequence must never dip below zero balance at any point.

Now, how to model the second condition.

When we process s_i followed by s_j, the balance starts at 0. As we process s_i, the balance increases and decreases. The minimal value of the balance during s_i is left_i. After s_i, the balance is right_i. Then, when processing s_j, the balance starts at right_i, and must not drop below zero at any point. So:

The minimum balance in the entire concatenated string is the minimum of (the minimum balance during s_i) and (right_i plus the minimum balance during s_j). 

Wait, let's think step by step.

Let's model the balance as a function. For the first string s_i, during processing, the balance goes from 0 to right_i. Let's say that during processing s_i, the balance has a minimum value of left_i. 

Then, when processing s_j, the initial balance is right_i. Let the balance during s_j starts at right_i, and the minimum value during s_j's processing is (current_initial_balance + s_j's left). Because when processing s_j, the balance starts at right_i, and the minimal balance in s_j is (right_i + s_j's left). 

So for the entire concatenated string to not have a negative balance, the following must be true:

- left_i >= 0: because during processing s_i, the balance must never drop below zero. Otherwise, even in s_i alone, there's a point where balance is negative, so when concatenated with s_j, that part is in the first string and would make the entire sequence invalid.

Wait, no. For example, s_i is ")(", which has left_i = -1 and right_i = 0. s_j is "()", which has left_j=0, right_j=0. Then s_i + s_j is ")()()", which balance steps are -1, 0, 1, 0. The minimum is -1, which is invalid. So the concatenated string is invalid. So even if s_j has left_j=0, the left_i being negative makes the whole thing invalid. So, for s_i + s_j to be valid, the left_i must be >=0. Because during processing s_i, the balance can't go negative. Also, the processing of s_j can't cause the balance to dip below zero. 

Wait, perhaps the correct conditions are:

1. The sum of right_i and right_j is zero.

2. The left_i (the minimum balance of s_i) must be >= 0. Because during processing s_i, if the balance ever drops below zero, then the concatenated sequence is invalid.

3. The left_j (the minimum balance of s_j) plus the right_i (the starting balance when processing s_j) must be >=0. Because during processing s_j, the initial balance is right_i, and the minimal balance during s_j is (right_i + left_j). So if this sum is >=0, then during s_j, the balance never drops below zero.

So putting this together:

For s_i + s_j to form a regular bracket sequence, the following must hold:

- right_i + right_j = 0

- left_i >= 0

- right_i + left_j >= 0 

Because:

- The sum of the right balances must be zero (so the total is balanced).

- The first string s_i's processing must not have any point where the balance drops below zero (so left_i >=0).

- When processing s_j, starting from right_i, the balance during s_j must not drop below zero. The minimal balance in s_j is (right_i + left_j), which must be >=0.

So these three conditions must be met.

So the plan is:

For each string s, compute:

- left: the minimal balance during processing the string.

- right: the total balance (sum of all '(' as +1 and ')' as -1).

Then, group the strings based on their right value. For example, for a string with right = a, we can look for strings with right = -a. 

Now, for each pair (a, -a), we need to count the number of pairs (s_i, s_j) where s_i has right a, s_j has right -a, and s_i's left >=0, and s_j's left >= (-a). Because in the third condition: right_i is a, so right_i + left_j >=0 → a + left_j >=0 → left_j >= -a.

Wait, the third condition is right_i + left_j >=0. Since right_i is a, and we're pairing with s_j which has right_j = -a. So the condition becomes a + left_j >=0 → left_j >= -a.

So, for a given a, the possible s_j's are those with right_j = -a and left_j >= -a.

But how to efficiently compute this?

So the steps would be:

1. Preprocess all strings to compute their left and right values.

2. For each string, if it's possible to be part of a pair (i.e., for some j, their sum is zero and the other conditions are met), then we can categorize them based on their right.

3. For each a in the possible right values, collect all the counts of strings with right = a, left >=0. Then, for each such a, find the count of strings with right = -a, and left >= (-a). Multiply the counts and add to the total.

But how to handle this efficiently?

Wait, but the a can be any integer. So for each possible a, we need to find the number of strings with right = -a, and left >= -a. Then, multiply by the number of strings with right = a and left >=0.

So, the approach is:

- Create a dictionary (like a hash map) that maps each possible right value to a list of lefts for strings with that right.

But for efficient querying, perhaps we can precompute for each a, the number of strings with right = a and left >=0. Then, for each a, the number of strings with right = -a and left >= (-a) is needed, and multiply the two counts.

Wait, but the strings that have right = a and left >=0 are the possible s_i candidates (since for them, left_i >=0 is required). And the s_j candidates are those with right =-a and left_j >= -a (since a + left_j >=0 → left_j >= -a).

So, the total pairs for a given a is (number of s_i with right = a and left >=0) multiplied by (number of s_j with right =-a and left >=-a).

Thus, the steps are:

- For all strings, compute (left, right) for each.

- For each possible right value a, collect two counts:

   a. the number of strings with right = a and left >=0 (call this count_a).

   b. for each possible a, precompute the number of strings with right = -a and left >= (-a) (call this count_neg_a).

But how to compute this efficiently?

Let's process all the strings first. For each string s, compute left and right. Then, group all strings by their right value. For each group a, we can collect all the left values of those strings. Then, for a group a, the count_a is the number of lefts in the group that are >=0. For the count_neg_a, which is the number of strings with right=-a and left >= -a.

But how to compute count_neg_a? For each a, we need to look into the group of right=-a, and count how many have left >= -a.

So, for each a, the total pairs contributed by this a is count_a * count_neg_a.

But how to handle this for all possible a?

But since a can be up to the maximum possible right value (since each string can have a right value up to its length, which can be up to 3e5 per string, but sum of all lengths is 3e5), but in practice, a can vary a lot.

But since the sum of all right values across all strings can be up to 3e5 (each string can contribute up to O(1) right value), but perhaps we can use a hash map (like a defaultdict) to track for each a, the count of strings with right=a and left >=0, and for each a, the number of strings with right=a and left >=x for any x.

Wait, no. For a given a, when we need to find the number of strings with right=-a and left >=-a, we can look into the group for -a. For each such string in that group, left >=-a.

So, for each group in the dictionary, which is a list of lefts, we can pre-sort them. Then, for a query like how many in this group have left >= x, we can use binary search to find the count.

Yes! So the plan is:

- For all strings, compute (left, right).

- Group the strings by their right value. For each group a, collect all left values, then sort them.

- For each a in the group's keys, calculate count_a (number of lefts in a's group that are >=0).

- Then, for each a, compute the required count_neg_a as the number of lefts in the group for -a that are >= (-a). This can be done using binary search on the sorted list.

- The total pairs is the sum over all a of (count_a * count_neg_a).

But wait, how do we avoid double-counting or missing pairs?

For example, when a=5 and -a=-5, the group a=5 and group -5 are separate. When a=5, we look for group -5 and count the lefts >= -5. Then, when a=-5, we look for group 5 and count the lefts >=5. But in the sum, this would count pairs (a=5, -a=-5) and (a=-5, a=5) separately. However, the problem requires that each pair (i,j) is considered once, even if i and j are from different groups. So perhaps the approach is correct.

Wait, no. Because for a given a, when we compute count_a * count_neg_a, that's for all pairs where s_i has right a and s_j has right -a, and the conditions are met. But when a is negative, the pair (s_i, s_j) where s_i has right a and s_j has right -a is different from when a is positive. So the sum over all a would include both a and -a.

But this would lead to double-counting. For example, a pair (i,j) where s_i has right a and s_j has right -a would be counted once for a, and once for -a. But that's not correct. Because when a is 5, the group for 5 is handled, and the group for -5 is handled. Wait, no. Because when a is 5, the count_neg_a would look into the group for -5. When a is -5, the count_neg_a would look into the group for 5. So each pair (i,j) where i has a and j has -a would be counted once in the a=5 case, and once in the a=-5 case, but those are different pairs.

Wait, no. Let's clarify with an example. Let's say a=5. Then, the count_neg_a would look for j's with right=-5. So the pairs (i,j) where i is in a=5 group and j is in a=-5 group. Then, when a=-5, the count_neg_a would look for j's with right=5. So the pairs (j,i) where j is in a=-5 group and i is in a=5 group. But these are different pairs (i,j) and (j,i), unless i=j. So the sum over all a would count both pairs (i,j) and (j,i) if both conditions are met. But according to the problem statement, each ordered pair (i,j) is considered, even if i and j are the same. So the approach is correct.

So, the code would process all possible a's and sum count_a * count_neg_a for all a. For example, a=5 and a=-5 are considered as separate a's, and contribute to the sum based on their own count_a and count_neg_a.

Therefore, the algorithm is:

1. Preprocess all strings to compute left and right.

2. For each string, group them by their right value. For each group, store a sorted list of left values.

3. For each possible a in the groups:

   a. Compute count_a: the number of strings in the a group with left >=0.

   b. Compute required x for the -a group: x = -a. For the -a group, count_neg_a is the number of strings with left >= x.

   c. Multiply count_a by count_neg_a and add to the total.

But how do we handle a=0? Because for a=0, the required -a is also 0. So for the group a=0, we need to count the number of strings with left >=0 (count_a) and the number of strings in the same group (a=0) with left >=0 (since x = -a = 0). So for a=0, count_neg_a is the count of left >=0 in the same group. Thus, the product would be (count_0) * (count_0), which includes all pairs (i,j) where both are in the a=0 group and satisfy the conditions. Which is correct.

Now, the steps for the code:

Read n.

For each of the next n lines:

   compute left and right.

   add to a dictionary, where the key is right, and the value is a list of lefts.

Then, for each key a in the dictionary:

   required is that the other key is -a.

   if -a is not present in the dictionary, then count_neg_a is 0.

   else, for the -a group, compute how many lefts are >= (-a).

   compute count_a as the number of lefts in a's group >=0.

   add to the total: count_a * count_neg_a.

But how to compute the count_neg_a?

For each group, we can sort the list of lefts. Then, for a given x, the number of elements >=x can be found using binary search.

For example, sorted_list = sorted(lefts). To find how many elements are >= x, we can find the first index where element >=x, and subtract from the length.

So in Python, for a sorted list, we can use bisect_left to find the insertion point of x, then the count is len(sorted_list) - pos.

So, the steps are:

For each group a in the dictionary:

   sort the list of lefts once.

So during preprocessing:

We can create a dictionary (defaultdict) where each key is the right value, and the value is a sorted list of lefts. Wait, no. Because for each group, the list of lefts can be sorted once, and then binary search is possible. So during the grouping, we can collect the lefts in a list, sort it once, and then store the sorted list.

But for efficiency, when building the dictionary, for each string's right, we append the left to the list, and after all strings are processed, sort each list.

So code steps:

from collections import defaultdict

groups = defaultdict(list)

for each string in input:

    compute left, right.

    groups[right].append(left)

Then, for each key in groups:

    sort the list of lefts.

Now, when processing each a in groups, the list for a is sorted.

So, when a group has right = a, and we need to find how many lefts are >= x, we can perform a binary search on the sorted list.

So, for each a in groups:

    sorted_list = groups[a]

    count_neg_a = number of elements in groups[-a] >= (-a)

    to compute this:

        if -a not in groups: count_neg_a = 0

        else:

            target_x = -a

            sorted_neg_a = groups[-a]

            pos = bisect.bisect_left(sorted_neg_a, target_x)

            count_neg_a = len(sorted_neg_a) - pos

    count_a is the number of elements in groups[a] >=0.

        pos_a = bisect.bisect_left(sorted_list, 0)

        count_a = len(sorted_list) - pos_a

    total += count_a * count_neg_a

So this would sum all possible pairs (i,j) where s_i has right a, s_j has right -a, and the conditions are met.

This approach should be O(n log n) for preprocessing (sorting each group's lefts) and O(m log k) for each group, where m is the number of groups and k is the average group size. Since each group's lefts are sorted once, and each query for count_a and count_neg_a is O(log k), this should be efficient enough for n up to 3e5.

Now, let's test this approach against the sample inputs.

First sample:

Input:

3

)

()

(

So the three strings are:

s1: ')', which is ')'

Compute left and right:

For s1:

balance starts at 0.

After first ')', balance is -1. So left is -1, right is -1.

s2: '()'

balance steps: 1, 0.

left is 0, right is 0.

s3: '('

balance steps: 1. left is 1 (since it's the minimum?), wait no. Wait, let's recalculate.

Wait, for each string, compute the balance step by step, track the minimum balance.

For s1: ')'

balance starts at 0. After ')', it's -1. So the min is -1. right is -1.

s2: '()'

balance steps: 0+1=1 (after '('), then 1-1=0 (after ')'). The min is 0. right is 0.

s3: '('

balance is 1. min is 1. right is 1.

So groups:

groups[-1] = [-1]

groups[0] = [0]

groups[1] = [1]

Now, processing each a in groups:

For a=-1:

count_a is number of lefts >=0 in groups[-1]. The lefts are [-1], so 0.

count_neg_a is for a=-1, the required -a is 1. Check group 1. For group 1, lefts are [1]. required x = -a = 1. So count_neg_a is number of lefts >=1 in group1. All 1's are >=1. So 1. So contribution is 0 * 1 = 0.

For a=0:

count_a is number of lefts >=0 in group0. The lefts are [0], so 1. count_neg_a is for -a=0. So check group0. x = 0. So count_neg_a is number of elements in group0 >=0. 1. So contribution is 1 * 1 =1.

For a=1:

count_a is left >=0: group1's lefts are [1], which is >=0. So count_a=1. count_neg_a is for -a=-1. Check group-1. x is 1 (since -a is -1, x = -a =1). So in group-1, lefts are [-1]. So elements >=1? None. So count_neg_a=0. Contribution 1*0=0.

Total sum is 0+1+0=1. But the sample output is 2. Wait, this can't be right. So there's a problem here.

Wait the sample output is 2, but according to this approach, the code would output 1. So where's the mistake?

Ah, the sample input 1:

The output is 2. Let's see what pairs are valid.

In the first sample:

The valid pairs are (3,1) and (2,2).

Let's see:

s3 is '(', right is 1.

s1 is ')', right is -1. So 1 + (-1) =0. So s3 + s1 is '()', which is RBS. So the pair (3,1) is valid.

s2 is '()', right 0. So s2 + s2 is '()()' which is RBS.

But according to the code's approach, when a=0:

count_a is 1 (since left is 0 >=0), count_neg_a is 1 (same group, left >=0). So 1*1=1. So this accounts for (2,2) pair.

When a=1: count_a is 1 (left is 1 >=0). count_neg_a is group-1, x = -a = -1. So group-1's lefts are -1. How many are >=-1? All. So group-1's lefts are [-1], so count_neg_a would be 1 (since x is -1, elements >=-1: 1 element). So a=1's contribution is 1 *1=1. Then total sum would be 0+1+1=2, which is correct.

Wait, but earlier calculation for a=1: group1 has right=1, left=1.

So for a=1, count_neg_a is for group -a = -1. So x is -a = -1. The required left_j >= x (-1). group-1's lefts are [-1]. So elements >=-1: 1. So count_neg_a=1. So contribution is 1*1=1.

Ah, yes! Earlier mistake was in the calculation of x for a=1. x is -a, which is -1. So for group-1's lefts, we need left_j >=-1. The lefts are [-1], which is exactly equal to x. So count_neg_a is 1.

So for a=1, the contribution is 1*1=1. Then, the sum is 0 (a=-1) +1 (a=0) +1 (a=1) =2, which matches the sample output.

So where was the mistake in the earlier analysis? Ah, I think I messed up the calculation for x when a=1. x is -a, which is -1. So left_j >=-1. group-1's lefts are [-1], which are >=-1, so count_neg_a=1. So that's correct.

So the code's approach is correct.

Now, the code needs to be written with this logic.

Now, let's see for the second sample input:

Input:

2

()

()

So each string has right=0, left=0.

The groups:

group0 has two elements, left=0 and left=0. sorted list is [0,0].

For each a in groups (only a=0):

count_a is number of left >=0: 2.

count_neg_a is for a=0, x is 0. group0's lefts are [0,0]. So count_neg_a is 2.

so contribution is 2*2=4. total sum is 4, which matches the sample output.

So code works here.

So the code logic is correct.

Now, implementing this in Python.

First, for each string, compute left and right:

To compute left and right:

Initialize balance =0, left_min =0.

Then, for each character in the string:

   if '(', balance +=1

   else, balance -=1

   left_min = min(left_min, balance)

right is balance after processing all characters.

So for each string:

left = left_min

right = balance

So code for processing each string:

def compute_left_right(s):

    balance = 0

    left_min = 0

    for c in s:

        if c == '(':

            balance +=1

        else:

            balance -=1

        left_min = min(left_min, balance)

    return left_min, balance

But wait, the initial left_min is 0. But after the first step, the balance could be -1 (if first character is ')'). Then left_min would be -1.

Wait, for example, the first string is ')'.

balance starts at 0.

After first character, balance is -1. left_min is min(0, -1) = -1.

So yes, correct.

So the code for each string is:

left_min, right = compute_left_right(s)

Then, group by right.

In Python, using defaultdict(list). Then, after all strings are processed, for each group, sort the list.

Then, for each a in groups:

sorted_list = groups[a]

count_a = len([x for x in sorted_list if x >=0]) → but this is O(n), but since the list is sorted, we can use bisect to find the first index where x >=0.

So for each a in groups:

sorted_list = groups[a]

count_a = bisect.bisect_left(sorted_list, 0) → no, wait. sorted_list is sorted. So to find the first index where x >=0, bisect_left returns the first position to insert 0 in the list, which is the first element >=0.

But wait, the list is sorted in ascending order. So, for example, if the list is [-2, -1, 0, 1], bisect_left for 0 would return index 2. So the number of elements >=0 is len(list) - index.

Yes.

So code:

Testing against sample input 1.

```python
import bisect
from collections import defaultdict


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    groups = defaultdict(list)

    for _ in range(n):

        s = input_stream.readline().rstrip("\n").strip()

        balance = 0

        left_min = 0

        min_balance = 0

        for c in s:

            balance += 1 if c == '(' else -1

            min_balance = min(min_balance, balance)

        # left_min is the minimum balance encountered

        left = min_balance

        right = balance

        groups[right].append(left)

    # Now, sort each group's list of lefts

    for key in groups:

        groups[key].sort()

    total = 0

    for a in groups:

        # count_a is the number of lefts >=0 in group a

        sorted_a = groups[a]

        pos_a = bisect.bisect_left(sorted_a, 0)

        count_a = len(sorted_a) - pos_a

        # find -a group

        required_b = -a

        if required_b not in groups:

            count_b = 0

        else:

            sorted_b = groups[required_b]

            # required x is -a for a's required_b group

            x = required_b

            # Wait, no.

            # For the j strings (right = required_b = -a), the condition is left_j >= (-a)

            # Because right_i is a, right_j is -a. So right_i + left_j = a + left_j >=0 → left_j >= -a.

            # So x is -a.

            x = -a

            # Now, find the number of elements in sorted_b >= x.

            pos_b = bisect.bisect_left(sorted_b, x)

            count_b = len(sorted_b) - pos_b

        total += count_a * count_b

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
()
()
""",
            "output": \
"""\
4
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Another case: a string has right=5 and left=3. Then, it can pair with a string with right=-5 and left >=-5.

So code counts all such pairs.

Another case: when a string's left is negative. For example, s_i's left is -1. Then, count_a is 0, so even if there are j's that could pair, this i is not considered. Which is correct.

So the code should be correct.
</think>

```python
import bisect
from collections import defaultdict

n = int(input())
groups = defaultdict(list)

for _ in range(n):
    s = input().strip()
    balance = 0
    min_balance = 0
    for c in s:
        balance += 1 if c == '(' else -1
        min_balance = min(min_balance, balance)
    left = min_balance
    right = balance
    groups[right].append(left)

# Sort each group's list of left values
for key in groups:
    groups[key].sort()

total = 0

for a in groups:
    sorted_a = groups[a]
    # Calculate count_a: number of elements in a's group with left >= 0
    pos_a = bisect.bisect_left(sorted_a, 0)
    count_a = len(sorted_a) - pos_a
    
    required_b = -a
    count_b = 0
    if required_b in groups:
        sorted_b = groups[required_b]
        x = -a
        pos_b = bisect.bisect_left(sorted_b, x)
        count_b = len(sorted_b) - pos_b
    
    total += count_a * count_b

print(total)
```
