<think>
Okay, let's see. The problem is to rearrange the given string of letters into the maximum possible binary number. The digits are formed by the words "zero" (0) and "one" (1). Each occurrence of these words contributes a digit. So the task is to find how many 1s and 0s we can form from the letters, and then output the digits in such a way that the overall number is maximized. Since the maximum binary number has as many 1s as possible followed by 0s, we need to maximize the count of 1s first, then 0s.

But how do we calculate the maximum possible count of 1s and 0s given the letters?

First, let's note the letters required for each word:

- "one" uses one 'o', one 'n', and one 'e'.
- "zero" uses one 'z', one 'e', one 'r', and one 'o'.

So each 'one' consumes o, n, e. Each 'zero' consumes z, e, r, o.

We need to determine the maximum number of '1's possible, then the remaining letters can form '0's. But there's a dependency between the two because both use some common letters.

Let me think: the key is to find how many 'one's can be made, given the constraints of the letters, and then how many 'zero's can be made with the remaining letters. But how?

Alternatively, perhaps we can model this as variables: let x be the number of 'one's and y the number of 'zero's. Then the constraints are:

For 'o's: x + y ≤ count['o']
For 'n's: x ≤ count['n']
For 'e's: x + y ≤ count['e']
For 'z's: y ≤ count['z']
For 'r's: y ≤ count['r']

So the variables x and y must satisfy all these inequalities. The goal is to maximize x + y (since each contributes a digit) but with x being as large as possible because 1 is larger than 0. Wait, no. The digits are ordered as per the binary number. So the maximum number is all 1s followed by 0s. So the count of 1s should be as large as possible, then 0s. So even if the sum x + y is not maximized, but x is as large as possible, that's better.

Wait, the maximum binary number is the one that has the highest possible 1s first. For example, if you can have two 1s and one 0, that's 110 which is better than 101 or 011. So the problem reduces to finding the maximum possible x (number of 1s), then use the remaining letters to form as many 0s as possible (y). But how to model this?

So the approach is to maximize x first, then maximize y given the remaining letters.

So how do we compute the maximum x possible?

The constraints for x (number of 'one's) are:

x must be ≤ count['o'], count['n'], count['e'].

But also, after using x 'o's, x 'n's, x 'e's, the remaining letters must be able to form y 'zero's, which requires:

y must be ≤ count['z'], count['r'], and the remaining o's (count['o'] - x) must be >= y, and the remaining e's (count['e'] - x) must be >= y.

So the problem is to find the maximum x such that:

x ≤ min( count['n'], count['o'], count['e'] )

and for the remaining letters, there exists a y such that:

y ≤ count['z']

y ≤ count['r']

y ≤ (count['o'] - x) 

y ≤ (count['e'] - x)

y >= 0

But since after x is chosen, the maximum possible y is min( count['z'], count['r'], (count['o'] - x), (count['e'] - x) ), the total digits would be x + y. However, the key is to maximize x first. So even if increasing x reduces the total x + y, it's better because 1s are more significant than 0s.

Wait, yes. For example, if x can be 2, but that leaves y as 0, while x=1 and y=2 would give a sum of 3. But the binary number would be 110 which is 6, whereas 11 is 3. Wait no, the sum x + y is the number of digits. Wait, no. Each 'one' is a digit '1', each 'zero' is a digit '0'. So the binary number is a sequence of x '1's followed by y '0's. So the total digits is x + y, and the value is (2^{y} -1) * 2^y + ... but for the binary number's maximum, the order is to have all 1's first. So the maximum is achieved when x is as large as possible, even if that reduces the total number of digits. For example, x=1 and y=0 gives the number '1', which is larger than x=0 and y=3 (000, which is 0). So the priority is to maximize x first, then y.

Therefore, the problem reduces to:

Find the maximum possible x (number of 'one's) such that there exists a y (number of 'zero's) that can be formed with the remaining letters.

So how do we compute the maximum x?

Let's think of possible x values. The maximum possible x is the minimum of count['n'], count['o'], count['e'].

But even if x is at that maximum, we need to check if there are enough letters left to form some y (could be zero). Because even if y is zero, x can still be considered.

Wait, but y can be zero. So the maximum x is the minimum of count['n'], count['o'], count['e'], and also, after subtracting x from o and e, the remaining o and e must be >= y, but since y can be zero, then any x that is <= min(n, o, e) is acceptable, and y will be zero if there's no z or r.

Wait, but the problem states that it is guaranteed that the letters can form a sequence of words. So the input is such that there exists at least one x and y such that the constraints are satisfied. So for our problem, we can ignore that, but the code must find x and y such that the letters are properly allocated.

