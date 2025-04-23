<think>
Okay, let's see. I need to solve this problem where I have to check if the happiness indexes for all cities are possible based on the people's movement and their mood changes. 

First, the problem says that each person starts in the capital (city 1) and takes the shortest path back home. The mood can change from good to bad during their journey, but once it's bad, it stays bad. For each city, the happiness index is the number of good people minus the bad people passing through that city.

So, the main idea is to model how each person's mood affects the cities along their path. Let's think about each person's path. Suppose a person lives in city u. Their path is from 1 to u. Along the way, they pass through all the ancestors of u in the tree. The person's mood can only be ruined once, which means that for all cities up to some point, they are considered in good mood, and from that city onward, they are in bad mood. Or they might never have their mood ruined.

But how does this affect each city's h_i? For each city i, the h_i is (number of good people passing through i) minus (number of bad people passing through i). So, for each person, along their path, all cities up to where their mood was ruined will have a +1 if they were good, and all cities after (including the ruin point) will have a -1. Wait, no. Wait, the person's mood is good until they decide to ruin it. So, for example, if a person ruins their mood on the road between city a and city b (which are connected), then in city a, they are still in good mood (since the mood is determined when they are inside the city), and in city b and onwards, they are in bad mood. So, the cities along the path from the capital to their home can be split into two parts: the ones before the switch (included) where the person contributes +1, and the ones after (excluded?) where they contribute -1. Hmm, maybe the switch happens between two cities. Let's model this.

Each person's path is a sequence of cities from 1 to u. Let's say the person ruins their mood on the edge between city k and city next. Then, all cities in the path up to and including k are considered as good (so contribute +1 to h for those cities), and all cities after (next, next.next, etc.) contribute -1. But how to model this?

Alternatively, for a person from city u, the cities on their path are all ancestors of u. Let’s denote the path as 1 = v0, v1, ..., vk = u. For each city in their path, the person's contribution to h depends on where they turned their mood bad. If they turned bad on the edge between v_i and v_{i+1}, then all cities up to v_i (including) will have +1, and from v_{i+1} onwards, -1. So, the city v_i is the last city where the person was in a good mood, and the cities after that are in bad mood.

Wait, but the problem says that the person's mood can be ruined on the way. So, for each edge in their path, the person can choose to ruin their mood when traveling along that edge. Once ruined, all subsequent cities (those in the path after that edge) are considered bad.

So, for each person, their choice is to select an edge along their path (or none) where they ruin their mood. The cities in the path up to and including the starting node of that edge (the parent) will get +1, and the remaining cities (from the child node onward) will get -1.

Alternatively, the person can choose to not ruin their mood at all. Then, all cities in their path contribute +1.

So, the problem is to assign for each person a certain position in their path (the edge where they ruin their mood) such that the sum for each city's h_i is exactly the given h_i.

But how do we model this? Let's think of each person contributing to the cities along their path. For a person from city u, their contribution depends on where they decided to switch. The cities before the switch (including the parent node of the switch edge) get +1, and the cities after (child node and onwards) get -1.

Alternatively, for each person, let's model their contribution as follows: suppose the path from 1 to u is a certain length. The person can choose to switch at any edge along that path. Let's denote the depth of the node u as d (distance from root 1). Then, for each person in u's population p_u, their decision affects the h values of all ancestors of u (including u itself) along the path.

But how to model this for all people and all cities?

Hmm. Let's think in terms of the variables for each city. Let's denote for city i, the number of people who have their switch point in the subtree of i. Or perhaps, for each city u, let's find the number of people whose path includes u and for whom u is the last city in their path where they were in a good mood. Then, for each such person, all cities along their path up to u (including u) get +1, and the ones after (the children) get -1. Wait, maybe that's a way to model it.

Wait, the problem is similar to a flow where each person contributes +1 to all cities up to a certain point, and -1 to the cities after. So, for each city u, the h_i can be calculated as (sum of all people passing through u where u is in their good part) minus (sum of all people passing through u where u is in their bad part).

Alternatively, for each person, the path is their entire path. Let's say the person's switch is at edge (a, b), which is part of their path. So, all cities from 1 up to a will have +1 (since when they pass through a, they are in good mood), and all cities from b onwards will have -1 (since they pass through them in bad mood). So, the city a's h increases by 1, the city b's h decreases by 1, and so do all cities after b in the path.

Wait, but the edge (a, b) is part of the path. So, when the person moves from a to b, their mood is ruined. So, in city a, they are in good mood (they are in a when leaving), and when they arrive at b, their mood is bad. So, cities a and all before it in the path get +1, cities from b onwards get -1.

But how does this affect all the cities in the path? Let's take an example. Suppose the path is 1 -> 2 -> 3 -> 4. A person from city 4. Suppose the switch is on the edge 2-3. Then, cities 1 and 2 get +1, cities 3 and 4 get -1. So for each city in the path, the contribution is based on where the switch is made.

So, for each person, their contribution to the cities in their path depends on the switch point. Let's model this for all people in the tree.

But how do we model this for all cities and people efficiently?

An alternative approach is to model for each city u, the number of people in its subtree (including u) who have their switch point in u's parent edge. Because that would determine how many people's good part ends at u, and their bad part starts at the next edge.

Wait, perhaps the key is to model for each city u, two variables: g_u and b_u. The g_u is the number of people in the subtree of u (including u) that are in a good mood when passing through u, and b_u is the number of people in the subtree of u that are in bad mood when passing through u.

Wait, but how does this work? Because a person in the subtree of u will pass through u when going back home. If the switch happens in the edge leading to u (i.e., in the edge from parent of u to u), then that person's good mood ends at the parent of u, and u and below are in bad mood. So, in u, their contribution is -1. If the switch happens in the edge leaving u (like from u to a child), then in u, the person is in good mood, so contributes +1.

But this seems complicated. Maybe there's a smarter way.

Another approach: For each city u, the number of people passing through u is equal to the sum of the p's of all the cities in the subtree rooted at u. Because each person from the subtree of u must pass through u when going back home. So, the number of people passing through u is s_u = sum_{v in subtree of u} p_v.

So, for each city u, the sum of people passing through it is s_u. Now, the h_u is equal to (g_u - b_u), where g_u is the number of people passing through u in good mood, and b_u is the number passing through in bad mood. Since s_u = g_u + b_u, then h_u = (g_u - (s_u - g_u)) = 2g_u - s_u. So, rearranged, g_u = (h_u + s_u)/2.

But h_u must be such that (h_u + s_u) is even and non-negative, and g_u must be between 0 and s_u. Otherwise, it's impossible.

So, for each city u, the following conditions must hold:

1. h_u + s_u must be even.

2. (h_u + s_u)/2 must be >=0 and <= s_u.

If any of these conditions is not met, the answer is NO.

Additionally, there's another condition. For a city u, the number of people in good mood passing through u (g_u) must be equal to the number of people in good mood that passed through its parent (say, parent u is p) minus those who had their switch in the edge p->u.

Wait, perhaps for the tree hierarchy, the constraints between parent and child must be considered. Because, the number of people in good mood in the parent's subtree must be at least the number in the child's subtree. Because a person can't switch their mood in a way that the child's g_u is greater than the parent's g_p.

