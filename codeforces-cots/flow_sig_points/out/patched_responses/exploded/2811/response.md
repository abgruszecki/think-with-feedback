<think>
Okay, let's tackle this problem. Hmm. So the problem is to determine which team wins based on their action strings. Both teams have strings of the same length, and each character represents an action. The goal is to compare the actions in each position and count which team has more winning actions.

First, I need to understand the rules of the game. Oh right, the problem says to figure out who wins based on their strings. So each character in the same position of the two strings are compared. For each position, whichever action beats the other gives a point to the corresponding team. If they are the same, no points. Then, after comparing all positions, the team with more points wins. If equal, it's a tie.

So the main task is to model the outcome of each individual character pair. Then sum the points for each team and compare the totals.

Let me think about the possible actions and their hierarchy. Wait, in the examples, they have characters like [], 8<, etc. Wait, the input strings are sequences of actions. Each action is a combination of characters? Or is each character in the string a separate action? For example, in the first example input:
[]()[]8<
8<[]()8<

Each team's string is like a series of actions. Wait, but looking at the sample input, the first team's string is "[]()[]8<", which seems like each action is a pair of characters. Like '[]' is one action, then '()', then another '[]', then '8<'? Similarly, the second team's string is "8<[]()8<". Wait, but the problem says the input is two strings of equal length. Each string describes the actions of one team. So perhaps each individual character is an action. Wait, but that can't be right because in the examples, the strings have even lengths. For example, the first sample input's first line is "[]()[]8<", which is 8 characters. So perhaps each action is represented by two characters. Like each pair of characters forms a single action. So for example, the first two characters '[]' form an action, then the next two '()', etc. So the total number of actions per team is the length of the string divided by two. Then, each action is compared between the two teams' corresponding positions. For example, in the first sample, each team has 4 actions. Then, each action from team 1 is compared to the same position's action from team 2.

Wait, but the problem statement says "each line describes the actions of one team." So maybe each action is a single character. Like, each character in the string is an action. So for a string of length N, there are N actions, each being one of certain possible characters.

But what are the possible action types and their hierarchy? The problem statement doesn't explicitly state the rules for which action beats another. So I need to infer this from the examples.

Looking at the first sample input:

Team1: []()[]8<
Team2: 8<[]()8<

The output is TEAM 2 WINS.

So let's break down each position. Since the strings are of equal length, each position's character from team1 and team2 are compared.

Wait, but the strings are of equal length. So each position's characters from the two teams are compared. But how? For example, in the first sample, each string is 8 characters long. So there are 8 positions. For each position, the characters are compared. Then, each position contributes to the score.

So for each index i from 0 to len-1, compare team1_char[i] vs team2_char[i]. For each such comparison, determine if team1's character beats team2's, or vice versa, or they tie.

The problem is to model the hierarchy of the characters. So what's the order of the actions?

Looking at the sample input 1:

Team1's string is "[ ] ( ) [ ] 8 <", but perhaps each character is part of an action pair. Alternatively, maybe each character is a separate action.

Alternatively, perhaps each action is one of the following:

- Rock (represented by some character)
- Paper
- Scissors
- etc. But I need to find out which characters correspond to which.

Alternatively, perhaps the possible actions are like in Rock-Paper-Scissors-Lizard-Spock, but with different symbols.

Alternatively, perhaps each action is a combination of characters, but that's more complex. But given the problem's examples, perhaps each action is a two-character symbol. For example, '8<' is an action. So the action symbols are made up of two characters. Then, each team's string is composed of a sequence of such two-character actions. So for example, a string of length 6 would have 3 actions.

So in the first sample input:

Team1's string is "[]()[]8<", which has 8 characters, so 4 actions. Each action is two characters: "[]", "()", "[]", "8<".

Team2's string is "8<[]()8<", which is also 8 characters, 4 actions: "8<", "[]", "()", "8<".

Then, each action is compared. For example, the first action of team1 is "[]", team2's first is "8<". Which one wins?

The output is TEAM 2 WINS, so perhaps in the first sample, team2's actions are winning more points.

So I need to figure out what beats what.

Looking at the first sample's first pair: [] vs 8<.

In team2's case, 8< is their action. How does that compare to []?

Assuming that each two-character action has a certain hierarchy. Let's think of possible action types and their beats.

The possible action symbols are: 8<, [], (), and maybe others. Wait, looking at the sample inputs, the possible actions are:

In the first sample input, the actions are "[]", "()", "8<", etc.

Wait, perhaps the possible actions are:

- 8< (which represents a rock, perhaps)
- [] (paper)
- () (scissors)

But that's a guess. Alternatively, maybe the hierarchy is as follows:

Each action can be one of:

- 8< (rock)
- [] (paper)
- () (scissors)
- (other possible actions?)

But then, according to rock-paper-scissors rules, paper beats rock, rock beats scissors, scissors beats paper.

In the first sample's first action pair: team1's [] (paper) vs team2's 8< (rock). Paper beats rock, so team1 would get a point. But the output is TEAM 2 WINS. So this suggests that maybe the hierarchy is different. So maybe the first action pair is team2's 8< beats team1's [].

Alternatively, perhaps the hierarchy is 8< beats [], () beats 8<, [] beats (). Or something else.

Alternatively, perhaps the hierarchy is:

Each action can be one of three types: 8< (Rock), [] (Paper), () (Scissors), but perhaps the beats relationships are different.

Alternatively, perhaps the actions are different, like 8< is Rock, [] is Paper, and () is Scissors. Then Rock beats Scissors, Scissors beats Paper, Paper beats Rock.

Wait, in the first sample, team1's actions are:

Action 1: [] (Paper)
Action 2: () (Scissors)
Action 3: [] (Paper)
Action 4: 8< (Rock)

Team2's actions:

Action1: 8< (Rock)
Action2: [] (Paper)
Action3: () (Scissors)
Action4: 8< (Rock)

So comparing each action:

Action1: Paper (T1) vs Rock (T2): Paper beats Rock → T1 gets a point.
Action2: Scissors (T1) vs Paper (T2): Scissors beats Paper → T1 gets another point.
Action3: Paper (T1) vs Scissors (T2): Scissors beats Paper → T2 gets a point.
Action4: Rock (T1) vs Rock (T2): Tie → no points.

So total points: T1 has 2 (action1 and 2), T2 has 1 (action3). So T1 would have more points, but the sample output is TEAM 2 WINS. So this contradicts. So perhaps the hierarchy is different.

Hmm, perhaps I need to look for another pattern.

Alternatively, perhaps the hierarchy is:

8< beats [] (Rock beats Paper?), no. That's not standard. Or perhaps the hierarchy is as follows:

8< (Rock) beats () (Scissors)
() (Scissors) beats [] (Paper)
[] (Paper) beats 8< (Rock)

That's the standard Rock-Paper-Scissors hierarchy. Then in action1: Paper (T1) vs Rock (T2) → Paper beats Rock → T1 gets a point. Action2: Scissors (T1) vs Paper (T2) → Scissors beats Paper → T1 gets a point. Action3: Paper (T1) vs Scissors (T2) → Scissors beats Paper → T2 gets a point. Action4: Rock (T1) vs Rock → tie.

So T1 has 2 points, T2 has 1. So the output would be TEAM 1 WINS. But in the first sample, the output is TEAM 2 WINS. So this suggests that my hierarchy is incorrect.

So the first sample's output is TEAM 2 WINS, meaning that team2's actions win more. Let's see the sample input again.

Team1's string is "[]()[]8<".

Breaking into two-character actions:

["[]", "()", "[]", "8<"]

Team2's string is "8<[]()8<".

Breaking into two-character actions:

["8<", "[]", "()", "8<"]

So, comparing each pair:

1. [] vs 8< → which wins? Team2's action here is 8<. So for team2 to get the point, 8< must beat [].
But in standard RPS, Paper ([]) beats Rock (8<). So if that's the case, team1 gets a point here. But according to the sample, team2 wins. So perhaps the hierarchy is reversed.

Alternatively, maybe 8< (Rock) beats [] (Scissors?), but that's not standard. Alternatively, perhaps the hierarchy is different.

Wait, maybe the hierarchy is:

8< (Scissors) beats [] (Paper)
[] (Paper) beats () (Rock)
() (Rock) beats 8< (Scissors)

Wait, but then 8< (Scissors) beats [] (Paper). So in the first action pair, team1's [] (Paper) is beaten by team2's 8< (Scissors). So team2 gets a point. Then action2: () (Rock) vs [] (Paper). Paper beats Rock → team2 gets another point. Action3: [] (Paper) vs () (Rock). Paper beats Rock → team1 gets a point. Action4: 8< (Scissors) vs 8< (Scissors) → tie. So points: team2 has 2 (action1 and 2), team1 has 1 (action3). So team2 wins, which matches the sample. So this hierarchy would fit.

So the hierarchy could be:

8< (Scissors) beats [] (Paper)
[] (Paper) beats () (Rock)
() (Rock) beats 8< (Scissors)
But what about other possible actions? Like, maybe other two-character combinations are possible. But according to the problem statement, each string is between 2 and 20 characters, so even lengths, implying that all actions are two-character. So possible actions are combinations of two characters. So perhaps the valid actions are:

- 8< (Scissors)
- [] (Paper)
- () (Rock)

And the hierarchy is:

Scissors (8<) beats Paper ([])

Paper ([]) beats Rock (())

Rock (()) beats Scissors (8<)

If that's the case, then the first sample would be:

Comparing each action pair:

1. [] (Paper) vs 8< (Scissors) → Scissors beat Paper → team2 gets 1 point.

2. () (Rock) vs [] (Paper) → Paper beats Rock → team2 gets another point.

3. [] (Paper) vs () (Rock) → Paper beats Rock → team1 gets a point.

4. 8< (Scissors) vs 8< → tie.

So total points: team2 has 2, team1 has 1. So team2 wins, which matches the sample.

Yes, this seems correct.

So the problem is to model each two-character action as either Scissors, Paper, or Rock, and apply the hierarchy where Scissors beats Paper, Paper beats Rock, Rock beats Scissors.

Wait, but according to the hierarchy above:

Scissors (8<) beats Paper ([])
Paper ([]) beats Rock (())
Rock (()) beats Scissors (8<)

So each action is a two-character symbol, and each is mapped to one of these three types.

So the first step is to parse each team's action sequence into their corresponding types. Each two-character pair is an action. Then, for each action pair (from team1 and team2), determine the outcome.

So the steps to solve the problem:

1. Split each team's string into two-character actions. For example, '8<[]()8<' becomes ['8<', '[]', '()', '8<'].

2. For each action in the same position, compare the team1's action vs team2's action.

3. Determine for each comparison which team gets a point (or none).

4. Sum the points for each team and compare.

Now, the main challenge is to correctly parse the actions and model the hierarchy.

First, check the possible two-character actions. According to the examples, the possible actions are '8<', '[]', '()', and perhaps others? Wait, the problem's examples include those. Let's see.

In the first sample input, the team1's actions are '[]', '()', '[]', '8<'. Team2's actions are '8<', '[]', '()', '8<'.

So the possible actions are '8<', '[]', '()'.

In the second sample input, the team1's string is '8<8<()' which breaks into '8<', '8<', '()'. Team2's string is '[]8<[]' which breaks into '[]', '8<', '[]'.

So the possible actions here are '8<', '()', '[]'.

Are there any other possible actions? The problem statement doesn't say, but according to the constraints, the input strings can be any characters, but we can infer that only these three actions are possible. But perhaps there are more. Wait, the problem's input is two strings, each line describes the actions of a team. The strings can have any characters (as per input), but according to the problem's examples, the actions are made up of these three. So perhaps the valid actions are these three. But perhaps other actions are possible, but according to the problem's examples, the possible actions are 8<, [], and ().

So, for each two-character action in the input, we need to check which type it is (Scissors, Paper, Rock). Then, for each pair of actions, determine which team wins that round.

So first, the code will process each string into a list of actions (two-character each). Then, for each pair of actions (team1's action and team2's action in the same position), compare them.

So, let's model the hierarchy.

Each action can be represented as a value, like a string. For example:

action_to_type = {
    '8<': 'scissors',
    '[]': 'paper',
    '()': 'rock'
}

Then, the hierarchy is:

scissors beats paper
paper beats rock
rock beats scissors

Wait, but in the hierarchy we inferred earlier, 8< (scissors) beats [] (paper), which beats () (rock), which beats 8< (scissors).

So in code, we can have a function that, given two actions, determines which one wins.

For example:

def get_winner(action1, action2):
    if action1 == action2:
        return 0  # tie
    beats = {
        '8<': ['[]'],  # scissors beats paper
        '[]': ['()'],  # paper beats rock
        '()': ['8<']   # rock beats scissors
    }
    if action2 in beats.get(action1, []):
        return 1  # team1 wins this round
    else:
        return 2  # team2 wins this round

Wait, but how does this work? Let's take action1 as '8<' (scissors) and action2 as '[]' (paper). Then, action2 is in beats[action1], so team1 wins. But in the first sample, team2's action was '8<' and team1's action was '[]' (paper) in the first position. So action1 is '[]', action2 is '8<'. Then, beats['[]'] is ['()'], so action2 is '8<' not in that list. So team2 wins, which is correct.

