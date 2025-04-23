<think>
Okay, let's see. The problem is to balance the load of servers by moving tasks between them, and find the minimum number of seconds needed. Each second, you can move one task from one server to another. So the goal is to compute the minimal total steps required to make the difference between the maximum and minimum loads as small as possible, which would ideally be zero or one.

First, I need to find out what the target configuration looks like. Because the sum of all tasks is fixed. Let's call the total sum S. Then, the average per server is S divided by n. Since tasks can't be split, each server should have either average or average plus one, depending on whether the sum is exactly divisible by n.

For example, if the sum is 10 and there are 3 servers, the average is 3.333, so two servers will have 3 and one will have 4. So the maximum minus minimum would be 1, and the total steps needed are the sum of how much each server deviates from the average (but considering whether they are above or below).

Wait right. The sum of all tasks is S = sum(mi). Each server will end up with either avg = S//n or avg +1. Because if S is not divisible by n, there will be S mod n servers that have avg +1 tasks, and the rest have avg. So the minimal possible difference is 0 if S is divisible by n, else 1.

So the steps needed are the sum of the absolute differences between each server's initial load and the target values. But since moving a task from a higher-than-target server to a lower one contributes 1 per task, but each move is counted as one step. So the total steps is the sum of (mi - target) for all mi that are above the target. Because for each such mi, you have to move (mi - target) tasks down, and those below need to receive (target - mi) tasks. The sum of the excesses should equal the sum of the deficits, which they do because the total sum is S.

So the approach is:

1. Calculate the total sum S of the array.
2. Compute the average per server, which is avg = S // n. The remainder r = S % n.
3. The target will be that r servers have avg +1 tasks, and the rest have avg.
4. For each server, if it's in the group that should be avg +1, then the target is avg +1, else avg. Wait, no. Wait, the sum S = avg * n + r. So r servers will have avg +1, and the rest will have avg. So the target for each server is either avg or avg +1, depending on how many need to be the higher value.

Wait no. The target is that exactly r servers will have avg +1, and the remaining n - r will have avg. Because r is the remainder when S is divided by n. So the sum of (avg+1)*r + avg*(n-r) = avg *n + r = S.

So, when calculating the required steps, we need to calculate for each server how much it's above or below the target. But the target isn't uniform for all servers. Wait, but perhaps the optimal arrangement is that all servers are either at avg or avg +1, but exactly r of them are at avg +1. So the way to compute the steps is to look at how much each server contributes to the total steps based on whether they are above or below their target.

Wait, no. Because the steps needed are the sum of the absolute differences between each server's initial value and the target. But the target is such that exactly r servers are at avg+1, and the rest at avg. So for each server, the target depends on whether it's one of the r servers.

But how do we choose which servers are which? Because we can choose any r servers to be the ones that have avg+1. So the minimal steps would be achieved by selecting the r servers that have the highest initial loads. Because those would require the least steps if they are allowed to have avg+1. Wait, perhaps not. Let's think.

Alternatively, the way to compute the steps is that for all servers, if their initial load is higher than avg, then they need to give away (mi - avg) tasks. But for the r servers that are allowed to have avg+1, they can keep one more. So the steps would be the sum of (mi - avg) for all servers, minus the r servers that can have one more. Wait, maybe.

Wait, let's think of it like this. The total excess is sum(max(0, mi - avg) for all servers). But since r servers can have up to avg +1, those servers can contribute (mi - (avg +1)) if mi is higher than avg +1. Wait, perhaps not. Let me see.

Let me take an example. Suppose the sum is 7 and n=3. So avg is 2, remainder 1. So one server will have 3 (avg+1), others 2. Suppose the servers are [5, 0, 2]. Sum is 7. The target is two servers with 2 and one with 3.

For the server with 5: it's 3 over avg. But since it's allowed to be one of the servers that can have 3 (since r=1), so the excess is 5 -3 =2. For the server 0: it's 2 below avg, so need to add 2. For the server 2: it's exactly avg, no change. So total steps is 2 + 2 =4.

But wait, if the server with 5 is allowed to have 3, then the steps needed for that server is 5-3=2. The others: 0 needs to reach 2 (steps 2), and 2 can stay at 2. So total steps is 2+2=4. Which is correct.

So the steps are the sum of (mi - target_i) for each server, where target_i is either avg or avg +1, depending on whether the server is one of the r selected.

But the key is that the sum of (mi - target_i) for all servers must be zero. Because the sum of target_i is exactly S. So the steps needed are the sum of all (mi - target_i) for mi > target_i. Because the excesses must equal the deficits. So for each server, if mi is above its target, we sum (mi - target_i). The servers below their targets will have (target_i - mi), but since those must equal the sum of excesses, we can compute just the sum of the excesses.

