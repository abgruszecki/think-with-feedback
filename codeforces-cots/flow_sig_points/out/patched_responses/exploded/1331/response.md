<think>
Okay, let's see. I need to solve this problem where there are n pairs of boys and girls in a circle. The boys move around based on the commands given. The challenge is to compute the final positions after all q commands efficiently, especially considering the constraints where n and q can be up to a million or two million. So, brute-force methods won't work here. I have to find a smart way to track the boys' positions without simulating each command step by step.

First, let's understand the problem. Initially, each boy i is paired with girl i. Girls stay in their positions. Boys move in two types of commands. The first type is moving x positions clockwise or counter-clockwise (depending on x's sign). The second type swaps the positions of boys in even and odd indices. But wait, the problem says that during the second command, the boys dancing with even-indexed girls swap with those in odd-indexed girls. So, for even i (like 2,4,6...), the boys swap with the previous (i-1) girl's partner. But wait, the example might help. Let's look at the first example:

Input 6 3, commands are 1 2 (move 2 positions clockwise), then 2 (swap even and odd pairs), then 1 2 again. The output is 4 3 6 5 2 1.

Let's break it down. Initial positions: boy i is with girl i.

After first command 1 2: each boy moves 2 positions clockwise. Since the girls are arranged in a circle, moving clockwise increases their position. So boy 1 would be at position 1 + 2 = 3 (girl 3), but wait, the movement is for boys. Wait, the girls are fixed. So when a boy moves x positions clockwise, his current position (girl) is increased by x. But since it's a circle, we take modulo n. But how exactly? Let's think.

If a boy moves x positions clockwise, the girl he is paired with increases by x, but since the girls are arranged in a circle, adding x and then mod n (with 1-based to 0-based or vice versa?). For example, if a boy is at girl 6 (n=6) and moves 2 positions clockwise, he ends up at (6 + 2) mod 6 = 8 mod6=2. But 6 is the last girl, so moving 1 position clockwise would take him to 1. Wait, maybe the girls are arranged in a circle, so moving clockwise means that the next girl is i+1. So for a boy, moving x positions clockwise would add x to his current girl index. But since the girls are arranged in a circle, this is mod n. But since the girls are numbered 1 to n, perhaps we need to adjust for 1-based indices.

Wait, the girls are arranged in a circle in the clockwise direction. So when a boy moves x positions clockwise, he moves from his current girl to the girl that is x steps ahead. For example, if he's at girl 1, moving 2 steps clockwise would take him to girl 3. But if he's at girl 6 (n=6), moving 2 steps takes him to girl 2 (since after 6 comes 1, then 2). So the calculation would be (current + x) mod n. But since the indices are 1-based, perhaps it's (current - 1 + x) mod n + 1. Because in 0-based, adding x and mod n gives the correct position, then adding 1 brings it back to 1-based. For example, current is 6 (1-based), subtract 1 to get 5, add x=2 gives 7, mod 6 is 1, add 1 gives 2. Which matches the example. So the formula for moving x positions clockwise would be (current_pos -1 + x) % n + 1. Similarly, moving x positions counter-clockwise would be equivalent to moving -x positions clockwise. Because moving counter-clockwise by x is the same as moving clockwise by (n -x) mod n. So for a command of type 1 with x, which can be positive (clockwise) or negative (counter-clockwise), the total shift is x. So, for each boy, their position is updated as (current_pos -1 + x) mod n +1.

But handling this for all boys could be O(n) per command, which is way too slow when q is 2e6. So we need a way to track the shifts without processing each boy individually.

Now, the second type of command is swapping even and odd pairs. For even i (like 2,4,6...), the boy at i swaps with the boy at i-1. So after this command, the girl i-1 is paired with the boy that was at i, and girl i is paired with the boy that was at i-1. But how does this affect the overall state?

Let me think: after a swap, the boys in even positions swap with the previous (odd) positions. So for all even i, swap i-1 and i. For example, in the first example after the first command (shift by 2), each boy's position is shifted by +2. Then, the swap happens. Then another shift of +2.

But processing each swap for even pairs would again be O(n) per command, which is not feasible. So again, we need a way to represent these swaps in a way that can be applied in bulk.

Hmm. The key here is to model the effect of these commands as transformations on the positions of the boys, and find a way to track the net effect of all commands, then apply them once to each boy's initial position.

So the initial position of boy i is i. So girl i is paired with boy i. But after a series of shifts and swaps, the boy's positions change. But how can we model this efficiently?

Let's consider that each boy's position can be represented as a function of their initial position. For example, each command applies a transformation to their current position. The challenge is to find the composite transformation after all commands, then apply it to the initial position of each boy.

But how to model the transformations. Let's think:

Initially, each boy's position is their own index. So for boy i, pos = i.

Each command of type 1 (shift) adds x to their position (mod n, with 1-based). But when there are swaps (type 2 commands), the order in which the shifts and swaps are applied matters.

Wait, but the swaps are between even and odd indices. For example, after a swap, the boy who was in position i (girl i) might have moved to i-1 or i+1, depending on whether i is even or odd. Then, any subsequent shifts will affect his new position.

So, the transformations are applied in sequence. The problem is to model these transformations in a way that allows us to compute the final position of each boy efficiently.

But considering the commands are applied in order, and each command can be either a shift or a swap, we need to track how each command affects the current mapping from the initial position to the current position.

Alternatively, perhaps we can track the transformations as a combination of shifts and swaps. Let's consider that each swap operation inverts the parity of the positions. For example, after a swap, a shift in the opposite direction may be needed, but perhaps we can model the swaps as a parity change.

Wait, let's think of it in terms of transformations. Let's track two variables: a shift offset (delta) and a flag indicating whether the current parity is even or odd (due to swaps). For example, after an even number of swaps, the parity is back to normal, but after an odd number of swaps, the positions are swapped between even and odd pairs.

But how can the swaps and shifts be combined?

Suppose that we have a current shift delta and a swap state (even_swapped). For each command:

