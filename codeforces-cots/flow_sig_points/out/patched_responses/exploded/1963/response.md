<think>
Okay, let's see. The problem is Jack wants to reach a certain point x on the number line by jumping. The first jump is 1 unit, then each subsequent jump increases by 1 unit. He can choose to jump left or right each time. We need to find the minimal number of jumps needed to exactly reach x.

Hmm. So, the key points here are:

- The sum of the jumps (with signs) must equal x.
- We need the smallest number of jumps possible.

First, let's think about the sum of the first n jumps. If all jumps are in the positive direction, the sum is 1 + 2 + ... + n = n(n+1)/2. Let's call this S(n). So S(n) is the maximum possible sum after n jumps.

If x is 0, the answer is 0. That's straightforward.

For other x, we need to find the smallest n where S(n) >= |x| (since direction can be adjusted), and then check if (S(n) - |x|) is even. Because the difference between the maximum sum and x must be even. Because changing the direction of a jump of length k changes the total sum by 2k. So, the parity of the difference must be even.

Wait, right. Because suppose the sum is S(n). If we reverse the direction of a jump of size k, the total sum becomes S(n) - 2k. So, the difference between S(n) and the target x must be even. Or wait, the target is |x| here. Because we can flip directions to reach either x or -x, but since x can be negative, taking absolute value first makes sense. Because the problem says Jack is at zero and wants to reach x. So, x can be positive or negative. But since the jumps can be in any direction, the minimal steps to reach x is the same as reaching |x|, because you can just flip all directions if x was negative. So, we can just consider x as its absolute value.

So, the approach should be:

1. Take absolute value of x. Let's call it target.

2. Find the smallest n such that S(n) >= target, and (S(n) - target) is even.

Because:

- If S(n) is exactly equal to target, then n is the answer.

- If S(n) is greater than target, but the difference is even, we can flip some jump direction(s) to subtract twice the sum of some jumps. So, flipping a jump of size k would reduce the total by 2k. So, the difference (S(n) - target) must be even. So, the problem reduces to finding the smallest n where S(n) >= target and (S(n) - target) is even.

So the steps are:

- Compute target = abs(x).

- If target is 0, return 0.

Else:

Find the smallest n where S(n) >= target and (S(n) - target) is even.

How to compute n?

We can start by finding the smallest n where S(n) >= target. Then check if the difference is even. If yes, return n. If not, check n+1. If that's still not even, then check n+2. Because adding two steps would change the sum by (n+1) + (n+2), but wait, the difference between S(n+2) and S(n) is (n+1) + (n+2) = 2n+3. Wait, but the parity of the sum.

Wait, S(n) is the sum from 1 to n.

Let's see, for example:

If S(n) is sum up to n. Let's compute S(n) mod 2.

Sum 1 to n is n(n+1)/2. So mod 2, this depends on n mod 4.

Wait, perhaps there's a pattern here.

But maybe it's easier to approach this step by step.

Once we find the minimal n where S(n) >= target, then:

If (S(n) - target) is even, return n.

Else, check n+1. Because S(n+1) = S(n) + (n+1). The difference here would be (S(n) + (n+1) - target). Let's see:

If original difference was d = S(n) - target. If d is odd, then adding (n+1) to S(n), the new difference is d + (n+1). So (d + (n+1)) mod 2 = (odd + (n+1)) mod 2.

But d is odd. So (odd + (n+1)) mod 2 is (1 + (n+1 mod 2)) mod 2.

Hmm. But perhaps this is not the right way. Let's think of possible cases.

Case 1: After n steps, sum S(n) >= target. Let d = S(n) - target. If d is even, done.

If d is odd:

We need to find the next n where S(n) - target is even. So:

If n+1 steps: S(n+1) = S(n) + n+1. The new d is d + (n+1). So (d + (n+1)) mod 2. Since d was odd, adding (n+1) could make it even or odd again.

For example, if n+1 is even, then adding even to odd d gives odd. If n+1 is odd, adding to odd gives even.

So, if d is odd, then:

If (n+1) is even, then (d + (n+1)) is even + odd (since d is odd, n+1 even, so sum is odd + even = odd). So S(n+1) - target is even? Wait, original d was S(n) - target = odd. Then S(n+1) - target is d + (n+1). So if (n+1) is even, then (d + even) is odd + even = odd. So it's still odd. So that's not helpful.

Wait, let's take an example.

