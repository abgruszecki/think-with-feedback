<think>
Okay, let's tackle this problem. The task is to find the longest common prefix among all the given phone numbers. The output is the length of that prefix. Hmm, how do I approach this efficiently, especially given the constraints?

First, let's understand the problem. All the strings are of the same length and consist of digits. We need to find the maximum length of the prefix that's common to all of them. For example, if all start with "00", but differ at the third character, the answer is 2.

So the straightforward approach would be to compare each character position across all strings until a mismatch is found. The maximum prefix length is the number of positions where all characters are the same, starting from the first.

But how to implement this efficiently, especially when n can be up to 3e4 and each string can be up to 20 characters long?

Let's think. The naive approach would be for each position i (starting from 0), check all strings to see if their i-th character is the same as the first string's i-th character. If any string has a different character at position i, then the maximum prefix is i. Otherwise, proceed to i+1.

But checking all n strings for each position up to the minimum length could take O(n * m) time, where m is the length of the strings. Since m is up to 20 and n is up to 3e4, that's 3e4 * 20 = 6e5 operations, which is acceptable. Because even with Python's speed, that's manageable. So maybe the straightforward approach is efficient enough here.

So the steps would be:

1. Read all the strings.
2. Iterate over each character position (starting from 0 to len(s)-1).
3. For each position i, check if all strings have the same character as the first string's i-th character.
4. The first position where there's a mismatch, return i as the length. If all positions match, return the length of the string.

But wait, what's the time complexity here? Let's see. For each character position (up to 20), we compare all n strings. So O(mn) time, which for 20 * 3e4 = 6e5 operations. That's very manageable in Python even under tight time constraints.

So this approach should be acceptable.

Now, how to implement this.

First, read n. Then read n strings, store them in a list. Let's say the list is called numbers.

The length of each string is the same, so take the first string's length as m.

Initialize the answer as 0. For each i from 0 to m-1:

Check if all numbers[j][i] == numbers[0][i]. If yes, increment answer. If no, break the loop.

At the end, return the answer.

But wait, in Python, how to check all elements? For each i, we can iterate through all n strings and check their i-th character against the first string's i-th. But in Python, this can be done with a loop or using a generator expression with all().

Yes, for each i in range(len(numbers[0])):

current_char = numbers[0][i]

if all(s[i] == current_char for s in numbers):

   answer +=1

else:

   break

That's concise and efficient.

But in the worst case, for each i, it's O(n) checks. So overall O(mn) time. Which is acceptable.

Another optimization: we can stop as soon as we find a mismatch. So even for the first i where there's a discrepancy, we break and return the current answer.

This approach is correct and efficient enough.

Now, test the examples.

First example:

4

00209

00219

00999

00909

The first string is '00209'.

Check i=0: all have '0'? The first four strings' 0th character is '0'? Yes. So answer becomes 1.

i=1: all have '0'? Let's see: the first string's second character is '0'. The others: the second string's is '0', third is '9', fourth is '9'. Wait, wait, the third and fourth strings here are 00999 and 00909. Wait, their first two characters are '0' and '0'? Wait, the first two characters of third string are '00', but the first string's first two are '00' as well. Wait, maybe the first example's input is:

Sample 1 input:

4

00209

00219

00999

00909

So the first two strings have '00', then the next two have '00' as well? Wait, but then why is the output 2?

Wait, let's look again. Wait, in the first sample input:

The four numbers are:

00209

00219

00999

00909

Wait, the first two numbers start with '002', and the next two start with '009'. So the first two characters (positions 0 and 1) are '00' for all, but position 2: first two have '2', next two have '9'. So the common prefix is '00', length 2. Which matches the sample output.

So the code would check position 0: all are '0', answer increments to 1.

Position 1: all are '0', answer increments to 2.

Position 2: check the third and fourth strings. The first string's position 2 is '2', the third string's is '9'. So all(s[2] == '2') would be false. So break. The answer is 2.

Which is correct.

Another sample: input is 2 numbers, "1" and "2". So the first position (0) is different. So answer 0.

Third sample: three numbers with a common prefix of length 12. So code would check each position up to 11 (assuming 0-based) and all match, then position 12 would differ. So answer is 12.

So the code works.

Now, considering the input size. For n=3e4 and m=20, this code would take 3e4 * 20 = 6e5 operations, which is acceptable.

