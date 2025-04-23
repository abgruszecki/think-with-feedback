<think>
Okay, let's try to figure out this problem. The goal is to make as many large bouquets as possible. Each large bouquet needs to consist of two or more initial bouquets, and the total number of flowers in it has to be odd. Also, each initial bouquet can be used at most once. So, how do we maximize the count here?

First, let's think about the constraints. Each large bouquet must have an odd sum. The sum of two numbers is odd only when one is even and the other is odd. Similarly, for more than two numbers, the sum will be odd if there's an odd number of odd elements in the group. Because adding an even number of odds gives even, and the rest (evens) don't affect the parity. So for any group, if the count of odd numbers is odd, the total sum is odd.

But each large bouquet must have at least two bouquets. So, for a group to be valid, the sum must be odd. Let's consider possible combinations:

Case 1: Pair an even and an odd. Their sum is odd. So each such pair forms a valid bouquet. Each pair uses two bouquets.

Case 2: A group of three bouquets where two are even and one is odd. Wait, no. Let's see: sum would be even + even + odd = odd. So that's valid. But that's three bouquets. But could we instead form two pairs from those three, maybe getting a higher total?

Alternatively, maybe combining three bouquets (like two evens and one odd) into one bouquet would use three, but that counts as one large bouquet, whereas maybe pairing them as even+odd and leave the third unused. So it's possible that using three bouquets as a group of three (if their sum is odd) gives one bouquet, but maybe combining into pairs could yield more.

Wait, but the problem is to maximize the number of large bouquets, not the number of bouquets used. So each large bouquet is counted once, regardless of how many initial bouquets are in it. So for example, a pair (two bouquets) gives one large bouquet. A group of three bouquets (if sum is odd) gives one large bouquet. So in that case, it's better to use pairs where possible, because each pair contributes one, and the three-group would contribute one. So using two pairs (four bouquets) gives two large bouquets, which is better than a three-group plus a pair (total two) but same as three-group plus a single pair (but maybe not possible). So to maximize, we need to find the optimal way to group the bouquets.

So perhaps the optimal strategy is to:

1. Pair as many even and odd bouquets as possible. Each such pair contributes one large bouquet.

2. Then, among the remaining unpaired bouquets, see if we can form groups of three to make more large bouquets. For example, if there are leftover odds (after pairing), maybe three odds can form a group (sum is odd + odd + odd = odd). Because 3 is an odd count. So that's a valid group. But each group of three odds gives one large bouquet. So if we have O remaining odds, how many such groups can we form? O divided by 3? No, wait, O needs to be grouped into groups of three. So for O >=3, each group of three gives one. But maybe even better, like if we have 5 odds left: three groups of three would need 9, but 5 is less. So 5//3=1 (using 3), leaving two. So possible.

But how does this affect the total?

Alternatively, maybe after pairing even-odds, the remaining odds can form groups of three, each contributing one bouquet.

Wait, here's the plan:

We need to consider all possible ways to form pairs and groups. But this can get complicated. Let's think step by step.

First, count the number of even and odd bouquets.

Let E be the number of even, O the number of odd.

The maximum pairs of even-odd is min(E, O). Each such pair contributes 1 bouquet. Then, after pairing as many as possible, there are E' and O' remaining.

E' = E - min(E,O) → if E > O, then E' = E-O. Else, E' is 0.

Similarly O' = O - min(E,O) → if O > E, then O' = O-E. Else, O' is 0.

Now, after this, we have E' evens left and O' odds left.

But wait, O' is either 0 (if O was less than E) or O - E (if O was larger than E). Similarly for E'.

So, for the remaining odds, O':

If O' >= 3, then each group of 3 odds gives a bouquet. Because sum is 3 odds = odd. So O'//3 is the number of such groups. But wait, if O' is 5: 5//3 is 1, which uses 3, leaving 2. Can those two be used? Well, perhaps not, unless there's an even to pair with. But after the initial pairing, there are no evens left (E' is zero if O' is positive, because O' = O-E, which implies that O > E, so E' is zero). So in that case, the remaining evens are zero, and O' is O-E.

So for example, O' could be 3, 4, 5, etc. Wait, O' would be O-E. But O > E, so O-E is the remaining odds. So the remaining evens are zero. So after pairing all possible even-odd pairs, the remaining are O' odds and E'=0.

Wait, no. Let me see. Suppose E is 2, O is 5. Then min(E, O) is 2. So we pair 2 evens with 2 odds. Now, E' is 0, O' is 5-2 = 3. So O' is 3. Then, O'//3 = 1. So we can form 1 more bouquet. So total pairs (2) + 1 (group of 3) = 3.

