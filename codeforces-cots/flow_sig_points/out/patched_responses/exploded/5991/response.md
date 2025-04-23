<think>
Okay, let's tackle this problem. Hmm, the problem is about football teams and their kits. Each team plays home and away games. The home team uses their home kit, and the away team uses their away kit. But if the home kit colors clash (i.e., the away team's away kit is the same as the home team's home kit), then the away team switches to their home kit instead. We need to calculate for each team how many times they play in home and away kits overall.

Wait, let's break it down. For each game between two teams A (home) and B (away), the setup is:

- A wears home kit (color x_A)
- B normally wears away kit (y_B), but if y_B == x_A, then B has to wear their home kit (x_B) instead.

So for each team, their home kit usage includes all their home games (each team plays (n-1) home games, since they play against every other team once at home), plus any away games where their away kit's color clashes with the home team's home color, forcing them to switch to home kit.

So for each team i, their home appearances are:

home_games = (n-1) games (since they are the home team in each of those)
plus for every away game they play where the home team's home color is equal to their away color (y_i). Because in that case, they have to switch to their home kit.

The away appearances are the remaining games. Each team plays (n-1) away games (since they are the away team in each of those), but subtract the number of times they had to switch to home kit. So away_usage = (n-1) - clashes (where clashes is the number of times y_i == x_j for some j where j is the home team and i is away).

So the total home_usage for team i is (n-1) + count of x_j == y_i for all j.

Wait, because when team i is the away team in a game against j (so j is the home team), and j's home color x_j is equal to team i's away color y_i, then team i must switch to their home kit. So for each j, if x_j == y_i, that contributes to team i's home_usage.

So for each team i, the count is the number of j where x_j == y_i. Let's call this cnt_i. So home_usage_i = (n-1) + cnt_i.

