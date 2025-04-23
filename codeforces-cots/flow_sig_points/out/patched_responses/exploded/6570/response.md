<think>
Okay, let's see. The problem is about a line of people playing table tennis. The first two play, the loser goes to the end of the line, and the winner plays the next person. This continues until someone wins k games in a row. We have to find out which player that is. All players have distinct powers, and the higher power always wins.

Hmm. The key here is that the process will have a dominant player once the strongest player gets to the front. Because once the strongest is in play, they can't lose any game. So once that player starts a streak, they'll just keep winning until they hit k consecutive wins. So the question is, when does this happen, or maybe whether the required k is small enough that a player other than the strongest can accumulate k wins before the strongest comes into play.

Wait, but the maximum possible k is up to 1e12. So simulating each game step by step is impossible for large k. So the solution must avoid simulating every single game, especially when k is large.

So what's the pattern here? Let's think. Let's process the initial players. The first two play, the winner is the one with higher power. The loser goes to the back. Then the winner plays the next in line (third person), and so on. So the current champion stays until defeated. But since all powers are unique, the current champion is the maximum of all the players encountered so far. Because if there's a stronger player in the remaining line, when they meet, the stronger one will take over.

Wait, that's right. Because each time the current champion (current_max) is compared to the next challenger. If the challenger is stronger, they become the new current_max, and the old champion goes to the end of the line. Otherwise, the current_max remains, and the challenger goes to the end.

So the process is that the current_max will be the maximum of the players encountered so far. Once the overall maximum player (the one with the highest power in the entire list) comes into the game, they will never lose again. So once they start winning, they will accumulate wins one after another, and eventually hit k.

So the problem reduces to: before the maximum player comes into play, how many consecutive wins does each current champion have? Once the maximum player is the current champion, they will win all subsequent games. So the answer is the maximum of the entire array if k is larger than the number of games before the maximum takes over. Otherwise, it's the first player that can accumulate k consecutive wins before the maximum comes into play.

So the steps are:

1. Find the maximum element in the array. Let's call it max_player.

2. Simulate the process until either:
   a. The current champion has accumulated k consecutive wins, in which case return that champion.
   b. The current champion is the max_player, in which case return the max_player, since they will win all remaining games and eventually reach k.

But how to simulate this efficiently?

Let's think about the initial sequence. Let's process the players in the order they are played. The initial queue is the list of players. The first two play. The loser is sent to the end of the queue. The winner becomes the current champion and plays the next in the queue. Each time, the current champion (current_max) is compared with the next challenger. The winner is the higher of the two. So the current champion can accumulate consecutive wins until a higher player comes along.

Wait, but for the first steps, each time the current champion is the maximum between the previous champion and the next challenger. So the current champion is the maximum of all players that have been part of the queue up to that point.

So the process will proceed with the current champion being the maximum of the first i players, where i increases each time until all players are processed, but once the overall maximum is found, the process stops because that player will win all subsequent games.

So, the idea is: track the current champion and the current streak. For each step, compare the current champion with the next challenger. The winner is the higher of the two. If the current champion is the same as before, their streak increases by 1. If a new champion is found (higher than current), then their streak is 1 (since they just won once). Then, check if the current streak reaches k. If so, return the current champion. If not, proceed.

But when the current champion is the overall maximum (max_player), then any further games will just add to their streak. So once the max_player is the current champion, the required answer is the max_player if k is greater than the current streak. Because the streak will keep increasing by 1 each game until it reaches k. So in that case, the max_player will be the answer.

So the algorithm can be:

- Find the max_player.

- Simulate the games until either the current streak reaches k, or the current champion is the max_player.

- If during the simulation, a streak of k is achieved, return that champion.

- If the max_player becomes the current champion, then the answer is the max_player (since after that, each game adds 1 to the streak, so once their streak is >=1, and k is the target, even if k is very large, the max_player will be the answer).

So the steps in code would be:

Initialize the queue with the given players.

current_champion = first player in queue. Remove it from queue.

current_streak = 0.

Then, loop:

   next_challenger = next player in queue. Remove from queue.

   if current_champion > next_challenger:

       current_streak += 1

       queue.append(next_challenger)

   else:

       queue.append(current_champion)

       current_champion = next_challenger

       current_streak = 1

   if current_streak == k:

       return current_champion

   if current_champion == max_player:

       return max_player

But the problem here is that when the queue is large, and k is up to 1e12, this simulation is O(n) per step, which for n=500 is manageable only if the number of steps before the max_player is encountered is O(n). But in the worst case, the initial queue could be arranged such that the max_player is at the end, and we have to process all previous elements. Let's see.

