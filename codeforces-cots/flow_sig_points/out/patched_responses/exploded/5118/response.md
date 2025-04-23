<think>
Okay, let's see. The problem is to find the number of ways to remove exactly one substring from the given string such that all remaining characters are the same. The answer has to be modulo 998244353. 

First, I need to understand what constitutes a valid way. The substring removal must leave all remaining characters equal. Also, removing the entire string is allowed, which counts as all characters being removed (so zero left, which is considered valid). Also, the substring must be exactly one; so you can't remove multiple non-contiguous parts. 

Let's think about possible scenarios where the remaining characters are all the same. There are two main cases:

1. The remaining characters are all the same after removing a substring. This can happen in two ways:
   a. The remaining part is a prefix (possibly empty) consisting of a single character, followed by a gap (the removed substring), and then a suffix (possibly empty) of the same character. But wait, no. Because when you remove a substring, the remaining parts are the parts before and after the substring. So after removal, the left and right parts are concatenated. So for the entire remaining string to be the same character, either the left part is all some character and the right part is all the same (but they must be the same as each other), or one of the parts is empty.

Wait, maybe the valid cases are when the left part (before the removed substring) consists of some number of the same character, say 'a's, and the right part (after the removed substring) also consists of 'a's, possibly zero. But that's not the only case. Alternatively, maybe the entire remaining string is a prefix of some character, or a suffix of some character, or a combination where the prefix and suffix are the same character.

Alternatively, here's a better approach: the remaining string must be either all left (so the entire right part is removed), all right (entire left is removed), or a combination where the left prefix and right suffix are the same character. 

So for example, if the string starts with a bunch of 'a's and ends with a bunch of 'a's, then removing the middle part (which includes all the non-'a's) would leave the prefix and suffix 'a's, which are all 'a's. So that's a valid case.

So the possible valid cases can be broken down as:

1. Remove a substring that leaves only a prefix of a certain character. For example, removing all characters from position i onwards. But the prefix up to i-1 must be all the same character. Or wait, no. Because the remaining part after removal is the prefix up to l-1 and the suffix from r+1 onwards. So if you remove a substring s[l..r], then the remaining is s[0..l-1] + s[r+1..n-1]. For this to consist of all the same character, either:

- The left part (before l) is empty, and the right part (after r) is all the same character. Or,
- The right part is empty, and the left part is all the same character. Or,
- Both the left and right parts are non-empty and consist of the same character.

Wait, but for the remaining string to be all the same, the left and right parts must consist of the same character. So the valid cases are when:

Either:

- All the left part (if non-empty) is the same character c, and all the right part (if non-empty) is the same character c. 

So, the possible scenarios are:

a) The remaining string is all the same character c, possibly formed by a prefix of c and a suffix of c with some part removed in between.

So how do I compute all possible such substrings?

Alternatively, perhaps the valid cases are when the union of the left and right parts (after the substring is removed) is all the same character.

So to model this, let's first find the longest prefix of the same character and the longest suffix of the same character. Let's call the prefix length as 'left' and the suffix length as 'right'. The prefix is s[0], s[1], ..., s[left-1], all the same character. The suffix is s[n-right], ..., s[n-1], all the same character.

If the prefix and suffix characters are different, then the only possible valid cases are removing a substring that leaves a prefix of the left character (so the entire right part is removed), or a suffix of the right character (entire left part is removed). But wait, no. Because if the prefix is all 'a's and the suffix is all 'b's, then any substring removal that leaves only 'a's (like removing the entire string except the prefix) or only 'b's (removing the entire string except the suffix) would be valid. Also, if you remove a substring that includes all the 'a's except some, but that's not possible because the remaining left part would have 'a's and the right part would have 'b's, which are different. So in that case, the only valid ways are to take the entire prefix or entire suffix.

But if the prefix and suffix are the same character, then there's another possibility: combining some of the prefix and some of the suffix. For example, if the string starts with 'a's and ends with 'a's, then removing the middle part (which contains non-'a's) would leave a combination of prefix and suffix 'a's, which is all 'a's. So in this case, the number of valid ways includes these possibilities.

So the approach is to first compute the maximum prefix length (left) of the same character, and the maximum suffix length (right) of the same character. Then:

- If the prefix and suffix characters are different, then the answer is (left + right + 1). Wait, no. Let's see. For example, in the third test case input, which is "az". The maximum prefix is 1 (a), the suffix is 1 (z). The answer is 3. According to (left + right +1) that would be 1+1+1=3, which matches. For the first example, the input is 'abaa' (a, then b, a, a). The maximum prefix is 1 (a), the suffix is 2 (a). So if they are the same, then the answer is left + right +1. Wait, in the first example, the answer is 6, which is 1 + 2 + (1 * 2) + 1? Or maybe not.

Wait, let's look at the first example. The input is 'abaa' (n=4). The prefix is the first 'a' (left=1). The suffix is the last two 'a's (right=2). The characters are the same. So the answer would be (left + right + 1). 1+2+1 =4. But the actual answer is 6. So that formula is incorrect.

Hmm, maybe I need to rethink.

Alternative approach: the answer is the sum of:

1. The number of ways to remove a substring that leaves a prefix (possibly empty) of a single character.

2. The number of ways to remove a substring that leaves a suffix (possibly empty) of a single character.

3. If the first and last characters are the same, the number of ways to remove a substring that leaves a combination of some prefix and some suffix (with the same character), minus the overlap between these cases.

Wait, this might get complicated. Let's think.

For case 1: removing a substring that leaves a prefix of c. The prefix can be any number of c's up to the maximum possible. For example, if the string starts with k c's, then the number of ways to leave a prefix of c is equal to the number of possible substrings you can remove that result in a prefix of c. That would be: for each possible length of the prefix (from 0 to k), how many substrings can I remove such that the remaining prefix is exactly that length. Wait, maybe not. Let's think.

Alternatively, to leave a prefix of c (assuming the first character is c), the remaining characters after removal must consist of some number of c's, possibly zero. So the allowed substrings are those that start after the prefix. For example, if the maximum prefix is m (all c's), then any substring that starts at position m (the first non-c) and ends anywhere (including the end) would allow the remaining prefix to be m. Wait, maybe not. Let's see. Let's say the maximum prefix is m. Then, to leave a prefix of c's, the substring to remove must start at some position l (from 0 to m) and end at some position r (>= l). Wait, perhaps this is getting too complicated.

Alternatively, the number of ways to leave a prefix of length i (all c's) is equal to (n - i) possible substrings. Because to leave exactly the first i characters (which are all c's), you can remove any substring that starts at i, i+1, ..., n-1. Wait, no. For example, if i is 0 (no prefix), then the substring to remove must be the entire string. But 0 is allowed here. Wait, the problem states that you have to remove exactly one substring. So to leave a prefix of i characters (all c's), the substring removed must start at i, and end at any position from i to n-1. So the number of possible substrings is (n - i). For example, i=0: the substring to remove is from 0 to any position (since the prefix is 0, which is allowed if the entire string is removed). Wait, but in that case, the remaining string is empty, which is allowed. So for each i from 0 to m (where m is the maximum possible prefix length of c's), the number of possible substrings is (n - i) ?

