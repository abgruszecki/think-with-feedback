<think>
Okay, let's tackle this problem. So the problem is about fitting as many arrays as possible into the available memory clusters. The arrays need consecutive cells and can't split between clusters. The key here is to maximize the number of arrays placed. 

Hmm. Let's think about the approach. Each array requires 2^b_j cells. The memory clusters are a collection of sizes a_i, which are the sizes of the empty clusters. 

First, I need to sort both the clusters and the array sizes in a way that allows efficient matching. Since larger arrays can't fit into smaller clusters, but maybe we can fit multiple smaller arrays into a larger cluster. Wait, but the problem says that each array must fit into a cluster. Oh wait, no: a cluster is a sequence of consecutive empty cells. So each array must fit entirely within a single cluster. Because they can't be divided between clusters. Oh right. So each array must be placed into a cluster that is at least as large as the array's size. 

So the strategy is to assign the largest possible arrays first to the largest clusters, but perhaps there's a better way when you have multiple smaller arrays that can fit into a cluster. Wait, but if you have a large cluster, you can split it into multiple smaller arrays. For example, if a cluster is size 8, and you have two arrays of size 4 each, you can place both into the same cluster. So the cluster's size needs to be >= array size, and then the maximum number of arrays that can fit into it is (cluster size) divided by (array size). 

But how do we efficiently compute the maximum possible number of arrays? 

So here's the plan:

1. Sort the memory clusters in descending order. Because larger clusters can accommodate more arrays, especially when broken down into smaller chunks. For example, a cluster of 8 can handle one 8, two 4s, four 2s, etc. So handling larger clusters first allows us to use them optimally for the largest possible arrays.

2. Sort the array sizes (after converting their 2^b_j) in ascending order. Because we want to handle the smallest arrays first. Wait, no. Wait, maybe we should sort the arrays in descending order. Because if we have a cluster that can fit one big array or multiple small ones, but the big array is needed first. Wait, but the problem is to maximize the count. So, for example, if we have a cluster of 8 and arrays of size 8, 4, 4. Using the cluster for the 8 would allow one array, but using it for two 4s would allow two. So in that case, it's better to assign the smaller arrays first. So, maybe the optimal approach is to process the arrays in ascending order (smallest first), because then each array requires the smallest possible cluster, and allows more arrays to be placed. 

Wait, this is the classic greedy problem. The optimal approach is to sort the arrays in ascending order (smallest required size first) and the clusters in descending order. Then, for each array in order (from smallest to largest), try to fit it into the largest possible cluster that can accommodate it. Wait, but how? Let's think:

If we sort the clusters in descending order, and the array sizes in ascending order. Then, for each array (starting with the smallest), we find the first cluster that can fit it. Once that cluster is used, we subtract the array's size and possibly reuse the remaining part for future arrays. 

Wait, but the array must fit entirely in a cluster, but the cluster can be split into multiple arrays. For example, a cluster of 8 can fit two 4s. But the way to maximize the count is to take as many small arrays as possible. So, perhaps we can model each cluster's available size, and for each array, find how many times it can fit into the remaining clusters. 

But with n and m up to 1e6, we need an efficient way to do this. 

Alternative approach:

- Sort the clusters in descending order. For example, clusters [8,4,3,2,2]. Sort them as 8,4,3,2,2.

- Sort the arrays in ascending order (since 2^b_j is the size). For example, the arrays are 8,4,4. So sorted as 4,4,8. Wait no, sorted in ascending order. Wait, in the first example, the array sizes are 3 (which is 8), 2 (4), 2 (4). So sorted in ascending order of their 2^b_j, which would be 4,4,8. 

Wait, the arrays are 3,2,2 in the input. The sizes are 8,4,4. So sorted as 4,4,8. But when sorted in ascending order, that's 4,4,8. So we process the smallest arrays first. 

The idea is that by processing the smallest arrays first, we can fit them into the clusters that are just big enough, leaving the larger clusters for larger arrays. But in reality, processing the largest arrays first would require using up the largest clusters first. But this might not maximize the count. For example, if there's a large cluster that can fit multiple small arrays. 

So the optimal approach is to process the arrays in ascending order of size (smallest first) and the clusters in descending order. Then, for each array size s, we find the largest cluster that can fit s, and use it as much as possible, then proceed to the next array.

Wait, but how? Let's think of it this way:

We have a list of clusters sorted in descending order. For each array size s (sorted ascending), we want to see how many of them we can fit into the clusters. 

For example, let's say clusters are [8,4,3,2,2], and array sizes are [4,4,8]. 

Processing arrays in sorted order: 4,4,8.

First array s=4. We look for the largest clusters that can fit 4. The first cluster is 8. 8//4 = 2 arrays. So we can take two 4s here. That uses up the entire 8 (since 2*4=8). Then, the next array is 4. The next cluster is 4. 4//4=1. So that's one. Then the next array is 8. The next cluster is 3, which is too small. Then 2, etc. So total is 2 + 1 = 3. But the sample input's output is 2. Wait, that contradicts. Hmm. Wait the first sample's input is:

n=5, m=3. Clusters are 8,4,3,2,2. Arrays are 3,2,2 → their sizes are 8,4,4. So sorted arrays as 4,4,8. The correct output is 2. 

Wait, but according to the approach above, the two 4s could be placed into the 8 (two arrays) and the 4 (one array) for a total of 3. But the sample's answer is 2. Oh wait, because in the sample, the arrays are 8,4,4. So when sorted ascending, they are 4,4,8. 

