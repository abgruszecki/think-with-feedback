<think>
Okay, I need to solve this problem. Let's read the problem carefully and understand what's going on.

So, the problem is about simulating a game where teams take turns explaining words from a deck of cards. Each team has two players. The order of turns is first all the first players of each team in order, then all the second players, and this repeats. Each turn lasts t seconds. When a player takes a card, they explain it for some time. The time they take depends on the card's complexity, their skills, and previous attempts. If they can explain it within the remaining time, the card is removed, the team gets a point. Otherwise, the card is put back at the bottom, and the time spent is recorded for next time.

The goal is to simulate this process and output for each team the number of points and the words they guessed in order.

Hmm. So the main challenge here is to model the game step by step, keeping track of all the necessary variables. Let's break down the problem.

First, the input:

- n teams, each with two players (each with aij and bij).
- m cards, each with a word and a complexity ck.
- The deck starts in a certain order. The order of play is first player 1 of each team in order, then player 2 of each team, then repeat.

Each turn starts with t seconds. For each card taken from the top of the deck:

Compute the time needed to explain it. For the current player (team i, player j), the teammate is q (the other player). So the time needed is max(1, ck - (aij + biq) - dik), where dik is the time already spent on this card by team i. Initially, dik is 0 for all.

Then, check if the remaining time in the current turn is >= this time. If yes:

- Subtract the time from the remaining time.
- The team gains the card (add to their points and list).
- Remove the card from the deck (so it's not part of future turns).
- Continue the turn until time runs out.

If not enough time:

- The time spent during this turn (the remaining time) is added to dik.
- The card is put at the bottom of the deck.
- The remaining time becomes zero, so the turn ends.

The game ends when all cards are guessed.

So the steps are:

1. Simulate the turns in the correct order of players (player 1 of each team, then player 2, repeating).
2. For each player's turn, process the deck's cards until time runs out.
3. Track which cards each team has collected, and the order.

Now, considering the constraints: n and m up to 100. Time limit per test is 1 second. So the algorithm's time complexity needs to be manageable for these sizes.

Wait, m can be up to 100. So for each card, each team's dik can be tracked. Let's see. For each team and each card, we need to track how much time they've spent on it. So a dictionary or a 2D array: dik is an array of size n x m. So for n=100 and m=100, that's 10,000 entries. That's manageable.

The deck is a queue of cards. Each card is processed in order. When a card is not guessed, it's placed at the bottom of the deck. So we can model the deck as a deque (double-ended queue) where we pop from the front and append to the back when needed.

But wait, when a team starts a turn, they take cards from the top until the time runs out. So during a player's turn, they take a card, process it. If the card is guessed (time is sufficient), then it's removed. Otherwise, it's appended back to the end (but perhaps other teams may have processed other cards in between). So the deck is a dynamic structure, and we need to process it in the order of the cards as they are.

But each turn is handled by the current player, and the deck is processed in the order they take the cards. For example, during a player's turn:

Time left = t.

While time left >0:

- Take the first card from the deck.

- Compute the time needed for this card. For the current team, player j, and their teammate q.

- time_needed = max(1, ck - (aij + biq) - dik)

- If time_needed <= time_left:

   - team gains the card. Add to their list.

   - subtract time_needed from time_left.

   - dik for this team and card is now increased by time_needed (but since the card is removed, maybe not necessary to track anymore?)

   - the card is removed from the deck.

- Else:

   - time_spent = time_left.

   - dik for the team and card increases by time_spent.

   - the card is put back to the end of the deck.

   - time_left becomes 0.

This process continues until time_left is 0.

So the key points are:

- Each team has a dictionary (or array) tracking the accumulated time they have spent on each card (dik).

- The deck is a deque that changes as cards are processed and either removed or placed at the end.

- The order of players is a cycle: player 1 of each team (1 to n), then player 2 of each team (1 to n), then repeat.

Now, the steps for the simulation:

1. Initialize the deck as a deque of the cards in their initial order. Each card should have its word, ck, and perhaps an index to track which card it is (since words are unique, maybe the word is the identifier). But since m can be 100, and each card is unique, perhaps we can track the cards as objects with their word, ck, and for each team, their accumulated time on it.

Wait, but for each team and card, we need to track dik. So perhaps we can have a 2D array (teams x cards) where each entry is the total time spent by that team on that card. Then, when processing a card, for the current team, we look up their dik in this array.

So for each card, when processed by a team, the current team's dik is retrieved, and the time_needed is computed. Then, if the card is not guessed, the team's dik is updated by adding the time_spent (time_left in that case). If the card is guessed, the team's dik is updated by the time_needed (but since the card is removed from the deck, perhaps we don't need to track it anymore. But once a card is removed, it's no longer in the deck, so other teams can't process it again. So once a card is guessed by a team, it's removed from the deck and no longer part of the game. So for the dik, once a card is removed, the entries for other teams' dik are irrelevant.

So the initial steps:

- Read all the cards, store them in a list. Each card has word, ck. Also, perhaps assign each card a unique index (0 to m-1) to track in the dik array.

- The deck is a deque of these card objects (or their indices, perhaps, to make it efficient).

- For each team i, and each card k, we have a dik value. So a 2D array: d = [[0 for _ in range(m)] for _ in range(n)].

Wait, but m can be up to 100, and n up to 100. So 100*100=10,000 entries. That's acceptable.

Then, the order of play is:

The players take turns in the order: team 1's player 1, team 2's player 1, ..., team n's player 1, then team 1's player 2, team 2's player 2, ..., team n's player 2, then back to team 1's player 1, and so on.

So the order of players is a list that cycles through each team's players in this order. So for each turn, we can track the current player index. The order is:

Players are ordered in rounds. Each round has n * 2 players. The first n are the first players of each team (in team order 1 to n), then the next n are the second players of each team (again 1 to n). Then it repeats.

Wait, no. Wait, the problem says:

Each turn continues for t seconds. The order is:

the 1-st player of the 1-st team, the 1-st player of the 2-nd team, ..., the 1-st player of the n-th team, the 2-nd player of the 1-st team, ..., the 2-nd player of the n-th team, then back to 1-st players again, etc.

So the order of players is a cycle of the sequence:

1st players of all teams in order, then 2nd players of all teams in order, then repeat.

So the order is team 1's player 1, team 2's player 1, ..., team n's player 1, then team 1's player 2, team 2's player 2, ..., team n's player 2, then again team 1's player 1, etc.

So each player's turn comes in a certain order. So for each turn, we need to track which player (team and player index) is taking the turn.

So for example, the first player to take a turn is team 1, player 1. Then team 2, player 1. Then team 3, player 1, etc. Then after all first players, it's the second players in the same team order.

Thus, the order of players can be generated as a cycle. Each step in the cycle is a player (team i, player j), where j is 1 or 2, and the order is such that all first players go first, then all second players, then repeat.

So how to model this cycle?

We can create a list of players in the order of turns. The list would be:

[(0, 0), (1, 0), ..., (n-1, 0), (0, 1), (1, 1), ..., (n-1, 1), (0, 0), (1, 0), etc.]

But since the game could take a long time (until all m cards are processed), but m is up to 100, and each card requires at least one turn (since the time needed is at least 1, and t could be 100, so perhaps some cards are processed quickly), the total number of turns is manageable.

But perhaps the best way is to generate the order as a cycle. For each turn, we can track the current position in the cycle. For example, the cycle is a list of (team index, player index). The cycle is generated as:

for player_j in 0, 1 (since j=1 and 2, but maybe 0-based indices here?), then for each team in 0..n-1, add (team, player_j) to the cycle. Then repeat this.

Wait, no. The order is first all the first players (j=1) of each team in order 1 to n, then all the second players (j=2) in the same team order. Then repeat.

So the cycle for the players is:

team order is 1 to n, but in code, perhaps 0-based. So the order is:

for j in 0 (player 1), then 1 (player 2):

   for each team in 0..n-1:

      player (team, j)

But this would cycle through j=0, then j=1, then j=0, etc. Wait, no. The order is first all j=0 (player 1) for all teams, then j=1 (player 2) for all teams, then j=0 again, etc.

So the cycle is:

j alternates between 0 and 1. But the cycle is:

player_j starts as 0. For each team in 0..n-1: (team, 0).

Then player_j is 1. For each team in 0..n-1: (team, 1).

Then repeat.

So the order is a list that is generated as follows:

while True:

   for j in 0, 1:

      for i in 0 to n-1:

         yield (i, j)

Wait, no. Because in each round, the first players (j=0) of all teams take their turns first, then the second players (j=1) of all teams. Then the cycle repeats with j=0 again.

So the cycle is: first, j=0 for all teams, then j=1 for all teams, then j=0 again for all teams, etc.

But how to model this as a cycle?

Each full cycle has 2n turns (n teams for j=0, then n teams for j=1). So the cycle is infinite, repeating these 2n steps. So for the simulation, each turn is determined by the step in the cycle.

So to track the current player, we can have a variable that cycles through 0 to 2n-1, incrementing each time a turn is taken, and wrapping around modulo 2n. Then, for each step in the cycle, the player is determined by:

current_cycle_step = step % (2n)

if current_cycle_step < n: j=0, team = current_cycle_step

else: j=1, team = current_cycle_step - n

Wait, no. Because for 2n steps, the first n steps are j=0 (player 1) for each team 0 to n-1. Then the next n steps are j=1 (player 2) for each team 0 to n-1. Then step 2n would be j=0 again.

So for example, n=2:

step 0 → team 0, j=0

step 1 → team 1, j=0

step 2 → team 0, j=1

step 3 → team 1, j=1

step 4 → team 0, j=0

etc.

So for step s, the team and j can be determined by:

cycle = s % (2n)

if cycle < n: j=0, team = cycle

else: j=1, team = cycle - n

Yes. So in code, for each step (turn), we can compute the current team and j (player index).

So the steps for simulation:

1. Read all input data: teams' a and b values, and the cards.

2. Initialize the deck as a deque containing the cards in their initial order.

3. For each team i, and card k, track dik (time spent on card k by team i). Initialize to 0.

4. For each team, track their collected words (list) in order.

5. Simulate the game until the deck is empty (all cards are guessed).

6. For each turn:

   a. Determine the current team and player (j) based on the step in the cycle.

   b. The player's turn starts with t seconds.

   c. While there are cards in the deck and remaining_time >0:

      i. Take the first card from the deck.

      ii. Compute the teammate q. For the current player j (0 or 1), q is 1-j (since j=0 → q=1, j=1 → q=0).

      iii. aij is the player's a value. biq is the teammate's b value.

      iv. time_needed = max(1, ck - (aij + biq) - dik[team][card_index])

      v. if time_needed <= remaining_time:

         - The team guesses the card. Add the word to their list.

         - Subtract time_needed from remaining_time.

         - Update dik[team][card_index] += time_needed (though since the card is removed, this might not be needed, but perhaps it's irrelevant once the card is removed.)

         - Remove the card from the deck. (Since it's processed and guessed.)

      else:

         - time_spent = remaining_time

         - dik[team][card_index] += time_spent

         - remaining_time = 0

         - Put the card back at the end of the deck.

      d. Repeat until deck is empty or remaining_time is 0.

   d. If the deck is empty, break out of the loop.

So the simulation must loop over each turn, in the correct order, until all cards are processed.

Now, the main data structures:

- deck: deque of card objects. Each card has a word, ck, and index (if needed). Alternatively, since the cards are processed in order, perhaps each card can be represented as a dictionary or a tuple. But since the order in the deck can change (cards are moved to the end when not guessed), perhaps each card should be stored with their index (from 0 to m-1) so that we can quickly look up their ck and word.

Wait, but when a card is processed, we need to know its ck. So perhaps during input, each card is stored with its word and ck. Then, when processing, for each card in the deck, we can refer to its ck.

But how to track the card's index for the dik array?

Wait, during input, the cards are given in order. So the first card is index 0, second 1, etc. So when reading the input, we can assign each card a unique index (k from 0 to m-1). Then, when a card is processed (taken from the deck), we can get its index, and use that to access dik for the current team.

So, the steps for input:

Read m cards. For each card, read two lines: the word and ck.

So for example, for the first sample input:

3 cards:

home (ck=1), index 0

car (ck=1), index 1

brother (ck=1), index 2

The deck is deque([0,1,2]) initially.

Then, as the deck is processed, cards are removed when guessed, or placed at the end when not.

So each card in the deck is represented by its index. So the deck is a deque of indices. The ck and word can be stored in a list where the index is the card's index.

So in code:

cards = []
for k in range(m):
    word = input().strip()
    ck = int(input())
    cards.append( (word, ck) )

Then, the deck is deque([0,1,2,...]).

Then, for each card index in the deck, we can get its ck and word via cards[k][0] and cards[k][1].

So now, when processing a card (k):

For the current team, aij is team's player j's a, biq is team's player q's b.

Then time_needed is max(1, cards[k][1] - (aij + biq) - dik[team][k])

So the dik array is a 2D list of size n x m, initialized to 0.

Now, the code structure.

The simulation loop:

Initialize deck as deque of card indices in order.

Initialize dik as a list of lists: [[0] * m for _ in range(n)]

Each team's points and words are stored in a list of lists: results = [[] for _ in range(n)]

current_turn = 0  # step counter to determine the order.

while deck is not empty:

   # determine which team and player's turn it is.

   cycle_step = current_turn % (2 * n)

   if cycle_step < n:

       team = cycle_step

       player_j = 0  # 0-based, corresponds to player 1 in the problem statement.

   else:

       team = cycle_step - n

       player_j = 1  # player 2.

   # Now, team is 0-based, player_j is 0 or 1.

   # Get the teammate's index (q is 0 or 1, the other player)

   q = 1 - player_j

   aij = teams[team][player_j][0]

   biq = teams[team][q][1]

   remaining_time = t

   # process the player's turn.

   while remaining_time > 0 and deck:

       card_index = deck.popleft()

       ck = cards[card_index][1]

       # get the current dik for this team and card.

       current_dik = dik[team][card_index]

       time_needed = max(1, ck - (aij + biq) - current_dik)

       if time_needed <= remaining_time:

           # team guesses the card.

           results[team].append( cards[card_index][0] )

           # update dik (though not necessary, since the card is removed)

           dik[team][card_index] += time_needed

           remaining_time -= time_needed

       else:

           # not enough time. add to dik, put back card, subtract remaining_time.

           time_spent = remaining_time

           dik[team][card_index] += time_spent

           # put the card back at the end.

           deck.append(card_index)

           remaining_time = 0

       # after processing, check if the deck is empty.

       # because if the card was guessed and removed, and deck is now empty, break.

   current_turn += 1

Once the deck is empty, the simulation ends.

Then, for each team in 0..n-1, output the number of words and the words in order.

Now, edge cases to consider:

- What if during a turn, a player processes multiple cards? For example, if t is very large and each card takes 1 second. Then a player can process several cards in their turn.

- The order of the deck must be maintained correctly. For example, when a card is put back, it's at the end. So other cards in the deck are processed first.

Now, testing against the sample input.

Sample 1:

Input:

2 2

1 1 1 1

1 1 1 1

3

home

1

car

1

brother

1

Sample output:

2 home car

1 brother

Let's see.

Teams 0 and 1 (0-based). Each team's players have a and b values (a11=1, b11=1, a12=1, b12=1 for team 1 in input). Wait, the input for teams is:

First line: ai1, bi1, ai2, bi2 for team 0.

Second line: same for team 1.

So for team 0:

player 0 (j=0) has a=1, b=1.

player 1 (j=1) has a=1, b=1.

Same for team 1.

Cards are home (ck=1), car (ck=1), brother (ck=1).

Deck is deque([0,1,2]).

Simulation:

current_turn starts at 0.

cycle_step is 0 % (2*2=4) → 0.

cycle_step < 2 (n=2), so team 0, player 0.

remaining_time = 2.

Processing:

card 0 (home, ck=1).

aij (team 0, j=0) a=1, biq (q=1) → biq is 1.

time_needed = max(1, 1 - (1+1) - 0) → max(1, -1) → 1.

remaining_time is 2 >=1. So subtract 1, remaining_time becomes 1.

Team 0's results get 'home'.

Deck is now deque([1,2]).

Next, remaining_time is 1. Take card 1 (car, ck=1).

time_needed for team 0, player 0: 1 - (1+1) -0 = -1 → max 1.

remaining_time 1 >=1 → subtract 1. Remaining_time 0.

Team 0's results add 'car'.

Deck becomes deque([2]).

current_turn increments to 1.

Now, next turn: cycle_step 1 (1%4=1 <2). Team 1, player 0.

remaining_time is 2.

Process deck [2]. card 2 (brother, ck=1).

time_needed: 1 - (1+1) -0 → 1-2= -1 → max 1.

remaining_time 2 >=1 → subtract 1. Team 1 adds 'brother'. Deck is empty.

But wait, the sample output shows team 0 has 2 points (home and car), team 1 has 1 (brother). But according to the first sample's output, team 2 (the second team) has 1 point. Wait wait, in the sample input, the first sample output is:

2 home car

1 brother

So team 1 (second team) has 1 point. But according to the simulation here, team 1's player 0 takes the turn (current_turn=1) and processes card 2 (brother) in their turn. Then deck is empty, so the game ends. So team 1 has one card. Team 0 has two.

So the sample output matches.

Another sample:

Input:

2 4

1 2 2 1

2 3 2 2

4 cards:

armchair (3), quetzalcoatl (10), pilotage (5), defibrillator (7).

Output is team 1 has 2 cards, team 2 has 2.

But according to the order:

Let's see. Let's model the steps.

But perhaps for the purposes of code, the code should handle all these steps correctly.

Now, code structure.

Read n and t.

Read n teams. For each team, read ai1, bi1, ai2, bi2. So for each team, we can store a list of two players, each with a and b. So teams is a list of lists. For team i, players are [ [ai1, bi1], [ai2, bi2] ].

Then read m. Read m pairs of lines (word, ck). Store as a list of tuples, cards.

Then initialize deck as deque of card indices (0 to m-1).

Initialize dik as a 2D array of n rows and m columns, all 0.

Initialize results as list of empty lists.

current_turn starts at 0.

Loop while deck not empty:

   compute cycle_step = current_turn % (2*n)

   team = cycle_step // 1? No. Wait, as earlier:

   if cycle_step < n → team = cycle_step, j=0.

   else → team = cycle_step -n, j=1.

So code:

cycle_step = current_turn % (2 * n)

if cycle_step < n:

    team = cycle_step

    j = 0

else:

    team = cycle_step - n

    j = 1

q = 1 - j

aij = teams[team][j][0]

biq = teams[team][q][1]

remaining_time = t

then process the deck:

while remaining_time >0 and deck:

   card_index = deck.popleft()

   ck = cards[card_index][1]

   current_dik = dik[team][card_index]

   time_needed = max(1, ck - (aij + biq) - current_dik)

   if time_needed <= remaining_time:

       # guessed

       results[team].append(cards[card_index][0])

       dik[team][card_index] += time_needed

       remaining_time -= time_needed

   else:

       # not guessed

       time_spent = remaining_time

       dik[team][card_index] += time_spent

       deck.append(card_index)

       remaining_time = 0

current_turn +=1

Once all cards are processed, output the results.

So now, code.

Now, possible optimizations. For m=100 and n=100, and each card requiring several steps, the code may need to process up to m * (some steps per card) but given that the time per card is up to 100 steps, but 1e4 operations should be manageable.

Now, let's code this.

Testing the first sample:

Sample 1:

n=2, t=2.

teams:

team 0: ai1=1, bi1=1, ai2=1, bi2=1.

team 1: same.

cards:

3 cards: home (1), car (1), brother (1).

Deck starts as [0,1,2].

First turn (current_turn=0):

cycle_step=0 <2 → team 0, j=0.

q=1.

aij = 1, biq=1.

remaining_time=2.

Process card 0: ck=1.

time_needed = max(1, 1 - (1+1) -0 ) → max(1, -1) →1.

remaining_time 2-1=1. Card is added to team 0's results. deck is [1,2].

Next card 1: ck=1.

time_needed same →1. remaining_time becomes 0. team 0 adds 'car'. deck is [2].

current_turn becomes 1.

Next turn: cycle_step=1 <2 → team 1, j=0.

remaining_time=2.

card 2: ck=1.

time_needed 1 - (1+1) -0 = -1 →1.

remaining_time 2-1=1. card is added to team1's results. deck becomes empty.

current_turn increments to 2.

But deck is empty. So loop breaks.

Output is team 0 has 2 words (home, car), team1 has 1 (brother). Which matches the sample.

Another sample:

Sample 2:

Input:

2 4

1 2 2 1

2 3 2 2

4 cards:

armchair (3)

quetzalcoatl (10)

pilotage (5)

defibrillator (7)

The output is:

2 armchair quetzalcoatl

2 pilotage defibrillator

So team 0 (first team) gets two cards, team 1 (second) gets two.

Let's see how this happens.

Teams:

team 0:

player 0: a=1, b=2

player 1: a=2, b=1

team 1:

player 0: a=2, b=3

player 1: a=2, b=2

Cards:

indices 0,1,2,3.

Deck starts as [0,1,2,3].

Let's simulate the turns.

Turn 0 (current_turn=0):

cycle_step=0 <2 → team 0, j=0.

q=1.

aij=1, biq=1 (player 1's b is 1).

remaining_time=4.

Process card 0 (armchair, ck=3).

time_needed = max(1, 3 - (1+1) -0) →3-2=1 →max 1.

4 >=1. time left 3.

Team 0 adds armchair. deck becomes [1,2,3].

Next card 1 (quetzalcoatl, ck=10).

time_needed: 10 - (1+1) -0 =8. max(1,8)=8. 3 <8: no.

So time_spent=3. dik[0][1] +=3 →3.

card is appended to deck. deck becomes [2,3,1]. remaining_time is 0.

So team 0's results: [armchair]

current_turn increments to 1.

Turn 1 (current_turn=1):

cycle_step=1 <2 → team 1, j=0.

q=1.

aij=2 (player 0's a), biq=2 (player 1's b).

time_needed for card 2 (pilotage, ck=5):

5 - (2 +2) -0 =1. time_needed=1.

remaining_time=4. Subtract 1 →3. Team1 adds pilotage. deck becomes [3,1].

Next card 3 (defibrillator, ck=7).

time_needed:7 - (2+2) -0=3. 3 <=3. team1 adds defibrillator. time left 0. deck becomes [1].

current_turn increments to 2.

deck is [1].

Turn 2 (current_turn=2):

cycle_step=2 %4=2 >=2 → team 0 (2-2=0), j=1.

q=0.

aij=2 (player1's a), biq=2 (player0's b).

remaining_time=4.

card 1 (quetzalcoatl, ck=10).

current_dik for team0:3 (from previous attempt).

time_needed:10 - (2 +2) -3 =10-4-3=3. max(1,3) →3.

4 >=3 → subtract 3 →1 left. team0 adds quetzalcoatl. deck is empty.

So team0's results are [armchair, quetzalcoatl].

Team1's results are [pilotage, defibrillator].

Thus, the sample output matches.

So the code should handle these cases correctly.

Now, code.

But code needs to read input and process the cards correctly.

Edge cases:

- What if the time needed is exactly the remaining time? Then subtract and proceed.

- What if a card is in the deck but not guessed by any team for several turns?

Now, code.

Implementing in Python.

But note that for the deck, we need to use a deque for efficient pops from the front and appends to the end.

Also, the card indices are from 0 to m-1.

So code:

import sys
from collections import deque

n, t = map(int, input().split())
teams = []
for _ in range(n):
    a1, b1, a2, b2 = map(int, input().split())
    teams.append([(a1, b1), (a2, b2)])

m = int(input())
cards = []
for _ in range(m):
    word = input().strip()
    ck = int(input())
    cards.append((word, ck))

deck = deque(range(m))
dik = [[0]*m for _ in range(n)]
results = [[] for _ in range(n)]
current_turn = 0

while deck:
    cycle_step = current_turn % (2 * n)
    if cycle_step < n:
        team = cycle_step
        j = 0
    else:
        team = cycle_step - n
        j = 1
    q = 1 - j
    aij, bij_teammate = teams[team][j][0], teams[team][q][1]
    remaining_time = t
    while remaining_time > 0 and deck:
        card_index = deck.popleft()
        ck = cards[card_index][1]
        current_dik = dik[team][card_index]
        time_needed = max(1, ck - (aij + bij_teammate) - current_dik)
        if time_needed <= remaining_time:
            # guessed
            results[team].append(cards[card_index][0])
            dik[team][card_index] += time_needed
            remaining_time -= time_needed
        else:
            # not guessed
            time_spent = remaining_time
            dik[team][card_index] += time_spent
            deck.append(card_index)
            remaining_time = 0
    current_turn += 1

for res in results:
    print(len(res), end=' ')
    print(' '.join(res))

This code should handle the problem.

Testing the first sample:

Yes.

In code, team is 0-based. So in the first sample, the first team is team 0, second team is team 1.

The output is team 0's results first, then team1's.

Which matches the sample.

Another test case.

Now, possible optimizations:

- Using deque is efficient.

But since m is small, no problem.

What about the dik array? For each card and team, storing the accumulated time. Even for m=100 and n=100, it's 10,000 entries. Which is manageable.

The code reads inputs correctly, processes each turn in order.

Yes.

So this code should work.
</think>

```python
import sys
from collections import deque

n, t = map(int, sys.stdin.readline().split())
teams = []
for _ in range(n):
    a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
    teams.append([(a1, b1), (a2, b2)])

m = int(sys.stdin.readline())
cards = []
for _ in range(m):
    word = sys.stdin.readline().strip()
    ck = int(sys.stdin.readline())
    cards.append((word, ck))

deck = deque(range(m))
dik = [[0] * m for _ in range(n)]
results = [[] for _ in range(n)]
current_turn = 0

while deck:
    cycle_step = current_turn % (2 * n)
    if cycle_step < n:
        team = cycle_step
        j = 0
    else:
        team = cycle_step - n
        j = 1
    q = 1 - j
    aij = teams[team][j][0]
    biq = teams[team][q][1]
    remaining_time = t
    while remaining_time > 0 and deck:
        card_idx = deck.popleft()
        ck_val = cards[card_idx][1]
        current_d = dik[team][card_idx]
        time_needed = max(1, ck_val - (aij + biq) - current_d)
        if time_needed <= remaining_time:
            results[team].append(cards[card_idx][0])
            dik[team][card_idx] += time_needed
            remaining_time -= time_needed
        else:
            time_spent = remaining_time
            dik[team][card_idx] += time_spent
            deck.append(card_idx)
            remaining_time = 0
    current_turn += 1

for res in results:
    print(len(res), end=' ')
    print(' '.join(res))
```