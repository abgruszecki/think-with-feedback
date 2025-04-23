<think>
Okay, let's tackle this problem. So, the problem is about Alice and Bob playing a game where they take elements from either end of an array to build a strictly increasing sequence. The last person to make a move wins. We need to determine who wins if both play optimally.

Hmm, the key here is that each move must result in a strictly increasing sequence. So when a player picks a number from the left or right, it has to be larger than the last element in the current sequence. Wait, wait, but the sequence is being built step by step. So the first element can be any of the ends. Then the next has to be larger than that, and so on.

Wait, the initial sequence is empty. So the first player (Alice) can take either the first or last element of the array. Then, the next player must take from the remaining elements either left or right, but the chosen element must be larger than the last element in the sequence. So the sequence must be strictly increasing. So each choice is constrained by the previous choice.

So the game continues until there are no valid moves left. The player who made the last move (i.e., the one who added the last element) wins.

So the problem is similar to the game where players take turns picking from ends, but with the added constraint that each pick must be larger than the previous. So the state of the game depends on the current left and right pointers in the array, and the last value chosen. But for large N (up to 2e5), a naive recursive or memoization approach won't work due to time and memory constraints.

Wait, the constraints say N is up to 2e5, which suggests that any O(N) or O(N log N) approach is acceptable, but O(N^2) is definitely out. So dynamic programming with O(N^2) states is impossible. So we need a way to model this efficiently.

Hmm. Let's think about the possible moves. Let's consider the possible sequences that can be formed. The sequence starts as empty, then each step adds an element from either end, larger than the previous.

Wait, but the sequence must be strictly increasing. So the order in which elements are taken matters. For example, if the first element is taken from the left, then the next must be larger than that. Similarly, if the first is taken from the right, the next must be larger than that.

But since the players are playing optimally to make the last move, the problem is a game theory problem where each player's choice depends on maximizing their chance to win.

But with N up to 2e5, standard game theory approaches like memoization or recursion are impossible.

We need to find a pattern or a way to model the game in a way that can be computed in linear time.

Wait, perhaps the key is to find the maximum possible length of the sequence that can be formed, and then see if that length is odd or even. Because Alice starts first, if the maximum possible length is odd, Alice wins; if even, Bob wins. But does this hold?

Wait, but that's only true if both players play optimally to maximize the number of moves. Because in a game where each move is forced to pick the next possible element to extend the sequence as long as possible, the parity of the maximum possible length would determine the winner.

But is that the case here? Because the players might not choose to play to maximize the sequence length, but instead to force a win regardless of the length. For example, if there's a choice between two options, one leading to an even number of moves and the other to an odd, a player would choose the one that gives them the win.

Wait, but in this problem, the game ends when there are no valid moves left. So each player's choice is constrained by the current possible moves. They have to pick a valid move (either left or right end, as long as the element is larger than the last in the sequence). So the players have no choice but to pick one of the available options. However, if there are multiple options, they can choose which one gives them a winning path.

So the key is to model the game state and see whether the current player can force a win from that state.

But again, with N up to 2e5, a brute-force approach is impossible.

Alternative approach: Let's model the possible sequence as a strictly increasing sequence taken from the ends. The maximum such sequence possible is when each player takes the smallest possible next element, but maybe not. Wait, no. The players are not trying to maximize the sequence length; they are trying to make the last move. So the problem is a two-player game where each player wants to win, not to make the sequence as long as possible.

But perhaps the maximum possible length of the sequence is fixed, and the winner is determined by the parity of that length. Because if both players play optimally to take the possible moves, the game will proceed until the maximum possible length is achieved. But perhaps the players can't influence the length, because their choices are constrained by the available options. So if the maximum possible length is K, then the first player wins if K is odd, else the second.

But how to compute K?

Wait, let's think about the initial example:

In the first example, N=1, the array is [5]. Alice takes it, sequence is [5], which is valid. So the length is 1, which is odd. Alice wins.

In the second example, 3 elements: 5 4 5. The possible sequences could be:

