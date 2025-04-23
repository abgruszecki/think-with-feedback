<think>
Okay, let's try to solve this problem. The problem is about finding the minimum number of changes needed to a string of directions so that the total movement ends at the origin. The directions can be L, R, U, D. Each character can be changed to any of these, and we need the minimal edits.

First, let's think about the necessary conditions. The movement ends at the origin if the total left-right movement cancels out and the total up-down movement cancels out. So, the sum of R and L directions (with R being +1, L being -1) should be zero, and similarly for U and D (U being +1, D being -1). But since we can change characters, the question is how to adjust the counts of these directions such that the net movement is zero, with minimal changes.

Let me break it down. Let's say the original counts are:

count_L: number of L's in the string
count_R: number of R's
count_U: number of U's
count_D: number of D's

But since we can replace any character, the actual counts can be adjusted. However, the total number of characters (n) is fixed. Let's denote the total length as n.

So, after replacement, we have new counts:

new_L, new_R: these contribute to the horizontal movement. So, (new_R - new_L) must equal zero. Wait, no. Wait, each R adds +1 (right), L adds -1 (left). So the horizontal movement is (R_count - L_count) + (other directions that were changed to R or L? No, wait: all characters are part of either horizontal or vertical movement. For example, a character could be changed to R, contributing +1 to horizontal, or to U, contributing +1 to vertical, etc.

So, the problem is to assign each character to be either L/R (horizontal) or U/D (vertical), such that the sum of horizontal directions (R - L) is zero, and the sum of vertical directions (U - D) is zero. Wait no: each character can be any direction, but the total sum of all horizontal directions (R and L) must be even? Wait, no. Let me think again.

The total displacement is (horizontal, vertical), where horizontal is (number of R) - (number of L), and vertical is (number of U) - (number of D). We need both to be zero.

But each character can be changed to any direction. So, for each character, we can choose which direction to assign. The goal is to choose directions such that the sum of R-L is zero, sum of U-D is zero, and the number of changes (from the original) is minimized.

Wait, but the problem statement says that the trident can replace any character with any direction. So, the original directions don't matter except for the count of changes needed. Wait, wait, no. Because, if a character is already, say, R, and we change it to R again, that's zero changes. So, the minimal changes required depends on how many characters we can leave as they are, while adjusting the counts to meet the required conditions.

Wait, the problem is to modify some characters to make the total displacement (0,0), and the minimal number of changes. So, the initial counts of L, R, U, D are known, but we can change any of them. For example, if the original string is "RRU", then after changes, we can have "RLD", which would sum to R-L (1) and U-D (-1), but that's not zero. Hmm, but how?

Alternatively, maybe the problem is that the sum of all horizontal and vertical movements must be zero. Let's model this.

Let me think: each character in the string can be assigned to contribute either to horizontal or vertical direction. But once assigned, the direction (like left/right for horizontal) will determine the sum. But the problem allows any direction. So, for each character, we can choose which direction to take (L, R, U, D), and the sum of all the horizontal (R-L) must be zero, and the vertical (U-D) must be zero.

But how to model this. Because the sum of all horizontal movement (R-L) is (R_count - L_count) and vertical is (U_count - D_count). But we can choose how to split the characters into horizontal and vertical directions.

But perhaps the key is that the total horizontal steps plus vertical steps equals the length of the string. Because each character contributes to either horizontal or vertical.

Wait, but each character is assigned to be either a horizontal (L/R) or vertical (U/D) direction. So, the total number of horizontal steps is h = a + b, where a is the number of R and b the number of L. Then the net horizontal is (a - b). Similarly, the vertical steps is v = c + d (c U's, d D's), net vertical is (c - d). And h + v = n.

But we need (a - b) = 0 and (c - d) = 0. So, a = b and c = d.

But since h = a + b = 2a, which must be even. Similarly, v = 2c must be even. And since h + v = n, the sum of two even numbers (h and v) must be equal to n. So, n must be even. Otherwise, it's impossible.

Wait, that's a crucial observation. Because if n is odd, then h and v are both even (since h = 2a, v = 2c), but h + v = even + even = even. But if n is odd, then even + even can't be equal to an odd n. So, in that case, it's impossible to split into h and v such that their sum is n. Therefore, the first check is: if the length of the string is odd, then output -1.

Wait, but let's see the first example:

Input: RRU (length 3, which is odd). Output is -1, which aligns with this observation.

Yes. So, the first thing to check is if the length of the string is even. If it's odd, output -1.

So, the first step is to check if n is even. If not, return -1.

Assuming n is even, we need to split the string into h and v steps, where h is even (since h = 2a) and v is even (v = 2c). And h + v = n.

But h and v can be any even numbers adding up to n. For example, if n=4, possible splits are h=0 and v=4 (but then h must be 0, which would require a net of 0, which is possible if all vertical steps are split into U and D equally). Or h=2 and v=2, etc.

But how to model this. Wait, perhaps the minimal changes required can be found by trying all possible splits of h and v (even numbers adding to n), compute the minimal changes required for each split, and then take the minimal among all possible splits.

But how?

Alternatively, perhaps the optimal split is to have h and v as even numbers, and in such a way that the sum of their required directions can be achieved with minimal changes.

Wait, perhaps for each possible split into h and v steps (horizontal and vertical), we can compute the minimal number of changes required to have a net of zero in both directions. Then, among all possible splits (h and v even, h + v = n), select the split that gives the minimal total changes.

But the problem is that h and v can be any even numbers adding up to n. For example, if n is 4, possible splits are (0,4), (2,2), (4,0). For each split, we need to assign h characters to horizontal directions (L/R) and v to vertical (U/D). Then, for horizontal, the net must be zero, so the number of R and L must be equal. Similarly for vertical. But how to model that.

Alternatively, perhaps the minimal changes can be found as follows:

Let the number of horizontal steps (h) be any even number. Then, the vertical steps (v) must be n - h, which must also be even. So, h can range from 0 to n in steps of 2, and for each such h, compute the minimal number of changes required.

But how to compute the minimal changes for a given h?

Wait, perhaps the problem can be rephrased. For a given h, which is even, the horizontal steps need to contribute 0 net movement. So, in the horizontal directions, we need exactly h/2 R and h/2 L. Similarly, for the vertical steps (v = n - h, which must be even), we need v/2 U and v/2 D.

So, for each h (even), we can compute the minimal number of changes required to select h characters (from the original string) to be in horizontal directions (R or L) and the remaining (n-h) in vertical directions (U or D), such that in horizontal, the count of R and L is equal (h/2 each), and in vertical, the count of U and D is equal (v/2 each). But how?

Wait, perhaps for a given h and v, the problem can be broken down into:

- How many of the original R and L can be used in the horizontal steps (which are h in total, requiring exactly h/2 R and h/2 L). So, any original R or L can be used as R or L (without change), but if they are used in the vertical steps, they need to be changed to U or D, which counts as a change.

Alternatively, perhaps the approach is to decide for each character in the string whether to assign it to horizontal or vertical movement. Then, within those assignments, choose directions (R/L or U/D) such that the counts meet the required even splits. But this seems complex.

Alternatively, perhaps the problem can be viewed as follows:

The minimal changes required is the sum of:

- The number of characters that are not R or L in the horizontal group (since they need to be changed to R or L).

- Plus the number of characters that are not U or D in the vertical group (since they need to be changed to U or D).

But that's not exactly right. Because, for example, a character that is R can be kept as R (so no change) if it's in the horizontal group, or it can be changed to U or D (so a change) if it's in the vertical group.

But the key is to choose which characters are assigned to horizontal and vertical groups such that:

- The total horizontal group has h characters (h must be even).

- The total vertical group has v = n - h characters (v must be even).

Within the horizontal group, exactly h/2 R's and h/2 L's.

Within the vertical group, exactly v/2 U's and v/2 D's.

The minimal number of changes is the sum over all characters not matching their assigned direction.

But how to model this.

Alternatively, for a given h (even), the minimal changes would be:

For the horizontal group: select h characters from the original string. Among these h, how many can be R or L (since they can be used as R or L without change). The rest (non-R/L characters) in the horizontal group must be changed to R or L. But since the horizontal group needs exactly h/2 R and h/2 L, we can take the maximum possible of R and L in the original string that can contribute to the required counts.

Alternatively, perhaps the optimal way is to take as many R and L as possible in the horizontal group, but this is getting complicated.

Let me think of another approach. Let's consider that the problem requires that the total number of R minus L must be zero (so even number of horizontal steps, split equally between R and L) and same for U and D.

So, the sum of all R and L must be even (since h must be even), and the same for U and D (sum even? No, v is even, so the total U and D is even, and their counts must be equal. So, for each split h and v (even), we can model the problem as follows.

But perhaps the key insight is that the minimal number of changes depends on the maximum possible matches we can have in the required direction counts.

Alternatively, let's think of it as: for each possible h (even), compute the maximum possible number of characters that can be kept (without change) in the horizontal group (as R or L) and vertical group (as U or D), and then subtract this sum from the total n to get the minimal changes required.

So for each h:

max_keep = (number of R and L in horizontal group) + (number of U and D in vertical group).

But how to compute that.

Let's denote:

original_R: number of R's in the original string.

original_L: number of L's.

original_U: number of U's.

original_D: number of D's.

Suppose we choose h characters to be in the horizontal group (must be even). The horizontal group needs exactly h/2 R and h/2 L. So, the maximum number of R and L that can be kept in the horizontal group is min(original_R, h/2) + min(original_L, h/2). But wait, if original_R is more than h/2, then the horizontal group can take h/2 R. Similarly for L. But perhaps the sum of original_R and original_L could be greater than h. But in that case, the maximum possible is h (since the horizontal group has h characters, and each can be R or L, but we need exactly h/2 R and h/2 L). So the maximum possible is min(original_R + original_L, h/2 + h/2) = min(original_R + original_L, h).

Wait, no. Because in the horizontal group, the sum of R and L must be exactly h. And among them, the number of R must be h/2, L must be h/2. So, the maximum number of original R and L that can be used in the horizontal group is the sum of the minimum between original_R and h/2 (since we need exactly h/2 R's), plus the minimum between original_L and h/2 (since we need h/2 L's). So, that's min(original_R, h/2) + min(original_L, h/2). But if original_R is less than h/2, we can't take enough R's. So, the sum here is (available R + available L) but capped by h.

Wait, for example, if h is 4 (so h/2=2). original_R is 3, original_L is 1. Then, in the horizontal group, we can take 2 R's and 1 L. Then, the remaining 1 character in the horizontal group (since 2+1=3 < 4) must be taken from other directions (U, D) and changed to R or L. But that would require changes.

So, the maximum number of R and L that can be kept in the horizontal group is the sum of the minimum between original_R and h/2, and original_L and h/2. The remaining (h - (sum)) characters in the horizontal group must be changed to R or L, which counts as a change.

Similarly, for the vertical group (v = n - h), which must be even. We need exactly v/2 U's and v/2 D's. So, the maximum number of U and D that can be kept is min(original_U, v/2) + min(original_D, v/2). The rest in the vertical group (v - (sum)) must be changed, which counts as a change.

Additionally, for the characters not in the horizontal group (i.e., in the vertical group), the original R and L are considered as part of the vertical group. But since vertical group can only have U or D, any R or L in the vertical group must be changed to U or D, which counts as a change.

Wait, no. The vertical group is supposed to consist of U and D. So, any character in the vertical group that is not U or D (i.e., R or L) must be changed to U or D. Similarly, for the horizontal group, any character not R or L must be changed to R or L.

So, the total changes needed for a given h is:

changes = (h - (min(R, h/2) + min(L, h/2))) + (v - (min(U, v/2) + min(D, v/2))) + (other characters in the vertical group that are R/L) + (other characters in the horizontal group that are U/D).

Wait, this is getting complicated. Maybe I should model this as:

Total changes = (number of characters in horizontal group that are not R or L) + (number of characters in horizontal group that are R or L but exceed h/2 R or L) + (number of characters in vertical group that are not U or D) + (number of characters in vertical group that are U or D but exceed v/2 U or D).

Alternatively, perhaps the minimal changes for a given h is:

For the horizontal group:

- The maximum possible R and L we can use is min(R, h/2) + min(L, h/2). The remaining (h - (min(R, h/2) + min(L, h/2))) characters in the horizontal group must be changed to R or L. Also, any R or L in the horizontal group beyond what's needed counts as a change. Wait, no. Because if original_R is larger than h/2, then in the horizontal group, we can only take h/2 R's. The rest of the R's (original_R - h/2) must be in the vertical group and changed to U or D.

Similarly, for L's.

So, the changes for horizontal group are:

In the horizontal group:

- For R's: if there are more than h/2 R's, then (original_R_in_horizontal) = h/2, and the rest (original_R - h/2) will be in the vertical group and must be changed.

But this is getting a bit too involved. Let's model it step by step.

For a given h (even):

horizontal_group_size = h.

vertical_group_size = v = n - h (must be even as well).

In the horizontal group, we need exactly h/2 R and h/2 L.

In the vertical group, exactly v/2 U and v/2 D.

The steps to compute the minimal changes for this h are:

1. For the horizontal group:

   a. The maximum R we can use is min(original_R, h/2). Let's call this R_used.

   b. The maximum L we can use is min(original_L, h/2). Let's call this L_used.

   c. The total R and L used in horizontal group is R_used + L_used.

   d. The remaining horizontal positions (h - (R_used + L_used)) must be filled by other characters (U, D) from the original string. These are changes, because they are not R or L and must be changed to R or L.

   e. Also, any R or L in the original string that are not used in the horizontal group are part of the vertical group and must be changed to U or D. So, the R and L in the vertical group are (original_R - R_used) + (original_L - L_used). Each of these must be changed.

2. For the vertical group:

   a. The maximum U we can use is min(original_U, v/2). Let's call this U_used.

   b. The maximum D we can use is min(original_D, v/2). Let's call this D_used.

   c. The total U and D used in vertical group is U_used + D_used.

   d. The remaining vertical positions (v - (U_used + D_used)) must be filled by other characters (R, L) from the original string. These are changes.

   e. Any U or D in the original string that are not used in the vertical group are part of the horizontal group and must be changed to R or L, but since we already considered the horizontal group's changes, this is already accounted for.

Wait, maybe not. Let's think again.

The horizontal group is of size h, and the vertical group is of size v. All characters are in either group.

In the horizontal group, any character that is not R or L must be changed. Also, the R and L in the horizontal group can be used up to h/2 each. Any excess R or L (beyond h/2) must be in the vertical group, where they are changed to U or D.

In the vertical group, any character that is not U or D must be changed. Also, the U and D in the vertical group can be used up to v/2 each. Any excess U or D (beyond v/2) must be in the horizontal group, where they are changed to R or L.

This seems quite complex. Maybe a better way is to model the minimal changes as:

changes = (number of characters not in horizontal group that are R or L) + (number of characters not in vertical group that are U or D) + (number of characters in horizontal group that are not R or L) + (number of characters in vertical group that are not U or D) - but this might not be correct.

Alternatively, the total changes needed can be calculated as:

changes = (h - (number of R and L used in horizontal group)) + (number of R and L not used in horizontal group) + (v - (number of U and D used in vertical group)) + (number of U and D not used in vertical group).

Wait, perhaps this is the right approach.

Because:

- For the horizontal group (size h):

   - We can use up to h/2 R and h/2 L.

   - The number of R and L that can be used in the horizontal group is (R_used + L_used) = min(R, h/2) + min(L, h/2).

   - The remaining characters in the horizontal group (h - (R_used + L_used)) must be non-R/L characters (U/D) that are changed to R/L. Each of these contributes 1 change.

   - Also, any R or L not used in the horizontal group are in the vertical group, which requires them to be changed to U/D. So, the number of R and L not used in the horizontal group is (original_R - R_used) + (original_L - L_used). Each of these contributes 1 change.

- For the vertical group (size v):

   - Similarly, U_used = min(U, v/2), D_used = min(D, v/2).

   - The number of U and D that can be used in the vertical group is U_used + D_used.

   - The remaining characters in the vertical group (v - (U_used + D_used)) are non-U/D characters (R/L) that are changed to U/D. Each contributes 1 change.

   - Also, any U or D not used in the vertical group are in the horizontal group, which requires them to be changed to R/L. But this is already accounted for in the horizontal group's calculation.

Wait, perhaps the total changes can be expressed as:

changes = (h - (R_used + L_used)) + (original_R + original_L - (R_used + L_used)) ) + (v - (U_used + D_used)) + (original_U + original_D - (U_used + D_used)) )

