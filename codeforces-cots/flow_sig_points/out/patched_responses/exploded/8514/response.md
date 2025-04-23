<think>
Okay, let's see. The problem is to find the maximum k such that for every pair of indices i and j in the array, k multiplied by the absolute difference of i and j is less than or equal to the minimum of a_i and a_j. 

Hmm, so the expansion coefficient is the largest possible k where this condition holds for all possible pairs. 

First, I need to figure out how to compute this efficiently. The brute force approach would be to check all possible pairs for each k, but that's obviously impossible given n can be up to 300,000. So we need a smarter way.

Let me think about the condition k * |i-j| <= min(a_i, a_j) for all i,j. For the maximum possible k, this must hold true. So how can we model this?

The key observation is that for each pair (i, j), the maximum allowed k for that pair is floor( min(a_i, a_j) / |i-j| ). The overall maximum k is the minimum of all these values across all pairs. Because even if one pair allows a smaller k, that's the limiting factor.

Wait right. So the maximum possible k is the minimum over all possible (i, j) pairs of (min(a_i, a_j) // |i-j|). But calculating this for all possible pairs is O(n^2), which is way too slow for n=3e5.

So the problem reduces to finding the minimum value of (min(a_i, a_j) / |i-j|) across all pairs (i,j). But how to compute this efficiently?

Wait, but even that approach would require considering all possible pairs, which is O(n^2) time. We need a way to compute this without checking every pair.

Let me think about the pairs. For each adjacent pair (i, i+1), the distance is 1, so the allowed k is min(a_i, a_i+1) / 1. Similarly, for pairs two apart, the distance is 2, so the allowed k is min(a_i, a_i+2)/2. For each possible distance d (from 1 to n-1), we need to find the minimal (min(a_i, a_j) / d) across all pairs (i,j) with |i-j|=d. Then the overall k is the minimum of all these minimal values.

Ah! Because for a given distance d, the maximum possible k allowed by that d is the minimum of (min(a_i, a_j) / d) across all pairs with that d. Then, the maximum possible k is the minimum over all d of these values.

So for each d from 1 to n-1, compute the minimal (min(a_i, a_{i+d})/d) for all i where i and i+d are within the array. Then take the minimum of all those values across d. That's the answer.

Wait, but why? Because for any d, the maximum allowed k for that d is the minimal (min(a_i, a_j)/d) across all pairs with distance d. Because for that d, the condition k <= min(a_i, a_j)/d for all pairs at distance d. So the maximum possible k is the minimum of all (min(a_i,a_j)/d) for all possible d and their pairs.

Therefore, the maximum possible k is the minimum over all d of (the minimal (min(a_i, a_j)/d) for pairs at distance d).

So the problem now is, for each d in 1..n-1, compute the minimal (min(a_i, a_{i+d})/d) for all i, and then find the overall minimum among all these.

But even if we do that, for each d, we need to check all possible pairs (i, i+d) which is O(n) per d, leading to O(n^2) time. Which is again impossible.

So this approach is not feasible for large n. Therefore, we need a way to find the minimal (min(a_i, a_j)/d) across all possible pairs (i, j) without checking all pairs.

Hmm. Let's think. For each d, the minimal value of min(a_i, a_{i+d}) for pairs at distance d is the limiting factor. So for each d, the minimal min(a_i, a_{i+d}) is divided by d, and among all d, the minimal of these values is the answer.

So perhaps the key is to find, for each possible d, the minimum of min(a_i, a_{i+d}), and then compute (that minimum) / d, then take the overall minimum of those values.

If that's the case, then perhaps for each d, we can compute the minimal min(a_i, a_{i+d}), which is the minimal of the pair minima for all pairs at distance d. Then, for each d, compute that minimal divided by d, and find the minimal over all d of these.

But how to compute, for each d, the minimal min(a_i, a_{i+d}) efficiently?

Let's think: For each d, the pairs are (0, d), (1, d+1), ..., (n-d-1, n-1). So for each d, the array elements a[0], a[1], ..., a[n-d-1] and a[d], a[d+1], ..., a[n-1]. The min for each pair is the min of a[i] and a[i+d]. So the minimal of these min values is the minimum of min(a[i], a[i+d]) for all i from 0 to n-d-1.

But how to compute this for all d efficiently?

Wait, but for each d, we need the minimal of min(a[i], a[i+d]). Let's denote this as m(d). Then, the answer is the minimal m(d)/d for all d from 1 to n-1.

So the problem now reduces to calculating m(d) for all d, and then find the minimal m(d)/d.

The challenge is to compute m(d) for all d quickly.

But with n up to 3e5, even O(n) per d is O(n^2), which is not feasible. So there must be another approach.

Hmm. Let's think of possible observations.

Wait, perhaps the minimal m(d) for a particular d is determined by some minimal elements in the array. For example, if there is a position i where a[i] and a[i+d] are both small, then that pair contributes a small min.

But how to find these pairs efficiently.

Alternatively, perhaps the minimal m(d) for a given d is equal to the minimal of the sliding window minimum of size (d+1) in some way. Or maybe not. Let's think.

Wait, for d=1, the pairs are (0,1), (1,2), ..., (n-2, n-1). For each pair, min(a[i], a[i+1]). The minimal m(1) is the minimal of these mins.

Similarly, for d=2, the pairs are (0,2), (1,3), etc. The minimal m(2) is the minimal of min(a[i], a[i+2]).

But how to find these minima for all d efficiently.

Let me consider that for each possible pair (i, j), j = i + d. The min(a[i], a[j]) could be a[i] if a[i] <= a[j], or a[j] otherwise.

But perhaps the minimal min for a given d is the minimal of the a[i] and a[j] in the pairs. But how?

Wait, for a given d, m(d) is the minimum of min(a[i], a[i+d]) over all possible i.

But min(a[i], a[i+d]) is the smaller of a[i] and a[i+d].

So m(d) is the minimum of all a[i] and a[i+d], but considering only pairs (i, i+d). For example, if in all pairs (i, i+d), one element is very small, then m(d) is that small element.

But how can we compute this efficiently?

Hmm. Let's think of the array. For each d, the pairs are (0, d), (1, d+1), ..., (n-d-1, n-1). So for each position i in the first part, up to n-d-1, the pair is i and i+d.

The min for each pair is the smaller of a[i] and a[i+d]. So m(d) is the minimum over all these pairs' minima.

So m(d) = min{ min(a[i], a[i+d]) | i in 0..n-d-1 }

Now, to compute this for all d from 1 to n-1, but with n up to 3e5, this would take O(n^2) time if done naively.

So we need a smarter approach.

Alternative idea: For each possible d, the minimal m(d) is the minimal of the elements in the array, but considering that each element can only be part of some pairs. But I don't see how that helps.

Wait, another approach: The minimal m(d) for a particular d can't be smaller than the minimal element in the array. Because the minimal element could be part of some pair. Wait, no. For example, the minimal element could be at position i, but if d is such that i - d is out of bounds, then it's not part of any pair. Wait, no. Because for a given d, pairs are (i, i+d) where i ranges from 0 to n-d-1. So the minimal element in the array is part of pairs only if it is in the first part (i.e., in positions 0 to n-d-1). For example, if the minimal element is at position k, then for d =1, it's part of the pair (k, k+1) if k+1 <n.

But perhaps the minimal m(d) across all d is determined by the minimal elements of the array.

Alternatively, perhaps the minimal m(d) for a given d is the minimal of the elements in the array, but in a certain way.

Alternatively, perhaps the minimal m(d) occurs when the two elements in the pair are as small as possible and as close as possible. For example, pairs with small d. Because when d is small, the division by d is larger. Wait, but m(d)/d is the value. So for a given m(d), if d is larger, then m(d)/d is smaller. So the overall minimal (m(d)/d) would be for some d where m(d) is small and d is large. Or when m(d) is very small even for a small d.

But this is getting a bit abstract. Let's think of an example.

Take the first sample input:

4
6 4 5 5

So the array is [6,4,5,5].

For d=1, the pairs are (0,1), (1,2), (2,3). The min for each pair is 4,4,5. So m(1)=4. Then m(1)/1 is 4.

For d=2, pairs are (0,2) (6 and5 →5), (1,3) (4 and5 →4). m(2) is4. 4/2=2.

For d=3: pairs (0,3) →6 and5 →5. m(3)=5. 5/3≈1.666. So the minimal among all m(d)/d is the minimal of 4 (d=1), 4/2=2 (d=2), 5/3≈1.666 (d=3). Then the overall minimum is 1.666, which is 1 when floored. But the correct answer is 1. Wait, but the problem says to find the maximum k where k is the largest integer such that for all pairs, k * |i-j| <= min(a_i,a_j). So the actual answer is the floor of the minimal m(d)/d over all d. Wait, no. Because k must be an integer. So the maximum k is the maximum integer such that k <= (min(a_i,a_j)/|i-j|) for all i,j. So the maximum possible k is the minimal of (min(a_i,a_j)/|i-j|) over all i,j, and then take the floor.

Wait, but for example, if the minimal is 1.666, then the maximum k is 1.

Yes. So the answer is the floor of the minimal (min(a_i,a_j)/d) over all pairs (i,j). So for each pair (i,j) where j >i, d = j-i. So for each pair, compute min(a_i,a_j)/(j-i). The minimal value of this across all pairs is the maximum possible k, which is then floored. Wait, no. Because k can be any integer up to that minimal value. For example, if the minimal is 3, then k can be 3. If the minimal is 3.5, then k can be 3. So the answer is the integer part (floor) of the minimal value.

So, the problem reduces to finding the minimal value of (min(a_i,a_j)/(j-i)) for all pairs (i<j). Then, the answer is the floor of that minimal value.

But how to compute this minimal value efficiently?

So, the crux is to find the minimal (min(a_i,a_j)/d) over all d from 1 to n-1 and all pairs with distance d.

But even if we find that, the answer is the floor of that minimal value.

Now, the question is how to compute this minimal value efficiently.

Alternative approach: For each possible pair (i,j), j = i +d, d >=1. The term for that pair is min(a_i,a_j)/d. The minimal of all such terms is the answer.

But with n up to 3e5, there are O(n^2) pairs, which is impossible.

Therefore, we need to find a way to compute this minimal term without checking all pairs.

Let me think about the possible minimal terms. The minimal term can be achieved either by:

1. A pair with a very small d and a small min(a_i,a_j), or

2. A pair with a larger d but a very small min(a_i,a_j).

But how to find such pairs efficiently.

Wait, the minimal term is the minimal of (min(a_i,a_j)/d) over all possible d. Let's denote d = j-i.

But (min(a_i,a_j)/d) can be small if either min(a_i,a_j) is small or d is large, or both.

So perhaps the minimal term is determined by the pairs where min(a_i,a_j) is as small as possible, and d is as large as possible. Or perhaps when min(a_i,a_j) is small and d is not too small.

But how to find these pairs.

Another idea: For each element in the array, check the minimal (a_i/d) where d is the distance between i and some j. For example, for a_i, the minimal a_i/d could be when d is as large as possible. So for the element a_i, the maximum possible d is (i) to the left (distance i) or (n-1 -i) to the right. So for a_i, the minimal term involving a_i is a_i divided by the maximum possible d for that a_i.

Wait, because if a_i is the minimum in a pair (i,j), then the term is a_i/d. So for a_i, the minimal possible a_i/d is when d is as large as possible. So for a_i, the minimal contribution is a_i divided by the maximum possible d that a_i can be part of.

So, for each a_i, the maximum possible d is max(i, (n-1) -i). For example, if i is in the middle, the maximum possible d is (n-1)/2. So for a_i, the minimal contribution could be a_i/(max_d).

But that's only when a_i is the min in the pair. So, perhaps the minimal term in the entire array is the minimal among all a_i divided by their maximum possible d.

Wait, let's take an example. Suppose the array has a 0 in the middle. Then for that 0, the minimal term is 0 divided by d for the pairs involving it. So the minimal term would be 0, which would make the answer 0. Which is correct. For example, the second sample input has 0 as the first element. So the pairs (0,1) and (0,2) would have min 0. So 0/1 =0, 0/2=0. So the minimal term is 0, so the answer is 0.

But this approach would require checking for each a_i, compute a_i divided by the maximum possible d. Then take the minimal of all such terms. But is that sufficient?

Not necessarily. Because there could be a pair where the min is not a_i or a_j, but their min is small and divided by a large d. For example, consider two elements that are 1, and their positions are at the ends of the array. So d =n-1. So their min is 1, divided by d. If n is large, say 3e5, then 1/(3e5) is 0.000003333..., which could be the minimal term. So in that case, the answer is 0. So the minimal term is 1/(n-1), which for large n is very small.

But if we only consider each a_i divided by their maximum possible d, perhaps this case would be captured. Because for each a_i, the maximum d is the maximum of (i, n-1 -i). So for the two 1s at the ends, their maximum d is (n-1 -0) =n-1 for the first element, and (n-1 - (n-1)) =0 for the last element. Wait, no. The maximum d for the first element is the maximum possible distance between it and another element. For the first element (i=0), the maximum possible d is n-1 (j =n-1). So for a_i=1, the term is 1/(n-1). Similarly, for the last element (i=n-1), the maximum possible d is n-1 (when j=0), so 1/(n-1). So when considering each element's a_i divided by their maximum possible d, we would capture this term, which is the minimal possible.

So, perhaps the minimal term in the entire array is the minimal among all a_i divided by (max possible d for i) and the minimal min(a_i, a_j) divided by d for adjacent pairs (d=1) and other small d's. But how can we be sure?

Alternatively, the minimal term could be the minimum between:

a) The minimal a_i divided by their maximum possible d.

