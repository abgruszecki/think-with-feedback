<think>
Okay, I need to solve this problem where Masha has some cubes, and we need to find the maximum x such that all numbers from 1 to x can be formed using those cubes. Let's think about how to approach this.

First, let's understand the problem. Each cube can be rotated to show any of its 6 faces. When building a number, you select some subset of cubes (all if needed), arrange them in a row, and read the digits from their upper faces. The number can't have leading zeros, so the first digit can't be zero. Also, digits 6 and 9 are considered different; you can't swap them.

The constraints say n can be up to 3. So for numbers with 1 digit, we need to check if each digit 1-9 is present on at least one cube. For two-digit numbers, each number from 10 to 99 (but wait, wait, no. Wait, the numbers start at 1. So x is the largest where every number from 1 to x is present. So for example, if we can form 1, 2, ..., 87, but not 88, then the answer is 87.

So the approach is: check for all possible numbers starting from 1 upwards until we find the maximum x where all numbers up to x are possible.

But how to efficiently check if all numbers up to x can be formed with the given cubes?

First, generate all possible numbers of various lengths and check each one. The maximum x would be the largest consecutive sequence starting from 1 where each number is present.

But how do we check if a number can be formed with the cubes?

Let's think about how numbers are built. For a number with k digits, we need to select k distinct cubes (since each digit is placed on a cube, and you can't reuse a cube for multiple digits). For each digit in the number, there must be a cube that has that digit (on any face), and each cube is used exactly once in the digit positions.

Wait, no. For a k-digit number, you need exactly k cubes. Because each digit in the number comes from a different cube. Because you can't use the same cube twice in a single number. So the selection is choosing a subset of k cubes (if n >=k) and arrange them in order.

Wait, the problem says: "the number can't contain leading zeros. It's not required to use all cubes to build a number." So for a k-digit number, you use exactly k cubes, selected from the available n, and each cube is used once. So for example, if n=3, a 2-digit number would use any two of the three cubes.

So for each number, we need to check if there's a way to arrange a subset of k cubes (k being the number of digits) such that each digit in the number is present on the corresponding cube, considering that each cube is used exactly once.

So, the steps to solve the problem:

1. Precompute all possible numbers starting from 1, checking each in order until we find the maximum x where all 1..x are possible.

2. For each number, check if it can be formed using some subset of cubes.

The key challenge is efficiently checking for each number whether it can be formed with the available cubes.

Let's think about the steps for checking a number.

For example, take the number 87. It's two digits. We need two cubes. Each cube must have the corresponding digit (8 and 7) in their faces. But the cubes can be arranged in any order. Wait, the cubes are arranged in a row. So the digits are in order, but the selection of cubes must be a permutation. For example, 87 can be formed by cube A (with 8) and cube B (with 7), arranged as A followed by B. Or cube B followed by A, but that would give 78, which isn't the number. So the order of the cubes matters as per the digits of the number.

Wait, but the cubes can be arranged in any order. So for the number 87, the first digit is 8 and the second is 7. So the first cube in the arrangement must have 8, the second cube must have 7. So the permutation is important.

So for a number with digits d_1 d_2 ... d_k, we need to check if there exists a permutation of k distinct cubes (selected from the n cubes) where the first cube in the permutation has d_1, the second has d_2, etc.

Therefore, for each number, we need to split its digits into a list (like [8,7] for 87), and then check if there's a way to select k cubes (k is the length of the number), permute them, and each cube in the permutation has the corresponding digit.

So for the number 12, digits [1, 2], we need to find two cubes where one has 1 and the other has 2, and arrange them in order.

So the approach is:

For a given number, generate its digits as a list. Let k be the length. Then, generate all possible permutations of k cubes (without replacement) from the available n cubes, and check if any permutation satisfies that the i-th cube in the permutation has the i-th digit.

But for numbers up to, say, 999 (which is the maximum possible with 3 cubes), the permutations are manageable.

But considering that n can be up to 3, the permutations for k=3 would be 3P3 = 6, for k=2, 3P2=6, etc.

So for each number, the checking process would involve generating all possible permutations of the cubes (subset of size k) and checking if any of them can form the number.

But how to implement this efficiently?

Let's think about precomputing the possible digits for each cube. Each cube has a set of digits. For example, cube 0's digits are {0,1,2,3,4,5}, etc. Then, for a number's digits [d0, d1, ..., dk-1], we need to find a permutation of k cubes (each cube is unique) such that each cube in the permutation has the corresponding digit.

