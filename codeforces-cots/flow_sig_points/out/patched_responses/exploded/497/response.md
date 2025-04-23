<think>
Okay, let's see. I need to solve this problem where two variables a and b are modified according to certain steps until certain conditions are met. The goal is to find their final values after the process ends.

First, let me understand the process step by step. The steps are:

1. If either a or b is zero, stop.
2. If a is at least twice b, subtract 2*b from a and repeat.
3. Else if b is at least twice a, subtract 2*a from b and repeat.
4. Else, stop.

So the operations are: in each step, whichever of a or b is at least twice the other will get reduced by 2*the other. But this needs to be done until neither can be reduced anymore, except when one becomes zero.

But how can I model this efficiently, especially given the constraints where a and b can be up to 1e18? If I try to simulate each step step by step, that would be way too slow for large values. For example, if a is 1e18 and b is 1, then each step subtracts 2 from a, which would take 5e17 steps. That's impossible to handle in a loop.

So I need a smarter approach, perhaps mathematical, that can compute the result in logarithmic time.

Let me think about the operations. Each time, the larger number is reduced by a multiple of the smaller. This reminds me of the Euclidean algorithm for finding GCD, which uses modulo operations to skip steps. But the condition here is different. Instead of subtracting the smaller number, we subtract twice the smaller number if possible.

Wait, let's take an example. Suppose a is 12 and b is 5. Then:

Step 1: a >= 2*b (12 >= 10). So a becomes 12-2*5=2. Now a=2, b=5.

Check again. Now, since b (5) is >= 2*a (4), step 3 applies. So subtract 2*2=4 from b. Now b becomes 5-4=1. Now a=2, b=1.

Check again. Now a is 2 >= 2*1? Yes. So subtract 2*1=2 from a. Now a=0, b=1. Process ends.

So the steps are: subtract as many 2*b as possible from a, then subtract as many 2*a from b, and so on, alternating. But this can take a lot of steps if the numbers are big.

So the key is to find how many times each step can be applied in a single iteration, instead of doing it one by one.

For example, when a >= 2*b, how many times can we subtract 2*b from a? Let's see. Let's say a is initially A, and b is B. Then the maximum k times we can subtract 2*B from A such that A - k*(2B) >= 2B. Wait, no. Wait, each step requires that a >= 2b. So after subtracting 2b once, the new a is a - 2b. But the next subtraction can only happen if the new a is >= 2b again. Wait, no. Because after the first subtraction, a becomes a-2b. Then, in the next step, we check if a (now a-2b) is >= 2b again. So the number of times we can do this is floor((a) / (2b)), but wait, maybe not exactly. Let's see.

Wait, let's say a is 7 and b is 2. Then a >= 2b (7 >=4). Subtract 4, a becomes 3. Now a=3, which is not >= 2b (3 >=4 is false). So we can only subtract once. So the number of steps here is 1, which is (7) // (2*2) = 1 (7//4=1). So that works.

Another example: a=12, b=5. 12//10 = 1 (since 2*5=10). So subtract once, a becomes 2. So yes.

But what if a is 20, b=5. 2*5=10. 20//10=2. So subtract twice. But let's see:

First subtract 10: a=10. Check again, a >=10? Yes. Subtract 10: a=0. Then the process stops.

So the number of steps is 2, which is 20/(2*5) = 2. So yes, the quotient here gives exactly the number of times you can subtract 2b from a.

So when a >= 2b, the maximum k is a // (2b). But wait, if a is exactly divisible by 2b, then after k steps a becomes zero and we stop. Otherwise, a becomes a mod (2b), but since after subtracting k*2b, the remainder is a mod 2b. But wait, let me verify:

Take a = 24, b=5. 2b=10. 24//10=2. So subtract 20, a becomes 4. Then, since 4 < 10, process stops. So 24 mod 10 is 4. Which is correct.

So in this case, the number of steps is k = a // (2b), but only if a >= 2b.