- If it's a shift by x: we add x to delta. But we have to consider the current swap state. Because after swaps, the direction of the shift may be modified. For example, if after a swap, the even and odd pairs are swapped, then a shift of x would affect the positions as if the even and odd pairs were in their original positions.

Wait, maybe not. Let me think again. Let's model the swap as a permutation of the boys. Each swap command toggles the parity of the positions. For example, after a swap, the boys in even positions are swapped with their previous odd positions. Then, the next shift is applied to the current positions of the boys, which are now in a swapped state.

But if we can model the swap as a permutation that can be combined with the shift, perhaps we can track the overall effect using some variables.

Alternatively, think of the swap as a transformation that affects the way shifts are applied. For example, after a swap, applying a shift of x is equivalent to applying a shift of x but in the opposite parity.

Alternatively, let's model the problem with a shift and a swap count (even or odd). Each swap toggles the parity. Then, when applying shifts, the actual shift depends on the current swap parity. For instance, when the swap parity is even, shifts are applied normally. When the swap parity is odd, the shift direction may be reversed for even and odd positions.

Wait, maybe not. Let me think of an example.

Suppose we have a swap (command 2). After that, the even and odd pairs are swapped. So, the boy at position 1 is now at position 2, and vice versa. Then, a shift of x would affect these swapped positions. So, the shift is applied to the current positions of the boys.

But how can we model this in terms of shifts and swaps? Let's consider that each swap inverts the parity. So, after an even number of swaps, the parity is back to original. After an odd number, it's swapped.

Now, the shift is applied to the current positions. But when the parity is swapped, the shift's effect on the even and odd positions may be different. For example, suppose we have a swap followed by a shift. Let's model this.

Original positions: boy 1 at 1, boy 2 at 2, etc.

After swap command (type 2):

boy 1 is now at position 2, boy 2 at 1, boy 3 at 4, boy 4 at 3, etc.

Then, a shift of x. So each boy moves x positions clockwise. The current positions are 2,1,4,3,6,5 (for n=6). Adding x=2:

Each position is (current_pos +x) mod n. So for the first boy (current pos 2), 2+2=4 mod6=4. The second boy (current pos 1), 1+2=3 mod6=3. Then, their positions are 4,3,6,5, 2,1. Which is the result after the first two commands in the first example.

But how can we model this without tracking each boy's position?

Hmm. So the problem is that after swaps, the positions are permuted. Then shifts are applied to those permuted positions. So the overall effect is a combination of the permutation (swaps) and the shifts.

This suggests that we need to track the permutation applied so far, and the shifts. But permutations can be represented as functions, but combining them with shifts might be tricky.

Alternatively, perhaps we can track two variables: the shift delta and the swap parity. Then, for each boy's initial position, we can compute their final position based on these variables.

Wait, here's an idea. Let's model the effect of all commands as a function that, given the initial position of a boy (i), returns his final position. This function can be represented as a combination of shifts and swaps.

Let's track the cumulative shift (delta) and the number of swaps (swap_count). But how do swaps interact with shifts?

Let's think in terms of a boy's position. Each swap command inverts the parity. So, for a boy in position j, after a swap, if j is even, he moves to j-1, and if j is odd, he moves to j+1 (assuming j is even and odd in the original positions). Wait, not exactly. Because the swap is between even and odd pairs. So for even i (girls), the boys swap with the previous (i-1) girl's partner. So for even i, the boys at i and i-1 swap positions.

So, for each even i (girls 2,4,6...), the boy who was at i-1 is now at i, and the boy who was at i is now at i-1. So for each pair of even and odd girls (like 2 and 1, 4 and 3, etc.), their boys are swapped.

So, after a swap, the boys in even positions (i) are swapped with the boys in i-1 positions.

So, the swap can be represented as a permutation: for each even i, swap i and i-1.

Now, the challenge is to model the effect of multiple swaps and shifts on the positions of the boys. Let's see.

Each swap (type 2 command) toggles the permutation state. So, for example, after one swap, the permutation is applied. After another swap, it's reversed. So, the swap state can be represented as a boolean (even_swapped) indicating whether the current permutation is in the swapped state (even and odd positions are swapped).

Each shift (type 1 command) adds a delta to the current positions. However, this delta is applied after considering the current permutation state.

Wait, but the shifts are applied after any previous permutations. So, the order of operations matters. For example, a swap followed by a shift is different from a shift followed by a swap.

So, the problem is that the permutations (swaps) and shifts are applied in sequence. We need to find a way to track the cumulative effect of these operations.

Let's think of it as a series of transformations. For each command, we can track how it affects the current state. The state can be represented by a shift delta and a swap parity (even_swapped, which can be 0 or 1). Let's model the state with these two variables.

Initially, delta is 0 and even_swapped is False (no swaps).

For each command:

- Type 1 (shift x):

If even_swapped is False, then the shift is added to delta as x.

But wait, if even_swapped is True, then applying a shift x would have a different effect. Because in the swapped state, the boys' positions are permuted. So, a shift x in the swapped state is equivalent to shifting each pair of even and odd positions in a certain way. Wait, this seems complicated.

Alternatively, perhaps when even_swapped is True, the direction of the shift is reversed for even and odd positions.

Alternatively, perhaps we can model the shift delta as being applied in the current permutation state. For example, if the current permutation is even_swapped, then the shift is applied to the permuted positions, which is equivalent to first unpermuting the shift, then applying the permutation again. Let's think in terms of function composition.

Let me denote the permutation caused by a swap as S. Then, a shift of x (operation T_x) can be applied, and when the current state is S, the effect of T_x followed by S would be S o T_x. Wait, but the order is reversed. Because if you first apply T_x and then S, the composite would be S(T_x(p)), which is S applied to the result of T_x on p.

Alternatively, if the current state is a permutation S, and a new operation is a shift T_x, then the composite transformation would be T_x followed by S. Wait, no. The current state is that all positions are transformed by S. Then, applying a shift T_x would mean that each position is first shifted by x, then permuted by S. Wait, no. Wait, the current state is that each boy's position is S(p), where p is the original position (after all previous operations). Then, applying a shift would take the current position (S(p)), add x (mod n), then that's the new position. But the shift is applied after the permutation S.