But that would be:

= [h - (R_used + L_used)] → number of non-R/L in horizontal group (changes)

+ [original_R + original_L - (R_used + L_used)] → R/L not used in horizontal group (must be in vertical group, which requires changing to U/D → each is a change)

+ [v - (U_used + D_used)] → number of non-U/D in vertical group (changes)

+ [original_U + original_D - (U_used + D_used)] → U/D not used in vertical group (must be in horizontal group → changed to R/L → changes)

But this is adding all possible changes, but some of these may be overlapping. For example, the U/D not used in the vertical group are in the horizontal group, and their changes are already counted in the first part (h - (R_used + L_used)), since those U/D in the horizontal group are not R/L.

So perhaps this formula is correct.

But let's see:

Each character in the string contributes 1 change if:

- It's in the horizontal group and is not R or L (must be changed to R/L).

OR

- It's in the vertical group and is not U or D (must be changed to U/D).

Additionally, even if it's R/L, but in the vertical group, it's a change. Similarly, U/D in the horizontal group is a change.

So, the total changes is:

sum over all characters:

   if in horizontal group and (char is R or L) → no change (if they are used as R or L)

   else if in horizontal group → change (1)

   if in vertical group and (char is U or D) → no change (if used as U or D)

   else if in vertical group → change (1)