Wait, but according to the sample's explanation, two arrays can be placed. So why the discrepancy? Because perhaps the approach of processing the arrays in ascending order and clusters in descending order is not correct. 

Wait let's think again. The first sample input:

Clusters: 8,4,3,2,2 (sorted descending). Arrays: 8,4,4 (sorted as 4,4,8). 

Processing arrays in ascending order:

First array is 4. Take the largest cluster, 8. 8//4 = 2. So we can fit two 4s here. Then, the next array is 4. But we already used the 8 to fit two 4s, and the next cluster is 4. 4//4=1. So that's another array. Then the last array is 8. The remaining clusters are 3,2,2. None can fit. So total is 2+1+0=3. But the sample's answer is 2. So this approach is wrong. 

Wait, but in the sample explanation, the correct answer is 2. So there's a problem here. Why?

Ah, because the arrays to be placed are m=3. The first sample's input is arrays of 8,4,4. So how can the maximum be 2? Because the sample explanation says:

Either place the 8 and one 4, which uses the 8 and 4 clusters. Or place two 4s in the 8 and none in the 4 cluster. Or use the 8 cluster for two 4s and the 4 cluster for nothing, but then the 8 array can't fit. So the maximum possible is two arrays. 

Wait, this is confusing. Let me re-examine the sample input.

Sample input 1:

Clusters: 8,4,3,2,2. Arrays: 8,4,4. So possible options:

Option 1: place 8 in the first cluster (8), then 4 in the second (4), then 4 can't fit. Total 2.

Option 2: place two 4s in the first cluster (8). Then the third array (8) can't fit. So total 2. So maximum is 2.

So according to the sample, the correct answer is 2. But according to the previous approach, the code would process the arrays in order 4,4,8 and compute 3. So that approach is wrong. 

So where is the mistake here? The problem is that the array sizes are not in the order of processing. Because the arrays in the sample are 8,4,4. If we process them in the order of 4,4,8, then the first two 4s can be placed in the 8 cluster (2 arrays), and the 8 would not fit. So total is 2. But according to the initial approach's calculation, that's not what happens. Wait, no. Because the array to be placed is 8, which is the third array. 

Wait, perhaps I got the array processing order wrong. Let me re-express the approach.

Wait, the arrays in the first sample are sizes 8,4,4. So sorted in ascending order is 4,4,8. So processing order is 4,4,8. The first array (4) can fit into the 8 cluster. So the 8 cluster can fit 8/4=2 arrays. So the two 4s can be placed into the 8 cluster. Then, the third array (8) can't fit into the remaining clusters (4,3,2,2). So total is 3? But sample's answer is 2. 

But that's a contradiction. So why the sample's answer is 2? Because the problem statement says that each array must be placed as a whole. So in the case of the two 4s, each array is an individual array. So the 8 cluster can fit two of them, which would require two arrays. So in the sample, the three arrays are 8,4,4. The code would place two 4s (using the 8 cluster) and the 8 array can't fit. So that's two arrays. Then the 4 array is placed in the next cluster (4). So total three? But the sample says the answer is 2. 

Wait, the sample's output is 2, but according to this reasoning, it should be 3. So there's a misunderstanding here. Let me re-examine the sample explanation.

In the first example:

The arrays are sizes 8,4,4. The available clusters are 8,4,3,2,2. 

The sample's explanation says that the answer is 2. So how? Because if you place two 4s into the 8 cluster (which uses two of the three arrays), then you have the 4 cluster left. The 4 array (the third array) can't be placed because the third array is 8. Wait, no: the arrays are 8 (from 3), 4 (from 2), 4 (from 2). So when sorted in ascending order of their size, they are 4,4,8. So when processing the two 4s first, they can both fit into the 8 cluster. Then the 8 array would require a cluster of 8, but the 8 cluster is already used. So the next available clusters are 4,3,2,2. None can fit 8. So total is 2+0=2. Which matches the sample's answer. 

Ah! So the arrays are sorted in ascending order. So the order is 4,4,8. The first two are 4 and 4. So when you process them first, the code would assign them to the largest possible clusters. So for the first array (4), the 8 cluster is used. It can fit two 4s. So the code would use that cluster to fit both 4s, which are two arrays. Then the third array is 8. But the 8 cluster is already used (split into two 4s). So the 8 array can't fit. So total is 2. 

So the problem is that when you have a cluster of 8 and two arrays of 4 each, you can fit both into the cluster, which uses up two arrays. Then, the third array (8) can't fit. So the answer is 2. 

So the approach must be to process the arrays in ascending order (smallest first) and assign them to the largest possible clusters. But how to manage the clusters' remaining capacity.

The key is that each cluster can be used to fit multiple arrays of the same size. So for each array size, we need to find the largest cluster that can fit it, and then see how many of that array size can be placed in the clusters.

Wait, but the arrays can have varying sizes. So for example, after placing some arrays of a smaller size, larger arrays may not have any clusters left. So the approach must be to sort the arrays in ascending order (smallest first) and process them in that order. For each array size, we want to use the largest possible clusters that can fit that size, and as many as possible. 

So here's the plan:

1. Sort the clusters in descending order. So that we can process them from largest to smallest.

2. Sort the array sizes (after converting 2^b_j) in ascending order. 

3. For each array size in the sorted list, we need to count how many times it can be placed into the clusters. But how?

Alternatively, for each array size s, we can iterate through the clusters (sorted descending) and for each cluster, compute how many arrays of size s can fit into it (floor(cluster_size / s)), then accumulate until we've covered all arrays of that size. But with m up to 1e6, and n up to 1e6, this approach would be O(n*m), which is way too slow.

