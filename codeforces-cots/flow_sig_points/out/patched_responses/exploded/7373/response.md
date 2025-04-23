<think>
Okay, I need to solve this problem where Devu wants the minimum of array a to be at least the maximum of array b. And I have to find the minimum number of operations to achieve this. Let's think.

First, what's the condition here? The minimal element in a after all operations must be >= the maximal element in b. So the key is to determine what the target values are for the elements of a and b.

Wait, but the problem allows modifying any elements. So the way to minimize operations is to adjust the minimal a and maximal b, but perhaps other elements in a and b can be modified as well. But since the problem's condition only depends on the minimal of a and maximal of b, maybe we just need to make sure that the minimum of a after any operations is >= the maximum of b after any operations. But how?

Wait, but the way to minimize the operations is probably to set the minimal a (after operations) as the maximum between the current minimal a and the current maximum b, but maybe even higher? No, because that would require more operations. Wait, let's see.

For example, suppose the current min a is 2, current max b is 5. Then the min a must be increased to at least 5. So each element in a must be >= 5. But the minimal of a needs to be >=5, which means all elements in a must be >=5. So the minimal element in a has to be >=5. So the minimal a after operations is 5 (or higher). But what's the most efficient way?

Wait, no. Because the minimal of a after operations must be >= the maximum of b after operations. So the maximum of b can be decreased. So maybe the optimal approach is to find a value x such that the minimal a after operations is x, and the maximum of b after operations is <=x. Then, the minimal x that allows this. Then the total operations would be the sum of (ai - original ai if we are decreasing them to x, but wait no. Wait, ai can be modified in any way, but the minimal a after modification must be >= x, and the maximum b after modification must be <=x. So the minimal a (after modification) is the smallest element in a after modifications. So that smallest element must be >= x. The largest element in b after modifications must be <=x. So x must be at least the maximum between the original minimal a (if we can increase some a's elements) and the original max b (if we can decrease some elements of b). Wait, maybe x needs to be the maximum of the original a's min and b's max, but perhaps even higher?

Hmm, no. Because if the original a's min is already >= the original b's max, then x can be the original a's min. So no operations needed. Like example 3.

But if the original a's min is less than the original b's max, then we need to adjust. For example, in example 1, the original a is [2,3], min is 2. Original b is [3,5], max is 5. So 2 <5. So x needs to be at least 5. But wait, in example 1, after operations, the a's min becomes 3, and the b's max becomes 3. So x here is 3. Wait, but how? Wait, the a's min after operations is 3, which is >= the b's max after operations (3). So x here is 3. But in that case, the original a's min is 2 and the original b's max is 5. So x here is 3, which is higher than the a's original min but lower than the original b's max. But in that case, the maximum of b after operations is 3. So how was that achieved? Because we can decrease the elements of b. So the idea is to choose x such that x is >= some value. Wait, perhaps x is the maximum between the minimal possible a's min (after increasing some elements) and the minimal possible b's max (after decreasing some elements). Wait, perhaps x can be any value that is at least the maximum of (current a's min, current b's max). Wait no. Let's think differently.

Let me rephrase the problem. We need to find the minimum possible x such that x is >= all elements in b (after any modifications) and x is <= all elements in a (after any modifications). Because the maximum of b's elements after modifications must be <=x, and the minimum of a's elements after modifications must be >=x. So x must be in the range where x is the minimal possible value that allows this. Because the higher x is, the more operations we might need. Wait, no. Wait, the minimal number of operations would be when x is as low as possible. Because if x is lower, then we have to do fewer operations. For example, if x is 5, then a's elements need to be at least 5 (so each a_i that is below 5 needs to be increased to 5, which takes (5 - a_i) steps), and each element in b that is above 5 needs to be decreased to 5 (taking (b_i -5) steps). But if x is 6, then the steps would be higher. So the minimal x that satisfies x >= all elements in b (after modifications) and x <= all elements in a (after modifications) would be the minimal possible x. Wait, no. Because the elements in a can be modified to any values as long as their minimum is >=x, and the elements in b can be modified as long as their maximum is <=x. So the minimal x is the maximum between the minimal possible a's min and the maximal possible b's max. Wait, this is getting a bit confusing.

Alternative approach: To satisfy the condition, the minimal of a (after modification) must be >= the maximum of b (after modification). So let's denote the minimal a after mod as A_min, and the maximum b after mod as B_max. Then A_min >= B_max. To minimize the operations, what's the best way to choose A_min and B_max? We can choose B_max as high as possible, as long as it's <= A_min. So the minimal total operations would be achieved when A_min = B_max. Because if we have A_min > B_max, then perhaps we can decrease A_min and B_max to meet at some lower x, which would reduce the required operations.

So the optimal x is the minimal possible value such that x >= original B_max and x >= original A_min. Wait, no. Because in example 1, the original A_min is 2, original B_max is 5. So x must be >=5 (since A_min has to be >= B_max's new value. But in the example 1 solution, x is 3. Wait, how? Because in that case, the B_max after modifications is 3, which is less than the original B_max of 5. So x can be lower than the original B_max if we modify the B array to reduce their elements.

Ah, right. So x can be any value such that the maximum of the modified B array is <=x, and the minimum of the modified A array is >=x. So the minimal x possible is the maximum between the original A_min (if we can't lower it) and the original B_max (if we can't lower it). But perhaps x can be lower than both if we can adjust both arrays.

Wait, but how? Let's think. Suppose original a is [2,3], min is 2. Original b is [3,5], max is5. So the original condition is 2 <5, so not satisfied. To make the a's min >= b's max, we can either increase a's elements so that their min is >=5, or decrease b's elements so that their max is <=2. Which one is cheaper.

In the first case, the a's elements must all be at least 5. So for a array [2,3], we need to increase 2 to5 (3 operations) and 3 to5 (2), total 5. The b array's elements must be <=5, but since their max is 5, no change needed. So total 5 operations. But the sample output is 3, which is achieved by increasing a's min to3 (from2, cost1) and decrease b's max from5 to3 (cost2). So total 3. So this approach is better. So here, x is3. So x can be lower than both original A_min and original B_max. Wait, original A_min is2, original B_max is5. So x is3, which is higher than original A_min (2) and lower than original B_max (5). But how is that possible?

Because when we modify a and b arrays. For a, the new min is3 (so we set the original 2 to3, and 3 remains3). For b, the new max is3 (original 3 and5, which are modified to3 and3). So in this case, x is3, which is >=a's new min (3) and >=b's new max (3). Wait, but the condition is a's min >=b's max. So 3 >=3. So that's allowed. So in this case, x is3. So x can be any value that allows a's min to be >= x and b's max to be <=x. Wait, no. Wait, the a's min is the minimum of the modified a array, which must be >= the maximum of the modified b array (which is <=x). So x is not necessarily the same as the a's min or the b's max, but it's the threshold that a's min must be >= and the b's max must be <=. Wait, maybe I'm getting confused here.

Alternatively, the problem requires that min(a) >= max(b). So the minimal possible x where x is the minimal possible value of max(b) such that x <= min(a). So to minimize the operations, we can find the x such that x is the maximum between the original minimum of a and original maximum of b. Wait, but in example1, the original minimum of a is2 and original maximum of b is5. So x would be5. But in the example, x is3. So that approach is not correct.

Hmm. So perhaps the optimal x is the maximum between the original minimum of a and the original maximum of b. Wait, no. Because in example1, the original min a is2, original max b is5, which gives x=5. Then, for a to have min 5, the operations are (5-2)+(5-3) =3+2=5. For b to have max5, which is already 5, no operations. So total 5. But the example's answer is3, which is better. So this approach is wrong.

So, what's the correct way to model this?

The key is that modifying elements of a and b can allow for x to be any value where x is such that the minimal element of a is at least x and the maximal element of b is at most x. So x can be any value in between, as long as these two conditions are satisfied. Our goal is to find the x that requires the least total operations.

So for each possible x, compute the cost required to make all a's elements >=x (so the minimal a's element is >=x) and all b's elements <=x (so the maximum b's element is <=x). Then find the x that minimizes the total cost.

But how do we find x efficiently? Since x can be any integer (since elements can be modified to any integers), but the possible x's are constrained by the original arrays. For example, x can't be lower than the original a's min (since we can decrease a's elements, but then the minimal of a would be lower than x, which would not satisfy the condition). Wait no. Wait, if x is the value such that the minimal a after modification is >=x, then x can be any value, but the minimal a after modification must be >=x. So for example, if we have a's original elements [2,3], and x is3, then the minimal a after modification must be >=3. So we can modify the 2 to3 (cost1) and leave 3 as is. So the minimal is3, which is >=x (3). But if x is4, then the minimal a must be >=4, which would require modifying 2 to4 (cost2) and 3 to4 (cost1), total 3. So the x can vary, and the cost depends on it.

