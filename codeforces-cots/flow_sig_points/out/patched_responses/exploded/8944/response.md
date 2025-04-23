<think>
Okay, let's see. The problem is to find the minimum number of onager shots needed to break at least two sections of the wall. Each shot deals 2 damage to the target and 1 to adjacent sections. Hmm.

So, Monocarp can choose any sections to shoot any number of times. The goal is to have at least two sections broken. The key is to find the optimal way to do this with the least shots.

First, I need to model how the shots affect the sections. For each possible pair of sections that could break, calculate the minimum shots required and then choose the minimum among all pairs. But since n can be up to 2e5, checking all possible pairs is O(n^2) which is way too slow. So that approach isn't feasible.

Wait, but perhaps there's a way to find the best pairs efficiently. Let's think about the possible scenarios where two sections break. The two sections could be adjacent, or not. Also, maybe overlapping, like shooting a section between them.

Alternatively, maybe the optimal solution is either two adjacent sections or two sections with one in between (like i and i+2). Or maybe even two sections that are further apart, but that's probably not optimal because the overlapping effect would be less.

So perhaps we need to consider all possible pairs of sections that are adjacent or have one section between them, and compute the minimal shots for those. Then pick the minimum among those possibilities. Because if the two sections are further apart, the required shots would be higher.

Wait, let's think. For two sections that are k apart (k ≥ 3), the shots needed would be the sum of their individual a_i divided by 2 (since each shot to them affects only themselves and their immediate neighbors, which are not overlapping). But if they are close, like adjacent or with one in between, then shooting in the middle can affect both. For example, shooting between two adjacent sections can damage both.

So the minimal shots might come from pairs that are adjacent or separated by one. Let's consider all possible pairs of sections where their positions are either adjacent (i and i+1) or next-nearest (i and i+2). For each of these pairs, compute the minimal shots required to break both, then take the minimum over all these pairs. Then compare that with the minimal sum of (ceil(a_i / 1) / 1) for any two sections (like if you break them individually by shooting their own positions), but wait, no. Because each shot on a position affects multiple sections. So breaking two distant sections by shooting each of them might not be the best approach.

Alternatively, for each possible pair of two sections, whether adjacent or not, the minimal shots required can be found by considering the optimal way of shooting to break those two. However, for large n, checking all pairs is O(n^2), which is not feasible. So we need a smarter approach.

Wait, maybe the optimal solution is to break two adjacent sections. Because shooting between them can hit both. For example, if you shoot at section i, then i-1 and i+1 take 1 damage each. So shooting the same section multiple times can affect two adjacent sections.

So perhaps the optimal solution comes from considering adjacent pairs and pairs with one in between. Let's see.

Take the example where the two sections are adjacent. Suppose sections i and i+1. To break them, what's the minimal shots? Let's model this.

Each shot at i will deal 2 damage to i, 1 to i-1 and i+1. Similarly, a shot at i+1 deals 2 to i+1, 1 to i and i+2. But maybe shooting the middle (i or i+1) multiple times can help both.

