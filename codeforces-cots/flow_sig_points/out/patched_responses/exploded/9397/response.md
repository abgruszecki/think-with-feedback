<think>
Okay, let's tackle this problem. So the task is to simulate the behavior of the 'cd' and 'pwd' commands in a shell. We need to process a series of commands and output the correct absolute path whenever 'pwd' is called. 

First, I need to understand the requirements thoroughly. The key points here are handling both absolute and relative paths correctly. Let's break down the problem.

The current directory starts as the root '/'. When a 'cd' command is given, the path can be absolute (starting with '/') or relative. For absolute paths, we split them into components and process each part. For relative paths, we start from the current directory. Each component could be a directory name, which we add to the current path, or '..', which takes us up one level. Also, the problem states that there's no attempt to go above the root, so we don't have to handle that case.

So the main challenge is correctly parsing and handling the paths. Let's think about the data structure to represent the current path. Since we need to handle directories in a hierarchical way, a stack (like a list in Python) would be suitable. The stack would contain the directory names in order from root to current. For example, if the path is '/home/vasya', the stack would be ['home', 'vasya']. Then, when we 'cd ..', we pop the last element.

For absolute paths, we split the path into components, ignoring empty strings caused by leading or trailing slashes. For example, '/a/b/' would split into ['a', 'b'] (assuming we split on '/'), but we need to process each part. If the path starts with '/', we reset the current directory to the root and then process each component. For relative paths, we process each component starting from the current directory.

Parsing the path correctly is crucial. Let's think about the steps:

1. When a 'cd' command is received, parse the path.
2. If the path starts with '/', it's absolute. So we reset the current directory to root (empty stack?), but wait: the root is represented by an empty stack. Because when we build the path, each element in the stack is a directory name. For the root, the stack is empty, and the pwd output is '/'.
Wait, no. Wait, if the stack is empty, then the absolute path is '/'. So, for example, after 'cd /', the stack is empty. Then when 'pwd' is called, we output '/'.

Wait, maybe the stack should represent the directories after the root. So the root is the base, and the stack holds the directories in order. So, for the root, the stack is empty. So when we process a path, like 'home/vasya', the stack becomes ['home', 'vasya'], and the absolute path is '/home/vasya/'.

