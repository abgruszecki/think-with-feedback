<think>
Okay, let's try to figure out this problem. The task is to find the k-th pair in the lexicographically sorted list of all possible pairs (ai, aj) from the array. Hmm.

First, I need to understand how the pairs are ordered. Lex order for pairs (p, q) means that (p1, q1) comes before (p2, q2) if p1 < p2, or p1 == p2 and q1 < q2. So the primary key is the first element of the pair, and the secondary is the second.

So the approach here is to first sort the array to handle the ordering. Wait, but the pairs are generated from the original array. But when sorted lex, the first elements determine the order. So maybe if we sort the array first, we can group the first elements and then within each group, handle the second elements.

Let me think. If the original array is sorted, then all possible pairs would be ordered by their first element. But since the pairs are generated from the original array, but we need to sort all possible pairs lexicographically. So the first step is to sort the array in non-decreasing order. Because when you list all possible pairs, the ones with the smallest first elements will come first, then the next, etc. But if the array isn't sorted, then the pairs might be in a different order. So to efficiently find the k-th pair, we need the array to be sorted. Because then the pairs will be grouped by their first element in order.

Wait, but the problem says that all possible pairs are considered, and then sorted. So the initial array's order doesn't matter once we sort all the pairs. So the correct approach would be to first sort the array, and then generate all pairs in such a way that they are ordered lex. So sorting the array first would allow us to process the pairs in order.

Yes. So the first step is to sort the array. Because once the array is sorted, the pairs will be ordered first by their first element (since the array is sorted, the first elements are in non-decreasing order), and for each first element, the pairs will have their second elements in the order of the sorted array as well.

Wait, no. For a fixed first element ai, the second elements are all elements in the array, but sorted in non-decreasing order. Because when the array is sorted, all possible aj for a given ai will be in sorted order. So for each ai in the sorted array, the pairs (ai, a1), (ai, a2), ..., (ai, an) are ordered as a1 <= a2 <= ... <= an. But since the array is sorted, the second elements are in order. So the pairs for a particular ai are (ai, a1), (ai, a2), ..., (ai, an), which are sorted lex in their second elements.

Therefore, once the array is sorted, the entire list of pairs is in lex order. So the k-th pair can be found by first determining how many pairs have a first element less than the current one, and then how many are in the current group.

So here's the plan:

1. Sort the array in non-decreasing order. Let's call this sorted array 'sorted_arr'.

2. Find the first element x in the sorted array such that the number of pairs with first element less than x is less than k, and the number of pairs with first element <= x is >= k. So x is the first element of the k-th pair.

3. Once x is found, compute how many pairs are there before the first occurrence of x. Let's call this 'before'. Then, the remaining k' = k - before will be the position within the x group.

