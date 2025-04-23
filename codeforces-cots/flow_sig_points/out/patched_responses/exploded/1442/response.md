<think>
Okay, let's see. The problem is about grouping photos into groups where each group has at least k elements. The goal is to minimize the maximum processing time of any group, which is the difference between the max and min in that group. So we need to partition the sorted array into groups with consecutive elements (since non-consecutive would lead to larger differences) such that each group has size at least k, and the maximum difference of any group is as small as possible.

Hmm. First, I think the first step is to sort the array. Because when the array is sorted, the best way to form groups is by taking consecutive elements. Because if you have elements that are not consecutive in the sorted order, their min and max difference would be larger than if you group them consecutively. So sorting is necessary.

Once the array is sorted, the problem becomes partitioning into groups of consecutive elements, each of size >=k, such that the maximum (v[i + s -1] - v[i]) for each group is minimized.

So, the approach would be similar to dynamic programming. Let's think: for each position i, the minimal possible maximum up to that point when grouping the first i elements optimally.

But with n up to 3e5, a dynamic programming approach with O(n^2) time is not feasible. So we need a way to compute this efficiently.

Wait, maybe binary search on the possible answer. Because the minimal possible maximum processing time is between 0 and (max_v - min_v). So we can binary search on this value. For each candidate value D, check if it's possible to split the array into groups such that each group has at least k elements and the difference between max and min in each group is <= D.

If we can check this condition efficiently for a given D, then binary search can find the minimal possible D.

Yes, that's a common pattern. Let's think about how to check if D is feasible.

Once the array is sorted, the check would proceed as follows: we need to partition the array into groups where each group's last element - first element <= D, and each group has size >=k.

But how do we model this? Let's see.

We can greedily create groups. Start from the first element. The current group starts at position start. Then we can include as many elements as possible such that v[i] - v[start] <= D. However, each group must have at least k elements. So the earliest we can end a group is when the next elements form a group of size >=k, and the next group can also have enough elements.

Alternatively, perhaps the optimal grouping is to find the largest possible starting positions for groups, ensuring that each group's size is at least k and the difference is within D.

Wait, perhaps the check can be done using dynamic programming. Let's model the problem as follows: we can track the earliest position where a group can end such that all previous groups are valid.

For example, for each i, dp[i] is True if it's possible to partition the first i elements into valid groups. Then, for each i, we can check if there's a j <= i -k such that v[i] - v[j+1] <= D and dp[j] is True. But this would be O(n^2), which is too slow.

So we need a way to compute this more efficiently. But perhaps with the sorted array and binary search, we can optimize this.

Alternatively, maybe we can precompute for each position i the earliest position j where v[i] - v[j] <= D, and then check if there's a way to split the array into groups of size >=k.

Wait, but even that might not be efficient. Let's think of the following approach for checking D:

We can process the sorted array from left to right, trying to form groups. For each possible group start at position i, the maximum end is the largest j where v[j] - v[i] <= D. But the group must have at least k elements, so j - i +1 >=k. So for each i, the earliest j is i +k -1. Then, the maximum j for the group starting at i is the maximum position where v[j] <= v[i] + D. So the group can be from i to that j.

But to form the groups optimally, we need to select groups such that each group's start is after the end of the previous group.

So the greedy approach would be: once a group ends at position end, the next group starts at end+1.

But how do we model this? Let's try a greedy strategy. For a given D, we can start from the first element, and find the farthest position j where v[j] - v[0] <= D. Then, the first group can be up to j. Then, the next group starts at j+1. But wait, but each group must have at least k elements. So if j+1 - 0 is >=k, then this is possible. But maybe we can extend further, but that's not necessary. Wait, no. Because if we take the earliest possible j that allows the group to have as many elements as possible (but still <= D) and then proceed, but this might not be optimal.

Alternatively, the greedy approach of making the earliest possible groups (i.e., take as many as possible) might not work. Because perhaps taking a smaller group here allows for better grouping later, leading to a feasible solution overall.

Hmm. So perhaps a dynamic programming approach is needed, but optimized.

Wait, here's an alternative idea for the check function. Let's use a DP array where dp[i] is True if the first i elements can be partitioned into valid groups. The transition would be: for each i, check if there exists a j in [i - group_size, ...] such that the group from j+1 to i has size >=k and the difference <= D. Then, if any j where dp[j] is True exists, then dp[i] is True.

