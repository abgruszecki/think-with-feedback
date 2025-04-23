<think>
Okay, so I need to solve this problem where I have to count the number of beautiful fences of a certain length. Let's try to understand the problem first.

The fence is made up of boards. Each board is from one of the n types. But, the same type can't be used consecutively. Also, each subsequent board's length must equal the previous board's width. And the total length of the fence (sum of all board lengths) should be exactly l.

Wait, wait. Wait, the total length of the fence is the sum of the lengths of each board. Because each board contributes its length to the total. So for example, if the first board is placed as a x b (so length a), then the next must be length b (since the previous's width is b), and so on. So the sum of all the lengths (a_i's) of the boards in their chosen orientation must equal l.

So the problem is to find sequences of boards (with possible rotation, except squares) where consecutive types are different, and each step's length is the previous's width, and the sum of all lengths is l. And count all possible such sequences.

Hmm. So the approach is dynamic programming. Because for each step, the state depends on the previous type and the current expected length (the next board's length must be equal to the previous width). Also, we need to track the sum so far.

Let's think about possible state variables. The state could be:

- The current total length accumulated (sum of lengths so far).
- The last board's type (to ensure the next is different).
- The current expected length for the next board. Which is the same as the last board's width.

Wait, but the next board's length must be equal to the previous width. So after placing a board (in some orientation), the next board's length is fixed as the previous width. So the next board's length is determined by the previous's width.

So the state transitions would be based on the previous board's end width. So for each step, the state can be represented as (current_sum, last_type, next_required_length). Wait, but the next_required_length is determined by the previous board's width. So perhaps the state is (current_sum, last_type, current_end_length). Wait, no. Let's think.

Suppose we have a board that contributes a length of a, and its width is b. Then the next board's length must be b. So the next board's length is fixed. So the next board must be placed with length equal to the previous width. So when building a sequence, each new board's length is determined by the previous board's width.

So the state for dynamic programming could be:

- The sum accumulated so far (s).
- The last type used (t).
- The next required length (w). Because the next board's length must be w, which is the previous board's width.

Wait, no. Wait, when you have a board that is placed as a (length) x b (width), then the next board's length must be b. So the next board's length is b. So the next board can be placed either as (b, x) or (x, b) if it's not square. But the length in the next step would be x, but that's only possible if the next board is placed as x by ... no. Wait, for the next board, since the next board's length must be equal to the previous board's width, which is b. So the next board's length is fixed as b. So the next board can be placed in any orientation (if possible) such that its length is b. Then, its width becomes the next required length.

So the state for dynamic programming would be:

sum_so_far: the total sum up to this point.

last_type: the type of the previous board.

current_required_length: the length that the next board must have.

Wait, but current_required_length is determined by the previous board's width. So when we add a new board, its length must be equal to current_required_length. Then, its width becomes the new current_required_length for the next step.

So, for example:

State (s, t, w) represents that we have a partial fence of sum s, the last board was of type t, and the next board must have a length of w.

When we choose a new board of type k (k != t), which can be placed in a way that its length is w. So for each possible type k (k != t), and each possible orientation of k's board (if possible), if the length in that orientation is w, then we can add this board. The sum would increase by w, and the new required length would be the width of this new board (in the chosen orientation).

So the transitions would be:

For each state (s, t, w), and for each possible next type k != t:

Check if there's a way to place a board of type k such that its length is w. For that, the board must have either (a, b) where a == w or (b, a) where b == w, provided that it's not a square (if a == b, then rotation is not allowed). Wait, the problem says: "Vasya is allowed to turn the boards as he builds the fence. However, Vasya cannot turn square boards."

So, for a non-square board (a != b), you can rotate it, so the possible orientations are a x b and b x a. For a square board (a == b), you can't rotate, so only one orientation is possible.

So, for a board of type k with dimensions (a, b), the possible orientations are:

- If a == b: only one orientation, length a, width b (same as length).

- Else: two orientations: length a, width b; or length b, width a.

So for each board type, we can precompute all possible (length, width) pairs that are allowed. For example, for a non-square board, two possible pairs. For a square, one pair.

So for each type k, we can have a list of possible (length, width) pairs, and then for a given required length w, we check if any of those pairs has a length equal to w. If so, then using that orientation contributes a transition.

So the dynamic programming approach would track the current sum, last type, and required next length (w).

The initial state is: sum 0, no previous type (or a dummy value), and the first board can have any length. Wait, but according to the problem statement:

"the first board of the fence has an arbitrary length, and the length of each subsequent board equals the width of the previous one".

So the first board can choose any orientation (according to its type), and its length is the sum that is added. Then, the next boards must have their length equal to the previous board's width.

So the initial state is when sum is 0, and the next required length is not fixed. Wait, no. Wait, for the first board, there's no required length. So the first board's length can be any possible (from any of the possible orientations of any type), and then the next required length is the width of that first board.

So the initial transitions are for the first step. For each possible type k, and each possible orientation of k (if allowed), the sum is the length of the first board. The next required length is the width of that orientation.

So the DP can be initialized by considering all possible first steps, adding their lengths and setting the next required length to their width.

Then, for each step, we process the current sum, and for each possible next type (different from last), and next possible orientation that starts with the required length.

So the DP state is (current_sum, last_type, next_required_length).

Now, the maximum possible l is 3000, and n is up to 100. So we need to model this efficiently.

Let's think about the state space.

For sum_so_far, it can go up to 3000.

last_type can be up to n (100).

next_required_length (w) can be up to the maximum possible board dimension. Since each board has a_i and b_i up to 100, the possible w values can be up to 100.

Wait, because when you place a board, the next required length is the width of that board. The width is either a or b (for non-squares) or a (for squares). Since a and b are up to 100, the maximum possible next_required_length is 100.

So the possible values for w are up to 100.

So the state variables are:

s (sum_so_far): up to 3000.

t (last_type): up to 100.

w (next_required_length): up to 100.

So the total number of possible states is 3000 * 100 * 100 = 30,000,000. Hmm, but 3e7 is a bit big for Python, which can be slow. But perhaps it's manageable with some optimizations.

Wait, but n can be up to 100, so 3000 * 100 * 100 = 3e6? Wait, no. Let's compute: 3000 (sum) * 100 (types) * 100 (w values) = 3,000,000 * 100 = 300,000,000? Wait, wait, 3000 sum * 100 types (n) * 100 w values. 3000*100=300,000, multiplied by 100 gives 30,000,000. So 3e7 states. Hmm, that's a lot. But maybe some optimizations can be done.

Alternatively, perhaps we can model the DP in a way that tracks the current required length and last type, and sum up to s. So for each s, we can track the possible (t, w) pairs. Let's see.

The DP can be a 2D array for each s, where for each possible (t, w) pair, we have the count of ways to reach sum s with last type t and next required length w.

So for each s from 0 to l, and for each possible (t, w) pair, we track the count.

The transitions would be:

For each state (s, t, w):

If we choose a board of type k (k != t) that can have length w (with some orientation), then for each possible orientation of k where length is w:

The sum becomes s + w_new, where w_new is the length of the board (which is w, but maybe that's redundant). Wait, no. Wait, the length is w (the required next length). The sum_so_far is s. Adding this board's length (w) gives s + w. Then, the next required length is the width of this board (either a or b, depending on the orientation).

So the transition is:

new_s = s + w

new_t = k

new_w = board's width in this orientation.

So for each (t, w) in the current state for sum s, we can iterate over all possible next boards (k) and their possible orientations that can contribute a length of w, then add to new_s = s + w, new_t = k, new_w = orientation's width.

Thus, the steps are:

Initialize the DP for sum 0. Then, for each possible board type and orientation, add to sum a (the length of the first board). The next required length is b (the width of the first board). So for each first board, sum is a, last type is k, next required length is b. So the initial state is sum a, with (k, b) as the state. Each such transition contributes 1 way (since it's the first step).

Then, for each s from 1 to l, and each possible (t, w) in s, we look for transitions to s + new_length (where new_length is the next board's length, which is w). Wait, no. Wait, the next board's length must be equal to the current required length (w). So the next board's length is w, so the sum increases by w, and the new required length is the width of that board.

So the steps are:

For each possible current state (s, t, w):

If s + w exceeds l, we can't proceed. Otherwise, for each possible board type k (k != t), check if there's any possible orientation of k that has length w. For each such orientation, the new_sum is s + w. The new_t is k. The new_w is the width of the orientation. Then, add the number of ways from (s, t, w) to (new_sum, k, new_w).

So to model this, for each k in 0..n-1, and for each possible orientation of k's board, precompute the possible (length, width) pairs.

So the first step is to precompute for each board type all possible (a, b) orientations. For example:

For each board (a_i, b_i):

If a_i == b_i: only one orientation (a_i, a_i).

Else: two orientations (a_i, b_i) and (b_i, a_i).

So for each board, we can generate these possible orientations.

Once we have all possible orientations, we can for each possible w (current required length) and next board type, check if any of the orientations of the next type has length w.

So, to model the transitions efficiently, perhaps we can precompute a map for each possible (w, k) pair, the possible (width) values that would result from choosing a board of type k with length w.

For example, for each k, create a dictionary where the key is the possible length (w), and the value is a list of possible widths (since a board can be placed in different orientations, but only those orientations where length is w).

Wait, but for each board type k, and possible orientation, we can have a (length, width) pair. So for each (k, w) pair, collect all possible widths from the orientations of k where the length is exactly w.

So for each k in 0..n-1:

- create a list of (length, width) pairs.

Then, for each possible w (the current required length), for the next board type k (k != t), check if there exists any (length, width) in k's list where length == w. For each such (length, width), the transition is possible.

So during the DP, when processing a state (s, t, w), and considering a next type k (k != t), we look up all possible widths in k's orientations that have length w. Then, for each such width, we can add to new_sum = s + w, new_t = k, new_w = width.

So the steps are:

1. Precompute for each board type, all possible (length, width) orientations.

2. For each board type k, build a dictionary (or a list) that maps possible lengths to a list of possible widths. So for example, for type k, if it has orientations (a, b) and (b, a), then for length a, add b; for length b, add a (if a != b). For a square board (a = b), then only length a maps to a.

3. Then, in the DP transitions, for a given current state (s, t, w), and for each possible k != t, check if k has any orientations where the length is w. For each such width in k's possible widths for length w, we can transition to s + w, k, new_width, adding the number of ways.

So now, the DP can be structured as follows:

- We have a dp array where dp[s][t][w] is the number of ways to reach sum s with last type t and next required length w.

But given that the sum can be up to 3000, t up to 100, and w up to 100, the array could be represented as a dictionary of dictionaries, but in Python, perhaps using a list of lists of dictionaries would be more efficient. However, considering memory constraints, perhaps we can model the DP using two layers: current and next. Since for each step, when processing sum s, we can generate transitions to s + w (which is s plus the current required length w). Wait, but the new_sum would be s + w (the next board's length is w). So for each state (s, t, w), the transitions would be to new_sum = s + w, and the new_w is the width of the next board's orientation.

So for each possible sum s, we process all the (t, w) pairs for that sum, and generate transitions to s + w. But s + w must be <= l.

So the DP can be built incrementally. We can process sums in order from 0 to l. For each sum s, we process all (t, w) pairs, and for each possible transition, add to the new_sum's states.

But since the sum s can't exceed l, for each s in 0 to l:

For each (t, w) in dp[s], we look for transitions to s + w (which must be <= l). Then, for each possible k != t, check if k has any orientations with length w. For each such k and possible width, add to dp[s + w][k][width] the current count from dp[s][t][w].

But the initial state is sum 0, and we need to process the first board. Because the first board can be any type, any orientation. So for sum 0, the state is not really applicable. So perhaps we need to initialize the DP for sum s = 0 as a dummy state, but then process all possible first boards.

Wait, the first board can be any of the possible orientations of any type. Each first board contributes to sum a (its length) and sets the next required length to its width.

So the initial step is for sum 0, but there's no previous type. So for the first board, all types are allowed, and all possible orientations are considered.

So the initial state is sum 0, and the next required length can be any possible (but in reality, the first step's next required length is the sum of the first board's length. Wait, no. Wait, the first board's sum is its length. Then, the next required length is the first board's width. So for the first board, sum is 0 + a (length). Then the next required length is b (width).

So the initial step is to generate all possible first boards, which contribute to sum s = a (their length) and set the next required length to b (their width). Also, the last type is the type of the board.

So the initial setup is:

For each type k (0 <= k < n), for each possible orientation (a, b) of that type (including rotated ones if applicable):

Add 1 to dp[a][k][b], and also sum a must be <= l.

So after initializing all possible first steps, we can proceed to process sum s from 1 to l.

Wait, but the first sum can be as small as 1 (if the board's length is 1) up to, say, 100 (since a_i and b_i are up to 100). So the DP for s = a is initialized.

So, the steps are:

1. Preprocess all board types into their possible (a, b) orientations.

2. For each possible first board (any type, any orientation):

   a. If a (the length) exceeds l, skip.

   b. Add to dp[a][k][b] += 1.

3. Then, for each sum s from 1 to l:

   a. For each (t, w) in dp[s]:

      i. For each type k not equal to t:

         - Check if k has any orientations where length is w.

         - For each such possible width in k's orientations when length is w:

             * new_sum = s + w

             * if new_sum > l: skip.

             * add dp[s][t][w] to dp[new_sum][k][width].

So the key is to precompute for each type k, the possible length to widths mappings.

So, how to implement this?

First, for each type, precompute the possible (length, width) pairs.

Then, for each type k, create a dictionary that maps possible lengths to a list of possible widths. For example, if type k can be placed as (a, b) and (b, a), then for length a, the possible width is b; for length b, the possible width is a. But if a == b, then only a is present once.

So, code steps:

Read n and l.

Then, read each of the n boards, and for each, generate the possible orientations.

For each board (a, b):

if a == b:

   add (a, a) as the only orientation.

else:

   add (a, b) and (b, a).

Then, for each type, create a dict (length_to_widths) that for each possible length in that type's orientations, lists all possible widths.

For example, for a board (2,3), the possible orientations are (2,3) and (3,2). So for length 2, the width is 3; for length 3, the width is 2. So the dict for this type would be {2: [3], 3: [2]}.

For a square board (2,2), the dict would be {2: [2]}.

Once this is done, the DP can proceed.

Now, the DP can be represented as a list of dictionaries. For each sum s, we have a dictionary where the keys are tuples (t, w), and the value is the count of ways.

But given that s can be up to 3000, and per s, the possible (t, w) pairs are up to 100*100=10,000 (since n is 100, w up to 100), the memory could be manageable.

But in Python, using a list of dictionaries for each s from 0 to l is feasible. For example, dp is a list of length l+1, each element is a dictionary (or a default dict) that maps (t, w) to the count.

So, the initial steps would be:

Initialize a list dp of size l+1, each element is a default dictionary (like Counter) that holds (t, w) as keys and counts as values.

For the first step:

For each type k in 0..n-1:

   for each (length, width) in the orientations of k:

       if length > l:

           continue

       dp[length][ (k, width) ] += 1

Wait, but for the first step, the sum is length (the first board's length), and the next required length is width (so the state is (k, width)).

Yes.

Then, for each sum s in 1 to l:

   for each (t, w) in dp[s]:

       current_count = dp[s].get( (t, w), 0 )

       if current_count == 0:

           continue

       for k in 0..n-1:

           if k == t:

               continue

           # Check if k has any orientations where length is w.

           possible_widths = type_k's length_to_widths.get(w, [])

           for width in possible_widths:

               new_sum = s + w

               if new_sum > l:

                   continue

               dp[new_sum][ (k, width) ] += current_count

               dp[new_sum][ (k, width) ] %= MOD

But this is O(l * n * average (t, w) per s * n * average possible widths per k and w).

Given that l is up to 3000, and for each s, the (t, w) pairs per s could be up to 100*100=1e4, and for each (t, w), you loop over n types (excluding t), and for each k, possible widths (could be up to 2 per k, if non-square and w matches one of the lengths), this might be acceptable.

But in the worst case, it's O(3000 * 1e4 * 100 * 2) = 3e6 * 2e2 = 6e8 operations, which is way too much for Python (which can handle about 1e8 operations per second). So this approach may not be feasible for the time constraints.

Hmm, so this approach may not be efficient enough. Need to find optimizations.

Alternative idea: precompute for each possible (w, k) pair, the possible transitions. For each k, precompute a map from possible w (length) to list of widths. Then, for each (t, w) state, for each possible k (k != t), check if k has a way to use w as the length. If so, then for each width in the list, transition to new_sum = s + w, new state (k, width).

But how to speed this up?

Another idea: for each k, precompute all possible (length, width) pairs, and then for each possible (t, w) state, iterate over all k != t, and check if k can have a length of w. For each such k, get the possible widths and proceed.

But the problem is that for each (t, w) state, you have to check all n-1 other k's.

Alternative approach: for each possible w (length), precompute a list of types k that can have a length of w. Then, for a given (t, w) state, you can iterate over all k in the list for w, except t.

This way, instead of iterating over all possible k (100 types) each time, you can iterate only over the k's that are relevant for the current w. For example, if the current w is 2, and only 5 types have a possible orientation with length 2, then you only process those 5 types (excluding the current t).

So this can reduce the number of k's considered per (t, w) state.

So, let's precompute for each possible w, a list of k's (types) that have at least one orientation with length w.

Then, for each (t, w) state in the DP, we can look up the list of k's for this w, and process only those k's (excluding t).

This would save time in the inner loop.

So, steps to precompute for each w, the list of k's that can be used with length w.

Let's create a dictionary called length_to_types, where for each possible w, we have a list of (k, possible_widths) pairs. But perhaps even better, for each w, store a list of (k, [width1, width2, ...]) pairs. But maybe for each w, and each k in the list, the possible widths when using w as length.

But perhaps a better way is to have for each w, a list of (k, widths), where widths is the list of possible widths for type k when length is w. So for a given w, when we process a (t, w) state, we can look up the list of k's (excluding t) that have possible widths for w, and then for each such k and width, add transitions.

So, how to build this:

For each type k in 0..n-1:

   for each (length, width) in k's orientations:

       if length not in length_to_types:

           length_to_types[length] = []

       # Check if k is already in the list for this length. Maybe not, but for each occurrence, add (k, width) to the list.

       # Wait, for each (length, width) pair in k's orientations, add to length_to_types[length] the (k, width) pair.

       # So for a board with two orientations (like (a, b) and (b, a)), if a != b, then length_to_types[a] will have (k, b), and length_to_types[b] will have (k, a).

So length_to_types is a dictionary where the keys are possible lengths (w), and the values are lists of tuples (k, width), where k is a type and width is the corresponding width when using length w.

This way, when we have a current (t, w) state, we can look up all (k, width) pairs in length_to_types.get(w, []), and for each such (k, width), if k != t, we add the transition.

This would save us from checking all possible k's each time, and instead only check the k's that have a possible orientation with length w.

So, this is a crucial optimization.

So, the steps are:

1. Precompute for each type k, its possible (length, width) orientations.

2. For each (length, width) in all types' orientations, add (k, width) to length_to_types[length].

Then, in the DP transitions, for a given (t, w) state:

- Look up all (k, width) pairs in length_to_types.get(w, []).

- For each such (k, width) where k != t:

   new_sum = s + w

   if new_sum > l: skip

   dp[new_sum][k][width] += dp[s][t][w]

So, this way, for each (t, w) state, instead of iterating over all possible k (n possibilities), we only iterate over the k's that have a possible length of w, which can be much fewer. For example, if only 5 types can have a length of w, then we process 5 k's instead of 100.

This should significantly reduce the number of transitions processed.

Now, let's model the DP accordingly.

So, the code outline is:

Read n and l.

MOD = 1e9 +7

precompute for each type, the possible (length, width) orientations.

precompute length_to_types: for each possible length w, a list of (k, width) pairs where k is a type that can have length w, and width is the corresponding width.

Then, initialize the DP:

dp is a list of dictionaries. Each dp[s] is a dictionary mapping (t, w) to count.

Initialize dp as a list of default dictionaries (like using a list of defaultdict(Counter)), but perhaps using a list of dictionaries where each element is a defaultdict(int) or similar.

But in Python, using a list of dictionaries for each s, and each dictionary maps (t, w) tuples to counts.

But for speed, perhaps using a list of defaultdicts of defaultdicts.

Alternatively, for each s, use a dictionary where keys are tuples (t, w) and values are the counts.

So:

Initialize dp as a list of empty dictionaries, with length l +1.

For s in 0 to l:

   dp[s] = {}

Then, for the first step:

For each type k in 0..n-1:

   for (a, b) in orientations[k]:

       if a > l:

           continue

       key = (k, b)

       if a not in dp:

           dp[a] = {}

       if key not in dp[a]:

           dp[a][key] = 0

       dp[a][key] += 1

       dp[a][key] %= MOD

Then, for each sum s from 1 to l:

   if s not in dp:

       continue

   for (t, w_current) in list(dp[s].keys()):  # Iterate over current states (t, w_current)

       current_count = dp[s].get( (t, w_current), 0 )

       if current_count == 0:

           continue

       # Look up all possible k and widths that can have length w_current

       for (k, new_width) in length_to_types.get(w_current, []):

           if k == t:

               continue

           new_sum = s + w_current

           if new_sum > l:

               continue

           key = (k, new_width)

           # Update dp[new_sum]

           if new_sum not in dp:

               dp[new_sum] = {}

           if key not in dp[new_sum]:

               dp[new_sum][key] = 0

           dp[new_sum][key] = ( dp[new_sum][key] + current_count ) % MOD

Finally, the answer is the sum of all counts in dp[l], for all (t, w) pairs (since once the sum is l, the fence is complete regardless of what the next required length is).

So, the total number of ways is the sum of all values in dp[l].values().

So, in code:

ans = sum(dp[l].values()) % MOD

But what if l is 0? Well, the problem states that l is at least 1. So no need to handle that.

Now, testing the first example:

Sample 1:

Input:

2 3

1 2

2 3

The possible orientations for type 0:

(1,2) and (2,1). But since it's not square.

So for type 0, the orientations are (1,2) and (2,1).

For type 1: (2,3) and (3,2).

First, initial step:

For each orientation:

Type 0:

orientations are (1,2) and (2,1).

So for (1,2), sum is 1, and next required length is 2. So added to dp[1][ (0, 2) ] +=1.

For (2,1), sum is 2, added to dp[2][ (0, 1) ] +=1.

Type 1:

(2,3) and (3,2).

(2,3): sum 2, next required 3. Added to dp[2][ (1,3) ] +=1.

(3,2): sum 3, next required 2. Added to dp[3][ (1,2) ] +=1.

Then, for sum=1, we process (0,2). Then look up length_to_types[2] which includes:

Looking at the precomputed length_to_types:

For length 2:

Which types have orientations where length is 2?

Type 0: orientation (2,1) has length 2.

Type 1: orientation (2,3) has length 2.

So length_to_types[2] would contain (0, 1) and (1, 3).

So for the state (0, 2), when sum is 1:

For each (k, new_width) in length_to_types[2], which are (0, 1) and (1,3).

But k must not be equal to t=0. So (0, 1) is skipped. (1,3) is considered.

So new_sum = 1 + 2 =3.

Add to dp[3][ (1,3) ] += current_count (1).

But current_count is the value of dp[1][ (0,2) ] which is 1.

So dp[3][ (1,3) ] becomes 1.

Then, for sum=2:

dp[2] has:

(0,1) (count 1) from type 0's (2,1) orientation.

(1,3) (count 1) from type 1's (2,3) orientation.

Processing (0,1):

current_count is 1.

Looking up length_to_types[1], which is orientations where length is 1.

Which types have that?

Type 0's orientation (1,2) has length 1. So (0,2) is in length_to_types[1].

So for (0,1), sum is 2, and the next required length is 1.

Looking up length_to_types[1] gives (0,2).

So k can be 0, but current t is 0 (k can't be same as t). So this is skipped.

Also, any other types? Suppose there's another type with length 1. But sample input only has two types.

So no transitions from (0,1) in sum 2.

Then, processing (1,3) in sum 2:

current_count is 1.

look up length_to_types[3].

Which types have orientations with length 3? Type 1's orientation (3,2) has length 3, and possibly other types. In this case, only type 1 has that.

So length_to_types[3] contains (1, 2).

But k can't be 1 (same as current t=1). So no transitions.

So sum 2's processing doesn't generate any new transitions.

Then, sum=3:

dp[3] has:

(1,2) (count 1) from type 1's orientation (3,2).

(1,3) (count 1) from the transition from sum 1, (0,2).

For each of these:

Processing (1,2):

sum is 3.

Looking up length_to_types[2] gives (0,1) and (1,3).

But k can't be 1.

So for (0,1):

new_sum = 3 + 2 =5, which is more than l=3. So skipped.

Processing (1,3):

sum is 3.

Looking up length_to_types[3] gives (1,2). But k can't be 1. So no transitions.

So the total is sum of dp[3] which is 1 (from (1,2)) and 1 (from (1,3)), total 2. Which matches the sample.

So this approach works.

Another sample: input 1 2, board (2,2). Since it's square, only one orientation (2,2). So first board's sum is 2, which equals l=2. So count is 1.

So the code would add to dp[2][ (0, 2) ] +=1.

So the answer is 1.

The third sample: the code needs to handle multiple transitions.

Now, the problem with the code is how to efficiently manage the DP. In Python, using dictionaries for each sum is manageable, but for performance, perhaps using a list of dictionaries, and pre-allocating the sum steps.

But given the time constraints, perhaps this approach is feasible.

Now, code implementation.

First, preprocess the orientations for each type.

Then build the length_to_types map.

Then initialize the DP.

Then process each sum in order.

Now, implement this in Python.

Let's code:

Read n and l.

Then, for each type, generate orientations.

For each type, add to orientations list the possible (a, b) pairs.

Then build length_to_types as a defaultdict(list).

Then, for each type index k:

   for (length, width) in orientations[k]:

       add (k, width) to length_to_types[length].

Then initialize dp as a list of empty dictionaries.

Then for each sum from 0 to l, dp[s] is a dict.

Then, for each type k, for each (a, b) in orientations[k]:

   if a > l: skip.

   add to dp[a][ (k, b) ] +=1.

Then, for each s in 1 to l:

   if s not in dp:

       continue.

   for (t, w_current) in list(dp[s].keys()):

       current_count = dp[s][ (t, w_current) ]

       for (k, new_width) in length_to_types.get(w_current, []):

           if k == t:

               continue

           new_sum = s + w_current

           if new_sum > l:

               continue

           # add to dp[new_sum][ (k, new_width) ]

           key = (k, new_width)

           dp[new_sum][key] = ( dp[new_sum].get(key, 0 ) + current_count ) % MOD

Finally, the answer is sum of all counts in dp[l].

So the code would look like this:

But how to handle the dp as a list of dictionaries. Let's use a list of defaultdicts, but in Python, perhaps it's better to use a list of default dicts, but for efficiency, perhaps using a list of regular dictionaries.

So here's the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, l = map(int, input_stream.readline().rstrip("\n").split())

    types = []
    for _ in range(n):
        a, b = map(int, input_stream.readline().rstrip("\n").split())
        orientations = []
        if a == b:
            orientations.append( (a, b) )
        else:
            orientations.append( (a, b) )
            orientations.append( (b, a) )
        types.append(orientations)

    # Precompute length_to_types: for each possible length, list of (k, width)
    from collections import defaultdict

    length_to_types = defaultdict(list)
    for k in range(n):
        for a, b in types[k]:
            length_to_types[a].append( (k, b) )

    # Initialize DP
    dp = [dict() for _ in range(l+1)]

    # Initialize first step
    for k in range(n):
        for a, b in types[k]:
            if a > l:
                continue
            key = (k, b)
            if key in dp[a]:
                dp[a][key] = (dp[a][key] + 1) % MOD
            else:
                dp[a][key] = 1

    # Process transitions
    for s in range(1, l+1):
        if not dp[s]:
            continue
        # Iterate over all (t, w_current) in dp[s]
        for (t, w_current), cnt in list(dp[s].items()):
            # Iterate over all possible (k, new_width) for w_current
            for (k, new_width) in length_to_types.get(w_current, []):
                if k == t:
                    continue
                new_sum = s + w_current
                if new_sum > l:
                    continue
                key = (k, new_width)
                if key in dp[new_sum]:
                    dp[new_sum][key] = (dp[new_sum][key] + cnt) % MOD
                else:
                    dp[new_sum][key] = cnt % MOD

    # Sum all possibilities in dp[l]
    result = sum(dp[l].values()) % MOD

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2
2 2
""",
            "output": \
"""\
1
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

This code should handle the samples correctly.

Now, for the third sample, which is larger, but the code should handle it.

Now, possible optimizations:

In Python, using a list of dictionaries can be slow. So perhaps, for each sum s, use a defaultdict to track the (t, w) counts. However, in the code above, we're using a list of regular dictionaries. So for each key in the dictionary, we can directly check and update.

Another possible optimization is to process the sum in a BFS-like manner, only processing sums that have been reached. For example, keep a queue or a set of sums that have entries in dp. This way, for large l, but sparse sums, we can avoid iterating all 3000 sums.

But given the problem constraints (l up to 3000), this may not be necessary.

Another optimization is to use a single dictionary for the current sum, and another for the next sum. But perhaps the code as written is sufficient.

Now, memory considerations:

Each state (t, w) for each sum s. For s up to 3000, t up to 100, w up to 100. So per sum, the number of (t, w) pairs is up to 100*100=10,000. So for 3000 sums, 3e4 * 1e4 = 3e8 entries. But in reality, many sums are not reachable, so the actual numbers are much smaller. But using dictionaries per sum s would store only the existing (t, w) pairs, so memory should be manageable.

So the code should work.

Testing the code for the third sample would require more detailed analysis, but given that the code works for the first two samples, it's likely correct.
</think>

```python
MOD = 10**9 + 7

n, l = map(int, input().split())

types = []
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        types.append([(a, b)])
    else:
        types.append([(a, b), (b, a)])

from collections import defaultdict

length_to_types = defaultdict(list)
for k in range(n):
    for a, b in types[k]:
        length_to_types[a].append((k, b))

dp = [dict() for _ in range(l + 1)]

for k in range(n):
    for a, b in types[k]:
        if a > l:
            continue
        key = (k, b)
        dp[a][key] = dp[a].get(key, 0) + 1

for s in range(1, l + 1):
    if not dp[s]:
        continue
    for (t, w_current), cnt in list(dp[s].items()):
        for k, new_width in length_to_types.get(w_current, []):
            if k == t:
                continue
            new_sum = s + w_current
            if new_sum > l:
                continue
            key = (k, new_width)
            dp[new_sum][key] = (dp[new_sum].get(key, 0) + cnt) % MOD

result = sum(dp[l].values()) % MOD if l <= 3000 else 0
print(result)
```