b) The minimal min(a_i, a_j) divided by d for small d.

But how to combine these.

Alternatively, the minimal term could be the minimal between all a_i divided by (max possible d) and the minimal pairs for d=1, 2, etc.

But how to compute that.

Another idea: To compute the minimal term, we can consider two cases:

1. All pairs where d is large. For these, the minimal a_i's divided by their maximum d would capture the minimal terms.

2. All pairs where d is small. For these, the minimal min(a_i, a_j) could be small enough that even divided by a small d, the term is small.

So, perhaps the minimal term is the minimum between the minimal a_i/(max_d) and the minimal min(a_i,a_j)/d for small d (like d=1,2,3).

But how to choose what counts as small d.

Alternatively, the minimal term could be either:

- The minimal a_i / (max possible d for i) for all i.

OR

- The minimal min(a_i, a_{i+1}) /1 (since d=1 is the smallest possible).

OR

- The minimal min(a_i, a_{i+2}) /2 for d=2.

But for d=1, the min is the minimal among all adjacent pairs. So if any of those is 0, then the term is 0, which would be the minimal. But in other cases, perhaps the minimal term comes from a large d.

So, perhaps the minimal term is the minimum between:

- The minimal a_i / (max possible d for i) for all i.

- The minimal min(a_i, a_{i+1}) /1.