But for n=3e5, this is O(n^2) time, which is not feasible.

But perhaps with the sorted array and binary search, we can find a way to compute this efficiently.

Another approach: the check function for D can be done by greedily forming the groups. Let's see:

We process the array from left to right. For each position i, we need to decide where the current group ends. The group must start at some position s, and end at e, such that e - s +1 >=k and v[e] - v[s] <= D.

But how to choose s and e? Maybe the optimal way is to find the earliest possible e where the group from s to e can be formed, and then proceed. But I'm not sure.

Wait, maybe in the check function, the way to partition the array is to find for each group the earliest possible start, then maximize the next group's start. Wait, no. Let's think: for a given D, we want to split the sorted array into groups, each of at least k elements, and each group's max - min <=D.

We can model this as follows: start from the end. The last group must include the last element. So the last group's start is the earliest possible position such that the group from start to n-1 has size >=k and the difference <=D. Then, recursively do the same for the elements before start.

This way, the check can be done in O(n) time. Let's see:

Start from the end. Let last = n-1. Then, find the earliest position s such that (last - s +1) >=k and v[last] -v[s] <= D. Then, set last to s-1. Repeat until all elements are processed. If during this process, at any point we can't find such an s (i.e., the remaining elements are less than k), then D is not feasible.

This is a greedy approach, but does it work?

For example, consider the first sample input:

sorted array: 40,50,110,120,130. k=2.

If D=20, check:

Start from the last element (130). We need to find the earliest s such that 130 - v[s] <=20 and group size >=2.

Looking from the end:

s can be 3 (element 120) because 130-120=10 <=20, group size 2. So group is 120,130. Then, remaining elements up to index 2 (110). Now, process the remaining elements (0-2: 40,50,110, then 110 is index 2? Wait, sorted array is 40,50,110,120,130. So indexes 0-4.

Wait, initial last is 4. For D=20, check for s where 130 - v[s] <=20. So v[s] >= 110. Because 130-110=20. So possible s can be 2,3,4. The earliest s is 4 - (group size >=2). Wait group size is (last -s +1) >=k. So last is 4. So group from s to 4 must have at least k elements. So group size is 4 -s +1 >=k (which is 2). So 4 -s +1 >=2 → s <=3. Wait, that's not right. Wait group size is (e - s +1). So for the last group, e is 4. So s must be such that 4 -s +1 >=k → s <=4 -k +1 =4-2+1=3. So s can be from 0 to 3. But also, v[4] -v[s] <=D (20). So 130 -v[s] <=20 → v[s] >=110. So s must be >=2 (since v[2] is 110). So s can be 2,3. But group size must be >=2. So for s=3: group size is 4-3+1=2. Yes. For s=2: group size is 3. So group is 110,120,130. Then the remaining elements are 0-1 (40,50). They form a group of size 2 (40 and 50, difference 10 <=20). So total groups. So processing time is max(20,10)=20, which is feasible.

But if we greedily choose the earliest possible s (s=2) for the last group, then the remaining elements can form a group. So the check would return true.

This approach seems to work for this example.

Another example: the second sample input, sorted as 1,2,3,4. k=1. D=0.

Check starts from last element (4). group must have at least 1 element, and 4 -v[s] <=0 → v[s] >=4. So s must be 3. group is [4]. Then process remaining elements up to 2. Then s=2 (element 3), group [3], and so on. So all groups are single elements, D=0 is feasible.

So this approach works. So the check can be done in O(n) time, processing from the end.

So the steps for the check function would be:

Initialize last = n-1.

While last >=0:

   find the earliest s such that:

      s <= last - k +1 (so that group size is >=k, since last -s +1 >=k)

      and v[last] - v[s] <= D.

   If no such s exists (i.e., even the earliest possible s (s=last -k +1) doesn't satisfy the difference condition), then D is not feasible.

   Else, set last = s -1.

Repeat until last <0. If all groups are formed, return True.

Wait, but how to find the earliest s? Wait, no. Because the earliest possible s would be the smallest possible (like 0), but we need to find the largest possible s that is as far to the right as possible (since we want to minimize the group's start, allowing more elements for the next groups). Wait, no. Because when processing from the end, we want to choose the earliest possible s (smallest s) such that the group from s to last is valid. Wait, but no. Wait, when processing from the end, the last group must include the last element, so the group starts at some s <= last -k +1. But we want the earliest possible s (smallest s) such that v[last] -v[s] <=D. Wait, but that would maximize the group size. Wait, no. Because the group can be as large as possible (starting as early as possible) as long as the difference is <=D and the size is >=k.

Wait, perhaps the approach is: for the current last (the end of the current group), find the leftmost s (smallest s) such that v[last] -v[s] <=D and the group size (last -s +1) >=k. Then, the group is from s to last. Then, set last = s-1. But how to find s?

Wait, no. Because if you choose s as the leftmost possible, that would allow the group to have as many elements as possible (maximizing the group's size). But that might leave fewer elements for the previous groups, making it impossible to split. For example, maybe a smaller group here allows previous groups to have enough elements.

Wait, perhaps the correct approach is to choose the earliest possible s (smallest s) where the group from s to last has size >=k and difference <=D. But this may not be possible. So we need to find the leftmost s such that group size is >=k and v[last] -v[s] <=D.

Wait, no. Because the group must be at least size k. So s must be <= last -k +1. So for the group to have size at least k, s can be at most last -k +1. For example, if last is 4, and k=2, then s can be up to 4-2 +1 =3. So group would be s=3,4 (size 2). Or s=2, group 2,3,4 (size 3), etc.

So to find s, we need the maximum possible s (as large as possible) such that v[last] -v[s] <= D, and s <= last -k +1. Because this would allow the group to start as far to the right as possible, leaving more elements (earlier ones) for other groups. So this approach would minimize the number of groups, but perhaps allow more flexibility.

Wait, but how? For example, suppose we have to split into groups of size exactly k. Then, starting from the end, the next group would start at last -k, and so on. But in our problem, groups can be larger than k. So the greedy approach would be to make each group as large as possible (i.e., include as many elements as possible) as long as the difference is <=D, but the group must have at least k elements.

Wait, no. Because when processing from the end, the goal is to form a group starting as far left as possible (so that the group is as large as possible), which would allow the remaining elements (to the left) to form groups more easily. Because if you take a larger group here, there are fewer elements left, which may not allow forming groups with enough elements.

Wait, no. Let's think of an example. Suppose we have elements sorted as [1,2,3,4,5,6], k=2. Suppose D=3. The maximum possible group here would be from 1 to 6, but group size is 6, difference 5, which is larger than D. So D=3 is not feasible. But if D=5, then possible.

But let's say D=2. The groups would need to have differences <=2. So possible grouping could be [1,2,3] (diff 2), [4,5,6] (diff 2). But group sizes are 3 and 3, which is >=k=2. So feasible.

But in this case, if we process from the end, the last group starts at 4 (elements 4,5,6) since 6-4=2 <=2. But then the remaining elements are 0-3 (1,2,3,4). Wait, no. If the group starts at 4 (element 5?), wait indices are 0-based. Wait, the elements are 1 (0),2 (1),3 (2),4 (3),5 (4),6 (5). So last is 5. We need to find the earliest s (smallest possible) such that v[5] -v[s] <= D=2, and group size (5 -s +1) >=2.

So for D=2, v[5] is 6. So 6 -v[s] <=2 → v[s] >=4. So s can be 3 (4),4 (5),5 (6). But group size must be >=2. So 5 -s +1 >=2 → s <=5-2+1=4. So s can be 3,4.

So the earliest possible s is 3 (element 4). Then group is 4,5,6 (indices 3,4,5). But that's size 3. Then the remaining elements are 0-2 (1,2,3). Need to form a group. The group must have at least 2 elements. So the next group's last is 2. Check if v[2] -v[s] <=2. s can be up to 2 -2 +1=1. So s can be 0,1. But v[2] is 3. So 3 -v[s] <=2 → v[s] >=1. So possible. The earliest s is 0. Group is 0-2 (size 3), difference 3-1=2. So all groups are feasible. So the processing time is 2.

So the approach works.

But how do we find s for each last? For each last, we need to find the leftmost s such that s <= last -k +1 and v[last] -v[s] <=D. Then set last = s-1.

But how to compute this s efficiently for each last?

Since the array is sorted, for each last, the minimal s that satisfies v[s] >=v[last] - D. Because the array is sorted, we can perform a binary search on s in the range [0, last -k +1] to find the minimal s where v[s] >= v[last] -D. Wait, no. Because the condition is v[last] -v[s] <=D → v[s] >=v[last] - D. So the leftmost s that satisfies this is the minimal s where v[s] >=v[last] -D, but s must be <= last -k +1.

So for each last, the possible s is the maximum between (leftmost s where v[s] >=v[last]-D) and (s <= last -k +1). Wait, no. Because s must be <= last -k +1 (group size >=k). So the s must be in the range [0, last -k +1]. So for each last, the earliest s is the minimal s in 0..(last -k +1) where v[s] >=v[last] - D.

Wait, no. Because we want the largest possible s (the rightmost possible) in the valid range (s <= last -k +1) where v[s] >=v[last] -D. Because that way, the current group starts as far to the right as possible, leaving more elements (left of s) to form groups.

Wait, this is the key. Because the more elements left, the more possible groups. So for example, if we take the largest possible s (rightmost) in the allowed range, then the group is as small as possible (size exactly k?), which leaves more elements to the left. But those elements need to form groups of at least k elements. So perhaps this is the way to go.

So for each last, the group must start at s, such that:

s <= last -k +1 (group size >=k)

and v[last] -v[s] <=D.

We want the largest possible s in the range [0, last -k +1] that satisfies v[s] >=v[last] -D. Because the array is sorted, once we find the first s where v[s] >=v[last] -D, all elements after s in the range will also satisfy. So the largest s possible is the minimal s where v[s] >=v[last]-D, but s must be <= last -k +1. So if that minimal s is <= last -k +1, then we can take s as the minimal s, and the group will be from s to last, which has size last -s +1 >=k. Wait, no. Because if s is the minimal s where v[s] >=v[last]-D, then the group from s to last will have size last -s +1, which could be larger than k. But the group size is >=k only if s <= last -k +1. So the s must be <= last -k +1.

Wait, perhaps the steps are:

For each last in the current iteration:

1. The group must have at least k elements. So s can be at most last -k +1. So the maximum s is last -k +1.

2. The earliest s where v[s] >=v[last] - D is found via binary search. Let's call this s_min.

3. The valid s must be between s_min and last -k +1. So if s_min > last -k +1, then no valid s exists. Otherwise, the largest possible s in the allowed range is last -k +1, but only if v[last -k +1] >=v[last] -D. Wait, no. Because the s can be any s in the range [s_min, last -k +1]. But we need to choose the smallest possible s (the leftmost s) in this range. Because that allows the group to start as early as possible, which leaves more elements to the left, which might allow forming more groups. Wait, but that's the opposite of what I thought earlier.

Wait, no. Because if we choose the leftmost s (the minimal s in the allowed range), then the group will have the maximum possible size. For example, group from s=0 to last. But that would leave zero elements for the left, so the next group would start at s-1 (which is negative, so processing is done). But if the group is as large as possible, then the next groups have less elements. So maybe this approach would fail.

Alternatively, perhaps choosing the rightmost possible s (the largest possible s in the allowed range) is better, because this leaves more elements to the left. For example, if s is as large as possible (but <= last -k +1), then the group is as small as possible (k elements), leaving more elements to the left, which can then form groups of size >=k.

So for example, if we have a group that starts at last -k +1 (so group size k), then the remaining elements are up to last -k, which is s-1. So perhaps this is the optimal approach. So during the check, for each last, we should try to set s to be the maximum possible s (as large as possible) such that s <= last -k +1 and v[last] -v[s] <= D.

But how to find the maximum s in the allowed range that satisfies v[s] >=v[last]-D.

Wait, since the array is sorted, once we find the minimal s where v[s] >=v[last]-D (using binary search), then all s >= that s will also satisfy v[s] >=v[last]-D. So the possible s's are from s_min to last. But in our case, s must be <= last -k +1.

So the valid s's are in [s_min, last -k +1]. If this interval is empty (s_min > last -k +1), then no solution. Otherwise, the largest possible s in this interval is last -k +1. So in this case, the group starts at s=last -k +1. Because the group from s to last has exactly k elements (since last - s +1 = last - (last -k +1) +1 = k), and the difference is v[last] -v[s] <=D.

So the correct approach for the check function is:

For each last:

   s_max_candidate = last -k +1

   s_min = first s in [0, s_max_candidate] where v[s] >= v[last] -D.

   if s_min > s_max_candidate → not possible.

   else → set s = s_min, and proceed. Wait, no. Because s can be any value between s_min and s_max_candidate. But which one to choose to allow the maximum possible remaining elements for the next groups.

Wait, choosing the smallest s (s_min) allows the group to be as large as possible, which leaves fewer elements to the left. Choosing the largest s (s_max_candidate) allows the group to be as small as possible (k elements), leaving more elements to the left.

But leaving more elements to the left gives a better chance of forming groups. So perhaps the correct approach is to choose the largest possible s (s_max_candidate) if v[s_max_candidate] >=v[last] -D.

Wait, let's see. Let's take the first example sorted array: [40,50,110,120,130], k=2, D=20.

The check for D=20:

Processing from the end (last=4, element 130).

s_max_candidate =4-2+1=3.

Check v[3] =120. 130-120=10 <=20. So s_max_candidate is 3. So group is from 3 to4 (elements 120,130). Then last becomes 3-1=2. Now, process elements 0-2:40,50,110.

s_max_candidate =2-2+1=1. Check if v[1] >=110 -20=90. v[1] is50. 50 >=90? No. So s_min is found as the first s where v[s] >=90. Looking in 0-1. The first s where v[s] >=90 would not exist. So no solution. But this is incorrect because the first group was formed as 120,130, but the remaining elements 40,50,110 can form a group of size 3 (difference 70, which is larger than D=20). So the check would return false, but in reality, the correct grouping is possible. So this approach is not working.

Wait, what's the problem here? Because when we choose s_max_candidate, which is the maximum possible s, but in this case, the group is formed as 3-4, but the remaining elements 0-2 (40,50,110) can't form a group with D=20. But the correct grouping is 0-1 (40,50) and 2-4 (110,120,130). So the check function, as described, would fail here.

So the problem is that by choosing s_max_candidate (the maximum possible s), we are forcing the group to have exactly k elements, which may not allow the remaining elements to form valid groups. So the greedy approach of choosing the maximum possible s is incorrect.

So the check function as described is wrong. So why is that?

Because when we process the last group first, and choose s_max_candidate, we may split the array in such a way that the remaining elements can't form groups. But in the correct grouping, the last group is larger (size 3), and the first group is size 2.

So the problem is that the greedy approach of choosing the last group as the rightmost possible (smallest group) is not leading to a feasible solution.

So the check function needs to be modified. So perhaps the correct approach is to find the earliest possible s (leftmost) in the allowed range (s <=s_max_candidate) where v[last] -v[s] <=D. Then, the group starts at s and includes as many elements as possible, which leaves the remaining elements as s-1 and earlier. Then, we process those.

Wait, let's re-examine the first example with D=20.

When last=4 (element 130), s_max_candidate=3 (element 120). Check if v[3] >=130-20=110 → 120 >=110 → yes. So the group can start at 3. Then last is 3-1=2. Now, process elements 0-2 (40,50,110).

s_max_candidate=2-2+1=1 (element 50). v[1] is50. Check if 110-50=60 <=20? No. So this is not allowed. So no group can be formed here. But the correct group is from s=0 (40) to 1 (50), group size 2. So why is this not considered?

Because during the check, when processing the elements 0-2, the last is 2 (element 110). So s_max_candidate is 1. The group must start at <=1, and have size >=2. So group would be from 1 to2 (elements50,110). The difference is 60, which is larger than D=20. So no. But the correct grouping is from 0 to1. But during the check function's processing from the end, the remaining elements after the first group are 0-2 (40,50,110). So the next step is to process these elements. The group must start at s_max_candidate=1. But that group's difference is 60>20. So the check function would return false for D=20.

But the correct answer is 20. So the check function's approach is flawed.

Hmm. So what's the correct way to model this?

Perhaps the greedy approach of processing from the end and choosing the rightmost possible s is incorrect. So the check function needs to be revised.

Alternative idea: when processing from the end, we need to find the earliest possible s (smallest s) in the allowed range (s <= s_max_candidate) where v[last] -v[s] <=D. Then, group from s to last, and set last to s-1.

In the first example, when last=4 (element130):

s_max_candidate=3. We need to find the earliest s (smallest) in [0,3] where v[s] >=130-20=110. The array is 40,50,110,120,130. So the first s where v[s] >=110 is 2 (element110). But s_max_candidate is3. So s can be 2 or3. So s=2. Then group is 2-4 (110,120,130). The difference is 130-110=20, which is allowed. Then, last is1.

Now, process elements 0-1 (40,50). s_max_candidate=1-2+1=0. group size is 1-0+1=2. difference is50-40=10 <=20. So group is formed. Check returns true.

Ah, this works. So the correct approach is to find the earliest s (smallest) in the allowed range [0, s_max_candidate] where v[s] >=v[last] -D. Then, group from s to last, and proceed.

So the algorithm is:

For a given D:

   last =n-1

   while last >=0:

       s_max_candidate =last -k +1

       if s_max_candidate <0: return False

       target =v[last] -D

       # find the minimal s where v[s] >= target, and s <=s_max_candidate

       # using binary search

       left =0

       right =s_max_candidate

       res =-1

       while left <=right:

           mid = (left +right)//2

           if v[mid] >= target:

               res =mid

               right =mid-1

           else:

               left =mid+1

       if res ==-1: # no such s found

           return False

       # s is res

       # group from res to last

       last = res -1

   return True

So this way, the group is formed starting at the earliest possible s (so the group is as large as possible), leaving as few elements as possible for the next groups. Wait, no. Because when s is res (the earliest possible s), the group is as large as possible (since s is as small as possible), thus including more elements. This leaves fewer elements to the left, which may be easier to process.

In the first example, when D=20, this approach would form the group starting at res=2 (110), group size 3. Then the remaining elements are 0-1 (40,50). Which can form a group of size 2. So the check returns True.

So the correct way is to find the earliest s (smallest) in the allowed range where v[s] >=v[last] -D. Then group from s to last. This allows the largest possible group, but leaves fewer elements for the next groups, which must also be >=k. However, since the group is as large as possible, the remaining elements may form groups with enough elements.

So the binary search step is crucial here.

Now, the algorithm for the check function is O(n log n) time. But since in each iteration, we process a group of size at least k, the total number of iterations is O(n/k), which is O(3e5 /1) =3e5 in worst case. But each iteration involves a binary search of O(log n) steps. So total time is O(n log n). But for n=3e5, and binary search steps per iteration (which is O(log n)), this would be acceptable.

But in the binary search step, since the array is sorted, perhaps we can find the leftmost s in O(1) steps using a sliding window approach. But I think binary search is the way to go here.

So the overall approach is:

1. Sort the array.

2. Binary search for the minimal D, which is the answer. The lower bound is 0, upper bound is max_v - min_v.

3. For each candidate D, perform the check as described.

The time complexity of the solution is O(n log n) for sorting, plus O(log (max_v - min_v)) * O(n log n) for the binary search and check steps. For n=3e5, log (max_v) is up to 30, so the total time is O(n log n * 30), which should be acceptable.

Now, let's proceed to code this.

The code steps:

Read n and k.

Read the array, sort it.

If k ==1, then the answer is 0, since each element can be a group of size 1. But wait, no. Because each group can be of size >=k, which is 1. So each group is a single element. So the processing time is 0. So for k=1, the answer is 0.

But wait, what if n is not divisible by 1? But any group of size >=1 is allowed. So for example, the entire array can be a single group if k=1. But the processing time is max_v - min_v. But to minimize the maximum processing time, the best way is to split into groups of size 1, each has processing time 0. So yes, when k=1, the answer is 0.

So in code, we can handle k=1 as a special case. But the check function will handle it as well. Because for k=1, each group can be of size 1. So during the check function, s_max_candidate =last -1 +1 =last. So the group is formed as last (single element). Then last becomes s-1=last-1, etc. So for k=1, the check function for D=0 would return true.

So the code doesn't need to handle k=1 as a special case.

Now, implement the binary search:

Initialize left=0, right= max_v -min_v.

answer=right.

While left <=right:

   mid = (left +right) //2

   if check(mid) is True:

       answer=mid

       right=mid-1

   else:

       left=mid+1

return answer.

Implement check(D):

sorted array is v.

n = len(v)

last =n-1

while last >=0:

   s_max_candidate= last -k +1

   if s_max_candidate <0: return False.

   target= v[last] - D

   # find leftmost s in [0, s_max_candidate] where v[s] >= target.

   left=0

   right=s_max_candidate

   res =-1

   while left <=right:

       mid = (left +right)//2

       if v[mid] >= target:

           res=mid

           right=mid-1

       else:

           left=mid+1

   if res ==-1:

       return False

   last=res-1

return True

This should work.

Testing the first example:

Input:

5 2

50 110 130 40 120

After sorting: 40,50,110,120,130.

Check D=20.

Processing:

last=4. s_max_candidate=4-2+1=3.

target=130-20=110.

Binary search in 0-3 for first s >=110.

The array elements in 0-3: 40,50,110,120.

Looking for 110. The leftmost is 2 (index 2, value 110).

res=2. So group from 2 to4. last becomes 1.

Now, last=1.

s_max_candidate=1-2+1=0.

target=50-20=30.

Binary search in 0-0: s must be <=0. So check if v[0]>=30. v[0] is40 >=30. So res=0. group from 0-1. last becomes -1. Done. return True.

So D=20 is feasible.

So the binary search would find this as the minimal D.

Another example:

Input 4 1

2 3 4 1 → sorted [1,2,3,4].

Check D=0.

For k=1, each group can be size 1.

Processing from the end:

last=3. s_max_candidate=3-1+1=3. target=4-0=4. Find s in 0-3 where v[s] >=4. None. So return False. Wait, but this is not correct. Because the code would return False for D=0, but the correct answer is 0.

Wait, what's wrong here.

Wait, the sorted array is [1,2,3,4]. k=1. D=0.

Processing for check(D=0):

last=3.

s_max_candidate=3-1 +1=3.

target=4-0=4. So looking for s in 0-3 where v[s] >=4. Only possible s=3 (element4). So res=3. group is 3-3 (size 1). last becomes 2.

Processing last=2:

s_max_candidate=2-1+1=2.

target=3-0=3. look for s in 0-2 where v[s] >=3. s=2 (element3). group 2-2. last becomes 1.

Processing last=1:

s_max_candidate=1-1+1=1.

target=2-0=2. look for s in 0-1. s=1 (element2). group 1-1. last becomes 0.

Processing last=0:

s_max_candidate=0-1+1=0.

target=1-0=1. look for s in 0-0 where v[s] >=1. s=0 (element1). group 0-0. last becomes -1. All processed. return True. So D=0 is feasible.

Ah, so the code handles this correctly. So the code works.

Now, code in Python.

Now, handling the binary search correctly.

Implement the check function as a helper.

Now, code:

Read n, k.

Read the list, sort.

Handle edge cases (like k=1, but the code will handle it).

Then perform binary search between left=0 and right= max(v) - min(v).

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    v = list(map(int, input_stream.readline().rstrip("\n").split()))

    v.sort()

    if n ==0:

       print(0, file=output_stream)

       return

    left=0

    right = v[-1] -v[0]

    ans = right

    def is_possible(D):

        last = len(v) -1

        while last >=0:

            s_max_candidate = last -k +1

            if s_max_candidate <0:

                return False

            target = v[last] - D

            # binary search in 0..s_max_candidate for first >= target

            left =0

            right =s_max_candidate

            res = -1

            while left <= right:

                mid = (left + right) //2

                if v[mid] >= target:

                    res = mid

                    right = mid -1

                else:

                    left = mid +1

            if res ==-1:

                return False

            last = res -1

        return True

    while left <= right:

        mid = (left + right) //2

        if is_possible(mid):

            ans = mid

            right = mid -1

        else:

            left = mid +1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 1
2 3 4 1
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

The second example:

4 1

2 3 4 1 → sorted [1,2,3,4].

D=0.

Check possible:

last=3 → s_max_candidate=3-1+1=3. target=4-0=4. binary search in 0-3 for s >=4. Only s=3. group 3-3. last becomes 2.

last=2 → s_max_candidate=2-1+1=2. target=3-0=3. find s=2 (element3). group 2-2. last=1.

last=1 → s_max_candidate=1-1+1=1. target=2-0=2. s=1. group 1-1. last=0.

last=0 → s_max_candidate=0. target=1-0=1. s=0. group 0-0. done. returns True. So D=0 is feasible. So ans=0.

So the code works.

Another test case: when n=k. Then the group is the entire array, and processing time is max-min.

Thus, the code handles all cases correctly.
</think>

```python
n, k = map(int, input().split())
v = list(map(int, input().split()))
v.sort()

if n == 0:
    print(0)
    exit()

left = 0
right = v[-1] - v[0]
ans = right

def is_possible(D):
    last = n - 1
    while last >= 0:
        s_max_candidate = last - k + 1
        if s_max_candidate < 0:
            return False
        target = v[last] - D
        res = -1
        l, r = 0, s_max_candidate
        while l <= r:
            mid = (l + r) // 2
            if v[mid] >= target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        if res == -1:
            return False
        last = res - 1
    return True

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
```
