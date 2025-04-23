<think>
Okay, let's tackle this problem. Hmm, the task is to determine if a group of integers is friendly. So, a friendly group is one where every pair of integers are friends. And two integers are friends if one divides the other. 

So, the problem reduces to checking for all pairs in the group whether each pair (a, b) has a divides b or b divides a. If even one pair doesn't satisfy this, the group isn't friendly. But checking all pairs could be time-consuming if the group is large. Wait, the constraints say n can be up to 1000. The number of pairs is n*(n-1)/2. For n=1000, that's about 500,000 pairs. Checking each pair's divisibility might be feasible, but maybe there's a smarter way.

Wait, but even 500,000 operations are manageable in Python, especially since each check is a simple modulo operation. So the brute-force approach of checking all pairs might be acceptable here. But maybe there's a way to optimize.

Alternatively, perhaps the group can be structured in a way that all elements are multiples of the smallest element. Or maybe the entire group is such that they form a chain where each element is a multiple of the previous one. But no, that's not necessarily the case. For example, the sample input 1,3,6,12. Here, 1 divides all, 3 is divided by 6 and 12. So the group is friendly. But 3 and 1: 3 is not a divisor of 1. So in that case, the smallest element might be the one that divides all others. Wait, in that example, the smallest element is 1. So all elements are multiples of 1, which makes them pairwise friends. Wait, no. Wait, in that example, 1 is a divisor of every other element, so for every pair that includes 1, they are friends. But the other pairs, like 3 and 6: 3 divides 6. 6 and 12: yes. 3 and 12: yes. So all pairs here are friends. So the group is friendly.

But what's the pattern here? If all elements are multiples of the first element (the smallest one), then every element can be divided by the first element. So for any two elements a and b, if the first element divides both, then a and b may or may not divide each other. Wait, no. For example, if the first element is 2, and there are elements 2,4,6. Then 4 and 6: 4 doesn't divide 6 and 6 doesn't divide 4. So the group would not be friendly. So the initial thought is incorrect.

Hmm. So the key is that for any two elements in the group, one must divide the other. So how can this condition be satisfied for all pairs?

One possible structure is that all elements are the same. For example, [6,6,6]. Then every pair is friends. Alternatively, the elements form a chain where each element is a multiple of the previous one, but that's not sufficient. For example, 2,4,8 would work. Each element divides the next, so all pairs are friends. But if the group is 2,4,16, then 4 and 16 are friends, 2 and 4 are friends, but 2 and 16: 2 divides 16. So that's okay.

Alternatively, the group can be such that all elements are divisors of the maximum element. Then for any two elements, a and b, if a divides the maximum and b divides the maximum, then a divides b or b divides a? No. For example, 2,4,6. The maximum is 6. 2 divides 6, 4 does not divide 6. So in that group, 2 and 4 would not be friends. So that's not a valid approach.

So perhaps the only way to have all pairs be friends is that all elements are multiples of the smallest element, and arranged in a way that each element is a multiple of all previous ones. But I'm not sure.

Alternatively, maybe the group must form a set where every element is a multiple of the smallest element and all elements are arranged in a chain where each element is a multiple of the previous. But that's not necessarily required.

Wait, perhaps the necessary and sufficient condition is that all elements are multiples of the smallest element, and for any two elements, the larger one is a multiple of the smaller one. Because then, for any pair, the smaller one divides the larger. So if that's the case, then the group is friendly.

So the steps to check could be:

1. Find the smallest element in the group. Let's call it m.
   Since the input is sorted in non-decreasing order, the first element is the smallest. So m is the first element.

2. Check that all other elements are multiples of m. Because if any element is not a multiple of m, then m (the smallest) cannot divide it, so that pair (m and that element) is not friends, so the group is not friendly. So this is a necessary condition.

But even if all elements are multiples of m, it's not sufficient. For example, elements 2,4,6. All multiples of 2. But 4 and 6: neither divides the other. So the group is not friendly. So the condition is necessary but not sufficient.

So how to proceed?

Another approach: For the group to be friendly, all elements must form a chain where each element divides the next one. But that's only possible if the group is sorted in non-decreasing order, which it is. Wait, but even in that case, all elements after the first must be multiples of the first, but also each subsequent element must be a multiple of the previous. Because otherwise, there would be elements where a previous element doesn't divide a later one. For example, 2,4,8: works. 2 divides 4, 4 divides 8, etc. All pairs are friends. But if the list is 2,6,12: 2 divides 6, 6 divides 12. But then, 2 and 12: 2 divides 12, which is okay. So this would work. But in this case, each element divides the next.

