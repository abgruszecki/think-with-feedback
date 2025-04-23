<think>
Okay, let's tackle this problem. So, the task is to find for each possible diversity k (from 1 up to the total diversity of the string) the number of substrings that have exactly k distinct characters. The string can be up to 3e5 characters long, which is pretty big. So, we need an efficient approach here.

First, I need to understand what the total diversity is. The total diversity d(s) is just the number of unique characters in the entire string. For example, if the string is 'abca', then d(s) is 3 because there's a, b, c. So, the first part is easy: compute the number of unique characters in the string.

The main challenge is calculating the number of substrings with exactly k distinct characters for each k from 1 to d(s). But how to do this efficiently?

Let me think about possible approaches. The brute-force approach would be to check all possible substrings, count their distinct characters, and accumulate the counts. But that's O(n^2) for the number of substrings, which is way too slow for n=3e5. So we need a smarter method.

I remember that there's a sliding window technique for finding the number of substrings with at most k distinct characters. Then, using inclusion-exclusion, we can find the number of substrings with exactly k by subtracting the count of at most (k-1) from at most k. But wait, how does that work here?

Wait, the standard approach for exactly k is to compute (number of substrings with at most k) minus (number with at most k-1). But since we need to compute for all k from 1 to d(s), maybe we can compute the at most counts for each possible k and then derive the exact counts.

But let's think about this. For each k, the exact number is at_most_k - at_most_{k-1}. But how to compute at_most_k for all k up to d(s) efficiently?

But even if we can compute at_most for all k, the problem is that for each k from 1 to d(s), we need to calculate exactly. So first, compute for each k the number of substrings with at most k distinct characters, then subtract the at_most (k-1) to get exactly k.

But for that, we need to compute at_most for 0 (which is zero) up to d(s). Then, the exact count for k is at_most[k] - at_most[k-1].

So the plan could be:

1. Find d(s), the total number of distinct characters in s.
2. For each k in 1 to d(s):
   a. Compute the number of substrings with exactly k distinct characters by using at_most[k] - at_most[k-1].
3. Output the counts.

The key then is to compute the at_most[k] efficiently for all required k. But how?

The standard sliding window approach for at_most k distinct is O(n) per k. But for k up to d(s), which could be up to 26 (since the characters are lowercase letters), that would be O(26n) = O(n), which is acceptable for n=3e5. Because 26 * 3e5 is 7.8e6 operations, which is manageable.

Wait, but in the worst case, if d(s) is 26, then we need to run the sliding window 26 times. Each sliding window is O(n). So total time is O(26n) which is acceptable.

So this approach is feasible.

So, let's outline the steps:

- Compute the total distinct count, d.
- For each k from 1 to d, compute the number of substrings with at most k distinct characters. Then, for each k, the exact count is at_most[k] - at_most[k-1]. But wait, no. Because when we compute at_most(k), that's the sum of all substrings with 1 to k distinct. So exactly k is the difference between at_most(k) and at_most(k-1).

Therefore, to get exactly k, for each k from 1 to d, we need to compute at_most(k) - at_most(k-1). Here, at_most(0) is 0.

So the plan is:

Compute for each k in 1..d:

exact_k = at_most(k) - at_most(k-1)

But how do we compute at_most(k) for each k? Let's recall the sliding window approach for at_most k distinct.

The sliding window approach for at_most k distinct:

Initialize left=0, right=0. Use a frequency map. For each right, add the character to the map. If the number of keys exceeds k, move left forward until the count is <=k. Then, the number of valid substrings ending at right is (right - left + 1). Accumulate this sum.

This is O(n) per k.

So for each k from 1 to d, run this sliding window once. Then compute the exact counts.

But when d is up to 26, this is 26 * O(n) operations. For n=3e5, that's 7.8e6 steps, which is acceptable.

So this approach is feasible.

Now, implementing this:

First, compute the total distinct characters in s. That's easy: len(set(s)).

Then, for each k in 1 to d:

   compute the number of substrings with at most k distinct characters.

Then, for each k, exact = at_most_k - at_most_{k-1}.

But how to compute at_most_k for each k? Let's code the sliding window function.

Implement a function that, given a maximum allowed distinct characters (k), returns the number of substrings with at most k distinct.

Implementing this function:

def count_at_most_k(s, k):
    count = {}
    left = 0
    res = 0
    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        while len(count) > k:
            left_char = s[left]
            count[left_char] -= 1
            if count[left_char] == 0:
                del count[left_char]
            left += 1
        res += right - left + 1
    return res

