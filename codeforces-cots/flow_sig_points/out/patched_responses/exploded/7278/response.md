<think>
Okay, let's try to figure out this problem. So the task is to find the minimal number of wooden bars needed to make two door frames. Each door frame requires two vertical sides of length a and one top of length b. Since there are two doors, total we need 4a (two vertical per door, two doors) and 2b (one top per door). So total required lengths are 4a + 2b. But the problem is to cut these pieces from the bars of length n, with each piece being a solid part of a bar. Each bar can be cut into multiple pieces as long as each piece is a continuous part of the bar. The goal is to minimize the number of bars used.

First, I need to model how the pieces can be arranged into the bars. Each bar can be cut into several pieces, but each piece's length must be <= n, and each required piece (each a or b) must come from a single bar's part. So for example, if a bar is of length 8, and the required pieces are 1,2,1,2, etc., then maybe we can fit all of them into one bar.

The challenge is to find the minimal number of bars such that all 4a and 2b lengths can be covered by the sum of the pieces in each bar, and each required piece (like each a, each a again, etc.) is a solid piece from a bar. So the problem is similar to a bin packing problem, but with the twist that the sum of the required pieces in each bar must not exceed n, and each required piece must fit as a single segment in a bar.

Wait, no. Each bar can be split into multiple pieces. For example, a bar of length 10 can be split into a piece of 3, 5, and 2, as long as 3+5+2=10. Wait, no. Wait, no. Because the sum of the pieces can't exceed the bar's length. Wait, each piece is part of the bar. So the sum of the lengths of the pieces cut from a bar must be <= n. Because each bar is of length n, and when you cut it into pieces, the sum of those pieces can't exceed n, right? Because you can't have overlapping parts. So, for example, if a bar is length 8, and you need to get pieces of 1,2,5, that sum to 8, so that's okay. But if you need pieces 3 and 6, sum is 9, which is more than 8, so that's impossible. So each bar can contribute multiple pieces, but their sum must be <=n.

So the problem reduces to packing all 4a and 2b pieces into the minimal number of bars (each of length n), such that for each bar, the sum of the pieces in it is <=n. Each piece must be exactly a or exactly b. So all pieces are either a or b, and there are 4a pieces and 2b pieces.

Wait no. Wait, each of the vertical sides is a piece of length a. So there are 4 pieces of a (since two per door, two doors) and 2 pieces of b (one per door, two doors). So total required pieces: 4 a's and 2 b's.

So each bar can contain multiple a's and b's, but the sum of their lengths must not exceed n. For example, if a bar is of length 8, and a=1, b=2, then we can fit 4 a's and 2 b's into a single bar: 4*1 + 2*2 = 4+4=8. Which is exactly the first example. So the sum must be <=n.

But the order in which they are cut doesn't matter. So the key is to find how to optimally pack these 4 a's and 2 b's into as few bars as possible.

So the problem is a bin packing problem where the items are 4 a's and 2 b's. Each bin (bar) can have a sum of items' lengths <=n. We need to find the minimal number of bins required.

But bin packing is NP-hard, but here the number of items is small: 4+2=6 items. So maybe we can brute-force all possible combinations.

Wait, but even with 6 items, the possible ways to group them into bins is a lot. But perhaps there's a way to model this problem with some mathematical approach.

Alternatively, perhaps we can consider all possible ways to group the 4a's and 2b's into different bars, and find the minimal number.

But the key is that each bar can have any number of a's and b's, as long as the sum of their lengths is <=n.

So the steps to solve this problem would be:

1. Compute the total required length: total = 4*a + 2*b. The minimal possible bars is ceil(total / n), but this is only a lower bound. However, due to the way the pieces are divided into the bars, this lower bound may not be achievable.

For example, in the first example, total is 4*1 + 2*2 = 8. n is 8. So total /n is exactly 1. So the lower bound is 1, which is achievable.

In the second example: input is 5,3,4. So a=3, b=4. So total is 4*3 + 2*4 = 12 +8=20. Each bar is 5. 20/5=4, but the sample output is 6. So in that case, the lower bound is 4, but the actual answer is higher. So the lower bound is not always achievable.