Because for d=1, the term is min of adjacent pairs, divided by 1. For d=2, the term is min of pairs two apart, divided by 2. For larger d, the maximum possible d for any element is up to n-1, but for elements in the middle, the maximum d is about n/2. So for a given element, if a_i is small and is in the middle, then a_i/(n/2) could be small. For example, if a_i is 1000 and n is 3e5, then 1000/(1.5e5) is ~0.006, which is larger than 0. But if a_i is 1 and n is 3e5, then 1/3e5 is ~3e-6. But if in the array there exists a pair with d=1 and min 0, then that term is 0, which is the minimal.

So the minimal term could be either from a pair with a small d and small min, or from a pair with a large d and a small a_i.

So perhaps the approach is to compute:

- The minimal a_i divided by their maximum possible d.

- The minimal of min(a_i, a_{i+1}) for all i (d=1).

- The minimal of min(a_i, a_{i+2}) for all i (d=2).

But even this, considering up to d=2, could miss some cases. For example, a pair with d=3 and min 3. Then 3/3=1, but if there's a pair with d=3 and min 2, then 2/3 is 0.666, which is smaller.

But how to efficiently check all possible d's up to a certain value. Like, perhaps checking d up to some small k, and then the rest are handled by the a_i/(max_d) approach.

Alternatively, perhaps the minimal term is the minimum between the minimal a_i/(max_d) and the minimal (min(a_i, a_j)/d) for all pairs where d <= K, where K is a small constant like 100. Then, for all d> K, the minimal a_i/(max_d) would be the main factor.

But how to choose K and verify that this approach works.

