You will be given a competitive programming problem.
Your task is to analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits. Explain why your chosen implementation strategy is the most efficient solution and then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must:
- Read input using input()
- Write output using print()
- Avoid any debug prints or extra output

Wrap your final solution in a single code block using triple backticks, like this:
```python
<your code here>
```

# Quest (VK Cup 2015 - Раунд 3, 2015)

You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Polycarp is making a quest for his friends. He has already made n tasks, for each task the boy evaluated how interesting it is as an integer qi, and the time ti in minutes needed to complete the task.

An interesting feature of his quest is: each participant should get the task that is best suited for him, depending on his preferences. The task is chosen based on an interactive quiz that consists of some questions. The player should answer these questions with "yes" or "no". Depending on the answer to the question, the participant either moves to another question or goes to one of the tasks that are in the quest. In other words, the quest is a binary tree, its nodes contain questions and its leaves contain tasks.

We know that answering any of the questions that are asked before getting a task takes exactly one minute from the quest player. Polycarp knows that his friends are busy people and they can't participate in the quest for more than T minutes. Polycarp wants to choose some of the n tasks he made, invent the corresponding set of questions for them and use them to form an interactive quiz as a binary tree so that no matter how the player answers quiz questions, he spends at most T minutes on completing the whole quest (that is, answering all the questions and completing the task). Specifically, the quest can contain zero questions and go straight to the task. Each task can only be used once (i.e., the people who give different answers to questions should get different tasks).

Polycarp wants the total "interest" value of the tasks involved in the quest to be as large as possible. Help him determine the maximum possible total interest value of the task considering that the quest should be completed in T minutes at any variant of answering questions.

## Constraints
Time limit per test: 1.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first line contains two integers n and T (1 ≤ n ≤ 1000, 1 ≤ T ≤ 100) — the number of tasks made by Polycarp and the maximum time a quest player should fit into.

Next n lines contain two integers ti, qi (1 ≤ ti ≤ T, 1 ≤ qi ≤ 1000) each — the time in minutes needed to complete the i-th task and its interest value.

## Output Format
Print a single integer — the maximum possible total interest value of all the tasks in the quest.

## Examples
```input
5 5
1 1
1 1
2 2
3 3
4 4
```
```output
11
```
-----
```input
5 5
4 1
4 2
4 3
4 4
4 5
```
```output
9
```
-----
```input
2 2
1 1
2 10
```
```output
10
```

## Note
In the first sample test all the five tasks can be complemented with four questions and joined into one quest.

In the second sample test it is impossible to use all the five tasks, but you can take two of them, the most interesting ones.

In the third sample test the optimal strategy is to include only the second task into the quest.

Here is the picture that illustrates the answers to the sample tests. The blue circles represent the questions, the two arrows that go from every circle represent where a person goes depending on his answer to that question. The tasks are the red ovals.

Mutant Code

'''python
def test_program(input_stream, output_stream): # pragma: no mutate
    import builtins # pragma: no mutate
    input = lambda: input_stream.readline()[:-1] # pragma: no mutate
    print = lambda *args, **kwargs: builtins.print(*args, **kwargs, file=output_stream) # pragma: no mutate
    n, T = None
    bits = [[] for _ in range(101)]  # d ranges from 0 to 100

    for _ in range(n):
        ti, qi = map(int, input().split())
        max_d = T - ti
        if max_d < 0:
            continue
        max_d = min(max_d, 100)
        for d in range(max_d + 1):
            bits[d].append(qi)

    prefix = []
    for d in range(101):
        bits[d].sort(reverse=True)
        curr = [0]
        s = 0
        for q in bits[d]:
            s += q
            curr.append(s)
        prefix.append(curr)

    dp = {0: 0}
    for d in range(100, -1, -1):
        new_dp = {}
        p = prefix[d]
        m = len(p) - 1
        for carry_in, sum_qi in dp.items():
            for t in range(0, m + 1):
                total = t + carry_in
                if d > 0:
                    if total % 2 != 0:
                        continue
                    new_carry = total // 2
                    new_sum = sum_qi + p[t]
                    if new_carry in new_dp:
                        new_dp[new_carry] = max(new_dp[new_carry], new_sum)
                    else:
                        new_dp[new_carry] = new_sum
                else:
                    if total != 1:
                        continue
                    new_sum = sum_qi + p[t]
                    if 0 in new_dp:
                        new_dp[0] = max(new_dp[0], new_sum)
                    else:
                        new_dp[0] = new_sum
        dp = new_dp

    print(dp.get(0, 0))
'''

Now you must:
1. Identify the bug(s) in the mutant code.
2. Clearly explain your correct algorithmic approach.
3. Write a correct and optimized Python 3 solution, ensuring correctness for all test cases and respecting the constraints.
4. Output only your final code in a valid Python code block, using input() and print() directly.

