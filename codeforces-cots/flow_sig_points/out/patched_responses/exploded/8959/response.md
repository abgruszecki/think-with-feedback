<think>
Okay, let's see. The problem is about calculating the minimum and maximum number of rounds Alice can win in a Rock-Paper-Scissors game with given counts of each choice for Alice and Bob. 

First, for the maximum number of wins. That's probably straightforward. Because Alice wants to maximize her wins, each of her choices should beat Bob's corresponding choices as much as possible. So the maximum possible wins would be the sum of the minimum of Alice's rock times Bob's scissors (since rock beats scissors), Alice's scissors times Bob's paper, and Alice's paper times Bob's rock. That's the classic approach for maximum possible wins in these types of problems. So the maximum is min(a1, b2) + min(a2, b3) + min(a3, b1).

Now the tricky part is the minimum number of wins. Because here, Alice wants to lose as much as possible, but she's constrained by the number of times she and Bob use each move. So the minimum wins would be determined by the scenarios where Alice's moves are arranged in a way that they don't beat Bob's moves as much as possible, but also considering that the total number of moves per type must match their counts.

But how do we model that? Well, the minimum wins can be found by considering the maximum number of losses and draws, but perhaps there's a smarter way. Wait, maybe we can model this as the total possible rounds minus the maximum number of non-wins (losses + draws). Because the minimum wins would be total rounds minus the maximum possible non-wins. 

Alternatively, perhaps another approach: to minimize Alice's wins, we need to maximize the number of times Alice's move either loses to Bob's or draws. So, for each of Alice's moves, we want to pair them with Bob's moves that either they lose against or draw. 

But how to calculate that? Let's think. For example, Alice's rocks (a1) can lose to Bob's papers (b3) or draw with Bob's rocks (b1). So for a1, the maximum possible non-wins would be min(a1, b1 + b3). Similarly for scissors (a2) and paper (a3). Wait, but that might not account for overlapping uses. Because Bob's moves are fixed. So maybe this approach is not correct.

Alternatively, the minimum number of wins is when Bob's moves are arranged to minimize Alice's wins. So for each possible pair where Alice can win, we need to minimize that. So the problem is to minimize the sum of (a_rock * b_scissors) + (a_scissors * b_paper) + (a_paper * b_rock). But how?

Wait, the minimum wins would occur when Bob's choices are arranged such that as many as possible of Alice's choices are countered. But given that Bob's counts are fixed, how can we model this?

Alternatively, perhaps the minimal number of Alice's wins is equal to the total possible wins minus the maximum possible wins that Bob can achieve. Wait, no. Because Bob's wins are determined by his moves beating Alice's. So Bob's maximum wins would be when Bob's rock beats Alice's scissors, etc. So maybe the minimum Alice's wins is equal to (a1 + a2 + a3) - (maximum possible Bob's wins + maximum possible draws). But that's not quite right. Because the total rounds are n. So the sum of Alice's wins, Bob's wins, and draws is n. So Alice's wins + Bob's wins + draws = n. So to minimize Alice's wins, we need to maximize Bob's wins plus the draws. But draws occur when Alice and Bob choose the same move. So perhaps the minimal Alice's wins can be found by considering the maximum possible of (Bob's wins + draws). Then, Alice's wins would be n - (max_bob_wins + max_draws). Wait, but how do we compute that?

Alternatively, here's an approach:

The minimal number of Alice's wins is equal to the total possible Alice's wins (which is the sum of a1*b2 + a2*b3 + a3*b1) minus the maximum possible of Bob's wins. Wait, no. Because the maximum Bob's wins are when Bob's moves are arranged to maximize his own wins. But since the counts of each move are fixed, maybe the maximum Bob's wins is min(b1, a2) + min(b2, a3) + min(b3, a1). So then Alice's minimal wins would be the sum of her possible wins (the original maximum) minus the maximum possible Bob's wins. But I'm not sure. Let me think again.

Wait, the minimal Alice's wins can't be directly the maximum of Bob's wins. Because when Alice's wins are minimized, that's when Bob's wins are maximized. Because in that scenario, as many of Alice's possible wins are turned into Bob's wins. But how?

Alternatively, the minimal number of Alice's wins is the maximum between zero and (a1 + a2 + a3) - (b1 + b2 + b3 + maximum draws + maximum Bob's wins). Wait, this seems unclear.

