<think>
Okay, let's see. The problem is to determine if we can turn the given 8x8 chessboard into a proper one by cyclically shifting rows. A proper chessboard has alternating colors, no same adjacent in rows or columns, and the top-left is white. So each row must be a shifted version of either "WBWBWBWB" or "BWBWBWBW", but since the first row's top-left must be white, the first row has to be exactly "WBWBWBWB". Wait, no. Wait, the rows can be shifted cyclically. Wait, the rows can be shifted any number of times. But the first row's first cell after shifting must be white. Because the top-left is white in a proper board. So for each row, when shifted, the first element must be the correct color according to the chessboard pattern.

Wait, the proper chessboard starts with white in the top-left. Then each row alternates. So row 1 must start with white, row 2 starts with black, row 3 white, etc. And each consecutive cell in a row alternates between white and black.

So each row must be a cyclic shift of either "WBWBWBWB" (for even rows) or "BWBWBWBW" (for odd rows). Wait, no. Wait, the rows alternate starting with white and black. So row 1 must start with white. Then row 2 starts with black. Row 3 white again, etc. So each row's pattern is determined by its row number.

Wait, for a proper chessboard:

Row 1: starts with W, then alternates.
Row 2: starts with B, then alternates.
Row 3: starts with W, etc.

So for each row i (1-based), the correct starting character is W if i is odd, B if even. Then the rest of the row alternates.

So for each row in the input, after some cyclic shifts, it must match the correct starting character and the alternating pattern.

But cyclic shifting a row can rotate it. So for each row, we need to check if there's a cyclic shift that makes it fit the required pattern for its row number.

Wait, but the rows also need to alternate with the previous and next rows. For example, row 1's first cell is W, row 2's first cell is B, row 3's first cell is W, etc. But when you shift a row, you can choose any starting point. So each row's possible shifted versions must have the correct starting character (based on row number) and alternate with the rows above and below.

Wait, but the problem allows shifting each row any number of times. So each row can be cyclically shifted to any possible rotation. For example, a row of 8 characters has 8 possible shifts (including shifting 0 times). So for each row, we can generate all possible shifted versions and check if there exists a combination where all rows fit the correct pattern and their adjacent rows do not have the same starting character.

But since the rows are 8 in total, and each has up to 8 possible shifts, trying all possibilities (8^8) is way too big. 8^8 is 16,777,216. That's about 16 million possibilities. Hmm, but 16 million is manageable for Python in 2 seconds? Wait, maybe. Because 2 seconds is 2000 milliseconds. Each iteration needs to process 8 rows. Let's see: 16 million iterations, each doing 8 checks. That's 128 million operations. Python can handle about 1e8 operations per second. So 128 million would take about a second. But maybe there's a smarter way.

Alternatively, perhaps there's a way to precompute for each row the valid shifts that would make it fit the required pattern for its row. For example, for row i, the valid shifts are those that result in the first character being correct (W if i is odd, B if even), and the entire row alternates correctly. Then, once each row's possible shifts are known, we need to choose shifts for consecutive rows such that the starting characters alternate (so row i and row i+1 must start with different characters).

Wait, but the row's starting character is determined by the row's number. Because in a proper chessboard, row i starts with W if i is odd, B if even. So for row 1, after shifting, the first character must be W. For row 2, after shifting, it must be B. For row 3, W again, etc. So each row's possible shifts are those that make the row start with the correct character (based on row number) and the entire row alternates properly.

Wait, but the row's entire pattern must alternate. So even if a row starts with the correct character, the entire row must alternate. For example, the row "WBWBWBWB" is valid. If shifted once, it becomes "BWBWBWBW", which starts with B. So for row 2, which requires starting with B, that shifted version would be a valid option. But then, the entire row must alternate, so after the first character, each next must be the opposite. So any shift of a correctly alternating row will result in another correctly alternating row. Because the original row is correct, shifting it will just rotate the pattern but maintain the alternation. Wait, no. Let's see. The original row is WBWBWBWB. If we shift it once, it becomes BWBWBWBW. Which alternates properly. So as long as the row is a cyclic shift of the correct pattern, then the entire row will alternate. Because the original is correct, shifting it any number of times will preserve the alternation. So the only requirement for a row after shifting is that the first character is correct for its row number. Because once the first character is correct, the rest of the row must alternate, and hence the entire row is correct.