Alternatively, since the minimal a_i/(max_d) is the minimal a_i divided by the maximum possible d for that a_i. For a_i, the maximum d is the maximum of (i, (n-1)-i). So for a_i in the middle, the max d is (n-1)/2. For elements near the ends, the max d is larger. For example, the first element's max d is n-1 (distance to last element).

So, the minimal a_i/(max_d) is the minimal among a_i divided by (max_d_i) for all i.

So if there's an element a_i that is 0, then 0/(max_d_i) is 0. Which would be the minimal possible term, leading to answer 0.

But what if all elements are large, but there exists a pair with min(a_i,a_j) = x and d is large enough that x/d is smaller than all a_i/(max_d_i).

For example, if the array is [1e9, 1e9, ..., 1e9]. Then, for any pair (i,j), the min(a_i,a_j) is 1e9. So for each d, the term is 1e9/d. The minimal term is 1e9/(n-1). So the answer is floor(1e9/(n-1)).

But for this array, the a_i/(max_d_i) for each i is 1e9/(max(i, n-1 -i)). The minimal of these would be 1e9/(n-1) (for the first and last elements). So the minimal term is the same as the minimal of all possible pairs. So in this case, considering the a_i/(max_d_i) approach gives the correct answer.

So perhaps the minimal term is the minimal between the a_i/(max_d_i) and the minimal (min(a_i,a_j)/d) for all pairs with d <= some value.

Wait, but how to know. Because there could be a pair with d=10 and min=5, leading to 0.5, but the a_i/(max_d_i) for all i could be higher than 0.5.

But if d=10, then the max_d for i and j could be larger than 10. For example, if i is 0, then max_d is n-1. So for d=10, the term 5/10=0.5. But the a_i/(max_d_i) for i=0 is 1e9/(n-1), which could be larger than 0.5 if n is 3e5 (n-1 is 299999, so 1e9/299999 ≈3333.333, which is way larger than 0.5). So the minimal term is 0.5, which is smaller than all a_i/(max_d_i) terms.

So in this case, the a_i/(max_d_i) approach would not capture the minimal term. So how can we handle this.

Hmm. So the previous idea of considering a_i/(max_d_i) is insufficient because there could be pairs with small d that have min(a_i,a_j)/d smaller than all a_i/(max_d_i) terms.

So what's the solution here?

We need to find the minimal min(a_i,a_j)/d across all possible pairs (i,j).

But how to compute this efficiently.

Another idea: For each element a_i, check the elements to the left and right within a certain window. For example, check a certain number of elements to the left and right (like 100) and compute min(a_i, a_j)/(j-i) for those j. Then the minimal among these and the a_i/(max_d_i) would give the answer.

But again, how to choose the window size. If the window is large, like 100, then for n=3e5, this would be O(n*100) =3e7 operations, which is manageable. But how to determine if this approach is sufficient.

Alternatively, the minimal term could be found either in the a_i/(max_d_i) or in pairs that are within a certain distance (like 100) of each other.

So the plan is:

1. Precompute all possible pairs (i,j) where j-i <= K (K is a small constant, like 200). For each such pair, compute min(a_i,a_j)/(j-i). Find the minimal among these.

2. Compute the minimal a_i/(max_d_i) for all i, where max_d_i is the maximum distance possible for a_i (max(i, n-1 -i)).

3. The answer is the minimum between the minimal from step 1 and the minimal from step 2.

But how to choose K such that if there exists a pair (i,j) with j-i >K and min(a_i,a_j)/(j-i) < the minimal from step 1 and step 2, then K must be chosen larger.

So this approach would not work if there exists a pair with j-i> K that contributes a smaller term than all pairs with j-i <=K and all a_i/(max_d_i).

But how likely is that?

For example, suppose K is 200. Then for j-i =201, the minimal term would be min(a_i,a_j)/201. For this to be smaller than the minimal a_i/(max_d_i), which is a_i divided by something like n-1 (if i is at the start or end), but if the array is such that a_i and a_j are small and j-i is large.

But in such a case, how can we ensure that K is large enough.

Alternatively, let's think mathematically. Let the minimal term from step 1 (pairs with d<=K) be m1, and the minimal from step 2 (a_i/max_d_i) be m2. Then the minimal between m1 and m2 is our candidate. But there could be a pair with d> K and min(a_i,a_j)/d < min(m1, m2). How can that happen?

Suppose that there's a pair (i,j) with d= K+1, and min(a_i,a_j) =x. Then x/(K+1) must be less than both m1 and m2.

But m2 is the minimal of a_i/(max_d_i). For this pair, the a_i and a_j may be part of other pairs. For example, a_i's max_d_i is the maximum between i and n-1 -i. Suppose that a_i is small, and the max_d_i is large. Then a_i/(max_d_i) is small, which would be part of m2. But in that case, if x/(K+1) is even smaller than a_i/(max_d_i), then x/(K+1) < m2, but this is impossible because m2 is the minimal a_i/(max_d_i). Or wait, perhaps for this pair, the min(a_i,a_j) is x, which is equal to a_i. Then x/(K+1) = a_i/(K+1). But the a_i's max_d_i is larger than K+1 (since d can be up to n-1). So a_i/(max_d_i) would be <= a_i/(K+1), because max_d_i >= K+1. Therefore, x/(K+1) = a_i/(K+1) >= a_i/(max_d_i) >= m2 (since m2 is the minimal a_i/max_d_i). So in this case, x/(K+1) is larger than m2, so the minimal term is m2.

But wait, this is only true if in the pair (i,j), a_i is the min. If a_j is the min, then similar reasoning applies.

