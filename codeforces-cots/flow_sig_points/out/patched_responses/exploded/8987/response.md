<think>
Okay, let's see. The problem is about maximizing the convenience of the subway system by changing at most two stations' destinations. The convenience is the number of ordered pairs (x, y) such that you can get from x to y by following the subway trains any number of times. 

First, I need to understand the structure of the subway. Since each station has exactly one outgoing and one incoming edge, the subway consists of a set of cycles. Each cycle is a permutation where each node points to the next in the cycle. So the current setup is a collection of disjoint cycles.

The convenience for a single cycle of size k is k^2. Because for any two nodes x and y in the cycle, x can reach y (since it's a cycle). So for all x and y in the cycle, the pair (x,y) is valid. So the total for a cycle is k*k. If there are multiple cycles, the total convenience is the sum of the squares of each cycle's size. Because nodes from different cycles can't reach each other. So the original convenience is sum of c_i^2 where c_i are the cycle sizes.

Now, the goal is to change up to two edges (pi values) to merge some cycles and maximize the sum. But after changing, the permutation must still form a valid set of cycles (so the Law is maintained). Changing two edges implies that we can merge up to two cycles into one. Wait, no. Because merging two cycles would require breaking each cycle and connecting them. For example, suppose we have two cycles A and B. If we change one node in A to point to a node in B, and another node in B to point back to A, then the two cycles would merge into a single cycle. But how?

Wait, the key here is that each change must not break the permutation structure. So for each node you change, you must adjust another node to maintain the permutation. Because each node's p_i must form a permutation again. So changing a node's p_i from a to b would require that another node's p_j is changed from b to a's original value? Or maybe not. Wait, no. The original permutation is such that all p_i are distinct. So if we change p_i from its original value to some new value, that new value must not be present elsewhere. Wait no, because after changing, the new permutation must still have all p_i distinct. So when you modify up to two nodes, the new p's must still form a permutation.

So, modifying two nodes' p values would mean that their new p's are different from all others, and the permutation remains a permutation. So, the new configuration must be a permutation of 1..n.

Hmm. So the problem allows us to change at most two values in the permutation. The new permutation must also be a permutation (so all elements distinct). The goal is to maximize the sum of squares of cycle sizes.

So the initial sum is the sum of squares of the current cycles. The maximum possible sum can be achieved by merging two cycles into a larger one, because (a + b)^2 = a² + b² + 2ab, which is larger than a² + b². So merging two cycles gives a gain of 2ab. But each merge requires that we can break two cycles and combine them into one.

But how to do that with up to two changes. Let me think. Let's say there are two cycles, A and B. Each cycle is a closed loop. To merge them into a single cycle, we need to connect them. For example, in cycle A, we can change a node's p to point to a node in B. Then in cycle B, change a node's p to point back to A. That way, the two cycles are merged. However, this requires two changes. 

For example, suppose cycle A is a1 → a2 → ... → a_k → a1. Cycle B is b1 → b2 → ... → b_m → b1. If we change a1's p from a2 to b1, and change b1's p from b2 to a2, then the new cycle would be a1 → b1 → a2 → a3 → ... → a_k → a1? Wait, no. Let me see. Let's imagine the original pointers. Suppose a1's next is a2, and a2's next is a3, and so on. Suppose b1's next is b2, etc. 

If we change a1's next to b1, then the cycle becomes a1 → b1 → b2 → ... → b_m → b1 → ... Wait, no. Because after a1 points to b1, then following the path from a1 would go to b1, then follow b1's original next (b2), then through B's cycle until it loops back to b1. Then, how does a2 fit in? Because a2's next is a3, which is still part of cycle A. So this would create two separate cycles: the original A (minus a1) and the B cycle merged with a1. Wait, perhaps not. 

Alternatively, maybe changing two nodes' pointers can merge two cycles into one. Let's take two cycles. To merge them, you need to create a path that connects them. For instance, in cycle A, take a node x and change its next to a node y in cycle B. Then, in cycle B, take a node z and change its next to x's original next. This way, the two cycles are merged. But how?

Alternatively, perhaps each merge of two cycles can be done with two changes. Let's see. Let's take two cycles C1 and C2. To merge them into a single cycle, you can find a node in C1 (say, a) and a node in C2 (say, b). Change a's next to point to the original next of b, and change b's next to point to the original next of a. Wait, maybe that's not correct. Let's take an example. Suppose C1 is 1 → 2 → 1 (size 2). C2 is 3 → 4 → 3 (size 2). So the current sum is 4 + 4 = 8. If we can merge them into a single cycle of size 4, the sum would be 16, which is better. To do that, maybe change 2's next from 1 to 3, and 4's next from 3 to 1. Then the cycle would be 1 → 2 →3 →4 →1. That's a cycle of size 4. So two changes here. So merging two cycles of sizes a and b gives a gain of (a + b)^2 - a² - b² = 2ab. So if we can merge the two largest cycles, this would give the maximum possible gain. 

Therefore, the optimal strategy is to merge the two largest cycles. The gain would be 2ab. So the maximum possible sum would be the original sum minus a² - b² + (a + b)^2 = original sum + 2ab. 

But what if there's only one cycle? Then changing two edges can't split it, because splitting a cycle into two would require changing two edges, but the permutation must still be valid. For example, suppose the cycle is 1 →2 →3 →1. If you change 2's next to 3 (so 2 →3) and 3's next to 2, then you split into two cycles: 1 →2 →3 →2 (no, that's not valid because 3 points to 2, 2 points to 3, so that's a cycle of 2 and 3. Then 1's next is 2, but 2's next is 3, which is part of a cycle. Wait, but the permutation is invalid because 3's next is 2, but 1's next is 2. So p would have two nodes pointing to 2. That's not allowed. So you can't split a single cycle into two by changing two edges. Because that would require creating two pointers to the same node. So when the initial permutation is a single cycle, you can't split it. Therefore, if the initial sum is n², then changing two edges can't create a larger sum. So the maximum possible sum is n². 

But what if the initial sum has some cycles and merging two gives a higher sum? So the approach is: compute the original sum. Then find the top two largest cycles. The gain would be 2ab. Add that to the original sum minus a² - b². 

But wait, the original sum is sum of squares. So if you have two cycles a and b, then their contribution is a² + b². Merging them gives (a + b)^2. The difference is 2ab. So the maximum gain possible by merging two cycles is 2ab. Therefore, the optimal approach is to find the two largest cycles, and compute the original sum plus 2ab. 

But what if there are multiple cycles? For example, if there are three cycles of sizes a, b, c. Then merging the two largest (a and b) would give a gain of 2ab. Alternatively, merging a and c gives 2ac, etc. So choosing the two largest gives maximum gain. 

So the optimal approach is to:

1. Find all cycle sizes in the current permutation.

2. If there are at least two cycles, compute the original sum, then compute the maximum possible gain by merging the two largest cycles (2ab), and add that to the original sum. 

But wait, what if we have more than two cycles? For example, three cycles. Then, merging two of them (the two largest) would add 2ab, but leave the third cycle's contribution as c². So the total would be (a+b)^2 + c² + sum of other cycles. Which is the original sum minus a² - b² + (a + b)^2 + other cycles. Which is original sum + 2ab. 

But the original sum is sum of squares of all cycles, so if we merge two cycles of sizes a and b, the new sum is (sum - a² - b²) + (a + b)^2) = sum + 2ab. 

Therefore, the maximum possible gain from merging any two cycles is 2ab, which is maximized when a and b are the two largest cycles. 

But then what if there's only one cycle? Then merging isn't possible, but maybe we can split into smaller cycles. But as discussed earlier, splitting a cycle into two would require changing two edges but making the permutation invalid. Because splitting would require two nodes to point to the same node, which is not allowed. So that's impossible. So for a single cycle, the original sum is n². Since we can't change anything (unless merging is possible, but there's only one cycle), so the maximum sum remains n². 

But wait, the problem allows changing up to two stations. So what if there's a single cycle, but you can't split it, but maybe adding more edges. Wait, no. If there's a single cycle, changing two edges can't create a larger sum. Because the sum is already n², which is the maximum possible. So in that case, you can't do anything. So the answer is n². 

So the algorithm is:

- Find all cycle sizes.

- If there are multiple cycles, compute the original sum plus 2ab where a and b are the two largest cycle sizes.

- Else, the original sum is already n², which is the maximum possible.

But wait, what if there are more than two cycles? Then merging the two largest cycles gives the maximum possible gain. Because 2ab is the maximum possible when a and b are the two largest. 

So the steps are:

Compute the original sum (sum of squares of cycle sizes).

If the number of cycles is 1, output the original sum (since changing two edges can't create a larger sum).

Else, find the two largest cycle sizes, compute original_sum + 2*a*b, and output that.

Wait, but what if there's another way to merge three cycles into one with two changes? For example, suppose there are three cycles. To merge all three into one, perhaps with two changes. But how?

Hmm. Let's think: Suppose there are three cycles, A (size a), B (size b), C (size c). To merge them into one cycle, you would need to connect them. For example, connect A and B into a single cycle (requires two changes), then connect the combined AB cycle with C. But that would require another two changes, which is over the allowed two changes. So no. Therefore, with two changes, you can merge at most two cycles. So the maximum gain is merging the two largest cycles. 

Therefore, the optimal approach is to compute the sum of squares of cycle sizes, then add 2ab where a and b are the two largest cycle sizes. If there are two or more cycles, otherwise, nothing. 

But wait, what if there's a case where merging three cycles in two changes is possible? Let me see. Let's say there's three cycles: A (a), B (b), C (c). Suppose we can find a way to merge all three into one with two changes.

How? For example, take a node from A and point it to a node in B. Then take a node from B and point it to a node in C. Then, the cycles would form a single cycle? Let's see. 

Original cycles: A is x → ... → x (size a), B is y → ... → y (size b), C is z → ... → z (size c). 

Change x's next to y, and y's next to z. Then the new cycle is x → y → z → ... → y's original next → ... → x? Not sure. This would require that the rest of the cycles are connected. But I think that changing two nodes' pointers can merge three cycles into one. Let me take an example.

Example: three cycles of size 1 each. Let's say 1 →1, 2 →2, 3 →3. 

If we change 1's next to 2, and 2's next to 3. Then the cycles would be 1 →2 →3 →3. Wait, no. Because 3's next is still 3. So after the changes, 1 →2 →3 →3, which is a cycle of 3. But the cycle would be 1→2→3→3. So 1's next is 2, 2's next is 3, 3's next is 3. So 3's cycle is itself, and 1's cycle is 1→2→3→3. So 1, 2, 3. But 3 is a self-loop. So the cycles are now 1→2→3→3 (so the cycle is 3, and 1→2→3). Wait, maybe not. Let's see:

Original cycles: each node points to itself.

After changing 1's next to 2 and 2's next to 3:

1 →2 →3 (but 3 still points to itself). So starting at 1: 1→2→3→3, so the cycle is 3. Then starting at 2: 2→3→3. So cycle is 3. So the cycles are 1→2→3→3. Wait, no. Because 1's next is 2, which's next is 3. 3's next is itself. So from 1, we go to 2, then to 3, then stop. So the path from 1 is 1→2→3. So the reachable nodes from 1 are 2 and 3. But 3 can't reach 1. So the pairs (1,1), (1,2), (1,3), (2,3), (2,2), (3,3). Wait, but this isn't a cycle. So the sum would be 3 (from the original 3's cycle) plus 2 (from 1 and 2's cycle?) Wait, no. Because 1's cycle is 1 →2 →3 →3, but 3 is a cycle. So the cycles are:

- 3 is a cycle of size 1.

- 1 →2 →3 →3, but since 3 is part of its own cycle, maybe this forms a chain leading to 3. So 1's cycle is actually a cycle of size 1 (since eventually you loop on 3). Wait, but 3's next is itself. So after changing the pointers, the permutation would have 1→2, 2→3, 3→3. So the cycles are 1→2→3→3, but 3's next is itself. So 1's next is 2, 2's next is 3, 3's next is 3. So the cycle for 3 is itself, and the cycle for 1 and 2 is 1→2→3→3 (but that's not a cycle). Because when you reach 3, you loop there. So the cycle for 1 is 1→2→3→3, but that's not a cycle. So the cycles would be 3, and then 1→2→3. But that's not a valid permutation. Because 3's next is 3, but 2's next is 3. So 3 is pointed to by two nodes (2 and itself). Which violates the permutation's uniqueness. 

Ah, right. Because the problem states that after the changes, the permutation must still be a permutation, i.e., each node's p_i must be unique. So in the example above, changing 1's p_i to 2 (originally, 1's p_i was 1) and 2's p_i to 3 (originally 2's p_i was 2) would result in p_3 = 3, p_2 =3 (no, wait, original p_3 is 3. So after changes, p_1=2, p_2=3, p_3=3. Then p_3 is duplicated (appears in p_2 and p_3). So that's invalid. So in that case, the changes would result in an invalid permutation, which is not allowed. 

Therefore, when making changes, the new permutation must have all p_i distinct. Therefore, any change must be such that the new p_i is not already present elsewhere. 

So to merge three cycles into one with two changes is impossible. Because merging three cycles would require three changes. For example, each cycle requires a change to connect to the next. So merging three cycles into one would need at least two changes, but perhaps not possible. Let's think again.

Wait, suppose there are three cycles: A (a), B (b), C (c). To merge all three into one, you need to connect them. For example, take a node in A (x) and change its next to a node in B (y). Then take a node in B (y) and change its next to a node in C (z). Then take a node in C (z) and change its next to x. But that's three changes, which is not allowed. So with two changes, you can only connect two cycles. Therefore, the maximum possible gain is when you merge two cycles. 

So, the conclusion is that the optimal approach is to merge the two largest cycles. Therefore, the solution is to compute the original sum, then add 2ab where a and b are the two largest cycle sizes. If there's only one cycle, then the sum remains the same. 

Now, the problem allows changing up to two stations. But according to our analysis, merging two cycles requires two changes (like changing two nodes' pointers). So in that case, the two changes are allowed (since changing two nodes is <=2). 

So, the steps are:

1. Find all cycle sizes in the permutation.

2. Compute the original sum as sum of squares of cycle sizes.

3. If the number of cycles is 1, output the original sum.

4. Else, find the two largest cycle sizes a and b. The maximum possible sum is original_sum - a² - b² + (a + b)^2 = original_sum + 2*a*b. 

But wait, what if there are more than two cycles, but merging two of them gives a larger sum than merging others. So the two largest cycles are the ones to merge. 

So, the code can be structured as follows:

- First, compute the cycles in the permutation. For each node, if not visited, traverse until we find the cycle. Record the size.

- Sort the cycles in descending order.

- Compute the sum as sum of squares.

- If the number of cycles is 1: output sum.

- Else: compute sum + 2 * (a * b), where a is the first element in sorted list, b the second. Output this value.

Now, let's test this with the examples.

First example:

Input:

3

2 1 3

The permutation is [2,1,3]. So the cycles are:

1 →2 →1 (size 2), and 3 →3 (size 1). The original sum is 2² +1² =5. Then, merging 2 and 1 gives a sum of (2+1)^2=9. Which is the correct output. So our code would compute sum + 2*2*1 =5 +4=9. Which matches.

Second example:

Input:

5

1 5 4 3 2

The permutation is 1→1, 5→2→5, 4→3→4. So cycles are [1] (size 1), [5,2] (size 2), [4,3] (size 2). Original sum is 1 +4 +4=9. The two largest are 2 and 2. Merging them gives 2+2=4. Their square is 16. So the new sum is 9 -4 -4 +16 =17. Which matches the sample output.

So the code seems to handle these cases.

Another example: single cycle. Like n=3, permutation [2,3,1]. The original sum is 9. So output is 9.

Another test case: n=4, two cycles of size 2. Original sum 4+4=8. Merging gives (2+2)^2=16. So sum + 2*2*2=8+8=16. Correct.

Now, how to compute the cycles in the permutation?

We can do a standard cycle detection: for each node from 1 to n, if not visited, traverse until we loop back. Mark all nodes in the cycle and record the size.

For n up to 1e5, this is O(n), which is acceptable.

So the code steps:

Read n.

Read p as a list (note that the input is 1-based? The problem says pi are 1-based, since pi is the destination station. So the permutation is given as a list of 1-based elements.)

So for example, the first sample input is 3 stations with p = [2,1,3]. So the permutation is 1→2, 2→1, 3→3.

So the code will process each node, track visited, and find cycles.

Once cycles are found, collect their sizes, sort in descending order.

Then compute the sum, and if there are at least two cycles, add 2*a*b, else the sum remains the same.

Now, code in Python:

We need to read n, read the list p (0-based or 1-based?), but the input is given as p1 to pn, which are the destinations for stations 1 to n.

So in Python, the input is read as a list, but since Python uses 0-based indexing, perhaps we need to adjust. Wait, in the code:

The stations are 1-based. So for station i (1-based), pi is given as the next station. So the list is 0-based in Python, but the values are 1-based. So the code should process 1-based indexes.

Wait, no. Let's see. Suppose the input is 3, and the list [2,1,3]. Then station 1's next is 2, station 2's next is 1, station 3's next is 3.

So the permutation is stored in a list where the index is 0-based (assuming Python reads the list as 0-based). So perhaps in code, for i in 0 to n-1, the next node is p[i] (1-based). Wait, no. Because the input is given as p1, p2, ..., pn. So for station 1 (i=0 in 0-based), the next is p1 (the first element in the list, which is at index 0). So the list is 0-based for the indices (i from 0 to n-1), but the values are 1-based. So when processing, when we are at station (i+1) (since station numbers are 1-based), the next station is p[i] (which is 1-based). 

So to model the permutation correctly, the code can create a list where for index i (0-based), the value is p[i]-1 (converting to 0-based). Then, the permutation can be processed as a standard permutation of 0-based indexes. 

Yes. Because, for example, if the input is [2,1,3], then the code will convert p[0] (2) to 1, p[1] (1) to 0, p[2] (3) to 2. So the permutation becomes [1, 0, 2]. Then, the cycles are 0 →1 →0 (size 2), and 2 →2 (size 1). So that's correct.

Therefore, in code, first, we read the list p, then convert each element to 0-based by subtracting 1. Then process the permutation as a list of 0-based indexes.

So the code can be written as follows:

Read n.

Read p as list of integers.

Convert each element to p_i-1, resulting in a 0-based permutation.

Then, find cycles in this permutation.

Once cycles are found, compute the sum of squares.

Sort the cycle sizes in descending order.

If there are at least two cycles, compute sum + 2*a*b.

Else, sum remains the same.

So the code:

n = int(input())
p = list(map(int, input().split()))
p = [x-1 for x in p]

visited = [False]*n
cycles = []

for i in range(n):
    if not visited[i]:
        current = i
        cycle = []
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = p[current]
        cycles.append(len(cycle))

sum_sq = sum(c*c for c in cycles)
if len(cycles) >=2:
    cycles.sort(reverse=True)
    a = cycles[0]
    b = cycles[1]
    sum_sq += 2*a*b

print(sum_sq)

Wait, but this is the case where we can merge the two largest cycles. So the code would compute sum_sq as the original sum, then add 2*a*b (the gain from merging the two cycles) and output that. 

Testing the first example:

Input 3, p = [2,1,3]. Converted to [1,0,2]. Cycles are of sizes 2 and 1. sum_sq is 4 + 1 =5. Then, adding 2*2*1=4, giving 9. Correct.

Second example:

5, p = [1,5,4,3,2]. Converted to [0,4,3,2,1]. The permutation is:

0 →0 (cycle size 1).

1 →4 →1 (cycle size 2).

2 →3 →2 (cycle size 2).

So cycles are [1,2,2]. sum_sq is 1+4+4=9. Then merging the two largest (2 and 2) gives 9 + 2*2*2= 17. Correct.

Another test case with a single cycle. For example, n=3, p = [2,3,1]. Converted to [1,2,0]. The cycle is 0→1→2→0. Size 3. sum_sq is 9. Since only one cycle, output 9.

So this code should work.

But what if there's a case where there are three cycles, and the two largest are not the first two? For example, cycles of sizes 3, 2, 2. The two largest are 3 and 2. So merging gives 2*3*2=12. Original sum is 9 +4+4=17. New sum 17 +12=29. So correct.

So the code is correct.

So this should be the solution.
</think>

```python
n = int(input())
p = list(map(lambda x: int(x)-1, input().split()))
visited = [False] * n
cycles = []

for i in range(n):
    if not visited[i]:
        cnt = 0
        j = i
        while not visited[j]:
            visited[j] = True
            cnt += 1
            j = p[j]
        cycles.append(cnt)

total = sum(c**2 for c in cycles)
if len(cycles) > 1:
    cycles.sort(reverse=True)
    total += 2 * cycles[0] * cycles[1]

print(total)
```