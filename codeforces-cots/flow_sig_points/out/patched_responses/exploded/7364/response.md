<think>
Okay, let's try to solve this problem. Hmm, the problem says we need to compute the distance between permutation a and each cyclic shift of permutation b. The distance here is the minimum |i-j| where a_i equals b_j in the shifted b. For each cyclic shift of b, we have to find this minimum value.

First, let's understand what a cyclic shift does. For example, if the original b is [b1, b2, b3, ..., bn], a cyclic shift by k positions would make it [bk+1, bk+2, ..., bn, b1, b2, ..., bk]. Wait, no. Wait, the problem says cyclic shift number i is bi followed by bi+1 ... bn, then b1 to bi-1. Oh right, so for shift 1, it's the original array. Shift 2 would start with the second element, then third, etc., and wrap around. Wait, no. Wait, the problem's description says: cyclic shift number i is bi, bi+1 ... bn, followed by b1, b2, ..., bi-1. So for example, if n=4 and i=3, the shift is b3, b4, b1, b2. So for each shift i (1-based?), the new permutation is created by rotating the original b so that the i-th element comes first. So the shift count is equal to how many positions you've rotated. For example, shift 1 is the original, shift 2 would be starting with the second element, etc. Wait, no. Wait, the cyclic shift number i refers to the starting element. So for shift 1, the permutation starts with b1, then b2, etc. For shift 2, it's b2, b3, ..., bn, then b1. So the cyclic shifts are the permutations obtained by rotating the original array left by (i-1) positions. For example, shift 1 is the original. Shift 2 is rotating once to the left, so the first element moves to the end. No, wait. Let me see. The cyclic shift number i would have the elements arranged as bi, b_{i+1}, ..., b_n, followed by b_1, b_2, ..., b_{i-1}. So for i=1, it's the original array. For i=2, it's [b2, b3, ..., bn, b1]. For i=3, it's [b3, b4, ..., bn, b1, b2], etc. So each shift is determined by the starting index. So the shift with number i is equivalent to rotating the array such that the i-th element becomes the first.

Now, the problem requires that for each such shift of b, we compute the minimum |i-j| where a_i equals the shifted b's j-th element. But the way the shift is structured, the j-th position in the shifted array corresponds to a certain position in the original array. Let's think of the original positions in b. For a cyclic shift with number k, the shifted array is [b_k, b_{k+1}, ..., b_n, b_1, b_2, ..., b_{k-1}]. The j-th element in the shifted array is b_{k + j - 1} if j <= n - k + 1, else b_{j - (n -k +1)}. Wait, maybe it's easier to model the shifted array as starting at position k, then wrapping around. So for the shifted array S, S[0] is b[k], S[1] is b[k+1], etc., modulo n. Wait, but the indices here need to be 1-based. Hmm. So for a given shift k (from 1 to n), the shifted array's elements can be represented as follows: for each position j in the shifted array (0-based?), the original index in b is (k-1 + j) mod n. Because, for example, when k=1, the shifted array starts at 0 (assuming 0-based?), but the problem's description uses 1-based indices. Let me re-express this. Original b is 1-based. For a shift k, the first element is b[k], then b[k+1], ..., up to b[n], then b[1], ..., b[k-1]. So for the shifted array, the j-th element (1-based) is equal to b[(k + j - 2) mod n + 1]. Let's see: when j=1, it's k. j=2: k+1, etc. Once we reach j = n -k +1, then the next j would wrap around. Alternatively, for each j in the shifted array (1-based), the original position in b is (k + j -1 -1) mod n +1? Wait, maybe an example will help. Let's take n=4 and k=3. Shifted array is [3,4,1,2]. So for j=1 in shifted array, it's b[3]. j=2: b4. j=3: (3+3-1) mod 4 +1? Hmm, maybe not. Alternatively, for shift k, the j-th element of the shifted array is b[(k + j -1 -1) mod n + 1]?

Wait, maybe it's easier to model the original indices as 0-based. Let's reindex everything to 0-based. Then for shift k (which would be 0-based), the shifted array is [b_k, b_{k+1}, ..., b_{n-1}, b_0, b_1, ..., b_{k-1}]. So for shifted array position j (0-based), the original index is (k + j) mod n. But in the problem statement, shifts are 1-based. So if the problem's shift is numbered i (1-based), then in 0-based terms, the starting index is i-1. So for shift i (1-based), the original index in b for the j-th position (0-based) in the shifted array is ( (i-1) + j ) mod n. So the shifted array S_i is such that S_i[j] = b[ (i-1 +j) mod n ].

But in the problem's terms, when you have a cyclic shift of b, each element's position in the shifted array corresponds to a certain position in the original array. So for example, when we perform a cyclic shift i, the element x in the original array at position p will be in the shifted array at position (p - (i-1)) mod n. Because, the shifted array starts at position i-1 (0-based). So the original position p in b is mapped to (p - (i-1)) mod n in the shifted array. Wait, perhaps not. Let's think: in the shifted array, the first element is original position i-1 (0-based). The second element is i, and so on. So for each element in the original array, its position in the shifted array is (original_p - (i-1)) mod n. For example, if original_p is i-1, then it's at position 0. If original_p is i, it's at position 1, etc. So for any original position p in b, its position in the shifted array for shift i is (p - (i-1)) mod n.

