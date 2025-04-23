<think>
Okay, I need to solve this problem where two players take turns removing elements from a list until only one remains. The first player wants to minimize the final number, the second wants to maximize it. Both play optimally. Hmm, how do I model their choices?

Let's think about the problem step by step. The key is to figure out the optimal strategy for each player. Let's consider the order in which elements are removed. Since both players are making optimal choices, the outcome depends on the number of turns each has. The first player starts, and they alternate, so the number of moves each makes depends on whether n-1 is even or odd. Wait, n-1 is the total number of moves. For example, if n is 3, there are 2 moves. First player moves first, second next. So if the number of moves is even (like n-1 being even), then the first and second players have equal turns? Or wait, when n-1 is the total moves. For example, n=3, moves: first does 1, second does 1. So if n-1 is even, each player has (n-1)/2 moves. If n-1 is odd, the first has one more move. Wait, n-1 can be even or odd. Let's see: when n-1 is even, the first player makes (n-1+1)/2 moves, because it's alternating starting with the first. Wait, for example, n-1=2: first does move 1, second does move 2. So each has 1 move. If n-1 is 3: first, second, first. So first has 2 moves, second 1. So the parity of n-1 determines how many times each player gets to move. So the first player moves ceil((n-1)/2) times, the second floor((n-1)/2) times. Because n-1 is the total moves. For example:

n-1 = 1: first moves once.

n-1 = 2: first and second each once.

n-1 = 3: first twice, second once.

So the first player has more moves when n-1 is odd. Wait, the first player starts. So for each turn, players alternate. So the number of moves the first player makes is (n-1 + 1) // 2. Because for even n-1, it's (even number divided by 2), but for odd it's (odd +1)/2. So for example, n-1=3: (3+1)/2=2. Which is correct.

So the first player makes m = (n-1 +1)//2 moves. The second makes (n-1 - m) moves. Wait, no. Let's compute m as the number of moves first player makes. Since they start, the sequence is 1st, 2nd, 1st, 2nd, etc. So the number of first's moves is ceil( (n-1) / 2 ). For example, n-1=2: 2/2=1. So first makes 1. n-1=3: 3/2 is 1.5, ceil gives 2.

So first player's moves is m = ceil( (n-1) / 2 ), second's is floor( (n-1)/2 ). Because the sum is (ceil + floor) = n-1.

So the problem reduces to selecting m moves by the first player (who wants to minimize the final value), and then the remaining (n-1 -m) moves by the second (who wants to maximize it).

Wait, but how does the selection of elements to remove affect the remaining one? Because each player is removing elements in a way that their strategy affects the possible outcome. So the process is: each step, the current player chooses which element to remove, and after all steps, the last remaining element is the result.

But how to model this? Since each choice affects the remaining elements, the players have to consider all possible options at each step. However, with n up to 1000, a recursive approach would be impossible due to time constraints.

So we need a mathematical approach rather than a simulation. Let's think about the optimal strategies.

Let's consider that after all moves, the remaining element is determined by the order in which elements are removed. But given that both players play optimally, the final result can be determined by the sorted array. Let's think of an example.

In the first sample input: sorted array is [1,2,3]. The first player wants to minimize the result. So he removes 3, leaving 1 and 2. Then the second player wants to maximize, so he removes 1, leaving 2. So the final is 2.

Another example: if n is 2. Then first player removes the higher number, leaving the lower. So the answer is the minimum of the two. Because the first player's move is to leave the smallest possible. Wait, if n is 2, n-1=1 move. The first player removes one of them. Since he wants to leave the smaller, he will remove the larger one. So the remaining is the smaller.

If n is 4. The total moves are 3. The first player has 2 moves, second has 1. The first's goal is to minimize, the second's to maximize. Let's see the sorted array. Let's think of the process:

Players alternate, but the order in which they remove elements depends on their strategies.

Wait, perhaps the optimal play is such that the remaining element is the (m)th element in the sorted array. Wait, m is the number of moves the first player makes. Let's see.

