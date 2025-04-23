<think>
Okay, let's try to solve this problem. Hmm, the problem is about Arkady needing to get from his school (which is at x1) to his home (xn) using bike rentals. Each bike can be ridden for up to k kilometers. The key is that he can switch bikes at the rental points, and each time he does, the distance counter resets. We need to find the minimal number of bike rentals he needs, or return -1 if it's impossible.

So, first, what's the approach here? It feels like a greedy problem. Because we want to minimize the number of switches, the optimal strategy would be to go as far as possible with each bike. That way, each step covers the maximum possible distance, leading to fewer rentals.

Let me think. Let's start at x1. From there, he can take a bike and ride it. The maximum distance he can cover is x1 + k. So, the next rental point he can reach must be the farthest possible within this range. Then, from there, he repeats the process. If at any step there's no next point within reach, then it's impossible.

Yes, this makes sense. So the algorithm would be:

1. Start at position x1 (index 0). Count the first bike.
2. Find the farthest rental point that is <= current position + k.
3. If that point is xn (the end), return the count.
4. If there's no such point (i.e., next point is beyond current + k), return -1.
5. Otherwise, move to that farthest point, increment the count, and repeat.

But wait, how do we find the farthest point each time efficiently?

The rental points are sorted, so for each current position (say, at index i), we can look for the maximum j where x[j] <= x[i] +k. Then set current to j. If j is not found (i.e., i+1 is already beyond x[i] +k), then impossible.

So, for example, in the first sample input:

Points are 3,6,8,10. k=4.

Start at 3. Max reach is 3+4=7. The farthest point <=7 is 6 (index 1). Then from 6, max reach is 6+4=10. The farthest point is 10 (index 3). So total steps: 2.

In the second example, points are 10 and 20. k=9. Starting at 10, max reach is 19. But next point is 20, which is beyond. So return -1.

Third example: 12 points. The steps would involve jumping as far as possible each time.

So, the algorithm is to iterate through the points, greedily choosing the farthest possible each time.

Now, the implementation. The main challenge is to efficiently find the farthest point within x[i] +k each time.

The naive approach would be, for each current index i, loop from the next possible point (i+1) up to the end, check if x[j] <= x[i] +k, and track the maximum j. But with n up to 1000, this is O(n^2), which should be acceptable. Because 1000^2 is a million operations, which is manageable within Python's time constraints for a 1-second limit.

Alternatively, we can use binary search to find the farthest point. Since the array is sorted, for each current x[i], the maximum x[j] is the largest x <= x[i] +k. So binary search can find the upper bound, then subtract 1. This would reduce the per-step time to O(log n), but for n=1e3, even O(n) per step is okay. However, for code conciseness and efficiency, using binary search is better.

So, the steps would be:

Initialize current index to 0, count to 1 (since the first bike is taken).

Loop:

- Find the farthest index j where x[j] <= x[current] +k.

