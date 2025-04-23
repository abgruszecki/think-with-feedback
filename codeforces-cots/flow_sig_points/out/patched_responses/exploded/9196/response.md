<think>
Okay, let's tackle this problem. So the problem is about selecting k cards from n to maximize the coins. The coins are calculated by summing for each chosen card the number of times its letter appears in the selected set. So essentially, the total coins are the sum of the squares of the counts of each letter in the selected k cards. Wait, no, let me think. Because for each card i in the chosen set, you add the count of that letter in the chosen set. So if there are m cards of a certain letter, each of those m contributes m to the sum. So total for that letter is m * m. So the total coins is the sum of squares of the counts of each letter in the selected k cards.

So the problem reduces to selecting a subset of k cards such that the sum of squares of their frequencies is maximized. How do we approach this?

Hmm. Let's think of the frequencies. Let's say the letters in the selected subset have frequencies a1, a2, ..., am. Then the sum is a1² + a2² + ... + am². We need to maximize this sum given that the sum of all a's is k.

So this is a classic problem where the maximum sum of squares is achieved by making one of the a's as large as possible and the others as small as possible. Because the square function grows faster when numbers are larger. For example, having 5² + 1² = 26 versus 3² +3²= 18. So the maximum sum is when one of the frequencies is as large as possible, and the remaining are 1 if possible.

So the optimal strategy is to take as many copies as possible of the most frequent letter, then fill the remaining with the next most frequent letters, but in a way that uses up the remaining k count optimally.

