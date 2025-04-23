<think>
Okay, let's tackle this problem. Hmm. So the problem is about a card game between two soldiers. The game continues in rounds where each round they take the top card of their stacks. The one with the higher card value wins the fight and puts both cards to the bottom of their stack, first the opponent's card then their own. We need to find out how many fights happen before someone's stack is empty, or output -1 if it loops forever.

The constraints are interesting. Wait, n can be up to 10. Oh right, but even with n=10, the possible states of the game could be large. Because each player's stack can be a permutation of their current cards. Wait, but how many unique states can there be? For example, each state is defined by the two players' stacks. Since all cards are unique, the total possible distinct states would be the number of possible subsets for each player's stack, but considering the order. For n=10, each possible division of the 10 unique cards into two ordered sequences. But even that number is quite high. For example, for each possible partition of the cards between the two players, the number is (sum_{k1=1 to 9} C(10, k1) * k1! * (10 - k1)! )) ). But even that sum is 10! * sum_{k1=1 to9} 1/(k1! (10 -k1)! )) * k1! (10 -k1)! ) ) which simplifies to 10! * sum_{k1=1 to9} 1) ) which is 9*10! (since sum from 1 to9 is 9 terms). But 10! is 3.6 million, multiplied by 9 gives around 32 million. But that's a lot. However, the time limit is 2 seconds. So simulating until a state repeats could be feasible if the number of steps isn't too high. But how?

Wait, but in the worst case, the game could loop infinitely. So the simulation needs to track all previously seen states. If during the simulation, a state repeats, then we can conclude that it's an infinite loop and return -1. Otherwise, if a player's stack becomes empty, return the count and the winner.

So the approach is: simulate each fight step by step, and track the states we've seen before. For each step, check if the current state (the sequences of both players' stacks) has been seen before. If yes, return -1. Otherwise, add the state to the seen set. Continue until one of the stacks is empty.

Now, the challenge is representing the states efficiently. Because for n=10, each player's stack can be represented as a tuple. For example, the first player's stack is a tuple, and the second's is another tuple. So the combined state is a pair of tuples. We can store these in a set to check for duplicates.

But even with n=10, the maximum number of steps could be high. Wait, but given that the number of possible unique states is up to 9 * 10! = 32,659,200 (if n=10), and each step is O(1) operations (since each fight processes two cards), maybe even for n=10, the simulation would run within time. Because even if we have to loop through 10 million steps, each step involves checking a hash set, which is O(1) average time. Python's dictionaries and sets can handle that if optimized properly.

So the plan is:

1. Read the initial stacks for both players. Let's call them s1 and s2.

2. Initialize a set to keep track of all previously seen states (s1, s2).

3. Initialize a fight count to 0.

4. Loop:

   a. Check if either s1 or s2 is empty. If yes, return the count and the winner.

   b. Check if the current state (tuple(s1), tuple(s2)) is in the seen set. If yes, return -1.

   c. Add the current state to the seen set.

   d. Each player takes their top card (a = s1[0], b = s2[0]). Remove them from the stacks.

   e. Compare a and b. The higher card wins.

   f. The winner takes both cards, first the opponent's card (b if the winner is 1, a if the winner is 2) then their own card (a for 1, b for 2) and appends them to the bottom of their stack.

   g. Increment the fight count by 1.

   h. Repeat the loop.

But wait, how to manage the stacks? Because each time we need to take the top card (i.e., the first element in the list), and then add the two cards to the end of the winner's list.

In Python, using lists for s1 and s2, popping from the front (using pop(0)) would be O(k) time each time, which for k up to 10 is manageable, but with many iterations, could it be a problem? For example, in the worst case where each fight adds two cards to the winner's stack. But in practice, since each fight removes two cards and adds two to the winner's stack, the total number of elements in each stack remains the same. Wait, no: the total number of cards is n. Each fight moves two cards from the two stacks to the winner's stack, but the total remains n. So the size of each stack can vary, but the sum is always n.

