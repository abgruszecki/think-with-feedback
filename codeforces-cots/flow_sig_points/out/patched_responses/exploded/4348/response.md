<think>
Okay, I need to solve this programming problem. Let's read the problem carefully and understand what's required.

The problem is about determining how many unordered pairs {x, y} from a list of distinct integers satisfy the condition that Arrayland is completely inside Vectorland. Let's break down what that means.

From the legend:
- Arrayland is the interval between |x| and |y|, including endpoints. So the Arrayland interval is [min(|x|, |y|), max(|x|, |y|)].
- Vectorland is the interval between |x - y| and |x + y|. So Vectorland's interval is [min(|x - y|, |x + y|), max(|x - y|, |x + y|)].

The condition is that Arrayland is completely inside Vectorland. That means the min and max of Arrayland must be within the Vectorland interval. So, the min of Arrayland (which is min(|x|, |y|)) must be >= the min of Vectorland, and the max of Arrayland (max(|x|, |y|)) must be <= the max of Vectorland.

Wait, no. Wait, the Arrayland's interval is [a, b], where a is the minimum of |x| and |y|, and b is the maximum. Vectorland's interval is [c, d], where c is min(|x-y|, |x+y|), d is max(|x-y|, |x+y|). The condition is that [a, b] is completely inside [c, d], including endpoints. So a >= c and b <= d.

So the problem reduces to finding pairs (x, y) where min(|x|, |y|) >= min(|x - y|, |x + y|) and max(|x|, |y|) <= max(|x - y|, |x + y|).

Hmm. Let's try to find a mathematical condition that can be checked efficiently for each pair (x, y) without having to compute all possible pairs (since n can be up to 2e5, which would result in O(n^2) pairs, which is 4e10 operations — way too slow).

So we need a way to compute the number of valid pairs efficiently.

Let's think about the mathematical conditions.

Let’s denote A = min(|x|, |y|), B = max(|x|, |y|).

Vectorland's min is min(|x - y|, |x + y|), and max is max(|x - y|, |x + y|).

The condition is that A >= min(|x-y|, |x+y|) and B <= max(|x-y|, |x+y|).

Wait, but |x + y| and |x - y| can be related in some way. Let's think about what their min and max are.

Let’s compute |x - y| and |x + y|. Let’s assume x and y are two numbers, possibly positive or negative.

But since x and y can be any integers, perhaps it's easier to consider the absolute values and see if there's a way to express the conditions in terms of |x| and |y|.

Wait, let's consider that for any x and y:

|x + y| and |x - y|. The maximum of these two is equal to the sum of |x| and |y|. Because, for example, if x and y have the same sign, then |x + y| = |x| + |y|, and |x - y| is | |x| - |y| |. So the maximum is |x| + |y|. If they have opposite signs, then |x - y| is |x| + |y|, and |x + y| is | |x| - |y| |. So again, the maximum is |x| + |y|.

So max(|x + y|, |x - y|) = |x| + |y|.

Similarly, the minimum of these two is | |x| - |y| |. Because if x and y have the same sign, |x - y| is | |x| - |y| |, and |x + y| is |x| + |y|. So the min is | |x| - |y| |. If they have opposite signs, |x + y| is | |x| - |y| |, and |x - y| is |x| + |y|. So again, the min is | |x| - |y| |.

So, Vectorland's interval is [ | |x| - |y| | , |x| + |y| ].

So the condition that Arrayland is inside Vectorland is:

min(|x|, |y|) >= | |x| - |y| | 

and 

max(|x|, |y|) <= |x| + |y|.

But wait, the second condition is always true. Because max(|x|, |y|) is <= |x| + |y|, since the other term is non-negative. So the second condition (B <= max(...)) is automatically satisfied.

So the only condition that needs to be checked is whether the minimum of |x| and |y| is >= the minimum of |x-y| and |x+y|, which as we established is | |x| - |y| |.

But the min of |x| and |y| is equal to | |x| - |y| | when |x| and |y| are such that one is at least twice the other. Wait, perhaps not. Let's think.

Wait, let's denote a = |x| and b = |y|. Let's assume a <= b. Then the Arrayland's interval is [a, b]. The Vectorland's interval is [b - a, a + b]. The condition is that a >= (b - a) (since the min of |x| and |y| is a, and the min of |x-y| and |x+y| is |a - b|, which is b - a if a <= b). Wait, no. If a and b are absolute values, then |x - y| could be | |x| - |y| | if x and y have the same sign, or | |x| + |y| | if opposite. But earlier analysis showed that the min of |x + y| and |x - y| is |a - b| when a and b are the absolute values. So, in terms of a and b, the Vectorland's min is |a - b| and max is a + b.

