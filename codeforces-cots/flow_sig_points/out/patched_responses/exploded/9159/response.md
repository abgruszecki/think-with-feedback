<think>
Okay, I need to solve this problem where Grigory can perform synchronization operations on his stones to see if he can reach Andrew's configuration. Let's think about what these operations do.

So, when you synchronize an inner stone i (so i is between 2 and n-1), the charge of that stone becomes c[i-1] + c[i+1] - c[i]. Hmm. What's the effect of this operation? Let's see. For example, if I have three stones with charges a, b, c, and I synchronize the middle one, the new charge is a + c - b. Then the new triplet is a, (a+c -b), c. 

Wait, but what's the invariant here? Because each operation only affects the middle stone. Maybe there's some invariant that stays the same no matter how many operations are performed. For example, maybe certain properties of the array can't change, which would determine whether the transformation is possible.

Let's think about the parity of the array. Or maybe some linear combination that's preserved. Let's consider the parity of the positions. Wait, for example, if we have an array c1, c2, c3, c4. Let's see what happens when we perform operations on different positions.

For instance, if we synchronize position 2 in a 4-stone setup:

Original: c1, c2, c3, c4
After syncing 2: c1, (c1 + c3 - c2), c3, c4.

Then, if we sync position 3:
c1, (c1 + c3 - c2), ( (c1 + c3 - c2) + c4 - c3 ), c4
= c1, (c1 + c3 - c2), (c1 + c4 - c2), c4.

Hmm. But what's the overall pattern here?

Alternatively, maybe the sum of certain elements remains the same. Let's think about the sum of all elements. When you perform a sync on position i, the new value is c[i-1] + c[i+1] - c[i]. So the total sum becomes sum (old c) - c[i] + (c[i-1] + c[i+1] - c[i]) = sum - c[i] + c[i-1] + c[i+1] - c[i] = sum + c[i-1] + c[i+1] - 2c[i]. Wait, but that's not the same as the original sum. So the sum is not preserved. So that's not an invariant.

Hmm. So maybe there's another invariant. Let's think about the difference between adjacent elements. Or maybe something else.

Wait, let's model the operation as a linear transformation. Suppose after each operation, the array changes in some way. Let's see: the operation replaces c_i with c_{i-1} + c_{i+1} - c_i. So for example, in a 3-element array, after performing an operation on position 2, the array becomes [c1, c1 + c3 - c2, c3]. The sum of the array is now c1 + (c1 + c3 - c2) + c3 = 2c1 + 2c3 - c2. Which is different from the original sum of c1 + c2 + c3. So the sum isn't preserved. Therefore, the sum can change, so it's not part of the invariant.

Let me think again. Let's see if applying the operation multiple times can lead back to the original array. For example, if I apply the same operation twice. Let's take the initial array [a, b, c]. After first sync on middle: [a, a + c - b, c]. Then, if I sync again the middle element: [a, (a + c - (a + c - b)), c] → [a, b, c]. So two operations on the same position bring it back. So the operation is its own inverse. So applying it an even number of times cancels out, and an odd number of times is like applying it once. Interesting.

But how does this help in determining whether the target array can be reached from the initial array?

Let's consider that the order of operations might not matter. Or maybe the parity of the number of operations on each position matters. But even that's unclear.

Alternatively, perhaps the parity of the number of operations applied to each position affects the outcome. But given that the problem allows any number of operations (including zero), maybe there's a way to model the possible transformations.

Wait, but the problem allows any number of operations, and each operation can be on any inner position. So the key is to find if the initial array can be transformed into the target array through any sequence of such operations.

Hmm. Let's think about the effect of the operations on the array. Let's see if there's a pattern here. For example, in the first sample input:

After synchronizing position 3, the array becomes 7, 2, 10, 12. Then, synchronizing position 2 gives 7, 15, 10, 12. Which matches the target. So the sequence of operations can affect elements in a way that propagates changes.

But how to model all possible changes? It's tricky because each operation can be applied multiple times and in different orders.

Wait, perhaps there's a pattern in the parity of the positions. For example, let's consider the first and last elements. When you perform any operation, the first and last elements are never modified. Because when you sync position i (between 2 and n-1), you only modify c_i. So, the first element c_1 and the last element c_n remain the same throughout all operations. Therefore, for the problem's answer to be "Yes", the first and last elements of c and t must be equal. If c[0] != t[0] or c[-1] != t[-1], then it's impossible, and we can immediately return "No".

That's a crucial observation. Let's test this against the sample inputs.

First sample input:
c is [7, 2, 4, 12], t is [7, 15, 10, 12]. The first elements are 7 and 7, last are 12 and 12. So that's good.

Second sample input: c is [4,4,4], t is [1,2,3]. The first elements are 4 vs 1 → no match, so answer is No. Which matches the sample output.

So that's a necessary condition. So first step: check if c[0] == t[0] and c[-1] == t[-1]. If not, output No.

If they are equal, then we need to check the rest of the elements. But how?

So the rest of the elements (from 2 to n-1) can be modified through the operations. But what's the invariant here?

Let's think of the array after any number of operations. The first and last elements are fixed. What about the other elements? Let's see if there's some invariant that's preserved.

Wait, maybe the parity of the positions. For example, for even-length arrays, certain combinations may be preserved. Or maybe the even and odd indexed elements (excluding first and last) have some invariant.

Alternatively, perhaps the sequence of differences between adjacent elements has some invariant. Let's try.

Let's say for the array [a, b, c, d], after any operations, the differences might have some preserved properties. Let's compute the initial differences: a, b - a, c - b, d - c.

When we perform a sync on position 2, the array becomes [a, a + c - b, c, d]. The new differences are a, (a + c - b) - a = c - b, c - (a + c - b) = b - a, d - c. So the differences between positions 1-2 is c - b, between 2-3 is b - a. So the differences between adjacent elements have swapped. Hmm. So the original differences for positions 1-2 and 2-3 were (b -a) and (c - b). After the operation, they become (c - b) and (b -a). So the differences are swapped. 

What about the differences further out? Let's see. For a 4-element array, after syncing position 3. Original array: [a, b, c, d]. After syncing 3, it becomes [a, b, (b + d - c), d]. The differences then are: a, b - a, (b +d -c) - b = d -c, d - (b +d -c) = c -b. So the differences between 3-4 is now c - b, which is the original difference between 2-3. So again, the differences between positions 2-3 and 3-4 are swapped.

So this suggests that when you perform a synchronization on position i, the differences between (i-1, i) and (i, i+1) are swapped. Because the operation affects the i-th element, which is between i-1 and i+1. So the differences for (i-1, i) and (i, i+1) before the operation are d1 and d2. After the operation, they become d2 and d1. So each operation on position i swaps the adjacent differences d_{i-1} and d_i. 

Wait, but in the example for a 3-element array, when you sync position 2, the differences between 1-2 and 2-3 are swapped. So the initial differences are (b -a) and (c -b). After the operation, the array is [a, a + c -b, c], so the differences are (a + c -b -a) = c - b, and c - (a + c -b) = -a + b. Which is (c - b) and (b - a). So the original differences (d1, d2) become (d2, -d1) ? Wait, no. Wait, original differences: d1 = b -a, d2 = c -b. After the operation, the differences are ( (a + c -b) - a ) = c - b (which is d2), and (c - (a + c -b )) = ( -a + b ) = -(a - b) = -d1. So yes, the new differences are d2 and -d1. Hmm, that's different from the 4-element case. So maybe this approach isn't leading me anywhere.

