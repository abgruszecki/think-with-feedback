<think>
Okay, let's tackle this problem. So, the problem is about psychos killing their right neighbor in steps until no more killings happen. We need to find out how many steps that takes. Hmm.

First, let's understand the process. Each step, every psycho that has a higher ID than their right neighbor kills them. But the killing happens simultaneously. So, even if a psycho is killed in the same step, their left neighbor might have already killed someone. Wait, but if a psycho is killed, they can't participate in killing others in the same step. Oh right, because the killings are all done in the same step. So, the order of processing matters. Because if a psycho is killed, they can't be part of any killing during that step.

So the main challenge is to model this process efficiently. Because if we try to simulate each step by checking each psycho every time, it's going to be O(n^2) in the worst case, which won't work for n up to 1e5. So we need a smarter approach.

Let's think about when a psycho gets killed. For a psycho at position i, when does he get killed? It's when the psycho to his left (i-1) has a higher ID than him, but only if that left neighbor wasn't killed in the previous steps. Wait, no. Because the killing happens in steps. So in each step, all psychos that have a higher right neighbor are marked to kill. Then, after all these are processed, the killed psychos are removed. So the key is that each psycho can only be killed once, and the order in which they are killed affects the steps.

Another approach: For each psycho, determine when he will be killed. Then, the maximum of these times across all psychos is the answer. Because the number of steps required is the maximum number of steps any psycho is present in before being killed.

But how to compute the time each psycho is killed. Let's see.

For example, take the first sample input:

10 9 7 8 6 5 3 4 2 1

In the first step, all psychos who are higher than their right neighbor kill them. Let's list them:

10 >9 → kill 9.

9's right is 7, but 9 is killed in the same step, so maybe 7's killer is not considered? Wait, no. Wait, in the first step, all psychos that have a right neighbor with a lower ID are active. So for each pair (i, i+1), if a[i] > a[i+1], then i will kill i+1. But if i is killed in this step, then perhaps their killing action still happens. Because all killings are processed in parallel.

Wait, the killing is done in the same step. So during the step, for all psychos, if their right neighbor exists and their ID is higher, then the right neighbor is marked to be killed. Then, after all these marks are made, all marked psychos are removed at once. So even if a psycho is killed, their action of killing their right neighbor still happens in that step.

So in the first step:

Original array: [10,9,7,8,6,5,3,4,2,1]

Check each psycho:

- 10 >9 → mark 9 to be killed.
- 9's right is 7, but 9 is marked to be killed. But during this step, the 9 is still part of the array until the end of the step. So 9 kills 7 (since 9>7). So 7 is marked.
- 7's right is 8. 7 is not marked (since in this step, the check is before any removal), so 7<8 → no kill.
- 8>6 → mark 6.
- 6>5 → mark5.
-5>3 → mark3.
-3<4 → no.
4>2 → mark2.
2>1 → mark1.

So all marked psychos (9,7,6,5,3,2,1) are removed. Wait, but wait, the initial array is 10,9,7,8,6,5,3,4,2,1.

Wait, during step 1:

Each psycho checks their right. Let's go through each position:

Positions 0-9 (0-based):

0 (10) → right is 9 (position 1). 10>9 → mark position1 (9) to be killed.

Position1 (9) → right is 7 (position2). 9>7 → mark position2 (7) to be killed.

Position2 (7) → right is 8 (position3). 7<8 → no.

Position3 (8) → right is 6 (position4). 8>6 → mark4.

Position4 (6) → right is5 → 6>5 → mark5.

Position5 (5) → right is3 →5>3 → mark6.

Position6 (3) → right is4 →3<4 → no.

Position7 (4) → right is2 →4>2 → mark8.

Position8 (2) → right is1 →2>1 → mark9.

So the marked positions are 1,2,4,5,6,8,9.

Wait, that's 9,7,6,5,3,2,1. Wait the elements at positions 1 (9), 2 (7), 4 (6),5 (5),6 (3),8 (2),9 (1). So after removing all these elements, the array becomes [10,8,4]. Because the surviving elements are those not marked. Let's see:

Original array indices 0:10 (survives), 3:8 (since 3 is not marked?), wait no. Wait the marked positions are the ones to be killed. So when we process the array after the step, we need to collect the elements that are not marked. So the survivors are the elements at positions 0 (10), 3 (8), 7 (4). Because positions 1,2,4,5,6,8,9 are marked. So the new array is [10,8,4].

Then step 2:

In this array, 10>8 → mark8 (position1). 8's right is4. 8>4 → mark4 (position2). So in this step, positions1 and 2 are marked. After removal, the array becomes [10]. So step 2 is the last step. Then step 3, there's nothing to kill. So total steps are 2.

So the answer is 2.

So each step, all the elements that are to be killed are marked based on their current neighbors (the array before any removal in that step). Then all marked elements are removed, and the array is updated. Then the next step starts with the new array.

Now, the problem is to model this process and find the number of steps required until no more killings happen.

But for n up to 1e5, simulating each step by checking each element in the array step by step is O(n^2) in the worst case. For example, if the array is in decreasing order, each step removes all elements except the first one. But if the array is like [n, n-1, ...,1], then step 1 removes all except n. So that's O(1) steps. Hmm, but other cases may require O(n) steps. Wait, no. Let's think: How many steps could there be?

Each step reduces the array by some amount. For example, in the worst case, each step could remove about half the elements. But how?

Alternatively, each element can be killed in a certain step. The maximum step number in which any element is killed is the answer.

So perhaps the approach is to determine for each element the step in which it is killed, then take the maximum of those steps.

So how to compute this step for each element.

Let's model the elements as a linked list. Each element has a left and right neighbor. When an element is killed, its left and right are updated. But this might be tricky.

Alternatively, we can process the elements and for each element, track when it will be killed, based on the elements around it.

Another idea: For each element, the step when it is killed is the earliest step when either its left neighbor is larger than it, or its right neighbor is smaller than it. Wait, no. Because the killing is based on the left neighbor in the current step.

Wait, an element is killed if it is the right neighbor of a larger element. So during some step, the element's left neighbor (in the current arrangement) is larger than it. Then that element will be killed in that step.

But the arrangement changes each step as elements are removed. So perhaps the order in which elements are removed affects when other elements are killed.

Hmm, but perhaps we can model the steps for each element by considering the order in which elements are killed.

Another approach is to note that for an element to be killed in step k, it must have a left neighbor in the previous step's array that is larger than it. But the left neighbor must also have survived until the previous step.

Wait, let's think recursively. Let's consider the elements and their death steps.

For example, in the first sample, 9 is killed in step 1, 8 is killed in step 2.

Let's think for each element when it dies.

An element can be killed in step s if, in the (s-1)th step's array, it is the right neighbor of a larger element.

So, for each element, the death step is determined by the earliest step where the left neighbor in the current array is larger than it.

But how to track this efficiently.

Let's think of each element's death time. Let's create an array death_step of size n, where death_step[i] is the step when the element a[i] (original array) is killed. If it's not killed, death_step[i] is 0 (or some default).

Initially, all elements are alive. For each step, the elements that are killed are those that have a left neighbor (in the current arrangement) larger than them.

Wait, but the left neighbor in the current arrangement depends on which elements have been killed in previous steps. So the arrangement is dynamic, and the order in which elements are removed affects the death steps of other elements.

This seems complex, but perhaps there's a way to model it using a linked list structure, where each element keeps track of its neighbors, and for each element, we can track the earliest step it can be killed based on the neighbors.

Alternatively, let's process the elements in the order of decreasing death steps. For example, elements that are killed first are those that are to the right of a larger element in the initial array.

Wait, perhaps the key is to process the elements in the initial array, and for each element, determine when it will be killed based on its neighbors. But how.

Let's consider the elements in the original array. For each element a[i], the earliest it can be killed is in the first step if a[i-1] > a[i]. But in some cases, a[i-1] might be killed before step 1, so a[i] could be killed in a later step.

