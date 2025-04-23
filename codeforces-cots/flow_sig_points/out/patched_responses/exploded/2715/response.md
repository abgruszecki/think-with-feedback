<think>
Okay, let's see. I need to find the minimum number of x's to remove so that there's no three in a row. Hmm. So the problem is to eliminate any occurrences of "xxx" in the string by deleting as few characters as possible.

Wait, how do I approach this? Let's think. For example, if there's a long sequence of x's, like in the third example, "xxxxxxxxxx" (10 x's). The output is 8. Because after removing 8, we have two x's left. So for a group of m x's in a row, the minimum deletions needed would be max(0, m - 2). Because each group of x's can't have more than two. So any group longer than two x's needs to have (m-2) x's removed. But wait, maybe there are overlapping sequences? Like, maybe the way the x's are arranged in the string could lead to overlapping triplets. But I think the approach is to process the string and track consecutive x's. Whenever there's a run of x's longer than 2, count how many need to be removed.

So the plan is:

1. Iterate through the string and find all consecutive sequences of 'x's.
2. For each such sequence, if its length is >=3, add (length - 2) to the total deletions.
3. Sum all these deletions across the entire string.

Wait, but how about overlapping groups? Let me think. For example, a string like "xxxx". It has two overlapping triplets: positions 0-2, 1-3. But if we process the entire sequence of four x's as a single group, the required deletions would be 4-2=2. Which is correct because after removing two x's, only two remain. So that's the right approach.

So the steps would be:

- Initialize a counter for the current x streak.
- Traverse each character in the string.
- Whenever we hit an 'x', increment the current streak.
- When we hit a non-'x' character, check the current streak. If it's >=3, add (streak - 2) to the result. Then reset the streak to 0.
- After processing the entire string, check the last streak (in case the string ends with x's).

Yes, that makes sense. So for each consecutive group of x's, the number of deletions is the max(0, len(group) - 2). Sum all those up.

So the implementation would be straightforward. Let's test this logic against the examples.

First example: "xxxiii" has a group of 3 x's. So 3-2=1. Output is 1. Correct.

Second example: "xxoxx" has two groups of 2 x's each. So 2-2=0 for both. Sum is 0. Correct.

Third example: 10 x's. 10-2=8. Correct.

What about a case with multiple groups? Like "xxxxxxoooxx". The first group is 6 x's → 6-2=4, then a group of 3 o's (but not x's, so ignored), then 2 x's → 0. Total 4. So the answer would be 4. Which is correct.

So this logic should work.

So the algorithm is O(n) time, which is acceptable for n up to 100. So the code can process this efficiently.

Now, let's code this in Python.

The steps in code:

Read n, then the string.

Initialize current_x = 0, deletions =0.

Loop over each char in the string:

if char is 'x', current_x +=1

else:

   if current_x >=3:

       deletions += current_x -2

   current_x =0

After the loop, check if current_x >=3 and add to deletions.

Then print deletions.

Yes. Let's code this.

Testing the examples:

Sample 1: input is 6, 'xxxiii'

Loop:

First three chars are 'x's. current_x becomes 3.

Then next char is 'i'. current_x is 3 >=3: deletions +=1. current_x resets. Then other 'i's do nothing. Then the last three 'i's. So total is 1. Correct.

Sample 2: 'xxoxx' → groups of 2, 2. So no deletions. Output 0.

Sample3: 10 x's. current_x is 10. After loop, check again: 10-2=8. Output 8.

Looks good.

So the code should handle all cases.
</think>

```python
n = int(input())
s = input().strip()

current_x = 0
deletions = 0

for char in s:
    if char == 'x':
        current_x += 1
    else:
        if current_x >= 3:
            deletions += current_x - 2
        current_x = 0
# Check the last group of x's
if current_x >= 3:
    deletions += current_x - 2

print(deletions)
```