Another approach: Let's model the problem as a flow or a mathematical equation. We need to distribute Alice's and Bob's moves such that the number of Alice's wins is minimized.

Each Alice's rock (a1) can potentially be matched against Bob's rock (draw), scissors (Alice wins), or paper (Bob wins). To minimize Alice's wins, we want as many of her rocks to be matched against Bob's paper (so Bob wins) or his rocks (draw) as possible. Similarly for other moves.

So for each move type of Alice, the maximum possible non-wins (i.e., Bob's wins or draws) would be the sum of Bob's moves that can lead to that. For example:

For Alice's rock (a1), the possible non-wins are Bob's rock (b1) and Bob's paper (b3). So the maximum possible non-wins for a1 is a1's total (a1) must be matched with some combination of Bob's b1 and b3. But since Bob's total is fixed, we can't take more than b1 + b3. So the non-wins from a1 would be min(a1, b1 + b3). Similarly for a2: non-wins are Bob's scissors (b2) and Bob's rock (b1). So min(a2, b2 + b1). And a3: non-wins are Bob's paper (b3) and Bob's scissors (b2). min(a3, b3 + b2).

Wait, but this approach would sum all these min values and subtract them from the total n to get the minimal wins. Because sum of non-wins (draws + Bob's wins) is the sum of all possible non-wins for each of Alice's moves. Then, the minimal Alice's wins is n minus the sum of these non-wins. But wait, no. Because the sum of non-wins can't exceed n. But this approach might be overcounting. Because Bob's moves are limited. For example, if a1 is matched to b1 and b3, but the sum of a1's non-wins plus a2's non-wins might require Bob's b1 to be used in both, which is impossible.

So this approach is incorrect because it doesn't account for overlapping resources (Bob's moves can't be used in multiple places). So, we need a way to model the problem where the allocation of Bob's moves to Alice's moves is done in a way that maximizes the sum of non-wins (i.e., Bob's wins and draws), thereby minimizing Alice's wins.

This seems like a problem of finding the maximum possible non-wins (draws plus Bob's wins), given the constraints of Alice's and Bob's move counts.

The key here is to model the problem as a system where we want to maximize the number of non-wins. So for each Alice's move type, we can pair it with Bob's move types in such a way that the outcome is either a draw or a Bob's win.

Let me break down the possible non-wins for each Alice move:

- Alice plays rock (a1): possible non-wins are when Bob plays rock (draw) or paper (Bob wins). The total possible here is up to a1, but constrained by Bob's available rocks and papers (b1 + b3).
- Alice plays scissors (a2): non-wins when Bob plays scissors (draw) or rock (Bob wins). So sum of Bob's b2 + b1.
- Alice plays paper (a3): non-wins when Bob plays paper (draw) or scissors (Bob wins). So sum of Bob's b3 + b2.

But again, we can't just sum the minima of a_i and (sum of Bob's possible moves for non-wins) because Bob's moves are a limited resource. For example, Bob's rock (b1) is used in both a1's non-wins (when Alice plays rock and Bob plays rock) and a2's non-wins (when Alice plays scissors and Bob plays rock). So if a1 uses some of b1, that leaves less for a2.

So this becomes a problem of distributing Bob's moves across Alice's moves in a way that maximizes the total non-wins. How do we model this?

This is similar to a bipartite matching problem, but perhaps there's a mathematical approach. Let's consider that the maximum possible non-wins is the maximum number of pairs (i,j) where Alice's move i and Bob's move j result in a non-win for Alice. The constraints are that for each move type of Alice (a1, a2, a3), the sum of Bob's moves paired with them must not exceed a_i, and for each move type of Bob (b1, b2, b3), the sum of Alice's moves paired with them must not exceed b_j.

So the problem reduces to finding the maximum possible sum of x, y, z, u, v, w where:

x: a1 paired with b1 (draw)
y: a1 paired with b3 (Bob's win)
z: a2 paired with b1 (Bob's win)
u: a2 paired with b2 (draw)
v: a3 paired with b2 (Bob's win)
w: a3 paired with b3 (draw)

Subject to:

x + y ≤ a1
z + u ≤ a2
v + w ≤ a3

x + z ≤ b1 (because x is a1's rocks paired with b1, and z is a2's scissors paired with b1)
y + v ≤ b3 (y is a1's rocks paired with b3, v is a3's papers paired with b3)
u + w ≤ b2 (u is a2's scissors paired with b2, w is a3's papers paired with b2)

And we want to maximize x + y + z + u + v + w.

This is a linear programming problem. However, given the constraints, perhaps there's a smarter way to compute this.

But with n up to 1e9, we need an O(1) solution, so any approach that requires iterating through possibilities is not feasible.

Another way to approach this: the maximum possible non-wins is equal to the sum of the minimum of Alice's a_i and the sum of Bob's possible moves that can pair with a_i for non-wins, but adjusted so that the sum of Bob's moves across all pairings does not exceed their available counts.

But how?

Alternatively, let's model the problem as follows:

The maximum non-wins can be calculated by considering that:

Each of Alice's a1 can pair with Bob's b1 and b3. The maximum possible non-wins from a1 is a1, but Bob's available b1 and b3 must be allocated. Similarly, a2 can pair with b1 and b2. a3 can pair with b2 and b3.

The problem is to find the maximum sum of these pairings, given the constraints on Bob's moves.

So, the variables are:

- x1: a1 paired with b1 (draw)
- x3: a1 paired with b3 (Bob wins)
- y1: a2 paired with b1 (Bob wins)
- y2: a2 paired with b2 (draw)
- z2: a3 paired with b2 (Bob wins)
- z3: a3 paired with b3 (draw)

Constraints:

x1 + x3 ≤ a1
y1 + y2 ≤ a2
z2 + z3 ≤ a3

x1 + y1 ≤ b1
y2 + z2 ≤ b2
x3 + z3 ≤ b3

We need to maximize x1 + x3 + y1 + y2 + z2 + z3.

But solving this system for maximum seems complicated. However, perhaps there's a pattern here. Let's think of the total possible non-wins as the sum of all possible pairings that are non-wins. The maximum possible is the sum of the possible pairs, but limited by the availability of each move.

Alternatively, the maximum non-wins is equal to (a1 + a2 + a3) - (the minimum number of Alice's wins possible). Wait, that's the opposite of what we need. We need to compute the minimum Alice's wins. So maximum non-wins = n - min_wins. Therefore, min_wins = n - maximum_non_wins.

So the problem now is to compute the maximum possible non-wins (draws + Bob's wins) given the constraints. Then subtract this from n to get the minimal Alice's wins.

But how do we compute this maximum non-wins?

Hmm. Let's think of this as an optimization problem. We need to maximize the sum of x1 + x3 + y1 + y2 + z2 + z3, given the constraints.

This can be viewed as follows:

The variables are:

x1 (a1 paired with b1) contributes to a1's count and b1's count.

x3 (a1 paired with b3) contributes to a1's and b3's.

Similarly for others.

The variables are the allocations of Bob's moves to Alice's moves in such a way that each allocation is a non-win for Alice.

We can model this as:

max (x1 + x3 + y1 + y2 + z2 + z3)

subject to:

x1 <= a1, x3 <= a1 - x1

y1 <= a2, y2 <= a2 - y1

z2 <= a3, z3 <= a3 - z2

x1 <= b1, y1 <= b1 - x1

y2 <= b2, z2 <= b2 - y2

x3 <= b3, z3 <= b3 - x3

But this seems really complicated. Let's think of it in terms of the variables:

For Bob's moves:

Total available:

b1 can be used in x1 (a1's rock) and y1 (a2's scissors). So x1 + y1 <= b1.

b2 can be used in y2 (a2's scissors) and z2 (a3's paper). So y2 + z2 <= b2.

b3 can be used in x3 (a1's rock) and z3 (a3's paper). So x3 + z3 <= b3.

So, the sum x1 + y1 + y2 + z2 + x3 + z3 is the total non-wins. But how to maximize this sum given the constraints on a1, a2, a3 and the Bob's move allocations.

This seems like a problem that can be modeled as a maximum flow or a system of equations. However, given the problem constraints (n up to 1e9), the solution must be O(1), not O(n) or similar.

Alternative approach: perhaps the maximum possible non-wins can be found by considering the minimum of certain sums. Let's see:

The sum of all possible non-wins is limited by:

For Alice's moves:

- a1 can contribute up to a1 non-wins (rock vs rock or paper)
- a2 can contribute up to a2 non-wins (scissors vs scissors or rock)
- a3 can contribute up to a3 non-wins (paper vs paper or scissors)

But Bob's moves are limited:

- The sum of x1 + y1 (rock from Bob's perspective) is <= b1
- The sum of y2 + z2 (scissors from Bob's perspective) is <= b2
- The sum of x3 + z3 (paper from Bob's perspective) is <= b3

So the total non-wins can't exceed a1 + a2 + a3 (which is n), and also can't exceed the sum of Bob's possible non-win pairs (b1 + b2 + b3) (but that's also n, so that's not helpful). Wait, but Bob's non-win pairs are the moves that can cause non-wins. But Bob's moves are exactly his choices, so the sum of all Bob's moves is n.

Alternatively, the maximum possible non-wins is the sum of all possible pairings where Alice's move and Bob's move result in a non-win, subject to the constraints of their counts.

But how?

Another idea: the maximum non-wins is equal to the sum of:

min(a1, b1 + b3) + min(a2, b1 + b2) + min(a3, b2 + b3) 

But then subtract the overlaps where Bob's moves are used in multiple a_i's.

Wait, but this might overcount. For example, suppose a1 is 5, and b1 + b3 is 10. Then a1 can contribute 5 non-wins. But when a2's min is taken, it could require some of Bob's b1, which were already used in a1's non-wins. 

So this approach would not account for overlapping resources.

Thus, this approach is incorrect.

Alternative approach inspired by the maximum problem:

In the maximum case, we pair each of Alice's moves with the maximum possible Bob's moves that lead to a win. For the minimum case, perhaps we need to pair each of Alice's moves with the maximum possible Bob's moves that lead to a non-win (either a loss or a draw), but considering that Bob's moves are a limited resource.

But how?

Another way to think about this is that the minimum Alice's wins is equal to the maximum possible Bob's wins plus the draws. Wait, no. Because draws are when both have the same move, which is a non-win for Alice but not a win for Bob. So the minimal Alice's wins is when Bob's wins are as high as possible, and the draws are as high as possible. But how?

Alternatively, the minimal Alice's wins can be calculated as (total possible wins) minus (the maximum possible wins Bob can have). But that's not correct. For example, in the first test case, Alice can have maximum 1 win. If Bob's maximum wins are 1, then Alice's minimum would be 0. Which matches the example.

Wait, let's look at the first example:

n=2

Alice's moves: 0,1,1 (rock, scissors, paper)

Bob's moves:1,1,0 (rock, scissors, paper)

Maximum Alice's wins is 1 (e.g., she plays paper and scissors. Bob plays rock and scissors. Alice's paper beats rock, scissors loses to scissors (draw). So one win.)

Minimum Alice's wins is 0. How? Bob's maximum wins would be 1 (e.g., Bob's rock and scissors. Alice's scissors and paper. Bob's rock beats scissors, and scissors beats paper. So Bob wins two times. Wait, but that's 2 Bob's wins, leading to Alice's wins 0. But according to the example, the output is 0. So in that case, the minimum Alice's wins is 0, which is when Bob's wins are 2. But according to this idea, the minimal Alice's wins would be (max possible Alice wins) - (max Bob's wins). Wait, no.

This suggests that the maximum Bob's wins plus the draws is equal to the total non-wins. So to find the minimal Alice's wins, we need to maximize Bob's wins and draws.

But how?

Alternatively, let's model Bob's wins. Bob's wins occur when:

Bob's rock beats Alice's scissors (a2)
Bob's scissors beats Alice's paper (a3)
Bob's paper beats Alice's rock (a1)

So the maximum possible Bob's wins is min(b1, a2) + min(b2, a3) + min(b3, a1).

So in the first example:

Bob's possible wins are min(1,1) (b1 and a2) =1, min(1,1) (b2 and a3) =1, min(0,0) =0. Sum is 2. So Bob can have 2 wins, which leaves Alice's wins as 0. Which matches the example.

So in this case, the minimal Alice's wins is (original maximum) - Bob's maximum wins. Wait, but in the first example, the maximum Alice's wins is 1, Bob's maximum wins is 2, and the sum is 3, which is larger than n=2. That can't be.

Wait, there's a mistake here. Because the maximum Alice's wins and maximum Bob's wins can't both be achieved. For example, in a scenario where Alice's rock beats Bob's scissors (max Alice's), Bob's paper beats Alice's rock (max Bob's). These two can't happen simultaneously. So the sum of Alice's maximum wins and Bob's maximum wins can't exceed n. But in the first example, 1+2=3 >2. So this approach is incorrect.

Therefore, the minimal Alice's wins is not simply (original maximum) - (Bob's maximum wins). Because that would lead to possible negative values.

So this approach is not valid.

Another idea: The minimal Alice's wins is the maximum between zero and (sum of possible Alice's wins minus Bob's possible wins). But again, this is not correct.

Alternatively, the minimal Alice's wins is the total possible Alice's wins (max case) minus the sum of Bob's maximum possible wins. But again, this may lead to negative values.

Hmm. Let's think differently. The minimal number of Alice's wins is the maximum between zero and (the sum of her possible wins minus the sum of Bob's possible wins and possible draws). Wait, perhaps not.

Wait, the problem is that we need to arrange Alice's and Bob's moves such that the number of Alice's wins is as small as possible. So the question is: what's the worst possible arrangement for Alice, given their move counts.

So to compute this, perhaps the minimal Alice's wins can be calculated as:

max(0, (a1 + a2 + a3) - (b1 + b2 + b3) + (max Bob's wins + max draws)) ?

No, that's not clear.

Alternatively, here's an approach that might work:

The minimal number of Alice's wins is equal to the maximum of (a1 - (b1 + b3) + a2 - (b1 + b2) + a3 - (b2 + b3) + (b1 + b2 + b3)) ), but this seems incorrect.

Alternatively, perhaps the minimal Alice's wins can be computed as follows:

Each of Alice's moves can at best be matched against a certain number of Bob's moves that result in a loss or draw. But since Bob's moves are fixed, we need to model the overlap.

Wait, the minimal Alice's wins is the sum of the maximum possible of (Alice's move type i can be matched with Bob's moves that do not result in a win for Alice). So for each i:

For a1 (rock), the non-winning Bob's moves are b1 (rock) and b3 (paper). So the maximum possible non-wins for a1 is min(a1, b1 + b3).

Similarly for a2 (scissors), non-winning Bob's moves are b1 (rock) and b2 (scissors). So min(a2, b1 + b2).

For a3 (paper), non-winning Bob's moves are b2 (scissors) and b3 (paper). So min(a3, b2 + b3).

The sum of these three minima would be the maximum possible non-wins, and the minimal Alice's wins is n minus this sum.

But wait, the sum of these minima may exceed the total possible Bob's moves. For example:

Suppose Alice has a1=5, a2=5, a3=5. Bob has b1=5, b2=5, b3=5.

For each a_i, the min is 5+5=10. So sum is 5+5+5 =15. But Bob's total moves are 15. So sum is 15, which is allowed. So non-wins would be 15, leading to Alice's wins of 0, which matches the second example.

Another example:

Third example input:

3

0 0 3 (Alice's paper)

3 0 0 (Bob's rock)

So for a3=3. Bob's b2 is 0 and b3 is 0. So min(a3, b2 + b3) = min(3,0+0)=0. So non-wins sum is 0+0+0=0. Then minimal wins is 3 -0=3, which is correct.

Another example:

First example:

n=2

Alice's moves: a1=0, a2=1, a3=1.

Bob's: b1=1, b2=1, b3=0.

For a1=0: min(0, 1+0) =0.

a2=1: min(1, 1+1)=1. But Bob's b1 +b2 is 1+1=2. So min(1,2) is1.

a3=1: min(1, 1+0)=1. Sum is 0+1+1=2. So non-wins sum is 2. Alice's wins is 2-2=0, which is correct.

So in this case, this approach seems to work. So perhaps the minimal Alice's wins is max(0, (a1 +a2 +a3) - (sum of min(a_i, (possible Bob's non-wins for a_i)))).

Wait, but n is a1+a2+a3. So the minimal wins would be n minus the sum of min(a1, b1 +b3) + min(a2, b1 +b2) + min(a3, b2 +b3). But wait, in the first example, the sum of min values is 0+1+1=2. n is 2. So 2-2=0. Which is correct.

Another example: fourth input.

Sample input 4:

686

479 178 29

11 145 530

Sample output: 22 334.

Let's see the minimal wins according to the formula:

sum for a1: min(479, 11 (b1) +530 (b3)) = min(479,541) → 479.

sum for a2: min(178, 11 (b1) +145 (b2)) → 11+145=156 → min(178,156) →156.

sum for a3: min(29, 145+530=675 → 29. Sum total is 479+156+29=664. n=686. 686-664=22, which matches the sample output. So this formula works.

Similarly, for sample input 5:

319

10 53 256 (a1, a2, a3)

182 103 34 (b1, b2, b3)

sum for a1: min(10, b1 +b3=182+34=216 → 10.

sum for a2: min(53, b1 +b2=182+103=285 →53.

sum for a3: min(256, b2 +b3=103+34=137 →137. Sum total is 10+53+137=200. n=319 →319-200=119, which matches the sample output.

So this approach works.

So the formula for the minimal Alice's wins is:

min_wins = max(0, (a1 + a2 + a3) - (min(a1, b1 + b3) + min(a2, b1 + b2) + min(a3, b2 + b3))))

Since a1+a2+a3 =n, this simplifies to min_wins = max(0, n - (s)), where s is the sum of the three minima.

Therefore, the steps are:

1. Compute the maximum possible wins for Alice: max_win = min(a1, b2) + min(a2, b3) + min(a3, b1).

2. Compute the sum s = min(a1, b1 + b3) + min(a2, b1 + b2) + min(a3, b2 + b3). Then min_win = max(0, n - s).

So this is the solution.

Now, to implement this in Python:

The code will read n, a1, a2, a3, then b1, b2, b3.

Compute max_win as min(a1, b2) + min(a2, b3) + min(a3, b1).

For min_win:

s = min(a1, b1 + b3) + min(a2, b1 + b2) + min(a3, b2 + b3)

min_win = max(0, n - s)

Then output min_win and max_win.

That's straightforward.

So the code will be:

n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

max_win = min(a1, b2) + min(a2, b3) + min(a3, b1)

s = min(a1, b1 + b3) + min(a2, b1 + b2) + min(a3, b2 + b3)
min_win = max(0, n - s)

print(min_win, max_win)

Testing this against the examples:

Sample input 3:

3

0 0 3 (a3=3)

3 0 0 (b1=3)

max_win = min(0,0) + min(0,0) + min(3,3) →0+0+3=3.

s = min(0, 3+0) →0, min(0,3+0)=0, min(3,0+0=0) →0. s=0. min_win=3-0=3.

Which matches the sample.

Sample input 2:

15

5 5 5

5 5 5

max_win: min(5,5) + min(5,5) + min(5,5) →5+5+5=15.

s = min(5,5+5) →5, min(5,5+5=10) →5, min(5,5+5=10) →5. sum 5+5+5=15. min_win=15-15=0.

Which matches sample.

Sample input 4:

686 →n=686.

a:479,178,29.

b:11,145,530.

max_win= min(479,145) →145. min(178,530) →178. min(29,11) →11. sum 145+178+11=334. Which matches sample's max.

s: min(479, 11+530=541) →479. min(178,11+145=156) →156. min(29,145+530=675) →29. sum 479+156+29=664. min_win=686-664=22. Which matches sample.

Thus, the code works.
</think>

```python
n = int(input())
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)
s = min(a1, b1 + b3) + min(a2, b1 + b2) + min(a3, b2 + b3)
min_wins = max(0, n - s)

print(min_wins, max_wins)
```