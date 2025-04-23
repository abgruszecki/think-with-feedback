<think>
Okay, let's see. The problem is about lamps and keys. Pressing a key toggles certain lamps. The key i when pressed toggles all lamps x where i divides x. So for each key press in the list, I need to flip the state of those lamps. Then, after all the key presses, output the final states.

Hmm. The challenge here is handling this efficiently, especially when n is up to 1e5 and k up to 1e4. Because if we naively process each key press by iterating through all multiples of i (the key number), then for each key, we could be doing O(n/i) operations. But when i is 1, that's n operations. And if k is 1e4, and each key is 1, that's 1e4 * 1e5 = 1e9 operations, which would be way too slow. That's definitely not going to work.

Wait, but maybe there's a smarter way. Let's think about the fact that flipping a lamp an even number of times cancels out. So for each lamp x, the number of times it's toggled is equal to the number of keys that are divisors of x. Because each key i pressed adds 1 if i divides x. So for each lamp x, the total toggles is the count of how many keys pressed are divisors of x.

If this count is even, the lamp's state remains the same as initial. If odd, it's flipped.

Ah, right! So the key insight here is that instead of processing each key press and flipping all multiples of i, which is O(k * n/i) time, we can instead for each lamp x, compute how many times it was toggled by the keys, which is the number of keys in the list that divides x. Then, for each x, if the count is even, no change; odd, flip.

So the problem reduces to, for each x in 1..n, count the number of keys pressed that are divisors of x, and determine if that count is odd or even.

So the steps would be:

1. Read the initial states of the lamps.

2. Read the list of keys pressed, which is a list of integers (possibly with duplicates).

3. For each key in the list, count the number of times each key i is pressed. But since flipping is a binary toggle (even/odd), what matters is whether the count for each i is even or odd. Wait, no. Because each time a key is pressed, it's another toggle. So for example, if key 2 is pressed 3 times, that's equivalent to pressing it once. So for each key i, we can track the parity (even or odd) of the number of times it was pressed. Because pressing it even times cancels out.

So first, we can create a frequency map for each key i, and then take mod 2 of the frequency. Then, the effective keys are those with a non-zero mod 2 (i.e., pressed an odd number of times). So the problem reduces to: the set of keys that were pressed an odd number of times.

So the actual effective key presses are the keys that have been pressed an odd number of times. So for each key i in the list, count how many times it appears, mod 2. Then, the effective keys are those i where this is 1. Then, for each lamp x, count the number of effective keys that are divisors of x.

So the plan is:

- For all keys pressed, compute their frequency modulo 2. So any key that's pressed even times can be ignored, and those pressed odd times are considered once.

- Then, for each lamp x (from 1 to n), compute the number of divisors of x that are present in the effective keys. If that count is even, the lamp's state remains as initial. If odd, it's flipped.

So the problem now is, for each x in 1..n, count the number of divisors of x that are in the set S (effective keys).

Now, how to compute this efficiently for all x from 1 to n?

The straightforward approach would be, for each x, iterate through all its divisors and check if they are in S. But for x up to 1e5, and each x having up to O(sqrt(x)) divisors, this could be O(n * sqrt(n)), which for n=1e5 would be 1e5 * 300 (approx sqrt(1e5)) = 3e7 operations, which is manageable within the time constraints.

But 3e7 operations might be tight, but perhaps manageable. Let's check: 1e5 elements, each with up to 1000 divisors (though in reality, numbers up to 1e5 have at most a few hundred divisors). Wait, no. For example, 1e5 has divisors 1, 2, 4, 5, 8, 10, etc. The maximum number of divisors for a number up to 1e5 is like 1000? Maybe not. The number with the most divisors under 1e5 is 83160 with 128 divisors. So per x, up to 100 divisors. So 1e5 * 100 = 1e7 operations, which is acceptable.

But perhaps there's a smarter way. Let's think about it.

Alternative approach: for each effective key i in S, iterate through all multiples of i (i.e., x = i, 2i, 3i, ..., up to n), and for each x, increment a counter (mod 2) that represents the number of toggles. Because each key i in S contributes to all x that are multiples of i. Then, the total number of times x is toggled is the sum over i in S of 1 if i divides x. So for each i in S, we can add 1 to all multiples of i, and then check if the sum is even or odd.

Wait, that's similar to the sieve approach. For example, for each i in S, mark all multiples of i. For each x, the count is the number of times x was marked.

