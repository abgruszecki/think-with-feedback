<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So the problem is about Mashmokh saving tokens each day such that the money he gets is maximized. For each day, he gets some tokens, then gives back some to get money. The money is calculated as the floor of (w * a)/b, where w is the number of tokens he gives back. The goal is to find, for each day, the maximum number of tokens he can save (i.e., the amount not given back) while still getting the maximum possible money that day.

Hmm. So for each day, we have to compute the maximum possible savings, which is x_i minus the minimal possible w that gives the maximum possible money. Wait, no. Wait, the money is maximized when he gives the optimal w. But then, he wants to save as many tokens as possible, which means he wants to choose the smallest possible w that gives the maximum possible money. Because if there are multiple w's that result in the same maximum money value, he can choose the smallest w, thus saving the most tokens (x_i - w).

So the problem breaks down into, for each x_i, compute the minimal possible w that allows the maximum possible money. Then the answer is x_i - w.

But how to compute that minimal w?

Let me think. The maximum possible money is floor( (w *a ) /b ). To maximize this value, we need to find the maximum possible floor( (w *a ) /b ) given that w is between 0 and x_i (since he can give back up to x_i tokens each day).

The maximum possible value of this floor is achieved when w is as large as possible. Wait, but what if (x_i *a )/b is not an integer? Then the maximum floor is floor( (x_i *a )/b ), which would be achieved when w is x_i. But maybe there's a smaller w that gives the same floor value. For example, if a and b are such that adding more tokens doesn't increase the floor. So Mashmokh can choose the minimal w that gives this maximum floor, thereby saving more tokens.

Wait, let's think. Let's denote M as the maximum possible floor value for a particular day. Then, M is equal to floor( (x_i * a ) / b ). Because when w is x_i, (x_i *a )/b is the maximum possible, so the floor is M. However, perhaps there exists a smaller w where floor( (w *a)/b ) is equal to M. So the minimal w is the smallest w where floor( (w *a)/b ) = M, and then the answer is x_i - w.

Wait, but that can't be. Because if M is the maximum possible, then all w's up to x_i would give floor values <= M. But M is achieved when w is x_i. So how can there be a smaller w where the floor is M? Unless for some w < x_i, (w *a)/b is >= M, but when you take the floor, it's equal to M.

Wait, M is floor( (x_i *a ) /b ). Let me compute that. For example, if x_i is 12, a is 1, b is 4, like in the first example. Then x_i*a is 12*1=12, divided by 4 gives 3. So M is 3. So any w where (w *1)/4 >= 3 would have a floor of 3. But the maximum possible is when w is x_i, which gives exactly 3. So for other w's, like w=12, which gives 3. For w=11, 11/4=2.75 → floor is 2. So that's less. So in that case, the minimal w that gives M is x_i, so the answer is 0 (x_i -12=0). But that's the first example's first output.

Wait, but the first example's input is 5 1 4, and the first x_i is 12. Output is 0. So for that day, he gives all 12 tokens, gets 3 dollars. But maybe there's a smaller w where he can get the same 3 dollars. Let's see: 12*1/4 =3. So floor is 3. Let's see for w=12, M is 3. What if he gives 11 tokens? 11*1/4 is 2.75 → floor 2. So no. So in that case, the minimal w is 12. So he has to give all, save 0.

Another example: in the second input sample, input is 3 1 2. The second x_i is 2. So x_i*a is 2*1=2, divided by 2 is 1. So M is 1. What is the minimal w where floor(w *1/2) =1? The minimal w is 2, because 2/2=1. But wait, wait: when w=2, floor(2/2) is 1. But what if he gives 1 token? Then 1/2 is 0.5, floor is 0. So the maximum M is 1, achieved only when w is 2. So the answer is 2-2=0. Which matches the second example's second output.

Another example from the second sample: third x_i is 3. a=1, b=2. So x_i *a =3. 3/2=1.5 → M is 1. The minimal w that gives floor(w *1/2) =1 is w=2, since 2/2=1. Then 3-2=1. Which matches the output.