But in Python, loops are a bit slower. So using the all() function here is efficient because it's optimized in C.

Another approach: precompute the minimum possible prefix. For each position i, check the first string's i-th character against all others. But even that is O(n) per i.

Alternatively, for each i, take the i-th character of the first string, then check if all other strings have that same character. If any does not, break.

Yes, which is exactly what the code does.

So the code seems correct.

Now, edge cases:

- All strings are the same? No, the problem says all strings are different. So that's impossible. So the maximum possible prefix is when all but one have a certain prefix, but since the problem says that all are different, but even if two have same prefix and others vary, but the code checks all of them.

Wait, the code checks all strings. So for example, if n=3, and two have a prefix, but the third is different, then the code will stop at the first position where they differ.

So code is correct.

Another edge case: n=2, and the two strings are "0" and "1". Answer is 0.

Another case: all strings start with the same m characters. Then answer is m.

But since all strings are different, the maximum possible is m-1 if all characters are same except the last, but that's possible. For example, if two strings of length 2: "11" and "12". The common prefix is 1 (length 1).

So the code handles that.

Now, the code:

Read n.

Read n lines, stripping any whitespace (but input is correct as per problem statement). So in Python, using input().strip().

But the problem says that the strings are given in the input as per the lines, so maybe just read them as:

numbers = [input().strip() for _ in range(n)]

Then, if n is zero (but n is at least 2 per constraints), so no problem.

Then, if there's only one string, but n is at least 2. So code is okay.

Then, for each i in 0 to len(numbers[0])-1:

current_char = numbers[0][i]

if all(s[i] == current_char for s in numbers):

   ans +=1

else:

   break

But for n=3e4, each i-th iteration checks 3e4 elements. But the all() function in Python is optimized and will exit early as soon as it finds a False. So for example, if in the first string, the first character differs from some other string's first character, then the loop will check until it finds that string. So in the worst case, for each i, it checks all n elements. But in the best case, it checks one.

But in the worst case, for all m characters, all strings have the same prefix, but since the problem states that all strings are different, they must differ at some position. So for example, if all strings are same except the last character. Then, for m=20, the code will check all n strings for each of the first 19 positions, then on the 20th (index 19) it will find a mismatch. But that's O(mn) time.

But in practice, for m=20, that's 3e4 *20 = 6e5 operations. Which is acceptable.

So the code should work.

Now, let's write the code.

Read n.

Read the first string to get the length (since all have the same length).

Then, for each i from 0 to len(s)-1:

Check if all s[i] == first string's i-th character.

If yes, increment ans.

Else, break.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    numbers = [input_stream.readline().rstrip("\n").strip() for _ in range(n)]

    if n == 0:
        print(0, file=output_stream)
        return

    m = len(numbers[0])
    ans = 0

    for i in range(m):
        current_char = numbers[0][i]
        for s in numbers[1:]:
            if s[i] != current_char:
                print(ans, file=output_stream)
                return
        ans +=1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
1
2
""",
            "output": \
"""\
0
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

Wait sample input 1:

The numbers are:

00209

00219

00999

00909

So numbers[0] is "00209"

numbers[1] is "00219"

numbers[2] is "00999"

numbers[3] is "00909"

At i=0, all s[i] are '0', so ans increments to 1.

i=1: check s[1] for all others. For numbers[1], s[1] is '0', numbers[2] s[1] is '0', numbers[3] s[1] is '0'. So ans increments to 2.

i=2: check numbers[1] s[2] is '2'; numbers[2] s[2] is '9'. So mismatch. So print ans 2. Correct.

Yes.

So code works.

Another sample where answer is 0.

n=2, "1" and "2". i=0: check numbers[1][0] is '2' vs current_char '1'. So print 0.

Yes.

Third sample: 3 numbers. All have the first 12 characters same. So code loops i from 0 to 11. For each, check all s[i] == current_char, which they are. ans becomes 12. Then i=12, check the other strings. Suppose they differ. So return 12.

So code works.

Thus, this approach is correct and efficient.

Now, code in Python:

Read n, read the numbers, then loop over each character position, compare all others.

Now, in Python, input().strip() is used to read each line, but since the problem says the input is correct, perhaps just input() is enough, but stripping any leading/trailing whitespace (though the problem says that the phone numbers consist of digits only and have the same length). So using .strip() is safe.

