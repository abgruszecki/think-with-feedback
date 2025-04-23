<think>
Okay, I need to solve this problem where I have to find a subarray of length at least k with the maximum possible median. Let's think about how to approach this.

First, understanding the problem. The median of a subarray is the element in the middle position after sorting. For a subarray of length m, the median is the element at position floor((m+1)/2) when sorted. So for even lengths, it's the lower of the two middle elements. For example, length 4 gives position 2 (0-based would be 1, but maybe it's 1-based here? Wait, no. Wait the problem says after sorting, the position is floor((n+1)/2). So for a subarray of length 3, it's the 2nd element (0-based index 1), and for length 4, it's the 2nd element (0-based index 1 again, since (4+1)/2 is 2.5, floor is 2, so 1-based index 2). Wait, maybe the positions are 1-based here. Let's see the examples.

In the first example, the input is [1,2,3,2,1], k=3. The possible subarrays are length 3,4,5. For example, the subarray [1,2,3] has median 2. All of them have median 2. So the output is 2. But why is the maximum 2 here? Because maybe there's no longer subarrays that can have a higher median.

Wait, the second example: input [1,2,3,4], k=2. The subarray [3,4] of length 2. The median is (3+4)/2? No, wait according to the problem's definition, the median is the element at position floor((2+1)/2) = 1.5 floor is 1. So 1-based index 1? Wait, the example says median([3,4]) is 3. So sorted, it's [3,4], length 2. The median is the element at position (2+1)/2 = 1.5, floor is 1. So 1-based index 1, which is 3. So yes. So the median is the element at position (m+1)/2 floored, where positions are 1-based.

So for a subarray of length m, the median is the element at position (m+1)//2 when sorted. So for even lengths, it's the first of the two middle elements.

The goal is to select a subarray of length >=k, such that this median is as large as possible.

Now, how to approach this efficiently given the constraints of n up to 2e5.

First, let's think of possible approaches.

An initial thought is that the maximum median possible would be one of the elements in the array. So perhaps we can binary search for the maximum possible value that can be the median of some subarray of length >=k.

Wait, but how to check if a certain value x can be the median of some subarray of length >=k. But even more, since we're looking for the maximum possible, we can perform a binary search on the possible x values (sorted array) and check for each x if there exists a subarray of length >=k where the median is >=x. Then select the maximum x where this is true.

But how to perform this check efficiently.

Alternatively, since the median is the middle element, perhaps the optimal approach is to find the maximum possible element such that there exists a subarray of length at least k where at least (length+1)/2 elements are >=x, and x is as large as possible.

Wait, but the median is the (m+1)//2-th smallest element. So for a subarray of length m, the median is the value that is >= (m+1)//2 elements in the subarray. So, if we can find a subarray of length >=k where there exists a position (the median position) such that there are enough elements >=x in the subarray.

Alternatively, if x is the median, then in the subarray, at least (m+1)//2 elements are >=x. Because when sorted, the median is the (m+1)//2-th element, which must be >=x.

Wait, no. Suppose x is the median. Then in the subarray, there are at least (m+1)//2 elements that are <=x and >=x. Wait, perhaps I'm getting this mixed up.

Wait, the median is the (m+1)//2-th element in the sorted subarray. So for x to be the median, there must be at least (m+1)//2 elements <=x (since when sorted, the element at that position is x) but how?

Alternatively, the median of a subarray is the value that is the (m+1)//2-th smallest element. So for a subarray of length m, the median is the value such that there are at least (m+1)//2 elements in the subarray that are <= the median, and at least (m - (m+1)//2 + 1) elements >= the median. Wait, maybe that's not the right way to think about it.

Alternatively, if we have a subarray where at least (m+1)//2 elements are >=x, then the median of that subarray must be >=x. Because in the sorted array, the (m+1)//2-th element (1-based) must be at least x. So, if there's a subarray of length m >=k, and in that subarray, there are >= t elements >=x, where t is (m+1)//2. Then the median is >=x.

So, to maximize x, perhaps we can binary search x. For each x, check if there exists a subarray of length >=k where in that subarray, the number of elements >=x is >= the required t (which depends on the length of the subarray).

But the problem is that the required t depends on m (the length of the subarray). So for a subarray of length m, t is (m+1)//2. So for example, if the subarray is of length k, t is (k+1)//2. If the subarray is longer, say k+1, t is (k+2)//2.

But how can we check for any subarray of length >=k, whether there exists one where the number of elements >=x is >= t, where t is (m+1)//2 (with m being the subarray's length). That seems complicated.

Alternatively, perhaps we can find the maximum x such that there exists a subarray of some length m >=k where the number of elements >=x in the subarray is >= (m+1)//2.

But how to check this efficiently.

Hmm. Let's think of binary searching x. For each x, we can transform the array into a binary array where 1 represents a[i] >=x, 0 otherwise. Then, the problem reduces to finding a subarray of length >=k where the sum of the binary array (number of 1's) is >= t, where t is (m+1)//2, and m is the length of the subarray.

