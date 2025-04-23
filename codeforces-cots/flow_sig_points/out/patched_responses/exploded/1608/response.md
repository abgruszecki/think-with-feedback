<think>
Okay, let's try to solve this problem. Hmm. So the problem is about checking if Peter's two sequences of colors appear in the correct order on either the forward or backward path of the train's route, right? And we have to determine if it's possible in either direction, both, or neither.

First, the input is three lines: the first is the path from A to B. The second and third are Peter's two sequences. We need to check if there's a way to split the path (either forward or reversed) into two parts such that the first sequence appears in the first part and the second sequence appears in the second part. Oh wait, but the sequences must be in order. So the first sequence must be a consecutive substring in the path, followed by the second sequence occurring after the end of the first, right?

So the approach would be:

1. Check the forward direction (original string) for the two sequences. If found in order, mark forward as possible.
2. Check the backward direction (reversed string) similarly. If found in order, mark backward as possible.
3. Depending on which options are possible, output the corresponding result.

But how do we check if the two sequences appear in order with the first before the second?

Let's think about the steps for one direction (forward or reversed). For example, in the forward direction:

- The path is the original string S.
- We need to find an index i where the first sequence s1 appears ending at i, and the second sequence s2 starts at some j >= i+1. Wait, no. Wait, the sequences must be in order. So the first sequence must appear somewhere, then the second sequence must appear after the first sequence's end. So the entire s1 must be a substring of S, and s2 must be a substring that occurs after the end of s1.

So for the forward check, here's what we need to do:

1. Find all possible starting indices where s1 occurs in S. For each occurrence of s1, note the end index (start + len(s1) - 1). Then check if s2 occurs anywhere in S after that end index. So for each occurrence of s1, we check if s2 is present in the substring starting from end index + 1.

But since the sequences can be up to 100 characters each, and the main string can be up to 1e5, this approach could be efficient if we find the first occurrence of s1 and then check s2 after, but maybe we need to check all possible positions where s1 occurs.

Wait, but the problem states that Peter saw the first sequence during his first wake period and the second during the second. So the sequences must appear in order, but not necessarily consecutively. So for example, s1 could be at positions 0-2, then s2 could be at 5-7. That's allowed.

So the steps for one direction:

For the given direction (forward or reversed):

a. Find all the starting indices where s1 occurs in the direction's path.

b. For each such starting index, calculate the end index (start + len(s1) - 1). Then check if s2 occurs in the path starting from (end index + 1) onwards.

If any of these checks pass, then the direction is possible.

But checking all possible starting indices of s1 might be time-consuming if s1 occurs many times. However, since s1's length is up to 100, and the main string is 1e5, the maximum number of possible occurrences is up to 1e5 - 100 + 1 = ~1e5. That's a lot. But checking each occurrence and then checking s2 each time could be O(n * m) where m is the sum of the lengths of s1 and s2. Wait, but maybe there's a smarter way.

Alternatively, find all possible end positions of s1. Then for each end position, check if s2 exists in the remaining part of the string.

But how to efficiently check if after a certain position, s2 exists?

An efficient approach would be:

For a given direction:

1. Precompute all the positions where s1 occurs. For each occurrence, note the end index (start + len(s1) - 1).

2. For each end index, check if s2 occurs in the string starting from end_index + 1 onwards.

If any occurrence of s1 is followed by s2 in the remaining part, then the direction is possible.

So the question is, how to find the occurrences of s1 and s2 in the string efficiently.

Now, for the string searching, we can use the KMP algorithm or the built-in string methods. But in Python, the 'in' operator is optimized, but perhaps for longer substrings, using the find method with start indices is better.

But let's think about the steps again.

For checking s1 in the string S (forward direction):

- For each occurrence of s1 in S, note the end index.

Then for each such end index, check if s2 is present in S from (end index + 1) onwards.

So for each occurrence of s1, check if s2 is a substring of S starting from (end index + 1) to the end.

But how do we check if s2 is present in that substring?

In Python, the string method 'find' can take a start and end index.

So for the forward check:

Check if s1 is present anywhere in S. For each occurrence of s1, after its end, check if s2 is present in S after that.