Alternatively, perhaps the key is to model the problem as a system where certain operations can be applied, and find if the target can be reached.

But given the problem constraints (n up to 1e5), we need an O(n) approach. So brute-force checking is impossible.

Let me think again. Let's see what the operation does. Each operation on position i inverts the value of c_i to c_{i-1} + c_{i+1} - c_i. Let's look for invariants in the array. Let's consider the parity of the number of times each position is operated. Because applying the same operation twice cancels its effect (since the operation is its own inverse). For example, applying the operation to position i twice gives back the original array. So the net effect is the same as not applying it. Therefore, the order of applying operations (even number of times) doesn't matter, and the parity (whether you apply it even or odd times) is what determines the outcome.

But since each operation can be applied any number of times, the overall effect depends on the parity of operations applied to each position. Because even applications cancel out, and odd applications are equivalent to one application.

But how does applying operations on different positions affect the array? Let's model this.

Suppose we have the array c_1, c_2, c_3, c_4, c_5.

If we apply an operation on position 2, the new array is c_1, (c_1 + c_3 - c_2), c_3, c_4, c_5.

Then, applying an operation on position 3:

The new array becomes:

c_1, (c_1 + c_3 - c_2), ( (c_1 + c_3 - c_2) + c_4 - c_3 ), c_4, c_5 → c_1, (c_1 + c_3 - c_2), (c_1 + c_4 - c_2 ), c_4, c5.

Hmm. So each operation on a position affects that position's value based on its current neighbors. But after multiple operations, how do these changes accumulate?

Alternatively, perhaps the parity of the positions (even or odd) affects the possible transformations. For example, maybe after applying certain operations, the array can be transformed in such a way that even and odd indexed elements (excluding first and last) can be adjusted in a certain way.

Another approach: think about the possible transformations for even and odd n. Let's see for small n.

Case 1: n=2. Then there are no inner stones. So the array can't be changed. So c must equal t.

Case 2: n=3. Only position 2 can be synced. Each operation on position 2 flips it to c1 + c3 - c2. Applying the operation again brings it back. So after any number of operations, the possible configurations are either the original or the one after one operation. So the possible target for position 2 is either the original c2 or (c1 + c3 - c2). So for n=3, to get the target, the first and last elements must match, and the middle element must be either equal to the original or to (c1 + c3 - c2). The sample input 2 is n=3. The target for position 2 is 2. Original c2 is 4, and (4 + 4 -4) =4. So the possible values are 4. So if the target is 2, it's impossible.

So for n=3, it's straightforward.

Now, for larger n. Let's think about n=4. Let's see. The operations can be applied on positions 2 and 3. How do these operations affect the array?

For example, applying the operation on position 2, then position 3. Let's see:

Original array: [a, b, c, d]

After syncing position 2: [a, a + c - b, c, d]

Then syncing position 3: [a, a + c - b, (a + c - b) + d - c, d] → [a, a + c - b, a + d - b, d ]

So the middle two elements are now (a + c - b) and (a + d - b).

Hmm. Now, what's the difference between these two elements? Let's compute:

(a + c - b) and (a + d - b) → their difference is (a + d - b) - (a + c - b) = d - c.

Which is the original difference between c and d.

Alternatively, maybe there's a pattern in the parity of the array.

Another idea: the parity of the number of times each position is operated. For example, applying an operation on position i and then on position i+1. How does this affect the array?

But this line of thinking might not lead to an efficient solution.

Let's think again. Since the first and last elements must be the same between c and t, we can first check that. Then, for the remaining elements (positions 2 to n-1), we need to see if they can be transformed into the target.

Now, considering that each operation on position i affects c_i, and the effect is that c_i becomes c_{i-1} + c_{i+1} - c_i. Let's look for a pattern here. For example, the sum of c_i and c_{i} (after operation) is c_{i-1} + c_{i+1} - c_i + c_i = c_{i-1} + c_{i+1}. So this suggests that the sum of c_i and the new value is the sum of its neighbors. Not sure if that helps.

Alternatively, perhaps the parity of the array in some transformed way is preserved. Let's model the array as a combination of certain variables that are invariant under the operations.

Wait, when you perform an operation on position i, the new value is c_{i} → c_{i-1} + c_{i+1} - c_i. Let's see what the difference between the new c_i and the original c_i is. The change is (c_{i-1} + c_{i+1} - c_i) - c_i = c_{i-1} + c_{i+1} - 2c_i. So the change is (c_{i-1} - c_i) + (c_{i+1} - c_i) = (c_{i-1} + c_{i+1} - 2c_i). But how does this affect the rest of the array?

Another approach: Let's consider the possible transformations as linear operations and look for a basis. However, this might get complicated for large n.

Alternatively, perhaps the key is that the order of operations doesn't matter. For example, applying operations on position i and then j might be equivalent to applying them in the reverse order. If that's the case, then the final state depends only on the parity of the number of times each position is operated.

But how does applying multiple operations on different positions affect the array?

Let's try with n=4. Suppose we have the initial array [a, b, c, d]. Apply operation on position 2, then on position 3.

First operation (pos 2): [a, a + c - b, c, d]

Second operation (pos3): [a, a + c - b, (a + c -b) + d - c, d] → [a, a + c -b, a + d - b, d]

Now, apply operation on position 2 again:

After operation on pos2: [a, a + (a + d -b) - (a + c -b ), a + d -b, d ] → [a, (a + a + d -b - a -c +b ), ... ] → [a, (a + d - c), a +d -b, d ]

Hmm. So each operation can be combined in different ways, making it hard to model.

Alternatively, perhaps the parity of the number of operations applied to each position is the key. Since applying a pair of operations on the same position cancels out, the overall effect is determined by the parity (even or odd) of operations on each position. However, how do these parities interact with each other?

For example, applying an operation on position i and then on position i+1. Let's see.

Original array: positions i-1, i, i+1, i+2.

After operation on i: the value at i becomes (i-1) + (i+1) - i → the new i is (i-1) + (i+1) - i = (i-1 + i+1) - i = 2i - i = i → Wait, no. Wait, the values are a, b, c, d. After applying operation on position i=2, the value becomes a + c -b.

But applying operation on position i=2 and then i=3 may have a certain combined effect.

But this is getting too complex. Perhaps there's a mathematical pattern here.

Let me think: what is the effect of applying an operation on position i. Let's model it as a linear transformation.

The operation is c_i' = c_{i-1} + c_{i+1} - c_i.

So, for each position i, the new value depends on its neighbors. Let's see how this affects the entire array.

But how can this be modeled? Let's imagine that each operation is a transformation that can be applied, and we need to find if the target can be reached through any combination of these transformations.

Alternatively, perhaps the parity of the array's possible transformations depends on the parity of the positions. For example, for even and odd positions, the possible transformations might be different.

Another idea: since the first and last elements are fixed, perhaps the problem can be transformed into checking whether the transformed array (c) can reach the target array (t) by flipping certain positions. But how?

Alternatively, considering that each operation on position i can be seen as flipping the value of c_i based on its neighbors. Let's imagine that for each position i (2 <= i <=n-1), we can choose whether to apply the operation (flip) or not. But since applying it an even number of times cancels out, each position can be either flipped once or not at all. However, flipping one position may affect the possibility of flipping another.

Wait, but flipping position i changes the value of c_i, which in turn affects the neighbors when flipping adjacent positions. So the order of flipping matters.

