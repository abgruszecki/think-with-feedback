<think>
Okay, let's try to figure out this problem. So the problem is about Appleman and Toastman splitting groups of numbers and calculating the maximum possible score. Hmm.

The initial group is given to Toastman, who adds the sum to the score. Then Appleman splits it into two non-empty groups. This process repeats until all groups are single elements. The goal is to find the maximum possible score they can achieve.

Let's think about what contributes to the score each time a group is processed. Every time a group is split, the sum of that group is added again when the subgroups are processed. For example, in the first example, the group [3,1,5] is split into [3,5] and [1]. The sum 9 is added once, then the subgroups 8 and 1 are added. Then [3,5] is split into 3 and 5, adding 8 again, but then each of those adds 3 and 5 again. Wait, but how does that work?

Wait, the process is that each time a group is split, the subgroups are passed back to Toastman. So for any group larger than 1 element, it's split into two, and each split contributes the sum of the subgroups once. So the total contribution of a group's sum depends on how many times it is split. Or maybe how many times the group is split into subgroups, each time adding their sums.

Wait, let's take the first example. The initial group is [3,1,5]. Sum is 9, added once. Then it's split into [3,5] (sum 8) and [1] (sum 1). Both are added to the score. Then the [3,5] is split into [3] and [5], adding 3 and 5. So the total for the initial group is 9 (initial) + 8 (from split) +1 (from split) +3 (split of 8) +5 (split of 8). Wait, but then how many times does each element's value get added?

Alternatively, maybe each element is added to the score as many times as the number of times it's included in a group that is passed to Toastman. For example, the element 3 is part of the initial group, then part of [3,5], then as [3]. So it's added 3 times. Similarly, 5 is added three times. The 1 is part of the initial group and then as a single element, so added twice. So the total is (3+1+5) + (3+5) +1 +3 +5 = 9+8+1+3+5=26.

Hmm. So each element's contribution depends on how many times it's part of a group that is processed by Toastman. So to maximize the total score, we need to maximize the sum of all elements multiplied by the number of times they are included in a group.

But how is the number of times determined by the splitting process? Let's model this.

Every time a group is split into two, each element in that group will be part of exactly one of the two subgroups. So, each split increases the count by one for each element in the group. Because the group is split once, and each element is in one subgroup, which will be processed again. So for example, if a group of size k is split, each element in it is now part of a subgroup (so their count increases by 1). Then each of those subgroups may be split again, leading to more increments.

Wait, maybe each element's total contribution is equal to the number of times it appears in any group passed to Toastman. The initial group counts once, then each split adds more groups.

So for example, the initial group is processed once. Then when split into two groups, each of those is processed once. Then splitting those into two more groups (if possible) each of those is processed once. So the total times an element is included is equal to the number of groups it's part of during the process.

So the problem reduces to determining for each element a_i, how many groups it's part of, then sum a_i multiplied by that count.

So the key is to find for each a_i, the number of times it's part of a group that is processed by Toastman, and sum all a_i * count_i.

Now the question is, how to compute count_i for each a_i.

Let's think about the splitting process. Every group that has more than one element must be split into two groups. The way the groups are split can affect the count_i. But since we want to maximize the total score, we need to choose splits such that the sum of a_i * count_i is maximized. However, perhaps the maximum sum is achieved regardless of the splitting method, as long as the splitting is done optimally. So maybe there's a mathematical way to compute the counts based on the initial structure of the array.

Wait, perhaps the maximum score is achieved by splitting the groups in a way that each element's count is as large as possible. How can we model that?

Alternatively, perhaps the count for each element a_i depends on the number of times the groups that contain a_i are split. For example, when a group is split, each element in that group will be in exactly one of the two subgroups, so their counts will each be incremented by 1 for each split of a group they are part of. The initial group contributes 1 to each count. Then, each split of a group that contains the element adds 1 to the count (because that split creates a new group containing the element, which is then processed).

So for example, the initial group is processed once (count +1 for all elements). Then, when the group is split into two, each element is in exactly one subgroup. So each element gets +1 count (from the subgroup). Then, if that subgroup is split again, each element in it gets another +1.

So the count for an element is equal to 1 (initial group) + the number of splits made on groups that include the element.

So the problem reduces to finding, for each element, how many splits occur in the groups that contain it. The initial group's split counts towards the elements in the group.

So the total count_i for an element a_i is 1 (initial group) plus the number of splits in groups that include a_i.

So the question becomes: how many splits are made in groups that contain a_i, given that each group of size >=2 must be split as much as possible. But how does the splitting process affect this?

