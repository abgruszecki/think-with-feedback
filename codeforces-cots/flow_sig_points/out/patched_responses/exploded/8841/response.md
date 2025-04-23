<think>
Okay, let's tackle this problem. Hmm, what's the problem statement again? Oh right, we need to determine if Lesha's problem is brand new by checking if any of the archive problems contain a permutation of Lesha's problem words as a subsequence. If not, output "Brand new problem!". Otherwise, find the archive problem with the highest similarity, where similarity is calculated based on the permutation with the least inversions when appearing as a subsequence.

First, let's understand the steps required.

So, for each archive problem, we need to check if there's any permutation of Lesha's words that exists as a subsequence in the archive's problem description. Among all such permutations that can form a subsequence, we have to choose the one with the smallest number of inversions. Then, compute the similarity p based on that inversion count.

But considering that n can be up to 15, checking all permutations (which is 15! ≈ 1e12) is impossible. So we need a smarter approach.

Wait, but the key here is that the permutation's order in the archive's problem must be a subsequence. So the problem is equivalent to finding a permutation of Lesha's words (all distinct) that appears in order as a subsequence in the archive's problem. For each archive problem, we need to find if such a permutation exists, and among those permutations, find the one with the minimal number of inversions (since the similarity is maximized when x is minimized).

But how do we find the permutation of Lesha's words that can be a subsequence in the archive's problem, with the minimal inversion count?

Alternative approach: For each archive problem, check if it contains all the words in Lesha's problem (since Lesha's problem has no duplicates, but the archive's problem might have duplicates). If the archive problem doesn't contain all n words, skip it. Otherwise, proceed to find the permutation that can be a subsequence with the least inversions.

So first, for each archive problem, check if each of Lesha's words is present at least once. If not, then this archive problem can't have a permutation of Lesha's words as a subsequence. So we can skip those.

Now, for archive problems that do have all the words, we need to find the permutation (as a sequence) that is a subsequence of the archive's problem, and among all possible such permutations, the one with the smallest inversion count.

The inversion count here is the number of pairs (i,j) in the permutation where i < j but the original order (Lesha's problem's order) has the permutation's i-th word before the j-th word. Wait, no. Wait, the original problem's words are in a certain order. The permutation's inversion count is the number of pairs in the permutation that are out of order compared to the original.

Wait, the note says: the inversion count is the number of pairs of words that follow in the permutation not in their original order. So, for example, original is "add two numbers", permutation is "numbers add two". The inversions are (numbers, add) and (numbers, two). So the inversion count here is 2.

So, for a permutation P of the original words, the inversion count is the number of pairs (i,j) where in P, i comes before j, but in the original order, j comes after i.

So the problem reduces to finding a permutation P of Lesha's words that is a subsequence of the archive's problem, and among all possible such P, choose the one with the minimal inversion count. Then compute p = n(n-1)/2 - x +1, where x is the inversion count. The higher the p, the better (since x is minimized).

But how do we find such a permutation P for each archive problem?

Hmm. Let's think about the archive's sequence. For Lesha's problem's words, we need to choose a permutation such that each word appears once in the permutation, and the permutation is a subsequence of the archive's problem. Then, among all possible such permutations, pick the one with the least inversion count.

This seems computationally expensive, but n is up to 15. Wait, 15! is way too big. So brute-forcing all permutations is not feasible.

Alternative idea: Since the archive problem's sequence is given, and we need to find the permutation that is a subsequence and has minimal inversions. How can we model this?

Wait, but the archive problem's sequence is fixed. So for each permutation of Lesha's words, we can check if it's a subsequence. But for each archive problem, this is O(n! * k), where k is the length of the archive problem. For n=15, this is impossible.

Thus, we need a smarter way. Let's think of the problem as trying to find the permutation of Lesha's words that can be a subsequence of the archive's problem and has the minimal possible inversion count.

But how?

Another angle: The minimal inversion count permutation is the one that is as close as possible to the original order. Wait, no. Because the inversion count is the number of inversions in the permutation compared to the original order. So the minimal inversion count would be 0 (the original order), but if that's a possible subsequence of the archive's problem, then that's the best. If not, then we need to find permutations with the least inversions.

So the approach would be for each archive problem:

1. Check if all the words in Lesha's problem are present in the archive's problem. If not, skip.

2. Then, check if the original order of Lesha's words is a subsequence of the archive's problem. If yes, then x=0, which is the best possible. So p is maximum, and this archive problem is a candidate with maximum similarity.

3. If not, then we need to find other permutations. But how? For n up to 15, even n=15, checking all permutations is impossible.

Alternative approach: The problem of finding a permutation of Lesha's words that is a subsequence of the archive's problem and has minimal inversions is equivalent to finding a permutation that is a subsequence and is as close as possible to the original order.

But how can we model this? Hmm. Perhaps we can model this as a dynamic programming problem, where we track the positions of the words in the archive's sequence and the order in which they are selected.

Wait, perhaps the key is to model the problem as a state where we track the next possible positions for each word in the permutation. But I'm not sure.

Alternatively, here's an idea inspired by the problem of finding the longest common subsequence (LCS) or the problem of checking if a string is a subsequence of another.

For the archive problem's sequence S, we can precompute for each word in Lesha's problem, the indices where it occurs in S. Then, the problem reduces to finding an order of Lesha's words (permutation) such that each subsequent word in the permutation appears after the previous in S. And among all such permutations, find the one with the minimal inversion count.

But how do we efficiently find such a permutation?

Another idea: the minimal inversion count is achieved when the permutation is as lexicographically ordered as possible, but considering the positions in S. But I'm not sure.

Alternatively, think of the permutation as a sequence of positions in S. The permutation must be a sequence of indices i_1 < i_2 < ... < i_n, where each S[i_k] is the permutation's k-th word, and all n words are covered once.

But how do we find the permutation of words with such indices that the inversion count compared to the original order is minimized.

Wait, inversion count is based on the permutation's order compared to the original. So for each possible permutation that is a subsequence of S, compute the inversion count, then pick the smallest.

But for n=15, that's 15! permutations. Which is way too big.

