<think>
Okay, let's see. So the problem is about cutting trees either to the left or right, such that their fallen intervals don't overlap. And we need to maximize the number of trees cut. Hmm.

First, the trees are given in order of increasing x coordinates. That's important because the order will affect which trees can be felled. So processing them in order makes sense.

The key is to decide for each tree whether to cut it left, right, or not at all. But how do we choose optimally?

Let me think about a greedy approach. Because each decision affects the next trees. For example, if we fell a tree to the right, it might block the next trees. Similarly, falling left might interfere with previous trees.

Wait, but since the trees are processed in order of increasing x, maybe we can process them left to right, keeping track of the last occupied position. That way, for each tree, we can first try to fell it to the left if possible. If that's not possible, try to the right. Otherwise, leave it.

Wait, but the optimal choice might not be just left first. Like, maybe if we choose to fell a tree to the right, it allows more trees to be felled later. For example, if the next tree is very close, but if we fell current right, then next can't fall left, but if we leave current, next can fall left and right. So greedy might not work. But given the constraints of n up to 1e5, a dynamic programming approach might be necessary. But DP for 1e5? Let's think.

Alternative approach: For each tree, we can track the earliest possible position to the right that a tree can occupy. Let's process the trees in order and keep track of the last position occupied.

So for each tree, we have three possibilities:

1. Don't cut it. Then the last position remains the previous one.
2. Cut it to the left. The new interval is [x_i - h_i, x_i]. Check if this interval's start is after the previous end.
3. Cut it to the right. The interval is [x_i, x_i + h_i]. Check if this start is after the previous end.

But the decision for the current tree affects the next trees. So perhaps a greedy approach that always chooses the best possible option for the current tree (i.e., preferring left if possible, then right, else not cutting) might not be optimal. But maybe in some cases, choosing to cut right even when left is possible allows more trees to be cut later.

For example:

Suppose we have three trees at positions 1, 5, 6. Heights h1=3 (so left would be -2 to 1), h2=2 (left would be 3-5, right 5-7), h3=1 (left 5-6, right 6-7). Let's say the first tree is cut left, then the second can't be cut left (since 3 is after 1), but can it be cut right? Then it's 5-7, which would block the third tree. If instead, the first tree is not cut, then the second can be cut left (5-2=3 to 5?), no. Wait, x2=5, h2=2. So left would be 3 to 5. Third tree is at 6. If second is cut left (3-5), then third can be cut left (6-1=5 to 6), but the previous end is 5, which is okay. So in that case, cutting the second left allows the third to be cut left. So total 3 trees. Alternatively, if the first is cut left, second can't be cut left (since 3 is after previous end of 1). Wait, no. Wait, first tree is cut left to -2 to 1. Then the second tree's left interval is 3-5. Since 3 is after 1, that's okay. Then the third tree's left is 5-6. So that's okay. So all three can be cut. Hmm. So maybe the initial approach works.

But maybe there's a case where not cutting a tree allows more options. Let's see another example.

Suppose trees at positions 1, 4, 5. h1=3 (left: -2 to 1, right: 1-4). h2=1 (left:3-4, right:4-5). h3=1 (left:4-5, right:5-6).

If first is cut right (1-4), then the second can't be cut left (3 is within 1-4). So second can be cut right (4-5). Then third's left would be 4-5, but 4 is at 5's position. Wait, the third tree's x is 5. So cutting left would be 5-1=4, so interval 4-5. But the previous end is 5 (from the second tree being cut right to 5). So the third tree can't cut left because 4-5 starts at 4, but the previous end is 5. Wait, no. Wait, the previous interval is 4-5. So the third tree's left interval is 4-5. That's overlapping, so it's not allowed. So third can't be cut left. If third is cut right (5-6), then 5-6 starts after 5, so that's okay. So in this case, first is cut right (occupies 1-4), second is cut right (4-5), third is cut right (5-6). Total 3.

Alternatively, if the first tree is cut left (ends at 1), then the second can be cut left (3-4), then the third can be cut left (4-5). That's 3 again.