Wait, the function get_winner would return 1 if action2 is in the list of actions that action1 beats. Otherwise, team2 wins.

Wait, the function is called with action1 as team1's action, action2 as team2's action. So the logic is:

If action1 beats action2 → team1 gets a point.

If action2 beats action1 → team2 gets a point.

If they are the same → no points.

So the beats dictionary should map each action to the list of actions that it beats.

So for example, '8<' beats '[]', '[]' beats '()', '()' beats '8<'.

So the beats dictionary would be:

beats = {
    '8<': ['[]'],
    '[]': ['()'],
    '()': ['8<']
}

Then, for action1 and action2:

if action2 is in beats[action1], then team1 wins.

else if action1 is in beats[action2], then team2 wins.

else if they are same → tie.

So code:

for each pair in actions:

    if action1 == action2:
        continue
    elif action2 in beats[action1]:
        team1_score += 1
    elif action1 in beats[action2]:
        team2_score += 1
    else:
        # unknown action, but according to problem statement, perhaps all actions are valid and covered here.
        # but according to the problem statement, the input is two strings of equal length (even length?), but perhaps the input can have other two-character actions. But according to the problem examples, the actions are 8<, [], ().

Wait, but the problem statement allows any two characters. So what if an action is not in the beats dictionary? For example, if an action is 'aa'? Then, how do we handle that.

But according to the problem statement, each team's actions are given as strings. So perhaps the input can contain any two-character sequences, but according to the problem examples, the valid actions are the three we mentioned. So perhaps the problem expects us to only compare the three possible actions. If the input has other two-character sequences, they are considered invalid, but according to the problem's examples and the problem statement, perhaps the input will only consist of the three valid actions. Because in the sample inputs, all actions are among 8<, [], ().

So perhaps the code can assume that all actions are valid and part of the three types.

So, the code can proceed under that assumption.

So, the steps are:

Read two lines of input.

For each line, split into two-character chunks.

Then, for each corresponding action pair, compare using the beats dictionary.

Sum the points for each team.

Compare the sums. If team1's sum is higher, output "TEAM 1 WINS". If team2's sum is higher, output "TEAM 2 WINS". Else, output "TIE".

Now, code in Python.

First, read the two input lines:

team1 = input().strip()
team2 = input().strip()

Check that their lengths are equal, and even. But according to the problem statement, the input strings are of equal length (between 2 and 20, inclusive). So we can proceed.

Then, split each into two-character actions.

For splitting into two-character actions:

def split_actions(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

team1_actions = split_actions(team1)
team2_actions = split_actions(team2)

Then, for each pair of actions, compute the result.

Initialize team1_score and team2_score to 0.

beats = {
    '8<': ['[]'],
    '[]': ['()'],
    '()': ['8<']
}

for a1, a2 in zip(team1_actions, team2_actions):
    if a1 == a2:
        continue
    if a2 in beats.get(a1, []):
        team1_score += 1
    elif a1 in beats.get(a2, []):
        team2_score += 1
    else:
        # what's the default? Perhaps if two actions are not in the beats relation, they are considered a tie. But according to the problem statement, the input is valid. So perhaps this case cannot happen.
        pass

Then, compare the scores.

if team1_score > team2_score:
    print("TEAM 1 WINS")
elif team2_score > team1_score:
    print("TEAM 2 WINS")
else:
    print("TIE")

But wait, in the first sample, the code would split the team1's actions into:

['[]', '()', '[]', '8<'] 

team2_actions: ['8<', '[]', '()', '8<']

Now, compare each pair:

1. a1 = '[]', a2 = '8<'

Check if a2 is in beats[a1]. beats['[]'] is ['()'], which a2 is '8<', not in the list. Then check if a1 is in beats[a2]. beats['8<'] is ['[]']. So a1 is in beats['8<'] → so team2 gets a point.

So team2_score +=1.

Second pair: a1 = '()', a2 = '[]'

beats['()'] is ['8<']. a2 is '[]' not in that list. Check a2's beats. beats['[]'] is ['()'], and a1 is '()' in that list → so a2 (team2's action) beats a1. So team2 gets another point. team2_score +=1.

Third pair: a1 = '[]', a2 = '()'. beats['[]'] includes '()' → a2 is in beats[a1], so team1 gets a point. team1_score +=1.

Fourth pair: a1='8<', a2='8<' → tie. No points.

So total team1_score=1, team2_score=2. So output TEAM 2 WINS. Which matches the sample.

Another sample:

Input:

8<8<()
[]8<[]