So, we need a way to model the problem that allows us to find the permutation with minimal inversion count without enumerating all possibilities.

Let's think of this as a graph problem. Each state represents a subset of words already chosen, and the order in which they were chosen. For each state, we track the last position in S where the previous word was found, and the inversion count so far.

But even this seems challenging. For example, for n=15, the number of subsets is 2^15 = 32768. But the order in which they were chosen is important for the inversion count.

Alternatively, we can model the state as the subset of words used, and the order in which they were added. But this again is not feasible for n=15.

Alternative approach inspired by dynamic programming:

For each position in S, we can track the possible subsets of Lesha's words that have been matched up to that point, along with the order in which they were matched, and the inversion count. But again, for S of length up to 500,000 and n=15, this is not feasible.

Wait, but perhaps the order in which the words are chosen (the permutation) directly affects the inversion count. So the inversion count is determined by the permutation's order. To minimize inversion count, perhaps the permutation should be as close as possible to the original order.

But how?

Another idea: The minimal inversion count permutation that is a subsequence of S is the one that, in the earliest possible positions in S, follows the original order as much as possible. But I'm not sure.

Alternatively, think of the permutation as a rearrangement of the original order. The problem is similar to finding a permutation that is a subsequence of S, and has the minimal inversion count relative to the original order.

This sounds like a problem that can be modeled using the greedy algorithm. For example, try to arrange the words in the original order as much as possible, but when that's not possible, make the minimal necessary changes.

But how to implement this?

Alternatively, here's a possible approach:

We need to find a permutation of the original words that is a subsequence of S, and has the minimal inversion count. Let's model this as a problem of choosing positions in S where each word appears once, and their order in S forms the permutation.

The inversion count is the number of pairs in the permutation that are inverted compared to the original order.

To minimize the inversion count, we want as many pairs as possible to be in the original order.

So, the problem reduces to finding a permutation that is a subsequence of S, and as "close" as possible to the original order. But how to find this efficiently.

Let me think. Suppose we model the problem as a sequence of positions in S where we select words from Lesha's problem, such that each subsequent word in the permutation is after the previous in S. The inversion count is the number of pairs in the permutation that are in reverse order compared to the original.

So, the minimal inversion count would be achieved by choosing a permutation that is as close to the original order as possible, given the constraints of S.

An efficient way to do this is to find the earliest possible occurrence of the words in the original order, but allowing for some changes. But how to model this.

Alternatively, this seems similar to the problem of finding the permutation of the words that can be embedded as a subsequence in S with the minimal inversion count. To find this, we can model it as a problem of dynamic programming where each state represents the current position in S and the subset of words selected, along with their order.

But even that seems challenging.

Wait, perhaps the key is to model the permutation as the order in which the words are selected from S, and for each possible subset of words and their order, track the minimal inversion count. But the order is what's important here, which complicates things.

Alternatively, perhaps we can model the problem with a dynamic programming approach where we track the order of the selected words based on the original indices.

Let me think: For example, suppose we have the original order of words as a_1, a_2, ..., a_n. The inversion count is the number of pairs (i,j) where i < j in the original order but j comes before i in the permutation.

So, the problem is to select a permutation P of the original words that is a subsequence of S, and among all such permutations, the one with the least inversion count.

An alternative way to compute the inversion count is to compare the permutation's order to the original order. For each word in the permutation, count how many words that come after it in the permutation were before it in the original order. Sum all these counts.

So, inversion count x is sum over each word in the permutation of the number of words to the right of it in the permutation that are earlier in the original order.

Hmm. For example, original order is [A, B, C, D]. If permutation is [B, A, D, C], then for B, there's one word (A) to the right that is earlier in the original. For A, none. For D, one (C). For C, none. Total x=2.

So, inversion count is the sum of inversions in the permutation compared to the original.

To find the permutation that is a subsequence of S and has the minimal x, perhaps we can model this as a dynamic programming problem where the state represents which words have been selected and their order, and the current position in S. But with n=15, even the number of possible subsets is 2^15=32768, but considering the order, it's 15! possible states, which is impossible.

So, this approach isn't feasible.

Alternative idea: Since the minimal inversion count is desired, perhaps the optimal permutation is the one that, as much as possible, follows the original order. So, perhaps the optimal permutation is the original order if it exists as a subsequence. If not, find the minimal changes needed to make it a subsequence, which would result in minimal x.

But how do we check if the original permutation is a subsequence?

Yes. So first, for each archive problem, after checking that all words are present, check if the original order is a subsequence. If yes, then x=0, which is minimal, and thus this archive problem's similarity is maximized. So, in that case, the similarity is n(n-1)/2 -0 +1 = (n(n-1)/2 +1). So, in this case, this is the best possible.

So, for any archive problem where the original order is a subsequence, we can immediately take that permutation (x=0) and compute p. So, the first step for each archive problem is to check if the original order is a subsequence. If yes, then we don't need to consider any other permutations.

If the original order is not a subsequence, then we need to find other permutations.

But checking for the original order being a subsequence is O(k), where k is the length of the archive's problem. For each archive problem, that's feasible since m is up to 10 and k up to 5e5. So for each archive problem, first check if all words are present, then check if original order is a subsequence.

So, the algorithm could be:

For each archive problem:

1. Check if all Lesha's words are present. If not, skip.

2. Check if the original order is a subsequence. If yes, then x=0, p is maximal for this problem.

3. Else, find the permutation of Lesha's words that is a subsequence and has minimal x.

But how to do step 3?

For step 3, since n can be up to 15, trying all permutations is impossible. So, we need an efficient way.

Hmm. But for n=15, 15! is way too big. So, we need a smarter approach.

Alternative approach: for each archive problem, when the original order is not a subsequence, the minimal x is the minimal possible among all possible permutations that are subsequences. But how to find that.

Wait, perhaps the problem is similar to the problem of finding the lex order smallest permutation that is a subsequence. But here, the order is determined by the inversion count.

Alternatively, think of it as trying to arrange the words in a permutation that is as close as possible to the original order, but in a way that allows it to be a subsequence of S.