Hmm. This complicates things.

Wait, but perhaps the problem can be viewed as a system of equations. For each position i (2 <= i <= n-1), the target t_i must equal to the original c_i modified by some combination of flips. But how?

Alternatively, perhaps the parity of the number of flips applied to the positions affects the possible values. For example, each flip on position i changes the value of c_i, and perhaps the parity of the number of flips in certain positions determines the final array.

But given that the order of operations can affect the outcome, this approach might not work.

Another approach: let's model the problem as a graph where each state is a possible array configuration, and edges are operations. But this is infeasible for n=1e5.

We need a smarter way.

Let's think of the process of applying operations. Each operation can be applied multiple times, but the key is that each operation is its own inverse. So the order of applying operations in pairs doesn't matter, but the parity (whether you apply an even or odd number of operations) does.

But how to model the effect of applying a set of operations (each applied once or not) in some order.

Alternatively, perhaps the parity of the number of operations applied to each position is not important, but the cumulative effect of applying certain operations is. For example, maybe the parity of the number of operations applied to even positions and the parity applied to odd positions matters.

Wait, let's take a small example. n=4. Apply operation on position 2 and then on position 3. What's the effect?

Original: a, b, c, d.

After 2: a, a + c - b, c, d.

After 3: a, a + c -b, (a + c -b) + d -c, d → a, a +c -b, a + d -b, d.

Now, if we apply operation on 2 again:

a, (a + (a +d -b) ) - (a +c -b) ), a +d -b, d → a, a +a +d -b -a -c +b → a, (a +d -c), a +d -b, d.

Hmm. Not sure.

Alternatively, perhaps there's an invariant for each position i (2 <= i <=n-1) that is a linear combination of the original array. For example, after any number of operations, certain linear combinations of elements remain the same.

For instance, perhaps the sum of c_i and c_{i+1} for even i is preserved. Or some other combination.

Alternatively, think about the problem as being similar to the inversion problem. For example, each operation inverts a certain value based on its neighbors, leading to a possible parity-based invariant.

Alternatively, consider that each operation on position i affects the value of c_i, but also affects the neighboring positions when other operations are applied. For example, flipping position i and then flipping position i-1 would affect c_i-1 and c_i.

This seems complicated. Let's think about the problem from the end. Suppose we have the target array t. What's the condition that allows it to be transformed from the initial array c?

We know that c[0] must equal t[0], c[-1] must equal t[-1]. For the other positions, perhaps the parity of certain sums or differences must match between c and t.

Alternatively, think about applying the operations in reverse. Suppose we start from the target array and try to reach the initial array. Each operation is the same (since applying it again reverses the previous step). So the problem is symmetric. So the same conditions apply.

Another idea: For the positions 2 to n-1, the parity of the number of operations applied to each position can be determined based on the required changes. But since applying an operation on position i affects the value of c_i, but also affects the ability to apply operations on neighboring positions (since their neighbors' values change), this might not be straightforward.

Wait, but perhaps for even n, the parity of the array's possible transformations is different compared to odd n.

Alternatively, consider that after any number of operations, the array's elements can be expressed in terms of the original elements. For example, the value of each element is a linear combination of the original elements. But this might be difficult for large n.

Let's try to find a pattern. For example, after applying an operation on position i, the value of c_i becomes c_{i-1} + c_{i+1} - c_i. Let's see what happens if we apply this operation again. The new value would be (c_{i-1} + c_{i+1} - c_i) → applying the operation again, the new value is (c_{i-1} + c_{i+1} - c_{i-1} - c_{i+1} + c_i ) ) → c_i. So applying the operation twice returns to the original value. So each operation is an involution.

Therefore, for each position, applying the operation an even number of times is equivalent to not applying it at all, and applying it once is equivalent to flipping the value once.

But since the order of flipping affects the values (because flipping position i changes the neighbors of i, which in turn affects the result of flipping positions i-1 or i+1), the parity alone isn't sufficient to model the problem.

Hmm. So this suggests that the problem may require checking some invariants for the array, beyond the first and last elements.

Wait, let's consider the following. For each position i (2 <= i <= n-1), after any number of operations, the value of c_i can be written as a linear combination of the original array. However, given the nature of the operations, perhaps the parity of the number of operations applied to i and its adjacent positions affects the outcome. This might be too complex.

Alternatively, perhaps for each position i (2 <= i <=n-1), the difference between the current value and the original can be expressed in terms of the differences of the neighboring elements.

But I'm stuck here. Let's think of another approach.

Wait, let's model the operation as a sequence of swaps. For example, when you apply the operation to position i, you are swapping certain values. Let's look at the differences between adjacent elements again.

Let me compute the differences for the array after an operation. For example, original array: [a, b, c, d]. After operation on position 2, it becomes [a, a + c - b, c, d]. The differences are a (for position 1-2: a remains first), (a + c - b -a) = c - b, (c - (a + c -b)) = -a +b, and d - c.

So the differences between positions 2-3 have changed from (c - b) to (c - (a + c -b)) = -a +b.

Hmm. Let's compare the original and new differences. The original differences are (b -a, c -b, d -c). After the operation on position 2, the differences are ( (a + c -b -a) = c -b, (c - (a + c -b) ) = -a +b, d -c ). So the differences for positions 2-3 are swapped and negated.

Wait, original difference between 2 and 3 is (c -b). After the operation, the difference between 2 and 3 is ( (a + c -b) and c) → c - (a + c -b) = -a +b. So the new difference is -(a -b) = - (a -b) = - ( (b -a) - 2b + ...? Not sure.

Alternatively, for positions i-1, i, i+1:

Original differences: (c_i-1 - c_i-2), (c_i - c_i-1), (c_i+1 - c_i).

After applying operation on i, the new c_i is (c_i-1 + c_i+1 - c_i). The new differences for positions i-1 and i are:

(c_i-1 + c_i+1 - c_i) - c_i-1 = c_i+1 - c_i.

And for i and i+1:

c_i+1 - (c_i-1 + c_i+1 - c_i) = c_i-1 - c_i.

So the differences between i-1 and i, and i and i+1 have been swapped. 

Wait, the original differences between i-1 and i is (c_i - c_i-1). The new difference between i-1 and i is ( (c_i-1 + c_i+1 - c_i) - c_i-1 ) = c_i+1 - c_i. Which is the original difference between i and i+1. And the new difference between i and i+1 is (c_i+1 - (c_i-1 + c_i+1 - c_i )) = c_i - c_i-1. So the two differences are swapped. 

So applying an operation on position i swaps the differences between (i-1, i) and (i, i+1). 

Ah! This is a key insight. Each operation on position i swaps the two adjacent differences. Because the difference between i-1 and i was (c_i - c_i-1), and after the operation, it's (c_i+1 - c_i). So the two differences are swapped.

But wait, in the example above, after the operation on i=2:

Original differences (for i=1-2, 2-3, 3-4) were (b -a, c -b, d -c).

After the operation on i=2, the differences become ( (a +c -b -a) = c -b, (c - (a +c -b )) = -a +b, (d -c) ). So the first two differences (positions 1-2 and 2-3) are swapped, but the third difference remains the same. Wait, that's not matching the earlier statement. Hmm.

Wait, the new differences after the operation on i=2 are:

- Position 1-2: c[2] - c[1] = (a +c -b) - a = c -b. Which was the original difference between 2-3.

- Position 2-3: c[3] - c[2] = c - (a +c -b) = -a +b. Which was the original difference between 1-2 (b -a) but multiplied by -1.

Hmm, so the two differences are not exactly swapped. The first difference becomes the original second difference, and the second difference becomes the negative of the original first difference.

Wait, this contradicts the earlier conclusion. So perhaps the initial observation was incorrect. 

Let me re-express the differences.

Original differences:

For positions i-1 and i: d1 = c_i - c_{i-1}

For positions i and i+1: d2 = c_{i+1} - c_i

After the operation on i, the new c_i is c_{i-1} + c_{i+1} - c_i.

The new differences:

For positions i-1 and i: new_c_i - c_{i-1} = (c_{i-1} + c_{i+1} - c_i) - c_{i-1} } = c_{i+1} - c_i = d2.