So in other words, for any pair (i,j) with d> K, the min(a_i,a_j) is either a_i or a_j. Suppose it's a_i. Then, a_i/(d) >= a_i/(max_d_i), since max_d_i >=d (because max_d_i is the maximum possible distance for a_i, which could include d if i is at the start or end). So a_i/(d) >= a_i/(max_d_i). So if this is part of m2 (the minimal a_i/(max_d_i)), then the term for this pair can't be smaller than m2. Therefore, the minimal term for pairs with d> K can't be smaller than m2.

Therefore, the minimal term overall is the minimal between m1 (the minimal for pairs with d<=K) and m2 (the minimal a_i/(max_d_i)).

So this approach is valid, and K can be set to 200. Then, for all pairs (i,j) with d>200, their terms are >= m2, so the minimal term is either in m1 or m2.

Thus, the algorithm is:

1. Compute m1 as the minimal (min(a_i,a_j)/d) for all pairs with d<= K.

2. Compute m2 as the minimal (a_i / max_d_i) for all i.

3. The answer is the floor of the minimum between m1 and m2.

This would be O(n*K) for step 1, which is acceptable if K is 200 (3e5 *200=6e7 operations, which is manageable in Python).

So the steps are:

- For K=200, check all pairs with distance 1 to K.

- For each i in the array, check up to K elements to the right (i+1, i+2, ..., i+K) and compute the min(a_i, a_j)/d, keeping track of the minimal.

- Also compute for each i, a_i divided by the maximum possible d for i, which is max(i, (n-1)-i), and track the minimal of these.

- The answer is the minimal between the two.

Now, let's test this approach against the sample inputs.

Sample input 1:

4
6 4 5 5

max_d_i for each i:

i=0: max(0, 3-0) =3 →6/3=2.

i=1: max(1, 3-1)=2 →4/2=2.

i=2: max(2, 3-2)=2 →5/2=2.5.

i=3: max(3, 3-3)=3 →5/3≈1.666.

So m2 is the minimal of 2, 2, 2.5, 1.666 →1.666.

Now, for K=200 (but since n=4, K is 3), check all pairs with d up to 3.

For d=1: pairs (0,1), (1,2), (2,3). Their terms are 4/1=4, 4/1=4,5/1=5. The minimal here is 4.

d=2: pairs (0,2), (1,3). Terms 5/2=2.5, 4/2=2. Minimal here is 2.

d=3: pair (0,3). Term 5/3≈1.666.

So m1 is the minimal between all these terms. Which is 1.666.

So overall minimum is min(1.666, 1.666) =1.666 →floor is 1, which is correct.

Sample input 2:

3

0 1 2

max_d_i:

i=0: max(0,2) →2. 0/2=0.

i=1: max(1,1) →1. 1/1=1.

i=2: max(2,0) →2. 2/2=1.

So m2 is 0.

For K=3 (since n=3, check d=1,2):

d=1: pairs (0,1) min 0/1=0; (1,2) min 1/1=1.

d=2: pair (0,2) min 0/2=0.

So m1 is 0.

So overall minimum is 0 →answer 0.

Sample input 3:

4

821 500 479 717

Compute m2:

i=0: max(0,3-0)=3. 821/3 ≈273.666.

i=1: max(1,3-1)=2. 500/2=250.

i=2: max(2,3-2)=2. 479/2=239.5.

i=3: max(3,0)=3. 717/3=239.

m2 is 239.

For K=3, check d=1,2,3.

d=1:

pairs (0,1): min(821,500) →500 /1=500.

(1,2): min(500,479) →479 /1=479.

(2,3): min(479,717) →479 /1=479.

d=2:

pairs (0,2) → min(821,479)=479 /2=239.5.

(1,3) → min(500,717)=500 /2=250.

d=3:

pair (0,3) → min(821,717)=717 /3=239.

So m1 is the minimal among all these terms. The minimal is 239 (from d=3).

So the overall minimum is min(239, 239) →239. Answer is 239.

Which matches the sample.

So this approach works for the samples.

Another test case: array of all 1e9 and n=3e5. Then m2 is 1e9/(3e5-1) ≈3333.333. But for pairs with d=3e5-1, the term is 1e9/(3e5-1) which is the same as m2. So the approach captures that.

Another test case: array where there's a pair with d=200 and min=200. So term is 1. But the m2 is 200 / (max_d_i). For example, if the pair is (0,200) → min is 200. d=200. term is 1. But m2 for i=0 would be 200/(3e5-1) ≈0.000666. So the minimal term is 0.000666. But according to the approach, K=200. The pair (0,200) has d=200. So in step 1, when K is 200, this pair is considered. The term is 200/200=1. But this is larger than m2 (0.000666). So the minimal term is m2. So the approach would correctly find the minimal term.

But if there's a pair with d=201 and min=201, then term is 1. But the a_i/(max_d_i) for i=0 is 201/(3e5-1) which is 0.00067. So the minimal term is 0.00067, which is captured by m2.

Another example: array [0,1e9,1e9,...,1e9]. So the first pair (0,1) has min 0, term 0. So the answer is 0.

In this case, m1 would capture the 0 (since d=1 is <= K=200). So m1 is 0, which is the correct answer.

So this approach seems to work.

Now, the plan is:

1. Compute m1 as the minimal min(a_i, a_j)/d for all pairs with d <= K (K=200).

2. Compute m2 as the minimal a_i / max_d_i, where max_d_i is max(i, n-1 -i).

3. The overall minimal term is the minimum between m1 and m2.

4. The answer is the floor of this minimal term.

But how to implement this efficiently.

Now, for K=200, we need to check all pairs (i,j) where j=i+d, and d ranges from 1 to min(K, n-1). For each d, we iterate over i from 0 to n-1 -d, and compute min(a[i], a[i+d])/d. Keep track of the minimal value among all these.

