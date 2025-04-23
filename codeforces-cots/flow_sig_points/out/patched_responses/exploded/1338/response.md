<think>
Okay, I need to find the maximum XOR sum when selecting up to k candies from n, each labeled 1 to n. Let's think about how to approach this.

First, the key observation here is that the maximum XOR depends on the highest possible bits. The maximum possible XOR sum would be when we can set as many high bits as possible. 

Let's consider the binary representation. The maximum XOR for numbers up to n can be found by determining the highest bit where there's a possibility of flipping. For example, if n is 4 (100 in binary), the highest bit is the third position (counting from 0). The maximum XOR would be 7 (111), which is higher than 4. But how?

Wait, when k is at least 2, maybe we can get the maximum possible XOR by creating a number that's all 1s in binary up to the highest bit of n. For instance, if n is 4 (100), the highest bit is at position 2 (since 4 is 100). Then the maximum possible XOR is 7 (111). But how to achieve that?

The idea is that if we can select two numbers such that their XOR has a higher bit than the highest bit in n. Wait, no. Let me think again. For example, in the first sample input where n=4 and k=3, the maximum XOR is 7. This is achieved by XORing 1, 2, 4. The XOR of 1^2=3, then 3^4=7. But how does this work?

Another example: when n=6 and k=6, the maximum is 7. So taking all six numbers, but their XOR is 7. So in that case, the XOR of all numbers from 1 to 6 is 7. So the sum is 7.

Hmm. So the pattern here might be that when k is 1, the maximum is n. But when k is greater than 1, the maximum possible is a number with all bits set up to the highest bit of (the next power of two minus one if possible). Wait, perhaps the maximum possible XOR when k >= 2 is the next power of two minus one that is higher than or equal to the highest bit in n. For example, in the first case, n=4 is 100. The next is 111 (7), which is 2^3 -1. So if we can get that, that's the maximum.

So the strategy could be: find the largest number m such that m is (2^b -1), where b is the number of bits in the highest possible position. If n is already of the form 2^b -1, then that's the maximum. Otherwise, we can check if we can get the next higher such number.

But how do we know when we can achieve that?

Wait, let's think. For example, when n is 4 (100). The maximum possible XOR is 7 (111). How can we get that? By choosing 1, 2, 4. Their XOR is 7. Similarly, when n is 5 (101), the maximum is 7. So the maximum possible seems to be 2^{b} -1 where b is the position of the highest set bit plus 1. For example, if the highest bit of n is at position m (like 4 is 100, m=2), then 2^{m+1} -1 is the maximum possible XOR when allowed to select multiple numbers.

So the steps could be:

1. Find the highest bit position (m) in n. So m is the floor of log2(n). Then the next possible maximum is 2^{m+1} -1. But how to check if we can form that number with up to k elements?

Wait, but if k >= 2, then perhaps we can form the maximum possible as 2^{m+1} -1, where m is the position of the highest set bit in n. For example, when n is 4 (100), the highest bit is at position 2, so m+1 is 3, 2^3-1=7. So if k >=2, the answer is 7.

But how does this hold in different cases?

Let's take n=3. The highest bit is 1 (since 3 is 11). Then m+1 is 2, 2^2-1=3. But for k=2, the maximum XOR would be 3. For example, selecting 1 and 2 gives 3, which is the same as 3. So that works.

Another example: n=5 (101). The highest bit is at position 2 (since 5 is 101). So m=2, m+1=3. 2^3-1=7. So if k >=2, can we get 7? Let's see. Numbers up to 5 are 1,2,3,4,5. Let's pick 3 (011), 4 (100). Their XOR is 111 (7). So yes. So for n=5 and k>=2, the maximum is 7.

So the pattern is that when k is at least 2, the maximum possible XOR is the next higher number which is all 1s in binary, i.e., 2^{m+1} -1, where m is the position of the highest set bit in n.

But wait, what if n is already 7 (111). Then m is 2, m+1 is 3. 2^3-1 is 7. So the maximum is 7. Which is correct.

So the formula seems to be: if the maximum XOR is (2^(b) -1), where b is the position of the highest set bit plus 1, but only if that number is present in the possible combinations. Wait, but how do we know that such a number can be achieved?

Wait, for example, in the case of n=4, the maximum is 7. How do we get that? By selecting 1,2,4. Their XOR is 7. So when you have numbers up to n, and n is not a 2^m-1 number, then by combining numbers from the previous power of two, you can get that maximum.

So the general approach is:

If k ==1: the maximum is n.