Another idea: For the archive's problem S, we can model the problem as a directed acyclic graph (DAG), where each node represents a state of selected words and their order, and edges represent adding a new word to the permutation. But again, with n=15, this approach is not feasible.

Alternative plan:

If the original order is not a subsequence, then the minimal x is the minimal possible x such that there exists a permutation with x inversions that is a subsequence of S.

But how to compute that? Let's think of the inversion count as the measure of how different the permutation is from the original. So, the goal is to find the permutation that is as similar as possible to the original order (in terms of inversion count) that is a subsequence.

But I'm stuck here. Let's think of an alternative approach.

Let's precompute for each possible subset of Lesha's words and their order. For example, for each possible permutation, check if it's a subsequence. But even for n=10, this is 3.6 million permutations, which might be manageable if each check is efficient. But for n=15, it's impossible.

Wait, but the archive's problem's length can be up to 500,000, and checking if a permutation is a subsequence would take O(k) time, which is 5e5 per permutation. For n=10, that's 3.6e6 * 5e5 = 1.8e12 operations. That's way too slow.

Thus, this approach is not feasible.

Alternative idea: Since we need the permutation to be a subsequence of S, perhaps we can model this as a problem of finding the permutation with the minimal inversion count that is a subsequence. To find this, perhaps we can model the problem as a dynamic programming approach where we track the current positions in S and the selected words, along with some measure of inversion count.

But again, this seems challenging.

Wait, perhaps the problem can be rephrased as follows: find a permutation P of Lesha's words such that P is a subsequence of S, and the permutation P has the minimal number of inversions compared to the original order. We need to find such a permutation, if any.

But how to model this.

An alternative approach is to model the problem as a state in DP where the state is the set of words used so far and the last position in S where a word was taken. For each step, we choose the next word to add such that its next occurrence in S after the last position is the earliest possible. This is similar to the standard approach for finding the minimal sequence in a subsequence.

But this approach gives us the earliest possible permutation (lex order), but not necessarily the one with minimal inversion count.

But perhaps we can modify this approach to track not only the earliest possible positions but also the inversion count. Hmm.

Alternatively, for each position in S and for each subset of Lesha's words, track the minimal inversion count so far. But even with n=15, the number of subsets is 2^15=32768. For each subset and position in S (up to 5e5), this would be 5e5 * 3e4 = 1.5e10 states. That's way too much.

So this is not feasible.

Alternative Idea:

Another way to look at the problem: the permutation P is a sequence of the Lesha's words. To be a subsequence of S, the order of the words in P must appear in S in the same order. The inversion count x is the number of pairs in P that are inverted compared to the original order.

We need to find the permutation P that is a subsequence of S and minimizes x.

The inversion count x can be expressed as the number of inversions in the permutation when compared to the original order.

Thus, the problem reduces to finding the permutation of Lesha's words that is a subsequence of S and has the least possible inversion count.

But how?

Let me think about a way to model the permutation's order. For each possible permutation P, x is the inversion count. We need to find the P with minimal x that is a subsequence of S.

But for n=15, this is impractical.

Alternative approach inspired by the standard method for finding the minimal number of inversions in a permutation that is a subsequence of S. Wait, but I'm not aware of any standard method for this.

Wait, perhaps we can model this as a problem where for each word in the permutation, we track the earliest position in S where it can appear, given the previous words in the permutation and their positions.

This is similar to the standard method of checking if a particular sequence is a subsequence of S.

For example, to check if the original order is a subsequence, we can iterate through S and find the positions in order. If that's possible, then x=0.

So, the standard approach for checking if a sequence is a subsequence is to walk through S and find the first occurrence of the first word, then the first occurrence after that of the second word, etc.

If during this process we can find all words in order, then it's a subsequence.

So, perhaps for permutations other than the original, we can use a similar approach but with the permutation's order.

But again, trying all permutations is impossible.

Alternative Idea:

If the original order is not a subsequence, perhaps the next best option is to find a permutation that differs minimally from the original order. For example, swap a few adjacent pairs where necessary to make the permutation a subsequence of S. The minimal x would correspond to the minimal number of such swaps.

But how to model this.

Alternatively, we can model the problem as a DAG where each node represents the current state of the permutation's formation. Each node would track:

- The current position in S.

- The set of words already included in the permutation.

- The order in which they were included.

But again, this is not feasible for n=15.

Another Idea:

Let me think of the inversion count as the sum of inversions between all pairs. So, the inversion count x is the number of pairs (i,j) in the permutation where i comes before j in the permutation but i was after j in the original order.

So, to minimize x, we want as many pairs as possible to be in the same order as the original.

This suggests that the optimal permutation P is the one that, for each possible pair, follows the original order as much as possible.

Thus, the problem reduces to finding a permutation P that is a subsequence of S and has as many pairs in the original order as possible.

But how to find this.

Hmm. Perhaps this is similar to the problem of finding the longest increasing subsequence (LIS), where the "increasing" is defined as following the original order. But here, we need the entire permutation, not just a subsequence.

Alternatively, for each word in Lesha's problem, we can track the positions where they appear in S. Then, the goal is to select one occurrence of each word in S, such that their order in S forms a permutation of the words, and the permutation has minimal inversion count.

But how to model this selection.

Alternatively, this seems like a problem that can be modeled using dynamic programming, where the state is a bitmask representing which words have been selected so far, and the last position in S. For each state, we track the minimal inversion count up to that point.

Here's the idea:

- The DP state is a bitmask (indicating which words are included) and the last index in S where the previous word was taken.

- For each state, we can try to add a new word (not yet included) and find the next occurrence of that word in S after the last index. For each possible new word, we compute the number of inversions added by adding this word next.

The number of inversions added would be the number of words in the original order that are after this word but haven't been added yet. Because adding this word now would mean that any such words added later would contribute to the inversion count.

Wait, but inversion count is determined by the order in the permutation compared to the original. For example, if in the original order, word A comes before B, but in the permutation, B comes before A, then that's one inversion.

So, when building the permutation incrementally, the inversion count can be computed as the sum of, for each new word added, the number of words already in the permutation that appear after it in the original order. Because those words were added before this one, but in the original order they come after, thus forming inversions.

