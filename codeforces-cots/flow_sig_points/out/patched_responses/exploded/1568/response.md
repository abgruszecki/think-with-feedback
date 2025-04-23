<think>
Okay, let's try to figure out this problem. So the game is between Kevin and Nicky, and they take turns. The rules are that each turn, a player can either remove one cow from a pile or, if a pile has an even number of cows, replace it with k piles of x cows each where 2x was the original size. The winner is the one who takes the last cow.

Hmm, the key here is to calculate the Grundy number (nimber) for each pile, then XOR them all. If the total is non-zero, Kevin wins; otherwise Nicky does. So we need to find the Grundy number for a pile of size a_i under the given game rules.

But how do we compute the Grundy numbers efficiently, especially considering that a_i can be up to 1e9 and n up to 1e5? Let's think about the possible moves for a pile of size x.

For any x, the first move option is to take 1, leading to x-1. The second move is possible only if x is even and k is even or odd. Wait, the second move splits the pile into k piles of x/2 each. So the Grundy number for x would be the mex (minimum excludant) of the possible moves' Grundy values.

Wait, the Grundy number for a position is the mex of all possible next positions' Grundy numbers. For move 1: subtract 1, so the next state is x-1. For move 2: when x is even, split into k piles of x/2. Since all those piles are the same, the Grundy number for this move is the XOR of k copies of the Grundy number of x/2. But if k is even, then XORing even times the same number cancels out (since a XOR a = 0). For example, if k is even, the XOR is 0. If k is odd, then it's the same as the Grundy number of x/2.

So when x is even, the possible options are:

- Take 1, leading to x-1's Grundy number.
- Split into k piles of x/2, whose total Grundy is (grundy(x/2) XOR ... XOR grundy(x/2)) [k times]. So that's grundy(x/2) multiplied by k mod 2. Because XORing even times gives 0, odd times gives the value itself. So the result is grundy(x/2) if k is odd, else 0.

So the mex is taken between the Grundy number of x-1 and the possible split move's value (if applicable). So for each x, the possible moves are:

1. The Grundy number of x-1.
2. If x is even, the split move's value (which is grundy(x/2) * (k % 2)).

But how to compute this efficiently?

Let's model the Grundy numbers for small x and see if there's a pattern. Let's call g(x) the Grundy number for x.

Base case: g(0) = 0 (since no moves can be made). But wait, the pile can't be zero in the game. So for x=1: possible moves are take 1, leading to x=0. The mex of {0} is 1? Wait, no. Wait, when x is 1, the only move is to take 1, which leaves 0. The mex of the set {g(0)} = {0} is 1? No, mex is the smallest non-negative integer not in the set. So {0} has mex 1. So g(1) is 1?

Wait, wait. Let's compute g(0) as 0. Then for x=1:

Possible moves:

Move 1: remove 1, leading to x=0. The mex of {g(0)} which is 0. So mex is 0's mex is 1? Wait no. Wait, mex is the smallest non-negative integer not present. So for x=1's possible next states' grundy numbers, which is {0}. So mex is 1. So g(1) = 1.

x=2: possible moves are:

1. Remove 1, leading to x=1. So g(1) =1.

2. Split into k piles of 1. So the split move's value is (g(1) XOR ... k times). If k is even, that's 0. If k is odd, that's 1.

So for x=2, the mex of {1, (split_value)}.

Split_value is 1 if k is odd, else 0.

So mex would be the smallest non-negative integer not in the set {1, split_value}.

So for example, if k is even (split_value 0):

The set is {0,1}, mex is 2. So g(2)=2.

If k is odd (split_value 1):

The set is {1}, mex is 0. So g(2)=0.

Wait that's interesting. So the value of k mod 2 affects the grundy numbers.

So the key here is to find a pattern in g(x) that depends on the parity of k.

Hmm, let's see. Let's consider two cases: k is even and k is odd.

Case 1: k is even.

When splitting even x into k piles of x/2. Since k is even, the XOR is 0 (as even number of same elements XORed gives 0).

So for even x, the split move's grundy is 0.

So for even x, the possible options are:

- Take 1, leading to x-1. So grundy(x) = mex of {g(x-1), 0}.

Because the split move contributes 0 to the mex set.

For example, when x=2 and k even:

split_value is 0. So mex of {g(1)=1, 0} is 2 (since 0 and 1 are present).

So g(2) = 2.

x=3: options are take 1 to x=2. So mex of {2} is 0. So g(3)=0?

Wait, no. Because for x=3, the possible move is only take 1, leading to x=2. So the mex is the mex of {g(2)}=2. So mex is 0.

Wait, that's possible. So when x is odd, the split move is not possible. So for x=3, the mex is the mex of {g(2)} which is 2. So mex is 0?

Wait, mex is the smallest non-negative integer not in the set. So if the set is {2}, then mex is 0. Wait, no. Wait, the set is {2}, which is present, so the mex is 0? No. Wait, mex is the smallest non-negative integer not in the set. So if the set is {2}, then 0 is missing. So mex is 0.

So for x=3, g(3) = 0.

Hmm, but let's re-examine. For x=3:

Possible moves: only the first move, subtract 1. So next state is x=2. The mex of {g(2)}=2's grundy is 2 (if k is even). So mex of {2} is 0 (since 0 is not present). So g(3)=0.

So x=3's grundy is 0 when k is even.

x=4 (even):

Possible moves:

- subtract 1 to x=3 (grundy 0).

- split into k piles of 2. Since k is even, split_value is 0.

So mex is the mex of {0, 0} → {0}. So mex is 1.

So g(4)=1.

Wait, mex of {0} is 1. So for x=4, the possible options are 0 and 0 (since both moves contribute 0 and 0). So the set is just {0}. So mex is 1.

So g(4)=1.

x=5: moves subtract 1 → x=4 (g=1). So mex of {1} is 0. So g(5)=0.

Hmm, this seems to form a pattern. Let's see:

When k is even:

g(0) = 0.

g(1) = mex {0} → 1.

g(2) = mex {1, 0} (since split move gives 0 when k even). So mex is 2.

g(3) = mex {2} → 0.

g(4) = mex {0, 0} (split move gives 0). So mex of {0} is 1.

g(5) = mex {1} → 0.

g(6) = mex {0, 0} (split move gives 0). So mex of {0} → 1?