So the condition that Arrayland is inside Vectorland is:

a >= |a - b| 

and 

b <= a + b (which is always true). So the second condition is always satisfied, so we only need to check the first condition.

Wait, since a and b are positive (as they are absolute values), then a >= |a - b|. Let's see when this holds.

If a >= b, then |a - b| = a - b. Then the condition is a >= a - b → 0 >= -b → which is always true. But wait, in this case, a >= b implies that in Arrayland, a is the maximum (since a and b are |x| and |y|). Wait, no. Wait, a is |x|, b is |y|. If a >= b, then the Arrayland is [b, a]. Wait, no. Wait, Arrayland is the interval between |x| and |y|. So when |x| = a and |y| = b, and a >= b, the Arrayland is [b, a]. Wait no: Arrayland is [min(|x|, |y|), max(|x|, |y|)]. So if a is |x| and b is |y|, then if a >= b, min is b, max is a. So Arrayland is [b, a].

But Vectorland's interval is [a - b (since a >= b, |a - b| = a - b), a + b]. So the condition for Arrayland's min (which is b) to be >= Vectorland's min (a - b) is:

b >= a - b → 2b >= a → a <= 2b.

But in this case, a >= b, so the condition is a >= b and a <= 2b. So when a is between b and 2b.

Wait, let me re-express the condition for a and b where a >= b. So the condition is:

b >= (a - b) → a <= 2b.

But since a >= b, the possible a is in [b, 2b].

Alternatively, if a <= b, then a is the min of |x| and |y|, and b is the max. Then the Vectorland's min is |a - b| = b - a. So the condition is a >= (b - a) → 2a >= b → b <= 2a.

So combining these two cases:

If a and b are the absolute values of x and y, then the condition for Arrayland to be inside Vectorland is:

max(a, b) <= 2 * min(a, b).

Because:

- If a >= b: the condition is a <= 2b.
- If b >= a: the condition is b <= 2a.

So in both cases, the maximum of a and b must be <= twice the minimum of a and b.

So the problem reduces to counting the number of unordered pairs {x, y} where max(|x|, |y|) <= 2 * min(|x|, |y|).

That's a huge simplification! Because now, for each pair (x, y), we can compute the absolute values a = |x|, b = |y|, then check if max(a, b) <= 2 * min(a, b).

So the problem is to count the number of unordered pairs of distinct elements in the array where the maximum of their absolute values is at most twice the minimum.

So how can we compute this efficiently?

The steps are:

1. Compute the absolute values of all elements in the array. Let's call this array S.