Wait, but this is not considering the required counts of R and L in the horizontal group. For example, even if a character is R, if it's in the horizontal group but not part of the required R count (h/2), then it must be changed to L. Which is a change.

So, this approach is getting too complicated.

Alternative approach: For a given h (even), the minimal changes required is (number of changes to make the horizontal group have exactly h/2 R and h/2 L) + (number of changes to make the vertical group have exactly v/2 U and v/2 D).

But how to compute that.

Let's model the problem as follows:

For each possible h (even), compute:

- The horizontal group must have h characters. Of these, exactly h/2 are R and h/2 are L.

- The vertical group must have v = n - h characters. Exactly v/2 are U and v/2 are D.

The minimal changes required for this split is:

The sum of:

- The number of R and L in the original string that are not used in the horizontal group (they must be changed to U/D).

- The number of U and D in the original string that are not used in the vertical group (they must be changed to R/L).

- Plus, any other characters (like original R or L that are in the vertical group, or U/D in horizontal group) that need to be changed.

Wait, perhaps the minimal changes can be computed as:

changes = (total R + L - (h/2 * 2)) + (total U + D - (v/2 * 2)) + (other characters?)

No, that's not right. Because (h/2 * 2) is h, which is the size of the horizontal group. So (total R + L) is the number of R and L in the original string. If we use h/2 R and h/2 L, then the R and L used are h. The remaining (R + L - h) must be in the vertical group and thus changed.

But the original R and L may not be sufficient. For example, if original R is 5 and h is 4 (h/2 is 2), then in the horizontal group, we can use 2 R and 2 L (if original L is >=2). Otherwise, we have to use as much as possible.

So, the minimal changes for a given h is the sum of:

- The number of R and L not used in the horizontal group → (original_R + original_L) - (R_used + L_used) → but R_used = min(original_R, h/2), L_used = min(original_L, h/2). So, R_used + L_used can be up to h (if original_R + original_L >= h). Otherwise, it's original_R + original_L.

Wait, but if original_R is 3, original_L is 1, h is 4 (h/2 is 2). Then R_used is 2, L_used is 1. Total used in horizontal is 3. So, the horizontal group needs 4 characters. So 4-3=1 characters must be taken from U/D and changed to R/L → 1 change. Also, the remaining R (3-2=1) and L (1-1=0) must be in the vertical group, which contributes 1 (R) changes (since vertical group can't have R's).

