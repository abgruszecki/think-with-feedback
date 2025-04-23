<think>
Okay, let's try to understand this problem. The task is to find the largest group of rays such that every ray in the group intersects all the others in the group. Hmm. 

First, I need to model how the rays are arranged. Each ray enters through a hole on one side and exits through a hole on the opposite side. The positions of the entry and exit holes determine the path of the ray. For two rays to intersect each other, their entry and exit positions must form a certain configuration. 

Let me think: Two rays a and b. Suppose in the entry side, a is to the left of b. If, in the exit side, a is to the right of b, then their paths cross and they intersect. So for two rays to intersect, their entry order is the reverse of their exit order. 

So, the problem reduces to finding a subset of rays where every pair in the subset has their entry order and exit order reversed. Wait, but for a group of more than two rays, how does that work? Because each pair must satisfy this condition. 

Wait, if in the group, the entry order is a permutation where each pair is inverted in the exit order. So, for example, in a group of three rays A, B, C, if in the entry order they are A comes before B, which comes before C, then in the exit order, C comes before B, which comes before A. Then every pair (A and B, A and C, B and C) would have their entry and exit orders inverted, so all pairs intersect. 

Wait, no. Let's see: For three rays, if the entry order is A B C, and the exit order is C B A. Then A and B are inverted (A comes before B in entry, but after in exit), B and C are inverted (B comes before C in entry, after in exit), and A and C are inverted. So all pairs intersect. So such a group is valid. 

So the largest such group is a sequence of rays where the entry order is a permutation that is the reverse of their exit order. But how can we model this for any subset?

Alternatively, each ray is defined by its entry position and exit position. Let's model each ray as a pair (x_i, y_i), where x_i is the entry position (from the first line), and y_i is the exit position (from the third line). Wait, wait: the second line gives the entry positions. The second line's i-th integer x_i is the ray that enters the i-th hole. So the entry positions for the rays are determined by the second line. For example, if the second line is [1,4,5,2,3], then the entry positions are such that ray 1 enters position 1, ray 4 enters position 2, ray5 position 3, etc. So for each ray, the entry position is the index in the second line where the ray appears. Similarly, the exit position is the index in the third line where the ray appears. 

Ah, right. So for each ray, we need to find its entry index and exit index. So for example, if the second line is [1,4,5,2,3], then the entry index for ray 1 is 0 (assuming 0-based or 1-based?), but the problem says the i-th integer is the ray entering the i-th hole. So the entry hole for ray xi is position i. Wait, the second line is the entry holes. The second line has n integers. The i-th integer in the second line (call it x_i) is the ray that enters from the i-th hole. So each hole (position) on the entry side is given by the index i (from 1 to n), and the ray x_i is the one entering through that hole. So for example, if the second line is [3,1,2], then in entry position 1 (hole 1), the ray is 3. Entry position 2 (hole 2), ray 1. Entry position 3, ray 2. 

Similarly, the third line gives the exit holes. The i-th integer y_i is the ray exiting from the i-th hole. So for the exit positions, the i-th hole (position) has ray y_i exiting. 

So for each ray r, we can find its entry position (entry[r] = the index in the second line where r appears) and exit position (exit[r] = the index in the third line where r appears). 

So for example, in the first sample input:

Second line: 1 4 5 2 3. So entry positions are:
ray 1: entry index 0 (assuming 0-based) or 1 (1-based)? The problem says the i-th integer is the ray entering the i-th hole, which is probably 1-based. So in the sample input, the second line's first number is 1, which is the ray entering hole 1. So for ray 1, entry position is 1. For ray 4, entry position is 2. So entries are 1-based.

Similarly, the third line's first number is 3, so for ray 3, exit position is 1. 

So each ray r has an entry position e_r and exit position x_r. 

Now, two rays a and b intersect if (e_a < e_b) != (x_a < x_b). So when e_a < e_b but x_a > x_b, they cross. 

Now, the problem is to find the largest subset S of rays such that every pair in S intersects. 

What's the structure of such a subset S?

In such a subset, for any two distinct rays a and b in S, (e_a < e_b) if and only if (x_a > x_b). 

Wait, because for any two, a and b in S, if e_a < e_b, then x_a must be > x_b. Because otherwise, if e_a < e_b and x_a < x_b, they don't cross. So in the subset S, the order of e's is the reverse of the order of x's. 

So, for the entire subset S, the entry positions must form a sequence where they are ordered in a way that their exit positions are in the exact reverse order. 