So the problem reduces to: find which servers are allowed to have avg +1 (exactly r of them), such that the sum of (mi - target_i) for all mi > target_i is minimized.

Wait, but the way the target is set is that exactly r servers can have avg +1. So for the servers that are allowed to have avg +1 (r servers), their target is avg +1. For the rest, it's avg.

So when calculating the excess for each server, for the servers in the allowed group (r servers), their excess is max(0, mi - (avg +1)). For the others, their excess is max(0, mi - avg). Then, the sum of all these excesses is the total steps needed.

But how do we choose which r servers are allowed to have avg +1 to minimize the total steps?

Ah, here's the key. To minimize the total steps, we need to assign the avg +1 to the r servers with the largest mi. Because these are the servers that are most likely to have a higher mi than avg +1, so by allowing them to have one more, we reduce their excess.

Wait, for example, consider a server with mi = avg +5. If it's allowed to have avg +1, then its excess is 4. If not, it's 5. So allowing it to be in the allowed group reduces the excess by 1. So for all servers where mi is higher than avg, we want as many as possible to be in the allowed group (r servers) to minimize the excess.

But since the allowed group is exactly r servers, the optimal choice is to select the r servers with the highest mi. Because for each of them, being allowed to have avg +1 reduces their excess by 1 compared to if they were not allowed.

So the algorithm is:

1. Compute sum S of the array.

2. Compute avg = S // n, r = S % n.

3. Sort the array in non-decreasing order.

Wait, but if we want the r largest elements, perhaps sorting in non-increasing order is better.

But perhaps the sorted array isn't needed. Wait, no. Because to find the r largest elements, we can take the last r elements in the sorted array.

So the steps are:

For each server:

- if the server is one of the r largest (mi), then its target is avg +1. The excess is mi - (avg +1) if mi > avg +1, else 0.

- else, target is avg. Excess is mi - avg if mi > avg, else 0.

Sum all these excesses.

So the steps are:

- Sort the array in non-decreasing order.

- For each element in the array, if it's among the last r elements (since they are the largest), then compute max(0, mi - (avg +1)).

- For the others, compute max(0, mi - avg).

Sum all these values.

Wait, but what if the array has elements less than avg +1?

For example, if a server is in the allowed group (r largest) and its mi is 3, and avg +1 is 4. Then, its excess is 0. So it's allowed to have one more, but since it's below the target, it's not contributing to the excess.

But in this case, since sum is fixed, there must be other servers that have higher than their target. So the sum of excesses is correct.

So the approach is:

Sort the array.

For the first n - r elements (since the sorted array is in increasing order), their target is avg. For the last r elements, their target is avg +1.

For each element, subtract the target from the element if it's larger than the target. Sum all these.

So the code can be written as:

sum all (mi - avg) if mi > avg for the first n - r elements, and sum (mi - (avg +1)) if mi > (avg +1) for the last r elements.

Wait, but the sorted array is in increasing order. So the last r elements are the largest. So for each of the last r elements, if mi is greater than avg+1, then we add (mi - (avg+1)) to the total. For the first n - r elements, if mi is greater than avg, add (mi - avg) to the total.

But wait, when the array is sorted in increasing order, the first n - r elements could also have mi > avg. For example, suppose avg is 2, and a server is in the first n - r group (target is avg=2) but mi is 5. Then, that server contributes 3 to the total.

But since we're allowed to choose which servers are in the allowed group (the ones that can have avg+1), the optimal choice is to select the r largest mi's as the allowed group. Because for those, their target is higher, so their excess is lower.

For example, in the third sample input:

5
1 2 3 4 5

