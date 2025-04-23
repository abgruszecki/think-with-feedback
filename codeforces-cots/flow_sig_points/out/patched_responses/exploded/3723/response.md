<think>
Okay, let's try to solve this problem. So the problem is about finding the minimal number of moves to make exactly half of the piles perfect squares (for Ann) and the other half not (for Borya). The moves allowed are adding or removing one candy at a time from a pile.

First, I need to understand for each pile what's the cost to make it a square or not a square. Then, decide which piles should be converted into squares and which into non-squares, such that the total cost is minimized.

Let's break it down. For each pile, compute two values: the minimal steps required to turn it into a square (if it's not already), and the minimal steps required to turn it into a non-square (if it's a square). Wait, but if a pile is already a square, then for Borya's part (non-squares), we have to change it. Similarly, if a pile is a non-square, for Ann's part (squares), we need to change it.

So first, for each pile, determine whether it's a perfect square. Then, for each pile, calculate two values:

1. The cost to make it a square (if it's not already). For example, if the current number is 12, find the nearest square (9 or 16) and compute the minimal steps. For 12, the closest square is 9 (3 steps down) or 16 (4 steps up). So minimal is 3 steps. But wait, maybe the minimal steps is the minimal steps to reach any square, not just the closest. Because sometimes the closest might not be the minimal steps. Wait, no, the minimal steps would be the minimal difference between the current number and a square. So yes, the closest square gives the minimal steps.

Wait, let's think. For a given number x, the minimal steps to turn it into a square is the minimal of |x - s| where s is a perfect square. So we need to find the nearest square below or above x.

But how do we compute that efficiently? For example, for x, the square root is sqrt(x), which could be an integer or not. So for x, the nearest squares are floor(sqrt(x))² and ceil(sqrt(x))². Then the minimal steps would be min(x - floor², ceil² - x).

But wait, if x is a perfect square, then the cost is zero. So for each a_i, we can compute the minimal steps to make it a square (cost_square) and the minimal steps to make it a non-square (cost_non_square). However, if the original number is a square, then cost_non_square is the minimal steps to reach the nearest non-square. How?

Wait, for a pile that is already a square (say s²), how do we make it a non-square with minimal steps? Because adding or removing 1 would take us to s² ± 1. But s² ±1 is not a square. Because s² +1 is between s² and (s+1)^2 (s² + 2s +1). So adding 1 would make it s²+1, which is not a square. So the minimal steps here is 1. Similarly, subtracting 1 (if possible) would take s² to s²-1. But again, (s-1)^2 is (s² - 2s +1). So s²-1 is between (s-1)^2 and s². So s²-1 is not a square. So the minimal steps for a square to become non-square is 1. Except when s² is zero. Because if x is zero, then subtracting 1 isn't possible. So for x=0, the only option is to add 1 (cost 1), which makes it 1, which is a square. Wait, that's a problem. Wait, no. Wait, if the original x is zero (a square), to make it a non-square, we need to change it to a number that's not a square. So zero is a square. So adding 1 would make it 1, which is a square. That's not allowed. So we have to add 2 steps to make it 2 (non-square). Or subtract 1 is not possible (since x is zero). So the minimal steps here would be 2. Wait, that's an edge case.

So, for a square number x, the cost_non_square depends on x:

If x is 0: then the next non-square is 1 (but that's a square). So we need to go to 2. So steps are 2 (add 2).

If x is 1: subtract 1 (if possible) would take to 0, which is a square. So we can't. So add 1 to make 2 (steps 1).

Wait, let's think again. For a square x, the minimal steps to make it non-square.

Case 1: x is 0. Then the minimal steps would be 2 (add 2 to get 2, which is not a square). Because adding 1 gives 1 (a square). So for x=0, the cost_non_square is 2.

Case 2: x is 1. Adding 1 gives 2 (non-square) → cost 1. Subtracting 1 gives 0 (square) → not allowed. So cost is 1.

Case 3: x is 4 (s=2). Adding 1 →5 (non-square) → cost 1. Subtracting 1 →3 (non-square) → cost 1. So cost is 1.

So in general, for squares, the minimal steps to turn into non-squares is 1, except for x=0, which requires 2 steps.

So, for each a_i, we need to compute:

- cost_square: 0 if it's already a square, else the minimal steps to reach the nearest square.

- cost_non_square: if it's not a square, then 0. If it's a square, then 1 (unless x is 0, then 2).

Once we have these two costs for each pile, the problem reduces to selecting exactly k = n/2 piles to be squares (and the rest to be non-squares). But wait, the problem requires exactly n/2 to be squares and the other half non-squares. So for each pile, if we choose to assign it to be a square, we pay cost_square. If assigned to non-square, we pay cost_non_square.

But how do we select which piles to assign to which category to minimize the total cost, with exactly k squares and (n -k) non-squares.

So the approach is:

1. For each pile, compute cost_square and cost_non_square.

2. Then, select exactly k piles to be squares (paying their cost_square) and the remaining n-k to be non-squares (paying their cost_non_square). The total is sum of the selected costs.

We need to choose this selection such that the total is minimized.

But how do we do this efficiently?

Let's think of all the piles. For each, we can see the difference between cost_non_square and cost_square. Because when we choose whether to assign a pile to square or non-square, the cost difference may influence the selection.

Wait, but perhaps we can model this as a problem where we have to pick exactly k piles to be squares, and the rest as non-squares. The total cost is sum of (selected squares' cost_square) + sum of (selected non-squares' cost_non_square).

So the goal is to choose exactly k squares such that the sum is minimized.

An alternative approach: for each pile, if we decide to assign it to be a square, the cost is cost_square. If assigned to non-square, the cost is cost_non_square. We need to choose exactly k squares, and the rest non-squares. The total cost is the sum of all chosen assignments.

So how to select k piles with the minimal sum of (cost_square) and the rest (n-k) with (cost_non_square).

But the problem is to choose which ones to assign as squares such that the total is minimized.

So perhaps, for each pile, the "gain" of choosing it as a square instead of a non-square is (cost_non_square - cost_square). Because if I select this pile as a square, instead of non-square, the cost is reduced by (cost_non_square - cost_square).

Wait, no. Let's think: if the pile is assigned as a square, the cost is cost_square. If it's assigned as non-square, cost is cost_non_square. The difference between the two is (cost_square - cost_non_square). So if this is negative, assigning it as a square is better.

But in our selection, we need to choose exactly k squares. So the strategy is to pick the piles where (cost_square - cost_non_square) is minimized. Because if (cost_square - cost_non_square) is negative, then the cost is lower when we assign it as a square. So selecting such piles as squares gives us a lower total cost.

Wait, maybe another way: For each pile, the cost if we choose to make it a square is cost_square, and the cost if we don't is cost_non_square. So the total cost is sum of (for all piles, either cost_square or cost_non_square). We need exactly k piles to be cost_square, and the rest to be cost_non_square. We need to pick the k piles where (cost_square - cost_non_square) is the smallest. Because by selecting these, the total sum would be the sum of all cost_non_square for all piles, plus the sum of (cost_square - cost_non_square) for the selected k piles. So to minimize the total sum, we want to select the k piles with the smallest (cost_square - cost_non_square) values. Because adding a lower value (which could be negative) would reduce the sum.

Wait, that makes sense. Because the sum of all cost_non_square is a base. Then, for each pile selected as square, the delta is (cost_square - cost_non_square). So if we add that delta, the total sum would be sum_non_square + sum_deltas. So to minimize the total sum, we want the sum_deltas to be as small as possible. Since we need to select exactly k deltas, we should pick the k smallest (cost_square - cost_non_square) values.

So the steps would be:

1. For each pile, compute cost_square and cost_non_square.

2. Compute the difference (cost_square - cost_non_square) for each pile.

3. Select the k piles with the smallest differences. Sum their (cost_square) and sum the rest's cost_non_square.

But wait, how to compute this?

Alternatively, the total cost is sum of (for each pile, cost_square if selected, else cost_non_square). So that's equal to sum(cost_non_square for all) + sum( (cost_square - cost_non_square) for selected piles).

So, the minimal total cost is sum_non_square_total + sum of the k smallest (cost_square - cost_non_square) differences.

So the algorithm would be:

- Calculate for each pile the cost_square and cost_non_square.

- Calculate sum_non_square_total = sum of cost_non_square for all piles.

- Calculate the list of differences (cost_square - cost_non_square) for each pile.

- Sort these differences, take the first k (smallest) ones, sum them.

- Add this sum to sum_non_square_total to get the total cost.

So the key is to choose k piles where choosing them as squares gives the least possible increase (or maximum possible decrease) in the sum compared to if all were non-squares.

But this works only if the sum of k smallest differences (cost_square - cost_non_square) is as small as possible.

Yes. For example, if a pile has cost_square = 3 and cost_non_square = 5, then the difference is -2. Selecting this pile as a square would reduce the total sum by 2. So including such a pile in the selected k is beneficial.

So the steps are:

Compute for each pile the two costs.

Compute the differences.

Sort the differences in ascending order.

Take the first k differences (smallest ones), sum them.

Add to sum_non_square_total.

This gives the minimal possible total cost.

So the main steps are:

1. Determine for each a_i whether it is a square.

2. Compute cost_square and cost_non_square for each a_i.

3. Compute the differences and sum the cost_non_square for all.

4. Sort the differences, take the first k and sum.

5. The result is sum_non_square_total + sum_of_k_smallest_differences.

Now, the problem reduces to efficiently computing these values.

Now, let's think about how to compute whether a number is a perfect square.

For a given a_i, compute the integer square root. Then check if the square of that integer is equal to a_i. For example, in Python, we can compute s = int(math.isqrt(a_i)), then check s*s == a_i. But we need to handle zero correctly.

Wait, math.isqrt in Python returns the integer square root, which is the floor of the exact square root. So for example, math.isqrt(16) is 4, which squared is 16. For 15, math.isqrt(15) is 3, 3*3=9 <15. So yes, the correct approach is to compute s = math.isqrt(x), and check if s*s == x.

So for x in a_i, we can compute is_square = (s*s == x) where s = math.isqrt(x).

Once we have is_square for each a_i, compute cost_square and cost_non_square.

So for each x:

if is_square:

    cost_square = 0

    if x ==0:

        cost_non_square = 2

    else:

        cost_non_square =1

else:

    # compute cost_square: minimal steps to make it a square.

    s = math.isqrt(x)

    lower = s*s

    upper = (s+1)*(s+1)

    cost_down = x - lower

    cost_up = upper -x

    cost_square = min(cost_down, cost_up)

    cost_non_square =0

So that's how we compute the two costs.

Now, once all cost_square and cost_non_square are computed, the next step is to compute the sum of all cost_non_square and then the sum of the k smallest (cost_square - cost_non_square) where k = n//2.

But in the problem statement, n is even, so k is exactly n/2.

So the code outline is:

Read n.

Read the list a.

Compute for each x in a:

    is_square = check.

    compute cost_square and cost_non_square.

sum_non_square = sum of cost_non_square for all.

differences = [cost_square - cost_non_square for each x in a]

sort differences.

sum the first k elements of the sorted differences.

total = sum_non_square + sum_differences.

Now, this approach will work. Let's test it against the sample inputs.

Sample 1:

Input:

4

12 14 30 4

For each a_i:

12: is not a square. s=3 (3^2=9, 4^2=16. cost_down 12-9=3, cost_up 4. So cost_square=3. cost_non_square=0.

14: s=3. lower 9, upper 16. cost_down 14-9=5, cost_up 2. So cost_square=2. cost_non_square=0.

30: s=5, 5^2=25, 6^2=36. cost_down 30-25=5, cost_up 6. cost_square=5. cost_non_square=0.

4: is square (2^2=4). cost_square=0. cost_non_square=1 (since x is not zero). So for 4, cost_non_square is 1.

sum_non_square is 0 +0 +0 +1 =1.

differences for each:

12: 3 -0=3.

14:2-0=2.

30:5-0=5.

4:0-1= -1.

differences list: [3,2,5,-1]. sorted is [-1, 2,3,5]

k=2. sum the first two: -1 +2 =1.

sum_non_square (1) + sum (1) = 2. Which matches the sample output.

Sample 2:

Input:

6

0 0 0 0 0 0

Each x is 0, which is a square. So cost_square is 0. cost_non_square is 2.

sum_non_square =6 * 2=12.

differences are cost_square (0) - cost_non_square (2) = -2 for each.

k=3 (6/2=3). We need to select 3 piles as squares and 3 as non-squares. Wait, no. Wait, the problem requires exactly n/2 (3) squares and 3 non-squares. So in this case, each pile is a square. So to make 3 non-squares, each of those 3 must be converted. But for each of those 3, cost_non_square is 2. So sum_non_square_total is 3 *2 (since 3 are converted to non-squares) and 3 *0 (since they are squares). But according to the algorithm:

sum_non_square for all piles is 6*2=12.

differences for each: 0-2 =-2.

sorted differences: [-2, -2, -2, -2, -2, -2]. Take the first 3: sum is -2*3 =-6.

Total is 12 + (-6) =6. Which matches sample 2.

Sample 3:

Input:

6

120 110 23 34 25 45

Wait, 25 is a square (5^2=25). The others are not.

So for each:

120: not a square. compute nearest squares. s=10 (10^2=100, 11^2=121. cost_up 121-120=1. cost_down 20. So cost_square=1. cost_non_square=0.

110: s=10. 10^2=100, 11^2=121. cost_down 10, cost_up 11. So cost_square=10.

23: s=4. 16 vs 25. 23-16=7, 25-23=2 → cost_square=2.

34: s=5 (25 vs 36. 34-25=9, 36-34=2 → cost_square=2.

25: is square. cost_square=0. cost_non_square=1.

45: s=6 (36 vs 49. 45-36=9, 49-45=4 → cost_square=4.

So the cost_non_square for all except 25 is 0. For 25, it's 1.

sum_non_square is 1 (for 25) + 0*5 =1.

differences:

120: 1 -0 =1.

110:10-0=10.

23:2-0=2.

34:2-0=2.

25:0-1= -1.

45:4-0=4.

differences list: [1,10,2,2,-1,4]. sorted: [-1,1,2,2,4,10].

k=3 (6/2=3). sum first three: -1 +1 +2 =2.

total: 1 +2 =3. Which matches sample 3.

Sample 4:

Input:

10

121 56 78 81 45 100 1 0 54 78

We need to check which are squares:

121 (11^2 yes), 56 (no), 78 (no), 81 (9^2 yes), 45 (no), 100 (10^2 yes), 1 (1^2 yes), 0 (yes), 54 (no), 78 (no).

So n=10, so k=5.

Currently, there are 5 squares (121,81,100,1,0) and 5 non-squares. So the sum_non_square would be sum of cost_non_square for all. For the squares:

121's cost_non_square is 1 (since x !=0). 81's is 1. 100's is 1. 1's is 1. 0's is 2. Sum is 1+1+1+1+2=6. For the non-squares (56,78,45,54,78), their cost_non_square is 0. So sum_non_square_total is 6 + 0*5 =6.

But since k=5, we need to select 5 squares and 5 non-squares. Wait, but the current number of squares is 5, and non-squares is 5. So the cost is 0. So sample 4's output is 0.

In this case, the sum_non_square_total is 6 (since the squares have cost_non_square of 1,1,1,1,2). But according to the algorithm, the sum_non_square is sum of cost_non_square for all piles. But in this case, 5 of the piles are squares (so their cost_non_square is non-zero), and 5 are non-squares (cost_non_square is zero). So sum_non_square_total is 1+1+1+1+2 +0*5 =6.

But the sum of the differences would be (cost_square - cost_non_square) for each pile.

For the squares:

121: cost_square is 0. cost_non_square is 1. difference is 0-1 =-1.

81: same → 0-1=-1.

100: same →0-1=-1.

1: 0-1=-1.

0: cost_square is 0. cost_non_square is 2. difference is 0-2=-2.

For the non-squares:

56: cost_square is min(56 - 7^2=56-49=7, 8^2-56=64-56=8) →7. So difference is7 -0=7.

78: 8^2=64, 9^2=81. 78-64=14, 81-78=3 → cost_square is3. difference 3-0=3.

45: 6^2=36, 7^2=49. 45-36=9, 49-45=4 → cost_square is4. difference4-0=4.

54: 7^2=49, 8^2=64. 54-49=5, 64-54=10 →5. difference5-0=5.

78: same as the other 78 →3. difference3-0=3.

So the list of differences is:

For the squares: -1, -1, -1, -1, -2.

For the non-squares:7,3,4,5,3.

So the differences list is: [-1, -1, -1, -1, -2,7,3,4,5,3].

Sort this list: [-2, -1, -1, -1, -1,3,3,4,5,7].

We need to choose k=5 elements. Summing the first 5: -2 + (-1)*4 = -6. sum_non_square_total is6. So total would be 6 + (-6) =0. Which matches sample 4.

So the algorithm works for the samples.

Now, the problem is to code this efficiently, considering that n can be up to 2e5, which is manageable.

Now, let's think about possible edge cases.

Edge case 1: all piles are squares. n=2. Then k=1. So need to choose one to remain square (cost 0) and one to convert to non-square (cost 1 if x is not 0, 2 if x is 0). For example, input 2 4 9. Then, sum_non_square_total is 1 (for 4) +1 (for 9) =2. differences are (0-1) =-1 for 4, (0-1)=-1 for 9. sum of first 1 is -1. total is 2 -1 =1. So the minimal steps is 1.

Edge case where x=0. For example, input 2 0 0. So k=1. sum_non_square_total is 2+2=4. differences are (0-2)=-2 for each. take one of them. sum is -2. total is4-2=2. So the answer is 2. Which is correct: one zero remains (cost 0), the other becomes 2 (cost 2).

Another edge case: x=0. For example, n=2, input 0 0. The sum_non_square_total is 2+2=4. differences are -2 and -2. sum of 1 is -2. total is4-2=2. So the answer is 2. Which is correct: one is converted to 0 (square, cost 0) and the other to 2 (cost 2). Or, one is converted to 0 (cost 0) and the other to 2 (cost 2). So total is 2.

So code needs to handle x=0 correctly.

Now, let's code this.

In Python:

First, read n.

Then the list a.

For each element in a, compute is_square.

To compute is_square:

s = math.isqrt(x)

if s * s == x: then it's a square.

But for x=0, s is 0, and 0*0=0.

Then compute cost_square and cost_non_square.

Now, for code:

import math

n = int(input())
a = list(map(int, input().split()))

sum_non_square = 0
differences = []

for x in a:
    s = math.isqrt(x)
    is_square = (s * s == x)
    if is_square:
        # cost_square is 0
        # cost_non_square: 2 if x is 0, else 1
        if x ==0:
            cn = 2
        else:
            cn =1
        sum_non_square += cn
        # difference is 0 - cn
        differences.append(0 - cn)
    else:
        # compute cost_square: min between x - lower and upper -x
        lower = s * s
        upper = (s+1)*(s+1)
        cost_down = x - lower
        cost_up = upper - x
        cs = min(cost_down, cost_up)
        # cost_non_square is 0
        sum_non_square +=0
        # difference is cs -0
        differences.append(cs)

k = n //2

# sort differences and take first k
differences.sort()

sum_diff = sum(differences[:k])

total = sum_non_square + sum_diff

print(total)

This code should work.

Testing sample 2:

input 6 0 0 0 0 0 0.

Each x is 0. So is_square is true. cn is 2. sum_non_square is 6*2=12.

differences are 0-2=-2 for each.

sorted differences is six -2's. sum first 3: -6. total 12-6=6.

Sample 1:

sum_non_square is 1. differences are 3,2,5,-1. sorted -1,2,3,5. sum first 2: -1+2=1. 1+1=2.

Sample 4: sum_non_square is 6 (1+1+1+1+2). differences for squares: -1, -1, -1, -1, -2. For non-squares:7,3,4,5,3. So sorted list includes these, sum first 5 is -2-1*4= -6. sum 6-6=0.

All samples work.

Now, considering the time and memory constraints.

n can be up to 2e5. Sorting a list of 2e5 elements is O(n log n), which is acceptable for Python even with 2e5 elements. For 2e5, log2(2e5) is around 18. 2e5 *18 is 3.6e6 operations. Python can handle that.

Memory-wise, the differences list is O(n), which is acceptable.

So the code should pass all test cases.
</think>

```python
import math

n = int(input())
a = list(map(int, input().split()))

sum_non_square = 0
differences = []

for x in a:
    s = math.isqrt(x)
    if s * s == x:
        # It's a square, calculate cost to non-square
        if x == 0:
            cost_non = 2
        else:
            cost_non = 1
        sum_non_square += cost_non
        differences.append(-cost_non)
    else:
        # Not a square, calculate cost to square
        lower = s * s
        upper = (s + 1) ** 2
        cost_square = min(x - lower, upper - x)
        differences.append(cost_square)

k = n // 2
differences.sort()
total = sum_non_square + sum(differences[:k])

print(total)
```