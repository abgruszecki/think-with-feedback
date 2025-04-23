<think>
Okay, let's see. The problem is about Maxim buying games in order. We need to count how many games he can buy based on the rules given.

So the input is the number of games n and the number of bills m. Then the costs of the games, and the values of the bills. The order of the bills is important because he uses them in order. For each game in order from first to nth, he takes the first bill (if any left) and checks if it's >= the game's cost. If yes, he uses that bill (so it's removed from the wallet, and the next bill becomes first), and counts the purchase. Otherwise, he leaves the bill and moves to the next game.

Our goal is to compute the total number of games he buys.

Hmm. So the approach is to iterate through each game in order, and for each, check if there's a bill left. If there is, take the first one. If the bill's value is >= game cost, increment count, and move to the next bill. Otherwise, leave the bill and proceed to next game.

So, the steps would be something like:

Initialize a pointer for the current bill (starting at 0). Then for each game in c:

- If the pointer is >= m, break (no more bills)
- Check if a[pointer] >= c[i]
  - If yes: increment count, pointer +=1
  - Else: do nothing, move to next game.

Wait, that's it? Because for each game, he can only use the first bill (current pointer) if available. If it's not enough, he skips the game, but keeps the bill for the next game.

So the algorithm is straightforward. For each game in order, check if there are bills left. If yes, check the first bill. If it's sufficient, take it, count++, and proceed. Else, leave the bill and check next game.

So in code terms:

Read n and m.

Read list c (n elements).

Read list a (m elements).

Initialize pointer = 0, count = 0.

Loop through each game in c:

    if pointer >= m: break

    if a[pointer] >= current game's cost:

        count +=1

        pointer +=1

    else:

        do nothing (pointer remains)

So after processing all games, output count.

Wait, but the problem statement says that after buying the nth game, he leaves. So even if there are bills left, he's done once all games are processed.

Yes. So this approach should work.

Testing the first example:

c = [2,4,5,2,4], a = [5,3,4,6]

pointer starts at 0.

Game 0 (cost 2): a[0] is 5 >= 2 → count 1, pointer 1.

Game 1 (4): a[1] is 3 <4 → no.

Game 2 (5): a[1] is 3 <5 → no.

Game 3 (2): a[1] is 3 >=2 → count 2, pointer 2.

Game4 (4): a[2] is4 >=4 → count3, pointer3.

So total 3, which matches the example.

Another example: when a has bills that can't even buy the first game. Like the second example, where a starts with 19 and 20. The first game is 20. 19 <20, so can't buy. Then next games are 40,50, etc., but the first bill (19) is still there, so none get bought. So output is 0.

Third example: all a's are 1000. He has 4 bills. So for each game, he uses the first bill. So count is 4 (since there are 4 bills and 6 games). So after 4 games, no bills left. The output is 4.

So the algorithm seems correct.

Now, what's the time complexity? For each of n games, we do O(1) operations. So O(n) time, which for n up to 1000 is perfectly acceptable.

Space is O(n + m), which is also acceptable.

So the code in Python would be straightforward.

Read n and m from input.

Then read the list c (n elements), and a (m elements).

Initialize pointer = 0, count =0.

Loop through each cost in c:

    if pointer >= len(a): break

    if a[pointer] >= cost:

        count +=1

        pointer +=1

    else:

        continue

At the end, print count.

Yes, that's all. So the code is simple.

Now, possible edge cases:

- All games are cheaper than the first bill. Then he buys min(n, m) games.

- All games are more expensive than their first available bill. Then count is 0.

What about if m is 0? But according to constraints, m is at least 1. So no, because m is >=1 (since 1<=n,m<=1000). So no need to handle m=0.

Another edge case: m is larger than n. Then he can buy up to n games if all a's are >= the costs.

So the code should handle all these.

So code:

Read first line as n, m.

Then read c as list of integers.

Then read a as list of integers.

pointer = 0

count =0

for cost in c:

    if pointer >= m:

        break

    if a[pointer] >= cost:

        count +=1

        pointer +=1

print(count)

Yes. That's the code.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    c = list(map(int, input_stream.readline().rstrip("\n").split()))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    pointer = 0
    count = 0

    for cost in c:
        if pointer >= m:
            break
        if a[pointer] >= cost:
            count += 1
            pointer += 1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 2
20 40 50 20 40
19 20
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    c = list(map(int, input_stream.readline().rstrip("\n").split()))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    pointer = 0
    count = 0

    for cost in c:
        if pointer >= m:
            break
        if a[pointer] >= cost:
            count += 1
            pointer += 1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 4
4 8 15 16 23 42
1000 1000 1000 1000
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

Third sample: 6 games, 4 bills. All a are 1000. So each of first 4 games: cost 4,8,15,16 → 1000 >= each. So count increases to 4. Then no more bills. So output is 4.

Yes.

So this code should be correct.
</think>

```python
n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

pointer = 0
count = 0

for cost in c:
    if pointer >= m:
        break
    if a[pointer] >= cost:
        count += 1
        pointer += 1

print(count)
```