Suppose target is 2. The sample input. Then S(2) is 3. So S(2) - target is 1, which is odd. So the initial n is 2. But since d is odd, we need to check next n.

But in the sample input, the correct answer is 3. Let's see:

n=3, S(3) =6. S(3) -2=4, which is even. So 3 steps. That's correct.

So in the case where initial d is odd, adding steps until the difference becomes even.

But how?

Let me think. For the first n where S(n) >= target:

If (S(n) - target) is even: return n.

If not, then check n+1. If (S(n+1) - target) is even, return n+1.

If not, check n+2. Because adding two steps, S(n+2) = S(n) + (n+1) + (n+2) = S(n) + 2n +3. The difference would be d + 2n +3. Since d is odd (original difference), 2n is even, 3 is odd. So d + 2n+3 = (d +3) + 2n. Since d is odd, d+3 is even. 2n is even. So overall even. So d+2n+3 is even. So in this case, n+2 steps would have even difference.

So in the case where initial n gives an odd difference, the next possible steps are n+1 or n+2.

Wait, let's see:

When d is odd.

If we add one step (n+1):

The new difference is d + (n+1).

If (n+1) is even, then d (odd) + even is odd. So difference is odd again.

If (n+1) is odd, then d + odd = even. So difference is even. So if (n+1) is odd, adding one step would solve the problem.

So, in the case where initial n has d odd:

Check if (n+1) is odd. If yes, then return n+1. Else, return n+2.

Wait, but how to determine that.

Let's take some examples.

Example 1: target=2.

Initial n is 2 (sum 3, which is >=2). d=1, odd.

Check n+1=3. Sum is 6, d=4, even. So return 3.

Another example: target=5.

The sum S(3) is 6, d=1. Odd.

n=3, d=1. Then check n+1=4. Sum is 10. d=5, which is odd. So not even. So then check n+2=5. Sum is 15. d=10, even. So return 5.

Wait, but that's not optimal. Wait, is there a better n?

Wait, for target=5.

Wait, let's see:

n=3: sum 6. difference 1. odd.

n=4: sum 10. difference 5. odd.

n=5: sum 15. difference 10. even. So answer is 5. But can we find a smaller n?

Wait, what about n=4. But difference is 5, which is odd. So no.

Hmm. But maybe there's a way with n=5 steps. So why would that be the case?

Alternatively, maybe there's a way to reach 5 in 5 steps. Let's see:

Each step can be + or -.

Sum after 5 steps is 15. We need to reach 5. So 15 - 2k =5 → 2k=10 → k=5. So we need to reverse a jump of 5. So steps: 1+2+3+4-5=5. That's 5 steps. So yes.

But wait, 1+2+3+4-5 = 5. So that's correct. So answer is 5.

So the algorithm works here.

Another example: target=4.

Find the minimal n where S(n) >=4.

n=3: sum 6. difference 2 (even). So return 3.

Yes: 1+2+3 =6. But how to get 4? 1+2-3=0. No. Wait, wait. Maybe 1+2+3 - something else?

Wait, maybe 3 steps: 1+2+3=6. To reach 4, the difference is 2. So 6-2=4. So need to flip a jump of 1, since 2=2*1. So 1+2+3 becomes -1+2+3 =4. So yes. So answer is 3.

So the algorithm works.

Another example: target=7.

Find S(n) >=7. S(4) =10. d=3. odd. So check n+1=5. sum=15. d=8. even. So return 5.

But 5 steps: sum 15. need to reach 7. 15-7=8. So 8/2=4. So flip a jump of 4. So 1+2+3-4+5=7. Yes. So 5 steps.

But what about n=4? sum 10. d=3. odd. So need to check n+1=5, which gives even difference.

So the algorithm works.

Another example: target=8.

S(4) is 10. difference is 2, even. So return 4.

Yes: 1+2+3+4=10. But we need 8. So 10-2=8. 2=2*1. So flip 1. So -1 +2+3+4=8. So yes. 4 steps.

So the algorithm works.

So the steps are:

1. Compute target = abs(x). If target is 0, return 0.

2. Find the minimal n where S(n) >= target, and (S(n) - target) is even.

3. To find n, we can start by finding the smallest n where S(n) >= target. Then check if the difference is even. If yes, done. If not, check n+1 and n+2.

But how to find the initial n?

The sum S(n) = n*(n+1)/2 >= target.

We can solve for n using quadratic formula. Let's rearrange:

n^2 +n - 2*target >=0.

