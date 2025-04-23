<think>
Okay, let's see. The problem is about two friends on a coordinate axis. They want to meet at some integer point, and we need to find the minimal total tiredness they can achieve. The tiredness is calculated by adding up 1 for the first move, 2 for the second, and so on. Each movement (each step) contributes to this sum. So, for example, moving left then right then left again adds 1+2+3=6.

Hmm. The key here is to find the optimal meeting point where the sum of both friends' tiredness is minimized. Let's think about how to approach this.

First, the initial positions are a and b, and a is not equal to b. Let's compute the distance between them. The minimal total moves would probably involve them moving towards each other, but maybe sometimes one moves more than the other, depending on the distance.

Wait, but the meeting point can be anywhere, not necessarily in the middle. For example, maybe one moves a lot and the other moves a little. But how do we model the tiredness for each possible meeting point?

So the plan is: iterate over all possible meeting points between a and b, compute the total tiredness for each, and find the minimum.

But what's the range of possible meeting points? Well, since the friends can move any number of steps (including zero), the meeting point can be anywhere. But considering that moving away from each other would increase the total distance they have to cover, the optimal point is likely somewhere between a and b. So perhaps we should only consider points between min(a, b) and max(a, b). Wait, but maybe moving beyond that could lead to a lower sum? Let's see.

For example, if a is 3 and b is 4. The possible meeting points are 3 (friend 2 moves left once), 4 (friend 1 moves right once), or maybe some other points. But in that case, the minimal sum is 1. If they meet at 5, friend 1 has to move two steps (sum 1+2=3), friend 2 moves one step (sum 1+2=3?), wait no. Wait, friend 2's position is 4, meeting at 5 would require him to move right once. So his tiredness is 1. So total is 3 (friend1: 2 steps, sum 1+2=3) plus 1 (friend2: 1 step) = 4, which is worse than the optimal 1. So the optimal point is between the two initial positions.

So probably, the optimal meeting point is somewhere between a and b. But not necessarily exactly in the middle.

So the first step is to find all possible meeting points, which could be anywhere on the integer line, but in practice, the optimal is between a and b, perhaps even just in the interval [min(a,b), max(a,b)].

So let's compute the positions from left to right. Let's call the meeting point x. Then, the distance each friend has to move is |x - a| for the first friend, and |x - b| for the second. Wait, but each step is a move. So for a friend to cover a distance of d steps, they have to make d moves. For example, moving 3 steps to the right requires 3 moves. So the number of moves is exactly the distance, since each move is one step.

So for each x, compute the sum of the tiredness of moving d1 steps and d2 steps, where d1 = |x - a|, d2 = |x - b|.

The problem reduces to finding x that minimizes the sum of the tiredness for d1 and d2 steps.

So now, how do we compute the tiredness for a given number of steps (d)?

The tiredness for moving d steps is the sum of the first d natural numbers: sum(1..d) = d*(d+1)/2. Because each move contributes an incrementing value. First step adds 1, second 2, etc.

Wait, yes. For example, if you move 3 steps, the sum is 1 + 2 + 3 = 6, which is 3*4/2 = 6.

So for each x, the total tiredness is (d1*(d1 +1)/2) + (d2*(d2 +1)/2), where d1 is |x -a| and d2 is |x -b|.

We need to find x that minimizes this sum.

But how do we efficiently find x? The possible x's could be from 0 to some large number, but given the constraints of a and b (they are up to 1000), maybe trying all possible x in a reasonable range is feasible.

But wait, in the problem statement, a and b are up to 1000, but what about x? For example, if a is 1 and b is 1000, then the possible x's could be anywhere between 1 and 1000, but perhaps even beyond. But in that case, moving further away would increase the distance for both friends, leading to higher tiredness.

So maybe the optimal x is somewhere in the range [min(a,b), max(a,b)]. Let's see.

Wait, let's think of x being to the left of min(a,b). For example, a=5 and b=10. If x is 3, then d1=2, d2=7. Sum is 2*3/2 +7*8/2 = 3 + 28 = 31. If x is 5, d1=0, d2=5. Sum is 0 + 15 = 15. So better. So moving x to the left of min(a,b) may not be optimal. Similarly, moving to the right of max(a,b) may not be optimal.

Therefore, the optimal x is in the interval [min(a,b), max(a,b)]. So we can iterate x from min(a,b) to max(a,b), compute the sum for each x, and find the minimum.

Since the maximum possible distance between a and b is 999 (if a=1 and b=1000), then the range of x is 1000 elements. So trying all possibilities is acceptable, even for the largest input. So for each x in that range, compute d1 and d2, then the sum of their triangular numbers.

Wait, but even if x is beyond min or max, maybe that's better. Let's take an example: a=3, b=4. The possible x could be 3, 4, or 2,5.

Wait, in the first example, the optimal is x=3 or 4. Let's see x=2: d1=1, d2=2. Sum is 1 + 3 (1+2) = 4, which is worse than 1. So moving beyond the initial positions is worse.

Another example: a=5, b=10. The sample input gives output 9. The optimal is x=8. Let's see: friend1 moves 3 steps (sum 6), friend2 moves 2 steps (sum 3). Total 9. So x is between a and b.

