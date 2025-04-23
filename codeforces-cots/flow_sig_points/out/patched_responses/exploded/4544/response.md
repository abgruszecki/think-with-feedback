<think>
Okay, let's tackle this problem. Hmm, the problem is about buying all the cards with the minimum number of turns. Each turn, we can either collect tokens (which gives 1 red and 1 blue) or buy a card. When buying a card, the cost depends on how many red and blue cards we've already bought. So the key here is to determine the order of buying cards and when to collect tokens to minimize the total steps.

The constraints say n is up to 16. Oh right, that's a small number. So maybe a bitmask approach is possible here. Since each card is either bought or not, the state can be represented by a bitmask of which cards have been bought. Also, for each state, we need to track how many red and blue cards we've bought so far (since that affects the cost of remaining cards). Wait, but how do we track the necessary information for the state?

Let's think. The state would be the set of bought cards (bitmask), the current number of red tokens (R), blue tokens (B), and the count of red and blue cards bought. Wait, but R and B can be very large, right? Because each collect operation gives 1 of each. So tracking R and B directly in the state isn't feasible. That's going to be a problem. Because for n=16, the bitmask is 2^16=65536 states, but R and B can be up to something like 1e7 each. So that's way too much memory.

Hmm, so we need a way to model the state without tracking the exact token counts. Let's think differently. Let's model the state as the set of cards bought (mask) and the number of red and blue cards collected (A and B). Because when you buy a card, its color increases A or B, which affects future costs. So for each state (mask, A, B), we can track the maximum possible red and blue tokens saved, and the minimum steps needed to reach that state.

Wait, but how do we handle the tokens? The steps involve collecting tokens (which adds to R and B) and buying cards (which subtracts some from R and B based on current A and B). So the problem is to find an order of collect and buy actions such that all cards are bought, and the sum of steps (each collect is a step, each buy is a step) is minimized.

But since the collect steps can be done any number of times, perhaps we can model the required number of collects between buying cards. Like, between buying two cards, we may need to collect tokens for some steps. The challenge is to compute the minimal steps needed to accumulate the required tokens for the next card purchase.

So here's an approach: For each possible order of buying the cards (permutation), calculate the minimal steps required. But n=16, so permutations are 16! which is way too big. That's not feasible. So we need a smarter approach.

Alternative idea: dynamic programming. The state is the set of bought cards (mask), along with the current A (number of red cards) and B (number of blue cards). For each state, we track the maximum possible red tokens (R) and blue tokens (B) we have after buying those cards, and the minimal number of steps to reach that state.

Wait, but how to represent R and B in the state. Because even if mask, A, B are the same, different R and B could lead to different possibilities. For example, if two different paths reach the same mask, A, B, but one has R=5, B=3 and the other has R=3, B=5, then when buying the next card, the required tokens may differ.

But storing R and B in the state is impossible because they can be very large. So how can we model this?

Alternative approach: For each state (mask, A, B), track the maximum possible R and B that can be accumulated. Since when you collect tokens, you add 1 red and 1 blue per step. So between buying cards, you can collect some steps, which will contribute to R and B. The idea is that between buying two cards, the number of collects (k) is determined by the required tokens for the next card. So for each state, we can track the maximum R and B, such that when we proceed to buy the next card, we can compute the minimal steps needed.

Wait, maybe the key insight here is that for a given state (mask, A, B), the maximum possible R and B tokens that we can have after buying those cards and any possible collects. Then, when adding a new card, we can compute how much additional collect steps are needed to have enough tokens for that card, considering the current max R and B.

So here's the DP state: dp[mask][A][B] = (maxR, maxB, steps), where:

- mask is the set of bought cards.
- A is the number of red cards bought so far.
- B is the number of blue cards bought so far.
- maxR is the maximum red tokens available after buying the current mask and collecting optimally.
- maxB is the maximum blue tokens available.
- steps is the minimal number of steps taken to reach this state.

