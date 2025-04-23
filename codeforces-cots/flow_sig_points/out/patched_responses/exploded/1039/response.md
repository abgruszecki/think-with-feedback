<think>
Okay, let's try to figure out this problem. The task is to find the number of beautiful submatrices in a given matrix. A beautiful submatrix is one where, after reordering each row independently, every row and every column of the submatrix becomes a palindrome. 

Hmm. So first, I need to understand the conditions for a submatrix to be beautiful. Let's break it down. For each row in the submatrix, after reordering, the row must be a palindrome. Similarly, each column in the submatrix, after the rows are reordered, must also be a palindrome. 

Wait, but the columns are determined after the rows are reordered. So the way we arrange each row affects the columns. But since each row is rearranged independently, how do the columns end up being palindromes?

Wait, the rows can be reordered in any way, but once they are reordered, the columns must form palindromes. So, for the columns to be palindromes, each column must have the same set of characters when read top to bottom as when read bottom to top. But since each row is reordered, the columns are formed by taking the j-th element of each row (after reordering). 

Wait, but each row is reordered. So for example, a row might be "abc" and we can reorder it as "acb". Then, when looking at the columns, each column's characters are taken from the reordered rows. 

So the key point is that after rearranging each row's characters, the entire submatrix's rows and columns must be palindromes. 

But what's the condition for that? Let's think about the rows first. Each row, after rearrangement, must be a palindrome. So for each row, the count of each character must allow forming a palindrome. For a string to be a palindrome, all characters except possibly one (the middle one in odd length) must have even counts. 

Wait, no. Wait, the row can be rearranged into a palindrome. So for a row of even length, all character counts must be even. For a row of odd length, exactly one character has an odd count. 

But when you reorder the row to form a palindrome, the counts must satisfy that. So for a row of length L, the counts of each character must allow forming a palindrome. 

But for the rows, since they can be reordered, each row must have a multiset of characters that can form a palindrome. Then, for the columns, each column must also form a palindrome after the rows are reordered. 

But the columns are sequences of characters from each row (after their own reordering). So each column must be a palindrome. But how can that happen when each row is arranged in a way that allows their own row to be a palindrome?

Hmm. Let's think: For a column to be a palindrome, the i-th row from the top and the i-th row from the bottom (within the submatrix) must have the same character in that column. Because the column must read the same forwards and backwards. So for each column in the submatrix, the first and last elements must be the same, the second and second last must be the same, etc. 

But since the rows are reordered, the arrangement of characters in each row can be done in a way that allows this. But the columns are determined after the rows are reordered, so how can the columns form a palindrome?

Wait, perhaps each column in the submatrix must have all elements even, except possibly one in the middle (if the number of rows is odd). But that's for the column to be a palindrome. But the way the rows are arranged affects the column's characters. 

Alternatively, maybe for the entire submatrix to be beautiful, the following conditions must hold:

For every row in the submatrix, the multiset of characters in that row can form a palindrome (so it meets the even-odd count condition based on the row's length). 

Additionally, for each column in the submatrix, when considering the multiset of characters from all the rows in that column, they must be able to form a palindrome (but the column's length is the number of rows in the submatrix). 

Wait, but the column's characters are the j-th elements of each row after reordering. So the columns are sequences formed by the rows' arrangements. For a column to be a palindrome, each pair of rows symmetric around the center of the column must have the same character. 

Wait, for example, if the submatrix has k rows, then in the column, the first row must equal the k-th row, the second must equal the (k-1)-th, etc. 

So for each column in the submatrix, the j-th element of row i (after reordering) must equal the j-th element of row (k - i + 1), where k is the number of rows in the submatrix. 

But since each row can be reordered, perhaps the columns can be adjusted to meet this condition. 

Wait, but how? Because each row is reordered, but the arrangement of the rows' elements must be such that for each column position, the elements in symmetric rows are the same. 

So perhaps the key idea is that for a submatrix to be beautiful, all rows in the submatrix can be arranged into palindromes, and for every pair of rows symmetric around the center of the submatrix (like row i and row k - i + 1 in a k-row submatrix), the multiset of characters in those two rows must be identical. Because then, when you arrange each row into a palindrome, you can mirror their arrangements so that each column is the same as its symmetric counterpart, thus making the column a palindrome. 

Wait, that might make sense. Let's think: if the submatrix has an even number of rows. Then, each pair of rows (i and k-i+1) must have the same multiset of characters. Then, when each row is arranged as a palindrome, the columns can be mirrored. For example, the first row's arrangement is the reverse of the second row's arrangement. Then, each column would have the same first and second elements. 

Similarly, for an odd number of rows, the middle row can have any arrangement (as a palindrome), and the other rows must be paired with their symmetric counterparts. 

So the conditions for a submatrix to be beautiful are:

1. For each row in the submatrix, the character counts allow the row to be a palindrome (i.e., the row's length is even and all counts even, or length is odd and exactly one count is odd).

2. The multiset of characters for each pair of rows symmetric around the center of the submatrix are the same. 

If both conditions are met, then the submatrix is beautiful. 

Wait, but what about the columns? For example, suppose the submatrix has two rows. Then, the two rows must have the same multiset of characters. Then, when arranged as palindromes, they can be arranged such that each row is a palindrome, and the two rows are mirrored. For example, row 1 is arranged as "abba", row 2 as "abba", then each column (a,a), (b,b), (b,b), (a,a) would be palindromes. 

So the key is that the multiset for rows in symmetric pairs must be equal. Then, each column would have the same characters in each symmetric pair, thus forming a palindrome. 

So the approach is:

For any submatrix (i1, j1, i2, j2), check:

- Each row in [i1, i2] can be rearranged into a palindrome (based on the row's length in the submatrix, which is j2 - j1 + 1).

- For each pair of rows symmetric around the vertical center of the submatrix, the multiset of characters in those rows (but in the submatrix's columns) must be equal. 

Wait, but the submatrix's columns are j1 to j2. So for each row in the submatrix, we need to look at the characters in columns j1 to j2. 

Wait, the original problem statement defines a submatrix as a rectangle in the original matrix. So the rows in the submatrix are from i1 to i2 (inclusive), and columns j1 to j2 (inclusive). 

Each row in the submatrix is a substring from j1 to j2. So for each row in the original matrix (row r), the part from j1 to j2 is considered for the submatrix. 

So for a submatrix (i1, j1, i2, j2), each row r (from i1 to i2) has a substring from j1 to j2. 

Then, for the rows in the submatrix to be reordered into palindromes, each of these substrings (the part in j1 to j2 of row r) must have a multiset that can form a palindrome. 

Additionally, the rows in symmetric positions within the submatrix must have the same multiset. 

So the steps are:

1. Precompute for each possible row r and each possible column range (j1, j2) the multiset of characters in row r's columns j1 to j2. Then, check if that multiset can form a palindrome (i.e., satisfies the even/odd condition based on the length (j2 - j1 + 1)). Also, compute a "hash" or signature that represents the multiset. 

2. For any possible submatrix (i1, j1, i2, j2), check two conditions:

   a. For each row in i1 to i2, the j1-j2 substring of the row can form a palindrome. 

   b. For each pair of rows symmetric in the vertical direction (i.e., row i and i2 - (i - i1)), the signatures of their j1-j2 substrings must be equal. 

If both conditions are met, then the submatrix is beautiful. 

Now, the problem is to count all possible (i1, j1, i2, j2) such that these conditions are satisfied. 

But how to compute this efficiently, given that n and m are up to 250? 

The total number of possible submatrices is O(n^2 * m^2) which for 250 is 250^4 = about 4e9, which is way too big. So we need a smarter approach. 

So the key is to find a way to efficiently check these conditions for all possible submatrices. 

Let's think about how to approach this. 

First, for each possible j1 and j2 (columns), we can precompute for each row r whether the substring from j1 to j2 in row r can form a palindrome (condition 1a). 

Then, for a given j1 and j2, the problem reduces to finding all vertical ranges (i1, i2) such that:

- For all rows in i1 to i2, the j1-j2 substring can form a palindrome. 

- For each pair of rows symmetric around the vertical center of the i1-i2 range, their j1-j2 substrings have the same multiset. 

So for each j1 and j2, we can process all possible column ranges (j1, j2) and then for each such range, process all possible vertical ranges (i1, i2) that are valid. 

But how? Let's think about j1 and j2. There are O(m^2) possible j1 and j2. For each such pair, we can precompute for each row r a binary flag indicating whether the j1-j2 substring can form a palindrome. Then, for each row r, the flag is 1 if the substring can form a palindrome, else 0. 

Then, for each j1, j2, we have a list of rows where the flag is 1. Then, for each possible vertical range (i1, i2) where all rows from i1 to i2 have flag 1, we need to check the symmetry condition. 

But even this is O(m^2 * n^2), which for 250 is 250^4 = 3.9e9 operations. That's way too slow. 

Hmm. So we need a way to count the number of vertical ranges (i1, i2) where:

- All rows in i1 to i2 have the substring j1-j2 that can form a palindrome. 

- The multiset of the substring j1-j2 for each row i in i1 to i2 is symmetric, i.e., the i-th row from the bottom (i1) and the i-th row from the top (i2) have the same multiset. 

Wait, but how can we model the symmetry condition? 

The symmetry condition is that for the vertical range i1 to i2, each row at position k (relative to the vertical range) must have the same multiset as the row at position (i2 - (k - i1)). For example, in a vertical range of 3 rows (i1, i1+1, i1+2), the first and third rows must have the same multiset, the middle row can be any. 

So for the vertical range to be symmetric, the multiset array must form a palindrome. 

So for a given j1 and j2, and considering a vertical range i1 to i2, the multiset signatures of the rows in this vertical range must form a palindrome. 

Thus, the problem reduces to, for each possible j1, j2, find the number of vertical ranges (i1, i2) where:

1. All rows in i1 to i2 have their j1-j2 substring can form a palindrome (so the flag is 1 for each row). 

2. The array of multiset signatures for the rows in i1 to i2 forms a palindrome. 

So for each j1, j2, we need to count all palindromic subarrays in the array of multiset signatures (for that j1, j2), considering only the rows where the flag is 1. 

But how can we compute this efficiently? 

Calculating the number of palindromic subarrays in an array can be done using Manacher's algorithm for each possible center, but that's O(n) per j1, j2. 

But with m^2 possible j1, j2, that's O(m^2 * n) time, which for m=250 is 250^2 * 250 = ~15 million operations. That's manageable. 

So here's the plan:

1. Precompute for each row r and for each possible j1, j2 (j1 <= j2), whether the substring from j1 to j2 can form a palindrome. Also precompute the multiset signature for each substring. 

But how to compute the multiset signature efficiently? 

Wait, the multiset can be represented by the count of each character. Since there are 26 lowercase letters, perhaps we can compute a 26-element array, or a bitmask that represents parity of counts (but that's only for the even-odd case, which may not be sufficient). Wait, no. For the symmetry condition, the exact counts matter, not just their parity. Because two rows can have the same multiset (same counts for all characters) only if their exact counts match. 

So the signature for a substring j1-j2 of row r is a tuple (count_a, count_b, ..., count_z). But storing this for all possible j1, j2 for all rows is memory-intensive. For example, each row has O(m^2) possible j1, j2 pairs. For 250 rows, that's 250 * 250^2 = 15,625,000 entries. Each entry is 26 integers (counts), but maybe we can hash them. 

Alternatively, we can precompute a hash for each (r, j1, j2) that uniquely represents the multiset of the substring. 

To compute the counts efficiently, we can use prefix sums for each row and each character. For each row r, we can compute prefix[r][c][j] = number of times character c appears in row r up to column j. Then, for substring j1-j2 in row r, the count for character c is prefix[r][c][j2] - prefix[r][c][j1-1]. 

This allows O(1) access to the count of any character in any substring. 

So for each row r and j1 <= j2, the signature can be computed as a tuple of counts for each character. Then, we can hash this tuple into a unique value (like a number) to use as a signature. 

But storing the counts as a tuple for each (r, j1, j2) is memory-heavy. For 250 rows and 250 columns, each row has 250*251/2 = 31375 possible (j1, j2) pairs. For each, a 26-element tuple is stored, which is 26 * 4 bytes per element (assuming integers), which is 104 bytes per entry. For 250 rows, 31375 * 250 * 104 bytes = about 790MB, which is over the memory limit. So this approach is not feasible. 

Alternative idea: For each row r, precompute the prefix sums for each character, then for a given j1 and j2, compute the counts on the fly. 

So when processing a j1 and j2, for each row r, compute the counts for characters in j1-j2. Then, check if the counts can form a palindrome (for that row's substring length) and compute the signature. 

But how to do this efficiently. 

The steps for each j1 and j2:

For j1 from 1 to m:

   for j2 from j1 to m:

      for each row r:

         compute the counts of each character in columns j1-1 to j2-1 (assuming 0-based or 1-based, need to adjust indices)

         check if the counts can form a palindrome (i.e., at most one character has an odd count if the length is odd, all even if even)

         compute the signature (hash of the counts)

      collect all rows where the palindrome condition is satisfied (flag is 1)

      then, for the array of signatures of these rows, compute the number of palindromic subarrays where the signature array is a palindrome

But even this approach has a problem: for each j1 and j2, processing each row takes O(26) time (for 26 characters). For j1 and j2 up to 250, this is 250 * 250 * 250 * 26 = 40,625,000 operations, which is acceptable. 

Then, for each j1, j2 pair, we need to process all rows and collect their signatures and flags. Then, for the array of signatures (filtering only rows where the flag is 1), we need to find the number of palindromic subarrays. 

But even that, for each j1, j2, the array is of size n (250), and we can compute the number of palindromic subarrays in O(n) time. 

Wait, but how to compute the number of palindromic subarrays in an array of size n efficiently. 

A palindromic subarray is a contiguous sequence of elements that form a palindrome. The number of such subarrays is the sum for each possible center (for odd length) and each possible center between elements (even length) of the maximum expansion possible where the elements mirror around the center. 

But Manacher's algorithm can find all palindromic substrings in O(n) time. But in this case, the array elements are the signatures (which are unique if the counts are different). So two elements are considered equal only if their signatures are the same. 

So the problem reduces to finding all contiguous subarrays (i1, i2) where the sequence of signatures from i1 to i2 is a palindrome. 

But this is equivalent to the subarray being a palindrome. For example, if the array is [a, b, a], then the entire array is a palindrome. 

But how can we count all such palindromic subarrays efficiently? 

An O(n^2) approach would be to check each possible subarray whether it's a palindrome. For each possible center, expand as much as possible. But for n=250, this would be O(n^2) per j1, j2, which for m=250 gives O(m^2 * n^2) = 250^4 = 3.9e9 operations. That's way too slow. 

Alternative idea: For each j1, j2 pair, we can precompute the array of valid rows (flag=1), and their signatures. Then, for this array of signatures, the number of palindromic subarrays is the sum over all possible i1 and i2 where the subarray is a palindrome. 

But how to compute this quickly. 

Another approach is to note that a palindromic subarray must have a mirror structure. So for each position in the array, we can check for even and odd length palindromes centered there. 

For each center, expand outwards as long as the left and right elements are equal. For each expansion, increment the count. 

But this is O(n^2) per j1, j2. For m=250, this would be O(m^2 * n^2) = 250^4 = 3.9e9 operations. Which is too slow. 

Hmm. So perhaps we need a smarter way. 

Wait, but the problem is that for each j1, j2, the array of valid rows (those that can form a palindrome for j1-j2) may be sparse. For example, some j1, j2 pairs might have very few valid rows, leading to fewer palindromic subarrays to check. 

But even that, in the worst case, this approach is O(n^2 * m^2), which is not feasible. 

Alternative idea: For each possible vertical range (i1, i2), precompute all j1, j2 pairs such that for this vertical range, the conditions are met. But I don't see how this would be easier. 

Alternative approach: Let's think of the problem in terms of the vertical ranges. For each possible i1 and i2 (vertical range), determine the maximum possible j1 and j2 such that:

- For all rows in i1 to i2, the substring j1-j2 can form a palindrome. 

- The signatures of the rows form a palindromic array. 

But this seems even more challenging. 

Another angle: For the submatrix to be beautiful, the vertical range must form a palindromic array of signatures (for the given j1, j2), and all rows must be valid (can form a palindrome). 

But how can we model the palindromic array of signatures? 

Another observation: The vertical range must be a palindrome in terms of the signatures. So for a vertical range [i1, i2], the array of signatures for rows i1 to i2 must be a palindrome. 

Thus, the problem for each j1, j2 is to count the number of palindromic subarrays in the array of signatures (for that j1, j2), but only considering rows where the substring j1-j2 is valid. 

So, the steps are:

For each j1 and j2:

   1. Precompute for each row r whether the j1-j2 substring can form a palindrome (valid[r] = True or False).

   2. For the rows where valid[r] is True, collect their signatures (counts of each character in j1-j2 substring).

   3. For this array of signatures, count the number of palindromic subarrays. 

But even this, the third step is O(n^2) per j1, j2. 

Wait, but maybe we can precompute for each possible vertical range (i1, i2) whether the signature array is a palindrome and all rows are valid. 

But again, it's O(n^2) per j1, j2. 

Alternative Idea: The signature of a row's j1-j2 substring is a 26-element array. To check if a vertical range is a palindrome, we can precompute for each possible vertical range (i1, i2) the hash of the concatenated signatures, and see if it's the same forwards and backwards. 

But even so, for each j1, j2, the number of vertical ranges is O(n^2), which again is too slow. 

Hmm. So perhaps we need to find another way to model the problem. Let's think again about the symmetry condition. 

The vertical range must be such that the i-th row in the range and the (k - i + 1)-th row (where k is the length of the range) have the same signature. 

So for example, a vertical range of length 3 (rows i1, i1+1, i1+2) must have the same signature for i1 and i1+2, and the middle row can be any. 

So the vertical range's signature array must be a palindrome. 

Thus, the number of valid vertical ranges for a given j1, j2 is equal to the number of palindromic subarrays in the array of valid signatures (where each row is valid). 

Now, the problem is how to efficiently compute the number of palindromic subarrays in the array of signatures (after filtering out invalid rows). 

But even here, the standard way to count palindromic substrings is O(n^2), which is too slow. 

Wait, but perhaps we can model the palindromic subarrays in a way that leverages the fact that the entire array is built from valid rows. 

Wait, but even for a j1, j2 pair, the valid rows are a subset of all rows. For example, some rows might not be valid for this j1, j2 pair. So the array of signatures for valid rows is not necessarily contiguous. 

Wait, no. The valid rows are all rows where the substring j1-j2 can form a palindrome. So for a given j1, j2, some rows are valid and others are not. But the vertical ranges must consist of consecutive valid rows. Wait no: the vertical range can include any rows between i1 and i2, but all of them must be valid. 

So, for a vertical range (i1, i2), all rows i1 to i2 must be valid (i.e., their j1-j2 substring can form a palindrome), and the signatures of rows i1 to i2 must form a palindrome. 

Thus, the problem for each j1, j2 is to process the array of valid rows (all rows where the j1-j2 substring is valid) and count the number of palindromic subarrays. 

But how to handle non-consecutive valid rows? For example, if rows 1 and 3 are valid for j1, j2, but row 2 is invalid, then a vertical range (1,3) is invalid because row 2 is invalid. 

So, for each j1, j2, the valid rows are a subset of all rows (those where valid[r] is True). Then, the vertical ranges (i1, i2) can only consist of consecutive rows where all rows between i1 and i2 are valid, and the signature array from i1 to i2 is a palindrome. 

Thus, for each j1, j2, the valid vertical ranges are those where all rows in i1 to i2 are valid, and the signatures form a palindrome. 

So for each j1, j2, the steps are:

1. Precompute for each row whether it's valid. 

2. Precompute the array of signatures for valid rows. 

3. For this array, count the number of palindromic subarrays. 

But the array is not contiguous. For example, the valid rows may be spread out. 

Wait no. Because a vertical range (i1, i2) must have all rows from i1 to i2 valid. So the valid vertical ranges are those where all rows in i1 to i2 are valid, and the signature array for i1 to i2 is a palindrome. 

Thus, for each j1, j2, the valid vertical ranges are those i1, i2 where i1 <= i2, and for every row r in i1 to i2, valid[r] is True, and the signature array for rows i1 to i2 is a palindrome. 

So for each j1, j2, we need to find all possible i1, i2 such that:

- All rows from i1 to i2 are valid (valid[r] is True for each r in i1..i2)

- The signature array of rows i1..i2 is a palindrome. 

Thus, the problem reduces to, for each j1, j2, generate a list of valid intervals (i1, i2) where all rows are valid, and the signature array is a palindrome. 

So how to compute this efficiently. 

An alternative approach: For each j1, j2, generate a list of valid intervals where all rows are valid. Then, for each such interval, check if the signature array is a palindrome and count it. 

But generating all valid intervals is O(n^2) per j1, j2. 

Hmm. Let's think about the possible j1, j2 pairs. 

For j1 and j2, there are m*(m+1)/2 = O(m²) possible pairs. 

For each pair, the processing steps are:

1. For each row r, compute if it's valid (O(26) per row). 

   Time: O(n * 26) per j1, j2.

2. Compute the signature for each valid row (O(26) per row). 

   Time: O(n * 26) per j1, j2.

3. For the valid rows, compute the number of palindromic intervals. 

   For example, the valid rows are contiguous ranges. Or maybe not. 

Wait, the valid rows can be any subset of the rows. For example, rows 1,3,5 are valid. Then, the valid intervals are (1,1), (3,3), (5,5), (1,3) (if all rows 1-3 are valid?), etc. 

But no. For an interval (i1, i2) to be valid, all rows from i1 to i2 must be valid. So for example, if rows 1,3 are valid but row 2 is not, then the interval (1,3) is invalid. 

Thus, the valid intervals are those where i1 to i2 is a contiguous range of valid rows. 

Wait, no. For example, if rows 1,2,3 are all valid, then (1,3) is valid. But if row 2 is invalid, then (1,3) is invalid. 

So the valid intervals are the intervals where all rows between i1 and i2 are valid. 

So, for each j1, j2, the valid rows are a set of indices. The valid intervals are the maximal consecutive sequences of valid rows, and any sub-intervals within them. 

For example, if rows 1, 2, 3, 5, 6 are valid, then the maximal valid intervals are [1-3], [5-6]. 

Within each maximal interval, all possible sub-intervals (i1, i2) where i1 <= i2 and i1 and i2 are within the maximal interval are valid. 

So for each maximal interval of length L, the number of valid intervals is L*(L+1)/2. 

But in addition to that, each valid interval must have a signature array that is a palindrome. 

So the approach is:

For each j1, j2:

   a. Compute which rows are valid. 

   b. Split the rows into maximal intervals of consecutive valid rows. 

   c. For each such maximal interval, compute the number of palindromic subarrays within it. 

But how to compute the number of palindromic subarrays within a contiguous array of valid rows. 

For example, consider a maximal interval of valid rows with indices [a, b] (row a, a+1, ..., b are valid). For this interval, the signature array is the list of signatures for each row in a to b. 

We need to count the number of subarrays of this signature array that are palindromic. 

So for each such maximal interval of consecutive valid rows, compute the number of palindromic subarrays in the signature array. 

The total count for j1, j2 is the sum over all maximal intervals of the count of palindromic subarrays within them. 

Now, the problem reduces to, for a given array of signatures (from a to b), count the number of palindromic subarrays. 

But how to do this efficiently. 

The standard approach for counting palindromic substrings is O(n²), which for n=250 would be 250² = 62,500 operations per j1, j2. For 250² j1, j2 pairs, this would be 250^4 = 3.9e9 operations, which is way too slow. 

But given that the time limit is 1.5 seconds, which is about 1e8 operations, this approach is not feasible. 

So we need a smarter way. 

Alternative Idea: Precompute for each possible j1, j2 pair and each possible vertical range (i1, i2) whether the conditions are met, and sum up. 

But that's O(n^2 * m^2) which is not feasible. 

Alternative Idea: Find that for a vertical range (i1, i2) to be valid, the signatures must form a palindrome. So the array of signatures must be a palindrome. 

But how to precompute for all possible vertical ranges (i1, i2) whether their signatures for j1, j2 form a palindrome. 

But even if we could compute this for all possible j1, j2, i1, i2, it's not clear how to do it efficiently. 

Alternative Idea: For each row r, precompute all possible j1, j2 pairs where the substring j1-j2 can form a palindrome, and their signature. Then, for each possible vertical range (i1, i2), check if all rows are valid for j1, j2, and their signatures form a palindrome. 

But again, this doesn't seem to help with the time complexity. 

Alternative Idea: The key insight is that the vertical ranges must have their signatures form a palindrome, which implies that the array of signatures is the same forwards and backwards. 

Thus, for each possible j1, j2 and vertical range (i1, i2), the signature array from i1 to i2 must be a palindrome. 

But how to model this. 

Another Idea: For each possible j1, j2 and vertical range (i1, i2), the number of palindromic vertical ranges is equal to the number of pairs (i1, i2) where the signature array is a palindrome and all rows are valid. 

But the problem is how to find these pairs (i1, i2) efficiently. 

Alternative Idea: For each j1, j2, precompute the signature for each valid row, and then precompute the palindrome status of each possible vertical range. Then, count all such ranges. 

But this is again O(n^2) per j1, j2. 

Hmm. Maybe the time constraints are manageable. Let's compute the worst-case time. 

Each j1, j2 pair has:

   For each row, compute valid and signature: O(n * 26) 

   For the array of signatures, process each possible vertical range (i1, i2) and check if it's a palindrome. 

The second part is O(n²) per j1, j2. 

So total time is O(m² * n²) + O(m² * n * 26). 

For m=250, n=250: 

m² * n² = 250^4 = 390,625,000 

m² * n * 26 = 250^2 * 250 * 26 = 406,250,000 

Total operations: ~796 million. 

This is way too slow for 1.5 seconds. 

So we need a smarter way. 

Alternative Idea: For each row and j1, j2, precompute the valid and signature. Then, for each j1, j2, compute a hash for each row's signature. Then, for vertical ranges, check if the hash of the first half equals the reversed hash of the second half. 

But again, for each vertical range, this is O(n) time per check. 

Alternative Idea: Find that the vertical range must be a palindrome, so for each possible center, expand around it to find all possible palindromic vertical ranges. 

This is similar to Manacher's algorithm. 

But how to apply this here. 

For each j1, j2, the valid rows are those where the substring is valid. 

For each j1, j2:

   Generate the list of valid rows. 

   For each valid row, compute the signature. 

   Then, find all palindromic subarrays in this list. 

   The count is the sum of all such palindromic subarrays. 

But how to do this efficiently. 

Manacher's algorithm can find all palindromic substrings in O(n) time. But the palindromic substrings are contiguous. 

Wait, but the palindromic subarrays here are contiguous sequences of signatures that form a palindrome. 

So for example, the list of signatures could be [A, B, A], which is a palindrome. 

So Manacher's algorithm can be adapted to count the number of palindromic substrings in O(n) time per j1, j2. 

Yes! Because the problem is now reduced to, for each j1, j2, and the array of signatures of valid rows, find the number of palindromic substrings (contiguous sequences that form a palindrome). 

The number of such substrings is the sum for each possible center (for even and odd lengths) of the maximum possible expansion. 

This approach is O(n) per j1, j2. 

So for each j1, j2, the steps are:

1. For each row r, compute if valid[r] for j1, j2. 

2. Collect the signatures of valid rows in an array S. 

3. For array S, compute the number of palindromic substrings (contiguous subarrays that are palindromes). 

4. Sum this count over all j1, j2. 

But wait, no. Because the valid vertical ranges are those where all rows in i1 to i2 are valid. So the array S is exactly the list of valid rows. For example, if the valid rows are 1,3,5, then the array S is [sig1, sig3, sig5], and the vertical ranges are (1,1), (3,3), (5,5), (1,3), (3,5), (1,5), etc. But no, the vertical ranges must be contiguous. So if rows 1 and 3 are valid, but row 2 is invalid, then a vertical range (1,3) is invalid. 

Thus, the array S must consist of consecutive valid rows. 

So the valid vertical ranges are exactly the contiguous subarrays of the array of valid rows. 

Thus, the array S is the array of valid rows in order, but consecutive. So if there are invalid rows in between, they split the array into multiple segments. 

For example, if the valid rows are 1,2,4,5, then the array S for j1, j2 is [sig1, sig2, sig4, sig5]. But the vertical ranges (1,2), (4,5), etc. must be considered as separate segments. 

Wait, no. The valid vertical ranges are those where all rows in i1 to i2 are valid, i.e., consecutive in the original row ordering. So for example, if rows 1 and 2 are valid, then (1,2) is valid. If rows 4 and 5 are valid, then (4,5) is valid. But rows 1 and 4 are not consecutive, so a vertical range (1,4) is only valid if all rows 1-4 are valid. 

Thus, the array S for j1, j2 is the list of valid rows in order. For example, if the valid rows are 1,2,4,5, then the array S is [sig1, sig2, sig4, sig5]. But the vertical ranges (1,2) and (4,5) are valid, but (2,4) is invalid because rows 3 and 4 are not valid. 

Thus, the array S is the list of valid rows in order, but not necessarily consecutive. 

But this complicates the application of Manacher's algorithm, because the vertical ranges must be contiguous in the original row indices, but the array S may have gaps. 

For example, if the valid rows are 1, 3, 5, then the array S is [sig1, sig3, sig5], and the vertical ranges allowed are (1,1), (3,3), (5,5), (1,3), (3,5), (1,5) only if all rows between 1 and 3 (rows 2) are valid. But if rows 2 are invalid, then those ranges are invalid. 

Wait, no. Because the vertical range (1,3) includes rows 1, 2, 3. If rows 2 is invalid, then (1,3) is not a valid vertical range. 

So, the array S for j1, j2 is the list of rows that are valid. But the vertical ranges must be contiguous in the original row indices. So the array S is not a list of consecutive valid rows, but includes all valid rows, regardless of their position. 

This means that the vertical ranges (i1, i2) are only valid if all rows between i1 and i2 are valid (i.e., the rows form a contiguous block in the original matrix). 

Thus, the array S can't be processed as a single list. Instead, for each j1, j2, we need to find all contiguous blocks of rows where all are valid. For each such block, process the signature array of the block and count the palindromic subarrays within it. 

For example, suppose for j1, j2 the valid rows are 1,2,3, forming a contiguous block. Then, the signature array is [sig1, sig2, sig3]. We can process this array to find all palindromic subarrays, which are the vertical ranges (1,1), (2,2), (3,3), (1,2), (2,3), (1,3), etc., but only if the signature array for that subarray is a palindrome. 

But if the valid rows are 1,3,5 (non-consecutive), then there are no valid vertical ranges because any range like (1,3) would include row 2 which is invalid. 

Thus, for each j1, j2, we can split the valid rows into contiguous blocks (maximal intervals of consecutive valid rows), and for each such block, compute the number of palindromic subarrays in the signature array of that block. 

The steps are:

For each j1, j2:

   a. For each row r, compute valid[r] and signature[r]. 

   b. Split the rows into maximal contiguous intervals where all rows are valid. 

   c. For each such interval, compute the number of palindromic subarrays in the signature array of that interval. 

   d. Sum all these counts. 

Now, the problem is to split into contiguous intervals and process each interval. 

But how many such intervals can there be? In the worst case, each valid row is isolated (e.g., valid rows are 1,3,5,...), leading to O(n) intervals. But in practice, for each j1, j2, the number of intervals would be O(n). 

Thus, for each j1, j2, the steps are:

   O(n) time to compute valid and signature.

   O(n) time to split into intervals. 

   For each interval of length L, O(L) time to compute the number of palindromic subarrays (using Manacher's algorithm). 

The total time per j1, j2 is O(n) + O(sum over intervals of L) = O(n) per j1, j2. 

So the overall time is O(m² * n) which is 250² * 250 = 15,625,000 operations. Which is manageable. 

Thus, the plan is:

Precompute for each row r and j1, j2:

   - valid[r][j1][j2]: True if the substring j1-j2 can form a palindrome. 

   - signature[r][j1][j2]: the hash of the character counts in the substring j1-j2. 

But storing this is impossible due to memory constraints. 

Thus, for each j1, j2 pair, and for each row r, compute valid[r] and signature[r] on the fly. 

Thus, for each j1, j2:

   For each row r:

      compute the substring from j1 to j2. 

      compute the count of each character. 

      determine if the counts can form a palindrome (valid[r] is True or False). 

      compute the signature (e.g., a tuple of counts, or a hash). 

   Then, split the rows into contiguous valid intervals. 

   For each interval:

      collect the signatures. 

      compute the number of palindromic subarrays in this signature array. 

Sum all counts over all j1, j2 and intervals. 

Now, the question is, how to compute the signature efficiently. 

To compute the signature, for each row r and j1, j2, we need the counts of each character in the substring j1..j2. 

Using prefix sums for each row and character can help. 

So for each row r, compute a prefix sum array for each character. 

For example, prefix[r][c][j] is the number of times character c appears in row r up to column j. 

Then, for substring j1..j2, the count of character c is prefix[r][c][j2] - prefix[r][c][j1-1]. 

This allows O(1) per character per row and j1, j2. 

Thus, for each row r and j1, j2:

   For each character c in 'a' to 'z':

      count[c] = prefix[r][c][j2] - prefix[r][c][j1-1]

   Check if the counts can form a palindrome (i.e., the number of characters with odd counts is 0 or 1, depending on the length of the substring). 

   Compute a hash for the counts. 

The hash can be a tuple of the counts, or a unique value that represents the counts. 

But tuples are not hashable for dictionaries, but for comparing signatures, we can use a tuple. 

Thus, for each row r and j1, j2, the signature is a tuple of counts for each character. 

But comparing two tuples for equality is O(26) time. 

Thus, for each j1, j2 pair, and for each contiguous interval of valid rows, the signature array is a list of tuples, and we need to find the number of palindromic subarrays in this list. 

Using Manacher's algorithm for each such interval would take O(L) time per interval. 

But to compare two elements (tuples) for equality, it's O(26) time. 

Thus, the total time for checking each expansion step in Manacher's algorithm is O(26). 

But Manacher's algorithm requires O(n) steps for each interval. So for each j1, j2 and interval of length L, the time is O(L * 26). 

Which for m=250, n=250 is 250^2 * 250 * 26 = 406,250,000 operations. 

Hmm. This is getting tight. 

But perhaps with optimizations, this can pass. 

So now, let's outline the steps for the code:

Precompute the prefix sums for each row and character. 

For each j1 in 0 to m-1 (assuming 0-based):

   for j2 in j1 to m-1:

      valid = [False]*n

      signatures = [[] for _ in range(n)]

      for r in 0 to n-1:

          counts = [0]*26

          for c in 0..25:

              counts[c] = prefix[r][c][j2+1] - prefix[r][c][j1] 

              (assuming prefix is 1-based for columns)

          length = j2 - j1 + 1

          # Check if can form a palindrome

          odd = 0

          for cnt in counts:

              if cnt % 2 != 0:

                  odd +=1

          if (length % 2 == 0 and odd ==0) or (length %2 ==1 and odd ==1):

              valid[r] = True

              # Compute signature as a tuple of counts, sorted?

              signature = tuple(counts)

              signatures[r] = signature

          else:

              valid[r] = False

      # Now, find contiguous valid intervals

      intervals = []

      current_start = -1

      for i in range(n):

          if valid[i]:

              if current_start == -1:

                  current_start = i

          else:

              if current_start != -1:

                  intervals.append( (current_start, i-1) )

                  current_start = -1

      if current_start != -1:

          intervals.append( (current_start, n-1) )

      # For each interval, compute the number of palindromic subarrays in the signature array

      total = 0

      for (start, end) in intervals:

          L = end - start + 1

          s = [signatures[i] for i in range(start, end+1)]

          count = 0

          # Manacher's algorithm to count palindromic substrings in s

          # Alternatively, expand around each center

          for i in range(len(s)):

              # odd length

              l = i

              r = i

              while l >=0 and r < len(s) and s[l] == s[r]:

                  count +=1

                  l -=1

                  r +=1

              # even length

              l = i

              r = i+1

              while l >=0 and r < len(s) and s[l] == s[r]:

                  count +=1

                  l -=1

                  r +=1

          total += count

      ans += total

This code would be O(m^2 * n * 26) for the prefix sum part, and O(m^2 * sum over intervals of L * 26) for the palindrome checking. 

But this would be O(m^2 * (n*26 + n * 26)) ) = O(m^2 * n * 26 * 2), which for m=250 is 250^2 * 250 * 26 * 2 = 812,500,000 operations. This is probably too slow for Python, which can handle about 1e8 operations per second. 

But perhaps we can optimize some steps. 

For example, the code to compute the counts can be optimized. Instead of iterating over all 26 characters each time, perhaps we can precompute the prefix sums for each row and character. 

Yes, that's already part of the plan. 

Another optimization: For each row r and j1, j2, the length of the substring is j2-j1+1. 

The code to check if the counts can form a palindrome can be optimized. Instead of checking all 26 characters, perhaps we can track the number of characters with odd counts. 

But to compute the number of odd counts, we have to check each character's count. 

Alternatively, during the computation of counts, we can track the number of odd counts. 

So for each row r and j1, j2:

   odd_count = 0

   for c in 0..25:

       cnt = prefix[r][c][j2+1] - prefix[r][c][j1]

       if cnt % 2 == 1:

           odd_count +=1

   length = j2 - j1 + 1

   if (length % 2 == 0 and odd_count == 0) or (length % 2 ==1 and odd_count ==1):

       valid[r] = True

   else:

       valid[r] = False

This reduces the check to O(26) per row and j1, j2. 

But no, we need to compute the counts for the signature. Because the signature is the tuple of counts. 

So we need to compute the counts for each character regardless. 

So perhaps the signature can be represented as a tuple of counts, but when comparing signatures, we need to compare all 26 elements. 

This is a bottleneck. 

Alternative Idea: Compute a hash of the signature. For example, for each row and j1, j2, compute a hash value that uniquely represents the counts. This way, comparing signatures is O(1) per comparison. 

But how to compute this hash efficiently. 

For example, the hash could be a tuple of the counts, or a bitmask where each bit represents the parity of the count (but this would not capture the exact counts, so it's not suitable). 

Alternatively, for each count, we can compute a product of primes raised to the count. For example, for 'a' -> prime 2, 'b' -> prime 3, etc. Then, the hash is the product of primes^count. 

But this would quickly overflow, even for small counts. 

Alternatively, use a rolling hash where each character's count is multiplied by a base and added. For example, each character's count is treated as a digit in a base-B number, and the hash is computed as sum(count[c] * B^c). But with 26 characters, this could be manageable with a large base and using Python's arbitrary-precision integers. 

Alternatively, use a tuple of the counts as the hash. Since tuples are hashable, we can compare them directly. 

But in Python, comparing two tuples of 26 elements is O(26) time. 

Thus, comparing the signatures during the palindrome expansion is O(26) per comparison. 

This is the main time-consuming part. 

But in the worst case, each expansion step (for the odd and even lengths) could require O(26) comparisons for each step. 

So for a vertical interval of length L, the number of steps is O(L), and each step has O(26) comparisons, leading to O(L * 26) time per interval. 

But this is still expensive. 

Alternative Idea: Precompute for each row and j1, j2 a unique integer identifier for the signature. Then, comparing two signatures becomes O(1). 

But to do this, we need to map each unique tuple of counts to a unique integer. 

This can be done using a dictionary. 

So for each row and j1, j2, compute the tuple of counts, and assign a unique integer to each unique tuple. 

But for each j1, j2, this may not be feasible due to time and memory constraints. 

Alternatively, precompute a hash function that maps the tuple to a unique value. 

But even this is time-consuming. 

Alternatively, use a hashing technique like rolling hash. 

For example, for each tuple of counts, compute a hash as follows:

hash = 0

for c in 0 to 25:

    hash = hash * 1000003 + counts[c]

This gives a unique hash for each tuple, assuming the counts are not too large (since the maximum count per character is up to m, which is 250. 1000003 is a prime larger than 250 * 26). 

But in Python, this is manageable. 

So for each row and j1, j2, compute the hash, and compare the hash values instead of the tuples. 

Thus, comparing two signatures becomes O(1) time. 

Thus, the code can be optimized as follows:

For each row r and j1, j2:

   compute counts as before

   compute the hash as sum( counts[c] * (1000003)^c ), but perhaps a better way is to compute a polynomial rolling hash. 

But for simplicity, perhaps compute a tuple of counts and use a hash function that converts the tuple into an integer. 

In Python, tuples are hashable and can be used as keys in a dictionary. However, the hash of a tuple is computed based on the elements, but two different tuples will have different hash values. 

But in practice, the hash may have collisions. But for the purpose of this problem, perhaps using the tuple directly as the signature is acceptable. 

Alternatively, use a library that can compute a collision-resistant hash. But for the scope of this problem, using tuples and comparing them directly should suffice. 

Thus, during the palindrome expansion, when comparing two elements, we compare their tuples (signatures). 

But for each expansion step, this takes O(26) time. 

But in Python, comparing two tuples is optimized and should be fast. 

But for large m and n, this may still be a problem. 

Alternative Idea: Use bitmasking. But since the counts are up to 250, which requires 8 bits per character, a 26-character tuple would require 208 bits, which can be represented as a Python integer. 

For example, for each count of a character, shift and add to form a unique integer. 

For example:

signature = 0

for c in 0 to 25:

    signature = (signature << 8) | (count[c] & 0xFF)

This would give a unique integer for each possible combination of counts (assuming counts are <= 255). 

Thus, each signature can be represented as a 208-bit integer. 

This allows comparing signatures in O(1) time. 

Thus, this would significantly speed up the comparisons during the palindrome expansion. 

So, the code can be modified to compute the signature as an integer. 

Thus, for each row r and j1, j2:

   compute counts[c] for each character. 

   compute the signature as an integer, e.g., by packing the counts into a single integer. 

This way, comparing signatures is O(1). 

Thus, the code would look like:

for c in 0..25:

    signature = signature << 8 | counts[c]

But in Python, integers can be arbitrarily large. 

This would work, but for 26 characters, each requiring 8 bits, the signature would be 26 * 8 = 208 bits. 

Thus, the code can compute the signature as follows:

signature = 0

for c in range(26):

    signature = (signature << 8) | counts[c]

This will generate a unique integer for each possible combination of counts. 

Thus, comparing two signatures is a simple integer comparison. 

This reduces the comparison time from O(26) to O(1) per comparison. 

Thus, the code's time complexity becomes O(m² * n) for the prefix sum part, and O(m² * sum of L) for the palindrome checking part. 

For each j1, j2 pair:

   For each row r:

       O(26) time to compute counts and signature. 

   For each contiguous valid interval of length L:

       O(L) time to compute the number of palindromic subarrays. 

Thus, the total time is O(m² * n * 26) + O(m² * sum of L). 

But sum of L over all j1, j2 and intervals is O(m² * n), because for each j1, j2, sum of L is the number of valid rows for that j1, j2. 

Thus, the total time is O(m² * n * 26) + O(m² * n) = O(m² * n * 27) → acceptable for m=250 and n=250. 

Thus, this approach should work. 

Now, let's proceed to code this. 

First, precompute the prefix sums for each row and character. 

In Python:

n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

prefix = [[[0]*(m+1) for _ in range(26)] for __ in range(n)]

for r in range(n):
    row = matrix[r]
    for c in range(26):
        char = chr(ord('a') + c)
        cnt = 0
        for j in range(m):
            if row[j] == char:
                cnt +=1
            prefix[r][c][j+1] = prefix[r][c][j] + (1 if row[j] == char else 0)
    # Alternative way to compute prefix sums:
    # for j in range(1, m+1):
    #     for c in range(26):
    #         prefix[r][c][j] = prefix[r][c][j-1] + (1 if matrix[r][j-1] == chr(ord('a') + c) else 0)

But this is O(n*m*26), which is acceptable for n=250, m=250: 250*250*26=1,625,000 operations. 

Then, for each j1 and j2 (columns are 1-based?), need to compute for each row r the counts. 

But in code, columns are 0-based or 1-based? Let's assume that the prefix array is 1-based. So for j in 1..m, prefix[r][c][j] is the count up to column j (exclusive?), or inclusive? 

Wait, the code above initializes prefix[r][c][j] as the count from the start up to and including column j-1. For example, for j=0, prefix is 0. For j=1, it's the count in column 0. For j=2, count in columns 0 and 1. 

But perhaps it's easier to adjust the indices. 

Alternatively, for each row r and character c, prefix[r][c][j] is the number of times character c appears in the first j columns (columns 0 to j-1). 

Thus, the count from j1 to j2 (0-based) is prefix[r][c][j2+1] - prefix[r][c][j1]. 

Yes. 

So, for example, if j1=0, j2=2 (columns 0, 1, 2), the count is prefix[r][c][3] - prefix[r][c][0]. 

Thus, the code for the counts is:

counts = [0]*26
for c in range(26):
    counts[c] = prefix[r][c][j2+1] - prefix[r][c][j1]

where j1 and j2 are 0-based columns (j2 >= j1). 

Thus, the code can proceed. 

Now, the code for processing each j1 and j2:

ans = 0
for j1 in range(m):
    for j2 in range(j1, m):
        valid = [False]*n
        signatures = [0]*n
        for r in range(n):
            counts = []
            for c in range(26):
                cnt = prefix[r][c][j2+1] - prefix[r][c][j1]
                counts.append(cnt)
            # Check if can form a palindrome
            length = j2 - j1 + 1
            odd = 0
            for cnt in counts:
                if cnt % 2 != 0:
                    odd +=1
            if (length % 2 == 0 and odd == 0) or (length % 2 ==1 and odd ==1):
                valid[r] = True
                # Compute signature as integer
                sig = 0
                for cnt in counts:
                    sig = (sig << 8) | cnt
                signatures[r] = sig
            else:
                valid[r] = False
                signatures[r] = 0
        # Split into contiguous valid intervals
        intervals = []
        current_start = None
        for i in range(n):
            if valid[i]:
                if current_start is None:
                    current_start = i
            else:
                if current_start is not None:
                    intervals.append( (current_start, i-1) )
                    current_start = None
        if current_start is not None:
            intervals.append( (current_start, n-1) )
        # Process each interval
        for (s, e) in intervals:
            L = e - s + 1
            # Collect signatures of this interval
            sigs = [signatures[i] for i in range(s, e+1)]
            # Count palindromic subarrays
            count = 0
            for i in range(len(sigs)):
                # Odd length
                l = i
                r = i
                while l >= 0 and r < len(sigs) and sigs[l] == sigs[r]:
                    count +=1
                    l -=1
                    r +=1
                # Even length
                l = i
                r = i+1
                while l >=0 and r < len(sigs) and sigs[l] == sigs[r]:
                    count +=1
                    l -=1
                    r +=1
            ans += count
print(ans)

But this code has a few issues. For example, the prefix sum calculation is incorrect in the code. Let's fix that. 

First, the code for prefix sums needs to correctly compute the count of each character up to each column. 

In Python, for each row r:

row = matrix[r]
for c in range(26):
    cnt = 0
    prefix[r][c][0] = 0
    for j in range(m):
        prefix[r][c][j+1] = prefix[r][c][j] + (1 if row[j] == chr(ord('a') + c) else 0)

Thus, the prefix sums are correctly computed. 

Now, the code should work. 

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    matrix = [input_stream.readline().rstrip("\n").strip() for _ in range(n)]

    # Precompute prefix sums for each row and character
    prefix = [[[0] * (m + 1) for _ in range(26)] for __ in range(n)]
    for r in range(n):
        row = matrix[r]
        for c in range(26):
            char = chr(ord('a') + c)
            current = 0
            for j in range(m):
                prefix[r][c][j + 1] = current + (1 if row[j] == char else 0)
                current = prefix[r][c][j + 1]

    ans = 0

    for j1 in range(m):
        for j2 in range(j1, m):
            valid = [False] * n
            signatures = [0] * n
            for r in range(n):
                counts = []
                for c in range(26):
                    cnt = prefix[r][c][j2 + 1] - prefix[r][c][j1]
                    counts.append(cnt)
                length = j2 - j1 + 1
                odd = 0
                for cnt in counts:
                    if cnt % 2 != 0:
                        odd += 1
                if (length % 2 == 0 and odd == 0) or (length % 2 == 1 and odd == 1):
                    valid[r] = True
                    sig = 0
                    for cnt in counts:
                        sig = (sig << 8) | cnt
                    signatures[r] = sig
                else:
                    valid[r] = False
            
            intervals = []
            current_start = None
            for i in range(n):
                if valid[i]:
                    if current_start is None:
                        current_start = i
                else:
                    if current_start is not None:
                        intervals.append((current_start, i - 1))
                        current_start = None
            if current_start is not None:
                intervals.append((current_start, n - 1))
            
            for (s, e) in intervals:
                sigs = [signatures[i] for i in range(s, e + 1)]
                count = 0
                for i in range(len(sigs)):
                    l = i
                    r = i
                    while l >= 0 and r < len(sigs) and sigs[l] == sigs[r]:
                        count += 1
                        l -= 1
                        r += 1
                    l = i
                    r = i + 1
                    while l >= 0 and r < len(sigs) and sigs[l] == sigs[r]:
                        count += 1
                        l -= 1
                        r += 1
                ans += count

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 3
aca
aac
""",
            "output": \
"""\
11
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

The code reads the matrix, computes the prefix sums for each character, then for each j1, j2 pair, computes the valid rows and their signatures. For each contiguous valid interval, it counts the number of palindromic subarrays using expansion around the center. 

The code uses the signature as an integer, allowing O(1) comparisons. 

Thus, this code should work and pass all test cases.
</think>

```python
n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

# Precompute prefix sums for each row and character
prefix = [[[0] * (m + 1) for _ in range(26)] for __ in range(n)]
for r in range(n):
    row = matrix[r]
    for c in range(26):
        char = chr(ord('a') + c)
        current = 0
        for j in range(m):
            prefix[r][c][j + 1] = current + (1 if row[j] == char else 0)
            current = prefix[r][c][j + 1]

ans = 0

for j1 in range(m):
    for j2 in range(j1, m):
        valid = [False] * n
        signatures = [0] * n
        for r in range(n):
            counts = []
            for c in range(26):
                cnt = prefix[r][c][j2 + 1] - prefix[r][c][j1]
                counts.append(cnt)
            length = j2 - j1 + 1
            odd = 0
            for cnt in counts:
                if cnt % 2 != 0:
                    odd += 1
            if (length % 2 == 0 and odd == 0) or (length % 2 == 1 and odd == 1):
                valid[r] = True
                sig = 0
                for cnt in counts:
                    sig = (sig << 8) | cnt
                signatures[r] = sig
            else:
                valid[r] = False
        
        intervals = []
        current_start = None
        for i in range(n):
            if valid[i]:
                if current_start is None:
                    current_start = i
            else:
                if current_start is not None:
                    intervals.append((current_start, i - 1))
                    current_start = None
        if current_start is not None:
            intervals.append((current_start, n - 1))
        
        for (s, e) in intervals:
            sigs = [signatures[i] for i in range(s, e + 1)]
            count = 0
            for i in range(len(sigs)):
                l = i
                r = i
                while l >= 0 and r < len(sigs) and sigs[l] == sigs[r]:
                    count += 1
                    l -= 1
                    r += 1
                l = i
                r = i + 1
                while l >= 0 and r < len(sigs) and sigs[l] == sigs[r]:
                    count += 1
                    l -= 1
                    r += 1
            ans += count

print(ans)
```
