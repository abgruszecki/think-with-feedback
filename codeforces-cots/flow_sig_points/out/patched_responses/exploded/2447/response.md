<think>
Okay, let's see. The problem is about a grasshopper jumping on a strip of cells. We need to determine if it will eventually jump out (finite) or get stuck in an infinite loop.

Hmm. So each cell has a direction (left or right) and a jump length. The grasshopper starts at the first cell and follows the directions. If it jumps out of the strip, it stops. Otherwise, it continues.

The key is to find out if the grasshopper's path ever repeats a cell. Because if it does, that's a cycle and it will loop infinitely. Otherwise, if it keeps moving without repeating, but eventually exits, then it's finite.

But wait, with n up to 1e5, we can't track every step the grasshopper takes, because in the worst case, each step is O(1), but for 1e5 steps that's manageable. But if the steps are up to 1e9, like in the input, the steps could be so long that the grasshopper jumps out immediately. So we need a way to detect cycles efficiently.

Let me think. The grasshopper can be in a cell, and each step, it moves either left or right by di steps. But the position after the move must be within the strip (1-based?), otherwise it exits.

Wait, the cells are 1 × n. So the cells are numbered 1 to n. So the grasshopper starts at cell 1. Each step, from cell i, it moves direction based on s[i-1] (since the string is 0-based?), and the distance is d[i-1].

So, for example, if the grasshopper is at cell i, and the direction is '>', then he jumps to i + d[i-1]. If that's beyond n, then he exits. Similarly, if direction is '<', jumps to i - d[i-1]. If that's less than 1, exits.

But if the jump leads to another cell within 1..n, then he continues.

The problem is to determine if he will eventually exit or loop forever.

So the main challenge is detecting cycles. Because if he comes back to a cell he's already visited, then the same steps will repeat, leading to an infinite loop.

So the approach is to track visited cells. Once a cell is revisited, we can return "INFINITE". Otherwise, if he exits, return "FINITE".

But with n up to 1e5, how do we track visited cells efficiently? Because if each step is O(1), but in the worst case, he could visit each cell once and then exit, which is O(n) steps.

Wait, but the grasshopper's path is determined uniquely by his current cell. So each step, he's in cell i, and the next step is determined by the direction and di of cell i. So the path is a sequence of cells, each leading to the next. So if he ever returns to a cell he's visited before, then there's a cycle. So the problem reduces to detecting if there's a cycle in this path.

So the solution is to simulate the path, keeping track of visited cells. As soon as we hit a cell that's already been visited, return "INFINITE". Otherwise, if the grasshopper steps out, return "FINITE".

But the problem is that simulating each step could take O(n) time, which is acceptable for n up to 1e5, right? Because 1e5 steps in Python are manageable within 2 seconds. Wait, but each step is O(1) operations. Let's see. For each step, we check if the current cell is visited. If not, mark it as visited, then compute the next cell.

But for cases where the grasshopper jumps in a cycle of 2 cells, like in the second example, we can detect this quickly. So the maximum number of steps needed is n steps. Because after n+1 steps, by the pigeonhole principle, we must have revisited a cell. So the maximum steps to simulate is n. So this approach is O(n) time and space, which is acceptable for n up to 1e5.

Wait, but in Python, a list of 1e5 elements is manageable. Let's see. Each element is a boolean. A list of 1e5 booleans is 1e5 bytes (if stored as bits, but in Python, each is a separate object, so it's actually more). But even 1e5 elements take up about 800KB (since each list slot in CPython uses a reference, which is 8 bytes, so 1e5 * 8 bytes is 800KB). Which is under the 256MB memory limit.

So the plan is:

- Create a visited array of size n+1 (since cells are 1-based), initialized to False.

- Start at current cell 1.

- While current cell is between 1 and n:

   - If visited[current] is True: return "INFINITE"

   - Mark visited[current] as True.

   - Get direction and distance.

   - Compute next cell: current +/- distance.

   - If next cell is outside 1..n: return "FINITE"

   - Else: set current to next cell.

So this will process each cell once. Since each step either exits or moves to a new cell (until a cycle is found). So the loop runs at most n times. For n=1e5, that's 1e5 iterations. Each iteration is O(1) operations. So the time complexity is O(n), which should be acceptable.

Testing on the examples:

First example:

n=2, directions "><".

cells are 1 and 2.

d = [1,2]

Start at 1. direction is '>', so jump 1 to 2. Mark 1 as visited.

At 2. direction is '<', jump 2. 2-2=0, which is outside. So output FINITE.

Second example:

n=3, directions ">><".

d = [2,1,1].

Start at 1. direction '>', jump 2 to 3. Mark 1.

At 3, direction is '>', but wait, the string is ">><", which is index 0 is '>', 1 is '>', 2 is '<'. So cell 3's direction is '<', so d is 1.

So next cell is 3 - 1 = 2. Mark 3 as visited.

