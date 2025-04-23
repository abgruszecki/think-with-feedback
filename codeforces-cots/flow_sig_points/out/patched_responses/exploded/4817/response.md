<think>
Okay, let's see. The problem is to find the minimal number of lab works Vasya needs to redo so that his average is at least 4.5 when rounded in his favor. Hmm. So, the key here is understanding how the average is calculated and what the minimal steps are to reach that threshold.

First, let's think about the current average. The average is the sum of all grades divided by the number of grades. But since we need the average after possible rounding to be 5, the actual average (before rounding) needs to be >=4.5. Because any average equal to or higher than 4.5 will round up to 5. So our target is to make the sum such that sum/n >=4.5.

Wait, no. Wait, the problem says the average is rounded to the nearest integer, rounding in favor of the student. So 4.5 is rounded up to 5, but 4.4 is rounded down to 4. So the condition is that the average must be >=4.5. Because if it's exactly 4.5, it's rounded up, and anything above is also rounded up.

So the sum of the grades after redoing some must be at least 4.5 * n. Because sum >= 4.5 * n → average >=4.5 → rounded to 5.

Wait, but n is an integer. So 4.5 * n is a number that could be a decimal. For example, if n is 3, like the first sample, 4.5 * 3 = 13.5. The sum needs to be at least 13.5.

But sum is an integer since all grades are integers. Wait, the sum is the sum of the grades. Each grade is an integer, so the sum is an integer. So 4.5 *n might be a non-integer. So for example, in the first sample, 3 grades: the required sum is 13.5. But sum must be an integer. So the sum must be >=14 (since 13.5 is not possible, but sum must be an integer). Wait, no. Wait 13.5 is the threshold. So sum must be >=13.5. Since sum is an integer, the minimal sum is 14. Because 14 is the first integer greater than or equal to 13.5.

Wait, but 13.5 is exactly 4.5 *3. So the sum needs to be >=13.5. But sum can't be a fraction. So yes, sum needs to be at least 14. So the required condition is sum >= ceil(4.5 * n - 1e-9) ? Wait, maybe not. Let's see.

Let's compute 4.5 * n. If this is an integer, then sum must be at least that. For example, if n=4, 4.5*4=18. So sum must be >=18. Which gives an average of 4.5, which rounds up. If 4.5*n is not an integer, like n=3 (13.5), sum must be 14. So yes, the minimal sum required is the ceiling of 4.5 * n. Because if 4.5 *n is integer, then sum >=4.5n is sum >= that integer. If it's not, then sum is the next integer.

So the target sum S is ceil(4.5 *n). But how to compute that in code?

Alternatively, since the sum is the sum of grades after converting some to 5, we can compute the current sum, then see how much more we need.

So initial_sum = sum of current grades.

We need initial_sum + delta >= 4.5 *n.

delta is the total increase we can get by converting some grades to 5.

Each time we redo a grade, the maximum possible increase is (5 - original grade). Because, for example, if the original grade is 4, converting to 5 gives +1. If it's 3, converting gives +2, etc.

So the problem reduces to selecting the minimal number of grades to convert (each to 5) such that the sum of their increases (5 - original) plus the initial_sum is >= 4.5 *n.

But how to calculate this.

Let me outline the steps:

1. Compute the current sum of grades.

2. Compute the required sum S = ceil(4.5 * n). Wait, but how to compute this in code.

Wait, 4.5 *n can be represented as (9n)/2. So if n is even, 9n is even, so 9n/2 is an integer. If n is odd, then 9n is odd, so 9n/2 is 4.5n, which is a .5.

So S is the minimal sum required, which is (9n +1 )//2. Because:

If n is even: 9n is even. (9n)/2 is an integer. So 9n/2 is S. For example, n=4: 9*4=36/2=18. So sum >=18.

If n is odd: 9n is odd. For example, n=3: 9*3=27 → 27/2 =13.5. So sum needs to be >=14. So (27 +1)/2 =14. So for n=3, (9*3 +1)/2 =28/2=14.

So in code, S can be calculated as (9*n +1) // 2. Because:

For even n: 9n is even. (9n +1) is odd. When divided by 2, integer division, but 9n+1 divided by 2 is 4.5n + 0.5. Wait, no. Wait for even n:

Let's take n=4. 9*4=36. (36 +1) =37. 37//2=18.5 → but integer division in Python is floor. So 37//2=18. Which is correct for S=18.

Wait, that's the same as 9*4//2 =36//2=18. So for even n, (9n +1)//2 is the same as (9n)//2 + 0.5, but since 9n is even, adding 1 and then dividing by 2 gives (even +1)/2 = (even/2) + 0.5, but when using integer division, this would be (even +1) // 2 = even//2 + 0.5 is not an integer. Wait, this seems conflicting. Wait, maybe I made a mistake here.

Wait, let's recalculate:

n=4 (even):

9n=36. 4.5n is 18. So required sum is 18. So (9n +1)/2 = (37)/2=18.5, but in integer division, 37//2=18. Hmm, that's 18.5 rounded down to 18, which is correct. Because 18 is exactly 4.5*4. So the sum must be >=18. So 18 is the required sum.

Wait, (9n +1) //2 for even n gives (36 +1)/2 =37//2=18. Which is correct.

For odd n=3: (9*3 +1)/2=28/2=14. Which is correct.

So yes, the required sum S can be computed as (9*n +1) // 2. So this formula works for both even and odd n.

So the steps:

Compute current_sum = sum of the array.

If current_sum >= S: then output 0.

Else, compute the deficit = S - current_sum.

We need to find the minimal number of grades to change, each contributing (5 - original_grade) to the sum. The sum of these contributions must be >= deficit.

We need to choose the largest possible increments first to minimize the count. So the algorithm is:

Sort the original grades in ascending order. For each grade, compute (5 - grade). But since we can only convert a grade once, and the best strategy is to pick the ones that give the maximum possible increase first.

Wait, but the array's elements are the original grades. So for example, if grades are [2,3,4], the possible increments are 3, 2, 1. So if the deficit is 4, then we can take 3 +1 (two steps) instead of 2+2 (two steps). So yes, the optimal is to take the largest increments first.

So the approach is:

Sort the list of possible increments (5 - grade) in descending order. Then accumulate them until the sum reaches or exceeds the deficit. The number of steps needed is the minimal count.

But wait, the possible increments are (5 - grade) for each grade. However, since Vasya can choose to redo a lab work, which changes its grade to 5. So the possible increment is (5 - original_grade). But for example, if the original grade is 5, the increment is 0, so there's no point in redoing those. So we can ignore those.

So the steps:

1. Compute current_sum and required_sum S = (9n +1) //2.

If current_sum >= S → output 0.

Else:

2. Compute the deficit = S - current_sum.

3. For each grade in the list, compute (5 - grade). Collect all possible increments where (5 - grade) >0. Because if the grade is 5, no change. For others, the possible gain is (5 - grade).

Sort these possible gains in descending order.

4. Iterate through the sorted gains, adding each to a total until the total >= deficit. The number of gains added is the answer.

So for example, in the first sample:

Input 3

4 4 4 → sum is 12. S is (9*3 +1)/2 →28//2=14. Deficit is 2.

Possible gains are (5-4=1) for each of the 3. So sorted gains [1,1,1].

To get deficit 2: take two of them. So answer is 2.

Another example: input 5 3 3 5.

Original sum: 5+3+3+5=16. n=4. S= (9*4 +1)/2= (37)/2=18.5 → no, wait. Wait 9*4=36, 36+1=37, divided by 2 is 18.5, but integer division in Python would be 18.5 → no, wait wait. Wait 37 divided by 2 is 18.5, but integer division (//) in Python truncates towards negative infinity. So 37//2 is 18. So required sum is 18.

Original sum is 16. deficit is 18-16=2.

Possible gains are for the two 3's: 5-3=2 each. So sorted gains [2,2]. So sum 2 (one gain) is enough. So answer is 1.

Yes, which matches the third sample.

So the algorithm seems correct.

Now, how to implement this.

In code:

Read n.

Read the list of grades.

Compute current_sum = sum(grades).

Compute S = (9 *n +1) // 2.

if current_sum >= S: print 0.

else:

Compute deficit = S - current_sum.

Compute the possible gains: [5 - x for x in grades if 5 -x >0]. Because only these can contribute.

Sort gains in descending order.

Then iterate through the gains, adding to a running total, count how many needed until the total >= deficit.

If no gains (but deficit is positive, but according to the problem statement, it's guaranteed that Vasya can reach the required sum by redoing enough lab works. So in practice, gains will exist if deficit is positive.)

So code steps.

Now, code in Python.

But since n can be up to 100, even O(n log n) is acceptable.

So code:

n = int(input())
grades = list(map(int, input().split()))
current_sum = sum(grades)
required = (9 * n + 1) // 2

if current_sum >= required:
    print(0)
else:
    deficit = required - current_sum
    gains = [5 - g for g in grades if 5 - g > 0]
    gains.sort(reverse=True)
    count = 0
    total = 0
    for gain in gains:
        total += gain
        count +=1
        if total >= deficit:
            print(count)
            exit()
    # According to the problem statement, it's guaranteed that a solution exists.
    # So this loop will always find a count.

But wait, in the case where all gains are zero? Like if all grades are 5. Then required sum is (9n+1)//2. But sum is 5n. Let's see for n=1: required sum is (9+1)/2=5. So 5 >=5. So output 0. So in the code, if current_sum is 5, which is equal to required, which is 5, then the code outputs 0. So that's correct.

So this code should handle all cases.

Testing the first sample:

Input 3, [4,4,4].

current_sum=12. required =14.

deficit=2.

gains are [1,1,1]. sorted descending.

loop:

gain=1: total=1, count=1. 1 <2.

gain=1: total=2, count=2. which meets deficit. So output 2. Correct.

Third sample:

grades [5,3,3,5]. sum is 16. required 18. deficit 2.

gains are [2,2]. sorted as [2,2]. take first gain: 2 >=2 → count=1.

So output 1. Correct.

Second sample:

grades [5,4,5,5]. sum is 5+4+5+5=19. required is (9*4+1)//2= (37)//2=18. 19 >=18 → output 0. Correct.

Another test case where deficit requires more than one gain.

Sample: input 5, [2,2,2,2,2]. sum=10. required is (9*5 +1)/2= (46)/2=23. deficit=13.

Each gain is 3 (5-2=3). sorted as [3,3,3,3,3].

We need 13. Each gives 3. 3*4=12, 3*5=15. So 5 steps. Because 4 steps give 12, which is <13. So fifth step needed. So answer is 5. Because 5*3=15 >=13.

So code would loop through gains:

total after 4 steps: 4*3=12. deficit is 13. Not enough. Add fifth step: total 15 >=13 → count=5.

So code outputs 5.

Yes.

Thus, the code should work correctly.
</think>

```python
n = int(input())
grades = list(map(int, input().split()))
current_sum = sum(grades)
required = (9 * n + 1) // 2

if current_sum >= required:
    print(0)
else:
    deficit = required - current_sum
    gains = [5 - g for g in grades if 5 - g > 0]
    gains.sort(reverse=True)
    total = 0
    count = 0
    for gain in gains:
        total += gain
        count += 1
        if total >= deficit:
            print(count)
            break
```