So, for each x in a, we can find where it appears in b. Let's create a dictionary pos_b where pos_b[x] is the position (original index in b, 0-based) where x is located. Then, for each x in a, which is at position i_a in a (0-based), we can compute for each shift i (1-based in the problem, 0-based in our code?), the position in the shifted array where x is located. But wait, in the problem, the distance is between the position in a and the position in the shifted array. So for each x, a's position for x is i_a (0-based?), and the shifted array's position for x is (pos_b[x] - (i_shift -1)) mod n, where i_shift is the problem's 1-based shift number. Then the absolute difference between i_a and that position is a candidate for the distance.

But the problem is that for each shift, we need to compute the minimum over all x of |i_a - ( (pos_b[x] - (shift-1)) mod n ) |, where shift ranges from 1 to n (1-based). Then, for each shift, we have to find the minimal such value.

The key insight here is that for each x in a, and its corresponding pos_b[x], we can model how the |i_a - shifted_pos| changes for each shift. Then, for each shift, the minimal value among all x is the answer.

But computing this for each shift directly would be O(n^2), which is way too slow for n=1e5.

We need a smarter approach. Let's think about how the shifts affect the position of x in the shifted array.

For a given x, which is in a's position i (0-based) and in b's position p (0-based), then for each shift k (1-based shift number), the position of x in the shifted array is (p - (k-1)) mod n. Wait, because when the shift is k (1-based), the shifted array starts at position k-1 (0-based). So the element at position p in the original array will be in the shifted array at position (p - (k-1)) mod n.

But the shifted array's positions are 0-based. So for x in a[i], the shifted array's position for x is (p - (k-1)) mod n. Then the distance for x in this shift is |i - ((p - (k-1)) mod n)|.

The problem is that for each shift k (from 1 to n), we have to find the minimum of this value over all x in a.

So the approach is to precompute, for each possible shift, the minimal |i - ( (p - (k-1)) mod n ) | across all x in a.

But how do we compute this efficiently?

Let's think of each x in a as contributing a possible value for each shift. For each x, the value |i - ( (p - (k-1)) mod n ) | is a function of k. We need for each k, find the minimum of all these values across x.

But n is up to 1e5, so O(n^2) is impossible. So we need a way to precompute for each possible shift the minimal value.

Alternative approach: For each x in a, we can model the possible shifts where the distance between i and (p - (k-1) mod n) is minimized, and track the minimal across all x.

But how?

Let's rephrase the expression. Let's denote shift k as s (since k ranges from 1 to n, s ranges from 0 to n-1 if we model it as 0-based shift). Let s = k-1. So s ranges from 0 to n-1. Then the position in the shifted array for x is (p - s) mod n. The distance for x is |i - ( (p - s) mod n ) |.

So the problem reduces to, for each s in 0..n-1, find the minimal |i_x - ((p_x - s) mod n)| over all x.

But how to compute this for all s efficiently.

Hmm. Let's consider that for each x, the term (p_x - s) mod n can be written as (p_x - s + n) mod n. So (p_x - s) mod n is equivalent to (n - s + p_x) mod n, but maybe that's not helpful.

Alternatively, for a given x, the term (p_x - s) mod n is equal to (p_x - s) if s <= p_x, else (p_x - s + n). So the position in the shifted array is (p_x - s) if s <= p_x, else (p_x - s + n). Then the distance is |i_x - (p_x - s)| if s <= p_x, else |i_x - (p_x - s + n)|.

But how can we model this for all s and find the minimal value per s?

Alternatively, let's consider that for each x, the distance for shift s is |i_x - ( (p_x - s) mod n )|. We can expand this as the minimum between two possibilities. Because (p_x - s) mod n can be written as (p_x - s) if s <= p_x, or (p_x - s +n) otherwise. So the absolute value can be written as either |i_x - (p_x - s)| when s <= p_x, or |i_x - (p_x - s + n)| otherwise.

But I'm not sure if that helps. Let's think in terms of s. For each x, the distance is a function of s, and we need to compute for each s the minimum of all x's distances.

Alternatively, for each x, the distance function over s can be considered as a periodic function. Let's see: when s increases by 1, the (p_x - s) mod n decreases by 1 (mod n). So for a particular x, as s increases, the position in the shifted array (for x) decreases by 1 each time, wrapping around when s passes p_x.

But the distance is |i_x - shifted_pos|. So for a particular x, as s increases, the shifted_pos for x is (p_x - s) mod n. So for x, the shifted_pos for s is (p_x - s) mod n, which is equal to (p_x - s + n) if s > p_x. So when s is in [0, p_x], shifted_pos = p_x - s. When s is in [p_x +1, n-1], shifted_pos = p_x - s + n.

So the distance for x and shift s is |i_x - (p_x - s)| when s <= p_x, else |i_x - (p_x - s + n)|.

Let's split into two cases:

Case 1: s <= p_x. Then shifted_pos = p_x - s. Distance is |i_x - (p_x - s)| = | (i_x - p_x) + s |.

Case 2: s > p_x. Then shifted_pos = (p_x - s) + n. Distance is |i_x - (p_x - s +n)| = | (i_x - p_x +n) - s |.

So for each x, the distance is the minimum between two linear functions of s, depending on whether s is in [0, p_x] or [p_x+1, n-1].

But how can we track this for all x and compute the minimal value per s?

