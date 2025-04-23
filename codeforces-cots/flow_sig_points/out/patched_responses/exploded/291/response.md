<think>
Okay, let's try to figure out this problem. Hmm. So the problem is about Masha swapping balls and faking some swaps. The special ball starts at position k, and after m swaps (some of which are possibly faked), we need to find for each position i the minimum number of swaps she must fake so that the special ball ends up there. If it's impossible, output -1.

Wait, so each swap can be either performed or not. The idea is that the order of swaps matters, but since she can choose to fake any of them, the path the special ball takes depends on which swaps are real and which are fake. But how do we model this?

Hmm. Let's think of it as the position of the special ball after each swap. For each swap, when it's real, the special ball's position changes if the swap involves its current position. If it's fake, then the position remains the same.

But Masha can choose which swaps to fake. So for each position i, we need the minimal number of swaps to fake such that after all swaps (with some faked), the special ball ends up at i.

The key is to track all possible positions the special ball could be in after each swap, considering whether the swap was faked or not, and keeping track of the minimum number of fakes required for each possible position at each step.

But with n up to 2e5 and m up to 2e5, a straightforward approach like BFS for each swap step would be O(m*n), which is way too slow. So we need a smarter way.

Let's think about dynamic programming. Maybe for each step, we track the possible positions of the special ball and the minimal number of fakes required to reach that position after that step.

Yes. For example, after each swap operation (step i), we can track a dictionary or array that maps positions to the minimal number of fakes needed to reach them after processing the first i swaps.

But with n up to 2e5, even using arrays for each step would be O(mn) time and memory, which is 4e10 operations. That's impossible.

So we need a way to model this more efficiently.

Wait, but for each swap, the swap operation affects exactly two positions. So perhaps, the possible positions of the special ball can only change in certain ways. Let's see.

Suppose after processing the first i-1 swaps, we have a set of possible positions S with their minimal fake counts. For the i-th swap (x, y):

For each position pos in S:

If the swap is not faked (i.e., performed), then the new position would be:

if pos is x, then it becomes y.

if pos is y, then it becomes x.

otherwise, remains pos.

If the swap is faked (i.e., not performed), then the position remains pos, but the fake count increases by 1.

So for each possible previous state (pos, fake_count), after the current swap, there are two options:

1. Perform the swap: new_pos is determined by swapping x and y if pos is x or y. The fake count remains the same.

2. Fake the swap: new_pos remains the same, fake count increases by 1.

We need to track, for each possible position, the minimal fake count needed to reach it after each swap.

But if we do this naively, for each swap, we might have O(1) or O(2) new positions. Wait, maybe we can model this with a data structure that allows us to efficiently track the minimal fake counts.

At each step, the possible positions are either the same as before (if we fake the swap) or swapped (if we perform it). So the transitions are limited.

So, for each swap, the new possible positions are:

For each pos in the current possible positions, when performing the swap, we get a new pos (if x or y), and when faking, same pos but +1 fake.

But tracking all possibilities with minimal fake counts is tricky. Let's think about how the minimal fake counts can be updated.

Let's model this as a state where for each position, we have the minimal number of fakes required to reach it. Then, for each swap, we can compute the new state based on the previous state.

At the start, the initial position is k, with 0 fakes. All other positions are either unreachable (infinity) or not considered yet.

For each swap (x_i, y_i), we can compute the next state as follows:

For each possible position in the previous state (pos_prev):

Option 1: Perform the swap. The new_pos is pos_prev if pos_prev is not x_i or y_i. If pos_prev is x_i, new_pos is y_i. If pos_prev is y_i, new_pos is x_i. The fake count remains the same.

Option 2: Fake the swap. The new_pos is pos_prev. The fake count increases by 1.

But since we want the minimal fake counts, for each position in the new state, we need to take the minimum between existing values and possible new values from either option.

But how do we compute this efficiently?

Let's denote that for the previous state, we have a map (like a dictionary) where for each position, we have the minimal fake count to reach it. Then, for the current swap, the next state can be computed by considering both options for each possible position in the previous state.

But if the previous state has O(1) possible positions (since in each step, the swap can only affect the positions x and y), maybe we can model this efficiently.

Wait, maybe the number of possible positions for the special ball is small. Let's think: initially, it's at k. Then, each swap can either move it (if performed) or not (if faked). So after m swaps, the possible positions are those that can be reached by a subset of swaps, possibly including or excluding each swap.

But the problem is that the swaps are processed in order, and each decision (fake or not) affects the current position. So the path is a sequence of choices (perform or fake) for each swap, leading to different positions.

