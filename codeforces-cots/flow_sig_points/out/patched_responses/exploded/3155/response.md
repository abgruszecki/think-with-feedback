<think>
Okay, I need to solve this problem where I have to find the smallest common substring that is unique in both s1 and s2. Hmm, let's think about the approach here.

First, the problem says a substring is unique in a string if it occurs exactly once. So for each possible substring in both s1 and s2, I need to check if it's unique in each. Then find the minimum length of such a common substring.

But how do I efficiently check for common substrings and their uniqueness in both strings? Because if I check all possible substrings for both, that could be O(n^4), which is way too slow for n=5000. So that's not feasible.

Wait, the constraints are that the maximum length of each string is 5000. So a brute-force approach is definitely out of the question. Need a smarter way.

Let me think: For each possible substring of s1 that is unique, and also check if it exists in s2 as a unique substring. Then among all such substrings, find the one with the smallest length.

But even that approach would be O(n^3) if done naively, which is way too slow. So I need a way to efficiently find the common substrings that are unique in both.

Alternative idea: For each possible length, check all possible substrings of that length in s1 that are unique, then check if s2 has the same substring also unique. The first length (starting from 1 upwards) where this is possible is the answer.

So the plan is:

1. Iterate over possible lengths starting from 1 upwards.
2. For each length l, collect all substrings of s1 of length l that are unique in s1.
3. Check if any of these substrings also exist in s2 as a unique substring.
4. The first such l (smallest) is the answer. If none found, return -1.

This way, as soon as we find a length l where such a substring exists, we can return it immediately, since we start checking from the smallest possible.

Now, the key is how to efficiently generate the unique substrings of a given length l for each string.

For each string, for each possible substring of length l, we can count their occurrences. But doing this naively for each l would be O(n^2) per string, which for l up to 5000 would be O(n^3) in total, which is way too slow for n=5000.

Wait, but the worst case for s1 and s2 being 5000 each, that's 5000 * 5000 = 25 million possible substrings. Hmm, but that's manageable if we can find a way to process them efficiently.

But how to track the occurrence count of each substring in a string?

An efficient way would be to use a dictionary (hash map) where the key is the substring and the value is the count. But generating all substrings of a certain length and checking their counts is O(n) per length for each string, which for l from 1 to max_length (5000) would be O(n^2) time for each string.

Wait, for each l, for a string of length n, there are (n - l + 1) substrings. So for each l, processing both s1 and s2 would take O((n1 - l +1) + (n2 - l +1)) time. But since we start checking l from 1 upwards, and for each l, if there's a common substring, we can return immediately. So the worst case is when the answer is the maximum possible, which is the minimum of the two string lengths. But even then, for each l from 1 to min_len, we process both s1 and s2's substrings of length l.

So total time would be O( sum_{l=1 to min_len} (n1 + n2 - 2l + 2) )) which for n1 and n2 up to 5000 would be O( (5000 + 5000) * min_len ) = O(10,000 * 5000) = 5e7 operations, which is manageable.

Wait, but for each l, we need to generate all substrings of that length in s1 and s2, then check if any of the unique ones in s1 are present and unique in s2.

So here's the detailed steps:

For each l from 1 to min(len(s1), len(s2)):

   For s1:
      create a frequency map of all substrings of length l. Then collect those substrings that have frequency exactly 1.

   For s2:
      create a frequency map of all substrings of length l. Collect those with frequency exactly 1.

   Find the intersection of the two sets (unique substrings of length l in s1 and s2). If the intersection is non-empty, return l as the answer.

If after checking all l up to min len, there's no such l, return -1.

Yes, this approach makes sense. Because once we find the smallest possible l where the intersection exists, that's our answer.

The key is to process the substrings efficiently for each l.

But generating all substrings of length l for a string can be done in O(n) time per l. For example, sliding a window of length l over the string and storing the substring in a hash map.

But for Python, using a dictionary to count the occurrences is feasible. Let's see.

