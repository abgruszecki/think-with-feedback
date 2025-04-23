<think>
Okay, let's try to understand this problem. So, the city is structured as a tree with n squares connected by n-1 roads. All roads are directed in such a way that you can reach any square from the main square (which is square 1). So the structure is a directed tree with edges going away from the root.

The bandit starts at square 1. The process is that first, all citizens move along one of the outgoing roads from their current square. Then the bandit moves. This repeats until the bandit is on a square with no outgoing roads. At that point, he catches all citizens there. Both the bandit and citizens act optimally: the bandit wants to maximize the caught citizens, the citizens want to minimize it. We need to find the maximum number the bandit can catch under optimal play.

Hmm. Let's think about the structure. Each node except the leaves (nodes with no outgoing edges) has children. The direction of roads is such that each node's parent is p_i, which is less than i, so the tree is built in a way that parents come before children. So the tree is a rooted tree where edges go from parent to child.

The citizens' movement is first. Each citizen on a node with outgoing edges must choose one of them to move. So if a node has multiple children, the citizens can split into different paths. Then the bandit moves. The bandit chooses a path to follow. The process repeats until the bandit ends up in a leaf.

The problem is to model this game and find the optimal strategies for both parties.

Let me think about the optimal play. The citizens want to minimize the number that the bandit can capture. The bandit wants to choose a path that maximizes this.