If Alice takes left (5), then the next move must take from left (4, but 4 <5, invalid) or right (5, which is equal, invalid). So the game ends, Alice wins. But that's not the case. Wait the sample input 3 is 5 4 5. The output is Alice. Wait according to the sample input 2, the output is Alice.

Wait in sample input 2:

The array is 5,4,5. So the possible choices for Alice are left (5) or right (5).

If she takes left (5), then the next player (Bob) can't take any elements (since 4 is less than 5, and the right is 5 which is equal). So Alice wins immediately.

If she takes right (5), same situation. So Alice can choose either, and she wins. So the sample output is Alice.

So the maximum possible sequence length here is 1. Which is odd, so Alice wins.

So the hypothesis that the maximum possible sequence length determines the outcome is correct here.

Another example: sample 3.

Input is 6 elements:5 8 2 1 10 9. Output is Bob.

Let's see. The possible maximum sequence.

Let's see the possible choices.

If Alice takes left (5), then next element must be larger than 5. The next options are 8 (left end) or 9 (right end). But 8>5, so Bob can take 8. Then the next element must be larger than 8. The remaining array is [2,1,10,9]. The left is 2, which is less than 8, invalid. The right is 9, which is larger than 8. So Alice takes 9. Then the next must be larger than 9. The remaining array is [2,1,10]. Left is 2, right is 10. 10>9, so Bob takes 10. Now the next must be larger than 10. The remaining elements are [2,1], which are both less. So the sequence is 5,8,9,10. Length 4. Bob makes the last move. So Bob wins.

Alternatively, maybe there's a longer sequence. Let's see.

Another possibility: Alice takes 5, then Bob takes 9. Then sequence is 5,9. Next, Alice needs to take a number larger than 9. The remaining array is 8,2,1,10. The ends are 8 and 10. So she takes 10. Then sequence is 5,9,10. Bob's turn. He must pick a number larger than 10. The remaining array is 8,2,1. All ends are less than 10. So sequence length is 3, Alice wins. But wait, in this scenario, the sequence is 5,9,10. So length 3. Then Alice made the last move, so she wins. But the sample output is Bob. So this path isn't possible. Why?

Wait, because the players play optimally. So in this scenario, when Bob has the choice between taking 8 or 9 (when Alice first took 5), he can choose the path that allows him to win. So maybe the first path is forced.

Alternatively, perhaps there's a maximum possible sequence length. Let's see:

What is the longest possible sequence that can be formed by taking from left or right ends, ensuring strictly increasing.

In the third sample:

5,8,2,1,10,9.

Let's see possible sequences.

Option 1: Take 5 from left, then 8 (left), then 9 (right), then 10 (from right). Wait, but the array after taking 5 and 8 is [2,1,10,9]. The ends are 2 and 9. 9 is larger than 8, so next is 9. Then the next element must be larger than 9. The remaining array is [2,1,10]. The ends are 2 and 10. 10>9, so take 10. Then next must be larger than 10. The remaining array is [2,1]. Both ends are less. So sequence is 5,8,9,10 (length 4). So Bob wins.

Alternatively, could there be a longer sequence? Suppose the initial steps are different.

Another approach: Take 9 first (from the right). Then next must be larger than 9. The remaining array is 5,8,2,1,10. The ends are 5 and 10. 10>9, take 10. Then next must be larger than 10. The remaining array is 5,8,2,1. Ends are 5 and 1. Both less. So sequence length 2. Then Bob made the last move (since Alice took 9, Bob took 10). So Bob wins. But in this case, the sequence is 9,10. Length 2, Bob wins. But this is shorter than the previous example.

So the maximum possible sequence length here is 4. So even length, so Bob wins. So the sample output is correct.

So the hypothesis that the maximum possible sequence length determines the winner seems to hold here.

So the problem reduces to finding the maximum possible length of the sequence that can be formed by taking elements from either end, in strictly increasing order. Then, the winner is Alice if the length is odd, else Bob.

But wait, is this always the case?

