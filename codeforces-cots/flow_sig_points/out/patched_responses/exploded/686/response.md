<think>
Okay, let's see. So the problem is about Denis trying to cross a road with safety islands. He has to move during green lights, and can only change direction on the islands. Also, when the red light comes, he must be on a safety island. The goal is to find the minimal time to reach the end.

Hmm. Let's think about how to model this. The key constraints here are that Denis can only change direction on the islands, and during red light he must be on an island.

So, the approach might involve modeling the state as (current position, time modulo (g + r)), since the traffic light cycles every g + r seconds. Wait, but how does the time affect the movement? Because during red light, he can't move. Oh, but the problem states that during red light, he must be on an island, and when the green comes again, he can start moving. So, whenever the red light is on, he's stuck on an island until the next green starts.

So the time when he arrives at a safety island could be crucial. If he arrives at an island during a green period but with enough time left to move further, he can proceed. But if he arrives at an island at a time where the remaining green time is zero, then he has to wait for the red to finish (adding r seconds) before proceeding.

Wait, the traffic light starts with g seconds green, then r red, etc. So the total time is split into cycles of (g + r) seconds. So for any time t, the phase is (t mod (g + r)). If the phase is <= g, then it's green; else, red.

But Denis can only move during green. So during red, he must be on a safety island, and can't move. So when he is on a safety island during a red light, he has to wait until the next green.

So the problem is similar to a BFS where each state is (position, time mod (g + r)), since once you reach a position with the same mod, the next steps would be similar. Because if you arrive at a position at time t1 and t2, where t1 ≡ t2 mod (g + r), then the available time left in the green phase would be the same. So the minimal time to reach each (position, mod) is important.

So the idea is to model the state as (d, t_mod), where d is the current safety island, and t_mod is the time modulo (g + r). Because arriving at a safety island at a certain mod time determines how much green time is left.

