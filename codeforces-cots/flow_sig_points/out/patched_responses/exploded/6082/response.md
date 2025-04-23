<think>
Okay, let's try to understand this problem. So, the problem is about apples rolling down a tree structure made of inflorescences. Each apple starts in its own inflorescence and rolls down every second. When two apples are in the same inflorescence at the same time, they annihilate each other in pairs. Arcady collects apples that reach the first inflorescence the moment they arrive. We need to calculate how many apples he collects.

Hmm. Let's break this down. Each apple from inflorescence i will take a certain amount of time to reach the first inflorescence. For example, if the path from i to 1 is i → p_i → p_p_i ... → 1, then the time taken is the number of steps in that path. Let's call this time 'depth' of the inflorescence i. So, for each apple, we can compute the time it takes to reach inflorescence 1. The key thing here is that apples that arrive at the same time to the first inflorescence will annihilate each other if there's an even count, or leave one if odd. But wait, the problem says that apples are collected the moment they arrive. So, all apples arriving at time t to the first inflorescence will be considered at once. The number of such apples that survive annihilation (i.e., count mod 2) determines how many are added to the total.

So, the approach is: compute for each inflorescence the time it takes for its apple to reach the root (inflorescence 1). Then, count how many apples arrive at the root at each time t. For each t, if the count is odd, add 1 to the total; if even, add 0. The initial apple in the root (inflorescence 1) is collected at time 0, so that's one apple. Then, other apples arrive at their respective times.

The main challenge is efficiently computing the depth (time) for each node, then counting the frequencies modulo 2.

Let's think about the steps:

1. For each inflorescence from 2 to n, compute the time it takes for the apple to reach 1. The time for i is the number of steps needed to reach 1. For example, if i's parent is p_i, then the depth of i is 1 + depth of p_i. But wait, because each step takes one second. So, the depth of i is the length of the path from i to 1. So for each i, the depth is the depth of its parent plus one. The root (1) has depth 0.

Wait, but the root's apple is collected immediately. So the time for the apple in 1 is 0. For i=2, if its parent is 1, then depth is 1. So the apple from 2 takes 1 second to reach 1. So, it arrives at t=1. The apple from 3 which has p3=2 would have a depth of 2 (1 step to 2, then 1 step to 1, total 2 steps).

So, the plan is to precompute the depth for each node. Then, for all nodes (including 1?), count the number of nodes with each depth. Wait, but node 1's apple is collected at t=0. But according to the problem statement, each inflorescence starts with exactly one apple. So the apple in 1 is collected at time 0. Then, all other apples roll down each second.

So the initial step is that apples are in their respective nodes. Then, all apples except those in 1 start moving. So the first movement happens in the first second. So for node i, the time to reach 1 is the depth of i. But node 1's time is 0.

So the steps:

- The initial apples in 1 is collected at time 0. That's +1.

- For each node i >=2, compute depth_i. The apple from i will arrive at the root after depth_i seconds. So, each such apple contributes to the count for time t=depth_i.

Then, the total apples collected is 1 (from the root) plus the sum over each t of (count[t] mod 2).

Wait, but the root's apple is collected once. So yes. So first, the answer starts at 1. Then, for all other nodes (i=2 to n), their contribution is to the time t equal to their depth. Then, for each t, if the number of apples arriving at t is odd, add 1; else 0.

So the steps to compute:

1. Compute the depth for each node (1's depth is 0, and others are computed based on their parent's depth +1).

But wait, node 1's depth is 0. Then, for node i=2, if p_i is 1, then depth is 1. For node i=3 with p_i=2, depth is 2, etc.

So how to compute the depth efficiently?

We can precompute the depth for each node using a memoization approach. Since each node's parent is less than the node (since pi < i), we can compute the depths in order from 2 to n. For each i, depth[i] = depth[p_i] + 1. So this is O(n) time.

Once we have all the depths, we need to count how many nodes have each depth. For example, in the first sample input:

Sample 1:

n=3, p2=1, p3=1.

Depths:

1: 0.

2: 1 (p2 is 1, so depth 0 +1 =1).

3: 1 (p3 is 1, depth 0 +1=1).

So for depth 1, count is 2 (nodes 2 and 3). So the apples arrive at time 1: 2 apples. 2 is even, so they annihilate. So the total is 1 (from root) + 0 =1.

Which matches the sample.

Sample 2:

n=5, p2=1, p3=2, p4=2, p5=2.

Depths:

1:0.

2:1 (p2 is 1, depth 0+1=1).

3:2 (p3=2, depth 1+1=2).

4:2 (p4=2, depth 1+1=2).

5:2 (p5=2, depth 1+1=2).

So the counts:

depth 0:1 (root).

depth 1:1 (node 2).

depth 2:3 (nodes 3,4,5).

So for each time:

Time 0: 1 (root) → contributes 1.

Time 1: node 2's apple arrives. count is 1 → odd → contribute 1.

Time 2: three apples → 3 mod 2 is 1 → contribute 1.

Total is 1 + 1 + 1 =3.

Which matches sample 2.

So the approach is correct.

Now, how to implement this efficiently.

First, compute the depth array. For each node from 2 to n, we can compute depth[i] as depth[p_i] +1. Since p_i <i, the parents are already processed when we get to i.

Then, create a frequency dictionary (or array) where for each depth, we count the number of nodes (apples) arriving at that time.

Then, the answer is 1 (for depth 0) plus the sum of (1 if count is odd else 0) for all depths >=1.

But wait, the root's depth is 0, and it's counted as 1. Then, all other nodes contribute to their depths. So the initial 1 is added for the root. Then, for all other nodes (i=2 to n), their depth is added to the frequency count.

So the steps in code:

Read n.

Read the p array (p2, p3,...,pn). But since the input is given as p2 to pn, for i=2 to n, p[i] is given. So for example, in the first input line, for n=3, the second line is 1 1 → p[2] =1, p[3]=1.

Then, compute the depth array. depth[1] =0. For i from 2 to n, depth[i] = depth[p[i]] +1.

Then, create a frequency dictionary. For i from 2 to n, increment the count for depth[i] by 1.

