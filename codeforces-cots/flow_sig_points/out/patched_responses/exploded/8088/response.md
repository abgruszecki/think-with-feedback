<think>
Okay, let's see. The problem is about simulating the shooting of birds on wires and how the birds redistribute after each shot. Hmm. So, the initial setup is n wires, each with some number of birds. When a bird is shot on wire xi at position yi (1-based), all birds to the left of it jump up to the previous wire (xi-1), if it exists. And all to the right jump down to the next wire (xi+1), if that exists. Those on non-existent wires fly away. Then, the dead bird is removed. Oh right, and the order of the shots matters because each shot affects the current state.

So, the challenge is to model this process efficiently. The constraints are n and m up to 100, which isn't too bad. Even with m=100, each step can be handled in O(1) per wire, maybe. Let's think about how to model each shot.

Let's break down each shot step by step. Suppose we have wire x (1-based). The yi-th bird is shot. So, on wire x, there are a total of a[x] birds. When the shot happens:

- The yi-th bird is removed.
- All birds to the left (positions 1 to yi-1) move up to x-1. But if x-1 is 0 (i.e., x is the first wire), they fly away.
- All birds to the right (positions yi+1 to a[x]) move down to x+1. If x+1 exceeds n, they fly away.

Wait, but in the problem statement, after the shot, the birds to the left and right are the ones moving. So, for example, if the shot is at position yi on wire x:

The number of birds that move up is (yi-1) birds. Because those are the ones left of the dead bird. Similarly, the number of birds moving down is (a[x] - yi) birds. Because the dead bird is at position yi, and the right side is from yi+1 to a[x], which is (a[x] - yi) birds.

Wait, but the initial count is a[x], and after the shot, the dead bird is removed. So the original number of birds on the wire x is a[x]. After the shot, the remaining birds are (yi-1) + (a[x] - yi) = a[x] -1 (since the dead bird is removed). But the left and right birds are moving. So the steps would be:

For the current shot on x (xi), and yi-th bird:

1. The original count on x is a[x]. Let's call it original_count = a[x].

2. Check if yi is between 1 and original_count, inclusive. But the problem states that it's guaranteed, so we don't have to handle invalid inputs.

3. The left_birds = yi - 1. Because there are yi-1 birds to the left.

4. The right_birds = original_count - yi. Because from yi+1 to original_count, there are (original_count - yi) birds.

5. Then, the dead bird is removed. So after processing, the wire x will have 0 birds left, because all the left and right birds have moved, and the dead one is gone. Wait no. Wait, when you shoot the yi-th bird, all the left ones (positions 1..yi-1) jump up, the right ones (positions yi+1..a[x]) jump down. Then the dead bird (position yi) is removed. So after the shot, wire x's count is left_birds + right_birds? No, wait, no. Because after the shot, the left and right birds have moved. So the original wire x's birds are all gone except the dead one, but the dead one is removed. Wait no. The left birds jump up (so they leave the wire x), the right ones jump down (leaving wire x), and the dead bird is removed. So after the shot, wire x's count is zero? Because all the left and right have moved, and the dead is removed. So for example, if the original a[x] was 10, and yi is 5. Left is 4, right is 5. So after the shot, wire x has 0, because all left and right birds left. Then, the left birds (4) are added to x-1 (if exists), and right birds (5) added to x+1 (if exists).

Wait, that's correct. Because when the shot happens, all the birds to the left of the dead one (positions 1 to yi-1) jump up. So they leave wire x and go to x-1. All the birds to the right (yi+1 to a[x]) jump down. So they leave x and go to x+1. The dead one is removed. So wire x's new count is zero (assuming left and right birds were all moved, but the dead bird is subtracted). So the total for x is (yi-1) (left) + (original_count - yi) (right) is (original_count - 1) birds. But all of these are moved away, and the dead is removed. So wire x's count becomes 0. Because all left and right have moved, and the dead is gone.

So for each shot:

- Calculate left_birds = yi - 1.

- right_birds = original_count - yi.

- Then:

   - If x-1 >= 1, add left_birds to wire x-1.

   - If x+1 <= n, add right_birds to wire x+1.

   - Set wire x to 0 (since all birds are gone except the dead, which is removed).

Wait, but wait. The original count was a[x] birds. So the dead is in position yi. So after processing, the wire x has left_birds (moved to x-1) + right_birds (moved to x+1) + the dead bird. But the dead is removed. So the original a[x] was left_birds + right_birds + 1 (dead). So after removing the dead, the wire x has left_birds + right_birds, but those were all moved away. Wait, no. Because the left and right birds are leaving the wire. So the wire x's count becomes zero. Because all the left and right are moved, and the dead is gone.

Yes. So wire x's count after the shot is zero, because all birds are either moved or dead.

So the steps for each shot are:

1. Get xi (the wire number) and yi (the position of the bird to shoot).

2. current_wire = xi - 1 (since Python lists are 0-based, and the problem uses 1-based for input). Or wait, in code, perhaps we have a list where index 0 is wire 1? No, better to use 0-based for the list. So for the input, xi is 1-based. So when stored in a list, wire 0 is xi=1, wire 1 is xi=2, etc. Wait no, no. Let's say the input is:

n=5, wires 1-5. So the list in Python can be a list with indexes 0-4, corresponding to wires 1-5. So when the input is xi (1-based), we subtract 1 to get the index. So for example, if the input is xi=2, then the index is 1.

So for each shot:

xi_input = the input's xi (1-based), so the index in the list is xi_idx = xi_input - 1.

yi is the position (1-based) on that wire.

Then:

original_count = a[xi_idx]

left_birds = yi - 1

right_birds = original_count - yi

So, the birds to the left (left_birds) will go to xi-1 wire (xi_input-1, which is xi_idx-1 in list), if exists.

Similarly, right_birds go to xi+1 (xi_input+1, xi_idx+1 in list), if exists.

Then, the wire xi_idx's count becomes 0. Because all left and right have moved, and the dead is removed.

So in code, for each shot:

xi, yi = map(int, input().split())

xi_idx = xi - 1

current_count = a[xi_idx]

left = yi - 1

right = current_count - yi

# process left

if xi_idx > 0:  # i.e., xi-1 >=1 (since xi is 1-based, xi_idx=0 is the first wire, so xi-1 is 0-based index-1, which would be -1. So wait, for xi_idx-1 to be valid, we need to check if xi_idx > 0? No. Let's think:

Original xi is 1-based. So xi can be 1, 2, ..., n.

xi_idx = xi-1, which is 0-based index.

So for the left movement, they go to the previous wire (xi-1), which in 1-based is (xi-1). So in 0-based index, that's xi_idx-1.

So if xi_idx is 0 (xi=1), then xi_idx-1 is -1, which is invalid. So we can check if xi_idx-1 >=0. Which is the same as xi_idx > 0.

So:

if xi_idx > 0:

    a[xi_idx-1] += left

Similarly, for the right movement:

if xi_idx+1 < n:

    a[xi_idx+1] += right

Then, set a[xi_idx] = 0.

Yes. Because all left and right birds are moved, and the dead is removed. So the current wire has 0 birds left.

So the code for each shot is:

xi, yi = map(int, input().split())

xi_idx = xi - 1

current = a[xi_idx]

left = yi - 1

right = current - yi

if xi_idx > 0:

    a[xi_idx-1] += left

if xi_idx + 1 < n:

    a[xi_idx+1] += right

a[xi_idx] = 0

Wait, but in code, n is the number of wires, so the indices for a are from 0 to n-1. So xi_idx+1 must be less than n to be a valid index. So:

if xi_idx + 1 < n: --> which is xi_input +1 <= n, since xi_idx +1 is (xi-1) +1 = xi. So when xi is n (1-based), xi_idx is n-1. xi_idx+1 is n, which is >=n (since a has indexes up to n-1). So in code, check if xi_idx + 1 < n, which is same as xi_idx +1 <= n-1. So yes.

So for example, if xi is n (xi_idx = n-1), then xi_idx+1 is n, which is not <n. So the right_birds are added to x+1, which doesn't exist, so they fly away.

So this logic should be correct.

Let's test the sample input.

Sample Input 1:

5

10 10 10 10 10

5

2 5 → xi=2 (0-based index 1), yi=5.

Original count on wire 2 (index 1) is 10.

left_birds =5-1=4 → move to wire 1 (index 0).

right_birds=10-5=5 → move to wire 3 (index 2).

So after this shot:

a[1] becomes 0.

a[0] increases by 4 → 10+4=14.

a[2] increases by5 →10+5=15.

The other wires are unchanged.

But the next shot is 3 13. Let's see.

After first shot, the wires are:

14, 0, 15, 10, 10.

Now, the next shot is xi=3 (index 2), yi=13.

Original count on index 2 is 15. So current_count=15.

left =13-1=12. So left_birds=12.

right =15-13=2.

Check if index 2-1=1 >=0: yes. So a[1] +=12 → a[1] was 0 → now 12.

Check if index 2+1=3 <5 → yes. a[3] +=2 →10+2=12.

Then, set a[2] to 0.

So after this shot, the wires are:

14, 12, 0, 12, 10.

Third shot is 2 12.

xi=2 (index 1), yi=12. current_count is 12.

left=12-1=11. So left_birds=11. They would move to index 0.

right=12 -12=0. So no right birds.

So a[0] +=11 →14+11=25.

a[2] (index 1+1=2) is 0, so add 0.

Set a[1] to 0.