But since the swaps are in order, the possible positions after each swap are determined by the previous steps. However, if we track the minimal number of fakes required to reach each possible position, maybe for each step, the number of possible positions is small.

Wait, for example, the initial position is k. After the first swap, which is between x1 and y1:

If the swap is performed, the new position is swapped if the previous was x1 or y1. Otherwise, same as before.

If the swap is faked, the position remains the same, but the fake count increases by 1.

So after each step, the possible positions can be tracked, but perhaps the number of possible positions is manageable.

But for m=2e5 steps, even if each step adds a few possibilities, the total could be O(m) possibilities, which would be acceptable if processed efficiently.

Wait, but even so, for each swap, the next possible positions are derived from the previous ones. Let's model this with a dictionary (or a list) that tracks the possible positions and their minimal fake counts.

At each step, we can process the swaps and update the possible positions.

Let's see:

Initialize a dictionary (say, current_pos) where current_pos[pos] = min_fakes. Initially, it's {k: 0}.

For each swap (x, y) in the list of swaps:

    Create a new dictionary (next_pos) which will track the minimal fakes for each position after this swap.

    For each (pos, count) in current_pos.items():

        Option 1: Perform the swap. The new position is:

            if pos == x: new_p = y

            elif pos == y: new_p = x

            else: new_p = pos

        For this new_p, if it's not in next_pos or if count is less than the existing value, we update next_pos[new_p] = min(count, existing value).

        Option 2: Fake the swap. The new position is pos, and the count increases by 1.

        For pos in this case, if pos is not in next_pos or count + 1 is less than the existing value, update next_pos[pos] = min(count + 1, existing value).

    After processing all entries in current_pos, set current_pos to next_pos.

After processing all swaps, we have current_pos which maps each possible final position to the minimal number of fakes needed. For any position not in current_pos, output -1. Otherwise, output the minimal count.

But wait, this approach would take O(m) steps, and for each step, the number of entries in current_pos could be up to O(m), leading to O(m^2) time, which is 4e10 operations for m=2e5. That's way too slow.

So we need a smarter way. Let's think: for each swap, the possible positions can only be the ones that were either present before the swap, or their swapped versions. So maybe the number of possible positions is very limited.

Wait, but consider that each swap can affect the current position. If the special ball is not involved in the swap (i.e., pos is not x or y), then performing the swap doesn't change its position. So the choice to perform or fake the swap would result in the same position (if performed but pos is not x or y, then no change; if faked, pos remains and fake count +1).

Wait, that's a problem. Because in this case, for a position not involved in the swap, performing the swap is the same as not performing it in terms of the position (since pos is not x or y), but the fake count increases by 1 if we fake it. So, in this case, for such a pos, the better option is to perform the swap (since fake count remains the same). So the minimal fake count for pos after this swap would be the same as before if we perform the swap, or previous count +1 if we fake it. Since we want the minimal, performing the swap (no fake) is better.

But how to model this.

Alternatively, for a position not involved in the current swap, when we process the swap, performing the swap (no fake) gives the same pos and same fake count as before, while faking it (so pos remains) gives fake count +1. So for such pos, the minimal fake count after this swap would be the minimal between the previous count (if we perform the swap) and previous count +1 (if we fake it). But since the previous count is already the minimal, the minimal for this pos after the swap would be min(previous_count, previous_count +1) → previous_count. So, performing the swap is better, and there's no change in the fake count. So, for positions not involved in the swap, the minimal fake count remains the same as before.

Wait, but this suggests that for such positions, after this swap, the minimal fake count can be updated by either choosing to perform (no cost) or fake (cost +1). Since performing gives a lower cost, the minimal remains the same as before. Therefore, for positions not involved in the swap (x and y), the minimal fake count after this swap is the same as before. So, in this case, if the current_pos includes such a pos, then after this swap, the minimal fake count for pos is the same as before. But if the swap is processed, and the position is not x or y, then the new pos is the same as the old, and the minimal fake count is the same as before.

Hmm. So perhaps, for the swap (x, y), the only positions that can change their minimal fake counts are x and y. For other positions, the minimal fake count remains the same.

Wait, but how? Let's see. Suppose a position z is not x or y. Suppose before the swap, the minimal fake count to reach z is c. Then, during this swap:

Option 1: perform the swap. Since z is not x or y, the new position is still z, and the fake count remains c. So, after performing, the minimal for z remains c.

Option 2: fake the swap. The position is still z, and the fake count becomes c + 1.

