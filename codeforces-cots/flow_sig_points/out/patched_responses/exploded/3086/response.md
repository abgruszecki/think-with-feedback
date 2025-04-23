<think>
Okay, let's see. The problem is about determining if we can reach cell t starting from cell 1 by using the portals in a Line World. Each portal i allows us to move from cell i to cell i + a_i. And we can't move back. So the question is whether following these portals step by step leads us to cell t.

Hmm, the approach here must be efficient because n can be up to 3e4, which is 30,000. So any O(n) algorithm would be acceptable, but anything more than that like O(n^2) would be too slow.

Let's think of how the movement works. Starting at cell 1, each time we can take the portal from the current cell. So the next cell is current + a[current_pos]. So the path is determined by the a values. We need to simulate this until we either reach t or go beyond it.

Wait, but simulating step by step might be O(n) time. For example, if the path is 1 → 1+a1 → next cell, etc. So for each step, we move to the next cell. So the maximum steps would be up to n-1 steps (if you step through each cell). But even 3e4 steps are manageable in Python within 2 seconds.

So the plan is:

1. Start at position 1.
2. At each step, use the portal at the current position to move to next cell (current + a_i). But wait, the portals are numbered from 1 to n-1. So for each cell i (from 1 to n-1), the portal leads to i + a_i. So when we are in cell i, we can only take that portal once, and that's the next step. So the path is deterministic. Each step is determined by the a_i values. So the path is fixed once you start.

So the process is like:

current = 1
while current < n:
    current += a[current-1] (since a is 0-based in the input but the cells are 1-based)
    if current == t:
        return YES
if current == t:  # but since t is <=n, and a[i] is <= n-i, this would only happen if t is n and current reaches it?
But according to the problem statement, the portals can't take you out of the line world. So a[i] is at most n-i. So the maximum you can get from cell i is i + (n-i) = n. So the path will end at cell n eventually.

Wait, but in the problem statement, it's given that using the transportation system, you can't leave the Line World. So the portals are set such that you'll never go beyond n. So the path will eventually reach cell n. So the process will terminate either when you reach t before n, or when you reach n (if t is n, then you can reach it). Otherwise, if you never hit t along the way, then output is no.

So the algorithm is straightforward: simulate the jumps starting at 1. At each step, move to next cell using the a[i] of the current cell. Check if any step lands on t. If yes, output YES. If we reach cell n without hitting t, output NO.

So for example, in the first sample input:

n=8, t=4.

a = [1,2,1,2,1,2,1]

The steps would be:

current starts at 1.

First, use portal 1 (a_0 in 0-based) which is 1. So current becomes 1+1=2.

Check if 2 is 4? No.

Next, current is 2. Use portal 2 (a_1=2), so 2+2=4. Now current is 4. Which matches t=4. So output YES.

In the second example, t=5. The path steps are:

1 → 2 (a[0]=1), then 2 → 4 (a[1]=2), then 4 →6 (a[3]=2), then 6→7 (a[5]=1), then 7→8 (a[6]=1). So the path is 1,2,4,6,7,8. So 5 is not in the path. So output NO.

So the simulation approach is correct. Now, how to implement this in Python efficiently.

The steps are:

- Read n and t.

- Read the list a (n-1 elements).

- Start at position current = 1.

- While current < t:

   - Check if current is 1, then move to current + a[0]. Wait, no: the portals are for each cell. So when current is i, we use a[i-1], because the input is a list of a_1 to a_{n-1} (assuming 0-based here). Wait, no: the input is a1 to a_{n-1}, which are the portals 1 to n-1, each portal i (1-based) connects i to i + a_i. So the portals are in 1-based numbering, and the input list is in the order a1, a2, ..., a_{n-1}. So for the current cell i (1-based), the portal i's a_i is a[i-1] in the input list.

So for example, when current is 1, the portal is a1, which is the first element of the input. So current becomes 1 + a[0].

Then, current is 1 + a[0]. Then, if current is equal to t, return YES. Otherwise, continue.

So the loop is:

current = 1

while current < n:

   if current == t:

       print YES and exit.

   next_current = current + a[current-1]

   current = next_current

After the loop, check if current == t (in case t is n).

So code steps:

Read n, t.

Read list a as integers.

current = 1

while True:

   if current == t:

       print "YES"

       exit.

   if current > t:  # because the next steps can't go back, once we pass t, no need to check.

       break.

   if current >= n:  # reached end

       break.

   current += a[current-1]

After loop, check if current == t? Wait, no. Because once current >=n, the loop breaks. But if t is n, then current could be equal to n. So after the loop, check if current == t.