For positions i and i+1: c_{i+1} - new_c_i = c_{i+1} - (c_{i-1} + c_{i+1} - c_i) ) = -c_{i-1} + c_i = -(c_{i-1} - c_i) = -d1.

So after the operation on i, the two differences d1 and d2 are replaced by d2 and -d1. 

So the differences are transformed as follows: (d1, d2) → (d2, -d1).

This is an important observation. So applying the operation on position i swaps the adjacent differences and negates the second one. Or wait, after the operation, the first difference becomes d2, the second becomes -d1. 

So this transformation is a rotation with negation. So for example, applying the operation once on position i transforms the pair (d1, d2) into (d2, -d1). Applying it again would then take (d2, -d1) → (-d1, -d2). And applying it a third time would turn into (-d2, d1), and a fourth time back to (d1, d2). 

So after applying the operation twice, the differences become (-d1, -d2). Applying four times brings them back. So the parity of the number of operations on i determines how the differences are transformed.

This seems like a key invariant. So the operation on position i affects the two adjacent differences (d1, d2) by swapping them and negating the new second difference. 

But how does this help us determine whether the target array can be reached?

Let's think about the entire sequence of differences in the array. For the original array, we have differences d_1, d_2, ..., d_{n-1}, where d_i = c_{i+1} - c_i}.

For the target array, the differences must be t_1, t_2, ..., t_{n-1}, where t_i = t_{i+1} - t_i}.

But in the original array, the first and last elements are fixed. So the first difference (d_1) and the last difference (d_{n-1}) are fixed? Wait, no. Because the first element is c_1, which must equal t_1. The last element is c_n, which must equal t_n. So the sum of the differences in the original array must be equal to the sum of the differences in the target array. Because the sum of the differences is c_n - c_1. But since c_1 = t_1 and c_n = t_n, the sum of the differences for the original and target arrays must be the same. So sum(d_i) = sum(t_i). But this is already covered by the first and last elements being equal.

But for the other differences (positions 2 to n-2), we need to see if the operations can transform the original differences into the target differences. But each operation on position i affects the differences i-1 and i. 

So the problem reduces to transforming the original differences (d_2, d_3, ..., d_{n-2}) into the target differences (t_2, t_3, ..., t_{n-2}) through a series of operations that swap and negate pairs of differences. But how?

Wait, the operation on position i affects the differences i-1 and i. For example, operation on position i=2 affects differences d_1 and d_2 (assuming the differences are 0-based or 1-based). Wait, the differences are d_1 = c_2 - c_1, d_2 = c_3 - c_2, ..., d_{n-1} = c_n - c_{n-1}. 

When you perform an operation on position i (which is between positions i-1 and i+1), you are affecting the differences d_{i-1} and d_i. Because the operation changes c_i, which affects both d_{i-1} (since it's c_i - c_{i-1}) and d_i (since it's c_{i+1} - c_i).

So for the array, the differences after an operation on position i are transformed as follows:

Original differences for positions (i-2, i-1, i, i+1):

... d_{i-2}, d_{i-1}, d_i, d_{i+1} ...

After operation on i, the differences i-1 and i become d_i and -d_{i-1}, respectively.

So, the operation swaps d_{i-1} and d_i, and negates the new d_i (the one that was originally d_{i-1}).

Wait, no. Let me re-examine:

After the operation, the new d_{i-1} is (new c_i - c_{i-1}) = (c_{i-1} + c_{i+1} - c_i) - c_{i-1} = c_{i+1} - c_i = d_i.

The new d_i is (c_{i+1} - new c_i) = c_{i+1} - (c_{i-1} + c_{i+1} - c_i) = c_i - c_{i-1} = d_{i-1} (original). But wait, no. Because original d_{i-1} was c_i - c_{i-1}. The new d_i is c_{i+1} - new_c_i = c_{i+1} - (c_{i-1} + c_{i+1} - c_i) → simplifying:

c_{i+1} - c_{i-1} - c_{i+1} + c_i → c_i - c_{i-1} → which is the original d_{i-1}.

Wait, so the new d_{i-1} is d_i (original), and the new d_i is d_{i-1} (original). So this suggests that the two differences are swapped. But earlier analysis said that they are swapped and one is negated. Which is correct?

Wait, let's take an example. Original array: [a, b, c, d]. Differences are [b-a, c-b, d-c].

Operation on position 2 (i=2) changes the array to [a, a + c -b, c, d]. New differences are ( (a + c -b -a) = c -b, c - (a + c -b) = -a + b, d - c).

So the new d_1 (which is the difference between positions 1-2) is c -b, which was the original d_2 (difference between 2-3). The new d_2 (difference between 2-3) is -a +b, which is -(b -a) = -d_1 (original).

So yes, after the operation on i=2, the differences d_{i-1} (d_1) and d_i (d_2) become d_i (original) and -d_{i-1} (original).

So the transformation is (d_{i-1}, d_i) → (d_i, -d_{i-1}).

So this is the pattern. So each time you perform an operation on position i, the adjacent differences d_{i-1} and d_i are transformed to (d_i, -d_{i-1}).

This is crucial. So the operation on position i swaps the two differences and negates the second one (which was the original d_{i-1}).

So, for example, if you perform the operation once on i, the pair becomes (d_i, -d_{i-1}).

If you perform it again, the pair becomes (-d_{i-1}, -d_i).

Third time: (-d_i, d_{i-1}).

Fourth time: (d_{i-1}, d_i).

So after four operations, the original pair is restored.

So this transformation is cyclic with period 4.

The question is, how can we use this to model the possible transformations of the differences. Since each operation affects a pair of differences in this way, the problem now reduces to whether we can transform the original differences into the target differences by applying a series of such transformations.

But how do we model this for all the differences in the array?

The key observation is that applying an operation on position i affects the pair (d_{i-1}, d_i). So the order in which operations are applied is important. For example, applying an operation on position i and then on position i+1 can have different effects than applying them in reverse.

But with large n, we need a way to model this efficiently.

Another observation: For the problem to be possible, the differences in the target array must be reachable from the original differences via these transformations. But given the complexity of the transformations, perhaps there's a pattern that allows us to check for certain invariants.

For example, let's consider that each operation on position i toggles the pair (d_{i-1}, d_i) through the transformation (d_i, -d_{i-1}).

But how can multiple operations on different positions affect the array of differences?

Let's consider that each operation on position i affects a pair of differences, and this can be done any number of times. But each operation on i toggles the pair's state. However, the effect depends on the current state of the pair.

But this seems difficult to model for large n. So perhaps there's an invariant that applies to each pair of differences.