But since the count is mod 2, the parity is what's important. So this can be represented as a binary array, where each i in S flips the parity for all multiples of i.

So the algorithm would be:

1. Initialize an array toggle_count of size n+1 (since x is 1-based) with all zeros. This array will track the parity of the number of toggles for each x.

2. For each effective key i in S:
   a. Iterate through all multiples of i (x = i, 2i, 3i, ..., up to n)
   b. For each x, toggle_count[x] ^= 1 (since each occurrence of i adds 1 to the count mod 2)

3. After processing all keys in S, for each x, if toggle_count[x] is 1, then the lamp's state is flipped; otherwise, it remains as initial.

This approach would be O(k_effective * n/i), but since k_effective is the number of unique keys pressed an odd number of times. The worst case is when S contains a lot of small i's.

For example, if S has all i from 1 to n, then the total operations would be sum_{i=1 to n} (n / i) ) = O(n log n), which for n=1e5 is about 1e5 * 18 ≈ 1.8e6 operations, which is manageable.

Wait, the sum of n/i for i=1 to n is O(n log n). For n=1e5, log n is about 17. So 1e5 * 17 ≈ 1.7e6 operations. That's acceptable.

So this approach is feasible.

So the steps would be:

- Process the key presses and create a frequency dictionary, then filter out keys with even counts, keeping those with odd counts (since even counts contribute nothing). Let's call this set S.

- Initialize a toggle array of size n+1 (since x starts at 1) initialized to 0.

- For each i in S:
   For j in i, 2i, 3i, ..., up to n:
       toggle[j] ^= 1

- Then, for each lamp x (1..n), if toggle[x] is 1, flip its initial state. Otherwise, leave it.

This approach is O(m + n log n), where m is the number of pressed keys (since we process each key once to count frequencies). The sieve-like part is O(n log n) in the worst case.

