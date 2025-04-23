<think>
Okay, I need to find the smallest positive integer that has at least one digit from the first list and at least one from the second. Hmm. Let's think about how to approach this.

First, the simplest cases. Like if there's a digit that's in both lists. Then the smallest number is that single digit. For example, if the first list has 1 and the second has 1, then 1 is the answer. Because it's the smallest possible, and it meets both conditions.

So the first step is to check if there's any common elements between the two lists. If yes, then the answer is the minimum of those common elements. That's because a single-digit number is the smallest possible, and if there's a digit that's present in both, then that's the answer.

If there's no common digit, then the next step is to look for two-digit numbers. Because two digits would be the next smallest possible. So we need to find the smallest possible combination where one digit is from the first list and the other is from the second. But the order matters here. For example, 25 is smaller than 52. So the two-digit number could be the combination of the smallest a and the smallest b, but arranged with the smaller first. Wait, no. Wait, let's see: suppose a has 2 and 4, b has 5,7,6. Then the possible two-digit numbers are 25, 27, 26, 45,47,46, 52,54,72,74,62,64. Wait, but in the first example, the answer was 25. Which is indeed the minimal combination where a digit from the first list and a digit from the second are present. So the two-digit numbers can have a from first list and then from second, or vice versa. Wait, but the first example's output is 25. Let's see: the first list is [4,2], second [5,7,6]. The possible two-digit numbers where one is from a and one from b would be 25 (2 from a, 5 from b) which is 25. That's the smallest possible. So the approach here would be to take the minimal digits from each list and combine them in both possible orders (like min_a and min_b, then min_b and min_a) and pick the smaller of those two.