So, the minimal between c and c +1 is c. So, the minimal for z after this swap is c. Therefore, the minimal fake count for z remains unchanged. So, the swap (x, y) doesn't affect the minimal count for any positions other than x and y.

But wait, that's only if the swap is applied to a position that's not x or y. So, for all positions except x and y, their minimal fake counts can be carried over as-is. Only x and y are affected.

So, the key insight here is that each swap (x, y) only affects the positions x and y. All other positions' minimal fake counts are carried forward as before. So, during each swap, we only need to update the minimal fake counts for x and y.

Wait, but how?

Let me think. Let's denote that after processing i swaps, we have for each position p, the minimal number of fakes required to reach p. Now, when processing the (i+1)-th swap (x, y), the new minimal counts for the positions x and y can be updated based on the previous counts.

For any position p not x or y, the minimal count remains the same as before. For x and y, their new minimal counts can be computed as the minimum between:

1. The minimal counts if we perform the swap (so their positions change) or fake the swap (so their positions stay but count increases).

Hmm. Let's model this step by step.

Let's suppose that before processing the current swap (x, y), the minimal fake counts are stored in a dictionary called 'prev'.

Now, when processing the swap (x, y), for positions other than x and y, their counts are the same as prev. For x and y, new possibilities arise.

For position x in prev:

Option 1: perform the swap. The new position is y. The fake count is prev[x].

Option 2: fake the swap. The position remains x. The fake count is prev[x] + 1.

For position y in prev:

Option 1: perform the swap. The new position is x. The fake count is prev[y].

Option 2: fake the swap. The position remains y. The fake count is prev[y] + 1.

For other positions, like z, their prev[z] is carried over, and during the swap, if we perform it, they remain z (so no change), or if we fake, they remain z but count increases by 1. But the minimal for z after this swap is min(prev[z], prev[z] + 1) → prev[z]. So, for z, the minimal remains prev[z].

Wait, but that's only if we have some way to reach z by either performing or faking. So, for other positions, the minimal fake count is the same as before. So, during the swap, we can carry forward all the previous entries except for x and y.

So, the approach would be:

After each swap, the new minimal counts for all positions are the same as before, except for x and y, which are updated based on the possible transitions from their previous values and the transitions from each other.

So, for each swap (x, y), the new possible counts for x and y are:

new_x = min(prev[y] (from performing the swap), prev[x] + 1 (from faking)).

new_y = min(prev[x] (from performing the swap), prev[y] + 1 (from faking)).

Wait, but what if x or y were not present in prev before the swap? For example, if after previous swaps, the special ball cannot be in x or y, then processing this swap might allow it to reach x or y.

So, during each swap, the minimal fake counts for x and y are computed as follows:

new_x is the minimum between:

- prev[y] (if we perform the swap, and the previous position was y, which would swap to x)

- prev[x] + 1 (if we fake the swap, so x stays and adds 1 to fake count)

Similarly, new_y is the minimum between:

- prev[x] (if we perform the swap, previous x becomes y)

- prev[y] + 1 (if we fake, so y stays and adds 1)

But what if the previous positions didn't include y or x? Then those options aren't possible. So we have to consider the current possible positions.

So, for the current swap (x, y):

- For new_x:

We can get x by either:

a) Being at x in prev and faking the swap (count increases by 1).

b) Being at y in prev and performing the swap (count remains same, moves to x).

So new_x is the minimum of (prev[x] + 1) if x was present, and (prev[y]) if y was present. If neither x nor y were present, then new_x is not possible.

Similarly for new_y:

new_y is the minimum of (prev[y] + 1) if y was present, and (prev[x]) if x was present.

But also, all other positions (except x and y) remain the same. So, the new state is all the previous positions (except x and y), plus x and y updated with the new minimal counts.

Wait, but how? Because for other positions (like z not x or y), performing the swap doesn't change their position. So, for those positions, the minimal fake count is the same as prev[z], because performing the swap (cost 0) gives the same position and cost as before, while faking (cost +1) would result in a higher cost. So the minimal is the same as before.

But if z is present in prev, then in the new state, z's count is prev[z], and if we fake the swap, it's prev[z] + 1, which is worse. So the minimal remains prev[z].

So, for all positions except x and y, the minimal fake count remains the same as before. So, the new state after the swap is:

All positions in prev except x and y, plus the new x and y with their computed values.

But how do we compute the new x and y?

Let's think of it step by step:

Initialize a dictionary (current) which starts with {k: 0}.

