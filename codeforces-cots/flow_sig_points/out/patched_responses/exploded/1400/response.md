<think>
Okay, let's see. The problem is about assigning points to programming contest problems such that the Robo-Coder robot (R) gets more points than the BionicSolver robot (B). We need to find the minimal possible maximum p_i. Hmm.

First, I need to figure out under what conditions it's possible. If R and B solve the exact same set of problems, then their sum will be equal regardless of the p_i values. So in that case, the answer is -1. Also, if R's set is a subset of B's, then even if all p_i are 1, B's sum would be equal or higher. Wait, but maybe there's a case where R solves some problems that B doesn't. Wait, no. If B solves all the problems that R does, then R's sum can't exceed B's. So in that case, it's impossible. So first, we need to check if there's at least one problem that R solves but B doesn't. Otherwise, it's impossible.

So the first step: check if there exists an i where r_i=1 and b_i=0. If there are none, output -1. Because any problem that R solves, B also solves. So B's sum will be at least as much as R's. So R can't have a higher sum.

Wait, but what if R solves some problems that B doesn't? Then those can contribute to R's sum but not B's. So in that case, even if other problems B solves, but R doesn't, maybe R can have a higher sum by making those unique p_i high enough.

So the initial check is: the set of problems where R solves and B doesn't must be non-empty. Otherwise, return -1.

Once that's confirmed, we need to assign p_i's such that the sum of (r_i * p_i) > sum of (b_i * p_i). And we need to minimize the maximum p_i.

So how to model this? Let's think about each problem. For each problem i, the contribution to the difference (R's points minus B's) is (r_i - b_i) * p_i. Because R's sum is sum(r_i * p_i), B's is sum(b_i * p_i). The difference is sum( (r_i - b_i) * p_i ). We need this sum to be > 0.

So, the problem is to assign p_i >=1 for each i, such that the sum of (r_i - b_i)*p_i > 0, and minimize the maximum p_i.

Hmm. So the key is to maximize the sum of (r_i - b_i)*p_i in a way that the sum is positive, but with the minimal possible maximum p_i.

Wait, but how do we approach this optimization problem? Let's think about the possible cases for each problem:

For each problem i, (r_i, b_i) can be:

(1, 0): R solves, B doesn't. Then (r_i - b_i) is 1. So this contributes +p_i to the difference.

(0, 1): R doesn't solve, B does. Then (r_i - b_i) is -1. So this contributes -p_i to the difference.

(1,1): Both solve. Then (r_i - b_i) is 0. So p_i can be 1, as it doesn't affect the sum.

(0,0): Neither solve. p_i can be 1 as well.

So the only variables are the p_i's for the cases (1,0) and (0,1). The rest can be set to 1.

So let's split the problems into three categories:

A: Problems where R solves and B doesn't (r_i=1, b_i=0). These contribute +p_i to the difference.

B: Problems where B solves and R doesn't (r_i=0, b_i=1). These contribute -p_i to the difference.

C: All others. These contribute 0, so p_i can be 1.

Let’s denote the variables:

Let S_A = sum of p_i for all A problems.

S_B = sum of p_i for all B problems.

The total difference is S_A - S_B.

We need S_A - S_B > 0.

But all p_i >= 1. So for A problems, p_i >=1. For B problems, p_i >=1. For C, p_i =1.

Our goal is to choose p_i for A and B such that S_A > S_B, and the maximum p_i (considering all A and B problems) is minimized.

Wait, but for C problems, p_i is 1. So the maximum p_i is the maximum between the p_i's in A and B and 1. But since in A and B, p_i >=1, the maximum is either the maximum among A and B, or 1, but if all A and B have p_i >=1, then the maximum will be the maximum of A and B's p_i.

So the problem reduces to assigning p_i's to A and B, where each p_i >=1, such that sum(A) > sum(B), and the maximum p_i in A and B is as small as possible.

But how?

Let me think. Let's say there are a problems in A and b problems in B.

