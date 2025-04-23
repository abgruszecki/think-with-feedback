<think>
Okay, let's try to solve this problem. So, the problem is about calculating the minimum and maximum possible total fare for a bus with n adults and m children. The constraints are that each adult can take up to one child for free. But wait, no—wait, the description says that a grown-up can have k children, and pays k rubles: one for himself and (k-1) for the children. So, each adult can have any number of children, but the way the fare is calculated is based on how many children they take. For each adult with k children, the cost is 1 (for the adult) plus max(k-1, 0) for the children. Wait, no. Wait, the example says when an adult has two children, he pays 2 rubles. Because 1 for himself and 1 for one child (since the other is free). Wait, no: the problem statement says, "no more than one child can ride for free with each grown-up." So, each adult can take one child for free. For the rest, they have to pay. So, for k children, the cost for that adult is 1 (adult's ticket) plus max(k - 1, 0). Because one child is free, the others are paid.

So the total fare per adult is 1 plus (number of children they take -1). But the children must not be able to ride alone. So, all children must be assigned to some adult. If there are children left without adults, then the scenario is impossible.

So the first thing is to check if the situation is possible. The conditions for impossibility are:

- If there are any children (m >0) and no adults (n ==0), then impossible.
- Otherwise, all children must be covered by the adults. But how?