Similarly for the reversed check (the reversed S).

So the steps would be:

1. Read the three input lines: S, s1, s2.

2. Check for the forward direction (S):

   a. Find all starting indices where s1 is a substring.

   b. For each such start index, compute the end index (start + len(s1) -1).

   c. For the substring of S from end+1 to the end, check if s2 is present.

   d. If any occurrence of s1 has s2 present after, then forward is possible.

3. Check the reversed direction (S_reversed = S[::-1]):

   a. Similarly find all occurrences of s1 in S_reversed.

   b. For each occurrence's end index, check if s2 is present after.

   c. If any, then backward is possible.

4. Based on which directions are possible, output the result.

Now, the key points here are how to efficiently find the occurrences of s1 and then check for s2.

But for Python, even if S is 1e5 characters, checking each occurrence of s1 (if s1 is 100 characters long) could take O(n) time for each occurrence. Wait, no: for each possible start index in S, we can check if the substring starts with s1. But that's O(n * len(s1)) time, which for n=1e5 and len(s1)=100 is 1e7 operations, which is manageable for Python's speed, but maybe tight.

But perhaps there's a smarter way. The KMP algorithm can find all occurrences of a substring in O(n + m) time, where m is the length of the pattern (s1 here). So that would be better for longer s1.

But implementing KMP for each check might be time-consuming. However, in Python, the built-in string methods might be optimized. So for example, using the 'find' method in a loop can be efficient.

Alternatively, here's a way to find all starting indices of s1 in S:

start = 0

while True:

    pos = S.find(s1, start)

    if pos == -1:

        break

    # record pos

    start = pos + 1

This loop will find all occurrences of s1 in S, starting from the beginning. Each 'find' is O(n) in the worst case. But if s1 is not present, it's fast. But if s1 is present many times, say every position, this loop would be O(n) for each occurrence, leading to O(n^2) time. But given that s1's length is up to 100, this is only possible if s1 is a single character. But the problem says that the sequences are non-empty. For example, if s1 is 'a', then in a string of all 'a's, each position (except the last 99 characters) is a starting index. So the number of occurrences would be O(n) for s1 of length 1. Then, checking each occurrence would take O(n) operations for each, leading to O(n^2) time, which is 1e10 operations for n=1e5. That's way too slow.

So this approach would not work for such cases. So we need a more efficient way to find all starting indices of s1 in S.

So the problem is that for some cases, the number of occurrences of s1 can be very large (like 1e5), and for each occurrence, checking s2 in the remaining part could take O(m) time where m is the length of s2. So the total time would be O(k*(n + m)), where k is the number of occurrences of s1. For k up to 1e5, this is 1e5 * (1e5 + 1e2) which is way too big (1e10 operations). That's way beyond the time limit.

So this approach is not feasible. So we need a better way.

Alternative idea: For each direction, check if s1 occurs at least once in the string, and after the end of that occurrence, s2 occurs. But instead of checking all possible occurrences of s1, maybe find the earliest occurrence of s1, and then check if s2 occurs after. Alternatively, find the earliest occurrence of s1 such that after it, s2 exists. But this might not work because a later occurrence of s1 might leave enough space for s2.

Wait, no. Because if s1 occurs at position x, and s2 occurs after x + len(s1), then any occurrence of s1 after x would also have the same s2, but perhaps that's not the case. For example, if s1 occurs at positions 0 and 100, and s2 occurs at position 50. Then the first occurrence of s1 would check for s2 after 0 + len(s1) - 1, which is position len(s1)-1, and s2 is at 50. If len(s1) is 10, then 50 is after 9, so yes. But the second occurrence at 100 would check after 100+9=109, but s2 is at 50, which is before. So in that case, the first occurrence is valid, but the second is not. So the earliest occurrence is sufficient.

Wait, no. Suppose s1 is 'abc', and the string is 'abcxabc'. s1 occurs at 0 and 4. Suppose s2 is 'y'. So the first occurrence ends at 2. The remaining part after 3 is 'xabc', which doesn't contain 'y'. The second occurrence ends at 6. The remaining part is empty. So in this case, even though s1 occurs, s2 is not present. So only the first occurrence is considered, but no.