But wait, is that allowed? Because the group of 3 uses 3 initial bouquets, which is allowed as a large bouquet (since it's two or more). So that's valid.

So in this case, the total would be 2 (from pairs) + 1 (from group of three) = 3.

Another example: O=5, E=1. Then min(E,O)=1. So pair 1 even and 1 odd. Then O'=4. E'=0. So the remaining 4 odds. How? Then 4 odds can be grouped into groups of three? No, 4//3 is 1 group of 3, leaving 1. So total would be 1 pair + 1 group = 2. But wait, the remaining O' is 5-1=4. So group of 3: 4-3=1. So yes. So total 2.

But wait, group of 3 requires 3 bouquets. So 4 left: can take 3, make one group, then have 1 left. So yes.

So the approach would be:

After pairing all possible even-odd pairs, the remaining odds can form O' // 3 bouquets. Wait, no: O' is the remaining odds. So for example, O' =4, then 4//3 is 1. So one group of 3, and one left. So yes.

Wait, but 3 is allowed. So each group of three contributes one bouquet.

So the formula after pairing is:

max_pairs = min(E, O)

remaining_odds = O - max_pairs

if E >= O:

   remaining_evens = E - O

else:

   remaining_evens = 0

But after that, the remaining_evens can't form any bouquets. Because they are even, and to form a group sum that is odd, you need an odd number of odds in the group. But if all remaining are evens, then any group of them would sum to even. So no bouquets can be formed from the remaining evens.

So the remaining_evens are not useful. So the only way to get more bouquets is to use the remaining_odds.

So the remaining_odds can be grouped into groups of three. Each group of three adds one bouquet.

So the total is max_pairs + (remaining_odds // 3) if remaining_odds >= 3.

But wait, let's test the first example:

Sample Input 1:

5

2 3 4 2 7 → evens are [2,4,2] → E=3; odds are [3,7] → O=2.

Wait, wait: the numbers are 2 (even), 3 (odd), 4 (even), 2 (even), 7 (odd). So E is 3, O is 2.

max_pairs = min(3,2) = 2. So two pairs are made. Now, O becomes 0 (since O was 2, and we paired 2), E becomes 3-2=1. So remaining_evens=1, remaining_odds=0.

But no, wait:

Wait, after pairing 2 evens and 2 odds, the remaining E is 3-2=1, O is 2-2=0. So the remaining_odds is 0. So there are no odds left. So we can't form any more bouquets. So total is 2. Which matches the sample output.

But according to the sample explanation, they made two bouquets: one pair and another pair, but perhaps the example is different. Wait, sample input 1:

They made (2 +7) =9 (odd) as one bouquet (pair), and (3+4)=7 (another pair). Then the fourth bouquet (2) is unused. So that's two bouquets, which matches the calculation.

But according to our approach, yes. So that works.

Another sample: input 3.

3

11 4 10 → E=2 (4,10), O=1 (11). So max_pairs = min(2,1) =1. So pair one even and one odd. Then remaining E is 1, O is 0. So no more bouquets. But according to the sample, the answer is 1. But wait, the sample explanation says all three are used. So sum is 11+4+10=25 (odd). So that's a group of three. So according to our approach, we paired 1 even and 1 odd. So one pair, and then the remaining even (4 or 10) and the third bouquet (the other even) are left. But how can that be?

Wait, in this case, the initial approach would pair one even (say 4) with 11 (odd). Then the remaining E is 1 (10), O is 0. So no more bouquets. So total is 1. Which matches the sample output. But the sample used all three in a group, which is a different way. So according to our approach, that's not considered, but the answer is the same.

Wait, but in this case, the initial approach's answer is 1, which is correct. So the approach works here.

But wait, the sample's correct answer is 1, which is what the approach gives. So that's correct.

But how does the approach account for the possibility of using three bouquets instead of a pair?

In this example, if instead of pairing one even and one odd (using two bouquets and making one bouquet), we group all three (two evens and one odd) into a bouquet, that gives one bouquet as well. So the total is the same. But according to the approach, the answer would be 1 in both cases. So the approach's calculation is correct.

But in this case, the approach's steps would give the same answer. So it's okay.

So the approach seems to work.

Another example: input 2:

6

2 2 6 8 6 12 → all even. So E=6, O=0. So max_pairs = 0. Then remaining_odds =0. So total is 0. Which matches the sample.

Another example: Let's say O=4, E=1.

max_pairs is 1. Then remaining_odds=4-1=3. So 3//3=1. So total is 1+1=2.

Another example: O=5, E=0. So max_pairs=0. Then remaining_odds=5. 5//3=1 (since 3*1=3, 5-3=2). So total is 1.

But can we make two bouquets here? Let's see: group into two pairs and one group of three. Wait no, because each bouquet must consist of two or more. So for O=5, possible groups:

One group of 3 and one group of 2. But group of 2 odds: sum is even (since 2 odds sum to even). So that's invalid. So group of 3 and 2 can't be used. So only the group of 3 is valid, and the two remaining are left. So total 1.

So according to the approach, O=5, remaining_odds=5 → 5//3 =1. So correct.

But what if O=7. Then remaining_odds=7 → 7//3=2 (3+3=6, leaving 1). So two groups of three. So total 2.

Yes.

So the approach is to:

1. Pair as many even-odd pairs as possible. Each contributes 1 bouquet.

2. Then, take the remaining odds and group them into groups of three. Each group contributes 1 bouquet.

So total is the sum of these two steps.

But wait, is that the optimal approach? What if there's a better way to form more bouquets by not pairing all possible even-odd pairs, and instead creating some groups of three odds plus even pairs?

Hmm. Let's think. Suppose we have 3 odds and 1 even.

Option 1: pair the even with one of the odds. Then remaining_odds=2. No groups of three, so total 1+0=1.

Option 2: group the three odds into one bouquet, and leave the even unused. Then total 1. So same result.

Another example: 4 odds and 1 even.

Option 1: pair the even with one odd. Then remaining_odds=3. Group into one group of three. Total 1+1=2.

Alternatively, group the four odds into one group of three and leave one. But that's 1. So same as the first approach.

So the approach is correct.

Another case: 2 odds and 1 even.

Option 1: pair even with one odd. Remaining_odds=1. No groups. Total 1.

Option 2: form one group of two odds and even. But group of two odds would sum to even. Adding even gives even. So invalid. So only option is to pair even and one odd, making one bouquet. So approach is correct.

So the approach seems to work.

So the steps are:

- Count the number of even and odd bouquets.

- The maximum pairs possible is min(E, O).

- The remaining_odds after pairing is O - min(E,O).

- Then, the remaining_odds can form (remaining_odds // 3) bouquets.

So the total is min(E,O) + (remaining_odds // 3).

But wait, what if after pairing, the remaining_odds is 4. Then 4//3=1. So total is 1 +1 =2. But in this case, there are 4 odds left. Could there be a better way?

No, because grouping 3 of them into a bouquet gives one, and leaves one. So that's the maximum possible.

Thus, the approach seems correct.

So the code would be:

Read n.

Read list of a_i.

Compute E as the count of even numbers (a_i %2 ==0), O as the count of odd numbers.

max_pairs = min(E, O)

remaining_odds = O - max_pairs

total = max_pairs + (remaining_odds // 3)

But wait, what if O - max_pairs is negative? No, because max_pairs is min(E, O). So when E >= O, max_pairs = O. So O - O =0. remaining_odds is 0. So adding 0.

When O > E, remaining_odds = O-E.

So code:

E = sum(1 for x in a if x % 2 ==0)
O = len(a) - E

max_pairs = min(E, O)
remaining_odds = O - max_pairs
additional = remaining_odds //3

total = max_pairs + additional

print(total)

Wait, let's test the third sample:

Sample 3:

3 bouquets: 11,4,10.

E=2 (4,10), O=1 (11).

max_pairs =1. Then remaining_odds =1-1=0. So additional is 0. Total 1. Correct.

Sample 1:

E=3, O=2.

max_pairs=2. remaining_odds=0. So total 2. Correct.

Another example: E=0, O=3. Then max_pairs=0. remaining_odds=3. 3//3=1. So total 1.

Another example: E=0, O=5. Then max_pairs=0. remaining_odds=5. 5//3=1. So total 1. But 5 odds can form one group of 3, leaving 2. So correct.

Wait, but 5 can't form more than one group. So yes.

So the code seems correct.

But wait, there's a case where O - max_pairs could be negative? No, because when E >= O, max_pairs is O. So remaining_odds is O - O =0.

So code is correct.

Thus, the code would be:

Read n.

Read list.

E = sum(1 for x in list if x%2 ==0)

O = len(list) - E

max_pairs = min(E, O)

remaining_odds = O - max_pairs

additional = remaining_odds //3

total = max_pairs + additional

print(total)

This seems correct. Let's test all samples.

Sample 2:

Input: 6 even numbers. E=6, O=0.

max_pairs =0. remaining_odds=0. total 0. Correct.

Sample3: as before.

Another test case where O=4 and E=1:

E=1, O=4.

max_pairs=1. remaining_odds=4-1=3. 3//3=1. total=2.

Yes.

Another case where O=5, E=1:

max_pairs=1. remaining_odds=5-1=4. 4//3=1. total=2.

So that's correct.

So the code works.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
even = sum(1 for x in a if x % 2 == 0)
odd = n - even
pairs = min(even, odd)
remaining_odd = odd - pairs
print(pairs + remaining_odd // 3)
```