Alternatively, perhaps the maximum possible count_i is achieved when each split is done in a way that maximizes the number of splits for each element. Wait, perhaps the count depends on the structure of the splitting tree. Each element is part of a certain number of splits. For example, in a binary tree structure, the depth of the element in the tree determines the number of splits. Because each split adds a level in the tree.

Alternatively, let's model the splitting as a binary tree. The initial group is the root. Each split creates two children. Each node in the tree represents a group. Each element is present in all the groups along the path from the root to the leaf (which is the element itself). The number of splits for a group is equal to the number of times it is split. For each element, the number of splits in groups that contain it is equal to the number of internal nodes (non-leaf nodes) in its path from the root to the leaf. Because each internal node (group) is split once, contributing one split. For example, in the first example:

The tree would look like this:

Root: [3,1,5] (split once)
Left child: [3,5] (split once)
Right child: [1] (leaf)
Left child's left: [3] (leaf)
Left child's right: [5] (leaf)

For element 3: path is root -> left child -> left. So internal nodes are root (split once), left child (split once). So splits count is 2. So total count_i is 1 (initial) + 2 (splits) =3. Which matches 3 being added 3 times.

Similarly, element 1: path is root -> right. The root is split once (so 1 split), then right is a leaf. So count_i is 1+1=2. Which matches 1 being added twice.

So for each element, the count_i is equal to the number of splits in the groups along its path from the root to the leaf. And since each split of a group contributes +1 to all elements in that group, the count_i for each element is 1 (initial group) + sum of splits for each group in its path that is split.

But how do we model this for maximum score?

The maximum possible count_i is when each element is part of as many splits as possible. How can we maximize the splits for all elements?

Wait, when a group is split, all elements in that group will be part of one subgroup. So the splits are additive for each element in the group. To maximize the total sum, each split of a group contributes (sum of all elements in the group) * 1. Because the group is split once, so each element in the group gets +1 to their count. Therefore, the total sum contributed by splitting a group is (sum of group) multiplied by 1. So to maximize the total, we should split groups in such a way that the sum of the group's elements is as large as possible. Because each split of a group adds that sum to the total score. Wait, this is a key insight.

Wait, let's think again. The initial sum is S = sum(a_i). Then, each split of a group adds the sum of the two subgroups. So for example, splitting a group into two with sums S1 and S2 adds S1 + S2 to the total. But S1 + S2 is equal to the original group's sum. So each split of a group adds the sum of the group to the total. Wait, that's interesting.