Split into team1_actions: ['8<', '8<', '()'], team2_actions: ['[]', '8<', '[]']

Compare each:

1. 8< vs []: team2's action is [], which is beaten by 8<. So team1 gets a point.

Because beats['8<'] is ['[]'], so a2 is in that list. So team1_score +=1.

Second pair: 8< vs 8< → tie.

Third pair: '()' vs '[]'. beats['()'] is ['8<'], so a2 is '[]' not in the list. Check if a1 is in beats[a2]. beats['[]'] is ['()'], and a1 is '()' is in the list. So team2's action (a2) is '[]', which beats a1 '()' → team2 gets a point.

So team1 has 1, team2 has 1. Tie → output TIE. Which matches the second sample.

So this code should work.

Now, code considerations.

The code reads two lines, splits into two-character actions, compares each pair.

What about leading/trailing whitespaces? The problem says the input is two strings, so perhaps leading/trailing spaces are not part of the input, but according to Python's input().strip(), which removes leading and trailing whitespace. So perhaps using strip() is better.

But according to the sample inputs, the first sample input is:

[]()[]8<
8<[]()8<

So leading and trailing spaces are not present.

But the code uses input().strip(), which would remove any leading/trailing whitespace. So the code may not work if the input strings have internal spaces. But according to the problem statement, each line describes the actions of a team. So the strings should not have any spaces, as they are part of the actions.

But in the problem statement, the input is two strings. So each line is read as a single string. So the code is correct.

Now, code implementation.

But wait, in the code, when splitting the strings into actions, for a string of even length, it's split into pairs. For example, a string of 8 characters → 4 actions. For a string of 6 characters → 3 actions.

Yes, that's handled by range(0, len(s), 2), which steps by 2 each time.

But in Python, when using s[i:i+2], for even-length strings, all characters are covered. For example, len(s) is 8: i runs 0, 2,4,6 → i+2 is 2,4,6,8. So slices 0:2, 2:4, 4:6, 6:8 → four two-character strings.

So the code is correct.

Now, code.

Putting it all together:

Read the two lines, split into actions, compare each pair, count scores, output.

So the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    team1 = input_stream.readline().rstrip("\n").strip()
    team2 = input_stream.readline().rstrip("\n").strip()

    def split_actions(s):
        return [s[i:i+2] for i in range(0, len(s), 2)]

    actions1 = split_actions(team1)
    actions2 = split_actions(team2)

    beats = {
        '8<': ['[]'],
        '[]': ['()'],
        '()': ['8<']
    }

    t1 = 0
    t2 = 0

    for a1, a2 in zip(actions1, actions2):
        if a1 == a2:
            continue
        if a2 in beats.get(a1, []):
            t1 +=1
        elif a1 in beats.get(a2, []):
            t2 +=1

    if t1 > t2:
        print("TEAM 1 WINS", file=output_stream)
    elif t2 > t1:
        print("TEAM 2 WINS", file=output_stream)
    else:
        print("TIE", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8<8<()
[]8<[]
""",
            "output": \
"""\
TIE
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

team1: '8<8<()' → split into ['8<', '8<', '()']
team2: '[]8<[]' → split into ['[]', '8<', '[]']

Compare pairs:

1. '8<' vs '[]': a2 in beats['8<'] → ['[]'] → yes. So t1 +=1 → t1=1.

2. '8<' vs '8<' → same.

3. '()' vs '[]': a2 is '[]'. beats['()'] is ['8<'], a2 not in that. Check a1 in beats[a2] → beats['[]'] is ['()']. a1 is '()' which is in the list → team2 gets a point. t2=1.

Total t1=1, t2=1 → TIE.

Which is correct.

So the code works for these cases.

Now, code optimization. Since the input strings can be up to 20 characters long, the maximum number of actions is 10. So the code is O(1) time and memory, which is acceptable.

Thus, the code is correct and optimized.
</think>

```python
team1 = input().strip()
team2 = input().strip()

def split_actions(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

actions1 = split_actions(team1)
actions2 = split_actions(team2)

beats = {
    '8<': ['[]'],
    '[]': ['()'],
    '()': ['8<']
}

t1, t2 = 0, 0

for a1, a2 in zip(actions1, actions2):
    if a1 == a2:
        continue
    if a2 in beats.get(a1, []):
        t1 += 1
    elif a1 in beats.get(a2, []):
        t2 += 1

print("TEAM 1 WINS" if t1 > t2 else "TEAM 2 WINS" if t2 > t1 else "TIE")
```
