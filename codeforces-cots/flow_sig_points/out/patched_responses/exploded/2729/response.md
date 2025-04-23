<think>
Okay, so I need to find the smallest super lucky number that's at least n. Let's think about what a super lucky number is. Oh right, it's a number made of 4s and 7s, and the count of 4s and 7s must be equal. So like, for example, 47 has two digits, one 4 and one 7. So the total number of digits must be even, right? Because if the digits are split equally between 4 and 7, the total has to be even. So the first thing I can do is generate all possible super lucky numbers and find the smallest one >=n. But the problem is, n can be up to 1e9, which is a pretty big number. So generating all possible candidates might be computationally feasible if done smartly.

Hmm, so let's think about the possible candidates. The super lucky numbers must have an even number of digits. The possible lengths are 2,4,6,... up to maybe 10 digits (since 4444477777 is 10 digits). Wait, but even for the maximum n of 1e9, which has 9 digits, the next possible even length is 10. So the candidate numbers can be of lengths 2,4,6,8,10, etc., but considering that the minimal length needed would be the smallest even number >= the number of digits in n.

Wait, for example, if n is 4500, which is 4 digits, then possible candidates are 4-digit super lucky numbers with two 4s and two 7s. But 4500 is 4500, and the next possible in 4 digits is 4747, which is the example's output. But if there's no 4-digit super lucky number >=n, then we need to look for the next even length, which is 6 digits.

So the approach would be:

1. Generate all possible super lucky numbers with 2k digits (k=1,2,3,...), in order of increasing length. For each possible length, generate all possible combinations of 4s and 7s with exactly k 4s and k 7s, sorted in ascending order, and check if any of them is >=n. The first such number is the answer.

But generating all combinations for each length might be time-consuming. However, considering the maximum possible length required. Let's see, for example, the maximum possible n is 1e9, which is 9 digits. So the next possible even length is 10 digits. So for n=999,999,999, the next possible super lucky number is 4444477777 (with 5 4s and 5 7s). So the possible lengths we need to check are up to 10 digits.

But even 10 digits is manageable. Let's see: for a length of 10, the number of possible permutations is C(10,5) = 252. For each possible length 2k, the number of permutations is (2k choose k). For k up to 5 (10 digits), the maximum is 252. For 20 digits, it's 184756, but for the problem constraints, since n can be up to 1e9, the maximum length needed is 10 digits, so even for larger n, like up to 1e18, the possible lengths needed are manageable.

Wait, but the problem says that the input n can be up to 1e9. So the maximum possible n is 1e9, which has 9 digits. So the possible candidates would be numbers with 10 digits. So the maximum length to consider is 10 digits. So even generating all possible 10-digit super lucky numbers (which is C(10,5)=252 numbers) is feasible.

So the plan is:

- For each possible even length L (starting from the minimal possible which is the number of digits in n if even, else next even, and then increasing by 2 each step), generate all possible super lucky numbers of that length, sort them, and check if any is >=n. The first one found in this order is the answer.

So first, determine the minimal possible length. For example:

If n has 5 digits (odd), the minimal length to check is 6. If n has 4 digits, check 4 digits first. Then 6, 8, etc. until we find the first valid number.

But generating all permutations for each length, then checking each one in order. But generating permutations in numerical order is important. Because for a given length, the numbers can be generated in sorted order so that once a number >=n is found, it's the minimal for that length. Then among all lengths, the minimal overall is the answer.

Wait, but we need to check all possible lengths in order of increasing length, and within each length, check the numbers in sorted order. So for example, first check all 4-digit numbers (if applicable) in sorted order, then 6-digit, etc.

But how do we generate the numbers for a given length in sorted order? For a given 2k digits, we need all combinations with k 4s and k 7s. But generating them in sorted order can be done by generating all possible permutations and then sorting them. However, generating all permutations and then sorting may not be efficient. But given that for 10 digits, there are 252 numbers, even generating all permutations and then sorting is manageable.