But suppose s2 is 'xab'. Then after the first occurrence (ends at 2), the remaining string starts at 3: 'xabc'. The substring from 3 is 'xabc', so 'xab' is present starting at 3. So the first occurrence allows s2 to be found. The second occurrence's end is 6, and there's no remaining characters. So the first occurrence is the one that works.

But if s2 is 'ab', then after the first occurrence (ends at 2), the remaining string is 'xabc'. s2 starts at 3 (the 'abc' part). So after the first occurrence's end, there's no 'ab'. But in the second occurrence, the end is 6, nothing after. So in this case, no.

Wait, but the first occurrence's end is 2. The remaining string starts at 3. So in the remaining part (indices 3 to 6?), maybe s2 is present.

So, the point is, the earliest occurrence of s1 may not be sufficient. Because even if the earliest occurrence is followed by s2, but there's a later occurrence of s1 that is followed by s2, we have to check all.

But that's time-consuming. So we need a way to check in O(n) time for both s1 and s2.

Alternative approach:

For a given direction, find the first occurrence of s1, then check if s2 exists after its end. If yes, then the direction is possible. If not, check the next occurrence of s1. But in the worst case, this could be O(n) time.

But in practice, the first occurrence that allows s2 to be found after would be sufficient. Because once we find one such occurrence, the direction is possible, and we can return early.

Wait, the problem requires that there exists at least one occurrence of s1 followed by s2. So once we find any such occurrence, we can mark the direction as possible and move on.

So for each direction:

Check if there exists any occurrence of s1 in the direction's path such that s2 occurs after the end of s1.

So the algorithm can be:

For direction in [forward, backward]:

   check if exists:

       s1 occurs in S, and s2 occurs in S after the end of s1.

If yes, then direction is possible.

So the key is to find the earliest occurrence of s1, and then check s2 in the remaining part. If not found, find the next occurrence of s1, and check again. But in the worst case, this can take O(n) time.

But perhaps we can optimize by finding the earliest possible end of s1, such that the remaining part of the string contains s2. So perhaps the earliest occurrence of s1, then check. If not, the next occurrence, etc., until found.

But how to do this efficiently.

Another idea: For the direction's path, first find all the starting indices where s1 occurs. Then for each such start index, check if the substring starting at (start + len(s1)) contains s2. If any of them do, then return True.

But the problem is, how to efficiently find all the start indices of s1.

In Python, the 'find' method can be used iteratively. But for large N and s1 of length 1, this could take O(n) time. But for the worst case, it's O(n) for s1 and O(n) for s2, but multiplied by the number of occurrences of s1.

But perhaps in practice, the code can pass within the time constraints. Let's think of the example where S is 'a' * 1e5, and s1 is 'a', s2 is 'a'. Then the code would find that s1 occurs 1e5 - 0 times (since len(s1) is 1). Then for each occurrence, check if the remaining part (from start + 1) contains 'a', which is true. So the code would return early on the first occurrence, which is position 0. But the code would check the first occurrence, find that the remaining part (positions 1 to 1e5) has 'a' * (1e5-1), so s2 is present. So it returns True for that direction.

So even if s1 has many occurrences, the code can return after the first check. Because once any occurrence is found where s2 is present after, we can mark the direction as possible.

Thus, the approach can be:

For a direction (forward or reversed):

   Find all possible start indices of s1 in the direction's path.

   For each start index:

       end = start + len(s1) - 1

       remaining_start = end + 1

       if remaining_start + len(s2) -1 >= len(S):

           continue (since not enough space for s2)

       check if S[remaining_start:] contains s2.

       if yes:

           return True for this direction.

   If no such occurrence found:

       return False.

So in code, for each direction, we can iterate through all possible starts of s1, and check s2 in the remaining part.

But how to find all possible starts of s1 efficiently.

So, the code could be:

def check_direction(s, s1, s2):

    len_s = len(s)

    len_s1 = len(s1)

    len_s2 = len(s2)

    if len_s1 + len_s2 > len_s:

        return False  # because after s1, there's not enough space for s2.

    start = 0

    while True:

        pos = s.find(s1, start)

        if pos == -1:

            break

        # Check if there's enough space after s1 for s2.

        end = pos + len_s1

        if end + len_s2 > len_s:

            start = pos + 1

            continue

        # Check if s2 is present from end onwards.

        if s.find(s2, end) != -1:

            return True

        # Move to next possible position.

        start = pos + 1

    return False

Wait, but the s.find(s2, end) returns the first occurrence of s2 starting from 'end'. So even if there's any occurrence after 'end', it will return True.

So this code would check for each occurrence of s1 in s, and see if there's any occurrence of s2 after the end of s1.

But in the code, the check is: if the substring s[end:] contains s2. Because s.find(s2, end) returns the first occurrence's index, if any. So if it's not -1, then there's at least one occurrence.

So the code for check_direction would return True if there exists any occurrence of s1 followed by s2.

Now, the code for check_direction has time complexity O(n) for finding s1's occurrences (since each 'find' moves start forward, but in the worst case it's O(n) for each occurrence) plus O(n) for checking s2 for each occurrence. But in practice, when s1 is found and s2 is checked, once a s2 is found, the function returns early.

So in the best case, the code is O(n) (find s1 once, check s2 once). In the worst case, like when s1 is 'a' and s is 'a...a' and s2 is not present, the code would be O(n^2) for s1's 'find' steps and O(n) for s2 checks each time. Which is 1e10 operations for n=1e5, which would be way too slow.

But given the problem constraints (time limit 1 second, which is about 1e8 operations), this code would not pass for such cases.

So this approach is not feasible. We need a better way.

Alternative idea: precompute the positions where s1 occurs, and for each of those positions, check if s2 occurs after. But again, this is the same problem.

So perhaps the key is to find the earliest occurrence of s1 such that the remaining string after s1's end has s2. But how to find that.

Alternative approach:

For the given direction's path:

   Find the first occurrence of s1.

   Then, check if s2 is present after the end of that s1. If yes, return True.

   Else, find the next occurrence of s1, but starting after the first occurrence's start. But how?

Wait, but the first occurrence of s1 may not leave enough space for s2. For example, s is 's1...s1...s2', where the first s1 is at position 0, but after that there's no s2, but the next s1 is at position 100, and after that there's s2. So in this case, the code would check the first s1, find no s2, then check the next s1, which may have s2.

But the code as written would process this correctly, but for large n, the time is prohibitive.

So what can be done?

We need a way to find, in O(n + m) time, if there exists a s1 followed by s2 in the string.

An efficient way would be to:

1. Find all possible start indices of s1 in the string.

2. For each start index, compute the end index.

3. Check if the substring starting at end index + 1 contains s2.

But again, this is O(k * (n)), where k is the number of s1 occurrences.

Alternative idea: precompute all possible end indices of s1, then find if any of these end indices have s2 starting after them.

But how to precompute the end indices.

Alternatively, use the Knuth-Morris-Pratt (KMP) algorithm to find all occurrences of s1 in O(n) time. Then, for each occurrence, check if s2 is present after.

But then, how to check if s2 is present after each occurrence. For this, we can precompute all occurrences of s2 and then, for each occurrence of s1, check if there's any occurrence of s2 that starts after the end of s1.

So here's the plan:

For a direction's path S:

   Find all the occurrences of s1 (start indices) and compute their end indices (start + len(s1) -1).

   Find all the start indices of s2.

   For each occurrence of s1's end index, check if there's a s2 start index >= (s1's end index + 1).

   If any s2 starts after (s1's end index + 1), then return True.

So the steps would be:

1. Use KMP to find all start indices of s1 in S.

   Let these be list_s1_starts.

   The corresponding end indices are list_s1_ends = [start + len(s1) - 1 for start in list_s1_starts]

2. Use KMP to find all start indices of s2 in S.

   Let these be list_s2_starts.

3. For each s1_end in list_s1_ends:

   Find if there exists any s2_start in list_s2_starts such that s2_start >= (s1_end + 1).

   Also, s2_start + len(s2) - 1 <= len(S) -1.

   But since list_s2_starts are valid, the s2_start is already a valid start.

   So, for each s1_end, check if there's a s2_start >= s1_end + 1.

   So the problem reduces to, for each s1_end, check if the minimal s2_start >= s1_end +1.

   To do this efficiently, we can sort list_s2_starts and perform a binary search for s1_end +1.

So steps:

- Preprocess list_s2_starts sorted.

- For each s1_end in list_s1_ends:

   compute target = s1_end + 1.

   perform binary search on list_s2_starts to find the first s2_start >= target.

   if such a s2_start exists, then return True.

Thus, the time for this approach is:

   O(n) for finding s1 and s2 occurrences with KMP.

   O(k log m) for each check, where k is the number of s1 occurrences, m is the number of s2 occurrences.

But for KMP, finding all occurrences of s1 and s2 is O(n) each.

Sorting the s2_starts takes O(m log m).

For each s1_end, binary search is O(log m).

Thus, total time is O(n + m + k log m), where k is the number of s1 occurrences.

This is acceptable even for large n (1e5) and large m (1e5) because O(n) is manageable.

Thus, this approach is feasible.

So the steps are:

Implement KMP for s1 and s2 to find all their start positions.

Sort the s2_start list.

For each s1_end in the list of s1's end positions:

   binary search s2_start list for the first value >= s1_end +1.

   if found, return True.

Else, after checking all s1_end, return False.

This way, even if there are 1e5 s1 occurrences, each binary search is O(log m), which is acceptable.

So now, the task is to implement KMP for finding all occurrences of s1 and s2 in a given string.

Alternatively, use the built-in string methods but with KMP-like efficiency.

But implementing KMP for this problem is necessary.

So let's proceed to implement KMP.

The KMP algorithm for finding all occurrences of a pattern in a text.

The KMP algorithm preprocesses the pattern to create a partial match table (failure function), then scans the text in O(n) time to find all occurrences.

So, for a pattern and text, we can find all start positions where the pattern occurs.

Thus, the code for KMP:

def kmp_failure_function(pattern):

    n = len(pattern)

    fail = [0] * n

    j = 0

    for i in range(1, n):

        while j > 0 and pattern[i] != pattern[j]:

            j = fail[j-1]

        if pattern[i] == pattern[j]:

            j += 1

            fail[i] = j

        else:

            fail[i] = 0

    return fail

def kmp_search(text, pattern, fail):

    n = len(text)

    m = len(pattern)

    j = 0

    occurrences = []

    for i in range(n):

        while j > 0 and text[i] != pattern[j]:

            j = fail[j-1]

        if text[i] == pattern[j]:

            j += 1

            if j == m:

                # occurrence at i - m +1

                start = i - m +1

                occurrences.append(start)

                j = fail[j-1]

        else:

            j = 0

    return occurrences

So, for a given text and pattern, generate the failure function, then use kmp_search to find all occurrences.

Thus, for each direction, we can:

- Generate the failure function for s1 and s2.

- Find all occurrences of s1 in the direction's path.

- Find all occurrences of s2 in the direction's path.

- Sort the s2 occurrences.

- For each s1 occurrence's end position (start + len(s1) -1), check if there's an s2 occurrence starting at >= end +1.

Thus, the code for check_direction becomes:

def check_direction(S, s1, s2):

    len_s1 = len(s1)

    len_s2 = len(s2)

    if len_s1 + len_s2 > len(S):

        return False

    # Find all occurrences of s1 in S.

    if len_s1 == 0 or len(S) < len_s1:

        s1_occurrences = []

    else:

        fail_s1 = kmp_failure_function(s1)

        s1_occurrences = kmp_search(S, s1, fail_s1)

    # Find all occurrences of s2 in S.

    if len_s2 == 0 or len(S) < len_s2:

        s2_occurrences = []

    else:

        fail_s2 = kmp_failure_function(s2)

        s2_occurrences = kmp_search(S, s2, fail_s2)

    # If no occurrences of s1 or s2, return False.

    if not s1_occurrences or not s2_occurrences:

        return False

    # Sort s2_occurrences.

    s2_occurrences.sort()

    # For each s1 occurrence, check if there's a s2 occurrence after.

    for s1_start in s1_occurrences:

        s1_end = s1_start + len_s1 -1

        # We need s2_start >= s1_end +1.

        target = s1_end + 1

        # Binary search in s2_occurrences for the first start >= target.

        low = 0

        high = len(s2_occurrences) -1

        found = False

        while low <= high:

            mid = (low + high) // 2

            if s2_occurrences[mid] >= target:

                found = True

                high = mid -1

            else:

                low = mid +1

        if found:

            # Check if s2_occurrences[low] is >= target.

            if s2_occurrences[low] >= target:

                return True

    return False

Wait, but after the binary search, if found is True, then the index is low.

But the code may have a mistake here.

The binary search code can be replaced with using the bisect module's bisect_left function.

In Python, the bisect module provides bisect_left, which returns the insertion point for the target in a sorted list. We can use this to find the first occurrence of s2_start >= target.

So:

import bisect

...

for s1_start in s1_occurrences:

    s1_end = s1_start + len(s1) - 1

    target = s1_end + 1

    idx = bisect.bisect_left(s2_occurrences, target)

    if idx < len(s2_occurrences):

        # s2_occurrences[idx] is >= target.

        return True

So, if any of the s1 occurrences leads to an idx < len(s2_occurrences), then there's a valid s2 occurrence after.

Wait, but in the code above, the loop returns True as soon as any occurrence of s1 has a s2 after. So for the first occurrence of s1 that has a s2 after, return True. But in the code, the for loop continues for all s1_occurrences, and only returns False if none are found.

But in the code, when using the bisect approach, for each s1_start in s1_occurrences, check if there's a s2 occurrence after. If even one such exists, return True.

But in the code above, the code returns True immediately when any s1 occurrence has a s2 after. So the code is correct.

But the code as written would for each s1 occurrence, check if there's a s2 occurrence after. As soon as one is found, return True.

Thus, the code for check_direction would be:

import bisect

def check_direction(S, s1, s2):

    len_s1 = len(s1)

    len_s2 = len(s2)

    # Check if the combined lengths exceed S's length.

    if len_s1 + len_s2 > len(S):

        return False

    # Find all occurrences of s1 and s2.

    if len_s1 == 0:

        s1_occurrences = []

    else:

        fail_s1 = kmp_failure_function(s1)

        s1_occurrences = kmp_search(S, s1, fail_s1)

    if len_s2 == 0:

        s2_occurrences = []

    else:

        fail_s2 = kmp_failure_function(s2)

        s2_occurrences = kmp_search(S, s2, fail_s2)

    # If either has no occurrences, return False.

    if not s1_occurrences or not s2_occurrences:

        return False

    # Sort s2_occurrences.

    s2_occurrences.sort()

    # Check each s1 occurrence.

    for s1_start in s1_occurrences:

        s1_end = s1_start + len_s1 - 1

        target = s1_end + 1

        idx = bisect.bisect_left(s2_occurrences, target)

        if idx < len(s2_occurrences):

            return True

    return False

Wait, but even if the s2_occurrences's start is after the target, but there's not enough space for s2 (i.e., the s2's start + len(s2) -1 exceeds the string length?), but according to the problem statement, the stations have no flags at A and B. So the problem states that the train moves all the time, so one flag cannot be seen twice. So the sequences are part of the list of flags that the train passes sequentially. So the sequences must be a contiguous subsequence of the flags. So for s2 to be present after s1's end, it must occur as a contiguous substring.

But when we find the start index of s2 in S, it's valid if from that start index, the next len(s2)-1 characters are present. So the code for finding s2 occurrences using KMP would already have checked that.

So the code for kmp_search would only return valid start positions where the entire pattern matches. So the s2_occurrences list contains only valid start indices where s2 is a substring of S.

Thus, the code for check_direction can safely check if any s2 starts after s1's end.

Thus, this approach should work.

Now, the code for the problem would read:

Read S, s1, s2.

Check forward direction: check_direction(S, s1, s2).

Check backward direction: check_direction(S[::-1], s1, s2).

Then:

forward_flag = check_direction(S, s1, s2)

backward_flag = check_direction(S[::-1], s1, s2)

Then output the corresponding result.

Now, let's test this code against the examples.

First example:

Input:

atob

a

b

S is 'atob', forward direction. s1 is 'a', occurs at 0. end is 0. target is 1. s2 is 'b', occurs at 3. So s2_occurrences is [3]. bisect_left([3], 1) is 0. idx is 0 < 1, so return True. So forward is True.

Backward direction: S[::-1] is 'bot a'. Wait, wait, S is 'atob' (length 4), reversed is 'b o t a'? Wait, 'atob' is 'a','t','o','b'. Reversed is 'b','o','t','a'.

So reversed S is 'botA'? Wait, no, the input is 'atob' which is 'a t o b' (assuming that's the exact letters). Reversed is 'b o t a'.

Check for s1='a' in reversed S. The reversed S is 'b o t a'. So 'a' occurs at position 3. So s1_end is 3. target is 4. But the reversed S is of length 4. So target is 4, but the reversed S has no characters after 3. So s2 is 'b'. Check if s2 occurs in reversed S after 4. So reversed S is 'bot a' (no, the reversed S is 'bot a'? Wait, S is 'atob', so reversed is 'bota'. Hmm, perhaps I should double-check.

Original S is 'atob' → 'a', 't', 'o', 'b'. Reversed is 'b', 'o', 't', 'a'. So reversed S is 'bota'.

Check in reversed S for s1='a' → occurs at index 3. s2 is 'b' → occurs at index 0. So s1 occurs at 3, end is 3. target is 4. So in reversed S, s2_occurrences is [0]. So idx = bisect.bisect_left([0], 4) → returns 1. Which is >= len([0]), so no. Thus, backward_flag is False.

Thus, the output is 'forward', which matches the example.

Second example:

Input:

aaacaaa

aca

aa

Original S is 'aaacaaa'.

Forward direction:

Check s1 is 'aca' and s2 is 'aa'.

In S: 'aaa c aaa' → looking for 'aca'. Let's see: indices 0: a a a c a a a → 'aca' starts at 2: a a a c a a a → indices 2-4: a c a → yes. So s1_occurrences is [2]. end is 4. target is 5. Now check s2 (aa) in S starting from 5. The substring from 5 is 'aa', which has 'aa' starting at 5 and 6. So s2_occurrences are [0,1,4,5]. After sorting, [0,1,4,5]. bisect_left for target 5 is index 3. s2_occurrences[3] is 5 >=5 → yes. So forward is True.

Backward direction: S reversed is 'aaacaaa' → 'aaacaaa' reversed is 'aaacaaa' (wait, original S is 'aaacaaa', which is 7 characters. Reversed is 'aaacaaa' → same as original? Because the first three are 'aaa', then 'c', then 'aaa'. So reversed would be 'aaa c aaa' → which is same as original. Wait, no: the original S is 'aaacaaa' → characters are a a a c a a a. Reversed is a a a c a a a. So same as original? Oh wait, yes. Because the first three a's, then c, then three a's. Reversed is same as original. So reversed S is same as original. So in the backward check, same as forward. So s1 is 'aca' occurs at position 2. end is 4. target is5. s2 is 'aa' occurs at 5, etc. So same as forward. So backward is also True. Thus, output is 'both', which matches the example.

So the code should work.

Now, the code for KMP needs to be implemented.

But let's proceed to write the code.

The code in Python:

Implement the KMP functions.

Read the three lines.

Check forward and backward.

Then output the result.

But also, note that in the problem statement, the first line is the path from A to B, and the backward direction is the reversed path.

So for the backward check, the code is:

reversed_S = S[::-1]

check_direction(reversed_S, s1, s2)

But since reversed_S is a new string, the code should work.

Thus, the complete code would be:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    def kmp_failure_function(pattern):
        n = len(pattern)
        fail = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and pattern[i] != pattern[j]:
                j = fail[j-1]
            if pattern[i] == pattern[j]:
                j += 1
                fail[i] = j
            else:
                fail[i] = 0
        return fail

    def kmp_search(text, pattern, fail):
        n = len(text)
        m = len(pattern)
        j = 0
        occurrences = []
        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = fail[j-1]
            if text[i] == pattern[j]:
                j += 1
                if j == m:
                    start = i - m + 1
                    occurrences.append(start)
                    j = fail[j-1]
            else:
                j = 0
        return occurrences

    def check_direction(S, s1, s2):
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_S = len(S)
        if len_s1 + len_s2 > len_S:
            return False
        if len_s1 == 0 or len_s2 == 0:
            return False
        # Find s1 occurrences.
        fail_s1 = kmp_failure_function(s1)
        s1_occurrences = kmp_search(S, s1, fail_s1)
        if not s1_occurrences:
            return False
        # Find s2 occurrences.
        fail_s2 = kmp_failure_function(s2)
        s2_occurrences = kmp_search(S, s2, fail_s2)
        if not s2_occurrences:
            return False
        # Sort s2_occurrences.
        s2_occurrences.sort()
        # Check each s1 occurrence.
        for s1_start in s1_occurrences:
            s1_end = s1_start + len_s1 -1
            target = s1_end + 1
            idx = bisect.bisect_left(s2_occurrences, target)
            if idx < len(s2_occurrences):
                return True
        return False

    # Read input.
    S = input_stream.readline().rstrip("\n").strip()
    s1 = input_stream.readline().rstrip("\n").strip()
    s2 = input_stream.readline().rstrip("\n").strip()

    forward = check_direction(S, s1, s2)
    backward = check_direction(S[::-1], s1, s2)

    if forward and backward:
        print("both", file=output_stream)
    elif forward:
        print("forward", file=output_stream)
    elif backward:
        print("backward", file=output_stream)
    else:
        print("fantasy", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
aaacaaa
aca
aa
""",
            "output": \
"""\
both
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

Sample Input 2:

aaacaaa

aca

aa

S is 'aaacaaa' → 'aaa c aaa'. len 7.

s1 is 'aca' (len 3). s2 is 'aa' (len 2).

forward check:

s1_occurrences: find 'aca' in 'aaacaaa'.

Looking at the pattern 'a','c','a'.

In the text 'a a a c a a a', the only occurrence is starting at index 2: 'a a a c a a a' → positions 2,3,4 are 'a','c','a' → yes. So s1_occurrences is [2]. s1_end=2+3-1=4. target=5.

s2_occurrences: find 'aa' in S. Occurrences are 0,1,4,5.

sorted, [0,1,4,5]. bisect_left([0,1,4,5],5) is 3. 3 <4 → yes. So returns True.

backward check: S reversed is 'aaacaaa' reversed, which is same as original. So same as forward. So both directions return True. So output 'both'.

Thus, the code works.

Now, the code uses KMP for efficient pattern matching, which is O(n) for each pattern. The bisect is O(log m) per s1 occurrence, which is manageable. Thus, this code should handle the worst cases within the time constraints.
</think>

```python
import bisect

def kmp_failure_function(pattern):
    n = len(pattern)
    fail = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j
        else:
            fail[i] = 0
    return fail

def kmp_search(text, pattern, fail):
    n = len(text)
    m = len(pattern)
    j = 0
    occurrences = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j-1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                start = i - m + 1
                occurrences.append(start)
                j = fail[j-1]
        else:
            j = 0
    return occurrences

def check_direction(S, s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    len_S = len(S)
    if len_s1 + len_s2 > len_S:
        return False
    
    fail_s1 = kmp_failure_function(s1)
    s1_occurrences = kmp_search(S, s1, fail_s1)
    if not s1_occurrences:
        return False
    
    fail_s2 = kmp_failure_function(s2)
    s2_occurrences = kmp_search(S, s2, fail_s2)
    if not s2_occurrences:
        return False
    
    s2_occurrences.sort()
    
    for start in s1_occurrences:
        end = start + len_s1 - 1
        target = end + 1
        idx = bisect.bisect_left(s2_occurrences, target)
        if idx < len(s2_occurrences):
            return True
    return False

S = input().strip()
s1 = input().strip()
s2 = input().strip()

forward = check_direction(S, s1, s2)
backward = check_direction(S[::-1], s1, s2)

if forward and backward:
    print("both")
elif forward:
    print("forward")
elif backward:
    print("backward")
else:
    print("fantasy")
```
