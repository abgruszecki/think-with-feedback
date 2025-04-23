<think>
Okay, I need to solve this problem where I have to find out how many bits change when adding 1 to a binary number stored in a special way. Let's see.

The problem says that the bits are stored with the least significant bit (LSB) first. So the first character in the input string is the LSB, the next is the next bit, and so on. The last character is the most significant bit (MSB). When you add 1, you have to process the bits in the usual binary way, but considering their order.

So, for example, if the input is 1100 (n=4), the bits are ordered as follows: the first bit is the LSB (rightmost in the normal binary representation). Wait, no. Let me think again. The problem states that the first character is the first bit of the cell, which is the least significant. So the binary number is built as follows: the first bit is 2^0, the second is 2^1, ..., the nth bit is 2^(n-1). So the string '1100' would represent 0*2^3 + 1*2^2 + 1*2^1 + 0*2^0. Wait no, wait: each position i (starting from 0) in the string is the (i+1)th bit. Wait, no. Let's see the example:

In the first sample input, the string is '1100', n=4. So the bits are:

bit 1 (LSB) is '1' → 1 → 2^0 contribution.
bit 2 is '1' → 2^1.
bit 3 is '0' → 2^2.
bit 4 (MSB) is '0' → 2^3.

So the original number is 1*2^0 +1*2^1 +0*2^2 +0*2^3 = 1 + 2 =3. Adding 1 gives 4. But since the cell has 4 bits, the maximum is 2^4-1=15. Wait, no. Wait, the cell's maximum value is 2^4 -1, right? Because 4 bits can represent up to 15. But when adding 1, if the number overflows, the extra bits are discarded. So for example, adding 1 to 15 (all bits 1) would become 16, but since we have 4 bits, the result is 0. Which explains the second sample: input is 1111 (all bits set). Adding 1 gives 0000, so all 4 bits flip.

So the task is to compute the number of bits that change when you add 1 to the current value, considering the way the bits are stored.

So, the approach is to:

1. Convert the input string into the binary value it represents.
2. Add 1 to this value, modulo 2^n (since adding 1 can overflow beyond n bits, and we need to keep only the lower n bits).
3. Convert the new value back into the bit string representation (LSB first).
4. Compare the original and new bit strings, counting the number of differing bits.

But wait, for n=100, converting the binary string to a number may be possible in Python as it handles big integers, but for n=100, 2^100 is a big number, but Python can handle that. However, maybe there's a smarter way without converting the entire number. Let's think.

Alternatively, the process of adding 1 to a binary number is equivalent to flipping the first 0 from the right (LSB side), and flipping all the 1s before it. But since the bits are stored in the string with LSB first (index 0 of the string is the LSB), then the process is:

Start with the first bit (index 0). If it's 1, flip it and carry over. Then check the next bit (index 1), etc. This continues until we hit a 0, which we flip to 1, and stop. If all bits are 1, then all are flipped to 0 (overflow).

So the steps are:

- Find the position of the first 0 in the original bit string, starting from the left (LSB to MSB direction). All the bits before that (to the left) are 1s and will flip to 0. The first 0 will flip to 1. If there are no zeros (all 1s), then all bits flip.

So, the number of bits that change is equal to (the position of the first 0 +1) if there's a zero, otherwise n.

Because:

For example, in the first sample input: '1100' (indexes 0-3: 0:1, 1:1, 2:0, 3:0). Wait, the input string is '1100', so the first character is index 0: '1' (LSB), next index 1: '1', then index 2: '0', index 3: '0' (MSB). Wait, that's the original string. So when adding 1, the process is:

Check bits from left (LSB) to right (MSB):

- The first 0 is at position 2 (third bit in the string). Wait, no. Wait, the bits are 1,1,0,0. So adding 1 would start from the LSB (position 0):

Original bits: 1 (pos0), 1 (pos1), 0 (pos2), 0 (pos3).

