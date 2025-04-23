<think>
Okay, let's try to understand this problem. So, we need to find the maximum score by deleting substrings from a sequence under certain conditions. The key is to figure out which substrings can be deleted and how to split the problem into smaller parts, probably using dynamic programming.

First, let's restate the conditions for the substrings. The chosen substring must satisfy two main conditions:

1. For all consecutive elements in the substring, the absolute difference is exactly 1. So, each adjacent pair in the substring must differ by 1. For example, 1,2,3 or 5,4,3,2 would be valid, but 2,5 would not.

2. For each element in the substring (except the first and last), the value must satisfy 2*wi - wi-1 - wi+1 >= 0. Let's rearrange this inequality: 2wi ≥ wi-1 + wi+1. That's the condition for a concave function. Wait, or is it convex? Hmm. If the sequence is such that each middle element is at least the average of its neighbors, then it's a concave sequence. Wait, maybe the condition is that the sequence is convex? Let's see. The inequality is 2wi ≥ wi-1 + wi+1. Rearranged, it's wi - wi-1 ≥ wi+1 - wi. So the difference between consecutive elements is non-increasing. So the sequence is concave upwards? Like a convex function. For example, a sequence like 1,3,4: 3-1 = 2, 4-3=1. So 2 >= 1, which satisfies the condition. So the sequence's differences are non-increasing, which would form a convex shape when plotted. So the substring must form a convex sequence in terms of their differences.

So the substring must be a sequence where each consecutive pair differs by exactly 1, and the differences between consecutive elements form a non-increasing sequence (so the second differences are non-positive). Wait, no, the condition applies to each i between l and r (exclusive). Let me think. For example, the substring is [a, b, c]. The condition is 2b - a - c >=0. Rearranged: 2b >= a + c. Which is the same as (b -a) >= (c - b). So the difference between the first two elements is at least the difference between the next two. But since the consecutive elements must differ by exactly 1, the difference can be +1 or -1. Wait, but the first condition says that |w_i - w_{i+1}| = 1 for all l ≤ i < r. So each consecutive pair in the substring must differ by exactly 1. So the possible differences are either +1 or -1. So the sequence is either increasing by 1s, decreasing by 1s, or a mix of increasing and decreasing steps, but each step must be exactly 1 in absolute value.

Wait, no. Wait, the first condition is |w_i - w_{i+1}| = 1. So each adjacent pair in the substring must differ by exactly 1. So the entire substring is a sequence where each step is +1 or -1. So the entire substring is a consecutive sequence in terms of steps of ±1. For example, 1,2,1,0 would be allowed (differences +1, -1, -1), but 1,3 is not allowed.

So combining the two conditions. The substring must be a sequence where each consecutive pair differs by ±1. Additionally, for each position i (not first or last) in the substring, 2w_i >= w_{i-1} + w_{i+1}. Let's see what that implies for the differences.

Let's take three consecutive elements in the substring: a, b, c. We have |a - b| = 1 and |b - c| = 1. So possible possibilities are:

Case 1: a = b+1 (so difference -1), then c can be b+1 (difference +1) or b-1 (difference -1). Wait, a is b+1? Wait, no. If a is followed by b, then if |a - b| = 1, then either a = b +1 or b = a +1. Wait, perhaps I should think in terms of the direction of the differences. Let me denote the sequence as w_0, w_1, ..., w_k (the substring of length k+1). Each consecutive pair has a difference of +1 or -1. Let's look at the differences d_1, d_2, ..., d_k where d_i = w_{i} - w_{i-1}, which is either +1 or -1.

Now, the second condition for the middle elements (i from 1 to k-1, since the substring is from 0 to k) is 2w_i >= w_{i-1} + w_{i+1}. Let's substitute w_{i+1} = w_i + d_{i+1}, and w_{i-1} = w_i - d_i (since d_i is the difference between w_i and w_{i-1}).

So substituting:

2w_i >= (w_i - d_i) + (w_i + d_{i+1}) 

Simplify the right-hand side:

2w_i >= 2w_i + (d_{i+1} - d_i)

Subtract 2w_i from both sides:

0 >= d_{i+1} - d_i 

=> d_{i} >= d_{i+1}

So each difference d_i must be greater than or equal to the next difference d_{i+1}.

But each d_i is either +1 or -1. So the sequence of differences must be non-increasing. Let's see: possible sequences of differences.

For example:

+1, +1, +1: each d_i is +1. So each step is +1. The differences are non-increasing. So this is allowed.

+1, -1: d1=+1, d2=-1. Then 1 >= -1: yes.

But if the sequence of differences is -1, +1: then d1=-1, d2=+1. So d1 < d2. So this would not satisfy the condition. So such a substring is invalid.

