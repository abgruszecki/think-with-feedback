<think>
Okay, let's see. The problem is about finding the number of good candies. A good candy is one that, when removed, causes the sum of the even days to equal the sum of the odd days in the remaining sequence. 

Hmm, let's break it down. For each candy i, when it's removed, the remaining candies are eaten in order, with their original numbering. But the days are counted based on their new sequence. Wait, the days are determined by the order after removal. So, if the original indices are 1,2,3,4 and we remove 2, the remaining are 1,3,4. Then the days are day 1 (1), day 2 (3), day3 (4). So the odd days are 1 and 3 (sum a1 + a4?), wait no. Wait, the days are numbered based on the order of the remaining candies. So, the first candy in the remaining list is day 1 (odd), second is day 2 (even), etc. 

So for each i, when we remove the i-th candy, the remaining list is all the candies except a_i, in the original order. Then the sum of the odd days (positions 1,3,5...) and even days (positions 2,4,6...) should be equal.

Our task is to compute how many such i's exist.

The constraints are n up to 2e5, which means O(n) solutions are needed, O(n^2) is too slow.

So, the brute force approach is to iterate each i, compute the sum of odd and even days when i is removed, and check if they are equal. But for n=2e5, this would be O(n^2) time, which is way too slow.

We need a smarter approach. Let's think about precomputing some prefix sums that allow us to calculate the required sums efficiently for each i.

Let's model the problem. When we remove the i-th candy, the remaining candies are [1,2,...,i-1, i+1,...,n]. The order is preserved. Now, when we process these candies, their positions in the new sequence will determine whether they contribute to the even or odd sum.

The key insight here is to figure out how the removal of a candy affects the parity of the positions of the remaining candies.

For example, candies before i (i.e., 1 to i-1) are in the new sequence as before, but their positions in the new sequence depend on how many candies are before them. Candies after i (i+1 to n) will have their positions in the new sequence shifted left by one, which affects their parity.

Wait, let's think about each element's original index and whether their position in the new sequence is even or odd.

Suppose we have a candy j. If j is less than i, then in the new sequence, its position is j's original position minus the number of elements removed before j. But since we're removing exactly one element (i), and j < i, the position of j in the new sequence is j - (number of removed elements before j), which is j - 0, since j is before i and the only removed element is i. So j's position in the new sequence is j, but only up to i-1. Then, the elements after i (k > i) have their position in the new sequence as k-1 (since one element before them is removed). 

Wait, no. Let's take an example. Original indices 1,2,3,4,5. If we remove i=3, the new sequence is 1,2,4,5. The positions in the new sequence are 1,2,3,4. So for elements before i (1 and 2), their new positions are same as their original. For elements after i (4,5), their new positions are original position minus 1 (since i was removed). So, their parity may change. For example, original 4 was position 4 (even) but in new sequence it's position 3 (odd). So when we remove i, the elements after i have their parity flipped in the new sequence.

So, when we remove a candy at position i:

- For all j < i: their new position is j. So the parity is same as their original position in the full array (since the number of elements before them is j-1, which doesn't change, so parity is even or odd based on j's original position).
- For all j > i: their new position is j-1. So the parity of j in the new sequence is (original position j - 1) parity. So if j was even in original array (j even), then j-1 is odd. If j was odd, j-1 is even. So for elements after i, their contribution to the sum (whether they are added to even or odd sum) is flipped.

But in the original array (without removing i), each j's parity is determined by their original position. When we remove i, the j's after i have their parity flipped.

Therefore, the sum can be calculated as:

sum_even = sum of a_j for j < i, j even (original even positions) + sum of a_j for j >i, where (j-1) is even (original j even? Wait, j-1's parity depends on j. Let's think:

For j > i:

In the new sequence, their position is j-1 (since we removed i). So the parity is (j-1) % 2. So if j-1 is even (i.e., j is odd), then it's even day. If j-1 is odd (j even), then it's odd day.

So for j > i:

if (j-1) is even → even day → contribute to even sum. So j must be odd (since j-1 even implies j is odd). So j is odd → contributes to even sum in new sequence.

Wait, j-1 even → j-1 % 2 == 0 → j is odd.

Similarly, j-1 odd → j is even → contributes to odd sum in new sequence.

But in the original array, j's parity was j % 2.

So, for j > i, their contribution depends on (j-1) % 2.

So, when removing i, the even sum is:

sum_even = sum of original even positions before i + sum of original j's where j >i and (j-1) is even (i.e., j is odd) → which in original terms were odd positions, but in the new sequence they are even positions.

Similarly for the odd sum.

So the total even sum when removing i is:

sum_even = (sum_even_before_i) + (sum_odd_after_i).

Because for j > i, if (j-1) is even (j is odd), then in the new sequence they are even days. But j was originally odd, so sum_odd_after_i is sum of j >i where j is odd. Similarly, the sum_odd_after_i is the sum of j's where j is odd and j >i.

Wait, maybe not. Let's clarify:

In the new sequence, j >i have their new position as j-1. So the parity is (j-1) % 2. For j >i:

- If (j-1) is even → even day → add to even sum. So j-1 is even → j is odd.

- If (j-1) is odd → odd day → add to odd sum. So j is even.

So the sum_even for j >i is the sum of all j >i where j is odd.

The sum_odd for j >i is the sum of all j >i where j is even.

So when we remove i, the even sum is:

sum_even = sum_even_before_i (since j <i, their parity is original even) + sum_odd_after_i (since j >i and j is odd → (j-1) even → even day).

Similarly, the odd sum is sum_odd_before_i (original j <i and j is odd) + sum_even_after_i (j> i and j even → (j-1) is odd → odd day).

Therefore, for each i, the even_sum is even_before_i + odd_after_i, and the odd_sum is odd_before_i + even_after_i.

If even_sum equals odd_sum, then i is a good candy.

So the problem reduces to precomputing prefix sums for even and odd positions, and suffix sums for even and odd positions.

Let me define:

prefix_even[i] = sum of a_j for j <i and j is even.

prefix_odd[i] = sum of a_j for j <i and j is odd.

Similarly, suffix_even[i] = sum of a_j for j >=i and j is even.

suffix_odd[i] = sum of a_j for j >=i and j is odd.

Wait, but how to compute these suffix sums? For example, suffix_even[i] would be sum of a_j for j >=i where j is even. Similarly for suffix_odd[i].

Once we have these prefix and suffix arrays, for each i, we can compute:

even_sum = prefix_even[i] + (suffix_odd[i+1] if i+1 <=n else 0)

Because j >i → j starts from i+1 to n. So the sum_odd_after_i is sum of a_j where j >i and j is odd → which is suffix_odd[i+1].

Similarly, odd_sum = prefix_odd[i] + suffix_even[i+1]

Then, we check if even_sum == odd_sum.

So the steps are:

1. Precompute prefix_even and prefix_odd arrays. prefix_even[i] is the sum of even-indexed elements (original positions) up to i-1. Similarly for prefix_odd.

Wait, but indices are from 1 to n. So for each i (1-based), prefix_even[i] is sum of a_j where j is even and j <i.

For example, prefix_even[1] = 0 (no elements before 1). prefix_even[3] is a_2.

Similarly, prefix_odd[i] is sum of a_j where j is odd and j <i.

Similarly, suffix_even[i] is sum of a_j where j >=i and j even. So suffix_even[1] is sum of all even positions.

Suffix_odd[i] is sum of a_j where j >=i and j odd.

So for each i, the sum_odd_after_i (elements j>i and j is odd) is suffix_odd[i+1], assuming i+1 <=n.

So, for each i:

even_sum = prefix_even[i] + suffix_odd[i+1]

odd_sum = prefix_odd[i] + suffix_even[i+1]

We need to check if even_sum == odd_sum.

If yes, count that i as a good candy.

So the plan is:

- Compute prefix_even and prefix_odd arrays.

- Compute suffix_even and suffix_odd arrays.

- Iterate each i from 1 to n, compute even_sum and odd_sum as above, check equality, increment count if so.

This would be O(n) time, which is acceptable for n=2e5.

Now, how to compute the prefix and suffix arrays.

For prefix_even and prefix_odd:

We can initialize prefix_even as an array of size n+2 (since i ranges from 1 to n, and prefix_even[i] is sum up to i-1). Similarly for prefix_odd.

prefix_even[1] = 0.

For i from 1 to n:

prefix_even[i] = prefix_even[i-1] + (a[i-1] if (i-1) is even ?)

Wait, since the original indices are 1-based. So in code, perhaps the list a is 0-based (since in Python, lists are 0-based). So when the original problem says the first element is a_1, in the code it's a[0].

So for j in 1-based index, a[j-1] is the element.

So, for j from 1 to n:

if j is even, then a[j-1] contributes to prefix_even.

So for i in 1-based:

prefix_even[i] = prefix_even[i-1] + (a[i-2] if (i-1) is even? Wait, perhaps not.

Wait, prefix_even[i] is the sum of even j <i. So j is even and j <i.

For example, for i=3, j can be 2. So j=2 <3.

But in code, for i=3 (1-based), j runs from 1 to i-1. Wait, no. Wait, j is the original positions. So j can be 1,2,3, etc. For prefix_even[i], it's sum of all j in 1..i-1 where j is even.

So for each i, j ranges from 1 to i-1.

So for each i in 1-based:

prefix_even[i] = prefix_even[i-1] + (a[j-1] if j is even, else 0), where j is the current i-1?

Wait, no. Let me think again.

The prefix_even array is built incrementally. For i=1, there are no elements before, so prefix_even[1] = 0.

For i=2, j can be 1. But j=1 is odd, so prefix_even[2] = prefix_even[1] + 0 =0.

Wait, no. Wait, when i=2, the elements before i (i.e., less than 2) is j=1. j is 1, which is odd. So prefix_even[2] remains 0.

For i=3, elements before are j=1 and 2. j=2 is even. So prefix_even[3] = prefix_even[2] + a[1] (since j=2 is even, and a[1] is the 2nd element in 1-based, which is a[1] in 0-based).

So the way to compute prefix_even and prefix_odd is:

prefix_even[0] = 0 (for i=0?), but maybe better to use 1-based.

Initialize prefix_even as [0]*(n+2), same for prefix_odd.

Then, for each i from 1 to n:

current_j = i-1 (since i is 1-based). Wait, no. Wait, i is the current index for the prefix array. Wait, perhaps the prefix arrays are 1-based. So for each position i in the prefix array (1-based), prefix_even[i] is the sum of even j's that are <i.

So for i=1, there are no j <1. So sum is 0.

For i=2, j can be 1. 1 is odd, so sum remains 0.

For i=3, j can be 1 and 2. j=2 is even, so add a[1].

So the approach is:

for each i in 1..n:

   prefix_even[i] = prefix_even[i-1]

   prefix_odd[i] = prefix_odd[i-1]

   j = i-1  # because the current i is the upper bound (sum j <i). So the j-th element (1-based) is the element a[i-2] in 0-based? Wait, perhaps I'm getting mixed up.

Wait, let's clarify:

The prefix_even[i] is the sum of all elements in positions j (1-based) that are even and j <i.

So j can be 2,4,6... up to i-1.

For example, for i=5 (1-based), the elements considered are j=2,4 (since j must be even and <5).

So in code, for each i (1-based), we can check if (i-1) is even. Because when we are building prefix_even[i], we are adding the element at j=i-1 (since j is up to i-1).

Wait, perhaps it's easier to loop through all j from 1 to n, and for each j, update prefix_even and prefix_odd for i = j+1.

For example:

Initialize prefix_even and prefix_odd arrays of size n+2, initialized to 0.

For j from 1 to n:

   if j is even:

       prefix_even[j+1] = prefix_even[j] + a[j-1]

       prefix_odd[j+1] = prefix_odd[j]

   else:

       prefix_odd[j+1] = prefix_odd[j] + a[j-1]

       prefix_even[j+1] = prefix_even[j]

Wait, this way, for each j (1-based), we compute the prefix sums up to j. Then, for i = j+1, prefix_even[i] is the sum of even j's up to j. Because j <i.

Yes, that makes sense.

For example, j=1 (odd):

prefix_even[2] = prefix_even[1] (0) → remains 0.

prefix_odd[2] = prefix_odd[1] (0) + a[0] → a[0].

Then j=2 (even):

prefix_even[3] = prefix_even[2] (0) + a[1].

prefix_odd[3] = prefix_odd[2] (a[0]).

And so on.

So for each j in 1..n, we update the prefix arrays for j+1.

So the code for prefix_even and prefix_odd can be built in O(n) time.

Similarly, the suffix_even and suffix_odd arrays can be built.

For the suffix arrays:

suffix_even[i] is sum of a_j for j >=i where j is even.

Similarly for suffix_odd[i].

We can compute these by iterating from n downto 1.

Initialize suffix_even and suffix_odd as arrays of size n+2, initialized to 0.

For j from n downto 1:

   if j is even:

       suffix_even[j] = suffix_even[j+1] + a[j-1]

       suffix_odd[j] = suffix_odd[j+1]

   else:

       suffix_odd[j] = suffix_odd[j+1] + a[j-1]

       suffix_even[j] = suffix_even[j+1]

So for j=4 (even):

suffix_even[4] = suffix_even[5] (0) + a[3]

suffix_odd[4] = 0.

For j=3 (odd):

suffix_odd[3] = suffix_odd[4] (0) + a[2]

suffix_even[3] = suffix_even[4] (a[3]).

So suffix_even[i] accumulates all even j's >=i.

Once these arrays are built, for each i in 1..n:

even_sum = prefix_even[i] + suffix_odd[i+1]

odd_sum = prefix_odd[i] + suffix_even[i+1]

Because:

- prefix_even[i] is the sum of even j's <i.

- suffix_odd[i+1] is the sum of odd j's >=i+1 (since i+1 is the next j after i).

Similarly, prefix_odd[i] is sum of odd j's <i.

suffix_even[i+1] is sum of even j's >=i+1.

So if even_sum == odd_sum, then this i is a good candy.

Now, the code steps:

Read n.

Read a as a list of integers (probably 0-based in code).

Compute prefix_even and prefix_odd.

Compute suffix_even and suffix_odd.

Initialize count to 0.

For each i in 1..n:

   even = prefix_even[i] + (suffix_odd[i+1] if i+1 <=n else 0)

   odd = prefix_odd[i] + (suffix_even[i+1] if i+1 <=n else 0)

   if even == odd:

       count +=1

Return count.

So the code should handle cases where i is the last element (i+1 >n), so suffix_odd[i+1] would be 0.

Now, the code for this in Python.

But since n can be up to 2e5, we need to precompute these arrays efficiently.

Let's see how to code the prefix and suffix arrays.

Sample code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    prefix_even = [0] * (n + 2)
    prefix_odd = [0] * (n + 2)

    for j in range(1, n+1):
        if j % 2 == 0:
            prefix_even[j+1] = prefix_even[j] + a[j-1]
            prefix_odd[j+1] = prefix_odd[j]
        else:
            prefix_odd[j+1] = prefix_odd[j] + a[j-1]
            prefix_even[j+1] = prefix_even[j]

    suffix_even = [0] * (n + 2)
    suffix_odd = [0] * (n + 2)

    for j in range(n, 0, -1):
        if j % 2 == 0:
            suffix_even[j] = suffix_even[j+1] + a[j-1]
            suffix_odd[j] = suffix_odd[j+1]
        else:
            suffix_odd[j] = suffix_odd[j+1] + a[j-1]
            suffix_even[j] = suffix_even[j+1]

    count = 0
    for i in range(1, n+1):
        even_sum = prefix_even[i] + suffix_odd[i+1]
        odd_sum = prefix_odd[i] + suffix_even[i+1]
        if even_sum == odd_sum:
            count +=1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
4 8 8 7 8 4 4 5
""",
            "output": \
"""\
2
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

So the code should work.

Now, considering time and memory:

Each of the prefix and suffix arrays is O(n), which is acceptable for 2e5.

The code runs in O(n) time, which is acceptable.

So this approach is optimal.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

prefix_even = [0] * (n + 2)
prefix_odd = [0] * (n + 2)

for j in range(1, n + 1):
    if j % 2 == 0:
        prefix_even[j + 1] = prefix_even[j] + a[j - 1]
        prefix_odd[j + 1] = prefix_odd[j]
    else:
        prefix_odd[j + 1] = prefix_odd[j] + a[j - 1]
        prefix_even[j + 1] = prefix_even[j]

suffix_even = [0] * (n + 2)
suffix_odd = [0] * (n + 2)

for j in range(n, 0, -1):
    if j % 2 == 0:
        suffix_even[j] = suffix_even[j + 1] + a[j - 1]
        suffix_odd[j] = suffix_odd[j + 1]
    else:
        suffix_odd[j] = suffix_odd[j + 1] + a[j - 1]
        suffix_even[j] = suffix_even[j + 1]

count = 0
for i in range(1, n + 1):
    even_sum = prefix_even[i] + suffix_odd[i + 1]
    odd_sum = prefix_odd[i] + suffix_even[i + 1]
    if even_sum == odd_sum:
        count += 1

print(count)
```
