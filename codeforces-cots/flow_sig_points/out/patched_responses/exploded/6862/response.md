<think>
Okay, I need to solve this problem where I have to find the minimum number of operations to make an array non-decreasing. Each operation allows me to select any number of indices and increment their values by 1 modulo m. The goal is to do this in as few steps as possible. Let's think through how to approach this.

First, let's understand the operations. Each operation can increment a set of elements, but when you do this, their value wraps around mod m. For example, if m is 7, then an element that's 6 becomes 0 when incremented. So, the challenge is to find the optimal way to apply these increments such that after all operations, the array is non-decreasing.

Hmm, the key here is that each operation can affect multiple elements at once. To minimize the number of operations, we want to group as many necessary increments as possible into a single step. But how do we model this?

Let's think about the required final array. Each element a_i must be <= a_{i+1} in the final array. Since each operation can add 1 to some elements (mod m), the problem is to determine for each element how many times it needs to be incremented (mod m) so that the array becomes non-decreasing. But since each increment can be applied to multiple elements in the same operation, we need to find a way to align these increments into the fewest possible steps.

Wait, but each operation can be applied to any subset of elements. So, for example, if I need to increment elements at positions i and j by 1 each, doing them in the same operation counts as one step instead of two. So the problem reduces to finding the required increments for each element and then grouping these increments such that whenever an increment is needed in a step, all higher steps can include that element's increments. Because once you've done an increment in a step, all subsequent steps can include that element again if needed. Wait, no. Because each increment is a step. Wait, each operation is a single step where you can choose any subset of elements to increment. So, each time you perform an operation, you can select some elements to add 1. The order of operations matters because each operation's increments are applied before the next.

So, for example, if an element needs to be incremented 3 times, that requires 3 operations. But if in each of those operations, you include that element, then after three steps, it's incremented three times. But maybe you can group the increments for different elements into the same steps as long as their required increments are ordered.

Wait, perhaps the minimal number of operations is equal to the maximum number of times any element needs to be incremented. Because, in each operation, you can include all elements that still need to be incremented. So, for example, if element A needs 2 increments and element B needs 3, then you can have three operations. In each of the first three steps, you include B. In the first two steps, you also include A. Then A gets 2 increments, B gets 3. The total steps would be 3. So the maximum required increments for any element gives the minimal number of steps. But wait, perhaps there's a way to have even fewer steps by aligning the required increments in a way that each operation can cover all necessary increments at that step. Hmm, perhaps this is the case. So the minimal number of operations is the maximum number of increments required for any element. But how to model this.

But the problem is that each element's required increments depend on the previous elements. So we need to model the required increments for each element in a way that after all operations, the array is non-decreasing.

So first, we need to determine for each element the minimal number of increments required, such that each a_i (after increments) is >= the previous a_{i-1} (after increments). But how do we model that.

Let's think of the problem in terms of the required increments for each element. Let's denote the number of increments for element i as x_i. Then, after all increments, the value is (a_i + x_i) mod m. But since we can choose any x_i (possibly 0), we need to find x_i such that for all i < j, (a_i + x_i) mod m <= (a_j + x_j) mod m. But since mod is cyclic, this complicates things. However, perhaps we can find a way to model this in a linear fashion.

Alternatively, maybe we can process the array from right to left. Because the rightmost element's x_n can be chosen such that it's as small as possible, then x_{n-1} must be chosen such that (a_{n-1} + x_{n-1}) mod m <= (a_n + x_n) mod m. But how to model this.

Another approach: since the array must be non-decreasing, perhaps each element (after increments) must be >= the previous. However, due to the modulo, this can wrap around. For example, if m is 7, a previous element could be 6, and the next could be 0, but that's allowed only if the next element has been incremented once (so becomes 1, which is larger than 6 mod 7). Wait, no. If the previous element is 6 and the next is 0, then after increments, if next is incremented once, it becomes 1. Then 6 <= 1 mod 7 is not true, since 1 is less than 6. Wait, but mod m, the ordering is not straightforward. So, we need to model the sequence such that each element is at least the previous one in the modified array. So (a_i + x_i) mod m >= (a_{i-1} + x_{i-1}) mod m is not sufficient. Because mod m, the values wrap around. So perhaps the problem is better modeled by considering the actual values without mod, but this is impossible since m can be large and the increments can be multiple times. Wait, but each x_i can be any non-negative integer. So (a_i + x_i) mod m can be any value. However, the actual x_i can be chosen as the minimal number of increments needed to reach the desired value. For example, if you want the final value to be 3 mod 7, then x_i can be (3 - a_i) mod 7. But this is only if you're allowed to choose x_i once. But since each x_i is the number of times the element is incremented, which is the same as the number of operations in which this element is selected. So the total increments for element i is x_i, and the final value is (a_i + x_i) mod m.

Wait, no. Because each time you select an element in an operation, it's incremented by 1. So x_i is the total number of times the element was chosen in any operation. So the final value is (a_i + x_i) mod m.

The problem is to choose x_1, x_2, ..., x_n such that:

For all i from 1 to n-1:

(a_i + x_i) mod m <= (a_{i+1} + x_{i+1}) mod m

And the sum of x_1, x_2, ..., x_n is minimized? No, wait. The number of operations is not the sum of x_i. Because in each operation, you can select any subset of elements and increment them. So x_i is the number of times the element was included in any operation. Therefore, the number of operations is equal to the maximum x_i across all elements. Because each operation can increment any subset. So, for example, if in the first operation, you select elements that need 3 increments, then in three steps, those elements are incremented each time, leading to x_i = 3. So the total number of operations is the maximum x_i. Therefore, the problem reduces to finding x_i for each element such that the array is non-decreasing, and the maximum x_i is minimized.

So the problem is to find x_i such that for all i < j, (a_i + x_i) mod m <= (a_j + x_j) mod m, and the maximum x_i is minimized.

So the key is to model the x_i's such that each x_i is as small as possible, and the maximum of them is minimized.

But how to model the constraints (a_i + x_i) mod m <= (a_j + x_j) mod m. This is tricky because of the modulo.

Let's think in terms of possible values for each x_i. For each element, x_i can be any non-negative integer. But the constraints between consecutive elements must be satisfied. Let's process the array from right to left. Because the rightmost element can be set in a certain way, and then each previous element can be adjusted based on the next.

For example, starting with the last element. x_n can be 0, since there's no element after it. Then, for the element before, x_{n-1} must be chosen such that (a_{n-1} + x_{n-1}) mod m <= (a_n + x_n) mod m. Wait, but perhaps there's a minimal x_{n-1} that allows this. Then, for the previous elements, each must be chosen based on the next element's x.

But how do we model this when there's a wrap-around. Let's think about the possible values of (a_i + x_i) mod m. Let's call this value v_i. So the problem becomes selecting v_i for each i such that v_1 <= v_2 <= ... <= v_n, and for each i, v_i ≡ (a_i + x_i) mod m. Then, the x_i is the minimal number of steps needed to reach v_i from a_i, which is (v_i - a_i) mod m. But since x_i is the number of times the element is incremented (each increment adds 1), x_i is exactly (v_i - a_i) mod m. Because adding 1 x_i times will take a_i to a_i + x_i mod m.

Wait, but (a_i + x_i) mod m is equivalent to (a_i mod m + x_i mod m) mod m. But since a_i is already between 0 and m-1, it's just (a_i + x_i) mod m. So x_i can be any non-negative integer such that (a_i + x_i) mod m = v_i. The minimal x_i is (v_i - a_i) mod m. Wait, no. Because if a_i is 2, m is 5, and v_i is 4, then x_i can be 2 (2 + 2 =4). But if v_i is 1, then x_i can be (1 -2 +5) mod5 =4, so x_i is4. Because adding 4 times: 2+4=6 mod5 is 1.