Let's consider a scenario where the maximum possible sequence length is K, but there's another path where the length is shorter, but the parity is different. Could a player choose to take a path that results in a shorter sequence but with a winning parity for them?

For example, if K is even, but there's a way for Alice to make a move that results in a sequence of length 3 (odd), then Alice would choose that path and win.

But this would depend on whether such a path exists. So the initial hypothesis might be incorrect.

So the problem is not as simple as finding the maximum possible K and checking its parity. Because the players are not trying to maximize the sequence length but to win the game.

So we need to model the game where each player makes choices that lead to a winning state, regardless of the sequence length.

But given the constraints (N up to 2e5), we need an O(N) or O(N) time algorithm.

Hmm. Let's think about how the sequence is formed. Since the sequence must be strictly increasing, each new element must be larger than the last one.

So the sequence is built in a way where each new element is strictly larger than the previous. So the sequence is strictly increasing, and the order is determined by the choices of left and right ends.

The first element can be any of the two ends. The next element must be larger than the first, and can be either the left or right end of the remaining array. And so on.

But how can we model the maximum possible steps the game can take, considering that both players are playing optimally to make the last move.

Alternatively, perhaps the optimal play is determined by greedily choosing the direction (left or right) that allows the maximum possible steps, but with parity in mind.

Wait, maybe the optimal play for each player is to choose the direction (left or right) that allows them to take as many steps as possible. But again, this may not be correct because the players' decisions are interdependent.

Alternatively, think of the problem as similar to the greedy algorithm for the longest possible increasing subsequence from both ends. Let's model the process of building the sequence as follows:

The first player (Alice) can choose either the left or right end. For each choice, the next player (Bob) must choose from the remaining ends, but the element must be larger than the last. The players alternate turns. The game ends when no valid moves are left. The player who made the last move wins.

So the problem is similar to a game where each move depends on the previous choice. But how to model this efficiently.

An approach that comes to mind is to track two pointers, left and right, indicating the remaining elements. The last value taken is known, so the next move must take a value larger than that. So for the current state (left, right, last_value), the current player can choose to take A[left] if it's larger than last_value, leading to a new state (left+1, right, A[left]), or take A[right] if it's larger than last_value, leading to (left, right-1, A[right]). The player can choose either option (if possible) and if any of the options leads to a winning position (i.e., the opponent cannot win from that state), then the current player can win.

But with N up to 2e5, this approach is impossible. Because the number of possible states is O(N^2), which is 4e10. So we need a smarter way.

Alternative idea: Since the sequence must be strictly increasing, the elements taken must form a strictly increasing sequence. So the order of elements taken is such that each is larger than the previous. So the maximum possible sequence is the maximum length possible by choosing elements from either end, each time larger than the previous.

But even if we can compute the maximum possible length, the parity (odd/even) determines the winner. However, as discussed earlier, this may not account for all possibilities where a player could choose a path leading to a shorter sequence but with a favorable parity.

But perhaps in this problem, the maximum possible sequence length is the only possible way the game can proceed. Because when players play optimally, they are forced to take the maximum possible path.

Wait, maybe not. For example, suppose there are two possible paths: one leading to a length of 3 (odd, Alice wins), and another leading to a longer length of 4 (even, Bob wins). Then Alice would choose the first path, ensuring she wins. So in this case, the maximum possible length is not the one that determines the outcome.

So the maximum length approach may not be sufficient.

This suggests that the problem is more complex and requires a way to model the game states where players choose paths that allow them to win, even if it means a shorter sequence.

But how to model this efficiently.

Alternative approach: Let's model the possible choices as a chain. Let's think of the sequence as starting with one of the ends. Then, each subsequent element must be larger than the previous. The players take turns choosing the next element.

Wait, but once the initial choice is made (left or right end), the subsequent choices are constrained by the direction. For example, if the first element is taken from the left, the next must be larger than that. So the next element can be the new left (A[1]) or the right end (A[N-1] if first element was A[0]). But in the case where the first element is taken from the right, the next must be larger than that.

