<think>
Okay, let's try to figure out this problem. The task is to find the maximum possible sum of a sequence of numbers that starts with n and ends with 1, where each subsequent number is a divisor of the previous one (since after arranging into a rows of b, we take b as the next step, but a must be greater than 1). Also, each step must be strictly decreasing. So, for each ci (except 1), we need to choose a divisor of ci that is as large as possible, but not equal to ci itself. Wait, no. Because the arrangement is such that ci+1 is a factor of ci. Because a * b = ci, and then ci+1 is b, which is ci divided by a. So a must be a divisor of ci greater than 1. So for each step, we can split ci into a * b where a>1, and then take b as the next step. So ci+1 = b = ci / a, where a is a divisor of ci (since a must divide ci exactly, because all pebbles are used). 

The goal is to choose, at each step, the split (a) such that the sum of all the ci's is maximized. The sum includes all the ci's from c1 down to ck=1.

So the problem reduces to finding a path from n down to 1, where each step is a division by some a>1 (so the next term is ci/a, which must be an integer), and the sum of all the terms along the path is maximized.

This seems like a dynamic programming problem. For each number x, the maximum sum is x plus the maximum sum of the next step. The base case is when x is 1, which contributes 0 (but since the sequence ends with 1, the sum would have included 1 already). Wait, wait. The sum includes all the terms, including 1. So for x=1, the sum is 1, but since it's the end of the sequence, there are no more steps. So the base case is when x is 1, return 1. But wait, in the examples, for the first example:

n=10, and the path is 10 ->5 ->1. Sum is 10+5+1=16. So for x=5, the sum would be 5 + (sum for 1) =5+1=6. So the recursion would be sum(x) = x + max(sum(x / a)), where a is a divisor of x greater than 1. Wait, no. Because the next step is x / a, which is equal to b. So for each x, the possible next steps are all possible b's such that there exists a>1 where a*b = x. Then, sum(x) is x plus the maximum sum of all possible b's.

But how to compute this efficiently for large x (up to 1e9)? Because for each x, we need to check all possible a>1 divisors of x, compute x/a, and then recursively compute sum for that.

But using a recursive approach would be too slow for x up to 1e9. So we need a memoization approach combined with factorization.

Alternatively, perhaps there's a pattern here. Let's think about how to maximize the sum. To get the maximum sum, we need to choose the next term as large as possible. But that's not necessarily the case. For example, perhaps taking a smaller next term could allow for more steps, leading to a larger total sum. For example, consider n=8. The sample output is 15. Let's see: 8 splits into 4 (split into 2 rows of 4). Then 4 splits into 2 (split into 2 rows of 2). Then 2 splits into 1 (split into 2 rows of 1). So sum is 8+4+2+1=15. Alternatively, if 8 splits into 8/2=4, which is same as above. Another option is split into a=4, so 8/4=2, then 2 splits into 1. Sum is 8+2+1=11. So the first path gives a better sum.

Wait, so splitting into the largest possible next term (like 4) is better. But in the first example, 10 splits into 5 (the largest possible) then 5 splits into 1. Sum is 10+5+1=16. Alternatively, splitting 10 into 2 (so next term is 5, same as before). So the path is same. So choosing the largest possible next term (which is the largest possible divisor of x) might be the optimal approach. But how?

Wait, the largest possible next term would be when a is as small as possible. Because a must be at least 2, so the largest possible next term is when a is 2, which gives b = x/2. But that's only if x is even. But perhaps that's not the case. For example, let's take x=6. If we split as a=2, then next term is 3. Then 3 can split into a=3, next term 1. Sum is 6+3+1=10. Alternatively, split 6 into a=3 (b=2). Then 2 splits into 1. Sum is 6+2+1=9. So choosing the larger next term (3) gives a better sum. So perhaps the optimal approach is to choose the next term as the largest possible, which would be x/(smallest possible a). Because a must be a divisor of x greater than 1. The smallest possible a is the smallest prime factor of x. Because then, x/a would be the largest possible divisor (since a is the smallest possible, so x/a is the largest possible).

Wait, let's see. Let's take x=12. The factors a>1 are 2, 3, 4, 6, 12. But a must be a divisor of x. So possible a's are 2,3,4,6,12. But for each a, the next term is x/a. So possible next terms are 6 (12/2), 4 (12/3), 3 (12/4), 2 (12/6), 1 (12/12). But a must be greater than 1, so x/a must be less than x. So possible next terms are 6,4,3,2,1, but x/a must be less than x. So a can be any divisor of x greater than 1, and a <= x/1, but a must divide x.

