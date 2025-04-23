<think>
Okay, let's try to figure out this problem. So, we have a circle of n chips that change color over k iterations based on their neighbors. The main challenge is handling large n and very large k efficiently. 

First, let's understand the problem. Each chip's next state depends on itself and its two immediate neighbors. For each position, we look at three chips: left, current, right. Then, if the majority are white (at least two), it becomes white. Otherwise, black. 

But with n up to 200,000 and k up to 1e9, simulating each step is impossible. So we need a smarter approach. 

Hmm. Let's think about patterns here. Maybe after some steps, the configuration starts repeating. Like cycles. If we can find the cycle length, then compute k modulo that cycle length. But even that might not be straightforward, especially for large n. 

Alternatively, perhaps after a certain number of steps, the system stabilizes. For example, if all chips become the same color. Once that happens, further iterations won't change anything. Let's check the examples. In the second example, after 3 steps, all become W. So subsequent steps would leave them all W. So if we reach a state where all are W or B, then we can stop early. 

So maybe, for each chip, after some steps, it stops changing. Or perhaps the entire system stabilizes into a fixed point or a cycle of small length. 

Another observation: The transformation rules are deterministic and local. Each step depends only on the previous state. So for a given initial state, the future states are uniquely determined. 

But how can we model this efficiently? Let's think about possible scenarios:

1. The system reaches a fixed point (no more changes) after some iterations. Then, after that point, we can return that state. 
2. The system enters a cycle of period m. Then, after m steps, it repeats. So we can compute k modulo m once we reach the cycle. 

But how do we find out when this happens? For n up to 2e5, we can't track all possible states. 

Wait, but the problem is that even if individual positions have their own cycles, the entire state might not. So this approach might not be feasible. 

Alternative idea: For each position, determine after how many steps its color stabilizes, and what the final color is. But since each step depends on the neighbors, this seems non-trivial. 

Wait, the key is that each step's state depends on the previous state. So perhaps after some steps, the state becomes periodic. Let's think about the third example. The pattern alternates between BWBWBW and WBWBWB every iteration. So the period is 2. So for k=4, it's even, so returns to the original. 

So in such cases, the state alternates between two configurations. So if k is large, we can compute whether it's even or odd and return the appropriate state. 

So how can we model this? Let's think: for some configurations, after a few steps, the state stops changing (fixed point) or cycles between a few states. 

But how do we detect this for a general case? For large n and k, simulating each step until the cycle is detected is impossible. So we need a smarter approach. 

Let's think about the possible transitions. Let's model each cell's next state based on its current state and neighbors. 

Each cell's next state is determined by the majority in the triplet (left, current, right). Since majority requires at least two, the next color is W if two or three of the three are W, else B. 

But since the chips are arranged in a circle, the transitions are circular. 

Let me consider some small cases to see if there's a pattern. 

For example, if a chip and its two neighbors are all W, then next state is W. Similarly for all B. 

But if there's a mix, like W B W, then the next state for the middle B would be W (since two Ws). 

Hmm. So maybe regions of consecutive same colors expand. 

Wait, another observation: Once three consecutive Ws occur, those positions will stay W forever. Because in the next step, each of their triplets has at least two Ws. 

Wait, let's see. Suppose positions i-1, i, i+1 are all W. For position i, the triplet is all W, so next state is W. For position i-1, the triplet is (i-2, i-1, i). If i-1 and i are W, then if i-2 is W, then all three W. If i-2 is B, then two Ws, so i-1 becomes W. So the only way for a W to stay W is if either the triplet has majority W. So once a W has two W neighbors, it remains W. 

Similarly for B? No. If a B is between two Bs, then triplet is Bs, so next state is B. If a B is between B and W, then two Bs (current and one neighbor) and one W. So majority is B, so B stays B. 

So maybe once a chip is part of a block of three same colors, it will stay that color. Otherwise, it might flip. 

So perhaps the system stabilizes once all consecutive triplets have majority in their own color. 

Alternatively, after each iteration, the regions of same colors may expand. 

This suggests that after some steps, the system reaches a state where no more changes occur. But how many steps could that take? For example, in the third example, the system alternates between two states. So it never stabilizes. So in that case, the period is 2. 

So how can we handle this in code? 

Idea: For each position, check if it's in a block of three same colors. If so, it's stable. Otherwise, compute how it changes. But even that may not be efficient for large n. 

But with k up to 1e9, we can't process each iteration step by step. So we need a way to compute the state after k steps without iterating each step. 

Alternative approach: Find that after a certain number of steps, the state stops changing. For example, after O(n) steps, the system stabilizes. Then, for k larger than that, we can compute the stabilized state. 

But how to find that number of steps? 

Suppose that the system stabilizes after m steps. Then, for k >= m, the answer is the same as after m steps. So if m is O(n), then for k up to 1e9, we can compute up to m steps and then return the result. 

But how to find m? 

Let's think: Each step, the regions of same color might expand. For example, if there's a run of three Ws, they stay. Then, their adjacent positions might flip to W in the next steps. 

So perhaps, after each step, the number of stable regions increases. For instance, after each step, the influence of a stable region can cause neighboring regions to stabilize. 

Alternatively, the maximum number of steps required for stabilization could be O(n), which for n=2e5 would be manageable. But even 2e5 steps would be O(n) time, which is acceptable. 

So here's the plan:

1. For each step until the state stabilizes or until k steps, compute the next state. 
2. Once the state stabilizes (no changes from one step to the next), we can stop early. 
3. If the system reaches a cycle (like the third example), we need to detect that and compute the remaining steps modulo the cycle length. 

But how to detect cycles? For example, in the third example, after each step, the state alternates. So after the first step, it's WBWBWB, then BWBWBW, then WBWBWB again. So the cycle length is 2. 

But detecting such cycles is tricky, as the state could have a cycle of any length, and comparing the entire state after each step is O(n) time, which would be expensive for n=2e5 and steps up to O(n). 

Alternative idea: The system may either stabilize (enter a fixed point) or enter a cycle of length 2. Are there any examples where the cycle is longer than 2? Let's think. Suppose a configuration that cycles through 3 states before repeating. For example, for some pattern, after 3 steps, it returns to the original. But I can't think of such a case. Maybe not. 

So perhaps all cycles are of length 1 (fixed point) or 2. If that's the case, then after each step, we can check if the current state is the same as the previous state (fixed point) or the state two steps back (cycle of 2). 

If we can detect that, then we can compute the remaining steps based on whether it's even or odd. 

So the approach could be:

- Simulate each step, keeping track of the previous states. 
- After each step, check if the current state is the same as the previous state (fixed point) or the same as the state two steps back (cycle of 2). 
- If a fixed point is found, stop and return the state. 
- If a cycle of 2 is found, then compute the parity of the remaining steps and return accordingly. 

But for n=2e5, storing the entire state for each step would take O(n) memory per step, which is impossible. So even storing two steps would take O(2n) memory, which is manageable. 

Wait, but for each step, we need to generate the next state based on the current state. So we can simulate steps, but keep track of the current state and the previous one, and the one before that. 

Wait, for example, after each step, we can check if the current state equals the state two steps back. If yes, then we have a cycle of length 2. Then, for the remaining steps, even k would leave it as the current state, and odd would flip once. 

But how to check if the current state is the same as a previous one. For large n, comparing all n elements each time is O(n) per step, which could be O(n^2) time if we have up to O(n) steps. For n=2e5, that's 4e10 operations, which is way too slow. 

So this approach isn't feasible. 

Alternative idea: Find that after a certain number of steps (say, O(log n)), the state either stabilizes or starts cycling. But I'm not sure. 

Hmm. Let's think differently. Let's model each cell's state over steps. Each cell's next state depends on its left, itself, and right. So for each cell i, next state is a function of i-1, i, i+1 in the current state. 

But this is a deterministic cellular automaton with a certain rule. The behavior of such systems can be complex. 

But given the problem's constraints, perhaps we can find that after each step, the number of changes (cells that flip) decreases, leading to a stabilization. 

Wait, let's think about the first example. After the first iteration, some cells change. Then, in subsequent steps, perhaps the changes become fewer. 

Alternatively, maybe the system reaches a state where no two consecutive cells are the same. Like in the third example. But how would that affect the transitions? 

Alternatively, perhaps after some steps, the state becomes "periodic" with certain patterns. For example, in the third example, the pattern alternates between B and W for each cell, leading to a cycle of 2. 

But to model this for all possible cases, perhaps the key is to note that after O(1) steps, the system either stabilizes or starts cycling with period 2. 

Wait, in the third example, after one step, the state changes to WBWBWB. Then after another step, it returns to BWBWBW. So each step flips all the cells. So after two steps, you're back to the original. 

In that case, the cycle length is 2. So for k steps, if even, the state is the original. If odd, it's the flipped version. 

So, for the third example, the answer depends on whether k is even or odd. 

So how can we detect this? 

If after two consecutive steps, the state returns to the previous state (i.e., after step m and m+2, the states are the same), then we have a cycle of 2. 

But checking this for every two steps would require storing the previous two states. 

But for large n, comparing two arrays of size 2e5 each step is O(n) time. Which would be O(n^2) in the worst case. Not feasible. 

Alternative Idea: For each step, compute the next state and check if it's the same as the previous state (fixed point) or the same as the one before that (cycle of 2). 

But again, comparing the entire array is O(n) per step. 

So, how can we track this without comparing the entire array? 

Hmm. Maybe use a hash to represent the state. For example, compute a checksum (like a hash) of the current state. Then, for each step, store the hash and see if it repeats. But even then, for n=2e5, computing the hash each time could be O(n) per step. Which again is O(n^2) in the worst case. 

So, this approach isn't feasible either. 

Alternative Idea: Realize that after a certain number of steps, the state stops changing. So if we can find that after m steps, the state stops changing, then for k >= m, the answer is the state after m steps. 

But how to compute m? 

Perhaps m is at most n steps. For example, each step, the pattern propagates changes in a way that after n steps, all possible changes have happened. 

But this is a rough guess. Let's see. For example, in the third example, the system cycles between two states, so m would not exist. So in that case, we need to handle cycles. 

So here's the plan:

1. Simulate steps until either:

   a. The state becomes the same as the previous state (fixed point). Then, return it. 

   b. The state becomes the same as the state two steps back (cycle of 2). Then, compute the remaining steps modulo 2. 

   c. We reach k steps. 

2. For each step, compute the next state and check these conditions. 

But comparing the entire array each time is O(n), which for m steps would be O(mn). If m is O(n), then O(n^2), which for n=2e5 is 4e10 operations—way too slow. 