So in this case, both options give the same result. But perhaps there are cases where choosing to cut in a certain way gives a better result.

Hmm. So maybe the optimal approach is to process the trees in order and, for each tree, choose the best possible option (left first, then right, then none) based on the current state.

But how do we model the state? The state is essentially the last occupied position. For example, after processing each tree, the maximum number of trees cut and the last occupied position would be tracked.

But since we can't track all possible previous states for each tree (as that would be O(n) time which is manageable but maybe tricky), perhaps a dynamic programming approach where for each tree, we track the best possible options: either not cutting it, cutting left, or cutting right, based on the previous state.

But for each tree, there are three possibilities. But maybe we can model it with two variables: the maximum number of cuts up to the previous tree, along with the last occupied position. But since the last position depends on the previous choices, perhaps for each tree, we can track the best possible scenario (left cut, right cut, or not cut) and choose the option that allows the maximum count.

Alternatively, since the trees are processed in order, and for each tree, the decision only affects the next trees, perhaps a greedy approach is feasible. The idea is to always try to cut the tree to the left first, then to the right, in a way that allows the maximum possible trees.

Wait, here's an idea: for each tree, the earliest possible position to the left that can be taken, so that the next trees can have as much space as possible. So, if we can cut a tree to the left, that leaves the earliest possible end, which might allow more trees to be cut. Alternatively, cutting to the right might block some trees but allow others.

Wait, let's think. If we cut a tree to the left, its interval is [x_i - h_i, x_i]. Then the next tree can start after x_i. If we cut it to the right, the interval is [x_i, x_i + h_i], so the next tree has to start after x_i + h_i. But if we don't cut it, the next tree can start after x_i.

So, cutting to the left leaves the earliest possible end (x_i), which allows more flexibility for the next trees. So perhaps a greedy approach is to always cut to the left if possible, otherwise to the right, else not.

But wait, maybe sometimes cutting to the right allows a better arrangement. For example:

Imagine tree 1 at x=1 with h=2. Tree 2 at x=3 with h=1.

If we cut tree 1 to the left (interval [-1,1]), then tree 2 can be cut to the left (2-3), which starts after 1. So both can be cut. Total 2.

Alternatively, if we cut tree1 to the right (1 to 3), then tree2 can't be cut (its x is 3, which is in the interval [1,3], so can't cut left (2-3) or right (3-4) because 3 is in the previous interval). So in that case, cutting left is better.

But what if the next tree is x=4. Then cutting tree1 to the right would allow tree2 (x=4) to be cut left (4- h= something). Wait, perhaps this is a case where the optimal approach is to always choose the left first.

So perhaps the greedy approach is: for each tree in order, try to cut left first. If possible, do it. Then, if not possible, try to cut right. Otherwise, don't cut. This would maximize the number of trees cut.

But why is that the optimal approach? Because cutting left leaves the earliest possible end position, allowing more trees to be cut in the future. So even if cutting right seems possible now, it might block future trees.

But let's see an example where cutting right could allow more trees.

Example:

Tree 1: x=1, h=2. Tree2: x=2, h=1. Tree3: x=4, h=1.