But how can we model this? It seems similar to finding a sequence where the entries are in a certain order and exits are in the reverse. So for the subset S, when sorted by entry positions, their exit positions are in decreasing order. Because then, for any two elements in the subset, if a comes before b in entry, their exit is after, so they cross. 

But wait, in such a case, the exit positions form a decreasing sequence. So the problem reduces to finding the longest decreasing subsequence in the exit positions when sorted by entry positions. But wait, no. Because the subset S must be such that all pairs cross. So in the subset, every pair must cross each other. 

So the subset S must be such that when ordered by entry positions, the exit positions are in strictly decreasing order. Because in that case, every pair in the subset will have their entry order and exit order reversed. So the subset S is a chain where the entries are increasing and exits are decreasing. 

But in such a subset, any two elements in S form a pair that crosses. So the maximum size of such a subset is the length of the longest decreasing subsequence in the exit positions, when the rays are sorted by their entry positions. 

Wait, that makes sense. Because if we arrange the rays in the order of their entry positions (from left to right), then their exit positions must form a strictly decreasing sequence. Because then, any two rays in this sequence will have entry order a_i < a_j and exit order a_i > a_j. So the maximum size is the length of the longest decreasing subsequence (LDS) of the exit positions when the rays are sorted by their entry positions. 

Alternatively, the maximum size is the length of the longest such subsequence. 

Wait, but the problem requires that every pair in the subset must cross. So if the subset is such that when sorted by entry positions, the exit positions are in a decreasing sequence, then all pairs cross. Because for any i < j in the sorted entries, exit[i] > exit[j], so the pair (i,j) crosses. 

So the problem reduces to: arrange the rays in the order of their entry positions (since entry positions are unique, each ray has a unique entry position). Then, for the sequence of exit positions, find the length of the longest decreasing subsequence. 

But wait, the longest decreasing subsequence is the same as the longest subsequence where each element is less than the previous. 

Wait, but in the sample input 1:

The second line (entry order) is [1,4,5,2,3]. So the entry positions are ordered as 1,4,5,2,3. Wait, no. Wait, the entry positions for each ray are determined by their index in the second line. So for the second line, the first element is 1, which is the ray entering hole 1. The second element is 4, ray entering hole 2. So for the entry positions, the order of the rays is 1, 4,5,2,3. Then, their exit positions (third line is [3,4,2,1,5]). Let's map each ray's exit position:

Third line is [3,4,2,1,5]. So for exit positions:

ray 3 is at exit position 1 (since third line's first element is 3).

ray 4's exit position is 2 (since third line's second element is 4).

ray 2's exit position is 3 (third line's third element is 2).

ray 1's exit position is 4 (third line's fourth element is 1).

ray 5's exit position is 5 (third line's fifth element is 5).

Wait, no. Wait, the third line gives the exit holes. So the i-th integer in the third line is the ray exiting from the i-th hole. So for example, the third line's first element is 3, which means ray 3 exits from exit hole 1. The third line's fourth element is 1, which means ray 1 exits from exit hole 4. 

So for each ray, we can create a dictionary mapping the exit position. For example:

In the first sample input, the third line is [3,4,2,1,5]. So:

exit_hole for ray 3 is 1.

exit_hole for ray4 is 2.

exit_hole for ray2 is 3.

exit_hole for ray1 is 4.

exit_hole for ray5 is5.

So when we arrange the rays in the order of their entry positions (as given by the second line), which is [1,4,5,2,3], their exit positions are [4, 2,5,3,1]. So the sequence of exit positions is [4,2,5,3,1]. 

Wait, let's compute this:

For each ray in the second line (entry order):

Second line is 1,4,5,2,3. So the entry order is rays 1,4,5,2,3.

For each of these rays, their exit position is:

Ray 1: exit position 4 (from the third line).