But wait, for each i in S, the number of multiples is n/i. So the total sum over i in S of (n//i) is what matters.

If S is all possible i's from 1 to n, then sum (n//i) for i=1..n is O(n log n). For n=1e5, that's acceptable.

But if S is smaller, like k_effective up to 1e4 (since k is up to 1e4), but those keys could be numbers up to 1e5. For example, if all keys in S are 1e5, then each of them has n//i = 1e5 /1e5 =1. So sum is 1e4 *1 =1e4. So in this case, the sieve part is 1e4 steps.

But in the worst case, if all keys in S are 1, then each has n//i =1e5 steps. So 1e4 keys, each with 1e5 steps: 1e9 operations. That's way too slow. Wait, but no. Because the same key can't be in S more than once. Because S is the set of keys pressed an odd number of times. So even if the original key list has multiple instances of the same key, after mod 2, the key is either in S once or not at all.

So for example, if the key 1 is pressed 5 times, in S it will be present once. So when processing key 1, we process all multiples of 1 (i.e., all lamps). So 1e5 steps. If S contains 1, then that's 1e5 steps. If S has 1 and 2, then 1e5 + 5e4 steps, etc. So if S has keys 1,2,3, ..., 1e5, then sum is O(n log n). But if S has a lot of small keys, like 1,2,3, etc., then sum would be O(n log n) steps.

But in the problem, the maximum k is 1e4, which means the maximum possible size of S is 1e4 (if all keys pressed are unique and pressed once). So the worst case is when S contains 1e4 unique keys, each being small. For example, if all keys are 1, then S has 1 once. So processing that is 1e5 steps. If S has 1e4 different keys, but all large (like 1e4 and above), then sum n/i for each i is 1e5 / i. For i=1e4, n/i is 10. So 1e4 keys would contribute 1e4 *10= 1e5 steps. That's manageable.

But if the 1e4 keys in S are all 1, then it's 1e5 steps. Wait, but if the same key is pressed multiple times (even number of times), then S doesn't include it. So the maximum possible S size is up to 1e4. Because the keys can be up to n=1e5, but each key in S is unique (but may be present once).

Wait, no. The S is a set of keys that have been pressed an odd number of times. So if a key is pressed 3 times, it's in S once. So the size of S can't exceed the number of unique keys pressed. For example, if all k=1e4 key presses are the same key, then S will have that key once. So the worst case for S's size is 1e4, which is when all keys pressed are unique.

But when the keys in S are small, like 1, 2, 3, etc., the sieve step would take a lot of steps. For example, if S has 1e4 keys, each i=1, then that's a problem. But no, since in S each key is unique. So if S has 1e4 different keys, each pressed once (after mod 2), then each of those keys is processed once.

So, for example, S could have 1e4 different keys, each of which is 1. Wait, but that's not possible. Because the keys are in the list, but each key is processed once (since frequency mod 2 is 1). So S can have a key once even if it's pressed multiple times (odd times). So for example, if the same key is pressed 3 times, it's in S once.

So the worst case for the sieve is when S has as many keys as possible, and those keys are small.

For example, if S has all keys from 1 to 1e4. Then the sieve steps would be sum_{i=1 to 1e4} (1e5 // i). Let's compute that sum:

sum_{i=1 to 1e4} (1e5 /i) = 1e5 (sum_{i=1 to 1e4} 1/i) ≈ 1e5 * (log(1e4) + gamma) ≈ 1e5 * (9.21) ≈ 9.21e5 operations. Which is manageable.

But if S contains 1e4 keys, each being 1, then sum is 1e5 * 1e4 = 1e9, which is way too much. But that's impossible because S is a set, so each key is present once. So if the same key is pressed multiple times, even after mod 2, it's in S once. So in the example where all 1e4 keys are 1, then S has {1}, and the sieve step is 1e5 steps. Which is manageable.

Ah, right. So S is a set (or a frequency map where each key is present once if pressed an odd number of times). So even if the same key is pressed multiple times, as long as the count is odd, it's included once. So the sieve step's complexity is O(sum_{i in S} (n//i)), and S's size can be up to k (1e4), but each i is unique in S.

So the worst case is when S contains as many small i as possible. For example, S contains 1, 2, 3, ..., 1e4. Then sum (n//i) for i=1 to 1e4.

But for i=1, it's 1e5; i=2, 5e4; etc. Wait, but 1e4 is 10,000. n is up to 1e5. So for i=1e4, n//i is 10 (since 1e5 / 1e4 =10). So the sum would be:

sum_{i=1 to 1e4} (1e5 //i) 

But 1e4 is 10,000. For i=1 to 1e4, the sum is approximately the same as the sum from i=1 to 1e4 of 1e5/i. Which is 1e5 * (H(1e4)), where H is the harmonic series. H(1e4) is about ln(1e4) + gamma ~ 9.21. So sum is ~ 9.21e5 operations. Which is acceptable.

Thus, the sieve approach is feasible.

So the steps are:

1. Read n.

2. Read the initial states of the lamps. Since the output requires "on" or "off", we can parse each state into a boolean (True for on, False for off, or vice versa) but to save memory, perhaps store as a list of strings.

3. Read k, then the list of keys. For each key in the list, count their frequency, mod 2.

4. Create a set S of keys with odd counts.

5. Initialize a toggle array of size n+1 (since x is 1-based) to 0.

6. For each i in S:
   a. For each multiple j of i (i, 2i, ..., up to n):
       toggle[j] ^= 1

7. Then, for each x from 1 to n:
   a. If toggle[x] is 1, flip the initial state. Else, leave as is.

But how to represent the initial state? The initial state is given as a list of words. For example, the first sample input is:

2
off off
2
1 2

The initial states are ["off", "off"]. The keys pressed are 1 and 2.

Processing the keys: 1 and 2 each appear once. So S is {1,2}.

For x=1, the divisors in S are 1. Toggled once → flip.

For x=2, divisors in S are 1 and 2. Toggled twice → even → no flip.

So initial state for x=1 is "off" → flip to "on". x=2 remains "off".

Thus, output "on off".

So the code needs to process the initial states, apply the flips based on the toggle array.

Now, implementing this in Python.

But let's think about the data structures.

First, the initial states are in a list. Then, after processing, for each lamp, we check if toggle[x] is 1 → flip.

So steps in code:

Read n.

Read the initial states as a list.

Read k, then read the list of keys.

Count the frequency of each key, mod 2.

S is a dictionary or a list of keys where frequency is odd.

Then, create toggle array, initialize to 0.

For each i in S:
   for j in range(i, n+1, i):
       toggle[j] ^= 1

Then, for each x in 1..n:
   if toggle[x] is 1:
       flip the state of lamp x-1 (since list is 0-based)
   else:
       leave as is.

Then, output the list.

Now, considering the constraints:

n can be up to 1e5 → toggle array is 1e5 +1 elements → 1e5+1 booleans or integers. That's manageable.

Time-wise, the sieve part is O(sum (n//i) for i in S). For worst case, as discussed, this is manageable.

Memory-wise, for n=1e5, the toggle array is 1e5 integers, which is about 400 KB (since each int is 4 bytes), which is negligible.

So code steps in Python:

But in Python, loops can be slow. So for the sieve part, even with 1e5 iterations, it's possible that it's acceptable.

But when S contains a key like 1, which requires 1e5 iterations. For example, in Python, a loop that runs 1e5 times is okay. But for 1e4 keys each taking 1e4 steps (like for i=10, 1e5//10=1e4 steps), that's 1e8 steps. Which would be too slow.

Wait, but wait. For example, if S has 1e4 keys, each with i=1e4, then each i contributes 1e5 /1e4=10 steps. So 1e4 *10 =1e5 steps. Which is manageable.

But if S has 1e4 keys, but they are all i=2, then each contributes 5e4 steps. 1e4 *5e4=5e8 steps. That's way too slow. Because Python can handle about 1e6 operations per second. So 5e8 would take 500 seconds, which is way over the time limit.

But how can that happen? Because in the problem statement, the keys pressed can be up to 1e4 in count, but each key can be any number up to n (1e5). So if S has 1e4 keys, each of which is 1, then for each i=1, the loop runs 1e5 steps. 1e4 *1e5 =1e9 steps → which would take way too long.

Wait, but in the code, the keys in S are unique. So for example, if the same key is pressed multiple times, but the count is odd, it's included once. So the code processes each i in S once. So even if a key is pressed 100 times (odd), it's included once. So the worst case is when S contains a lot of small keys. For example, S has 1e4 keys, each of which is 1. But how can that happen? Because the input keys can have duplicates, but after mod 2, each key is either in S once or not. So for example, if the user presses 1 1 1 2 2, then after mod 2, 1 is pressed 3 times (mod 2 is 1), 2 is pressed 2 times (mod 2 is 0). So S includes 1 once.

So S can't have multiple copies of the same key. So the code can process each key in S once, regardless of how many times it was pressed (as long as it's odd).

So the problem is that if S has a lot of keys, even if they are all unique, but small. For example, S contains 1e4 keys, all of which are 1, 2, 3, ..., 1e4. Then, the sieve step for each key i would be O(n/i) steps. Summing for i from 1 to 1e4, that's O(n log n) steps, which for n=1e5 is 1e5 * 12 (approx) = 1.2e6 steps. Which is manageable.

Wait, but how is that possible? Let's compute the sum for i=1 to 1e4 of 1e5//i.

Let's see:

sum_{i=1 to 1e4} (1e5 // i)

For i=1: 1e5

i=2: 5e4

i=3: 33333

i=4: 25,000

...

i=100: 1000

i=500: 200

i=1000: 100

i=10,000: 10.

So the sum is 1e5 +5e4 +3e4 +2.5e4 + ... until i=1e4.

But the sum is going to be O(1e5 * (ln(1e4) + 1)), which for 1e4 is ln(1e4)= ~9. So 1e5 * 10 =1e6 steps.

That's manageable in Python.

But if S contains a key like 1, which requires 1e5 steps, then even for 1e4 keys, but each is 1, but that's impossible. Because S can't have duplicate keys. So S can have key 1 once, even if it's pressed 1e4 times (mod 2 is 0 if pressed even times, 1 if pressed odd times). So pressing key 1 1e4 times (even) would not include it in S. But pressing 1e4+1 times would include it once.

So in the worst case, S can have key 1 once. So the sieve step for key 1 is 1e5 steps. Then, other keys may contribute varying steps. So overall, the sieve step is O(1e5) steps.

Thus, in code, even in Python, this approach is feasible.

Now, the code:

Read n.

Read the initial states. The initial states are given as a list of 'off' and 'on' strings. So for example, the list is ['off', 'off'].

Read k. Then read a list of k integers. Then, count the frequency of each integer modulo 2. The keys with odd frequency form S.

Then, create a toggle array of size n+1 (since lamp numbers are 1-based), initialized to 0.

For each i in S:

   for j in range(i, n+1, i):

       toggle[j] ^= 1

Then, for each lamp x (1-based), check if toggle[x] is 1. If so, flip the initial state. Else, leave as is.

Finally, output the resulting states as space-separated words.

So in code:

In Python, the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    initial = input_stream.readline().rstrip("\n").split()
    k = int(input_stream.readline().rstrip("\n"))
    keys = list(map(int, input_stream.readline().rstrip("\n").split()))

    from collections import defaultdict

    freq = defaultdict(int)
    for key in keys:
        freq[key] += 1

    S = [key for key in freq if freq[key] % 2 == 1]

    toggle = [0] * (n + 1)  # 1-based indexing

    for i in S:
        for j in range(i, n+1, i):
            toggle[j] ^= 1

    result = []
    for x in range(1, n+1):
        if toggle[x]:
            # flip the state
            result.append('on' if initial[x-1] == 'off' else 'off')
        else:
            result.append(initial[x-1])

    print(' '.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
off off on
6
1 1 1 1 2 2
""",
            "output": \
"""\
off off on
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

Input:

3

off off on

6

1 1 1 1 2 2

Processing keys: 1 appears 4 times (even → not in S), 2 appears 2 times (even → not in S). So S is empty.

So toggle array remains all 0. So all lamps stay as initial.

Output is the same as input: 'off off on'.

Yes, matches sample.

Another test case: what if keys are [1,1,2]. Then, frequency of 1 is 2 (even, not in S), 2 is 1 (in S). So S = [2]. Then, for x=2, 4, 6, etc., toggle is flipped once.

So for x=2: initial state is flipped once.

But depends on the initial state.

But code seems correct.

Now, optimizing the code for speed.

In Python, loops can be slow. So when S contains a key i=1, which requires 1e5 steps, this loop in Python will take O(1e5) operations. For n=1e5, each iteration is a simple XOR, but in Python, even that could be slow.

Wait, but for n=1e5, the inner loop for i=1 is:

for j in range(1, n+1, 1):

    toggle[j] ^= 1

Which is 1e5 iterations. Each iteration is a list access and XOR. In Python, this is manageable? Let's see.

But let's see: for n=1e5, and S containing i=1, the loop for i=1 is 1e5 steps. How long does that take in Python? Probably a few milliseconds. But if S has 1e4 such keys (but unique), but each with i=2, then the loop for each i=2 is 5e4 steps. 1e4 *5e4 steps is 5e8, which is way too much. But wait, no. Because in that scenario, S can't have 1e4 unique keys. Because each key in S must be <=n. So if n is 1e5, then S can have up to 1e4 unique keys (since k is up to 1e4). For example, if all 1e4 keys are different and in 1..1e5.

But for the worst case, where S contains 1e4 keys, each being 1, which is impossible. Because S is a set, so each key is unique. So S can have a key once even if pressed multiple times. So the maximum possible is that S has up to 1e4 unique keys.

Thus, the worst case for the sieve step is when S contains 1e4 keys, each being small.

But even with that, the total steps would be sum_{i in S} (n//i). Let's assume that S has 1e4 keys, all from 1 to 1e4. Then sum (1e5//i) for i=1 to 1e4 is approximately 1e5 * (ln(1e4) + gamma) ≈ 1e5 * 10 → 1e6 steps. Which is manageable in Python.

But when S contains a key i=1, which is 1e5 steps. Let's see.

In Python, a loop that runs 1e5 times and performs a simple operation (toggle[j] ^=1) takes about 0.01 seconds (assuming 1e6 operations per second). So 1e5 steps would take 0.1 seconds. Which is acceptable.

But when there are multiple such keys, say S has 100 keys, each of which is 1, but that's impossible because S is a set. So S can have i=1 once. So the total steps for that would be 1e5.

Thus, the code should be efficient enough.

But in Python, list comprehensions and other optimizations can help. For example, using a bitmask or other methods. But the code as written is straightforward.

Now, about memory. The toggle array is of size 1e5+1, which is manageable. Each element is an integer (0 or 1), but in Python, each integer is 28 bytes (for small integers). Wait, but a list in Python of integers uses 8 bytes per entry (as pointers to integers). So for 1e5 elements, that's 8e5 bytes, which is about 800KB. Well within the memory constraints (256MB).

Thus, the code should work.

Thus, the final code is as written.
</think>

```python
n = int(input())
initial = input().split()
k = int(input())
keys = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)
for key in keys:
    freq[key] += 1

S = [key for key in freq if freq[key] % 2 == 1]

toggle = [0] * (n + 1)

for i in S:
    for j in range(i, n + 1, i):
        toggle[j] ^= 1

result = []
for x in range(1, n + 1):
    if toggle[x]:
        result.append('on' if initial[x-1] == 'off' else 'off')
    else:
        result.append(initial[x-1])

print(' '.join(result))
```
