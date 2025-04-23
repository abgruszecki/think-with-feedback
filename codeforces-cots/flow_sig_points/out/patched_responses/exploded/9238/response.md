<think>
Okay, I need to solve this problem where Mike is building a resistor network using the minimum number of unit resistors. The goal is to find the smallest number of resistors required to achieve a resistance of a/b. Let's think through this.

The problem says that each resistor is 1 ohm. The operations allowed are adding a resistor in series or in parallel to an existing element. So, for each step, we can build up the resistance using these operations, and we need to model how that affects the resistance and the count of resistors used.

Let's start by understanding how the series and parallel additions work. For series, adding a resistor to an element with resistance Re gives Re + 1. For parallel, adding a resistor to Re gives 1/(1/Re + 1/1) = Re/(Re + 1). Wait, no. Wait, the formula for parallel is 1/( (1/Re) + (1/R0) ), where R0 is 1. So that's 1/( (1/Re) + 1 ) = Re/(Re + 1). Right.

But how do these operations affect the fraction a/b? Let's model this as fractions and see how they can be built up.

Let's think recursively. Suppose we have a resistance R = p/q. To get this, what was the previous step? Because each step adds one resistor, the previous step must have been either a series addition (so previous resistance was (p/q) - 1) or a parallel addition (so previous resistance is p/(q - p), but only if q > p). Wait, let's see.

For example, if the current step was adding in series, then previous resistance Re is R_prev. So R_prev + 1 = p/q. So R_prev = (p/q) - 1 = (p - q)/q. But this would only make sense if (p - q) is positive, because resistance can't be negative. So p/q must be greater than 1. Then, the previous resistance would be (p - q)/q, but since R_prev must be positive, we must have p > q.

Alternatively, if the previous step was adding in parallel, then R_prev and 1 are in parallel. The combined resistance is (R_prev * 1) / (R_prev + 1) = R_prev/(R_prev + 1). But wait, no—when you add in parallel, the new resistance is 1/(1/R_prev + 1/1) → which equals 1/( (1 + R_prev)/(R_prev) ) → R_prev/(1 + R_prev). So if the current resistance is p/q, then R_prev/(R_prev + 1) = p/q. Solving for R_prev gives R_prev = p/(q - p). But for R_prev to be positive, q - p must be positive, so p < q. Then R_prev is p/(q-p).

So, the idea is to model this as a fraction and work backwards. For example, given a target fraction a/b, we can decompose it step by step by subtracting 1 (series step) or inverting the subtraction (parallel step) until we reach 1/1, which requires 1 resistor. Each step increments the count of resistors by 1.

But since the problem asks for the minimum number of resistors, this suggests that we need to find the shortest path from 1/1 to a/b by applying the inverse operations. So, the approach would be similar to the Euclidean algorithm for GCD. Let's think of this in terms of how to reduce a/b to 1.

Let's take an example. Let's look at the sample input 3/2. How do we get there?

In the sample, the answer is 3. The steps are: two resistors in parallel (1/(1+1) = 1/2), then adding a resistor in series gives 1/2 + 1 = 3/2. So total 3 resistors. But when working backwards, 3/2 can be written as (1/2) +1. So previous step would be 1/2. Then, 1/2 is R_prev/(R_prev +1) → R_prev is 1. So then that's the first resistor. So the steps backwards are 3/2 → 1/2 (parallel step) → 1 (series step). Wait, no. Let me see:

Wait, the current resistance is 3/2. Since it's larger than 1 (3/2 = 1.5), the previous step must have been a series addition. Because a parallel step would lead to a resistance less than 1. So previous step was (3/2 - 1) = 1/2. So subtract 1, and that's a series step. Then, the 1/2 must have come from a parallel step. Because 1/2 is less than 1. So R_prev/(R_prev +1) = 1/2. Solving that gives R_prev = 1. So the previous step was 1, which takes 1 resistor. So total steps: 1 (series step, add 1 resistor) → 2 resistors (1/2) → then series step again? Wait, no. Wait, the steps are: first resistor (1). Then, add a resistor in parallel (so two resistors). Then add a resistor in series (total three). So when working backwards, 3/2 → subtract 1 (1/2) → then invert the parallel operation (so 1/2 = R_prev/(R_prev +1) → R_prev is 1). Then R_prev is 1, which takes one resistor. So total steps: 3.