Wait, maybe I'm overcomplicating. Let's think of each operation as a function that transforms the current position of a boy. So, for a given boy's initial position i, after all operations, his final position is the result of applying all the command operations in sequence.

Each command is a function that takes a current position and returns a new position.

For a command of type 1 (shift x), the function is: pos = (pos + x) mod n.

For a command of type 2 (swap even and odd), the function is: if pos is even, then pos becomes pos -1; if pos is odd, then pos becomes pos +1. But wait, for example, if a boy is in position 2 (even), after a swap, he moves to position 1. If in position 1 (odd), he moves to 2. Similarly, positions 3 and 4 swap, etc. So the function is: for any position, if it's even, subtract 1; if it's odd, add 1. But this is only for even n, which the problem states. So for even n, this function is valid. However, after swapping, the even and odd pairs are swapped. So for example, after a swap, the next swap would swap them back.

So, the swap function can be represented as: swap(pos) = pos + 1 if pos is odd, pos - 1 if pos is even.

But this is the same as: swap(pos) = pos + (-1)^(pos % 2 + 1). For example, even pos (mod 2 is 0) → subtract 1. Odd → add 1.

But the swap function is its own inverse. Applying it twice brings the position back to the original. So, applying two swaps is equivalent to doing nothing.

But when multiple swaps and shifts are applied, the order matters. For example, a shift followed by a swap is different from a swap followed by a shift.

But how can we model this efficiently for all possible combinations?

Let's think of the transformations as permutations and shifts. The key insight here is that shifts and swaps can be represented in a way that allows us to track their combined effect without having to process each boy's position individually.

Let's track two variables:

- delta: the total shift that has been applied. However, this delta is adjusted based on the swap state.

- swap_count: the number of swaps performed, modulo 2 (since two swaps cancel each other). So swap_count can be 0 or 1.

The idea is that applying a swap toggles the swap_count (even_swapped state). The delta is adjusted in such a way that when a swap is applied, the delta's direction is inverted for even and odd positions.

Wait, perhaps not. Let's see.

Suppose we have a swap_count of 0 (no swaps). Applying a shift x would add x to each boy's position. If there's a swap (swap_count becomes 1), then the next shift would have to account for the swapped positions.

Alternatively, when swap_count is even, the shift is applied as normal. When it's odd, the shift is applied in a way that accounts for the swapped even and odd positions.

But how?

Alternatively, when swap_count is even, the current positions are not swapped, and a shift x is applied normally. When swap_count is odd, each position is in swapped state, so a shift x would have to be applied to the swapped positions. But how can we model this without tracking each position?

Wait, perhaps the delta can be adjusted based on the swap_count. For example, if there's a swap, then the delta's direction is reversed for even and odd positions. But this seems complex.

Alternatively, consider that each swap inverts the parity of the positions, so when a shift is applied, the direction depends on the current swap_count. For example, when swap_count is even, a shift x is applied as usual. When swap_count is odd, applying a shift x is equivalent to applying a shift -x, but only for even positions.

Wait, that might not be correct. Let me think with an example.

Suppose after a swap (swap_count is 1), the boys are in swapped positions. Then, a shift x is applied. For example, let's say after swap, the boy originally in position 1 is now at position 2. Then a shift x of 2 would take him to position 4 (2+2=4). But if the swap had not been applied, the shift x would have taken him to 3 (1+2=3). So the delta is added to the swapped positions.

But how can this be modeled as a combination of delta and swap_count?

Alternatively, the delta can be adjusted based on the swap_count. Let's see. For a swap_count of 1, the current positions are swapped even and odd. So, when applying a shift x, it's equivalent to applying the shift x in the swapped state. But how to model this in terms of delta and swap_count.

Wait, perhaps when a swap is applied, the direction of the delta for even and odd positions is reversed. For example, in swapped state, a shift x would effectively be applied as x for even positions and -x for odd positions. But this might not be the case.

Alternatively, let's model the delta and swap_count as parameters that, when applied to the initial position i, compute the final position. The key is to find a formula that, given i, delta, and swap_count, returns the final position.

Let's try to derive such a formula.

Suppose initial position i. Then, after some swaps and shifts, the final position is computed as follows:

If swap_count is even (0 mod 2):

final_pos = (i + delta) mod n.

If swap_count is odd (1 mod 2):

Each swap toggles the parity. So after one swap, the position i becomes i+1 if i is odd, i-1 if i is even.

But after that, applying a shift x would change the position to:

for swap_count=1:

current_pos after swap: j = i + 1 if i is odd, i-1 if i is even.

Then, add delta: j + delta mod n.

But this is the same as (swap(i) + delta) mod n, where swap(i) is i+1 if odd, i-1 if even.

But then, applying another swap would swap the position again.

So, if swap_count is even, the swap operations cancel each other. For swap_count even, the final swap operations can be ignored. For swap_count odd, we have to apply the swap once.

So, the formula would be:

if swap_count is even:

final_pos = (i + delta) mod n.

if swap_count is odd:

final_pos = swap( (i + delta) mod n )

But wait, no. Because the order of operations matters. The swaps and shifts are applied in sequence. For example, a shift followed by a swap would be different from a swap followed by a shift.

So, the formula depends on the order in which swaps and shifts are applied.

But how can we model this with delta and swap_count?

Hmm. Let's think of the delta and swap_count as accumulated variables that can track the effect of all commands up to now. Each new command modifies these variables accordingly.

When a new command is processed:

If it's a type 1 (shift x):

delta += x (but possibly adjusted for the current swap_count).

Wait, but how does the swap_count affect the delta. For example, if there have been an odd number of swaps, then the delta is applied to the swapped positions. So, the delta is added to the current positions, which are swapped.

But we need to find a way to represent the delta in such a way that after all swaps and shifts, the final positions can be computed by a formula that uses delta and swap_count.

Alternatively, let's model the transformations as follows:

Each swap command toggles the swap_count (even or odd).

