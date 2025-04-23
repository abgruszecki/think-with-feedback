<think>
Okay, let's tackle this problem. Hmm, the problem statement is a bit complex. Let me try to understand it.

So, the input is a string that represents a tree structure of comments. Each comment has some replies (children), and the structure is serialized in a specific way. Our task is to parse this structure and output the maximum depth of the comments and then for each level from 1 to d, list the comments in the order they appear in the original input at that depth.

First, I need to parse the input string into the hierarchical structure of comments. Then, traverse this structure to collect the comments grouped by their depth.

Wait, how is the input structured? For each comment, it's written as [text],[number of children], followed by the children comments. So the parsing is recursive. For example, the first example's input is "hello,2,ok,0,bye,0,test,0,one,1,two,2,a,0,b,0".

Breaking that down: The root comments are the ones that are siblings. The root level has "hello", then "test", then "one". Because each root comment's entire structure is written in the input before the next root comment.

Wait, no. Wait, the way the input is written is that each root comment is processed first, then the next root, etc. Because the root comments are the highest level. So the entire input is a list of root comments, each of which may have their own children, recursively.

So the parsing process needs to process the input as a list, where each element is a root comment. Each comment is processed by reading the text, then the number of children, then recursively processing each child in sequence.

So the parsing will result in a list of nodes, each with their children. But the order in which nodes appear in the input is important for the output. Because the output requires the comments to be grouped by their depth and in the order they appeared in the original feed.

So, the key is to parse the input into a tree structure, and then perform a breadth-first traversal (or some traversal that captures the order of appearance and their levels) to collect the nodes by their depth.

Wait, but how do the depths work? The root comments are at depth 1. Their children are depth 2, and so on.

Yes, because the root comments are the highest level, so each root is depth 1, their children are 2, etc.

So the problem reduces to:

1. Parsing the input string into a list of root comments (each with their own subtree).
2. Traversing all nodes in the order they were parsed (since the order in the output is the same as the input order for each depth level), and track their depth.
3. Group all nodes by their depth, and for each depth level, collect the nodes in the order they were encountered in the input.
4. Find the maximum depth, then output the nodes per depth level, from level 1 to max depth.

Wait, but the nodes are processed in a way that parent comes before their children. So in the input, a parent is written before its children. So during parsing, the parent is added to the list first, then its children are parsed. So in the traversal, the order for a given depth would be the order in which the nodes were parsed. But when you traverse the tree, the nodes are processed in a way that parents come first, then their children. So the order of nodes in the same depth is the same as the order they appear in the input.

So the approach is:

- Parse the entire input into a tree structure, keeping track of the order of nodes as they appear in the input. Because each node's children are parsed after the node itself, but the siblings (other root comments) are parsed later.

Wait, no. Let's think. For example, the first example's input is:

hello,2,ok,0,bye,0,test,0,one,1,two,2,a,0,b,0

Breaking this down:

The root comments are hello, test, one.

- The first root is "hello" with 2 children. Then we parse its children: "ok" (0 children) and "bye" (0). Then comes the next root comment "test" (0 children), then "one" (1 child: two, which has 2 children: a and b).

So during parsing, the order of the nodes in the input is:

hello (depth 1), ok (depth 2), bye (depth 2), test (depth 1), one (depth 1), two (depth 2), a (depth 3), b (depth 3).

So when we group by depth, depth 1 has hello, test, one; depth 2 has ok, bye, two; depth 3 has a, b. The output is ordered per depth in the order the nodes were first encountered in the input.

So the key is to track, for each node, the depth it is at, and the order in which they were parsed.

So how can we parse the input and track the depth of each node?

The parsing process is a recursive structure. For example, when parsing a root comment (depth 1), we parse its children (depth 2), which in turn parse their children (depth 3), etc.

Therefore, during parsing, each node's depth is known based on the depth of its parent. The root nodes have depth 1. Each child's depth is parent's depth +1.

But the nodes are parsed in a depth-first order. For example, the first root node (hello) is parsed, then its children (ok, then bye), then the next root node (test), then the next root node (one), then its children (two), then two's children (a and b).

So the order in which nodes are parsed (i.e., the order they appear in the input) is hello, ok, bye, test, one, two, a, b.

Wait, but in the input, the root nodes are processed in the order they are written. So the input is a list of root nodes. Each root is processed by writing its text, then the number of children, then each child (which are processed recursively). So the order of nodes in the input is a pre-order traversal of the tree.