Add 1: pos0 is 1, so it flips to 0, carry over. pos1 is 1, flips to 0, carry over. pos2 is 0, flips to 1, no carry. Stop. So the new bits are 0,0,1,0 → string '0010'. Comparing with original '1100', the differing bits are positions 0,1,2,3? Let's see:

Original: 1 1 0 0

New:     0 0 1 0

Comparing each position:

pos0: 1→0 → changed.

pos1: 1→0 → changed.

pos2:0→1 → changed.

pos3:0→0 → same.

So total of 3 changes. Which matches the sample.

So the logic is: find the first 0 in the original string (starting from index 0), and count all the bits up to and including that 0. If there is no 0 (all 1s), then all n bits change.

So the number of bits that change is (position of first 0 +1) if there's any 0, else n.

Wait, but in the first sample, the first 0 is at index 2. So 2+1=3, which is the answer.

In the second sample, all 1s. So answer is 4.

So this approach works.

So the steps for solving the problem are:

1. Iterate through the input string from left (index 0) to right (index n-1) to find the first occurrence of '0'. Let's call this index i.

2. If such a 0 exists, then the number of bits that change is (i+1). Because when you add 1, all the bits from 0 up to i will flip (those before i are 1s, flip to 0, the 0 at i flips to 1). So the total is (i+1) bits.

3. If there is no 0 (all 1s), then after adding 1, all bits flip to 0. So the number is n.

So the code can be written as follows:

Read the string, loop through each character until a '0' is found. If found, the answer is the index +1. If not, answer is n.

But wait, that seems much simpler than converting the entire number. So why not do that?

Yes, that's a much better approach. Because converting the entire number could be computationally heavy for n=100, but for n=100, it's manageable. However, even for n=1e5, the first approach would be O(n), which is acceptable. But the problem says n can be up to 100, so it's definitely manageable.

So the steps are:

- For each bit in the input string (starting from the left), check if it's '0'. The first occurrence of '0' in the string (from left to right) gives the index. The answer is index +1. If no zeros, answer is n.

This approach is O(n) time and O(1) space, which is optimal.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()
    for i in range(n):
        if s[i] == '0':
            print(i + 1, file=output_stream)
            return
    print(n, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1111
""",
            "output": \
"""\
4
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

Second sample input: '1111' → no zeros. Answer is 4. Correct.

Another test case: '0100' → the first '0' is at index 0. So answer is 0+1=1. Let's see. The original bits are 0 (LSB), 1, 0, 0. Adding 1 changes the LSB to 1. So new bits are 1,1,0,0. So only the first bit changes. So answer is 1. Correct.

Another test case: '0011' → first '0' is at index 0. So answer is 1. Adding 1 changes 0 to 1. So the new number is 1 followed by 0,1,1. So only the first bit changes.

Another case: '1000' → the first '0' is index 1. So answer is 2. Let's see. Original bits are 1,0,0,0 (MSB). Adding 1: the first bit is 1, becomes 0. Then carry over. Next bit is 0, becomes 1. So the new bits are 0,1,0,0. Comparing to original '1','0','0','0' → bits 0 and 1 have changed. So 2 bits. Correct.

Yes, this logic works.

So the code can be written as:

Read n, then the string. Iterate through the string, find the index of the first '0'. If found, answer is index+1, else n.

So the code is straightforward.

Now, code steps:

Read n: n = int(input())

Read the string: s = input().strip()

Loop through each character in s, from left to right (from index 0 to n-1):

for i in range(n):

    if s[i] == '0':

        print(i+1)

        exit()

print(n)

Yes. That's all. So for example, in the first sample, the loop checks index 0 (s[0] is '1'), then index 1 (s[1] is '1'), index 2 (s[2] is '0'). So returns 3. Correct.

In the second sample, all are 1's. So loop runs through all, none found. Then print 4.

This should handle all cases.

So the code is simple and efficient. O(n) time, no issues with n up to 100. So this is the optimal solution.
</think>

```python
n = int(input())
s = input().strip()
for i in range(n):
    if s[i] == '0':
        print(i + 1)
        exit()
print(n)
```
