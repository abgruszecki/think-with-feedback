<think>
Okay, let's try to figure out this problem. So, the task is to find the minimum possible penalty when distributing balls of different colors into their respective boxes. The penalty is the sum of the sizes of the groups we split each time. 

Hmm. Let's start by understanding the operations. Each turn, Ivan takes all balls from a box and splits them into k=2 or k=3 non-empty groups. The penalty for that turn is the total number of balls taken (the sum of the group sizes, which is the original box's size). The goal is to arrange all colors into their correct boxes with minimal total penalty.

So, each color's balls (a_i) must end up in their own box. The initial setup is that all balls are in the first box. Then, through splitting operations, we move them to the correct boxes.

The key observation here is that each split step can be thought of as building a tree structure. For each color, the initial group (the root) is split into children, and so on until each leaf is a single color. The penalty is the sum of the values of all the internal nodes in this tree. Our goal is to arrange the splits such that the sum of all the internal node values is minimized.

Wait, right. For example, in the first sample input: 1, 2, 3. The optimal is to split all at once into 3 groups (k=3), so the penalty is 1+2+3 =6. That's the only split needed. So the sum of the split steps (which is the sum of the parent nodes) is just 6.

In the second example, the sum is 14 +5=19. Let's see: the first split is 2+3+4+5 =14 (sum of all, then split into 3 groups, maybe 3,4,5 and 2?), but I need to check how exactly. Then the next split is 5 (sum of 2+3?), split into 2 groups. So the sum is 14+5=19.

So the problem reduces to, for each a_i (the number of balls of color i), we need to model the splitting process as a tree where each non-leaf node must have exactly 2 or 3 children. The sum of all the node values (excluding leaves) is the total penalty. We need to find the minimal sum for all a_i's.

Wait, but each a_i is the number of balls of color i, which must end up in its own box. So the splitting process for each color's a_i is independent? Or does the splitting involve combining different colors? Oh, no. Because once a split occurs, the group is placed into a new box, which can then be split again. But each split must separate into non-empty groups. But the problem states that each group must end up in a box. So the process for each color's a_i is to split the group until it's in its own box. So each a_i contributes to the penalty based on how it's split down from the initial group.

Wait, but the initial group contains all colors. So the first split might separate colors into different groups, which then get split further. So the process is more complicated. Hmm. Wait, no. Because the initial group (the first box) has all colors. Then, when you split that group into k groups, each group can be a subset of the colors. But the splits are done in such a way that each split must create groups that are non-empty. So, perhaps the splitting process can be considered as a tree where each node represents a group of colors (a subset), and splitting into k groups (children) such that each child is a subset of the parent's colors. The leaves are the individual colors. The penalty for each split is the sum of the values (number of balls) of the parent node. 

But each split's sum (the penalty) is the value of the parent (the number of balls in the group being split). So for each split step, the penalty is the size of the group that is split. The total penalty is the sum of all the split group sizes. So the problem reduces to building a tree for each color's path from the root to the leaf (color i), such that each split along the path contributes the size of the group at that node. Wait, but how do the splits contribute when a group is split into multiple parts? For example, splitting a group of size S into k groups: the penalty is S, and then each of the k groups will be split further, adding their own penalties if they are split. So the total penalty is the sum of all the S values for every split made.

So the problem is similar to Huffman coding, but with a different constraint. In Huffman coding, we merge nodes to minimize the weighted path length, but here, each split can split a group into 2 or 3 parts. Each split contributes the group's size to the total penalty. Our goal is to arrange the splits such that the sum is minimized.

So, for each a_i, the path from the root (the initial group) to the leaf (a_i) contributes the sum of all the group sizes along the path, except the leaf. But how is this structured? For example, if a_i is split in a group that's split multiple times, each split along the path contributes the group's size. So the a_i's contribution depends on how many times its group is split until it becomes a single color.

But how do the groups get split? Let's think of the entire process as building a tree where each node represents a group of colors, and each internal node (split) has 2 or 3 children. The leaves are the individual colors. The penalty is the sum of the sizes of all the internal nodes.

