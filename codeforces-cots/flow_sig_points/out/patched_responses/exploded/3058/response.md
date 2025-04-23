<think>
Okay, let's see. The problem is about finding the minimum cost to get all three vitamins (A, B, C) by buying some combination of juices. Each juice has a set of vitamins, and we need to cover all three. The challenge is to find the cheapest way to do this.

Hmm, so the first thing I need to think about is all possible combinations of juices that together cover A, B, and C. But considering all possible subsets of juices would be computationally expensive, especially with n up to 1000. Wait, but maybe there's a smarter way. Since each juice can contribute up to all three vitamins, perhaps we can track the vitamins we have so far and find the minimal cost combinations.

Wait, maybe the key is to look for all possible combinations of 1, 2, or 3 juices that together cover all three vitamins. Because using more than three might not be necessary. For example, if a single juice has all three, that's one possibility. Otherwise, two juices: one that covers two vitamins and another that covers the third, or two that each cover two but together all three. Or three juices each covering one.

So the possible minimal combinations are:

1. One juice with all three vitamins (ABC)
2. One juice with two vitamins and another juice with the third (e.g., AB and C)
3. Two juices each covering two vitamins that together cover all three (e.g., AB and AC)
4. Three juices, each covering a different single vitamin (A, B, C)
5. Combinations of three juices where one covers two and the others cover the remaining, but that might not be cheaper than other options.

But considering all possible combinations up to three juices might be manageable, since even if n is 1000, checking all possible combinations of 1, 2, or 3 juices is O(n) + O(n²) + O(n³). But n=1000, so n³ is 1e9, which is way too big. That's impossible. So we need a smarter approach.

Hmm, but maybe we can track for each possible vitamin combination the minimal cost. For example, there are 2^3 -1 =7 possible non-empty combinations of vitamins (A, B, C, AB, AC, BC, ABC). For each of these, we can keep track of the minimal cost to obtain those vitamins. Then, we can combine these to cover all vitamins.

Wait, dynamic programming approach. Let's see. We can represent each possible state as a bitmask where each bit represents whether we have a certain vitamin. For example:

A is 001 (binary 1)
B is 010 (binary 2)
C is 100 (binary 4)
AB is 011 (3), etc.

The goal is to reach 111 (7) with minimal cost.

We can initialize a dictionary or array that tracks the minimal cost for each possible state. Then, for each juice, we update the possible states by combining the current state with the vitamins in the juice. For example, if we have a state that covers A and B (3), and a juice that covers C (4), then combining them gives 7 (all vitamins). The cost would be the sum of the existing cost and the juice's cost.

This way, for each juice, we iterate through all existing states and update new states accordingly. But the number of possible states is small (only 7 possible non-empty combinations before the target, but actually the states can be up to 7). Wait, no. The possible states are from 0 (no vitamins) to 7 (all vitamins). But since each state can be reached in various ways, we need to track the minimal cost for each state.

But how to initialize and process this.

Let's think:

Initialize a dictionary (or array) where dp[mask] represents the minimal cost to achieve the set of vitamins in mask. Initially, dp is empty except for the masks that are exactly the vitamins of each juice. Wait, perhaps better to start with dp as a dictionary, and for each juice, we process it by updating the possible combinations.

Alternatively, here's the approach:

We start with all possible existing masks from the juices. For each juice's mask, we can merge it with existing masks to create new masks. For each possible mask combination, we check if adding the current juice's mask gives a better (cheaper) way to reach the combined mask.

So the steps would be:

1. Initialize a dictionary (or array) for the current minimal costs of each mask. Initially, all masks are infinity except for the masks that are possible from individual juices.

Wait, perhaps the DP starts empty, and for each juice, we consider adding it to the existing masks.

Wait, no. Let me think again. Let's model this as a BFS-like approach where each state is a mask, and we try to reach the full mask (7) with minimal cost.

