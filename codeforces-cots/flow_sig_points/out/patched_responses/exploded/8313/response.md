<think>
Okay, let's see. We need to find for each student a, which student ends up with two holes when the process starts with a. The process is that the teacher follows the p pointers until they hit a student that's already been visited (i.e., has a hole). The first student to get a second hole is the answer for a.

Hmm. So for each a, we need to simulate the path taken starting from a, and track the first student that is visited twice. Because once the teacher arrives at a student that's already been visited (has a hole), that's when the process stops. So the second visit to that student is when the second hole is made.

So for each a, the steps are: start at a, then go to p[a], then p[p[a]], etc., keeping track of visited students. The first time we encounter a student that's already in the visited set is the answer for that a.

But simulating this for each a directly might not be efficient if n is up to 1000. Wait, but n is 1000, so for each a, the path could be up to O(n) steps, leading to O(n^2) time, which is 1e6 operations. That's acceptable for Python in 1 second, right? Because 1e6 operations are manageable.

Wait, but maybe there's a smarter way. Let's think about the structure of the p array. Since each p_i points to another student, the graph is made up of cycles and trees leading into cycles. Because each node has exactly one outgoing edge (since each p_i is a single value), so the structure is a collection of cycles with trees directed towards them.

So when you start at a node a, you follow the path until you hit a cycle. The first node that is revisited in the traversal is part of the cycle. So for a node a, the answer is the first node in the cycle of its component that is visited twice.