Wait, the problem says that children can't ride unaccompanied. So the sum of all children must be covered by the adults. So each child must be in a group with at least one adult. So the number of children m must be <= sum of the number of children each adult can take. But since each adult can take any number of children (as long as all are accounted for), but the calculation of the fare is based on how many each takes. So the only way for the situation to be possible is if there are enough adults to cover the children. Wait, no. Wait, even if there are more adults than children, that's okay. Because each child must be assigned to some adult. For example, if there are 3 adults and 1 child, the child can be assigned to any one of them. The other two adults have 0 children. So, in that case, the fare would be (1 (adult) +0 (child's free)) for that adult plus 1 for each of the other two. So total 3+1=4? Wait, no. Wait, the adult with the child has 1+ (1-1) =1 ruble. The other adults each pay 1. So total is 3*1 + (1-1) =3. So total is 3. So, the maximum and minimum would be the same in that case.

So the first condition is: if m > 0 and n ==0, impossible.

Otherwise, the possible case is when there are enough adults to cover the children. But how?

Wait, no. Wait, the problem states that children can't ride unaccompanied, so if there are any children, there must be at least one adult. So the first condition is if m >0 and n ==0, output impossible. Otherwise, proceed.

So now, for the possible case, compute min and max fare.

For maximum fare:

The maximum fare is when each adult takes as few children as possible, leading to more children per adult, but how does that affect the fare?

Wait, the fare per adult is 1 + (k-1) where k is the number of children assigned. So for maximum total fare, we need to maximize the sum over all adults of (1 + (k_i -1)) = sum(1 +k_i -1) = sum(k_i). But since sum(k_i) is exactly m (because all children are assigned), the maximum sum would be n + (m). Because each adult pays 1 + (k_i -1) =k_i. So sum(k_i) is m. The total fare is sum(k_i) =m. Wait, that can't be right. Wait, wait, no. Wait, wait: the fare per adult is 1 (for the adult) plus (k_i -1) for the children. So each adult contributes 1 + (k_i -1) =k_i. So sum over all adults is sum(k_i). But sum(k_i) is the total number of children plus the number of adults. Wait, no. Because sum(k_i) is the number of children each adult is responsible for. So sum(k_i) =m. Because each child is assigned to exactly one adult. Then, the total fare is sum(k_i) for all adults. So sum(k_i) = m. So the total fare would be m. But that's only possible if each child is counted once. Wait, that's not possible. Wait, let's see: for example, in the first sample input, n=1, m=2. The adult takes 2 children. The fare is 1 + (2-1) =2. So sum is 2, which equals m. Wait, yes. So the sum is m. So in that case, the maximum and minimum fare would be m. But wait, the sample shows that output is 2 2. So sum is 2, which is equal to m=2.

Another example: input 2 2. The output is min 2, max 3. Let's see. For maximum fare: how? Let's see. The maximum is achieved when one adult takes two children (fare 1+1=2) and the other takes zero (fare 1). So total is 3. Which is m (2) plus (number of adults) 2 minus 1? Not sure. Wait, in that case, sum(k_i) is 2 (from the first adult) + 0 (from the second, but no children). Wait no: sum(k_i) is 2 (children) for the first, 0 for the second. So sum is 2. Then the fare would be 2 (from first) +1 (from second) =3. Wait, because the fare for each adult is 1 + (k_i -1). So first adult: 1 + (2-1) =2. Second adult: 1 + (0-1) → no, because k_i can't be negative. Wait, k_i is the number of children assigned to that adult. So if an adult has zero children, then k_i is zero. So fare is 1 + (0-1) → but that's 0? No, because the max between (k_i -1) and 0. Wait, no. Wait, the fare is 1 (for the adult) plus (k_i -1) if k_i >=1, else 0. So for an adult with zero children: fare is 1 +0 =1.

So in the example where n=2 and m=2, the maximum fare would be when one adult takes both children (fare 1+1=2) and the other takes zero (fare 1). So total 3. So sum is 3. But sum(k_i) is 2, so the total fare is sum(1 + max(k_i-1,0)) for all adults. Which is sum(1) + sum(max(k_i-1,0)). So for each adult, the fare is 1 plus max(k_i-1, 0). The sum is n + sum(max(k_i-1, 0)).

So in the first example, sum(max(k_i-1,0)) is 1 (adult has 2 children, so 2-1=1). So total is 1 (n) +1=2. Which matches.

In the second case (n=2, m=2) for the max fare: sum(max(k_i-1,0)) would be (2-1) + (0) =1. So total is 2+1=3.

So the maximum fare is achieved when as many children as possible are assigned to a single adult, so that the sum of (k_i -1) is maximized. Because each child beyond the first assigned to an adult adds 1 to the sum. So to maximize, we should assign as many children as possible to a single adult. Because then, (k_i-1) is maximized. Wait, but the sum over all (k_i-1) is equal to (sum k_i) - (number of adults with at least one child). Because sum(k_i) is m, so sum(k_i-1) for all adults with k_i >=1 is m - (number of such adults). So, to maximize sum(k_i-1), we need to minimize the number of adults that have at least one child. Because sum(k_i-1) = m - t, where t is the number of adults that have at least one child. So to maximize m - t, we need to minimize t.

So the minimal t is 1 if possible. Because that way, m - t is m-1, which is the maximum possible. But is it possible to have t=1?

Only if one adult can take all m children. So, if m <= (some maximum possible per adult). But the problem doesn't specify a maximum per adult. So any adult can take any number of children. So as long as there's at least one adult (which is the case here), then yes. So for maximum fare:

The maximum fare is n + (m - t), where t is the number of adults that have at least one child. To maximize m -t, we need to minimize t. The minimal t is 1 (if possible) or the minimal number of adults needed to cover all children, but since each child can be assigned to any adult, as long as t >=1 (since m >=1?), no. Wait, if m is zero, then t is zero, but that's a different case.

Wait, the maximum fare is when the sum (n + (sum (k_i -1)) ), which is n + (m - t), where t is the number of adults that have at least one child. Because sum (k_i -1) over all adults where k_i >=1 is (sum k_i) - t = m -t.

So to maximize, we need to maximize (m -t), which requires minimizing t. The minimal t can be 1, if m >=1. So the maximum fare is n + m -1. Because t is 1. So sum is n + (m-1). For example, in the first sample, n=1, m=2. Max is 1+2-1=2, which matches. In the second sample (n=2, m=2), the maximum is 2+2-1=3, which matches the example.

So maximum fare is n + m -1, but only if m >=1. If m is zero, then the sum is n (each adult pays 1, no children). So the maximum fare when m is zero is n.

So maximum is:

if m ==0 → max is n

else → n + m -1

Wait, but what if m is zero and n is non-zero? Then each adult pays 1, so sum is n. So yes.

So maximum is always n + max(m-1, 0).

Wait, because if m is zero, then max(m-1,0) is 0. So sum is n. But if m >=1, then it's n + (m-1).

But how does that apply to the first example. Let's see: n=1, m=2. 1 + 2-1=2. Correct.

For the third example, the maximum is 2 + 2-1=3. Correct.

Another example: n=3, m=5. Then maximum is 3+5-1=7. How?

Assign all 5 children to one adult. Then that adult's fare is 1 +5-1=5. The other two adults have 0 children, paying 1 each. Total 5+1+1=7. Which is 3+5-1=7. Yes.

So maximum is n + m -1 if m >=1, else n.

Now, the minimum fare.

The minimum fare occurs when each adult takes as many children as possible, thereby maximizing the number of children that ride for free. Because each child after the first one for an adult adds 1 to the fare. So to minimize the fare, we want as many children as possible to be covered by the first (free) per adult.

So the minimal fare is n (each adult pays 1) plus the number of children that exceed the number of adults. Because each adult can take one child for free. So the number of free children is the number of adults (since each can take one). So the remaining children (m -n) must each pay 1, but only if m >n. If m <=n, then all children are covered by the free ones, so no extra cost. So the minimal fare is n + max( m -n, 0 ). But wait, how?

For example, when n=1, m=2: the first adult takes two children. The fare for that adult is 1 +1 (since 2-1=1). So the total is 2. Which is 1 + (2-1) =2.

Another example: n=2, m=2. The minimum is 2. How? Each adult takes one child. So each's fare is 1 +0 (since 1-1=0). Total 2.

If n=3, m=5: each adult takes one child (3 free), leaving 2 to pay. So fare is 3 (adults) +2 (extra children) =5.

So minimal fare is n + max( m -n, 0 ). But wait, if m is zero, then it's n +0 =n, which is correct.

So putting this together.

The minimal fare is max( m -n, 0 ) +n.

But wait, that's equivalent to max(m, n). Because if m >=n: (m -n) +n =m. If m <n: 0 +n =n. So the minimal fare is max(n, m).

Wait, wait: for example, n=2, m=2: max(2,2) is 2. Correct. For n=3, m=5: max(5,3) is5. Which matches. For n=1, m=2: max(2,1) is2. Correct.

But wait, earlier example where n=2, m=2, the minimal fare is 2 (adults each take one child, sum is 2+0=2). Which is correct. So yes, the minimal fare is max(n, m).

Wait, this seems to be the case.

Wait, let's see another example. n=2, m=3. So minimal fare: each adult takes one child (free), third child has to be assigned to one of them, adding 1. So total fare is 2 (adults) +1 (third child) =3. Which is max(2,3) =3. Correct.

Another example: n=3, m=1. Each adult can take one child. But there's only one child, so two adults have zero. So fare is 3 +0 (since m -n is negative) → 3. Which is correct. So yes, minimal fare is max(n, m).

So, the minimal fare is max(n, m) when possible.

But wait, no. Wait, wait: if m is greater than n, then the minimal fare is m. Because the adults can take n children for free (each takes one), and the remaining (m-n) children each add one to the fare, so total is n + (m-n) =m. If m <=n, then all children are covered by the free ones, so total is n.

So yes, the minimal fare is max(n, m).

But how to confirm with the examples.

Sample input 2 2: output min is 2. Which is max(2,2) =2. Correct.

Sample input 1 2: output min is 2. Which is max(1,2) =2. Correct.

Sample input 0 5: impossible.

Sample input 2 3: min is3.

Yes, this seems correct.

So, the minimal and maximum fares are:

If the situation is possible (i.e., (n >=1 or m==0)), then:

minimum = max(n, m)

maximum = n + max(m-1, 0) if m >=1 else n.

But wait, when m ==0, the maximum is n, which is correct.

But when m is zero, the minimum is max(n,0) → since m is zero, the minimal fare is n. Which is correct.

So, putting it all together.

The possible condition is: if m ==0, then possible as long as n can be anything (since children are zero). Or, if m >0 and n >=1.

So the possible condition is: (n >=1 and m >=0) or (n ==0 and m ==0). Wait, no. Because if m is zero and n is also zero, then it's possible (no passengers, so no fare). But according to the problem statement, what's the output in that case? Let's see.

If n=0 and m=0, then the output would be 0 0. Because there are no passengers, so the sum is zero.

But according to the problem statement's output examples, when the input is 0 5, output is impossible. So the possible conditions are:

If m ==0 → possible (even if n=0?), but in that case, the fare is 0 0.

Wait, the problem's output in case of 0 0 would be "0 0" because there are no passengers, so fare is zero.

But the problem's constraints say that n and m can be zero. So let's see.

So the possible conditions are:

If m >0 and n ==0 → impossible.

Else, possible.

So the code needs to check:

if (n ==0 and m >0) → impossible.

Else:

compute min and max.

But for the case when both n and m are zero, the output is 0 0.

So, now, the steps for the code are:

Read n and m.

Check if m >0 and n ==0 → output impossible.

Else:

if possible, compute min and max.

Compute min as max(n, m). Because:

- When m <=n: each adult can take one child (free), so sum is n. But since m <=n, the sum is n.

Wait, no: when n=3, m=2. Then all m children are taken by adults, each taking one, so the sum is 3 (each adult pays 1, and the children are free). So min is 3.

max(n, m) is 3, which is correct.

When m >n: sum is m.

So min is max(n, m).

Max is:

if m ==0 → n.

else → n + m -1.

So code steps:

n, m = map(int, input().split())

if m >0 and n ==0:

    print("Impossible")

else:

    if m ==0:

        min_fare = n

        max_fare = n

    else:

        min_fare = max(n, m)

        max_fare = n + m -1

    print(f"{min_fare} {max_fare}")

Wait, but wait, the problem's first example:

Input 1 2 → output is 2 2. So according to the code, min is max(1,2)=2, max is 1+2-1=2. So correct.

Second example:

0 5 → impossible.

Third example:

2 2 → min is max(2,2)=2, max is 2+2-1=3 → correct.

Another example: n=0, m=0 → output 0 0.

Another example: n=3, m=5 → min is5, max 3+5-1=7.

Another example: n=5, m=3 → min is5, max 5+3-1=7.

Another example: n=0, m=0 → possible, output 0 0.

What about when m=0 but n is not zero? Like n=5, m=0 → min and max are 5.

Yes.

So this code seems to handle all cases.

So, the code would be:

Read n and m.

If m >0 and n ==0 → impossible.

Else:

if m is 0:

    min and max are n.

else:

    min is max(n, m)

    max is n + m -1.

Then print min and max.

But wait, what about when m is zero but n is zero?

n=0, m=0 → possible, so code proceeds to else.

Since m is zero, min and max are n=0.

Which is correct.

So this code should handle all cases.

So the code is:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    if m > 0 and n == 0:

        print("Impossible", file=output_stream)

    else:

        if m == 0:

            min_f = n

            max_f = n

        else:

            min_f = max(n, m)

            max_f = n + m -1

        print(f"{min_f} {max_f}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
0 5
""",
            "output": \
"""\
Impossible
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

test case: input 0 0 → output 0 0.

Another test case: input 5 0 → output 5 5.

Another test case: input 3 5 → 5 7.

Another test case: input 3 1 → 3 3 (because m=1 >=1, max is 3+1-1=3, min is max(3,1)=3).

Yes, correct.

So this code should solve the problem.
</think>

```python
n, m = map(int, input().split())
if m > 0 and n == 0:
    print("Impossible")
else:
    min_f = max(n, m)
    max_f = n + max(m - 1, 0) if m else n
    print(f"{min_f} {max_f}")
```