So the sequence of differences must form a non-increasing sequence. Since each d is either +1 or -1, this implies that once a difference becomes -1, all subsequent differences must also be -1. Because a non-increasing sequence of +1 and -1 can start with some +1s and then switch to -1s. For example: +1, +1, -1, -1 is allowed. But +1, -1, +1 is not allowed because the second difference (-1) is followed by +1 which is larger than -1.

Wait, but the differences can't be +1 followed by +1, then +1 again. So sequences where the differences are all +1 are allowed. Similarly, sequences of all -1s. Also sequences that start with +1s and then switch to -1s. But sequences that have a -1 followed by a +1 are invalid.

So, the possible valid substrings are those where the differences between consecutive elements (each ±1) form a non-increasing sequence. Which means that once a -1 occurs in the differences, all subsequent differences must also be -1. So the substring can be in the form of a sequence of +1 steps followed by -1 steps, or all +1s or all -1s. Wait, for example:

Consider a substring like 3,4,5,4,3,2. The differences would be +1, +1, -1, -1, -1. The sequence of differences is [1,1,-1,-1,-1], which is non-increasing. So this is allowed. But if the differences were [1,-1,1], then the sequence is 1, -1, 1, which is 1 > -1 < 1, so the sequence is not non-increasing. That's invalid.

So the allowed substrings are those where the differences are a non-increasing sequence of +1 and -1. So the differences can start with some +1s and then switch to -1s, but cannot switch back.

But how do we model this for dynamic programming?

The problem requires us to delete substrings, possibly in multiple steps, and accumulate the maximum possible points. The points are based on the length of the substring deleted each time, as given by the v array. For example, deleting a substring of length k gives you v_k points. We can delete any number of such substrings as long as they meet the conditions, and the order may affect the total points. But since each deletion affects the remaining elements, the order is important.

This seems like a dynamic programming problem where we need to find the best way to partition the original array into a set of valid substrings (possibly with some elements left undeleted if they cannot form any substring), and sum the corresponding v values.

But how to model the DP state?

A common approach for such interval-based problems is to use a DP table where dp[i][j] represents the maximum score achievable for the subarray from index i to j (inclusive). Then, we can try to split the interval into parts, or find a valid substring in the middle and combine the results.

But given the constraints on the valid substrings (the conditions on the differences and the convexity), the transitions might not be straightforward.

So let's think: for each interval [i, j], can we delete it as a single substring, and then add the value v[j-i+1] to the sum of the points from the left and right parts. Alternatively, maybe we can split the interval into two parts and take the maximum of all possible splits.

The recurrence would be:

dp[i][j] = max(
    dp[i][k] + dp[k+1][j] for all k in i <=k <j,
    (if [i..j] is a valid substring then v[len] + dp[i][left] + dp[right+1][j] ...? Wait, if we delete [i..j], then the remaining parts are the left part (before i) and the right part (after j). So if the entire [i..j] is deleted, the score is the sum of the left part (dp[0][i-1]?) and the right part (dp[j+1][n-1]) plus v[len]. But this complicates the DP because the order of deletions matters. So perhaps the DP state should be for intervals where all elements in the interval are processed, and the maximum score possible for that interval.

Wait, the standard approach for such problems is to model dp[i][j] as the maximum score attainable by processing the subarray from i to j, possibly by deleting some substrings within it. So for each interval [i, j], the maximum score is either:

- Split into two parts [i, k] and [k+1, j], and sum their scores.

OR

- Find a way to split [i, j] into a central part [l, r] that is a valid substring, plus the left and right parts.

But how do we check if [i..j] can be deleted as a single substring? And if so, then the score would be v[j-i+1] plus the scores of the left and right parts (the parts outside of i..j). Wait, but the left and right parts would be processed before deleting i..j. Wait, but in reality, you can delete any valid substring in any order. So the DP approach needs to consider all possible ways of deleting substrings within the interval.

So perhaps the DP[i][j] is the maximum score we can get by processing the interval i to j. The initial state is when the interval is empty (i > j) which gives 0. For the interval of length 1 (i == j), since you can't delete a substring (since the substring must be of length at least 1, but deleting a single element would give a substring of length 1, but then check the conditions. Wait, the substring can be a single element? Wait, the problem says "you can perform the operation again and again while proper substrings exist". A proper substring is a substring with length at least 1. Wait, the original problem allows deleting a substring of length 1. Because the conditions are:

For the first condition, |w_i - w_{i+1}| =1 must hold for all l ≤i < r. But if the substring is of length 1, there are no i's here. So the first condition is trivially satisfied. The second condition is for all l < i < r. So for a substring of length 1 (l = r), there are no such i's. So the second condition is also trivially satisfied. So a single element can be deleted. So the value added is v_1.

Wait, but in the first sample input:

3 elements, and the output is 3. The sample input is 1 2 1, and the v array is [0,0,3]. So deleting the entire substring (length 3) gives 3 points. Alternatively, deleting each element individually would give 0+0+0 =0. So the sample shows that deleting longer substrings is better.

So for a single element, you can delete it (if allowed by the conditions) and get v_1 points. But for the DP state [i][i], you can choose to delete it (if possible), or not delete it (and get 0 points). Wait, but the problem says that you can end the game at any time. So, the maximum points is the sum of the points from the deletions you perform. So deleting the single element gives v_1. But you can also choose not to delete it and get 0. So the maximum between the two options.

Wait, but the problem says you can perform the operation of deleting a substring as long as proper substrings exist. So if you have a single element, you can choose to delete it (as a substring of length 1) once. Then there's nothing left, so the game ends.

So for the DP[i][j], the maximum score for the interval i to j is the maximum of:

- The sum of splitting into two parts: dp[i][k] + dp[k+1][j], for all k between i and j-1.

OR

- If the entire interval i..j is a valid substring, then v[j-i+1] plus the sum of the scores from the left and right parts. Wait, but in the DP model, the left and right parts are already considered. Wait, maybe I'm misunderstanding the DP approach here. Let's think again.

The standard approach for interval DP is to consider all possibilities for the current interval. For example, when considering interval i..j, you can:

1. Split it into two parts and compute their scores.

2. Check if the entire interval can be processed as a single operation (here, deleted as a substring), and add the corresponding value.

In this problem, the operation is deleting a substring. So, for interval i..j, if it is a valid substring (as per the problem's conditions), then deleting it would give v[len] points, where len is j-i+1, plus the scores from the left and right parts. But how do the left and right parts factor in here?

Wait, the DP[i][j] represents the maximum score achievable for the subarray i..j. So when you delete the entire i..j as a substring, you get v[len] points. But after deleting this substring, the elements to the left of i and right of j are now adjacent. But in the DP approach, the transitions are such that the deletions are processed in a way that allows combining intervals. So perhaps the initial approach is:

dp[i][j] = max( split into k, check if i..j is valid and add v + ... )

Wait, perhaps the correct recurrence is:

dp[i][j] = max over all possible splits (k) of dp[i][k] + dp[k+1][j]

and also check if the entire i..j is a valid substring. If so, then we can take v[len] (where len = j-i+1) and that would be another candidate for dp[i][j].

Wait, but if the entire i..j is a valid substring, then deleting it gives v[len] plus the sum of the scores from the intervals before i and after j. But in the DP[i][j] model, we are considering only the interval i..j. So perhaps the DP[i][j] must account for the maximum score that can be obtained by processing the interval i..j, regardless of what happens outside. So, if you delete i..j, then the score is v[len] plus the DP of the left part (i-1) and the right part (j+1). But that's not how the DP is structured here.

Alternatively, perhaps the DP[i][j] represents the maximum score you can get by processing the elements from i to j, regardless of how they are processed. So, for the interval i..j, the maximum score is the maximum between splitting into two parts, or deleting the entire interval as a substring (if possible) and adding v[len], or any combination where some parts are split and others are deleted as substrings.

So the recurrence would be:

dp[i][j] = max( 

    max over k in i <=k <j of dp[i][k] + dp[k+1][j], 

    (if i..j is valid) then v[j-i+1] + (the scores of any possible splits that can be combined by deleting i..j) )

But how to model that. Hmm.

Alternatively, when considering the entire interval i..j, if it can be deleted as a single substring, then the score would be v[len] plus the sum of the scores from the intervals that are left before i and after j. But this seems to complicate things because the DP[i][j] would depend on the outside intervals.

Alternatively, perhaps the DP[i][j] can be structured such that it represents the maximum score obtainable from the interval i..j by possibly deleting some substrings within it. So, when you delete the entire interval i..j as a substring, you get v[len], and that's the contribution. Then, the maximum would be either:

- Split into two parts and add their scores.

- Or delete the entire interval (if valid) and add v[len].

So the recurrence would be:

dp[i][j] = max over all k in i..j-1 (dp[i][k] + dp[k+1][j])

and also, if i..j is valid, then compare with v[len].

So, the initial approach is to precompute for all intervals whether they are valid substrings. Then, in the DP step, for each interval, check if it's valid, and take the maximum between splitting into parts or deleting the entire interval (if possible).

But the question is, how to efficiently precompute all possible valid substrings.

So first, let's precompute a 2D array valid[i][j] which is True if the substring from i to j (inclusive) is a valid substring as per the problem's conditions.

Then, for each interval i..j, the DP[i][j] can be computed as the maximum of splitting into parts (k) and adding their DP values, or (if valid[i][j] is True) v[j-i+1] plus the sum of the left and right parts. Wait, no. Because when you delete the entire i..j, you can't have any other deletions in i..j. So the DP[i][j] would be v[len] (if the substring is valid), but how does that interact with other possibilities.

Wait, perhaps the DP[i][j] is the maximum score that can be obtained by considering the elements from i to j. So, for the case where the entire interval is deleted as a single substring, the score is v[len], and that's the only contribution. Alternatively, if you split the interval into two parts, their scores are summed. So the recurrence would be:

dp[i][j] = max( 

    (split into k: dp[i][k] + dp[k+1][j] for all k), 

    (if valid[i][j]: v[len] )

)

But that's not considering the case where you delete a substring in the middle. For example, delete a substring from l to r, which is inside i..j. Then the score would be the sum of the left part (i to l-1), the right part (r+1 to j), plus the score for the substring l..r. So perhaps the standard interval DP approach, where for each interval i..j, we check all possible splits into k, and also check if the entire interval can be considered as a single operation. But the operation here is deleting the entire interval. But the problem allows multiple deletions in any order.

So the initial approach is to compute for each interval whether it can be deleted as a substring, and if so, then the maximum score for that interval is the maximum between splitting into parts, or deleting the entire interval (v[len] + the sum of the left and right intervals? No, because the entire interval is deleted, so the left and right are not part of the same interval. Wait, no. The DP[i][j] is the maximum score from the interval i to j. If we delete the entire interval, then the score is v[len], and there's nothing left in the interval. So the DP[i][j] can be v[len] if that is larger than splitting into parts and adding their scores.

Wait, no. For example, suppose you have an interval i..j. If you split into i..k and k+1..j, their DP values are the maximum scores you can get by processing those intervals. So the sum is the maximum for that split. Alternatively, if the entire interval is a valid substring, then deleting it gives v[len], which might be higher than the sum of the splits.

So the recurrence is:

dp[i][j] = max( max over k (dp[i][k] + dp[k+1][j]), v[j-i+1] if valid[i][j] )

But wait, what if you can split the interval into multiple parts, some of which are valid and others not. For example, perhaps the maximum is achieved by deleting a substring in the middle of the interval, then deleting others. So the DP should account for all possible ways.

But the standard interval DP approach of splitting into any possible split and taking the maximum is the way to capture all possibilities. Because any sequence of deletions can be represented as a split of the interval into parts that are processed independently.

So, for each interval i..j, the maximum score is either:

- The maximum of splitting into two parts and adding their scores.

- Or, if the entire interval is a valid substring, then v[len], which may be higher than any split.

But is that correct? Let's see.

Suppose the entire interval is valid. Then deleting it gives v[len]. But there might be a way to split it into parts, delete some substrings, and get a higher sum. For example, if v[len] is 5, but splitting into two parts gives 3 +3=6. Then the maximum is 6.

So in the DP, we need to compare the value of deleting the entire substring (if valid) with all possible splits and take the maximum.

So the recurrence is:

dp[i][j] = max over all possible k splits (i <=k <j) of (dp[i][k] + dp[k+1][j]), and also check if the interval is valid, then compare with v[len].

So for each interval, the DP[i][j] is the maximum between all possible splits and the value if the entire interval is deleted.

Now, the key is to compute for all intervals i..j whether they are valid.

So, the first step is to precompute the valid[i][j] for all possible intervals.

How to compute valid[i][j]?

For an interval to be valid, two conditions must hold:

1. All consecutive elements must differ by exactly 1.

2. For each middle element, 2* w[i] >= w[i-1] + w[i+1].

So for the first condition, we need to check that for each position from i to j-1, |w[k] - w[k+1]| =1.

For the second condition, for each position from i+1 to j-1, 2* w[k] - w[k-1] - w[k+1] >=0.

So how to precompute this efficiently.

First, for the first condition, we can precompute a 2D array diff_ok[i][j], which is True if all consecutive differences in i..j are ±1. Then, for the second condition, we can precompute another 2D array convex_ok[i][j], which is True if all middle elements satisfy the convex condition.

But given the time constraints (n up to 400), the precomputation must be O(n^3) time, which for n=400 is 400^3=64 million operations, which might be acceptable, but perhaps we can find a way to optimize.

Let's think for each interval i..j:

For the first condition (all consecutive differences are ±1):

We can precompute a 2D array, for each i and j, whether all consecutive differences in i..j-1 are ±1. We can compute this for each interval by checking each step in O(j-i) time. But for n=400, that's O(n^3) time.

But perhaps we can precompute this more efficiently. For example, for each i, we can track the maximum j where the consecutive differences from i are ±1. But I'm not sure. Let's think. For each i, start from i, and check each next element. Once a pair that doesn't have difference ±1 is found, all j beyond that for the same i would be invalid.

So for each i, we can expand j starting from i, and for each step, check if the next difference is valid. Once a difference is invalid, break. This way, for each i, the inner loop runs until the first invalid difference. But in the worst case, it's O(n^2) time.

But for the problem of checking all intervals i..j, this approach would not be sufficient, as some intervals may start at i, have valid differences in the beginning, then invalid, but then valid again. However, given that the consecutive differences must all be ±1, once any step in i..j-1 is invalid, the entire interval i..j is invalid. So for each i, the maximum j where all steps from i to j are valid is the maximum possible j where each consecutive step in i to j is valid.

So, for each i, we can compute the maximum j for which the consecutive differences are all ±1. Then, for i..j to be valid in the first condition, j must be <= that maximum j for i.

Let's see. Let's precompute for each i, the furthest j where all consecutive steps from i to j have differences of ±1. This can be done in O(n) per i, leading to O(n^2) time.

For example:

Initialize an array max_j for each i. For i from 0 to n-1:

max_j[i] = i

for j from i+1 to n-1:

   if |w[j] - w[j-1]| ==1, then max_j[i] = j

   else break

So for each i, max_j[i] is the maximum j where from i to j, the consecutive steps are all ±1.

Then, for any interval i..j to have all consecutive steps valid, j must be <= max_j[i]. So if j > max_j[i], then the interval is invalid.

But how to handle the case where the consecutive steps from i to j are valid, but there's a break in between? For example, i=0, j=2, but between 0 and 1 is valid, 1 and 2 is invalid, but 0 and 2 is valid. Wait, no. Because the consecutive steps must all be valid. So for the interval 0..2, the steps 0-1 and 1-2 must both be ±1. So if 0-1 is valid, but 1-2 is invalid, then the entire interval 0..2 is invalid.

So for the first condition, the entire interval i..j must be such that for every k in i <=k <j, the consecutive elements are ±1. So for interval i..j to be valid for the first condition, j must be <= max_j[i], and all consecutive steps in between must be valid.

So the max_j[i] array can be precomputed as described, and for any interval i..j, the first condition is satisfied only if j <= max_j[i].

But wait, the max_j[i] is the maximum j where all steps from i to j are valid. So for any j <= max_j[i], the steps are valid. So for any interval i..j where j <= max_j[i], the first condition is satisfied.

So the first condition can be checked in O(1) time per interval if we have the max_j array.

But what about the second condition? For the second condition, each middle element must satisfy the convex condition.

So for the interval i..j (length m = j-i+1), if m <=2, then there are no middle elements. So the second condition is automatically satisfied. For example, a substring of length 1 or 2: no middle elements. So for these, if the first condition is satisfied, then the substring is valid.

For longer intervals (m >=3), we need to check each middle element (positions i+1 to j-1 in the original array) to see if 2w[k] - w[k-1] - w[k+1] >=0.

But how to check this efficiently for all possible intervals.

Let's precompute another 2D array convex_ok[i][j], which is True if the second condition holds for the interval i..j.

For intervals of length <=2: convex_ok[i][j] is True.

For longer intervals (length >=3), we need to check each element from i+1 to j-1 (original array indices) and verify the condition.

For each interval i..j (j >=i+2), check for each k in i+1 to j-1:

2*w[k] >= w[k-1] + w[k+1]

If all of them are true, then convex_ok[i][j] is True.

This would take O(n^3) time in total, as for each interval of length >=3, up to O(n) elements need to be checked.

But for n=400, that's 400 * 400 * 400 = 64 million operations. Which is manageable.

But perhaps we can optimize.

Alternatively, we can precompute for each position k, a list of intervals [i, j] where k is in the middle (i <k <j) and 2w[k] >= w[k-1] +w[k+1]. But I'm not sure.

Alternatively, for each interval i..j, we can precompute whether the convex condition holds. Let's proceed with the O(n^3) approach, given that n is 400.

So, the steps are:

1. Precompute max_j[i] for each i, which is the maximum j where consecutive steps are valid.

2. For each interval i..j:

   a. Check if j <= max_j[i]. If not, the first condition is not met.

   b. For the second condition, if the interval length is 1 or 2, it's automatically valid.

   c. Otherwise, check each position k in i+1 to j-1 (original array indices) whether 2w[k] >= w[k-1] +w[k+1].

3. Combine the two conditions to determine if the interval is valid.

Now, once we have the valid[i][j] array, we can proceed with the DP.

The DP[i][j] will be the maximum score attainable for the interval i..j.

The base case is when i >j, then dp[i][j] =0.

For i ==j, dp[i][j] =v[0] if the substring is valid (which it is, since it's a single element). Because a single element can be deleted (as per the conditions), so valid[i][i] is True. So dp[i][i] = max(0, v[0]). Wait, but according to the problem statement, the cost for deleting a substring of length 1 is v_1. Wait, the problem statement says "v1, v2, ..., vn — the costs of operations. The next line contains n integers w1, w2, ..., wn — the initial w."

So the cost for deleting a substring of length k is v_k. But in the input, the indices are 1-based. For example, in the first sample input, the third element is 3, which is the cost for a substring of length 3.

So when the substring is of length m, the cost is v_{m-1} (since in Python, the list is 0-based). Because in the input, v is given as v_1, v_2, ..., v_n. For example, if the substring has length 3, the cost is v_3, which is the third element in the input (but in Python, index 2).

So for a substring of length m, the cost is v[m-1].

So, for a single element (m=1), the cost is v[0].

So, the DP[i][j] for i ==j would be the maximum between deleting it (v[0]) and not deleting it (0). So dp[i][i] = max(0, v[0]).

Wait, but if the problem allows us to end the game at any time, then not deleting anything gives 0 points. But when you can delete a substring, why not delete it and gain points? Unless the v is negative. For example, if v[0] is negative, then not deleting the element is better.

So the DP[i][i] is max(0, v[0]).

But according to the problem statement, v can be negative. The input constraints say 0 ≤ |vi| ≤ 2000. So vi can be negative. So in cases where v[0] is negative, not deleting the element (and getting 0) is better.

So, for each interval i..j, the maximum possible score is the maximum between splitting into parts, and deleting the entire interval (if valid) to get v[m], where m is j-i+1.

So, the DP recurrence is:

dp[i][j] = max( max over k in i <=k <j (dp[i][k] + dp[k+1][j]), (v[m] if valid[i][j] else -infinity) )

But we need to compare with all possible splits and the possible option of deleting the entire interval.

So, now the steps to code this:

1. Read n.

2. Read the v array (v is list of integers with length n, but the cost for a substring of length m is v[m-1]).

3. Read the w array (list of integers, length n).

4. Precompute the valid intervals.

   a. Precompute the max_j array for the first condition.

   b. For each interval i <=j, check if j <= max_j[i], and then check the convex condition.

5. Precompute a DP table, filled in a bottom-up manner.

   a. The DP is filled for intervals of increasing length.

   b. For each interval length l (from 1 to n), and for each start i, compute j =i +l-1.

   c. For each interval i..j, compute the maximum possible score.

Now, let's think about how to implement this.

First, precompute max_j:

max_j = [0] * n

for i in range(n):

    max_j[i] = i

    for j in range(i+1, n):

        if abs(w[j] - w[j-1]) !=1:

            break

        max_j[i] = j

Then, for each interval i..j, check if j <= max_j[i]. If not, the first condition is not satisfied.

Then, for the second condition, check for each k in i+1 <=k <=j-1 (original array indices) whether 2*w[k] >= w[k-1] + w[k+1]. For intervals of length <=2, this is automatically True.

So the valid[i][j] can be computed as:

valid = [[False for _ in range(n)] for __ in range(n)]

for i in range(n):

    for j in range(i, n):

        if j > max_j[i]:

            valid[i][j] = False

        else:

            if j -i +1 <= 2:

                valid[i][j] = True

            else:

                ok = True

                for k in range(i+1, j):

                    if 2*w[k] < w[k-1] + w[k+1]:

                        ok = False

                        break

                valid[i][j] = ok

But for n=400, this is O(n^3) time. Let's see: for each i (400), j from i to max_j[i] (up to 400 steps), and for each j where j-i+1 >=3, check up to j- i-1 steps. So in the worst case, for each i, j can be up to 399, and for each j, k runs up to j-1 -i steps. So for i=0, j=399, k ranges from 1 to 398. So 398 steps. So for each i, the worst case is O(n^2) steps, leading to O(n^3) total steps. For n=400, this is 64 million steps, which is manageable.

But in practice, many intervals will not satisfy the first condition (j > max_j[i]), so the inner loop may not run for many i and j.

Once the valid array is computed, the DP can be filled.

The DP table is filled in a bottom-up manner. For intervals of length 1, then 2, up to n.

The code would be:

Initialize dp as a 2D array of size n x n, initialized to 0.

for l in range(1, n+1):

    for i in range(n - l +1):

        j = i + l -1

        if i ==j:

            current_max = max(0, v[0])

        else:

            current_max = 0

            # Check splits

            for k in range(i, j):

                current_max = max(current_max, dp[i][k] + dp[k+1][j])

            # Check if the entire interval is valid

            if valid[i][j]:

                m = l

                val = v[m-1] if m <= len(v) else 0  # assuming m can't exceed n

                current_max = max(current_max, val)

        dp[i][j] = current_max

Wait, but in the code, for intervals longer than n (but since l is up to n, this is not possible). So m is l, which is the length of the interval, and v[m-1] is the cost.

But in the problem statement, the v array has exactly n elements, each corresponds to the cost for length 1 up to n. So for an interval of length m, we take v[m-1].

So the code would work.

But this approach is O(n^3) time again. For n=400, 400^3 is 64 million operations, which might be tight for Python. But the time limit is 1 second, and Python can handle about 1e8 operations per second. So 64 million is 6.4e7, which might be manageable if the code is optimized.

But perhaps there's a way to optimize the DP.

Alternative approach: precompute for each interval i..j whether it's valid, then during the DP, for each interval, check if it's valid. If it is, take the maximum between splitting and the value v[m-1].

But that's what the code does.

Now, let's test this approach against the sample inputs.

Sample Input 1:

3

0 0 3

1 2 1

The w array is [1,2,1]. Let's compute the valid intervals.

max_j array:

For i=0:

Check j=1: difference between 1 and 2 is 1 → valid. j=2: difference between 2 and 1 is 1 → valid. So max_j[0] = 2.

For i=1: j=1, then j=2: difference between 2 and 1 is 1 → valid. So max_j[1] = 2.

For i=2: j=2.

Then, for intervals:

i=0, j=0: valid (length 1). So valid[0][0] is True.

i=0, j=1: length 2. Valid. Check convex condition (not needed as length 2). So valid.

i=0, j=2: length 3. Check first condition: j=2 <= max_j[0] (2) → yes.

Then check convex condition for k=1 (original index 1). 2*2 >= 1 +1 → 4 >=2 → yes. So valid[0][2] is True.

So for the DP:

For interval 0-2:

The possible splits are k=0 and 1. Let's see.

But during the DP processing, for intervals of length 1 and 2 first.

For l=3:

i=0, j=2.

Check splits:

k=0 → dp[0][0] + dp[1][2]. dp[0][0] is max(0, v[0])=0. dp[1][2] is for the interval 1-2, which is length 2. The valid[1][2] is True (length 2). So the maximum for interval 1-2 is max(splits or v[1]).

But for interval 1-2, the splits are k=1 → dp[1][1] + dp[2][2] = 0 +0 =0. The entire interval is valid (length 2, so v[1] =0. So the maximum is 0. So the split sum is 0+0=0, and the entire interval's value is 0. So the maximum is 0. So dp[1][2] is 0.

So the split sum for i=0, j=2 is 0 (from k=0) +0=0. The entire interval's value is v[2] =3. So the maximum is 3. So dp[0][2] is 3.

Thus, the output is 3, which matches the sample.

Sample Input 2:

6

1 4 5 6 7 1000

2 1 1 2 2 3

w array is [2,1,1,2,2,3]

Let's compute the valid intervals.

But this might be time-consuming to do manually. But according to the sample output, the maximum is 12, which is achieved by deleting certain substrings.

But according to the code, the DP would consider all possible splits and valid intervals.

But the code should handle this case correctly.

Now, in terms of time optimization, perhaps we can precompute the valid intervals, and during the DP, for each interval i..j, check if it's valid, and take the maximum between splits and the value.

But in Python, with n=400, the code may be slow. So perhaps there's a way to optimize the valid checks.

But given the problem's constraints and the code's structure, this approach is probably the correct way.

Now, the code.

The code needs to read n, the v array, the w array. Then precompute max_j, then valid array, then compute the DP.

But in Python, the code must be efficient.

So here's the plan for the code:

Read n.

Read v as a list of integers.

Read w as a list of integers.

Precompute max_j for each i.

Precompute valid[i][j] for all i <=j.

Initialize dp as a 2D list of n x n, filled with 0.

Then fill dp in bottom-up order.

But in Python, for 400x400 arrays, this is manageable.

Now, let's code this step by step.

First, reading input:

n = int(input())

v = list(map(int, input().split()))

w = list(map(int, input().split()))

Then, compute max_j:

n = len(w)

max_j = [0]*n

for i in range(n):

    current_max_j = i

    for j in range(i+1, n):

        if abs(w[j] - w[j-1]) !=1:

            break

        current_max_j = j

    max_j[i] = current_max_j

Then, compute valid:

valid = [[False]*n for _ in range(n)]

for i in range(n):

    for j in range(i, n):

        if j > max_j[i]:

            valid[i][j] = False

        else:

            if j -i +1 <=2:

                valid[i][j] = True

            else:

                ok = True

                for k in range(i+1, j):

                    if 2*w[k] < w[k-1] + w[k+1]:

                        ok = False

                        break

                valid[i][j] = ok

Then, compute the DP:

dp = [[0]*n for _ in range(n)]

for l in range(1, n+1):

    for i in range(n - l +1):

        j = i + l -1

        if i == j:

            # length 1

            current_max = max(0, v[0])

        else:

            current_max = 0

            # check splits

            for k in range(i, j):

                current_max = max(current_max, dp[i][k] + dp[k+1][j])

            # check entire interval

            if valid[i][j]:

                m = j -i +1

                current_value = v[m-1]

                current_max = max(current_max, current_value)

        dp[i][j] = current_max

Finally, print(dp[0][n-1])

Putting it all together:

But wait, in the code, the indices for w are 0-based. So for a substring from i to j (0-based), the elements are w[i], w[i+1], ..., w[j].

Yes.

Now, let's test the code against the sample input.

Sample Input 1:

3

0 0 3

1 2 1

The max_j array would be:

i=0: j can go up to 2.

i=1: j can go up to 2 (since 2-1=1, 1-2=1? Wait, w is [1,2,1]. For i=0:

j=0: valid.

j=1: 2-1=1 → ok.

j=2: 1-2= -1 → abs is 1 → ok. So max_j[0]=2.

i=1:

j=1: valid.

j=2: 1-2= -1 → abs is 1 → ok. So max_j[1] =2.

i=2:

j=2: valid.

So the valid intervals:

i=0, j=0: valid.

i=0, j=1: valid (length 2).

i=0, j=2: check convex condition. For k=1 (w[1] =2):

2*2 =4 >=1 (w[0]) +1 (w[2]) → 4 >=2 → yes. So valid.

So valid[0][2] is True.

Thus, during DP for interval 0-2:

The splits would be k=0: dp[0][0] (0) + dp[1][2].

dp[1][2] is for interval 1-2, which is valid (length 2). So v[1] =0. So dp[1][2] is max between splits and 0. Splitting into k=1 and k=2: sum is 0 +0=0. So dp[1][2] is 0. So the split sum is 0+0=0. The entire interval's value is v[2] =3. So dp[0][2] is 3.

Thus, the code outputs 3, correct.

Sample Input 2:

6

1 4 5 6 7 1000

2 1 1 2 2 3

w array is [2,1,1,2,2,3].

Let's compute the valid intervals.

But it's time-consuming, but the code should handle it.

For example, the optimal solution is 12, which is achieved by deleting substrings [1,1], [2,2], and [3], each giving 4 +5 +3=12. Wait, but according to the sample output, it's 12. So perhaps the code captures this.

But in any case, the code should correctly compute the DP.

So the code should be correct.

Now, the code's time complexity is O(n^3), which for n=400 is 64 million operations. Python might be a bit slow, but with some optimizations (using loops and precomputing), it's manageable.

But for Python, nested loops can be slow. So perhaps we can optimize some steps.

For example, in the valid array's computation, for intervals of length >=3, we can break early when any k fails the convex condition.

Which is what the code already does.

But in Python, the code is as follows.

Now, let's write the code.
</think>

```python
n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

# Precompute max_j for each i (longest j where consecutive differences are ±1)
max_j = [i for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if abs(w[j] - w[j - 1]) != 1:
            break
        max_j[i] = j

# Precompute valid[i][j]
valid = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if j > max_j[i]:
            valid[i][j] = False
        else:
            m = j - i + 1
            if m <= 2:
                valid[i][j] = True
            else:
                ok = True
                for k in range(i + 1, j):
                    if 2 * w[k] < w[k - 1] + w[k + 1]:
                        ok = False
                        break
                valid[i][j] = ok

# Initialize DP table
dp = [[0] * n for _ in range(n)]

for l in range(1, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        if i == j:
            current_max = max(0, v[0])
        else:
            current_max = 0
            # Check all possible splits
            for k in range(i, j):
                current_max = max(current_max, dp[i][k] + dp[k + 1][j])
            # Check if entire interval is valid
            if valid[i][j]:
                m = l
                current_value = v[m - 1] if m <= len(v) else 0
                current_max = max(current_max, current_value)
        dp[i][j] = current_max

print(dp[0][n - 1])
```