But for n=10, even with O(k) operations for each fight, since each fight is O(k) for each stack, but for k up to 10, each fight's processing is O(1) per element. So for n=10, each fight's processing is O(1) time. So even with millions of steps, it's manageable.

But in Python, popping from the front of a list is O(k) time. For example, if s1 is a list of 10 elements, popping the first element takes O(10) time. But for n=10, and say 1e6 steps, that's 1e6 * 10 operations, which is 1e7 operations. Python can handle that, but perhaps using deque would be more efficient. Because deque's popleft is O(1) time.

Ah right. So for better performance, we should represent s1 and s2 as deque (double-ended queue) from the collections module. Then, popping from the front is O(1), and appending to the end is O(1). So that's better.

So modifying the approach:

- Use deque for s1 and s2.

So in code:

from collections import deque

Read the initial s1 and s2 as deques.

Then, for each step:

a = s1.popleft()

b = s2.popleft()

Compare a and b.

If a > b: then s1.append(b), s1.append(a)

else: s2.append(a), s2.append(b)

Each step's deque operations are O(1) time.

Yes, this will be much more efficient.

Now, the main steps are:

- Keep track of the state (s1 and s2) as tuples, since deques are not hashable. So for each state, we can convert the deque into a tuple and store that in the seen set.

But for each step, converting deques to tuples can take O(k) time, where k is the size of the deque. For n=10, each deque can have up to 10 elements, so converting to a tuple would take O(10) time per step, which is manageable.

So in code, for each step after popping the two cards, but before processing the fight, the current state is the current s1 and s2. Wait no: the popped cards are removed from the deques. So after popping, the deques are the current state minus the two top cards. But then the fight happens, and the winner appends the two cards. So the state after processing the fight is the new state. But wait, the fight is part of the step. So the steps are:

At the start of the loop:

Check if s1 or s2 is empty. If yes, return.

Check if the current state (s1, s2) is in seen. If yes, return -1.

Add the current state to seen.

Then process the fight.

So the code:

seen = set()

while True:

    if not s1 or not s2:

        print(fight_count, 1 if s2 else 2)

        return

    state = (tuple(s1), tuple(s2))

    if state in seen:

        print(-1)

        return

    seen.add(state)

    # process the fight

    a = s1.popleft()

    b = s2.popleft()

    if a > b:

        s1.append(b)

        s1.append(a)

    else:

        s2.append(a)

        s2.append(b)

    fight_count += 1

Wait, but in the state, after popping the two cards and processing the fight, the deques are modified. Wait, no: the state is captured before processing the fight. Because the fight is part of the next step. For example, the state before processing the fight is the current state. Then, after processing the fight, the deques are modified. So in the next iteration, the new state is the modified deques. So the code correctly captures the state before the fight is processed.

Yes. Because the state is stored before the fight is processed, and then the fight modifies the deques. So the next iteration will check the new state.

So the code as above should correctly track the states.

Now, the test cases.

First sample input:

4

2 1 3

2 4 2

So initial s1 is deque([1,3]), s2 is deque([4,2]).

First fight:

a=1, b=4. 1 <4, so s2 appends 1 and 4. s2 becomes [2, 1,4].

Fight count 1.

Second fight:

s1 is [3], s2 is [2,1,4]. Fight: 3 vs 2. 3>2. So s1 appends 2,3. s1 is [3,2,3]? Wait no. Wait, after the fight, s1's deque after popping 3, and s2's deque after popping 2. Then, since 3>2, s1 appends 2 first, then 3. So after this fight, s1 is [3]. Then, after appending, s1 becomes [3]. Wait, no: s1 was [3] before the fight. Then we pop 3 (a=3), s2 pops 2 (b=2). a> b, so s1 appends 2 and then 3. So s1's deque is now empty after popping, then appends 2 and 3. So after this fight, s1 is deque([2,3]). s2 is deque([1,4]).

