<think>
Okay, I need to solve this problem where I have to count the number of powerful substrings in a given string. A powerful substring is one that starts with "heavy" and ends with "metal". The key here is to find all possible substrings that meet both conditions.

Hmm, let's think. The substring has to start with "heavy" and end with "metal", and those two parts can overlap in the string. So the approach should be to first find all the positions where "heavy" occurs, then all the positions where "metal" occurs. Then, for every occurrence of "heavy" that is before an occurrence of "metal", we can count one powerful substring. Because any "heavy" that comes before a "metal" will form a valid substring from the start of "heavy" to the end of "metal".

So the steps would be:

1. Iterate through the string and collect all the indices where "heavy" starts.
2. Iterate through the string again and collect all the indices where "metal" starts. Then, since "metal" is 5 letters long (wait, "metal" is 5 letters? Wait, 'm','e','t','a','l'— yes, 5 letters. Wait no: m, e, t, a, l— that's 5 letters? Let me count. m is 1, e 2, t 3, a 4, l 5. Oh right, so the substring "metal" is 5 characters long. So the starting index of "metal" would be at position i, and the substring is from i to i+5-1 = i+4. So the end index is i+4.

Wait, but for a substring to end with "metal", the "metal" must be the ending part. So the substring must include the "metal" part. So the start of the substring can be any "heavy" occurrence's start, and the end must be the end of a "metal" occurrence. So for each "heavy" at position i, any "metal" that starts at position j where j >= i + 5 (since "heavy" is 5 letters long? Wait, "heavy" is h,e,a,v,y— that's 5 letters. So the "heavy" starts at i and ends at i+4. Then, the "metal" can start at any j >= i+5. Wait, no. Because the substring has to start with "heavy" and end with "metal". So the "metal" part can start at any j >= i, as long as the substring includes both. Wait, but the substring must start with "heavy" (so the first 5 characters of the substring are 'heavy'), and end with 'metal' (the last 5 characters of the substring are 'metal'). So the entire substring is from the start of "heavy" to the end of "metal". So the substring starts at i (start of heavy) and ends at j+4 (since "metal" starts at j and ends at j+4). So the substring is s[i..j+4], inclusive. So for any i (start of heavy) and j (start of metal), as long as j >= i. Because even if j is before i, that would mean the metal is before the heavy, which is impossible. Wait, no. Suppose heavy starts at i and metal starts at j. For the substring to start with heavy and end with metal, the start of metal must be after or equal to the start of heavy. Because the heavy is the start. So the substring would start at i, and the metal's start j must be >= i, but also, the metal's end is j+4. So the substring must start at i and end at j+4. So the metal's start j can be anywhere, but j must be >= i (so that the metal starts after the heavy starts). But also, the heavy's end is i+4. So the metal can start at j >= i, but in order for the metal to be part of the substring, j must be <= i + 4 + ... (Wait, no. Because the substring can start at i, and the metal can start at j, as long as j+4 >= i. So for example, the heavy is from i to i+4, and the metal is from j to j+4. The substring must include both. So the start is i, the end is j+4. So the substring is from i to j+4. For that to be valid, j must be >= i (so that the metal starts after the heavy starts) but the metal's start can be anywhere as long as j+4 is after the heavy's start. Wait, perhaps I'm overcomplicating. The key is that the substring starts with heavy and ends with metal. So any occurrence of heavy and any occurrence of metal where the heavy is before (or overlapping?) but the metal's start is after the heavy's start. Wait, but the substring starts with heavy. So the heavy must be at the beginning of the substring. The substring ends with metal. So the metal must be at the end of the substring. So the heavy's start is the start of the substring. The metal's end is the end of the substring. So the substring is i to j+4, where i is the start of a heavy and j is the start of a metal. And j must be >= i (since the substring starts at i and includes the metal starting at j). But also, j+4 must be >= i. But j can be anywhere >= i. For example, if j is i, then the metal starts at i, but then the heavy and metal overlap. The substring would be from i (heavy's start) to j+4 (i+4). So the length is 5, which is the length of heavy, but then the metal would start at i and take 5 characters. So that would require that the substring is "heavymetal", but that's overlapping. Wait, no. Let's see: the heavy starts at i, is 5 characters. The metal starts at j. For example, if j is i, then the metal starts at i. The substring would be from i to j+4 = i+4. So the substring is 5 characters long. So the heavy is at i (5 chars), and the metal is at j=i (5 chars). But that would require that the first 5 characters are both "heavy" and "metal". Which is impossible unless "heavy" and "metal" are the same. Which they are not. So in practice, the j must be such that the metal's start is >= i, and j+4 must be >= i (which is always true if j >=i). Wait, j can be i. Then the substring would be from i to i+4, which is 5 characters. So that's the same as the heavy. But then the substring would need to end with metal, which is 5 characters. So in that case, the substring is the same as the heavy, but the substring would need to end with metal. Which is possible only if the heavy is "metal", which it's not. So in reality, j must be such that the metal starts after the heavy starts, but the substring includes both.

Wait, perhaps a better approach is to collect all the indices where "heavy" occurs, and all the indices where "metal" occurs, and then for each "heavy" index, count how many "metal" indices are >= that "heavy" index. Because for a heavy at i, any metal that starts at j >= i will form a valid substring. Because the substring starts at i (the start of heavy) and ends at j+4 (the end of metal). So the metal's start can be anywhere >= i. But the metal itself is 5 characters long. So the j must be such that j+4 < len(s), so the substring is valid.

Wait, but j can be any index where "metal" starts, and j+4 is within the string. So during the collection of metal indices, we check that.

So the steps are:

1. Find all the indices where "heavy" starts. Let's call this list heavy_indices.
2. Find all the indices where "metal" starts. Let's call this list metal_indices.
3. For each index h in heavy_indices, count the number of m in metal_indices where m >= h. Sum all these counts.

Because each such pair (h, m) where m >= h contributes one powerful substring.

So the problem reduces to, for each h, find the number of m in metal_indices that are >= h. Then sum all these numbers.

Now, the key is to do this efficiently. Since the string can be up to 1e6 characters, and the heavy and metal lists can be O(n) in size.

But how do we efficiently compute for each h in heavy_indices, the number of m >= h in metal_indices?

The metal_indices list is sorted, since we process the string from left to right. So for each h, we can perform a binary search in the metal_indices list to find the first m >= h, and then the count is the number of elements from that position to the end.

So if we pre-sort the metal_indices list (which it is, since we collect them in order), then for each h, we can use bisect_left to find the insertion point of h in metal_indices, and the number of elements from that insertion point onwards is the count.

So the steps:

Collect heavy_indices by scanning the string for "heavy" starting at each possible index. Similarly for metal_indices.

Once we have the two lists, we can iterate through each h in heavy_indices, and use binary search on the metal_indices to find how many m's are >= h. Sum all those counts.

Now, the time complexity.

For collecting heavy_indices: O(n), where n is the length of the string. Because for each i from 0 to len(s)-5 (since "heavy" is 5 letters), check if s[i:i+5] == "heavy". Similarly for "metal", which is 5 letters (wait, "metal" is 6 letters? Wait, 'm','e','t','a','l' is 5 letters. So yes, 5 letters. So for "metal", check s[i:i+5] == "metal".

So for each i from 0 to len(s)-5 inclusive, check for the substring. So for n characters, the loop runs up to len(s)-5. For n up to 1e6, that's O(n) steps.

Once we have the lists, the metal_indices are sorted. For each h in heavy_indices, binary search is O(log m), where m is the number of metal_indices. The total time for this part is O(k log m), where k is the number of heavy_indices.

In the worst case, k is O(n) and m is O(n). So total time is O(n log n), which for n=1e6 is acceptable, because log2(1e6) is ~20, so 1e6 * 20 = 2e7 operations, which is manageable within 2 seconds.

So this approach should work.

Now, the implementation.

First, how to collect heavy_indices and metal_indices.

In Python, for a given string s, we can loop through i from 0 to len(s) - 5 (inclusive) and check if the substring matches "heavy" or "metal".

But for large strings, this might be time-consuming. However, in Python, slicing is O(k) where k is the length of the substring. Since each check is O(5) steps, for n up to 1e6, this is 5e6 operations, which is acceptable.

Alternatively, we can precompute all possible starting positions for "heavy" and "metal" using a sliding window approach.

But the straightforward approach is acceptable here.

So code steps:

Read the input string s.

Collect all i where s starts with "heavy" at i.

Collect all j where s starts with "metal" at j.

Then, for each i in heavy_indices, count the number of j >= i in metal_indices.

Sum all those counts.

Now, for the binary search part. Since metal_indices is sorted, we can use the bisect module in Python.

Import bisect.

For each h in heavy_indices, the number of elements in metal_indices >= h is equal to len(metal_indices) - bisect.bisect_left(metal_indices, h).

So sum all (len(metal_indices) - pos) for each h in heavy_indices.

This gives the total count.

Now, handling the edge cases.

For example, if there are no heavy or metal indices, the answer is zero.

Another example: if a heavy is at position i, but all metals are before i, then those contribute nothing.

Testing the sample input:

First sample input: "heavymetalisheavymetal"

Heavy starts at 0, 10.

Metal starts at 5, 15, 20.

Each heavy index (0 and 10) will count the number of metals >= 0 and >=10.

For 0: metals are 5,15,20. All are >=0. So 3.

For 10: metals are 15,20. So 2. Wait, but 5 is less than 10? No, 5 is 5, which is less than 10. So the metals >=10 are 15 and 20. So 2. So total 3+2=5? Wait the sample output is 3. Wait, this suggests that my approach is wrong.

Wait, wait, what's the first sample input:

The input is "heavymetalisheavymetal".

Breaking it down:

The first part is 'heavy' starts at 0, then 'metal' starts at 5. Then, after some letters, another 'heavy' starts at 10 (assuming the string is "heavymetalisheavymetal"), then 'metal' at 15. Then the final 'metal' starts at 20?

So the heavy indices are 0,10.

The metal indices are 5,15,20.

For each heavy index:

h=0: how many metals are >=0? 5,15,20. 3 metals. So contributes 3.

h=10: metals >=10 are 15,20. 2. So total 3+2=5. But the sample output is 3. So where is the mistake?

Ah, wait, the sample output is 3. Hmm, so this suggests that my approach is wrong. What's the problem here?

Wait, in the first sample input, the correct answer is 3. But according to this approach, the count would be 0's heavy (3 metals) and 10's heavy (2 metals), totaling 5. But the sample output is 3. So clearly, there's a mistake in the approach.

What's the error here?

Ah! Because the metal must be part of the substring that starts with heavy. So the metal's start must be >= the heavy's start, but also, the substring must include the entire metal. So the metal's start can be anywhere >= the heavy's start. But the substring starts at the heavy's start and ends at the metal's end.

Wait, but in the first sample input:

For example, the heavy at 0. The metals are at 5,15,20.

Each of these metals will form a substring starting at 0 and ending at 5+4=9 (for 5), 15+4=19, 20+4=24.

So the substrings are:

0 to 9: 'heavym' (no, wait, 0 to 9 is 10 characters. Let's see: 'heavy' is 5 letters starting at 0 (ends at 4), 'metal' starts at 5 (ends at 9). So the substring from 0 to 9 is 'heavymetal' (5+5=10 letters), which is correct. Then the substring from 0 to 19 (metal starts at 15, ends at 19) would be the entire string up to 19. Then from 0 to 24 (if the string is longer). So each of these metals contributes a valid substring.

Similarly for the heavy at 10, the metals at 15 and 20. So two substrings. So total 3+2=5. But the sample output is 3. So where's the mistake?

Wait, the sample input's output is 3. Let's look at the note:

In the first sample, the string is "heavymetalisheavymetal". The powerful substrings are:

- "heavymetal" (starts at 0, ends at 9)

- "heavymetalisheavymetal" (starts at 0, ends at 20+4=24, if the string is that long?)

Wait, maybe the actual string is longer. Let's see:

The input is given as "heavymetalisheavymetal".

Let's count the letters:

"heavy" is 5 letters, "metal" is 5.

Then "is" is 2, then "heavy" is 5, "metal" is 5.

So the total length is 5+5 + 2 +5 +5 = 22 letters.

So the first 'heavy' starts at 0. Metals are at 5,15,20.

So the substrings would be:

0 to 5+4=9 → 'heavymetal' (valid).

0 to 15+4=19: but the string's length is 22. So 15+4=19 is within the string. So the substring starts at 0, ends at 19. Which includes 'heavymetalisheavymetal'?

Wait, the substring from 0 to 19 is 20 characters. Let's see:

0-4: heavy

5-9: metal

10-11: is

12-16: heavy (assuming starts at 12?)

Wait, no. Let's parse the string:

Original input: "heavymetalisheavymetal"

Breaking it down:

h e a v y m e t a l i s h e a v y m e t a l

Indices 0-4: heavy

Indices 5-9: metal (m at 5, e 6, t7, a8, l9)

Then "is" is i (10) s (11)

Then "heavymetal" starts at 12: h e a v y (indices 12-16), then m e t a l starts at 17 (17-21). So the second metal starts at 17, ends at 21. The third metal is at 22? But the input may not have that. Wait, perhaps the original input is "heavymetalisheavymetal", which would be:

h e a v y m e t a l i s h e a v y m e t a l → length 22 letters.

So the metal starts at 5, 17, 22?

Wait, perhaps I'm miscalculating. Let's count:

After the first "heavymetal" (indices 0-9), then "is" (10-11), then "heavy" starts at 12 (12-16), then "metal" starts at 17 (17-21). Then "metal" again? Or is the input "heavymetalisheavymetal" which would end after the second metal. So the length would be 5+5 + 2 +5 +5 = 22.

So the metals are at 5 (positions 5-9), 17 (17-21), and 22 would be beyond the string. So how is the third metal possible?

Ah, perhaps the sample input is such that there's a third metal. Maybe the input is longer. Let's re-examine the sample input:

The first sample's input is "heavymetalisheavymetal". So the string is "heavymetalisheavymetal". Let's split it into parts.

Looking for "metal" occurrences:

After the first "heavymetal" (0-9), the next part is "is" (10-11). Then "heavymetal" (12-21). So the "heavy" starts at 12, "metal" starts at 17. Then the last part is "metal" again? Wait, perhaps the input is "heavymetalisheavymetal". Let's count:

0-4: heavy

5-9: metal

10-11: is

12-16: heavy

17-21: metal

So the metals are at 5,17. So there are two metals, but the sample output is 3. Wait, the sample output is 3. How does that happen?

Wait, in the note of the first sample, it says that there are three powerful substrings. The first two are "heavymetal" twice, and the entire string.

Ah! So the entire string is also a powerful substring. So the entire string starts with "heavy" (at 0) and ends with "metal" (at 17, or somewhere else? Let's see: the entire string is "heavymetalisheavymetal". The last "metal" is at 17. But the entire string's length is 22 characters. The substring that is the entire string starts at 0, ends at 21. So the last "metal" is at 17-21. So the entire string starts with heavy (0) and ends with metal (17-21). So yes, that's a valid substring.

But according to the approach, when we have heavy indices at 0,12 (assuming the 'heavy' starts at 12?), and metal indices at 5,17, and 22 (if possible), but in this case, the last 'metal' in the input would start at 17. So the metals are 5,17. So for heavy indices 0 and 12:

For h=0, metals >=0 are 5 and 17. So 2.

For h=12, metals >=12 is 17. So 1.

Total is 3, which matches the sample output.

Ah! So the mistake earlier was in the way I collected the heavy and metal indices.

So the problem is that in the first sample, the heavy indices are 0 and 12, and the metal indices are 5, 17, and 22 (if the string is longer). Wait, but in the input "heavymetalisheavymetal", the 'metal's are at 5, 17, and then after the second 'metal' ends at 21 (starts at 17), the input has another 'metal'? Let's see:

The input is "heavymetalisheavymetal".

Breaking down:

After the second 'metal' (17-21), the remaining letters are 'al'? Or is the input "heavymetalisheavymetal" which would have 'heavymetal' (0-9), 'is' (10-11), 'heavy' (12-16), 'metal' (17-21), 'al' (22-23) — but 'al' can't form a 'metal'. So no, in this input, there are two metals: at 5 and 17.

But the sample output is 3. So the third metal is where?

Ah, perhaps the entire string is considered as a substring. So the 'heavy' is at 0, and the last 'metal' is at 17. So the entire string is from 0 to 21. But the sample says that there are three powerful substrings. The first two are "heavymetal" (0-9) and "heavymetalisheavymetal" (0-21), and the third is the substring starting at 12 (the second 'heavy') and ending at 17's metal. So that would be three.

So in that case, the heavy indices are 0 and 12. The metal indices are 5, 17, and also the one at 17 again? Or perhaps the 'metal' starts at 17 and at 22?

Wait, I'm getting confused. Let's re-examine the first sample:

Input: "heavymetalisheavymetal"

The string is as follows:

Indices:

0: h

1: e

2: a

3: v

4: y

5: m

6: e

7: t

8: a

9: l → this is the first 'metal' (starts at 5).

Then 'is' → i at 10, s at 11.

Then 'heavy' starts at 12 (h at 12, e 13, a14, v15, y16).

Then 'metal' starts at 17 (m at 17, e18, t19, a20, l21).

So the entire string is 22 characters long (indices 0-21).

So the metal indices are 5 and 17.

So heavy indices are 0 and 12.

Then, for each heavy:

h=0 → metals >=0 are 5 and 17. So 2.

h=12 → metals >=12 is 17. So 1.

Total 3, which matches the sample output.

Ah! So the problem with the initial approach was that I had incorrectly assumed that the 'metal' indices were 5,15,20 in the first sample, but in reality, the correct ones are 5 and 17.

So the approach is correct as long as the code correctly collects all 'heavy' and 'metal' indices.

So the code needs to find all the starting indices of 'heavy' and 'metal' in the string.

So, for each i from 0 to len(s) - 5 (inclusive), check if s starts with 'heavy' at i. Similarly for 'metal'.

So, in code:

s = input().strip()

heavy = []
metal = []

n = len(s)
for i in range(n - 4):
    if s[i] == 'h':
        if i + 4 < n and s[i:i+5] == 'heavy':
            heavy.append(i)
    elif s[i] == 'm':
        if i + 4 < n and s[i:i+5] == 'metal':
            metal.append(i)

Wait, no. The code must check for substrings of length 5. So 'heavy' is 5 letters, so i can range from 0 to len(s) - 5 (inclusive). So for i in range(len(s) -4):

Wait, len(s) - 5 + 1. For example, if len(s) is 5, then i can be 0.

So the correct loop is for i in range(len(s) - 4):

Wait, len(s) -5 +1 = len(s)-4. Because for a substring of length 5, the starting index can be 0 to len(s)-5. So the loop is for i in range(len(s)-4):

Wait, no. Let's see, for i in 0 to len(s)-5 inclusive. So in Python, the range is range(len(s) -4) because in Python, range is exclusive of the upper bound. For example, len(s)-4 would be the upper bound, but since the loop runs from 0 to len(s)-5, because len(s) -5 +1 is the number of possible positions.

Wait, for example, if the string has length 5: len(s) is 5. Then len(s) -5 =0, so the loop runs from 0 to 0 (inclusive), which is i=0.

So the correct code is:

for i in range(len(s) -4):

    substr = s[i:i+5]

    if substr == 'heavy':

        heavy.append(i)

    elif substr == 'metal':

        metal.append(i)

Wait, but 'metal' is also 5 letters, so the same logic applies.

So the code to collect the indices is:

heavy = []
metal = []

n = len(s)
for i in range(n -4):
    substr = s[i:i+5]
    if substr == 'heavy':
        heavy.append(i)
    elif substr == 'metal':
        metal.append(i)

But in this code, the 'metal' indices are collected in the same loop. So, for example, if a substring is both 'heavy' and 'metal' (which is impossible), but the code would check 'heavy' first and add to heavy.

But that's not possible, so the code is correct.

So in the first sample input, the code will collect:

For i=0: substr is 'heavy' → added to heavy.

i=5: substr is 'metal' → added to metal.

i=12: substr is 'heavy' → added to heavy.

i=17: substr is 'metal' → added to metal.

So heavy = [0,12], metal = [5,17].

Then, for each h in heavy:

h=0: find the number of metals >=0 → 5 and 17 → count 2.

h=12: metals >=12 are 17 → count 1.

Total 3 → correct.

So the code works for the first sample.

Another sample: input "heavymetalismetal" → output 2.

The heavy starts at 0, and the metals are at 5 and 11 (assuming the 'ismetal' part: after 'heavymetalismetal' → 'ismetal' is 'i s m e t a l'? So the 'metal' starts at 10 (positions 10-14). So metals are 5 and 10.

So heavy is [0], metals [5,10].

For h=0: metals >=0 are 5 and 10 → count 2. Which matches the sample output of 2.

Wait, but the sample output is 2. But according to the approach, the sum is 2. But the sample says there are two substrings: 'heavymetal' and the entire string 'heavymetalismetal'.

So the entire string starts at 0 (heavy) and ends at 10+4=14. So the code counts both metals (5 and 10) for h=0, leading to 2, which is correct.

So the approach works.

So the code is correct.

Now, implementing it in Python with optimized code.

But for large strings, the loop can be time-consuming. However, in Python, it's manageable. But using a loop that checks each character for possible 'h' or 'm' can be optimized.

Wait, the current code checks every possible starting index for 5-letter substrings. For a string of length 1e6, this is 999,996 iterations. Each iteration involves slicing 5 characters and comparing to 'heavy' or 'metal'. This is O(n) time but for large n, this is acceptable.

But for optimization, perhaps we can find the positions of 'heavy' and 'metal' more efficiently.

Alternative approach: precompute all indices where 'heavy' starts by scanning the string once, and similarly for 'metal'.

But in Python, the code as written is manageable.

Another thing to consider: the code uses s[i:i+5], which creates a new substring each time. For 5 characters, this is O(5) time per iteration, which for 1e6 iterations is 5e6 operations. Which is acceptable.

But to optimize, perhaps compare the characters directly:

for i in range(len(s) -4):

    if s[i] == 'h' and s[i+1] == 'e' and s[i+2] == 'a' and s[i+3] == 'v' and s[i+4] == 'y':

        heavy.append(i)

    elif s[i] == 'm' and s[i+1] == 'e' and s[i+2] == 't' and s[i+3] == 'a' and s[i+4] == 'l':

        metal.append(i)

This way, we avoid creating the substring and just check the individual characters. This can be faster in Python, as string slicing is O(k) and for small k (like 5) it's manageable, but checking each character can be faster.

So this is a possible optimization.

Thus, the code can be written as:

heavy = []
metal = []
n = len(s)
for i in range(n - 4):
    if s[i] == 'h' and s[i+1] == 'e' and s[i+2] == 'a' and s[i+3] == 'v' and s[i+4] == 'y':
        heavy.append(i)
    elif s[i] == 'm' and s[i+1] == 'e' and s[i+2] == 't' and s[i+3] == 'a' and s[i+4] == 'l':
        metal.append(i)

This approach should be faster as it avoids creating substrings.

Now, once heavy and metal lists are collected, we need to compute the sum of the number of elements in metal that are >= h for each h in heavy.

As the metal list is sorted (since we process i in increasing order), we can use bisect_left for each h.

So the code:

import bisect

count = 0
for h in heavy:
    # find first index in metal >= h
    pos = bisect.bisect_left(metal, h)
    count += len(metal) - pos

print(count)

This should give the correct count.

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    heavy = []
    metal = []
    n = len(s)
    for i in range(n - 4):
        if s[i] == 'h' and s[i+1] == 'e' and s[i+2] == 'a' and s[i+3] == 'v' and s[i+4] == 'y':
            heavy.append(i)
        elif s[i] == 'm' and s[i+1] == 'e' and s[i+2] == 't' and s[i+3] == 'a' and s[i+4] == 'l':
            metal.append(i)

    count = 0
    for h in heavy:
        pos = bisect.bisect_left(metal, h)
        count += len(metal) - pos

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
heavymetalismetal
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

So this code should work.

Now, handling edge cases:

Case where no heavy or no metal: output 0.

Case where a metal starts before a heavy. For example, metal at 0, heavy at 5. Then the code will not count that.

Another case: heavy and metal overlap. For example, heavy starts at i, metal starts at i+3. Then the code will count that, as the code allows any metal >= heavy's start.

But in this case, the substring starts at i, includes the heavy (i to i+4) and the metal starts at i+3. The substring ends at (i+3)+4 = i+7. So the substring includes both parts even if overlapping.

Yes, according to the problem statement, such a substring is valid.

So the code correctly handles overlapping cases.

Now, considering the data structures: using lists and bisect is efficient. The code runs in O(n) for collecting indices, and O(k log m) for counting, which is acceptable for n=1e6.

Now, the final code.

So the code will read the input string, collect heavy and metal indices, then compute the count.

Implementing this in Python.
</think>

```python
import bisect

s = input().strip()
heavy = []
metal = []
n = len(s)
for i in range(n - 4):
    if s[i] == 'h' and s[i+1] == 'e' and s[i+2] == 'a' and s[i+3] == 'v' and s[i+4] == 'y':
        heavy.append(i)
    elif s[i] == 'm' and s[i+1] == 'e' and s[i+2] == 't' and s[i+3] == 'a' and s[i+4] == 'l':
        metal.append(i)

count = 0
for h in heavy:
    pos = bisect.bisect_left(metal, h)
    count += len(metal) - pos

print(count)
```