Else: The maximum possible XOR is the largest number with all bits set up to the highest bit position of (n) plus 1. For example, for n=5 (101), the highest bit is at position 2. So the maximum is 7 (111). This can be achieved if there are two numbers in the set that can combine to give those bits.

So the algorithm can be:

Find the highest power of two that is greater than n. Then subtract 1. That gives the maximum possible XOR when k >=2.

But how to compute this?

The steps would be:

1. If k is 1, return n.

2. Else, compute the maximum possible XOR which is (2^(m+1) -1), where m is the position of the highest set bit in n.

Wait, but how to find m? For example, for n=4 (100), the highest set bit is at position 2. So m+1 is 3, and 2^3-1=7. For n=5 (101), same m=2, so 7. For n=6 (110), same m=2. For n=7 (111), m is 2, but 2^(3)-1=7. So yes.

So the code can be written as:

Compute the next power of two after n. Let's say the next power is 2^b. Then the maximum XOR is (2^b -1).

Wait, but how?

Wait, the maximum possible XOR sum for a subset of numbers from 1 to n is the maximum possible value which is the next power of two minus one. For example, if n is 5 (101), the next power is 8, so 8-1=7. So this is the maximum.

So the approach is:

If k >= 2, then the maximum XOR is (next power of two after n) -1.

But how do I compute the next power of two after n?

Alternatively, find the highest bit position of n, add 1, then compute 2^ that minus 1.

For example, for n=4 (100), highest bit is 2, add 1: 3. 2^3-1=7.

Yes.

So the code for the maximum XOR when k >=2 is (1 << (highest_bit +1)) -1.

So the steps for the code:

Check if k is 1. If yes, return n.

Else, compute the maximum possible XOR as (the next power of two minus one), which is (1 << (highest_bit_position +1)) -1.

But how to compute the highest_bit_position of n?

In Python, we can use the bit_length() function. For example, n.bit_length() gives the number of bits required to represent n in binary, excluding the sign and leading zeros.

For example, 4 is 100, bit_length is 3. The highest bit position is 2 (since 2^2=4). So highest_bit_position is n.bit_length()-1.

So:

highest_bit_pos = n.bit_length() -1

max_xor = (1 << (highest_bit_pos +1 )) -1

But wait, let's test this.

For n=4:

bit_length is 3, highest_bit_pos=2. 1<<3 is 8, 8-1=7. Correct.

n=5: bit_length is 3, same steps. 7.

n=7: bit_length is 3, 8-1=7. Correct.

n=6: same as 7.

So yes.

But what if n is 1? For example, n=1, k=1: output is 1. If k=2, but n=1, then k is 1, but since n is 1, but k can't be 2. So in the code, for n=1 and k=1, it's 1.

So the code can be written as follows:

Read n and k.

If k ==1:

    output n

else:

    compute the maximum possible XOR as (1 << (n.bit_length())) -1

Wait, wait. Because n.bit_length() is the number of bits. So for example, n=4, bit_length is 3. (1 << (3)) -1 is 8-1=7. Which is correct.

Yes.

So the code becomes:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    if k ==1:

        print(n, file=output_stream)

    else:

        print( (1 << (n.bit_length())) -1 , file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 6
""",
            "output": \
"""\
7
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

Sample 2:

n=6, k=6. The code outputs (1<<3)-1=7. Which matches the sample.

Another test case: n=3, k=2. The code outputs (1<<2)-1=3. Which is correct. Because 3 is 11 in binary, and the maximum XOR when selecting two numbers. For example, 1 and 2 gives 3.

Another test case: n=1, k=1. Output is 1.

n=2, k=2. Output is 3.

Yes, 1 XOR 2 is 3.

Another case: n=5, k=2. The code outputs 7. Which is correct as 3 and 4 (3 is 011, 4 is 100) XOR gives 111.

So the code seems to handle all cases correctly.

But why does this approach work?

Because when you have at least two numbers, you can choose the two numbers that can create the highest possible XOR. For example, for any n that is not a power of two minus one, there exists two numbers in the range 1 to n whose XOR is the next higher 2^m -1. For instance, take the highest power of two in n (like 4 in the case of n=5). Then 4 and (4-1) can be XORed to get 7.

Wait, 4-1 is 3. 3 XOR 4 is 7. So yes.

So whenever we have two numbers that are consecutive (like 3 and 4), their XOR is 7, which is the maximum possible.

Thus, the approach holds.

So the code is correct.
</think>

```python
n, k = map(int, input().split())
print(n if k == 1 else (1 << n.bit_length()) - 1)
```