Another idea: For each pair of consecutive differences (d_{i}, d_{i+1}), the parity of some combination is preserved. For example, the sum of their squares or their product.

Wait, let's compute the product of the two differences before and after an operation. 

Original pair (a, b). After operation, the pair becomes (b, -a). Their product is a*b. After transformation, the product is b*(-a) = -a*b. So the product's sign is flipped. 

But the square of the product (a*b)^2 is preserved, as (-a*b)^2 = (a*b)^2. So the magnitude of the product is preserved.

So the product of the pair (d_{i}, d_{i+1}) is preserved modulo sign.

But how does this help us? Because each operation on position i+1 affects the pair (d_i, d_{i+1} ), which would change their product's sign. So this is not a global invariant.

Alternatively, perhaps for each pair of differences (d_{i}, d_{i+1}), their product modulo the operations is preserved in absolute value, but the sign can change. However, this seems not to directly help in determining the possibility.

Alternatively, let's think in terms of the entire array of differences. Each operation can be viewed as a transformation on two consecutive differences, swapping them and negating the second. 

For example, applying the operation on position i transforms (..., a, b, ...) into (..., b, -a, ...).

But this transformation is similar to a rotation with negation. 

So the problem is now to determine whether we can reach the target difference array from the original difference array by applying a series of such swaps and negations on adjacent pairs.

This is similar to certain permutation and sign-flip puzzles, but with the added complexity of the transformations.

But for large n, we need an efficient way to check this.

Another approach: Let's model the differences for the original array and the target array. For positions 1 and n-1, the differences are fixed (since the first and last elements are fixed). For the other differences (positions 2 to n-2), we can apply the transformations.

But wait, the first difference d_1 = c_2 - c_1, but since c_1 is fixed, and c_2 can be modified by operations on position 2. Wait, no. Because the operation on position 2 affects d_1 and d_2. For example, applying an operation on position 2 changes d_1 and d_2. So the first difference (d_1) is not fixed. So this line of thinking is incorrect.

Ah, my mistake. Earlier, I thought that the first and last elements are fixed, which is correct. But the first difference d_1 is c_2 - c_1. Since c_1 is fixed, but c_2 can change (through operations on position 2), the first difference can vary. Similarly, the last difference d_{n-1} = c_n - c_{n-1} can change (since c_{n-1} can be modified by operations on position n-1). So the first and last differences are not fixed. Only the sum of all differences (which equals c_n - c_1) is fixed. But since c_n and c_1 are fixed, the sum of all differences is fixed. But this doesn't directly help.

So, the initial approach of checking the first and last elements is correct, but beyond that, the differences can vary.

But how to check whether the target can be achieved?

Another key insight: Each operation on position i can be applied any number of times, but since it's an involution, applying it even times is the same as not applying it. So the parity of the number of times each position is operated is important. But how to model this for large n?

Alternatively, think about the following: Each operation on position i transforms the differences d_{i-1} and d_i. So for the problem to have a solution, the original differences must be able to reach the target differences through a series of such transformations.

But for large n, we need an efficient way to model these transformations.

Let me think of the problem in terms of possible transformations for the differences. For example, the difference array after any number of operations can be obtained by a series of swap-and-negate operations on adjacent pairs. 

But the order in which these operations are applied will affect the final array. 

For example, applying the operation on position 2, then position 3, then position 2 again.

But this seems difficult to model.

Alternatively, perhaps the parity of the number of operations applied to each position affects the final array. For example, applying an operation on position i an odd number of times will swap and negate the pair of differences. Applying it even times will return to the original state.

But this is not accurate, because applying the operation on position i twice transforms the pair (d_i-1, d_i) as follows:

First operation: (d_i-1, d_i) → (d_i, -d_i-1)

Second operation: (d_i, -d_i-1) → (-d_i-1, -d_i)

So after two operations, the pair becomes (-d_i-1, -d_i).

So applying the operation twice on the same position inverts the pair's signs.

Hmm. So the parity of the number of operations on a position affects how the pair is transformed. But even so, this makes it difficult to model for all positions.

Another idea: for the problem to be possible, the target difference array must be reachable from the original difference array through a series of swap and negate operations. But how to model this?

Let's consider the following: For each pair of differences (d_i-1, d_i), we can perform any number of operations, leading to certain possible transformations. For example, applying the operation once leads to (d_i, -d_i-1). Applying it again leads to (-d_i-1, -d_i). Applying it a third time leads to (-d_i, d_i-1), and a fourth time returns to (d_i-1, d_i).

So for each pair of consecutive differences, there are four possible states. The problem requires that all pairs of differences can be transformed into the target states through these operations, considering that each operation affects a pair and possibly adjacent pairs.

But this is not tractable for large n.

Alternatively, perhaps the problem has a parity-based invariant. For example, for even and odd positions, certain properties must hold between the original and target arrays.

Wait, after the transformation of a pair (d_i, d_i+1) via an operation on position i+1, the new pair becomes (d_i+1, -d_i). So the sum of the pair changes: original sum is d_i + d_i+1, new sum is d_i+1 - d_i. This isn't preserved. So sum isn't an invariant.

Alternatively, perhaps the product of the entire difference array is preserved modulo some factor. But this seems unlikely.

Alternatively, perhaps the problem can be viewed as a graph where each node is a possible configuration of the difference array. But this is impossible for n=1e5.

Another approach: Let's model the difference array for the original and target. Let's call the original differences d and the target differences td. We need to check if d can be transformed into td via a series of swap-and-negate operations on adjacent pairs.

But how to do this efficiently?

Let's think of the difference array as a sequence. We need to transform it into the target sequence. Each operation allows us to swap two adjacent elements and negate the first element of the pair.

Wait, no. The operation on position i+1 affects the pair (d_i, d_{i+1}), replacing them with (d_{i+1}, -d_i). So the first element becomes the second, and the second becomes the negative of the first.

This is similar to a rotation with a negation. 

If we can perform such operations in any order and any number of times, perhaps we can model the possible transformations as a series of these operations that can generate the target difference array.

But how to determine if this is possible?

Let's think of this as a permutation problem with sign changes. Each operation allows us to swap adjacent elements and multiply the first element by -1. But this is not exactly the case. For example, swapping the pair (a, b) into (b, -a). The first element becomes the second, and the second becomes the negative of the first. So the transformation is (a, b) → (b, -a).

If we can perform this transformation on any adjacent pair, what sequences are possible?

For example, consider a sequence of differences [a, b, c]. Applying the operation on position 2 (which affects the pair (a, b) → (b, -a)), resulting in [b, -a, c]. Then applying the operation on position 3 (which affects the pair (-a, c) → (c, a)), resulting in [b, c, a]. So the sequence becomes [b, c, a].

So, through a series of such operations, we can permute the elements and change their signs in certain ways. But how?

Another example: Let's say we have three differences [a, b, c]. Applying the operation on position 2: [b, -a, c]. Then apply operation on position 3: [b, c, a]. So the third element is now a. 

But this suggests that elements can be permuted with certain sign changes. 

But for larger n, the possible permutations and sign changes are not straightforward. 

This is getting quite complex. Perhaps there's a pattern here that can be exploited. For example, the parity of the number of inversions required to permute the array may be related to the sign changes. But I'm not sure.

Alternatively, perhaps the problem is possible if and only if the original and target difference arrays have the same multiset of absolute values, but with possible sign changes and permutations that can be achieved through the allowed operations. But this is not necessarily true.

