<think>
Okay, I need to solve this problem where I have to determine if all given points can be covered by at most two straight lines. Let me think about the approach.

First, the problem says that all points must lie on at least one of the two lines. So, if there are 0, 1, or 2 points, the answer is definitely YES. Because with two lines, you can cover any two points (each line can be a single point, but since lines are straight, two points are on the same line). Wait, but the lines are straight lines. So for n<=2, it's always possible. But the constraints say that n starts from 1. So for n=1, any two lines would cover it. For n=2, a single line covers both points, so two lines is trivial.

The real problem starts when n is 3 or more. So the first step is to handle the cases where n is small. But how to handle larger n?

The main idea is that if the answer is YES, then the first few points (like the first three) must form lines that can be part of the two required lines. Because if the first three points are all on one line, then maybe all others must be on that line or another. Or, if the first three form two lines, then the other points must be on those lines.

Wait, but there could be two lines that don't include all of the first three. For example, maybe the first three points are split between the two lines in a way that requires the lines to be determined by other points.

Hmm. So maybe the correct approach is to try all possible candidate lines from the first few points. For example, if the first three points form three possible lines (each pair forms a line), then check if any of those lines can be one of the two lines needed, and then check if the remaining points can be covered by another line.

Alternatively, here's a common approach for problems where the answer depends on some initial points: pick the first few points (like the first 3) and generate possible candidate lines. Then, for each candidate line, check which points are not on it, and see if those remaining points form a single line.

Because, if the answer is YES, then one of the two lines must be formed by some combination of the first three points. For example, if all points are on two lines, then at least two of the first three points must be on one of those lines. But if the first three are split across the two lines (like two on line A, one on line B), then the candidate lines would be line A (the two points) and line B (the third plus another point not on line A).

But how to handle all possibilities?

So here's a plan:

If n <= 2, return YES.

Otherwise:

Check all possible pairs of lines derived from the first three points. For each possible candidate line (like the line through the first and second point), collect all points not on this line. Then check if those remaining points lie on a single line. If any of these checks pass, return YES.

If none of the candidate lines from the first three points work, then return NO.

Wait, but what about cases where the two lines are not among the first three points' pairs? For example, maybe the first three points are all on one line, but the other line is formed by points later in the list. But in that case, the initial approach would still work because when we check the line formed by the first two points, and collect the remaining points, if all those remaining form a single line (including the third point), then it would be detected.

But let's think of an example. Suppose all points except one are on line A (which includes the first two points). Then the remaining points (after line A) are checked to form a line. If there's only one such point, then yes. So the approach would work.

Another example: suppose there are two lines, line A and line B. The first three points are two on line A and one on line B. Then when we check line A (the first two points), the remaining points (including the third) would need to be on line B, which is the case. So the check would pass.

But what if the first three points are all on line B, but the other line is line A, which includes points not in the first three? Then checking the first line (line B) would collect all points not on line B. Those would be on line A, which is the other line. So this would also be detected.

Therefore, the approach of considering all possible candidate lines from the first three points (including all possible pairs) and checking if the remaining points form a line is sufficient.

So, the steps are:

1. If n <= 2, return YES.

2. Otherwise, collect the first three points as a, b, c.

3. Generate all possible candidate lines from these three. For example:

   a. The line through a and b.

   b. The line through a and c.

   c. The line through b and c.

4. For each candidate line, collect all points not on this line. Then check if those remaining points lie on a single line. If for any candidate line, this is true, return YES.

5. If none of the candidate lines work, return NO.

But why the first three points? Because if the answer is YES, then among the first three points, at least two must lie on one of the two lines. So, one of the candidate lines (from the three pairs) would be that line. Then the remaining points (including the third point) must lie on the other line.

Wait, but the two lines could have any of the first three points. For example, maybe two lines have two of the first three points each. Like a and b are on line1, c is on line2. Then when we check line1 (a and b), the remaining points (including c) must all be on line2. So the check would work. Similarly, if line1 is a and c, and line2 is b and the others, then checking line1 would collect all points not on line1, which would include b and maybe others. But if those others form a line, then yes.

Alternatively, if all three points are on one line (say line1), then the other line could be any line covering the remaining points, which are not on line1. So when we check line1 (using a and b), collect the remaining points (which include c) and check if they are all on another line. Since in this case, the remaining points (if any) must be on the other line, the check would pass.