So this approach is not feasible. 

Alternative Idea: Find that after a small number of steps (like 100), the state either stabilizes or starts cycling. But that's a conjecture. 

Wait, let's look at the examples. 

First example: 6 chips. After 1 step, the state changes, but perhaps after some steps, it stabilizes. 

Second example: after 3 steps, it becomes all W. So no more changes. 

Third example: cycles every 2 steps. 

So, perhaps in practice, the number of steps required to reach a fixed point or a cycle is small. For example, in the worst case, O(1) steps. 

But how to verify this. 

Another Idea: For each position, after some steps, the state becomes fixed. For example, if a position and its neighbors are all the same color, then it's fixed. 

But even if a position is part of a trio, the entire array might not stabilize. Like in the third example. 

Wait, in the third example, each trio consists of two Bs and one W, or vice versa. So each step flips all the colors. 

So perhaps, when there are no three consecutive same colors, the system can enter a cycle. 

So the key is whether there are three consecutive same colors. 

Let me think: if a chip has the same color as both neighbors, then it will stay that color. Because the trio would have three same colors, majority. So the next state is same. 

But if a chip has different colors than at least one neighbor, then its next state depends on the majority. 

So perhaps, once a trio of three same colors exists, those positions are fixed. 

So for example, if there's a trio of Ws, then those Ws will remain W in all future steps. Their neighbors' next states may depend on that. 

So maybe, the presence of such trios can help the system stabilize. 

If the initial configuration has no trios of same colors, then after each step, perhaps the entire state flips. Like in the third example. 

So, the problem can be divided into two cases:

1. The configuration has at least one trio of same colors. Then, after some steps, the system stabilizes. 

2. The configuration has no trios. Then, each step flips all the colors. So the state alternates between the initial and flipped state each step. 

So, first, we need to check if the initial configuration has any trio (three consecutive same colors). 

If there are no trios in the initial configuration, then each step will flip all the colors. Because for each position, the trio (left, current, right) has two of one color and one of another. So the majority is two, which is the opposite of the current color. For example, if current is B and left is W, right is W, then majority is two Ws, so current becomes W. But in the initial case where there are no trios, the next state would flip all colors, leading to all trios again not existing, but each step flips again. 

