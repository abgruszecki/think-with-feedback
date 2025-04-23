<think>
Okay, let's tackle this problem. So, the task is to simulate how a queue of boys and girls changes over t seconds based on certain swapping rules. Let's see the details.

The problem says that every second, each boy that is immediately in front of a girl will swap places with her. But the swaps happen simultaneously for all such pairs. So, in each second, all the pairs are identified first, and then all the swaps happen at once. That's important because if you process swaps one by one, you might affect the subsequent swaps in the same step. So, for example, if you have "BBG", the first B and the second B are both followed by a G. But during the same second, the second B and G would swap, but the first B and second B (now G) would not. Wait, no. Let's think: in the initial step, for the string "BBG", at time x=0, the first B is in position 1, the next B in position 2. The B in position 2 is followed by a G. So during the first second, only the B in position 2 and G in position 3 swap. So after one second, it becomes "BGB". Then, in the next second, the B in position 1 is followed by a G (position 2 now). So they swap, leading to "GBB". So each time, all possible swaps are considered, processed in a way that the leftmost possible swaps happen first, but since the swaps are done in a single pass, but simultaneously, we need to process the swaps correctly.

So the key is that in each time step, we scan the string from left to right, and whenever we find a 'B' followed by a 'G', we swap them, but since multiple swaps can happen in the same time step, but each swap affects the next positions. Wait, no. Because the swaps are done in parallel. For example, in the first sample input:

BGGBG → after 1 second becomes GBGGB. Let's see:

Original positions: 1=B, 2=G, 3=G, 4=B, 5=G.

At time x, look for B followed by G. Position 1 and 2: B followed by G → swap. So positions 1 and 2 become G and B. Then, position 4 and 5: B followed by G → swap. So after the first second, the string becomes G B G G B → wait, but the original positions were B G G B G. Let's process step by step.

