<think>
Okay, let's see. The problem is about selecting some cards with certain jump lengths and costs such that the greatest common divisor (gcd) of all selected jump lengths is 1. Because if the gcd is 1, then by the coin problem, you can reach any integer combination. So the key here is to find the subset of cards whose gcd is 1 and the sum of their costs is minimized.

So the main goal is to compute the minimum cost of a subset of cards whose gcd is 1. If no such subset exists, return -1.

The constraints are n up to 300. Hmm. So for each possible subset, the worst-case approach is O(2^300), which is impossible. So we need a smarter way.

Wait, the gcd of the selected cards must be 1. So the problem reduces to finding the minimal cost subset of cards where the gcd of their lengths is 1. How can we model this?

Dynamic programming comes to mind. Let's think about states where we track the current gcd, and for each card, we decide whether to take it or not. The state transitions would be the new gcd when we include a new card.

So the state could be a dictionary (or a hash map) that maps a current gcd value to the minimal cost needed to achieve that gcd. For each card, we iterate through all existing gcds in the current state and compute the new gcd when adding this card. Then, we update the next state accordingly.

Let me formalize this:

Initialize the DP as empty. For each card i in order:

- For each existing entry (g, cost) in the current DP:
   - Compute the new_gcd = gcd(g, li)
   - If new_gcd is not in the DP or the new cost (current cost + ci) is lower than the existing entry, update it.

Additionally, each card can be considered on its own. So for each card, if we take it, the current gcd is li. So we can start by considering each individual card, and then build up.

But with n=300, and possible gcd values up to 1e9, how do we manage the DP efficiently?

The key observation is that the number of unique gcd values encountered during this process is manageable. Because each time you take a new card, the gcd can only decrease or stay the same. So when combining with a new li, the possible gcd values are the divisors of the existing gcd and li. So the number of possible states (gcd values) is limited. For example, if you process the cards in a certain order, the number of gcd values tracked in the DP doesn't explode exponentially.

So the approach would be:

1. Initialize a dictionary (dp) to keep track of the minimal cost for each possible gcd.
2. For each card in the list:
   a. For each existing gcd g in the current dp, calculate the new gcd between g and the current card's length.
   b. For each such new gcd, update the dp by taking the minimum cost between existing entries and new possibilities.
   c. Also, consider taking the current card alone (gcd of li), and update the dp accordingly.
3. After processing all cards, check if there's an entry in dp with gcd 1. If yes, the minimal cost is the answer. Otherwise, -1.

But how to handle the initial state? Initially, the dp is empty. So for the first card, the dp after processing it would have an entry for l1 with cost c1. Then for the next card, you can either take it alone (l2 with cost c2) or combine with l1 (gcd(l1, l2) with cost c1 + c2). And so on.

Wait, but the problem allows selecting any subset of the cards. So for each card, when processing it, we can choose to add it to any existing subset, or not. Wait no, actually, the DP approach here is considering all possible subsets by considering each card and for each possible current gcd, adding the card's effect. But since including a card may only decrease the gcd, the DP state transitions are such that each step builds upon previous possibilities.

But in reality, the DP approach here is similar to the knapsack problem, where for each item (card), we can choose to include it and update the possible states. However, instead of tracking a sum, we track a gcd. The key is that including a card can only reduce the gcd of the subset, so the number of possible gcd values is manageable.

So the steps would be:

- Start with an empty DP.
- For each card (li, ci) in the list:
   - Create a temporary dictionary (new_dp) to hold the updated states.
   - For each existing state (g, cost) in DP:
      - new_gcd = gcd(g, li)
      - if new_gcd is not in new_dp or the cost (cost + ci) is less than the current value, update it.
      - Also, check if the existing new_gcd entry in the original DP (without adding this card) is better. Wait, maybe not. Because the new_dp is built from the existing DP and the current card. So for each existing state, adding the current card gives a new state, which is merged with the existing possibilities (including not adding this card). Wait, no. Wait, the new_dp is built for the current card. Then, after processing all existing states, we merge the new possibilities with the existing ones. But this approach might miss some possibilities where we don't take the current card. So perhaps the correct approach is to, for each card, consider both possibilities: taking it and not taking it. But the not taking it part is already handled by the previous DP states. So perhaps the algorithm should process each card by merging the possibilities of adding the card to existing subsets and also keeping the existing subsets that don't include the card.

