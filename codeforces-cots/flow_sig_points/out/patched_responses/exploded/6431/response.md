<think>
Okay, let's see. The problem is about two teams choosing their attack and defense players optimally to determine if one team can guarantee a win. 

So, the first team (players 1 and 2) chooses their attack and defense arrangement first. Then the second team (players 3 and 4) does the same. We need to find out if, given optimal choices by both teams, either team 1 can definitely win, team 2 can definitely win, or it's a draw.

Hmm. The key here is that each team's choice affects the next. The first team's choice is made first, then the second team reacts. So for team 1 to have a guaranteed win, they must have a way to arrange their attack and defense such that no matter how team 2 arranges theirs, team 1's defense is strictly greater than team 2's attack and team 1's attack is strictly greater than team 2's defense.

Wait, but the problem says "one team is guaranteed to beat the other one if its defense is strictly greater than opponent's attack and its attack is strictly greater than opponent's defense." So, for team 1 to win, in their chosen arrangement, their defense (d1) must be > team 2's attack (a2), and their attack (a1) must be > team 2's defense (d2). Then team 1 wins. Similarly for team 2.

But the order of choices is crucial. The first team picks their attack and defense (for example, player1 in attack, player2 in defense, or vice versa), then the second team picks their arrangement. The second team's choice will depend on the first team's choice, trying to maximize their own chances.

So, to determine if team1 can guarantee a win, we need to check if there's a possible arrangement for team1 where, for all possible arrangements of team2, team1's conditions hold. If such an arrangement exists, then team1 can win. Similarly, for team2, but considering that team2's choice is after team1's.

Wait, but the problem statement says that the teams act optimally. So for team1 to be able to win, they must choose an arrangement such that no matter how team2 chooses their arrangement (optimally for team2's benefit), team1's conditions are met. Alternatively, team2's optimal choice might try to avoid team1's conditions.

Wait, but the question is about whether a team can be "guaranteed" to win. So, for team1 to have a guaranteed win, there must exist some arrangement (attack/defense choice) for team1 such that, regardless of team2's arrangement (even if team2 chooses the worst possible option for team1), team1's attack and defense are greater than team2's defense and attack, respectively. Wait, no. Because team2's choice is made after team1's. So team2 will choose the arrangement that is best for them. So, for team1 to have a guaranteed win, there must be some arrangement where, for all possible responses by team2 (their possible arrangements), team1's attack and defense are strictly greater than team2's defense and attack.

Alternatively, maybe team2's optimal response would be to choose an arrangement that minimizes the chance of team1 winning. So, for team1 to have a guaranteed win, even in the worst case (team2's best possible response), team1's arrangement must still satisfy the conditions.

Wait, the problem statement says: "each team arrange their teams optimally". So when the first team chooses their arrangement, they know that the second team will then choose their best possible arrangement in response. So, team1's choice must be such that, even after team2 chooses their best possible arrangement (from their perspective, which might be trying to prevent team1's win or trying to maximize their own win), team1's conditions hold.

But how do we model this?

Let's break it down step by step.

First, team1 has two possible options for attack and defense. Since there are two players (1 and 2), the possible arrangements are:

- Player A in attack (using their attack skill) and player B in defense (using their defense skill). So, for team1, the attack is b_A and defense is a_B if they choose to have player A as attacker and player B as defender.

Wait, no. Wait, the problem says: the team's defense is the defense skill of the player who plays defense. The attack is the attack skill of the player who plays attack. So for each team, you choose two players (since there's two players in the team) to assign to attack and defense. But wait, each team has two players. So, for team1, they can choose either:

player1 in attack (so attack is b1) and player2 in defense (so defense is a2), or player2 in attack (b2) and player1 in defense (a1). Because each team's players are two, the possible options are two: assign one to attack and the other to defense. So, each team's possible arrangements are two possibilities.

Similarly for team2.

So, for team1, the possible options are:

Option 1: attack is b1 (player1's attack), defense is a2 (player2's defense).

Option 2: attack is b2 (player2's attack), defense is a1 (player1's defense).

Similarly, team2's possible options are:

Option A: attack is b3 (player3's attack), defense is a4 (player4's defense).

Option B: attack is b4 (player4's attack), defense is a3 (player3's defense).

So, team1's choice is between two options. Then team2 chooses between their two options, knowing team1's choice.

