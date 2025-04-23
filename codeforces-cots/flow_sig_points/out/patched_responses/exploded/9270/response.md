<think>
Okay, let's see. The problem is to find the minimum number of elements to add to the array so that the median becomes x. The initial array can't be changed, only added to. And the added elements can be any integers from 1 to 1e5. Oh right, including the same numbers.

First, I need to understand what the median position is. The problem says that the median is the element at position floor( (n+1)/2 ) after sorting. Wait, for an array of length m (after adding elements), the median is at position (m+1)//2 - 1 if using zero-based indices. For example, the first sample input has an initial array of 3 elements. The median is position 2 (since (3+1)/2 = 2, so the second element in 1-based). Then, when they add one element, the array has 4 elements. The median is at position (4+1)/2 = 2.5, floored to 2. So the second element in 1-based, which is index 1 in zero-based. So the array after adding 9 becomes [9,10,20,30], sorted. The median is 10, which is correct.

So the approach is to figure out how to add elements so that when the array is sorted, the element at the median position (as per the new array's length) is x.

Let me think about the steps. The initial array is sorted. We can add elements, but they can be placed anywhere in the sorted order. The key is to have x in the median position after adding.

So, the strategy is: after adding k elements, the total array length is m = n + k. The median position is (m+1)//2. For x to be the median, at least (m+1)//2 elements must be <= x, and the rest >= x. But how to ensure that x is exactly at that position.

Alternatively, in the sorted array, the element at position (m+1)//2 - 1 (zero-based) must be x. So, after adding elements, when sorted, the element at that position is x.

So how can we achieve that with the minimal k?

Let's think of the initial array. Let's sort it. Let's see where x would fit in the current array. Then, determine how many elements in the initial array are <=x and >=x.

Wait, perhaps the steps are:

1. Sort the initial array.
2. Find the position where x would be inserted to keep the array sorted. Let's call this pos. This is the count of elements <=x in the array (but maybe not exactly, depending on duplicates).
3. Then, after adding elements, the new array must have enough elements <=x so that x is at the median position.

Wait, but the added elements can be any numbers, including x. So the optimal way is to add as many x's as needed, or elements <=x. Because adding elements <=x can help increase the count of elements <=x, which might be needed.

Wait, the approach should be: the median position depends on the total length m. For x to be the median, there must be at least (m+1)//2 elements in the array (original plus added) that are <=x. Because when sorted, the element at position (m+1)//2 -1 (zero-based) is x. So all elements before that position are <=x, and all after are >=x.

So, the key is to have sufficient elements <=x so that the required position is covered.

Wait, no. Let's think again. Suppose after adding elements, the array is sorted. The median is at position (m+1)//2 -1 (zero-based). So that element must be x. So, all elements before that position must be <=x, and the elements after can be >=x. But how to ensure that x is exactly at that position.

Alternatively, the number of elements <=x in the array (original plus added) must be >= required, and the number of elements >=x must be >= required. Wait, maybe not. Let's think of the required condition.

For x to be the median of the new array (length m), there must be at least (m+1)//2 elements that are <=x, and at least (m - (m+1)//2 +1) elements that are >=x. Because the x is in the middle, but there could be duplicates.

But maybe a better way is to count how many elements in the original array are <=x and how many are >=x. Then, figure out how many elements we need to add to make sure that in the new array, the number of elements <=x is at least the required median position (since the median is the (m+1)//2-th element in 1-based, which is the ( (m+1)//2 ) elements must be <=x (including x itself). Because after sorting, the median is the element in that position. So the required number of elements <=x in the new array is at least (m+1)//2.

Similarly, the required number of elements >=x in the new array is at least (m - ((m+1)//2 -1) ) = (m - (m+1)//2 +1) ) = (m+1)//2 (since m+1//2 is ceiling of m/2). Wait, but maybe the elements >=x must be at least (m - ((m+1)//2 -1)), which is (m - (m+1)//2 +1) = (m - (m+1)//2 +1) = ( (2m - m -1 + 2 ) / 2 ) ? Not sure. Maybe that's not necessary, but the main point is that x must be in the correct position.

But perhaps the key is to find the minimal k such that when m = n + k, the (m+1)//2-th element in the sorted array (original plus added elements) is x.

So how do we model this?

Let me think about the original array sorted. Let's compute the number of elements <=x in the original array. Let's call this cnt_le. The number of elements >=x is cnt_ge. But wait, x may be present in the array, so cnt_le and cnt_ge would include those x's.

But in any case, to have the median be x, after adding k elements (some of which can be x), we need that in the sorted array of length m = n +k, the element at position (m+1)//2 -1 (zero-based) is x.

So the condition is:

In the sorted array, the ( (m+1)//2 ) elements from the start must include enough elements <=x, and the x must be in the correct position.

Wait, perhaps the approach is to find the minimal k such that after adding elements, the required position ( (m+1)//2 )-th element (1-based) is x.

So for example, let's sort the initial array and see where x would fit.

Let's take the second example. Input is 3 4, array [1,2,3]. Original sorted array is [1,2,3]. Current median is 2. The desired x is 4. So we need to add elements so that when sorted, the median is 4. The sample output is 4. After adding four elements (4,5,5,5), the array is [1,2,3,4,5,5,5], sorted. The length is 7. The median position is (7+1)/2 =4, so the fourth element. The array elements are 1,2,3,4,5,5,5. The fourth element is 4. So the required number of elements to add is 4.

How do we model this?

The initial array has 0 elements <=4 (since 1,2,3 are all <=4, wait wait. Wait, the initial array is [1,2,3]. So all elements are <=4. So cnt_le is 3. cnt_ge is 0 (since none are >=4 except 3 is 3 <4? Wait, no. The initial array elements are 1,2,3. So x is 4. So all elements are <=4. So in the original array, cnt_le is 3. cnt_ge is 0 (since 3 is less than 4).

But how do we reach the required condition? We need to add elements such that the median is 4. So the new array's median position must have 4.

In the sample, after adding 4 elements (4,5,5,5), the array is [1,2,3,4,5,5,5], sorted. The median is the 4th element (1-based), which is 4. So the number of elements <=4 in this array is 4 (1,2,3,4). The required position is 4th element. So the number of elements <=4 in the array is exactly equal to the position. Hmm.

So perhaps the condition is: the number of elements in the original array that are <=x, plus the number of added elements that are <=x, must be >= required position ( (m+1)//2 ), and the number of elements >=x (original plus added) must be >= (m - (required position -1) ), which is (m - ( (m+1)//2 -1 )) = (m +1)//2. Because after the median, there are m - (required position) elements.

Wait, maybe not. Let's think differently.

In the new array of length m, the median is at position (m+1)//2. So to have x be the median, the x must be in that position. So after adding elements, when the array is sorted, the x must be placed such that there are at least ( (m+1)//2 ) elements <=x (including the x's), and at least (m - ( (m+1)//2 -1 )) elements >=x (including x's).

But how to model this with the original array and the added elements.

Let me think of the initial array sorted. Let's count how many elements are less than x, equal to x, and greater than x. Let's call:

- a: number of elements <x in the original array.
- b: number of elements ==x in the original array.
- c: number of elements >x in the original array.

So the original array has a + b + c = n.

Now, when we add elements, we can add any numbers between 1 and 1e5. So to maximize the effect of adding elements towards making x the median, we can add elements that are <=x or ==x. Because adding elements <=x can increase the count of elements <=x, which helps in getting the required position.

The strategy is to add as many elements <=x as needed so that the total elements <=x (original plus added) is >= the required position for x to be the median.

Wait, but the added elements can also be x. So adding x's would contribute to both the <=x and >=x counts. Because x is equal to x.

So the problem is: what's the minimal number of elements to add (k) such that for some m = n +k, the median position ( (m+1)//2 )-th element is x.

Alternatively, after adding k elements, the array has m = n +k elements. The median is the ( (m+1)//2 )-th element. We need to choose k elements such that when sorted, this position is x.

Let's think of how to model this.

Let's sort the initial array. Then, for each possible k (starting from 0 upwards), check whether it's possible to have x as the median. The minimal k is the answer.

But trying all possible k's could be time-consuming. But perhaps we can model this mathematically.

The key observation is that after adding k elements, the median position is ( (n +k +1) // 2 ). So for x to be the median, in the combined sorted array (original + added elements), the element at this position must be x.

The added elements can be chosen optimally. So how to find the minimal k such that when you add some elements (possibly including x), the x is in the required position.

Let's think of the original array sorted. Let's find the position where x would be inserted to keep the array sorted. Then, the elements to the left are <=x, and the right are >x.

Wait, but there could be elements equal to x in the array. So the original array's sorted list may have some elements equal to x. Let's find the first occurrence of x and the last occurrence.

Alternatively, after sorting the initial array, let's find the number of elements less than x (a), equal to x (b), and greater than x (c). So a = number of elements <x, b = number of elements ==x, c = number of elements >x.

So a + b + c = n.

Now, when we add elements, they can be any values between 1 and 1e5. The optimal way to add elements is to add elements that are <=x (to increase a +b + added elements) or exactly x (which increases b). Because adding elements larger than x would not help in making x the median; they would only add to the right side. But perhaps sometimes you need to add larger elements. Wait, but in the problem statement, the required median is x. So to have x in the required position, the elements to the left of the median position must be <=x, and the elements to the right can be >=x. So adding elements larger than x can be added to the end of the array, but that would increase the length, possibly requiring more elements <=x.

So the optimal approach is to add as many x's as possible, or elements <=x, because that helps in increasing the count of elements <=x.

Wait, but adding elements <=x can increase the count of elements <=x. So for example, adding elements that are smaller than x would increase a, but that's perhaps not necessary. Because the median is x, which is in the array after adding. So the elements before the median position can be a mix of elements <=x, but the x must be in the correct spot.

Alternatively, perhaps the minimal k is determined by ensuring that in the new array, the required position (m+1)//2 is such that the number of elements <=x in the original array plus the elements added that are <=x is >= the required position. And the number of elements >=x in the original array plus the elements added that are >=x is >= m - (required position -1). But since the added elements can be x (which counts as both), perhaps the key is to maximize the overlap.

Hmm, this is getting a bit complicated. Let's think of the steps again.

The minimal k is the smallest integer such that when we add k elements (any combination of numbers between 1 and 1e5), the median of the resulting array (n +k elements) is x.

Let's think of how the median position depends on the total length m. For each possible m (n +k), we can compute the required position ( (m +1)//2 ). Then, check whether in the original array plus added elements, x can be placed at that position.

But how?

Let's think of the sorted array (original + added elements). Let's say the added elements are all x. Then, when we sort the array, all the added x's would be merged with the existing x's. So the sorted array will have a block of x's. The median position must be within this block.

So the approach could be:

1. Sort the original array and find the positions of elements <=x and >=x.

2. For each possible m (from n upwards), compute the required position ( (m+1)//2 ). Then, check if the original array's elements can allow x to be at that position when adding some elements.

3. The minimal k is m -n where m is the minimal possible.

But trying all possible m's might be feasible, given that n can be up to 500. Wait, but m can be up to n + k, and k can be up to some large number. How do we find the minimal k?

Alternatively, perhaps we can model the problem as follows.

The required position in the sorted array is (m +1)//2. Let's call this pos = (m +1)//2.

We need to have at least pos elements in the original array (a +b) plus the added elements that are <=x. Because the added elements can be <=x, which would contribute to the count. Similarly, the remaining elements (m - pos) can be >=x (including the added elements that are >=x).

Wait, but the added elements can be any combination. So the minimal k is the minimal number such that:

After adding k elements, the total elements <=x (original a +b plus any elements added that are <=x) >= pos.

And the total elements >=x (original b +c plus any elements added that are >=x) >= (m - (pos -1)).

But since the added elements can be chosen optimally, the best way is to add as many elements <=x as possible (if needed) or elements >=x as needed, but perhaps the minimal k comes from adding elements <=x and/or x itself.

Alternatively, since adding x's is allowed, which count towards both <=x and >=x, perhaps the optimal way is to add x's.

Because adding x's increases both the count of elements <=x and elements >=x.

So the steps are:

For the original array:

Sort and compute a, b, c where:

a is the number of elements <x

b is the number of elements ==x

c is the number of elements >x

Then, when we add k elements (all x's), the new counts are a, b +k, c.

Now, the total elements is m = n +k. The required pos is (m+1)//2.

In the new array (original + added x's, sorted), the x's are in the middle.

So the array after adding x's would be:

[ elements <x ] + [x's (original + added) ] + [ elements >x ]

Now, the position of the median (pos) must be within the x's block.

So the conditions are:

The start of the x's block is a elements (all elements <x) and the end of the x's block is a + b +k elements (since all x's are here).

So for the median position (pos) to be within the x's block, the following must hold:

a < pos <= a + b +k

But since the added elements are x's, which are in the x's block, the x's block starts at a and ends at a + b +k.

So the median must be in this block.

So the condition for x to be the median is:

pos must be in (a, a + b +k].

But pos is (m+1)/2 = (n +k +1)/2.

So combining these:

We need a < (n +k +1)/2 <= a +b +k.

But since k is the number of added elements (all x's), let's model this.

We can rearrange the inequality:

a < (n +k +1)/2 

and 

(n +k +1)/2 <= a +b +k 

But (n +k +1)/2 must be an integer if m is even? Wait, no. m is n +k. So m can be even or odd. The pos is (m+1)//2, which is integer.

So (n +k +1) must be divided by 2 and floored. Wait, (m+1) is (n +k +1), and divided by 2, then floor.

Wait, no. For example, if m is 4, (4+1)/2 is 2.5, floor to 2. So pos is 2 (1-based) which is the second element. So in zero-based index, it's 1.

Wait, the pos is (m+1)//2 in 1-based. So in code, pos = (m +1) // 2.

So for m = 4, (4+1)//2 = 2, which is the second position in 1-based. For m=5, (5+1)//2 =3.

So, the condition is:

pos = (n +k +1) // 2

We need to have:

a < pos <= a + b +k 

Because the x's block starts at a (since all elements before are <x) and ends at a + b +k (since all elements after are >x).

Wait, no. The elements before the x's block are a (elements <x), then the x's block (b +k elements), then c elements (elements >x).

So the x's block starts at index a (0-based) and ends at a + b +k -1 (since there are b +k elements). Wait, the count is a (elements <x) + (b +k) elements x's, then c elements >x.

So the x's block is from position a to a + b +k -1 (0-based). So the median position (pos_0 = pos -1) must be within [a, a +b +k -1], where pos is (n +k +1)//2.

So the condition is:

a <= (pos -1) <= a +b +k -1

Which simplifies to:

a <= ( (n +k +1)//2 -1 ) <= a +b +k -1

Simplify the left side:

(n +k +1)//2 -1 >= a 

=> (n +k +1 -2 +1) //2 >= a ?

Wait, perhaps better to substitute.

pos = (n +k +1) // 2

pos_0 = pos -1

So:

pos_0 >= a 

and pos_0 <= a +b +k -1

So:

(n +k +1)//2 -1 >= a 

and 

(n +k +1)//2 -1 <= a +b +k -1 

These are two inequalities that must hold.

We can simplify these.

First inequality:

(n +k +1) //2 -1 >= a 

=> (n +k +1) //2 >= a +1 

Second inequality:

(n +k +1)//2 -1 <= a +b +k -1 

=> (n +k +1) //2 <= a +b +k 

So combining:

a +1 <= (n +k +1)//2 <= a +b +k 

We need to find the minimal k >=0 such that these inequalities hold.

Now, the question is to find the minimal k where these two inequalities are satisfied.

The idea is that adding k elements (all x's) can be the optimal approach, as adding x's contributes to both the count of elements <=x and >=x. So trying to model this as adding x's is the best way.

But perhaps there are cases where adding elements <x would help, but in those cases, adding x's would also help. For example, if adding elements <x increases the required a, but perhaps adding x's allows a lower k.

But to find the minimal k, perhaps adding x's is the optimal way. Because adding elements <x would require adding more elements to reach the same effect. For example, adding an element <x increases a by 1 (the count of elements <=x increases by 1). Adding x increases both the count of elements <=x and >=x by 1. So adding x's can achieve the desired condition with fewer elements.

Therefore, the minimal k is achieved by adding x's. So the problem reduces to finding the minimal k where the two inequalities hold when we add k x's.

So, given that the added elements are all x's, compute the minimal k.

So the problem becomes: find the minimal k such that:

a +1 <= (n +k +1) //2 <= a +b +k 

So how can we model this?

Let's try to model this as:

We need to find the smallest k >=0 such that:

left = (n +k +1) //2 

left must be >= a +1 

and 

left <= a +b +k 

So we can model this for k starting from 0 upwards until the conditions are met.

But with n up to 500, this is feasible.

Alternatively, we can find k using mathematical expressions.

Let's consider the first inequality:

(n +k +1) //2 >= a +1 

Let's denote m = n +k 

Then, (m +1) //2 >= a +1 

=> (m +1) >= 2*(a +1) 

But since (m +1)//2 is the floor division, (m +1) must be >= 2*(a+1) -1 +1 ?

Wait, perhaps to think in terms of inequalities:

For (m +1)//2 >= t, where t is a +1.

We can write:

(m +1) //2 >= t 

Which implies that:

m +1 >= 2t 

Because if m +1 is even, then (m+1)/2 >= t → m+1 >= 2t.

If m +1 is odd, then (m+1)//2 = (m)/2.5 rounded down. For example, m+1 =5 → (5)//2 =2. So m+1 >= 2t → if m+1 is even or odd, the floor division is >=t when m+1 >= 2t.

Wait, no. Let me think.

If m+1 >= 2t → (m+1)/2 >= t → floor((m+1)/2) >=t.

But if m+1 < 2t, then floor((m+1)/2) <t.

So the first inequality can be rewritten as:

m +1 >= 2*(a+1) 

=> since m = n +k:

n +k +1 >= 2*(a+1) 

=> k >= 2*(a+1) -n -1 

Which simplifies to:

k >= 2a +2 -n -1 

= 2a +1 -n 

But k must be >=0, so the minimal k for the first inequality is max(0, 2a +1 -n).

But this is only for the first inequality. The second inequality must also be satisfied.

So for the first part, k must be >= (2a +1 -n). Let's call this k_min1.

Now, the second inequality:

(n +k +1) //2 <= a +b +k 

But (n +k +1)//2 is the same as (m+1)//2, where m =n +k.

So:

(m+1)//2 <= a +b +k 

But since m =n +k, substitute:

(m+1)//2 <= (a +b) + (m -n)

Because k = m -n.

So:

(m+1)//2 <= (a +b) + m -n 

Rearranged:

(m+1)//2 -m +n <= a +b 

Let's compute (m+1)/2 -m:

= (m+1 -2m)/2 

= (-m +1)/2 

So (m+1)//2 -m = floor( (m+1)/2 ) -m 

Which for even m: m is even, m+1 is odd. (m+1)/2 = (m/2) +0.5 → floor is m/2. So floor(...) -m = m/2 -m = -m/2.

For example, m=4 → (5/2) floor is 2. 2-4 =-2.

For m=5 → (6/2) is 3. 3-5 =-2.

So (m+1)//2 -m = - floor(m/2).

So the left side of the second inequality becomes:

- floor(m/2) +n <= a +b 

=> n - floor(m/2) <= a +b 

But a +b is the count of elements <=x in the original array. Because a is elements <x, b is elements =x.

So a +b is the number of elements <=x.

So the inequality can be rewritten as:

n - floor(m/2) <= a_plus_b 

=> floor(m/2) >= n - a_plus_b 

But a_plus_b = a +b.

But n - a_plus_b = (a +b +c) - (a +b) ) = c.

So floor(m/2) >= c 

Because m =n +k.

So the second inequality is equivalent to floor( (n +k)/2 ) >= c 

So:

(n +k) // 2 >= c 

This is the second condition.

So combining both inequalities:

k >= 2a +1 -n 

and 

(n +k) //2 >= c 

So the problem reduces to finding the minimal k >= max(0, 2a +1 -n) such that (n +k) //2 >= c.

Wait, but these two conditions are necessary and sufficient?

Because when adding k x's, the two conditions derived from the two original inequalities.

So the minimal k is the smallest k >= max(0, 2a +1 -n) such that (n +k) // 2 >= c.

So how to compute this.

First, compute a, which is the number of elements in the original array less than x.

Compute c, the number of elements greater than x.

Compute the required k_min1 = max(0, 2a +1 -n)

Then, we need to find the minimal k >=k_min1 such that (n +k) //2 >=c.

So the steps are:

1. Sort the array and compute a, b, c.

2. Compute k_min1 = max(0, 2a +1 -n)

3. Find the minimal k >=k_min1 such that (n +k) //2 >= c.

The minimal such k is the answer.

But how?

Let's model it.

We need to find the smallest k >=k_min1 where (n +k) //2 >= c.

Let's denote t = (n +k) //2 >=c.

We can solve for k:

(n +k) //2 >=c → n +k >= 2c → k >= 2c -n 

But wait, (n +k) //2 >=c implies that n +k >= 2c → k >= 2c -n.

But when n +k is even, (n +k) //2 = (n +k)/2 ≥c → n +k ≥2c →k ≥2c -n.

When n +k is odd, (n +k)//2 = (n +k -1)/2 ≥c → n +k -1 ≥2c → n +k ≥2c +1 → k ≥ 2c +1 -n.

So the minimal k for this condition is:

k_min2 = max( 2c -n, 0 )

But wait, not exactly. Because if 2c -n is negative, then k can be zero. So k_min2 = max(0, 2c -n) if (n +k) is even. But since k must be >=k_min1, and also >=k_min2.

Wait, perhaps the minimal k is the maximum of k_min1 and k_min2, where k_min2 is 2c -n if 2c -n is even or odd?

Wait, perhaps this approach is incorrect. Let's think of it differently.

We need to find the minimal k >=k_min1 such that (n +k) >=2c.

Because:

If (n +k) >=2c → then (n +k) //2 >=c.

But for example, if (n +k) =2c-1 → (2c-1)//2 = c-1 <c. So that's not sufficient. So the condition is (n +k) >= 2c.

So the second condition requires k >= 2c -n.

But since k can't be negative, we have k_min2 = max(0, 2c -n).

So the minimal k that satisfies both conditions is the maximum of k_min1 and k_min2.

But wait, perhaps not. Let's see.

If k_min1 is 5 and k_min2 is 3, then the maximum is 5. So k=5.

But what if k=5 satisfies both conditions.

But maybe there exists a k between 3 and 5 that also satisfies (n +k) >=2c.

For example, if 3 >=k_min1 (3 >=5? No). So perhaps not. So the minimal k is the maximum of k_min1 and k_min2).

But let's test this with the sample inputs.

Sample Input 1:

3 10

10 20 30 → sorted [10,20,30]

a is the number of elements <10 → 0.

b is elements ==10 →1.

c is elements >10 → 2 (20,30).

k_min1 = max(0, 2*0 +1 -3) → max(0, -2) →0.

k_min2 = max(0, 2*2 -3) →max(0,1) →1.

So the required k is max(0,1) →1. Which matches the sample output.

Sample Input 2:

3 4

1,2,3 → sorted. a is elements <4 →3. b=0. c=0.

k_min1 = max(0, 2*3 +1 -3) →max(0, 6+1-3=4) →4.

k_min2 = max(0, 2*0 -3) →0.

So required k is 4. Which matches the sample.

Another example: let's take the second sample. Original array is [1,2,3]. x is 4. a=3, b=0, c=0.

k_min1 is 2*3+1-3=4. So k>=4.

k_min2 is 2*0-3 = -3 →max(0,-3) →0.

So k must be >=4. Now check (3+4) //2 =3.5 →3.5 floored to 3 >=0 (c is 0). So condition is satisfied. So k=4 is the answer.

So this approach works.

Another test case: suppose original array is [5], x=5.

a=0, b=1, c=0.

k_min1 = 2*0 +1 -1=0. k_min2=2*0-1= -1 →0. So k must be >=0. Now, (1 +0) //2=0 >=0 → yes. So k=0. Which is correct, as the median is 5.

Another case: array [3,1,4,1,5], x=3. sorted is [1,1,3,4,5]. a=2 (elements <3), b=1 (element 3), c=2 (4,5).

n=5.

k_min1= 2*2 +1 -5 =5-5=0.

k_min2= 2*2 -5=4-5=-1 →0.

So required k is 0. Check the conditions:

m=5+0=5. pos = (5+1)/2=3 →3rd element in 1-based (index 2 in zero-based). The array is [1,1,3,4,5]. The median is 3. So correct.

Another case: array [5,5,5], x=5. a=0, b=3, c=0.

k_min1=0, k_min2=0. So k=0. Which is correct.

Another case: array [5,5,6,7,8], x=5. a=0, b=2, c=3.

k_min1=2*0+1-5= -4 →0.

k_min2=2*3-5=6-5=1. So required k is max(0,1)=1.

So k=1. m=5+1=6. pos=(6+1)//2=3.5 →3. So the median is the 3rd element in 1-based (zero-based index 2). The array after adding one 5 would be [5,5,5,6,7,8]. Sorted. The third element is 5. So correct.

So the approach seems to work.

Thus, the solution is to compute a (number of elements <x), c (number of elements >x), compute k_min1 = max(0, 2a+1 -n), k_min2 = max(0, 2c -n). Then the answer is max(k_min1, k_min2).

Wait, but in the first sample, the k_min2 was 1, which is correct. But according to the formula k_min2 = max(0, 2c -n) → c was 2. 2*2 -3=4-3=1. So yes.

But let's see. The formula says that k must be >= max(k_min1, k_min2). So the minimal k is the maximum of these two values.

So the steps to solve the problem are:

1. Sort the array and count a (elements <x), b (elements ==x), c (elements >x).

2. Compute k_min1 = max(0, 2a +1 -n).

3. Compute k_min2 = max(0, 2c -n).

4. The answer is the maximum of k_min1 and k_min2.

But wait, what if k_min1 and k_min2 are both zero? For example, when the array already has the correct median.

But in that case, the answer is zero.

Yes.

Another example: array is [10,20,30], x=20. a=1, c=1. n=3.

k_min1=2*1+1-3= 3-3=0.

k_min2=2*1-3= -1 →0. So answer is 0. Which is correct. The median is 20.

So the formula works.

So the solution is to compute a and c, then calculate k_min1 and k_min2 as described, then output their maximum.

Thus, the code can be written as follows:

Read n and x.

Read the array.

Sort the array.

count a = number of elements <x.

count c = number of elements >x.

k1 = max(0, 2*a +1 -n)

k2 = max(0, 2*c -n)

ans = max(k1, k2)

print(ans)

Wait, but wait. Let's test another case where the required k is determined by both conditions.

For example:

Original array is [1,3], x=3. sorted array [1,3].

a=1, c=0.

n=2.

k_min1 = 2*1 +1 -2 =3-2=1.

k_min2 = 2*0 -2 = -2 →0.

max is 1.

So k=1. m=2+1=3. pos is (3+1)/2=2. The array after adding 3 is [1,3,3]. sorted. median is 3. So yes. So answer is 1.

But what if original array is [1,3], x=3. Then adding 1 element (3). So the sorted array is [1,3,3]. The median is 3.

Yes.

Another example:

Original array [2,2], x=2. a=0, c=0.

k_min1=2*0+1-2= -1 →0.

k_min2=0.

so answer is 0. Which is correct.

Another example:

array [1,2,3,4,5], x=3. a=2 (1,2), c=2 (4,5). n=5.

k_min1= 2*2+1-5=5-5=0.

k_min2= 2*2-5=4-5=-1 →0.

so answer is 0. The current array's median is 3. So no elements needed.

Yes.

Thus, this approach works.

So the code is straightforward. We need to count the number of elements less than x and greater than x.

Then compute the two values k_min1 and k_min2, then return their maximum.

This is O(n log n) time due to the sorting step, which is acceptable for n=500.

Now, let's code this.

Read n and x.

Read the array.

Sort the array.

a = number of elements <x.

c = number of elements >x.

k1 = max(0, 2*a +1 -n)

k2 = max(0, 2*c -n)

ans = max(k1, k2)

print(ans)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, x = map(int, input_stream.readline().rstrip("\n").split())
    arr = list(map(int, input_stream.readline().rstrip("\n").split()))
    arr.sort()
    a = sum(1 for num in arr if num < x)
    c = sum(1 for num in arr if num > x)
    k1 = max(0, 2 * a + 1 - n)
    k2 = max(0, 2 * c - n)
    print(max(k1, k2), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 4
1 2 3
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

Second sample:

3 4

array [1,2,3]. a=3 (elements <4: all). c=0.

k1= 2*3 +1 -3=6+1-3=4. k2=0.

ans=4.

Which matches.

Another test case where a=3, c=3, n=5.

k1=2*3 +1 -5=7-5=2.

k2=2*3 -5=6-5=1.

ans=2.

So code is correct.

Thus, the code should work.
</think>

```python
n, x = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
a = sum(1 for num in arr if num < x)
c = sum(1 for num in arr if num > x)
k1 = max(0, 2 * a + 1 - n)
k2 = max(0, 2 * c - n)
print(max(k1, k2))
```
