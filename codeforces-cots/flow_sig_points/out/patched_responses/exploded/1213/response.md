<think>
Okay, let's tackle this problem. The problem is about calculating the number of possible second cards that, when combined with the queen of spades, gives exactly n points. The queen of spades is already taken, so we need to exclude that card from the possible choices for the second card.

First, I need to understand how the points work. The queen of spades is worth 10 points. So the second card must contribute (n - 10) points. Let's call that required value 'k'. So k = n - 10.

But wait, there's a catch. If the second card is an ace, it can be counted as 1 or 11. So for the ace, we need to check if either 1 or 11 can make the sum equal to n. Wait, but in this problem, the sum is determined by the player's choice. So, if the sum of the queen (10) plus the second card's possible value (either 1 or 11 for an ace) equals n, then the ace is a valid option.

So the approach is: for each possible card (excluding the queen of spades already taken), check if any of its possible values (if it's an ace) can sum up to n. If yes, then count this card as a valid option. Otherwise, not.

Let's break this down.

The queen of spades is already taken, so the second card cannot be the queen of spades. All other cards are available except that one.

So first, calculate the target value that the second card needs to contribute. The queen is 10 points, so the sum is 10 + value of second card (with aces being flexible).

So for the second card, possible scenarios:

If the card is a 2-10: contributes exactly its face value. So for these, the required value is (n - 10). So if k is 2, then any 2 would work. But wait, for 2-10, the card's point is exactly its number. So for those, the second card's value must be exactly (n-10).

If the card is a Jack, King, or Queen: each contributes 10 points. So their contribution is 10. So the total sum would be 10 + 10 = 20. So if n is 20, these cards (excluding the queen of spades) are valid.

If the card is an Ace: it can contribute 1 or 11. So for an ace to be a valid choice, either 10 + 1 = n or 10 + 11 = n. So check if n is either 11 or 21.

So the steps are:

1. Calculate k = n - 10. For non-ace cards, the required value is k. For aces, check if 1 or 11 can contribute to sum n.

2. Determine all possible cards (excluding queen of spades) that can contribute the required points.

3. Count the number of such cards.

Now, let's think about all possible cases.

First, the possible values for the second card:

Possible cards and their point contributions:

- 2: 2 points
- 3: 3
- ...
- 10: 10
- Jack: 10
- Queen: 10 (but queen of spades is already used)
- King: 10
- Ace: 1 or 11

So for each card type, we need to check if their possible points can contribute to the sum n.

So for non-ace cards:

- For 2-10: if their value is k = n -10, then they are valid.
- For Jack, King, and Queen (not spades): if 10 (their contribution) equals k. But the queen of spades is already taken, so other queens are allowed if they meet the condition.

For Ace: check if either 1 or 11 makes the sum 10+1=11 or 10+11=21. So if n is 11 or 21, then aces are valid.

So let's formalize:

Let's compute for each possible second card type:

Case 1: The card is not an Ace and not a Queen (but Queen of spades is already taken). So:

- For 2-10, check if their value equals k.
- For Jack, King, Queen (other suits), check if 10 equals k.

Case 2: The card is a Queen. But queen of spades is already taken, so other queens (hearts, diamonds, clubs) are possible. Each of those queens contributes 10 points. So if k is 10, then each of these three queens would count.

Case 3: The card is a Jack or King. They contribute 10. So same as case 2 for queens.

Case 4: The card is an Ace. Check if 1 or 11 can make the sum. So if n is 11 (10+1) or 21 (10+11), then the ace counts. Each ace (4 in total) would contribute once per possible condition. Wait, no: each ace is a single card. So for example, if n is 11, then each ace can be used as 1, so the sum is 11. If n is 21, then each ace can be used as 11. If n is both 11 and 21 (which can't happen since 11+10=21?), but n can't be two values. So for a given n, the ace is counted if either 1 or 11 is valid. So for each ace, if (10 + 1) =n or (10 +11) =n, then the ace is counted once.

So the steps:

Calculate k = n -10.

Then, for each possible card:

Check if the card's possible contribution can be k (for non-Ace) or if the sum can be n (for Ace).

So let's proceed:

First, the queen of spades is already taken. So when considering queens, we have 3 queens left (hearts, diamonds, clubs).

For other cards:

Total counts:

- 2: 4 suits → 4 cards
- 3: 4 → 4
- ...
- 10: 4 →4
- Jack: 4 suits →4 cards
- King:4 →4
- Queen: 3 (since queen of spades is already used)
- Ace:4 →4

Now, for each of these, we need to see if they contribute to the sum.

So for each possible card type:

Check if their points can contribute to the sum being n.

Let's think of all possible card types and their counts:

Let's structure this:

For non-Ace, non-Queen cards:

If the card's value (as per points) is equal to (n - 10), then the number of such cards is:

- For 2-10: if (n-10) is between 2 and 10, then 4 cards (each suit)
- For Jack, King: if (n-10) is 10 → since they contribute 10 points. So if n is 20, then (n-10)=10. So Jacks (4) and Kings (4) contribute. Plus the other queens (3) as they also contribute 10. So for n=20, 4+4+3=11, plus queens? Wait, no. Wait, for example, in n=20, the required k is 10. So any card that contributes 10 points would count. So Jacks (4), Kings (4), Queens (other 3), 10s (but 10's value is 10, so if k=10, then 10s would also contribute. Wait wait, this depends on what the required k is. Let's see.

Wait, for a card that is a 10, it contributes 10 points. So if k is 10 (n=20), then all 10s (4) would count. Similarly, Jacks (4), Kings (4), other Queens (3). So for k=10, total cards would be 4 (10s) +4 (Jacks) +4 (Kings) +3 (Queens) = 15. Which matches the second example. So in that example, the output is 15.

So for non-Ace cards:

If their point value is equal to k, then add their count.

For example, for k=2 (n=12), the card must be a 2. There are 4 2s. So output is 4. Which matches the first example.

Now, for Ace cards:

Each Ace can contribute either 1 or 11 points. So the sum after adding the queen's 10 points would be 11 or 21. So for the Ace to be a valid second card, n must be 11 or 21. So:

If n is 11: each Ace (4) is valid (since 10+1=11)
If n is 21: each Ace is valid (since 10+11=21)
Otherwise, Aces are not valid.

So the number of Aces contributing is 4 if n is 11 or 21, else 0.

So putting it all together:

Total ways = (number of non-Ace, non-Queen cards that contribute k points) + (number of Queens that contribute k points) + (number of Aces if applicable).

Wait, but Queen of spades is already taken, so other Queens are considered in their own category. For example, the Queens (other 3) contribute 10 points. So when k=10, they are counted.

So the steps to compute:

1. Compute k = n -10.

2. Count the number of non-Ace, non-Queen cards that have point value equal to k.

   - For 2-10: if k is between 2 and 10, then 4 * (if card's value is k)
   Wait, for example, if k=5, then all 5s (4) contribute.

   So for 2-10: if k is in 2-10, then 4 cards.

   For Jack: if k=10, add 4.

   For King: same as Jack.

   So non-Queen, non-Ace cards: their counts are:

   if the card is a 2-10 and k is the same as the value → 4 each.

   if the card is Jack or King and k=10 →4 each.

3. Count the number of Queens (other than spades) that contribute. Since they are 3 in total, and each contributes 10 points. So if k=10, then add 3.

4. Count the number of Aces: if n is 11 or 21 → 4 each. Else 0.

So combining all these:

Let's compute each part.

First, calculate k = n -10.

For non-Ace, non-Queen cards:

sum_non_ace_non_queen = 0

if 2 <= k <=10:

   sum_non_ace_non_queen += 4 * (number of card types that have point value k in 2-10, which is 1 if k is in that range, 0 otherwise) → wait, for example, if k is 5, then it's 4 (cards of 5). So sum_non_ace_non_queen +=4.

if k ==10:

   sum_non_ace_non_queen +=4 (Jacks) +4 (Kings) → total 8.

Wait, no: Jacks and Kings each contribute 10 points. So for k=10, their contributions are 10. So when k is 10, each of them is counted. So for Jacks and Kings, if k=10, add 4 each.

So the code could be:

sum_non_ace_non_queen = 0

if 2 <= k <=10:

   sum_non_ace_non_queen +=4  # for 2-10 of that value

if k ==10:

   sum_non_ace_non_queen +=4 +4  # jacks and kings

Then, sum_queen = 3 if k ==10 else 0.

sum_ace = 4 if (n == 11 or n ==21) else 0.

Total = sum_non_ace_non_queen + sum_queen + sum_ace.

Wait, let's test this with the examples.

First example: input 12 → n=12. So k=2.

sum_non_ace_non_queen: 2 is in 2-10 → 4. sum_queen is 0. sum_ace: n is 12, not 11 or 21 →0. So total 4.

Which matches the first sample.

Second example: input 20 →k=10.

sum_non_ace_non_queen: 4 (for 10s) + 4 (Jacks) +4 (Kings) → wait wait. Wait, no:

Wait, for k=10, the 2-10 part is if k is between 2 and 10. So yes, 10 is in that range. So sum_non_ace_non_queen for 2-10 is 4 (the 10s). Then, since k=10, add 4 (Jacks) +4 (Kings). So sum_non_ace_non_queen is 4 +4+4=12. sum_queen is 3 (since k=10). sum_ace is 0. So total 12+3=15, which matches the second sample.

Third example: input 10 →k=0. sum_non_ace_non_queen: 0. sum_queen:0. sum_ace:0. So total 0.

Another test case: n=21 →k=11. So sum_non_ace_non_queen: since k=11 is not in 2-10, that part is 0. Jacks and kings contribute only if k=10, so no. sum_queen is 0. sum_ace is 4. So total 4.

Another test case: n=11. k=1. sum_non_ace_non_queen: 0. sum_queen:0. sum_ace:4. total 4.

Another test case: n=20. As before.

So the code would be structured as follows:

Read n.

Compute k = n -10.

sum_non_ace_non_queen = 0

if 2 <= k <=10:

   sum_non_ace_non_queen +=4  # for the 2-10 of value k.

if k ==10:

   sum_non_ace_non_queen +=4 +4  # jacks and kings

sum_queen = 3 if k ==10 else 0

sum_ace =4 if (n == 11 or n ==21) else 0

total = sum_non_ace_non_queen + sum_queen + sum_ace

print(total)

Wait, but wait: in the case of k=10, the sum_non_ace_non_queen includes 4 (from 10s) plus 8 (jacks and kings), sum_queen adds 3. So total is 4+8+3=15, which is correct.

But what about the case where k is 10, but the card is a 10. Then 10s contribute 4, jacks and kings 4 each, queens 3. So sum is 4+4+4+3=15.

Yes.

Now, what about the case when n=20 and the second card is a 10. Then 10+10=20 → that's correct. So the code counts the 4 10s.

So the code seems to handle all cases.

Now, code:

Read n as integer.

Compute k = n-10.

sum_ =0

if 2 <=k <=10:

    sum_ +=4  # for the 2-10 of value k.

if k ==10:

    sum_ +=4+4  # jacks and kings.

sum_queen = 3 if k ==10 else 0

sum_ace =4 if (n ==11 or n==21) else 0

total = sum_ + sum_queen + sum_ace

print(total)

Yes. Let's code this.

But wait, in the code, for the sum_queen, which is part of the queens (other than spades), which contribute 10 points. So when k=10, sum_queen is 3. Because there are 3 queens left.

Yes.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    k = n - 10

    count = 0

    # Handle 2-10
    if 2 <= k <= 10:
        count += 4

    # Handle Jack and King (each contribute 10)
    if k == 10:
        count += 8  # 4 Jacks + 4 Kings

    # Handle other Queens (3 remaining)
    if k == 10:
        count += 3

    # Handle Aces (1 or 11)
    if n == 11 or n == 21:
        count += 4

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
""",
            "output": \
"""\
0
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

Sample 3: n=10 →k=0. sum_=0. sum_queen=0. sum_ace=0. total=0.

Sample 1: n=12 →k=2. sum_=4. sum_queen=0. sum_ace=0. total=4.

Another case: n=21 →k=11. sum_=0. sum_queen=0. sum_ace=4. total=4.

Another case: n=11 →k=1. sum_ace=4. sum others 0. total 4.

Another case: n=17 →k=7. sum_ +=4 (cards 7) →sum_=4. sum_queen 0. sum_ace 0. total=4.

But wait, what about queens? For example, if n=20, the sum includes queens (other than spades). Because for those queens, their contribution is 10, which adds to 20.

So the code is correct.

Thus, the code seems to handle all cases.
</think>

```python
n = int(input())
k = n - 10

count = 0

# Handle 2-10
if 2 <= k <= 10:
    count += 4

# Handle Jack and King (each contribute 10)
if k == 10:
    count += 8  # 4 Jacks + 4 Kings

# Handle other Queens (3 remaining)
if k == 10:
    count += 3

# Handle Aces (1 or 11)
if n == 11 or n == 21:
    count += 4

print(count)
```