Wait, the initial sum is added once. Then, every time a group is split, the sum of the two subgroups (which is equal to the original group's sum) is added again. So each split contributes the sum of the group once. Therefore, the total score is the initial sum plus the sum of all group sums that are split. For example, in the first example:

Initial sum:9. Then split into 8 and 1 (sum 9). Then split 8 into 3 and 5 (sum 8). So total is 9 + (9+8) = 26. Which matches the example.

So the total score is equal to the sum of all the group sums that are split plus the initial sum. Wait, the initial sum is added once, and each split contributes the sum of the group being split. So the formula for the total is:

Total = sum_initial + sum of (sum of group) for each split group.

So the problem reduces to finding the maximum possible sum of the sums of all groups that are split during the process. Because the initial sum is fixed (sum of all a_i), the problem is to maximize the sum of the split groups' sums.

But how can we model this? Since each group of size >=2 must be split, but the way of splitting can affect which groups are split. So the sum of the split groups depends on how we split each group.

But to maximize the sum, when splitting a group into two parts, we should split it in such a way that the sum of the split parts is as large as possible. Wait, but the sum of the split parts is equal to the original group's sum. So splitting a group into two parts contributes the group's sum once to the total. So regardless of how we split the group, the contribution is the same. So the total sum of split groups is fixed, regardless of how we split the groups. Wait, that can't be right.

Wait, wait a minute. Let's think again. Suppose you have a group G. If you split it into G1 and G2, then the sum of G1 and G2 is sum(G). So when the split occurs, the sum of the split groups is sum(G). So each split of G contributes sum(G) to the total. But how many times can a group G be split? Because once a group is split into G1 and G2, those groups can be split again if their size is >=2.

So the number of times a group is split depends on the size of the group. For example, a group of size k (k >=2) can be split once, and each of the resulting groups (if size >=2) can be split again, and so on.

But each split of any group contributes the sum of that group. So the total contribution is the sum over all splits of the sum of the group being split. But how does this depend on the structure of the splitting?

Wait, here's a key observation: Each group of size >=2 must be split exactly once. Because, after splitting, the subgroups are passed to Toastman, and if they have size >=2, they are split again. So for each group of size >=2, exactly one split is performed. So the total number of splits is equal to the number of groups formed during the process that have size >=2.

Wait, let's see. For example, the initial group is size 3. It's split once. Then each subgroup (sizes 2 and 1). The size 2 subgroup is split once, producing two size 1 subgroups. So total splits: initial (1) + split of size 2 (1) → total 2 splits.

Each split corresponds to a group of size >=2. So the total number of splits is equal to the number of groups that are split, which is all non-leaf nodes in the splitting tree.

So for a group of size k, how many splits does it generate?

For example, a group of size k:

Each split of the group will generate two subgroups. Each subgroup with size >=2 must be split again. So the number of splits for a group of size k is 1 (the split of the group itself) plus the sum of the splits of the two subgroups.

But this seems recursive. So the total splits for a group of size k is (k-1). Because for a group of size k, the total splits required is k-1. For example:

k=1 → 0 splits.

k=2 → 1 split. Then two groups of size 1. Total splits 1.

k=3 → split into two groups (say 1 and 2). Then the group of size 2 splits once. Total splits 2.

Which matches 3-1=2.

k=4 → split into two groups. Suppose split into 2 and 2. Then each of those splits once. So total splits 1 + 2 =3, which is 4-1=3.

Yes. So for a group of size k, the number of splits is k-1, regardless of how it is split. Because each split reduces the number of groups by one. Wait, maybe that's another way to think about it. The total number of splits required for a group of size k is (k-1). Because you start with one group and end up with k groups (each of size 1). Each split increases the number of groups by 1. So to go from 1 to k, you need (k-1) splits.

So the total number of splits for the entire process is (n-1), since the initial group is size n. Each split increases the number of groups by 1. So from 1 group to n groups (each of size 1), we need (n-1) splits.

But each split contributes the sum of the group being split. So the total sum is the initial sum plus the sum of all split groups' sums.

But how do we compute the sum of all split groups' sums?

Each split group's sum is added once. So the problem reduces to adding the sum of all groups that are split. The initial sum is added once, and each split group's sum is added once.

Wait, but the initial group is added once, and then each split group is added once. So the total score is the initial sum (added once) plus the sum of all groups that are split (each added once).

Wait no. The initial group is added once. Then, each split group is split into two groups, which are then added to the score. So the initial group's sum is added once. Then, each split contributes the sum of the split groups. But wait, when you split a group into two, the two subgroups are added to the score. So each split operation adds the sum of the two subgroups. Which is equal to the sum of the original group. So each split adds the sum of the group being split. So for each split (each time a group is split), the group's sum is added to the total. Therefore, the total score is the initial sum plus the sum of all groups that are split.

Because the initial group is added once. Then, each split of a group (each group that is split) contributes its sum. Since there are (n-1) splits (each split reduces the number of groups to split by 1?), wait no. Wait, for each split, the number of groups increases by 1. So the total splits are (n-1) as each split moves from 1 group to n groups. Each split is a group of size >=2 being split. So the sum of all split groups' sums is the sum of the groups that are split. Each group that is split is counted once. So the total score is S_initial + sum (split_groups_sum). But the initial group is split as well. For example, in the first example, the initial group is split once. So the sum of split groups is 9 (the initial group) plus 8 (the split group [3,5]) → total 17. Then 9 + 17 = 26, which matches the example.

Wait, but wait. The initial group's sum is added once (as the initial step), and then when it's split, the group's sum is added again. So in the first example, the initial group is split once. So the split groups are the initial group (sum 9) and the group [3,5] (sum 8). So sum of split groups is 9+8=17. Then the total score is 9 (initial) + 17 = 26. Which matches.

So the formula is total = sum_initial + sum of split groups. And each split group is exactly the groups that are split during the process. The initial group is split once, contributing its sum again.

So how to compute the sum of all split groups. Since each split group's sum is added once, and each split of a group contributes the sum of that group.

The key is that each group that is split (i.e., groups of size >=2) is split exactly once. Therefore, the sum of all split groups' sums is the sum of all the groups that are split during the process.

But how do we compute this sum? Because the way the groups are split can vary, but we want to maximize the sum. Wait, no. Wait, the problem statement says that the initial group is given, and the splitting is done by Appleman. The goal is to find the maximum possible score. So Appleman can choose any possible way to split the groups to maximize the score.

But according to the earlier observation, the sum of all split groups is the sum of all groups that are split. So to maximize the total score, we need to choose splits in such a way that the sum of the split groups' sums is maximized.

But wait, each split of a group adds the sum of that group. So the order of splitting doesn't matter as long as all possible split groups are considered. Wait, no. For example, suppose we have a group of size 3. We can split it into [a, b] and [c]. Then split [a,b] into [a] and [b]. The split groups are the initial group (sum a+b+c) and [a, b] (sum a+b). So the sum of split groups is (a+b+c) + (a+b) = a+b+c +a+b = 2a + 2b + c.

Alternatively, if we split the initial group into [a] and [b,c], then split [b,c] into [b] and [c]. The split groups are (a+b+c) and (b+c). Sum is (a+b+c) + (b+c) = a + 2b + 2c. Which is different from the first case.

So the sum of split groups depends on how the groups are split. For example, in the first case, the sum is higher when a and b are larger than c. So to maximize the sum of split groups, we need to split groups in a way that maximizes the sum of the split groups' sums.

So the problem is now: how to split the groups such that the sum of all split groups is maximized.

This seems like a problem that can be solved greedily. For each group, when splitting into two subgroups, we should split in a way that maximizes the sum of the split groups. Wait, but splitting a group into two subgroups will add the sum of the original group once. Then, each subgroup's sum is added once if they are split. So for example, when you split a group G into G1 and G2, you add sum(G) to the total. Then, if G1 is split, you add sum(G1), and if G2 is split, you add sum(G2). So the total is sum(G) + sum(G1) (if G1 is split) + sum(G2) (if G2 is split). So the way you split G affects whether G1 and G2 are split, and thus their sum contributions.

But the problem is, for a group G, splitting into two subgroups G1 and G2 will lead to the sum(G) being added once. Then, each of G1 and G2, if they are of size >=2, are split again. So the optimal way to split G is to maximize the sum of G's contribution plus the contributions of G1 and G2's splits.

But this seems recursive. So the optimal split for G is to split into G1 and G2 such that sum(G) + max_sum(G1) + max_sum(G2) is maximized.

But how do we compute this? For a group G, the maximum sum is the sum of G plus the maximum sum of its possible splits.

But this approach would be computationally expensive for large n. However, perhaps there's a pattern here.

Wait, perhaps the optimal way to split a group is to split it into two subgroups in such a way that the sum of the split groups (sum(G1) + sum(G2)) is as large as possible. But since sum(G1) + sum(G2) is equal to sum(G), this is fixed. So splitting a group into any two parts will contribute sum(G) once. So the contribution of splitting G is fixed, but the subsequent contributions of splitting G1 and G2 depend on how they are split.

But for the maximum sum, perhaps the optimal strategy is to split a group into two parts, one of which is as large as possible. For example, when splitting a group into a single element and the rest. Then, the larger subgroup (the rest) can be split again, contributing a larger sum each time.

Wait, let's take the first example. The initial group is [3,1,5]. Sum is 9. Splitting into [3,5] and [1] adds 9 to the split sum. Then, splitting [3,5] adds 8. So the split sum is 9+8=17. If instead, the initial group was split into [3,1] (sum 4) and [5], then splitting [3,1] would add 4, leading to split sum 9+4=13. Then the total would be 9 + 13 =22, which is worse. So splitting into a group with a larger sum (the [3,5] group) allows for a higher split sum.

So the optimal way is to split the group into two parts, where one part is as large as possible. Because then that larger part can be split again, contributing its sum again.

So the strategy is to split the group into a single element and the rest. For example, each time we split a group, take out one element (the smallest possible to leave the rest as large as possible). But wait, perhaps the key is to split the group into a single element and the rest each time. That way, the remaining group (size k-1) can be split again, contributing sum(a_i - x) each time, where x is the element taken out.

Wait, but to maximize the sum of split groups, perhaps we should split the group into the smallest possible elements first, leaving larger elements to be part of more splits.

Alternatively, the optimal approach is to sort the array in ascending order, and each time split off the smallest element. Then, the remaining group will be larger and contain higher elements, leading to more contributions when split.

Let's think of the example again. The elements are 3,1,5. Sorting gives 1,3,5. Then, first split into [1] and [3,5]. Split sum is 1+3+5=9 (the initial group's sum). Then split [3,5] into [3] and [5], which adds 8. So sum is 9+8=17. Total score 9+17=26. Which is the correct example.

