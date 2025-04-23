<think>
Okay, I need to solve this problem where I have to repeatedly merge consecutive equal elements until there are no more such pairs. The key is to find an efficient way to process this, especially since the input size can be up to 2e5 elements. Let me think about how to approach this.

First, the brute force approach would be to process each pair step by step. But with n up to 2e5, that's not feasible. Each merge could potentially create a new pair that needs to be processed, and in the worst case, like the second example where all elements are the same, the number of operations would be O(n), which would be 2e5 steps, each requiring O(n) time. That's O(n^2), which is 4e10 operations—way too slow. So I need a smarter approach.

Hmm. Let's think about the data structure. What if we can model this process in a way that allows us to merge elements and check for possible new merges efficiently? A stack-based approach comes to mind. Let me consider using a stack where each element keeps track of the current value and possibly the count or something else.

Wait, the problem requires that whenever there's a pair of equal consecutive elements, we merge them, replacing them with x+1. But merging two elements might cause the new element to be equal to its left neighbor. For example, in the sequence [2, 2, 2], first merge the leftmost two into a 3, resulting in [3, 2]. Then no merge. But another scenario: [3, 3, 3]. The first merge becomes [4,3], then no merge. Wait, but in that case, merging the first two creates 4, which isn't equal to the next 3.

Wait, but maybe after merging a pair, the newly inserted x+1 could form a new pair with the previous element. For example, if we have [1,1,1,1], first merge the first two into 2, making [2,1,1]. Then the next pair is the two 1s, merge into 2, resulting in [2,2], which then merges into 3. So the stack approach would need to handle this.

So here's the idea: use a stack to keep track of the elements. When adding a new element, check if it's equal to the top of the stack. If so, pop the top, merge them (x+1), and then check again if this new value equals the new top. Repeat this process until the top of the stack is different or the stack is empty.

Wait, but merging can only happen once per step. Wait no. Wait the operation is to find the leftmost pair. So when you merge a pair, you replace them with x+1, which might create a new pair that is to the left of any other possible pairs. So you have to process that new pair immediately.

For example, in the sequence [2,2,2], the first two merge into 3, making [3,2]. But the next step would have no pairs, so the stack approach would work here.

Another example: [2,2,2,2]. The process would be:

- merge first two into 3, stack is [3,2,2]. Then check if the new top (3) equals next (2). No. Then process the next pair, 2 and 2. Merge into 3, stack becomes [3,3]. Then check if those two are equal. Merge into 4. So the stack approach would correctly handle this.

So the stack approach seems to work. Let's think of the algorithm:

Initialize a stack.

For each element in the input array:

    While the top of the stack is equal to the current element:

        Pop the top element, increment by 1, set current element to this new value.

        Repeat this until the top is different or stack is empty.

    Push the current element onto the stack.

Wait, but let's test this with the first example.

First example input: 5, 2, 1,1,2,2.

Processing each element:

- 5: stack is empty, push 5. Stack: [5]

- 2: push 2. Stack: [5,2]

- 1: push 1. Stack: [5,2,1]

- Next element is 1. Now, top is 1. Pop, increment to 2. Now, current element is 2. Check stack top. Now stack is [5,2]. Top is 2, which equals current element 2. So pop 2, increment to 3. Now current is 3. Check top, 5 is different. Push 3. Stack becomes [5,3].

Wait, but in the original example, after merging the two 1s into 2, the next elements are 2,2. So the stack after merging 1 and 1 into 2 would be [5,2,2], which then would merge into 3, but the original example after first operation is [5,2,2,2,2]. Hmm, perhaps my initial approach is not capturing the entire process correctly.

Wait, perhaps the stack approach is not sufficient because when merging elements, the new element is inserted in place of the original pair. So when we process the elements, the merging can affect elements that are before the current position.

Wait, the problem says that each operation finds the leftmost pair. So after merging a pair, the next possible pair is determined again by the entire sequence.

The stack approach may not capture this, because it processes elements in a left-to-right manner and merges as they are added. Let me think again.

Alternative approach: Imagine that whenever you process an element, you check if it's the same as the top of the stack. If so, merge them (i.e., increment and replace the top with x+1). But after merging, this new value could be equal to the new top, so we have to check again.

Wait, this seems to model exactly the process of merging leftmost pairs. Because when processing elements in order, the stack represents the merged elements so far. So any new merge would only happen with the previous elements, which are on the stack. So this approach might work.

Let's walk through the first example step by step.

Original input: 5, 2, 1,1,2,2.

Processing:

element 5: stack is empty. Push 5. Stack: [5]

element 2: top is 5. Not same. Push 2. Stack: [5,2]

element 1: top is 2. Push 1. Stack: [5,2,1]