The initial masks are those of each individual juice. Then, for each existing mask, we can combine it with another juice's mask to form a new mask. We want to track the minimal cost for each possible mask.

But how to process this efficiently.

Alternatively, we can iterate through each juice and update the DP.

Here's how it might work:

- Initialize dp as a dictionary where each key is a mask, and the value is the minimal cost to reach that mask. Initially, dp is empty.

- For each juice in the list:
   a. Convert its vitamins to a mask (e.g., 'A' is 1, 'B' is 2, 'C' is 4. So 'AB' would be 1+2=3, etc.)
   b. For this mask, if the current cost is cheaper than existing in dp, update dp.
   c. Then, for each existing entry in dp, create a new mask by combining it with the current juice's mask. The cost would be the sum of the existing cost and the current juice's cost. Check if this new mask can be updated with a lower cost.

But wait, processing each juice in this way would be O(n * 2^7) operations, which for n=1000 is manageable. Because 2^7 is 128, so 1000 * 128 = 128,000 operations. That's acceptable.

So the algorithm steps would be:

- For all juices, process them one by one, updating the DP.

- The DP starts empty.

- For each juice, first check if adding it by itself can contribute to the masks. Then, check all existing masks in the DP and see if combining with this juice's mask gives a better cost for the new mask.

Let me outline this:

Initialize dp as {mask: cost}, initially empty.

For each juice in the list:
    current_mask = mask of the juice
    current_cost = c_i

    # First, check if this juice's mask can be added to the DP. If the current_mask is not in dp, or the cost is cheaper, update it.
    if current_mask not in dp or current_cost < dp[current_mask]:
        new_dp_entry = {current_mask: current_cost}
        # Merge this into a temporary dictionary to avoid modifying dp during iteration
        # Then, after processing all existing entries, merge into dp
        temp = {}
        temp[current_mask] = current_cost
        for existing_mask in dp:
            combined_mask = existing_mask | current_mask
            combined_cost = dp[existing_mask] + current_cost
            if combined_mask not in temp or combined_cost < temp[combined_mask]:
                temp[combined_mask] = combined_cost
        # Now, merge temp into dp:
        for mask in temp:
            if mask not in dp or temp[mask] < dp[mask]:
                dp[mask] = temp[mask]
    else:
        # Also, check if combining this juice with existing masks can produce better results
        temp = {}
        for existing_mask in dp:
            combined_mask = existing_mask | current_mask
            combined_cost = dp[existing_mask] + current_cost
            if combined_mask not in dp or combined_cost < dp.get(combined_mask, float('inf')):
                temp[combined_mask] = min(combined_cost, temp.get(combined_mask, float('inf')))
        # merge temp into dp:
        for mask in temp:
            if mask not in dp or temp[mask] < dp[mask]:
                dp[mask] = temp[mask]

Wait, perhaps a better way is to process each juice, and for each existing mask in the current DP, create a new mask by OR-ing with the juice's mask, and track the minimal cost.

But to avoid modifying the dp while iterating through it, we can create a temporary copy.

Alternatively, here's a more efficient approach:

For each juice, generate a new temporary state map. For the current juice's mask, add it as a possible state. Then, for each existing state in the original dp, combine it with the current juice's mask and add the sum of costs. Then, merge this temporary state map into the original dp, keeping the minimal cost for each mask.

Wait, here's the step-by-step:

1. Start with dp as a dictionary of masks and their minimal costs.

2. For the next juice (mask m, cost c), we can create two possibilities:

   a. Using this juice alone. So the mask is m, cost c.

   b. Using this juice in combination with any existing mask in dp. For each existing mask e in dp, the combined mask is e | m, and the cost is dp[e] + c.

3. For all these possibilities, we update the temporary dictionary, and then merge it into the original dp, keeping the minimal cost for each mask.

So the code would be:

For each juice in juices:

   m = get_mask(s_i)
   c = c_i

   new_entries = {}

   # Option a: use this juice alone
   if m not in new_entries or c < new_entries[m]:
       new_entries[m] = c

   # Option b: combine with existing entries in dp
   for existing_mask in dp:
       combined_mask = existing_mask | m
       combined_cost = dp[existing_mask] + c
       if combined_mask not in new_entries or combined_cost < new_entries[combined_mask]:
           new_entries[combined_mask] = combined_cost

   # Now, merge new_entries into dp, keeping the minimum cost for each mask
   for mask in new_entries:
       if mask not in dp or new_entries[mask] < dp[mask]:
           dp[mask] = new_entries[mask]

So this way, for each juice, we generate all possible combinations with existing masks, and update the dp accordingly.

This approach ensures that after processing all juices, the dp will contain the minimal cost to reach each possible mask. Then, the answer is the minimal value in dp for mask 7 (which is 0b111, or 7).

If dp[7] is not present, return -1.

This approach should handle all possible combinations, including using 1, 2, or 3 juices. For example, three juices each contributing a single vitamin, two juices (one with AB and another with C), or one juice with all three.

Let's see:

In the first example, the third juice has mask 7 (ABC) with cost 16. The other juices are A, B, C. The combination of A+B+C costs 4+5+6=15, which is cheaper than 16. So the DP would track mask 7 as 15 after combining all three individual masks.

But how does the algorithm process this?

Processing the first juice (mask C (4), cost 5):

new_entries will have mask 4 with cost 5. dp is now {4:5}.

Next juice (mask B (2), cost 6):

new_entries for this juice is mask 2 (cost 6). Then combining with existing mask 4 (cost 5 +6=11 for mask 6 (B | C)). So new_entries becomes {2:6, 6:11}. Then merge into dp. Now dp has 4:5, 2:6, 6:11.

Third juice (mask 7, cost 16). new_entries for this is mask7 (16). Then combine with existing masks:

existing masks are 4,2,6.

4 |7 =7: cost 5+16=21. 2|7=7:6+16=22. 6|7=7:11+16=27. So new_entries includes mask7 with 16, 21, 22, 27. The minimal is 16. So after merging, dp[7] is 16.

Fourth juice (mask A (1), cost 4). new_entries is mask1 (4). Then combine with existing masks:

4: combining 4 (cost5) +4 → mask1 |4=5. Cost5+4=9. So mask5 (A | C) cost9.

Similarly, existing masks are 4,2,6,7.

For each existing_mask in dp:

existing_mask |1:

mask4 (C) |1 → A|C (5). cost5 +4=9.

mask2 (B) |1 → AB (3). cost6+4=10.

mask6 (B|C) |1 → ABC (7). cost11 +4=15.

mask7 |1 → 7. cost16+4=20. But existing mask7 has 16, so this is worse.

So new_entries for this juice:

mask1 (4).

Then combinations:

mask5 (cost9), mask3 (cost10), mask7 (cost15).

So when merging into dp:

Existing dp[7] is 16. The new cost for 7 is 15, which is better. So dp[7] becomes 15.

So after processing all four juices, the minimal cost for mask7 is 15, which matches the first example.

So this approach works.

Now, how to implement this in Python.

First, need to process each juice, convert the string to a mask.

Each character in s_i is 'A', 'B', 'C'. So for each character in the string, we set the corresponding bits.

For example, 'A' → mask 1 (binary 001), 'B' → 2 (010), 'C' →4 (100). So the mask is the sum of 1<< (ord(c) - ord('A')) for each c in s_i.

Wait, let's see:

For 'A', ord('A')-ord('A')=0 → 1<<0 =1.

For 'B', 1<<1=2.

For 'C', 1<<2=4.

So mask can be computed as sum of (1 << (ord(c) - ord('A')) for c in s_i).

Yes.

So for each s_i, the mask is sum(1 << (ord(c) - ord('A')) for c in s_i).

So code for mask:

mask = 0
for c in s_i:
    mask |= 1 << (ord(c) - ord('A'))

That's better. Because for each character in the string, set the corresponding bit.