Wait, no. Suppose the original row is not a cyclic shift of the correct pattern. For example, consider a row like WWBWBWBW. If you shift it once, it becomes WBWBWBWW. The first character is W. Then the next is B, W, B, W, B, W, W. Oh, the last two characters are W and W. So the alternation is broken. So the row must be a cyclic shift of the correct pattern. Otherwise, even if the first character is correct, the rest of the row may not alternate.

Ah, right. So the key is that each row in the original board must be a cyclic shift of either the correct even or odd row pattern. Because otherwise, even if you shift it to start with the correct character, the rest of the row may not alternate.

So for each row in the input, we need to check if it is a cyclic shift of either "WBWBWBWB" or "BWBWBWBW". Because only those rows can, when shifted, form a correct pattern. For example, a row that is "BWBWBWBW" is a cyclic shift (shifted once) of "WBWBWBWB". So for a row to be valid, it must be possible to shift it such that it starts with the correct first character (based on row number), and that the entire row is a cyclic shift of the correct pattern.

Wait, but "WBWBWBWB" and "BWBWBWBW" are the only two possible correct patterns for rows. Because those are the two possible starting points. So any row that is a cyclic shift of one of these two can be transformed into a correct row by shifting.

So for each row, first check if it is a cyclic shift of either of the two possible patterns. Then, for each row, collect the possible shifts that would align it to start with the correct first character for its row (W for odd rows, B for even rows). If any row cannot be a cyclic shift of either pattern, then the answer is NO.

Wait, but how to check if a row is a cyclic shift of the correct patterns.

So for each row in the input, we need to check if it can be rotated into either "WBWBWBWB" or "BWBWBWBW". If not, then it's impossible to form the chessboard.

Wait, but no. Because even if a row is a cyclic shift of, say, "WBWBWBWB", but when shifted to match the required starting character (based on row number), the entire row is correct.

Wait, perhaps for each row, the only possible correct possibilities are those that are cyclic shifts of the correct pattern. So the row must be a cyclic shift of one of the two patterns. Otherwise, no matter how you shift it, it can't form the correct row.

So the first step is to check each row whether it's a cyclic shift of the correct patterns.

For example, if a row is "WWBWBWBW", then shifting it once gives "WBWBWBWW", which is not a correct pattern, but if the original row is a cyclic shift of either of the two patterns, then it can be adjusted.

So, the approach is:

1. For each row in the input, check if it is a cyclic shift of either "WBWBWBWB" or "BWBWBWBW". If any row is not, then output NO.

   How to check this? For a given row, generate all possible cyclic shifts and see if any of them match either of the two target strings. But generating all 8 shifts for each row and checking against the two targets is manageable. Since there are 8 rows, each with 8 shifts, this is 8*8=64 checks. For each row, check all 8 possible shifts. If none of them matches either target, then the row cannot be transformed into a valid row via shifts, so answer is NO.

   Alternatively, since the two target strings are cyclic shifts of each other (since shifting "WBWBWBWB" once gives "BWBWBWBW", shifting again gives "WBWBWBWB" again after 8 shifts?), wait, no. Wait, "WBWBWBWB" shifted once becomes "BWBWBWBW". Shifted twice becomes "WBWBWBWB" again? Wait, no. Let's see:

Original: W B W B W B W B
Shift 1: B W B W B W B W (no, wait, cyclic shift moves the last character to the front. So the original is "WBWBWBWB". Shifting once would move the last B to front: B W B W B W B W. Shifting again would move the last W to front: W B W B W B W B again. So shifting once gives BWBWBWBW. Shifting again (twice) would give WBWBWBWB again? No, wait, shifting once again would take the last character of the shifted string, which is W, and move it to front. So after shifting once, the string is B W B W B W B W. Shifting this once would result in W B W B W B W B. So yes. So the two possible correct row patterns are cyclic shifts of each other. So any row that is a cyclic shift of either is valid, but must be shifted to the correct starting character based on the row's number.

Wait, but for the chessboard, the first row must start with W, the second row with B, third with W, etc. So for row i, the starting character must be W if i is odd, B if even.

So, for each row in the input, after checking that it's a cyclic shift of one of the two patterns, we need to see if there exists a shift that results in the first character being the correct one (W for odd rows, B for even rows) and the entire row being the correct pattern.

Wait, but the row is a cyclic shift of one of the two patterns. So once we have that, shifting it into the correct starting position (for the row's parity) is possible only if the correct starting character exists in the row. For example, if the row is a cyclic shift of the W-starting pattern, then all shifts of it will have either W or B in the first position. So for a row that is a cyclic shift of the W pattern, the possible first characters after shifting are W and B. But for row i, the starting character must be W if i is odd. So for such a row (a cyclic shift of the W pattern), we can only choose a shift that results in the first character being correct.

So for each row, after confirming it's a cyclic shift of one of the two patterns, we need to check if there's a shift that aligns the first character to the required one (based on row number). Then, for all rows, their shifts must align such that consecutive rows have different starting characters (since row i is W if i is odd, B if even, so consecutive rows will alternate).

Wait, but according to the problem statement, after shifting, the rows must form a proper chessboard. So each row's starting character is determined by its row number. So row 1 must start with W, row 2 with B, etc. So, for each row i, after shifting, the first character must be W if i is odd, B if even.

Additionally, each row must alternate correctly (which is guaranteed if the row is a cyclic shift of one of the two patterns and the shift is correct).

So the steps are:

1. For each of the 8 input rows, check if it is a cyclic shift of either "WBWBWBWB" or "BWBWBWBW". If any row is not, output NO.

2. For each row, collect all possible shifts that would make the first character correct for its row (i.e., for row i, the first character after shifting must be W if i is odd, B if even). For a row to be valid, there must be at least one such shift. If any row has no possible shifts, output NO.

3. Now, for all rows, select a shift (from their possible shifts) such that consecutive rows have starting characters that alternate. Since the starting characters are determined by row numbers, this is automatically satisfied. Because row i is even or odd, the starting characters alternate. So once each row is shifted correctly, their starting characters are W, B, W, B, etc. So the problem reduces to: after shifting each row to have the correct starting character (based on row number), check if the entire board is a proper chessboard (i.e., adjacent rows have different starting characters, and within each row, the colors alternate).

Wait, but if all rows are shifted to have the correct starting character (W for odd rows, B for even), then consecutive rows will automatically have alternating starting characters. For example, row 1 starts with W, row 2 with B, row 3 with W, etc. So consecutive rows will have starting characters that are different. So the main check is that each row is shifted to have the correct starting character, and that each row's pattern is correct (alternating colors). But since we already ensured that each row is a cyclic shift of one of the two correct patterns, shifting it to the correct starting character would ensure the entire row alternates correctly.

Wait, but let's think: the original row is a cyclic shift of either "WBWBWBWB" or "BWBWBWBW". So when we shift it to have the correct starting character, the entire row must alternate. For example, suppose the original row is a cyclic shift of "WBWBWBWB". So when shifted to start with W (for row i=1), the row becomes "WBWBWBWB", which alternates correctly. Similarly, if the row is a cyclic shift of "BWBWBWBW", then shifting to start with B (for even rows) will result in "BWBWBWBW", which also alternates. So if all rows are shifted correctly, then their patterns are correct. So the key steps are:

- Check each row is a cyclic shift of either correct pattern.

- For each row, find if there exists a shift that makes the first character correct for its row.

If both conditions are met, then the answer is YES. Otherwise, NO.

So the problem can be broken down into these two checks.

But wait, there's a mistake here. For example, suppose a row is a cyclic shift of "WBWBWBWB" (like "BWBWBWBW" which is shifted once). For row 2 (even), the starting character must be B. So shifting this row to start with B. But the row is "BWBWBWBW", which starts with B and alternates correctly. So the row is valid. But what if the row is a cyclic shift of the correct pattern but there's no shift that gives the correct starting character?

For example, consider a row that is "WWBWBWBW" (not a cyclic shift of the correct patterns). But wait, such a row would not pass the first check (is it a cyclic shift of the correct patterns). So the first check is to ensure that the row is a cyclic shift of either correct pattern. So in that case, for each row, after step 1, the row can be shifted to any of the 8 possible positions. Then, step 2 is to check if there exists a shift that gives the correct starting character (based on row number). If that's possible, then the row is valid.

So the steps are:

For each row in input:

   a. Check if it can be generated by a cyclic shift of either "WBWBWBWB" or "BWBWBWBW". If not, answer is NO.

   b. Check if any of the possible shifts (which can generate the correct pattern) results in the first character matching the required for the row (W for odd rows, B for even). If not, answer is NO.

If all rows pass both checks, answer is YES.

So now, the question is how to implement these steps.

First, generate all possible cyclic shifts for each row. For a row of 8 characters, there are 8 possible shifts. For each shift, check if it matches either of the two target patterns. For example, for a row, generate all 8 possible shifted versions, then check if any of them equals "WBWBWBWB" or "BWBWBWBW".

But generating all shifts for each row might be time-consuming. However, for 8 rows and 8 shifts each, it's manageable.

Alternatively, for each row, check if it's a cyclic shift of the correct patterns. How?

Another approach: The correct patterns are "WBWBWBWB" and "BWBWBWBW". So any row that is a cyclic shift of these must have all even indices (0-based) as B in one pattern, but perhaps the key is that the row alternates W and B. Wait, but any cyclic shift of these two patterns will also alternate. So for a row to be a valid cyclic shift, it must have exactly 4 Ws and 4 Bs? No, wait, the original patterns have 4 Ws and 4 Bs. So their cyclic shifts also have 4 Ws and 4 Bs. So any row that has a different count of W and B can be rejected immediately. So first, check if each row has exactly 4 Ws and 4 Bs. If not, then it's impossible.

Wait, this could be a quick check. Let's see. For example, if a row has 5 Ws and 3 Bs, it's impossible to be a cyclic shift of the correct patterns. So this can quickly rule out some rows.

So step 0: for each row, check if the number of Ws is 4. If not, output NO.

But wait, the correct patterns have 4 Ws and 4 Bs. So their cyclic shifts also have 4 Ws and 4 Bs. So any row that doesn't have exactly 4 Ws and 4 Bs cannot be a cyclic shift of the correct patterns. So this is a necessary condition, but not sufficient. For example, a row with 4 Ws and 4 Bs arranged in a different way (like WWBWBWBW) would not be a cyclic shift of the correct pattern.

So step 0 can be to check each row has exactly 4 Ws and 4 Bs. If any row doesn't, answer is NO. Else, proceed.

This can save time in checking.

So the approach would be:

For each of the 8 input rows:

   - Check that it has exactly 4 Ws and 4 Bs. If not, output NO.

   - Check if it is a cyclic shift of either "WBWBWBWB" or "BWBWBWBW".

   - If not, output NO.

   - Else, check if there's at least one shift (for this row) that makes the first character correct for its row (W for odd, B for even). For example, for row i (1-based), check if any of the cyclic shifts that align it to either pattern starts with the correct character.

Wait, but if the row is a cyclic shift of "WBWBWBWB", then when shifted appropriately, the first character can be W or B. Similarly for the other pattern. So for a row that is a cyclic shift of "WBWBWBWB", the possible first characters after shifts are all possible W and B in the positions.

Wait, no. For a cyclic shift of "WBWBWBWB", the first character can be any of the characters in the original string. The original has W, B, W, B, etc. So the possible first characters after shifting are W, B, W, B, W, B, W, B. So for a row that is a cyclic shift of this pattern, the possible first characters are alternating W and B. So for example, shifting by 0: W. Shift by 1: B. Shift by 2: W. etc.

So, for a row that is a cyclic shift of "WBWBWBWB", the possible first characters are W and B, alternating with each shift. So to get a first character of W (for odd rows), the row must be shifted by an even number of positions. For example, shift 0: W, shift 2: W, etc. For B, shifts 1,3,5,7.

Similarly, for a row that is a cyclic shift of "BWBWBWBW", which is the other pattern, the possible first characters after shifts are B, W, B, W, etc. So shifts 0: B, shift 1: W, etc.

So for each row, after checking it's a cyclic shift of one of the two patterns, we can determine which pattern it belongs to. Then, for that row, the possible first characters after shifting are the characters of that pattern in order. So for example, if the row is a cyclic shift of the W-pattern (WBWBWBWB), then the possible first characters when shifted are W, B, W, B, etc. For the B-pattern (BWBWBWBW), the possible first characters are B, W, B, W, etc.

So the approach could be:

For each row:

   - Check if it's a cyclic shift of W-pattern or B-pattern. If neither, output NO.

   - For the pattern it belongs to, determine if there exists a shift where the first character matches the required one (W for odd rows, B for even).

   - If no such shift exists for any row, output NO.

So how to implement this.

First, for each row, check if it's a cyclic shift of either pattern. Let's generate all possible shifts of the row and see if any match the W-pattern or B-pattern.

Alternatively, for a given row, check if it can be represented as a rotation of the W-pattern. For example, for the row s, check if there exists a rotation k such that rotating s by k steps gives the W-pattern. Similarly for the B-pattern.

But generating all rotations for each row is manageable. For each row, generate all 8 possible rotations (shift 0 to 7). For each rotation, check if it equals W-pattern or B-pattern. If for any rotation it matches either, then the row is valid. Else, invalid.

So for each row in the input:

   valid = False

   for shift in 0..7:

       rotated_row = rotate row by shift steps (e.g., shift steps to the right)

       if rotated_row == W_pattern or rotated_row == B_pattern:

           valid = True

           break

   if not valid:

       output NO

So this is the first check. If any row fails this, output is NO.

Once all rows pass this check, proceed to check if for each row, there exists a shift that makes the first character correct for the row's position.

But wait, the row could be a cyclic shift of either pattern. So for each row, when rotated, it's either part of the W-pattern's cyclic shifts or the B-pattern's.

For example, if a row is a cyclic shift of the W-pattern, then all possible shifts of the row are cyclic shifts of the W-pattern. Similarly for the B-pattern.

So once a row is determined to be a cyclic shift of either pattern, then we can know that the possible first characters after rotation are the same as the first characters of the rotations of the original pattern.

For example, the W-pattern rotated has first characters W, B, W, B, etc. Similarly, the B-pattern rotated has first characters B, W, B, W, etc.

So for a row that is a cyclic shift of the W-pattern, the possible first characters after rotation are W and B. For a row that is a cyclic shift of the B-pattern, the possible first characters are B and W.

But wait, the B-pattern is BWBWBWBW. Rotating it once gives WBWBWBWB, which is the W-pattern. Wait, no. Wait, the B-pattern is BWBWBWBW. Shifting once (moving the last character to front) gives WBWBWBWB. So a cyclic shift of the B-pattern can result in the W-pattern. Therefore, the two patterns are cyclic shifts of each other. So the set of all cyclic shifts of the W-pattern and the B-pattern is the same. Wait, but that's not possible. Because the W-pattern has 8 characters, so shifting it 8 times brings it back to the original. So shifting the W-pattern once gives BWBWBWBW. Shifting again gives WBWBWBWB again? No, shifting once gives BWBWBWBW. Shifting once again would take the last character (W) and move it to front, resulting in WBWBWBWB. So after two shifts, it's back to the original? Wait, no. Let's see:

Original W-pattern: W B W B W B W B.

Shift once (last character B to front): B W B W B W B W (BWBWBWBW).

Shift again (last character W to front): W B W B W B W B (WBWBWBWB again). Wait, no. Wait, the first shift gives B W B W B W B W. Shifting this once again (move last character to front) would take the last character (W) and move it to front, making W B W B W B W B. So yes, after two shifts of the W-pattern, we get back to the original. So the W-pattern's cyclic shifts are:

Shift 0: WBWBWBWB

Shift 1: BWBWBWBW

Shift 2: WBWBWBWB (again)

Shift 3: BWBWBWBW

and so on. So the W-pattern's cyclic shifts alternate between WBWBWBWB and BWBWBWBW for even and odd shifts. Similarly for the B-pattern.

Wait, but the B-pattern is BWBWBWBW. Shifting it once gives WBWBWBWB. Shifting again gives BWBWBWBW again, etc.

So, the cyclic shifts of the W-pattern and B-pattern are the same. Because shifting the W-pattern once gives the B-pattern, and shifting again gives the W-pattern again. So the entire set of cyclic shifts for both patterns is just two possible patterns. So any row that is a cyclic shift of either pattern is a cyclic shift of both. Therefore, for any row that is a cyclic shift of either, the possible first characters after rotation are W and B, alternating with each shift.

So, regardless of which pattern the row belongs to, the possible first characters after rotation are W and B.

So, for a row, the possible first characters are either W and B, but only in certain shifts. So for a row to be valid for a particular row number (i), the required first character is W if i is odd, B if even.

So, for each row, given that it's a cyclic shift of the correct patterns, we need to check if there exists a shift that results in the first character being the desired one for the row's index.

But since the possible first characters after shifts alternate between W and B (for even and odd shifts), we can determine if the required character is present.

For example, for a row that is a cyclic shift of the correct patterns, the possible first characters are W and B, each appearing 4 times (since the row length is 8, shifts 0-7: shifts 0,2,4,6 give W and B depending on the initial pattern. Wait, perhaps this is getting complicated.

Alternatively, for each row, once it's determined to be a cyclic shift of the correct patterns (i.e., the row is either WBWBWBWB or BWBWBWBW or any cyclic shift thereof), then the possible shifts for the row can be considered. For each row, the required first character is determined by the row's position (i). So for row i (1-based), the required first character is W if i is odd, B if even.

But for a row that is a cyclic shift of the correct patterns, the possible first characters when rotated are W and B. So for row i:

If required first character is W (i is odd), then the row must have at least one shift where the first character is W. Similarly for B (even rows).

But how can we check if such a shift exists?

Well, since the row is a cyclic shift of the correct patterns, the first characters for the possible shifts alternate between W and B. So for example, the W-pattern starts with W, then B, W, etc. So shifts 0, 2, 4, 6 of the W-pattern give W as the first character. Shifts 1,3,5,7 give B. Similarly for the B-pattern.

But the B-pattern is shifted once from the W-pattern. So for any row that is a cyclic shift of the correct patterns, the possible first characters after shifts are either W or B. So the row can be shifted to have the first character as W or B.

But wait, if the row is a cyclic shift of the correct patterns, then for shifts 0, 2, 4, 6, the first character is W if the original pattern was W-pattern, or B if the original pattern was B-pattern. Wait, perhaps it's easier to think that for any row that is a cyclic shift of the correct patterns, the first characters after even shifts (0, 2, 4, 6) are the same as the original pattern's first character, and after odd shifts are the opposite.

But this is getting complicated. Let's think of an example.

Original W-pattern: WBWBWBWB.

Shift 0: W (first character W).

Shift 1: B.

Shift 2: W.

Shift 3: B.

And so on.

So for the W-pattern, even shifts (0, 2, 4, 6) produce W as first character, odd shifts (1,3,5,7) produce B.

Similarly, for the B-pattern (BWBWBWBW):

Shift 0: B.

Shift 1: W.

Shift 2: B.

Shift 3: W.

So for even shifts, first character is B; odd shifts, W.

So, for a row that is a cyclic shift of the W-pattern, the possible first characters after even shifts are W, after odd shifts B.

For a row that is a cyclic shift of the B-pattern, the possible first characters after even shifts are B, after odd shifts W.

But since the B-pattern is a shift of the W-pattern, perhaps the row can be considered as part of either pattern. Wait, but the original pattern is either W or B, but after shifting, they are the same.

So for example, if a row is BWBWBWBW (the B-pattern), shifting it by 1 gives WBWBWBWB (the W-pattern). So when considering all possible shifts, the row can be seen as part of either pattern's shifts.

But when checking if the row is a cyclic shift of either pattern, any row that is a cyclic shift of either will be considered valid.

So for the problem, the key is:

For each row i (1-based), required first character is W if i is odd, B if even.

For the row to be valid, there must exist a shift that results in the first character being the required one.

So for each row, after checking that it's a cyclic shift of the correct patterns (step 1), we need to check whether the required first character (based on row number) is present in any of the possible shifts of that row.

But since the row is a cyclic shift of the correct patterns, the possible first characters are either W and B. So for example, for row 1 (requires W), there must be at least one shift of the row that produces W as the first character.

But how to determine that.

Wait, given that the row is a cyclic shift of the correct patterns, then the possible first characters are W and B. So for a row that is a cyclic shift of the correct patterns, the possible first characters are W and B, and each appears 4 times (since for 8 shifts, each even shift gives one character, odd gives the other).

So for such a row, there are always shifts that result in W and shifts that result in B.

Therefore, for any row that passes step 1 (being a cyclic shift of the correct patterns), there will exist a shift that makes the first character W and another shift that makes it B. Therefore, for any row, if the required first character is either W or B, there exists a shift that satisfies it.

Wait, no. For example, suppose the row is the B-pattern (BWBWBWBW). For row 1 (requires W as first character), the row can be shifted once to get WBWBWBWB, which has first character W. So possible. For row 2 (requires B), the row can be shifted 0 times to get B as first character. So possible.

So for any row that is a cyclic shift of the correct patterns, the required first character is achievable.

Wait, this seems to be the case. Because for any such row, it can be rotated to the W-pattern or B-pattern. For example, a row that is a cyclic shift of the correct patterns can be rotated to WBWBWBWB (shift k times). Then, for odd rows, the first character is W. For even rows, the required first character is B, which can be achieved by shifting once.

So for any row that is a cyclic shift of the correct patterns, the required first character is always achievable. Therefore, step 2 is automatically satisfied. So once all rows pass step 1 (are cyclic shifts of the correct patterns), then the answer is YES.

But wait, is that true?

Let's take an example.

Consider row i=1 (must start with W).

Suppose the row is BWBWBWBW (B-pattern). So, to get first character W, we need to shift it once. Shifting it once gives WBWBWBWB. So first character W. So it's possible.

Another example: row i=2 (even, must start with B). The row is WBWBWBWB (W-pattern). To get first character B, shift it once. Shifting once gives BWBWBWBW. So first character is B.

So yes, any row that is a cyclic shift of the correct patterns can be shifted to have the required first character.

Therefore, the only checks needed are:

1. Each row has exactly 4 Ws and 4 Bs.

2. Each row is a cyclic shift of either WBWBWBWB or BWBWBWBW (i.e., the row is a cyclic shift of the correct patterns).

If both conditions are met, then output YES. Else, NO.

So the steps are:

For each row:

   a. Check if it has exactly 4 Ws and 4 Bs. If not, output NO.

   b. Check if it is a cyclic shift of the correct patterns. If not, output NO.

If all rows pass these checks, output YES. Else, NO.

So the code can be written as follows.

First, generate the two correct patterns:

pattern1 = "WBWBWBWB"

pattern2 = "BWBWBWBW"

Then, for each row in the input:

   - Check if the row's count of 'W' is 4. Else, output NO.

   - Check if the row is a cyclic shift of either pattern1 or pattern2. To do this, generate all possible rotations of the row and see if any match pattern1 or pattern2.

If all rows pass these checks, output YES.

Now, the code.

But generating all rotations for each row can be time-consuming. How to generate them?

For a given row s, the possible rotations are:

for shift in 0 to 7:

   rotated = s[-shift:] + s[:-shift]

Wait, no. For a cyclic shift to the right by k times. For example, shifting "WBWBWBWB" once to the right would be "BWWBWBWB" — no, wait, no. Wait, when you perform a cyclic shift to the right once, the last character becomes the first.

So for example, "WBWBWBWB" shifted once to the right becomes "BWBWBWBW". Shifting twice to the right would move the last two characters to the front: "WWBWBWBW", but wait, no. Let's see:

Original: W B W B W B W B

Shift 1: B W B W B W B W (last character B moved to front)

Shift 2: W B W B W B W B → Wait, that's shifting once again. So shift 2 would be the same as shift 0 mod 8.

So the correct way to generate all possible shifted versions is for each shift k (0-7), the rotated string is s[k:] + s[:k]. Wait, no. For example, shifting to the right by 1, the rotated string is s[-1] + s[:-1]. So for a string s of length 8, shifting right by 1 is s[7] + s[0:7].

Yes. So for shift in 0-7, the right-shifted version is s[-shift:] + s[:-shift].

So for example, shift=0: s[-0:] is empty, but s[-0:] is the entire string. Wait, Python's slicing is a bit tricky here. Let's see:

s = "abcdefgh"

shift=1: s[-1:] + s[:-1] → 'h' + 'abcdefg' → 'habcdefg'

shift=2: s[-2:] + s[:-2] → 'gh' + 'abcdef' → 'ghabcdef'

Yes. So the correct way to generate a right shift by k steps is s[k:] + s[:k] → no, wait, that's left shift. For example, shifting left by 1: 'bcdefgha'.

Right shift by 1: 'habcdefg'.

So the right shift can be implemented as s[-k:] + s[:-k].

Yes.

So for each row, to generate all possible right-shifted versions (from 0 to 7 steps), we can loop k from 0 to 7, compute s_rotated = s[-k:] + s[:-k], then check if any of these equals pattern1 or pattern2.

So in code:

for each row in input_rows:

    if row.count('W') !=4:

        print("NO")

        exit()

    found = False

    for k in range(8):

        rotated = row[-k:] + row[:-k]

        if rotated == pattern1 or rotated == pattern2:

            found = True

            break

    if not found:

        print("NO")

        exit()

print("YES")

So this code would check for each row if it can be rotated to either pattern. If any row cannot, output NO. Else, output YES.

But wait, there's a mistake here. For example, the row "WBWBWBWB" is already pattern1, so yes. But for a row that is a cyclic shift of pattern2 (like BWBWBWBW), then rotating it by k=0 gives pattern2. So the code would find that.

But pattern2 is a valid pattern. So in this case, the code would correctly recognize it.

But what if a row is a cyclic shift of pattern2, but not of pattern1? But pattern2 is a cyclic shift of pattern1. So any row that is a cyclic shift of pattern2 is also a cyclic shift of pattern1, since pattern2 is a cyclic shift of pattern1. Wait, no. For example, if the row is pattern2 (BWBWBWBW), then shifting it by 1 gives WBWBWBWB (pattern1). So any row that is a cyclic shift of pattern2 is also a cyclic shift of pattern1. So the two patterns are part of the same cycle.

So the code above checks if any rotated version of the row is either pattern1 or pattern2. But since pattern2 is a shift of pattern1, the code is redundant. Because if the row is a cyclic shift of pattern2, then one of its rotations would be pattern1. For example, the row is pattern2 (BWBWBWBW). Rotating it by 1 step gives WBWBWBWB (pattern1). So the code would find that.

Therefore, the code above correctly checks whether the row is a cyclic shift of either pattern, because any cyclic shift of pattern1 will include both pattern1 and pattern2, and their other shifts.

But wait, for example, a row that is WBWBWBWB shifted by 2 steps: WBWBWBWB shifted twice to the right would become WBWBWBWB again. Because shifting once gives BWBWBWBW, shifting again gives WBWBWBWB. So the code's loop for k=0 to 7 would generate all possible shifts. For the row WBWBWBWB, the rotated versions for k=0, 2,4,6, etc. would be pattern1, and for k=1,3,5,7 would be pattern2.

So in code, when checking for each k, if any of the rotated versions equals pattern1 or pattern2, then the row is valid.

But since the two patterns are part of the same cyclic group, the code could be optimized by checking if any rotated version matches pattern1. Because pattern2 is a shifted version of pattern1, and any cyclic shift of pattern1 will have a rotation that is pattern1 or pattern2.

But the code as written will correctly catch all possible rows that are cyclic shifts of either pattern.

So the code works.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    pattern1 = "WBWBWBWB"
    pattern2 = "BWBWBWBW"

    def is_valid_row(row):
        if row.count('W') != 4:
            return False
        for k in range(8):
            rotated = row[-k:] + row[:-k] if k !=0 else row
            if rotated == pattern1 or rotated == pattern2:
                return True
        return False

    for _ in range(8):
        row = input_stream.readline().rstrip("\n").strip()
        if not is_valid_row(row):
            print("NO", file=output_stream)
            return
    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
WBWBWBWB
WBWBWBWB
BBWBWWWB
BWBWBWBW
BWBWBWBW
BWBWBWWW
BWBWBWBW
BWBWBWBW
""",
            "output": \
"""\
NO
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

The second sample input:

WBWBWBWB

WBWBWBWB → this row has 8 W's? Wait, no. WBWBWBWB has 4 Ws and 4 Bs. Wait, the sample input in the second case:

Sample Input 2:

WBWBWBWB → 4 W, 4 B.

WBWBWBWB → same.

BBWBWWWB → count of W: Let's count. B B W B W W W B → W: 4? Let's see: positions 2,4,5,6 are W. 4 Ws. But the row is BBWBWWWB. So W count is 4.

But when we check all possible shifts, does any of them match pattern1 or pattern2?

The row is BBWBWWWB. For any shift, can it be rotated to pattern1 or pattern2?

For example, shifting it 0 times: BBWBWWWB. Not equal to either pattern.

Shifting once: B BBWBWWW → "B" + "BWBWWWB"? Wait, no. The original is BBWBWWWB. Let's see:

s = BBWBWWWB (indexes 0-7).

Shift by k=1: last character (index 7) is B. So rotated is B + BBWBWWW (s[:-1] is BBWBWWW). So rotated string is B followed by BBWBWWW → BBBWBWWW. Which is not pattern1 or pattern2.

Similarly, shifting by k=2: last two characters are WB. rotated is WB + BBWBWW → WBBWBWW. Not matching.

So this row would fail the check. So code returns NO.

Thus, the code correctly handles the sample inputs.

So the code is as described.
</think>

```python
pattern1 = "WBWBWBWB"
pattern2 = "BWBWBWBW"

def is_valid_row(row):
    if row.count('W') != 4:
        return False
    for k in range(8):
        rotated = row[-k:] + row[:-k] if k !=0 else row
        if rotated == pattern1 or rotated == pattern2:
            return True
    return False

for _ in range(8):
    row = input().strip()
    if not is_valid_row(row):
        print("NO")
        exit()
print("YES")
```
