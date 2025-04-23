<think>
Okay, I need to solve this problem. Let's read the problem carefully.

The task is to find the maximum k such that any promo code can be uniquely identified even if up to k errors are made. So, for each promo code, if someone types a code with up to k errors, it should not match any other promo code's possible valid code. Wait, no. Wait, the problem says that when you type a code with up to k errors, you can still uniquely determine which original promo code it was. So the idea is that for any two different promo codes, their "error spheres" (all codes within k errors) must not overlap. Because if there's a code that's within k errors of two different promo codes, then when that code is entered, you can't tell which original it was. Therefore, the maximum k is the minimal pairwise (k_i) minus 1, where k_i is the minimal number of differing digits between any two promo codes. Because the maximum allowed k is such that the minimal distance between any two codes is at least 2k + 1. Wait, wait. Let me think.

Hmm. So the problem is similar to error-correcting codes. The minimal Hamming distance between any two codes in the set must be at least 2k + 1. Because if two codes differ by d digits, then their spheres (all codes within k errors) will not overlap if d > 2k. Because the spheres would each include all codes at distance up to k from their centers. So the maximum k is the floor((d-1)/2), where d is the minimal Hamming distance between any two codes in the set. Therefore, the maximum possible k for the entire set is the minimal d among all pairs, subtract 1, then divide by 2, floor it.

Wait, for example, in the first sample input:

The two codes are 000000 and 999999. The Hamming distance is 6. So d=6. So (d-1)/2 = 5/2 = 2.5, so floor is 2. Hence k=2. Which matches the sample output.

In the second sample input, the minimal Hamming distance between any pair is 1 (like between 211111 and 212111, which differ in the third digit). So (1-1)/2 = 0. So k=0. Which matches the sample.

So the solution is to compute the minimal Hamming distance between any pair of promo codes, then compute (min_distance - 1) // 2. That's the maximum possible k.

So the problem reduces to:

1. Compute all pairs of promo codes.
2. For each pair, compute the Hamming distance (number of differing digits).
3. Find the minimal Hamming distance in all pairs.
4. Then, the maximum k is (min_distance - 1) // 2.

But the problem is that the number of pairs can be up to n*(n-1)/2. For n=1000, that's about 500,000 pairs. For each pair, we need to compute the Hamming distance between two 6-digit codes.

How to compute the Hamming distance efficiently?

Each promo code is a 6-digit string. For two codes, we can compare each of the six characters and count the differences. Since the codes are 6 digits long, this is O(1) per pair. So for 1000 codes, 500k pairs, each requiring 6 comparisons, that's 3 million operations. Which is acceptable for Python in 1 second, right?

Yes. So the plan is:

- Read all the promo codes into a list.
- Iterate over all possible pairs (i, j) where i < j.
- For each pair, compute their Hamming distance.
- Keep track of the minimal distance found.
- Finally, compute (min_distance -1) // 2.

But wait, if n is 1, then there are no pairs. In that case, since there's only one code, the maximum k is 6, because even with all 6 digits wrong, the code can be uniquely identified (since there are no other codes to conflict). Because the problem statement says, "any promo code can be uniquely identified if typed with up to k mistakes." But if there's only one promo code, then regardless of k, even if you make 6 errors (so a completely different code), since there's no other promo code, the input will still be uniquely identified as the only possible code. Wait, but the problem says "any promo code can be uniquely identified". If there's only one, then any k is allowed. Because there's no other code to clash with. So the maximum k is 6. Because the problem says, the output is the maximum k such that any promo code can be uniquely identified. So in this case, when n=1, the answer is 6.

Ah right. So we need to handle that case. So in code, after calculating the minimal distance, if n is 1, then the minimal distance is considered as 6*2 +1 = 13? Wait, no. Because when n=1, there are no pairs. So the minimal distance is undefined. So in code:

if n == 1:

   print(6)

else:

   compute minimal distance between all pairs, then (d-1)//2.

So that's an edge case to handle.

So steps:

1. Read n.

2. Read n promo codes, store as a list.

3. If n == 1: output 6.

4. Else:

   compute minimal Hamming distance d between any two codes.

   then output (d-1) // 2.

So how do we compute the Hamming distance between two 6-digit codes?

For two strings s1 and s2:

sum(1 for a, b in zip(s1, s2) if a != b)

Yes.

So for each pair of codes, compute that sum, track the minimal.

Now, in Python, for n=1000, there are 1000*999/2 = 499,500 pairs. For each pair, comparing 6 digits is manageable.

But can we optimize this?

Hmm. Let's think. For each code, compare it with every code that comes after it. For each pair, compute the Hamming distance.

Yes.

So the code would look like:

n = int(input())

codes = [input().strip() for _ in range(n)]

if n == 1:

    print(6)

else:

    min_dist = 6  # maximum possible is 6, start with that

    for i in range(n):

        for j in range(i+1, n):

            d = sum(c1 != c2 for c1, c2 in zip(codes[i], codes[j]))

            if d < min_dist:

                min_dist = d

                if min_dist == 1:  # can't get lower, break early

                    break

        if min_dist == 1:

            break

    print( (min_dist -1) // 2 )

Wait, but in the case where min_dist is 1, (1-1)//2 = 0. Which is correct.

But for n=1, output is 6.

Yes.

But why 6? Because when there's only one code, you can make up to 6 errors. For example, the code is 000000. Even if you type in 111111 (all digits wrong), since there are no other codes, it's uniquely identified. So the maximum k is 6.

So that's correct.

Now, what's the time complexity?

For n=1000, the code loops 1000*999/2 = 499500 times. Each loop does 6 comparisons. So 499500 * 6 = 2,997,000 operations. That's acceptable for Python in 1 second.

But perhaps we can optimize further.

Wait, in the code above, once min_dist reaches 1, we can break out early. Because if there's a pair with Hamming distance 1, then the minimal is 1, and no need to check further pairs.

So adding the early break when min_dist becomes 1 is a good optimization. Similarly, if during checking a pair, the current distance is 0 (but the problem states all promo codes are distinct, so this can't happen). But the problem says "all promo codes are distinct", so the minimal distance is at least 1.

So the code can proceed as written.

Testing sample input 1:

n=2, codes are 000000 and 999999. The Hamming distance is 6. So min_dist=6. (6-1)//2 = 5//2=2. Correct.

Sample input 2:

n=6. The minimal pair is 211111 and 212111. Hamming distance is 1. So output (1-1)/2=0. Correct.

So the code works.

Now, let's code this in Python.

Wait, but in the code above, when i and j are being looped, and for each i, j starts from i+1. For each i, j, compute the distance. For each pair, if the distance is less than current min_dist, update min_dist. And if min_dist reaches 1, break early.

Yes.

So here's the code.

Now, the edge case when n=1, output is 6.

Other cases, compute min distance between all pairs, then (d-1)//2.

So the code should look like this.
</think>

```python
n = int(input())
codes = [input().strip() for _ in range(n)]
if n == 1:
    print(6)
else:
    min_dist = 6
    for i in range(n):
        for j in range(i + 1, n):
            current = sum(c1 != c2 for c1, c2 in zip(codes[i], codes[j]))
            if current < min_dist:
                min_dist = current
                if min_dist == 1:
                    break
        if min_dist == 1:
            break
    print((min_dist - 1) // 2)
```