So, considering all possible candidate lines from the first three points (three possible lines) is sufficient.

But wait, the first three points could be split in such a way that two are on line1 and one on line2. Then when checking the line formed by the first two (line1), the remaining points (including the third, which is on line2) would need to form a line. So if all other points are either on line1 or line2, then the check would pass.

Therefore, this approach covers all possible cases.

So the plan is:

For each candidate line (three possibilities from the first three points):

   collect all points not on this line.

   check if those points form a single line.

If any of the three candidate lines passes this check, return YES.

Else, return NO.

Additionally, there's a possible case where the first three points are all on one line. Then, the candidate line is that line. The remaining points could either all be on that line (then the other line can be anything), but in this case, since the remaining points would be zero, which is covered by the check (all zero points form a line trivially). So for example, if all points are on line1 (the candidate line), then the remaining points are zero, and so the check passes, leading to YES.

Wait, but if all points are on line1, then the remaining points after checking line1 is empty. Then the code would see that the remaining points (empty) can form a line (since zero or one points are considered to form a line). So that would return yes.

Yes. So the code needs to handle the case where all points are on a single line.

But let's think about the code steps:

For each candidate line (from the first three points):

   collect all points not on this line.

   if the size of this collection is zero: return yes.

   else, check if all the points in the collection are colinear.

So in the case where all points are on line1 (the candidate line), the collection is empty, so the check passes.

Thus, the code would return yes.

So that's covered.

Now, how to implement the check if a point is on a line?

A line can be represented in the general form: ax + by + c = 0. But handling the coefficients as integers could be tricky due to division and floating points. So perhaps it's better to represent the line in a way that avoids floating points.

Alternatively, for two points (x1, y1) and (x2, y2), a third point (x, y) is on the same line if the area of the triangle they form is zero. The area can be computed using the determinant:

(x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) == 0.

This is the cross product approach and avoids division. So for a line defined by two points (a and b), any point c is on the line if (b.x - a.x) * (c.y - a.y) == (b.y - a.y) * (c.x - a.x).

This is a good way to check because it uses integers and avoids floating point inaccuracies.

So for a given candidate line (defined by two points), we can check all other points against this line.

Now, the steps for each candidate line:

- Take the two points that define the line (like a and b).

- Collect all points that are not on this line (using the cross product check).

- If there are zero points left, return True.

- If there are one or two points left, they can form a line, so return True.

- Else, take the first two points in the remaining list and check if all remaining points are colinear with them.

If so, return True for this candidate line.

So, in code:

For a candidate line (p1, p2):

   remaining = [p for p in all_points if not colinear(p1, p2, p)]

   if len(remaining) <= 1:

       return True

   else:

       Check if all remaining points are colinear with remaining[0] and remaining[1].

       If yes, return True.

So for each candidate line, we do this check.

If any of the three candidate lines passes this check, then the answer is YES.

Otherwise, NO.

But how do we choose the candidate lines? The candidate lines are the three possible lines formed by pairs of the first three points. So for the first three points a, b, c, the lines are (a, b), (a, c), (b, c).

But wait, in the case where the first three points are colinear (all on the same line), then all three lines (a, b), (a, c), (b, c) are the same line. So checking any of them would suffice.

But to cover all possibilities, even if they are colinear, we check all three lines. But since the lines are the same, the code would check the same line three times, which is redundant, but for the sake of code simplicity, it's acceptable.

Now, for the code structure:

We can process the first three points. For each of the three pairs (a,b), (a,c), (b,c), check if the remaining points (after excluding those on the line) form a single line.

If any of the three checks returns true, then output YES. Else, NO.

But let's think about some edge cases.

Edge case 1: All points are on a single line.

In this case, any candidate line (like a and b) would have remaining points as all other points except those on line a-b. Wait, no. If all points are on the line a-b, then all points are on that line. So the remaining points would be empty. Thus, the check would return True.

Edge case 2: The two lines are the same. For example, all points are on a single line. Then the code would pass because remaining points are empty.

Edge case 3: There are two lines, and the first three points are all on one of them. For example, the first three points are on line1, and others are on line2. Then, checking line1 (a and b) would collect the remaining points (those not on line1, which are line2 points). Then check if those are colinear. Since they are on line2, the check would pass.

Another example: the first three points are a, b, c. a and b are on line1. c is on line2. The rest are on line2. Then, when checking line1 (a and b), the remaining points include c and others. Check if they are colinear. Since they are on line2, yes. So the code returns YES.