If there are no B problems (b=0), then sum(B) is 0. So sum(A) must be at least 1, but since each p_i in A is at least 1, sum(A) >= a. So sum(A) >=a. So S_A - S_B = a >=1. So in this case, all p_i can be 1. The maximum is 1. So answer is 1.

But when B is present, how to model this?

Hmm. Let's imagine that for each B problem, the p_i is set to some value. The sum of B's p_i's must be less than the sum of A's p_i's.

But for B problems, each p_i is at least 1, so sum(B) >= b. For A problems, sum(A) >= a.

So the condition is sum(A) > sum(B). And the maximum p_i in A and B is to be minimized.

We need to find the minimal possible maximum p_i such that sum(A) > sum(B), where each p_i in A is >=1, and each p_i in B is >=1.

So the question is how to assign these p_i's.

Let's consider the problem: For A and B groups, how to choose their p_i's to minimize the maximum.

An approach could be to set as many p_i's as possible to 1, and adjust the necessary ones to get the sum(A) > sum(B).

But how?

Let's first compute the minimal sum for B. sum(B) is at least b.

sum(A) needs to be > sum(B). Since sum(B) can be as low as b, sum(A) needs to be at least b +1.

But sum(A) is at least a (since each of the a A's is at least 1). So if a > b, then sum(A) >=a >= b+1 (if a >b). So sum(A) can be a, sum(B) can be b, and a >=b+1. Then the condition is satisfied. So in that case, all p_i in A and B can be 1, and the maximum p_i is 1.

But if a <= b, then sum(A) >=a, sum(B) >=b. But a <=b, so even sum(A) =a and sum(B) =b. Then a needs to be >b, which isn't possible. So in this case, we need to set some p_i in A higher than 1, or some p_i in B higher than 1, but that seems counterintuitive.

Wait, wait. Let's think. For example, suppose a=2, b=3. sum(A) is 2, sum(B) is 3. Then 2>3 is false. So we need to increase sum(A) or decrease sum(B) (but sum(B) can't be decreased below 3). So sum(A) must be >=4 (since sum(A) > sum(B) => sum(A) > sum(B) which is at least 3). So sum(A) must be at least 4. Since a=2, each A can be 2. So sum(A) is 4. sum(B) is 3. Then the maximum is 2. So in this case, the answer is 2.

So the key is to find the minimal k such that sum(A) > sum(B), where each A's p_i <=k, each B's p_i <=k, and all p_i >=1.

But how to model this?

Alternatively, think of the minimal k such that when all A's are set to 1, and B's are set to 1, but if sum(A) > sum(B), then k=1. Otherwise, we need to find the minimal k where we can adjust some p_i's in A and/or B to reach sum(A) > sum(B) with maximum p_i <=k.

Hmm. Let's model this as an optimization problem where we want to minimize k.

The approach could be binary search on k. For a given k, can we assign p_i's to A and B such that sum(A) > sum(B), and all p_i <=k and >=1?

If we can find the minimal k where this is possible, that's our answer.

So the steps would be:

1. Check if there is at least one A (r_i=1 and b_i=0). If not, return -1.

2. Then, compute a = number of A's (r=1, b=0). b = number of B's (r=0, b=1).

3. The minimal possible sum for B is b (each p_i=1). The minimal sum for A is a. If a > b, then sum(A) can be a (each 1), sum(B) is b, so a >b. So sum is a -b >0. So possible with k=1.

So in this case, answer is 1.

Else, we need to find k such that sum(A) can be as large as possible (up to a *k) and sum(B) as small as possible (but >=b). So sum(A) must be > sum(B). So sum(A) >= sum(B) +1.

But how to model this.

Alternatively, binary search for k. For a given k, what's the maximum possible sum(A) - sum(B) given that all p_i <=k and >=1.

The maximum sum(A) is a *k (each p_i is k). The minimum sum(B) is b (each p_i is 1). So sum(A) - sum(B) would be a*k - b. If this is >0, then it's possible.

But maybe even with smaller sum(A) and higher sum(B), but still sum(A) > sum(B).

