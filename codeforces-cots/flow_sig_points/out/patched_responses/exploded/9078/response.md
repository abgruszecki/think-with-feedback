<think>
Okay, let's see. The problem is about Xenia moving around the ringroad to complete tasks. The goal is to calculate the minimal time she needs to take, considering that each move between adjacent houses takes 1 unit of time. 

So, the initial position is house 1. For each task in order, she must go to the required house ai. But there's a catch: for the i-th task, all previous tasks (with lower indices) must be completed. So the order of the tasks matters. But since the tasks are processed in order, each subsequent task has to be done after the previous ones.

The key here is to model the movement between consecutive tasks and calculate the total time.

Let's think about the movement from one task to the next. Suppose the current position is at position prev, and the next task is at curr. Since the houses are arranged in a ring (circular), the distance between prev and curr depends on whether you move clockwise (since the traffic is one-way, that's the only direction allowed). 

So, for example, if prev is 3 and curr is 2 in a 4-house ring, moving clockwise would mean going from 3 →4 →1 →2, which is a distance of 3 steps. But wait, no, in a one-way circular movement, the direction is fixed. So the distance from prev to curr is (curr - prev) mod n if that's the clockwise way. Wait, no. Because the ring is circular and movement is clockwise, moving from x to x+1 is next, and so on. So when you're at prev, to get to curr, the number of steps is (curr - prev) if curr >= prev. Otherwise, it's (curr - prev + n) because you wrap around. For example, if prev is 4 and curr is 1 in a 4-house ring, the distance would be 1 -4 = -3, but since we can't move backward, we have to go 4 →1, which is 1 step. Wait, no. Wait, in the problem statement, the ring is one-way and clockwise. So each step moves you to the next higher number, but after n comes 1. So moving from 4 to 1 is a single step. So the number of steps between prev and curr is (curr - prev) if curr >= prev, otherwise (curr + n - prev). So the formula can be written as (curr - prev) % n if that's positive. Wait, let's see: (curr - prev) mod n. Let's take examples:

prev=3, curr=2. (2-3) mod 4 is -1 mod4 = 3. Which is correct: 3 →4 (1 step), 4→1 (another), 1→2 (another). So 3 steps. So yes, (curr - prev + n) %n gives the correct distance. Because when curr < prev, (curr - prev) is negative. Adding n and mod n gives the correct positive distance. So the formula for the distance between prev and curr is (curr - prev) %n if the result is non-negative, but that's the same as (curr - prev) when curr >= prev. Wait, but mod n gives the same as (curr - prev +n) %n. Let's see: for curr >= prev, (curr - prev) is positive, so (curr - prev) mod n is correct. For curr < prev, (curr - prev) is negative. For example, prev=4, curr=1: (1-4) mod4 is -3 mod4 = 1. But the actual steps needed are 1. So mod n gives (curr - prev) %n. Wait, that would be (1-4) mod4 = (-3) mod4=1. Which is correct. So yes, the formula is (curr - prev) %n. Because 1-4 = -3, and -3 mod4 is 1 (since 4* (-1) is -4, -3 - (-4) is 1). So yes. So the distance between prev and curr in the clockwise direction is (curr - prev) modn. 

So the approach is to track the current position (starting at 1), and for each task in the list, compute the steps needed to move from the current position to the next task's position, accumulate this into the total time, and then update the current position to the next task's position. But wait, the problem statement says that for the i-th task, all previous tasks (with numbers less than i) have been completed. So the order of processing is sequential. So the steps are indeed cumulative as we process each task in order.

But then, what about tasks that are the same as the previous? For example, consecutive tasks at the same house. Then the distance would be zero, so no steps added. Which is correct.

So the algorithm would be:

Initialize current_pos = 1, total_time =0.

For each ai in the list of tasks:

   steps = (ai - current_pos) %n

   total_time += steps

   current_pos = ai

So for each ai, compute the steps from the current position to ai, add to total, update current.

But wait, what if n is 4, current_pos is 3, ai is 2. Then (2-3) mod4 is ( -1) mod4 = 3. So adding 3 steps. Which is correct.

Yes, this seems correct.

Now, the problem is to process m tasks, each in O(1) time, so the total time is O(m), which is acceptable for m up to 1e5. So this approach is optimal.