For example, consider the original difference array [a, b, c], and target [b, -a, c]. This is achievable by one operation on position 2. But if the target is [a, c, -b], this might require operations on position 3.

But how to model this for large n.

Another idea: The allowed operations can be used to reverse the order of the differences, with sign changes. For example, applying operations on positions 2, 3, 4, ..., n-1 in sequence can reverse the array, but with each element negated.

But this is just a hypothesis.

Alternatively, the allowed operations allow us to perform any permutation of the differences, but each permutation has a certain parity of sign changes. For example, each swap of adjacent elements introduces a sign change. 

But this is getting into the realm of permutation parity and signed permutations. But given the time constraints, this line of thinking may not lead to a solution.

So, perhaps the key insight is that the allowed operations allow us to permute the differences in any order, but each swap of two adjacent elements introduces a negation of the elements. However, for even-length arrays, this might allow certain permutations and sign changes that are not possible for odd lengths.

But I'm not certain. 

Another idea: Let's consider the following. For the difference array, each operation on position i allows us to swap the i-1 and i-th differences, but with the latter being negated. For example, (a, b) → (b, -a). 

This is similar to generating a rotation of the elements with sign changes. 

But how can we model the effect of multiple such operations?

Alternatively, imagine that each difference can be moved to any position in the array, but each time it moves left or right, it picks up a certain number of sign changes. 

For example, to move a difference from position i to position j, you need to swap it with each adjacent pair between i and j. Each swap introduces a negation. So the total number of swaps would determine the sign. 

For example, moving a difference from position 2 to position 4:

Original array: [a, b, c, d]

Apply operation on position 3: [a, b, d, -c]

Apply operation on position 2: [b, -a, d, -c]

Now, the differences are [b, -a, d, -c]. Wait, no. The differences are:

d_1 = b - a_1. Wait, this is getting too complicated.

Alternatively, perhaps each element can be moved to any position in the array, but the number of sign changes depends on the number of times it crosses certain positions.

But again, this is not leading to a concrete solution.

Given the time constraints, perhaps it's best to look for an alternative approach. 

Another observation: Since each operation on position i affects the differences d_{i-1} and d_i, and leaves the rest of the array unchanged, the problem can be decomposed into individual pairs of differences. But this is not the case because operations on adjacent positions can affect overlapping pairs.

Alternatively, perhaps the order in which operations are applied can be rearranged so that we first process the array from left to right or right to left. 

For example, suppose we process the array from right to left. Applying operations on position i to fix the difference d_{i-1} and d_i. Once processed, moving leftwards may not affect the already processed differences. 

But how?

Let's consider that the target differences are [td_1, td_2, ..., td_{n-1}]. 

We can process the array from left to right. For each position i from 2 to n-1, we can apply operations on position i to transform the current differences into the desired td_{i-1} and td_i. 

But how?

For example, let's start with the original differences. For i=2, the current pair is (d_1, d_2). We need to transform this pair into (td_1, td_2). We can apply the operation on i=2 as many times as needed (once or not at all), since applying it twice would transform the pair into (-d_1, -d_2), which may not help. 

Alternatively, since applying the operation once transforms (d_1, d_2) into (d_2, -d_1), applying it again transforms into (-d_1, -d_2), etc. So there are four possible states for each pair. 

But this approach may not allow us to reach the desired state. 

Alternatively, perhaps the key is that the parity of the number of operations applied to each position i is determined by the desired transformation of the pair (d_{i-1}, d_i).

But this requires a way to compute the required number of operations for each pair. 

But given that each operation on position i affects the pair (d_{i-1}, d_i), and the next pair (d_i, d_{i+1}), we can't process the pairs in isolation. 

This seems like a dead end. 

Let me think of the problem differently. Suppose that the difference array can be transformed into any possible permutation with certain sign changes. In that case, the problem reduces to checking if the target differences are a permutation of the original differences with possible sign changes and reorderings. But this is not necessarily true. 

Alternatively, perhaps the following: For the problem to be possible, the multiset of absolute values of the differences (excluding the first and last) must match between the original and target arrays. 

But this is not necessarily the case, as in the first sample input. 

Original differences for sample 1:

c array is [7, 2, 4, 12], differences are (2-7) = -5, (4-2) = 2, (12-4)=8.

Target array is [7,15,10,12], differences are (15-7)=8, (10-15)=-5, (12-10)=2. 

The absolute values of the differences are 5,2,8 and 8,5,2. So they are the same, but reordered. 

So in this case, the multiset of absolute values matches. 

In the second sample input, the original array is [4,4,4], differences are 0 and 0. Target array is [1,2,3], differences are 1 and 1. The absolute values don't match, so it's impossible. 

So this suggests that the multiset of absolute values of the differences (excluding the first and last) must be the same for the original and target arrays. But wait, in the first sample, the first and last differences are allowed to vary. But the first and last elements are fixed. 

Wait, no. For the first sample, the first and last elements are fixed, but the first difference (d_1) is 2-7 = -5 in the original. In the target, it's 15-7 =8. So the first difference has a different absolute value. But the sample output is "Yes".

So this suggests that the first and last differences can change, provided that the first and last elements of the array are fixed. 

So the multiset idea is not correct. 

This indicates that there's no such invariant based on the absolute values. 

Thus, I'm stuck. I need to find another approach.

Let me look back at the initial example. 

Sample input 1:

Original array: [7, 2, 4, 12], target array: [7, 15, 10, 12].

The first and last elements are the same. The differences for the original are:

d1 = 2-7 = -5

d2 =4-2 = 2

d3 =12-4 =8

The target differences are:

td1=15-7=8

td2=10-15=-5

td3=12-10=2

So the target differences are [8, -5, 2]. The original differences are [-5, 2, 8].

We can see that the target differences are a shifted version of the original. 

But how?

It looks like applying operations on positions 2 and 3 transforms the differences.

Let's see. Original differences: [-5, 2, 8]

Apply operation on position 2. The new pair (d1, d2) becomes (2, 5). Because original d1=-5, d2=2. After operation on position 2, the new d1=2, d2=5.

Wait, no. Let's recalculate:

Original array after operation on position 2:

The new array is [7, 7+4 -2 =9, 4, 12]. The differences are:

9-7=2 (d1)

4-9 =-5 (d2)

12-4=8 (d3)

So the new differences are [2, -5, 8]. 

Then, applying an operation on position 3 (which affects d2 and d3). The original differences are [2, -5, 8]. Applying operation on position 3, the new differences become:

d2=8, d3=5.

So the new differences are [2, 8, 5]. 

Wait, but in the target array, the differences are [8, -5, 2]. So this approach doesn't directly get us there. 

But in the sample explanation, after syncing position 3 and then position 2, the differences become:

After syncing position 3:

Original array becomes [7, 2, 10, 12]. Differences are 2-7=-5, 10-2=8, 12-10=2. So differences are [-5, 8, 2].

Then syncing position 2:

Array becomes [7, 15, 10, 12]. Differences are 15-7=8, 10-15=-5, 2. So differences are [8, -5, 2], which matches the target.

So how did this happen?

The sequence of operations on position 3 and then 2 transformed the differences as follows:

Original differences: [-5, 2, 8]

After operation on 3: the pair (d2, d3) is transformed. Original d2=2, d3=8. After operation on 3, the new pair is (8, -2). So the differences become [-5, 8, -2].

Wait, no. Let's compute the array after each step:

Initial array: [7,2,4,12]