Wait, the loop will break when current >=n. Because in the loop condition, we have 'current < n' as the loop condition. Wait, no. Let me think again.

The code would be something like:

current = 1

while current < n:

   if current == t:

       print("YES")

       exit.

   next = current + a[current-1]

   current = next

After the loop ends (current >=n), check if current == t. Because if t is n, then current could have reached n, which is equal to t. So in that case, output YES.

Else, output NO.

Wait, let's see:

If t is n, then during the loop, current will be 1, then next steps. For example, if in the loop, current is 5, and a[4] is (n-5) (since a[i] can be up to n - i). So current becomes 5 + (n-5) = n. Then, the loop condition is current <n? No. So the loop exits. Then, check if current ==t. Since t is n, output YES.

Yes.

So the code steps:

Read n and t.

Read the list a.

current =1.

while current <n:

   if current ==t:

       print YES and exit.

   current += a[current-1]

After loop:

if current ==t:

   print YES

else:

   print NO.

Yes. Because the loop runs as long as current is less than n. So when current reaches n, the loop stops. Then check if current equals t.

So this code would handle all cases correctly.

Now, for the input:

For example, when n=8, t=8. Then during the loop, each step adds the a[i], and when current becomes 8, the loop stops. Then, check if current is t (8), output YES.

So this approach is correct.

Now, what about time constraints? For the worst case, when t is n. Then the loop would have to process each cell from 1 to n-1, adding each a[i] which is 1 each time, leading to O(n) steps. But n is up to 3e4, which is manageable in Python. Because 3e4 steps are trivial for Python's speed.

So the algorithm is O(n), which is acceptable.

So the code is straightforward. Let's code this.

In Python:

n, t = map(int, input().split())

a = list(map(int, input().split()))

current = 1

while current < n:

    if current == t:

        print("YES")

        exit()

    current += a[current-1]

print("YES" if current == t else "NO")

Wait, but in Python, 'exit()' is not the best way. Instead, perhaps, once current reaches t, break and print.

But in the code above, when current is in the loop, and equals t, print YES and exit. Then, after the loop, check if current ==t.

Wait, but during the loop, current is checked before updating. Let me see:

Wait, the code is:

current starts at 1.

Loop condition: current <n.

Inside loop:

if current ==t: print yes and exit.

then, current += a[current-1].

So, for example, if current is 4 (t=4) in the first iteration, print yes.

But if during the loop, current is 3 and a[3-1] is 1, then next current is 4. Then, in next iteration, the loop condition is 4 <n (say n=8). So loop runs again. Then check if current ==t (4). So print yes.

So the code is correct.

Yes.

So this code should handle all cases correctly.

Testing sample input 1:

n=8, t=4.

a is [1,2,1,2,1,2,1].

current starts at 1.

Loop runs since 1 <8.

Check current (1) ==4? No.

current +=a[0] (1) → becomes 2.

Loop again (2<8). Check 2==4? No.

current +=a[1] (2) →2+2=4.

Check in next loop iteration:

current is 4 <8: loop runs.

Check 4 ==4 → yes. Print YES and exit.

Sample 2:

n=8, t=5.

a is [1,2,1,2,1,1,1].

current starts at 1.

Loop: 1 <8.

Check 1 vs5: no.

current +=1 →2.

2 <8: check 2 vs5: no.

current +=a[1] (2) →4.

4 <8: check 4 vs5: no.

current +=a[3] (2) →6.

6 <8: check 6 vs5: no. (5 is smaller than 6, but 6 is larger than t, but in code, the loop continues as long as current <n. So after adding a[3], current is 6, which is <8. So next step is check 6 ==5? No. Then current +=a[5] (which is 1) →7.

Check 7 vs5: no. Add a[6] (1) →8.

Now, current is 8. Loop condition is 8 <8? No. Exit loop.

Check if 8 ==5? No. So print NO.

So code works.

Another test case where t is n.

n=5, t=5.

a = [4,3,2,1]

current =1.

loop:

current <5.

Check 1 ==5? No.

current +=a[0] (4) →5. Now, loop condition 5 <5? No. Exit loop. Check current ==t (5) → yes. So output YES.

So code works.

So this code should handle all cases correctly. Time complexity is O(n), which is acceptable for n up to 3e4.
</think>

```python
n, t = map(int, input().split())
a = list(map(int, input().split()))
current = 1
while current < n:
    if current == t:
        print("YES")
        exit()
    current += a[current-1]
print("YES" if current == t else "NO")
```