So the problem reduces to finding x such that:

x can be any integer (since we can adjust elements as needed), but the minimal x must be such that the sum of (max(0, x - a_i) for a_i <x) to increase a's elements to x (but wait, no. Wait, the a's elements can be adjusted to any values as long as their minimum is >=x. So we can have some a's elements higher than x. So the minimal possible cost is for each a_i, if a_i is less than x, we have to increase it to at least x. But increasing it to exactly x is the minimal cost. Because if we increase it to x+1, that would cost more. So the minimal cost for a is sum(max(0, x - a_i) for all a_i). Because each a_i must be >=x. So for a_i less than x, we have to increase them to x. For a_i >=x, no cost. Similarly, for each element in b, we have to ensure that they are <=x. So for each b_i greater than x, we need to decrease them to x. The cost is sum(max(0, b_i -x) for all b_i).

So the total cost for a given x is sum(max(0, x - a_i) for a_i in a) + sum(max(0, b_i -x) for b_i in b).

We need to find the x that minimizes this total cost.

But what are the possible x values?

The x can be any integer where x is >= the minimal a's element after modification (which is >=x). Wait, no. The x is the value that the minimal a after modification must be >=x. Wait, but if x is 3, and all a's elements are increased to 3, then the minimal a is 3 >=3, which is okay. But if x is 4, then all a's elements must be >=4. So for a's original [2,3], you have to raise 2 to4 (cost2), and 3 to4 (cost1). So the minimal a is4 >=4.