The problem asks: can team1 choose their arrangement such that, no matter how team2 chooses their arrangement (optimally for team2's benefit), team1's conditions are met (their defense > team2's attack and their attack > team2's defense) OR team2's conditions are not met, and team2 cannot make their own conditions met.

Wait no. The problem says that the team is guaranteed to beat the other if the defense and attack conditions are met. So, for team1 to win, in the current arrangement, their defense must be > team2's attack, and their attack must be > team2's defense. If either of these is not true, then team1's conditions are not met.

But team2's goal is to prevent team1 from winning and possibly to allow themselves to win. So, when team1 chooses their arrangement, they need to choose it in a way that, even after team2 chooses their best possible arrangement (which might be to make team1's conditions not met or to make their own conditions met), team1's conditions are still satisfied.

So, the process is:

1. Team1 chooses their arrangement (attack and defense) options: T1_1 or T1_2.

2. Team2, knowing team1's arrangement, chooses their arrangement (T2_1 or T2_2) that is best for them. Best here could mean that if team2 can win (their conditions are met) then they choose that. Otherwise, they choose an arrangement that makes sure team1 can't win.

So, for team1 to have a guaranteed win, there must exist an arrangement (either T1_1 or T1_2) such that, for all possible responses (T2_1 and T2_2) that team2 can make, team1's conditions (d1 > a2 and a1 > d2) are true. Because team2 would choose their best arrangement, which could be to try to prevent team1's conditions.

Wait, but team2's optimal choice depends on their own options. For example, team2's best choice might be to choose the arrangement where their own conditions (d2 > a1 and a2 > d1) are met, which would make team2 the winner. But if that's possible, then team1's choice would not be a winning one.

So, for team1 to have a possible winning arrangement, when they choose that arrangement, team2's best response (for team2) would not be able to prevent team1's conditions from being met.

Alternatively, perhaps team1's arrangement must be such that, regardless of team2's choice (even if team2 chooses any of their options), team1's conditions are met. Because team2 will choose the best possible arrangement for themselves, which might be to allow team1's conditions to be met if that's unavoidable, but team1's goal is to choose an arrangement where all possible team2 responses result in team1's conditions being met.

Wait, but the problem statement says: "the teams arrange their teams optimally". So, team2 will choose the arrangement that maximizes their own chances. So, for team1's arrangement, team2 can choose between their two options. For team1 to have a guaranteed win, in both possible team2 responses, team1's conditions must hold. Because if there's any team2 arrangement that makes team1's conditions not hold, then team2 will choose that arrangement, thus preventing team1's win.

So, for team1 to be able to guarantee a win, they must choose an arrangement where, for all possible team2's arrangements, team1's attack and defense are strictly greater than team2's defense and attack, respectively.

Wait, no. Because team2's arrangement choice is based on their own optimality. So, for team1's arrangement, team2 will choose the arrangement that is best for their own team. If in any of the team2's possible arrangements, team2 can make their own conditions (d2 > a1 and a2 > d1) true, then team2 will win. Otherwise, team2 will choose the arrangement that prevents team1's conditions from being true.

So, for team1's chosen arrangement, team2 can choose between their two options. Team1's arrangement is only a winning one if, after team2 picks their best possible arrangement (from their perspective), team1's conditions are still satisfied.

But how do we model this?

Let's think in terms of game theory. The first team chooses their arrangement. Then, the second team chooses their arrangement, knowing the first's choice. The second team's choice is to maximize their own outcome. So, for team1 to have a winning scenario, they need to choose an arrangement such that, in all possible team2's responses (which could be either of their two options), team1's conditions are met.

Alternatively, perhaps the second team's choice is to pick the arrangement that is best for them, which could be to either allow them to win or prevent team1 from winning.

So, for team1 to have a possible winning arrangement, they need to find an arrangement where, after the second team has chosen their best possible response, team1's conditions are still met.

But how to model this?

Let's take an example.

Suppose team1 chooses arrangement X. Then team2 can choose between Y and Z. For team1 to win, in all possible Y and Z, team1's conditions must hold? Or is team2 allowed to choose the best possible Y or Z that could make team1's conditions not hold?

Ah, right. Because team2 will choose their arrangement in a way that is optimal for them, which could include trying to make their own conditions hold (thus winning) or, if that's not possible, making team1's conditions not hold (so the result is a draw or they lose). Wait, but in the problem statement, it says that a team is guaranteed to beat the other if their conditions are met. So, if team1's arrangement allows team2 to choose an arrangement where team2's conditions are met, then team2 will choose that, thus winning. Otherwise, team2 will choose an arrangement that doesn't allow team1 to meet their conditions.

