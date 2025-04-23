<think>
Okay, I need to solve this problem where I have to determine if two strings are equivalent based on the given recursive definition. Let's see. The problem says two strings are equivalent if either they are equal, or if when split into two halves (each of same length), the first half of a is equivalent to the first half of b and the second half of a is equivalent to the second of b, or vice versa with the halves swapped. 

So the approach here is probably a recursive one. But considering the constraints, the strings can be up to 200,000 characters long. A straightforward recursive approach might hit stack overflow or be too slow. So I need to think about an efficient way to check equivalence without getting into too deep recursion, which could cause stack issues or timeouts.

First, let's think about the base case. If the strings are of odd length, then they can't be split into two equal halves, so the only way they can be equivalent is if they are exactly equal. For even lengths, we have to check both possibilities: splitting into a1/a2 and comparing a1 with b1 and a2 with b2, or a1 with b2 and a2 with b1. But even this could be expensive if done naively for large strings.

Wait, but how do the splits work? Each time the string is split into two halves, which are each split again if possible. So the equivalence is determined recursively. But for very large strings, the recursion depth could be log2(n), which for 2e5 is about 18, which is manageable if each step is O(n). But even O(n log n) could be acceptable.

Hmm. Let's think of a way to memoize or to process the strings in a way that avoids redundant computations. Alternatively, perhaps the equivalence can be determined by comparing the sorted versions of the strings at each level of recursion. Wait, but that's not necessarily the case. Because the split into halves and their equivalence isn't just a matter of the characters being present, but the structure. For example, in the first sample input:

aaba and abaa. Let's see. When split into two halves, each becomes two parts. Then each of those parts might be split again. So the order and the structure matters. So sorting the entire string wouldn't work. For instance, "ab" and "ba" are equivalent because each can be split into single characters (since length 2 is even), and the split gives "a" and "b" for the first, and "b" and "a" for the second. So swapping the halves gives equivalence. So the sorted approach would have both as "ab", but the equivalence is based on the recursive splits, not the entire sorted order. But in this case, at each split level, if the current strings are even length, we check the two possibilities. So how can we model this?

An alternative approach is to represent each string by a unique key that captures its equivalence. If two strings have the same key, they are equivalent. The key can be built recursively. For example, for a string s of even length, the key is the sorted combination of the keys of the two possible splits. For odd length, the key is the string itself. Then, two strings are equivalent if their keys are the same.

