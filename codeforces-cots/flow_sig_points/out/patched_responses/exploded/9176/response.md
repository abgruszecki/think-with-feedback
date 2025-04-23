<think>
Okay, I need to solve this problem where I have to find the minimal number of rotations needed to type a given string using the embosser wheel. Let's see. The wheel is arranged like the lowercase letters in a circle. The pointer starts at 'a'. Each time, to type a character, you have to move the wheel so the pointer points to that character, then press the button. The question is, what's the minimal steps needed for the entire string.

Hmm, so each character in the string must be processed in order. For each consecutive pair of characters, I need to compute the minimal steps from the current character to the next one. Because each step is a rotation either clockwise or counter-clockwise. Oh right, the wheel can rotate either direction each step. So for two consecutive characters, the steps needed is the minimal between moving clockwise or counter-clockwise.

Wait, how is the wheel arranged? The problem says that the letters are arranged in a circle. The initial position is 'a'. So the order is 'a', then maybe 'b', 'c', ..., 'z', but arranged in a circle. So the letters are in a circle of 26 letters, each adjacent to the next and previous. So from 'a', moving one step clockwise would go to 'b', and one step counter-clockwise would go to 'z'.

Wait, no. Wait, when you rotate clockwise, does the wheel turn so that the next character comes under the pointer? Or does the pointer move? Let me think. For example, if the current character is 'a', rotating clockwise once would bring the wheel so that the pointer now points to 'z'? Or 'b'? Because the problem says that the initial position is 'a', and in the first example, moving from 'a' to 'z' is 1 rotation counterclockwise. So that suggests that rotating counterclockwise once from 'a' brings you to 'z'. So, perhaps the wheel is arranged in the order a, b, c, ..., z, and arranged in a circle. So moving clockwise would go from a to b, then to c, ..., z, then back to a. Counter-clockwise would go from a to z, then y, etc.

Wait, but the first example input is 'zeus'. The steps are:

a → z (1 counter-clockwise rotation, which is 1 step). Then z → e (5 steps clockwise). Let's check: z to e via clockwise. So from z, moving clockwise: next is a, then b, c, d, e. That's 5 steps. So yes. So the clockwise direction is moving forward in the alphabet (a to b, etc.), and counter-clockwise is backward.

Wait, but how many steps between z and e when moving clockwise? Let's see. Starting at z, each step clockwise would be a, then b, then c, d, e. So that's 5 steps. So yes. So the clockwise steps between two characters is (target - current) mod 26, but if you can go the other way for a shorter path.

Wait, the minimal steps between two characters is the minimal of two options: moving clockwise steps or counter-clockwise steps. For example, between 'a' and 'z', the clockwise steps would be 25 (since you go through all letters except z), but counter-clockwise is 1 step. So minimal is 1. So for each consecutive pair, we need to compute the minimal steps between them.

So the approach is:

- Start at 'a' (the initial position). Then for each character in the input string, compute the steps needed from the previous character (starting with 'a' for the first character) to the current character. Sum all those steps.

Wait, no. Wait, the initial position is 'a'. The first character is the first character of the input. So for the first character, steps are from 'a' to that character. Then, each subsequent character, steps are from the previous character (in the input string) to the next one. Because after typing the first character, the wheel is left pointing at that character. So each step between consecutive characters in the input contributes to the total.

So for example, input 'zeus' is processed as:

- a → z: steps = 1 (counter-clockwise)
- z → e: steps = min(5 (clockwise) or 21 (counter-clockwise)) → 5
- e → u: steps. Let's see. e to u. Let's calculate the clockwise and counter steps.

In clockwise direction: the letters after e are f, g, ..., u. How many steps? u is the 20th letter (a=0, e=4, u=20). So from e (4) to u (20) clockwise steps: 20 -4 =16 steps? Wait no, 20-4=16. But if you move clockwise, you add steps. Wait, the total number of steps between two letters is the minimal between (target - current) mod 26 and (current - target) mod 26. Wait, no. For example, from e to u:

Clockwise: u is higher in the order. So steps is (u - e) steps. But if that's more than 13, then counter-clockwise would be shorter.