Now, the code needs to:

- Read all the points.

- Handle the trivial cases (n <= 2).

- Take the first three points (if n >=3), and generate the three candidate lines.

- For each candidate line, collect the remaining points.

- Check if remaining points can form a single line.

So, for the code:

Read n.

If n <= 2: print YES.

Else:

Read all points into a list.

Take the first three points (a, b, c).

Generate three candidate lines: (a, b), (a, c), (b, c).

For each candidate line (p1, p2):

   collect all points not on the line (using cross product).

   if len(remaining) <=1:

       return YES.

   else:

       take the first two points of remaining, check if all others are colinear with them.

       if yes, return YES.

If none of the three checks pass, return NO.

But wait, in the case where the remaining points are more than two, but all are colinear. For example, if remaining is a list of three points that are colinear. Then, the check would pass.

Now, implement this.

But how to handle the remaining points?

For example, in the code, when you collect the remaining points (those not on the candidate line), you need to check if all of them are colinear. The way to check is to pick the first two points in the remaining list (if there are at least two), then check if all other points are on the line formed by these two.

But if there are zero points remaining, the check passes. If there is one, it's also okay. If two, then yes. If more than two, check if all are on the line formed by the first two.

But the code for the check is:

def are_colinear(points):
    if len(points) <= 1:
        return True
    # pick first two points
    p0 = points[0]
    p1 = points[1]
    for p in points[2:]:
        if (p1[0] - p0[0]) * (p[1] - p0[1]) != (p1[1] - p0[1]) * (p[0] - p0[0]):
            return False
    return True

So, in code:

So, for each candidate line (p1, p2):

remaining = [p for p in all_points if (p2[0] - p1[0])*(p[1] - p1[1]) != (p2[1] - p1[1])*(p[0] - p1[0])]

if len(remaining) == 0: return YES.

elif len(remaining) == 1: return YES.

else:

   check if all in remaining are colinear.

But how about if the remaining points are all on a line, but that line is different from the candidate line. That's exactly the case we need to check.

So, the code for the candidate line (p1, p2) would check the remaining points (which are not on p1-p2 line) to see if they form a single line.

Thus, the code is correct.

Now, considering the constraints. For n up to 1e5, and each candidate line check requires O(n) time. There are three candidate lines to check. So the total time is O(n *3) = O(3e5) operations, which is acceptable for a 2-second time limit.

But in Python, for 1e5 elements, list comprehensions can be slow if not optimized. So perhaps precomputing the points and then processing them efficiently is needed.

Another optimization: since the candidate lines are derived from the first three points, but after that, for the remaining points, we can process them all in a loop.

So the code steps:

Read all the points.

If n <=2: YES.

Else:

Check the three candidate lines.

Each candidate line is (a, b) from the first three points.

For each candidate line (p1, p2):

   remaining = list of points not on the line.

   if len(remaining) <=1:

       return YES.

   else:

       take the first two points in remaining: x, y.

       check if all other points in remaining are on the line formed by x and y.

       if yes: return YES.

If none of the three passes, return NO.

Now, code.

But in Python, for 1e5 points, list comprehensions can be slow. So perhaps we can process this in a way that avoids building a new list each time. For example, for each candidate line, iterate through all points and collect the count of those not on the line, and check the first two points not on the line.

Wait, but for the check, we need to collect all the points not on the candidate line. Because once we have that list, we need to check if all of them are colinear.

But building a list of all points not on the line can take O(n) time and space. For n=1e5, this is manageable, but perhaps we can optimize.

Alternatively, during the first pass through the points for the candidate line (p1, p2), we can:

- Find the first two points not on the line. Then, for each subsequent point, check if it's colinear with those two.

If any of the points is not, then this candidate line is invalid.

But how?

For the candidate line (p1, p2):

   first_remaining = None

   second_remaining = None

   for p in all_points:

       if p is not on (p1, p2):

           if first_remaining is None:

               first_remaining = p

           elif second_remaining is None:

               second_remaining = p

               # Now, compute the line between first_remaining and second_remaining.

               dx = second_remaining[0] - first_remaining[0]

               dy = second_remaining[1] - first_remaining[1]

           else:

               # Check if p is on the line between first_remaining and second_remaining.

               # (second_remaining.x - first_remaining.x) * (p.y - first_remaining.y) == (second_remaining.y - first_remaining.y) * (p.x - first_remaining.x)

               if dx * (p[1] - first_remaining[1]) != dy * (p[0] - first_remaining[0]):

                   # Invalid, break

                   break

   else:

       # All points not on candidate line are colinear.

       return YES