So the problem reduces to, for each x_i, compute M = floor( x_i * a /b ), then find the minimal w where floor( w*a /b ) = M. Then the answer is x_i - w.

Wait, but M is the maximum possible. Because when w is x_i, then the floor is M. So the maximum possible value for floor(w a /b) is M, which is achieved at least when w is x_i. So for each x_i, the maximum possible M is fixed. Then, the problem is to find the minimal w such that floor( w a /b ) = M. Then the answer is x_i - w.

So how to find that minimal w?

Let's think about it. We can model the problem as follows: find the smallest w such that:

floor( (w *a ) /b ) = M.

But M is equal to floor( (x_i *a ) /b ). Let's denote that M = (x_i *a ) // b. Because that's how integer division works in Python.

So for each x_i, M is fixed. Now, we need to find the minimal w in [0, x_i] such that floor( (w*a)/b ) = M. Then the answer is x_i - w.

Wait, but maybe for some x_i, the maximum M is not achieved. Wait, no. Because when w is x_i, M is exactly floor( x_i a /b ), which is the maximum possible. So for all other w's <=x_i, their M's can't be higher.

So now the problem is, given M, find the minimal w where floor( (w a)/b ) = M.

Wait, but how to compute that w. Let's express the equation:

floor( (w a)/b ) = M.

Which implies that:

M <= (w a)/b < M+1.

Multiply all terms by b:

M*b <= w a < (M+1)*b.

Divide by a (since a can be zero? Well, according to constraints, a >=1, so no division by zero.)

So (M*b)/a <= w < ( (M+1)*b ) /a.

But w must be an integer. So the minimal w is the minimal integer w that is >= (M*b)/a and such that when multiplied by a, divided by b, the floor is M.

Wait, but (M*b)/a may not be an integer. Wait, no, but we can compute the minimal w such that w >= ceil( (M*b) /a ), and then check if this w when multiplied by a gives a quotient >= M*b and < (M+1)*b.

Wait, perhaps a better approach is to compute the minimal w where w >= ceil( (M*b) /a ), and w <= x_i.

Wait, but M is floor(x_i a /b ), so x_i a >= M*b.

Wait, let's see:

M = floor( (x_i a ) / b )

So M is the maximum possible value for floor( w a /b ), since when w is x_i, we get that value.

So the maximum M is fixed. Now, we need to find the minimal w such that floor(w a /b ) = M. So for that, the minimal w is the minimal integer that satisfies:

w a >= M*b → w >= ceil( (M*b) /a )

and

w a < (M+1)*b → w < ( (M+1)*b ) /a → since w is integer, w <= floor( ( (M+1)*b -1 ) /a )

But in our case, since M is the maximum possible, when we take w as x_i, we have:

floor( x_i a /b ) = M.

But when we compute the minimal possible w, it's the minimal w where floor( w a /b ) = M, which must be >= ceil( (M*b)/a ), but <=x_i.

