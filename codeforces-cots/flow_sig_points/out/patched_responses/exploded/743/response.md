<think>
Okay, let's see. The problem is to find the maximum height of a pyramid given n cubes. The pyramid's levels are built such that the i-th level requires 1+2+...+i cubes. Wait, wait. Wait, the description says that the top level is 1 cube, the second has 3 (1+2), third 6 (1+2+3), etc. So each level i (starting from 1) requires the sum of 1 to i cubes. So for level 1: 1 cube, level 2: 3 cubes, level 3: 6, level 4: 10, and so on. The total cubes used for a pyramid of height h is the sum of the first h triangular numbers.

So the problem reduces to finding the largest h such that the sum of the first h triangular numbers is ≤ n.

The sum of the first h triangular numbers is known to be h*(h+1)*(h+2)/6. Wait, right? Because each triangular number is k(k+1)/2 for k from 1 to h. Summing that from k=1 to h gives the sum S = sum_{k=1 to h} k(k+1)/2 = [h(h+1)(h+2)] / 6. Let me confirm that formula. Let's see for h=1: 1*2*3/6=6/6=1. Correct. h=2: 2*3*4/6=24/6=4, which is 1+3=4. Yes. h=3: 3*4*5/6=60/6=10, which is 1+3+6=10. Yep. So the formula holds.

So the problem becomes finding the maximum h where h(h+1)(h+2)/6 ≤ n.

Given n, we need to compute the largest h for which this inequality holds. So the approach would be to compute this h efficiently.

Now, given that n can be up to 1e4, but perhaps even for larger n, we can compute h via binary search. Wait, but what's the maximum possible h for n up to 1e4? Let's see:

We can compute h where h^3/6 <= n. So h^3 <=6n. So for n=1e4, 6n=6e4, h^3 ~6e4, h is around cube root of 6e4 which is cube root of 60000. Cube of 39 is 59319, 40^3=64000. So h would be up to 40 or so. So even a linear search would work for n up to 1e4, since 40 iterations are negligible.

But for the sake of efficiency, even if binary search is overkill, perhaps a binary search approach would be better. Let's think.

But given the small possible h, even a loop that increments h until the sum exceeds n would be efficient. Let's think about the steps for h=1, 2, etc., compute the sum until it's larger than n, then return h-1.

For example, take the sample input 25:

h=4: sum is 4*5*6/6= 120/6=20. 20 <=25. Next h=5: 5*6*7/6=210/6=35>25. So maximum h is 4. Which matches the sample.

Another example, n=1: h=1 is 1, which is equal to 1. So output is 1.

So the approach can be:

Initialize h=0, sum=0. Iterate h from 1 upwards, compute the current sum. If sum exceeds n, return h-1. Otherwise, continue.

But how to compute the sum for each h? Using the formula h*(h+1)*(h+2)/6.

So the loop would be:

h starts at 1.

current_sum = h*(h+1)*(h+2)//6

if current_sum >n, then return h-1.

Else, increment h.

Wait, but for h=1, current_sum is 1*2*3/6=6/6=1. If n is 1, then current_sum is equal to n. So h is 1. If n is 1, then the loop would check h=1, sum=1. Since 1 <=1, increment h to 2, compute sum=2*3*4/6=24/6=4. Now 4>1, so return h-1=1. Which is correct.

So the steps would be:

Initialize h=0.

Loop:

h +=1

sum = h*(h+1)*(h+2)//6

if sum >n: break

so after breaking, the answer is h-1.

But wait, no. Because the sum is for h. So for example, when h=4, sum is 20. Which is <=25. Then h increments to 5, sum is 35. Which is >25. So the answer is h-1=4.

So the loop is:

start h=0, current_h=0.

Then, in each iteration:

h +=1

compute sum for h.

if sum >n: break.

then return h-1.