- If j is current (can't move), return -1.

- If j reaches the last index (n-1), return count.

- Else, set current to j, increment count.

Wait, wait. Wait, the initial current is 0. The first bike is taken. Then, each time we switch, we take a new bike, so count increments.

But when you take the first bike (at x1), that's count 1. Then, moving to j, take another, count becomes 2, etc.

Wait, the problem says "минимальное число раз ему необходимо будет взять велосипед в прокат, включая первый велосипед". So the initial bike is counted as 1.

So, the algorithm steps:

current = 0

count = 1

if x[-1] (xn) > x[0] +k: impossible (but since xn is the end, but maybe this is covered in the steps)

But let's proceed:

Loop:

Find the farthest j where x[j] <= x[current] +k.

If j == current, then there's no way to move forward, return -1.

If j >= n-1, then done. Return count.

Else:

current = j

count += 1

So, for example, in the first sample:

current is 0 (x=3). x[0] +k=7. The farthest j is 2 (x=8? Wait no. Wait the sample input is 3,6,8,10. So x[0] is 3, x[0] +4=7. The points up to 7 are 3,6. Because 8 is 8>7. So j would be 1. Then x[1] +4=10. So the farthest j is 3. So count becomes 2, which is correct.

So yes. So the code steps:

We can proceed as follows.

Now, the code:

We need to read n and k.

Then the list x.

Then, process the steps.

Initialize current = 0, count =1.

Then loop:

Find the maximum j such that x[j] <= x[current] +k.

If j is current, then return -1 (can't move).

If j is the last index, return count.

Else, set current to j, count +=1.

Repeat.

So, the key part is finding j for each current.

Implementing this with binary search.

In Python, the bisect module can help. For each current index i, x[i] +k is the target. We can use bisect_right to find the insertion point of x[i]+k, then subtract 1 to get the largest j where x[j] <= x[i]+k.

But wait, the list is sorted, so bisect.bisect_right returns the insertion point. For example:

x = [3,6,8,10], target 7: bisect_right would return 2 (since 7 is between 6 and 8). So j is 2-1=1.

Yes. So for x[i], target = x[i] +k. The insertion index is found with bisect.bisect_right(x, target) -1.

But since the list is 0-based, and the indices go from 0 to n-1.

So the code for finding j:

import bisect

current_x = x[current]

max_reach = current_x +k

j = bisect.bisect_right(x, max_reach) - 1

But we need to check that j is at least current +1. Because, for example, if the current is at index i, then j must be at least i+1. Otherwise, if j is <= i, then we can't move forward. Wait, no. For example, the current is i=0, and j is 0. That would mean x[0] +k is less than x[1], so we can't reach any further. So if j is <= current, then it's impossible. Because all next points are beyond current_x +k.

So in the code:

current = 0

count =1

while True:

    max_reach = x[current] +k

    j = bisect.bisect_right(x, max_reach) -1

    if j == current:  # can't move forward

        print(-1)

        exit()

    if j >= n-1:  # reached the end

        print(count)

        exit()

    # else, find the farthest possible j in [current+1, j]

    # but wait, j is the largest index where x[j] <= max_reach. So, the next current is j.

    current = j

    count +=1

Wait, but j can be any index between current+1 and the possible maximum. But in the code, after the first step, current is 0. j is the farthest possible. So next current is j, and count increases by 1.

For example, in the third sample input:

12 3

4 6 7 9 10 11 13 15 17 18 20 21

Let's see:

current is 0 (4). max_reach is 4+3=7. The x list up to 7 is 4,6,7. So bisect_right finds x[j] <=7. The insertion point for 7 is 3 (since x[3] is 9), so bisect_right returns 3, minus 1 is 2. So j is 2. count is 1. Then, current is 2 (7). max_reach is 7+3=10. x[j] <=10 is up to 11 (index 5). So j is 5. count becomes 2. Next, max_reach is 11+3=14. x[j] <=14 is 13 (index 6). count becomes 3. Then max_reach 13+3=16. x[j] is 15 (index 7). count 4. Then 15+3=18, find up to 18 (index 9). count 5. Then 18+3=21, which is the last index (11). So count becomes 6. So that's the correct answer.

So this approach works.

Now, code in Python.

But need to read the inputs. The first line is n and k. Second line is x1 to xn.

In Python, code:

Testing against sample input 2.

```python
import bisect


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    x = list(map(int, input_stream.readline().rstrip("\n").split()))

    current = 0

    count = 1

    while True:

        max_reach = x[current] + k

        j = bisect.bisect_right(x, max_reach) -1

        if j == current:

            print(-1, file=output_stream)

            return

        if j >= n-1:

            print(count, file=output_stream)

            return

        current = j

        count +=1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
12 3
4 6 7 9 10 11 13 15 17 18 20 21
""",
            "output": \
"""\
6
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

Another case: what if x has a point that's exactly current +k? For example, if x is [0,5,10], k=5. Then starting at 0, max_reach 5. j is 1. Then from 5, max_reach 10. j is 2. So count is 2.

Yes.

Now, what about a case where j is not the immediate next, but allows for multiple steps?

Like x = [0, 3, 4, 6, 8], k=5.

Start at 0: max_reach 5. The farthest is 3 (index 1) and 4 (index 2) and 6 (if 6 is <=5? No. So j is 2 (4). So next current is 2, count is 2. max_reach is 4+5=9. The farthest is 8 (index4). So count becomes 2 (since we can reach 8 in one step from 4).

So the code would find j=4, which is the end, so return count 2.

Yes.

So this code seems to handle the cases correctly.

What's the time complexity? For each step, a bisect is O(log n). The number of steps is O(n) in the worst case (like when each step moves only one point). But since n is up to 1e3, and log n is about 10, the total steps are 1e3 * 10 = 1e4 operations. Which is acceptable.

So this code should work.

Testing the third sample input:

12 3

4 6 7 9 10 11 13 15 17 18 20 21

We need to see how the steps go.

Current starts at 0 (4). max_reach 7. bisect_right returns index of first element >7. The elements are up to 7 (indices 0-2: 4,6,7). Next elements are 9. So bisect_right(x,7) returns 3. j=2. count=1.

current becomes 2 (7). max_reach 10. elements <=10 are up to 11 (index5). j=5. count=2.

current 5 (11). max_reach 14. elements <=14 are 13 (index6). j=6. count=3.

current 6 (13). max_reach 16. elements up to 15 (index7). j=7. count=4.

current7 (15). max_reach 18. elements up to 18 (index9). j=9. count=5.

current9 (18). max_reach 21. elements up to 21 (index11). j=11. So since j >= n-1 (11 ==11), return count=5+1? Wait, no. Wait, when j is 9, current is 9. Then max_reach is 18+3=21. bisect_right finds x=21. The list's last element is 21. So bisect_right returns 12 (since the list is of length 12, indices 0-11). So j=12-1=11. Then j is >=n-1 (11), so print count=5+1? No, the code increments count only when moving. Let's see:

At step:

current=9, count=5.

max_reach=18+3=21.

bisect_right returns 12 (since x[11] is 21, which is equal to 21). So j=12-1=11.

Check if j == current (9)? No. Then check if j >=n-1 (11==11), so yes. So output count=5. Wait, but that's not matching the sample's expected output of 6.

Wait, the sample's output is 6. So there's a problem here.

Wait, let's retrace the steps for sample 3:

Sample input 3:

12 3

4 6 7 9 10 11 13 15 17 18 20 21

Sample output is 6.

Let's compute the steps:

Initial current=0 (4), count=1.

max_reach 4+3=7. The farthest is 7 (index 2). So j=2. count becomes 1. Then current is 2, count increments to 2.

Then current=2 (7). max_reach 10. The farthest is 11 (index5). count becomes 3.

current=5 (11). max_reach 14. Farthest is 13 (index6). count 4.

current=6 (13). max_reach 16. Farthest is 15 (index7). count 5.

current=7 (15). max_reach 18. Farthest is 18 (index9). count 6.

current=9 (18). max_reach 21. Farthest is 21 (index11). j=11, which is the end. So count is 6. So the code should output 6.

But in the code, when current is 9, j is 11. So code checks if j >=n-1 (11 is 11, which is yes). Then prints count, which is 6. Because count is 6.

Wait, how does the code reach that?

Let's walk through the code steps:

current=0, count=1.

max_reach=4+3=7. bisect_right finds the insertion point for 7 in x. The elements are [4,6,7,9,10,11,13,15,17,18,20,21]. So 7 is at index 2. bisect_right returns 3 (since x[3] is 9, which is >7). So j=3-1=2. current is not j. j is not the last index. So current becomes 2, count increases to 2.

current=2 (7). max_reach=7+3=10. bisect_right looks for 10. The elements after 7 are 9,10,11, etc. 10 is at index4. bisect_right returns 5 (because after 10, the next is 11 at index5. So insertion point is5, j=5-1=4. So j is 4 (x=10). current is 2. j is not current. j is 4. Not last index. So current becomes4, count=3.

current=4 (10). max_reach 13. Elements after 10 are 11,13. 13 is <=13. bisect_right returns 6 (x[6] is 13. The next is 15. So insertion point for 13 is 6. j=5 (6-1=5? Wait wait. x[5] is 11, x[6] is13. So bisect_right for 13 would return 7? Wait no. Let's see:

x = [4,6,7,9,10,11,13,15,17,18,20,21]

Looking for 13 in x.

x[6] is13. The elements after are 15, etc. bisect_right returns 7. So j=7-1=6.

Wait, for current=4 (x=10), max_reach=10+3=13. So we need to find the largest x[j] <=13.

Looking in x: x[5] is 11, x[6] is13. So yes. So the insertion point of 13 is 7 (since x[6] is 13, and the next is 15. So bisect_right returns 7. j=7-1=6.

So current becomes6, count=3+1=4.

current=6 (13). max_reach=16. x[j] <=16 is 15 (index7), 17 is 17>16. So bisect_right for16 in x.

x[7]=15, x[8]=17. So insertion point is8. j=8-1=7. current becomes7, count=5.

current=7 (15). max_reach=18. x[j] <=18. The elements after 15 are17,18, etc. 18 is index9. So bisect_right(18) returns 10 (since x[9] is18, x[10] is20). So j=10-1=9. current becomes9, count=6.

current=9 (18). max_reach=21. bisect_right(x,21) returns 12 (since x[11] is21, and it's the last element). j=12-1=11. Now, j is 11, which is the last index (n-1=11). So code outputs count=6. Which is correct.

So the code works for the sample. So why when I tried to step through in my mind earlier, I thought current=9 would lead to count=5? Because I missed some steps. The code correctly increments the count each time.

So the code is correct.

Now, code:

We need to import bisect.

But in the code, after each step, the current is updated to j, and count increases.

Yes.

So, the code is correct.

Another possible edge case: when the total distance is exactly k. For example, n=2, x1=0, x2=5, k=5. Then code outputs 1. Because current=0, j=1. count is 1. j is n-1, so return 1. Correct.

Another edge case: when after some steps, the j is the same as current. Like, for example, x = [0, 2, 4], k=1. Then starting at 0, max_reach=1. j=0. So code returns -1.

So the code should handle all cases.

Thus, the code is correct.
</think>

```python
import bisect

n, k = map(int, input().split())
x = list(map(int, input().split()))

current = 0
count = 1

while True:
    max_reach = x[current] + k
    j = bisect.bisect_right(x, max_reach) - 1
    if j == current:
        print(-1)
        break
    if j >= n - 1:
        print(count)
        break
    current = j
    count += 1
```
