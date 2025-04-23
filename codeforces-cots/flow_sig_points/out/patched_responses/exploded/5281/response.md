<think>
Okay, let's see. The problem is about destroying elements in a certain order and after each step, finding the maximum sum of a contiguous subarray that doesn't include any destroyed elements. Hmm. Oh right, and the sum is zero if all are destroyed.

The constraints are up to 1e5 elements. So a naive approach would probably be too slow. For example, if after each step we tried to compute the maximum subarray from scratch, that's O(n^2) time which is definitely not going to work for n=1e5.

So we need a smarter way. Let's think about the reverse process. Instead of adding elements one by one (destroying them), maybe we can model this as adding elements to an empty array and keeping track of the maximum segment. Because when you destroy elements, the problem is similar to building the array by adding the elements in reverse order of destruction and keeping track of the maximum sum as you go. That way, each time you add an element, you can check the adjacent elements and merge intervals if possible.

Wait, this is a classic approach in some union-find problems. For example, when you have elements being destroyed, and you want to track connected components. But here, the sum is the key. So when you reverse the process, each step adds a new element (the one that was destroyed last in the original problem) and you can check its left and right neighbors to see if they are already present. Then, merge the intervals and keep track of the maximum sum.

So here's the plan:

1. Read the array and the destruction order. Let's call the destruction order as 'order', where order[i] is the 1-based index of the element to be destroyed in the i-th step.

2. Reverse the destruction order. Now, we'll process the elements in reverse. So the first element in the reversed order is the last one to be destroyed. Adding them one by one, and after each addition, compute the maximum sum.

3. We need to track for each element whether it's been added (i.e., not destroyed in the current step). When processing in reverse, adding an element would mean that it's not destroyed anymore.

4. For each added element, check the left and right elements. If they are present (i.e., have been added already), merge the current element's interval with theirs. This way, each time we add an element, we can calculate the sum of the merged interval and update the maximum sum accordingly.

5. The maximum sum after each addition (in reverse order) will correspond to the original problem's steps. For example, when we add the first element in the reversed order (the last to be destroyed), that corresponds to the original problem after n-1 destructions. The maximum sum at that point is the answer after all but the last destruction. Then, when we add the second element, which was the second to last to be destroyed, the maximum sum is the answer after n-2 destructions, and so on.

6. The answers are collected in reverse order and then reversed again to get the correct output.

So the key data structures here are a Union-Find (Disjoint Set Union) structure that can track the intervals and their sums. Each node in the DSU will need to track the leftmost and rightmost indices of the interval, as well as the sum of the elements in that interval. Additionally, we need to track which elements have been added already (so we know when to merge left or right).

Let's outline the steps in code:

- Initialize an array 'destroyed' that marks whether an element has been destroyed. Initially, all elements are destroyed except those we add in reverse order.

Wait, no. Wait, in the reverse process, we start with all elements destroyed (since the original problem starts with none destroyed and ends with all destroyed). Then, each step in the reverse process adds back an element (i.e., marks it as not destroyed). So in the reverse process, after k steps, the elements added are the last k elements to be destroyed in the original problem.

For example, in the first sample input:

Original destruction order is [3,4,1,2].

Reversed order is [2,1,4,3]. So step 1 in reverse is adding element 2 (which was the last to be destroyed in the original). Then step 2 is adding element 1, etc.

But in the original problem, after i destructions, i elements are destroyed. So in the reversed process, after adding i elements, n - i elements are destroyed. So the maximum sum after adding i elements in reverse is the answer after (n - i) destructions.

So the steps would be:

- Initially, all elements are destroyed. The maximum sum is 0.

- For each element in reversed destruction order:

   a. Add this element (mark as present).

   b. Check left and right elements. If present, merge their intervals with the current element.

   c. Update the current sum of the merged interval.

   d. Update the maximum sum.

   e. Record this maximum sum.

- The recorded maximum sums are in reverse order of the original problem's steps. So the first recorded sum (after adding 1 element) is the answer after (n-1) destructions. The second is after (n-2), etc. The final answer after all destructions is 0, which is handled by the initial step.

So the answer array after processing all elements in reverse order will have n entries. For example, after processing all elements, the sum is the original array's maximum subarray (since all are present). Then, when we reverse the answer array, the first entry (0) corresponds to all elements destroyed, the next entries are the answers after each destruction step.

Wait, let's think again. Let's take the first sample:

Original destruction steps: after 0 steps, all elements are present. After 1 step, third element is destroyed. After 2 steps, fourth is destroyed, etc.

In reverse processing:

We process destruction order in reverse: 2,1,4,3.

