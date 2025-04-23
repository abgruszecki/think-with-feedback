<think>
Okay, let's tackle this problem. Hmm, the task is to find the number of supercentral points. So, a supercentral point must have at least one neighbor in each of the four directions: left, right, upper, and lower. 

First, I need to understand how to check for each point if it has these neighbors. Let's break it down. For a given point (x, y), right neighbor must have the same y-coordinate and a larger x. Left neighbor same y and smaller x. Upper same x and larger y. Lower same x and smaller y. 

So for each point, I need to check four conditions. The straightforward approach is, for each point, check if there's any point with the same y and x larger than it (right), same y and x smaller (left), same x and y larger (upper), same x and y smaller (lower). 

But how do I efficiently check these conditions for all points? Let's think about the data structures. 

Maybe we can group points by their x and y coordinates. For example, for checking left and right, perhaps we can group all points by their y-coordinate. Then, for a point (x, y), in the list of points with y-coordinate equal to y, check if there are points with x less than and greater than x. 

Similarly, for upper and lower neighbors, group points by their x-coordinate. So that for a point (x, y), in the group of x, check if there are points with y less than and greater than the current y. 

So the plan is:

1. Create two dictionaries:
   a. One that maps each y-coordinate to a sorted list of x-values. This helps in checking left and right neighbors.
   b. Another that maps each x-coordinate to a sorted list of y-values. This helps in checking upper and lower neighbors.

2. For each point (x, y), check:
   a. In the y-group (from the first dict), are there x-values less than current x (left exists) and greater than current x (right exists).
   b. In the x-group (from the second dict), are there y-values less than current y (lower exists) and greater than current y (upper exists).
   If all four conditions are true, increment the count.

But how do we efficiently check if there are elements less than or greater than a certain value in a sorted list? 

For a sorted list, we can perform a binary search to find the insertion point. For example, for checking if there's a left neighbor, we can check if there's any x in the list for the same y that is less than the current x. So, if the first element in the sorted list is less than x, then there's a left neighbor. Wait, no. Wait, the list is sorted. So for the same y, all x's are in sorted order. So for a given x in that list, if there's a value before it in the list (i.e., the current x is not the first), then there's a left neighbor. Similarly, if there's a value after it (current x is not the last), then right exists.

Wait, that's right! Because the list is sorted. So for example, the group for y has x1, x2, ..., xn sorted. So for a point with x=xk in this group, left neighbor exists if there is any x in the group that is less than xk. That's equivalent to checking if xk is not the first element. Similarly, right neighbor exists if xk is not the last element.

Same for the x-group. For a point (x, y) in the x-group's sorted list of y's, upper neighbor exists if there's a y greater than current (so check if the current y is not the last in the list), and lower exists if there's a y smaller than current (current is not the first).

Wait, but this might not be correct. Because, for example, in the y-group for a certain y, the x's are sorted. So for a point x, if there is at least one x' < x (in the same y group), then left neighbor exists. Similarly for the rest.

So the steps are:

- For each point (x, y), in the y group's x list (sorted), check if there exists x' < x and x'' > x.
- Similarly, in the x group's y list (sorted), check if there exists y' < y and y'' > y.

But how to check this efficiently. For example, in the sorted list of x's for the same y, the list is sorted. So for a given x in the list, if there is any element before it (i.e., index > 0), then left neighbor exists. Similarly, if there's any element after (index < len(list)-1), then right exists.

Wait, no. Because the current x's index in the list might be in the middle. For example, the list could be [1, 3, 5]. If current x is 3, then left (1) exists, right (5) exists. If current x is 1, left doesn't exist. If current x is 5, right doesn't exist.

So for the left neighbor, the condition is whether the current x is not the first in the sorted x list for that y. Similarly for right: current x is not the last.

Similarly, for the upper and lower neighbors: in the sorted list of y's for the same x, current y's position must not be first (so lower neighbor exists) and not last (upper exists).

So the approach is:

1. Preprocess the points into two dictionaries:
   a. For each y, collect all x's and sort them.
   b. For each x, collect all y's and sort them.

2. For each point (x, y), check in the y's x-list (sorted) if x is not the first (has left) and not the last (has right). Then check in x's y-list (sorted) if y is not the first (has lower) and not the last (has upper). If all four conditions are met, count it.

So, how to implement this?

First, read all the points, and build these two dictionaries.

For example, for the first sample input:

8
1 1
4 2
3 1
1 2
0 2
0 1
1 0
1 3

The y dictionary would map each y to a sorted list of x's. Let's see:

y=0: x=1 (from (1,0))
y=1: x=0 (from (0,1)), 1 (from (1,1)), 3 (from (3,1)), 4 (from (4,2) no wait, no. Wait (4,2) has y=2. So for y=1, the points are (1,1), (3,1), (0,1). Wait, let's recheck.

Wait sample input has 8 points:

Points:

(1,1), (4,2), (3,1), (1,2), (0,2), (0,1), (1,0), (1,3)

So for y=1: x's are 1 (from (1,1)), 3 (from (3,1)), 0 (from (0,1)). Wait, no. Let's list all points where y is 1:

Looking through the list:

1 1 → y=1, x=1.

3 1 → y=1, x=3.

0 1 → y=1, x=0.

So the x's for y=1 are [0, 1, 3], sorted. So in the y_dict, y=1 maps to [0,1,3]. 

So for point (1,1) which is in this list, its index is 1. So it's not the first (has left neighbor 0) and not the last (has right neighbor 3). So left and right conditions are met.

Then, for x=1, check the x_dict. For x=1, the points have y-values 0,1,2,3 (from (1,0), (1,1), (1,2), (1,3)). So sorted y list is [0,1,2,3]. For point (1,1), which is in this list, it's index 1. So not first (has lower 0) and not last (has upper 2 and 3). So upper and lower conditions are met. So this point is supercentral.

Similarly for point (1,2). Let's see:

In x=1's y list: [0,1,2,3]. The current y is 2. So index is 2. So not first (y=0,1,2 → lower exists) and not last (y=3 exists). So upper and lower conditions are met. For y=2, the x's are 0,1,4 (from (0,2), (1,2), (4,2)). The current x is 1. So sorted x list is [0,1,4]. So x=1 is in the middle. So left (0) and right (4) exist. So all four conditions are met.

So how to implement this in code.

In Python, for each point, we need to check in the sorted lists. So for the y_dict and x_dict:

We can create a dictionary where for each y, the value is a sorted list of x's. Similarly for x, a sorted list of y's.

So:

Read all points, collect them into a list. Then build the two dictionaries:

y_dict = defaultdict(list)
x_dict = defaultdict(list)

for each point in points:
    x, y = point
    y_dict[y].append(x)
    x_dict[x].append(y)

Then, for each y in y_dict, sort the x list. Similarly for x_dict's y lists.

Once the dictionaries are built, for each point (x, y):

Check in y_dict[y], the sorted x list. Check if x is not the first element (left exists) and not the last (right exists). But how to check that?

Wait, but for a given point (x,y), when we process the y_dict for y, the x is in the list. So for the list y_x = sorted_x_list. We can find the index of x in y_x. But since the list is sorted, we can use bisect.bisect_left to find the index. Wait, but since the list is sorted, and contains x, the index can be found via binary search.

But in Python, using list.index(x) could work, but if there are multiple points with the same x and y (but the problem states all points are distinct, so same x and y can't exist). So each x in a y's list is unique. So for y_dict[y], each x in the list is unique. So for a given x, in the list for y, the index can be found via bisect.bisect_left or list.index.

But since the list is sorted, we can use bisect to find the insertion point. For example, if the list is [0,1,3], and x is 1, the bisect_left returns index 1. Then, the left exists (index >0) and right exists (index < len(list) -1? len(list) is 3, so index 1 < 2 (3-1=2). So yes, right exists.

So code steps:

For a point (x,y):

left_neighbor = exists if there is at least one x' < x in the same y group.

In the sorted list for y, if the x is not the first element (i.e., index in the list >0), then left exists.

Similarly, right exists if the x is not the last element (index < len(list) -1).

Same for upper and lower:

In x_dict[x], the sorted list of y's. Current y must not be first (lower exists) and not last (upper exists).

So, for each point (x,y):

Check:

left = (index_in_y_x_list > 0)

right = (index_in_y_x_list < len(y_x_list) - 1)

lower = (index_in_x_y_list > 0)

upper = (index_in_x_y_list < len(x_y_list) -1)

If all four are true, count the point.

So the code steps:

Initialize count to 0.

For each point (x, y):

1. Get the sorted x list for y from y_dict. If y is not in y_dict, then no (but since the point is in the list, it must be in the dict).

2. Find the index of x in this list. Since the list is sorted and contains x, use bisect.bisect_left.

3. Check if left exists: index >0.

4. Check if right exists: index < len(list) -1.

5. Get the sorted y list for x from x_dict. Again, x must be present.

6. Find the index of y in this list.

7. Check if lower exists: index >0.

8. Check if upper exists: index < len(list) -1.

If all four conditions are met, increment count.

Now, for the bisect part. Since the lists are sorted, bisect.bisect_left is O(log n) time. But for n up to 200, even O(n) is acceptable. So in code, perhaps for each list, we can pre-sort them once, then for each point, use bisect to find the index.

So code steps:

After building the dictionaries, for each key in y_dict, sort the list. Same for x_dict.

Then, for each point in the input, process as above.

Now, implement this in Python.

But how to handle the case where the point is the only one in its y or x group. For example, a point (0,0) with no other points in y=0. Then, in the x_dict for x=0, the y list would have only 0. So in that case, the index is 0. So lower (index>0) is false. Upper (index <0) is also false. So such a point will not be counted.

But in the second sample input:

5 points:

(0,0), (0,1), (1,0), (0,-1), (-1,0)

Looking at (0,0):

In the y=0 group (x_dict?), no. Wait, for y=0, the x's would be 0 (from (0,0)), 1 (from (1,0)), -1 (from (-1,0)). Wait no: wait, the x_dict maps x to list of y's. So for x=0, the y's are 0,1,-1. Sorted, so [-1,0,1].

Wait, (0,0) is in x=0. So the x_dict for x=0 has the list of y's: 0 (from (0,0)), 1 (from (0,1)), -1 (from (0,-1)). So sorted list is [-1,0,1]. So for the point (0,0), its y is 0, which is in the list. The index is 1. So lower exists (since index>0 → -1 is lower) and upper exists (index < 2 → yes, since 1 is the length of the list minus 1 is 2. 1 < 2 → yes). So upper and lower conditions are met.

Then, check the y group. For the point (0,0), y is 0. So in the y_dict, for y=0, the x's are 0 (from (0,0)), 1 (from (1,0)), -1 (from (-1,0)). Sorted x list is [-1, 0, 1]. So index of 0 is 1. Left exists (index>0) → yes (x=-1). Right exists (index <2) → yes (x=1). So all four conditions are met. So (0,0) is counted. Which matches the sample output.

So the code seems to handle that correctly.

Now, let's think about the time complexity. For each of the n points (up to 200), we perform two binary searches (each O(log k), where k is the number of points in the group, up to 200). So total time is O(n log k), which is acceptable for n=200.

So the code should work.

Now, the code steps:

Read n.

Read n points as a list. Also, build the two dictionaries.

Sort the lists in the dictionaries.

For each point, check the four conditions.

Now, code in Python:

We can use the bisect module for finding the indices.

But note that in Python, list.index() would also work, but for sorted lists, bisect is more efficient, especially if the list is large. But since the maximum length is 200, bisect is overkill, but using it is correct.

But let's proceed.

Sample code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    points = []
    y_dict = dict()
    x_dict = dict()

    for _ in range(n):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        points.append( (x, y) )
        if y not in y_dict:
            y_dict[y] = []
        y_dict[y].append(x)
        if x not in x_dict:
            x_dict[x] = []
        x_dict[x].append(y)

    # sort the lists in the dictionaries
    for y in y_dict:
        y_dict[y].sort()
    for x in x_dict:
        x_dict[x].sort()

    count = 0

    for x, y in points:
        # check left and right
        y_x = y_dict[y]
        idx = bisect.bisect_left(y_x, x)
        if idx == 0:
            has_left = False
        else:
            has_left = True
        if idx == len(y_x) - 1:
            has_right = False
        else:
            has_right = True

        # check upper and lower
        x_y = x_dict[x]
        idy = bisect.bisect_left(x_y, y)
        if idy == 0:
            has_lower = False
        else:
            has_lower = True
        if idy == len(x_y) -1:
            has_upper = False
        else:
            has_upper = True

        if has_left and has_right and has_lower and has_upper:
            count +=1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
0 0
0 1
1 0
0 -1
-1 0
""",
            "output": \
"""\
1
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

Sample 2:

5 points.

For (0,0):

y_dict for y=0: x's are -1,0,1. So [ -1, 0, 1 ] (from points (-1,0), (0,0), (1,0)).

x_dict for x=0: y's are -1,0,1 (sorted). So (0,0) is in index 1.

In the x group (x=0), y=0's index is 1. So lower exists (y=-1), upper exists (y=1). 

In the y group (y=0), x=0 is in index 1. Left (x=-1), right (x=1) exist.

So all four conditions met. So count is 1.

The code should output 1 for sample 2.

Thus, the code should handle all cases correctly.

Now, check for edge cases. Like n=1. Then, the point can't have any neighbors, so count is 0.

Another case: a point that has exactly one left, right, upper, lower. For example:

4 points arranged in a cross. Like (0,0), (1,0), (-1,0), (0,1), (0,-1). Then (0,0) is supercentral.

So code should count 1.

So code seems correct.
</think>

```python
import bisect

n = int(input())
points = []
y_dict = {}
x_dict = {}

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    if y not in y_dict:
        y_dict[y] = []
    y_dict[y].append(x)
    if x not in x_dict:
        x_dict[x] = []
    x_dict[x].append(y)

for y in y_dict:
    y_dict[y].sort()
for x in x_dict:
    x_dict[x].sort()

count = 0

for x, y in points:
    # Check left and right neighbors
    x_list = y_dict[y]
    idx_x = bisect.bisect_left(x_list, x)
    has_left = idx_x > 0
    has_right = idx_x < len(x_list) - 1
    
    # Check upper and lower neighbors
    y_list = x_dict[x]
    idx_y = bisect.bisect_left(y_list, y)
    has_lower = idx_y > 0
    has_upper = idx_y < len(y_list) - 1
    
    if has_left and has_right and has_lower and has_upper:
        count += 1

print(count)
```
