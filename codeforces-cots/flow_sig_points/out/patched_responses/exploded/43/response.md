<think>
Okay, I need to solve this problem where I have to find the maximum possible number by replacing a contiguous subsegment of the original number with their mapped values using function f. And I can do this operation at most once. So, the key is to find the optimal subsegment to replace so that the resulting number is the largest possible.

Let me think about the approach. The problem requires that I process a large input (up to 2e5 digits) efficiently, so the solution must be O(n) time. Any O(n^2) approach would be too slow.

First, let's understand when replacing a digit is beneficial. For each digit x in the original number, if f(x) > x, then replacing it would make the number larger. Conversely, if f(x) < x, replacing it would be worse. If f(x) == x, replacing it doesn't change the value.

The optimal strategy is to find the leftmost position where f(x) > x, then replace a contiguous segment starting from there as far right as possible, but stopping when f(y) < y (because after that, replacing those digits would make the number smaller). Wait, but maybe even if some digits in the middle have f(y) == y, it's still worth replacing them since it doesn't hurt. Because the entire segment is replaced once. So once we start replacing, as long as the digits in the segment are either mapped to higher or equal, but we must make sure that starting the segment at the earliest possible position where f(x) > x, and extending the segment as far as possible where replacing them doesn't make the number worse.

Hmm. Let's think step by step.

The maximum possible number is achieved by finding the earliest position where replacing the digit with f(x) gives a higher value. Then, in that segment, we replace all digits starting from that position, and include as many consecutive digits as possible where either f(y) >= y. But once we hit a digit where f(y) < y, we shouldn't include it in the segment. Wait, but even if we include some digits where f(y) == y, that's okay. Because replacing them doesn't make it worse, but perhaps allows a longer segment that contributes to a higher overall number.

Wait, for example, if the original number is 1337, and the function f maps 3 to 5. So, the first digit is 1, which maps to 1. Then the next two 3's become 5. The 7 maps to 3. So replacing the middle two 3's gives 1557. So the segment chosen was from position 2 to 3. Because the first 3 is replaced to 5, which is higher. Then the next 3 is also higher. The 7 is replaced to 3, which is worse, so we stop before that.

So the approach is to:

1. Iterate through each digit in the original number, left to right.
2. Find the first position where f(digit) > digit. This is the starting point of our segment.
3. Then, continue replacing digits as long as f(digit) >= current digit. But once we hit a digit where f(digit) < current digit, we stop the segment before that.
4. Once the segment is replaced, the number is maximized.

But wait, maybe there are multiple positions where replacing gives a higher digit. For example, suppose after the initial segment, there's another digit where f(d) > d. But replacing the earliest possible gives a larger number because the leftmost change is more significant. Because changing a higher digit (like the thousands place) has a bigger impact than changing a lower digit (like the hundreds place).

So the optimal strategy is to find the earliest possible starting position where f(d) > d, then replace as far to the right as possible, but only include digits where f(d) >= d. But even if some digits in the segment have f(d) equal to d, we can include them. Because replacing them doesn't decrease the value, and allows the segment to extend further right, possibly including more digits where f(d) > d.

So the steps would be:

- For each digit in the original number, check if replacing it with f(d) gives a higher value. The first such position is the start of the segment.
- Once the start is found, continue replacing until the end of the digits, but stop when a digit y is found where f(y) < y. Because after that, replacing y would make it smaller, so the segment must end before y.
- All digits after the start and before the first such y (or till the end) are included in the segment, even if their f(d) is equal to d. Because including them can't decrease the number.

Wait, but what about digits after the start where f(d) is equal to d? For example, suppose the original number is 123. f(1) = 1, f(2) = 3, f(3)=3. Then the best segment would be replacing 2 and 3. The 3's mapped value is equal to itself, but including it in the segment would make the number 133, which is better than 133 (if we only replace 2). Wait, no, because if you replace 2 and 3, the 3 becomes 3. So the original was 123, replaced segment is 23 → 33. So new number is 133. If the function for 3 is 3, then yes.