So x_i is (v_i - a_i) mod m. But x_i can be any non-negative integer that satisfies (a_i + x_i) mod m = v_i. The minimal x_i is indeed (v_i - a_i) mod m, because x_i can be (v_i -a_i) mod m. Because if (v_i -a_i) is negative, adding m gives the minimal x_i. For example, a_i=3, v_i=1, m=5. Then (1-3) mod5 is ( -2 ) mod5 =3. So x_i=3, which gives 3+3=6 mod5=1.

So, given that, the problem is to choose a sequence of v_i's that form a non-decreasing sequence, and for each i, x_i = (v_i - a_i) mod m. Then, the number of operations is the maximum x_i across all elements.

So, our goal is to find a non-decreasing sequence v_1 <= v_2 <= ... <= v_n (each between 0 and m-1) such that for each i, x_i = (v_i - a_i) mod m, and the maximum x_i is as small as possible.

So the problem reduces to selecting the v_i's such that the sequence is non-decreasing, and the maximum of (v_i - a_i) mod m across all i is minimized.

But how to compute this sequence of v_i's.

Let's process the array from right to left. For the last element, the best possible v_n is a_n + x_n mod m. Since there's no constraint after it, we can choose x_n to be 0, so v_n = a_n. That's optimal, because any x_n >0 would increase the maximum.

Then, for element i (starting from n-1 down to 1), we need to choose v_i such that v_i <= v_{i+1}, and x_i = (v_i - a_i) mod m is as small as possible. Also, we need the x_i's to be such that when considering all elements up to i, the maximum x_i is minimized.

Wait, but how do we choose v_i given v_{i+1}? Let's think of the possible choices for v_i. It has to be <= v_{i+1}. But also, we want (v_i - a_i) mod m to be as small as possible. But how does that translate into the choice of v_i.

Wait, the minimal x_i is (v_i - a_i) mod m. So for each possible v_i <= v_{i+1}, we can compute the x_i and choose the v_i that gives the minimal x_i. But since we are processing right to left, each step depends on the next element's v.

But maybe there's a way to model this. Let's think: for the current element i, given the next element's v_{i+1}, what is the best possible v_i?

We want to maximize v_i (since a higher v_i would allow for smaller x_i) but not exceeding v_{i+1}.

Wait, because the higher v_i is (without exceeding v_{i+1}), the smaller x_i could be. For example, suppose a_i is 3, m is 5. If v_i can be up to 4 (the maximum possible), then x_i is (4 -3) mod5 =1. But if v_{i+1} is 2, then v_i can't be higher than 2, so x_i would be (2-3) mod5 = ( -1 ) mod5 =4, which is worse. So the optimal is to choose v_i as large as possible (up to v_{i+1}) but such that (v_i -a_i) mod m is minimized.

So for each i, the optimal v_i is the maximum possible value <= v_{i+1} such that (v_i -a_i) mod m is as small as possible. Because the maximum possible v_i <=v_{i+1} would give the minimal x_i, since x_i = (v_i -a_i) mod m. For example, if a_i is 3, m is5, and v_{i+1} is4, then the best v_i is4, x_i=1. But if v_{i+1} is3, then v_i can be3, x_i=0.

So, for each i, given the next element's v_{i+1}, the optimal choice for v_i is the maximum possible <=v_{i+1} such that (v_i - a_i) mod m is minimal. That would be the largest possible v_i <=v_{i+1}, which would give the minimal x_i.

Wait, but wait. The x_i is (v_i -a_i) mod m. For example, if a_i is 3, m is5, and possible v_i ranges up to v_{i+1}=4. Then the best choice is v_i=4, x_i=1. But if v_i=3, x_i=0. So why isn't 3 better?

Ah, right! So the x_i is (v_i -a_i) mod m, which is the same as (v_i -a_i) if v_i >=a_i, otherwise (v_i -a_i +m). So to minimize x_i, for a given v_i, we want v_i to be >=a_i as much as possible. Because then x_i is (v_i -a_i), which is smaller than (v_i -a_i +m) if v_i <a_i. So, the minimal x_i for a particular v_i is achieved when v_i is as large as possible (<=v_{i+1}) and >=a_i. If that's possible, then x_i is (v_i -a_i). Otherwise, if even the maximum possible v_i (v_{i+1}) is less than a_i, then x_i is (v_i -a_i +m) = (v_{i+1} -a_i +m). But that would be larger than if we can have v_i >=a_i.

So, the optimal choice for v_i is min(v_{i+1}, the largest possible value >=a_i and <=v_{i+1}).

Wait, but how to model this. Let's see:

If a_i <= v_{i+1}, then the best possible v_i is min(v_{i+1}, a_i + m -1), but within the limit of v_{i+1}. Wait, no. Because the maximum possible v_i is v_{i+1}, but within that, the best is to choose the largest possible v_i >=a_i, so that x_i is (v_i -a_i). If v_{i+1} >=a_i, then v_i can be v_{i+1} (if possible). Wait, no. Because if v_{i+1} >= a_i, then the best v_i is the maximum possible (v_{i+1}), which gives x_i =v_{i+1} -a_i. But if v_{i+1} is less than a_i, then we can't have v_i >=a_i, so x_i is (v_i -a_i +m). But in this case, we want to choose v_i as large as possible (v_{i+1}), which gives x_i = (v_{i+1} -a_i +m) mod m. Since m is added, but mod m, it's equivalent to (v_{i+1} -a_i) mod m.

Wait, but for example, a_i=3, m=5, v_{i+1}=2. Then the maximum possible v_i is2, which is less than a_i. So x_i is (2-3) mod5 =4. Which is (2-3 +5) mod5=4. So x_i is4.

But perhaps if there's a way to wrap around. For example, maybe v_i can be 2 (as per v_{i+1}=2), but if the next element is 2, perhaps that allows the current element to be higher (but not in this case, since it's constrained by the next element's v). So the processing from right to left makes sense, as each element's v_i is constrained by the next element's v_{i+1}.

So, the approach is:

1. Start from the right, set v_n = a_n. x_n=0.

2. For i from n-1 downto 1:

   a. The maximum possible v_i is v_{i+1}.

   b. We want to choose the best v_i (<=v_{i+1}) such that x_i is minimal.

   c. So, if possible, choose v_i as the maximum between a_i and ... wait, no. Because if a_i is <= v_{i+1}, then the best is to choose v_i as v_{i+1}, because that's the largest possible, leading to x_i =v_{i+1} -a_i. If a_i is larger than v_{i+1}, then the best v_i is v_{i+1}, which gives x_i = (v_{i+1} -a_i +m) mod m.

Wait, but that's not correct. For example, if a_i is 3, m is5, and v_{i+1} is4. Then v_i can be4, x_i is1. Which is better than any other choice. If v_{i+1} is3, then v_i can be3, x_i is0. If a_i is3 and v_{i+1} is2, then v_i must be2, x_i is4.

So, in general, for each i:

v_i can be up to v_{i+1}, and we want to choose v_i to be as large as possible (which is v_{i+1}), but if a_i is larger than v_{i+1}, then we have to wrap around.

Wait, but how does this affect the x_i. Let's model this:

For i-th element, given v_{i+1}, the maximum possible v_i is v_{i+1}.

