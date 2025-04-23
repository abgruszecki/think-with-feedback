<think>
Okay, so I need to solve this problem where a ninja is trying to escape a canyon by climbing or jumping between two walls. The problem says that each second, the ninja does an action, then the water level rises. The goal is to determine if the ninja can escape before getting submerged.

Let me first understand the problem details. The canyon has two walls, left and right, each divided into n areas. The ninja starts at the first area of the left wall. Each action can be climbing up, down, or jumping to the opposite wall k meters higher. But when he jumps, if x + k exceeds n, he escapes. But the water is rising each second. So after each ninja's move, the water level goes up by 1. So the water starts at level 0 (before the first move?), but according to the note, maybe the initial water level is at the lower border of the first area. So during the first second, after the ninja's first move, the water level becomes 1. Then after each subsequent move, it increases by 1. So the ninja can't be on any area that's submerged. So for example, after t seconds, the water level is t. Because the first action is followed by the first increase to 1. So at time t (after ninja's t moves), the water is at level t. So for the ninja's position after t moves, he must be on a cell higher than the water level. Wait, no. Because after each ninja's move, the water rises. So the sequence is: ninja moves (time 1), then water is 1. Then ninja moves again (time 2), water becomes 2, etc. So after t moves, the water level is t. So the ninja's current position must be on a cell that is strictly higher than t, because during his move, he can't be on a submerged cell. Because after each move, the water rises. So during his move, after he moves, the water level is t (after t moves). Wait, maybe the water level is t after t moves. Because after the first move (t=1), the water becomes 1. So yes. So at step t, the ninja has done t moves, and the water level is t. So when he is making his t-th move, the water level is t-1. But during that move, he moves, then the water rises to t. So after the move, he must not be in a cell that's <= t. Because the water has just risen. So during the move, he can move to a cell higher than t? Or is the check done after the move?

The problem statement says that the ninja can't be on an area covered by water. So after each move (action), the water level increases. So after each action, the water is at level equal to the number of actions taken so far. So during the ninja's action, he must not be on a cell that's submerged. Wait no. Let me re-read that part.

The note says that the ninja and water move in turns. First ninja does an action, then water raises. So for example:

Time 0: ninja is at position 1 (left wall). Water level is 0 (lower border of first area). So the first action (time 1) is taken by the ninja. Then the water level becomes 1. Then ninja's second action (time 2), then water becomes 2, etc.

So after each ninja's action (t actions done), the water level is t. So when the ninja is in the process of doing the t-th action, the previous water level was t-1. So during his t-th action, he can move to a cell, but after the move, the water level becomes t. So the cell he is in after the move must be higher than t. Otherwise, he's submerged.

Wait, but the problem says that the ninja cannot be on the area covered by water. So the area covered by water is the ones up to the current water level. For example, after t moves, the water level is t. So any cell with number <= t is submerged. So the ninja's position after the t-th move must be on a cell that's not submerged. So after each move, the cell he's on must be > t (since the water is now t). Because the water has just risen by one.

So the problem is to find a sequence of moves where, after each move i (i steps taken), the ninja's current position is a safe area (not X) and its number is > i.

Moreover, if during any move, the ninja jumps and his new position is x + k > n, then he escapes, and it's a success.

So the task is to model the possible positions the ninja can be in, and check if there's a path that leads to escaping the canyon, under the constraints that after each move, his current position is safe and above the current water level (i steps => water level i, so x > i).

Hmm. So this looks like a BFS problem. Because the ninja can be in different states (current wall, current position, time step). But since the time step increases each move, we need to track the time steps. Because at each step t, the position must be > t.

But since n can be up to 1e5, and steps can be up to n (since if the ninja hasn't escaped after n steps, the water level is n, so he can't be anywhere), we need an efficient way to model this.

Wait, the maximum possible steps t can be up to n, because after t steps, the water level is t, so if the ninja is on a cell x, x must be > t. But since the maximum x is n, t can be at most n-1. Because for x = n, t must be < n. So after n steps, the water level is n, so the ninja can't be on any cell. So the maximum steps the ninja can take is n steps, but even that may be impossible. So the BFS needs to track the time steps up to n, but that's O(n) time.

But for BFS, each state is (wall, position, time). The wall can be left (0) or right (1). Position ranges from 1 to n. Time ranges up to t steps. So the total possible states are 2 * n * n. But for n=1e5, that's 2e10 states, which is impossible.

Wait, that's way too big. So the BFS approach with these parameters is not feasible. So there must be a smarter way.

Alternative approach: since the time step is equal to the number of moves taken, each time we take a move, the time increases by 1. So for each position, the time step must be t, and the cell must be safe and x > t.

Wait, perhaps the key is that for each possible position (wall, x), the earliest time step t when the ninja can reach it. Because if he reaches (wall, x) at time t, then x must be > t. And for the next move (t+1), he must move to a position that's > t+1. So perhaps we can model this using BFS, but track for each position (wall, x) the earliest time t when it's possible to reach there. Because once a position is visited at time t, any later time (t') >= t is worse, since the x must be > t'. So arriving earlier gives a better chance to proceed further.

So this is similar to BFS where each state is (wall, x), and the time step t. We need to track the minimal t for each (wall, x). Because if we can reach (wall, x) at time t, then for any next steps, the time will be t+1, t+2, etc. But if we already have a way to reach (wall, x) at an earlier time, then there's no need to consider later times.

So the idea is to model this as a BFS, where each node is (wall, x) and the time when the ninja arrives here. But since we can only reach (wall, x) at time t where t is the number of steps taken (since each move increases the step by 1), the time is equal to the number of moves taken. So when you arrive at (wall, x) in step t, that's after t moves, and the water level is t. So x must be > t.

But when you make a move, you are in step t+1. Wait, no. Let's think: initial state is step 0 (no moves taken), water level 0. Then, after the first move (step 1), the water level is 1. So the state after the first move is step 1. So each node (wall, x) is reached at step t, which is the number of moves made. So x must be > t. For example, after step t, the position x must be x > t.

So for BFS, we can model each state as (current wall, current x, current step t). The initial state is (left wall, x=1, step 0). Because initially, after 0 moves, the ninja is at (left, 1), and the water is at 0. But since x=1 > 0, it's allowed.

But in the first move (step 1), after the move, the water is 1. So the new position x must be >1.

So the BFS proceeds by steps. Each time, we process the current state (wall, x, t), and generate the next possible states (wall', x', t+1), ensuring that x' > t+1 and the cell is safe.

But even with that, for n=1e5, the BFS might be O(n) steps, which is manageable. Because each state is processed once. Since each (wall, x) can be visited at the earliest possible step t. Once we process a state, we don't need to process it again with a higher t, because arriving earlier gives more possibilities (since in later steps, the allowed x is higher).

So for example, if we reach (left, x) at step t, and then later find another path to reach (left, x) at step t' > t, we can ignore the second path since it's worse. So we can track the earliest step t at which each (wall, x) is visited.

Therefore, we can use a BFS approach where each state is (wall, x) and we track the earliest step t for which it's possible. For each such state, when we process it, we generate possible next moves (up, down, jump), check if the next x is valid (<=n, and safe), and the next step t+1 must satisfy that next x > t+1.

But how to model this? Let's think:

We can have a 2D array (or two arrays for left and right) that keeps the earliest time when each position is visited. Initially, all positions are unvisited except for the start position (left, x=1) which is visited at step 0.

For each state (wall, x) with time t, we can generate possible next positions:

1. Move up to x+1 (same wall). The next step is t+1. The new x is x+1. Check that x+1 is <=n, the cell (wall, x+1) is safe (not X), and x+1 > t+1.

2. Move down to x-1 (same wall). The next x must be >=1. Check if cell (wall, x-1) is safe, and (x-1) > t+1.

3. Jump to the opposite wall, new x is x + k. If x + k > n, then the ninja escapes (return YES). Otherwise, check if the opposite wall's new x is safe, and new x > t+1.

So for each possible move, we need to check these conditions.

Now, the key is to process states in BFS order, so that the earliest t is processed first. Because once a state is visited with some t, any later t is irrelevant (since arriving later gives less flexibility for next steps).

So the BFS can be implemented with a queue, and for each (wall, x) we keep track of the earliest t when we arrived there. If we try to visit a state (wall, x) again with a higher t, we can ignore it.

So the steps are:

Initialize a distance array (or two arrays for left and right walls) with infinity. For the starting position (left wall, x=1), set distance to 0.

Then, use a queue to process the states. For each state (current wall, x, t), check the three possible moves:

For each move:

- Compute the new x and new wall.

- For move up: new_x = x + 1, same wall.

- For move down: new_x = x - 1, same wall.

- For jump: new_wall is opposite, new_x = x + k.

For each new position (new_wall, new_x), compute the new time t+1.

Check:

- If new_x exceeds n, then the ninja escapes. Return YES.

- Else, check that the new_x's cell is safe (not X), and new_x > t+1.

If these are satisfied, check if the new state (new_wall, new_x) has not been visited yet, or if the new t+1 is earlier than the existing recorded time.

If so, update the distance and add to the queue.

If any of these moves can escape (new_x + k >n when jumping, or new_x after moving up/down exceeds n?), wait no: moving up can only take x+1, which is <=n unless it's already n. But jumping may take x +k to be >n, which is escape.

So for example, in any move, if the new x (after the move) is >n, then the ninja escapes.

So during the processing of each move, we first check if the new x (after the move) is greater than n. If yes, return YES.

Otherwise, proceed to check if the new_x is safe, and if new_x > new_t (t+1).

If all conditions are met, then we can add this new state to the queue if it's the first time or better than previous.

So the BFS proceeds, processing each possible state once.

Now, considering that n is up to 1e5, and for each of the two walls, we have up to 1e5 positions. So the total possible states are 2*1e5=2e5. For each state, we can process it once, leading to O(n) time.

That's manageable.

Now, let's think about how to implement this.

We can represent the walls as two arrays: left and right. Each array has n elements, indicating whether the cell is safe ('-') or not.

We can read the two strings, and for each cell, check if it's safe.

The distance arrays can be two arrays, left_dist and right_dist, each of size n+2 (since x can be from 1 to n). Initialize them to -1 (unvisited), except left_dist[1] = 0.

Then, use a deque to process the states. Each state is a tuple (wall, x, t), but since t is the distance of that state, we can track t from the distance arrays. For example, when we process (wall, x) with t = left_dist[x] (if wall is left) or right_dist[x] (if wall is right).

Wait, perhaps the distance arrays for left and right walls can store the earliest time t when the position was reached. For example:

left_dist[x] = the earliest step t when the ninja is on the left wall, position x.

Similarly for right_dist.

So the initial state is left_dist[1] = 0.

Then, when processing a state (left, x, t), we can check the three possible moves:

1. Up: new_x = x+1. If x+1 > n, then escape. Else, check left[x+1] is '-', and new_x (x+1) > t+1. If yes, and left_dist[x+1] is unvisited (-1) or larger than t+1, then update it and add to queue.

2. Down: new_x = x-1. Must be >=1. Check left[x-1] is '-', and x-1 > t+1. Then same as above.

3. Jump: new_wall is right, new_x = x +k. If new_x >n → escape. Else, check right[new_x] is '-', and new_x > t+1. Also, check if right_dist[new_x] is unvisited or can be updated to t+1.

Similarly, for right wall positions.

So for each move, the new time is t+1.

This seems manageable.

Now, the key is to process each (wall, x) only once, when we find the earliest t to reach there.

So the BFS is a standard BFS, which processes nodes in order of their distance (time t) increasing. Because the first time a node is processed is with the smallest possible t.

Thus, when processing a node, we can explore all possible moves, and for each, check if the new node can be visited with t+1 steps, and if it's better than the existing (or not yet visited).

So the algorithm steps:

1. Read n, k.

2. Read left and right walls' strings.

3. Check if left[0] is not 'X' (but according to the problem statement, the first area of left is safe, so this is guaranteed. So no need.)

4. Initialize left_dist and right_dist arrays of size n+1 (since positions are 1-based?), filled with -1. left_dist[1] = 0.

5. Create a queue. Start with (left, 1, 0). Wait, but perhaps the queue can just track (wall, x), and the current t can be retrieved from the distance arrays.

Alternatively, the queue can hold (wall, x), and whenever we process (wall, x), we get t from the distance arrays. Because each (wall, x) is processed once, with the minimal t.

So the queue starts with (left, 1). Then, for each element dequeued, we get the current t (left_dist[x] for left wall).

So the queue could be a deque of tuples (wall, x). For each (wall, x), when dequeued, we process all possible moves.

So steps:

Initialize left_dist[1] = 0.

Add (0, 1) to the queue (0 represents left wall, 1 represents position).

Then, while the queue is not empty:

   Dequeue (current_wall, current_x).

   Get current_t from the distance array (left_dist[current_x] if current_wall is 0, else right_dist[current_x]).

   Check if current_t > current_x: since when the ninja is here, current_x must be > current_t. Because when he arrives here at step current_t, the water is current_t. So current_x must be > current_t. So if current_x <= current_t, this position is invalid. So this state can be skipped. Because it's impossible to have arrived here.

Wait, this is crucial. Because when we process (wall, x) with t, the x must be > t, otherwise it's already invalid. So when dequeuing a state, we must first check if x > t. If not, skip processing it.

Because even though we stored this state, maybe the x is now <= t, which makes it impossible. For example, if during processing a state (wall, x) where x was >t when enqueued, but during the time it's in the queue, some other path could have a lower t. But since BFS processes states in order of t, this can't happen. Because once we enqueue a state, we process it in order of the earliest t. So when dequeued, t is the minimal possible, so x must be >t. Because otherwise, the state would have been invalid when added.

Wait, for example, when adding a state (wall, x) with time t, we check that x> t. Because when you reach x at time t, x must be > t. Otherwise, that state is invalid and cannot be part of the solution.

So when we generate a new state (new_wall, new_x) with time t+1, we must check that new_x > t+1. Otherwise, we can't add it to the queue.

But during the BFS, when we process (wall, x) with time t, the code must first check that x >t. Because if not, this state is invalid and can be skipped.

So in the code, after dequeuing (wall, x), retrieve t from the distance array, then check if x > t. If not, skip processing this state.

This is because if x <= t, then the ninja is already submerged. So this state is invalid and cannot be part of the solution path.

So the processing steps would be:

For each (wall, x) in the queue:

   Get t from the distance array.

   if x <= t: skip processing (since this state is invalid)

   else:

      process all possible moves.

This check is important to prevent processing invalid states.

So now, the code steps:

Read n, k.

Read left_wall: string of length n. left_wall[i] is the i+1-th position (since 0-based).

Similarly for right_wall.

Create left = list(left_wall), right = list(right_wall).

Create left_dist and right_dist arrays of size n+2, initialized to -1.

left_dist[1] = 0.

queue = deque([(0, 1)]) # 0 is left, 1 is right.

found = False.

while queue not empty:

   current_wall, current_x = queue.popleft()

   current_t = left_dist[current_x] if current_wall == 0 else right_dist[current_x]

   # Check if this state is valid. x must be > current_t.

   if current_x <= current_t:

       continue

   # Check all possible moves.

   for each move in [up, down, jump]:

       compute new_wall, new_x.

       if new_x > n:

           print YES and exit.

       else:

           check if the new_x is safe (left or right wall's new_x-1 is '-', since 0-based).

           check if new_x > (current_t + 1).

           if yes, and the new state hasn't been visited (distance is -1) or can be updated to a smaller time:

               set the distance for new_wall, new_x to current_t +1.

               add (new_wall, new_x) to the queue.

So for each move:

Case 1: Up.

new_x = current_x +1.

same wall.

if new_x >n → escape.

else:

   check if current_wall's wall has new_x-1 (since 0-based) as '-'.

   new_t = current_t +1.

   if new_x > new_t:

       then, check if left_dist[new_x] (if same wall) is -1. If so, set to new_t and add to queue.

Case 2: Down.

new_x = current_x -1.

same wall.

if new_x <1 → invalid.

else:

   check if current_wall's wall has new_x-1 (0-based) as '-'.

   new_t = current_t +1.

   if new_x > new_t:

       check if distance is -1. Update and add to queue.

Case 3: Jump.

new_wall is 1 - current_wall.

new_x = current_x +k.

if new_x >n → escape.

else:

   check if new_wall's wall has new_x-1 (0-based) as '-'.

   new_t = current_t +1.

   if new_x > new_t:

       check if the new_wall's distance array has new_x as -1. If yes, set to new_t and add to queue.

If any of these moves leads to new_x >n, then return YES.

Else, process all possible moves.

If the queue is exhausted and no escape is found, return NO.

Now, let's test this logic against the sample inputs.

Sample Input 1:

7 3

---X--X

Left wall is positions 1-7:

Indices 0-6: '---X--X' → positions 1: '-', 2: '-', 3: '-', 4: 'X', 5: '-', 6: '-', 7: 'X' (but wait n=7, so positions 1-7. So the string is 7 characters. So left[0] is position 1, left[3] is position 4, which is 'X'. So yes.

Right wall: '-X--XX-' → positions 1: '-', 2: 'X', 3: '-', 4: '-', 5: 'X', 6: 'X', 7: '-'.

Sample Output: YES.

The ninja's path:

Start at left 1 (t=0). x=1>0.

First move: jump to right wall. new_x =1+3=4. new_t=1. 4>1 → yes. Check right[4-1] (right[3] is '-', yes. So added to queue. So right_dist[4] =1.

Then, step 1: move down to 3 (right wall). new_t=2. x=3>2? 3>2 → yes. So right_dist[3] =2.

Then step 2: jump to left, x=3+3=6. new_t=3. 6>3 → yes. left[6-1] is left[5] which is '-', yes. So left_dist[6] =3.

Then step3: move up to 7. new_t=4. 7>4 → yes. Then jump:7+3=10>7 → escape. So return YES.

So the code should process these steps.

Another sample: input 2.

n=6, k=2.

left: --X-X- → positions 1: '-', 2: '-', 3: 'X', 4: '-',5: 'X',6: '-'.

right: X--XX- → positions 1:'X', 2:'-',3:'-',4:'X',5:'X',6: '-'.

Sample Output: NO.

So the code should process and find no possible path.

So the code logic seems correct.

Now, let's code this in Python.

But for the code:

We need to represent left and right walls as 0-based indexes.

left_wall = input().strip()

right_wall = input().strip()

So for position x (1-based), the index in the string is x-1.

So left_safe[x] is left_wall[x-1] == '-'

Similarly for right.

But in the code, when checking, for example, if moving up to x+1 on left wall:

current_wall is 0 (left), current_x is x.

new_x = x +1.

if new_x >n → escape.

else: check left_wall[new_x -1] == '-', and new_x > new_t (current_t+1).

So in code:

if new_x <=n:

   if (current_wall is 0 and left_wall[new_x-1] == '-') or (current_wall is 1 and right_wall[new_x-1] == '-'):

       then check new_x > (current_t +1).

Similarly for down and jump.

So the code:

We need to read n, k.

Then read left and right strings.

Implement left_dist and right_dist arrays. Since n can be up to 1e5, using lists of size n+2 (since x can be up to n).

But for Python, initializing two lists of size n+2 with -1 is feasible.

Then, use a deque.

Now, the code outline:

import sys

from collections import deque

n, k = map(int, sys.stdin.readline().split())

left = sys.stdin.readline().strip()

right = sys.stdin.readline().strip()

left_dist = [-1] * (n + 2)

right_dist = [-1] * (n + 2)

left_dist[1] = 0

q = deque()

q.append( (0, 1) ) # left wall, position 1.

found = False

while q:

    wall, x = q.popleft()

    # Get current time

    if wall ==0:

        t = left_dist[x]

    else:

        t = right_dist[x]

    # Check if current state is valid (x > t)

    if x <= t:

        continue

    # Check possible moves

    # Move up

    new_x = x +1

    new_t = t +1

    if new_x >n:

        print("YES")

        found = True

        break

    else:

        if wall ==0:

            safe = (left[new_x -1] == '-')

        else:

            safe = (right[new_x -1] == '-')

        if safe and new_x > new_t:

            if wall ==0:

                if left_dist[new_x] == -1:

                    left_dist[new_x] = new_t

                    q.append( (0, new_x) )

            else:

                if right_dist[new_x] == -1:

                    right_dist[new_x] = new_t

                    q.append( (1, new_x) )

    # Move down

    new_x = x -1

    new_t = t +1

    if new_x >=1:

        if wall ==0:

            safe = (left[new_x -1] == '-')

        else:

            safe = (right[new_x -1] == '-')

        if safe and new_x > new_t:

            if wall ==0:

                if left_dist[new_x] == -1:

                    left_dist[new_x] = new_t

                    q.append( (0, new_x) )

            else:

                if right_dist[new_x] == -1:

                    right_dist[new_x] = new_t

                    q.append( (1, new_x) )

    # Jump

    new_wall = 1 - wall

    new_x = x +k

    new_t = t +1

    if new_x >n:

        print("YES")

        found = True

        break

    else:

        # Check if new_wall's new_x is safe.

        if new_wall ==0:

            safe = (left[new_x -1] == '-')

        else:

            safe = (right[new_x -1] == '-')

        if safe and new_x > new_t:

            if new_wall ==0:

                if left_dist[new_x] == -1:

                    left_dist[new_x] = new_t

                    q.append( (0, new_x) )

            else:

                if right_dist[new_x] == -1:

                    right_dist[new_x] = new_t

                    q.append( (1, new_x) )

if not found:

    print("NO")

But wait, in the code, after processing each possible move, we check if new_x is > new_t. If yes, proceed to check if the cell is safe, then update the distance.

But the code may process moves in any order, but for the BFS, the earliest time is processed first.

Another thing to note is that when we generate new_x (like in jumping), even if new_x is <=n, but adding it to the queue may lead to a possible escape in the next steps.

But the code may have multiple checks for escape. For example, moving up could lead to new_x >n, and we return YES.

But what if during the jump, new_x is x +k which is over n? Then we return YES.

So the code checks for escaping in all possible moves.

Now, let's test this code with sample input 1.

Sample Input 1:

7 3

---X--X

Left is '---X--X' → positions 1: '-', 2: '-',3: '-',4: 'X',5: '-',6: '-',7: 'X'.

Right is '-X--XX-' → positions 1: '-', 2: 'X',3: '-',4: '-',5: 'X',6: 'X',7: '-'.

The initial state is left wall, x=1, t=0.

Processing (0,1):

t=0. x=1>0.

Check moves:

Move up: new_x=2. left[1] is '-', safe. new_t=1. 2>1 → yes. left_dist[2] is set to 1. added to queue.

Move down: x-1=0 → invalid.

Jump: new_wall=1 (right), new_x=1+3=4. right[3] is '-', safe. new_t=1. 4>1 → yes. right_dist[4] =1. added to queue.

So queue now has (0,2), (1,4).

Next, process (0,2):

t=1. x=2>1.

Move up: x=3. left[2] is '-'. new_t=2. 3>2 → yes. left_dist[3] =2.

Added to queue.

Move down: x=1. left[0] is '-'. new_t=2. 1>2 → no. So not added.

Jump: new_x=2+3=5. right wall. right[4] is 'X' → not safe. So no.

So added (0,3).

Process (1,4):

t=1. x=4>1.

Move up: x=5. right[4] is 'X' → unsafe.

Move down: x=3. right[2] is '-'. new_t=2. 3>2 → yes. right_dist[3]=2. added to queue.

Jump: new_x=4+3=7. new_wall=0. left[6] is 'X' → unsafe. So no.

So queue has (0,3), (1,3).

Processing (0,3):

t=2. x=3>2.

Move up: x=4. left[3] is 'X' → unsafe.

Move down: x=2. left[1] is '-'. new_t=3. 2>3 → no. Not added.

Jump: new_x=3+3=6. right wall. right[5] is 'X' → unsafe.

So no additions.

Process (1,3):

t=2. x=3>2.

Move up: x=4. right[3] is '-'. new_t=3. 4>3 → yes. right_dist[4] is already 1 (from before?), but we check if it's -1. Since right_dist[4] is 1, which is not -1, so no addition.

Move down: x=2. right[1] is 'X' → unsafe.

Jump: new_x=3+3=6. new_wall=0. left[5] is '-'. new_t=3. 6>3 → yes. left_dist[6] is set to 3. added to queue.

Now, queue has (0,6).

Processing (0,6):

t=3. x=6>3.

Move up: x=7. left[6] is 'X' → unsafe.

Move down: x=5. left[4] is '-'. new_t=4. 5>4 → yes. left_dist[5]=4. added to queue.

Jump: x+3=9. which is >7. So return YES.

Thus, the code would print YES here.

So the code works for sample 1.

Sample 2:

n=6, k=2.

Left: --X-X- → '--X-X-' → positions 1: '-', 2: '-',3:'X',4:'-',5:'X',6:'-'.

Right: X--XX- → positions 1:'X', 2:'-',3:'-',4:'X',5:'X',6:'-'.

Initial state (0,1), t=0.

Processing (0,1):

t=0. x=1>0.

Move up: x=2. left[1] is '-'. new_t=1. 2>1 → yes. left_dist[2]=1. added to queue.

Move down: invalid.

Jump: x+2=3 → new_wall=1. new_x=3. right[2] is '-'. new_t=1. 3>1 → yes. right_dist[3] =1. added to queue.

Queue now has (0,2), (1,3).

Processing (0,2):

t=1. x=2>1.

Move up: x=3. left[2] is 'X' → unsafe.

Move down: x=1. new_t=2. 1>2 → no.

Jump: x+2=4. new_wall=1. right[3] is '-'. new_x=4 → new_t=2. 4>2 → yes. right_dist[4] =2. added.

Queue has (1,3), (1,4).

Processing (1,3):

t=1. x=3>1.

Move up: x=4. right[3] is '-'. new_t=2. 4>2 → yes. right_dist[4] is 2. added.

Move down: x=2. right[1] is '-'. new_t=2. 2>2 → no. Not added.

Jump: x+2=5. new_wall=0. left[4] is '-'. new_t=2. 5>2 → yes. left_dist[5] =2. added.

Now, queue has (1,4), (0,5).

Processing (1,4):

t=2. x=4>2.

Move up: x=5. right[4] is 'X' → unsafe.

Move down: x=3. right[2] is '-'. new_t=3. 3>3 → no.

Jump: x+2=6 → new_wall=0. new_x=6. left[5] is '-'. new_t=3. 6>3 → yes. left_dist[6]=3. added.

Queue has (0,5), (0,6).

Processing (0,5):

t=2. x=5>2.

Move up: x=6. left[5] is '-'. new_t=3. 6>3 → yes. left_dist[6] is 3. added (but already in queue).

Move down: x=4. left[3] is '-'. new_t=3. 4>3 → yes. left_dist[4] =3. added.

Jump: x+2=7 → escape. So code would print YES, but sample output is NO.

Wait, but sample 2's output is NO.

Hmm, this suggests a problem in the code. Wait, what's the sample input 2?

Sample Input 2:

6 2

--X-X-

X--XX-

So left is "--X-X-": positions 1: '-', 2: '-', 3: 'X', 4: '-', 5: 'X', 6: '-'.

Right is "X--XX-": positions 1: 'X', 2: '-', 3: '-',4: 'X',5: 'X',6: '-'.

So for the state (0,5), x=5, t=2. So during processing (0,5):

Jump: new_x=5+2=7>6 → escape. So the code would return YES. But the sample output is NO.

This is conflicting. So what's wrong here?

Wait, the sample input 2's output is NO, but according to this code's logic, the code would return YES. That suggests a mistake in the code.

But why? Let's re-examine the sample input.

Wait, the code must have a mistake.

In sample input 2, the ninja starts at left wall, position 1.

Let's step through the code's processing:

Initial state: (0,1) t=0.

Move up to 2 (t=1), added.

Jump to 3 (right wall, new_x=1+2=3. right[3-1] is right[2] which is '-', so safe. new_t=1. x=3>1 → yes. So added.

Then processing (0,2) (t=1).

Move up: x=3 (left) is 'X' → invalid.

Jump: x+2=4. right wall. new_x=4. right[3] is 'X' → unsafe. So no.

So (0,2) can't proceed.

Then processing (1,3) (t=1).

Move up to 4 (right wall, x=4). right[3] is 'X' → unsafe.

Move down to 2 (right wall, x=2). new_t=2. x=2>2 → no. So not added.

Jump: x=3+2=5 → left wall. left[4] (x=5-1=4?) → left[4] is '-'. new_t=2. x=5>2 → yes. So added (0,5) with t=2.

Now, processing (0,5) (t=2).

Jumping from x=5, new_x=5+2=7. Which is >6 → escape. So code returns YES. But sample output is NO.

But according to the sample input 2's output, the correct answer is NO. So this indicates that the code is incorrect.

But why?

Ah! Because the code's check for the jump is wrong. Because when you jump to x +k, you need to check if that's allowed. For example, in the sample input 2, when the ninja is at x=5 (left wall), t=2, and jumps to x=5+2=7. Since 7>6 (n=6), this would allow the ninja to escape. But according to the sample's explanation, there's no way.

But why? Let's think. How does the ninja reach x=5 on the left wall at t=2?

Let's retrace the path.

After the ninja jumps to the right wall at x=3 (t=1), then jumps to left wall x=3+2=5 (t=2). So the steps are:

t=0: left 1.

t=1: jump to right 3 (water level 1).

t=2: jump to left 5 (water level 2).

At this point, after the second jump (t=2), the water level is 2. The ninja is on x=5, left wall. x=5 >2 → allowed.

Now, during the next move (t=3), the ninja can jump again. But according to the code's logic, when processing (0,5) t=2, the code checks all three moves.

In the code, for the jump move:

new_x=5+2=7>6 → escape. So the code returns YES.

But according to the sample input 2's answer, the correct output is NO. So there's a discrepancy here.

But according to the problem statement, in the sample input 2, the ninja can't escape. So the code is giving the wrong answer.

What's wrong here?

Ah! Let me re-examine the code's logic for the jump.

When the ninja is at x=5 (left wall) at t=2.

new_x =5+2=7.

The code checks if new_x>6 (n=6), which it is. So the code returns YES.

But according to the problem statement, the sample input 2's correct output is NO. So what's wrong?

Ah! Because the code is not considering that the water level increases after each move. So the ninja's move is t=2. After this move, the water level becomes t=3. So the new_x=7 is valid, but the problem requires that after the move, the water level is t=3. Wait, no. The code's logic says that after t moves, the water level is t. So when the ninja makes a move (the t-th move), the water level after the move is t.

Wait, let's re-express the steps:

Each move is step 1, 2, ..., t.

After each move, the water level is equal to the number of moves made so far.

So after the ninja's first move (t=1), the water is 1.

After t moves, the water is t.

So when the ninja is at x=5 (left wall) at t=2, he made 2 moves. So the water level is 2. x=5>2 → allowed.

In his next move (t=3), he jumps to x=7, which is >6 (n=6). So he escapes. But according to the code, when he makes the jump in t=2, the new_x=7 is larger than n=6, so the code returns YES.

But according to the sample input 2, the answer is NO.

This suggests that the code's logic is incorrect.

But why? What's the mistake here?

Ah! Let's look at the sample input 2's description. The sample input 2's output is NO. So why does the code think the ninja can escape?

Let's see:

The code's logic says that when the ninja is at x=5 (left wall) with t=2, making a jump to x+2=7>6. So the code returns YES.

But according to the problem's note for sample input 2, there's no way to escape. So what's the mistake?

Ah! Because the code is allowing jumps that would take the ninja beyond the canyon during any move, but the problem's escape condition is that during a move, the ninja's new position is x+k>n. But perhaps the code is missing the fact that the ninja's current x must be safe.

Wait, when the ninja jumps to x +k, even if x +k >n, does the current x need to be safe?

No. Because the ninja is jumping from x to x+k. If x+k exceeds n, he escapes. But during the jump, the current x is safe and not submerged.

So during the jump, the ninja's position before the jump is x, which must be safe and x> t.

So for the sample input 2:

After two moves, the ninja is at x=5 (left wall), t=2. x=5>2, and the current cell is safe (left[4] is '-'). So he can jump to x=5+2=7>6. So the code's logic is correct, but according to the sample input 2, the correct answer is NO. This is conflicting.

But according to the sample input 2's description, there's no way to escape. So either the code is wrong, or the sample input's explanation is wrong.

But according to the sample input 2's details:

The left wall is "--X-X-" (positions 1: '-', 2: '-', 3:'X',4:'-',5:'X',6: '-').

Right wall is "X--XX-" (1:'X', 2:'-',3:'-',4:'X',5:'X',6: '-').

So the path the code is thinking is:

move 1: jump from left 1 to right 3 (t=1).

move 2: jump from right 3 to left 5 (t=2).

move 3: jump from left 5 to right 7 (escape, t=3).

But wait, the third move is move 3. After that, the water level is 3. But when the ninja makes the third move (jump to 7), the code returns YES.

But according to the problem's sample input 2, the answer is NO. So why?

Ah! Because after the third move (t=3), the water level is 3. The ninja is at x=7 (escaping), which is allowed. So the code is correct, but the sample input 2's explanation must be wrong?

No, this can't be. The sample input 2's output is NO. So there's a mistake in the code's logic.

Wait, perhaps the code allows the ninja to be on x=5, which is position 5 of the left wall. But according to the input's left wall, position 5 is 'X', which is dangerous. Wait, no. The left wall in sample input 2 is "--X-X-". Let's see:

The left wall string is "--X-X-". For position 5 (0-based index 4), the character is 'X'. So position 5 of the left wall is dangerous. So the ninja can't be there.

Ah! Here's the mistake.

In sample input 2, the left wall's fifth position (x=5) is 'X'. So when the ninja jumps to x=5, he can't be there. So the code's logic is incorrect because it allows the ninja to be in x=5.

So why is the code allowing the ninja to be there?

Because the code checks if the new_x's cell is safe. But in the code's code for the jump move:

When jumping from current_x to new_x = current_x +k.

current_wall is 1 (right) → new_wall is 0 (left).

So new_x is 3+2=5 (current_x is 3, right wall). So new_wall is left. The code checks if left[5-1] is '-', which is left[4] (since Python is 0-based). left wall's fourth position is '-', according to the input.

Wait, the left wall is "--X-X-". The indexes are 0-based. So:

positions:

1: 0 → '-'

2: 1 → '-'

3: 2 → 'X'

4: 3 → '-'

5:4 → 'X'

6:5 → '-'

Wait, sample input 2's left wall is "--X-X-". So for position x=5 (1-based), the index is 4 (0-based). So left[4] is 'X'. So new_x=5 (left) is dangerous.

So during the jump, the code checks whether the new_x's cell is safe. So when the ninja jumps to left x=5, the code checks left[5-1] = left[4], which is 'X', so it's unsafe. Hence, this move is not allowed.

Ah! This is where the code is wrong.

In the code, when processing the jump move from (1,3) (right wall, x=3, t=1):

new_x =3 +2 =5. new_wall is 0 (left). So the code checks if left[5-1] is '-', which is left[4], which is 'X' → unsafe. Hence, this move is not allowed. So the code does not add (0,5) to the queue.

But in my previous analysis of the code's steps, I thought that the code allowed this, but that's a mistake.

So the code correctly checks that the new_x's cell is safe. So in sample input 2, the ninja cannot jump to x=5 on the left wall, because it's 'X'.

Thus, the code for sample input 2 would not have added (0,5) to the queue, and thus the code would return NO.

So why in the previous analysis of the code's steps did I think that (0,5) was added? Because I made a mistake in the analysis.

So the code correctly handles this case.

Thus, the code is correct and passes the sample input 2.

But when I initially tested the code with sample input 2, I incorrectly thought that the code would process (0,5) and escape. But that's a mistake because the code checks the new_x's cell for safety.

Thus, the code is correct.

So the code should correctly handle both sample inputs.

Another thing to note is that in the code, when the ninja is at (1,3) (right wall, x=3, t=1), the code processes the jump move:

new_wall=0 (left), new_x=3+2=5.

Check if left[5-1] == '-', which is left[4] which is 'X' → unsafe. So this move is not added to the queue.

Thus, the code correctly skips this move.

Thus, in sample input 2, the code returns NO.

So the code is correct.

Thus, the code should handle all cases correctly.

Now, let's implement this in Python.
</think>

```python
import sys
from collections import deque

def main():
    n, k = map(int, sys.stdin.readline().split())
    left_wall = sys.stdin.readline().strip()
    right_wall = sys.stdin.readline().strip()
    
    left_dist = [-1] * (n + 2)
    right_dist = [-1] * (n + 2)
    left_dist[1] = 0
    q = deque([(0, 1)])  # 0 for left, 1 for right
    
    found = False
    while q:
        wall, x = q.popleft()
        current_t = left_dist[x] if wall == 0 else right_dist[x]
        
        if x <= current_t:
            continue
        
        # Move up
        new_x = x + 1
        new_t = current_t + 1
        if new_x > n:
            print("YES")
            found = True
            break
        else:
            if (wall == 0 and left_wall[new_x - 1] == '-') or (wall == 1 and right_wall[new_x - 1] == '-'):
                if new_x > new_t:
                    if wall == 0:
                        if left_dist[new_x] == -1:
                            left_dist[new_x] = new_t
                            q.append((0, new_x))
                    else:
                        if right_dist[new_x] == -1:
                            right_dist[new_x] = new_t
                            q.append((1, new_x))
        
        # Move down
        new_x = x - 1
        new_t = current_t + 1
        if new_x >= 1:
            if (wall == 0 and left_wall[new_x - 1] == '-') or (wall == 1 and right_wall[new_x - 1] == '-'):
                if new_x > new_t:
                    if wall == 0:
                        if left_dist[new_x] == -1:
                            left_dist[new_x] = new_t
                            q.append((0, new_x))
                    else:
                        if right_dist[new_x] == -1:
                            right_dist[new_x] = new_t
                            q.append((1, new_x))
        
        # Jump
        new_wall = 1 - wall
        new_x = x + k
        new_t = current_t + 1
        if new_x > n:
            print("YES")
            found = True
            break
        else:
            if (new_wall == 0 and left_wall[new_x - 1] == '-') or (new_wall == 1 and right_wall[new_x - 1] == '-'):
                if new_x > new_t:
                    if new_wall == 0:
                        if left_dist[new_x] == -1:
                            left_dist[new_x] = new_t
                            q.append((0, new_x))
                    else:
                        if right_dist[new_x] == -1:
                            right_dist[new_x] = new_t
                            q.append((1, new_x))
    
    if not found:
        print("NO")

if __name__ == "__main__":
    main()
```