Wait, maybe the maximum prefix m is the longest possible sequence of the first character. For example, if the string starts with a, a, a, then m is 3. But if after that there's another a, but the next character is different, then m is 3. So for the case where the prefix is m characters of a, the possible ways to leave a prefix of i a's (0 <= i <= m) is (n - i). Because the substring to remove must start at i and end anywhere from i to n-1. So for each i, the number of ways is 1 (start at i, end at i), 1 (start at i, end at i+1), etc., up to start at i, end at n-1. So total (n - i) ways. But then the sum for i from 0 to m is sum_{i=0}^m (n -i). Wait, but wait. For example, if the maximum prefix is m, then for i > m, the first i characters are not all the same. So in that case, those i's are not allowed. So the sum would be from i=0 to m.

Similarly for the suffix. Let's say the maximum suffix is k characters of the same character (could be same or different from the prefix). Then the sum for the suffix is sum_{j=0}^k (j + 1) possible ways. Because to leave j characters in the suffix (all the same), you can remove any substring that starts at 0, 1, ..., (n-j-1) and ends at (n-j-1). Because the remaining substring after removal is from (n-j) to end. So for example, j=0: remove the entire string. j=1: remove substring from start to n-2. j=2: start to n-3, etc. So the number of ways for j is (n-j) ways again. Wait, no: for a suffix of j characters, the substring to remove must start at any position from 0 up to (n-j-1) and end at (n-j-1). So the number of possible substrings is (n-j) (since start can be 0 to (n-j-1), and end is (n-j-1), but the substring must include from start to end. So the number of substrings is (n-j) choices for start, and end is fixed as (n-j-1). Wait, no. For example, for j=2 in a string of length 5, the suffix is the last 2 characters. So the substring to remove is any substring that starts at 0,1,2 and ends at 2,3. Wait, maybe this is getting too confusing.

Alternatively, for the suffix part, the number of ways to leave exactly j characters (all the same) in the suffix is (n - j) possible substrings. Because to remove a substring that starts at 0, and ends at (n-j-1). Or starts at 1, ends at (n-j-1). Wait, no. For example, to leave j suffix characters, the substring to remove must start at some l and end at (n-j-1). So the substring starts at l and ends at r = (n-j-1). Then the remaining suffix is from (n-j) to end, which has length j. So l can be any value from 0 to (n-j-1). So the number of possible substrings is (n-j) (since l ranges from 0 to (n-j-1), and r is (n-j-1), so the length is (n-j-1 - l + 1) = (n-j - l) ). Wait, but the substring can start at any l and end at any r >= l, as long as the suffix is j characters. So the way to leave j suffix characters is to remove a substring that starts anywhere and ends exactly at (n-j-1). So for j suffix characters, the number of possible substrings is (n-j) (since the start can be from 0 to (n-j-1), inclusive). So for each j, the number of ways is (n-j).

So sum for the suffix is sum_{j=0}^k (n-j), where k is the maximum suffix length.

But wait, what if the suffix's character is different from the prefix's? Then the sum for the prefix and the sum for the suffix are added, but we have to subtract the overlapping case where we remove the entire string (counted once in prefix sum and once in suffix sum). Because the entire string removal is allowed and counted once in each sum. So in that case, the total would be (sum for prefix) + (sum for suffix) - 1.

Wait, but when the prefix and suffix characters are different, the only overlapping case is the entire string removal. Because that's the only way that the remaining string is empty, which is counted in both sums (as i=0 and j=0). So in that case, when adding the two sums, we have to subtract 1 to avoid double-counting the entire string removal.

But if the prefix and suffix are the same character, then the sum for prefix and sum for suffix would include overlapping cases. For example, if the entire string is of the same character, then all possible substrings are valid. But in this problem, the input is guaranteed to have at least two different characters, so the entire string can't be all same. So when the prefix and suffix are the same, the sum for prefix and sum for suffix might overlap in some cases. So perhaps the approach is:

If the first character (c1) and last character (c2) are different, then the answer is (sum of prefix ways) + (sum of suffix ways) - 1 (since the entire string removal is counted in both sums, but it's one way).

If c1 and c2 are the same, then the answer is (sum of prefix ways) + (sum of suffix ways) - (overlap) + (additional ways where you combine some prefix and suffix).

Wait, but this is getting complicated. Let's think with examples.

Take the first example: 'abaa'. The first character is 'a', last is 'a'. The prefix is 1 (only the first 'a'), the suffix is 2 (last two 'a's). So sum for prefix is (n - 0) + (n -1) = 4 (i=0: 4 ways, i=1: 3 ways). Wait, sum_{i=0}^1 (4 - i) = 4 +3=7. Sum for suffix is (4 -0) (j=0) + (4-1) (j=1) + (4-2) (j=2) =4 +3 +2=9. But the actual answer is 6. So that approach can't be right. So this suggests that the initial idea is incorrect.

Wait, the first example's correct answer is 6. Let's see all the possible ways:

The valid ways are:

- Remove substring s[1..2] (positions 0-based or 1-based? The problem statement uses 1-based in the example. Let's check. The first example's input is abaa (length 4). The correct answer lists substrings from positions 1;2 to 2;4. Assuming the positions are 1-based. So for example, s[1..2] is the first two characters (a and b). Removing that leaves the third and fourth 'a's, which are 'aa' — valid.

Hmm, perhaps the initial approach is not correct. Let's try to model this properly.

Alternative approach: the remaining characters after removal must all be the same. So the remaining string can be:

- All the same character, possibly empty.

So, the possible scenarios are:

1. The entire string is removed (counts as 1 way).

2. The remaining string is a non-empty prefix of some character c.

3. The remaining string is a non-empty suffix of some character d.

4. The remaining string is a combination of a prefix of c and a suffix of c, but in between those parts, some characters are removed. So the prefix and suffix are both c and the removed substring is in between them.

So, how to model all these possibilities.

Let's break down into cases based on the first and last characters.

Case 1: The first character (c1) and last character (c2) are different.

In this case, the only possible valid ways are:

- Remove a substring that leaves a prefix of c1 (all same characters up to some point).

- Remove a substring that leaves a suffix of c2 (all same characters from some point to the end).

- Remove the entire string (counted once).

But in this case, the prefix and suffix can't be combined since c1 and c2 are different.

So the number of ways is (number of ways to leave a prefix of c1) + (number of ways to leave a suffix of c2) + 1 (the entire string removal).

Wait, no. Because in the case where c1 and c2 are different, the entire string removal is counted in both the prefix sum (i=0) and the suffix sum (j=0). So when we compute (prefix_sum + suffix_sum), we have to subtract 1 to avoid double-counting the entire string removal.

So for case 1 (c1 != c2), the answer is (prefix_sum + suffix_sum - 1).

But what's prefix_sum? It's the sum of (n - i) for i from 0 to m, where m is the maximum prefix length of c1.

Similarly, suffix_sum is sum of (n - j) for j from 0 to k, where k is the maximum suffix length of c2.

Case 2: The first and last characters are the same (c).

In this case, the possible valid ways are:

- All the ways where the remaining string is a prefix of c (sum of (n-i) for i from 0 to m, where m is max prefix length).

- All the ways where the remaining string is a suffix of c (sum of (n-j) for j from 0 to k, where k is max suffix length).

- All the ways where the remaining string is a combination of some prefix of c and some suffix of c. But how?

For example, suppose the string starts with m c's and ends with k c's. Then, removing any substring that starts in the prefix (from 0 to m-1) and ends in the suffix (from (n -k) to n-1). Wait, but the substring must be contiguous. So, if the substring starts in the prefix and ends in the suffix, then the remaining string would be the part of the prefix before the start and the part of the suffix after the end, which are all c's. So the total ways here would be (m) * (k), since the start can be any of the first m positions (0-based?), and the end can be any of the last k positions.

Wait, let's see. Let's say the prefix has m c's (positions 0 to m-1), and the suffix has k c's (positions n-k to n-1). Then, any substring that starts at s (0 <= s <= m-1) and ends at e (n-k <= e <= n-1) can be removed. The remaining string would be the prefix 0..s-1 (all c's) and the suffix e+1..n-1 (all c's). So the remaining characters are all c's. So the number of such substrings is m * k. Because for each s in 0..m-1 and e in n-k..n-1, the substring s..e is removed. So the total is m * k.

So for case 2 (c1 == c2 = c), the answer is (prefix_sum + suffix_sum - 1) + m * k.

But wait, when we add prefix_sum and suffix_sum, we subtract 1 to avoid counting the entire string removal twice. Then, we add m*k for the overlapping cases.

Wait, but why subtract 1? Because when c1 and c2 are the same, the entire string removal is counted in both prefix_sum (i=0) and suffix_sum (j=0), so adding them would count it twice. So the total is (prefix_sum + suffix_sum - 1) + (m * k).

But let's check with the first example:

First example: s = abaa. c1 = a, c2 = a. m (max prefix) is 1 (only the first 'a'), k (max suffix) is 2 (last two 'a's). So m=1, k=2.

prefix_sum is sum_{i=0}^1 (4 -i) = 4 +3 =7. suffix_sum is sum_{j=0}^2 (4-j) =4 +3 +2=9. So (7 +9 -1) =15. Then add m*k=1*2=2. Total 15+2=17, but the correct answer is 6. So this can't be right.

Wait, clearly something is wrong here. Let's re-examine the approach.

Alternative Idea:

The correct approach must account for all possible valid substrings. Let's think of all possible ways to remove a substring and leave a string of all same characters.

The valid ways are:

1. Remove the entire string: 1 way.

2. Remove a substring that leaves a non-empty prefix (all same character).

3. Remove a substring that leaves a non-empty suffix (all same character).

4. Remove a substring that leaves both a prefix and suffix of the same character (but the prefix and suffix are adjacent in the original string, but separated by the removed substring).

So, for the case where the first and last characters are the same, the count includes all four possibilities. For the case where first and last are different, only possibilities 1,2,3, and in possibility 2 and 3, the characters must be the same as the first or last.

So, perhaps the formula is:

If the first and last characters are different:

answer = (number of prefix ways) + (number of suffix ways) - 1.

Because the entire string removal is counted once in prefix (i=0) and once in suffix (j=0), so subtract 1 to avoid double-counting.

If the first and last are the same:

answer = (number of prefix ways) + (number of suffix ways) - 1 + (m * k).

But in the first example, let's compute this.

prefix ways: the number of ways to leave a prefix of 'a's. The maximum prefix m is 1. So for i=0 (remove entire string) → 1 way (but since in the case of c1 and c2 being same, the entire string is allowed here. But in the example, the problem says the input has at least two different characters, so the entire string can't be all same. So when we compute the prefix_sum, it's sum_{i=0}^m (n-i) where m is the maximum possible. For i=0, the prefix is 0 characters, so the remaining is empty. That's allowed and counts as 1 way (entire string removed). For i=1, the prefix is the first character (a), so the number of ways is (n -i) = 4-1=3. So prefix_sum = 1 +3 =4.

Similarly, suffix_sum is sum_{j=0}^k (n-j), where k is 2 (max suffix of a's). For j=0 → 4 ways (entire string removed), j=1 →3 ways (remove substring ending at position n-2), j=2 →2 ways (remove substring ending at n-3). So suffix_sum=4+3+2=9.

So (prefix_sum + suffix_sum -1) =4+9-1=12. Then add m*k=1*2=2 → total 14. But the correct answer is 6. So this approach is definitely wrong.

Hmm, clearly my previous reasoning is incorrect. Let's think again.

Alternative approach:

The problem is to count the number of substrings that can be removed such that the remaining characters are all the same. Let's think of all possible such substrings.

The remaining characters are the concatenation of the left part (before the removed substring) and the right part (after the removed substring). So for the remaining characters to be all the same, the left and right parts must all be the same character, and that character must be the same in both.

So possible cases:

1. Left part is empty: the right part is all the same character. So the right part must consist of all the same character. The substring to remove is from the beginning (0) up to some position r. The remaining right part (r+1 to end) must be all same character.

2. Right part is empty: left part is all same character.

3. Both left and right parts are non-empty and consist of the same character.

So the total ways are the sum of the ways in each of these three cases.

Let's break down each case.

Case 1: Right part is all same character. How many ways to remove a substring that starts at 0 and ends at r (0 ≤ r ≤ n-1), such that the remaining right part (r+1 to end) is all same character. But wait, the substring to remove can be any substring that leaves the right part. So for example, the substring can start anywhere as long as the entire right part is after it. Wait no. If you remove a substring [l, r], then the remaining right part is from r+1 to end. So for case 1 (left is empty), the substring must start at l=0 and end at any r. But the remaining right part (r+1 to end) must be all same character.

But for the right part to be all same character, the entire right part (from r+1 to end) must be the same character. So for this case, the right part can be of any length (including zero, which is handled in case 1 when r =n-1).

Wait, but in case 1, the left part is empty, which implies that the substring to remove starts at l=0 and ends at r. Then the remaining right part is r+1 to end. For that remaining part to be all same character, the substring from r+1 to end must be all same character. So the maximum possible r is such that the suffix starting at r+1 is all same.

Similarly for case 2: the right part is empty. The substring to remove starts at l and ends at n-1. The left part (0 to l-1) must be all same character.

Case 3: Both left and right parts are non-empty and all same character. So the left part (0 to l-1) is all c, and the right part (r+1 to end) is all c. So the substring to remove is [l, r]. So for this case, the left part's character and the right part's character must be the same.

So the total number of ways is:

(number of ways in case 1) + (number of ways in case 2) + (number of ways in case 3).

Now, let's compute each case.

Case 1: Right part is all same character.

To compute this, we need to find all possible r (0 ≤ r ≤ n-1) such that the substring from r+1 to end is all same character.

The maximum possible r for which the suffix is all same is the position such that s[r+1] = s[r+2] = ... = s[n-1]. Let's compute the longest suffix of the same character. Let's call this 'suffix_len' and the character is 'c_suffix'.

So, the suffix can be of length 0 (empty) up to suffix_len. Wait, no. The maximum suffix length is 'suffix_len', and the suffix starts at position (n - suffix_len). So for any r where r+1 >= (n - suffix_len) and r+1 <= n-1, the suffix from r+1 to end is all c_suffix. Wait, no. For example, if the entire suffix is of length k, then the last k characters are the same. So for the right part to be all same, the substring r+1 to end must be within this suffix.

So for case 1, the possible r's are those where r+1 is >= (n - suffix_len). Because then the suffix from r+1 is part of the maximum suffix and thus all same characters.

So the number of ways for case 1 is the number of possible r such that r+1 >= (n - suffix_len). Because then the right part is all same. But also, the substring to remove is [0, r]. So the substring starts at 0 and ends at r. So for each such r, the substring [0..r] is removed, leaving the right part from r+1 to end.

So the possible r's are from (n - suffix_len -1) to (n-1). Because r+1 must be >= n - suffix_len. So r >= n - suffix_len -1. And r can be up to n-1 (so the entire right part is empty).

The number of possible r's is (n-1) - (n - suffix_len -1) +1 = suffix_len +1.

Wait, let's see:

n - suffix_len -1 <= r <= n-1.

Number of integers in this range is (n-1) - (n - suffix_len -1) +1 = suffix_len +1.

So case 1 contributes (suffix_len + 1) ways.

Similarly, case 2: left part is all same. The substring to remove starts at l and ends at n-1, and the left part (0 to l-1) is all same. The possible l's are from 0 to (prefix_len -1). Because the left part (0 to l-1) must be all same as the prefix character.

So the number of possible l's is prefix_len. Because l can be 0, 1, ..., prefix_len-1. For each l, the substring [l..n-1] is removed, leaving the left part (0..l-1) which is all same.

So case 2 contributes prefix_len ways.

Case 3: both left and right parts are non-empty and same character. So the left part (0..l-1) is all c, and the right part (r+1..n-1) is all c, and c is the same for both. So the character must be the same as the prefix and suffix, which implies that the prefix and suffix are of the same character. So this case is possible only if the prefix and suffix characters are the same.

So, if the prefix character (c_prefix) is different from the suffix character (c_suffix), case 3 contributes 0.

Otherwise, case 3 contributes the number of possible pairs (l, r) such that l is in [0, prefix_len -1], r is in [n - suffix_len, n-1], and l <= r. So the substring [l..r] is removed. For each l in 0..prefix_len-1 and r in (n - suffix_len)..n-1, the substring is valid. So the number of ways is prefix_len * suffix_len.

But wait, the substring can be any l <= r where l is in the prefix (all c) and r is in the suffix (all c). For example, l can be 0 and r can be n-1 (removing the entire string). But wait, that's case 1 (if l=0, r can be up to n-1, but then the left part is empty and right part is empty. But in case 3, left and right parts are non-empty. So perhaps case 3 requires that both left and right parts are non-empty.

So for case 3, the left part (0..l-1) must be non-empty and all c, and the right part (r+1..n-1) must be non-empty and all c. So l must be >=1 (so left part has at least one character) and r must be <=n-2 (so right part has at least one character). So the l ranges from 0 to prefix_len-1 (but l can be 0, which would make left part empty, which is not allowed). So this requires l >=0, but the left part (0..l-1) must be non-empty. So l must be >=1. Similarly, the right part (r+1..n-1) must be non-empty, so r+1 <=n-1 → r <=n-2.

So the valid l's are 1..prefix_len-1, and valid r's are (n-suffix_len)..n-2.

So the number of ways in case 3 is (prefix_len - 1) * ( (n-2) - (n-suffix_len) +1 ) → (prefix_len-1) * (suffix_len -1 +1) → (prefix_len-1)* suffix_len.

Wait, let me compute the range of r:

r must be >= n - suffix_len and <=n-2. The number of possible r's is (n-2) - (n-suffix_len) +1 = suffix_len -1.

So the total for case 3 is (prefix_len-1) * (suffix_len -1 +1) ? Wait, the range is from (n-suffix_len) to (n-2). So the number of possible r's is (n-2) - (n-suffix_len) +1 = suffix_len -1. So for each l in 1..prefix_len-1, there are (suffix_len -1) possible r's.

So case 3 contributes (prefix_len-1) * (suffix_len -1) ways.

But only if the prefix and suffix characters are the same.

Putting it all together:

If c_prefix != c_suffix:

answer = case1 + case2 + case1_entire_string.

Wait, no. Because case1 includes the entire string removal. Let's re-express.

Wait, case 1 includes the entire string removal when r =n-1. Then, the remaining part is empty (r+1 is n, which is beyond the end). So that's allowed and counted as case 1.

Similarly, case 2 includes the entire string removal when l=0. So the entire string is removed. But in this case, case1 and case2 both count the entire string removal. So for the case where c_prefix != c_suffix, the entire string removal is counted once in case1 (if c_suffix is the same as the suffix's character) and once in case2 (if c_prefix is the same as the prefix's character). Wait, no. Because when c_prefix and c_suffix are different, case1 is when the remaining part is all c_suffix. So case1 includes the entire string removal only if the suffix is all c_suffix, which it is. So if the entire string is removed, it's allowed (counted once). But when c_prefix and c_suffix are different, the entire string removal is counted in case1 (if c_suffix is the suffix's character), and in case2 (if c_prefix is the prefix's character). But if the entire string is allowed in case1 and case2, but only when the remaining parts are all same. But in the case of entire string removal, the remaining part is empty, which is allowed. So this would be counted in case1 (if the suffix is c_suffix and the right part is empty), but also in case2 (if the left part is empty and prefix is c_prefix). But if c_prefix and c_suffix are different, the entire string removal is allowed once, but it's counted in both case1 and case2. So we need to subtract 1 to avoid double-counting.

So, for c_prefix != c_suffix:

answer = case1 + case2 - 1 + case3.

But case3 is zero in this case.

So:

answer = (suffix_len +1) + (prefix_len) -1 + 0 → suffix_len +1 + prefix_len -1 = suffix_len + prefix_len.

Wait, but this can't be right. Let's test with the third example:

Third example: input is 'az' (n=2). The prefix is 1 a, the suffix is 1 z. So case1 is suffix_len +1 =1+1=2 (r can be 0 and 1). For r=0: remove [0..0], remaining is 'z' (valid). For r=1: remove entire string, remaining is empty (valid). So case1 contributes 2 ways. Case2 is prefix_len=1 ways (remove from l=0 to 1: entire string, but that's counted in case1). Wait, case2 is when you remove a substring that starts at l and ends at n-1, and the left part (0..l-1) is all a. So possible l's are 0 and 1. But l can be 0 (remove [0..1], left part is empty) which is allowed (case2). For l=0: left part is empty, but case2 requires that the left part is all a. Which it is (empty is allowed?). No, because case2 is when the left part is non-empty. Or is it?

Wait, case2 is when the right part is empty. So the left part must be all same. But the left part can be empty. Wait no, because case2 is when the right part is empty (substring removed is from l to end). So the remaining part is 0 to l-1. Which can be empty (if l=0). But in that case, the remaining part is empty, which is allowed.

So in case2, the left part is 0..l-1, which is allowed to be empty. So the number of ways is prefix_len ways (l ranges from 0 to prefix_len-1). For the third example, prefix_len is 1. So case2 contributes 1 way (l can be 0). Removing [0..1] → left part is empty. Which is allowed, counted in case2.

So case1 is 2 (r=0 and r=1), case2 is 1 (l=0). So case1 + case2 = 3. But the entire string removal is counted in both case1 (r=1) and case2 (l=0). So subtract 1. So answer is 2+1-1=2. But the correct answer is 3. So this approach is also wrong.

Hmm, this is getting really confusing. Maybe I need to model it differently.

Alternative plan:

We can precompute the longest prefix of the same character (left_len) and the longest suffix of the same character (right_len). Let the first character be c_first and last be c_last.

Case 1: c_first != c_last.

In this case, the only valid ways are:

- Remove a substring that leaves a prefix of c_first (of length up to left_len).

- Remove a substring that leaves a suffix of c_last (of length up to right_len).

- Remove the entire string (counted once).

So for each possible prefix length i (0 <= i <= left_len), the number of ways to remove a substring that leaves a prefix of i characters is (n - i). For example, i=0: remove the entire string. For i=1: remove any substring starting at 1 (so the prefix is first character). The number of ways is n -i = 2-1=1 in the third example. So for i=1 in the third example, there's 1 way (removing substring [1..1], which leaves 'a').

Similarly for the suffix.

So the total ways when c_first != c_last is:

sum_{i=0}^{left_len} (n -i) + sum_{j=0}^{right_len} (n -j) - 1.

The -1 is because the entire string removal is counted in both sums (i=0 and j=0).

Let's test this in the third example:

left_len=1, right_len=1.

sum_i=0^1 (2 -i) → (2-0)+(2-1) =2 +1=3.

sum_j=0^1 (2-j) → same, 3.

Total 3+3-1=5. But correct answer is 3. So this approach is wrong.

But in the third example, the answer is 3. How?

The valid ways are:

1. Remove [1..1] → leaves 'a' → valid.

2. Remove [0..0] → leaves 'z' → valid.

3. Remove [0..1] → leaves empty → valid.

So three ways. According to the formula, sum_i=0 to 1 (2 -i) is 2+1=3 (prefix ways), sum_j=0 to 1 (2-j)=3 (suffix ways). 3+3-1=5, which is way too high.

So this approach is definitely incorrect.

Alternative Idea:

For the case when c_first and c_last are different, the valid ways are:

- Remove a substring that leaves a prefix of c_first (of length >=0). But the prefix must consist of all c_first. So the maximum possible prefix length is left_len. So the number of ways to leave a prefix of i characters (all c_first) is (n -i), where i can be from 0 to left_len. But wait, when i is 0, the entire string is removed, which is allowed.

Similarly for suffix.

So for the third example, sum_i=0 to 1 (2-i) → 2+1=3. sum_j=0 to 1 (2-j) →3. Total is 3+3-1=5. But the actual answer is 3. So this suggests that the formula is wrong.

What's wrong with the formula? Because when c_first and c_last are different, the entire string removal is counted once (i=0 and j=0) but the other ways in the sums may overlap. For example, the third example's valid ways include:

- i=0: entire string (counted once).

- i=1: prefix of 1 character. The ways are (n-i) =1 way (remove substring starting at 1). Which is removing [1..1], leaving 'a'.

- j=0: entire string (counted once).

- j=1: suffix of 1 character. The ways are (n-j)=1 way (removing substring ending at 0. So removing [0..0], leaving 'z'.

But according to the formula, sum_i=3 (i=0 and i=1) and sum_j=3 (j=0 and j=1). So sum_i + sum_j -1 =5. But the actual valid ways are 3.

So why is this discrepancy?

Ah, because when c_first and c_last are different, the ways to leave a prefix of i characters (i>0) are only possible if the entire prefix up to i is all c_first. Similarly for j>0. So for the third example:

sum_i (i=0 to 1) for prefix:

i=0: ways is (2-0)=2 → can remove substring starting at 0 and ending anywhere (but the remaining right part must be empty). For i=0, the prefix is empty, which is allowed. The ways are removing [0..0] (leaves 'z') and [0..1] (leaves empty). Wait, no. For i=0, the number of ways is (n -i) =2. Those ways are removing substrings starting at 0. So the substrings are [0..0] (removes 'a', leaving 'z') and [0..1] (removes 'az', leaving empty). So those are two ways. But in the actual answer, [0..1] is counted once as the entire string removal, which is part of both sums. 

Similarly, for i=1, the number of ways is (2-1) =1. That's removing substring starting at 1 (i=1) and ending at 1: removes 'z' (leaves 'a').

Sum for prefix is 2+1=3.

Sum for suffix:

j=0: ways is 2 (n-j=2). Removing substrings ending at n-j-1 =1. So substrings that end at 1 (the last character). So substrings are [0..1] (entire string) and [1..1]. Removing [0..1] leaves empty, which is allowed. Removing [1..1] leaves 'a' (but j=0 corresponds to removing the entire string, but the suffix is 'z' in this case. Wait, this is where the confusion lies.

Wait, for the suffix case, when j is 0, the remaining part is empty. For j=1, the remaining suffix is 1 character (z). So the ways are removing substrings that start at any l and end at n-j-1 =n-1 -j. For j=0: end at n-1-0 =1. So the substring must end at 1, and start anywhere from 0 to 1. So the possible substrings are [0..1], [1..1]. But for the suffix to be of j=0 characters (empty), the remaining part is empty, so removing those substrings is allowed. But in the case where j=1, the suffix is 1 character. So the substring to remove must end at 0 (since j=1: end at n-1-j =2-1-1=0). So for j=1, the substring must end at 0, and start anywhere from 0 to 0. So the only way is [0..0], which leaves 'z'.

So sum_j=0 to 1 (2-j) → j=0: 2 ways (substrings [0..1], [1..1]). j=1: 1 way (substring [0..0]). So sum_j=2+1=3.

But in reality, the valid ways for the suffix case are:

- j=0: two ways (entire string removal and [1..1] removal). But [1..1] removal leaves 'a', which is a prefix, not a suffix. Wait, no. Because for the suffix case, the remaining part must be all same as c_last (z in this example). So the suffix case j=1 would require that the remaining suffix is 'z' (j=1 character). But in the third example, the suffix is 'z', so j=1 is valid. So when j=1, the remaining suffix is 1 character 'z'. So the ways for j=1 are the substrings that start at 0 and end at 0 (removing 'a'), leaving 'z'. So that's one way. 

The case j=0 for suffix requires that the remaining suffix is empty. So any substring that ends at 1 (n-1) and starts anywhere from 0 to 1. Removing [0..1] leaves empty. Removing [1..1] leaves 'a', which is a prefix of 'a', which is part of the prefix case. So in the suffix case, j=0 allows any substring that ends at 1 and starts at any l. But the remaining suffix is empty, which is allowed. So for j=0, the two ways are:

- removing [0..1] → empty.

- removing [1..1] → 'a' (prefix).

But the remaining part for j=0 is empty, which is allowed. So those two ways are valid for the suffix case. But the second way ([1..1] removal) leaves 'a', which is part of the prefix case, but in the suffix case, the remaining part is empty, which is allowed. Wait, no. For the suffix case j=0, the remaining part is empty. But according to the case definition, the suffix case is when the remaining part is a suffix of c_last. But empty is allowed. So in the third example, the suffix case j=0 has two ways: removing [0..1] and [1..1]. But the latter leaves 'a', which is a prefix case, but how is it counted in the suffix case?

This is the problem. The formula is considering all possible substrings that leave a prefix of i characters (even if the remaining part is not a prefix of i characters). So when the substring is removed in such a way that the remaining part is a prefix of i characters (all c_first), the formula counts it. But when the substring is removed in a way that the remaining part is a prefix of i characters but also a suffix of j characters (like empty), the formula counts it in both sums. So this leads to overcounting.

This suggests that the initial approach is fundamentally flawed.

Alternative Idea: Let's think in terms of the two cases when the remaining string is all same character c. The ways can be:

1. The remaining string is empty (counted once).

2. The remaining string is non-empty and consists of c. This can be achieved in two ways:

   a. All characters are to the left of some position l (i.e., remove a substring starting at l and ending at the end). So the left part must be all c.

   b. All characters are to the right of some position r (i.e., remove a substring starting at the beginning and ending at r). The right part must be all c.

   c. The remaining string is a combination of a prefix and suffix of c, with a substring removed in between.

So, let's compute these possibilities.

The total number of valid ways is:

empty case (1) + case 2a (left parts) + case 2b (right parts) + case 2c (combinations).

But case 2c is only possible if the prefix and suffix characters are the same.

So:

if c_first != c_last:

total = 1 (empty) + left_non_empty (ways to leave a non-empty left part all c_first) + right_non_empty (ways to leave a non-empty right part all c_last).

else:

total = 1 + left_non_empty + right_non_empty + combinations (prefix and suffix).

Now, how to compute left_non_empty and right_non_empty.

left_non_empty: the number of ways to remove a substring that leaves a non-empty left part (all c_first). These are the ways to remove a substring starting at l and ending at the end (n-1). The left part is 0..l-1, which must be non-empty and all c_first. So l can range from 0 to (left_len -1), but l must be >=0 and l <= (left_len -1). So for each l in 0..left_len-1, the left part is 0..l-1 (which has length l, which is >=1 when l >=1). Wait, if l=0, the left part is empty. So to get a non-empty left part, l must be >=1. So the valid l's are 1..left_len-1. For each l, the substring to remove is [l..n-1]. The number of ways is left_len-1 (since l ranges from 1 to left_len-1). But wait, for example, left_len=1, then l can be 1..0, which is invalid. So left_non_empty is 0 if left_len <1. Which makes sense.

Similarly, right_non_empty: number of ways to remove a substring that leaves a non-empty right part (all c_last). These are substrings that start at 0 and end at r. The right part is r+1..n-1, which must be non-empty and all c_last. So r can range from (n - right_len) to (n-2). The number of such r's is right_len-1.

So for c_first != c_last:

total = 1 + (left_len -1) + (right_len -1) + 0.

But in the third example, left_len=1, right_len=1. So 1 +0 +0=1, but the answer is 3. So this is wrong.

Wait, the third example's valid ways are:

- Remove [0..0] → leaves 'z' → right_non_empty (right_len is 1, so right_non_empty is right_len-1=0 → not counted).

Hmm, this approach is not working.

Alternative Idea:

Let's try to think differently. For each possible valid remaining string, count how many ways to achieve it.

The remaining string must be all same character c. It can be empty.

So for each c in the possible characters, we need to find the number of ways to remove a substring such that the remaining string is all c or empty.

But since the entire string removal is allowed, which is counted once.

So, the total is:

sum_{c in all chars} (number of ways to leave non-empty string of c) + 1.

But how to compute this for each c.

For a character c, the non-empty remaining string can be:

1. A prefix of c's. The maximum possible prefix is m. So for each i in 1..m, the number of ways is (n -i). This is because the substring must start at i and end anywhere (i to n-1), which is (n-i) ways.

2. A suffix of c's. The maximum possible suffix is k. So for each j in 1..k, the number of ways is (n -j) ways.

3. A combination of prefix and suffix of c's. Only possible if the first and last characters are c. For this, the number of ways is (m-1) * (k-1), where m is the maximum prefix of c and k is the maximum suffix of c.

So for each c:

number of ways for c = sum_{i=1}^m (n-i) + sum_{j=1}^k (n-j) + (m-1)*(k-1) if first and last characters are c, else 0.

Then, add 1 for the entire string removal.

So the total is:

sum_c (sum_{i=1}^m (n-i) + sum_{j=1}^k (n-j) + overlap) ) + 1.

But this seems complicated.

Let's apply this to the first example.

First example: s=abaa (n=4).

Characters are a, b, a, a.

The possible c's are a and b.

For c=a:

max_prefix m is 1 (first character a).

sum_{i=1}^1 (4-1) =3.

max_suffix k=2 (last two a's).

sum_{j=1}^2 (4-1) + (4-2) →3+2=5.

overlap since first and last are a. (m-1)*(k-1) =0*1=0.

So for a: 3+5+0=8.

For c=b:

max_prefix is 0 (since first character is a).

sum_{i=1}^0 ... =0.

max_suffix is 0.

sum_{j=1}^0 ...=0.

overlap=0.

So total for c=a is 8, c=b is 0. Plus 1 for the entire string removal. Total 8+0+1=9. But the correct answer is 6. So this approach is incorrect.

Clearly, this approach is not working.

Another Idea: For the remaining string to be all the same, it must be either:

- All the same as the first character, and is a prefix.

- All the same as the last character, and is a suffix.

- A combination of some prefix and suffix of the same character.

So, the total ways are:

ways for first character (prefix) + ways for last character (suffix) + ways for combining prefix and suffix (if first and last are same) - overlapping ways (entire string removal).

But how to calculate each part.

For the first character (c_first):

The ways to have a non-empty prefix of c_first is sum_{i=1}^m (n-i), where m is the max prefix of c_first.

The ways to have a non-empty suffix of c_first is sum_{j=1}^k (n-j), where k is the max suffix of c_first (only if c_first == c_last).

The combination ways is (m-1) * (k-1), where m is the max prefix of c_first and k is the max suffix of c_first.

Similarly for c_last.

But this is getting too complicated.

Alternative Idea inspired by the sample input:

Let's look at the first sample input: 'abaa' (n=4).

The answer is 6. The valid ways are:

Removing substrings [1-2], [1-3], [1-4], [2-2], [2-3], [2-4].

So the remaining string after removal is either 'aa' or 'a' or 'a' (from prefix) or 'aa' (from suffix) or empty (removed entire string).

Wait, but in the sample explanation, the entire string removal is not listed as one of the valid ways. Oh no, wait in the first example, the sample input's output includes 6 ways. The explanation lists 6 ways, none of which is the entire string removal. Because the sample explanation lists the ways to remove substrings like [1;4], which is the entire string. So in that case, the entire string removal is allowed and counted as one way.

So why in the first example, the answer is 6? Let's count all valid ways.

The valid ways are:

1. Remove substring [1;2] (characters 'ab'): remaining 'aa' → valid.

2. Remove [1;3] ('aba'): remaining 'a' → valid.

3. Remove [1;4] (entire string): remaining empty → valid.

4. Remove [2;2] ('b'): remaining 'aaa' → valid.

5. Remove [2;3] ('ba'): remaining 'aa' → valid.

6. Remove [2;4] ('baa'): remaining 'a' → valid.

So total 6 ways.

So the entire string removal is counted once.

Now, according to this, the ways are:

- Cases where the remaining string is all 'a's.

These include:

- remove entire string (empty).

- remove 'b' (case 4).

- remove 'ab' (case1), leaves 'aa'.

- remove 'aba' (case2), leaves 'a'.

- remove 'ba' (case5), leaves 'aa'.

- remove 'baa' (case6), leaves 'a'.

So the ways are a combination of removing substrings that leave a prefix, suffix, or a combination.

So the problem is to find all possible substrings [l, r] such that the remaining characters (before l and after r) are all the same.

So the key is to find all possible [l, r] such that:

all characters before l are the same (c), all characters after r are the same (c), and c is the same for both.

Or, the remaining parts (before l and after r) are both empty.

So the approach is:

For each possible [l, r], check if the union of the left and right parts is all the same character.

But checking each possible substring is O(n^2), which is impossible for n=2e5.

Thus, we need an O(n) approach.

The optimal approach is to precompute the maximum prefix and suffix lengths, then compute the possible cases based on those.

So, the correct approach is:

- Compute left_len: the maximum number of leading characters equal to s[0].

- Compute right_len: the maximum number of trailing characters equal to s[-1].

- If s[0] != s[-1], then the answer is (left_len + right_len + 1). Because:

   The ways are:

   - Remove a substring that leaves a prefix of s[0]. The number of ways is left_len + 1 (i from 0 to left_len: sum (n -i) for i=0 is 4, but wait no. Wait, in the third example, when s[0] is 'a' and s[-1] is 'z', the answer is 3. left_len is 1, right_len is 1. So 1 +1 +1=3. Which matches the third example's output.

   - Remove a substring that leaves a suffix of s[-1]. The number of ways is right_len +1.

   - The entire string removal is counted in both, so we add 1 (left_len + right_len + 1).

Wait, no. For example, in the third example, left_len is 1, right_len is 1. The answer is 3. 1+1+1=3. So this formula works.

In the first case, when s[0] == s[-1], the answer is left_len + right_len + 1 + (left_len * right_len).

Let's see first example: s[0] is a, s[-1] is a. left_len is 1, right_len is 2. So 1 +2 +1 + (1*2) =1+2+1+2=6. Which matches the first example's output.

Second example: s is 'aacdeee' (n=7). The first character is 'a', last is 'e'. left_len=2, right_len=3. So answer is 2+3 +1 =6, which matches the sample.

Third example: 1+1+1=3. Correct.

So the formula is:

if s[0] != s[-1], answer is (left_len + right_len + 1).

if s[0] == s[-1], answer is (left_len + right_len + 1) + (left_len * right_len).

But why?

Because:

When s[0] != s[-1], the only valid ways are:

- Remove a substring that leaves a prefix of s[0] (left_len+1 ways).

- Remove a substring that leaves a suffix of s[-1] (right_len+1 ways).

- But these counts include the entire string removal in both. So the total is (left_len+1) + (right_len+1) -1 = left_len + right_len +1.

When s[0] == s[-1], the valid ways are:

- (left_len+1) + (right_len+1) -1 (for the entire string removal counted once).

- Plus the ways to remove a substring that includes the entire middle part (so that the remaining parts are some prefix of s[0] and some suffix of s[0], which are all the same character).

The number of such ways is left_len * right_len.

Thus, the total is (left_len + right_len + 1) + (left_len * right_len).

So this formula seems to fit all the examples.

Now, the task is to compute left_len and right_len.

This can be done in O(n) time.

For example, left_len is computed by iterating from the start until the characters are the same as s[0].

Similarly for right_len.

Once we have left_len and right_len, the answer can be computed using the formula.

So, the steps are:

1. Read n and s.

2. Compute left_len: maximum number of consecutive s[0] at the start.

3. Compute right_len: maximum number of consecutive s[-1] at the end.

4. If s[0] != s[-1], then answer is (left_len + right_len + 1) mod 998244353.

5. Else, answer is (left_len + right_len + 1 + left_len * right_len) mod 998244353.

Wait, let's test this:

First example:

left_len=1, right_len=2. s[0] == s[-1]. So 1+2+1 +1*2 =6 → correct.

Second example: s[0] is 'a', s[-1] is 'e' → different. left_len=2, right_len=3. So 2+3+1=6 → correct.

Third example: left_len=1, right_len=1, different. 1+1+1=3 → correct.

Another test case: if the entire string is "aaaa", but the problem says it's guaranteed that there are at least two different characters. So that case is impossible.

Another test case: s="aabbaaa". s[0] is 'a', s[-1] is 'a'. left_len=2, right_len=3. So answer is 2+3+1 +2*3= 6 +6=12.

But what are the valid ways?

The valid ways include:

- Removing any prefix of 0..i (i ranges from 0 to 2). For example, removing the entire string (i=0, but left_len=2 → i ranges from 0 to 2. So sum is (n -i) for i=0,1,2 → 7-0=7, 7-1=6, 7-2=5. Sum is 7+6+5=18.

- Removing any suffix of j=0,1,2,3. sum is 7-0=7,7-1=6,7-2=5,7-3=4. Sum 7+6+5+4=22.

- The entire string removal is counted once.

- The combination ways are left_len * right_len = 2*3=6.

So the total according to the formula is 2+3+1 +6 =12.

But according to the previous approach, the answer is 12. But according to the sum of prefix and suffix ways minus 1 plus combination, it's (2+3+1) +6=6+6=12. So yes.

But what is the actual count?

The string is "aabbaaa". So s[0] is 'a', s[1] is 'a', s[2] 'b', s[3] 'b', s[4] 'a', s[5] 'a', s[6] 'a'.

left_len=2 (first two 'a's).

right_len=3 (last three 'a's).

The formula gives 2+3+1 + 2*3=12.

The valid ways would include:

- All ways to remove a prefix of 'a's (i=0,1,2 →3 ways).

But according to the formula, when s[0] == s[-1], the answer is left_len + right_len + 1 + left_len*right_len =2+3+1+6=12.

So the formula seems to work.

Thus, the correct approach is to compute left_len and right_len, and apply the formula based on whether the first and last characters are the same.

So the code would be:

Read n, s.

Compute left_len: iterate from start until characters are s[0].

Compute right_len: iterate from end until characters are s[-1].

If s[0] != s[-1], answer is (left_len + right_len + 1) mod MOD.

Else, answer is (left_len + right_len + 1 + left_len * right_len) mod MOD.

But wait, why add 1?

In the case where s[0] and s[-1] are different, the formula is left_len + right_len + 1. But according to the third example, left_len and right_len are 1 each, which sums to 3. Which is correct.

But in the formula, when they are different, it's left_len + right_len +1. Because the total ways are:

left_len+1 (prefix ways, including i=0) + right_len+1 (suffix ways, including j=0) -1 (overlap of entire string).

But left_len+1 + right_len+1 -1 = left_len + right_len +1.

Yes.

So the code should implement this.

Let's test this with the first example:

n=4, s=abaa.

left_len=1 (first 'a').

right_len=2 (last two 'a's).

s[0] == s[-1], so answer is 1+2+1 +1*2 =6. Correct.

Another test case: n=2, s=az.

left_len=1, right_len=1.

answer is 1+1+1=3. Correct.

Another test case: n=7, s=aacdeee.

s[0] is 'a', s[-1] is 'e'.

left_len=2 (aa at start), right_len=3 (eee at end).

answer is 2+3+1=6. Correct.

Thus, the code should be straightforward.

Now, implement this in Python.

The code steps:

1. Read n and s.

2. Compute left_len:

left_len = 0

while left_len < n and s[left_len] == s[0]:

    left_len +=1

But wait, no. Because left_len is the maximum number of consecutive s[0] from the start. For example, in 'aabbaaa', the first two characters are 'a's, so left_len is 2.

So code:

left_len = 1

for i in range(1, n):

    if s[i] == s[0]:

        left_len +=1

    else:

        break

Similarly for right_len:

right_len =1

for i in range(n-2, -1, -1):

    if s[i] == s[-1]:

        right_len +=1

    else:

        break

3. Check if s[0] == s[-1].

If yes: answer is (left_len + right_len + 1 + left_len * right_len) mod MOD.

Else: answer is (left_len + right_len + 1) mod MOD.

Yes.

So the code would be:

MOD = 998244353

n = int(input())

s = input().strip()

if n ==0:

    print(0)

else:

    c_first = s[0]

    c_last = s[-1]

    left_len = 1

    for i in range(1, n):

        if s[i] == c_first:

            left_len +=1

        else:

            break

    right_len =1

    for i in range(n-2, -1, -1):

        if s[i] == c_last:

            right_len +=1

        else:

            break

    if c_first != c_last:

        ans = (left_len + right_len +1) % MOD

    else:

        ans = (left_len + right_len +1 + left_len * right_len) % MOD

    print(ans)

But wait, in the case where the entire string is the same character, but the problem states that there are at least two different characters, so left_len and right_len won't cover the entire string. So no problem.

Let's test this code with the first example:

Input:

4

abaa

left_len: first character is 'a'. s[0] is 'a', s[1] is 'b' → loop breaks. So left_len=1.

right_len: last character is 'a'. s[3] is 'a', s[2] is 'a' (i=2). Then i=1, which is 'b' → break. So right_len=2.

c_first == c_last. ans =1+2+1 +1*2=6 → correct.

Third example:

2

az

left_len=1 (only 'a').

right_len=1 (only 'z').

ans=1+1+1=3 → correct.

Second example:

7

aacdeee

c_first is 'a', c_last is 'e'. left_len=2, right_len=3.

ans=2+3+1=6 → correct.

Another test case: n=3, s='aba'. left_len=1, right_len=1. c_first is 'a', c_last is 'a. So ans=1+1+1 +1*1= 4. What are the valid ways?

The string is 'aba'. The valid ways are:

1. Remove entire string.

2. Remove 'b' → 'aa' → valid.

3. Remove 'ab' → 'a'.

4. Remove 'ba' → 'a'.

5. Remove 'a' (prefix) → 'ba' → invalid.

Wait, no. Let's think:

The valid ways are those where the remaining characters are all 'a', 'a', or empty.

Possible ways:

- Remove [0..0] → 'ba' → not valid.

- Remove [0..1] → 'a' → valid.

- Remove [0..2] → empty → valid.

- Remove [1..1] → 'aa' → valid.

- Remove [1..2] → 'a' → valid.

- Remove [2..2] → 'ab' → invalid.

So valid ways are: [0..1], [0..2], [1..1], [1..2]. So 4 ways. Which matches the formula's answer of 4.

So the code works.
</think>

```python
MOD = 998244353
n = int(input())
s = input().strip()

if n == 0:
    print(0)
    exit()

c_first = s[0]
c_last = s[-1]

left_len = 1
for i in range(1, n):
    if s[i] == c_first:
        left_len += 1
    else:
        break

right_len = 1
for i in range(n-2, -1, -1):
    if s[i] == c_last:
        right_len += 1
    else:
        break

if c_first != c_last:
    ans = (left_len + right_len + 1) % MOD
else:
    ans = (left_len + right_len + 1 + left_len * right_len) % MOD

print(ans)
```