So, the idea is: whenever a >= 2b, subtract 2b as many times as possible (k times, where k = a // (2b)), then set a = a - k*2b. Similarly for when b >=2a.

But the problem is that after each subtraction, the other variable might now satisfy the condition. So we need to loop through these steps, but in a way that each iteration processes as many steps as possible for the current condition.

This is similar to the Euclidean algorithm, where instead of subtracting the smaller from the larger step by step, we use division to find how many times we can subtract and then take the remainder. This reduces the number of steps from linear to logarithmic.

So the approach here is to loop until neither a >= 2b nor b >= 2a. Each time, we check which of the two conditions holds, compute the maximum possible steps (k) for that condition, subtract 2*b*k from a (or 2*a*k from b), and repeat.

Wait, but wait. Let's think. For example, if a >= 2b:

Compute how many times we can subtract 2b from a. Let's say k = a // (2b). Then a becomes a - 2b *k. But wait, maybe after this, a is still >= 2b? No, because k is the maximum possible. For example, a=25, b=5. 2b=10. 25//10=2. So 25-2*10=5. Now a is 5, which is less than 10. So no, the quotient gives exactly how many times you can subtract 2b from a before it becomes less than 2b.

So the algorithm would be:

While True:

   if a ==0 or b ==0: break

   if a >= 2*b:

      k = a // (2*b)

      a = a - k * 2*b

   elif b >= 2*a:

      k = b // (2*a)

      b = b - k * 2*a

   else:

      break

Wait, but after this, the new a and b could still be in a state where a >=2b or b >=2a again, so we need to loop again.

Wait no. Because when we compute k as a// (2b), the new a is a - 2b*k. Since k is the maximum possible, the new a is a mod 2b. So if a >=2b, then a mod 2b is in [0, 2b). So after subtracting, the new a is less than 2b. But that's not necessarily the same as being less than 2b. Wait, for example, a=3b. Then 2b is 2b. So 3b mod 2b is b. Which is less than 2b. So the new a is b, which is less than 2b (since b is positive). So in that case, after the subtraction, a is equal to b. Then, since neither a >=2b nor b >=2a (since they are equal), the loop breaks.

So in this approach, each iteration (either a >=2b or b >=2a) reduces the problem to a smaller state. So the loop will run O(log(max(a,b))) times.

Wait, but how? Let's see.

Take a=1e18, b=1.

First iteration: a >=2b. So k = 1e18 // 2*1 = 5e17. So subtract 5e17*2*1=1e18, a becomes zero. Then the loop breaks. So only one step.

Another example: a=7, b=3.

First check: 7 >=6 (2*3). Yes. k=7//6 =1. a becomes 7-6=1. Now a=1, b=3.

Check if b >=2*a: 3 >=2*1=2. Yes. So k=3//2=1. b becomes 3-2*1=1. Now a=1, b=1. Neither condition holds. Break. So final a=1, b=1.

So each step reduces the numbers, but the number of steps is logarithmic.

Thus, this approach is efficient even for large a and b.

So the plan is:

- Use a loop where in each iteration, check if a or b is at least twice the other.

- Compute the maximum possible k (times) we can subtract and subtract accordingly.

- Repeat until neither condition is true.

But wait, in the first step of the problem statement, if a or b is zero, we end. So in the loop, we first check if a or b is zero. If yes, break.

But in our code, after each subtraction, one of them could become zero, which would stop the process.

So the code structure should be:

loop:

   if a ==0 or b ==0: break

   if a >= 2*b:

       subtract 2*b as much as possible (k = a//(2*b)), a -= 2*b*k

   elif b >= 2*a:

       subtract 2*a as much as possible (k = b//(2*a)), b -= 2*a*k

   else:

       break

This loop will exit once neither condition is met, or if one becomes zero.

This approach should handle even the largest inputs efficiently, since each iteration reduces the numbers significantly.

Now, let's test this approach against the examples.

First example:

Input 12 5.

Loop:

a=12, b=5. a >=2*b (12>=10). k=12//10=1. a becomes 12-10=2. Now a=2, b=5.

Check again. b >=2*a (5 >=4). Yes. k=5//4=1. b becomes 5-4=1. Now a=2, b=1.

Check again. a >=2*b (2>=2*1=2). Yes. k=2//2=1. a becomes 0. Now, since a is zero, loop breaks. Output is 0 1. Which matches the first sample.

Second example: 31 12.

Loop:

a=31, b=12. Check if a >=2*b: 31 >=24. Yes. k=31//24=1. a becomes 31-24=7. Now a=7, b=12.

Check if b >=2*a: 12 >=14? No. Check if a >=2*b: 7 >=24? No. So loop breaks. Output is 7 12. Which matches the sample.

Another test case: a=7, b=3.

Loop steps:

a=7, b=3. a >=2*3=6. k=7//6=1. a becomes 1. Now a=1, b=3.

Check if b >=2*a:3 >=2. yes. k=3//2=1. b becomes 1. Now a=1, b=1. Conditions not met. Output 1 1.

Another test case: a=5e18, b=1.

a is 5e18. 2*b=2. a >=2b. k=5e18 // 2 = 2.5e18. So a becomes 5e18 - 2*2.5e18 =5e18 -5e18=0. Process stops. Output is 0 1.

So code works.

Now, let's code this in Python. The variables a and b can be up to 1e18, but Python handles big integers fine.

But when performing division, we need to use integer division. Also, note that in each iteration, we have to check which condition holds.

So code steps:

Read n and m as integers (a and b).

Then, loop:

while True:

   if a ==0 or b ==0: break

   if a >= 2*b:

       k = a // (2*b)

       a -= 2*b*k

   elif b >= 2*a:

       k = b // (2*a)

       b -= 2*a*k

   else:

       break

Once loop ends, print a and b.

Yes, that's the code.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a, b = map(int, input_stream.readline().rstrip("\n").split())
    while True:
        if a == 0 or b == 0:
            break
        if a >= 2 * b:
            k = a // (2 * b)
            a -= 2 * b * k
        elif b >= 2 * a:
            k = b // (2 * a)
            b -= 2 * a * k
        else:
            break
    print(a, b, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
31 12
""",
            "output": \
"""\
7 12
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

Sample 2: 31 12.

a=31 >= 24: yes. k=1. a=7. Next iteration.

a=7, b=12. Neither condition. exit. Output 7 12.

Another test case: a=20, b=5. a >=10. k=20//10=2. a=20-2*10=0. loop breaks. Output 0 5.

Yes.

So the code works.

Now, the code in Python:

Read input as n and m.

Then, loop as described.

Now, code:

Read n and m:

a, b = map(int, input().split())

Then, loop:

while True:

    if a ==0 or b ==0:

        break

    if a >= 2 * b:

        k = a // (2 * b)

        a -= 2 * b * k

    elif b >= 2 * a:

        k = b // (2 * a)

        b -= 2 * a * k

    else:

        break

print(a, b)

Yes, that's the code.

This code should handle all cases efficiently, even for 1e18 numbers. Because in each step, the larger number is reduced by a factor of at least two each time. For example, if a is much larger than b, then after subtracting 2*b multiple times, a becomes a mod (2*b), which is less than 2*b, but since a was larger than 2*b, the new a is less than 2*b, but since b is smaller than a, after this step, the next step would check if b is larger than 2*a, which is not possible. Then the loop would break. So each step reduces the numbers by a factor of 2 or more, leading to O(log(max(a,b))) iterations, which is manageable even for 1e18.

Thus, the code is efficient and correct.
</think>

```python
a, b = map(int, input().split())
while True:
    if a == 0 or b == 0:
        break
    if a >= 2 * b:
        k = a // (2 * b)
        a -= 2 * b * k
    elif b >= 2 * a:
        k = b // (2 * a)
        b -= 2 * a * k
    else:
        break
print(a, b)
```