This function is O(n), as each character is added once and removed once.

Then, for each k from 1 to d, compute at_most_k and at_most_{k-1}.

But when k is 1, at_most_0 is 0. So:

exact_1 = at_most(1) - at_most(0) → which is at_most(1) - 0 = at_most(1).

So the code would be:

Compute all at_most for 0 up to d.

But since at_most(0) is zero, we can compute:

d_total = len(set(s))

at_most = [0] * (d_total + 1)  # indexes 0 to d_total

for k in 1 to d_total:
    at_most[k] = count_at_most_k(s, k)

Then, the exact counts are:

exact = [0] * (d_total + 1)
for k in 1 to d_total:
    exact[k] = at_most[k] - at_most[k-1]

Then, output d_total, followed by exact[1], exact[2], ..., exact[d_total]

But for the constraints, when the string is up to 3e5 characters and d_total is 26, this approach would be O(26*3e5) = 7.8e6 operations. Which should fit within the 1 second time limit.

But wait, even 3e5 per k=26 would be 7.8e6 steps, which is acceptable.

But in Python, each loop iteration is slower than in C++. So for 7.8e6 steps, would that be acceptable? Let's see: Python can handle about 1e8 operations per second (rough estimate). 7.8e6 is manageable.

So this approach should work.

But let's test with the sample input.

Sample Input 1: 'abca' → d=3.

Compute at_most(1):

For substrings with at most 1 distinct char. How many?

Looking at the example:

The individual 'a', 'b', 'c', 'a' → 4 substrings. Then, any longer substrings would have more than 1 distinct. So for k=1, at_most(1) is 4.

But according to the function, let's see:

The code would process each right, and for each step, count the number of substrings ending at right with at most 1 distinct.

For 'a', 'b', 'c', 'a':

At right=0 (char 'a'), left is 0. count is {'a':1}. res += 1 → res=1.

right=1 (char 'b'). count becomes {'a':1, 'b':1} → len(count)=2>1. So move left until len(count) <=1. So delete 'a' (count becomes {'b':1}), left=1. res += 1 → res=2.

right=2 (char 'c'). count becomes {'b':1, 'c':1} → len=2>1. Move left to 2. res +=1 → res=3.

right=3 (char 'a'). count becomes {'c':1, 'a':1} → len=2>1. Move left to 3. res +=1 → res=4.

So total at_most(1) is 4.

Then at_most(2) is the number of substrings with at most 2 distinct.

In the sample, the total substrings are 10. The exact counts for 1 is 4, for 2 is 3, and for 3 is 3. So at_most(2) is 4 (exact1) +3 (exact2) + ... Wait, no. Wait, the sum of at_most(k) is the number of substrings with at most k distinct.

So for k=2, the function would count all substrings with 1 or 2 distinct.

In the sample, the exact counts are 4 (k=1), 3 (k=2), 3 (k=3). So at_most(2) is 4+3=7. Then at_most(3) is 10 (all substrings). Then:

exact1 = 4-0 =4

exact2 =7-4=3

exact3=10-7=3

Which matches the sample output.

So this approach works for the sample.

Now, the problem is to code this in Python.

But what about the time when d(s) is 26? Let's see. For each k from 1 to 26, the code runs the sliding window function. Each of those functions is O(n). So total time is O(26n). For n=3e5, 26*3e5=7.8e6 steps. Each step is a few operations, which should be manageable.

But in Python, the sliding window implementation can be optimized.

Wait, the current code for count_at_most_k uses a dictionary to track the count of each character. But for each character access, we have to check if it's in the dictionary, and then increment. Also, when moving the left pointer, we have to decrement counts and possibly delete entries. This can be slow for large n.

An alternative is to use a fixed-size array for counts, since the characters are limited to lowercase letters. So instead of a dictionary, we can use an array of size 26, with indices 0-25 representing 'a'-'z'.

This might be faster in practice, as array accesses are O(1) and avoid the overhead of hash tables.

So modifying the count_at_most_k function:

We can use a list of size 26, initialized to 0. For each character, convert it to an index (ord(c) - ord('a')). Then, track the current number of distinct characters (current_distinct).

Each time a character is added to the window:

- if the count was zero before, current_distinct increases by 1.

Each time a character is removed from the window (when moving left):