But since m can vary, this seems tricky. However, perhaps the optimal subarray for x is one of certain lengths, such as the minimal possible (k) or longer. For example, considering that for a longer subarray, the required t increases, but perhaps the sum can also increase. So maybe the optimal m is k, and we need the sum of 1's in a window of length k to be >= (k+1)//2. Because for larger m, the required t (m+1)//2 may be higher, but the sum may not increase enough.

Wait, let's think. Suppose x is a candidate. The maximum sum of 1's in any window of length >=k. For each possible window length m >=k, the required sum is (m+1)//2. So the required sum is ceil(m/2). For example, m=k: sum >= ceil(k/2). For m=k+1: sum >= ceil((k+1)/2) = ceil(k/2)+ (if k is even). Hmm.

But how can we find if there exists a window of any length >=k where the sum of 1's in that window is >= ceil(m/2), where m is the window length.

Alternatively, perhaps the maximum sum over all windows of length >=k (with their respective required thresholds) can be found.

But how to model that. Alternatively, perhaps the maximum value of (sum - ceil(m/2)) over all m >=k and all windows of length m. If any window has sum >= ceil(m/2), then x is possible.

But how to compute this efficiently.

Alternatively, let's consider that for a given x, the binary array is 1's and 0's. Then, for a window of length m, the sum must be >= (m+1)//2. Let's denote s = sum of the window. Then s >= (m+1)/2. So s*2 >= m +1. Which is equivalent to 2s - m >=1.

But 2s -m = 2*(sum of 1s) - m. So 2s - m = (sum of 1s) - (sum of 0s). Because sum of 1s = s, sum of 0s = m - s. So s - (m-s) = 2s -m.

So 2s -m >=1. So (sum of 1s - sum of 0s) >=1.

So for a window of any length m >=k, we need (sum of 1s - sum of 0s) >=1.

But how can we find a window of length >=k where this is true?

Let's model this. For each position i in the binary array, compute a prefix sum array where each element is 1 if a[i] >=x, else -1. Then the sum of 1s minus sum of 0s is the sum of the binary array transformed as 1 for a[i] >=x, -1 otherwise.

Wait, for each element in the binary array, we can represent it as 1 if a[i] >=x, else -1. Then, the sum of such elements over a window [l..r] is equal to (number of 1s) - (number of 0s). Because each 1 contributes +1, each 0 contributes -1. So the sum is (sum_1) - (sum_0) = (sum_1) - (m - sum_1) = 2*sum_1 - m.

Which is exactly the value we need to check if >=1.

So, for the transformed array (where elements are 1 or -1), the problem reduces to finding a window of length >=k where the sum is >=1.

Because if sum >=1, then 2*sum_1 -m >=1, which implies sum_1 >= (m+1)/2.

So, for a given x, the problem becomes: does there exist a subarray of length >=k in the original array where the sum of the transformed array (1 if >=x, -1 else) is >=1.

If yes, then x is a possible candidate for the maximum median, and we can try higher x. Otherwise, we need to try lower.

So the problem now reduces to, for each x, can we find such a subarray. Then, perform a binary search over x's possible values (the sorted unique elements of the array) to find the maximum x for which the answer is yes.

So the steps are:

1. Binary search on the possible x values (sorted array elements).

2. For each x, check if there's a subarray of length >=k with sum >=1 in the transformed array (1 for elements >=x, -1 otherwise).

3. The maximum x where this is possible is the answer.

Now, how to efficiently check step 2.

We need to find a subarray of length >=k where the sum is >=1.

Let me think about how to compute this.

The transformed array is T, where T[i] = 1 if a[i] >=x, else -1.

We need to compute if there exists a window of length >=k where the sum of T[i] in that window is >=1.

Let's compute the prefix sums of the transformed array.

Let's denote P[0] = 0, P[i] = T[1] + T[2] + ... + T[i].

The sum of a subarray [l..r] is P[r] - P[l-1].

We need to find r and l where r - l +1 >=k, and P[r] - P[l-1] >=1.

Which can be rewritten as P[r] -1 >= P[l-1], with r - (l-1) >=k.

So for each r, we want to check if there exists some l-1 <= r -k, such that P[l-1] <= P[r] -1.

If for any r, the minimum prefix sum in the range [0..r -k] is <= P[r] -1, then such a subarray exists.

So the approach is:

- Compute the prefix sums array P.

- For each r from k to n, compute the minimum prefix sum in the range 0 to r -k. If this minimum is <= P[r] -1, then return True.

We can compute the minimums efficiently by maintaining a running minimum as we iterate through the array.

So for each x, the check can be done in O(n) time.

Now, the binary search over x. The initial array a has elements up to 2e5. So the unique sorted elements are O(2e5) in the worst case. But binary search would take O(log n) steps. Each step takes O(n) time. So overall time is O(n log n), which is acceptable for n=2e5 (2e5 * 20 is 4e6 steps).

So this approach is feasible.

Now, let's outline the code.

First, sort the array a to perform binary search on possible x values.

Wait, but the binary search can be done on the sorted list of possible x candidates. So, the possible x's are the elements of a, sorted. So we can start with low=min(a), high=max(a). For each mid, check if it's possible, and adjust the binary search bounds accordingly.