So the problem reduces to: given a sequence of digits (the number's digits), can we select a permutation of k distinct cubes where each cube in the permutation has the respective digit in the sequence.

So for example, for the number 87, the digits are [8,7]. So we need to find two distinct cubes, where one has 8 and the other has 7, arranged in the order [8,7]. But the permutation could be cube A (8) followed by cube B (7), or cube B (7) followed by cube A (8), but wait, in that case, the digits would be 78. So for the number 87, the permutation must have cube with 8 first, then cube with 7.

So the permutation order is critical. For each digit in the number, the cube in that position must have that digit.

Therefore, for the number's digits, the checking process is: for any permutation of k distinct cubes (selected from n cubes), check if each cube in the permutation has the corresponding digit.

So how can we efficiently check this?

An approach is to generate all permutations of k cubes (all possible k-length permutations of the n cubes), and for each permutation, check if each cube in the permutation has the required digit.

If any permutation satisfies this, then the number can be formed.

But for small values of n (up to 3), and k up to 3, this is manageable.

For example, with n=3, checking all possible permutations for k=3 would be 6 permutations. For k=2, 3P2=6 permutations. For k=1, 3 possibilities. So for each number, the checking is O(k! * C(n, k))?), but since n and k are small, this is feasible.

Now, the plan is:

1. Generate all numbers starting from 1 upwards, in order. For each number x, check if it can be formed.

2. Once a number x is found that can't be formed, the answer is x-1. If all numbers up to a certain point can be formed, that's the answer.

But how to determine up to which number we need to check?

The maximum possible x when n=3 is 3 digits. For example, 987, but perhaps higher. But since each cube can contribute a digit, the maximum possible x with 3 cubes is 999 (if possible). But perhaps the cubes don't have the digits. So the maximum possible x is 999, but maybe not.

But how to find all possible numbers up to 999, but that's 999 numbers. But for each, the checking would be manageable.

But even with 999 numbers, and for each number up to 999, for each digit in the number, generate all permutations of cubes (with length k) and check if any permutation's cubes have the required digits.

So for the code:

First, for each cube, precompute the set of digits it has. Because for a cube to contribute a digit, that digit must be in its set.

So for each cube i, create a set s_i of its digits.

Then, for a given number x:

- Convert x to a list of digits, e.g., x=87 → [8,7].

- Let k be the length of the digits list.

- If k > n, then x is impossible (since you need k cubes but have n <k). So such x can't be formed, and thus x would break the sequence.

- Else, generate all possible permutations of k cubes from the n available.

- For each permutation of k cubes, check for each position i (0 to k-1), whether the cube in that permutation has the digit in the i-th position of the digits list.

- If any permutation satisfies this, then x is possible.

If x=1, k=1. Check if any cube has 1.

So the code can proceed as follows.

Now, the steps for the code:

Read n.

Read n lines, each with 6 digits. For each cube, create a set of its digits. So cubes = [set1, set2, set3...]

Then, generate numbers starting from 1 upwards. For each x in 1, 2, 3...:

Check if x can be formed. If not, return x-1. If yes, proceed.

But how to generate all possible x until the first x that is invalid?

But the maximum x possible is when all numbers up to x can be formed, but x+1 cannot. So for example, if all numbers up to 987 can be formed, but 988 can't, the answer is 987.

But how do we know when to stop? For example, with 3 cubes, the maximum possible x is 999 if all possible numbers up to that can be formed. But if even 999 can be formed, then we return 999. So we need to check all possible x up to 999 (since n is at most 3).

Wait, but for 3 cubes, the maximum possible x is 999. Because with 3 digits, each cube is used once. But for numbers with 1, 2, or 3 digits.

So for x=1, check if any cube has 1.

For x=10, check if there's a cube with 1 (for the first digit) and a cube with 0 (second digit). But since leading zeros are not allowed, but 10 is okay (the first digit is 1, second is 0).

So the code can loop x from 1 upwards, check each, and once an x is found that can't be formed, return x-1.

But how to loop up to the maximum possible x, which depends on n.

For n=1, the maximum possible x is 9 (if the cube has all digits 1-9). But if the cube has 0, but no other digits, then the maximum x is 0. For example, if the cube only has 0, then 1 cannot be formed, so answer is 0.

So the code can proceed by:

Initialize the answer as 0. Then, for x starting from 1, check if x can be formed. If yes, update the answer to x. Continue until x is such that it can't be formed. Then, the answer is the previous x.

But how to know when to stop checking? Because for n=3, the maximum possible x is 999. So for x up to 999, if all can be formed, then the answer is 999. But if some x in between can't be formed, then the answer is x-1.

So the code can generate x from 1 up to 999 (for n=3), 99 (for n=2), 9 (for n=1). Wait, but if n=2, can you form 99? You need two cubes, each with 9. So yes, if two cubes have 9.

So the code can loop x from 1 to the maximum possible for the given n, which is 10^3 -1 for n=3 (999), 99 for n=2, 9 for n=1.

But wait, for n=3, x can be up to 999. So the code can generate x from 1 to (10^n -1), which is 999 for n=3.

But for each x in this range, check if x can be formed.

Once the code finds the first x that can't be formed, return x-1. If all x up to 999 (for n=3) can be formed, then return 999.

So, the code steps:

Read n, then the cubes.

For x in 1 to max_possible (based on n):

   if can_form(x):

      answer = x

   else:

      break and return answer

So the code will check each x in order. The answer is the maximum x where all 1..x are formable.

Now, how to implement 'can_form' function.

The 'can_form' function for x:

1. Convert x into a list of digits as a list (digits), e.g., x=87 → [8,7].

2. k = len(digits). If k > n: return False.

3. Generate all possible permutations of k cubes from the n cubes.

4. For each permutation (cube indices, order matters), check:

   For each position i in 0..k-1:

      cube = cubes[permutation[i]]

      if digits[i] not in cube's digits: break, this permutation is invalid.

   If all positions are valid, return True.

5. If no permutation works, return False.

Now, how to generate all permutations of size k from n cubes. For example, if n=3 and k=2, permutations are (0,1), (0,2), (1,0), (1,2), (2,0), (2,1) — all possible orderings of selecting 2 out of 3.

In Python, this can be done with itertools.permutations.

So for each x, we can generate digits, check if k is >n. Then, generate all possible permutations of k cubes (using itertools.permutations with r=k), and for each permutation, check if each cube in the permutation has the corresponding digit.

Yes. So the code can use itertools.permutations.

Now, the code outline:

Read n.

Read n cubes: for each, create a set of digits.

max_possible = 10**n -1  (for n=3: 999; n=2: 99; n=1:9)

ans = 0

for x in 1 to max_possible:

   digits = list of digits of x as integers.

   k = len(digits)

   if k > n:

      continue? Or break, but no. Wait, because if n=3, x=100 has k=3, which is allowed. So, if k >n, then x can't be formed, so return False. So in can_form(x), if k>n, return False.

   if can_form(x, digits, cubes, n):

      ans = x

   else:

      break

return ans

But how to loop x from 1 upwards until the first failure, and return the last x that was good.

So the code would:

Initialize ans = 0.

for x in 1, 2, ...:

   if x's digits length >n: then break, since can't form x. So for example, if n=1 and x=10, which is 2 digits, which requires 2 cubes. So can't form it. So once x reaches 10 (for n=1), all x >=10 can't be formed. So the loop can stop when x exceeds the max_possible.

Wait, the max_possible is 10^3 -1 for n=3. So the loop can iterate x from 1 to max_possible. For each x in that range, check can_form(x). If any x in this range can't be formed, then the answer is x-1, and break. If all can be formed, return max_possible.

So the code:

max_possible = 10**n -1

ans = 0

for x in range(1, max_possible +1):

   digits = list(map(int, list(str(x))))

   k = len(digits)

   if k >n:

       # can't form x, break the loop

       break

   # check if can form x

   # generate all permutations of k cubes

   # permutations of length k from 0..n-1, with no repetition

   found = False

   for perm in itertools.permutations(range(n), k):

       valid = True

       for i in range(k):

           cube_index = perm[i]

           if digits[i] not in cubes[cube_index]:

               valid = False

               break

       if valid:

           found = True

           break

   if not found:

       # x can't be formed. So the answer is the previous max x, which is ans.

       break

   ans = x

# Now, after the loop, check if x was the max_possible. If the loop completed all x up to max_possible, then ans is max_possible. Otherwise, ans is the last x that was valid.

if ans == max_possible:

   print(ans)

else:

   print(ans)

Wait, no. Because in the loop, for x in 1 to max_possible:

   check if can form x.

   if yes, ans =x.

   else, break.