Alternative idea: For each x, we can model the distance as | (i_x - p_x) + s | for s in [0, p_x], and | (i_x - p_x +n) - s | for s in [p_x +1, n-1]. Then, for each x, we can generate intervals of s where the distance is given by one of these expressions, and then track the minimal value across all x for each s.

But even this seems challenging, as for each x, there are two linear functions over different intervals of s.

But maybe we can model this as events on the s-axis (from 0 to n-1) and track for each s the minimal | ... |.

Alternatively, let's consider that for each x, the distance can be represented as a function of s. For example, for x, the distance function has a V-shape, but split into two parts. However, since the problem requires the minimal distance across all x for each s, perhaps we can precompute for each s the minimal of all | (i_x - p_x) + s | and | (i_x - p_x +n) - s |, considering the ranges where each applies.

But this seems complicated. Let's think of it as two separate functions for each x:

For each x, compute two possible distance functions:

1. When s <= p_x: distance = | (i_x - p_x) + s |. Let's denote this as d1(s) = | (i_x - p_x) + s |.

2. When s > p_x: distance = | (i_x - p_x +n) - s |. Let's denote this as d2(s) = | (i_x - p_x +n) - s |.

But for a given x, which of these functions is active depends on s. So for each x, there are two possible linear functions of s, each active in a certain interval.

The goal is, for each s, find the minimal value of min(d1(s), d2(s)) across all x.

But how to compute this efficiently.

Hmm. Let's note that for each x, the two functions d1 and d2 can be rewritten as:

d1(s) = | s + (i_x - p_x) |.

d2(s) = | s - (i_x - p_x +n) |.

So for each x, these are absolute value functions. The minimal of the two would depend on the value of s.

But to find the minimal across all x for each s, perhaps we can model these as events and use a line sweep algorithm.

Alternatively, let's precompute for each x the possible s ranges where d1 or d2 is active and contribute to the minimal distance.

But this seems difficult. Let's think of each x contributing to certain s ranges, and track for each s the minimal distance from all x.

Another angle: The minimal distance for each s is the minimum of |i_x - ((p_x - s) mod n)| over all x. Since the problem requires the minimum over all x, perhaps for each s, the minimal is achieved by the x that has (i_x - ((p_x - s) mod n)) as close to zero as possible.

But how to find that x quickly.

Alternative idea: For each x, compute (p_x - i_x) mod n. Let's call this shift_opt. Because when s equals (p_x - i_x) mod n, then the position in the shifted array for x is (p_x - s) mod n = (p_x - (p_x - i_x)) mod n = i_x mod n. Then the distance is |i_x - i_x| = 0. So for shift s equal to (p_x - i_x) mod n, x contributes a distance of 0. However, this is only possible if s is such that the x's position in the shifted array is exactly i_x. But in that case, the distance is zero, which is the minimal possible. So for each x, there exists a shift s where x contributes a distance of 0. However, other x's may have lower distances in that shift.

So the minimal distance for a shift s is zero if there's any x such that (p_x - s) mod n == i_x. So for each x, the s where (p_x - s) mod n == i_x is s = (p_x - i_x) mod n. Because (p_x - s) mod n = i_x mod n implies s ≡ (p_x - i_x) mod n. So s = (p_x - i_x) mod n.

So for each x, the optimal shift s for x is s_x = (p_x - i_x) mod n. If for a given shift s, any x has s_x = s, then the answer for that shift is zero. Otherwise, the answer is the minimal among the other x's distances.

So the first thing to check is: for each shift s, is there any x where s_x = s. If yes, then the answer is zero. Otherwise, compute the minimal distance among all x.

So the plan is:

1. Precompute for each x the s_x = (p_x - i_x) mod n.

2. For each s in 0..n-1, collect the count of x's with s_x = s.

3. For each shift s, if there's at least one x with s_x = s, output 0.

4. Else, compute the minimal distance among all x's for this shift s.

But step 4 is O(n) per s, which is O(n^2) in total. Which is impossible for n=1e5.

So we need a way to compute step 4 efficiently when there's no x with s_x = s.

But how?

Alternatively, we can precompute for each s, the minimal distance from all x's. But how.

But for a given s, the minimal distance is the minimum over all x's of |i_x - ((p_x - s) mod n)|. Which is equivalent to | (i_x - p_x) + s | if s <= p_x, else | (i_x - p_x + n) - s |.

But perhaps we can model this as two separate line sweeps.

Wait, perhaps it's possible to precompute for each s the minimal of the two functions (d1 and d2) across all x, considering the intervals where they apply.

Alternatively, for each x, the d1(s) is active for s <= p_x. The minimal d1 for s is | (i_x - p_x) + s |. The minimal of this for s in [0, p_x] is zero when (i_x - p_x) + s =0 → s = p_x - i_x. But if s is not in [0, p_x], then the minimal in the interval is the minimal between the endpoints and possible zero if possible.

But this seems complicated.

Alternative approach: For each x, the contribution to a shift s can be represented as a function. So for each x, we can precompute the minimal possible distance and track for each s the minimal distance across all x.

But again, how to do this.

Wait, let's think of the problem in terms of events. For each x, we can generate events on the s-axis that represent the minimal distance contributed by x. Then, for each s, we can compute the minimal of all x's distances.

But this seems abstract. Let's try to model this.

For each x, the distance function as a function of s is:

d(s) = min( |a + s| , |b - s| ), where a = i_x - p_x, and b = i_x - p_x +n.

Wait, no. Because:

In the case where s <= p_x: d(s) is |a + s| where a = i_x - p_x.

In the case where s > p_x: d(s) is |b - s| where b = i_x - p_x +n.

So for each x, the distance function is the minimum between two absolute value functions, but each applies to a certain interval of s.

But how to combine all x's contributions.

Alternative idea: For each x, the minimal distance over s is zero when s = s_x. So the shifts where some x contributes zero are the ones where the answer is zero. For other shifts, the answer is the minimal non-zero distance from all x.

But when s is not s_x for any x, then for each x, compute the minimal between |a + s| and |b - s|, and take the minimum across all x.

But how to compute this efficiently.

Alternatively, for each x, the minimal possible distance when s is not s_x is 1. But that's not necessarily true. For example, in the first sample input, when shift is 1, the answer is 1. Because in that case, the two elements are 1 and 2. The positions of 1 in a is 0 (0-based?), in b it's position 1. For shift 1 (s=0), the position in shifted array is (1 -0) mod 2 =1. So distance is |0-1|=1. For 2 in a, it's in a's position 1, and in b's position 0. For shift 1, the position in shifted array is (0-0) mod 2 =0. Distance is |1-0|=1. So the minimal is 1.

But in the second shift (s=1), for x=1 in a (position 0), the position in shifted array is (1 -1) mod 2=0. So distance is 0. So the answer is 0.

So for shifts where no x has s_x =s, the minimal distance is at least 1.

But how to compute this minimal.

Another Idea: For each shift s where there's no x with s_x = s, the answer is the minimal of the minimal distances contributed by each x. Each x contributes two possible distances (d1 and d2), and for each x, the minimal of the two is taken. Then the answer is the minimal among all these minima.

But for a given s, how to compute the minimal of min(d1, d2) for all x.

But how can we compute this for all s efficiently.

Wait, the minimal of min(d1, d2) for each x and s is the same as the minimal of all d1(s) and d2(s) for all x.

But since d1 and d2 are functions of s, we can precompute for each s the minimal among all x's d1(s) and d2(s).

But how to compute this.

Alternatively, for each x, we can compute two events:

- For all s where d1(s) is the active function (s <= p_x), compute the minimal d1(s) in that range.

- For all s where d2(s) is the active function (s > p_x), compute the minimal d2(s) in that range.

But this seems complicated.

Alternative approach: For each x, the function d(s) can be written as:

d(s) = min( |s + (i_x - p_x)|, |s - (i_x - p_x +n)| )

But since n is fixed, (i_x - p_x +n) can be written as (i_x - p_x +n) mod n. Wait, no. Because (i_x - p_x +n) is not modulo n. It's a positive value.

Wait, but (i_x - p_x) can be negative. For example, if i_x is 0 and p_x is 3 (in a 4-element array), then (i_x - p_x) is -3, and (i_x - p_x +n) is 1 (if n=4). So (i_x - p_x +n) is (i_x - p_x) mod n plus n? Not sure.

But regardless, for a given x, the two terms are |s + a| and |s - b|, where a = i_x - p_x, and b = i_x - p_x +n.

So for each x, the minimal of |s + a| and |s - b| for s in [0, n-1].

But since s ranges over [0, n-1], and a can be negative or positive.

The minimal between the two is the minimal of these two absolute values.

But how can we precompute this for all s.

Another Idea: For each x, the two functions |s + a| and |s - b| can be visualized as V-shaped graphs. The minimal between them is the lower envelope of these two Vs.

But how to combine the lower envelopes of all x's into a single minimal for each s.

But this seems challenging. Let's think of each x as contributing two possible values for each s: the two distances. The minimal for s is the minimal of all possible values (each x contributes either d1 or d2, whichever is active, but for x, the active function depends on s's relation to p_x).

But again, it's not clear how to model this.

Alternative Idea: For each x, the minimal distance over s is the minimum between the two possible distances. However, for shifts where x's s_x is not present, the minimal distance may be 1.