So for 'AB', mask is 1 | 2 =3.

Now, the DP:

We can represent dp as a dictionary, initially empty. Then, for each juice, process as per the steps above.

So the code steps:

Read n.

Read the n lines, for each line, parse c_i and s_i into mask and cost.

Then, process each juice as per the algorithm.

After processing all juices, check if mask 7 is in dp. If yes, output the minimal cost. Else, output -1.

Now, let's code this.

But what about the initial state of the DP? Initially, it's empty. So for the first juice, the new_entries will be the mask of the juice and all possible combinations (which is none, since dp is empty. So the first juice's processing will add its mask to the DP.

Yes.

So the code:

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    juices = []
    for _ in range(n):
        c, s = input_stream.readline().rstrip("\n").split()
        c = int(c)
        mask = 0
        for char in s:
            mask |= 1 << (ord(char) - ord('A'))
        juices.append( (mask, c) )

    dp = {}

    for mask, cost in juices:
        new_entries = {}
        # Add the juice alone
        if mask not in new_entries or cost < new_entries.get(mask, float('inf')):
            new_entries[mask] = cost
        # Combine with existing entries in dp
        for existing_mask in list(dp.keys()):  # iterate over a copy to avoid modifying during iteration
            combined_mask = existing_mask | mask
            combined_cost = dp[existing_mask] + cost
            if combined_cost < new_entries.get(combined_mask, float('inf')):
                new_entries[combined_mask] = combined_cost
        # merge new_entries into dp
        for m in new_entries:
            if m not in dp or new_entries[m] < dp[m]:
                dp[m] = new_entries[m]

    print( dp.get(7, -1) if 7 in dp else -1 , file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
100 A
355 BCA
150 BC
160 AC
180 B
190 CA
""",
            "output": \
"""\
250
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

So the code works.

Now, in terms of performance:

Each juice is processed once. For each juice, we iterate through all existing masks in dp (which is O(2^3) =7 possible masks at most). Wait, but in practice, the masks can be up to 7, but the number of masks in dp can be up to 7 (since there are only 7 possible non-empty masks). Wait, no, when combining, you can have all 7 possible masks except 0 (since each juice has at least one vitamin). But the code starts with empty dp. So for each juice, the number of existing masks in dp is up to 7. Because there are 7 possible non-empty masks. So for each juice, the loop for existing_mask in list(dp.keys()) is O(7) steps. For n=1000, this is 7*1000 =7000 steps. Which is very manageable.

Thus, the code is O(n * 7) = O(7n), which is acceptable for n=1e3.

In terms of memory, the dp will have up to 7 entries, so it's O(1) in memory.

Thus, this approach is optimal.

Now, the code:

We need to read each juice, compute its mask and cost. Then, process each juice as per the algorithm.

The code can be written as follows.

But in Python, dictionaries are easy to handle. So here's the code:

Read n.

Initialize juices as a list of (mask, cost).

Initialize dp as an empty dictionary.

For each (mask, cost) in juices:

   create new_entries as a dictionary.

   add the current mask and cost as a possible new entry.

   then, for each existing mask in dp, compute combined_mask and combined_cost.

   update new_entries with the minimal cost.

   then, merge new_entries into dp.

Finally, check if 7 is in dp. If yes, output the cost. Else, output -1.

But in the code, for each juice, when creating new_entries, we have to:

- Add the current juice's mask and cost.

- Then, for each existing mask in dp (from before processing this juice), combine with current mask and add the sum.

Thus, in code:

for mask, cost in juices:

    new_entries = {}

    # Adding current juice alone

    if mask not in new_entries or cost < new_entries.get(mask, float('inf')):

        new_entries[mask] = cost

    # Combine with existing masks in dp

    for existing_mask in list(dp.keys()):

        combined_mask = existing_mask | mask

        combined_cost = dp[existing_mask] + cost

        if combined_cost < new_entries.get(combined_mask, float('inf')):

            new_entries[combined_mask] = combined_cost

    # Now merge new_entries into dp

    for m in new_entries:

        if m not in dp or new_entries[m] < dp[m]:

            dp[m] = new_entries[m]

Yes.

Testing this code on the examples should work.

Another example: input 4:

6

100 A → mask1, cost100

355 BCA → mask7, cost355

150 BC → mask6, cost150

160 AC → mask5 (1+4=5?), cost160

180 B → mask2, cost180

190 CA → mask5, cost190.

The correct output is 250. Let's see how.

Looking for the minimal combination.

Possible options:

- The BC (150) + AC (160): combined mask 6 |5 =7 → 150+160=310.

- Or BCA (355) alone → 355.

But the correct answer is 250. Wait, how?

Wait the correct answer is 250. Which must come from combining two juices. Which ones?

Looking at the input:

The third juice is BC (mask6, cost150).

The fourth juice is AC (mask5, cost160). 150+160=310. Not 250.

Wait, maybe other combinations.

Ah, wait the sixth juice is CA (mask5, cost190). Not helpful.

Wait, perhaps the fourth and third examples:

Wait, the sample input 4's output is 250. So how is that achieved?

Looking at the input:

6
100 A → mask1, 100
355 BCA → mask7, 355
150 BC → mask6, 150
160 AC → mask5 (A and C), 160
180 B → mask2, 180
190 CA → mask5, 190.

Wait, the correct combination is BC (150) + AC (160) → mask6 |5 =7, cost310. But the sample output is 250. So perhaps I'm missing something.

Wait, the sample output is 250. So perhaps another combination.

Wait, perhaps BCA (mask7) cost355 is not part of the solution. Or maybe other combinations:

Wait, what about B (180) + AC (160) → mask2 |5 =7 (2 is B, 5 is A and C). So 180+160=340. No.

Hmm, maybe BC (150) + A (100) → mask6 |1=7. 150+100=250. Oh right! Because BC is vitamins B and C. Adding A's 100, which is 100, so total 250.

Yes. So the two juices BC (cost150) and A (cost100) combine to all vitamins. Total 250.

So in the code, when processing the first juice (A, mask1, 100), then when processing the third juice (BC, mask6, 150), their combination is 1 |6=7, cost100+150=250. So the code should track that.

Let's see how.

Processing the first juice (mask1, 100):

new_entries is {1:100}. dp is {1:100}.

Second juice is BCA (mask7, 355):

new_entries starts as {7:355}.

Combine with existing mask1 → 1 |7 =7 → cost100+355=455. So new_entries has {7:355, 7:455}. The minimal is 355. So after merging, dp is {1:100, 7:355}.

Third juice (mask6, 150):

new_entries starts as {6:150}.

Combine with existing masks (1,7):

1 |6=7 → cost100+150=250.

7 |6=7 → 355+150=505.

So new_entries after combining: {6:150,7:250}.

Now, merging into dp:

dp's existing 7 is 355. The new entry is 250, which is better. So dp[7] becomes 250.

So the answer is 250.

Thus, the code correctly captures that combination.

Yes, so the code works for this case.

Thus, the code is correct.
</think>

```python
n = int(input())
dp = {}
for _ in range(n):
    c, s = input().split()
    c = int(c)
    mask = 0
    for char in s:
        mask |= 1 << (ord(char) - ord('A'))
    new_entries = {}
    if mask not in new_entries or c < new_entries.get(mask, float('inf')):
        new_entries[mask] = c
    for existing_mask in list(dp.keys()):
        combined_mask = existing_mask | mask
        combined_cost = dp[existing_mask] + c
        if combined_cost < new_entries.get(combined_mask, float('inf')):
            new_entries[combined_mask] = combined_cost
    for m in new_entries:
        if m not in dp or new_entries[m] < dp.get(m, float('inf')):
            dp[m] = new_entries[m]
print(dp.get(7, -1) if 7 in dp else -1)
```
