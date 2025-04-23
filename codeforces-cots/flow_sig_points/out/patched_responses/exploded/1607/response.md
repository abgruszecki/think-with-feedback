<think>
Okay, let's see. The problem is about groups of people waiting for a bus. The bus can carry m people each time. The groups are in order, and they load into the bus in that order. If a group can't fit entirely into the current bus, they wait for the next one along with the following groups. So, each time a bus comes, we start with the first group in the queue and add as many full groups as possible until adding another would exceed m. Then the bus leaves, and the next groups are considered in the next bus. But the groups are processed in the same order each time, just that some groups might be split across buses.

Wait, no. The problem statement says that if a group can't fit all into the current bus, they wait for the next. So the group is not split. So the process is: for each bus, we take as many groups as possible from the front, summing their people, but without exceeding m. Each group must be entirely in a bus. So we have to find for each bus how many groups can fit into it, starting from the current first group, until adding the next group would make the sum exceed m.

Wait, no. The first group starts entering. If the entire group fits (their size is <= remaining space), then they get on. If not, then the group doesn't get on at all. So for each bus, you process the groups in order, adding each group's a_i to the current bus's total as long as the sum does not exceed m. If adding a group would exceed m, then that group (and all remaining) have to wait for the next bus.

So the algorithm would be something like:

Initialize the number of buses to 0.

While there are groups left to process:

   current_bus_capacity = 0

   buses += 1

   for each group in the remaining groups:

      if current_bus_capacity + group's size <= m:

          add the group to the bus (current_bus_capacity += group's size)

          remove the group from the queue (or mark as processed)

      else:

          break (this bus is full, process next bus)

So the key is to process the groups in order, adding as many as possible per bus without exceeding m. Each time a bus is filled, we take as many consecutive groups from the front as possible, until adding the next would go over m.

The problem is to compute how many buses are needed.

So, for example, the first sample input:

4 3

Groups: 2,3,2,1

First bus:

Take the first group (2). Current sum 2 <=3. Then next group is 3. 2+3=5>3, so can't take. So first bus takes group 1. Then groups left are 3,2,1.

Second bus: sum starts at 3. Add group 3: 3. Sum is exactly 3. So take group 3. Then next group is 2. 3+2=5>3. So the bus takes group 2. Now groups left are 2,1.

Third bus: sum starts at 2. Add group 2's 2: total 2. Then next group is 1. 2+1=3 <=3. So add it. Now all groups are processed. So total 3 buses.

Which matches the sample output.

Another example:

3 4

Groups: 1,2,1.

First bus: 1+2+1 =4. So all fit. One bus.

So the algorithm is correct.

So how to model this in code?

We can process the groups in order, keeping track of the current bus capacity. For each bus, start adding groups until we can't add the next. Then increment the bus count and reset the current capacity.

So, in code:

Read n and m.

Read the list a of n integers.

Initialize buses =0.

current_index =0.

while current_index <n:

   current_bus =0

   buses +=1

   while current_index <n and current_bus + a[current_index] <=m:

       current_bus += a[current_index]

       current_index +=1

So for each bus, we process as many groups as possible from the current index onwards, adding their a[i] to current_bus until adding the next would exceed m.

Each iteration of the outer loop represents a new bus.

This approach is O(n), which is acceptable since n is up to 100. Even for n=1e5, this would be acceptable, but here n is small. So the code will be efficient.

So the code in Python would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    buses = 0

    current_index =0

    while current_index <n:

        buses +=1

        current_bus =0

        while current_index <n and current_bus + a[current_index] <=m:

            current_bus += a[current_index]

            current_index +=1

    print(buses, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 4
1 2 1
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

Second sample:

n=3, m=4.

a = [1,2,1]

current_index=0.

buses=1.

current_bus=1. current_index=1.

Check 1+2=3 <=4: yes. Add. current_bus=3, index=2.

Check 3+1=4: yes. Add. current_bus=4. index=3. Exit inner loop. So buses=1.

Correct.

Yes, this code should work.

Now, what about cases where a group's size is exactly m? For example, m=5 and group is 5. Then one bus per group. But code adds the group (since 0+5 <=5) and index increments. So that's correct.

Another test case: n=1, m=5. a=[5]. Then buses=1.

Another test case: n=5, m=5. a=[1,1,1,1,1]. All fit in one bus.

Yes.

So the code is correct.

Now, the constraints are n and m up to 100. The code runs in O(n) time, which is acceptable. For n=100, it's 100 steps. So even in Python, this is way under the time limit.

Memory usage is O(n) for storing the list. Which is also acceptable.

So the code is correct and efficient.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
buses = 0
current_index = 0
while current_index < n:
    buses += 1
    current_sum = 0
    while current_index < n and current_sum + a[current_index] <= m:
        current_sum += a[current_index]
        current_index += 1
print(buses)
```