So the possible next terms are all the divisors of x that are less than x. Because a must be >1, so x/a must be a divisor of x, and less than x.

Wait, no. For example, if x=6, possible a's are 2,3,6. Then x/a is 3,2,1. So next terms are 3, 2, or 1. But in the problem statement, each step must have ci+1 < ci. So the next term must be strictly smaller than the current. So the next term must be a proper divisor of x. So for each x>1, the possible next terms are all the divisors of x that are less than x. But how?

Wait, the next term is b = x/a, where a>1 and a divides x. So b must be a divisor of x, since x = a*b. So for x>1, possible next terms are all possible divisors of x that are less than x. Because a can be any divisor of x greater than 1. So for example, x=6, the next terms can be 3 (when a=2), 2 (a=3), 1 (a=6).

So the possible next terms are the divisors of x (other than x itself). But since a must be >1, the next term is x/a, which can be any divisor of x that is less than x. So to get the maximum sum, for each x, we need to choose the next term (d) as a divisor of x, d < x, such that d plus the maximum sum of its sequence is maximized.

But how to compute this efficiently for large x (up to 1e9)? A naive recursive approach would be to memoize each x and compute the sum. However, for x up to 1e9, this is impossible because the memoization table would be too large.

So we need a way to compute the maximum sum without memoizing all possible x's. Let's think about the structure of the problem.

The key insight here is that the optimal path for x is to split x into its prime factors. For example, let's take x=12. Its prime factors are 2^2 *3^1. The optimal sum would be 12 + 6 + 3 +1 = 22. Or 12 +4 +2 +1=19. Or 12+3+1=16. So the first path gives a higher sum. So choosing the largest possible next term each step seems better.

But how to choose which divisor to take?

Another observation: the maximum sum is achieved by choosing the next term as the largest possible divisor of x that is not x itself. Because then, each step contributes the maximum possible value. For example, in x=12, the largest divisor less than 12 is 6. Then for 6, the largest divisor is 3, then 1. Sum is 12+6+3+1=22.

But wait, let's see. For x=8, the largest divisor is 4. Then 4's largest is 2, then 1. Sum is 8+4+2+1=15, which matches the sample. For x=10, the largest divisor is 5. Then 5 can only split into 1. Sum 10+5+1=16. So that's correct.

So if we can always split x into its largest possible divisor (other than x itself), then we can compute the sum by adding x plus the sum of that largest divisor's sum.

But how do we find the largest possible divisor of x (other than x itself)? The largest possible divisor is x/2 if x is even. But that's not the case. For example, x=15. The largest divisor less than 15 is 5 (since 15/3=5). So the largest possible divisor is 5. So for x=15, the next term would be 5, then 5 splits into 1. Sum 15+5+1=21.

Alternatively, if x is prime, then the only possible next term is 1. So sum is x +1.

So the problem reduces to, for each x, if x is prime, then the sum is x +1. Otherwise, the sum is x + sum of the maximum path starting from the largest possible divisor of x (other than x).

But how to find the largest possible divisor of x? The largest divisor is x divided by the smallest prime factor of x. Because, the smallest prime factor (spf) of x is the smallest prime that divides x. So x = spf * k. So k is the largest possible divisor (since spf is the smallest possible, dividing x by it gives the largest possible factor). For example, x=15, spf is 3. So largest divisor is 15/3=5. For x=12, spf is 2. 12/2=6, which is the largest divisor. For x=9, spf is 3. 9/3=3. Which is the largest divisor (since 3 is next, then 1). Sum is 9+3+1=13.

So the optimal strategy is to split x into the largest possible divisor each time, which is x divided by its smallest prime factor.

But how to compute this sum efficiently?

Let me think about the steps for a number x. Let's denote the sum as f(x).

If x is 1, f(x) =1.

If x is prime, then the only possible split is into a=x, which gives next term 1. So f(x) =x +1.

If x is composite, then the largest possible next term is x/spf(x), where spf is the smallest prime factor. So f(x) =x + f(x/spf(x)).

But wait, x/spf(x) may not be prime. For example, x=12, spf is 2, x/spf is 6. Then f(6) is 6 +3 +1=10. So f(12) is 12+6+3+1=22.

But this approach would require us to find the smallest prime factor for x, then recursively compute the sum for x/spf(x). How do we compute this efficiently?