So the stack approach works. Each element is a directory name. When we process a component, if it's a directory name, we append it. If it's '..', we pop the last element (but only if the stack is not empty, but the problem states that we don't have to handle going beyond the root).

So the algorithm steps would be:

For each command:

- If it's 'pwd', output '/' followed by the stack elements joined with '/', followed by a '/'.
- If it's 'cd', process the path:
   a. Split the path into parts. For example, 'a/b/c' becomes ['a', 'b', 'c'].
   b. Determine if the path is absolute (starts with '/'). If so, reset the stack to empty, and process each part (ignoring the initial empty string from splitting on '/').
   c. For relative paths, split the current path (the stack) and process each part from the given path.

Wait, but how to split the path into components? Let's take an example. The path could be something like 'a/../../b' which, when split, would be ['a', '..', '..', 'b'], but as a relative path. Processing each component step by step:

Starting from current stack, say ['home', 'vasya'], processing 'a' would push 'a', then '..' would pop 'a', then another '..' would pop 'vasya', leading to ['home'], then push 'b' → ['home', 'b'].

But how to split the path into components correctly?

The splitting needs to split on '/' but ignore empty parts. For example, the path '/a/b/c' would split into ['a', 'b', 'c'], but leading slash indicates absolute path. The path 'a/b/c/' would split into ['a', 'b', 'c', ''] → but according to the problem statement, the parameter for 'cd' does not end with a slash except when it's the root. So in the input, the 'cd' command's parameter ends with a slash only if it's the root. So in code, when splitting, we can split on '/', filter out any empty strings, then process each component.

Wait, but for the case of absolute path '/', the split would result in [''] (after splitting by '/'). So for absolute path, if the path is '/', then after splitting, we get [''] → which after filtering empty strings becomes empty. So processing an absolute path '/' would reset the stack to empty, then process the components (none), so stack remains empty. Which is correct.

So the plan for splitting a path:

- If the path starts with '/', it's absolute. So we split the path into parts by splitting on '/'. Then, for each part, if it's non-empty, add to a list. Then reset the stack to empty and process each part (so for example, '/a/b' → split into ['a', 'b'], then stack becomes empty, then process 'a' → append, then 'b' → append → stack is ['a', 'b'].

- For a relative path (doesn't start with '/'), split the path into parts by splitting on '/', filter out empty strings, then process each part in order. For each part, if it's '..', pop the last element (if possible, but problem says we don't have to handle cases where stack is empty and trying to pop). Else, append the part.

So code steps for processing a 'cd' command:

Parse the path parameter.

If it's absolute (starts with '/'):

   Split the path into components by splitting on '/', filter out empty strings. Then reset the stack to empty. Then process each component as per '..' or directory name.

Else (relative path):

   Split into components (same way). Then for each component in order, process each (push or pop).

So for example, the path 'vasya/../petya' would split into ['vasya', '..', 'petya']. Processing each:

- 'vasya' → append → stack becomes [..., 'vasya']
- '..' → pop → stack becomes [ ... ] (without 'vasya')
- 'petya' → append → stack becomes [ ..., 'petya']

Thus, the correct path is built.

Now, considering the constraints. The maximum n is 50, and each command can have up to 200 characters. So even if we process each command with O(k) time where k is the number of components (split into parts), it's acceptable. Since for each command, the split is O(length of path), which is up to 200, and each component processed in O(1) (append or pop), the total time is negligible. So this approach is feasible.

Now, the data structure for the current directory stack can be a list in Python, where appending and popping from the end (which is O(1) time) is efficient.

So the steps in code:

Initialize a stack (list) as empty.

For each command:

   If it's 'pwd', output '/' + '/'.join(stack) + '/' (if stack is empty, output '/').

   Else (cd with path):

      Parse the path.

      If path starts with '/', process as absolute:

          parts = path.split('/')[1:] → but split would split into ['', ...]. So maybe split on '/' then filter out empty strings.

          components = list(filter(None, path.split('/'))) → this gives all non-empty parts. For example, '/a/b' → split into ['', 'a', 'b'], filter → ['a','b'].

          Then, reset the stack to empty.

          Then, process each component in components:

              for part in components:

                  if part == '..':

                      stack.pop()

                  else:

                      stack.append(part)

      Else (relative path):

          components = list(filter(None, path.split('/'))) → split on '/' and filter out empty.

          for part in components:

              if part == '..':

                  stack.pop()

              else:

                  stack.append(part)

Wait, but in the case of a relative path like '../../a', the components would be ['..', '..', 'a']. Processing each part:

First '..' → pop (but stack is initially empty? Wait, no. The problem says that all transitions are valid. So in the input, the 'cd' commands will not try to go above the root. So when processing components in a relative path, each '..' can be popped as the stack will not be empty. So we can safely pop.

But according to the problem statement, "It is guaranteed that there is no attempt of transition to the parent directory of the root directory." So no need to handle cases where after popping, stack becomes empty and then another '..' is processed. So we can safely process each '..' by popping the last element.

Thus, the code can proceed as above.

Now, testing with the examples.

First example input:

7 commands:

1. pwd → output '/'

2. cd /home/vasya → absolute path.

Split into ['home', 'vasya'], stack becomes ['home', 'vasya']

3. pwd → output '/home/vasya/'

4. cd .. → relative path. Split into ['..'], pop → stack becomes ['home']

5. pwd → '/home/'

6. cd vasya/../petya → relative path. Split into ['vasya', '..', 'petya']

Processing:

append 'vasya' → ['home', 'vasya']

then '..' → pop → ['home']

then append 'petya' → ['home', 'petya']

7. pwd → output '/home/petya/'

Which matches the example.

Second example:

4 commands:

cd /a/b → absolute. stack becomes ['a', 'b']

pwd → /a/b/

cd ../a/b → relative. components ['..','..', 'a', 'b'] → wait, no. The path is '../a/b' → split into ['..', 'a', 'b']

Processing:

stack is ['a', 'b'].

Process '..' → pop → ['a']

Process 'a' → append → ['a', 'a']

Process 'b' → append → ['a', 'a', 'b']

So pwd outputs '/a/a/b/'

Which matches the sample.

So the code seems to handle these cases.

Now, the code implementation.

In Python, the stack can be a list. For each 'cd' command, process the path as follows.

Let's code the steps.

Read n, then loop n times.

For each line:

split into parts. For 'pwd', output. For 'cd', take the path.

So:

import sys

n = int(input())

stack = []

for _ in range(n):
    parts = input().split()
    if parts[0] == 'pwd':
        if not stack:
            print('/')
        else:
            print('/' + '/'.join(stack) + '/')
    else:
        # cd command
        path = parts[1]
        if path.startswith('/'):
            # absolute path
            components = list(filter(None, path.split('/')))
            stack.clear()
            for part in components:
                if part == '..':
                    stack.pop()
                else:
                    stack.append(part)
        else:
            # relative path
            components = list(filter(None, path.split('/')))
            for part in components:
                if part == '..':
                    stack.pop()
                else:
                    stack.append(part)

Wait, but wait: in the case of an absolute path, the split could have parts. For example, path is '/a/../b'. Split into ['a', '..', 'b']. Then, processing each part:

After stack is cleared, append 'a', then '..' → pop 'a', stack empty, then append 'b' → stack is ['b'].

Thus, the absolute path is /b/ when pwd is called. Which is correct.

Another example: cd / → path starts with '/', components is empty (split is ['', ...], filtered to empty). So stack is cleared (now empty), and processing no components. So stack remains empty. Then pwd outputs '/'.

That's correct.

Another edge case: cd a → relative path. components is ['a']. stack appends 'a' → stack is ['a']. pwd outputs '/a/'.

Another edge case: cd a/b/c → components ['a', 'b', 'c']. stack appends all. pwd outputs '/a/b/c/'.

What about a command like 'cd ../x/y' when current stack is ['a', 'b', 'c']? So components are ['..', 'x', 'y']. Process:

pop → stack ['a', 'b'], append 'x' → ['a', 'b', 'x'], append 'y' → ['a', 'b', 'x', 'y']. So pwd would be '/a/b/x/y/'.

Yes.

So the code seems correct.

Now, for the output: when stack is empty, output '/'. Otherwise, output '/' + '/'.join(stack) + '/'.

Yes.

Testing this with the examples.

First example:

After first 'cd /home/vasya', stack is ['home', 'vasya'].

pwd → /home/vasya/

After 'cd ..', stack becomes ['home'] → pwd outputs '/home/'.

After 'cd vasya/../petya', components are ['vasya', '..', 'petya']. Relative path:

Process 'vasya' → stack becomes ['home', 'vasya'], then '..' → ['home'], then 'petya' → ['home', 'petya'].

pwd → '/home/petya/'.

So code works.

So the code should handle all cases correctly.

Now, some possible optimizations. Since the constraints are small (n up to 50, each command up to 200 chars), the code is efficient enough. However, using split and filter is O(k) for each path, which is acceptable.

Thus, the code should be correct.
</think>

```python
n = int(input())
stack = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'pwd':
        print('/' + '/'.join(stack) + '/' if stack else '/')
    else:
        path = cmd[1]
        if path.startswith('/'):
            components = list(filter(None, path.split('/')))
            stack.clear()
            for part in components:
                stack.pop() if part == '..' else stack.append(part)
        else:
            for part in filter(None, path.split('/')):
                stack.pop() if part == '..' else stack.append(part)
```