Original string: B G G B G (indices 0-4 if 0-based, but in the problem description, positions are 1-based. So when processing the string, for each i from 0 to n-2 (since we check i and i+1), check if s[i] is B and s[i+1] is G. If so, mark these positions to swap.

But the swaps must all happen at once. So, for each time step, we need to process all possible swaps in one pass, but ensure that each swap doesn't interfere with the others in the same step. For example, if there's a sequence like B B G, during the first second, the second B and G swap, leading to B G B. But during the same step, the first B is now followed by G. But since the swap for the first pair (positions 0 and 1) wasn't considered in the same step, because after the first swap, the first B is followed by G. But the processing for the time step should only consider the original arrangement at the start of the step.

So the correct approach is: for each time step, create a new string (or list) based on the current state. For each position i, check if in the current state, the character at i is B and the next is G. If so, swap them in the new state. But to avoid overwriting the current state while processing, we need to build the next state based on the original state.

Wait, but when processing left to right, if you swap a pair, the next pair might involve the same characters. For example, consider the string "BGB". Let's say we have B at position 0, G at 1, B at 2. So during a time step, the first B (0) and G (1) will swap, leading to G B B. But the next pair (position 1 and 2) is B and B, so no swap. But if we process the string step by step, modifying it as we go, then after swapping 0 and 1, the next check would be between 1 (B) and 2 (B), which is not a swap. But in the original approach, the swaps are determined based on the state at the beginning of the time step. So in the same time step, any swap is based on the original arrangement.

So the way to model this is: for each time step, we create a copy of the current arrangement. Then, we iterate through the original arrangement, and for each i, if s[i] is B and s[i+1] is G, we mark that this pair should be swapped. But since multiple swaps can't interfere with each other in the same time step (since they are based on the original arrangement), the way to do this is:

- Create a list of positions where a swap needs to happen during this time step.

But wait, the problem is that when you swap a pair, you might affect adjacent pairs. For example, in "BBG", during the first time step:

Original arrangement is B B G.

Check each pair:

- Pair 0 and 1: B followed by B → no swap.

- Pair 1 and 2: B followed by G → swap. So in the next step, this pair is swapped.

But when processing the original string, all swaps are determined based on the original state. So even if after swapping pair 1 and 2, the new pair 0 and 1 would be B and G (from original B and B), but since we are processing based on the original state, this isn't considered.

Therefore, the correct approach is to process all possible swaps in the current time step based on the original state before any swaps in that time step.

So, for each time step, we need to:

1. Create a new array (or list) to represent the next state.

2. Iterate through the current state from left to right, and whenever a B is followed by a G, swap them in the new state. However, we need to handle overlapping swaps.

But here's the catch: if we process the string left to right and swap pairs, but then proceed to check the next pair, which may have already been swapped. So if you have a sequence like "BGB", the first pair (B and G) is swapped to make G B B. Then, the next pair (B and B) is not swapped. But if you process left to right, modifying the array as you go, you might have issues. For example, if the original string is "BGGBG" (as in the first example), then the first pair (positions 0 and 1) is B followed by G → swap. Then, the next pair (positions 1 and 2) are now G and G → no swap. Then positions 3 and 4: B and G → swap. So the next state would be G B G G B → but wait, the original string was BGGBG (positions 0-4). So during the first time step:

Original pairs to swap are (0,1) and (3,4). So in the new array, these pairs are swapped. So the new array would be G B G G B → which becomes GBGGB as in the sample.

So the correct way is to collect all the pairs that need to be swapped during this time step, then apply all swaps in a way that doesn't interfere with each other. Because each swap in the same time step is based on the original state.

Therefore, the approach should be:

For each time step:

- Iterate through the string, note all the positions i where s[i] is B and s[i+1] is G.

- Then, create a new string where for each such i, the B and G are swapped, but when building the new string, we have to ensure that each swap is applied to the original state, not the modified one.

But how to do this? Let's think.

For example, if we have the original string and a list of positions to swap. Then, when building the new string, each swap is applied to the original positions, so overlapping swaps (like i and i+1, then i+1 and i+2) are handled correctly.

Wait, but the problem is that a position can be part of at most one swap in a single time step. Because if a position i is part of a swap (i-1, i) and (i, i+1), but that's impossible. For example, if the original string is "BGG", then positions 0 and 1 are swapped (B and G). Then position 1 and 2 (G and G) don't swap. So no overlapping.

Alternatively, if the original string is "BGBG". Then, during the time step:

Check positions 0-1 (B and G → swap). Positions 2-3 (B and G → swap). So in the next step, the new string is "GBGB".

So the way to model this is:

The new string is built by first copying the original, then for each swap pair (i, i+1) found in the original, swap them in the new string.

But how to do this without overlapping swaps?

Because if you have a sequence like "BGGBG", the original pairs are (0,1) and (3,4). So in the new string, these two pairs are swapped. So the new string would be G B G G B → which is correct.

So the steps for each time step are:

1. Create a list of indices where a swap is needed (i and i+1 where B followed by G in the original string).

But when processing these swaps, we have to be careful. For example, if two consecutive swaps are possible (i and i+1, then i+1 and i+2), but in the original string, these pairs are B followed by G. However, after swapping i and i+1, the next pair would be (i+1 and i+2), which in the original string may not have been a swap. So in the same time step, the swaps are determined based on the original string, not the modified one.

Therefore, the correct approach is to first collect all the positions i where the original string has B followed by G. Then, in the new string, for each such i, swap the characters at i and i+1. However, when building the new string, we must not overwrite the original string until all swaps are processed. So the steps are:

- Start with the original string as a list (since strings are immutable in Python, using a list is easier).

- For each time step, create a copy of the current list.

- Iterate through the original list from left to right, check for B followed by G.

- For each such pair, mark their positions to be swapped in the new list.

But when creating the new list, how to handle overlapping swaps? For example, if we have a pair i and i+1, and then i+1 and i+2, but in the original string, i is B, i+1 is G (so they swap), and i+1 is G, i+2 is B (so no swap). Wait, in the original string, if the pair i and i+1 is B followed by G, then in the original, the pair i+1 and i+2 could be G followed by B, which would not be swapped. So in this case, the swaps are non-overlapping.

Wait, but in the case of "BBGG". Original is B B G G. In the first time step:

Check each pair:

0-1: B B → no swap.

1-2: B G → swap.

2-3: G G → no.

So in the new list, swap 1-2. The new list is B G B G. Now, in the next time step:

Check the original list (B G B G):

Check pairs:

0-1: B G → swap → becomes G B B G.

1-2: B B → no.

2-3: B G → swap → becomes G B G B.

But during the same time step, the original pairs would have been 0-1 (B G → swap), and 2-3 (B G → swap). So in the same time step, both swaps are processed. So the new list is G B G B.

Therefore, the way to process the swaps is to collect all the indices i where the original has B followed by G, then for each of these indices, swap the characters at i and i+1 in the new list. But since these swaps are based on the original positions, there's no overlap. Because each swap in the same time step is between i and i+1, and after swapping, the next swap (if any) would involve i+2 and i+3. So in a single time step, the swaps can't interfere with each other as they are all based on the original positions.

But wait, suppose we have a scenario like "BGBG". The original pairs are 0-1 (B G → swap), 2-3 (B G → swap). So in the same time step, both swaps are processed. The new string is G B G B. So the swaps are non-overlapping. Thus, processing them in any order (left to right) and swapping in the new list would work.

But how to model this? Because if you process the swaps from left to right and modify the list as you go, you might affect later swaps. For example, consider the original string "BGG". Then, the pair 0-1 (B G) is to be swapped, and the pair 1-2 (G G) is not. So after swapping 0-1, the new list is G B G. Then, during the same time step, the pair 1-2 is B G, which would be a swap. But wait, no, because the original state was B G G. So in the original state, the pair 0-1 is B G (swap), and pair 1-2 is G G (no swap). So in the time step, only 0-1 is swapped. So the new list is G B G. So that's correct.

But if you process the swaps in the new list, you might end up with additional swaps. But since the swaps are based on the original list, not the new list, you should not do that.

So the correct approach is:

For each time step:

1. Create a list of the current arrangement.

2. Scan this list from left to right, checking for B followed by G.

3. For each such pair, mark them to be swapped.

4. Create a new list (copy of the original), then apply all the swaps in the order of the indices collected. But since the order of processing the swaps (left to right) and applying them to the new list (based on the original indices), there's no overlap. For example, if in the original list, indices 0 and 1 are swapped, and indices 2 and 3 are swapped. When building the new list, the original list is copied, then indices 0 and 1 are swapped, then indices 2 and 3 are swapped. So the order in which the swaps are applied doesn't matter because they are based on the original positions.

But wait, what if a swap is done for index 0, then index 1. For example, original string is "BGGBG". Then, in the first step, indices 0 and 1 (B and G) are swapped, and indices 3 and 4 (B and G) are swapped. So when building the new list, the original list is copied, then:

- swap positions 0 and 1 → becomes G B G B G.

Then swap positions 3 and 4 → becomes G B G G B.

Which matches the sample input.

So the steps are:

- For each time step, collect all the indices i where s[i] is B and s[i+1] is G.

- Then, create a new list (as a copy of the original), and for each i in the collected list, swap the elements at i and i+1 in the new list.

But wait, in the collected list, the order might matter. For example, if you collect i=0 and i=1 (if the original string is "BBGG", then in the original, i=1 (B followed by G), but after swapping i=0 and 1 (if they were B and B, then i=1 would be B in the original, which is not part of a swap. So the collected list is based on the original, not the modified.

So in the new list, all swaps are applied to the original positions. So the order in which the swaps are applied doesn't matter. Because each swap is based on the original state.

So for example, if two adjacent swaps are possible, like i=0 and 1 (B followed by G) and i=1 and 2 (B followed by G) in the original string. Then, both swaps would be applied in the new list. So swapping i=0 and 1 first would turn those into G and B. Then, swapping i=1 and 2 (original B and G) would swap those as well, leading to G B → G. So the new list would have G G B. But wait, the original list had B at 0, B at 1, G at 2. So in the original list, the pairs (0,1) are B B → no swap. Pair (1,2) is B G → swap. So in the new list, only (1,2) would be swapped, leading to B G B. But in the example I thought of, the original was B B G. So the first pair (0,1) is B B → no swap, pair (1,2) is B G → swap. So the new list is B G B. So the initial thought was incorrect.

So the key is that in each time step, the swaps are determined based on the original state. So even if the original state allows for multiple swaps, but overlapping, they are only processed if they are B followed by G in the original.

So the way to model this is: collect all the indices i where in the original list, s[i] is B and s[i+1] is G. Then, in the new list, swap those pairs. The order of processing these swaps in the new list does not matter because each swap is applied to the original positions.

Therefore, the algorithm can be implemented as follows:

Initialize the current arrangement as a list (since strings are immutable).

For each time step from 1 to t:

   Create a copy of the current list.

   Iterate through the original list (before any swaps) from i=0 to n-2:

      if current[i] is 'B' and current[i+1] is 'G':

          mark this pair for swapping.

   For each marked i in the original list:

       in the new list, swap positions i and i+1.

   Set the current list to the new list.

Thus, each time step is processed by first finding all possible swaps based on the original state, then applying all of them in the new list.

Now, considering the constraints: n and t can be up to 50 each. So for t=50 and n=50, the algorithm would process 50 time steps, each time O(n) operations to find swaps and apply them. This is acceptable. The time complexity is O(t*n), which is 50*50=2500 operations. That's trivial for Python, even with loops.

So the plan is:

- Read n and t.

- Read the initial string.

- Convert the string to a list for easier manipulation.

- For each of the t steps:

   - Create a copy of the current list.

   - Find all the positions i where current[i] is 'B' and current[i+1] is 'G'.

   - For each such i, in the new list, swap i and i+1.

   - Set the current list to the new list.

- After all steps, join the list into a string and output.

Wait, but how to create the new list each step. Let's see. For each step:

current_list is the list from the previous step.

new_list = list(current_list)  # creates a copy

Then, for each i in the indices where B is followed by G in current_list:

   swap new_list[i] and new_list[i+1]

Wait, no. Because the new_list is a copy of current_list. So when you find a pair in current_list, you swap them in new_list. But the next pair is checked in current_list, so the swaps in new_list do not affect the processing of the current step.

Yes. So in each time step:

current_list is the original state.

new_list is a copy.

Then, for each i in 0 to n-2:

   if current_list[i] is 'B' and current_list[i+1] is 'G':

       swap new_list[i] and new_list[i+1]

So even if multiple swaps are done in new_list, the next swaps are based on current_list, not new_list. Therefore, all swaps in the same time step are based on the original state.

But the problem is that when you swap in new_list, subsequent swaps in the same time step (based on current_list) may overwrite the new_list. For example, consider a case where in current_list, i=0 and 1 are B and G, and i=1 and 2 are B and G.

So in current_list, 0-1 is B followed by G → swap in new_list.

Then, 1-2 in current_list is B followed by G → swap in new_list.

But new_list after first swap is G B ... then in the new_list, positions 1-2 are B and G. But the second swap is based on current_list, which is the original list, not the new_list.

Wait, no. The second swap is processed based on current_list[i+1], which in current_list is B followed by G. So in current_list, 1 is B, 2 is G. So the swap is applied to new_list's positions 1 and 2.

So in new_list, after the first swap (0-1), the new_list is G B B G ... (assuming original was B B G G). Then, the swap for i=1 would swap B and G in new_list, resulting in G B → G, so new_list becomes G G B G ... But the original current_list was B B G G. So the swap for i=1 is only done if current_list[1] is B and current_list[2] is G. Which in the original, they are B and G → yes. So the new_list after these swaps would be G G B G. But in reality, the original current_list for i=1 and 2 was B and G. So the new_list is first copied from current_list (B B G G). Then, when i=0: swap 0 and 1 (B and B → no). So no swap. When i=1: B and G → swap in new_list, making new_list[1] and [2] G and B. Then i=2: G and G → no swap.

So the new list after this time step is B G B G? No. Wait, the original list is B B G G. new_list is initially a copy of this.

For i in 0 to 3:

i=0: current_list[0] is B, current_list[1] is B → no swap.

i=1: current_list[1] is B, current_list[2] is G → swap in new_list. new_list becomes B G B G.

i=2: current_list[2] is G, current_list[3] is G → no swap.

So after the swap for i=1, new_list becomes B G B G.

But the original list is B B G G. So in the same time step, the swap for i=1 is applied once.

So the new_list is B G B G.

Yes, which is correct.

But the problem is that when you process the swaps in new_list, if you have multiple swaps, the order of processing could affect the result. For example, if you process i=0 and then i=1, but the current_list for i=0 is B followed by G, and for i=1 is G followed by B. So in the original list, the first swap is applied, but the second is not. But if the original list has i=0 and i=1 both as B followed by G, then the swaps are applied in order. But since the swaps are applied to the new_list, which is a copy of current_list, the order in which the swaps are applied (i=0 then i=1) does not affect the outcome.

Wait, let's take another example. Original list is B G B G.

In the first time step, check all pairs:

i=0: B G → swap.

i=1: G B → no swap.

i=2: B G → swap.

So in the new_list, first copy the original, then swap i=0 and i=2.

So in the new_list:

After i=0 is processed: positions 0 and 1 are swapped → G B B G.

After i=2 is processed: positions 2 and 3 are swapped → G B G B.

So the new_list is G B G B.

So the order in which we process the swaps (i=0 first, then i=2) does not affect the outcome. Because each swap is applied to the original list's positions.

Therefore, the algorithm can be implemented as follows:

Loop t times:

   create a new list which is a copy of current list.

   collect all the indices i where current_list[i] is B and current_list[i+1] is G.

   for each i in this list:

       swap new_list[i] and new_list[i+1]

   set current_list = new_list.

Wait, but how to collect the indices. Because when you loop through the current_list from left to right, and for each i check if current_list[i] and current_list[i+1] are B followed by G. Then, for each such i, you swap them in the new_list. But if you process them in left to right order, then when you swap i=0, it may affect the next i=1, but in the new_list. But no, because the swaps are based on the current_list. So the order of processing the swaps (left to right, or in any order) does not matter. Because all swaps are based on the current_list's state.

Therefore, to collect all the i's, you can loop through the current_list once, note all the positions where B is followed by G. Then, apply all swaps to the new_list. The order in which you apply the swaps (left to right, right to left, etc.) does not matter, since each swap in the new_list is based on the original current_list's positions.

So, for example, if in the current_list, positions i=0 and i=1 are B and G, and positions i=1 and i=2 are B and G, then in the new_list, both swaps are applied. But since the current_list's positions 0 and 1 are B and G (so swap), and 1 and 2 are B and G (so swap), in the new_list, after swapping 0-1 and 1-2:

Original current_list: B B G → new_list starts as B B G.

Swap 0-1 (B B → no? Wait, no. Wait, current_list[i=0] is B, current_list[i+1=1] is B → no swap. So why would i=0 be in the list. Oh, in that case, the original list is B B G. So i=0 is B and i+1 is B → no swap. i=1 is B and G → swap. So new_list after swapping i=1: B G B. So the next step.

So the algorithm is correct.

Now, the code.

In Python:

We can represent the current state as a list of characters.

For each time step in t:

   create a new list as a copy of the current list.

   iterate through the current list from i=0 to n-2:

       if current[i] is 'B' and current[i+1] is 'G':

           swap new_list[i] and new_list[i+1]

   set current = new_list

Wait, but when you swap new_list[i] and new_list[i+1], you are modifying the new_list. But for multiple swaps, this could affect other swaps. But no, because all swaps are based on the original current list, not the new list.

So the code is:

current = list(s)

for _ in range(t):

    new = list(current)

    for i in range(n-1):

        if current[i] == 'B' and current[i+1] == 'G':

            new[i], new[i+1] = new[i+1], new[i]

    current = new

Wait, but this is incorrect. Because in this code, for each i in 0 to n-2, if the current[i] is B and current[i+1] is G, then in the new list, we swap new[i] and new[i+1]. However, the new list was copied from current, so new[i] and new[i+1] are the same as current[i] and current[i+1] initially. So when we swap them, the new list is modified. But subsequent swaps in the same loop will process the original current list's i and i+1, but the new list's swaps may have modified positions that are to the left of the current i. For example, after swapping i=0 and 1 in new, when processing i=1, the new list's i=1 is now B (if originally it was G), but current[i=1] is still G, so the code would check current[i=1] and i+1=2. So the code correctly uses the current list to decide swaps, and applies the swaps to the new list, which is a copy. So the code is correct.

Wait, no. Let's see. Suppose the current list is 'BGGBG' (as in the first sample input). So current = ['B','G','G','B','G'].

In the first time step:

new is a copy: ['B','G','G','B','G'].

We loop i from 0 to 4-1=3.

i=0: current[i] is B, current[i+1] is G → swap new[0] and new[1]. new becomes ['G', 'B', 'G', 'B', 'G'].

i=1: current[i] is G → no swap.

i=2: current[i] is G → no swap.

i=3: current[i] is B, current[i+1] is G → swap new[3] and new[4]. new becomes ['G', 'B', 'G', 'G', 'B'].

So after this loop, current is set to new, which is the correct output for the first sample.

Yes. So the code works.

But wait, in the code, when i=0 is processed, the new list's elements at 0 and 1 are swapped. Then, when i=3 is processed, the new list's elements at 3 and 4 are swapped, regardless of any prior swaps. But this is correct because the swaps are based on the original current list.

Yes, because the code checks current[i] and current[i+1], not new[i] and new[i+1]. So the code correctly captures all the swaps that need to happen in the current time step based on the original state.

So the code is correct.

Testing the first sample:

Sample 1:

Input:

5 1

BGGBG

Which is 'B','G','G','B','G'.

After one step:

i=0: B and G → swap new[0] and 1 → new becomes G B G B G.

Then i=3: B and G → swap new[3] and 4 → new becomes G B G G B.

Which matches the sample output.

Sample 2:

After 2 steps:

First step as before. Current is GBGGB.

Second step:

current = ['G','B','G','G','B']

loop i from 0 to 3:

i=0: G followed by B → no.

i=1: B followed by G → yes. Swap new[1] and 2. new is G G B G B.

i=2: G followed by G → no.

i=3: G followed by B → no.

So the new list after step 2 is GGBGB, which matches the second sample.

Third sample:

Input: 4 1 → GGGB.

current is ['G','G','G','B'].

loop i from 0 to 2:

i=0: G and G → no.

i=1: G and G → no.

i=2: G and B → no (since it's G followed by B, which does not require a swap).

So no swaps happen. The output is GGGB.

Thus, the code works.

Therefore, the code is correct.
</think>

```python
n, t = map(int, input().split())
s = list(input())
current = s.copy()

for _ in range(t):
    new = current.copy()
    for i in range(n - 1):
        if current[i] == 'B' and current[i+1] == 'G':
            new[i], new[i+1] = new[i+1], new[i]
    current = new

print(''.join(current))
```