So the lower bound is the minimal possible, but sometimes we have to use more bars. For example, when the individual pieces can't fit into the bars.

So the problem is to find the minimal number of bars needed such that all 4a and 2b pieces are packed into the bars, each bar's sum of a's and b's is <=n, and each a and b is accounted for.

So how to approach this?

Possible approach:

We can model this as trying to find the minimal number of bars, considering all possible combinations of how a's and b's are packed into each bar. But with 6 items (4 a's and 2 b's), how can we compute this efficiently?

Another idea is to realize that the problem is small enough that we can precompute all possible groupings of the 4 a's and 2 b's into bars, and find the minimal number of bars.

But perhaps there's a smarter way.

Alternative approach:

For each bar, find the maximum possible number of a's and b's that can fit into it. Then, see how to distribute the required 4a and 2b into these bars.

But this is not straightforward because different bars can have different combinations.

Alternatively, let's think about all possible possibilities for a single bar. For a single bar, the possible combinations are all (x, y) where x*a + y*b <=n, and x and y are non-negative integers.

Each bar can hold x a's and y b's. The total across all bars must be 4 a's and 2 b's.

We need to find the minimal number of bars such that the sum of x's over all bars is >=4, sum of y's >=2, and for each bar x*a + y*b <=n.

Wait, no: the sum of x's must be exactly 4, sum of y's exactly 2. Because each a and b is a piece that must be accounted for. So, the problem is to select a set of (xi, yi) pairs, each satisfying xi*a + yi*b <=n, such that sum(xi) =4 and sum(yi)=2. The minimal number of such pairs (bars) is the answer.

So we need to find a collection of bars where each bar has (xi, yi) where xi is the number of a's in the bar, yi the number of b's, and the sum of xi is 4, sum yi is 2, and the total number of bars is minimized.

This seems like a dynamic programming problem, but with multiple variables. However, given that the numbers are small (4 a's and 2 b's), perhaps we can precompute all possible options.

For example, the maximum possible a's in a bar is floor(n/a). Since a can be up to n. But when a is 1, floor(n/1) =n, which can be up to 1000. Similarly for b.

But since the total required a's is 4, the maximum number of a's per bar is min(4, floor(n/a)). Similarly for b's, but per bar it's min(2, floor(n/b)), but in the context of the bar's combination.

But even this approach could be computationally intensive. However, considering the problem's constraints (n up to 1000, but the total required a and b are 4 and 2), perhaps it's manageable.

Alternative idea: iterate over all possible numbers of bars k, starting from the lower bound (ceil(total /n)), and check if it's possible to distribute the 4 a's and 2 b's into k bars.

For each possible k (starting from the lower bound), check if there exists a way to assign the a's and b's into k bars such that each bar's sum is <=n.

If we can find the minimal k for which this is possible, that's the answer.

So how to check if for a given k, it's possible to split 4 a's and 2 b's into k bars, each with sum <=n.

But how to model this? For each bar, the possible a's and b's that can be in it are constrained by:

x_i * a + y_i * b <=n

sum x_i =4

sum y_i =2