Alternatively, we can use the sorted list of a, but for the binary search, the elements are not necessarily unique. However, in practice, the binary search can proceed as follows:

Sort the unique elements of a, and perform binary search on that list.

But perhaps it's easier to sort the array, and then binary search the index. For example:

sorted_a = sorted(a)

low = 0, high = len(sorted_a)-1.

mid = (low + high) // 2.

x = sorted_a[mid].

Check if possible. If possible, move low up, else move high down.

But even better, to avoid duplicates, perhaps we can collect the unique elements in sorted order, but for the problem, since the x can be any possible element (since the median has to be an element of the array), we can just process the sorted array, even if there are duplicates, since the binary search will converge to the maximum possible x.

But during binary search steps, duplicates may cause the same x to be checked multiple times, but that's acceptable.

Now, the code steps:

Read n and k, then the array a.

Sort the array a (needed for binary search).

Initialize low=0, high = n-1.

result = -infinity.

While low <= high:

   mid = (low + high) // 2

   x = a_sorted[mid]

   Check if possible to have a subarray of length >=k with median >=x.

   If possible:

      result = max(result, x)

      low = mid +1

   else:

      high = mid -1

At the end, output result.

Wait, but the sorted array a_sorted may have duplicates, so we need to find the rightmost x that is possible.

But in binary search, this approach would work.

Now, the problem is in the check function.

Implementing the check function:

For a given x, create the transformed array T where T[i] is 1 if a[i] >=x else -1.

Compute prefix sums P[0] = 0, P[i] = P[i-1] + T[i-1] (since a is 0-based in code, but the problem is 1-based in input).

Then, for each r in 0..n, compute the sum from l to r (with length >=k). The length is r - l +1 >=k, so l <= r -k +1.

Wait, in terms of the prefix sums:

sum from l to r (inclusive) is P[r+1] - P[l].

The length is r - l +1.

We need r - l +1 >=k => l <= r -k +1 +1?

Wait, perhaps it's easier to think in terms of the possible start positions.

For the current x, the transformed array T is of length n. The prefix sum array P has length n+1, where P[0] =0, P[i] = sum of T[0..i-1].

We need to find if there exists r >=k-1 (since length must be >=k), and l such that l <= r -k +1, and P[r+1] - P[l] >=1.

Because the subarray from l to r (0-based) has length r - l +1 >=k.

So, for each r in 0..n-1 (since the array is 0-based in code), the subarray length is (r - l +1) >=k. So l can be as low as 0 up to (r -k +1).

Wait, for a subarray ending at index r (0-based), and of length >=k, the starting index l must be <= r -k +1.

So for each r in [k-1, ..., n-1], we need to check if there exists a l in [0, ..., r -k +1] such that P[r+1] - P[l] >=1.

Which is equivalent to P[l] <= P[r+1] -1.

So for each r, the minimal P[l] in the range l=0 to l=(r -k +1) must be <= P[r+1] -1.

So, the approach is:

Compute the prefix sums P.

Initialize min_prefix = P[0].

For each r from 0 to n:

   if r >=k:

      current window is up to r -k, so the next position after r-k is (r -k +1) ?

   Wait, perhaps we can track the minimum prefix up to (r -k) for each r.