Alternatively, the minimal steps between two letters is the minimal of (distance clockwise) and (distance counter-clockwise). For example, e is 4, u is 20. So clockwise steps: 20 -4 =16. Counter-clockwise steps: 4 + (26-20) = 10 (since from e, moving counter-clockwise steps would go e → d → ... → a → z → ... → u). So 4 steps down to a (from e: 4 steps?), then a to u is 26-20=6 steps? Wait, maybe I need to compute the clockwise and counter distances correctly.

Wait, the total number of letters is 26. The minimal steps between two letters is the minimal of (target - current) mod 26, or (current - target) mod 26, but only considering the minimal of the two. Wait, no. For example, between a (0) and z (25):

Clockwise steps would be 25 steps (a to z via clockwise). Counter-clockwise is 1 step (a to z directly via counter). So minimal is 1.

Another example: from e (4) to u (20). Clockwise steps: 20-4 =16. Counter steps: 4 -20 = -16 mod 26 → 10? Wait, maybe I should compute the clockwise and counter-clockwise steps as follows:

The clockwise steps from current to target is (target - current) if target >= current, else (26 - (current - target)). Wait, no. Let me think: moving clockwise from current to target, the steps required is (target - current) mod 26. But if that's more than 13, then moving counter-clockwise would be shorter. Because the maximum steps for the minimal path is 13. For example, between any two letters, the minimal steps is at most 13.

So for any two letters, the minimal steps between them is the minimal of ( (target - current) % 26, (current - target) % 26 ). But wait, (target - current) mod 26 gives the clockwise steps. But if that's more than 13, then the counter-clockwise steps would be 26 - (target - current) mod 26. Wait, maybe it's better to compute the clockwise steps as (target - current) % 26. Then the counter-clockwise steps is (current - target) % 26. Then the minimal of those two is the minimal steps. Wait, no. Because, for example, if current is a (0) and target is z (25), then clockwise steps would be 25, counter-clockwise steps would be 1. So the minimal is 1. So the minimal steps between current and target is the minimal of ( (target - current) % 26, (current - target) % 26 ), and then taking the minimum of those two. Wait, but (current - target) mod 26 is (26 - (target - current) ) mod 26. So perhaps a better way is to compute the absolute difference between the two letters, then take the minimal between that and 26 - that difference. Because moving clockwise that many steps, or counter-clockwise (26 - that) steps, whichever is smaller.

Yes. So for any two letters, the steps is the minimal between the clockwise steps and the counter-clockwise steps. To compute this:

Calculate the absolute difference between the two letters. Let delta = abs(current - target). Then the minimal steps is min(delta, 26 - delta).

So for example, current is e (4), target is u (20). delta = 16. So 26 - delta is 10. So minimal steps is 10. Which is why in the first example, moving from e to u is 10 steps counter-clockwise.

So the approach is:

- Convert each character to its position (a=0, b=1, ..., z=25).

- Start at position 0 (a).

- For each character in the input string, compute the current position and the next character's position. Then compute the minimal steps between current and next, add to the total.

- Update the current position to the next character's position.

So the steps would be:

Initialize total_steps = 0.

current_pos = 0 (a).

for each char in the input string:

    target_pos = ord(char) - ord('a')

    delta = abs(current_pos - target_pos)

    steps = min(delta, 26 - delta)

    total_steps += steps

    current_pos = target_pos

return total_steps

Yes, that seems right.

Testing the first example:

Input: 'zeus'

Characters: z, e, u, s.

Convert to positions: z is 25, e is 4, u is 20, s is 18.

Processing:

Start at 0.

First step: 0 → 25.

delta = 25. min(25, 1) → 1. So total_steps +=1. Now current_pos is 25.

Second step: 25 →4.

delta = 21. min(21, 5) →5. So total +=5 (total is 6). current_pos is 4.

Third step:4 →20.

delta is 16. min(16, 10) →10. total is 16. current_pos is20.

Fourth step:20 →18.

delta is2. min(2,24) →2. total becomes 18. current_pos 18.