If we cut tree1 left: interval [-1,1]. Tree2 can't cut left (2-1=1 to 2, which starts at 1 which is the end of previous. So that's allowed. So tree2 can be cut left (1-2) but since previous end is 1, the start is 1, which is allowed (since the previous interval ends at 1). So yes. Then tree3 can be cut left (4-1=3 to 4, but previous end is 2. So 3 is after 2, so allowed. So total 3.

Alternatively, if tree1 is cut right (1 to 3), then tree2's x=2 is within 1-3. So can't be cut. Tree3 can be cut left (3-4). So total 2.

So cutting left is better here.

Another example where cutting right could be better.

Tree1: x=1, h=3. Tree2: x=3, h=2. Tree3: x=5, h=2.

If tree1 is cut left ([-2,1]). Then tree2 can be cut left (3-2=1 to 3. So starts at 1, which is after previous end. So allowed. Then tree3 can be cut left (5-2=3 to5. Starts at 3, which is after previous end of 3. So allowed. Total 3.

If tree1 is cut right (1 to4). Then tree2's x=3 is in the interval. So can't be cut. Tree3 can be cut left (5-2=3 to5. But the previous end is 4, so 3 <4. So can't. So tree3 can be cut right (5 to7). So total 2.

So again, cutting left is better.

Hmm. So maybe the greedy approach is the way to go. Let's formalize it.

Initialize the last occupied position to -infinity.

For each tree in order:

- Try to cut left: check if x_i - h_i > last_pos. If yes, then cut left. Update last_pos to x_i. Increment count.
- Else, try to cut right: check if x_i + h_i < next_tree's x (if there is a next tree). Wait, no. Wait, cutting right would occupy [x_i, x_i + h_i]. The next tree is at x_{i+1} > x_i. So the next tree's possible left cut is x_{i+1} - h_{i+1}, which must be >= x_i + h_i (if current is cut right). But how do we know? Because the next tree's x is bigger than current's x. So when cutting right, the interval is [x_i, x_i + h_i]. The next tree's x is higher than x_i. So if the next tree is processed, its x is higher than x_i + h_i, then cutting right here is safe. Otherwise, if the next tree's x is <= x_i + h_i, then even if we cut right here, the next tree can't be cut left (since x_i + h_i >= next x - h_next). But perhaps the next tree can be cut right.

But in the current step, how do we decide whether cutting right is possible? Because the next tree's x is higher than current x. So the interval for cutting right here is [x_i, x_i + h_i]. So the next tree's x must be > x_i + h_i? No. The next tree's x is given in order. So x_{i+1} > x_i. But if we cut right, the interval ends at x_i + h_i. So for the current tree, to cut right, we need to check that x_i + h_i is less than the next tree's x. Because otherwise, if the next tree's x is <= x_i + h_i, then even if we cut right here, the next tree's x is within the current interval, so the next tree can't be cut left. But maybe the next tree can be cut right.

Wait, for example:

Current tree at x=5, h=5. Next tree is x=6, h=1. If we cut current to the right (5-10), then the next tree's x is 6, which is within 5-10. So the next tree can't be cut left (6-1=5 is within 5-10) or right (6+1=7 is also within 5-10). So it can't be cut. So cutting current right here would prevent the next tree from being cut.

But if we didn't cut current, then the next tree can be cut left (5 to 6-1=5 to 6?), but wait, x is 6. So cutting left gives [5,6], which is okay if previous end is <=5. If previous end was 5 (from not cutting the current tree). Then yes. But the current tree's x is 5. So if current tree is not cut, then the next tree's left interval starts at 5. Since current tree's x is 5, which is a point. So the next tree's left interval [5,6] doesn't overlap with current tree's position. So cutting next left is allowed.

But how to model this when processing the current tree? Because the next tree's x is 6. So when processing current, the next tree's x is known. But how to make the decision.

Ah, perhaps when processing the current tree, when considering cutting to the right, the interval [x_i, x_i + h_i] must not include x_{i+1}, the next tree's x. Because if x_i + h_i >= x_{i+1}, then even if we cut current to the right, the next tree's x is inside the interval, so the next tree can't be cut in any direction.

So to maximize the total, perhaps cutting right is only allowed if x_i + h_i < x_{i+1}.

But how do we know that? Because the next tree's x is known when processing the current tree.

So the greedy approach can be:

For each tree i from 1 to n:

1. Check if cutting left is possible. The left interval is [x_i - h_i, x_i]. For this to be allowed, x_i - h_i must be > last_occupied_pos. If yes, cut left, increment count, set last_occupied_pos to x_i.

2. Else, check if cutting right is possible. The right interval is [x_i, x_i + h_i]. This is allowed only if x_i + h_i < x_{i+1} (if there is a next tree), and x_i must be > last_occupied_pos. Wait, because if previous intervals ended before x_i, then cutting right here would occupy x_i to x_i +h_i. So x_i must be > last_occupied_pos. Because the current tree's x is after the previous occupied position. So the interval [x_i, ...] must not overlap with the previous interval.

Wait, no. The previous interval could have ended before x_i. For example, suppose last_occupied_pos was 10. Current tree's x is 15. Then cutting right would start at 15, which is after 10. So allowed.

So for cutting right to be allowed, the current x_i must be > last_occupied_pos, and the end of the right interval (x_i + h_i) must be before the next tree's x (if there is one). Because if there's a next tree, and x_i + h_i >= x_{i+1}, then cutting right here would make the next tree's x be inside the interval, so the next tree can't be cut in any direction (since the next tree's x is part of the current interval). Thus, by cutting right here, we might block the next tree from being cut.

So the condition to cut right is:

current x_i > last_occupied_pos and (if there is a next tree, x_i + h_i < x_{i+1} else true).

But wait, even if there's no next tree, cutting right is allowed as long as x_i > last_occupied_pos.

So for the current tree, after checking left, if left is not possible, check right. So:

if (x_i > last_occupied_pos) and (x_i + h_i < x_{i+1} or i is the last tree).

But in the code, how to handle this? For i from 0 to n-1:

current x_i is known. next_x is x_{i+1} if i <n-1 else infinity (so that x_i +h_i is always less than next_x).

Wait, but the next_x is known for all except the last tree. So for the last tree, cutting right is allowed as long as x_i > last_occupied_pos.

So for the current tree i:

If cutting left is possible (x_i - h_i > last_occupied_pos), then do it.

Else, check if cutting right is possible. For cutting right:

x_i must be > last_occupied_pos (so that the start of the interval is after the previous end).

Also, the end of the interval (x_i +h_i) must be < next_x (if i is not the last tree).

If both conditions are met, then cut right. Update last_occupied_pos to x_i +h_i. Increment count.

Else, do not cut.

This seems like a valid approach. Let's test it against the sample inputs.

Sample 1:

Input:

5

1 2

2 1

5 10

10 9

19 1

Processing in order.

Tree 1 (x=1, h=2):

Check left. x_i -h_i = -1. last_occupied_pos is initially -infinity. So yes. Cut left. count=1. last_occupied = 1.

Tree 2 (x=2, h=1):

Check left. x_i -h_i = 1. last_occupied is 1. So 1 is not >1. So can't. Check right.

x_i is 2 >1. Next_x is 5. 2+1=3 <5. So yes. Cut right. count=2. last_occupied =3.

Tree 3 (x=5, h=10):

Check left:5-10= -5. Which is <3. Can't. Check right. 5>3. Next_x=10. 5+10=15>10. So condition 5+10 <10 is false. So can't cut right. So no cut. count remains 2. last_occupied remains 3.

Tree4 (x=10, h=9):

Check left:10-9=1>3? No. Check right. x=10>3. next_x=19. 10+9=19. 19 <19 is false. So can't. So no cut. count remains 2.

Tree5 (x=19, h=1):

Check left:19-1=18>3. Yes. So cut left. count=3. last_occupied=19.

So output is 3. Which matches the first sample.

Sample 2:

Input:

5

1 2

2 1

5 10

10 9

20 1

Last tree's x is 20.

Tree4 (x=10, h=9). Next x is 20.

Check left:10-9=1>3? No. Check right. 10>3. next_x=20. 10+9=19 <20. So yes. Cut right. count increases to 3. last_occupied=19.

Tree5 (x=20). Check left:20-1=19>19? No. Check right. 20>19. No next tree. So yes. Cut right. count=4.

So output is 4. Which matches the sample.

So the approach works for these samples.

Another test case. Let's take the example where cutting right allows next tree to be cut.

Suppose trees:

1 3 (x=1, h=3)

4 2 (x=4, h=2)

6 1 (x=6, h=1)

Processing:

Tree1 (1,3). Left:1-3=-2. last is -inf. So cut left. last=1. count=1.

Tree2 (4,2). left is 4-2=2>1. So cut left. last=4. count=2.

Tree3 (6,1). left is 5>4. Cut left. count=3. So total 3.

Alternative scenario: suppose tree1 is cut right. Let's see.

Tree1: check left not possible (if possible). So left is allowed. So the code would cut left first.

But in another example, perhaps:

Tree1 is x=1, h=1. Tree2 x=3, h=1. Tree3 x=4, h=5.

If tree1 is cut left: interval 0-1. Tree2 can't cut left (3-1=2, which is after 1. So cut left. Tree2 left is 2-3. Then tree3 can be cut left (4-5=-1?), no. Wait, x=4, h=5. x_i -h_i= -1. Which is <3 (last_occupied_pos after tree2 is 3). So can't. So can we cut right? 4+5=9. Next tree's x? None. So yes. So total 3.

But if tree1 is cut right (1-2), then tree2 x=3. Check left:3-1=2>2 (from previous interval's end). No. Check right:3+1=4. Next x is 4. So 4 >=4. So can't. So tree2 can't be cut. Then tree3's x=4. Check left:4-5=-1 <2. Can't. Check right. 4+5=9. No next tree. So yes. So count is 2.

So cutting left first is better.

So the algorithm's approach of trying to cut left first, then right, seems to work.

So the code can be written as follows:

Read n.

Read the list of (x, h) in order. Then, for each tree from 0 to n-1:

current x, h = trees[i]

next_x = trees[i+1][0] if i <n-1 else infinity.

If i ==n-1, next_x is infinity (so x_i +h_i < next_x is True).

Check left: if (x - h) > last_pos:

   cut left. count +=1. last_pos =x.

Else:

   check if can cut right: x > last_pos and (x +h) < next_x.

   if yes:

      cut right. count +=1. last_pos =x +h.

   else:

      do nothing.

So, code steps.

Implementing this in Python.

But for n=1e5, the code must be efficient. But since it's O(n), it's acceptable.

Now, code.

We need to read n lines. Each line has x and h. We need to process them in order.

In Python:

Read n.

trees = []

for _ in range(n):

    x, h = map(int, input().split())

    trees.append( (x, h) )

Then, for each i in 0..n-1:

x, h = trees[i]

next_x = trees[i+1][0] if i+1 <n else float('inf')

Check if (x - h) > last_pos:

Yes: cut left. Update last_pos to x. count +=1.

Else:

Check if x > last_pos and (x +h) < next_x:

Yes: cut right. Update last_pos to x +h. count +=1.

Else: do nothing.

Initialize last_pos = -infinity. count=0.

Yes.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    trees = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(n)]

    last = -float('inf')

    count = 0

    for i in range(n):

        x, h = trees[i]

        next_x = trees[i+1][0] if i <n-1 else float('inf')

        # Try left

        left = x - h

        if left > last:

            count +=1

            last = x

            continue

        # Try right

        right = x + h

        if x > last and right < next_x:

            count +=1

            last = right

            continue

        # else, do nothing. last remains as it was.

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2
2 1
5 10
10 9
20 1
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

Sample 2:

i=3 (x=10, h=9). next_x=20.

Check left:1>3? No.

Check right: x=10>3. right=19 <20 → yes. count becomes 3. last=19.

i=4: x=20, h=1. next_x is infinity.

left=20-1=19>19? No.

Check right: x=20>19. right=21 <inf. yes. count=4.

So code works.

Another test case where the next tree's x is exactly x_i +h_i. For example, x_i=5, h=5, next_x=10. x_i +h_i=10. So 10 < next_x (10) → no. So can't cut right. So in this case, cutting right is not allowed.

Yes, because the interval would be [5,10], and the next tree's x is 10. So next tree's x is in the interval. So cutting right is blocked.

Thus, the code correctly skips cutting right in this case.

So the code should handle all cases correctly.
</think>

```python
n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]
last = -float('inf')
count = 0

for i in range(n):
    x, h = trees[i]
    next_x = trees[i+1][0] if i < n-1 else float('inf')
    
    if x - h > last:
        count += 1
        last = x
    else:
        right = x + h
        if x > last and right < next_x:
            count += 1
            last = right

print(count)
```
