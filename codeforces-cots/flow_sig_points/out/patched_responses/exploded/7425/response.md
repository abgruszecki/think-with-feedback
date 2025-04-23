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

Another sample:

Input 'aabacaabbad' → output 4, then 14,19,28,5.

So d_total=4.

Compute at_most[1], at_most[2], at_most[3], at_most[4].

Then exact[1] = at_most[1], exact[2] = at_most[2] - at_most[1], etc.

But how to verify these numbers? Well, the sample shows that for k=4, the exact is 5. So at_most[4] - at_most[3] =5. Which implies that at_most[4] is the total number of substrings (since all substrings can have up to 4 distinct characters). Let's compute that. The length of the input is len('aabacaabbad') → let's count:

a a b a c a a b b a d → 11 characters.

The total number of substrings is n*(n+1)/2 = 11*12/2 =66. So at_most[4] is 66. Then at_most[3] would be 66-5=61. Then exact[3] is at_most[3] - at_most[2] =28, so at_most[2] is 61-28=33. And so on.

But I think the code would handle it correctly.

Now, potential optimizations.

The current code calls count_at_most_k for each k from 1 to d_total. Each call is O(n) time. But perhaps there's a way to compute all at_most values in a single pass. But I don't think so. The sliding window approach for different k's are independent.

Another optimization: since the maximum possible k is 26, and each call is O(n), it's manageable.

But in Python, loops over 3e5 characters can be slow. So using a precompiled list of the ord values might speed things up. For example, converting the string to a list of integers (0-25) once, and then processing that.

Yes. So, for example, converting the string s into a list of ordinals once can save time in the loops. Because in each function call, we have to convert each character to an integer. So for each function call, for each character, ord(s[right]) is called. But if we precompute this once, then each function can use the precomputed list.

So modifying the code:

pre_s = [ord(c) - ord('a') for c in s]

Then, in the count_at_most_k function, instead of s, we pass pre_s. So inside the function:

for right in range(len(pre_s)):

    c = pre_s[right]

Similarly for the left_c.

This saves the time of converting characters to integers each time.

This can save some time in Python, as ord is called once per character, not once per function call per character.

So, integrating that into the code:

s = input().strip()

pre_s = [ord(c) - ord('a') for c in s]

d_total = len(set(pre_s))  # since each element is 0-25, but the number of unique elements is the same as the original string.

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

Then, the loop for k in 1 to d_total:

at_most = [0]*(d_total +1)

for k in range(1, d_total+1):
    at_most[k] = count_at_most_k(pre_s, k)

This should be more efficient as it avoids recomputing ord(c) each time.

Another optimization: the 'count' array can be reused between function calls. However, since each call to count_at_most_k is for a different k, and each call is independent, it's better to reset the count array for each function call. So the code above is correct.

Another point: in Python, list comprehensions and pre-processing can speed up the code. For example, pre_s is a list of integers, which is fast to access.

Now, considering the memory constraints. The pre_s array is O(n), which for n=3e5 is acceptable. 3e5 integers is about 2.4MB (each int is 28 bytes in Python, but lists have some overhead). For 3e5 elements, that's manageable.

So the code should work within the memory limit.

Now, putting all together.

The code steps are:

1. Read the input string.

2. Precompute pre_s as list of integers (0-25).

3. Compute d_total as the number of unique elements in pre_s.

4. Compute at_most for k from 1 to d_total.

5. Compute exact counts as at_most[k] - at_most[k-1].

6. Output d_total followed by each exact count in order.

Testing this code against the samples.

Sample 1:

Input: abca → pre_s is [0, 1, 2, 0].

d_total is 3.

count_at_most_k for k=1:

current_distinct starts at 0.

At right=0 (c=0):

count[0] was 0 → current_distinct becomes 1. Add 1 to count[0]. Since current_distinct (1) is not >k (1), proceed. res += 1-0+1=1.

Wait, wait. Wait, the code adds (right - left +1) to res. Because the number of substrings ending at right is (right - left +1). For right=0, left is 0: 0-0+1=1. res is 1.

Then right=1 (c=1):

count[1] is 0 → current_distinct becomes 2. Now current_distinct (2) >k (1). So enter the while loop.

Move left: left=0. left_c is 0. count[0] is decremented to 0. current_distinct becomes 1. left becomes 1. Now, current_distinct is 1 <=1. So exit loop.

Add (1-1+1) =1. res is 2.

Right=2 (c=2):

count[2] is 0 → current_distinct becomes 2. Enter loop. current_distinct (2) >1.

Decrement left_c (pre_s[1] is 1). count[1] was 1. Now 0. current_distinct becomes 1. left becomes 2. Add (2-2+1) =1. res is 3.

Right=3 (c=0):

count[0] is 0 → current_distinct becomes 2. Enter loop. left=2. left_c is pre_s[2] =2. count[2] is 1 → decrement to 0. current_distinct becomes 1. left becomes 3. Add (3-3+1) =1. res is 4. So for k=1, returns 4.

Similarly for k=2 and k=3, which gives the correct results.

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