So yes, the optimal x is between a and b, inclusive.

So the approach is:

1. Compute the minimum and maximum of a and b. Let's say left = min(a, b), right = max(a, b).

2. For each x in [left, right], compute d1 = |x - a|, d2 = |x - b|. Then compute sum = (d1*(d1+1) + d2*(d2+1))/2.

3. Find the minimum sum among all x in this range.

But wait, let's check the sample input 2.

Sample input 2: a=101, b=99. So left=99, right=101. So possible x's are 99,100,101.

x=99: friend1 moves 2 steps (sum 3), friend2 0 steps. Total 3.

x=100: friend1 moves 1 step (sum 1), friend2 moves 1 step (sum 1). Total 2.

x=101: friend1 moves 0, friend2 moves 2 (sum 3). Total 3. So the minimum is 2. Which matches the sample.

So yes, iterating x from left to right is sufficient.

But wait, in the third sample, a=5, b=10. The meeting point is 8. So x runs from 5 to 10. For x=8: d1=3, sum 6; d2=2, sum 3. Total 9. For other x's:

x=7: d1=2, sum 3; d2=3, sum 6. Total 9.

x=6: d1=1, sum 1; d2=4, sum 10. Total 11.

x=5: sum 0 + 5 steps (15) total 15.

x=8 and x=7 give the same sum of 9. So in the sample, the correct output is 9.

So the code would find the minimal sum among all x in the range.

Thus, the approach is to iterate x from left to right, compute the sum for each, track the minimum.

Now, for a and b up to 1000, the maximum possible range is 1000-1 = 999 steps, but since a and b can be as close as 1 apart (like 1 and 2), the code will handle that.

So the steps for the code are:

1. Read a and b.

2. Compute left and right as min(a,b) and max(a,b).

3. Initialize min_total to a large number.

4. For x in left to right inclusive:

   a. d1 = x - a if a < x? Wait, no: d1 is |x - a|.

   So d1 = abs(x - a)

   d2 = abs(x - b)

   sum_t = (d1 * (d1 +1)) // 2 + (d2 * (d2 +1)) // 2

   compare to min_total, keep the minimum.

5. After checking all x, output the min_total.

Yes.

But what about x beyond left and right? Let's see. For example, sample input 1: a=3, b=4. The code checks x=3 and 4.

x=3: d1=0, sum 0. d2=1, sum 1. Total 1.

x=4: d1=1, sum 1. d2=0. Total 1.

But what if x=5? Then d1=2, sum 3. d2=1, sum 1. Total 4. Which is higher than 1.

So the code will correctly find the minimal sum.

Therefore, the approach of checking all x between left and right is sufficient.

Thus, the code can be written as:

Read a and b.

Compute left = min(a, b), right = max(a, b).

Initialize the minimum as a very large number.

Loop x from left to right:

   compute d1 and d2 as absolute differences.

   compute sum of their triangular numbers.

   if sum is less than current min, update min.

Finally, output the min.

Now, considering the constraints, a and b are up to 1000. So the maximum number of x's is 1000 (if a=1 and b=1000). So 1000 iterations, each involving simple calculations, which is trivial for Python even in the worst case.

So the code is efficient.

Testing sample input 3:

a=5, b=10.

Loop x from 5 to 10.

For x=8:

d1 = 3, sum 3*4/2 =6.

d2=2, sum 2*3/2=3. Total 9.

Which is the correct answer.

So the code will work.

Now, code implementation:

We can read a and b as integers.

Compute left and right.

Initialize min_total to a large number (like infinity).

Loop x in range(left, right+1):

   d1 = abs(x - a)

   d2 = abs(x - b)

   total = (d1*(d1+1))//2 + (d2*(d2+1))//2

   if total < min_total:

       min_total = total

After all iterations, print min_total.

Yes.

So the code is straightforward.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    a = int(input_stream.readline().rstrip("\n"))
    b = int(input_stream.readline().rstrip("\n"))
    left = min(a, b)
    right = max(a, b)
    min_total = float('inf')
    for x in range(left, right + 1):
        d1 = abs(x - a)
        d2 = abs(x - b)
        total = (d1 * (d1 + 1) // 2) + (d2 * (d2 + 1) // 2)
        if total < min_total:
            min_total = total
    print(min_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
10
""",
            "output": \
"""\
9
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

Sample 3:

a=5, b=10.

Loop x from 5 to 10.

At x=5:

d1=0, sum 0. d2=5, sum 15. Total 15.

x=6: d1=1 (sum 1), d2=4 (sum 10). Total 11.

x=7: d1=2 (sum 3), d2=3 (sum 6). Total 9.

x=8: sum 6 +3=9.

x=9: d1=4 (sum 10), d2=1 (sum1). Total 11.

x=10: sum 15 +0=15.

So the minimal is 9.

So code works.

Therefore, the code is correct.
</think>

```python
a = int(input())
b = int(input())
left = min(a, b)
right = max(a, b)
min_total = float('inf')
for x in range(left, right + 1):
    d1 = abs(x - a)
    d2 = abs(x - b)
    total = (d1 * (d1 + 1) // 2) + (d2 * (d2 + 1) // 2)
    if total < min_total:
        min_total = total
print(min_total)
```
