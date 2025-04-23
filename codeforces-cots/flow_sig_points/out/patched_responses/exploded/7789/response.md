<think>
Okay, let's see. The problem is about placing electrons and protons on given points such that when they move to their respective axes, the maximum distance between any two points is minimized. And we need to output the square of that minimum possible diameter.

Hmm, the key is to decide for each point whether to make it an electron (moving to x-axis) or a proton (moving to y-axis) in a way that the maximum pairwise distance is as small as possible. The distance is measured as the Euclidean distance, but since we need the square of the maximum, maybe we can work with squared distances to avoid floating points.

Wait, the maximum distance squared is the same as the square of the maximum distance. So we can compute all squared distances and find the maximum, then minimize that.

So the problem reduces to choosing for each point (x_i, y_i) whether to take (x_i, 0) or (0, y_i) such that the maximum squared distance between any two chosen points is minimized.

The challenge is to find the optimal assignment of electrons and protons that gives the smallest possible maximum distance squared.

But with n up to 1e5, we need an algorithm that's O(n) or O(n log n), otherwise it's not feasible. For each point, there's a binary choice, which suggests that checking all possibilities is impossible (2^1e5 is way too big). So we need a clever way to model this.

Let me think about possible approaches.

First, for each point, we have two options. The optimal solution would involve selecting some points as electrons and others as protons such that the maximum pairwise distance is minimized.

But how to model this? The maximum distance can come from two points both being electrons, both being protons, or one of each.

Wait, but electrons are on the x-axis, protons on the y-axis. So the possible points after movement are all (x_i, 0) and (0, y_i) for each original point.

So the set of possible points after movement is a mix of points on x and y axes.

The maximum distance between any two points in the new set is the maximum of:

- The maximum distance between two x-axis points (which is the maximum |x_i - x_j|)
- The maximum distance between two y-axis points (which is the maximum |y_i - y_j|)
- The maximum distance between an x-axis point and a y-axis point (sqrt(x_i^2 + y_j^2) for each i,j where one is on x and the other on y)

But since we need to choose the assignments such that all these possibilities are considered, the problem is to split the points into two groups: those assigned to x (electrons) and those assigned to y (protons). Then compute the maximum of the three possibilities above, and find the split that minimizes this maximum.

But even if we split into X and Y groups, the maximum can come from the X group's max x difference, Y group's max y difference, or the maximum x in X and y in Y (sqrt(x^2 + y^2)).

Wait, but in terms of squared distances, the maximum would be the maximum of:

- (x_i - x_j)^2 (for two X points)
- (y_i - y_j)^2 (for two Y points)
- x_i^2 + y_j^2 (for an X point and a Y point)

So the problem is to choose for each point whether to take x_i or y_i (but not both) such that the maximum of the three terms above is minimized.

Hmm. How can we model this?

An alternative approach: Let's suppose we decide to have some points in X and others in Y. Then:

max_x is the maximum x in X minus the minimum x in X. The squared distance between the two farthest X points is (max_x_X - min_x_X)^2.

Similarly, max_y_Y is (max_y_Y - min_y_Y)^2.

Then, the maximum between x and y in X and Y groups is max( (max_x_X - min_x_X)^2, (max_y_Y - min_y_Y)^2, (max_x_X)^2 + (max_y_Y)^2 )

Wait, no. Because if you have a point in X with x=5 and another in Y with y=3, their squared distance is 5^2 +3^2=34. So the maximum over all cross terms would be the maximum x in X squared plus the maximum y in Y squared, but perhaps that's not the case. Wait, because for any x in X and y in Y, their squared distance is x^2 + y^2, so the maximum such value is (max_x_X)^2 + (max_y_Y)^2. Because x can be either positive or negative. Wait, but if x is negative, then x^2 is positive. So the maximum x squared is the maximum of (x_i)^2 for X points, same for Y points. So the cross term maximum is (max_x_X_squared) + (max_y_Y_squared), where max_x_X_squared is the maximum of x_i^2 for X points, and max_y_Y_squared is the maximum of y_j^2 for Y points.

Wait, but that's only true if all X points are on the x-axis. For example, if in X group, there are points 3 and -5. The maximum x squared is (-5)^2 =25. Similarly, Y group's max y squared is whatever. So the cross term is (25) + (max_y^2). But for any X point x and Y point y, the squared distance is x^2 + y^2, which would be <= 25 + max_y^2. So the maximum cross distance squared is the sum of the maximum x squared (from X group) and maximum y squared (from Y group).