So, total changes for horizontal part is 1 (from horizontal group) + 1 (from vertical group's R) = 2.

But according to the formula (original_R + original_L - (R_used + L_used)) = (3 +1) - (2+1) = 1. So, changes from vertical group's R and L is 1. Then, changes from horizontal group is (h - (R_used + L_used)) = 4-3=1. Total changes for horizontal part is 1+1=2. Which matches.

So, the formula for the horizontal changes is:

horizontal_changes = (h - (R_used + L_used)) + (original_R + original_L - (R_used + L_used)).

Similarly, vertical_changes = (v - (U_used + D_used)) + (original_U + original_D - (U_used + D_used)).

So, the total changes for a given h is horizontal_changes + vertical_changes.

But then, the problem is to compute this for all possible even h and find the minimal changes.

So, the steps are:

1. Check if n is even. If not, return -1.

2. For all even h from 0 to n, step by 2:

   a. v = n - h. Must be even. So h must be even and v even.

   b. For horizontal:

      R_used = min(original_R, h//2)

      L_used = min(original_L, h//2)

      sum_rl_used = R_used + L_used

      horizontal_changes = (h - sum_rl_used) + (original_R + original_L - sum_rl_used)

   c. For vertical:

      U_used = min(original_U, v//2)

      D_used = min(original_D, v//2)

      sum_ud_used = U_used + D_used

      vertical_changes = (v - sum_ud_used) + (original_U + original_D - sum_ud_used)

   d. total_changes = horizontal_changes + vertical_changes.

   e. Keep track of the minimal total_changes.

3. After checking all h, if any possible h leads to a valid solution (i.e., sum_rl_used <= h and sum_ud_used <=v), then return the minimal total_changes. Otherwise, return -1.

Wait, but for some h, the sum_rl_used can be less than h, but the remaining (h - sum_rl_used) can be filled with U/D converted to R/L. So, even if original_R and original_L are very small, the h can be possible.

But according to the formula, the sum_rl_used is min(original_R, h/2) + min(original_L, h/2). For example, if h is 4, and original_R=0, original_L=0, then sum_rl_used=0. So horizontal_changes is (4-0) + (0+0 -0) =4. So, all 4 characters in the horizontal group are non-R/L and must be changed to R/L. Then, in the vertical group, there are v =n-4 characters. So, the formula allows for any h as long as h is even.

But what about the sum_rl_used can be any value up to h. So, the formula accounts for all possibilities. Thus, the code can iterate over all possible even h and calculate the total_changes using the formula.

So, the approach is:

- Precompute the counts of R, L, U, D in the original string.

- Check if n is even. If not, return -1.

- Iterate h in even numbers from 0 to n (inclusive), step 2.

   - For each h, compute v =n-h. If v is even (which it will be since n is even and h is even), proceed.

   - Compute horizontal_changes and vertical_changes as per the formula.

   - Keep track of the minimal changes.

- Return the minimal changes found. If no possible h leads to a solution (like in the first example, where n=3 is odd → return -1), but since we checked n even, perhaps in some cases even h may not allow a solution (like when sum_rl_used + sum_ud_used + ... is not possible). But according to the formula, even if there are not enough R/L or U/D, the changes will account for converting other characters. For example, if h=4, sum_rl_used is 0 (no R or L in original), then all 4 horizontal characters must be converted to R/L. So the code will compute that.

But why would there be a case where even after considering all h, there's no solution? For example, if n is even, but after all possible splits h, the sum of horizontal and vertical changes is impossible? Like when the required directions can't be achieved.

Wait, no. Because the code allows for any h even. For example, even if the original string has no R/L, but you choose h=0. Then, all characters are in the vertical group. So, the vertical group must have even size. Then, for the vertical group, we need exactly v/2 U and v/2 D. So, changes are (v - (U_used + D_used)) + (original_U + original_D - (U_used + D_used)). For example, if the original string has 2 U and 0 D, and v=4. Then U_used = 2 (since min(2, 2)), D_used=0. So sum_ud_used=2. vertical_changes is (4-2) + (2+0 -2) = 2 + 0 = 2. So the vertical group needs 2 more characters (which are non-U/D → R/L in the original string) which must be changed to U/D. But in the original string, those R/L are in the vertical group, so they must be changed. So, this is possible.

Wait, but in this example, the vertical group must have exactly 2 U and 2 D. So, if original has 2 U and 0 D, then in the vertical group, we use 2 U (max possible) and 0 D. So the remaining 2 characters must be changed to D. So the total changes are 2 (from the 2 R/L in the vertical group) + 0 (from the U/D not used). So total changes are 2, which matches the formula.

So, in this case, the formula works. So the code will find a solution, even if it requires changing all the R/L to U/D.

Thus, the code will always find a solution if n is even, because for each even h, the formula allows for all possible combinations. So, the answer is possible unless n is odd.

Wait, but there's the first example where n=3 is odd, which returns -1. But what if n is even but there's no way to split the characters to get a valid configuration? For example, let's say n=2, and the original string is "RR". Then, h can be 0, 2.

If h=0: vertical group size 2. Need 1 U and 1 D. Original has 0 U and 0 D. So sum_ud_used=0. vertical_changes is (2-0) + (0+0-0) → 2. So changes is 2. So the vertical group has 2 characters (both R's in the original), which must be changed to 1 U and 1 D. So changes are 2.

If h=2: horizontal group needs 1 R and 1 L. Original has 2 R's. sum_rl_used = min(2,1) + min(0,1) →1 +0=1. horizontal_changes = (2-1) + (2+0 -1) →1 +1 →2. vertical group size 0 → vertical changes 0. So total changes 2. So the answer is 2.

But the desired displacement is zero. So in this case, changing the two R's to R and L (but original has two R's → can change one R to L (1 change), the other remains R. So net displacement is zero. But according to the formula, the changes are 2. Wait, why?

Wait, in the h=2 case:

sum_rl_used is min(2,1) + min(0,1) →1 +0=1.

horizontal_changes is (2-1) =1 (from U/D in the horizontal group → but original has no U/D, so horizontal group has two R's. So sum_rl_used is 1 (R_used=1, L_used=0). So the horizontal group has 1 R and 1 L. So one R is kept, another R is changed to L. So changes are 1. But according to the formula, horizontal_changes is (2-1) →1 (for non-R/L in horizontal group) → but there are none, so sum_rl_used is 1 (R_used=1, L_used=0), so horizontal group is 1 R and 0 L. But the horizontal group needs 1 R and 1 L. So one of the R's must be changed to L.

So the formula gives horizontal_changes = (h - sum_rl_used) → 2-1=1 (this is the number of non-R/L characters in the horizontal group, which is zero in this case). Then, the second part is (original_R + original_L - sum_rl_used) → 2+0-1=1. So total horizontal_changes is 1+1=2.

But why?

Because in the horizontal group:

- R_used is 1 (min(2, 1)), L_used is 0 (min(0,1)).

- So sum_rl_used =1. So the horizontal group has 1 R and 0 L. But h is 2, so the remaining 1 character must be filled by non-R/L (but original has none). So that character is changed to L. So change count is 1 (for that character).

But the original has two R's. One is used in the horizontal group, the other R is in the vertical group (which is size 0). Wait, no. If h=2, then vertical group is 0. So all characters are in the horizontal group. So the two R's are in the horizontal group.

But for the horizontal group, we need 1 R and 1 L. So in the horizontal group, one R is kept, the other must be changed to L. So changes are 1.

But according to the formula, horizontal_changes is (h - sum_rl_used) + (original_R + original_L - sum_rl_used) → (2-1) + (2+0-1) →1 +1=2. Which is wrong.

Wait, this suggests that the formula is incorrect.

So, the formula gives 2 changes in the horizontal group, but the actual required changes are 1.

Hmm, this indicates a problem with the formula. So the approach is flawed.

So, what's wrong with the formula?

Let's re-express the formula:

horizontal_changes = (h - sum_rl_used) → number of non-R/L characters in the horizontal group (they have to be changed to R/L)

plus (original_R + original_L - sum_rl_used) → number of R/L characters not used in the horizontal group (they are in the vertical group and have to be changed to U/D).

In the example where original string is "RR", h=2:

sum_rl_used = 1 (R_used=1, L_used=0).

h - sum_rl_used = 2-1=1 → this counts the number of non-R/L characters in the horizontal group. But in this case, all are R's. So this part is 1, but that's incorrect. There are no non-R/L characters in the horizontal group. So this term is 0, but the formula gives 1.

So the formula is wrong.

Ah, I see the problem. The term (h - sum_rl_used) is intended to represent the number of non-R/L characters in the horizontal group, but sum_rl_used is the number of R and L used in the horizontal group. But sum_rl_used can be less than h even if all characters in the horizontal group are R/L. For example, if there are not enough R and L to fill the required counts.

Wait, in the example:

original_R=2, original_L=0. h=2. sum_rl_used = min(2, 1) + min(0, 1) =1 +0=1. So sum_rl_used is 1. So in the horizontal group, there are 1 R and 0 L. But since the horizontal group needs 1 R and 1 L, the remaining character must be L. So even though the original characters are all R's, one of them has to be changed to L. So changes for the horizontal group is 1.

But according to the formula:

horizontal_changes = (h - sum_rl_used) → 2-1=1 (but there are no non-R/L in the horizontal group) → this term is wrong.

The formula assumes that (h - sum_rl_used) is the number of non-R/L characters in the horizontal group. But in reality, sum_rl_used can be less than h even if all characters in the horizontal group are R/L, but you can't split them into R and L.

So the formula is incorrect.

This indicates that the approach is flawed, and the formula does not correctly capture the required changes.

So, this requires a different approach.

Alternative idea:

For the horizontal group, the required number of R and L is h/2 each.

The maximum R that can be used is min(original_R, h/2).

Similarly for L.

The total number of R and L in the horizontal group is R_used + L_used.

If R_used + L_used < h, then the remaining (h - R_used - L_used) must be filled with other characters (U/D) which are changed to R or L. Each such character is a change.

Additionally, in the horizontal group, the R and L used are R_used and L_used, but they need to be exactly h/2 each. So, if R_used < h/2, then we need to add (h/2 - R_used) L's in the horizontal group. Wait, no. For example, if we have h=2 (h/2=1), and R_used=1 and L_used=0. Then the horizontal group has 1 R and 1 character which must be L. But since the original L is 0, that character must be changed to L. So the number of changes in the horizontal group is 1.

So the formula for the horizontal changes is:

horizontal_changes = (number of R in horizontal group that are beyond R_used) + (number of L in horizontal group beyond L_used) + (number of non-R/L in horizontal group).

Wait, no. The horizontal group has R_used R's and L_used L's. The required is h/2 R and h/2 L. So, the changes in the horizontal group are:

(number of R's in horizontal group - R_used) → which must be R's that are not used (but in this case, R_used is min(original_R, h/2), so if original_R > h/2, then R_used is h/2, and any R's in the horizontal group beyond h/2 must be changed to L. So this part is (original_R_in_horizontal - R_used) → which is (R_used + ...? Not sure.

This is getting too complicated. Perhaps we need to model the changes in the horizontal group as:

The horizontal group needs h/2 R and h/2 L.

The number of R in the horizontal group is R_used = min(original_R, h/2).

The number of L in the horizontal group is L_used = min(original_L, h/2).

But the total required R and L is h/2 each. So:

changes in horizontal group for R: (h/2 - R_used) → because we need h/2 R's, but have R_used. So (h/2 - R_used) R's must be obtained by changing other characters (L, U, D) to R.

Similarly for L: (h/2 - L_used) L's must be obtained by changing other characters to L.

Additionally, any R or L in the horizontal group that are not needed must be changed. For example, if there are more R's than h/2, but how can that happen? Because R_used is min(original_R, h/2), so if original_R >= h/2, then R_used = h/2. So the R's in the horizontal group are exactly h/2.

So, no, the R_used is the maximum possible R's that can be used without exceeding h/2.

So the changes required for R in the horizontal group are (h/2 - R_used), and for L similarly (h/2 - L_used).

Additionally, any character in the horizontal group that is not R or L must be changed to R or L.

The number of non-R/L characters in the horizontal group is (h - R_used - L_used).

So, the total changes in the horizontal group is:

(h/2 - R_used) + (h/2 - L_used) + (h - R_used - L_used).

Which simplifies to:

(h/2 - R_used) + (h/2 - L_used) = h/2*2 - (R_used + L_used) = h - (R_used + L_used).

Adding (h - R_used - L_used) gives:

h - (R_used + L_used) + (h - R_used - L_used) = 2*(h - R_used - L_used).

But that's for the horizontal group. But this can't be right. For example, in the previous example where original_R=2, h=2, R_used=1 (h/2=1), L_used=0:

changes in horizontal group would be (1-1) + (1-0) →0 +1=1. Plus the non-R/L in the group (h - R_used - L_used=2-1-0=1). So total 1+1=2. But the correct answer is 1.

So this approach is also incorrect.

Alternative Idea:

Perhaps the minimal changes for the horizontal group is (h/2 - R_used) + (h/2 - L_used) + (number of non-R/L in horizontal group).

So for the example:

R_used = 1, L_used=0.

non-R/L in horizontal group: 0.

So changes are (1-1) + (1-0) + 0 → 0 +1 +0=1. Which is correct.

So, the formula for horizontal changes is:

horizontal_changes = (h/2 - R_used) + (h/2 - L_used) + (number of non-R/L in horizontal group).

The non-R/L in horizontal group is (h - (R_used + L_used)).

But how to find the number of non-R/L in the horizontal group.

Assuming that the horizontal group is selected to include as many R and L as possible.

The horizontal group will consist of R_used R's and L_used L's. The remaining characters in the horizontal group are chosen from the other characters (U and D). So, the number of non-R/L in the horizontal group is (h - R_used - L_used).

Thus, the formula for horizontal changes is:

horizontal_changes = (h/2 - R_used) + (h/2 - L_used) + (h - R_used - L_used).

But R_used = min(original_R, h/2).

L_used = min(original_L, h/2).

So, for example:

original_R=2, original_L=0, h=2.

R_used=1, L_used=0.

horizontal_changes = (1-1) + (1-0) + (2-1-0) →0 +1 +1=2. Which is still incorrect.

But the correct answer is 1 change: changing one R to L.

Hmm, this is conflicting. What is the correct way to model this.

Let's think differently. For the horizontal group, we need exactly h/2 R and h/2 L.

Each character in the horizontal group contributes to a change in the following cases:

- If it's an R, but there are more than h/2 R's in the horizontal group → must be changed to L.

- If it's an L, but there are more than h/2 L's in the horizontal group → must be changed to R.

- If it's a U or D → must be changed to R or L.

So, the changes for the horizontal group are:

number of R's in horizontal group exceeding h/2 → max(0, R_in_horizontal - h/2) +

number of L's in horizontal group exceeding h/2 → max(0, L_in_horizontal - h/2) +

number of U/D in horizontal group.

But R_in_horizontal can't exceed h/2 because R_used is min(original_R, h/2). So, R_in_horizontal is R_used. Similarly for L.

So, R_in_horizontal can be at most h/2. Similarly for L.

So, the changes for R and L in the horizontal group are (h/2 - R_used) and (h/2 - L_used), respectively. Because we need to get h/2 R and L, but we can only use R_used and L_used from the original. The rest must be changed from other characters (U/D) to R/L.

Additionally, the U/D in the horizontal group are (h - R_used - L_used), which must be changed to R or L.

So, the total horizontal changes are:

(h/2 - R_used) + (h/2 - L_used) + (h - R_used - L_used).

= (h/2*2 - R_used - L_used) + (h - R_used - L_used).

= (h - R_used - L_used) + (h - R_used - L_used).

= 2*(h - R_used - L_used).

But this gives the example where h=2, R_used=1, L_used=0 → 2*(2-1-0)=2. But the correct answer is 1 change.

So this approach is also incorrect.

Clearly, there's a flaw in the way we're modeling the problem. So perhaps the problem is better approached by considering that the minimal changes required is the sum of the number of characters that must be changed to meet the required R and L counts for the horizontal group and U and D counts for the vertical group.

Let's consider that for the horizontal group, we need exactly h/2 R and h/2 L. To achieve this, we can use up to h/2 R's from the original. The remaining R's in the horizontal group must be changed to L. Similarly, any L's in the horizontal group beyond h/2 must be changed to R. And any U/D in the horizontal group must be changed to R or L.

But how to calculate this.

Alternative Idea: For the horizontal group, the changes are:

For each character in the horizontal group:

- If it's R and we have used less than h/2 R's → keep it (no change).

- If it's R and we have already used h/2 R's → must change to L (change).

- If it's L and we have used less than h/2 L's → keep it (no change).

- If it's L and we have already used h/2 L's → must change to R (change).

- If it's U or D → must change to R or L (change).

But how to model this when selecting which characters to include in the horizontal group.

But this seems complex. Perhaps the key insight is that the minimal number of changes for the horizontal group is h/2 (required R) + h/2 (required L) - (original_R + original_L) + (h - (original_R + original_L))), but this is not clear.

Alternatively, perhaps the minimal changes for the horizontal group is (h/2 - original_R) + (h/2 - original_L) + (original_R + original_L - h/2 - h/2), but this is not correct.

Alternatively, the minimal changes for the horizontal group is:

max(0, h/2 - original_R) + max(0, h/2 - original_L) + (number of U/D in the horizontal group).

But this is also not correct.

At this point, I'm stuck and need to find a different way to approach the problem.

Alternative Idea:

The total number of changes required is the sum of:

- The number of characters that must be changed to R or L to meet the horizontal group's requirements (h/2 R and h/2 L).

- The number of characters that must be changed to U or D to meet the vertical group's requirements (v/2 U and v/2 D).

But how to model this.

For the horizontal group:

The required R's are h/2. The available R's are original_R. So, the number of R's that can be used is min(original_R, h/2). The remaining R's in the original are original_R - min(original_R, h/2), which must be in the vertical group and changed to U or D. Similarly for L's.

For the horizontal group, the required R's are h/2. The number of R's used is min(original_R, h/2). The number of R's that must be added (by changing other characters) is h/2 - min(original_R, h/2). Similarly for L's.

Additionally, any U/D in the horizontal group must be changed to R or L.

So, the changes in the horizontal group are:

(R_required - R_available) + (L_required - L_available) + (number of U/D in horizontal group).

Where R_required = h/2, R_available = min(original_R, h/2), same for L_available.

But R_available is the R's in the horizontal group. So, the number of R's that must be added is R_required - R_available. Similarly for L's.

The number of U/D in the horizontal group is (h - R_available - L_available).

So, changes for horizontal group:

(R_required - R_available) + (L_required - L_available) + (h - R_available - L_available).

This is:

(h/2 - R_available) + (h/2 - L_available) + (h - R_available - L_available).

Which simplifies to:

h/2 - R_available + h/2 - L_available + h - R_available - L_available

= h - R_available - L_available + h - R_available - L_available

= 2h - 2(R_available + L_available).

But this can't be right. For the example where original_R=2, h=2, R_available=1, L_available=0:

changes = 2*2 - 2*(1+0) =4-2=2. But the correct answer is 1.

This suggests that the formula is incorrect.

At this point, I'm stuck. Perhaps I need to look for a different approach.

Alternative Idea:

The problem can be viewed as requiring the sum of R and L in the horizontal group to be exactly h (since each R and L contributes +1 and -1 respectively, and their difference must be zero. So, the number of R and L must be equal (h/2 each).

Similarly for the vertical group.

Thus, for the horizontal group, the number of R and L must be exactly h/2 each.

The minimal changes required for the horizontal group is:

The number of R and L not used as R or L in the horizontal group, plus the number of other characters in the horizontal group.

So, for example:

If we have original_R=2, original_L=0, h=2.

We need 1 R and 1 L in the horizontal group.

We can use 1 R from the original. The remaining 1 character must be L.

But original_L=0, so that L must be obtained by changing another character (the second R in the original) to L.

So changes are 1.

Similarly, for the horizontal group, the changes are:

(R_needed - available_R) + (L_needed - available_L) + (number of non-R/L in horizontal group).

But available_R is min(original_R, R_needed).

So:

R_deficit = R_needed - available_R.

L_deficit = L_needed - available_L.

non-R/L = h - (available_R + available_L).

changes = R_deficit + L_deficit + non-R/L.

In the example, R_needed=1, available_R=1 → R_deficit=0.

L_needed=1, available_L=0 → L_deficit=1.

non-R/L= 2 - (1+0)=1 → but in reality, the horizontal group has no non-R/L characters. So this approach is again incorrect.

Hmm.

Another Idea:

Each character in the original string can contribute to either the horizontal or vertical group. For the horizontal group, the required R and L are h/2 each. For the vertical group, required U and D are v/2 each.

The problem is to select which characters are assigned to which group and what direction they are assigned to, such that the required counts are met, with minimal changes.

But this is a combinatorial optimization problem and can't be solved by brute force for large n.

So, perhaps the correct approach is to compute for each possible h (even) the minimal changes by considering:

For the horizontal group, we can take up to h/2 R and up to h/2 L from the original. The remaining characters in the horizontal group must be filled with other directions (U/D) which are changed to R or L.

The changes for the horizontal group are:

(number of R in horizontal group not used as R) + (number of L in horizontal group not used as L) + (number of non-R/L in horizontal group).

But this is still unclear.

At this point, I think I need to look for patterns in the examples.

Example 2:

Input: UDUR → length 4 (even).

Original counts:

U:2, D:1, R:1, L:0.

Possible h splits:

h=0: vertical group is 4. Need 2 U and 2 D.

Available U:2, D:1.

U_used=2, D_used=1. sum_ud_used=3. But vertical group size is 4. So, 4-3=1 character must be changed to U or D. Also, U_used is min(2,2) →2. D_used is min(1, 2) →1. So sum_ud_used=3. So vertical changes: (4-3) + (2+1 -3) →1 +0=1. But also, the vertical group has the R and L from the original, which are 1 R and 0 L. So those are changed to U or D. So vertical changes would be 1 (for the R) plus 1 (for the remaining vertical character). Total 2. But according to the formula, it's 1. So this is incorrect.

But the example output is 1. So perhaps the correct approach is to consider the best possible h for each case.

In example 2, the best h is 2:

h=2: horizontal group needs 1 R and 1 L.

Original R=1, L=0.

R_used=1, L_used=0.

horizontal changes: (1-1) R deficit + (1-0) L deficit + (2 -1-0) non-R/L → 0 +1 +1=2.

vertical group size 2: needs 1 U and 1 D.

U_used=2, D_used=1. So sum_ud_used=3. But vertical group size is 2. So U_used= min(2,1)=1. D_used= min(1,1)=1. sum_ud_used=2. So vertical changes: (2-2) + (2+1-2)=0 +1=1. So total changes 2+1=3.

But according to the example, the answer is 1.

So the previous approach is clearly incorrect.

This indicates that the approach is wrong. I need to find another way.

Alternative Idea:

The problem can be transformed into: find the minimal number of changes required to make the total number of R-L = 0 and U-D = 0.

But how?

The total displacement in the horizontal direction is (R - L) = 0.

The total displacement in the vertical direction is (U - D) = 0.

So, R = L and U = D.

The total number of R and L must be even (since R + L must be even to have R = L).

Similarly for U and D.

But how does this help?

We can choose any number of R and L such that R = L. Similarly for U and D.

The sum of R + L + U + D = n.

So, R + L must be even, U + D must be even, and R + L + U + D = n.

But since R + L is even and U + D is even, their sum is even → n must be even. So first check if n is even.

The minimal changes required is the minimal number of characters to change so that:

R = L and U = D.

But how?

Let me think of this as follows:

We can model the problem by considering that after changes, we have R = L and U = D.

The total number of R + L can be any even number, and U + D is also even, with R + L + U + D =n.

But the key is to find the minimal number of changes to reach such a state.

But how to compute this.

For example, for each possible even h = R + L (h can range from 0 to n in even steps), the possible U + D is n - h, which must also be even. For each such h, the required R = L = h/2, and U = D = (n-h)/2.

The minimal changes required for this split is the number of characters in the original string that are not already in their required roles.

For example, for the required R and L counts:

required_R = h/2.

required_L = h/2.

The number of changes needed for R and L is:

max(0, required_R - original_R) → if original_R is less than required_R, need to change some characters to R.

plus max(0, required_L - original_L) → same for L.

But also, any characters in the original string that are R or L but not used in their required counts must be changed. For example, if original_R is 5 and required_R is 3, then 2 R's must be changed to other directions.

Alternatively, the total changes for R and L is:

abs(original_R - required_R) + abs(original_L - required_L) + (number of characters that are U or D and need to be changed to R or L).

This is getting too vague.

But perhaps the minimal changes for a given split h is:

changes = (required_R + required_L - (original_R + original_L)) → if this is positive, it's the number of characters needed to be changed to R or L. Otherwise, it's zero. Plus (original_U + original_D - required_U - required_D) → if this is positive, the number of characters needed to be changed to U or D. Otherwise, zero.

Wait, no. Because the required_R is h/2, required_L is h/2. So required_R + required_L = h.

The original_R + original_L is the number of R and L in the original string. The required_R + required_L is h. So if the sum of R and L in the original is less than h, then we need to change (h - (original_R + original_L)) characters (which are U or D) to R or L. If the sum is greater than h, then (original_R + original_L - h) characters (which are R or L) must be changed to U or D.

Similarly for the U and D: required_U + required_D = v = n - h. So, if original_U + original_D is less than v, then (v - (original_U + original_D)) characters must be changed to U or D. If it's greater, then (original_U + original_D -v) characters must be changed to R or L.

But then, the total changes is:

max(0, h - (original_R + original_L)) → number of U/D to be changed to R/L.

plus max(0, (original_R + original_L) - h) → number of R/L to be changed to U/D.

plus max(0, v - (original_U + original_D)) → number of R/L to be changed to U/D.

plus max(0, (original_U + original_D) - v) → number of U/D to be changed to R/L.

But this is not correct. Because this approach does not account for the individual required R and L counts.

For example, in the case where h=2 and required_R=1 and required_L=1, if original_R=2 and original_L=0:

Then required_R + required_L=2. original_R + original_L=2. So, max(0, 2-2)=0 and max(0, 2-2)=0. So, no changes from this part. But the required R and L are 1 each. So original_R=2 must contribute 1 R, and the remaining 1 R must be changed to L. So, changes are 1. But the formula above gives 0.

So, this approach is incorrect.

This indicates that the problem requires considering the individual required R and L counts, not just their sum.

At this point, I'm stuck and need to find a new way to model the problem.

Final Idea: Maybe the minimal number of changes is determined by the following formula:

The minimal number of changes is equal to (n - (R + L + U + D)) + ... but no, since R, L, U, D are not known.

Alternatively, perhaps the minimal changes can be found by considering that:

We need to have R = L and U = D. The total number of changes required is:

abs(R - L) + abs(U - D) / 2.

But this is not correct.

Alternatively, the minimal changes required is (total characters) - (max possible matches to required R, L, U, D).

But this is also unclear.

At this point, I think I need to look for the correct solution approach from a different perspective.

The problem is to find the minimal number of character changes required to have R = L and U = D.

So, the net horizontal displacement is zero and vertical is zero.

Let’s denote:

After changes:

R' = number of R's.

L' = number of L's.

U' = number of U's.

D' = number of D's.

We need R' - L' = 0 → R' = L'.

U' - D' = 0 → U' = D'.

The sum R' + L' + U' + D' = n.

But R' and L' must be equal, so R' + L' must be even. Similarly for U' and D'.

Thus, the sum of R' + L' is even, and sum of U' + D' is even. So their sum is even → n must be even. Hence, if n is odd, return -1.

If n is even, proceed.

The minimal number of changes is:

(R' + L' - R - L) → number of changes to increase R and L.

Plus (U' + D' - U - D) → number of changes to increase U and D.

But this is not correct.

Alternatively, the minimal number of changes is:

sum over each character's change:

if the character's original direction is different from the new direction, count 1.

The new directions must satisfy R' = L' and U' = D'.

But how to model this.

But the problem allows us to choose any new directions for the characters. So, for example, any character can be changed to any direction.

The key is to maximize the number of characters that can be kept as they are, while satisfying R' = L' and U' = D'.

So, the problem reduces to finding the maximum possible number of characters that can remain unchanged, given that R' = L' and U' = D'.

Let me denote:

original_R = R, original_L = L, original_U = U, original_D = D.

We need to choose R', L', U', D' such that R' = L' and U' = D' and R' + L' + U' + D' =n.

The maximum possible kept characters is the sum of min(R, R') + min(L, L') + min(U, U') + min(D, D').

But how to choose R', L', U', D' to maximize this sum, given the constraints R' = L', U' = D'.

This is a optimization problem.

Let's denote:

R' = L' = a.

U' = D' = b.

Then, 2a + 2b =n → a + b =n/2.

We need to choose a and b (non-negative integers) such that a + b =n/2.

For each possible a (from 0 to n/2), compute the maximum possible kept characters as:

min(R, a) + min(L, a) + min(U, b) + min(D, b).

Then, the maximal value of this sum over all a from 0 to n/2 gives the maximum kept characters, and the minimal changes is n - maximal_kept.

So, this seems promising.

Let's see.

For example, in the second sample input:

UDUR → original counts:

R=1, L=0, U=2, D=1.

n=4. n/2=2. So a + b=2.

Possible values of a:0, 1, 2.

For a=0:

b=2.

min(R, 0) + min(L, 0) + min(U,2) + min(D,2) → 0 +0 +2 +1=3.

For a=1:

b=1.

min(1,1) + min(0,1) + min(2,1) + min(1,1) →1+0+1+1=3.

For a=2:

b=0.

min(1,2) →1 + min(0,2) →0 + min(2,0) →0 + min(1,0) →0. Sum 1+0+0+0=1.

The maximum is 3. So minimal changes is 4-3=1, which matches the sample.

So this approach is correct.

Similarly, in the first sample input:

RRU → n=3 (odd). Output is -1.

In the third sample input:

RUUR → n=4.

Original counts: R=3, U=1, L=0, D=0.

n/2=2.

Possible a ranges from 0 to 2.

For a=0:

b=2.

kept = min(3,0) + min(0,0) + min(1,2) + min(0,2) →0+0+1+0=1. Changes 4-1=3.

For a=1:

b=1.

kept = min(3,1) + min(0,1) + min(1,1) + min(0,1) →1+0+1+0=2. Changes 4-2=2.

For a=2:

b=0.

kept = min(3,2)+ min(0,2) + min(1,0) + min(0,0) →2+0+0+0=2. Changes 4-2=2.

So the minimal changes is 2, which matches the sample.

Thus, the approach is:

For even n:

Compute a and b where a + b =n/2.

For each a from 0 to n/2:

   compute kept = min(R, a) + min(L, a) + min(U, b) + min(D, b).

The maximal kept is the maximum of all such kept values.

The minimal changes is n - maximal kept.

If n is odd, return -1.

This is the correct approach.

So, the steps are:

1. Compute the counts of R, L, U, D in the input string.

2. If the length is odd, return -1.

3. Else, compute n_even = n//2.

4. Iterate a from 0 to n_even inclusive:

   b = n_even - a.

   current_kept = min(R, a) + min(L, a) + min(U, b) + min(D, b).

   track the maximum current_kept.

5. The minimal changes is n - max_kept.

6. If max_kept is zero (which is possible only if n is zero, which is not possible per constraints), return -1. Otherwise, return the minimal changes.

But for cases where a + b =n_even, but the required R and L and U and D can't be satisfied. But according to this approach, it's allowed to have a and b as any values, and the code finds the maximum possible kept.

So, the code will work.

Now, how to implement this efficiently for large n (up to 1e5). The iteration of a from 0 to n_even can be up to 5e4 for n=1e5. Which is manageable.

But for n=1e5, n_even is 5e4. Iterating 5e4+1 times is acceptable.

Thus, the code can be implemented as follows.

First, count the number of R, L, U, D in the input.

If n is odd, output -1.

Else, compute the maximum kept over all possible a.

The code is then:

s = input().strip()

R = s.count('R')
L = s.count('L')
U = s.count('U')
D = s.count('D')
n = len(s)

if n % 2 != 0:
    print(-1)
else:
    max_kept = 0
    n_even = n // 2
    for a in range(0, n_even + 1):
        b = n_even - a
        current = min(R, a) + min(L, a) + min(U, b) + min(D, b)
        if current > max_kept:
            max_kept = current
    print(n - max_kept)

But wait, this may not work for cases where a is larger than possible R or L.

For example, a=3 and R=2. min(R,3) is 2.

But the code correctly handles it.

But why would this approach work?

Because for each possible a (number of R' and L' pairs), and b (number of U' and D' pairs), the code computes how many of the original characters can be kept. The a and b are allowed to be any non-negative integers that sum to n_even.

This approach ensures that R' = L' =a and U' = D' =b, and thus, the total displacement is zero.

Thus, the code is correct.

Testing the examples:

First example:

Input: RRU → n=3, odd. Output -1.

Second example: UDUR → n=4.

R=1, L=0, U=2, D=1.

n_even=2.

Iterate a from 0 to 2.

a=0 → b=2.

current = min(1,0) + min(0,0) + min(2,2) + min(1,2) →0+0+2+1=3.

a=1 → b=1.

current=min(1,1)+0+min(2,1)+1 →1+0+1+1=3.

a=2 → b=0.

current=1+0+0+0=1.

max_kept is 3. Changes 4-3=1.

Third example: RUUR → counts R=3, U=1, L=0, D=0. n=4.

n_even=2.

a ranges from 0 to 2.

a=0: b=2.

current=0 +0 + min(1,2) +0 →1.

a=1: current= min(3,1) +0 + min(1,1) +0 →1+0+1+0=2.

a=2: min(3,2) +0 +0 +0 →2.

max_kept=2. changes 4-2=2.

Which matches the sample.

Thus, the code is correct.

So, the correct code is as follows.
</think>

```python
s = input().strip()
R = s.count('R')
L = s.count('L')
U = s.count('U')
D = s.count('D')
n = len(s)
if n % 2 != 0:
    print(-1)
else:
    max_kept = 0
    half = n // 2
    for a in range(0, half + 1):
        b = half - a
        current = min(R, a) + min(L, a) + min(U, b) + min(D, b)
        if current > max_kept:
            max_kept = current
    print(n - max_kept)
```