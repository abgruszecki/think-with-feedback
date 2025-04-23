<think>
Okay, so I need to solve this problem where the goal is to find the optimal floor x for the elevator to minimize the total electricity units used by all the people in the building. Let's see. 

The problem says that each person uses the elevator twice a day: once to go down from their floor to the first floor, and once to come back up. For each of these trips, the elevator has to move in a certain way. 

Let me break down what happens when a person on floor a uses the elevator. 

For the morning trip (from a to 1):
1. The elevator starts at x, goes to a (distance |x - a|).
2. Then goes from a to 1 (distance |a - 1|).
3. Then returns from 1 back to x (distance |1 - x|). Wait, no, no. Wait, according to the problem statement, after each trip, the elevator returns to x. So each time a person uses the elevator for a trip (either down or up), the elevator's movement is as follows: 

Each individual trip (like a to b) is processed as three steps:
- Move from x to a: distance |x - a|.
- Move from a to b: distance |a - b|.
- Move back to x: distance |b - x|.

So each trip contributes (|x - a| + |a - b| + |b - x|) * number of people on floor a. 

But since each person makes two trips per day: one from their floor to 1 (a to 1) in the morning, and then another from 1 to a in the evening. 

Each of these two trips contributes their own cost. 

So for each person on floor i, the total electricity for their two trips is:

Morning trip: (|x - i| + |i - 1| + |1 - x|) * 1 (per person)
Evening trip: (|x - 1| + |1 - i| + |i - x|) * 1 (per person)

Wait, but in the evening, the person is going from 1 to i. So the trip is from 1 to i. So for that trip:

Steps are:
- Elevator starts at x, moves to 1 (distance |x - 1|).
- Then moves from 1 to i (distance |i - 1|).
- Then returns to x: distance |i - x|.

So per evening trip per person, the cost is (|x - 1| + |i - 1| + |i - x|) * 1.

So combining the two trips per person:

Total per person on floor i:
= [ (|x - i| + |i-1| + |1 - x| ) + (|x - 1| + |i - 1| + |i - x| ) ] * 1.

Wait, let's compute this. Let's see:

Morning trip cost: |x - i| (elevator to i) + |i - 1| (i to 1) + |1 - x| (back to x). So sum is |x-i| + (i-1) since i is >=1 (since it's the floor number). Wait, but the problem statement says that the elevator starts at x each time. So each trip (morning and evening) is treated independently.

But wait, the first time, the elevator is at x. Then after the morning trip, it returns to x. Then in the evening trip, it starts again from x.

So for each trip (morning and evening), the elevator's path is the same as described.

So for each person on floor i:

Each day, they have two trips. Let's compute each trip's cost.

Morning trip (from i to 1):

Cost for that trip is (distance from x to i) + (distance from i to 1) + (distance from 1 back to x). So that's |x - i| + (i - 1) + (x - 1) if x >=1. Wait, but 1 is the first floor, so i could be 1. Hmm. Let's see, in the problem statement, the floors are numbered from 1 to n, right? Because the first example has a_1 as 0, which is the first floor. So yes.

So for the morning trip, the path is x → i → 1 → x. The total movement is |x-i| + |i-1| + |1 -x|.

Evening trip (from 1 to i):

Path is x → 1 → i → x. The movement is |x -1| + |1 -i| + |i -x|.

So adding both, the total per person is:

[ |x-i| + |i-1| + |1-x| + |x-1| + |i-1| + |i-x| ] 

But let's simplify this expression.

Let me expand:

|x-i| + |i-x| = 2*|x-i| (since |x-i| is the same as |i-x|).

Then |1-x| + |x-1| = 2*|x-1| (since those are the same terms).

So the total per person is:

2*|x-i| + (|i-1| * 2) + 2*|x-1| 

Wait, wait:

Wait, in the morning trip, the elevator goes from i to 1 (distance i-1 if i >=1) and from 1 to x (distance |x-1|). So for the morning trip, the total movement is |x-i| (x to i) + (i-1) (since going down to 1) + |x-1| (back to x).

Similarly, evening trip is |x-1| (x to 1) + (i-1) (since going up to i from 1) + |i-x| (back to x).

So when we sum both trips:

|x-i| + |i-1| + |x-1| (morning)
+
|x-1| + |i-1| + |i-x| (evening)
=
|x-i| + |i-x| → which is 2|x-i|
|i-1| + |i-1| → 2(i-1) (since i >=1, so |i-1|=i-1)
|x-1| + |x-1| → 2|x-1|

So total per person is 2(|x-i| + (i-1) + |x-1| )

Wait, no. Because |i-1| is (i-1) because floors are 1-based. So for each trip, the movement from i to 1 is i-1 steps (since i is higher than 1 if i>1). Wait, but if i is 1, then it's 0 steps. So for i=1, the movement from i to 1 is 0. So in that case, for a person on the first floor, their morning trip would be x to 1 (distance |x-1|), then 0 steps (since a to b is 1 to 1), then back to x (distance |1-x|). So per trip, the cost would be |x-1| + 0 + |1-x| = 2|x-1|. But for their evening trip, same as well. So for a person on floor 1, each trip (morning and evening) is 2|x-1|.

So combining both trips, a person on floor 1 would contribute 2*2|x-1| = 4|x-1|.

But for other floors (i>1), let's see:

Each trip (morning and evening) contributes:

Morning: |x-i| + (i-1) + |x-1|
Evening: |x-1| + (i-1) + |x-i|

So adding them:

Morning: (x-i is the same as |x-i|, but the sign depends on x and i) → sum is |x-i| + (i-1) + |x-1|
Evening: |x-1| + (i-1) + |x-i|

Adding both: 2|x-i| + 2(i-1) + 2|x-1|

So per person, that's 2[ |x-i| + (i-1) + |x-1| ].

So for a person on floor i, the cost is 2*( |x-i| + (i-1) + |x-1| ) * a_i (since there are a_i people on that floor).

Wait, but a_i is the number of people on floor i. So for each i, multiply by a_i.

So the total cost for all people is sum over all i from 1 to n of [ 2*( |x-i| + (i-1) + |x-1| ) * a_i ].

Wait, but perhaps there's a way to simplify this expression. Let's see.

Let me factor out the 2. So total cost is 2 * sum over i [ a_i ( |x-i| + (i-1) + |x-1| ) ]

But can I combine terms here?

Let's expand the terms inside the sum:

|x-i| + (i-1) + |x-1| = |x-i| + |x-1| + (i-1)

Hmm. So for each floor i, the expression is |x-i| + |x-1| + (i-1). And this is multiplied by a_i, then summed over all i, then multiplied by 2.

So the problem is to choose x (which floor to set as the elevator's resting position) such that this sum is minimized.

Now, the key is to compute this sum for each possible x (from 1 to n), and choose the x with the minimal sum.

But since n can be up to 100, trying all possible x values is feasible. Because for each x in 1..n, compute the sum and take the minimum.

So the approach is:

1. Iterate x from 1 to n.

2. For each x, compute the sum over all i of a_i * ( |x-i| + |x-1| + (i-1) )

3. Find the x that gives the minimal sum.

4. Multiply the minimal sum by 2, since the total cost is 2 times the sum.

Wait, yes. Because the sum inside the 2*sum(...) is the sum of [ |x-i| + |x-1| + (i-1) ] multiplied by a_i. So for each x, compute this sum, multiply by 2, and that's the total cost. We need to find the x that gives the smallest such value.

So, since n is up to 100, and for each x, we need to compute the sum over 100 terms (each floor), the total operations are 100*100 = 10,000, which is acceptable.

So the algorithm is straightforward: iterate all possible x from 1 to n, compute the sum for each, then take the minimum.

But perhaps there's a smarter way. Let's see.

Alternatively, perhaps we can find the optimal x by considering certain properties of the sum. But since n is small, perhaps it's not necessary, and brute-force is acceptable.

So let's proceed with the brute-force approach.

Now, let's look at the sample input:

Sample 1:

3

0 2 1

So the floors are 1,2,3. a_1=0, a_2=2, a_3=1.

We need to compute for x=2 (the optimal choice):

For each i:

i=1: a_i=0. So contributes 0.

i=2: a_i=2. ( |2-2| + |2-1| + (2-1) ) * 2 → (0 +1 +1) *2 = 2 *2=4. Wait, but per person, the sum is 0 (x-i) + 1 (x-1) +1 (i-1). So 0+1+1=2. Multiply by a_i (2) → 4. Then multiplied by 2 (from the 2*sum) gives 8. But in the sample explanation, the total for i=2 is 4*2 (2 people) which is 8. Then the sample output is 16. Wait, but according to our formula, the sum would be 4 (from i=2) plus 8 (from i=3) → sum is 12, multiplied by 2 gives 24. Wait, this seems conflicting.

Wait, perhaps I have a mistake in the formula.

Wait, let's re-examine the sample. In the first example, the optimal x is 2.

Each person on floor 2 (2 people) uses the elevator twice:

Morning trip: x=2. So elevator starts at 2, goes to 2 (distance 0), then to 1 (distance 1), then returns to 2 (distance 1). So total for this trip is 0+1+1=2. Then evening trip: elevator starts at 2, goes to 1 (distance 1), then to 2 (distance 1), then returns to 2 (distance 0). So each trip contributes 1+1+0=2. So per person, each trip is 2 units. So two trips per person: 4 units. Two people: 8.

The person on floor 3: morning trip. Elevator starts at 2, goes to 3 (distance 1), then to 1 (distance 2), returns to 2 (distance 1). Total 1+2+1=4. Evening trip: elevator starts at 2, goes to 1 (distance 1), then to 3 (distance 2), returns to 2 (distance 1). Total 1+2+1=4. So per person, 8. One person: 8.

Total is 8+8=16. Which matches the sample output.

But according to our formula, for x=2:

sum over i of a_i * ( |x-i| + |x-1| + (i-1) )

For i=2: |2-2|=0, |2-1|=1, (2-1)=1. Sum per i=2: 0+1+1=2. a_i=2 → 2*2=4.

For i=3: |2-3|=1, |2-1|=1, (3-1)=2. Sum per i=3: 1+1+2=4. a_i=1 → 4*1=4.

Sum is 4+4=8. Multiply by 2 → 16. Which matches the sample.

So the formula is correct. So why in my initial analysis did I think that the sum would be 12? Because perhaps I made a miscalculation. So the formula seems correct.

So the approach is correct.

Thus, the steps are:

For each x in 1..n:

Compute the sum for each floor i:

term_i = a_i * ( |x -i| + |x-1| + (i-1) )

sum all term_i for i=1 to n. Then multiply by 2 to get the total cost. Find the minimal such total cost.

So now, the code.

The code needs to read n, then the list a (which is a list of n elements, a_1 ... a_n). Then, for each x from 1 to n, compute the sum, then find the minimum sum multiplied by 2.

So code steps:

Read n.

Read list a as integers.

Initialize min_total to a large value.

For x in range 1 to n+1 (since floors are 1-based?):

sum_terms = 0

for i in 1..n:

    floor = i (since the input is given as a_1 ... a_n, which are for floors 1 to n)

    term = a[i-1] * ( abs(x - i) + abs(x-1) + (i-1) )

    sum_terms += term

total_cost = 2 * sum_terms

if total_cost < min_total:

    min_total = total_cost

At the end, output min_total.

This should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    min_total = float('inf')

    for x in range(1, n + 1):
        current_sum = 0
        for i in range(1, n + 1):
            ai = a[i - 1]
            term = ai * (abs(x - i) + abs(x - 1) + (i - 1))
            current_sum += term
        total_cost = 2 * current_sum
        if total_cost < min_total:
            min_total = total_cost

    print(min_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
1 1
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

n=2, a=[1,1].

For x=1:

sum_terms:

i=1: a[0] =1. term is 1*(0 +0 +0) → 0.

i=2: a[1]=1. term is 1*( (1-2 is -1, abs is 1) + (x-1 is 0) + (2-1=1) → 1+0+1=2. So term is 1*2=2.

sum_terms=0+2=2. total_cost=4. Which matches the sample.

Thus, the code works for the samples.

So now, the code can be written.

Now, considering the constraints. The input can be up to 100 floors. For each x (up to 100), we loop through 100 floors. 100*100=10,000 operations, which is trivial for Python even under 1 second.

In terms of memory, the code just uses O(n) space, which is acceptable.

So the code is straightforward.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
min_total = float('inf')

for x in range(1, n + 1):
    current_sum = 0
    for i in range(1, n + 1):
        ai = a[i - 1]
        term = ai * (abs(x - i) + abs(x - 1) + (i - 1))
        current_sum += term
    total_cost = 2 * current_sum
    if total_cost < min_total:
        min_total = total_cost

print(min_total)
```