So working backwards, each step we can either subtract 1 (if a/b >1) or invert (if a/b <1), but the way the steps work is that each step corresponds to one operation (series or parallel) and thus adds one resistor. The total number of steps is the number of resistors minus 1, but not exactly. Let's model this.

The key observation is that the problem can be modeled as a continued fraction decomposition of a/b.

Let me try to see how the process works. Let's take the example where a=199, b=200. The answer is 200. So in this case, the fraction is 199/200, which is just under 1. To reach this, we must have added a resistor in parallel to a previous step. So the previous step would have resistance R_prev = 199/(200-199) = 199/1 =199. Then, 199 is larger than 1, so that must have come from adding resistors in series. For example, 199/1 would have required 199 steps of series additions. So total resistors would be 199 (for the 199/1) plus 1 (for the parallel step) → 200. Which matches the sample.

So the approach is to model this as a process of reducing the fraction a/b step by step. Each time, if the current fraction is greater than 1 (a > b), we subtract 1 (series step) and add the count, but in reality, subtracting 1 once would account for adding one resistor. However, when a is much larger than b, like in the case a=199, b=1, we can subtract 1 as many times as possible. Wait, but in that case, the initial approach would subtract 199 times 1, each step adding a resistor. So the count would be 199.

But wait, when you have a resistance of 199/1, how do you get there? Starting from 1, you add 198 resistors in series. So the total is 199 resistors. So each time you subtract 1 from the current a/b, that's equivalent to a series step. So for each subtraction of 1, you add one resistor. But when a is much larger than b, you can subtract multiple times. For example, if a is 5 and b is 2 (5/2), then that's 2 steps of subtracting 1 (5/2 → 3/2 → 1/2, but wait, no, that's not right). Wait, let's think.

Wait, 5/2 is greater than 1. So subtract 1 → 3/2. Then again, 3/2 is greater than 1, subtract 1 → 1/2. Then, 1/2 is less than 1. So the steps would be 5/2 → 3/2 (series step, count increases by 2?), or how?

Wait, perhaps the approach is similar to the Euclidean algorithm. For example, when a > b, the number of times you can subtract 1 (series steps) is equal to (a//b) times. Then, the remaining a becomes a mod b. Each of those steps contributes (a//b) resistors, but perhaps not. Let's think.

In the case of a=5, b=2: 5/2 is 2 + 1/2. So the series steps would have added 2 resistors (each contributing 1 ohm in series). Then, the remaining 1/2 is handled via parallel steps.

Wait, how? Let's model this.

Original target:5/2. Since 5>2, subtract 2 (i.e., a//b =2) → 5-2*2=1 → new a is 1, b is 2. So the total resistors added here would be 2 (since each subtraction of 1 contributes 1 resistor). Then, the remaining 1/2 is handled by a parallel step.

So the steps would be:

Start with 1 resistor (1/1). Then, two series steps add 2 resistors (total 3), making 1+2=3. Then, add a parallel step (adding 1 resistor, total 4), leading to 3/(3+1) = 3/4. Wait, that's not matching. Hmm. Maybe I'm getting confused here.

Alternatively, perhaps the way to model it is to think that each time a > b, we can subtract (a//b) * 1 from the fraction, which reduces it by (a//b) steps of series connections. Each such step contributes (a//b) resistors. Then, the remaining a is a mod b. But perhaps this is the right approach.

Wait, let's take the example where a=5, b=2. So the fraction is 5/2. Since 5>2, we can subtract 2 (since 5//2 is 2) → 5-2*2=1. So the new fraction is 1/2. The resistors added here are 2 (each subtraction of 1 contributes 1 resistor). Then, for the 1/2, which is less than 1, we invert the problem. So the previous step would have been a parallel step. So 1/2 comes from R_prev/(R_prev +1) → R_prev=1. Then we add 1 resistor (the parallel step), total 3 resistors. Wait, but 1 resistor is for the initial R_prev=1, then adding a parallel resistor (total 2), then adding 2 series steps (each contributing 1 resistor) → total 2 + 2 =4 resistors. Hmm, but how does that align with the steps?

Alternatively, maybe the correct approach is to model the problem as follows:

The minimal number of resistors is the sum of the coefficients when the fraction a/b is decomposed via the continued fraction method, similar to the Euclidean algorithm. So for example, whenever a > b, we subtract as many 1's as possible (equivalent to a//b steps of series addition), which adds a//b resistors. Then, the remaining a is a mod b. Then, invert the fraction (since after the series steps, the next step is a parallel step). And so on, until we reach 1.

Let's take the sample input 3/2. a=3, b=2.

a > b → subtract 1 once (3-2=1, a//b=1). So add 1 resistor. Now the remaining is 1/2. Then invert, since this step is a parallel step. The next fraction is 2/1. Now, a >b again. Subtract 2/1 (a//b=2) → add 2 resistors. Wait, but this would make the total 1+2=3, which matches the sample.

Wait, how? Let's see:

3/2 → subtract 1 (series step) → 1/2, count +=1.

Invert 1/2 → 2/1, then subtract 2 → 0, count +=2. Then total is 1+2=3. That works.

But how does inverting work here?

Another example: 199/200. a=199, b=200. Since a <b, invert the fraction to 200/199. Then, subtract 1 (200//199=1) → 200 - 199*1 =1. count +=1. Then, invert again (1/1) → count +=1. But 1/1 requires 1 resistor. So total is 1 (from 199/200) → invert (count +=0?), subtract 1 (count +=1), invert (count +=1?), but maybe the inversion steps don't contribute directly to the count. Hmm, perhaps the inversion steps are part of the process, but the resistors are added when we process the a//b steps.

Wait, maybe the correct algorithm is:

Initialize count =0.

While a and b are not equal:

   if a > b:

      count += a // b

      a = a % b

   else:

      count += b // a

      b = b % a

But when a and b are coprime, this would sum up the steps similar to the Euclidean algorithm. Wait, but for example, in the case of 3/2:

Step 1: a=3, b=2. a >b.

count +=3//2=1. a becomes 1. Now, a <b.

Step2: a=1, b=2. b//a=2. count +=2. a=1, b=0. But since b=0, loop ends. Then the total count is 1+2=3. Which matches the sample.

Another example: 199/200. Since a <b, we swap them and do:

a=200, b=199. a//b=1. count +=1. a becomes 1. Then, b=199, a=1. Now, b//a=199. count +=199. a becomes 1, b=0. Total count is 1+199=200. Which matches the sample.

Another example: 1/1 → count is 0. But the loop never runs, so we need to add 1 at the end?

Wait, this seems like the algorithm would work, but perhaps the initial approach misses the case where a and b are 1.

Wait, let's test with the first sample input: 1/1.

The loop condition (a and b not equal) is false, so loop doesn't run. Then, the count is 0. But the answer is 1. So the algorithm would return 0, which is incorrect.

Hmm, so the problem is that when a ==b, which implies that the fraction is 1, which requires 1 resistor. So the code needs to handle this case.

So the algorithm would be:

Compute the sum of the integer divisions (a//b and b//a) as you go through the steps. Then, when a and b become equal (but not 0), add 1 to the count (since that's one resistor). Wait, but for the case where a and b are 1, the sum is 0 (since no steps are taken), and then adding 1 gives the correct answer.

So the steps would be:

Initialize count=0.

While a !=0 and b !=0:

   if a >=b:

      count += a//b

      a %=b

   else:

      count +=b//a

      b %=a

But wait, when a or b becomes 0, then the loop stops. Then, since the original fraction is irreducible, the only time one becomes 0 is when the other is 1. For example, after processing 199/200, the steps would be:

a=200, b=199.

count +=1 → a=1.

Then, since a=1, b=199:

count +=199 → b=0. Then loop stops.

So total count is 1+199=200.

But when a and b are 1, the loop doesn't run, so count remains 0. Then, the answer is 1. So we need to handle that case.

So the code would be:

After computing the count via the loop, check if a + b ==0 (both zero) → but that's impossible since the input is a/b which is irreducible, so the loop will end when either a or b is 0, and the other is 1. Wait, no. Wait, the loop continues as long as a and b are not zero. So when a becomes 1 and b is 0, the loop stops. So in that case, the sum is count plus 1 (for the 1 resistor).

Wait, perhaps the code should be:

count =0

while a !=0 and b !=0:

    if a > b:

        count += a // b

        a = a % b

    else:

        count += b //a

        b = b %a

But after the loop, if a ==0:

    the original fraction was (b, something) → but since the input is irreducible, the only case when a becomes 0 is when the original fraction was 1/1. Wait, no. For example, the 3/2 case:

In processing 3/2 → a=3, b=2:

a//2 =1 → count +=1. a=1.

Now, b=2, a=1.

count +=2//1=2. b=0.

Loop stops.

So the count is 3. Which is correct.

But in the case where a and b are 1, the loop doesn't run. So count remains 0, but the correct answer is 1. So how do we handle that?

Wait, perhaps the loop's initial condition is not sufficient. Let me think. The loop runs while a and b are not zero. So when a=1 and b=1, the loop condition is true, but inside, a >=b, so a//b is 1. count +=1. a becomes 0. Then the loop stops. So the count is 1, which is correct.

Wait, let's test the sample input 1/1.

Initial a=1, b=1.

Loop runs since a and b are not zero.

a >=b (1 >=1). a//b is 1. count +=1.

a =1%1 =0.

Now, the loop condition checks a and b are not zero. Since a is 0, the loop stops. So count is 1. Which is correct.

Wait, that's different than what I thought earlier. So in the code, when a and b are 1, the loop runs once, and adds 1 to the count, then a becomes 0, and the loop stops. So the count is 1. Which is correct.

So the code would be:

count =0

while a !=0 and b !=0:

    if a >=b:

        count += a //b

        a %=b

    else:

        count += b //a

        b %=a

print(count)

But let's test this with the sample inputs.

Sample 1: 1 1 → count is 1. Correct.

Sample 2:3 2 → steps:

a=3, b=2.

a >=b → add 3//2=1. a becomes 1.

b is 2, a=1. So a <b.

Add 2//1=2. count becomes 1+2=3. b becomes 0. Loop stops. Correct.

Sample 3:199 200.

a=199, b=200. a <b.

Add 200//199=1 → count=1. b=200%199=1.

Now a=199, b=1. a >=b.

Add 199//1=199 → count=200. a=0. Loop stops. Correct.

Another test case: 5/2.

a=5, b=2. a >=b. 5//2=2. count +=2. a=5%2=1. Now, b=2, a=1.

Add 2//1=2 → count=4. b=0. So total 4 resistors. Let's see.

How would you build 5/2?

Start with 1 resistor (1). Add two in series: 1+1+1=3. Then add two resistors in parallel: 3 in series with two parallel resistors. Wait, no. Hmm. Let's think.

Alternatively, when working backwards:

5/2 → subtract 2 (series steps) → 1/2. Then invert to 2/1. Subtract 2 (series steps) → 0. But how does this add up to 4 resistors?

Hmm, perhaps the code works but the reasoning is a bit different. For example:

The code's logic is that each time you take a//b, you add that to the count, which represents the number of resistors added in that step. Then, the remaining a is a mod b. For example, in 5/2 → the code adds 2 (series steps) → resistors added 2. Then, for 1/2 → invert, add 2 (parallel steps?), which gives a count of 4. So the code returns 4. But how does this work in practice?

Let's see. To build 5/2:

Possible steps:

Step 1: 3 resistors in series (3 ohms). Then, add a parallel resistor (so 3 in parallel with 1 → resistance is 3/(3+1) = 3/4. Then add another series resistor (3/4 +1 = 7/4, which is 1.75). Hmm, not 5/2. Alternatively, maybe there's a different arrangement.

Alternatively, maybe the code's approach is correct, but the way the resistors are added in series and parallel steps accumulates the count in a way that's not obvious. But according to the code's logic, the answer for 5/2 is 4. Let's check what the code's output would be.

So code returns 4. Let's see how that's possible.

Another approach: Each step in the code represents a series of steps where you add multiple resistors in a single operation. For example, when a is much larger than b, the code adds all the possible series steps at once, which adds a//b resistors. Similarly for parallel steps. But how?

Wait, when a >b, the code adds a//b resistors for each series step. For instance, a=5, b=2. The code adds 2 resistors (5//2=2), which implies that adding two resistors in series. So the initial 1 ohm resistor plus two in series would make 3, but the code's step is a//b=2. Then the code processes the remaining a mod b, which is 1.

But then, 1/2 is processed by adding 2 resistors (parallel steps). So how does that lead to 5/2?

Alternatively, perhaps the code's approach is correct, but the steps are a combination of series and parallel operations, not necessarily in a way that's obvious. For example, the code's logic is that each time you have a fraction greater than 1, you can subtract all possible 1's (series steps) at once, adding a//b resistors. For fractions less than 1, you invert (so it's handled as parallel steps) and subtract (series steps again). This seems similar to the Euclidean algorithm for GCD, which runs in O(log min(a, b)) time, which is acceptable for a=1e18.

So the code is correct. Let's test the sample 5/2. According to the code, the answer is 4. Let's see how to build it.

The code's approach suggests that 5/2 is built in 2 + 2 =4 steps. Let's model it:

Start with 1 resistor (1 ohm).

Then, add two resistors in series: 1+1+1=3 (3 resistors). Now, the resistance is 3.

Then, add a resistor in parallel. The new resistance is 3*1/(3+1) = 3/4. 4 resistors.

But then, adding a resistor in series gives 3/4 +1 =7/4=1.75, which is 7/4, not 5/2.

Hmm, this doesn't add up. So perhaps the code is incorrect. Wait, what's the correct minimal number of resistors for 5/2?

Wait, perhaps there's another way.

Suppose:

Start with two resistors in parallel: 1/(1+1) = 1/2.

Then, add three resistors in series: 1/2 +3= 3.5 =7/2. Not 5/2.

Alternatively, two resistors in series (2 ohms) and then two in parallel:

2 in parallel with 1 → 2/(2+1) = 2/3. Then add two in series → 2/3 +2 = 8/3 ≈2.666. Not 5/2.

Hmm. Alternatively:

Another approach: 5/2 = 2 + 1/2. So to get this, you can have a series step of adding two resistors (each in series) to a previous resistance of 1/2.

So, the previous resistance is 1/2. How to get that? That's two resistors in parallel. So total steps: two resistors (parallel) → 1/2. Then adding two in series → 1/2 +2 = 5/2. Total resistors: 2+2=4. Which matches the code's output.

So how:

Resistors used: 2 (parallel) gives 1/2. Then adding two in series: each adds 1 ohm. So total 4 resistors. Resistance is 1/2 +2 =5/2. Correct. So the code's answer is correct.

Thus, the code's approach is correct.

So the algorithm is:

We repeatedly subtract the maximum possible multiples of the smaller number from the larger, adding the quotient to the count. This is similar to the Euclidean algorithm for GCD. The total count is the sum of the quotients obtained in each step. This gives the minimal number of resistors required.

Thus, the code is as follows: read a and b, then perform the steps of the algorithm, then output the count.

Now, the code must handle very large numbers (up to 1e18), but since the algorithm is O(log(min(a, b))), it will be efficient enough even for the largest input.

Now, implement this in Python.

So code steps:

Read a and b as integers.

Initialize count=0.

While a !=0 and b !=0:

   if a >=b:

      count += a//b

      a %=b

   else:

      count +=b//a

      b %=a

Print(count).

Wait, but let's test the first sample input 1 1:

a=1, b=1.

Loop runs since a and b are not zero.

a >=b: count +=1//1=1 → count=1. a becomes 0.

Loop ends. Print 1. Correct.

Another example: a=3, b=2.

Loop:

a=3 >=2 → count +=1 → a=1.

Now, b=2, a=1.

count +=2//1=2 → count=3. b=0.

Loop ends. Print 3. Correct.

Another example: a=199, b=200.

a=199 <200 → count +=200//199=1 → b=200%199=1.

Now, a=199, b=1.

a >=b → count +=199//1=199 → a=0. count=200. Print 200. Correct.

Thus, the code works for all samples.

So the code is:

Read a, b.

count =0

while a !=0 and b !=0:

    if a > b:

        count += a // b

        a = a % b

    else:

        count += b // a

        b = b % a

print(count)

But wait, the code uses the condition a >b and a >=b? Let's check.

In the code, when a >=b, we do a//b and add to count, then a %=b.

Wait, the code above has a >=b, but in code:

if a >=b:

    count += a//b

    a %=b

else:

    count +=b//a

    b %=a

Wait, but in the previous examples, when a and b are equal, like 1/1, then a//b is 1, and a becomes 0. Which is correct.

So the code uses a >=b condition. So yes, that's correct.

Thus, the code should be written as follows.
</think>

```python
a, b = map(int, input().split())
count = 0
while a != 0 and b != 0:
    if a >= b:
        count += a // b
        a %= b
    else:
        count += b // a
        b %= a
print(count)
```