Wait, for example, initial state is BWBWBW (n=6). Each trio is BWB, WBW, BWB, etc. For each trio, two Bs and one W (for the first trio, left is B, current is W, right is B. So W is the current, and majority is two Bs, so next state is B. So the current W becomes B. But in the third example, after the first step, the entire state flips. So each step inverts all the colors. 

So, for a configuration with no trios, the system will alternate between the initial and flipped state every step. 

So, the key is to check whether the initial configuration has any trio. 

If there are no trios, then the state alternates every step. So after even steps, it's the same as initial. After odd steps, it's the flipped. 

But wait, in the third example, after one step, it's WBWBWB. Then, after another step, it's BWBWBW again. So the cycle is 2. 

So, in this case, when there are no trios, the state alternates every step. 

But how to detect if there are any trios in the initial state. 

So, the plan is:

- Check if the initial configuration has any trio. 

   a. If there are trios, then simulate steps until either k steps are done or the state stabilizes (no changes). 

   b. If there are no trios, then check if the entire state flips each step, leading to a cycle of 2. Then, compute based on k's parity. 

But even if there are trios, the system may not stabilize quickly. For example, a trio may spread to neighboring positions. 

But how to handle this efficiently. 

So, for the case where there are trios in the initial state, we can simulate each step until either the state stabilizes (no changes from previous step) or we reach k steps. 

But for n=2e5 and k=1e9, how many steps do we need to simulate? 

Assuming that the system stabilizes in O(n) steps, then for n=2e5, this would be O(2e5) steps, which is manageable. 

But in practice, it might stabilize much faster. 

So the steps would be:

1. Check if the initial state has any trios. 

   a. If not, then after each step, the entire state flips. So the result after k steps is:

      - if k is even: same as initial state.

      - if k is odd: flipped state.

   b. If there are trios, then simulate each step. For each step:

      - Generate the next state based on the current state. 

      - Check if the next state is the same as the current. If yes, break and return.

      - Otherwise, check if it's the same as two steps back (cycle of 2). If yes, compute remaining steps modulo 2.

      - Otherwise, proceed until k steps. 

But how to check for the cycle of 2 without storing the previous states. 

Alternatively, since the cycle of 2 can only happen if there are no trios (since trios would prevent flipping), then maybe once there's a trio, the system will eventually stabilize. So, if the initial state has trios, then after some steps, the system will stabilize into a fixed point. 

But this is not certain. Let's see. 

Suppose we have a configuration with some trios. For example:

WWWBBBB

The trio at the beginning is three Ws. Those will stay W. The next positions are B's. For a B in position 4 (neighbors 3 and 5 are B and B), so triplet is B, B, B. So they stay B. So the entire configuration is fixed. 

Another example: WWBWW. 

In the first step:

For position 1: neighbors 3 and 2. Wait, original positions are 1, 2, 3, 4, 5 (n=5? Or maybe a larger n). Let's take n=5, initial state is WWBWW. 

Wait, position 1's neighbors are 5 and 2. 

So the trio for position 1 is 5,1,2. All are W except position 5. Wait, initial state is WWBWW. So positions 1: W, 2: W, 3: B, 4: W, 5: W. 

For position 1, triplet is 5 (W), 1 (W), 2 (W). So majority W. So next state W. 

Position 2: neighbors 1 (W), 2 (W), 3 (B). So majority W. Next state W. 

Position 3: neighbors 2 (W), 3 (B), 4 (W). So two W's, majority. Next state W. 

Position 4: neighbors 3 (B), 4 (W), 5 (W). Majority W. Next state W. 

Position 5: neighbors 4 (W), 5 (W), 1 (W). All W. So next state W. 

So after one step, all become W. So the system stabilizes. 

So the presence of even a single trio can lead to the system stabilizing after a few steps. 

So perhaps, once there's at least one trio, the system will stabilize in O(1) steps. 

But how to determine this. 

Alternatively, in the first example, there are trios after one step. For example, in the first step, the state becomes WBBBWW. Let's check for trios:

W B B B W W. 

Looking for three consecutive same colors. The B's at positions 2,3,4 are three consecutive B's. So they form a trio. So in the next step, their color remains B. 

In the next step, their neighbors (positions 1,5, etc) may change based on their neighbors. 

So the presence of trios can cause the system to stabilize. 

So the general approach could be:

- Check if initial state has any trio. If not, handle the flipping case. 

- Else, simulate steps until either the state stabilizes (no change from previous step) or we reach k steps. 

But how to check for trios in the initial state. 

To check for trios in the initial state, we can loop through each position and see if s[i] == s[i-1] and s[i] == s[i+1], considering the circular arrangement. 

But for n=2e5, this is O(n) time. 

Once we have this information, we can proceed accordingly. 

So the steps for the code would be:

1. Read n, k, and the initial string. 

2. Check if the initial string has any trio. 

3. If there's no trio:

   a. If k is even, output the initial string. 

   b. If k is odd, output the flipped string (each character is inverted). 

4. Else:

   a. Simulate steps until either k steps are done or the state stops changing. 

   b. For each step, generate the next state and check if it's the same as the previous. 

   c. Once the state stops changing, break and output it. 

But simulating steps for a large n (2e5) could be O(mn) time, where m is the number of steps. 

But how many steps are needed until stabilization? 

If after each step, the trios expand, then for each step, the number of positions that are part of a trio increases. So after O(log n) steps, the entire array is covered. 

But this is not clear. 

Alternatively, perhaps after O(1) steps, the system stabilizes. For example, in the first example, after one step, there are trios. Then in the next step, those trios influence their neighbors, leading to more trios. 

But how to model this. 

Alternatively, for each step, the state can be computed in O(n) time. 

But for n=2e5 and m=200 steps, this would be 4e7 operations, which should be manageable. 

But how many steps are needed for the system to stabilize. Let's think. 

Suppose that during each step, a trio in the current state causes their adjacent positions to form trios in the next step. 

For example, in the first step, a trio is formed. Then, in the next step, the neighbors of this trio form trios. So the trio expands. 

If this is the case, then after O(n) steps, the entire array would be filled with trios. 

But I'm not sure. 

Alternatively, let's take the first example:

Initial state: B W B B W W (after the first iteration, it becomes W B B B W W). 

In the first iteration, there's a trio of B's in positions 2,3,4 (assuming 1-based index). So during the next iteration, these B's will remain. 

Then, their neighbors (positions 1,5, and 5,6,1?) 

Wait, perhaps after a trio is formed, the neighboring positions may form their own trios. 

But this depends on their neighbors. 

Alternatively, once a trio is formed, their neighbors will have two B's (assuming the trio is B's). So for example, in the trio B B B, the neighbor to the left (assuming the trio is positions 2,3,4) is position 1. Position 1's neighbors are position n (which is 6) and 2. So if the trio is in 2,3,4, then position 2 is part of the trio. So during the next step, for position 1, its neighbors are 6 (W), 1 (current state?), and 2 (B). 

Hmm, perhaps the trios expand outward. 

But this is getting complicated. 

Alternatively, perhaps the maximum number of steps needed is 100. So even for n=2e5, 100 steps would be 2e7 operations, which is manageable. 

But how to verify this. 

Alternatively, for any state with at least one trio, the system stabilizes after at most O(log n) steps. 

But I'm not sure. 

Alternatively, for any state with a trio, after each step, the system will either stabilize or add more trios. 

But I'm not certain. 

So the code plan is:

If there are no trios initially, then handle the flipping case. 

Else, simulate each step, up to k steps, until the state stabilizes. 

So the code steps are:

Check if the initial string has any trio. 

If no trios:

   if k is even: output initial string.

   else: flip each character and output.

Else:

   prev = initial string.

   for step in 0 to k-1:

      compute next state.

      if next == prev: break (fixed point).

      check if next == two steps back (if stored). But not sure how to track this. 

      else:

          prev = next.

   output prev.

But how to compute the next state. 

For each position i in 0..n-1 (assuming 0-based), the next state depends on the previous state of (i-1) % n, i, and (i+1) % n. 

We need to compute the next state for all i in O(n) time. 

So for each i, we look at the three positions and count W's. 

If the count is >=2, next state is W, else B. 

So for each i, next[i] = 'W' if (prev[(i-1)%n] + prev[i] + prev[(i+1)%n]).count('W') >=2 else 'B'. 

This is O(n) per step. 

