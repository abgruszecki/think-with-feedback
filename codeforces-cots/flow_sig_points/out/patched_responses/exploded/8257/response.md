<think>
Okay, let's see. I need to solve this problem where I have to simulate multiple processor cores executing instructions over m cycles, and track when each core gets locked due to conflicts in writing to cache cells. Hmm.

So, the problem statement says that during each cycle, each core gives an instruction. If the instruction is 0, they do nothing. Otherwise, they try to write to that cell. If two or more cores try to write to the same cell in the same cycle, all those cores get locked immediately. Also, the cell gets locked, so any future attempts to write to it will lock the core attempting it.

The output for each core is the cycle number when it was locked, or 0 if it never was.

Constraints are n, m, k up to 100, which is manageable. So, even a straightforward simulation should work, but I need to structure it properly.

Let me think about the steps:

For each cycle from 1 to m:
   For each core that is not yet locked:
      Check their instruction for this cycle.
      If it's 0: do nothing.
      Else:
         Check if the target cell is already locked. If yes, then this core is now locked at current cycle.
         Else, collect all cores trying to write to this cell in this cycle. Then, if there are 2 or more such cores, all of them get locked, and the cell is locked.

But the problem is, during a cycle, all the instructions are processed in parallel. So, for each cycle, I need to check all active cores (not locked) and see what their instruction is. Then, for each cell, collect all the cores that are attempting to write to it in this cycle. For each cell that has two or more such cores, those cores get locked at this cycle, and the cell becomes locked.

Moreover, any core that is attempting to write to a cell that is already locked (from previous cycles) gets locked immediately in this cycle.

So the steps per cycle would be:

1. For the current cycle, collect all the cells that are being written to by active cores. But first, check if the cell is already locked. For each core, if the cell is locked, then the core is locked now.

Wait, no. Wait, during the current cycle, each core that is not locked processes their instruction. So for each such core:

If the instruction is 0: do nothing.

If the instruction is a cell number (1..k):

   Check if the cell is already locked. If yes, the core is locked in this cycle.

   If the cell is not locked, then the core is attempting to write to it. But the locking happens only if during this cycle, multiple cores (including this one) are trying to write to the same cell.

So, the steps per cycle are:

For each cell, collect all the cores that are trying to write to it in this cycle (but not locked yet, and the cell is not locked yet). Then, if any cell has >=2 such cores, all of them are locked, and the cell is locked.

Additionally, any core that tried to write to a cell that was already locked (from previous steps) is locked in this cycle.

Wait, but the order here is important. Because, when processing a cycle, first, any core that is trying to write to a locked cell is locked. Then, among the remaining cores (those whose target cell is not locked), check if multiple cores are writing to the same cell. If so, lock them and the cell.

But how to model this?

Alternatively, during the current cycle, for each core that is not locked:

- Check if their instruction for this cycle is 0. If yes, do nothing.
- Else, the cell is x. Check if x is locked. If yes, lock the core (record its lock time as current cycle).
- If x is not locked, add this core to a list of candidates for x.

After processing all cores for the current cycle, check all the cells in the candidates. For each cell in the candidates:

If the count of cores in the candidate list for that cell is >=2, then:

   Lock all those cores (set their lock time to current cycle)
   Lock the cell.

But wait, this approach has a problem. Because the core could be added to the candidate list even if the cell was already locked by a previous cell in the same cycle. For example, during the same cycle, two cores try to write to cell A. They are added to the candidate list for A. Then, during processing, cell A is locked, and all cores in the candidate list are locked. But another core might try to write to cell A in the same cycle, but after the cell was locked. Wait, no. Because all the processing for the current cycle is done in parallel. So, all cores that are active (not yet locked) and have a non-zero instruction for this cycle are processed.

So, in the same cycle, the steps are:

1. For each core that is not locked:

   a. Check instruction for current cycle.

   b. If it's 0: skip.

   c. Else, if the cell is already locked (from previous steps), then the core is locked now.

   d. Else, add to the cell's list for possible conflict.

2. After all cores are processed in step 1, check each cell in the cell lists. For cells with >=2 cores, lock the cell and all those cores.

But the order here is important. Because, for the same cycle, the cell could be locked in step 2, which would affect other cores in step 1. Wait no, because step 1 and 2 are separate phases.

So, the correct approach is:

During cycle t:

- For all cores not locked, check their instruction.

   - For each core, if instruction is a cell that is already locked (before this cycle), then lock the core at t.

   - Else, if instruction is non-zero and the cell is not locked, add the core to a list for that cell.

- After processing all cores, for each cell in the list:

   - if the cell's list has >=2 cores, lock the cell and mark all those cores as locked at t.