For each swap (x, y) in the m swaps:

    Create a new dictionary (new_current).

    For all positions pos in current, except x and y, add them to new_current with their current value. Because for those positions, during the swap, the best option is to perform the swap (cost remains the same) and keep their position. So their minimal fake count remains the same as before.

    Now, handle x and y:

    The new x can be achieved in two ways:

        1. If prev had y, then performing the swap would move from y to x. The fake count is current[y].

        2. If prev had x, then faking the swap would leave x as x, with fake count current[x] + 1.

    So new_x_val is the minimum of these two possibilities (if they exist).

    Similarly for new_y_val:

        1. If prev had x, then performing the swap moves x to y. So current[x] is the fake count.

        2. If prev had y, faking the swap leaves y as y, with fake count current[y] + 1.

    So new_y_val is the minimum of these two.

    So, collect all possible sources for x and y.

    Then, compare the new possible values with any existing values for x and y in new_current (from other positions?), but in our approach, for positions other than x and y, we carry over their values. Wait, no. Because the other positions are added to new_current as is, except x and y.

    Wait, no. Because for the other positions (not x or y), when you process the swap, performing the swap leaves their position the same. So their minimal fake count is the same as before. So, for example, if a position z is in current, then in new_current, z's value is the same as current[z], because performing the swap (cost 0) gives the same position and same cost as before, while faking (cost +1) would be worse. So the minimal is the same.

    So, for all positions except x and y, we can just copy them from current to new_current.

    Then, for x and y, compute the new possible values based on the previous current's x and y.

    So, the steps are:

    new_current = a copy of current, but excluding x and y.

    Then, compute possible new values for x and y.

    For x:

    candidates = []

    if y is in current:

        candidates.append(current[y])

    if x is in current:

        candidates.append(current[x] + 1)

    if candidates:

        new_x_val = min(candidates)

        if x is in new_current:

            new_current[x] = min(new_current[x], new_x_val)

        else:

            new_current[x] = new_x_val

    For y:

    candidates = []

    if x is in current:

        candidates.append(current[x])

    if y is in current:

        candidates.append(current[y] + 1)

    if candidates:

        new_y_val = min(candidates)

        if y is in new_current:

            new_current[y] = min(new_current[y], new_y_val)

        else:

            new_current[y] = new_y_val

    Then, after processing x and y, set current = new_current.

But wait, this approach would require that for each swap, we create a new dictionary and copy all the entries except x and y. However, for n=2e5, this would be O(n) per swap, leading to O(mn) time, which is 4e10 operations. That's way too slow.

So, this approach is not feasible. So we need a better way.

But perhaps, during each swap, the only positions that can be affected are x and y. All other positions are carried over as is, but their values remain the same. So, perhaps we can model current as a dictionary where only x and y are modified, and all other positions are considered to have their previous values.

Wait, but how? Because for other positions, their minimal fake count is the same as before. So, perhaps we can track the current positions and their minimal counts, and for each swap, we only need to process x and y.

But this requires that the dictionary only contains the positions that are different from the base case. But I'm not sure.

Alternatively, perhaps the minimal fake count for positions not x or y can be tracked with a default value, and the current dictionary only contains the exceptions. But this seems complicated.

Alternatively, let's think of the initial state as all positions except k having infinity (unreachable), and k having 0.

Then, for each swap (x, y), we can process the possible transitions for x and y. For other positions, their values remain the same as before.

So, the key idea is that during each swap, the only positions whose minimal fake counts can change are x and y.

Because for other positions, the minimal fake count remains the same as before.

So, for each swap (x, y), we can compute the new possible minimal counts for x and y based on the previous values of x and y.

Wait, but how? Let's see.

Let's denote:

prev_x = current.get(x, infinity)

prev_y = current.get(y, infinity)

Then, after the swap:

new_x can be min(prev_y, prev_x + 1)

new_y can be min(prev_x, prev_y + 1)

But wait:

If we perform the swap, then x's new position is y's previous position, and y's new position is x's previous position. Wait, no. Because during the swap, performing it swaps x and y. So if the special ball is at x, it moves to y; if it's at y, it moves to x. Otherwise, no change.

So, the possible transitions for x and y are:

For x:

- If we perform the swap, then any position that was y before the swap would now be x. So, the minimal fake count for x is the minimal between the current count of y (because performing the swap moves y to x) and the previous count of x plus 1 (if we fake the swap, x remains and count increases by 1).

Similarly for y.

So, the new_x = min(current[y], current[x] + 1)

new_y = min(current[x], current[y] + 1)