But wait, let's test this with the examples.

First example:

Input:

4 3

3 2 3

Initial current_pos=1.

First ai=3: steps (3-1) mod4= 2. total_time=2. current_pos=3.

Second ai=2: (2-3) mod4= ( -1) mod4=3. total_time=5. current_pos=2.

Third ai=3: (3-2) mod4=1. total_time=6. Which matches the sample output.

Yes.

Second example:

4 3

2 3 3

Initial current=1.

First ai=2: steps (2-1) mod4=1. total=1. current=2.

Second ai=3: (3-2) mod4=1. total=2. current=3.

Third ai=3: (3-3) mod4=0. total=2. Which matches the sample.

So this approach works.

So the code is straightforward. We can read the list of a_i, then iterate through each a_i, compute the steps as (a_i - current_pos) %n, add to total, update current_pos.

Now, in Python, how to handle this efficiently.

The steps would be:

Read n and m.

Read the list a.

Initialize current = 1, total =0.

For each num in a:

   steps = (num - current) %n

   total += steps

   current = num

Print total.

Yes. That's the code.

But wait, wait. What about the modulo operation when the difference is negative. For example, in the first sample when current is 3 and next is 2. 2-3 is -1, mod4 is 3. Which is correct.

So this code should handle all cases.

Now, let's check for the second sample.

Sample 2:

n=4, m=3, a=[2,3,3]

Processing:

current=1.

First 2: (2-1) mod4 =1. total=1. current=2.

Next 3: (3-2) mod4=1. total=2. current=3.

Next 3: 0 mod4=0. total remains 2. Which is correct.

Yes.

Another test case: n=2, m=2, a=[2,1].

Processing:

current=1.

First 2: (2-1) mod2=1. total=1. current=2.

Second 1: (1-2) mod2 = ( -1 ) mod2 =1. total=2.

So Xenia moves 2 steps. Which makes sense: 1→2 (1 step), then 2→1 (another step). So total 2. Correct.

Another case: n=5, m=1, a=[3]. Steps: 3-1=2, mod5=2. So total 2.

Yes.

So the code seems correct.

Now, considering the constraints. n and m can be up to 1e5, but the code is O(m) time and O(1) space (since we can process the list as we read it, not storing all the elements, but in Python, reading the list is O(m) space, but that's acceptable for 1e5 elements). However, the problem says that the input is m elements on the second line, so we have to read them all. So for m=1e5, the list is manageable.

In Python, when reading input with input().split(), it's efficient. So the code should handle the constraints.

So the code is:

Read n and m from input.

Read the list a as integers.

Initialize current_pos =1, total=0.

Loop through each ai in a:

   steps = (ai - current_pos) %n

   total += steps

   current_pos = ai

Print total.

Yes.

So the code is straightforward. Let's code it.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
current = 1
total = 0
for num in a:
    delta = num - current
    if delta < 0:
        delta += n
    total += delta
    current = num
print(total)
```

Wait, but earlier analysis showed that (num - current) %n is the same as the delta. So in code, why not compute delta as (num - current) %n? Because for negative values, mod n gives the correct positive value. So the code can be simplified as:

for num in a:
    total += (num - current) % n
    current = num

But in Python, the modulo operator handles negative numbers correctly. For example, (2-3) %4 = (-1) %4 = 3. So yes.

So the code could be written as:

n, m = map(int, input().split())
a = list(map(int, input().split()))
current = 1
total = 0
for num in a:
    total += (num - current) % n
    current = num
print(total)

Which is even more concise and efficient. Because (num - current) %n directly gives the steps, regardless of sign.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    current = 1
    total = 0
    for num in a:
        delta = num - current
        if delta < 0:
            delta += n
        total += delta
        current = num
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3
2 3 3
""",
            "output": \
"""\
2
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

Yes. So the code is correct.

The second example:

n=4, a=[2,3,3].

current=1.

First 2: (2-1) mod4=1. total=1. current=2.

Second 3: (3-2) mod4=1. total=2. current=3.

Third 3: (3-3) mod4=0. total remains 2. Correct.

So this code is correct.

Therefore, the code can be written as:

Read the input, compute (num - current) %n for each step, sum, and output.