But to maximize the binary number, we need to make as many '1's as possible, then '0's.

So the approach is:

1. Compute the counts of each character: z, e, r, o, n.

2. The maximum possible x (number of 'one's) is the minimum of n, o, e, but also, after choosing x, we need to make sure that the remaining letters can form some number of 'zero's. But since the problem says it's guaranteed that the letters can form a valid sequence, perhaps we can just compute x as the maximum possible, and then compute y accordingly.

Wait, but what if x is maximum possible (min(n, o, e)), but then there's not enough z or r to form even zero 'zero's? But in that case, y would be zero, and that's allowed because the problem says that the input is valid. So for example, if x is set to min(n, o, e), then the remaining letters may not form any 'zero's, but that's acceptable. So the code can proceed as:

x_max = min(count['n'], count['o'], count['e'])

But then, to get the maximum possible x, we can set x to x_max, and then compute y as min( count['z'], count['r'], (count['o'] - x), (count['e'] - x) )

But wait, if we set x to x_max, then maybe (count['o'] -x) could be negative. But since x is the minimum of o, n, e, then if x is o, then o - x is zero, so (count['o'] -x) is zero. So the remaining o is zero, so y can't be more than zero. So in that case, y is zero.

But this may not be correct. For example, suppose count['o'] is 5, count['n'] is 3, count['e'] is 4. Then x_max is 3. Then after x=3, the o's left are 5-3=2, e's left are 4-3=1. Then y can be up to min(z, r, 2, 1). So if z and r are say 3 and 4, then y is 1.

But in this case, x is 3 (max possible), and y is 1, leading to 3+1=4 digits. Alternatively, if we take x=2, maybe y can be higher, but the binary number would be 1100... which is worse than 1110...

So the correct approach is to maximize x first, regardless of how y is affected.

So the steps are:

Calculate the maximum possible x (number of 'one's) as the minimum of count['n'], count['o'], count['e'].

Once x is determined, calculate the maximum possible y (number of 'zero's) as the minimum of:

count['z'], count['r'], (count['o'] - x), (count['e'] -x).

Once we have x and y, the output is '1 ' repeated x times, followed by '0 ' repeated y times, then strip the trailing space.

But wait, the problem says that the original arrangement is possible. So when we compute x_max, but then after that, the y can be zero. So even if there are z and r left, but not enough o or e, it's okay. For example, if x is set to min(n, o, e), but after that, the remaining o is zero, then even if z and r are present, y can't be more than zero.

But how to compute x correctly.

So let's code this:

count the letters.

x_max_possible = min( count['n'], count['o'], count['e'] )

But wait, the letters for 'one' are o, n, e. So x can't be more than the minimum of these three.

Then, after choosing x_max, the remaining o is count_o -x, e is count_e -x.

y_max_possible = min( count['z'], count['r'], (count_o -x), (count_e -x) )

So y can be at most that.

But the problem says that the input is valid, so for x_max, perhaps even if y is zero, that's acceptable.

Thus, the correct approach is to maximize x first, then y.

Therefore, the algorithm is:

- Count the occurrences of each character.

- x is the minimum of n, o, e.

- y is the minimum of z, r, (o -x), (e -x).

Then, output '1 ' x times followed by '0 ' y times, joined and stripped.

Wait, but in some cases, choosing a lower x could allow for a higher x + y. For example:

Suppose count['n'] = 1, count['o'] = 3, count['e'] = 3.

count['z'] = 1, count['r'] = 1.

Then x_max is 1. Then y is min(1, 1, 3-1=2, 3-1=2) → 1. So total digits 2 → 1 1 0. Wait, no, x is 1 (so one '1'), y is 1 (one '0'), total digits 2 → '1 0' ?