For example, for s = "apple" and l=2:

substrings are 'ap', 'pp', 'pl', 'le'. So for each of these, count them. Then, those with count 1 are the unique ones.

So for each l, for each string, we can:

- Iterate through all possible starting indices (from 0 to len(s) - l)
- For each substring, add to a dictionary (count)
- Then collect all substrings with count == 1.

Once we have the unique substrings for s1 and s2 of length l, check if there's any common substring. The first l where this happens is the answer.

This approach should be efficient enough.

But let's think about the possible time complexity. For each l, processing s1 and s2 is O(n1 + n2). For l up to min(n1, n2), the total time is O( (n1 + n2) * min(n1, n2) ). For n=5000, this is O( (5000 +5000) *5000 )= O(5e7), which is acceptable.

But in Python, creating substrings for each l can be a bit slow, especially for large l. For example, for l=5000, each string of length 5000 would have one substring. But for l=1, it's 5000 substrings. So the total number of substrings across all l is O(n^2), which for n=5e3 is 25 million per string, leading to 50 million total. But with the approach of checking l in order and stopping as soon as a solution is found, perhaps the average case is acceptable.

But how to optimize this in Python? Let's think.

In Python, slicing strings can be O(k) where k is the length of the substring. So for l=5000, each substring is O(5000) time, which is expensive. But for l=5000, the loop for that l is O(n-l+1) = O(1) for each string. But for l=5000, each substring is 5000 characters. So for each of those substrings, slicing is O(5000) time, which for 1 substring per string (for l=5000) is O(5000) per l. But for l=1, each substring is a single character, but there are 5000 of them. So the total time across all l is O(n1^2 + n2^2) in the worst case. For n=5000, that's 25 million *2 = 50 million operations. But each operation is O(l) time. Wait, no: the slicing for each substring of length l is O(l) per substring. So for each l, the total time is O(l*(n - l +1))). So for l up to n, the total is O(n^3) for each string. That's 5e3^3 = 1.25e11 operations for each string. Which is way too slow.

Oh no, this is a problem. Because in Python, the approach of generating all substrings for each l by slicing would be O(n^3) time, which is way beyond the acceptable time limits.

So we need a more efficient way to represent the substrings. How can we compute the frequency of substrings of length l in a way that avoids slicing the entire substring each time?

Ah, here's where rolling hash comes into play. Rolling hash allows us to compute the hash of each substring in O(1) time after the first computation, which is O(n) per l. So using rolling hash can reduce the time for generating the substrings.

But then, we can use a hash map that uses the hash value as the key. However, different substrings can have the same hash (collisions), so we need a way to avoid that. Alternatively, we can use two different rolling hashes (like double hashing) to minimize collision probability.

Alternatively, perhaps for each l, we can compute the polynomial rolling hash for all substrings of length l, and use those as keys in the frequency dictionary. That way, generating the hash is O(n) time per l, which is manageable.

For example, for each string and for a given l, we can precompute the rolling hash for all substrings of length l. Then, we can count the occurrences of each hash. But even with that, there's a possibility of collision. So to avoid that, perhaps we can also check the actual substrings when a hash collision is possible.

But in practice, for programming competition, using a good base and modulus can minimize the collision probability to the point where it's acceptable. Alternatively, we can use a tuple of (hash1, hash2) as the key, using two different bases and moduli, which makes the collision probability extremely low.

Alternatively, another approach is to precompute all possible substrings for all possible l, but that's not feasible.

Wait, but perhaps the problem is that when we generate the substrings for each l, the time is O(n^3) because for each l, each substring is O(l) time. So for l=5000, even though there's one substring, it's O(5000) time. For l=5000, that's manageable, but for l=2500, there are 2500 substrings each of length 2500. That's 2500*2500 = 6,250,000 operations for that l alone.

So for l=2500, the time for s1 would be O(2500 * (5000 -2500 +1)) = 2500*2501= ~6 million. For each l up to 5000, this sums up to O(n^3) time.