So x can be any integer, but the minimal a after modification is >=x, and the maximum b after modification is <=x.

But how to model x in such a way that the minimal a is >=x and the maximum b is <=x. Wait, no. Because the minimal a after modification is the minimal of all a_i after modification. So if x is 3, then each a_i must be >=3, so the minimal of a_i is >=3. Similarly, each b_i must be <=3, so the maximum of b_i is <=3. Thus, x must be >= the minimal of a's modified array and <= the maximum of b's modified array. Wait, no. The x is the value that the minimal a is >=x and the maximum b is <=x. So x can be any value between the minimal a and maximum b after modifications, but how?

No, that's not possible. Because the minimal a after modifications is >=x, and the maximum b after modifications is <=x. Therefore, the minimal a is >=x and the maximum b is <=x. So x must be <= the minimal a's modified value and >= the maximum b's modified value. But since the minimal a's modified value is >=x and the maximum b's modified value is <=x, then x must be >= maximum b's modified value and <= minimal a's modified value. But for this to be possible, the maximum b's modified value must be <=x <= minimal a's modified value. But this is only possible if x is between those two values. So the minimal a's modified value must be >=x and the maximum b's modified value must be <=x. So x can be any value that is between the maximum b's modified value and the minimal a's modified value. But how do we find such x?

Alternatively, the x is a value that must be chosen such that x is the maximum between the required a's minimal and the required b's maximum. Wait, this seems getting too abstract. Let's think in terms of the cost function.

The total cost is a function of x: cost(x) = sum( max(0, x - a_i) for a_i in a ) + sum( max(0, b_i - x) for b_i in b )

We need to find the x that minimizes cost(x).

But what is the domain of x for which the problem's condition is satisfied? For the problem's condition to be satisfied, the minimal of a after modifications (which is the minimal of a's modified values) must be >= the maximum of b after modifications (which is the maximum of b's modified values). But how does that relate to x? Because x is the threshold for the cost calculation. So for example, if x is 3, then the cost calculation assumes that all a's elements are >=3 (so the minimal a after modification is 3) and all b's elements are <=3 (so the maximum b after modification is3). So in that case, the minimal a is3 and the maximum b is3, which satisfies the condition. So the cost function's x is exactly the minimal x that allows the problem's condition to be satisfied.

Wait, no. Because if x is 3, but some a's elements are modified to 4 (so their cost is 1 each), then the minimal a would be3 (if there's an element modified to3). So in that case, the minimal a is3, which is >=x (3). So for the problem's condition, the minimal a is >= the maximum b. But in this scenario, the maximum b is3. So it's satisfied.

So the cost function's x is a parameter that, when chosen, ensures that the problem's condition is met. Because:

- All a's elements are >=x. So the minimal a after modification is >=x.

- All b's elements are <=x. So the maximum b after modification is <=x.

Thus, minimal a >=x >= maximum b. So minimal a >= maximum b, which satisfies the problem's condition.

Thus, for any x, the cost function's x ensures that the problem's condition is satisfied. Therefore, to find the minimal cost, we need to find the x that minimizes the sum of operations, which is the sum of (x - a_i) for a_i <x (increase a_i to x) and (b_i -x) for b_i >x (decrease b_i to x).

So now the problem reduces to finding the x that minimizes the cost function.

But what x values should we consider? Because x can be any integer where the a's elements are modified to >=x and the b's elements are modified to <=x. However, the optimal x is likely to be in the range between the original minimum of a and the original maximum of b, or perhaps even beyond.

Wait, no. Let's think. Suppose the original a's min is 2, and original b's max is5. Then x can be 3, which is between them. But how?

But in that case, all a's elements must be >=3, which requires increasing those a_i below3. All b's elements must be <=3, which requires decreasing those b_i above3.

But how can x be between the original a's min and original b's max? For example, in the first example, x is3, which is between a's min (2) and b's max (5). So that's allowed.

So the x can be any value. But how to find the minimal cost?

The cost function is a convex function. Let's see. For a given x, the cost is sum of (x -a_i) for a_i <x, plus sum (b_i -x) for b_i >x. As x increases, the first part (sum for a) increases for a_i <x, but when x crosses a_i, the term for that a_i starts increasing. Similarly, the second part (sum for b) decreases as x increases, but when x crosses a b_i, the term for that b_i stops contributing. So overall, the cost function is a convex function. It first decreases, reaches a minimum, then increases. Therefore, the minimal cost is achieved at a certain x, and we can use ternary search to find it.