4. Then, find the (k')-th element in the sorted array, which will be the second element of the pair.

Wait, no. Because within the x group, all possible pairs are (x, a_j) where a_j is in the sorted array. So for each x in the sorted array, the group of pairs is all (x, a_j) for each j, and since the array is sorted, these are ordered by a_j. So the entire list of pairs is grouped by x, and within each x group, the a_j's are in order.

But when the array is sorted, the x's themselves are in order. For example, if the sorted array is [1, 3, 5], then the groups are (1, ...), (3, ...), (5, ...). Each group has n elements. So the total number of pairs is n^2.

Wait, but if the array has duplicate elements, like [1, 1, 2], then the sorted array is [1,1,2]. So the groups are (1,1), (1,1), (1,2), (1,1), (1,1), (1,2), (2,1), (2,1), (2,2). Wait, but when sorted, the pairs are generated as all possible combinations. But when we sort the entire list of pairs lex, duplicates are allowed.

But in the problem statement's first example, the array is [3,1,5], sorted as [1,3,5], and the pairs are ordered as per the example. So when the array is sorted, the pairs are in lex order.

Therefore, the first step is to sort the array. Then, the entire list of pairs is the sorted array's elements cross product with themselves, ordered lex. So the sorted array is the key here.

So the problem reduces to: given the sorted array, find the k-th pair in the cross product (all possible pairs) ordered lex.

Now, the question is how to compute the first and second elements of the k-th pair efficiently.

Let's think of the sorted array as A.

Each element in the cross product is (A[i], A[j]) for all i and j.

The lex order is such that (A[i], A[j]) comes before (A[i'], A[j']) if A[i] < A[i'], or A[i] == A[i'] and A[j] < A[j'].

So the pairs are grouped by i. Wait, no. Because for each i, the first element is A[i], and the second elements are all elements in the array. But the pairs are ordered by the first element first, so all pairs where the first element is less than some x will come before those where the first element is x. So the cross product is ordered by the first element in the same order as the sorted array.

Wait, but the sorted array is in non-decreasing order. So A[0] <= A[1] <= ... <= A[n-1]. So the first elements of the pairs are in non-decreasing order. For each first element, all possible second elements are the entire array, sorted in non-decreasing order. Therefore, the entire list of pairs is in lex order.

Wait, no. For example, if the sorted array is [1,3,5], the pairs are ordered as (1,1), (1,3), (1,5), (3,1), (3,3), (3,5), (5,1), (5,3), (5,5). But in the list, the pairs for first element 3 include (3,1), which is lex ordered correctly because 1 <3. Wait, but the array is sorted, so the second elements are all elements in the array, which includes 1,3,5. So when the first element is 3, the second elements are 1,3,5. But in lex order, (3,1) comes before (3,3), which comes before (3,5). So the second elements are ordered in the same order as the array.

But wait, the sorted array is in non-decreasing order, but the second elements are the entire array. So the second elements for a given first element are in the same order as the sorted array. So yes, for the first element x, the second elements are A[0], A[1], ..., A[n-1], which are in non-decreasing order. So all pairs for x are ordered by their second elements in non-decreasing order.

So the entire list of pairs is ordered first by the first element (in the order of the sorted array) and then by the second element (also in the order of the sorted array).

So the k-th pair is the pair (x, y), where x is the element in the sorted array such that the number of pairs with first element less than x is less than k, and the remaining part (after subtracting those counts) is the index within the x group. Then y is the element at position (remaining_k - 1) in the sorted array.

But how do we compute x and the position in the x group?

Let's break it down. The total number of pairs for elements less than x is the number of elements less than x multiplied by n. For example, if there are m elements less than x, then m * n pairs are before all pairs starting with x. Then, the number of elements equal to x is cnt. So each occurrence of x contributes n pairs. Wait, no. Because each element in the array (including duplicates) is considered as the first element. So if the sorted array has elements like [1,1,2], then the first elements are 1,1,2. Each of these contributes 3 pairs. So the count of pairs for elements less than x is the number of elements in the array that are less than x multiplied by n. Then, the elements equal to x are considered next. The first element of the pair can be any of the x's. But when considering the x group, each occurrence of x in the first element contributes n pairs. So the total number of pairs before the x group is (count of elements < x) * n. Then, within the x group, each occurrence of x in the first element contributes n pairs. So the x group has (count of x) * n pairs. So to find the x, we can think in terms of how many groups of elements are there. Wait, but this approach might not work because elements can have duplicates, and the first elements can be grouped into multiple instances of the same value.

Alternatively, perhaps we can model the first elements as all elements in the sorted array. So the pairs are ordered by the first elements as per their order in the sorted array. So for example, if the sorted array is [a, b, c], then the first elements in order are a, a, a (if all elements are a). Wait, no. The sorted array is [a, a, a], then the first elements in the pairs are a, a, a (each one in the first element, leading to 3 * 3 pairs). But when sorted lex, all these pairs are ordered by their second elements.

So for the first step, the first elements are processed in the order they appear in the sorted array. So each occurrence of a value in the sorted array contributes to the first element. So the first element is the i-th element in the sorted array. So the k-th pair's first element is the (i)th element in the sorted array, where i is determined such that the cumulative count up to i-1 elements multiplied by n is less than k, and up to i elements multiplied by n is >=k.

Wait, perhaps that's the right approach. Let's consider the sorted array A. For each element in A, when it's the first element of the pair, there are n possible pairs (since the second element can be any element in the array). So the total number of pairs up to the i-th element (inclusive) in the sorted array is (i+1)*n. So the k-th pair is found by finding the smallest i such that (i+1)*n >=k. Then, the first element is A[i], and the second element is A[(k-1) - (i)*n)] ?

Wait, let me think with an example.

Suppose the sorted array is [1,3,5], n=3. The pairs are ordered as follows:

(1,1), (1,3), (1,5), (3,1), (3,3), (3,5), (5,1), (5,3), (5,5). So each of the 3 elements in the first position contributes 3 pairs. So for i=0 (element 1), the first 3 pairs. For i=1 (element 3), next 3 pairs (positions 4-6). For i=2 (element 5), next 3 pairs (7-9).

If k=4, the first element is the 1st index (3), and the second element is (4-3) =1, so the index is 0 in the array (element 1). So the pair is (3,1), which is correct.

Another example: the first sample input is [2,1], sorted to [1,2]. Then pairs are (1,1), (1,2), (2,1), (2,2). So n=2. For k=4: the first element is at index 1 (element 2), and the second element is (4 - 2*2) = 0? Wait, no. Let's see:

Each element in the sorted array contributes n pairs. So the first element (1) contributes 2 pairs (positions 1-2). The second element (2) contributes 2 pairs (positions 3-4). So for k=4, it's the second element's group (2), and the position within the group is 4 - 2*2 = 0. So the second element is sorted_array[0], which is 1. So the pair is (2,1). Wait but in the first sample input, the output is (2,2). Wait, that's conflicting. What's wrong here?

Wait wait the first sample input is n=2, k=4, array is [2,1]. The sorted array is [1,2]. The pairs when sorted lex are (1,1), (1,2), (2,1), (2,2). The 4th pair is (2,2). So according to this approach, the first element is at index 1 (element 2), and the position within the group is 4 - 2*1 = 2. Because (i+1)*n >=k? Let's recalculate:

For each i (0-based), the cumulative count up to i is (i+1)*n. So for the first element (i=0), cumulative is 2. For i=1, cumulative is 4. So k=4 is exactly the 4th pair. So the group is i=1. The position within the group is k - (i)*n -1 = 4- (1)*2 =2. Wait, but the group size is n. So the position is (k - (sum before)) -1. Because sum before is i elements multiplied by n. Wait, sum before is (i) *n. Because for i=0 (element 0), sum before is 0. For i=1, sum before is 2*1=2 (since i=1, sum before is 0+2=2). So for i=1, the group starts at sum_before +1 =3? Or maybe not.

Wait, let's think in terms of total pairs up to and including the i-th element. For the i-th element in the sorted array, the total pairs up to and including that element is (i+1)*n. So for the first element (i=0), 1*2=2 pairs. For i=1, 2*2=4 pairs. So for k=4, it's the last pair in the second group (element 2). The position within the group is (4 - 0) if we subtract the sum up to i-1. Wait, sum up to i-1 is (i)*n. So for i=1 (element 2), sum up to i-1 (i=0) is 0*2 =0? No. Wait, when i=1 (the second element in the sorted array), the sum up to i-1 (which is i=0) is (0+1)*n =1*2=2. Because for i=0, the cumulative is (i+1)*n =1*2=2. So sum before the group of i=1 is 2. Then, the group of i=1 has 2 pairs. So for k=4, it's the second pair in the group. So the second element is A[1], which is 2. So the pair is (2, 2), which matches the sample.

So the correct approach is:

1. Sort the array.

2. For each element in the sorted array (in order), compute the cumulative number of pairs up to and including that element. The cumulative up to the i-th element (0-based) is (i+1)*n.

3. Find the smallest i such that (i+1)*n >=k. Then, the first element is A[i].

4. The number of pairs before this group is (i)*n. So the position within the group is (k - (i)*n) -1 (since we start from 0).

Wait, the position within the group is (k - (i)*n) -1? Let's see:

For the first sample, i=1. sum_before =1*2=2. k=4. So 4-2 =2. So the position is 2-1=1? Wait, no. Because the group starts at sum_before +1 (sum_before is 2, so the group is positions 3 and 4). For k=4, which is the second element in the group (positions 3 is 3rd, 4 is 4th). The index is 1 (0-based). So the second element is A[1], which is 2.

So the formula is: position_in_group = (k - sum_before) -1.

Yes. Because sum_before is (i)*n. Then, within the group, the first pair is sum_before +1, and the next n pairs. So for k, the index within the group is (k - sum_before -1) (0-based). Wait, let's compute:

sum_before = i *n. Then, the group starts at sum_before +1. So for sum_before=2 (i=1 in first sample), the group is 3 and 4. So for k=4, it's the second pair in the group, which is index 1 (0-based). So (k - sum_before) -1 = (4-2) -1 =1. Correct.

Therefore, the algorithm steps are:

- Sort the array.

- Iterate through the sorted array, for each element A[i], compute the cumulative pairs up to (i+1)*n.

- Find the smallest i where (i+1)*n >=k.

- The first element is A[i].

- Compute sum_before = i *n.

- position_in_group = k - sum_before -1 (since the first element in the group is sum_before +1, which is k= sum_before+1, position_in_group is 0).

- The second element is A[position_in_group].

So the code would be:

Sort the array.

Loop through each i to find the correct i where (i+1)*n >=k. But since the array is sorted, and the elements can be duplicates, but we don't need to group them. Because each occurrence in the sorted array contributes to the first element's group. For example, if the array is [1,1,2], then the first two elements are 1. The first group (i=0) has 3 pairs (sum 3), then i=1 (sum 6), i=2 (sum 9). So for k=5, sum after i=1 is 6 >=5. sum_before is 3 (i=1 is 1, sum_before is 1*3=3). position_in_group is 5-3-1=1. So the pair is (1, A[1] =1).

Wait, but in this example, the sorted array is [1,1,2], so A[1] is 1. So the pair is (1,1), which is the 5th pair. Let's list the pairs:

Group i=0 (element 1):

(1,1), (1,1), (1,2) → 3 pairs (sum 3).

Group i=1 (element 1):

(1,1), (1,1), (1,2) → sum 6.

Group i=2 (element 2):

(2,1), (2,1), (2,2) → sum 9.

So the 5th pair is the 5-3-1=1 (position_in_group=1) of group i=1. So the second element is A[1]=1. So the pair is (1,1). That's correct.

So this approach works even when there are duplicates.

Now, how to implement this efficiently.

The sorted array is O(n) space. Sorting is O(n log n) time, which is acceptable for n up to 1e5.

Then, we need to find the i where (i+1)*n >=k. Let's compute i as the minimum i such that (i+1)*n >=k.

This can be computed as i = ceil(k /n) -1. Wait, let's see:

For example, if n=3, k=4. Then (i+1)*3 >=4. i+1 >= 2 (since 2*3=6 >=4). So i=1. Then, (i+1)*3=6 >=4. So yes.

But wait, for k=3. Then (i+1)*3 >=3 → i+1 >=1 → i=0. So sum_before is 0. position_in_group is 3-0-1=2. So the second element is A[2]. Which is correct.

So i can be calculated as (k-1) //n. Because (k-1) //n gives the i. Because (i+1)*n is >=k. For example, k=4, n=2 → (4-1)//2 =1 → i=1. Which is correct. For k=2, (2-1)//2=0. So i=0. Correct.

Yes, because (k-1) //n gives the zero-based index i.

So the steps:

Sort the array.

Compute i = (k-1) // n.

Then, sum_before = i *n.

position_in_group = (k-1) - sum_because (k-1) is zero-based index in the entire list.

Wait, another approach. The entire list is ordered, each element is (i, j) where i is from 0..n-1 and j from 0..n-1. The pair (i,j) is ordered lex. So the index of the pair (i,j) in the list is i *n + j. So to find the k-th element (1-based), the index is k-1. So i = (k-1) //n, j = (k-1) %n.

Wait, but this is exactly the case. Because the pairs are ordered first by i, then by j. So the first element (i=0) has j from 0 to n-1, so indices 0 to n-1. The second element (i=1) has indices n to 2n-1. So the k-1-th index (0-based) is in the i-th group where i = (k-1) //n, and j is (k-1) %n.

So the code can be as simple as:

Sort the array.

i = (k-1) //n

j = (k-1) %n

return (A[i], A[j])

Wait, that can't be right. Because the pairs are ordered lex, but the sorted array is sorted in non-decreasing order. So the first element is A[i], and the second is A[j]. So the pairs (A[i], A[j]) are ordered lex in the same way as (i,j) would be if the array is sorted. But the lex order for the pairs (A[i], A[j]) is determined by their values, not their indices. So this approach would work only if the array is sorted and all elements are unique. Wait, no. Let's think.

For example, sorted array is [1,3,5]. Then, the pairs are ordered as (1,1), (1,3), (1,5), (3,1), (3,3), (3,5), (5,1), (5,3), (5,5). The i is the index of the first element. So for k=4, (i=1, j=0) gives the pair (3,1), which is correct.

So in this case, the code would work. But wait, the problem's first sample input, which when sorted is [1,2], and k=4. Then (k-1) is 3. i=3//2=1. j=3%2=1. So the pair is (2,2), which is correct.

Another example: the problem's second sample input is n=3, k=2. The sorted array is [1,3,5]. (k-1) is 1. i=1//3=0. j=1%3=1. So the pair is (1,3), which is the correct answer.

So this seems to work. But why?

Because when the array is sorted, the pairs are ordered lex, which is equivalent to the order of the indices (i,j) ordered lex. Because the array is sorted, A[i] <= A[i+1]. So when comparing two pairs (i1,j1) and (i2,j2), if i1 <i2, then A[i1] <=A[i2], so (A[i1], A[j1]) is lex <= (A[i2], A[j2]). If i1 ==i2, then j1 <j2 implies A[j1] <=A[j2], so the pairs are ordered accordingly. Therefore, the lex order of the pairs (A[i], A[j]) is exactly the same as the order of the (i,j) pairs in lex order. So the k-th pair in the sorted list of all pairs is simply the pair (A[i], A[j]) where i and j are the indices computed as i = (k-1) //n and j = (k-1) %n.

This is a brilliant realization. So the code can be written as simply sorting the array, then compute i and j as (k-1)//n and (k-1)%n, then output A[i], A[j]. That's O(n log n) time for sorting, which is acceptable for n=1e5. Then, the rest is O(1).

But why does this work even when there are duplicates?

Take an example: array [1,1,2], sorted as [1,1,2], n=3. Let's list all pairs:

i=0 (1): pairs (1,1), (1,1), (1,2)

i=1 (1): pairs (1,1), (1,1), (1,2)

i=2 (2): pairs (2,1), (2,1), (2,2)

So the lex order is:

(1,1), (1,1), (1,1), (1,1), (1,2), (1,2), (1,2), (2,1), (2,1), (2,2). Wait, no, n is 3, so there are 9 pairs.

Wait, for i in 0,1,2:

i=0: j=0,1,2 → (1,1), (1,1), (1,2)

i=1: j=0,1,2 → (1,1), (1,1), (1,2)

i=2: j=0,1,2 → (2,1), (2,1), (2,2)

So the lex order of all pairs is:

(1,1), (1,1), (1,1), (1,1), (1,2), (1,2), (2,1), (2,1), (2,2).

Wait, but according to the code, for k=5, (k-1) is 4. i=4//3 =1, j=4%3=1. The pair is (1,1). Which is the fifth element. But according to the list, the fifth element is (1,2). Wait, this is conflicting. What's wrong here.

Wait, let's re-examine. The code's approach would be: the sorted array is [1,1,2]. For the k=5-th pair (1-based), which is 4 in 0-based.

i =4 //3 =1. j=4%3=1. So A[i] is 1, A[j] is 1. So the pair is (1,1). But according to the actual lex order, the fifth pair is (1,2). So the code is wrong here.

Wait, this is a problem. What's the issue here?

Ah, because the lex order of the pairs (A[i], A[j]) is not the same as the order of the (i,j) indices. Because in the array [1,1,2], A[0] and A[1] are both 1. So the pairs (0,0) is (1,1), (0,1) is (1,1), (0,2) is (1,2). (1,0) is (1,1), (1,1) is (1,1), (1,2) is (1,2). (2,0) is (2,1), etc.

But lex order for pairs (A[i], A[j]) is based on their values, not their indices. So the first four pairs in lex order are (1,1), (1,1), (1,1), (1,1). Then (1,2), (1,2), (2,1), (2,1), (2,2).

But according to the code, the fifth pair (k=5) is (A[1], A[1])= (1,1), which is the fourth element. But the fifth element is (1,2). So the code's approach is wrong in this case.

So why is that?

Because the code assumes that the lex order of the pairs is equivalent to the lex order of their indices (i,j). But when there are duplicates in the array, this is not the case. Because the first element of the pair can be the same for different i's. For example, in the array [1,1,2], the first element can be 1 (i=0), 1 (i=1), or 2 (i=2). So when the code groups pairs by i, the first element of the pair is A[i], but when multiple i's have the same A[i], all of their pairs are grouped together. But in reality, in the lex order, all pairs where the first element is 1 are grouped together, and within that group, all pairs (1, A[j]) are ordered by A[j]. So the code's approach of using i=(k-1)//n and j=(k-1)%n is incorrect because it assumes that the first element is ordered by the index i, but when multiple i's have the same value, their pairs are interleaved in the lex order.

So the code's approach works only if the array is strictly increasing. But when there are duplicates, the approach is wrong.

This is a problem. So the previous reasoning was incorrect. The correct approach must take into account that all pairs with the same first element are grouped together, regardless of their index i. Because in the lex order, (A[i], A[j]) is grouped by A[i], not by i. So for example, in the array [1,1,2], all pairs where the first element is 1 are before any pairs where the first element is 2. But in the code's approach, the pairs for i=0 (1) and i=1 (1) are considered as separate groups, but in reality, their pairs are all part of the same group in lex order.

So the initial approach is incorrect. Therefore, the correct way to handle this is to find the first element x in the sorted array such that the number of pairs with first element less than x is less than k, and the number of pairs with first element <=x is >=k. Then, within the x group, find the (k - count_less *n)th pair.

But how to compute x and the count_less.

For example, in the array [1,1,2], the sorted array is [1,1,2]. The lex order of pairs is:

(1,1), (1,1), (1,1), (1,1), (1,2), (1,2), (2,1), (2,1), (2,2).

So the first four pairs are all where first element is 1. The next two are first element 1, but in reality, the first element is 1 (from i=0 and i=1). So the code's approach of grouping by i is wrong.

So the correct approach is:

1. Sort the array.

2. Count the number of elements less than x, and the number of elements equal to x.

But to find the first element x such that the cumulative pairs up to x is >=k. Let's think again.

Each occurrence of a first element x in the sorted array contributes n pairs. But in lex order, all pairs with first element x (regardless of their position in the sorted array) are grouped together. Wait, no. Because if the sorted array has multiple x's, then each occurrence of x in the first element is part of the x group. But the pairs in the x group are ordered by their second elements. So for example, in the sorted array [1,1,2], all pairs where the first element is 1 are in the x=1 group. So the group has 3 (number of x's) *3 (n) pairs? No, because each occurrence of x in the first element contributes n pairs. So the total number of pairs in the x group is (number of occurrences of x) *n. So the total pairs in the x group is count_x *n. So the total pairs before x group is sum_{y <x} count_y *n.

Therefore, to find the x group, we need to find the x in the sorted array such that the sum of count_y *n for all y <x is less than k, and sum_{y <=x} count_y *n >=k.

But how to compute x?

But the array is sorted. So all elements are in non-decreasing order. So we can process the sorted array and group consecutive elements. For example, [1,1,2] has group 1 (count 2) and group 2 (count 1).

So, for each unique value in the sorted array, we can compute the cumulative count of elements (count) multiplied by n. Then, find the unique value x where the cumulative up to x's previous values is less than k, and cumulative up to x is >=k.

Once x is found, the number of pairs before x is sum_prev = sum_{y <x} (count_y) *n. Then, the remaining k' =k - sum_prev. The x group has (count_x)*n pairs. So the position within the x group is k' -1. Then, the first element of the pair is x, and the second element is the (position_in_group // count_x)-th element in the sorted array.

Wait, perhaps. Let me think:

Each occurrence of x in the first element contributes n pairs, all with first element x. For example, if x occurs 2 times in the array, then the x group has 2n pairs. For each of these 2 occurrences of x in the first element, their pairs are (x, a_0), (x, a_1), ..., (x, a_{n-1}).

In lex order, these are grouped together. But in lex order, all pairs in the x group are ordered first by x (since their first element is x), then by their second element. So within the x group, the pairs are ordered by the second element's value. So the entire x group is a sequence of (x, a_0), (x, a_1), ..., (x, a_{n-1}), (x, a_0), (x, a_1), ..., (x, a_{n-1}), ... (count_x times).

But when sorted, the array a is in non-decreasing order. So the second elements in each occurrence are ordered. So the x group's pairs are ordered by their second elements. For example, the x group's pairs are:

for each occurrence of x in the first element:

   (x, a_0), (x, a_1), ..., (x, a_{n-1}).

So when you have multiple occurrences of x in the first element, the pairs are ordered by their second elements. But since the array is sorted, the second elements are in non-decreasing order. So the entire x group's pairs are ordered as (x, a_0), (x, a_0) (for second occurrence of x), (x, a_1), (x, a_1), ..., (x, a_{n-1}), (x, a_{n-1}).

No, that's not correct. For example, in the array [1,1,2], the x group for x=1 has 2 occurrences of x in the first element. For each occurrence, the pairs are (1,1), (1,1), (1,2). Then, for the second occurrence, the pairs are (1,1), (1,1), (1,2). So the entire x group is 2*3=6 pairs. But in lex order, all pairs in the x group are ordered by their second element. So the lex order of the x group is:

(1,1), (1,1), (1,1), (1,1), (1,2), (1,2).

So within the x group, the pairs are ordered by the second element. So the x group's pairs are all (x, a_j) for each occurrence of x in the first element, but ordered by a_j. But how to model this.

Wait, no. Because the lex order of the pairs is determined first by the first element (x), then by the second element. So all pairs in the x group are ordered by their second element. So for the entire list of pairs in the x group, they are sorted by the second element. So the x group's pairs are all (x, a_j) for all j in 0..n-1, and for each occurrence of x in the first element. But when sorted, the order is all (x, a_0), (x, a_1), ..., (x, a_{n-1}) for each occurrence of x in the first element. But since the array is sorted, a_0 <= a_1 <= ... <= a_{n-1}, so the pairs for the x group are ordered by the second element. So the entire x group's pairs are ordered by the second elements. But for each occurrence of x in the first element, the pairs are arranged in the order of the array's sorted second elements. So when you have multiple occurrences of x, the pairs are repeated. For example, if x occurs twice and the array is [1,1,2], then the x group's pairs are (1,1), (1,1), (1,2) for the first occurrence, and (1,1), (1,1), (1,2) for the second occurrence. So the entire x group is 6 pairs, ordered as (1,1) *4, (1,2)*2. But in lex order, the pairs are ordered as (1,1), (1,1), (1,1), (1,1), (1,2), (1,2). So the ordering is correct.

So, the x group's pairs are ordered by their second elements. Therefore, for the entire x group, the pairs are ordered as follows: for each j in 0..n-1, the pair (x, a_j) appears once for each occurrence of x in the first element. So the number of pairs in the x group for j is count_x. So the total pairs in the x group is count_x *n. But when ordered lex, the pairs are grouped by a_j. For a_j, there are count_x pairs. So for each j, the pairs (x, a_j) are count_x times in a row.

So to find the k-th pair in the entire list:

1. Find the x such that sum_prev (sum of count_y *n for y <x) <k <= sum_prev + count_x *n.

2. Then, within the x group, the remaining k' =k - sum_prev.

3. Now, the x group is count_x *n pairs. But these pairs are ordered by a_j. For each j, there are count_x pairs (x, a_j). So the pairs are ordered as:

For j=0 to n-1:

   count_x copies of (x, a_j).

So the j-th group (for a_j) has count_x pairs.

So the problem now is to find, within the x group, the j such that (j-1)*count_x <k' <= j*count_x. Then, the second element is a_j.

Wait, let's think with the example:

In the x group for x=1, count_x=2, n=3. So sum_prev=0. The x group has 6 pairs.

k' =5. We need to find j.

Each a_j has count_x=2 pairs. So j=0: 2 pairs (1,1), j=1: 2 pairs (1,1), j=2: 2 pairs (1,2).

For k'=5, which is within j=2's group (positions 5-6). So j=2. So the pair is (1,2).

But how to compute j for a general k'.

Since each j contributes count_x pairs, the j is computed as (k'-1) // count_x.

Because:

For j=0, pairs 1-2 (k'=1-2) → 0-based index 0-1.

For j=1, pairs 3-4 (k'=3-4).

For j=2, pairs5-6 (k'=5-6).

So for k'=5, (5-1) //2=4//2=2 → j=2. Correct.

Another example: k'=3 → (3-1)/2=1 → j=1. So the pair is (1,1).

Yes.

So the algorithm steps are:

1. Sort the array.

2. Preprocess the sorted array to find the count of each element, and build a list of unique elements along with their counts and cumulative counts.

   For example, for sorted array [1,1,2], the unique elements are 1 and 2, with counts 2 and 1. The cumulative counts would be 0, 2, 3.

3. Compute the prefix sums of (count *n) for each unique element. For the example:

   unique_elements = [1,2]

   counts = [2,1]

   prefix_sums = [0, 2*3=6, 6 +1*3=9]

4. Find the index in the prefix_sums where the sum_prev <k <= sum_prev + count_x *n. This can be done with binary search.

5. Once x is found (the unique element at index i), compute sum_prev = prefix_sums[i].

6. Compute k' =k - sum_prev.

7. Compute j = (k'-1) // count_x.

8. The second element is the j-th element in the sorted array.

Wait, no. Because j is the index in the sorted array. For example, in the example where x=1, count_x=2. k'=5. j=(5-1) //2 =2. The second element is a[2], which is 2.

Yes.

So the code steps are:

- Sort the array.

- Create a list of unique elements with their counts and prefix sums.

   For example, sorted array is [1,1,2]. unique elements are 1,2. counts are [2,1]. prefix_sums is [0, 6, 9].

- Perform a binary search on the prefix_sums to find the first prefix_sums[i] where prefix_sums[i] >=k. The x is the unique element at index i-1.

   Wait, no. Because the prefix_sums array is [0, 6,9]. So for k=5, which is between 0 and 6, the x is 1 (prefix_sums[1] is 6 >=k=5). i=1. So the x is unique_elements[i-1] =unique_elements[0] =1.

- Then, sum_prev = prefix_sums[i-1] =0. k' =5-0=5.

- count_x = counts[i-1] =2.

- j=(5-1)//2=2.

- second element is sorted_array[2] =2.

So the pair is (1,2), which is correct.

Another example: sorted array [1,3,5]. unique_elements are [1,3,5], counts [1,1,1]. prefix_sums [0,3,6,9]. For k=2, sum_prev=0. k'=2. j=(2-1)//1=1. So pair is (1,3), which matches the sample.

Another example: the first sample input sorted array [1,2]. unique_elements [1,2]. counts [1,1]. prefix_sums [0, 2,4]. k=4. Find prefix_sums[i] >=4. i=2. sum_prev=prefix_sums[1]=2. x=2. count_x=1. j=(4-2-1) =1, but wait k'=4-2=2. j=(2-1) //1=1. So j=1. sorted array[1] is 2. Pair (2,2).

So this approach works.

Thus, the steps are:

1. Sort the array.

2. Precompute the unique elements, their counts, and prefix sums (sum of count *n up to each unique element).

3. Binary search the prefix sums to find the x group.

4. Compute j as (k' -1) // count_x, where k' is k - sum_prev.

5. The pair is (x, sorted_array[j]).

So the code needs to:

- Sort the array.

- Compute the unique elements and their counts.

- Compute the prefix sums, where prefix_sums[0] =0, prefix_sums[1] = count of first unique element *n, prefix_sums[2] = prefix_sums[1] + count of second unique element *n, etc.

- Binary search for the smallest i such that prefix_sums[i] >=k. The x is unique_elements[i-1].

But how to build the prefix_sums.

Example:

sorted array is [1,1,2].

unique_elements are [1,2].

counts are [2,1].

prefix_sums starts with [0], then 0 +2*3=6 → [0,6], then 6 +1*3=9 → [0,6,9].

So for a list of m unique elements, the prefix_sums has m+1 elements.

To binary search for the first prefix_sum >=k, the index i gives us the unique element at i-1.

Now, how to implement this.

In Python:

sorted_arr = sorted(array)

unique_elements = []
counts = []

current = sorted_arr[0]
current_count =1
for num in sorted_arr[1:]:
    if num == current:
        current_count +=1
    else:
        unique_elements.append(current)
        counts.append(current_count)
        current = num
        current_count =1
unique_elements.append(current)
counts.append(current_count)

Then, compute the prefix_sums.

prefix_sums = [0]
for i in range(len(unique_elements)):
    prefix_sums.append(prefix_sums[-1] + counts[i] *n)

Then, perform a binary search on prefix_sums to find the smallest i where prefix_sums[i] >=k.

The x is unique_elements[i-1], and the sum_prev is prefix_sums[i-1].

Then, k' =k - sum_prev.

count_x = counts[i-1]

j = (k'-1) // count_x

second_element = sorted_arr[j]

So the code should work.

Now, time complexity:

Sorting is O(n log n).

Building unique_elements and counts is O(n).

Building prefix_sums is O(m), where m is the number of unique elements.

Binary search is O(log m).

Everything else is O(1).

For n up to 1e5, this is acceptable.

So the code is correct.

Now, let's test the example where the array is [1,1,2], k=5.

sorted_arr is [1,1,2]

unique_elements = [1,2], counts = [2,1], prefix_sums = [0, 6, 9].

k=5: binary search for prefix_sums >=5. The prefix_sums are [0,6,9]. The first i where prefix_sums[i] >=5 is i=1. sum_prev =prefix_sums[i-1] =0. x=1. count_x=2.

k'=5-0=5.

j=(5-1) //2=2.

sorted_arr[j] =2. So pair is (1,2).

Which is correct.

Another test case:

Sample input 2:

n=3, k=2, array [3,1,5]. sorted array is [1,3,5].

unique_elements = [1,3,5], counts=[1,1,1]. prefix_sums = [0,3,6,9].

k=2: binary search for prefix_sums >=2. The first i is 1 (prefix_sums[1]=3 >=2). sum_prev=0. x=1.

k'=2-0=2.

count_x=1.

j=(2-1) //1 =1.

sorted_arr[1] is 3. Pair is (1,3). Correct.

Sample input 1:

n=2, k=4. array [2,1] sorted to [1,2]. unique_elements [1,2], counts [1,1]. prefix_sums [0,2,4].

k=4: binary search i=2 (prefix_sums[2]=4 >=4). sum_prev=prefix_sums[1]=2. x=2. count_x=1.

k'=4-2=2.

j=(2-1)//1=1.

sorted_arr[1] is 2. Pair (2,2). Correct.

The other example with duplicate first elements:

array [1,1,2], n=3, k=5.

As discussed, the code returns (1,2).

Yes.

So this approach works.

Now, implementing this in Python.

But what about when k is larger than the total number of pairs? According to the constraints, k <=n^2, so it's guaranteed to be valid.

Now, code steps:

Read n and k.

Read array.

Sort it.

Compute unique_elements and counts.

Compute prefix_sums.

Binary search to find the right i.

Then, compute x, sum_prev, k', count_x, j, and output.

Now, the code.

But how to do binary search on prefix_sums.

In Python, we can use the bisect module.

prefix_sums is a list that is strictly increasing.

We want to find the first index i where prefix_sums[i] >=k.

So:

import bisect

i = bisect.bisect_left(prefix_sums, k)

then, the unique element is at i-1.

But prefix_sums is a list where each element is the cumulative sum up to that unique element.

For example, for the sorted array [1,1,2], prefix_sums is [0,6,9].

So for k=5, bisect_left finds the first index where prefix_sums[i] >=5, which is 1.

Yes.

So the code can be written as:

import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# Compute unique elements and counts
unique = []
counts = []
if not a:
    pass  # but n >=1
current = a[0]
cnt =1
for num in a[1:]:
    if num == current:
        cnt +=1
    else:
        unique.append(current)
        counts.append(cnt)
        current = num
        cnt =1
unique.append(current)
counts.append(cnt)

# Compute prefix_sums
prefix_sums = [0]
for c in counts:
    prefix_sums.append(prefix_sums[-1] + c *n)

# Find i using bisect
i = bisect.bisect_left(prefix_sums, k)
# x is unique[i-1]
x = unique[i-1]
sum_prev = prefix_sums[i-1]
k_prime = k - sum_prev
count_x = counts[i-1]
j = (k_prime -1) // count_x
y = a[j]

print(x, y)

This should handle all cases correctly.

Let's test the example where array is [1,1,2], k=5.

sorted array is [1,1,2]. unique is [1,2], counts [2,1], prefix_sums [0,6,9]. bisect_left(prefix_sums,5) is 1. sum_prev=0, k_prime=5, count_x=2. j=(5-1)//2=2. a[2] is 2. So output is 1 2. Correct.

Another example:

array [1,3,5], k=2. prefix_sums [0,3,6,9]. bisect_left([0,3,6,9],2) is 1. x=1. sum_prev=0. k_prime=2. count_x=1. j= (2-1)//1=1. a[1] is3. output 1 3. Correct.

Sample input 1:

array [2,1] sorted to [1,2]. unique [1,2], counts [1,1]. prefix_sums [0, 2,4]. k=4. bisect_left([0,2,4],4) returns 2. i-1=1. x=2. sum_prev=2. k_prime=4-2=2. count_x=1. j=(2-1)//1=1. a[1] is2. output 2 2. Correct.

Thus, this code should handle all cases.
</think>

```python
import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

unique = []
counts = []
current = a[0]
cnt = 1
for num in a[1:]:
    if num == current:
        cnt += 1
    else:
        unique.append(current)
        counts.append(cnt)
        current = num
        cnt = 1
unique.append(current)
counts.append(cnt)

prefix_sums = [0]
for c in counts:
    prefix_sums.append(prefix_sums[-1] + c * n)

i = bisect.bisect_left(prefix_sums, k)
x = unique[i - 1]
sum_prev = prefix_sums[i - 1]
k_prime = k - sum_prev
count_x = counts[i - 1]
j = (k_prime - 1) // count_x
y = a[j]

print(x, y)
```