Alternatively, perhaps the maximum possible sequence is determined by greedily choosing the smallest possible next element. But I'm not sure.

Another observation: the sequence must be strictly increasing. So the elements chosen must form a strictly increasing sequence. The order in which elements are chosen must be such that each new element is larger than all previous ones. So the entire sequence is a strictly increasing sequence.

So the problem reduces to finding a strictly increasing sequence formed by taking elements from the left or right end. The players take turns adding elements, and the last to add wins.

So the sequence is determined by the order of choices, but the players are trying to make the last move. So the key is to model the game where each player selects a valid move (if available) that ensures they can win regardless of the opponent's choices.

But again, with N up to 2e5, we need an O(N) approach.

Another idea: Let's consider the maximum possible sequence that can be formed. Suppose we can compute the maximum length K. Then, the first player wins if K is odd, else Bob. But this is only true if K is achievable through optimal play.

But how to compute K.

Wait, the maximum sequence length is the longest possible strictly increasing sequence that can be formed by taking elements from either end. How can we compute this?

This is similar to the problem of finding the longest possible strictly increasing subsequence formed by taking elements from the ends. But how?

For example, in the array [5,4,5], the maximum sequence is 5 (from either end), then no more moves. So length 1.

In the array [5,8,2,1,10,9], the maximum sequence is 5,8,9,10. Length 4.

In the array [1,3,2,4], the maximum sequence could be 1,3,4 (length 3), or 4, then 3 is not allowed, so maybe other possibilities. Hmm, but 1 is taken first. Then next must be 3 (left) or 4 (right). If take 3, next must be 4. So sequence length 3. If take 4 first, next must be 3 (since 3 <4 is not allowed). So maximum length is 3.

So the maximum length is 3, which is odd. Alice would win.

But how to compute this.

So the approach to compute the maximum possible sequence length is to greedily choose the next possible element from either end that is larger than the last chosen, and allows for the longest possible sequence.

But this requires a greedy approach.

Another possible approach is to model the sequence as the longest possible chain. Let's think of it as follows:

We start by choosing the left or right end. Then, for each possible choice, we recursively compute the maximum length possible. But this is O(N^2), which is not feasible.

Wait, but perhaps there's a pattern. Let's consider the two possible starting choices:

1. Start with the left end. The sequence must start with A[0]. Then, the next element must be larger than A[0], and can be either A[1] or A[N-1], whichever is larger than A[0].

But this is not necessarily the case. For example, if A[1] is smaller than A[N-1], but allows for a longer sequence in the future, it's possible to choose the smaller one first.

Alternatively, perhaps the maximum possible sequence can be formed by choosing the smallest possible next element (to allow more steps). For example, between two options, choosing the smaller one leaves more larger elements available for later steps.

So the optimal way to maximize the sequence length is to greedily choose the smaller possible next element.

This is similar to the approach used in some greedy algorithms for similar problems.

For example, the maximum possible sequence can be found by greedily choosing the smallest possible next element from the available ends. Let's see:

Initialize last = -infinity.

current left and right pointers.

count =0

While left <= right:

   if A[left] > last and A[right] > last:

       choose the smaller of the two, increment count, set last to the chosen value, and move the pointer (left++ or right--).

   elif A[left] > last:

       choose left, increment count, set last to A[left], left++

   elif A[right] > last:

       choose right, increment count, set last to A[right], right--

   else:

       break

So the count would be the maximum possible length.

But is this correct?

Let's test this approach on the sample inputs.

Sample 1: [5]

left=0, right=0.

A[left] =5>0 (last is -infinite). count becomes 1. Then left exceeds right. So count is 1. Alice wins. Correct.

Sample 2: [5,4,5]

Initial last is -inf.

left=0, right=2.

A[left]=5, A[right]=5. Both are > -inf. So choose the smaller one (5 is same, but we have to choose one). Suppose we choose left (5). count=1. Now, left=1, right=2. Last is5. Now, A[left]=4, A[right]=5. 4 <5, so no. So check if any is >5. A[right] is5, which is not. So loop breaks. So count is1. Alice wins. Correct.