Wait, but for a given k, the maximum possible sum(A) is a*k, and the minimal sum(B) is b. So if a*k > sum(B) (where sum(B) is at least b), then the maximum possible difference (a*k - sum(B)) would be maximized when sum(B) is as small as possible. So if a*k > b, then there exists a way to assign p_i's such that sum(A) >= sum(B)+1.

Wait, no. Let's see:

For sum(A) to be as large as possible, set all A p_i to k. For sum(B) to be as small as possible, set all B p_i to 1. Then sum(A) = a*k, sum(B) = b. If a*k >b, then yes. So for a given k, if a*k >b, then answer is yes.

Wait, but what if a*k -b >=1? Because sum(A) must be > sum(B). So sum(A) >= sum(B) +1.

So for a given k, if a*k >= sum(B) +1, where sum(B) can be as small as b (since B p_i can be 1), then possible.

So the condition for k being possible is: a*k >= (sum_B_min) +1, where sum_B_min =b.

So a*k >= b +1.

If that holds, then yes. Because sum(A) can be set to a*k (max possible), sum(B) is sum_B_min (b). Then difference is a*k -b >=1.

So, the minimal k is the smallest integer such that a*k >= b +1.

But wait, what if a is 3 and b is 5. Then a=3, b=5.

So 3k >=5 +1 → 3k >=6 →k >=2.

So k=2. 3*2=6, which is >=6 → sum(A) is 6, sum(B) is 5. So 6>5. So yes. Then maximum p_i is 2.

But what if a=2, b=3?

Then 2k >=4 →k >=2.

At k=2, sum(A) is 4, sum(B) is 3 → difference 1. So yes.

So the formula seems to work.

But what about when a=3 and b=3. Then a*k >=4. So k >= 2 (since 3*2=6 >=4). Then sum(A)=6, sum(B)=3. 6-3=3>0. So yes.

So the minimal k is ceil( (b+1)/a )

Wait, because (b+1) /a rounded up.

But wait, if (b+1) is divisible by a, then k is (b+1)/a. Otherwise, (b+1)//a +1.

Yes.

So k_min = ceil( (b +1)/a )

But this is only when a <=b. Because when a> b, then k=1.

So putting it all together:

First, check if there are any A (r_i=1 and b_i=0). If not, output -1.

Else:

Compute a = number of A's (r=1, b=0).

Compute b = number of B's (r=0, b=1).

If a >b → then k=1.

Else:

k_min = ceil( (b +1)/a )

But wait, let's test this against the examples.

First example:

Input 5

R: 1 1 1 0 0 → A is positions 0,1,2 (r=1, b=0?)

Wait wait, the input for R and B is:

Second line: r's.

Third line: b's.

So for each i, check r_i and b_i.

In the first example:

r is [1,1,1,0,0]

b is [0,1,1,1,1]

So for each i:

i=0: r=1, b=0 → A (counts as A)

i=1: r=1, b=1 → C

i=2: r=1, b=1 → C

i=3: r=0, b=1 → B

i=4: r=0, b=1 → B

So a=1 (only i=0 is A), b=2 (i=3 and 4 are B).

So a=1, b=2.

Since a <=b → compute k_min = ceil( (2 +1)/1 )=3.

Which matches the sample output of 3.

Yes.

Another example in the note:

Sample input 4:

9

r:1 0 0 0 0 0 0 0 1 → a is the count where r_i=1 and b_i=0.

b:0 1 1 0 1 1 1 1 0.

So for each i:

i=0: r=1, b=0 → A (counted in a)

i=1: r=0, b=1 → B

i=2: r=0, b=1 → B

i=3: r=0, b=0 → C

i=4: r=0, b=1 → B

i=5: r=0, b=1 → B

i=6: r=0, b=1 → B

i=7: r=0, b=1 → B

i=8: r=1, b=0 → A.

So a=2 (i=0 and 8 are A), b=6 (i=1,2,4,5,6,7 are B).