- if the count becomes zero after decrement, current_distinct decreases by 1.

This way, we can avoid checking len(count) (which for a dictionary is O(1) but in practice, maybe using current_distinct as a variable is faster).

So here's the revised function:

def count_at_most_k(s, k):
    count = [0] * 26
    current_distinct = 0
    left = 0
    res = 0
    for right in range(len(s)):
        c = ord(s[right]) - ord('a')
        if count[c] == 0:
            current_distinct += 1
        count[c] += 1
        while current_distinct > k:
            left_c = ord(s[left]) - ord('a')
            count[left_c] -= 1
            if count[left_c] == 0:
                current_distinct -= 1
            left += 1
        res += right - left + 1
    return res

This should be more efficient as it uses a fixed-size array and tracks current_distinct explicitly.

This could save time in the inner loop, which is important for Python.

Now, the code would proceed as:

Compute d_total = len(set(s)).

Then, precompute at_most for all k from 1 to d_total.

Then compute exact[k] as at_most[k] - at_most[k-1].

But how to handle the at_most array.

Wait, since we need to compute for each k in 1 to d_total, the function count_at_most_k(s, k).

But the code will call this function for each k from 1 to d_total.

So the steps are:

s = input().strip()

d_total = len(set(s))

if d_total ==0:
    # but s can't be empty per problem constraints
    pass

at_most = [0]*(d_total+1)

for k in range(1, d_total+1):
    at_most[k] = count_at_most_k(s, k)

exact = [0]*(d_total+1)
for k in range(1, d_total+1):
    exact[k] = at_most[k] - at_most[k-1]

print(d_total)
for k in range(1, d_total+1):
    print(exact[k])

But wait, for k=1 to d_total.

Now, the problem is that for large d_total (like 26), this loop could take some time, but as discussed earlier, it's manageable.

Testing the first sample:

Input: 'abca' → d_total=3.

Call count_at_most_k for k=1, 2, 3.

k=1: returns 4.

k=2: returns 7.

k=3: returns 10.

So exact[1] =4-0=4; exact[2]=7-4=3; exact[3]=10-7=3. Which matches the sample.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    if not s:
        print(0, file=output_stream)
        return

    pre_s = [ord(c) - ord('a') for c in s]
    d_total = len(set(pre_s))

    def count_at_most_k(pre_s, k):
        count = [0] * 26
        current_distinct = 0
        left = 0
        res = 0
        for right in range(len(pre_s)):
            c = pre_s[right]
            if count[c] == 0:
                current_distinct += 1
            count[c] += 1
            while current_distinct > k:
                left_c = pre_s[left]
                count[left_c] -= 1
                if count[left_c] == 0:
                    current_distinct -= 1
                left += 1
            res += right - left + 1
        return res

    at_most = [0] * (d_total + 1)
    for k in range(1, d_total + 1):
        at_most[k] = count_at_most_k(pre_s, k)

    exact = [0] * (d_total + 1)
    for k in range(1, d_total + 1):
        exact[k] = at_most[k] - at_most[k-1]

    print(d_total, file=output_stream)
    for k in range(1, d_total + 1):
        print(exact[k], file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
aabacaabbad
""",
            "output": \
"""\
4
14
19
28
5
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

So the code works.

Another possible optimization: since the problem requires exactly k, and for k>d(s), there's no substrings. So we can ignore those.

But the code is already handling that by only processing up to d_total.

Thus, the code should be correct and efficient.
</think>

```python
s = input().strip()
if not s:
    print(0)
    exit()

pre_s = [ord(c) - ord('a') for c in s]
d_total = len(set(pre_s))

def count_at_most_k(pre_s, k):
    count = [0] * 26
    current_distinct = 0
    left = 0
    res = 0
    for right in range(len(pre_s)):
        c = pre_s[right]
        if count[c] == 0:
            current_distinct += 1
        count[c] += 1
        while current_distinct > k:
            left_c = pre_s[left]
            count[left_c] -= 1
            if count[left_c] == 0:
                current_distinct -= 1
            left += 1
        res += right - left + 1
    return res

at_most = [0] * (d_total + 1)
for k in range(1, d_total + 1):
    at_most[k] = count_at_most_k(pre_s, k)

exact = [0] * (d_total + 1)
for k in range(1, d_total + 1):
    exact[k] = at_most[k] - at_most[k-1]

print(d_total)
for k in range(1, d_total + 1):
    print(exact[k])
```
