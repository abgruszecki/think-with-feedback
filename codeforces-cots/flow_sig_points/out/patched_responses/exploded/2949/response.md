<think>
Okay, let's see. The problem is about Valera needing four horseshoes of different colors. He already has four, but some might be the same. We need to find out the minimum number he needs to buy so that all four are unique.

Hmm. So the approach here is to count how many duplicates there are in the original four. Then, based on that, determine how many to replace.

Wait, but how exactly? Let's think. For example, if all four are the same color (like the second test case), he needs to replace three of them. Because each new one must be unique. So in that case, he needs to buy 3.

Another example: the first input is 1,7,3,3. So there are two 3's. So he has three unique colors. He needs to replace one of the 3's. So he needs to buy one.

So the problem reduces to finding the number of duplicates and then calculating how many replacements are needed.

But how to compute the number of duplicates. Let's think: the number of required new horseshoes is equal to (number of duplicates) such that after replacement, all are unique.

Wait, maybe the formula is based on the number of duplicates. Let's see. The count of each color. For example, if there are two colors appearing twice each (like 1,1,2,2), then Valera has four shoes but two pairs. He needs to replace two of them. So in that case, he needs to buy two. Because each duplicate in the pairs must be replaced. So how?

Alternatively, the minimum number of shoes to buy is equal to (total duplicates) minus some. Wait, maybe not. Let's think in terms of frequency counts.

Let's count the frequency of each color in the four horseshoes. For instance, in the first example:

1: 1 occurrence
7: 1
3: 2 occurrences

So frequencies are [2,1,1]. The sum of frequencies is 4.

The number of duplicates is 2 (since the 3 appears twice). But how to model the required number of replacements.

Wait, perhaps the minimal number of shoes to buy is equal to (sum of (frequency - 1) for all frequencies) minus ... no, wait. Let's see. For each color that appears more than once, we need to replace (count - 1) shoes. For example, if a color appears 3 times, then we have to replace 2 of them. Because we can keep one, and replace the other two. Similarly, if a color appears 4 times (like all 7s in the second example), we need to replace 3 of them.

So the total number of required replacements is the sum of (count - 1) for each color.

Wait, let's test this.

First example: 3 appears twice. So (2-1) =1. Sum is 1. Which matches the output of 1.

Second example: 7 appears four times. (4-1) =3. Sum is 3. Output is 3.

Another test case: two pairs (like 1,1,2,2). Then each pair contributes (2-1) =1. Sum is 1+1=2. So the answer should be 2. For example, input 1 1 2 2 → output 2. Correct, because he needs to replace two of them.

Another test case: three same and one different. Like 1,1,1,2. Then the sum is (3-1) =2. So answer is 2. Which makes sense. Because he has to replace two of the three 1s. Then he has 1,2, plus two new colors.

So the formula seems to be sum (count_i -1) for each color in the frequency map.

So the approach is:

1. Count the frequencies of each color in the input list.
2. For each frequency, subtract 1 and sum all those values. That sum is the minimal number of horseshoes to buy.

So the steps are:

- Take the four input numbers.
- Create a frequency dictionary (like using a Counter in Python).
- For each value in the Counter's values, subtract 1 and sum all those.
- The result is the answer.

Yes, that makes sense. So the code can be written as:

Read the four numbers as a list.

Use collections.Counter to count frequencies.

Then sum (count -1 for each count in the Counter's values).

But wait, the sum of (count -1) for all elements is exactly the number of duplicates. Because for each element, if it's present once, it contributes 0. For example, in the first example, 3 appears twice: contributes 1. Others contribute 0. Sum is 1.

Yes. So this sum is the answer.

So the code can be:

import sys
from collections import Counter

shoes = list(map(int, sys.stdin.readline().split()))
freq = Counter(shoes)
total = sum(v-1 for v in freq.values())
print(total)

Wait, but let's test this with some examples.

Test case 1: 1 7 3 3 → Counter has counts {1:1,7:1,3:2} → sum (0+0+1) =1 → correct.

Test case 2: 7 7 7 7 → sum(3) → 3 → correct.

Another test case: 1 1 2 2 → sum(1+1) =2 → correct.

Another test case: 1 1 1 2 → sum(2 +0) =2 → correct.

Another test case: 1 2 3 4 → sum(0 for all) → 0 → correct.

Yes, this seems to work.

So the code is straightforward. The optimal approach is O(1) time and space, because there are only four elements. So even for the maximum constraints, which are 1e9 for the colors, but the code doesn't care about the actual values, only the counts.

So the data structure used is a Counter, which for four elements is trivial.

Thus, the solution is to count the frequency of each color and sum (count-1) for each, which gives the number of duplicates that need to be replaced.
</think>

```python
from collections import Counter
import sys

shoes = list(map(int, sys.stdin.readline().split()))
counts = Counter(shoes)
print(sum(v - 1 for v in counts.values()))
```