Wait, but how to compute this key efficiently. For example, for a string of even length, split into two halves, compute the key for each half, then sort the two keys and combine them (so that the order of the two halves doesn't matter because we can swap them), then the key for the current string is the sorted combination of the two subkeys. Then, for a string of odd length, the key is the string itself.

Yes, this seems like a viable approach. Let's take an example. For "ab", the key would be the sorted combination of the keys of "a" and "b". The key for "a" is "a", and for "b" is "b". So sorted combination would be "a" + "b" or "b" + "a"? Wait, no. Wait, when the string is even-length, split into two halves. For each of those halves, compute their keys. Then, for the current string's key, sort the two subkeys (since the two halves can be swapped), and combine them. So for "ab", split into "a" and "b", their keys are "a" and "b". So the current key would be the sorted pair ("a","b") concatenated. So the key would be "ab" sorted as "ab" (since the two are in order). Wait, but "ab" and "ba" would have the same key if we sort their subkeys. Because "ab" split into "a" and "b" gives key "a" and "b". "ba" split into "b" and "a" gives "b" and "a". When sorted, the two pairs are ("a", "b") and ("a", "b"), so the combined key is the same. Thus, their keys would be the same, so they are equivalent.

So the key idea is: for each string, recursively compute a key. For even length, split into two, compute their keys, sort the two keys (so the order of the halves doesn't matter), then combine them. For odd length, the key is the string itself.

Then, two strings are equivalent if their keys are the same.

So the algorithm would be:

Compute the key for both input strings. If the keys are equal, return YES, else NO.

But how to compute the key efficiently, especially for large strings?

The problem is that for a string of length n, the key could have size O(n log n) in the worst case. For example, each split requires combining two keys, each of which is O(n/2 log n/2), leading to O(n log n) total size. For a string of length 2^18, the key could be very large, leading to memory issues.

Wait, but for a string of length 2^k, the key is formed by combining sorted pairs recursively. For example, for a string of length 4, split into two of length 2. Each of those split into two of length 1. So the keys for those would be the characters. Then, each of the two halves of the original string would have a key that is the sorted combination of their two characters. Then the original key is the sorted combination of those two sorted pairs. So the key for the original string would be the sorted combination of the sorted pairs. So for example, the string "aabb" would split into "aa" and "bb". Their keys are "aa" (since sorted combination of "a" and "a" is "aa") and "bb". Then the original key is "aabb" sorted as "aa" and "bb" in order. But wait, since we sort the two parts, "aa" and "bb" are already in order, so the key is "aa"+"bb" → "aabb". But if the string was "abab", split into "ab" and "ab". Each "ab" would split into "a" and "b", which would generate keys sorted as "ab". So the two parts are "ab" and "ab", sorted gives "abab". But "aabb" and "abab" would have different keys, leading to the correct answer in the second sample input.

So the key approach would work. But for a string of length 2e5, the key could be extremely large. For example, each split doubles the length of the key. For example, each even split adds two parts. Wait, let's see: for a string of length 2n, the key is the combination of the two sorted subkeys. Each subkey is O(n log n) in size. So the key for the original string would be O(2n log n). So for a string of length N, the total key size could be O(N log N). For 2e5, that's 2e5 * 20 ≈ 4e6, which is manageable. But in practice, building such a key for a 2e5-length string might be time-consuming. Because each concatenation of two strings takes O(k) time for their combined length. So for a string of length N, the time complexity would be O(N log N) * O(N) per step. Wait, no. Let's see: For each recursive step, the time is the sum of the sizes of the subkeys plus the time to sort and combine them. For example, for a string of length N, split into two halves. The time to compute their keys is T(N/2) each. Then combining them: each key is of size O((N/2) log (N/2)), so combining them would take O(N log N) time. Then, for the overall time, the recurrence would be T(N) = 2*T(N/2) + O(N log N). Solving this, the total time is O(N (log N)^2). For 2e5, (log N)^2 is about (20)^2 = 400, so 2e5 * 400 = 8e7 operations. Which is acceptable for Python in 2 seconds? Maybe, but perhaps it's tight.

Alternatively, we can memoize the keys for substrings. But even that may not help, because each unique substring would have a unique key. For very long strings, this could be memory-intensive.

Another approach is to realize that when the string is even-length, the key is the sorted combination of the keys of the two halves. So, for two strings to be equivalent, their sorted combination of the two halves must match. But perhaps we can compute a hash that represents this, instead of the full key. But the problem is that different keys could hash to the same value. So we need a perfect hash. Alternatively, we can use memoization with the actual key strings, but that's going to be memory-heavy.

Alternatively, we can represent the key as a tuple of the sorted subkeys. But even then, for large N, the tuples can become large. But perhaps we can represent the key in a way that allows for equality checks without building the entire structure. For example, using a hash of the key. But again, collisions are possible unless we use a perfect hashing method, which is difficult.

Alternatively, when comparing two strings, instead of precomputing the entire key, we can compare their equivalence directly, using a recursive approach with memoization. For example, when comparing a and b:

- if a == b, return True.

- else if length is even:

   - split a into a1 and a2, split b into b1 and b2.

   - check if (a1 is equivalent to b1 and a2 equivalent to b2) OR (a1 equivalent to b2 and a2 equivalent to b1).

- else, return False.

But this approach could lead to O(N log N) time in the worst case, but for certain cases (like when the two strings differ early on) it could be efficient. However, in the worst case where the two strings are equivalent but require checking all possible splits, it might take O(N log N) time, which is acceptable for 2e5?

Wait, let's think about the time complexity. For each call to the equivalence function, if the strings are even-length, we split into two halves and make two recursive calls each. Wait, no: for each even-length case, we have to check two possibilities. Let's model it as:

The equivalence check function for two strings s and t:

def equivalent(s, t):

   if s == t:

      return True

   if len(s) % 2 != 0:

      return False

   split s into a1, a2

   split t into b1, b2

   return (equivalent(a1, b1) and equivalent(a2, b2)) or (equivalent(a1, b2) and equivalent(a2, b1))

But this is a problem because the number of recursive calls can be exponential. For example, in the case where the two strings are equivalent but each split requires checking both possibilities. For a string of length 2^k, the number of recursive calls could be O(2^k), which is way too big for k=20 (2^20 is a million, which is manageable? For 2^20, but the maximum N is 2e5, which is about 2^18. So 2^18 is 262,144. But even for 2^18, the number of calls could be O(2^18) which is about 2.6e5, which is manageable. Wait, but the recursion depth would be O(log n). For each split, the length halves. So the depth is O(log n). But for each call, we make up to two possibilities. So for each level, the number of calls could be multiplied by two. For example, at the top level (n=2^k), we have one call. Then, at each split, each call could split into two possibilities, leading to 2^d calls at depth d. For depth k, that's 2^k calls. Which for k=18 is 262,144. Which is manageable. But wait, each call may split into two possibilities. Wait, for each call where the strings are even and not equal, we split and check two possibilities. For example, for a and b of even length not equal, split into a1, a2 and b1, b2. Then check (a1 eq b1 and a2 eq b2) OR (a1 eq b2 and a2 eq b1). Each of those could require two recursive calls, but in the worst case, for each equivalence check, all possibilities are considered. But this could lead to O(2^k) calls, which for k=18 is 262,144. But that's manageable in Python, but maybe tight. However, in practice, the cases where the strings are equivalent may not require all possibilities to be checked. For example, if the first possibility returns True, then the second is not checked. But if the answer is "NO", then both possibilities must be checked. 

But for some cases, this approach may be too slow. For example, two strings that are not equivalent but the code has to check all possible split combinations. For example, two strings that are very similar but not equivalent. 

Hmm. So for the problem's constraints, with up to 2e5 characters, the recursive approach may not be feasible. Because for N=2e5, and log2(2e5) is around 18, the number of recursive steps could be 2^18 = 262,144. But each step involves splitting the string into two halves. Splitting a string of length 2e5 into two 1e5 parts takes O(n) time. For each recursive call, that's O(n) time, leading to O(n log n) total time. But 2e5 * log(2e5) is about 2e5 * 18 ≈ 3.6e6 operations. Which is acceptable for Python, as per the time constraints. But in practice, for the worst case, this might be too slow.

Wait, but in Python, splitting a string into two halves is O(k) for a string of length k. So for a recursive call that splits a string of length N, the splitting step is O(N) time. For each recursive call, the time is O(N), and the number of calls is O(log N) levels, but each level has O(2^d) calls, where d is the depth. For example, the first level (depth 0) is 1 call (n=2e5). Depth 1: two calls (each of n=1e5). Depth 2: four calls (each of n=5e4). And so on, until depth log2(n). The total time would be the sum over each level of the number of calls multiplied by the time per call. Each call splits the string into two, which is O(k) time, where k is the current string length. So for each level d (depth), the number of calls is 2^d, each processing a string of length n/(2^d). So the total time is sum_{d=0 to log2(n)} 2^d * (n/(2^d)) ) = sum_{d=0}^{} n → O(n log n). So this is O(n log n) time, which for n=2e5 is about 2e5 * 18 ≈ 3.6e6 operations. Which should be manageable in Python within 2 seconds. But how?

Wait, in the worst case, for each split, the two possibilities (either (a1, b1) and (a2, b2) or (a1, b2) and (a2, b1)) would have to be checked. For example, if in all splits, the two possibilities are not equal, then each equivalence check would have to check both possibilities, leading to more recursive calls.

But perhaps there's a way to memoize the equivalence of pairs of substrings. But since the substrings can vary in length and position, memoizing all possible pairs is not feasible for large N.

Alternative idea: precompute for each possible substring (specified by start and end indices) its equivalence key. But again, this would require O(n^2) space, which is impossible for n=2e5.

Hmm. So perhaps the recursive approach is manageable, but we need to optimize it by avoiding processing the same substrings multiple times. Wait, but how? The problem is that each call to equivalent(s, t) is for two different s and t. So even if s and t are the same as previous calls, but from different parent calls, we can't memoize that.

Alternative approach: for each string, compute a unique "canonical" form, which is the minimal form according to the equivalence rules. Then, the two strings are equivalent if their canonical forms are equal.

To compute the canonical form, for even-length strings, split into two halves, compute their canonical forms, sort them, and concatenate. For odd-length, the canonical form is the string itself.

This way, two equivalent strings will have the same canonical form. So the algorithm is to compute the canonical form for both input strings and compare them.

The question is, how to compute the canonical form efficiently.

For example, the canonical form of "ab" would be the sorted combination of the canonical forms of "a" and "b". Since "a" and "b" are length 1 (odd), their canonical forms are "a" and "b". Sort these two to get "ab" (sorted in order). Wait, but "ba" would split into "b" and "a", which are canonical forms "b" and "a", sorted to "ab", so the canonical form of "ba" is also "ab". So both "ab" and "ba" would have the same canonical form. Then, the equivalence is determined by their canonical forms being equal.

Yes. So this approach would work.

The problem is how to compute the canonical form efficiently. For large strings, this could be done recursively, but memoization could help.

But even without memoization, the time complexity is O(n log n), which should be manageable.

Let's see. For a string of length n:

If n is odd, return the string.

Else, split into two halves, compute canonical forms of each, sort the two, concatenate.

Each split is O(n) time (for splitting into two halves). But for each step, the total time is O(n). For example, for a string of length 2^d, the time is O(2^d) for the top level, then 2*(2^{d-1}) = 2^d for the next level, then 4*(2^{d-2}) = 2^d, etc. So for each level, the total time is O(2^d). There are d levels. So total time is O(d * 2^d) = O(n log n).

This is the same as the recursive approach.

But in Python, concatenating strings can be expensive. For example, building the canonical form for a string of even length would require splitting, recursively computing the canonical forms of the two halves (each of length n/2), then sorting these two strings, and concatenating them. The concatenation of two strings of length n/2 log n/2 each would take O(n log n) time. Wait, but for each split, the canonical form for the current string is the sorted combination of the two sub canonical forms. So for example, the canonical form for a string of length 2 is the sorted combination of the two characters. For a string of length 4, the canonical form is the sorted combination of the canonical forms of the two halves (each of length 2). The canonical forms of each half are the sorted pairs of their characters. So combining them, sorting the two pairs, and concatenating.

But the length of the canonical form for a string of length n can be O(n log n), which for n=2e5 could be up to 2e5 * 18 = 3.6e6. But building such a string would take O(3.6e6) steps, which is manageable.

But for n=2e5, the canonical form would be a very long string, which could take up a lot of memory and time to generate and compare.

This is a problem. For example, in the worst case, comparing two strings of length 2e5 would require generating canonical forms of about 3.6e6 characters each and then comparing them. That's O(3.6e6) time for the comparison. But in Python, comparing two strings of length 3e6 is O(k) where k is the length. So that's 3.6e6 steps, which could take some time. But perhaps it's manageable.

Alternative idea: memoize the canonical form for a string. But since the canonical form is determined recursively, and the same substrings can appear in different contexts, memoization could help. For example, if a substring's canonical form is already computed, we can reuse it. But for large strings, the memoization storage could be very high. For example, for a string of length 2e5, there are O(n) unique substrings. But each substring's canonical form is O(m log m) where m is the length of the substring. So the total storage would be O(n^2 log n), which is way too big for n=2e5.

Thus, memoization is not feasible.

Alternative approach: compute the canonical form as a tuple of some kind, but even then, the comparison would take time.

Hmm. So this suggests that the canonical form approach may not be feasible for the largest inputs due to memory and time constraints.

So, perhaps the recursive approach is better. Let's think again about the recursive approach:

def are_equivalent(a, b):

    if a == b:

        return True

    n = len(a)

    if n % 2 != 0:

        return False

    a1, a2 = a[:n//2], a[n//2:]

    b1, b2 = b[:n//2], b[n//2:]

    return (are_equivalent(a1, b1) and are_equivalent(a2, b2)) or (are_equivalent(a1, b2) and are_equivalent(a2, b1))

But for a= a1a2 and b= b1b2, this checks both possible permutations of the halves. However, this approach may lead to repeated checks. For example, when checking a1 vs b1 and a2 vs b2, if those checks are true, it returns immediately. But if not, it checks a1 vs b2 and a2 vs b1.

But for the worst case, this could lead to a lot of recursive calls. For example, two strings that are almost equivalent, but differ at the last split.

But perhaps this is manageable. Let's think about the sample input 1: aaba and abaa.

The first split into two halves of length 2. a1 is 'aa', a2 is 'ba'; b1 is 'ab', b2 is 'aa'. Then, check if (a1 equivalent to b1 and a2 equivalent to b2) or (a1 equivalent to b2 and a2 equivalent to b1). 

The first check would split a1 into 'a' and 'a' (each of length 1). So a1's split is 'a' and 'a', which are equivalent (since they are equal). So a1's equivalent to itself. Then, a2 is 'ba' which is split into 'b' and 'a' (each of length 1). So a2's canonical form is 'ab'. 

Wait, but according to the recursive function, when comparing a1 and b1, which are 'aa' and 'ab' respectively. So the function will split them into two halves again. 'aa' splits into 'a' and 'a', 'ab' splits into 'a' and 'b'. Then, the comparison would check if 'a' == 'a' and 'a' == 'b' → no. Then check if 'a' == 'b' and 'a' == 'a' → no. So a1 and b1 are not equivalent. Thus, the first condition (a1 equivalent to b1) is false. Then, check a1 equivalent to b2 ('aa') and a2 equivalent to b1 ('ab'). 

a1 is 'aa', which split into 'a' and 'a'. b2 is 'aa', which also split into 'a' and 'a'. So they are equivalent. a2 is 'ba', which splits into 'b' and 'a'. b1 is 'ab', which splits into 'a' and 'b'. Comparing 'ba' and 'ab' would split into 'b' vs 'a' and 'a' vs 'b'. So each split would compare 'b' vs 'a' (no) and then 'b' vs 'b' and 'a' vs 'a' (no). Wait, no. The 'ba' and 'ab' are even length (2), split into 'b' and 'a', and 'a' and 'b'. So the function would check if 'b' == 'a' and 'a' == 'b' → no. Then check if 'b' == 'b' and 'a' == 'a' → yes. So 'ba' and 'ab' are equivalent. 

So a2 is equivalent to b1. So the second condition (a1 equivalent to b2 and a2 equivalent to b1) is true, so the function returns true.

But in this case, the function does some redundant checks, but it's manageable.

But for a large input, this approach might take too long. So what's the alternative?

Alternative idea: memoize the results of comparing pairs of substrings. For example, when checking if two substrings are equivalent, store the result in a memoization dictionary. But since the substrings can be very long, using the actual string as a key is not feasible. So perhaps, memoize based on their start and end indices. But in this problem, the two input strings are fixed. So perhaps, for each pair of substrings (s1 and s2) from the two input strings, memoize whether they are equivalent.

But how to represent the substrings? For the first input string, let's call it S, and the second T. For each possible substring of S and T, defined by their start and end indices, we can memoize if S[i:j] and T[k:l] are equivalent. However, this approach would require a four-dimensional memoization (i, j, k, l), which is impossible for 2e5-length strings.

Alternative approach: note that for the equivalence check between two substrings, they must be of the same length. So for any call to are_equivalent(s, t), the length of s and t must be the same. So we can memoize based on the two strings and their length. But since the substrings are parts of the original strings, perhaps we can represent them by their start and end indices in the original strings. 

For example, memoize (i, j, k, l) where i and j are the start and end indices of the substring from S, and k and l are the start and end indices of the substring from T. But even with this, for 2e5-length strings, the number of possible combinations is O(n^4), which is impossible.

So this is not feasible.

Alternative Idea: If two substrings are equivalent, their hash must be the same. But the reverse is not true. But perhaps using a rolling hash function that uniquely identifies the equivalence. For example, for the canonical form approach, compute a hash of the canonical form. Then, two substrings are equivalent if their hash values are the same. This requires that the hash of the canonical form uniquely represents the equivalence. But how to compute such a hash efficiently.

For example, for each substring, compute a hash that is a combination of the hashes of its two halves (sorted), if even-length, or the hash of the substring itself if odd-length. This way, two equivalent substrings will have the same hash.

But the hash computation can be done recursively. Let's see:

def compute_hash(s):

    n = len(s)

    if n % 2 != 0:

        return hash(s)  # or a tuple representation

    h1 = compute_hash(s[:n//2])

    h2 = compute_hash(s[n//2:])

    # sort the two hashes and combine

    if h1 <= h2:

        return hash( (h1, h2) )

    else:

        return hash( (h2, h1) )

But even this approach would require O(n log n) time. But the problem is that in Python, using the built-in hash function may not be reliable because of collisions. So we need a way to compute a unique hash that is collision-free. However, this is impossible in practice, but using a perfect hashing scheme for the problem's constraints may be possible.

Alternatively, we can represent the hash as a tuple that uniquely represents the canonical form. For example, for even-length strings, the tuple is a sorted pair of the two child tuples. For odd-length, the tuple is the string itself. Then, two substrings are equivalent if their hash tuples are equal.

But tuples can be large for long strings. For example, a string of length 2e5 would generate a tuple of depth log2(2e5) ≈ 18, each level being a sorted pair of the lower-level tuples. But comparing tuples in Python is done element-wise, which is O(1) if the first elements differ, but up to O(k) if all elements are same until the end. So comparing two tuples for equality is O(k), where k is the length of the tuple's structure. For large tuples, this could be expensive.

But perhaps this approach is manageable. Let's see.

Implementing this, the compute_hash function returns a tuple that represents the canonical form. For example:

def canonical(s):

    n = len(s)

    if n % 2 != 0:

        return (s,)

    left = canonical(s[:n//2])

    right = canonical(s[n//2:])

    if left < right:

        return (left, right)

    else:

        return (right, left)

Then, comparing the canonical tuples of two strings s and t would determine equivalence.

But the tuples can become large. For example, a string of length 2^k would have a tuple of depth k. Each node in the tuple is a pair of tuples. The total number of elements in the tuple would be 2^k, but structured as a tree. Comparing two such tuples would take O(1) time if the top-level tuples are different. Otherwise, recursively compare the children. But in practice, for equivalent strings, the entire structure must be compared, which could take O(log n) time.

Wait, no. The tuples are nested. For example, for a string of length 4, the canonical tuple would be ((a, b), (c, d)), sorted. Comparing two such tuples would be done by Python in O(1) time if the top-level elements are different. But if they are the same, then recursively compare their elements. However, this depends on how Python implements tuple equality. 

But perhaps the time to compare two tuples is O(1) in practice, but this is not the case. For example, two tuples with different structures will have O(1) comparison if the first differing element is found early. But for equivalent tuples, the entire structure must be compared, which would take time proportional to the size of the tuple structure. For large tuples, this could be expensive.

Thus, for the problem's constraints, generating the canonical tuples for both strings and then comparing them may be feasible, but it's possible that the tuples are very large and comparison takes too long.

Alternative Idea: Precompute the canonical form for each string and then compare them. But for large strings, generating the canonical form as a string may be too time-consuming.

Another Idea: The problem can be viewed as a decision tree where each even split branches into two possibilities. The equivalence is determined by the existence of a path through the tree that allows the strings to be equal. But this is similar to the recursive approach.

But in practice, for large inputs, the recursive approach may be too slow. So perhaps we need to find a way to compute the equivalence in O(n log n) time with O(n) space.

Wait, here's a different perspective: two strings are equivalent if their multiset of characters is the same and they can be split into pairs according to the equivalence rules. But this is not sufficient. For example, the first sample input has aaba and abaa. Both have the same multiset of characters (3 a's and 1 b?), but other examples may have different multisets. So checking the multiset is a necessary condition, but not sufficient.

Thus, the multiset check can be used as a first step to quickly eliminate some cases where the strings are not equivalent. But the real solution requires checking the structure.

So the steps could be:

1. Check if the two strings have the same multiset of characters. If not, return NO.

2. Otherwise, proceed with the recursive equivalence check.

But how much does this help? For large strings where the multisets differ, it's a quick check. For those where they match, we proceed. But the main time is spent on the recursive check. However, this may not help in cases where the multisets are the same but the structure is not, but it's worth adding as a preliminary check.

Another Idea: The equivalence is a form of a tree isomorphism. Each even split creates two children, and the order of children is irrelevant. So the equivalence is similar to comparing two binary trees where the left and right children can be swapped. The canonical form is the minimal representation of this tree. So the problem reduces to building such a tree for each string and comparing them.

But building the tree for a string of length 2e5 would require O(n log n) time. The tree would have O(n) nodes. Comparing two such trees for isomorphism can be done in O(n) time.

But how to represent the tree and compute a unique identifier for each node. For example, using a hash or a unique number for each node's structure.

This brings us back to the canonical form approach. But to compute the hash efficiently.

So, let's think of the following approach:

For each string, compute a hash that uniquely represents its canonical form. The hash is computed recursively:

- For odd-length strings, the hash is the string itself.

- For even-length strings, split into two halves, compute their hashes, sort the two hashes, and combine them into a new hash.

But to make this efficient, we can represent the hash as a tuple of the hashes of the sorted sub-hashes. However, in Python, tuples are hashable and can be compared directly. But for large strings, this would generate very deep tuples, leading to increased time for comparisons.

Alternative Idea: Use memoization for the hash computation. For each substring (by start and end indices), compute its hash once and reuse it. This way, even if a substring is processed multiple times in different parts of the recursion, its hash is computed only once.

But how to manage this. For the original two input strings, S and T, we can precompute the hash for all possible substrings. However, for strings of length 2e5, there are O(n^2) possible substrings, which is impossible. So this approach is not feasible.

Another Idea: The equivalence check between two strings can be done using a memoization dictionary that maps pairs of (start_S, start_T, length) to their equivalence result. Since the strings must be of the same length, we can represent the equivalence check as a function of (start_S, start_T, length). For example, for a given length l, and start positions i and j in S and T, respectively, the function checks whether S[i:i+l] is equivalent to T[j:j+l].

This reduces the memoization key to (i, j, l). For strings of length up to 2e5, the possible values of l are up to 2e5. For each l, the number of possible pairs (i, j) depends on the length of the strings. However, in the worst case, this could be O(n^3) entries, which is impossible.

But in practice, the recursive approach may reuse the same (i, j, l) multiple times, but for large l, this is unlikely.

Thus, this approach may not be feasible.

Alternative Idea: Implement the recursive equivalence check with memoization, but only for the current pair of strings and their substrings. Since the problem has two fixed input strings, we can memoize the equivalence of their substrings by their start indices and length. For example, for a substring of S starting at i with length l, and a substring of T starting at j with length l, memoize the result of their equivalence.

This way, the memoization key is (i, j, l). The total number of possible keys is O(n^2), which for n=2e5 is 4e10, which is impossible.

Thus, this approach is not feasible.

So, the only feasible approach seems to be to proceed with the canonical form approach, generating the canonical form for each string and comparing them. But how to compute this efficiently.

Let's try to implement the canonical form approach and see if it works for the given examples.

For example, let's compute the canonical form for 'aaba' and 'abaa'.

For 'aaba' (length 4):

Split into 'aa' and 'ba'.

Compute canonical for 'aa' (length 2 → split into 'a' and 'a'. Canonical form is sorted 'a' and 'a' → 'aa').

Compute canonical for 'ba' (split into 'b' and 'a'. sorted → 'ab').

Then, sort the two canonical forms 'aa' and 'ab' → 'aa' comes first. So the canonical form for 'aaba' is 'aaab'? Wait, no. Wait, the canonical form is the sorted combination of the two sub canonical forms. So 'aa' and 'ab' are sorted, so 'aa' comes first, then 'ab' → concatenated as 'aaab'?

No, wait, the canonical form for the even-length string is the sorted combination of the two sub canonical forms. So 'aa' and 'ab' are the two parts. Since 'aa' comes before 'ab' lex order, the canonical form for 'aaba' is the concatenation of 'aa' and 'ab', which is 'aaab'.

Wait, but 'ab' is the canonical form of 'ba'. So the two sub canonical forms are 'aa' and 'ab'. When sorted, since 'aa' comes before 'ab', the canonical form of 'aaba' is 'aaab'.

For 'abaa' (length 4):

Split into 'ab' and 'aa'.

Canonical of 'ab' is 'ab' (split into 'a' and 'b' → sorted as 'ab').

Canonical of 'aa' is 'aa'.

Sorted combination of 'ab' and 'aa' → 'aa' comes first. So the canonical form is 'aaab' → same as 'aaba', so they are equivalent.

Which matches the first sample's output.

The second sample input: aabb and abab.

For 'aabb':

Split into 'aa' and 'bb'.

Canonical of 'aa' is 'aa'.

Canonical of 'bb' is 'bb'.

Sorted combination is 'aabb'.

For 'abab':

Split into 'ab' and 'ab'.

Canonical of 'ab' is 'ab' (split into 'a' and 'b' → sorted as 'ab').

Sorted combination of 'ab' and 'ab' is 'abab'.

So 'aabb' and 'abab' have different canonical forms, hence output is NO.

So the approach works for these cases.

But for large inputs, the canonical form can be very large, leading to O(n log n) time and space. For example, a string of length 2^18 would have a canonical form of length 2^18 * 18. But 2^18 is 262,144 → 262,144 * 18 is 4,718,592 characters. Storing and comparing two such strings in Python may be manageable but will take some time.

But given the time constraints (2 seconds), and Python's speed, this may be tight but acceptable. So the plan is:

- For each input string, compute its canonical form recursively.

- Compare the two canonical forms. If equal, output YES, else NO.

Implementing this in Python.

But how to compute the canonical form efficiently.

The recursive approach for canonical form:

def compute_canonical(s):

    n = len(s)

    if n % 2 != 0:

        return s

    half = n // 2

    left = compute_canonical(s[:half])

    right = compute_canonical(s[half:])

    if left < right:

        return left + right

    else:

        return right + left

But in Python, for large n, this will generate very large strings. For example, for n=2e5, the function will generate a string of size O(n log n), which could be up to 2e5 * 18 = 3.6e6. For n=2e5, this would take O(n log n) time. For 3.6e6 characters, each concatenation is O(k) where k is the length of the strings. For each split level, the total time is O(n) (since for each split, the sum of all string operations is O(n)), and there are O(log n) levels, so total time is O(n log n), which for n=2e5 is about 2e5 * 18 = 3.6e6 operations, but each operation involves string concatenations of growing sizes.

In Python, string concatenation is O(k), so for each split level, the time is O(n), leading to O(n log n) time. For 2e5, this is 2e5 * 18 ≈ 3.6e6 steps. Python can handle about 1e8 operations per second, so 3.6e6 should take about 0.036 seconds, which is acceptable.

But for each split, the code is splitting the string into two halves. For example, for the initial string of length 2e5, the first split is into two 1e5-length strings. Each of those is split into two 5e4-length strings, and so on. The split operations in Python (s[:half] and s[half:]) are O(k) time, where k is the length of the string. So for each split, the time is O(k) for each recursive call. The total time is sum_{k=1 to log n} 2^{k} * (n/2^{k}) ) → sum of n for each level → O(n log n) time.

But in practice, for Python, this approach may be too slow. For example, for a string of length 2e5, the code will split it into two 1e5-length strings, which takes O(2e5) time. Then each of those splits into two 5e4-length strings, which takes 2 * O(1e5) time. And so on. The total time is O(n log n) time.

But what is the actual running time for a 2e5-length string in Python?

Alternatively, perhaps we can memoize the canonical forms for each substring, but given the problem constraints, this is not feasible.

Another Idea: To avoid generating the entire canonical form string, compute a hash that uniquely represents it. For example, compute a hash for each canonical form, and compare the hashes. But the hash must uniquely represent the canonical form to avoid collisions.

In Python, using a perfect hash is not feasible, but using a tuple of hashes can help. For example, for each even-length string, compute the hash as a sorted pair of the two child hashes. But this approach would allow comparing the hashes instead of the full canonical form strings.

Let's try to implement this:

def compute_hash(s):

    n = len(s)

    if n % 2 != 0:

        return hash(s)

    half = n // 2

    h_left = compute_hash(s[:half])

    h_right = compute_hash(s[half:])

    if h_left <= h_right:

        return hash( (h_left, h_right) )

    else:

        return hash( (h_right, h_left) )

Then, the two strings are equivalent if their hashes are equal.

But hash collisions could occur. For example, two different canonical forms could have the same hash. However, the probability of collision is low, especially if using a cryptographic hash or a tuple-based hash. But since Python's built-in hash is not collision-resistant for large data, this approach is not reliable.

Alternative Idea: Use a tuple to represent the hash structure. For example, for odd-length strings, the hash is the string itself. For even-length strings, the hash is a sorted tuple of the left and right hash tuples. Then, two strings are equivalent if their hash tuples are equal.

This approach would avoid generating large strings and instead work with tuples. Comparing tuples in Python is done recursively, which could be efficient enough.

Let's implement this:

def compute_canonical_tuple(s):

    n = len(s)

    if n % 2 != 0:

        return (s,)

    half = n // 2

    left = compute_canonical_tuple(s[:half])

    right = compute_canonical_tuple(s[half:])

    if left < right:

        return (left, right)

    else:

        return (right, left)

Then, compare the two tuples. If they are equal, output YES.

But for large strings, this will generate deep tuples, which may be slow to compare. But for the problem's constraints, it may be manageable.

Testing this approach for the first sample input:

For 'aaba' → split into 'aa' and 'ba'.

'aa' splits into 'a' and 'a' → ('a',) and ('a',) → sorted, so ('a', 'a').

'ba' splits into 'b' and 'a' → ('b',) and ('a',) → sorted → ('a', 'b').

So the tuple for 'aaba' is (('a', 'a'), ('a', 'b')).

For 'abaa' → split into 'ab' and 'aa'.

'ab' splits into 'a' and 'b' → sorted → ('a', 'b').

'aa' is ('a', 'a').

Sorted combination of ('a', 'b') and ('a', 'a') → ('a', 'a') comes first. So the tuple is (('a', 'a'), ('a', 'b')).

So the tuples are equal, so output is YES.

This works.

For the second sample input:

'aabb' → split into 'aa' and 'bb'. Their tuples are (('a','a'), ('b','b')).

'abab' → split into 'ab' and 'ab', each becomes (('a','b'), ('a','b')), which when sorted becomes (('a','b'), ('a','b')).

So the tuples are different.

Thus, this approach works.

But the time and memory efficiency depends on the depth of the tuples and the comparison time.

But for large strings, the tuples can have a depth of O(log n), and each node in the tuple has two children. Comparing two such tuples for equality would take O(1) time if the top-level tuples are different, but O(d) time for the depth d if they are the same. For equivalent strings, this would require comparing the entire structure, which is O(log n) time. For non-equivalent strings, it may exit early.

So the time to compare the tuples would be acceptable.

Thus, the plan is:

- Compute the canonical tuple for each string.

- Compare the two tuples. If equal, output YES, else NO.

But in Python, comparing tuples is done element-wise, and for large tuples, this could be efficient.

But how to implement this in Python.

Let's try to implement the compute_canonical_tuple function.

But for the code to handle very large strings, it's important to avoid deep recursion. Python's default recursion depth is around 1e4, which is sufficient for len(s) up to 2^14 (16384). But for len(s) up to 2e5 (which is 200,000, which is about 2^18), the recursion depth would be 18, which is within Python's default recursion limit.

Thus, recursion should not be a problem.

So the code would look something like:

def main():

    import sys

    s = sys.stdin.readline().strip()

    t = sys.stdin.readline().strip()

    if len(s) != len(t):

        print("NO")

        return

    def canonical_tuple(s):

        n = len(s)

        if n % 2 == 1:

            return (s,)

        half = n // 2

        left = canonical_tuple(s[:half])

        right = canonical_tuple(s[half:])

        return (left, right) if left <= right else (right, left)

    ct_s = canonical_tuple(s)

    ct_t = canonical_tuple(t)

    print("YES" if ct_s == ct_t else "NO")

But wait, no. The canonical_tuple function returns a nested tuple. For example, for 'ab', it returns (('a',), ('b',)) but sorted. So the tuples are compared recursively.

Yes.

But for large strings, the nested tuples can be deep, but Python can handle comparing them.

Testing this code with the sample inputs:

Sample Input 1:

aaba

abaa

The canonical tuples would be equal, so output is YES.

Sample Input 2:

aabb

abab

Canonical tuples are different, so output is NO.

Thus, the code works for the samples.

But what about the time and memory constraints.

For a string of length 2e5, each recursive call to canonical_tuple splits the string into two halves, and builds a tuple of two elements. Each split is O(k) time, where k is the current substring length. The total time is O(n log n). But in Python, string slicing (s[:half] and s[half:]) creates new strings, which for large k can be time-consuming. For example, splitting a string of length 1e5 into two 5e4-length strings requires copying 1e5 characters, which is O(k) time.

Thus, the time complexity is O(n log n), which for n=2e5 is about 2e5 * 18 = 3.6e6 operations. But each split involves slicing, which is O(k) time. So the total time would be O(n log n) * O(n), which is O(n^2 log n), which is way too slow.

Wait, no. The split into two halves for a string of length k takes O(k) time. So for each recursive call for a string of length k, the time is O(k) for the splits. The recurrence is T(k) = 2*T(k/2) + O(k). The solution to this recurrence is T(k) = O(k log k). So for a string of length n, the total time is O(n log n). But how does this fit with the split times?

Yes. The recurrence is T(n) = 2*T(n/2) + O(n). This sums to O(n log n) time. So for n=2e5, it's 2e5 * 18 ≈ 3.6e6 operations. But each operation (splitting the string into two halves) is O(n) time. So for a string of length n, each split takes O(n) time, but this happens log n times. So the total time is O(n log n) time. 

But in Python, string slicing is O(k) for a slice of length k. So for a string of length 2e5, the first split is O(2e5), then two splits of O(1e5) each, and so on. The total time is O(n log n) time, which is acceptable.

But for 2e5, 2e5 * log2(2e5) ≈ 2e5 * 18 = 3.6e6. In Python, each operation is about 1e6 per second. So 3.6e6 operations would take about 3.6 seconds, which is over the 2-second time limit.

So this approach may not be feasible for the largest inputs.

Thus, we need a more optimized approach.

Alternative Idea: Instead of creating new strings for each split, use indices to represent the substring. For example, pass the original string and start and end indices to the recursive function, avoiding creating new substrings. This way, splitting is O(1) time.

But in Python, strings are immutable, so accessing a substring via indices is O(1) time? No, in Python, slicing creates a new string, which is O(k) time. So this approach would not help.

Another Idea: Precompute all possible split positions and memoize the hashes, but this is not feasible for large n.

Alternative Idea: Use a bottom-up approach. For each possible length (starting from 1, then 2, 4, etc.), compute the canonical form for all substrings of that length. For length 1, the canonical form is the character. For even lengths, combine the canonical forms of the two halves. But this requires storing the canonical forms for each position and length, which is O(n log n) space. For 2e5, this is feasible.

But how to implement this.

For example, for a string of length 8, we can process the canonical forms for length 1, 2, 4, 8.

For each position i and length l, compute the canonical form for the substring s[i:i+l].

This can be done in a dynamic programming manner.

But for large n, storing all possible canonical forms is not feasible. For example, for length 2e5 and log2(n) levels, the total storage is O(n log n), which is manageable.

But in practice, for each even length l, each substring of length l is formed by two substrings of length l/2. For each such substring, compute the canonical form by combining and sorting the canonical forms of the two halves.

But this approach can be implemented using memoization with indices and lengths.

Let's see:

We can create a 2D array dp where dp[l][i] represents the canonical form of the substring starting at index i with length l.

For l=1: dp[1][i] = s[i]

For l even: dp[l][i] = sorted combination of dp[l/2][i] and dp[l/2][i + l/2]

For l odd: dp[l][i] = s[i:i+l]

But for l up to 2e5, and for each l, i ranges up to n - l, this requires O(n log n) space, which for 2e5 log(2e5) is about 2e5 * 18 = 3.6e6 entries. Each entry is a string, which can be up to l characters long. But for l=2e5, the string is 2e5 characters, leading to O(n^2) storage, which is impossible.

Thus, this approach is not feasible.

Thus, we need a way to compute the canonical form without generating the entire string or tuple, which brings us back to the recursive approach but with optimizations.

Alternative Idea: Implement the recursive approach but with memoization of the canonical form for each substring. However, since the same substring may appear in multiple places, memoization can help. For example, for the input strings s and t, we can memoize the canonical form for each possible substring.

But again, for large n, this is not feasible.

Alternative Idea: Instead of using strings, use hashing at each step. For example, compute a hash for each substring that uniquely represents its canonical form. For even-length substrings, combine the hashes of the two halves (sorted) to compute the hash for the current substring. For odd-length, use the hash of the substring itself.

This way, two equivalent substrings will have the same hash.

But the problem is ensuring that hash collisions are unlikely. To mitigate this, use a combination of two hash values (e.g., using a tuple of two different hash functions) or a larger hash.

But in practice, for the problem's constraints, using a single hash function with a good distribution may suffice.

Implementing this:

For each substring, compute its hash recursively:

def compute_hash(s):

    memo = {}

    def helper(lo, hi):

        if (lo, hi) in memo:

            return memo[(lo, hi)]

        n = hi - lo

        if n % 2 != 0:

            # odd length, hash of substring s[lo:hi]

            res = hash(s[lo:hi])

            memo[(lo, hi)] = res

            return res

        mid = lo + n // 2

        left = helper(lo, mid)

        right = helper(mid, hi)

        res = hash(tuple(sorted((left, right))))

        memo[(lo, hi)] = res

        return res

    return helper(0, len(s))

But even with memoization, for a string of length 2e5, the number of possible (lo, hi) pairs is O(n^2), which is 4e10, which is impossible.

Thus, this approach is not feasible.

Thus, the only feasible approach seems to be the recursive canonical form approach with strings or tuples, but optimizing it to avoid unnecessary string copies.

But in Python, string slicing is unavoidable and expensive for large strings.

Alternative Idea: Use a different data structure to represent the string, such as a linked list, but this would complicate the code and may not provide a significant speedup.

Thus, the best approach for this problem is to implement the canonical form approach using recursion with string slicing, but in Python, this may be too slow for the largest inputs.

But according to the problem statement, the solution must read input from stdin, write to stdout, and be efficient.

Alternative Idea: Precompute the canonical form for both strings using iterative dynamic programming, building up from the smallest substrings.

For example:

For each possible length l in increasing order:

   for each possible starting index i:

      compute the canonical form for the substring s[i:i+l].

This way, we can compute canonical forms for all possible substrings, but again, this is O(n^2) time and space, which is impossible.

Thus, back to the original recursive approach.

Perhaps, in Python, the string slicing and concatenation can be optimized. For example, using mutable data structures like lists to build the canonical form.

Let's try to reimplement the canonical form using lists.

For example:

def compute_canonical_list(s):

    n = len(s)

    if n % 2 != 0:

        return list(s)

    half = n // 2

    left = compute_canonical_list(s[:half])

    right = compute_canonical_list(s[half:])

    if left <= right:

        return left + right

    else:

        return right + left

Then, compare the two lists.

But converting the lists to a tuple for comparison may be more efficient. However, in Python, comparing lists is done element-wise, which is O(k) time for lists of length k. So for large lists, this is O(k) time.

But for a string of length 2e5, the canonical list could have O(n log n) elements. For example, each split adds the two sublists, leading to O(n log n) elements. For 2e5, this could be up to 3.6e6 elements. Comparing two such lists would take O(3.6e6) time, which is expensive.

Thus, this approach may not be better.

Thus, the original approach using strings is the best possible, but perhaps can be optimized.

Another Idea: Note that the order of processing the two halves (sorted) allows us to compare the canonical forms of the two halves directly. Thus, we can memoize the canonical form for a given string to avoid recomputing it multiple times. But for large strings, this is not feasible.

But for the problem, we have two input strings. We need to compute their canonical forms. If we can find a way to compute them efficiently, perhaps by using a divide-and-conquer approach and avoiding unnecessary string operations.

But in Python, even with the best optimizations, the recursive approach may not be feasible for the largest inputs.

Thus, the only way to proceed is to implement the recursive approach and hope that it is efficient enough.

But given the problem's constraints, the recursive approach with canonical forms may not be feasible for the largest inputs. So perhaps there's a smarter way to model the equivalence.

Alternative Idea: The equivalence can be checked by comparing the strings' minimal forms, which can be computed by recursively splitting and sorting the halves. Thus, the minimal form is the lex smallest possible string that can be formed by recursively splitting and sorting the halves.

Thus, for each string, compute its minimal form. If the minimal forms of the two strings are equal, they are equivalent.

This is what the canonical form approach does. Thus, the minimal form approach is the same as the canonical form approach.

Thus, the code must be written as efficiently as possible.

Thus, the final code will be:

Read the two input strings.

If their lengths are different, return NO.

Compute the canonical form of each string.

Compare the canonical forms.

Output YES or NO.

Implementing this in Python.

But how to compute the canonical form efficiently.

In Python, string concatenation is expensive. So, perhaps using a different data structure, such as a deque, or a list, to accumulate the characters can help.

Alternatively, represent the canonical form as a tuple of characters. But this would still require O(n log n) time and space.

But the code is required to be in Python, which may not be the best language for this problem. However, the code must be written.

But let's think about the following example: for a string of length 2^k, the canonical form is built by recursively splitting and sorting the halves. For example, each split combines the sorted sub canonical forms. But for a string of length 4, the canonical form is the sorted combination of the two halves' canonical forms.

Thus, the code can be written as follows:

def canonical(s):

    n = len(s)

    if n % 2 == 1:

        return s

    half = n // 2

    a = canonical(s[:half])

    b = canonical(s[half:])

    if a <= b:

        return a + b

    else:

        return b + a

s = input().strip()

t = input().strip()

if len(s) != len(t):

    print("NO")

else:

    print("YES" if canonical(s) == canonical(t) else "NO")

But for large inputs, this code will be too slow.

Thus, what can be done to optimize this code?

Alternative Idea: Prune cases where the two strings are already equal. If the input strings are equal, return YES immediately.

But this may not help for large inputs where the strings are not equal but have the same canonical form.

Alternative Idea: Check if the two strings have the same multiset of characters. If not, return NO. This can be done quickly.

Thus, adding this step can help in some cases.

But the problem is that even if the multiset is the same, the strings may not be equivalent. But it's a quick check.

Thus, the code can be modified as follows:

from collections import Counter

s = input().strip()

t = input().strip()

if len(s) != len(t):

    print("NO")

elif Counter(s) != Counter(t):

    print("NO")

else:

    # proceed to compute canonical forms

    pass

But this adds O(n) time for the Counter, which is acceptable.

But this is a necessary condition, not sufficient. So, in cases where the multiset is different, return NO. Otherwise, proceed.

But in the worst case, this does not help.

Thus, this optimization is worth adding.

Thus, the code becomes:

from collections import Counter

def canonical(s):

    n = len(s)

    if n % 2 == 1:

        return s

    half = n // 2

    a = canonical(s[:half])

    b = canonical(s[half:])

    return a + b if a <= b else b + a

s = input().strip()

t = input().strip()

if len(s) != len(t):

    print("NO")

elif Counter(s) != Counter(t):

    print("NO")

else:

    print("YES" if canonical(s) == canonical(t) else "NO")

But even with this, for large inputs, the canonical function will take O(n log n) time and generate large strings.

But in Python, even this may be too slow. For example, for n=2e5, the code will make 2e5 log 2e5 operations, which may not fit into the 2-second time limit.

Thus, the problem requires a more efficient approach.

Alternative Idea: Implement the canonical form using memoization with hashing, and compare the hashes.

But even this may not help.

Thus, perhaps the problem requires a different approach.

Alternative Idea: The equivalence check can be done using a hash of the canonical form, computed in a way that avoids building the entire string. For example, compute a hash that combines the hashes of the two sorted sub-hashes. This way, the hash can be computed recursively without generating large strings.

Thus, the code can compute a hash for each substring, which is based on the sorted hashes of the two halves. This approach uses integers for the hash values, which are faster to compute and compare.

But to avoid hash collisions, use a tuple of two different hash functions. For example, for a string of length n, compute two hash values and combine them. This reduces the chance of collisions.

But in practice, using a single hash may suffice for the problem's constraints.

Thus, the code can be rewritten as follows:

from collections import Counter

def compute_hash(s):

    def helper(lo, hi):

        n = hi - lo

        if n % 2 == 1:

            # Use a hash of the substring

            return hash(s[lo:hi])

        mid = (lo + hi) // 2

        left = helper(lo, mid)

        right = helper(mid, hi)

        if left <= right:

            return hash((left, right))

        else:

            return hash((right, left))

    return helper(0, len(s))

s = input().strip()

t = input().strip()

if len(s) != len(t):

    print("NO")

elif Counter(s) != Counter(t):

    print("NO")

else:

    hash_s = compute_hash(s)

    hash_t = compute_hash(t)

    print("YES" if hash_s == hash_t else "NO")

But this approach uses Python's built-in hash function, which is not reliable for large data due to collision possibilities. For example, different canonical forms could hash to the same value.

Thus, this approach may not be correct.

Alternative Idea: Use a perfect hash. For example, use a tuple of the canonical form's structure. Thus, the hash is the canonical tuple itself. But comparing tuples may be expensive.

Thus, the code must compute the canonical tuple and compare them.

But for large inputs, this is the only way to ensure correctness.

Thus, the final code would be:

from collections import Counter

def canonical(s):

    n = len(s)

    if n % 2 == 1:

        return (s,)

    half = n // 2

    a = canonical(s[:half])

    b = canonical(s[half:])

    return (a, b) if a <= b else (b, a)

s = input().strip()

t = input().strip()

if len(s) != len(t):

    print("NO")

elif Counter(s) != Counter(t):

    print("NO")

else:

    print("YES" if canonical(s) == canonical(t) else "NO")

But for large n, this code will generate deep tuples, which may be compared efficiently in Python.

Testing this code with the sample inputs:

Sample Input 1:

aaba

abaa

The canonical tuples for both are ((('a',), ('a',)), (('a',), ('b',))). 

Sample Input 2:

aabb

abab

The canonical tuple for 'aabb' is ((('a',), ('a',)), (('b',), ('b',))), and for 'abab' is ((('a',), ('b',)), (('a',), ('b',))). Thus, they are different.

Thus, the code works for these cases.

But for large inputs, the code may be slow.

But given the problem's time constraints and Python's speed, this may be the best possible approach.

Thus, the final code is as written.
</think>

```python
from collections import Counter

def main():
    import sys
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    if len(s) != len(t):
        print("NO")
        return
    
    if Counter(s) != Counter(t):
        print("NO")
        return
    
    def canonical_tuple(s):
        n = len(s)
        if n % 2 != 0:
            return (s,)
        half = n // 2
        left = canonical_tuple(s[:half])
        right = canonical_tuple(s[half:])
        return (left, right) if left <= right else (right, left)
    
    ct_s = canonical_tuple(s)
    ct_t = canonical_tuple(t)
    
    print("YES" if ct_s == ct_t else "NO")

if __name__ == "__main__":
    main()
```