For example, consider the array [5,3,4,2,1]. In the first step, 5>3, 3's right is 4 (3 is killed in step 1). But 3 is killed in step 1, so in the next array, the array becomes [5,4,2,1]. Then step 2: 5>4 (killed), 4>2 (killed), 2>1 (killed). So the array becomes [5]. So step 2. The death steps are:

3 (step 1),4 (step2),2 (step2),1 (step2). So the maximum step is 2.

But how to compute this for all elements.

Another idea: Each element can be killed only when its left neighbor in the current array is larger than it. So the killing happens in steps where the left neighbor is present and alive.

So perhaps for each element, the death step depends on the death steps of the elements to the left and right of it.

Wait, perhaps we can model this by looking for the elements that are "triggered" to kill their right neighbor. For example, in the initial array, any a[i] > a[i+1] will cause a[i+1] to die in step 1. Then, in the next array, any a[j] (in the new array) > a[j+1] will cause a[j+1] to die in step 2, and so on.

So for each element, the step in which it dies is the number of steps required for its left neighbor (in the original array) to survive until that step, and be larger than it.

Wait, this seems complicated. Let's think of the elements in the original array. For each a[i], the earliest step it can die is step 1 if a[i-1] > a[i]. But if a[i-1] dies in step 1, then a[i] can only die in a step after that. Hmm, no. Because once a[i-1] dies, it's removed from the array, so a[i]'s left neighbor in subsequent steps is the first surviving element to the left.

So perhaps the death step of a[i] is determined by the maximum death step of the elements to the left that are larger than a[i], plus one.

Alternatively, for each element a[i], the death step is the number of steps required until a left neighbor (in the original array) that is larger than a[i] and has a death step >= the death steps of all elements between that left neighbor and a[i].

This is getting a bit abstract. Let's think of the elements and track the steps they are killed.

Let's take the first sample again. The death steps for the elements:

Indices (0-based) and their values:

0:10 (survives all steps)
1:9 (dies step 1)
2:7 (dies step1)
3:8 (dies step2)
4:6 (dies step1)
5:5 (dies step1)
6:3 (dies step1)
7:4 (dies step2)
8:2 (dies step1)
9:1 (dies step1)

So the maximum step is 2.

Hmm. For element 3 (8), how does it die in step 2? Because in step1, the array becomes [10,8,4]. Then in step2, 8's left is 10, which is larger. So 8 is killed in step2. Similarly, 4's left is 8 (now in the array of step2), which is larger than 4, so 4 is killed in step2.

So the key is, in each step, the left neighbor in the current array must be larger than the element.

