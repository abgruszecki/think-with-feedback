<think>
Okay, let's try to figure out this problem. So, we need to find four positive integers a, b, c, d such that their sum is n, and the gcd of a and b equals the lcm of c and d. Hmm, interesting.

First, let's think about the constraints. The problem says that for any n >=4, there's always a solution. So we need to find a pattern or a way to construct such numbers regardless of n.

Let's start by considering the example cases. For n=4, all are 1. So 1+1+1+1=4, and gcd(1,1)=1, lcm(1,1)=1. That works.

In the second example, n=7, the output is 2 2 2 1. The sum is 2+2+2+1=7. The gcd of 2 and 2 is 2, and the lcm of 2 and 1 is 2. So that's good.

Another example is n=10, where a=3, b=5, c=1, d=1. Their sum is 10. gcd(3,5)=1, lcm(1,1)=1. That works.

Looking at these examples, it seems like sometimes the gcd(a,b) is set to 1, and the lcm(c,d) is also 1. For example, the fifth test case. So maybe a way is to split the problem into two parts: a and b contributing a certain gcd, and c and d contributing the same value as their lcm.

So perhaps the approach is to set a and b such that their gcd is some k, and c and d such that their lcm is k. Then, the sum a + b + c + d must equal n.

But how to choose k? Let's see. Let's think of k as 1 first. Because if k is 1, then the lcm of c and d must be 1. Which implies that c and d are both 1. Because the lcm of two numbers is 1 only if both are 1. So if we set c and d to 1 each, then their sum is 2. Then a + b would be n-2. And we need a and b to be such that their gcd is 1. So a and b must be coprime and sum to n-2. But how can we find two numbers that sum to (n-2) and are coprime? Well, for example, if n-2 is even, then we can split it into 1 and (n-3). Wait, 1 and (n-3) would sum to n-2, and their gcd is 1 if n-3 is not 1. Wait, no. Wait, 1 and any number are coprime. So if we choose a=1 and b=(n-2-1) = n-3, then their gcd is 1, which is what we need. But wait, n-3 must be at least 1. Since n >=4, n-3 is at least 1 when n is 4. So for n=4, 1+1+1+1: but here, a and b would be 1 and 1, sum 2, which is n-2=2. Then c and d are 1 each, sum 2. Total 4. That works. For n=5, a=1 and b= (5-2-1) = 2. So sum a +b is 3, sum c+d=2. Total 5. But 1+2+1+1 =5. Yes, and gcd(1,2)=1, lcm(1,1)=1. That works. So this seems like a possible approach. But what if n-2 is even? Like, let's take n=6. Then a +b =4. We can choose a=1 and b=3. Their sum is 4, gcd(1,3)=1. So c and d are 1 each, sum 2. Total 6. So output would be 1 3 1 1. That works. So this approach works for even and odd n-2.

But wait, the sum a + b must be n-2, which is allowed as long as a and b are positive. So a=1 and b = (n-3), but for n >=4, n-3 is at least 1, so that's okay.

So in this case, the four numbers would be 1, (n-3), 1, 1. Summing to 1 + (n-3) + 1 +1 =n-3 +3 =n. So yes. And the gcd(1, n-3) is 1. The lcm(1,1) is 1. So that's valid. So this approach would work for any n >=4. But wait, let's check for n=7. Then according to this approach, the numbers would be 1, 7-3=4, 1, 1. Sum 1+4+1+1=7. Gcd(1,4)=1, lcm(1,1)=1. Which satisfies the condition. But in the example given for n=7, the output is 2,2,2,1. Which gives a sum of 7. Here, the gcd(2,2) is 2 and the lcm(2,1) is 2. So why is that? Because the approach I suggested would give a different solution. So the problem allows any valid solution, so both are acceptable. So the approach I'm thinking of would work, but the example uses a different approach.

So why not always use this approach? Because in some cases, maybe the sum a + b would be 2 (like when n=4) and a=1, b=1. That works.

So this seems like a general solution. But let's see if there are any cases where this approach doesn't work. For example, when n-3 is 0. But n is at least 4, so n-3 is at least 1. So a and b would be 1 and (n-3), which are both >=1.

But wait, what if n is 5? Then a=1, b=2 (since 5-3=2). Sum 1+2+1+1=5. Correct. So yes.

So this approach would work for all n >=4. But wait, why isn't this approach used in the sample test case for n=7? Because the sample's approach uses a different way. But the problem allows any valid solution, so the approach is correct. So perhaps this is a viable solution.

So the idea is: set c=1 and d=1, so their lcm is 1. Then, set a and b to 1 and (n-3). Then the sum is 1+ (n-3) +1 +1 =n. The gcd(a,b) is gcd(1, n-3)=1, which equals the lcm(1,1)=1. So this works. So this approach would work for any n >=4.

But wait, the sample input for n=7 uses a different approach, but that's okay. The problem allows any solution.

So why would the sample for n=7 not use this approach? Because perhaps the problem expects us to output the numbers in a different way. But since the problem allows any valid solution, the approach of 1, n-3, 1, 1 would work for all test cases.

But let's test this approach against the sample inputs.

