<think>
Okay, let's see. The problem is about finding the number of cars that definitely overtook someone else in the tunnel. The key point is that a car must be fined if there's at least one car it overtook. So, how do we model this?

Hmm, the input gives us the entry order and exit order. The entry order is a list of car IDs in the order they entered. The exit order is the order they left. 

The main idea is that if a car i entered after car j, but exits before car j, then i definitely overtook j, so i gets fined. But we need to find all such cars i where there exists at least one j that meets this condition.

So, the problem reduces to finding all cars that have at least one inversion in their entry-exit positions. 

Wait, but how to efficiently check for each car if there's any car that entered before them but exited after them. Because for a car x, any car y that entered before x but exits after x would mean x overtook y. So x should be fined if there's at least one such y.

So the approach is: for each car, check if there's any car that comes after it in the entry list but before it in the exit list. Wait no, wait. Wait, the entry order is a1, a2, ..., an. So a1 entered first, then a2, etc. The exit order is b1, b2, ..., bn. So b1 is the first to exit.

So for a car x, any car y that entered before x (i.e., x's entry position is after y's) but exits after x (i.e., x's exit position is before y's) would be a case where x overtook y. So for x to be fined, there must be at least one such y.

So the problem is to count all x where in the exit order, x appears before some y that entered before x.

But how do we model this efficiently?

Let's think in terms of the exit positions. For each car x, let's find the earliest exit position among all cars that entered after x. If any of those have exit positions earlier than x's, then x has overtaken someone. Wait, no, wait. Wait, no: for x to have overtaken someone, it's x that entered after someone else (y), but exits before that someone else (y). So x's entry is after y's entry, but exit is before y's exit. So for x, we need to find if there exists a y such that y's entry is before x's entry and y's exit is after x's exit.

So x is fined if there's a y where entry order of y < entry order of x, and exit order of y > exit order of x.

So for each x, the number of such y is the number of inversions where, in the entry sequence, y is before x, but in the exit sequence, y is after x. If that number is >=1, then x is fined.

So, the task is to count how many x have at least one such y.

Now, how do we compute this efficiently?

The straightforward approach would be for each x, check if there's any y in the entry list before x that has a higher exit position than x. But doing this naively for each x would result in O(n^2) time, which is not feasible for n up to 1e5.

So we need a more efficient way.

Alternative approach: Let's consider the exit order. For each car x, the exit position is the index in the b array. Let's create a mapping from car id to its exit position. For example, exit_pos[x] = i where b[i] = x.

