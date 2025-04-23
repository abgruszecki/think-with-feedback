<think>
Okay, I need to solve this problem where I have to find the first occurrence of a digit c in the decimal expansion of a fraction a/b after the decimal point. The constraints are that a and b are positive integers with a < b, and c is between 0 and 9. The output is the position of the first occurrence of c, starting from 1. If it's not there, output -1.

First, I should think about how to find the decimal expansion. Since a/b is a fraction where a < b, the decimal part starts with 0. Then, when you divide, you perform the long division process. The key here is to track the remainder at each step because if a remainder repeats, the decimal starts to cycle, so we can detect a repeating pattern.

The problem is to find the first occurrence of the digit c in this expansion. So the plan is to simulate the division step by step, keep track of the remainders we've seen to detect cycles, and for each digit after the decimal point, check if it's equal to c. Once we find it, return the position. If we loop until we either find the digit or detect that the remainder becomes zero (which means the decimal terminates) and there's no c, then return -1.

But wait, how do we simulate the decimal digits? Let's see. Let's take the example where a=1, b=2. The first step is 1 divided by 2. The decimal starts as 0. Then, 1 *10 = 10. 10 divided by 2 is 5, remainder 0. So the first digit after decimal is 5, then the next digits are 0s. So in that case, for c=0, the first occurrence is at position 2.

So the approach is: perform the division steps, each time multiplying the remainder by 10, divide by b to get the next digit, and check if that digit is c. The position increments each step. But also, we need to track remainders to avoid infinite loops. Because if the same remainder occurs again, the digits will start repeating from there, so if we haven't found c by the time we see a repeated remainder, we can break and return -1.

So here's the algorithm step by step:

1. Initialize current_remainder as a % b. Wait, no. Wait, a < b, so when you divide a by b, the integer part is 0, and the remainder is a. So the initial remainder is a. Because a/b is 0.xxxx.

Wait, no. Let's think again. When you compute a divided by b (a < b), the integer part is 0, and the remainder is a. Then, to compute the decimal digits, you multiply the remainder by 10 and divide by b again. So the first step after the decimal is (a * 10) // b, which is the first digit. Then the new remainder is (a *10) % b. Then, multiply by 10 again, etc.

So for each step:

digit = (remainder * 10) // b

new_remainder = (remainder *10) % b

So the steps are:

Initialize remainder = a

But wait, wait. Let's take a=1, b=2. Remainder starts as 1. Multiply by 10: 10. Digit is 10//2=5, remainder 0. Next step: 0 *10 =0. Digit is 0, remainder 0. Then it repeats.

Wait, but after the remainder becomes 0, all subsequent digits are 0. So in this case, the digits after the decimal are 5, then 0, 0, etc.

So for each step, the process is:

remainder starts as a.

For each position starting from 1:

remainder = remainder *10

digit = remainder // b

remainder = remainder % b

Then check if the digit is c.

But wait, in code terms, maybe:

current_remainder = a

But wait, initial remainder is a. Then, multiply by 10, get digit, then remainder is the remainder after division by b.

Wait, in the first step, the first digit after the decimal is (a *10) // b, and the new remainder is (a*10) % b.

Wait, for a=1, b=2:

First step: 1 *10 =10 → 10 //2=5 (digit 5), remainder 0. So the first digit is 5 (position 1), next remainder is 0.

Second step: 0*10=0 → digit 0, remainder 0. So position 2 is 0.

So in the first example, c is 0, which is found at position 2.

So the algorithm should:

Loop for each possible digit position (starting from 1):

At each step:

Multiply the current remainder by 10.

digit = (current remainder *10) // b → no, wait: current_remainder is a. Then, multiply by 10 → current_remainder *10.

digit is (current_remainder *10) // b.

Then, new remainder is (current_remainder *10) % b.

Wait, no. Let's re-express:

current_remainder starts at a.

For each position:

digit = (current_remainder * 10) // b

new_remainder = (current_remainder * 10) % b

Then, current_remainder becomes new_remainder for the next step.

Yes. So for example, in the first step, current_remainder is a. Multiply by 10, divide by b, that's the first digit. Then the remainder is (a*10) mod b.

So the loop is:

current_remainder = a

position = 1

We need to track the remainders we've seen, because if a remainder repeats, the digits will start repeating. So once we see the same remainder again, the sequence is in a cycle, and if we haven't found c by then, we can break and return -1.

So the steps are:

- Initialize a dictionary to track remainders and their positions. Because each remainder corresponds to a specific position (the next digit's position). Wait, maybe not. Let's think.

For example, when we start with remainder a, that's before processing position 1. Then, after processing position 1, we have a new remainder.

Wait, the remainder after step 1 (position 1) is new_remainder. So each remainder is associated with the next position.

Wait, perhaps. Let's see:

Suppose current_remainder is r. Then, when processing position k:

digit is (r*10) //b, and the new remainder is (r*10) %b.

So the next position will be k+1, and the new remainder is (r*10) %b.

So the key is that the remainder after step k determines the next digit. So, if we ever see the same remainder again, the digits will start repeating from that point onwards.

Therefore, in order to detect cycles, we can track the remainders we have encountered. If during the loop, a remainder repeats, then we know that the digits will start repeating from the position where this remainder was first seen.

So, the algorithm steps:

1. Initialize current_remainder = a.

2. For each position from 1 to ...:

   a. current_remainder is multiplied by 10.

   b. digit = current_remainder // b

   c. remainder_after = current_remainder % b

   d. Check if digit is equal to c. If yes, return current position.

   e. Check if the current_remainder (after step a, before division?) Wait, no. Wait, the current_remainder in step a is multiplied by 10. So the remainder after step a is (previous_remainder *10). Then divided by b to get digit and remainder.

Wait, perhaps the steps should be:

current_remainder starts as a.

At each step:

current_remainder *=10 → this is the new value.

digit = current_remainder // b

new_remainder = current_remainder % b

So in code, it's:

digit = (current_remainder *10) // b → no. Wait, the code would be:

current_remainder = a

for position in 1, 2, ...:

   current_remainder *=10

   digit = current_remainder // b

   remainder = current_remainder % b

   if digit == c:

       return position

   current_remainder = remainder

   check if current_remainder is in seen_remainders → if yes, break and return -1

But this seems a bit different. Let's see with the first example:

a=1, b=2, c=0.

current_remainder is 1.

position 1:

current_remainder *=10 → 10.

digit = 10 //2 →5. Not 0. remainder is 0.

current_remainder becomes 0.

Check if 0 is in seen_remainders. Initially, seen_remainders is empty. So add 1 (the initial current_remainder before processing position 1?), wait no. Wait, perhaps the key is to track the current_remainder before processing each step. Because when you process a step, you multiply by 10, then compute digit and new remainder.

So the initial current_remainder is a. Then, for each position:

- multiply by 10.

- compute digit and new remainder.

So in the first iteration (position 1):

current_remainder is 1 (from initial step). Then multiply by 10 →10. So digit is 10//2=5, remainder 0. current_remainder is set to 0.

So the seen_remainders would track the current_remainder after each step. Wait, but how to track the remainders to detect cycles.

Wait, in the first step, after processing, the new remainder is 0. So in the next step, position 2:

current_remainder is 0. Multiply by 10 →0. digit is 0. So check if c is 0. If so, return position 2.

But in the first example, the digit is 0 here, which is position 2, so output is 2.

But how do the remainders affect cycle detection. Let's see:

The initial current_remainder is a (1). Then, after processing, the remainder becomes 0.

At position 2:

current_remainder is 0. Multiply by10 →0. digit 0, remainder 0. So the next remainder is 0 again.

So after processing position 2, the current_remainder is 0. So in the next step (position3), same thing: digit 0, remainder 0. So once the remainder is zero, all subsequent digits are zero.

Thus, once the remainder becomes zero, after that, the digits will be zero. So, in the problem, once we reach a remainder of zero, we can process all the digits until then, and if c is 0, then after the first zero digit (if any), we can have infinite zeros. So for example, if in any step the digit is c, return that position. Else, if the remainder is zero, then after that, all digits are zero. So, if c is zero and the remainder becomes zero, then the next digit is zero (since remainder zero will generate digit zero every time). So in that case, the first occurrence of c=0 would be the position after the remainder becomes zero.

Wait, this is a bit tricky. Let's think through:

Suppose the remainder after step k is zero. Then, step k+1:

current_remainder is zero. Multiply by 10 →0. digit is 0. So in step k+1, the digit is 0, and the remainder is zero. So all subsequent digits are zero.

So, if during processing, we have a digit which is zero and c is zero, we return the position. If we reach a remainder of zero and haven't found c yet, then after that step, all digits are zero. So if c is zero, the next position (k+1) will be the first occurrence. But if c is not zero, then we can return -1.

So, the algorithm needs to handle two cases:

1. The decimal terminates (i.e., after some steps, the remainder becomes zero). In this case, the digits after that are all zero. So:

   a. If during the steps before termination, we found c, return the position.

   b. Else, check if c is zero. If yes, return the position of the first zero after termination (which is the next position after the step where remainder became zero). But wait, let's see.

Wait, for example, when the remainder becomes zero after step k, then step k+1 will have digit zero. So in the case where the remainder becomes zero after step k, the digits after that are all zero. So the positions k+1, k+2, etc., are zeros. So if c is zero and we have a step where the remainder becomes zero (i.e., after step k, the remainder is zero), then the first occurrence of zero in position k+1.

So, in the code, after each step, when we compute the new_remainder (which is current_remainder *10 % b), if new_remainder is zero, then after this step (the next steps will generate zeros).

Wait, perhaps not. Let's take the example where a=1, b=2. The steps are:

Initial remainder: 1.

Position 1:

current_remainder =1*10=10 → digit 10//2=5. remainder is 10%2=0.

So after position 1, the remainder is zero.

So the next step (position 2):

current_remainder is zero. Multiply by10 →0. digit is 0. So position 2's digit is zero.

So in this case, if c is zero, the first occurrence is position 2.

So during processing, after step 1 (position 1), the remainder is zero. So in the next step (position 2), we process the remainder zero and get digit zero.

Thus, the code needs to process the steps until the remainder becomes zero, and then check if c is zero, and if so, the next position is the first zero.

Wait, but how to handle that in the code. Let's outline the steps:

We can have a loop where each iteration represents a digit position.

In each iteration:

1. Multiply current_remainder by 10.

2. Compute digit = (current_remainder) // b.

3. Check if digit is c. If yes, return current position.

4. Compute new_remainder = current_remainder % b.

5. Check if new_remainder is zero. If so, check if c is zero. If yes, then the next position (current position +1) will have a zero. So return current position +1. Else, return -1.

Wait, but how? Let's think.

After step 4, if new_remainder is zero, then all subsequent digits are zero. So:

If during the loop, we process a digit (position k) and then new_remainder is zero. Then, in the next step (position k+1), the remainder is zero. Multiply by10 → zero, digit is zero, etc.

So, after step k, if new_remainder is zero, then:

If the digit computed in step k+1 is zero (which it will be), then if c is zero, the first occurrence is at position k+1.

But how to check that in code.

Wait, for example:

In step k:

current_remainder is r. Then, multiply by 10 → r*10.

digit = (r*10) //b → d.

new_remainder = (r*10) %b → nr.

If nr is zero, then next step (k+1) will be:

current_remainder is nr (zero). multiply by10 →0.

digit is 0.

So, in this case, if after step k, the new_remainder is zero, then in step k+1, the digit is zero.

Thus, if during step k, after processing, the new_remainder is zero, then:

If c is zero, then the digit in position k+1 is zero. So if c is zero and we haven't found it in positions up to k, then return k+1.

But how to model this in code.

The algorithm can proceed as follows:

We loop for each position, up to a maximum of, say, 1e6 steps (but that's not feasible). So, better to track the remainders to detect cycles and avoid infinite loops.

But given the constraints (a and b up to 1e5), the maximum possible number of steps is b, because there are b possible remainders (from 0 to b-1). Once a remainder repeats, the digits cycle.

So, the steps:

Initialize a dictionary (remainder_map) that maps remainders to the position they were first seen.

current_remainder = a

positions start at 1.

We also need to track the current position.

But the steps:

At each step (position):

1. Multiply current_remainder by 10.

2. digit = current_remainder // b.

3. Check if digit is c. If yes, return current position.

4. Compute new_remainder = current_remainder % b.

5. Check if new_remainder is 0. If yes:

   a. Check if c is 0. If yes, return current position + 1 (since next digit is 0).

   b. Else, return -1.

6. Check if new_remainder is in remainder_map. If yes, there's a cycle and we can't find c, return -1.

7. Else, add new_remainder to remainder_map with the next position (current position +1).

8. Set current_remainder = new_remainder.

Wait, perhaps I'm getting confused here.

Wait, let's re-express the steps correctly.

Each step corresponds to a position. Let's structure the code as:

Initialize current_remainder = a

remainder_map = { current_remainder: 1 }

position =1

Wait, no. Because the first step is position 1. For example, in the first step, current_remainder is a. Then, multiply by 10 to get a*10, then digit is (a*10) //b.

But how to track the remainders. Let's think again.

Let's say we track the remainder before processing each step.

So:

current_remainder is the remainder from the previous step, which will be multiplied by 10 in the current step.

So, for example:

Initially, current_remainder is a.

Then, step 1:

digit is (a *10) //b

new_remainder = (a*10) %b

If new_remainder is zero:

   if c is zero, then next position (2) will have digit zero.

Else, after this step, no more digits (since remainder is zero, all digits after are zero).

Else:

   check if new_remainder is in remainder_map. If yes, return -1.

Else add to remainder_map.

So the code would need to track the new_remainder after each step.

But the remainder_map should track the remainders that can lead to cycles. Because if a remainder is encountered again, it means that the digits from that point on will repeat.

Thus, the steps in code would be:

current_remainder = a

remainder_map = {a: 1}

position =1

But in the first step:

digit is (current_remainder *10) //b → (a*10)//b

new_remainder = (current_remainder *10) %b → (a*10) %b

But in this case, current_remainder is a. So after the first step, new_remainder is (a*10) %b.

But the code must track the new_remainder as the next current_remainder.

Wait, perhaps the code should be structured as:

current_remainder = a

for each position starting from 1:

   current_remainder *=10

   digit = current_remainder //b

   new_remainder = current_remainder %b

   if digit == c:

       return position

   if new_remainder ==0:

       if c ==0:

           return position +1

       else:

           return -1

   if new_remainder in remainder_map:

       return -1

   remainder_map[new_remainder] = position +1

   current_remainder = new_remainder

But wait, in the first step:

current_remainder starts as a.

Multiply by 10 → a*10.

digit is (a*10) //b.

new_remainder is (a*10) %b.

Then, check if new_remainder is zero. If yes, check if c is zero.

But in this case, if new_remainder is zero, then the next step's current_remainder is zero. Then, when processing position+1 (position+1 is next position):

current_remainder is zero. Multiply by10 →0. digit is zero. So if c is zero, the next position (position+1) is where it's found.

But in the code above, after position=1, if new_remainder is zero and c is zero, we return position+1.

Which would be 2. Which is correct for the first example.

So, the code would:

current_remainder = a

for each position in 1, 2, ... up to some limit (until remainder repeats or zero):

   current_remainder *=10 → becomes current_remainder *10

   digit = current_remainder //b

   if digit ==c → return position

   new_remainder = current_remainder %b

   if new_remainder is 0:

       if c ==0 → return position +1

       else → return -1

   if new_remainder in seen → return -1 (cycle detected, but no c found)

   add new_remainder to seen with position+1

   current_remainder = new_remainder

But the key is that for each step, we have to track the remainder after the step, because that will be the starting point for the next step.

Wait, but in this code structure, the new_remainder is (current_remainder *10) %b. Because current_remainder is multiplied by 10 first.

But then, when we check if new_remainder is zero, that's the remainder after this step. So, if new_remainder is zero, then in the next step, current_remainder is zero. So when we multiply by 10, digit is zero, which is for position+1.

So, if new_remainder is zero, and c is zero, then the next digit (position+1) is zero → return position+1.

But in the code above, after checking if digit is c, we check if new_remainder is zero. If yes, and c is zero, return position+1.

Yes. That's correct.

So, in code:

We can proceed as follows:

Read a, b, c.

If c is 0 and a/b is 0.0 (but since a <b, it's 0.xxxx...). So, for example, if a=0, but the problem states that a is a positive integer, so a is at least 1.

So, proceed.

Initialize:

current_remainder = a

seen = {} → a dictionary to track remainders and their positions.

loop for position starting at 1:

   current_remainder *=10

   digit = current_remainder //b

   if digit ==c:

       return position

   new_remainder = current_remainder %b

   if new_remainder ==0:

       if c ==0:

           return position +1

       else:

           return -1

   if new_remainder in seen:

       return -1

   seen[new_remainder] = position +1

   current_remainder = new_remainder

So, the code loops for each position. For each position:

- Multiply current_remainder by 10.

- Compute digit and new_remainder.

- Check if digit is c. If yes, return position.

- Check if new_remainder is zero. If yes, then:

   if c is zero, next digit is zero → return position+1.

   else, there are no more digits (all zeros) → return -1.

- Else, check if new_remainder has been seen before (i.e., in 'seen' dictionary). If yes, then a cycle is detected, and we can't find c → return -1.

- Else, add new_remainder to 'seen' with the next position (position+1), and set current_remainder to new_remainder for the next iteration.

This approach ensures that each step is processed, and cycles are detected.

But what about the case where the remainder is zero after some steps, but c is zero?

For example, in the first example, after position 1, the new_remainder is zero. Then, check if c is zero. If yes, return position+1 (2), which is correct.

Another example: a=2, b=5. The decimal is 0.4, so remainder after step 1 is 0. So, new_remainder is zero. If c is zero, return position+1 (2). So in this case, the output would be 2. But the actual decimal is 0.4000..., so the first zero is at position 2.

But if c is 4, then in position 1, digit is 4 → return 1.

If c is 0, return 2.

If c is 5, return -1.

This logic seems correct.

Now, the code needs to handle these steps. But how to track the 'seen' remainders. For each new_remainder, we need to check if it's been seen before. Because once a remainder is encountered again, the digits start repeating.

For example, consider a=1, b=3. The decimal is 0.(3). So steps:

current_remainder starts as 1.

position 1:

current_remainder *=10 →10. digit=3. new_remainder=1. 10%3=1.

If c is 3, return position 1.

Else, new_remainder is 1, which is already in 'seen' (since initial 'current_remainder' was 1, and in the first iteration, new_remainder is 1, which is added to 'seen' as position+1=2.

Wait, no. Let's walk through the code step by step.

Example: a=1, b=3, c=3.

current_remainder =1.

position=1:

current_remainder *=10 →10.

digit =10//3=3 →3. if c is 3, return 1. So code would output 1.

If c is not 3, like c=6:

current_remainder=1. Processing:

position=1:

digit=3. Not 6. new_remainder=1%3=10%3=1 → new_remainder=10%3=1?

Wait, wait:

current_remainder after multiplying by 10 is 10.

digit is 10//3=3.

new_remainder is 10%3=1.

So, new_remainder is 1.

Check if new_remainder is 0 → no.

Check if new_remainder is in 'seen' → initially, 'seen' is empty.

Add new_remainder (1) to 'seen' with position+1=2.

current_remainder is now 1.

Next position is 2:

current_remainder *=10 →10.

digit=3 again. If c is 6, not 3. new_remainder=1 again.

Check if new_remainder is zero → no.

Check if new_remainder is in 'seen' → yes, because 'seen' has 1 → position 2.

So return -1.

Which is correct.

So the code correctly detects the cycle and returns -1.

Now, the code needs to handle all these cases.

Another test case:

Input 2 3 7.

The decimal is 0.(6). So the code would process:

current_remainder=2.

position=1:

current_remainder *=10 →20.

digit=20//3=6. Check if 6==7 → no.

new_remainder=20%3=2.

Check if new_remainder is 0 → no.

Check if new_remainder (2) is in 'seen'. Initially, 'seen' is empty. Add 2 with position+1=2.

current_remainder=2.

position=2:

current_remainder *=10 →20.

digit=6 again. Not 7. new_remainder=2.

Check if in 'seen' → yes (2 was added at position 2). So return -1.

So code outputs -1, which matches the example.

Another example: a=1, b=6. The decimal is 0.1(6). Let's see.

current_remainder=1.

position 1:

current_remainder *=10 →10.

digit=10//6=1. If c is 1, return 1.

Else, new_remainder=10%6=4.

Add 4 to 'seen' with position 2.

position 2:

current_remainder=4*10=40 → digit 6 (40//6=6), new_remainder 40%6=4.

Check digit == c. If c is 6, return 2.

Else, new_remainder=4 is in 'seen' (since position 2, the new_remainder is 4, which was added in position 2-1=1? Wait, perhaps I'm getting confused.

Wait, in the code's logic:

In the first step (position 1):

current_remainder is 1.

Multiply by 10 →10.

digit is 1. new_remainder is 10%6=4.

Then, check if new_remainder (4) is zero. No.

Check if 4 is in 'seen' (which is empty now). No. Add 4 to 'seen' with position+1=2.

current_remainder becomes 4.

Next iteration (position 2):

current_remainder *=10 →40.

digit=6. new_remainder=40%6=4.

Check if digit is c. If c=6, return 2.

Else, check new_remainder is 4, which is in 'seen' (position 2). So return -1.

So for example, if c is 6, output is 2. If c is 4, then after processing position 1, digit is 1 (not 4). Then new_remainder is 4. Then, in next step (position 2), digit is 6 (not 4). new_remainder is 4. Which is in 'seen' (position 2). So return -1.

Thus, code works.

Now, code steps:

Implement the algorithm:

Read a, b, c.

current_remainder = a.

seen = { current_remainder: 1 }

But wait, no. Because the code starts processing position 1. The initial current_remainder is a. Then, during position 1 processing, current_remainder is multiplied by 10. But the seen map is for new_remainder.

Wait, in the code's 'seen' dictionary, when we process a step, we check if the new_remainder is in the map. So the code starts with:

current_remainder = a.

Then, in the loop:

for each position in 1, 2, ...:

   current_remainder *=10 → becomes a*10 for first iteration.

   digit = current_remainder // b.

   if digit ==c → return.

   new_remainder = current_remainder %b.

   if new_remainder ==0:

       handle zero case.

   if new_remainder in seen → cycle → return -1.

   add new_remainder to seen with position +1.

   current_remainder = new_remainder.

So, in the code, the 'seen' dictionary is tracking the new_remainder and the next position (position+1).

So the first time through:

current_remainder is a.

Multiply by 10 → a*10.

digit is (a*10)//b.

new_remainder is (a*10) %b.

Check if new_remainder is zero. If not, check if in seen. The initial 'seen' is empty, so add new_remainder with position+1=2.

Wait, no. Because the first time through, position is 1. So when adding to 'seen', new_remainder is added with position+1=2.

Because the next position after position 1 is 2.

So, the code's 'seen' is a dictionary that maps each new_remainder to the next position.

Thus, in the next iteration, when we process position 2, current_remainder is new_remainder from the previous step.

So, the code correctly tracks the next position.

Now, the code needs to implement this.

But how to loop? Because the code can't loop infinitely.

In Python, we can use a while loop, which continues until we return.

So, code outline:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    current_remainder = a

    seen = {}

    position = 1

    while True:

        current_remainder *= 10

        digit = current_remainder // b

        if digit == c:

            print(position, file=output_stream)

            return

        new_remainder = current_remainder % b

        if new_remainder == 0:

            if c == 0:

                print(position +1, file=output_stream)

            else:

                print(-1, file=output_stream)

            return

        if new_remainder in seen:

            print(-1, file=output_stream)

            return

        seen[new_remainder] = position +1

        current_remainder = new_remainder

        position +=1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 3 7
""",
            "output": \
"""\
-1
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

Another test case: 2 3 7.

current_remainder=2.

position=1:

current_remainder *=10 →20.

digit=6 !=7.

new_remainder=20%3=2.

Check if new_remainder is 0 → no.

Check if 2 is in seen → no.

Add 2 to seen with position+1=2.

current_remainder=2.

position becomes 2.

Loop:

current_remainder *=10 →20.

digit=6 !=7.

new_remainder=2.

Check if new_remainder is 0 → no.

Check if 2 is in seen → yes (it was added in the first step with position 2). So print -1.

Which is correct.

Another test case where the remainder is zero and c is zero. For example, a=1, b=5. The decimal is 0.2000...

So, for c=0:

position 1: current_remainder=1*10=10 → digit=2. Not 0. new_remainder=0.

Check new_remainder is zero → yes. Check if c=0 → yes. Return position+1=1+1=2. Which is correct, as the digits are 2 followed by 0s.

Another test case: a=3, b=4 → decimal 0.75. So new_remainder after step 1 is 3*10=30 →30//4=7. new_remainder=30%4=2. Then step 2: current_remainder=2*10=20. digit=5. new_remainder=0.

If c is 5, returns position 2. If c is 0, returns 3.

So code should handle that.

Thus, the code seems correct.

Now, code considerations:

- The 'seen' dictionary can grow up to O(b) entries. For b up to 1e5, this is manageable.

But in Python, dictionaries can handle that.

- The loop runs at most O(b) times, which for b up to 1e5 is acceptable, as 1e5 operations are manageable within 1 second.

Thus, the code should work within the constraints.
</think>

```python
a, b, c = map(int, input().split())
current_remainder = a
seen = {}
position = 1

while True:
    current_remainder *= 10
    digit = current_remainder // b
    if digit == c:
        print(position)
        break
    new_remainder = current_remainder % b
    if new_remainder == 0:
        if c == 0:
            print(position + 1)
        else:
            print(-1)
        break
    if new_remainder in seen:
        print(-1)
        break
    seen[new_remainder] = position + 1
    current_remainder = new_remainder
    position += 1
```
