<think>
Okay, so I've got this programming problem to solve. Let's read through it carefully. 

The problem is about knights who can kill others. Each knight has a certain power and coins. A knight can kill another if their power is higher. But each can kill at most k others. After killing, they take all the coins of the victims. We need to compute for each knight the maximum coins they can have after killing up to k knights they can defeat.

Hmm. Let's break down the problem. 

First, the key points:

- Each knight can kill others with lower power. 
- The maximum number of kills allowed per knight is k, which can be up to 10.
- For each knight, we need to select up to k knights with lower power (so weaker than them) and choose those that maximize the sum of coins. 

So the steps I need to take are:

1. For each knight, find all knights weaker than them. 
2. Among those, select up to k with the highest coins. Sum their coins along with the knight's own coins.
3. Return this sum for each knight.

But how to do this efficiently, especially considering the constraints where n can be up to 1e5?

Let's think about the constraints. For each knight, if we process all weaker knights and select the top k coins, that could be O(n^2) in the worst case, which is way too slow. So we need a smarter approach.

First, let's sort the knights by their power. Then, for each knight, all the knights before them in the sorted list are weaker. So if we sort the knights in increasing order of power, then for knight i, the first i knights (if there are any) are weaker. 

Wait, no. If the list is sorted in increasing order, then for a knight at position i, all knights before i (positions 0 to i-1) have lower power. So that's correct.

So for each knight i in this sorted list, the possible victims are all knights before i. Now, for each such i, we need to take the top min(k, i) coins from the first i knights, sum them, and add to the knight's own coins.

But how to compute this efficiently?

The idea is to pre-process the coins in a way that allows us to quickly get the sum of the top m elements for each i, where m is up to k. 

Let's consider that once the knights are sorted by power, for each knight i, we have a list of coins of all weaker knights (those before i). We need to keep track of the maximum k coins from this list. 

But if we can maintain a max-heap or a sorted list that allows us to track the top k elements as we go through each knight in the sorted order, that could work. 

Wait, here's an approach:

1. Sort all knights by their power in ascending order. So, the order is from weakest to strongest.
2. For each knight in this sorted list, as we process them, we keep track of the top k coins from all the knights processed so far (i.e., the weaker ones). But wait, no. Because each knight can only kill knights weaker than them, but once we process a knight (say, knight j), any knight that comes after j (in the sorted list) can kill j. So for each knight i (after j), j is a possible victim. 

Wait, the sorted list is in order of increasing power. So for each knight at position i (0-based), all knights from 0 to i-1 are weaker. So when processing knight i, the possible victims are all those in 0 to i-1. 

But for each knight i, when we process them, we can collect all the coins of the previous knights (0 to i-1), and select the top k coins (if there are more than k). Then the sum of these plus the current knight's coins is the answer for this knight. 

But how to efficiently compute the sum of the top k elements among all elements before i? 