So a=2, b=6. So a <=b.

k_min = ceil( (6+1)/2 ) = ceil(7/2) =4. Which matches the sample output.

Yes.

So the formula holds.

Another example: if a=3, b=5.

k_min= ceil(5+1 /3 )=ceil(6/3)=2.

Which would require sum(A)=3*2=6, sum(B)=5. 6>5 → yes.

So the approach is:

Compute a and b.

If a ==0 → output -1.

Else if a >b → output 1.

Else, output ceil( (b+1)/a ).

But wait, this is only correct if all B's p_i are set to 1. But in reality, the B's p_i can be set higher than 1. Wait, but in our calculation, we assumed that sum(B) is at least b. So the minimal possible sum(B) is b (when all are 1). So our formula gives the minimal possible k based on the worst case scenario where sum(B) is as small as possible. Because if sum(B) is higher than b, then sum(A) needs to be even larger. But in that case, perhaps the required k would be higher. But the formula gives the minimal possible k under the assumption that sum(B) is minimal. So how is that correct?

Wait, no. Because the formula is based on the minimal sum(B) and maximal sum(A). Because in that case, the difference is maximized (sum(A) is as large as possible, sum(B) as small as possible). So for a given k, the maximum possible difference is a*k - b. If this difference is >=1, then the assignment is possible. But in reality, sum(B) can be larger than b. For example, if B's p_i are higher than 1. So the actual sum(B) can be up to b*k. But in that case, sum(A) is a*k. So the difference would be a*k - sum(B). But sum(B) can be as high as b*k. So for the difference to be positive, a*k > sum(B). But if sum(B) can be as high as b*k, then the condition would be a*k > sum(B). The worst case is sum(B) =b*k. So the condition a*k >b*k → (a -b) *k>0. But if a <=b, then (a -b) is <=0. So this can't happen. So in such a case, even with sum(B) being as large as possible, it's impossible. But this contradicts our earlier approach.

Wait, this suggests that the formula is not correct. Because in some cases, even if a*k >=b+1, but when sum(B) can be higher than b, the difference may not be sufficient.

Wait, no. Because sum(B) can be anything between b and b*k. So for the difference sum(A) - sum(B) to be positive, sum(A) must be > sum(B). The maximum possible sum(B) is b*k. So for the assignment to be possible for a given k, sum(A) must be > sum(B) for all possible sum(B) in [b, b*k]. But that's not feasible. Wait, no. Because sum(B) is determined by the p_i's chosen. The problem allows us to choose the p_i's such that sum(A) is as large as possible, and sum(B) as small as possible. So the optimal way is to set sum(B) to the minimal possible (b), and sum(A) to the maximal possible (a*k). If even this gives sum(A) > sum(B), then it's possible. Otherwise, even if some sum(B) could be higher, but the minimal sum(B) case doesn't work, then we need to try a higher k.

So the formula remains correct.

So the minimal k is ceil( (b+1)/a ), when a <=b.

So the overall steps are:

1. Check if there is any problem where R solves and B does not. If not, output -1.

2. Compute a (number of such problems) and b (number of problems where B solves and R does not).

3. If a >b: then even with all p_i=1, sum(A) =a, sum(B)=b. So a >b → sum(A) - sum(B) =a -b >=1. So possible with k=1.

4. Else, compute k=ceil( (b +1)/a ). This is the minimal k to ensure that sum(A) (which can be up to a*k) is >= sum(B) (at least b) +1.

So the code can be written as follows:

Read n.

Read r list.

Read b list.

Compute a = sum( r_i ==1 and b_i ==0 for all i )

if a ==0:

    output -1

else:

    b_count = sum( r_i ==0 and b_i ==1 for all i )

    if a > b_count:

        print(1)

    else:

        required = (b_count +1 + a -1 ) // a  # ceiling( (b+1)/a )

        print(required)