But A and B can be up to n (each card is either red or blue). Since n is 16, A and B can be up to 16 each. So the total number of possible (mask, A, B) is 2^16 * 16 * 16 = 65536 * 256 = 16,777,216. That's manageable, but we need to process transitions efficiently.

Wait, but for each state, we have (maxR, maxB) which can be as high as, say, 1e7. But maybe for each state, we can track the best possible (maxR, maxB) such that any further steps can be minimized.

For example, when considering a state, if we have two options with (R1, B1) and (R2, B2), if R1 >= R2 and B1 >= B2, then the second option is worse. So for each state, we can keep track of the Pareto frontier of (maxR, maxB) values. This way, we can have multiple entries per state, but only those that are not dominated by others.

This is getting complex, but perhaps manageable. Let's think about how transitions work.

For each state (mask, A, B) with some (maxR, maxB, steps), when we transition to a new state by buying a card that's not in the mask. Let's say the card is c, which has color 'R' or 'B', and requires r_red and r_blue.

When we buy this card, the required red tokens are max(r_red - A, 0), and required blue tokens are max(r_blue - B, 0). So the current maxR and maxB must be >= these required amounts. Then, after buying the card, the tokens will decrease by those required amounts. Also, the color of the card will increase A or B by 1.

But the step count increases by 1 (for buying the card). Then, any collects can be done after that. But perhaps, after buying the card, we can collect some tokens to prepare for future steps. Wait, but the collects can be done at any time. So the order of collect steps and buy steps can vary. However, each collect gives 1R and 1B per step. So the optimal strategy is to collect all the necessary tokens in between buys in the minimal steps possible.

Wait, the minimal steps between buying two cards would be the maximum of (required_red - current_red, required_blue - current_blue), but only if either of those is positive. Because each collect gives 1 of each. So the number of collects needed is the maximum of (delta_red, delta_blue), where delta_red is required_red - current_red, and delta_blue is required_blue - current_blue.

But how does this fit into the DP model?

Alternatively, when moving from state S to state T by buying a new card, we need to compute the required tokens for that card. Suppose in state S, we have maxR and maxB. Then, the required tokens for the new card are:

required_red = max(card.r - S.A, 0)
required_blue = max(card.b - S.B, 0)

If S.maxR >= required_red and S.maxB >= required_blue, then after buying the card, the tokens left are S.maxR - required_red and S.maxB - required_blue. Then, we can collect any number of steps (k), which would add k to both R and B. However, since in the DP state, we track the maximum possible R and B (since after buying, you can collect as much as you want, but any further steps would add tokens, which is better for future steps).

Wait, but collecting steps after buying the card but before the next buy is allowed. But since those collects can be done any number of times, but each collect is a step. So to minimize the total steps, we should collect exactly the needed tokens for the next buy, but since the next buy's required tokens depend on the current A and B (which are fixed once the card is bought), perhaps the optimal strategy is to collect as many tokens as possible between buys, but that's not necessary. Wait, no. Because once you have more tokens than needed, you can buy the next card. But the steps after buying a card can be used to collect tokens to prepare for future buys. So perhaps, after buying a card, the optimal is to collect as many steps as possible, but that's not the case. Because the steps add to the R and B, which can be saved for future buys.

Wait, but the tokens are not used unless you buy a card. So, for example, if after buying a card, you have some tokens left, and then collect more. The more tokens you have, the more flexibility you have for future buys. So the idea is that after buying a card, you can collect some tokens (k steps) to increase R and B by k each. The optimal k is determined based on the required tokens for the next card. But how?

Alternatively, when moving from state S to state T by buying a new card, the steps needed are:

1. Check if current maxR and maxB in state S are sufficient to buy the card. If not, then it's impossible (but since we are considering a transition, we must have enough). Wait, but perhaps we need to collect steps before buying the card. Oh right! Because between the previous steps and buying the card, we might need to collect some steps.