Each shift command adds x to the delta, but if the current swap_count is odd, the shift is applied in a way that depends on the parity of the current position.

Wait, this might be possible. Let's try to model this.

Let me think: the delta is a value that accumulates the total shift, but in a way that depends on the swap_count. For example, when swap_count is even, the delta is added normally. When swap_count is odd, the delta is added but with a direction that alternates between even and odd positions.

Alternatively, when swap_count is odd, applying a shift x is equivalent to adding x for even positions and subtracting x for odd positions, but this seems complicated.

Alternatively, perhaps when swap_count is even, the delta is added as x. When swap_count is odd, the delta is added as x multiplied by the parity (even or odd) of the position. But I'm not sure.

Alternatively, think of the swap as a permutation that is applied after all previous shifts. So, when a swap occurs, the current delta is applied to the permuted positions.

Wait, this is getting complicated. Maybe we need to model the delta and swap_count in such a way that the final position for each boy can be computed as:

final_pos = swap_count_parity ( (i + delta) mod n )

where swap_count_parity is the number of swaps (mod 2). If swap_count is even, no swap is applied. If odd, the swap is applied once.

But this assumes that all swaps are applied after all shifts, which may not be the case.

Wait, but if we can model the cumulative effect of the commands as if all swaps are applied first, then all shifts. But that's not possible because the order of commands can be arbitrary.

Alternatively, perhaps each swap can be modeled as a transformation that affects the delta. For example, when a swap is performed, the direction of the delta is reversed for even and odd positions.

Let me try to work through an example.

Case 1: swap followed by shift.

Original i=1:

After swap: i=2.

Shift x=2: becomes 2+2=4.

Final position:4.

Case 2: shift followed by swap.

Original i=1.

Shift x=2: becomes 3.

Swap: 3 is odd → becomes 4.

Final position:4.

So, same result. Hmm. So maybe in this particular case, the order doesn't matter. But this may not hold for other cases.

Another example.

Case 1: swap, shift x=1.

i=2:

swap: becomes 1.

shift x=1 → 2.

Final position:2.

Case 2: shift x=1, swap.

i=2: shift becomes 3.

swap: 3 is odd → becomes 4.

Final position:4.

Different results. So the order of swap and shift matters. So how can this be modeled?

Therefore, the order of operations is crucial. So the approach of representing the final position as (i + delta) mod n, followed by a swap if swap_count is odd is incorrect.

Hence, we need a way to track how swaps and shifts are interleaved.

Hmm. So perhaps the solution is to track two separate shifts: one for even positions and one for odd positions. Because each swap operation swaps even and odd positions, and shifts after a swap would affect even and odd positions differently.

But even that might not be manageable, but let's think.

Suppose we have even_shift and odd_shift variables. Each shift command adds x to even_shift and odd_shift. But when a swap occurs, the even_shift and odd_shift are swapped. Because after a swap, the even positions become odd and vice versa, so their shifts are swapped.

For example:

Initially, even_shift=0, odd_shift=0.

Apply shift x=2: even_shift=2, odd_shift=2.

Apply swap: even_shift and odd_shift are swapped. Now even_shift=2, odd_shift=2 (since they were the same). So no change.

But then apply another shift x=3: even_shift=5, odd_shift=5. So again, same.

But this doesn't model the example where order of swap and shift matters.

Alternatively, when a swap occurs, the even and odd shifts are swapped. So:

Suppose even_shift and odd_shift track the shifts for even and odd positions. After a swap, even positions become odd, and vice versa, so their shifts are swapped.

Let's model this.

Each shift command of x would add x to both even_shift and odd_shift, but considering the current swap state. Wait, maybe not. Let's see:

Initially, even_shift is 0 and odd_shift is 0. swap_count is 0.

A command of type 1 (shift x) adds x to both even_shift and odd_shift. Because all boys are shifted by x, regardless of their current position's parity.

Then, when a swap occurs (command type 2), the even_shift and odd_shift are swapped, and swap_count is toggled.

Wait, perhaps not. Let me think. Let's say after a swap, the even and odd positions are swapped. So any shifts applied after the swap would affect the new even and odd positions. So, to model this, when a swap occurs, we need to swap the even_shift and odd_shift variables. Because now, what was even_shift (applied to even positions) will now apply to odd positions, and vice versa.

So for example:

Initially, even_shift=0, odd_shift=0, swap_count=0.

Apply shift x=2: even_shift=2, odd_shift=2.

Apply swap: even_shift and odd_shift are swapped → even_shift=2, odd_shift=2 (no change, since they are the same). swap_count=1.

Apply shift x=3: even_shift=5, odd_shift=5.

Another swap: even_shift and odd_shift are swapped again (no change), swap_count=0.

So final shifts are 5 and 5. So each boy's position is i +5 mod n.

But how does this model account for the swaps and shifts in the correct order?

Let's try the example where order matters:

Example:

Case 1: swap then shift.

swap_count=1.

Shift x=1. So even_shift and odd_shift are added x=1. But after the swap, even_shift is applied to odd positions and vice versa.

Wait, perhaps not. Let's model it:

swap_count starts at 0.

Command 2 (swap): swap_count becomes 1. even_shift and odd_shift are swapped. Initially, they were 0, so no change.

Command 1 (shift x=1): since swap_count is 1, adding x=1 to even_shift and odd_shift. So even_shift =1, odd_shift=1.

But after a swap, even_shift and odd_shift are for the swapped positions. So when swap_count is 1, even_shift is the shift to apply to the current even positions (which were originally odd). So when applying the shift, it's added to both even_shift and odd_shift.

Hmm, perhaps this model is not capturing the required behavior. Let's take an example where order matters.

Example: n=2, commands are swap then shift x=1.

Original positions: boy 1 at 1, boy 2 at 2.

After swap: boy 1 at 2, boy 2 at 1.

Shift x=1: each boy moves 1 position clockwise. Boy at 2 → 3 mod 2 =1. Boy at 1 →2. So final positions are 1 and 2. So girls 1 and 2 are paired with boys 1 and 2 again. So output is 1 2.