Operation on position 3 (i=3):

c3 becomes c2 + c4 -c3 = 2 + 12 -4 = 10. So the new array is [7,2,10,12]. 

Differences are:

2-7 = -5 (d1)

10-2=8 (d2)

12-10=2 (d3)

Then, operation on position 2 (i=2):

c2 becomes c1 + c3 -c2 =7 + 10 -2 =15. New array [7,15,10,12]. 

Differences are:

15-7=8 (d1)

10-15=-5 (d2)

12-10=2 (d3)

So the target differences are [8, -5, 2]. 

So the original differences were [-5, 2, 8]. After operation on 3, they became [-5, 8, 2]. Then after operation on 2, they became [8, -5, 2]. 

So each operation swaps the pair and negates the second element. For example, operation on 3 transforms the pair (d2, d3) from (2, 8) to (8, -2). But in this case, after operation on 3, d3 is 2 (since 12-10=2). So perhaps I'm missing something.

Wait, the operation on position 3 affects the pair (d2, d3) as follows. The original d2 is 2 (from 4-2), and d3 is 8 (from 12-4).

After operation on 3, the new array is [7, 2, 10, 12]. The new differences are d2=10-2=8, d3=12-10=2. So the pair (d2, d3) was (2,8), becomes (8, 2). Wait, but according to the earlier transformation rule, applying the operation on position i=3 should swap d2 and d3, and negate the new d3 (which was originally d2). But here, d2 and d3 are swapped and not negated. So the transformation here doesn't fit the earlier model. 

This suggests that my earlier analysis was incorrect. 

What's happening here?

When applying the operation on position i=3, the differences affected are d2 and d3. 

Original array after operation on i=3: 

The new array is [7, 2, 10, 12]. 

Differences:

d1 = 2-7 =-5

d2 =10-2=8

d3=12-10=2.

So the pair (d2, d3) changed from (2, 8) to (8, 2). 

According to the transformation rule, applying an operation on i=3 should swap d2 and d3 and negate d3. But here, d3 is 2, which is 8- (2+8) ?

Wait, the transformation rule for i=3 would swap d2 and d3 and negate the new d3. 

Original d2 = 2, d3 =8. After operation on i=3:

d2 becomes 8 (original d3), d3 becomes -2 (original d2). 

But in the example, after operation on i=3, d3 is 2, not -2. So there's a discrepancy here. 

What's wrong with the earlier analysis?

Ah! Wait, the operation on i=3 affects the differences d2 and d3. The operation replaces c3 with c2 + c4 - c3. The new c3 is 2 + 12 -4 =10. 

The new d2 is c3 - c2 = 10 - 2 = 8. The new d3 is c4 -c3 = 12 -10 = 2. 

So the new pair (d2, d3) is (8, 2). 

According to the earlier transformation rule, this should have been (d3, -d2) = (8, -2). But here, it's (8, 2), which is (d3, d2). 

So the earlier analysis must be incorrect. 

What's the correct transformation for the differences when applying an operation on position i?

Let's re-examine:

When applying an operation on position i, the new c_i is c_{i-1} + c_{i+1} - c_i.

The new differences are:

d_{i-1} = new_c_i - c_{i-1} = (c_{i-1} + c_{i+1} - c_i) - c_{i-1} = c_{i+1} - c_i = d_i (original).

d_i = c_{i+1} - new_c_i = c_{i+1} - (c_{i-1} + c_{i+1} - c_i) = -c_{i-1} + c_i = -(c_{i-1} - c_i) = -d_{i-1} (original).

So the pair (d_{i-1}, d_i) becomes (d_i, -d_{i-1}).

Ah! So for i=3, the operation affects the pair (d2, d3). The original pair is (d2=2, d3=8). After the operation, the pair becomes (8, -2). But in the example, the new pair is (8, 2). 

This suggests that the transformation rule is not followed, which is a contradiction. 

What's wrong here?

Ah! Oh no, I made a mistake in the example. Let's recompute the differences after the operation on i=3.

Original array: [7,2,4,12]. 

After operation on i=3: new array is [7,2,10,12]. 

So the differences are:

d1 = 2-7 = -5 (same as before).

d2 = 10-2 =8.

d3 =12-10=2.

So the pair (d2, d3) is (8, 2). 

But according to the transformation rule, after the operation on i=3, this pair should be (8, -2). 

But in this case, the new d3 is 2, which is positive. 

This suggests that the earlier analysis is incorrect. 

So where is the mistake?

Let's re-examine the transformation.

When you apply the operation on position i, the new differences are:

d_{i-1} (new) = new_c_i - c_{i-1} = (c_{i-1} + c_{i+1} - c_i) - c_{i-1} = c_{i+1} - c_i = d_i (original).

d_i (new) = c_{i+1} - new_c_i = c_{i+1} - (c_{i-1} + c_{i+1} - c_i) = c_i - c_{i-1} = d_{i-1} (original).

Wait, that's different from what I thought earlier. 

So the new pair (d_{i-1}, d_i) is (d_i, d_{i-1} ), which is a swap of the two differences without any negation.

This contradicts the earlier analysis.

So the correct transformation is that the operation on position i swaps the adjacent differences d_{i-1} and d_i. No negation is involved. 

But this contradicts the earlier example where the operation on position 3 swaps d2 and d3. 

But in the example, after the operation on position 3, the differences become (d2=8, d3=2). Which is the swapped pair of the original (d2=2, d3=8). So the transformation is a simple swap, with no negation. 

So why was my earlier analysis incorrect?

Let me re-examine the calculation. 

Original array: c_1, c_2, c_3, c_4.

Operation on i=3: new c_3 = c_2 + c_4 - c_3.

The new differences:

d_2 (new) = new c_3 - c_2 = (c_2 + c_4 - c_3) - c_2 = c_4 - c_3 = d_3 (original).

d_3 (new) = c_4 - new c_3 = c_4 - (c_2 + c_4 - c_3) = c_3 - c_2 = d_2 (original).

So the two differences are swapped. No negation occurs. 

So earlier analysis was wrong. The correct transformation is that applying the operation on position i swaps the adjacent differences d_{i-1} and d_i. 

This is a crucial correction. 

So this changes everything. Now, the operation on position i swaps the adjacent differences d_{i-1} and d_i. 

So the transformation is simply a swap of the two adjacent differences. 

This explains why in the example, applying the operation on position 3 swaps the differences d2 and d3. 

This is a key insight that was missing earlier. 

So the correct transformation is: applying an operation on position i swaps the adjacent differences d_{i-1} and d_i. 

This is a much simpler transformation to model. 

So now, the problem reduces to whether we can transform the original difference array into the target difference array by swapping any adjacent pair of differences. 

Because each operation on position i swaps d_{i-1} and d_i, which is equivalent to swapping the differences. 

So, the difference array can be transformed into any permutation of the original difference array. 

But wait, how?

For example, if we can perform any number of adjacent swaps, then the difference array can be transformed into any permutation of the original differences. 

Thus, the problem reduces to whether the target difference array is a permutation of the original difference array. 

But this is only possible if the first and last elements of the original and target arrays are the same, and the multiset of differences (excluding the first and last) are the same. 

But in the first sample input, the original differences are [-5, 2, 8], and the target differences are [8, -5, 2]. So the multiset is the same, and the order can be achieved by swapping pairs. 

The second sample input has differences [0,0] in the original and [1,1] in the target. These multisets are different, so it's impossible. 

