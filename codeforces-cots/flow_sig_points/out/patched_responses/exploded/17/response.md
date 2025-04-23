<think>
Okay, let's tackle this problem step by step. The goal is to find the minimal number of piles needed to arrange all the boxes such that each box's strength constraint is satisfied. 

First, I need to understand the problem thoroughly. Each box can have at most xi boxes on top of it in the same pile. But since you can't stack more than one box directly on top of another, the pile must form a vertical stack where each step down adds one more box below. For example, if a box has strength 2, then in the pile, there can be up to two boxes above it. So, if a box is the k-th from the bottom in a pile, then its strength must be at least (k-1), because there are (k-1) boxes above it.

Hmm. Wait, no. Because the way the problem is described, the pile is constructed such that each box (from top to bottom) has some boxes above it. The i-th box (starting from the bottom) would have (i-1) boxes on top. So for each box in the pile, if it is in position j (from the bottom, 1-based), then its strength must be >= (j-1). Because the number of boxes on top of it is (j-1). Because the pile is built such that each box is directly on top of the previous. Like, the bottom box is position 1, the next is 2, etc. Wait, maybe I'm mixing up the positions here.

Wait, let's think differently. Suppose a pile has m boxes. The bottom box is the first, then the next is on top of it, etc. So the bottom box has m-1 boxes on top. So its strength must be >= m-1. The next one (second from bottom) has m-2 boxes on top, so strength >= m-2. And so on, up to the top box, which has 0 boxes on top.

So the problem reduces to arranging all the boxes into some number of piles, each of which has a certain length. For each pile of size k, the boxes in that pile must have strengths >= k-1, k-2, ..., 0 respectively. But how do we arrange the boxes into such piles to minimize the number of piles?

The key insight here is that the minimal number of piles required is determined by the maximum number of boxes that require a certain position in the pile. For example, consider the sorted list of box strengths. Let's sort them in non-decreasing order. Then, for each box i (after sorting), the maximum possible position it can occupy in a pile is (strength + 1). But when trying to assign boxes to positions, if we have a sorted list, we can check for each position j (starting from 1) whether the sorted box at position i (0-based) has a strength >= j-1. The minimal number of piles is the maximum number of boxes that are required up to each position j.

Wait, maybe this is similar to the problem where you need to arrange numbers and find the minimal number of increasing sequences. There's a theorem called Dilworth's theorem, but perhaps this problem can be solved using a greedy approach.

Alternatively, here's an approach that I've heard about for this type of problem:

Sort the boxes' strengths in non-decreasing order. Then, iterate through each box, and for each box x, the earliest pile it can be placed in is the one where the current number of boxes in that pile is <= x. If we can't find such a pile, we need to create a new one.

Wait, no. Wait, for example, if a box has strength s, then in a pile, it can be placed as the k-th box (from bottom), where k <= s+1. Because the k-th box from the bottom would have (k-1) boxes above it. So the strength must be >= (k-1). So k can be at most s+1. So when placing the box in a pile, we need to find the smallest possible pile where the current length of the pile is <= s. Because adding this box to that pile would make the pile's new length (current length + 1). For example, if the pile currently has length l, then after adding the box, the length becomes l+1. The box's strength must be >= (l+1-1) = l. So l must be <= s. Therefore, for each box s, the maximum allowed current pile length is s. So the problem becomes, for each s (sorted in non-decreasing order), assign it to the leftmost pile whose current length is <= s. If none, create a new pile.

Wait, that makes sense. Let's see with some examples.

Take the first example:

Input is 0 0 10. Sorted, they are 0,0,10.

We process each in order.

First 0: The allowed pile lengths are <=0. Since there are no piles, create a new pile. Now piles are [1].

Second 0: Again, allowed pile lengths are <=0. So need to create a new pile. Now piles are [1,1].

Third 10: The allowed pile lengths are <=10. The existing piles are [1,1], which are <=10. So add to the first pile. Now it becomes [2]. The second remains 1. So total piles is 2.

Which matches the example.

Another example: input is 0 1 2 3 4. Sorted. Each in order:

First 0: create pile [1].

Second 1: allowed current pile length <=1. Check existing piles. The existing pile is length 1. So 1 <=1? Yes. So add to it. Now pile becomes [2]. But the box's strength is 1. The pile's length after adding is 2, so the box is in position 2 (from bottom). So the strength is 1 >= (2-1) which is 1, which is okay. Then third box is 2. Existing pile is length 2. 2 <=2. Add to it, becomes 3. Then 3: 3 <=3, add. Then 4: 4<=4, add. So all in one pile. Correct.

Third example: 4 zeros. Sorted, all 0. Each needs to be in a pile where current length is <=0. So first 0: create a pile [1]. Second: need to create another pile. Third: another, fourth: another. Total 4.

So this approach works.

So the algorithm is:

1. Sort the list of strengths in non-decreasing order.