Ray4: exit position 2 (third line's second element is 4, so exit hole 2).

Ray5: third line's fifth element is5, so exit position5.

Ray2: third line's third element is2, so exit position3.

Ray3: third line's first element is3, so exit position1.

So the sequence of exit positions is [4,2,5,3,1]. 

Now, the problem is to find the longest decreasing subsequence in this sequence. Let's see:

The sequence is 4,2,5,3,1. 

Looking for the longest decreasing subsequence:

Possible candidates:

4,2,3,1: that's decreasing? No, 4>2>3 is not. Wait, no. The sequence must be strictly decreasing. 

Wait, the longest decreasing subsequence here is 5,3,1 (length 3). Or 4,2,1 (length 3). So maximum is 3, which matches the sample output. 

Yes, the sample output is 3, which is correct. So the approach seems correct. 

So the problem reduces to:

- For each ray, determine its entry position (the index in the second line where it appears) and exit position (the index in the third line where it appears). 

- Sort the rays in the order of their entry positions (since they must be arranged in increasing entry order, as per the entry positions). 

- Then, the exit positions of these ordered rays form a sequence. Find the length of the longest decreasing subsequence (LDS) in this sequence. 

The maximum possible LDS is the answer. 

So the problem is now to compute the LDS of a sequence, which can be done in O(n log n) time. 

But how to compute the LDS efficiently? 

The standard approach for the longest increasing subsequence (LIS) uses a patience sorting-like algorithm with binary search, which runs in O(n log n) time. For the LDS, since it's the same as the LIS of the negated sequence, we can compute it similarly. 

So the steps are:

1. For each ray, find its entry position and exit position. 

2. Create an array of exit positions sorted by the entry positions. 

3. Find the LDS of this array. 

So the code steps:

- Read n. 

- Read the second line as a list of rays in entry order. Create a dictionary to map each ray to its entry index (1-based, perhaps). 

- Read the third line as a list of rays in exit order. Create a dictionary to map each ray to its exit index. 

- For each ray in the entry order list (since we need to process them in the order of entry positions), collect their exit positions. 

- Then, compute the LDS of this exit positions list. 

So, how to compute LDS efficiently?

The LDS can be computed by maintaining a list where we track the smallest possible last element of a decreasing subsequence of length l. 

For example, for each element x in the sequence, we find the first position in the list where the element is less than x. Replace that position with x. The length of the list at the end is the length of the LDS. 

Wait, the standard approach for LIS in O(n log n) time is to keep a list of the smallest possible last elements for increasing sequences of different lengths. For LDS, we can reverse the logic. 

So, for each x in the sequence, we want to find the first element in the list that is <= x (since we are looking for a decreasing sequence). Wait, no. Let's think again. 

In the LIS approach, for each x, we find the first element in the list that is >= x (if we want to allow duplicates in non-strictly increasing sequences). Wait, perhaps it's better to think in terms of the LDS being the same as the LIS of the negated sequence. So, if we take all elements and multiply by -1, then the LIS of this new sequence is the LDS of the original. 

For example, the sequence [4,2,5,3,1] becomes [-4,-2,-5,-3,-1]. The LIS of this new sequence is 3 (e.g., -5, -3, -1). The LDS of the original is the same as the LIS of the negated sequence. 

So, if we compute the LIS on the negated sequence, we get the LDS of the original. 

Thus, the code can be written as follows:

Take the sequence of exit positions. Create a new sequence by negating each element. Compute the LIS of this new sequence, which gives the LDS of the original. 

But the problem requires that the subset must have all pairs crossing, which implies a strictly decreasing sequence. So, in the exit positions, the LDS must be strictly decreasing. 

Wait, because if two elements are equal in the exit positions, then when their entry positions are in order (since the entry order is sorted), their exit positions are equal. So, for two rays a and b with entry a before entry b, and exit a equal to exit b, then a and b do not cross. Because (e_a < e_b) and (x_a == x_b), so (e_a < e_b) and (x_a not > x_b) → they don't cross. 

Thus, the subset must have exit positions strictly decreasing. So the LDS must be a strictly decreasing sequence. 

So, when computing the LDS, we need to find the longest strictly decreasing subsequence. 

In that case, when we compute the LIS for the negated sequence, we have to find the longest strictly increasing subsequence. 

Because the original sequence is strictly decreasing if and only if the negated sequence is strictly increasing. 

So, the algorithm for the LDS in this case is equivalent to the LIS of the negated sequence, but with strict inequalities. 

The standard LIS algorithm can be modified to handle strict inequalities by using bisect_left or bisect_right. 

So, the approach is:

- Negate all elements of the exit sequence. 

- Compute the LIS of this negated sequence, with strictly increasing order. 

- The length of this LIS is the required answer. 

So, how to compute the LIS with strict increasing order efficiently? 

The standard approach is as follows:

Initialize an empty list. For each element in the sequence:

- Use binary search to find the first position in the list where the element is >= current element. 

- If found, replace the element at that position with the current element. 

- Else, append the current element. 

This gives the length of the LIS for strictly increasing sequences. 

For example, let's see the first sample's negated sequence: [-4, -2, -5, -3, -1]. 

Processing each element:

Start with empty list.

First element is -4. List is empty, append. List: [-4]

Second element is -2. Since -2 is greater than -4, append. List: [-4, -2]

Third element is -5. Binary search for the first element >= -5. The list is [-4, -2]. -5 is less than all, so position 0. Replace -4 with -5. List: [-5, -2]

Fourth element is -3. Find first element >= -3. The list is [-5, -2]. -3 is between -5 and -2. The first element >= -3 is -2 (index 1). Replace -2 with -3. List: [-5, -3]

Fifth element is -1. It's greater than all in the list ([-5, -3]), so append. List becomes [-5, -3, -1]. Length is 3. 

Which matches the sample's expected answer. 

So the approach works. 

Thus, the steps for the code are:

1. Read n.

2. Read the entry list (second line) and create a dictionary entry_pos where entry_pos[ray] = i (1-based index).

3. Read the exit list (third line) and create exit_pos[ray] = i (1-based index).

4. Create a list of exit positions for each ray in the order of their entry positions. So, for each ray in the entry list (order of entry), append exit_pos[ray].

5. Negate all elements in this list. 

6. Compute the LIS of this negated list, using the standard algorithm for strict increasing. 

7. The length of the LIS is the answer. 

Now, the problem is to handle n up to 1e6. So the code needs to handle O(n log n) time, which for 1e6 is acceptable. 

But in Python, using the standard approach with a list and bisect may be too slow for 1e6 elements. Because for each element, performing a bisect (O(log n)) step, multiplied by 1e6 gives around 1e6 * 20 = 2e7 operations, which should be manageable. 

But in Python, the bisect module is implemented in C, so it's fast. So the code should handle 1e6 elements. 

Now, the code steps:

First, read the input. 

But the input for n can be up to 1e6. So for reading the second and third lines, which are n elements each, we need to read them efficiently. 

In Python, using input().split() may be slow for large n. But for 1e6 elements, it's manageable. 

But perhaps using sys.stdin is better. 

But for code submission, the standard way is to use input() for reading. However, when n is 1e6, using input().split() can be slow. 

So perhaps the code should read via sys.stdin. 

So, in Python:

import sys

n = int(sys.stdin.readline())

entry_rays = list(map(int, sys.stdin.readline().split()))
exit_rays = list(map(int, sys.stdin.readline().split()))

Then, create entry_pos and exit_pos dictionaries. 

But for 1e6 elements, using a dictionary may be slow. So better to use a list where the index is the ray number. 

Wait, rays are numbered from 1 to n. So for entry_rays and exit_rays, we can create lists where the index is the position (0-based or 1-based?), and the value is the ray number. 

Wait, for entry_rays, the i-th element (0-based) is the ray that enters the (i+1)-th hole. So entry_pos[ray] = i+1. 

So, to create entry_pos, we can do:

entry_pos = [0] * (n + 1)  # rays are 1-based
for i in range(n):
    entry_pos[entry_rays[i]] = i + 1  # since the i-th hole is (i+1)th position?

Wait, no. The entry_rays list is the list of rays in the order of the entry holes. For example, if the entry_rays list is [3,1,2], then hole 1 (position 1) has ray 3 entering, hole 2 (position 2) has ray 1, etc. So for ray 3, entry position is 1. For ray 1, entry position is 2. 

So the entry_pos for a ray r is the 1-based index of its occurrence in the entry_rays list. 

So for the entry_rays list, we can loop over each element, and for each r in entry_rays, store entry_pos[r] = (i+1). Because the list is 0-based, and the hole positions are 1-based. 

Similarly for exit_rays. 

So code for entry_pos and exit_pos:

entry_pos = [0] * (n + 1)
for idx in range(n):
    r = entry_rays[idx]
    entry_pos[r] = idx + 1

exit_pos = [0] * (n + 1)
for idx in range(n):
    r = exit_rays[idx]
    exit_pos[r] = idx + 1

Then, create the list of exit positions sorted by entry order. 

The entry order is the order of the rays in the entry_rays list. So for each ray in entry_rays, we get their exit position. 

So the exit_sequence is:

exit_sequence = []
for r in entry_rays:
    exit_sequence.append(exit_pos[r])

Then, we negate each element in exit_sequence:

negated = [-x for x in exit_sequence]

Then compute the LIS of the negated sequence. 

But wait, the problem requires that the exit positions are in a strictly decreasing order. So the negated sequence must be strictly increasing. 

So, the code for LIS (strictly increasing):

import bisect

lis = []
for num in negated:
    # Find the index where num can be inserted in lis to replace the first element >= num
    idx = bisect.bisect_left(lis, num)
    if idx < len(lis):
        lis[idx] = num
    else:
        lis.append(num)
return len(lis)

Wait, no. Wait, the bisect_left function returns the insertion point for num in a sorted list. For a strictly increasing sequence, we want to find the first element >= num and replace it with num. 

Wait, no. Let's think again. 

For example, if the current sequence in lis is [2,5,7], and the next num is 3. Then, bisect_left returns index 1 (since 3 is between 2 and 5). Replacing 5 with 3 gives [2,3,7], which allows for longer sequences. 

In the standard approach, for a strictly increasing LIS:

We use bisect.bisect_left. 

So for each num in the sequence, if num is larger than the last element in lis, append it. Otherwise, find the first element in lis that is >= num, replace it with num. 

Wait, no. That's for non-decreasing. Because in that case, when num is equal to an element, it would replace the next one. 

Wait, the standard approach for strictly increasing LIS would use bisect_left. Let's see:

Suppose we have a sequence where we want to find the longest strictly increasing subsequence. 

The approach is to maintain a list where each element is the smallest possible last element of an increasing subsequence of that length. 

For each new element x:

- If x is larger than the last element of the list, append x. 

- Else, find the first element in the list that is >= x, and replace it with x. 

This way, the list remains sorted, and each element is the smallest possible for that length. 

But for strictly increasing, this approach works. 

Wait, for example, the sequence [1,3,3,4]. The LIS is 3 (1,3,4). The algorithm would produce:

Process 1: list is [1]

Process 3: append → [1,3]

Process 3: find first >= 3 → index 1. Replace → [1,3]

Process 4: append → [1,3,4]. Length is 3. 

Which is correct. 

But the actual LIS for strictly increasing would be 3 as well. 

But in the case where there are duplicates, like [1,2,2,3], the algorithm would compute the LIS as 3 (1,2,3), which is correct. 

So the standard approach using bisect_left works for strictly increasing sequences. 

Thus, the code for the LIS (strictly increasing) is correct. 

So putting it all together:

Read the entry_rays and exit_rays lists. 

Create entry_pos and exit_pos as arrays where entry_pos[r] is the 1-based index of the ray r in the entry_rays list, and exit_pos[r] is the 1-based index of the ray r in the exit_rays list. 

Then, create the exit_sequence as the list of exit_pos[r] for each r in entry_rays in order. 

Negate each element to get the negated list. 

Compute the LIS of this negated list using the standard approach with bisect_left, which gives the LDS of the original exit_sequence. 

Return the length of the LIS. 

Testing the first sample:

exit_sequence = [4,2,5,3,1]

negated = [-4,-2,-5,-3,-1]

Processing:

-4 → lis = [-4]

-2 is larger than -4 → append → [-4,-2]

-5 is less than -4 → replace at 0 → [-5,-2]

-3 is less than -5 → no. Wait, the next number is -3. 

Wait, the next number in the negated sequence is -3 (from exit_sequence element 3 → 3 becomes -3). So processing -3:

Current lis is [-5, -2]. 

We check if -3 is larger than the last element (-2), which it is not. So find the first element >= -3. 

The list is [-5, -2]. 

-3 is between -5 and -2. So bisect_left for -3 in [-5, -2] returns index 1 (since -3 >-5 and -3 < -2). So replace the element at 1 (-2) with -3. Now the list is [-5, -3]. 

Then, next element is -1. It's larger than the last element (-3), so append. lis becomes [-5, -3, -1]. Length 3. 

Which is correct. 

Second sample input:

3

3 1 2

2 3 1

Entry_rays: [3,1,2]

Exit_rays: [2,3,1]

entry_pos:

3 → 1 (index 0 → 1-based), 1 → 2, 2 →3.

exit_pos:

2 →1 (index 0 → 1-based), 3 →2, 1→3.

So exit_sequence is:

for each ray in entry_rays (3,1,2):

3's exit_pos is exit_pos[3] = 2.

1's exit_pos is exit_pos[1] =3.

2's exit_pos is exit_pos[2] =1.

So exit_sequence is [2,3,1]. 

negated is [-2,-3,-1]. 

Processing:

-2 → list is [-2]

-3 is less than -2 → find first >= -3. In list [-2], -3 < -2 → index 0. Replace → list becomes [-3].

-1 is larger than -3 → append. list is [-3, -1]. Length is 2. 

Which matches the sample output. 

So the code works. 

Now, implementing this in Python.

But for n up to 1e6, the code must be efficient. 

But using the bisect module's bisect_left function is O(n log n), which is acceptable. 

But in Python, list appends and replaces are O(1) for appends, and O(1) for replacing elements. 

So the code should handle 1e6 elements. 

Now, code:

We need to read the entry and exit lines, create entry_pos and exit_pos arrays. 

But in Python, for n=1e6, using a list of size n+1 (since rays are 1-based) is acceptable. 

Then, processing each ray in the entry_rays list, getting their exit position. 

So the code steps:

Read n.

Read entry_rays (n elements).

Read exit_rays (n elements).

Create entry_pos as [0]*(n+1). For each index in 0..n-1, entry_pos[entry_rays[index]] = index+1.

Similarly for exit_pos.

Then, create exit_sequence as [exit_pos[r] for r in entry_rays].

Then, negate each element.

Then, compute the LIS of the negated list. 

So the code:

import bisect

n = int(input())
entry_rays = list(map(int, input().split()))
exit_rays = list(map(int, input().split()))

entry_pos = [0] * (n + 1)
for idx in range(n):
    r = entry_rays[idx]
    entry_pos[r] = idx + 1

exit_pos = [0] * (n + 1)
for idx in range(n):
    r = exit_rays[idx]
    exit_pos[r] = idx + 1

exit_sequence = [exit_pos[r] for r in entry_rays]
negated = [-x for x in exit_sequence]

lis = []
for num in negated:
    idx = bisect.bisect_left(lis, num)
    if idx < len(lis):
        lis[idx] = num
    else:
        lis.append(num)

print(len(lis))

Yes, that's the code. 

Testing the sample inputs:

First sample:

5

1 4 5 2 3

3 4 2 1 5

exit_sequence would be for each entry_rays element:

1 → exit_pos[1] =4.

4 → exit_pos[4] =2.

5 → exit_pos[5] =5.

2 → exit_pos[2] =3.

3 → exit_pos[3] =1.

So exit_sequence is [4,2,5,3,1]. 

negated is [-4,-2,-5,-3,-1].

Processing as above gives lis length 3. 

Second sample:

3

3 1 2

2 3 1

entry_rays is [3,1,2].

exit_rays is [2,3,1].

entry_pos[3] =1, entry_pos[1]=2, entry_pos[2]=3.

exit_pos[2] =1, exit_pos[3] =2, exit_pos[1] =3.

exit_sequence is [2,3,1]. 

negated is [-2,-3,-1]. 

Processing gives lis of length 2. 

So the code works. 

Now, check for possible optimizations. 

For example, using sys.stdin for faster input. 

In the code, input() is used. But for large n, using sys.stdin.readline() is better. 

So, modifying the code:

import sys
import bisect

n = int(sys.stdin.readline())
entry_rays = list(map(int, sys.stdin.readline().split()))
exit_rays = list(map(int, sys.stdin.readline().split()))

entry_pos = [0] * (n + 1)
for idx in range(n):
    r = entry_rays[idx]
    entry_pos[r] = idx + 1

exit_pos = [0] * (n + 1)
for idx in range(n):
    r = exit_rays[idx]
    exit_pos[r] = idx + 1

exit_sequence = [exit_pos[r] for r in entry_rays]
negated = [-x for x in exit_sequence]

lis = []
for num in negated:
    idx = bisect.bisect_left(lis, num)
    if idx < len(lis):
        lis[idx] = num
    else:
        lis.append(num)

print(len(lis))

This should be faster for large input. 

Thus, the code should handle all test cases within the time constraints.
</think>

```python
import sys
import bisect

n = int(sys.stdin.readline())
entry_rays = list(map(int, sys.stdin.readline().split()))
exit_rays = list(map(int, sys.stdin.readline().split()))

entry_pos = [0] * (n + 1)
for idx in range(n):
    r = entry_rays[idx]
    entry_pos[r] = idx + 1

exit_pos = [0] * (n + 1)
for idx in range(n):
    r = exit_rays[idx]
    exit_pos[r] = idx + 1

exit_sequence = [exit_pos[r] for r in entry_rays]
negated = [-x for x in exit_sequence]

lis = []
for num in negated:
    idx = bisect.bisect_left(lis, num)
    if idx < len(lis):
        lis[idx] = num
    else:
        lis.append(num)

print(len(lis))
```