But how to handle the case where sum equals n exactly? Like n=1. Then sum is 1 when h=1. So sum is not >n. Then h increments to 2. sum is 4>1. So returns 2-1=1. Correct.

Another case: n=20. Then h=4: sum=20. Not >20, so h increments to 5. sum=35>20. So returns 4. Correct.

So the algorithm works.

So the code can be written as:

Read n.

Initialize h=0.

loop:

h +=1

current_sum = h*(h+1)*(h+2) //6

if current_sum >n:

    break

return h-1.

But how to implement this? In Python:

n = int(input())

h = 0

while True:

    h +=1

    current = h*(h+1)*(h+2) //6

    if current >n:

        break

print(h-1)

But wait, let's test for n=1:

Loop starts with h=0.

h becomes 1. current is 6//6=1. Which is equal to 1. So not >n. So loop continues.

h increments to 2. current is 2*3*4=24//6=4>1. Break. print(2-1)=1. Correct.

Another test case: n=25.

h increments to 4, current=4*5*6=120//6=20 <=25. Loop continues.

h=5: 5*6*7=210//6=35>25. Break. print(5-1=4). Correct.

Another test case: n=10. The sum is 20 for h=4. Wait, no. Wait when h=3, sum is 3*4*5//6=60//6=10. So current_sum is 10. So h=3: sum=10. So if n=10, the code will:

h increments to 1: sum 1. <=10.

h=2: sum 4 <=10.

h=3: sum 10 <=10.

h=4: sum 20>10. Break. So print 3. Which is correct.

So the code works.

But what about when n is exactly the sum for h=5, like n=35. Then code would break when h=5 is sum 35, which is equal to n. So code would not break. Then h increments to 6, sum 6*7*8/6= 56*6=336/6=56. 56>35. So return 6-1=5. Correct.

Thus, the code works.

But wait, let's compute h*(h+1)*(h+2) //6 for h=5: 5*6*7=210, 210//6=35.

So for n=35, the code would have:

h increments to 5, current=35. 35 <=35. So loop continues.

h becomes 6, current=6*7*8//6= 336//6=56. 56>35. Break. return 5. So correct.

Thus, the code works.

So the code is straightforward. The time complexity is O(h_max). For n up to 1e4, h_max is about 40, which is trivial.

So this approach is optimal and efficient. No need for binary search here.

But let's consider possible maximum h for n up to 1e4. Let's compute h*(h+1)*(h+2) <=6n.

For n=1e4, 6n=6e4.

We can compute h:

h=39: 39*40*41=39*1640= 63960. 63960/6=10660. Which is 10660. That's for h=39. The sum is 10660. So if n is 1e4 (10000), then 10660>10000. So h=39 is sum 10660>10000. So maximum h is 38. Let's compute for h=38: 38*39*40= 38*1560= 59280. 59280/6= 9880. 9880<=10000. So h=38 would be allowed, and h=39 would exceed. So the maximum h is 38.

So for n=1e4, the code would loop h from 1 to 39, which is 39 iterations. No problem.

Thus, the code is efficient enough.

So the code is correct and efficient.

Now, let's code it in Python.

Read n as input.

Initialize h=0.

Loop:

h +=1

compute current = h*(h+1)*(h+2)//6

if current >n: break.

print h-1.

Yes.

Testing the sample inputs:

Sample 1:

Input:1.

Loop:

h=1, current=1*2*3//6=6//6=1. Not >1. Continue.

h=2: current=2*3*4//6=24//6=4>1. Break. Output 1.

Sample 2:

n=25.

h=4: current=4*5*6//6=20 <=25. h increments to 5: 5*6*7//6=35>25. Break. Output 4.

Yes.

Another test case: n=10. Output 3.

Another test case: n=35. Output 5.

Thus, the code works.
</think>

```python
n = int(input())
h = 0
while True:
    h += 1
    current = h * (h + 1) * (h + 2) // 6
    if current > n:
        break
print(h - 1)
```