Thus, the key is that during a cycle, first, we check for cores that are trying to write to already locked cells. Then, for the remaining cores (trying to write to unlocked cells), group them by cell and check for conflicts.

This way, any core that writes to a cell that gets locked in this same cycle (due to a conflict) is not processed again, because the cell is locked only after the conflict is detected.

So, the steps are:

For each cycle t from 1 to m:

   create a dictionary (or list) to track which cells are being written to by active cores.

   first, process each core not yet locked:

      if their instruction for t is 0: do nothing.

      else:

         cell = x.

         if cell is already locked (from previous cycles):

             lock the core now (t is their lock cycle)

         else:

             add to the cell's list for this cycle.

   then, process each cell in the cell's list:

      if the count of cores in the cell's list >=2:

          lock the cell.

          lock all cores in the list for this cell, set their lock cycle to t.

So, in code:

We need to track:

- For each core, whether it's locked, and at which cycle.

- For each cell, whether it's locked.

So, initializing:

locked_cores = [False] * n

lock_time = [0] * n

locked_cells = [False] * (k+1)  # since cells are 1-based.

Then, for each cycle t in 1..m:

   per_cell_cores = defaultdict(list)

   # First pass: check if the cell is already locked.

   for core in 0..n-1:

      if locked_cores[core]:

          continue

      instruction = x[core][t-1]  # assuming x is 0-based in the cycle.

      if instruction ==0:

          continue

      cell = instruction

      if locked_cells[cell]:

          # core is locked now.

          locked_cores[core] = True

          lock_time[core] = t

      else:

          # add to per_cell_cores for possible conflict.

          per_cell_cores[cell].append(core)

   # Second pass: check for conflicts in each cell.

   for cell in per_cell_cores:

      cores = per_cell_cores[cell]

      if len(cores) >=2:

          # lock cell and cores.

          locked_cells[cell] = True

          for core in cores:

              if not locked_cores[core]:  # in case they were locked in previous steps?

                  locked_cores[core] = True

                  lock_time[core] = t

So, in this approach, during the first phase of the cycle, cores that are trying to write to already locked cells are marked as locked. Then, the remaining cores (those who tried to write to unlocked cells) are grouped by cell. For each cell, if there are two or more cores, all of them are locked, and the cell is locked.

This should handle all possible cases.

Let's test this logic against the examples.

First example input:

4 3 5

1 0 0

1 0 2

2 3 1

3 2 0

Processing each cycle:

Cycle 1:

Cores 0,1,2,3 (all not locked initially).

Core 0's instruction is 1. Cell 1 is not locked. Add to per_cell_cores[1] = [0]

Core1's instruction is 1. Add to per_cell_cores[1] = [0,1]

Core2's instruction is 2. Cell 2 is not locked. Add to per_cell_cores[2] = [2]

Core3's instruction is 3. Add to per_cell_cores[3] = [3]

Then, check per_cell_cores:

cell1: 2 cores. So lock cell1. Lock cores 0 and 1. Their lock time is 1.

cell2: 1 core. Do nothing.

cell3: 1 core. Do nothing.

So output for cores 0 and 1 is 1.

Cycle2:

Check cores 2 and 3 (cores 0 and 1 are locked).

Core2's instruction is 3. Cell3 is not locked. Add to per_cell_cores[3] = [3 (core2?)]

Wait, no. Core2 is the third core (since cores are 0-based). Wait, the input's first line is for core 1 (since the problem says the i-th line is the i-th core, but in code, perhaps the 0-based index is used). Wait, in the input, the cores are numbered 1 to n, but in code, we'll index them as 0..n-1. So for the first example, the first line is core 0, instructions 1,0,0.

So in cycle 2, core 0 is locked, so he's skipped.

Core1 is also locked.

Core2's instruction for cycle 2 is 3. So cell3 is unlocked. Add to per_cell_cores[3] = [2]

Core3's instruction is 2. Cell2 is unlocked. Add to per_cell_cores[2] = [3]

After this phase, per_cell_cores has:

cell3: [2]

cell2: [3]

No conflicts. So nothing happens.

Cycle3:

Check cores 2 and 3 (since 0 and 1 are locked).

Core2's instruction is 1. Cell1 is already locked (from cycle1). So core2 is now locked in cycle3.

Core3's instruction is 0. Do nothing.

So core2's lock time is 3.

So output for the four cores:

1,1,3,0. Which matches the first example.

Another example:

3 2 2

1 2

1 2

2 2

Output is 1,1,0.

So cycle1:

Cores 0,1,2.

Core0: cell1. Not locked. Add to cell1's list.