So, to check if team1 can guarantee a win, we need to find if there exists a team1 arrangement where, for team2's optimal choice (which is the best possible for team2), team1's conditions are still met.

But how to model the optimal choice for team2 given team1's arrangement.

Let's formalize this.

For each possible team1 arrangement (T1_1, T1_2), we need to see what team2 would choose.

When team2 chooses their arrangement, they have two options. They can choose T2_1 or T2_2.

For each possible team2 arrangement, we can compute whether team2's conditions (d2 > a1 and a2 > d1) are met. If any of their options allows them to meet their conditions, they will choose that, thus team2 wins. Otherwise, they will choose an arrangement that makes team1's conditions not met (so the result is either a draw or team2 can't win but team1 can't either).

So, for team1's arrangement to be a winning one, it must be that, after team2 chooses their best possible arrangement (for their own benefit), team1's conditions are met.

So, for a given team1 arrangement (t1_attack, t1_defense), team2's possible responses are their two arrangements. Let's consider all possible team2 arrangements and check:

1. If any of team2's arrangements satisfies their own conditions (t2_defense > t1_attack AND t2_attack > t1_defense), then team2 will choose that arrangement and win. Thus, in this case, team1's arrangement is not a winning one.

2. If none of team2's arrangements satisfy their own conditions, then team2 will choose an arrangement that makes team1's conditions (t1_defense > t2_attack AND t1_attack > t2_defense) false. So team2 will choose the arrangement where either t2_attack >= t1_defense OR t2_defense >= t1_attack. If possible, they will choose an arrangement that breaks team1's conditions.

In this case, for team1's arrangement to be a winning one, it must be that for all possible team2 arrangements that team2 can choose (even those that team2 would choose to minimize team1's chances), team1's conditions are still met.

Wait, but if team2's options are such that neither of their arrangements allows them to win (i.e., neither arrangement meets their conditions), then team2 will choose an arrangement that makes team1's conditions not hold. So, team1's conditions must hold in all possible team2 arrangements that team2 could choose. But if team2 can choose between two options where one makes team1's conditions hold and the other not, then team2 will choose the latter. So for team1 to have a winning arrangement, in all possible team2 arrangements (after team2 chooses their best), team1's conditions must hold.

So, the algorithm for team1 is:

For each possible team1 arrangement (t1_attack, t1_defense):

   Check all possible team2 arrangements (t2_attack, t2_defense):

      If any team2 arrangement allows team2 to win (t2_defense > t1_attack and t2_attack > t1_defense), then team2 will choose that, leading to team2's victory. Thus, team1's arrangement is invalid.

   If none of the team2 arrangements allow team2 to win:

      Then team2 will choose an arrangement that maximizes their own chances, which in this case is to choose the arrangement where team1's conditions are not met. So, for team1's arrangement to be valid, both of team2's arrangements must satisfy team1's conditions (t1_defense > t2_attack and t1_attack > t2_defense).

Wait, no. Because team2 can't make their own conditions true, so their goal is to prevent team1's conditions from being true. So, team2 will choose between their two options the one that makes team1's conditions false. If there exists at least one arrangement for team2 where team1's conditions are not met, team2 will choose that, making team1's arrangement invalid.

Thus, for team1's arrangement to be a valid winning option, it must be that:

   For all possible team2's arrangements (t2_attack, t2_defense):

      Either:

         a) team1's conditions (t1_defense > t2_attack and t1_attack > t2_defense) are met, OR

         b) team2's conditions (t2_defense > t1_attack and t2_attack > t1_defense) are met.

But since in the first step, we already check that none of team2's arrangements meet their own conditions (because if any do, then team2 chooses that and wins), then in the second case, team2's arrangements are such that none of them meet their conditions. So team2 will choose the arrangement that makes team1's conditions false.

Therefore, for team1's arrangement to be valid, in all team2's possible arrangements, either team2's conditions are met (but we have already checked they aren't) or team1's conditions are met. But since team2's conditions are not met, team1's arrangement must, for all possible team2's arrangements, have their own conditions met. Because if any of team2's arrangements breaks team1's conditions, then team2 will choose that arrangement, causing team1 to not meet their conditions.

Wait, this is getting a bit confusing. Let's structure this step by step.

For team1 to have a winning arrangement (t1_attack, t1_defense):