So this code would handle all cases.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    r = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))
    a = sum(ri == 1 and bi == 0 for ri, bi in zip(r, b))
    if a == 0:
        print(-1, file=output_stream)
    else:
        b_count = sum(ri == 0 and bi == 1 for ri, bi in zip(r, b))
        if a > b_count:
            print(1, file=output_stream)
        else:
            print((b_count + 1 + a - 1) // a, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
0 0 0
0 0 0
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

Testing against sample inputs 2, 3.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    r = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))
    a = sum(ri == 1 and bi == 0 for ri, bi in zip(r, b))
    if a == 0:
        print(-1, file=output_stream)
    else:
        b_count = sum(ri == 0 and bi == 1 for ri, bi in zip(r, b))
        if a > b_count:
            print(1, file=output_stream)
        else:
            print((b_count + 1 + a - 1) // a, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 1 1 1
1 1 1 1
""",
            "output": \
"""\
-1
""",
        }, 
        {
            "input": \
"""\
9
1 0 0 0 0 0 0 0 1
0 1 1 0 1 1 1 1 0
""",
            "output": \
"""\
4
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

Fourth example:

9

r:1 0 0 0 0 0 0 0 1 → a is count where r_i=1 and b_i=0.

b:0 1 1 0 1 1 1 1 0.

Check each i:

i=0: r=1, b=0 → yes → a +=1.

i=1: r=0 → no.

i=2: r=0 → no.

i=3: r=0 → no.

i=4: r=0 → no.

i=5: r=0 → no.

i=6: r=0 → no.

i=7: r=0 → no.

i=8: r=1, b=0 → yes → a=2.

b_count is sum(r=0 and b=1).

For each i:

i=0: r=1 → no.

i=1: r=0, b=1 → yes.

i=2: r=0, b=1 → yes.

i=3: r=0, b=0 → no.

i=4: r=0, b=1 → yes.

i=5: r=0, b=1 → yes.

i=6: r=0, b=1 → yes.

i=7: r=0, b=1 → yes.

i=8: r=1 → no.

So b_count is 6.

a=2 <=6.

required = (6+1 +2-1 )//2 → (7 +1-1? Wait, no. Wait (6+1) is 7, divided by 2. 7/2 is 3.5, ceiling is 4.

So (7 + 2-1) //2 → (7+1)//2=8//2=4. So required is 4. Which matches the sample.

So the code works for all these cases.

Another test case where a=2, b=3:

required = (3+1)/2=4/2=2. So k=2. Which is correct.

Another case where a=3, b=5: (5+1)/3=2. So k=2.

So the code seems correct.

So the code is straightforward once we have a and b.

Thus, the code can be written as:

Read n.

Read r as list of integers.

Read b as list of integers.

a = sum(1 for i in range(n) if r[i] ==1 and b[i] ==0)

if a ==0:

    print(-1)

else:

    b_count = sum(1 for i in range(n) if r[i] ==0 and b[i] ==1)

    if a > b_count:

        print(1)

    else:

        print( (b_count +1 + a -1) // a )

Yes, that's the code.

Now, test for edge cases:

Case where a=0 → output -1.

Case where a=1, b=0: then a >b → output 1.

Case where a=3, b=3 → (3+1)/3 →4/3=1.333 → ceil is 2. So required is 2.

But a=3, sum(A) can be 3*2=6, sum(B) is 3*1=3. 6>3 → yes.

Another edge case: a=1, b=1. (b+1)/a= 2/1=2 → output 2.

Sum(A) =2, sum(B)=1 → 2>1. Correct.

Another case: a=5, b=5. required is (5+1)/5=6/5=1.2 → ceil is 2. So sum(A) 5*2=10, sum(B) 5 → 10>5. Yes.

So the code works.

Thus, the code is correct.
</think>

```python
n = int(input())
r = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sum(ri == 1 and bi == 0 for ri, bi in zip(r, b))
if a == 0:
    print(-1)
else:
    b_count = sum(ri == 0 and bi == 1 for ri, bi in zip(r, b))
    if a > b_count:
        print(1)
    else:
        print((b_count + 1 + a - 1) // a)
```