So, the best v_i is min(v_{i+1}, the maximum possible value >=a_i). But if a_i <=v_{i+1}, then the maximum possible v_i is v_{i+1}, leading to x_i =v_{i+1} -a_i.

If a_i >v_{i+1}, then the maximum possible v_i is v_{i+1}, but then x_i =v_{i+1} -a_i +m. Because (v_{i+1} -a_i) is negative, adding m gives the correct x_i.

So the formula for x_i is (v_i -a_i) mod m, where v_i is <=v_{i+1}.

But since v_i is set to v_{i+1} (if possible), the x_i is (v_{i+1} -a_i) mod m.

Wait, no. Because when a_i is larger than v_{i+1}, then the x_i is (v_{i+1} -a_i) mod m. But that's negative, so mod m gives (v_{i+1} -a_i +m) mod m. Which is v_{i+1} -a_i +m.

So, in this case, x_i is (v_{i+1} -a_i +m) mod m, which is the same as (v_i -a_i +m) mod m.

So, putting this together:

For each element i from right to left:

If a_i <=v_{i+1}:

   then set v_i =v_{i+1}, x_i =v_{i+1} -a_i.

Else:

   set v_i =v_{i+1}, x_i = (v_{i+1} -a_i +m) mod m.

Wait, but in this case, the sequence of v_i's would be non-decreasing because each v_i is set to v_{i+1} (if possible). Wait, no. For example, suppose i is 3, v_{i+1} is 4, a_i is 3. Then v_i becomes4, which is larger than a_i. Then x_i is1. But then the next element (i=2) would have v_i set to4, which is >= a_i if possible.

Wait, this approach would lead to all v_i's being equal to v_{n} (the last element). But that's not correct. Because in some cases, a_i may be higher than v_{i+1}, but wrapping around could allow for a lower x_i. Wait, but how?

Wait, perhaps there's a scenario where a_i is higher than v_{i+1}, but choosing a v_i that is lower than v_{i+1} but higher than a_i (mod m) could lead to a smaller x_i. For example, suppose m=5, a_i=3, v_{i+1}=2. Then, if we set v_i=2, x_i is (2-3 +5) mod5=4. But if we could set v_i to 4 (but that's larger than v_{i+1}=2, which is not allowed). So no, that's not possible. So the maximum v_i is v_{i+1}, so in this case, the x_i is 4.

Alternatively, if v_{i+1} is 4, and a_i is 3, then setting v_i to4 (max possible) gives x_i=1.