1. For team2's possible arrangements (t2_1 and t2_2):

   a. Check if any of these arrangements allows team2 to win. If yes, then team2 will choose that arrangement, and team1's arrangement is invalid.

   b. If none of team2's arrangements allow team2 to win, then team2 will choose an arrangement that makes team1's conditions not met. So for team1's arrangement to be valid, in both of team2's possible arrangements, team1's conditions must hold. Because if even one arrangement of team2's breaks team1's conditions, team2 will choose that, making team1's conditions not met.

So, the steps for team1 to have a possible winning arrangement are:

For each team1 arrangement:

   Check if any team2 arrangement leads to team2's victory (their conditions met). If yes, then team1's arrangement is invalid.

   Else, check if all team2 arrangements lead to team1's victory (their conditions met). If yes, then team1's arrangement is valid.

So, in code terms:

for t1_option in [ (b1, a2), (b2, a1) ]:

    t1_attack, t1_defense = t1_option

    team2_options = [ (b3, a4), (b4, a3) ]

    # Check if any team2 option allows team2 to win.

    team2_can_win = any( (t2_defense > t1_attack) and (t2_attack > t1_defense) for (t2_attack, t2_defense) in team2_options )

    if team2_can_win:

        continue  # team2 would choose this option and win, so team1's arrangement is invalid.

    else:

        # Now, team2 cannot win. They will choose an option that makes team1's conditions false.

        # So, for team1's arrangement to be valid, in all team2's options, team1's conditions must hold.

        # Otherwise, team2 can choose an option that breaks team1's conditions.

        team1_wins_all = all( (t1_defense > t2_attack) and (t1_attack > t2_defense) for (t2_attack, t2_defense) in team2_options )

        if team1_wins_all:

            return "Team 1" can win.

Similarly, for team2 to have a possible winning arrangement, we need to check if, after team1 chooses their arrangement (optimally), team2 can choose an arrangement that leads to their own victory regardless of team1's choice.

Wait, but the problem states that team1 chooses first, then team2. So for team2 to have a guaranteed win, they must be able to choose their arrangement in response to team1's arrangement such that, for all possible team1's arrangements, team2 can choose their own arrangement to meet their conditions.

But how?

Alternatively, team2 can only win if, for every possible team1's arrangement, team2 can choose an arrangement that allows them to win.

So, for team2 to have a guaranteed win, for every possible team1 arrangement (t1_attack, t1_defense), there exists a team2 arrangement (t2_attack, t2_defense) such that team2's conditions (t2_defense > t1_attack and t2_attack > t1_defense) are met.

Because team1's choice is first. Team2 can choose their arrangement based on team1's choice. So, team2 can win if, no matter how team1 arranges their players, team2 can find a response that makes their conditions true.

So, team2's condition for guaranteed victory is: for all team1's possible arrangements (t1_attack, t1_defense), there exists a team2 arrangement (t2_attack, t2_defense) such that t2_defense > t1_attack and t2_attack > t1_defense.

If this is true, then no matter what team1 does, team2 can choose an arrangement that allows them to win. Hence, team2 is guaranteed to win.

If neither team1 nor team2 can guarantee a win, then it's a draw.

So, putting this all together:

The solution steps are:

1. Check if team1 can have a winning arrangement.

   For each of team1's possible arrangements:

      a. Check if team2 can win with any of their options. If yes, then team1's arrangement is invalid.

      b. Else, check if team1's conditions hold for all of team2's options. If yes, then team1 can win.

   If any of team1's arrangements pass (b), then team1 can win.

2. Else, check if team2 can always win regardless of team1's arrangement.

   For team2 to win, for every team1 arrangement, team2 has at least one arrangement that allows them to win.

   So, for each team1 arrangement (t1_attack, t1_defense):

      Check if there exists at least one team2 arrangement where t2_defense > t1_attack and t2_attack > t1_defense.

   If for all team1 arrangements, this is true, then team2 can win.

3. Else, output Draw.

So, let's model this.

First, generate all possible team1 arrangements (there are two: (b1, a2) and (b2, a1)).

For team1 to have a winning possibility, there exists at least one arrangement (t1_a, t1_d) where:

   - None of team2's arrangements allow team2 to win (i.e., for all team2 options, team2's conditions are not met).

   - And, all team2's arrangements (since team2 can't win) must lead to team1's conditions being met. Because team2 will choose the arrangement that breaks team1's conditions if possible, but if all team2's arrangements result in team1's conditions being met, then team1's arrangement is valid.