So the maximum distance squared in the entire configuration is the maximum of:

- (max_x_X - min_x_X)^2 (the squared distance between two X points)
- (max_y_Y - min_y_Y)^2 (squared distance between two Y points)
- (max_x_X_sq + max_y_Y_sq) (squared distance between X and Y points)

Wait, but how about the X group's max x and min x? For example, if X has x ranging from -5 to 3. The distance between them is 8, squared is 64. But the max_x_X_sq is 25 (from -5) and the max_y_Y_sq is, say, 16. Then the cross term is 25+16=41, which is less than 64. So the maximum would be the X group's own spread.

So the maximum of the three values is the overall maximum squared distance.

So the problem reduces to partitioning the points into X and Y groups such that the maximum of these three terms is as small as possible.

Now, how do we model this? Let's think about possible ways to split the points.

The possible splits can be characterized by which points go to X and which go to Y.

But with n up to 1e5, we need an efficient way to compute the best split.

An alternative approach: perhaps the optimal solution is to put all points on X or all on Y. Let's see.

For example, in the first sample input, putting all on X gives a max distance of 0. Which is better than any split.

In the second sample, putting one on X and one on Y gives a cross term of 1 +1=2, which is better than putting both on X (distance (1-10)^2=81) or both on Y (distance (10-1)^2=81). So splitting is better.

So sometimes splitting is better, sometimes not.

We need to find the split that gives the minimal possible maximum of the three terms.

But how?

Another observation: For any split, the maximum cross term (max_x_sq + max_y_sq) can't be less than the maximum of max_x_sq and max_y_sq. Because if, say, max_x_sq is 25 and max_y_sq is 16, then the sum is 41, which is larger than both.

But when all points are in X, the cross term is 0 (since Y is empty). So the maximum is the spread of X points.

So the problem is to choose between splitting into X and Y, or putting everything in X or everything in Y.

But how to evaluate all possible splits efficiently?

Wait, perhaps the minimal possible maximum is the minimum among:

1. The maximum when all are X points.

2. The maximum when all are Y points.

3. The minimal maximum when some are X and others Y.

So first, compute the case where all are X: compute the spread (max_x - min_x) squared. Then compute the case where all are Y: spread (max_y - min_y) squared. Then, compute the minimal possible maximum when splitting into X and Y. The answer is the minimum of these three.

So the main challenge is to compute the third case: the best possible split into X and Y groups.

But how to compute that efficiently.

Hmm. Let's think about the split case. The maximum can come from three sources: the X spread, Y spread, or cross term.

So when we split into X and Y, we need to track:

- max_x and min_x for X group.

- max_y and min_y for Y group.

- max_x_sq (max of x_i^2 in X)

- max_y_sq (max of y_i^2 in Y)

But how do we model this? For each possible split, we need these values.

But trying all possible splits is impossible. So we need a way to find the split that minimizes the maximum of the three terms.

Alternative idea: perhaps the optimal split is determined by some criteria on x and y values. For example, for a point (x, y), if x^2 is smaller than y^2, assign it to X, else to Y. But this might not work for all cases.

Alternatively, perhaps the optimal split is such that for each point (x, y), if x^2 <= y^2, we assign it to X, else to Y. Let's see if this works for the sample input.

Sample 2:

Points (1,10) and (10,1). For the first point, x^2=1, y^2=100. So 1 < 100: assign to X. The second point x^2=100, y^2=1. 100>1: assign to Y. So cross term is 1^2 +1^2=2, which is correct. So that's the optimal split.

Another example: if a point has x=3 and y=4. x^2=9, y^2=16. Assign to X (since 9 <16). Then in Y group, perhaps other points with higher y^2.

But how does this affect the maximum cross term?

Hmm. The cross term is the sum of the maximum x^2 in X and maximum y^2 in Y. So if we split points into X and Y such that for all X points x_i^2 <= y_i^2, and for Y points y_j^2 < x_j^2, then the maximum x^2 in X is the maximum among all x_i where x_i^2 <= y_i^2. Similarly for Y.

Then the cross term would be (max_x_X_sq) + (max_y_Y_sq). But what's the maximum between X's own spread, Y's own spread, and this cross term?

But perhaps this split is the best possible. Let's see.

If we split all points into X where x^2 <= y^2, and Y otherwise, then the cross term would be (max x^2 in X) + (max y^2 in Y). But since in X group, x^2 is <= y^2, but in Y group, y^2 < x^2. So max x^2 in X is the maximum x^2 among those points where x^2 <= y^2. Max y^2 in Y is the maximum y^2 among points where y^2 < x^2.