So in this approach, for each i, we set v_i to v_{i+1}, and compute x_i as (v_{i+1} -a_i) mod m. But this would create a non-decreasing sequence since each v_i is <=v_{i+1} (but wait, no. Because v_i is set to v_{i+1}, so the sequence is all equal? No. Because when a_i is larger than v_{i+1}, then v_i is set to v_{i+1}, which is less than a_i. Wait, no. Let me see.

Wait, if a_i is larger than v_{i+1}, then v_i is set to v_{i+1}, but since a_i is larger than that, then (v_i -a_i) is negative, so x_i is (v_i -a_i +m) mod m. So for example, if v_{i+1} is 2 and a_i is3, then x_i is (2-3 +5) mod5=4.

But in this case, the sequence of v_i's would be non-decreasing, because each v_i is set to the minimum possible value (since we are processing from right to left). Wait, no. Because in this approach, each v_i is set to v_{i+1} if possible, which would make v_i = v_{i+1}. But if a_i is <=v_{i+1}, then v_i is set to v_{i+1}, leading to a non-decreasing sequence. However, if a_i is greater than v_{i+1}, then v_i is set to v_{i+1}, which is less than a_i. But in that case, (a_i +x_i) mod m would be v_{i+1}, which is less than a_i. But how is that possible?

Wait, this approach would create a sequence where each v_i is <=v_{i+1}. Because we set v_i to the minimum possible between v_{i+1} and something. Wait, no. Because for each i, v_i is set to v_{i+1}. So the sequence is all equal. For example, if the last element is a_n, then v_{n-1} is set to a_n, and so on. So the entire array's v_i's would be equal to a_n, except when a_i is greater than v_{i+1}, which would require wrapping around. But this doesn't seem right.

Wait, let's take the second example from the input:

Input:

5 7

0 6 1 3 2

The correct output is1.

According to the sample, after one operation, the array becomes [0,0,1,3,3]. So the final array is [0,0,1,3,3], which is non-decreasing.

So the x_i's for the sample are:

Original array:0,6,1,3,2.

After x_i increments:

0+0=0 mod7=0.

6+1=7 mod7=0.

1+0=1.

3+0=3.

2+1=3.

So x_2 is1 (selected once), x_5 is1. So x's are [0,1,0,0,1]. The maximum is1, which is the answer.

But according to our approach:

We process from right to left.

v_5 =2.

i=4: a_4=3. a_4 <=v_5 (3 <=2) is false. So v_i is set to v_5=2. x_i = (2-3 +7) mod7=6 mod7=6. But this would lead to x_4=6, which is way larger than the actual solution.

But in the sample solution, x_4 is0. So our approach would not work here. So there's a flaw in the approach.

Ah, this suggests that the approach of setting v_i =v_{i+1} for all i is not correct. So we need to rethink the problem.

Hmm, perhaps the error in the previous approach is that it doesn't account for the possibility that v_i can be higher than a_i, even if that requires wrapping around. For example, in the sample, the first element is 0, which is allowed to be 0. The second element is6. But after incrementing it once, it becomes0. So the final array becomes [0,0,1,3,3]. So the v_i's are 0,0,1,3,3. Which is non-decreasing.

But according to the approach of processing from right to left, starting with v_5=2.

i=4 (third element in 0-based?), wait original indices are 1-based. Let's index from 1 to5.

Processing i=4 (element 3) and i=5 (element2).

Wait, perhaps the right approach is to find a sequence of v_i's such that each v_i can be in the range [prev_v, prev_v + m -1] modulo m, but how?

Alternatively, maybe the problem requires that the sequence v_i's can be non-decreasing, but considering the modulo m circular nature. So, for example, if v_{i} is 6 and v_{i+1} is 0 (mod7), then this would require that v_i <=v_{i+1} only if 6 <=0, which is not the case. So in such a case, the sequence is not allowed.

But according to the problem statement, the array must be non-decreasing after the operations. So the sequence of v_i's must be non-decreasing in the usual integer sense (not considering mod m). Because (v_i + x_i) mod m must form a non-decreasing sequence. Wait, but mod m is applied to each element. How can the array be non-decreasing?

For example, consider two elements: 6 and 0, m=7. To make them non-decreasing, the first element can be 6 mod7=6, the second can be0 mod7=0. That's [6,0], which is not non-decreasing. So this is not allowed. But if we increment the second element once, it becomes1. Then the array is [6,1], which is still not non-decreasing. So we need to increment the first element once: it becomes0 mod7, and the second becomes1. The array [0,1], which is non-decreasing.

Alternatively, increment the second element six times: it becomes6. Then the array is [6,6], which is non-decreasing.

So the key is that the sequence of (a_i +x_i) mod m must be non-decreasing in the standard integer sense. So even though the values are mod m, the sequence must be non-decreasing as integers. So for example, 6 mod7 is6, and 0 mod7 is0, but 6>0, so this is not allowed. So the modulo doesn't affect the ordering; the values are treated as integers in [0, m-1], and must form a non-decreasing sequence.

So the problem is to choose x_i's such that the sequence (a_1 +x_1) mod m, (a_2 +x_2) mod m, ..., (a_n +x_n) mod m is non-decreasing, and the maximum x_i is minimized.

Thus, the problem is to find a non-decreasing sequence of integers v_1, v_2, ..., v_n where 0 <= v_i < m, such that v_i >= v_{i-1} for all i, and x_i = (v_i -a_i) mod m. The goal is to choose the sequence with the minimal maximum x_i.

So, this is the crux of the problem.

Now, how to model this.

Let's think again of processing from right to left. The idea is to assign to each element the minimal possible x_i, given the x_{i+1} (or v_{i+1}).

Let's formalize this. For each i from n-1 down to 1:

We need to choose v_i <=v_{i+1}.

But we want to choose v_i as large as possible (<=v_{i+1}) to minimize x_i. Because x_i is (v_i -a_i) mod m. To minimize x_i, we want v_i to be as large as possible (mod m) that is <=v_{i+1} and >= a_i. If possible, this would give x_i =v_i -a_i, which is the smallest possible. If that's not possible (i.e., a_i >v_{i+1}), then we have to wrap around. For example, a_i is3, m=5, and v_{i+1} is2. Then, the best v_i is2, which gives x_i= (2-3 +5) mod5=4.

But wait, perhaps there's another option. Like, what if we choose v_i to be something larger than v_{i+1} but mod m it's smaller. For example, if v_{i+1} is 2, then possible v_i could be 3 (mod5), but that's larger than 2, which would not be allowed. Because the sequence must be non-decreasing in integer terms, not modulo terms.

So, the constraints are strict: each v_i must be <=v_{i+1} as integers.

So, the modulo does not affect the ordering. So for the sequence to be non-decreasing, each v_i must be <=v_{i+1} as integers.

Thus, processing from right to left makes sense. For each i, v_i can be up to v_{i+1}. The best possible v_i is the largest possible value that allows x_i to be as small as possible.

So, for each i, given v_{i+1}, the optimal v_i is the maximum possible value <=v_{i+1} such that x_i is minimized.

Let's model this. To minimize x_i, we need to maximize v_i (since x_i = (v_i -a_i) mod m). The maximum possible v_i is v_{i+1}, so we can set v_i to v_{i+1} if possible, and compute x_i.

But wait, when a_i is larger than v_{i+1}, then setting v_i to v_{i+1} (the maximum allowed) would give x_i = (v_{i+1} -a_i) mod m. Which could be a large value. But perhaps there's a way to choose v_i in a way that allows a smaller x_i. How?

For example, suppose m=7, a_i=6, v_{i+1}=0. Then, v_i can be 0. x_i is (0-6) mod7=1. Which is better than choosing any other value. Because 0 is the maximum allowed, so x_i=1.

Alternatively, if v_{i+1} is5, and a_i is6. Then, v_i must be <=5. So x_i is (5-6) mod7=6. Which is worse than if v_{i+1} is higher.

So, in such cases, when a_i is larger than v_{i+1}, the x_i is (v_{i+1} -a_i) mod m. Which could be (v_{i+1} -a_i +m) mod m. Since (v_{i+1} -a_i) is negative.

So, the only option is to set v_i to v_{i+1}, but x_i would be (v_{i+1} -a_i +m) mod m.

But how to compute this.

So, the approach would be:

Start with v_n =a_n. x_n=0.

For i from n-1 downto 1:

   v_i can be up to v_{i+1}.

   We want to choose v_i as large as possible (<=v_{i+1}) to minimize x_i.

   If possible, choose v_i as the maximum between a_i and ... wait, no. Because the maximum possible is v_{i+1}.

Wait, perhaps the optimal v_i is min(v_{i+1}, the smallest possible that allows x_i to be minimal). Or, maybe, the optimal v_i is the largest possible (<=v_{i+1}) such that v_i >=a_i. If such a v_i exists (i.e., if a_i <=v_{i+1}), then x_i is v_i -a_i. Otherwise, if a_i >v_{i+1}, then x_i is (v_i -a_i +m) mod m.

So:

For each i:

   if a_i <=v_{i+1}:

      v_i =v_{i+1}  --> this is the largest possible v_i <=v_{i+1}, which would give x_i =v_i -a_i =v_{i+1} -a_i.

   else:

      v_i =v_{i+1} --> which is less than a_i. x_i = (v_{i+1} -a_i +m) mod m.

But this approach may not work, as the sample shows.

Let's apply this approach to the sample input:

Sample Input 2:

5 7

0 6 1 3 2

Processing from right to left:

v_5 =2, x_5=0.

i=4 (element 3):

a_i=3. v_{i+1} =2. a_i=3 >v_{i+1}=2.

So v_i=2. x_i= (2-3+7) mod7 =6 mod7=6.

But in the sample, x_4 is0. So this approach gives x_i=6, which is incorrect.

So clearly, this approach is wrong.

Hmm, what's wrong here.

In the sample, the optimal x_i's are [0,1,0,0,1]. So for the third element (a_i=1), x_i=0. For the fourth element (a_i=3), x_i=0. So according to this, the v_i's would be:

v_5=2.

i=4: a_i=3. But according to the sample, v_i is3 (since a_i +x_i=3+0=3 mod7=3). But according to the approach above, v_i would have to be <=v_{i+1}=2. Which would require that v_i is2, but that's not the case in the sample.

So, the approach of processing from right to left and setting v_i to v_{i+1} when a_i>v_{i+1} is not correct. So there's a flaw in the initial approach.

So what's the correct way to model this?

Perhaps the correct approach is to allow v_i to be larger than v_{i+1} but wrap around. But no, because the sequence must be non-decreasing in the integer values. So if v_i is 3 and v_{i+1} is2, then the sequence is not non-decreasing, which is invalid.

So the problem must be to find v_i's that are non-decreasing in integer order.

So the sample has v_4=3 and v_5=3. Which is allowed. But according to the approach of processing from right to left, how can v_4 be3 if the initial v_5 is2?

Ah, because after processing i=5, the initial v_5 is2. Then, when processing i=4 (element3), the next element's v is2. So the current v_i must be <=2. But in the sample solution, element3's v_i is3, which is larger than 2. So how is that possible?

This suggests that the initial approach is incorrect. So there must be another way to model the v_i's.

Ah, perhaps the problem is that the initial approach sets v_i to v_{i+1} when possible, but that's not the correct way to model the v_i's. Instead, perhaps we can allow v_i to be up to m-1, but then v_{i+1} must be >=v_i.

Wait, but the processing is from right to left. So for i=4 (element3), v_{i+1} is the v of the next element. So for the sample, after processing i=5 (element5), v_5=2. Then, when processing i=4 (element4), which is3, we need to choose v_4 <=v_5=2. But in the sample, the v_4 is3, which is larger than 2. So that can't be right. So there's a contradiction here.

Wait, no. The sample's final array is [0,0,1,3,3]. So the v_i's are:

v_1=0, v_2=0, v_3=1, v_4=3, v_5=3. Which is non-decreasing.

But according to the initial approach of processing from right to left, the first step is to set v_5=2. So this is not possible. So how is this possible?

Ah, this indicates that the initial approach of setting v_n=a_n is incorrect. Because in the sample, a_5 is2, but the optimal solution requires v_5=3 (after incrementing once). So, the initial approach of setting v_n=a_n is wrong.

Ah! Here's the mistake. The initial approach assumes that the optimal solution for the last element is to set x_n=0. But this is not necessarily the case. Because by allowing x_n to be non-zero, the last element could be higher, which may allow the previous elements to have lower x_i's. So the previous approach is incorrect because it assumes that the last element's x is zero, but in reality, the last element can be incremented to allow the previous elements to have smaller x_i's.

So this is a key insight. The optimal solution might require incrementing the last element to allow the previous elements to have smaller x_i's, which could lead to a lower maximum x_i.

So, the correct approach must consider that the last element can be incremented multiple times (x_n can be positive) to allow the previous elements to have smaller x_i's.

But how to model this, given that the problem allows x_i to be any non-negative integer (including wrapping around).

So the problem is now much more complex. We need to find a non-decreasing sequence v_1 <=v_2 <= ... <=v_n (each between 0 and m-1) such that the maximum x_i (x_i = (v_i -a_i) mod m) is minimized.

So, the minimal maximum x_i is the minimal possible over all possible non-decreasing sequences of v_i's.

This seems challenging, but perhaps there's a way to model this with dynamic programming.

An alternative approach is to realize that for each element i, the possible x_i can be determined by the next element's v_{i+1}, but since v_{i+1} can be any value >=v_i, it's not possible to process from left to right or right to left in a straightforward manner.

But considering the problem's constraints (n and m up to 3e5), we need an O(n) or O(n log m) solution.

Another idea is that for each element, the possible v_i can be in a range that depends on the next element's v_{i+1}. But how to represent this range efficiently.

Perhaps, for each element i, the optimal v_i is the maximum possible such that v_i <=v_{i+1} and x_i is minimized.

But since v_{i+1} is a variable, we need to find for each i the best possible v_i and v_{i+1} combination that minimizes the maximum x_i.

This seems like a dynamic programming problem where, for each i, we track the possible ranges of v_i and the maximum x_i up to that point.

But given the size of n and m, this would be infeasible.

Another idea is to model the possible v_i as a range and track the minimal maximum x_i for each possible v_i.

But how.

Let's think of the problem as follows. For each element i, we can have a set of possible values for v_i, which must be >=v_{i-1} (assuming processing from left to right). For each possible v_i, we track the minimal maximum x_i up to that point.

But even this approach would be O(nm), which is not feasible for n up to 3e5.

Thus, we need a different approach.

Alternative approach inspired by the sample:

In the sample, the optimal solution involved increasing the second element once and the fifth element once. This resulted in x_2=1, x_5=1, and the other x's zero. The maximum is1.

But according to the initial approach, processing from right to left and setting v_5=2 (a_5=2), then for i=4 (a_4=3) which is >2, so x_4= (2-3+7)=6. Then for i=3 (a_3=1), since 1 <=2, x_3=2-1=1. For i=2 (a_2=6>2), x_2= (2-6+7)=3. For i=1 (0<=2, x_1=2-0=2). The maximum x is6, which is way larger than the correct answer. So the initial approach is incorrect.

The correct approach must allow the last element to be increased. For example, in the sample, the last element is 2. By incrementing it once, it becomes3 mod7=3. Then, the fourth element can be3, which requires x_4=0. Which gives a better maximum x_i.

So the initial approach of fixing v_n =a_n is incorrect.

So, the problem requires that we consider all possible v_n and choose the one that allows the minimal maximum x_i.

But with m up to 3e5, this would be O(mn), which is impossible.

Thus, we need a way to find the optimal v_n and compute the minimal maximum x_i based on that.

Alternatively, perhaps the optimal solution requires that the sequence of v_i's forms a non-decreasing sequence where each v_i can be written as (a_i + x_i) mod m, and the x_i's are chosen such that the maximum x_i is minimized.

But how.

Another idea: the minimal possible maximum x_i is the minimal t such that there exists a sequence of x_i's (each x_i <=t) such that (a_i +x_i) mod m is non-decreasing.

But finding the minimal t is challenging. We can model this as a binary search problem. We can binary search on the possible t values (from0 to m-1) and check if there exists a valid sequence of x_i's <=t that forms a non-decreasing sequence.

But how to check for a given t whether such a sequence exists.

For a given t, each x_i can be in 0<=x_i <=t. For each element i, the possible values of (a_i +x_i) mod m are [a_i, a_i +t] mod m, which is a contiguous interval of length t+1. But since it's mod m, this could wrap around.

So for each element i, the possible (a_i +x_i) mod m is a set of values. We need to choose a value v_i from this set for each i, such that the sequence is non-decreasing.

This sounds similar to a problem where each element has a range of possible values, and we need to choose a non-decreasing sequence within those ranges.

This is a known problem. The approach is to greedily assign the smallest possible value for each element that is >= previous and within its range.

But in our case, the ranges are determined by t. For each i, the possible v_i is the set of (a_i +x_i) mod m, where x_i <=t. This is equivalent to v_i being in [a_i, a_i +t] mod m. Which could be a range of up to t+1 values.

But how to model this.

Alternatively, for each element, the possible v_i can be any value in the interval [a_i mod m, (a_i +t) mod m], considering the wrap-around.

For example, if a_i is 5, m=7, t=3, then x_i can be0-3. So possible v_i are5,6,0,1 (mod7).

So the possible v_i's are a contiguous interval modulo m. However, this depends on whether a_i +t exceeds m-1.

So, for each element i, the possible v_i can be in the interval [a_i, a_i +t] mod m, which can be either a contiguous interval or two intervals (if the interval wraps around).

But for the purpose of finding a non-decreasing sequence, the interval can be treated as a range. For example, if a_i +t >=m, then the possible v_i's are [a_i, m-1] and [0, (a_i +t) mod m].

But this complicates the problem.

However, there's a way to model this by considering the possible lower and upper bounds for each element's v_i.

For a given t, the possible values of v_i for element i are:

low =a_i

high = (a_i +t) mod m

If low <= high: then the possible v_i's are [low, high]

Else: possible v_i's are [low, m-1] and [0, high]

But we need to choose v_i's such that the sequence is non-decreasing.

So, the problem reduces to checking whether there exists a non-decreasing sequence v_1 <=v_2 <=... <=v_n where each v_i is in the interval for element i.

This can be done greedily as follows:

We can process each element from left to right. For each element i, we set v_i to the smallest possible value >=v_{i-1} that is in the interval for element i. If no such value exists, then it's impossible for this t.

But how to compute this efficiently.

For example, when processing element i, the previous v_{i-1} is known. We need to find the minimal v_i >=v_{i-1} that is in the interval for i.

If the interval for i is [low_i, high_i], and low_i <= high_i:

   if v_{i-1} <= high_i:

      v_i = max(low_i, v_{i-1})

   else:

      no solution.

If the interval is split into [low_i, m-1] and [0, high_i], then we have to check if there's a value >=v_{i-1} in either of these ranges.

If v_{i-1} <=m-1 and is in [low_i, m-1], then v_i = max(low_i, v_{i-1})

Else, check if there's a value in [0, high_i] that is >=v_{i-1}. Since [0, high_i] is possible only if high_i >=0 and the interval wraps around. But in this case, high_i is (a_i +t) mod m. Which could be less than low_i.

So, this becomes complicated.

But for a given t, this check can be done in O(n) time. Since for each element, the intervals can be determined and processed in O(1) time.

Therefore, the plan is:

Binary search on t (the maximum x_i). For each t, check if there exists a non-decreasing sequence v_1 <=v_2 <= ... <=v_n such that each v_i is in the possible interval for element i and t.

The minimal such t is the answer.

This approach would have a time complexity of O(n log m), which is acceptable for n up to 3e5 and m up to 3e5.

So, the steps are:

1. Binary search t between 0 and m-1.

2. For each t, check if a valid sequence exists.

3. Find the smallest t for which the check passes.

Now, the challenge is to implement the check efficiently.

Implementing the check for a given t:

For each element i, compute the interval [low_i, high_i] = [a_i, (a_i +t) mod m].

If low_i <= high_i:

   the interval is [low_i, high_i].

Else:

   the interval is [0, high_i] and [low_i, m-1].

We need to find a non-decreasing sequence v_i's where each v_i is in their interval, and each v_i >=v_{i-1}.

The greedy approach is to keep track of the previous v and for each i, choose the smallest possible v_i >= prev_v that is in the current interval.

If this is not possible, then t is invalid.

Let's see how to handle each case:

Case 1: low_i <= high_i (the interval is continuous).

If prev_v <= high_i:

   choose v_i = max(prev_v, low_i).

Else:

   no solution.

Case 2: low_i > high_i (interval is split into two parts: [low_i, m-1] and [0, high_i]).

We need to choose v_i >= prev_v and in either of the two ranges.

But how to find the minimal possible v_i.

If prev_v is <= high_i:

   possible to choose v_i in [prev_v, high_i].

   v_i is max(prev_v, 0) up to high_i.

Else if prev_v >= low_i:

   possible to choose v_i in [prev_v, m-1].

   v_i is prev_v.

Else:

   prev_v is in (high_i, low_i). So, can't choose from the lower part. So, check if there's a value >= prev_v in the upper part.

   If prev_v <= m-1 and low_i <= m-1, then the upper range is [low_i, m-1]. So if low_i <= m-1 and prev_v <= m-1, then v_i can be max(prev_v, low_i).

   If that's possible, proceed. Otherwise, no.

But this is getting complicated. Let's formalize this.

For case 2 (low_i > high_i):

We have two possible ranges: [low_i, m-1] and [0, high_i].

We need to choose v_i >= prev_v and in either of these ranges.

Possible scenarios:

A. prev_v <= high_i:

   The best choice is to take v_i = max(prev_v, 0). But since the lower range is [0, high_i], the max(prev_v, 0) is prev_v. So v_i can be prev_v, if it's <= high_i. This is possible, so v_i = prev_v.

B. prev_v >= low_i:

   Then v_i can be prev_v, which is in the upper range.

C. prev_v is between high_i +1 and low_i -1:

   In this case, there's no possible v_i in the lower range. So we must choose from the upper range. So we need to find the smallest v_i in the upper range >= prev_v.

   The upper range is [low_i, m-1]. So if prev_v <= m-1 and low_i <= m-1:

      if low_i <= prev_v <= m-1: then v_i = prev_v.

      else: v_i = low_i.

   But if prev_v > m-1, this is impossible. But prev_v is <= m-1 by definition (since it's a value in [0, m-1]).

So in case C:

   if low_i <= m-1 and prev_v <= m-1:

      if low_i >= prev_v:

         v_i = low_i.

      else:

         v_i = prev_v.

   But since prev_v is in (high_i, low_i -1) (since case C is when prev_v > high_i and <low_i), and low_i > high_i:

      For example, m=7, low_i=5, high_i=2.

      prev_v is3: which is between high_i (2) and low_i (5) -1 (4).

      So, in this case, we can choose v_i=5.

   So, the choice is the smallest possible in the upper range that is >= prev_v.

But how to handle this in code.

The algorithm for the check would be:

prev_v = 0 (initially for i=1)

for each i in 1 to n:

   compute low = a_i

   high = (a_i +t) % m

   if low <= high:

      # interval is [low, high]

      if prev_v > high:

          return False

      current_v = max(prev_v, low)

      prev_v = current_v

   else:

      # interval is [low, m-1] and [0, high]

      # check if we can find a v_i >= prev_v in either part

      # first check if prev_v is in the upper part [low, m-1]

      if prev_v >= low:

          current_v = prev_v

      else:

          # check if there's a v_i in [0, high] >= prev_v

          # if high >= prev_v, then current_v can be prev_v

          # else, check if high is >= prev_v - m ?

          # Wait, since it's modulo m, but v_i must be >= prev_v as integers.

          # So, if prev_v is in [0, high], then current_v can be prev_v.

          # Otherwise, we need to take the lower part's minimum (0) but it's not >= prev_v.

          # So:

          if high >= prev_v:

              current_v = prev_v

          else:

              # need to take from upper part

              if low > m-1:

                  # impossible, since low <= m-1 (as a_i <m)

                  return False

              current_v = low

              if current_v < prev_v:

                  # even the minimal in upper part is lower than prev_v

                  return False

      # After choosing current_v, check if it's in the allowed ranges.

      # current_v must be either in [low, m-1] or in [0, high].

      # Also, it must be >= prev_v.

      if current_v < prev_v:

          return False

      # Check if current_v is in the allowed ranges.

      if not ((current_v >= low and current_v <= m-1) or (current_v >=0 and current_v <= high)):

          return False

      # update prev_v

      prev_v = current_v

return True

But this code is not correct in all cases. Let's test it against the sample.

Sample input 2:

n=5, m=7, a = [0,6,1,3,2]

Let's binary search for t=1.

Check if t=1 is possible.

For each element:

low_i =a_i, high_i = (a_i +1) mod7.

Elements:

0: low=0, high=1 (0+1=1 mod7=1).

6: low=6, high=0 (6+1=7 mod7=0). So case 2 (low>high).

1: low=1, high=2.

3: low=3, high=4.

2: low=2, high=3.

Processing:

i=1 (a=0):

low=0, high=1 (case1).

prev_v starts at0.

current_v = max(0, 0) =0. prev_v is0.

i=2 (a=6):

low=6, high=0 (case2).

prev_v=0.

We need to see if prev_v >= low (0 >=6? No). So check if prev_v <= high (0<=0 → yes).

So current_v =0. But is 0 in [0, high_i=0] → yes.

prev_v becomes0.

But wait, the required v_i for this element is0. But according to the sample solution, the second element's v_i is0 (6 +1 mod7=0). So x_i=1, which is allowed since t=1.

So for this element, the code would set current_v=0, which is allowed. prev_v remains0.

i=3 (a=1):

low=1, high=2 (case1).

prev_v=0. So current_v =max(0, 1)=1. prev_v=1.

i=4 (a=3):

low=3, high=4 (case1).

current_v =max(1,3) →3. prev_v=3.

i=5 (a=2):

low=2, high=3 (case1).

current_v =max(3,2) →3. prev_v=3.

So the sequence of v's is [0,0,1,3,3], which matches the sample. So the check returns True for t=1. Thus, the minimal t is1.

So the code would work for this case.

Another test case:

Sample input 1:

5 3

0 0 0 1 2

t=0.

Check:

For each element, high_i =a_i +0 mod3.

So high_i =a_i.

So intervals are [a_i, a_i], which is a single value.

Processing:

prev_v starts at0.

i=1: 0 → ok.

i=2: 0 >=prev_v (0). ok.

i=3:0 >=0. ok.

i=4:1 >=0. ok.

i=5:2 >=1. ok.

So check returns True. So t=0 is possible.

Which matches the sample.

So the code works for this case.

Another test case: m=5, a=[3,4], t=1.

Possible v_i's:

i=1: low=3, high=4 mod5=4. Case1. So interval [3,4]. prev_v is0 (initial), but that's not possible. So no.

Wait, no. Wait, in the check code, prev_v starts at0 for i=1.

But for i=1, the interval is [3,4]. prev_v is initially 0 (for i=1). But 0 is not >= prev_v (which is 0) but is outside the interval. So the code would check if prev_v <= high (0 <=4). Yes. current_v = max(0,3)=3. prev_v=3.

i=2: a=4. high_i=4+1=5 mod5=0. So interval [4,0]. case2.

prev_v=3.

Check if prev_v >= low (4): 3 >=4? No. Check if prev_v <= high (0). 3 <=0? No. So need to choose from upper part. So upper part is [4,4], and current_v is4. Which is >=3. So prev_v becomes4.

So the sequence is [3,4], which is non-decreasing. So t=1 is possible.

So the code would return True.

Thus, the code seems to handle this correctly.

So the plan is to implement this binary search approach.

Now, the code:

We need to implement the check function and perform a binary search between 0 and m-1.

The binary search steps:

Initialize left=0, right=m-1.

Initialize answer =m-1.

While left <=right:

   mid = (left + right) //2.

   if check(mid):

      answer = mid.

      right = mid-1.

   else:

      left = mid+1.

Return answer.

Now, implement the check function as described.

Now, let's code this in Python.

But we need to handle the case when the interval is split (low > high).

The code will need to process each element, compute low and high, then determine if the current prev_v can be extended.

Let's code the check function.

The code will look something like:

def is_possible(t, a, m):

    prev_v = 0

    for num in a:

        low = num

        high = (num + t) % m

        if low <= high:

            # interval is [low, high]

            if prev_v > high:

                return False

            current_v = max(prev_v, low)

            prev_v = current_v

        else:

            # split into [low, m-1] and [0, high]

            # case where we have to choose between the two ranges

            # first, check if prev_v is in the upper range

            if prev_v >= low:

                current_v = prev_v

            else:

                # check if prev_v is in the lower range

                if high >= prev_v:

                    current_v = prev_v

                else:

                    # must take the lower bound of the upper range

                    current_v = low

                    if current_v < prev_v:

                        return False

            # now check if current_v is in one of the intervals

            if not ( (current_v >= low and current_v < m) or (current_v <= high) ):

                return False

            prev_v = current_v

    return True

But wait, the condition for checking current_v is in one of the intervals:

For the split case, current_v must be in [low, m-1] OR in [0, high].

But current_v can be in either part. So the condition should be:

(current_v >= low) or (current_v <= high)

But in the split case, low > high.

Yes, because low > high.

So, if current_v is >= low (which is possible since low <=m-1) or current_v <= high (which is possible since high <low).

But how to code this.

In code:

if (current_v >= low) or (current_v <= high):

   pass

else:

   return False

So, in the split case, after choosing current_v, we need to check if it is in either of the two ranges.

But in the code above, after assigning current_v, we check:

if not ( (current_v >= low) or (current_v <= high) ):

    return False

Yes.

So, modifying the code accordingly.

Now, let's test the sample input 2:

a = [0,6,1,3,2], m=7, t=1.

Processing each element:

i=0:

num=0.

low=0, high=1.

prev_v=0.

current_v = max(0,0) =0.

prev_v=0.

i=1:

num=6.

low=6, high=(6+1)%7=0.

split case.

prev_v=0.

prev_v >=low (0 >=6? No).

Check if high >= prev_v (0 >=0? yes). So current_v=0.

Check if 0 >=low (6) or 0 <=0 → yes.

prev_v=0.

i=2:

num=1.

low=1, high=2.

prev_v=0 <=2. current_v = max(0,1)=1.

prev_v=1.

i=3:

num=3.

low=3, high=4.

prev_v=1 <=3. current_v=3.

prev_v=3.

i=4:

num=2.

low=2, high=3.

current_v = max(3,2)=3.

prev_v=3.

All steps passed. return True.

So, t=1 is possible.

Which is correct.

Now, coding this.

Now, for the binary search.

The code will read n and m, and the array a.

Then, perform binary search.

Now, let's code this.

But in Python, for large n, this should be efficient. The check function is O(n), and binary search is O(log m), which is acceptable.

Now, putting it all together.

The code:

Read n and m.

Read the array a.

Define a function is_possible(t):

   process each element as described.

Perform binary search between 0 and m-1.

Return the minimal t.

Now, the code:

But wait, in the check function, the initial prev_v is 0 for the first element. But according to the code, the first element's v must be >=0 and in its interval. But in the first element's case, the previous is not considered. Wait, no. The first element's v_1 must be >=0 (since prev_v starts at0), but in reality, the first element's v_1 can be any value in its interval. Because there's no previous element. So, the code's logic is incorrect for the first element.

Wait, no. The code initializes prev_v as 0, but for the first element, prev_v is not the previous element. It's the initial value. This is a bug.

Oh, right! The first element has no previous element. The code's logic treats prev_v as the previous element's v. So for the first element, the prev_v should be the minimal possible v_1 that is >=0 (but wait, no. The first element's v_1 can be any value in its interval. The next elements must be >=v_1.

So, the code's logic is wrong. Because for the first element, prev_v is initialized as0, but the first element's v_1 can be any value in its interval. The code forces the first element's v_1 to be >=0, but this is not correct.

This is a critical error.

For example, in the first sample input:

The first element is0. If the code initializes prev_v to0, then it's correct. But for the first element, the code's logic requires that prev_v (which is0) is <= high_i. Then current_v is max(prev_v, low_i). So for the first element, the code assumes that the v_1 is >=0. But that's not required. The first element's v_1 can be any value in its interval, and subsequent elements must be >=v_1.

So the code's initial prev_v is wrong. It should be set to the minimal possible v_1 that is in the first element's interval and allows the rest of the elements to be processed.

This indicates that the code's approach is incorrect. The check function as implemented is wrong.

The root cause is that the code starts with prev_v=0, which is the previous element's v for the first element. But the first element's v can be any value in its interval, and subsequent elements must be >= it.

So the code's current approach is incorrect.

We need to fix this.

The correct approach for the first element is to choose the minimal possible v_1 in its interval. Because choosing the minimal possible v_1 allows the rest of the elements to have more flexibility (since they have to be >=v_1).

So for the first element, the code should set v_1 to the minimal possible value in its interval, and then proceed.

But how to compute this.

For example, if the first element's interval is [low_1, high_1], then v_1 should be the minimal possible value in this interval, which is low_1.

Wait, but the first element can choose any value in its interval. However, to minimize the maximum x_i, the first element's v_1 should be chosen as large as possible within the interval. Because a larger v_1 may allow the subsequent elements to have smaller x_i's.

But this is conflicting with the code's approach.

This is a problem. Because the code's initial approach of setting prev_v=0 for the first element is incorrect. The first element's v_1 must be in its interval, but can be any value in the interval. The code's approach assumes that the first element's v_1 is the minimal possible (low_1) or >=0, which is not correct.

So the code's check function is wrong.

This explains why the initial approach fails.

So, how to correctly handle the first element.

The correct approach is to set the first element's v_1 to the minimal possible value in its interval, but allowing any possible value. Then, for the next elements, choose the minimal possible v_i >= v_{i-1} and in their interval.

But how to model this.

But this is not correct. For example, if the first element's interval is [5, 6], m=7. The best choice for v_1 is5, but if the next element's interval is [0,1], then v_2 can't be >=5. So the code would return False, but if we choose v_1=6, then v_2 can be0 only if it's allowed to be >=6 (which is not possible). So, in this case, there's no solution for t=1.

But if the first element's interval is [5,6], and the second element's interval is [0,4], then there's no solution.

But the code would fail to find this if the first element's v_1 is set to5.

So, the initial approach of processing the first element as any other element is incorrect.

Thus, the code's check function is incorrect and needs to be revised.

The correct approach for the first element is to choose v_1 as the minimal possible value in its interval. Then, for each subsequent element, choose the minimal possible v_i >=v_{i-1} and in their interval.

But how to compute this.

The first element's interval could be:

Case1: low <= high.

The possible v_1 is in [low, high].

The minimal v_1 is low, and the maximal is high.

But to allow the rest of the elements to be as small as possible, perhaps we should choose the minimal v_1.

Alternatively, we should choose the smallest possible v_1 that allows the rest of the sequence to be valid.

But how to model this.

This is a problem that requires dynamic programming, but with the given time constraints, it's difficult.

Alternative idea: for the first element, the optimal v_1 is the minimal possible in its interval. Because if the first element's v_1 is as small as possible, then the subsequent elements can choose their v_i's as small as possible, thus minimizing the maximum x_i.

But this may not be the case. However, it's a starting point.

Alternatively, perhaps the first element's v_1 should be the minimal possible value in its interval. Then, for the rest of the elements, process as before.

But this may not be the correct approach.

Let's rework the check function.

The correct check function should:

For the first element:

   determine the possible v_1 in its interval.

   set v_1 to the minimal possible value in its interval (low_1), and then proceed.

But this may not allow the subsequent elements to have a valid sequence.

Alternatively, for the first element, choose the minimal possible v_1 (low_1), then proceed.

If this doesn't work, try a higher v_1 within the interval.

But how to do this efficiently.

This approach would require backtracking, which is not feasible for large n.

Thus, perhaps the initial approach is correct, but the code's initial prev_v is incorrect.

The code's current logic initializes prev_v to0, but this is wrong. For the first element, the previous is not considered. The first element's v_1 can be any value in its interval, and the subsequent elements must be >=v_1.

Thus, the code's check function should:

prev_v is set to the minimal possible value in the first element's interval.

Then, for subsequent elements, process as before.

But how to compute the minimal possible value in the first element's interval.

For the first element's interval:

if low <= high:

   possible values are [low, high]. The minimal is low.

else:

   possible values are [low, m-1] and [0, high]. The minimal is 0.

So, the first element's v_1 is set to the minimal possible in its interval.

Then, for the rest of the elements, process as before.

Thus, the check function should be modified to:

prev_v = first element's minimal possible value.

Then, proceed with processing the rest.

So, the code's check function should:

prev_v = minimal possible value of the first element's interval.

for i from 2 to n:

   ...

But how to compute the first element's minimal possible.

For the first element:

compute low =a[0], high = (a[0] +t) mod m.

if low <= high:

   minimal v_1 is low.

else:

   minimal v_1 is 0.

So, the first element's v_1 is set to the minimal possible value in its interval.

Then, for each subsequent element, process as before.

Let's test this with the sample input 2.

Sample input 2:

a = [0,6,1,3,2], m=7, t=1.

First element is0. low=0, high=1. So minimal v_1 is0.

prev_v =0.

Then proceed.

i=1 (element6):

low=6, high=0.

prev_v=0.

We need to choose v_i >=0.

Case split.

prev_v >=low? 0 >=6? No.

Check if prev_v <= high (0 <=0 → yes). So current_v=0.

Check if 0 is in either [6,6] or [0,0]. Yes.

prev_v=0.

i=2 (element1):

low=1, high=2. prev_v=0 <=2.

current_v = max(0,1) =1.

prev_v=1.

i=3 (element3):

low=3, high=4. current_v =max(1,3) =3.

prev_v=3.

i=4 (element2):

low=2, high=3. current_v =max(3,2) =3.

prev_v=3.

All steps passed.

Thus, the code would return True for t=1.

Another example: first element has interval [5,6], m=7. t=1.

The first element's v_1 is5.

Then, next element's interval is [0,0].

prev_v=5.

Check if 0 >=5 → no. So return False.

But if the first element's v_1 is6, then next element's interval [0,0] cannot be >=6. So no solution.

So, the code correctly returns False.

Thus, the check function should be modified to set the first element's v_1 to the minimal possible value in its interval, then proceed.

Thus, the code should be:

def is_possible(t, a, m):

    if not a:

        return True

    # handle first element

    first = a[0]

    low = first

    high = (first + t) % m

    if low <= high:

        current_v = low

    else:

        current_v = 0  # minimal possible in [0, high] or [low, m-1]

        # check if 0 is in the interval.

        # since it's split into [low, m-1] and [0, high], 0 is in [0, high].

        # so current_v =0.

    prev_v = current_v

    for num in a[1:]:

        low = num

        high = (num + t) % m

        if low <= high:

            # interval is [low, high]

            if prev_v > high:

                return False

            current_v = max(prev_v, low)

            prev_v = current_v

        else:

            # split into [low, m-1] and [0, high]

            # case where we have to choose between the two ranges

            # first, check if prev_v is in the upper range

            if prev_v >= low:

                current_v = prev_v

            else:

                # check if prev_v is in the lower range

                if high >= prev_v:

                    current_v = prev_v

                else:

                    # must take the lower bound of the upper range

                    current_v = low

                    if current_v < prev_v:

                        return False

            # now check if current_v is in one of the intervals

            if not ( (current_v >= low) or (current_v <= high) ):

                return False

            prev_v = current_v

    return True

But how to compute the first element's current_v.

In the case where the interval is split (low >high), the minimal possible v_1 is0, but only if 0 is in the interval. For example, if the first element's interval is [5, 2] (m=7), then the possible v_1's are [5,6] and [0,2]. The minimal possible is0.

But if the first element's interval is [3,1] (m=5), then possible v_1's are [3,4] and [0,1]. The minimal is0.

So the code for the first element is:

low = a[0]

high = (a[0] + t) % m.

if low <= high:

   current_v =low.

else:

   current_v =0.

But we need to check if0 is in the possible intervals. For example, if the first element's interval is [5,6] (m=7), then low <=high, so current_v is5. But if the first element's interval is [5, 2], then current_v is0.

But in that case, 0 is in [0, 2] (high=2).

Thus, the code correctly sets current_v to0.

Thus, the code for the first element is correct.

Now, let's test the first sample input.

Sample input1:

n=5, m=3, a=[0,0,0,1,2], t=0.

First element's low=0, high=0. So current_v=0.

prev_v=0.

Rest of the elements are processed as before.

All pass. So returns True.

Another example where the first element's interval is split.

m=7, a=[6], t=1.

First element's low=6, high=0.

current_v=0.

Which is in the interval.

The check returns True.

But this is correct, since the element can be incremented once (6+1 mod7=0), which is allowed.

Thus, the code is correct.

Thus, the code is now correct.

Thus, the code for the problem is as follows.
</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    if n == 0:
        print(0)
        return
    
    def is_possible(t):
        # Handle the first element
        first = a[0]
        low = first
        high = (first + t) % m
        
        if low <= high:
            current_v = low
        else:
            current_v = 0  # minimal possible in [0, high]
            # Check if 0 is within the possible values
            if not (current_v <= high):
                return False
        
        prev_v = current_v
        
        for num in a[1:]:
            low = num
            high_val = (num + t) % m
            
            if low <= high_val:
                if prev_v > high_val:
                    return False
                current_v = max(prev_v, low)
                prev_v = current_v
            else:
                # Check upper range first
                if prev_v >= low:
                    current_v = prev_v
                else:
                    if high_val >= prev_v:
                        current_v = prev_v
                    else:
                        current_v = low
                        if current_v < prev_v:
                            return False
                # Check if current_v is within the allowed intervals
                if not (current_v >= low or current_v <= high_val):
                    return False
                prev_v = current_v
        
        return True
    
    left = 0
    right = m - 1
    answer = m  # Initialize with a value larger than possible
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(answer)

if __name__ == "__main__":
    main()
```