Fight count increments to 2.

Then the next state is ( [2,3], [1,4] )

And the loop continues. After 6 fights, according to the sample, s2 wins.

So the code should capture that.

The second sample input is:

3

1 2

2 1 3

So initial s1 is deque([2]), s2 is deque([1,3]).

Fight 1: 2 vs 1. 2>1. So s1 appends 1 and 2. s1 becomes [1,2]. s2 becomes [3].

Fight 2: s1 is [1,2], s2 is [3]. 1 vs3. 3 wins. s2 appends 1,3. s2 becomes [3,1,3]? Wait:

Wait, after the fight: a=1, b=3. So s2 appends 1 and then 3. So s2 becomes deque([3,1,3]? No, original s2 after popping 3. Wait initial s2 after first fight is deque([3])? Wait the initial s2 is deque([1,3]). First fight: a=2, b=1 (from s2's first card). Then s1 appends 1 and 2. So s1 becomes [1,2], and s2 becomes deque([3]).

So second fight: s1 is [1,2], s2 is [3]. a=1, b=3. 3 wins. So s2 appends 1, then 3. So s2 becomes deque([3,1,3]? No, wait, the original s2 deque was [3]. After popping 3, then appending 1 and 3. So s2 becomes deque([1,3]). Then fight count is 2.

Then third fight: s1 is [2], s2 is [1,3]. a=2 vs b=1. 2>1. s1 appends 1 and 2. s1 becomes [1,2]. s2 becomes [3].

This looks like a cycle between states. After fight 2, the state is s1 = [1,2], s2 = [3]. Then fight 3: s1 is [2], s2 is [3]. Fight 3: 2 vs3 → 3 wins. s2 appends 2 and3. s2 becomes [3,2,3]. Fight count is 3. Then s1 is empty after that fight? No, after popping 2 from s1 (which was [2]), s1 becomes empty. Then in the next loop iteration, the code checks if s1 is empty. So fight count increments to 3. Then the code checks if s1 is empty (yes) → outputs 3 and the winner is 2. But according to the sample, this input outputs -1. Wait, but in the sample input 2, the output is -1. Hmm, that's conflicting with the example.

Wait wait, sample input 2:

3

1 2

2 1 3

So initial s1 is [2], s2 is [1,3]. Let's walk through the steps.

Fight 1: a=2 (s1), b=1 (s2). 2>1. So s1 appends 1, then 2. So s1 becomes [1,2]. s2 becomes [3]. Fight count 1.

Check the next state: s1 is [1,2], s2 is [3]. Check if this state is in seen. Let's track the seen set.

Initial state: ( (2), (1,3) ) → added to seen before fight 1.

After fight 1, the new state is ( [1,2], [3] ). So next iteration:

Check if s1 or s2 is empty: no. Check if the state ( (1,2), (3) ) is in seen. Not yet. Add it.

Fight 2: a=1 (s1), b=3 (s2). 3>1. s2 appends 1, then 3. So s2 becomes [3,1,3]? Wait no: original s2 was [3]. After popping 3, s2 is empty. Then append 1 and 3. So s2 becomes deque([1,3]). So after fight 2, s1 is [2], s2 is [1,3]. Fight count is 2.

Check new state: ( [2], [1,3] ). Which is the same as the initial state. So when this state is checked again, it's already in the seen set. So the code would output -1. But according to the sample input 2, the output is -1.

So in this case, after fight 2, the state returns to the initial state, causing a loop.

Wait let's see:

After fight 1: state is ( (1,2), (3) )

After adding that to seen.

Fight 2: a=1 and b=3. s2 wins. So s2 appends 1 and 3. So s2's deque becomes [3, 1, 3]? No. Wait, after popping 3 from s2 (which was deque([3])), s2 becomes empty. Then the winner appends first the opponent's card (1) and then their own (3). So s2 becomes [1,3]. So fight 2 ends with s1 as [2] (since s1 was [1,2], popped 1, now has [2] left), and s2 is deque([1,3]).

So the new state is ( [2], [1,3] ), which is the initial state. So when we check if this state is in the seen set, which was added before fight 1. So in the next loop iteration:

After fight 2, the fight count is 2. Then, the code loops again:

Check if s1 or s2 is empty: no.

Check state ( [2], [1,3] ) is in seen (yes). So output -1.

So the code would correctly output -1, as in sample 2.

So the code logic is correct.

Now, the code needs to:

- Read the input correctly.

For example, the first line is n.

Second line: k1 followed by k1 integers.

Third line: k2 followed by k2 integers.

So in code:

n = int(input())

k1, *rest = list(map(int, input().split()))
s1 = deque(rest)

k2, *rest = list(map(int, input().split()))
s2 = deque(rest)

Wait, no. Wait, the second line is k1 followed by k1 integers. So the split would give k1 as the first element, then the rest. So for example, in sample 1, the second line is "2 1 3". So k1 is 2, rest is [1,3]. So s1 is deque([1,3]).

Yes.

So code:

from collections import deque

n = int(input())

s1 = deque()
s2 = deque()

# Read s1's cards
parts = list(map(int, input().split()))
k1 = parts[0]
s1 = deque(parts[1:])

parts = list(map(int, input().split()))
k2 = parts[0]
s2 = deque(parts[1:])

Then, simulate.

Implement the loop as discussed.

Now, in Python, tuples of deques (converted to tuples) are stored in the seen set. So for each iteration, the current state is tuple(s1), tuple(s2). So for example, s1 is deque([1,3]), then tuple(s1) is (1,3).

So the code:

seen = set()

fight_count = 0

while True:

    if not s1:

        print(fight_count, 2)

        exit()

    if not s2:

        print(fight_count, 1)

        exit()

    # Check for cycle

    state = (tuple(s1), tuple(s2))

    if state in seen:

        print(-1)

        exit()

    seen.add(state)

    # Get top cards

    a = s1.popleft()

    b = s2.popleft()

    # Compare and append

    if a > b:

        s1.append(b)

        s1.append(a)

    else:

        s2.append(a)

        s2.append(b)

    fight_count +=1

Wait, but what about the case where the fight count exceeds a very large number? But according to the problem statement, we have to detect cycles. So as long as we track the states properly, the code will either exit when a player wins or when a cycle is detected.

This code should handle all cases.

Testing against sample input 1.

```python
from collections import deque


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s1 = deque(map(int, input_stream.readline().rstrip("\n").split()[1:]))
    s2 = deque(map(int, input_stream.readline().rstrip("\n").split()[1:]))

    seen = set()
    fight_count = 0

    while True:
        if not s1:
            print(fight_count, 2, file=output_stream)
            break
        if not s2:
            print(fight_count, 1, file=output_stream)
            break
        
        state = (tuple(s1), tuple(s2))
        if state in seen:
            print(-1, file=output_stream)
            break
        seen.add(state)
        
        a = s1.popleft()
        b = s2.popleft()
        
        if a > b:
            s1.append(b)
            s1.append(a)
        else:
            s2.append(a)
            s2.append(b)
        
        fight_count += 1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 2
2 1 3
""",
            "output": \
"""\
-1
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

</think>

```python
from collections import deque

n = int(input())
s1 = deque(map(int, input().split()[1:]))
s2 = deque(map(int, input().split()[1:]))

seen = set()
fight_count = 0

while True:
    if not s1:
        print(fight_count, 2)
        break
    if not s2:
        print(fight_count, 1)
        break
    
    state = (tuple(s1), tuple(s2))
    if state in seen:
        print(-1)
        break
    seen.add(state)
    
    a = s1.popleft()
    b = s2.popleft()
    
    if a > b:
        s1.append(b)
        s1.append(a)
    else:
        s2.append(a)
        s2.append(b)
    
    fight_count += 1
```