But how to determine the possible range for x where the minimal cost is achieved.

The minimal possible x is the minimal a's element (since x can't be lower than that, because if x is lower than some a_i, but then the a_i can be left as is, but the minimal a after modification would be >=x. For example, x=1, but a's elements are 2 and3. Then sum (x -a_i) would be negative, but since we take max(0, x -a_i), which is zero. So the cost for a is zero, but x must be <= the minimal a after modifications. Wait, but in this case, the minimal a after modifications is2, which is >=x=1. So the condition is satisfied. So in this case, the x can be as low as possible, but then the sum for b's elements (which are, say, 5) would be sum (5 -x) =5-1=4. So the total cost is4. But if x is3, the sum for a would be (3-2)=1, and for b would be (5-3)+(3-3)=2. So total 3, which is better.

So the minimal x could be in a range where x is between the minimal a and the maximal b. But how to find the x that gives the minimal cost?

Alternatively, the minimal x is the minimal possible, but when x is lower than the original a's min and original b's max, perhaps that's not possible. Because in that case, the sum for a is zero (since x is less than or equal to all a_i's, so x -a_i is negative, so max(0, ...) is zero. So the sum for a is zero. For b, the sum is sum(b_i -x) for each b_i >x. So to minimize the sum, x should be as large as possible, but if x is less than the original b's max, then sum will be higher. So perhaps the minimal x is somewhere around the original a's min and original b's max.

But how to model this? Let's think about the cost function.

Let me see the cost function as a function of x. For x less than all a_i and x greater than all b_i, the sum for a is zero and the sum for b is zero. But that's only possible if x is <= min(a) and x >= max(b). Which is possible only if min(a) >= max(b). In that case, x can be any value in [max(b), min(a)], and the cost is zero. Which is the case in example3.

So the minimal cost is achieved when the problem's condition is already satisfied, so x can be any value between max(b) and min(a), and the cost is zero.

But when min(a) < max(b), then x must be chosen to be >= some value. So how?

Let me think of the cost function as follows.

For x in the range from the original a's min (a_min) to the original b's max (b_max), the cost function is sum of (x - a_i) for a_i <x and sum (b_i -x) for b_i >x.

But when x is less than a_min, the sum for a is zero (since all a_i are >=x), and the sum for b is sum(b_i -x). This sum decreases as x increases. So the cost is sum(b_i -x) in that region.

When x is between a_min and b_max, the sum for a increases as x increases (since x is larger than a_min, so some a_i may be less than x). The sum for b decreases as x increases (since x is larger, more b_i are <=x). So in this region, the cost function may have a minimum.

When x is greater than b_max, the sum for a is sum(x -a_i) for all a_i (since x is larger than all a_i), and sum for b is zero (since x is larger than all b_i). So the cost is sum(x -a_i) for all a_i. Which increases as x increases.

So the cost function is:

- For x < a_min: cost(x) = sum_b (b_i -x) if b_i >x. Since x < a_min <= a_i, sum_a is zero. But sum_b is sum of (b_i -x) for all b_i >x.

- For a_min <=x <=b_max: cost(x) = sum_a (x -a_i for a_i <x) + sum_b (b_i -x for b_i >x).

- For x >b_max: cost(x) = sum_a (x -a_i) for all a_i (since x> a_i), sum_b is zero.

So the minimal cost is either in the a_min <=x <=b_max region, or in the x <a_min region, or in the x >b_max region. Wait, but if a_min <b_max, then x <a_min implies that x <a_min <b_max, so the sum_b (b_i -x) for x <a_min would include all b_i >x. So for example, if x is a_min-1, then sum_b is sum(b_i -x) for all b_i >x (which is all b_i >=a_min-1+1 =a_min). So this could be a large sum.