So for example, if x=87 is the last possible, then ans would be 87. Then, the loop breaks, and the code returns 87.

So the code after the loop would print ans.

So that's correct.

Now, let's test this approach against the examples.

First example:

Input:

3

0 1 2 3 4 5

6 7 8 9 0 1

2 3 4 5 6 7

The cubes are:

Cube0: {0,1,2,3,4,5}

Cube1: {0,1,6,7,8,9}

Cube2: {2,3,4,5,6,7}

The sample output is 87.

So, all numbers up to 87 can be formed, but 88 cannot.

Check why 88 can't be formed: the digits are 8 and 8. So need two different cubes with 8.

Looking at the cubes:

Cube1 has 8, cube0 and cube2 do not. So only one cube (cube1) has 8. So 88 needs two 8s, but only one cube can contribute an 8. So 88 is impossible. Hence, answer is 87.

So the code should find that 88 is not possible, break the loop, and return 87.

The code will loop x from 1 to 999 (since n=3, max_possible is 999). For each x, check.

Now, the code will check 88. The digits are [8,8]. k=2. So permutations are 2 cubes from 3.

So possible permutations are all possible 2-length permutations of the 3 cubes. So possible permutations are (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (0,0 is invalid because permutations are distinct indices), wait no: permutations of (n, k) is all possible ordered selections of k distinct elements. So for n=3 and k=2, permutations are 3*2=6 possibilities.

For each permutation:

Check if first cube has 8, and second cube has 8.

But cube0: has 0,1,2,3,4,5 → no 8.

Cube1: has 0,1,6,7,8,9 → yes 8.

Cube2: has 2,3,4,5,6,7 → no 8.

So the permutations are:

(0,1): cube0 (no 8) first digit → invalid.

(0,2): cube0 (no 8) first → invalid.

(1,0): cube1 (has 8) first, cube0 (second digit 8? cube0 has no 8. So for x=88, the digits are 8 and 8. So in permutation (1,0), first cube (cube1) has 8 (good), second cube (cube0) must have 8 → cube0 doesn't. So invalid.

Permutation (1,2): cube1 (8) and cube2 (needs 8, which cube2 doesn't have). So invalid.

Permutation (2,1): cube2 (no 8) first → invalid.

Permutation (2,0): cube2 (no 8) → invalid.

Thus, no permutation can form 88. Hence, the code breaks at x=88 and returns ans=87.

Which matches the sample.

Second example:

Input:

3

0 1 3 5 6 8

1 2 4 5 7 8

2 3 4 6 7 9

Sample output: 98.

So all numbers up to 98 are possible.

Check 99: digits are [9,9]. The cubes must have two 9s.

Looking at the cubes:

Cube0's digits: 0,1,3,5,6,8 → no 9.

Cube1's digits: 1,2,4,5,7,8 → no 9.

Cube2's digits: 2,3,4,6,7,9 → has 9.

So only cube2 has 9. So to form 99, need two 9s, but only one cube can contribute a 9. So 99 is impossible. So 98 is the answer.

So the code would check x=98: can it be formed?

Digits [9,8]. k=2.

Check permutations of two cubes.

Possible permutations: (0,1), (0,2), (1,0), (1,2), (2,0), (2,1).

Check if any permutation allows the first cube to have 9, second to have 8.

Cube0: 0,1,3,5,6,8 → 8 is present. Cube1: 8 is present. Cube2: 9 is present.

Wait, for the digits 9 and 8. The first digit is 9, second is 8.

So the first cube in the permutation must have 9, the second must have 8.

Which cubes have 9?

Only cube2.

Which cubes have 8?

Cube0 and cube1.

So possible permutations where first cube is 2 (has 9), and second is 0 or 1 (has 8).

So permutations (2,0) and (2,1).

Check:

For permutation (2,0):

cube2's digits: 2,3,4,6,7,9 → yes for 9.

cube0's digits: 0,1,3,5,6,8 → yes for 8.

So this permutation works. So 98 can be formed.

Thus, x=98 is possible. Then x=99 is not possible. So the answer is 98.

Thus, the code would return 98.

Now, the code's approach seems correct.

Now, the code in Python.

But in Python, for n=3, checking up to 999 numbers. For each number, for k=1,2,3, permutations of k cubes.

But for k=3, the permutations are 3! =6 possibilities.

For each x, the code will generate permutations and check. But 999 * 6 (for k=3) is 5994 checks. But for k=2, permutations are 3P2=6 per x. For 99 numbers of 2 digits, 99 *6=594. For k=1, 9 numbers, each with 3 possibilities.

So total operations are manageable.

So the code is feasible.

Now, code steps:

Import itertools.

Read n.

Read n lines. Each line has 6 numbers. For each line, create a set of integers. So cubes = [set(), set(), set() ... ]

Then, compute max_possible = 10**n -1.

Initialize ans=0.

Loop x from 1 to max_possible inclusive:

   digits = list of digits of x as integers.

   k = len(digits).

   if k >n → can't form x → break the loop.

   generate all permutations of k cubes (indices).

   for each permutation in itertools.permutations(range(n), k):

       check each digit in digits against the cube's set.

       if all digits are present in the permutation's cubes, then x is possible.

   if any permutation works → continue and set ans=x.

   else → break loop and return ans.

After the loop, print ans.

Now, code:

But in Python, for converting x to digits:

digits = list(map(int, str(x)))

Yes.

Now, code:

import itertools

n = int(input())
cubes = []
for _ in range(n):
    faces = list(map(int, input().split()))
    cubes.append(set(faces))

max_possible = 10**n -1
ans = 0

for x in range(1, max_possible +1):
    s = str(x)
    k = len(s)
    if k > n:
        break  # can't form x, since need more cubes than available
    digits = list(map(int, s))
    # check all permutations of k cubes from n
    found = False
    for perm in itertools.permutations(range(n), k):
        valid = True
        for i in range(k):
            cube_idx = perm[i]
            if digits[i] not in cubes[cube_idx]:
                valid = False
                break
        if valid:
            found = True
            break
    if not found:
        break
    ans = x

print(ans)

This code should work.

Testing the first sample:

Cubes are:

Cube0: {0,1,2,3,4,5}

Cube1: {0,1,6,7,8,9}

Cube2: {2,3,4,5,6,7}

When x=88, digits are [8,8]. k=2. Need two cubes.

Check all permutations of 2 cubes:

Possible permutations are all 2-length permutations of 0,1,2.

For each:

(0,1): cube0 and cube1. digits[0]=8 → cube0 doesn't have 8. invalid.

(0,2): cube0 (no 8). invalid.

(1,0): cube1 (has 8), cube0 (digits[1]=8? cube0 has no 8. invalid.

(1,2): cube1 (8) first, cube2 (digits[1] is 8? cube2 has 6,7, etc. No. invalid.

(2,0): cube2 (digits[0] is 8? cube2 has 2,3,4,5,6,7. No. invalid.

(2,1): cube2 (no 8). invalid.

So no permutation is valid. Thus, code breaks and returns 87.

Second sample:

Cubes:

0 1 3 5 6 8 → set {0,1,3,5,6,8}

1 2 4 5 7 8 → set {1,2,4,5,7,8}

2 3 4 6 7 9 → set {2,3,4,6,7,9}

For x=98:

digits are [9,8]. Check permutations of 2 cubes.

Possible permutations:

(0,1): cube0 (digits[0]=9? cube0 has 0,1,3,5,6,8 → no. invalid.

(0,2): cube0 (no 9). invalid.

(1,0): cube1 (digits[0]=9? cube1 has 1,2,4,5,7,8 → no. invalid.

(1,2): cube1 (no 9). invalid.

(2,0): cube2 has 9 (digits[0] yes), cube0 (digits[1] 8. cube0 has 8 → yes. So this permutation is (2,0). So valid.

So x=98 is possible. Then x=99: digits [9,9]. k=2. Need two cubes with 9. Only cube2 has 9. So permutations must use cube2 twice, but permutations are for distinct cubes. So no. So can't form 99. The code will break at x=99 and return 98.

Thus, the code works.

Thus, the code should be correct.
</think>

```python
import itertools

n = int(input())
cubes = []
for _ in range(n):
    faces = list(map(int, input().split()))
    cubes.append(set(faces))

max_possible = 10**n - 1
ans = 0

for x in range(1, max_possible + 1):
    s = str(x)
    k = len(s)
    if k > n:
        break
    digits = list(map(int, s))
    found = False
    for perm in itertools.permutations(range(n), k):
        valid = True
        for i in range(k):
            if digits[i] not in cubes[perm[i]]:
                valid = False
                break
        if valid:
            found = True
            break
    if not found:
        break
    ans = x

print(ans)
```