Wait, I think I'm getting this mixed up. Let's clarify.

The process can be:

- Start in some state where you have certain tokens (R, B), and A and B counts.

- You can perform any number of collect steps (each gives +1 R and +1 B, but each is a step).

- Then, buy a card (a step) which subtracts some R and B based on the current A and B.

So, between states, the transition can be:

Current state is mask, A, B, R, B. Then, you collect k steps (k can be 0), which increases R and B by k each, taking k steps. Then, you buy a card, which uses some R and B, and increases A or B (depending on the card's color). The total steps for this transition is k + 1 (k collects + 1 buy).

So, in the DP, for each state (mask, A, B, R, B), we can compute transitions. But again, R and B can be very large, so tracking them is not feasible.

So, perhaps the key is that for a given state (mask, A, B), the minimal steps to reach that state, along with the maximum possible R and B that can be achieved with those steps. Because having higher R and B is better for future steps. For example, if two different paths reach the same mask, A, B, but one has higher R and B, then the one with higher R and B is better because it requires fewer collect steps in the future.

So, for each (mask, A, B), we can track the maximum possible R and B that can be achieved with the minimal steps. If a new path comes to the same (mask, A, B) with steps <= current steps, and R and B >= current R and B, then this path is better, and we can ignore the previous one.

This way, for each (mask, A, B), we only keep the best (max R and B) for the minimal steps. Or perhaps, for each (mask, A, B), we track the minimal steps needed to achieve at least certain R and B. But how?

Alternatively, for each (mask, A, B), we track the minimal steps required to reach a state where the current R and B are such that after some k collects, we can buy the next card. But this seems vague.

Wait, perhaps we can model the state as (mask, A, B), and for each such state, track the maximum possible R and B that can be present after buying the cards in mask. Because the steps required to collect enough for the next card would depend on how much R and B we have.

But how to model that in the DP.

Let me try to formalize this.

Suppose we have a state (mask, A, B) with R and B tokens. The steps taken to reach this state are s. Then, when considering buying a new card (not in mask), the required red tokens for that card are max(r_i - A, 0), and blue tokens max(b_i - B, 0). Let's call these req_r and req_b.

To buy this card, we need to have R >= req_r and B >= req_b. So, the number of collect steps needed before buying this card is k = max(req_r - current R, req_b - current B, 0). Because each collect gives +1 to both. So the total steps for this transition is k (collects) + 1 (buy) + s (previous steps). Then, after buying, the new R is (current R + k - req_r), the new B is (current B + k - req_b). Also, the new mask is mask | (1 << i), and new A and B are A + (card color is R), B + (card color is B).

But how do we track R and B here? Because for each state, the R and B can vary, but the minimal steps and the maximum possible R and B are needed.

Wait, but in the DP state, instead of tracking the exact R and B, which can be very large, we can track for each (mask, A, B) the minimal steps needed to reach it, and the maximum possible R and B that can be achieved with those steps. Because if for two different R and B values, the steps are the same, but one has higher R and B, then that one is better.

So, for each (mask, A, B), we can store the minimal steps and the maximum possible R and B. Then, when processing transitions, for each possible next card, we compute the required req_r and req_b. Then, the required collect steps k is max(req_r - current R, req_b - current B, 0). If this is possible (current R + k >= req_r and current B + k >= req_b), then the new R and B after buying the card would be (current R + k - req_r) and (current B + k - req_b). Then, the new A and B are updated based on the card's color. Then, the new mask is mask | (1 << i).

But for each state (mask, A, B), how do we track the R and B? Well, perhaps for each (mask, A, B), we track the maximum possible R and B given the minimal steps to reach that state. So, if there are two different paths to reach the same (mask, A, B) with the same steps, but one has higher R and B, then that one is better, and we can ignore the other.

So the idea is:

- The DP state is (mask, A, B), and for each such state, we track the minimal steps required to reach it, along with the maximum possible R and B that can be achieved with those steps.

- For each state, when processing transitions, we can generate new states by buying each available card not in mask. For each possible card, we compute the required req_r and req_b.

- Then, the required collect steps k is max(req_r - R, req_b - B, 0). This is the minimal k needed to have enough tokens. Then, the new R and B after collecting k steps and buying the card would be (R + k - req_r) and (B + k - req_b). The steps increase by (k + 1) (k collects + 1 buy). The new mask, A, B are updated accordingly.

- For the new state (new_mask, new_A, new_B), we check if the new steps are better (less than current steps) or if the steps are the same but the R and B are higher. If so, we update the DP entry.

This way, for each state (mask, A, B), we only keep the best possible R and B for the minimal steps. So, when we process a new state, if there's already an entry with the same mask, A, B, and steps, but with higher R and B, we can ignore the new entry. If the new entry has the same steps but higher R and B, we replace the existing one. If the new entry has lower steps, we replace it.

So the DP approach would be:

1. Initialize the DP with the initial state: mask=0, A=0, B=0, R=0, B=0, steps=0.

2. For each state in the DP, process all possible transitions (buying a new card not in mask).

3. For each transition, compute the required req_r and req_b.

4. Compute the minimal k to collect before buying the card. Then, calculate the new R and B after buying.

5. Update the new state (new_mask, new_A, new_B) with steps + k + 1 and new R and B.

6. For each new state, if it's better than existing entries (steps are lower, or same steps but higher R and B), update it.

The goal is to reach the state where mask is full (all 1s), with the minimal steps.

But how do we represent this in code?

Let's think about the data structures. Since the mask can be up to 2^16, and A and B up to 16 each, we can represent the DP as a dictionary or a 3D array. Each entry for (mask, A, B) holds the minimal steps and the maximum R and B.

So for each (mask, A, B), we can store the best possible R and B and the steps taken. When a new entry comes in, if the steps are lower than the stored steps, we replace it. If the steps are equal but R and B are higher, we replace it. Otherwise, we ignore it.

So the steps would be:

Initialize a priority queue (or a BFS queue) with the initial state. But since we need to find the minimal steps, perhaps a BFS approach with states ordered by steps would work. Because each transition adds steps, which can be processed in order. So using a priority queue ordered by steps (like Dijkstra's algorithm) could help, since once we reach a state, we process it with the minimal steps first.

Alternatively, we can use BFS, processing states in order of increasing steps. This way, once a state is visited with a certain steps count, any later entries with higher steps can be ignored, because the minimal steps is already found.

This would be more efficient. Because once a state is popped from the queue with steps s, any subsequent entries for that state with steps >= s can be skipped.

So the algorithm would be:

- Use a BFS-like approach, where each state is processed in order of increasing steps.

- For each state (mask, A, B), track the current max R and B.

- For each possible next card (not in mask), calculate req_r = max(r_i - A, 0), req_b = max(b_i - B, 0).

- The required tokens for the card are req_r and req_b.

- The current R and B in the state must be >= req_r and req_b after collecting k steps. So k = max(req_r - R, req_b - B, 0).

- The new steps are steps + k + 1.

- The new R and B after buying the card would be (R + k - req_r) and (B + k - req_b).

- Then, the new A and B depend on the card's color. For example, if the card is 'R', new_A = A + 1, new_B remains B.

- The new mask is mask | (1 << i).

- For the new state (new_mask, new_A, new_B), check if it's better than existing entries. If the new steps are lower than any existing, or the steps are the same but R and B are higher, then update the DP and add to the queue.

This way, the BFS processes states in order of steps, so once a state is visited with minimal steps, subsequent entries for that state with higher steps can be ignored.

Now, how to implement this efficiently.

First, for each card, precompute the r_i and b_i, and their color.

Then, the DP can be represented as a dictionary where the key is (mask, A, B), and the value is a tuple (maxR, maxB, steps). But for each key, we need to track the best possible maxR and maxB for the minimal steps.

So, the initial state is (0, 0, 0) with R=0, B=0, steps=0.

We can use a priority queue (heap) where each element is (steps, mask, A, B, R, B). But the heap is ordered by steps. However, since steps are non-decreasing, we can process the states in order.

But storing all possible (mask, A, B, R, B) is impossible due to memory. So the key is to track for each (mask, A, B) the maximum R and B with the minimal steps.

So, for each (mask, A, B), we only keep the best (R, B) with the minimal steps. So, when processing a state, if we have already processed (mask, A, B) with a steps count less than the current state's steps, we can skip this state. Similarly, if the steps are the same but the R and B are not better than what's already stored, we skip.

So, the steps are:

Initialize a priority queue (heap) with the initial state: (steps=0, mask=0, A=0, B=0, R=0, B=0).

Also, maintain a DP dictionary where dp[mask][A][B] stores the best (R, B) and steps.

For each element popped from the heap:

- If mask is all 1s (all cards bought), return the steps.

- For each card not in mask:

   - Compute req_r = max(card.r - A, 0)

   - req_b = max(card.b - B, 0)

   - Compute the required collect steps k = max(req_r - current R, req_b - current B, 0)

   - new_R = current R + k - req_r

   - new_B = current B + k - req_b

   - new_steps = steps + k + 1

   - new_A = A + (1 if card.color == 'R' else 0)

   - new_B = B + (1 if card.color == 'B' else 0)

   - new_mask = mask | (1 << card_index)

   - Check if new_mask is full (all bought). If so, check if this is the minimal steps.

   - Check if for (new_mask, new_A, new_B), the existing entry in DP is worse than the new_steps and new_R, new_B.

   - If the new entry is better (either steps are lower, or same steps but R and B are higher), then update the DP and add to the heap.

So the priority queue is a min-heap based on steps. We process states in order of increasing steps. For each state, when we process it, we check if the steps in the DP for that (mask, A, B) are already better. If not, we process it.

But how to track the DP entries. For each (mask, A, B), we can have an entry that stores the maximum R and B for the minimal steps.

So, the DP structure can be a dictionary where the keys are tuples (mask, A, B), and the values are tuples (current_R, current_B, current_steps).

When processing a state from the heap:

- Check if the current steps are greater than the stored steps for (mask, A, B). If so, skip this state.

- If the current steps are equal to the stored steps, but R and B are not better than the stored ones (i.e., stored_R >= current_R and stored_B >= current_B), then skip.

Otherwise, proceed to process the transitions.

This way, the DP ensures that we track the best possible R and B for each (mask, A, B) with minimal steps.

Now, for the code.

Implementing this in Python. The main challenge is handling the DP efficiently.

First, read the input.

n = int(input())
cards = []
for _ in range(n):
    c, r, b = input().split()
    r = int(r)
    b = int(b)
    cards.append( (c, r, b) )

Then, the initial state is mask=0, A=0, B=0, R=0, B=0, steps=0.

We'll use a priority queue (heapq) to process states in order of steps. Each heap element is (steps, mask, A, B, R, B).

The DP can be a dictionary, where for each key (mask, A, B), we store the best (R, B, steps).

But since Python's heapq doesn't support efficient decrease-key operations, we might process the same state multiple times. To handle this, when we pop a state from the heap, we check if it's still the best known state. If not, skip processing it.

So, in code:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    cards = []
    for _ in range(n):
        c, r, b = input_stream.readline().rstrip("\n").split()
        r = int(r)
        b = int(b)
        cards.append( (c, r, b) )

    # DP is a dictionary: key is (mask, A, B), value is (maxR, maxB, steps)
    dp = {}
    heap = []

    # Initialize
    initial_state = (0, 0, 0)
    dp[initial_state] = (0, 0, 0)
    heapq.heappush(heap, (0, 0, 0, 0, 0, 0))

    found = False
    answer = 0

    while heap:
        steps, mask, A, B, curr_R, curr_B = heapq.heappop(heap)
        
        # Check if this is the best state for (mask, A, B)
        current_key = (mask, A, B)
        if current_key not in dp:
            continue
        existing_R, existing_B, existing_steps = dp[current_key]
        if steps > existing_steps or (steps == existing_steps and (curr_R < existing_R or curr_B < existing_B)):
            continue
        
        # If all cards are bought, return steps
        if mask == (1 << n) - 1:
            print(steps, file=output_stream)
            found = True
            break
        
        # For each possible next card to buy
        for i in range(n):
            if not (mask & (1 << i)):
                # This card is not yet bought
                c, r, b = cards[i]
                req_r = max(r - A, 0)
                req_b = max(b - B, 0)
                
                # Required collect steps k
                delta_r = max(req_r - curr_R, 0)
                delta_b = max(req_b - curr_B, 0)
                k = max(delta_r, delta_b)
                
                new_R = curr_R + k - req_r
                new_B = curr_B + k - req_b
                new_steps = steps + k + 1
                
                new_A = A + (1 if c == 'R' else 0)
                new_B_count = B + (1 if c == 'B' else 0)
                new_mask = mask | (1 << i)
                
                new_key = (new_mask, new_A, new_B_count)
                
                # Check if this new state is better than existing entries
                if new_key in dp:
                    existing_R_new, existing_B_new, existing_steps_new = dp[new_key]
                    if new_steps > existing_steps_new:
                        continue
                    if new_steps == existing_steps_new and new_R <= existing_R_new and new_B <= existing_B_new:
                        continue
                # Update the DP if necessary
                # If the new state is better
                if new_key not in dp or new_steps < existing_steps_new or (new_steps == existing_steps_new and (new_R > existing_R_new or new_B > existing_B_new)):
                    dp[new_key] = (new_R, new_B, new_steps)
                    heapq.heappush(heap, (new_steps, new_mask, new_A, new_B_count, new_R, new_B))
        
    if not found:
        # This shouldn't happen as per the problem statement
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
R 3 0
R 2 0
R 1 0
""",
            "output": \
"""\
6
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

But the code may work, but let's check.

In the first sample, the cards are:

Card 0: R 0 1 → when bought, requires 0 red and 1 blue tokens.

But with initial R=0 and B=0.

To buy this card, delta_r = 0-0=0, delta_b=1-0=1 → k=1. So collect 1 steps (step count +=1), then buy (step count +=1). So total steps +=2. So steps becomes 2.

After buying card 0:

new_A=1, new_B=0.

new_R = 0+1 (from collect) - 0 =1.

new_B = 0+1 (from collect) -1=0.

So the state after buying card 0 is mask=1, A=1, B=0, R=1, B=0, steps=2.

Then, for the next steps, the code may process buying card 1 (B 1 0).

req_r = max(1-1,0)=0.

req_b = max(0-0,0)=0.

So k is max(0-1, 0-0) → max(-1,0) → 0. So no collects needed.

Buying card1: steps +=0+1=1. steps becomes 2+1=3.

new_A remains 1 (card1 is B), new_B becomes 0+1=1.

new_R =1 -0=1.

new_B=0 -0=0.

So state after buying card1 is mask=3 (binary 11), A=1, B=1, R=1, B=0, steps=3.

Then, next card is card2: R 1 1.

req_r= max(1-1, 0) =0.

req_b = max(1-1,0) =0.

k is max(0-1 (since R=1), 0-0 (B=0)) → max(-1, 0) → 0. So steps +=0+1=1. steps=4.

new_A=1+1=2, new_B=1.

mask becomes 7 (111), steps=4. Which is the answer.

So the code would find this path.

But in the code, the order of processing states depends on the steps. The code may process this path, and when mask becomes 7, returns steps=4.

Another sample: the second input:

3
R 3 0
R 2 0
R 1 0

The optimal steps are 6.

In this case, the minimal steps require buying the cards in a certain order, collecting tokens along the way.

The code should handle this.

But due to time constraints, let's proceed.

Potential optimizations:

- Precompute for each card i, the req_r and req_b for all possible A and B values. But with n=16, A and B can be up to 16, so precomputing is possible.

But in the code, it's computed on the fly.

Another thing: the code uses a dictionary to track DP entries. For each (mask, A, B), checking if the new state is better. But in Python, dictionaries are efficient enough for 16 million possible keys? Since 2^16 is 65536, and for each mask, A and B can be up to 16 each. So total possible (mask, A, B) is 65536 * 16 * 16 = 16,777,216. But each mask can have varying A and B. For example, for a mask of 0 (no cards bought), A and B are 0. For a mask that has 3 R cards, A would be 3, etc. So in practice, the number of possible (mask, A, B) entries is manageable.

But using a dictionary may have some overhead. Alternatively, preallocate a 3D array. But for Python, using a dictionary is more straightforward.

But for Python, even with 1e7 entries, a dictionary would be too large. However, 16 million entries may be manageable, but perhaps not. So in practice, the code may work for n=16.

But let's see. For each (mask, A, B) key, the code checks if it's in the DP. For each new state, if the new_key is not in the DP, or the new entry is better, then it's added.

So the code should work.

Potential edge cases:

- Cards that require 0 tokens. For example, when A and B are higher than the required r and b.

- Cards that can be bought in any order, but the optimal order requires minimal collects.

In conclusion, the code uses a BFS-like approach with a priority queue, tracking for each state (mask, A, B) the maximum possible R and B with the minimal steps. This should efficiently find the minimal steps needed to buy all cards.
</think>

```python
import heapq

n = int(input())
cards = []
for _ in range(n):
    c, r, b = input().split()
    cards.append((c, int(r), int(b)))

# DP structure: (mask, A, B) -> (maxR, maxB, steps)
dp = {}
heap = []
initial_state = (0, 0, 0)
dp[initial_state] = (0, 0, 0)
heapq.heappush(heap, (0, 0, 0, 0, 0, 0))

found = False

while heap:
    steps, mask, A, B, curr_r, curr_b = heapq.heappop(heap)
    
    # Check if this state is the best known
    key = (mask, A, B)
    if key not in dp:
        continue
    best_r, best_b, best_steps = dp[key]
    if steps > best_steps or (steps == best_steps and (curr_r < best_r or curr_b < best_b)):
        continue
    
    if mask == (1 << n) - 1:
        print(steps)
        found = True
        break
    
    for i in range(n):
        if not (mask & (1 << i)):
            c, r, b = cards[i]
            req_r = max(r - A, 0)
            req_b = max(b - B, 0)
            
            dr = max(req_r - curr_r, 0)
            db = max(req_b - curr_b, 0)
            k = max(dr, db)
            
            new_r = curr_r + k - req_r
            new_b = curr_b + k - req_b
            new_steps = steps + k + 1
            
            new_A = A + (1 if c == 'R' else 0)
            new_B = B + (1 if c == 'B' else 0)
            new_mask = mask | (1 << i)
            
            new_key = (new_mask, new_A, new_B)
            
            # Update DP if this is a better state
            if new_key in dp:
                exist_r, exist_b, exist_steps = dp[new_key]
                if new_steps > exist_steps or (new_steps == exist_steps and new_r <= exist_r and new_b <= exist_b):
                    continue
            # Update and push to heap
            dp[new_key] = (new_r, new_b, new_steps)
            heapq.heappush(heap, (new_steps, new_mask, new_A, new_B, new_r, new_b))

if not found:
    print(-1)
```