So, this approach avoids building the entire remaining list and instead checks each point as it's processed, which can be more memory efficient and possibly faster.

Because for each candidate line (p1, p2), we can process each point once, and track the first two points not on the line, then check the rest against the line formed by those two.

This approach reduces memory usage because we don't build a list, and for large n, this could be more efficient.

So the code for each candidate line would be:

def check_candidate(p1, p2, points):

    # Compute the line parameters (p1-p2 line)

    # For each point, check if it's on the line.

    # Track the first two points not on the line.

    first = None

    second = None

    dx_line = p2[0] - p1[0]

    dy_line = p2[1] - p1[1]

    for p in points:

        # Check if p is on the line p1-p2.

        # cross product: (p2.x - p1.x) * (p.y - p1.y) == (p2.y - p1.y) * (p.x - p1.x)

        if dx_line * (p[1] - p1[1]) == dy_line * (p[0] - p1[0]):

            continue  # point is on the candidate line.

        # Point is not on the candidate line.

        if first is None:

            first = p

        elif second is None:

            second = p

            # Compute dx and dy for the new line (first and second)

            dx_remaining = second[0] - first[0]

            dy_remaining = second[1] - first[1]

        else:

            # Check if p is on the line first-second.

            # (second.x - first.x) * (p.y - first.y) == (second.y - first.y) * (p.x - first.x)

            if dx_remaining * (p[1] - first[1]) != dy_remaining * (p[0] - first[0]):

                # Not colinear, invalid.

                return False

    # If all points are processed and passed.

    return True

But in this code, how do we handle the cases where there are zero, one, or two points not on the candidate line?

If first is None: all points are on candidate line. So return True.

If first is not None and second is None: only one point not on candidate line. return True.

Else, all points not on candidate line are on the line formed by first and second. So return True.

But in the code above, if first and second are set, then for the remaining points (not on the candidate line), each is checked against the line formed by first and second.

So if any of them fails, return False.

Thus, the check_candidate function returns True if all points not on the candidate line are colinear (possibly zero, one, two, or more).

Thus, for each candidate line, if check_candidate returns True, then the answer is YES.

So the code can be structured as:

Read all points.

if n <=2: output YES.

else:

   a, b, c = points[0], points[1], points[2]

   if any of the three candidate lines (a and b, a and c, b and c) passes check_candidate, output YES.

   else output NO.

So the code would look like:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    if n <= 2:

        print("YES", file=output_stream)

        return

    points = [tuple(map(int, input_stream.readline().split())) for _ in range(n)]

    a, b, c = points[0], points[1], points[2]

    # Check the three candidate lines.

    def is_valid(p1, p2):

        # Check if all points are either on p1-p2 line or on another line.

        dx_line = p2[0] - p1[0]

        dy_line = p2[1] - p1[1]

        first = None

        second = None

        dx_remaining = 0

        dy_remaining = 0

        for p in points:

            if dx_line * (p[1] - p1[1]) == dy_line * (p[0] - p1[0]):

                continue

            # Not on candidate line.

            if first is None:

                first = p

            elif second is None:

                second = p

                dx_remaining = second[0] - first[0]

                dy_remaining = second[1] - first[1]

            else:

                # Check if p is on first-second line.

                if dx_remaining * (p[1] - first[1]) != dy_remaining * (p[0] - first[0]):

                    return False

        return True

    # Check the three candidates.

    if is_valid(a, b) or is_valid(a, c) or is_valid(b, c):

        print("YES", file=output_stream)

    else:

        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
0 0
1 0
2 1
1 1
2 3
""",
            "output": \
"""\
NO
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

Second example:

5

0 0

1 0

2 1

1 1

2 3

First three points are (0,0), (1,0), (2,1).

Check candidate lines:

a-b (0,0) and (1,0): line y=0.

Check remaining points: (2,1), (1,1), (2,3).

For these three, the code would check if they form a line. The first two are (2,1) and (1,1). The line is y=1. The third point (2,3) is not on this line. So returns false.