But this seems a bit arbitrary. For example, if a point has x=4, y=3. Then x^2=16>9=y^2. So it goes into Y. The cross term would be (max x^2 in X) + (max y^2 in Y). For Y points, their y^2 can be up to (x^2 -1) for each point.

But perhaps this split minimizes the cross term. Because for each point in X, we are choosing the axis where their squared value is smaller, thus contributing less to the cross term.

But even if this split gives the minimal possible cross term, we still need to consider the X group's spread and Y group's spread.

So perhaps the optimal split is to split the points into X and Y as described (X where x^2 <= y^2, Y otherwise), then compute the maximum between X spread, Y spread, and cross term, and compare with all-X and all-Y cases.

But how do we compute the X and Y group's spread and their max x^2 and max y^2 quickly?

For all points, we can precompute:

- All x's and y's.

But for the split where X is those with x^2 <= y^2, and Y otherwise, we can:

- Collect all X points' x coordinates (so for X group, the spread is max_x_X - min_x_X), and their max x squared (which is max(x_i^2 for X group points)).

- Collect Y points' y coordinates (spread is max_y_Y - min_y_Y), and their max y squared (max(y_i^2 for Y group points)).

Then compute the three terms and take the maximum.

But then, this split may not be optimal. Are there cases where a different split gives a better result?

Hmm. Let's think of a scenario where splitting some points with x^2 > y^2 into X might improve the overall maximum.

For example, suppose we have two points:

Point A: (3,0) → x^2 =9, y^2=0. So x^2 > y^2. So according to the split, it would go to Y. But assigning it to X would make the X group's spread include 3, and Y group would be empty. But the cross term would be zero. So the maximum would be the X spread. But if the point is assigned to Y, then it's a Y group point (since x^2 > y^2 here?), but Y group points have their y coordinates. Wait, no. Wait, when a point is assigned to Y, it's (0, y_i). So for point A, if it's assigned to Y, the new point is (0,0). So in the split where all points go to Y, the spread is (max_y_Y - min_y_Y) squared, which is zero. So the maximum is zero.

So in this case, putting all points in Y gives a better result. So the split based on x^2 and y^2 may not be optimal.

So perhaps the split based on x^2 and y^2 is not the optimal way. Therefore, this approach might not work.

Alternative approach: The cross term (x^2 + y^2) is minimized when for each point, we choose the axis (X or Y) that gives the smaller contribution to their possible cross terms. But when splitting, the cross term is the sum of the maximum x^2 in X and the maximum y^2 in Y. So perhaps, the best way to minimize this sum is to split the points into X and Y such that the maximum x^2 in X and the maximum y^2 in Y are as small as possible.

But how to achieve that.