Another scenario: suppose we split [3,1,5] into [1,3] and [5]. Sum of split groups is 4 (sum of the split group [1,3], which is split once, adding 4. So total split sum is 9 (initial split) +4 =13. Then the total is 22. Which is worse.

So the optimal strategy is to split off the smallest elements first. Then, the remaining group has larger elements and can contribute more in subsequent splits.

So the algorithm is:

Sort the array in non-decreasing order. Then, each split removes the smallest element from the group. The sum of split groups is the sum of all possible groups formed by the remaining elements after each split.

Let me try to model this. For example, after sorting the elements as a1 ≤ a2 ≤ ... ≤ an.

The initial group is all elements. Sum S0 = sum(a_i).

Then, split into a1 and the rest (a2, a3, ..., an). Sum S0 is added to the split sum.

Next, the group (a2, a3, ..., an) is split into a2 and (a3, ..., an). Sum S1 = sum(a2, ..., an) is added.

Continue this until the group has size 1.

So the split sum would be:

sum_{k=0 to n-2} sum_{i=k+1 to n} a_i

Because for each split step k (starting from 0), the group is (a_{k+1}, a_{k+2}, ..., a_n). When split, the sum of this group is added. The number of splits is n-1 (since we start with n elements and split n-1 times). Wait, but the split steps are for groups of size >=2. So for a group of size m, you split m-1 times. So for n elements, you have n-1 splits, each adding the sum of the group at that step.

Wait, the split groups are:

Group 1: all elements (sum S) → split once. Contributes S.
Group 2: elements 2 to n (sum S - a1) → split once. Contributes S - a1.
Group 3: elements 3 to n (sum S -a1 -a2) → split once. Contributes S -a1 -a2.
...
Group n-1: elements n-1 and n (sum a_{n-1} + a_n) → split once. Contributes a_{n-1} + a_n.
Group n: a_n → no split.

So the split sum is S + (S - a1) + (S - a1 -a2) + ... + (a_{n-1} + a_n) + ... ?

Wait, no. Let's count how many splits there are and which groups are split.

Each split is performed on a group of size >=2. The total number of splits is n-1.

Each group that is split contributes its sum once.

The groups that are split are:

- The initial group (sum S) → split once.

- Then, the group after removing a1 (sum S - a1) → split once.

- Then, the group after removing a2 (sum S -a1 -a2) → split once.

...

This continues until the group is split into two elements. For example, the last split is of a group of size 2 (sum a_{n-1} + a_n), which is split into two single elements.

So the split sum is:

split_sum = S + (S - a1) + (S -a1 -a2) + ... + (a_{n-1} + a_n)

But how many terms are there? For n elements:

The first term is S (sum of all elements), which is split once.

The next term is sum of elements from a2 to an → S - a1.

The next term is sum of elements from a3 to an → S - a1 -a2.

...

This continues until the group is of size 2. For example, when we split the group of size 2 (a_{n-1}, a_n), the sum is a_{n-1} + a_n.

So the number of terms is (n-1) because each split corresponds to a group of size >=2. For example, n=3:

split_sum = S (3+1+5=9) + (3+5=8) → two terms. Which is correct.

So the split_sum for n elements is sum_{k=0}^{n-2} (S - sum_{i=1}^k a_i) )