So, in code:

team1_possible = False

for t1_a, t1_d in [(b1, a2), (b2, a1)]:

    team2_options = [(b3, a4), (b4, a3)]

    # Check if team2 can win with any option.

    team2_can_win = any( (t2_d > t1_a and t2_a > t1_d) for t2_a, t2_d in team2_options )

    if team2_can_win:

        continue  # team1 can't use this arrangement, team2 would choose the winning option.

    # Now, team2 can't win. Check if team1's conditions hold for all team2 options.

    team1_wins = all( (t1_d > t2_a and t1_a > t2_d) for t2_a, t2_d in team2_options )

    if team1_wins:

        team1_possible = True

        break

If team1_possible is True, then output "Team 1".

Else, check team2's possibility.

For team2 to be able to win regardless of team1's choice, every team1 arrangement must have at least one team2 arrangement that meets team2's conditions.

So, for each team1 arrangement (t1_a, t1_d):

   Check if there exists at least one team2 arrangement (t2_a, t2_d) where t2_d > t1_a and t2_a > t1_d.

If this is true for all team1 arrangements, then team2 can win.

So:

team2_possible = True

for t1_a, t1_d in [(b1, a2), (b2, a1)]:

    team2_options = [(b3, a4), (b4, a3)]

    # Check if any of team2's options allows them to win.

    possible = any( (t2_d > t1_a and t2_a > t1_d) for t2_a, t2_d in team2_options )

    if not possible:

        team2_possible = False

        break

If team2_possible is True, then output "Team 2".

Else, output "Draw".

That's the logic.

Now, let's test this with the examples.

First example:

Input:

1 100

100 1

99 99

99 99

Team1 options:

Option 1: attack=100 (b1=100), defense=1 (a2=1). Because player1 is attack, player2 defense.

Wait, wait, for team1's options:

Player1 and player2.

Possible arrangements:

Either player1 attack (b1=100) and player2 defense (a2=1). So attack is 100, defense is 1.

OR player2 attack (b2=1) and player1 defense (a1=1). Wait, the first line is player1's a and b. So a1 is 1, b1 is 100. Second line is a2=100, b2=1.

So, team1's options are:

Option 1: attack is b1 (100), defense is a2 (100) → because player2 is in defense, so a2 is 100.

Option 2: attack is b2 (1), defense is a1 (1).

Wait, no. Wait, the first team's possible arrangements are:

- Player1 is attack, player2 is defense: attack is b1 (100), defense is a2 (100). Because a2 is the defense skill of player2 (which is 100). So this arrangement's attack is 100, defense is 100.

- Player2 is attack, player1 is defense: attack is b2 (1), defense is a1 (1). So attack is 1, defense is 1.

So team1's two options are (100, 100) and (1, 1).

Then, team2's options are (b3, a4) and (b4, a3). The third and fourth players are players3 and4. The third line is a3=99, b3=99. Fourth line is a4=99, b4=99.

So team2's options are:

Option1: attack is b3 (99), defense is a4 (99).

Option2: attack is b4 (99), defense is a3 (99).

So, team2's options are (99,99) and (99,99).

Now, for team1's first option (100, 100):

Check if team2 can win in any of their options.

Team2's conditions: t2_defense (99) > t1_attack (100) → 99>100 is false. And t2_attack (99) > t1_defense (100) → false. So team2 can't win.

So team1's arrangement (100,100) now needs to check if all team2's options (both (99,99)) satisfy team1's conditions (t1_defense (100) > t2_attack (99) and t1_attack (100) > t2_defense (99)).

Yes. So team1's conditions are met. So team1 can choose this arrangement, and team2's options can't prevent it. So team1 can win.

So the output is Team1, which matches the first example.

Second example:

Input:

1 1

2 2

3 3

2 2

Team1's options:

Option1: attack is b1 (1) and defense is a2 (2). So (1,2).

Option2: attack is b2 (2) and defense is a1 (1). So (2,1).

Team2's options:

player3 and4. Player3: a=3, b=3. Player4: a=2, b=2.

So team2's arrangements are:

Option1: attack is b3 (3), defense is a4 (2) → (3,2).

Option2: attack is b4 (2), defense is a3 (3) → (2,3).

Now, check team2's possibility.

For team2 to be able to win regardless of team1's arrangement.

For each team1's arrangement, check if team2 has at least one option that allows them to win.

Team1's arrangement 1: (1, 2).