So we need a more efficient way.

Alternative approach:

Group the array sizes. For example, if multiple arrays have the same size s, we can process them together. Then, for each s, find how many clusters can contribute to the count. 

So steps:

1. Sort the clusters in descending order. Let's call the sorted list as A.

2. Sort the array sizes in ascending order, and group them into frequency counts. For example, if there are x arrays of size s. 

But even this, the processing could be O(n + m) which is manageable.

Wait, let's see. Suppose we have all array sizes sorted. Then, for each s in the sorted array, we need to assign as many as possible arrays of size s into the clusters, using the largest possible clusters first.

But the problem is that once a cluster is used (partially) for a certain size, the remaining part can be used for smaller sizes. 

So how to model the clusters after each allocation.

This sounds like a problem where the clusters are initially sorted, and for each array size, we track how much of each cluster is available. But for large n and m, this is impractical.

An alternative approach is to model the clusters as a multiset of available sizes. For each array size s, we need to find the largest cluster >= s, then take as many s as possible from that cluster, subtract s * k from the cluster, and add the remainder (if any) back into the multiset. But with m up to 1e6, even this approach would be O(m log n), which may be acceptable. But the problem is that 1e6 * log 1e6 is about 20 million operations, which should be manageable in Python. But in practice, Python's data structures may not be efficient enough.

But given the time constraints, let's think of an optimized way.

Another idea: since clusters are sorted in descending order, and array sizes are sorted in ascending order, perhaps we can use a two-pointer approach. 

Let's imagine that we process the array sizes in ascending order (smallest first). For each size s, we want to find the earliest cluster in the sorted list that is >= s. Once found, we can use as many of the s-sized arrays as possible from that cluster, then proceed to the next cluster. 

But how to track how many arrays of s can be placed into each cluster. 

Wait, but the array sizes are sorted. So once we process a certain s, all remaining s's are larger or equal. So once a cluster is used to fit some s, the remaining part of the cluster can be used for larger s's.

Wait, no. Because the array sizes are processed in ascending order. So after processing s, all next arrays are larger or equal. So the remaining part of a cluster after using it for s is not useful for the next arrays (since they are larger than s). Therefore, once a cluster is partially used for s, the remaining part can't be used for larger s's. Because larger s's need larger cluster sizes. 

Therefore, the optimal way is to, for each s (in ascending order), and for each cluster (processed in descending order), use as many of s as possible from the cluster, then any remaining part is left for future s's (but since future s's are larger, the remaining part is irrelevant). So for each cluster, once processed for a certain s, any remaining part can't be used for future s's. 

Wait, but this is not true. For example, a cluster of 8 is used for two 4s. The remaining part is 0. But if the next s is 8, there's no space. But if the next s is 3, but the cluster is already used. 

So, the approach is: for each s in ascending order, process the clusters in descending order. For each cluster that is >= s, compute how many s's can fit (k = floor(cluster / s)), and subtract as many as possible from the required count for s. 

But how to manage the clusters.

Let me think of this as follows:

We have the clusters sorted in descending order. For each s in the array's sorted list (ascending), we iterate through the clusters until we find a cluster >= s. Then, for each such cluster, we calculate how many s's can be placed in it (floor(cluster / s)). Then, we take as many as possible, up to the remaining number of s arrays. 

But this approach would require for each s to iterate through the clusters until the remaining s's are filled or the clusters are exhausted. But with m up to 1e6 and n up to 1e6, this would be O(n*m), which is not feasible. 

Thus, this approach is not efficient enough.

Alternative Idea:

Group the array sizes and process them in ascending order. For each size s, compute the total number of arrays of size s. Then, find the maximum number of arrays of size s that can be placed in the available clusters. 

But how to compute that.

