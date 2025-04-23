<think>
Okay, I need to solve this problem where I have to find the number of good substrings with even and odd lengths. Let's start by understanding what a good substring is. 

A good substring is one where, after merging all consecutive equal characters, the resulting string is a palindrome. So, for example, "aabba" becomes "aba" after merging, which is a palindrome. The key here is that the merged version must be a palindrome. 

First, I need to figure out what the merged string looks like for any substring. The merged string is formed by replacing consecutive equal characters with a single one. So, the merged string is a sequence of alternating characters. For instance, "aaabbb" becomes "ab". 

Now, for the merged string to be a palindrome, the sequence of characters must read the same forwards and backwards. Since the merged string is made of alternating 'a's and 'b's (because consecutive duplicates are merged), the merged string can be a palindrome in two cases:
1. The merged string has all characters the same. For example, "aaaaa" would merge to "a", which is a palindrome.
2. The merged string alternates between 'a' and 'b' in a way that the entire string is a palindrome. For example, "ababa" (merged as "ababa") is a palindrome. Similarly, "abbaa" would merge to "aba", which is a palindrome.

Wait, wait. Let's think again. Suppose the merged string is like "aba", which is a palindrome. Then the original substring could have any number of consecutive a's and b's as long as they alternate. But when merged, the structure is a palindrome.

So, the merged string must be a palindrome. Let's analyze the structure of the merged string. Let's call the merged string M. For M to be a palindrome, the first and last characters must be the same, and the inner parts must also form a palindrome. But since M is already a sequence of alternating characters, the entire merged string can only be a palindrome if it's either a single character (length 1) or a palindrome where the first and last characters are the same and the rest mirrors accordingly.

Wait, the merged string can be of any length, but since it's formed by merging consecutive duplicates, each adjacent character is different. So, M has no consecutive duplicates. So, for M to be a palindrome:

Case 1: length is 1. Then it's a palindrome. Any substring that merges to a single character is a good substring. For example, "aaa" becomes "a", so it's good.

Case 2: length is greater than 1. Then, since the merged string has no duplicates, the first and last characters must be the same, and the inner parts must form a palindrome. For example, "aba" is a palindrome. "abba" would merge to "ab", which is not a palindrome. Wait, "abba" merges to "ab", but "ab" is not a palindrome. So the original substring's merged version must itself be a palindrome.

So, the merged string is a palindrome when:

- Either its length is 1, or
- Its first and last characters are the same, and the substring between them is also a palindrome (which, for merged strings, would require that the entire structure is symmetric).

Wait, but for a merged string of length k (all characters alternating), the palindrome condition requires that the i-th character equals the (k - i + 1)-th character. So, for example, if the merged string is "ab", then k=2. The first character is 'a', the second is 'b'—so not a palindrome. If the merged string is "aba", then it's a palindrome. If it's "abba" merged to "aba", which is a palindrome.

Wait, no. Let's take the example of the substring "babb" from the third sample input. The sample output includes "bab" as a good substring. Let's see: the substring "bab" would merge to "bab", which is a palindrome. So that's valid.

So, the merged string's structure must be a palindrome. For a merged string of length l:

- If l is 1: yes.
- If l is even: the first half must be a mirror of the second half. But since merged strings have alternating characters, this would require that the first character is the same as the last, the second the same as the second last, etc. For example, "abba" would merge to "ab", which isn't a palindrome. Wait, "abba" as a substring would merge to "ab", which is not a palindrome. So that's not a good substring. But the substring "abab" would merge to "ab", which is not a palindrome. Hmm, maybe I'm getting this wrong.

Wait, let's think about the merged string structure. The merged string is made by collapsing consecutive duplicates, so the merged string alternates between 'a's and 'b's. So, for example, any substring that's a sequence of a's followed by b's followed by a's, etc., will have a merged string that alternates. Now, for this merged string to be a palindrome, the sequence must read the same forwards and backwards. 

In the case where the merged string has an even length, that's impossible. Because, for example, if the merged string is "ab", then the first character is 'a' and the last is 'b'—so not a palindrome. But if the merged string is "aa", that's not possible because consecutive duplicates are merged. Wait, no. The merged string can't have consecutive duplicates, so the merged string's length can be 1, 2, etc., but each character is different from the next. So, the merged string can't have even length unless the first and last characters are the same and the structure is symmetric. Wait, let's take an example.

Suppose the merged string is "aba". Then it's a palindrome. Length is 3 (odd). Another example is "abbaa" which would merge to "aba". That's a palindrome. 

If the merged string is "abab", then the merged string would be "abab" (since each 'a' and 'b' are alternating). This is not a palindrome. The first character is 'a', last is 'b'—so no. So, for even-length merged strings to be palindromes, they must have the same first and last characters. But for even lengths, that would require that the first and last are the same, but how? Let's see. Let's say merged string is of even length l. Then the first character is the same as the last, the second is the same as the second last, etc. But since the merged string alternates, the first and second characters are different. So for even l:

merged string is c1, c2, c3, ..., cl. Since it's even, the first and last characters must be the same. But then, since the merged string alternates, c1 != c2, c2 != c3, etc. So, if the first character is c1, then the second is c2 (different), third is c1 (since it alternates), fourth c2, etc. Wait, no. The merged string is formed by merging consecutive duplicates, so the actual characters can vary. For example, "aabbaab" would merge to "abab". So the merged string can be of any pattern as long as consecutive characters are different.

Wait, so the merged string is formed by collapsing consecutive duplicates. So, the merged string can have any sequence of 'a's and 'b's, as long as no two consecutive characters are the same. So, the merged string could be "ababab" (alternating), "abba" (but merged as "ab", no), etc. Wait, no. For example, the substring "abba" would be merged as "ab", since the 'b's are consecutive. So merged string is "ab".

So the merged string can have even length. For example, "ab" (length 2), "aba" (length 3), etc. So, when is the merged string a palindrome? Let's see:

- If the merged string has length 1: it's a palindrome.
- If the merged string has length 2: the first and second characters must be the same. But since the merged string can't have consecutive duplicates, the two characters must be different. So, length 2 merged strings can't be palindromes. So the only possibility for even-length merged palindromes is when the length is 0, which isn't possible here. Wait, but the merged string is at least length 1. So for even-length merged strings (like 2,4, etc.), the first and last characters must be the same, but since consecutive characters are different, perhaps even-length merged palindromes can only exist when the entire string is a palindrome of even length. But how?

Wait, let's take a merged string of length 3: "aba". That's a palindrome. If the merged string is of length 4, then for it to be a palindrome, the first character must equal the fourth, and the second equals the third. For example, "abba". But merged as "abba" would have consecutive 'b's, so the original would have to be like 'a' followed by 'b's, then 'b's again. Wait, but that's not possible. Because the merged string can't have consecutive duplicates. So merged string "abba" is not possible. Because after merging, consecutive duplicates are removed. So 'a' followed by 'b's (merged to 'b') followed by 'a's (merged to 'a') becomes 'aba', which is length 3. So merged strings of even length can only exist if the original substring alternates between two different characters. For example, "ababab" would merge to "ababab" (if the original is like a, b, a, b, a, b). So, the merged string length is even (6). For this to be a palindrome, the first character must equal the last (a and b in this case, so no). So, in order for a merged string of even length to be a palindrome, the first and last characters must be the same, but in that case, the merged string must have even length, which requires that the first and last are the same, but in a way that the entire structure mirrors. Wait, but how can that happen?

For example, if the merged string is "abba" (but that's impossible because merged strings can't have consecutive duplicates). So, the merged string must be a sequence of alternating characters. So, the merged string can be of even length only if the first and second characters alternate all the way. For example, "abab" (length 4), which would have characters a, b, a, b. But this is not a palindrome. The first character is a, last is b. So not a palindrome. So any even-length merged string would have first and last characters different, making them not palindromes. Therefore, the only way for a merged string to be a palindrome is if its length is 1 (so all characters in the original substring are the same) or the merged string has an odd length and is a palindrome (like "aba", "ababa", etc.). 

So, the conclusion is that a merged string is a palindrome if and only if:

- It consists of a single character (length 1), OR
- It has an odd length (>=3) and the first and last characters are the same, and the entire string is a palindrome.

Wait, but for example, "ababa" is a palindrome. The merged string is of length 5, which is odd. So that's a palindrome. So, for the merged string to be a palindrome when its length is odd, the first and last characters must be the same. So, for a merged string of length l (odd), the first and last characters must be the same, and the middle character is the same as itself. Then the rest of the characters mirror around the center.

So, the merged string must be of the form c1, c2, ..., c(k), c2, c1, where k is (l-1)/2. And since the merged string has no consecutive duplicates, c1 != c2, c2 != c3, etc. So, the merged string is a palindrome of odd length.

So, putting this together, any substring that when merged becomes a palindrome must satisfy:

Either:

1. The merged string is of length 1 (all characters in the substring are the same), or

2. The merged string has odd length >=3, starts and ends with the same character, and the entire merged string is a palindrome.

So, how do we count all such substrings?

Let's approach this step by step.

First, for all possible substrings, we can group them into two categories: those that when merged have a palindrome of length 1, and those that when merged have a palindrome of odd length >=3.

Let's handle the first case first: merged string length 1. These are all substrings that consist of the same character. For example, "aaa", "b", etc. The number of such substrings is the sum for each run of the same character of (k*(k+1))/2, where k is the length of the run. Because for a run of k same characters, the number of substrings is k*(k+1)/2.

Now, the second case: merged string has odd length >=3 and is a palindrome. For such substrings, the merged string must be a palindrome of odd length. Let's denote the merged string as M. Since M is a palindrome of odd length, the first and last characters of M are the same, and the entire string is symmetric around the center.

Now, the key insight here is that the merged string M must be a palindrome, which for the merged structure (no consecutive duplicates) implies that the positions in M are symmetric. For example, M of length 3 must have first and third characters equal, and the second is any. For length 5, first equals fifth, second equals fourth, third is any.