Wait, but current could not have x or y. For example, if x is not present in current (i.e., the special ball can't be at x before this swap), then the new_x can be current[y] (if y is present) or nothing.

So, the approach is:

For each swap (x, y):

1. Compute new_x and new_y based on the current values of x and y.

2. Create a new dictionary where:

   a. All entries except x and y are kept as before.

   b. x and y are updated to new_x and new_y, if those values are better than existing ones.

But how to efficiently compute this?

Wait, perhaps we can represent the current state as a dictionary, and for each swap, compute the new values for x and y, and then merge them into the current state, keeping the minimal values.

But even this could be O(1) per swap, since we only need to process x and y.

Wait, perhaps the key is that during each swap, the only positions that can change are x and y. All other positions' minimal fake counts remain the same as before. So, for each swap, we can compute the new possible values for x and y, and then create a new dictionary by taking the current dictionary, removing x and y (if present), and adding the new x and y with the new minimal counts.

But this would not account for other positions. Wait, but other positions are not affected, so their entries remain the same.

Wait, no. For example, if a position z is in the current dictionary (has a minimal count), then during this swap, since z is not x or y, performing the swap leaves it at z (so the same as before), and faking the swap would leave it at z with count +1. But the minimal count for z would be the same as before, because performing the swap is better (cost 0). So, the entries for z remain the same as before.

So, during the swap, the only changes are to x and y. So, the new dictionary is the current dictionary, but with x and y's values updated to new_x and new_y (if they are better than their current values).

So, the algorithm could be:

Initialize a dictionary current = {k:0}

For each swap (x, y):

    new_current = current.copy()

    # Check if y was present in current. If so, performing the swap would move it to x.
    # So new_x could be current[y] (if we perform the swap)
    # Also, if x was present, faking the swap would leave it at x, with count +1.
    # So new_x is the min of these two possibilities.

    possible_new_x = []
    if y in new_current:
        possible_new_x.append(new_current[y])
    if x in new_current:
        possible_new_x.append(new_current[x] + 1)
    if possible_new_x:
        new_x_val = min(possible_new_x)
        if x not in new_current or new_x_val < new_current[x]:
            new_current[x] = new_x_val

    # Similarly for y
    possible_new_y = []
    if x in new_current:
        possible_new_y.append(new_current[x])
    if y in new_current:
        possible_new_y.append(new_current[y] + 1)
    if possible_new_y:
        new_y_val = min(possible_new_y)
        if y not in new_current or new_y_val < new_current[y]:
            new_current[y] = new_y_val

    # Update current to new_current
    current = new_current

Wait, but this approach copies the current dictionary each time. For m=2e5 steps, this would be O(m) time, but each copy is O(1) (since dictionaries are handled by reference? No, in Python, the copy() method creates a shallow copy, which is O(1) for small dictionaries?), but even if it's O(1), this approach would process each swap in O(1) time, as for each swap, only x and y are considered, and the rest of the positions remain the same.

But wait, in Python, the dict.copy() is O(n) where n is the number of entries in the dictionary. If the current dictionary has a lot of entries, this would be O(m * size_of_dict) time, which could be O(m^2) in the worst case.

But that's a problem. So, perhaps we need a way to track the current possible positions and their minimal counts without copying the entire dictionary each time.

Alternative approach:

Instead of copying the dictionary, we can directly modify it. But during the processing of the swap, the new values for x and y are computed based on the previous values (before the swap).

So:

For each swap (x, y):

    prev_x = current.get(x, None)
    prev_y = current.get(y, None)

    new_x_val = None
    new_y_val = None

    possible = []
    if prev_y is not None:
        possible.append(prev_y)
    if prev_x is not None:
        possible.append(prev_x + 1)
    if possible:
        new_x_val = min(possible)

    possible = []
    if prev_x is not None:
        possible.append(prev_x)
    if prev_y is not None:
        possible.append(prev_y + 1)
    if possible:
        new_y_val = min(possible)

    # Now, update x and y in the current dict.

    # To avoid interference between the old and new values, we need to compute new_x and new_y based on the previous state.

    # So, first, we remove x and y from the current dict (so that their previous values are not considered in the current step)
    # Then, compute the new values based on the previous values (before removal)

    # So, save the previous values
    old_x = current.pop(x, None)
    old_y = current.pop(y, None)

    # Now, compute new_x_val and new_y_val based on old_x and old_y.

    possible_new_x = []
    if old_y is not None:
        possible_new_x.append(old_y)
    if old_x is not None:
        possible_new_x.append(old_x + 1)
    if possible_new_x:
        new_x_val = min(possible_new_x)
        current[x] = new_x_val

    possible_new_y = []
    if old_x is not None:
        possible_new_y.append(old_x)
    if old_y is not None:
        possible_new_y.append(old_y + 1)
    if possible_new_y:
        new_y_val = min(possible_new_y)
        current[y] = new_y_val

    # Also, add back the old_x and old_y if necessary (but they were popped earlier)
    # No, because the current dict now contains x and y's new values (if any)
    # Because after popping, if old_x or old_y were present, they were removed.

    # So, after popping, the current dict no longer has x and y. Then, we compute the new x and y based on old_x and old_y (the previous values), and add them to current if possible.

    # For example, if old_x was 3 and old_y was 5, then after the swap:

    # new_x_val = min(5, 3+1) → 4.

    # So current[x] is set to 4.

    # new_y_val = min(3, 5+1) →3.

    # So current[y] is set to 3.

    # The other entries in current are unaffected.

So, this approach does not require copying the entire dictionary each time. Instead, for each swap, we remove x and y from the dictionary, compute their new values based on their previous values (before removal), and then add them back if applicable.

This way, the current dictionary is modified in place, and the other entries remain as they were. So, this approach has O(1) time per swap (since each swap only involves x and y).

Wait, but in the worst case, the dictionary could have O(m) entries. But how?

Let me see: Initially, the dictionary has one entry (k). For each swap, at most two new entries (x and y) are added. But after some swaps, the number of entries could grow to O(m) entries.

For example, if each swap involves new positions x and y that were not in the current dictionary, then for each swap, the new entries x and y are added. So after m swaps, there could be up to 2m entries.

But with m up to 2e5, 2e5 entries is manageable, as dictionaries can handle that.

But in practice, many swaps may involve overlapping positions, so the size of the current dictionary may be much smaller.

Thus, this approach would be O(m) time, which is acceptable.

So, this seems like a feasible solution.

Let's test this logic with the first example.

Sample Input 1:

4 5 1

Swaps:

3 4

2 1

4 1

3 1

3 1

Sample Output:

2 0 3 1

Let's walk through the steps.

Initial current: {1:0}

Swap 1: 3 4

x=3, y=4.

prev_x = current.get(3) → None.

prev_y = current.get(4) → None.

possible_new_x: [prev_y (None) is ignored, prev_x (None) +1 is ignored. So no possible new_x_val. So new_x_val is None. Similarly for new_y_val.

So, current remains {1:0}.

Swap 2: 2 1.

x=2, y=1.

prev_x = current.get(2) → None.

prev_y = current.get(1) →0.

possible_new_x (x=2):

possible sources: prev_y (0) from performing swap (since y=1 was present). Or prev_x (None) +1 → not possible.

So new_x_val = 0.

possible_new_y (y=1):

possible sources: prev_x (None) → no, so new_y_val is prev_y (0) +1 =1.

So after this swap:

current is {1:1, 2:0}?

Wait, let's see.

Original current before swap 2: {1:0}.

Processing swap x=2, y=1:

Remove x=2 and y=1 from current. So current becomes empty.

But prev_x (2) is None, prev_y (1) is 0.

new_x_val (2) is min(0) → 0.

new_y_val (1) is min(0 +1) → 1.

So current after swap 2 becomes {2:0, 1:1}?

Wait, no. Because after popping x and y (2 and 1), the current is empty. Then, for x=2, we add it to current with new_x_val=0. For y=1, we add it with new_y_val=1.

So current after swap 2 is {2:0, 1:1}.

So now, the possible positions are 1 and 2, with counts 1 and 0, respectively.

Swap 3: 4 1.

x=4, y=1.

prev_x = current.get(4) → None.

prev_y = current.get(1) →1.

new_x_val (4) is min(prev_y (1), prev_x (None) +1 → no). So new_x_val =1.

new_y_val (1) is min(prev_x (None) → no, prev_y (1) +1 → 2. So new_y_val=2.

So after popping x=4 and y=1 from current (current now has 2:0). Then:

current[4] =1, current[1] =2.

So current is {2:0,4:1,1:2}.

Wait, but initially, current was {2:0, 1:1}.

After processing swap 3 (4,1):

We remove x=4 (not present) and y=1 (current[1] =1).

prev_x = None, prev_y=1.

For new_x (4):

possible sources: prev_y (1) → yes. So new_x_val =1.

For new_y (1):

possible sources: prev_x (None) → no. So new_y_val = prev_y +1 → 1+1=2.

So current after this swap is:

existing entries (2:0) plus 4:1 and 1:2.

So current is {2:0,4:1, 1:2}.

Swap 4:3 1.

x=3, y=1.

prev_x = current.get(3) → None.

prev_y = current.get(1) →2.

new_x_val (3) is min(prev_y (2), prev_x (None) +1 → 2).

new_y_val (1) is min(prev_x (None) → no. So new_y_val = prev_y (2) +1 →3.

So after popping x=3 and y=1 (current becomes {2:0,4:1}).

Then, new_x_val for 3 is 2. So current[3] =2.

new_y_val for 1 is 3. So current[1] =3.

Current now is {2:0,4:1,3:2,1:3}.

Swap 5:3 1.

x=3, y=1.

prev_x = current[3] →2.

prev_y = current[1] →3.

new_x_val (3) is min(prev_y (3), prev_x (2)+1=3) → min(3,3)=3.

new_y_val (1) is min(prev_x (2), prev_y (3)+1=4) → min(2,4) →2.

So after popping x=3 and y=1 from current (current is {2:0,4:1}).

Then, new_x_val for 3 is 3. So current[3] =3.

new_y_val for 1 is 2. So current[1] =2.

So after swap 5, current is {2:0,4:1,3:3,1:2}.

Now, after all swaps, the current dict contains:

1:2, 2:0, 3:3, 4:1.

So for positions 1-4:

position 1:2, position 2:0, position3:3, position4:1.

Which matches the first sample output.

So the algorithm works for this case.

Another test case.

Sample Input 2:

5 7 4

Output: 2 2 0 3 1.

Let's see.

Initial current: {4:0}.

Swap 1:3 2.

x=3, y=2.

prev_x: None, prev_y: None.

No changes. current remains {4:0}.

Swap 2:3 2.

Same as swap 1. No change.

Swap 3:4 2.

x=4, y=2.

prev_x:0 (current[4]=0).

prev_y: None.

new_x (4):

possible sources: prev_y (None) → no. prev_x (0) +1 →1.

new_x_val =1.

new_y (2):

possible sources: prev_x (0) → yes. new_y_val=0.

So after this swap, current becomes {2:0, ...?}.

Wait:

Initial current is {4:0}.

Processing swap (4,2):

Remove 4 and 2 (current becomes empty).

prev_x (4) is 0, prev_y (2) is None.

new_x_val (4): possible sources are prev_y (None) → no, prev_x (0) +1 →1. So new_x_val=1.

new_y_val (2): possible sources are prev_x (0) → yes, so new_y_val=0.

So current becomes {4:1, 2:0}.

Swap 3 done.

Swap 4:3 4.

x=3, y=4.

current has 4:1, 2:0.

prev_x=3 is not present (prev_x is None).

prev_y=4 is 1.

new_x_val (3):

possible sources: prev_y (1) → yes. So new_x_val=1.

new_y_val (4):

possible sources: prev_x (None) → no. prev_y (1)+1 →2. So new_y_val=2.

So after this swap, current is {2:0,3:1,4:2}.

Swap 5:4 1.

x=4, y=1.

prev_x=4:2.

prev_y=1: not present.

new_x_val (4):

prev_y (None) → no. prev_x (2) +1 →3.

new_y_val (1):

prev_x (2) → yes. new_y_val=2.

So after this swap, current becomes {2:0,3:1,4:3,1:2}.

Swap 6:3 2.

x=3, y=2.

prev_x=3:1.

prev_y=2:0.

new_x_val (3) → min(prev_y (0), prev_x (1)+1 → 2 → min(0,2)=0.

new_y_val (2) → min(prev_x (1), prev_y (0)+1 →1 → min(1,1)=1.

So after popping 3 and 2 from current (current has 4:3,1:2).

new_x (3) is 0.

new_y (2) is 1.

So current becomes {4:3,1:2,3:0,2:1}.

Swap 7:5 2.

x=5, y=2.

prev_x=5: not present.

prev_y=2:1.

new_x_val (5) → prev_y (1) → yes. So new_x_val=1.

new_y_val (2) → prev_x (None) → no. prev_y (1) +1 →2.

So after popping 5 and 2 from current (current has 4:3,1:2,3:0).

new_x (5) →1.

new_y (2) →2.

So current becomes {4:3,1:2,3:0,5:1,2:2}.

So after all swaps, the minimal fake counts for each position:

1:2, 2:2, 3:0, 4:3,5:1.

Which matches the sample output.

So this approach works.

Thus, the algorithm is:

- Initialize a dictionary (current) with the starting position k and 0 fakes.

- For each swap (x, y):

   a. Remove x and y from the current dict, storing their previous values.

   b. Compute the new possible values for x and y based on the previous values.

   c. Update the current dict with the new values for x and y, if applicable.

After processing all swaps, for each position from 1 to n, if it's present in the current dict, output the minimal fake count. Otherwise, output -1.

So, in code, we can implement this as follows:

We use a dictionary (like a Python dict) to track the current positions and their minimal fake counts.

For each swap, we extract the x and y values, then compute the new x and y based on the previous state.

Now, let's code this.

But in Python, dictionaries are mutable, so we can modify them in place.

So, the code steps are:

Read n, m, k.

Read the m swaps into a list.

Initialize current = {k: 0}.

For each x, y in the swaps:

    prev_x = current.get(x, None)
    prev_y = current.get(y, None)

    # Remove x and y from current
    if x in current:
        del current[x]
    if y in current:
        del current[y]

    # Compute new_x_val and new_y_val
    new_x_val = None
    new_y_val = None

    # For new_x_val (x)
    candidates = []
    if prev_y is not None:
        candidates.append(prev_y)
    if prev_x is not None:
        candidates.append(prev_x + 1)
    if candidates:
        new_x_val = min(candidates)

    # For new_y_val (y)
    candidates = []
    if prev_x is not None:
        candidates.append(prev_x)
    if prev_y is not None:
        candidates.append(prev_y + 1)
    if candidates:
        new_y_val = min(candidates)

    # Update current with new values if they are better.
    if new_x_val is not None:
        if x in current:
            if new_x_val < current[x]:
                current[x] = new_x_val
        else:
            current[x] = new_x_val
    if new_y_val is not None:
        if y in current:
            if new_y_val < current[y]:
                current[y] = new_y_val
        else:
            current[y] = new_y_val

After all swaps, for each position from 1 to n:

    print(current.get(i, -1), end=' ')

But wait, in the code above, when we process x and y, we first delete them from current. Then compute their new values based on prev_x and prev_y (the values before deletion). Then, we add them back if applicable.

Yes. So, the code correctly captures the previous state.

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().split())
    swaps = [tuple(map(int, input_stream.readline().split())) for _ in range(m)]
    
    current = {k: 0}
    
    for x, y in swaps:
        # Extract previous values and remove x, y from current
        prev_x = current.get(x)
        prev_y = current.get(y)
        if x in current:
            del current[x]
        if y in current:
            del current[y]
        
        # Compute new_x and new_y
        new_x = None
        new_y = None
        
        # For x
        candidates = []
        if prev_y is not None:
            candidates.append(prev_y)
        if prev_x is not None:
            candidates.append(prev_x + 1)
        if candidates:
            new_x = min(candidates)
        
        # For y
        candidates = []
        if prev_x is not None:
            candidates.append(prev_x)
        if prev_y is not None:
            candidates.append(prev_y + 1)
        if candidates:
            new_y = min(candidates)
        
        # Update current with new_x and new_y if they are better
        if new_x is not None:
            if x in current:
                if new_x < current[x]:
                    current[x] = new_x
            else:
                current[x] = new_x
        if new_y is not None:
            if y in current:
                if new_y < current[y]:
                    current[y] = new_y
            else:
                current[y] = new_y
    
    # Prepare the output
    output = []
    for i in range(1, n+1):
        output.append(str(current.get(i, -1)))
    print(' '.join(output), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 7 4
3 2
3 2
4 2
3 4
4 1
3 2
5 2
""",
            "output": \
"""\
2 2 0 3 1
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

</think>

```python
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    swaps = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    
    current = {k: 0}
    
    for x, y in swaps:
        # Extract previous values and remove x, y from current
        prev_x = current.get(x)
        prev_y = current.get(y)
        if x in current:
            del current[x]
        if y in current:
            del current[y]
        
        # Compute new_x and new_y
        new_x = None
        new_y = None
        
        # For x
        candidates = []
        if prev_y is not None:
            candidates.append(prev_y)
        if prev_x is not None:
            candidates.append(prev_x + 1)
        if candidates:
            new_x = min(candidates)
        
        # For y
        candidates = []
        if prev_x is not None:
            candidates.append(prev_x)
        if prev_y is not None:
            candidates.append(prev_y + 1)
        if candidates:
            new_y = min(candidates)
        
        # Update current with new_x and new_y if they are better
        if new_x is not None:
            if x in current:
                if new_x < current[x]:
                    current[x] = new_x
            else:
                current[x] = new_x
        if new_y is not None:
            if y in current:
                if new_y < current[y]:
                    current[y] = new_y
            else:
                current[y] = new_y
    
    # Prepare the output
    output = []
    for i in range(1, n+1):
        output.append(str(current.get(i, -1)))
    print(' '.join(output))

if __name__ == "__main__":
    main()
```