For a given s, the maximum number of arrays that can be placed is the sum over all clusters of (cluster_i // s). But we have to consider that clusters may have been used for previous s's. Wait no. Because when we process the arrays in ascending order, the clusters are considered in their original size, since previous s's are smaller than current s. For example, if a cluster was used to fit some s_prev (smaller than current s), then the remaining part of the cluster is cluster_i - k * s_prev. But since s_prev is smaller than current s, the remaining part (if any) is less than s_prev. So for current s, the remaining part is not enough. Therefore, we can model the clusters as their original size, but for each s, the total possible arrays is sum (a_i // s). However, this sum must be >= the number of arrays of size s and all larger s's. But this is not correct, because once a cluster is used for a larger s, it's possible that it can't be used for smaller s's. 

Wait, but since we process the arrays in ascending order (smallest first), the clusters can be used multiple times. For example, a cluster of 8 can fit two 4s (s=4), then after that, the cluster is used up, but if the arrays were processed in reverse order, perhaps the 8 could have been used for a single 8 array. 

Therefore, the correct approach is to process the arrays in descending order. Let's think again.

Wait, if we process the arrays in descending order (largest first), and the clusters in descending order. Then, for each array size s, we take the first available cluster that can fit s, and place it there. This way, larger arrays take the largest clusters, and smaller arrays can fit into the remaining parts. 

But this approach might miss the optimal count. For example, a large cluster can fit multiple small arrays. 

But how to decide which approach is correct.

Let's consider the first sample again. If arrays are processed in descending order (8,4,4):

First, the 8 array is placed into the 8 cluster. Then, the two 4 arrays are placed into the 4 cluster (1 array) and the 3 cluster (0), etc. So total 3 arrays. But the sample's answer is 2. So this approach is wrong. 

So clearly, this approach is incorrect.

But the sample's correct answer is 2. So why is that?

Ah, because the problem statement says that each array must be placed into a single cluster. So the 8 array takes the entire 8 cluster. The two 4 arrays can be placed into the 4 cluster (1) and perhaps another cluster. For example, the 3 cluster can't fit. So only one 4 array can be placed, totaling 1 + 1 = 2. Which matches the sample. 

So in this case, processing the arrays in descending order (largest first) gives the correct answer. 

But how?

So the key is that when you process larger arrays first, you use up clusters that could have been used for smaller arrays. Which could result in fewer total arrays placed. 

So which approach is correct: processing arrays in ascending or descending order?

This is the crux of the problem. To maximize the number of arrays placed, we need to decide whether to process smaller arrays first (to fit more of them into larger clusters) or larger arrays first (to use the clusters optimally for larger arrays).

The correct approach must be to process the arrays in ascending order. Because smaller arrays can fit into larger clusters, allowing multiple arrays per cluster, leading to a higher count. 

But the sample shows that this approach can lead to a higher count than the correct answer, but the sample's correct answer is lower. So what's the mistake here?

Wait, in the first sample, processing the arrays in ascending order (4,4,8) allows two 4s to be placed into the 8 cluster (total of two arrays). The third array (8) can't be placed, so the answer is two. Which matches the sample. So that approach works. 

But how does the code decide how many arrays can fit into each cluster for each s?

The correct approach is:

- Sort the array sizes in ascending order. This way, we handle the smallest possible arrays first. 

- Sort the clusters in descending order.

- For each array size s in ascending order, iterate through the clusters (starting from the largest) and for each cluster >= s, compute how many arrays of size s can fit into it (cluster // s). Add the minimum of (remaining arrays of size s, cluster//s) to the total count, and subtract this from the remaining arrays of size s. If no more arrays of size s are left, break and move to the next size. 

But how to manage this efficiently. 

For example, if we have multiple array sizes, we need to process each size, and for each, find how many clusters can contribute to that size. 

But with m up to 1e6, this approach is O(m*n), which is not feasible. 

So we need a way to group the array sizes. 

So here's the optimized approach:

1. Sort the array sizes in ascending order. Also, group the same sizes together. For example, count how many arrays are there for each s. Let's say we have a list of (s, count) pairs, sorted by s in ascending order.

2. Sort the clusters in descending order. 

3. For each s in the sorted list of array sizes (ascending order):

   a. For each cluster in the sorted clusters (descending order):

      i. If cluster < s, break, since all remaining clusters are smaller than s.

      ii. Compute the maximum number of arrays of size s that can fit into this cluster: k = cluster // s.

      iii. Take the minimum between k and the remaining count for s.

      iv. Subtract this from the remaining count and add to the total.

      v. Update the cluster to cluster - (k_used * s). But wait, after using some arrays in the cluster, the remaining space is cluster % s. But since we're processing arrays in ascending order, future arrays will be larger than or equal to s. Therefore, the remaining space (which is less than s) can't be used for any future arrays. So once we use a cluster for s, we can effectively mark it as used, since any remaining space is useless for larger s's. 

   b. Once all clusters are processed for this s, if there are remaining arrays of s, they can't be placed and are skipped.

But this approach is O(n * m), which is not feasible for n and m up to 1e6. 

So this approach is too slow. We need a better way.

Alternative Idea:

We can precompute for each cluster the maximum s that can fit into it, and then for each s, the number of clusters that can fit at least s. But how to use this.

Wait, the total possible arrays of size s is the sum over all clusters (a_i >= s) of (a_i // s). But this is the maximum possible for s. If the sum is >= the number of arrays of size s, then all arrays of s can be placed. Otherwise, only up to the sum can be placed. 

But how to compute this efficiently. 

But since the array sizes are up to 1e9 (since 2^b_j can be up to 1e9), we need a way to compute for each s in the array, the sum of (a_i // s) for a_i >= s. 

But the a_i's can be up to 1e9 as well. 

So the problem reduces to, for each s in the array, compute sum_{a_i >= s} (a_i // s). Then, the answer is the sum over all s of min(count_s, sum_floor), but we need to subtract overlapping counts. Because once a cluster is used for a certain s, it's still available for larger s's. 

Wait, no. Because the sum_floor is calculated for each s based on the original a_i. But in reality, when you place arrays of size s1 into a cluster, the remaining space (a_i % s1) may be less than s2 (s2 >= s1), so it's not possible to use that cluster for s2. 

Therefore, the sum_floor for s2 would not include that cluster. 

But this means that the sum_floor approach would overcount, as it doesn't account for the fact that clusters are used for smaller s's. 

Thus, the initial approach of processing the arrays in ascending order and greedily using the largest clusters first is correct, but the problem is how to compute this efficiently. 

Alternative Idea:

For each s in the sorted array sizes, sorted in ascending order, compute how many arrays of size s can be placed into the clusters, considering that the clusters have not been used by larger arrays (since we process s in ascending order). 

In other words, when processing s in ascending order, the clusters are available in their original sizes. Because any cluster that is used for s can't be used for larger s's (since s is processed in ascending order). 

Wait, no. Because s is being processed in ascending order. So after processing s, future s's are larger. So when you use a cluster for s, the remaining space is a_i % s. Since future s's are larger than or equal to s, the remaining space (which is less than s) is not sufficient for any future s's. Therefore, once a cluster is used for s, it's effectively exhausted for future s's. 

Therefore, the sum_floor for s is sum (a_i // s) for all a_i. But once you place k arrays of s into a cluster, that cluster's contribution to larger s's is (a_i - k * s) // s_new. But since s_new >= s, (a_i -k*s) may be less than s_new. 

So the initial sum_floor approach is not applicable, as it doesn't account for the usage of clusters for smaller s's. 

So the correct approach must process the arrays in ascending order, and for each array, greedily use the largest possible clusters first, subtracting the used space. But how to do this efficiently. 

An efficient way to do this is to use a priority queue (max-heap) to keep track of the available clusters. For each s in sorted array sizes:

   While there are clusters >= s and there are arrays left to place:

      Take the largest cluster from the heap.

      Compute how many arrays of size s can fit into it (k = cluster // s). 

      Take the minimum between k and the remaining arrays of s.

      Add this to the total.

      Subtract the used arrays from the remaining count.

      Compute the remaining space (cluster - used * s). 

      If the remaining space > 0, add it back to the heap. 

This way, each cluster is split into the maximum number of s arrays, and the remaining space is available for larger s's. 

But in this approach, since s is processed in ascending order, the remaining space (after using s) is less than s, so for larger s's, the remaining space is not enough. So the remaining space is only useful if s_new <= remaining space. But since s is processed in ascending order, s_new >= s. So the remaining space is s_remain = cluster % s. Since s_new >= s, s_remain < s <= s_new. Therefore, the remaining space can't be used for any larger s's. 

Therefore, once a cluster is used for s, the remaining space is useless and should not be added back to the heap. 

So the correct approach is:

- Use a max-heap to track the available clusters. 

- Sort the array sizes in ascending order.

- For each s in the array sizes:

   While there are arrays of s left and the heap is not empty:

      Take the largest cluster from the heap.

      If cluster < s: break (since all remaining clusters are smaller).

      k = cluster // s

      take m = min(k, remaining arrays of s)

      total += m

      remaining arrays of s -= m

      used = m * s

      remaining_cluster = cluster - used

      if remaining_cluster > 0:

          push remaining_cluster back into the heap.

But wait, this is incorrect. Because after placing m arrays of size s into the cluster, the remaining_cluster is cluster - m*s. 

But since we are processing s in ascending order, the remaining_cluster can be added back to the heap for possible use by larger s's. 

But s is being processed in ascending order. So the next s's are larger than or equal to s. Therefore, the remaining_cluster (which is cluster - m*s) must be less than s. Because m is the maximum possible (k = cluster//s, so m*s <= cluster). 

But the next s's are >= s. So the remaining_cluster (which is < s) can't be used for any s_new >= s. 

Therefore, the remaining_cluster should not be added back to the heap. Because it's useless for any future s's. 

Thus, the correct approach is:

For each s in sorted array sizes (ascending order):

   while remaining arrays of s > 0 and there are clusters >= s:

      take the largest cluster >= s.

      k = cluster // s.

      m = min(k, remaining)

      total += m

      remaining -= m

      cluster -= m*s

      if cluster >0:

          no, because m is the maximum possible (k is cluster//s). So cluster after subtraction would be cluster - m*s, which is less than s. So adding it back to the heap is pointless. 

So the cluster is discarded after processing. 

Therefore, the algorithm is:

Sort the array sizes in ascending order. 

Sort the clusters in descending order. 

Use a pointer to track the current cluster. 

Initialize a pointer i = 0 (points to the first cluster). 

For each s in sorted array sizes:

   while remaining arrays of s >0 and i <n and clusters[i] >=s:

      k = clusters[i] // s

      take m = min(k, remaining)

      total +=m

      remaining -=m

      i +=1

   if remaining arrays of s >0:

      break and proceed to next s.

But this is not correct, because clusters after the current i may have larger clusters. For example, if we have clusters [5,4,3], and s=2. 

Processing s=2:

clusters[0] =5 → 5//2=2. If we have 3 arrays of size 2, we take 2 from cluster 0. Then, cluster 0 is 1, which is less than 2. Then i increments to 1. But cluster 1 is 4, which is >=2 and can fit 2 arrays. So we can process cluster 1. 

But the current approach would skip cluster 1 after incrementing i. 

Ah, this is a problem. 

Thus, the pointer approach is not correct. 

Therefore, the correct approach is to use a priority queue (max-heap) to keep track of the available clusters. 

But building a max-heap in Python is possible using the heapq module, but since Python's heapq is a min-heap, we can invert the values. 

So here's the plan:

1. Sort the array sizes in ascending order.

2. Sort the clusters in descending order.

3. Use a max-heap to keep track of the available clusters. Initially, push all clusters into the heap (as negative values to simulate a max-heap).

4. For each s in sorted array sizes:

   a. While there are remaining arrays of s and the heap is not empty:

      i. Pop the largest cluster from the heap (by taking the negative of the min-heap's top).

      ii. If the cluster < s: discard it (since no larger clusters are left) and continue.

      iii. Compute k = cluster // s.

      iv. m = min(k, remaining)

      v. total += m

      vi. remaining -= m

      vii. new_cluster = cluster - m*s

      viii. If new_cluster >= s:

          # This can't happen, since m = min(k, remaining), and k = cluster//s. So m*s <= k*s <= cluster. So new_cluster = cluster - m*s >=0. But if m is the maximum possible (k), then new_cluster is cluster % s, which is < s. So new_cluster < s. So we don't need to push it back.

      ix. If new_cluster >0 and new_cluster >= next s's (but s is in ascending order, so next s's are larger, so new_cluster is < s and thus can't be used). So we discard new_cluster. 

      x. If new_cluster >0 but s is the last s, discard it.

   b. If there are no remaining arrays of s, proceed to next s.

But this approach would require pushing back the new_cluster only if it's >= s, which can't happen. So we don't push it back. 

But then, this approach would process each cluster once per s. Which is O(n * m), which is again not feasible for n and m up to 1e6. 

But wait, the array sizes are grouped. For example, multiple arrays of the same s. 

Thus, grouping the arrays into counts per s can reduce the number of operations. 

So here's the optimized plan:

- Sort the array sizes in ascending order, and count the frequency for each s. So we have a list of (s, count) pairs sorted by s. 

- Sort the clusters in descending order. 

- Use a max-heap (using negatives for Python's heapq).

- For each (s, count_s) in the sorted list:

   a. while count_s >0 and heap is not empty:

      i. Pop the largest cluster (current_cluster = -heapq.heappop(heap)).

      ii. if current_cluster < s:

          # This cluster is too small for any future s's, so discard.

          continue

      iii. max_possible = current_cluster // s

      iv. use = min(max_possible, count_s)

      v. total += use

      vi. count_s -= use

      vii. remaining_cluster = current_cluster - use * s

      viii. if remaining_cluster >= s:

          # impossible, since use is current_cluster // s.

          # So remaining_cluster = current_cluster mod s < s

          pass

      ix. if remaining_cluster > 0:

          # but since s is processed in ascending order, remaining_cluster < s and next s's are >= s. So no use.

          # discard remaining_cluster.

      x. else:

          # cluster is exactly used up.

          pass

   b. After processing all clusters, if count_s >0, break (can't fit all arrays of this size and beyond).

But this approach is O(m log n), which is acceptable. 

Wait, but each cluster can be pushed and popped from the heap once per s. For example, a cluster of 1e9 could be popped for each s in the sorted array sizes. But if the array sizes are up to 1e6, and each pop is O(log n), this is O(m log n), which for m=1e6 and n=1e6 is 1e6 * 20 = 2e7 operations, which is manageable. 

But what's the actual complexity? Let's think: for each array size s, we process clusters until we can't fit any more of s. Once a cluster is processed for s, it is discarded (since the remaining part is < s and future s's are larger). 

So each cluster is processed at most once. Because once it's popped from the heap for a particular s, and it's >= s, it's either used for s (and the remaining part is discarded) or it's < s (and thus, any future s's are larger, so it's discarded). 

Wait, no. Because for each s, we process all clusters that are >= s. For example, a cluster of 8 may be processed for s=4, then for s=2 (but it's already used and the remaining is 0). So no. Once a cluster is processed for s=4, it's removed from the heap and not considered again. 

Thus, each cluster is popped from the heap exactly once. So the total number of heap operations is O(n), plus the initial building of the heap. 

Wait, no. Because for each s, the code may process some clusters. For example, the first s may process a few clusters, which are then discarded. The next s may process some more clusters. 

But in total, each cluster is popped once. Because once a cluster is popped and processed, it is either used (and the remaining part is discarded) or it's too small for s and thus discarded. 

Therefore, the total number of heap operations is O(n). Because each cluster is pushed once (during initialization) and popped once. 

So the time complexity is O(n log n) for building the heap (initial push), and O(n log n) for all the pops. Then, for each array size s, we process the clusters until count_s is zero or the heap is empty. But since each cluster is processed once, the total number of operations is O(n log n + m log n). 

But m can be up to 1e6, and n up to 1e6, and log n is around 20. So 1e6 * 20 is 2e7, which is manageable. 

So this approach is feasible. 

Now, let's see how to implement this in Python. 

Implement steps:

1. Read n and m.

2. Read a list of a_i's. 

3. Read the list of b_j's. Convert each to s_j = 2^b_j. 

4. Sort the a list in descending order and push them into a max-heap. Wait, no. The heap is a max-heap, so we can push the negative values. 

But in Python, the heapq module is a min-heap, so to simulate a max-heap, we push the negative values. 

So:

import heapq

clusters = list(map(int, input().split()))
clusters.sort(reverse=True)
heap = []
for c in clusters:
    heapq.heappush(heap, -c)

5. Convert the b list to s list, count frequencies. 

s_list = list(map(lambda x: 2**x, list_of_bs))
s_list.sort()
from collections import defaultdict
freq = defaultdict(int)
for s in s_list:
    freq[s] +=1
sorted_s = sorted(freq.keys())

Wait, no. We need to process the s in sorted order. So group the frequencies for each s. 

But perhaps it's more efficient to sort the list of s's, then iterate through them, grouping consecutive duplicates. 

For example:

s_list = sorted(2**b for b in bs)

Then, group them into (s, count). 

This can be done by iterating and counting consecutive elements. 

For example:

current_s = s_list[0]
count =1
grouped = []
for s in s_list[1:]:
    if s == current_s:
        count +=1
    else:
        grouped.append( (current_s, count) )
        current_s = s
        count =1
grouped.append( (current_s, count) )

Then, grouped contains the sorted s and counts. 

Now, for each (s, count) in grouped:

   process as described. 

So the code outline is:

total =0

for s, count_s in grouped:

    while count_s >0 and heap:

        current_cluster = -heapq.heappop(heap)

        if current_cluster < s:

            # can't use, and since heap is max-heap, all remaining clusters are smaller than current_cluster, which is <s. So break.

            heapq.heappush(heap, -current_cluster)  # put it back, since there's no use

            break

        max_possible = current_cluster // s

        use = min(max_possible, count_s)

        total += use

        count_s -= use

        remaining_cluster = current_cluster - use * s

        if remaining_cluster >0:

            # push back only if it can be used for larger s's?

            # since s is processed in ascending order, remaining_cluster < s. So no. So discard. 

        # else, cluster is exactly used. 

    if count_s >0:

        # can't fit all arrays of size s. 

        # but proceed to next s.

Thus, the key step is to break out of the loop when the current_cluster is < s. Because the heap is a max-heap, the next clusters are all smaller than current_cluster, which is less than s. So there's no point in checking them. 

But in the code above, after popping current_cluster and finding it's < s, we need to put it back into the heap. Because there might be other clusters in the heap that are larger than current_cluster but still < s. 

Wait, no. Because the heap is a max-heap. So when we pop the largest cluster. If that cluster is less than s, then all other clusters in the heap are also less than s. Because the heap is a max-heap. 

Yes. Because the largest cluster is current_cluster. If current_cluster < s, then all other clusters in the heap are <= current_cluster (since we popped the largest). So they are all < s. 

So in that case, we can break the loop. 

But in the code above, when current_cluster is < s, the code breaks and pushes the current_cluster back into the heap. 

But this is unnecessary. Because all other clusters are <= current_cluster (which is <s), so they are also <s. So pushing back current_cluster into the heap is not needed. Because we are breaking the loop and not processing further. 

But this will leave the current_cluster in the heap for future s's. But future s's are larger than current s, so this cluster is even less useful. 

But in the code above, after popping the current_cluster and finding it's <s, we push it back into the heap. This is a mistake. Because if current_cluster is the largest in the heap and is <s, then all other clusters in the heap are smaller than s. So we can break and discard the current_cluster. Because the next time the heap is accessed, this cluster will be popped again and again, but since future s's are larger, it's even less useful. 

Wait, but the code is processing s in ascending order. So for the next s', which is larger than s, the current_cluster (which is <s) will be even smaller than s', so it can't be used. 

Therefore, once a cluster is popped and found to be <s, it can be discarded, not pushed back into the heap. Because future s's will not need it. 

Thus, the code should be:

if current_cluster < s:

    break  # no need to push back.

But this would discard the current_cluster, which may have been pushed into the heap earlier. 

Wait, the code is:

for each s in sorted_s:

    while count_s >0 and heap not empty:

        current_cluster = -heapq.heappop(heap)

        if current_cluster < s:

            break

        process...

But this is not correct. Because once we pop the current_cluster and it's <s, we break the loop and don't push it back. So the current_cluster is lost. 

But in reality, since the heap is a max-heap, the current_cluster is the largest remaining. So if it's <s, then all other clusters are also <s. So pushing it back is unnecessary. 

But the code in this case would have popped the current_cluster, which is part of the heap. So if it's not pushed back, the heap will lose that cluster. 

Which is a problem. 

So the correct approach is:

When we pop a cluster from the heap, check if it's >= s. If yes, use it. If not, we need to put it back into the heap. 

But no. Because if the largest cluster is <s, then all other clusters are <= it. So the next time, when processing a larger s', all clusters are <s, which is smaller than s'. So they are of no use. 

Thus, once a cluster is popped and found to be <s, we can discard it (not put it back), and continue processing other clusters. 

But this is incorrect, because other clusters may be smaller than s but larger than other s's. 

Wait, no. For example, suppose s is 4. The largest cluster is 3. So after popping it, since 3 <4, we break. But there are other clusters, like 2,1. So in future s's, like 5, these are even less useful. 

Thus, once a cluster is popped and found to be <s, and s is the current s being processed, then all other clusters in the heap are <= current_cluster <s. So they are not useful for s, and future s's are larger. 

Therefore, once the largest cluster is <s, we can discard all remaining clusters. 

Thus, the code should be:

when current_cluster < s:

   break

But then, the current_cluster is discarded (not put back into the heap). 

But this would lose all the remaining clusters in the heap. 

No. Because the heap is a max-heap. When we pop the current_cluster, which is the largest, and it's <s, then all remaining clusters in the heap are <= current_cluster. So they are all <s. So for this s, they are of no use. And for future s's, which are larger, they are also of no use. 

Thus, once we find a cluster <s, we can discard it and all other clusters in the heap, as they are all <s. 

Therefore, the code should break and not push the current_cluster back. 

But this would cause those clusters to be removed from the heap, and thus not available for future s's. But since future s's are larger, they are not useful. 

Thus, the code is correct. 

So the code for processing each s is:

for s, count_s in grouped:

    while count_s >0:

        if not heap:

            break

        current_cluster = -heapq.heappop(heap)

        if current_cluster < s:

            # no more clusters can fit s, and all others are smaller

            heapq.heappush(heap, -current_cluster)  # put it back, but we break

            break

        # process this cluster

        max_possible = current_cluster // s

        use = min(max_possible, count_s)

        total += use

        count_s -= use

        remaining_cluster = current_cluster - use * s

        # remaining_cluster is current_cluster % s, which is <s.

        # no use for future s's. So discard.

    # end of while

But this code has a problem. Suppose we popped current_cluster, and it's >=s. We process it, then in the next iteration of the loop, we pop the next largest cluster, which may be >=s. 

But after processing, we discard the remaining_cluster. 

But this is correct, because the remaining_cluster is <s. 

So the code would process all clusters >=s for this s. 

But this approach may pop all clusters from the heap each time. For example, if the clusters are sorted in descending order, and s is small, the code will process all clusters for s. 

But this is O(n) for each s, which is not feasible if there are many s's. 

But with the grouping of s's, the number of s's is O(m), but after grouping, it's O(k), where k is the number of distinct s's. 

So if m is 1e6 but all arrays have the same s, then the grouping reduces it to one s. 

In this case, the code will process all clusters once. 

But for the worst case where all s's are distinct and in ascending order, the code will process each cluster once for each s. But since s is increasing, each cluster is processed once. 

Thus, the total number of operations is O(n log n) for heap operations plus O(k) for the grouped s's, which is acceptable. 

So the code outline is correct. 

Now, let's test this approach against the sample input.

Sample Input 1:

5 3

8 4 3 2 2

3 2 2

The s_list is 8,4,4. Sorted is 4,4,8. Grouped is [(4,2), (8,1)].

Clusters are sorted in descending order: 8,4,3,2,2. The heap is built with these values. 

Processing s=4, count_s=2:

current_cluster is 8. 

max_possible=8//4=2. use=min(2,2)=2. count_s becomes 0. 

remaining_cluster=8-2*4=0. 

total becomes 2. 

So the code would process this and exit the loop. 

Next, s=8, count_s=1:

Check the heap. The next clusters are 4,3,2,2. 

But the heap was built with 8,4,3,2,2. 

Wait, no. Wait, after processing s=4, the code processed the 8 cluster. The remaining clusters are 4,3,2,2. 

But in the code, the heap is being used as a max-heap. 

Wait, initial heap is built with [8,4,3,2,2], but stored as negatives. 

When s=4 is processed:

We pop 8 (current_cluster =8). 

Use it for 2 arrays of 4. 

remaining_cluster=0, not pushed back. 

So the heap now contains [-4, -3, -2, -2]. 

So when processing s=8:

pop 4 (current_cluster=4), which is <8. 

So push back 4 into the heap and break. 

So no arrays are placed. 

Thus, total is 2. Which matches the sample. 

Thus, the code works for the first sample. 

Second sample:

Input:

10 6

1 1 1 1 1 1 1 1 1 1

0 0 0 0 0 0

s_list: 1,1,1,1,1,1. sorted as six 1s. grouped is [(1,6)]

Clusters are all 1. Sorted descending: 10 1's. 

Processing s=1, count_s=6. 

We need to process each cluster. Each cluster is 1, which >=1. 

Each cluster can fit 1 array. So 10 clusters, 6 arrays. So total 6. 

Thus, the code works. 

Thus, the code should handle both samples correctly. 

Now, the Python code:

First, read the input. 

Then, process as per the steps. 

But handling large input efficiently. 

Now, code:

Testing against sample input 1.

```python
import heapq
from collections import defaultdict


def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr +=1
    m = int(input[ptr])
    ptr +=1
    a = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    b = list(map(int, input[ptr:ptr+m]))
    ptr +=m

    # Compute s_list
    s_list = [ (1 << bi) for bi in b ]
    s_list.sort()

    # Group s_list into (s, count)
    grouped = []
    if not s_list:
        print(0, file=output_stream)
        return
    current_s = s_list[0]
    count =1
    for s in s_list[1:]:
        if s == current_s:
            count +=1
        else:
            grouped.append( (current_s, count) )
            current_s = s
            count =1
    grouped.append( (current_s, count) )

    # Build max heap of clusters
    heap = []
    for c in a:
        heapq.heappush(heap, -c)

    total =0

    for s, cnt in grouped:
        remaining = cnt
        while remaining >0 and heap:
            current_cluster = -heapq.heappop(heap)
            if current_cluster < s:
                # No more clusters can fit s, push back and break
                heapq.heappush(heap, -current_cluster)
                break
            # Compute how many can be taken
            max_possible = current_cluster // s
            take = min(max_possible, remaining)
            total += take
            remaining -= take
            # Compute remaining_cluster
            remaining_cluster = current_cluster - take * s
            if remaining_cluster >0:
                # But it's <s, so no use for future s's. Discard.
                pass
            # else, it's zero, discard.
        if not heap:
            break  # no more clusters left

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 6
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0
""",
            "output": \
"""\
6
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

Sample 2:

Clusters are 10 1's. 

grouped is [(1,6)].

For s=1, process 6 clusters, each 1. Take 1 each. 

Total 6. 

Thus, the code works.
</think>

```python
import heapq
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr + n]))
    ptr += n
    b = list(map(int, input[ptr:ptr + m]))
    ptr += m

    s_list = [1 << bi for bi in b]
    s_list.sort()

    grouped = []
    if not s_list:
        print(0)
        return
    current_s = s_list[0]
    count = 1
    for s in s_list[1:]:
        if s == current_s:
            count += 1
        else:
            grouped.append((current_s, count))
            current_s = s
            count = 1
    grouped.append((current_s, count))

    heap = []
    for c in a:
        heapq.heappush(heap, -c)

    total = 0

    for s, cnt in grouped:
        remaining = cnt
        while remaining > 0 and heap:
            current_cluster = -heapq.heappop(heap)
            if current_cluster < s:
                heapq.heappush(heap, -current_cluster)
                break
            max_possible = current_cluster // s
            take = min(max_possible, remaining)
            total += take
            remaining -= take
            remaining_cluster = current_cluster - take * s
            if remaining_cluster > 0 and remaining_cluster >= s:
                heapq.heappush(heap, -remaining_cluster)
        if not heap:
            break

    print(total)

if __name__ == "__main__":
    main()
```