So even if replacing a digit with f(d) equal to d, including it in the segment is allowed. Because it doesn't hurt. So during the replacement phase, once we start the segment, we can include all consecutive digits until we hit a digit where f(d) < d. Because once that happens, including that digit would make the number worse, so we must stop the segment before that.

So the algorithm should be:

Loop through each digit from left to right.

For each position i:

- if f(a[i]) > a[i], then this is the start of the segment. Then, we need to replace this digit and as many as possible following digits until we hit a digit where f(d) < d. All digits in between (even those with f(d) == d) are replaced. So the segment starts at i and ends at j, where j is the last position where f(a[j]) >= a[j], and after j+1, either it's the end or f(a[j+1]) < a[j+1].

Once this segment is chosen, the entire number after replacement is the maximum possible.

But how to find the start and end efficiently?

The steps would be:

1. Find the first position where f(a[i]) > a[i]. Let's call this start.

If there is no such position, then replacing any segment won't help. So output the original number.

Otherwise:

2. From start, find the longest possible contiguous segment where all digits after start (inclusive) are replaced. The segment includes all digits from start to end (inclusive), where end is the maximum index such that for all k in [start, end], f(a[k]) >= a[k]. But as soon as a digit k after start has f(a[k]) < a[k], the segment must end at k-1.

Wait, no. Because after the start, once we start replacing, we can include any digits as long as they are >=. So even if in the middle of the segment, some digits have f(d) equal to d, it's okay. But as soon as a digit comes where f(d) < d, the segment must stop at the previous digit.

So for example:

Original digits: 1 3 3 7.

f(3) =5, f(7)=3.

So the first digit where f(d) >d is the second position (3 becomes 5). Then, the next digit is 3 →5 (equal to itself, so >=). Then 7 →3 (which is less than 7). So the segment is from position 2 to 3 (assuming 0-based or 1-based? Need to be careful with indexing). Wait, in the example given, the output is 1557. So replacing the two 3's. The 7 is not replaced. So the segment is digits 2 and 3 (if the string is 1,3,3,7). So the start is at index 1 (assuming 0-based), and the end is at index 2.

So the algorithm would be:

- Find the first index i where f(a[i]) > a[i].

Once found, start replacing from i onwards until:

- For each j >= i, replace until the first j where f(a[j]) < a[j]. Then end is j-1.

But how to determine end?

Wait, the end is the maximum possible index where for all k in [i, end], f(a[k]) >= a[k]. So after i, we can keep replacing until we find a k where f(a[k]) < a[k], then end at k-1. If all digits after i are >=, then end is n-1.

So the steps are:

Once the start i is found, then:

Initialize end = i.

Then, iterate from i+1 to the end of the array. For each j:

if f(a[j]) >= a[j], continue (extend end to j).

else, break the loop.

So end is the last j where f(a[j]) >= a[j].

Once the start and end are determined, replace all digits from start to end.

But why not include digits after j where f(a[j]) >= a[j] again? Because the segment has to be contiguous. So once you hit a digit where f(a[j]) < a[j], you can't continue the segment beyond that, even if there are later digits that can be replaced. But since we are allowed to choose any contiguous segment once, the optimal choice is to start as early as possible (to affect higher digits) and extend as far as possible until the first occurrence where a digit's replacement is worse.

So the code steps:

First, precompute for each digit in the original number, whether f(d) > d, >=d, or <d.

Then, find the first index where f(d) > d. Let's call this i.

If there's no such index, then no replacement is done (or check if any segment where all digits are replaced with f(d) >=d gives a higher number. Wait, no. Because if all digits when replaced are less than or equal to original, then replacing any segment would not increase the number. So the best is to not replace anything. So output the original.

Else, when we have i:

Now, the start is i.

