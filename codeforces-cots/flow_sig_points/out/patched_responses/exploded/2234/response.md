<think>
Okay, let's see. I need to solve this problem where two teams are playing Quidditch, and I have to track the score based on the actions in each step. The main thing is to process all the steps correctly and detect when a goal is scored. Hmm.

First, let me read the problem statement again carefully. The key points are:

- The Quaffle starts somewhere on the field. Players can catch it, move with it, throw it. When it's thrown or released, if it's left on a goal of the opposing team (or their own?), a goal is scored. Wait, no: the problem says, when a player leaves the Quaffle at a goal of the other team. Oh, but if a player puts it in their own goal, the other team gets the point. So for example, if a red player leaves the Quaffle in a red goal (RG), then the blue team gets the point. Because the other team is the one that's supposed to target that goal. So the scoring is determined by which team's goal the Quaffle is placed in. So, RG is a red goal. So blue team wants to put the Quaffle there, and red team wants to put it in BG. But if a red player leaves it in RG, that's their own goal, so blue gets a point. Got it.

Each step is an action by an entity (player or ball). The Quaffle's position is tracked, and whether a player is holding it. When a player catches the Quaffle (C .Q), they start carrying it. Then, any movement by the player moves the Quaffle along with them. When they throw it (T), the Quaffle is placed at their current position. At that point, we check if that position is a goal. If so, the appropriate team gets the point, and the Quaffle is moved to the middle.

So the steps to model are:

1. For each action in order, process it.
2. After processing the action, check if the Quaffle is at a goal cell (RG or BG) and is not being carried. Because when it's thrown (T) or when a player moves and then maybe leaves it (but during movement, if the player is holding the Quaffle, the Quaffle's position is same as the player's). Wait, the Quaffle's position is only updated when the player moves if they are carrying it. So when a player moves while holding the Quaffle, the Quaffle's position is the same as the player's.

Wait, when a player is carrying the Quaffle, the Quaffle's position is wherever the player is. So during movement, as the player moves, the Quaffle moves with them. But if the player is not carrying the Quaffle, then the Quaffle's position is tracked separately.

So, the Quaffle can be in two states: either being carried by a player, or free on the field.

So I need to track:

- The current position of the Quaffle. If it's being carried, then its position is the same as the player who's holding it. Otherwise, it's at a certain cell.

- Which player (if any) is currently holding the Quaffle.

So, for each step, when an action is performed, we need to update the state accordingly. Then, after the action, check if the Quaffle is in a goal cell and not being carried (i.e., it was thrown there or left there after a movement, but not held). If so, process the goal.

So the steps for processing each action:

For each action in order t from 0 to T-1:

1. Process the action. This involves moving the entity (player or ball), catching, or throwing.

   a. If the entity is a player, and the action is movement (U/D/L/R), move the player (and if they are carrying the Quaffle, the Quaffle's position is updated to the new position). Also, if the entity is the Quaffle (if it's moving, but according to the problem statement, the Quaffle can only move when it's not being carried. Because when it's carried, the player moves and the Quaffle follows. So the Quaffle's movement actions are only when it's free. Wait, but in the problem statement, the Quaffle is an entity that can perform an action (like move). Wait, the problem says: each step, one entity (player or ball) performs an action.

   Wait, the problem says: "each step, one entity on the field (a player or a ball) performs one action. All entities can move. A player can also catch a ball or throw the Quaffle that it is carrying."

   So, the Quaffle (as a ball) can perform actions. For example, in a step, the Quaffle can move (if it's not being carried). So in that case, the Quaffle's position is updated.

   So when the Quaffle is not being carried, it can move. When it's being carried, the player's movement moves it. But the Quaffle's own movement actions would only occur when it's not being carried.

   So, during processing of each action:

   - The entity is either a player (like R0, B1), or a ball (like .Q).

   So, the action processing must account for all possibilities.

   But according to the input, the first part of each action line is the entity's identifier (pair of characters). For example, in the first example, the first action is "B2 U" which is a player moving up.

   So, for each action:

   - Identify which entity is performing the action.

   Then, process that action:

   Case 1: Entity is a player.

   - The player can move, catch a ball, or throw.

   Case 2: Entity is the Quaffle (i.e., the entity is .Q). Then the action must be a movement (U/D/L/R), since catching and throwing are player-only actions.

   But according to the problem statement, the Quaffle can perform actions (movement) when it's not being carried. So during such steps, the Quaffle moves on its own.

   So, the steps are:

   For each action:

   If the entity is a player (e.g., R0):

   - If action is movement (U, D, L, R): move the player in that direction. If the player is holding the Quaffle, then the Quaffle's position is updated to the player's new position. Also, check if after moving, the Quaffle is in a goal cell. But wait, no. Because the player is carrying the Quaffle, so the Quaffle's position is the same as the player's. But a goal is scored only when the Quaffle is left (not carried) in a goal. So while being carried, even if the player is in a goal cell, no goal is scored. Only when the Quaffle is placed (thrown or left after movement when not caught) in a goal cell.

   So, after the action is processed (movement, catch, throw), check if the Quaffle is in a goal cell and not being carried.

   So the key is to check after each action whether the Quaffle is in a goal cell and not being held.

   So, for each action step:

   Process the action. Then, check if the Quaffle is in a goal cell and is not being held by a player. If so, that's a goal. Then, process the goal (add points, reset Quaffle to middle, and output the event).

   Wait, but according to the problem statement, when a player puts the ball into a goal, the Quaffle is instantly moved to the middle. So in that case, the check is done right after the action. So how do we track when the Quaffle is placed in a goal.

   Let me think about the sequence of events:

   For example, when a player throws the Quaffle (T action). After throwing, the Quaffle is placed at their current position. So if that position is a goal cell, then a goal is scored. So after processing the T action, we check where the Quaffle is (now it's not being carried). If that position is a goal cell, then process the goal.

   Similarly, if the Quaffle moves on its own (like when it's not carried and has a move action), then after moving, check if it's in a goal cell.

   So the steps are:

   1. Process the action, which may update the position of the Quaffle and/or whether it's being held.

   2. Check if the Quaffle is not being held and is in a goal cell. If yes, then:

      a. Determine which team scored (the other team's goal). For example, if the Quaffle is in RG (red goal), then the blue team scores. If in BG (blue goal), red team scores.

      b. Increment the appropriate score.

      c. Output the current step (t) and the team that scored.

      d. Move the Quaffle to the middle of the field.

   Also, note that if the Quaffle is moved into a goal cell in the same step as being thrown or moved, the goal is processed immediately, and the Quaffle is moved to the middle. So even if the action was moving the Quaffle into a goal, it's detected and handled.

   Now, the main challenge is to model the state of the Quaffle (held or not, and if held, by whom), the positions of all entities (players, Quaffle, goals), and process each action correctly.

   Let's think about the data structures:

   - The field has cells that can contain goals. We need to know for each cell whether it's a goal (RG or BG), which can be stored in a grid. So maybe a grid of N rows and M columns, where each cell has info about any goals present.

   But since multiple entities can be in the same cell, but goals are static. So perhaps we can pre-process the goals into a separate structure.

   So, create a dictionary or a grid where for each (x, y) cell, we know if it's a RG, BG, or neither. That way, when checking the Quaffle's position after an action, we can quickly determine if it's in a goal.

   The players' positions are dynamic. Each player (R0, R1, etc., B0, B1, etc.) has a position. So perhaps a dictionary mapping player identifiers (like 'R0') to their (x, y) position. Similarly for the Quaffle's position and whether it's held.

   So, data structures:

   - goals: a grid (list of lists) indicating for each cell, whether it's RG, BG, or None.

   - players: a dictionary where keys are player identifiers (like 'R0') and values are their current (x, y) positions.

   - quaffle_holder: a variable that holds the identifier of the player holding the Quaffle, or None if it's free.

   - quaffle_pos: the current position of the Quaffle. If it's held, this is the same as the holder's position, but we can update it when the holder moves.

   Wait, perhaps it's better to track the Quaffle's position as either being held by a player (so quaffle_holder is the player's ID) or being at quaffle_pos. So whenever the holder moves, the Quaffle's position is updated to the holder's new position. When it's thrown, quaffle_holder becomes None, and quaffle_pos is set to the holder's current position.

   So during movement steps:

   - If the entity is a player, and they move, update their position. If they are holding the Quaffle, then the Quaffle's position is updated.

   - If the entity is the Quaffle (not held), then moving it changes its position.

   For catching:

   - The player catches the Quaffle. So check if they are in the same cell as the Quaffle (when not held). Then set quaffle_holder to the player.

   For throwing:

   - The player releases the Quaffle. So set quaffle_holder to None, and set quaffle_pos to the player's current position.

   So, the steps for processing each action:

   Let's outline each possible action type:

   For the entity in the action:

   If the entity is a player:

   - If action is movement (U/D/L/R):

      - Compute the new position based on direction.

      - Update the player's position.

      - If the player is holding the Quaffle (quaffle_holder is this player), then update the Quaffle's position to the new position.

   - If action is catching (C .Q):

      - The player must be in the same cell as the Quaffle (which is not held by anyone). Then, set quaffle_holder to this player.

   - If action is throwing (T):

      - The player must be holding the Quaffle. Set quaffle_holder to None, and quaffle_pos to the player's current position.

   If the entity is the Quaffle (entity is .Q):

   - The action must be a movement (U/D/L/R).

   - Check if the Quaffle is not held (quaffle_holder is None). Then, move it in the direction.

   Then, after processing the action, check if the Quaffle is in a goal cell and not held. If so:

   - Determine which type of goal (RG or BG). Then, the team that scored is the opposite of the goal's team. For example, if the Quaffle is in RG (red goal), then the blue team scores. If in BG, red team scores. Unless it's a player putting it in their own goal, which is the same logic.

   So, if the Quaffle is in RG, the scoring team is blue. If in BG, the scoring team is red.

   Then, increment the score, add the event to the output list, and move the Quaffle to the middle. Also, since after moving it to the middle, the Quaffle is not held by anyone.

   Now, to model all of this, we need:

   - Read the initial field setup to get players' starting positions, goals, and initial Quaffle position.

   - For each step, parse the entity and action, update the state accordingly.

   So, first step: parsing the input.

   The input starts with N and M. Then N lines, each with M pairs of characters. For each cell (i, j) in the grid (0-based or 1-based?), the pairs are the contents.

   Wait, the problem says: positions are integers. For example, the middle is at ( (M+1)/2 -th column of (N+1)/2 -th line, starting from 1). So, assuming 1-based indices for rows and columns.

   So, for a 5x5 grid, middle is at line (5+1)/2=3, column (5+1)/2=3. So (3,3) in 1-based, which is (2,2) in 0-based.

   So when moving entities, we need to make sure that movement is allowed (the problem says the actions are guaranteed to be valid, so we don't need to handle invalid moves. So we can safely process the action as per the input.

   So, during initial setup:

   Read each line of the grid, split into M pairs. For each pair, check if it's a player, a goal, the Quaffle, or empty.

   For players (like R0, B1), store their initial positions.

   For goals (RG, BG), store in a grid (we can have multiple goals in the same cell? The problem says: the field contains goals for each team (each can have 1-5). So the initial setup can have multiple goals. But the goals are stored in their cells. So for each cell (x, y), note if it's RG, BG, or neither.

   The Quaffle's initial position is where the .Q is found.

   Now, the players' initial positions are where their identifiers are in the grid.

   So, the steps for initial processing:

   - Read N and M.

   - Read N lines. For each line, split into M pairs.

   - For each cell (i, j) (0-based?), iterate through the pairs. Wait, each line represents a row. So for row i (0-based?), the line has M pairs. Each pair is the content of cell (i, j) for j from 0 to M-1.

   Wait, the problem says "N lines of M pairs of characters". So for each line (i from 0 to N-1), each of the M columns (j from 0 to M-1) has a pair.

   So, for example, in the first sample input:

   The third line (0-based index 2) is "RG R0 .Q B0 BG". So for row 2 (third line), columns 0 to 4 (5 columns) are:

   (0,2): RG (red goal)
   (1,2): R0 (red player 0)
   (2,2): .Q (Quaffle)
   (3,2): B0 (blue player 0)
   (4,2): BG (blue goal)

   So for each cell (row, column) in 0-based, we process the pair.

   So, the initial setup:

   - For each cell (i, j):

      pair = grid[i][j]

      if pair is 'RG' or 'BG', then add (i, j) to the goals grid as that type.

      if pair starts with R or B followed by a digit, it's a player. So, add to players dictionary: key is the pair (e.g., 'R0'), value is (i, j).

      if pair is '.Q', then initial quaffle_pos is (i, j), and quaffle_holder is None.

   So, the initial quaffle_holder is None, unless someone is holding it initially? Wait, no. The initial state is given by the grid. If the Quaffle is in a cell (as .Q), then it's free. If a player is in the same cell as the Quaffle, they don't automatically catch it. Players have to catch it via actions.

   So the initial state is that the Quaffle is at its position, and not held by anyone, unless a player is in the same cell and catches it. But according to the problem statement, the input's actions are valid. So initial setup may have players and Quaffle in the same cell, but the initial state is that the Quaffle is not held. Only when a player performs a 'C' action in a step will they catch it.

   So, initial processing:

   Read all the players, goals, and Quaffle's initial position.

   Now, processing the T steps:

   For each step:

      Read the line, split into parts. The first part is the entity's identifier. Then the action, and possibly more (like the ball identifier for catching).

      For example, "B2 C .Q" is an action where entity B2 catches the .Q ball.

      So, the line is split into parts: for the first example step: ['B2', 'C', '.Q'].

      The entity is 'B2', which is a player.

      The action is 'C', and then the ball is '.Q'.

      So, for each action line:

         parts = line.split()
         entity = parts[0]
         action = parts[1]
         if action is 'C', then ball = parts[2]

      So, in code:

      For each step in T steps:

         parts = input().split()

         entity = parts[0]

         action_type = parts[1]

         ... process accordingly.

   Now, let's model the code structure.

   Data Structures:

   players: dict mapping player ID (string) to (x, y) position. Initially filled from the grid.

   goals: a grid (list of lists) where each cell is either None, 'RG', or 'BG'. We can precompute this from the initial grid.

   quaffle_holder: None or the player's ID (string). Initially None.

   quaffle_pos: (x, y) tuple. Initially set to the position found in the grid.

   middle: ( (N//2), (M//2) ) assuming 0-based. Because N and M are odd. So for N=5, (N//2) is 2 (since 5//2=2 in integer division), which is the third row (0-based) which is (5+1)/2=3 in 1-based. So yes, 0-based.

   So middle is (n_middle, m_middle) = (N//2, M//2) ?

   Wait, original problem says the middle is ( (N+1)/2-th line, (M+1)/2-th column ), starting from 1.

   For example, N=5, M=5: (3,3) 1-based, which is (2,2) 0-based. So for 0-based indices, middle is ( (N-1)//2, (M-1)//2 ). Because (5-1)/2 = 2, which is correct.

   So for general N and M (odd), the middle is ( (N-1)//2, (M-1)//2 ) in 0-based indices.

   So compute middle_x = (N-1) // 2, middle_y = (M-1) // 2.

   Now, processing actions:

   For each action, determine the entity. If the entity is a player, process their action. If the entity is .Q (Quaffle), process its movement.

   Let's model the code.

   Initialize:

   Read N, M.

   Read N lines for the grid.

   For each cell (i, j):

      for each pair in the cell (since the problem says that several entities can be in the same cell. Wait, but the grid is given as N lines, each with M pairs. Each pair is the content of the cell. So for each cell (i, j), the pair is a combination of the entities present. For example, a cell can have a player and a goal and the Quaffle. But according to the problem statement, the grid's pairs are:

      Each pair of characters can be:

      .. empty.

      R0, R1, etc. for players.

      RG, BG for goals.

      .Q for the Quaffle.

      So each cell can have multiple pairs. Wait, no: the problem says that each cell is represented by a pair of characters. So each cell contains exactly one pair. So the input's grid is N lines, each with M pairs. Each cell (i,j) is represented by exactly one pair. So the pair can be, for example, RG (a goal), or R0 (player), or .Q (Quaffle), etc.

   So, for each cell (i, j), the pair is one of the possible options. So, for example, a cell can be R0 (player), another can be RG (goal), another can be .Q (Quaffle).

   So, during initial processing:

   For each cell (i, j):

      pair = grid[i][j]

      if pair == 'RG' or pair == 'BG':

          goals[i][j] = pair

      elif pair[0] in ('R', 'B') and pair[1] in digits:

          players[pair] = (i, j)

      elif pair == '.Q':

          quaffle_pos = (i, j)

      else:  # .. or other cases like other balls (but problem says only Quaffle exists in this version)

          pass

   So, the code can process this.

   Now, for each step:

   For example, in the first sample input:

   The step "B2 U" is processed as follows:

   The entity is B2, which is a player. The action is U (move up). So the player's position is updated from (4, 0) (assuming initial position as per the first sample input) to (3, 0). Then, if B2 is holding the Quaffle, the Quaffle's position is also updated.

   But initially, the Quaffle is at (2, 2). So B2 isn't holding it. So moving B2 up doesn't affect the Quaffle.

   So, the code must:

   For the movement action (U/D/L/R):

      new_x, new_y = compute new position based on direction.

      Check that the movement is valid (but the problem says all actions are valid, so no need to handle invalid).

      Update the player's position to (new_x, new_y).

      If the player is holding the Quaffle (quaffle_holder == entity), then set quaffle_pos to (new_x, new_y).

   For catching:

      The player (entity) is in the same cell as the Quaffle (quaffle_holder is None and quaffle_pos is equal to the player's position). Then, set quaffle_holder to the player.

   For throwing:

      The player (entity) is holding the Quaffle. Set quaffle_holder to None, and quaffle_pos to the player's current position.

   For Quaffle movement:

      entity is '.Q', action is movement.

      Check that quaffle_holder is None (since otherwise, the Quaffle can't move on its own).

      Update quaffle_pos according to the direction.

   After processing the action, check if quaffle_holder is None and quaffle_pos is in a goal cell.

   If yes:

      Determine the goal type. If it's RG, then the scoring team is blue. If BG, then red.

      Add the event to the output list (current step index t).

      Increment the score for the scoring team.

      Move the Quaffle to the middle, set quaffle_pos to (middle_x, middle_y), and quaffle_holder remains None.

   So, after a goal is scored, the Quaffle is reset to the middle. But what if the middle is a goal cell? According to the problem statement, the middle has no goal. So we can assume that the middle cell is not a goal. So when moving the Quaffle to the middle, no new goal is triggered.

   So steps to handle after a goal:

   - Move the Quaffle to the middle.

   So, the code structure:

   Read N, M.

   Read the grid, process into players, goals, and initial Quaffle position.

   Read T steps into a list.

   Initialize red_score and blue_score to 0.

   Initialize events list.

   Process each step in order (t from 0 to T-1):

      line = steps[t]

      parse entity, action.

      process the action.

      check if quaffle_holder is None and quaffle_pos is in a goal cell.

      if yes:

          determine the goal type (RG or BG).

          the scoring team is the opposite (RG → blue, BG → red).

          add to events: (t, team)

          increment score.

          move Quaffle to middle.

   After all steps, output the events in order, then the final score.

   Now, how to represent the goals. Since each cell can have a goal or not, and which type, we can create a grid (list of lists) where goals[i][j] is None, 'RG', or 'BG'.

   So, during initial processing:

   goals = [[None for _ in range(M)] for _ in range(N)]

   Then, for each cell (i, j):

      pair = grid[i][j]

      if pair == 'RG':

          goals[i][j] = 'RG'

      elif pair == 'BG':

          goals[i][j] = 'BG'

   So, to check if the Quaffle is in a goal cell after an action:

   x, y = quaffle_pos

   if quaffle_holder is None and goals[x][y] is not None:

       # then a goal is scored.

   Now, for code:

   Let's think about the code steps.

   First, reading the grid.

   Then, the players are stored in a dictionary.

   Then, the steps are read and stored in a list.

   Then, processing each step.

   Let's code step by step.

   Read N and M:

   n, m = map(int, input().split())

   Then, read n lines:

   goals = [[None for _ in range(m)] for _ in range(n)]

   players = {}

   quaffle_pos = None

   quaffle_holder = None

   for i in range(n):

       line = input().strip().split()

       for j in range(m):

           pair = line[j]

           if pair == 'RG':

               goals[i][j] = 'RG'

           elif pair == 'BG':

               goals[i][j] = 'BG'

           elif len(pair) == 2:

               if pair[0] in ('R', 'B') and pair[1].isdigit():

                   players[pair] = (i, j)

               elif pair == '.Q':

                   quaffle_pos = (i, j)

   Then, read T:

   t = int(input())

   steps = [input().strip() for _ in range(t)]

   Now, process each step:

   red_score = 0

   blue_score = 0

   events = []

   middle_x = (n - 1) // 2

   middle_y = (m - 1) // 2

   for step_idx in range(t):

       line = steps[step_idx]

       parts = line.split()

       entity = parts[0]

       action = parts[1]

       # process the action.

       if entity == '.Q':

           # Quaffle is moving.

           # check if it's not held.

           if quaffle_holder is not None:

               # according to problem statement, actions are valid. So this shouldn't happen.

               pass

           # move the Quaffle.

           direction = action

           x, y = quaffle_pos

           if direction == 'U':

               x -= 1

           elif direction == 'D':

               x += 1

           elif direction == 'L':

               y -= 1

           elif direction == 'R':

               y += 1

           quaffle_pos = (x, y)

       else:

           # entity is a player.

           # get current position.

           current_pos = players[entity]

           x, y = current_pos

           if action in ('U', 'D', 'L', 'R'):

               # move the player.

               direction = action

               new_x, new_y = x, y

               if direction == 'U':

                   new_x -= 1

               elif direction == 'D':

                   new_x += 1

               elif direction == 'L':

                   new_y -= 1

               elif direction == 'R':

                   new_y += 1

               # update the player's position.

               players[entity] = (new_x, new_y)

               # if the player is holding the Quaffle, update its position.

               if quaffle_holder == entity:

                   quaffle_pos = (new_x, new_y)

           elif action == 'C':

               # catch the ball.

               ball = parts[2]

               # according to problem, the ball is in the same cell.

               # assuming that the action is valid.

               # only .Q is considered here.

               if ball == '.Q':

                   quaffle_holder = entity

                   # the Quaffle's position is now the same as the player's.

                   quaffle_pos = players[entity]

           elif action == 'T':

               # throw the Quaffle.

               quaffle_holder = None

               # set quaffle_pos to current player's position.

               quaffle_pos = players[entity]

       # after processing the action, check if Quaffle is in a goal cell and not held.

       if quaffle_holder is None:

           x, y = quaffle_pos

           goal_type = goals[x][y]

           if goal_type is not None:

               # score.

               if goal_type == 'RG':

                   # blue team scores.

                   blue_score += 1

                   events.append( (step_idx, 'BLUE') )

               else: # 'BG'

                   red_score += 1

                   events.append( (step_idx, 'RED') )

               # move Quaffle to middle.

               quaffle_pos = (middle_x, middle_y)

               # since after this, the Quaffle is at the middle, which has no goal.

       # end of action processing.

   # after all steps, output events in order.

   events.sort()  # but they should be in order as they are added.

   # but wait, the events are added in the order they happen, so they should already be sorted by step_idx.

   for t, team in events:

       print(f"{t} {team} GOAL")

   print(f"FINAL SCORE: {red_score} {blue_score}")

   Now, let's test this code against the sample inputs.

   Let's take the third sample input:

   Input:

3 5

.. .. R0 .. ..

RG .. .Q .. BG

.. .. B0 .. ..

5

R0 D

R0 C .Q

R0 L

R0 L

R0 T

The initial grid is:

Row 0 (0-based):

.. .. R0 .. ..

So, row 0, columns 0: '..', 1: '..', 2: 'R0', 3: '..', 4: '..'

Row 1:

RG .. .Q .. BG

So, row 1:

columns 0: 'RG' (red goal), 1: '..', 2: '.Q', 3: '..', 4: 'BG' (blue goal)

Row 2:

.. .. B0 .. ..

columns 2: 'B0'.

So, players are:

R0: (0, 2)

B0: (2, 2)

Quaffle is initially at (1, 2) (row 1, column 2).

Processing steps:

Step 0: R0 D (action is D). So, move down from (0,2) → (1,2). Check if R0 is holding Quaffle. Initially, no. So R0's new position is (1,2). Quaffle_holder is None. Now, after moving, check if Quaffle is in goal. Quaffle is still at (1,2) (the same as R0's new position? No, because the Quaffle is still at (1,2) unless someone is holding it. Wait, after step 0:

R0 moves to (1,2), which is the same cell as the Quaffle. But since he's not holding it (he hasn't caught it yet), the Quaffle's position is (1,2). So after moving, the Quaffle's position is still (1,2). But since the player is not holding it, the cell is RG for (1,0), BG for (1,4). So (1,2) is .Q's initial position. The Quaffle's position is now (1,2) (since R0 moved into that cell, but didn't catch it yet.

But the action is movement, and the Quaffle's position is still (1,2) (because the Quaffle is not held by anyone). So after R0's movement, he's at (1,2), which is the same cell as the Quaffle. But the Quaffle is still there. So after step 0, the Quaffle is at (1,2), which is a goal cell? No. The goals are at (1,0) (RG), (1,4) (BG), and (1,2) is '.Q' in the initial setup. So goals[1][2] is None. So no goal is scored.

Step 1: R0 C .Q. So R0 catches the Quaffle. Now, quaffle_holder is R0. Quaffle's position is set to R0's position (1,2). So after this action, the Quaffle is held by R0.

Check if quaffle_holder is None: no. So no goal.

Step 2: R0 L (move left). R0's current position is (1,2). Moving left to (1,1). Since R0 is holding the Quaffle, quaffle_pos becomes (1,1). No goal.

Step 3: R0 L (move left to (1,0)). Now, R0's position is (1,0). The Quaffle is at (1,0). Check if (1,0) is a goal cell. Yes, it's RG. But since the Quaffle is held (quaffle_holder is R0), no goal is processed.

Step 4: R0 T (throw). So quaffle_holder becomes None. Quaffle_pos is set to R0's current position (1,0). Now, check if it's a goal cell. Yes, RG. So quaffle_holder is None. So the scoring team is blue (since RG is red's goal). So blue_score +=1. The event is added for step 4. Then, the Quaffle is moved to the middle. The middle for N=3, M=5 is (1, 2). So quaffle_pos becomes (1,2).

So the output is step 4: "4 BLUE GOAL".

Which matches the third sample's output.

So code seems correct.

Another sample: the second input.

Sample input 2:

3 5

.. .. R0 .. ..

RG .. .Q .. BG

.. .. B0 .. ..

12 steps.

The steps include R0 taking the Quaffle, moving, throwing. Then B0 catches and moves into RG.

But according to the code, after R0 throws the Quaffle, the Quaffle's position is checked. If that position is a goal cell (BG or RG), then a goal is processed.

In the second sample's step 3, R0 throws the Quaffle into a BG cell (probably). Let's see:

After processing step 3 (R0 T), the Quaffle is placed at R0's current position, which after moving R and R. Wait, step 3 in the sample's steps:

The steps are:

12 steps:

R0 D

R0 C .Q

R0 R

R0 T

R0 D

B0 R

B0 U

B0 C .Q

B0 L

B0 L

B0 L

B0 T

Let's walk through.

After step 3 (index 3), R0 throws the Quaffle. At that point, R0's position is (1,3) (after moving R twice from initial position (0,2) → down to (1,2) (step 0), then right to (1,3) (step 2). So when R0 throws, the Quaffle is placed at (1,3). Check if that's a goal cell. Looking at the initial grid, (1,3) is '..', so no goal. So no event. Then, the Quaffle is at (1,3).

In step 7 (index 7), B0 C .Q. B0's position is (2,2) → after moving R (step 5: B0 R → (2,3)), then U (step 6: B0 U → (1,3)), which is where the Quaffle is. So after catching, B0 holds the Quaffle.

Then, steps 8-10: B0 moves left three times to (1,0). Then throws.

In step 11 (index 11), B0 T. The Quaffle is placed at (1,0), which is RG (red goal). So blue team scores.

So the event is step 11, BLUE GOAL.

Which matches the sample output.

So the code should handle this.

Now, the code seems correct. Now, let's check for possible edge cases.

What if multiple goals are scored in a single step?

For example, after throwing, the Quaffle is in a goal cell. Then, after moving it to the middle, the middle cell has a goal. But according to the problem statement, the middle has no goal. So no.

Another edge case: when a player throws the Quaffle into a goal, but after processing, it's moved to the middle. Then, in the same step, the Quaffle is in the middle (no goal) so no further checks.

Another case: the Quaffle is moved by its own action (like moving itself) into a goal cell.

For example, the Quaffle is free, and in a step, the action is .Q R (move right into a goal cell). After processing the movement, the Quaffle is in a goal cell. So score is processed.

Yes.

Another case: the Quaffle is thrown into a goal, which is processed, then in the same step, after moving to the middle, the middle is a goal (but the problem says the middle has no goal). So no.

Thus, the code should handle all cases.

Now, code:

Read the input, process each step, check for goals after each step.

Now, implement the code in Python.

But we have to make sure that all variables are correctly tracked.

Potential issues:

- The initial position of the Quaffle is read correctly.

- The movement of the player and Quaffle is correctly handled.

- After a goal is processed, the Quaffle is moved to the middle, and quaffle_holder is None.

Yes.

Now, code:

The code as outlined above should work. Let's write it in Python, handling all cases.

Testing the code with the samples.

Sample 1:

Input:

5 5

.. R1 .. B1 ..

RG .. .. .. BG

RG R0 .Q B0 BG

RG .. .. .. BG

.. R2 .. B2 ..

13 steps.

Sample Output:

6 BLUE GOAL

12 RED GOAL

FINAL SCORE: 1 1

In this case, after step 6 (t=6), B2 throws the Quaffle into a RG cell. So Blue scores. Then, the Quaffle is moved to the middle (position 2,2). Then, R0 moves, catches, etc. Then, step 12 (t=12), R0 throws into BG, so Red scores.

But according to the code, after step 6, the Quaffle is at B2's position when thrown. Let's see.

But code should handle this.

Thus, the code should be correct.
</think>

```python
n, m = map(int, input().split())
goals = [[None for _ in range(m)] for _ in range(n)]
players = {}
quaffle_pos = None
quaffle_holder = None

for i in range(n):
    line = input().split()
    for j in range(m):
        cell = line[j]
        if cell == 'RG':
            goals[i][j] = 'RG'
        elif cell == 'BG':
            goals[i][j] = 'BG'
        elif cell == '.Q':
            quaffle_pos = (i, j)
        elif cell[0] in ('R', 'B') and cell[1].isdigit():
            players[cell] = (i, j)

T = int(input())
steps = [input().strip() for _ in range(T)]

red_score = 0
blue_score = 0
events = []
middle_x = (n - 1) // 2
middle_y = (m - 1) // 2

for step_idx in range(T):
    parts = steps[step_idx].split()
    entity = parts[0]
    action = parts[1]
    
    if entity == '.Q':
        if quaffle_holder is None:
            x, y = quaffle_pos
            if action == 'U':
                x -= 1
            elif action == 'D':
                x += 1
            elif action == 'L':
                y -= 1
            elif action == 'R':
                y += 1
            quaffle_pos = (x, y)
    else:
        current_x, current_y = players[entity]
        if action in ('U', 'D', 'L', 'R'):
            dx, dy = 0, 0
            if action == 'U':
                dx = -1
            elif action == 'D':
                dx = 1
            elif action == 'L':
                dy = -1
            elif action == 'R':
                dy = 1
            new_x, new_y = current_x + dx, current_y + dy
            players[entity] = (new_x, new_y)
            if quaffle_holder == entity:
                quaffle_pos = (new_x, new_y)
        elif action == 'C':
            ball = parts[2]
            if ball == '.Q' and (current_x, current_y) == quaffle_pos:
                quaffle_holder = entity
                quaffle_pos = (current_x, current_y)
        elif action == 'T':
            quaffle_holder = None
            quaffle_pos = players[entity]
    
    if quaffle_holder is None:
        x, y = quaffle_pos
        goal = goals[x][y]
        if goal is not None:
            if goal == 'RG':
                blue_score += 1
                team = 'BLUE'
            else:
                red_score += 1
                team = 'RED'
            events.append((step_idx, team))
            quaffle_pos = (middle_x, middle_y)

for t, team in events:
    print(f"{t} {team} GOAL")
print(f"FINAL SCORE: {red_score} {blue_score}")
```