And the away_usage_i is the number of times they wore their away kit. Normally, when they are away, it's (n-1) games. But when they had to switch, they used home kit. So the away_usage is (n-1) - cnt_i (since those cnt_i cases are now part of home_usage). But wait, no: when team i is away, they play (n-1) games (since they play each other team once away). In each of these (n-1) games, if the home team's x_j is equal to y_i, then they wear their home kit. So the away_usage for away games is (n-1) - cnt_i (since those cnt_i games are now in home_usage). But also, when team i is home, they wear home kit in all (n-1) games. So the total home_usage is (n-1) + cnt_i. The away_usage is (the number of times they are away and don't have to switch) plus the number of times they are home and wear away kit? Wait, no. Wait, the away_usage is only when they are away and their away kit is used. Which is (n-1) - cnt_i. So the total away_usage is (n-1) - cnt_i.

Wait, the problem states that each team plays exactly one home and one away game with each other team. So each team plays (n-1) home games (against each other team once at home) and (n-1) away games (against each other team once away). So for each team, in their home games, they wear home kit. So that's (n-1) home kit uses. For their away games, they normally wear away kit, but in cnt_i cases (where x_j of the home team j equals y_i), they have to wear home kit. So in their away games, the number of times they wear home kit is cnt_i, and the number of times they wear away kit is (n-1) - cnt_i.

Therefore, the total home_usage is (n-1) (home games) + cnt_i (away games where they had to switch). The total away_usage is (n-1) - cnt_i (away games where they didn't switch).

So the answer for each team i is:

home = (n-1) + cnt_i
away = (n-1) - cnt_i

So the problem reduces to, for each team i, count how many teams j have x_j equal to y_i.

The key here is to compute for each color c, how many times x_j is equal to c across all teams j. Then for each team i, cnt_i is the frequency of y_i in the x_j's.

So the approach is:

1. Create a frequency map (like a dictionary) that counts the number of times each color appears as x_j (home color) across all teams.
2. For each team i, cnt_i is the frequency of y_i (their away color) in this map.
3. Then, compute home = (n-1) + cnt_i and away = (n-1) - cnt_i for each team.

This seems straightforward, and the time complexity would be O(n), which is acceptable for n up to 1e5.

So the steps in code:

- Read n.
- Read each team's x and y, store them in a list.
- Create a frequency dictionary (could use a Counter) that counts the occurrences of x in all teams.
- For each team in the list, compute cnt as freq[y], then calculate home and away as (n-1 + cnt) and (n-1 - cnt), then output those two numbers.

Wait, let's test this against the sample input.

First sample:

Input:
2
1 2
2 1

So the x's are 1 and 2. The frequency map is {1:1, 2:1}.

For the first team (y_i = 2), cnt_i is frequency of 2, which is 1. So home = 1 (n-1) + 1 = 2. away = 1 -1 =0. Which matches the output.

Second team's y_i is 1. frequency of 1 is 1. home =1 +1=2, away 1-1=0. Which matches.

Second sample:

3
1 2
2 1
1 3

x's are 1,2,1. So frequency map is {1:2, 2:1}.

For team 1, y_i=2. frequency of 2 is 1. home =2+1=3. away=2-1=1.

Team2: y_i=1. frequency is 2. home=2+2=4, away=2-2=0.

Team3: y_i=3. frequency of 3 in x's is 0. home=2+0=2, away=2-0=2. Which matches the sample output.

So this approach works.

Now, implementing this in Python.

But we need to handle colors up to 1e5, but with n up to 1e5. The Counter will be efficient enough.

In Python, using a list or a dictionary for the frequencies. Since colors can be up to 1e5, but for 1e5 elements, a dictionary is manageable.

So code steps:

Read n.

Then read n lines, each with x_i and y_i. Store them as a list.

Then create a frequency dict. For example:

from collections import defaultdict

freq = defaultdict(int)
for x, y in teams:
    freq[x] +=1

Wait, no. For each team, we have x (home color) and y (away color). But the frequency is for x across all teams.

So:

teams = []
for _ in range(n):
    x, y = map(int, input().split())
    teams.append( (x,y) )

freq = {}
for x, _ in teams:
    if x in freq:
        freq[x] +=1
    else:
        freq[x] =1

Alternatively, using a Counter:

from collections import Counter

xs = [x for x, y in teams]
freq = Counter(xs)

Then, for each team (x, y), the count is freq.get(y, 0).

Then compute home = (n-1) + count.

Away = (n-1) - count.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    teams = []
    for _ in range(n):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        teams.append( (x, y) )

    xs = [x for x, y in teams]
    from collections import Counter
    freq = Counter(xs)

    for x, y in teams:
        cnt = freq.get(y, 0)
        home = (n-1) + cnt
        away = (n-1) - cnt
        print(home, away, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 2
2 1
1 3
""",
            "output": \
"""\
3 1
4 0
2 2
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

teams are (1,2), (2,1), (1,3). xs is [1,2,1]. freq is {1:2, 2:1}.

First team: y=2. cnt=1 (since freq[2] is 1). home=2+1=3, away=2-1=1.

Second team: y=1. cnt=2 (freq[1] is 2). home=2+2=4, away=0.

Third team: y=3. freq[3] is 0. So home=2+0=2, away=2-0=2.

Yes.

Now, what about constraints? n can be up to 1e5. Reading 1e5 lines is manageable. The Counter is O(n) time. Then processing each team is O(n). So overall O(n), which is acceptable.

Memory-wise, storing the list of teams (each with two integers) is 2*1e5 numbers, which is acceptable. The Counter is O(u) where u is the number of unique x's. But worst case, if all x's are unique, it's 1e5 entries, which is manageable.

So this code should work.
</think>

```python
from collections import Counter

n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]
xs = [x for x, y in teams]
freq = Counter(xs)
for x, y in teams:
    cnt = freq.get(y, 0)
    print((n-1) + cnt, (n-1) - cnt)
```