So the total penalty is the sum over all internal nodes of their sizes. The size of a node is the sum of the a_i's of the colors in that group. For example, the root node has size sum(a_i) for all colors. When split into k children, each child's size is the sum of the a_i's in that group. Each of these children is an internal node (if split again) or a leaf (if it's a single color).

Thus, the problem is to arrange a tree structure where all leaves are individual colors, each internal node has 2 or 3 children, and the sum of all internal nodes' sizes is minimized.

So this problem is equivalent to building a Huffman-like tree with the constraint that each node can have 2 or 3 children. The goal is to minimize the sum of the internal nodes' values.

Huffman coding works by merging the two smallest nodes first, but here we need to split into 2 or 3 nodes. So perhaps a similar greedy approach applies here, but with different constraints.

Let's consider the Huffman algorithm for ternary splits. In standard Huffman coding for ternary splits, the algorithm works optimally when the number of leaves is such that (n-1) is divisible by (k-1), where k is the number of children allowed. For example, in ternary, (n-1) must be divisible by 2. So, for n leaves, the number of internal nodes is (n-1)/(k-1) for k-ary trees. However, in this problem, the tree can have internal nodes with either 2 or 3 children. So it's a mix of binary and ternary splits.

Wait, but for the sum to be minimized, perhaps the optimal approach is to use as many ternary splits as possible, since splitting into more groups (k=3) reduces the number of splits needed. For example, splitting into 3 groups requires one split, whereas splitting into 2 groups twice (to get 4 groups) requires two splits. So using higher k when possible can reduce the number of splits, which reduces the sum of the penalties. However, each split's penalty is the size of the group, so the earlier splits (higher in the tree) contribute larger penalties.

So the optimal approach would be to merge smaller groups first, but using ternary splits where possible. This is similar to the Huffman algorithm but with variable k.

Alternatively, the problem can be modeled as building a Huffman tree where each merge step can combine either 2 or 3 nodes, but each merge step's cost is the sum of the merged nodes. Wait, because in Huffman, the cost is the sum of the merged nodes, which corresponds to the split cost here.

Wait, maybe there's a connection. Let's see. If we model the problem as building a tree where the internal nodes are the splits. Each split (internal node) has a cost equal to the sum of the values of the children. The sum of all internal nodes is the total penalty. So the total penalty is the sum of the internal nodes' values.

In Huffman coding, the cost is the sum of the products of the weight and the depth. But here, the cost is the sum of the internal node values, which is equivalent to the sum of the weights multiplied by the number of splits they are involved in. Wait, perhaps not exactly, but there's a similarity.

Alternatively, in the Huffman problem, each time you merge nodes, the cost is the sum of their weights. The total cost is the sum of all such merge costs. So the Huffman algorithm minimizes this total cost by greedily merging the two smallest nodes first.

In this problem, the merge cost would correspond to the split penalty. So, merging two nodes (A and B) would create a parent node with value A+B, and the cost added is (A+B). If merging three nodes (A, B, C), the cost is (A+B+C). But the problem allows merging two or three nodes each step. So, the optimal strategy would be to merge as many nodes as possible each step to minimize the number of higher-cost steps.

But how do we model this? Let's think in terms of the Huffman algorithm. The standard Huffman algorithm for binary merges works optimally. But when allowing ternary merges, the optimal approach requires that (n-1) must be divisible by (k-1), where k is the maximum number of children per node. So for k=3, we need (n-1) to be even. If not, we can add dummy nodes with 0 weight. But in our problem, the splits can be either binary or ternary. So the tree can have a mix of nodes with 2 or 3 children.

But how to model this? Let's consider the initial leaves (the a_i's). The total number of internal nodes required would depend on how the splits are made. For example, each split (internal node) reduces the number of required splits by (k-1). For a tree with n leaves, the number of internal nodes is (n-1)/(k-1) for each split, but here k can vary between 2 and 3.

This seems complex. Let's think of the problem as a generalized Huffman coding problem where each merge can be of 2 or 3 elements. Our goal is to minimize the sum of the merge costs (the sum of the merged values each time).