So the formula for split_sum is S*(n-1) - sum_{k=1}^{n-1} a_k * (k-1) ?

Wait, let's see. Each term is S minus the sum of the first k elements. For k from 0 to n-2:

split_sum = sum_{k=0 to n-2} (S - sum_{i=1}^k a_i )

Wait, for k=0: sum_{i=1}^0 a_i is 0 → term is S.

k=1: sum a_1 → term is S -a1.

k=2: sum a1 +a2 → term S - (a1+a2).

...

k = n-2: sum a1 + ... +a_{n-2} → term S - sum_{i=1}^{n-2} a_i.

Wait, but for example, when n=3:

k ranges from 0 to 1 (n-2=1). So terms are S (k=0) and S -a1 (k=1). But in the example, the split_sum is S (9) + (S -a1 -a2) → 9 + (9 -1 -3) =9+5=14? No, the example's split_sum is 9 +8=17. Wait, the example has split_sum as 9 (initial group) and 8 (group [3,5]). So what's wrong here?

Ah, because the split_sum is S (sum of initial group) plus sum of all groups that are split after the initial. But according to the model where we split off one element each time, the split groups are:

After initial split of S (sum 9), the group [3,5] (sum 8) is split. So split_sum is 9+8 =17.

But according to the formula sum_{k=0}^{n-2} (S - sum_{i=1}^k a_i ), when n=3, sum_{k=0}^1 (S - sum_{i=1}^k a_i ):

k=0 → sum is 0 → term 9 -0=9.

k=1 → sum a1 (which is 1) → term 9 -1=8.

Total is 9+8=17, which is correct.

So the formula works for that example.

But how to compute this sum efficiently?

The sum can be written as:

split_sum = S*(n-1) - sum_{k=1}^{n-1} a_k * (k-1)

Because:

Each term in the split_sum is S - sum_{i=1}^k a_i, where k ranges from 0 to n-2.

Wait, but for k from 0 to n-2:

The sum of S terms is (n-1)*S.

The subtracted sum is sum_{k=0}^{n-2} sum_{i=1}^k a_i.

