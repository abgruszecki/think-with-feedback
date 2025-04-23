<think>
Okay, let's tackle this problem. So the problem is about students exchanging books based on their best friends. Each day, every student gives their book to their best friend. After k days, we need to determine where each initial book ends up.

Hmm. Let's think about what's happening here. Each student's best friend forms a permutation. Because each student has exactly one best friend, and all are part of a cycle. So the permutation can be broken down into cycles. For example, if student 1 gives to 2, who gives to 3, who gives to 1, that's a cycle of length 3.

Now, the key is that after k steps, each book moves k times along the cycle. So for each cycle, the position after k steps can be determined by k mod the cycle's length. Because after moving cycle_length steps, the book returns to its original position.

So the approach here is to:

1. Find all the cycles in the permutation given by the best friend list.
2. For each cycle, determine where each element in the cycle ends up after k steps. Then, for each position in the cycle, the initial book at position i will end up at the position (i's index in the cycle + k) mod cycle_length.

But wait, how do we model the permutation here? The best friend list is given such that a_i is the best friend of i. Wait, the problem statement says, "ai is equal to the number of the pupil who has the best friend with the number i." Wait, that's a bit confusing. Let me re-read that.

Ah, yes: the second line contains n integers ai, where ai is the pupil who is the best friend of pupil i. Wait, no. Wait, the problem says: "ai is equal to the number of the pupil who has the best friend with the number i." So wait, if ai is the pupil who's best friend is i. Wait, that's a bit tricky. Let me parse this again.

Original problem statement: ai is equal to the number of the pupil who has the best friend with the number i. So for example, if a_1 is 2, that means the best friend of pupil 2 is pupil 1. Because pupil 2's best friend is i=1. So the array a represents the inverse of the permutation. Because normally, if the best friend of i is j, then in a permutation, j = f(i). But here, the array a is such that a_i = j implies that j's best friend is i, i.e., f(j) = i.

Wait, this might be a source of confusion. Let's clarify.

Suppose the array a is given. For each i, a_i is the pupil who has best friend i. So, if a_1 is 2, that means pupil 2's best friend is 1. Because a_i is the pupil (j) whose best friend is i. So j's best friend is i. So the permutation here is j's best friend is i. So the permutation function is f(j) = i when a_i = j.

Wait, no. Let's take the first sample input:

Sample Input 1:
4 1
2 4 1 3

Sample Output:
3 1 4 2

In the note, it says that:

- pupil 3 is the best friend of 1.
- pupil 1 is the best friend of 2.
- pupil 4 is the best friend of 3.
- pupil 2 is the best friend of 4.

So the best friend array is: for each pupil i, their best friend is someone. Let's see:

Pupil 1's best friend is 3 (because a_3 is 1? Wait the array a is [2,4,1,3]. So a[1] is 2, which means that pupil 2's best friend is 1. So for pupil 2, their best friend is 1. Similarly, a[2] is 4: pupil 4's best friend is 2. a[3] is 1: pupil 1's best friend is 3. a[4] is 3: pupil 3's best friend is 4. Wait, that's not possible. Because then the best friends form a cycle.

Wait, perhaps the best friend array is a permutation where each a_i is the best friend of i. Wait, no, because according to the problem statement, "ai is equal to the number of the pupil who has the best friend with the number i." So for example, a_1 is the pupil whose best friend is i=1. So for the first sample, the array is [2,4,1,3]. So:

a_1 = 2: pupil 2's best friend is 1.

a_2 =4: pupil4's best friend is 2.

a_3=1: pupil1's best friend is3.

a_4=3: pupil3's best friend is4.

Wait, that can't be. Because then pupil1's best friend is3 (since a_3=1), and pupil2's best friend is1 (since a_1=2). So the best friends are:

1's best friend is 3.

3's best friend is4.

4's best friend is3? No, wait a_3=1 implies that pupil1's best friend is3. a_4=3 implies that pupil3's best friend is4.

Wait, this is getting confusing. Let's re-examine the note of the first sample input.

The note says:

The list of the best friends equals to {2,4,1,3}. It means that:

- the pupil with the number 3 — is the best friend of pupil 1,

So pupil 1's best friend is 3. Then, according to the note:

pupil 3's best friend is1's best friend? Or wait, the list is {2,4,1,3} — which is the a array. So the a array is [2,4,1,3], which is the input.

The note explains:

In the list, for each i, a_i is the best friend of i's best friend. Wait, no. Let me see:

The note says:

- the pupil with the number 3 is the best friend of pupil 1. So pupil1's best friend is3. Then, a_i for i=3 would be 1. Because a_i is the pupil who has the best friend i. So if pupil3's best friend is1, then a_1 is3? No, the array is given as [2,4,1,3].

Wait, I think there's confusion here. Let's re-express the problem statement.

The input array is such that for each i (1-based), a_i is the number of the pupil who is the best friend of i. Wait, no. The problem statement says:

"ai is equal to the number of the pupil who has the best friend with the number i."

So, a_i = j implies that j's best friend is i.

Ah! So j is a pupil, and j's best friend is i. So the best friend of j is i. So for example, in the first sample, the a array is [2,4,1,3]. So for i=1, a_1 is 2. That means j=2's best friend is 1. So j=2's best friend is i=1. So 2's best friend is 1. Similarly, i=2's a_i is4: j=4's best friend is 2. And so on.

So the best friend structure is defined as follows: for each pupil j, their best friend is given by the inverse of the a array. Because a_i is j, which means j's best friend is i. So the best friend of j is i. So the mapping from j to i is the best friend of j is i. So to get the best friend of j, we need to find the i where a_i = j. Because a_i = j implies j's best friend is i.

Wait, no. Let's think again.

If a_i is j, that means that j's best friend is i. So the best friend of j is i. So the best friend function is: for each j, best_friend(j) = i where a_i = j.

Wait, but how to get the best friend for each j? Because the a array is given as follows: for each i (from 1 to n), a_i is j, which indicates that j's best friend is i. So for j, their best friend is i where a_i = j. So for example, to find the best friend of j, we need to find the i such that a_i = j.

Wait, but that's not directly possible unless we build a reverse map. So the best friend of j is the i where a_i = j. So j's best friend is i. So the best friend function is best_friend[j] = the i for which a_i = j.

So to model the permutation, the best friend of each pupil j is the index i where a_i = j.

Wait, but how can we find that efficiently? Because given the a array, which is a permutation (since each pupil is the best friend of exactly one other), we need to create a reverse mapping. For example, if a is [2,4,1,3], then for j=2, the i where a_i=2 is 1. Because a_1 is 2, so best friend of j=2 is 1.

Wait, perhaps the best way to model the permutation is to create an array f where f[j] is the best friend of j. So for each j, f[j] is the i such that a_i = j. Because a_i is j's best friend is i. So for j to find their best friend, we look for the i in a's array where a_i is j. So the array f can be constructed by inverting the a array. For example:

If a = [2,4,1,3], then:

Looking for j's best friend:

- For j=1, find i where a_i =1. a_3 is 1. So f[1] =3.

- For j=2, find i where a_i=2. a_1 is 2. So f[2] =1.

- j=3: find i where a_i=3. a_4 is3. So f[3] =4.

- j=4: a_i=4. a_2 is4. So f[4]=2.

So the best friend array f would be [3,1,4,2]. So when a pupil gives their book to their best friend, each day, the book moves according to f. So the permutation is given by f.

So, for the problem, the permutation to model is f, which is the inverse of the a array. So given a, the permutation f is constructed by f[j] = i if a[i] = j.

So the first step is to create the permutation f, which is the inverse of the a array. Because each a_i is the j for which f[j] = i.

Once we have f, the problem becomes: after k steps, where each step is moving according to f, what is the final position of each element. For example, the initial position is each student i has their own book. After each day, each student passes their book to f[i], which is their best friend. So after k days, the book that started at i will be at f^k(i), where f^k is the function applied k times.

So to model this, we can decompose the permutation f into cycles. For each cycle of length m, the position of a book after k steps is (current position in cycle +k) mod m steps ahead.

So the algorithm steps are:

1. Precompute the permutation f from the input a. Since a is a permutation (as per the problem statement, each pupil is the best friend of exactly one other), f will be a permutation as well.

2. Decompose f into cycles.

3. For each cycle, compute the effective shift as k modulo the cycle's length. Because after m steps, the cycle repeats.

4. For each element in a cycle, determine its position after shifting by k steps. Then, the initial book at position i will be at the position in the cycle that is (original index in cycle + k) mod m steps ahead.

Wait, but wait. Let's say a cycle is [1,3,4], length 3. After 1 step, each element moves to their next position. So 1 →3, 3→4,4→1. So after k steps, the position of the book that started at 1 is (0 +k) mod 3 steps ahead. So for k=1, it's at index 1 (3), for k=2, index 2 (4), for k=3, index 0 (1 again). So yes, the shift is k mod m.

So for each cycle, after k steps, each element's book will have moved (k) steps in the cycle. So for the cycle's elements, the result is a rotation by k mod m steps.

So the steps are:

For each cycle in f's permutation:

- For each element in the cycle, compute the new index in the cycle as (original index +k) mod m.

- The book that was originally at element x (which is at index i in the cycle) will end up at the element at index (i +k) mod m.

So the plan is:

- For each cycle in f's permutation:

   - Determine the length m.

   - Compute shift = k mod m.

   - For each element in the cycle, the destination after k steps is the element that is shift steps ahead in the cycle.

So, for example, in the first sample input:

a is [2,4,1,3]. The inverse gives f as [3,1,4,2].

So the permutation f is:

1 →3

3 →4

4 →2

2 →1

Which forms a cycle: 1 →3 →4 →2 →1. Wait, that's a cycle of length 4. Wait, let's see:

Starting with 1: next is 3. Then 3's next is4. 4's next is2. 2's next is1. So the cycle is 1-3-4-2, length 4.

In the first sample, k is 1. So after 1 step, each book moves once. So the book starting at 1 moves to3. But in the output, the first element is 3. Which matches the sample. So this approach seems correct.

So the problem reduces to:

- For each element i, find the cycle it is in, compute the shift (k mod m), and determine where the book ends up.

But how to model this? Let's think about building a result array where res[i] is the pupil who has the original book of i after k days.

Wait, no. Wait, the problem statement says: the output is n integers where the i-th integer is the pupil who has the book that the pupil i had initially. So, for example, after k days, the book that was with i at day 0 is now with res[i].

So to model this, we need to compute for each i, where the book that started at i is after k steps.

But when we apply the permutation f once, each book moves to f[i]. So after k steps, the book from i is at f^k(i), where f^k is the permutation applied k times.

But to compute res[i], it's the position of the book that started at i after k steps. So res[i] = f^k(i).

But how to compute this efficiently.

An alternative way: for each cycle, for each element x in the cycle, after k steps, the book that was at x is at the element that is k steps ahead in the cycle. So for each cycle, for each x in the cycle, the res[x] is the element that is (pos(x) +k) mod m steps ahead in the cycle. Here, pos(x) is the index of x in the cycle (0-based).

Wait, let's see. For example, in a cycle of [x1, x2, x3], each step moves the book to the next element. So after k steps, the book from x1 is at x_{(0 +k) mod 3}. So for k=1, it's x2. For k=2, x3. For k=3, x1 again.

Yes. So for the cycle [x0, x1, ..., xm-1], the book from x_i will be at x_{(i +k) mod m} after k steps. So res[x_i] = x_{(i +k) mod m}.

But the permutation f is such that each step is applying f. So to find where a book starting at x_i ends up after k steps, it's equivalent to moving k steps along the cycle.

So the steps to compute the result are:

1. For each element in the permutation, find which cycle it's in and the cycle's length.

2. For each cycle, compute the effective shift (k mod cycle_length).

3. For each element x in the cycle, compute the new position as (current index in cycle + shift) mod cycle_length. The new element in the cycle is then the one at that new index. So, for example, the cycle is stored as a list, and for each x in the cycle, the new position is determined by the shifted index.

Once we have that, the result array can be filled.

Now, the problem is to implement this efficiently, given that n can be up to 1e5 and k up to 1e16.

So, the steps in code:

First, compute the permutation f from the a array. Since a is given as a list where a_i is the pupil who's best friend is i. So f[j] = i where a_i = j. So to compute f, for each j in 1..n, find i such that a_i = j. But since a is a permutation (since each pupil has exactly one best friend, and each is a best friend of exactly one other), the a array is a permutation. So the inverse of the a array gives the f array.

So for example, if a is [2,4,1,3], then:

a[1] =2 → so j=2's best friend is 1. So f[2] =1.

a[2] =4 → j=4's best friend is2 → f[4] =2.

a[3] =1 → j=1's best friend is3 →f[1] =3.

a[4] =3 → j=3's best friend is4 →f[3] =4.

So f is [3,1,4,2] (assuming 1-based index). So f is built as follows:

for i in 1..n:

   j = a[i]

   f[j] = i

Because a[i] is the j where the best friend of j is i. So f[j] =i.

Yes.

So building f can be done as follows:

f = [0]*(n+1)  # since pupils are 1-based.

for i in 1..n:

   j = a[i]

   f[j] = i

Once f is built, then decompose f into cycles.

Now, the challenge is to find cycles efficiently. For n up to 1e5, we can do this with a visited array.

Once we have the cycles, for each cycle, compute the shift as k mod len(cycle). Then for each element in the cycle, compute the new position.

But how to track the result.

The result array res is such that res[i] is the pupil who holds the book that started with i after k days.

So for each cycle, for each x in the cycle, the book from x will be at the element that is (pos_in_cycle +k) mod cycle_length steps ahead. So, for example, the cycle is [x0, x1, x2], shift is 2. Then the book from x0 is at x2 (0+2 mod 3=2), x1 is at x0 (1+2=3 mod3=0), etc.

Thus, for each cycle, we can precompute the shifted positions.

So in code:

visited = [False] * (n+1)

res = [0]*(n+1)

for i in 1 to n:

   if not visited[i]:

       # find the cycle starting at i

       cycle = []

       current = i

       while not visited[current]:

           visited[current] = True

           cycle.append(current)

           current = f[current]

       m = len(cycle)

       shift = k % m

       for idx in 0 to m-1:

           original_pos = idx

           new_pos = (idx + shift) % m

           # the book that was at cycle[original_pos] is now at cycle[new_pos]

           res[cycle[original_pos]] = cycle[new_pos]

So for each element x in the cycle, res[x] is set to the element in the cycle that is shift steps ahead.

Yes.

This should work.

Now, let's test this logic with the first sample.

Sample 1:

n=4, k=1.

a = [2,4,1,3]

Building f:

for i=1, a[i] =2 → f[2] =1.

i=2, a[i]=4 → f[4]=2.

i=3, a[i]=1 →f[1]=3.

i=4, a[i]=3 →f[3]=4.

So f is [0,3,1,4,2]. Because:

f[1] =3, f[2]=1, f[3]=4, f[4]=2.

So the permutation f is 1 →3 →4 →2 →1. So the cycle is [1,3,4,2], length 4.

Shift is 1 mod4=1.

So for each element in the cycle:

original_pos (index) and new_pos:

0 →0+1=1 →3 is in index 1 (cycle[1] is3).

Wait, no: the cycle is [1,3,4,2].

Wait, no. Let's see. When we start with i=1:

current =1, added to cycle.

current =f[1] =3 →added.

current =f[3]=4 →added.

current =f[4] =2 →added.

current =f[2]=1 →already visited.

So cycle is [1,3,4,2], length 4.

Shift is 1 mod4=1.

For each element in the cycle:

original_pos is 0 (for 1), new_pos=0+1=1 mod4 →1. So res[1] = cycle[1] =3.

For element 3 (original_pos=1), new_pos=1+1=2 →4. So res[3] =4.

For element4 (original_pos=2), new_pos=2+1=3 mod4 →3 →2. res[4]=2.

For element2 (original_pos=3), new_pos=3+1=4 mod4=0 →1. res[2] =1.

Thus, the res array is:

res[1] =3, res[2]=1, res[3]=4, res[4]=2.

Which matches the sample output: 3 1 4 2.

So the logic works.

Another sample: sample 2.

Sample 2:

5 5

3 4 5 2 1

So a = [3,4,5,2,1]. So building f:

for each i from1 to5:

i=1 →a[1] =3 →j=3 →f[3]=1.

i=2 →a[2]=4 →f[4] =2.

i=3 →a[3]=5 →f[5]=3.

i=4 →a[4]=2 →f[2]=4.

i=5 →a[5]=1 →f[1]=5.

So f is [5,4,1,2,3].

So the permutation is:

1 →5 →3 →1 (cycle length 3).

2 →4 →2 (cycle length 2).

So for k=5:

Cycle 1: [1,5,3], length 3. Shift =5 mod3=2.

So each element's new pos is (idx +2) mod3.

For idx=0: 0+2=2 →3 → cycle[2] is3.

Wait, the cycle list for the first cycle would be [1,5,3]. So:

idx 0: 1 → new_pos 0+2=2 →3.

So res[1] =3.

idx1:5 → new_pos 1+2=3 mod3=0 →1. So res[5]=1.

idx2:3 → new_pos 2+2=4 mod3=1 →5. res[3]=5.

Then cycle 2: [2,4], shift=5 mod2=1.

idx0:2 →0+1=1 →4. res[2]=4.

idx1:4 →1+1=2 mod2=0 →2. res[4]=2.

So the res array is:

res[1]=3, res[2]=4, res[3]=5, res[4]=2, res[5]=1.

Which gives the output 3 4 5 2 1. Which matches sample 2.

Sample 3:

n=6, k=18.

a is [2,3,5,1,6,4].

Building f:

for i=1: a[1]=2 →f[2]=1.

i=2: a[2]=3 →f[3]=2.

i=3: a[3]=5 →f[5]=3.

i=4: a[4]=1 →f[1]=4.

i=5: a[5]=6 →f[6]=5.

i=6: a[6]=4 →f[4]=6.

So f is [4,1,2,6,3,5].

So permutation:

1 →4 →6 →5 →3 →2 →1.

So the cycle is 1,4,6,5,3,2. Length 6.

Shift is 18 mod6=0. So each element's new pos is same as original. So res[i] =i for all. So output is 1 2 3 4 5 6. Which matches sample 3.

So the logic works.

Now, the code needs to be written.

First, read n and k.

Then read the a array (note that the input is 1-based? Because the problem says the second line contains n different integers ai (1 ≤ ai ≤n), where ai is equal to the number of the pupil who has the best friend i.

So a is 1-based? Wait, the input is given as a list of n integers, which are 1-based. For example, in sample 1, the input line is "2 4 1 3". So the first element is a_1, which is 2.

So in Python, the a list can be read as a list of integers, then we process each index i (1-based) to get a[i], then set f[a[i]] =i.

So in code:

n, k = map(int, input().split())

a = list(map(int, input().split()))

But note that in Python, the list is 0-based. So the first element in a (index 0) is a_1. Wait, no. Let's see:

Input line is "2 4 1 3" for sample 1. This is a list of a_1 to a_4, since n=4. So the list is [2,4,1,3]. So for i in 1..4, a[i-1] is the value of a_i.

So to build f:

f = [0]*(n+1)

for i in range(1, n+1):

    j = a[i-1]

    f[j] = i

Then, decompose f into cycles.

Once the cycles are found, compute shift for each cycle, and set res.

Implementing this.

Now, considering n can be up to 1e5, this approach is O(n), which is acceptable.

Now, code:

Read n, k.

Read a as list.

Build f.

Then, for each unvisited node, find the cycle.

Compute shift, and assign res[x] = cycle[(pos + shift) % len(cycle)].

Now, code.

Now, code in Python:

Read input:

n, k = map(int, input().split())

a = list(map(int, input().split()))

Build f:

f = [0] * (n + 1)

for i in range(1, n+1):

    j = a[i-1]

    f[j] = i

Then, find cycles.

visited = [False] * (n+1)

res = [0]*(n+1)

for i in range(1, n+1):

    if not visited[i]:

        cycle = []

        current = i

        while not visited[current]:

            visited[current] = True

            cycle.append(current)

            current = f[current]

        m = len(cycle)

        shift = k % m

        for idx in range(m):

            new_pos = (idx + shift) % m

            res[cycle[idx]] = cycle[new_pos]

Finally, output res[1], res[2], ..., res[n], space-separated.

So the code would be:

n, k = map(int, input().split())

a = list(map(int, input().split()))

f = [0]*(n+1)

for i in range(n):

    # i is 0-based in the list a, representing i+1-th pupil.

    # a[i] is the value of a_{i+1}, which is j where j's best friend is i+1.

    # So f[j] = i+1.

    j = a[i]

    f[j] = i+1

visited = [False]*(n+1)

res = [0]*(n+1)

for i in range(1, n+1):

    if not visited[i]:

        cycle = []

        current = i

        while not visited[current]:

            visited[current] = True

            cycle.append(current)

            current = f[current]

        m = len(cycle)

        shift = k % m

        for idx in range(m):

            new_idx = (idx + shift) % m

            res[cycle[idx]] = cycle[new_idx]

print(' '.join(map(str, res[1:n+1])))

Testing this code against sample 1:

Sample 1 input:

4 1

2 4 1 3

In code:

a = [2,4,1,3]

Building f:

i in 0-based loop from 0 to 3 (since n=4).

For i=0 (pupil 1):

j = a[0] =2 →f[2] =1.

i=1 (pupil 2):

a[1]=4 →f[4] =2.

i=2 (pupil3):

a[2] =1 →f[1] =3.

i=3 (pupil4):

a[3] =3 →f[3]=4.

So f is [0,3,1,4,2].

Then, cycles:

Starting with 1, which is unvisited.

current=1, add to cycle, mark visited. current becomes f[1]=3.

current=3: add to cycle. current becomes f[3]=4.

current=4: add to cycle. current becomes f[4]=2.

current=2: add to cycle. current becomes f[2]=1, which is visited.

Cycle is [1,3,4,2], m=4.

shift=1 mod4=1.

For each idx in 0-3:

new_idx = idx+1 mod4.

res[1] =3 (cycle[1]).

res[3] =4 (cycle[2]).

res[4] =2 (cycle[3]).

res[2] =1 (cycle[0 mod4=0 →cycle[0] is1).

So res is [0,3,1,4,2, ...], but in the output, res[1..4] is 3,1,4,2 → which matches sample.

So code works.

Another sample, sample 3:

n=6, k=18.

a is [2,3,5,1,6,4].

Building f:

i ranges from 0 to5.

i=0 (pupil1):

a[0] =2 →f[2] =1.

i=1 (pupil2):

a[1] =3 →f[3] =2.

i=2 (pupil3):

a[2] =5 →f[5] =3.

i=3 (pupil4):

a[3] =1 →f[1] =4.

i=4 (pupil5):

a[4] =6 →f[6] =5.

i=5 (pupil6):

a[5] =4 →f[4] =6.

So f array is:

0-based indexes:

f[0] =0 (unused).

f[1] =4.

f[2] =1.

f[3] =2.

f[4] =6.

f[5] =3.

f[6] =5.

So the permutation is:

1 →4 →6 →5 →3 →2 →1.

Cycle length is 6. shift is 18 mod6=0.

Thus, each element's new position is same as original. So res[i] =i.

Thus, output is 1 2 3 4 5 6.

Which matches sample3.

Thus, the code should be correct.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))

f = [0] * (n + 1)
for i in range(n):
    j = a[i]
    f[j] = i + 1

visited = [False] * (n + 1)
res = [0] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        cycle = []
        current = i
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = f[current]
        m = len(cycle)
        shift = k % m
        for idx in range(m):
            new_idx = (idx + shift) % m
            res[cycle[idx]] = cycle[new_idx]

print(' '.join(map(str, res[1:n+1])))
```