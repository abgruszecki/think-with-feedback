<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The task is to process a list of participants in a bowling tournament and output their rankings. The rankings are determined first by their scores in descending order. If two participants have the same score, their names are sorted lexicographically. Then, the places are assigned. If multiple participants have the same score, they all share the same place range. For example, if two participants are tied for third place, they get 3-4, but if three are tied, it's 3-5, etc.

So, the steps I need to follow are:

1. Read the input: first n, then n lines of name and score.
2. Sort the participants first by score (descending), then by name (ascending).
3. Assign ranks to each participant, considering ties. When a group of participants have the same score, they all share a range of positions. The next group after a tie starts from the position after the last in the previous group.

Let me think about how to calculate the ranks.

Suppose after sorting, the participants are ordered as follows:

mike 44 (highest)
katya 33
ted 11
petya 10
vasya 10

In the first example, mike is first. Then katya is second. Ted is third. Then petya and vasya have the same score. Their positions are 4 and 5. So their ranks are 4-5.

So the approach is to group consecutive participants with the same score. For each group, all members get a rank that starts at the start position of the group and ends at the start + size -1.

So the key is to determine for each participant which group they belong to, and then calculate their start and end positions.

So, steps:

- Sort the list of participants as described.
- Iterate through the sorted list and group them by score.
- For each group, calculate the start and end positions.
- Then, for each participant in the group, output the appropriate place (either a single number if the group has size 1, or start-end if the group is larger).

How to group them? Let's see.

Once sorted, the first group is the first element. Compare each subsequent element's score to the current group's score. If same, add to the group. Otherwise, start a new group.

For each group, the start position is the previous group's end position +1. For example, first group (size 1) starts at 1, ends at 1. Second group (size 1) starts at 2, ends at 2. Third group (size 2) starts at 4, ends at 5.

So during the iteration:

Initialize current_position = 1.

For each group in the list of groups:

   group_size = len(group)
   start = current_position
   end = current_position + group_size -1
   for each participant in the group:
      if group_size ==1: output "start name"
      else: output "start-end name"
   current_position += group_size

Yes, that makes sense.

So the main challenge is to group the sorted list by score, and for each group compute the start and end positions.

Now, handling the data:

First, read all participants, store as a list of tuples (name, score). Then sort them in descending order of score, and ascending order of name in case of same scores.

Once sorted, group them. Then compute the start and end for each group.

So for the sorted list, we can loop through and group. For example:

sorted_list = sorted(participants, key=lambda x: (-x[1], x[0]))

Then, group consecutive elements where the score is the same.

But how to group them? We can iterate through the sorted list, keeping track of the current score. When the next element's score is different, we close the group.

So code steps:

sorted_people = sorted(participants, key=lambda x: (-x[1], x[0]))

groups = []
current_group = []
current_score = None

for person in sorted_people:
    if person[1] != current_score:
        if current_group:
            groups.append(current_group)
        current_group = [person]
        current_score = person[1]
    else:
        current_group.append(person)
groups.append(current_group)  # add the last group

Once we have the groups, then calculate the start and end positions for each group.

current_position starts at 1.

For each group in groups:

    group_size = len(group)
    start = current_position
    end = current_position + group_size -1
    for each person in group:
        if group_size ==1:
            place = str(start)
        else:
            place = f"{start}-{end}"
        print(f"{place} {person[0]}")
    current_position += group_size

Yes. That seems correct.

Now, what about the sample inputs?

Sample 1:

5 participants:

After sorting:

mike 44 (score 44)
katya 33 (33)
ted 11 (11)
petya 10 (10)
vasya 10 (10)

Groups:

Group1: [ (mike,44) ] → size 1. start=1, end=1. output "1 mike".
Group2: [ (katya,33) ] → size 1. start=2 → "2 katya".
Group3: [ (ted, 11) ] → size 1. start=3 → "3 ted".
Group4: [petya, vasya] → size 2. start=4, end=5. So each gets "4-5 ...".

Sample 2:

3 participants:

sorted as:

b 13 (score 13)
a 1 (1)
c 1 (1)

Groups: group1 (b) → start 1. group2 (a, c) → start 2, end 3. So each in group2 is "2-3".

So the output is as given.

Now, the code.

Read n, then read n lines.

Each line is split into name and score (score is integer).

Then sorted as per the key.

Then grouped.

Then process each group as above.

Now, code structure.

In Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    participants = []
    for _ in range(n):
        name, score = input_stream.readline().rstrip("\n").split()
        participants.append( (name, int(score)) )

    sorted_people = sorted(participants, key=lambda x: (-x[1], x[0]))

    groups = []
    current_group = []
    current_score = None

    for p in sorted_people:
        score = p[1]
        if current_score is None:
            current_group.append(p)
            current_score = score
        else:
            if score == current_score:
                current_group.append(p)
            else:
                groups.append(current_group)
                current_group = [p]
                current_score = score
    # add the last group
    groups.append(current_group)

    current_pos = 1

    for group in groups:
        group_size = len(group)
        start = current_pos
        end = current_pos + group_size -1
        for p in group:
            if group_size ==1:
                place_str = str(start)
            else:
                place_str = f"{start}-{end}"
            print(f"{place_str} {p[0]}", file=output_stream)
        current_pos += group_size



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
a 1
b 13
c 1
""",
            "output": \
"""\
1 b
2-3 a
2-3 c
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

After sorting: b 13, a 1, c 1.

Groups:

Group1: [('b',13)] → start 1.

Group2: [('a',1), ('c',1)] → start 2, end 3.

So output is as expected.

Another test case: when all have the same score.

For example, n=3, all score 5. Then they are sorted by name. Then group has size 3. So all get 1-3.

Yes.

Edge case: n=1. Then output "1 name".

Another case: two same scores. Like:

3

a 5

b 5

c 5

They form a group of 3. All get 1-3.

Another case: two groups with same scores. Like:

4

a 5

b 5

c 4

d 4.

After sorting, a and b (sorted lex) have 5. Then c and d (sorted lex) have 4. The groups are:

Group1: a and b (size 2). Start 1, end 2. Output 1-2 a, 1-2 b.

Group2: c and d. Start 3, end 4. Output 3-4 c and d.

Wait, no. Because group1 has size 2. So start is 1, end is 2. Then current_pos becomes 3. Group2 has size 2. start is 3, end 4. So each in group2 is 3-4.

Yes.

So the code seems correct.

Now, regarding the constraints.

Constraints are n up to 100. So even with O(n^2) algorithms, it's acceptable. But the code here is O(n log n) for the sort, which is optimal.

Memory-wise, even for n=100, the data is manageable. Each entry is a tuple of small size. So no problem.

So the code is optimal and should handle all cases correctly.

Now, code needs to read from stdin, output to stdout. No debug prints.

The code should have no unnecessary variables. Let me check.

Yes. The code should be correct.
</think>

```python
n = int(input())
participants = []
for _ in range(n):
    name, score = input().split()
    participants.append((name, int(score)))

sorted_people = sorted(participants, key=lambda x: (-x[1], x[0]))

groups = []
current_group = []
current_score = None

for p in sorted_people:
    score = p[1]
    if current_score is None:
        current_group.append(p)
        current_score = score
    elif score == current_score:
        current_group.append(p)
    else:
        groups.append(current_group)
        current_group = [p]
        current_score = score
if current_group:
    groups.append(current_group)

current_pos = 1
for group in groups:
    size = len(group)
    start = current_pos
    end = current_pos + size - 1
    for name, _ in group:
        if size == 1:
            print(f"{start} {name}")
        else:
            print(f"{start}-{end} {name}")
    current_pos += size
```
