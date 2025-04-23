<think>
Okay, let's try to figure out this problem. So the problem is about Winnie-the-Pooh visiting his friends' houses and minimizing the total distance he travels for n meals. He starts at Rabbit's house. Each time after eating, he has to leave and go to another friend's house. The goal is to find the minimal distance after n meals.

Let me start by understanding the problem step by step. The first meal is at Rabbit's house. Then each subsequent meal requires moving to a different house. So for each meal after the first, he must choose which path to take, but he can't stay in the same house as the previous meal.

The paths are between Rabbit (R), Owl (O), and Eeyore (E). The distances between them are a (R-O), b (R-E), and c (O-E). So the three possible edges are R-O (a), R-E (b), O-E (c).

The key is to find the sequence of visits that minimizes the total distance, given that each visit must be to a different house than the previous one.

Let's think about small values of n to see a pattern.

For n=1: He stays at R. Total distance is 0. That's the second example.

For n=2: He must go from R to either O or E. Then he eats again. So the first step is to choose the minimum between a (R-O) and b (R-E). Then for the second meal, he's at O or E. But since it's the second meal (n=2), he doesn't need to move again. Wait, wait, no: the first meal is at R, then he moves to another house for the second meal. So total distance is the cost of moving once. So for n=2, the minimal distance is min(a, b).

But wait, in the first example, n=3. Let's see the example:

Input:
3
2
3
1

The steps are R → O → E. The distances are 2 (R-O) and 1 (O-E), total 3. So after three meals, the total is sum of two moves.

So for n meals, the number of moves is n-1. Because each move is between two meals. For example, 3 meals require 2 moves.

So the problem reduces to finding the minimal sum of (n-1) edges, such that consecutive edges are between different houses, and each move alternates between the possible houses.

Wait, but each move is determined by the current house and the next. For example, if he's at R, he can go to O (a) or E (b). Then from O, he can go to R (a) or E (c). But he can't stay in the same house. So each step depends on the current location.

So the problem is similar to a dynamic programming problem where the state is the current house, and the number of meals eaten so far. For each state, we track the minimal distance required to reach that state with that number of meals.

Let me model this. Let's define dp[k][current] as the minimal total distance after eating k times, ending at 'current' house. The initial state is dp[1][R] = 0, because the first meal is at R, no distance needed.

For each subsequent meal (from 2 to n), we look at the previous possible houses and compute the minimal distance. For example, to compute dp[k][O], we look at the previous possible houses which are R and E, since the previous meal must have been in a different house. Then, the distance would be the previous dp[k-1][R] + a (distance from R to O), or dp[k-1][E] + c (distance from E to O via O-E edge). Wait, but E to O is via the edge with length c, yes.

So the transitions would be:

For each k from 2 to n:
   for each current house (R, O, E):
       dp[k][current] = min over all previous houses (other than current) of (dp[k-1][prev] + distance between prev and current)

But since the first meal is at R, the initial state is only dp[1][R] = 0. The other houses (O and E) can't be the first meal.

So for k=1, dp[1][O] and dp[1][E] would be infinity or some invalid value, except for R.

Then, for each k up to n, we compute the minimal possible distances.

But since n can be up to 100, and the state is 3 houses, the DP table is manageable. For each of 100 steps, we have 3 states, so total 300 entries. Each entry requires looking at two possible previous states (since the previous house must be different from the current one). So this is feasible.

Let's model the houses as 0, 1, 2 (like R, O, E). But perhaps using letters and a dictionary would be easier, but for speed, maybe integers are better.

Wait, perhaps we can assign R=0, O=1, E=2.

The distances between houses can be represented as a matrix. For example:

distance[0][1] = a (R to O)
distance[0][2] = b (R to E)
distance[1][2] = c (O to E)
And the reverse directions would have the same distance. Like distance[1][0] = a, distance[2][0] = b, distance[2][1] = c.

So the distance matrix is symmetric.

So for any current house, the possible transitions are to the two other houses, with the corresponding distance.

So the DP transitions would be:

For each k in 2..n:
   For each current_house in 0,1,2:
       prev_houses = other two houses (not current_house)
       dp[k][current_house] = min( dp[k-1][prev1] + distance[prev1][current_house], 
                                   dp[k-1][prev2] + distance[prev2][current_house] )

But for k=1, only current_house=0 (R) is possible.

So the steps are:

Initialize dp[1][0] = 0, others (for k=1) as infinity.

Then for each step from 2 to n:

   For each possible current house, compute the minimal distance from the previous steps.

At the end, after n meals, the total distance is the minimum among dp[n][all houses], but wait no: because after the nth meal, he doesn't need to move. Wait, the problem says, he needs to have n meals, which involves (n-1) moves. Because the first meal is at R (no move), then each subsequent meal requires a move. So the transitions are correct.

Wait, the number of moves is (number of meals - 1). Because each move happens between meals.

So for the DP, the state represents the current house after k meals. The transitions are for adding a move between k-1 and k.

So the final answer is the minimal value of dp[n][*], because after the nth meal, he stops. But the moves are between the meals. So yes, the DP correctly accumulates the sum of the (n-1) moves.

So the approach is:

- Use dynamic programming where the state is (k, current_house), storing the minimal total distance.

Now, the initial state is (1, R) with 0, others (for k=1) are impossible.