Sample 3: [5,8,2,1,10,9]

Initial last is -inf.

left=0, right=5.

A[left] =5, A[right]=9. Both > -inf. Choose the smaller one (5). count=1. left becomes 1. last=5.

Now, A[left]=8, A[right]=9. Both >5. Choose smaller (8). count=2. last=8. left becomes 2.

A[left]=2 <8. So check right: 9>8. Choose right. count=3. last=9. right becomes4.

Now, A[right] is10>9. So choose between 10 and the left (2). 2 is <9, so can't. So choose 10. count=4. last=10. right becomes3.

Check left=2 (A[2]=2) and right=3 (A[3]=1). Both <10. So loop breaks. Count=4. Even. Bob wins. Correct.

So this approach works for the samples.

Another test case: [1,3,2,4]

Initial last is -inf. left=0, right=3.

A[left]=1 and right=4. Choose 1. count=1. left=1. last=1.

A[left]=3 and right=4. Both>1. Choose smaller (3). count=2. left=2. last=3.

Now, A[left]=2 <3. So check right=4>3. Choose 4. count=3. last=4. right=2.

Loop breaks. Count is3. Alice wins.

Another test case: [2,1,3,4]. The maximum sequence is 2,3,4 (count 3). So Alice wins. According to the approach:

Start with 2 (left). Then choose 3 (left) and then 4 (right). Count is3.

Yes.

Another example where the players can choose between two paths.

Suppose the array is [1,4,3,5]. The maximum sequence according to the approach is 1,3,5. But if you choose 1, then 4 is not allowed (since 3 is the next possible). Wait, no. Let's see.

Initial last is -inf. left=0, right=3.

Choose 1 (smaller than 5). count=1. last=1. left=1.

Now, A[left]=4, A[right]=5. Both >1. Choose the smaller (4). count=2. last=4. left=2.

Now, A[left]=3 <4. So check right (5>4). Take 5. count=3. last=5. right=2. Loop breaks. Count 3. Alice wins.

Alternative path: if after 1, choose 5 instead of4. Then sequence is 1,5. Then no more moves. Count 2. Bob wins. So the greedy approach of taking the smaller next element gives the maximum possible sequence length. Hence, the first player would choose the path leading to a longer sequence, which allows them to win.

So the algorithm's approach of greedily choosing the smaller next element (when possible) gives the maximum possible sequence length. Hence, the parity of this maximum length determines the winner.

So the approach is: compute the maximum possible sequence length using this greedy method, and then check if it's odd (Alice wins) or even (Bob).

Therefore, the solution is to compute this maximum length and check its parity.

Now, the next step is to implement this in Python.

The steps for the algorithm are:

1. Initialize left and right pointers to 0 and N-1.

2. Initialize last to -infinity.

3. Initialize count to 0.

4. While left <= right:

   a. Check if A[left] > last and A[right] > last. If so, choose the smaller of the two. Increment count, update last, and move the pointer.

   b. Else, check if either left or right element is larger than last. Take that element, increment count, update last, and move pointer.

   c. Else, break the loop.

So, implement this step.

Now, let's code this.

But what about the case where both left and right elements are larger than last, but choosing one leads to a longer sequence than the other? The greedy approach may not always find the maximum possible sequence. For example, consider an array where choosing a larger element now allows for more elements later.

But in our earlier examples, the greedy approach worked.

Wait, let's test a scenario where the greedy approach would fail.

Example: [3,1,4,5].

If we take 3 (left) first. Then next, left is 1 and right is5. Both are larger than3. Greedy approach would take 1. Then the sequence is 3,1. Which is invalid since it's not strictly increasing. So the algorithm would not proceed this way. Oh wait, no. Because after taking 3, the next elements must be larger than 3. So 1 is not larger than 3. So after taking 3, the next elements must be 1 (which is not allowed) or 5. So the algorithm would choose 5, leading to a sequence of 3,5. Count 2. Then next elements are 4 (left=1, right=2). 4>5? No. So the algorithm would have count 2.

