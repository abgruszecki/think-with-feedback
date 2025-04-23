<think>
Okay, so I need to solve this problem where I have to find the minimum number of additional requests Polycarp needs to make so that the array of requests is strictly increasing up to a peak and then strictly decreasing after that. Hmm, let's think about how to approach this.

The problem says that after some peak, the array must strictly decrease. Both parts can be empty, so the entire array could be strictly increasing or strictly decreasing. But if there's a peak, then everything before must be strictly increasing, and everything after must be strictly decreasing. Also, adjacent elements can't be equal.

So the main idea is to find for each position i (the peak), the minimal additional requests needed if that i is the peak. Then we take the minimum over all possible peaks.

But how do we compute the required values for each possible peak efficiently?

Let's consider that for each position i, the array up to i must be strictly increasing, and the array from i onwards must be strictly decreasing. However, the peak can be part of both sequences. Wait, no. Because the peak is the highest point. So for the increasing part, each element before i must be less than the peak. And for the decreasing part, each element after i must be less than the peak. But wait, maybe that's not the case. Let me think again.

Actually, the array must be strictly increasing up to the peak (including the peak?), then strictly decreasing after. No. Wait, the description says that before some moment the load strictly increases and after that moment strictly decreases. The peak is at the moment where the increase stops. For example, in the array [1, 3, 5], the peak is at index 2 (0-based?), but the array is strictly increasing, so the peak is the last element. Then the decreasing part is empty. Similarly, [10] is allowed. So for each possible peak position (from 0 to n-1), we need to construct two sequences:

Left part: a_1 < a_2 < ... < a_peak.

Right part: a_peak > a_peak+1 > ... > a_n.

But how to model this?

For each position i, the left sequence must be strictly increasing up to i, and the right must be strictly decreasing from i. So, for each i, we need to compute the minimal possible a[i] such that the left is strictly increasing and the right is strictly decreasing.

Wait, no. The actual a array is modified by adding some requests. So for each position i as the peak, we need to set the values such that:

- For all j < i: a_j (modified) < a_{j+1} (modified). So the left part up to i is strictly increasing.

- For all j > i: a_j (modified) < a_{j-1} (modified). So the right part from i onwards is strictly decreasing.

But the peak a_i must be greater than a_{i-1} (if i>0) and greater than a_{i+1} (if i <n-1).

Wait, no. The peak is part of both sequences. So for the left part, a_0 < a_1 < ... < a_i. For the right part, a_i > a_{i+1} > ... > a_{n-1}. So the peak is the maximum in the array, and the array must form a strictly increasing up to the peak and then strictly decreasing.

Therefore, for each possible peak position i, we can compute the minimal required a values such that:

Left part up to i is strictly increasing.

Right part from i is strictly decreasing.

But the a array can be modified by adding to any elements as needed. Our goal is to find the minimal total additions.

So for each i, how do we compute the minimal required additions?

Let's think about the left part first. For the left part, each element must be strictly increasing. So for each j from 0 to i:

If j is 0, the left_max is a[0]. But if j>0, then left_max[j] = max(left_max[j-1] + 1, a[j]).

Wait, no. Because for the left part to be strictly increasing, each element must be at least one more than the previous. So, for example, if a[j] is greater than left_max[j-1], then left_max[j] can be a[j]. But if a[j] is <= left_max[j-1], then we have to increase it to left_max[j-1] +1. So for the left array, we can precompute the minimal required values to make the sequence strictly increasing, starting from the left.

Similarly, for the right part, starting from the end, each element must be strictly decreasing. So for the right part, starting from the end and moving left to i, each element must be at least one less than the previous. So for j from n-1 downto i:

If j is n-1, then right_max[j] = a[j]. Otherwise, right_max[j] = max(a[j], right_max[j+1] +1). Wait, no. Because the right part from i to n-1 must be strictly decreasing. So the next element (j+1) must be less than j. So for j in the right part (from i to n-1), a[j] must be greater than a[j+1]. Wait no. The right part starts at i and is strictly decreasing. So for j >=i, a[j] must be greater than a[j+1], except for j =n-1. Wait, in the right part, each element after i must be less than the previous. So for the right part, for j from i down to 0, no, wait the array is i to the end. So for j starting at i and going to the end:

Wait, the right part is from i onwards. So the elements after i (i+1, i+2, etc.) must be strictly less than the previous. So for example, a[i] must be > a[i+1], a[i+1] > a[i+2], etc.

So for the right part, starting at i, we can compute the minimal required values by moving right to left. For each position j in the right part (starting from the end and moving left to i), the minimal required value is the maximum between a[j] and (right_min[j+1] +1). Because right_min[j+1] is the minimal required value for j+1 to ensure the sequence is strictly decreasing. So j must be at least right_min[j+1] +1.

