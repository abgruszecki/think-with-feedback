<think>
Okay, let's see. The problem is to determine how much to increase Tokitsukaze's HP by 0, 1, or 2 to get the highest possible category. The categories are ordered A > B > C > D. So for each possible a (0,1,2), we need to compute the new HP (x + a) and find its category. Then select the a that gives the highest category. If there's a tie, choose the smallest a.

First, let's figure out how to determine the category for a given number. The categories are based on the remainder when divided by 4. Let's list them out:

- If (x+a) mod 4 is 1 → A
- mod 3 → B
- mod 2 → C (but wait, wait. Wait, original definitions are:

Category A is 4n+1 → remainder 1 when divided by 4.
B is 4n+3 → remainder 3.
C is 4n+2 → remainder 2.
D is 4n → remainder 0.

So the mod 4 result gives us the category directly. For example:

mod 4 | category:
0 → D
1 → A
2 → C
3 → B

Wait, that's important. So for a number, compute mod 4. Then:

remainder 1 → A
3 → B
2 → C
0 → D.

So the priority order is A (highest) then B, then C, then D.

So the approach is: for each possible a (0,1,2), compute x+a, then mod 4, and find the category. Then among the three options, choose the a that gives the highest category. If multiple a's give the same highest category, pick the smallest a.

So the steps are:

1. For a in 0,1,2:
   a. compute new_hp = x + a
   b. compute rem = new_hp % 4
   c. determine the category based on rem.
2. Compare the three categories (for a=0,1,2) and select the best one. If two a's give the same category, pick the smaller a.

So how do we represent the categories and their priorities? Maybe assign a priority value. For example:

A: priority 4 (highest)
B: 3
C: 2
D: 1

Then for each a, calculate the priority, and select the a with the highest priority. If same priority, pick the smallest a.

So let's code this.

Let's think about the steps.

Given x, iterate a from 0 to 2.

For each a, compute new_hp = x + a.

Then rem = new_hp %4.

Then category:

if rem ==1: A

elif rem ==3: B

elif rem ==2: C

else (rem 0): D.

Then for each a, determine the category's priority.

We need to track the best a (the one with highest priority, and smallest a in case of ties).

So for each possible a (0,1,2):

Compute the category, then compare with the current best.

We can track the best a as follows:

Initialize best_priority to -infinity, best_a to 0, best_category to something.

For a in 0,1,2:

   compute category.

   get its priority.

   if priority > best_priority:

       update best_priority, best_a, best_category.

   elif priority == best_priority:

       if a < best_a:

           update best_a and best_category (but same priority).

So after checking all three a's, output the best_a and best_category.

So code steps:

Read x.

Compute for a=0,1,2:

new_x = x + a.

rem = new_x %4.

Then map rem to category.

Then compare.

Examples:

First sample input 33.

x=33. Check a=0: 33 mod4 is 33/4=8*4=32, remainder 1. So category A. priority 4.

a=1: 34 mod4 is 34-8*4=34-32=2 → rem2 → C. priority 2.

a=2: 35 mod4 is 35-8*4=35-32=3 → rem3 → B. priority3.

So best is a=0, category A.

Second sample: 98.

a=0: 98 mod4. 4*24=96 → rem 2 → C (priority2).

a=1: 99 mod4: 99-24*4=99-96=3 → B (priority3).

a=2: 100 mod4 → 0 → D (priority1).

So best is a=1, B.

So code needs to handle that.

Now, implementing this in Python.

First, read x. Then for each a in 0,1,2:

compute new_x = x +a.

rem = new_x %4.

Then determine category based on rem.

Then compare.

So code:

x = int(input())

best_a = -1

best_priority = -1

best_cat = ''

for a in range(3):

    new_x = x +a

    rem = new_x %4

    if rem ==1:

        cat = 'A'

        priority =4

    elif rem ==3:

        cat = 'B'

        priority =3

    elif rem ==2:

        cat = 'C'

        priority =2

    else:  # rem 0

        cat = 'D'

        priority =1

    # compare

    if priority > best_priority:

        best_priority = priority

        best_a =a

        best_cat = cat

    elif priority == best_priority:

        if a < best_a:

            best_a =a

            # cat is same as previous, so no need to change

print(f"{best_a} {best_cat}")

Wait, but what if two a's have the same priority and same a? Well, since a is 0,1,2, and we check in order, the first one (smallest a) will be chosen. Wait, but in the loop, a is 0,1,2. For example, if a=0 and a=1 have same priority. Then, when a=0 is checked, best_priority is set, best_a is 0. Then a=1 comes, priority is same as current best. So the code checks if a (1) is less than best_a (0), which is not. So no change. So in this case, the best_a remains 0. Which is correct, because for same priority, we choose the smallest a.

So the code is correct.

Testing the first sample:

x=33, a=0: priority4. So best becomes a=0.

Then a=1: priority2, so not better.

a=2: priority3, not better. So output 0 A.

Second sample: x=98.

a=0: priority2 (C). So best_priority is 2.

a=1: priority3 (B). So better, set best_a=1, priority3.

a=2: priority1 (D). So not better.

Thus, output 1 B.

Another test case: x=34 (34 mod4 is 2 → category C). Let's see:

a=0: 34 → C (priority2).

a=1: 35 → 35 mod4 is 3 → B (priority3). Better.

a=2:36 mod4 is 0 → D (priority1). So best is a=1, B.

Another test: x=35. 35 mod4 is 3 → B.

a=0 → B (priority3).

a=1 →36 mod4 0 → D (priority1).

a=2 →37 mod4 1 → A (priority4). So best a=2, A.

So output 2 A.

Thus code works.

So this approach is O(1) time, which is acceptable for any x up to 1e18. But here x is up to 100. So no problem.

So the code is correct and optimal. The data structures are minimal. Just iterate 3 possibilities, check each, and track the best. No need for any complex structures.
</think>

```python
x = int(input())
best_a = 0
best_priority = -1
best_cat = ''

for a in range(3):
    rem = (x + a) % 4
    if rem == 1:
        cat, priority = 'A', 4
    elif rem == 3:
        cat, priority = 'B', 3
    elif rem == 2:
        cat, priority = 'C', 2
    else:
        cat, priority = 'D', 1
    
    if priority > best_priority or (priority == best_priority and a < best_a):
        best_priority = priority
        best_a = a
        best_cat = cat

print(f"{best_a} {best_cat}")
```