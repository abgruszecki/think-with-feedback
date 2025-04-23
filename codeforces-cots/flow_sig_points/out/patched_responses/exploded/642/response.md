<think>
Okay, let's try to figure out how to solve this problem. The problem is about tracking the bone's position through a series of swaps, considering that if it ever lands on a hole, it stops moving. So, the main challenge is to efficiently track where the bone is after each swap, check if it's in a hole, and if so, break early.

First, let's understand the input. We have n cups arranged in positions 1 to n. The bone starts at position 1. Then, we have m holes which are certain positions. Then, k swaps: each swap exchanges the cups (and their contents, including the bone) at two positions. So, whenever a swap happens, if the bone is in either of the two positions being swapped, it moves to the other position. But if at any time (before or after a swap) the bone is in a hole, it falls through and remains there.

So the steps we need to do are:

1. Read the initial holes and check if position 1 is a hole. If yes, the bone is already in a hole, and we can output 1 immediately (but only if the first position is a hole). But according to the problem statement, the bone is initially at position 1. So the initial check is important.

Wait, the problem says that if the bone is at any time (including after a swap) in a hole, it falls into the hole and won't be affected by future swaps. So before any swaps, we need to check if position 1 is a hole. Because if it is, then the bone is already in a hole, and all the swaps don't matter.

So first step: check if the initial position (1) is a hole. If yes, output 1 and that's it.

Otherwise, process each swap in order, updating the bone's position, and after each swap, check if the new position is a hole. If it ever is, break and output that position. Otherwise, after all swaps, output the current position.

So the algorithm is:

- Check initial position (1) in the holes. If present, output 1.
- Else, track the bone's current position, starting at 1.
- For each swap (u, v):
   - If current pos is u, it becomes v.
   - Else if current pos is v, it becomes u.
   - Check if new position is a hole. If yes, break and output.
- After all swaps, output current position.

The key is to efficiently check if a position is a hole. Since m can be up to n (1e6), we need a way to check in O(1) time. So the best way is to store the holes in a set. Since the holes are given as a list of distinct integers, converting them into a set will allow O(1) lookups.

So steps:

Read n, m, k.

Read the m holes into a set. Check if 1 is in the set. If yes, output 1.

Else, current_pos is 1.

For each of the k swaps:

   u, v = the two positions.

   if current_pos is u or v:

       swap the current_pos (if u, then set to v; if v, set to u)

       check if new current_pos is in the holes set.

       if yes, break and output.

So this approach is O(k) time, which is acceptable since k is up to 3e5, which is manageable.

The main thing is to process each swap in O(1) time, and check for the hole quickly.

Now, considering the constraints:

- n can be up to 1e6, but storing a set of m holes (up to 1e6) is manageable. In Python, even with m=1e6, the set will take some memory, but 1e6 elements are manageable (each int is about 28 bytes, so 1e6 would be 28MB, which is acceptable for the 256MB limit).

So the steps in code would be:

Read n, m, k.

Read the m holes as a list, then convert to a set.

Check if 1 is in the set: if yes, print 1 and exit.

Else, current_pos is 1.

Loop through each swap:

   u, v = map(int, input().split())

   if current_pos == u:

       current_pos = v

   elif current_pos == v:

       current_pos = u

   else:

       continue (no change)

   if current_pos in holes:

       break the loop

After processing all swaps, print current_pos.

This should work.

Now, let's test against the examples.

First example:

Input:

7 3 4

3 4 6

1 2

2 5

5 7

7 1

Holes are {3,4,6}.

Initial position is 1, which is not in the holes.

First swap: 1 and 2. Current pos is 1, so becomes 2. Check 2 not in holes. Proceed.

Second swap: 2 and 5. Current is 2, becomes 5. Check 5 not in holes.

Third swap:5 and7. Current is5, becomes7. 7 is not a hole.

Fourth swap:7 and1. Current is7, becomes1. Check 1 not in holes. After all swaps, output 1.

But wait, after the first swap, the bone is at 2, then swapped to 5, then 7, then 1. None of these positions are in the holes. So output is 1.

The sample output is 1, which matches.

Second example:

5 1 2

2

1 2

2 4

Holes are {2}.

Initial pos is 1. Not a hole.

First swap 1 and 2. Current is 1, becomes 2. Now, check if 2 is in holes (yes). So break, output 2.

So the code works.

So the code seems correct.

Now, for the code:

We need to read the inputs efficiently.

In Python, for large inputs, reading with input() can be slow. So using sys.stdin would be better.

But for k up to 3e5, in Python, using a loop with input() might be slow. So perhaps using sys.stdin to read all the lines at once.

But the code structure would be:

Read n, m, k.

Read the m holes.

Read k swaps, process each as we read them.

But for m, the holes are given in the second line. So split that line into integers, make a set.

So code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().split())

    holes = set(map(int, input_stream.readline().split()))

    if 1 in holes:

        print(1, file=output_stream)

        return

    current = 1

    for _ in range(k):

        u, v = map(int, input_stream.readline().split())

        if current == u:

            current = v

        elif current == v:

            current = u

        # else, do nothing

        if current in holes:

            break

    print(current, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 1 2
2
1 2
2 4
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

Second example:

holes is {2}.

current is 1.

First swap 1 and2 → current becomes2. Then check if in holes. Yes. Break and print 2.

Yes.

So the code seems correct.

Now, for the edge cases:

Test case where the initial position is a hole: output 1 immediately.

Test case where the bone moves to a hole in a swap. Like:

n=2, m=1, k=1.

holes is 2.

Initial pos 1.

Swap 1 and 2. current becomes2. Check in holes. So output 2.

Another case: the bone is swapped multiple times, but ends up in a non-hole.

Another case: the bone is in a position that is swapped multiple times, but after each swap, the new position is not a hole until the last swap.

So the code should handle all these.

Thus, this approach should work.
</think>

```python
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    holes = set(map(int, sys.stdin.readline().split()))
    if 1 in holes:
        print(1)
        return
    current = 1
    for _ in range(k):
        u, v = map(int, sys.stdin.readline().split())
        if current == u:
            current = v
        elif current == v:
            current = u
        if current in holes:
            break
    print(current)

if __name__ == "__main__":
    main()
```