Wait, no. Let's think: when adding a new word, the inversion count contributed is the number of words already in the permutation that come after this new word in the original order. Because those words are in the permutation before the new word, but in the original order, the new word is before them. So each such pair contributes one inversion.

For example, original order is A B C D. Suppose we add C first. Then, when adding A next, the inversion count would be 1 (since C comes after A in the original order). Then adding B would contribute 2 inversions (C and A are before B, but in the original order B comes after A and before C). Wait, no. The inversion count is the sum of pairs in the permutation where a word comes before another in the permutation but comes after in the original.

So, when adding a new word to the permutation, the number of inversions added is the number of words already in the permutation that are after the new word in the original order.

So, if the new word is the i-th word in the original order, then any word already in the permutation that has an original index greater than i contributes an inversion. So for each new word, the contribution is the number of words already present with higher original indices.

Thus, the inversion count can be tracked incrementally. So, for a DP state, we can track:

- The set of words used (bitmask).

- The last index in S where the last word was taken.

- The current inversion count.

The goal is to find the minimal inversion count achievable for the full set of words.

The transitions would be: for each possible next word (not in the current set), find all possible positions in S where the next word occurs after the last index. For each such occurrence, add the next word to the set and update the inversion count.

But for n=15, the bitmask can be up to 2^15 = 32768 possible states. For each state, the last index can be up to 5e5, which is way too big to track. So this approach is not feasible.

Alternative Idea: Instead of tracking the last index, track for each word the next occurrence after a certain position. Precompute for each position in S and for each word, the next occurrence index. Then, during the DP transitions, we can quickly find the next occurrence of a word.

Yes, precomputing the next occurrence for each word and position can help.

Here's how to precompute next occurrence:

For each word in Lesha's problem, precompute a list of indices where it appears in S. Then, for a given position, the next occurrence of the word is the smallest index in its list that is greater than the current position.

This can be done using binary search.

So, for each word w in Lesha's problem, we have a sorted list pos_w of indices where w appears in S.

Then, given a current position pos in S, the next occurrence of w after pos can be found by finding the first index in pos_w that is > pos.

If pos_w is empty, then the word can't be used, but we already checked earlier that all words are present in the archive's problem.

So, for each word, we can have a list of its occurrence positions in S, sorted.

Thus, during DP transitions, when we have a current position and a candidate next word, we can binary search in the word's list to find the next occurrence after the current position. If there's none, then this transition is not possible.

So, the DP approach would be:

- State: bitmask (representing used words), last position in S, and inversion count.

But again, even with this, the number of states is 32768 (bitmask) * 5e5 (last positions) * (max inversion count possible). Which is way too large.

But perhaps the inversion count can be tracked as part of the state and we can keep the minimal inversion count for each (bitmask, last position) pair.

Alternatively, for each bitmask, track the minimal inversion count and the earliest possible last position in S. Because the earlier the last position, the more options we have for subsequent words. So, for each bitmask, we can track the minimal inversion count and the earliest possible last position.

This is similar to the approach used in the problem of finding the lex smallest subsequence, where we track the earliest positions.

So, for each bitmask, we can track two things: the minimal inversion count achieved so far for that subset, and the earliest position in S where that subset can be formed with that inversion count.

Thus, the state is the bitmask, and for each bitmask, we store the minimal inversion count and the earliest position where this can be achieved.

This approach could work as follows:

Initialize the DP with the empty set (mask 0), inversion count 0, and position -1 (indicating that we need to find the first occurrence of a word).

For each state (mask, inv_count, pos), we can iterate through all words not in mask. For each such word w:

- Find the next occurrence of w in S after pos. If none, skip.

- Compute the new inversion count: inv_count + number of set bits in mask that correspond to words with original index higher than w's original index. Because those words are already in the permutation, and since w is added next, each of those words contributes one inversion.

- The new mask is mask | (1 << w_index).

- If this new state (mask | (1 << w_index)) has not been recorded yet, or if the new inversion count is less than the previously recorded one, or if the inversion count is the same but the new position is earlier, then we update the DP for this new mask.

This way, for each mask, we track the minimal possible inversion count and the earliest possible position to achieve that count.

Once all transitions are processed, the minimal inversion count for the full mask (all words included) would be the answer.

If the DP for the full mask exists, then x is that minimal inversion count. Otherwise, no permutation exists (but we have already checked that all words are present).

This seems promising. Let's formalize this:

For each word in Lesha's problem, assign an index from 0 to n-1 based on their original order. So, original_order = [w0, w1, ..., w_{n-1}].

For a given word w, its original index is i where w == original_order[i].

For a subset mask, and a new word w (not in mask), the number of words already in the mask that have original index greater than w's index is equal to the number of bits set in mask that are higher than the original index of w.

This is because each such word in the mask that comes after w in the original order contributes an inversion when w is added next.

Thus, when adding w to the permutation next, the inversion count increases by the number of such bits.

The DP state will track for each mask the minimal inversion count and the earliest position in S where this is achieved.

We can model this as a dictionary for each mask, storing the minimal inversion count and the earliest position.

The steps for each archive problem:

1. Check if all Lesha's words are present in S. If not, skip.

2. Check if the original order is a subsequence. If yes, x=0. Process this as the best possible.

3. Else, use the DP approach described above to find the minimal x.

If the DP for the full mask exists, then compute p = (n(n-1)/2) -x +1.

Else, no permutation exists (but since we checked that all words are present, there must be at least one permutation. But maybe the DP approach would have found it).

Wait, but the initial check that all words are present in S ensures that there's at least one permutation (the one that uses the earliest occurrence of each word, regardless of order). But how can that be a subsequence? For example, S contains all the words, but not in any order. Wait, the permutation can be in any order, but the words must appear in that order as a subsequence. So, as long as all words are present, there's at least one permutation possible.

So, for the DP approach, as long as all words are present, the full mask will be reachable.

Thus, the algorithm for step 3 is:

- Precompute for each word in Lesha's problem, the list of positions in S where it occurs. If any word has an empty list, the archive problem is skipped.