Core1: cell1. Add to cell1's list.

Core2: cell2. Add to cell2's list.

Processing per_cell_cores:

cell1 has 2 cores: lock them. lock_time becomes 1.

cell2 has 1 core: do nothing.

So cores 0 and 1 are locked at 1.

Cycle2:

Core0 and 1 are locked. Only core2 is active.

His instruction is 2. Cell2 is not locked. So added to cell2's list. Then check cell2: 1 core, no conflict. So nothing. So core2 is not locked.

So output is 1,1,0.

So code seems correct.

Now, for the implementation.

We need to read n, m, k.

Then read n lines, each with m integers. Then for each core (0-based), store their instructions for each cycle (0-based? Or 1-based? Wait, in the problem statement, cycles are 1-based. So in the input, the first instruction is cycle1, etc. So for core i, xij is the instruction for cycle j (1-based). So in code, for cycle t (1..m), the instruction is x[i][t-1].

So the code steps:

Read n, m, k.

Then read n lines, each line has m integers. Store as a list of lists.

Initialize locked_cores as a list of False for each core.

lock_time as [0]*n.

locked_cells as [False]*(k+1) (since cells are 1-based).

Then, for each cycle from 1 to m:

   per_cell_cores is a defaultdict(list).

   for each core in 0..n-1:

      if locked_cores[core] is True: skip.

      instruction = x[core][t-1] (since t is 1-based, cycles 1 to m).

      if instruction ==0: continue.

      cell = instruction.

      if cell is already locked (locked_cells[cell] is True):

          lock the core now.

          locked_cores[core] = True

          lock_time[core] = t.

      else:

          add core to per_cell_cores[cell].

   after processing all cores, check per_cell_cores:

   for each cell in per_cell_cores:

      cores_in_cell = per_cell_cores[cell]

      if len(cores_in_cell) >=2:

          locked_cells[cell] = True

          for core in cores_in_cell:

              if not locked_cores[core]:

                  locked_cores[core] = True

                  lock_time[core] = t

Once all cycles are processed, output each lock_time[i], per core.

So that's the plan.

Now, implement this in Python.

Read input:

n, m, k = map(int, input().split())

instructions = [list(map(int, input().split())) for _ in range(n)]

locked_cores = [False]*n

lock_time = [0]*n

locked_cells = [False]*(k+1)  # cells 1..k

for t in range(1, m+1):

    per_cell = dict()

    # Phase 1: check cells already locked

    for core in range(n):

        if locked_cores[core]:

            continue

        instr = instructions[core][t-1]

        if instr ==0:

            continue

        cell = instr

        if cell <1 or cell >k:

            # invalid, but according to problem statement, xij is 0 or 1..k.

            # So perhaps no need to handle.

        if locked_cells[cell]:

            # lock the core now

            locked_cores[core] = True

            lock_time[core] = t

        else:

            # add to per_cell

            if cell not in per_cell:

                per_cell[cell] = []

            per_cell[cell].append(core)

    # Phase 2: check for conflicts in per_cell

    for cell in per_cell:

        cores_list = per_cell[cell]

        if len(cores_list) >=2:

            locked_cells[cell] = True

            for c in cores_list:

                if not locked_cores[c]:

                    locked_cores[c] = True

                    lock_time[c] = t

After processing all cycles, print each lock_time[i], or 0 if not locked.

Wait, no. The lock_time is initialized to 0. So for cores not locked, their lock_time remains 0. So outputting lock_time[i] directly will give 0 for unlocked cores.

Yes. So, after processing all cycles, for each core in 0..n-1, print lock_time[core].

Thus, the code should be:

Read n, m, k.

Read instructions.

Initialize the locked arrays.

Process each cycle.

Finally, print each lock_time[i].

Now, test the code with the first example:

Sample input 1:

4 3 5

1 0 0

1 0 2

2 3 1

3 2 0

instructions becomes:

[
 [1,0,0],
 [1,0,2],
 [2,3,1],
 [3,2,0]
]

Processing cycle 1:

t=1.

Phase1:

cores 0-3:

core0: instr 1, cell1 not locked. add to per_cell[1] = [0]

core1: instr1, cell1 not locked. add to per_cell[1] = [0,1]

core2: instr2, cell2 not locked. add to per_cell[2] = [2]

core3: instr3, cell3 not locked. add to per_cell[3] = [3]

Phase2:

cell1: 2 cores. Lock cell1, and lock cores 0 and 1.

cell2: no. cell3: no.

So lock_time for 0 and 1 is 1.

Cycle2, t=2:

Phase1:

core0 and 1 are locked.

core2: instr3 (cycle2's instruction is 3, since t is 2, index is 1. instructions[2][1] =3. cell3 not locked. Add to per_cell[3] = [2]

core3: instr2 (instructions[3][1] is 2). cell2 not locked. add to per_cell[2] = [3]

Phase2: per_cell has cell3 and 2, each with 1 core. No changes.

Cycle3, t=3:

Phase1:

core0,1 locked.

core2: instr1. cell1 is locked (from cycle1). So core2 is locked now. lock_time[2] =3.

core3: instr0. do nothing.

Phase2: per_cell is empty.

So lock_time is [1,1,3,0].

Which matches the sample.

Another test case:

Input 3:

3 2 2

1 2

1 2

2 2

instructions:

[[1,2], [1,2], [2,2]]

Cycle1, t=1.

Phase1:

core0: cell1, not locked. add to per_cell[1] = [0]

core1: cell1. add to per_cell[1] = [0,1]

core2: cell2. add to per_cell[2] = [2]

Phase2: cell1 has 2 cores. lock cell1, lock cores 0 and 1. cell2 has 1, no.

Cycle2, t=2:

core0 and 1 are locked. core2 is active.

Phase1:

core2: instr2. cell2 not locked. add to per_cell[2] = [2]

Phase2: cell2 has 1 core. no change.

So lock_time is [1,1,0].

Which matches.

So code should be correct.

Now, code in Python.

Make sure that per_cell is a defaultdict or a normal dictionary. For each cycle, per_cell can be a dict initialized as empty.

In Python, for the code:

n, m, k = map(int, input().split())

instructions = [list(map(int, input().split())) for _ in range(n)]

locked_cores = [False] * n

lock_time = [0] * n

locked_cells = [False] * (k + 1)  # index 0 unused

for t in range(1, m + 1):
    per_cell = {}
    # Phase 1: check already locked cells
    for core in range(n):
        if locked_cores[core]:
            continue
        instr = instructions[core][t-1]
        if instr == 0:
            continue
        cell = instr
        if locked_cells[cell]:
            # Lock the core now
            locked_cores[core] = True
            lock_time[core] = t
        else:
            # Add to per_cell
            if cell not in per_cell:
                per_cell[cell] = []
            per_cell[cell].append(core)
    # Phase 2: check for conflicts
    for cell in per_cell:
        cores_list = per_cell[cell]
        if len(cores_list) >= 2:
            locked_cells[cell] = True
            for c in cores_list:
                if not locked_cores[c]:
                    locked_cores[c] = True
                    lock_time[c] = t

for time in lock_time:
    print(time)

This should work. Let me check for possible errors.

Wait, in the code for per_cell, initially, per_cell is a normal dict. So, when we process each core, for a new cell, we check if the cell is in per_cell. If not, we add it as a key with an empty list. Then append the core.

Yes.

Testing with sample 3:

Input 1 1 1:

1 1 1

0

So, lock_time is [0]. The code prints 0.

Yes.

Another test case:

Sample 2 input:

3 2 2

1 2

1 2

2 2

Which outputs 1,1,0.

The code would process cycle 1:

phase1:

cores 0,1,2.

core0: cell1, per_cell[1] = [0]

core1: cell1, per_cell[1] becomes [0,1]

core2: cell2, per_cell[2] = [2]

phase2:

cell1's cores 0,1: lock them. cell1 is locked.

core2's cell2: 1 core, no action.

So lock_time[0] and 1 are 1. core2 not locked.

cycle2:

core2's instruction is 2. cell2 is not locked. add to per_cell[2] = [2]. phase2: cell2 has 1 core. no action.

so lock_time[2] is 0.

Yes.

Thus, the code should work.
</think>

```python
n, m, k = map(int, input().split())
instructions = [list(map(int, input().split())) for _ in range(n)]
locked_cores = [False] * n
lock_time = [0] * n
locked_cells = [False] * (k + 1)

for t in range(1, m + 1):
    per_cell = {}
    # Phase 1: Check for cores accessing locked cells
    for core in range(n):
        if locked_cores[core]:
            continue
        instr = instructions[core][t-1]
        if instr == 0:
            continue
        cell = instr
        if locked_cells[cell]:
            locked_cores[core] = True
            lock_time[core] = t
        else:
            if cell not in per_cell:
                per_cell[cell] = []
            per_cell[cell].append(core)
    # Phase 2: Check for conflicts in accessed cells
    for cell in per_cell:
        cores = per_cell[cell]
        if len(cores) >= 2:
            locked_cells[cell] = True
            for core in cores:
                if not locked_cores[core]:
                    locked_cores[core] = True
                    lock_time[core] = t

for time in lock_time:
    print(time)
```