Wait, maybe not. Let's think again. The DP after processing the first i cards represents the minimal cost for all subsets that can be formed by any subset of the first i cards. So when processing the (i+1)-th card, the new subsets are either the existing subsets (without the new card) or the existing subsets plus the new card. So the way to model this is to take the existing DP (without the new card) and combine it with the DP entries obtained by adding the new card to existing entries. Then, take the minimum of overlapping entries.

Wait, but how to do this. Let's consider that for each card, we can add it to any subset of the previous cards, which would create new subsets. So for each existing subset with gcd g, adding this card would create a new subset with gcd(gcd(g, li)). However, the existing subsets (without the new card) remain as part of the DP. Therefore, when processing a new card, the new DP is the union of the existing DP (subsets not including the new card) and the new possibilities (subsets that include the new card, possibly combined with previous subsets).

But if we process the cards one by one, then the DP starts empty. For the first card, the possible subsets are either take it (gcd l1, cost c1) or not take it (empty subset, which is not useful). But the empty subset's gcd is undefined. So perhaps the initial state is empty, and for each card, we process it by creating a temporary DP that includes the previous DP (not taking the current card) and the new entries from taking the current card either alone or combined with previous subsets.

Alternatively, perhaps for each card, we can generate new entries by considering the existing entries and adding the current card. Then, merge these new entries into the DP, keeping the minimal cost for each gcd.

So the algorithm would look like this:

Initialize dp as empty.

For each (li, ci) in the list of cards:

    temp_dp = copy of dp (this represents the subsets not including the current card)
    for each (g in dp):
        new_g = gcd(g, li)
        new_cost = dp[g] + ci
        if new_g not in temp_dp or new_cost < temp_dp[new_g]:
            temp_dp[new_g] = new_cost
    Also, check if the current card alone is better:
    if li not in temp_dp or ci < temp_dp[li]:
        temp_dp[li] = ci
    Now, set dp = temp_dp

At each step, the dp contains the minimal cost for each possible gcd achievable by subsets up to the current card.

After processing all cards, if there is an entry for gcd 1 in dp, then the minimal cost is the answer. Else, -1.