At 2, direction is '>', so jumps 1 to 3. Now, 3 is already visited. So INFINITE.

So the approach works.

What about a case where the grasshopper jumps in a cycle of longer length? Like cell 1 → 2 →3 →1. Then after three steps, we reach 1 again, which was already visited. So the code would detect it.

So the algorithm works.

Now, the code.

We need to read n, the string s (length n), and the list d (n integers).

In Python:

n = int(input())

s = input().strip()

d = list(map(int, input().split()))

Then, create a visited array of size n+1 (cells are 1-based). So indexes 0 is unused, 1 to n.

visited = [False] * (n+1)

current = 1

loop:

while True:

   if current is <1 or >n: break and output finite.

   if visited[current] is True: output infinite.

   mark as visited.

   direction = s[current-1]

   distance = d[current-1]

   next_cell = current + distance if direction is '>' else current - distance.

   current = next_cell.

So code:

But how to loop:

current = 1

while True:

   if current < 1 or current > n:

       print("FINITE")

       exit()

   if visited[current]:

       print("INFINITE")

       exit()

   visited[current] = True

   dir_char = s[current-1]

   step = d[current-1]

   if dir_char == '>':

       current += step

   else:

       current -= step

So this loop will process each step correctly.

Testing edge cases.

For n=1:

s is either '<' or '>', d[0] is 1. Let's see.

If s is '>', then from cell 1, direction is '>', step is 1. next cell is 2, which is outside. So output FINITE.

If s is '<', then step is 1. next cell is 0 → outside. So output FINITE.

Another case: n=1, s is '>', d is 1. Output FINITE.

Another case: n=1, s is '>', d is 0. Wait, no, d is at least 1. So no, the problem says di ≥1.

Another case where the grasshopper jumps in a cycle. Like n=4, directions such that 1→3→4→1.

But the code would detect when it comes back to 1 again.

So the code seems correct.

But what about the case where the grasshopper jumps to a new cell each time, but eventually exits. Like n=3, steps 1 →4 (exit). So the code checks current=1, not visited, mark it. Compute next cell as 1 + d[0], suppose direction is '>', d[0] is 3. next cell is 4, which is outside. So output FINITE.

Now, the code's time and space.

Time: O(n) steps. For n=1e5, that's manageable.

Space: O(n) for the visited array. For n=1e5, that's acceptable.

So this should pass all test cases.

Now, code:

Read n, s, d.

Initialize visited as a list of booleans.

Then process current steps.

But in Python, for n=1e5, creating a list of 1e5+1 elements is manageable. Let's see.

Yes.

Now, code:

Read n, s, d.

But the input for d is n integers. So:

n = int(input())

s = input().strip()

d = list(map(int, input().split()))

Then, the code:

visited = [False] * (n + 1)

current = 1

while True:

    if current < 1 or current > n:

        print("FINITE")

        exit()

    if visited[current]:

        print("INFINITE")

        exit()

    visited[current] = True

    dir_char = s[current-1]

    step = d[current-1]

    if dir_char == '>':

        current += step

    else:

        current -= step

Yes.

This code should handle all cases correctly.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()
    d = list(map(int, input_stream.readline().rstrip("\n").split()))
    visited = [False] * (n + 1)
    current = 1

    while True:
        if current < 1 or current > n:
            print("FINITE", file=output_stream)
            break
        if visited[current]:
            print("INFINITE", file=output_stream)
            break
        visited[current] = True
        dir_char = s[current - 1]
        step = d[current - 1]
        current += step if dir_char == '>' else -step



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
>><
2 1 1
""",
            "output": \
"""\
INFINITE
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

n=3, s is '>><', d is [2,1,1].

current starts at 1.

Not visited. Mark. s[0] is '>', step 2. current becomes 3.

Check 3: not visited. Mark. s[2] is '<', step 1. current 3-1=2.

Check 2: not visited. Mark. s[1] is '>', step 1. current 2+1=3.

Now, current 3 is already visited. So output INFINITE.

Which is correct.

Another test case: n=1, s='>', d=1. current is 1. direction is '>', step 1. next is 2. Output finite.

Another test case where the grasshopper enters a loop after some steps. For example, n=4, s is '>>><', d = [2,1,3,1]. Let's see.

Start at 1. direction '>', step 2. current is 3.

Mark 3. direction '>', step 3. current is 6. Which is beyond 4. Output finite.

So that's finite.

Another case: n=4, s is '<<<<', d all 1. Grasshopper steps: 1 →0 → exit. Output finite.

So code should work.
</think>

```python
n = int(input())
s = input().strip()
d = list(map(int, input().split()))
visited = [False] * (n + 1)
current = 1

while True:
    if current < 1 or current > n:
        print("FINITE")
        break
    if visited[current]:
        print("INFINITE")
        break
    visited[current] = True
    dir_char = s[current - 1]
    step = d[current - 1]
    current += step if dir_char == '>' else -step
```