Check team2's options:

Option1: (3,2). team2's conditions: 2 > 1 (t1_attack=1) → 2>1 is true. 3>2 (t1_defense=2) → 3>2 is true. So team2's conditions are met. So team2 can choose this option and win.

So for this arrangement, team2 can win.

Team1's arrangement 2: (2,1).

Check team2's options:

Option1: (3,2). team2_defense=2, attack=3.

Conditions: 2>2 (team1's attack is 2) → 2>2 is false. So team2's conditions are 2>2 (false) and 3>1 (true). So both conditions not met.

Option2: (2,3). team2_defense=3, attack=2.

Conditions: 3>2 (team1's attack is 2) → true. 2>1 (team1's defense is 1) → true. So team2's conditions are met. So team2 can choose option2 and win.

So, for both team1's arrangements, team2 can choose an option to win. Thus, team2 can always win regardless of team1's choice. So output is Team2.

Third example:

Input:

3 3

2 2

1 1

2 2

Team1's options:

Option1: attack is b1 (3), defense is a2 (2) → (3,2).

Option2: attack is b2 (2), defense is a1 (3) → (2,3).

Team2's options:

player3 (a=1, b=1) and player4 (a=2, b=2).

Team2's arrangements:

Option1: attack is b3 (1), defense is a4 (2) → (1,2).

Option2: attack is b4 (2), defense is a3 (1) → (2,1).

Check team1's possibilities.

First, check if team1 can have a winning arrangement.

Check team1's option1: (3,2).

Team2's options:

Check if any team2's option allows them to win.

For option1 (1,2): team2_defense=2 > team1_attack=3? 2>3 is false. team2_attack=1 > team1_defense=2? 1>2 is false. So no.

For option2 (2,1): team2_defense=1>3? No. attack 2>2? 2>2 is false. So no.

So team2 can't win. Now check if team1's conditions hold for all team2's options.

For team2's option1 (1,2):

team1_defense (2) > team2_attack (1) → yes. team1_attack (3) > team2_defense (2) → yes.

For team2's option2 (2,1):

team1_defense (2) > team2_attack (2) → no (2>2 is false). So team1's conditions are not met.

Thus, team2 can choose option2, which breaks team1's conditions. So team1's arrangement (3,2) is invalid.

Check team1's option2: (2,3).

Team2's options:

Check if any option allows team2 to win.

For option1 (1,2): team2_defense=2>2? No. attack=1>3? No.

For option2 (2,1): team2_defense=1>2? No. attack=2>3? No. So team2 can't win.

Now check team1's conditions for all team2 options.

team1_defense (3) > team2_attack (1) → yes. team1_attack (2) > team2_defense (2) → no (2>2 is false).

Thus, in team2's option2 (attack 2, defense 1), team1_attack (2) > defense (1) → yes. So team1's conditions are 3>2 (yes) and 2>1 (yes). So for team2's option2 (attack=2, defense=1), team1_defense (3) > 2 (team2's attack?), wait wait:

Wait, team1's arrangement is attack 2 (b2), defense 3 (a1=3). So t1_attack=2, t1_defense=3.

team2's option1: attack=1, defense=2.

Check team1's conditions: defense (3) > attack (1) → yes. attack (2) > defense (2) → no. So team1's conditions are not met.

Wait, this is confusing. Let's re-examine.

Team1's arrangement is (2,3): attack is 2, defense is 3.

Team2's options:

Option1: attack is 1, defense is 2.

So, team1's conditions: defense (3) > team2's attack (1) → yes. attack (2) > team2's defense (2) → 2>2 is no. So conditions are not met.

Option2: attack is 2, defense is 1.

team1's defense (3) > attack (2) → yes. attack (2) > defense (1) → yes. So conditions are met.

So, team1's conditions are met for option2 but not for option1.

Thus, team2 can choose option1, which breaks team1's conditions.

Thus, team1's arrangement is invalid.

So team1 cannot win.

Now check team2's possibility.

For each team1's arrangement, see if team2 can win.

Team1's arrangement (3,2):

Team2's options:

Check if any of them allow team2 to win.

team2's conditions are t2_defense > t1_attack and t2_attack > t1_defense.

t1_attack is 3, t1_defense is 2.

team2's option1: defense is 2, attack is 1.

t2_defense (2) > 3 → no.

team2's option2: defense is 1, attack is 2.

t2_defense (1) >3 → no. So team2 can't win.