We need to find the maximum end j such that for all k in [i, j], f(a[k]) >= a[k]. And the first occurrence of a digit after i where f(a[k]) < a[k], then j is k-1.

So after i, we can iterate until the end of the array, but stop when we find a digit where f(a[k]) < a[k].

Once the start and end are determined, replace all digits from start to end with their f(d) values.

This would give the maximum possible number.

Now, let's test this logic against the examples.

First example:

Input digits: 1 3 3 7.

f(1) is 1, which is equal. So first i where f(d) > d is index 1 (second digit, 3 becomes 5). Then, from i=1, check next digits:

At index 2: 3 →5 (5>3, so >=3 → include. end becomes 2.

Next index 3: 7→3. 3 <7 → break. So end is 2.

So replace indices 1-2 (digits 3 and 3) to 5 and 5. Result is 1 5 5 7 →1557. Correct.

Second example:

Input 11111. f(1) =9. So first i is 0. Then, all digits can be replaced since f(1)=9>1, and all digits are 1. So replace all to 9. So output 99999. Correct.

Third example: 33. f(3)=1. Both digits are 3. f(3)=1 <3. So no i found. So no replacement. Output 33. Correct.

Another test case: what if there's a situation where after starting the segment, there are some digits with f(d) ==d, then a digit with f(d) <d, then digits with f(d) >d.

For example:

Original digits: 2 3 1 4.

f(2) →3 (so >2), f(3)→3 (==), f(1)→2 (>1), f(4)→5 (>4).

So the first i is 0 (digit 2 →3). Then, we check from 0 onwards:

digit 0: 2→3 (okay, >=).

digit 1:3→3 (==, include, end becomes 1.

digit 2:1 →2 (>=1, include. end becomes 2.

digit 3:4→5 (>=4, include. end becomes 3.

So the segment is 0-3. All digits are replaced. Result is 3,3,2,5 →3325. Which is the maximum possible.

But wait, what if the digits after the initial segment have higher possibilities. For example, in the same example, if the initial segment is replaced, but there's a later digit that when replaced gives a higher digit. But since the initial replacement starts at the earliest possible, it's better to start there.

So the algorithm is correct.

Now, how to implement this in code.

First, read n, the string a, and the list f.

Then, for each digit in a, compute f(d). But since the string is a sequence of characters, we need to map each to integer, then apply f.

But for processing, perhaps we can precompute a list of the original digits and their f values.

So, steps in code:

Read n.

Read a as a string.

Read f as a list of 9 integers. Note that f[0] is f(1), since the input is f(1), f(2), ..., f(9). So for a digit x (as integer), f[x-1] gives the mapped value.

So, for each character in a, convert to integer, then compute f_val = f[x-1].

Now, find the first index where f_val > x. Let's call this start.

If no such index exists, output the original string.

Else, find the end as the maximum index >= start where for all digits from start to end, f_val >= x.

Once start and end are found, replace all digits from start to end with their f_val.

Else, output the original.

So code steps:

Compute a list of the original digits (as integers), and a list of their f values.

Then, find the first index where f_val[i] > original[i].

If no such index, return the original string.

Else, set start = i.

Then, from start, go to the right, as long as f_val[j] >= original[j], extend end.

Once we hit a j where f_val[j] < original[j], break.

Set end to j-1, which could be up to n-1.

Then, construct the result as:

original[:start] + [f_val of start to end] + original[end+1:].

But since the original a is a string, perhaps building the result as a list of characters.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = input_stream.readline().rstrip("\n").strip()

    f = list(map(int, input_stream.readline().rstrip("\n").split()))  # f[0] is f(1), etc.

    original = list(a)

    f_val = [str(f[int(c)-1]) for c in original]  # list of characters

    start = -1

    for i in range(n):

        c = original[i]

        c_f = f_val[i]

        if c_f > c:

            start = i

            break

    if start == -1:

        # no possible replacement

        print(''.join(original), file=output_stream)

        return

    # find end

    end = start

    for j in range(start+1, n):

        c_j = original[j]

        c_f_j = f_val[j]

        if c_f_j < c_j:

            break

        end +=1

    # replace from start to end inclusive

    result = original[:]

    for i in range(start, end+1):

        result[i] = f_val[i]

    print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
11111
9 8 7 6 5 4 3 2 1
""",
            "output": \
"""\
99999
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = input_stream.readline().rstrip("\n").strip()

    f = list(map(int, input_stream.readline().rstrip("\n").split()))  # f[0] is f(1), etc.

    original = list(a)

    f_val = [str(f[int(c)-1]) for c in original]  # list of characters

    start = -1

    for i in range(n):

        c = original[i]

        c_f = f_val[i]

        if c_f > c:

            start = i

            break

    if start == -1:

        # no possible replacement

        print(''.join(original), file=output_stream)

        return

    # find end

    end = start

    for j in range(start+1, n):

        c_j = original[j]

        c_f_j = f_val[j]

        if c_f_j < c_j:

            break

        end +=1

    # replace from start to end inclusive

    result = original[:]

    for i in range(start, end+1):

        result[i] = f_val[i]

    print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
33
1 1 1 1 1 1 1 1 1
""",
            "output": \
"""\
33
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

Third example: input 33, f(3) is 1. So original digits are '3' and '3', f_val is 1 and 1. So comparing '1' > '3'? No. So start remains -1. So output original. Correct.

Another test case: if after the start, there is a digit where f(d) == d, then another where f(d) >d. For example:

Original digits: 2 3 1 4.

f(2) is 3, f(3) is 3, f(1) is 2, f(4) is5.

original: ['2', '3', '1', '4']

f_val: [3,3,2,5]

start is 0 (3>2). Then check j=1: 3 ==3 → include. j=2: 2>1 → include. j=3:5>4 → include. So end is 3. So all replaced. Result is 3325.

Which is the maximum possible.

So the code seems correct.

What about a case where after the start, there's a digit where f(d) ==d, then a digit where f(d) <d, then a digit where f(d) >d.

E.g., digits: 2 3 5 1 4.

f(2)=3, f(3)=3, f(5)=4, f(1)=2, f(4)=5.

So original digits: 2,3,5,1,4.

f_val:3,3,4,2,5.

So start is 0 (3>2). Then:

j=1:3==3 → include. j=2:4 <5 → break. So end is 1. So replace 0-1 to 3,3. The rest remains. So the number becomes 3 3 5 1 4 →33514. But what about the digits after 2? The digit 5 is replaced to4 (which is less than 5). So in this case, the code correctly stops at j=2 (index 2), and ends at j=1. So the segment is 0-1. The code replaces them. Then the 5 is left as is. But there's a later digit 1 →2 and 4→5, which could be replaced, but since they are after the initial segment, the code doesn't process them. But since the code chooses the earliest possible start, which gives a higher digit in the leftmost position, which is better than a later start. So even if there's a later segment that gives a higher value, the leftmost is better.

For example, in this case, replacing 0-1 gives 33514, but if there's a segment from 3-4 (digits 1 and4 →2 and5, which gives 25. So the number becomes 23525. But 33514 is larger.

So the code correctly chooses the earliest possible start.

Thus, the code is correct.

Now, for the code's efficiency:

All steps are O(n), which is acceptable for n=2e5.

Memory usage is O(n) for storing original and f_val lists, which is acceptable.

So the code should work.
</think>

```python
n = int(input())
a = list(input().strip())
f = list(map(int, input().split()))
f_val = [str(f[int(c)-1]) for c in a]
start = -1

for i in range(n):
    if f_val[i] > a[i]:
        start = i
        break

if start == -1:
    print(''.join(a))
    exit()

end = start
for j in range(start + 1, n):
    if f_val[j] < a[j]:
        break
    end = j

result = a[:]
for i in range(start, end + 1):
    result[i] = f_val[i]

print(''.join(result))
```