Wait, the initial queue is the list a. The first two are compared, the loser goes to the end. Then the winner (the max of the first two) plays the next in the queue (third element). The winner is the max between the two. The loser goes to the end. So each step, the current champion is the maximum of all elements processed so far. Because whenever a new challenger is higher than the current champion, the challenger becomes the new champion. So the current champion is always the maximum of the first m elements, where m is increasing as we process each new element.

Therefore, the process of determining the current champion is that once we have processed the first m elements, the current champion is the maximum of the first m elements. The next step, we process the (m+1)th element. If that element is higher than the current champion, then the new champion is the maximum of the first m+1 elements, and the current streak is 1. Otherwise, the streak increases by 1.

Therefore, the current champion is the maximum of all the elements processed so far. So once all elements are processed (i.e., after n-1 steps), the current champion is the max_player. Because the max_player is somewhere in the array. So once all elements have been processed, the current champion is the max_player, and from then on, the streak increases by 1 each time.

So the simulation can stop when either:

1. The current streak reaches k.

2. The current champion is the max_player (since after that, any further games will just add to the streak, and since k can be up to 1e12, we can immediately return the max_player once he is the current champion, regardless of k).

So the steps in code would be:

Find the maximum of the array.

Initialize the queue as the array.

current_champion is the first element of the queue, then queue is the rest.

But wait, initially, the first two players play. So the first step is to compare the first two elements.

Wait, maybe the queue starts with all elements. The first two are taken out. The winner is the max of the two, becomes current champion, and the loser is added to the end. Then, the current champion plays the next element (third in the original array, but maybe others have been added to the end).

Alternatively, perhaps it's easier to represent the queue as a deque. The initial deque is the list a. Then, take the first two elements, compare them. The winner becomes the current champion, the loser is pushed to the back. Then, for each next step, the current champion plays the next element (front of the deque). So the deque starts as [a1, a2, a3, ... an]. Take a1 and a2. Compare, winner is current, loser to the back. Then, current plays the next element in deque (a3), etc.

But perhaps a better approach is to model the queue as a deque. Initially, the deque is all elements except the first two, and the current_champion is the winner of the first two. Wait, no. Let's think again.

The first two players in the line play. So for example, in the first example input:

2 2

1 2

The initial line is [1, 2]. They play. 2 wins, so 1 goes to the end. Streak is 1. Then, the next challenger is the next in line, which is 1 again. 2 wins again. Streak is 2, so return 2.

So the first two elements are the initial players. Then, the next challengers come from the deque, but after the first two, the queue is the rest of the players plus the losers.

So the initial steps:

Initialize deque as the list a.

Take the first two elements from the deque: x and y.

current_champion is max(x, y).

loser is min(x, y). Add loser to the end of the deque.

current_streak is 1.

Then, in each subsequent step:

Take the next element from the front of the deque (call it challenger).

Compare with current_champion.

If current_champion wins, streak +=1. Add challenger to the end.

Else, add current_champion to the end. current_champion becomes challenger. streak=1.

After each step, check if streak >=k. If yes, return current_champion.

Also, check if current_champion is the max_player. If so, return max_player.

So the simulation can proceed until either:

- The current streak reaches k.

- The current champion is the max_player. Because once that happens, the streak will keep increasing by 1 each game, and since the max can't lose, the answer is max_player.

So the key insight here is that once the current champion is the maximum element in the array, we can immediately return it as the answer, regardless of k. Because after that, the streak will just keep increasing by 1 each time, and since k can be up to 1e12, the answer will be the max_player.

So the steps for the algorithm are:

1. Find the maximum player in the array.

2. Initialize the deque with all elements except the first two? No. Wait, the initial deque is all elements. Then, the first step is to take the first two elements and compare them. The winner is the current champion, the loser is added to the end. Then, in subsequent steps, the deque contains the rest of the elements (if any) plus the losers.

Wait, perhaps the initial deque is the entire list. For example, in the first example, the deque starts as [1,2]. Then, the first two elements are taken (1 and 2). The winner is 2, added to the deque (current champion), and the loser 1 is added to the end. Wait, no. Wait, after the first game, the loser (1) goes to the end. So the deque after the first step is [1]. Then, the next game is between current champion (2) and the next element in the deque (1). So the deque is now empty after taking 1, but after losing, the challenger (1) is added back to the end.

Wait, perhaps the deque starts as the entire array. Then, the first two elements are popped, and processed. Then, after each game, the loser is added to the end of the deque.

But the current champion is not part of the deque. The deque is the queue of people waiting to challenge the current champion.

Wait, perhaps the deque is the queue of the remaining challengers. The current champion is separate. So, the initial steps are:

Deque starts with all players except the first two (since the first two play each other).

Wait, no. Let's think again.

