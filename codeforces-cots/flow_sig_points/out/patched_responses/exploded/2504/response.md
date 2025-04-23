<think>
Okay, let's see. The problem is about Caisa trying to buy sugar such that he gets the maximum number of sweets as change. And the catch is that the supermarket gives change in sweets instead of cents, but the maximum number of sweets they can give is 99. Also, the sellers maximize the number of dollars in the change. So, for example, if the change is 100 cents, that's converted to 1 dollar, so no sweets. So, the sweets are equal to the cents part of the total price subtracted from the amount he has.

Wait, no. Let me re-read the problem statement. Hmm.

Oh right, the problem says that the sellers give sweets as change instead of cents. But when they compute the change, they maximize the number of dollars. So, for example, if the total price is 3.90 dollars (so 390 cents), and Caisa pays 5 dollars (500 cents), the change is 110 cents. But the seller would give 1 dollar (100 cents) and 10 sweets. Because 100 cents is a dollar, which is maximized, leaving 10 cents as sweets. So the sweets are the remaining cents after converting as much as possible into dollars.

So the way to calculate the sweets is: the total change in cents is (s dollars * 100) minus the total price (xi * 100 + yi). Then, the number of sweets is (change % 100). But wait, only if the change is positive, right? Because if he can't afford the sugar, he can't buy it.

So the steps are:

1. For each sugar type, check if he can afford it. That is, the total cost (xi dollars and yi cents) is <= his s dollars (and 0 cents, since he pays in dollars). So, (xi * 100 + yi) <= s * 100. If not, skip this type.

2. For each valid type, compute the change in cents: (s * 100) - (xi * 100 + yi). Then, the number of sweets is this change modulo 100. Because when the seller gives change, they convert as many cents as possible into dollars. So the remaining is the modulo 100 part.

But wait, for example, if the change is 150 cents, that's 1 dollar (100 cents) and 50 sweets. So the sweets are 50.

So, for each sugar that he can afford, calculate (change % 100) as the sweets. But if the change is exactly 0 (like when s*100 equals the price), then the sweets would be 0.

Our task is to find the maximum such sweets among all affordable sugars. If none are affordable, output -1.

So the approach is:

- Iterate through all n sugar types.
- For each, check if xi * 100 + yi <= s * 100. If not, skip.
- If yes, compute the change in cents (s *100 - (xi*100 + yi)), then sweets = change % 100.
- Keep track of the maximum sweets value.
- After processing all, output the max sweets found, or -1 if none.

But wait, what if the change is negative? Then he can't buy it, so we ignore.

So the steps are straightforward.

Now, considering the constraints: n and s can be up to 100. So for each of the 100 entries, processing is O(1). So even with 100 entries, it's manageable.

So the code needs to:

Read n and s.

Then read n lines of xi and yi.

For each line, check if xi * 100 + yi <= s * 100.

If yes, compute the change (s*100 - (xi*100 + yi)), then sweets = change % 100.

But wait, if the change is 0, then sweets is 0. Which is allowed.

So, collect all possible sweets values from the affordable sugars. Then the maximum among them. If the list is empty, output -1.

So the code can look like:

Initialize max_sweets = -1.

For each sugar in the list:

   cost = xi * 100 + yi

   if cost > s*100: continue

   change = s*100 - cost

   sweets = change % 100

   if sweets > max_sweets:

       max_sweets = sweets

After all, print max_sweets if it's >=0, else -1.

Wait, but when change is 0, sweets is 0, which is >=0. So in that case, max_sweets would be 0.

But if all possible options are 0, then the output is 0, not -1.

So, in the code, the initial max_sweets is -1. Then, whenever a sugar is affordable, even if it gives 0 sweets, we compare. So for example, if a sugar's cost is exactly s dollars, then the change is 0, sweets is 0. So that would set max_sweets to 0, which is better than -1.

So in the end, if any of the sugars is affordable, max_sweets will be >=0, and we output that. Otherwise, -1.

So that's the logic.

Now, looking at the examples:

First example input:

5 10

3 90 → 390 cents. 10*100=1000. 1000-390=610. 610 mod 100 is 10. So sweets 10.

Wait, but in the sample output, the answer is 50. Wait, wait. Let me check.

Wait the first example:

Wait the fourth line is 5 50. So xi=5, yi=50. The cost is 5*100 +50 =550. s is 10, so 1000. 1000-550=450. 450 mod 100 is 50. So yes, that's 50 sweets. Which is the sample's correct answer.

So the code would pick that.

So the code is correct.

Another example: when s is 5, and all sugars cost more than 5*100. Then output is -1.

So the code works.

Now, handling the input:

We need to read n lines of xi and yi.

In Python, the code can be:

n, s = map(int, input().split())

max_sweets = -1

for _ in range(n):

    xi, yi = map(int, input().split())

    cost = xi * 100 + yi

    if cost > s * 100:

        continue

    change = (s * 100) - cost

    sweets = change % 100

    if sweets > max_sweets:

        max_sweets = sweets

print(max_sweets if max_sweets != -1 else -1)

Wait, but in the case where change is 0 (i.e., sweets is 0), the code would set max_sweets to 0, which is correct.

Yes.

Testing the first example:

After processing the fourth line (5 50):

cost is 550. 1000-550=450. 450 mod 100 is 50. So max_sweets is 50.

Which is correct.

Another test case where a sugar costs exactly s dollars. For example, s=3, xi=3, yi=0. Then change is 0. Sweets is 0. So output is 0.

In code, max_sweets would be 0.

Thus, the code is correct.

So this should handle all cases.

So the code should be as written.
</think>

```python
n, s = map(int, input().split())
max_sweets = -1
for _ in range(n):
    xi, yi = map(int, input().split())
    total_cost = xi * 100 + yi
    if total_cost > s * 100:
        continue
    change = s * 100 - total_cost
    sweets = change % 100
    if sweets > max_sweets:
        max_sweets = sweets
print(max_sweets if max_sweets != -1 else -1)
```