Sample input 4: output is 1 1 1 1. Which is exactly this approach: a=1, b=1, c=1, d=1. Sum 4.

Sample input 7: according to the approach, the output would be 1 4 1 1. Sum 1+4+1+1=7. Gcd(1,4)=1. lcm(1,1)=1. So that's correct. But the sample output is 2 2 2 1. So both are correct, and the problem allows either.

Similarly, for n=8, according to the approach, the output would be 1,5,1,1. Sum 8. Gcd(1,5)=1. But the sample output is 2 2 2 2. Which has gcd(2,2)=2 and lcm(2,2)=2. So that's a different solution, but also valid.

So the approach of a=1, b= (n-3), c=1, d=1 works for all n >=4. But why does the sample have different outputs? Because the problem allows multiple solutions. So this approach would work, but maybe it's possible to have a solution where the gcd and lcm are not 1. Which could be better in some cases.

Wait, but in the sample input for n=8, the output is four 2s. So sum is 8, and gcd(2,2)=2. The lcm(2,2) is 2. So that's a valid solution. So this approach would require that a and b's gcd is 2. Then, c and d's lcm is 2. So how can that be constructed?

In this case, a and b can be 2 and 2. Their sum is 4, and the remaining sum is 4. Then, c and d need to sum to 4 and their lcm is 2.

So possible c and d: 2 and 2. lcm is 2. So that works.

So for n=8, the sample uses a different approach. But our approach would also work. So the problem is to find any valid solution.

But why not use the approach of a=1, b= n-3, c=1, d=1 for all cases? Because it's straightforward and works for all n >=4.

So perhaps this is the optimal solution. Let's check for n=9. The sample output is 2 4 2 1. Sum is 9. The gcd(2,4) is 2. The lcm(2,1) is 2. So that works. According to our approach, the output would be 1, 6, 1, 1. Sum 9. Gcd(1,6)=1. So the solution exists, but the sample uses a different approach. However, the problem allows any valid solution.

So the approach of setting a=1, b= n-3, c=1, d=1 is a valid and simple solution for all n >=4.

So the code would be:

For each test case, output 1, (n-3), 1, 1.

Wait, but wait. Let's confirm that the sum is correct. a + b + c + d = 1 + (n-3) + 1 + 1 = (1 + (n-3)) + 2 = (n-2) + 2 =n. So yes. And the gcd(a, b) is gcd(1, n-3) =1, and the lcm(c, d) is lcm(1,1)=1. So this works.

So this approach is valid for all n >=4, and it's O(1) per test case, which is acceptable for t=1e4 and n up to 1e9.

Therefore, the optimal solution is to output 1, (n-3), 1, 1 for each test case.

But wait, in the sample input for n=7, the sum is 7. According to this approach, the numbers would be 1,4,1,1. Sum 7. But the sample uses 2,2,2,1. Which also works. So the approach is correct.

So this seems to be a valid solution and the code is very straightforward. Let's test this approach against the sample input.

Sample input 4: output 1,1,1,1. Correct.

Sample input 7: 1,4,1,1. Sum 7. Gcd(1,4)=1, lcm(1,1)=1. Correct.

Sample input 8:1,5,1,1. Sum 8. Correct.

Sample input 9:1,6,1,1. Sum 9. Correct.

Sample input 10:1,7,1,1. Sum 10. Correct.

But in the sample output for n=10, the answer is 3,5,1,1. Which also works, but according to our approach, 1,7,1,1 is another valid solution.

So why isn't this approach used in the sample outputs? Because there are multiple possible solutions. But the problem says any valid solution is acceptable.

Therefore, the code can be written as follows: for each test case, output 1, (n-3), 1, 1. This is O(1) per test case and handles all constraints.

Now, let's check for n=5. The code would output 1,2,1,1. Sum 5. Gcd(1,2)=1, lcm(1,1)=1. Correct.

Another test case: n=6. Output is 1,3,1,1. Sum 6. Correct.

So this approach works. Therefore, the code is straightforward.

So the code would be:

Read t test cases.

For each test case, read n.

Print 1, n-3, 1, 1.

Wait, but wait: the sum must be n, and all four numbers must be positive. So for example, when n=4, n-3 is 1. So 1+1+1+1=4. Correct.

But when n=5, n-3 is 2. So 1+2+1+1=5. Correct.

So all numbers are positive. So the approach is valid.

This solution is optimal because it requires O(1) computation per test case and handles all possible n >=4.

So the code is as simple as:

t = int(input())
for _ in range(t):
    n = int(input())
    print(1, n-3, 1, 1)

But wait, wait. Let's test this with a testable snippet.

```python
def main(input_stream, output_stream):
  t = int(input_stream.readline())
  for _ in range(t):
      n = int(input_stream.readline())
      print(1, n-3, 1, 1, file=output_stream)

import io

TEST_CASES = [{
    "input": """\
5
4
7
8
9
10\
""",
    "output": """\
1 1 1 1
2 2 2 1
2 2 2 2
2 4 2 1
3 5 1 1\
""",
}, ]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    main(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, \
        f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

print('Tests passed 😎')
```

RUN_SNIPPET
```text
```