So the solution is:

Check if the first and last elements of c and t are equal. Then, check if the multiset of differences (d_1, d_2, ..., d_{n-1}) is a permutation of the target differences (td_1, td_2, ..., td_{n-1}).

But wait, this can't be correct. Because the operation allows swapping any adjacent differences, but the first and last differences can be part of swaps. 

For example, in the first sample, the first difference is -5 and the last is 8. After swapping, the first difference becomes 8, which is the target. 

So, the first and last elements of the array are fixed, but the differences can be swapped, allowing the first and last differences to change. 

So the first and last elements being fixed is a necessary condition, and the multiset of differences (including all differences) must be the same between the original and target arrays. 

So the solution steps are:

1. Check if c[0] == t[0] and c[-1] == t[-1]. If not, return "No".

2. Compute the differences for the original array (d) and target array (td).

3. Check if the multiset of d is the same as the multiset of td. 

If all conditions are met, return "Yes", else "No".

But wait, this is only true if the order of differences can be rearranged via adjacent swaps, which is possible if and only if the multisets are the same. 

Yes. Because any permutation can be achieved via adjacent swaps. 

So, the correct approach is:

- Check if the first and last elements are equal.

- Check if the multiset of differences between consecutive elements (d_1, d_2, ..., d_{n-1}) is the same for the original and target arrays.

If both conditions are met, return "Yes", else "No".

But let's test this against the sample inputs.

Sample 1:

Original c: [7, 2,4,12]. Differences: [2-7= -5, 4-2=2, 12-4=8]

Target t: [7,15,10,12]. Differences: [15-7=8, 10-15=-5, 12-10=2]

The multiset of differences for c is {-5, 2, 8}, for t it's {8, -5, 2}. They are the same. So output is "Yes".

Sample 2:

Original c: [4,4,4]. Differences: [0, 0]

Target t: [1,2,3]. Differences: [1, 1]

Multisets are different. So output "No".

Another test case: n=2.

Original c: [5, 10]. Differences: [5].

Target t: [5, 10]. Differences: [5]. Multiset is same. Output "Yes".

Another test case where c and t have the same elements but in a different order. 

For example, original c: [1,3,5], t: [1,5,3].

Differences for c: [2,2]. For t: [4, -2]. Multisets are different. So output "No".

Wait, no. The differences for t are 5-1=4, 3-5=-2. So multiset is {4, -2}, which is different from {2, 2}. So output "No".

But according to the problem's transformation rules, can you swap the differences to achieve this?

No, because the multiset is different. So the answer is "No".

Thus, the solution is to check the first and last elements, and then whether the multiset of differences is the same.

This approach is O(n) time and space, which is feasible for n=1e5.

So the steps are:

1. Check if c[0] != t[0] or c[-1] != t[-1]. If so, output "No".

2. Compute the differences for c and t.

3. Check if the sorted list of differences is the same for both. If yes, output "Yes". Else, "No".

But wait, what about the order of differences? For example, if the differences are in a different order but the multiset is the same, then the answer is "Yes". Because the operations allow us to swap any adjacent differences, thus allowing us to permute the differences into any order. 

So the order of the differences does not matter. Only the multiset. 

Yes. Because any permutation can be achieved via adjacent swaps (like bubble sort steps). 

Thus, the algorithm is:

Check first and last elements. If they match, check if the sorted lists of differences are equal.

So, in code:

Read n.

Read c array.

Read t array.

if c[0] != t[0] or c[-1] != t[-1], print "No" and exit.

compute differences for c:

diffs_c = [c[i] - c[i-1] for i in range(1, len(c))]

diffs_t = [t[i] - t[i-1] for i in range(1, len(t))]

Sort both lists.

if sorted(diffs_c) == sorted(diffs_t), then output "Yes", else "No".

But wait, the sample input 1's differences for c are [-5, 2, 8], and for t are [8, -5, 2]. When sorted, both are [-5, 2, 8], so they are equal.

Sample 2: [0, 0] vs [1, 1], sorted lists are different.

Thus, this approach would work.

But why does this work? Because the differences can be rearranged into any order via swapping adjacent differences, which is allowed by the operations.

So the code would look like this.

This approach is O(n log n) time due to the sorting, which is acceptable for n up to 1e5.

But wait, the problem allows n up to 1e5. Sorting two lists of 1e5 elements each is manageable.

Thus, the code is:

Read n.

c = list(map(int, input().split())).

t = list(map(int, input().split())).

if c[0] != t[0] or c[-1] != t[-1]:

    print("No")

    exit()

if n == 1:

    print("Yes")

    exit()

diffs_c = [c[i] - c[i-1] for i in range(1, len(c))]

diffs_t = [t[i] - t[i-1] for i in range(1, len(t))]

if sorted(diffs_c) == sorted(diffs_t):

    print("Yes")

else:

    print("No")

Wait, but for n=1, but according to the constraints, n >=2. Because the first line of input is n (2<=n<=1e5). So the check for n==1 is redundant. But in code, the input may have n=2, which is allowed.

Thus, the code is:

Read n.

c = list(map(int, input().split())).

t = list(map(int, input().split())).

if c[0] != t[0] or c[-1] != t[-1]:

    print("No")

else:

    diffs_c = [c[i] - c[i-1] for i in range(1, len(c))]

    diffs_t = [t[i] - t[i-1] for i in range(1, len(t))]

    if sorted(diffs_c) == sorted(diffs_t):

        print("Yes")

    else:

        print("No")

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    c = list(map(int, input_stream.readline().rstrip("\n").split()))
    t = list(map(int, input_stream.readline().rstrip("\n").split()))

    if c[0] != t[0] or c[-1] != t[-1]:
        print("No", file=output_stream)
    else:
        def compute_diffs(arr):
            return [arr[i] - arr[i-1] for i in range(1, len(arr))]
        
        diffs_c = compute_diffs(c)
        diffs_t = compute_diffs(t)
        
        print("Yes" if sorted(diffs_c) == sorted(diffs_t) else "No", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
4 4 4
1 2 3
""",
            "output": \
"""\
No
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

c: [4,4,4]

t: [1,2,3]

c[0] =4 !=1 → output "No".

Another test case: n=2.

c: [5, 10]

t: [5, 10]

diffs_c = [5], diffs_t = [5]. sorted lists are equal → "Yes".

Another test case: n=2, c=[5,10], t=[5, 5]. Then t[1] !=c[1], so output "No".

This seems to cover all cases.

But wait, what about when the first and last elements are equal, but the differences are not permutations?

For example:

n=3.

c: [1,3,5]. differences: [2,2].

t: [1,5,5]. differences: [4,0].

sorted diffs_c: [2,2], sorted diffs_t: [0,4]. Not equal → output "No".

Which is correct.

Another test case where differences are a permutation:

n=5.

c: [a, b, c, d, e]. differences: [d1, d2, d3, d4].

t: [a, ... , e], differences: d3, d4, d1, d2 → sorted diffs_c and diffs_t are same → output "Yes".

Thus, the code is correct.
</think>

```python
n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

if c[0] != t[0] or c[-1] != t[-1]:
    print("No")
else:
    def compute_diffs(arr):
        return [arr[i] - arr[i-1] for i in range(1, len(arr))]
    
    diffs_c = compute_diffs(c)
    diffs_t = compute_diffs(t)
    
    print("Yes" if sorted(diffs_c) == sorted(diffs_t) else "No")
```