Wait, but this is not necessarily true. For example, if x has a= -3, then for s=0, |0 + a|=3. For s=3, |3+ (-3)|=0. So if s=3 is allowed (i.e., if x's p_x >=3), then this would be the s_x for x. Otherwise, perhaps it's not.

But perhaps we can find for each x, the minimal possible distance it can contribute when s is not s_x.

But how does that help.

Alternatively, let's precompute for each x the two possible values of s where the distance is 1 (if possible). For example, the minimal distance is 1 when s is s_x ±1, but perhaps modulo n.

But this may not be the case.

Alternatively, perhaps for each x, the minimal possible distance is 1 if there exists some s where the distance is 1. But again, this is not helpful.

Let me think of the problem in terms of the possible answers.

The possible answers for each shift s can be:

- 0 if there exists any x with s_x = s.

- Otherwise, the minimal distance is the minimal of the minimal distances from all x's for that shift.

But how to compute that minimal.

Wait, but perhaps for each x, when s is not s_x, the minimal possible distance contributed by x is at least 1. So when there's a shift s with no x having s_x =s, the answer is the minimal of the distances contributed by each x for that s.

But even this requires O(n) per s, which is O(n^2) time. Which is not feasible.

So we need a way to precompute for each s the minimal distance among all x's, but in O(1) per s after some preprocessing.

An alternative approach is to precompute for each s:

- Check if there's any x with s_x = s. If yes, output 0.

- Else, find the x that gives the minimal distance for s. How?

But how to find this x quickly.

Perhaps we can precompute for each s the minimal distance, assuming that there are no x's with s_x =s.

But even this requires a way to compute the minimal for each s efficiently.

Let's think of the minimal distance for s when there's no x with s_x =s.

The minimal distance would be the minimal over all x of min( |s + a_x|, |s - b_x| ), where a_x = i_x - p_x, and b_x = i_x - p_x +n.

We can rewrite this as:

min( |s + a_x|, |s - (b_x)| )

But since a_x and b_x are linked: b_x = a_x +n.

So for each x, the two possible terms are |s + a_x| and |s - (a_x +n)|.

But since s ranges from 0 to n-1, perhaps we can find for each s the minimal among all x's of these two terms.

But how.

Another Idea: For each x, the two terms are |s - (-a_x)| and |s - (a_x +n)|. So each x contributes two possible points on the number line: -a_x and a_x +n. The minimal distance from s to either of these two points.

So the minimal of |s - (-a_x)| and |s - (a_x +n)| is the minimal distance between s and the closer of the two points (-a_x) and (a_x +n).

But since s is in [0, n-1], and the two points are:

- Point1 = -a_x.

- Point2 = a_x +n.

But a_x can be any integer. So for example, if a_x is negative, Point1 is positive, and Point2 is a_x +n.

Alternatively, the two points can be rewritten as:

Point1 = - (i_x - p_x) = p_x - i_x.

Point2 = (i_x - p_x) +n.

But how do these points relate to the range of s (0 to n-1)?

For example, let's take a_x = i_x - p_x. Then:

Point1 is p_x - i_x.

Point2 is a_x +n = i_x - p_x +n.

But since p_x and i_x are between 0 and n-1, a_x ranges from -(n-1) to (n-1).

So Point1 can be as low as 0 (if i_x = p_x) to as high as 2(n-1) (if i_x is 0 and p_x is n-1).

Wait, for example, if i_x is 0 and p_x is 3 (n=4), then a_x is -3. Point1 is 3, and Point2 is -3 +4=1.

So for s in 0-3, the distance from x is the minimal of |s -3| and |s -1|.

The minimal of those two is the minimal distance between s and either 3 or 1.

So the minimal for x is the minimal of the two distances.

But for s in [0,3], the minimal between |s-3| and |s-1| is min(3-s, s-1) if s >=1, but otherwise depends.

Wait, for s=0: distance is min(3, 1) →1.

s=1: min(2,0) →0.

s=2: min(1,1) →1.

s=3: min(0, 2) →0.

So for this x, the minimal distances are 1,0,1,0.

But this is for each shift s. So for each x, the minimal distance for s is the minimal of the two distances between s and either Point1 or Point2.

But the problem is that for each s, we need to find the minimal of all x's minimal distances (between their two points and s).

But how to model this.

Another Idea: For each x, the minimal distance between s and the two points (Point1 and Point2) is equivalent to the minimal distance between s and the set {Point1, Point2}.

So the problem reduces to, for each s, find the minimal distance to any of the points in the union of all x's {Point1, Point2} sets.

But this is only true if for each x, the minimal distance for s is the minimal between the two points. But wait, for x, the minimal distance is either |s + a_x| or |s - (a_x +n)|, but these are exactly the distances between s and Point1 (-a_x) and Point2 (a_x +n).

So for each x, the minimal distance for s is the minimal between the distance from s to Point1 and the distance from s to Point2.

Therefore, the overall minimal distance for s (when there's no x with s_x = s) is the minimal distance between s and any of the points in the union of all x's Point1 and Point2.

So the problem reduces to: for each s in 0..n-1, if there's any x with s_x = s, output 0. Else, output the minimal distance between s and any of the 2n points (each x contributes two points).

But how to compute this efficiently.

This is a classic nearest neighbor problem. For each s, find the minimal distance to any of the points in a set of size 2n. But for n=1e5, this set would have 2e5 points. We need a way to answer for each s in O(1) or O(logn) time.

This is possible by building a sorted list of all the points and using binary search to find the closest points to s.

But the points can be in any range. Wait, but s is between 0 and n-1. So the points that are relevant are those that are in or around this interval. But since the points can be anywhere, we can modulo them into the [0, 2n) range.

Wait, but the points can be arbitrary. However, the minimal distance between s and a point p can be computed as the minimal of |s - p| and |s - (p + n)| and |s - (p -n)|, but this seems complicated.

Alternatively, we can consider the problem in the circular arrangement. Since the shifts are modulo n, perhaps the minimal distance can be considered as the minimal of |(s - p) mod n| and |(s - p +n) mod n|, but I'm not sure.

Alternatively, for each point p in the set, the minimal distance to s is the minimal of |s - p| and |s - p + n| and |s - p -n|, but this is only when considering the circular nature of the shifts. But since s is in [0, n-1], and the points can be any integer, but the minimal distance is the minimal of |s - p| and |s - (p mod n)|.

Wait, perhaps not. For example, if p is 2n +5, then the minimal distance would be |s -5|.

But since s is in 0..n-1, the minimal distance between s and p can be computed as the minimal between |s - (p mod n)| and |(p mod n) -s -n|, whichever is smaller.

Alternatively, since we can model all points modulo n, but that depends on the actual value of p.

This seems complicated.

But if we can arrange all points in a way that wraps around the [0, n) interval, perhaps using modulo operations, then we can manage.

Alternatively, since the minimal distance between s and p is min( |s-p|, n - |s-p| ), but this is when considering that the shifts are cyclic. Wait, but in our case, the s is in [0, n-1], and the distance is measured as the absolute difference. Because the positions are in the same permutation, which is of length n, the minimal distance between positions i and j is min( |i-j|, n - |i-j| ), but no, that's not the case. For example, in a permutation of length 4, positions 0 and 3 are distance 3, but the minimal is 1 (3 vs 4-3=1). Wait, no. Wait, the problem defines the distance as the absolute difference of the positions. So for positions 0 and 3 in a permutation of length 4, the distance is 3. The problem does not consider it as a circular distance. So the minimal distance between positions i and j is |i-j|.

But in our case, the points p can be outside the range [0, n-1], but when we compute |s - p|, it's the actual distance in the integer line, not modulo n. So for example, if s=0 and p= n+1, the distance is 1 (because s=0, p= n+1, but modulo n, p is 1, so |0-1|=1. But according to the problem's definition, the distance is 0+1 =1 (since the shifted position is 1, and a's position is 0). But no, the actual distance is |0 -1|=1.

Wait, this is getting a bit messy. Let's go back to the problem.

The distance between a's position i and the shifted position of x is |i - ((p_x - s) mod n)|.

But the shifted position is (p_x - s) mod n. So this is equivalent to (p_x - s + kn) for some k such that the result is in [0, n-1]. So the shifted position is (p_x -s) mod n, which can be negative. For example, if p_x=1, s=3, n=4: (1-3) mod 4 is (-2) mod 4 = 2. So the shifted position is 2.

But the absolute difference between i and this shifted position is what we need.

But when we model the points as Point1 and Point2, these are:

Point1 = p_x - i_x.

Point2 = i_x - p_x +n.

But wait, a_x = i_x - p_x.

So Point1 = p_x - i_x = -a_x.

Point2 = a_x +n.

So for each x, the two points are -a_x and a_x +n.

The distance from s to Point1 is |s - (-a_x)| = |s +a_x|.

The distance from s to Point2 is |s - (a_x +n)|.

So for x, the minimal of these two is the minimal between the two distances.

But these two points can be anywhere on the number line. So for example, if a_x is -3, Point1 is 3, and Point2 is -3 +n. If n=5, then Point2 is 2.

But s is between 0 and 4.

So the distance between s and Point1 (3) is |s-3|. The distance between s and Point2 (2) is |s-2|. So for this x, the minimal distance is the minimal between these two for each s.

So the minimal distance contributed by this x is min( |s-3|, |s-2| ), which varies per s.

But how to find the minimal over all x for each s.

This seems like a problem of having 2n points and needing to find the closest point to s for each s in [0, n-1].

To solve this efficiently, we can build a sorted list of all points (from all x's Point1 and Point2), and for each s, perform a binary search to find the closest points and compute the minimal distance.

But with 2e5 points (n=1e5), building a sorted list and performing a binary search for each s (n=1e5) would take O(2n log 2n) time for sorting and O(n log 2n) for queries, which is feasible.

So the steps are:

1. Preprocess for each x:

   a. Compute s_x = (p_x - i_x) mod n. If there's any x with s_x = s, then the answer for s is 0.

   b. Compute Point1 and Point2 for x.

2. Build a set (sorted list) of all these points (Point1 and Point2 for all x).

3. For each shift s:

   a. Check if s is in the s_x set. If yes, output 0.

   b. Else, find the minimal distance between s and any point in the sorted list. Output that minimal distance.

But this approach is incorrect. Because for x's contribution, the minimal distance for s is the minimal between the two points (Point1 and Point2) for that x. But by collecting all points and finding the minimal distance to any point, we are taking the minimal over all points from all x, which may include both Point1 and Point2 for different x's. However, this is correct because for each x, the minimal distance contributed by x is min(distance to Point1, distance to Point2). The global minimal distance for s is the minimal of all x's minimal distances. But this is the same as the minimal distance from s to any of the 2n points (because for each x, the minimal is either distance to Point1 or Point2 for that x, and the global minimal is the smallest of all these).

So this approach would work.

But how to efficiently compute this.

Yes. So, for each s, if there's any x with s_x = s, output 0. Otherwise, find the minimal distance between s and any of the 2n points (Point1 and Point2 for all x), and output that minimal.

But how to compute this.

The way to do this is to sort all the points and, for each s, perform a binary search to find the insertion point in the sorted list. The closest points are either the one before or after the insertion point. Compute the minimal distance between these candidates and s.

So, here's the plan:

- Precompute for each x, s_x. Create a frequency array or a hash set to check for each s whether there's any x with s_x =s.

- Precompute for each x, Point1 and Point2. Collect all these points into a list.

- Sort this list.

- For each s from 0 to n-1:

   a. If s is in the s_x set, output 0.

   b. Else, compute the minimal distance between s and any point in the sorted list. This minimal distance is the answer.

But how to handle points that are outside the 0..n-1 range? For example, Point1 could be 1000 for a certain x. But when s is 0, the distance to Point1 is 1000. But the minimal distance between s and Point1 is 1000, but there may be other points closer.

But the sorted list approach will correctly find the minimal distance regardless of where the points are.

So the steps in code:

1. Read n, a, b.

2. Create pos_b: a dictionary mapping each value in b to its index (0-based).

3. For each x in a, compute its index i in a (0-based), and its position p in b (pos_b[x]).

4. For each x, compute s_x = (p - i) mod n. Add all s_x to a set or a frequency array.

5. For each x, compute a_x = i - p. Then, Point1 = -a_x (since a_x is i-p, so Point1 = p-i). Point2 = a_x +n = (i-p) +n.

6. Collect all Point1 and Point2 into a list, then sort it.

7. For each s in 0..n-1:

   a. If s is in the s_x set, output 0.

   b. Else, find the minimal distance between s and any point in the sorted list. Output that distance.

But how to handle the sorted list efficiently.

The sorted list can have duplicates. For example, multiple x's can have the same Point1 or Point2.

But duplicates don't matter because we need the minimal distance.

So, code steps:

Implement the above steps.

Now, for the binary search part.

Implement a function to find the minimal distance from s to the sorted list.

In Python, the bisect module can be used.

For example, sorted_points is the sorted list of all points.

For a given s, using bisect.bisect_left to find the insertion index.

Then, check the elements at index idx-1 and idx (if they exist) and compute the minimal distance.

But the points can be anywhere on the number line. So even if the insertion index is at 0, we need to compare with the last element as well (wrapping around if necessary). Because the list is sorted, but if the s is at the beginning, the minimal distance could be to the last element (if the list contains a point near n).

Wait, no. Because the list is sorted, the last element is the largest point. So if s is 0 and the list has a point 1000, then the minimal distance is 1000-0. But if there's a point at 3, then the minimal is 3-0. But in the sorted list, the points before the insertion index are <= s, and the points after are >= s.

But when the insertion index is 0, the closest is the first element.

When the insertion index is len(sorted_points), the closest is the last element.

Otherwise, check the elements at idx-1 and idx.

But this works only for points in the list. However, if the list contains points that are much larger than n, then the minimal distance could be to the first or last element, depending on s.

But the code will correctly find the minimal distance between s and any point in the list.

So, for example, if the list contains 10,000 and s is 5, then the code would find that the minimal distance is 10,000 -5. But perhaps there's a closer point in the list.

But the binary search approach is correct.

Now, testing with the sample input.

Sample Input 1:

2

1 2

2 1

The a array is [1, 2], and the b array is [2, 1].

pos_b is {2:0, 1:1}.

For each x in a:

For x=1: i=0, p=1. a_x =0-1 = -1. s_x = (1-0) mod 2 =1.

Point1 = -a_x =1. Point2 = a_x +n =-1+2=1.

So points are 1 and 1.

For x=2: i=1, p=0. a_x=1-0=1. s_x=(0-1) mod 2= ( -1) mod 2=1.

Point1= -1. Point2=1+2=3.

So points are 1,1, -1,3.

sorted_points is [-1, 1,1,3]

Now, for s=0:

Check if s is in s_x set. s=0 is not present (all s_x are 1). So find minimal distance between 0 and any of the points.

The closest points are -1 and 1. The distances are 1 and 1. So the minimal is 1.

So output is 1.

For s=1:

Check if s is in s_x set. Yes, both x's have s_x=1. Output 0.

Sample output is 1 and 0, which matches the first sample.

Sample Input 2:

4

2 1 3 4

3 4 2 1

a is [2,1,3,4]

b is [3,4,2,1]

pos_b is {3:0,4:1,2:2,1:3}.

For each x:

x=2: i=0, p=2 (since x=2 is at position 2 in b). a_x=0-2= -2. s_x = (2-0) mod4=2.

Point1 = 2, Point2= (-2)+4=2.

x=1: i=1, p=3. a_x=1-3= -2. s_x=(3-1) mod4= 2. Point1=2, Point2= -2+4=2.

x=3: i=2, p=0. a_x=2-0=2. s_x=(0-2) mod4= 2. Point1= -2, Point2= 2+4=6.

x=4: i=3, p=1. a_x=3-1=2. s_x=(1-3) mod4= ( -2) mod4=2. Point1= -2, Point2=2+4=6.

So all x's have s_x=2. But in the sample input, the output for shifts 1,2,3,4 is 2,1,0,1. But according to this, for shift 3 (s=2?), output is 0. Wait, but in the sample input, the third shift's output is 0. Let's see:

Wait, the shifts are numbered from 1 to n. For the sample input 2, when shift is 3, s =3-1=2 (since shift 3 is s=2 in 0-based). So for s=2, the code checks if s is in the s_x set, which is all 2. So yes, output is 0. Which matches the third line of the sample output.

But according to the code's approach, for all shifts except s=2 (0-based?), the code will compute the minimal distance from the sorted list.

But the sorted list for sample input 2:

Points for x=2: 2,2.

x=1: 2,2.

x=3: -2,6.

x=4: -2,6.

So all points are: 2,2,2,2, -2,-2,6,6.

sorted_points is [-2,-2,2,2,2,2,6,6].

For s=0 (shift 1, 0-based s=0):

Check if s=0 is in s_x set (all 2). No. So compute minimal distance between 0 and any point in sorted_points.

The closest points are -2 and 2.

distance to -2 is 2. distance to 2 is 2. So minimal is 2. Which matches the sample output's first line (shift 1's output is 2).

For s=1 (shift 2, 0-based s=1):

Check if 1 is in s_x (2). No. The closest points are 2 (distance 1) and -2 (distance 3). So minimal is 1. Which matches the sample's second line.

For s=2 (shift 3, 0-based s=2): it's in s_x set. Output 0.

For s=3 (shift 4, 0-based s=3):

Check if 3 is in s_x (2). No. Closest points are 2 (distance 1) and 6 (distance 3). Minimal is 1. Which matches the fourth line.

So the code works for the sample.

Now, the code steps:

Read n.

Read a as a list of integers.

Read b as a list of integers.

Create pos_b as a dictionary: for i in range(n), pos_b[b[i]] = i.

Compute s_x for each x in a: for each i, x = a[i], p = pos_b[x], s_x = (p - i) % n.

Check for each s in 0..n-1 whether any x has s_x =s. If yes, output 0.

Else, compute the minimal distance between s and any of the points (Point1 and Point2 for all x).

Now, how to efficiently check if s is present in s_x.

We can create a list (or a set) of s_x values. For example, a frequency array or a hash set. Since n is up to 1e5, a frequency array is feasible.

But for Python, using a set is more efficient in terms of memory and checking.

So:

s_x_set = set of all s_x for x in a.

Then, for each s in 0..n-1, check if s is in s_x_set.

Now, for the points:

points = []

for each x in a:

   i = index in a (0-based)

   p = pos_b[x]

   a_x = i - p

   point1 = -a_x

   point2 = a_x + n

   points.append(point1)

   points.append(point2)

sorted_points = sorted(points)

Once sorted, for each s, perform a binary search.

Now, code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    pos_b = {val: i for i, val in enumerate(b)}

    s_x_set = set()

    points = []

    for i in range(n):

        x = a[i]

        p = pos_b[x]

        s_x = (p - i) % n

        s_x_set.add(s_x)

        a_x = i - p

        point1 = -a_x

        point2 = a_x + n

        points.append(point1)

        points.append(point2)

    sorted_points = sorted(points)

    for s in range(n):

        if s in s_x_set:

            print(0, file=output_stream)

        else:

            idx = bisect.bisect_left(sorted_points, s)

            min_dist = float('inf')

            # Check idx and idx-1

            if idx >0:

                min_dist = min(min_dist, abs(s - sorted_points[idx-1]))

            if idx < len(sorted_points):

                min_dist = min(min_dist, abs(s - sorted_points[idx]))

            # Also check wrap-around for cases where the list is cyclic, but not sure

            # But according to the previous sample, this approach works.

            print(min_dist, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
2 1 3 4
3 4 2 1
""",
            "output": \
"""\
2
1
0
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

For s=1:

Check if 1 is in s_x_set. Yes. output 0.

So the code works for the first sample.

The second sample:

n=4.

a: [2,1,3,4]

b: [3,4,2,1]

pos_b: 3:0,4:1,2:2,1:3.

For each i:

i=0, x=2:

p=2.

s_x = (2-0) mod4=2.

a_x=0-2=-2.

point1=2, point2=-2+4=2.

i=1, x=1:

p=3.

s_x=(3-1) mod4=2.

a_x=1-3=-2.

point1=2, point2= 2.

i=2, x=3:

p=0.

s_x=(0-2) mod4= 2.

a_x=2-0=2.

point1=-2, point2=2+4=6.

i=3, x=4:

p=1.

s_x=(1-3) mod4= 2.

a_x=3-1=2.

point1=-2, point2=6.

points = [2,2, 2,2, -2,6, -2,6].

sorted_points = [-2, -2, 2, 2, 2, 2, 6,6].

For s=0:

Check if 0 is in s_x_set (all 2). No.

bisect_left(sorted_points, 0) returns 2 (since -2 <0 <2).

Check idx=2.

sorted_points[1] (idx-1=1) is -2. distance is 0 - (-2) =2.

sorted_points[2] is 2. distance is 0-2=2.

min_dist is 2.

Which matches sample's first output line.

For s=1:

bisect_left returns 2 (since 1 is between -2 and 2). So idx=2.

Check idx-1=1: sorted_points[1] is -2. distance 3.

Check idx=2: sorted_points[2] is 2. distance 1. So min_dist is 1.

Which matches the sample's second line.

So the code works for the sample.

Now, considering the time and memory constraints.

Time:

- Building s_x_set is O(n).

- Generating points is O(n).

- Sorting 2n points is O(n log n).

- For each s in 0..n-1: O(1) check for s in s_x_set (since it's a set), and a binary search which is O(log 2n) per s.

Total time is O(n + n log n + n log n) = O(n log n), which is acceptable for n=1e5.

Memory:

- The sorted list has 2e5 elements, which is manageable.

So this code should work within the time and memory constraints.
</think>

```python
import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos_b = {val: i for i, val in enumerate(b)}
s_x_set = set()
points = []

for i in range(n):
    x = a[i]
    p = pos_b[x]
    s_x = (p - i) % n
    s_x_set.add(s_x)
    a_x = i - p
    points.append(-a_x)
    points.append(a_x + n)

sorted_points = sorted(points)

for s in range(n):
    if s in s_x_set:
        print(0)
    else:
        idx = bisect.bisect_left(sorted_points, s)
        min_dist = float('inf')
        if idx > 0:
            min_dist = abs(s - sorted_points[idx-1])
        if idx < len(sorted_points):
            min_dist = min(min_dist, abs(s - sorted_points[idx]))
        print(min_dist)
```