So wires after this shot: 25,0,0,12,10.

Fourth shot: 1 13.

xi=1 (index 0), yi=13. current_count=25.

left=12. move to index -1 (invalid, so fly away).

right=25-13=12. move to index 1.

So a[0] becomes 0.

a[1] +=12 →0+12=12.

So wires:0,12,0,12,10.

Fifth shot:4 6. xi=4 (index 3), yi=6.

current_count=12.

left=6-1=5. move to index 2.

right=12-6=6. move to index4.

So a[3-1=2] (index2) is 0 → 0+5=5.

a[3+1=4] (index4) is10+6=16.

a[3] becomes 0.

So final wires:0,12,5,0,16.

Which matches the sample output.

So the code seems correct.

Another sample input:

3

2 4 1

1

2 2 → xi=2 (index1), yi=2.

Original a[1] =4.

left=1. right=4-2=2.

So move left to index0 (if exists). yes, since index1-1=0.

So a[0] +=1 →2+1=3.

move right to index2 (3 exists as 3 is 3, but in 0-based, index2 is 3rd wire. a[1+1=2] is 1 → add 2 →3.

Set a[1] to0.

So final wires are 3,0,3. Which matches the sample.

So the code works for this.

Now, considering the constraints, the code is O(m) per shot, with each step being O(1) operations. Since m is up to 100, and each step is a few operations, this is well within the time constraints.

Regarding the data structures, using a list to represent the wires is straightforward and efficient. Each shot is processed in O(1) time. So the code is optimal.

So the plan is:

- Read n.

- Read the list of a_i's, as a list of integers.

- Read m, then process m shots:

   For each shot:

      read xi, yi.

      compute xi_idx = xi-1.

      current_count = a[xi_idx]

      left = yi-1

      right = current_count - yi

      if xi_idx >0 (i.e., wire xi-1 exists), add left to that wire.

      if xi_idx+1 <n (wire xi+1 exists), add right to that.

      set a[xi_idx] to 0.

Then, output the a list, each element on a separate line.

So the code should be straightforward.

Now, code in Python:

Read n via int(input())

Then read the next line as list(map(int, input().split())).

Then read m, then read m lines.

Then process each as per above.

Edge Cases:

- When n=1. Then, any left or right movement would go to non-existent wires, so all left and right birds fly away, and the current wire is set to 0.

- When yi=1: left_birds=0, so nothing moves up. Only right_birds = current_count -1. So all to the right (if any) move down.

Similarly, when yi= a[xi_idx], then right_birds=0. So only left_birds = yi-1 move up.

So code handles these cases.

Another case: when the current wire has 0 after processing. For example, if a shot is made when the wire has exactly one bird. Then left and right are 0 and 0. So the wire becomes 0, and no additions to adjacent wires.

So code seems solid.

Now, let's code this.

Read the inputs:

n = int(input())

a = list(map(int, input().split()))

m = int(input())

for _ in range(m):

    xi, yi = map(int, input().split())

    xi_idx = xi -1

    current = a[xi_idx]

    left = yi -1

    right = current - yi

    # add left to xi-1 wire (if exists)

    if xi_idx >0:

        a[xi_idx -1] += left

    # add right to xi+1 (if exists)

    if xi_idx +1 < n:

        a[xi_idx +1] += right

    # set current wire to 0

    a[xi_idx] =0

Then, print each element in a, each on a new line.

Wait, but the output expects each line to be the number of birds on the i-th wire. The input's a1 is the first line, etc. So after processing, print each element of the list, each on a new line.

Yes.

So the code is:

n = int(input())

a = list(map(int, input().split()))

m = int(input())

for _ in range(m):

    xi, yi = map(int, input().split())

    xi_idx = xi - 1

    current = a[xi_idx]

    left = yi - 1

    right = current - yi

    if xi_idx > 0:

        a[xi_idx -1] += left

    if xi_idx + 1 < n:

        a[xi_idx +1] += right

    a[xi_idx] = 0

for num in a:

    print(num)

This should handle all cases.

Testing with sample inputs.

First sample input:

5

10 10 10 10 10

5

2 5 → code steps:

xi=2, xi_idx=1.

current=10.

left=4, right=5.

xi_idx>0 → yes (1>0). a[0] +=4 →10+4=14.

xi_idx+1=2 <5 → yes. a[2] +=5 →10+5=15.

a[1] =0.

Then next steps as before.

Which gives the correct output.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    xi, yi = map(int, input().split())
    xi_idx = xi - 1
    current = a[xi_idx]
    left = yi - 1
    right = current - yi
    if xi_idx > 0:
        a[xi_idx - 1] += left
    if xi_idx + 1 < n:
        a[xi_idx + 1] += right
    a[xi_idx] = 0
for num in a:
    print(num)
```