Which is way too slow for Python, as 5000^3 is 125e9 operations. That's way beyond the 1e8 operations that can be handled in a second.

Thus, this approach is not feasible. We need a way to compute the substring counts for each l in O(n) time, not O(n*l) time.

So here's where rolling hash can save us. The rolling hash allows us to compute the hash of each substring in O(1) time per substring, after an O(n) pre-processing step.

So, let's think about how to compute the rolling hash for all possible l.

For a string s, precompute the prefix hashes for a base and modulus. Then, for any substring s[i...i+l-1], the hash can be computed in O(1) time. Then, for each l, we can iterate over all possible i (start indices), compute the hash in O(1) time, and count the frequencies.

This way, for each l, processing the string takes O(n) time instead of O(n*l), leading to O(n^2) time overall, which is acceptable.

So here's the plan:

1. Precompute the prefix hash arrays for s1 and s2 using two different base and modulus combinations to minimize collision probability. Alternatively, for the problem constraints, perhaps using a single hash is sufficient, but to be safe, using two different hashes can avoid collisions.

But for the sake of time, perhaps using a single rolling hash is manageable. However, in practice, even with a single rolling hash, there's a chance of collision, which could lead to incorrect counts. So using double hashing (storing tuples of two different hash values) would be better.

But for the purposes of code, perhaps it's easier to just use the actual substrings. Wait, but even that would require O(n*l) time.

Alternatively, perhaps we can use the rolling hash and hope that collisions are negligible, but given the problem statement's constraints, perhaps the test cases do not include collision scenarios. However, in a programming competition, that's a risky approach.

Hmm. So maybe the alternative is to find a way to represent the substrings in a way that allows us to count their occurrences in O(n) time per l, without generating the entire substring each time.

Wait, but the problem is that even if you compute the hash quickly, you need to store the substring (or some representation) to check if two substrings are equal. So perhaps the rolling hash approach is the way to go.

But how to avoid collisions? Well, perhaps for the problem's constraints, using two different hashing methods (like two different moduli and bases) and combining their hash values into a tuple would effectively eliminate collisions.

So here's how to proceed:

For each string s (s1 and s2), precompute prefix hashes for two different bases and moduli. Then, for each substring of length l, compute the two hash values and use the tuple (hash1, hash2) as the key in the frequency map. This way, the collision probability is extremely low, and we can safely consider two substrings equal if their two hash values match.

Thus, the steps would be:

For each l from 1 to min(len(s1), len(s2)):

   For s1:
      Compute all hash tuples (h1, h2) for substrings of length l. Count the frequency of each tuple. Collect those tuples that have frequency 1.

   For s2:
      Compute all hash tuples (h1, h2) for substrings of length l. Count the frequency of each tuple. Collect those tuples that have frequency 1.

   Check if there's any tuple present in both unique sets. If yes, return l.

Thus, the code can proceed efficiently using rolling hashes.

Now, how to implement rolling hash with two different moduli and bases.

Let's choose two different base and modulus pairs. For example:

Base1 = 911382629
Mod1 = 10^18 + 3

Base2 = 3571428571
Mod2 = 10^18 + 7

These are large primes and bases to minimize collisions.

We need to precompute for each string s:

- prefix1: array where prefix1[i] is the hash of s[0..i-1] using base1 and mod1.

- power1: array where power1[i] is (base1^i) mod mod1.

Similarly for base2 and mod2.

Then, the hash of a substring s[i...j] (0-based, j exclusive) in base1 is computed as (prefix1[j] - prefix1[i] * power1[j-i]) mod mod1.

Similarly for base2.

So for each l, the code would:

For s in s1 and s2:

   For i in 0 to len(s) - l:

      j = i + l

      h1 = (prefix1[j] - prefix1[i] * power1[l]) % mod1

      h2 = (prefix2[j] - prefix2[i] * power2[l]) % mod2

      add the tuple (h1, h2) to the frequency map.