So, the order in which nodes are encountered in the input is the same as a pre-order traversal of the entire tree (since each node's children are written immediately after it).

So, when we parse the input, the nodes are processed in pre-order (parent first, then children, in order). So, when we collect the nodes in the order they were parsed (pre-order), and track their depth, grouping them by depth, the order within each depth is the order in which they were first encountered in the input.

Therefore, the plan is:

1. Split the input string into tokens. The input is a comma-separated list of elements. Each element is either a string (text of a comment) or a number (count of children). So the first token is the text of the first root comment, then the next token is the number of children, then each child (each child is a text followed by its children count and so on), then the next root comment, etc.

So the parsing can be done by splitting the input string into tokens (split by commas). Then, process the tokens in sequence.

The parsing can be done using a stack. Here's how:

We can model the parsing as a stack of nodes that need to process their children. Each node in the stack is a tuple of (number_of_children_remaining, parent_depth). For example, when we encounter a node's text and the number of children, we create a new node with depth. Then, we need to read that number of children. So, after processing the text and the count, we push onto the stack an entry that says how many children are left to process. Then, each child is processed in sequence.

Wait, perhaps a better approach is to use a recursive approach. But since the input can be very large (up to 1e6 characters), recursion might hit the stack limit. So better to use an iterative approach.

Let me think of a way to parse the tokens into a list of nodes, each with their depth.

The tokens are a list generated by splitting the input on commas.

We can process the tokens in order, keeping track of the current depth and the parent nodes.

Wait, here's an alternative approach:

We can use a stack to track the current nodes that have children remaining. Each element in the stack is a (node, remaining_children_count, depth). When processing a new node:

- The next token is the text.
- Then the next token is the number of children (k).
- Create a node with text, and depth = current depth (determined by the stack's top element's depth +1, or 1 if stack is empty).
- Add this node to the list of all nodes (maintaining the order they are parsed).
- Then, if k >0, we push a new entry onto the stack indicating that this node expects k children. Then, the next k nodes will be children of this node, and thus have depth +1.

Wait, but how to track the depth correctly.

Wait, let's model the stack as a list where each entry represents a parent node and how many children it still needs to process. Each time we process a new node, its depth is determined by the current stack depth.

Wait, perhaps the depth is the length of the stack plus 1. Because when the stack is empty, the node is a root (depth 1). When the stack has one entry (the parent), the node is depth 2. When processing a child, the stack has the parent entry, and so on.

Wait, no. Let's see:

- Root nodes are processed when the stack is empty. Each root node is depth 1.

- When processing a root node, if it has k children, we push (k) onto the stack. Then, the next k nodes are the children of this root. Each of these children is at depth 2.

- When processing a child node (depth 2), if it has m children, then push (m) onto the stack, and the next m nodes are depth 3.

Wait, maybe the stack can keep track of the number of children remaining for each parent. But how does this affect the depth?

Hmm, perhaps the depth is equal to the current level of nesting. So when processing a node, its depth is determined by the number of active parents in the stack.

Wait, for example:

Initially, stack is empty. Processing a root node: depth is 1. If it has k children, we push k to the stack (indicating that we need to process k children for this node). Then, the next nodes are children of this root, so their depth is 2. For each child, after processing its own children count, if it has m children, then we push m to the stack, and their depth is 3, and so on.

Wait, but the stack can be a stack of the counts of remaining children for each level. For example, when a node has k children, the stack is [k]. When processing a child, the count is decremented. When the count reaches zero, it's popped from the stack. But this approach might not track the depth correctly.

Alternatively, perhaps the stack can track the number of children remaining for the current parent. Let's think step by step.

Let's take the first example input:

The tokens are:

['hello', '2', 'ok', '0', 'bye', '0', 'test', '0', 'one', '1', 'two', '2', 'a', '0', 'b', '0']

Parsing steps:

- Start with stack empty. The current depth is 1 (since stack is empty).

- Take the first token 'hello' as text. Next token is '2' (k=2). So create a node 'hello' at depth 1. Add to the list. Then, since k=2, we push 2 onto the stack. The next nodes will be children of this node, so their depth is 2.

- Next token is 'ok' (text). Next token is '0' (k=0). So create a node 'ok' at depth 2 (since the stack is not empty, depth is current stack depth +1? Wait, stack is [2], so the depth is 2. Add to the list. Since k=0, no children. So the stack's top entry (2) is decremented to 1 (since we processed one child). Now, the stack is [1].

- Next token is 'bye' (text). Next token is '0' (k=0). Create node 'bye' at depth 2. Add to list. Decrement stack top to 0. Now, stack is [0]. So pop it, and proceed.

- Now stack is empty. Next token is 'test' (text). Next token is '0' (k=0). So depth is 1 again. Add to list, no stack entry.

- Next token is 'one' (text). Next token is '1' (k=1). Add node 'one' depth 1. Push 1 onto stack. Next nodes are children (depth 2).

- Next token is 'two'. k=2. Add node 'two' depth 2. Push 2 onto stack. Next children (depth 3).

- Next token 'a' (k=0). Add depth 3. stack becomes [2-1=1]. Then next token 'b' (k=0). Add depth 3. stack becomes [0], pop. Now stack is empty. Then, the next nodes are siblings of 'two'? Wait, no. The 'two' node had two children, which are 'a' and 'b'. So after processing 'a' and 'b', stack is empty (since the 2 was popped after processing both). Then, the parent of 'two' is 'one', which had k=1. So after processing 'two', which is the first child of 'one', the stack entry for 'one' is 1-1=0. So after processing 'two' and its children, the stack for 'one' is popped, and stack is empty. Then, proceed to next tokens.

Wait, perhaps the stack should track for each parent how many children are remaining. Each time a node is processed (text and count of children), we check if the stack is not empty. If the stack is not empty, the node is a child of the current parent. Then, after processing the node's k children, the parent's count is decremented.

Wait, perhaps a better way to model this is with a stack where each entry is the number of remaining children that the current parent expects. For example:

- When processing a root node (text, k), we add it to the list with depth 1. Then, if k>0, we push k to the stack. The next nodes will be its children, which have depth 1 + current stack size (since stack size is 1 now, depth is 2). Then, each time a child is processed, we decrement the top of the stack. When the top becomes zero, we pop it. So the depth is determined by the current stack size plus 1.

Wait, let's see:

Stack size represents the number of parents that are expecting children. So, for a root node with k children:

- After processing the root node (depth 1), stack is [k]. Then, the next node is a child, which has depth = stack.size() + 1 - 1? Or stack.size() + 1?

Wait, maybe stack.size() is the number of active parent levels. So for a node, the depth is stack.size() + 1.

Let me test this:

Root node:

- stack is empty. depth is 0 +1 =1.

Then, after pushing k=2, stack is [2]. Next node is child, depth is 1 +1 =2.

Then, when processing a child with k=0, depth is 1 (stack size is 1) +1= 2. Then, after processing it, stack remains [2 (now 1 after decrement)].

So the depth of each node is stack.size() + 1.

Yes, that makes sense.

So during parsing, the depth is determined by the current stack size plus 1.

So the parsing process can be as follows:

Initialize a list to collect all nodes in order (with their depth).

Initialize a stack. The stack keeps track of the number of children remaining for each parent.

Process the tokens in pairs: the first is the text, next is the number of children (k).

For each pair (text, k):

- The current depth is stack.size() + 1.

- Add the node (text, depth) to the list.

- If k >0, push k to the stack. Then, the next nodes will be children of this node, so their depth will be stack.size() +1.

But when processing the children, how do we track how many are left for each parent?

Wait, maybe the stack should track the remaining children count for each parent. For example, when a parent has k children, we push k to the stack. Then, for each child processed, we decrement the top of the stack. When the top becomes zero, we pop it.

Wait, let's think step by step:

Initial state: stack is empty.

Token pairs:

1. 'hello', 2:

   - depth = 0 +1 =1.

   - add node hello, depth 1.

   - k=2. push 2 to stack. stack is [2].

2. 'ok', 0:

   - stack is [2]. depth is 1 (stack.size() is 1) +1 =2.

   - add node ok, depth 2.

   - k=0. no children. So stack remains [2]. Then, decrement the top of stack by 1 (since this was a child of the parent with remaining count 2). Now stack becomes [1].

3. 'bye',0:

   - stack is [1]. depth is 1 +1=2.

   - add node bye, depth 2.

   - k=0. stack becomes [0]. Then, since the top is zero, pop it. stack is now empty.

4. 'test',0:

   - stack is empty. depth is 0 +1=1.

   - add node test, depth 1.

   - k=0. no stack changes.

5. 'one',1:

   - stack is empty. depth 1.

   - add node one, depth1.

   - k=1. push 1. stack is [1].

6. 'two',2:

   - stack is [1]. depth=1+1=2.

   - add two, depth 2.

   - k=2. push 2. stack is [1,2].

7. 'a',0:

   - stack size 2. depth 2+1=3.

   - add a, depth3.

   - k=0. decrement top (2 becomes 1). stack [1,1].

8. 'b',0:

   - stack size 2. depth3.

   - add b, depth3.

   - decrement top (1-1=0). pop from stack. stack becomes [1].

   - Now, stack is [1]. top is 1.

   - Then, since the top is 1 (parent of 'two' had k=1?), wait no. Wait, the stack after processing 'two' was [1,2]. Then, 'a' and 'b' are processed as children of 'two'. So when 'a' is processed, the stack becomes [1,1], then 'b' is processed, stack becomes [1,0], so pop, stack is [1].

   Then, after 'two's children are processed, we go back to the parent of 'two', which is 'one'. But 'one's children count is 1. So after processing 'two' (which is the first child of 'one'), the stack entry for 'one' is decremented to 0. Then, pop from stack. stack is empty.

So the stack entries track how many children are left for each parent. So when processing a node (text, k):

1. Calculate the current depth as stack.size() +1.

2. Add the node to the list with this depth.

3. If k >0, push k into the stack. Then, the next k nodes will be children of this node.

But wait, no. Because each child is processed one by one, and after processing each child, the parent's remaining count is decremented.

So the stack should track the remaining children for each parent. Each time a node is processed, it's a child of the current parent (the top of the stack). So:

Each time you process a node (text and k):

- The depth is stack.size() +1.

- Add the node to the list.

- If k >0:

   - push k to the stack.

- Then, after processing all children of this node (i.e., after processing k nodes which are children), we need to pop the stack.

Wait, but how do we track how many children remain for each parent?

Ah, here's the correct approach:

The stack is a list of (remaining_children, ...). Wait, perhaps each entry in the stack is the number of remaining children for the current parent. So:

When a node has k children, we push k to the stack. Then, each time a child is processed (regardless of whether it has children or not), the top of the stack is decremented by 1. If after decrementing, the top becomes 0, it is popped from the stack.

So, during processing:

- The depth is the current stack size (before processing this node) +1. Because the stack size is the number of parents that are expecting children. For example, when a root node is processed, the stack is empty. So depth is 0+1=1. After pushing k=2 (for root's children), the stack is [2]. The next nodes will be children of the root, their depth is 1+1=2 (stack size is 1).

So, for each node:

depth = len(stack) + 1.

Yes.

So, the algorithm for parsing is:

Initialize stack = []

tokens = input.split(',')

i = 0

all_nodes = []

while i < len(tokens):

   text = tokens[i]

   k = int(tokens[i+1])

   i += 2

   depth = len(stack) +1

   all_nodes.append( (text, depth) )

   if k >0:

       stack.append(k)

   else:

       # process any parent decrements

       pass

   # now, process the stack to decrement parents' counts

   # because the current node may be a child of some parent

   # but how?

Wait, no. Because the current node is a child of the current top of the stack. So after processing the node (text, k), if k>0, we push k to the stack. Then, the next nodes are the children of this current node.

But after processing this node, we need to check if the current parent (if any) has remaining children.

Wait, maybe the stack is a list of the number of children each parent has yet to process. For example:

When a node is processed, if it is a child of the current parent (stack not empty), then we decrement the top of the stack by 1.

Wait, this is the correct approach.

So, the steps are:

For each node (text, k):

1. depth is len(stack) + 1.

2. add to all_nodes.

3. if k >0, push k to the stack.

4. then, check if the stack is not empty. While the top of the stack is 0, pop it. Then, if the stack is not empty, decrement the top by 1.

Wait, perhaps:

After adding the node to the list:

   if the stack is not empty:

       stack[-1] -=1

   then, if k>0:

       stack.append(k)

   then, while stack and stack[-1] ==0:

       stack.pop()

       if stack:

           stack[-1] -=1

       else:

           break

Wait, perhaps not. Let me think.

No, the steps should be:

- After processing the node (text, k), which is a child of the current parent (if any), we need to decrement the parent's remaining count.

Because the node is a child of the parent at the top of the stack (if stack is not empty). So:

For example, when processing a child node:

Parent had a remaining count of 2. After processing this child, the parent's remaining count is 1.

So, after processing the node, if there's a parent (stack not empty), decrement the top.

Then, check if the top is zero. If so, pop it. Because that parent has no more children. Then, check again if the new top (if any) has been decremented (since that parent's remaining count would have been decremented when a previous child was processed). So perhaps this part is not necessary here.

Wait, perhaps the correct approach is:

Whenever a node is processed, after adding it to the list and handling its own children count (k), we need to decrement the parent's count (if any). Then, if that parent's count reaches zero, pop it, and continue decrementing higher parents (if any).

Wait, here's the correct sequence of steps:

1. Process the node (text, k). Add to all_nodes with depth len(stack) +1.

2. If k>0, push k to the stack (this node will have k children, which will be processed next).

3. Then, check if the stack is not empty (i.e., if this node is not a root, or if any parents are expecting children). Wait, no. Wait, the stack is the list of parents expecting children. So, when this node is a child of a parent, the parent's count is tracked in the stack. So, after processing this node (which may be a child), we need to decrement the parent's remaining count.

Wait, perhaps the stack is for the parents. For example, the top of the stack is the number of children remaining for the current parent.

So, when you process a node (could be a root or a child), after processing it, if there is a parent (stack not empty), then this node was a child of the parent. So the parent's remaining count should be decremented by 1.

But how do we know whether the current node is a child of the current stack's top parent?

The stack is maintained such that each entry represents the number of children remaining for a parent. So, when a node is processed, the stack is in a state where the top entry is the number of children remaining for the current parent. So, the current node is a child of that parent.

Therefore, after processing the node, if the stack is not empty, the top of the stack is decremented by 1 (because this node was a child of that parent).

Then, after decrementing, if the top becomes zero, it is popped from the stack. Then, the next node (if any) will be a sibling of the parent (if the parent was the child of a higher parent). So, this part is handled by the stack.

So, the algorithm steps for each node (text, k):

- depth = len(stack) + 1.

- add (text, depth) to all_nodes.

- if k >0: push k to the stack.

- then, while stack is not empty and stack[-1] ==0:

   pop from stack.

- if stack is not empty:

   stack[-1] -= 1

Wait, perhaps the correct steps are:

After adding the node to all_nodes:

   if stack is not empty:

       stack[-1] -=1

   if k>0:

       stack.append(k)

   # Now, check if any parents have reached zero.

   while stack and stack[-1] ==0:

       stack.pop()

       if stack:

           stack[-1] -=1

       else:

           break

       # after popping, check again.

Hmm, maybe this approach will correctly decrement the parents and handle popping when counts reach zero.

Let's test this with the first example:

Processing 'hello',2:

- stack is empty. depth=1.

- add 'hello' to all_nodes with depth 1.

- since k=2>0: push 2 to stack. stack is [2].

- then, check if stack is not empty: stack[-1] is 2. 2 !=0. So no popping.

- Then, stack is not empty (still [2]). So decrement stack[-1] by 1. stack becomes [1].

Wait, but in this case, the node is the parent. So after pushing 2 to the stack (because 'hello' has 2 children), the next step is to check if the parent (which is 'hello') has any remaining children. But 'hello' has 2 children, so after processing one child, the stack will be decremented.

Wait, perhaps my logic is inverted here.

Let me walk through the first example step by step.

Initial tokens list after split: ['hello', '2', 'ok', '0', 'bye', '0', 'test', '0', 'one', '1', 'two', '2', 'a', '0', 'b', '0']

Processing the first token pair 'hello', 2:

1. text='hello', k=2.

2. depth = len(stack) +1 =0+1=1.

3. all_nodes adds ('hello',1).

4. since k=2>0: stack.append(2). stack is now [2].

5. then, check if stack is not empty: yes. stack[-1] -=1 → becomes 1.

6. then, since stack[-1] is 1 (not zero), no popping.

So stack is [1]. i is now 2.

Next token pair: 'ok',0.

1. text='ok', k=0.

2. depth = len(stack) +1 =1 +1=2. Add (ok,2) to all_nodes.

3. k=0 → don't append anything to stack.

4. check if stack is not empty: yes. stack[-1] is 1. decrement by 1 → 0.

5. now, stack is [0].

6. enter loop: stack[-1] is 0 → pop. stack is empty.

7. check stack is now empty. loop ends.

i is now 4.

Next token pair: 'bye',0.

1. text='bye', k=0.

2. stack is empty → depth=0+1=1. Add (bye,1) to all_nodes.

Wait, but this is not correct. Because 'bye' is the second child of 'hello', which should be depth 2.

Hmm, this suggests that the algorithm is incorrect.

Wait, after processing 'hello', the stack is [2], which after decrement becomes [1].

Then, processing 'ok' (k=0):

- stack is [1].

- depth is 1 +1=2. correct.

- after processing 'ok', stack is [1], then stack[-1] is decremented to 0.

Then, stack is [0], which is popped, leaving stack empty.

So when processing 'bye', the stack is empty. So depth is 0+1=1. But 'bye' is a child of 'hello', so should be depth 2.

Ah, here's the problem. Because after processing 'hello' (text, k=2), the stack becomes [2]. Then, after processing 'hello', we decrement stack[-1] by 1 (to 1). But 'hello' is the root node. The next node is 'ok', which is the first child. So 'ok' is processed with stack [2]?

Wait, no. Let's re-examine the steps.

The 'hello' node:

After processing the node:

- stack is [2] (because k=2>0, so pushed).

- Then, check if stack is not empty → yes. stack[-1] is 2 → decrement by 1 → becomes 1.

So stack is [1].

Next, processing 'ok':

- stack is [1].

- depth is 1 +1=2.

- process 'ok', k=0. no stack append.

- check if stack is not empty → yes. stack[-1] (1) is decremented by 1 → 0.

- then, check if stack[-1] is 0 → yes. pop. stack is empty.

So after 'ok', stack is empty. So the next node (bye) is considered a root node.

But 'bye' is supposed to be the second child of 'hello', which is depth 2.

But according to the algorithm, 'bye' is processed with stack empty → depth 1. Which is wrong.

Ah, so the algorithm is incorrect. So there's a flaw in how the stack is managed.

What's the root cause here?

The problem is that after processing the first child ('ok') of 'hello', the stack for 'hello' is decremented to 1, then after processing 'ok', the stack becomes [1 → 0, then popped to empty]. So 'hello's remaining count is 1, but the stack is empty. So when processing 'bye', the algorithm thinks it's a root node, but it should be the second child of 'hello'.

Ah, this suggests that the way the stack is being managed is incorrect. Because when a parent has remaining children, but the stack is empty, the next nodes are not processed as children.

So the error is in the step where after processing a node, we decrement the parent's count, which may lead to the parent being popped from the stack even though there are more children to process.

For example, the 'hello' node has k=2 children. After processing the first child, 'ok', the stack was [1] (remaining 1 child). Then, when processing 'ok', after handling k=0, the code checks if stack is not empty (yes, [1]). So stack[-1] is 1. Then, we decrement by 1 to 0. Then, check if stack[-1] is 0. Pop it. So stack is now empty. So the parent 'hello's remaining count is 0. But 'hello' has another child to process (the 'bye' node).

This is the crux of the problem. The algorithm incorrectly pops the parent from the stack after processing the first child.

So the algorithm's logic for decrementing and popping is flawed.

Alternative approach: The stack should track the remaining children for each parent. When a parent's remaining count is decremented, but not popped until it reaches zero. But the parent's entry should remain on the stack until all its children are processed.

So perhaps the steps should be:

When processing a node:

1. The current depth is len(stack) +1.

2. Add to all_nodes.

3. if k>0:

   stack.append(k)

   (this is for the current node's children)

4. else:

   no action.

5. Then, check the stack. While the top of the stack is zero:

   pop it.

6. if the stack is not empty:

   decrement the top by 1.

But wait, when you process a node, you first handle its own children (k) by appending to the stack. Then, you check the stack for any parents that need to have their remaining count decremented.

Wait, perhaps the correct steps are:

After processing the node (text, k), which may have children (k>0), we append k to the stack if needed. Then, regardless of whether this node has children, we need to check if the previous parents have remaining children.

Wait, this is getting complicated. Let's think of the stack as a list of pending children counts for each parent.

Each time a node is processed, if it is a child of a parent, then the parent's count is decremented. However, the parent's count is tracked in the stack, but the current node's children (if any) are added to the stack after the parent's count is updated.

Wait, perhaps the correct approach is:

Each node can have children. For each node, after processing it (text, k), we add k to the stack (if k>0) to indicate that we need to process k children. Then, after that, we check if the current parent (the previous entry in the stack) has any remaining children. Wait, this may not work.

Alternative idea:

The stack holds the number of children that the current parent expects. When a new node is processed, it is a child of the parent in the stack (if stack is not empty). So, after processing the node's text and k, if there are children (k>0), the node becomes the new parent, and its expected children count is pushed onto the stack. Then, we decrement the previous parent's expected children count (if any). But this seems conflicting.

Alternatively, the stack can track the current number of children expected by each parent.

So, when we process a node:

1. The depth is len(stack) +1.

2. add to all_nodes.

3. if k>0:

   push k to the stack. (This node's children will be processed next.)

4. then, while stack is not empty and stack[-1] ==0:

   pop from stack.

5. if stack is not empty:

   stack[-1] -=1

Wait, let's try this.

Let's re-examine the first example step by step.

First node: 'hello', 2.

- depth=0+1=1. add to all_nodes.

- k=2>0: push 2 to stack. stack is [2].

- stack is not empty and stack[-1] is 2 !=0. so loop doesn't run.

- then, if stack is not empty: stack[-1] -=1 → becomes 1. stack is [1].

So stack is [1].

Next node: 'ok', 0.

- depth = len(stack)+1 =1+1=2. add to all_nodes.

- k=0 → no push to stack.

- check stack: [1].

- while stack[-1] ==0? No. so loop doesn't run.

- stack is not empty: decrement stack[-1] → 0. stack is [0].

- then, while stack and stack[-1] ==0 → pop. stack becomes empty.

So after processing 'ok', stack is empty.

Next node: 'bye',0.

- depth is 0+1=1. add to all_nodes. (This is wrong, 'bye' should be depth 2.)

But according to this algorithm, 'bye' is processed as a root node.

So this approach is incorrect.

Hmm, what's wrong here?

The problem is that after processing 'ok', the stack was [1], which was decremented to 0, and then popped. But the parent 'hello' had 2 children. The first child 'ok' was processed, but after that, the stack is emptied, so the second child 'bye' is processed as a root node.

So the algorithm is not properly tracking the parent's remaining children.

Ah, the problem is that when a parent's remaining children count is pushed to the stack, the stack is tracking the number of children expected, but after each child is processed, the count is decremented, and if it reaches zero, the parent is popped. But this leaves any remaining children of that parent to be processed as root nodes.

But that's not correct.

So the error is in the order of operations. When a parent has k children, the stack entry for that parent is k. Then, each time a child is processed (regardless of whether it is a child of that parent or a deeper parent), the parent's count is decremented.

But how to track which parent's count to decrement.

Ah, perhaps the stack should not be popped until all children of the parent are processed.

Wait, perhaps the stack is a list of tuples, where each tuple is (remaining_children, ...). But I'm not sure.

Alternative idea:

The stack should be a list of the number of children remaining for each parent. For example:

When processing a node:

1. The depth is len(stack) +1.

2. Add to all_nodes.

3. if k>0:

   push k to the stack. (This node's children will be processed next.)

4. else:

   while the stack is not empty:

       stack[-1] -=1

       if stack[-1] ==0:

           stack.pop()

       else:

           break

So, when a node has no children (k=0), we decrement the parent's count. If the parent's count becomes zero, we pop and continue decrementing the next parent.

But in the case where the node has children (k>0), we push k to the stack (so the next nodes are children of this node), and no decrement is done to the parent's count until all children of this node are processed.

Wait, perhaps this is the correct approach.

Let's test this.

First example:

Processing 'hello', 2.

1. depth 1. add to list.

2. k=2>0 → push 2. stack is [2].

3. no else part (since k>0).

4. So stack is [2].

Next node: 'ok',0.

1. depth len(stack)+1 =2. add to list.

2. k=0 → enter else.

3. while stack not empty:

   stack[-1] -=1 → 2-1=1.

   if 1 !=0 → break loop.

So stack is [1].

Next node: 'bye',0.

1. depth len(stack) +1=1+1=2. add to list.

2. k=0 → enter else.

3. while stack not empty:

   stack[-1] -=1 → 1-1=0.

   if stack[-1] ==0 → pop. stack becomes empty.

   loop continues → stack is empty, so loop breaks.

So after processing 'bye', stack is empty.

Next node: 'test',0.

1. depth 0+1=1. add to list.

2. k=0 → enter else.

3. stack is empty → loop doesn't run.

So stack remains empty.

Next node: 'one',1.

1. depth 0+1=1. add to list.

2. k=1>0 → push 1. stack is [1].

Next node: 'two',2.

1. depth len(stack)+1=2. add to list.

2. k=2>0 → push 2. stack is [1,2].

Next node: 'a',0.

1. depth 2+1=3. add to list.

2. k=0 → enter else.

3. while stack not empty:

   stack[-1] (2) is decremented to 1. → stack becomes [1,1].

   since 1 !=0 → break.

Next node: 'b',0.

1. depth len(stack)+1=2+1=3. add to list.

2. k=0 → enter else.

3. while stack not empty:

   stack[-1] (1) → 0. stack becomes [1,0].

   since stack[-1] is 0 → pop. stack becomes [1].

   now, stack is not empty. stack[-1] is 1 → decrement to 0.

   since 0 → pop. stack is empty.

So after processing 'b', stack is empty.

Next tokens: none.

This way, all nodes are processed with their correct depths.

In the first example, the nodes and depths would be:

hello →1

ok →2

bye →2

test →1

one →1

two →2

a →3

b →3

Which matches the expected output.

So this approach seems correct.

So the algorithm steps are:

For each node (text, k):

1. depth is len(stack) +1.

2. add to all_nodes.

3. if k >0:

   stack.append(k)

4. else:

   while stack is not empty:

       stack[-1] -=1

       if stack[-1] ==0:

           stack.pop()

       else:

           break

So, when a node has children (k>0), we push k to the stack. This indicates that the next k nodes are its children. But each child will be processed in sequence, and when they are processed, the stack will be updated.

When a node has no children (k=0), we need to decrement the parent's remaining children count. This is done by decrementing the top of the stack (if any) and popping if it reaches zero. If after popping, the new top is also zero, continue popping.

Let's test this algorithm with the first example.

Processing 'hello', 2:

- stack is empty. depth 1.

- push 2. stack [2].

- no else clause.

Processing 'ok', 0:

- depth is 2.

- else clause:

   stack[-1] -=1 → 2-1=1. stack [1].

   since 1 !=0, break.

Processing 'bye', 0:

- depth 2 (stack len 1 → 1+1=2).

- else clause:

   stack[-1] -=1 → 1-1=0. stack becomes [0].

   stack[-1] is 0 → pop. stack is empty.

Processing 'test',0:

- depth 1.

- else clause. stack is empty → loop not entered.

Processing 'one',1:

- depth 1.

- push 1. stack [1].

Processing 'two',2:

- depth 2.

- push 2. stack [1, 2].

Processing 'a',0:

- depth 3.

- else clause:

   stack[-1] (2) → 2-1=1. stack [1,1].

   break.

Processing 'b',0:

- depth 3.

- else clause:

   stack[-1] (1) → 0. stack [1,0].

   pop → stack becomes [1].

   stack[-1] is 1 → decrement to 0. stack [0].

   pop → stack empty.

So after all processing, all nodes are added with correct depths.

Yes, this seems to work.

So the algorithm is:

For each token pair (text, k):

   depth = len(stack) + 1

   add to all_nodes.

   if k>0:

       stack.append(k)

   else:

       while stack not empty:

           stack[-1] -=1

           if stack[-1] ==0:

               stack.pop()

           else:

               break

So this correctly manages the stack, and thus the depth of each node.

Now, the next step is to group the nodes by their depth. The nodes are added to all_nodes in the order they are parsed, which is pre-order (parents before children). So the order in the all_nodes list is the same as the order in the input. So grouping by depth and collecting the text in the order they appear in all_nodes will give the required output.

Once all nodes are parsed and grouped by depth, we can:

- Find the maximum depth.

- For each depth from 1 to max_depth, collect the texts of the nodes with that depth, in the order they appear in all_nodes.

So, after parsing, we can create a dictionary where keys are depths, and values are lists of texts. Then, for each depth from 1 to max_depth, output the list joined by spaces.

So, in code:

Parse the input into all_nodes (a list of (text, depth) tuples).

Create a dictionary, levels = defaultdict(list).

for text, depth in all_nodes:

   levels[depth].append(text)

max_depth = max(levels.keys()) if levels else 0.

print(max_depth)

for depth in range(1, max_depth+1):

   print(' '.join(levels[depth]))

Now, the parsing step needs to split the input into tokens and process them in pairs.

But the input can be up to 1e6 characters. So splitting by commas into a list can be memory-intensive. However, in Python, splitting by commas for a 1e6-length string should be manageable.

But let's think about the time and memory constraints. The input is split into a list of tokens. For example, a string with 1e6 characters may generate up to 5e5 tokens (since each token is at least one character). So the list would have up to 5e5 elements. This is acceptable.

So, the code steps:

Read the input string.

Split into tokens by commas.

Process the tokens in pairs: text, k.

Handle each pair as per the algorithm above.

Now, code:

But in Python, the code would look like this:

import sys
from collections import defaultdict

def main():
    s = sys.stdin.readline().strip()
    tokens = s.split(',')
    n = len(tokens)
    all_nodes = []
    stack = []
    i = 0
    while i < n:
        text = tokens[i]
        k = int(tokens[i+1])
        depth = len(stack) + 1
        all_nodes.append( (text, depth) )
        i += 2
        if k > 0:
            stack.append(k)
        else:
            # decrement parents
            while stack:
                stack[-1] -=1
                if stack[-1] == 0:
                    stack.pop()
                else:
                    break
    # group by depth
    levels = defaultdict(list)
    max_depth = 0
    for text, depth in all_nodes:
        levels[depth].append(text)
        if depth > max_depth:
            max_depth = depth
    print(max_depth)
    for d in range(1, max_depth+1):
        print(' '.join(levels[d]))

if __name__ == "__main__":
    main()

But wait, what if there are no nodes? The problem states that each comment is a non-empty string, and the input is guaranteed to be valid. So there's at least one node.

Testing this code with the first example:

Input: hello,2,ok,0,bye,0,test,0,one,1,two,2,a,0,b,0

The all_nodes list after parsing will be:

('hello',1), ('ok',2), ('bye',2), ('test',1), ('one',1), ('two',2), ('a',3), ('b',3)

Grouping:

depth 1: ['hello', 'test', 'one']

depth 2: ['ok', 'bye', 'two']

depth 3: ['a', 'b']

max_depth=3.

Output is:

3

hello test one

ok bye two

a b

Which matches the first example.

Another test case: the second example.

Input: a,5,A,0,a,0,A,0,a,0,A,0

Tokens: ['a', '5', 'A', '0', 'a', '0', 'A', '0', 'a', '0', 'A', '0']

Processing:

i=0:

text='a', k=5.

depth=0+1=1.

push 5 to stack. stack [5].

i +=2 → 2.

i=2:

text='A', k=0.

depth=1+1=2.

append (A,2).

k=0.

enter else:

decrement stack[-1] (5-1=4). stack [4]. break loop.

i +=2 →4.

text='a', k=0.

depth=1+1=2.

append (a,2).

k=0.

decrement stack[-1] to 3. stack [3]. break.

i=6: text='A',0. append (A,2).

decrement stack to 2. break.

i=8: text='a',0. append (a,2). decrement to 1. break.

i=10: text='A',0. append (A,2). decrement to 0. stack becomes [0].

Loop:

stack[-1] is 0 → pop. stack is empty.

So after processing all tokens:

all_nodes is:

('a',1), ('A',2), ('a',2), ('A',2), ('a',2), ('A',2)

levels:

depth 1: ['a']

depth 2: ['A', 'a', 'A', 'a', 'A']

max_depth=2.

Output:

2

a

A a A a A

Which matches the second example.

Third example input:

A,3,B,2,C,0,D,1,E,0,F,1,G,0,H,1,I,1,J,0,K,1,L,0,M,2,N,0,O,1,P,0

Processing this would require careful steps, but the code should correctly parse the nodes and depths.

The output is 4.

The code should correctly group the nodes.

Thus, the code seems correct.
</think>

```python
import sys
from collections import defaultdict

def main():
    s = sys.stdin.readline().strip()
    tokens = s.split(',')
    n = len(tokens)
    all_nodes = []
    stack = []
    i = 0
    while i < n:
        text = tokens[i]
        k = int(tokens[i+1])
        depth = len(stack) + 1
        all_nodes.append((text, depth))
        i += 2
        if k > 0:
            stack.append(k)
        else:
            while stack:
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                else:
                    break
    levels = defaultdict(list)
    max_depth = 0
    for text, depth in all_nodes:
        levels[depth].append(text)
        if depth > max_depth:
            max_depth = depth
    print(max_depth)
    for d in range(1, max_depth + 1):
        print(' '.join(levels[d]))

if __name__ == "__main__":
    main()
```