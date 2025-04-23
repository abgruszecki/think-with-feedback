<think>
Okay, let's try to figure out this problem. So, the problem is about selecting some of the given strings to form a palindrome by concatenating them, and we need to maximize the total beauty. Each string can be used at most once. The empty string is allowed, which gives a sum of 0 if all a_i are negative.

Hmm. First, I need to understand how the strings can form a palindrome when concatenated. Since all the strings have the same length, when they are concatenated in some order, the entire string must read the same forwards and backwards.

Wait, each string is of length n. Let's say the total concatenated string has length m * n (since each is n). For this to be a palindrome, each character in position i must equal the character in position (m * n - i - 1). But since each string is n characters long, the way the strings are arranged must form a mirror image.

Alternatively, the order in which the strings are placed must form a palindrome when considered as a sequence of blocks. For example, if you have strings s1, s2, s3, then the concatenated string s1s2s3 must be a palindrome. But each s_i is length n, so the first n characters (s1) must mirror the last n characters (s3 reversed), and s2 must be a palindrome itself. Similarly, if there's an even number of strings, then each string must have a mirror pair in reverse order.

Wait, perhaps the correct approach is to group the strings into pairs such that one is the reverse of the other. Then, these pairs can be placed symmetrically around the center. Additionally, there can be at most one string that is itself a palindrome, which can be placed in the center.

So, the strategy might be:

1. For each string, check if it's a palindrome. If it is, it can be used as the center of the palindrome, but only once.

2. For non-palindromic strings, we can pair them with their reverse. For example, if we have a string s and another string t which is the reverse of s, then each occurrence of s and t can be paired (taking as many pairs as possible) to contribute their combined beauty. However, this depends on whether the pair's total beauty (a + b) is positive. If the sum is positive, we should include the pair; otherwise, it's better to skip them.

3. Additionally, we need to consider that some strings may have a reverse that's not present. So, for a string s, if there's no reverse of s, then s can't be used in any pair, and thus can't contribute to the palindrome unless it's a palindrome itself. Wait, no. Because if s is not a palindrome, then to include it in the palindrome, there must be another string that is its reverse. Otherwise, it's impossible. So, non-palindromic strings can only be part of pairs with their reverse.

So, the steps are:

- For each string s, compute its reverse s_rev.

- Group the strings into pairs (s, s_rev) where s is not a palindrome. For each such pair, if we take them, their combined beauty is the sum of their a_i values. We can choose to take as many pairs as possible, but only once per each string (since each string can be used once).

Wait, but each string can be used once. So, for example, if there are multiple instances of s and multiple of s_rev, the maximum pairs possible is the minimum of the count of s and s_rev. However, in the problem, each string is given once (or multiple times with possibly different a_i). Wait, the input is k lines, each is a string and a beauty. The same string can appear multiple times, even with different a_i. So, for example, "abb 2" and "abb 5" are two separate entries, both with s = "abb".

So, for the problem, when considering pairs, for each s and s_rev, we can have multiple possible pairs, but each string can be used at most once.

Wait, but each entry in the input is a separate string (even if same characters) and can be used once. So when grouping, for example, if s and s_rev are different, we need to consider all possible pairs of s and s_rev. For each occurrence of s and each occurrence of s_rev, we can form a pair. However, each pair uses one s and one s_rev. So, for all such pairs, the maximum number of pairs is min(count of s, count of s_rev), but since each can have different a_i, perhaps we need to select the best pairs.

Wait, this seems complicated. Let's think again.

Let's model the problem as follows:

We have two main types of strings: palindromic and non-palindromic.

For non-palindromic strings, a string s can contribute to the palindrome only if its reverse s_rev is also present. Then, for each such pair (s, s_rev), we can take them once each, adding their a_i values. But we need to select the pairs such that the sum of a_i + a_j (where s_j is s_rev) is positive. If the sum is positive, then each such pair contributes a positive value to the total. Otherwise, it's better not to include them.

For palindromic strings, each can be used once, either as part of a pair (but since they are palindromes, pairing them with themselves would be possible, but perhaps not necessary) or as the central element.

Wait, but a palindrome's reverse is itself. So, if s is a palindrome, then s_rev is s. So, for palindromic strings, when considering pairs, you can pair two copies of the same string. However, in such a case, each pair contributes 2 * a_i (assuming you take two copies). But each of those two copies must be distinct entries in the input. For example, if there are two entries of "aaa" with a_i 3 and 4, then taking them as a pair adds 3+4=7. But each can be used once.

Alternatively, the pairs for palindromic strings can be formed by taking two copies (if available). However, for each such pair, the sum of their a_i's must be positive. For example, if there are multiple palindromic strings of the same type (same s), then the optimal is to take as many pairs as possible (each contributing a_i + a_j), but each pair uses two different entries.

But wait, even palindromic strings can form pairs. However, when you pair two palindromic strings (since their reverse is themselves), you can place them symmetrically. For example, two palindromic strings s and s (same s) can form a pair, contributing a1 + a2. Then, when building the palindrome, they can be placed as s followed by s. Since each is a palindrome, the concatenation s+s would form a palindrome only if s is a palindrome (which it is), but the entire string s+s is a palindrome only if s is a palindrome. But in that case, s is a palindrome, so s + s's reverse (which is s) would form a palindrome. So, for palindromic strings, pairing them with themselves (as in two copies) allows them to contribute to the total, as their sum a_i + a_j, but only if the sum is positive.