Wait, here's the idea. For a node u, the people who are in good mood in u's subtree (i.e., those whose switch hasn't happened yet) must be a subset of the people in good mood in the parent's subtree. Because if a person's switch happens in the edge between parent u and u, then in the parent's path, they were in good mood, but in u and below, they are in bad mood. So, the number of good people in u's subtree must be equal to the number of people in u's subtree that didn't switch in the edge leading to u.

So, for each node u, the g_u (number of good people passing through u) must equal the sum of the good people in all children of u's subtree plus the number of people in u's subtree (including u) that did not switch in the edge leading to u. Wait, this is getting a bit complicated.

Alternatively, let's model for each node u:

g_u is the number of people in the subtree of u (including u) that pass through u in good mood.

But how does this relate to the parent's g?

Let's think of the hierarchy. The parent of u is p. For u's subtree, the people in the subtree are contributing to g_u. However, some of these people may have switched their mood on the edge p-u. For those people, their good mood stops at p, so they are counted in p's g_p but not in u's g_u. But the people in the subtree of u that did not switch on the edge p-u (or any edge above) would have their good mood counted in both p's g_p and u's g_u.

So, for the parent p of u, the number of people in u's subtree that are in good mood when passing through u (g_u) must be less than or equal to the number of people in u's subtree that were in good mood when passing through p (which is part of p's g_p). Because any person in u's subtree that is in good mood in u must also have been in good mood in p (since their path passes through p before u). So, the number of such people (g_u) must be <= the number of people in u's subtree that were in good mood at p.

But the people in u's subtree that were in good mood at p are equal to the sum of the people in u's subtree (s_u) minus the number of people who switched on the edge p-u. Let's denote x as the number of people in u's subtree that switched on the edge p-u. Then, the number of people in u's subtree that were in good mood at p is (s_u - x). These people are then passing through u. But among them, those who switched on the edge p-u (x) are now in bad mood at u, contributing to b_u, and the rest (s_u - x - x_other) ?? Wait, maybe I'm overcomplicating.

Alternatively, the people in u's subtree contribute s_u to the parent p's s_p. For each person in u's subtree, their presence in the parent's path affects the g_p. If they switch on the edge p-u, then they contribute +1 to p's g_p and -1 to u's h_u, etc.

Wait, perhaps the key insight is that for each node u, the value of g_u (the number of people in good mood passing through u) must be equal to the sum of the g_v for all children v of u, plus the number of people in p_u (the number of people living in u) who have not switched their mood by the time they reach u, and the same applies for the rest of the subtree.

Alternatively, here's a step-by-step approach:

1. For each test case, compute the subtree sizes s_u for each node u. s_u is the sum of p_v for all descendants of u (including u itself). This can be done with a post-order traversal of the tree.

2. For each node u, check if (h_u + s_u) is even, and (h_u + s_u)/2 is between 0 and s_u. If any node fails this, answer is NO.

3. Then, for each node u, compute g_u = (h_u + s_u) // 2. Now, check if the sum of all g_children (sum of g_v for all children v of u) is <= g_u - p_u. Because the people living in u (p_u) must be part of the g_u. Wait, maybe not. Let me think again.

The people living in u (p_u) are part of the subtree of u, so their path includes u. So for each such person, if they are in good mood when passing through u, they contribute +1 to g_u. If their mood is ruined on the edge from u's parent to u, then they are counted as part of p's g_p but not in u's g_u.

Wait, perhaps the people living in u (p_u) must have their switch point after u. But that's not possible because their home is u. So, their path is up to u. So, for a person in u's home, their switch can be on any edge along their path from 1 to u. So, if their switch is on the edge leading to u (parent to u), then u's h would get -1. If they switch after u, but since u is their home, their path ends at u. So, for u's p_u people, their switch can be anywhere along their path. So, for u's own p_u people, they contribute to the g_u if their switch is not on any edge in their path (i.e., they are always in good mood) or if their switch is on an edge after u (which doesn't exist). Wait, but u is their home. So, their path is from 1 to u. So, their switch can be on any edge along that path. For example, the edges leading to u's ancestors.

So, for the people in u's p_u, their contribution to g_u is +1 if they didn't switch on any edge leading to u. Otherwise, if they switched on an edge in the path from 1 to u (say, in the edge between a and b, where b is in the path), then in u's case, since u is after b, their contribution is -1.

Hmm, perhaps the approach is to model for each node u, the constraints that the sum of the good people in all its children plus the number of people in the subtree of u (including u) that did not switch in the edge leading to u must equal g_u.

But this is getting too vague. Let's look for a pattern here.

Another idea: For each node u, the value of g_u (the good people passing through u) must be equal to the sum of g_v for all children v of u plus (s_u - sum_children_s_v) * 1, because those are the people living in u (since sum_children_s_v is sum of s_v for all children of u, so s_u - sum_children_s_v is p_u). But wait, no. The s_u is sum of all p_v in u's subtree. For the children v of u, s_v is their subtree. So, s_u = p_u + sum(s_v for all children v of u). 

So, for each node u, s_u = p_u + sum(s_v for children v of u).

Now, for the g_u, which is (h_u + s_u)/2. The key is that the sum of g_v for all children v of u plus the number of people in u's subtree (excluding children's subtrees) that didn't switch in u's edge. Because those people (the p_u plus any in children?) No, perhaps not.

Alternatively, the people in u's subtree consist of:

1. The people in u's own p_u.

2. The people in the subtrees of u's children.

So, for u's g_u, the good people passing through u are:

- All the good people from the children's subtrees (sum of g_v for children v of u). Because these people must have passed through u in good mood (since they are in their children's g_v, which implies that their switch is after u, so they were in good mood when passing through u).

Plus, the people in u's own p_u who decided not to switch on any edge along their path. For these people, their path includes u, and they are in good mood when passing through u. So, their contribution to g_u is 1.

Additionally, the people in u's own p_u who switched on some edge before reaching u. For these people, their contribution to g_u is -1.

Wait, but how does that fit into the model?

Alternatively, the people in u's own p_u can choose where to switch. For example, someone in u's p_u can switch on any edge along the path from 1 to u. Suppose they switch on edge (a, b), which is part of their path. Then, in all cities from 1 to a, they are in good mood (+1), and in cities from b to u, they are in bad mood (-1). So, their contribution to u's h_u is -1. But if they do not switch, their contribution to all cities in their path (including u) is +1.

But how does this affect the sum for u's g_u?

Each person in u's p_u contributes either +1 or -1 to h_u. So, the sum of their contributions is (number of people in p_u who did not switch in any edge up to u) - (number of people in p_u who did switch in any edge up to u). Let's call the number of people in p_u who did not switch along their path (i.e., stayed in good mood) as x. Then, the sum from p_u is x - (p_u - x) = 2x - p_u. So, the total contribution to h_u from p_u is 2x - p_u. But h_u is the sum of contributions from all people passing through u.

But for the people in the subtrees of u's children, their contribution to h_u depends on whether they switched before reaching u. For example, a person in child v's subtree who switched on an edge between u and v (the parent of v) would contribute -1 to u's h_u. If they switched on a higher edge, then u is part of their good path, contributing +1.

Wait, but if a person is in the subtree of v (a child of u), then their path to home is 1 -> ... -> u -> v -> ... -> their home. So, if they switched on an edge between u and v, then in u they are in good mood (since the switch happens on the edge u-v), so u's h increases by 1, and v's h decreases by 1, etc. So, for such a person, their contribution to u is +1. But when the person is in their own home, the switch is on the edge u-v, then u's h is +1, but v's h is -1. So, the person contributes +1 to u, but -1 to v and beyond.

But this complicates the model. How to aggregate all this?

Alternatively, the initial approach where for each node u, we compute s_u and check that (h_u + s_u) is even and that g_u = (h_u + s_u)/2 is within 0 and s_u. Then, for the tree hierarchy, the sum of the g's of the children must be <= g_u - p_u. Wait, maybe not. Let's think.

For a node u, the sum of the g_v for all children v of u plus the number of people in u's subtree (excluding children) who are in good mood (x) must equal g_u. Because each child's g_v represents the number of people in their subtree that passed through v in good mood (and thus also passed through u in good mood). The x is the number of people in u's own p_u who are in good mood when passing through u. 

But x can be at most p_u. So, sum(g_v) + x = g_u. And x must be between 0 and p_u. Also, x can't be more than p_u, since those are the people living in u. So, sum(g_v) <= g_u <= sum(g_v) + p_u.

But sum(g_v) is the sum of the children's g's. So, we can compute sum_g_children = sum(g_v for all children v of u). Then, x = g_u - sum_g_children. This x must be between 0 and p_u. Because x is the number of people in u's own p_u that are in good mood (i.e., did not switch in any edge along their path to u). 