But for n=2e5 and k=1e9, this is impossible. 

But wait, in the case where there are trios, perhaps the system stabilizes in O(1) steps. For example, in the first example, after one step, there are trios and the next step's state is the same as the current. 

Wait, no. Let's see the first example:

Input:

6 1

BWBBWW → "B","W","B","B","W","W"

After 1 iteration, the output is WBBBWW. Let's see what happens in step 2. 

For each position in WBBBWW (positions 0 to 5):

Position 0:

Neighbors are 5 (W) and 1 (B). Current is W. So the three are W, W, B → count W is 2. So next is W. 

Position 1: neighbors 0 (W), 1 (B), 2 (B). W, B, B → W count 1. Next is B. 

Position 2: neighbors 1 (B), 2 (B), 3 (B). All B. Next B. 

Position 3: neighbors 2 (B), 3 (B), 4 (W). B, B, W → count W is 1. Next B. 

Position 4: neighbors 3 (B), 4 (W), 5 (W). B, W, W → count W is 2. Next W. 

Position 5: neighbors 4 (W), 5 (W), 0 (W). All W. Next W. 

So next state is W B B B W W. Wait, but the previous state after iteration 1 was W B B B W W. So next state would be the same as current. So the system has stabilized. 

So after step 1, the state becomes W B B B W W. Then, in step 2, the state is the same. So after step 1, the system is already in a fixed point. 

Thus, simulating steps until the state stops changing is feasible. 

So, in code, after each step, we can compare the current state with the next state. If they are the same, then we can break early. 

So, for the case with trios, the code would:

prev = initial state.

for step in range(k):

   compute next state.

   if next == prev: break.

   prev = next.

output prev.

But comparing two strings of length 2e5 each time is O(n), which for each step could be O(n) per step. 

If the number of steps until stabilization is O(1) steps, then this is manageable. 

But how many steps could there be in the worst case? 

Another example: initial state has a single trio. How many steps until stabilization. 

Say n=200,000, and initial state is "W" followed by 199,999 B's. So, the first trio would be the three B's, but wait, no. The initial state is W followed by B's. The trio can't exist. 

Wait, this example is not a trio. 

Another example: n=5, initial state WWBWW. 

As discussed earlier, after one step, all become W. 

Another example: initial state is B B W B B B. 

Here, positions 3,4,5 (0-based?) are B's. So during the first step, they remain B. The rest may change. 

But perhaps after a few steps, the entire array becomes all B's. 

So, for the code, we can proceed as follows:

For the case with trios, simulate steps until the state stops changing. 

Each step:

- Generate the next state based on the current. 

- Compare the next state with the current. If same, break. 

Else, set current to next and proceed. 

Once the loop breaks, output the current state. 

But what if it takes 200,000 steps? For n=2e5, this would be O(2e5 * 2e5) = 4e10 operations, which is way too slow. 

So this approach is not feasible. 

Thus, this suggests that the initial idea is not correct, and we need to find another approach. 

Alternative Idea: When there are trios in the initial state, the system stabilizes in O(1) steps. But how? 

Looking back at the first example: after one step, the system stabilizes. 

In the example where the initial state is WWBWW (n=5), after one step, all become W. 

In the case of a trio, perhaps after one step, the trio's influence propagates to their adjacent positions, forming new trios, leading to the entire system stabilizing quickly. 

But how to model this. 

Alternative Idea: After each step, each trio in the current state may cause their neighboring positions to form new trios. So the number of trios increases, and after log n steps, the entire array is covered. 

But I'm not sure. 

Alternatively, once a trio exists, the next step will create new trios around them. 

For example, consider a trio of B's at positions i-1, i, i+1. 

In the next step, positions i-2 and i+2:

For position i-2, its neighbors are i-3, i-2, i-1. 

But if i-1 is B, and i-2's current color is (unknown), but perhaps after the trio step, some neighbors get fixed. 

Alternatively, perhaps the steps can be modeled in terms of blocks. 

Alternatively, perhaps after each step, the system can be represented as a set of intervals of the same color, and these intervals expand. 

But modeling this is complex. 

Another Idea: For each position, if it is part of a trio in the current state, then in the next state, its color remains the same. Otherwise, its color is determined by the majority of its trio. 

But this is not necessarily true. For example, if a trio is present in the current state, then their next color remains the same. 

Wait, yes. Because if a trio of three B's exists in the current state, then each of them has two B's as neighbors. So, their next state is B. Similarly for W's. 

So, once a position is part of a trio, it will remain that color forever. 

Thus, during each step, any position that is part of a trio will remain that color in all future steps. 

So, the key is to find for each position, the earliest step when it becomes part of a trio, and then determine its final color. 

But how to compute this for all positions. 

Ah, this is a crucial insight. 

Once a position is part of a trio (i.e., it and its two neighbors are the same color) at step t, then in step t+1, it will retain that color. And since its neighbors are also part of the trio, their colors also remain the same. Thus, in all future steps, this position remains the same. 

So, the process of stabilization is such that once a trio is formed, the positions in the trio are fixed. Their neighbors may then form trios in subsequent steps. 

Thus, the system stabilizes in O(n) steps. 

But how to model this. 

For example, in the first step, certain positions may form trios. Their neighbors may form trios in the next step. 

So, each step, new positions become part of trios and are fixed. 

Thus, after O(n) steps, all positions are part of trios. 