Team1's arrangement (2,3):

t1_attack 2, t1_defense 3.

team2's options:

option1: defense 2, attack 1 → t2_defense (2) > 2? No. attack 1>3? No.

option2: defense 1, attack 2 → t2_defense (1) >2 → no.

So team2 can't win in any case.

Thus, team2 can't always win. So output is Draw.

Which matches the third example.

So the algorithm seems correct.

Now, implement this in Python.

Read the four players' a and b.

Compute team1's two options.

Check team1_possible.

Then check team2_possible.

Else, output Draw.

Now, code.

Read the input: four lines. Each line is a_i and b_i.

player = [ ]

for _ in range(4):

    a, b = map(int, input().split())

    player.append( (a, b) )

Then, team1's possible arrangements are:

t1_options = [ (player[0][1], player[1][0]), (player[1][1], player[0][0]) ]

Similarly, team2's options are:

t2_options = [ (player[2][1], player[3][0]), (player[3][1], player[2][0]) ]

Wait, for team2, players3 and4 (indices 2 and3 in 0-based list). So team2's arrangements are:

Option1: player3 attack (b3) and player4 defense (a4) → (player[2][1], player[3][0]).

Option2: player4 attack (b4) and player3 defense (a3) → (player[3][1], player[2][0]).

So team2's options are as above.

So for each team1 option, we need to check team2's options.

Now, code.

Check team1 possible:

team1_possible = False

for t1_attack, t1_defense in [ (player[0][1], player[1][0]), (player[1][1], player[0][0]) ]:

    team2_can_win = any( (t2_defense > t1_attack) and (t2_attack > t1_defense) for t2_attack, t2_defense in [(player[2][1], player[3][0]), (player[3][1], player[2][0])] )

    if team2_can_win:

        continue

    # Check if all team2 options allow team1 to win.

    team1_all_win = all( (t1_defense > t2_attack) and (t1_attack > t2_defense) for t2_attack, t2_defense in [(player[2][1], player[3][0]), (player[3][1], player[2][0])] )

    if team1_all_win:

        team1_possible = True

        break

If team1_possible is True, then output "Team 1".

Else, check team2_possible.

team2_possible = True

for t1_attack, t1_defense in [ (player[0][1], player[1][0]), (player[1][1], player[0][0]) ]:

    team2_has_winning = any( (t2_defense > t1_attack) and (t2_attack > t1_defense) for t2_attack, t2_defense in [(player[2][1], player[3][0]), (player[3][1], player[2][0])] )

    if not team2_has_winning:

        team2_possible = False

        break

If team2_possible is True, output "Team 2".

Else, output "Draw".

Putting this all together.

Now, code:

Read the four players.

Compute team1 options and team2 options.

Check team1 possible.

Check team2 possible.

Else, Draw.

So the code is:

players = [tuple(map(int, input().split())) for _ in range(4)]

# Team1 options: (b0, a1), (b1, a0)
t1_options = [
    (players[0][1], players[1][0]),
    (players[1][1], players[0][0]),
]

# Team2 options: (b2, a3), (b3, a2)
t2_options = [
    (players[2][1], players[3][0]),
    (players[3][1], players[2][0]),
]

team1_win = False
for t1_a, t1_d in t1_options:
    # Check if team2 can win with any of their options
    team2_win_any = any(
        (t2_d > t1_a) and (t2_a > t1_d) for t2_a, t2_d in t2_options
    )
    if team2_win_any:
        continue
    # Check if team1's conditions hold for all team2's options
    team1_win_all = all(
        (t1_d > t2_a) and (t1_a > t2_d) for t2_a, t2_d in t2_options
    )
    if team1_win_all:
        team1_win = True
        break

if team1_win:
    print("Team 1")
else:
    team2_win_all = True
    for t1_a, t1_d in t1_options:
        team2_has_option = any(
            (t2_d > t1_a) and (t2_a > t1_d) for t2_a, t2_d in t2_options
        )
        if not team2_has_option:
            team2_win_all = False
            break
    if team2_win_all:
        print("Team 2")
    else:
        print("Draw")

Let's test this code against the examples.

First example:

Players input:

1 100 → player0: a=1, b=100

100 1 → player1: a=100, b=1

99 99 → player2: a=99, b=99

99 99 → player3: a=99, b=99

t1_options:

player0's b is 100, player1's a is 100 → (100, 100)

player1's b is 1, player0's a is 1 → (1, 1)