- Precompute next occurrence for each word and position.

- Initialize the DP: a dictionary where the key is the mask, and the value is a tuple (min_inversion_count, earliest_position).

- Start with mask 0, inversion count 0, position -1.

- For each mask in order of increasing number of bits, process each possible transition to add a new word.

- For each transition, compute the new inversion count and find the next position in S where the new word occurs after the current earliest_position.

- Update the DP accordingly.

Once all transitions are processed, the minimal inversion count for mask (1<<n) -1 is x. Then compute p.

This approach has a complexity of O(2^n * n * log k), where k is the length of S. For n=15, 2^15 is 32768. For each mask, there are up to n transitions (adding each possible word not in the mask). For each transition, binary search takes O(log k) time.

Thus, for n=15, m=10, and k up to 5e5, this would be manageable.

Now, let's think about the steps to implement this.

Implementation Steps:

1. Read n and Lesha's words. Ensure they are unique (as per problem statement).

2. Read m archive problems. For each:

   a. Read k and the list of words S.

   b. Check if all Lesha's words are present in S. We can do this by counting the occurrences of each word. If any of Lesha's words is not present, skip this archive problem.

   c. Precompute for each Lesha's word, the list of indices in S where it occurs. For example, for each word in Lesha's list, collect all positions in S where it appears. Store this as a dictionary: positions[word] = list of indices (sorted).

   d. Check if the original order is a subsequence. This can be done by iterating through S and checking if the original sequence can be formed. If yes, then x=0, and compute p.

   e. If not, proceed to compute the minimal x using the DP approach.

   f. For the DP approach:

      i. Precompute the next occurrence for each word and current position. For a given current position, the next occurrence of a word can be found by binary search in the word's positions list.

      ii. Initialize the DP. For each mask, track the minimal inversion count and earliest position.

      iii. Process each mask in order of increasing set bits (BFS-like approach). For each mask, and for each possible word not in the mask, compute the next occurrence of the word after the current earliest position. For each possible transition, compute the new inversion count and update the DP for the new mask if it's better.

      iv. After processing all masks, retrieve the minimal inversion count for the full mask. Compute x and p.

   g. Compare this p with the current maximum across all archive problems. Keep track of the archive problem with the highest p (and smallest index in case of ties).

3. After processing all archive problems, output the result.

Now, let's think about the code structure.

First, for each archive problem, steps:

Check if all words are present. For example, using a Counter for S's words. But since S can have duplicates, but Lesha's words are unique, we just need to ensure that each Lesha's word is present at least once in S.

Then, check if the original order is a subsequence. To do this:

Initialize a pointer for Lesha's original list (original_ptr = 0). Iterate through S's words. For each word in S:

   if it matches original_order[original_ptr], increment original_ptr. If original_ptr reaches n, break.

If original_ptr == n, then the original order is a subsequence.

If not, proceed with the DP approach.

Now, for the DP approach:

Each Lesha's word has an original index (0-based) based on their order in the original problem. For example, original_order[0] is the first word, original_order[1] is the second, etc.

For a given word w in Lesha's words, its index is original_order.index(w).

But since the original list has unique words, we can create a dictionary to map each word to its original index for O(1) lookups.

Then, for the DP:

We need to track for each mask (subset) the minimal inversion count and the earliest possible position in S where this subset can be formed.

The DP can be represented as a dictionary where the keys are masks, and the values are tuples (min_inversion, earliest_position).

Initialize the DP with mask 0: {0: (0, -1)}.