So, the merged string's structure is determined by the sequence of characters in the original substring. Each time a run of the same character alternates between a and b. For example, the substring could be "aabbaabbaa", which merges to "ababa" (a palindrome of length 5).

So, to count these substrings, we need to find all substrings where:

- The merged string starts and ends with the same character (say 'a' or 'b').

- The merged string is a palindrome.

But how can we model this?

Alternative approach: The merged string is a palindrome of odd length. Let's consider that the merged string has length 2k+1. The middle character is at position k+1, and the rest are symmetric.

But perhaps a better way is to model the runs of the original string. The original string can be divided into runs of consecutive a's and b's. For example, "baab" is split into runs: [b, aa, b]. The merged string is formed by taking the first character of each run, so "b a b".

So, the merged string is the sequence of run characters. For example, the runs of the substring from index i to j in the original string would form a merged string of the run characters. So, if a substring starts in run m and ends in run n, then the merged string is the characters of runs m to n.

Thus, the problem reduces to finding all ranges of runs [m, n] such that the merged string (the sequence of run characters) is a palindrome, and the original substring's length (the sum of the lengths of runs m to n) is considered as a substring. But wait, no. The original substring can be any substring that starts in run m and ends in run n, but not necessarily the entire run. For example, the substring could start in the middle of a run. Wait, no: the merged string is determined by the sequence of runs in the original substring. Wait, if a substring starts in the middle of a run of a's, then that part of the run is considered in the merged string. For example, suppose the original string is "aaabbb". The runs are a:3, b:3. If the substring is "aab" (the first two a's and first b), then the merged string is "ab". But if the substring is the first a and the first two b's, then the merged string is "ab". So, any substring that starts within a run and ends within another run will have a merged string that is the same as the merged string of the entire run (if the runs are the same). Wait, perhaps not. Let's think:

The merged string is formed by merging consecutive equal characters. So, any substring that starts within a run of a's (like in the middle) will have the first part of the run (if any) merged into a single a. So the merged string of the substring is determined by the sequence of runs that are present in the substring. For example, in the original runs [a:3, b:2, a:4], any substring that includes parts of the first a run and the entire b run and part of the a run would have merged string a b a. So, the merged string's structure depends on which runs the substring starts and ends in. Because, even if the substring starts in the middle of a run, the merged string will have a character for that run (as it's part of the same run in the substring). 

Wait, no. For example, take the original string "aaabbbaaa". The runs are a:3, b:3, a:3. If I take a substring that is "aab", which is part of the first run (aa) and the start of the second run (b). Then the merged string is "ab". If I take a substring that is "aaab" (the first a's and first b), merged string is "ab". So, the merged string is determined by the transitions between runs in the substring. So, the merged string is built by the runs in the substring. So, the merged string's characters are exactly the characters of the runs that the substring passes through. 

Wait, let's take another example. Original runs: [a:3, b:2, a:4]. A substring that starts in the first a run and ends in the second a run (but includes the entire b run and some a's from the third run) will have runs a (the part of the first a run that's included), followed by the entire b run, followed by the part of the third a run included. But since these are consecutive runs of a, b, a, the merged string is "aba". So the merged string is determined by the runs that the substring spans. 

Therefore, the merged string of a substring is determined by the sequence of runs in the original string that the substring starts and ends in. Specifically, the merged string is the sequence of characters of those runs. For example, if a substring starts in run m and ends in run n, then the merged string is the characters of run m, m+1, ..., n. But this is only true if the substring starts at the beginning of run m and ends at the end of run n. Otherwise, the substring may start in the middle of a run and end in the middle of another run, but the merged string will still be the sequence of run characters for the runs that are fully covered in the substring. Wait, no. If the substring starts in the middle of a run, the merged string's first character is the same as that run's character. Because the entire substring's first part is part of that run. For example, if a run is a:5, and the substring starts at position 3, then in the substring, the first part is a's (since the entire run is a's). So the merged string's first character is a. So, regardless of where the substring starts within a run, as long as the entire run is part of the substring, the merged string includes that run's character. Wait, no. Let me think again.

Suppose the original string is "aabbaa". The runs are a:2, b:2, a:2. Any substring that starts in the middle of the first a run (say, the second a) and ends in the middle of the third a run (say, the fifth character) would consist of parts of the first a run, the entire b run, and part of the third a run. The merged string would be "aba". Because the first part (a) is merged into a single a (since it's a continuous part of the a run), then the b's are merged into a single b, then the a's into a single a. So the merged string is aba.

But the runs in the original string are a:2, b:2, a:2. The substring spans parts of the first and third runs, but includes the entire second run. The merged string is formed by the characters of the runs that the substring passes through. So the merged string is a, b, a.

So, the merged string of a substring is determined by the runs that are present in the substring, in the order they appear. Each time the substring transitions from one run to another in the original string, that contributes a new character to the merged string.

Therefore, the merged string is the sequence of the original runs' characters, but only for the runs that are intersected by the substring. However, this is only true if the substring starts at a run boundary. Wait, no. For example, a substring that starts in the middle of a run and ends in the middle of another run will have a merged string that starts with the character of that run, then the next run, etc. So, the merged string is the sequence of the original runs' characters for the runs that the substring spans. 

Wait, perhaps the key is to model the original string as a list of runs. For example, the original string is represented as a list of pairs (char, count). Then, any substring will correspond to a sequence of runs in this list. The merged string is the sequence of characters of these runs, regardless of how much of each run is included in the substring (as long as at least part of the run is included). Because even if the substring starts in the middle of a run, that part is considered part of the run, so the merged string's character is the same as the run's character. So, the merged string's characters are exactly the characters of the runs that the substring spans. 

So, the merged string of a substring is the sequence of characters of the runs that the substring starts and ends in, regardless of where in the runs the substring starts or ends. For example, a substring that starts in run i and ends in run j will have a merged string consisting of the characters of runs i, i+1, ..., j. 

Therefore, the problem reduces to finding all intervals [i, j] of runs such that the sequence of characters of runs i to j is a palindrome. For each such interval [i, j], the number of possible substrings that correspond to this interval is (number of possible starting positions in run i) * (number of possible ending positions in run j). Because the substring can start anywhere in run i and end anywhere in run j. 

Wait, let's clarify. For the interval of runs [i, j], the merged string is the characters of runs i to j. So, any substring that starts in run i (any position within run i) and ends in run j (any position within run j) will have a merged string that includes the characters of runs i to j. Therefore, the number of such substrings is the product of the lengths of run i and run j. Because:

- The start can be any of the run i's length positions (even if the substring starts in the middle of the run, the merged string's first character is run i's character).

Wait, no. For example, run i has length 5. If the substring starts at position 3 of this run, the merged string's first character is the same as the run's character. So, for the merged string to be the sequence of runs i to j, the substring must start in run i and end in run j. But the start can be anywhere in run i (even the first character), and the end can be anywhere in run j (even the last character). So, the number of substrings that correspond to the interval [i,j] is (length of run i) * (length of run j). Because for run i, there are 'len_i' possible starting points (since each position in run i can be the start of the substring, but as long as the substring extends into run j, the merged string will include all the runs from i to j). Wait, but this is only true if j >= i. So, if the interval is [i, j], then the merged string has j - i + 1 runs. But the substring must start in run i and end in run j, but include all the runs in between. Wait, no. If the substring starts in run i and ends in run j, but skips some runs in between, then the merged string would consist of run i, followed by the runs between i and j that are included in the substring. But that's impossible because the substring is a continuous part of the original string. So, the runs between i and j must all be included. So, the interval [i,j] must be a consecutive sequence of runs in the original string. 

Therefore, the merged string's sequence of characters is runs i, i+1, ..., j. So, for each such consecutive interval of runs, the merged string is the sequence of their characters. Therefore, the problem reduces to:

For each consecutive interval of runs [i, j], determine if the merged string (the sequence of characters of runs i to j) is a palindrome. If so, then the number of substrings corresponding to this interval is (run_i's length) * (run_j's length). Then, sum all such products over all valid intervals [i,j].

But wait, this is only when j > i. When j == i (i.e., the interval is a single run), then the merged string is a single character (the run's character). The number of substrings in this case is (run_i's length * (run_i's length + 1)) / 2, which is the count for all possible substrings of that run.

So, the approach can be divided into two parts:

1. Count all single-run intervals (which contribute to merged strings of length 1), and calculate their counts (even and odd lengths).

2. Count all intervals of multiple runs (i to j, j >= i+1) where the merged string is a palindrome. For each such interval, the number of substrings contributing is run_i's length multiplied by run_j's length, and each such substring's length can be even or odd.

Wait, but the merged string's length being a palindrome is determined by the interval of runs. However, the actual length of the substring (which determines even or odd) is the sum of the lengths of the runs i to j. Wait, no. The substring can start anywhere in run i and end anywhere in run j. So, the actual length of the substring is (position in run j - position in run i + 1). So, for example, run i has length 3, run j has length 4. The substring can start at the second character of run i (length 3) and end at the third character of run j (length 4). The actual substring's length is (3 - 2 + 1) + (sum of the lengths of runs i+1 to j-1) + (3 - 1 + 1) = but this is getting complicated. Wait, no. The actual substring's length is (end_pos - start_pos + 1). So, for a substring that starts at position s in run i and ends at position e in run j, the length is (e - s + 1). But the start can be any position in run i, and end can be any position in run j. So, the possible lengths are all possible (e - s + 1) where s is between 1 and len_i, and e is between 1 and len_j. But this depends on the actual positions of the runs in the original string.

But this approach would be computationally expensive for large runs. So, perhaps we can find a way to model the even and odd counts based on the product of the lengths of run i and run j, and their parity.

Wait, the length of the substring can be even or odd. For each such substring in the interval [i,j], the length is (run_i_part) + ... + (run_j_part). However, since the runs are consecutive, the actual length is (sum of lengths of runs i to j) minus (the part of run i not included) minus (the part of run j not included). Wait, perhaps not. For example, run i has len_i=5 (positions 1-5), run j has len_j=3 (positions 6-8). A substring starting at position 3 of run i (length 3) and ending at position 2 of run j (position 7) would have length 7-3+1=5. So, the length is (7-3+1)=5. But the sum of the run lengths between i and j is 5 (run i) + ... + (run j's len). Wait, maybe not. The sum of the run lengths is the total length of the runs from i to j. For example, runs i to j may consist of run i (len 5), run i+1 (len 3), run j (len 4). So sum is 5+3+4=12. But the substring can start anywhere in run i and end anywhere in run j, so the actual length can vary between 1 (if starts and ends at the same position in run i and j) up to the sum of all run lengths from i to j.

But this approach seems complicated. However, perhaps we can model the number of even and odd length substrings in the interval [i,j] as follows:

Each substring in [i,j] corresponds to a start in run i and end in run j. The length of the substring is (sum of all runs from i to j) - (the number of characters skipped in run i) - (the number of characters skipped in run j). But this is complicated. 

Alternatively, the length of the substring is (pos_end - pos_start + 1), where pos_start is in run i and pos_end is in run j. 

But to compute the number of even and odd length substrings in the interval [i,j], we can model it based on the parity of (pos_end - pos_start +1).

Let’s denote:

s can be any start position in run i (from 1 to len_i), and e can be any end position in run j (from 1 to len_j). The actual positions in the original string are offset by the cumulative sum of previous runs, but perhaps it's easier to model the length as (sum_run_i_to_j) - (s_start -1) - (len_j - e_end), where s_start is the start within run i (1-based), e_end is the end within run j (1-based). Then, the length is:

sum_run = sum of len_i, len_{i+1}, ..., len_j

length = sum_run - (s_start -1) - (len_j - e_end) 

= sum_run - s_start +1 - len_j + e_end 

= (sum_run - len_j + 1) + (e_end - s_start)

But sum_run - len_j + 1 is the sum of the lengths of runs i to j-1 plus 1. Not sure if this helps.

Alternatively, the length is (e_end_pos - s_start_pos + 1), where s_start_pos is the global start position in the original string (e.g., if run i starts at position x, then s_start can be x + s-1, where s is 1..len_i). Similarly for e_end_pos. But this seems complicated.

Alternatively, notice that for a given interval [i,j], the sum of the runs from i to j is S. Then, the possible lengths of substrings in this interval range from (1) to S. However, the actual possible lengths for the interval's substrings can be determined by the way start and end are chosen. But this is not straightforward.

Wait, but in the case where the interval [i,j] consists of multiple runs, the merged string's structure is the same for all substrings in this interval (as the merged string is determined by the runs). However, the actual length of the substring can vary. For example, in runs [a:3, b:2], the merged string is "ab". Substrings can be "ab" (length 2), "aab" (length 3), "abb" (length 3), "aabb" (length 4), etc. The merged string is always "ab", which is not a palindrome, so those substrings are not counted. But in the case where the merged string is a palindrome (like "aba"), then each possible start and end in runs i and j will contribute a substring with varying lengths (even or odd).

But our problem requires counting the number of good substrings of even and odd lengths. For each interval [i,j], if the merged string is a palindrome (either length 1 or odd >=3), then we need to count how many substrings in this interval have even length and how many have odd length.

So, for each interval [i,j], the merged string is a palindrome. Let's handle the two cases:

Case 1: merged string is length 1 (i == j). The substrings are all the substrings of this single run. For a run of length L, the number of substrings is L*(L+1)/2. For each substring, its length is from 1 to L. So, the number of even-length substrings is sum_{k=1 to L} (if k is even, then (L -k +1) else 0). Similarly for odd. For example, L=3: substrings of length 1 (3), 2 (2), 3 (1). Even count is 2 (k=2: 2 substrings). Odd count is 3 + 1 =4? Wait, no. For L=3, possible substrings are:

Length 1: 3 (all odd).

Length 2: 2 (positions 1-2, 2-3) → even.

Length 3: 1 (positions 1-3) → odd.

So even count is 2, odd count is 3+1=4.

But how to compute this for any L?

The number of even-length substrings in a run of length L is floor(L/2) * (ceil(L/2)). For example, L=3: floor(3/2)=1, ceil(3/2)=2 → 1*2=2. Which matches. L=4: floor(4/2)=2, ceil(4/2)=2 → 4 even-length substrings. Let's see:

Substrings of length 1 (4), 2 (3), 3 (2), 4 (1). Even lengths are 2 and 4. Count for 2:3, for 4:1 → total 4. Which matches 2*2=4. So the formula seems to hold.

Similarly, the number of odd-length substrings is ceil(L/2) * ceil(L/2). Wait, for L=3: ceil(3/2)=2 → 2*2=4. Which matches. For L=4: ceil(4/2)=2 → 2*2=4. But the odd-length substrings are 1 and 3. For L=4, 1:4 substrings (length 1), 3: 2 substrings (length 3) → total 6. Wait, this contradicts the formula.

Hmm, maybe I need a different approach. Let's find a general formula for the number of even and odd-length substrings in a run of length L.

For a run of length L:

The number of substrings of length k is (L - k + 1).

So, for even k: sum_{k even} (L -k +1) for k from 1 to L.

Similarly for odd k.

Let's compute this.

Let’s separate even and odd:

For even lengths:

sum_{m=1 to M} (L - 2m +1), where 2m ranges up to L.

Wait, perhaps it's easier to compute:

The even-length substrings are those where the length is even. So, for each possible even length e (2,4,... up to L if even), the count is L -e +1.

The total even substrings is sum_{e=2,4,...} (L -e +1).

Similarly for odd.

This can be expressed as:

For even:

If L >=2: sum_{e=2 to min(L, even)} (L -e +1).

Similarly for odd.

Alternatively, using mathematical formulas.

The sum of even lengths:

The sum is sum_{e=2,4,..., E} (L -e +1), where E is L if even, or L-1 if L is odd.

Similarly for odd.

Let's calculate this sum.

Let’s denote for even:

The sum is sum_{k=1}^{m} (L - 2k + 1), where m is floor((L-1)/2). Wait, perhaps not. Let's think for even L and odd L.

Let me think of L as even. Let L=2n.

Even lengths are 2,4,..., 2n.

Sum for even lengths:

sum_{k=1 to n} (2n -2k +1) = sum_{k=1 to n} (2n +1 -2k) 

= sum_{k=1 to n} (2(n -k) +1) 

= sum_{i=0 to n-1} (2i +1) 

= sum of first n odd numbers.

Sum of first m odd numbers is m². So here, sum is n².

But 2n is L, so n = L/2.

So sum for even L: (L/2)².

For odd L: L=2n+1.

Even lengths are 2,4,..., 2n.

Sum for even lengths:

sum_{k=1 to n} (2n+1 -2k +1) = sum_{k=1 to n} (2n+2 -2k) 

= sum_{k=1 to n} 2(n +1 -k) 

= 2 * sum_{k=1 to n} (n +1 -k)

= 2 * sum_{i=1 to n} i 

= 2 * (n(n+1)/2) ) 

= n(n+1).

But L=2n+1 → n = (L-1)/2.

So sum becomes ( (L-1)/2 ) * ( (L-1)/2 +1 ) = ( (L-1)/2 ) * ( (L+1)/2 ) ) = (L² -1)/4.

Wait, but when L is even, sum is (L/2)^2. When L is odd, sum is ((L-1)(L+1))/4 = (L²-1)/4.

Wait, let's test with L=3 (odd). 

Even-length sum: 2 (only k=2). (3-2 +1) = 2. So sum is 2. 

(L²-1)/4 = (9-1)/4= 8/4=2. Correct.

For L=4 (even):

Even sum is (4/2)^2= 2^2=4. Which matches sum for 2 and 4: (4-2+1) + (4-4+1) → 3 +1=4.

So even sum is:

if L is even: (L/2)^2

if L is odd: (L^2 -1)/4

Similarly, for odd-length substrings:

sum for odd k: sum_{k=1,3,...} (L -k +1).

For even L:

L=2n. odd k: 1,3,5,...,2n-1.

sum_{m=0}^{n-1} (2n - (2m+1) +1) = sum_{m=0}^{n-1} (2n - 2m) 

= sum_{m=0}^{n-1} 2(n -m) 

= 2 * sum_{m=1 to n} m 

= 2*(n(n+1)/2) 

= n(n+1)

Which for L=4 (n=2) gives 2*3=6. Which is correct: the odd-length substrings are 1,3 → sum (4-1+1) =4 (for k=1) and (4-3+1)=2 (k=3) → total 6.

For odd L=2n+1:

sum of odd k: sum_{m=0 to n} (2n+1 - (2m+1) +1) = sum_{m=0 to n} (2n+1 -2m -1 +1) = sum_{m=0 to n} (2n+1 -2m) 

= sum_{m=0}^n (2(n -m) +1)

= sum_{i=0}^n (2i +1) → sum of first n+1 odd numbers, which is (n+1)^2.

For L=3 (n=1): sum is (1+1)^2=4. Which matches the sum (3-1+1=3 for k=1, 3-3+1=1 for k=3 → total 4).

So, the odd sum is:

if L even: (L/2) * (L/2 +1)

if L odd: ((L+1)/2)^2

But wait, for even L:

The formula is n(n+1), where n = L/2. So (L/2) * (L/2 +1) = (L² +2L)/4.

For odd L:

((L+1)/2)^2 → ((2n+2)/2)^2 = (n+1)^2.

So, putting this together:

For a single run of length L, the number of even-length substrings is:

even_count = (L is even) ? (L/2)^2 : (L^2 - 1) /4

The number of odd-length substrings is:

odd_count = (L is even) ? (L/2) * (L/2 +1) : ((L+1)/2)^2 

This is important for calculating the first case (merged string of length 1).

Now, for the second case: merged string is a palindrome of odd length >=3.

In this case, the merged string is formed by multiple runs (i to j where j >=i+1), and the sequence of their characters forms a palindrome of odd length.

So, the merged string must start and end with the same character (since it's a palindrome), and the entire sequence of runs' characters must be symmetric. 

For example, if the merged string is "aba", then the sequence of runs is a, b, a. The characters must form a palindrome.

To find all such intervals [i,j], we can model this as follows:

For each interval [i,j], check if the sequence of characters from run i to run j is a palindrome. 

But for large n (up to 1e5), we need an efficient way to do this. 

The standard approach for checking palindromic substrings is to use a Manacher's algorithm or expand around centers. However, the merged string is a sequence of characters from the runs. So, the merged string is a string where each character is the character of a run. Let's call this the run string. 

For example, if the runs are [a, b, a, a, b], then the run string is "abab". So, the run string is a string where each character is the character of the corresponding run.

The problem now reduces to finding all palindromic substrings of the run string. But not exactly, because the run string can be up to 1e5 in length (since the original string can have up to 1e5 runs in the worst case, like a and b alternating). However, the original string can have up to 1e5 characters, so the number of runs can be up to 1e5 (if the input is alternating a and b). So, the run string can be up to 1e5 in length. 

But we need to process all palindromic substrings of the run string, and for each such substring, compute the number of even and odd-length substrings in the original string that correspond to it. 

But how to map the palindromic substrings in the run string to the actual substrings in the original string?

Each palindromic substring in the run string corresponds to a consecutive sequence of runs. For example, the run string is "ababa", and a palindromic substring is "ababa" (the entire string), which corresponds to runs 1 to 5. 

For each such palindromic substring [i,j] in the run string (i.e., the sequence of runs from i to j forms a palindrome), the number of original substrings that correspond to this is the product of the lengths of run i and run j. Because the start can be any position in run i, and the end can be any position in run j. 

But this is only true if the merged string of the original substring is exactly the sequence of runs i to j, which requires that the substring starts in run i and ends in run j, and includes all runs in between. 

So, for each palindromic substring [i,j] in the run string, the number of original substrings that contribute to the good substrings is len_i * len_j. 

But wait, this is only true when i < j. When i =j, the merged string is a single character, which we already handled in the first case.

So, for the second case (merged string is a palindrome of odd length >=3), we need to consider all palindromic substrings [i,j] of the run string where j >i and the length of the run string substring is odd (since the merged string's length is odd). 

But the run string is formed by the runs, so each character in the run string corresponds to a run in the original string. So, for the run string, each character is either 'a' or 'b', and consecutive characters are different. So, the run string has no consecutive duplicates. 

Therefore, the run string is a string where no two adjacent characters are the same. 

This is important because when we look for palindromic substrings in the run string, we know that their lengths can be either odd or even. However, for the merged string to be a palindrome of odd length, the run string's substring must be a palindrome of odd length. Because the merged string's length is the same as the run string's substring length. So, if the run string's substring is a palindrome of odd length, then the merged string is a palindrome of that odd length. 

So, our goal is to find all palindromic substrings of the run string that have odd lengths. For each such substring [i,j], where j -i +1 is odd, the number of original substrings is len_i * len_j. 

But how do we efficiently find all such palindromic substrings and compute their contributions to the even and odd counts?

To solve this, we can use Manacher's algorithm, which finds all palindromic substrings of a string in O(n) time. However, since the run string can be up to 1e5 in length, and Manacher's algorithm is O(n), this is feasible.

Once we have all palindromic substrings of the run string with odd lengths, we can iterate through each such substring's start and end indices (i and j in the run string) and accumulate the product len_i * len_j, considering whether the original substrings' lengths (which vary based on where the start and end are in the runs) contribute to even or odd counts.

But here's the problem: the merged string's length is the same as the run string's substring length. For example, a run string's substring of length 3 corresponds to a merged string of length 3. But the original substring's length can vary. For example, runs i, i+1, j (3 runs) have lengths 2, 3, 4. The original substring can start anywhere in run i and end anywhere in run j. The merged string's length is 3 (which is the length of the run string's substring), but the original substring's length can be even or odd. 

Wait, no. The merged string's length is the same as the run string's substring length. But the original substring's length is the sum of the lengths of the runs i to j minus the parts not included. 

But the original substring's length can vary between (run_i_len + run_j_len) (if the start is at the beginning of i and end at the end of j, and there are no other runs) and (1 + 1) (if the start is at the end of i and end at the beginning of j, but that's not possible if there are runs in between). 

Wait, the merged string's length is j - i + 1 (the number of runs in the interval [i,j]). The original substring's length is the sum of the lengths of the runs in [i,j] minus the left part of run i (before the start) minus the right part of run j (after the end). But for each possible start and end in runs i and j, the original substring's length is (run_i_len - start_pos +1) + sum_{k=i+1 to j-1} run_k_len + (end_pos). 

But this depends on the start and end positions in runs i and j. 

Alternatively, the original substring's length is (start in run i's position) to (end in run j's position) in the original string. Let's say the original string has runs stored as a list, each with their starting and ending positions. For example, run i starts at position s_i and ends at position e_i. 

If a substring starts at position x in run i (s_i ≤ x ≤ e_i) and ends at position y in run j (s_j ≤ y ≤ e_j), then the length is y -x + 1. 

But x can be any position in run i, and y can be any position in run j. 

So, for the interval [i,j], the possible lengths are all possible (y -x +1) where x ∈ run i, y ∈ run j. 

We need to calculate the number of pairs (x, y) such that (y -x +1) is even or odd. 

But how? 

Note that y -x +1 is even if and only if (y -x) is odd. Which is equivalent to (x + y) is odd. 

So, the parity of the length depends on the parity of (x + y). 

So, the number of even-length substrings is the number of pairs (x, y) where x is in run i, y is in run j, and x + y is odd. 

Similarly, the number of odd-length substrings is the number of pairs where x + y is even. 

So, for each interval [i,j], which is a palindromic substring of the run string of odd length, the contribution to the even and odd counts is:

even_contribution = number of pairs (x,y) where x + y is odd.

odd_contribution = number of pairs (x,y) where x + y is even.

But how to compute this? 

Let's denote:

run_i_len = len_i

run_j_len = len_j

In run i, the positions are from a to b (inclusive). For example, if run i starts at position s_i and has length len_i, the positions are s_i, s_i+1, ..., s_i + len_i -1. 

Similarly for run j.

But the actual positions are not needed. What's important is the parity of x and y. 

For any x in run i, the parity of x can be even or odd. Similarly for y in run j. 

The sum x + y is even if x and y have the same parity. It's odd if x and y have different parities. 

But run i's positions are consecutive. Let's assume that the run i's first position is even or odd. 

For example, suppose run i starts at position start_i. Then, the parity of the first position is start_i % 2. 

The positions in run i are start_i, start_i+1, ..., start_i + len_i -1.

So, the parity of the first position is start_i % 2.

The run i contains len_i consecutive positions, so the parities alternate. 

The number of even positions in run i is:

if start_i is even:

number_evens = (len_i +1) // 2

number_odds = len_i // 2

else:

number_evens = len_i // 2

number_odds = (len_i +1) // 2

Similarly for run j.

But this requires knowing the parity of the first position of each run. 

But this could be computationally expensive to calculate for each run. 

Alternatively, the parity of the first position of run i can be computed based on the cumulative sum of previous run lengths. 

Let’s precompute the cumulative sum of run lengths. For example, the first run starts at position 1. The second run starts at position 1 + len_1. The third run starts at position 1 + len_1 + len_2, and so on. 

So, the starting position of run k is sum_{m=1 to k-1} len_m + 1. 

Thus, the parity of the first position of run i is (sum_{m=1 to i-1} len_m + 1) % 2. 

But summing len_m up to i-1 could take O(n) time per run, which is O(n^2) time. However, if we precompute a prefix sum array, we can compute the starting position of each run in O(1) time. 

So, let's precompute a prefix array, where prefix[i] is the sum of the lengths of the first i runs. Then, the starting position of run i is prefix[i-1] + 1. 

Assuming that the runs are numbered from 1 to m, where m is the number of runs, and prefix[0] = 0. 

So, for run i, start_i = prefix[i-1] + 1. 

Thus, the parity of start_i is (prefix[i-1] + 1) % 2. 

Once we have the parity of the starting position of run i and run j, and their lengths, we can compute the number of even and odd positions in each run. 

Let's denote for run i:

start_parity_i = (prefix[i-1] + 1) % 2

Then, the number of even positions in run i is:

if start_parity_i is even (0):

even_count_i = (len_i +1) // 2

odd_count_i = len_i // 2

else:

even_count_i = len_i // 2

odd_count_i = (len_i +1) // 2

Similarly for run j.

Then, the number of pairs (x,y) where x is in run i, y is in run j, and x + y is even is:

even_pairs = (even_count_i * even_count_j) + (odd_count_i * odd_count_j)

Similarly, the number of pairs where x + y is odd is:

odd_pairs = (even_count_i * odd_count_j) + (odd_count_i * even_count_j)

Thus, for each palindromic substring [i,j] in the run string of odd length, the contribution to the even and odd counts is:

even_total += odd_pairs (because the merged string is a palindrome of odd length, and the original substring's length is even if x + y is odd)

Wait, wait. The merged string is a palindrome of odd length. But the original substring's length can be even or odd. So, for each such palindromic substring [i,j], we need to add the number of original substrings with even length (odd_pairs) to the even count, and the number of original substrings with odd length (even_pairs) to the odd count. 

Because the original substring's length is even if (y -x +1) is even, which happens when x + y is odd. 

So, the even_pairs (x and y have same parity) contribute to odd lengths, and odd_pairs contribute to even lengths. 

Thus, for each interval [i,j], the contribution is:

even_contribution = odd_pairs

odd_contribution = even_pairs

So, the steps are:

1. Preprocess the input string into runs, storing their lengths and characters.

2. Precompute the prefix sum array for the runs to compute the starting positions.

3. Precompute for each run i the number of even and odd positions (even_count_i, odd_count_i).

4. Generate the run string (each run's character).

5. Find all palindromic substrings in the run string with odd lengths.

6. For each such palindromic substring [i,j] (i < j), compute the number of even and odd contributions as (odd_pairs, even_pairs) and add them to the respective totals.

7. Additionally, handle the single-run substrings (i=j), which contribute to the first case.

Putting it all together:

First, process the input into runs.

For example, "baab" becomes runs of 'b' (length 1), 'a' (2), 'b' (1). The run string is "bab".

Then, the single-run substrings are:

- run 1 (length 1): contributes 0 even, 1 odd.

- run 2 (length 2): contributes 1 even, 2 odd.

- run 3 (length 1): contributes 0 even, 1 odd.

So, single-run contribution is even_total_single = 1, odd_total_single = 4.

For the multi-run palindromic substrings:

The run string is "bab". The palindromic substrings of odd length are:

- "b" (run 1 → handled in single-run).

- "a" (run 2 → handled in single-run).

- "b" (run 3 → handled in single-run).

- "bab" (runs 1-3). The run string's substring is "bab", which is a palindrome of length 3 (odd). So, i=1, j=3.

Compute even and odd pairs:

For run i=1 (len 1, start_parity is 1 (starts at position 1)).

even_count_i = 0 (since start_parity is odd (1) and len=1 → len//2=0). odd_count_i = 1.

For run j=3 (len 1, start_parity is (prefix[2] +1) → prefix[2] is 1+2=3. start_parity is 4%2=0. len=1 → start_parity even: (1+1)/2=1 even_count_j is 0, since start_parity is even and len 1: (1+1)//2=1 even count is 1 if start_parity is even and len is 1? Wait, let me re-calculate.

Wait, for run j=3:

start_parity is (prefix[2] +1) mod 2. prefix[2] is sum of first 2 runs:1+2=3. +1=4 → mod 2 is 0. So start_parity is even. len_j is 1.

So:

start_parity even. len_j=1.

even_count_j = (1 +1)//2 = 1. Because start_parity even, the first position is even, so positions are even (start even, len 1 → 1 even position.

odd_count_j = 0.

So, even_count_i=0, odd_count_i=1.

even_count_j=1, odd_count_j=0.

even_pairs = (0 *1) + (1 *0) = 0.

odd_pairs = (0 *0) + (1 *1) = 1.

So, contribution is even_contribution=1, odd_contribution=0.

But wait, the merged string "bab" is a palindrome of length 3. The original substrings are those that start in run 1 and end in run 3. Each such substring's length can be even or odd.

In this case, run 1 has length 1, run 3 has length 1. So the possible original substrings are those that start at position 1 of run 1 and end at position 1 of run 3. The length is 3 (1-1+1=3, but the actual length is (run 1's len + run 2's len + run 3's len) - (start_pos-1) - (run3's len - end_pos). 

Wait, the original substring starts in run 1 (position 1) and ends in run 3 (position 1 of run 3). The runs between are runs 2 (len 2). So the length is 1 (run1) + 2 (run2) + 1 (run3) =4. But the start is at run1's position 1 and end at run3's position 1. The actual length is (1+2+1) - (start_pos-1) - (run3's len - end_pos) → (4) - 0 - (1-1) →4. So the length is 4, which is even. So this particular substring contributes to even_contribution. 

But according to the calculation above, for interval [1,3], the contribution is even_contribution=1 (odd_pairs=1). So yes, this is correct.

So, the even_total_multi increases by 1, and the odd_total_multi increases by 0.

Thus, the total even count is 1 (single) +1 (multi) =2. The odd count is 4 (single) +0 (multi) =4. Which matches the second sample input.

So, this approach seems correct.

The steps are now:

1. Process the input into runs.

   For example, for input 'baab', the runs are:

   [('b',1), ('a',2), ('b',1)].

2. Compute the prefix sums of the run lengths. For the above example, prefix is [0,1,3,4].

3. For each run, compute start_parity (start_i mod 2), then compute even_count and odd_count for the run.

4. Generate the run string: 'bab'.

5. Find all palindromic substrings of the run string with odd lengths, and for each such substring [i,j] (i < j), compute the contribution based on the even and odd pairs.

To find all palindromic substrings of the run string with odd lengths, we can use Manacher's algorithm. But implementing Manacher's algorithm can be a bit involved. Alternatively, we can use the expand around center approach. For each center (each character and each gap between characters), expand as long as the substring is a palindrome. Since the run string is up to 1e5 characters, and the expand around center approach is O(n^2), this would be too slow for n=1e5. So, Manacher's algorithm is needed.

But wait, the run string can have up to 1e5 characters. Manacher's algorithm is O(n), which is acceptable.

So, the plan is:

- Use Manacher's algorithm to find all palindromic substrings of the run string with odd lengths.

Wait, no. Manacher's algorithm is designed to find all palindromic substrings, but for each center, it finds the longest palindrome centered there. However, we can use the radius information to find all palindromes. 

Alternatively, for each possible center, find all possible odd-length palindromes.

But in the run string, since consecutive characters are different (no two consecutive runs are the same), the palindromic substrings of even length are impossible. Because, for a substring of even length to be a palindrome, the first and second halves must be mirrors, but since the run string has no consecutive duplicates, even-length palindromes must have even length and the first character equals the second, which is impossible. So, the only possible palindromic substrings of the run string are those with odd length. 

Because in the run string, characters alternate between a and b. Wait, no. The run string can have runs of any length (but the characters alternate). For example, the run string can be "ababab...", with each run being a single character, so the run string has alternating characters. 

In such a case, the run string has no two consecutive characters the same. So, any even-length substring would have characters alternating, but the first and last characters would be different, so it can't be a palindrome. For example, a run string substring "ab" (length 2) would have first 'a' and last 'b', not a palindrome. 

Thus, all palindromic substrings in the run string must have odd lengths. Because, for even lengths, the first and last characters are different. 

This is a crucial insight. 

Therefore, when checking palindromic substrings in the run string, we only need to consider odd lengths, and each such palindrome must have the same first and last character. 

So, the run string's palindromic substrings are exactly those with odd lengths and centered around a certain position, expanding symmetrically. 

Thus, the number of palindromic substrings in the run string can be computed using Manacher's algorithm, and each such substring is of odd length. 

Therefore, the steps are:

- For the run string, generate all palindromic substrings. Each of these has odd length. 

For each such palindromic substring [i,j], where i and j are indices in the run string (1-based?), compute the contribution as:

even_contribution = odd_pairs (number of pairs (x,y) with x in run i and y in run j and x + y is odd)

odd_contribution = even_pairs (number of pairs (x,y) with x and y have the same parity)

Thus, the total even and odd counts are:

even_total = sum of even_contribution for all multi-run intervals plus sum of even counts from single-run intervals.

odd_total = sum of odd_contribution for all multi-run intervals plus sum of odd counts from single-run intervals.

Now, the code steps:

First, process the input into runs.

For example:

s = input().strip()

runs = []
if not s:
   ... handle empty, but the input has n >=1.

prev = s[0]
count =1
for c in s[1:]:
   if c == prev:
      count +=1
   else:
      runs.append( (prev, count) )
      prev = c
      count =1
runs.append( (prev, count) )

Then, compute the prefix sums for the runs.

m = len(runs)
prefix = [0]*(m+1)
for i in range(1, m+1):
   prefix[i] = prefix[i-1] + runs[i-1][1]

Then, precompute for each run i (1-based?), the start_parity, even_count, odd_count.

But in code, runs are 0-based in the list. Let's say runs are 0-based. So, for run in runs:

for i in range(m):
   start_i = prefix[i] +1
   start_parity = start_i %2
   len_i = runs[i][1]
   if start_parity ==0:
      even_count = (len_i +1)//2
      odd_count = len_i //2
   else:
      even_count = len_i //2
      odd_count = (len_i +1)//2
   # store even_count, odd_count for run i

So, create two arrays even_counts and odd_counts for each run.

Then, generate the run string: run_chars = [r[0] for r in runs]

Now, find all palindromic substrings in run_chars. Since all palindromic substrings have odd lengths, we can use Manacher's algorithm to find all possible palindromic substrings.

Once we have all palindromic substrings (i, j) (0-based indices), then for each such substring where j >i (i.e., length >=3), compute the contribution.

Wait, no. The length of the substring is j -i +1. For a palindrome of length >=3, the start and end must be the same. So, for each palindromic substring [i,j], the start and end characters are the same, and the substring is a palindrome.

So, using Manacher's algorithm, for each possible center, we can get the maximum radius and then iterate over all possible palindromes.

But the code for Manacher's algorithm can be adapted.

But since all palindromic substrings are of odd length, the Manacher's algorithm can be simplified. 

Manacher's algorithm for odd-length palindromes:

The algorithm computes for each position i the maximum radius d such that the substring centered at i with radius d is a palindrome. The total length of the palindrome is 2d +1.

So, for each i in 0 to n-1, the maximum radius is d_i. Then, the number of palindromic substrings centered at i is d_i +1 (since radius can be 0, 1, ..., d_i). 

But we need to find all possible palindromic substrings and their start and end indices.

For each palindrome centered at i with radius r (0 <= r <=d_i), the start and end indices are i -r and i +r.

So, for each i and r, the substring is s[i-r ... i +r], which has length 2r+1.

So, for the run_chars string, we can compute the maximum radius for each center using Manacher's algorithm, then for each possible palindrome, record the start and end indices (i-r, i+r), and then process each such interval.

But since we need all palindromic substrings, even those with radius 0 (single character), but in the multi-run case, we need to process only those intervals where j >i (i.e., the start and end are different runs). So, for single-character palindromes (i==j), those are handled in the single-run case.

Thus, when processing the palindromic substrings from Manacher's algorithm, we need to iterate for each possible palindrome, and for those where the length is >=3 (radius >=1), compute the contribution.

Alternatively, for each palindrome of length >=3 (radius >=1), compute the contribution.

But in code, how to avoid processing the single-character palindromes again?

The answer is: in the multi-run processing, we only consider palindromic substrings where j >i (i.e., the start and end are different runs). So, for the Manacher's algorithm, after generating all palindromic substrings, we filter those where the start and end are different runs (i < j).

But in the case of a palindrome with radius >=1, the start and end indices are i-r and i+r. Since the run string has length m, the start and end can be any, but we need to ensure that start <= end and start <= end, and that start < end (since j must be >i).

Wait, no. For a palindrome centered at i with radius r, the start is i -r and end is i +r. The length is 2r+1. So, for r=0, the length is 1 (start = end =i). For r=1, length is 3, start =i-1, end =i+1. 

Thus, for palindromes with length >=3 (r >=1), the start and end are different. 

But in code, for each possible palindrome, we need to check if start < end (i.e., the palindrome spans multiple runs). 

But in the run string, the palindrome's start and end indices are in the run string. So, for example, if the run string is "bab", then a palindrome centered at index 1 (0-based) with radius 1 would have start=0, end=2. Thus, i=0 and j=2, which are different runs. 

Thus, for each palindrome with radius r >=1, we can get the start and end indices and compute their contribution.

Thus, the code steps are:

- For the run string S, compute the Manacher's array for odd lengths.

- For each center i (0 <=i < m), get the maximum radius d_i.

- For each possible radius r from 0 to d_i:

   - if r >=1:

      - compute start = i -r

      - end = i +r

      - check if start >=0 and end <m.

      - the substring is S[start..end], which is a palindrome of length 2r+1.

      - compute the contribution for this interval [start, end] in the run string.

Thus, the code will iterate through all possible palindromic substrings of the run string with length >=3 (r >=1), and for each, compute the even_contribution and odd_contribution.

But this can be time-consuming. However, since the run string can have up to 1e5 characters, and for each center i, the maximum radius d_i can be up to m, this would be O(n^2), which is not feasible.

Ah, here's the problem. Manacher's algorithm is O(n), but enumerating all possible palindromes would be O(n^2) in the worst case (like when the run string is all 'a's, but no, since run string cannot have consecutive duplicates. So, the run string can't have two same consecutive characters, so the maximum possible radius for a palindrome is 0. So, all palindromes are single-character. Wait, no. For example, if the run string is "ababa", which is a palindrome of length 5 (radius 2 centered at index 2). 

But in this case, each center can have varying maximum radii.

But even so, the total number of palindromic substrings in a string with no two consecutive characters being the same is O(n). Because the maximum possible radius is 0 for all positions except those where the characters alternate in a certain way. 

Wait, let's think: the run string has no two consecutive characters the same. So, for a palindrome centered at i, the maximum radius is the largest r such that S[i -k] = S[i +k] for all 0 <=k <=r. 

But since consecutive characters are different, for any palindrome of length >=3, the characters must alternate around the center. 

For example, in the run string "ababa", centered at 2 (0-based), the radius is 2. 

But for a run string like "ababab", the maximum radius for the center at index 2 is 2 (S[2-2] = 'a', S[2+2] = 'a'). 

So, in this case, the maximum radius can be up to O(n) for a run string of length O(n). 

But this is not possible. Because after a certain radius, the characters will not match. 

For example, in "abababa", the maximum radius for the center 3 (0-based) is 3. 

But the total number of palindromic substrings can be O(n^2) in the worst case. 

But with the run string of length up to 1e5, this approach will not work, as it will result in O(n^2) time.

This indicates that the expand around center approach is not feasible. Thus, we need a different way to compute the number of palindromic substrings in the run string that can be processed in O(n) time.

Alternatively, since all palindromic substrings in the run string are of odd length and their characters alternate, perhaps there's a pattern we can exploit. 

For example, each palindrome must start and end with the same character, and the characters in between form a palindrome. 

But how?

Alternatively, note that the run string has no two consecutive characters the same. So, any palindrome must have characters that are symmetric around the center. 

For example, the run string S is a palindrome if S[i] = S[L -i -1] for all i. 

But this is the general definition of a palindrome. 

But in this case, since the run string has no two consecutive characters, any palindrome must have the same first and last character, and the substring between them must also be a palindrome. 

But this is the same as the normal palindrome definition. 

So, for a run string, all palindromic substrings are of odd length. 

But how to find all such substrings efficiently?

This seems like a dead end. 

An alternative idea is that for a run string S, the number of palindromic substrings is equal to the number of possible centers where the characters expand outward as long as the left and right are the same. 

But with the run string having no consecutive duplicates, each expansion step adds two characters (left and right) which must be the same. 

But this can be done in O(n) time using Manacher's algorithm. 

Manacher's algorithm runs in O(n) time, and for each center, finds the maximum possible radius. 

The total number of palindromic substrings is the sum over all centers i of (max_radius[i] + 1). 

But since all palindromes are of odd length, and we need to process all of them, this sum would be O(n) time. 

But to process each palindrome, we need to find all possible (i, r) pairs where r ranges from 1 to max_radius[i], and then compute the contribution for each such (i, r).

But this would take O(n) time, because for each i, max_radius[i] can be up to the minimum of i and (n-1 -i), and summing across all i would be O(n) time. 

So, this is manageable. 

Thus, the plan is:

1. Use Manacher's algorithm to compute the maximum radius for each center in the run string.

2. For each center i and radius r (from 1 to max_radius[i]), compute the start and end indices of the palindrome (i -r, i +r). 

3. For each such (start, end), compute the contribution to even and odd counts based on the even and odd pairs between the runs start and end.

But wait, the start and end in the run string correspond to runs. For each such start and end in the run string, the contribution is even_contribution = odd_pairs, and odd_contribution = even_pairs. 

Thus, the code would look like:

run_chars = [r[0] for r in runs]

max_radius = manacher(run_chars)

even_multi =0

odd_multi=0

for i in range(len(run_chars)):
    max_r = max_radius[i]
    for r in range(1, max_r+1):
        start = i - r
        end = i + r
        if start <0 or end >= len(run_chars):
            break
        # compute contribution from start to end
        even_count_i = even_counts[start]
        odd_count_i = odd_counts[start]
        even_count_j = even_counts[end]
        odd_count_j = odd_counts[end]
        even_pairs = even_count_i * even_count_j + odd_count_i * odd_count_j
        odd_pairs = even_count_i * odd_count_j + odd_count_i * even_count_j
        even_multi += odd_pairs
        odd_multi += even_pairs

But this is O(n^2) in the worst case, which is not acceptable for n=1e5.

This indicates that even with Manacher's algorithm, the nested loop (for each i, for r from 1 to max_r) is O(n^2) time. For example, if the run string is "abababab...", then for each center i, max_r is up to i, leading to O(n^2) operations. 

Thus, this approach is not feasible for large n. 

So, we need a different way to compute the contributions from all palindromic substrings in O(n) time. 

Alternative idea: for each possible pair of runs (i,j) where i <=j, determine if the substring [i,j] is a palindrome. If so, add the contribution. 

But checking all pairs (i,j) is O(n^2), which is not feasible. 

Another idea: since the run string has no consecutive duplicates, the only possible palindromes are those with odd lengths, and their centers have characters that expand outward. 

But how to model this. 

Alternatively, the run string is such that any palindrome must have a symmetric structure. For example, the run string "ababa" is a palindrome. 

But for each palindrome [i,j], the contribution is len_i * len_j. 

Wait, no. The contribution is based on the product of the counts of even and odd pairs between the start and end runs. 

But even if the run string is a palindrome, the start and end runs are i and j. 

Thus, for each palindrome [i,j], the contribution is (number of pairs (x,y) where x is in run i and y is in run j and x +y is even/odd).

But how to model this.

Alternative approach:

For each possible palindrome [i,j] in the run string, compute the start and end runs, then compute even_pairs and odd_pairs as described earlier. 

But the problem is how to efficiently find all such palindromic [i,j] pairs. 

This seems stuck. 

Alternative idea: precompute for each possible run i, the maximum possible j such that [i,j] is a palindrome. Then, for each i, j can be up to some maximum. 

But again, this is O(n^2) time. 

Thus, perhaps the correct approach is to accept that this problem can be solved in O(n^2) time, but find a way to optimize it for the given constraints. 

But given the constraints (n up to 1e5), O(n^2) is impossible. 

Thus, we need to find a way to compute the contributions for all palindromic substrings in O(n) time. 

Alternative approach: find that the only possible palindromes are those where the entire run string is a palindrome, and their contributions are based on the product of pairs of runs. But this is not correct. 

Alternatively, notice that the run string's palindromes are determined by their centers. For each center, the contribution is the sum over all possible radii r of the product of the even and odd pairs for runs i-r and i +r. 

But this requires finding a way to compute this sum efficiently. 

For example, for each center i, the contributions come from palindromes of radius r=1,2,...,d_i. For each r, the start is i -r and end is i +r. 

For each such start and end, the contribution is:

even_pairs = (even_s * even_e) + (odd_s * odd_e)

odd_pairs = (even_s * odd_e) + (odd_s * even_e)

even_contribution += odd_pairs

odd_contribution += even_pairs

Where even_s is even_count[start], etc. 

Thus, for a given center i, the total contribution is the sum over r=1 to d_i of (even_pairs and odd_pairs) for the start and end runs. 

But even if we can compute this sum for each center efficiently, it's still O(n) centers and O(n) time per center. 

But perhaps for each center i, the sum can be computed in O(1) time using prefix sums. 

But how?

Suppose for each center i, the possible radius r ranges from 1 to d_i. For each r, the start and end are i -r and i +r. 

Thus, for each r, start = i -r and end = i +r. 

The contribution for radius r is:

even_contribution_r = (even_s[start] * odd_e[end] + odd_s[start] * even_e[end])

odd_contribution_r = (even_s[start] * even_e[end] + odd_s[start] * odd_e[end])

But even_e[end] is even_count[end], etc. 

The total contribution for center i is the sum over r=1 to d_i of even_contribution_r and odd_contribution_r. 

Thus, the problem reduces to, for each center i, compute the sum over r=1 to d_i of:

even_contribution_r = (even_s[i-r] * odd_e[i+r] + odd_s[i-r] * even_e[i+r])

odd_contribution_r = (even_s[i-r] * even_e[i+r] + odd_s[i-r] * odd_e[i+r])

If we can precompute the prefix sums for even_s, odd_s, even_e, odd_e, then for each center i and radius r, we can compute these terms quickly. 

But the challenge is that for each i and r, the start is i-r and end is i +r. 

This is equivalent to pairs of indices (i-r, i +r) for r=1 to d_i. 

For example, i=3, r=1: start=2, end=4.

r=2: start=1, end=5.

r=3: start=0, end=6.

Thus, for each center i, the pairs of runs are (i-r, i +r). 

This resembles a symmetric pattern around i. 

But how to compute the sum of products for these pairs.

An alternative idea is to precompute for each possible pair (x, y) where x + y is even (due to the symmetry), and then sum over all x and y such that x = i -r and y = i +r.

But this seems unclear. 

Alternatively, for each center i, the sum can be expressed as:

sum_{r=1 to d_i} [ (even[i-r] * odd[i+r] + odd[i-r] * even[i+r]) ] 

for even_contribution.

And similarly for odd_contribution.

But even and odd arrays are precomputed for each run.

This sum can be computed by iterating r from 1 to d_i and accumulating the terms. However, for large d_i (up to 1e5), this would be O(n) time per center, leading to O(n^2) time. 

Thus, this approach is not feasible. 

This indicates that we need to find a way to compute this sum for all possible centers and radii efficiently, which is not straightforward. 

Given the time constraints, perhaps the problem requires a different approach. 

Alternative Idea:

The merged string is a palindrome if and only if the first and last characters are the same, and the substring between them is also a palindrome. 

But since the merged string has no consecutive duplicates, this implies that the merged string must be of the form c, d, c, d, ... c for odd length. 

Thus, the merged string must start and end with the same character and have alternating characters. 

But how to count this. 

Alternatively, for the merged string to be a palindrome of odd length:

- The first character must be the same as the last character.

- The sequence of characters between them must form a palindrome. 

But this is the standard definition of a palindrome.

But given that the merged string has no consecutive duplicates, the entire merged string must be a palindrome, which requires that the first and last characters are the same, and the inner parts form a palindrome. 

But this is the same as the normal palindrome definition. 

Thus, the problem reduces to:

For each pair of runs (i,j) where i < j and the merged string from i to j is a palindrome:

   contribute even_contribution and odd_contribution based on the parity of the original substring's length.

But how to find these pairs (i,j) efficiently.

Another observation: for the merged string from i to j to be a palindrome, the first and last characters must be the same, and the merged string from i+1 to j-1 must also be a palindrome. 

This recursive definition suggests that we can use dynamic programming to find all palindromic substrings. 

We can create a DP table where dp[i][j] is true if the merged string from i to j is a palindrome. 

But for n=1e5, this approach is O(n^2) time and space, which is impossible. 

Thus, we are back to the original problem. 

Alternative Idea:

The merged string is a palindrome of odd length >=3 if and only if the first and last characters are the same and the merged string is a palindrome. Since the merged string has no consecutive duplicates, the merged string must alternate characters. 

For example, "ababa" is a palindrome. 

The merged string's characters must form a palindrome of odd length. 

But the merged string is a sequence of runs' characters. 

So, the merged string must be a palindrome of odd length. 

Thus, the only possible palindromic merged strings are those where the run string's substring is a palindrome of odd length. 

But how to compute the number of such palindromes efficiently. 

Manacher's algorithm can find all such palindromes in O(n) time, but the problem is to compute the contribution for each such palindrome, which involves accessing the runs i and j (start and end of the palindrome), and multiplying their even and odd pairs. 

But even if Manacher's algorithm can give us the start and end of each palindrome in O(1) time per palindrome, the nested loop over all possible radii is still O(n^2) in the worst case. 

Thus, this problem seems challenging. 

But given the sample inputs and the examples, perhaps the correct approach is to realize that the merged string must be a palindrome of odd length, and that the merged string's first and last characters are the same. 

Thus, the runs must start and end with the same character. 

So, for a merged string from run i to j to be a palindrome, the following must be true:

1. The character of run i is the same as run j.

2. The merged string of runs i+1 to j-1 is also a palindrome.

This is the standard palindrome recurrence. 

But to find all such pairs (i,j), we can use dynamic programming with memoization. 

But for n=1e5, this is not feasible. 

Alternative Idea:

For all pairs (i,j) where i < j and run[i] == run[j], and the merged string of runs i+1 to j-1 is a palindrome. 

But how to compute this. 

An alternative approach is to note that for each run i, we can find all runs j >i where run[i] == run[j], and the substring i+1 to j-1 is a palindrome. 

This is the same as finding even-length palindromes for the substring i+1 to j-1. But this is unclear. 

Alternatively, we can precompute for each run i, the possible j's where run[i] == run[j], and the merged string i to j is a palindrome. 

But again, this is O(n^2) in the worst case. 

Thus, I'm stuck. 

Perhaps the correct way is to proceed with the initial approach, despite the O(n^2) time, and find that the run string's maximum possible length is O(n), but in practice, for the given constraints, it's manageable. 

But for n=1e5, this is not possible. 

Alternative Idea:

Notice that for the merged string to be a palindrome of odd length, the run string's substring must be a palindrome of odd length. 

But the run string is a string where no two consecutive characters are the same. 

Thus, the maximum possible radius for any center in the run string is 0. Because, if the first two characters are different, then any expansion would require that the next characters are the same. 

Wait, no. For example, run string is "ababa". 

Manacher's algorithm would find that the center at index 2 (the middle 'a') has radius 2, covering the entire string. 

Thus, in this case, the maximum radius is 2. 

So, the run string can have palindromic substrings with varying radii. 

But in the worst case, the run string is like "abababab...", which allows for palindromic substrings of varying radii. 

But even so, the total number of palindromic substrings is O(n), because each expansion step is O(1) time. 

But no, for a run string of length n, the total number of palindromic substrings can be up to O(n^2). 

Thus, this problem seems impossible to solve within the time constraints. 

But given that the problem is given and the sample inputs, perhaps the correct solution is to realize that for the merged string to be a palindrome, the first and last characters are the same, and the merged string is a palindrome. 

Thus, the number of good substrings is equal to the number of palindromic substrings of the run string multiplied by the product of the lengths of the start and end runs. 

But again, this is not the case. 

Wait, perhaps the correct approach is:

For the merged string to be a palindrome, it must be of the form c_0 c_1 ... c_{k} where c_0 = c_{k}, and the middle part is a palindrome. 

But in the run string, since consecutive characters are different, any palindrome must have characters that alternate. 

Thus, the merged string's length must be odd. 

Thus, the merged string is a palindrome if and only if it is of odd length and the first and last characters are the same. 

Wait, no. For example, "aba" is a palindrome of odd length. "ababa" is also a palindrome of odd length. 

But "abba" would merge to "ab", which is not a palindrome. 

Thus, the merged string is a palindrome of odd length if and only if the run string's substring is a palindrome of odd length. 

Thus, the problem reduces to counting the number of palindromic substrings of the run string of odd length, and for each such substring, multiply the lengths of the first and last runs. 

Wait, but no. For example, in sample input 1:

input is "bb". 

The runs are [ ('b',2) ].

The run string is "b". 

Palindromic substrings are "b", which is handled in the single-run case. 

But the sample input's output includes the substring "bb" which is merged to "b", which is a palindrome. 

Wait, the sample input 1 is 'bb', which has three good substrings: "b" (length 1), "b" (length 1), and "bb" (length 2). 

But according to our initial analysis, the merged string for "bb" is "b", which is a palindrome. Thus, this substring is counted as a good substring. 

But according to the initial approach, the merged string for "bb" is length 1, which is handled in the single-run case. But the run is ('b', 2), so the single-run contribution is even_count = (2/2)^2 = 1 (even) and odd_count = (2/2) * (2/2 +1) = 1*2=2. 

But wait, the single-run case for len=2 (even) has even_count = (2/2)^2 = 1, and odd_count = (2/2)*(2/2 +1) = 1*2=2. 

But the substring "bb" is merged to "b", which is a single-run case, but it is a single run, so the contribution is even_count=1, odd_count=2. 

But the sample input's output says there are 1 even and 2 odd. Which matches the single-run case. 

But in the sample input 1, the three good substrings are "b", "b", and "bb". 

But according to the single-run contribution for len=2, the even_count is 1 (substrings of length 2) and odd_count is 2 (length 1 and 3, but len=2 has no 3). So the even_count is 1 (substring of length 2), and odd_count is 2 (substrings of length 1). 

So, in the single-run case for len=2, even_count =1 (substrings of even length) and odd_count= 2 (substrings of odd length). 

Thus, the initial approach handles the "bb" case correctly. 

But for the multi-run case, the sample input 2 is "baab". The runs are [b, a, b]. The run string is "bab". 

The palindromic substrings are:

- "b" (run 0)

- "a" (run 1)

- "b" (run 2)

- "bab" (runs 0-2)

The multi-run contribution comes from the "bab" palindrome. 

For this palindrome, start=0, end=2. 

Run 0: len=1, start_parity=1 (start=1). So even_count_i =0, odd_count_i=1.

Run 2: len=1, start_parity=4 (start=1+2+1=4. 4%2=0). So even_count_j=1, odd_count_j=0.

even_pairs = (0 *1) + (1 *0) =0.

odd_pairs = (0 *0) + (1 *1) =1.

So, even_contribution +=1, odd_contribution +=0.

The multi-run even is 1, and the single-run even is 1 (from run 1, len=2). 

But according to the sample input 2's output, the even count is 2. 

Ah, the sample input's even count is 2. 

But according to the initial approach, the single-run even_count is 1 (run 1, len=2 contributes 1 even), and the multi-run even_contribution is 1 (from "bab"), so total even is 2. 

Which matches. 

Thus, the approach is correct. 

But the problem is how to compute the multi-run contributions efficiently.

But given that Manacher's algorithm is O(n), and for each palindrome, the start and end runs can be determined, the code must process all palindromes in O(n) time. 

But how?

An alternative Idea:

The multi-run contribution for a palindromic substring [i,j] in the run string is len_i * len_j, and the parity of the original substring's length depends on the sum of the lengths of the runs i to j, but this is not correct. 

But earlier analysis shows that the parity depends on the start and end positions in runs i and j. 

Thus, the correct approach is to process each palindrome in the run string, compute the start and end runs, and compute even_pairs and odd_pairs. 

But with Manacher's algorithm, the number of palindromes is O(n), and for each palindrome, the processing is O(1) time. 

But how?

Manacher's algorithm provides the maximum radius for each center. For each center, the maximum number of palindromes is equal to the maximum radius. 

But in practice, the sum of all radii is O(n), as Manacher's algorithm is linear. 

Thus, the code can proceed as follows:

Implement Manacher's algorithm to find the maximum radius for each center. 

For each center i, and for each possible radius r (from 1 to max_radius[i]), compute the start and end runs (i -r and i +r). 

For each such start and end, compute the even_pairs and odd_pairs. 

This is O(n) time if the total number of palindromes is O(n). 

But is this possible?

Yes, because the sum of max_radius[i] for all i is O(n). 

Manacher's algorithm processes each character in O(1) time, and the total time is O(n). 

Thus, even though for each center i, there are max_radius[i] radii to process, the total sum over all max_radius[i] is O(n). 

Thus, the total number of palindromes processed is O(n). 

Thus, the code can process each palindrome in O(1) time, leading to O(n) time overall. 

This is the key insight. 

Thus, the code can proceed as follows:

1. Process the input into runs.

2. Precompute even_count and odd_count for each run.

3. Generate the run string.

4. Compute the max_radius for each center using Manacher's algorithm.

5. Iterate through each center and radius, compute start and end runs, and accumulate the even and odd pairs.

Thus, the code can be implemented in O(n) time. 

Now, implementing Manacher's algorithm:

The standard implementation for Manacher's algorithm for odd-length palindromes:

def manacher(s):
    n = len(s)
    d = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else min(d[l + r - i], r - i + 1)
        while 0 <= i - k and i + k < n and s[i -k] == s[i +k]:
            k +=1
        d[i] = k
        if i +k -1 > r:
            l = i -k +1
            r = i +k -1
        d[i] = k -1  # because k was incremented once more after the loop
    return d

Wait, no. The standard Manacher's algorithm for odd-length palindromes uses a radius that is the number of steps the palindrome can expand. 

But I'll need to refer to the correct implementation. 

An alternative implementation:

def manacher(s):
    s = '#' + '#'.join(s) + '#'
    n = len(s)
    P = [0] * n
    C = R = 0

    for i in range(n):
        mirror = 2*C -i
        if i < R:
            P[i] = min(R -i, P[mirror])
        # expand around center
        a, b = i + P[i] +1, i - P[i] -1
        while a < n and b >=0 and s[a] == s[b]:
            P[i] +=1
            a +=1
            b -=1
        if i + P[i] > R:
            C = i
            R = i + P[i]
    return P

But this is for the standard Manacher's algorithm which finds all palindromes (even and odd). 

But since we have a run string with no two consecutive characters the same, even-length palindromes are impossible. Thus, the standard Manacher's algorithm can be modified to process only odd-length palindromes. 

But perhaps using the standard algorithm and then filtering even-length palindromes is better. 

But for our case, since even-length palindromes are impossible, we can process the run string using the standard Manacher's algorithm and then extract only the odd-length palindromes. 

But this is not necessary. 

Thus, the code for Manacher's algorithm can be adjusted to process the run string and find all palindromic substrings of odd length. 

But given time constraints, perhaps the standard Manacher's code can be used, and then for each palindrome length, we can check if it's odd. 

But this is redundant because all palindromes in the run string are of odd length. 

Thus, for each palindrome in the run string, the length is 2*P[i]+1 (if using the transformed string). But perhaps the code can be adapted. 

But perhaps it's easier to use the original Manacher's code for odd-length palindromes. 

But in any case, the code must be implemented. 

Now, putting it all together:

The code steps are:

Read the input string.

Process into runs.

Compute prefix sums.

Precompute even_counts and odd_counts for each run.

Generate the run string.

Compute max_radius for each center using Manacher's algorithm.

Iterate through each center and radius to accumulate the contributions.

Sum the single-run contributions.

Output the even and odd totals.

Thus, the code would look something like this:

But given time constraints, here's the code:

Processing runs:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    if not s:
        print(0, 0, file=output_stream)
        return

    runs = []
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count +=1
        else:
            runs.append( (prev, count) )
            prev = c
            count =1
    runs.append( (prev, count) )

    m = len(runs)
    if m ==0:
        print(0,0, file=output_stream)
        return

    # Compute prefix sums of run lengths
    prefix = [0]*(m+1)
    for i in range(m):
        prefix[i+1] = prefix[i] + runs[i][1]

    # Precompute even and odd counts for each run
    even_counts = []
    odd_counts = []
    for i in range(m):
        start_i = prefix[i] +1
        start_parity = start_i % 2
        len_i = runs[i][1]
        if start_parity ==0:
            even_count = (len_i +1)//2
            odd_count = len_i//2
        else:
            even_count = len_i//2
            odd_count = (len_i +1)//2
        even_counts.append(even_count)
        odd_counts.append(odd_count)

    # Generate run string
    run_chars = [r[0] for r in runs]

    # Manacher's algorithm to find all odd-length palindromes
    def manacher(s):
        n = len(s)
        d = [0]*n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r -i +1)
            while 0 <= i -k and i +k < n and s[i-k] == s[i+k]:
                k +=1
            d[i] = k-1
            if i +k -1 > r:
                l = i -k +1
                r = i +k -1
        return d

    max_radius = manacher(run_chars)

    even_multi = 0
    odd_multi =0

    for i in range(len(run_chars)):
        radius = max_radius[i]
        for r in range(1, radius+1):
            start = i -r
            end = i +r
            if start <0 or end >= len(run_chars):
                continue
            # Check if start and end are valid
            if run_chars[start] != run_chars[end]:
                continue  # This should not happen due to Manacher's algorithm
            # Get even and odd counts for start and end
            even_s = even_counts[start]
            odd_s = odd_counts[start]
            even_e = even_counts[end]
            odd_e = odd_counts[end]
            even_pairs = even_s * even_e + odd_s * odd_e
            odd_pairs = even_s * odd_e + odd_s * even_e
            even_multi += odd_pairs
            odd_multi += even_pairs

    # Compute single-run contributions
    even_single = 0
    odd_single =0
    for i in range(m):
        L = runs[i][1]
        if L %2 ==0:
            even_single += (L//2)**2
            odd_single += (L//2) * (L//2 +1)
        else:
            even_single += (L**2 -1)//4
            odd_single += ((L+1)//2)**2

    # Total
    even_total = even_single + even_multi
    odd_total = odd_single + odd_multi

    print(even_total, odd_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
baab
""",
            "output": \
"""\
2 4
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    if not s:
        print(0, 0, file=output_stream)
        return

    runs = []
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count +=1
        else:
            runs.append( (prev, count) )
            prev = c
            count =1
    runs.append( (prev, count) )

    m = len(runs)
    if m ==0:
        print(0,0, file=output_stream)
        return

    # Compute prefix sums of run lengths
    prefix = [0]*(m+1)
    for i in range(m):
        prefix[i+1] = prefix[i] + runs[i][1]

    # Precompute even and odd counts for each run
    even_counts = []
    odd_counts = []
    for i in range(m):
        start_i = prefix[i] +1
        start_parity = start_i % 2
        len_i = runs[i][1]
        if start_parity ==0:
            even_count = (len_i +1)//2
            odd_count = len_i//2
        else:
            even_count = len_i//2
            odd_count = (len_i +1)//2
        even_counts.append(even_count)
        odd_counts.append(odd_count)

    # Generate run string
    run_chars = [r[0] for r in runs]

    # Manacher's algorithm to find all odd-length palindromes
    def manacher(s):
        n = len(s)
        d = [0]*n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r -i +1)
            while 0 <= i -k and i +k < n and s[i-k] == s[i+k]:
                k +=1
            d[i] = k-1
            if i +k -1 > r:
                l = i -k +1
                r = i +k -1
        return d

    max_radius = manacher(run_chars)

    even_multi = 0
    odd_multi =0

    for i in range(len(run_chars)):
        radius = max_radius[i]
        for r in range(1, radius+1):
            start = i -r
            end = i +r
            if start <0 or end >= len(run_chars):
                continue
            # Check if start and end are valid
            if run_chars[start] != run_chars[end]:
                continue  # This should not happen due to Manacher's algorithm
            # Get even and odd counts for start and end
            even_s = even_counts[start]
            odd_s = odd_counts[start]
            even_e = even_counts[end]
            odd_e = odd_counts[end]
            even_pairs = even_s * even_e + odd_s * odd_e
            odd_pairs = even_s * odd_e + odd_s * even_e
            even_multi += odd_pairs
            odd_multi += even_pairs

    # Compute single-run contributions
    even_single = 0
    odd_single =0
    for i in range(m):
        L = runs[i][1]
        if L %2 ==0:
            even_single += (L//2)**2
            odd_single += (L//2) * (L//2 +1)
        else:
            even_single += (L**2 -1)//4
            odd_single += ((L+1)//2)**2

    # Total
    even_total = even_single + even_multi
    odd_total = odd_single + odd_multi

    print(even_total, odd_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
babb
""",
            "output": \
"""\
2 5
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