So the death step for a[i] is 1 + the death step of any elements between the previous left neighbor (that's larger than a[i]) and a[i], that are killed in previous steps.

Wait, perhaps the death step of a[i] is the maximum death step of the elements to the left of a[i] that are smaller than a[i], plus 1. Or something like that.

Alternatively, for each element a[i], the earliest step when it can be killed is when the next surviving element to the left is larger than it.

So perhaps the approach is to process the elements from left to right, tracking for each element the maximum step required for the elements to the left that are larger than it, and then determine the death step based on that.

Alternatively, think of the elements in the original array, and for each element, find the next greater element to the left. But that's not exactly the case here, as the next greater element could be killed earlier.

Alternatively, for each element, the death step is determined by the maximum death step of the elements that are between the leftmost greater element and itself, plus 1.

Wait, let's model it with a stack.

An approach inspired by the problem of finding the number of visible elements after deletions. For each element, we can track the earliest step when it will be killed. Let's see.

We can process the array from right to left, and for each element, determine the step when it will be killed. The idea is that for an element to be killed, it must have a left neighbor that's larger than it. But the left neighbor must have survived until that step.

Let's try to model this.

For example, consider element i. If there is an element j < i such that a[j] > a[i], and all elements between j and i are killed before a[i] is killed, then a[j] will be the left neighbor of a[i] in some step, leading to a[i] being killed.

But how to model this.

Another idea: For each element, the death step is 1 + the maximum death step of the elements between its left neighbor (in the original array) and the next element to the left that is larger than it.

Wait, for example, in the first sample:

Original array is 10,9,7,8,6,5,3,4,2,1.

For the element 8 (index3):

The next left element larger than 8 is 10 (index0). But there are elements 9 (index1) and 7 (index2) between them. These elements are killed in step1. So after step1, the left neighbor of 8 is 10. So in step2, 10>8, so 8 is killed.

So the death step of 8 is 2.

So, the death step of 8 is the maximum death step of the elements between 10 and 8 (which are 9,7) plus 1.

The death steps of 9 and7 are 1. So max(1) +1 = 2.

So for element a[i], the death step is max(death_step[j] for j in (k+1, ..., i-1)) +1, where k is the nearest element to the left of i that is larger than a[i].

If there is no such k (i.e., there's no larger element to the left of i), then a[i] is not killed (death_step[i] = 0).

So the steps can be computed as follows:

We can precompute for each element the nearest larger element to the left (call this NL[i]). Then, the death step for element i is the maximum death step between NL[i]+1 and i-1, plus 1. If NL[i] is -1 (no such element), then death_step[i] is 0.

This seems promising. Let's test this logic on some examples.

First example:

For element 8 (index3):

NL[i] is 0 (a[0] is 10, which is larger than 8). The elements between 0 and3 are 1,2 (9 and7). Their death steps are 1 and1. Max is 1. So death step for 3 is 1+1=2. Correct.

For element 4 (index7, value4):

NL[i] is index3 (a[3]=8, which is larger than4). The elements between3 and7 are 4,5,6 (6,5,3). Their death steps are1,1,1. Max is 1. So death step for7 is1+1=2. Correct.

For element9 (index1):

NL[i] is0 (a[0]=10>9). The elements between0 and1 is none. So max is0. So death step is0+1=1. Correct.

For element7 (index2):

NL[i] is1 (a[1]=9>7). The elements between1 and2: none. So death step is0+1=1. Correct.

For element6 (index4):

NL[i] is3 (a[3]=8>6). Elements between3 and4: none. So death step is0+1=1. Correct.

For element5 (index5):

NL[i] is4 (a[4]=6>5). Elements between4 and5: none. So death step 0+1=1. Correct.

For element3 (index6):

NL[i] is5 (a[5]=5>3). Elements between5 and6: none. Death step 0+1=1. Correct.

For element2 (index8):

NL[i] is7 (a[7]=4>2). Elements between7 and8: none. Death step0+1=1. Correct.

For element1 (index9):

NL[i] is8 (a[8]=2>1). Death step0+1=1. Correct.

For element10 (index0): no NL[i], so death step0. Correct.

So the maximum death step is2, which is the answer. So this approach works for the first example.

Another example: the second input where the array is sorted in increasing order. Each element has no left neighbor larger than it. So all death steps are0. Hence the answer is0. Which matches the sample.

Another test case: array [5,3,4,2,1].

NL for each element:

index0:5 (no left, NL is -1. Death step0.

index1:3. NL is0. death_step[1] is max between 0 and0 (since elements between0 and1 are none) →0+1=1.

index2:4. NL is0. elements between0 and2 are1. The death step of1 is1. So death step for2 is1+1=2.

index3:2. NL is2 (a[2]=4>2). elements between2 and3: none. death step is0+1=1.

index4:1. NL is3 (a[3]=2>1). death step0+1=1.

So the death steps are0,1,2,1,1. The maximum is2. Which is correct, as the steps are 1 and2.

So this approach seems to work.

So the plan is:

1. Precompute NL (nearest left) for each element. This can be done in O(n) time using a stack.

2. For each element, compute death_step[i] as max(death_step[j] for j in (NL[i]+1 to i-1)) +1. If NL[i] is -1, death_step[i]=0.

But how to compute the max death_step[j] in the range (NL[i]+1 to i-1) efficiently.

If we process the elements in order, and for each i, the NL[i] is known, then the elements between NL[i]+1 and i-1 are those that are to the right of NL[i] and to the left of i. So perhaps for each NL[i], we can track the maximum death_step in that range.

Wait, but how to track this.

Another approach: Since we process the elements from left to right, for each i, when we find the NL[i], we can track the maximum death_step in the segment between NL[i] and i-1. Then death_step[i] = max_death +1.

But how to track the max_death between NL[i]+1 and i-1.

We can model this with a dynamic programming approach. Let's think:

We can create an array max_death, where max_death[i] represents the maximum death step between NL[i]+1 and i-1.

But how to compute this.

Alternatively, since the elements are processed in order, and for each i, the elements between NL[i]+1 and i-1 are contiguous and to the left of i, perhaps we can track for each i the maximum death step in the subtree.

Alternatively, for each i, the range (NL[i]+1, i-1) is a consecutive sequence. So for each i, the maximum death_step in that range can be found using a segment tree or a sparse table. But for n=1e5, a segment tree with O(n) preprocessing and O(log n) per query would be acceptable.

But building a segment tree for each i's range would take O(n log n) time, which is manageable.

Alternatively, perhaps there's a way to compute this maximum during the NL computation.

Wait, the stack approach for NL. Let's think:

When we compute NL[i] using a stack, the elements in the stack are in decreasing order. For each i, we pop elements from the stack until we find an element larger than a[i]. Then NL[i] is that element's index.

So during this process, for the elements between NL[i] and i-1, we can track the maximum death_step.

Wait, but how. Let's see.

Suppose we have a stack that contains the elements in decreasing order, and for each element in the stack, we also track the maximum death_step in the range from the previous element in the stack plus one up to current element.

Hmm, perhaps this is possible.

For example, when processing element i, after finding NL[i], the elements between NL[i]+1 and i-1 are those that were in the stack after NL[i] and were popped because they were smaller than a[i]. So those elements are all between NL[i] and i-1. The maximum death_step among them would be the maximum death_step in that range.

But how to track this.

Alternatively, for each element j, when it is popped from the stack (when processing some element i), we can note that j's right bound is i. Then, during this processing, for j, we can track the elements that are to the right of j's NL and to the left of j. But this is getting complicated.

Another idea: Since death_step[i] depends on the max death_step in the range between NL[i]+1 and i-1, and the NL array is built using a stack, perhaps during the stack processing, we can track the maximum death_step for each possible range.

Alternatively, we can note that when we process the elements in order, and maintain a stack that keeps track of elements and their maximum death steps in the ranges.

Wait, perhaps for each element in the stack, we can track the maximum death_step in the segment from the previous element in the stack to the current element.

For example, let's have the stack as a list of pairs (value, max_death_so_far).

When we process element i, we pop elements from the stack that are smaller than a[i]. For each popped element j, we can update some variables to track the maximum death_step. Then, the NL[i] is the top element of the stack after popping. The max_death for the range between NL[i]+1 and i-1 is the maximum of the death steps of the popped elements, and the death steps of the elements between the previous elements in the stack.

Wait, maybe this is possible.

Let me try to model this.

Suppose we have a stack that stores elements in decreasing order. Each element in the stack is a tuple (index, current_max_death). The current_max_death represents the maximum death step in the segment from the previous element's index +1 to this element's index.

When processing a new element i, we pop all elements from the stack that are smaller than a[i]. For each popped element, we keep track of the maximum death_step encountered. Then, the NL[i] is the index of the top element of the stack after popping. The current_max_death for the range between NL[i]+1 and i-1 is the maximum of the death steps of all popped elements, and any previous max_death stored in them.

Wait, but this is not clear. Let's think with an example.

Take the first example again.

Processing elements from left to right:

i=0: stack is empty. NL[0] = -1. death_step[0] =0. Push (0, 0) to stack.

i=1 (a[i]=9):

Pop elements with value <9. Stack has (0,10). 10 is bigger than9, so no popping. So NL[1] is0. The range between0+1=1 and1-1=0. No elements, so max_death is0. So death_step[1] =0+1=1. Push (1,1) to the stack. The stack is now [(0,0), (1,1)].

i=2 (a[i]=7):

Compare with stack top (1,1) which is9>7. So NL[2]=1. Range is1+1=2 to 2-1=1. No elements. So max_death=0. death_step[2]=0+1=1. Push (2,1) to stack. Stack is [(0,0), (1,1), (2,1)].

i=3 (a[i]=8):

Compare stack top (2,1)=7 <8. Pop it. The popped element's max_death is1. Then compare with next top (1,1) which is9>8. So NL[3]=1. The range is1+1=2 to3-1=2 (element2). So the max_death is the max of the popped elements' max_death (1). So death_step[3]=1+1=2. Push (3,2) to stack. The stack is now [(0,0), (1,1), (3,2)].

i=4 (a[i]=6):

Compare with stack top (3,2)=8>6. So NL[4]=3. Range is3+1=4 to4-1=3. No elements. max_death=0. death_step[4]=0+1=1. Push (4,1) to stack. Stack becomes [(0,0), (1,1), (3,2), (4,1)].

i=5 (a[i]=5):

Stack top (4,1)=6>5. NL=4. Range4+1=5 to5-1=4. No elements. max_death=0. death_step=1. Push (5,1).

i=6 (a[i]=3). Stack top (5,1)=5>3. NL=5. Range5+1=6 to6-1=5. No elements. death_step=1.

Push (6,1).

i=7 (a[i]=4). Compare with stack top (6,1)=3 <4. Pop it. max_death=1. Next top is (5,1)=5>4. So NL=5. Range5+1=6 to7-1=6. Element6. So death_step=1 (from popped elements) +1=2. Push (7,2).

i=8 (a[i]=2). Stack top (7,2)=4>2. NL=7. Range7+1=8 to8-1=7. No elements. death_step=0+1=1.

i=9 (a[i]=1). Stack top (8,1)=2>1. NL=8. death_step=1.

So for each i, the death_step is computed correctly.

So the idea is, during the stack processing for NL[i], when we pop elements smaller than a[i], we track the maximum death_step in those popped elements. Then, the death_step for i is that max plus one.

The stack can keep track of the maximum death_step in the segment that each element covers.

This way, when we process i, the popped elements' max_death are accumulated, and the death_step[i] is set to max_popped_deaths +1.

So this approach can work.

So the steps are:

1. Initialize a stack. Each element in the stack is a tuple (index, current_max_death). The current_max_death represents the maximum death step in the segment from the previous element in the stack's index +1 to the current element's index.

2. For each i from 0 to n-1:

   a. While stack is not empty and a[stack[-1][0]] < a[i], pop elements from the stack.

   b. Record the maximum death step among all popped elements. This is the max_death for the current i's range.

   c. If stack is empty, NL[i] = -1, else NL[i] = stack[-1][0].

   d. Compute death_step[i] as (max_death +1) if NL[i] !=-1, else 0.

   e. The current_max for the new element to be pushed is max(death_step[i], stack[-1][1] if stack not empty else 0). Wait, no. Because when we push (i, death_step[i]) into the stack, the current_max_death for the segment up to i is death_step[i], but perhaps this isn't correct.

Wait, the current_max_death stored in the stack should represent the maximum death step in the segment from the previous element's index +1 to the current index.

Wait, when we push (i, current_max_death), the current_max_death is the maximum death step in the range from the previous element in the stack's index +1 to i.

So when processing a new element i, after popping elements smaller than a[i], the new NL[i] is the top of the stack. The popped elements contribute their max_death to the current max_death for i's range.

Once NL[i] is determined, the range between NL[i]+1 and i-1 is the elements that were popped. The max_death is the maximum of their stored current_max_death values.

Then, the death_step[i] is max_death +1.

When pushing the new element to the stack, the current_max_death is death_step[i], because the segment from the previous element's index +1 (which is NL[i]+1) to i is covered by the new element. But wait, the current_max_death for the new element in the stack would be the maximum between death_step[i] and the previous current_max_death of the stack's top.

Wait, perhaps not. Let's think:

The previous element in the stack is NL[i]. The current_max_death for the new element is death_step[i], because the range from NL[i]+1 to i is covered, and the max death step in that range is the max of the popped elements' current_max_death (which is the max_death computed earlier) plus the new death_step[i]. Or wait, the max_death is the maximum of the popped elements' current_max_death, which is the max in the range NL[i]+1 to i-1, and then death_step[i] is the max_death +1.

So when pushing the new element, the current_max_death for the new element is death_step[i], since the segment from NL[i]+1 to i includes death_step[i], which is part of the new element's range.

Wait, perhaps the current_max_death for the new element is death_step[i], because in the range from the previous stack element's index+1 to i, the maximum death step is death_step[i]. Because the popped elements had their max_death computed, and death_step[i] is max_death_popped +1, which is larger than any of the popped elements' death steps.

But this may not be the case. For example, if multiple popped elements have higher current_max_death, then death_step[i] is the max of those plus 1. So death_step[i] = max_popped +1. Therefore, death_step[i] is larger than any of the popped elements' current_max_death.

So when we push the new element into the stack, the current_max_death is death_step[i], which is the maximum in the range from the previous element's index+1 to i.

So during the stack processing, for each element (index, current_max_death), the current_max_death is the maximum death step in the segment from the previous element's index+1 to the current index.

Thus, when popping elements, the max_popped is the maximum current_max_death of the popped elements.

So the steps are:

For each i in 0..n-1:

   Initialize max_death = 0

   While stack is not empty and a[stack[-1][0]] < a[i]:

       (idx, current_max) = stack.pop()

       if current_max > max_death:

           max_death = current_max

   if stack is empty:

       nl = -1

   else:

       nl = stack[-1][0]

   if nl == -1:

       death_step[i] = 0

   else:

       death_step[i] = max_death +1

   # Now, push (i, current_max_death) into stack. The current_max_death for i is death_step[i]?

   # Because the segment from nl+1 to i is covered by this element. So the current_max_death for this segment is death_step[i], which is the maximum between the popped elements' max_death and the new death_step[i].

   # But death_step[i] is max_popped +1, which is greater than the max_popped. So current_max_death is death_step[i].

   current_max_death = death_step[i]

   # Also, if there are elements in the stack, the previous element's current_max_death could be higher. So the current_max_death for the new element should be the maximum between death_step[i] and the previous element's current_max_death.

   # Wait, no. Because the previous element's current_max_death is the maximum of the range up to that element. But when we push the new element, the new segment is from the previous element's index +1 to i, and the current_max_death is death_step[i].

   # So in the stack, each element's current_max_death is the maximum in their own segment.

   stack.append( (i, current_max_death) )

So with this approach, for each popped element, their current_max_death is the maximum in their segment, which is the max between their own death_step and any previous segments.

But I'm not sure. Let's test this with the sample.

Processing i=3 (a[i]=8):

stack is [(0,0), (1,1), (2,1)].

Popping (2,1): max_death becomes1.

a[2] is7 <8. Continue.

Next, stack top is (1,1). a[1]=9>8. So NL=1.

death_step[3] =1 (max_popped is1) +1 =2.

Push (3,2) to stack.

So stack becomes [(0,0), (1,1), (3,2)].

For i=7 (a[i]=4):

Processing the stack. Current stack is after processing i=6 (3) as [ (0,0), (1,1), (3,2), (4,1), (5,1), (6,1) ].

a[i]=4.

Popping elements smaller than4:

First (6,1) (a[6]=3 <4). Max_death=1.

Then (5,1) (a[5]=5>4). So stop. NL=5.

death_step[7] =1 (max_death) +1=2.

Push (7,2) to stack.

So the stack becomes [ (0,0), (1,1), (3,2), (4,1), (5,1), (7,2) ].

So this seems correct.

Thus, the approach is:

Compute the nearest left (NL) for each element using a stack, tracking the maximum death step in the range between NL[i]+1 and i-1. Then, death_step[i] is that max +1 (if NL[i] exists). The stack also tracks the maximum death step in the segment covered by each element.

This allows us to compute death_step[i] in O(n) time, as each element is pushed and popped once from the stack.

Once we have all death_step values, the answer is the maximum value in the death_step array.

So the steps are:

- Compute the death_step array using the stack method.

- The answer is the maximum value in death_step.

Now, let's code this.

Implementing this in Python:

We need to read the array, compute NL for each element using a stack that keeps track of (index, current_max_death). For each element i:

Initialize max_death =0.

While the stack is not empty and the top element's value is less than a[i], pop it, and update max_death to the maximum between current max_death and the popped element's current_max_death.

Then, NL is the top element's index if stack is not empty, else -1.

If NL is -1, death_step[i] is0.

Else, death_step[i] = max_death +1.

Then, push (i, death_step[i]) to the stack.

Wait, but during the pushing, the current_max_death for the new element is death_step[i], because in the segment from NL[i]+1 to i, the maximum death_step is death_step[i] (since all elements in between were popped and their max_death is considered in the max_death variable, and death_step[i] is max_death +1, which is larger than the max_death).

Thus, when pushing to the stack, the current_max_death for the new element is death_step[i].

Thus, the code:

n = int(input())
a = list(map(int, input().split()))
death_step = [0]*n
stack = []
for i in range(n):
    current_max_death =0
    while stack and a[stack[-1][0]] < a[i]:
        idx, md = stack.pop()
        if md > current_max_death:
            current_max_death = md
    if not stack:
        nl = -1
    else:
        nl = stack[-1][0]
    if nl == -1:
        ds =0
    else:
        ds = current_max_death +1
    death_step[i] = ds
    stack.append( (i, ds) )
print(max(death_step))

Wait, let's test this code with the first sample.

Sample input 1:

10

10 9 7 8 6 5 3 4 2 1

Processing i=0: stack is empty. nl=-1. ds=0. stack becomes [(0,0)].

i=1 (9):

pop nothing. stack is [(0,0)]. a[0]=10>9. So nl=0.

ds=0 (current_max_death=0) +1=1. death_step[1] =1. stack becomes [(0,0), (1,1)].

i=2 (7):

stack top (1,1) a=9>7. So nl=1. current_max_death is0. ds=0+1=1. stack becomes [(0,0), (1,1), (2,1)].

i=3 (8):

pop (2,1) (a=7<8). current_max_death=1.

a[1] (9) >8. So nl=1. ds=1+1=2. death_step[3]=2. stack becomes [(0,0), (1,1), (3,2)].

i=4 (6):

stack top is3, a=8>6. nl=3. current_max_death is0. ds=0+1=1. stack appends (4,1).

i=5 (5): stack top is4, a=6>5. nl=4. ds=0+1=1. stack appends (5,1).

i=6 (3): stack top is5, a=5>3. nl=5. ds=0+1=1. stack appends (6,1).

i=7 (4):

pop (6,1) (a=3<4). current_max_death=1. next top is5 (a=5>4). nl=5. ds=1+1=2. stack appends (7,2).

i=8 (2): stack top is7 (a=4>2). nl=7. ds=0+1=1. append (8,1).

i=9 (1): stack top is8 (a=2>1). nl=8. ds=0+1=1. append (9,1).

death_step array is:

[0,1,1,2,1,1,1,2,1,1]. The maximum is2. Correct.

Sample input2:

6

1 2 3 4 5 6

Processing each element:

Each element has no left elements larger than it. So all death steps are0. The maximum is0. Correct.

Another test case:

array [5,3,4,2,1].

Processing:

i=0: stack empty. death_step[0] =0.

i=1 (3): a[0]=5>3. nl=0. ds=0+1=1. stack becomes [(0,0), (1,1)].

i=2 (4). Pop (1,1) (a=3<4). current_max_death=1. stack top is0 (5>4). nl=0. ds=1+1=2. stack appends (2,2).

i=3 (2). stack top is2 (4>2). nl=2. ds=0+1=1.

i=4 (1). stack top is3 (2>1). nl=3. ds=0+1=1.

death_step array is [0,1,2,1,1]. Max is2. Correct.

So the code seems to work.

This approach is O(n) time and O(n) space, which is suitable for n=1e5.

Thus, the code should pass all test cases.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
death_step = [0] * n
stack = []
for i in range(n):
    current_max = 0
    while stack and a[stack[-1][0]] < a[i]:
        _, md = stack.pop()
        current_max = max(current_max, md)
    nl = stack[-1][0] if stack else -1
    death_step[i] = 0 if nl == -1 else current_max + 1
    stack.append((i, death_step[i]))
print(max(death_step))
```