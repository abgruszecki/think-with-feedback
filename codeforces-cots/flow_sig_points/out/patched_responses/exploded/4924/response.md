<think>
Okay, let's tackle this problem. So the problem is about Anya launching apps on her smartphone, and each time she does, the app's icon moves up one position if possible. We need to calculate the total number of gestures she makes when launching a sequence of apps.

Hmm. Let's parse the problem again. The initial order of the apps is given. Each time an app is launched, if it's not already first, it swaps places with the app before it. So every time you launch an app, its position in the list improves by one (unless it's already first). The gestures are calculated based on the screen the app is on. The screen is determined by the position: each screen has k icons. So for position p (starting from 1?), the screen is (p-1)//k + 1. The initial screen is screen 1, and each time you launch an app, you have to scroll to its screen (t-1 gestures) plus 1 to press. Then after launching, the app moves up if possible, which affects future positions.

So the main challenge is to track the positions of each app efficiently over multiple launches, considering that each launch might change the order. The naive approach would be to simulate each step, but for m up to 1e5, that's O(m) time, which is manageable only if each step is O(1). But tracking positions with a list would be O(n) per swap, which is too slow. So we need a data structure that allows us to track the positions of each app in O(1) time and perform swaps in O(1) time as well.

Wait, each time an app is launched, we swap it with the previous one. So for example, if app X is at position p, after launching, it moves to position p-1 (if p>1). So the swaps are only between consecutive positions. So how can we model this?

We need to represent the current order of the apps. Let's think: for each app, we can track its current position. Also, for each position, we can track which app is there. But when two apps swap, we need to update both their positions and the entries in the position array.

Yes. Let's have two arrays (or dictionaries):

- pos: pos[app] gives its current position (1-based)
- apps: apps[p] gives the app at position p.

So when app b is launched:

If its position is >1:

- The app before it is apps[pos[b] - 1], let's call it a.

- We swap a and b. So:

pos[a] becomes pos[b], and pos[b] becomes pos[b] - 1.

Then, in the apps array, we swap the entries at pos[b] and pos[b]-1.

Wait, the order here matters. Let's see. For example, original positions: a is at p-1, b is at p.

After swap, a is at p, b is at p-1.

So:

apps[p-1] = b

apps[p] = a

So yes, this can be modeled by swapping the entries in apps for positions p and p-1 (where p is the original position of b).

So the steps when app b is launched (assuming pos[b] > 1):

original_p = pos[b]

prev_p = original_p - 1

a = apps[prev_p]

swap a and b:

pos[a] = original_p

pos[b] = prev_p

apps[original_p] = a

apps[prev_p] = b

This way, each swap is O(1) time.

So for each launch, we can:

1. Find the current position of the app (pos[b_i]).

2. Calculate the screen number (screen = (p-1) // k + 1). The gestures for this launch are (screen - 1) + 1 = screen.

Add that to the total.

3. Then, if p > 1, swap with the previous app.

So the key is to model the positions and the apps array correctly, and update them in O(1) time for each launch.

Now, considering that n and m can be up to 1e5, using arrays (lists in Python) for pos and apps would be efficient. Because accessing and updating elements in a list is O(1).

So the steps are:

- Read the initial order into the apps list. Since positions are 1-based, perhaps we can index the list from 1 to n. But in Python, lists are 0-based, so maybe adjust accordingly.

Wait, for example, the initial order is given as a1, a2, ..., an, which are the apps in positions 1 to n. So for apps, we can have a list where apps[0] is a1 (position 1?), or perhaps apps[1] is a1. To make it easier, maybe we can use 1-based indexes. So we can create a list of size n+1, where apps[1] is the first app, etc. Similarly, the pos dictionary (or list) will have pos[app] = position (1-based).

Yes. So initial setup:

apps = [0]*(n+1)  # apps[1..n] hold the initial a1..an.

pos = [0]*(n+1)  # pos[app] gives its current position (1-based).

So for i in 0 to m-1 (since the input is given as a list of m apps to launch):

Read the initial a1, a2, ..., an. Then for each i in 1..n, set apps[i] = a[i-1], and pos[apps[i]] = i.

Then, for each of the m launches:

Take b_j. Get its current position p = pos[b_j].

Compute the screen: (p-1) // k + 1. Add (screen-1) + 1 = screen to total.

Then, if p > 1:

- The previous app is apps[p-1], which is a.

- Swap their positions:

   pos[a] = p

   pos[b_j] = p-1

   apps[p] = a

   apps[p-1] = b_j

This way, each step is O(1) time. For m steps, this is O(m) time, which is acceptable for 1e5.

So the main data structures are the apps and pos arrays.

Now, handling the initial input. Let's see.

First, read n, m, k.

Then, read the a1 to an as a list, say a = list(map(int, input().split())).

Then, apps[1] = a[0], apps[2] = a[1], etc.

So for i in 1..n:

apps[i] = a[i-1]

pos[apps[i]] = i.

So for example, in the first sample input:

n=8, m=3, k=3.

Initial a list is 1,2,3,4,5,6,7,8.

So apps[1] = 1, apps[2] =2, etc. pos[1] =1, pos[2]=2, ..., pos[8] =8.

Then, when app 7 is launched. Its position is 7.

Screen is (7-1)/3 +1 = 6/3 +1=2+1=3. So gestures 3 (screen-1) +1 =3 gestures. Wait, no: the problem says gestures are (t-1) +1, where t is the screen number. So the total for each launch is (t-1) +1 = t. Wait, no. Let's recheck:

The gestures for launching an app on screen t is (t-1) gestures to scroll, plus 1 to press. So total t gestures.

So for app 7, which is in position 7. Screen t is (7-1)//3 +1= 2 +1=3. So 3 gestures. That's correct.

Then, after launching 7, since it's not first (position 7), it swaps with app 6 (position 6). So now 7 is at 6, 6 is at 7.

So next time when app 8 is launched, its position is 8. Screen (8-1)//3 =7//3=2, screen 3. So 3 gestures again.

Then, app 8 is moved to position 7 (swapped with app 6 at position 7?), no wait. Wait, after the first launch:

After app 7 (original position 7) is launched, it swaps with app in position 6, which is app 6. So now app 7 is at 6, app6 at7. So app7's pos is 6, app6's pos is7. apps[6] =7, apps[7]=6.

Then when app8 is launched. Its position is 8. Screen (8-1)//3=7//3=2, screen 3. So 3 gestures. Then since position8 is not 1, swap with app6 (position7). Wait, no. App8 is in position8. The previous app is apps[7], which is6. So after swap, app8 moves to7, app6 moves to8. So app8's position becomes7, app6's becomes8.

So when next app1 is launched, its position is1. Screen1: 1 gesture.

So total 3+3+1=7, which matches the sample.

So the approach works.

Now, let's think about the second sample input:

Input:

5 4 2

3 1 5 2 4

4 4 4 4

Initial apps:

positions 1:3, 2:1,3:5,4:2,5:4.

So pos[3] =1, pos[1]=2, pos5=3, pos2=4, pos4=5.

The sequence is 4,4,4,4.

First launch 4:

current pos is5. screen (5-1)/2 +1=4/2=2 +1=3. gestures 3.

Then, since position5 is not 1, swap with app in position4, which is2.

So now, apps[4] is4, apps5 is2. pos[4]=4, pos2=5.

Next launch 4: position4.

screen (4-1)/2 =3//2=1, screen 2. gestures 2.

swap with app in position3:5.

apps[3] becomes4, apps4 becomes5.

pos[4] =3, pos5=4.

Third launch4: position3.

screen (3-1)/2=1, screen 2. gestures2.

swap with app in position2:1.

apps[2] becomes4, apps3 becomes1.

pos4=2, pos1=3.

Fourth launch4: position2.

screen (2-1)/2=0.5, so screen1. gestures1.

swap with app in position1:3.

apps1 becomes4, apps2 becomes3.

pos4=1, pos3=2.

Total gestures:3 +2 +2 +1 =8.

Which matches the sample.

So the algorithm works for that case.

Now, the key is to implement this in Python efficiently.

Now, in Python, using lists for apps and pos. But since n can be up to 1e5, initializing a list of size n+1 (for 1-based indices) is manageable.

So steps for code:

Read n, m, k.

Read the initial list a: list of n integers.

Read the list of m queries: list of m integers.

Initialize apps as [0]*(n+1), pos as [0]*(n+1).

For i from 1 to n:

   apps[i] = a[i-1]

   pos[ apps[i] ] = i

Initialize total_gestures =0

For each b in the m queries:

   p = pos[b]

   screen = (p-1) //k +1

   total_gestures += screen

   if p >1:

       # swap with previous app

       a_prev = apps[p-1]

       # update pos

       pos[a_prev] = p

       pos[b] = p-1

       # update apps

       apps[p-1], apps[p] = b, a_prev

Print total_gestures.

Yes, this should work.

But wait, in Python, for n=1e5, initializing a list of size 1e5+1 is feasible. Also, for m=1e5 steps, each step is O(1).

So this code should run efficiently within the time constraints.

Now, let's test this code with the first sample.

Sample input 1:

8 3 3

1 2 3 4 5 6 7 8

7 8 1

apps after initialization:

apps[1] =1, apps[2]=2, ..., apps[8]=8.

pos[1]=1, etc.

First b is7:

p=7. screen=(7-1)/3=2 → screen3. total +=3.

p>1. So swap with apps[6] (6).

a_prev is apps[6] =6.

pos[6] becomes7, pos[7] becomes6.

apps[6] becomes7, apps[7] becomes6.

Next b is8:

p=8. screen (8-1)//3=7//3=2 → screen3. total +=3 →6.

p>1. swap with apps[7] which is6.

pos[6] becomes8, pos[8] becomes7.

apps[7] becomes8, apps[8] becomes6.

Third b is1:

p=1. screen is (0)//3+1=1. total +=1 →7.

No swap.

So total 7. Correct.

Second sample:

n=5, m=4, k=2.

Initial a:3 1 5 2 4 → apps[1]=3, apps[2]=1, apps3=5, apps4=2, apps5=4.

queries:4,4,4,4.

First query4:

pos[4] =5.

screen (5-1)/2 =2 → screen3. total +=3.

swap with apps4=2. So pos[2] becomes5, pos4 becomes4. apps[4] and apps5 are swapped.

Second query4:

pos4=4. screen (4-1)/2=1.5 → screen2. total=3+2=5.

swap with apps3=5. So pos5 becomes4, pos4 becomes3. apps3=4, apps4=5.

Third query4:

pos4=3. screen (3-1)/2=1 → screen2. total=5+2=7.

swap with apps2=1. pos1 becomes3, pos4 becomes2. apps2=4, apps3=1.

Fourth query4:

pos4=2. screen (2-1)/2=0 → screen1. total=7+1=8.

swap with apps1=3. pos3 becomes2, pos4 becomes1. apps1=4, apps2=3.

Total is 8. Correct.

So the code works.

Now, considering the constraints. For n up to 1e5, the lists apps and pos are manageable. For m up to 1e5, each step is O(1), so total O(m) steps.

Thus, this code should pass all test cases.

Now, implement this in Python.

But in Python, for reading input, when the input is large, using input().split() can be slow. So it's better to read from sys.stdin. But in code submission, the standard way is to read via input(), but sometimes for very large inputs, using sys.stdin.readline is better.

But given that m is up to 1e5, and the third line (the list of m numbers) is a line of up to 1e5 numbers, split may take time. So perhaps using:

import sys

n, m, k = map(int, sys.stdin.readline().split())

Then the initial a list: a = list(map(int, sys.stdin.readline().split())).

Then the b list: b = list(map(int, sys.stdin.readline().split())).

But in the problem statement, the third line is m integers. So yes.

But sometimes, the third line could have more or less than m numbers. But the problem says it's correct, so the code can proceed.

So the code is:

Read the three variables.

Read a as list of n elements.

Read b as list of m elements.

Then, initialize apps and pos.

Then process each element in b.

Thus, the code would be:

import sys

n, m, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

b = list(map(int, sys.stdin.readline().split()))

apps = [0] * (n + 1)

pos = [0] * (n + 1)

for i in range(1, n+1):

    apps[i] = a[i-1]

    pos[apps[i]] = i

total = 0

for x in b:

    p = pos[x]

    screen = (p-1) // k + 1

    total += screen

    if p > 1:

        prev_app = apps[p-1]

        # swap x and prev_app

        pos[prev_app] = p

        pos[x] = p-1

        apps[p-1], apps[p] = x, prev_app

print(total)

Yes, this code should work.

Testing with the first sample:

The first line:

8 3 3

a becomes [1,2,3,4,5,6,7,8]

apps[1] =1, etc.

b becomes [7,8,1]

Processing:

7's p is7. screen 3. total=3.

swap with apps[6]=6. So apps[6] becomes7, apps[7]=6. pos[6]=7, pos[7]=6.

Next 8: p=8. screen3. total 6.

swap with apps[7]=6. apps[7]=8, apps[8]=6. pos[6]=8, pos[8]=7.

Next 1: p=1. screen1. total7. no swap.

Thus, correct.

Second sample:

n=5, m=4, k=2.

a is [3,1,5,2,4].

apps[1] =3, apps[2] =1, apps3=5, apps4=2, apps5=4.

pos[3]=1, pos[1]=2, pos[5]=3, pos[2]=4, pos[4]=5.

b is [4,4,4,4].

First 4: p=5. screen (5-1)/2 +1=2+1=3. total=3. swap with apps[4]=2. pos[2] becomes5, pos4 becomes4. apps[4] and 5 are swapped.

Then next 4 is at p=4. screen (4-1)/2=1.5 → 1. screen=2. total=5. swap with apps3=5. apps3 becomes4, apps4 becomes5. pos5=4, pos4=3.

Next 4: p=3. screen (3-1)/2=1 → screen2. total=7. swap with apps2=1. apps2 becomes4, apps3=1. pos4=2, pos1=3.

Next 4: p=2. screen (2-1)/2=0 → screen1. total=8. swap with apps1=3. pos3=2, pos4=1. apps1=4, apps2=3.

Thus, total 8. Correct.

Thus, the code works.
</think>

```python
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    
    apps = [0] * (n + 1)
    pos = [0] * (n + 1)
    
    for i in range(1, n+1):
        apps[i] = a[i-1]
        pos[apps[i]] = i
    
    total = 0
    for x in b:
        p = pos[x]
        screen = (p - 1) // k + 1
        total += screen
        
        if p > 1:
            prev_app = apps[p-1]
            pos[prev_app], pos[x] = p, p-1
            apps[p-1], apps[p] = x, prev_app
    
    print(total)

if __name__ == "__main__":
    main()
```