Wait, but the process is such that the teacher starts at a, then each step follows p, and stops when they hit a node that has already been visited (i.e., the first time they step on a node that's already in the path). So the path forms a chain leading into a cycle, and the first duplicate is the start of the cycle.

Wait, for example, if the path is a → b → c → d → c → ... then the first duplicate is c. So the answer for a would be c. Because the teacher visits a (hole 1), then b (hole 1), c (hole 1), d (hole 1), then returns to c (hole 2). So c is the answer.

So the problem reduces to, for each node a, find the start of the cycle in its component, which is the first node that is revisited when following the p pointers. That node will be the answer.

So the key insight here is that each component is a linked list leading into a cycle. The answer for any node in the component is the entry point of the cycle.

So for each a, when you traverse the path from a, you need to detect the first node that is visited twice. That's the answer.

So how can we compute this efficiently?

The straightforward way is for each a, simulate the path until we find the first duplicate. But as n is 1000, this is O(n^2) steps. For n=1000, 1e6 steps should be manageable. Python can handle that, right? Because 1e6 steps are about a million operations, which is acceptable in 1 second.

So the plan is:

For each a in 1..n:

- Keep a visited set or a dictionary to track visited nodes as we traverse.

- Start at a, add to visited.

- Then follow p[a], check if it's in visited. If yes, that's the answer. Else, add to visited.

- Continue until we find the first node that is already in visited.

So for each a, the steps are O(k), where k is the length of the path until the cycle starts. The worst case is O(n) per a.

But with n=1e3, 1e3 * 1e3 = 1e6 steps. Which is manageable.

But maybe there's a smarter way. Let's think about precomputing for each node the answer.

But how?

Alternatively, we can note that each node's answer is the start of the cycle in its component. So if we can find for each node which cycle it's part of, or where the cycle starts for their component, then we can precompute all answers.

For example, in a component that is a cycle (like a loop), then each node in the cycle will have the answer as the node itself. Because when you start at a node in the cycle, you loop around and the first node you hit again is the starting node. Wait, no. Let's see.

Wait, if a node is part of a cycle, then starting at that node, you follow the cycle. The first time you hit a node again is after going all the way around. So for example, nodes 1 → 2 → 3 → 1. So starting at 1, the path is 1 (hole 1), 2 (hole 1), 3 (hole 1), 1 (hole 2). So the answer is 1. Similarly, starting at 2, the path is 2,3,1,2 → the answer is 2.

So for nodes in a cycle, their answer is themselves.

But for nodes that are in trees leading into the cycle, their answer is the entry point of the cycle.

For example, consider nodes 4 →5 →2 →3 →2. So 2 and 3 form a cycle, and 4 and 5 are trees leading into it. So starting at 4, the path is 4 →5 →2 →3 →2. The first duplicate is 2, which is the entry point. So answer is 2.

So for any node in the tree part, their answer is the entry point of the cycle in their component. For nodes in the cycle, their answer is themselves.

So the problem reduces to, for each node, find the entry point of the cycle in its component.

So how can we find this for all nodes efficiently?

One approach is to use Floyd's cycle-finding algorithm (tortoise and hare) for each component, but that's maybe more complex. Alternatively, we can precompute for each node the answer by finding the cycle for their component.

But maybe the simplest way is to precompute for each node the answer by tracking the path when we visit it, and for each node in the path, if we haven't computed their answer yet, we can set it once the cycle is detected.

This is similar to the way we find cycles in a linked list and assign the entry point to all nodes in the path leading to the cycle.

Here's the approach:

For each node from 1 to n:

If the node hasn't been processed yet, start traversing from it, keeping track of the path. When a node is encountered that is already in the current path (i.e., the cycle is detected), then the entry point is that node. All nodes in the path from the start to the entry point (excluding the entry point itself) are part of the tree leading into the cycle, and their answer is the entry point. All nodes in the cycle have their answer as themselves.

Wait, no. Let's see:

For example, if the path is a → b → c → d → c → ..., then the entry point is c. The nodes a, b are in the tree leading into the cycle. Their answer is c. The nodes c, d are part of the cycle. Their answer is c for a starting point of a, but wait, when starting at c, the path is c, d, c. So the answer for c is c itself.

So for all nodes in the component, their answer is the entry point of the cycle. Wait, no. Because nodes in the cycle, when you start at them, you'll loop around and hit themselves again. So the entry point is themselves.

Wait, perhaps the entry point is the first node in the cycle that is visited twice. So for a component consisting of a cycle and trees leading into it:

All nodes in the tree leading into the cycle (the chain) have their answer as the entry point (the start of the cycle). The nodes in the cycle have their answer as themselves.

So how do we find this for each node?

Another way to look at it: For each node, when you follow the path, the first node that is revisited is the answer. For nodes in the cycle, this will be the node where the cycle starts. For nodes in the tree, this will be the entry point to the cycle.

So perhaps for each node, we can track the path until we find a cycle, and then for each node in the path, set their answer to the entry point of the cycle.

But how to do this efficiently.

An alternative approach is to process each component once. For example, when we find a component (cycle plus trees), process all nodes in that component in O(k) time, where k is the size of the component. Then, for all nodes in the component, their answer is determined.

So the steps would be:

1. Iterate through each node from 1 to n.

2. For each unvisited node, start traversing until we find a cycle.

3. Once the cycle is found, backtrack and assign answers for all nodes in the path leading to the cycle, and for the cycle nodes.

But how?

Let me think of an example. Let's say the path is a → b → c → d → e → c. So the cycle is c → d → e → c.

So the entry point is c.

Now, the nodes a and b are in the tree leading into the cycle. Their answer is c.

Nodes c, d, e are in the cycle. So their answer is themselves.

So the way to process this would be:

When we start at a, we traverse a, b, c, d, e, c (which is already in the path). The first duplicate is c. So for all nodes up to c (a, b, c), their answer is c. But wait, for node c, when you start at c, the path is c, d, e, c. So the first duplicate is c. So the answer for c is c. Similarly, d's answer would be d? Or wait, no. Wait, let's see.

Wait, the answer for a is c. For b, the answer is c. For c, when we start at c, the path is c (hole 1), then d (hole 1), e (hole 1), then c (hole 2). So the answer is c. For d: starting at d, the path is d (hole 1), e (hole 1), c (hole 1), d (hole 2). So the answer is d. Wait, but according to the sample input, for the case where the cycle is 2 →3 →2, starting at 3 gives 3 as the answer.

Wait, in the first example:

Sample Input 1:

3

2 3 2

So p = [2,3,2]

So the students are 1: p_1 = 2, 2: p_2=3, 3: p_3=2.

The answer for 3 is 3, because the path is 3 →2 →3. So when starting at 3, the first duplicate is 3. So the answer is 3.

So for the cycle 2 →3 →2, the entry point is 2. But when you start at 3, the path is 3 →2 →3. So the first duplicate is 3? Wait, no. Wait, the steps for starting at 3 would be:

Step 1: 3 (hole 1). Then p[3] is 2 (hole 1). Then p[2] is 3 (hole 1). Then step 3 is 3 again. So the teacher comes to 3 again, which already has a hole, so the answer is 3.

So in that case, the answer for 3 is 3, which is part of the cycle but the answer is the node where the cycle is entered again.

Wait, this suggests that the answer is the first node that is encountered twice. So for the cycle, when you start at a node in the cycle, you go through the cycle once, then hit the starting node again. So the answer is the starting node.

But when you start at a node that leads into the cycle, you enter the cycle and the first node that is hit again is the entry point.

Hmm, this complicates things. Because in the case of a cycle, the answer for any node in the cycle is themselves. But when you start at a node leading into the cycle, the answer is the entry point.

So how can we model this?

Alternatively, for each node a, the answer is the first node that is visited again when following the path starting at a. This could be a node in a cycle, which may be a itself.

So for example:

If the cycle is a → b → a, then starting at a: the path is a (hole 1), b (hole 1), a (hole 2). Answer is a. Starting at b: path is b (hole 1), a (hole 1), b (hole 2). Answer is b.

So in this case, the answer for nodes in the cycle is themselves.

But for a component that's a chain leading into a cycle, like a → b → c → d → c, the answer for a is c, for b is c, for c is c, for d is d. Because:

Starting at a: path is a →b →c →d →c (duplicate is c). Answer is c.

Starting at b: path is b →c →d →c (duplicate c). Answer is c.

Starting at c: path is c →d →c (duplicate c). Answer is c.

Starting at d: path is d →c →d (duplicate d). Answer is d.

Wait, but according to this, the answer for d is d. But in the cycle c →d →c, the cycle is between c and d. Wait, in this example, the cycle is c →d →c. So when you start at d, the path is d →c →d. So the first duplicate is d (since d is the first node visited again). So the answer is d.

But according to the component processing approach, the entry point of the cycle is c, but in this case, starting at d, the entry point would be d.

So this suggests that the entry point depends on where you start in the cycle. Which makes this approach more complex.

So the only way to find the answer for each node is to simulate the traversal until the first duplicate is found.

Thus, perhaps the straightforward approach is acceptable here. For each a, simulate the path, track visited nodes, and return the first duplicate.

But with n=1000, this is O(n^2), which for Python is manageable. Let's see.

In the worst case, each a requires up to n steps. For n=1000, that's 1e6 steps. Python can handle that in under a second. So perhaps this approach is feasible.

So let's proceed with this approach.

So the plan is:

For each a from 1 to n:

Initialize a visited set (or a list of booleans).

Start at a, add to visited.

Then next_node = p[a-1] (since p is 0-indexed in Python's list if stored as a list).

Check if next_node is in visited. If yes, return next_node.

Else, add to visited, and proceed.

Repeat until you find the next_node in visited.

So the code would look something like:

n = int(input())
p = list(map(int, input().split()))

result = []
for a in range(1, n+1):
    visited = set()
    current = a
    while True:
        if current in visited:
            result.append(str(current))
            break
        visited.add(current)
        current = p[current-1]  # because p is 0-based in the list?

Wait, let's check the input:

The second line is p_1 ... p_n, which are 1-based. So p[0] in the list corresponds to p_1. So for student a (1-based), their p_a is stored as p[a-1]. So yes.

So for a in 1..n:

current = a

loop:

if current is in visited, return current.

else, add to visited.

current becomes p[current-1]

So for each a, this process finds the first duplicate.

But wait, in the first example:

Input:

3

2 3 2

p is [2,3,2] in the list (0-based index 0: p_1=2, index 1: p_2=3, index 2: p_3=2.

For a=1:

visited starts empty.

current =1. add to visited.

current becomes p[0] = 2. add to visited.

current becomes p[1] =3. add to visited.

current becomes p[2] =2. Check if 2 is in visited. Yes. So append 2 to result.

Which matches the first example.

Yes.

Another example:

Input:

3

1 2 3

So p is [1,2,3].

For a=1: current is 1. added to visited. next is p[0] =1. check if 1 is in visited: yes. So append 1.

Which matches the second example.

So the code works for the sample cases.

But what about the time?

For each a, the loop runs until the first duplicate is found. For a cycle, this would take steps equal to the cycle length. For a node leading into a cycle, the steps are the length of the chain leading into the cycle plus the cycle up to the first duplicate.

But in the worst case, each a takes O(n) steps. So for 1e3 nodes, it's 1e6 steps.

In Python, each step is a simple lookup in a set. However, using a set may be a bit slower than a list of booleans.

Alternative approach: use a visited array (list) of size n+1 (since students are numbered from 1 to n). For each a, we can reset this array to all False, then mark as we go.

But for each a, we need O(n) space. But since n is 1e3, for each a, creating a new list of n+1 elements (1e3+1) is 1e3 elements, which is manageable. But doing this for each a would use O(n^2) space. For n=1e3, that's 1e6 elements. But since each a's visited array is processed and then discarded, it's manageable. But in practice, using a list and resetting for each a may be more efficient than using a set.

Alternatively, for each a, we can use a visited list initialized to False for all elements, and mark True as we visit. For each a:

visited = [False] * (n+1)

current = a

loop:

if visited[current] is True: append current.

else: mark as True, proceed.

So code:

for a in 1..n:

visited = [False] * (n+1)

current = a

while True:

if visited[current]:

    result.append(current)

    break

visited[current] = True

current = p[current-1]

This approach uses a list of booleans, which is faster for checking and marking than a set, especially for larger n.

This should be more efficient than using a set, especially for n=1e3.

Thus, this approach is better.

So the code would be:

n = int(input())
p = list(map(int, input().split()))

ans = []
for a in range(1, n+1):
    visited = [False] * (n+1)
    current = a
    while True:
        if visited[current]:
            ans.append(str(current))
            break
        visited[current] = True
        current = p[current -1]

print(' '.join(ans))

Wait, but in Python, for each a, creating a new list of size n+1 (1001 elements) 1000 times is 1000*1000 = 1e6 elements. But each is a boolean, which is just one byte. So 1e6 booleans is about 1MB, which is acceptable.

But for n=1000, creating a list of 1001 elements 1000 times would take up 1e6 elements, which is manageable.

But in Python, list creation is O(n) time. So for each a, creating a visited list is O(n) time. So the total time would be O(n^2) time. For n=1e3, that's 1e6 operations. Which is acceptable.

But perhaps we can optimize by reusing a single visited array and resetting it for each a. But in Python, creating a new list each time is more straightforward and avoids potential bugs.

In any case, for n=1e3, this code should work within the time limit.

Testing the first sample:

Input:

3

2 3 2

Processing a=1:

visited is all False.

current=1: mark as True.

current becomes 2: mark as True.

current becomes 3: mark as True.

current becomes 2: already True. Append 2.

a=2:

current=2 → mark as True.

current is 3 → mark True.

current is 2 → already True. Append 2.

a=3:

current=3 → mark True.

current is 2 → mark True.

current is 3 → already True. Append 3.

So output is 2 2 3, which matches.

Second sample:

3

1 2 3

For a=1: the loop runs once. current=1 is marked. next is 1, which is already marked. So append 1.

a=2: current=2, mark. next is 2. append 2.

a=3: current=3, next is 3. append 3.

Output is 1 2 3.

Which matches.

So the code works for the samples.

Thus, this approach is correct and efficient enough.
</think>

```python
n = int(input())
p = list(map(int, input().split()))

ans = []
for a in range(1, n + 1):
    visited = [False] * (n + 1)
    current = a
    while True:
        if visited[current]:
            ans.append(str(current))
            break
        visited[current] = True
        current = p[current - 1]

print(' '.join(ans))
```