Wait, but what's the minimal possible two-digit number here? For example, if the minimal a is 2 and minimal b is 5, then 25 and 52. The smaller is 25. So the minimal two-digit number would be the combination of the smallest a and smallest b, but ordered such that the first digit is the smaller between a and b. Wait no. Wait, if the a's min is 2 and b's min is 5, then 25 is smaller than 52. So the minimal two-digit combination would be min_a followed by min_b. But what if the min of a is higher than the min of b? Like a has min 3, b has min 2. Then the possible two-digit numbers are 32 and 23. The smaller is 23. So in that case, the correct approach is to take min_b as first digit and min_a as second, but wait no. Wait, in this case, the first digit is 2 (from b's list), second digit is 3 (from a's list). So the number is 23. Which is smaller than 32. So the minimal two-digit number is the smallest possible combination where each digit comes from the respective list. But how do we compute that?

So the minimal two-digit number would be the minimum between all possible combinations where one digit is from a and the other from b. So for each digit in a, and each digit in b, create numbers by combining them in both possible orders (like a's digit first, then b's; and b's digit first, then a's). Then find the minimal among all these possibilities.

Wait, but that's a lot of possibilities. For example, if a has m digits and b has n digits, then for two-digit numbers, the total possibilities are m * n * 2 (each pair in both orders). But since m and n can be up to 9 each, that's 9*9*2=162 possibilities. Which is manageable. So for the two-digit case, we can generate all possible two-digit numbers where one digit is from a and the other from b, then take the minimum of those.

Alternatively, perhaps there's a smarter way. For example, find the smallest possible a (min_a) and the smallest possible b (min_b). Then the two possible combinations are min_a followed by min_b, and min_b followed by min_a. The minimum of these two would be the minimal two-digit number. But is that correct?

Let's test this approach. Suppose a has digits 3 and 2. B has digits 1 and 4. Then min_a is 2, min_b is 1. The possible combinations are 21 and 12. The minimal is 12. Which is correct, but according to the approach, the two options would be 21 and 12, so the minimal is 12. So yes, that approach would give the correct result.

Another example: a has digits 5 and 1. B has digits 3 and 2. Then min_a is 1, min_b is 2. The combinations are 12 and 21. The minimal is 12. But in this case, 12 is the correct answer because it's a two-digit number with a digit from a and a digit from b.

But what if there's a combination of a higher a and lower b that gives a smaller number? For example, a has digits 3 and 5. B has digits 2 and 4. Then min_a is 3, min_b is 2. The combinations are 32 and 23. The minimal is 23. But perhaps there's another pair like 5 and 2, which would be 52 and 25. 23 is better. Wait, no. Wait in this example, the min a is 3, min b is 2. So 32 and 23. The minimal is 23. So the approach of considering min_a and min_b gives the correct result.

But what if a has digits 4 and 2, and b has digits 5,7,6. Then min_a is 2, min_b is5. The combinations are 25 and 52. The minimal is 25. Which is correct as per the first example.

So the approach would be:

1. Check if there's any common digit between a and b. If yes, the answer is the minimal such digit.

2. Else, generate all possible two-digit numbers where one digit is from a and the other from b, in any order. Find the minimal among these.

So, the algorithm is:

- Find the intersection of the two lists. If not empty, return the min of the intersection.

- Else, find the minimal a (min_a) and minimal b (min_b). Then the possible candidates are min_a followed by min_b, and min_b followed by min_a. The answer is the minimum of these two.

Wait, but wait. Could there be a two-digit number that is even smaller than those two? Like, maybe there's a combination where a different a and b gives a smaller number. For example, if a has 2 and 9, and b has 3 and 4. Then min_a is 2, min_b is 3. So 23 and 32. The minimal is 23. But if there is a combination like 3 (from b) and 2 (from a), which would be 32. So 23 is indeed the smallest. So the approach seems to hold.

But what if a has digits 2 and 1, and b has digits 3 and 0. Wait, but according to the problem statement, the lists contain non-zero digits, so 0 can't be in the input. So the digits are from 1-9.

So the approach is correct. Therefore, the steps are:

1. Check for any common digits. If present, return the smallest one.

2. Else, the answer is the minimum between (min_a * 10 + min_b) and (min_b * 10 + min_a).

Wait, no. Because the digits in a are from the first list, and digits in b are from the second. So in a two-digit number, one digit must be from a and one from b. So for example, the first digit could be from a and the second from b, or the first from b and the second from a.

Thus, the minimal two-digit number is the minimal among all possible combinations where one digit is from a and the other from b, in either order.

But generating all possible combinations and taking the minimal is feasible.

But considering that for each a in list_a and each b in list_b, there are two possibilities: a followed by b, and b followed by a.

So the minimal two-digit number is the minimum of all possible such numbers.

So for example, if a is [4,2], b is [5,7,6], then the possible two-digit combinations are:

4 followed by 5,7,6 → 45,47,46.

2 followed by 5,7,6 → 25,27,26.

5 followed by 4,2 → 54,52.

7 followed by 4,2 → 74,72.

6 followed by 4,2 → 64,62.

So the numbers are 45,47,46,25,27,26,54,52,74,72,64,62. The minimal here is 25. Which matches the first example.

But generating all possible two-digit numbers would require checking all a in list_a and b in list_b for both orders.

Alternatively, the minimal two-digit number can be found by:

min_ab = min(a) * 10 + min(b)

min_ba = min(b) * 10 + min(a)

the minimal of these two.

Wait, in the first example, min(a) is 2, min(b) is 5. So min_ab is 25, min_ba is 52. The minimal is 25. Which is correct.

In the second example, the first list has 1, and the second list also has 1, so the answer is 1.

Another example: suppose a is [3, 1], b is [2,4]. The common digits? None. So min_ab is 12, min_ba is 21. The minimal is 12. But there's also combinations like 14 (1 from a, 4 from b) which is 14. Wait, 14 is 14, which is higher than 12. So the minimal is 12.

But if a is [1, 3], b is [2,5]. Then the possible two-digit numbers are 12,15, 32,35, 21,23,51,53. The minimal is 12. Which is indeed min_ab (1*10 + 2=12). So that approach would work.

Wait another case: a is [1, 9], b is [3, 2]. Then the possible two-digit numbers are 13,12,93,92, 31,21,39,29. The minimal is 12 (from 1 followed by 2). So min_ab (1 and 2 →12), min_ba (2 and1 →21). So the minimal is 12.

But if a is [2, 1], b is [3, 0] (but 0 is not allowed). So in a case where a has min 1, b has min 2, the minimal is 12.

So it seems that the approach of taking the minimum between (min_a followed by min_b) and (min_b followed by min_a) gives the correct minimal two-digit number.

But why is that the case? Because among all possible combinations, the minimal a and minimal b would form the minimal two-digit number when ordered correctly. Because any other combination would have a higher digit in one of the positions.

So, perhaps, the minimal two-digit number is the minimum between (min_a *10 + min_b) and (min_b *10 + min_a).

Thus, the steps are:

Check if there's a common digit. If yes, return the smallest common digit.

Else, compute the minimal a and minimal b, then return the minimum between the two possible two-digit numbers.

That's O(1) time once you have the common digits and the minima.

So how do we implement this?

First, read n and m.

Then read the two lists. For the first list, we can store as a set for O(1) lookups. Same for the second list.

Then compute the intersection of the two sets. If not empty, the answer is the min of the intersection.

Else, find min_a (min of list_a) and min_b (min of list_b).

Then compute the two possibilities: min_a *10 + min_b, and min_b *10 + min_a. The answer is the minimum of these two.

Yes, this seems correct.

So code steps:

Read n and m.

Read list_a as a list of integers. Then read list_b as a list of integers.

Convert both to sets.

common = set_a & set_b. If common exists, then the answer is min(common).

Else, compute min_a and min_b.

Compute candidate1 = min_a *10 + min_b

candidate2 = min_b *10 + min_a

the answer is min(candidate1, candidate2).

So code:

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

set_a = set(a)
set_b = set(b)

common = set_a & set_b
if common:
    print(min(common))
else:
    min_a = min(a)
    min_b = min(b)
    candidate1 = min_a * 10 + min_b
    candidate2 = min_b * 10 + min_a
    print(min(candidate1, candidate2))

But wait, what if the two-digit numbers have a leading zero? But according to the problem statement, all digits are non-zero, so that's not possible. Because the input lists contain non-zero digits. So min_a and min_b are at least 1. So the two-digit numbers can't have leading zeros.

Yes, because in the input, all digits are from 1 to 9.

So this code should work.

Testing the first example:

Input:

2 3

4 2

5 7 6

common is empty. min_a is 2, min_b is5. candidate1=25, candidate2=52. min is 25. Correct.

Second example:

8 8

1 2 3 4 5 6 7 8

8 7 6 5 4 3 2 1

common is {1,2,3,4,5,6,7,8}. So min is 1. Correct.

Another test case where there's no common elements, but the minimal two-digit is the second candidate.

Like:

a is [3], b is [2].

common is empty. min_a=3, min_b=2.

candidate1=32, candidate2=23. So the answer is 23.

Another case: a is [9,5], b is [1,4]. common is empty. min_a=5, min_b=1. candidate1=51, candidate2=15. min is15.

So code would output 15.

Yes.

Thus, the code should handle all cases correctly.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
set_a = set(a)
set_b = set(b)
common = set_a & set_b
if common:
    print(min(common))
else:
    min_a = min(a)
    min_b = min(b)
    print(min(min_a * 10 + min_b, min_b * 10 + min_a))
```