But what if the elements are 2,4,6,12. Let's see:

Check 2 and 4: okay. 2 and 6: okay. 2 and 12: okay. 4 and 6: 4 doesn't divide 6, 6 doesn't divide 4. So the group is not friendly. So even if the elements are sorted and each is a multiple of the first, but there exists a pair where neither divides the other, the group is not friendly. So the only way to ensure that all pairs are friends is that for every pair (a, b), one divides the other.

So the brute-force approach is to check all possible pairs. For n=1000, that's 1000*999/2 = 499,500 pairs. Each check is O(1) (check if a divides b or b divides a). That's manageable in Python even for 10^6 operations. So for n=1e3, 5e5 operations is acceptable. Let's see: each pair is checked by two mod operations. But wait, for each pair (a, b), assuming a <= b (since the list is sorted), then we only need to check if a divides b. Because if a <= b, then a can't be larger than b, so if a divides b, then it's okay. Otherwise, since the list is sorted, the other elements would be >= b, so this pair (a, b) would not be friends. Wait, no. Because even if a doesn't divide b, but some other elements could be friends. Wait, no. The list is sorted, so for each pair (i, j) where i < j, a_i <= a_j. So for the pair (a_i, a_j), if a_i divides a_j, then it's okay. If not, then the pair is not friends, so the entire group is invalid. So for all pairs i < j, check if a_i divides a_j. Because a_i <= a_j, so if a_i doesn't divide a_j, then the pair isn't friends. So we can optimize the check by only considering pairs where i < j, and check if a_i divides a_j. This reduces the number of pairs to check by half, but it's already part of the initial approach.

Wait, but wait: the problem says two integers are friends if either divides the other. So for a pair (a, b), where a <= b, if a divides b, then they are friends. If not, then if b divides a, but since a <= b, that's only possible if a == b. So in that case, if a divides b (since a and b are equal, 0 mod is 0). So the only way a pair (a, b) with a <= b is friends is if a divides b. So for all pairs where a <= b, we need to check if a divides b. So this simplifies the check.

So the algorithm can be: for each pair of elements (i, j) where i < j, check if a[i] divides a[j]. Because a[i] <= a[j] (since the list is sorted), so for the pair to be friends, a[i] must divide a[j]. If any such pair does not satisfy this, output "NOT FRIENDS". Otherwise, output "FRIENDS".

Wait, but what about the case where two elements are equal? For example, 6 and 6. Then each divides the other. But in that case, when i < j, a[i] == a[j], so a[i] divides a[j], so it's considered as friends.

So this approach works. So the algorithm is:

Sort the list (but input is already sorted in non-decreasing order). For each j from 1 to n-1, for each i from 0 to j-1, check if a[i] divides a[j]. If any pair fails, return false.

Wait, no. Because for the pair (i, j), since the list is sorted, a[i] <= a[j]. So we just need to check for all j in 1..n-1, and for each j, check all i in 0..j-1 whether a[i] divides a[j]. Because if any a[i] does not divide a[j], then the pair (i, j) is not friends. So this way, all pairs are checked. Because for any pair (k, l) where k < l, the check is when j = l and i = k. So that's all pairs.

Wait, no. Because in this approach, for j, we check all i < j, but for each i < j, check if a[i] divides a[j]. But that's not all possible pairs. Because, for example, if we have elements a, b, c, sorted as a <= b <= c. Then in the approach, for j=2 (c), we check a divides c and b divides c. But the pair (b, a) is not checked, but since a <= b, that's not a problem. Wait, no. Because the pairs are (i, j) where i < j, so all possible pairs where j is larger than i. So for a sorted list, each pair (i, j) with i < j is considered once, and in each case, a[i] <= a[j], so checking if a[i] divides a[j] is sufficient. Because if a[i] doesn't divide a[j], then the pair (i, j) is invalid. For pairs where i > j, but that's not possible in the loop structure.

Wait, the loop is for j from 1 to n-1, and for each j, i ranges from 0 to j-1. So all possible pairs (i, j) with i < j are checked. So for each such pair, we check a[i] divides a[j]. If any of these checks fail, the group is not friendly.

So the algorithm is:

For each j from 1 to n-1:

   For each i from 0 to j-1:

      if a[i] divides a[j], continue.

      else, return False.

If all pairs pass, return True.