The roots of the equation n^2 +n -2t =0 are [-1 ± sqrt(1 +8t)]/2. We take the positive root. So n >= [sqrt(8t +1) -1]/2.

So the minimal n is the ceiling of [sqrt(8t +1) -1]/2.

But since t can be up to 1e9, we need an efficient way to compute this.

But in Python, we can compute this using math.sqrt. Let's see.

For example, for target=2:

8t+1=17. sqrt(17)=~4.123. 4.123-1=3.123. Divided by 2 is ~1.561. Ceiling is 2. Which is correct.

For target=6: 8*6+1=49. sqrt is 7. 7-1=6. 6/2=3. Ceiling is 3. Correct.

So the initial n can be found by calculating the ceiling of (sqrt(8t +1) -1)/2).

Once n is found, check if S(n) - target is even.

If yes, return n.

Else, check n+1. Then check if S(n+1) - target is even. If yes, return n+1.

Else, return n+2.

Wait, but why n+2?

Because when S(n) is the first sum >= target, and n+1 gives sum S(n+1) = S(n)+n+1.

If S(n) - target is odd, and (n+1) is even, then S(n+1) - target = (S(n) - target) + (n+1). So adding an even number to an odd gives odd again. Then n+2 steps would give sum S(n+2) = S(n) + (n+1) + (n+2) = S(n) + 2n +3. So the difference becomes (S(n) - target) + 2n+3. Since 2n is even and 3 is odd, 2n+3 is odd. So adding to the original odd difference (S(n)-target is odd) gives (odd + odd) = even. So the difference is even. Therefore, n+2 steps would work.

But why can't n+1 steps work?

Because if (n+1) is odd, then S(n+1)-target would be (S(n)-target) + (n+1). Which is (odd) + (odd) = even. So if (n+1) is odd, then n+1 steps would work.

So the logic is:

After finding initial n:

If (S(n) - target) is even → return n.

Else:

If (n+1) is odd → return n+1.

Else → return n+2.

Wait, but how to determine when (n+1) is odd. Let's see.

Let's think in terms of parity.

Case 1: initial n's sum S(n) >= target. Difference d is odd.

We need to find the smallest m >=n where S(m) - target is even.

So m can be n, n+1, or n+2.

Wait, but m has to be >=n. Since n is the minimal for S(m) >= target.

Wait, but when m increases, S(m) increases. So S(n) >= target, and S(n+1) = S(n) + (n+1) >= S(n) >= target.

So for m >=n, S(m) >= target.

So, the possible candidates are n, n+1, n+2.

But in the initial check, n is the minimal such that S(n) >= target. So for m <n, S(m) < target. So the only possible candidates are n, n+1, n+2.

But in the case where the difference is odd, we have to check n+1 and n+2.

So the algorithm becomes:

Compute initial n where S(n) >= target.

Check if d = S(n) - target is even. If yes → return n.

Else:

Check if (S(n+1) - target) is even. If yes → return n+1.

Else → return n+2.

But how do these cases work?

Because:

If d is odd, then:

Case 1: (n+1) is even. Then adding (n+1) (even) to d (odd) → sum becomes d + even = odd. So S(n+1) - target is odd. So then check n+2.

Case 2: (n+1) is odd. Then adding (n+1) (odd) to d (odd) → sum becomes even. So S(n+1)-target is even. So return n+1.

So in code, after computing initial n, and finding that d is odd:

if (n+1) is odd → return n+1.

else, return n+2.

Because:

If (n+1) is odd → adding it to d (odd) gives even → return n+1.

If (n+1) is even → adding it gives odd → need to add two steps. But adding two steps (n+1 and n+2) will add (n+1) + (n+2) = 2n +3. 2n is even, 3 is odd → sum added is even + odd = odd. So d + (2n+3) = odd + odd = even. So in this case, n+2 steps will have even difference.

But wait, wait. Let's re-express S(n+2) - target.

S(n+2) = S(n) + (n+1) + (n+2) = S(n) + 2n+3.

So S(n+2) - target = (S(n) - target) + 2n+3 = d + 2n +3.

Since d is odd, 2n is even, 3 is odd. So overall, d + even + odd = odd + odd = even. So yes.

So in this case, n+2 steps will give even difference.

So the code can be written as:

Compute initial n.

d = S(n) - target.

if d % 2 ==0: return n.

else:

   if (n+1) % 2 ==1: return n+1.

   else: return n+2.

Wait, but how to compute S(n) ?