In the first example, n=3. n-1=2 moves. m= (2+1)/2=1.5? Wait, no. Wait m is the number of moves the first player makes, which is ceil( (n-1)/2 ). So for n=3, n-1=2. ceil(2/2) = 1. So m=1. The first player makes one move. The second makes 1. So the sorted array is [1,2,3]. After first player removes 3, the second removes 1, leaving 2. Which is the element at index (m) in the sorted array (if sorted in ascending order). Wait, indexes start at 0. If sorted array is [1,2,3], m=1. Then the remaining element is at position 1 (0-based?), or 1? Hmm, m=1. So 1st player has 1 move. How does that map to the index?

Wait maybe the answer depends on the parity of m and the moves. Let's think for different n:

Another example: n=4. Then n-1=3 moves. m= ceil(3/2) = 2. So first player has 2 moves, second has 1. So the sorted array is [a1, a2, a3, a4] in ascending order. The first player (minimizing) will try to remove the largest elements. The second (maximizing) will try to remove the smallest elements. So after two moves by first and one by second, the remaining element would be the third in the sorted array? Let's see.

Take n=4, array [1, 2, 3,4]. First player's first move: to remove 4 (to minimize the possible remaining). Then second player's move: to remove 1 (to maximize the remaining). Then first player again: remove 3. So remaining is 2. Or wait, after first two moves: first removes 4, second removes 1. Now there are 2 elements left: 2 and 3. The first player removes the larger of these (3), leaving 2. So the final is 2. The sorted array is [1,2,3,4]. The remaining element is 2, which is at index 1 (0-based). But m is 2. Hmm, not sure. So in this case, the index is 1. But 2 moves by first player.

Alternatively, maybe the answer is the element at position (m-1) when the array is sorted in ascending order. Because for the first example, m=1. Position 0: 1, 1:2, 2:3. The answer is 2, which is at position 1. Hmm, m-1=0. Not matching. Wait that's not right.

Alternatively, perhaps the answer is the element at position (m-1) in the sorted array when the array is sorted in ascending order. Wait, for the first example, m=1. So 1-1=0. The answer would be the first element. But the answer was 2. So that's not matching.

Hmm, maybe I need to think differently. Let's look for a pattern in small examples.

Let's consider various n and sorted arrays to see what the result is.

Case 1: n=1. Then the result is the only element. So for any array of size 1, that's the answer.

Case 2: n=2. The first player removes the larger element. The remaining is the smaller. So sorted array [a, b], a < b. Result is a. So the first element in the sorted array.

Case 3: n=3. Sorted [a, b, c]. First player removes c (to minimize the remaining). Then the second removes a (to maximize), leaving b. So the middle element. So the sorted array's second element (index 1 in 0-based). Which is the element at position (m) where m=1 (since m=ceil(2/2)=1). So m is the number of moves made by the first player. So in this case, the answer is the element at index m in the sorted array (0-based? No, because for n=3, m=1, index 1 is the middle). So 0-based index m is 1.

Another example: n=4. As discussed earlier, the answer is the second element (index 1) in the sorted array. Because the first player makes two moves. Let's see:

Sorted array [1,2,3,4]. The first player's moves are:

First move: remove 4 (max) to minimize the possible. Second move: remove 3. The second player's move is to remove 1. So remaining is 2.

So the answer is 2, which is the element at index 1. The first player made two moves. So m=2. So the answer is at index m-1? Because 2-1=1. So maybe the answer is the (m-1)th element in the sorted array.

Wait, for n=3, m=1. So m-1=0. But the answer is index 1.

Hmm, this line of thinking might not be leading me anywhere. Let's try another approach.

The problem resembles a game where each player alternately picks elements to remove, with opposite goals. The final result depends on the order of removals.

But how to model the optimal play. Let's think recursively. Suppose we have a list of elements. The first player's turn: they can choose any element to remove. Then the second player does the same, and so on. The outcome is the last remaining element. But with n up to 1000, a recursive approach is impossible due to time.

Alternative idea: the optimal play for both players would result in the final element being either the k-th smallest element, where k depends on the number of moves each player can make.

Wait, perhaps the players' choices can be viewed as selecting elements to remove in a way that the remaining elements form a window in the sorted array. Let's sort the array first. Then, the first player, wanting to minimize the final element, will try to eliminate the larger elements. The second player, wanting to maximize, will try to eliminate smaller elements. But the order of their moves determines how much they can influence the outcome.