But for n=3e5 and K=200, this is O(3e5 *200) =6e7 operations. Which should be manageable in Python.

Then, for each i in 0..n-1, compute max_d_i = max(i, (n-1)-i), and compute a[i]/max_d_i. Keep the minimal value.

Finally, compare the two minima and take the floor.

Now, let's code this.

First, read n and the array.

Then, compute m1:

Initialize m1 to a large value (like infinity).

For d in 1 to min(K, n-1):

   for i in 0 to (n-1-d):

       current_min = min(a[i], a[i+d])

       current_val = current_min / d

       if current_val < m1:

           m1 = current_val

But this would take O(K*(n-d)) time, which for K=200 is acceptable.

But for n=3e5 and K=200, this is 3e5*200 =6e7 operations. Which is okay.

But in Python, loops can be slow. So perhaps we can optimize this.

But given that the code must handle large n, we need to make this as efficient as possible.

Alternative approach for m1:

Loop d from 1 to K:

   for each possible i in 0 to n-d-1:

       compute min(a[i], a[i+d]) and divide by d.

But in Python, this can be done with a loop.

But for K=200, perhaps this is manageable.

Now, code steps:

Read n, a as list.

Compute m1:

m1 = infinity

for d in range(1, K+1):

    if d >= n:

        break  # because for n=1, but n >=2 per problem constraints

    for i in range(0, n-d):

        current = min(a[i], a[i+d])

        m1 = min(m1, current / d)

Compute m2:

m2 = infinity

for i in range(n):

    max_d = max(i, (n-1) -i)

    if max_d ==0:

        # but max_d can't be zero for n >=2

        pass

    current = a[i] / max_d

    m2 = min(m2, current)

Then, the answer is floor(min(m1, m2)).

Wait, but how to handle cases where the array is very large. For example, when K is 200, but n is 1e5, then for each d from 1 to 200, you have to loop through 1e5 -d elements. Which for d=1, 1e5-1 elements. But even 200*1e5=2e7 steps, which is manageable.

But in Python, loops are slower than in C++. So perhaps for K=200, this is feasible.

But perhaps we can optimize the m1 computation by precomputing the sliding window minima. But that's more complex.

Alternatively, for each d, we can compute the minimum of the min between a[i] and a[i+d] for all i, then divide by d. The minimal of these values over all d is part of m1.

But how?

For example, for d=1:

The minimal min(a[i], a[i+1]) for all i. Then divide by 1. So the minimal term is the minimal of all adjacent pairs' minima.

For d=2:

The minimal of min(a[i], a[i+2]) for all i. Divide by 2.

So for each d, the minimal (min(a[i], a[i+d])/d) is (min of min(a[i],a[i+d]) for all i) /d.

But wait, no. Because for each d, the minimal (min(a[i],a[i+d])/d) is the minimal over all i of (min(a[i],a[i+d])/d). Which is equivalent to (min over i of min(a[i],a[i+d])) ) /d. Because dividing by d (a positive number) preserves the order.

So for each d, find the minimal min(a[i],a[i+d]) for all i, then divide by d. Then take the minimal over all d.

So, for example, if for d=3, the minimal min(a[i],a[i+3]) is 6, then the term is 6/3=2.

So, for each d, the minimal term for that d is (minimal of min(a[i],a[i+d]) for i) /d.

So, the m1 is the minimal of (min_val_d /d) for d=1 to K.

This way, instead of checking all i for each d, we can compute the minimal of min(a[i],a[i+d]) for each d.

But how to compute that efficiently.

This would reduce the number of operations from O(K*n) to O(K*n) in the worst case. Wait, no. Because for each d, we have to check all i from 0 to n-d-1. Which is O(n) per d. So same as before.

But perhaps in practice, the minimal min(a[i],a[i+d]) can be found quickly.

But the previous approach of checking all pairs (i,i+d) for d<=K is the same as the current approach.

So back to the original plan.

Now, code:

But for handling large n, it's better to iterate through d from 1 to K and for each d, iterate through i and compute the min.

But in Python, for each d, looping from i=0 to n-d-1:

But for example, for d=1:

for i in range(n-1):

    current = min(a[i], a[i+1])

    m1 = min(m1, current / 1)

Similarly for other d.

So code:

n = int(input())

a = list(map(int, input().split()))

K = 200  # this is the K parameter.

m1 = float('inf')

max_d_to_check = min(K, n-1)

for d in range(1, max_d_to_check +1):

    for i in range(n - d):

        current_min = min(a[i], a[i + d])

        current_val = current_min / d

        if current_val < m1:

            m1 = current_val

# Compute m2.

m2 = float('inf')

for i in range(n):

    max_d = max(i, (n-1) - i)

    if max_d ==0:

        # this can only happen when n=1, but problem says n>=2.

        continue

    current = a[i] / max_d

    if current < m2:

        m2 = current

# Find the overall minimal.

overall_min = min(m1, m2)