But if x is a_min, then sum_a would start contributing (summing a_i <x, which is a_i <a_min. But since a_min is the original a's minimum, there are no a_i <a_min. So sum_a is zero. Sum_b would be sum(b_i -a_min) for b_i >a_min.

So the cost for x=a_min is sum_b (b_i >a_min) (b_i -a_min). For x=a_min+1, sum_a is sum (x -a_i for a_i <x). Since a_i >=a_min (as a_min is the original min), but x is a_min+1. So a_i can be a_min or higher. So sum_a is (a_min+1 - a_min) for a_i =a_min. So for each a_i equal to a_min, we add 1. For a_i larger, nothing. Sum_b is sum (b_i -x) for b_i >x. So x is a_min+1. So sum_b is sum (b_i - (a_min+1)) for b_i >a_min+1.

So the cost could be lower than x=a_min.

So the minimal cost is likely to be in the a_min <=x <=b_max region, or perhaps x >=b_max. But how?

Alternatively, the minimal cost could be achieved when x is the median of some values.

But considering that the cost function is convex, ternary search can be applied. So the approach could be:

1. Find the minimal a_min and maximal b_max in the original arrays.

2. If a_min >=b_max, then return 0. No operations needed.

3. Else, perform ternary search in the possible x range to find the x that gives the minimal cost.

The possible x range would be from a_min to b_max. Because for x <a_min, the sum_a is zero, but sum_b is sum(b_i -x) which is higher for lower x. So the minimal in this region is x=a_min. But that's included in the a_min <=x <=b_max range.

So the ternary search would be between x_low and x_high, where x_low is a_min and x_high is b_max.

Wait, but the minimal cost may not be in this interval. For example, suppose that a has elements [1,2,3], and b has [4,5]. So a_min is1, b_max is5. The condition is not satisfied. The required x must be >=1 and >= the modified b's max. But x can be 3, which is between a_min and b_max. So the sum for a is (3-1)+(3-2) = 2+1=3. Sum for b is (4-3)+(5-3) =1+2=3. Total 6. Alternatively, x=5. Sum a is 5-1 +5-2 +5-3 =4+3+2=9. Sum b is0. Total9. So better to choose x=3.

But how do we know that x is in [a_min, b_max]?

Well, in the example where a_min is1 and b_max is5, the minimal cost is achieved at x=3, which is within the interval.

Another example: a is [2,3], b is [3,5]. a_min=2, b_max=5. The minimal x is3, which is in the interval.

So perhaps the minimal x is in [a_min, b_max], so the ternary search can be done between a_min and b_max.

So the steps are:

- Compute a_min = min(a array)

- Compute b_max = max(b array)

- If a_min >=b_max: output 0.

- Else:

   - The x must be in [a_min, b_max], since for x <a_min: sum_a is zero (since x is <a_min, which is the minimal a_i. So all a_i >=x. So sum_a is zero. sum_b is sum(b_i -x) for b_i >x. Which is sum(b_i) - m*x, where m is the count of b_i >x. As x increases, this sum decreases. So the minimal x in this region is x =a_min. But the cost at x=a_min is sum(b_i -a_min) for b_i >a_min. Then, when x is a_min+1, the sum_b is sum(b_i - (a_min+1)) for those b_i >a_min+1. Which could be smaller. So the minimal cost may be found in the [a_min, b_max] interval.

So to find the minimal x, we can perform a ternary search in the range [a_min, b_max], as the cost function is convex.

But how to handle the integer values for x? Because ternary search is typically applied to real numbers, but here x must be an integer. So we can adapt the ternary search for integers.

Alternatively, since the cost function is convex, we can compute the minimal by checking x in the range where the cost is minimized. For example, find x where the cost(x) is minimal, which can be found by checking the points where the derivative changes sign.

But for integers, the minimal can be found by checking x where cost(x) is <= cost(x-1) and cost(x) <= cost(x+1). So once we find such an x, that's the minimal.

Alternatively, perform a ternary search between a_min and b_max, and compare the cost at mid and mid+1 to decide the direction.

So let's outline the steps:

1. Compute a_min and b_max.

2. If a_min >=b_max, return 0.

3. Else, find x in [a_min, b_max] that minimizes cost(x).

The cost function for x is sum of (x - a_i if a_i <x else 0) for all a_i, plus sum of (b_i -x if b_i >x else 0) for all b_i.

So how to compute this efficiently?

The sum for a can be computed as sum( max(0, x - a_i) for a_i in a )

But for large n and m (up to 1e5 each), we need an O(1) or O(log n) way to compute the sum for a and sum for b for a given x.

To compute sum of (x - a_i) for all a_i <x: this can be done by sorting the a array and finding the number of elements less than x and their sum. Similarly for the b array.

So the steps are:

- Sort a in ascending order.

- Sort b in descending order (or ascending, then reversed).

Wait, for a array:

sum of (x -a_i) where a_i <x: this can be computed as x * k - sum_a_less, where k is the number of a_i <x, and sum_a_less is the sum of those a_i.

Similarly for b: sum of (b_i -x) where b_i >x: sum_b_greater - x * l, where l is the number of b_i >x, and sum_b_greater is the sum of those b_i.

So to compute this efficiently, we can pre-sort a and b.

So for the a array, sorted in ascending order:

For a given x, find the index where a_i <x. All elements before that index are <x.

Similarly for the b array sorted in ascending order: elements after a certain index are >x.

So here's the plan:

1. Sort the a array in ascending order, compute a prefix sum array.

2. Sort the b array in ascending order, compute a prefix sum array.

3. For a given x:

   a. For a array, find the largest index where a_i <x. The number of elements less than x is idx+1. The sum of those elements is the prefix sum up to idx+1.

   b. The sum for a is x*(idx+1) - prefix_a[idx+1].

   c. For b array, find the smallest index where b_i >x. The number of elements greater than x is len(b) - idx. The sum of those elements is total_b_sum - prefix_b[idx].

   d. The sum for b is sum_b_greater - x * (len(b) - idx).

   e. Total cost is sum_a + sum_b.

So, to compute this for a given x, the time is O(log n + log m), which is acceptable.

Thus, the overall approach is:

- Pre-sort the arrays and compute their prefix sums.

- Use ternary search between a_min and b_max to find the x that minimizes the cost.

Now, implementing this.

But first, how to handle the possible x values? Let's see.

The ternary search for integers works as follows:

Initialize low = a_min, high = b_max.

While low < high:

   mid = (low + high) // 2

   if cost(mid) < cost(mid+1):

       high = mid

   else:

       low = mid +1

At the end, low is the minimal x.

But wait, this is the case for a convex function. For example, the function first decreases then increases. So when comparing mid and mid+1, if cost(mid) < cost(mid+1), then the minimal is in the left half. Else, in the right half.

This approach would find the minimal x.

But need to verify.

So the code steps would be:

Sort a, compute prefix sums.

Sort b, compute prefix sums and total sum.

Compute a_min = a[0], b_max = b[-1].

If a_min >=b_max: output 0.

Else:

   Perform ternary search between low =a_min and high =b_max.

Once x is found, compute cost(x).

But wait, perhaps the minimal x is not in this range, but when x is a_min-1, but that's not possible because when x is a_min-1, a's sum is zero (since all a_i >=x), but b's sum is sum(b_i -x) for b_i >x. For x =a_min-1 <a_min, which may be possible if a_min is not 1.

But in that case, the sum for a is zero, and the sum for b is sum(b_i -x) for b_i >x. But x is a_min-1. For example, a_min is2, x=1. So sum for a is zero. sum for b is sum(b_i -1) for b_i>1. Which may be higher than when x is2.

But in the ternary search between a_min and b_max, the minimal x could be in that interval. So perhaps the minimal x is found in that interval.

But perhaps not. For example, suppose a is [2,3], and b is [5,5]. a_min is2, b_max is5. So x can be 3.

Cost for x=2: sum a is0 (since a_i >=2), sum b is (5-2)*2 =3*2=6. Total6.

For x=3: sum a is (3-2)*1 +0=1. sum b is (5-3)*2=4. Total5.

For x=5: sum a is (5-2)+(5-3) =3+2=5. sum b is0. Total5.

So here, the minimal cost is5, achieved at x=3 and x=5. So the minimal x is in the interval. But wait, the cost is same at x=3 and x=5?

Wait, no. Let me calculate.

Wait, a is [2,3], x=3:

sum a is (3-2) =1, since 3 is >=3, so only the first element contributes. sum a is1.

sum b is (5-3)*2=2*2=4. Total 5.

x=5:

sum a is (5-2)+(5-3) =3+2=5. sum b is0. Total5.

So the total cost is same. So the minimal x could be any x between 3 and5. Wait, but what's the cost for x=4?

sum a: (4-2)+(4-3) =2+1=3.

sum b: (5-4)*2=1*2=2. Total5.

Wait, 3+2=5. So same total.

So for x=3,4,5, the cost is5. So the minimal cost is5.

But the x can be anywhere in [3,5]. So the minimal x is not unique.

But the problem requires the minimal x that gives the minimal cost. But in this case, any x in that range would give the same cost.

But how to find the minimal x. Well, the ternary search would find one of them.

But in terms of code, the ternary search would find the minimal x in the interval [a_min, b_max], which is the x that is the first one where the cost is minimal.

But for the code, as long as we compute the minimal possible cost, it's okay.

So the plan is:

- Sort a in ascending order, compute prefix sums.

- Sort b in ascending order, compute prefix sums and the total sum of b.

- Compute a_min and b_max. If a_min >=b_max: return0.

- Else, perform ternary search between a_min and b_max.

Now, how to implement the cost function.

For a given x:

In a, find the number of elements <x. Since a is sorted, we can use bisect_left to find the insertion point of x. The number of elements less than x is the insertion index.

sum_a = x * num_less - prefix_a[num_less]

In b, find the number of elements >x. Since b is sorted in ascending order, we can find the first index where b_i >x. All elements after that are >x.

For example, using bisect_right(x) gives the insertion point after all elements <=x.

So the number of elements >x is len(b) - bisect_right(x).

sum_b_greater = total_b_sum - prefix_b[bisect_right_x]

sum_b = sum_b_greater - x * num_greater.

Thus, sum_total = sum_a + sum_b.

So code steps.

Now, let's code this.

First, read input:

n, m = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

Sort a and compute prefix sums.

a.sort()

prefix_a = [0] * (n+1)

for i in range(n):

    prefix_a[i+1] = prefix_a[i] + a[i]

Sort b and compute prefix sums and total sum.

b.sort()

prefix_b = [0] * (m+1)

for i in range(m):

    prefix_b[i+1] = prefix_b[i] + b[i]

total_b = prefix_b[-1]

Compute a_min and b_max.

a_min = a[0]

b_max = b[-1]

If a_min >=b_max: print(0) and exit.

Else, perform ternary search.

But how to implement ternary search for integers.

Here's the approach:

low = a_min

high = b_max

while low < high:

    mid = (low + high) // 2

    if cost(mid) < cost(mid +1):

        high = mid

    else:

        low = mid +1

At the end, compute cost(low) and also check cost(high) in case.

But since after the loop, low == high, which is the x that minimizes the cost.

But wait, let's test with the example where x can be 3,4,5.

Suppose during the loop:

low =3, high=5.

mid=4.

compute cost(4) and cost(5). cost(4) is5, cost(5) is5. So since cost(4) < cost(5) is false, low=mid+1=5. Now low=5, high=5. Loop ends. So the x is5. But the minimal x is3. So this approach would choose x=5, but the cost is the same. So the code would still compute the correct total cost.

But in the case of multiple x's with the same cost, the code will return one of them. But since the problem requires the minimal operations, which is the same in all cases, it's okay.

Thus, the code can proceed.

Implementing the cost function.

def compute_cost(x):

    # a array: sum (x - a_i) for a_i <x

    # find the number of a_i <x.

    # a is sorted.

    num_less = bisect.bisect_left(a, x)

    sum_a = x * num_less - prefix_a[num_less]

    # b array: sum (b_i -x) for b_i >x

    # find the first index where b_i >x.

    pos = bisect.bisect_right(b, x)

    num_greater = m - pos

    sum_b = (prefix_b[m] - prefix_b[pos]) - x * num_greater

    return sum_a + sum_b

Yes.

So the code will use bisect module.

But in Python, we can use the bisect module.

Now, putting all together.

But let's see the first example:

Sample1:

n=2, m=2

a = [2,3]

b = [3,5]

a_min=2, b_max=5.

We need to find x in 2..5.

Possible x:

x=2: sum_a is0 (since a_i >=2). sum_b is (3-2) + (5-2) =1+3=4. Total4.

x=3: sum_a is3-2=1 (only the first element). sum_b is (3-3) +5-3=0+2=2. Total3.

x=5: sum_a is5-2 +5-3=3+2=5. sum_b is0. Total5.

So the minimal is x=3.

The ternary search code would find this.

Let's see the code steps.

low=2, high=5.

mid=(2+5)//2=3.

compute cost(3) and cost(4).

cost(3) is 1+2=3.

cost(4) is (4-2)+(4-3)=2+1=3 for a. sum_b for x=4: bisect_right(b,4) is2 (since b is [3,5], bisect_right(4) gives1 (since 3<=4 and 5>4). pos=1. num_greater=2-1=1. sum_b =5-4=1. sum_total=3+1=4.

so cost(3)=3, cost(4)=3+1=4. So cost(3) < cost(4). So high=3.

Now low=2, high=3.

mid=2.

compute cost(2) and cost(3).

cost(2)=0+ (3-2 +5-2) =1+3=4.

cost(3)=3. Since 4>3, so set low=2+1=3.

Now low=3, high=3. Exit loop.

So x=3, which is correct.

Thus, the code works.

Another example: sample2.

Sample2 input:

3 2

1 2 3

3 4

a sorted [1,2,3], a_min=1.

b sorted [3,4], b_max=4.

a_min=1 <4.

x should be between1 and4.

What is the minimal cost?

Possible x:

x=3: sum_a for elements <3: 1 and2. sum_a=3-1 +3-2 =2+1=3. sum_b for elements>3:4-3=1. total4.

x=4: sum_a= (4-1)+(4-2)+(4-3)=3+2+1=6. sum_b=0. total6.

x=2: sum_a=2-1=1. sum_b=(3-2)+(4-2)=1+2=3. total4.

x=3: total4.

So possible x=3 or x=2.

But according to the sample, the output is4.

So what's the code's calculation?

Let's see.

The code will perform ternary search between1 and4.

Initial low=1, high=4.

mid=(1+4)//2=2.

compute cost(2) and cost(3).

cost(2):

sum_a: a_i <2 are 1. sum_a=2*1 -1=1.

sum_b: elements>2 are3 and4. pos =bisect_right(2) in [3,4] is0. num_greater=2. sum_b=(3+4) -2*2=7-4=3. total1+3=4.

cost(3):

sum_a: a_i <3:1,2. sum_a=3*2 - (1+2)=6-3=3.

sum_b: elements>3:4. sum_b=4-3=1. total4.

So cost(2)=4, cost(3)=4.

So compare cost(2) < cost(3) ?

No. Because 4 is not <4. So else clause: low=mid+1=3.

Now low=3, high=4.

mid=3+4//2=3.

compute cost(3) and cost(4).

cost(3)=3+1=4.

cost(4)=6+0=6.

cost(3) < cost(4) → high=3.

Now low=3, high=3. Exit.

x=3. cost is4.

But the sample output is4. So code returns4. Which is correct.

Thus, the code works.

Another test case: sample3.

Input:

3 2

4 5 6

1 2.

a_min=4, b_max=2. So 4>=2 → output0. Correct.

Thus, the code should handle all cases correctly.

Now, the code.

But for the code, need to handle the prefix sums and bisect.

So the code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    a.sort()
    prefix_a = [0] * (n + 1)
    for i in range(n):
        prefix_a[i+1] = prefix_a[i] + a[i]

    b.sort()
    prefix_b = [0] * (m + 1)
    for i in range(m):
        prefix_b[i+1] = prefix_b[i] + b[i]
    total_b = prefix_b[-1]

    a_min = a[0]
    b_max = b[-1]

    if a_min >= b_max:
        print(0, file=output_stream)
    else:
        low = a_min
        high = b_max

        while low < high:
            mid = (low + high) // 2
            # Compute cost(mid) and cost(mid+1)
            # Compute cost for mid
            num_less = bisect.bisect_left(a, mid)
            sum_a = mid * num_less - prefix_a[num_less]
            pos = bisect.bisect_right(b, mid)
            num_greater = m - pos
            sum_b = (prefix_b[m] - prefix_b[pos]) - mid * num_greater
            cost_mid = sum_a + sum_b

            # Compute cost for mid+1
            num_less = bisect.bisect_left(a, mid+1)
            sum_a = (mid+1)*num_less - prefix_a[num_less]
            pos = bisect.bisect_right(b, mid+1)
            num_greater = m - pos
            sum_b = (prefix_b[m] - prefix_b[pos]) - (mid+1)* num_greater
            cost_mid_plus_1 = sum_a + sum_b

            if cost_mid < cost_mid_plus_1:
                high = mid
            else:
                low = mid + 1

        # Compute the cost for low
        num_less = bisect.bisect_left(a, low)
        sum_a = low * num_less - prefix_a[num_less]
        pos = bisect.bisect_right(b, low)
        num_greater = m - pos
        sum_b = (prefix_b[m] - prefix_b[pos]) - low * num_greater
        total = sum_a + sum_b
        print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2
1 2 3
3 4
""",
            "output": \
"""\
4
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

Thus, code works.

Sample2: output4. As discussed.

Sample3: output0.

Thus, code is correct.

Now, to check for possible edge cases.

Edge case where a and b have one element each.

n=1, m=1.

a = [1], b = [2].

a_min=1 <b_max=2.

code will loop between1 and2.

mid=1. compare cost(1) and cost(2).

cost(1):

sum_a: elements <1:0 → sum_a=0.

sum_b: elements>1 →2-1=1. total1.

cost(2):

sum_a=2-1=1. sum_b=0. total1.

So cost(1) =1, cost(2) =1. So in the loop, since cost(1) is not < cost(2), low becomes 2. Then low=2, high=2. sum is1. output1.

But the correct answer is 1.

Yes.

Another edge case: a is all elements higher than b.

n=3, m=2.

a = [5,6,7], b=[1,2]. a_min=5, b_max=2. So output0.

Thus, code works.

Another case where x is found outside the initial a_min and b_max.

But according to the code, the x is constrained between a_min and b_max.

Thus, the code should handle all cases correctly.

Thus, the code is correct.
</think>

```python
import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
prefix_a = [0] * (n + 1)
for i in range(n):
    prefix_a[i + 1] = prefix_a[i] + a[i]

b.sort()
prefix_b = [0] * (m + 1)
for i in range(m):
    prefix_b[i + 1] = prefix_b[i] + b[i]
total_b = prefix_b[-1]

a_min = a[0] if n > 0 else 0
b_max = b[-1] if m > 0 else 0

if a_min >= b_max:
    print(0)
else:
    low = a_min
    high = b_max

    while low < high:
        mid = (low + high) // 2
        # Calculate cost for mid and mid + 1
        num_less = bisect.bisect_left(a, mid)
        sum_a = mid * num_less - prefix_a[num_less]
        pos = bisect.bisect_right(b, mid)
        num_greater = m - pos
        sum_b = (prefix_b[m] - prefix_b[pos]) - mid * num_greater
        cost_mid = sum_a + sum_b

        num_less = bisect.bisect_left(a, mid + 1)
        sum_a = (mid + 1) * num_less - prefix_a[num_less]
        pos = bisect.bisect_right(b, mid + 1)
        num_greater = m - pos
        sum_b = (prefix_b[m] - prefix_b[pos]) - (mid + 1) * num_greater
        cost_mid_plus_1 = sum_a + sum_b

        if cost_mid < cost_mid_plus_1:
            high = mid
        else:
            low = mid + 1

    # Compute the final cost for low
    num_less = bisect.bisect_left(a, low)
    sum_a = low * num_less - prefix_a[num_less]
    pos = bisect.bisect_right(b, low)
    num_greater = m - pos
    sum_b = (prefix_b[m] - prefix_b[pos]) - low * num_greater
    print(sum_a + sum_b)
```