Another example: shift x=1 then swap.

Original positions: 1 and 2.

Shift x=1: boys are at 2 and 3 mod2=1. So positions are 2 and 1.

Swap: swap even and odd positions. So boy at 2 (even) swaps with 1 (odd). So positions are 1 and 2. Same as previous example.

So in this case, the order didn't matter. But earlier example where order matters.

Another example: n=4.

Command 1: shift x=1. Then command 2: swap. Then command 3: shift x=1.

Original positions: 1,2,3,4.

After shift x=1: 2,3,4,1.

Swap: even and odd pairs are swapped. So positions become 3,2,1,4, 1 → swapped in pairs. Wait, the swap is between even and odd pairs. So for n=4, the pairs are (1,2), (3,4).

After swap, the boys in even positions (2,4) swap with their previous odd partners (1,3). So positions become:

Girl 1: boy 2, girl 2: boy1, girl3: boy4, girl4: boy3.

Then shift x=1: each boy moves 1 position clockwise. So boy 2 is at girl3, boy1 at girl2, boy4 at girl4+1=1 mod4=1, boy3 at girl4+1=5 mod4=1. So girls' partners after shift are:

1: 4 (from boy4), 2:1+1=2, 3:2+1=3 mod4=3, 4:3+1=4. So final positions are 4,2,3,4. Wait, this is getting complicated. Maybe this model isn't the right approach.

Alternative approach: For each boy, the final position can be determined by applying all commands in order. But with n up to 1e6 and q up to 2e6, this is O(qn) which is way too slow. So we need a way to model the commands as a function that can be applied to each boy's initial position in O(1) per boy.

The key is to find that function.

Let's model the commands as a series of transformations.

Each command is either a shift or a swap.

Let's denote the current position of a boy as p.

For each command:

If it's a shift x: p = (p + x) mod n.

If it's a swap: p = p + 1 if p is odd, p-1 if p is even.

But applying these transformations directly for all q commands would take O(q) per boy, which is O(nq) total time. This is not feasible for large n and q.

So, we need to find a way to compute the final position for each boy by composing all commands into a single transformation.

The problem is to find this composed transformation.

Let's consider that after applying all commands, the final position for a boy i is given by:

final_p = (swap_q ( swap_{q-1} ( ... swap_1 ( (i + delta) mod n ) ... ) )) )

But this is not helpful.

Alternatively, let's track the cumulative effect of swaps and shifts. The challenge is to find how the order of swaps and shifts can be represented in terms of delta and swap_count.

Let's think of it as a permutation. Each swap is a permutation S, and each shift is a permutation T_x. The final permutation is the composition of all commands, which are permutations in order.

But since the commands are applied in sequence, the final permutation is T_xk ... S_j T_x1 S_1 ... etc.

But for large q, we need a way to represent this composition efficiently.

But how to model the composition of swaps and shifts?

Another idea: each swap toggles a flag (even_swapped). The delta is adjusted based on the flag. For example:

When even_swapped is True, the delta is applied in reverse direction for even and odd positions. But how?

Alternatively, we can track the delta and even_swapped, and compute the final position for a boy i as follows:

if even_swapped:

    i = swap(i)

i = (i + delta) % n

if even_swapped:

    i = swap(i)

But this is incorrect because the order of swaps and shifts depends on the sequence of commands.

Wait, perhaps we can model the final position as:

After applying all swaps and shifts in order, the final position is:

p = (initial_p + delta) mod n.

Then, if even_swapped is True, apply the swap once.

But this would only be the case if all swaps are applied after all shifts, which is not necessarily true.

But in the example where swaps and shifts are interleaved, this would give the wrong result.

But perhaps this model can be adapted by adjusting delta and even_swapped in a way that accounts for the order of operations.

Let's try to model delta and even_swapped:

Initially, delta =0, even_swapped = False.

For each command:

If type 1 (shift x):

   if even_swapped is False:

       delta += x

   else:

       delta -= x

Because when even_swapped is True, the shift direction is reversed for even and odd positions. Wait, but this might not be accurate.

Alternatively, when even_swapped is True, the shift x is effectively applied to the swapped positions, which could be represented as shifting x in the opposite direction.

But I'm not sure.

Alternatively, think of it this way: each swap inverts the parity of the positions. So, applying a shift x when even_swapped is True is equivalent to applying a shift x and then swapping. But this is not helpful.

Perhaps the correct way is to track the delta and even_swapped, and when a swap is performed, the delta is inverted for even and odd positions.

Alternatively, each swap operation changes the direction in which shifts are applied. For example, after a swap, a shift of x is equivalent to a shift of -x.

But this may not be the case.

Let me try to think through an example where a swap and a shift are applied in sequence.

Example 1:

n=4.

Initial positions: 1, 2, 3, 4.

Command 2 (swap):

Boys are now at positions 2, 1, 4, 3.

Command 1 (shift x=1):

Each boy moves 1 position clockwise. So:

2 → 3, 1 →2,4→5 mod4=1, 3→4 mod4=4.

Final positions: 3, 2, 1,4.

Girl 1 has boy 3, girl 2 has boy 2, girl3 has boy1, girl4 has boy4.

So the output would be 3 2 1 4.

Now, according to the model where even_swapped is True and delta=1:

For even_swapped True, the final position is swap( (i + delta) mod n ), delta=1.

For each boy i=1: (1+1) mod4=2 → swap(2) →1.

Wait, but the actual final position for boy 1 is 3. So this model is incorrect.

So this approach doesn't work.

Alternative idea: Let's model the current permutation as a combination of a shift and swaps. For example, after a series of swaps and shifts, the current permutation can be expressed as:

p = (swap_count mod 2) times swap applied to (initial_p + delta) mod n.

But this would assume that all swaps are applied after the shifts, which is not the case.

But in the example above, the swap was applied before the shift. So this model would be:

delta = 1, swap_count =1.

So for i=1:

(1+1) mod4=2 → swap(2) →1. But the actual final position for boy1 is 3.

So this model is incorrect.

Another example:

Original i=1.

Commands: swap (swap_count=1), then shift x=1 (delta=1).

According to the model: (1 +1) mod4=2 → swap(2) →1.

But the actual final position is 3.

So the model is incorrect.

Hence, this approach isn't working.

Another approach: Think of each command as transforming the current state, which is a function that maps initial positions to current positions.

Each command is a transformation that is composed with the current state.

For example, the initial state is f0(i) = i.

After a swap command, the state becomes f1(i) = swap(f0(i)).

After a shift x command, the state becomes f2(i) = (f1(i) + x) mod n.

After another swap, the state becomes f3(i) = swap(f2(i)).

And so on.

The final state is the composition of all commands.

To compute this efficiently for all i, we need to find a way to represent the final function f(i) as a combination of swaps and shifts.

But composing many swaps and shifts into a single function is the key.

Let's see. Let's track the state as a function f(i) = (i * a + b) mod n, where a and b are parameters that can be modified by each command.

But this is only applicable if the function is linear. However, the swap function is not linear. So this approach may not work.

Alternatively, the swap function can be represented as a permutation that alternates even and odd positions. So, for each i, the swap function is:

swap(i) = i + 1 if i is odd, i-1 if i is even.

So, for even n, this function is a bijection.

The shift function is f(i) = (i + x) mod n.

The problem is to find the composition of these functions.

Let's see how the functions compose.

Suppose we have a shift x followed by a swap.

Then, the composite function is swap( (i + x) mod n ).

If it's a swap followed by a shift x, the composite function is (swap(i) + x) mod n.

These are different.

So, the order of operations matters.

Now, for each command, we can track the composite function as a series of swaps and shifts. However, with 2e6 commands, we need to find a way to represent this composite function efficiently.

But how?

Each swap can be represented as a bit flip in the parity of the current state. For example, each swap toggles a flag that indicates whether even and odd positions are swapped.

Then, each shift can be represented as adding x to the current position, but the effect of the shift depends on the current swap flag.

So, here's a possible approach:

We track two variables: delta and swap_count (mod 2).

Each shift command modifies delta based on the current swap_count.

When swap_count is even (0), a shift x adds x to delta.

When swap_count is odd (1), a shift x adds -x to delta.

Wait, why?

Because when swap_count is 1 (even_swapped is True), the current positions are swapped. So, applying a shift x in this state is equivalent to applying a shift x to the swapped positions. But when we later apply the swap again (if swap_count is even), the effect of the shift is reversed.

Alternatively, perhaps each swap inverts the direction of the shift.

For example:

When swap_count is even, delta is added normally.

When swap_count is odd, delta is subtracted.

But how?

Let me try with an example.

Example 1:

n=6.

Commands: type 1 (x=2), type 2 (swap), type 1 (x=2).

According to the first sample input.

Initial delta=0, swap_count=0.

Command 1: delta += 2 → delta=2, swap_count=0.

Command 2: swap_count becomes 1. So delta is now adjusted to delta * (-1), because in the swapped state, shifts are subtracted. Or perhaps when swap_count is odd, the delta is subtracted. So after the swap, delta is 2 * (-1) = -2.

Command 3: type 1, x=2. Since swap_count is 1, delta += x * (-1) → delta = -2 + (-2) = -4. Then swap_count is still 1.

After all commands, swap_count is 1, delta is -4.

But wait, the final delta is -4. Now, for each boy's initial position i, the final position is swap( (i + delta) mod n ), since swap_count is 1.

Let's compute:

delta =-4, swap_count=1.

For i=1: (1 -4) mod 6 = (1-4)= -3 mod6=3. Then swap(3) →3 is odd →3+1=4. So final position 4.

i=2: (2-4) mod6= (-2 mod6)=4. swap(4) →4-1=3. So final position 3.

i=3: (3-4) mod6=5. swap(5) →5+1=6.