We need to process the knights in order, and for each i, track the top k coins from the first i elements. Because once i is processed, the next knight (i+1) can take up to k elements from the first i+1 elements (but wait, no. The next knight can take any of the first i+1 elements (since they are weaker). So for each knight, the coins of all previous knights (including those processed so far) are available. 

Wait, no. Because the sorted list is from weakest to strongest. So when we process the knights in order, each knight can only kill the ones before them. So for knight i, the possible victims are 0 to i-1. So the coins available to pick are those of the knights before i. 

But for knight i, the top k coins would be the maximum sum from any up to k coins from the first i knights (excluding the current knight's coins, but wait no—the current knight's coins are their own. The problem says the sum is their own coins plus the sum of up to k victims. So for each knight, the sum is c_i (their own coins) plus the sum of the top m coins from the victims, where m is the minimum between k and the number of possible victims (i, since before i there are i victims).

So the problem reduces to, for each i in 0..n-1, take the first i elements (the coins of the weaker knights), select up to k of the largest ones, sum them and add to c_i.

So the challenge is to compute for each i, the sum of the largest min(k, i) elements in the first i elements. Then add the current c_i to that sum.

But how to compute this efficiently for all i?

If we can keep a data structure that allows us to track the top k elements as we process each knight in order, then for each knight, we can quickly get the sum of the top min(k, m) elements, where m is the number of elements so far.

So here's the plan:

- Sort the knights in increasing order of power. So the weakest comes first, strongest last.
- For each knight in this sorted list, we need to process their coins and track the top k coins among all coins of the previous knights.
- For each knight i, the sum for the answer is c_i + sum of top min(k, i) coins from the first i knights (but wait, the first i knights include the current knight? No. Because for knight i (0-based), the first i knights are those before him. Because in the sorted list, the knight's position is determined by their power. So the first i knights (0 to i-1) are weaker. So when processing knight i, the previous coins are 0 to i-1.

Wait, no. Let's clarify: when the list is sorted in increasing power, the order is from weakest to strongest. So knight 0 is the weakest, knight n-1 is the strongest. 

So for knight i (sorted in this order), all knights before him (0 to i-1) are weaker. So when processing knight i, the possible victims are 0 to i-1. So for the sum, it's the sum of the top k coins from the coins of 0 to i-1, up to k elements, plus the current coin c[i].

But how do we track the top k coins for each knight up to i-1?

We can maintain a max-heap or a priority queue. But inserting into a heap takes O(logk) time for each element. Wait, but if we have a max-heap of size up to k, then for each new element (the coins of the previous knights), we can add it to the heap if it's larger than the smallest element in the heap (since we can only keep the top k elements). Wait, but perhaps a min-heap would be better here. 

Wait, here's an approach: maintain a min-heap of size up to k. For each new coin value from the previous knights (0 to i-1), we can do the following:

- If the heap has less than k elements, add the coin to the heap. 
- Else, if the current coin is larger than the smallest element in the heap (the top), replace the smallest with this new coin. 
- This way, the heap always contains the top k coins seen so far. 

Then, for each knight i, after processing the coins from 0 to i-1, the sum of the elements in the heap is the sum of the top min(k, i) coins. Because for i elements, we take the top k (if possible). 

But how do we process this incrementally? Let's think:

As we iterate through the sorted list of knights, for each knight i (starting from 0 to n-1):

- Before processing i, we have a heap that contains the top min(k, i) coins from the first i knights (0 to i-1). Wait, no. Because when processing knight i, the coins from 0 to i-1 are already considered. Wait, no. Let's see:

Wait, the sorted list is in order of power. So the first knight (i=0) can't kill anyone (since there are no knights before him). So his sum is just his own coin. 

For knight i=1 (second knight in the sorted list), he can kill the first knight. So if k>=1, the sum is c[1] + sum of the top 1 coins (which is the first knight's coin, if it's positive). 

So the approach is: for each knight i in the sorted list, after processing knights 0 to i-1, we need to have a data structure that allows us to get the sum of the top m coins, where m is min(k, i). 

So the idea is to process the knights in order of increasing power. For each knight, when processing them, add their coins to a structure that keeps track of the top k coins. Then, for the next knights, this structure will already have the top k coins from all previous knights. 

Wait, no. Because when processing knight i, the coins from 0 to i-1 are the possible victims for knight i. But when we process knight i+1, the possible victims are 0 to i, including the i-th knight. So the structure should accumulate all the previous knights' coins as we process them. 

So here's the plan:

1. Sort all knights by their power in increasing order. 
2. Initialize a min-heap (priority queue) to keep track of the top k coins encountered so far. Also, keep a sum variable that tracks the sum of the elements in the heap. 
3. For each knight in the sorted list:
   a. The current knight's maximum coins is their own coins plus the sum of the elements in the heap (since the heap contains up to k elements, which are the top coins from the previous knights). 
   b. Then, add the current knight's coins to the heap (if needed) for future knights (since future knights can kill this knight). 

Wait, no. Because future knights (those with higher power) can kill this knight. So when we process the current knight, we need to add their coins to the data structure so that future knights can consider them as potential victims. 

So for each knight i:

- The answer for i is their own coins plus the sum of the top m elements from the previous knights (0 to i-1), where m is min(k, i). 
- Then, add their coins to the structure so that future knights (i+1, i+2, etc.) can include them as possible victims. 

So the data structure needs to track all coins up to i, but when processing i+1, the data structure includes all coins from 0 to i. 

So here's the correct process:

Initialize a min-heap with maximum size k. Also track the sum of elements in the heap. 

Sort the knights by power in increasing order. 

Then, for each knight in order:

- The answer is c_i plus the sum of the heap (sum_of_heap). Because the heap contains the top min(k, i) coins from the previous knights (0 to i-1). 
- Then, add the current knight's coin to the heap. If the heap has less than k elements, add it. Otherwise, if the current coin is larger than the smallest in the heap (heap[0]), replace the smallest with current coin. Also, update the sum_of_heap accordingly. 

Wait, but when adding the current knight's coin to the heap, that's for the next knights (i+1, etc.) to consider. Because when we process the next knight, they can kill the current knight. So the heap accumulates all coins of the knights processed so far (including the current one), but only the top k. 

So the algorithm would be:

sorted_knights = sorted(zip(p, c), key=lambda x: x[0])

heap = []
sum_heap = 0

answers = [0]*n

for i in range(n):
    current_c = sorted_knights[i][1]
    # The answer for this knight is current_c plus sum_heap
    answers[i] = current_c + sum_heap
    # Now, add current_c to the heap if possible
    if len(heap) < k:
        heapq.heappush(heap, current_c)
        sum_heap += current_c
    else:
        if k > 0:
            if current_c > heap[0]:
                removed = heapq.heappop(heap)
                sum_heap -= removed
                heapq.heappush(heap, current_c)
                sum_heap += current_c
    # Then, for the next knights, the heap contains the top k coins up to this point

But wait, after adding the current knight's coins to the heap, the heap now includes their coins. But the next knight (i+1) will have a higher power, so they can kill this knight. So when processing knight i+1, the heap contains up to k coins from knights 0 to i. So this seems correct. 

Yes, this approach should work. 

Let's test this logic against the examples.

First example:

Input:
4 2
4 5 9 7 → sorted by power would be 4,5,7,9 (since 7 is less than 9). So the sorted order of p is [4,5,7,9]. The coins are [1,2,33,11]. Wait, original c array is [1,2,11,33]. So the sorted list would be:

p:4,5,7,9 → sorted as 4,5,7,9. The c values are 1 (for 4), 2 (for 5), 33 (for 7), 11 (for 9). Wait, no. Wait, original input is:

The second example in the first sample input:

The input is:

4 2

Power:4,5,9,7 → sorted by power would be 4,5,7,9. 

Coins:1,2,11,33. So the sorted c array would be [1,2,33,11] ?

Wait, when the knights are sorted by power (p), their c values are ordered accordingly. So the knights in sorted order are:

Knight 0: p=4, c=1

Knight 1: p=5, c=2

Knight 2: p=7, c=33

Knight 3: p=9, c=11

But in the first example's explanation, the third knight (sorted as position 3) can kill the second and fourth knights. Wait, maybe I need to re-examine the first example.

Wait the first example's input is:

4 2

Power:4 5 9 7 → So when sorted by power, the order is 4,5,7,9. 

But the coins are 1,2,11,33. So the sorted list of knights is:

p:4 → c:1

p:5 → c:2

p:7 → c:33 (original fourth knight)

p:9 → c:11 (original third knight)

Now, processing each knight in order:

Initialize heap as empty, sum_heap=0.

For knight 0 (i=0):

answer is 1 + 0 = 1. Then, since k=2, add 1 to the heap. heap is [1], sum_heap=1.

For knight 1 (i=1):

answer is 2 + 1 (sum of heap which has 1 element) =3. Then, add 2 to the heap. Now heap has [1,2], sum=3.

For knight 2 (i=2):

answer is 33 + 3 (sum of heap [1,2]) → 36. Then, adding 33. Since heap size is 2 (k=2), compare 33 with heap[0] (1). 33>1. So replace 1 with 33. sum becomes 3-1 +33 =35. heap now contains [2,33].

For knight 3 (i=3):

answer is 11 +35 (sum of heap [2,33] sum is 35) →46. Then, adding 11. Current heap has size 2 (k=2). Compare 11 with heap[0] (2). 11>2. So replace 2 with 11. sum becomes 35-2 +11=44. So heap is [11,33], sum is 44.

But the answers for each knight in sorted order are [1,3,36,46]. But the original problem's output is [1,3,46,36], which suggests that the order in which the output is given is the original order of the input. Oh right! Because the output must be in the original order of the input. So the problem requires that the answer for each knight in the input's order is the computed value. 

So, after processing all knights in sorted order, we have computed the answers in the sorted order, but need to map them back to the original input order. 

So this approach requires that after computing all answers in the sorted order, we reorder them back to the original input's order. 

Therefore, the steps are:

1. Read the input as a list of knights with their p and c. 
2. Sort the knights in increasing order of p. 
3. Compute the answers for each knight in this sorted order using the heap approach. 
4. Then, create a result list that maps the sorted answers back to the original order. 

So, to handle this, each knight in the sorted list must retain their original index. 

So, when sorting, we can keep track of the original indices. 

For example, the sorted list would be a list of tuples: (p, c, original_index). 

This way, after processing all the sorted knights and computing their answers, we can place the answers in the original order. 

So modifying the approach:

sorted_knights = sorted( ( (p[i], c[i], i) for i in range(n) ), key=lambda x: x[0] )

Then, during processing, for each knight in sorted_knights, we compute the answer and store it in the answers list at the original index. 

So the code would look like:

heap = []
sum_heap = 0

answers = [0]*n

for knight in sorted_knights:
    p_i, c_i, original_i = knight
    ans = c_i + sum_heap
    answers[original_i] = ans
    # Then add c_i to the heap
    if len(heap) < k:
        heapq.heappush(heap, c_i)
        sum_heap += c_i
    else:
        if k >0 and c_i > heap[0]:
            sum_heap -= heapq.heappop(heap)
            heapq.heappush(heap, c_i)
            sum_heap += c_i

This way, after processing all knights in sorted order, the answers are stored in their original positions. 

Testing this with the first example:

Original input:

n=4, k=2

p = [4,5,9,7]

c = [1,2,11,33]

sorted_knights are sorted by p:

4 (original 0) → c=1, original index 0

5 (original 1) → c=2, original index 1

7 (original 3) → c=33, original index 3

9 (original 2) → c=11, original index 2

Processing these in order:

i=0 (original index 0):

ans =1 + 0 =1. Add to heap. heap is [1], sum 1.

answers[0] =1.

i=1 (original index 1):

ans=2 +1=3. Add to heap. heap [1,2], sum 3. answers[1]=3.

i=2 (original index 3):

c_i=33. ans=33 +3=36. Then, since k=2, heap is full. compare 33 with heap[0] (1). 33>1. replace 1 with 33. sum becomes 3-1 +33=35. heap now [2,33]. answers[3] =36.

i=3 (original index 2):

c_i=11. ans=11 +35=46. Then add 11. heap is full (size 2). compare 11 with heap[0] (2). 11>2. replace 2 with 11. sum becomes 35-2 +11=44. heap now [11,33]. sum is 44. answers[2] =46.

So the answers array is:

original index 0 →1

original index1 →3

original index2 →46

original index3 →36

Which matches the first example's output: 1 3 46 36. 

Yes, this works.

Another test case:

Second example:

Input:

5 1

p = [1,2,3,4,5]

c = [1,2,3,4,5]

sorted_knights are ordered by p (same as original order). 

Processing each:

heap is empty, sum 0.

i=0: ans=1+0=1. add to heap (k=1). heap [1], sum 1. answers[0] =1.

i=1: ans=2 + sum_heap (1) =3. Then, add 2. heap is full. compare 2 vs 1. 2>1. replace. sum becomes 1-1 +2=2. heap [2]. answers[1] =3.

i=2: ans=3 +2=5. add 3. compare 3>2 → replace. sum becomes 2-2 +3=3. answers[2]=5.

i=3: ans=4+3=7. add 4>3 → replace. sum becomes 3-3 +4=4. answers[3]=7.

i=4: ans=5+4=9. add 5>4 → replace. sum becomes 4-4 +5=5. answers[4] =9. 

So output is 1 3 5 7 9. Which matches the second example. 

Third example: n=1, k=0.

The only knight's answer is c_i (3) + sum of heap (0) →3. 

So yes. 

So this approach works.

Now, considering the constraints. 

n can be up to 1e5. For each element, we perform heap operations (heappush, heappop) which are O(logk) time. Since k is up to 10, logk is around 3. So for 1e5 elements, the total time is O(n logk) which is acceptable. 

Space-wise, we need O(n) for the answers array and O(k) for the heap, which is acceptable.

Now, implementing this in Python. 

But in Python, the heapq module is a min-heap, which is exactly what we need here. 

So the code steps:

Read n and k from input.

Read p array.

Read c array.

Create a list of tuples (p[i], c[i], i) for i in 0..n-1.

Sort this list by p[i].

Initialize heap and sum_heap.

Process each knight in sorted order, compute the answer and store in the answers array at original index.

Finally, print the answers array as space-separated integers.

Edge cases:

- k=0: each knight cannot kill anyone, so the answer is their own c.

- n=1 and k=0: same.

Now, code:

But wait, when k is 0, we can't add any elements to the heap. So in the code, when k is 0, the code skips adding to the heap. 

In code:

if k >0:

   ... do heap processing

Else:

   for each knight, answer is c_i + sum_heap (which is 0, since heap is never added to)

So code handles k=0 correctly.

Another edge case: when k is 0, and all other knights have higher power, so each can't kill anyone. So the answer is their own c.

Now, coding:

So here's the code:

import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
knights = sorted( ( (p[i], c[i], i) for i in range(n) ), key=lambda x: x[0] )

answers = [0]*n
heap = []
sum_heap = 0

for knight in knights:
    _, ci, original_i = knight
    ans = ci + sum_heap
    answers[original_i] = ans
    if k ==0:
        continue
    if len(heap) < k:
        heapq.heappush(heap, ci)
        sum_heap += ci
    else:
        if ci > heap[0]:
            sum_heap -= heapq.heappop(heap)
            heapq.heappush(heap, ci)
            sum_heap += ci

print(' '.join(map(str, answers)))

Testing this code against the first example:

Input:

4 2

4 5 9 7

1 2 11 33

sorted knights are in order 4 (c=1),5 (2),7 (33),9 (11). 

Processing:

original_i=0:

ans=1+0=1. heap has [1], sum 1.

original_i=1: ans=2+1=3. heap [1,2], sum 3.

original_i=3 (since sorted knight 7's original index is 3): ans=33+3=36. Then, since heap is size 2 (k=2), compare 33>1. replace 1 with 33. sum becomes 3-1 +33=35. heap is [2,33].

original_i=2 (sorted knight 9's original index is 2): ans=11 +35=46. Then, add 11. Compare 11>2. sum becomes 35-2 +11=44. heap becomes [11,33]. 

So answers array:

original indexes 0,1,3,2 → answers[0] =1, answers[1]=3, answers[3]=36, answers[2]=46. So the output is 1 3 46 36, which matches.

Yes.

So this code should work. 

But wait, when k=0, the code skips adding anything to the heap. So sum_heap remains 0. For each knight, ans is ci + 0 → correct.

Another test case where k is larger than the number of possible victims. For example, if k=3 but a knight has only 2 victims. Then, sum all 2. 

Yes, the code handles that because when len(heap) is less than k, it adds all possible, which is up to the number of victims. 

Yes. 

So this code should be correct.
</think>

```python
import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
knights = sorted(((p[i], c[i], i) for i in range(n)), key=lambda x: x[0])

answers = [0] * n
heap = []
sum_heap = 0

for knight in knights:
    _, ci, original_i = knight
    ans = ci + sum_heap
    answers[original_i] = ans
    if k == 0:
        continue
    if len(heap) < k:
        heapq.heappush(heap, ci)
        sum_heap += ci
    else:
        if ci > heap[0]:
            sum_heap -= heapq.heappop(heap)
            heapq.heappush(heap, ci)
            sum_heap += ci

print(' '.join(map(str, answers)))
```