Alternatively, we can generate the numbers in lex order by backtracking. For example, for a 4-digit number, the lex order would be 4477, 4747, 4774, 7447, 7474, 7744. Wait, but the actual numerical order is different. For example, 4477 is 4477, 4747 is 4747, which is larger than 4477. So generating all permutations and then sorting them as integers would give the correct order.

So the steps would be:

1. For each possible length L in even digits (starting from the minimal possible, then increasing by 2 each step), do:

   a. Generate all possible combinations of 4s and 7s with exactly (L/2) 4s and (L/2) 7s.

   b. Convert these combinations to integers, collect all of them.

   c. Sort them in ascending order.

   d. Check if any of them is >=n. If yes, return the first such number.

   e. If not found in this length, proceed to the next even length.

So the algorithm is to generate all possible candidates in increasing length and within each length, sorted order, and return the first candidate that is >=n.

Now, the problem is how to generate all possible permutations of 4s and 7s with exactly k 4s and k 7s for a length of 2k digits.

Wait, for 2k digits, the count of 4s is k and 7s is k. So the permutations are all possible strings made of k 4s and k 7s, but in all possible positions.

So to generate all such numbers, we can generate all possible combinations of positions for the 4s (or 7s) and then generate the number by placing 4s in those positions and 7s elsewhere.

This can be done using itertools.combinations in Python.

For example, for 4 digits (k=2), the possible combinations are the positions where 4s are placed. The positions are 0-based indices. So for 4 digits, the positions are 0,1,2,3. We need to choose 2 positions for 4s. Each combination will generate a number. Then, all possible such numbers can be generated, sorted, and checked.

So the approach for each length L=2k is:

- Generate all possible combinations of k positions out of 2k.

- For each combination, create a list of '4's and '7's, with '4's in the chosen positions and '7's elsewhere.

- Convert this list into a string, then to an integer.

- Collect all these integers, sort them, and check.

So, for each length L=2k, generate all possible numbers, sort them, and find the first >=n.

But generating all combinations and creating the numbers for each length can be done efficiently.

So, the steps in code:

First, determine the minimal even length. For example, if the input number has m digits. If m is even, then start with m. If m is odd, start with m+1. Then proceed to m+2, etc. But wait, the input could have even digits, but all possible numbers of that length are smaller than n. For example, n could be 7777. For 4-digit numbers, the maximum super lucky number is 7744 (if k=2, the 4s and 7s are two each). Wait no, wait for 4 digits with two 4s and two 7s, the maximum possible is 7744. So if n is 7777, then there are no 4-digit super lucky numbers >=7777. So we need to check the next even length, which is 6 digits. So in that case, the minimal super lucky number would be 444777 (but that's 6 digits, with three 4s and three 7s). So the code must check all possible even lengths starting from the minimal possible (m if even, m+1 if odd), and proceed to higher even lengths until a candidate is found.

Now, how to compute the minimal even length:

n_str = str(n)

m = len(n_str)

min_length = m if m % 2 == 0 else m +1

But wait, even if the length is even, maybe all possible numbers of that length are less than n. For example, if n is 7777 (4 digits), but all 4-digit super lucky numbers are smaller than 7777, then we need to check 6-digit numbers. So the code must check all even lengths starting from the minimal, and for each, generate all possible numbers of that length, sorted, and check if any is >=n.

So the code will:

For each length L in even_lengths (starting from min_length, then L+2, etc.):

   generate all possible super lucky numbers of length L, sorted.

   for each number in the sorted list:

       if number >=n, return it.

So the code can generate the even lengths in order. Once a candidate is found in the first possible length, return it. Otherwise, proceed to longer lengths.

But how to generate all possible super lucky numbers for a given length L=2k.

In Python, for a given k, we can generate all combinations of positions where 4s are placed. The code can use itertools.combinations to generate all possible positions, then build the number.

But for numbers with 10 digits (k=5), the number of combinations is 252, which is manageable.

So the code steps:

Read the input as a string, and as an integer.

Compute the minimal even length.

Loop over possible even lengths starting from the minimal, in increasing order:

   For each length L:

       k = L // 2

       Generate all combinations of k positions from 0 to L-1.

       For each combination:

           create a list of '7's of length L.

           for each position in the combination, set the character to '4'.

           convert this to a string, then to integer.

       collect all these integers, sort them, and check if any is >=n.

       If yes, return the smallest such.

So, for example, for L=4, k=2.

combinations are all 2-length combinations of 0,1,2,3.

Each combination represents positions where 4s are placed. The rest are 7s.

So for combination (0,1), the number is 4477.

combination (0,2) → 4747, etc.

Once all combinations are generated and sorted, the code can check if any is >=n.

So, for the code:

We can start by reading the input as a string, then converting to integer.

But wait, when n is up to 1e9, but when converted to integer, that's manageable.

Then, for each possible even length, generate the candidates.

But for very large n (like 1e9), the code may have to check multiple lengths.

But for example, if n is 4500 (4 digits, even length), generate all 4-digit super lucky numbers, sorted. The first one >=4500 is 4747, which is the answer.

Now, the code needs to generate all possible candidates for a given length, sort them, and check.

But generating the candidates can be optimized. For each combination, generating the number as a string, then comparing as a string with the input n's string may be more efficient than converting to integer, especially for very large lengths. But in Python, even numbers with 1e18 digits can be converted to integers as Python handles big integers. However, for numbers with 10 digits, conversion to integer is straightforward.

But since the input n is up to 1e9 (9 digits), the code can process the candidates as integers.

So, the code will proceed as follows:

Read n as an integer.

Convert the input to a string to get the length.

Compute the minimal even length.

Then, for each even length starting from minimal:

   generate all possible candidates of that length (sorted), and check if any is >=n.

   if found, return the minimal such.

So the code would look like:

Testing against sample input 1.

```python
import itertools


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n").strip())

    original_n = n

    n_str = str(n)

    m = len(n_str)

    # Determine the possible even lengths to check.

    current_length = m if (m % 2 ==0) else m+1

    while True:

        k = current_length // 2

        # Generate all combinations of k positions from 0 to current_length -1

        candidates = []

        positions = itertools.combinations(range(current_length), k)

        for pos in positions:

            num_list = ['7'] * current_length

            for idx in pos:

                num_list[idx] = '4'

            num_str = ''.join(num_list)

            num = int(num_str)

            candidates.append(num)

        # sort the candidates and check

        candidates.sort()

        for candidate in candidates:

            if candidate >= original_n:

                print(candidate, file=output_stream)

                return

        # if not found, try the next even length.

        current_length +=2



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
47
""",
            "output": \
"""\
47
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

In the second example, input 47 → the code checks current_length=2 (since 47 is two digits). The candidates are 47 (positions 0 and 1: 4 and 7? Wait, no. Wait for current_length=2, k=1. So the combinations are [0], [1]. For [0], the number is 47. For [1], the number is 74. So the candidates are [47,74]. Sorted as 47,74. So the first candidate is 47 which is equal to n. So output is 47.

Yes.

Now, what about the case where n is larger than any possible candidate in the minimal even length. For example, n=7744 (which is a 4-digit super lucky number). The next possible candidate in 4 digits would be 7744. But if n is 7745, then the code would check 4-digit candidates. The candidates are sorted. 7744 is the last candidate. Since 7744 <7745, the code proceeds to check 6-digit numbers.

So the code would generate 6-digit numbers, which have 3 4s and 3 7s. The minimal such number is 444777. So for n=7745, the answer would be 444777.

But wait, maybe there is a 6-digit number that's larger than 7745 but smaller than 444777. No, because 444777 is 444777, which is 6 digits. 7745 is a 4-digit number, so 7745 is 4 digits. All 6-digit numbers are larger than 7745. So the code would generate 6-digit numbers. The minimal 6-digit super lucky number is 444777, which is 444777. So the code would output that.

But according to the code's logic, since the code is checking even lengths in order, the first candidate found in the next length (6 digits) would be the minimal possible. So in this example, the code would generate all 6-digit super lucky numbers, sort them, and return the first one, which is 444777, which is indeed >=7745.

So the code seems correct.

Now, considering time constraints. For each even length, the code generates combinations, creates the numbers, sorts them, and checks. For the worst case, when the code has to check multiple even lengths. For example, when n is 77777777 (8 digits), all 8-digit super lucky numbers have 4 4s and 4 7s. The maximum such number is 77774444. But if n is 77777777, then the code checks 8-digit numbers. Since all 8-digit candidates are less than 77777777, the code proceeds to 10-digit numbers. The minimal 10-digit super lucky number is 4444477777 (5 4s and 5 7s), which is 4444477777, which is larger than 77777777.

So the code will generate all possible 8-digit numbers (C(8,4) =70 combinations), which is manageable. Then for 10 digits, 252 combinations. So even in the worst case, the code is efficient.

Now, considering the possible lengths. For n=1e9 (9 digits), the code starts with current_length=10. k=5. So generating 252 candidates, sorted. The first candidate is 4444477777 (since the 4s are in the first 5 positions). But what if n is 4444477777, then that's the answer. If n is higher, like 7777777777 (10 digits), which is higher than 4444477777, then the code would generate all 10-digit candidates. The sorted list will have the first candidate as 4444477777, then others in order. But if none of the 10-digit numbers is >=n, then the code proceeds to 12 digits, but in this case, n is 7777777777. The code would generate 10-digit numbers. The maximum 10-digit super lucky number is 7777744444 (assuming k=5). Wait, no. For k=5, the maximum is 7777744444? No, that's 5 7s followed by 5 4s. But the maximum would be when all 7s are on the left and 4s on the right. So the maximum 10-digit super lucky number is 7777777777? No, because that's 10 7s, which has zero 4s, so not super lucky. The maximum 10-digit super lucky number is 7777774444 (5 7s and 5 4s arranged as 7777744444?) Wait, no. Wait, the super lucky numbers must have exactly 5 4s and 5 7s. So the maximum possible 10-digit number would be 7777744444 (five 7s followed by five 4s). But that's 7777744444. Which is 7777744444. So if n is 7777777777 (10 digits), but this number has 9 7s and 1 4, which is not a super lucky number. So the code would generate the 10-digit candidates. The maximum candidate is 7777744444, which is 7777744444. If n is 7777777777, which is larger than all 10-digit super lucky numbers, then the code would proceed to 12-digit numbers. The minimal 12-digit super lucky number is 444444777777, which is 444444 followed by six 7s. So the code would return that.

But for the code to handle this, the code must generate all possible candidates for each length. But even for 12 digits, the number of combinations is C(12,6)=924, which is manageable.

Thus, the code is efficient enough for the problem's constraints.

Now, for the code in Python:

We need to generate combinations using itertools.combinations. For each combination, create the number as a string, then convert to integer. Collect all numbers, sort them, and check.

But generating the combinations in Python can be done efficiently. For example, for 10 digits, 252 combinations, each processed quickly.

But in Python, for the code to be as efficient as possible, perhaps pre-sorting is better. But since the code is generating the candidates in a way that the combinations are ordered in lex order, but the numerical order may differ. For example, in 4 digits, combinations are generated in order of (0,1) → 4477, (0,2) → 4747, which is numerically smaller than (1,2) → 7474? Wait no. For example, (0,1) gives 4477, (0,2) gives 4747, (0,3) gives 4774, (1,2) gives 7447, (1,3) gives 7474, (2,3) gives 7744. So the code's generated list would be in lex order of the combination positions, which corresponds to the numbers in the correct sorted order. Wait, 4477 is 4477, then 4747, then 4774, then 7447, then 7474, then 7744. So when sorted numerically, they are in the same order. Because when the combinations are generated in lex order (i.e., sorted by their positions), the numbers they form are in numerically increasing order. Because each next combination creates a larger number than the previous.

Wait, for example, in 4 digits:

Combinations are generated in the order:

(0,1) → 4477 (4477)

(0,2) →4747 (4747)

(0,3) →4774 (4774)

(1,2) →7447 (7447)

(1,3) →7474 (7474)

(2,3) →7744 (7744)

These are sorted in numerical order. So when generated via combinations in lex order, the numbers are already in numerical order, so no need to sort them. Wait, but is this the case? Let's see.

For example, for combinations of 2 positions in 4 digits:

The code uses itertools.combinations which returns tuples in lex order. So the first is (0,1), then (0,2), (0,3), (1,2), (1,3), (2,3). The numbers generated are:

4477 → 4477

4747 →4747

4774 →4774

7447 →7447

7474 →7474

7744 →7744.

These numbers are in order from smallest to largest, so they are already sorted. So perhaps when generating the combinations in lex order, the numbers are generated in numerical order, so no need to sort them. This would save time.

If this is the case, then the code can collect the numbers in the order generated by combinations, and they are already sorted, so no need to sort. Then, for each candidate in order, check if it is >=n, and return the first one.

This would save the time of sorting.

But why is this the case? Because each combination is generated in lex order, and the lex order of the combination corresponds to the lex order of the number when the 4s are placed in those positions.

For example, in the 4-digit case, the combinations are ordered as (0,1), (0,2), (0,3), (1,2), (1,3), (2,3). The generated numbers are 4477,4747,4774,7447,7474,7744. These are in numerical order. So the code can process them in the order generated, and the first one that is >=n is the minimal candidate in that length.

Thus, we can avoid sorting the candidates, which would save time.

This is a crucial optimization. Because for each length, instead of generating all candidates, sorting them (O(k log k) time), which could be expensive for large k, but even for k up to 5 (10 digits) it's 252 elements, but perhaps in practice, the code can generate the candidates in order, and check them in order, stopping as soon as a candidate >=n is found.

So the code can be optimized as follows:

For each length L:

   generate combinations in lex order (as per itertools.combinations).

   for each combination in order:

       generate the number as a string, then as integer.

       if the number >=n:

           return it immediately.

   proceed to next length.

This would avoid generating all candidates for a given length, but instead process them one by one, and return as soon as a valid candidate is found.

But how can we be sure that the order of combinations is such that the generated numbers are in increasing order?

Let's think: the combinations are generated in lex order. For example, for 4 digits, combinations are (0,1), (0,2), (0,3), (1,2), etc. The corresponding numbers are 4477,4747,4774,7447, etc. Which are in numerical order. Because, for example, the first combination (0,1) creates a number where the 4s are placed in the leftmost positions, leading to the smallest possible number. Each subsequent combination places the 4s in positions that are higher, leading to higher numbers.

Thus, the generated order of combinations corresponds to the numerical order of the numbers. So the code can process the candidates in the order they are generated, and return the first one that is >=n, which is the minimal possible candidate for that length.

This is a significant optimization, as it reduces the processing for each length from O(C(2k, k)) + O(C(2k,k) log C(2k,k)) to O(C(2k,k)) in the worst case, but in practice, early exit when the first candidate >=n is found.

Thus, the code can be optimized as follows:

For each even length L:

   k = L//2

   generate all combinations of k positions in lex order.

   for each combination in lex order:

       create the number as a string.

       convert to integer.

       if the number >=n:

           return it.

So, the code would process the combinations in order, and return the first candidate >=n. Because the candidates are generated in numerical order, this is correct.

So, in code:

import itertools

n = int(input().strip())

original_n = n

n_str = str(original_n)

m = len(n_str)

current_length = m if m %2 ==0 else m+1

while True:

    k = current_length //2

    # Generate combinations in lex order.

    # For each combination, create the number and check.

    for positions in itertools.combinations(range(current_length), k):

        # create the number: 4 in positions, 7 elsewhere.

        num_list = ['7'] * current_length

        for idx in positions:

            num_list[idx] = '4'

        num_str = ''.join(num_list)

        # compare with n. But converting to int may be slow for large numbers. So compare as strings?

        # but how?

        # wait, comparing as integers is straightforward but for very large numbers, but since the maximum length is 10 digits, converting to integer is manageable.

        candidate = int(num_str)

        if candidate >= original_n:

            print(candidate)

            exit()

    # After checking all candidates in this length, proceed to next even length.

    current_length +=2

Wait, but there's a problem here. For example, if the candidate is of length greater than the original n's length, then it is automatically larger. For example, if n is 4500 (4 digits) and the code checks 4-digit candidates. But if the code proceeds to check 6-digit candidates, all of which are 6-digit numbers, which are larger than 4500. So in this case, the first 6-digit candidate is 444777, which is 6 digits. So the code will generate 444777 as a candidate and return it. But this is not correct. Because the code is supposed to return the minimal possible super lucky number >=n. So in this example, the code would have found 4747 in the 4-digit candidates, which is correct. But in cases where the current_length is larger than the original number's length, all numbers of that length are larger than n, so the minimal candidate is the first candidate in that length (since they are generated in numerical order).

Thus, in code, for current_length greater than the original n's length, the first candidate generated (the minimal in that length) is the minimal possible, and can be returned immediately.

So the code can be further optimized by checking if current_length > len(n_str). If yes, then the first candidate in that length is the minimal possible, which is the answer.

So:

In each iteration:

if current_length > len(n_str):

   generate the first candidate (which is the minimal in that length), return it.

else:

   generate all candidates in order, check each.

But how to check if current_length is larger than the original length?

For example, original length is 4, current_length is 6. Then 6>4. So any 6-digit super lucky number is larger than n. So the minimal 6-digit super lucky number is 444777, which is the first candidate (with all 4s in the first 3 positions).

Thus, in code:

during the loop over current_length:

   if current_length > m:

       # the minimal candidate for this length is the first one (444...777...)

       # generate the first candidate (all 4s first, then 7s)

       # for example, for 6 digits, 444777.

       num_str = '4'*k + '7'*k

       candidate = int(num_str)

       print(candidate)

       exit()

   else:

       # generate all candidates for current_length and check in order.

But wait, the code may have to check for current_length equal to m first, and then proceed to higher lengths.

So in code:

current_length starts at min_length.

In each iteration:

   if current_length > m:

       # generate the minimal possible candidate for this length (444...777...), which is the first candidate.

       # return it.

   else:

       # check all candidates in order.

Thus, the code can be optimized by checking if the current_length is greater than m. If so, the minimal candidate in that length is the answer.

So the code can be rewritten as:

import itertools

n = int(input().strip())

original_n = n

n_str = str(original_n)

m = len(n_str)

current_length = m if m %2 ==0 else m+1

while True:

    if current_length > m:

        # the minimal candidate for current_length is the first one.

        k = current_length //2

        minimal_candidate = int('4'*k + '7'*k)

        print(minimal_candidate)

        exit()

    else:

        # process the current_length which is equal to m.

        # generate all candidates in order.

        k = current_length //2

        found = False

        for positions in itertools.combinations(range(current_length), k):

            num_list = ['7'] * current_length

            for idx in positions:

                num_list[idx] = '4'

            candidate = int(''.join(num_list))

            if candidate >= original_n:

                print(candidate)

                exit()

        # no candidate found in this length.

        current_length +=2

But wait, when current_length is equal to m, but even, but all candidates in that length are less than n. Then the code increments current_length by 2, and in the next iteration, current_length is m+2. Which is greater than m. So the code will generate the minimal candidate for that length.

But wait, suppose current_length is m (even), and after checking all candidates, none are >=n. Then current_length +=2, which is m+2. Which is larger than m. So the code returns the minimal candidate for current_length.

But in this case, the code is correct. For example, if n is 7777 (4 digits), and all 4-digit candidates are less than 7777, then the code proceeds to 6 digits, returns 444777.

But the minimal super lucky number larger than 7777 is indeed 444777.

So this optimization is correct.

Thus, this code would handle all cases correctly.

But let's test with n=7744 (which is a super lucky number of 4 digits). The code processes current_length=4. Generates candidates in order. The first candidate is4477, then4747, etc., until the last candidate is7744. Since 7744 is equal to n, the code returns it.

Another test case: n=7777 (4 digits). The code processes current_length=4. All candidates are checked. The largest is 7744. Which is less than 7777. So code proceeds to current_length=6. Then current_length=6>4, so code returns 444777.

Yes.

This optimization reduces the number of combinations generated in cases where current_length is greater than the original length. Because for example, if n is 1e9 (9 digits), current_length starts at 10 (since 9 is odd, current_length=9+1=10). Then, since 10>9, the code returns the minimal candidate for 10 digits, which is '4444477777'.

But what if the original n is 4444477777 (10 digits)? Then, current_length is 10 (even), m=10. The code generates all 10-digit candidates. Since 4444477777 is the first candidate (all 4s in the first 5 positions), it is equal to n, so the code returns it.

But if n is 4444477777 +1 (i.e., 4444477778), then the code processes current_length=10. All candidates are generated, and none are >=4444477778. So code proceeds to current_length=12, which is>10, returns 444444777777.

So this approach works.

Thus, the code can be optimized to:

- For current_length greater than the original number's length, the first candidate (minimal of that length) is the answer.

- For current_length equal to the original number's length, generate all candidates in order and check.

So the code now has two cases:

If the current_length is larger than the original length, return the minimal candidate for that length.

Else, generate all possible candidates in order (which are already sorted), and return the first one >=n.

This reduces the computational time significantly, as for current_length greater than the original length, the code doesn't need to generate all combinations, but just returns the minimal candidate.

Thus, the code is correct and efficient.

Now, considering the code's efficiency:

In the worst case, where the original n has even length and the minimal super lucky number is in that length, but requires checking all combinations, the code would generate all combinations and check them in order. For example, if n is the maximum possible 4-digit number, 7744. Then the code would generate all 6 combinations, and return 7744.

But in practice, even for the worst case of current_length=10 (1e9 input), the code would generate 252 combinations, but when current_length is 10, which is larger than the original length (9), the code would immediately return 4444477777, which is the minimal candidate of that length.

Thus, the code is optimized and will run within the time constraints.

Now, the code implementation in Python.

But wait, when current_length is greater than m, the code returns the minimal candidate, which is '4'*k + '7'*k. This is the minimal possible candidate for that length. For example, for current_length=6 (k=3), the minimal candidate is '444777'. Yes, that's correct.

Thus, the code's logic is correct.

Now, handling the case where the original length is even, but the code needs to check all candidates in that length, and none are found. For example, n=7744, but code needs to check for 4-digit candidates. The code generates all 6 candidates and returns 7744.

But if n is 7745, then after checking all 4-digit candidates (none >=7745), the code proceeds to 6-digit candidates. Since current_length=6 is larger than m=4, returns '444777'.

Yes.

Thus, the code handles all cases correctly.

Now, the code's implementation:

Read the input as integer and string.

current_length is initialized based on the input's length.

Loop:

   if current_length> m:

       generate the minimal candidate and return.

   else:

       generate all combinations for current_length, check in order.

       if found, return.

       else, current_length +=2.

This is the code.

Now, code for the problem:

import itertools

n = int(input().strip())

original_n = n

n_str = str(n)

m = len(n_str)

current_length = m if m % 2 == 0 else m + 1

while True:

    if current_length > m:

        k = current_length // 2

        minimal_candidate = '4' * k + '7' * k

        print(minimal_candidate)

        exit()

    else:

        k = current_length // 2

        for positions in itertools.combinations(range(current_length), k):

            num_list = ['7'] * current_length

            for idx in positions:

                num_list[idx] = '4'

            candidate = int(''.join(num_list))

            if candidate >= original_n:

                print(candidate)

                exit()

        current_length += 2
</think>

```python
import itertools

n = int(input().strip())
original_n = n
n_str = str(n)
m = len(n_str)

current_length = m if m % 2 == 0 else m + 1

while True:
    if current_length > m:
        k = current_length // 2
        print('4' * k + '7' * k)
        exit()
    else:
        k = current_length // 2
        for positions in itertools.combinations(range(current_length), k):
            num = ['7'] * current_length
            for i in positions:
                num[i] = '4'
            candidate = int(''.join(num))
            if candidate >= original_n:
                print(candidate)
                exit()
        current_length += 2
```