So for each node, when the bandit arrives there, the citizens in that node (if any) would have already moved to their children (since the node isn't a leaf, so there are outgoing edges). Then the bandit moves to one of the children.

Wait, the process steps:

1. All citizens move (if they are on a node with outgoing roads). So during each step, the citizens move first. Then the bandit moves.

So when the bandit is at a node, the citizens in that node at that time would have already moved to their children. So the bandit can't capture any citizens in that node. The capture only happens when the bandit is on a leaf (no outgoing roads), so there, the citizens can't move anymore and are caught.

So the key is to model for each node, the possible paths the bandit can take, and how the citizens distribute themselves to minimize the maximum possible capture.

Let me think recursively. Suppose we have a node u. The bandit is at u. The citizens in u have already moved to children of u. Then the bandit chooses a child v to move to. The total caught is the sum of the a_i in the leaf where the bandit ends up, but considering all the steps.

Wait, but the a_i is the initial number of citizens. However, during each step, the citizens can split into the outgoing edges. So the a_i in the leaves depends on how the citizens distributed themselves through the steps.

Wait, perhaps the optimal strategy is determined by considering the minimal maximum that the bandit can collect. For each node, the citizens can distribute their citizens to the children, and the bandit will choose the child that leads to the maximum possible capture.

So for a node u, let's say the citizens have a total of s citizens (from their own a_u plus any incoming from previous steps) that need to be distributed to the children. The bandit will choose the child with the maximum value (after the citizens distribute the s in the best possible way to minimize this maximum). So the minimal possible maximum of the children's values.

So, for each node u, the optimal value (the maximum the bandit can get from this subtree) is the minimum among the maximum values of the children. But wait, perhaps it's more complicated.

Wait, the process for node u is: when the bandit is at u, the citizens in u (from the previous steps) have already moved to the children. So the bandit can choose any child. The value for u would be the maximum of the children's values (since the bandit chooses the best path). But the citizens can distribute the citizens in u to the children in a way that minimizes this maximum. So for node u, the value is the minimum possible maximum of the children's values, given that the citizens can split their current count into the children.

So, for a node u with children, the citizens have to split their total (the a_u plus the sum from the parent?) into the children. Wait, no. Because each step, the citizens are on their current node and must move. So the initial a_u is the citizens that were there at the start. Then, during the first step, they all move to children. Then, during the next steps, those citizens move again if their current node has children.

Wait, this is a bit confusing. Let's think of it step by step.

Initially, the bandit is at node 1. All citizens are in their initial positions.

Step 1:
- Citizens move. Each citizen on a node with outgoing edges (i.e., non-leaf) must choose one of the outgoing edges. So all citizens in node 1 (a_1) move to their children. Then the bandit moves to one of the children.

But the citizens can distribute a_1's citizens to the children in any way. For example, if node 1 has two children, they can split the a_1 into any ratio between them.

Then, in the next step, the bandit is at a child, say v. The citizens in v (from the previous step) must move to v's children (if any). Then the bandit moves again.

This continues until the bandit reaches a leaf. At that point, the citizens in that leaf (from the previous steps) are captured.

So the problem is to model the distribution of citizens through the tree such that, when the bandit chooses the path that leads to the maximum possible capture, the citizens have distributed in a way that minimizes this maximum.

So, for each node u, the value that the bandit can collect from u's subtree is determined by how the citizens distribute the available citizens among u's children. The optimal strategy for the citizens is to split the available citizens into the children in such a way that the maximum value among the children is as small as possible. The bandit will then choose the child with the maximum value.

Thus, for each node u, the value is the maximum of the children's values plus the a_u, but wait, no. Wait, when the citizens are in u, they can split into the children. Then, the bandit chooses a child. The value for u is the maximum of the children's values. But the citizens can split their a_u (plus any accumulated from above) into the children in a way that minimizes this maximum.

Wait, perhaps the value of a node u is the minimal possible maximum value among its children when the citizens distribute the a_u plus any incoming to u. Wait, but how?

Alternatively, the process can be modeled bottom-up.

For leaves, the value is a_i. Because once the bandit arrives there, he captures all the citizens present. So any leaf u's value is a_u (but wait, in the initial state, the citizens are at their nodes. So when the bandit arrives at a leaf, the citizens there are the ones that were there initially, but if the leaf has no children, the citizens can't move, so they are caught. But for a leaf, when the bandit arrives, there are no steps where the citizens move again. So the value for a leaf is the sum of all citizens that end up there.

Wait, maybe each node's value is the maximum possible number of citizens that the bandit can capture when starting from that node, given optimal play.

So for a leaf, the value is the a_i of that node, because when the bandit is there, he captures all a_i. But wait, the citizens could have moved there from the parent steps. Hmm, no. Because for a leaf, there are no outgoing edges, so the citizens in that node cannot move. So once the bandit arrives at a leaf, he captures all the citizens present there at that time.

But how do the citizens arrive there? For example, consider a tree where the root (1) has a child (2), which is a leaf. Then initially, the citizens are on node 1. The citizens must move to node 2 (since node 1 has outgoing edges). Then the bandit moves to node 2. Since node 2 is a leaf, the bandit captures all the citizens there. So the total is a_1 (all moved to 2) + a_2 (originally there). So the value for node 1 is a_1 + a_2.

Wait, but according to the first example:

Input:
3
1 1
3 1 2

So the tree is 1 → 2 and 1 → 3. So node 1 has two children (2 and 3). Both 2 and 3 are leaves (since their p_i is 1, and n=3, so nodes 2 and 3 have no children).

So initially, the bandit is at 1. The citizens in 1 (3) must move to either 2 or 3. Then the bandit chooses to go to 2 or 3.

The citizens want to split the 3 into two groups such that the maximum of (sum in 2 plus a_2, sum in 3 plus a_3) is minimized. Because the bandit will choose the maximum of these two.

In the first example, a_2 is 1, a_3 is 2. The citizens can split the 3 into 2 and 1. So 2 goes to 2 (1+2=3) and 1 goes to 3 (2+1=3). Then the bandit chooses either, resulting in 3. So the answer is 3.

So the value for node 1 is the minimal possible maximum of its children's (sum of their a_i plus the citizens sent to them) after splitting the a_1 (3 in this case) among the children.

So for each node u, the value is a_u plus the sum of the citizens that came into u from its parent (if any) split into the children. Then, the value of u is the minimal possible maximum value among its children. Because the citizens split optimally to minimize this maximum, and the bandit then chooses the maximum path.

Wait, no. Wait, the value of u is the maximum of the values of its children. But the citizens can split the a_u (their initial a_u) plus any citizens that come into u from the parent. Wait, maybe not. Let's think.

The total citizens in u's subtree is a_u plus all the citizens that come into it. But when the bandit is at u, the citizens present in u (from the parent steps) must move to u's children. So the value for u is the minimal possible maximum value of its children when the citizens distribute a_u (plus any incoming) into the children.

Wait, maybe the value of a node u is determined as follows:

- For a leaf node, the value is a_u. Because once the bandit arrives here, all citizens in this node are captured. But since it's a leaf, the citizens in this node can't move anymore.

- For a non-leaf node u, the citizens must distribute their a_u (initial) plus the citizens that came into u (from their parent) into the children. Then, the bandit will choose the child with the maximum value. The citizens will split the total (a_u + s, where s is the sum that came into u) into the children in such a way that the maximum of the children's values is minimized.

Wait, but the initial a_u is part of the sum that the citizens must distribute. For example, in the first step, node 1's a_1 is 3. The citizens there must split into children (2 and 3). So the total to split is 3. Then, each child's value is their own a_i plus the citizens sent to them, but for non-leaf nodes, those sent citizens would be split again into their children. But for leaves, the value is the sum of their a_i plus any citizens sent to them.

So the value of a node is the sum of the a_i in that node plus the citizens sent there, but only if it's a leaf. Otherwise, the value is determined by the minimal maximum of the children's values after distributing the a_u (plus incoming) into the children.

Wait, perhaps the value for a node is the maximum of the children's values, but the citizens can split the a_u (plus any that came in) into the children, so the minimal possible maximum after splitting.

So the problem reduces to, for each node u (starting from the leaves and moving up), compute the value as follows:

- If u is a leaf, then value[u] = a[u].

- Else, sum all the a[u] and the incoming citizens (but how?), and split them into the children such that the maximum of the children's value is minimized. Then the value[u] is this minimal maximum.

Wait, but the a[u] is fixed. Let me think again.

Let me model this as a recursive problem. For each node u, the value is the maximum of the children's values after the citizens split a[u] into the children.

Wait, maybe not. Let's think of the first example:

node 1 has a_1=3. It has two children: 2 (a_2=1, leaf) and 3 (a_3=2, leaf). The citizens can split the 3 from node 1 into the two children. For child 2, the value is 1 + x, where x is the number of citizens sent to it. For child 3, the value is 2 + (3 - x). The citizens choose x to minimize the maximum of (1+x, 2+(3 -x)). The minimal maximum is when 1 +x = 5 -x → x=2. So 3 and 3. So the value for node 1 is 3.

So the value of node 1 is 3. The bandit can choose either child, resulting in 3 captured. So the answer is 3.

So the value for non-leaf nodes is the minimal possible maximum among their children's values when a[u] is split among them. The split must be such that the sum of the split is a[u], and each split part is added to the child's value (which is the value of that child's subtree).

Wait, but the a[u] is the initial number of citizens in u. So when the bandit is at u, the citizens from u (a_u) must move to the children. So they split a_u into the children. So for each child v, they send s_v citizens such that sum(s_v) = a_u. Then, the value of u is the maximum of (value[v] + s_v) for all children v. The citizens want to choose s_v to minimize this maximum.

Wait, that makes sense. Because when the bandit is at u, the citizens split a_u into s_v (summing to a_u) among the children. Then, for each child v, the value is s_v plus the value of v's subtree. The bandit will choose the child with the maximum such value. The citizens' optimal choice is to split s_v in such a way that the maximum of (s_v + value[v]) is as small as possible.

Yes, this seems correct. So the problem can be modeled by calculating for each node u (starting from the leaves and moving upwards) the minimal possible maximum of (s_v + value[v]), where sum of s_v is a_u.

So, for each node u (non-leaf), the value is the minimal maximum of (s_v + value[v]) over all children v, given that sum(s_v) = a_u.

But how to compute this?

Let me think of the children of u. Let's say u has children v_1, v_2, ..., v_k. The value for each v_i is known. The citizens can distribute a_u as s_1, s_2, ..., s_k (summing to a_u), such that the maximum (s_i + value[v_i]) is minimized.

This is an optimization problem. The minimal possible maximum.

What's the optimal way to split a_u into s_i's such that sum(s_i) = a_u, and the maximum of (s_i + value[v_i]) is minimized.

This is similar to the problem of distributing a resource to minimize the maximum after adding to each item.

Let me consider the example where u has two children v1 and v2 with values c1 and c2. We need to split s1 + s2 = a_u, such that max(s1 + c1, s2 + c2) is minimized.

The minimal maximum is achieved when s1 + c1 = s2 + c2. Because if one is higher than the other, you can adjust the split to make them more balanced.

So, in this case, the optimal maximum would be (a_u + c1 + c2)/2, if possible. But if a_u is not sufficient to make both equal, then we take the maximum between the two.

Wait, let's see. Suppose a_u is 3, c1 is 1, c2 is 2. Then, the optimal split is s1=2, s2=1. Then s1 +c1=3, s2 +c2=3. The maximum is 3.

If c1=1 and c2=4, and a_u=3. Then the optimal split is s1=3, s2=0. Then s1 +c1=4, s2 +c2=4. Wait, but that's 3 +1=4 and 0+4=4. Sum s1 +s2 =3.

Alternatively, if a_u is 5, c1=1, c2=4. Then possible to split s1=2, s2=3. Then 3 and 7. So maximum is 7. Alternatively, split s1=5, s2=0. Then 6 and 4. Maximum 6. So better.

So in this case, the minimal maximum is 6. Because the sum of s1 is 5, which added to c1=1 gives 6. s2 is 0, added to c2=4 gives 4.

So the minimal maximum is max(1 + s1, 4 + s2) with s1 + s2 =5.

To minimize the maximum, the best is to make s1 as large as possible (since c1 is smaller than c2). Because adding to the smaller c will give a better chance to balance the maximum.

Wait, in this case, the optimal split would be to set s2=0, s1=5. So maximum is 6. If we split s1=4, s2=1: maximum is 5 and 5. So 5. But 4+1=5? 4+1=5. So 4+1=5, but s1=4, s2=1. Then s1 +c1=5, s2 +c2=5. So maximum is 5. Which is better than 6.

Wait, this contradicts my earlier reasoning. So what's wrong here.

Ah, right. The sum of s1 and s2 must equal a_u, which is 5. So in this case, c1=1, c2=4. The goal is to split s1 + s2 =5 such that max(1 + s1, 4 + s2) is minimized.

If s1=4, s2=1: 1+4=5, 4+1=5 → max 5.

If s1=5, s2=0 → 6 and 4 → max 6.

So the optimal split is 4 and 1, leading to max 5.

So the minimal possible maximum is 5. So the initial approach of balancing the two was correct.

So the approach is, for two children, to set s1 + c1 = s2 + c2, but only if possible given the a_u.

So the formula is:

desired = (a_u + c1 + c2) / 2

s1 = desired - c1

s2 = a_u - s1

But if s1 is negative, then set s1=0, s2=a_u. Then the maximum is max(c1 +0, c2 +a_u) = max(c1, a_u + c2). Similarly if s2 is negative.

Wait, but how to generalize this.

Alternatively, the minimal maximum is the maximum between (sum a_u + sum c_i) / k, where k is the number of children, but I'm not sure.

Alternatively, for each node u with children v_1, v_2, ..., v_k, each with value c_i, the citizens must distribute s_1 + s_2 + ... + s_k = a_u, such that the maximum (s_i + c_i) is as small as possible.

This is a classic optimization problem. The minimal possible maximum is the minimal value m such that for each c_i, s_i >= m - c_i, and sum (s_i) = a_u.

But since s_i >= m - c_i for all i, then sum (s_i) >= sum (m - c_i). So sum (m - c_i) <= a_u → m <= (a_u + sum c_i) / k.

Wait, no. Let's think again. The sum of s_i is a_u.

The sum of (m - c_i) must be <= a_u.

m *k - sum c_i <= a_u → m <= (a_u + sum c_i)/k.

But since the maximum of (s_i + c_i) is m, then each s_i + c_i <= m → s_i <= m - c_i. Wait, no: s_i + c_i <= m → s_i <= m - c_i. So sum s_i <= sum (m - c_i). But sum s_i is a_u. So sum (m - c_i) >= a_u → m >= (a_u + sum c_i)/k.

So the minimal possible m is the maximum between the maximum c_i and (a_u + sum c_i)/k.

Wait, but perhaps not. Let's see.

Suppose that (a_u + sum c_i) / k >= max c_i. Then, the minimal possible m is (a_u + sum c_i)/k. Because you can distribute s_i = m - c_i for each i, sum to a_u.

But if (a_u + sum c_i)/k < max c_i, then m must be at least max c_i, because one of the s_i + c_i is at least c_i (since s_i >=0). So in that case, the minimal m is max c_i.

So the minimal possible m is the maximum between the maximum c_i and the ceiling (but since fractions are allowed here, perhaps it's the exact value) of (a_u + sum c_i)/k.

Wait, but in the case where (a_u + sum c_i)/k < max c_i, then even if you distribute s_i as (m - c_i) for all i, the sum would be (m *k - sum c_i). If m is max c_i, then sum s_i would be (max_c *k - sum c_i). If this is less than a_u, then we can't. So in that case, perhaps m must be higher than (a_u + sum c_i)/k.

Wait, this is getting complicated. Let's think with examples.

Case 1: a_u =3, c1=1, c2=2 (from first example).

sum c_i =3. (1+2) =3. k=2.

(a_u + sum c_i)/k = (3+3)/2=3. max c_i is 2. So the minimal m is max(2, 3) =3.

Which matches the example.

Case 2: a_u=5, c1=1, c2=4.

sum c_i=5. (5+5)/2=5. max c_i=4. So m=5.

Which allows s1=5-1=4, s2=5-4=1. Sum 4+1=5 =a_u. So yes. The maximum is 5.

Another example where (a_u + sum c_i)/k is larger than max c_i.

Case 3: a_u=3, c1=1, c2=4.

sum c_i=5. (3+5)/2=4. max c_i=4. So m=4.

Wait, then sum s_i = (4-1)+(4-4) =3+0=3 =a_u. So yes. Then the maximum is max(4, 4) =4. So the answer is 4.

But in this case, a_u=3, c1=1, c2=4.

If citizens split s1=3, s2=0. Then max(3+1=4, 0+4=4). So 4.

Which matches the m=4.

So the formula seems to hold.

Another example where (a_u + sum c_i)/k < max_c.

Let's say a_u=2, c1=3, c2=4. So sum c_i=7. (2+7)/2=4.5. max_c=4.

So m is 4.5. But max_c is 4. So the minimal m is 4.5.

But that's higher than max_c. So in this case, how?

s1 =4.5 -3=1.5, s2=4.5-4=0.5. sum is 2.

Then s1 + c1=4.5, s2 +c2=4.5. So maximum is 4.5.

But the max_c is 4. So the formula says m=4.5.

But the initial thought was that m can't be lower than max_c. But in this case, the maximum of (s_i +c_i) is 4.5, which is higher than max_c (4). So the formula still holds.

So in general, the minimal possible m is the maximum between the maximum of c_i and the value (a_u + sum c_i)/k.

So for each node u, the value is this m.

So, the algorithm is:

1. For each node, compute the value as follows:

   a. If the node is a leaf (has no children), then value is a_u.

   b. Else, collect the values of all children. Compute sum_children = sum of children's values. k = number of children. max_child = max(children's values).

   c. Compute m = max(max_child, (a_u + sum_children) / k).

   d. The value of u is m.

But wait, in the first example, the sum_children is 1+2=3. a_u=3. (3+3)/2=3. max_child=2. So m=3.

Which matches the example.

Another example: the second sample input.

Sample Input 2:

3

1 1

3 1 3

So the tree is 1 →2 and 1→3. Both children are leaves.

The citizens in 1 (3) must split into two children.

The sum_children =1+3=4. (3+4)/2=3.5. max_child=3.

So m=3.5. But the bandit will choose the child with maximum value. But the citizens split to make the maximum as 3.5.

Wait, but the actual a_2 and a_3 are 1 and 3. So the split is:

s1 + s2 =3.

The values for the children would be 1 + s1 (for 2) and 3 + s2 (for 3).

The optimal split is to have 1 + s1 <=3.5 and 3 + s2 <=3.5.

s1 = 3.5 -1 =2.5.

s2 =3.5-3=0.5.

sum s1 + s2 =3.0. So yes.

But 2.5 +0.5 =3. So sum is correct.

So the values are 3.5 for both children, so the maximum is 3.5. But since the a_u is 3, and sum_children is 4, m is 3.5.

But the answer for the second sample is 4.

Wait, the sample input 2 output is 4.

Hmm. Let's see. What's the problem here.

Sample input 2's note says that no matter how the citizens act, the bandit can catch at least 4.

So according to the note, the answer is 4.

But according to our formula, the value of node 1 would be max(3, (3+1+3)/2) = max(3, 3.5) → 3.5. So the answer would be 3.5. But that's a fraction, which is not possible. Or wait, perhaps the a_u is 3, and the sum of the children's values is 4 (1 and 3). So (3 +4)/2 =3.5. But how can the citizens split the 3 into s1 and s2 such that 1+s1 <=3.5 and 3 +s2 <=3.5.

s1 =3.5-1=2.5, but 3.5-3=0.5. So s1 +s2 =3.0. That works.

So the maximum is 3.5. But the answer is 4.

Wait, there's a contradiction here. So my approach must be wrong.

Wait, perhaps the model is incorrect. Let's look at the sample input 2.

Sample Input 2:

3

1 1

3 1 3

So nodes 2 and 3 are leaves.

The initial a_1 is 3. Citizens must split into two children.

The optimal split would try to minimize the maximum of (1+s1, 3+s2) where s1+s2=3.

So the citizens can choose s1 and s2 such that max(1+s1, 3+s2) is as small as possible.

The minimal maximum is achieved when 1+s1 =3 +s2. Since s1 + s2=3.

So:

1 +s1 =3 + (3 -s1).

1 +s1 =6 -s1 → 2s1 =5 → s1=2.5, s2=0.5.

Then, the maximum is 3.5.

But according to the sample output, the answer is 4.

So why is that?

Ah, because in the sample note, the answer is 4. So according to the problem statement, the bandit can catch 4 citizens. But according to this model, the answer is 3.5. But citizens can't split in fractions. Wait, the problem allows citizens to split in any possible way, including fractions? Or do they have to be integers?

The problem statement says that a_i can be up to 1e9, but in the input, a_i can be zero. But during the movement, the citizens can choose any split, but in reality, the number of citizens is an integer. So perhaps the model must use integer splits.

Wait, the problem statement says "each citizen chooses one of the outgoing roads". So the split must be integers. So s_v must be an integer.

So in the sample input 2, the split s1 and s2 must sum to 3, but be integers.

So possible splits are:

0 and 3 → max(1+0=1, 3+3=6 →6) → bandit captures 6.

1 and 2 → max(2,5) →5.

2 and 1 →3 and4 →4.

3 and 0 →4 and3 →4.

So the minimal maximum possible is 4.

But according to the model, the formula (3 +4)/2=3.5 would be the optimal, but since we can't split into fractions, the minimal maximum is 4.

Ah, so the model works for real numbers, but the actual problem requires integer splits. So my initial approach is wrong.

But the problem statement says nothing about the splits being integers. But the input a_i can be up to 1e9, which suggests that the splits can be in any possible real numbers. But the problem says "each citizen that is currently on a square with some outgoing one-way roads chooses one of such roads and moves along it to another square." So each citizen must choose a road. So the split is possible only in integers. Because each citizen is a discrete entity.

But the problem statement says that a_i can be up to 1e9. So handling this as fractions would be possible, but maybe the model assumes that it's possible to split into fractions. But in reality, the problem may require integer splits.

But in the sample input 1, the answer is 3, which is possible with a split of 2 and 1 (sum 3). So that model works. But for sample input 2, according to the model, the answer would be 3.5, which is not possible. So the initial model is incorrect.

So the problem requires that the splits are integers. Thus, the model needs to be adjusted to account for integer splits.

But handling this for large n and large a_i would be computationally challenging. So there must be a way to model this with integer splits.

Wait, but the sample input 2's note says that the answer is 4. Let's see why.

The initial a_1 is 3. The citizens can split into s1=3, s2=0 → node 2 has 1+3=4, node 3 has 3+0=3. Bandit chooses node 2 →4.

Alternatively, split s1=2, s2=1 → node2:3, node3:4. Bandit chooses node3 →4.

Or s1=1, s2=2 → node2:2, node3:5. Bandit chooses 5.

So the minimal maximum is 4.

So the citizens can't split into fractions, so they have to choose s1=3, s2=0. Or other splits that result in maximum 4.

So the optimal split for citizens is to have maximum 4. Hence, the answer is 4.

So the model must be adjusted to account for integer splits.

But how to model this?

Alternatively, perhaps the problem allows splitting into real numbers, but the answer is rounded to the nearest integer. But sample input 2's answer is 4, which is higher than 3.5. So that's not possible.

Alternatively, the problem's model is that the citizens can split into real numbers, and the answer is the minimal maximum possible, which can be a real, but the output is an integer.

But sample input 2's output is 4. So perhaps the model allows for real splits, but the correct answer for sample input 2 is 3.5. But the sample output is 4. Which contradicts.

Hmm, this is a problem. So perhaps the model is incorrect.

Let me re-examine the problem statement.

The problem says that citizens can choose any outgoing road, and move along it. So each citizen moves to one child. So the split s_v is the number of citizens that move to child v, which is an integer.

So in this case, the splits must be integers. So for the sample input 2, the minimal maximum is 4.

But how to model this for large n and a_i up to 1e9?

This makes the problem much more complex. The initial approach of using (a_u + sum_c) / k is for continuous splits. But with integer splits, the minimal maximum is the ceiling of (a_u + sum_c) /k, or the maximum of (ceil((a_u + sum_c)/k), max_c).

But how to compute this.

Alternatively, the initial approach is correct, and the problem allows splitting into real numbers, which would make the answer in sample input 2 to be 3.5, but according to the sample output, it's 4. So this suggests that the initial model is wrong.

But the sample input 2's note says that no matter how the citizens split, the bandit can capture at least 4. So the answer is 4.

So the model must be different. What's wrong here.

Wait, perhaps I'm misunderstanding the problem. Let's re-examine the problem statement.

The bandit wants to maximize the number of citizens caught, the citizens want to minimize it. Both act optimally.

In the second sample, the citizens cannot split the 3 in such a way that the maximum of the two children's values is less than 4. So the answer is 4.

So the minimal maximum is 4. So the model must output 4.

But according to the initial approach, the model would compute (3 +1+3)/2 = 3.5, which is 3.5. But the maximum of (3.5, 3.5) would be 3.5. So why is the answer 4?

Ah, because the bandit's path is determined by the actual values after splitting. But perhaps the citizens can't split into fractions. So the initial approach is incorrect.

So the problem requires that splits are integers, and the model must take this into account.

So the problem is to model the splits as integers. Which makes the problem much more challenging.

So how to model this.

Let's think of the problem again.

For each node u, the value is the minimal possible maximum among the children's values (after adding s_v) given that sum of s_v = a_u, and s_v are non-negative integers.

So for the second sample:

a_u =3. Children c1=1, c2=3.

We need to split s1 + s2 =3. s1 and s2 are non-negative integers.

The maximum of (1+s1, 3+s2).

We need to choose s1 and s2 such that this maximum is as small as possible.

Possible splits:

s1=3, s2=0 → max(4,3) →4.

s1=2, s2=1 →3,4 →4.

s1=1, s2=2 →2,5 →5.

s1=0, s2=3 →1,6 →6.

So the minimal possible maximum is 4.

So the value of node 1 is 4. Hence, the answer is 4.

But according to the initial approach (using real numbers), the value would be 3.5. So the model must take into account that splits are integers.

Thus, the initial approach is incorrect. So we need a different way to model this.

But how to compute this for large n and a_i up to 1e9.

An alternative approach is to realize that for each node u, the minimal maximum when splits are integers is ceil( (a_u + sum_c) /k ), but not less than the maximum c_i.

Wait, for the second sample:

sum_c=4, a_u=3. (3+4)/2=3.5 → ceil(3.5)=4. Which matches the sample.

Another example: a_u=3, c1=1, c2=2. sum_c=3. (3+3)/2=3 → ceil(3)=3. Which matches the first sample.

Another example: a_u=5, c1=1, c2=4. sum_c=5 →5+5=10/2=5. So ceil(5)=5. Which would split into s1=4, s2=1. Then 5 and 5. Which is correct.

So the formula could be that for each node u with children:

value[u] = max( max_c, ceil( (a_u + sum_c) / k ) )

But how to compute this.

But why would this be the case.

For example, if (a_u + sum_c) is exactly divisible by k, then it's exactly (a_u + sum_c)/k. Otherwise, it's the ceiling.

Yes. Because sum_c is the sum of the children's values.

But why.

Let me think of the general case.

We need to split a_u into k children's s_v such that sum s_v =a_u and s_v >=0.

The goal is to minimize the maximum (s_v + c_v).

The minimal possible maximum is the minimal m such that for each child v, s_v >= m -c_v. And sum (m -c_v) <= a_u.

But since the s_v are integers, m must be such that sum (m - c_v) <=a_u, and m is the minimal possible.

But how to find m.

Wait, the minimal m is the smallest integer m such that:

sum (m -c_v) <=a_u.

But also, m >= max c_v.

So solving for m:

sum (m - c_v) =k*m - sum c_v <=a_u.

=> m <= (a_u + sum_c)/k.

But m must be an integer. So the minimal m is the maximum between the maximum c_v and ceil( (a_u + sum_c) /k )

Wait, no. Because the sum of (m -c_v) must be >=a_u.

Wait, wait, no. Because for each s_v >= m -c_v, sum s_v >= sum (m -c_v).

But sum s_v is equal to a_u. So sum (m -c_v) <=a_u.

=> k*m - sum_c <=a_u.

=> m <= (a_u + sum_c)/k.

But m must be as small as possible. So the minimal m is the maximum between the maximum c_v and the ceiling of (a_u + sum_c -1)/k +1 ?

Wait, this is getting complicated. Let's try to find m.

The minimal m is the smallest integer such that:

m >= max_c,

and k*m - sum_c <=a_u.

So:

m >= max_c.

and m <= (a_u + sum_c)/k.

But since m must be >= max_c, the minimal m is the maximum between max_c and ceil( (a_u + sum_c) /k ).

Wait, no. For example:

a_u=3, sum_c=3, k=2. (3+3)/2=3. So ceil(3) =3. max_c=2.

So m=3.

Another example: a_u=3, sum_c=4, k=2. (3+4)/2=3.5. ceil(3.5) =4. max_c=3.

So m=4.

Which matches the sample.

Another example: a_u=5, sum_c=5, k=2. (5+5)/2=5. ceil(5) =5. max_c=4. So m=5.

Which is correct.

So the formula is:

m = max( max_c, ceil( (a_u + sum_c) /k ) )

But how to compute this.

Yes. So for each node u, the value is the maximum between the maximum of its children's values and the ceiling of (a_u + sum_c) divided by the number of children.

Thus, the algorithm becomes:

For each node u:

If u is a leaf, value[u] =a_u.

Else:

sum_c = sum of children's values.

k = number of children.

max_c = max(children's values).

m = max( max_c, (a_u + sum_c +k -1) //k )

value[u] =m.

This formula uses integer division with ceiling. (a +b -1) //b gives the ceiling of a/b.

So for example:

a_u + sum_c =7, k=2 → (7 +2-1)/2 =8/2=4.

Which is correct.

Another example: a_u=3, sum_c=3, k=2. (3+3 +2-1)/2 → (8-1? Wait, 3+3 is 6, plus k-1=1 → 7 →7/2=3.5 → integer division gives 3. But ceil(6/2) is 3.

Wait, maybe the formula for ceiling(a/b) is (a +b -1)//b.

Yes. So (a +b-1) //b.

So for a=3, sum_c=4 → a_u + sum_c =7. k=2 →7+2-1=8. 8//2=4.

Which is correct.

So the formula for m is:

m = max( max_c, (a_u + sum_c +k-1) //k )

This handles the integer division with ceiling.

Thus, the model is:

For each node u, compute value[u] as:

if u is a leaf: a_u.

else:

sum_c = sum of value[v] for children v of u.

max_c = max(value[v] for v in children).

k = number of children.

value_u = max( max_c, (a_u + sum_c + k-1) //k )

So, for the second sample:

sum_c=1+3=4.

k=2.

a_u=3.

(3+4 +2-1)/2 → (7+1)/2=8/2=4.

max_c=3.

value_u= max(3,4) →4.

Which matches the sample.

For the first sample:

sum_c=3. (3+3 +2-1)/2= (6+1)/2=7/2=3.5 → integer division is 3.

max_c=2.

value_u= max(2,3) →3.

Which matches the sample.

So this model works.

Thus, the approach is to process the tree in post-order (since children's values are needed before parents), and for each node, compute its value as per the formula above.

The steps are:

1. Read the tree structure. Since the tree is given in a way that each node's parent is before it, we can build a tree structure by having a list of children for each node.

2. Compute for each node, its children.

3. Process the nodes in reverse order (post-order traversal), starting from the leaves and moving up to the root.

4. For each node, compute its value based on the children's values.

The root is node 1, and the answer is the value of node 1.

Now, the problem is to implement this efficiently.

Given that n can be up to 2e5, we need an O(n) algorithm.

The steps:

- Read the parent array for nodes 2 to n.

- Build a list of children for each node. For example, children[u] is a list of all children of u.

- Compute the value for each node in post-order (starting from leaves, which are nodes with no children).

So, for each node u in 1..n, process its children first.

But how to process in post-order.

We can perform a post-order traversal of the tree.

Alternatively, we can process the nodes in reverse order (from n downto 1), since the tree is a rooted tree where parents are always less than the children. So nodes with higher numbers can't be parents of lower numbers.

Thus, node n can be processed first, then n-1, etc., down to 1.

But each node's parent is stored, and the children can be built as a list.

So for each node u from n downto 1:

   if u is a leaf (children[u] is empty), then value[u] =a[u].

   else:

      sum_c = sum of value[v] for all v in children[u].

      max_c = max( value[v] for v in children[u] )

      k = len(children[u])

      value[u] = max( max_c, (a[u] + sum_c + k-1) //k )

But how to compute sum and max efficiently.

Yes. For each node, we need to iterate over its children and sum their values, find the maximum.

This would be O(n) in total.

Because each node is processed once, and each child is visited exactly once when processing the parent.

So, for n=2e5, this is manageable.

Thus, the code can be written as follows.

Read n.

Read p_2 to p_n, which are the parents of nodes 2 to n.

Build a children list.

Read a array (0-based or 1-based).

Process nodes from n downto 1:

   if children[u] is empty:

      value[u] =a[u]

   else:

      sum_c = sum of value[v] for v in children[u]

      max_c = max of value[v] for v in children[u]

      k = len(children[u])

      value[u] = max( max_c, (a[u] + sum_c +k -1) //k )

The answer is value[1].

Now, let's test this model against the samples.

Sample Input 1:

3

1 1 → children[1] = [2,3]

a = [3,1,2]

Processing nodes 3, 2, 1.

node 3: no children → value[3]=2.

node 2: no children → value[2]=1.

node 1:

sum_c =1 +2=3.

max_c=2.

k=2.

(3 +3 +2-1)/2 → (6 +1)/2=7/2=3.5 → 3.5 is 3.5, but integer division gives 3.5 → floor would be 3, but (3+3+1)/2=7/2=3.5 → (7)//2=3. So the formula (3 +3 +2-1) is 3+3=6, 2-1=1, 6+1=7. 7//2=3. So value[u] =max(2,3) →3.

Which is correct.

Sample Input 2:

3

1 1 → children[1] = [2,3]

a =3,1,3.

Processing nodes 3,2,1.

node3: value=3.

node2: value=1.

node1: sum_c=1+3=4. max_c=3. k=2.

(3 +4 +2-1)/2 → (7+1)/2=8/2=4. max(3,4)=4. So value is4.

Which matches the sample.

Thus, the model works.

Now, the code can be written as follows.

Read n.

Read p_2 to p_n as list.

Build a children list: for each u in 2..n, add u to children[p[u]].

Read a list as a_1, a_2, ..., a_n.

Initialize an array value of size n+1 (since nodes are 1-based).

For u from n downto 1:

   if not children[u]:

      value[u] =a[u-1]  # assuming a is 0-based.

   else:

      sum_c =0

      max_c =0

      for v in children[u]:

          sum_c += value[v]

          if value[v] > max_c:

              max_c = value[v]

      k = len(children[u])

      total = a[u-1] + sum_c

      temp = (total + k -1) // k

      value[u] = max(max_c, temp)

print(value[1])

Wait, the a array is given as a_1 to a_n. So for node 1, a[0] in 0-based.

Yes.

But for the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    p = list(map(int, input_stream.readline().rstrip("\n").split())) # p[0] is p_2, p[1] is p_3, etc.

    children = [[] for _ in range(n+1)]

    for i in range(2, n+1):

        parent = p[i-2] # since p is for 2 to n. i starts at 2, so p[i-2] is the correct index.

        children[parent].append(i)

    a = list(map(int, input_stream.readline().rstrip("\n").split())) # a is 0-based. a[0] is a_1, a[1] is a_2, etc.

    value = [0]*(n+1)

    for u in range(n, 0, -1):

        if not children[u]: # leaf node

            value[u] = a[u-1]

        else:

            sum_c = 0

            max_c = 0

            for v in children[u]:

                sum_c += value[v]

                if value[v] > max_c:

                    max_c = value[v]

            k = len(children[u])

            total = a[u-1] + sum_c

            temp = (total + k -1) // k

            value[u] = max(max_c, temp)

    print(value[1], file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 1
3 1 3
""",
            "output": \
"""\
4
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

n=3.

p = [1,1]

a = [3,1,3]

u=3: value=3.

u=2: value=1.

u=1: sum_c=3+1=4, total=3+4=7 → (7 +2-1)/2 →8//2=4. max(3,4) →4.

Output 4.

Which matches.

Thus, the code should be correct.

Now, for handling large n (2e5), this code should be efficient. Because it's O(n) time.

Each node is processed once, and for each non-leaf node, we iterate over its children. Each edge is processed once. So the total time is O(n).

Space-wise, the children list uses O(n) space.

Thus, this code should work.
</think>

```python
n = int(input())
p = list(map(int, input().split()))
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    parent = p[i - 2]
    children[parent].append(i)
a = list(map(int, input().split()))
value = [0] * (n + 1)

for u in range(n, 0, -1):
    if not children[u]:
        value[u] = a[u - 1]
    else:
        sum_c = 0
        max_c = 0
        for v in children[u]:
            sum_c += value[v]
            if value[v] > max_c:
                max_c = value[v]
        k = len(children[u])
        total = a[u - 1] + sum_c
        temp = (total + k - 1) // k
        value[u] = max(max_c, temp)

print(value[1])
```