But wait, for j=2 (third element), the checks are i=0 and i=1. So a[0] divides a[2], and a[1] divides a[2]. So, for example, in the first sample input:

elements are 1,3,6,12.

j=1 (3):

i=0: 1 divides 3 → yes.

j=2 (6):

i=0: 1 divides 6 → yes.

i=1: 3 divides 6 → yes.

j=3 (12):

i=0: 1 divides 12 → yes.

i=1: 3 divides 12 → 12/3 is 4, yes.

i=2: 6 divides 12 → yes.

So all checks pass.

In the second sample input: 1,2,9.

Check for j=1 (2):

i=0: 1 divides 2 → yes.

j=2 (9):

i=0: 1 divides 9 → yes.

i=1: 2 divides 9 → no. So the check fails, return false.

So this approach works for the samples.

Now, the problem is, for n=1000, the number of pairs is 1000*999/2 = 499,500. For each pair, perform a divisibility check. But in Python, even 1e6 operations are manageable in 2 seconds. So 5e5 is acceptable.

But perhaps there's a way to optimize this. For example, once we find a pair that fails, we can immediately return "NOT FRIENDS". So in the worst case (when all pairs are valid), we need to check all pairs, but in the best case (some early failure), we can exit early.

Another optimization: for each j, check all i from 0 to j-1. But for i=0, if a[0] does not divide a[j], then the entire group is invalid. Because a[0] is the smallest element, and if it doesn't divide a[j], then the pair (0, j) is invalid. So for each j, first check if a[0] divides a[j]. If not, return false immediately. Then, for the other i's (i >0) up to j-1, check if a[i] divides a[j]. Because if a[0] divides a[j], but some a[i] (i>0) doesn't divide a[j], then the pair (i,j) is invalid.

Wait, but the logic is that a[i] must divide a[j]. So for any i < j, a[i] divides a[j]. So for each j, the element a[j] must be a multiple of all a[i] for i < j.

So a[j] must be a multiple of all previous elements. Because if any of the previous elements doesn't divide a[j], then the pair (i,j) is invalid.

Thus, for each j, a[j] must be a multiple of all a[i] where i < j.

So, for j=2, a[2] must be a multiple of a[0] and a[1].

So, for each j, if a[j] is not a multiple of all previous elements, then the group is invalid.

Therefore, the algorithm can be optimized as follows:

For each j from 1 to n-1:

   Check if a[j] is divisible by all a[i] for i < j.

   If not, return false.

But how to check that efficiently.

Wait, but for j elements, the check is whether a[j] is divisible by all a[i] where i < j.

Because a is sorted in non-decreasing order, a[i] <= a[j] for i < j. So for a[j] to be divisible by a[i], a[i] must be a divisor of a[j].

So the check is, for each j, check that a[j] is divisible by every a[i] where i < j.

But how to do this efficiently.

Well, for each j, we can iterate through all i from 0 to j-1, and check if a[i] divides a[j]. But that's the same as the initial approach.

But perhaps there's a smarter way. For example, if a[j] is divisible by a[i], then it's automatically divisible by all divisors of a[i]. But I don't think that helps here.

Alternatively, perhaps once a[j] is divisible by a[i], then for larger i's, it's not necessary to check all. No, because even if a[j] is divisible by a[i], but not by a[i+1], it's still invalid.

So for each j, the only way to confirm that a[j] is divisible by all previous elements is to check each previous element.

Thus, the algorithm remains O(n^2), which for n=1000 is 1e6 operations, which should be acceptable.

But maybe we can optimize by pre-checking some elements. For example, if a[j] is divisible by a[i], but a[i] is not a divisor of a[j], then the check fails.

Wait, that's not helpful.

Another thought: The group must form a chain where each element is a multiple of all the previous elements. So, for example, a[j] must be a multiple of the maximum element in the previous elements.

Wait, no. For example, in the sample input 1,3,6,12: 3 is not a multiple of 1, but 1 divides 3. Wait, 3 is a multiple of 1. Oh right. So each element is a multiple of the previous elements. Because 3 is a multiple of 1. 6 is a multiple of 1 and 3. 12 is a multiple of all previous. So for each element, it's a multiple of all previous. That's required. Because if any element is not a multiple of a previous element, then that pair would not be friends.

So the key is that each a[j] must be a multiple of all a[i] for i < j. Because the list is sorted, so a[i] <= a[j], so the only way for a[i] and a[j] to be friends is if a[i] divides a[j].