Wait, but how exactly? Let's think of an example. Suppose the original letters have counts like in the first sample input: maybe D appears 11 times, F appears a few, etc. Then Toastman takes 9 D's (since 9 is the maximum possible for 10 cards? Wait no, the sample input says 15 10. The input string is DZFDFZDFDDDDDDF. Let's count D's here: let's see the string:

Looking at the input: D Z F D F Z D F D D D D D D F. Wait, maybe not exact, but in the first example, the maximum possible D's is 9. Because when you select 9 D's and 1 other (like F), each D contributes 9 coins, so 9*9 =81, and the F contributes 1, total 82. Which matches the sample output.

So the approach is: select as many of the highest frequency letters as possible, then use the remaining k - x to take either all of the next letters, but maybe in a way that distributes the remaining in 1's. Wait, but how?

The key is that to maximize the sum of squares, we want as many letters as possible to have as high a count as possible. So the optimal is to take the highest frequency letters first, using as much as possible of each, but perhaps not all.

Wait, for example, suppose the letters are A:5, B:4, C:3. And k is 7.

If we take 5 A's, then 2 B's: sum is 5² + 2² =25+4=29.

Alternatively, take 4 B's and 3 C's: 16+9=25. Which is worse.

Alternatively, 4 A's, 3 B's: 16 +9=25, which is worse than 29.

So the maximum is when we take as many as possible from the highest frequency letter, then the next, etc.

So the algorithm should be:

1. Count the frequency of each letter in the input.

2. Sort these frequencies in descending order.

3. Then, select the letters in order of their frequencies, taking as much as possible from each until we reach k.

But how exactly?

Wait, suppose we have frequencies sorted as [a1, a2, a3, ...], where a1 >= a2 >= a3 >= ... 

We need to select k cards. Let's say we take x1 from the first letter, x2 from the second, etc., such that sum(xi) =k, and each xi <= ai.

We want to maximize sum(xi^2).

The way to maximize this is to take as much as possible from the largest available. So the optimal is to take min(a1, k) from the first, then min(a2, remaining k) from the second, etc. But wait, perhaps that's not the case. Let's see.

Wait, no. For example, suppose a1 is 5, a2 is 5, and k is 6. Then taking 5 and 1 gives sum 25 +1 =26. Alternatively, taking 3 and 3 gives 9+9=18. So taking as much as possible from each higher frequency is better.

Another example: a1=3, a2=3, a3=3, k=4. Take 3 from a1, 1 from a2: 9+1=10. Alternatively, 3 from a1, 0 from a2, 1 from a3: same. So the sum is 10. If you take 2 and 2: sum is 4+4=8, which is worse. So the optimal is to take as much as possible from the largest.

So the approach is: greedily take the maximum possible from each frequency in order, until the sum reaches k.

But how to compute this?

Let's think. We sort the frequencies in non-increasing order.

Then, for each frequency in the sorted list, we take as much as possible, given the remaining k.

But what's the process?

Initialize sum_so_far =0.

For each frequency in the sorted list:

   possible = min(freq, remaining_k)

   sum_so_far += possible^2

   remaining_k -= possible

   if remaining_k ==0: break

So this is the approach.

Wait, but in the first sample input:

The letters are D, F, Z. Let's see the input string. Let me count:

Original input is "DZFDFZDFDDDDDDF". Let's count D's.

Looking at each character:

Positions:

1: D

2: Z

3: F

4: D

5: F

6: Z

7: D

8: F

9: D

10: D

11: D

12: D

13: D

14: D

15: F

So D appears in positions 1,4,7,9,10,11,12,13,14. That's 9 times? Wait 1 is D, 4 is D, 7 is D, 9 is D, 10 is D, 11 D, 12 D, 13 D, 14 D. So that's 9 D's. Then F's are at 3,5,8,15. So 4 F's. Z's at 2 and 6. So 2 Z's.

So the sorted frequencies are D:9, F:4, Z:2. But n is 15 here. Then k is 10. So we take as much as possible from the highest frequencies.

Take 9 D's (since 9 is the frequency, but k is 10, so 9 is possible). Then remaining_k is 1. Then next is F:4. Take 1. So sum is 9² +1² = 81+1=82. Which matches the sample.

So this approach works.

Another example: input is YJSNPI, which is 6 letters. n=6, k=4.

Letters: Y, J, S, N, P, I. Each occurs once. So sorted frequencies are [1,1,1,1,1,1]. We need to take 4. So take 1 from each of the first four. Sum is 1+1+1+1=4. Which matches the sample.

So the algorithm works.

So the steps are:

1. Count the frequencies of each character in the input string.

2. Sort the frequencies in non-increasing order.

3. Iterate through the sorted list, taking as much as possible from each frequency (up to the remaining k needed) until we've taken k total.

4. Sum the squares of each taken count.

So how to implement this?

In Python, first, we can count the frequencies using a Counter. Then, we sort the values in descending order.

Then, for each frequency in this list, we take min(frequency, remaining k) as the count, add its square to the total, subtract that from remaining k, and proceed until remaining k is 0.

Yes. That's straightforward.

Now, considering the constraints.

n can be up to 1e5, and k up to 1e5. But the frequencies sorted would be O(n log n) time, which is acceptable. The rest is O(m), where m is the number of distinct letters. But since m can be up to 26 (since all are uppercase letters), the loop over the frequencies is O(26) steps. So overall the time is acceptable.

So the code steps:

Read n and k.

Read the string.

Count the frequencies using collections.Counter.

Sort the frequency values in reverse order.

Initialize remaining_k =k, total=0.

For each freq in sorted_freqs:

   take = min(freq, remaining_k)

   total += take * take

   remaining_k -= take

   if remaining_k ==0:

       break

Output the total.

Yes, that's the code.

Wait, but the problem says that the letters are given as a single string without spaces. So for example, in the second sample input, the input is "YJSNPI", which is 6 letters. The code would count each as 1.

Now, the code needs to read the input correctly.

In Python, the code would be:

Testing against sample input 1.

```python
from collections import Counter


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    s = input_stream.readline().rstrip("\n").strip()

    counts = Counter(s)

    freqs = sorted(counts.values(), reverse=True)

    total = 0

    remaining = k

    for f in freqs:

        take = min(f, remaining)

        total += take * take

        remaining -= take

        if remaining ==0:

            break

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 4
YJSNPI
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

Second sample input: counts are all 1. sorted as [1,1,1,1,1,1]. k=4. take 1,1,1,1. sum 4.

Which matches.

So the code works.

In terms of time and memory:

The Counter is O(n) time, which for n=1e5 is acceptable. Sorting 26 elements (since uppercase letters are 26 possible) takes O(1) time. So the code is optimal.

So this is the correct approach.
</think>

```python
from collections import Counter

n, k = map(int, input().split())
s = input().strip()
counts = Counter(s)
freqs = sorted(counts.values(), reverse=True)
total = 0
remaining = k
for f in freqs:
    take = min(f, remaining)
    total += take * take
    remaining -= take
    if remaining == 0:
        break
print(total)
```