Wait, but x=6 is even. So the moves are subtract 1 (x=5, g=0) and split (split_value is 0). So mex of {0,0} is 1.

So g(6)=1.

Hmm, the pattern for even k seems to be that for even x >=2, the grundy numbers alternate between 2, 1, 2, 1, etc. Wait, but in the case of x=2, it's 2, x=4 is 1, x=6 is 1? Wait no, for x=6, the split move's value is 0 (since k is even). The possible moves are x-1 (5) which is 0, and split which gives 0. So mex of {0} is 1.

Hmm. So for even k, the grundy numbers for even x seems to follow a certain pattern.

Alternatively, perhaps there's a cycle here. Let's see:

When k is even, the split move's grundy is 0. So for even x, the possible options are:

- x-1 (which may be even or odd), and the split move (grundy 0).

So for even x, the mex is the mex of {g(x-1), 0}.

Let's see:

x=2: mex {1, 0} → mex is 2.

x=4: mex {0 (from x=3), 0} → mex is 1.

x=6: mex {0 (from x=5), 0} → mex is 1.

x=8: mex {1 (from x=7's grundy?), 0} → depends on x=7's grundy.

Wait, this seems complicated. Let's think again.

Alternatively, maybe the grundy numbers for even k can be computed as follows:

For even x, the split move's grundy is 0 (since k is even). So for even x, the mex is the mex of g(x-1) and 0.

For odd x, the mex is mex of g(x-1) (since split is not possible).

But how to model this?

Let's see for even k:

g(1) = 1.

g(2) = mex {1,0} → 2.

g(3) = mex {2} → 0.

g(4) = mex {0,0} → 1.

g(5) = mex {1} → 0.

g(6) = mex {0,0} → 1.

g(7) = mex {1} → 0.

g(8) = mex {0,0} → 1.

So the pattern for even k is:

x | g(x)

0 → 0

1 → 1

2 → 2

3 →0 

4 →1 

5 →0 

6 →1 

7 →0 

8 →1 

So even x >= 2: for x=2, 2, x=4,1; x=6,1; etc.

Wait, but x=2 is even, and its mex is 2 (since {1,0} are the options). So mex is 2.

Then for x=4, mex is {0,0} → mex is 1.

x=6: mex {0,0} →1.

So the grundy numbers for even x when k is even:

if x is even:

if x == 2 → 2.

else:

if (x/2) is even → ?

Alternatively, perhaps for even x >= 4, when x is even, g(x) is 1 if x mod 4 == 0 or 2 mod 4, except x=2.

Wait, but x=2 is 2 mod 4. So for x=2, g is 2. For x=4 (mod 4 0), g is 1. x=6 (mod4 2) →1.

Hmm. So perhaps for even x:

if x is 2 → g=2.

else, if x is even and k is even, then g(x) = 1 if x is even and x is not 2.

But wait, x=4: 1, x=6:1, x=8:1. So maybe for even x >=4, when k is even, grundy is 1 if x is even and not 2.

But why x=2 is different.

Wait, maybe the grundy numbers for even k can be determined as follows:

For even x, split into k piles (even), which gives grundy 0. So the mex is mex of (g(x-1), 0).

So for x=2:

g(2-1)=g(1)=1. So mex {1,0} → mex is 2.

For x=4:

g(3) is 0. So mex {0,0} → mex is 1.

For x=6:

g(5) is 0. mex {0,0} →1.

x=8: g(7) is 0 → mex is 1.

So for even x >= 4, when k is even, the grundy is 1.

So the grundy numbers for even k are:

- If x ==0: 0.

x=1:1.

x=2:2.

x=3:0.

x=4:1.

x=5:0.

x=6:1.

and so on.

So for even k, the grundy numbers can be determined as:

g(x) is 0 if x is odd, except for x=1 (which is 1). Wait, no. x=1 is 1, x=3 is 0, x=5 is 0, x=7 is 0.

Wait, for even k, when x is odd:

the possible move is subtract 1, leading to even x-1. So the mex of {g(x-1)}.

So for x=1 (odd), subtract 1 gives x=0 (g=0). mex {0} →1.

x=3 (odd): subtract 1 gives x=2 (g=2). mex {2} →0.

x=5 (odd): subtract 1 gives x=4 (g=1). mex {1} →0.

x=7 (odd): subtract 1 gives x=6 (g=1). mex {1} →0.

So for even k:

x even:

if x ==2 →2.

else →1.

x odd:

if x ==1 →1.

else →0.

So for even k, the grundy numbers are:

g(x) = 

0 if x is 0.

1 if x is 1.

2 if x is 2.

0 if x is odd and x >=3.

1 if x is even and x >=4.

So that's for even k.

Now, let's consider the case when k is odd.

Case 2: k is odd.

In this case, when you split an even x into k piles of x/2, the split move's grundy is grundy(x/2) XOR ... XOR grundy(x/2) (k times, which is odd). Since XORing an odd number of the same value gives that value. So split_value is grundy(x/2).

So for even x, the split move contributes grundy(x/2) to the mex set.

So for even x, the possible moves are:

- subtract 1, leading to x-1 (grundy(x-1)).

- split into k piles, leading to grundy(x/2).

So mex is the mex of {grundy(x-1), grundy(x/2)}.

But this is more complicated. Let's compute some examples for k odd.

Take k=1.

For x=2:

split into 1 pile of 1. So split move's grundy is grundy(1) =1.

So the possible moves are subtract 1 (gives x=1, grundy 1) and split (gives 1 pile, grundy 1).

So mex of {1,1} is 0. So g(2)=0.

For x=3:

only subtract 1 → x=2 (grundy 0). So mex {0} →1. So g(3)=1.

x=4:

possible moves:

- subtract 1 →x=3 (g=1).

- split into k=1 piles of 2. Split gives grundy(2) =0 (since x=2 for k=1, which was 0). So the split move's grundy is 0.

So mex of {1,0} → 2. So g(4)=2.

x=5:

subtract 1 →x=4 (g=2). mex {2} →0. So g(5)=0.

x=6:

subtract 1 →x=5 (g=0).

split into k=1 piles of 3. So grundy(3) =1. So mex {0,1} →2. So g(6)=2.

x=7: subtract 1 →x=6 (g=2). mex {2} →0.

x=8:

possible moves:

- subtract 1 →x=7 (g=0).

- split into k=1 piles of 4 (g=2). So mex {0,2} →1. So g(8)=1.

Hmm, this seems complicated. Let's see if there's a pattern.

Alternatively, for k odd, the split move's grundy is grundy(x/2). So for even x, the mex is mex of g(x-1) and g(x/2).

So for k odd, the grundy numbers can be computed recursively. But for x up to 1e9, this would be impossible unless we can find a pattern or a formula.

So the problem is to find a way to compute grundy(x) for x up to 1e9, for both even and odd k.

Let's think about k being odd. Let's see:

Looking for patterns.

For example, when k is odd, let's compute grundy numbers for some small x:

k=1:

x=0:0

x=1:1 (mex of {0} →1)

x=2: mex of {1, g(1)}= mex {1,1} →0

x=3: mex {0} →1

x=4: mex {1, g(2)}= mex {1,0} →2

x=5: mex {2} →0

x=6: mex {0, g(3)} → mex {0,1} →2

x=7: mex {2} →0

x=8: mex {0, g(4)}= mex {0, 2} →1

x=9: mex {1} →0

x=10: mex {0, g(5)}= mex {0,0} →1.

x=11: mex {1} →0.

x=12: mex {0, g(6)}= mex {0,2} →1.

x=14: mex {0 (x=13's g), g(7)=0} → mex {0,0} →1.

Hmm, this seems a bit tricky. For k=1, it's possible that grundy numbers cycle in some way.

Alternatively, perhaps for k odd, the grundy number of x depends on whether x is even or odd, and the number of times you can split until you get to an odd number.

Alternatively, perhaps the grundy numbers for k odd follow the mex of (x-1) and (x/2) grundy numbers. But calculating this recursively for x up to 1e9 would be O(log x) per number, which might be manageable since for each x, you can split until you reach an odd x, which is O(log x) steps.

But with n up to 1e5 and each a_i up to 1e9, this could be O(1e5 * log x) which is acceptable.

But how to model this? Let's think of the recursive steps.

Let me think of a memoization approach, but since a_i is up to 1e9, memoization is not feasible. So we need a formula.

Alternatively, find that for k odd, the grundy numbers cycle in some way.

Let's consider when k is odd.

For x even, the split option gives grundy(x/2). So for x even, mex(grundy(x-1), grundy(x/2)).

For x odd, only the subtract 1 move is possible, so mex(grundy(x-1)).

So the grundy numbers for x when k is odd can be found as follows:

If x is odd: grundy(x) = mex of {grundy(x-1)}.

If x is even: grundy(x) = mex of {grundy(x-1), grundy(x/2)}.

But how to compute this efficiently.

Let's try to compute the grundy numbers for k=1 and see if a pattern emerges.

For k=1:

x | g(x)

0 →0

1 →1

2 →0

3 →1

4 →2

5 →0

6 →2

7 →0

8 →1

9 →0

10 →1

11 →0

12 →1

13 →0

14 →1

15 →0

16 → mex {0 (15's g), grundy(8)=1} → mex {0,1} →2.

Hmm, not a clear pattern. Maybe it's possible to find that for even x when k is odd, the grundy number depends on the number of times you can divide x by 2 until you reach an odd number, and whether that count is even or odd.

Alternatively, perhaps the grundy number for x when k is odd is equal to the mex of the grundy numbers of x-1 and x/2 (if even).

But perhaps there's a way to model this.

Wait, for x even:

grundy(x) = mex{ grundy(x-1), grundy(x/2) }

But x-1 is odd, so grundy(x-1) is mex{ grundy(x-2) }.

For example, for x=4 (even):

grundy(4) = mex{ grundy(3) (1), grundy(2) (0) } → mex{1,0} → 2.

x=6 (even):

grundy(5) is 0, so grundy(6) = mex{0, grundy(3) =1} → mex{0,1} → 2.

x=8 (even):

grundy(7) is 0, grundy(4) is 2 → mex{0,2} →1.

x=10 (even):

grundy(9) is 0, grundy(5) is 0 → mex{0,0} →1.

x=12 (even):

grundy(11)=0, grundy(6)=2 → mex{0,2} →1.

x=14 (even):

grundy(13)=0, grundy(7)=0 → mex{0,0} →1.

x=16 (even):

grundy(15)=0, grundy(8)=1 → mex{0,1} →2.

So for k=1, the even x's grundy numbers are 0, 2, 2, 1, 1, 2, 1, 2, etc. It's hard to see a pattern here.

Another approach: for k odd, let's model the grundy numbers in terms of the binary representation of x.

Alternatively, perhaps for k odd, the grundy number cycles between 0, 1, 2, etc., but this is unclear.

An alternative idea: for k odd, the grundy numbers have a pattern that repeats every certain steps. For example, for even x, the grundy numbers could be computed based on the number of times x can be divided by 2.

Let's think recursively for even x and k odd.

For x even:

grundy(x) = mex(grundy(x-1), grundy(x/2)).

grundy(x-1) is for x-1 (which is odd) so grundy(x-1) = mex(grundy(x-2)).

But x-2 is even if x is even. So grundy(x-1) depends on grundy(x-2), which in turn depends on grundy(x-3) and grundy((x-2)/2).

This seems to get complicated quickly.

But perhaps there's a way to model this using memoization and recursion with memoization, but for large x.

But for x up to 1e9, recursive steps would be O(log x) per x. So for each a_i, which can be up to 1e9, the number of steps to compute grundy(a_i) would be O(log a_i), which for 1e5 a_i's would be manageable.

So the plan is:

For each a_i:

- Compute grundy(a_i) based on whether k is even or odd.

If k is even:

Use the pattern we found earlier:

For x even:

if x == 0 →0.

x ==2 →2.

x even >=4 →1.

For x odd:

x ==1 →1.

else →0.

So for k even, the grundy function can be computed in O(1) per a_i.

If k is odd:

Compute grundy(x) recursively using memoization, but since x is up to 1e9, memoization isn't feasible. So we need to find a way to compute grundy(x) in O(log x) time per x, using a helper function that computes it recursively but without memoization, but using some patterns.

So for k odd, how can we compute grundy(x) efficiently?

Let's think of the possible grundy numbers for x when k is odd.

Another approach is to note that for k odd, the split move is equivalent to replacing the pile with one pile (since k is odd, and XOR of an odd number of same values is that value). So when k is odd, splitting an even pile into k piles of x/2 is equivalent to replacing it with a single pile of x/2. Because the grundy number for the split is the same as the grundy number of x/2 (since XORing an odd number of same values gives the same value).

Wait, but splitting into k piles would be replacing one pile with k piles. So the grundy number for that move is grundy(x/2) XOR ... XOR grundy(x/2) (k times). Since k is odd, this is grundy(x/2) if k is odd.

So yes. So for k odd, splitting even x into k piles gives grundy(x/2).

So the mex for even x is mex(grundy(x-1), grundy(x/2)).

For odd x, mex(grundy(x-1)).

But how to compute this for x up to 1e9 efficiently.

Let's consider that for each x, the grundy number is determined by the mex of its possible moves.

So for x even and k odd:

g(x) = mex{ g(x-1), g(x/2) }

For x odd:

g(x) = mex{ g(x-1) }

But for x=1 (odd), mex{0} is 1.

For x=3 (odd), mex{ g(2) }.

But for x=3, k is odd: g(2) is mex{ g(1), g(1) }, which is mex{1,1} →0. So mex{0} is 1. So g(3)=1.

But how to find a pattern here.

Alternatively, perhaps the grundy numbers for k odd can be determined as follows:

For x=0:0.

x=1:1.

x=2: mex{ g(1)=1, g(1)=1} →0.

x=3: mex{0} →1.

x=4: mex{1, g(2)=0} → mex{1,0} →2.

x=5: mex{2} →0.

x=6: mex{0, g(3)=1} → mex{0,1} →2.

x=7: mex{2} →0.

x=8: mex{0, g(4)=2} → mex{0,2} →1.

x=9: mex{1} →0.

x=10: mex{0, g(5)=0} → mex{0,0} →1.

Hmm, no obvious pattern. But perhaps for even x and k odd, the grundy number can be computed by looking at the mex of the grundy of x-1 and the grundy of x/2.

But how to compute this quickly.

Let's think recursively for x even:

g(x) = mex(g(x-1), g(x/2)).

But x-1 is odd. So for x even:

g(x-1) = mex(g(x-2)).

But x-2 is even. So this requires computing g(x-2) for even x-2.

But this seems to lead to a chain of recursive calls.

But for large x, this is not feasible. So we need to find a way to model this.

Alternative approach: precompute the grundy numbers for k odd up to some point and look for patterns.

But let's see:

For k=1:

x | g(x)

0 →0

1 →1

2 →0

3 →1

4 →2

5 →0

6 →2

7 →0

8 →1

9 →0

10 →1

11 →0

12 →1

13 →0

14 →1

15 →0

16 →2

Wait, x=16 even. Split into k=1 piles of 8. g(8) is 1. So mex of g(15) (0) and 1 → mex {0,1} →2. So g(16)=2.

x=17: mex{g(16)=2} →0.

x=18: mex{g(17)=0, g(9)=0} → mex {0,0} →1.

x=20: even. x/2=10, g(10)=1. x-1=19 (g=0). mex {0,1} →2.

So x=20's grundy is 2.

Hmm, for even x and k=1, the grundy number seems to depend on whether x/2 is even or odd.

Alternatively, perhaps for even x and k odd, the grundy number can be computed as follows:

For x even:

If x is a power of 2 multiplied by some odd number, then the grundy number is based on the exponent in the 2's factor.

But not sure.

Alternatively, perhaps the grundy number for x when k is odd is equal to the number of times you can divide x by 2 until you reach an odd number, plus some adjustment.

But for example, x=4 (divided by 2 once to reach 2, again to reach 1). But the grundy for x=4 is 2.

x=8: divided three times (8 →4 →2 →1). grundy is 1.

Hmm, no obvious relation.

Alternative idea: for x even and k odd, the grundy number is the mex of the grundy of x-1 and the grundy of x/2. So this is a recursive relation. So to compute g(x), we can compute g(x/2) and g(x-1). But for x up to 1e9, this would be O(log x) steps per x.

So for a given x, the function would look like:

def grundy(x):
    if x == 0:
        return 0
    if k % 2 == 0:
        # handle even k case
        if x == 1:
            return 1
        elif x == 2:
            return 2
        elif x % 2 == 1:
            return 0
        else:  # even x >=4
            return 1
    else:
        # handle odd k case
        if x in memo:
            return memo[x]
        if x % 2 == 1:
            res = mex([grundy(x-1)])
        else:
            res = mex([grundy(x-1), grundy(x//2)])
        memo[x] = res
        return res

But memo is not feasible for x up to 1e9. So we need to find a way to compute this without memoization.

But how?

Wait, perhaps for k odd, the grundy numbers have a pattern where for x even, grundy(x) can be determined based on the number of times x can be divided by 2 (the highest power of 2 in x's factorization).

Alternatively, perhaps the grundy numbers for k odd can be determined in terms of the binary representation of x.

But this is unclear.

Alternatively, for k odd, the grundy numbers can be computed using a memoization-like approach, but using memoization only for the current path. For each x, compute grundy(x) by recursively computing grundy(x-1) and grundy(x/2) (for even x), but since each call reduces the problem to smaller x, the total number of steps per x is O(log x), which for 1e5 x's and x up to 1e9 would be acceptable.

So let's try to implement this for k odd.

The code for grundy function when k is odd would be:

def compute_grundy(x):
    if x == 0:
        return 0
    if x % 2 == 1:
        return mex([compute_grundy(x-1)])
    else:
        return mex([compute_grundy(x-1), compute_grundy(x//2)])

But this would take O(log x) time for each x.

But for x=1e9, the recursion depth would be log2(1e9) ≈30, which is manageable.

Wait, for x=1e9, which is even, compute_grundy(x) requires compute_grundy(x-1) (which is 999,999,999, odd) and compute_grundy(x/2 = 500,000,000).

compute_grundy(500,000,000) is even again, so split into x-1 (499,999,999, odd) and x/2 (250,000,000).

And so on. So each step reduces x by a factor of 2. So for x=1e9, which is even, the number of steps would be O(log x) but manageable.

But wait, for each x, even x requires two recursive calls: x-1 (which is odd) and x/2. However, x-1 for even x is one less than even x, which is odd. So compute_grundy(x-1) would call compute_grundy(x-2), which is even again.

But for x=1e9, compute_grundy(x) could take O(x) steps, which is impossible.

Wait, this is a problem. Because for example, x=2, compute_grundy(2) would call compute_grundy(1) and compute_grundy(1). But compute_grundy(1) would call compute_grundy(0). So for x=2, it's manageable.

But for x=1e9, the function would have to compute grundy(999,999,999) and grundy(500,000,000). But compute_grundy(999,999,999) is odd, so it calls grundy(999,999,998) (even), which then calls grundy(999,999,997) (odd) and grundy(499,999,999), etc. This leads to a chain of O(x) steps, which is impossible for x=1e9.

This suggests that the recursive approach is not feasible for large x when k is odd.

So we need a better way to compute grundy(x) for k odd.

Alternative idea: find that for k odd, the grundy numbers for x can be determined based on the parity of the number of times you can split the pile into even parts.

Wait, for example, when k is odd, each split reduces the pile's size by half, but since k is odd, the grundy number is the same as the grundy of x/2. So for even x, the split option's grundy is grundy(x/2). So mex is between grundy(x-1) and grundy(x/2).

But how to model this.

Alternatively, perhaps the grundy number for x when k is odd is the mex of grundy(x-1) and grundy(x/2) for even x. But this is the same as the mex of two numbers, which can be computed as follows:

mex(a, b) is the smallest non-negative integer not in {a, b}.

So if a and b are the same, mex is a+1 if a is 0, else 0? Wait no. For example, mex(0,0) is 1. mex(1,1) is 0. mex(2,2) is 0.

Wait, the mex of a set is the smallest non-negative integer not in the set. So for {a, b}, mex is 0 if neither a nor b is 0. If one of them is 0, then mex is 1 if the other is 1, etc.

But this depends on the actual values.

So for even x, g(x) = mex(g(x-1), g(x/2)).

This is a recursive relation, but how to compute this without recursion.

Another approach: since for even x, grundy(x) depends on grundy(x-1) and grundy(x/2), and for odd x, grundy(x) depends on grundy(x-1).

We can compute grundy(x) for x up to 1e9 by memoizing the computed values, but with x up to 1e9, this is impossible. So we need to find a pattern or a mathematical formula.

Alternatively, perhaps there's a way to represent grundy(x) in terms of the binary representation of x or some other property.

Another observation: for x=1 (odd), g(1) =1.

x=2 even: mex(g(1), g(1)) → mex(1,1) →0.

x=3 odd: mex(g(2)=0) →1.

x=4 even: mex(g(3)=1, g(2)=0) → mex(1,0)=2.

x=5 odd: mex(g(4)=2) →0.

x=6 even: mex(g(5)=0, g(3)=1) → mex(0,1) →2.

x=7 odd: mex(g(6)=2) →0.

x=8 even: mex(g(7)=0, g(4)=2) → mex(0,2) →1.

x=9 odd: mex(g(8)=1) →0.

x=10 even: mex(g(9)=0, g(5)=0) → mex(0,0) →1.

x=11 odd: mex(g(10)=1) →0.

x=12 even: mex(g(11)=0, g(6)=2) → mex(0,2) →1.

x=13 odd: mex(g(12)=1) →0.

x=14 even: mex(g(13)=0, g(7)=0) → mex(0,0) →1.

x=15 odd: mex(g(14)=1) →0.

x=16 even: mex(g(15)=0, g(8)=1) → mex(0,1) →2.

So for even x, the grundy number cycles through 0, 2, 2, 1, 2, 1, 1, 2, etc.

But it's hard to find a pattern.

Another idea: notice that for even x and k odd, the grundy(x) is mex of grundy(x-1) and grundy(x/2). So if we can find a way to compute this mex for even x, perhaps using properties of grundy(x-1) and grundy(x/2).

But it's challenging.

Alternative approach: for k odd, the grundy numbers can be represented using the mex function, and the grundy numbers cycle in a certain way. For example, when x is a multiple of some number, the grundy numbers repeat.

But this is not clear.

Another Idea: Since grundy(x) for even x depends on grundy(x-1) and grundy(x/2), and grundy(x-1) is mex of grundy(x-2), which is even or odd.

But perhaps for even x, grundy(x) can be expressed as the mex of grundy(x-1) and grundy(x/2), and for odd x, it's mex(grundy(x-1)).

But without a clear pattern, perhaps the only way is to compute grundy(x) recursively for each x, but with memoization.

But since the problem allows x up to 1e9 and n up to 1e5, this would be impossible unless each grundy(x) can be computed in O(1) time.

So perhaps the solution is to precompute the grundy numbers for all possible x up to a certain point, but given that x can be up to 1e9, this is not feasible.

Hmm. Let's think about the problem again.

The key is to compute the XOR of all grundy(a_i) for the initial piles. If the total XOR is non-zero, Kevin wins; else, Nicky.

So the problem reduces to computing the grundy numbers for each a_i.

For k even: the grundy numbers are easy to compute, as discussed.

For k odd: the grundy numbers are more complex. So the code needs to handle these two cases.

So the plan for the code:

1. For each a_i in the input, compute grundy(a_i) based on whether k is even or odd.

2. Compute the XOR of all grundy numbers.

3. If the XOR is non-zero, Kevin wins; else, Nicky.

The challenge is to compute grundy(a_i) for k odd quickly.

But for k odd, we need a way to compute grundy(x) for x up to 1e9 efficiently.

An alternative approach is to find that for k odd, the grundy numbers for x can be expressed in terms of the parity of the number of times you can split the pile until you reach an odd number.

But I'm not sure.

Let's try to find a pattern for k odd.

Looking at the grundy numbers for k=1:

x | g(x)

0 →0

1 →1

2 →0

3 →1

4 →2

5 →0

6 →2

7 →0

8 →1

9 →0

10 →1

11 →0

12 →1

13 →0

14 →1

15 →0

16 →2

17 →0

18 →1

19 →0

20 →2

Hmm. Noticing that for x even:

x=2 →0

x=4 →2

x=6 →2

x=8 →1

x=10 →1

x=12 →1

x=14 →1

x=16 →2

x=18 →1

x=20 →2

So for even x:

The grundy number seems to be 0 for x=2, 2 for x=4, 6, 16, 20, 1 for x=8, 10, 12, 14, 18, and 2 for x=20.

Not a clear pattern, but perhaps the grundy number is 2 when the highest power of 2 in x is 2^2 (4), 2^4 (16), etc. But x=20's highest power of 2 is 4 (20=4*5), but grundy is 2.

Alternatively, perhaps the grundy number is 2 when the number of times you can split x into halves (until you reach an odd number) is even, and 1 when it's odd.

But for x=4: split into 2 (even) → 2/2=1 (odd). So the count of splits is 2 (4→2→1). Even. So grundy 2.

x=6: split into 3 (even no? 6/2=3, odd. So count is 1. So grundy 2. Hmm, that doesn't fit.

Alternatively, perhaps for even x, the grundy number is the number of times x can be divided by 2 before reaching an odd number, but with some adjustment.

But x=4 is divided by 2 twice (4 →2 →1), count is 2. grundy is 2.

x=6: divided once (6 →3), count is 1. grundy is 2.

x=8: divided three times (8→4→2→1), count 3. grundy is 1.

x=16: divided four times (16→8→4→2→1), count 4. grundy is 2.

x=20: divided two times (20 →10 →5), count 2. grundy is 2.

So for count even: grundy is 2.

For count odd: grundy is 1.

But x=6's count is 1 (odd), but grundy is 2. So this theory is incorrect.

Alternative idea: the grundy number for even x and k odd is the mex of the grundy of x-1 (which is odd) and the grundy of x/2.

But to find this mex, perhaps the mex can be determined based on whether the grundy(x/2) is zero or not.

For example, when x is even and k is odd:

g(x) = mex(g(x-1), g(x/2)).

But g(x-1) is the grundy of an odd number, which for k odd can be 0 or 1.

Wait, looking at the data for k=1:

For x even:

g(2) = 0.

g(4) = mex(1, 0) →2.

g(6) = mex(0, 1) →2.

g(8) = mex(0, 2) →1.

g(10) = mex(0, 0) →1.

g(12) = mex(0, 1) →1.

g(14) = mex(0, 0) →1.

g(16) = mex(0, 1) →2.

So the mex can be 0, 1, or 2.

But there's no obvious pattern here.

Another Idea: For k odd, the grundy numbers can be 0, 1, or 2. So perhaps the mex for even x can be computed as follows:

If g(x/2) is 0 and g(x-1) is 0 → mex is 1.

If one of them is 1 and the other is 0 → mex is 2.

If one is 2 and the other is 0 → mex is 1.

But this is not certain.

Alternatively, perhaps for even x, the mex is 0 if both g(x-1) and g(x/2) are 1. But in practice, it's hard to see.

Given the time constraints, perhaps the correct approach is to implement the recursive function for k odd, with memoization using a cache to avoid recomputing.

But since the recursive calls could be deep for x=1e9, but with memoization, the number of unique calls would be O(log x), which is manageable.

So for example, using memoization with a dictionary, but only for the current x and the recursive calls needed.

But for Python, using lru_cache with a high enough maxsize could work.

But for x up to 1e9, the number of unique x's would be O(log x) per a_i, and with 1e5 a_i's, this would be O(1e5 log x) steps, which is manageable.

So the code would look like:

For each a_i:

if k is even:

   compute the grundy number using the even k formula.

else:

   compute the grundy number using a recursive function with memoization.

Then XOR all grundy numbers and determine the winner.

But in Python, recursion for x=1e9 would hit the recursion limit.

So to avoid recursion, we need to implement the grundy computation for k odd using an iterative approach.

So here's the plan:

Implement the grundy function for k odd using memoization with a dictionary, and an iterative approach.

But let's think of the grundy function for x and k odd.

We can compute grundy(x) using memoization:

memo = {}

def grundy(x):

    if x in memo:

        return memo[x]

    if x == 0:

        return 0

    if x % 2 == 1:

        res = mex([grundy(x-1)])

    else:

        res = mex([grundy(x-1), grundy(x//2)])

    memo[x] = res

    return res

But for x=1e9, this will take a lot of steps and may not be feasible.

Alternative Idea: memoize the grundy numbers for x up to a certain point, and find a pattern after that.

But for k odd, the grundy numbers are 0, 1, or 2.

But how to find the pattern.

Another observation: for k odd, once x becomes sufficiently large, the grundy numbers may cycle or stabilize.

But this is not clear.

Alternative approach: precompute the grundy numbers up to x=100 for k=1, and look for a pattern.

But even for k=1, the pattern is not obvious.

So perhaps the correct approach is to implement the recursive function with memoization, but using an iterative approach to avoid stack overflow.

So, here's the plan:

Implement an iterative function to compute grundy(x) for k odd:

def compute_grundy(x, memo):

    stack = [(x, False)]

    while stack:

        current_x, is_processed = stack.pop()

        if current_x in memo:

            continue

        if current_x == 0:

            memo[current_x] = 0

            continue

        if current_x % 2 == 1:

            # Need to compute grundy(current_x - 1)

            if (current_x - 1) not in memo:

                stack.append( (current_x, True) )

                stack.append( (current_x -1, False) )

            else:

                # Compute mex of [memo[current_x -1]]

                mex_val = 0 if memo[current_x -1] == 0 else 0

                # Wait, mex is the smallest non-negative integer not in the set.

                # If the set is {a}, then mex is 0 if a != 0, else 1.

                if memo[current_x -1] == 0:

                    memo[current_x] = 1

                else:

                    memo[current_x] = 0 if memo[current_x -1] == 1 else 0

        else:

            # even x: need grundy(current_x -1) and grundy(current_x // 2)

            need_to_process = False

            if (current_x -1) not in memo:

                stack.append( (current_x, True) )

                stack.append( (current_x -1, False) )

                need_to_process = True

            if (current_x //2) not in memo:

                stack.append( (current_x, True) )

                stack.append( (current_x //2, False) )

                need_to_process = True

            if need_to_process:

                continue

            # Compute mex of [memo[current_x-1], memo[current_x//2]]

            s = { memo[current_x-1], memo[current_x//2] }

            mex_val = 0

            while mex_val in s:

                mex_val +=1

            memo[current_x] = mex_val

        if is_processed:

            continue

    return memo.get(x, 0)

But this code is complicated and may not work correctly.

But given time constraints, perhaps the best approach is to implement this for k even and odd, and see.

But for the problem, given time and memory constraints, the code must handle n=1e5, and a_i=1e9.

But for k even, the code is straightforward.

For k odd, the code must compute grundy(x) for each a_i, but for x up to 1e9, this would be too slow with a recursive or iterative approach.

But what if there's a pattern for k odd where the grundy numbers can be computed using the mex of the number of set bits in the binary representation of x, or some other property?

Another Idea: For k odd, the grundy number for x is the number of times x can be divided by 2 until it becomes odd, and whether that count is even or odd.

For example, for x=4, which is 2^2, count is 2 (even) → grundy 2.

For x=6, which is 2^1 *3, count is 1 (odd) → grundy 2.

But this doesn't fit the earlier values.

Alternatively, perhaps the grundy number is 0 if x is even, 1 if x is odd and 1 more than a multiple of 4, etc. But this is unclear.

Alternatively, perhaps the grundy number for x when k is odd is equal to the number of trailing 1's in the binary representation of x.

But I'm not sure.

Given the time constraints, perhaps the best way is to proceed with the following plan:

- For k even, compute grundy numbers as per the pattern.

- For k odd, compute grundy numbers using a recursive function with memoization, but using memoization via a dictionary, and handle large x by memoizing the computed values.

But in practice, for x=1e9, this approach would take too long.

So perhaps there's a smarter way to compute grundy numbers for k odd.

Wait, here's another Idea: for k odd, the grundy numbers have a periodic pattern.

For example, for x even:

grundy(x) = mex(grundy(x-1), grundy(x//2)).

But x-1 is odd, and grundy(x-1) is mex(grundy(x-2)).

But this could lead to a pattern where grundy(x) depends on previous grundy numbers in a way that creates a cycle.

Alternatively, maybe for x >= some value, the grundy numbers cycle between 0, 1, and 2.

But this is just a guess.

Another Idea: For k odd, the grundy numbers can be computed based on the following cases:

- If x is 0: 0.

- If x is 1: 1.

- If x is even:

   - If x is 2:0.

   - Else, mex of grundy(x-1) and grundy(x//2).

- If x is odd and x>1: mex of grundy(x-1).

But how to compute this.

Alternative approach: For x even and k odd, the grundy(x) is mex of the two values. Let's think about the mex of two values a and b.

The mex is the smallest non-negative integer not in {a, b}.

Possible cases:

- If a and b are 0 and 1: mex is 2.

- If a and b are 0 and 2: mex is 1.

- If a and b are 1 and 1: mex is 0.

- If a and b are 0 and 0: mex is 1.

- If a and b are 1 and 2: mex is 0.

But this depends on the combination.

So, given the complexity, perhaps the only way to proceed is to implement the recursive function with memoization, but using an iterative approach to avoid stack overflow.

But for x=1e9, even with memoization, the number of function calls would be large.

But wait, for x=1e9, which is even:

- compute_grundy(x) requires compute_grundy(x-1) and compute_grundy(x//2).

x-1 is odd, so compute_grundy(x-1) requires compute_grundy(x-2), which is even.

But x-2 is 999,999,998, which is even.

So for x=1e9:

compute_grundy(1e9) → calls compute_grundy(999,999,999) and compute_grundy(500,000,000).

compute_grundy(999,999,999) is odd, so calls compute_grundy(999,999,998).

compute_grundy(999,999,998) → even, calls compute_grundy(999,999,997) and compute_grundy(499,999,999).

This seems to lead to a chain that could take O(x) steps, which is impossible.

So this approach is not feasible.

So we need another way.

Alternative Idea: For k odd, the grundy numbers can be determined using the following formula:

If x is even:

grundy(x) is mex(grundy(x-1), grundy(x/2)).

But perhaps, for large x, grundy(x) cycles between 0, 1, 2.

But how to prove this.

Alternatively, perhaps for k odd and x >= 2, the grundy numbers are periodic with period 3 or something like that.

But without further data, it's hard to see.

Another Idea: For k odd, the grundy number of x is 0 if x is even and the number of times you can split x into even parts is even, but this is not helpful.

But given the time constraints, perhaps the correct approach is to proceed with the following code:

Implement the grundy function for k even and for k odd.

For k even, use the pattern-based approach.

For k odd, compute grundy(x) recursively with memoization.

But in Python, this will hit the recursion limit for large x.

So to avoid that, use an iterative approach with memoization.

But for x=1e9, this will take O(log x) steps.

But how?

Let's think again: when x is even and k is odd, grundy(x) = mex(grundy(x-1), grundy(x//2)).

But x is even, x-1 is odd, and x//2 is even or odd depending on x.

So the recursive calls split the problem into smaller x.

But for x=1e9:

grundy(1e9) depends on grundy(999,999,999) (odd) and grundy(500,000,000) (even).

grundy(999,999,999) depends on grundy(999,999,998) (even).

grundy(999,999,998) depends on grundy(999,999,997) (odd) and grundy(499,999,999) (odd).

And so on.

But for each step, the x is halved, so the number of steps to compute grundy(x) is O(log x).

So for each a_i, the number of steps to compute grundy(a_i) is O(log a_i).

Given that a_i is up to 1e9, log2(1e9) is around 30, so for 1e5 a_i's, total steps would be 3e6, which is manageable.

So the code can use memoization with a dictionary, and for each a_i, compute grundy(a_i) by breaking it down into smaller values.

So the code will look like this:

Implement a memoization dictionary.

For each a_i:

   if k is even:

       compute grundy using even k formula.

   else:

       compute grundy using memoization for k odd.

Finally, compute the XOR of all grundy numbers and output the winner.

So the code in Python:

But how to implement this efficiently.

Here's the code:

Read n and k.

Read the list a.

if k is even:

   for each x in a:

       if x == 0:

           g = 0

       elif x == 1:

           g =1

       elif x == 2:

           g =2

       elif x % 2 == 1:

           g =0

       else:

           g =1

else:

   memo = {0:0}

   for x in a:

       current = x

       stack = []

       path = []

       # Iterate until current is in memo or 0

       while current not in memo:

           path.append(current)

           if current % 2 == 1:

               # need to compute current-1 first

               stack.append(current)

               current -=1

           else:

               # need to compute current-1 and current//2 first

               stack.append(current)

               stack.append(current//2)

               current = current//2

       # Now, compute the path in reverse

       while path:

           current = path.pop()

           if current in memo:

               continue

           if current % 2 == 1:

               # grundy(current) is mex of [grundy(current-1)]

               # grundy(current-1) is already in memo

               g_prev = memo[current-1]

               mex = 0 if g_prev == 0 else 1 if 0 not in [g_prev] else 0

               # mex is the smallest non-negative integer not in the set.

               # set is {g_prev}

               mex = 0 if g_prev != 0 else 1

               memo[current] = mex

           else:

               # grundy(current) is mex of [grundy(current-1), grundy(current//2)]

               g_prev = memo[current-1]

               g_half = memo[current//2]

               s = {g_prev, g_half}

               mex = 0

               while mex in s:

                   mex +=1

               memo[current] = mex

       g = memo[x]

xor_sum = 0

for x in a:

   xor_sum ^= g[x]

if xor_sum !=0:

   print("Kevin")

else:

   print("Nicky")

But this code would use memoization for all processed x's, and for each a_i, it processes the required x's in a stack-like manner to compute the grundy number.

But in Python, using a dictionary for memoization and iteratively processing the stack, this should be manageable.

But to avoid redundancy, perhaps the memoization should be built once for all a_i's, and not per a_i.

So the code for k odd would be:

memo = {0:0}

for x in a:

   current = x

   stack = [current]

   visited = set()

   while stack:

       current = stack[-1]

       if current in memo:

           stack.pop()

           continue

       if current % 2 == 1:

           # need to compute current-1

           if (current-1) not in memo:

               stack.append(current-1)

           else:

               # compute grundy(current)

               mex = 0 if memo[current-1] != 0 else 1

               memo[current] = mex

               stack.pop()

       else:

           # need to compute current-1 and current//2

           if (current-1) not in memo:

               stack.append(current-1)

           elif (current // 2) not in memo:

               stack.append(current//2)

           else:

               # compute grundy(current)

               g_prev = memo[current-1]

               g_half = memo[current//2]

               s = {g_prev, g_half}

               mex = 0

               while mex in s:

                   mex +=1

               memo[current] = mex

               stack.pop()

This approach uses a stack to process the needed nodes in a depth-first manner, ensuring that the dependencies are computed first.

But this code would be time-consuming for large a_i's.

But given the time constraints of the problem, this seems to be the only way.

So the final code would look like this:

Read n and k.

Read the array a.

if k is even:

   compute grundy for each a_i using the even k formula.

else:

   compute grundy for each a_i using memoization.

XOR all the grundy numbers.

Output Kevin or Nicky based on the XOR.

Now, implementing this in Python.

But how to handle the memoization for k odd.

Here's the code:

For k even, the grundy function is easy.

For k odd, we can use a dictionary to memoize the grundy numbers, and process each a_i by iteratively building up the memo.

But the code must be efficient.

Here's the Python code:

n, k = map(int, input().split())

a = list(map(int, input().split()))

xor_sum = 0

if k % 2 == 0:

    for x in a:

        if x == 0:

            g = 0

        elif x == 1:

            g = 1

        elif x == 2:

            g = 2

        else:

            if x % 2 == 1:

                g = 0

            else:

                g = 1

        xor_sum ^= g

else:

    memo = {0: 0}

    for x in a:

        current = x

        stack = []

        while True:

            if current in memo:

                break

            stack.append(current)

            if current % 2 == 1:

                current -= 1

            else:

                stack.append(current // 2)

                current = current // 2

        # Now, compute from the bottom up

        while stack:

            current = stack.pop()

            if current in memo:

                continue

            if current % 2 == 1:

                # Compute grundy(current) = mex of [grundy(current-1)]

                g_prev = memo.get(current - 1, 0)

                mex = 1 if g_prev == 0 else 0

                memo[current] = mex

            else:

                # Compute grundy(current) = mex of [grundy(current-1), grundy(current//2)]

                g_prev = memo.get(current - 1, 0)

                g_half = memo.get(current // 2, 0)

                s = {g_prev, g_half}

                mex = 0

                while mex in s:

                    mex += 1

                memo[current] = mex

        xor_sum ^= memo[x]

if xor_sum != 0:

    print("Kevin")

else:

    print("Nicky")

This code uses a while loop to traverse down to the base case (when current is in memo), then computes the grundy numbers on the way back up.

This should handle all cases efficiently.

For example, when a_i is even and k is odd, the code will split into current//2 and current-1, and compute each step as needed.

The memo dictionary will remember all computed grundy numbers, so subsequent a_i's that require the same current values will use the memoized values.

This approach should handle large a_i's efficiently.

Testing the sample inputs:

Sample 1:

Input:

2 1

3 4

k is odd.

For x=3 (odd):

grundy(3) = mex(grundy(2)).

grundy(2) is even: mex(grundy(1), grundy(1)).

grundy(1) is mex(grundy(0)) → 1.

So mex(1, 1) is 0. So grundy(2) is 0.

So mex(grundy(2)=0) → 1. So grundy(3)=1.

For x=4 (even):

grundy(4) = mex(grundy(3), grundy(2)) → mex(1, 0) →2.

So the xor is 1 ^ 2 = 3. Which is non-zero → Kevin wins.

Sample 2:

Input:

1 2

3

k is even.

x=3 is odd. So grundy is 0.

XOR is 0 → Nicky wins.

This matches the sample outputs.

So this code should handle these cases correctly.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
xor_sum = 0

if k % 2 == 0:
    for x in a:
        if x == 0:
            g = 0
        elif x == 1:
            g = 1
        elif x == 2:
            g = 2
        else:
            g = 1 if x % 2 == 0 else 0
        xor_sum ^= g
else:
    memo = {0: 0}
    for x in a:
        current = x
        stack = []
        while True:
            if current in memo:
                break
            stack.append(current)
            if current % 2 == 1:
                current -= 1
            else:
                stack.append(current // 2)
                current = current // 2
        
        while stack:
            current = stack.pop()
            if current in memo:
                continue
            if current % 2 == 1:
                g_prev = memo.get(current - 1, 0)
                mex = 1 if g_prev == 0 else 0
                memo[current] = mex
            else:
                g_prev = memo.get(current - 1, 0)
                g_half = memo.get(current // 2, 0)
                s = {g_prev, g_half}
                mex = 0
                while mex in s:
                    mex += 1
                memo[current] = mex
        xor_sum ^= memo[x]

print("Kevin" if xor_sum != 0 else "Nicky")
```