But wait, this approach skips some possibilities. Because the temp_dp is built by adding the current card to the existing subsets. But also, the current card can be added to any subset, including those created in previous steps. However, the way this is structured, for each card, we consider all existing entries (from the previous iteration) and add the current card to them, then merge these into the temp_dp. The temp_dp also includes the existing entries (as a copy of dp), which represents not taking the current card. Wait no, the code as described first copies the existing dp (so temp_dp is initially a copy of the previous dp, which represents not taking the current card). Then, for each existing entry in dp (the previous step's entries), adding the current card gives new entries (gcd(g, li) with cost + ci). These new entries are added to the temp_dp. Additionally, the current card alone is considered (if not already in the temp_dp, add it with cost ci). Then, the dp is updated to temp_dp.

Wait, this seems correct. Because for each card, the new subsets are either:

- Subsets not including this card (the original dp entries, which are copied into temp_dp first)
- Subsets that include this card, which can be formed by adding it to any subset from the previous dp. The new_gcd is computed, and the cost is added.
- The subset consisting of just this card (which is handled by checking if li is already in temp_dp, and adding it if needed)

But wait, when we add the current card to the existing subsets (from the previous dp), the cost is the sum of the existing subset's cost and the current card's cost. So this correctly represents the union of the existing subsets and the subsets that include the current card. Then, the temp_dp will hold all possible subsets (both those that include and exclude the current card), but only for the first i cards.

Yes, this approach should work.

Now, considering the constraints. n is up to 300. For each card, the number of entries in the dp can be up to the number of divisors of the current gcds. Since each step adds a new card, the possible gcds are divisors of the previous gcds and the new li. The number of possible gcds per step is O(log(li)), but over multiple steps, the number of entries in the dp could be up to O(n * log(max li)), which is manageable. For example, if each step adds a few new divisors, the total number of entries would be in the thousands, not millions.

So this approach should be feasible.

Now, the steps for implementation:

1. Read n, list l, list c.

2. Check if the overall gcd of all l's is 1. If not, then even selecting all cards will not give a gcd of 1, so output -1. Wait, but maybe selecting a subset could have a gcd of 1 even if the entire set's gcd is greater than 1. For example, if the entire set's gcd is 2, but a subset's gcd is 1. So that check is not sufficient. So we can't do that initial check. We have to proceed with the DP.

3. Initialize the DP as empty. For each card in the list:

   a. Create a new temporary DP, which starts as a copy of the current DP. This represents the subsets that do not include the current card. Wait, no. Wait, the current DP is for subsets up to the previous cards. Then, for the current card, we can create new subsets by adding this card to any subset in the previous DP. So the temp_dp is first a copy of the previous DP (subsets not including this card), and then we add new entries by considering adding this card to previous subsets.

   Wait, but that's not correct. Because the temp_dp is initially a copy of the previous DP, which includes all subsets up to the previous cards. Then, for the current card, we generate new entries (existing subsets plus current card). These new entries are added to the temp_dp. So the temp_dp will include:

   - All subsets from the previous DP (without the current card)
   - All subsets formed by adding the current card to any subset from the previous DP
   - The current card alone (if not already covered)

   So after processing the current card, the temp_dp represents all possible subsets formed by considering the first i cards (current and previous), and the DP is updated to temp_dp.

4. For each new entry, we want to keep the minimal cost. So for each possible gcd, if there are multiple entries leading to the same gcd, we keep the one with the minimal cost.

5. After processing all cards, check if there's an entry with gcd 1. If yes, return the minimal cost. Else, return -1.

Now, let's think about the sample inputs.

First sample:

3
100 99 9900
1 1 1

Processing first card (100, 1):

dp is empty. So temp_dp is empty. Then, check adding the current card. Since temp_dp is empty, the li (100) is added with cost 1. So dp becomes {100: 1}.

Processing second card (99, 1):

Create temp_dp as {100:1}.

For each existing entry in dp (100):

new_g = gcd(100,99) = 1.

new_cost = 1 + 1 = 2. So temp_dp now has 1:2. Also, check adding the current card alone: 99. Since 99 is not in temp_dp, add it with cost 1. So temp_dp becomes {100:1, 99:1, 1:2}.

So after second card, dp is {100:1,99:1,1:2}.

Processing third card (9900,1):

temp_dp starts as {100:1, 99:1, 1:2}.

For each entry in dp (100,99,1):

For entry 100: gcd(100,9900) = 100. new_cost =1+1=2. But temp_dp already has 100:1, so since 2 is larger than 1, no change.

For entry 99: gcd(99,9900) is 99. new_cost =1+1=2. temp_dp has 99:1, so 2 is larger, no change.

For entry 1: gcd(1,9900) is 1. new_cost is 2 +1=3. existing entry for 1 is 2, so no change.

Then, adding the current card alone (9900,1). So check if 9900 is in temp_dp. It's not, so add it with cost 1. Now, temp_dp includes 9900:1.

But the existing entries include 1:2, which is the minimal cost. So after processing all cards, the minimal cost for gcd 1 is 2. Hence, the answer is 2, which matches the first sample.

Second sample:

5
10 20 30 40 50
1 1 1 1 1

The gcd of all is 10. So even if we select all, the gcd is 10, which is not 1. So the answer is -1.

Third sample:

7
15015 10010 6006 4290 2730 2310 1
1 1 1 1 1 1 10

The card with l=1 is cost 10, but other cards' l's may combine to a gcd 1. For example, the other 6 cards may have a subset with gcd 1, which would cost 6. Hence, the answer is 6.

Fourth sample:

The details are more complicated, but the approach should handle it.

Now, considering the implementation.

In Python, using dictionaries for the DP. For each step, we process each card, create a new temporary dictionary, then merge the existing entries with the new possibilities.

But since dictionaries are mutable, we need to create a copy of the current DP before modifying it. However, for efficiency, perhaps we can process the current DP and generate new entries, then merge them into a new dictionary.

Wait, perhaps a better approach is:

For each card, create a new temporary dictionary. Then, for each existing entry in the current DP, generate new entries by adding the current card, compute the new_gcd and new_cost. Then, in the temporary dictionary, for each new_gcd, we check if it's already present and take the minimum between existing and new_cost.

Additionally, we also need to consider adding the current card alone. So even if the current DP was empty, the current card's li is added.

So here's how the code can be structured:

Initialize dp as an empty dictionary.

For each (l, c) in zip(li, ci):

    new_dp = {}
    # Copy the existing entries (subsets not including this card)
    # Wait, no. new_dp is initially empty, and we will add both existing entries (without the card) and new entries (with the card)
    # Wait, the existing entries (without the card) are part of the previous DP, but in the new_dp, we need to consider all possibilities.

    # Actually, the way to model the new subsets is:

    # The new_dp starts with the existing entries (subsets that do not include the current card)
    new_dp.update(dp)

    # Now, process adding the current card to existing entries and to itself
    # For each existing entry in the original dp (before processing this card)
    for g in list(dp.keys()):
        new_gcd = math.gcd(g, l)
        cost = dp[g] + c
        if new_gcd in new_dp:
            if cost < new_dp[new_gcd]:
                new_dp[new_gcd] = cost
        else:
            new_dp[new_gcd] = cost

    # Also, add the current card alone (if not already in new_dp)
    if l in new_dp:
        if c < new_dp[l]:
            new_dp[l] = c
    else:
        new_dp[l] = c

    # Update dp to be new_dp
    dp = new_dp

Wait, but in this code, the new_dp starts as a copy of the existing dp. Then, for each existing g in the original dp, we compute new_gcd and add it to new_dp. But wait, the original dp is the state before considering this card, so when we process each existing g, adding the current card to it gives new_gcd and new cost. These are added into the new_dp, which already has the original dp entries. But that's correct because the new_dp is built as:

- All subsets not including the current card (original dp entries)
- All subsets that include the current card and any previous subset (the entries generated by adding the current card to existing entries)
- The subset that is just the current card (handled by adding it if not present)

Wait, but when we add the current card to the existing entries (from the original dp), the new entries are added to new_dp, which already has the original dp entries. So for example, suppose the original dp has g=10 with cost 5. The new_dp starts as {10:5}. Then, for the current card l=20, c=3. The new_gcd would be gcd(10,20)=10. The cost is 5+3=8. So new_dp now has 10:5 (original) and 10:8 (new). So in this case, the code would check if new_gcd (10) is in new_dp, which it is, and the existing value is 5, which is less than 8, so no change. So the new_dp would remain 10:5.

But what if the new_gcd is a new gcd? For example, if the existing g is 6, and current l is 4. The new_gcd is 2. Suppose in the original dp, there is no entry for 2. Then, adding the current card to the existing entry 6 (cost x) would create an entry for 2 with cost x + c. If the new_dp already has an entry for 2 (from the original dp), then we take the minimum. Otherwise, the entry is added.

But this code seems correct. However, the way the code is written has an issue. Because when new_dp starts as a copy of the original dp, then for each existing entry in the original dp, the code adds the new_gcd and cost. However, when processing the original entries, some of them may have been updated in new_dp. But since the loop iterates over the original dp's keys (using list(dp.keys()) to avoid modification during iteration), the code is safe.

But in this approach, the new_dp is first a copy of the original dp. Then, for each entry in the original dp, we compute the new_gcd and new cost. For each new_gcd, if it's already present in new_dp, we compare and keep the minimum. Else, we add it. Finally, we check if the current card's l is present, and add it if necessary.

Wait, but in the code above, after adding the new entries from existing dp entries, we then check if the current card's l is in new_dp and add it. But adding the current card's l could have already been handled when considering adding the card to the original entries. For example, if the original dp is empty, then the code adds the current card's l to new_dp. But in the code as written, after the loop, the code checks if l is in new_dp. If the original dp is empty, then the loop (for g in list(dp.keys())) does nothing. Then, the code checks l in new_dp (which is empty, since new_dp was a copy of the original dp, which was empty). So the code adds l: c. Which is correct.

If the original dp is not empty, then adding the current card to the existing entries may or may not have added the current card's l. For example, if the existing entries have l1, and the current card is l2. Then, adding l2 to the existing entries will generate new_gcd = gcd(l1, l2), which may not be l2. So the code may not add the current card's l. Hence, the step where we check if l is in new_dp and add it with cost c (if cheaper) is necessary.

So the code structure is correct.

But in Python, dictionaries are mutable, so when we do new_dp = dp.copy(), but for large dictionaries, this can be time-consuming. Wait, but for each card, when we start by copying the existing dp into new_dp, which is O(k) for k entries. Then, for each existing entry in dp, we process it once. So for each card, the time per card is O(k), where k is the number of entries in the current dp.

Given that n is up to 300, and each step's k is manageable (maybe up to a few thousand per card), the total time is acceptable.

Now, let's code this.

But in Python, the initial code would be:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    l = list(map(int, input_stream.readline().rstrip("\n").split()))
    c = list(map(int, input_stream.readline().rstrip("\n").split()))

    dp = dict()

    for i in range(n):
        li = l[i]
        ci = c[i]
        new_dp = dict(dp)  # copy the existing entries (subsets without this card)
        # Process existing entries in dp to generate new entries by adding this card
        for g in list(dp.keys()):
            new_gcd = math.gcd(g, li)
            new_cost = dp[g] + ci
            if new_gcd in new_dp:
                if new_cost < new_dp[new_gcd]:
                    new_dp[new_gcd] = new_cost
            else:
                new_dp[new_gcd] = new_cost
        # Now, add the current card alone if not already present with a lower cost
        if li in new_dp:
            if ci < new_dp[li]:
                new_dp[li] = ci
        else:
            new_dp[li] = ci
        # Update dp to new_dp
        dp = new_dp

    # Check if gcd 1 is present
    if 1 in dp:
        print(dp[1], file=output_stream)
    else:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
10 20 30 40 50
1 1 1 1 1
""",
            "output": \
"""\
-1
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

Testing against sample input 3.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    l = list(map(int, input_stream.readline().rstrip("\n").split()))
    c = list(map(int, input_stream.readline().rstrip("\n").split()))

    dp = {}

    for li, ci in zip(l, c):
        new_dp = dict(dp)
        for g in list(dp.keys()):
            new_gcd = math.gcd(g, li)
            new_cost = dp[g] + ci
            if new_gcd in new_dp:
                if new_cost < new_dp[new_gcd]:
                    new_dp[new_gcd] = new_cost
            else:
                new_dp[new_gcd] = new_cost
        if li in new_dp:
            if ci < new_dp[li]:
                new_dp[li] = ci
        else:
            new_dp[li] = ci
        dp = new_dp

    print(dp.get(1, -1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
4264 4921 6321 6984 2316 8432 6120 1026
4264 4921 6321 6984 2316 8432 6120 1026
""",
            "output": \
"""\
7237
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

Therefore, the code should solve the problem correctly.
</think>

```python
import math

n = int(input())
l = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = {}

for li, ci in zip(l, c):
    new_dp = dict(dp)
    for g in list(dp.keys()):
        new_gcd = math.gcd(g, li)
        new_cost = dp[g] + ci
        if new_gcd in new_dp:
            if new_cost < new_dp[new_gcd]:
                new_dp[new_gcd] = new_cost
        else:
            new_dp[new_gcd] = new_cost
    if li in new_dp:
        if ci < new_dp[li]:
            new_dp[li] = ci
    else:
        new_dp[li] = ci
    dp = new_dp

print(dp.get(1, -1))
```