In this scenario, the greedy approach would be to merge as many small elements as possible in each step. For example, if we have a lot of small elements, merging three at a time would save on the higher cost steps. However, if the number of elements after some steps is not allowing for a ternary merge, we can switch to binary.

But how do we model this? Let's think about the process. Initially, we have all the a_i's as leaves. We need to merge them into a single root. Each merge step combines 2 or 3 elements into a parent node, whose value is their sum. The total penalty is the sum of all parent nodes' values.

The optimal strategy would be to combine the smallest possible elements first, but the choice between merging two or three depends on which leads to a lower total sum.

Wait, here's a possible approach: use a priority queue (min-heap) that holds all the current elements (initially the a_i's). Then, in each step, we can take either the two smallest elements and merge them (summing them, adding the sum to the total), or take the three smallest elements and merge them (summing them, adding the sum to the total). The choice between merging two or three would depend on which gives a lower total cost in the long run.

But this is a greedy approach, and it's not clear whether this would lead to the optimal solution. However, given the problem's constraints (n up to 2e5), we need an O(n log n) algorithm.

Alternatively, perhaps the optimal approach is to arrange the merges such that as many ternary merges as possible are done. But to allow this, the number of elements after all merges must satisfy (n_initial - 1) mod 2 = 0. Wait, because each ternary merge reduces the count by 2 (since 3 elements are merged into 1: 3-1=2). Each binary merge reduces by 1 (2-1=1). The total number of elements must be reduced from n to 1. So the number of steps (merges) is such that the sum of (k_i-1) for each merge i is (n-1), where k_i is the number of elements merged (2 or 3). So, (k_1-1) + (k_2-1) + ... + (k_m-1) = n-1. Each (k_i-1) is either 1 (binary) or 2 (ternary). So the equation becomes sum (for each merge) (k_i-1) = n-1. Let's denote s as the sum of (k_i-1) terms. Then s must equal n-1. So, each ternary merge contributes 2 to s, binary contributes 1.

So the problem is to find how many ternary merges (t) and binary merges (b) we need such that 2t + b = n-1, and t and b are non-negative integers. But since t can be any value as long as 2t ≤ n-1 and (n-1 - 2t) is the number of binary merges.

But how does this affect the sum? The goal is to maximize the number of ternary merges to minimize the sum. Because merging three small elements in one step (cost x+y+z) is better than merging two pairs (cost (x+y) + (x+y + z) = x+y + x+y+z = 2x+2y +z). Wait, no. Wait, merging three elements at once would cost x+y+z once. Merging two elements (x and y) first, then merging their sum with z would cost (x+y) + (x+y+z) = x+y + x+y+z = 2x + 2y + z. So merging three elements in one step is better.

So, in order to minimize the sum, we should merge as many elements as possible in groups of three, especially the smaller ones. So the strategy would be to merge the three smallest elements whenever possible.

But how do we handle the case when (n-1) is not congruent to 0 mod 2? Because each ternary merge contributes 2 to the sum s = n-1. So if (n-1) is even, then all can be ternary merges. If (n-1) is odd, we need to have one binary merge and the rest ternary.

Wait, for example, if n=3: n-1=2. So two ternary merges (each contributes 2) sum to 2. Wait, no, one ternary merge (3 elements into one) reduces the count by 2 (from 3 to 1). So for n=3, (3-1)=2, which is 2 = 2*1 → one ternary merge. So, yes. So for n=3, one ternary merge, which is optimal.

Another example: n=4. Then n-1=3. 3 can be written as 2*1 +1 → one ternary and one binary. Or 1*3 → three binary merges. But the first option allows one ternary merge and one binary. Let's see: merging 3 elements (sum a) then merging 2 elements (sum a + sum b). Which is better?

But the sum would be (sum of three) + (sum of two). If the two is the sum of the merged three and the fourth element, then perhaps it's better to have one ternary merge and one binary.

So, the approach would be to first check whether (n-1) is congruent to 0 mod 2. If not, then we need to have at least one binary merge. So, the plan is:

1. If n ==1: no splits needed, penalty 0.