element 1: top is 1. Pop, merge into 2. Now current is 2. Check stack top (2). So pop 2, merge into 3. Check stack top (5). Push 3. So after this step, stack is [5,3]. Then next element is 2.

element 2: stack top is 3. Push 2. Stack: [5,3,2]

element 2: stack top is 2. Pop, merge into 3. Check stack top is 3. Pop, merge into 4. Check stack top is 5. Push 4. Final stack is [5,4], which matches the first example.

Yes! So the stack approach works here.

Another test case: the second example.

Input: four 1e9.

Processing:

element 1e9: push.

element 1e9: top is same. Merge into 1e9+1. Now current is 1e9+1. Check stack (empty). Push.

element 1e9: stack top is 1e9+1. Not same. Push. Wait, but the original input is four 1e9. Let's see:

Wait, original input is [1e9, 1e9, 1e9, 1e9]. Let's process each element:

element 1: 1e9. Push.

element 2: 1e9. Top is same. Merge into 1e9+1. Now current is 1e9+1. Stack is empty, push.

element 3: 1e9. Stack top is 1e9+1. Not same. Push. Now stack is [1e9+1, 1e9].

element 4: 1e9. Top is 1e9. Merge into 1e9+1. Now current is 1e9+1. Stack now has [1e9+1], so check again. Pop, merge into 1e9+2. Push. So stack is [1e9+2]. Which is correct.

So the stack approach works here as well.

Third example: no consecutive duplicates. So the stack will just push each element, and no merges happen. So the output is the same as input.

So the stack approach seems to model the merging process correctly. Now the question is, how to implement this efficiently in Python.

The stack can be a list. For each element in the input, we process it as follows:

- current_val = element

- while stack is not empty and stack[-1] == current_val:

    pop the stack, current_val += 1

- append current_val to the stack.

This is O(n) time. Because each element is pushed once and popped at most once. Because for each element, the number of merges is the number of times it's part of a merge. Each merge increases the value, and each time a merge happens, the current_val increases. So for example, merging two elements x into x+1 can only happen once for each x. So the total number of operations is O(n), since each element is processed once, and each merge reduces the total count by 1.

Wait, perhaps the stack approach is O(n) in total. For example, in the worst case where all elements are 1 and n is a power of 2. Then after each merge, the number of elements halves. But the stack approach would process each element, merging as needed. But each element is pushed once and possibly merged a few times. However, each merge step (the while loop) could take O(1) amortized time. Let me see:

Each element is pushed once. Then, each time a merge happens, a pop occurs. So each element can be involved in at most log(max_value) merges. Wait, but the maximum possible value after merges is up to 1e9 + log2(2e5) (since each merge increases the value by 1). But the number of possible merges per element is limited by how many times it can be merged with the next elements.

But in the stack approach, each element is processed once. For example, once merged, the new value is added to the stack and may cause a new merge. But the while loop ensures that each time, the current value is compared with the top of the stack. So each element is processed in O(1) steps on average.

Wait, let's consider that each merge reduces the number of elements. However, in the stack approach, each element is processed once. For example, if you have a chain of k elements of the same value, the stack approach will process them in O(k) time. But since each merge reduces the count by 1, the total number of operations is O(n), because each element can be merged at most once. Wait, not sure. Let me think: For each element in the input, how many times is it involved in the while loop?

Suppose we have an element that is pushed to the stack. Then, when processing the next element, it may trigger a merge. Once merged, the new value is added, which may cause another merge. But each time, the current value is increased, so it can't merge again unless the next element (after processing) is equal to it. But the key is that each element is processed in O(1) amortized time. So the total time is O(n).

Therefore, the stack approach is O(n) time, which is acceptable for n up to 2e5.

So the plan is:

- Read n and the list of elements.

- Initialize a stack.

- For each element in the list:

   - current_val = element

   - while the stack is not empty and stack[-1] == current_val:

       - pop the last element from the stack

       - current_val += 1

   - append current_val to the stack.

- Finally, output the stack.

This seems correct. Let me test this logic against the examples.

First example:

Input sequence: 5,2,1,1,2,2.

Processing:

5: stack is empty, push. stack = [5]

2: not equal to 5. Push. stack = [5,2]

1: not equal to 2. Push. stack = [5,2,1]

1: stack[-1] is 1. Pop, current_val becomes 2. Now, check stack[-1] (2). Equal to 2. Pop, current_val becomes 3. stack is now [5]. Push 3. stack = [5,3].

Next element is 2: stack[-1] is 3. Push. stack = [5,3,2].

Next element is 2: stack[-1] is 2. Pop, current_val becomes 3. stack is now [5,3]. stack[-1] is 3. Equal to current_val. Pop, current_val becomes 4. stack is [5]. Push 4. stack = [5,4]. Which matches the example.