For the first option (100,100):

team2 options are (99,99) and (99,99).

Check team2_win_any:

For each option, check if t2_d (99) > 100 → no and t2_a (99) > 100 → no. So team2_win_any is False.

Then check team1_win_all: for both options, t1_d (100) > 99 (t2_a) → yes. t1_a (100) > 99 (t2_d) → yes. So team1_win_all is True. So team1_win becomes True.

So output Team1.

Second example:

Players:

1 1 → player0: a=1, b=1

2 2 → player1: a=2, b=2

3 3 → player2: a=3, b=3

2 2 → player3: a=2, b=2

t1_options:

Option0: (1,2), option1: (2,1).

Check team2 options:

player2's b is3, player3's a is2 → (3,2).

player3's b is2, player2's a is3 → (2,3).

So team2 options are (3,2) and (2,3).

For team1's option (1,2) → t1_a=1, t1_d=2.

Check team2 options:

For (3,2): t2_d=2 >1 → yes. t2_a=3>2 → yes. So team2 can win. So team1's option is skipped.

Next team1 option: (2,1). t1_a=2, t1_d=1.

Check team2 options:

For (3,2): t2_d=2>2? No. t2_a=3>1 → yes. So (2>2 is false) → team2's conditions are not met.

For (2,3): t2_d=3>2 → yes. t2_a=2>1 → yes. So team2 can win.

Thus, team1 has no valid option.

Check team2_win_all:

For each team1 option:

First team1 option: (1,2):

team2_has_option → check if any team2 option allows win.

Yes: (3,2) allows team2 to win.

So team2_has_option is True.

Second team1 option: (2,1):

team2_has_option → (2,3) allows team2 to win. So yes.

Thus, team2_win_all is True → output Team2.

Third example:

Players:

3 3 → player0: a=3, b=3.

2 2 → player1: a=2, b=2.

1 1 → player2: a=1, b=1.

2 2 → player3: a=2, b=2.

t1_options:

Option0: (3,2) → player0's b=3, player1's a=2.

Option1: (2,3) → player1's b=2, player0's a=3.

team2 options:

player2's b=1, player3's a=2 → (1,2).

player3's b=2, player2's a=1 → (2,1).

Check team1_win:

For option0 (3,2):

team2 options (1,2) and (2,1).

Check team2_win_any:

(1,2): team2_d=2 >3? No. team2_a=1>2? No.

(2,1): team2_d=1>3? No. team2_a=2>2? No. So team2_win_any is False.

Check team1_win_all:

For team2 option (1,2):

t1_d=2 >1 → yes. t1_a=3>2 → yes. So conditions met.

For team2 option (2,1):

t1_d=2 >2 → no. So team1_win_all is False. So this option is invalid.

Next team1 option: (2,3).

Check team2_win_any:

team2's options (1,2) and (2,1).

For (1,2): team2_d=2>2? No. team2_a=1>3? No.

For (2,1): team2_d=1>2? No. team2_a=2>3? No. So team2_win_any is False.

Check team1_win_all:

For (1,2) team2 option: t1_d=3>1 (yes). t1_a=2>2 (no). So conditions not met.

Thus, team1_win_all is False. So team1_possible remains False.

Check team2_possible:

For each team1 option.

First team1 option (3,2):

Check team2_has_option → any team2 options where team2 wins. As above, no.

So team2_has_option is False → team2_win_all becomes False.

Thus, output Draw.

So code works.

Now, code is as written.
</think>

```python
players = [tuple(map(int, input().split())) for _ in range(4)]
t1_options = [(players[0][1], players[1][0]), (players[1][1], players[0][0])]
t2_options = [(players[2][1], players[3][0]), (players[3][1], players[2][0])]

team1_win = False
for t1_a, t1_d in t1_options:
    team2_win_any = any((t2_d > t1_a and t2_a > t1_d) for t2_a, t2_d in t2_options)
    if team2_win_any:
        continue
    team1_win_all = all((t1_d > t2_a and t1_a > t2_d) for t2_a, t2_d in t2_options)
    if team1_win_all:
        team1_win = True
        break

if team1_win:
    print("Team 1")
else:
    team2_win_all = True
    for t1_a, t1_d in t1_options:
        team2_has_option = any((t2_d > t1_a and t2_a > t1_d) for t2_a, t2_d in t2_options)
        if not team2_has_option:
            team2_win_all = False
            break
    print("Team 2" if team2_win_all else "Draw")
```