Then, for each car in the entry order (a array), we can process them in order. As we process each car, we want to track the maximum exit position we've seen so far. Because if the current car's exit position is less than the maximum exit position up to that point, then there exists a car that entered before it (since we're processing in entry order) and has a higher exit position. So this current car must be fined.

Wait, yes! Because as we process cars in the order they entered, the maximum exit position up to the previous car is maintained. If the current car's exit position is less than this maximum, then there is at least one car before it (in entry order) that has a higher exit position, meaning that the current car exited before those cars, hence overtaking them. So the current car will be fined.

But if the current car's exit position is greater than or equal to the maximum so far, then it doesn't overtake any previous cars. However, if in the future, there are cars that have lower exit positions than this one, then those cars would have entered after this one and exited before. So those future cars would overtake this one. But for the current car, the only way it's fined is if it exits before some car that entered before it.

Ah, right. So the maximum exit position so far is tracked as we process the entry order. For each car in the entry order, if its exit position is less than the current maximum, then it must have overtaken at least one car (the one with the maximum exit position up to that point). Otherwise, the maximum is updated to this car's exit position.

This way, for each car, we can determine in O(1) time whether it has to be fined. The total time would be O(n), which is feasible for n up to 1e5.

So the steps would be:

1. Create a dictionary to map each car's id to its exit position. For example, exit_pos[b[i]] = i.

2. Iterate through the entry order (a array). For each car in a:

   a. Get its exit position from exit_pos.

   b. If this exit position is less than the current maximum exit position, then increment the result count.

   c. Else, update the current maximum to this exit position.

3. The result count is the number of cars to be fined.

Wait, does this capture all possible cases where a car has overtaken someone?

Yes. Because the maximum exit position up to the current point (i.e., before processing this car) represents the earliest exit time of any car that entered before the current car. If the current car's exit time is earlier than that maximum, then there's a car before it that exits after, hence the current car must be fined.

But wait, the maximum is the maximum of all exit positions up to and including the current car, or just up to the previous cars?

Let's see. As we process each car in entry order (a1, a2, ..., an), we keep track of the maximum exit position among the first i cars (after processing the ith car). For each car, if its exit position is less than the maximum before processing it, then there was a previous car with a higher exit position. Because when processing a_i, the maximum before processing a_i is the maximum of a_1 to a_{i-1}. So if a_i's exit position is less than that maximum, then a_i's exit is earlier than some a_j (j < i) which has exit position equal to that maximum. So a_i entered after a_j but exited before a_j, thus a_i is fined.

But what if there are multiple cars before a_i that have higher exit positions? Then a_i is still fined once, but according to the problem statement, each car is fined at most once. But since the problem requires that the car is fined if it has at least one such occurrence, this approach correctly counts the car if there's at least one such occurrence.

Yes, because the moment the current exit position is less than the maximum so far (from previous cars), the current car is fined, regardless of how many such previous cars there are.

So this approach would correctly count all cars that have at least one overtaking.

For example, let's look at the first sample input:

5

3 5 2 1 4

4 3 2 5 1

The exit positions are:

b array is 4,3,2,5,1. So exit_pos for 4 is 0 (since it's first), 3 is 1, 2 is 2, 5 is 3, 1 is 4.

Now, processing the entry order 3,5,2,1,4:

Process 3: exit_pos[3] is 1. The current maximum is 1. So no previous cars, so max becomes 1. Not fined.

Process 5: exit_pos[5] is 3. Current max is 1 (from 3). 3 is less than 3? No. So 5's exit is 3. Since 3 > current max (1), so max updates to 3. Not fined.

Process 2: exit_pos[2] is 2. Current max is 3. 2 < 3 → fined. So count becomes 1.

Process 1: exit_pos[1] is 4. Current max is 3. 4 > 3 → update max to 4. Not fined.

Process 4: exit_pos[4] is 0. Current max is 4. 0 <4 → fined. So count becomes 2. Which matches the sample.

So this approach works.

Another example: second sample input.

7

5 2 3 6 7 1 4

Exit order is 2,3,6,7,1,4,5.

So exit_pos for 5 is 6, 2 is 0, 3 is 1, 6 is 2,7 is 3, 1 is 4,4 is 5.

Processing entry order:

5 → exit_pos is 6. Max is 6. Not fined.

2 → exit 0. Current max is 6. 0 <6 → fined. Count 1.

3 → exit 1. Max is 6. 1 <6 → fined. Count 2.

6 → exit 2. <6 → fined. Count 3.

7 → exit 3. <6 → fined. Count4.

1 → exit4. Current max is 6. 4 <6 → fined. Count5.

4 → exit5. <6 → fined. Count6.

So total 6, which matches the sample.

Third sample:

2

1 2 → entry order.

exit order 1 2. So exit_pos for 1 is 0, 2 is 1.

Processing 1: max becomes 0. Not fined.

Processing 2: exit pos is 1, which is larger than current max (0). So max becomes 1. Not fined. So output 0.

So this approach works.

So the algorithm is O(n) time and O(n) space. Which is acceptable for 1e5.

Thus, the plan is:

- Create a dictionary to map each car to its exit position.

- Iterate through the entry order, keeping track of the maximum exit position encountered so far.

- For each car in entry order, check if their exit position is less than the current maximum. If yes, increment the count. Otherwise, update the maximum.

Thus, the code can be written as follows.

Now, the code steps:

Read n.

Read a as list of integers.

Read b as list of integers.

Create exit_pos dictionary, where exit_pos[b[i]] = i for i from 0 to n-1.

Initialize max_so_far = -infinity.

count = 0.

Loop over each car in a:

   pos = exit_pos[car]

   if pos < max_so_far:

       count +=1

   else:

       max_so_far = pos

Return count.

Yes, that's the code.

Testing the code against the samples.

Sample 1:

n=5

a=3 5 2 1 4

b=4 3 2 5 1 → exit_pos is 4:0,3:1,2:2,5:3,1:4.

Processing a in order:

3's pos is 1. max is -inf → set to 1. no count.

5's pos is3. 3>1 → set to3. no count.

2's pos is2. 2<3 → count=1.

1's pos is4. 4>3 → set to4. no count.

4's pos is0 <4 → count=2.

Which is correct.

Sample 2:

n=7

a=5,2,3,6,7,1,4.

b=2,3,6,7,1,4,5.

exit_pos:

2:0, 3:1, 6:2,7:3,1:4,4:5,5:6.

Processing:

5 → pos 6 → max=6. No count.

2 → pos 0 <6 → count=1.

3 → pos1 <6 → count=2.

6 → pos2 <6 → count3.

7 → pos3 <6 → count4.

1 → pos4 <6 → count5.

4 → pos5 <6 → count6.

So correct.

Thus, the code is correct.

So, the code is straightforward. Now, the only thing to note is that in Python, dictionaries are O(1) for lookups, so building the exit_pos as a list or a dictionary is possible. But since the car ids are from 1 to n, it's efficient to create a list where exit_pos[x] is the position of x in the b array.

So for example, in code:

exit_pos = [0]*(n+1)  # since car numbers are 1-based.

for i in range(n):

    exit_pos[b[i]] = i

Then, for each car in a, get exit_pos[car].

So in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    exit_pos = [0]*(n+1)

    for idx, car in enumerate(b):

        exit_pos[car] = idx

    max_so_far = -1

    count =0

    for car in a:

        pos = exit_pos[car]

        if pos < max_so_far:

            count +=1

        else:

            max_so_far = pos

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
5 2 3 6 7 1 4
2 3 6 7 1 4 5
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

So the code works.

Another test case where no overtaking happens:

n=2, a=[1,2], b=[1,2]

exit_pos[1] =0, exit_pos[2]=1.

Processing:

1: pos0. set max to0.

2: pos1>0 → set max to1. count remains 0.

Output 0.

So all correct.

Thus, this code should handle all test cases efficiently, in O(n) time and O(n) space. For n=1e5, this is acceptable.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

exit_pos = [0] * (n + 1)
for idx, car in enumerate(b):
    exit_pos[car] = idx

max_so_far = -1
count = 0

for car in a:
    pos = exit_pos[car]
    if pos < max_so_far:
        count += 1
    else:
        max_so_far = pos

print(count)
```