But again, for n=2e5, this would be O(n^2) steps. 

But wait, perhaps each step can process all positions and determine their next state, but for positions already in a trio, they are fixed. 

Thus, during step simulation, we can track for each position whether it is part of a trio, and if so, its color is fixed. 

But this requires checking trios in each step. 

Alternatively, since a position can become part of a trio only if its neighbors are the same as it. So, once a position is fixed, it can influence its neighbors. 

This suggests that the system stabilizes in O(n) steps. 

But how to compute this efficiently. 

Alternative Idea: For each position, the earliest step it becomes part of a trio can be computed. 

But this is non-trivial. 

Alternatively, perhaps we can model the process as follows:

For each step, the next state is determined by the current state. But for positions that are part of a trio in the current state, their next state is the same. For others, their next state is determined by the majority in their trio. 

So, the next state can be computed in O(n) time. 

But even so, for n=2e5, simulating O(n) steps would take O(n^2) time, which is not feasible. 

Thus, the problem is challenging. 

Alternative Idea: Note that after each step, the state changes only for positions not already in a trio. Once a position is in a trio, it never changes again. 

Thus, the number of steps needed is the maximum distance from a trio to any position. 

For example, if the initial state has a trio, then the changes propagate outwards, and each step can cover two more positions (left and right). 

Thus, the maximum number of steps needed is O(n/2). 

But this is still O(n) steps, which for n=2e5 is O(2e5) steps, each O(n) time. Which is O(4e10) operations—way too slow. 

Thus, this approach is not feasible. 

Thus, the problem requires a different approach. 

Wait, but perhaps the number of steps needed to stabilize is O(1) for all cases. 

For example, once a trio exists, after two steps, the entire array is filled with trios. 

But this is unlikely. 

Alternative Idea: For each position, if any of the three consecutive positions (i-1, i, i+1) in the initial state are the same, then the system will stabilize quickly. 

Alternatively, the problem requires us to find a way to compute the state after k steps without simulating each step. 

Another Idea: For each position, the state after k steps depends only on the initial state of positions within a certain distance from it. For example, after k steps, the state of position i is determined by the initial state of positions i -k, i -k +1, ..., i +k (mod n). 

But for k up to 1e9, this is not manageable. 

But perhaps the changes stabilize after a certain number of steps, so that after that, the state remains the same. 

Thus, the key is to find the state after which no more changes occur. 

But again, how to compute this. 

Alternative Idea: After the first step, the number of trios increases. Once all positions are part of a trio, the system is stable. 

Thus, the problem reduces to determining for each position, whether it can become part of a trio within k steps, and what its color would be. 

But how to model this. 

For example, a position i can become part of a trio if, in some step t, the positions i-1, i, i+1 (mod n) are the same. 

But this depends on the initial state and the propagation of changes. 

But this seems complex. 

Another Idea: Let's model the problem using the initial state and the presence of trios. 

If there are any trios in the initial state, then after each step, those trios' colors are fixed, and their neighboring positions may form new trios. 

Thus, the system stabilizes in at most (n + 1)/2 steps. 

For example, in the worst case, the trios propagate one step to the left and right each iteration. So after (n+1)/2 steps, the entire circle is covered. 

Thus, the maximum number of steps needed is O(n). 

But for n=2e5, this is 2e5 steps, each with O(n) processing. Which is 4e10 operations. Not feasible. 

Thus, this approach is not viable. 

Alternative Idea: Let's consider that the system stabilizes after at most log2(n) steps. For example, each step doubles the length of stable regions. 

But even then, log2(2e5) is about 18. So 18 steps would be manageable. 

But how to verify this. 

For example, imagine a line of B's with one W. But arranged in a circle. 

Wait, this may not be applicable. 

Alternatively, imagine a scenario where there's a single trio, and each step expands it by two positions. 

For example, initial state: ... B B B ... 

In the next step, the neighbors of the B's may also become B's. 

But this depends on their initial state. 

For example, initial state is B B B surrounded by W's. 

In the next step, the neighbors of the B's will see two B's and one W, so majority B. So they become B. 

So the trio expands by two positions each step. 

Thus, after O(log n) steps, the entire array is covered. 

But in this case, each step doubles the size of the B region. 

Thus, the number of steps needed is O(log n). 

For n=2e5, log2(n) is about 18. Thus, simulating 20 steps would be manageable. 

Thus, perhaps the code can simulate up to min(k, 100) steps and check for stabilization. 

If after 100 steps, the state hasn't stabilized, then it's either in a cycle of 2 steps or requires more steps. 

But for the case with trios, the state should stabilize in O(log n) steps. 

Thus, the code can simulate up to 200 steps (a safe upper bound) and then output the state. 

But how to determine when to stop. 

Thus, the code plan is:

- If there are no trios initially:

   - If k is even: output initial.

   - else: output flipped.

- Else:

   - Simulate up to min(k, 200) steps, or until the state stabilizes.

   - After each step, check if the next state is the same as current. If yes, output.

   - Otherwise, after min(k, 200) steps, output the current state.

But why 200? Because after 200 steps, even for n=2e5, the system should have stabilized. 

But this is a heuristic. 

But given the problem's constraints, this approach might work. 

Let's test this idea against the examples. 

In the third example, the initial state has no trios, so it's handled by the first case. 