Another idea: For each point, the contribution to the cross term if placed in X is its x^2 (if it's the maximum x in X), and if placed in Y, it's y^2 (if it's the maximum y in Y). So for each point, choosing to put it in X or Y depends on whether x^2 is less than y^2. Because by placing it in X, the x^2 may be part of the cross term sum. But if it's placed in Y, the y^2 may be part of the sum.

So perhaps the optimal split is indeed to assign each point to X if x^2 <= y^2, else to Y. Then, the cross term is the sum of the max x^2 in X and max y^2 in Y.

But how do the X and Y group spreads compare to the cross term sum?

In some cases, the X group's spread could be larger than the cross term sum. For example, X group could have points from -100 to 100. Then, the spread is 200^2 =40000, but the cross term sum might be 100^2 + (something else), which could be larger.

But perhaps in this case, the maximum between the spread and the cross term sum would be whichever is larger.

But how do we compute all of this efficiently.

The steps could be:

1. Compute the all-X case: all points are electrons. Compute max_x and min_x for X, then spread squared (max_x - min_x)^2.

2. Compute the all-Y case: all points are protons. Compute max_y and min_y for Y, spread squared (max_y - min_y)^2.

3. Compute the split case where each point is assigned to X if x^2 <= y^2, else to Y. For this split:

   a. Collect all x's in X group, compute max_x_X, min_x_X → spread_x = (max_x_X - min_x_X)^2.

   b. Collect all y's in Y group, compute max_y_Y, min_y_Y → spread_y = (max_y_Y - min_y_Y)^2.

   c. Compute cross_term = (max_x_sq_X) + (max_y_sq_Y), where max_x_sq_X is max x^2 in X group, max_y_sq_Y is max y^2 in Y group.

   d. The maximum of these three (spread_x, spread_y, cross_term) is the value for this split.

4. Then, compute the minimum possible maximum among all three cases (all-X, all-Y, split).

But maybe there's a better split than the one based on x^2 vs y^2. For example, some points could be moved to X even if their x^2 is larger than y^2, but that would lower the cross term sum.

But considering all possibilities is impractical. So perhaps this split is the best possible, or maybe there's a better way.

Another idea is to find for each point the optimal assignment that minimizes the cross term sum. But that's again not straightforward.

Alternatively, maybe the optimal split is such that the cross term sum is minimized. Because if the cross term sum is the largest of the three terms, then minimizing that sum would lower the overall maximum.

But how to model that.

Alternatively, think of the cross term sum as the sum of the maximum x^2 in X and maximum y^2 in Y. To minimize this sum, for each point, assign it to X if x^2 < y^2 (thus x^2 contributes less to the sum when in X group, and y^2 is not considered for Y group). But if x^2 is greater than y^2, assigning to Y reduces the sum.

But this is exactly the split where x^2 <= y^2 → X, else Y. Because in this split, for X group, the x^2 is <= y^2 (so their x^2 is as small as possible for their group), and for Y group, the y^2 is as small as possible (since x^2 > y^2). Thus, the sum of the maximum x^2 in X and maximum y^2 in Y is minimized.

Therefore, this split minimizes the cross term sum. But the cross term sum may not be the maximum term. For example, if the X group's spread is larger than the cross term sum, then the maximum is determined by the spread.

But by choosing this split, perhaps we have the minimal possible cross term sum. So the overall maximum (the maximum of the three terms) would be the minimal possible when considering all possible splits.

Thus, the approach would be:

Compute the three options (all X, all Y, split as per x^2 <= y^2) and take the minimum among them.

But is this sufficient?

Let's test this approach against the sample inputs.

First sample:

3 points with x=1 and varying y. All in X:

max_x and min_x are 1, so spread is 0. All-Y: the y's are 10, 20,30. Spread squared is (30-10)^2=400. Split case: each point's x^2 is 1, which is less than y^2 (10^2=100, etc.), so all go to X. So same as all-X case. Maximum is 0. So the minimum is 0.

Second sample: two points. All-X: spread is (1-10)^2=81. All-Y: (10-1)^2=81. Split case: point 1 (1,10) → x^2=1 <= 100 → X. point2 (10,1) → x^2=100 >1 → Y. So X group has x=1, spread 0. Y group has y=1, spread 0. Cross term is 1^2 +1^2=2. So maximum is 2. So the answer is min(81,81,2) → 2. Correct.

Another test case: say, two points (3,4) and (5, 0). All-X: spread is 5-3=2. Squared 4. All-Y: (4 and 0) spread 4-0=4. Squared 16. Split case: (3,4) → x^2=9 <16 → X. (5,0) → x^2=25 >0 → Y. So X group has x=3. Spread 0. Y group has y=0. Spread 0. Cross term 9+0=9. So maximum is 9. So the answer is min(4,16,9) →4. So the all-X case is better.

So in this case, the split case isn't the best. So the approach of considering all three possibilities works.

Thus, the approach is to compute all three possibilities (all-X, all-Y, split as per x^2 <= y^2) and choose the minimum among them.

But what if there exists a split that is better than these three possibilities?

For example, suppose we have four points:

A(0,0), B(0,0), but wait, the input says no two points coincide. So maybe another example.

Let's say, two points:

Point1: x=2, y=3 → x^2=4 <9 → X group.

Point2: x=3, y=2 → x^2=9>4 → Y group.

Cross term is 4 (max x in X is 2, max y in Y is 2 → 2² +2²=8). But the spread in X group is 0, Y group spread is 0. So max is 8.

But if instead, we assign point2 to X group, then X group has x=2 and 3. Spread is 1, squared 1. Y group is empty. So maximum is 1. Which is better than 8.

So this split (assigning point2 to X) gives a better result. But according to our initial split criteria (x² <= y²), point2 is assigned to Y. So in this case, the initial split gives a higher maximum than a different split.

So the approach of considering the split based on x² vs y² is not sufficient. So there must be a better way.

Hmm. So what's wrong here? In this example, the split based on x² vs y² leads to a cross term of 8, but if we split differently, the maximum is 1.

So the initial approach would miss this better split.

Thus, the initial approach is not sufficient. So what's the correct way to model this?

This suggests that the split based on x² <= y² is not optimal. So we need to find another way.

Alternative approach: perhaps the minimal possible maximum is the minimal possible among all possible splits, but how to find that.

But with n=1e5, how can we check all possible splits?

Alternatively, perhaps the optimal split is when one group is empty. That is, all-X or all-Y.

But in the previous example, all-X would have spread (3-2)=1, which gives squared 1. All-Y would have spread (3-2)=1, squared 1. So the answer is 1, which is better than the split.

So in this case, all-X and all-Y are better than the split.

So the approach of considering all three cases (all-X, all-Y, split based on x² vs y²) would work here. Because in this example, the all-X and all-Y cases give a better result.

So in that case, our initial approach would still select the correct answer.

Wait, in this example:

points (2,3) and (3,2).

all-X case: X group includes both points. So x coordinates are 2 and3. spread is 1. squared 1.

all-Y case: Y group includes both points. y coordinates are 3 and 2. spread is 1. squared 1.

split based on x² vs y²: point1 (2,3) → x²=4 <9 → X. point2 (3,2) → x²=9>4 → Y. So X has x=2, Y has y=2. cross term is 4 +4=8. So maximum is 8. The split case's maximum is 8. So the minimal is 1.

So the initial approach correctly selects the all-X or all-Y case, which gives a better result.

Thus, the initial approach of considering all three cases (all-X, all-Y, and split based on x² vs y²) would work.

But in some other cases, perhaps there is a split that is better than these three options.

But how to check that.

Another example.

Suppose we have three points:

A: x=1, y=5 → x²=1 <25 → X.

B: x=5, y=1 → x²=25>1 → Y.

C: x=3, y=3 → x²=9=9 → X.

Split based on x² vs y²: A and C in X, B in Y.

X group's spread: 1 and3 → spread 2. Squared 4.

Y group's spread: 1 → 0.

cross term: max x² in X is 9 (3²), max y² in Y is 1 (1²). sum 10. So maximum is max(4, 0, 10) =10.

But what if we assign C to Y. Then X group has x=1. Y group has B (y=1) and C (y=3). So Y group's spread is 3-1=2. Squared 4. Cross term: max x² (1) + max y² (3²=9) → 10. So maximum is 10.

Alternatively, if we assign C to X, then X group has x=1 and 3. Spread is 2 → 4. Y group has B. Cross term is 9 (3²) +1 →10. So same result.

But what if we assign B to X and C to Y.

X group: A, B → x=1,5. Spread 4 → 16.

Y group: C → y=3. spread 0.

cross term: max x² (5²=25) + max y² (9) →34. maximum is 34.

Which is worse.

Thus, in this case, the initial approach gives a maximum of 10. But what is the best possible split?

Is there a split with a maximum less than 10?

If we assign A to X, B to X, C to Y.

X group x: 1,5. spread 4 →16.

Y group y:3. spread 0.

cross term: 25 +9=34. So maximum is 34. No.

Alternatively, assign B to X, and A and C to Y.

X group: B's x=5. spread 0.

Y group: y=5 (A's y), 3 (C's y). spread 2 →4.

cross term: 25 (from X's 5²) +25 (Y's 5²) →50. maximum is 50.

No.

So in this example, the initial approach gives the best possible split. But maybe another approach could find a better split.

Alternatively, perhaps the minimal possible maximum is the minimum between all-X, all-Y, and the split case.

In this example, all-X would have points (1,0), (5,0), (3,0). spread is 5-1=4 → squared 16. All-Y would have points (0,5), (0,1), (0,3). spread is 5-1=4 → squared 16. So the split case gives a maximum of 10, which is better. So the answer is 10.

But in this case, the split case is better than all-X and all-Y.

So the initial approach works.

Another example where split case is better than all-X and all-Y.

Hmm. So perhaps the approach is correct.

Thus, the steps are:

1. Compute all-X case.

2. Compute all-Y case.

3. Compute split case where X is {x_i | x_i^2 <= y_i^2}, Y is others.

Compute the maximum of spread_x^2, spread_y^2, cross_term.

Take the minimum among the three options.

Thus, the code should:

- Precompute for all-X: max_x, min_x → (max_x - min_x)^2.

- Precompute for all-Y: max_y, min_y → (max_y - min_y)^2.

- For split case:

   a. Split points into X and Y based on x² <= y².

   b. For X group, collect all x coordinates. If none, then X group's spread is 0 (or ignore, since spread_x is 0). Compute max_x_X, min_x_X → spread_x = (max_x_X - min_x_X)^2.

   c. For Y group, collect all y coordinates. If none, then spread_y is 0. Compute max_y_Y, min_y_Y → spread_y = (max_y_Y - min_y_Y)^2.

   d. Compute max_x_sq_X as max(x_i^2 for X group), max_y_sq_Y as max(y_i^2 for Y group).

   e. cross_term = max_x_sq_X + max_y_sq_Y.

   f. current_max = max(spread_x, spread_y, cross_term).

   g. If X group is empty, then cross_term is max_y_sq_Y (since max_x_sq_X is 0? Or is it not present? Wait, if X group is empty, then cross_term is 0 (since there are no points in X and Y). Or wait, no. Because in split case, X and Y are non-empty. Wait, no. The split case can have X group empty (if all points have x² > y²) or Y group empty (if all have x² <= y²).

   So, for example, if all points are in X group, then Y group is empty. So for the split case:

   spread_x is (max_x_X - min_x_X)^2.

   spread_y is 0.

   cross_term is max_x_sq_X + 0 (since Y group is empty, max_y_sq_Y is 0? Or undefined?)

   Wait, in this case, Y group is empty. So when there are no points in Y group, the cross term is the maximum x squared in X (since there are no Y points, so no cross term). But cross term is the maximum between all x in X and all y in Y. But Y is empty. So cross term would be 0, since there are no points to pair between X and Y.

   Or perhaps cross term is 0 in that case. Because there are no pairs between X and Y.

   So in the split case where Y is empty, cross_term is 0. Similarly, if X is empty, cross_term is 0.

   So in code:

   For split case:

   if X group is empty: cross_term is 0.

   if Y group is empty: cross_term is 0.

   else: cross_term is max_x_sq_X + max_y_sq_Y.

So for split case:

if X group is empty:

   spread_x = 0

   cross_term = 0

   current_max = max(0, spread_y, 0) → spread_y.

Similarly for Y group empty.

Thus, the code must handle empty groups properly.

So steps for split case:

split the points into X and Y groups.

if X group is non-empty:

   max_x_X = max(x_i)

   min_x_X = min(x_i)

   spread_x = (max_x_X - min_x_X) **2

   max_x_sq_X = max(x_i^2 for x_i in X group)

else:

   spread_x = 0

   max_x_sq_X = 0

similar for Y group.

cross_term = (max_x_sq_X if X group non-empty else 0) + (max_y_sq_Y if Y group non-empty else 0)

then current_max_split = max(spread_x, spread_y, cross_term)

So the code must handle this.

Now, implementing this.

But how to compute all this efficiently.

In Python:

We can precompute all-x, all-y, then split into X and Y groups.

For each point (x, y):

if x² <= y² → add to X group (collect x)

else → add to Y group (collect y)

Then for X group:

if not empty → compute max_x, min_x, max_x_sq.

else → spread_x =0, max_x_sq=0.

Similarly for Y group.

Then compute spread_x, spread_y, cross_term.

current_max_split is max of the three.

The minimal of all-x case, all-y case, current_max_split is the answer.

Thus, the code can be structured as follows:

Read n.

Read all points as list.

Compute all-x case: collect all x coordinates, compute max_x and min_x → spread_x = (max_x - min_x)^2.

Compute all-y case: collect all y coordinates → spread_y = (max_y - min_y)^2.

Split the points into X and Y groups based on x² <= y².

Compute X group's max_x, min_x, max_x_sq.

Compute Y group's max_y, min_y, max_y_sq.

Compute spread_x_split = (max_x - min_x)^2 if X group non-empty else 0.

spread_y_split = (max_y - min_y)^2 if Y group non-empty else 0.

cross_term_split = (max_x_sq if X group else 0) + (max_y_sq if Y group else 0).

current_max_split = max(spread_x_split, spread_y_split, cross_term_split).

The answer is min(all-x spread, all-y spread, current_max_split).

Thus, the code can be written.

Now, let's test the code against the examples.

First example:

3 points:

1 10 → x²=1 <= 100 → X.

1 20 → X.

1 30 → X.

X group's max_x is 1, min_x 1 → spread 0.

Y group is empty → spread 0. cross_term is 1² +0=1?

Wait no. Because X group has max_x_sq = 1^2 =1. Y group is empty. So cross_term is 1 + 0 =1. But current_max_split is max(0,0,1) →1. But the all-x case gives spread 0. So the answer is min(0, 400, 1) →0. Correct.

Ah, right. So in the split case, cross_term is 1, but all-x case is 0.

So the code correctly chooses the all-x case.

Second example:

points (1,10) and (10,1).

all-x spread: (10-1)^2=81.

all-y spread: (10-1)^2=81.

split case: X group has x=1, Y group has y=1.

spread_x_split is 0, spread_y_split is 0. cross_term is 1 +1=2. current_max_split is 2. answer is min(81,81,2) →2.

Correct.

Third example: two points (2,3) and (3,2).

all-x spread: (3-2)^2=1.

all-y spread: (3-2)^2=1.

split case: X group x=2, Y group y=2.

spread_x_split 0, spread_y_split 0. cross_term 4+4=8. current_max_split is 8. answer is min(1,1,8) →1.

Correct.

Fourth example:

A(2,3), B(3,2), split case's cross_term is 8. But all-x case gives better.

Thus, the code works.

Now, let's think about the edge cases.

Case where all points are in X group in split.

Like all points have x² <= y².

Then, split case is same as all-x case. So the code's current_max_split would be same as all-x.

But then, the code will compare all three cases and take the minimum. So no problem.

Another edge case: when all points are assigned to Y group in split.

Same as all-Y case.

Another case where X and Y groups are non-empty, but the cross term is the maximum.

Like the second sample.

Thus, the code seems correct.

Now, let's code this.

In Python:

Read n.

points = list of (x, y) tuples.

Compute all_x_spread:

xs = [x for x, y in points]

if not xs: all_x_spread =0. But since n >=1, xs is not empty.

max_x = max(xs)

min_x = min(xs)

all_x_spread = (max_x - min_x) **2

Similarly for all_y_spread.

Split into X and Y groups:

x_group = [x for x,y in points if x*x <= y*y]

y_group = [y for x,y in points if x*x > y*y]

Compute for x_group:

if x_group is empty:

   spread_x_split =0

   max_x_sq =0

else:

   max_x = max(x_group)

   min_x = min(x_group)

   spread_x_split = (max_x - min_x) **2

   max_x_sq = max(x*x for x in x_group)

Similarly for y_group.

cross_term_split = max_x_sq + max_y_sq.

current_max_split = max(spread_x_split, spread_y_split, cross_term_split)

Then, the answer is min(all_x_spread, all_y_spread, current_max_split).

But wait, in the split case, the current_max_split is the maximum of spread_x_split, spread_y_split, cross_term_split.

So the code will compute that.

Thus, the code is:

Read n.

Then read n lines of x and y.

Compute all_x_spread, all_y_spread.

Split into X and Y groups.

Compute spread_x_split, spread_y_split, cross_term_split.

current_max_split is max of these three.

answer is min(all_x_spread, all_y_spread, current_max_split).

Now, in Python, for large n (1e5), list comprehensions are efficient.

But for x_group and y_group, we need to collect x and y values.

But perhaps it's more efficient to loop through each point once, and collect the x's and y's for the split.

Yes, for each point, check x^2 <= y^2. If yes, add x to x_group, else add y to y_group.

Thus, in code:

x_group = []
y_group = []
for x, y in points:
    if x * x <= y * y:
        x_group.append(x)
    else:
        y_group.append(y)

Then process x_group and y_group.

For the split case:

spread_x_split = 0

max_x_sq = 0

if x_group:

    max_x = max(x_group)

    min_x = min(x_group)

    spread_x_split = (max_x - min_x) **2

    max_x_sq = max(x*x for x in x_group)

Similarly for y_group.

Now, for max_x_sq, which is the maximum x^2 in x_group. Since x_group contains x's of points where x^2 <= y^2, the max x^2 is the maximum of x_group elements squared.

But since x can be negative, x squared is positive.

So for example, x_group could have elements -5 and 3. Their squares are 25 and 9. So the max x squared is 25.

Thus, max_x_sq = max(x **2 for x in x_group) → yes.

But for large n, this would take O(k) time where k is the length of x_group. For 1e5 elements, this is acceptable.

But for 1e5 elements, the max operation is O(n), but since it's done once for each group, it's acceptable.

Thus, the code should work.

Now, let's code this.

Also, note that the answer must be an integer. All computations are integer-based.

So code:

n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append( (x, y) )

# All X case
xs = [x for x, y in points]
max_x = max(xs)
min_x = min(xs)
all_x_spread = (max_x - min_x) ** 2

# All Y case
ys = [y for x, y in points]
max_y = max(ys)
min_y = min(ys)
all_y_spread = (max_y - min_y) ** 2

# Split case
x_group = []
y_group = []
for x, y in points:
    if x * x <= y * y:
        x_group.append(x)
    else:
        y_group.append(y)

spread_x_split = 0
max_x_sq = 0
if x_group:
    max_x_x = max(x_group)
    min_x_x = min(x_group)
    spread_x_split = (max_x_x - min_x_x) ** 2
    max_x_sq = max(x*x for x in x_group)

spread_y_split = 0
max_y_sq = 0
if y_group:
    max_y_y = max(y_group)
    min_y_y = min(y_group)
    spread_y_split = (max_y_y - min_y_y) ** 2
    max_y_sq = max(y*y for y in y_group)

cross_term_split = max_x_sq + max_y_sq

current_max_split = max(spread_x_split, spread_y_split, cross_term_split)

answer = min(all_x_spread, all_y_spread, current_max_split)

print(answer)

Testing this code against the sample inputs.

Sample 1:

3
1 10
1 20
1 30

x_group contains all three x's (1) since x²=1 <= y² (100, 400, 900).

split case:

spread_x_split is 0.

y_group is empty.

cross_term_split = 1^2 +0=1.

current_max_split is max(0,0,1) →1.

all_x_spread is 0.

answer is min(0, 400, 1) →0. Correct.

Sample 2:

2
1 10
10 1

all_x_spread is (10-1)^2=81.

all_y_spread is (10-1)^2=81.

split case: x_group contains x=1 (1²=1 <= 100), y_group contains y=1 (10²=100>1).

spread_x_split is 0, spread_y_split is 0. cross_term_split=1+1=2.

current_max_split is 2. answer is 2. Correct.

Another test case:

points (3,0) and (5,0). all_x_spread is 2²=4. all_y_spread is 0. split case: x_group includes both (3²=9>0 → no? Wait, x² for (3,0) is 9, y² is 0. So x²> y². So (3,0) is in Y group. y is 0. (5,0) also in Y group. So split case's Y group is [0,0]. spread_y_split is 0. cross_term is 0 +0=0. current_max_split is 0. So answer is min(4, 0, 0) →0. Which is correct. So all-Y case gives spread (0-0) →0. So answer is 0.

But according to the code, the all-Y case is 0.

Wait, in all-Y case, the y coordinates are 0 and 0 (since all points are put into Y group. So max_y and min_y are 0. spread is 0. So answer is 0.

Thus, code works.

Another example: points (2,3), (3,2).

split case: x_group has x=2 (4<=9 → yes). y_group has y=2 (x=3's x²=9>4 → yes. So Y group has y=2.

split case's cross term is 2² +2²=8. all-x case gives 1, which is better. So code selects 1.

Thus, the code works.

So this code should handle all cases correctly.

Now, for optimization:

The code runs in O(n) time for each part. The split case's loops are O(n). The max and min functions are O(n), but for the all-x and all-y cases, we already compute the max and min once. For the split case, we compute them again for x_group and y_group.

But for n=1e5, this is acceptable.

But in Python, the code may be optimized.

For example, in the split case, when building x_group and y_group, we can track the max and min for x_group and y_group as we go, to avoid looping through them again.

This would save O(k) time for each group, but for 1e5 elements, it's manageable, but can save some time.

But in Python, using the built-in max and min functions on lists is optimized and should be fast enough.

Alternatively, during the split loop:

for x, y in points:

   if x² <= y²:

       add to x_group and track current max and min.

But for code clarity, perhaps it's better to do it as in the previous code.

Thus, the code is acceptable.
</think>

```python
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# All X case
xs = [x for x, y in points]
max_x, min_x = max(xs), min(xs)
all_x = (max_x - min_x) ** 2

# All Y case
ys = [y for x, y in points]
max_y, min_y = max(ys), min(ys)
all_y = (max_y - min_y) ** 2

# Split case
x_group = []
y_group = []
for x, y in points:
    if x * x <= y * y:
        x_group.append(x)
    else:
        y_group.append(y)

spread_x = 0
max_x_sq = 0
if x_group:
    x_max, x_min = max(x_group), min(x_group)
    spread_x = (x_max - x_min) ** 2
    max_x_sq = max(x * x for x in x_group)

spread_y = 0
max_y_sq = 0
if y_group:
    y_max, y_min = max(y_group), min(y_group)
    spread_y = (y_max - y_min) ** 2
    max_y_sq = max(y * y for y in y_group)

cross = max_x_sq + max_y_sq
split_max = max(spread_x, spread_y, cross)

print(min(all_x, all_y, split_max))
```