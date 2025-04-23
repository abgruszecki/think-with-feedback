<think>
Okay, let's see. The problem is about Limak, the police officer, using a BCD device to determine which criminals he can be certain about. We need to calculate how many criminals he can catch based on the information from the BCD.

First, let me understand the problem step by step. The BCD tells Limak the number of criminals at each distance from his city a. For each distance d, the BCD gives the total number of criminals in all cities that are exactly d units away from a. But since cities are arranged in a straight line, for each distance d (except 0), there can be up to two cities: one to the left and one to the right of a. However, depending on the position of a, some distances might only have one city. For example, if a is the first city, then for distance d=1, there's only the city 2, and so on.

The key point here is that Limak can only be sure of a criminal's presence in a city if, for the distance d, the BCD's count matches the possible cities. For example, if for distance d, there's only one possible city (like when a is at the edge), then if the BCD says there's a criminal count of 1, Limak knows exactly that city has the criminal. Similarly, if there are two cities at distance d, but the BCD says the total is 2, then both must have criminals. Otherwise, if the BCD's count is 1, he can't be sure which one it is, so he can't catch either.

So, the approach is to:

1. For each possible distance d from 0 to max possible (which is max(a-1, n - a)), group the cities by their distance from a.
2. For each group (distance d), check if the BCD's count (sum of t_i in the cities at distance d) allows us to determine exactly which cities have criminals.
3. For each city in such a group, if the sum of criminals in the group equals the number of possible cities (so all must have criminals) or if there's only one city in the group (so the sum can only be 0 or 1, but if sum is 1 then that's the only one), then add those criminals to the total.

Let's think about how to structure this.

First, the cities are arranged in a line. For each city i, the distance is |i - a|. So, for each i from 1 to n, compute d = |i - a|.

Group all cities by their distance d. For each d, collect all cities that are at that distance. Then, for each group, if the sum of t_i for those cities is equal to the number of cities in the group, then all of them must have criminals. Otherwise, if the sum is 0, then none. But if the sum is between 1 and the group's size minus one, then Limak can't be sure about any of them except in the case when the group has only one city. 

Wait, no. Let's clarify:

For a group of cities with distance d, the BCD gives the sum of their t_i. For example, if the group has two cities (left and right), and the sum is 2, then both have criminals. If sum is 1, then Limak can't be sure which one, so he can't catch either. But if the group has only one city (like when a is at the edge), then sum can be 0 or 1. If it's 1, then that city is the only possibility, so he can catch that criminal.

So, for each distance d:

- Get all cities at that distance. Let's call the list cities_in_d.
- Compute the sum of t_i for those cities.
- The number of cities in the group is len(cities_in_d).
- If sum equals len(cities_in_d), then add all their t_i (since all must be 1).
- If sum is 0, add nothing.
- If sum is between 1 and len(cities_in_d)-1, then if len(cities_in_d) ==1, add sum (since sum can only be 0 or 1, but if sum is 1, then that's the only city). Otherwise, add 0.
Wait, no. Wait, when len(cities_in_d) is 1, then sum can only be 0 or 1. So if sum is 1, that's the only city in the group, so add 1. Otherwise, 0. So in that case, the sum is exactly the number of criminals that can be caught for that group.

Wait, no. For example, if a group has one city and the sum is 1, then Limak knows there's a criminal there. So that's added. If sum is 0, he knows there's none, so adds nothing.

So for each group:

If the sum is 0: add 0.

If the sum is equal to the group size: add sum (all criminals are present).

Else, if the group size is 1: add sum (since sum can only be 0 or 1, but sum is not 0 here (since sum is 0 is handled earlier), so sum must be 1. So add 1.

Wait, no. Wait, group size 1, sum is 0: add 0.

Group size 1, sum is 1: add 1.

If group size is more than 1 (like 2), and sum is 1: then the sum is 1, but there are two cities. So Limak can't determine which one, so adds 0.

So, for each group:

caught += sum if sum is 0 or sum == len(group) else (sum if len(group) == 1 else 0).

Wait, no. Let's rephrase.

If sum is 0: no criminals in that group. So add 0.

If sum is equal to the group size (for example, group of 2 and sum 2), then all have criminals. So add sum.

Otherwise:

if group size is 1: sum can't be anything else except 0 (handled) or 1. So sum is 1. So add 1.

But wait, when group size is 1, sum can only be 0 or 1. So if sum is 1, add 1. If sum is 0, add 0. So that's covered by the first two conditions.

Wait, for group size 1:

sum can be 0: add 0.

sum can be 1: which equals group size (1), so add 1.

So the two conditions (sum 0 and sum equals group size) cover all possibilities. So maybe the code can be written as:

for each group:

if sum == 0:

    add 0

elif sum == len(group):

    add sum

else:

    if len(group) == 1:

        add sum (but this can't happen because sum would be 0 or 1, and if len is 1, then sum would be 0 (handled) or 1 (sum == len). So this else clause is only for len(group) > 1 and sum not equal to len.

So perhaps the code can be written as:

total = 0

for each distance d:

    group = list of cities at distance d

    s = sum of t_i in group

    if s == 0:

        continue

    elif s == len(group):

        total += s

    else:

        # s is between 1 and len(group)-1

        # if group has only one city, this can't happen (since len(group) is 1, sum can only be 0 or 1. But 0 is handled above. So in else, len(group) must be >=2.

        # So in this case, Limak can't be sure, so add 0.

        # Wait, but in the problem statement, the BCD's sum is exactly the sum of t_i's in the group. So for the group, the sum is s, but Limak can only catch criminals in cities where he is sure. So if the group has two cities, and s is 1, then Limak can't catch either.

        # So for all groups where len(group) > 1 and sum is not equal to len(group) or 0, add 0.

So the code for each group is:

s = sum of t_i in group

if s == 0:

    contribute 0

elif s == len(group):

    contribute s

else:

    contribute 0

Wait, but for groups of size 1, the sum can only be 0 or 1. So for group size 1, the sum is 0 (handled) or 1 (sum equals len), so in all cases, the else clause is never entered for groups of size 1.

Thus, the code can be written as:

for each group:

    s = sum(t_i for i in group)

    if s == len(group):

        total += s

    elif s ==0:

        continue

    else:

        # group size must be >=2, sum between 1 and len-1

        # so no contribution

        pass

Wait, but what about groups of size 1 where sum is 0? That's handled by the first condition. Wait, no. If group is size 1 and sum is 0, then s is 0, so continue. So no contribution.

But when group is size 1 and sum is 1, then s equals len(group), so contribute 1.

So the code works for all cases.

Thus, the steps are:

1. For each city, calculate its distance from a.

2. Group the cities by their distance.

3. For each group:

   a. Compute the sum of t_i in the group.

   b. If the sum equals the number of cities in the group, add the sum to the total.

   c. Otherwise, add nothing (since sum is either 0 or between 1 and len-1).

Wait, but in the problem statement, the BCD gives the sum for each distance. So Limak knows the sum for each d. Then, he can only be sure about a city if all possible cities in that distance group must have criminals (sum equals group size), or if there's only one city in the group (sum is 1, which is group size 1).

Wait, but according to the code as written, when a group has sum equal to the group size, all cities in the group are counted. So that handles all cases.

So the algorithm is correct.

Now, how to implement this.

First, read n and a. Then, read the list of t's.

Then, create a dictionary to group cities by their distance from a.

Wait, but the cities are numbered from 1 to n. So for each city i (1-based index), the distance is |i - a|.

So, for each i in 1..n:

   d = abs(i - a)

   add (i, t_i) to the group for distance d.

Once all groups are created, process each group:

sum the t_i's. If the sum equals the group's length (number of cities in that group), add to total.

Otherwise, add nothing.

So the code can be structured as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, a = map(int, input_stream.readline().rstrip("\n").split())

    t = list(map(int, input_stream.readline().rstrip("\n").split()))

    from collections import defaultdict

    groups = defaultdict(list)

    for i in range(n):

        city = i + 1  # since input is 1-based

        d = abs(city - a)

        groups[d].append(t[i])

    total = 0

    for d in groups:

        members = groups[d]

        s = sum(members)

        if s == len(members):

            total += s

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 2
0 0 0 1 0
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

Second example:

5 2

0 0 0 1 0

Cities 1-5:

a is 2.

Distances:

city1: 1.

city2:0.

city3:1.

city4:2.

city5:3.

t array is [0,0,0,1,0].

groups:

d=0: city2, t=0. sum 0. contributes 0.

d=1: cities1 and3. t1=0, t3=0. sum 0. contributes 0.

d=2: city4, t=1. sum 1. len 1. contributes 1.

d=3: city5, t=0. sum 0. contributes 0.

Total is 1. Which matches the second example.

So the code seems to work.

Now, check the constraints. The maximum n is 100. So even for n=1e5, the code would work. But here n is up to 100. So no problem with time. The code is O(n), which is acceptable.

So the code is correct.
</think>

```python
n, a = map(int, input().split())
t = list(map(int, input().split()))

from collections import defaultdict
groups = defaultdict(list)

for i in range(n):
    city = i + 1
    d = abs(city - a)
    groups[d].append(t[i])

total = 0
for members in groups.values():
    s = sum(members)
    if s == len(members):
        total += s

print(total)
```