Then, the answer starts with 1 (the root's apple), then for each key in the frequency dictionary (excluding 0?), we check if the count is odd. Because the root's depth is 0, but all other depths (from i >=2) are >=1. So in the frequency dict, depth 0 is not present (since i starts from 2). Wait, for example, the root is 1. All other nodes (2 to n) have their own depths.

So the initial 1 is for the root. Then, for each depth in the frequency counts (which are depths >=1), we add 1 if the count is odd.

So code steps:

Initialize a list called depth, with depth[1] =0.

For i from 2 to n:

   depth[i] = depth[p_i] +1

Then, create a freq dictionary, and for each i from 2 to n, increment freq[d] where d is depth[i].

Then, the answer is 1 + sum(1 for count in freq.values() if count %2 ==1)

So for sample 1:

i=2, depth 1. i=3, depth 1. freq for 1 is 2. 2 mod 2=0 → adds 0. So total is 1.

Sample 2: freq for 1 is 1 (i=2), which is odd → adds 1. For depth 2, freq is 3 → odd → adds 1. So 1 +1+1=3.

Yes.

Now, considering the constraints:

n can be up to 1e5. So the solution must be O(n) time and O(n) space.

Computing the depth for each node in O(1) per node is manageable. The frequency counts can be stored in an array, where the maximum possible depth is up to n-1 (in a linear chain). So for n=1e5, the array can be of size 1e5.

But in Python, for n=1e5, a list of size 1e5 is acceptable.

So, for example, the steps:

Read n.

Read p_list: list of n-1 integers. These are p2, p3, ..., pn. So for i from 2 to n, p[i] = p_list[i-2].

Compute depth array:

depth = [0]*(n+1)

for i in 2..n:

   depth[i] = depth[p_list[i-2]] +1

Then, freq array:

freq = [0]*(max_depth +1) → but max_depth can be up to n-1. So create a list of size (n) (since depth can be up to n-1, for a linear chain).

But instead of precomputing the max depth, perhaps use a dictionary.

But for speed, using a list is better. Let's think:

The maximum possible depth for a node is up to n-1 (e.g., a linear chain 1-2-3-...-n. Each node's depth is i-1. So node 2 has depth 1, node 3 has depth 2, etc. So for node n, depth is n-1. So for n=1e5, the list size would need to be 1e5. But in Python, initializing a list of 1e5+1 elements is acceptable.

So:

Initialize a list of zeros with size (max possible depth). But how to compute the max possible depth? Alternatively, we can use a dictionary to count frequencies, which is O(1) per access, but for speed, perhaps a list is better.

But for n=1e5, a list of 1e5 elements (assuming that depth can be up to 1e5) is manageable.

Wait, but in Python, list indices start at 0. So for a node with depth d, which can be up to n-1 (like in a linear chain), the list needs to have at least (n) elements, since d can be from 0 (for node 1) up to n-1.

But the frequencies for the answer are only for depth >=1. Because the root's contribution is 1 (counted separately), and the rest (nodes 2..n) have depth >=1.

So, the steps:

- Initialize a list freq of size (max_depth +1). But since max_depth can be up to n-1, the freq list can be initialized to [0] * (n). Because the maximum possible depth is n-1 (for a linear chain of n nodes). For example, for n=5, a chain 1-2-3-4-5: depth 5 is 4 (since 5's depth is 4). So for n=1e5, the freq list needs to be size 1e5, but the maximum index would be 1e5-1. Wait, no. The maximum depth is (n-1) for node n, in a linear chain. So the freq list needs to have (n) elements, since depth can be from 0 to n-1. So for a list of size (n), indexes 0 to n-1. So for n=1e5, the list will have 1e5 elements, which is 1e5 * 4 bytes (if stored as integers) is 400KB, which is acceptable.

But in practice, the depth for all nodes 2..n will be computed. Then, for each i in 2..n, we take depth[i] and increment freq[depth[i]] by 1.

Once all nodes are processed, we sum 1 for each freq[d] where d >=1 and freq[d] is odd.

So, code steps:

n = int(input())

p = list(map(int, input().split()))  # p2 to pn. p[i] is the parent of i+2? Wait, no.

Wait, for example, in the first sample input:

n=3. The second line is 1 1 → which are p2 and p3. Because the nodes are 2 and 3, their parents are 1 and 1.

So for the input list, the index corresponds to the node i-2. For example, for node 2 (i=2), p[0] is the parent. For node 3, p[1] is the parent.

So the code:

p = list(map(int, input().split())) → len(p) is n-1.

For i in 2..n:

   parent = p[i-2]

So for i=2, index 0, etc.

Then, compute depth for each node from 2 to n.

So code:

depth = [0]*(n+1)  # assuming nodes are 1-based.

depth[1] = 0

for i in range(2, n+1):

    parent = p[i-2]

    depth[i] = depth[parent] + 1

Then, create a frequency list. Initialize a list of zeros of size (max_depth +1). But since max_depth can be up to (n-1), as per the linear chain example.

But to avoid having to track the max depth, perhaps using a dictionary is easier. But for speed, a list would be better.

Alternatively, since we can create a list of size (n) (since the maximum possible depth is n-1), and for each depth from 1 to n-1, count how many times it occurs.

So:

freq = [0]*(n)  # indexes 0 to n-1.

for i in 2 to n:

    d = depth[i]

    freq[d] +=1

Then, the answer is 1 (from depth 0) plus sum(1 if freq[d]%2 else 0 for d in range(1, n)).

But wait, the maximum depth can be up to n-1, so we need to loop up to (n-1) inclusive.

So, the code for the answer part:

ans = 1

for d in range(1, n):

    if freq[d] %2 ==1:

        ans +=1

But since for d >=1, the loop can run from 1 to (max_depth), but how do we know the max_depth? Well, in the worst case, the maximum depth is n-1, so checking up to n-1 is necessary.

But in Python, for a list of size n, indexes 0 to n-1. So for d in range(1, n) → includes 1 to n-1. Which is correct.

So this would cover all possible depths. Even if some depths are zero (but those are only for node 1, which is not in the loop for i=2..n).

Thus, the code should work.

Now, let's test it against sample 3.

Sample 3 input:

18

1 1 1 4 4 3 2 2 2 10 8 9 9 9 10 10 4

Wait, the input line is for p2 to p18. So the length is 17 (n=18, n-1=17).

Let's compute the depth for each node.

Let's list the nodes from 2 to 18 and their p values:

i | p[i-2]

2 → 1

3 →1

4→1

5→4

6→4

7→3

8→2

9→2

10→2

11→10

12→8

13→9

14→9

15→9

16→10

17→10

18→4

Let's compute the depth for each:

depth[1] =0.

i=2: p=1 → depth[2] = 0+1=1.

i=3: p=1 → depth=1.

i=4: p=1 → depth=1.

i=5: p=4. depth[4] is 1 → depth[5]=2.

i=6: p=4 → depth=2.

i=7: p=3. depth[3] is 1 → depth[7] =2.

i=8: p=2. depth[2] is 1 → depth[8]=2.

i=9: p=2 → depth=2.

i=10: p=2 → depth=2.

i=11: p=10 → depth[10] is 2 → depth 3.

i=12: p=8 → depth[8] is 2 → depth 3.

i=13: p=9 → depth[9] is 2 → depth 3.

i=14: p=9 → depth 3.

i=15: p=9 → depth 3.

i=16: p=10 → depth[10] is 2 → depth 3.

i=17: p=10 → depth 3.

i=18: p=4 → depth[4] is 1 → depth 2.

So the depths for nodes 2-18 are:

2:1

3:1

4:1

5:2

6:2

7:2

8:2

9:2

10:2

11:3

12:3

13:3

14:3

15:3

16:3

17:3

18:2

Now, let's count the frequencies for each depth:

depth 1: nodes 2,3,4 → count 3.

depth 2: nodes 5,6,7,8,9,10,18 → 7 nodes.

depth 3: nodes 11,12,13,14,15,16,17 →7 nodes.

So the freq array will have:

freq[1] =3 → mod 2 is 1 → add 1.

freq[2] =7 → mod 2 is 1 → add 1.

freq[3] =7 → mod 2 is 1 → add 1.

Plus the initial 1.

So total is 1 + 1 +1 +1 =4. Which matches the sample output.

Thus, the code works for this case.

Now, let's think about the space.

For n=1e5, the depth array is of size n+1 (1e5+1 elements), which is about 400KB (each element is an integer). The freq array is of size 1e5, which is 400KB. So total space is acceptable for 256MB.

Time-wise, the code is O(n), which for 1e5 is manageable.

So the code should work.

Now, let's implement this in Python.

But wait, in Python, list indexes start at 0. So when we create the freq list, for depth d, which can be up to n-1, the list should be of size n, since the maximum possible d is n-1. For example, if n=1e5, then the list is initialized as [0]*n, which gives indexes 0 to 99999. So for a node with depth d=99999, the index is correct.

Yes.

So code:

n = int(input())

p = list(map(int, input().split()))  # len(p) is n-1

depth = [0] * (n + 1)  # 1-based indexing

for i in range(2, n+1):

    parent = p[i-2]

    depth[i] = depth[parent] +1

freq = [0] * n  # indexes 0..n-1

for i in range(2, n+1):

    d = depth[i]

    freq[d] +=1

ans = 1  # the root's apple

for d in range(1, n):  # since depth can be up to n-1

    if freq[d] %2 ==1:

        ans +=1

print(ans)

But wait, the loop for d is from 1 to n-1 inclusive. Because in Python, range(1, n) gives numbers from 1 to n-1. So yes.

This should work.

Let's test the first sample:

Sample 1:

n=3.

p = [1,1].

depth[2] = depth[1]+1 →1.

depth[3] = depth[1]+1 →1.

freq for 1: 2.

ans starts at 1.

Loop for d=1 (since n=3, range(1,3) is 1 and 2? Wait, no. range(1,3) is 1 and 2. Because range is up to but not including the end. So for n=3, the loop runs from d=1 to 2. But in the first sample, the depths for nodes 2 and 3 are 1, so in freq, index 1 is 2, and index 2 is 0. So:

d=1: freq[1]=2 → even → no addition.

d=2: freq[2]=0 → even → no addition.

So ans is 1. Correct.

Sample 2:

n=5.

p is [1,2,2,2].

depth:

2:1

3:2 (parent 2's depth is 1)

4:2 (parent is 2)

5:2 (parent is 2)

freq[1] =1 (node2), freq[2]=3 (nodes3,4,5).

ans =1.

Then, d=1: freq 1 is 1 → add 1 → ans=2.

d=2: freq 3 → add 1 → ans=3.

d=3: freq 0 → no. So total 3.

Yes.

Sample3:

depth counts are 3,7,7.

So for d=1:3 mod 2 →1 → add.

d=2:7 mod 2 →1 → add.

d=3:7 mod 2 →1 → add.

ans=1 +3 =4. Correct.

So the code works for all samples.

Thus, this is the correct approach.
</think>

```python
n = int(input())
p = list(map(int, input().split()))
depth = [0] * (n + 1)
for i in range(2, n + 1):
    parent = p[i - 2]
    depth[i] = depth[parent] + 1

freq = [0] * n
for i in range(2, n + 1):
    d = depth[i]
    if d < n:
        freq[d] += 1

result = 1
for d in range(1, n):
    if freq[d] % 2 == 1:
        result += 1

print(result)
```