So the minimal w is the maximum between ceil( (M*b)/a ) and 0 (since w can't be negative). But also, this w must be <=x_i. However, since M is floor( x_i a /b ), then x_i a >= M*b → x_i >= M*b /a. So (M*b)/a <=x_i. So ceil( (M*b)/a ) could be <=x_i.

Wait, let's see. Let me take an example. Let's say x_i is 12, a=1, b=4. Then M is 12*1/4=3. So M is 3. Then M*b is 3*4=12. Then (M*b)/a is 12/1=12. So ceil(12/1) is 12. So the minimal w is 12, which is <=x_i (12). So in this case, answer is 0.

Another example from the first input: let's take x_i=6, a=1, b=4. Then M=6*1/4=1.5 → floor is 1. So M is 1. Then M*b is 4. So (M*b)/a is 4/1=4. So ceil(4) is 4. So minimal w is 4. So he gives 4 tokens, gets 1 dollar, saves 6-4=2. Which matches the sample output.

So the minimal w is the smallest integer >= ceil( (M*b) /a ). Because when w is that value, w*a is >= M*b → (w*a)/b >= M. But since (w*a) < (M+1)*b → (w*a)/b < M+1 → floor is M. So the minimal w is ceil( (M*b)/a ), provided that this value is <=x_i. Because M is floor(x_i a /b ), then x_i a >= M*b → x_i >= (M*b)/a. So (M*b)/a <=x_i. But ceil( (M*b)/a ) could be <=x_i. For example, if (M*b) is exactly divisible by a, then ceil is (M*b)/a. Otherwise, it's the next integer.

So the minimal w is ceil( (M*b)/a ). However, since M is fixed as floor(x_i a /b ), this w can't exceed x_i. Because if x_i a >= M*b → x_i >= (M*b)/a → ceil(M*b/a) could be <=x_i. So the minimal w is ceil(M*b/a). Then, the answer is x_i - w if w <=x_i. But wait, what if ceil(M*b/a) >x_i? Then that's impossible, since M is floor(x_i a /b ), which implies that x_i a >= M*b. So x_i >= (M*b)/a. So (M*b)/a <=x_i. So when we take the ceiling, the minimal w is the smallest integer >= (M*b)/a. So if (M*b) is divisible by a, then (M*b)/a is integer, so ceil is (M*b)/a. Otherwise, it's (M*b//a) +1.

Wait, but what if (M*b) is exactly divisible by a? For example, M=3, a=4, b=4. Then (M*b)/a = (3*4)/4=3 → ceil is 3. So w=3. Then a*w is 12, divided by b (4) is 3 → floor is 3. So correct.

Another example: M=2, a=3, b=5. Then (M*b) is 10. (10)/3 = 3.333, ceil is 4. So w=4. Then 4*3=12, divided by 5 is 2.4 → floor is 2. Which is equal to M.

So the minimal w is indeed ceil( (M*b)/a ).

So the steps to compute for each x_i:

1. Compute M = floor( x_i *a /b )

2. Compute minimal w as ceil( (M*b)/a )

3. The answer for that day is x_i - w.

Wait, but why can't w be lower than ceil(M*b/a)? Because if w is lower than that, then (w*a) < M*b → floor(w a /b ) would be less than M, which is not acceptable. So the minimal w is the smallest w such that w*a >= M*b → which is ceil( (M*b)/a ).

So yes, for each x_i, the answer is x_i - max( ceil( (M*b)/a ), 0 ), but since M is >=0 (since x_i, a, b are positive integers), M*b/a can be zero, but in that case, M is zero, and then ceil(0) is 0, so w would be zero. But in that case, the answer is x_i -0 =x_i, but that's not possible because when M is zero, then floor( x_i a /b ) is zero. So the minimal w is zero. Wait, let's see.

Wait, suppose x_i is 1, a=1, b=1. Then M=1*1/1=1 → floor is 1. So w must be ceil( (1*1)/1 )=1. So answer is 1-1=0. Which is correct.

Another example: x_i=1, a=1, b=2. M is 0. So ceil(0*2 /1) =0. So w=0. Then (0*1)/2=0, floor is 0. So M is 0. So the answer is 1-0=1. But according to the third example in the problem statement, when x=1, a=1, b=1, the output is 0. Which matches the first case.

Wait, but in the third example, the input is 1 1 1. x_i is 1. So M =1*1//1=1. So ceil( (1*1)/1 )=1. So w=1. So answer is 0. Which is correct.

So the formula seems to hold.

But what if M is zero? For example, x_i=3, a=1, b=10. Then M =3*1//10=0. So w must be ceil(0*10 /1 )=0. So the answer is 3-0=3. But then, the maximum possible money is zero. If he gives 0 tokens, he gets zero, which is the maximum possible. So he can save all 3 tokens, which is correct. But wait, in that case, even if he gives 0 tokens, he gets zero. So the answer is 3-0=3. Which is correct.

So, the formula is:

For each x_i:

Compute M = (x_i * a) // b.

Then compute w = ceil( (M * b) / a )

The answer is x_i - w.

But how to compute ceil(M*b /a) efficiently, given that M can be up to (1e9 *1e9)/1e9 =1e9, so M*b can be up to (1e9)*(1e9) =1e18, which is manageable.

Wait, but (M *b) can be up to ( (1e9 *1e9) //1e9 ) *1e9 → (1e9)*1e9 =1e18. So M*b can be 1e18.

So in Python, integers can handle that.

Now, to compute ceil( (M*b) /a ), when M*b and a are large numbers.

But how to compute this in code.

In Python, we can compute it as (M*b +a -1) //a.

Yes. Because:

ceil(p/q) = (p + q-1) // q.

So here, p is M*b, q is a.

So ceil( (M*b) /a ) is (M*b +a -1) //a.

So the steps for each x_i:

1. Compute M = (x_i *a) // b.

   Because x_i can be up to 1e9, a up to 1e9: x_i *a can be up to 1e18, but Python handles that.

2. Compute w = (M*b +a -1) //a.

3. The answer is x_i -w.

But wait, what if w exceeds x_i? Then this would give a negative answer. But according to the problem statement, the answer can't be negative. So how can that happen?

Wait, M is (x_i *a)//b. Then x_i *a >= M*b → x_i >= (M*b)/a. So (M*b)/a <=x_i. So when we compute ceil( (M*b)/a ), that would be the minimal w that is >= (M*b)/a. Since (M*b)/a <=x_i, then ceil( (M*b)/a ) could be up to x_i.

For example, if (M*b) is exactly divisible by a, then (M*b)/a =x_i. Then ceil is x_i. So w is x_i. Answer is zero.

If (M*b) is not divisible by a, then (M*b)/a is a fractional value less than x_i. So ceil( (M*b)/a ) could be less than or equal to x_i.

Wait, for example, M=3, a=4, b=5. Then (M*b) is 15. 15 /4=3.75. Ceil is 4. So w is 4. Suppose x_i is 5. Then 4 <=5, so answer is 5-4=1.

But how can we be sure that w <=x_i?

Since M is (x_i *a) //b, then x_i *a >= M*b → x_i >= (M*b)/a.

But since (M*b)/a <=x_i, then ceil( (M*b)/a ) is the smallest integer >= (M*b)/a. So this value could be <=x_i.

Wait, but suppose x_i = (M*b)/a. For example, x_i=3, a=3, b=3. Then M=3*3//3=3. Then (M*b)/a = (3*3)/3=3 → ceil is 3. w=3. x_i is 3, so 3-3=0.

Another example: x_i=5, a=4, b=5. M= (5*4)//5=4. So M=4. (4*5)/4=5. So ceil is 5. x_i is 5. So answer is 5-5=0.

But if x_i is 6, a=4, b=5. Then M= (6*4)/5=24/5=4.8 → floor is 4. So M=4. Then (4*5)/4=5. So w=5. x_i is 6. So 6-5=1.

So in all cases, w is <=x_i.

So the formula works.

So the code for each x_i is:

M = (x_i *a) //b

w = (M *b +a -1) //a

ans = x_i -w

But wait, when M is zero, then:

M=0. So w = (0 +a-1)//a = (a-1)//a =0.

So ans =x_i -0 =x_i.

But when M is zero, the maximum floor is zero. So the minimal w is zero, which gives floor(0) =0, which is the maximum. So the answer is x_i -0 =x_i, which is correct.

Wait, but in that case, the maximum possible money is zero. So giving zero tokens would give zero, and the worker can save all x_i tokens. Which is allowed.

For example, in the third example in the problem statement: x_i=1, a=1, b=1. Then M=(1*1)//1=1. So w=(1*1 +1-1)//1 =1. So answer is 1-1=0. Which matches the sample.

So this formula seems to be correct.

So the plan is: for each x_i in the list, compute M as (x_i*a)//b, then compute w as (M*b +a-1) //a, then subtract from x_i.

So the code can be written as follows:

Read n, a, b.

Read the list of x's.

For each x in the list:

   M = (x*a) //b

   w = (M*b +a -1) //a

   ans = x -w

   append ans to the list.

Then output all answers space-separated.

But wait, in Python, for big numbers, this should work as integer operations are handled correctly.

But let's check the sample input.

Sample input 1:

5 1 4

12 6 11 9 1

Sample output: 0 2 3 1 1

Let's compute for x=12:

M=(12*1)/4=3.

w=(3*4 +1-1)/1 → (12 +0)/1 =12. ans=0.

x=6: M=6*1//4=1. (1*4 +1-1)/1 =4. 6-4=2.

x=11: M=11*1//4=2. (2*4 +1-1)/1= (8+0)/1=8. 11-8=3.

x=9: M=9*1//4=2. w=8. 9-8=1.

x=1: M=1*1//4=0. (0*4 +1-1)/1=0. 1-0=1. So output is 1. Which matches the sample.

Another sample input:

3 1 2

1 2 3.

Sample output: 1 0 1.

For x=1:

M=(1*1)//2=0. w=(0*2+1-1)/1 → (0 +0)/1=0. ans=1-0=1.

x=2: M=2//2=1. w= (1*2 +1-1)/1 → (2+0)/1=2. ans=2-2=0.

x=3: M=3//2=1. w=(2+0)/1=2. 3-2=1.

Which matches the sample.

Third sample:

1 1 1

1.

M=1*1//1=1. w=(1*1 +1-1)/1=1. ans=0.

Which matches.

So the code seems correct.

Now, the problem constraints are n up to 1e5. So we need to process 1e5 elements. This approach is O(n), which is acceptable.

In Python, reading the input as a list, then processing each element and appending to a list, then joining into a string and printing, that's all O(n) time.

So the code can be written as:

Read n, a, b.

Read x list.

Compute for each x in the list:

   M = (x * a) //b

   w = (M * b + a -1) //a

   ans = x -w

   add to answers.

Print the answers as space-separated.

So the code is straightforward.

Now, the code must read from standard input and output to standard output.

In Python, for efficiency, when reading a large list, it's better to read the entire line and split into integers.

So, the code would be:

import sys

n, a, b = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
ans = []
for xi in x:
    M = (xi * a) // b
    w = (M * b + a -1) // a
    ans.append(str(xi - w))
print(' '.join(ans))

Yes, that's the code. Let's test with the samples.

Sample 1:

After reading, the x list is [12,6,11,9,1].

Processing each:

12: M=12*1//4=3. w=(3*4 +1-1)/1=12. 12-12=0.

6: M=6*1//4=1. w=(4 +0)/1=4. 6-4=2.

11: M=11*1//4=2. w=(8+0)/1=8. 11-8=3.

9: M=9//4=2. w=8. 9-8=1.

1: M=0. w=0. 1-0=1.

So output is 0 2 3 1 1. Correct.

Another sample:

3 1 2. x = [1,2,3].

For x=1: M=0. w=0. 1-0=1.

x=2: M=1. w=2. 0.

x=3: M=1. w=2. 3-2=1. Output 1 0 1.

Third sample: output 0. Correct.

So this code should work.

Now, about the constraints. n can be 1e5, which is manageable. The code is O(n), which is acceptable for Python.

In terms of memory, the list 'ans' will contain 1e5 strings, which is manageable.

So this code should pass all test cases.
</think>

```python
import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    res = []
    for xi in x:
        m = (xi * a) // b
        w = (m * b + a - 1) // a
        res.append(str(xi - w))
    print(' '.join(res))

if __name__ == "__main__":
    main()
```