Second example:

Input is four 1e9.

Processing first 1e9:

stack is empty. Push. stack = [1e9]

Second 1e9: equal to stack top. Pop, current_val is 1e9+1. stack is empty, push. stack = [1e9+1]

Third 1e9: stack top is 1e9+1. Not equal. Push. stack = [1e9+1, 1e9]

Fourth 1e9: stack top is 1e9. Pop, current_val becomes 1e9+1. stack is [1e9+1]. Now, current_val is 1e9+1, which is equal to stack top. Pop, current_val becomes 1e9+2. stack is empty. Push. stack = [1e9+2]. Correct.

Third example: no consecutive duplicates.

The stack would push each element, since no two consecutive are same. So output is same as input.

So this approach works for all the examples.

Now, in Python, implementing this is straightforward. However, since n can be up to 2e5, the code needs to be efficient. The stack operations in Python are O(1), and appending and popping from the end of a list is efficient.

Thus, the code would look something like this:

Read n.

Read the list of a's.

Initialize stack.

Loop over each element in a:

   current = element

   while stack and stack[-1] == current:

       current += 1

       stack.pop()

   stack.append(current)

Then, output the length and the elements.

Yes. Let's code this.

But wait, the problem says that when merging a pair, the new element is inserted in the position of the original pair, which could create a new pair with the previous element. The stack approach correctly handles this, because after merging, the new current_val is checked against the new top of the stack. So any possible merges to the left are handled by the while loop.

Yes. So the code should work.

Testing edge cases, such as when merging leads to multiple merges. Like [2,2,2,2]. The code would process each element:

First 2: push.

Second 2: stack[-1] is 2. Pop, current becomes 3. stack is empty. Push 3. Then third element is 2. stack[-1] is 3. Push. stack becomes [3,2]. Fourth element is 2. stack[-1] is 2. Pop, current becomes 3. stack is [3], stack[-1] is 3. Pop, current becomes 4. Push. So stack is [4]. Correct.

Another test case: [3,3,3,3]. Processing:

First 3: pushed.

Second 3: merged to 4. stack becomes [4].

Third 3: pushed. stack [4,3].

Fourth 3: merged to 4. stack becomes [4,4]. Then merged to 5. So final stack [5]. Correct.

So the code works.

Thus, the Python code should be:

Read n.

Read list.

Initialize stack = [].

For num in list:

    current = num

    while stack and stack[-1] == current:

        current += 1

        stack.pop()

    stack.append(current)

Then print len(stack) followed by the elements.

Yes. That's the code.

Now, considering that the input can be up to 2e5 elements. Reading the input via input().split() and converting to integers. But for large n, that's acceptable.

In Python, for speed, it's better to read via sys.stdin. But for code submission, sometimes using input() is acceptable, but for very large data, sys.stdin is faster. However, given the time constraints (1 second per test), using input().split() may be sufficient. Let's check:

For n=2e5, each element is an integer. So the input line would be 2e5 numbers, which is manageable. Using split() and converting to a list of integers would take O(n) time, which is acceptable.

So code:

n = int(input())

a = list(map(int, input().split()))

stack = []

for num in a:

    current = num

    while stack and stack[-1] == current:

        current += 1

        stack.pop()

    stack.append(current)

print(len(stack))

print(' '.join(map(str, stack)))

This should work.

Testing with the first example:

Input:

6

5 2 1 1 2 2

Processing:

stack starts empty.

Process 5 → stack [5]

Process 2 → [5,2]

Process 1 → [5,2,1]

Process 1:

current =1.

stack[-1] is 1. Pop, current=2. Then stack is [5,2]. stack[-1] is 2. Pop, current=3. stack is [5]. Append 3.

Process 2 → stack becomes [5,3,2]

Process 2:

current=2. stack[-1] is 2. Pop, current=3. stack becomes [5,3]. stack[-1] is 3. Pop, current=4. stack [5]. Append 4. Final stack is [5,4]. Correct.

Another test case: input of four 1e9.

Processing:

stack starts empty.

Process first 1e9: stack [1e9]

Second 1e9: current becomes 1e9+1, stack empty. Append.

Third 1e9: stack [1e9+1], append 1e9. stack [1e9+1, 1e9]

Fourth 1e9: current=1e9. stack[-1] is 1e9. Pop, current=1e9+1. stack [1e9+1]. stack[-1] is 1e9+1. Pop, current=1e9+2. Append. Final stack [1e9+2]. Correct.

Third example: the code outputs the same elements. Correct.

Thus, the code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
stack = []
for num in a:
    current = num
    while stack and stack[-1] == current:
        current += 1
        stack.pop()
    stack.append(current)
print(len(stack))
print(' '.join(map(str, stack)))
```