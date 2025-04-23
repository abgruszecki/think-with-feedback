<think>
Okay, let's tackle this problem. So the task is to find the maximum number of matches the burglar can take by choosing up to n matchboxes, considering that each container has ai matchboxes each with bi matches. The key here is to maximize the matches taken by selecting the best possible matchboxes.

Hmm. The first thing that comes to mind is that we should prioritize taking the matchboxes with the highest number of matches first. Because each matchbox from a container gives bi matches. So, containers with higher bi should be taken as much as possible until we reach the n limit.

So the plan is: sort the containers in descending order of bi. Then, for each container in this sorted list, take as many matchboxes as possible (either all from the container or as many as needed to fill the remaining capacity of the rucksack).

Let's think about the example. For instance, in the first example input:

7 3
5 10
2 5
3 6

The containers have bi values 10,5,6. Wait, no. Wait, the containers are the 3 entries. The first container has 5 boxes each with 10 matches. Second has 2 boxes with 5 each. Third has 3 boxes with 6 each. So when sorted by bi descending, the order is 10,6,5. Then we take 5 boxes from the first (bi=10), contributing 5*10=50. Then take all 3 from the third (bi=6), which is 3*6=18. Now total boxes taken is 5+3=8. But the rucksack can hold only 7. Wait, wait. Oh right! Because n is 7. So 5 boxes from the first (bi=10) uses 5 boxes. Then remaining 2. The next container (bi=6) has 3 boxes. Take 2 of them. So 5*10 + 2*6 = 50+12=62, which matches the sample output.

So the approach is correct. So the steps are:

1. Sort the containers in descending order of bi.
2. For each container in this order, take as many as possible (either all ai or up to remaining n), multiply by bi, add to total.
3. Subtract the taken boxes from n, and stop when n reaches 0.

Now, considering the constraints. Let's look at the input constraints:

n can be up to 2e8, m is up to 20. Each ai can be up to 1e8. Bi is up to 10.

So for each container, we need to take min(ai, remaining_n) boxes.

But since m is small (20), even iterating through all m containers is feasible. Even for m=20, the loop is negligible.

So the steps in code:

- Read n and m.
- Read m pairs of ai and bi.
- Sort the pairs in descending order of bi.
- Initialize remaining = n, total = 0.
- For each (a, b) in sorted list:
   take = min(a, remaining)
   total += take * b
   remaining -= take
   if remaining ==0: break
- Output total.

Yes, that seems straightforward.

Now, let's test against the examples.

First example:

n=7, m=3.

Containers after sorting: (5,10), (3,6), (2,5).

First, take 5 from first. Remaining is 2. Add 5*10=50. Next container (3,6): take 2, add 12. Total is 62. Correct.

Second example:

3 3

Containers are (1,3), (2,2), (3,1). After sorting by bi, it's (1,3), (2,2), (3,1). So take all 1 from first, 2 from next. 1*3 +2*2 =3+4=7. Correct.

So the algorithm works.

Now, handling the input. Each container's ai and bi are read, then sorted. So in code:

In Python, read m lines, collect the ai and bi pairs. Then sort them with key=lambda x: -x[1].

Yes.

Now, considering that m is small (20), and each operation is O(1) per container, the code will be very efficient even for the maximum inputs. The sorting is O(m log m) which is negligible. Then a loop through m steps. So time-wise, this is acceptable.

Memory-wise, storing m pairs (each with two integers) is trivial. Even for m=20, it's 20*2 integers. So no problem with memory.

Therefore, this approach is optimal. There's no way to optimize further, as we need to take the highest possible bi first. The problem is a classic greedy algorithm scenario where the optimal solution is achieved by taking the best options first.

Now, code.

Read n and m from the first line. Then read m lines, each with ai and bi.

Sort the list in descending order of bi.

Then iterate, accumulate the matches.

So the code would be:

n, m = map(int, input().split())
containers = []
for _ in range(m):
    a, b = map(int, input().split())
    containers.append( (b, a) )  # because we sort by bi, but need to sort in reverse order of b. So maybe better to have a tuple (-b, a) or similar.

Wait, wait. When sorting in Python, if we sort by -x[1], but in the code, the containers are stored as (a, b) pairs. Wait, in the code, after reading ai and bi, perhaps we should collect tuples of (bi, ai), then sort them in reverse order.

Wait, the containers are stored as (ai, bi). But for each container, we want to sort by bi in descending order.

Wait, the input for each container is ai and bi. So in the code, when reading, perhaps we should collect (bi, ai), then sort by bi in descending order.

Wait, no. Let's see. For each container i, there are ai matchboxes, each with bi matches. So for maximum efficiency, we need to take as many as possible from containers with higher bi.

So the code steps:

Read n and m.

Then for each of m lines, read ai and bi, and store in a list as (bi, ai).

Then sort this list in reverse order of bi (i.e., from highest to lowest).

Then for each (b, a) in this sorted list:

take min(a, remaining) boxes, add to total, subtract from remaining.

Yes.

So the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    containers = []
    for _ in range(m):
        a, b = map(int, input_stream.readline().rstrip("\n").split())
        containers.append( (b, a) )  # storing as (bi, ai)
    containers.sort(reverse=True)  # sorts by first element (bi) descending
    total = 0
    remaining = n
    for b, a in containers:
        if remaining <=0:
            break
        take = min(a, remaining)
        total += take * b
        remaining -= take
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
1 3
2 2
3 1
""",
            "output": \
"""\
7
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

Another example: second input.

3 3

1 3 → (3,1)

2 2 → (2,2)

3 1 → (1,3)

Sorting in reverse gives (3,1), (2,2), (1,3). Then:

Take min(1,3) →1. total=3. remaining=2.

Next (2,2): take min(2,2) →2. total +=4. remaining 0. total 7. Correct.

So the code works.

Now, considering the constraints. The code reads m containers, sorts them, loops through them.

Even with m=20, it's manageable.

Time constraints: the code will process each container in O(1) steps. The sorting is O(m log m), which for m=20 is negligible. So even with n up to 2e8, the code is fast.

In Python, even for large numbers, arithmetic operations are handled quickly.

So the code should pass all test cases within the time limits.

Memory-wise, the containers list is O(m), which is 20 elements, so no problem.

Thus, the code is optimal.
</think>

```python
n, m = map(int, input().split())
containers = []
for _ in range(m):
    a, b = map(int, input().split())
    containers.append((b, a))
containers.sort(reverse=True)
total = 0
remaining = n
for b, a in containers:
    if remaining <= 0:
        break
    take = min(a, remaining)
    total += take * b
    remaining -= take
print(total)
```
