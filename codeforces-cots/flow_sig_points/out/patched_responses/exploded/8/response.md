<think>
Okay, let's see. The problem is about a second-price auction. The winner is the one with the highest bid, but they pay the second highest price. So, I need to find the highest bid, then find the second highest among the others. Then output the index of the highest bidder (1-based) and the second highest value.

Hmm. How to approach this? Let's think about the steps.

First, the input is n followed by a list of n distinct integers. The output is the index of the maximum value and the second maximum value.

Wait, but the second maximum is the maximum of the remaining elements after removing the winner's bid. So, if the highest is at position i, then the price paid is the maximum of all elements except p_i.

Wait, right. Because the winner pays the highest price among the other participants. So even if the second highest is part of the same group, but once you take out the highest, the next is the maximum of the remaining.

So, for example, in the first sample input: 5 and 7. The highest is 7 (index 2), and the other is 5. So the price is 5. That's correct.

So the approach would be:

1. Find the maximum value in the list and note its index (since there are no duplicates, there's exactly one maximum).
2. Remove that maximum from the list (or create a new list without it) and find the maximum of the remaining elements. That's the price.

But how to do this efficiently?

Since n can be up to 1000, even a O(n^2) approach is acceptable, but we can do better.

Alternative approach:

We can track the first and second maximum values. But wait, the second maximum might not be the one that's needed. Because the second maximum in the entire list could be part of the same group as the first. For example, let's say the list is [10, 9, 8]. The highest is 10 (index 1), the other elements are 9 and 8. The second maximum among the others is 9. So the price is 9. But if the list was [9,10,8], then the highest is 10 (index 2), others are 9 and 8. So price is 9.

Wait, so in this case, the second maximum in the entire list is 9, which is the correct price. So, perhaps the second maximum in the entire list is the price to pay. But wait, what if there's a higher value after the first maximum? Like, in [1,3,2], the first max is 3 (index 2), the others are 1 and 2. So the second max is 2, which is the price. But the second maximum in the entire list is 2. So in this case, it's correct.

Wait, but what if the list is [5,7,6]. The max is 7 (index 2). The others are 5 and 6. So the second maximum in the others is 6. But the second max in the entire list is 6. So yes.

So the price the winner pays is the second highest value in the entire list. Wait, is that correct?

Wait, no. Wait, in the first case, the highest is 7. The other elements are 5. So the price is 5. But in the entire list, the second highest is 5, which is correct. So perhaps the price is the second maximum of the entire list. But wait, what if the two highest values are in the list. Let's take an example where the list is [10, 8, 9]. The maximum is 10 (index 1), the others are 8 and 9. The price is 9, which is the second highest in the entire list. So yes, the price is the second highest in the entire list.

So maybe the approach can be:

Find the index of the maximum value. Then find the maximum of all elements except that maximum.

Alternatively, find the two highest values. The highest is the winner, and the second highest is the price. But wait, no. Because the second highest could be next to the highest. For example, in [10, 9, 8], the second highest is 9, which is the price. But if the list is [9,10,8], the second highest is 9, which is the price. So yes, the price is the second highest value in the entire list. Wait, but in the case where the list is [10, 9, 7, 8], the second highest is 9, and when the maximum is 10, the price is 9. Which is correct. So perhaps the second maximum in the entire list is the price.

Wait, but what if the list is [10, 15, 14]. The maximum is 15 (index 2). The others are 10 and 14. The price is 14, which is the second highest in the entire list. So yes.

So in all these cases, the price is the second maximum. So the solution can be:

Find the maximum value (and its index), then find the maximum value in the list that is less than the maximum. That's the price.

Wait, but that's exactly the second maximum in the list. So the problem reduces to finding the two largest distinct elements. Since all prices are unique.

So the steps would be:

1. Find the maximum value and its index (the winner's index).

2. Find the maximum value among the remaining elements (i.e., the second maximum in the original list).

So the solution can be done in O(n) time.

So how to implement this?

We can loop through the list once, tracking the two highest values and their indices.

Alternatively, we can loop once to find the maximum and its index, then loop again through the list to find the maximum that is not the first maximum.

Either approach would be O(n), which is efficient.

For example:

Approach 1: Find max, then find max again excluding the max.

But how to exclude the max? Because there can be multiple elements with the same value, but the problem states all are distinct. So the max is unique. So the second loop can just check for elements less than the first max, and find the max among them.

Yes.

So code steps:

Read n.

Read the list p as integers.

max_val = max(p)

winner_index = p.index(max_val) + 1  # since 1-based.

Then, find the second_max_val = max( x for x in p if x != max_val )

Then output winner_index and second_max_val.

But wait, in Python, the index method returns the first occurrence. But since all elements are distinct, there is only one occurrence. So that's correct.

Yes.

So this approach would work.

Now, what about the time? For n=1000, two passes are O(n) each, which is acceptable.

So in code:

n = int(input())

p = list(map(int, input().split()))

max_val = max(p)

winner_index = p.index(max_val) + 1

second_max = max( x for x in p if x != max_val )

print(winner_index, second_max)

That's straightforward.

Testing the first example:

Input 2: 5 7.

max_val is 7, index 1 (0-based) +1 is 2. second_max is 5. Output 2 5. Correct.

Second example: 10, 2,8.

max_val is 10. index is 0, +1 is 1. second_max is max(2,8) is 8. So output 1 8. Correct.

Third example: 3 8 2 9 4 14.

max is 14. index is 5, +1 is 6. others are 3,8,2,9,4. max of these is 9. So output 6 9. Correct.

So the code works for these examples.

Now, let's think about possible edge cases.

Case where the second max comes after the first max.

Like input: [1,3,2]. Max is 3 (index 1), second max is 2. So output 2 (index 2) and 2.

Wait, code will compute second_max as max(1,2) which is 2.

Yes.

Another case: [5,4,3,2,1]. Max is 5 (index 0+1=1). second_max is 4. Correct.

What if the list is in reverse order: [5,4,3,2,1], same as above.

So the code works.

Another case where the max is in the middle: [2,5,3]. Max is 5 (index 1, 1-based 2). second_max is 3.

So code would output 2 3. Correct.

So the code is correct.

Now, about efficiency. For n up to 1000, this is trivial. The code will run in O(n) time, which is optimal.

So the code is correct and efficient.
</think>

```python
n = int(input())
p = list(map(int, input().split()))
max_val = max(p)
winner_index = p.index(max_val) + 1
second_max = max(x for x in p if x != max_val)
print(winner_index, second_max)
```