But sum_{k=0}^{n-2} sum_{i=1}^k a_i = sum_{i=1}^0 a_i (k=0) + sum_{i=1}^1 a_i (k=1) + ... + sum_{i=1}^{n-2} a_i (k=n-2).

Which can be rewritten as:

sum_{i=1}^0 a_i = 0.

sum_{i=1}^1 a_i = a_1.

sum_{i=1}^2 a_i = a_1 +a_2.

...

sum_{i=1}^{n-2} a_i = a_1 + ... +a_{n-2}.

So the total subtracted sum is:

0 + a_1 + (a_1 +a_2) + ... + (a_1 + ... +a_{n-2}).

Which is equal to sum_{i=1}^{n-2} a_i * (number of times a_i appears in the sums).

For example, a_1 appears in all terms from k=1 to k=n-2 → (n-2) times.

a_2 appears in terms from k=2 to k=n-2 → (n-2 -1) = n-3 times.

...

a_{n-2} appears once.

So the sum can be written as sum_{i=1}^{n-2} a_i * (n-1 -i).

Wait, perhaps there's a formula for this sum.

Alternatively, note that the sum is:

sum_{k=0}^{n-2} sum_{i=1}^k a_i = sum_{i=1}^{n-2} a_i * (n-2 - i +1) ) = sum_{i=1}^{n-2} a_i * (n-1 -i).

But for i from 1 to n-2, (n-1 -i) = (n-1 - i) = (n -i -1 +1) ? Wait, not sure.

Alternatively, for each a_i (i from 1 to n-2), the term a_i appears (n-2 -i +1) times. Because the sum from k=0 to n-2 of sum_{i=1}^k a_i is the same as sum_{i=1}^{n-2} a_i multiplied by the number of times they appear.

For a_i (i >=1), the number of times it appears is the number of terms where k >=i. For k ranges up to n-2. So for i <=n-2, the number of terms is (n-2) -i +1 = n-1 -i.

So sum_{k=0}^{n-2} sum_{i=1}^k a_i = sum_{i=1}^{n-2} a_i * (n-1 -i).

So split_sum = (n-1)*S - sum_{i=1}^{n-2} a_i*(n-1 -i).

But what about a_{n-1}?

Wait, in the example where n=3, the sum for a_1 (which is 1) is (n-1 -i) = 3-1 -1=1. So a_1 *1=1. Then split_sum = 9*(2) -1 = 18-1=17. Which is correct.

Another example: n=4.

If sorted a1=1, a2=2, a3=3, a4=4.

split_sum would be:

S =1+2+3+4=10.

split_sum = 10*3 - sum_{i=1}^2 a_i*(3 -i) → since n-2=2.

sum a1*(3-1) + a2*(3-2) → 1*2 + 2*1= 2+2=4.

split_sum =30 -4=26.

The split_sum is S (10) + (10-1=9) + (9-2=7) → 10+9+7=26. Which matches.

Yes. So the formula holds.

So the split_sum can be computed as:

split_sum = (n-1)*sum_total - sum_{i=1}^{n-1} a_i*(i-1)

Wait, wait, when n=3, the sum is up to n-2=1 (i=1).

But according to the example for n=3, the sum is a_1 * (3-1 -1) =a_1 *1. So the formula is sum_{i=1}^{n-1} a_i*(i-1) ?

Wait, I'm getting confused here. Let's re-derive:

split_sum = sum_{k=0}^{n-2} (S - sum_{i=1}^k a_i )

This can be rewritten as (n-1)*S - sum_{k=0}^{n-2} sum_{i=1}^k a_i.

sum_{k=0}^{n-2} sum_{i=1}^k a_i = sum_{i=1}^{n-2} a_i * (n-1 -i).

But when i ranges from 1 to n-2, (n-1 -i) is the number of times a_i appears in the sum.

But for a_i where i is from 1 to n-2.

But what about when n is larger? For example, n=4.

The sum is:

sum_{k=0}^2 sum_{i=1}^k a_i.

k=0: sum is 0.

k=1: a1.

k=2: a1+a2.

sum is 0 +a1 + (a1+a2) = 2a1 +a2.

Which is sum_{i=1}^2 a_i*(number of times). For i=1: 2 times (k=1 and k=2). For i=2:1 time (k=2). So 2a1 +a2.

Which is sum_{i=1}^2 a_i*(3 -i) → for i=1:3-1=2 → a1*2. For i=2:3-2=1 →a2*1.

So yes.

So split_sum = (n-1)*S - sum_{i=1}^{n-1} a_i*(i-1)

Wait, because sum_{k=0}^{n-2} sum_{i=1}^k a_i = sum_{i=1}^{n-1} a_i*(n-1 -i) ?