The problem says: the first two players in the line play. So the line is the initial order of the players. So the initial line is [a1, a2, a3, ..., an]. The first two (a1 and a2) play. The loser goes to the end of the line (so the line becomes [a3, a4, ..., an, loser]). The winner is the current champion and plays the next person in the line (a3). So the line after the first game is [a3, a4, ..., an, loser]. Then, the current champion (winner of a1 vs a2) plays a3. The loser of this game is added to the end of the line, and so on.

So the current champion is not part of the line. The line is the queue of people waiting to challenge the current champion.

So the process is:

Line starts as [a1, a2, a3, ..., an].

Take the first two players from the line: x and y.

Compare them. Winner becomes current champion, loser is added to the end of the line.

Then, the line is [a3, a4, ..., an, loser].

Then, the current champion plays the next person in the line: take the first element (a3) from the line, compare. Winner is current champion, loser added to line. Line becomes [a4, ..., an, loser, previous loser].

And so on.

Wait, no. The line after the first game is [a3, a4, ..., an, loser], and the current champion is the winner of x and y. Then, the next step is to take the next person from the line (a3) to challenge the current champion. The loser is added to the end of the line, which then becomes [a4, ..., an, loser (from first game), loser (from second game)].

So the deque (line) contains all the players who have not yet challenged the current champion, plus those who lost and were added to the end.

So the initial deque is [a1, a2, a3, ..., an].

Then, the first two elements are popped: x = deque.popleft(), y = deque.popleft().

winner = max(x, y)

loser = min(x, y)

current_champion = winner

current_streak = 1

deque.append(loser)

Then, for each subsequent step:

if deque is not empty:

   challenger = deque.popleft()

   if current_champion > challenger:

       current_streak += 1

       deque.append(challenger)

   else:

       deque.append(current_champion)

       current_champion = challenger

       current_streak = 1

   check if current_streak >=k or current_champion is max_player: return accordingly.

But in this scenario, the deque starts as the entire array, and each step processes one challenger (the next in line). The problem is, when the current champion is the maximum, then any further challengers (from the deque) will lose, and each step increments the streak by 1. So once the current champion is the max_player, the required answer is the max_player, because even if k is 1e12, the streak will reach it.

But how many steps do we need to take before the current champion becomes the max_player? Let's see.

The current champion is always the maximum of all elements processed so far. Because whenever a new challenger is higher than the current champion, it takes over. So the current champion after m steps (excluding the initial step) is the maximum of the first m+2 elements (since the initial step processes two elements). Wait, initial step processes two elements, then each subsequent step processes one element (the next challenger). So the number of challengers processed is m steps after the initial one.

So the first two elements are processed in the initial step, then each challenger is processed one by one. So after m steps, the current champion is the maximum of the first (2 + m) elements.

But the max_player is the overall maximum, so once the process reaches the point where the current champion is the max_player (i.e., the max_player is part of the first (2 + m) elements, and all previous challengers were less than the current champion), then any further challengers will lose, and the streak will keep increasing.

Thus, once the current champion is the max_player, the answer is the max_player.

So the algorithm can be structured as follows:

Find the max_player.

Simulate the games step by step, keeping track of current_streak and current_champion.

At each step:

   check if current_streak >=k: return current_champion.

   check if current_champion is max_player: return max_player.

   process next challenger.

If the deque becomes empty, then current_champion is the max_player (since all elements have been processed), so return it.

So, the steps in code would be:

Read n and k.

Read the array a.

max_player = max(a)

If k ==0: (But according to the constraints, k >=2)

But let's proceed.

Initialize deque with all elements.

But wait, the initial step is to take the first two elements from the deque. So:

if n < 2:

   (but according to constraints, n >=2)

current_champion = max(a[0], a[1])

loser = min(a[0], a[1])

deque = deque(a[2:])

deque.append(loser)

current_streak = 1

Then, in the loop:

Check if current_streak >=k → return current_champion.

Check if current_champion == max_player → return it.

If deque is empty → return current_champion (which is max_player).

Take challenger from deque.popleft().

Compare with current_champion.

If current_champion is larger:

   current_streak +=1

   deque.append(challenger)

Else:

   deque.append(current_champion)

   current_champion = challenger

   current_streak = 1

Repeat.

But how efficient is this?

In the worst case, the deque is processed until the max_player is encountered. For example, if the array is in ascending order, then each element is processed once until the max_player (last element) is reached. So for n=500, the loop runs 498 times (since the first two elements are processed in the initial step, then 498 more challengers). Then, the current champion becomes the max_player, and the code returns it. So for any k >=1, the answer is the max_player.

But for large k (like 1e12), the code would exit as soon as the current_champion is the max_player, which happens after O(n) steps.

For cases where the current_champion reaches k before the max_player is processed, the loop exits early.

So the total time complexity is O(n), which is acceptable for n=500 and k up to 1e12.