sum (x_i + y_i) >= k (since each bar must have at least one piece, but maybe not. Wait, no. A bar can have zero pieces, but since we are trying to minimize the number of bars, that's not possible. So each of the k bars must have at least one piece. So sum x_i + sum y_i = 4 + 2 =6. So the number of bars can't exceed 6. Because each bar must have at least one piece. So the minimal possible is ceil( (4a + 2b)/n ), and maximum possible is 6 (if each piece requires a separate bar).

But for the given problem, we need to find the minimal k between these two extremes.

So the steps could be:

Compute lower_bound = ceil( (4a + 2b) /n )

For k from lower_bound to 6:

   check if it's possible to split 4 a's and 2 b's into k bars, each with x_i *a + y_i *b <=n, x_i >=0, y_i >=0, sum x_i=4, sum y_i=2.

If yes, return k.

So the problem reduces to, for each k in [lower_bound ...6], check if possible. The first k where it's possible is the minimal answer.

So the question is, how to check for a given k whether the split is possible.

This seems feasible. But how to implement this check?

The problem is similar to integer partitioning with constraints on the sum per bar and the count of a's and b's.

An approach could be to model this with a recursive backtracking, but for small k and small counts (4 and 2), it's manageable.

Alternatively, for each possible k, generate all possible distributions of a's and b's across the k bars, ensuring that each bar's sum is <=n.

But for k=2 and higher, this could be computationally intensive, but given the small numbers, it's manageable.

But perhaps there's a smarter way.

Let's think of the problem as for each bar, we can assign x_i a's and y_i b's. The sum over all bars is 4 a's and 2 b's. Each bar's x_i a + y_i b <=n.

The variables are the x_i and y_i for each bar. Since k is the number of bars, and we're checking for a particular k, perhaps we can model this with dynamic programming, tracking the remaining a's, b's, and the current bar's usage.

But for each k, the approach would be different.

Alternatively, perhaps we can model this as follows:

We have to distribute 4 a's and 2 b's into k bars, each with sum <=n. For each bar, the possible combinations of x and y (number of a's and b's) can be precomputed.

So for each bar, possible (x, y) pairs are those where x*a + y*b <=n, and x >=0, y>=0.

We need to choose k such (x, y) pairs (with possible repeats), such that the sum of x's is 4 and sum of y's is 2.

So the problem is, for a given k, can we select k (x, y) pairs from the allowed (x,y) options, such that their x's sum to 4 and y's sum to 2.

But how to efficiently check this.

But given that k can be up to 6, and the possible (x,y) pairs for a bar can be precomputed, perhaps we can generate all possible combinations of k pairs and check.

But the number of possible pairs per bar is up to (floor(n/a)+1) * (floor(n/b)+1). For example, when a=1 and n=1000, floor(n/a) is 1000. So for a=1 and b=1, the possible pairs (x, y) are (1000, 0), (999, 1), ... (0, 1000). But that's 1001 * 1001 possible pairs, which is about a million. For k=6, that's (1e6)^6 possibilities, which is way too much.

But in reality, since the sum of x's is 4 and sum of y's is 2, the x can be up to 4 per bar (if there's one bar, x can be 4), but for larger k, x per bar can be 0 or 1 or 2, etc. Similarly for y.

So perhaps for each bar, the possible (x, y) pairs are limited by the remaining a's and b's. For example, when generating possible (x, y) pairs for the current bar, the x can be from 0 to min(max possible for that bar, remaining a's). Similarly for y.

But this seems like a backtracking approach, which could be feasible given the small numbers.

Let's think of the problem as follows: for a given k, we can model it as a backtracking problem where we select (x1, y1), (x2, y2), ... (xk, yk) such that:

x1 +x2 + ... +xk =4

y1 +y2 + ... +yk=2

and for each i, xi*a + yi*b <=n

We can try all possible combinations. But even for k=6, this could be manageable.

But how to implement this.

Alternatively, perhaps we can model this as a state-based problem. For each bar, track the remaining a's and b's, and the current bar count, and see if it's possible to reach (0,0) with exactly k bars.

Let's formalize this as a recursive function with memoization. The state is (remaining_a, remaining_b, bars_used). The goal is to reach (0,0) with bars_used <=k. But since k can vary, perhaps we can model it as for a given k, can we reach (0,0) with exactly k bars.

But given that the maximum possible bars is 6 (since 4+2=6, each bar can have at least one piece), the maximum k is 6.

So for each k from lower_bound to 6:

   check if possible to split into exactly k bars.

But how to model this.

Alternatively, for each possible k, generate all possible combinations of how the a's and b's are distributed across the k bars.

But for each bar, the possible (x, y) pairs must satisfy x*a + y*b <=n. So precompute all possible (x, y) pairs.

Once we have all possible (x,y) pairs for a bar, then the problem is to select k of them (with possible duplicates) such that the sum of x's is 4, sum of y's is 2.

But even this approach can be feasible for small k.

Let's outline the steps for a given k:

1. Precompute all possible (x, y) pairs where x*a + y*b <=n.

2. Then, find if there exists a multiset of k pairs from this list such that the sum of x's is 4 and sum of y's is 2.

But even with k=2, this could have a lot of possibilities.

Alternatively, for a given k, perhaps we can use dynamic programming with states tracking remaining a's and b's and the number of bars used so far.

For example, the state is (a_remaining, b_remaining, bars_used). The transitions are adding a possible (x, y) pair to the current bar, consuming x a_remaining and y b_remaining, and increasing bars_used by 1. The base case is when a_remaining=0 and b_remaining=0 and bars_used=k.

So for a given k, we can model this as a dynamic programming problem. The initial state is (4, 2, 0). For each step, for each possible (x, y) pair that can be taken (x <= a_remaining, y <= b_remaining, x*a + y*b <=n), transition to (a_remaining -x, b_remaining - y, bars_used +1). If we can reach (0,0, k), then it's possible.

But even this approach can be feasible given that a_remaining is 4, b_remaining is 2, and k can be up to 6.

The maximum possible a_remaining is 4, b_remaining is 2. So for each state, the possible values are:

a_remaining can be 0,1,2,3,4

b_remaining can be 0,1,2

bars_used can be from 0 to k.

For each k up to 6, the total possible states are 5 * 3 * (k+1) = 15*(k+1). For k=6, it's 15*7=105. So for each k, the number of states is manageable.

So for each possible k (from lower_bound to 6), we can perform this DP check.

The steps would be:

For a given k:

   Initialize a 3-dimensional DP array: dp[a_rem][b_rem][bars_used] = True/False.

   Initialize dp[4][2][0] = True.

   For each possible bar in the current count:

      For each possible a_rem and b_rem:

          For each possible (x, y) pair:

              if x <= a_rem and y <= b_rem:

                  new_a_rem = a_rem - x

                  new_b_rem = b_rem - y

                  new_bars_used = bars_used +1

                  if new_bars_used <=k:

                      if dp[new_a_rem][new_b_rem][new_bars_used] is not yet True:

                          set it to True.

   After processing all transitions, check if dp[0][0][k] is True.

If yes, then k is possible.

So the plan is:

1. Precompute all possible (x, y) pairs where x*a + y*b <=n, x >=0, y>=0.

2. For each k from lower_bound to 6:

   a. Check if k is possible using the DP approach described.

   b. If possible, return k as the answer.

So the code would first compute the lower_bound, then check each k starting from lower_bound upwards, and return the first k that is possible.

Now, let's think about how to generate the possible (x, y) pairs.

The maximum x for a bar is min(4, floor(n/a)), since each bar can't contribute more than 4 a's (since we have 4 in total). Wait, no. For example, if a=1, n=8, then a bar can have 8 a's. But since we only need 4, but the sum of x's across all bars must be exactly 4. So for a single bar, x can be up to min(4, floor(n/a)), but for multiple bars, x can be higher. Wait no. Because sum of x's across all bars must be 4. So for each bar, x can be up to the remaining a's. So during the DP process, x for a bar can't exceed the remaining a's. So when generating (x, y) pairs, we can generate all possible x and y where x*a + y*b <=n. But during the DP steps, x is limited by the remaining a's and y by the remaining b's. So when precomputing the (x, y) pairs, it's possible to include all x and y that could fit in a bar, regardless of the remaining a's and b's. Then, during the transitions, we check if x <= a_rem and y <= b_rem.

So for generating (x, y) pairs, we can generate all possible x and y where x >=0, y >=0, x*a + y*b <=n. The maximum x is floor(n/a), and maximum y is floor(n/b). For a=1 and n=1000, x can be up to 1000. But given that in the DP transitions, x can't exceed the remaining a's (which starts at 4), the actual x considered during transitions would be up to 4, even if the precomputed x is higher.

So generating all possible (x, y) pairs where x*a + y*b <=n is manageable, even for large x and y, because during the transitions, x is limited by the remaining a's (which is up to 4), and y by the remaining b's (up to 2).

So for example, when a=1 and n=1000, x can be up to 1000, but in the DP steps, since the remaining a's are 4, x can't be more than 4. So the precomputed (x, y) pairs include x up to 1000, but during transitions, only x <=4 are considered.

So generating the (x, y) pairs is possible, even for large x and y, but the code will automatically filter out x and y that exceed the remaining a's and b's.

So the steps for code:

Read n, a, b.

Compute the total required length: total = 4*a + 2*b.

Compute lower_bound = ceil(total /n). If total is zero (but a and b are at least 1, so this can't happen), but in code, we can use (total +n -1) //n to compute ceil.

Then, generate all possible (x, y) pairs where x >=0, y >=0, x*a + y*b <=n.

Then, for each k starting from lower_bound up to 6:

   check if the (x, y) pairs can be arranged into k bars, summing to 4 a's and 2 b's.

   if yes, output k and exit.

If none of the k in lower_bound to 6 is possible, output 6 (but this can't happen because 6 is the maximum possible).

Wait, but according to the problem statement, the answer can't exceed 6. Because each bar can hold at least one piece (since each piece is at least length 1, and the bar is at least length 1). But for example, if a=3 and n=3, then each a needs a separate bar, which would be 4 bars for the a's. The two b's could be each in a separate bar, but that's 2 more. Total 6. So yes, the maximum possible is 6.

So the code can proceed as follows.

Now, code steps:

Read n, a, b.

Generate all possible (x, y) pairs where x*a + y*b <=n.

For each k from lower_bound to 6:

   check if possible to split 4 a's and 2 b's into k bars using the pairs.

   if possible, return k.

So implementing the DP for each k.

Let's code this.

But in Python, for handling the DP, we can use a memoization approach or a BFS approach.

But for small k and small remaining a and b, a BFS approach is feasible.

So, for each k, the code can be:

precompute the list of possible (x, y) pairs.

Initialize a 3D array or a set that tracks the possible (a_remaining, b_remaining, bars_used).

Start with the initial state (4, 2, 0).

Then, for each state (a_rem, b_rem, bars), iterate through all possible (x, y) pairs. For each pair, if x <= a_rem and y <= b_rem, then compute new_a = a_rem -x, new_b = b_rem - y, new_bars = bars +1. If new_bars <=k, and (new_a, new_b, new_bars) is not visited yet, add it to the next states.

If after processing all steps, the state (0, 0, k) is reachable, then return k.

So the code can be structured as follows.

Now, the code steps:

First, read the inputs:

n = int(input())
a = int(input())
b = int(input())

Compute total = 4*a + 2*b.

lower_bound = (total + n -1) // n

Generate all possible (x,y) pairs:

pairs = []
max_x = n // a
for x in range(0, max_x +1):
    remaining = n - x*a
    if remaining <0:
        continue
    max_y = remaining // b
    for y in range(0, max_y +1):
        if x*a + y*b <=n:
            pairs.append( (x, y) )

Then, for each k from lower_bound to 6:

for k in range(lower_bound, 7):
    # Check if possible with k bars.
    # Initialize DP.
    from collections import deque
    visited = set()
    q = deque()
    initial_state = (4, 2, 0)
    q.append(initial_state)
    visited.add(initial_state)
    found = False
    while q:
        a_rem, b_rem, bars_used = q.popleft()
        if a_rem ==0 and b_rem ==0 and bars_used ==k:
            found = True
            break
        if bars_used >=k:
            continue
        for (x, y) in pairs:
            if x <= a_rem and y <= b_rem:
                new_a = a_rem -x
                new_b = b_rem -y
                new_bars = bars_used +1
                new_state = (new_a, new_b, new_bars)
                if new_state not in visited:
                    visited.add(new_state)
                    q.append(new_state)
    if found:
        print(k)
        exit()
print(6)

But wait, what about the case when lower_bound is greater than 6? For example, if n is 1, a=1, b=1. Then total is 4*1 +2*1=6. n=1, lower_bound is 6. So the loop would run k from 6 to 6. That's correct.

But since the code's loop runs up to 6, which is the maximum possible, the code will handle all cases.

Testing the sample inputs:

Sample 1:

n=8, a=1, b=2.

pairs: x can be from 0 to 8 (since 1*x <=8). For each x, y can be up to (8 -x)/2.

For x=4, y=2: 4*1 +2*2=4+4=8. So (4,2) is a pair.

So when k=1, the code checks if (4,2,1) is possible.

The initial state is (4,2,0). Process:

Take (4,2) pair. new_a =4-4=0, new_b=2-2=0, new_bars=1. So the state becomes (0,0,1). Since k=1, the code checks if (0,0,1) is found. Yes. So returns 1.

Sample 2:

n=5, a=3, b=4.

Each a is 3, each b is4.

Total is 4*3 +2*4= 12+8=20. lower_bound =20/5=4 (ceil(20/5) is 4).

Check k=4,5,6.

But for each bar, the sum x*3 + y*4 <=5.

Possible pairs:

x can be 0,1 (3*1=3 <=5).

For x=0:

y can be 0,1 (since 4*1=4 <=5). So (0,0), (0,1).

For x=1:

3 + y*4 <=5 → y*4 <=2 → y=0. So (1,0).

So the pairs are (0,0), (0,1), (1,0).

Wait, but (0,0) would contribute nothing. But in the code, we need to select k bars (exactly k). So when k=4, but for each bar, the sum of x's is 4, y's 2.

But possible (x, y) pairs are (0,1) (sum y=1) and (1,0) (sum x=1).

But for each bar, if we take (1,0), which contributes x=1. So for 4 bars, each with (1,0), sum x=4, but sum y=0. Which is not enough. Or mix with (0,1) for some bars.

For example, 4 bars: three (1,0) and two (0,1). But that's 5 bars, which exceeds k=4.

Wait, but in this case, each bar must contribute something. So for k=4, each bar must have at least one piece. But (0,0) is not allowed, but the code includes it. Wait, no. Because the (x, y) pairs are allowed to be (0,0), but in that case, the bar is being used but not contributing anything. So the code would generate such possibilities, but during the transitions, the code would only add (0,0) if x and y are allowed. But the code will only process (x,y) pairs where x and y are <= the remaining a and b. So, for example, when a_rem is 4 and b_rem is 2, if we take (0,0), then new_a_rem=4, new_b_rem=2, new_bars=1. Then, in the next steps, this would not help because the bars_used increases but nothing is subtracted. So the code would loop infinitely, but since the visited set is maintained, it would stop.

But in reality, the (0,0) pair is useless and can be skipped. Because it's better to not use such pairs. So in the code, perhaps we should generate pairs where x and y are not both zero.

So modifying the code to generate pairs where x and y are not both zero.

Because a bar with x=0 and y=0 is a waste of a bar. Since we're trying to minimize the number of bars, using a bar that contributes nothing is never optimal. So in the generated pairs, we can exclude (0,0).

So in the code:

when generating pairs:

for x in 0..max_x:

   for y in 0..max_y:

       if x*a + y*b <=n and (x>0 or y>0):

           add to pairs.

This will prevent (0,0) from being considered.

This is an optimization, but it's important to avoid generating (0,0) pairs which are not useful.

So modifying the code:

if x*a + y*b <=n and (x>0 or y>0):

This would exclude pairs where x=0 and y=0.

This is an important optimization because including (0,0) would generate many states that don't contribute anything and could lead to infinite loops (but with the visited set, it's prevented).

So in the sample 2 case, the possible pairs are (0,1), (1,0).

Each (0,1) contributes y=1, but requires b=4. For each such pair, sum of y's must be 2.

So for k=4, we need to select 4 bars, each with (0,1) or (1,0). Let's see:

sum x's is 4, sum y's is 2.

Each (1,0) contributes x=1, y=0.

Each (0,1) contributes x=0, y=1.

So sum x's: number of (1,0) pairs.

Sum y's: number of (0,1) pairs.

We need:

number of (1,0) pairs =4.

number of (0,1) pairs =2.

Total bars =4+2=6. But k=4. So it's impossible. Hence the answer is 6.

Which matches the sample.

But the code, for k=4, would check if possible. Let's see:

The code's pairs are (0,1), (1,0).

Each bar can be either of these.

So for k=4, the code would check if it's possible to sum 4 x's (from (1,0)) and 2 y's (from (0,1)) in 4 bars.

But each bar can contribute either x=1 and y=0, or x=0 and y=1.

So sum x's is the number of bars with (1,0), sum y's is the number of bars with (0,1).

So 4 x's → 4 bars of (1,0). sum y's is 0. Not enough.

Or, 3 bars of (1,0) (x=3), 1 bar of (0,1) (y=1). sum x=3, sum y=1. Not enough.

So impossible. Hence, for k=4, it's not possible. Then check k=5.

In k=5 bars:

Need to have sum x=4 and sum y=2. So the sum of bars is 5.

The number of (1,0) bars is x_count, and (0,1) bars is y_count.

x_count + y_count =5.

x_count =4.

y_count=1.

But y_count must be 2. So not possible.

Hence, k=5 is impossible.

k=6:

Each bar is either (1,0) or (0,1).

x_count + y_count=6.

x_count=4, y_count=2.

Yes. So 6 bars, each (1,0) four times and (0,1) twice. So each bar contributes one piece. Hence, the answer is 6.

So the code correctly finds that for k=6, it's possible.

Thus, the code should output 6.

Another sample:

Input 3:

6

4

2

So a=4, b=2.

Total is 4*4 + 2*2 =16+4=20. n=6.

lower_bound=20 /6 → 3.333 → ceil is 4.

Check if possible with 4 bars.

Possible pairs:

Each bar can have x a's and y b's such that 4x +2y <=6.

Possible pairs:

x can be 0,1 (since 4*1=4 <=6).

For x=0:

2y <=6 → y can be 0,1,2,3. But since y can't be more than 2 (since we need sum y=2), but pairs are generated for any y. But during transitions, it's checked.

But since (0,3) is a possible pair (4*0 +2*3=6=6), but sum y can't be 3.

But during transitions, the code would only allow y <= remaining b's.

So possible pairs:

For x=0:

y can be 0,1,2,3.

But since (0,3) is allowed, but sum y needed is 2. So during transitions, when b_rem is 2, y can't be 3.

So the pairs for x=0:

y can be 0,1,2,3.

But (0,3) would require 3 in y, but sum needed is 2. So during transitions, it's not possible.

But for x=0, the possible pairs are (0,1), (0,2), (0,3) (but (0,0) is excluded as before).

But for x=1: 4*1=4. 4 + 2y <=6 → 2y <=2 → y can be 0 or 1.

So pairs for x=1: (1,0) (4+0=4 <=6), (1,1) (4+2=6 <=6).

So all possible pairs (excluding x=0 and y=0):

(0,1), (0,2), (0,3), (1,0), (1,1).

So the possible pairs.

Now, for k=4:

We need to distribute 4 a's and 2 b's into 4 bars.

Each bar's sum 4x + 2y <=6.

Possible combinations:

For example, two bars of (1,1) → contributes x=2, y=2. Then two more bars of (1,0) → x=2. Sum x=4, y=2. So total bars=4.

So possible.

So the code should find this.

The code will check k=4:

possible.

So the answer is 4.

Thus, the code works.

Now, implement this in Python.

The code should generate all possible pairs, excluding (0,0), then for each k from lower_bound to 6, perform BFS to check if possible.

Now, the code:

Read the inputs.

Generate pairs.

Loop over k from lower_bound to 6.

Check for each k.

Now, the code:

But for the pairs, we need to generate x and y such that x*a + y*b <=n and (x>0 or y>0).

So:

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = int(input_stream.readline().rstrip("\n"))
    b = int(input_stream.readline().rstrip("\n"))

    total = 4 * a + 2 * b
    if total ==0:
        print(0, file=output_stream)
        return

    lower_bound = (total + n -1) // n

    pairs = []
    max_x = n // a
    for x in range(0, max_x +1):
        remaining = n - x * a
        if remaining <0:
            continue
        max_y = remaining // b
        for y in range(0, max_y +1):
            if x *a + y * b <=n and (x >0 or y>0):
                pairs.append( (x, y) )

    for k in range(lower_bound, 7):
        visited = set()
        from collections import deque
        q = deque()
        initial = (4, 2, 0)
        q.append(initial)
        visited.add(initial)
        found = False
        while q:
            a_rem, b_rem, bars = q.popleft()
            if a_rem ==0 and b_rem ==0 and bars ==k:
                found = True
                break
            if bars >=k:
                continue
            for (x, y) in pairs:
                if x <= a_rem and y <= b_rem:
                    new_a = a_rem -x
                    new_b = b_rem -y
                    new_bars = bars +1
                    new_state = (new_a, new_b, new_bars)
                    if new_state not in visited:
                        visited.add(new_state)
                        q.append(new_state)
        if found:
            print(k, file=output_stream)
            return

    print(6, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20
5
6
""",
            "output": \
"""\
2
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

Another sample:

Sample 4:

Input: 20

5

6

a=5, b=6.

Total is 4*5 + 2*6=20+12=32.

n=20.

lower_bound = 32 /20=1.6 → ceil is 2.

Check k=2.

Possible pairs:

x*a + y*b <=20.

a=5, b=6.

Possible x: 0,1,2,3,4 (since 5*4=20). For each x, y can vary.

For x=4: 5*4=20. y can be 0. So (4,0).

x=3: 15. remaining 5. y can be 0 (5/6=0). So (3,0).

x=2: 10. remaining 10. y can be 1 (6*1=6). 10+6=16 <=20. Or y=1. So (2,1).

x=1: 5 → remaining 15 → y can be 15//6=2. So (1,2) (5+12=17 <=20).

x=0: y can be up to 20//6=3. (0,3).

So possible pairs include:

(4,0) → sum 20.

(3,0) → 15.

(2,1) → 5*2 +6*1=16.

(1,2) → 5+12=17.

(0,3) → 18.

Other possibilities:

For x=2, y=1 is allowed.

Now, for k=2:

Need to split 4 a's and 2 b's into two bars.

Each bar must have sum <=20.

Looking for a way to have two bars that cover 4a and 2b.

For example:

Bar 1: 3a + 1b → 3*5 +6=21 → exceeds 20. Not allowed.

Another option: bar1: 2a and 1b → 10+6=16. Bar2: 2a and 1b → 10+6=16. Sum a's is 4, sum b's is 2. So two bars. So possible.

Thus, the code will find this.

But in the pairs, (2,1) is allowed.

So for each bar:

Bar1: (2,1) → a=2, b=1. Sum 16 <=20.

Bar2: (2,1) → a=2, b=1. Sum 16 <=20.

Total a's 4, b's 2. So possible with k=2.

Thus, code returns 2.

Which matches the sample.

Thus, the code works.

Finally, the code should handle all cases correctly.
</think>

```python
n = int(input())
a = int(input())
b = int(input())

total = 4 * a + 2 * b
if total == 0:
    print(0)
    exit()

lower_bound = (total + n - 1) // n

pairs = []
max_x = n // a
for x in range(0, max_x + 1):
    remaining = n - x * a
    if remaining < 0:
        continue
    max_y = remaining // b
    for y in range(0, max_y + 1):
        if x * a + y * b <= n and (x > 0 or y > 0):
            pairs.append((x, y))

for k in range(lower_bound, 7):
    visited = set()
    from collections import deque
    q = deque()
    initial = (4, 2, 0)
    q.append(initial)
    visited.add(initial)
    found = False
    while q:
        a_rem, b_rem, bars = q.popleft()
        if a_rem == 0 and b_rem == 0 and bars == k:
            found = True
            break
        if bars >= k:
            continue
        for (x, y) in pairs:
            if x <= a_rem and y <= b_rem:
                new_a = a_rem - x
                new_b = b_rem - y
                new_bars = bars + 1
                new_state = (new_a, new_b, new_bars)
                if new_state not in visited:
                    visited.add(new_state)
                    q.append(new_state)
    if found:
        print(k)
        exit()

print(6)
```