So first, add element 2 (original step 4's destruction). So after adding element 2 (index 2?), the array has element 2 (original element 3) destroyed? Wait, no. Wait, the destruction order is the permutation of 1..n, each element represents the position (1-based) of the element to destroy. So for example, in the first sample, the third step in destruction order is 1, which is the index of the first element (1-based) to be destroyed.

Wait, the destruction order is a permutation of 1 to n. So for the first sample, the destruction order is [3,4,1,2]. So the first element to destroy is the 3rd element (0-based index 2), which is 2 (the array is [1,3,2,5]). So after first destruction, the array is [1,3,*,5], then the fourth element (index 3) is destroyed, etc.

In reverse order, the steps are [2,1,4,3]. So the first step in the reverse process is adding back element 2 (original destruction step 4's element). Then 1 (step 3's element), then 4 (step 2's element), then 3 (step 1's element).

Wait, perhaps the elements to add are the ones destroyed in reverse order. So for the original destruction order, the order is d_1, d_2, ..., d_n. So the reverse is d_n, d_{n-1}, ..., d_1. So in the reverse process, the first added element is d_n (the last one destroyed in original). Then d_{n-1}, etc.

So when processing the reverse steps, each step adds back an element. Each such addition can connect to the left and right if those elements have already been added. The sum of the new interval is the sum of the left interval (if exists), plus the current element, plus the right interval (if exists). Then, the maximum sum is tracked, and stored in a list. After all steps, the list is reversed and each entry (except the last 0) is output, with an additional 0 at the end.

Wait, maybe. Let's see for the first sample:

Original destruction steps (n=4):

After step 1: destroy index 3 (original array's 0-based index 2) → sum is 5 (the 5 at index 3, which is 0-based index 3).

In reverse processing:

The destruction order reversed is [2,1,4,3]. So the reverse steps are adding the elements in the order of destruction steps 4, 3, 2, 1.

Wait, the original destruction steps are:

Step 1: destroy 3 (0-based 2)

Step 2: destroy 4 (0-based 3)

Step 3: destroy 1 (0-based 0)

Step 4: destroy 2 (0-based 1)

In reverse order, the steps would be steps 4,3,2,1. So the elements to add back are 2 (step4), 1 (step3), 4 (step2), 3 (step1).

Wait, but each step is the index (1-based) of the element to destroy. So for the destruction order array [3,4,1,2], the order is:

- step 1: destroy the 3rd element (1-based index 3 → 0-based index 2)

- step 2: destroy 4th (0-based 3)

- step 3: destroy 1st (0-based 0)

- step 4: destroy 2nd (0-based 1)

So the reversed destruction order is [2,1,4,3], which in 1-based is the order in reverse. So when reversed, the first element to add is 2 (0-based 1), then 1 (0-based 0), then 4 (0-based 3), then 3 (0-based 2).

In the reverse processing:

Initially, all elements are destroyed. The maximum sum is 0.

Processing step 1: add element 2 (0-based 1). Sum is 3. Max becomes 3. So the answer list has 3. But this corresponds to the original problem after 4-1=3 destructions. So in the original problem's output lines, after 3 destructions, the sum is 3. Wait, but in the first sample, after 3 destructions, the output is 3. The sample's output is:

5

4

3

0

So line 3 is 3, which is after 3 destructions. So the reverse processing's first step (adding element 2) gives the answer for 4-1=3 destructions, which is correct.

Then, processing step 2: add element 1 (0-based 0). Check left (none) and right (element 2 is already added). So merge them. Sum is 1+3=4. Max becomes 4. This corresponds to n-2=2 destructions. So the original step after 2 destructions (destroy 3 and 4) gives sum 4. Which matches the sample's second line.

Third step: add element 4 (0-based 3). Sum is 5. Now check left and right. No elements present. Max becomes max(4,5) →5. This corresponds to n-3=1 destructions. So original step after 1 destruction (destroy 3) gives sum 5. Which is the first line of the sample.

Fourth step: add element 3 (0-based 2). Check left and right. Left is 1-based 2 (0-based 1) added? Wait, no. The element at 0-based 2 is the third element (original index 3 in 1-based). So adding element 3 (0-based 2) has left neighbor at 0-based 1 (element 2, which is present) and right neighbor at 0-based 3 (element4, which is present). So merging all three intervals: sum is 3 (element1) + 2 (element2's sum?) Wait, I'm getting a bit confused here.

Wait, when adding an element, the sum is the value of the element plus the sum of the left interval (if exists) and the sum of the right interval (if exists).

Wait, the DSU structure for each node would track the sum of the interval. So when adding element x, we check if x-1 is present (left) and x+1 is present (right). For each of those, if present, we merge the intervals. The merged interval's sum is sum_left + a[x] + sum_right.

So in the first sample's fourth step (adding 3, which is 0-based index 2):

The value is 2 (since a[2] is 2). The left neighbor is x-1=1 (0-based 1), which is added (element 2). The right neighbor is x+1=3 (0-based 3), which is added (element4). So when we add x=2, we merge the left interval (sum 3+1=4?), the current element (2), and the right interval (sum5). So total sum is 4+2+5=11? But the sample's output for the fourth step (after all destructions) is 0. Hmm, perhaps I'm misunderstanding how the reverse processing maps to the original problem.

Wait, in reverse processing, after adding all four elements, the array is complete. So the maximum sum is the sum of the entire array. But in the first sample, the array is [1,3,2,5], which sums to 11. However, in the original problem, before any destructions, the maximum sum is 1+3+2+5=11. But the sample's output is 5 as the first line. So this suggests that my reasoning is wrong.

Ah! Oh right, wait. The problem says that after each destruction, we need to find the maximum sum of a contiguous segment that contains no destroyed elements. So the initial step (before any destruction) is the entire array. But in the sample input, the first output line is 5. That's because after the first destruction (element 3 is destroyed), the array is split into [1,3] and [5]. The maximum sum is 5.

So in the reverse processing:

The answer array starts as [0], then after each addition, the maximum sum is recorded. So after adding the last element (the first element in original destruction order), the array is completely restored. So the maximum sum is 11. But this would correspond to the original problem's step 0 (no destructions). However, the sample output doesn't include this step, as the first line is after the first destruction. So the reverse process's answers are stored in the list, which after being reversed and adding a 0 gives the correct output.

Wait, maybe the answer list after reverse processing has n entries. For example:

In the first sample, the reverse steps are adding 2,1,4,3. The answer list after each step is:

Step 1: add 2 → sum is 3 → answer list [3]

Step 2: add 1 → merged sum 1+3=4 → answer list [3,4]

Step3: add4 → sum 5 → answer list [3,4,5]

Step4: add3 → merged sum 1+3+2+5=11 → answer list [3,4,5,11]

Then, when reversed, we get [11,5,4,3], but we need to output for each step after i destructions (i from 1 to n). So after 1 destruction, the answer is 5 (from step3's addition), after 2 destructions 4 (step2), after 3 destructions 3 (step1), and after 4 destructions 0. So how does this mapping work?

Wait, perhaps the answer list in reverse processing is built as follows:

When processing the reversed destruction order, each step i (from 0 to n-1) in the reversed processing corresponds to having added i+1 elements. The maximum sum after adding i+1 elements is stored. Then, the answer list in the reversed processing is [max1, max2, ..., maxn]. Then, the answer for the original problem's step k is the (n-k)th element in this list. Because:

Original step k: after k elements are destroyed. So n -k elements remain. These are exactly the elements added in the first (n-k) steps of the reversed processing.

Wait, no. For example, after original step 1 (k=1), n -k =3 elements are present. Which would correspond to the reversed processing after 3 steps. Because the reversed processing adds elements in the order of the destruction steps. So the first 3 steps in reversed processing add the last 3 destruction elements. So the elements present after step 3 of reversed processing are those destroyed in the original steps 4,3,2 (so original steps 1,2,3 are the ones remaining? Not sure.

Alternatively, perhaps the answer list in the reversed processing (after adding each element) is stored, and then we reverse this list and prepend a 0. Then, when we output the answer for i steps of destruction, it's the (i)th element in this list.

Let me take the first sample again:

In reversed processing steps, the answer list is built as follows:

After adding 2: sum 3 → answer list [3]

After adding 1: sum4 → answer list [3,4]

After adding4: sum5 → answer list [3,4,5]

After adding3: sum11 → answer list [3,4,5,11]

Now, reverse this list to get [11,5,4,3]. Then, prepend a 0. So the list becomes [0,11,5,4,3]. Then, for original steps:

After 0 destructions: the sum is 11 → but the output is not required. The first line is after 1 destruction. So the output is:

Line 1: after 1 destruction → which is the second element in the new list (11 is after 0 destructions, 5 is after 1 destruction → the reversed list [11,5,4,3] corresponds to destructions 0,1,2,3. But the problem's output has to have n lines, each line after i destructions. So after i destructions, the maximum sum is the (i)th element in the list obtained by [0] + reversed(reversed_answers). Then, take the list [0] + reversed_answers_reversed → which would be 0 followed by 11,5,4,3 → but that's 5 elements for n=4. Then, the first line is after 1 destruction, which is the second element (5). Second line is 4 (after 2 destructions), third line 3 (after 3 destructions), fourth line 0 (after 4 destructions). Which matches the sample output.

Wait, perhaps the correct approach is:

The reversed processing produces a list of maximum sums, in the order of adding the elements. Each step in reversed processing (after adding the k-th element) corresponds to the original problem after (n -k) elements have been destroyed. Because adding k elements in reversed processing means that n -k elements are destroyed in the original problem. So the original problem's i-th step (i destructions) corresponds to reversed processing's (n -i) elements added. So the maximum sum for i destructions is the maximum sum after adding (n -i) elements in reversed processing. But during reversed processing, the maximum sum is kept track of as the maximum so far.

Wait, perhaps the reversed processing builds a list where the j-th element (0 <=j <n) is the maximum sum after adding j+1 elements. Then, for the original problem's i destructions (i steps), which leaves (n -i) elements present, the maximum sum is the maximum of all j+1 <= (n -i) elements. Wait, that doesn't make sense. Because adding elements in reversed order, each addition can merge intervals, which can lead to a higher sum than previous steps. So the maximum sum is non-decreasing as we add elements. So the maximum sum after adding j elements is the maximum possible sum for that step, and for the original problem's i destructions, the answer is the maximum sum after adding (n -i) elements.

Wait, but when you add more elements, the maximum sum can only increase or stay the same. So for the original problem, the answer after i destructions is the maximum sum of the intervals present after (n -i) elements have been added in the reversed processing. But since adding elements can create larger intervals, the maximum sum after j elements is the maximum possible for that j. So the answer for the original problem's i destructions is the maximum sum stored in the reversed processing's (n -i)th step.

But how to track this maximum sum? Because each step in reversed processing can have a new maximum. So during the reversed processing steps, we track the current maximum and after each addition, we record the current maximum. Then, when reversed, these recorded maxima form the answers for the original problem's steps. For example:

In the first sample:

Reversed steps:

Add 2 → sum 3. current max is 3. record 3.

Add 1 → sum 4. current max is 4. record 4.

Add4 → sum5. current max is5. record5.

Add3 → sum11. current max is11. record11.

The recorded list is [3,4,5,11]. Then, when we reverse this list and prepend a 0, we get [0,11,5,4,3]. Then, the original problem's steps:

After 0 destructions → sum 11 (but not part of output).

After 1 destruction → 5 (from 11 in reversed list, which was the third step? No, wait. Wait, the original i destructions correspond to (n -i) added elements. For example, i=1, then (n-i)=3 added elements. So the third entry in the reversed processing's list is 5. So the answer is 5. Which matches the sample.

Similarly:

Original step 1: i=1 → n-i=3. reversed processing list has 3 elements (after 3 steps). The third element is5.

Original step 2: i=2 →n-i=2. reversed processing list's second element is4.

Original step3: i=3 →n-i=1. reversed processing list's first element is3.

Original step4: i=4 →n-i=0. output 0.

So the output is [5,4,3,0], which matches the sample.

So the process is:

After reversed processing, the list is [3,4,5,11]. Then, to get the answers for the original problem's i steps (from 1 to n), the answer for i is the maximum sum in the reversed processing after (n -i) steps. But how?

Wait, perhaps the reversed processing's list is [3,4,5,11], which is for adding 1,2,3,4 elements. Then, the original problem's i=1 destructions leaves 3 elements (n-i=3). So the reversed processing's after 3 steps is 5. So the answer for i=1 is5.

But how to get this from the list. The list after 3 steps is [3,4,5], but the maximum is5. Wait, no. Because each step in reversed processing's list is the current maximum after adding that step's element. So the list is [3,4,5,11], where each entry is the current maximum. So when we have to find the maximum for the original problem's i steps, it's the entry at (n-i) -1 index in this list. Because for example, i=1: n-i=3 → the index is 3-1=2 (since adding 3 elements is the third entry in the list, which is5). Then, after reversing the list, we have [11,5,4,3], and then we add a 0 at the beginning. Wait, perhaps the steps are:

1. In reversed processing, for each step (adding an element), record the current maximum sum. So after step j (1<=j<=n), the maximum is stored in a list called res.

2. The res list has n elements, where the j-th element is the maximum after adding j elements.

3. For the original problem's i destructions, the number of elements present is (n - i). So j = (n -i). So the answer is res[j-1], but if j is 0, then the answer is0.

4. The answers for the original problem are:

After i destructions (i from 1 to n):

if (n-i) >=1 → res[n-i -1]

else →0

So the steps to create the output are:

output = [0] + res[::-1]

then, output[i] is the answer after i destructions.

Wait, for example:

res is [3,4,5,11]

reversed res is [11,5,4,3]

prepending 0 → [0,11,5,4,3]

then, for i from 1 to4:

i=1 → output[1] =11 → but in sample, it's5. This doesn't match.

Hmm, this suggests my approach is incorrect. So what's wrong?

Wait, perhaps the reversed processing's res list is [3,4,5,11], which is the maximum sum after adding 1,2,3,4 elements. But the original problem's steps are:

After i destructions, there are (n -i) elements left. So the maximum sum after adding (n -i) elements is res[(n -i) -1], but only if (n-i) >=1. Otherwise, it's0.

So for the first sample, after 1 destruction, (n-i)=3. So res[3-1=2] =5 → which is correct.

After 2 destructions, (n-i)=2 → res[1] =4 → correct.

After3 destructions → res[0] =3 → correct.

After4 →0.

So the output is:

res[2] →5

res[1] →4

res[0] →3

0

So the output list is [5,4,3,0], which matches the sample.

But how to get this from the res list?

The res list has 4 elements (indices 0-3), each corresponding to adding 1-4 elements. So for (n-i) elements added, the index is (n-i)-1.

So the answer for i destructions is:

if (n-i) ==0 →0

else → res[(n-i)-1]

So to create the output for the original problem, we need to generate for each i from1 to n:

if (n -i) >0 → res[(n-i)-1]

else →0

So the output list can be built by taking for each i in 1..n:

answer = res[(n-i)-1] if (n-i) >0 else 0

But this requires that for each i, we compute the correct index. However, the res list is ordered as the maximum after each addition step. So for example, res[0] is after adding 1 element, res[1] after adding 2, etc.

So for i destructions:

number of elements added in reversed processing is (n -i). So:

if (n-i) ==0 →0

else → res[(n-i)-1]

Thus, the output list is:

for i in 1..n:

   if (n -i) >=1:

       res[ (n -i) -1 ]

   else:

       0

Which can be written as:

output = []

for i in range(1, n+1):

   if (n -i) >=1:

       output.append( res[ (n-i) -1 ] )

   else:

       output.append(0)

But how to handle this efficiently.

Alternatively, if we reverse the res list and prepend a 0, then:

res_reversed = res[::-1]

output_list = res_reversed + [0]

Then, for i from1 to n:

output_list[i-1]

For example, in the first sample:

res = [3,4,5,11]

res_reversed = [11,5,4,3]

output_list = res_reversed + [0] → [11,5,4,3,0]

But original problem's outputs are after 1..4 destructions.

For i=1 → output_list[0] →11. Which is incorrect. So this approach isn't working.

Hmm. So perhaps I need to think differently. Let's see:

The res list contains the maximum sums after adding 1,2,3,4 elements. So the indices are 0-based:

res[0] →1 element added →max sum 3

res[1] →2 elements →4

res[2] →3 →5

res[3] →4 →11

These correspond to the original problem's steps where:

After (n - added) elements have been destroyed. For example:

added=1 → destroyed is n - added =4-1=3 → step3 → output after3 destructions.

So the original problem's step i (number of destructions) is n - added.

So for res[j], where j is 0-based (added = j+1):

i = n - (j+1)

We need to find j such that i is the number of destructions. So for a given i, j =n -i-1.

But the output list is required to have for i=1 to i=n, the sum after i destructions.

So for each i in 1..n:

sum = res[ j ] where j =n -i-1, but only if j >=0. Otherwise, sum is 0.

So for example:

i=1 → j=4-1-1=2 → res[2] =5 → correct.

i=2 → j=4-2-1=1 → res[1]=4 → correct.

i=3 →j=4-3-1=0 → res[0]=3 → correct.

i=4 →j=4-4-1= -1 → sum 0 → correct.

Thus, the output list is built by iterating i from1 ton and getting res[n-i-1] if possible.

So how to build this list from the res list.

But in Python, the res list is [3,4,5,11]. So for each i in1..4:

n-i-1 for n=4 is:

i=1 →2 →5

i=2 →1 →4

i=3 →0 →3

i=4 →-1 →0.

Thus, the output list is [5,4,3,0], which is correct.

So the process is:

After building the res list in the reversed processing steps, the output for each i is:

res[n-i-1] if (n-i-1) >=0 else 0.

So in code:

output = []

for i in range(1, n+1):

   idx = n -i -1

   if idx >=0:

       output.append(res[idx])

   else:

       output.append(0)

Then, print each element of output.

So the steps to implement:

1. Read n, array a, and destruction order (as list of integers, 1-based indices).

2. Reverse the destruction order to get the add order (processing in reverse).

3. Initialize a DSU structure where each element tracks the left, right, sum, and whether it's active.

4. Initialize a list 'active' to track which elements are added.

5. Initialize the maximum sum as 0.

6. For each element in the reversed destruction order:

   a. Convert the 1-based index to 0-based (element_pos = x-1)

   b. Mark this position as active.

   c. Set current_sum to a[element_pos]

   d. Check the left neighbor (element_pos -1). If active, find its root and get its sum. Merge left.

   e. Check the right neighbor (element_pos +1). If active, find its root and get its sum. Merge right.

   f. Update current_sum to be sum of left + current_sum + sum of right.

   g. Update the maximum_sum if current_sum is larger.

   h. Append the current maximum_sum to the res list.

7. After processing all elements, the res list has n elements.

8. Generate the output list by for each i from1 ton:

   idx =n-i-1

   if idx >=0: output res[idx] else 0.

9. Print each element of the output list.

Now, the key is to implement the DSU structure efficiently.

The DSU needs to track for each element, when it's added (active), and for each component, track the sum, leftmost and rightmost indices.

An efficient way is to use a dictionary or array to represent the parent of each node. But for n up to 1e5, an array is better.

Each node's parent will point to the root of the component.

For each component, we can track:

- sum: the sum of the component.

- left: the leftmost index.

- right: the rightmost index.

So for each element x, when we add it, we check x-1 and x+1. For each, if active, we find their root and merge them with x.

The merging process will combine the sum, update the left and right.

The DSU find and union operations need to be efficient, which is possible with path compression and union by rank/size.

But since we are always merging the current element with its left and right (which are either not present or roots), we can handle the union without the need for union by rank.

For example, when x is added, and its left is present:

Find the root of left. Then, the new component's sum is sum_left + a[x]. Similarly for the right.

Wait, but the DSU structure must track for each component the sum, left, and right.

So for each root node, we can keep track of sum, left, right.

Thus, when we find the root of a component, we can directly get the sum, left, and right of the component.

So the data structures would be:

parent: list where parent[i] is the parent of i. If i is the root, parent[i] =i.

sum: list where sum[i] is the sum of the component if i is a root.

left: list where left[i] is the leftmost index of the component if i is a root.

right: list where right[i] is the rightmost index of the component if i is a root.

But to handle this, when merging components:

For example, merging x's component (which is just x, since we're adding it now) with the left component (root l_root):

The new sum is sum[l_root] + a[x].

The left is left[l_root], right is x.

Wait, but x is being merged with the left component, which is from l_root's right to x-1. So the merged component's left is l_root's left, and right is x.

Similarly, if there's a right component (r_root), the merged component's left is x, right is r_root's right, sum is sum[x's component] (which is a[x] + sum[l_root] + sum[r_root}).

Wait, but when adding x, the current sum is a[x]. Then, if left is present, we need to merge x's component with the left component. Then, if right is present, merge with the right component.

So the steps are:

- x is added. Initially, its parent is x. sum[x] =a[x]. left[x] =x. right[x] =x.

- Check left neighbor x-1. If active, find its root (l_root). Then, sum of merged component is sum[l_root] + sum[x]. The left becomes left[l_root], right becomes x. Then, union l_root and x, with x's parent pointing to l_root (or vice versa). Wait, but which way to merge?

Alternatively, when merging x with l_root:

parent[x] = l_root.

sum[l_root] += sum[x]

left[l_root] remains as before.

right[l_root] =x's right (which is x).

Then, after merging x with l_root, check the right neighbor x+1.

If right neighbor is active, find its root (r_root). Then, merge the current root (l_root) with r_root.

Wait, but after merging x with l_root, the current component's right is x. If x+1 is active, its component's root is r_root. So merging l_root and r_root:

sum is sum[l_root] + sum[r_root]

left is left[l_root]

right is right[r_root]

So the DSU structure needs to handle these merges.

Thus, the DSU operations would be:

For find: standard path compression.

For union:

When merging two components, we need to update the sum, left, and right of the root.

But how to choose which component becomes the root.

In code, when we have two roots A and B (A is the root of the component to the left, B to the right), we can merge B into A. Or A into B. But since the order here is that the left component is to the left of the current node, and the right component is to the right, the merged component's left is A's left, right is B's right. So when merging, for example, when merging the left component (A) with x's component (initially x), we set x's parent to A, and update A's sum, left, right.

So for the code:

When adding x:

sum[x] = a[x]

left[x] = x

right[x] = x

parent[x] = x

active[x] = True

current_sum = a[x]

if x-1 is active:

   l_root = find(x-1)

   current_sum += sum[l_root]

   # merge x into l_root's component

   parent[x] = l_root

   sum[l_root] += sum[x]

   right[l_root] = x

   # Now, the left component's root is l_root, and the right is x

   # After merging, check x+1

current_sum = sum of the merged component so far.

if x+1 is active:

   r_root = find(x+1)

   current_sum += sum[r_root]

   # merge r_root into l_root (or x's root, which is l_root now if left was active)

   # find x's current root (which may be l_root or x if left was not active)

   current_root = find(x)

   parent[r_root] = current_root

   sum[current_root] += sum[r_root]

   left[current_root] = min(left[current_root], left[r_root])

   right[current_root] = max(right[current_root], right[r_root])

So after merging left and right, the current_sum is the sum of the new component.

Then, the maximum_sum is updated to the maximum between its current value and current_sum.

But wait, the current_sum would be the sum of the entire merged component. So after merging left and right, the sum is sum of left component + x's sum + right component's sum.

But in code, after merging left, the sum[l_root] is sum of left component plus x's sum. Then, when merging right, sum[r_root] is added to current_root's sum.

Thus, the code would need to correctly calculate the sum after each merge.

Alternatively, perhaps we can:

current_sum = a[x]

left_merged = False

if left is active:

   merge left component into x's component.

   current_sum += sum of left component.

if right is active:

   merge right component into x's component.

   current_sum += sum of right component.

Then, after merging left and right, the current_sum is the sum of the new component.

But how to track this.

An alternative approach is:

When adding x, the initial sum is a[x]. Then, check left and right.

For each direction:

- For left (x-1):

   if active, find its root.

   sum += sum[left_root]

   merge x into left_root (make left_root the parent of x).

   Then, the new root is left_root.

- For right (x+1):

   if active, find its root.

   sum += sum[right_root]

   merge right_root into the current root (left_root or x).

But merging the right into the current root.

So in code:

current_sum = a[x]

# handle left

if left exists:

   left_root = find(x-1)

   current_sum += sum[left_root]

   parent[x] = left_root

   sum[left_root] += a[x]

   # update left and right of left_root?

   # left of left_root remains the same.

   right[left_root] = x

# after handling left, the current component's root is left_root (if left was present), else x.

current_root = find(x)

# handle right

if right exists:

   right_root = find(x+1)

   current_sum += sum[right_root]

   # merge right_root into current_root

   parent[right_root] = current_root

   sum[current_root] += sum[right_root]

   # update left and right of current_root

   left[current_root] = min(left[current_root], left[right_root])

   right[current_root] = max(right[current_root], right[right_root])

But wait, when merging the right component into current_root:

The current_root's left and right may already have been updated from merging the left component. So after merging the right component, the left of current_root could be min(current_root's left and right component's left), but since the current component is the left component merged with x and possibly the right component, the right component's left is x+1, so the left of current_root would be the original left's left (from x-1's component) or x's original left (x) if no left merge. So merging right component's left is x+1's left, which is x+1's left (which could be x+1 if it's a single node, or something else if x+1 is part of a larger component).

Hmm. This suggests that the left and right for each root should be stored, and when merging, they are updated.

But in any case, the sum of the component is stored in the root's sum.

So when merging two components, the sum of the new root is the sum of both components.

The left of the new component is the minimum of the lefts of the two components.

The right of the new component is the maximum of the rights of the two components.

So in code:

When merging component A into component B:

sum[B] += sum[A]

left[B] = min(left[A], left[B])

right[B] = max(right[A], right[B])

parent[A] = B

So when merging left, we:

sum[left_root] += sum[x]

left[left_root] remains as before.

right[left_root] = x (since x is the new right end).

Then, when merging the right component into the current_root (which is left_root or x if left wasn't present):

sum[current_root] += sum[right_root]

left[current_root] = min(current_root's left, right_root's left)

right[current_root] = max(current_root's right, right_root's right)

Thus, the sum of the merged component is correctly tracked.

But how to implement this.

Let's think about the steps when adding x:

Initially, x is active. parent[x] =x, sum[x] =a[x], left[x]=x, right[x]=x.

Check x-1:

If active (i.e., exists in active array and find(x-1) is active), then:

   l_root = find(x-1)

   sum[x] += sum[l_root]

   parent[x] = l_root

   sum[l_root] += sum[x] --> Wait, no. Because sum[x] is a[x], and l_root's sum is sum of its component. So merging x into l_root's component.

   So sum[l_root] += a[x]

   right[l_root] =x

   left[l_root] remains the same.

But this is incorrect, since x is a single node. Wait, no. Because when merging x into l_root's component, the l_root's component's sum is increased by a[x], and its right boundary is updated to x.

So the correct steps are:

   sum[l_root] += sum[x]  # sum[x] is a[x]

   right[l_root] = x

   parent[x] = l_root

   # left[l_root] remains as before (since x is to the right)

Then, check x+1:

If active:

   r_root = find(x+1)

   sum[ current_root ] += sum[r_root ]

   parent[r_root] = current_root

   left[current_root] = min(left[current_root], left[r_root])

   right[current_root] = max(right[current_root], right[r_root])

So current_root is find(x), which after merging left is l_root.

Thus, merging the right component into current_root.

So the sum of current_root is sum[l_root] (which is sum of l_root's component plus x's a[x]) plus sum[r_root] (sum of r_root's component).

But perhaps the code should be:

current_root = find(x)

sum[current_root] += sum[r_root]

Then, merge r_root into current_root.

But I think the code will need to handle these steps.

But how to code this efficiently.

Another approach is to have for each component:

- The root of the component.

- sum, left, right stored only in the root.

Thus, when merging two components, we can get their roots and update the sum, left, right of the new root.

So when we add x:

1. Initialize x's component with sum =a[x], left=x, right=x.

2. Check if x-1 is active:

   a. If yes, find its root (l_root).

   b. Merge x into l_root:

      i. sum[l_root] += a[x]

      ii. right[l_root] = x

      iii. parent[x] = l_root

3. Check if x+1 is active:

   a. If yes, find its root (r_root).

   b. Merge r_root into the current root (which is l_root if left was merged, else x):

      i. sum[current_root] += sum[r_root]

      ii. left[current_root] = min(left[current_root], left[r_root])

      iii. right[current_root] = max(right[current_root], right[r_root])

      iv. parent[r_root] = current_root

Thus, the sum of the current component after merging left and right is a[x] + sum of left component + sum of right component.

The maximum_sum is then updated to the maximum between current maximum and this sum.

But wait, after merging left, the sum is sum[l_root] = sum of left component + a[x]. Then, merging right adds sum[r_root].

Thus, after all merges, the sum is sum[l_root] + sum[r_root] = sum_left + a[x] + sum_right.

Which is correct.

But how to track the sum of the merged component.

Alternatively, after all merges, the current_root will be the root of the component that x belongs to. The sum of the component is sum[current_root].

So the current_sum can be sum[current_root].

Thus, after processing left and right, the current_sum is sum[current_root].

Then, the maximum_sum is updated as max(max_sum, current_sum).

Thus, in code:

max_sum = 0

res = []

for x in reversed_order:

   pos = x-1  # convert to 0-based

   active[pos] = True

   parent[pos] = pos

   sum_ar[pos] = a[pos]

   left_ar[pos] = pos

   right_ar[pos] = pos

   current_sum = sum_ar[pos]

   # check left

   if pos >0 and active[pos-1]:

       l_root = find(pos-1)

       # merge pos into l_root

       parent[pos] = l_root

       sum_ar[l_root] += sum_ar[pos]

       right_ar[l_root] = pos

       current_sum = sum_ar[l_root]

       # after merging left, current root is l_root

   # check right

   if pos <n-1 and active[pos+1]:

       r_root = find(pos+1)

       # current_root is find(pos)

       current_root = find(pos)

       if current_root != r_root:

           # merge r_root into current_root

           parent[r_root] = current_root

           sum_ar[current_root] += sum_ar[r_root]

           left_ar[current_root] = min(left_ar[current_root], left_ar[r_root])

           right_ar[current_root] = max(right_ar[current_root], right_ar[r_root])

           current_sum = sum_ar[current_root]

   # update max_sum

   if current_sum > max_sum:

       max_sum = current_sum

   res.append(max_sum)

But this may not account for merging both left and right.

Wait, after merging left, the current_sum is sum_ar[l_root], which is sum of left component + a[pos].

Then, when merging right, the current_root becomes l_root (since parent[pos] is l_root, and find(pos) returns l_root). Then, merging r_root into l_root:

sum_ar[l_root] += sum_ar[r_root]

So current_sum becomes sum_ar[l_root], which is sum_left + a[pos] + sum_right.

Thus, this code correctly calculates current_sum.

Then, the maximum_sum is the maximum between previous max and current_sum.

So the code should work.

Now, the DSU find function with path compression:

def find(u):

   if parent[u] != u:

       parent[u] = find(parent[u])

   return parent[u]

Yes.

So, the steps in code:

Read n.

Read a as list.

Read destruction_order as list of integers (1-based).

Reversed_order = reversed(destruction_order)

Initialize parent as [0]*n.

sum_ar = [0]*n.

left_ar = [0]*n.

right_ar = [0]*n.

active = [False]*n.

res = []

max_sum =0

for x in reversed_order:

   pos =x-1

   active[pos] =True

   parent[pos] = pos

   sum_ar[pos] =a[pos]

   left_ar[pos] = pos

   right_ar[pos] = pos

   current_sum =a[pos]

   # merge left

   if pos >0 and active[pos-1]:

       l_root = find(pos-1)

       parent[pos] = l_root

       sum_ar[l_root] += sum_ar[pos]

       right_ar[l_root] = pos

       current_sum = sum_ar[l_root]

   # merge right

   if pos <n-1 and active[pos+1]:

       r_root = find(pos+1)

       current_root = find(pos)

       if r_root != current_root:

           parent[r_root] = current_root

           sum_ar[current_root] += sum_ar[r_root]

           left_ar[current_root] = min(left_ar[current_root], left_ar[r_root])

           right_ar[current_root] = max(right_ar[current_root], right_ar[r_root])

           current_sum = sum_ar[current_root]

   max_sum = max(max_sum, current_sum)

   res.append(max_sum)

Then, generate the output list:

output = []

for i in range(1, n+1):

   idx =n -i -1

   if idx >=0:

       output.append(res[idx])

   else:

       output.append(0)

Then, print each element.

But wait, in the first sample, when adding the third element (the last in reversed_order), which is 3 (0-based index 2):

After adding it, current_sum is 2. Then check left (pos-1=1, which is active? Yes, as it was added in step1.

So l_root = find(1) → which is 1's parent. Initially, when 1 is added, it's merged with left and right.

Wait, this seems complicated. But according to the code, it should correctly track the sum.

But to be sure, let's test the first sample.

Sample 1:

n=4.

a= [1,3,2,5]

destruction_order = [3,4,1,2]. reversed_order is [2,1,4,3]. But reversed_order is obtained by destruction_order[::-1], which for [3,4,1,2] is [2,1,4,3]. So in reversed_order, the elements are 2,1,4,3 (1-based), which in 0-based are 1,0,3,2.

Processing reversed_order:

First element is 2 →0-based 1 (value 3).

active[1] =True.

parent[1]=1.

sum_ar[1] =3.

left_ar[1] =1.

right_ar[1] =1.

Check left (pos-1=0, active is False). So no merge.

Check right (pos+1=2, active False. So no merge.

current_sum is3. max_sum is3. res.append(3).

Second element is1 →0-based 0 (value1).

active[0] =True.

parent[0]=0.

sum_ar[0] =1.

left_ar[0] =0.

right_ar[0] =0.

Check left (pos-1 =-1: no.

Check right (pos+1=1: active.

So r_root = find(1) →1.

current_root is find(0) →0.

Merge r_root (1) into current_root (0).

sum_ar[0] += sum_ar[1] →1+3=4.

left_ar[0] = min(0, left_ar[1]=1 →0.

right_ar[0] = max(0, right_ar[1]=1 →1.

current_sum=4. max_sum=4. res becomes [3,4].

Third element is4 →0-based 3 (value5).

active[3] =True.

parent[3] =3.

sum_ar[3] =5.

left_ar[3] =3.

right_ar[3] =3.

Check left (pos-1=2: active? Not yet. So no merge.

Check right (pos+1=4: invalid.

current_sum=5. max_sum becomes5. res [3,4,5].

Fourth element is3 →0-based 2 (value2).

active[2] =True.

parent[2] =2.

sum_ar[2]=2.

left_ar[2] =2.

right_ar[2] =2.

Check left (pos-1=1: active. Yes.

l_root = find(1). What is the parent of 1 now?

After processing the second element (0-based 0), when we merged 1 into 0's component, parent[1] =0.

So find(1) returns find(0) →0. So l_root=0.

sum_ar[0] is4.

So merge 2 into 0's component:

parent[2] =0.

sum_ar[0] += 2 →4+2=6.

right_ar[0] =2.

current_sum=6.

Then check right (pos+1=3: active.

r_root = find(3) →3.

current_root = find(2) →0.

Merge r_root (3) into current_root (0).

sum_ar[0] += sum_ar[3] →6+5=11.

left_ar[0] = min(0,3's left=3) →0.

right_ar[0] = max(2,3's right=3) →3.

current_sum=11.

max_sum is now 11.

res becomes [3,4,5,11].

Thus, the res list is [3,4,5,11].

Generating the output list:

For i from 1 to4:

i=1 →n-i-1=4-1-1=2 →res[2]=5.

i=2 →4-2-1=1 →res[1]=4.

i=3 →4-3-1=0 →res[0]=3.

i=4 →-1 →0.

Output list is [5,4,3,0], which matches the sample.

So the code works for this case.

Now, the code needs to handle large n (up to 1e5). So using arrays for parent, sum_ar, left_ar, right_ar is efficient.

The DSU operations are O(alpha(n)) per operation, which is acceptable for 1e5 elements.

Thus, the code should work.

Now, the final step is to write the Python code.

But in Python, for n=1e5, using lists for parent, sum_ar, left_ar, right_ar is feasible.

But for speed, we need to pre-initialize these lists.

Thus, code:

Read n.

Read the array a.

Read the destruction order as a list of integers.

Reverse it.

Initialize parent, sum_ar, left_ar, right_ar as lists of size n.

active as a list of booleans.

Then, process each element in reversed_order.

Finally, generate the output.

But in Python, for initializing lists:

parent = [i for i in range(n)] → but during processing, we reset parent[pos] to pos when adding. Wait, no. Because when adding pos, we set parent[pos] = pos. So initializing parent to any value is not necessary, as we set it when adding.

But wait, when processing reversed_order, each element is added once.

So when adding pos, we set parent[pos] = pos.

Thus, parent can be initialized to any values, as during adding, each pos is set.

But for efficiency, perhaps pre-initializing parent as a list of size n.

In code:

n = int(input())

a = list(map(int, input().split()))

destroy_order = list(map(int, input().split()))

reversed_order = reversed(destroy_order)

parent = [0]*n

sum_ar = [0]*n

left_ar = [0]*n

right_ar = [0]*n

active = [False]*n

max_sum =0

res = []

for x in reversed_order:

   pos = x-1

   active[pos] = True

   parent[pos] = pos

   sum_ar[pos] = a[pos]

   left_ar[pos] = pos

   right_ar[pos] = pos

   current_sum = a[pos]

   # check left neighbor

   if pos >0 and active[pos-1]:

       l_root = find(pos-1)

       parent[pos] = l_root

       sum_ar[l_root] += sum_ar[pos]

       right_ar[l_root] = pos

       current_sum = sum_ar[l_root]

   # check right neighbor

   if pos <n-1 and active[pos+1]:

       r_root = find(pos+1)

       current_root = find(pos)

       if current_root != r_root:

           parent[r_root] = current_root

           sum_ar[current_root] += sum_ar[r_root]

           left_ar[current_root] = min(left_ar[current_root], left_ar[r_root])

           right_ar[current_root] = max(right_ar[current_root], right_ar[r_root])

           current_sum = sum_ar[current_root]

   if current_sum > max_sum:

       max_sum = current_sum

   res.append(max_sum)

# generate output

output = []

for i in range(1, n+1):

   idx = n -i -1

   if idx >=0:

       output.append(res[idx])

   else:

       output.append(0)

for num in output:

   print(num)

But the find function is not defined. So we need to implement it.

Implementing find with path compression:

def find(u):

   while parent[u] != u:

       parent[u] = parent[parent[u]]

       u = parent[u]

   return u

But this is a standard DSU find with path compression.

But in Python, for large n, recursion depth is limited, so iterative implementation is better.

So integrating the find function into the code.

But how to handle this in Python.

Thus, the complete code would be:

Read the input, then define the find function.

Wait, but in Python, functions can be defined inside the code.

Thus, here's the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    destroy_order = list(map(int, input_stream.readline().rstrip("\n").split()))

    reversed_order = list(reversed(destroy_order))

    parent = [i for i in range(n)]  # initializing parent, but during processing, it's reset.

    sum_ar = [0]*n

    left_ar = [0]*n

    right_ar = [0]*n

    active = [False]*n

    def find(u):

        while parent[u] != u:

            parent[u] = parent[parent[u]]

            u = parent[u]

        return u

    max_sum = 0

    res = []

    for x in reversed_order:

        pos = x - 1

        active[pos] = True

        # Initialize parent, sum, left, right for this node

        parent[pos] = pos

        sum_ar[pos] = a[pos]

        left_ar[pos] = pos

        right_ar[pos] = pos

        current_sum = a[pos]

        # Check left neighbor

        if pos > 0 and active[pos-1]:

            l_root = find(pos -1)

            # Merge pos into l_root

            parent[pos] = l_root

            sum_ar[l_root] += sum_ar[pos]

            right_ar[l_root] = pos

            current_sum = sum_ar[l_root]

        # Check right neighbor

        if pos < n-1 and active[pos+1]:

            r_root = find(pos+1)

            current_root = find(pos)

            if current_root != r_root:

                parent[r_root] = current_root

                sum_ar[current_root] += sum_ar[r_root]

                left_ar[current_root] = min(left_ar[current_root], left_ar[r_root])

                right_ar[current_root] = max(right_ar[current_root], right_ar[r_root])

                current_sum = sum_ar[current_root]

        if current_sum > max_sum:

            max_sum = current_sum

        res.append(max_sum)

    output = []

    for i in range(1, n+1):

        idx = n - i -1

        if idx >=0:

            output.append(res[idx])

        else:

            output.append(0)

    for num in output:

        print(num, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2 3 4 5
4 2 3 5 1
""",
            "output": \
"""\
6
5
5
1
0
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

Thus, the code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
destroy_order = list(map(int, input().split()))
reversed_order = list(reversed(destroy_order))

parent = list(range(n))
sum_ar = [0] * n
left_ar = [0] * n
right_ar = [0] * n
active = [False] * n

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

max_sum = 0
res = []

for x in reversed_order:
    pos = x - 1
    active[pos] = True
    parent[pos] = pos
    sum_ar[pos] = a[pos]
    left_ar[pos] = pos
    right_ar[pos] = pos
    current_sum = a[pos]
    
    # Check left neighbor
    if pos > 0 and active[pos - 1]:
        l_root = find(pos - 1)
        parent[pos] = l_root
        sum_ar[l_root] += sum_ar[pos]
        right_ar[l_root] = pos
        current_sum = sum_ar[l_root]
    
    # Check right neighbor
    if pos < n - 1 and active[pos + 1]:
        r_root = find(pos + 1)
        current_root = find(pos)
        if current_root != r_root:
            parent[r_root] = current_root
            sum_ar[current_root] += sum_ar[r_root]
            left_ar[current_root] = min(left_ar[current_root], left_ar[r_root])
            right_ar[current_root] = max(right_ar[current_root], right_ar[r_root])
            current_sum = sum_ar[current_root]
    
    if current_sum > max_sum:
        max_sum = current_sum
    res.append(max_sum)

# Generate output
output = []
for i in range(1, n + 1):
    idx = n - i - 1
    output.append(res[idx] if idx >= 0 else 0)

for num in output:
    print(num)
```