Then, process the masks in order of increasing number of bits. For each mask in the current DP:

   For each word not in the mask:

      Get the word's original index.

      Get the list of positions where the word appears in S.

      current_earliest_position = dp[mask][1]

      Using binary search, find the smallest position in the word's positions list that is > current_earliest_position. If no such position exists, skip (but this can't happen since we checked all words are present).

      new_position = pos (the found position).

      new_mask = mask | (1 << word's original index)

      The number of new inversions added is the number of set bits in mask that have original indices > current word's original index.

      new_inversion = current_inversion + count of set bits in mask where their original index > current word's original index.

      Now, check if the new_mask is already in the DP. If not, add it with (new_inversion, new_position). If it is present, compare the new_inversion with the existing one. If new_inversion is smaller, or same inversion but new_position is earlier, update.

Thus, for each mask and each possible next word, we generate the new state and update the DP.

This way, after processing all possible transitions, the minimal inversion count for the full mask (all bits set) is found.

Once we have x = minimal_inversion_count, compute p = n*(n-1)//2 - x +1.

Now, comparing this across all archive problems, we select the one with the highest p. If multiple have the same p, select the one with the smallest index.

Now, let's think about implementing this.

First, for the DP, we need to process masks in order of increasing number of bits. This is to ensure that when we process a mask, all masks with fewer bits have already been processed. This can be done by iterating from mask 0 to mask (1<<n)-1, grouped by the number of set bits.

Alternatively, for each mask in the DP, we can process them in order of the number of bits.

Now, code structure:

For each archive problem:

   Check if all Lesha's words are present.

   If yes:

      Check if original order is a subsequence.

      If yes: x=0, p= n*(n-1)//2 +1.

      else:

         Precompute for each Lesha's word, the list of positions in S where they appear.

         Create a dictionary: word_to_indices = {word: list_of_indices}

         Create a dictionary word_to_original_index: maps each word to its index in original_order.

         Initialize DP as a dictionary.

         dp = {0: (0, -1)}

         for mask in dp, processed in order of increasing number of bits:

             current_inversion, current_pos = dp[mask]

             for each word in Lesha's words not in mask:

                 original_idx = word_to_original_index[word]

                 indices = word_to_indices[word]

                 # find the first index in indices greater than current_pos

                 # using bisect.bisect_right

                 idx_in_list = bisect.bisect_right(indices, current_pos)

                 if idx_in_list == len(indices):

                     continue  # no occurrence after current_pos (but this shouldn't happen)

                 new_pos = indices[idx_in_list]

                 # compute number of bits set in mask with original index > original_idx

                 count = 0

                 temp_mask = mask

                 while temp_mask:

                     lsb = temp_mask & -temp_mask

                     bit_pos = (lsb).bit_length() -1  # original index of the word in the mask

                     if bit_pos > original_idx:

                         count +=1

                     temp_mask &= temp_mask -1

                 new_inversion = current_inversion + count

                 new_mask = mask | (1 << original_idx)

                 # update dp

                 if new_mask not in dp:

                     dp[new_mask] = (new_inversion, new_pos)

                 else:

                     existing_inversion, existing_pos = dp[new_mask]

                     if new_inversion < existing_inversion or (new_inversion == existing_inversion and new_pos < existing_pos):

                         dp[new_mask] = (new_inversion, new_pos)

         # after processing all masks, check full mask

         full_mask = (1 << n) -1

         if full_mask in dp:

             x = dp[full_mask][0]

             p = (n*(n-1)//2) - x +1

         else:

             # impossible since all words are present

             pass

      compare p with the current best.

Now, but wait, how to process the masks in order of increasing bits. Because when you generate new masks from a current mask, the new mask has more bits than the current one. But in the code above, the order in which masks are processed may not follow the increasing bits order. So this could lead to incorrect transitions.

Thus, to process masks in order of the number of bits set (from 0 to n), we can use a list of masks for each possible bit count.

For example, we can precompute all masks grouped by the number of set bits. But for dynamic programming, it's better to generate masks in order of increasing bits.

An alternative approach is to use a BFS-like approach, where masks are processed in order of the number of set bits. So, for each bit count from 0 to n, process all masks with that many bits.

This can be done by maintaining a list of masks for each bit count. For example:

bit_count = 0: [0]

bit_count = 1: all masks with exactly one bit set.

and so on.

But how to generate this list? For each bit_count from 0 to n:

   generate all masks with exactly bit_count bits set.

But for n=15, this is manageable.

Alternatively, during the processing of the DP, we can track masks in the order of their bit counts. For example, process all masks with 0 bits first, then 1 bit, and so on.

But this may require more memory.

Alternatively, during the DP processing, for each mask, once we generate a new_mask, we can add it to a queue or a list, ensuring that masks are processed in order of increasing bit counts.

But for the code, perhaps using a queue where masks are processed in the order of their bit counts is the way to go.

Wait, perhaps the code can use a list of masks for each bit count, and process them in order from 0 to n.

For example:

max_bits = n

for bit_count in 0 to max_bits:

   for each mask in the list of masks with bit_count bits:

       process the mask (i.e., try adding each possible new word)

This way, masks are processed in order of increasing bit counts, which ensures that when we process a mask with bit_count bits, all masks with bit_count-1 bits have already been processed.

Thus, in code:

original_order = Lesha's words list

word_to_original = {word: idx for idx, word in enumerate(original_order)}

For each archive problem:

   # pre-check steps...

   # original_order is not a subsequence. Proceed to DP.

   # precompute word_to_indices.

   # precompute next occurrence.

   # initialize DP.

   dp = {}

   dp[0] = (0, -1)

   # process masks in order of increasing bit count.

   for bit_count in range(n):

       # iterate over all masks with bit_count bits.

       # but how to get these masks?

       # for each mask in dp:

       #   if bin(mask).count('1') == bit_count:

       #       process it.

       # but this is not efficient.

       # alternative approach: maintain a list of masks for each bit_count.

       # So for each bit_count, we process all masks with that number of bits.

       # So, for each mask in the current DP with bit_count bits, process it.

       # So, collect all masks in the current dp with bit_count bits.

       current_masks = [mask for mask in dp if bin(mask).count('1') == bit_count]

       for mask in current_masks:

           current_inversion, current_pos = dp[mask]

           # iterate through all words not in mask.

           for word in original_order:

               if (mask & (1 << word_to_original[word])) == 0:

                   # word is not in the mask.

                   # find next occurrence of this word after current_pos.

                   indices = word_to_indices[word]

                   idx_in_list = bisect.bisect_right(indices, current_pos)

                   if idx_in_list >= len(indices):

                       # no occurrence after current_pos. Skip.

                       continue

                   new_pos = indices[idx_in_list]

                   original_idx = word_to_original[word]

                   # count the number of set bits in mask with original index > original_idx.

                   count = 0

                   # iterate through the set bits in mask.

                   temp_mask = mask

                   while temp_mask:

                       lsb = temp_mask & -temp_mask

                       bit_pos = (lsb).bit_length() -1

                       if bit_pos > original_idx:

                           count +=1

                       temp_mask &= temp_mask -1

                   new_inversion = current_inversion + count

                   new_mask = mask | (1 << original_idx)

                   # update the dp for new_mask.

                   if new_mask not in dp:

                       dp[new_mask] = (new_inversion, new_pos)

                   else:

                       existing_inversion, existing_pos = dp[new_mask]

                       if new_inversion < existing_inversion or (new_inversion == existing_inversion and new_pos < existing_pos):

                           dp[new_mask] = (new_inversion, new_pos)

   # after processing all bit counts up to n-1, check the full mask.

   full_mask = (1 <<n) -1

   if full_mask not in dp:

       # impossible, since all words are present.

       continue

   x = dp[full_mask][0]

   p = (n*(n-1)//2) -x +1

Thus, this approach processes the masks in the order of their bit count. For each mask, when processing, all possible transitions to new masks with higher bit counts are considered.

This should ensure that the DP is built correctly.

But for n=15, the code may take a while. But given the constraints (m=10, n=15), and each mask being processed in O(n) time, and masks count up to 32768, this is manageable.

Now, code implementation.

But there's a mistake here: in the code above, for each bit_count from 0 to n-1, we process masks with that bit_count. But for a mask with bit_count bits, adding a word (not in the mask) would create a mask with bit_count+1 bits. Thus, for each bit_count, the next masks are processed in the next iteration.

But the code as written loops bit_count from 0 to n-1. Wait, because when bit_count is up to n-1, the maximum possible bit_count is n. But perhaps the code should loop up to n-1, because the full mask has n bits. So, for example, for a mask with n-1 bits, adding one more word will create a mask with n bits. So, the loop for bit_count up to n-1 would process all masks that can generate the full mask.

But in the code example above, the loop runs from 0 to n-1 (since in Python, range(n) gives 0 to n-1). For n=15, it's 0 to 14. Then, masks with 14 bits can generate masks with 15 bits (full mask).

But in the code, after processing all bit_count up to 14, the full mask (15 bits) is checked.

Yes, that should be correct.

Now, testing the code on the first example:

Sample Input 1:

4

find the next palindrome

1

10 find the previous palindrome or print better luck next time

Original order is ["find", "the", "next", "palindrome"]

Check if this is a subsequence of S.

S is ["find", "the", "previous", "palindrome", "or", "print", "better", "luck", "next", "time"]

In the original order, the fourth word is "next", which is not present until the 8th index (0-based). The third word in the original is "next", and the fourth is "palindrome". But in S, "next" is at position 8, and "palindrome" is at position 3. So the original order is not a subsequence. Thus, proceed to DP.

The minimal inversion count permutation would be ["find", "the", "palindrome", "next"], which has 1 inversion (palindrome and next). So x=1. Then p=4*3/2 -1 +1 =6.

Sample Output is "[:||||||:]" which has 6 |'s.

Thus, the code should compute x=1.

The DP approach should find this permutation.

Thus, the code should correctly compute x=1 for this case.

Another sample input is the third example, where the output is 4 |'s, implying p=4.

Original_order: these papers are formulas.

Archive problem 1's S is "what are these formulas and papers".

The original order is "these papers are formulas".

Check if this is a subsequence of S. The S is:

["what", "are", "these", "formulas", "and", "papers"]

Original_order is ["these", "papers", "are", "formulas"].

In S, the words are "are" comes before "these", so the original order is not a subsequence.

Thus, the code would proceed to find the minimal x. The permutation that is a subsequence would be "are these papers formulas", but I'm not sure. The actual permutation that is a subsequence and has minimal inversion count is "these are papers formulas" perhaps. But the code should find the correct minimal x.

But regardless, the code should compute the correct x.

Now, code implementation steps:

First, precompute for each Lesha's word the positions in S.

Then, for the DP:

Initialize mask 0 with inversion 0 and position -1.

Process each mask in order of increasing bit count.

For each mask, iterate through all words not in the mask.

For each word, find the next occurrence after the current position.

Compute the new inversion count and update the DP.

Once the full mask is processed, compute x and p.

Now, code.

Let's proceed to write the code.

First, read Lesha's words.

n = int(input())

lesha_words = input().split()

original_order = lesha_words.copy()

word_to_original = {word: idx for idx, word in enumerate(original_order)}

Then, read m archive problems.

m = int(input())

archive_problems = []

for i in range(m):

    parts = input().split()

    k = int(parts[0])

    s_words = parts[1:]

    archive_problems.append( (k, s_words) )

Then, for each archive problem, process:

max_p = -1

best_idx = -1

for problem_idx in range(m):

    k, s_words = archive_problems[problem_idx]

    # Check if all lesha_words are present in s_words.

    s_word_set = set(s_words)

    for word in lesha_words:

        if word not in s_word_set:

            break

    else:

        # All words are present.

        # Check if original order is a subsequence.

        ptr = 0

        for word in s_words:

            if ptr < n and word == original_order[ptr]:

                ptr +=1

                if ptr == n:

                    break

        if ptr == n:

            # Original order is a subsequence.

            x = 0

            p = (n*(n-1)//2) - x +1

            # Update if this p is higher than current max.

            if p > max_p or (p == max_p and problem_idx < best_idx):

                max_p = p

                best_idx = problem_idx

            continue

        else:

            # Proceed with DP.

            # Precompute word_to_indices.

            word_to_indices = defaultdict(list)

            for idx, word in enumerate(s_words):

                if word in word_to_original:

                    word_to_indices[word].append(idx)

            # Check if any lesha word has no indices (shouldn't happen).

            valid = True

            for word in lesha_words:

                if not word_to_indices[word]:

                    valid = False

                    break

            if not valid:

                continue

            # Precompute word_to_original indices.

            # Now, DP.

            dp = {}

            dp[0] = (0, -1)  # (inversion count, last_pos)

            # Process masks in order of increasing bit counts.

            for bit_count in range(n):

                # Collect masks with bit_count bits.

                current_masks = [mask for mask in dp if bin(mask).count('1') == bit_count]

                for mask in current_masks:

                    current_inversion, current_pos = dp[mask]

                    # Iterate through all possible words not in mask.

                    for word in lesha_words:

                        original_idx = word_to_original[word]

                        if (mask & (1 << original_idx)) != 0:

                            continue

                        # Get the list of indices for this word.

                        indices = word_to_indices[word]

                        # Find the next occurrence after current_pos.

                        idx_in_list = bisect.bisect_right(indices, current_pos)

                        if idx_in_list >= len(indices):

                            continue

                        new_pos = indices[idx_in_list]

                        # Compute the number of existing words in mask with higher original index.

                        count = 0

                        temp_mask = mask

                        while temp_mask:

                            lsb = temp_mask & -temp_mask

                            bit_pos = (lsb).bit_length() -1

                            if bit_pos > original_idx:

                                count +=1

                            temp_mask &= temp_mask -1

                        new_inversion = current_inversion + count

                        new_mask = mask | (1 << original_idx)

                        # Update DP.

                        if new_mask not in dp:

                            dp[new_mask] = (new_inversion, new_pos)

                        else:

                            existing_inversion, existing_pos = dp[new_mask]

                            if new_inversion < existing_inversion or (new_inversion == existing_inversion and new_pos < existing_pos):

                                dp[new_mask] = (new_inversion, new_pos)

            # Check if full_mask is in dp.

            full_mask = (1 << n) -1

            if full_mask in dp:

                x = dp[full_mask][0]

                p = (n*(n-1)//2) -x +1

                if p > max_p or (p == max_p and problem_idx < best_idx):

                    max_p = p

                    best_idx = problem_idx

            else:

                # This should not happen since all words are present.

                pass

    else:

        # Skip this problem.

        continue

# After processing all problems.

if best_idx == -1:

    print("Brand new problem!")

else:

    p = max_p

    print(best_idx +1)

    # Compute the number of |.

    # The output is [:: ... :], with p |'s.

    print("[:{}:]".format("|"*p))

But wait, in the code above, when checking if all lesha_words are present in the archive problem's S, we used s_word_set = set(s_words), which is O(k) time and O(k) space, but for k up to 5e5, this can be expensive in terms of memory. However, according to the problem constraints, the total length of words in all problem descriptions does not exceed 5e5+15. So this should be manageable.

But in Python, for large k, creating a set may take time. Alternative approach: check for each lesha_word in the s_words list by iterating through s_words and count occurrences.

But that would take O(k) time for each check. For n=15 and m=10, this is 15*10*5e5 = 7.5e7 operations. Which may be acceptable.

But for the current code, using a set is O(k) time and space, which is manageable.

Alternatively, for each lesha_word, check if it exists in s_words:

But in Python, 'in' on a list is O(k), but using a set is O(1) per check. So converting to a set is better.

Thus, the code is correct.

Now, let's test the code against the first sample input:

Sample Input 1:

4

find the next palindrome

1

10 find the previous palindrome or print better luck next time

Lesha's words are ["find", "the", "next", "palindrome"].

The archive problem's S is ["find", "the", "previous", "palindrome", "or", "print", "better", "luck", "next", "time"].

The original order is not a subsequence because "next" comes after "palindrome" in S.

The code proceeds to DP.

In the DP, the full mask is (1<<4)-1=15.

The minimal inversion count is 1.

Thus, p = (4*3/2) -1 +1 = 6.

The output is 1 and 6 |'s.

Thus, the code should output 1 and [:||||||:].

The code correctly handles this.

Another sample input is the second example, where none of the archive problems have all Lesha's words. Thus, output is "Brand new problem!".

Another sample input is the third example, where the archive problem's S contains all Lesha's words but the original order is not a subsequence. The code computes the minimal x and outputs the correct result.

Thus, the code should handle all cases correctly.

Now, handling the DP correctly, including the order of processing masks, is crucial.

The code uses a loop for each bit_count in range(n), and for each mask with bit_count bits, processes all transitions.

This ensures that masks are processed in order of increasing bit_count.

Thus, the code should be correct.

Edge Cases:

- n=1: The inversion count is 0. So p is 1-0+1=2.

- n=0: Not possible, since n >=1.

- Archive problem's S has exactly the same words as Lesha's, but in a different order.

Example:

n=3

Lesha's words: a b c.

Archive problem's S: [c, b, a].

Check if original order is a subsequence? No.

The minimal x is 3 (the permutation c b a has 3 inversions).

p = 3*2/2 -3 +1 = 3-3+1=1.

So the output would have p=1.

But wait, the minimal x is the inversion count of the permutation that is a subsequence.

In this case, the permutation can only be c b a. The inversion count is 3.

Thus, p= 3-3+1=1.

The output would be "[:|:]".

But the code should compute this correctly.

Another edge case: Lesha's words are present in S in an order that requires swapping two adjacent words.

For example, original order is a b. S has [b, a].

Then, the minimal x is 1. p is 1-1+1=1.

The code should compute this.

Thus, the code should handle these cases correctly.
</think>

```python
import bisect

n = int(input())
lesha_words = input().split()
original_order = lesha_words.copy()
word_to_original = {word: idx for idx, word in enumerate(original_order)}
m = int(input())
archive_problems = [input().split() for _ in range(m)]

max_p = -1
best_idx = -1

for problem_idx in range(m):
    parts = archive_problems[problem_idx]
    k = int(parts[0])
    s_words = parts[1:]
    s_word_set = set(s_words)
    # Check if all Lesha's words are present
    valid = True
    for word in lesha_words:
        if word not in s_word_set:
            valid = False
            break
    if not valid:
        continue
    # Check if original order is a subsequence
    ptr = 0
    for word in s_words:
        if ptr < n and word == original_order[ptr]:
            ptr += 1
            if ptr == n:
                break
    if ptr == n:
        p = (n * (n - 1) // 2) + 1
        if p > max_p or (p == max_p and problem_idx < best_idx):
            max_p = p
            best_idx = problem_idx
        continue
    # Proceed with DP
    word_to_indices = {}
    valid = True
    for word in lesha_words:
        indices = [i for i, w in enumerate(s_words) if w == word]
        if not indices:
            valid = False
            break
        word_to_indices[word] = indices
    if not valid:
        continue
    dp = {0: (0, -1)}
    for bit_count in range(n):
        current_masks = [mask for mask in dp if bin(mask).count('1') == bit_count]
        for mask in current_masks:
            current_inversion, current_pos = dp[mask]
            for word in lesha_words:
                original_idx = word_to_original[word]
                if (mask & (1 << original_idx)) != 0:
                    continue
                indices = word_to_indices[word]
                idx = bisect.bisect_right(indices, current_pos)
                if idx >= len(indices):
                    continue
                new_pos = indices[idx]
                count = 0
                temp_mask = mask
                while temp_mask:
                    lsb = temp_mask & -temp_mask
                    bit_pos = (lsb).bit_length() - 1
                    if bit_pos > original_idx:
                        count += 1
                    temp_mask &= temp_mask - 1
                new_inversion = current_inversion + count
                new_mask = mask | (1 << original_idx)
                if new_mask not in dp:
                    dp[new_mask] = (new_inversion, new_pos)
                else:
                    existing_inv, existing_pos = dp[new_mask]
                    if new_inversion < existing_inv or (new_inversion == existing_inv and new_pos < existing_pos):
                        dp[new_mask] = (new_inversion, new_pos)
    full_mask = (1 << n) - 1
    if full_mask in dp:
        x = dp[full_mask][0]
        p = (n * (n - 1) // 2) - x + 1
        if p > max_p or (p == max_p and problem_idx < best_idx):
            max_p = p
            best_idx = problem_idx

if best_idx == -1:
    print("Brand new problem!")
else:
    print(best_idx + 1)
    print(f"[:{'|' * max_p}:]")
```