2. Sort S in ascending order. Then, for each element s in S, we need to find the maximum index j where s_j <= 2 * s. The number of elements between the current index and j (inclusive) minus one (since we can't pair with ourselves) gives the count of elements that can form a valid pair with s.

But since the array is sorted, for each element s at position i, all elements from i+1 up to j can be paired with s, provided that s_j <= 2 * s.

Wait, but since the array is sorted, for each element s_i, the maximum s_j that can be paired with s_i is s_j <= 2*s_i. Because s_i is sorted, and s_j >= s_i (since the array is sorted in ascending order). So for each s_i, find the largest j where s_j <= 2*s_i. The number of elements between i+1 and j (inclusive) is the number of valid pairs for s_i.

But we have to make sure that for each s_i, we count all elements s_j >= s_i (since the array is sorted) and s_j <= 2*s_i.

So the approach is:

- Sort the absolute values array in non-decreasing order.

- For each index i (0-based), find the maximum index j where S[j] <= 2 * S[i]. Since S is sorted, we can perform a binary search for 2*S[i] in S[i+1 ... n-1], but wait, no: since the array is sorted, for S[i], all elements S[k] where k >= i, but S[k] can be as large as 2*S[i]. Wait, but in the sorted array, S is in non-decreasing order. So for S[i], all elements S[j] >= S[i], and we need to find the maximum j where S[j] <= 2*S[i]. But since S is sorted, once S[j] exceeds 2*S[i], we can stop. So for each i, we can binary search the upper bound in the entire array (since the array is sorted) and find the rightmost j where S[j] <= 2*S[i]. Then, the number of elements between i+1 and j (inclusive) is (j - i). Because for S[i], all elements from i+1 up to j (since the elements are sorted, and >= S[i], but <= 2*S[i]). Each of these elements forms a valid pair with S[i], since max(S[i], S[j]) = S[j] (since j >= i) and S[j] <= 2*S[i], which is the condition.

So the algorithm would be:

Sort S in non-decreasing order.

Initialize count = 0.

For each i from 0 to n-1:

   target = 2 * S[i]

   j = upper_bound of target in S, starting from i (since elements before i are smaller than S[i], so j is the first index where S[j] > target)

   j -= 1 (so j is the last index where S[j] <= target)

   if j > i:

      count += (j - i)

So the total number of valid pairs is the sum over all i of (j - i), where j is the largest index where S[j] <= 2*S[i].

Wait, but the elements in the array are absolute values. Also, since the original array elements are distinct, but their absolute values may not be. For example, if the original array has 3 and -3, their absolute values are the same. But the problem statement says that the input elements are pairwise distinct. So in the input, a_i are distinct. So when we take absolute values, some may become duplicates. However, the problem requires that the pair {x, y} is formed by two different elements. So even if two elements x and y have the same absolute value (like 3 and -3), they are considered distinct and can form a pair. But in the sorted array of absolute values, duplicates are possible. However, when we count pairs, even if two elements in S are equal (same absolute value), their original elements are different, so each pair is allowed.

So the approach of counting in the sorted S array is correct, even if there are duplicates in S.

Wait, but when we compute the absolute values, the original elements may have same absolute value but be different. For example, if the input has -2 and 2. Their absolute values are the same (2). So when sorted, S would have 2 and 2. When considering pairs (i=0 and j=1), S[i] = 2, S[j] = 2. The condition is max(2,2) <= 2*2 (yes), so this pair is counted. But in the original elements, these two form a valid pair if and only if their absolute values satisfy the condition. So yes, the approach works.

But since the original array elements are distinct, even if two have the same absolute value, the pair is allowed. So the approach of counting pairs in the sorted S array (after absolute values) is correct.

So the steps to compute the answer are:

1. Take all elements in the input array, compute their absolute values, sort them in non-decreasing order.

2. For each element in the sorted array, at position i, find the maximum j where S[j] <= 2 * S[i]. Since the array is sorted, this can be done via binary search (using bisect module in Python). The number of valid pairs for this i is (j - i), but only if j >= i+1. Otherwise, zero.

3. Sum all these counts to get the total number of valid pairs.

Now, considering the constraints:

- n can be up to 2e5. Sorting O(n log n) is acceptable.

- For each element, a binary search is O(log n), so overall O(n log n) time.

This should be efficient enough.

Let me test this approach with the examples.

First example:

Input: 3 elements [2,5,-3]. The absolute values are [2,5,3]. Sorted S is [2,3,5].

For each i:

i=0, S[i]=2. 2*2=4. Find the largest j where S[j] <=4. S is [2,3,5]. The elements after i=0 are 3 and 5. 3 <=4, 5>4. So j=1. So count += (1-0) =1. This is the pair (2,3). But in the original array, the pairs are {2,5}, {2,-3}, {5,-3}.

Wait, but in the sorted S array, for i=0 (value 2), j=1 (value 3) → valid pairs are (2,3). But in the original array, this corresponds to pairs where one is 2, the other is 3 (but 3 is the absolute value of -3). So {2, -3} is a pair.

But according to the first sample's explanation, the valid pairs are {5,-3} and {2,-3}. Let's see:

In the sorted S array:

i=0 (2):

We look for elements >=2 (i=0) and <=4. The elements are 2 (current i), 3 (i=1), 5 (i=2). The elements after i are 3 and 5. 3 <=4 → yes. 5>4 → no. So j=1. So the count is 1 (elements at i+1 to j). So this counts the pair (2,3) → which corresponds to (2, -3) in the original array. Which is valid.

i=1 (3):

2*3=6. Looking for elements >=3 (i=1) and <=6. The elements are 3,5. 5<=6 → j=2. So count += (2-1)=1. The pair is (3,5) → in the original array, 5 and -3 (since 3 is | -3 |, 5 is |5|). The pair (5, -3) is valid.

i=2 (5):

2*5=10. But elements after i are none. So j=2. So no pairs added.

Total count is 1+1=2 → matches the first example.

Second example:

Input: 3 and 6. Absolute values are [3,6]. Sorted S is [3,6].

i=0 (3):

2*3=6. Find j where S[j] <=6. The elements after i=0 is 6. 6<=6 → j=1. count +=1-0=1 → pair (3,6).

i=1 (6):

No elements after, so nothing added.

Total count 1, which matches the second example.

So the approach works.

Now, how to implement this in Python efficiently.

In Python, we can use the bisect module. For each element in the sorted S array, we can compute the upper bound (bisect_right) of 2*S[i] in the array. Then, the rightmost index is the upper bound minus 1. But since the array is sorted, and we want to find the maximum j where S[j] <= 2*S[i], we can use bisect_right for 2*S[i], then subtract 1.

Wait, bisect.bisect_right returns the insertion point, which is the first element > target. So, for target = 2*S[i], bisect_right returns the first index where S[j] > 2*S[i]. So the maximum j where S[j] <= 2*S[i] is (bisect_right -1).

But for each i, we need to look for elements starting from i+1, because the pair must consist of two distinct elements. Wait no: the pair can be i and j >= i, but since the array is sorted, for each i, j can be from i+1 to (bisect_right-1).

Wait, but in the code:

For each i in 0..n-1:

   the elements to consider are j where j > i (since unordered pairs, and each pair is counted once). So, for each i, the valid j are in [i+1, ... , j_max], where j_max is the largest index where S[j] <= 2*S[i].

So the code would be:

sorted_abs = sorted(abs(a) for a in array)

count = 0

for i in range(len(sorted_abs)):

    target = 2 * sorted_abs[i]

    j = bisect.bisect_right(sorted_abs, target, i+1, len(sorted_abs)) 

    # because j starts from i+1, but wait, the elements from i onwards are considered. Wait, no: in the sorted array, the elements at i and beyond are >= sorted_abs[i]. So to find j where j > i (since the pair is {i's element, j's element}, j must be after i to avoid duplicates. Wait, no: the array is sorted, and for each i, we are considering j >= i, but the pairs are unordered. So if we process all i and j >= i, but count each pair once, then in the code, for each i, j can start from i+1 (since j=i would be same element, but the problem requires pairs of different elements). Wait, no: the elements in the original array are distinct, but after taking absolute values, there might be duplicates. However, in the problem statement, the pairs are formed by two different elements, but their absolute values can be the same.

Wait, but in the code, the sorted_abs array is the absolute values of the input elements, which are distinct (since input elements are pairwise distinct). However, the absolute values could be the same. For example, input elements 3 and -3 would have absolute values 3 and 3. So, in the sorted_abs array, they are considered as two elements. So when i is the index of the first 3, and j is the index of the second 3, the pair is allowed as it's two distinct elements in the original array.

So, in the code, for each i, the j can be any index >= i+1 where S[j] <= 2*S[i].

Wait, but in the code, when considering i, the j starts from i+1. Because the pairs are unordered. So for each i, we look for j in i+1 to len(sorted_abs)-1, inclusive. So in the code, when we compute j_max, it's the largest index in the entire array where S[j] <= 2*S[i]. Then, the number of elements between i+1 and j_max is (j_max - i) if j_max >= i+1. Else, 0.

Wait, no. For example, if j_max is i, then there are no elements after i. So the code must ensure that j_max is >= i+1.

So the code would be:

sorted_abs = sorted( abs(a) for a in a_list )

count = 0

n = len(sorted_abs)

for i in range(n):

    a = sorted_abs[i]

    # find the largest j where sorted_abs[j] <= 2*a

    # use bisect_right to find the insertion point of (2*a), then subtract 1

    j_max = bisect.bisect_right(sorted_abs, 2*a) - 1

    # Now, j_max is the largest index where sorted_abs[j_max] <= 2*a

    # but j_max must be >= i+1, because j must be > i (since pairs are unordered and we process each once)

    if j_max > i:

        count += (j_max - i)

    else:

        # j_max <= i → no pairs

        pass

Wait, but in the code, the bisect_right is over the entire array, not starting from i+1. For example, consider i=0 and j_max=0. But j needs to be >= i+1, so j can't be 0. So the code should instead find the first j >= i+1 where sorted_abs[j] <= 2*a. Wait, no. Because j must be >= i+1. So perhaps the code should first find the first index where j >= i+1 and sorted_abs[j] <= 2*a.

But that's not correct. Because there can be elements after i that are <= 2*a. For example, the elements after i could be i+1, i+2, ..., j_max.

So the code as written (using bisect_right on the entire array, then j_max is the maximum possible j, then if j_max > i, then count += (j_max - i)) would include j=i, which is not allowed. Because j must be >= i+1.

Ah, right. So the code is incorrect as written. Because for j_max, the maximum index where sorted_abs[j] <= 2*a could be >= i, but we need j >= i+1. So the code should subtract i+1 to j_max.

Wait, let's take the example where i=0 and j_max=0. Then j_max - i =0, but j must be >=1. So this would add 0-0=0, which is correct. But if j_max is 1 and i=0, then j_max -i=1, which includes j=1 (i=0, j=1: correct). So the code as written (count += j_max -i) would be wrong, because when j_max is >=i but >=i, but j can be >=i (including j=i). So the code needs to find the number of elements j where j > i (j >=i+1) and sorted_abs[j] <= 2*a.

So how to adjust the code.

We can compute j_max as the largest index where sorted_abs[j] <= 2*a, and then the number of elements between i+1 and j_max (inclusive) is (j_max - i) if j_max >=i+1, else 0.

But how to compute j_max in this scenario.

Alternatively, we can find the first index where j >=i+1 and sorted_abs[j] <= 2*a. But since the array is sorted, perhaps we can use bisect_left or bisect_right on the subarray starting from i+1.

So for each i, the lower bound is i+1. So:

start = i+1

end = n

We can use bisect_right on the entire array, but the j_max is the largest index where sorted_abs[j] <= 2*a. Then, the valid j's are in [i+1, j_max].

So the number of valid elements is max(0, j_max - i) if j_max >= i+1.

Wait, no. Because j_max is the largest index where sorted_abs[j] <= 2*a, regardless of i. So if i+1 > j_max, then there are 0 elements. Otherwise, it's (j_max - (i+1) +1) = j_max -i.

Wait, the number of elements between a and b inclusive is (b -a +1). So between i+1 and j_max, the count is j_max - (i+1) +1 = j_max -i.

Yes. So if j_max >= i+1, the count is j_max -i. If j_max < i+1, 0.

So how to compute j_max correctly.

For example, in the code:

j_max = bisect_right(sorted_abs, 2*a) -1

if j_max >= i+1:

    count += (j_max - i)

else:

    count +=0

But this would be wrong. Because j_max could be >=i+1, but in that case, the count is (j_max - i). Let's test with the first example.

First example: sorted_abs = [2,3,5]

For i=0 (a=2):

j_max = bisect_right([2,3,5],4) -1. The bisect_right of 4 in [2,3,5] is 2 (since 3 <4, 5>4). So j_max=2-1=1. Then check if j_max >=i+1 → 1 >=1 → yes. So count +=1-0=1. Which is correct (i=0, j can be 1 (3)).

For i=1 (a=3):

bisect_right finds 6 in [2,3,5]. The array is [2,3,5], 6 is larger than all elements, bisect_right returns 3. j_max=3-1=2. Check if 2 >=2 (i+1=2). Yes. So count +=2-1=1. Which is correct (i=1, j=2 (5)).

For i=2 (a=5):

bisect_right(10) → returns 3. j_max=2. Check if 2 >=3 → no. So no addition.

Total count 2.

Which is correct.

Another test case: input is 2 and 3. Their absolute values are 2 and 3. sorted_abs is [2,3]. i=0:

bisect_right finds 4 in [2,3], returns 2. j_max=1. j_max >=i+1 (1 >=1 → yes). count +=1-0=1. i=1: no. Total count 1. Correct.

Another example: input is 3 and 6. Absolute values are 3 and 6. sorted_abs is [3,6]. i=0:

bisect_right(6) → in [3,6], the insertion point is 2. j_max=1. j_max >=1 (i+1=1). count +=1-0=1. i=1: no. So total 1. Correct.

Another example: what if the array has elements 4 and 2. Absolute values are 4 and 2. sorted_abs is [2,4]. i=0:

bisect_right(4) → insertion point is 2. j_max=1. Check if j_max >=1 → yes. So count +=1-0=1. So the pair (2,4) is considered. max(4,2)=4, 4 <= 2*2 → 4 <=4 → yes. So valid.

Another example: elements 5, 10. sorted_abs is [5,10]. 5*2=10. bisect_right(10) → returns 2. j_max=1. j_max >=1 (i+1=1) → count +=1-0=1. So valid. Because 10 is equal to 2*5.

Now, the code as written:

for each i in 0..n-1:

    a = sorted_abs[i]

    target = 2*a

    j_max = bisect_right(sorted_abs, target) -1

    if j_max >= i+1:

        count += j_max -i

    else:

        0

This seems correct. Because j_max is the largest index where sorted_abs[j] <= 2a. Then, among j >= i+1, the count is j_max -i.

Yes.

So the code can be implemented in Python using the bisect module.

Now, let's code this.

We can proceed as follows:

Read n, read the list of a_i.

Compute sorted_abs = sorted( abs(x) for x in a_i )

Initialize count to 0.

For each i in range(n):

    a = sorted_abs[i]

    target = 2 * a

    # find j_max using bisect_right

    j = bisect.bisect_right(sorted_abs, target) -1

    if j > i:

        count += (j - i)

Print the count.

This should work.

But wait, in the first example, for i=0, j_max is 1, which is greater than i=0. So adding 1-0=1.

Yes.

But in the code, j_max can be up to n-1. So for i=0, j_max can be n-1. But the code will include all elements from i+1 to j_max.

Yes.

Now, the code must handle all possible cases.

But how about when the same absolute value appears multiple times.

For example, input array: [3, -3, 6]. Absolute values are [3,3,6]. sorted_abs is [3,3,6].

For i=0 (3):

target =6. bisect_right in [3,3,6] for 6 is 3. j_max=3-1=2. j_max=2.

i=0, j_max=2. j_max >=1 (i+1=1). count += 2-0=2. So pairs (3,3) and (3,6). But wait, the elements are 3, -3, 6. The pairs {3,-3}, {3,6}, {-3,6}.

For {3,-3}:

a=3, b=3. max is 3 <= 2*3 → yes. So valid.

For {3,6}: 6 <= 2*3? 6 <=6 → yes. Valid.

For {-3,6}: same as {3,6}.

So the code counts 2 pairs for i=0.

i=1 (3):

target=6. bisect_right is 3. j_max=2. i+1=2. j_max >=2 → yes. j-i = 2-1=1. So count +=1. So pairs (3,6) again. But in the code, for i=1, j_max is 2. So the code would count 1 more. So total count 2+1=3.

But the actual valid pairs are {3,-3}, {3,6}, {-3,6}. So three pairs.

But according to the problem statement, the pairs are unordered and must consist of two different elements. So in this case, all three pairs are valid.

The code's logic would output 3 pairs. Which is correct.

But according to the code:

sorted_abs = [3,3,6]

For i=0:

j_max is 2 (since bisect_right([3,3,6], 6) is 3. j_max=2. 2 >= 1 → yes. count +=2-0=2. So pairs (i=0, j=1) and (i=0, j=2). These correspond to pairs (3,3) and (3,6) in sorted_abs. But the original elements for i=0 and j=1 are 3 and -3. So the pair {3, -3} is valid.

Then, i=1 (3):

j_max is 2. 2 >=2 → yes. count +=2-1=1. So pair (3,6) (i=1 and j=2). Which corresponds to {-3,6}.

i=2 (6):

j_max = bisect_right(12) → j_max=2. 2 >=3 → no. So no addition.

Total count 3.

Which is correct.

So the code handles duplicates correctly.

Thus, the code is correct.

Now, implementing this in Python.

In Python, the bisect module's bisect_right function can be used. So:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    sorted_abs = sorted(abs(x) for x in a)
    count = 0

    for i in range(n):
        target = 2 * sorted_abs[i]
        j = bisect.bisect_right(sorted_abs, target) -1
        if j > i:
            count += (j - i)
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
3 6
""",
            "output": \
"""\
1
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

Second example:

Input:

2

3 6

sorted_abs [3,6]

i=0: target 6. bisect_right returns 2. j=1. count +=1.

i=1: j=1. no.

Output 1.

Another test case with 3, -3, 6:

As discussed, code outputs 3.

Thus, the code is correct.
</think>

```python
import bisect

n = int(input())
a = list(map(int, input().split()))
sorted_abs = sorted(abs(x) for x in a)
count = 0

for i in range(n):
    target = 2 * sorted_abs[i]
    j = bisect.bisect_right(sorted_abs, target) - 1
    if j > i:
        count += (j - i)
print(count)
```