2. For each strength in the sorted list:

   a. Find the first pile whose current length is <= s. Because adding the box to this pile will make its new length (current length +1), and the box's strength must be >= (current length). So s >= current_length.

   b. If such a pile exists, add the box to it (increment the pile's length).

   c. Else, create a new pile with length 1.

The minimal number of piles is the number of piles after processing all boxes.

How to efficiently implement this?

But for n up to 100, even a straightforward approach would work. We can maintain a list of piles, each element representing the current length of the pile. For each box in the sorted list, iterate through the list of piles and find the first pile where length <= s. If found, increment that pile's length. If not, add a new pile of length 1.

But with n=100, and each step potentially iterating over up to 100 piles, this would be O(n^2) time, which is acceptable.

Let's test this approach against the examples.

Fourth example: input 0 1 0 2 0 1 1 2 10. Sorted: 0,0,0,1,1,2,2,10. Wait wait, the input is 0,1,0,2,0,1,1,2,10. So sorted gives 0,0,0,1,1,1,2,2,10. Let's process each:

0: create pile [1]

0: check existing pile (1). 1>0, can't add. So new pile. Now [1,1].

0: same. Now three piles [1,1,1]

1: look for first pile with length <=1. The first pile is length 1. So add to it: becomes 2. Now piles are [2,1,1]

Next 1: look for first pile <=1. The second pile is 1. Add to it, becomes 2. Piles [2,2,1]

Next 1: look for first pile <=1. Third pile is 1. Add to it, becomes 2. Piles [2,2,2]

Next 2: look for first pile <=2. All are 2. So add to first, becomes 3. Now piles [3,2,2]

Next 2: look for first pile <=2. The second is 2. Add to it, becomes 3. Piles [3,3,2]

Next 10: look for first pile <=10. All are 3,3,2. So the first pile is 3, which is <=10. Add to it, becomes 4. So total 3 piles. Which matches the example's output of 3.

So this approach works.

So the steps are:

Sort the strengths in non-decreasing order.

Maintain a list of piles' current lengths.

For each strength in sorted order:

   Find the first pile in the list with length <= current strength.

   If found, increment that pile's length.

   Else, add a new pile with length 1.

The answer is the length of the piles list.

Now, how to implement this efficiently.

In Python, for each box, we can loop through the piles and check for the first pile where the length is <= s. Once found, increment that pile's length.

Since the order in which the piles are checked can affect which pile is chosen, but since we want the leftmost possible, we need to check in order.

For example, in the first example, after two piles of length 1 each, the third box (strength 10) would check the first pile (length 1 <=10), increment it to 2.

Thus, the algorithm will work correctly.

Now, the code:

Read n.

Read the list of x_i.

Sort x_i in non-decreasing order.

Initialize a list called piles, which starts empty.

For each s in sorted_x:

   Iterate through the piles to find the first pile with length <= s.

   If found, increment that pile's length by 1.

   Else, append a new pile (length 1).

The answer is the length of the piles list.

Let's code this.

Sample Input 4:

9

0 1 0 2 0 1 1 2 10 → sorted is [0,0,0,1,1,1,2,2,10]

As per the example, the code correctly outputs 3.

Now, let's code.

The code would be:

Read n: n = int(input())

Read x list: x = list(map(int, input().split()))

Sort x: x.sort()

Initialize piles as a list.

For each s in x:

    for i in range(len(piles)):

        if piles[i] <= s:

            piles[i] += 1

            break

    else:

        piles.append(1)

The length of piles is the answer.

Yes, this code should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    x = list(map(int, input_stream.readline().rstrip("\n").split()))
    x.sort()
    piles = []
    for s in x:
        found = False
        for i in range(len(piles)):
            if piles[i] <= s:
                piles[i] += 1
                found = True
                break
        if not found:
            piles.append(1)
    print(len(piles), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
0 1 2 3 4
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    x = list(map(int, input_stream.readline().rstrip("\n").split()))
    x.sort()
    piles = []
    for s in x:
        found = False
        for i in range(len(piles)):
            if piles[i] <= s:
                piles[i] += 1
                found = True
                break
        if not found:
            piles.append(1)
    print(len(piles), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
0 0 0 0
""",
            "output": \
"""\
4
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

Sample 3: 4 zeros. Each step appends a new pile, leading to 4 piles.

Sample 4: the code correctly processes to 3 piles.

So all examples are handled correctly.

Time constraints: For n=100, each iteration may have to loop through up to 100 piles. 100*100 = 10^4 operations, which is acceptable.

Space is O(n), which is acceptable.

Thus, the code is correct.
</think>

```python
n = int(input())
x = list(map(int, input().split()))
x.sort()
piles = []
for s in x:
    found = False
    for i in range(len(piles)):
        if piles[i] <= s:
            piles[i] += 1
            found = True
            break
    if not found:
        piles.append(1)
print(len(piles))
```