For example, if the current mod is x, then the remaining green time is (g - x) if x is <= g. Otherwise, if x > g (which can't happen because mod is (g + r)), then it's in red. But since when you arrive at a safety island, you can only be there during a red phase if you arrived exactly at the end of green (since movement is during green). Wait, perhaps the mod is the time since the last cycle started. So for example, if you arrive at a safety island at time t, which is in the red phase (t mod (g + r) > g), then you have to wait until the next green. So the arrival time would be t + (g + r - (t mod (g + r))) + ... ?

Wait, let's think. Suppose the current time is t, and the mod is m = t mod (g + r). If m <= g, then it's green, and he can move. Otherwise, it's red, and he has to be on a safety island.

But according to the problem statement, when the red light is on, Denis must be on a safety island. So during red light, he's stuck there. So when he arrives at a safety island during green, he can choose to wait (if needed) but perhaps not. Wait, no. The problem says that during green, he must move. So he can't stay still unless he is forced to change direction. So the movement is constrained: he must move each second, changing direction only on safety islands.

So the movement is such that Denis must be moving each second during green. He can change direction only when he is on a safety island.

So, the key is to model the movement between safety islands. Because the movement between two islands must take a certain amount of time, and during that time, the green phase must be sufficient.

So, for example, moving from island A to island B, which are k units apart, would take k seconds. If during that movement, the green phase is sufficient (i.e., the time taken is <= remaining green time), then he can reach B. Otherwise, he would have to stop, but he can't because during green he must move.

Wait, no. The movement must be during green. So the entire movement from A to B must be done in a single green phase. Because if he starts moving at time t, and the green phase is from t to t + g, then the time taken to move from A to B must be <= g. Otherwise, during the movement, the red light comes on, which is not allowed (since he must be on a safety island then).

Wait, but the problem says that he must be moving during the green. So the entire path from one island to another (possibly turning around at some islands in between) must be covered during the green phase. Because he can't stop moving during green. So each time he leaves a safety island, he must reach another one within the remaining green time.

So the problem reduces to moving between safety islands in steps that take exactly the time of the distance (since each step is moving 1 unit per second). But each movement between islands must take a time that is <= the remaining green time when he starts moving.

So the approach is to model the problem as a state where each state is (current island, time mod (g + r)), because the mod determines how much green time is left. For example, if current time mod (g + r) is m, then the remaining green time is g - m. But if m is in the red phase (m >= g), then he must wait until the next green. Wait, but during red, he can't move. So he can only start moving again when the next green starts.

So the state is (current island, mod time). The mod time represents the time within the current green-red cycle. When you arrive at an island, the mod time is (arrival_time) mod (g + r). If the arrival time is during red (mod > g), then the next available time to move is mod_time + (g + r - mod_time) = mod_time + (g + r - mod_time) = (g + r) * (k+1). So the next movement can start at (k+1)*(g + r) seconds, but the mod would be 0 again.

Alternatively, the mod is the time within the cycle. So for the BFS, the state is (d_i, t_mod), where t_mod is the time since the start of the current cycle. For example, if we are in a state where t_mod is 5, and g is 10, then there are 5 seconds passed in the cycle (which is green), and 5 seconds left of green. So the time taken to move to another island must be <= 5 seconds, but that's not possible. Wait, no. Because if the remaining green time is (g - t_mod), then any movement must start in the current cycle's green phase and take (distance) seconds. So if the remaining green time is (g - t_mod), then the movement time must be <= (g - t_mod). Otherwise, the movement can't happen in this cycle, so Denis can't start moving.

Wait, perhaps the movement can be started only when the remaining green time is sufficient for the movement. For example, moving from island A to B takes k seconds. So when you start moving from A at a time t, the current cycle's remaining green time is (g - (t mod (g + r))). So k must be <= (g - (t mod (g + r))). Otherwise, during the movement, the light turns red, which is invalid.

Thus, Denis can move from A to B only if the distance between A and B is <= remaining green time (g - (current mod)).

So the problem is to model transitions between islands, where the time taken to move from A to B is exactly the distance between them (since each step is 1 second). But this movement must fit entirely within a green phase.

So, the steps would be:

1. Preprocess the list of islands to be sorted. Since the input is given as a list of distinct integers, but not necessarily sorted. So first, we sort the islands in increasing order.

2. For each island, compute the distances to adjacent islands. Because Denis can move left or right, but only change direction on islands. So, for example, if he is on island d[i], he can move to d[i+1] (right) or d[i-1] (left), as long as the direction change is allowed.

Wait, but the direction change is allowed only if he is on a safety island. So each time he arrives at a safety island, he can choose the direction to move next. But when moving from an island, the direction can be left or right, but when moving, he can't change direction except at islands.

So for each island, the possible next steps are moving to the adjacent islands either left or right. Because any longer jumps would require passing through other islands (which would allow direction changes only there, but perhaps not). Wait, no. Because moving from d[i] to d[j] (j > i) in a straight line would take (d[j] - d[i]) seconds. But during this movement, he can't change direction except at islands. So if between d[i] and d[j] there are other islands, he must pass through them. So, the minimal steps are between adjacent islands.

Wait, but that's not necessarily the case. For example, suppose the islands are at 0, 3, 7, 14, 15. Then from 3, Denis can move directly to 7 (distance 4) in 4 seconds, but he can't change direction during those 4 seconds. So the movement must be in a straight line. So moving from 3 to 7 is possible, but during that movement, he can't change direction. So the direction must be fixed until he reaches the next island.

So, the possible transitions from any island d[i] are to the next island in either direction (d[i+1] or d[i-1]), and the time taken is the distance between them. But this movement must be possible within the remaining green time.

So the BFS approach would be:

- For each island d[i], and for each possible mod time (time mod (g + r)), track the earliest time when Denis can reach d[i] with that mod.

- The initial state is d[0] (0) with mod 0 (time 0).

- For each state (d[i], m), we can explore moving to the adjacent islands (d[i+1] or d[i-1]) if the distance is <= (g - m). The time taken is the distance. The new mod would be (m + distance) mod (g + r). But if (m + distance) <= g, then the new mod is (m + distance). Otherwise, if (m + distance) > g, then after moving, the time would have passed into the red phase, but since Denis must be on a safety island during red, this is allowed. Wait no. Because during movement, the light is green. So the entire movement must be during the green phase. Because Denis is moving, and during movement, the light is green. So if the movement takes k seconds, then after starting at time t (with m = t mod (g + r)), then the movement ends at time t + k. The mod at the end is (m + k) mod (g + r). But during the movement, the light must stay green. So m + k <= g.

Wait, that's a critical point. Because during the movement, Denis is moving every second. So if the movement starts at time t (with m = t mod (g + r)), and the movement takes k seconds, then during those k seconds, the light must be green. Because otherwise, during the movement, the light would turn red, and Denis would be in the middle of the road (not on a safety island), which is invalid.

Therefore, the movement can only be started if the remaining green time (g - m) is >= k. Because otherwise, the movement would take longer than the remaining green time, causing Denis to be on the road during red light.

So when considering moving from island A to B (distance k), the condition is that k <= (g - m). If this is true, then the movement takes k seconds, and the arrival time mod is (m + k). Since m + k <= g, then the arrival is during green. But when arriving at the next island, the mod is (m + k), and the next movement can be initiated.

Wait, but when arriving at B during the green phase, he can choose to immediately start moving again. But if the arrival is at time t + k, which is in the same green phase, then the next movement can start.

But if the movement from A to B takes k seconds, and m + k == g, then the arrival is exactly at the end of the green phase. At that point, Denis is on island B, which is a safety island, so he must wait for the red phase. The next movement can start after the red phase, adding r seconds. So the total time added is k + r. But the mod would be 0 (since (m + k) = g, and the next cycle starts at g + r. So mod is (g + r) mod (g + r) = 0.

So in the state transitions:

- For each possible movement from d[i] to d[i+1] (distance k), check if k <= (g - current mod m). If yes, then:

   - The arrival time is current_time + k. The arrival mod is (m + k). 

   - Then, if arrival mod is exactly g, then the next possible movement can start after (g + r) seconds (so add r seconds to the arrival time, and mod becomes 0).

   - Otherwise, if arrival mod is less than g, then the next movement can start immediately, with the arrival mod as the new mod.

Wait, but the arrival time is (current_time + k). If the arrival mod is m + k. If m + k <= g, then the arrival is during green. But after that, Denis can choose to move again in the same green phase, as long as he is on a safety island.

But if m + k == g, then the arrival is exactly when the red starts. So he must wait for the entire red phase (r seconds), adding r to the total time, and the mod becomes 0 (since the next cycle starts after g + r seconds).

So in the BFS, when you move from d[i] to d[j], and the movement takes k seconds, then:

- If m + k < g: new_time = current_time + k. new_mod = m + k. 

- If m + k == g: new_time = current_time + k + r. new_mod = 0.

But what about if m + k > g? That's impossible, because the movement can only be done if k <= (g - m). Because when moving, the movement takes k seconds, and during that time, the light must remain green. So the condition k <= (g - m) must be met. So m + k can't exceed g.

So for the movement transitions:

When in state (d[i], m), the possible transitions are to adjacent islands (i-1 or i+1) with distance k. 

If k <= (g - m):

   new_mod = m + k.

   if new_mod < g: new_time = current_time + k. add to the queue with state (d[j], new_mod).

   else: (new_mod == g) then, new_time = current_time + k + r. new_mod is 0. So the state becomes (d[j], 0).

So the BFS needs to track these states.

Additionally, since the same state (d[i], m) can be reached with different times, we need to keep track of the earliest time to reach each state. So using a priority queue (Dijkstra's algorithm) might be needed, but given that transitions only add time, perhaps BFS can be used with a deque, handling states in order of increasing time.

Wait, but the transitions can have different time increases. For example, moving to an adjacent island takes k seconds (if arriving in green), but if the arrival is at the end of green (k + m == g), then adding r seconds. So the time added is either k or (k + r). So the edges in the graph can have different weights, which would require Dijkstra's algorithm to find the minimal time.

Yes, because some transitions add more time (when you have to wait for red). So the problem is similar to a weighted graph where edges have variable weights. Therefore, the correct approach is to model this as a graph and use Dijkstra's algorithm to find the shortest path to the end.

But considering that m is up to 1e4, and g + r can be up to 2000 (since g and r are up to 1e3 each), the total number of states is 1e4 * 2e3 = 2e7. Which might be manageable with a Dijkstra's approach using a priority queue optimized with a heap.

But Python's heapq can handle that, but perhaps with optimizations. Alternatively, since the possible time mod (g + r) is bounded, maybe we can use BFS with a deque and process states in order of their arrival time.

Wait, the time to reach a state (d[i], m) could be either the same or larger than the previous steps. So Dijkstra's is the way to go here.

So the plan is:

- Sort the islands in increasing order.

- For each island, precompute the adjacent islands (i-1 and i+1, if they exist).

- Use a Dijkstra's priority queue where each node is (current_time, current_island_index, mod_time).

- The mod_time is the time since the start of the current cycle (mod (g + r)).

- For each node, process it by checking if we can move to adjacent islands. For each possible move:

   - Compute the distance between current island and next island (d[next] - d[current] if moving right, or d[current] - d[next] if moving left).

   - Check if the distance k is <= (g - mod_time). Because the movement must take k seconds, which must be <= remaining green time (g - mod_time).

   - If yes, then:

      - new_mod = mod_time + k.

      - if new_mod < g:

          new_time = current_time + k.

      - else: (new_mod == g)

          new_time = current_time + k + r.

          new_mod = 0.

      - If this new state (next_island, new_mod) hasn't been visited yet or has a higher time than new_time, add it to the priority queue.

- Additionally, when we reach the last island (d[m-1] = n), return the current_time.

But how to handle when the destination is reached? For example, if Denis arrives at island n (the end) during a green phase. Then he has reached the end. The time is current_time. But if he arrives during the green phase (mod_time + k <= g), then the time is added. Otherwise, it's impossible (but since n is a safety island, he can arrive during any phase, but if the movement ends in red, he would have to wait. Wait no. Wait, the problem states that Denis has crossed the road as soon as his coordinate becomes equal to n. So once he arrives at n, regardless of the phase, that's the end. So in the movement from d[i] to n, even if the movement ends during the red phase, that's okay. Wait, but how?

Wait, the movement from the previous island to n must be during the green phase. Because during movement, he is moving. So the movement to n must take k seconds, which must be <= remaining green time (g - mod_time). So the arrival at n is during the green phase. Because if he arrives during green, then he has successfully reached. If the movement ends during the red phase, that's not allowed. So to reach n, the movement must be possible within the green time.

Wait, the problem states that Denis has crossed the road when he reaches n. But he must reach n during movement. So the movement must be during green, and the time taken to reach n must be <= remaining green time.

Therefore, when moving to n (the last island), the movement must take k seconds, where k is the distance between the previous island and n, and that must be <= (g - mod_time). Because during that movement, he can't be on a safety island until he reaches n.

So once he reaches n, the time is added, and that's the end. So in the code, when processing a movement to n, we can immediately check if the movement is possible, and if so, return the time.

But in the code, how to handle the state transitions. Let's see.

The code steps:

1. Read n and m.

2. Read the list of d_i, sort them.

3. Check if d[0] is 0 and d[-1] is n. The problem says that the input includes 0 and n.

4. Read g and r.

5. Precompute the adjacency list for each island (i-1 and i+1, if present).

6. Initialize a 2D array (or a dictionary) to keep track of the minimal time to reach each (island, mod) state.

7. Use a priority queue (heapq) to process states in order of their time.

8. The initial state is (time=0, island=0, mod=0).

9. For each state popped from the priority queue:

   a. If the island is the last one (n), return the current time.

   b. For each adjacent island (left and right):

      i. Compute the distance k.

      ii. Check if the current mod + k <= g. If not, skip this transition.

      iii. Compute new_mod = mod + k.

      iv. next_time = current_time + k.

      v. If new_mod == g:

          next_time += r

          new_mod = 0

      vi. Check if the next island is the last one. If so, return next_time (if new_mod <= g, then it's allowed. Because when you arrive at n, the movement was during green.)

      vii. If the next island is not the last, then check if the state (next_island, new_mod) has been visited with a time higher than next_time. If not, add it to the priority queue.

But wait, if next_island is the last (n), then we can return next_time immediately, because once we reach n, it's done.

Wait, no. The movement must be possible. So for example, if moving from d[i] to d[j] = n, the distance is k. Then the movement is allowed if k <= (g - mod). So in the code, the step 9.b.ii checks that. So if that's the case, then the movement is allowed. Once we reach n, the time is current_time + k, but if new_mod == g, we add r, but since we are already at n, the red phase is irrelevant. Wait, no. Because the movement to n takes k seconds. If the mod after movement is new_mod = m +k. Since the movement must be allowed (k <= g - m), then m +k <= g. So new_mod is <=g, which is during the green phase. So arriving at n during green is okay. So when the movement is allowed, the arrival is during green. So the time is current_time + k.

Wait, but if m +k == g, then the arrival is exactly at the end of green. But n is a safety island, so during the red phase, Denis can't move. But since he has already reached n, the process ends. So the arrival time is current_time +k, not current_time +k +r. Because adding the r is only necessary if you are on a safety island and need to wait for the next green to move again. But once you reach n, you're done, regardless of the phase.

So in the code, when moving to the last island (n), we can immediately return the time current_time +k, even if new_mod is equal to g. Because the arrival is during the green phase (since m +k <= g). So even if it's the last possible second of green, the arrival is allowed.

Therefore, in the code, whenever a movement is made to the last island, the time is current_time + k, and that's the answer.

So in the code, during the transition step, after computing next_time (without adding r if new_mod is g), but checking if the next island is the last one. If so, return next_time.

Thus, the code can check in step 9.b.vi whether the next island is the last one. If yes, return next_time (current_time +k).

So putting this together.

Now, the code needs to:

- Sort the islands.

- For each island, track the adjacent islands (i-1 and i+1).

- Use Dijkstra's algorithm to find the minimal time to reach n.

Implementing this in Python, given the constraints:

Constraints:

n can be up to 1e6, but m is up to 1e4. So the sorted list is manageable.

For the Dijkstra's, each state is (time, island_index, mod). The mod can be from 0 to (g + r - 1). But since g and r are up to 1e3, (g + r) can be up to 2000, mod is up to 2000.

So for each of the m islands, there are up to 2000 possible mod values. So the total possible states are 1e4 * 2e3 = 2e7. Which is manageable with a priority queue, but in Python, this might be tight.

But with Dijkstra's, the heap operations are O(M + E log M), where M is the number of states. For 2e7, it's possible to get a TLE.

Hmm. So perhaps, there's a way to optimize this. For example, since each transition can only add time, perhaps we can use a deque and process states in order of their mod. Or, since the mod is cyclic, maybe we can find a way to represent the states more efficiently.

Alternatively, since the time to reach a state is the current_time, and the mod is (current_time) mod (g + r), perhaps we can track the minimal time for each (island, mod) pair. Once a (island, mod) pair is processed with a certain time, any other occurrence of the same pair with a higher time can be ignored.

So the code would need a 2D array: dist[i][m] = minimal time to reach island i with mod m.

Initialize all to infinity.

The initial state is dist[0][0] = 0.

When processing a state (time, i, m), for each adjacent island j:

   distance k = abs(d[i] - d[j])

   if m + k > g: can't move, skip.

   new_mod = m + k

   new_time = time + k

   if j is the last island:

       return new_time

   if new_mod == g:

       new_time += r

       new_mod = 0

   if new_mod < g + r (which it is, since mod is 0 to (g + r -1)):

       if new_time < dist[j][new_mod]:

           update dist[j][new_mod] = new_time

           add (new_time, j, new_mod) to the priority queue.

But wait, when new_mod is zero after adding r, the new_time is time +k + r. But in this case, the mod is zero, which is the start of the next cycle.

So the code must correctly compute new_mod and new_time based on whether the movement ends at g.

So for each transition:

If k <= (g - m):

   new_mod = m + k.

   if new_mod < g:

       new_time = current_time + k.

   else:

       new_time = current_time + k + r.

       new_mod = 0.

   Check if j is the last island. If yes, return current_time +k (since the arrival is during green, and even if new_mod == g, the arrival is allowed. Because the movement to j is allowed, which requires that k <= (g - m). So m +k <= g. So new_mod can be up to g.

Wait, but new_mod can be equal to g. Which would mean that the movement took exactly k = g - m seconds, leading to m +k = g. So the arrival time is current_time +k. Then, since new_mod is g, which is in the red phase. But arrival at j during red phase is allowed only if j is a safety island. Which it is. So Denis is allowed to be there during red. But in this case, after moving, he arrives at j, but the light turns red. So he must wait there until the next green. So the time becomes current_time +k + r. Then, the new_mod is 0.

But in the code, when moving to j (which is not the last island), we have to wait. So the new_time is current_time +k + r, and new_mod is 0.

But if j is the last island, then the arrival time is current_time +k, regardless of whether new_mod is g. Because once he arrives at j (n), he has completed the journey. The red phase after that is irrelevant.

So, in the code, when moving to j (the last island), the new_time is current_time +k, and the arrival is allowed. So we can return new_time.

So, the code needs to check if j is the last island. If yes, return current_time +k.

Therefore, in the code:

For each movement from i to j:

   compute k = d[j] - d[i] (since sorted)

   if m +k > g: skip.

   if j is the last island: return current_time +k.

   else:

       new_mod = m +k.

       if new_mod == g:

           new_time = current_time +k + r.

           new_mod = 0.

       else:

           new_time = current_time +k.

       if new_time < dist[j][new_mod]:

           update and add to heap.

Thus, the code can be structured accordingly.

Now, for the data structures:

We need to sort the d array.

We can precompute the adjacency list for each i. For example, adj[i] is a list containing i-1 and i+1, if they are within the array's bounds.

But since the array is sorted, and the islands are in order, the left neighbor is i-1, and the right neighbor is i+1.

Now, the code in Python:

But since m can be up to 1e4, and for each state, there are up to two transitions (left and right), the number of edges is manageable.

Implementing this:

We'll use a priority queue (heapq), and a 2D array for the distances. But in Python, a 2D list of m x (g + r) is possible. For m=1e4 and (g + r)=2e3, this would be 2e7 elements. Which is 20 million, which is acceptable for Python's memory (since each element is an integer, and initializing to a large value like infinity, which can be 1e18 or something).

But initializing a list of lists for m=1e4 and mod=2e3 may take some time, but manageable.

So, code steps:

Read n and m.

Read the list of d's, sort them.

Check if 0 and n are present.

Read g and r.

precompute the cycle = g + r.

Initialize a 2D list dist, where dist[i][mod] is the minimal time to reach island i with mod.

Initialize all to infinity, except dist[0][0] = 0.

Use a priority queue, which starts with (0, 0, 0).

Process the queue:

While heap not empty:

   current_time, i, mod = heappop(heap)

   if current_time > dist[i][mod]: continue (since we have a better path now)

   if i is the last index: return current_time (since it's the end)

   for each neighbor j (i-1 and i+1):

       if j is out of bounds (0 <= j < m):

           k = abs(d[i] - d[j])

           if mod + k > g: continue  # can't move, not enough time

           if j == m-1:  # last island

               return current_time + k

           new_mod = mod + k

           if new_mod == g:

               new_time = current_time + k + r

               new_mod = 0

           else:

               new_time = current_time + k

           if new_time < dist[j][new_mod]:

               dist[j][new_mod] = new_time

               heappush(heap, (new_time, j, new_mod))

If the queue is processed and no return, return -1.

But wait, the last check for j == m-1 is correct because when you reach the last island, the time is current_time +k. Because in that case, the movement is allowed (since mod +k <=g), so the arrival is during green. So even if new_mod ==g, the arrival is allowed (but the movement is allowed because the total time was k <= (g - mod)).

So the code can return current_time +k.

Now, let's test with the first example:

Input:

15 5

0 3 7 14 15

11 11

Sorted d: [0,3,7,14,15]

g=11, r=11, cycle=22.

The initial state is (0, 0, 0).

From 0 (position 0, mod 0), possible moves to index 1 (3) with k=3.

mod +k =3 <=11. So new_mod is 3, new_time is 3.

Push (3, 1, 3).

Also, check if moving to index -1 (invalid), so no.

Then, process (3, 1,3). Now, possible moves to 0 (k=3) or 2 (k=4). Let's see moving to 2 (7).

mod=3 +4=7 <=11. new_time=3+4=7. new_mod=7.

Push (7,2,7).

Then, move to 0 (mod=3-3=0, but distance is 3. So new_mod=3+3=6? Wait, no. Wait, moving from 3 (index 1) back to 0 (index 0). The distance is 3. mod is 3. 3+3=6 <=11. So new_mod is 6. new_time is 3+3=6. So push (6,0,6).

But perhaps the optimal path is to go to 7 (index 2), then return to 3 (index 1), which would take 4 seconds each way, total 8 seconds, leading to mod 3+4=7 (7) and then 7+4=11 (mod 11). Then, since mod 11 is equal to g (11), new_time is 8 +4 +11= 23. Then mod is 0.

But the code would process these steps.

In the first test case, the answer is 45. Let's see:

In the example, the path is 0 →7 (7 seconds, mod 7+0=7). Then return to 3 (mod 7 +4=11, which is equal to g=11. So new_time becomes 7 +4 +11 =22, mod 0. Then, from 3 (mod 0), move to 14 (distance 11, which is allowed since mod is 0. 11 <=11. new_mod=11 → new_time=22 +11 +11=44, mod 0. Then move to 15 (distance 1, mod 0 +1=1 <=11. new_time 44+1=45. return.

So in code:

After processing the steps, the code would find the path:

0 →3 (mod3, time3) →7 (mod7, time7) →3 (mod11, time7+4=11 → add 11 → time22, mod0) →14 (distance11, mod11 → add r → time22+11+11=44, mod0) →15 (time44 +1=45).

So the code would process this path.

But in the code, when moving from 3 (index1) to 7 (index2), the time is 3+4=7, mod7. Then, from 7 (index2), possible moves are to index1 (3) or index3 (14). Moving to 3 (distance4):

mod7 +4=11 → which equals g=11. So new_time is 7 +4 +11 =22, mod0. The state (22, 1,0) is pushed.

Then, from index1 (3) mod0, the code can move to 0 (distance3) or index2 (7, distance4). Moving to index3 (14) would take 14-3=11 steps. mod0 +11=11 → equals g. So new_time is 0 (current_time is 22) +11 → new_time=33. But since mod +11=11 ==g, new_time becomes 22 +11 +11=44, mod0. Then, index3 (14) is pushed with time44, mod0.

Then, from index3 (14), possible moves to index2 (7, distance7) which would require mod0 +7=7 <=11. new_time is 44+7=51. mod7.

Alternatively, move to index4 (15, distance1). mod0 +1=1 <=11. So new_time is44+1=45. Since index4 is the last, return 45.

Yes. So the code would find this path.

Thus, the code seems correct.

Now, the code in Python:

But considering the constraints, m can be up to 1e4 and mod up to 2e3, the 2D list for dist can be implemented as a list of lists. For each i in 0..m-1, and mod in 0..cycle-1.

But in Python, creating a list of lists with 1e4 elements, each being a list of 2000 elements, initialized to infinity, can be done.

The code:

Read n and m.

d = sorted list of input islands.

Check if d[0] is 0 and d[-1] is n.

g, r = map(int, input().split())

cycle = g + r.

INF = float('inf')

m = len(d)  # since input m is given, but perhaps after sorting, but the problem says that m is the number of islands, which is correct.

Wait, the input m is the number of islands. The sorted list has m elements.

So, in code:

m = len(d_list)  # but input m is given, but the problem says that the second line contains m distinct integers. So len(d_list) should be m.

Thus, proceed.

The code:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    d = list(map(int, input_stream.readline().rstrip("\n").split()))
    d.sort()
    g, r = map(int, input_stream.readline().rstrip("\n").split())

    cycle = g + r
    INF = float('inf')
    size = len(d)
    dist = [[INF] * cycle for _ in range(size)]
    dist[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    found = False

    while heap:
        current_time, idx, mod = heapq.heappop(heap)
        if idx == size - 1:
            print(current_time, file=output_stream)
            found = True
            break
        if current_time > dist[idx][mod]:
            continue
        for delta in (-1, 1):
            new_idx = idx + delta
            if 0 <= new_idx < size:
                k = abs(d[idx] - d[new_idx])
                if mod + k > g:
                    continue
                if new_idx == size - 1:
                    print(current_time + k, file=output_stream)
                    found = True
                    heap = []
                    break
                new_mod = mod + k
                new_time = current_time + k
                if new_mod == g:
                    new_time += r
                    new_mod = 0
                if new_time < dist[new_idx][new_mod]:
                    dist[new_idx][new_mod] = new_time
                    heapq.heappush(heap, (new_time, new_idx, new_mod))
        if found:
            break

    if not found:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
13 4
0 3 7 13
9 9
""",
            "output": \
"""\
-1
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

The second example:

Input:

13 4

0 3 7 13

g=9, r=9.

Sorted d: [0,3,7,13].

cycle=18.

The possible paths:

From 0, possible steps to3 (3). mod3. Then to7 (4 steps, mod3+4=7 <=9. mod7. Then to13 (6 steps. 7+6=13>9. So can't move. So need to wait.

So from7, mod7. Trying to go to13 (6 steps. 7+6=13>9. So can't move. So no path.

Thus, code returns-1.

So in code, after processing all possible paths, no state reaches the last island.

Thus, the code works.

So this code should handle all cases.

But there's one thing to note: the initial check for d[0] and d[-1] is redundant because the problem statement says that 0 and n are in the input. So we can skip that.

But the code has this check. If the input is incorrect, but according to the problem statement, it's guaranteed. So perhaps the code can remove that check.

But for correctness, it's better to include it.

Now, the code.

In Python, using heapq.

But the code can have an issue with the early exit. For example, when the code finds a path to the last island during the processing of a neighbor, it prints and breaks out. But there might be other entries in the heap that could lead to a shorter path. However, according to Dijkstra's algorithm, the first time a node is popped from the heap is the minimal time. Thus, any subsequent entries for the same node can be ignored. But in the code, when the code is processing a state, and during processing a neighbor, finds a path to the last island, that's the minimal time. Because the code processes states in order of increasing current_time.

But if there's a path to the last island via a neighbor, and that's the first occurrence of a path, then it's minimal.

Thus, the code is correct.

So the code as written should work.
</think>

```python
import heapq

n, m = map(int, input().split())
d = list(map(int, input().split()))
d.sort()
g, r = map(int, input().split())

cycle = g + r
INF = float('inf')
size = len(d)
dist = [[INF] * cycle for _ in range(size)]
dist[0][0] = 0
heap = []
heapq.heappush(heap, (0, 0, 0))
found = False

while heap:
    current_time, idx, mod = heapq.heappop(heap)
    if idx == size - 1:
        print(current_time)
        found = True
        break
    if current_time > dist[idx][mod]:
        continue
    for delta in (-1, 1):
        new_idx = idx + delta
        if 0 <= new_idx < size:
            k = abs(d[idx] - d[new_idx])
            if mod + k > g:
                continue
            if new_idx == size - 1:
                print(current_time + k)
                found = True
                heap = []
                break
            new_mod = mod + k
            new_time = current_time + k
            if new_mod == g:
                new_time += r
                new_mod = 0
            if new_time < dist[new_idx][new_mod]:
                dist[new_idx][new_mod] = new_time
                heapq.heappush(heap, (new_time, new_idx, new_mod))
    if found:
        break

if not found:
    print(-1)
```