For example, if there are m moves for the first player and s moves for the second (m = ceil((n-1)/2), s = floor((n-1)/2)), then the first player will remove m elements, but which ones?

But perhaps the optimal play can be thought of as follows: after sorting the array, the first player removes the largest elements, and the second removes the smallest. The remaining element would be in the middle. Wait, but how?

Let's take n=5. So n-1=4 moves. m = ceil(4/2) = 2. So first player has two moves, second two moves. Sorted array [a, b, c, d, e]. The first player's goal is to leave the smallest possible element. So he would remove the largest elements first. The second player's goal is to leave the largest possible element. So he would remove the smallest elements first. So first player removes e and d. Second removes a and b. What's left is c. So the answer is c. Which is the middle element. But in this case, the index is 2 in 0-based (since 5 elements, sorted). Now, m=2. So m + s = 4. The index is (n - (m + s) -1)/2? Not sure. But the answer here is the third element (0-based index 2). For n=5, m=2. The index is 2, which is (5-1)/2 = 2. So perhaps the answer is the element at position (n-1 - s) where s is the number of moves by the second player. Alternatively, maybe the answer is at position (m) in the sorted array (0-based). For n=3, m=1, position 1. For n=5, m=2, position 2. For n=4, m=2, position 1 (as in the earlier example where the answer was 2 in [1,2,3,4] → index 1). Wait, no. For n=4, m=2, but the answer was at index 1 (0-based). So this line of reasoning might not hold.

Alternatively, perhaps the answer is the element at index (m - s) in the sorted array, but I'm not sure.

Wait, let's see:

In the first example, m=1 (n=3, moves). s=1. So m-s=0. But the answer is index 1.

In the n=4 example, m=2, s=1. m-s=1. The answer is at index 1.

In the n=5 example, m=2, s=2 (n-1=4 moves, m=2, s=2). m-s=0. Answer is index 2.

Hmm, that doesn't fit.

Alternative approach: When the players play optimally, the final element is determined by the order in which they remove elements. The first player will try to minimize, so they remove the largest elements. The second will try to maximize, so remove the smallest elements. But the order in which they do this depends on whose turn it is.

But after all possible removals, the remaining element would be the one that is in the middle of the sorted array when considering how many elements each player can remove from the ends.

For example, with m moves by the first player and s moves by the second:

The first player can remove m elements from the end (the largest ones) to minimize the possible result. The second player can remove s elements from the start (the smallest ones) to maximize the result. So after these m + s deletions, the remaining element is the (m)th element from the start (since we've removed s from the start and m from the end). Wait, but how?

Let me think of the sorted array. The first player's m moves: each time removing the largest element. So after m moves, the remaining array is the first (original_length - m) elements. Then the second player's s moves: each time removing the smallest element. So after s moves, the remaining array is the elements from s to (original_length - m -1). But how much is left?

Wait, let's see:

Original sorted array is sorted_a. The first player deletes m elements from the end (since those are the largest). So the array becomes sorted_a[0 : len(sorted_a) - m]. Then the second player deletes s elements from the beginning (the smallest), so the array becomes sorted_a[s : len(sorted_a) - m]. The remaining element is sorted_a[s + len(sorted_a) - m -1]? No, because after these deletions, the array would have (len(sorted_a) - m - s) elements. Wait, but len(sorted_a) is n. So after first player removes m elements, the array has n - m elements left. Then the second player removes s elements from the start, leaving (n - m - s) elements. But in our problem, the total number of elements removed is (m + s) = n-1, so (n - (m+s)) = 1. So the remaining element is at position s in the array after the first player's deletions. Because the second player deletes s elements from the start. So the remaining element is sorted_a[m + s]? Wait, no. Let's see:

Original array has length n.

After first player removes m elements (from the end), the array is sorted_a[0 ... n - m -1].

Then the second player removes s elements from the start (sorted_a[0 ... s-1]), so the remaining array is sorted_a[s ... n - m -1].

The length of this array is (n - m -1 - s +1) = n - m - s. Since m + s = n-1, this is 1. So the remaining element is sorted_a[s].

Wait, because n - m -1 - s +1 = n - m - s. Since m + s = n-1, this equals 1. So the element is sorted_a[s].

But in the first example, n=3. sorted_a is [1,2,3]. m=1, s=1. So sorted_a[s] is sorted_a[1] = 2. Which matches the example.

In the n=4 example, m=2, s=1. sorted_a is [1,2,3,4]. s=1. So sorted_a[1] is 2. Which matches the previous result.

Another example: n=5, m=2, s=2. sorted_a is [1,2,3,4,5]. s=2. The element is 3.

Another example: n=2, m=1, s=0. sorted_a[s] is 0, which is sorted_a[0] (since s=0). So the element is the first in the sorted array. Which matches the case where the first player deletes the larger element, leaving the smaller.

So this seems to hold. The formula is: after sorting the array, the answer is sorted_a[s], where s is the number of moves the second player has. Because after the first player deletes m largest elements, the array is sorted_a[0..n-m-1], then the second player deletes s smallest elements (the first s elements), leaving sorted_a[s] as the answer.

Wait, but how to compute s? Because s is the number of moves the second player makes, which is floor( (n-1)/2 ). Because m + s = n-1, and m = ceil( (n-1)/2 ). So for example, when n-1 is even:

n-1 = 2k. m = k, s = k. So the answer is sorted_a[k].

When n-1 is odd: n-1 = 2k + 1. m = k+1, s = k. So answer is sorted_a[k].

But wait, for n=3 (n-1=2, which is even), m=1, s=1. sorted_a[s] is 2. Which is correct.

For n=4 (n-1=3, which is odd), m=2, s=1. sorted_a[1] is 2. Correct.

For n=5 (n-1=4, even), s=2, sorted_a[2] is 3. Correct.

So s is equal to floor( (n-1)/2 ), because s = (n-1) - m. Since m is ceil( (n-1)/2 ), then s = (n-1) - ceil( (n-1)/2 ). For even n-1: ceil( (n-1)/2 ) = (n-1)/2. So s = (n-1)/2. For odd n-1: ceil( (n-1)/2 ) is (n)/2. s = (n-1) - (n/2). Let's see. For n=4 (n-1=3), s=3 - 2 =1. So s = floor( (n-1)/2 ). For n=5 (n-1=4), s=4-2=2. Which is floor(4/2) = 2.

So the formula for s is floor( (n-1)/2 ). So the answer is the element at index s in the sorted array.

So the algorithm is:

1. Sort the array in non-decreasing order.

2. Compute s = floor( (n-1)/2 )

3. The answer is a_sorted[s]

Let's test this with the examples:

First example:

3 elements sorted [1,2,3]. s = floor( (3-1)/2 ) = 1. a_sorted[1] is 2. Correct.

Second example:

3 elements all 2. sorted is [2,2,2]. a_sorted[1] is 2. Correct.

n=2: s = floor( (2-1)/2 ) = 0. a_sorted[0] is the smallest, which is correct.

n=4: s= floor(3/2) =1. a_sorted[1] is 2 (from [1,2,3,4]). Correct.

n=5: s=2. a_sorted[2] is the middle element. Correct.

So this seems to hold.

So the solution is to sort the array, then pick the element at index floor( (n-1)/2 ), which is equivalent to (n-1) // 2 in integer division.

Thus, the code is straightforward.

So the steps are:

- Read n.

- Read the array.

- Sort the array.

- Compute the index as (n-1) // 2.

- Output the element at that index.

Let me test this with the examples.

First example:

n=3, array [2,1,3]. sorted is [1,2,3]. (3-1)//2 =1. element is 2. Correct.

Second example: n=3, all 2. sorted is [2,2,2]. index 1 is 2. Correct.

Another test case: n=4, array [1,2,3,4]. (4-1)//2 =1. index 1 is 2. Correct.

So this works.

So the code is:

Read n.

Read list.

Sort.

Compute (n-1)//2.

Print the element at that index.

So the code is simple.

Now, considering the constraints: n can be up to 1000, which is trivial for Python's sort. The code will run in O(n log n) time, which is acceptable.

So the code will be:

Read n.

Read the list of numbers.

Sort them.

Compute index (n-1)//2.

Print the element.

Yes, that's the solution.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[(n-1)//2])
```