Wait, for r >=k-1 (since the length is r - l +1 >=k implies l <= r -k +1. So when r is the end index (0-based) of the subarray, the start index l can be from 0 to (r -k +1). So for the subarray ending at r (0-based) of length >=k, the start index l can be up to (r -k +1). For example, if r is index 4 (0-based) and k=3, then l can be 0,1,2. Then the subarrays are [0..4] (length 5), [1..4] (length 4), [2..4] (length 3). All >=k=3.

So for each r (0-based), the start index l can be from 0 up to (r -k +1). So when we process r (0-based), the maximum l is (r -k +1 +1 ?). Wait, perhaps I'm getting confused. Let me think again.

The length of the subarray is (r - l +1) >=k.

=> l <= r -k +1.

But since l is the start index (0-based), for a given r, the earliest l can be 0, but the latest l is (r -k +1) to ensure that the length is >=k.

So for each r in 0-based indices, we need to check for l in 0 <= l <= (r -k +1).

But when r is <k-1 (0-based, since r is the end index, the earliest possible subarray of length k is when r is k-1). So, for r <k-1, there is no possible subarray of length >=k. So, we can ignore those.

So for r starting from (k-1) (i.e., the first possible end index for a subarray of length k), up to (n-1):

   We need to check if there exists l in [0, ..., r -k +1] such that P[r+1] - P[l] >=1.

So the idea is to keep track of the minimal P[l] for l up to (r -k +1).

We can do this by maintaining a running minimum.

Wait, for example, as we iterate r from 0 to n-1:

For each r, if r >=k-1, then the current start indices l are up to (r -k +1). So for each such r, we can compute the minimal P[0..r -k +1], and check if this minimum is <= P[r+1] -1.

So, to compute the minimal P[l] for l up to (r -k +1), we can track the minimum as we go.

For example, when processing r, which is the end index of the subarray (0-based), we can track the minimum prefix up to (r -k +1) as follows:

We can have a variable that keeps track of the minimal prefix sum up to the current position (l) that can be considered for the next steps.

Wait, perhaps the code can be structured as follows:

Compute the prefix array P.

Initialize min_prefix to P[0].

For each i in 0 to n:

   if i >=k:

       current position in P is i.

       the end of the subarray is i-1 (since the prefix sum up to i is for elements 0..i-1).

       So, for the subarray ending at i-1 (0-based), the start index l can be up to (i-1 -k +1) = i -k.

       So, the l can be up to i -k.

       So, when processing prefix sum P[i], the minimum P[l] for l up to (i -k) is considered.

       So, the code would check if the current min_prefix <= P[i] -1.

       If yes, return True.

   Then, update min_prefix with the current P[i -k +1 +1] ?

Wait, perhaps this is getting messy.

Alternative approach:

For each i from 1 to n (since P has length n+1, 0-based from 0 to n), when i >=k, because the subarray must have length >=k. For example, if i is the current prefix index (i is up to n), then the subarray ending at i-1 (since P[i] is sum up to i-1) must be of length >=k. So the start index is j, where j <= i-1 -k +1 = i -k. So j can be from 0 to i -k.

So, for each i in [k, n], we need to find the minimum P[j] where j is in [0, i -k]. Then, if P[i] - min_P >=1, then return True.

So, the approach is to track the minimum of P[0..i -k] as i increases.

How can we compute this efficiently?

We can maintain a variable that tracks the minimum up to (i -k) as we iterate i from 0 to n.

Wait, here's a plan:

Initialize min_prefix = P[0].

For i in 1 to n:

   if i >=k:

       current window is up to (i -k), so the start j can be up to (i -k).

       check if min_prefix <= P[i] -1.

       if yes, return True.

   // update min_prefix for the next steps.

   if i - (k-1) >=0:

       // because when i increases by 1, the next possible j for the next i+1 will be up to i+1 -k.

       // but for the next step, when i becomes i+1, the current j can be up to i+1 -k.

       // so the current i is j +k <= i+1 -k +k = i+1.

       // perhaps, when i increases, the j's allowed for the next step are up to (i -k +1) ?

       // Maybe the min_prefix is the minimum of P[0..i -k +1], but I'm getting stuck.

Alternatively, for each i (prefix index up to n), the min_prefix is the minimum of P[0..i -k] when i >=k.

So, to compute this, as i increases from k to n, for each i, the j can be up to i -k.

So when i increases, the new j that can be considered is i -k. For example, when i=k, j can be 0 to 0 (since i-k=0).

So, for each i >=k, the j can be 0 to i-k.

So, as we iterate i from 1 to n (i is the prefix index), whenever i >=k, we need to consider all j from 0 to i-k.

But how to track the minimum up to i-k?

Ah, here's an idea. We can track the minimum of the prefix up to (i-k) for each i >=k.

For example, when i is k, then i-k=0. So the j ranges up to 0. The minimum is min(P[0]).

When i is k+1, j ranges up to 1. So the minimum is min(P[0], P[1]).

So, for each i >=k, the min_prefix is the minimum of P[0..i-k].

We can track this min_prefix as we go.

Initialize min_prefix to P[0].

Then, for i from 1 to n:

   if i >=k:

       // current i is the prefix index. The allowed j is up to i -k.

       // So when i is k, i -k =0.

       // when i is k+1, i -k=1, etc.

       // So for each i >=k, the j can be up to (i -k).

       // So when we process i, for the next i+1, the j can be up to (i+1 -k).

       // So, the j for i+1 can be up to (i -k +1) = (i+1 -k) -k? Wait no.

       // For example, i=k, then j can be up to 0. For i+1 =k+1, j can be up to 1.

       // So the new j that is added is j= (i -k +1) ?

       // Wait, i= k: j ranges up to 0.

       // i= k+1: j ranges up to 1.

       // So for each i, the j can be up to i -k.

       // So as i increases, the j can be up to i-k.

       // So for each i, when i >=k, the j can be up to i -k.

       // So when we are processing i, the next i will be i+1, and the j can be up to (i+1) -k.

       // Which is (i -k) +1.

       // So the new j that is added when i increases by 1 is (i -k) +1.

       // Therefore, to track the minimum up to j = i -k, for each i >=k:

       // For i >=k, the j can be up to i -k.

       // So when i= k, j can be 0.

       // when i= k+1, j can be 0 or 1.

       // So, for each i >=k, the j's allowed are 0,1, ..., i-k.

       // So, when we process i, the new j is i -k, which is (current i) -k.

       // So, for example, when i= k, the j is i-k=0.

       // So, during the iteration, after processing i= k, the next i is k+1.

       // The j allowed for i= k+1 is up to (k+1) -k =1.

       // So, the new j added is 1.

       // So, the minimum prefix is the minimum of previous min_prefix and P[j].

       // Thus, for each i >=k, the new j is i -k.

       // So, when i >=k, after checking the current condition, we can update the min_prefix by including P[i -k +1] ?

Wait, maybe I'm complicating it. Let's see:

We need to track the minimum of P[0 ... j], where j starts at 0 and increases by 1 each time i increases beyond k.

Wait, for i >=k, the maximum j allowed is i -k. So for each i, the maximum j is i -k.

So for each i, as it increases from k to n, j increases from 0 to (n -k).

But how to track the minimum of P[0..j], where j is from 0 to i -k.

So when i is k, j can be 0. The minimum is P[0].

When i is k+1, j can be 0 or 1. The minimum is min(P[0], P[1]).

When i is k+2, j can be 0,1,2. The minimum is min(P[0], P[1], P[2]).

And so on.

So, as i increases by 1 beyond k, the j increases by 1.

So for each i >=k, the j can be up to (i -k). So, the j for i is (i -k) = (k + m) -k = m, where m starts at 0 and goes up.

So the j values are 0,1,2,..., (n -k).

Thus, to track the minimum of P[0 ... j], we can, for each j from 0 to (n -k), track the minimum as we go.

So, when processing i (from k to n), the j is (i -k), and we need to include P[j] in the min_prefix.

So here's the approach:

Initialize min_prefix to P[0].

For i in 0 to n:

   if i <k: continue.

   j = i -k.

   // So j is the current j that is added to the possible j's.

   min_prefix = min(min_prefix, P[j])

   // Then, for the current i, check if P[i] - min_prefix >=1.

   if P[i] >= min_prefix +1:

       return True.

So, wait, but how does this fit into the code?

Wait, let's think again.

Wait, for each i (the prefix sum index, which is up to n), the condition is whether there exists j <= i -k such that P[i] - P[j] >=1.

So, the minimal P[j] for j <= i -k.

So, for each i, we can track the minimal P[j] up to j = i -k.

So the code would be:

prefix = [0]*(n+1)

for i in range(1, n+1):

   prefix[i] = prefix[i-1] + (1 if a[i-1]>=x else -1)

min_prefix = infinity

found = False

for i in range(1, n+1):

   if i >=k:

       j = i -k

       if j >=0:

           min_prefix = min(min_prefix, prefix[j])

       if prefix[i] - min_prefix >=1:

           found = True

           break

So this code would check for each i >=k (the prefix sum up to i elements, which is the sum of the first i elements of T), and for each i >=k, the j can be up to i -k.

Wait, but j = i -k. For example, when i=k, j=0. The min_prefix starts as infinity. For j=0, min_prefix is min(inf, prefix[0]) which is prefix[0]. Then check if prefix[i] (prefix[k]) - prefix[0] >=1.

Yes.

Then, as i increases, j increases by 1 each time. So for i=k+1, j=1. Then, min_prefix is min(prefix[0], prefix[1]). And so on.

So this approach tracks the minimal prefix sum up to j =i -k for each i >=k.

Thus, this code would work.

But wait, in the code, when i ranges from 1 to n (since prefix has length n+1), and for each i, we check if i >=k. Then j =i -k. But j can be up to i -k, which is the maximum j allowed for this i. So for example, when i is k, j=0, which is the first j. Then, the min_prefix is the minimum of prefix[0], and in the next steps, when i increases, j increases.

Yes.

So in this code, for each i from k to n, we compute j = i -k, and add prefix[j] to the min_prefix. Then check if prefix[i] - min_prefix >=1.

Thus, the code for the check function would be O(n), which is acceptable.

So, putting it all together:

The code will perform a binary search on the sorted array. For each candidate x, it will generate the transformed array, compute the prefix sums, and check for the existence of a subarray as described.

Now, let's test this logic with the examples.

First example:

Input: 5 3

array: 1 2 3 2 1.

The sorted array is [1,1,2,2,3].

The possible x's are 1,2,3.

We need to find the maximum x where the check returns True.

For x=3:

The transformed array is T = [ -1, -1, 1, -1, -1 ].

The prefix sums P would be [0, -1, -2, -1, -2, -3].

Then, for i >=3 (k=3):

i=3: j=0. P[3] is -1. P[0] is 0. P[3] - P[0] = -1-0= -1 <1. So no.

i=4: j=1. P[4] is -2. min_prefix is min(0, P[1]=-1) → -1. P[4] - (-1) = -2 +1= -1 <1.

i=5: j=2. P[5] is -3. min_prefix is min(-1, P[2]=-2) → -2. P[5] - (-2) =-3+2=-1 <1.

So check returns False. Thus x=3 is not possible.

Next, x=2.

The transformed array is T = [ -1, 1,1,1,-1 ].

prefix sums:

P[0] =0.

P[1] = -1.

P[2] =0.

P[3] =1.

P[4] =2.

P[5] =1.

Now, check for each i >=3.

i=3: j=0. P[3] is1. min_prefix is P[0]=0. 1-0=1 >=1 → yes. So check returns True.

Thus, x=2 is possible.

So the maximum possible is 2.

Which matches the example.

Second example:

Input:4 2.

array:1 2 3 4 → sorted [1,2,3,4].

Check x=4:

transformed array: [-1,-1,-1,1].

prefix sums: 0, -1, -2, -3, -2.

Check for i >=2.

i=2: j=0. P[2]=-2. min_prefix is 0. -2-0 =-2 <1 → no.

i=3: j=1. P[3]=-3. min_prefix is min(0, P[1]=-1) →-1. -3 - (-1) =-2 <1 → no.

i=4: j=2. P[4]=-2. min_prefix is min(-1, P[2]=-2) →-2. -2 - (-2) =0 <1 → no.

So x=4 is not possible.

Check x=3.

Transformed array: [-1,-1,1,1].

prefix sums: 0,-1,-2,-1,0.

Check for i>=2.

i=2: j=0. P[2]=-2. min_prefix is 0. -2-0 =-2 <1 → no.

i=3: j=1. min_prefix is min(0, P[1]=-1) →-1. P[3] =-1 - (-1) =0 <1 → no.

i=4: j=2. min_prefix is min(-1, P[2]=-2) →-2. P[4] is0. 0 - (-2) =2 >=1 → yes. So x=3 is possible.

Thus, the maximum x is 3.

Which matches the example.

Thus, the approach works.

Now, the code.

First, the binary search on the sorted array.

Then, for each x, perform the check as outlined.

Now, code in Python.

But for the code, we need to read the input, and process it.

The code steps:

Read n, k.

Read the array a.

Sort the array a.

Binary search between low=0 and high =n-1.

Initialize answer to -infinity.

While low <=high:

   mid = (low + high) //2.

   x = a_sorted[mid].

   if check(x):

       answer = x.

       low = mid +1.

   else:

       high = mid -1.

At the end, print answer.

But the sorted array may have duplicates, so for example, if the array has multiple elements with the same x, we need to find the rightmost one that passes the check.

But binary search should handle that.

Now, the check function.

Implementing the check function.

But in Python, for large n (2e5), we need to optimize the code.

Implementing the check function efficiently.

But for each x in the check, we can compute the transformed array, then compute prefix sums.

But for 2e5 elements, and for log2(2e5) ≈18 steps, this is manageable.

But for each check, creating the transformed array and prefix sums may take O(n) time and O(n) space. But for 2e5, this is 2e5 * 20 =4e6 operations, which is acceptable.

But in Python, with 2e5 elements, the code should be manageable.

Now, code for the check function.

def is_possible(x, a, k):

    n = len(a)

    prefix = [0]*(n+1)

    for i in range(1, n+1):

        if a[i-1] >=x:

            prefix[i] = prefix[i-1] +1

        else:

            prefix[i] = prefix[i-1] -1

    min_prefix = float('inf')

    found = False

    for i in range(1, n+1):

        if i >=k:

            j = i -k

            if j >=0:

                if prefix[j] < min_prefix:

                    min_prefix = prefix[j]

            if prefix[i] - min_prefix >=1:

                found = True

                break

        # We need to track the min_prefix for j up to i -k.

        # Wait, no. The j is i -k, but when i increases, j increases.

        # So, for each i >=k, j is i -k. So for example, when i= k, j=0. i=k+1, j=1, etc.

        # So the min_prefix is the minimum of P[j] for j from 0 to i-k.

        # So, during the loop, for each i, when i >=k, we check j =i -k, and update min_prefix as the minimum of previous min_prefix and P[j].

    return found

Wait, but in the code above, for each i >=k, we process j = i -k.

But when i increases by 1, j increases by 1. So, for example:

i= k → j=0.

i= k+1 → j=1.

So, in the code, for each i >=k, j =i -k.

Then, min_prefix is updated as min(min_prefix, prefix[j]).

This way, for all j up to i -k, min_prefix holds the minimum of all P[j] for j=0 to i -k.

Yes, because for i= k, j=0. Then, for i=k+1, j=1. So the code adds P[1] to the min_prefix.

Thus, the code correctly tracks the minimum prefix up to j=i -k.

Thus, the code is correct.

Now, testing the code with the examples.

First example:

n=5, k=3, a=[1,2,3,2,1].

sorted a is [1,1,2,2,3].

binary search:

low=0, high=4.

mid=2 → x=2.

Check x=2.

The transformed array is T = [ -1 (1), 1 (2), 1 (3),1 (2),-1 (1) ].

prefix sums are:

0, -1, 0, 1, 2, 1.

Check for i >=3.

i=3:

j=0 → prefix[0] =0. min_prefix is 0. prefix[3] is1. 1-0=1 >=1 → found is True.

Thus, returns True.

So x=2 is possible. So low=mid+1=3.

Next, mid= (3+4)//2=3 → x=2 again. Check again returns True. low=4.

mid=4. x=3. Check returns False. high=3. Loop ends. Answer is 2.

Second example:

n=4, k=2. a=[1,2,3,4]. sorted [1,2,3,4].

binary search:

low=0, high=3.

mid=1 (x=2). Check returns True. low=2.

mid=2 (x=3). Check returns True. low=3.

mid=3 (x=4). Check returns False. high=2. loop ends. answer is 3.

Thus, code works.

Now, code implementation.

But in Python, for the binary search, we can sort the array once, then use indices.

But since the array can have duplicates, the code needs to find the maximum possible x, even if it's in the middle of duplicates.

But the binary search handles that.

Now, the code:

Read n, k.

Read a as list of integers.

Sort a.

low=0, high =n-1.

ans = -inf.

while low <=high:

    mid = (low +high) //2

    x= a[mid]

    if is_possible(x, a, k):

        ans =x

        low =mid +1

    else:

        high = mid -1

print(ans)

Implementing the is_possible function as described.

But in Python, for n=2e5, creating a prefix array of size n+1 is manageable.

But we can optimize the prefix array by using a variable instead of a list. Because prefix[i] is computed as prefix[i-1] + t, where t is 1 or -1. So we can compute it on the fly.

Let's optimize:

Instead of building a prefix array, we can compute the current prefix sum and track it as we go.

Also, for the min_prefix, we can track it incrementally.

Here's the optimized code for the check function:

def is_possible(x, a, k):

    n = len(a)

    prefix =0

    min_prefix = float('inf')

    # We need to track the prefixes up to j =i-k.

    # To track j, which is up to (i-1) -k.

    # Wait, in the previous code, the j for i is i-k.

    # So when processing i (the current prefix sum), j is i-k.

    # So for the current prefix sum (i is from 1 to n), j = i-k.

    # But here, we can track the prefix sum on the fly.

    # Let's think of i as the number of elements processed.

    # So prefix is the sum of the first i elements (0..i-1 in the array).

    # So, for i from 0 to n:

    # for each element a[0], a[1], ..., a[i-1], the prefix sum is computed.

    # So, when i is in [k, n], then j = i -k.

    # Thus, the prefix sum for j is the sum of the first j elements.

    # So, for j= i -k.

    # So, during the iteration, for each i in 0..n:

    # compute the prefix sum.

    # and for j = i -k.

    # Wait, perhaps it's better to track the prefix sum step by step.

    # Let's restructure:

    current_prefix =0

    prefix_j = [0]  # prefix sums for j=0, 1, 2, ... 

    # j can be up to (n -k).

    # Because for i =n, j= n -k.

    # So for j, the indices are 0 to (n -k).

    # So during the iteration, for each element processed (each a[i]), we can compute the current_prefix.

    # But how to track the prefix sums for j.

    # Another approach:

    # The j's are from 0 to (n -k).

    # So for j in 0..n -k:

    # prefix[j] is the sum of the first j elements of the transformed array.

    # But j can be up to (n -k).

    # So, during the iteration, after processing each element, if we are at j=0, 1, etc., we can track the min_prefix.

    # This seems complicated.

    # Alternative approach: track the current_prefix and the min_prefix.

    # Also, track the prefixes for the j's.

    # Let's see:

    # We need to track the prefix sum up to j for j=0,1,...,n -k.

    # Because when i = j +k, the j is the index, and the subarray length is k.

    # So for j in 0..n -k:

    # the subarray starts at j and has length k, ends at j +k -1.

    # But this approach is not directly applicable.

    # Let's think again about the code.

    # The previous code with the prefix array is O(n) time and O(n) space.

    # For n=2e5, this is 2e5*4 bytes = 800KB, which is acceptable.

    # But perhaps using a list for the prefix is manageable.

    # But for the code to be accepted, perhaps the O(n) space is acceptable.

    # But let's optimize the space.

    # We can track the current prefix sum and the min_prefix as we go.

    # So:

    current_prefix =0

    min_prefix = float('inf')

    found = False

    # We need to track the prefix sums for j=0 to (current i -k).

    # But how?

    # For example, when processing the first k elements, the j can be 0.

    # So, when i=0 (processed 0 elements), current_prefix=0.

    # When i=1, current_prefix is 0 + T[0].

    # etc.

    # So, after processing each element, we can check if the current i >=k.

    # And track the prefixes for j = i -k.

    # Wait, perhaps the code can be rewritten as:

    prefix =0

    min_prefix = float('inf')

    # A deque to keep track of the j's.

    # Or another variable.

    # Let's think:

    # For each step i (0-based), the current element is a[i].

    # T[i] is 1 if a[i] >=x else -1.

    # prefix sum after i+1 elements is prefix + T[i].

    # j is the index up to (current i -k +1).

    # No, perhaps this is getting complicated.

    # Let's think of the code without using a prefix array.

    # We can compute the prefix sum on the fly and track the min_prefix.

    # Here's the idea:

    # The prefix sum starts at 0.

    # As we iterate through each element, we compute the current prefix sum.

    # For each element processed (after i steps), we have the current prefix sum.

    # Then, for each i >=k, we need to check if there was a previous prefix sum (at j =i -k) that is <= current prefix sum -1.

    # But how to track the min_prefix.

    # So, here's the code:

    current_prefix =0

    # We need to track the min_prefix of the prefix sums for j up to (current i -k).

    # For each i in 0..n:

    #   if i >=k:

    #       j = i -k

    #       the prefix sum up to j steps is stored.

    #       min_prefix is the minimum of the prefixes up to j steps.

    # So, as we process each element, after adding it to the current_prefix, we need to track the min_prefix for j steps.

    # But j steps are up to i -k.

    # So, during processing, after each step i (0-based), we can check if i >=k-1 (since the length is (i+1) -j >=k).

    # Wait, perhaps the code is:

    # Initialize current_prefix to 0.

    # We also need to track the prefix sums for j =0 to n -k.

    # So, when we process i from 0 to n-1:

    #   compute current_prefix += T[i]

    #   if i+1 >=k:

    #       j = (i+1) -k → i+1 is the current prefix index (i+1 steps processed).

    #       j = (i+1) -k → prefix index j.

    #       the prefix sum up to j is prefix[j].

    #       So, when i+1 is the current prefix index (after i+1 elements), j = (i+1) -k.

    #       So, for example, when i+1 =k → j=0.

    #       So, after processing the first k elements (i =k-1), j=0.

    # So, the code can be structured as:

    current_prefix =0

    min_prefix = float('inf')

    prefix_j_list = [0]  # prefix sum for j=0 (0 steps processed).

    found = False

    for i in range(n):

        # T[i] =1 if a[i] >=x else -1.

        current_prefix += 1 if a[i] >=x else -1

        # current_prefix is prefix[i+1].

        # Check if i+1 >=k.

        if (i+1) >=k:

            # j = (i+1) -k → j is the prefix index.

            j = (i+1) -k

            if j >=0:

                # the prefix sum for j is prefix_j_list[j]

                # which is prefix[j].

                # But how to track prefix[j]?

                # Wait, the prefix_j_list is built as we go.

                # For example, when j=0, prefix_j_list[0] is 0 (prefix sum after 0 elements).

                # When j=1, prefix_j_list[1] is prefix sum after 1 element.

                # So, as we process each element, after updating current_prefix, we need to store it in prefix_j_list.

                # But this way, prefix_j_list[i+1] is current_prefix.

                # So, for j= (i+1) -k, the prefix_j_list[j] is the sum after j elements.

                # But how to build prefix_j_list.

                # Let's track the prefix_j_list as we go.

                # For each i in 0..n-1:

                #   current_prefix is the sum up to i+1 elements.

                #   append current_prefix to prefix_j_list.

                #   then, for j= (i+1) -k, check if j >=0.

                #   if so, update min_prefix.

                # But this way, prefix_j_list will have i+1 entries after processing i steps.

                # So, during processing i, after adding to current_prefix, append to prefix_j_list.

                # Then, when checking j= (i+1) -k, the prefix_j_list has j+1 elements.

                # So, in the code:

                # current_prefix is added to prefix_j_list.

                # Then, for j= (i+1) -k, if j >=0, the prefix_j_list[j] is the sum after j elements.

                # So:

                # previous code:

                # current_prefix += T[i]

                # prefix_j_list.append(current_prefix)

                # then, if (i+1) >=k:

                #   j = (i+1) -k

                #   if j >=0:

                #       min_prefix = min(min_prefix, prefix_j_list[j])

                #   if current_prefix - min_prefix >=1:

                #       found = True

                #       break

                # So, this approach uses O(n) space for prefix_j_list.

                # Which is the same as before.

                # So, this code is same as before.

                # So, perhaps it's better to use a prefix array.

    # Thus, the code remains O(n) time and O(n) space.

But given that n is 2e5, using O(n) space is acceptable.

Thus, the code is correct.

Now, let's write the code.

The code should read input, process, and output the answer.

But for Python, the code may need to handle large inputs efficiently.

But using sys.stdin.readline for input can be faster.

But for the problem, the input is read via input(). But for large n, it's better to read via sys.stdin.

So, in code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())

    a = list(map(int, input_stream.readline().split()))

    a_sorted = sorted(a)

    low =0

    high = n-1

    ans =-1

    def is_possible(x, a, k):

        n = len(a)

        prefix = [0]*(n+1)

        for i in range(1, n+1):

            if a[i-1] >=x:

                prefix[i] = prefix[i-1]+1

            else:

                prefix[i] = prefix[i-1]-1

        min_p = float('inf')

        found = False

        for i in range(n+1):

            if i >=k:

                j = i -k

                if j >=0:

                    if prefix[j] < min_p:

                        min_p = prefix[j]

                if prefix[i] - min_p >=1:

                    found = True

                    break

        return found

    while low <= high:

        mid = (low + high) //2

        x = a_sorted[mid]

        if is_possible(x, a, k):

            ans =x

            low = mid +1

        else:

            high = mid -1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 2
1 2 3 4
""",
            "output": \
"""\
3
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

</think>

```python
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a_sorted = sorted(a)
    low = 0
    high = n - 1
    ans = -1

    def is_possible(x):
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            if a[i-1] >= x:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1] - 1
        min_prefix = float('inf')
        found = False
        for i in range(n + 1):
            if i >= k:
                j = i - k
                if j >= 0:
                    if prefix[j] < min_prefix:
                        min_prefix = prefix[j]
                if prefix[i] - min_prefix >= 1:
                    found = True
                    break
        return found

    while low <= high:
        mid = (low + high) // 2
        x = a_sorted[mid]
        if is_possible(x):
            ans = x
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == "__main__":
    main()
```