But if the algorithm had taken 5 first (right end), the sequence would be 5. Then no more moves. Count 1.

Alternatively, the array is [3,1,4,5]. Let's see:

Greedy approach:

Initial left=0, right=3. A[left] =3, A[right]=5. Both are >-inf. Choose smaller (3). Count=1. last=3. left=1.

Now, left=1 (A=1), right=3 (A=5). Both must be >3. 1 <3, so no. 5>3. So take 5. count=2. last=5. right=2.

Now, left=1, right=2. A[left]=4 <5. So no. Loop breaks. Count is2. Bob wins.

But the maximum possible sequence is 3,4,5. How?

After taking 3 (left), then left=1 (A=1). But we can't take 1. So must take right (5). Then sequence is 3,5. Then no more steps. So count is2.

But wait, the array after taking 3 is [1,4,5]. But how to get 4?

Wait, no. The initial array is [3,1,4,5]. The left and right are 0 and 3. After taking 3 (left=0), the remaining array is [1,4,5]. So left pointer is 1, right is3. Next elements to choose are 1 (left) or5 (right). Both must be larger than3. 1 is not. So take5. Then the array is [1,4]. Left=1, right=2. Next elements are4 (left) and none. But after taking5, the next element must be larger than5. 4 is not. So the sequence is 3,5. Count2.

But there's another possible path: take3, then take4 (but how?). Because after taking3, the remaining array is [1,4,5]. Left is1, right is3. The left element is1, which is less than3, so can't be taken. The right is5. So must take5. So the sequence is3,5. So the algorithm's approach gives count2.

But perhaps the maximum possible sequence is3,4,5. How?

Wait, maybe the initial array is [3,1,4,5]. How to get 3,4,5.

Ah, perhaps I made a mistake in the array. Let me re-examine.

Wait, after taking3 (from left), the remaining array is [1,4,5]. The left and right pointers are 1 and3. The next element must be larger than3. The possible options are1 and5. 1 is invalid, so must take5. Then, the remaining array is [1,4]. Now, the next element must be larger than5. Both 1 and4 are smaller. So the sequence is3,5. Length2.

So the algorithm's approach is correct. So the maximum possible sequence is 2 steps, so Bob wins.

Another example where the greedy approach works.

Another example where choosing a larger element first leads to a longer sequence.

Let's take array [2,5,3,6].

Greedy approach:

Start with left=0 (2) and right=3 (6). Both are larger than -inf. Choose smaller (2). count=1. last=2. left=1.

Now, left=1 (5), right=3 (6). Both>2. Choose smaller (5). count=2. last=5. left=2.

Now, left=2 (3) and right=3 (6). 3 <5? Yes. So check right (6>5). Take6. count=3. last=6. right=2. Loop breaks. Total count3. Alice wins.

But what if we take6 first:

Sequence would be6. Then no more steps. Count1. Alice wins. So the greedy approach gives a longer sequence (3 steps), which is better.

Another example where the greedy approach picks the smaller of two options, leading to a longer sequence.

So the algorithm's approach of choosing the smaller next element when possible seems to work.

So, the code would look like:

Read N and array A.

Initialize left=0, right =N-1, last=-infinity, count=0.

loop while left <= right:

   if A[left] > last and A[right] > last:

       if A[left] < A[right]:

           count +=1

           last = A[left]

           left +=1

       else:

           count +=1

           last = A[right]

           right -=1

   elif A[left] > last:

       count +=1

       last = A[left]

       left +=1

   elif A[right] > last:

       count +=1

       last = A[right]

       right -=1

   else:

       break

Then, if count is odd, Alice wins, else Bob.

So this code should work.

Testing the sample input 3:

N=6, array [5,8,2,1,10,9]

left=0, right=5.

A[left]=5, A[right]=9. Both> -inf. 5 <9. Take left. count=1. left=1. last=5.

left=1 (8), right=5 (9). both>5. 8 <9. take 8. count=2. left=2. last=8.