But wait, wait: for x=1, the 'one's take 1 o, 1 n, 1 e. Then remaining o is 3-1=2, e is 3-1=2. For y (zero's), each requires z, e, r, o. So each zero takes 1 z, 1 r, 1 o, 1 e. So in this case, z=1, r=1. So y can be min(1,1, 2, 2) → 1. So yes, x=1, y=1 → total digits 2. But what if we choose x=0. Then y would be min(1,1, 3,3) → 1. So digits 0 → 1, which is worse. So in this case, maximizing x first is better.

Another example:

Suppose count['n'] = 2, count['o'] = 3, count['e'] =3.

count['z'] =2, count['r']=2.

x_max is min(2,3,3) → 2.

Then y is min(2,2, (3-2)=1, (3-2)=1) →1. So x=2, y=1 → digits 2+1=3: '1 1 0'.

If x=1, then o left is 3-1=2, e left 3-1=2. Then y would be min(2,2,2,2) →2. So digits 1+2=3: '1 0 0'. Which is worse than 110.

So even though the sum is same, the binary number is better with higher x.

Thus, the correct approach is to set x as the maximum possible (minimum of n, o, e), then compute y as the maximum possible given that x.

Thus, the code steps are:

1. Read n and the string.

2. Count the occurrences of each character (z, e, r, o, n).

3. x = min(count['n'], count['o'], count['e']).

4. remaining_o = count['o'] -x.

remaining_e = count['e'] -x.

y = min( count['z'], count['r'], remaining_o, remaining_e )

5. Output '1 ' *x + '0 ' *y, then strip the trailing space.

But wait, after x is chosen, the remaining o and e are used for the zeros. Each zero requires o and e as well. So y can't exceed the minimum of remaining_o and remaining_e.

Yes.

So the code can be written as:

count = {'z':0, 'e':0, 'r':0, 'o':0, 'n':0}

for c in s:

    count[c] +=1

x = min(count['n'], count['o'], count['e'])

remaining_o = count['o'] - x

remaining_e = count['e'] -x

y = min( count['z'], count['r'], remaining_o, remaining_e )

digits = ['1']*x + ['0']*y

print(' '.join(digits))

But let's test this against the examples.

First example:

Input:

4

ezor → letters are e, z, o, r. So counts:

z:1, e:1, r:1, o:1, n:0.

x is min(n=0, o=1, e=1) →0. So x=0.

remaining_o=1-0=1, remaining_e=1-0=1.

y is min(z=1, r=1, 1, 1) →1. So y=1. So digits are ['0']*1 →0. Which matches the first example's output.

Yes.

Second example:

Input:

10

nznooeeoer → Let's count:

Looking at the string: n, z, n, o, o, e, e, o, e, r.

So:

n: 2, z:1, e:3, o:3, r:1.

count['n']=2, count['o']=3, count['e']=3 →x = min(2,3,3) →2.

remaining_o=3-2=1, remaining_e=3-2=1.

y is min(z=1, r=1, remaining_o=1, remaining_e=1) →1.

So digits are ['1', '1', '0'] →1 1 0, which matches the second example.

Yes.

Another test case: suppose the letters can form two ones and two zeros. For example:

count['n']=2, count['o']=4, count['e']=4.

count['z']=2, count['r']=2.

x = min(2,4,4) →2. Then remaining o is 4-2=2, e is 4-2=2. y is min(2,2,2,2) →2. So digits are 1 1 0 0. Which is correct.

So this approach seems correct.

But wait, what if the counts for z and r are higher than the remaining o and e? For example:

count['n']=3, o=5, e=5 → x=3.

remaining o=2, e=2.

count z=5, r=5. So y is min(5,5, 2,2) →2. So y=2.

Thus, the code works.

Thus, the code is correct.

Now, to code this in Python.

Read n, then the string.

count the letters.

Compute x and y as described.

Then output the digits separated by spaces.

Now, considering the constraints: n can be up to 1e5, but the code will process the string in O(n) time, which is acceptable.

For counting the letters, using a dictionary is O(n), which is acceptable.

Thus, the code is efficient.

Now, code:

Read the input:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    s = input_stream.readline().rstrip("\n").strip()

    count = {'z':0, 'e':0, 'r':0, 'o':0, 'n':0}

    for c in s:

        count[c] +=1

    x = min(count['n'], count['o'], count['e'])

    remaining_o = count['o'] -x

    remaining_e = count['e'] -x

    y = min(count['z'], count['r'], remaining_o, remaining_e)

    digits = ['1']*x + ['0']*y

    print(' '.join(digits), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
nznooeeoer
""",
            "output": \
"""\
1 1 0
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

Second example:

n=10, s is nznooeeoer.

count:

n:2, z:1, o:3, e:3, r:1.

x=2. remaining o=1, e=1. y=1. Output 1 1 0.

Yes.

Another case where x is limited by n.

Another case where after x, remaining o and e are zero. For example, count['n']=5, o=5, e=5. x=5. remaining o=0, e=0. So y can't be more than 0.

But z and r may be present. But y is zero.

Thus, the code correctly outputs five 1s and no zeros.

Thus, the code should be correct.
</think>

```python
n = int(input())
s = input().strip()
count = {'z':0, 'e':0, 'r':0, 'o':0, 'n':0}
for c in s:
    count[c] += 1
x = min(count['n'], count['o'], count['e'])
remaining_o = count['o'] - x
remaining_e = count['e'] - x
y = min(count['z'], count['r'], remaining_o, remaining_e)
digits = ['1'] * x + ['0'] * y
print(' '.join(digits))
```