Then, for each k from 2 to n:

   For each possible current_house, the previous step must have been in one of the other two houses.

   So for each current_house, look at the two possible previous_house options, take the minimal (dp_prev_prev_house + distance).

So the code structure could be:

Initialize a DP table. Since n is up to 100, and 3 houses, we can use a 2D array. Or even two 1D arrays for current and previous steps, since each step only depends on the previous step.

For example, for each step k, we can have a current DP array that depends on the previous step's array.

So, for space optimization, we can use two dictionaries or arrays: prev_dp and current_dp.

Let me outline the steps:

Read n, a, b, c.

Create a distance matrix. For example:

distance = [
    [0, a, b],
    [a, 0, c],
    [b, c, 0]
]

But since moving from house i to j is the same as j to i in terms of distance, the matrix is symmetric. So distance[i][j] is the same as distance[j][i].

Then, initialize prev_dp as {0:0, 1:infinity, 2:infinity} for k=1.

Wait, perhaps using a list where index 0 is R, 1 is O, 2 is E.

prev_dp = [0, inf, inf]  # for k=1, after first meal.

Then, for each k from 2 to n:

    current_dp = [inf, inf, inf]

    for current_house in 0,1,2:
        prev_houses = the two other houses.

        for prev_house in prev_houses:
            if prev_dp[prev_house] + distance[prev_house][current_house] < current_dp[current_house]:
                current_dp[current_house] = prev_dp[prev_house] + distance[prev_house][current_house]

    prev_dp becomes current_dp for the next iteration.

After processing all steps, the answer is the minimal value in prev_dp (since after n meals, the last step is at k=n, and the total is the sum of the moves up to that point).

Wait, but prev_dp is for k steps, which after the loop, when k reaches n, the prev_dp would hold the values for k=n.

Yes.

So the code would look something like this:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = int(input_stream.readline().rstrip("\n"))
    b = int(input_stream.readline().rstrip("\n"))
    c = int(input_stream.readline().rstrip("\n"))

    # Create the distance matrix
    distance = [
        [0, a, b],
        [a, 0, c],
        [b, c, 0]
    ]

    if n == 1:
        print(0, file=output_stream)
        return

    # Initialize for k=1
    prev_dp = [float('inf')] * 3
    prev_dp[0] = 0  # first meal is at Rabbit's house (0)

    for k in range(2, n+1):
        current_dp = [float('inf')] * 3
        for current_house in range(3):
            # Get the possible previous houses (not current_house)
            prev_houses = [h for h in range(3) if h != current_house]
            # For each possible previous house, check if we can come from there
            for prev_house in prev_houses:
                if prev_dp[prev_house] + distance[prev_house][current_house] < current_dp[current_house]:
                    current_dp[current_house] = prev_dp[prev_house] + distance[prev_house][current_house]
        prev_dp = current_dp

    # The minimal total distance is the minimal among the possible houses after n meals
    print(min(prev_dp), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
2
3
5
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

Another example: n=1. The code outputs 0, as required.

Another test case: n=2, a=2, b=3. Then the code would have k=2.

prev_dp for k=1 is [0, inf, inf].

For k=2, current_house 1 (O) is 0+2=2, current_house 2 (E) is 0+3=3. So the minimal is 2. So output is 2, which is correct.

So the code seems to handle these cases.

Now, what about when after some steps, there are multiple paths with varying costs? For example, maybe in some cases, taking a longer path first could lead to a better total.

But the DP approach takes care of that by always choosing the minimal path for each state.

In terms of code, using float('inf') to represent impossible states, but for Python, when the initial prev_dp is [0, inf, inf], and n=1, the code correctly outputs 0.

So the code seems correct.

Now, let's code this in Python, making sure to handle all edge cases.

Wait, but in the code, after the for loop from 2 to n inclusive. For n=1, the code exits early. For n=2, it runs the loop once (k=2), etc.

The code also correctly initializes the prev_dp as [0, inf, inf].

But what about when n=0? But the constraints say n ≥1, so no problem.

Another thing: the distance matrix for the same house (i.e., distance[i][i] is 0, but in the code, those are not used because when you transition, you can't come from the same house.

So the code is correct.

Now, coding this.

But wait, when building the distance matrix, the code uses:

distance = [
    [0, a, b],
    [a, 0, c],
    [b, c, 0]
]

Which is correct. Because from Rabbit (0) to Owl (1) is a, etc.

So yes.

So the code should be as follows.

Testing the second example: input 1. The code outputs 0.

Another test case: n=2, a=2, b=1. Then for the first step, k=2, the code computes current_dp[1] (O) as 0+2=2, current_dp[2] (E) as 0+1=1. So the minimal is 1, which would be the answer. So for n=2, the output is 1.

So code works.

Therefore, the code should be correct.
</think>

```python
n = int(input())
a = int(input())
b = int(input())
c = int(input())

if n == 1:
    print(0)
    exit()

distance = [
    [0, a, b],
    [a, 0, c],
    [b, c, 0]
]

prev_dp = [float('inf')] * 3
prev_dp[0] = 0  # Starting at Rabbit's house (0)

for k in range(2, n + 1):
    current_dp = [float('inf')] * 3
    for current in range(3):
        for prev in range(3):
            if prev != current and prev_dp[prev] + distance[prev][current] < current_dp[current]:
                current_dp[current] = prev_dp[prev] + distance[prev][current]
    prev_dp = current_dp

print(min(prev_dp))
```