But in code, perhaps it's easier to compute n by iterating until S(n) >= target, but for large target (like 1e9), that would be O(sqrt(target)) steps, which is acceptable since sqrt(1e9) is 3e4 steps.

But using the formula for n is better.

So steps:

1. Compute target = abs(x). if target ==0: return 0.

2. Compute n as the smallest integer where S(n) >= target.

   n can be found via the formula:

   n = ceil( (sqrt(8*target +1) -1)/2 )

3. Compute S(n) as n*(n+1)//2.

4. Check if (S(n) - target) is even. If yes: return n.

5. Else:

   if (n+1) is odd: return n+1.

   else: return n+2.

Wait, but why not compute S(n+1) and check (S(n+1)-target) mod 2 ?

But in code, for very large n, calculating S(n) is O(1) using the formula.

So the code would look something like:

import math

x = int(input())

target = abs(x)

if target ==0:

    print(0)

else:

    n = math.ceil( (math.sqrt(8 * target +1) -1)/2 )

    s = n*(n+1)//2

    if (s - target) %2 ==0:

        print(n)

    else:

        if (n+1) %2 ==1:

            print(n+1)

        else:

            print(n+2)

But wait, let's test some examples.

Sample input 2:

target=2.

n is computed as (sqrt(17)-1)/2. sqrt(17) is ~4.123. (4.123-1)/2 ~1.56. ceil is 2. S(2) =3. 3-2=1 (odd). So else block. (n+1) is 3, which is odd. So return 3. Correct.

Sample input 6: target=6.

n is (sqrt(49)-1)/2 = (7-1)/2 =3. ceil(3) is 3. S(3)=6. 6-6=0 even. return 3. Correct.

Another example: target=5.

n is (sqrt(41)-1)/2. sqrt(41) is ~6.403. (6.403-1)/2 ~2.701. ceil is 3. S(3)=6. 6-5=1 (odd). (n+1)=4, which is even. So return n+2=5.

Yes.

Another example: target=7.

n: 8*7 +1=57. sqrt(57)=~7.549. (7.549-1)/2=3.2745. ceil is 4. S(4)=10. 10-7=3 (odd). n+1=5, which is odd. So return 5. Which is correct.

Another example: target=1.

n=1. S=1. 1-1=0 even. return 1. Correct.

target=3.

n=2. S=3. 3-3=0 even. return 2. Which is correct (1+2=3).

target=4.

n=3 (sqrt(33)=5.744. (5.744-1)/2=2.372, ceil 3). S(3)=6. 6-4=2 even. return 3.

Yes.

Another example: target=11.

n: 8*11+1=89. sqrt(89)=~9.433. (9.433-1)/2=4.216 → ceil 5. S(5)=15. 15-11=4 even. So return 5. Which is correct. 1+2+3+4+5=15. Reverse a jump of 2 → 15-4=11. So -1+2 → sum is 1, then +3+4+5 → 1+3+4+5=13? Wait, no. Wait, the steps would be -1+2+3+4+5 =13. Hmm, that's 13. Wait, maybe another combination.

Wait, 15-4=11. So need to subtract 4. Which is 2*2. So reverse the 2. So 1-2+3+4+5 = (1-2)+(3+4+5) = (-1) +12=11. Yes. So 5 steps. Correct.

So the code works.

So the code seems correct.

Now, what about x=0? Then output is 0.

Another edge case: x=1. Output 1.

x=10^9: compute n as per formula.

What about x=1e9?

target=1e9.

n is computed as (sqrt(8*1e9 +1) -1)/2. Let's compute:

8e9 +1 =8000000001. sqrt of that is 89442.7... Wait, no. Wait, sqrt(8e9) is sqrt(8)*1e4.5. 8e9 is 8,000,000,000.

But for code, the math.sqrt in Python can handle it.

But let's see, the code would compute n correctly.

So the code should handle all cases efficiently.

Now, the code must read input, compute target, and output the answer.

In terms of time constraints, even for x=1e9, the code runs in O(1) time. So no problem with time limits.

Memory is also not an issue.

So the code should be correct.
</think>

```python
import math

x = int(input())
target = abs(x)
if target == 0:
    print(0)
else:
    n = math.ceil((math.sqrt(8 * target + 1) - 1) / 2)
    s = n * (n + 1) // 2
    if (s - target) % 2 == 0:
        print(n)
    else:
        if (n + 1) % 2 == 1:
            print(n + 1)
        else:
            print(n + 2)
```