Next candidate line a-c (0,0) and (2,1). The line equation is 1x - 2y = 0. The remaining points are (1,0), (1,1), (2,3). Check if they form a line. (1,0) and (1,1) are vertical x=1. (2,3) is not on x=1. So returns false.

Third candidate line is b-c (1,0) and (2,1). The line is y = x-1. The remaining points are (0,0), (1,1), (2,3). Check if they form a line. (0,0) and (1,1) are on y=x. (2,3) is not. So returns false.

Thus, all three candidates fail. Output is NO.

Which matches the example.

Thus, the code works for the examples.

Now, to handle large inputs, the code must be efficient.

But for each candidate line, it's O(n) time. Three candidates: O(3n) time. For 1e5, 3e5 operations, which is acceptable.

But in Python, even 1e6 operations are acceptable under 1 second, so 3e5 is manageable.

Memory-wise, the code only stores the points once. So for 1e5 points, it's manageable.

Potential optimizations:

- Precompute the cross products for all points once for each candidate line. But the code already processes each point once per candidate line.

But in the code above, for each candidate line, each point is checked against that line once. So for three candidates, each point is checked three times.

Thus, 3n checks. Each check is a few arithmetic operations. Which should be manageable.

Thus, the code should pass all test cases within time and memory constraints.

Another thing to note: the code reads all points first. For n=1e5, in Python, reading via sys.stdin may be faster with sys.stdin.read(). Split once.

So, perhaps optimize the input reading.

Instead of:

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

It's better to read all input at once.

For example:

import sys

def main():

    import sys

    data = sys.stdin.read().split()

    n = int(data[0])

    if n <=2:

        print("YES")

        return

    points = list(zip(map(int, data[1::2]), map(int, data[2::2])))

    a, b, c = points[0], points[1], points[2]

    ...

This could be faster, especially for large n.

Because reading via readlines or line by line can be slow in Python for 1e5 lines.

So modifying the code to read all input at once.

Thus, the code becomes:

import sys

def main():

    data = sys.stdin.read().split()

    ptr = 0

    n = int(data[ptr])

    ptr +=1

    if n <=2:

        print("YES")

        return

    points = []

    for _ in range(n):

        x = int(data[ptr])

        y = int(data[ptr+1])

        points.append( (x, y) )

        ptr +=2

    a, b, c = points[0], points[1], points[2]

    def is_valid(p1, p2):

        dx_line = p2[0] - p1[0]

        dy_line = p2[1] - p1[1]

        first = None

        second = None

        dx_rem = 0

        dy_rem = 0

        for p in points:

            if dx_line * (p[1] - p1[1]) == dy_line * (p[0] - p1[0]):

                continue

            if first is None:

                first = p

            elif second is None:

                second = p

                dx_rem = second[0] - first[0]

                dy_rem = second[1] - first[1]

            else:

                if dx_rem * (p[1] - first[1]) != dy_rem * (p[0] - first[0]):

                    return False

        return True

    if is_valid(a, b) or is_valid(a, c) or is_valid(b, c):

        print("YES")

    else:

        print("NO")

This should read the input efficiently.

Now, test the code with the examples.

Another possible optimization: check if the three candidate lines are the same. For example, if the first three points are colinear, then all three candidate lines are the same. So checking one is sufficient. But the code checks all three, which is redundant. However, for the sake of code simplicity and given that n is 1e5, the three checks are manageable.

Thus, this code should be correct and efficient.
</think>

```python
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    if n <= 2:
        print("YES")
        return
    
    points = []
    for _ in range(n):
        x = int(data[ptr])
        y = int(data[ptr + 1])
        points.append((x, y))
        ptr += 2
    
    a, b, c = points[0], points[1], points[2]
    
    def is_valid(p1, p2):
        dx_line = p2[0] - p1[0]
        dy_line = p2[1] - p1[1]
        first = None
        second = None
        dx_rem, dy_rem = 0, 0
        
        for p in points:
            if dx_line * (p[1] - p1[1]) == dy_line * (p[0] - p1[0]):
                continue
            if first is None:
                first = p
            elif second is None:
                second = p
                dx_rem = second[0] - first[0]
                dy_rem = second[1] - first[1]
            else:
                if dx_rem * (p[1] - first[1]) != dy_rem * (p[0] - first[0]):
                    return False
        return True
    
    if is_valid(a, b) or is_valid(a, c) or is_valid(b, c):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
```