So the algorithm can proceed as:

For each j from 1 to n-1:

   for each i from 0 to j-1:

      if a[j] % a[i] != 0 → return "NOT FRIENDS".

If all pass → return "FRIENDS".

So in code:

Read n.

Read the list as integers, split by commas.

Check if n is 1 → then, only one element. All pairs (none) are friends → output "FRIENDS".

Else:

   for j in range(1, n):

      for i in range(j):

          if a[j] % a[i] != 0:

              print("NOT FRIENDS")

              exit.

   print("FRIENDS")

But wait, let's test this logic against the first sample:

Sample 1:

4

1,3,6,12 → list is [1,3,6,12]

j=1 (element 3):

i=0 → 3 % 1 == 0 → ok.

j=2 (element 6):

i=0 → 6 % 1 → 0, ok.

i=1 → 6 %3 → 0, ok.

j=3 (element 12):

i=0 → 12%1=0.

i=1 → 12%3=0.

i=2 →12%6=0 → ok.

All pass → FRIENDS.

Sample 2:

3

1,2,9 → list [1,2,9]

j=1 (element 2):

i=0 → 2%1=0 → ok.

j=2 (element9):

i=0 → 9%1=0 → ok.

i=1 →9%2=1 → not 0 → return NOT FRIENDS.

Which matches the sample.

Another test case: [2,4,6]

Check for j=2 (element6):

i=0 →6%2=0.

i=1 →6%4=2 → not zero → returns not friends. Which is correct.

So this approach works.

But for n=1000, this code will take O(1e6) operations. Let's think about the time.

Each iteration checks a[j] % a[i]. The modulo operation is O(1) in Python, even for large numbers. So for 1e6 operations, each taking about 1e-6 seconds (assuming 1e6 operations per second), that's 1 second. So within 2 seconds, this should be manageable.

But wait, in Python, the actual speed can vary. For example, 1e6 operations may take about 0.1 seconds. So 5e5 operations would be manageable.

But perhaps there's a way to optimize further.

Wait, what if the list contains a zero? But the problem statement says the group is non-zero integers. So the input elements are non-zero. So we don't have to handle division by zero.

Another thing to consider is that in the list, elements may be repeated. For example, [2,2,2]. Then, all pairs pass.

Now, what about the case where the list is [2,2,4,8]. Then, for j=1, i=0: 2%2=0. j=2, i=0:4%2=0, i=1:4%2=0. j=3:8%2=0, 8%2=0, 8%4=0. So all pass. So the code works.

So the code seems to handle all cases correctly.

Now, the next step is to write this code in Python, reading the input, processing it, and outputting the result.

The code steps:

Read n from input.

Read the next line, split by commas, convert to integers.

Check if n is 1: output FRIENDS.

Else, for each j in 1 to n-1:

   for each i in 0 to j-1:

      if a[j] mod a[i] is not zero → print NOT FRIENDS and exit.

If all checks passed, print FRIENDS.

But in Python, using nested loops could be slow for n=1000. Wait, but 1000*1000/2 is 500,000 operations. Let's see:

In Python, loops are not as fast as in compiled languages. But even 1e6 operations can be handled in Python in about 0.1 seconds. Let's test.

But perhaps we can optimize the code.

Wait, for each j, the code checks all i < j. But once any i in that range for j has a[j] not divisible by a[i], we can break and return early.

But in the worst case (when all pairs are valid), we have to check all pairs. But in cases where there's an early failure, like the second sample, it exits early.

Another possible optimization: for j from 1 to n-1:

   Check if a[0] divides a[j]. If not, return not friends. Because a[0] is the smallest element. If a[j] is not divisible by a[0], then the pair (a[0], a[j]) is not friends, so the entire group is invalid.

So, for each j, first check a[0] divides a[j]. If not, return. Then, check the other i's.

But this may not save much time. For example, in a case where a[0] is 1. Then, all a[j] must be divisible by 1, which is always true. So the check for a[0] is redundant. But for cases where a[0] is not 1, this could save time. For example, if a[0] is 2, and some a[j] is 3. Then the check for a[0] would immediately fail.

So perhaps for each j, first check a[0] divides a[j]. If not, return false. Then, check the other i's in 1..j-1.

Wait, but even if a[0] divides a[j], but some a[i] (i >=1) does not divide a[j], then it's invalid.