Then, for each l, collect the tuples that have frequency exactly 1 in both s1 and s2. If any such tuple exists, return l.

This approach would reduce the per-l processing to O(n) time per string, using the precomputed prefix arrays and power arrays.

Now, the code steps:

Implement the precomputation for s1 and s2 for both base/mod pairs.

Then, for each possible l from 1 to min(len(s1), len(s2)):

   Compute the unique tuples for s1 and s2.

   Check for intersection.

   If any, return l.

Once all l are processed and no intersection found, return -1.

So the code needs to handle this.

Now, let's outline the code structure.

First, precompute for each string the prefix1, prefix2, power1, power2.

But how to precompute power arrays up to the maximum possible l (5000).

Wait, for each string, the maximum possible l is up to len(s). So for s of length 5000, we need power arrays up to 5000.

So code steps for precomputing:

For each string s (s1, s2):

   Compute prefix1, power1 for base1 and mod1.

   Compute prefix2, power2 for base2 and mod2.

Implement a helper function to precompute these.

Then, for each l from 1 to min_len:

   For s1, collect all (h1, h2) tuples of substrings of length l, count their frequencies, and collect those with count 1.

   For s2, do the same.

   Compute the intersection of the two sets. If not empty, return l.

Thus, the code would look like:

But first, implement the rolling hash for each string.

Now, in Python, handling large exponents can be done with modular exponentiation, and precomputing the power arrays.

But let's code this.

First, the helper function to compute the prefix and power arrays.

Base1 and Mod1 are as chosen earlier.

So code:

mod1 = 10**18 + 3
base1 = 911382629

mod2 = 10**18 + 7
base2 = 3571428571

def compute_prefix_hash(s, base, mod):
    n = len(s)
    prefix = [0] * (n + 1)
    power = [1] * (n + 1)
    for i in range(n):
        prefix[i+1] = (prefix[i] * base + ord(s[i])) % mod
        power[i+1] = (power[i] * base) % mod
    return prefix, power

Then, for s1 and s2:

s1 = input().strip()
s2 = input().strip()

s1_prefix1, s1_power1 = compute_prefix_hash(s1, base1, mod1)
s1_prefix2, s1_power2 = compute_prefix_hash(s1, base2, mod2)

s2_prefix1, s2_power1 = compute_prefix_hash(s2, base1, mod1)
s2_prefix2, s2_power2 = compute_prefix_hash(s2, base2, mod2)

Wait, but for s1, we need both the base1 and base2 prefixes. So perhaps for each string, we compute two separate prefix arrays and power arrays.

Alternatively, create two separate compute_prefix_hash functions for each base and mod.

But code can be written as follows.

Then, for each possible l, iterate from 1 to min(len(s1), len(s2)).

Now, for each l in this range:

Check if l is possible (i.e., if s1's length >= l and s2's length >= l). If not, skip.

But since we're iterating up to min(len(s1), len(s2)), this is covered.

For s1:

collect all the hash pairs (h1, h2) of substrings of length l.

Then, count their frequencies. Keep those that have frequency 1.

Same for s2.

Then, the intersection of the unique hash pairs from s1 and s2 is checked. If any, return l.

Thus, the code would:

for l in range(1, min(len(s1), len(s2)) + 1):

    # process s1 for l
    unique_s1 = set()
    freq = defaultdict(int)
    n1 = len(s1)
    for i in range(n1 - l + 1):
        j = i + l
        # compute hash1 for base1 mod1
        h1 = (s1_prefix1[j] - s1_prefix1[i] * s1_power1[l]) % mod1
        h2 = (s1_prefix2[j] - s1_prefix1[i] * s1_power2[l]) % mod2  # Wait, no, the second base is different.

Wait, here's a mistake. The second hash for s1 is computed using the base2 and mod2. So the prefix and power arrays for base2 should be computed separately.

Wait, in the code above, the s1_prefix2 and s1_power2 are computed with base2 and mod2.