But according to the problem statement, the input strings are the phone numbers and are given as per the lines. So for example, if a line has leading or trailing spaces, but according to the problem statement, the strings consist only of digits and have the same length. So perhaps the input lines have no whitespace, so the .strip() is redundant but safe.

So the code:

n = int(input())
numbers = [input().strip() for _ in range(n)]
if n == 0:
    print(0)
    exit()
m = len(numbers[0])
ans = 0
for i in range(m):
    current_char = numbers[0][i]
    for s in numbers[1:]:
        if s[i] != current_char:
            print(ans)
            exit()
    ans += 1
print(ans)

This should handle all cases correctly and efficiently.

But in Python, for very large n, numbers[1:] creates a new list each time. So for n=3e4, numbers[1:] is a slice of 29999 elements each time. But in Python, list slicing is O(k) time where k is the length of the slice. Wait, no. Wait, list slicing in Python creates a new list, which is a copy. So for numbers[1:], which is O(n) time and space. But doing this for each iteration of i (up to 20 times) would be O(n) per slice. But wait, in the code, numbers is a list, and numbers[1:] is generated for each i. For each i, the code loops through numbers[1:], which creates a new list each time. For n=3e4, this is 3e4 elements copied each time. For 20 times, that's 6e5 elements copied. Which is 6e5 elements, each being a string reference. So in Python, copying list slices is O(k) time where k is the slice length. So for each i, slicing numbers[1:] takes O(n) time, which for n=3e4 and 20 iterations is O(6e5) time. Which is manageable. But perhaps there's a way to avoid this.

An alternative is to precompute the list of all other numbers once. For example, others = numbers[1:]. Then, for each i, iterate through others. But this would require the same amount of memory, but the slice is created once. Wait, but the code loops for each i. So the code as written creates a new slice for each i. Hmm.

Wait, in the code, for each i, the code loops through numbers[1:], which creates a new list each time. So for 20 iterations, this is O(20 * n) time. For n=3e4, 20 * 3e4 = 6e5 operations. Which may be acceptable. But perhaps using a pre-sliced list would be more efficient.

But in practice, numbers is a list of strings. The slice numbers[1:] is a list of the same strings, so the slice operation is O(k) where k is len(numbers[1:]), but in Python, list slices are created by copying references. So the slice is O(k) time. But for 3e4 elements, this is manageable. But for 3e4 elements per i, and 20 i's, that's 6e5 elements copied. Which could take some time. So perhaps it's better to pre-slice once.

Alternatively, we can loop through numbers starting from index 1 each time. For example, for each i:

for j in range(1, n):

    if numbers[j][i] != current_char:

        print(ans)

        exit()

This way, there's no slicing. We loop from j=1 to n-1. This is O(n) time per i, but without creating a slice each time. So this would be more efficient.

Yes, that's better. Because numbers[1:] creates a new list each time, but looping through the indices 1 to n-1 is O(1) for each i. So let's adjust the code.

So revised code:

n = int(input())
numbers = [input().strip() for _ in range(n)]
if n < 2:
    print(0)
    exit()
m = len(numbers[0])
ans = 0

for i in range(m):
    current_char = numbers[0][i]
    for j in range(1, n):
        if numbers[j][i] != current_char:
            print(ans)
            exit()
    ans +=1

print(ans)

Yes. Now, for each i, instead of creating a new list slice, we loop through the indices from 1 to n-1. This is more efficient because it avoids creating a new list each time. For n=3e4, this saves 3e4 list elements being created each time. So the code is now O(m*n) time and O(n) space (storing all the numbers), which is optimal.

Thus, this code should be more efficient in terms of time and memory.

Testing the code with the same examples.

For the third sample, where all three numbers have a common prefix of 12 characters, the code loops i from 0 to 11. For each i, check j from 1 to 2. For each j, compare the i-th character. If all match, increment ans.

Yes.

So the code is correct.

So this code should be optimal.
</think>

```python
n = int(input())
numbers = [input().strip() for _ in range(n)]
if n < 2:
    print(0)
    exit()
m = len(numbers[0])
ans = 0

for i in range(m):
    current_char = numbers[0][i]
    for j in range(1, n):
        if numbers[j][i] != current_char:
            print(ans)
            exit()
    ans += 1

print(ans)
```
