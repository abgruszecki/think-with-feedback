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

# Bouquet (Easy Version) (Codeforces Round 961 (Div. 2), 2024)

You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

This is the easy version of the problem. The only difference is that in this version, the flowers are specified by enumeration.

A girl is preparing for her birthday and wants to buy the most beautiful bouquet. There are a total of $$$n$$$ flowers in the store, each of which is characterized by the number of petals, and a flower with $$$k$$$ petals costs $$$k$$$ coins. The girl has decided that the difference in the number of petals between any two flowers she will use in her bouquet should not exceed one. At the same time, the girl wants to assemble a bouquet with the maximum possible number of petals. Unfortunately, she only has $$$m$$$ coins, and she cannot spend more. What is the maximum total number of petals she can assemble in the bouquet?

## Constraints
Time limit per test: 1.5 seconds
Memory limit per test: 512.0 megabytes

## Input Format
Each test consists of several test cases. The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10\,000$$$) — the number of test cases. This is followed by descriptions of the test cases.

The first line of each test case contains two integers $$$n$$$, $$$m$$$ ($$$1 \le n \le 2 \cdot 10^5, 1 \le m \le 10^{18}$$$) — the number of flowers in the store and the number of coins the girl possesses, respectively. The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$1 \le a_i \le 10^9$$$), where $$$a_i$$$ is the number of petals of the $$$i$$$-th flower in the store.

The sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot {10}^5$$$.

## Output Format
For each test case, output a single integer — the maximum possible number of petals in the bouquet that the girl can assemble while meeting all the conditions listed above.

## Examples
```input
5
5 10
1 1 2 2 3
8 20
4 2 7 5 6 1 1 1
8 100000
239 30 610 122 24 40 8 2
11 13
2 4 11 1 1 2 3 5 4 3 2
8 1033
206 206 206 207 207 207 207 1000
```
```output
7
13
610
13
1033
```

## Note
In the first test case, you can assemble a bouquet with $$$(1, 1, 2, 2), (2, 2, 3), (1, 1), (2, 2)$$$. The maximum over all valid bouquets not greater than $$$10$$$ is $$$7$$$ for $$$(2, 2, 3)$$$. In the third test case, you can assemble a bouquet with only one flower of any type, so the answer is $$$610$$$. In the fourth test case, you can assemble a bouquet with $$$(4, 4, 5)$$$, which gives you $$$13$$$ petals, and it is the maximum amount of petals that the girl can buy.

Mutant Code

'''python
def test_program(input_stream, output_stream): # pragma: no mutate
    import builtins # pragma: no mutate
    input = lambda: input_stream.readline()[:-1] # pragma: no mutate
    print = lambda *args, **kwargs: builtins.print(*args, **kwargs, file=output_stream) # pragma: no mutate
    import bisect

    def main():
        import sys
        input = input_stream.read().split()
        ptr = None
        t = int(input[ptr])
        ptr += 1
        for _ in range(t):
            n = int(input[ptr])
            m = int(input[ptr + 1])
            ptr += 2
            a = list(map(int, input[ptr:ptr + n]))
            ptr += n
            a.sort()
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + a[i]
            max_sum = 0
            for j in range(n):
                target = a[j] - 1
                i_pos = bisect.bisect_left(a, target, 0, j + 1)
                sum_total = prefix[j + 1] - prefix[i_pos]
                if sum_total <= m:
                    current = sum_total
                else:
                    low, high = 1, j - i_pos + 1
                    best = 0
                    while low <= high:
                        mid = (low + high) // 2
                        start = j + 1 - mid
                        s = prefix[j + 1] - prefix[start] if start >= i_pos else 0
                        if s > m:
                            high = mid - 1
                        else:
                            best = s
                            low = mid + 1
                    current = best
                if current > max_sum:
                    max_sum = current
            print(max_sum)

    if __name__ == "__main__":
        main()
'''

Now you must:
1. Identify the bug(s) in the mutant code.
2. Clearly explain your correct algorithmic approach.
3. Write a correct and optimized Python 3 solution, ensuring correctness for all test cases and respecting the constraints.
4. Output only your final code in a valid Python code block, using input() and print() directly.