Wait, but for the right part, moving from the end towards i. Let's process j from n-1 down to i. For j =n-1, the minimal required is a[j]. For j =n-2, the value must be at least a[j] and greater than a[j+1]. So the minimal required is max(a[j], a[j+1] +1). Then for j-1, it's max(a[j-1], current j's value +1), etc.

But this is only correct if the right part starts at j. But when considering the peak i, the right part starts at i. So for each i, the right part needs to be strictly decreasing from i to the end.

So, for each i, the right part from i is processed as follows:

Initialize the right array for i. For j starting from i to n-1, but we need to compute the required values such that each is strictly less than the previous. So starting from the end, and moving left.

Wait, maybe the right processing for a peak at i is done by starting from the end and moving left to i. For j from n-1 downto i:

If j is the last element, then right_required[j] = a[j]. Otherwise, right_required[j] must be at least a[j], and also must be less than right_required[j+1]. Wait, no. Because right_required[j] must be greater than right_required[j+1], since the sequence is strictly decreasing. So right_required[j] has to be greater than right_required[j+1], but also at least a[j]. So for j, the minimal required is max(a[j], right_required[j+1] + 1).

Wait, no. If the sequence is a[j], a[j+1], ..., it must be strictly decreasing. So a[j] > a[j+1]. So right_required[j] must be greater than right_required[j+1]. So for j, we can compute right_required[j] as the maximum between a[j] and (right_required[j+1] + 1). Because if a[j] is already greater than right_required[j+1], then we can take a[j]. Otherwise, we have to set it to right_required[j+1] +1.

But this approach would process the right part for each i. But with n up to 1e5, doing this for each i would be O(n^2), which is way too slow.

So we need a way to precompute these required values for all possible i efficiently.

Wait, perhaps we can precompute for each position i, the minimal required value for the right part starting at i.

But how? Let's think.

For example, suppose we precompute an array 'right' where right[i] is the minimal required value for the right part starting at i. How can we compute this in O(n) time?

Processing from the end to the start. Let's compute right array.

Initialize right[n-1] = a[n-1].

Then for i =n-2 downto 0:

right[i] = max(a[i], right[i+1] +1).

But this right array is the minimal required for the right part starting at i and moving to the end, ensuring that each next element is less than the previous. However, this is for the entire right part. So if the peak is at i, then the right part starts at i. So for the right part of peak i, the required values would be the same as this precomputed right array, but for positions >=i. Wait, but no. Because when processing the peak i, the right part must start at i and be strictly decreasing. So the right part for peak i would need to have right_required[i] >= a[i], and each subsequent position j >=i must have right_required[j] < right_required[j-1].

But the precomputed right array is for the right part starting at i, which requires that the sequence from i to end is strictly decreasing. So the precomputed right array gives, for each i, the minimal required value for i if the peak is at i, but this is only part of the story. Because the peak i must also be greater than or equal to the left part.

Wait, but the left part and the right part for peak i must meet at i. So for the peak i, the left part must be strictly increasing up to i, and the right part must be strictly decreasing from i. Therefore, the left_required[i] (the value required for i after processing the left part) must be >= the left_required[i-1] +1 (assuming i>0). Similarly, the right_required[i] (the value required for i after processing the right part) must be >= a[i], but also the right_required[i] must be greater than right_required[i+1] +1 (if i is not the last element). Wait, but how do these two parts interact?

Wait, the left part is computed as follows:

left_required[0] = a[0]

For j from 1 to i:

left_required[j] = max(a[j], left_required[j-1] + 1)

So this ensures that left_required[j] is at least left_required[j-1] +1, which makes the left part strictly increasing.

Similarly, the right part for peak i is computed by:

right_required[i] = max(a[i], right_required[i+1] +1) if i is not the last element.

Wait, but for the right part, when the peak is i, the right_required[i] must be such that right_required[i] > right_required[i+1]. So the processing is similar to the left part, but in reverse.

But how do we combine the left and right parts for the peak i?

Because for the peak i, the left_required[i] must be <= the right_required[i], but wait, no. Because the peak's value must be the same for both parts. So when considering peak i, the maximum of left_required[i] and right_required[i] is the actual value we need for i, and the sum of the increments for left and right parts up to i and after i, plus the difference between the required i value and the original a[i].

Wait, this is getting a bit complicated. Let me think again.

For each possible peak position i, the required value at i is the maximum between the left_required[i] and the right_required[i]. Because:

- The left_required[i] is the minimal value required at i to make the left part strictly increasing up to i.

- The right_required[i] is the minimal value required at i to make the right part (from i onwards) strictly decreasing.

But the actual required value at i must satisfy both conditions, so it must be at least the maximum of left_required[i] and right_required[i].

Once we have that value, the total additional requests for this peak i is the sum of (left_required[j] - a[j]) for j up to i, plus the sum of (right_required[j] - a[j]) for j from i to n-1, but then subtract (left_required[i] - a[i] + right_required[i] - a[i]) because we are double-counting the a[i] term.

Wait, no. Let's break it down.

The left_required[i] is the value required for i after processing the left part. The right_required[i] is the value required for i after processing the right part. But when considering both parts, the actual required value for i is the maximum of the two, because the left part requires that i >= left_required[i], and the right part requires that i >= right_required[i]. But since the left and right parts are processed independently, their required i values might not be compatible. So the actual required value for i is the maximum of left_required[i] and right_required[i].

So the total additional requests for peak i would be:

sum_left[i] (sum of (left_required[j] - a[j] for j from 0 to i, where left_required[j] is computed with the peak i)) 

plus 

sum_right[i] (sum of (right_required[j] - a[j] for j from i to n-1, where right_required[j] is computed with the peak i))

But this approach is O(n^2) because for each i, we have to compute sum_left and sum_right. Which is impossible for n=1e5.

Hmm, so how can we precompute the left and right required values for all possible peaks efficiently?

Alternative approach:

Precompute two arrays:

left: where left[i] is the minimal required value for i when the sequence is strictly increasing up to i. This is computed from left to right.

right: where right[i] is the minimal required value for i when the sequence is strictly decreasing from i to the end. This is computed from right to left.

Then for each possible peak i, the required value is max(left[i], right[i]). The total additions would be (sum of left[j] - a[j] for j from 0 to i, where left[j] is the left array) + (sum of right[j] - a[j] for j from i to n-1, where right[j] is the right array) - (left[i] - a[i] + right[i] - a[i]) + (max(left[i], right[i]) - a[i]).

Wait, because left[i] and right[i] are computed independently. The sum for the left part includes left[i] -a[i], and the sum for the right part includes right[i] -a[i]. But when we take the maximum of left[i] and right[i], the actual required value is the maximum, so the sum would be:

sum_left_part (sum left[j] -a[j] for j=0 to i-1) + sum_right_part (sum right[j] -a[j] for j=i+1 to n-1) + (max(left[i], right[i]) - a[i]).

Because the left array up to i-1 is strictly increasing, and left[i] is left[i-1]+1 (if a[i] is less than that). So for the left part up to i, the left array would have left[i] = max(a[i], left[i-1] +1). Similarly, the right array for i is computed as right[i] = max(a[i], right[i+1]+1).

But if we use the precomputed left and right arrays, then for each peak i, the required left values up to i are given by the left array, and the required right values from i to end are given by the right array. However, when combining them, the value at i must be at least left[i] and right[i], but these two may conflict. For example, left[i] could be 5, right[i] could be 4. Then, the actual required value for i is 5, which is higher than right[i], so the right part from i onwards would have to be adjusted. But this breaks the precomputed right array.

So this approach is not directly applicable. Because the right array is computed under the assumption that the right part starts at i, but if the actual value at i is higher than right[i], then the right part's requirements might not hold.

Ah, so this approach might not work because the left and right arrays are computed independently. For example, if the required value at i is higher than the precomputed right[i], then the right part from i onwards would need to be adjusted. But since the right part is computed starting from the end, if we increase the value at i, then the right part from i onwards would have to be adjusted again. So the precomputed right array may not be valid if the peak's required value is higher than right[i].

Hmm, this seems like a problem. So we need to find for each i the minimal possible sum of additions such that the left is strictly increasing up to i, the right is strictly decreasing from i, and the peak value is at least the maximum of the left and right required for i.

But how to model this efficiently.

Alternative idea: For each i, the minimal required value at i is the maximum between the left part's required value and the right part's required value. Then, the left part up to i must be strictly increasing up to this value, and the right part from i must be strictly decreasing from this value.

So let's think:

For each i, compute the left_required[i], which is the minimal required value at i when building the left increasing sequence. Similarly, compute right_required[i], which is the minimal required value at i when building the right decreasing sequence. Then, the actual required value at i is max(left_required[i], right_required[i]).

Once we have this required value, we need to adjust the left and right sequences to meet this value.

But how?

For the left part up to i:

The left_required[i] is already >= left_required[i-1] +1. If the actual required value at i is larger than left_required[i], then the entire left sequence from 0 to i must be adjusted. For example, if left_required[i] is 5, but the actual required is 7, then the left_required[i] is 7, which would require that left_required[i-1] <=6. But previously left_required[i-1] could be 4. So this would create a chain reaction. So this approach seems computationally expensive.

So perhaps the initial approach is not feasible. Alternative approach: For each possible peak i, compute the minimal required additions by considering the left and right sequences in a way that the peak is i.

So here's another idea: For each possible peak i, compute two arrays:

- The left array up to i, which is strictly increasing.

- The right array from i, which is strictly decreasing.

The value at i must be the maximum between the left[i] and the right[i].

But how to compute this efficiently.

Alternative approach inspired by some algorithms for similar problems (like the largest palindromic substring, or other peak-based problems):

We can precompute for each position i the maximum value it can take in the left increasing sequence and in the right decreasing sequence. Then, the required value for i as peak is the maximum of these two. Then, for each i, we can compute the sum of required increases for the left and right sequences, but adjusted to the peak value.

But how to compute that.

Let's think again. The left_required array is computed as follows:

left_required[0] = a[0]

for j from 1 to i:

left_required[j] = max(a[j], left_required[j-1] + 1)

Similarly, right_required array for the right part (starting from i):

right_required[i] = a[i]

for j from i-1 downto 0:

right_required[j] = max(a[j], right_required[j+1] +1)

Wait, no. For the right part, if the peak is at i, then for j >=i, each element must be strictly decreasing. So right_required[i] is a[i], right_required[i+1] must be less than right_required[i], so right_required[i+1] = max(a[i+1], right_required[i] -1). Wait, no. For the right part (from i onwards), we need each element after i to be strictly less than the previous one. So for j from i+1 to n-1:

right_required[j] must be < right_required[j-1].

So for j starting at i+1:

right_required[j] = max(a[j], right_required[j-1] -1 - 1? Wait, no. Because right_required[j] has to be less than right_required[j-1], but also at least a[j]. So the minimal required value for j is the maximum between a[j] and (right_required[j-1] -1).

Wait, no. For example, if the previous element is 5, then the next element must be at least 4 (if a[j] is 4, then no change is needed). But if a[j] is 3, then we have to increase it to 4. So right_required[j] is max(a[j], right_required[j-1] -1).

Yes. So for the right part (from i onwards), processing from left to right (from i to the end):

right_required[i] = a[i]

for j in i+1 to n-1:

right_required[j] = max(a[j], right_required[j-1] - 1)

But this would build the right_required array for the right part starting at i. However, this is O(n) per i, which is O(n^2) overall, which is not acceptable.

So we need a way to precompute this for all possible i's.

Alternatively, for each position j, can we find the earliest i where j is part of the right part? Not sure.

Alternative idea inspired by the problem of finding the best peak:

For each position i, compute the minimal possible left_required array up to i, and the minimal possible right_required array from i. Then, the required additions for peak i is the sum of (left_required[j] - a[j] for j in 0..i) + sum (right_required[j] - a[j] for j in i..n-1) - (left_required[i] -a[i] + right_required[i] -a[i]) + (max(left_required[i], right_required[i]) -a[i]).

But how to precompute left_required and right_required arrays.

Wait, but the left_required array for any peak i is the same as the left_required array for the entire array up to i. Because the left_required array is built by making the left part strictly increasing, regardless of where the peak is. Similarly, the right_required array for any peak i is built by making the right part from i strictly decreasing.

But the left_required array up to i is computed as follows:

left_required[0] = a[0]

for j from 1 to i:

left_required[j] = max(a[j], left_required[j-1] +1)

But this left_required array is the same for any peak >=j. Wait, no. For example, if the peak is at i, then the left_required array up to i is computed as above. But if the peak is at i+1, then the left_required array up to i+1 is computed as left_required[i+1] = max(a[i+1], left_required[i] +1). So the left_required array is built incrementally as we move i from 0 to n-1. So we can precompute the entire left_required array once, as follows:

Compute left array:

left = [a[0]]

for j from 1 to n-1:

left.append(max(a[j], left[j-1] +1))

This gives the minimal required values to have a strictly increasing array up to each j. But this is for the case when the peak is at j. However, if the peak is at some i >=j, then the left array up to j remains the same, because the left array is built by ensuring strictly increasing.

Similarly, for the right part, we can precompute an array where right[i] is the minimal required value for i to be part of a strictly decreasing array starting from i. But how?

Alternatively, for the right part, compute a right array where right[i] is the minimal required value for i such that the array from i to n-1 is strictly decreasing. This can be computed by processing from the end to the beginning.

Compute right array:

right = [a[-1]]

for j from n-2 downto 0:

right.insert(0, max(a[j], right[0] + 1))

Wait, no. Because for the array to be strictly decreasing from j to the end, a[j] must be greater than a[j+1]. So for each j, right[j] is the maximum between a[j] and (right[j+1] + 1). So processing from the end to the start.

So right is computed as:

right = [0] * n

right[n-1] = a[n-1]

for j in range(n-2, -1, -1):

right[j] = max(a[j], right[j+1] + 1)

This gives for each j the minimal required value to have a strictly decreasing array from j to the end. So if the peak is at j, then the right part is from j onwards, and right[j] is the required value for j. Wait, but this is not correct. Because if the peak is at i, the right part is from i onwards, and must be strictly decreasing. So right[i] is the minimal required value for i. Then, the next element (i+1) must be less than right[i], so right[i+1] is the minimal required for i+1 to be less than right[i]. So the precomputed right array would give the minimal required values for a strictly decreasing array starting at j.

Wait, but in this case, the right array is computed under the assumption that the entire array is strictly decreasing. But for a peak at i, the right part is from i onwards. So the right array computed as above would not take into account the peak's required value. Hmm.

Wait, perhaps for the right part of a peak at i, the required values are computed by starting from i and ensuring that each next element is less than the previous. So for j =i+1, the required value is the maximum between a[j] and (required[i] -1). Then for j =i+2, the required value is max(a[j], required[i+1] -1), and so on. But this is O(n) per peak, which is not feasible.

Alternative approach: for each peak i, the right part can be computed as follows:

required[i] = value at i (after combining left and right requirements).

Then, for j =i+1: required[j] = max(a[j], required[i] -1)

for j =i+2: required[j] = max(a[j], required[j-1] -1)

But this would need to be computed for each i, which is O(n^2) time.

This is impossible for n=1e5.

So we need a smarter way.

Alternative idea: For each position i, the required left value is left[i], which is the minimal required value to make the array strictly increasing up to i. The required right value is right[i], which is the minimal required value to make the array strictly decreasing from i to the end. Then, the actual required value at i as the peak is max(left[i], right[i]). The total additions for peak i would be sum_left[i] + sum_right[i] - (left[i] - a[i] + right[i] - a[i]) + (max(left[i], right[i]) - a[i]).

But sum_left[i] is the sum of left[j] -a[j] for j from 0 to i, and sum_right[i] is the sum of right[j] -a[j] for j from i to n-1.

But wait, sum_left[i] is the sum of the left array up to i, which is the sum of the required additions for the left part up to i. Similarly, sum_right[i] is the sum of the required additions for the right part from i. However, when combining the two, the required value at i is the maximum of left[i] and right[i], which may be higher than either, so we need to adjust the sum accordingly.

For example, if left[i] is 5 and right[i] is 4, then the required value is 5. The sum_left[i] includes 5 -a[i], and sum_right[i] includes 4 -a[i]. But the actual required value is 5, so the sum for the right part from i must be adjusted. Because the right part from i must now start with 5, then the next element must be <5.

Wait, this seems complicated. So the precomputed right array assumes that the peak is at i and the value at i is right[i]. But if the actual required value is higher (because left[i] is higher), then the entire right part must be recomputed with a higher starting value.

So the precomputed right array is not sufficient for this scenario.

This suggests that the initial approach is incorrect, and we need a different way to model the problem.

Alternative approach inspired by the need to find the minimal additions for each possible peak, but in O(n) time.

Let's consider that for each peak i, the required value at i is the maximum between the left_required[i] (from left array) and the right_required[i] (from right array). But then, the right part after i must be adjusted to start from this higher value.

But how to compute this efficiently.

Hmm. Let's think of the left array as before, which is the minimal required to have a strictly increasing array up to each i.

The right array computed as before is the minimal required to have a strictly decreasing array from each i to the end.

Then, for each i, the peak's required value is max(left[i], right[i]).

But the right part for i must now be adjusted to start from this new value. For example, if the peak's required value is higher than right[i], then the right part must be recomputed starting from this higher value.

But how can we precompute this?

Alternative idea: for each i, after choosing the peak value as m = max(left[i], right[i]), compute the required right part sum for i based on m.

The sum for the right part is the sum of (required[j] - a[j]) for j from i to n-1, where required[j] is computed as:

required[i] = m

required[i+1] = max(a[i+1], required[i] -1)

required[i+2] = max(a[i+2], required[i+1] -1)

...

required[n-1] = max(a[n-1], required[n-2] -1)

But computing this for each i would be O(n) per i, which is O(n^2) overall. Not feasible.

So this approach is not going to work.

Alternative approach: realize that for a given peak i, the minimal required additions is:

sum_left[i] + sum_right[i] - (left[i] + right[i] - 2*a[i]) + (max(left[i], right[i]) -a[i])

Wait, sum_left[i] is sum of left[j] - a[j] for j=0 to i.

sum_right[i] is sum of right[j] - a[j] for j=i to n-1.

But sum_left[i] includes left[i] - a[i], and sum_right[i] includes right[i] - a[i]. So when combining them, we have to subtract one of them (since the actual required value is max(left[i], right[i]).

So the total additions would be:

sum_left[i] + sum_right[i] - (left[i] - a[i] + right[i] - a[i]) + (max(left[i], right[i]) - a[i]).

Which simplifies to:

sum_left[i] + sum_right[i] - left[i] - right[i] + 2*a[i] + max(left[i], right[i]) - a[i]

= sum_left[i] + sum_right[i] - left[i] - right[i] + a[i] + max(left[i], right[i])

But this is only valid if the right part can be adjusted to start from max(left[i], right[i]). However, if the max is larger than right[i], then the right part after i may require more additions than what is precomputed in sum_right[i]. So this approach would underestimate the required additions.

Therefore, this approach is not correct.

Alternative idea: For each possible peak i, the required additions can be split into:

1. The left part up to i must form a strictly increasing sequence.

2. The right part from i must form a strictly decreasing sequence.

3. The peak at i must be the maximum of the two.

So for the left part, compute the required left array as before (strictly increasing), and for the right part, compute a new array that takes into account the peak value.

But again, how to do this efficiently.

Another approach: for each i, the left array is precomputed as left[i] = max(a[i], left[i-1] +1). This is the minimal required for a strictly increasing sequence up to i.

Similarly, for the right part, compute for each i the maximal required value when processing from i to the end. But this right array is computed as right[i] = max(a[i], right[i+1] +1), which is the same as the initial approach.

Then, the peak's required value is max(left[i], right[i]).

But then, the right part must be strictly decreasing from i, but if right[i] is less than left[i], then the right part must be adjusted. So for the right part from i onwards, the required values must be strictly decreasing, starting from left[i].

But how to compute this.

For example, if the peak is i and required value is m = max(left[i], right[i]), then:

For j = i+1: required[j] = max(a[j], m -1)

For j = i+2: required[j] = max(a[j], required[j-1] -1)

And so on.

But again, this requires processing each j for each i, which is O(n^2).

But maybe there's a way to precompute for each i, the required sum of the right part starting from i with a given initial value.

But this seems tricky.

Alternative idea inspired by the fact that the right part's sum for a given peak i and initial value m can be computed using the precomputed right array, but adjusted based on m.

For example, if m is the required value at i, then the sum of the right part from i to n-1 is:

sum_right = 0

prev = m

sum_right += prev - a[i]

for j in i+1 to n-1:

current = max(a[j], prev -1)

sum_right += current - a[j]

prev = current

This is O(n) per i, which is not acceptable.

But perhaps there's a way to precompute for each position i, the sum of the right part if the initial value is m, but this seems unlikely.

Alternative approach: Find the optimal peak i where left[i] and right[i] are as close as possible, so that the required value is max(left[i], right[i]) and the sum is minimized.

But how.

Alternatively, for each i, compute the required sum as:

sum_left_up_to_i + sum_right_from_i_with_initial_value(max(left[i], right[i])) - (left[i] + right[i] - 2*a[i] + max(left[i], right[i]) - a[i])

But again, this seems unclear.

Let's look at the examples to see if this gives any insight.

First example:

Input: 5

1 4 3 2 5

The solution is to make the array [1,4,5,6,5], with 6 additional requests.

The peak is at index 2 (0-based) with value 5. The left array up to 2 would be 1,4,5. The right array from 2 would be 5,6,5. Wait, but the right array computed as per the initial approach would be different.

Wait, no. Let's compute the left array:

left[0] = 1

left[1] = max(4, left[0]+1=2) →4.

left[2] = max(3, left[1]+1=5) →5.

left[3] = max(2, left[2]+1=6) →6.

left[4] = max(5, left[3]+1=7) →7.

The right array:

right[4] =5.

right[3] = max(2, right[4]+1=6) →6.

right[2] = max(3, right[3]+1=7) →7.

right[1] = max(4, right[2]+1=8) →8.

right[0] = max(1, right[1]+1=9) →9.

So for peak i=2:

left[i] =5, right[i]=7. So max is7.

The required sum would be sum_left up to i (1-1=0, 4-4=0,5-3=2 → sum 2) plus sum_right from i with initial value7.

But the right part from i=2 would need to be computed with initial value7.

For j=2:7-3=4 added.

j=3: max(2,7-1=6) →6-2=4 added.

j=4: max(5,6-1=5) →0 added.

So sum is4+4+0=8. Then the total is 2 +8 - (5-3 +7-3) + (7-3).

Wait, sum_left up to i is 2 (left[0]-1 + left[1]-4 + left[2]-3 = 0+0+2=2). sum_right from i is sum right[j]-a[j] for j=2 to4. But in the initial right array, sum_right[i=2] is7-3 +6-2 +5-5 =4 +4 +0=8. So sum_left[i] + sum_right[i] is2+8=10. Then subtract (left[i] -a[i] + right[i] -a[i])=5-3 +7-3=2+4=6. So 10-6=4. Then add (max(left[i], right[i]) -a[i])=7-3=4. So total 4+4=8. But the correct answer is 6. So this approach is not working.

Hmm, this suggests that the initial approach is not correct.

So what's wrong here?

In the first example, the correct peak is at index 2. The required value there is 5 (from left) but the right array for i=2 is 7, which is higher. So the actual required value is7. But when we compute the right part from i=2 with initial value7:

- j=2: value7.

- j=3: must be less than7 →6. a[3] is2, so need to add4.

- j=4: must be less than6. a[4] is5, which is already 5, which is less than6. So no addition.

So sum for right part is (7-3)+(6-2)+(5-5) =4+4+0=8.

The left part up to i=2 is (1-1)+(4-4)+(5-3) =0+0+2=2.

Total additions:2+8=10. But the correct answer is6. So the approach is wrong.

But in the correct solution, the peak is at index3, but wait no. Wait the sample input's output is 6, and the resulting array is [1,4,5,6,5]. So the peak is at index3. So why are we considering i=2 here?

Ah, so perhaps the initial approach is not considering the correct peak.

So for i=3:

left[i] is6 (from left array), right[i] is6 (from right array). So max is6.

Sum_left up to i=3: sum of left[j]-a[j] for j=0-3 is0+0+2+4=6.

Sum_right for i=3: sum of right[j]-a[j] for j=3-4 is6-2=4 and5-5=0 → total4.

So sum_left + sum_right =6+4=10. Subtract (left[i] -a[i] + right[i] -a[i]) → (6-2)+(6-2)=4+4=8. So 10-8=2. Add (max(left[i], right[i])-a[i]) →6-2=4. Total is2+4=6. Which matches the sample.

Ah! So in this case, the correct peak is i=3. So the approach works here.

So the formula for the total additions is:

total = sum_left[i] + sum_right[i] - (left[i] -a[i] + right[i] -a[i]) + (max(left[i], right[i]) -a[i])

Which is sum_left[i] + sum_right[i] - (left[i] + right[i] - 2a[i]) + (max(left[i], right[i]) -a[i])

= sum_left[i] + sum_right[i] - left[i] - right[i] + 2a[i] + max(left[i], right[i}) -a[i]

= sum_left[i] + sum_right[i] - left[i] - right[i] + a[i] + max(left[i], right[i])

In the case of i=3:

sum_left[i] is6, sum_right[i] is4.

left[i] =6, right[i]=6.

max is6.

So 6+4 -6-6 +3 +6 = (10) -12 +3 +6 = 10 -12= -2, +3=1, +6=7. Wait, that doesn't add up. Hmm.

Wait wait, the formula is:

sum_left[i] + sum_right[i] - (left[i] - a[i] + right[i] -a[i]) + (max(left[i], right[i] -a[i]))

Wait, let me re-calculate for i=3:

sum_left[i] is sum of left[j] -a[j] for j=0 to3.

left[0]-a[0] is0.

left[1] is4-4=0.

left[2] is5-3=2.

left[3] is6-2=4.

Total sum_left[i] =0+0+2+4=6.

sum_right[i] is sum of right[j]-a[j] for j=3 to4.

right[3] is6-2=4.

right[4] is5-5=0.

sum_right[i] =4+0=4.

sum_left + sum_right= 10.

Subtract (left[i] -a[i] + right[i] -a[i] ) → (6-2)+(6-2) =4+4=8. 10-8=2.

Add (max(6,6) -a[i]) →6-2=4. So total is 2+4=6. Correct.

So the formula works for this case.

Another example: second sample input.

Sample input 2:

5

1 2 2 2 1

Output is 1.

The correct peak is at index2 (0-based). The array becomes [1,2,3,2,1]. So additions are0+0+1+0+0=1.

For i=2:

left[i] is max(2, left[1]+1=3) →3.

right[i] is computed as max(2, right[i+1]+1). right[i+1] for j=3 is max(2, right[4]+1=2) →2. So right[i=2] is max(2, 2+1=3) →3.

max(left[i], right[i]) is3.

sum_left[i] is (1-1)+(2-2)+(3-2)=0+0+1=1.

sum_right[i] is (3-2) + (2-2) + (1-1) =1+0+0=1.

Wait, but for i=2, sum_right[i] is sum of right[j] -a[j] for j=2 to4.

right array is computed as right[2] =3, right[3] = max(2, right[4]+1=2) →2. right[4] =1.

So sum_right[i=2] is3-2=1, 2-2=0, 1-1=0. Sum is1.

Then sum_left + sum_right=1+1=2.

Subtract (3-2 +3-2) =1+1=2. 2-2=0.

Add (3-2) =1. Total is0+1=1.

Which matches the sample.

So the formula works here.

Third sample input:

7

10 20 40 50 70 90 30

Output is0.

The array is already strictly increasing up to 90 (index5) and then strictly decreasing (30 <90). So the peak is at index5. left[5] is90 (since left array is built as increasing). right[5] is max(90, right[6]+1=30+1=31) →90. So max is90. sum_left[i=5] is sum of left[j]-a[j] up to5, which is all zeros since the array is already increasing. sum_right[i=5] is sum of right[j]-a[j] from5 to6. right[5] is90-90=0, right[6] is30-30=0. sum is0. So total is0+0 - (90-90 +90-90) + (90-90) →0. Correct.

So the formula works.

So the approach is to precompute the left array, the sum_left array, the right array, the sum_right array, then for each i compute the value using the formula.

So the steps are:

1. Compute left array, where left[i] is the minimal required value to make the array strictly increasing up to i.

sum_left[i] = sum_left[i-1] + (left[i] -a[i]).

We can precompute sum_left as a prefix sum array.

2. Compute right array, where right[i] is the minimal required value to make the array strictly decreasing from i to the end.

sum_right[i] = sum of (right[j] -a[j] for j from i to n-1).

We can precompute sum_right as a suffix sum array.

3. For each i from 0 to n-1:

   a. Compute the required peak value as m = max(left[i], right[i])

   b. Compute the total additions as sum_left[i] + sum_right[i] - (left[i] -a[i] + right[i] -a[i]) + (m -a[i])

4. The minimum of all such totals is the answer.

Now, the question is: can this approach be implemented in O(n) time?

Yes. Because:

- left array and sum_left can be computed in O(n) time.

- right array and sum_right can be computed in O(n) time.

- Then, iterating through each i and computing the total is O(n).

So overall, this is O(n) time and O(n) space.

Now, let's test this approach with the first sample:

Sample 1:

n=5, a = [1,4,3,2,5]

left array:

left[0] =1.

left[1] = max(4, 1+1=2) →4.

left[2] =max(3,4+1=5) →5.

left[3] =max(2,5+1=6) →6.

left[4] =max(5,6+1=7) →7.

sum_left array:

sum_left[0] =0.

sum_left[1] =0 +0=0.

sum_left[2] =0+0+2=2.

sum_left[3] =0+0+2+4=6.

sum_left[4] =6 + (7-5)=6+2=8.

right array:

right[4] =5.

right[3] =max(2,5+1=6) →6.

right[2] =max(3,6+1=7) →7.

right[1] =max(4,7+1=8) →8.

right[0] =max(1,8+1=9) →9.

sum_right array:

sum_right[4] =0.

sum_right[3] =6-2=4 +0=4.

sum_right[2] =7-3=4 +4=8.

sum_right[1] =8-4=4 +8=12.

sum_right[0] =9-1=8 +12=20.

Now, for each i:

i=0:

m = max(1,9) =9.

sum_left[i=0] =0.

sum_right[i=0] =20.

total =0 +20 - (1-1 +9-1) + (9-1) →20 - (0+8) +8 →20-8=12 +8=20.

i=1:

left[i=1] =4, right[i=1] =8.

m=8.

sum_left[i=1] =0+0=0.

sum_right[i=1] =12.

total=0+12 - (4-4 +8-4) + (8-4) →12 - (0 +4) +4 →12-4=8+4=12.

i=2:

left[i=2] =5, right[i=2]=7. m=7.

sum_left[i=2] =2.

sum_right[i=2]=8.

total=2+8 - (5-3 +7-3) + (7-3) →10 - (2+4) +4 →10-6=4 +4=8.

i=3:

left[i=3] =6, right[i=3] =6. m=6.

sum_left[i=3] =6.

sum_right[i=3] =4.

total=6+4 - (6-2 +6-2) + (6-2) →10 - (4+4) +4 →10-8=2+4=6.

i=4:

left[i=4] =7, right[i=4]=5. m=7.

sum_left[i=4] =8.

sum_right[i=4] =0.

total=8+0 - (7-5 +5-5) + (7-5) →8 - (2+0) +2 →8-2=6 +2=8.

The minimal is6, which is correct.

So this approach works.

Now, the code can be written as follows:

Read n.

Read a array.

Compute left array and sum_left:

left = [a[0]]

sum_left = [0] * n

sum_left[0] = left[0] - a[0]

for i in range(1, n):

    left_i = max(a[i], left[i-1] + 1)

    left.append(left_i)

    sum_left[i] = sum_left[i-1] + (left_i - a[i])

Compute right array and sum_right:

right = [0] *n

right[-1] = a[-1]

sum_right = [0] *n

sum_right[-1] = right[-1] - a[-1]

for i in range(n-2, -1, -1):

    right_i = max(a[i], right[i+1] +1)

    right[i] = right_i

    sum_right[i] = sum_right[i+1] + (right_i -a[i])

Then, for each i in 0..n-1:

current_sum = sum_left[i] + sum_right[i]

left_val = left[i]

right_val = right[i]

peak_val = max(left_val, right_val)

current_total = current_sum - (left_val - a[i] + right_val -a[i]) + (peak_val -a[i])

keep track of the minimal current_total.

So the code would look like this.

Now, let's implement this.

But wait, sum_right is computed from i to n-1. So sum_right[i] = sum of (right[j] -a[j] for j in i to n-1).

Yes.

Now, implement the code.

Testing this with the first sample:

left array is [1,4,5,6,7]

sum_left array would be [0, 0, 2, 6, 8].

right array is [9,8,7,6,5].

sum_right array would be:

sum_right[4] =0.

sum_right[3] =6-2=4.

sum_right[2] =7-3=4 +4=8.

sum_right[1] =8-4=4 +8=12.

sum_right[0] =9-1=8 +12=20.

Then, for i=3:

sum_left[3] =6.

sum_right[3] =4.

current_sum=6+4=10.

left_val=6.

right_val=6.

peak_val=6.

current_total=10 - (6-2 +6-2) + (6-2) →10 - (4+4) +4=10-8=2 +4=6.

Which is correct.

So the code seems correct.

Another test case: sample 2.

Sample 2:

n=5

a= [1,2,2,2,1]

left array:

left[0] =1.

left[1] = max(2, 1+1=2) →2.

left[2] =max(2, 2+1=3) →3.

left[3] =max(2,3+1=4) →4.

left[4] =max(1,4+1=5) →5.

sum_left array:

sum_left[0] =0.

sum_left[1] =0.

sum_left[2] =0+0 +1=1.

sum_left[3] =1 + (4-2)=3.

sum_left[4] =3+ (5-1)=7.

right array:

right[4] =1.

right[3] =max(2,1+1=2) →2.

right[2] =max(2,2+1=3) →3.

right[1] =max(2,3+1=4) →4.

right[0] =max(1,4+1=5) →5.

sum_right array:

sum_right[4] =0.

sum_right[3] =2-2=0.

sum_right[2] =3-2=1 +0=1.

sum_right[1] =4-2=2 +1=3.

sum_right[0] =5-1=4 +3=7.

For i=2:

sum_left[i=2] =1.

sum_right[i=2] =1.

left_val=3.

right_val=3.

current_sum=2.

total=2 - (3-2 +3-2) + (3-2) →2- (1+1) +1=0.

But the correct answer for i=2 is1.

Wait, what's wrong here?

Wait, no. For sample2, the correct answer is1. The code's calculation for i=2:

current_sum= sum_left[2] (1) + sum_right[2] (1) =2.

left_val=3, right_val=3.

peak_val=3.

current_total=2 - (3-2 +3-2) + (3-2) →2 - (1+1) +1 →2-2=0 +1=1. Which matches the sample.

Ah right. So the code correctly calculates it.

Thus, the code seems correct.

Now, the code will be written in Python as follows.

Read n.

Read a as list of integers.

Compute left array and sum_left.

Compute right array and sum_right.

Initialize the answer to a large value.

Iterate each i from 0 to n-1:

   current_total = sum_left[i] + sum_right[i] - (left[i] -a[i] + right[i] -a[i]) + max(left[i], right[i]) -a[i]

   answer = min(answer, current_total)

Return answer.

Now, let's code this.

But wait, sum_left is the sum of left[j] -a[j] for j up to i.

So sum_left[i] can be computed as a prefix sum.

Similarly, sum_right is the sum from j=i to n-1 of right[j] -a[j]. So sum_right[i] is computed as a suffix sum.

Implementing this:

For sum_left:

sum_left is an array where sum_left[i] is the sum of left[0..i] -a[0..i].

sum_left[0] = left[0] -a[0]

sum_left[i] = sum_left[i-1] + (left[i] -a[i])

For sum_right:

sum_right is an array where sum_right[i] is the sum of right[i..n-1] -a[i..n-1].

sum_right[n-1] = right[n-1] -a[n-1]

sum_right[i] = sum_right[i+1] + (right[i] -a[i])

So in code:

left = [a[0]]

sum_left = [0] * n

sum_left[0] = left[0] - a[0]

for i in range(1, n):

    next_left = max(a[i], left[-1] +1)

    left.append(next_left)

    sum_left[i] = sum_left[i-1] + (next_left - a[i])

right = [0] *n

right[-1] = a[-1]

sum_right = [0]*n

sum_right[-1] = right[-1] - a[-1]

for i in range(n-2, -1, -1):

    next_right = max(a[i], right[i+1] +1)

    right[i] = next_right

    sum_right[i] = sum_right[i+1] + (next_right - a[i])

Then, for each i in 0..n-1:

current_total = sum_left[i] + sum_right[i] - ( (left[i] - a[i]) + (right[i] - a[i]) ) + max(left[i], right[i]) - a[i]

ans = min(ans, current_total)

Yes.

Thus, the code should work.

Now, let's test this code with the samples.

Sample 1:

Input:

5

1 4 3 2 5

left array: [1,4,5,6,7]

sum_left: [0, 0, 2, 6, 8]

right array: [9,8,7,6,5]

sum_right: [20, 12,8,4,0]

For i=3:

sum_left[3] =6, sum_right[3] =4.

current_total =6+4 - (6-2 +6-2) + (6-2) →10 - (4+4) +4 →2 +4=6.

Sample 2:

Input:

5

1 2 2 2 1

sum_left for i=2 is1, sum_right[i=2] is1.

current_total=2 - (1+1) +1 →1.

Sample3:

Input:

7

10 20 40 50 70 90 30

left array is:

10, 20 (max(20,10+1=11 →20), 40 (max(40,20+1=21 →40),50,70,90, 30>90+1=91 →91.

Wait, no. Let's re-calculate.

Wait, the left array is built as:

left[0] =10.

left[1] =max(20, left[0]+1=11) →20.

left[2] =max(40, left[1]+1=21) →40.

left[3] =max(50, 40+1=41) →50.

left[4] =max(70,50+1=51) →70.

left[5] =max(90,70+1=71) →90.

left[6] =max(30,90+1=91) →91.

sum_left[5] = (10-10)+(20-20)+(40-40)+(50-50)+(70-70)+(90-90) =0.

sum_right[5] is sum of right[j] -a[j] for j=5 to6.

right array is:

right[6] =30.

right[5] =max(90,30+1=31) →90.

sum_right[5] = (90-90) + (30-30) =0.

current_total for i=5 is 0 +0 - (90-90 +90-90) + (90-90) →0-0+0=0.

Which is correct.

Thus, the code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

# Precompute left array and sum_left
left = [a[0]]
sum_left = [0] * n
sum_left[0] = left[0] - a[0]
for i in range(1, n):
    next_left = max(a[i], left[i-1] + 1)
    left.append(next_left)
    sum_left[i] = sum_left[i-1] + (next_left - a[i])

# Precompute right array and sum_right
right = [0] * n
sum_right = [0] * n
right[-1] = a[-1]
sum_right[-1] = right[-1] - a[-1]
for i in range(n-2, -1, -1):
    next_right = max(a[i], right[i+1] + 1)
    right[i] = next_right
    sum_right[i] = sum_right[i+1] + (next_right - a[i])

min_requests = float('inf')

for i in range(n):
    l_val = left[i]
    r_val = right[i]
    peak = max(l_val, r_val)
    current_sum = sum_left[i] + sum_right[i]
    subtract = (l_val - a[i]) + (r_val - a[i])
    add = peak - a[i]
    total = current_sum - subtract + add
    if total < min_requests:
        min_requests = total

print(min_requests)
```