answer = int(overall_min // 1)  # floor it.

print(answer)

But wait, when overall_min is a float, like 1.666, the floor is 1.

But how to compute the floor correctly.

In Python, using integer division of the float's floor may lose precision. Alternatively, since the minimal value is a float, we can cast it to integer, which automatically floors it.

But wait, for example, if overall_min is 1.9999999, then converting to int gives 1. But in reality, 1.9999999 is very close to 2.0, but the actual maximum k is 1, since k must be an integer and <= overall_min.

But how to compute the floor correctly.

The correct way is to take the integer part of the minimal value. So using math.floor(overall_min).

But when overall_min is computed as a float, due to floating-point precision errors, this can be problematic.

Alternatively, compute the maximum integer k such that k <= overall_min.

But in the code, the variables m1 and m2 are floating-point approximations. So the minimal value may not be precise.

But in practice, given that the numbers are up to 1e9, and n up to 3e5, the minimal value can be up to 1e9 /1 (d=1). So using floating points should have enough precision.

Alternatively, compute everything in integers, but that's challenging.

Alternative approach:

The expansion coefficient is the maximum k such that k <= min(a_i, a_j)/d for all pairs i,j.

But k must be the largest integer satisfying this. So k is the floor of the minimal (min(a_i,a_j)/d) over all pairs i,j.

But to compute this, using floating points may have precision issues. For example, when the minimal is exactly an integer, but due to floating-point imprecision, it's stored as 3.999999999999999 instead of 4.0. Then, taking the floor would give 3, which is incorrect.

So perhaps the solution is to compute the minimal (min(a_i,a_j) /d) as a fraction, and find the largest integer k <= this fraction.

But how to do this without floating points.

Alternatively, for each possible pair, compute min(a_i,a_j) divided by d, and keep track of the minimal value as a numerator and denominator. Then, the answer is the floor of this minimal fraction.

But this approach is not feasible for large n.

Alternatively, compute the minimal value as a fraction.

But this is complicated. Alternatively, note that the minimal value can be found as the minimal of (min_val, d) pairs, where min_val is the minimal of min(a_i,a_j) for a given d. Then, for each d, compute min_val //d. Wait, but this is not correct. For example, min_val=5 and d=3. Then 5/3=1.666, floor is 1. But if another d=2 has min_val=3, which is 3/2=1.5. Then the overall minimal is 1.5, floor is 1. So the answer is 1.

But how to compute this accurately.

Alternatively, the answer is the floor of the minimal (x / y), where x is min(a_i,a_j) and y is d.

But to compute this accurately, perhaps we can use integer arithmetic.

The minimal x/y is the same as the minimal (x) * (1/y) for all pairs (x, y). To find the minimal x/y, we can compare fractions as (x1*y2) vs (x2*y1). But again, comparing all pairs is not feasible.

But in our approach, we are checking all possible pairs for d<=200, and the a_i/max_d for all i.

But perhaps to avoid floating points, we can track the minimal fraction as a numerator and denominator. For example, track the minimal x/y as a fraction (x, y), and compare fractions using cross multiplication.

But this would require storing the current minimal as x and y, and for each new x_new/y_new, compare whether x_new * y < x * y_new (since x_new/y_new < x/y implies x_new*y < x*y_new).

But this approach can be used to track the minimal fraction accurately.

But this would require more complex code.

But given that the original code uses floating points, but for some test cases, this may lead to precision errors, perhaps this approach is better.

So, for example, for the first sample input:

The minimal fraction is 5/3 ≈1.666. So the answer is 1.

But using floating points, the code will correctly compute 5/3 as 1.666..., and floor to 1.

But in cases where the minimal fraction is very close to an integer, like 4.0, but due to floating-point imprecision, it's represented as 3.999999999999999, then the code would floor to 3 instead of 4.

To avoid this, perhaps we can use integers to compute the floor.

The minimal value of x/y is a real number. The floor is the largest integer k such that k <= x/y.

Which is equivalent to k ≤ x/y → k*y ≤x.

So the maximum possible k is the largest integer where for all pairs (i,j), k*d <= min(a_i,a_j).

Which is equivalent to k <= min(a_i,a_j)/d for all pairs.

Thus, the maximum k is the minimum over all pairs (i,j) of floor(min(a_i,a_j)/d).

But the correct answer is the minimum of all floor(min(a_i,a_j)/d) across all pairs.

But if we compute the minimal value of (min(a_i,a_j)/d) as a real number, and then floor it, it's the same as the minimal floor(min(a_i,a_j)/d).

Because the minimal real value may come from a pair (i,j) where min(a_i,a_j)/d is not an integer, but the floor is the minimal floor across all pairs.

For example, suppose there are two pairs:

Pair 1: min=5, d=3 →5/3=1.666... →floor 1.

Pair 2: min=3, d=2 →3/2=1.5 →floor 1.

The minimal floor is 1.

But if another pair has min=2 and d=3 →0.666, floor 0. Then the answer is 0.

So the correct answer is the minimal floor(min(a_i,a_j)/d) over all pairs.

But the problem's expansion coefficient is the maximum k such that for all pairs, k <= min(a_i,a_j)/d →k is the minimal of all min(a_i,a_j)/d, floor'ed.

So the answer is the floor of the minimal (min(a_i,a_j)/d) across all pairs.

But how to compute this floor accurately.

But the problem is that when the minimal (min(a_i,a_j)/d) is not an integer, but very close to an integer plus one.

But using floating points can have precision issues.

But given that the input a_i can be up to 1e9, and n up to 3e5, but the code's approach uses K=200, perhaps using floating points is sufficient.

Alternatively, to track the minimal fraction as a numerator and denominator, and compute the floor.

But this would require a lot of changes to the code.

Alternatively, compute the minimal as a fraction using integers.

For example, for each pair (i,j), the fraction is x = min(a_i,a_j), d = j-i.

The minimal fraction is the smallest x/d.

So to track the minimal x/d, we can represent it as a pair (x, d) and compare fractions using cross multiplication.

For example, current minimal is (x1, d1). New candidate is (x2, d2). We compare x1*d2 and x2*d1. If x1*d2 > x2*d1, then x2/d2 is smaller.

So, for each pair, we can track the minimal (x, d).

Similarly, for the m2 part, for each a_i, the fraction is a_i / max_d_i.

So, for each i, compute max_d_i = max(i, n-1 -i). The fraction is a_i / max_d_i.

We need to compare all these fractions.

So the code can be modified to track the minimal fraction as (x, d) pairs.

For example, initialize minimal_x and minimal_d as None.

For each pair (x, d) in the m1 and m2 steps, compare (x, d) with the current minimal (minimal_x, minimal_d) using cross multiplication.

But this would require more code.

But it's more accurate.

Let me think about how to implement this.

First, compute m1.

Initialize minimal_x = infinity, minimal_d = 1.

For each pair (i,j) with j-i <=K:

    x = min(a[i], a[j])

    d = j -i

    compare x/d with current minimal_x/minimal_d.

    if x * minimal_d < minimal_x * d:

        minimal_x = x

        minimal_d = d

For m2:

for each i in 0..n-1:

    max_d_i = max(i, (n-1)-i)

    x = a[i]

    d = max_d_i

    compare x/d with current minimal_x/minimal_d.

    if x * minimal_d < minimal_x *d:

        minimal_x =x

        minimal_d =d

Finally, the answer is minimal_x // minimal_d.

But this approach can be implemented.

But in code, this would require keeping track of the minimal_x and minimal_d as integers.

Let's see.

So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    K = 200

    minimal_x = None

    minimal_d = 1

    # Compute m1 part.

    for d in range(1, K+1):

        if d >=n:

            break

        for i in range(n -d):

            x = min(a[i], a[i+d])

            current_d = d

            if minimal_x is None:

                minimal_x =x

                minimal_d = current_d

            else:

                # Compare x/current_d with minimal_x/minimal_d

                # x * minimal_d < minimal_x * current_d → x/current_d is smaller.

                if x * minimal_d < minimal_x * current_d:

                    minimal_x =x

                    minimal_d = current_d

    # Compute m2 part.

    for i in range(n):

        max_d_i = max(i, (n-1) -i)

        x = a[i]

        current_d = max_d_i

        if current_d ==0:

            continue

        if minimal_x is None:

            minimal_x =x

            minimal_d = current_d

        else:

            if x * minimal_d < minimal_x * current_d:

                minimal_x =x

                minimal_d = current_d

    # Now compute answer: minimal_x // minimal_d.

    answer = minimal_x // minimal_d

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
0 1 2
""",
            "output": \
"""\
0
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    K = 200

    minimal_x = None

    minimal_d = 1

    # Compute m1 part.

    for d in range(1, K+1):

        if d >=n:

            break

        for i in range(n -d):

            x = min(a[i], a[i+d])

            current_d = d

            if minimal_x is None:

                minimal_x =x

                minimal_d = current_d

            else:

                # Compare x/current_d with minimal_x/minimal_d

                # x * minimal_d < minimal_x * current_d → x/current_d is smaller.

                if x * minimal_d < minimal_x * current_d:

                    minimal_x =x

                    minimal_d = current_d

    # Compute m2 part.

    for i in range(n):

        max_d_i = max(i, (n-1) -i)

        x = a[i]

        current_d = max_d_i

        if current_d ==0:

            continue

        if minimal_x is None:

            minimal_x =x

            minimal_d = current_d

        else:

            if x * minimal_d < minimal_x * current_d:

                minimal_x =x

                minimal_d = current_d

    # Now compute answer: minimal_x // minimal_d.

    answer = minimal_x // minimal_d

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
821 500 479 717
""",
            "output": \
"""\
239
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

Sample 3:

4

821 500 479 717

m1 part:

d=1:

i=0: min(821,500)=500/1=500.

i=1: min(500,479)=479/1=479.

i=2: min(479,717)=479/1=479.

d=2:

i=0: min(821,479)=479/2=239.5 →479 and 2.

Compare with current minimal (479,1) →479*2=958, 479*1=479 →958>479 →no change.

i=1: min(500,717)=500/2=250 →500/2=250. No change.

d=3:

i=0: min(821,717)=717/3=239 →717 and3.

Compare with current minimal (479,1):

717*1 =717, 479*3=1437 →717 <1437 →so 717/3 is smaller. So update minimal_x=717, minimal_d=3.

m2 part:

i=0: max_d_i=3. x=821/3=273.666. Current minimal is 717/3.

Compare 821*3 = 2463, 717*3=2151 → 821/3 is larger. No change.

i=1: max_d_i=2. x=500/2=250. Compare 500*3=1500, 717*2=1434 →500/2 (250) is larger than 717/3 (239). So no change.

i=2: max_d_i=2. x=479/2=239.5. Compare 479*3=1437 vs717*2=1434 →479/2 is 239.5. 1437>1434 →479/2 is larger than 717/3. So no change.

i=3: max_d_i=3. x=717/3=239. So same as current minimal.

So overall minimal is 717/3=239. Answer is 717//3=239.

Which is correct.

Thus, this approach works and avoids floating-point precision issues.

So the code is as follows.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
K = 200

min_x = None
min_d = 1

# Check all pairs with distance up to K
for d in range(1, K + 1):
    if d >= n:
        break
    for i in range(n - d):
        current_x = min(a[i], a[i + d])
        current_d = d
        if min_x is None:
            min_x, min_d = current_x, current_d
        else:
            if current_x * min_d < min_x * current_d:
                min_x, min_d = current_x, current_d

# Check individual elements divided by their maximum possible distance
for i in range(n):
    max_d_i = max(i, (n - 1) - i)
    current_x = a[i]
    current_d = max_d_i
    if current_d == 0:
        continue
    if min_x is None:
        min_x, min_d = current_x, current_d
    else:
        if current_x * min_d < min_x * current_d:
            min_x, min_d = current_x, current_d

print(min_x // min_d)
```