Wait, no. Because x is the number of people in u's own p_u that are in good mood when passing through u. Which includes those who did not switch anywhere (so contribute +1 to all cities on their path) and those who switched after u (but u is their home, so they can't switch after u). So, for u's own p_u people, they can only switch on edges along their path from 1 to u. If they switch on an edge in their path, then u's h is part of the bad cities (so contributes -1 to u's h).

So, the number of people in u's p_u that contribute +1 to h_u is x, and the rest (p_u - x) contribute -1. The total contribution from p_u is x - (p_u - x) = 2x - p_u. 

But for all people passing through u (including those in u's own p_u and those in the subtrees), the h_u is (sum of +1 for good, -1 for bad). So:

h_u = (g_u - (s_u - g_u)) = 2g_u - s_u. Which gives g_u = (h_u + s_u)/2.

But the key is that for the node u, the sum of its children's g_v plus the x (number of people in u's p_u that are in good mood) must equal g_u. So:

sum_g_children + x = g_u.

But x can be between 0 and p_u, and sum_g_children can't exceed g_u. So:

sum_g_children <= g_u <= sum_g_children + p_u.

But x is g_u - sum_g_children, which must be between 0 and p_u. So:

0 <= g_u - sum_g_children <= p_u.

Which simplifies to:

sum_g_children <= g_u <= sum_g_children + p_u.

So, for each node u, after computing g_u and s_u, we need to check if the sum of the children's g's is <= g_u, and that g_u <= sum_children_g + p_u. 

If this condition is violated for any node, then the answer is NO.

So, the steps are:

For each test case:

1. Read n, m, p array, h array, and the tree edges.

2. Check if the sum of p is m. If not, it's impossible. But the problem says that the sum is m. So we can ignore this check.

3. Build the tree structure. Since the tree is given as edges, we can build an adjacency list. Then, perform a post-order traversal to compute s_u (the sum of p in the subtree rooted at u). For this, we need to root the tree at 1.

4. For each node u, compute s_u. Also, compute g_u = (h_u + s_u)/2. Check if h_u + s_u is even, and g_u is between 0 and s_u. If any node fails, output NO.

5. For each node u (starting from the leaves and moving up to the root), compute the sum of the g's of its children. Then, check if sum_g_children <= g_u <= sum_g_children + p_u. If not, output NO.

6. If all checks pass, output YES.

But how to compute the sum of the children's g's? Since we need to process the tree in a bottom-up manner (children processed before parents), a post-order traversal is suitable.

So, the steps in code would be:

- For each test case:

   - Build the tree with root 1.

   - Compute s_u for each node via post-order traversal.

   - Check for each u: (h_u + s_u) must be even, and 0 <= (h_u + s_u)/2 <= s_u.

   - For each u, compute g_u.

   - Then, perform another post-order traversal to compute for each u the sum_g_children (sum of g_v for all children v).

   - Check if sum_g_children <= g_u <= sum_g_children + p_u. If not, return NO.

   - Also, for the root (node 1), after processing, we need to ensure that the sum_g_children (sum of g_v for children of root) plus x (which is g_1 - sum_g_children) must be <= p_1. But according to the previous condition, since for root 1, sum_g_children <= g_1 <= sum_g_children + p_1.

But wait, for the root node, the sum_g_children is the sum of g_v for all its children. The x for the root is g_1 - sum_g_children, which must be <= p_1 (since x is the number of people in root's p_1 who are in good mood). So, for the root, this check is part of the general condition.

So, this approach should handle all cases.

Let's test this logic with the sample input.

First sample input:

Test case 1:

7 4

p = [1,0,1,1,0,1,0]

h = [4,0,0,-1,0,-1,0]

Tree structure:

1 is root.

Children of 1: 2,3,4.

Children of 3:5,6,7.

So, the s_u for each node:

s_1 is sum(p_1..p_7) = 1+0+1+1+0+1+0 =4.

s_2 is 0.

s_3: sum of p_3,5,6,7: 1+0+1+0=2.

s_4: 1.

s_5:0.

s_6:1.

s_7:0.

Now, compute g_u:

For node 1:

g_1 = (4 +4)/2 =4.

Check: 4 is between 0 and 4: yes.

sum_g_children (sum of 2,3,4's g):

For node 2:

h_2 is 0, s_2 is 0. So (0+0)/2=0. Check 0 <=0 <=0: yes. sum_g_children is 0 (no children). Check 0 <=0 <=0+0: 0 is 0, so ok.

node3: h_3 is 0, s_3 is 2. g= (0+2)/2=1. sum_g_children: sum of 5,6,7's g.

node5: h_5 is0, s_5 is0. g=0. sum_children is 0. check 0<=0 <=0+0: yes.

node6: h_6 is-1, s_6=1. ( -1 +1 )/2 =0. check 0 is between 0 and 1: yes. sum_children is 0. check 0 <=0 <=0+1 (yes). sum_children is 0, so x=0. 0 <=0 <=1: yes.

node7: h_7=0, s=0. g=0. check ok.

So, for node3: sum_g_children is 0 (nodes5,6,7) sum is 0+0+0=0. So sum_g_children=0. Check sum_g_children <= g_3 (1) <= sum_g_children + p_3 (1). 0 <=1 <=0+1 (1<=1). So yes. x=1-0=1. p_3 is 1. So x=1 is allowed (<=1).

node4: h_4=-1, s_4=1. g= ( -1 +1 )/2=0. sum_children: 0 (no children). check 0 <=0 <=0+1 (yes). x=0. p_4 is1. So x can be 0, which is allowed.

So node1's sum_g_children is sum of g_2 (0) + g_3 (1) +g_4 (0) =1. sum_g_children=1. Check 1 <=4 <=1+1 (4 is not <=2). So this would fail?

Wait, but wait. For node1, sum_g_children is 0 (node2) +1 (node3) +0 (node4) =1. Then x = g_1 - sum_g_children =4-1=3. p_1 is1. So x must be <=p_1 (1), but 3>1. So this condition would fail, but according to the sample input, the answer is YES.

Hmm, this suggests that the logic is incorrect.

Wait, in the first sample input, the answer is YES. But according to our logic, node1's sum_g_children is 1, and x =4-1=3. But p_1 is1. So 3>1. So the condition 0<= x <=p_1 would fail, leading to a NO. But the sample's answer is YES.

This indicates that there's a flaw in the logic.

So, what's wrong here?

Let me re-examine the conditions.

The condition for each node u is:

sum_g_children <= g_u <= sum_g_children + p_u.

In the case of node1 in the first sample:

sum_g_children is 0 (node2's g) +1 (node3's g) +0 (node4's g) =1.

g_u is4.

sum_g_children + p_u is1+1=2.

But 4 is not <=2. So the condition is violated, which would mean the answer is NO. But the sample answer is YES.

Thus, the current approach is flawed. So, what's wrong?

Ah, wait. The sum_g_children is the sum of the children's g's. But the children's g's are not the sum of their own children's g's. For example, node3's g is1, which is sum of its children's g (0+0+0) plus x=1 (from p_3). So sum_g_children for node3 is 0, x=1. So sum_g_children (for node3) is 0, which is added to x=1 (p_3) to get g_3=1.

But for node1, the sum_g_children is the sum of the g's of its children (nodes2,3,4). node3's g is1, which already includes x=1. So, when processing node1, sum_g_children is sum of 0 (node2's g) +1 (node3's g) +0 (node4's g) =1.

Then x for node1 is g_u - sum_g_children =4-1=3. But p_1 is1. So x=3>1. So the condition sum_g_children <= g_u <= sum_g_children + p_u (1<=4<=2) is violated.

But according to the sample, the answer is YES. So the logic must be incorrect.

This suggests that the approach is missing something. What's the mistake?

Let's think again about what x represents. For node u, x is the number of people in u's p_u that contribute to g_u. But also, all people in u's p_u must contribute to g_u. How?

Wait, no. The people in u's p_u are part of the subtree of u, so they pass through u. For each such person, their path is from 1 to u. So, their contribution to g_u depends on where they switched their mood.

For example, a person in u's p_u (u is their home) can switch on any edge along their path. If they switch on the edge between a and b (part of their path), then their contribution to u's g_u is -1 if u is in the path after b, which is impossible since u is their home. Wait, no. For example, if the person's home is u, which is in the path 1 → a → b → u. If the person switches on the edge a→b, then their path's cities are 1 (good), a (good), then on edge a→b, they switch. So in city a, they are good, but in city b and u, they are bad. So their contribution to u's h is -1.

So, for a person in u's p_u, their contribution to u's h can be +1 (if they didn't switch on any edge up to u) or -1 (if they switched on any edge in their path).

But the sum of all people in u's p_u is p_u, and their contribution is (number of good) - (number of bad) = (x) - (p_u -x) = 2x - p_u. This contributes to h_u.

But the total h_u also includes contributions from people in the subtrees of u's children. For example, people in node3's subtree (like node6) contribute to h_3 and also to h_1.

So, the initial approach has a mistake. The condition sum_g_children <= g_u <= sum_g_children + p_u is not sufficient. Because the sum_g_children is the sum of the g's of the children, which include their own contributions (including people in their p_v). But for the parent u, the sum_g_children represents the number of people in the subtrees of u's children who passed through u in good mood. But how does that relate to the u's own p_u people?

Wait, the sum_g_children for u is the sum of the g's of its children. Each of these g's represents the number of people in the child's subtree (including the child) who passed through the child's node in good mood. However, for these people to have passed through the child's node in good mood, they must have passed through u in good mood as well (since u is on the path to the child). So, the sum of the children's g's is the number of people in the subtrees of the children that passed through u in good mood.

But how does this relate to u's own g_u?

The g_u is the total number of people passing through u in good mood. This includes:

- The sum_g_children (all people in children's subtrees that passed through u in good mood).

- The people in u's own p_u that passed through u in good mood (i.e., those who did not switch before reaching u).

So, x is the number of people in u's p_u that did not switch before reaching u. Then, g_u = sum_g_children + x.

But x can be at most p_u (since there are p_u people in u's p_u).

So, sum_g_children + x = g_u.

But x must be between 0 and p_u.

So, the condition should be:

sum_g_children <= g_u <= sum_g_children + p_u.

Which is what the initial approach says.

But in the first sample, for node1:

sum_g_children =0 (node2) +1 (node3) +0 (node4) =1.

g_u is4.

So x =4-1=3. But p_1 is1. So 3>1, which violates the condition. So according to this logic, the answer should be NO. But the sample says YES.

This implies that the logic is incorrect. So where is the mistake?

Let me re-examine the first sample.

In the first sample:

The node1 has g_1=4.

sum_g_children for node1 is sum of children's g's: node2 (g=0), node3 (g=1), node4 (g=0). Sum is 1.

So x =4-1=3. But p_1 is1. So x is3, which is larger than p_1 (1). But according to the problem's sample, this is possible.

This suggests that our logic is missing something. So what's wrong?

Ah! Wait, the x represents the number of people in u's p_u that are in good mood when passing through u. But the people in u's p_u are part of the subtree of u. So, for the root node (u=1), which is their home, their path is just the root. So their contribution to the root's g_1 is +1 if they did not switch anywhere, or -1 if they switched on some edge in their path (but there are no edges before u for the root node, since it's the capital). Wait, the root node (u=1) is their home. So their path is just node1. So they can't switch on any edge. Because there's no edges to switch on. They are already in the capital, so their path is just the capital. So, for the people in p_1, they must be in good mood when passing through node1 (since they can't switch anywhere). So, x must equal p_1. So for the root node, x is p_1, and sum_g_children + p_1 = g_1.

But in the first sample, node1's g_1 is4. sum_g_children is1, p_1 is1. So 1+1=2. But g_1 is4. So this would imply that x=3, which is impossible. So this is a contradiction.

But according to the sample explanation, this case is possible. Let's look at the sample explanation:

Sample1 Test case1:

The person from city1 is in good mood. So contributes +1 to h_1.

The person from city4: visited 1 and4. His mood was ruined between 1 and4. So, in city1, he contributes +1 (good), in city4, -1 (bad). So for h_1, this person contributes +1.

Person from city3: good, passes through 1 and3. Contributes +1 to each.

Person from city6: ruined between1 and3. So contributes +1 to city1 (good), but -1 to 3 and6.

So, total h_1 is:

Person1: +1 (city1).

Person4: +1 (city1).

Person3: +1 (city1).

Person6: +1 (city1).

So total h_1=4. Which matches.

So, for the root node, the sum_g_children is1 (node3's g=1, node2 and4's g=0). But according to our logic, sum_g_children + x = g_1 →1 +x=4 →x=3. But p_1 is1. So how can x be3 when there's only1 person in p_1?

Ah! This indicates that the initial approach is incorrect. The mistake is in how we model the sum_g_children and x. Because, in this case, the sum_g_children includes the people from node3's subtree who passed through node3 in good mood. But those people's paths include node1. So, their contribution to node1's g_1 is +1 (they were in good mood when passing through node1). So, node3's sum of g_v (which is1) represents the number of people in node3's subtree that passed through node3 in good mood. But these people also passed through node1 in good mood, contributing to node1's g_1. 

But according to the logic, sum_g_children for node1 is sum of g_2, g_3, g_4. So, for node3, g_3 is1. Which represents the number of people in node3's subtree passing through node3 in good mood. These people also passed through node1 in good mood. So, their contribution to node1's g_1 is the same as their contribution to node3's g_3. 

Wait, but in our initial model, the sum_g_children is the sum of the g's of the children, which includes all people in the children's subtrees that passed through their respective child nodes in good mood. But these people must have also passed through the parent (u) in good mood, so their contribution to u's g_u is already accounted for in the sum_g_children.

But according to the logic, for node1, sum_g_children is the sum of the children's g's. So, node3's g_3=1 implies that there are 1 people in node3's subtree that passed through node3 in good mood. These people also passed through node1 in good mood. So, their contribution to node1's g_1 is 1. So, in node1's g_1=4, these 1 people from node3's subtree contribute 1, and the remaining 3 must come from node1's own p_1 and the other children's g's.

But node1's p_1 is1. So, this is impossible. 

But according to the sample, this is possible. So where's the flaw?

Ah, perhaps the model is incorrect. Because the sum_g_children for node u is the sum of the g's of its children, but each child's g is the number of people in their subtree that passed through them in good mood. However, these people's paths include u (since the child is in u's subtree). So, each of these people's contribution to u's g_u is +1, but they are counted in the child's g.

But in the current model, sum_g_children is added to x (the people in u's p_u) to get g_u. But sum_g_children already includes people who passed through u in good mood. So, their contribution to u's g_u is already part of sum_g_children. Thus, the model is correct. 

But in the sample, for node1, sum_g_children is1 (from node3's g=1) and x=3. But node1's p_1 is1. So x can't be3. 

This suggests that the model is incorrect, and that there's a different way to model the problem.

Alternative approach: For each node u, the g_u represents the number of people in the subtree of u that passed through u in good mood. But since u's parent is part of the path, these people must have passed through the parent in good mood as well. So, for the parent p of u, the g_p must be at least g_u plus the number of people in u's subtree that passed through u in good mood. Because those people must have passed through p in good mood.

Wait, perhaps the correct condition is that for each node u (excluding the root), g_u <= g_p. Because any person who passed through u in good mood must also have passed through the parent p in good mood. So, the number of people in u's subtree that passed through u in good mood (g_u) cannot exceed the number of people in p's subtree that passed through p in good mood (g_p). Because those people in u's subtree are part of p's subtree.

In the first sample:

For node3, g_3=1. For node1, g_1=4. 1 <=4, which holds.

For node6, g_6=0. Its parent is node3. g_3=1. 0 <=1, holds.

For node4, g_4=0. parent is node1. 0<=4, holds.

So, for all nodes except the root, their g_u is <= g_p.

But the root has no parent, so no constraint here.

But how does this help in the conditions?

Also, for node1's own p_1 people, their contribution to g_1 is +1. So, for the sample's node1, the p_1 is1. So, one person in node1's p_1 contributes +1 to g_1.

But according to the initial model, the sum_g_children for node1 is1 (from node3's g=1), and x=3 (which would require 3 people from p_1). But p_1 is1. So this is impossible.

But according to the sample, it's possible. So the model must be incorrect.

Alternative idea: Maybe the sum_g_children is not the correct way to model the contribution of the children's subtrees. Perhaps the model should instead require that the sum of the g's of the children plus x (people in u's p_u) equals g_u.

But sum_g_children here is the sum of the children's g's, which is the number of people in the children's subtrees that passed through them in good mood. But each of these people must also have passed through u in good mood. So, their contribution to u's g_u is already part of their own contribution. So, the sum of the children's g's represents the number of people in the children's subtrees that passed through u in good mood (since they passed through the children in good mood, which implies passing through u in good mood). Thus, the total g_u should be the sum of the children's g's plus the number of people in u's p_u that passed through u in good mood (x). So, sum_g_children +x = g_u.

But x must be <= p_u.

Thus, the conditions are:

sum_g_children +x = g_u.

x <= p_u.

x >=0.

But how to compute x? 

But x is g_u - sum_g_children. So, this must be >=0 and <=p_u.

So, the condition is:

0 <= g_u - sum_g_children <= p_u.

Which is the same as sum_g_children <= g_u <= sum_g_children + p_u.

But in the sample, this condition is violated for the root node. So why is the sample's answer YES?

This suggests that the initial approach is incorrect and that there's a different way to model the problem.

Perhaps the mistake is that the sum_g_children is not the sum of the children's g's, but something else. 

Wait, let's consider the root node (u=1). The sum_g_children is sum of the g's of its children. Each child's g is the number of people in its subtree that passed through the child in good mood. 

But for each child v of u, the people in v's subtree who passed through v in good mood must have also passed through u in good mood. So, their contribution to u's g_u is equal to the number of such people. So, the sum of the g's of the children is exactly the number of people in the children's subtrees that passed through u in good mood.

So, the sum_g_children for u is the number of people in the children's subtrees that passed through u in good mood. 

Additionally, the people in u's own p_u that passed through u in good mood (x) contribute x to g_u.

Thus, g_u = sum_g_children + x.

But x can't exceed p_u.

But in the sample's root node:

g_u is4, sum_g_children is1 (from node3's g=1, node2's g=0, node4's g=0).

x=4-1=3. But p_u=1. So x=3>1. This suggests it's impossible. But the sample says it's possible.

This indicates a contradiction. So where's the mistake?

Wait, perhaps the initial step of computing s_u is incorrect. Let's recompute s_u for the sample.

Sample1 test case1:

n=7, m=4.

p array:1,0,1,1,0,1,0.

So, p_1=1, p_3=1, p_4=1, p_6=1. Other zeros.

Tree structure:

1 is connected to 2,3,4.

3 is connected to 5,6,7.

So, the subtree of 1 includes all nodes.

s_1=1+0+1+1+0+1+0=4.

s_2=0.

s_3: nodes3,5,6,7. p=1+0+1+0=2.

s_4=1.

s_5=0.

s_6=1.

s_7=0.

So s_u values are correct.

g_u for node1: (4 +4)/2=4.

sum_g_children for node1: sum of g_2, g_3, g_4.

g_2: h_2=0. (0+0)/2=0.

g_3: (0+2)/2=1.

g_4: (-1+1)/2=0.

sum_g_children=0+1+0=1.

x=4-1=3.

But p_1=1. x can't be3. 

So according to the model, this is impossible. But the sample says it's possible.

This suggests that the model is incorrect. 

So what's the error here?

Let me look at the people in the sample:

In the sample's first test case:

- Person from city1: in good mood, contributes +1 to city1.

- Person from city3: in good mood, passes through city1 and3. Contributes +1 to both.

- Person from city4: in good mood until after city1, then bad. Contributes +1 to city1, -1 to city4.

- Person from city6: in good mood until after city1, then bad. Contributes +1 to city1, -1 to city3 and city6.

So, the contributions to city1:

Each of the four people contributes +1 (1 from city1's person, 1 from city3's person, 1 from city4's person, 1 from city6's person). So total h_1=4.

But according to the model, the sum_g_children for node1 is1 (from node3's g=1, node2's g=0, node4's g=0). So sum_g_children=1. x=4-1=3. But node1's p_1=1. So how is this possible?

The answer is that the model is missing the contributions from the people in the children's subtrees who passed through the root node in good mood but did not contribute to the children's g's.

For example, the person from city4. Their home is city4. They switched on the edge between 1 and4. So, their path is 1→4. They contribute +1 to city1 (good), and -1 to city4 (bad). For city4's g_4: this person contributes -1. So g_4 is (h_4 + s_4)/2 = (-1 +1)/2=0. So g_4=0. 

But this person's contribution to city1's g_1 is +1. They are part of the sum_g_children of city1's child (node4), but their contribution to node4's g is not counted in node4's g_4. Because in node4, their contribution is -1.

So, sum_g_children for node1 includes node4's g_4=0. So, this person's contribution to sum_g_children for node1 is 0.

But their contribution to node1's g_1 is +1. So, how is this accounted for in the model?

Ah! The model is incorrect. Because the sum_g_children is the sum of the children's g's, but this sum only includes people who contributed +1 to the child's g. However, there are people in the children's subtrees who contribute +1 to the parent's g but contribute -1 to the child's g. Thus, their contribution to the parent's g is not captured by the child's g.

So, the initial model is wrong. Because sum_g_children is the sum of the children's g's, but the people in the children's subtrees who contribute to the parent's g are not the same as those who contribute to the children's g. 

This means that the condition sum_g_children +x =g_u is incorrect.

This is the crux of the problem.

Thus, the model must be revised. 

Alternative approach:

Each person's path is from the root to their home. For each person, their decision of where to switch (or not) determines the cities that get +1 and -1.

For a person in city u's subtree, their contribution to the parent's g is +1 if they passed through the parent in good mood, which depends on where they switched.

So, the sum of g's for the children is not sufficient to model the contributions to the parent's g.

Thus, the model must be re-examined.

Alternative idea:

For each node u, the number of people in the subtree of u that passed through u in good mood is g_u. 

But to compute this, we must consider:

- The people in u's own p_u who passed through u in good mood.

- The people in the subtrees of u's children who passed through u in good mood (which is the sum of the g's of the children, since passing through a child in good mood requires passing through u in good mood).

Thus, g_u = sum of children's g + x, where x is the number of people in u's p_u that passed through u in good mood.

But x can be between 0 and p_u.

So, the condition is sum_children_g <= g_u <= sum_children_g + p_u.

But the sample's case shows that this model is not sufficient.

But in the sample, for node1:

sum_children_g =1 (from node3's g=1).

x=3 (g_u - sum_children_g=4-1=3).

But p_1=1. So x=3 is impossible.

But according to the sample, the answer is YES. So, this suggests that the model is incorrect.

So, what's the correct way to model this?

Let me think again. The root's g_u is the number of people passing through the root in good mood.

In the sample, the root's g_u=4. This includes:

- The person from city1 (p_1=1), who contributes +1.

- The person from city3 (part of the sum_children_g=1 from node3's g=1). This person's path is root →3, and they passed through 3 in good mood. So they also passed through root in good mood.

- The person from city4's p_4=1. Their contribution to root's g_u is +1. Because they passed through root in good mood (switched on edge root→4). So, in root, they are in good mood.

- The person from city6's p_6=1. They passed through root in good mood (switched on edge root→3).

So, the root's g_u=4 is correct.

But according to the model, sum_children_g=1 (sum of node3's g=1, node2 and4's g=0). So x=4-1=3. But p_1=1. So where are the other 2 people coming from?

Ah, this is the mistake. The model assumes that x is the number of people in u's p_u that passed through u in good mood. But in reality, x can also include people from the children's subtrees. Wait, no. x is the number of people in u's own p_u who passed through u in good mood. 

But the sample's root has x=3, which exceeds p_1=1. So this is impossible. But according to the sample, it's possible. So the model is wrong.

Alternative approach: Perhaps the sum_children_g is not the sum of the children's g, but something else. Let's think differently.

For each node u, after processing its children, we can compute how many people in the subtree of u (excluding u's own p_u) passed through u in good mood. Then, add the people in u's own p_u that passed through u in good mood.

But how to compute this?

Perhaps the key is to realize that for each node u, the g_u should be equal to the sum of the people in the subtree of u (including u) that passed through u in good mood. This includes:

- All people in the children's subtrees that passed through u in good mood. For each child v of u, this is equal to the number of people in v's subtree that passed through v in good mood (g_v), because to pass through v in good mood, they must have passed through u in good mood.

- The people in u's own p_u that passed through u in good mood (x).

So, g_u = sum_g_children + x.

But x is between 0 and p_u.

This seems to be the same as the initial model. But in the sample, it's not holding.

But according to the sample, the root's g_u is4, sum_g_children=1 (node3's g=1), and x=3. But p_u=1. So x can't be3.

This suggests that the model is incorrect, but the sample is valid. So, the model must be wrong.

Alternative idea: Perhaps the sum_g_children is not the sum of the children's g's, but the sum of the number of people in the children's subtrees that passed through u in good mood. 

But how to compute that? For example, the people in child v's subtree that passed through v in good mood (g_v) must have passed through u in good mood. So, their contribution to u's g_u is g_v. 

So, the sum of the children's g's is indeed the number of people in their subtrees that passed through u in good mood. 

But then, in the sample, node3's g_3=1. Which represents one person in node3's subtree that passed through node3 in good mood. This person must have also passed through node1 (u's parent) in good mood, contributing to node1's g_u.

So, for node1's g_u=4, sum_g_children=1 (from node3's g=1, node2's g=0, node4's g=0), and x=3. So x=3, but p_u=1. This is impossible. But the sample allows it. 

Thus, the model must be incorrect. 

But what's the correct model?

Let's think of the problem in terms of the constraints.

For each node u, the following must hold:

1. (h_u + s_u) must be even.

2. 0 <= (h_u + s_u)/2 <= s_u.

3. For all children v of u, g_v <= g_u.

4. sum(g_v for v children of u) + x = g_u, where x is the number of people in u's p_u that passed through u in good mood. 0<=x<=p_u.

But in the sample, node1's g_u=4, sum(g_children)=1, x=3. But p_u=1. So x=3 is impossible. So according to this, the answer should be NO, but the sample says YES. So this suggests that one of the constraints is missing.

Ah! Wait, perhaps the people in the children's subtrees that are in the parent's subtree contribute to the parent's g_u even if their contribution to the child's g_v is zero. For example, a person in child v's subtree who switched on the edge between u and v. So, in v's g_v, this person contributes -1 (since they passed through v in bad mood). But in u's g_u, they contribute +1 (since they passed through u in good mood). 

But this is the crux of the problem. The initial model does not account for these people. Because the sum of the children's g_v is the number of people in their subtree that passed through v in good mood. But the people who passed through u in good mood but passed through v in bad mood are not counted in sum_g_children. However, they are part of u's g_u.

This means that the initial model is missing these contributions. So, the sum_g_children is not sufficient to model all the people in the children's subtrees that passed through u in good mood.

Thus, the model is incorrect. 

So, the correct approach must account for people in the children's subtrees who passed through u in good mood but did not pass through the child v in good mood.

This complicates the model, as it's no longer possible to compute sum_g_children simply by summing the children's g_v.

Thus, the initial approach is invalid, and a different approach is needed.

Alternative approach:

Each person's contribution to the nodes in their path is determined by the edge on which they switch. For example, a person from city u can switch on any edge in their path. 

For each node v in the path from 1 to u, if the person switches on an edge after v, then v's h_v is increased by 1. If the person switches on an edge before or at v, then v's h_v is decreased by 1.

But this seems difficult to model for all people.

Alternative idea:

The total number of people passing through a node u in good mood is equal to the number of people in the subtree of u who have not switched their mood on any edge along their path up to u. 

This is because a person in the subtree of u who switches on an edge after u will pass through u in good mood, contributing +1 to h_u. If they switch on or before u, they contribute -1.

Thus, for a node u, the number of people passing through u in good mood is equal to the number of people in the subtree of u who switched on an edge after u. 

Similarly, the number of people passing through u in bad mood is those who switched on or before u.

Thus, the total for h_u is (number of people in subtree u who switched after u) - (number of people in subtree u who switched on or before u).

But the sum of these two terms is s_u. So:

h_u = (after_u) - (before_u) = (after_u) - (s_u - after_u) = 2 * after_u - s_u.

Thus, after_u = (h_u + s_u) / 2.

Which is the same as the initial approach's g_u.

But after_u is the number of people in the subtree of u who switched after u. 

Thus, the key is to ensure that for each node u, after_u = (h_u + s_u)/2 must be an integer between 0 and s_u.

Furthermore, for the tree hierarchy, the number of people switching after u (after_u) must be at least the sum of after_v for all children v of u. Because any person in the subtree of v (a child of u) who switched after v is also in the subtree of u and switched after u. Because the edge from u to v is part of their path, so switching after v implies switching after u.

Wait, no. If a person is in the subtree of v (child of u), and they switch on an edge after v (e.g., in the edge between v and a child of v), then they are considered to have switched after v, which is part of u's subtree. But switching after v implies that their path passes through u, v, and then the switch edge. So, they switched after u (since the edge is after u). So, after_u includes all after_v for children v of u, plus any people in u's subtree who switched after u but not in the children's subtrees (i.e., the people in u's own p_u who switched after u).

So, for each node u:

after_u = sum_after_children + x,

where x is the number of people in u's own p_u who switched after u.

But x can be between 0 and p_u.

Thus, after_u must be >= sum_after_children, and after_u - sum_after_children <= p_u.

These are the same constraints as the initial model, but with after_u instead of g_u.

But in the initial model, g_u is after_u.

Thus, the initial model is correct. But how to reconcile this with the sample?

In the sample's root node:

after_u =4. sum_after_children is sum of after_v for children of root. 

The children of root are 2,3,4.

For node2, after_v=0 (since s_v=0). 

For node3: after_v= (h_3 + s_3)/2 = (0+2)/2=1.

For node4: after_v=( -1+1 )/2=0.

 sum_after_children =0+1+0=1.

x= after_u - sum_after_children =4-1=3.

But x is the number of people in root's p_u (1) who switched after root. 

But switching after root is impossible because the root is the home city. So, for a person in root's p_u, their path is only the root. They can't switch after the root. So, x can be either 0 or 1 (p_u=1), but in this case x must be1 (since they can't switch after root, so after_u for root is sum_after_children +x=1+1=2. But according to the sample, after_u for root is4. So this is impossible. 

But the sample says it's possible. So where's the mistake?

Ah! The key insight here is that the after_u for a node u is the number of people in the subtree of u who switched after u. For the root node u=1, the people in the subtree of u (all people) can switch after u, which is impossible because there are no edges after u. Thus, after_u for the root must equal the number of people in the subtree of u (all people) who did not switch at all. Which is the number of people in the entire tree who never switched, because the root's subtree includes all people.

But according to the sample, the after_u for the root is4 (since h_u=4, s_u=4, after_u= (4+4)/2=4). So all four people did not switch anywhere. But according to the sample explanation, some people did switch.

This is a contradiction. 

Thus, the initial model is incorrect. 

This suggests that there's a fundamental misunderstanding of the problem. 

Rewriting the problem:

For each person, their path is from the root (1) to their home city (u). They can switch their mood on any edge in this path. Once they switch, all subsequent cities in their path are considered in bad mood.

For each city v, the happiness index h_v is equal to the number of people who passed through v in good mood minus those who passed through v in bad mood.

The question is whether there exists a way to assign switch edges for each person so that the sum for each city v equals the given h_v.

Alternative approach:

For each city v, the number of people who passed through v in good mood is g_v, and in bad mood is b_v. So, h_v =g_v -b_v. Also, s_v =g_v + b_v, since all people in the subtree of v pass through v.

So, g_v = (h_v + s_v)/2, and b_v = (s_v -h_v)/2.

The conditions are:

1. h_v + s_v must be even.

2. g_v >=0 and <=s_v.

3. For each node v (except root), the number of people in the subtree of v who passed through v in good mood (g_v) must be <= the number of people in the subtree of v's parent who passed through parent in good mood (g_parent).

This is because a person who passes through v in good mood must have passed through parent(v) in good mood.

So, for each node v, g_v <= g_parent.

Additionally, the sum of g_v for all children of parent(v) plus x (people in parent(v)'s p) must equal g_parent.

But this requires more thought.

For example, the root's g_root is the number of people in the entire tree who passed through root in good mood. This includes all people in the tree who did not switch on any edge (since they passed through all nodes in good mood) and those who switched on edges after the root (but there are no edges after the root). So, root's g_root must be the number of people who never switched.

But for a person in the root's p_root, they can't switch anywhere (their path is only root), so they must be in good mood. So, x (people in p_root's own p who passed through root in good mood) must be equal to p_root.

Thus, for the root node, x = p_root. So, sum_g_children + p_root = g_root.

So, in the sample's root node, sum_g_children is1, p_root is1. Thus, 1+1=2, but g_root is4. This is impossible.

Thus, according to this model, the sample's answer should be NO, but it's YES. So the model is incorrect.

This suggests that the initial approach is fundamentally flawed, and that there's a different way to model the problem.

After some research and thinking, I realize that the mistake in the initial approach is that it does not account for the people in the children's subtrees who passed through the parent in good mood but not through the child in good mood. These people's contributions to the parent's g_u are not captured in the sum of the children's g_v. Hence, the sum_g_children is not the correct way to model the parent's g_u.

The correct approach is to realize that for each node u, the g_u is the number of people in the entire subtree of u who passed through u in good mood. This includes:

- People in u's own p_u who did not switch on any edge before u.

- People in the subtrees of u's children who passed through u in good mood.

But a person in a child's subtree can pass through u in good mood even if they switched after u. For example, a person in child v's subtree who switched on an edge after u but before v will pass through u in good mood but v in bad mood. Thus, their contribution to u's g_u is +1, but they are not counted in v's g_v.

Thus, the sum_g_children (sum of children's g_v) is the number of people in the children's subtrees who passed through the children in good mood. But there are additional people in the children's subtrees who passed through u in good mood but not through the child in good mood. These people contribute to u's g_u but are not counted in the children's g_v.

This means that the initial model's condition is not sufficient. 

Thus, the correct approach must account for all people in the subtree of u who passed through u in good mood. This includes:

- For each child v of u, the number of people in v's subtree who passed through u in good mood. This is equal to the number of people in v's subtree who passed through v's parent (u) in good mood, which is g_v plus the number of people in v's subtree who passed through u in good mood but not through v in good mood.

But this seems difficult to model.

Alternative approach inspired by the correct solution:

The key is to realize that for each node u, the following must hold:

g_u = (h_u + s_u) / 2.

Additionally, for each node u (excluding the root), g_u <= g_parent(u).

Also, for the root, g_root must equal the sum of g_root's children's g_children plus p_root.

But this is not the case in the sample.

Alternatively, for each node u:

sum of g_v for all children v of u <= g_u - p_u <= sum of g_v for all children v of u.

But this doesn't make sense.

After struggling with this for hours, I think I need to refer to the correct solution approach.

The correct approach is:

For each node u:

1. Check if (h_u + s_u) is even and non-negative, and that 0 <= (h_u + s_u)/2 <= s_u.

2. For each node u (not root), check that the g_u <= g_parent.

3. Additionally, for each node u, check that g_u + s_u >= g_parent.

This condition comes from the fact that the number of people in u's subtree who passed through u in good mood (g_u) plus the number who passed through u in bad mood (s_u - g_u) must equal s_u. But this is always true.

But this doesn't directly help.

The correct solution is to ensure that for each node u, the following conditions hold:

1. (h_u + s_u) is even and 0 <= g_u <= s_u.

2. For each node u (not root), g_u <= g_parent.

3. For each node u, g_u >= sum of g_v for all children v of u.

Wait, no. Because the sum of g_v for children v of u is the number of people in their subtrees who passed through v in good mood, which requires passing through u in good mood. So, the sum of g_v for children v of u must be <= g_u.

Thus, the conditions are:

- For each node u, sum of g_v for children v of u <= g_u.

- For each node u (not root), g_u <= g_parent.

So, in the first sample:

For node1:

sum of g_v for children (0+1+0)=1 <= g_u=4: yes.

For node3:

sum of g_v for children (0+0+0)=0 <= g_u=1: yes.

For node6:

sum of g_v for children (0) <=0: yes.

For node4:

sum of g_v for children (0) <=0: yes.

For node2:

sum of g_v for children (0) <=0: yes.

For node5:

sum of g_v for children (0) <=0: yes.

For node7:

sum of g_v for children (0) <=0: yes.

All nodes except the root have g_u <= g_parent:

- node2:0 <=4: yes.

- node3:1 <=4: yes.

- node4:0 <=4: yes.

- node5:0 <=1: yes.

- node6:0 <=1: yes.

- node7:0 <=0: yes.

Thus, all conditions are satisfied. So the answer is YES.

Thus, the initial model's condition of sum_g_children <= g_u is correct, but the other condition (g_u <= sum_g_children + p_u) is not required. 

So the correct conditions are:

For each test case:

1. For each node u, check that (h_u + s_u) is even and that 0 <= (h_u + s_u)/2 <= s_u.

2. For each node u (except root), check that g_u <= g_parent.

3. For each node u, check that sum of g_v for children v of u <= g_u.

Thus, the initial model's condition sum_g_children <= g_u <= sum_g_children + p_u is incorrect.

The correct conditions are:

- sum_g_children <= g_u.

- For non-root nodes, g_u <= g_parent.

- For the root node, no g_parent, but sum_g_children <= g_u <= sum_g_children + p_root.

Because for the root node, the people in the root's own p_root can contribute up to p_root to g_root.

But in the sample's root node, sum_g_children is1, and g_root is4. sum_g_children + p_root =1+1=2 <4. So the condition sum_g_children <= g_u <= sum_g_children + p_root is violated.

But according to the sample's correct answer, this is allowed. So this indicates that the root's condition is sum_g_children <= g_u and g_u <= sum_g_children + p_u.

But in the sample, this is not satisfied.

Thus, this suggests that the root's condition is different.

Wait, for the root node:

The people in the root's p_1 can contribute to the root's g_1. For each such person, their path is only the root. They can't switch on any edge, so they must be in good mood. So x (the number of people in p_1 contributing to g_1) is exactly p_1.

Thus, for the root node:

g_1 = sum_g_children + p_1.

If this is not the case, then it's impossible.

So, for the root node, the condition is:

sum_g_children + p_1 = g_1.

But in the sample:

sum_g_children (1) + p_1 (1) =2. But g_1=4.

This is not possible. But the sample's answer is YES.

Thus, this suggests that the root node's condition is not sum_g_children + p_1 =g_1.

So, the correct approach is to realize that the people in the root's p_1 can choose to switch or not. But since there are no edges in their path, they can't switch. So, all people in the root's p_1 must contribute +1 to the root's g_1. Thus, for the root node:

g_1 = sum_g_children + p_1.

But in the sample, sum_g_children is1, p_1 is1. So g_1=2. But the sample's g_1 is4.

This indicates that the initial approach is completely wrong.

So, what is the correct way to model the problem?

After more research, I find that the correct conditions are:

1. For each node u, (h_u + s_u) must be even, and 0 <= (h_u + s_u)/2 <= s_u.

2. For each node u (excluding root), the computed g_u must be <= g_parent.

3. For each node u, the computed g_u must be >= sum of the computed g_v for all children v of u.

4. Additionally, for the root node, the computed g_root must be equal to sum of the computed g_v for all children plus the p_root.

But in the sample's root node, this would require sum_g_children (1) + p_root (1) =2 =g_root. But g_root is4. So sample is invalid. But sample's answer is YES.

Thus, I'm missing something. The correct approach must have different conditions.

Another way to think about the problem is:

For each node u:

g_u = number of people in the subtree of u that passed through u in good mood.

This includes:

- All people in the children's subtrees who passed through u in good mood. For a person in child v's subtree to pass through u in good mood, they must not have switched on any edge before u.

So, for each child v of u, the number of people in v's subtree who passed through u in good mood is g_v (since passing through v in good mood implies passing through u in good mood).

But there are also people in v's subtree who passed through u in good mood but switched after u but before v. These people are counted in u's g_u but not in v's g_v.

Thus, the initial model's sum_g_children is missing these people.

Thus, the correct way to model g_u is:

g_u = sum_g_children + x, where x is the number of people in u's own p_u that passed through u in good mood (x can be between 0 and p_u).

But the sample's root node has sum_g_children=1, x=3, which exceeds p_u=1. So the sample must be invalid. But it's valid.

This indicates that the model is incorrect.

After hours of struggling, I think the correct approach is:

Each person contributes to all cities along their path up to the edge where they switched. For a person who switches on edge (u, v), then all cities from the root to u (inclusive) are passed in good mood, and cities from v onwards are passed in bad mood.

Thus, for each city w along the path to the home city:

- If w is on the path from root to u, then the person contributes +1 to h_w.

- If w is on the path from v to home, then contributes -1.

Thus, the total contribution for a person is the sum of +1 for the cities up to u and -1 for the cities from v onwards.

But the problem requires that for each city, the sum of these contributions equals h_i.

The key insight is that for each city u, the number of people who passed through u in good mood is (g_u) and in bad mood is (s_u - g_u). Thus, h_u = g_u - (s_u - g_u) = 2g_u - s_u.

This gives us the first condition: (h_u + s_u) must be even and 0 <= g_u <= s_u.

Additionally, for each node u (excluding root), the number of people in its subtree who passed through u in good mood (g_u) cannot exceed the number of people in its parent's subtree who passed through parent(u) in good mood (g_parent). Because to pass through u in good mood, they must have passed through parent(u) in good mood.

Thus, for each non-root node, g_u <= g_parent.

Finally, for each node u, the sum of g_v for all children v of u must be <= g_u. Because the children's g_v represents the number of people in their subtrees that passed through v (and hence u) in good mood. The remaining people in u's subtree (including u's own p_u) can be those who passed through u in good mood but did not pass through any child in good mood.

Thus, the conditions are:

1. For each node u:

   a. (h_u + s_u) is even.

   b. 0 <= g_u = (h_u + s_u)/2 <= s_u.

2. For each node u (non-root):

   a. g_u <= g_parent.

3. For each node u:

   a. sum(g_v for children v of u) <= g_u.

If all these conditions are met, then the answer is YES.

In the sample, these conditions are met:

For the root node:

sum(g_children) =0+1+0=1 <=4 (g_u=4). 

For non-root nodes:

node3's g=1 <=4 (parent's g=4).

node6's g=0 <=1 (parent's g=1).

node4's g=0 <=4 (parent's g=4).

etc.

Thus, all conditions are satisfied, so the answer is YES.

Thus, the correct model is to check these three conditions.

Thus, the correct approach is:

- Compute s_u for each node.

- Check condition 1 for each node.

- Check condition 2 for non-root nodes.

- Check condition 3 for each node.

This explains why the sample is possible despite the initial model's condition on the root node's sum_g_children + p_u.

Thus, the initial model's conditions were incorrect. The correct conditions are the three mentioned above.

Thus, the correct code is to:

- For each test case:

   a. Read the tree and build adjacency lists.

   b. Compute s_u for each node using DFS.

   c. Check condition 1 for each node. If any fails, output NO.

   d. For each node (processed in a way that parents are processed after children), check condition 3.

   e. For each non-root node, check condition 2.

   f. If all conditions are met, output YES; else, NO.

Thus, the code will be:

Implementing this requires:

- A way to compute s_u for each node via post-order traversal.

- Compute parent for each node.

- Check the three conditions.

Now, the code:

We need to read t test cases.

For each test case:

Read n and m.

Read p array (0-based or 1-based? The cities are numbered from 1 to n.)

Read h array.

Read n-1 edges and build adjacency list.

Then, build the tree rooted at 1. This requires a BFS or DFS to determine parent-child relationships.

Then compute s_u via post-order traversal.

Then, check for each node u:

1. (h_u + s_u) must be even.

2. 0 <= g_u <= s_u.

3. For non-root u, g_u <= g_parent.

4. For each u, sum of g_v for children <= g_u.

Thus, the code:

Implementing this.

Now, the code:

Read input.

For each test case:

n, m = map(int, input().split())

p = list(map(int, input().split()))

h = list(map(int, input().split()))

edges = [[] for _ in range(n+1)]

for _ in range(n-1):

   u, v = map(int, input().split())

   edges[u].append(v)

   edges[v].append(u)

Build the tree with root 1.

We'll perform a BFS or DFS to find parents and children.

Let's use BFS:

from collections import deque.

parent = [0]*(n+1)

children = [[] for _ in range(n+1)]

visited = [False]*(n+1)

q = deque([1])

visited[1] = True

while q:

   u = q.popleft()

   for v in edges[u]:

       if not visited[v]:

           visited[v] = True

           parent[v] = u

           children[u].append(v)

           q.append(v)

Now compute s_u via post-order traversal:

s = [0]*(n+1)

def post_order(u):

   s[u] = p[u-1]

   for v in children[u]:

       post_order(v)

       s[u] += s[v]

post_order(1)

Then, compute g for each node:

g = [0]*(n+1)

valid = True

for u in range(1, n+1):

   su = s[u]

   hu = h[u-1]

   if (hu + su) % 2 !=0:

       valid = False

       break

   gu = (hu + su) //2

   if gu <0 or gu > su:

       valid = False

       break

   g[u] = gu

if not valid:

   print("NO")

   continue

Now, check condition 2 and 3.

For condition 2: for each non-root u, g[u] <= g[parent[u]]

for u in range(2, n+1):

   if g[u] > g[parent[u]]:

       valid = False

       break

if not valid:

   print("NO")

   continue

For condition 3: for each u, sum of g[v] for children v <= g[u]

for u in range(1, n+1):

   total =0

   for v in children[u]:

       total += g[v]

   if total > g[u]:

       valid = False

       break

if not valid:

   print("NO")

else:

   print("YES")

This code should handle all conditions.

Testing the first sample:

Test case 1:

s = [0, 4, 0, 2, 1, 0, 1, 0]

g = [0,4,0,1,0,0,0,0]

Check condition 2:

For u=2: g=0 <= parent's g=4: yes.

u=3:1 <=4: yes.

u=4:0 <=4: yes.

u=5:0 <=1: yes.

u=6:0 <=1: yes.

u=7:0 <=0: yes.

Condition3:

For u=1: sum of children's g (0+1+0) =1 <=4: yes.

u=3: sum of children's g (0+0+0) =0 <=1: yes.

Others: sum is <= g[u].

Thus, valid.

Thus, sample output is YES.

Second sample:

Test case1:

4 4

p = [1,1,1,1]

h = [4,1,-3,-1]

s for each node:

s_1=4.

s_2=1.

s_3=1.

s_4=1.

g_1= (4 +4)/2=4.

g_2=(1+1)/2=1.

g_3= (-3 +1)/2= -1 → invalid. So code outputs NO.

Thus, the code correctly handles this.

Thus, this code should work.
</think>

```python
import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, m = int(input[ptr]), int(input[ptr+1])
        ptr +=2
        p = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        h = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        edges = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u = int(input[ptr])
            v = int(input[ptr+1])
            ptr +=2
            edges[u].append(v)
            edges[v].append(u)
        
        parent = [0]*(n+1)
        children = [[] for _ in range(n+1)]
        visited = [False]*(n+1)
        q = deque([1])
        visited[1] = True
        while q:
            u = q.popleft()
            for v in edges[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    children[u].append(v)
                    q.append(v)
        
        s = [0]*(n+1)
        def post_order(u):
            s[u] = p[u-1]
            for v in children[u]:
                post_order(v)
                s[u] += s[v]
        post_order(1)
        
        valid = True
        g = [0]*(n+1)
        for u in range(1, n+1):
            su = s[u]
            hu = h[u-1]
            if (hu + su) % 2 != 0:
                valid = False
                break
            gu = (hu + su) // 2
            if gu < 0 or gu > su:
                valid = False
                break
            g[u] = gu
        
        if not valid:
            print("NO")
            continue
        
        for u in range(2, n+1):
            if g[u] > g[parent[u]]:
                valid = False
                break
        if not valid:
            print("NO")
            continue
        
        for u in range(1, n+1):
            total = 0
            for v in children[u]:
                total += g[v]
            if total > g[u]:
                valid = False
                break
        print("YES" if valid else "NO")

if __name__ == "__main__":
    main()
```