No, when i ranges up to n-2, the sum is up to n-2. But in the formula for split_sum, when k ranges up to n-2, the sum for i is up to k. So the maximum i is n-2.

So sum_{k=0}^{n-2} sum_{i=1}^k a_i = sum_{i=1}^{n-2} a_i * (n-1 -i).

But how does this relate to sum_{i=1}^{n-1} a_i*(i-1) ?

Wait, perhaps there's a miscalculation here. Let's re-express.

We have:

split_sum = (n-1)*S - sum_{i=1}^{n-2} a_i*(n-1 -i).

But we can write this as:

split_sum = S*(n-1) - [sum_{i=1}^{n-1} a_i*(n-1 -i)] + a_{n-1}*(n-1 - (n-1)) → but no, a_{n-1} is not part of the sum up to n-2.

Alternatively, perhaps we can include all i up to n-1, but when i is n-1, the term (n-1 -i) is zero, so it's zero. So:

sum_{i=1}^{n-2} a_i*(n-1 -i) = sum_{i=1}^{n-1} a_i*(n-1 -i).

But when i =n-1, (n-1 -i) =0, so the term is zero. So it's equivalent.

Thus, split_sum can be written as:

split_sum = S*(n-1) - sum_{i=1}^{n-1} a_i*(n-1 -i).

But how to compute this sum?

Let me see. Let's arrange the terms:

sum_{i=1}^{n-1} a_i*(n-1 -i) = sum_{i=1}^{n-1} a_i*( (n-1) -i ).

Which can be written as (n-1)*sum_{i=1}^{n-1} a_i - sum_{i=1}^{n-1} a_i*i.

But sum_{i=1}^{n-1} a_i is (S - a_n), since the total sum S is sum of all elements.

So:

sum_{i=1}^{n-1} a_i*(n-1 -i) = (n-1)(S - a_n) - sum_{i=1}^{n-1} a_i*i.

So split_sum becomes:

split_sum = (n-1)*S - [ (n-1)(S -a_n) - sum_{i=1}^{n-1} a_i*i ) ]

= (n-1)*S - (n-1)(S -a_n) + sum_{i=1}^{n-1} a_i*i

= (n-1)*S - (n-1)S + (n-1)a_n + sum_{i=1}^{n-1} a_i*i

= (n-1) a_n + sum_{i=1}^{n-1} a_i*i.

So split_sum = sum_{i=1}^{n} a_i*i - a_n * (i= n ?) Wait, no. Let's see:

sum_{i=1}^{n-1} a_i*i + (n-1)*a_n.

Which is equal to sum_{i=1}^{n} a_i*i - a_n*n + (n-1)a_n = sum_{i=1}^n a_i*i - a_n.

So split_sum = sum_{i=1}^n a_i*i - a_n.

Wait, no. Let me re-calculate:

split_sum = (n-1)a_n + sum_{i=1}^{n-1} a_i*i.

But sum_{i=1}^{n} a_i*i = sum_{i=1}^{n-1} a_i*i + a_n*n.

So split_sum = [sum_{i=1}^n a_i*i - a_n *n ] + (n-1)a_n.

= sum_{i=1}^n a_i*i -a_n *n + (n-1)a_n.

= sum_{i=1}^n a_i*i - a_n.

So split_sum = sum_{i=1}^n a_i*i - a_n.

That's a much simpler formula!

Let's verify with the first example:

sum a_i*i for [1,3,5] (sorted):

1*1 +3*2 +5*3 =1 +6 +15=22.

subtract a_n (5) →22-5=17. Which matches the split_sum.

Another example:

n=4, sorted [1,2,3,4].

sum a_i*i: 1*1 +2*2 +3*3 +4*4=1+4+9+16=30.

split_sum =30 -4=26. Which matches the earlier example.

So the formula is split_sum = sum_{i=1}^n (a_i * i) - a_n.

But wait, this is only true if the elements are sorted in increasing order. Because the split is done by taking the smallest elements first.

So the algorithm is:

Sort the array in non-decreasing order.

Compute the sum of a_i multiplied by their 1-based index (i starts at 1) minus the largest element (a_n).

The initial sum is S = sum(a_i). The total score is S + split_sum = S + (sum(a_i*i) - a_n).

But wait, the initial sum is added once, and the split_sum is added.

So total score = S + split_sum = S + (sum(a_i*i) - a_n) = sum(a_i) + sum(a_i*i) -a_n.

But sum(a_i) + sum(a_i*i) is sum(a_i*(i+1)) -a_n.

Alternatively, sum(a_i*(i+1)) - a_n - a_n = sum(a_i*(i+1)) - 2a_n ?

Wait, perhaps not. Let's see:

sum(a_i) + sum(a_i*i) = sum(a_i*(1 +i)) = sum(a_i*(i+1)).

Then subtract a_n.

But in the first example:

sum(a_i*(i+1)) = 1*2 +3*3 +5*4=2+9+20=31. Subtract a_n (5) gives 26. Which is correct.

Another example, n=1. Then sum(a_i) = a_1. split_sum is sum(a_i*i) -a_n → a_1*1 -a_1=0. So total is a_1 +0 =a_1. Which matches the second example.

So the correct formula is total = sum(a_i) + sum(a_i*i) -a_n.

But sum(a_i) + sum(a_i*i) is sum(a_i*(i+1)).

But sum(a_i*(i+1)) -a_n = sum(a_i*(i+1)) - a_n.

Wait, sum(a_i*(i+1)) = sum(a_i *i) + sum(a_i). So sum(a_i) + sum(a_i*i) is equal to sum(a_i*(i+1)). So the total is sum(a_i*(i+1)) - a_n.

But why does this formula hold?

Because after sorting, the split_sum is sum(a_i*i) -a_n. Then total score is sum(a_i) + split_sum = sum(a_i) + sum(a_i*i) -a_n = sum(a_i*(i+1)) -a_n.

So the algorithm is:

Sort the array in non-decreasing order.

Compute for each element a_i (sorted) its value multiplied by (i+1), sum all those, then subtract a_n (the largest element).

Wait, no. Wait, sum(a_i) + split_sum = sum(a_i) + (sum(a_i*i) -a_n) = sum(a_i*(1 +i)) -a_n.

So the formula is sum(a_i*(i+1)) -a_n.

But why is that?

Let's see for the first example:

elements sorted [1,3,5].

sum(a_i*(i+1)) =1*(1+1) +3*(2+1) +5*(3+1) =1*2 +3*3 +5*4 =2+9+20=31.

31 -5=26, which matches.

Another example: n=1. sum(a_i*(i+1)) =1*(1+1) =2. subtract a_n=1. total 1, which matches.

Another example: n=4 sorted [1,2,3,4].

sum(a_i*(i+1)) =1*2 +2*3 +3*4 +4*5 =2+6+12+20=40. subtract a_n=4 →36. But earlier split_sum for this case was 26, and sum(a_i) is 10. 10+26=36. Yes. So correct.

So the formula holds.

So the steps are:

1. Sort the array in non-decreasing order.

2. Compute the sum of each a_i multiplied by (i+1), where i is the 1-based index.

3. Subtract the largest element (the last element in the sorted array).

The result is the maximum possible score.

So the implementation is straightforward. Sort the array, compute the sum as described.

Now, considering the constraints: n can be up to 3e5, and each a_i up to 1e6. So we need to process this efficiently.

In Python, sorting 3e5 elements is manageable.

For the sum, we can iterate through the sorted array with their indices (1-based), compute (i+1)*a_i for each, sum them, and subtract the last element.

So the code would look like:

n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(n):
    idx = i + 1  # 1-based
    total += a[i] * (idx + 1)
total -= a[-1]
print(total)

Wait, but wait:

For each element in the sorted array, index i (0-based in Python), 1-based index is i+1. So (i+1 +1) = i+2. So the multiplier is (i+2) ?

Wait, no. The formula is sum(a_i*(i+1)) where i is 1-based. Because in the code:

When sorted, the first element is a[0] in 0-based, which is i=1 in 1-based. So the multiplier is (1+1) =2. For the first element (i=0 in 0-based, which is 1-based index 1), the multiplier is 1+1=2.

Wait, the formula was sum(a_i*(i+1)) where i is the 1-based index. So in code:

for each element in the sorted array, 0-based index j:

i = j +1 (1-based index).

multiplier is i +1 → (j+1) +1 = j+2.

So for each element a[j], the term is a[j] * (j +2).

So the code should be:

sorted_a = sorted(a)

sum_ = sum( (i+2)*x for i, x in enumerate(sorted_a) )

result = sum_ - sorted_a[-1]

print(result)

But wait, let's test with the first example:

sorted_a is [1,3,5].

enumerate gives indices 0,1,2.

terms:

0: (0+2)*1 =2.

1: (1+2)*3=9.

2: (2+2)*5=20.

sum_ =2+9+20=31.

subtract 5 →26.

Which is correct.

Yes.

So this code would work.

So the code reads n, reads the list, sorts it, computes the sum with (i+2) multiplier for each element, subtracts the last element, and prints.

This is O(n log n) time due to sorting, which is acceptable for n=3e5.

Memory is O(n), which is acceptable.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
total = 0
for i in range(n):
    total += a[i] * (i + 2)
total -= a[-1]
print(total)
```