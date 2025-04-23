<think>
Okay, let's see. The problem is to select students from two rows such that no two consecutive are from the same row, and their indices are strictly increasing. The goal is to maximize the sum of their heights. Hmm.

So the constraints are that after choosing a student from a row, the next must be from the other row and have a higher index. And the indices must be strictly increasing. So the order of selection must follow the index order, and alternate rows.

Wait, the problem says that the indices of each chosen player (excluding the first) must be strictly greater than the previous. So the indices are in strictly increasing order, and the rows alternate. For example, if the first chosen is from row 1 index 2, the next can be row 2 index 3, then row 1 index 4, etc.

So the problem resembles a dynamic programming problem where at each step, we track the last row chosen and the current index, and decide whether to pick the next from the other row with a higher index.

But considering the size of n (up to 1e5), a naive DP approach with O(n^2) time is impossible. So we need a way to model this with O(n) or O(n log n) time.

Let's think about dynamic programming. Let's define two arrays:

dp1[i] = the maximum total height achievable up to index i, where the last selected student is from row 1 and ends at index i.

dp2[i] = same, but last is from row 2.

But even this might not work directly because for each i, we need to look at all previous j < i in the other row. Wait, but perhaps we can model it in a way that for each position, we track the best possible up to that index for each row.

Alternatively, since the indices must be strictly increasing, maybe the DP can track the maximum possible sum when ending at a particular index in row 1 or row 2. For each i, the best for row 1 at i would be the maximum of the best for row 2 up to i-1 plus h1[i], or possibly just taking h1[i] alone. Similarly for row 2.

Wait, here's an idea: for each position i (from 1 to n), we can track the maximum sum if we end at i in row 1, or row 2.

So for each i, the maximum for row1 would be the maximum between (taking h1[i] alone) or (max from row2 up to j < i) + h1[i]. Similarly for row2.

But how do we track the max from the other row up to j < i? Because when considering position i, the previous step could be any j < i in the other row. So for row1[i], the maximum would be h1[i] + max of all row2[j] for j < i.

But if we can keep track of the maximum of row2 up to j < i, then we can calculate row1[i] as h1[i] + max_prev_row2, where max_prev_row2 is the maximum of row2[0..i-1]. Similarly, row2[i] would be h2[i] + max_prev_row1.

But then, for each i, we need to keep track of the maximum values from the other row up to i-1. Let's think:

Initialize max1 and max2 as 0. As we process each i from 1 to n:

row1[i] = h1[i] + max_prev_row2 (which is the max of all row2 up to i-1)
row2[i] = h2[i] + max_prev_row1 (the max of all row1 up to i-1)

Then, we update max_prev_row1 and max_prev_row2 with the new row1[i] and row2[i], but wait, no. Because when we process i, the previous max for row2 is the maximum of all row2[j] where j < i. So as we iterate from left to right, for each i, before processing it, we have the maximum of row1 and row2 up to i-1.

Wait, perhaps the approach is to track two variables, say, best_other_row1 and best_other_row2, which represent the maximum sum achievable when ending in row1 or row2 up to the current position.

Wait, maybe the DP can be:

At each step i (the current index), we can choose to take row1[i] or row2[i]. But the choice depends on the previous selection being from the other row.

But how to model this. Let's think of two variables: prev_row1 and prev_row2. prev_row1 is the maximum sum when the last taken is from row1 and at index <= i. Similarly for prev_row2.

Wait, perhaps not. Let me think again.

Let's model the DP as follows:

For each index i (starting from 1 to n), we can decide whether to take row1[i] or row2[i], but only if the previous was taken from the other row. However, since the indices must be strictly increasing, the previous selection must have been from an index j < i. But since we process i in order, perhaps we can track the maximum possible up to i-1 for each row.

So for i-th index:

current_row1 = h1[i] + max_prev_row2
current_row2 = h2[i] + max_prev_row1

Where max_prev_row2 is the maximum of all dp2[j] where j < i. Similarly for max_prev_row1.

But how do we track these max_prev values?

We can keep track of two variables, max1 and max2. Initially, they are 0. For each i from 1 to n:

current_row1 = h1[i] + max2
current_row2 = h2[i] + max1

Then, we update max1 and max2 as the maximum between their previous value and current_row1/current_row2.

Wait, no. Because after processing i, the new max1 would be the maximum between the old max1 and current_row1. Similarly for max2.

Wait, let's see:

At each step i, the maximum possible when choosing to end at row1[i] is current_row1 = h1[i] + max2_prev, where max2_prev is the maximum of all dp2 up to i-1.

Similarly, current_row2 = h2[i] + max1_prev.

But after processing i, the new max1 would be the maximum between the previous max1 and current_row1 (since current_row1 could be a better option for future steps). Similarly for max2.

Wait, but for i=1:

max1_prev is 0 (since nothing before), so current_row1 is h1[1] + 0. Then, max1 becomes max(0, current_row1) = current_row1.

For i=2:

current_row1 = h1[2] + max2_prev (which is max2 after i=1, which was 0 if we didn't take row2 in i=1).

But how do the max variables work here?

Let's see with the first example:

Sample Input 1:

5

9 3 5 7 3

5 8 1 4 5

So for each i from 1 to 5:

i=1:

current_row1 = 9 + max2_prev (0) =9

current_row2 =5 + max1_prev (0) =5

max1 becomes max(0,9) =9

max2 becomes max(0,5)=5

i=2:

current_row1 =3 + max2_prev (5) =8

current_row2=8 + max1_prev (9) =17

max1 becomes max(9,8)=9 (unchanged)

max2 becomes max(5,17) =17

i=3:

current_row1 =5 + max2_prev (17) =22

current_row2=1 + max1_prev (9) =10

max1 is now max(9,22)=22

max2 is max(17,10) =17.

i=4:

current_row1 =7 + 17 =24

current_row2=4 +22=26.

max1 is max(22,24)=24

max2 is max(17,26)=26.

i=5:

current_row1=3 +26=29

current_row2=5 +24=29.

max1 becomes max(24,29)=29

max2 becomes max(26,29)=29.

At the end, the maximum between max1 and max2 is 29, which matches the sample output.

So this approach works.

So the algorithm is:

- Keep track of two variables, max1 and max2, which represent the maximum sum achievable up to the current index, ending in row1 or row2 respectively.

- For each i from 0 to n-1 (assuming 0-based or 1-based arrays?), we compute the current_row1 and current_row2 as h1[i] + max2_prev and h2[i] + max1_prev. Then, update max1 and max2 as the maximum between their previous value and current_row1/current_row2.

Wait, but in this approach, the indices are processed in order, and for each i, we can take the current h1[i] and h2[i], and combine with the max from the other row up to the previous steps.

So the variables max1 and max2 represent the maximum sum achievable when ending in row1 or row2, considering all indices up to the current i.

Wait, but initially, max1 and max2 are 0. For i=0 (assuming 0-based), current_row1 = h1[0] + max2 (0) → which is the sum when taking only row1[0]. Similarly for row2. Then, after processing i=0, max1 is h1[0], max2 is h2[0]. Then for i=1, the current_row1 is h1[1] + max2 (which is h2[0] if that's better than other possibilities). Wait, but if the first taken is row1[1], the previous must be from row2 and index <1. But in the first step, after processing i=0, the max1 is h1[0], max2 is h2[0]. Then, when i=1:

current_row1 = h1[1] + max2_prev (which is the max2 up to i=0, which is h2[0])

current_row2 = h2[1] + max1_prev (h1[0])

Then, the new max1 is the maximum between the previous max1 (h1[0]) and current_row1 (h1[1]+h2[0]).

So yes, this approach correctly builds up the maximum possibilities.

Thus, the steps are:

Initialize max1 and max2 to 0.

For each i in 0 to n-1:

   current1 = h1[i] + max2_prev

   current2 = h2[i] + max1_prev

   new_max1 = max(max1_prev, current1)

   new_max2 = max(max2_prev, current2)

   max1, max2 = new_max1, new_max2

After processing all, the answer is max(max1, max2).

Wait, but in the first step (i=0), current1 is h1[0] + 0 (since max2_prev is 0 initially). That's correct because we can take row1[0] as the first element. Similarly for row2[0]. Then, the max1 after i=0 is the maximum between 0 and current1, which is h1[0]. Similarly for max2.

So, this approach accumulates the maximum possible sum for each row, considering that the last selected is from that row. The key is that for each step, the current selection can either start a new sequence (taking just h1[i] if that's better than any previous sequence ending in row1) or add to the best possible sequence from the other row.

Wait, but in the code, the max1 and max2 are the maximum up to that index. So for example, if h1[i] is very large, but max2_prev is small, then current1 would be h1[i] + max2_prev, but if that's less than the current max1, then the new max1 remains as previous. But that's correct because maybe taking previous max1 (which could be a sequence that ends at an earlier index in row1) is better than adding the current h1[i] to a previous row2.

Wait, but that's a problem. Because, for example, if the current h1[i] is very large but the previous max2_prev is low. Then current1 would be h1[i] + max2_prev, but maybe there's a better option of not taking the current h1[i], and keeping the previous max1.

But that's exactly what the code does. For example, suppose at index i, the current1 is h1[i] + previous max2. Then, the new max1 is the maximum between the previous max1 (which could be a sum from row1 up to i-1) and current1. So if the previous max1 is higher, then it's better to ignore the current i in row1, and keep the previous max1.

But that's not correct, because the previous max1 could be for a row1 element at j < i. But the problem requires that the next element's index is strictly greater. So, for example, if the previous max1 is for row1 at j < i, then you cannot take row1[i] after that. So this approach is incorrect.

Wait, this is a critical point. Because if the current max1 is the maximum sum for sequences ending in row1 up to i-1, then adding row1[i] as a new start (without any previous selection) is allowed, but sequences that end in row1[i] can only be formed by sequences ending in row2[j] where j < i, then adding row1[i], or starting a new sequence with row1[i].

But the code's current approach is to track the maximum sum for sequences ending in row1 up to current i, but the way it's calculated may allow sequences that include row1[i] as a standalone, but not considering that previous sequences could have higher sums.

Wait, perhaps I'm misunderstanding the code.

Let's think again. The variables max1 and max2 represent the maximum sum achievable when the last selected student is in row1 or row2, respectively, with indices up to i.

So for each i, after processing, max1 is the maximum between the previous max1 (so sequences not including i) and current_row1 (which is sequences including i in row1).

So if the previous max1 is higher than current_row1, then the new max1 remains as the previous max1. That is correct, because taking the sequence that doesn't include i is better.

But this approach allows for the possibility of sequences that skip some indices. For example, the best sequence up to i may not include i.

But according to the problem statement, the selection can be any subset of the students as long as the indices are strictly increasing and the rows alternate. So the sequence can skip indices as needed.

But in the code, the max1 and max2 variables are the maximum possible sum for sequences that end at any index <=i (not necessarily i) in row1 or row2. Because when processing i, the code considers adding row1[i] to the best possible sequence from row2 up to i-1, and then updates max1 to be the maximum between the previous max1 (which could be for a sequence ending at j <i) and current_row1 (which is for sequences ending at i). So this correctly captures the best possible for sequences ending at any index up to i.

Therefore, the code correctly accumulates the maximum sum possible.

Thus, the approach is correct.

Now, let's see how to implement this.

We need to read n, then the two rows.

For each of the n elements, process them in order, keeping track of max1 and max2.

Initialize max1 and max2 to 0.

Then for each i from 0 to n-1:

current1 = h1[i] + max2

current2 = h2[i] + max1

new_max1 = max(max1, current1)

new_max2 = max(max2, current2)

Set max1 and max2 to new_max1 and new_max2.

After processing all elements, the answer is the maximum of max1 and max2.

Yes.

Testing this approach against the sample inputs:

Sample 1:

h1 = [9,3,5,7,3]

h2 = [5,8,1,4,5]

Processing step by step:

Initially max1=0, max2=0.

i=0:

current1 =9 +0=9

current2=5 +0=5

new_max1=9, new_max2=5.

max1=9, max2=5.

i=1:

current1=3 +5=8 → new_max1 = max(9,8)=9.

current2=8 +9=17 → new_max2 = max(5,17)=17.

Now max1=9, max2=17.

i=2:

current1=5 +17=22 → new_max1 max(9,22)=22.

current2=1+9=10 → new_max2 is 17.

max1=22, max2=17.

i=3:

current1=7 +17=24 → new_max1 is max(22,24)=24.

current2=4 +22=26 → new_max2 is max(17,26)=26.

max1=24, max2=26.

i=4:

current1=3+26=29 → new_max1 is max(24,29)=29.

current2=5 +24=29 → new_max2 is max(26,29)=29.

Final max1 and max2 are both 29. Answer is 29. Correct.

Sample 2:

n=3

h1 = [1, 2,9]

h2 = [10,1,1]

Processing:

max1=0, max2=0.

i=0:

current1=1 +0=1 → max1=1

current2=10+0=10 → max2=10.

i=1:

current1=2 +10=12 → new_max1 is max(1,12)=12.

current2=1 +1=2 → new_max2 is max(10,2)=10.

max1=12, max2=10.

i=2:

current1=9 +10=19 → new_max1 is max(12,19)=19.

current2=1 +12=13 → new_max2 is max(10,13)=13.

Final answer is max(19,13) =19. Correct.

Sample 3:

n=1

h1=7, h2=4.

i=0:

current1=7+0=7 → max1=7.

current2=4+0=4 → max2=4.

Answer is 7.

Yes.

So this approach works for all samples.

Now, the code is straightforward. Read n, read h1 and h2 as lists. Initialize max1 and max2 as 0. Iterate through each index, compute current1 and current2, update max1 and max2.

The time complexity is O(n), which is acceptable for n up to 1e5.

Memory-wise, we need to store the two h lists. Since each is 1e5 elements, it's manageable.

So the code in Python would be:

Read n.

Read h1 as list of integers.

Read h2 as list of integers.

Initialize max1 and max2 to 0.

Loop through each i in 0 to n-1:

current1 = h1[i] + max2

current2 = h2[i] + max1

new_max1 = max(max1, current1)

new_max2 = max(max2, current2)

max1, max2 = new_max1, new_max2

After the loop, output max(max1, max2).

But wait, in Python, for large n (1e5), using a loop is okay, as 1e5 iterations are manageable.

Yes.

So the code is as follows.
</think>

```python
n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
max1, max2 = 0, 0
for a, b in zip(h1, h2):
    current1 = a + max2
    current2 = b + max1
    new_max1 = max(max1, current1)
    new_max2 = max(max2, current2)
    max1, max2 = new_max1, new_max2
print(max(max1, max2))
```