So total is 1+5+10+2=18. Which matches the first example.

Second example: 'map' → output 35.

Let's see. The input is m, a, p.

Positions: m is 12, a is0, p is15.

Processing:

Start at 0 (a).

First step:0 →12.

delta is12. min(12,14) →12. total +=12. current_pos 12.

Second step:12 →0. delta is12. min(12,14) →12. total 24. current_pos 0.

Third step:0→15. delta 15. min(15, 11) →11. total 24+11=35. Which matches the example.

Third example: 'ares' → output 34.

Input: a, r, e, s.

Positions: a(0), r(17), e(4), s(18).

Processing:

Start at 0.

First step:0→0. delta 0. steps 0. total 0. current remains 0.

Wait, wait. The first character is 'a'? Then the first step is 0 steps. Then next is r (17). So steps between 0 and 17: delta is17. min(17,9) →9. Then total becomes 9. Then r to e (17→4). delta is13. min(13, 13) →13. So total 22. Then e to s (4→18). delta 14. min(14, 12) →12. total 22+13+12=47? Wait the sample output is 34. Hmm, wait maybe I made a mistake here.

Wait, let's see the third example input: 'ares'. The expected output is34.

Wait, let's compute step by step.

First character is 'a'. So initial position is 0. Moving from 0 to 'a' (0) is 0 steps. So total steps is 0. Next character is 'r' (17). From 0 to17. delta is17. min(17, 9) →9. So total is 9. Then next character is 'e' (4). From 17 to4. delta is13. min(13, 13) →13. total 22. Then next character is 's' (18). From4 to18: delta is14. min(14, 12) →12. total becomes 22+13=35, then add 12 →47. But the sample output is34. Hmm, this suggests that my approach is incorrect. Wait, but the sample says the output is34. So where is the mistake here?

Wait, the input is 'ares'? Let me check the sample input again.

Third example:

Input:

ares

Output:

34.

Hmm, according to the sample explanation:

Wait, maybe I'm misunderstanding the input. Wait the sample input says:

Sample Input 3:

ares

Sample Output:

34.

So according to my calculation, my approach would sum to 0 +9 (a to r) +13 (r to e) +14 (e to s) → but wait, e is4, s is18. Delta is14. 14 vs 12. So steps is 14? Or 12?

Wait wait, from 4 to18. 4 is current_pos. target is18.

delta = 18-4=14. So min(14, 26-14=12) →12. So steps would be 12. So 9+13+12=34. Oh right! I made a mistake earlier. Let's re-calculate:

First step: 0 →0 →0 steps. Then 0 →17: steps 9. Then 17 →4: steps 13. Then 4 →18: delta is 14. 26-14=12. So steps is 12. Total is 9 +13 +12 = 34. Yes. So why earlier calculation? Oh I think I made a mistake in the steps. So the steps for ares are:

a → r: 0 →17. steps 9.

r → e:17 →4. delta is13 (17-4=13). So steps min(13,13) →13.

e →s:4 →18. delta is18-4=14. So min(14,12) →12.

So sum is 9+13+12=34. Which matches the sample.

So my approach is correct.

So the algorithm is to process each character in order, compute the minimal steps between current and next, and sum.

So the code can be written as follows.

In Python:

Read the input string. Iterate through each character. Keep track of the current position (starting at 0). For each character, convert to its position (ord(c) - ord('a')), compute delta, add the minimal steps, update current position.

So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    total =0

    current =0

    for c in s:

        target = ord(c) - ord('a')

        delta = abs(current - target)

        add = min(delta, 26 - delta)

        total += add

        current = target

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
map
""",
            "output": \
"""\
35
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

So this code should handle all cases correctly. The code is O(n) time, where n is the length of the string. Since the maximum input is 100 characters, this is trivial for the time constraints. Memory usage is O(1) variables. So it's optimal.

Therefore, the code should work.
</think>

```python
s = input().strip()
total = 0
current = 0
for c in s:
    target = ord(c) - ord('a')
    delta = abs(current - target)
    total += min(delta, 26 - delta)
    current = target
print(total)
```