This approach should handle all cases, including the example where the max_player is at the end of the array. Let's test against the sample inputs.

Sample Input 2:

4 2

3 1 2 4

After the first step:

initial two are 3 and 1. Winner is 3, streak 1. Deque becomes [2,4,1].

Next step:

challenger is 2. 3 wins. streak 2 → returns 3. Because 2 is added to deque, but streak is 2 which meets k=2. So output is 3. Which matches the sample.

Another sample:

Input 4:

2 1e10

2 1

Initial two are 2 and 1. Winner is 2. Streak 1. Deque is [1].

Check: current_streak (1) <k (1e10), but current_champion is 2, which is max_player. So return 2. Which matches the sample.

So the code would correctly return 2.

So the algorithm is correct.

Now, the code in Python.

But how to handle the deque? Let's implement this.

We can use a deque from collections.

First, read n and k.

Then, read the array as a list.

Find max_player.

If n == 1, but constraints say n >=2.

But code can proceed.

Then:

if n >=2:

   first two elements are a[0] and a[1].

   current_champion = max(a[0], a[1])

   loser = min(a[0], a[1])

   from the remaining elements (a[2:]), create the deque.

   then append the loser.

   current_streak =1.

But wait, the initial deque after the first step is a[2:] plus the loser.

So:

Testing against sample input 1.

```python
from collections import deque
import sys


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))
    max_p = max(a)
    
    if n == 1:
        print(a[0], file=output_stream)
        return
    
    x, y = a[0], a[1]
    current = max(x, y)
    loser = min(x, y)
    q = deque(a[2:])
    q.append(loser)
    streak = 1
    
    while True:
        if streak >= k:
            print(current, file=output_stream)
            return
        if current == max_p:
            print(max_p, file=output_stream)
            return
        if not q:
            print(current, file=output_stream)
            return
        challenger = q.popleft()
        if current > challenger:
            streak += 1
            q.append(challenger)
        else:
            q.append(current)
            current = challenger
            streak = 1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 2
3 1 2 4
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

Testing against sample input 2.

```python
from collections import deque
import sys


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())
    a = list(map(int, input_stream.readline().split()))
    max_p = max(a)
    
    if n == 1:
        print(a[0], file=output_stream)
        return
    
    x, y = a[0], a[1]
    current = max(x, y)
    loser = min(x, y)
    q = deque(a[2:])
    q.append(loser)
    streak = 1
    
    while True:
        if streak >= k:
            print(current, file=output_stream)
            return
        if current == max_p:
            print(max_p, file=output_stream)
            return
        if not q:
            print(current, file=output_stream)
            return
        challenger = q.popleft()
        if current > challenger:
            streak += 1
            q.append(challenger)
        else:
            q.append(current)
            current = challenger
            streak = 1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 2
6 5 3 1 2 4
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

Sample input 4:

2 1e10

2 1.

current_champion is 2. streak 1. Check if streak >=1e10 → no. But current_champion is max_p. So output 2. Correct.

Another test case: n=3, a = [3, 2, 1]. k=2.

Initial step: compare 3 and 2. current champion 3, streak 1. q is [1, 2].

Loop:

current_streak 1 <2.

current champion is not max_p (max_p is 3). So continue.

challenger is 1. 3>1 → streak 2. q becomes [2,1]. Check streak >=2 → yes. Output 3.

But according to the code, current_champion is 3, which is max_p. So when processing the first iteration:

current_streak is 1. So check current_streak >=k (no). Then check current_champion == max_p (3 ==3 → yes). So code returns 3, even though the streak is 1. But since k=2, the code should return 3, because after one more game (challenger 2), the streak becomes 2. But according to the code's logic, once current_champion is max_p, the code returns it. So the code is correct.

But in this case, the code returns 3 even if the current streak is 1 and k is 2. But since the current champion is max_p, he will win all future games. So even if k is 2, the code returns the max_p, but the streak is 1. Because the next game would make it 2.

But according to the code's logic, that's correct. Because the code can't afford to simulate up to k steps when k is large, but once the max_p is current champion, the answer is always him. So the code is correct.

Thus, the code should handle all cases correctly.
</think>

```python
from collections import deque
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    max_p = max(a)
    
    if n == 1:
        print(a[0])
        return
    
    x, y = a[0], a[1]
    current = max(x, y)
    loser = min(x, y)
    q = deque(a[2:])
    q.append(loser)
    streak = 1
    
    while True:
        if streak >= k:
            print(current)
            return
        if current == max_p:
            print(max_p)
            return
        if not q:
            print(current)
            return
        challenger = q.popleft()
        if current > challenger:
            streak += 1
            q.append(challenger)
        else:
            q.append(current)
            current = challenger
            streak = 1

if __name__ == "__main__":
    main()
```