2. Else, create a priority queue (min-heap) of all the a_i's.

3. Compute the required number of ternary and binary merges. For that:

   The equation is 2t + b = n-1. We want t as large as possible. So for even (n-1): t=(n-1)/2, b=0.

   For odd (n-1): t=(n-1 -1)/2 = (n-2)/2, b=1.

   Wait, but n-1 can be even or odd. Let me see:

   For example, n=4 → n-1=3, which is odd. So t= (3-1)/2 =1, b=1. So total steps: 1 ternary (contribute 2) and 1 binary (contribute 1). 2+1=3.

   Yes. So the number of ternary merges is floor((n-1)/2) when n-1 is even, and floor((n-1-1)/2) when it's odd. Wait, perhaps a better way to compute t is t = (n-1 - r)/2, where r is the remainder when (n-1) is divided by 2. So r=0 or 1. Then, t = (n-1 -r)/2. Then, b= r.

   For example, when n-1 is even, r=0 → t=(n-1)/2, b=0. When n-1 is odd, r=1 → t=(n-1-1)/2 = (n-2)/2, b=1.

   So in total, t + b merges? No, because each ternary merge is one merge (taking three elements) and each binary is one merge (taking two elements). Wait, no: each ternary merge (merging three elements) contributes 2 to s (n-1). Each binary merge contributes 1. So the number of merges is t + b, but the sum of their contributions (2t +b) must be equal to n-1.

   So the initial approach would be to first make as many ternary merges as possible. But how to model this in the algorithm.

   But perhaps the algorithm can be structured as follows:

   - Use a min-heap to select the smallest elements.

   - If the number of elements in the heap is >=3 and we can do a ternary merge (i.e., the required number of ternary merges allows it), then merge the three smallest elements.

   - Otherwise, merge two smallest.

   Wait, but the required number of ternary merges depends on n, not the current state. So perhaps we need to precompute how many ternary merges we need to do. For example:

   If the original n is such that (n-1) mod 2 is 0, then all possible merges are ternary (but not exactly, because after each merge, the count of elements decreases by 2 (since 3→1). Wait, the initial count is n. Each ternary merge reduces the count by 2 (3 elements become 1, so net decrease of 2). Each binary merge reduces by 1 (2 elements become 1, net decrease of 1).

   So the process starts with n elements and ends when there's 1 element left. The number of merges is (n-1) / (k-1), but since k can vary, it's tricky.

   Alternatively, let's model the process. Let's say that during the merging process, we have to choose between merging 2 or 3 elements each time. The goal is to minimize the sum of the merged values. The optimal approach is to merge the smallest possible elements each time. But merging three elements might be better than merging two, even if it's possible.

   For example, if the three smallest are x, y, z. Merging them into x+y+z adds x+y+z to the total. If instead, we merge x and y first (cost x+y), then merge (x+y) and z (cost x+y+z). Total cost is (x+y) + (x+y + z) = x+y + x+y + z = 2x + 2y + z. Which is higher than the ternary merge cost (x+y+z). So merging three elements when possible is better.

   So whenever possible, merge three elements. But how to determine when it's possible?

   Wait, but the problem allows merges of 2 or 3 elements. So, in the algorithm, whenever there are at least two elements, you can choose to merge two. But merging three is allowed only if there are three elements. But how to decide whether to merge two or three when there are three elements.

   Wait, perhaps the optimal approach is to merge three elements only when (current number of elements) mod 2 is 1. Because merging three elements (reduces count by 2) would leave the count even. But this is not clear.

   Alternatively, the algorithm can proceed as follows:

   While the number of elements in the heap is greater than 1:

      if there are at least three elements, and (the number of elements minus 1) is even, then merge three.

      else merge two.

   But how to model this?

   Alternatively, here's a possible strategy inspired by the standard Huffman algorithm but with the option to merge three elements when possible.

   Let's start with a min-heap of all elements.

   The algorithm:

   total =0

   while the heap size >1:

       if the heap size >=3 and ( (heap_size -1) %2 ==0 ):

           # can merge three

           x = heappop()

           y = heappop()

           z = heappop()

           sum_xyz =x + y + z

           total += sum_xyz

           heappush( sum_xyz )

       else:

           # merge two

           x = heappop()

           y = heappop()

           sum_xy =x + y

           total += sum_xy

           heappush( sum_xy )

   return total

   But this is just a heuristic. Let's test this against the sample inputs.

   First sample input:

   3 elements: 1,2,3.

   heap is [1,2,3]

   heap_size is 3. (3-1) =2, which is even. So merge three.

   sum_xyz=6. total becomes 6.

   heap now has [6]. size is 1. stop. total is 6. which matches the sample.

   Second sample input:

   4 elements:2,3,4,5.

   The sorted list is [2,3,4,5].

   Let's simulate the algorithm.

   heap_size starts at 4.

   (4-1)=3, which is odd. So can't merge three. So merge two: take 2 and 3, sum 5. total=5. heap becomes [4,5,5].

   Now, heap_size is 3. (3-1)=2 even. So merge three: 4,5,5 → sum 14. total becomes 5+14=19. heap is [14]. size 1. return 19. Which matches the sample.

   So the algorithm works for the sample inputs.

   Another test case. Let's say n=2, a1=1, a2=1. Then the algorithm will have heap size 2. (2-1) is 1, which is odd. So merge two: sum 2. total is 2. Which is correct (only possible split is k=2, penalty 2).

   Another test case: n=5. For example, a=[1,1,1,1,1]. So initial heap has 5 elements.

   (5-1) mod 2 is 0. So first, check if heap_size >=3 and (heap_size-1) is even. Current heap_size is5. 5-1=4, even. So merge three smallest: 1,1,1. sum=3. total +=3. heap becomes [1,1,3].

   Now heap_size is3. 3-1=2 even. Merge all three: 1+1+3=5. total=3+5=8. heap becomes [5]. So total is 8. But let's see if that's optimal.

   Alternatively, what's the minimal sum. Let's think. We have 5 elements. Each split can be 2 or 3. The equation is 2t +b =5-1=4. So t=2, b=0. So two ternary merges. But how?

   First merge three 1's into sum 3 (cost 3). Then merge the remaining two 1's and 3 into sum 5 (cost 5). Then merge 5 and sum 3+5=8 (wait, no. Because after the first merge, we have 3,1,1. Then merge those three (sum 5). Then merge the 5 and the other 3 (wait, no). Wait, perhaps the initial approach was wrong.

   Alternatively, the algorithm's steps for n=5 would be:

   Initial heap: [1,1,1,1,1].

   heap_size=5. (5-1)=4 is even. So merge three: 1,1,1 → sum 3. total=3. heap becomes [1,1,3].

   Now heap_size=3. (3-1)=2 even. Merge three: 1,1,3 → sum 5. total=3+5=8. heap becomes [5]. So the total is 8.

   But another approach: split into two merges of two elements each. For example:

   First merge two 1's: sum 2. total=2. heap [1,1,1,2].

   Then merge two 1's: sum 2. total=4. heap [1,2,2].

   Then merge two 1+2: sum3. total=4+3=7. heap [2,3].

   Then merge those two: sum5. total=7+5=12. So that's worse.

   So the algorithm's approach gives a better total. So the algorithm works here.

   So the algorithm seems to work for these cases. Let's see another case where n=4. For example, a=[1,1,1,1]. Then:

   heap_size=4. (4-1)=3, which is odd. So merge two: 1+1=2. total=2. heap becomes [1,1,2].

   Now, heap_size=3. (3-1)=2 even. Merge three: 1+1+2=4. total=2+4=6. heap becomes [4]. So total is 6.

   Alternatively, if we first merge three elements (1,1,1) sum3, then merge the remaining 1 and 3 → sum4. Total is 3+4=7. Which is higher. So the algorithm's approach is better.

   So the algorithm seems to correctly choose the optimal steps.

   So the algorithm works as follows:

   - If the current heap size is >=3 and (current heap size -1) is even → merge three elements.

   - Otherwise, merge two.

   The reasoning is that merging three elements when possible (i.e., when (heap_size -1) is even) allows the remaining elements to be merged in a way that minimizes the number of required splits. This ensures that we can always proceed with ternary merges when possible, and only use binary merges when necessary.

   Now, the code for this algorithm can be written using a min-heap (priority queue). For Python, we can use the heapq module.

   But since n can be up to 2e5, and each operation is O(log n), the time complexity should be acceptable.

   Let's code this.

   The steps are:

   1. Read n.

   2. Read the list a.

   3. If n ==1: output 0.

   4. Else, push all a_i into a min-heap.

   5. Initialize total=0.

   6. While the heap size is greater than 1:

       a. Check if the heap size is >=3 and (heap_size -1) is even.

       b. If yes, merge three: pop three elements, sum them, add to total, push sum back.

       c. Else, merge two: pop two, sum, add to total, push sum back.

   7. Output total.

   Let's test this with the second sample input:

   Input:4 2 3 4 5 → a = [2,3,4,5]

   heap starts as [2,3,4,5].

   heap_size=4.

   4-1=3, which is odd. So merge two: 2 and3 → sum5. total=5. heap becomes [4,5,5].

   heap_size=3. 3-1=2 even. merge three: 4+5+5=14. total=5+14=19. heap becomes [14]. done. Output 19. Correct.

   Another test case: n=5, a=[1,1,1,1,1]. The algorithm gives total 8 as above.

   So the code should handle this.

   Now, implement this in Python.

   Edge Cases:

   - n=1: output 0.

   - n=2: merge two, sum a1 +a2.

   - n=0? No, constraints say n≥1.

   Also, when merging three, the order of popping is the three smallest elements.

   Now, in Python, the heapq module's heappop() pops the smallest element. So for merging three, we can pop three times.

   Now, the code:

   Read n.

   Read a as list of integers.

   if n ==1:

       print(0)

       exit()

   import heapq

   heapq.heapify(a)

   total =0

   while len(a) >1:

       if len(a)>=3 and (len(a)-1) %2 ==0:

           x= heapq.heappop(a)

           y= heapq.heappop(a)

           z= heapq.heappop(a)

           s =x + y + z

           total +=s

           heapq.heappush(a, s)

       else:

           x= heapq.heappop(a)

           y= heapq.heappop(a)

           s =x + y

           total +=s

           heapq.heappush(a, s)

   print(total)

   Wait, but the a_i can be up to 1e9. So the sum can be up to 1e9 * 2e5, which can be 2e14, but Python can handle that.

   Now, test this code.

   Let's test the first sample input:

   3

   1 2 3 → the heap is [1,2,3]. len is3. len-1=2 even. So merge three. sum 6. total 6. output 6. Correct.

   Another test case: n=4, a=[2,3,4,5] → output 19.

   So code works.

   What about n=2: input is 2 1 1. The code:

   heap starts as [1,1]. len(a) is 2. len(a)-1=1, odd. So merge two: sum 2. total 2. output 2.

   Which is correct.

   What about n=5, a = [1,1,1,1,1].

   The code:

   First len(a) is5. len-1=4 even. Merge three 1's. sum 3. total 3. a becomes [1,1,3].

   Now len is3. len-1=2 even. Merge three: sum 5. total 8. a becomes [5]. done. output 8.

   Which is correct.

   So the code seems to handle all cases correctly.

   Now, time complexity. Each heappop and heappush is O(log n). There are O(n) operations. For n up to 2e5, O(n log n) is acceptable.

   So the code should pass all test cases.
</think>

```python
import heapq

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    heapq.heapify(a)
    total = 0
    while len(a) > 1:
        if len(a) >= 3 and (len(a) - 1) % 2 == 0:
            x = heapq.heappop(a)
            y = heapq.heappop(a)
            z = heapq.heappop(a)
            s = x + y + z
            total += s
            heapq.heappush(a, s)
        else:
            x = heapq.heappop(a)
            y = heapq.heappop(a)
            s = x + y
            total += s
            heapq.heappush(a, s)
    print(total)
```