So, the approach could be:

1. For each string, check if it's a palindrome. For non-palindromic strings, group them with their reverses.

2. For each group of non-palindromic strings:

   a. Find all strings in the group that are s and s_rev.

   b. For these, the optimal way is to pair each s with a s_rev. For each pair, the sum of their a_i's should be positive. So, for all possible pairs between s and s_rev (but each can be used once), we need to select pairs where the sum is positive, and maximize the total.

   c. To compute this, we can collect all s and s_rev's a_i values, sort them in a way that pairs the largest possible a_i for s with the largest possible a_i for s_rev. For example, sort the s's a_i in ascending order and s_rev's in descending, then pair them and check if sum is positive. But this might not be the optimal way.

   Wait, perhaps the best way is to take all pairs of s and s_rev where their sum is positive. So, for each possible s and s_rev in the input, we can pair them, but we have to make sure each is used once.

   But this seems complicated. How can we model this?

   Let's consider that for each s and s_rev (s is not a palindrome), the maximum possible sum is the sum of all pairs (a_i for s, a_j for s_rev) where a_i + a_j > 0, and each s and s_rev is used at most once.

   But how to compute this efficiently?

   Alternative approach: for each s and s_rev (s is not a palindrome), collect all a_i of s and a_j of s_rev, sort them, and greedily pair the largest possible a_i from s with the largest possible a_j from s_rev.

   For example, if s has a list A = [5, 3, 1], and s_rev has a list B = [4, 2], then the best pairs would be 5+4=9 and 3+2=5. So total is 14.

   So the way to maximize the sum is to sort A in descending order, B in descending order, and pair the first elements, then second, etc., until either list is exhausted or the sum is not positive.

   So the algorithm for a pair group (s and s_rev) would be:

   - Sort the a_i of s in descending order.

   - Sort the a_j of s_rev in descending order.

   - Pair the largest remaining from each list, adding to the total if the sum is positive.

   So for each possible pair, if a_i + a_j >0, include it, else stop.

   This seems manageable. But how to efficiently compute this for all possible pairs?

   But first, the problem is that s and s_rev are two different groups. Wait, no. For example, if s is 'abc' and s_rev is 'cba', then the group for 'abc' would be all 'abc's and 'cba's. But we have to process this group once. So to avoid processing the same group twice (once for s and once for s_rev), we need to manage a way to track which groups have been processed.

   So the plan is:

   - For all strings, group them by their string. So for each string s, we have a list of a_i's.

   - For each s, compute s_rev. If s is not a palindrome, then check if s_rev exists in the groups.

   - For each pair s and s_rev (s < s_rev lex order to avoid processing the same pair twice), process them as a group.

   - For each such group, collect all a_i from s and a_j from s_rev. Sort them in descending order and pair the largest elements until sum is positive.

   - The sum from all such pairs is added to the total.

   Additionally, for palindromic strings, we can pair them with themselves. So, for each palindrome s, collect all a_i's. Then, we can form pairs of two, adding their sum to the total if the sum is positive. Then, any leftover a_i (if the count is odd) can be considered as a candidate for the center of the palindrome.

   Wait, but for palindromic strings, when you pair two of them, their sum is a_i + a_j. Since they are palindromes, placing them in the palindrome sequence as a pair (s followed by s) would form a palindrome. But each s is a palindrome, so s + s is a palindrome only if the entire string is a palindrome. But since each s is a palindrome, s reversed is s. So, s followed by s would be s + s, which reversed is s reversed (s) followed by s reversed (s) which is the same as the original. So yes, s+s is a palindrome.

   So for palindromic strings, pairing two of them (distinct entries) gives a sum of their a_i's. But only if the sum is positive.

   Then, for each group of palindromic strings, the maximum number of pairs is floor(count / 2). But each pair contributes a sum of a_i + a_j. So, to maximize the sum, we should sort the a_i's in descending order, and pair the first with the second, third with fourth, etc., as long as their sum is positive.

   For example, if a_i's are [5, 3, 2, 1], sorted as 5,3,2,1. Then pairs are 5+3=8 (positive), 2+1=3 (positive). So total is 11.

   But if the a_i's are [5, -3, -4], then pairs would be 5 + (-3) = 2 (positive?), so yes. Then sum is 2, but perhaps it's better to include that pair.

   Wait, the sum must be positive. So, if the sum is positive, include the pair. Otherwise, stop.

   So for the palindromic group:

   - Sort a_i's in descending order.

   - For i from 0 to len(a) -1 step 2:

      - if i+1 >= len(a), break.

      - sum = a[i] + a[i+1]

      - if sum >0, add to the total, else break.

      - increment i by 2.

   But wait, this approach would take pairs in order. However, maybe a better approach is to pair the largest possible a_i's first. For example, if the a_i's are [3,3,-5]. Then pairing the two 3's gives 6, which is better than pairing 3 and -5 (-2). So the sum would be 6.

   So sorting in descending order and pairing consecutive elements is the right approach.

   Then, after pairing as many as possible, any remaining a_i (if there's an odd number) can be considered as a candidate for the center. For example, in the group [5,3,2,1], after pairing 5+3 and 2+1, there are no remaining. In a group [5,3,2], after pairing 5+3, 2 is left and could be considered as a center candidate.

   So, after processing all pairs, we can collect all remaining a_i's (for palindromic groups) and track the maximum possible a_i that could be added as the center. Then, in the end, we can choose the best possible center (the maximum a_i from all possible candidates, including palindromic groups and any possible center from the non-palindromic groups? Wait, no. The center can only be a palindrome. Because if the total length is odd, the middle string must be a palindrome. Otherwise, the entire concatenated string can't be a palindrome.

   So, the center must be a palindrome. So the only possible candidates for the center are the palindromic strings.

   So, after processing all non-palindromic pairs and palindromic pairs, we can collect all possible candidates for the center (the leftover a_i's from palindromic groups) and choose the maximum a_i. If adding this a_i (if positive) to the total improves the sum, then we can add it. Otherwise, the total remains as is.

   So the steps are:

   1. For all strings, group them by their string.

   2. For each string s, check if it's a palindrome. If not, find s_rev and see if it's present. Then, process pairs of s and s_rev once (ensuring that each pair is processed once).

   3. For each non-palindromic s:

      a. If s has already been processed (as part of s_rev group), skip.

      b. Compute s_rev.

      c. If s_rev is not present in the groups, then the group s cannot form any pairs, so proceed.

      d. Else, collect the a_i's from s and s_rev, sort them in descending order.

      e. Pair the largest a_i from s and s_rev, sum them. If the sum is positive, add to the total. Continue until one of the lists is exhausted or the sum is no longer positive.

   4. For each palindromic s:

      a. Collect all a_i's, sort in descending order.

      b. Pair consecutive elements (i and i+1). If their sum is positive, add to the total. Then, track any remaining elements (if the count is odd) as possible center candidates.

   5. Finally, collect all possible center candidates (the remaining elements from palindromic groups), and select the maximum one. If adding this to the total increases it (i.e., if it's positive), then add it to the total. Otherwise, the total remains as is.

   Also, note that the empty string is a valid option. So even if all contributions are negative, the maximum is 0. But in our processing, we can track the total sum, and if it's negative, return 0.

   Now, the main challenge is to implement this efficiently, given the constraints. Let's see the constraints: k can be up to 1e5, and n up to 1e5, but n*k is up to 1e5. So the total input size is manageable.

   Let's think about how to represent the groups. For each string s, we can use a dictionary (hash map) that maps each string to a list of its a_i's. Also, for each s, precompute whether it's a palindrome.

   Then, for each group s in the dictionary:

   - If s is a palindrome: process as part of the palindromic groups.

   - Else: process if s is lex smaller than s_rev (to avoid processing pairs twice). For example, if s is 'abb' and s_rev is 'bba', then when s is 'abb', since 'abb' comes before 'bba' lex, we process them. When s is 'bba', since 'bba' is not a palindrome and s_rev is 'abb', which is lex smaller than 'bba', we skip processing this pair.

   So, the code steps:

   1. Read all k strings, group their a_i's in a dictionary. Also, check if each string is a palindrome, and store that info.

   2. For non-palindromic strings:

      For each s in the dictionary where s is not a palindrome and s < s_rev lex order:

         a. Check if s_rev exists in the dictionary.

         b. If not, skip.

         c. Else, get the list of a_i's for s and s_rev.

         d. Sort both lists in descending order.

         e. Pair elements from s and s_rev, adding the sum if it's positive.

         f. The number of pairs is min(len(s_list), len(s_rev_list)), but for each pair, the sum must be positive.

         Wait, no. The code would need to iterate through the lists until the sum is positive. For example, even if there are 5 elements in each list, but the sum of the first pair is positive, but the next pair is negative, we take only the first pair.

         So, the algorithm is:

         i = 0

         j = 0

         total_pairs = 0

         while i < len(s_list) and j < len(s_rev_list):

             sum_pair = s_list[i] + s_rev_list[j]

             if sum_pair > 0:

                 total += sum_pair

                 i += 1

                 j += 1

             else:

                 break

         So, this way, we take as many pairs as possible where the sum is positive, starting with the largest elements.

         Because both lists are sorted in descending order, the next pairs would have lower or equal sum. So once the sum becomes non-positive, all remaining pairs would also have non-positive sums, so we can break.

     3. For palindromic strings:

         For each s in the dictionary where s is a palindrome:

             collect all a_i's, sort in descending order.

             Then, iterate through the list in steps of 2.

             For each pair (a[i], a[i+1]):

                 sum_p = a[i] + a[i+1]

                 if sum_p >0:

                     total += sum_p

                 else:

                     break

             The remaining element (if count is odd) is a[i], which is the last element (since the list is sorted). So the maximum possible candidate is the maximum of all such remaining elements.

     4. After processing all pairs, collect all possible candidates for the center (the remaining elements from palindromic groups). The maximum among these candidates (if positive) is added to the total.

   Then, compare the total with zero and output the maximum of the two.

   Now, let's test this approach against the examples.

   First example:

   Input:

   7 3

   abb 2

   aaa -3

   bba -1

   zyz -4

   abb 5

   aaa 7

   xyx 4

   So, the strings:

   "abb" (a=2 and 5). Reverse is "bba".

   "aaa" is a palindrome (a=-3 and 7).

   "bba" (a=-1). Reverse is "abb".

   "zyz" (reverse is "zyz", which is same as the original. So it's a palindrome? Wait, wait: "zyz" reversed is "zyz", so yes, it's a palindrome. But in the input, the fourth line is "zyz -4". So that's a palindrome.

   "xyx" is a palindrome (a=4).

   So, processing non-palindromic groups:

   For "abb" and "bba" (since "abb" < "bba" lex order? Let's see: "abb" vs "bba". The first character 'a' is less than 'b', so yes. So process this pair.

   The a_i's for "abb" are [2,5], sorted in descending order [5,2].

   The a_i's for "bba" is [-1], sorted as [-1].

   Pairing:

   The first pair is 5 + (-1) =4>0 → add 4. Then, next elements: 2 in "abb" and nothing in "bba". So total from this pair is 4.

   Then, other non-palindromic groups: like "zyz" (palindrome), "xyx" (palindrome), "aaa" (palindrome), "zyz" and "xyx" are palindromes.

   Now, palindromic groups:

   For "aaa" → a_i's are [-3,7]. sorted → 7, -3.

   Pair them:

   7 + (-3) =4>0 → add 4. So sum from palindromic pairs is 4. Remaining elements? No, since two elements. So no leftover.

   For "zyz": a_i is -4. Only one element. So pairing none. The candidate is -4.

   For "xyx": a_i is 4. One element. Candidate is 4.

   Then, other palindromic strings?

   So after processing all, the total from non-palindromic is 4 (from abb/bba pair).

   The total from palindromic pairs is 4 (from aaa group).

   So total so far is 4 +4 =8. Then, the center candidates are 4 (xyx) and -4 (zyz). The maximum is 4. Adding this to total gives 8+4=12. Which matches the first example's output.

   Another example:

   Input 2:

   3 1

   a 1

   a 2

   a 3

   All are palindromes. Their a_i's are [1,2,3] sorted as [3,2,1].

   Pairs: 3+2=5 (sum positive), then 1 is left. So sum from pairs is 5. Then, the center candidate is 1. 5 +1 =6. Which is the output.

   Third example:

   Input:

   2 5

   abcde 10000

   abcde 10000

   Each string is "abcde", which is not a palindrome. Its reverse is "edcba". But there are no "edcba" in the input. So the pair can't be formed. So the total is 0 (since both can't be used, so the maximum is the empty string).

   So the output is 0.

   So the approach works for these examples.

   Now, the code.

   Let's think about how to implement this.

   First, read all the input strings, group them by their string. For each string, check if it's a palindrome.

   Then, process non-palindromic pairs and palindromic pairs.

   For grouping, in Python, a dictionary where the key is the string, and the value is a list of a_i's. Also, for each string, precompute whether it is a palindrome.

   How to check if a string is a palindrome: compare the string to its reverse.

   Now, for processing the non-palindromic pairs:

   For each s in the dictionary:

      if s is not a palindrome:

          s_rev = s[::-1]

          if s_rev is not in the dictionary, skip.

          else:

              if s < s_rev:

                  process the pair (s and s_rev)

   Then, for processing the pair:

   Get the a_i lists for s and s_rev, sort them in descending order.

   Iterate through both lists, adding the sum of pairs as long as the sum is positive.

   For example:

   s_list = sorted in descending order: [5,2]

   s_rev_list = sorted in descending order: [-1]

   Sum of 5 + (-1) =4>0 → add 4.

   Then, j runs out of elements. So stop.

   Now, code:

   For the non-palindromic pairs:

   for s in list(d.keys()):

       if is_palindrome[s] is False:

           s_rev = s[::-1]

           if s_rev in d:

               if s < s_rev:  # avoid processing twice

                   list_s = sorted(d[s], reverse=True)

                   list_rev = sorted(d[s_rev], reverse=True)

                   i = 0

                   j = 0

                   while i < len(list_s) and j < len(list_rev):

                       sum_p = list_s[i] + list_rev[j]

                       if sum_p >0:

                           total += sum_p

                           i +=1

                           j +=1

                       else:

                           break

   Then, for palindromic strings:

   for s in d:

       if is_palindrome[s]:

           list_a = sorted(d[s], reverse=True)

           current_sum =0

           max_center = -inf

           for i in range(0, len(list_a), 2):

               if i+1 < len(list_a):

                   pair_sum = list_a[i] + list_a[i+1]

                   if pair_sum >0:

                       current_sum += pair_sum

                   else:

                       # if even this pair is not positive, then no more pairs possible.

                       # Also, the remaining elements (i and beyond) can't form a positive pair.

                       break

               else:

                   # i is the last element, possible center.

                   if list_a[i] > max_center:

                       max_center = list_a[i]

                   break

           # Now, after processing pairs, collect the possible center.

           # If there's a remaining element after processing pairs:

           # Check if the total number of elements processed is even.

           # For example, if len is 5: processed 0,1,2,3 → 4 elements (i=4). Then, i=4 is even. But in the loop, i starts at 0, step 2. So for len 5, loop runs for i=0,2,4.

           # Wait, let's see:

           # len(list_a) is 5. i ranges 0,2,4.

           # For i=4:

               i+1 is 5, which is >= len(list_a), so enter the else.

               max_center is updated to list_a[4].

               break.

           So, in the code, after the loop, the max_center is the maximum possible among all elements that are left as possible centers.

           But wait, in the code above, the loop increments by 2. For example, in a list of 5 elements sorted in descending order:

           i starts at 0: check i+1 (1). sum is a[0]+a[1]. If positive, add to current_sum. i becomes 2.

           Then i=2: check i+1 (3). sum a[2] +a[3]. if positive, add. i becomes 4.

           Then i=4: i+1 is 5, which is out of range. So set max_center to a[4], break.

           So the code handles all possible pairs, and the max_center is the last element if the count is odd.

           But what if the pairs after the first are not added? For example, list_a is [5,3,2,-4]. Sorted as [5,3,2,-4].

           i=0: pair 5+3=8>0 → add. i becomes 2.

           i=2: pair 2 + (-4) =-2 → not added. So break.

           Then, since i is 2, which is even, but the loop stops here. So the code does not check for a possible center at i=2 (2). So, the max_center in this case is 2 (a[2])? Because in the loop, when i=2, we check i+1=3. The sum is negative, so we break. Then, in the else clause, since i+1 is not < len(list_a), which it is (3 is <4?), len is 4. So i=2, i+1=3 <4. So in that case, the code would check if pair_sum is positive. Since it's -2, the code breaks.

           So after the loop, the code does not have any remaining elements. So the max_center remains as the initial -inf. But in this case, the pairs are 5+3=8. The remaining elements are 2 and -4. Since the pair is not added, they are not considered. So the code doesn't track any center candidate here. But in reality, the code's code for the palindromic group would add 8 to the total, and no center candidate. So the code correctly adds 8, and no center.

           So, the code for palindromic groups:

           current_sum is added to the total. Also, the max_center is tracked (which is the maximum between existing max_center and the possible remaining elements). Then, after processing all palindromic groups, collect all max_centers and find the maximum among them. Then, if this maximum is positive, add it to the total.

           Wait, no. Because the code for palindromic groups needs to track the current_sum (the sum of pairs) and any possible remaining elements that can be the center. But in the code above, the code for palindromic groups is not collecting the max_center for each group.

           Wait, in the code I outlined earlier, the palindromic group's processing:

           For each group:

               sort the a_i's.

               pair them as much as possible (sum pairs).

               track the max_center for that group (the remaining elements after pairing).

               add the sum of pairs to the total.

               collect the max_center of this group as a candidate for the global center.

           Then, after all groups are processed, the maximum among all such candidates is added to the total if it's positive.

           So the code for palindromic groups:

           For each group:

               list_a = sorted in descending order.

               current_sum =0

               max_center_candidate = -infinity

               i =0

               while i < len(list_a):

                   if i+1 < len(list_a):

                       pair_sum = list_a[i] + list_a[i+1]

                       if pair_sum >0:

                           current_sum += pair_sum

                           i +=2

                       else:

                           # even if i is even, but the pair sum is not positive, break.

                           break

                   else:

                       # i is the last element, possible candidate.

                       max_center_candidate = max(max_center_candidate, list_a[i])

                       break

               # After processing the pairs, check if there's a leftover.

               # i could be even or odd.

               # If the loop ended without processing all elements, check if i is within the list.

               # For example, if the loop broke in the middle, i is pointing to the next unprocessed element.

               # Wait, the code above uses a for loop with steps of 2. Maybe the code should be rewritten with a while loop.

               # Let's think again.

               Maybe a better approach is to use a while loop:

               i = 0

               max_center_candidate = -inf

               while i < len(list_a):

                   if i+1 < len(list_a):

                       pair_sum = list_a[i] + list_a[i+1]

                       if pair_sum >0:

                           current_sum += pair_sum

                           i +=2

                       else:

                           # Check if the current element (i) is better than the previous max_center_candidate.

                           if list_a[i] > max_center_candidate:

                               max_center_candidate = list_a[i]

                           i +=1  # because this element can't form a pair, so break.

                           break

                   else:

                       # i is the last element.

                       if list_a[i] > max_center_candidate:

                           max_center_candidate = list_a[i]

                       i +=1

               # After the loop, check if there are remaining elements.

               # For example, if after processing pairs, i is at len(list_a).

               # Or if during the loop, after breaking, i may be less than len(list_a).

               # So after the loop:

               while i < len(list_a):

                   if list_a[i] > max_center_candidate:

                       max_center_candidate = list_a[i]

                   i +=1

               So this way, any remaining elements after the loop are considered.

               But this approach may not be efficient.

               Alternatively, after processing all possible pairs, the remaining elements (if any) are from i to len(list_a)-1. So the maximum among them is a candidate.

               So the code can collect the maximum of list_a[i:], but that would be O(n) in the worst case, which for k=1e5 could be expensive.

               So to avoid this, we need to track the maximum during the loop.

               So perhaps the code for palindromic groups:

               list_a is sorted in descending order.

               current_sum =0

               max_center = -inf

               i =0

               while i < len(list_a):

                   if i +1 < len(list_a):

                       pair_sum = list_a[i] + list_a[i+1]

                       if pair_sum >0:

                           current_sum += pair_sum

                           i +=2

                       else:

                           # check if list_a[i] is better than current max_center

                           if list_a[i] > max_center:

                               max_center = list_a[i]

                           # check if i+1 can contribute as a single element (if not paired)

                           # but since pair_sum is not positive, adding a single element would only be possible as the center.

                           # so the max_center can be updated with the maximum of the remaining elements.

                           # but how?

                           # after this, any elements after i+1 are also possible candidates.

                           # but since the list is sorted in descending order, the next elements are smaller.

                           # so the maximum possible candidate is list_a[i], or any element after i+1.

                           # but since the list is sorted in descending order, the maximum after i is list_a[i].

                           max_center = max(max_center, list_a[i])

                           # also, check i+1 if there's one.

                           if i+1 < len(list_a):

                               max_center = max(max_center, list_a[i+1])

                           break

                   else:

                       # single element left.

                       if list_a[i] > max_center:

                           max_center = list_a[i]

                       i +=1

               # after the loop, check if there are remaining elements beyond i:

               # no, because the loop increments i.

               # So if we break from the loop, i is pointing to somewhere.

               # So the max_center is the maximum between the current max_center and the remaining elements.

               # but since the list is sorted, the max_center is already the maximum possible.

               # So for example, if the loop breaks at i=2 (after processing two pairs), and there are elements from i=2 onward, the max_center would have already been updated.

               # Wait, not sure.

               Alternatively, after the loop, the remaining elements are from i to len(list_a)-1. The maximum among these is list_a[i] (since sorted in descending order). So the max_center is the maximum between current max_center and list_a[i].

               So after the loop, the code can do:

               if i < len(list_a):

                   if list_a[i] > max_center:

                       max_center = list_a[i]

               So the code for palindromic groups:

                   list_a = sorted(d[s], reverse=True)

                   current_sum = 0

                   max_center = -inf

                   i =0

                   while i < len(list_a):

                       if i+1 < len(list_a):

                           pair_sum = list_a[i] + list_a[i+1]

                           if pair_sum > 0:

                               current_sum += pair_sum

                               i +=2

                           else:

                               # check current i and i+1 (if any) for possible max_center

                               max_center = max(max_center, list_a[i])

                               if i+1 < len(list_a):

                                   max_center = max(max_center, list_a[i+1])

                               # since further pairs will have sum <= current pair_sum (since list is sorted), which is <=0

                               break

                       else:

                           # only one element left

                           max_center = max(max_center, list_a[i])

                           i +=1

                   # after the loop, check if there are elements left beyond i.

                   # no, because we increment i accordingly.

                   # So the max_center is the maximum between the current max_center and any elements not processed.

                   # But after the loop, i is either at len(list_a) or past it.

                   # So no more elements.

                   # Add current_sum to total.

                   total += current_sum

                   # collect max_center as a candidate for the global center.

                   if max_center > global_max_center:

                       global_max_center = max_center

               So, in this code, for each palindromic group, we process pairs, add their sum to total, and track the maximum possible center candidate (which is the maximum of any unpaired elements in the group).

               Then, after processing all groups, the global_max_center is the maximum of all such candidates. If this is positive, add it to the total.

               So the code would look like:

               global_max_center = -inf

               for s in d:

                   if is_palindrome[s]:

                       list_a = sorted(d[s], reverse=True)

                       current_sum = 0

                       group_max_center = -inf

                       i = 0

                       while i < len(list_a):

                           if i +1 < len(list_a):

                               pair_sum = list_a[i] + list_a[i+1]

                               if pair_sum >0:

                                   current_sum += pair_sum

                                   i +=2

                               else:

                                   # consider current i and i+1 as possible centers

                                   group_max_center = max(group_max_center, list_a[i], list_a[i+1] if i+1 < len(list_a) else -inf)

                                   break

                           else:

                               # only one element

                               group_max_center = max(group_max_center, list_a[i])

                               i +=1

                       # after processing all possible pairs:

                       # check if there are elements left after the loop.

                       # for example, if i was incremented by 2 and now is >= len(list_a), then no.

                       # if the loop broke in the middle, then after i, there may be elements.

                       # but since the list is sorted, the group_max_center is already the maximum possible.

                       # but wait, in the case where the loop processed all possible pairs and i is beyond len(list_a), then group_max_center is not updated.

                       # So after the loop, we need to check:

                       # during the loop, for example, if all pairs are taken (sum positive), then group_max_center remains -inf.

                       # So after the loop, if group_max_center is still -inf, then there are no unpaired elements.

                       # Otherwise, there are unpaired elements.

                       # So after the loop, in code:

                       # if i < len(list_a):

                       #    for j in range(i, len(list_a)):

                       #        group_max_center = max(group_max_center, list_a[j])

                       # but since the list is sorted, list_a[i] is the maximum in the remaining elements.

                       if i < len(list_a):

                           group_max_center = max(group_max_center, list_a[i])

                       # then, add current_sum to total.

                       total += current_sum

                       # update global_max_center if group_max_center is larger.

                       if group_max_center > global_max_center:

                           global_max_center = group_max_center

               # after processing all groups, add the global_max_center if it's positive.

               if global_max_center >0:

                   total += global_max_center

               So this code handles all possible palindromic groups and tracks the best possible center.

               Now, putting it all together.

               The code steps:

               1. Read k and n.

               2. Read k lines, for each line, parse s and a_i.

               3. For each s, check if it's a palindrome.

               4. Group all s into a dictionary, where the key is the string, and the value is a list of a_i's.

               5. Process non-palindromic pairs:

                   for each s in the dictionary keys:

                       if s is not a palindrome:

                           s_rev = s[::-1]

                           if s_rev is in the dictionary:

                               if s < s_rev:  # process once per pair.

                                   list_s = sorted(d[s], reverse=True)

                                   list_rev = sorted(d[s_rev], reverse=True)

                                   i = j = 0

                                   while i < len(list_s) and j < len(list_rev):

                                       sum_pair = list_s[i] + list_rev[j]

                                       if sum_pair >0:

                                           total += sum_pair

                                           i +=1

                                           j +=1

                                       else:

                                           break

               6. Process palindromic groups as outlined above.

               7. Finally, check if the total is less than zero, return 0; else, return the total plus the global_max_center (if it's positive).

               Also, note that even if all a_i's are negative, the global_max_center could be negative, but the total would then be max(0, ...).

               So after processing everything, the final answer is max(0, total).

               Wait, no. Because the empty string has beauty 0, which is allowed. So, the total computed after processing all pairs and the possible center is the maximum between the computed total and 0.

               Wait, no. Because the code's total includes all possible pairs and the center. For example, in a case where all a_i's are negative, then the code's total would be 0 (since the empty string is allowed). But the code's code would compute the sum as follows:

               For non-palindromic pairs: no pairs are added (sum_pair is negative).

               For palindromic pairs: no pairs are added. The group_max_center would be the maximum a_i (which is negative). global_max_center would be the maximum of all such group_max_centers, which is negative. So the code would add the global_max_center only if it's positive, but it's not. So the total remains 0.

               So, after all processing, the code should take max(total, 0).

               So, after all processing, the output is max(total, 0).

               So, in code:

               print(max(total, 0))

               So, in the code, after processing all steps, compute the maximum between the total and zero.

               Now, let's think about the code's time complexity.

               For the non-palindromic pairs:

               For each s and s_rev pair, sorting their lists is O(m log m) where m is the number of entries for each string.

               The pairing loop is O(m) for each of the two lists.

               Since the total number of characters is up to 1e5 (n*k ≤1e5), the total number of strings is up to 1e5 (since k can be up to 1e5, but n can be 1, so k can be up to 1e5). So, the time complexity for all non-palindromic pairs is O(m log m) for each pair.

               For palindromic groups:

               Sorting the list for each group is O(m log m). The pairing loop is O(m).

               The worst case is O(k log k) time for all groups.

               So, overall, the code should be acceptable for the constraints.

               Now, implementing this in Python.

               Let's code:

               Read the input.

               is_palindrome can be computed by checking s == s[::-1].

               The code:

               k, n = map(int, input().split())

               from collections import defaultdict

               d = defaultdict(list)

               is_palindrome = {}

               for _ in range(k):

                   s, a = input().split()

                   a = int(a)

                   d[s].append(a)

                   if s not in is_palindrome:

                       is_palindrome[s] = (s == s[::-1])

               total = 0

               # Process non-palindromic pairs.

               processed = set()

               for s in list(d.keys()):

                   if not is_palindrome[s]:

                       s_rev = s[::-1]

                       if s_rev in d:

                           if s < s_rev and s_rev not in processed:

                               list_s = sorted(d[s], reverse=True)

                               list_rev = sorted(d[s_rev], reverse=True)

                               i = j = 0

                               while i < len(list_s) and j < len(list_rev):

                                   sum_p = list_s[i] + list_rev[j]

                                   if sum_p > 0:

                                       total += sum_p

                                       i +=1

                                       j +=1

                                   else:

                                       break

                               processed.add(s)

                               processed.add(s_rev)

                   # else: it's a palindrome, processed later.

               # Process palindromic groups.

               global_max_center = -float('inf')

               for s in d:

                   if is_palindrome[s]:

                       list_a = sorted(d[s], reverse=True)

                       current_sum =0

                       group_max_center = -float('inf')

                       i =0

                       while i < len(list_a):

                           if i+1 < len(list_a):

                               pair_sum = list_a[i] + list_a[i+1]

                               if pair_sum >0:

                                   current_sum += pair_sum

                                   i +=2

                               else:

                                   # check current i and i+1 for possible group_max_center.

                                   group_max_center = max(group_max_center, list_a[i], list_a[i+1])

                                   # since the rest are smaller, no need to proceed.

                                   break

                           else:

                               group_max_center = max(group_max_center, list_a[i])

                               i +=1

                       # after the loop, check for remaining elements.

                       # since list is sorted, the remaining elements are from i onwards.

                       if i < len(list_a):

                           group_max_center = max(group_max_center, list_a[i])

                       # update the global_max_center.

                       if group_max_center > global_max_center:

                           global_max_center = group_max_center

                       total += current_sum

               # Check if we can add the global_max_center.

               if global_max_center >0:

                   total += global_max_center

               # The answer is the maximum between total and 0.

               print(max(total, 0))

               But wait, there's a problem here with the 'processed' set for non-palindromic pairs.

               In the code, when processing a pair s and s_rev, we add both to 'processed' to avoid processing them again. But this is wrong.

               Because for example, if there's another pair t and t_rev, which happen to be the same as s_rev and s, but since s < s_rev, they are processed once. So using 'processed' set is not needed. Because we already check if s < s_rev, which ensures that each pair is processed once.

               For example, when s is 'abb' and s_rev is 'bba', since 'abb' < 'bba' lex order, we process them. When s is 'bba', since s_rev is 'abb', and 'bba' > 'abb' lex order, we do not process them.

               So the 'processed' set is redundant. So the code should remove the 'processed' set.

               The corrected code for non-palindromic pairs:

               for s in list(d.keys()):

                   if not is_palindrome[s]:

                       s_rev = s[::-1]

                       if s_rev in d:

                           if s < s_rev:

                               list_s = sorted(d[s], reverse=True)

                               list_rev = sorted(d[s_rev], reverse=True)

                               i = j =0

                               while i < len(list_s) and j < len(list_rev):

                                   sum_p = list_s[i] + list_rev[j]

                                   if sum_p >0:

                                       total += sum_p

                                       i +=1

                                       j +=1

                                   else:

                                       break

               So the 'processed' set is not needed. Because for each s, we process only if s < s_rev. Thus, each pair is processed once.

               So the code for non-palindromic pairs is fixed.

               Let's test this code against the first example.

               First example:

               non-palindromic pairs:

               s is 'abb' (not palindrome). s_rev is 'bba' (not in the processed set?).

               'abb' < 'bba' lex order → yes.

               list_s is [5,2], sorted descending → [5,2].

               list_rev is [-1], sorted → [-1].

               i=0, j=0: sum 5 + (-1)=4>0 → total becomes 4. i=1, j=1.

               j is now >= len(list_rev) (1 >=1). So loop ends. Total from non-palindromic is 4.

               Then, for palindromic groups:

               'aaa' is a palindrome. a_i's are [-3,7], sorted → [7,-3].

               current_sum starts at 0. i=0.

               i+1 is 1 < 2.

               pair_sum =7 + (-3) =4>0 → current_sum +=4. i becomes 2.

               loop ends. group_max_center is -inf (since no remaining elements). group_max_center is updated to list_a[i] if i < len(list_a). i=2 >= len(list_a) (len is 2), so no. So group_max_center is -inf.

               current_sum is 4 added to total. total becomes 4+4=8.

               'zyz' is a palindrome. a_i is [-4]. sorted → [-4].

               i=0:

               i+1 >= len(list_a) (0+1 >=1). So else clause. group_max_center = max(-inf, -4) →-4.

               i becomes 1. loop ends.

               group_max_center is -4.

               current_sum is 0. added to total (total remains 8). global_max_center is max(-inf, -4) →-4.

               'xyx' is a palindrome. a_i is [4]. sorted → [4].

               i=0:

               i+1 >=1 → else clause. group_max_center is 4. i becomes 1.

               current_sum is 0. added to total (8 remains). global_max_center becomes 4.

               So after processing all palindromic groups, global_max_center is4.

               Then, add 4 to total (8+4=12). So total becomes 12. max(12, 0) is 12.

               Which matches the first example.

               The second example: all 'a's, which are palindromes.

               sorted list_a is [3,2,1].

               current_sum is 3+2=5. i becomes 2. then, i+1 is 3 >=3 → else clause. group_max_center is 1.

               current_sum is5 added to total. global_max_center is1.

               After processing, total is5. Then add 1 →6. max(6,0) →6.

               Third example: two 'abcde's. Not palindromes. Their reverse is 'edcba', which is not present. So no pairs processed. Total is 0. global_max_center is -inf. So output is 0.

               So the code works.

               Now, code for the problem.
</think>

```python
k, n = map(int, input().split())
from collections import defaultdict

d = defaultdict(list)
is_palindrome = {}

for _ in range(k):
    s, a = input().split()
    a = int(a)
    d[s].append(a)
    if s not in is_palindrome:
        is_palindrome[s] = (s == s[::-1])

total = 0

# Process non-palindromic pairs
for s in list(d.keys()):
    if not is_palindrome[s]:
        s_rev = s[::-1]
        if s_rev in d and s < s_rev:
            list_s = sorted(d[s], reverse=True)
            list_rev = sorted(d[s_rev], reverse=True)
            i = j = 0
            while i < len(list_s) and j < len(list_rev):
                sum_p = list_s[i] + list_rev[j]
                if sum_p > 0:
                    total += sum_p
                    i += 1
                    j += 1
                else:
                    break

# Process palindromic groups
global_max_center = -float('inf')
for s in d:
    if is_palindrome[s]:
        list_a = sorted(d[s], reverse=True)
        current_sum = 0
        group_max_center = -float('inf')
        i = 0
        while i < len(list_a):
            if i + 1 < len(list_a):
                pair_sum = list_a[i] + list_a[i + 1]
                if pair_sum > 0:
                    current_sum += pair_sum
                    i += 2
                else:
                    group_max_center = max(group_max_center, list_a[i], list_a[i + 1])
                    break
            else:
                group_max_center = max(group_max_center, list_a[i])
                i += 1
        # Check remaining elements after loop
        if i < len(list_a):
            group_max_center = max(group_max_center, list_a[i])
        if group_max_center > global_max_center:
            global_max_center = group_max_center
        total += current_sum

if global_max_center > 0:
    total += global_max_center

print(max(total, 0))
```