In the first example, there are no trios initially, but after one step, there's a trio. 

Wait, no. The first example's input is BWBBWW. Let's check for trios:

B W B B W W. 

Looking for three consecutive same characters. 

B and W are different. W and B are different. B and B are same. B and W are different. W and W are same. 

So no three consecutive same. So the initial state has no trios. So according to the first case, the code would check if k is even or odd. 

But the first example's output after 1 step is WBBBWW. Which is not the initial nor the flipped. So the first example is in the case where the initial state has no trios. But the code's first case would handle it by flipping if k is odd. But in this case, after one step, the state is not the flipped initial. 

So this suggests that the initial approach is incorrect. 

This indicates a mistake in the previous reasoning. 

Ah, so what's wrong with the previous logic. 

The initial state has no trios. But after one step, the state may have trios. 

Thus, the initial plan to handle the no-trio case as flipping each step is incorrect. 

So the previous approach is wrong. 

Thus, the initial assumption that if the initial state has no trios, then each step flips all colors is incorrect. 

This is a critical error. 

So, the previous idea is invalid. 

Thus, we need to think again. 

The third example's initial state is BWBWBW (n=6). No trios. Each step flips all colors. 

But the first example's initial state is BWBBWW (n=6). Let's check if there are any trios:

Positions 3,4,5 (0-based?) Let's see:

Original string is B W B B W W. 

Positions 0: B, 1: W, 2: B, 3: B, 4: W,5: W. 

So no three consecutive same. Thus, no trios. 

After one step, the output is W B B B W W. 

So in this step, the code would have flipped each character if the initial state has no trios and k=1 is odd. 

But the actual output is W B B B W W, which is not the flipped version of the initial. 

Initial state is B W B B W W. Flipping each character would give W B W W B B. 

But the actual output after one step is W B B B W W. 

Thus, the initial approach is incorrect. 

Thus, the assumption that when there are no trios, each step flips all colors is wrong. 

Thus, the previous approach is invalid. 

Thus, we need to re-examine the problem. 

So the key is that when there are no trios, the system may not flip all colors. 

Thus, the initial plan is invalid, and we need to find a different approach. 

Thus, the problem requires a different approach. 

Alternative Idea: For each position, determine the state after k steps based on the initial state of its neighborhood. 

But given the problem's time constraints, this is only feasible if the state can be determined in O(1) time per position. 

But how to model this. 

Each step, the state of a position is determined by the previous state of three positions. 

This is similar to a cellular automaton with a rule that depends on three neighbors. 

For k steps, the state of position i depends on the initial state of positions i - k, i -k +1, ..., i +k. 

But for k up to 1e9, this is not feasible. 

But perhaps the state stabilizes after a certain number of steps, and beyond that, it remains the same. 

Thus, the solution is to simulate until the state stabilizes or until k steps, whichever comes first. 

But how to do this efficiently. 

The main challenge is to compute each step efficiently. 

But for n=2e5, each step is O(n), and if the number of steps is O(100), then it's manageable. 

Thus, the code would:

Simulate each step up to k steps, or until the state stabilizes. 

But how to compute the next state efficiently. 

In Python, strings are immutable, so for each step, we need to create a new string. For n=2e5, this is O(n) per step. 

But for 100 steps, this is 2e7 operations, which is manageable. 

But how to compute the next state. 

Here's how to compute the next state:

For each position i (0-based), the next state is determined by s[i-1], s[i], s[i+1], where the indices are modulo n. 

We can precompute a list of the current state as a list of characters. 

Then, for each step, create a new list where each element is 'W' if the count of 'W's in the three positions is >=2. 

So, code snippet:

current = list(initial)
n = len(current)
for _ in range(k):
    next_state = []
    for i in range(n):
        left = current[(i-1) % n]
        right = current[(i+1) % n]
        me = current[i]
        count = (left == 'W') + (me == 'W') + (right == 'W')
        next_char = 'W' if count >= 2 else 'B'
        next_state.append(next_char)
    # check if next_state is same as current
    if next_state == current:
        break
    current = next_state
    # check if it's the same as two steps back, etc. But how?

But for n=2e5 and k=1e9, this is O(nk) time, which is impossible. 

But in practice, if the state stabilizes after a few steps, then the loop breaks early. 

But what if the system enters a cycle of 2 steps? 

Like the third example, where the state flips each step. 

In this case, the code would loop k steps, but for k=1e9, this is impossible. 

Thus, the code must handle cycles. 

But how to detect them without storing all previous states. 

Thus, the problem requires two cases:

1. The state stabilizes into a fixed point. 

2. The state enters a cycle of 2 steps. 

In the first case, once the state is stable, break and return. 

In the second case, compute whether the remaining steps are even or odd. 

Thus, the code must:

- Simulate steps until either:

   a. The next state is the same as the current (fixed point). 

   b. The next state is the same as the state two steps back (cycle of 2). 

   c. k steps are done. 

But to detect cycles of 2, we need to compare the current state with the state from two steps ago. 

But storing two previous states would require O(2n) space. 

Thus, the code can track the previous two states. 

Here's the plan:

prev_prev = None

prev = initial_state

current = initial_state

for step in range(k):

    compute next_state. 

    if next_state == current:

        break

    if prev_prev is not None and next_state == prev_prev:

        remaining = k - step - 1

        if remaining % 2 == 0:

            current = next_state

        else:

            current = prev

        break

    prev_prev = prev

    prev = current

    current = next_state