So for the second hash (h2), for substring i to i+l:

h2 = (s1_prefix2[j] - s1_prefix2[i] * s1_power2[l]) % mod2

Ah, right. So for each of the two hash functions, the prefix and power arrays are separate.

So the code for s1's h1 and h2 would be:

h1 = (s1_prefix1[j] - s1_prefix1[i] * s1_power1[l]) % mod1
h2 = (s1_prefix2[j] - s1_prefix2[i] * s1_power2[l]) % mod2

Similarly for s2.

So, in code:

For s1, for each i:

h1_part = (s1_prefix1[i + l] - s1_prefix1[i] * s1_power1[l]) % mod1
h2_part = (s1_prefix2[i + l] - s1_prefix2[i] * s1_power2[l]) % mod2

Then, the pair (h1_part, h2_part) is the hash for that substring.

Now, for each l, we can process s1 and s2 as follows:

Processing s1 for l:

freq1 = defaultdict(int)
for i in range(len(s1) - l + 1):
    j = i + l
    h1 = (s1_prefix1[j] - s1_prefix1[i] * s1_power1[l]) % mod1
    h2 = (s1_prefix2[j] - s1_prefix2[i] * s1_power2[l]) % mod2
    freq1[(h1, h2)] += 1

unique_s1 = {k for k, v in freq1.items() if v == 1}

Similarly for s2:

freq2 = defaultdict(int)
for i in range(len(s2) - l + 1):
    j = i + l
    h1 = (s2_prefix1[j] - s2_prefix1[i] * s2_power1[l]) % mod1
    h2 = (s2_prefix2[j] - s2_prefix2[i] * s2_power2[l]) % mod2
    freq2[(h1, h2)] += 1

unique_s2 = {k for k, v in freq2.items() if v == 1}

Then, check if unique_s1 and unique_s2 have any common elements. If yes, return l.

But even this may take O(n) per l for each string. For example, for l=1, each string has up to 5000 elements. So for each l, the processing is O(n) time for each string.

Thus, the total time complexity is O( min(n1, n2) * (n1 + n2) ), which for 5000, would be 5000 * (5000 + 5000) = 5e7 operations, which should be acceptable in Python.

Now, the code needs to handle this efficiently.

But in Python, using defaultdict and sets may introduce some overhead, but for 5e7 operations, perhaps it's manageable, but we need to optimize as much as possible.

Alternative approaches to optimize:

- Precompute all possible l for each string, but that's not feasible.

Alternatively, process l in order, and break as soon as a common substring is found. So the first l with the smallest value is returned.

Thus, the code can proceed to check l=1 first. For l=1, if there's any single character that appears exactly once in both s1 and s2, then return 1.

So for example, in the second example:

Input:

lover
driver

The 'v' appears once in both. So l=1 is the answer.

Thus, the code can check l=1 first. If found, return immediately.

In the code, the loop is from 1 to min_len, so it's checked first.

Thus, the code should be optimized as such.

Now, to handle l=1, the code would:

For s1, collect all characters (since l=1) and count their frequency. Then, collect those with count 1. Similarly for s2. Then check the intersection.

But even with the rolling hash approach, l=1 is handled by the same code.

But for l=1, the rolling hash can be computed quickly.

So the code as described earlier should work.

Now, let's test the code against the sample inputs.

Sample Input 1:

apple
pepperoni

Sample Output: 2

Let's see. For l=1:

s1 is 'apple' → letters a, p, p, l, e. So unique characters are a, l, e.

s2 is 'pepperoni' → letters p, e, p, p, e, r, o, n, i. Unique characters are r, o, n, i.

So intersection is empty. So l=1 not possible.

For l=2:

Check s1's substrings of length 2:

ap → 1 occurrence.

pp → 1 occurrence (since in s1, 'apple' has 'ap', 'pp', 'pl', 'le'). So 'pp' occurs once.

pl → once.

le → once.