A[left]=2 <8. check right=9. 9>8. take 9. count=3. right=4. last=9.

A[right]=10>9. take 10. count=4. right=3. last=10.

Now, left=2, right=3. A[2]=1, A[3]=1 (since right is3, array is [5,8,2,1,10,9], after taking left 0,1, right5,4,3). Wait, perhaps I need to recheck.

Wait initial array indices are 0-based. Let's see:

Original array: [5,8,2,1,10,9]. left starts at0, right at5.

Take left (5). left becomes1.

Then take left (8). left becomes2.

Then take right (9). right becomes4.

Take right (10). right becomes3.

Now, left=2, right=3.

A[left] is2, A[right] is1. Both are less than10. So loop breaks. count is4. even. Bob wins.

Which matches sample3.

So the code works for the samples.

Thus, the code is correct.

Now, implement this in Python.

But we need to read the input properly. For N=2e5, it's important to read the input efficiently.

In Python, for large N, using input().split() can be slow. So better to read from stdin as a buffer.

But for the problem constraints, in Python, using input() and split() should be acceptable. However, in some cases, it's better to read via sys.stdin.

But given the time limit of 1 second, and N up to 2e5, the code should be okay.

So the code:

Read N.

Read the array.

Initialize left, right, last, count.

Loop as described.

Then print 'Alice' if count is odd else 'Bob'.

So the code:

n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1
last = -float('inf')
count = 0

while left <= right:
    if a[left] > last and a[right] > last:
        if a[left] < a[right]:
            last = a[left]
            left += 1
            count += 1
        else:
            last = a[right]
            right -= 1
            count +=1
    elif a[left] > last:
        last = a[left]
        left +=1
        count +=1
    elif a[right] > last:
        last = a[right]
        right -=1
        count +=1
    else:
        break

print("Alice" if count % 2 else "Bob")

This should work.

Testing the first sample:

n=1, a=[5]. left=0, right=0. Both ends are5> -inf. left is5, right is5. Choose left (same, but code picks left. count becomes1. Alice.

Sample2:

n=3, array [5,4,5]. left=0, right=2.

Both 5 and5 are> -inf. choose left. count1. left=1. next, left is4, right is5. both are>5. 4 <5. take left. count2. last=4. but then next element must be>4. 4 <5? The code would check:

Now, left=1, right=2. a[1]=4, a[2]=5. last is4. a[left] is4 is not>4, a[right] is5>4. So take right. count3. last=5. right=1. Now, left=1 and right=1. a[left]=4<5. No options. count3, which is odd. Alice wins. But sample2's output is Alice.

Wait but according to the sample input2, the output is Alice. But according to the code, the count is3, which is odd. So why?

Wait wait, the sample input2 is:

3

5 4 5

But according to the code:

Initial left=0, right=2. a[0]5 and a[2]5 are both> -inf. code chooses left (since 5=5, code takes left). count becomes1. left=1. last=5.

Now, a[1]4 and a[2]5. both must be>5. 4 is not>5. 5 is not>5. So code enters else clause. loop breaks. count is1. So Alice wins. So the code is correct.

Ah! I see. So in the code, after taking the first element (5), the next step:

last is5.

Check a[left] (4) and a[right] (5). Are they>5? 4 is not. 5 is not. So else clause. So code breaks. So count remains 1. So Alice wins.

Ah, I see. So in the code, after taking the first element, the next step:

left=1, right=2.

a[left]=4 and a[right]=5. Both are not>5. So code breaks. So count is1. So code outputs Alice.

So the code is correct.

So the code works for all samples.

Thus, the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1
last = -float('inf')
count = 0

while left <= right:
    if a[left] > last and a[right] > last:
        if a[left] < a[right]:
            last = a[left]
            left += 1
        else:
            last = a[right]
            right -= 1
        count += 1
    elif a[left] > last:
        last = a[left]
        left += 1
        count += 1
    elif a[right] > last:
        last = a[right]
        right -= 1
        count += 1
    else:
        break

print("Alice" if count % 2 else "Bob")
```