But the code would need to check all i in 0..j-1. But by first checking a[0], which is the first element, perhaps we can early exit for some j's. For example, if a[0] is 2, and a[j] is 5 → 5%2 is 1 → exit. So in this case, j=1, and after checking i=0, the code returns. So the other i's (if any) are not checked.

But this is already handled in the original code, as in the original code, for each j, the code checks i from 0 to j-1, in order. So if a[0] doesn't divide a[j], then the code returns immediately for that j, without checking other i's. So the original code already has this optimization.

So perhaps the code can proceed as written.

But in Python, for large n, even 1e3, the code may take some time. Let's think of possible optimizations.

Wait, perhaps in Python, the inner loop can be optimized using list comprehensions or generators, but for early exits, it's better to use loops with breaks.

But in the original approach, the code checks each i for a given j. As soon as any i fails, the code exits. So the code is written as:

for j in range(1, n):

    for i in range(j):

        if a[j] % a[i] != 0:

            print("NOT FRIENDS")

            exit()

So the inner loop for i in range(j) is from 0 to j-1. So for j=1, i is 0. For j=2, i is 0,1. etc.

So in code:

Read n.

s = input().split(',')

a = list(map(int, s))

if n == 1:

    print("FRIENDS")

else:

    for j in range(1, n):

        for i in range(j):

            if a[j] % a[i] != 0:

                print("NOT FRIENDS")

                exit()

    print("FRIENDS")

But in Python, using exit() may not be the best way, but for code golfing, perhaps using sys.exit. So to exit, we can import sys and call sys.exit.

Wait, the code must read input via input(), and write via print(). So the code should be:

In Python, 'exit()' is a function in the sys module. So the code should import sys.

Wait, but in Python, when you call exit(), it's a built-in function, but in practice, when you call it with a message, it may not work. So better to import sys and use sys.exit().

But to print the message and exit, perhaps:

But in the code, after checking, when a pair fails, the code needs to print "NOT FRIENDS" and terminate. So the code would be:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    if n == 1:

        print("FRIENDS", file=output_stream)

        sys.exit()

    elements = list(map(int, input_stream.readline().rstrip("\n").split(',')))

    for j in range(1, n):

        for i in range(j):

            if elements[j] % elements[i] != 0:

                print("NOT FRIENDS", file=output_stream)

                sys.exit()

    print("FRIENDS", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1,2,9
""",
            "output": \
"""\
NOT FRIENDS
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

```

Sample 2:

3 → n=3.

elements [1,2,9].

j=1 (element 2):

i=0 →2%1=0 → ok.

j=2 (element9):

i=0 →9%1=0.

i=1 →9%2=1 → not 0 → print NOT FRIENDS and exit.

Which is correct.

Another test case: [2,4,6,8]

j=1 (4):

i=0 →4%2=0 → ok.

j=2 (6):

i=0 →6%2=0 → ok.

i=1 →6%4=2 → not 0 → exit. So output NOT FRIENDS.

Which is correct.

So the code works.

But for n=1000, the code may take time. Let's think about the worst case: a list where all elements are 1. Then, all pairs are friends. The code will check all 499,500 pairs, and for each, 1%1=0. So it will return FRIENDS.

In Python, how long does it take to loop 5e5 times?

Well, let's see. Each loop iteration is a modulo operation. In Python, even 1e6 operations take about 0.1 seconds. So 5e5 is manageable.

Another possible optimization is to break the inner loop as soon as a failure is found. But the code already exits immediately when a failure is found.

So this code should work within the time constraints.

Now, check for possible edge cases.

Edge case 1: n=1 → output FRIENDS. Correct.

Edge case 2: all elements are the same. Like [5,5,5]. All pairs are friends → output FRIENDS.

Edge case 3: list is [2,4,8,16, ..., up to 1000 elements]. All elements are multiples of previous ones. So code returns FRIENDS.

Edge case 4: list is [2,3, ...]. The first pair (2 and3) → not friends → code returns NOT FRIENDS.

So code works.

Now, code in Python:

But wait, in Python, the elements are read from the input line. The code reads the line, splits on commas, converts to integers. That's correct.

But what about leading zeros? The problem statement says that the numbers do not have any leading zeros, so we don't have to handle that.

So the code is correct.
</think>

```python
import sys

n = int(input())
if n == 1:
    print("FRIENDS")
    sys.exit()
elements = list(map(int, input().split(',')))
for j in range(1, n):
    for i in range(j):
        if elements[j] % elements[i] != 0:
            print("NOT FRIENDS")
            sys.exit()
print("FRIENDS")
```
