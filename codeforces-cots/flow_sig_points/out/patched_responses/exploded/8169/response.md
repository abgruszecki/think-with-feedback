<think>
Okay, let's see. The problem is that Limak has five cards with numbers, and he can discard some cards. But he can only do this once: he can discard either two or three cards that all have the same number. And the goal is to find the minimum possible sum of the remaining cards.

So the first thing I need to do is figure out for each possible number on the cards, how many times it appears. Because if a number appears two or three times, maybe we can remove those. Or if it appears four or five times, then we can choose to remove two or three of them, whichever gives a better result.

Wait, right. For example, if a number appears four times, then we could choose to remove three of them (since that's allowed as a single operation), which would remove more from the sum than removing two. But the problem says "at most once discard two or three cards with the same number". So if there's a number that occurs four times, then the maximum we can remove is either three (if possible) or two, but we can only perform one operation. So for a number that occurs four times, the best option is to remove three instances, which would leave one. That's better than removing two, which leaves two, contributing more to the sum.

So the approach here is: for each possible number in the cards, check the counts. For each number, compute how much we can subtract from the total sum if we remove either two or three of them (depending on the count), and then choose the maximum possible subtraction (since that would leave the minimal sum).

Wait, but how? Let's think.

The total sum is the sum of all five cards. The minimal remaining sum is total_sum minus the maximum possible deduction we can get by removing 2 or 3 cards of the same number, where the deduction is the number multiplied by the number of cards removed (either 2 or 3, whichever is allowed and gives a higher deduction).

So the steps are:

1. Compute the total sum of all five cards.
2. For each distinct number in the cards, check how many times it occurs.
3. For each such count, determine the maximum possible deduction: if the count is >=2, then possible deductions are (number * 2) or (number * 3 if count >=3). We can take the maximum of these possibilities. For example, if a number occurs 4 times, then we can remove 3 of them (since 3 <=4), which would give a deduction of 3*number. That's better than 2*number.
4. The maximum deduction across all possible numbers and their possible 2 or 3 removals is the best option. If there are no such possible deductions (like all numbers are unique), then the deduction is zero.
5. The minimal sum is total_sum - maximum_deduction.

So the key is to find, for each number, the maximum possible deduction allowed by the rules.

Let's take examples.

First example: 7,3,7,3,20. The counts are 7:2, 3:2, 20:1. For 7, deduction can be 2*7=14. For 3, deduction is 2*3=6. So the maximum is 14. So total sum is 7+3+7+3+20 =40. 40-14=26, which matches the example.

Third example: all 10s. Count is 5. So for each 10, possible deductions are 2*10=20 or 3*10=30. Since we can remove three (as count 5 >=3), so deduction is 30. So total is 50. 50-30=20. Correct.

Second example: all unique. So no deductions. Sum is sum of all, which is 28.

Another example: numbers 2,2,2,2,5. The counts for 2 are 4. So possible deductions are 2*2=4 or 3*2=6. We can choose to deduct 6 (since 3 is allowed as count is 4 >=3). So total sum is 2*4 +5 =13. 13-6=7.

So the plan is:

- Count the frequency of each number.
- For each number and its frequency, compute the maximum possible deduction (which is max between (if count >=2: 2*num, and if count >=3: 3*num)).
- Take the maximum deduction from all possible numbers.
- The answer is total_sum - max_deduction.

But wait, what if a number has frequency higher than 3? Like 4 or 5. For example, a frequency of 4. Then, for that number, possible deductions are 2*num or 3*num. Which is larger? 3*num is better. So for a number with count >=3, the maximum possible deduction is max(2*num, 3*num). But since 3 is larger than 2, if count >=3, then 3*num is better. So for any count >=3, the deduction is 3*num. For count 2, it's 2*num.

Wait, but if a number occurs 4 times, you can't remove all 4. You can only remove 2 or 3 once. So for a count of 4, the maximum possible is 3*num. Because 3 is allowed (since count >=3). Similarly, for count 5: you can remove 3, which is allowed, giving 3*num.

So the maximum deduction for a number with frequency c is:

if c >=3: 3 * num

else if c >=2: 2 * num

else: 0.

So for each number, the possible deduction is:

max_possible = 0

if count >=2:

   possible = 2 * num

if count >=3:

   possible = max(possible, 3 * num)

so the maximum between 2 and 3, but only if count allows.

So for a count of 4, possible is 3 * num (since count >=3).

Thus, the algorithm steps:

1. Calculate the total sum.

2. Create a frequency dictionary (counts for each number).

3. For each number in counts:

   a. current_count = counts[number]

   b. possible_deduction = 0

   c. if current_count >= 2:

      possible_deduction = 2 * number

   d. if current_count >=3:

      possible_deduction = max(possible_deduction, 3 * number)

   e. keep track of the maximum possible_deduction across all numbers.

4. The answer is total_sum - max_possible_deduction.

If there are no numbers with count >=2, then max_deduction is 0, so sum remains.

So the code can be written as:

Read the five numbers.

Compute total sum.

Compute a frequency dictionary (using collections.Counter, perhaps).

For each number in the Counter:

   get count.

   compute possible deduction as described.

   keep track of maximum.

Then subtract the maximum deduction from the total sum.

Now, let's test this approach against the examples.

First example:

Numbers are [7,3,7,3,20]

sum is 7+3+7+3+20 = 40.

counts:

7:2, 3:2, 20:1.

For 7: count is 2. possible is 14.

For 3: count is 2. possible is 6.

For 20: no.

Max deduction is 14. 40-14=26. Correct.

Third example:

All 10s. counts 10:5.

For 10: count >=3, possible is 3*10=30. So total sum is 50, 50-30=20. Correct.

Second example: numbers are all unique. So counts are 1 for each. No possible deductions. sum remains 28. Correct.

Another test case: [2,2,2,2,5]. Count for 2 is 4. possible is 3*2=6. sum is 2*4 +5=13. 13-6=7.

Another case: [5,5,5,5,5]. Count is 5. possible deduction is 3*5=15. sum is 25. 25-15=10.

Another case: [4,4,4,4,4]. possible deduction is 3*4=12. sum is 20. 20-12=8.

So code should handle that.

Now, how to implement this in Python?

We can read the five integers, sum them.

Use a Counter to get the counts.

Initialize max_deduction as 0.

Loop through each number and its count in the Counter.

For each, compute possible deduction:

if count >= 2:

   ded_2 = 2 * num

else:

   ded_2 = 0

if count >=3:

   ded_3 = 3 * num

else:

   ded_3 = 0

current_ded = max(ded_2, ded_3)

if current_ded > max_deduction:

   update max_deduction.

Finally, total_sum - max_deduction is the answer.

Wait, but in code, the steps could be:

for num, cnt in counts.items():

    possible = 0

    if cnt >=2:

        possible = 2 * num

        if cnt >=3:

            possible = max(possible, 3*num)

    max_deduction = max(max_deduction, possible)

Yes.

Alternatively:

for each number, possible is the maximum of (2 * num if cnt >=2 else 0, 3 * num if cnt >=3 else 0).

But in code, for each number and count:

if count >=2:

   temp = 2 * num

   if count >=3:

       temp = max(temp, 3*num)

   max_deduction = max(max_deduction, temp)

else:

   continue (no contribution)

So, code:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    cards = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = sum(cards)
    from collections import Counter
    counts = Counter(cards)

    max_deduction = 0

    for num, cnt in counts.items():
        if cnt >=2:
            current = 2 * num
            if cnt >=3:
                current = max(current, 3 * num)
            if current > max_deduction:
                max_deduction = current

    result = total - max_deduction
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 10 10 10 10
""",
            "output": \
"""\
20
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

Another test case: 2,2,2,2,5.

counts 2:4. For this, current starts as 4 (2*2), then since cnt >=3, compare to 6 (3*2). current is 6. So max_deduction is 6. sum is 2*4 +5=13. 13-6=7.

Yes.

So code seems correct.
</think>

```python
cards = list(map(int, input().split()))
total = sum(cards)
from collections import Counter

counts = Counter(cards)
max_deduction = 0

for num, cnt in counts.items():
    if cnt >= 2:
        current = 2 * num
        if cnt >= 3:
            current = max(current, 3 * num)
        if current > max_deduction:
            max_deduction = current

print(total - max_deduction)
```