Alternatively, for a pair of adjacent sections (i, i+1), the minimal shots can be found by considering that some shots are fired at i, some at i+1, and some at i+0.5 (but that's not possible, since you can only shoot sections). Hmm. Alternatively, think of shooting at i and/or i+1 and/or other positions. But how?

Alternatively, for the pair (i, i+1), perhaps the optimal way is to shoot some combination of i and i+1 such that the total damage to both is sufficient. Let's model this.

Let x be the number of shots fired at i, and y the number of shots fired at i+1. Then, the damage to i is 2x + y (since each shot at i gives 2 to i, and each shot at i+1 gives 1 to i). Similarly, damage to i+1 is x + 2y. We need 2x + y ≥ a_i, and x + 2y ≥ a_{i+1}.

We need to find the minimal x + y that satisfies these two inequalities. This is a linear programming problem, but since x and y are non-negative integers, we can model this as solving for the minimal x + y given the constraints.

Alternatively, to find the minimal sum x + y such that 2x + y ≥ s1 and x + 2y ≥ s2, where s1 = a_i, s2 = a_{i+1}.

This can be solved mathematically. Let's see:

We can model this as a system:

2x + y ≥ s1  
x + 2y ≥ s2  
x, y ≥ 0, integers.

We can find the minimal x + y.

The minimal sum would be the ceiling of (s1 + s2) / 3. But wait, maybe not exactly. Let's think. For example, in the second sample input:

3 sections, a = [1,8,1]. The optimal is to shoot once at position 2. This deals 2 damage to 2, and 1 to 1 and 3. So sections 1 and 3 take 1 each. Their initial durability is 1 each. So after one shot, they are both 0. So the minimal shots is 1. Here, s1 = 1 (for position 1), s2 =1 (position 3). But the pair (1,3) is not adjacent. So this case is different. Wait, in this example, the two sections are 1 and 3 (distance 2 apart). So perhaps the approach of considering all pairs of distance up to 2 is necessary.

But back to the adjacent pair. Let's model the equations for x and y.

The equations can be rewritten as:

y ≥ s1 - 2x  
x ≥ s2 - 2y  
But this is a bit messy. Let's think of the sum x + y.

Alternatively, if we consider the sum S = x + y. Let's see.

We have:

2x + y ≥ s1 --> y ≥ s1 - 2x  
x + 2y ≥ s2 --> x ≥ s2 - 2y  

But substituting y = S - x, then:

2x + (S - x) ≥ s1 → x + S ≥ s1 → x ≥ s1 - S  
Similarly, x + 2(S - x) ≥ s2 → -x + 2S ≥ s2 → 2S - x ≥ s2 → x ≤ 2S - s2  

But this seems a bit involved. Maybe there's a better approach.

Alternatively, think of x and y as real numbers (non-integers) and find the minimal sum. Then adjust to integers.

The minimal sum occurs when the two inequalities are tight. So:

2x + y = s1  
x + 2y = s2  
Adding the two equations: 3x + 3y = s1 + s2 → x + y = (s1 + s2)/3  
So the minimal sum is (s1 + s2)/3. But since x and y must be integers and the sum must be at least the ceiling of (s1 + s2)/3. But this is not necessarily the case. For example, if s1 and s2 are such that (s1 + s2) is not divisible by 3, then the sum x + y must be at least ceil((s1 + s2)/3). However, this might not always hold. Let's take an example.

Suppose s1=3, s2=3. Then (3+3)/3 = 2. So x+y=2. Let's see possible x and y.

Equations:

2x + y >=3  
x + 2y >=3  

Possible solutions: x=1, y=1 → sum 2. 2*1 +1=3 ≥3, 1 +2*1=3 ≥3. So sum is 2. Which works.

Another example: s1=2, s2=2. Then (2+2)/3=1.333. Ceiling is 2. Let's see: sum=2. x=2, y=0 → 2*2 +0=4 >=2, 2 + 0=2 >=2. Sum is 2. So yes.

So in the real case, the minimal sum is ceil((s1 + s2)/3). But when converted to integers, perhaps that's the minimal.

But in the case where s1 and s2 are large, and (s1 + s2) is divisible by 3, then sum is (s1 +s2)/3, which is the minimal. So for adjacent pairs, the minimal shots required is the ceiling of (a_i + a_{i+1}) / 3. But since we need integer shots, the minimal sum is ceil((a_i + a_{i+1}) / 3). Wait, but in the case where s1 and s2 are such that when added and divided by 3, the sum x + y is sufficient. Wait, but maybe there's a case where even if (s1 + s2) is divisible by 3, you might need x + y to be higher. But the example above shows that when s1=3, s2=3, sum is 2 (which is exactly (3+3)/3=2). So that's possible.

So for adjacent pairs, the minimal shots is ceil((s1 + s2)/3). But wait, what about if s1=5 and s2=5? (5+5)/3=3.333. Ceil is 4. Let's see if sum 4 is possible.

Equations:

2x + y >=5  
x + 2y >=5  
sum x + y =4.

Express y =4 -x.

Substitute into first equation: 2x + (4 -x) >=5 → x +4 >=5 → x >=1.

Second equation: x + 2*(4 -x) >=5 → x +8 -2x >=5 → -x >=-3 → x <=3.

So x can be 1,2,3.

Check x=1: y=3.

First equation: 2*1 +3=5 >=5. Second equation: 1 +2*3=7 >=5. So sum 4 works.

So sum 4 is sufficient. So yes, the minimal sum is indeed ceil((s1 +s2)/3).

So for adjacent pairs, the minimal shots needed is the ceiling of (a_i + a_{i+1}) / 3.

But since we can't have fractions, we can compute (s1 + s2 + 2) // 3. Because (a + b + 2) //3 is equivalent to ceil((a + b)/3). For example, 3+3=6 → 6//3=2. 5+5=10 → (10+2)/3=12/3=4. Correct.

So for each adjacent pair i and i+1, compute (a_i + a_{i+1} + 2) //3. The minimal among these is a candidate for the answer.

Then, what about pairs that are two apart (i and i+2). Let's see. For example, in the second sample input, the sections are 1, 8, 1. The pair 1 and 3 (distance 2 apart). The minimal shots is 1. How does that fit?

In this case, shooting once at position 2. Each shot at 2 deals 2 damage to 2, 1 to 1 and 3. So sections 1 and 3 each take 1 damage. Their initial a_i was 1 each. So after one shot, both are broken. So the sum is 1.

So for a pair i and i+2, the minimal shots can be determined by shooting at the middle section (i+1). Each shot here deals 1 to i and i+2. So each shot contributes 1 to each of them. So the number of shots needed is the maximum of ceil(a_i), ceil(a_i+2), but wait. Wait, the sum of the required damage for i and i+2.

Wait, each shot at i+1 gives 1 damage to i and 1 to i+2, and 2 to i+1. So, for the pair i and i+2, we can shoot k times at i+1. Then, the total damage to i is k, and to i+2 is k. So to break both, we need k ≥ a_i and k ≥ a_{i+2}. So the minimal k is max(a_i, a_{i+2}).

But wait, that's only if we are not considering shooting other positions. For example, perhaps shooting some shots at i, some at i+2, and some at i+1. But that might not be optimal.

Alternatively, the minimal number of shots to break both i and i+2 is the maximum of a_i and a_{i+2}. Because each shot at the middle gives 1 to each. So, for example, if a_i is 3 and a_{i+2} is 5, then we need 5 shots, which would deal 5 to a_i and 5 to a_{i+2}, breaking both. But perhaps there's a way to combine shots at i, i+1, and i+2 to reduce the total. Let's see.

Suppose we have a_i=3 and a_j=5 (j = i+2). If we shoot x times at i, y times at j, and z times at i+1.

Then, damage to i is 2x (from x shots at i) + z (from z shots at i+1) + ... (but if j is i+2, then shooting at j gives 1 damage to j-1 (i+1), but not to i). Wait, the j is i+2. So shooting at j (i+2) would affect j-1 (i+1) and j+1 (i+3), but not i. So the only way to damage i and j is to shoot at i, i+1, or j, but:

- Shooting at i: gives 2 to i, 1 to i-1 and i+1. So i+2 is not affected.
- Shooting at i+1: gives 2 to i+1, 1 to i and i+2.
- Shooting at j (i+2): gives 2 to j, 1 to j-1 (i+1) and j+1.

So to damage i and j (i+2), the only way is to shoot at i+1. Because shooting at i+1 gives 1 to i and 1 to j. So each shot at i+1 contributes 1 to both. So to break both, you need at least a_i and a_j damage. So the minimal k is max(a_i, a_j). Because each shot gives 1 to both, so you need k >= a_i and k >= a_j. So k is the maximum of the two. So the total shots is max(a_i, a_j). But wait, in the example where a_i=3 and a_j=5, then max is 5. But is there a way to do it in 5 shots?

Shooting 5 times at i+1: damage to i is 5 (3 + 5 >= 3?), but initial a_i is 3. So 5 damage would break it, and 5 damage to j (a_j=5) breaks it. So yes. So sum is 5 shots.

Alternatively, what if we shoot 3 times at i+1 and 2 times at j. Let's calculate:

Shooting 3 times at i+1: i gets 3 damage (so broken), j (i+2) gets 3. Then, shooting 2 times at j: each shot gives 2 to j, and 1 to i+1 and j+1. So the j's damage is 3 (from i+1 shots) + 2*2=4 → total 3+4=7, which is more than 5. But the total shots are 3+2=5. Wait, but j's initial a_j is 5. So 3 (from i+1) + 2*2 (from j's shots) = 3 +4 =7, which exceeds 5. So the j is broken. So total shots 5. But the original approach was 5 shots. So same sum.

But in this case, the shots at j are not contributing to i's damage, but perhaps we can find a way to reduce the sum. Hmm, but in this example, the sum is same as the maximum. So perhaps the minimal sum is indeed the maximum of a_i and a_j for i and j being two apart.

Wait, in the second sample input, the pair is 1 and 3 (a_1=1, a_3=1). The maximum is 1. So shooting once. Which works.

Another example: a_i=2, a_j=3. Max is 3. So shooting 3 times. Each shot gives 1 to each. So i is 3, which is >=2, broken. j is 3, broken. Sum 3. Alternatively, could we shoot 2 times at i+1 and 1 time at i. Let's see:

Shooting 2 times at i+1: i takes 2, j takes 2. Then, shoot once at i: gives 2 to i (total 2+2=4), 1 to i-1 and i+1. But j is i+2, so not affected. So j's damage is 2. So j's total is 2 <3, so not broken. So need 3 shots.

So in this case, the minimal is indeed 3.

So for pairs two apart, the minimal shots needed is the maximum of the two a's.

So, putting this together, the minimal shots can be either:

- The minimal (a_i + a_{i+1} + 2) //3 for adjacent pairs.

OR

- The minimal max(a_i, a_{i+2}) for pairs two apart.

Additionally, there's another case where we need to break two sections that are not adjacent or two apart. For example, if two sections are very far apart. For such pairs, the minimal shots would be the sum of the shots needed to break each individually. But how?

Wait, but each shot can affect multiple sections. So perhaps it's possible to break two far apart sections with fewer shots than breaking each individually. But how?

For example, suppose you have sections 1 and 4. To break them, maybe you can shoot section 2 and 3, which each affects their neighbors. But it's not clear. Let's see.

Alternatively, for any pair (i, j) where j >= i+3, the minimal number of shots required to break both is the sum of the minimal shots needed to break i and j individually, since each shot can affect at most one of them. But that's not necessarily true. For example, if you shoot a section that affects both. But if j >=i+3, then there's no way for a single shot to affect both. So any shot can't hit both. So for such pairs, the damage to i and j must be handled by separate shots. Therefore, the minimal shots would be the sum of the minimal shots needed to break each.

But the minimal shots to break a single section x is ceil(a_x / 2). Because each shot to x deals 2 damage. So, for example, if a_x is 5, then 3 shots (3*2=6 ≥5). So ceil(5/2) =3.

So for two sections that are far apart, the minimal shots required is ceil(a_i/2) + ceil(a_j/2).

So the overall minimal answer would be the minimum between:

1. The minimal (a_i + a_{i+1} + 2) //3 for all adjacent pairs.

2. The minimal max(a_i, a_{i+2}) for all pairs two apart.

3. The minimal ceil(a_i/2) + ceil(a_j/2) for all pairs.

But considering all pairs for case 3 is O(n^2), which is not feasible. So how can we find the minimal sum of ceil(a_i/2) + ceil(a_j/2) without checking all pairs?

The minimal sum in this case is the sum of the two smallest values of ceil(a_i/2). Because we need to pick two sections, and their ceil(a_i/2) summed. So to find the minimal sum, we can find the two smallest ceil(a_i/2) values and add them.

So for case 3, the minimal is the sum of the two smallest ceil(a_i/2) values.

So the overall approach is:

Compute three values:

- min_adjacent: the minimal (a_i + a_{i+1} + 2) //3 over all adjacent pairs.

- min_two_apart: the minimal max(a_i, a_{i+2}) over all pairs two apart (i, i+2).

- min_singles: the sum of the two smallest ceil(a_i/2) over all sections.

The answer is the minimum of these three values.

Wait, but for the third case, min_singles is the sum of the two smallest ceil(a_i/2) values. Because those two sections could be any, even adjacent or two apart. But if their sum is smaller than the first two cases, then that's better.

So, in code:

Compute all three possible candidates and take the minimal.

So, how to compute these?

Let's see:

For min_adjacent: iterate from i=0 to i=n-2, compute (a[i] + a[i+1] + 2) //3, take the minimal.

For min_two_apart: iterate from i=0 to i=n-3, compute max(a[i], a[i+2]), take the minimal.

For min_singles: find the two smallest values of ceil(a[i]/2). Sum them.

So for each a[i], compute (a[i] + 1) // 2. Then find the two smallest of these and sum.

So all three steps are O(n) time, which is acceptable for n up to 2e5.

Then, the answer is the minimum of these three candidates.

Yes.

Now, let's test this approach against the examples.

First example:

Input:5

20 10 30 10 20

Adjacent pairs:

(20,10): (20+10 +2)/3 =32//3=10.666 → 10.666 floored? Wait, (20+10+2)=32, 32//3=10.666 → 10 in integer division. But wait, (20+10) is 30. 30 /3 is 10. So (30 +2) is 32. 32//3 is 10. So the value is 10.666... So integer division gives 10.

But according to the formula (a_i +a_{i+1} +2)//3.

Wait, (a_i + a_j +2)//3 is equivalent to ceil((a_i +a_j)/3). Because (x + y +2) //3 is equal to (x + y) //3 if (x + y) mod3 is 0, else (x + y +2) //3 is (x + y) //3 +1. So it's the same as ceil((x+y)/3).

So for (20,10), sum is 30. 30/3=10. So candidate is 10.

The next pair (10,30): (10+30 +2)/3=42//3=14.

Then (30,10): 40+2=42/3=14.

Then (10,20): 30+2=32/3=10.666 → 10.

So the min_adjacent is 10.

min_two_apart: pairs are (20,30), (10,10), (30,20).

For (20,30) → max(20,30)=30.

(10,10) → 10.

(30,20) →30. So min_two_apart is 10.

min_singles: compute ceil(a_i/2) for each:

20 →10, 10 →5, 30→15, 10→5, 20→10.

The two smallest are 5 and 5. Sum is 10.

So all three candidates are 10, 10, 10. So the minimal is 10. Which matches the first example.

Second example:

3

1 8 1.

Adjacent pairs:

(1,8) → (9+2)//3=11//3=3.666→3. So 3.666 floored to 3. But wait, (1+8)/3=3 → ceil(3) is 3. So the candidate is 3.

(8,1) → (9+2)//3=3.666→3. So min_adjacent is 3.

But the correct answer is 1. So this suggests that the adjacent pair's candidate is 3, but the actual answer is in the two_apart case.

So min_two_apart: the pair (1,1), which is positions 0 and 2. max(1,1) =1. So min_two_apart is 1.

The min_singles would be ceil(1/2) + ceil(1/2) =1+1=2.

So the three candidates are 3,1,2. The minimal is 1. Which matches the example.

Third example:

6

7 6 6 8 5 8 → sample output is4.

Let's compute the three candidates.

Adjacent pairs:

(7,6) → (7+6+2)//3=15//3=5.

(6,6) →14//3=4.666→4. So 6+6=12; 12+2=14 →14//3=4.666 →4 in integer division. But (6+6)/3=4. So candidate is4.

(6,8) →14 +2=16//3=5.333→5.

(8,5) →13+2=15//3=5.

(5,8) →13+2=15//3=5.

So min_adjacent is4.

min_two_apart: pairs are (7,6) (i=0 and 2): max(7,6)=7.

(6,8): max(6,8)=8.

(6,5): max(6,5)=6.

(8,8): max(8,8)=8.

So the min_two_apart is6.

min_singles: ceil(7/2)=4, ceil(6/2)=3, ceil(6/2)=3, ceil(8/2)=4, ceil(5/2)=3, ceil(8/2)=4. The two smallest are3 and3. Sum is6.

So candidates are4,6,6. The minimal is4. Which matches the sample.

Fourth example:

Input:

6

14 3 8 10 15 4 → sample output is4.

Compute the three candidates.

Adjacent pairs:

14+3=17 →17+2=19 →19//3=6.333→6.

3+8=11 →11+2=13 →13//3=4.333→4.

8+10=18 →18+2=20 →20//3=6.666→6.

10+15=25 →25+2=27 →27//3=9.

15+4=19 →19+2=21 →7.

So min_adjacent is4 (from 3+8).

min_two_apart: pairs are (14,8), (3,10), (8,15), (10,4). 

max(14,8)=14; max(3,10)=10; max(8,15)=15; max(10,4)=10. The minimal is10.

min_singles: ceil(14/2)=7, 3→2, 8→4,10→5,15→8,4→2. The two smallest are2 and2. Sum is4.

So the candidates are4 (adjacent),10 (two_apart),4 (singles). So the answer is4. Which matches the sample.

Another sample:

Input:4

1 100 100 1 → output 2.

Adjacent pairs:

1 and100 → (1+100+2)/3=103//3=34.333→34.

100 and100 →200+2=202//3=67.333→67.

100 and1 →101+2=103//3=34.

So min_adjacent is34.

min_two_apart: pairs (1,100) (i=0 and2). max(1,100)=100. (100,1) (i=1 and3) →max(100,1)=100. So min_two_apart is100.

min_singles: ceil(1/2)=1 (for positions 0 and3), and 100s would be 50 each, but the two smallest are1 and1. Sum 2. So the minimal is2. Which is the answer.

So the three candidates are34,100,2. So the answer is2.

Another sample:

Input:3

40 10 10 → output7.

Adjacent pairs:

40+10=50 →50+2=52//3=17.333→17.

10+10=20 →20+2=22//3=7.333→7. So min_adjacent is7.

min_two_apart: pair is40 and10 (i=0 and2). max(40,10)=40. So min_two_apart is40.

min_singles: ceil(40/2)=20, ceil(10/2)=5, ceil(10/2)=5. Sum of two smallest is5+5=10.

So the candidates are7,40,10. So minimal is7. Which matches the sample.

So the approach seems to work.

So the code should compute these three values and take the minimal.

Now, the code steps:

Read n, a list.

Compute min_adjacent:

Initialize to a very large number.

Loop from i=0 to n-2:

current = (a[i] + a[i+1] + 2) //3

if current < min_adj: update min_adj.

Compute min_two_apart:

Initialize to very large.

Loop from i=0 to n-3:

current = max(a[i], a[i+2])

if current < min_two_ap: update.

Compute min_singles:

Compute all (a_i +1) //2.

Find the two smallest, sum them.

The answer is the minimal of min_adj, min_two_ap, and min_singles.

Edge cases:

n=2. Then, min_two_apart is not possible. So in code, the loop for min_two_apart will not run, and min_two_ap remains a large value. So when taking the minimum, min_two_ap is ignored.

Similarly, for n=2, the code works.

For example, n=2:

a = [1,1]

adjacent pair gives (1+1+2)//3=4//3=1.33→1. So min_adj is1.

min_two_ap is not considered (since n=2, no i+2). So min_two_ap is infinity.

min_singles: ceil(1/2)=1 and1 → sum 2.

So answer is1.

Another test case for n=2.

Sample input:

2

3 3 → output is (3+3+2)/3 =8/3=2.666 →2. So answer is2.

Which would break both after 2 shots. Let's see:

Each shot on section1: damage to1 is2 per shot, 1 to2.

Shoot section1 2 times:

damage to1: 2*2=4 →3-4 = -1.

damage to2: 2*1=2 →3-2=1. So section1 is broken. But section2 is not. So need to break another. Wait, but this would require shooting again.

Wait, the code's approach for adjacent pair would compute (3+3+2)/3=8/3=2. So the code's candidate is2. But in reality, 2 shots may not be enough.

Wait, let's model the adjacent pair for (3,3).

We need to find x and y (shots at i and i+1) such that:

2x + y >=3 → equations.

x + 2y >=3.

x + y is minimized.

Let x=1, y=1: sum=2.

Equations:

2*1 +1=3 >=3 → yes.

1 + 2*1=3 >=3 → yes. So sum is2.

So 2 shots. Let's see:

Shooting once at i and once at i+1.

Each shot on i: damage i by2, i+1 by1.

Each shot on i+1: damage i+1 by2, i by1.

So for i=1 (sections 1 and 2):

Shoot once at1 and once at2.

Damage to1: 2 (from shot at1) +1 (from shot at2) =3 →3 >=3.

Damage to2:1 (from shot at1) +2 (from shot at2) =3 →3 >=3.

Yes. So sum 2 shots. So the code's calculation is correct.

So the code works.

Another edge case: n=2, a = [1, 2].

Adjacent pair (1+2+2)=5 →5//3=1. So candidate is1.

But how?

x + y must be 1.

Possible x=0, y=1.

Equations: 2x +y =0 +1=1 >=1 → yes.

x +2y=0 +2*1=2 >=2 → yes. So sum is1. So possible.

So one shot at section2.

Damage to section1:1.

Damage to section2:2.

So initial a1=1, after 1 shot:

a1 is 1 -1 =0 → broken.

a2 is2 -2=0 → broken. So yes. So one shot is sufficient.

Thus, the code correctly computes this.

Thus, the code should handle all cases.

Now, implement this in Python.

Read n.

Read the list a.

Compute min_adjacent.

Compute min_two_apart.

Compute min_singles.

The minimal of the three is the answer.

Handle cases where n <3 for min_two_apart (like n=2, then min_two_ap is infinity).

For the two_apart case: loop i from 0 to n-3. For each i, compute max(a[i], a[i+2]).

For min_singles, compute all the (x+1)//2, collect in a list, then find the two smallest.

So code steps:

Read n.

a = list of integers.

Compute min_adj = min( (a[i] + a[i+1] + 2) //3 for i in range(n-1) )

min_two_ap = min( max(a[i], a[i+2]) for i in range(n-2) ) if n >=3 else infinity.

compute the list of (x +1)//2 for x in a.

sort this list, take first two elements, sum.

ans = min( min_adj, min_two_ap, min_singles )

print(ans).

But for n=2, the min_two_ap is not possible. So in code:

Initialize min_two_ap to a very large value (like 1e18). Then, if n >=3, loop through the possible i and find the minimal.

So code:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    min_adj = float('inf')

    for i in range(n-1):

        s = a[i] + a[i+1]

        current = (s + 2) // 3

        if current < min_adj:

            min_adj = current

    min_two_ap = float('inf')

    if n >=3:

        for i in range(n-2):

            current = max(a[i], a[i+2])

            if current < min_two_ap:

                min_two_ap = current

    # compute min_singles

    singles = [(x +1) //2 for x in a]

    # find the two smallest

    singles.sort()

    min_singles = singles[0] + singles[1]

    ans = min(min_adj, min_two_ap, min_singles)

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
7 6 6 8 5 8
""",
            "output": \
"""\
4
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

Testing against sample input 5.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    min_adj = float('inf')

    for i in range(n-1):

        s = a[i] + a[i+1]

        current = (s + 2) // 3

        if current < min_adj:

            min_adj = current

    min_two_ap = float('inf')

    if n >=3:

        for i in range(n-2):

            current = max(a[i], a[i+2])

            if current < min_two_ap:

                min_two_ap = current

    # compute min_singles

    singles = [(x +1) //2 for x in a]

    # find the two smallest

    singles.sort()

    min_singles = singles[0] + singles[1]

    ans = min(min_adj, min_two_ap, min_singles)

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
40 10 10
""",
            "output": \
"""\
7
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

Another test case: n=2, a=[1,1].

min_adj is (1+1+2)/3=4//3=1.

min_two_ap is infinity.

singles: [1,1]. sum is2.

ans is min(1, inf, 2) →1. Which is correct.

Another test case: n=2, a=[3,3].

min_adj: (3+3 +2)/3=8//3=2.666 →2.

min_two_ap: inf.

singles: 2+2=4.

ans is min(2, inf,4) →2. Correct.

Thus, the code works.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
min_adj = float('inf')
for i in range(n - 1):
    current = (a[i] + a[i + 1] + 2) // 3
    if current < min_adj:
        min_adj = current

min_two_ap = float('inf')
if n >= 3:
    for i in range(n - 2):
        current = max(a[i], a[i + 2])
        if current < min_two_ap:
            min_two_ap = current

singles = [(x + 1) // 2 for x in a]
singles.sort()
min_singles = singles[0] + singles[1]

ans = min(min_adj, min_two_ap, min_singles)
print(ans)
```