Sum is 15. avg is 3, r is 0. So all servers must have 3. The steps are sum of (1-3) is 0 (since it's below), (2-3) same, (3-3) 0, (4-3) 1, (5-3) 2. Total 3. Which matches the sample output.

Wait, but in that case, r is 0. So all servers must be at 3. So the steps are sum of (mi - 3) for each mi >=3. So (3-3) is 0, (4-3) 1, (5-3) 2. Sum is 3.

So that's correct.

Another sample: the first input is 2 servers, sum 7. avg is 3, r is 1. So the allowed group has 1 server, which is the larger of the two. So target for the larger server is 4, the other 3. The steps are (6-4) =2 for the larger, (1-3) is 0 (since it's below). Sum 2.

Which matches the sample.

So the code steps are:

Compute the sum S, then avg and r.

Sort the array.

For each element in the first (n - r) elements (sorted in increasing order), subtract avg. If the element is greater than avg, add the difference. For the remaining r elements (the largest ones), subtract (avg +1) and add the difference if it's positive.

So the code can be written as:

Read n.

Read the array m.

sum_m = sum(m)

avg = sum_m // n

r = sum_m % n

m_sorted = sorted(m)

total = 0

for i in range(n - r):

    if m_sorted[i] > avg:

        total += m_sorted[i] - avg

for i in range(n - r, n):

    if m_sorted[i] > avg + 1:

        total += m_sorted[i] - (avg +1)

print(total)

Wait, but in the first loop, we are looking at the first (n-r) elements. But since the array is sorted in increasing order, these are the smaller elements. But their target is avg. So for each of them, if they are larger than avg, they contribute (mi - avg). If they are less than avg, they are part of the deficit and don't contribute to the excess. Because the excess is only from servers that have more than their target.

But wait, if a server in the first (n - r) group has mi > avg, then that's possible. For example, the array is [2,3,3,3] with n=4 and sum 11. avg is 2 (11//4=2, r=3). So r is 3. So the first n -r =1 server has target 2. The others have 3. Suppose the sorted array is [2,3,3,3]. For the first server, 2 <=2: no contribution. For the remaining 3, each is 3. So target is 3. So they don't contribute. So total is 0.

Yes.

Another example: if the array is [4,4,4], sum 12, avg 4, r=0. All servers must be 4. So no steps needed.

So the code seems correct.

Now, what about the time and memory constraints?

n can be up to 1e5. Sorting 1e5 elements is O(n log n), which is acceptable for Python in 2 seconds. Because 1e5 log 1e5 is about 1e5 * 17 = 1.7e6 operations, which is manageable.

The sum is O(n), which is also acceptable.

Memory-wise, storing the array is O(n), which is acceptable for 1e5 elements (each being up to 2e4, but in Python, integers are stored as objects, but 1e5 elements are manageable).

So the code would be as follows:

Read n.

Read list m.

sum_m = sum(m)

avg = sum_m // n

r = sum_m % n

sorted_m = sorted(m)

total = 0

for i in range(n - r):

    if sorted_m[i] > avg:

        total += sorted_m[i] - avg

for i in range(n - r, n):

    if sorted_m[i] > avg + 1:

        total += sorted_m[i] - (avg + 1)

print(total)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    m = list(map(int, input_stream.readline().rstrip("\n").split()))
    total_sum = sum(m)
    avg = total_sum // n
    remainder = total_sum % n
    sorted_m = sorted(m)
    result = 0

    for i in range(n - remainder):
        if sorted_m[i] > avg:
            result += sorted_m[i] - avg

    for i in range(n - remainder, n):
        if sorted_m[i] > avg + 1:
            result += sorted_m[i] - (avg + 1)

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
10 11 10 11 10 11 11
""",
            "output": \
"""\
0
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

Third sample: 5 elements. sum is 15, avg=3, r=0. So all targets are 3. sorted [1,2,3,4,5]. For all 5 elements. First 5-0=5 elements. For each, if mi>3: 4>3 contributes 1, 5>3 contributes 2. So total 3. Correct.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    m = list(map(int, input_stream.readline().rstrip("\n").split()))
    total_sum = sum(m)
    avg = total_sum // n
    remainder = total_sum % n
    sorted_m = sorted(m)
    result = 0

    for i in range(n - remainder):
        if sorted_m[i] > avg:
            result += sorted_m[i] - avg

    for i in range(n - remainder, n):
        if sorted_m[i] > avg + 1:
            result += sorted_m[i] - (avg + 1)

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2 3 4 5
""",
            "output": \
"""\
3
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

So the code works for the samples.

Edge cases:

What if all servers are 0? Then sum is 0, avg is 0. r=0. All must be 0. So steps 0.

What if one server has a very high number. For example, n=1. Then sum is m1. avg is m1, r=0. So target is avg. So steps 0.

Wait, but the problem says n is a positive integer. So for n=1, the difference is 0, steps 0.

Another case: n=3, sum=4. avg=1, r=1. So one server can be 2, others 1. So sorted array [0,0,4]. The first 2 (n-r=3-1=2) elements are 0 and 0. Their target is 1. So 0 is less than 1, no contribution. The third element is 4. Target is 2. 4-2=2. So total steps 2.

Which is correct. For example, moving two tasks from the third server to the first and second. Each task takes one second.

So the code works.

So the code should be correct.
</think>

```python
n = int(input())
m = list(map(int, input().split()))
total_sum = sum(m)
avg = total_sum // n
remainder = total_sum % n
sorted_m = sorted(m)
result = 0

for i in range(n - remainder):
    if sorted_m[i] > avg:
        result += sorted_m[i] - avg

for i in range(n - remainder, n):
    if sorted_m[i] > avg + 1:
        result += sorted_m[i] - (avg + 1)

print(result)
```