So the unique substrings in s1 are all except perhaps any that are duplicates. Wait, no, because 'pp' occurs once. So all are unique.

In s2, substrings of length 2: 'pe', 'ep', 'pp', 'pe', 'ep', 'pr', 'ro', 'on', 'ni'.

Check frequencies:

pe occurs twice.

ep occurs twice.

pp occurs once (substrings starting at index 2: 'pp' in 'pepper' → positions 2-3. Also, index 3 is part of 'pp' in the 'pper' part? Let me see:

s2 = 'pepperoni' → indices 0-8 (length 9). For l=2, 8 substrings.

Indices 0-1: 'pe', 1-2: 'ep', 2-3: 'pp', 3-4: 'pe', 4-5: 'er', 5-6: 'ro', 6-7: 'on', 7-8: 'ni'.

So 'pe' occurs at 0-1 and 3-4 → count 2. 'ep' occurs at 1-2 and 4-5 (wait, 4-5 is 'er'? Wait no. Wait, after 'pp' at 2-3, the next is 3-4: 'pe' (s2[3] is 'p', s2[4] is 'e' → 'pe'). Then 4-5 is 'er' (s2[4] is 'e', s2[5] is 'r') → 'er'. So 'pe' occurs twice. 'pp' occurs once. 'er' once. 'ro' once. 'on' once. 'ni' once. So in s2, the unique substrings of length 2 are 'pp', 'er', 'ro', 'on', 'ni'.

The unique substrings in s1 are ap, pp, pl, le. So the common ones are 'pp'. So in s1, 'pp' is unique, and in s2, 'pp' is unique. So the answer is 2.

Thus, the code would return 2.

Sample input 2:

lover
driver

l=1: check for single characters. 'l' occurs once in 'lover', 'd' occurs once in 'driver'. 'v' occurs once in both. So 'v' is present in both's unique sets. So l=1 is the answer.

Sample input 3:

bidhan
roy

No common characters. So output -1.

Sample input4:

testsetses
teeptes

Sample output is 3.

Looking for the minimal l where there's a common unique substring. Let's think.

For l=3:

In s1: 'testsetses' → possible substrings of length 3. Let's see if any of them are unique.

But perhaps the common substring is 'tes'? Or another substring.

But regardless, the code will find the minimal l where the intersection exists.

Thus, the code should handle these cases.

Now, code implementation in Python.

But first, code for the helper function.

But in Python, using a helper function to compute the prefix and power arrays.

But for each string, compute two prefix and power arrays (one for each base/mod pair).

But how?

For s1:

s1_prefix1, s1_power1 = compute_prefix_hash(s1, base1, mod1)
s1_prefix2, s1_power2 = compute_prefix_hash(s1, base2, mod2)

Similarly for s2.

Then, for each l:

For s1's substrings of length l:

for i in 0 to len(s1)-l:

   j = i + l

   h1 = (s1_prefix1[j] - s1_prefix1[i] * s1_power1[l]) % mod1

   h2 = (s1_prefix2[j] - s1_prefix2[i] * s1_power2[l]) % mod2

Add (h1, h2) to the frequency map.

Same for s2.

Now, the code.

But for large mod values, we need to handle the modulus correctly. Python can handle big integers, but the calculation should be done correctly.

So the code:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    mod1 = 10**18 + 3
    base1 = 911382629

    mod2 = 10**18 + 7
    base2 = 3571428571

    def compute_prefix_hash(s, base, mod):
        n = len(s)
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)
        for i in range(n):
            prefix[i+1] = (prefix[i] * base + ord(s[i])) % mod
            power[i+1] = (power[i] * base) % mod
        return prefix, power

    s1 = input_stream.readline().rstrip("\n").strip()
    s2 = input_stream.readline().rstrip("\n").strip()

    min_len = min(len(s1), len(s2))

    if min_len == 0:
        print(-1, file=output_stream)
        return

    s1_prefix1, s1_power1 = compute_prefix_hash(s1, base1, mod1)
    s1_prefix2, s1_power2 = compute_prefix_hash(s1, base2, mod2)

    s2_prefix1, s2_power1 = compute_prefix_hash(s2, base1, mod1)
    s2_prefix2, s2_power2 = compute_prefix_hash(s2, base2, mod2)

    result = -1

    for l in range(1, min_len + 1):
        # Process s1 for length l
        s1_hash_counts = {}
        for i in range(len(s1) - l + 1):
            j = i + l
            h1 = (s1_prefix1[j] - s1_prefix1[i] * s1_power1[l]) % mod1
            h2 = (s1_prefix2[j] - s1_prefix2[i] * s1_power2[l]) % mod2
            key = (h1, h2)
            if key in s1_hash_counts:
                s1_hash_counts[key] += 1
            else:
                s1_hash_counts[key] = 1
        # Collect unique hashes in s1
        unique_s1 = set()
        for k, v in s1_hash_counts.items():
            if v == 1:
                unique_s1.add(k)
        
        # Process s2 for length l
        s2_hash_counts = {}
        for i in range(len(s2) - l + 1):
            j = i + l
            h1 = (s2_prefix1[j] - s2_prefix1[i] * s2_power1[l]) % mod1
            h2 = (s2_prefix2[j] - s2_prefix2[i] * s2_power2[l]) % mod2
            key = (h1, h2)
            if key in s2_hash_counts:
                s2_hash_counts[key] += 1
            else:
                s2_hash_counts[key] = 1
        # Collect unique hashes in s2
        unique_s2 = set()
        for k, v in s2_hash_counts.items():
            if v == 1:
                unique_s2.add(k)
        
        # Check intersection
        if unique_s1 & unique_s2:
            result = l
            break

    print(result if result != -1 else -1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
bidhan
roy
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

</think>

```python
mod1 = 10**18 + 3
base1 = 911382629
mod2 = 10**18 + 7
base2 = 3571428571

def compute_prefix_hash(s, base, mod):
    n = len(s)
    prefix = [0] * (n + 1)
    power = [1] * (n + 1)
    for i in range(n):
        prefix[i+1] = (prefix[i] * base + ord(s[i])) % mod
        power[i+1] = (power[i] * base) % mod
    return prefix, power

s1 = input().strip()
s2 = input().strip()

min_len = min(len(s1), len(s2))

if min_len == 0:
    print(-1)
    exit()

s1_prefix1, s1_power1 = compute_prefix_hash(s1, base1, mod1)
s1_prefix2, s1_power2 = compute_prefix_hash(s1, base2, mod2)

s2_prefix1, s2_power1 = compute_prefix_hash(s2, base1, mod1)
s2_prefix2, s2_power2 = compute_prefix_hash(s2, base2, mod2)

result = -1

for l in range(1, min_len + 1):
    # Process s1
    s1_hash_counts = {}
    for i in range(len(s1) - l + 1):
        j = i + l
        h1 = (s1_prefix1[j] - s1_prefix1[i] * s1_power1[l]) % mod1
        h2 = (s1_prefix2[j] - s1_prefix2[i] * s1_power2[l]) % mod2
        key = (h1, h2)
        s1_hash_counts[key] = s1_hash_counts.get(key, 0) + 1
    unique_s1 = {k for k, v in s1_hash_counts.items() if v == 1}
    
    # Process s2
    s2_hash_counts = {}
    for i in range(len(s2) - l + 1):
        j = i + l
        h1 = (s2_prefix1[j] - s2_prefix1[i] * s2_power1[l]) % mod1
        h2 = (s2_prefix2[j] - s2_prefix2[i] * s2_power2[l]) % mod2
        key = (h1, h2)
        s2_hash_counts[key] = s2_hash_counts.get(key, 0) + 1
    unique_s2 = {k for k, v in s2_hash_counts.items() if v == 1}
    
    # Check intersection
    if unique_s1 & unique_s2:
        result = l
        break

print(result)
```