The key is that the smallest prime factor of x can be found quickly, even for large x. For example, for x=1e9, we can check divisibility by primes up to sqrt(x), but that may be time-consuming. Alternatively, for each x, we can check divisibility starting from 2 up to sqrt(x). Once we find a divisor, we take the smallest one, which is the spf.

But for x up to 1e9, checking up to sqrt(x) is O(1e4.5) per number (since sqrt(1e9) is 3e4). So for numbers up to 1e9, this approach is manageable, but if we have to do this for each step in the recursion, the total time may be acceptable.

For example, let's take x=1e9. The spf is 2. Then x/spf is 5e8. Then spf is 2 again, x becomes 25e7. This continues until x becomes 1. So the number of steps is O(log x) in the worst case. For each step, we find the spf by checking divisors up to sqrt(x). But sqrt(1e9) is 3e4, and for each step, the number is divided by 2, so the next x is 5e8, sqrt(5e8) is about 2e4. So for each step, the cost is O(sqrt(x)), which may be expensive for very large x.

So this approach may not be efficient enough for numbers like x=1e18 (but the problem says up to 1e9, which is manageable). Let's see: for x=1e9, the spf is 2. Then x becomes 5e8. spf is 2 again, x becomes 25e7. And so on until x is 5^9, which is 1953125. Then check spf: 5, and so on. For each step, the number of checks is O(sqrt(x)), but for x=1e9, sqrt is 3e4. But in practice, since we stop once we find the first divisor, perhaps it's manageable.

Alternatively, we can optimize the process of finding the smallest prime factor. For a given x, we can check divisibility starting from 2 up to sqrt(x). Once any divisor is found, we take the smallest one, which is the spf. If no divisor is found up to sqrt(x), then x is prime.

So the algorithm for f(x) is as follows:

def f(x):
    if x == 1:
        return 1
    spf = find the smallest prime factor of x
    if spf is x (i.e., x is prime):
        return x + 1
    else:
        return x + f(x // spf)

But wait, when x is not prime, but composite, the largest possible divisor is x//spf. So adding x and then recursively compute f(x//spf).

But let's test this with the sample inputs.

Sample 1: n=10.

10's spf is 2. So next term is 10/2=5. 5 is prime. So sum is 10 + 5 +1 =16. Correct.

Sample 2: n=8.

8's spf is 2. Next term 4. 4's spf is 2. Next term 2. spf is 2. Next term 1. Sum 8+4+2+1=15. Correct.

Another example: n=6.

spf is 2. next term 3. 3 is prime. sum is 6+3+1=10. Which is better than splitting into 3 rows (sum 6+2+1=9). So correct.

Another example: n=12. spf is 2. next term 6. spf 2. next term 3. prime. sum 12+6+3+1=22. Which is correct.

So this approach seems to work. Now, how to implement it efficiently?

The key is to find the smallest prime factor (spf) for a given x quickly. Let's write a helper function to find the spf of x.

For a given x, start checking from 2 up to sqrt(x). The first divisor we find is the smallest possible. If no divisor is found, then x is prime.

So code for spf:

def find_spf(x):
    if x % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return i
    return x  # x is prime

Wait, but for even x, we check 2 first, which is correct. For odd x, check starting from 3, step 2. For example, x=15: check 3 (15 mod3=0), so spf is 3. For x=25: check 3 (25 mod3 is 1, 5 mod5 is 0). So the code would return 5.

This should work.

Once we have the spf, the recursive function can be implemented. But recursion in Python can hit stack limits for large x. For example, if x is a power of 2 (like 2^30), the recursion depth would be 30, which is manageable. But for numbers that are primes, the recursion depth is 1. So stack overflow is not an issue here.

But in Python, recursion for 1e4 steps could be a problem. But since each step reduces x to x/spf, which is at least x/2, the number of steps is logarithmic in x. For x=1e9, the maximum steps are log2(1e9) which is around 30. So recursion is acceptable.

Alternatively, we can implement this iteratively.

Let's think about the iterative approach. For a given x, we can keep adding x to the sum, then compute x as x/spf(x), until x becomes 1.

Wait, but the sum is the sum of all x's along the path, including 1. So for example, the sum for 10 is 10 +5 +1 =16.

But according to the function f(x), when x=1, return 1. So the iterative approach would be:

sum =0

current =n

while current !=1:

    sum += current

    spf = find_spf(current)

    if spf == current:  # current is prime

        sum +=1

        break

    else:

        current = current // spf

sum += current  # which is 1?

Wait, maybe not. Let's see:

Start with current =n.

sum =0.

Loop:

sum += current.

find spf.

if current is prime, then next step is 1. So sum +=1 (current=1). Then break.

Otherwise, current = current/spf.

Repeat.

Wait, but in the case where current is composite, then after adding current to sum, we proceed to current/spf.

For example, n=8:

current=8, sum=8. spf=2. current becomes 4. sum +=4 (sum=12). spf=2. current becomes 2. sum +=2 (sum=14). spf=2. current becomes 1. sum +=1 (sum=15). loop ends.

Yes, that's correct.

Another example, n=10:

current=10, sum=10. spf=2. current=5 (sum=10). then current is 5, which is prime. sum +=5 (sum=15), then add 1. sum=16.

Yes.

So the algorithm is:

Initialize sum =0.

current =n.

while True:

    sum += current.

    if current ==1:

        break.

    spf = find_spf(current).

    if spf == current:  # current is prime.

        sum +=1  # because next term is 1.

        break.

    else:

        current = current // spf.

sum is the total.

Wait, but when current is prime, the next term is 1, which is added to the sum. So for example, current=5:

sum +=5. Then check if current is prime (yes). So add 1 (the next term) and break. So sum becomes 5+1=6? Wait, no. The original code for f(5) is 5+1=6. But in the loop:

sum starts at 0.

current=5. sum +=5 (sum=5). check spf. spf=5. So add 1 (sum=6) and break. So sum is 5+1=6. But in the problem statement, the sum for a prime is 5+1=6. Which is correct.

But in the case of x=10:

sum starts at 0.

current=10: sum=10. spf=2. current becomes 5.

sum +=5: sum=15. then check spf=5. sum +=1: sum=16. break. So total is 16. Correct.

So the iterative approach is correct.

Thus, the algorithm is:

sum =0

current =n

sum += current.

if current is 1, break.

loop:

    spf = find_spf(current)

    if spf is current (prime):

        sum +=1

        break

    else:

        current = current // spf

        sum += current

But wait, no. Because in the code above, when current is not prime, we compute the next current as current/spf and add that to the sum. Then repeat.

Wait, let's see.

Take current=8:

sum starts at 8.

spf is 2. current becomes 4. sum +=4 (12).

spf is 2. current becomes 2. sum +=2 (14).

spf is 2. current becomes 1. sum +=1 (15). But current is 1 now, so loop breaks.

So the code would be:

sum =0

current =n

sum += current

while current !=1:

    spf = find_spf(current)

    if spf == current:  # prime

        sum +=1

        break

    else:

        current = current // spf

        sum += current

So the loop runs as long as current is not 1.

Wait, no. Because if current is prime, then after adding 1 to sum, we break. Otherwise, current is divided by spf and added to sum. Then repeat.

But when current is divided by spf, it's possible that the new current is 1, in which case the loop exits. For example:

current=2: sum +=2. then spf=2, which is equal to current, so sum +=1, break. Total sum 3. But 2 is prime, so the sum is 2+1=3.

But according to the problem's note, the sequence ends with ck=1. So when current is 2, the next term is 1, and sum adds 1.

Yes.

So the code is:

sum =0

current =n

sum += current

while current !=1:

    spf = find_spf(current)

    if spf == current:

        sum +=1

        break

    else:

        current = current // spf

        sum += current

But wait, in the case where current is 6:

current=6, sum=6. spf=2. current becomes 3. sum +=3 (9). spf=3. sum +=1 (10). break. So total sum is 10, which is correct (6+3+1=10).

Yes.

Another example: current=12.

sum=12.

spf=2. current becomes 6. sum +=6 →18.

spf=2. current becomes 3. sum +=3 →21.

spf=3. sum +=1 →22. break.

Yes.

So the code works.

Now, the problem is to implement the find_spf function efficiently. For x up to 1e9, the loop in find_spf runs up to sqrt(x). For x=1e9, sqrt(x) is 3e4, which is manageable. But for numbers that are primes, we have to check up to sqrt(x), which can be up to 3e4 for x=1e9, which is acceptable.

So the code would be:

Implement the find_spf function as follows:

def find_spf(x):

    if x % 2 ==0:

        return 2

    max_divisor = int(math.sqrt(x)) +1

    for i in range(3, max_divisor, 2):

        if x%i ==0:

            return i

    return x  # x is prime

Wait, but the loop is written as for i in range(3, max_divisor, 2). But the range in Python is [start, end), so if max_divisor is 3e4, it checks up to 3e4-1. But for example, x=9. sqrt(9) is 3. So max_divisor is 3+1=4. The loop runs from 3 to 4, step 2. So i=3. x%3==0, returns 3. Correct.

Another example, x=25. sqrt is 5. max_divisor=6. loop runs i=3,5 (since step 2). 3: 25%3 is 1. 5: 25%5 is 0. returns 5. Correct.

But wait, the loop for i in range(3, max_divisor, 2) would not check 5 in the case where max_divisor is 6. Because range(3,6,2) is 3,5. So 5 is included. So 25%5 is 0, returns 5. Correct.

Another example, x=21. sqrt is ~4.58. max_divisor=5. loop runs 3. 21%3=0, returns 3. Correct.

So the function works.

Now, the code for the problem:

Read n.

Compute the sum as per the iterative approach.

So the code in Python would be:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    def find_spf(x):
        if x % 2 == 0:
            return 2
        max_divisor = int(math.sqrt(x)) + 1
        for i in range(3, max_divisor, 2):
            if x % i == 0:
                return i
        return x  # x is prime

    sum_total = n
    current = n
    while current != 1:
        spf = find_spf(current)
        if spf == current:  # current is prime
            sum_total += 1
            break
        else:
            current = current // spf
            sum_total += current

    print(sum_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
""",
            "output": \
"""\
15
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

n=8.

current=8. sum=8.

spf=2. current becomes 4. sum 12.

spf=2. current becomes 2. sum 14.

spf=2. current becomes 1. sum +=1? Wait, no. Let's step through:

After current becomes 2 (sum 14), loop continues (current !=1).

spf of 2 is 2 (since it's prime). sum +=1 →15. break. So sum is 15. Correct.

Another test case: n=6.

sum starts at 6.

current=6. spf=2. current becomes 3. sum 9.

current=3. spf=3. sum +=1 →10. break.

Output 10. Correct.

Another test case: n=12.

sum starts at 12.

current=12. spf=2. current=6. sum 18.

current=6. spf=2. current=3. sum 21.

current=3. spf=3. sum 22. break.

Yes.

This code should handle all cases correctly. Now, let's test for some edge cases.

Test case: n=2 (prime). sum is 2+1=3.

Code: sum starts at 2. current is 2. spf=2. sum +=1 →3. Correct.

Test case: n=3. sum is 3+1=4. Correct.

Test case: n=4. code steps:

current=4. sum=4. spf=2. current=2. sum 6. current=2. spf=2. sum 7. break. sum is 4+2+1=7. Correct.

Another edge case: n=9.

sum starts at 9.

current=9. spf=3. current=3. sum 12.

current=3. spf=3. sum 13. break. So sum is 9+3+1=13. Correct.

So the code works.

Now, what about a number that is a product of multiple primes?

For example, n=105=3*5*7. The code's path:

sum=105.

spf=3. current=35. sum=140.

spf=5. current=7. sum=147.

spf=7. sum +=1 →148. Total sum 105+35+7+1=148.

Which is the correct path.

So the code seems correct.

Now, about the efficiency. For n=1e9, which is even, the spf is 2. current becomes 5e8. Then spf is 2 again. This continues until current is 5^9 (1953125), which is odd. Then, the code checks 3, 5, etc. But for 5e8, sqrt is 2.2e4, which is manageable. So for numbers up to 1e9, the code should run in O(k * sqrt(x)) time, but since each step reduces x by a factor of at least 2, the number of steps is O(log x), and each step's spf check is O(sqrt(x)), which for the worst case (x is a prime) would be O(sqrt(n)), but for n=1e9, sqrt is 3e4, which is acceptable within 2 seconds.

But for a prime number like 1e9+7 (which is a prime), the code would check all possible divisors up to sqrt(n), which is about 3e4 steps. That's manageable.

Thus, the code should pass all test cases within the time limit.
</think>

```python
import math

n = int(input())

def find_spf(x):
    if x % 2 == 0:
        return 2
    max_divisor = int(math.sqrt(x)) + 1
    for i in range(3, max_divisor, 2):
        if x % i == 0:
            return i
    return x  # x is prime

sum_total = n
current = n
while current != 1:
    spf = find_spf(current)
    if spf == current:  # current is prime
        sum_total += 1
        break
    current //= spf
    sum_total += current

print(sum_total)
```