else:

    # k steps done

    current = next_state

Thus, this code checks for fixed points and cycles of 2. 

But comparing the entire state each time is O(n) per step. 

But if the number of steps needed to detect a cycle is small (like 100), then it's manageable. 

For example, if after 100 steps, the code has not found a fixed point or a cycle, then it's unlikely to find one later. But this is not certain. 

But given the time constraints, this approach is the best possible. 

Thus, the code should:

- Check for each step if the next state is the same as current (fixed point) or the same as the state two steps back (cycle of 2). 

- If a cycle of 2 is detected, compute the remaining steps modulo 2 and return the appropriate state. 

- Otherwise, continue simulating steps up to k times. 

But for large n, this approach's time complexity depends on how many steps are needed to detect a cycle. 

But given the problem's time constraints, this is the only feasible approach. 

Thus, the code will look like this:

Read n and k.

Read the initial string.

current = list(initial)

prev_prev = None

prev = None

remaining_steps = k

for step in range(k):

    next_state = []

    for i in range(n):

        left = current[(i-1) % n]

        right = current[(i+1) % n]

        me = current[i]

        count = (left == 'W') + (me == 'W') + (right == 'W')

        next_char = 'W' if count >= 2 else 'B'

        next_state.append(next_char)

    # Check for fixed point

    if next_state == current:

        break

    # Check for cycle of 2

    if prev is not None and next_state == prev:

        # The current step is step+1 (0-based step)

        remaining_steps = k - (step + 1)

        if remaining_steps % 2 == 0:

            current = next_state

        else:

            current = prev

        break

    # Update previous states

    prev_prev = prev

    prev = current

    current = next_state

# Output current as a string

print(''.join(current))

But this code has a problem: 'prev' is assigned the previous current state, not the previous step. 

Wait, let's track the variables:

Initially, current is the initial state. 

prev is None. 

prev_prev is None. 

In the first iteration (step=0):

next_state is computed. 

Check if next_state == current (fixed point). 

If not, check if prev is not None and next_state == prev. But prev is None, so no. 

Then, prev_prev becomes prev (None), prev becomes current (initial state), current becomes next_state. 

In the next iteration (step=1):

compute next_state again. 

Compare with current (which is the next_state from step 0). 

If not equal, check if next_state == prev_prev (which is None, so no). 

Update prev_prev to prev (initial state), prev to current (step0's next_state), current becomes step1's next_state. 

After two steps, prev_prev is initial state, prev is step0's next_state, current is step1's next_state. 

When we compute step2's next_state, and if it equals prev_prev (initial state), then we have a cycle of 2. 

Thus, the code is correct. 

But for large n, this code could take O(n) per step, which is not feasible for large k. 

Thus, the code is only feasible if the number of steps simulated is small. 

But given the problem's time constraints, it's the only possible way. 

Testing this code against the examples:

First example:

Input: 6 1 BWBBWW → 'B','W','B','B','W','W'

Step 0:

next_state is computed. 

Each position's next state is determined. 

The code compares next_state with current. If they are different, proceed. 

Since step is 0, remaining_steps is k=1. 

After step 0, current becomes next_state. 

Thus, after one step, the code outputs the correct result. 

Second example: 7 3 WBWBWBW → 'W','B','W','B','W','B','W'

After each step, the state changes. 

After 3 steps, all become W. 

The code would simulate 3 steps. 

Third example: 6 4 BWBWBW → after two steps, it returns to the initial state. 

Thus, after two steps, a cycle of 2 is detected. 

remaining_steps = 4 - steps taken. 

Let's see:

initial state: B W B W B W

step 0:

next_state: W B W B W B 

step 1:

next_state: B W B W B W 

check if next_state == current (W B W B W B): no. 

check if next_state == prev (B W B W B W, which is the initial state). 

Yes. 

remaining_steps = 4 - 1 - 1 = 2. 

remaining_steps % 2 = 0. 

Thus, current is set to next_state (B W B W B W). 

Thus, after two steps, the code breaks and outputs B W B W B W. 

Which matches the third example. 

Thus, the code works for the examples. 

But for the first case where there are no trios, but the system doesn't flip all colors each step, this code correctly simulates the steps until a cycle is found. 

Thus, the code should handle all cases. 

But the code's performance depends on the number of steps simulated. 

For large n and k, if the system stabilizes after a few steps, the code is efficient. 

Otherwise, for systems with large cycles, it's not. 

But given the problem's time constraints, this is the best possible approach. 

Thus, the final code is as above.
</think>

```python
n, k = map(int, input().split())
s = list(input())
current = s.copy()
prev = None
prev_prev = None
steps_done = 0

for steps_done in range(k):
    next_state = []
    for i in range(n):
        left = current[(i-1) % n]
        right = current[(i+1) % n]
        me = current[i]
        count = (left == 'W') + (me == 'W') + (right == 'W')
        next_char = 'W' if count >= 2 else 'B'
        next_state.append(next_char)
    if next_state == current:
        break
    if prev is not None and next_state == prev:
        remaining = k - steps_done - 1
        if remaining % 2 == 0:
            current = next_state
        else:
            current = prev
        break
    prev_prev = prev
    prev = current.copy()
    current = next_state
    if steps_done >= k - 1:
        break

print(''.join(current))
```