i=4: (4-4) mod6=0 →0 mod6=0 →0+1=1. swap(0 is even? Wait, no. Wait, the initial mod gives 0, which is even. So swap(0) →0-1= -1 mod6=5.

Wait, this is getting complicated. Let's see:

For the first sample input:

After three commands, the output is 4 3 6 5 2 1.

Let's compute using the delta and swap_count model:

Commands:

Initial delta=0, swap_count=0.

Command 1: type 1 x=2. swap_count is 0 → delta +=2 → delta=2.

Command 2: swap_count becomes 1. Then, delta is multiplied by -1? Or how?

If swap_count is 1, then the next shift will be subtracted.

Command 3: type 1 x=2. Since swap_count is 1, delta += (x * (-1)) → delta = 2 + (-2) =0. Or perhaps after the swap, the delta is adjusted.

Alternatively, whenever a swap is performed, the delta is multiplied by -1.

So:

Command 2: swap_count becomes 1. delta *= -1 → delta= -2.

Command 3: type 1 x=2. Since swap_count is 1, delta += x * (-1) → delta =-2 + (-2) = -4.

Final delta is -4, swap_count=1.

Now, for each boy i:

(i + delta) mod n → (i -4) mod6.

Then, swap is applied (since swap_count is 1).

For i=1:

(1-4) mod6= 3 → swap(3) →4.

i=2: (2-4) mod6=4 → swap(4) →3.

i=3: (3-4) mod6=5 → swap(5) →6.

i=4: (4-4) mod6=0 →0 mod6 is 0. swap(0) →-1 mod6=5 →5.

i=5: (5-4) mod6=1 → swap(1) →2.

i=6: (6-4) mod6=2 → swap(2) →1.

So the final positions are 4,3,6,5,2,1. Which matches the first sample.

So this model works for the first sample.

Let's check another example.

Sample input 2:

2 3

1 1

2

1 -2

Output:1 2.

Commands:

Initial delta=0, swap_count=0.

Command 1: type 1 x=1 → delta +=1 → delta=1, swap_count=0.

Command 2: swap_count=1 → delta *= -1 → delta= -1.

Command 3: type 1 x=-2 → since swap_count is 1, delta += (-2)* (-1) → delta =-1 + 2 =1.

Wait, no. The model is: when a swap is applied, delta is multiplied by -1. Then, for subsequent shifts, when swap_count is 1, the delta is adjusted by x * (-1).

Alternatively, after each swap, the delta is multiplied by -1. Shifts after that are added to delta normally.

Let's re-express the model:

Initialize delta =0, swap_count=0.

For each command:

If the command is type 1 (shift x):

   if swap_count is even:

       delta += x

   else:

       delta -= x

   delta = delta mod n  # to keep it within modulo n.

If the command is type 2:

   swap_count +=1

   delta *= -1

   swap_count %= 2

   delta = delta mod n

This model may work.

Let's test sample 2.

n=2, q=3.

Commands:

1 1 → type 1 x=1.

swap_count is 0 → delta +=1 → delta=1.

Command 2: type 2 → swap_count becomes 1. delta *= -1 → delta= -1 mod2=1 (since -1 mod2 is 1).

Command 3: type 1 x=-2.

swap_count is 1 → delta -=x → delta =1 - (-2) =3 mod2=1.

So final delta=1, swap_count=1.

Final positions are computed as:

for each i in 1..2:

if swap_count is 1:

   swap( (i + delta) mod2 )

Else:

   (i + delta) mod2.

For i=1:

(1+1) mod2= 0 mod2=0 → swap(0) →0 is even →0-1= -1 mod2=1.

For i=2:

(2+1) mod2= 3 mod2=1 → swap(1) →2.

So final positions are 1 and 2. Which matches the sample output.

Another example.

Sample 3:

4 2

2

1 3

Output:1 4 3 2.

Let's model this.

Commands:

Command1: type 2 → swap_count=1, delta *= -1 → delta=0 * -1 =0.

Command2: type1 x=3 → swap_count=1 → delta -=3 → delta= -3 mod4=1.

Final delta=1, swap_count=1.

For each i:

swap( (i+1) mod4 )

i=1 → (2 mod4)=2 → swap(2) →1.

i=2 → (3 mod4)=3 → swap(3) →4.

i=3 → (4 mod4)=0 → swap(0) →-1 mod4=3.

i=4 → (5 mod4)=1 → swap(1) →2.

So the final positions are 1,4,3,2. Which matches the sample.

So this model seems to work.

Thus, the model is:

Track delta and swap_count.

For each command:

- type1 x:

   if swap_count is even:

       delta +=x

   else:

       delta -=x

   delta modulo= n

- type2:

   swap_count ^= 1 (toggle)

   delta = (-delta) %n

After processing all commands, for each girl i (which is paired with boy's initial position i):

final_pos = (i + delta) %n

if swap_count is 1:

   final_pos = swap(final_pos)

where swap(p) is p-1 if p is even, p+1 if p is odd.

But since the girls are arranged in a circle, after swap, the positions are adjusted modulo n.

Wait, but swap(p) must ensure that the new position is within 1..n. Because the initial positions are 0-based? Or 1-based.

Wait, the initial positions are 1-based. So when applying swap(p), where p is 0-based or 1-based?

In our model, all operations are done in 1-based positions.

But when we compute (i + delta) modn, the result is 0-based (since mod n gives 0..n-1), but adding 1-based i.

Wait, no. Let's re-express delta as a modular shift.

Wait, the problem states that when a boy moves x positions clockwise, it's equivalent to adding x to his current position, modulo n. But the girls are arranged in a circle, so adding x may wrap around.

For example, boy at girl 6 (n=6) moves 2 positions clockwise: 6+2=8 → 8 mod6=2.

So, the calculation is (current_pos + x) modn. But since current_pos is 1-based, when current_pos is added to x, it's possible that the sum is larger than n.

So, the code should compute (current_pos + x -1) modn +1 to handle 1-based indices correctly.

But in the model we have, delta is a shift that is added to the current position, and the modulo is handled by taking delta modulo n.

But the model may need to represent delta as the net shift, and when applying the shift to the initial position i, it's computed as (i + delta) modn, but considering 1-based.

Wait, perhaps the model is using 0-based indices internally. Let's re-express the model in 0-based.

But perhaps the code is easier to handle if we convert the girls' positions to 0-based.

Let's re-express the model:

Girls are 0-based (0, 1, ..., n-1).

Boys' initial positions are 0-based: boy i starts at girl i.

A shift of x positions clockwise is adding x to their current position, modulo n.

A shift of -x positions counter-clockwise is the same as adding x in the negative direction.

Swap command: even indices (girls) are 0-based, so even indices are 0, 2, 4, etc. But according to the problem statement, the even-indexed girls (1-based) are swapped with the previous (i-1) girl's partner. So in 1-based terms, even i (2,4,6) swap with i-1 (1,3,5).

In 0-based terms, this is girls 1, 3, 5 (odd indices) swap with their previous even indices (0, 2, 4).

So, for a boy in position j (0-based):

If j is even (0-based), then he swaps with j+1.

If j is odd (0-based), he swaps with j-1.

So the swap in 0-based terms is: for any j, swap(j) is j+1 if j is even, j-1 if j is odd.

Thus, in 0-based terms, swap(j) = j ^ 1 (XOR with 1).

So, for j in 0-based:

j even → j+1.

j odd → j-1.

Which is exactly j XOR 1.

So, the swap function in 0-based terms is j ^1.

Thus, the model can be simplified by working in 0-based indices.

So, the model now:

Track delta (the net shift in 0-based terms) and swap_count (mod 2).

For each command:

- type 1 (x):

   if swap_count is even:

       delta += x

   else:

       delta -= x

   delta = delta %n

- type 2:

   swap_count ^=1

   delta = (-delta) %n

Because when a swap is performed, the net shift is reversed. For example, in 0-based terms, after a swap, a shift x in the original direction is equivalent to a shift -x in the new swapped state.

Wait, how?

When swap_count is even, the shift is added normally. When swap_count is odd, the shift is subtracted. Then, when a swap is performed, the existing delta is multiplied by -1, because the swap inverts the direction of the shift.

So, for example:

delta = 2.

After a swap (swap_count becomes 1), delta becomes -2 mod n.

Another swap (swap_count becomes 0), delta becomes 2 mod n.

This models the fact that each swap inverts the direction of the current delta.

Thus, the model is:

For each type 2 command, swap_count is toggled, and delta is multiplied by -1 (mod n).

For type 1 commands, if swap_count is even (0), delta +=x; else, delta -=x.

Thus, the code will look something like this:

n, q = map(int, input().split())

delta = 0

swap_count = 0

for _ in range(q):

    cmd = input().split()

    if cmd[0] == '1':

        x = int(cmd[1])

        if swap_count %2 ==0:

            delta +=x

        else:

            delta -=x

        delta %=n

    else:

        swap_count +=1

        delta = (-delta) %n

        swap_count %=2

Then, after processing all commands, the final position for each girl i (0-based) is:

current = (i + delta) %n

if swap_count:

    current ^=1

Convert current to 1-based and output.

Yes! Because for each girl i (0-based), the boy's position is (i + delta) modn, and if there's an odd number of swaps, we XOR with 1 (swap even and odd 0-based indices).

Thus, the code will be:

Read n and q.

Initialize delta=0, swap_count=0.

Process each command:

   for type 1, adjust delta based on swap_count.

   for type 2, toggle swap_count and invert delta.

After processing all commands:

For each girl i (0-based):

   current = (i + delta) %n

   if swap_count is 1:

       current ^=1

   The girl i+1 is paired with boy current+1.

So, the output is the list of current+1 for i from 0 to n-1.

This approach is O(q) time for processing commands, and O(n) time for output. Since q can be 2e6 and n up to 1e6, this should be manageable.

Testing with sample 1:

Sample 1:

n=6, q=3.

Commands:

1 2 → type 1 x=2. swap_count is 0 → delta +=2 → delta=2.

2 → type 2 → swap_count becomes 1. delta = -2 mod6=4.

1 2 → type1 x=2. swap_count is 1 → delta -=2 →4-2=2 mod6=2.

delta=2, swap_count=1.

For each girl i (0-based 0-5):

current = (i +2) mod6.

If swap_count is 1 → current ^=1.

Girl 0 (i=0):

current = (0+2) mod6=2 → XOR 1 →3 → output 4 (3+1).

Girl 1 (i=1):

current =3 mod6=3 → XOR1 →2 → output 3 (2+1).

Girl 2 (i=2):

current=4 → XOR1 →5 → output 6.

Girl3 (i=3):

current=5 → XOR1 →4 → output5.

Girl4 (i=4):

current= (4+2)=6 mod6=0 → XOR1 →1 → output2.

Girl5 (i=5):

current= (5+2)=7 mod6=1 → XOR1 →0 → output1.

Which matches the sample output 4 3 6 5 2 1.

Sample 2:

n=2, q=3.

Commands:

1 1 → delta +=1 →1.

2 → swap_count becomes 1, delta= -1 mod2=1.

1 -2 → swap_count=1 → delta -= (-2) →1 +2=3 mod2=1.

Final delta=1, swap_count=1.

For each girl i in 0-based:

current = (i+1) mod2 → for i=0:1, i=1: 0.

Swap_count 1 → XOR1.

0 →1 → output 2.

1 →0 → output1.

Which matches sample output 1 2.

Sample3:

n=4, q=2.

Commands:

2 → swap_count becomes 1, delta =0.

1 3 → swap_count=1 → delta -=3 →0-3= -3 mod4=1.

delta=1, swap_count=1.

Girls:

i=0 → current =0+1=1 mod4 →1 ^1=0 → output 1.

i=1 →1+1=2 →2^1=3 → output4.

i=2 →2+1=3 →3^1=2 →output3.

i=3 →3+1=4 mod4=0 →0^1=1 →output2.

Thus, output is 1 4 3 2, which matches the sample.

Thus, this model works.

So the code in Python will be:

Read n and q.

delta and swap_count are initialized to 0.

Process each command:

   for type 1, adjust delta based on swap_count.

   for type 2, toggle swap_count and invert delta.

Then, for each girl in 0-based:

compute current = (i + delta) %n.

if swap_count is 1, xor with 1.

then current +1.

Output the list of current +1 for all girls.

This is O(q) time for processing commands and O(n) for output, which is acceptable for the constraints.

Now, for code optimization, we can read the commands efficiently. Since q can be up to 2e6, using input() for each line can be slow. Thus, reading all input at once using sys.stdin.read() and processing it can be faster.

But for Python, even with that, it's manageable. However, for very large inputs, it's better to read all the input at once.

So the code would look like:

Testing against sample input 2.

```python
import sys


def main(input_stream, output_stream):
    n, q = map(int, input_stream.readline().split())

    delta = 0

    swap_count = 0

    mod = n

    for _ in range(q):

        parts = input_stream.readline().split()

        if parts[0] == '1':

            x = int(parts[1])

            if swap_count:

                delta = (delta - x) % mod

            else:

                delta = (delta + x) % mod

        else:

            swap_count ^= 1

            delta = (-delta) % mod

    result = []

    for i in range(n):

        current = (i + delta) % mod

        if swap_count:

            current ^= 1

        result.append(current + 1)

    print(' '.join(map(str, result)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 2
2
1 3
""",
            "output": \
"""\
1 4 3 2
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

Thus, the code should be correct.
</think>

```python
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    q = int(input[ptr])
    ptr += 1
    delta = 0
    swap_count = 0
    mod = n
    for _ in range(q):
        cmd = input[ptr]
        ptr += 1
        if cmd == '1':
            x = int(input[ptr])
            ptr += 1
            if swap_count:
                delta = (delta - x) % mod
            else:
                delta = (delta + x) % mod
        else:
            swap_count ^= 1
            delta = (-delta) % mod
    result = []
    for i in range(n):
        current = (i + delta) % mod
        if swap_count:
            current ^= 1
        result.append(str(current + 1))
    print(' '.join(result))

if __name__ == "__main__":
    main()
```
