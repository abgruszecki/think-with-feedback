<think>
Okay, let's try to solve this problem. The task is to find the minimum number of adjacent swaps needed to modify a string so that there are no occurrences of the substring "VK". The key is to do this with the least number of moves possible.

First, I need to understand the problem constraints. The maximum input length is 75, which isn't too big, but the solution needs to be efficient enough to handle all possible cases within the time limit. So, what's the approach here?

Hmm. The main idea is to avoid any "VK" in the final string. So, for every possible position in the string, after all swaps, there shouldn't be a 'V' immediately followed by a 'K'. But how do we model the swaps and calculate the minimal moves?

Swapping adjacent characters is equivalent to the number of inversions when the characters are being rearranged. So, for a given target arrangement of characters, the number of swaps needed is the number of inversions required to reach that arrangement from the original string.

But since the problem allows us to choose any arrangement that doesn't have "VK", the challenge is to find such an arrangement with the minimal inversion count compared to the original string.

So the problem reduces to generating all possible valid configurations (those without "VK") and finding the one with the minimal inversion count. But generating all possibilities isn't feasible for n=75. So we need a smarter approach.

Wait, but maybe the optimal solution is to find positions where we can break all possible "VK" pairs with minimal swaps. Let's think about possible strategies.

An alternative approach is to consider that after processing, the string can have some 'V's and 'K's, but no 'V' followed by 'K'. So perhaps, the optimal arrangement is to have all 'K's before 'V's, but that's not necessarily the case. For example, if there's a 'K' followed by a 'V' followed by other characters that aren't 'K' or 'V', maybe that's allowed.

Wait, no. Because "VK" is the only forbidden substring. So in the final string, all 'V's must not be immediately followed by 'K's. So the arrangement can have 'K's and 'V's as long as none of them form consecutive "VK" pairs.

Hmm. So how can we model this? Maybe dynamic programming. The state would need to track certain information about the current arrangement to ensure that adding the next character doesn't create a "VK" pair.

Alternatively, perhaps the minimal number of swaps is achieved by first handling the 'VK's that are present in the original string and then ensuring that the remaining characters are arranged such that no new 'VK's are formed. But this seems vague.

Wait, let's think of the problem as follows: the main forbidden occurrence is any "VK" in the final string. To avoid that, we need to split all such pairs. The key is that in the final arrangement, any 'V' must be followed by something that's not a 'K'. So for example, after a 'V', there can be another 'V' or any other character except 'K'.

So the problem is to arrange the characters such that in the final string, all 'V's are either followed by non-K characters or are at the end. And we need to find the arrangement with the minimal number of swaps (inversions) required.

But how do we model this? The challenge is that the swaps count depends on the order of the characters in the original string. Each swap between adjacent characters contributes 1 to the total count. The total swaps needed for a certain permutation is equal to the number of inversions required to reach that permutation from the original.

Wait, the number of swaps needed to transform the original string into a target permutation is equal to the number of inversions between the original and the target. So for each character in the target, we need to count how many positions it has moved from its original position, considering the order of other characters.

But calculating this inversion count efficiently is tricky. For example, if we have a target permutation, the minimal number of swaps can be calculated by the inversion count between the original and target permutation.

But how do we model all possible valid permutations and find the one with the minimal inversion count? The problem is that for n=75, the number of possible permutations is astronomical. So we need a dynamic programming approach that captures the necessary state information to track possible valid configurations and compute the minimal inversion count.

Let's think about dynamic programming. The state could represent the current position in the string, the last character placed (to check if placing a 'V' followed by a 'K' would create a forbidden substring), and the count of inversions so far. But with n=75 and possible characters (all uppercase letters), this might not be feasible.

Alternatively, perhaps we can group the characters into three categories: V, K, and others (let's call them X). Because the problem only forbids "VK", the interactions between V and K are the critical ones. The X characters can be placed anywhere without affecting the forbidden condition, except when between a V and a K.

Wait, but even if an X is between V and K, that's allowed. So the only forbidden pair is consecutive V followed by K.

So perhaps the optimal approach is to arrange the characters such that after all V's and K's are placed in a way that no V is immediately followed by K. The X's can be placed anywhere else.

But how do we model this? Let's consider that the key is the arrangement of the V's and K's, as the X's don't form any forbidden pairs. So, for the V's and K's, we need to arrange them such that there's no V followed by K. The X's can be placed anywhere else, and their arrangement doesn't affect the forbidden condition.

But the problem is that the X's are part of the inversion count. So their positions affect the total number of swaps. So perhaps the X's can be arranged optimally around the V and K's, but their placement isn't constrained except for the V-K pairs.

Hmm. So perhaps the key is to first arrange the V's and K's in a way that there are no VK pairs, and then arrange the X's in such a way that their contribution to the inversion count is minimized. But how do we model that?

Alternatively, the X's can be treated as elements that can be placed anywhere, but their order relative to each other and to the V's and K's can affect the inversion count. However, since their order among themselves doesn't affect the forbidden condition, perhaps their optimal arrangement is to preserve their original order as much as possible (since that minimizes the inversion count).

Wait, but inversion count between the original and the target permutation is minimized when the target permutation is as close as possible to the original. So for the X's, their order in the target permutation should be the same as in the original, to minimize the inversion count. The same applies to V's and K's, except that they have to avoid creating VK pairs.

So perhaps the problem can be broken down as follows: arrange all the V's and K's in a way that there are no VK pairs, and in doing so, the order of V's and K's (among themselves) is as close as possible to their original order. The X's are arranged in their original order, but placed around the V and K's in such a way that their inversion count is minimized.

Wait, but how do the X's interact with the V and K's? For example, if an X is between a V and a K, then it's allowed. So the X's can be placed anywhere, but their presence doesn't affect the forbidden condition between V and K.

So the main problem is to arrange the V's and K's such that in their sequence, there is no V followed by K. The X's can be placed anywhere, and their inversion count is calculated as per their relative order in the original and target.

But how do we model the inversion count for the entire string, considering the positions of V's, K's, and X's?

This seems complex. Let's think of the problem as a permutation of the original string's characters, where the permutation must not contain "VK" as a substring. The goal is to find the permutation with the minimal inversion count compared to the original.

But even for n=75, considering all possible permutations is impossible. So we need a dynamic programming approach that captures the necessary state to track the constraints.

Another idea: since the forbidden pair is "VK", perhaps the optimal arrangement is to have all K's before all V's. However, this might not be optimal. For example, in some cases, having some K's after V's (but not immediately after) might result in a lower inversion count. But this arrangement would require that between K and V there's at least one non-K character (like X or V). But perhaps in the optimal solution, the arrangement of K's and V's is such that all K's come before all V's. Because that way, there's no possibility of a V followed by a K.

But wait, that's not necessarily true. For example, if there are K's and V's but some X's in between, then a K can come after a V as long as they are not consecutive. But if all K's are placed before V's, then there's no V followed by K. So the arrangement where all K's are before V's is a valid arrangement. But perhaps there's a more optimal arrangement where some K's are after V's but separated by X's or other K's.

But considering that inversion count is about the swaps needed to arrange the characters, perhaps the minimal inversion count is achieved by placing the K's and V's in a way that all K's are before V's. But this isn't necessarily the case. For example, if the original string has a V followed by some K's and X's, it might be cheaper to move a K to the end of the V group rather than moving all K's before the V.

So the problem is to find a way to arrange K's and V's such that no two are in a VK pair, and the inversion count is minimized.

Let me think of the problem in terms of grouping the V's and K's. Suppose we split the V's and K's into two groups: those that are in positions where they don't form VK pairs.

Wait, perhaps the key is to model the arrangement of V's and K's as a sequence where each V is followed by a non-K. So the arrangement can be a mix of V's and K's, but every occurrence of a V must not be immediately followed by a K.

So, for example, a possible arrangement is VVVK... but that's invalid because the last V is followed by a K. But if there's an X between them, it's allowed.

Wait, no. The X is part of the string, so if the arrangement is VVXVK, then the VK here is allowed only if there's something between them. Wait, no. The forbidden substring is "VK" as consecutive characters. So in VXVK, the V and K are separated by X, so that's allowed. But in VVK, the second V is followed by K, which is forbidden.

So the main constraint is that after any V, the next character (if any) can't be K.

So, the problem reduces to arranging the V's and K's such that whenever a V is followed by a character, that character isn't K. The X's can be placed anywhere else, but their arrangement affects the inversion count.

But how do we model this efficiently?

Alternative approach: model the problem as a dynamic programming problem where the state tracks the last character placed (if it's a V or not) and the counts of remaining V's, K's, and X's.

Wait, but even that might be too slow. For example, if n is 75, and we have up to 75 characters, the state would need to track the number of V's, K's, X's left, and the last character. Let's see:

The state could be:

- pos: current position (implicitly tracked by the count of placed characters)
- last_char: whether the last placed character is V or not
- remaining_v: number of V's left
- remaining_k: number of K's left
- remaining_x: number of X's left

But the counts of V, K, X can be up to 75 each, leading to a state space of O(2 * 75 * 75 * 75) = 843,750 states. For each state, transitions would involve choosing the next character to place (V, K, X) if they are available, and ensuring that placing a K after a V is not allowed.

But how do we track the inversion count? Because each choice of placing a character affects the number of swaps needed, based on the original positions of the characters.

Ah, here's the crux: the inversion count is the sum, for each character, of the number of characters that were originally before it but are placed after it in the target permutation. So, for example, if in the original string, character A is at position i and in the target it's at position j < i, then all characters between j and i-1 in the original that are placed after A contribute to the inversion count.

But calculating this for a dynamic programming approach requires tracking not just which characters are left but also their original positions, which is impossible for large n.

Hmm. So this suggests that the dynamic programming approach must track not only the counts of each type but also some information about their original positions. But that's not feasible for n=75.

Alternative idea: the inversion count can be computed as the sum, for each character in the target permutation, the number of characters that were originally before it but are placed after it in the target. So for each character c in the original string, when we place it at position i in the target permutation, the number of original characters before c that are placed after i contributes to the inversion count.

But how can we model this without tracking each individual character's position? It's difficult.

Another approach: The minimal number of swaps required to arrange a set of characters into a particular order is equal to the number of inversions in the permutation from the original order to the target order. So, the problem reduces to finding the target permutation that satisfies the constraints (no "VK" substrings) and has the minimal possible number of inversions compared to the original.

But how do we find such a permutation?

Perhaps we can model this with dynamic programming, where the state represents the current sequence's last character (to prevent 'V' followed by 'K') and the positions of each character type that have been used so far.

But this seems too vague.

Alternative Idea:

The problem can be split into two parts:

1. Decide which V's and K's will form a "VK" pair in the original string. For each such pair, we need to break it by moving either the V or K, which will cost some swaps. However, since the final string must not have any "VK" pairs, even those that are not in the original but are introduced by moving characters.

Wait, but that's not correct. For example, moving a K from the end of the string to the front could create new "VK" pairs. So the problem is not just breaking existing pairs but also ensuring that no new pairs are formed.

Thus, the approach of only modifying existing "VK" pairs is insufficient.

Alternative Idea Inspired by Greedy Algorithms:

Perhaps the optimal arrangement is to have all K's come before all V's, except for those K's that are already after V's and can be moved without creating new VK pairs.

But I'm not sure. Let's consider the example in the first sample input:

Original string: VKVK → after moving, the optimal is KKVV. The cost is 3 swaps.

In this case, moving all K's before the V's.

Another sample input: BVVKV → after two moves, it becomes BVVVK. Wait, but that's not possible. The sample output is 2, and one possible arrangement is VVBKV. Wait, the sample output says two moves leading to "VVBKV" or "BVKVV" → which don't have VK pairs.

Hmm. So in this case, the K is moved to after some V's, but there's an X (the B) in between.

So, the optimal arrangement is not necessarily all K's before all V's. Therefore, the arrangement must allow V's and K's to be in any order, as long as no V is immediately followed by K.

Thus, the key is to arrange the V's and K's such that between any V and K (in that order) there's at least one non-K character.

But how to model this?

An alternative approach is to model the problem by considering that in the final string, after each V, the next character can't be K. So, the arrangement of V's and K's must be such that all K's are placed either before any V's or after a non-K character following a V.

This seems complicated. So perhaps a dynamic programming approach where the state tracks the last character placed (whether it's a V or not) and the counts of remaining V's, K's, and X's. For each step, we can choose the next character to place (V, K, X) and track the cost (inversion count) accordingly.

But the problem is calculating the inversion count for each possible choice of next character. For example, if we choose to place a V next, we need to compute how many characters that were originally after this V in the original string are now placed before it, contributing to the inversion count.

Wait, but this requires knowing the order in which the characters are placed. For instance, the inversion count is the sum of the number of original characters that appear before this character in the original string but are placed after it in the target, and those that appear after in the original but are placed before.

So, when placing a character from the original string, the inversion count for this character is the number of characters already placed that were originally after this character. Because when you place a character in the target string, all characters that were originally after it but have already been placed contribute +1 to the inversion count.

So the inversion count can be computed incrementally. For example, if we have a list of characters in the original order, and as we build the target string, each time we select a character from the remaining ones, the inversion count increases by the number of characters already placed that were originally before this character. Wait, no. Let me think again.

Suppose the original order is [c0, c1, c2, ..., cn-1]. We are building the target string by choosing characters in some order. Each time we choose a character c from the original list (not yet chosen), the inversion count for this step is the number of characters already chosen that were originally after c. Because those characters were moved before c, contributing to the inversion count.

Wait, yes. For example, if in the original, the order is A, B, C. If we choose to arrange them as B, C, A. Then the inversion count is for B (0), C (0, since B was before in original), and A (2, since B and C were after in original but placed before). Total inversion count is 2.

So each time we select a character from the remaining ones, the number of characters already placed that were originally after it in the original string adds to the inversion count.

This suggests that we can model the inversion count incrementally. So, for dynamic programming, the state needs to track:

- The set of characters that have been placed so far. But with n=75, this is impossible.

Alternative Idea: Precompute the inversion cost for placing each character in a certain order. For example, if we have a certain order of V's, K's, and X's, the inversion count is the sum of the inversion counts for each individual character.

But how?

Another Idea: Since the inversion count is based on the order in which characters are selected from the original string, perhaps we can model the problem using a dynamic programming state that tracks:

- The last character placed (to avoid "VK" pairs)
- The indices of the characters that have been selected so far (but for n=75, this is impossible as the state would be 2^75, which is way too big)

Alternatively, model the problem by tracking the positions of the characters in the original string that have been used. For example, when building the target string, each character is chosen from the remaining original positions, and the inversion count is updated based on the number of already chosen characters that are in positions after the current character's original position.

But for n=75, even this approach is impossible as the state space is too large.

Alternative Approach Inspired by Permutation Inversion Count:

The inversion count for a permutation is equal to the number of pairs (i, j) where i < j in the original and the target permutation places j before i.

So, the problem is to find a permutation of the original string that has no "VK" substrings and has the minimal number of such inversion pairs.

But how do we model this?

Let's consider that the X's can be placed anywhere, but their order among themselves doesn't affect the forbidden pairs. So the optimal way to arrange the X's is to keep their original relative order, as that minimizes the inversion count. Similarly for the V's and K's among themselves, but with the constraint that no V is followed by a K.

So, the problem reduces to permuting the V's and K's such that there are no consecutive V followed by K, and the X's are arranged in their original order. The minimal inversion count is achieved by permuting the V's and K's in such a way that their relative order is as close as possible to the original, while avoiding V followed by K.

So the key is to arrange the V's and K's into a sequence where no V is immediately followed by a K, and the relative order of V's and K's is as close as possible to the original.

But how to model this?

Another Idea: Let's separate the V's and K's into a subsequence. For this subsequence, we need to arrange them such that there's no V followed by K. The X's are placed in the remaining positions, maintaining their original order.

The inversion count would then be the sum of the inversion count of the V/K subsequence plus the inversion count caused by the X's.

But the X's inversion count can be calculated based on their placement relative to the V's and K's. However, since the X's are placed in their original order, their inversion count is determined by how many V's and K's are placed before or after them compared to their original positions.

This seems complicated. Perhaps we can model the problem by first processing the V's and K's, and then the X's.

But how?

Alternative Idea inspired by Merging:

The minimal inversion count for the X's is achieved by keeping them in their original order. So, for any X that comes before a V or K in the original, if it's placed after that V or K in the target permutation, it contributes to the inversion count. But since the X's can be placed anywhere, perhaps the optimal is to interleave them with the V's and K's in such a way that their relative order is preserved. But this doesn't directly help in the inversion count calculation.

Another Idea: The problem can be viewed as a modified version of the standard problem of arranging characters with certain constraints. The standard approach for such problems is to model it with dynamic programming, tracking the necessary state to ensure the constraints are met.

In our case, the state needs to track the last character placed (to prevent a 'V' followed by 'K'). Additionally, for each possible state, we track the minimal inversion count required to reach that state.

So, the DP state can be:

dp[i][j][k][last_char] = minimal inversion count to place i V's, j K's, and k X's, with the last character being 'V' or 'K' or 'X' (or None for the first character).

But even this is manageable if we can compute the transitions.

Wait, but the problem is that the inversion count depends on the order in which the characters are placed. For example, placing a V from the original's position 5 after placing a K from position 3 would contribute 1 inversion (since 3 <5 but K is placed first). So, the inversion count depends on the order in which the original characters are selected.

But how to model this in the DP state?

This seems impossible because the inversion count is dependent on the specific order of selection of the original characters. For example, choosing a V that is early in the original and then a K that is later would contribute less inversion count than if their order is reversed.

So, perhaps the problem requires tracking not only the counts of V, K, and X placed but also their original positions. But with n=75, this is not feasible.

Alternative Idea inspired by Greedy and Mathematical Models:

Let's think about the minimal number of swaps needed to prevent any "VK" pairs. The minimal swaps would be to break all existing "VK" pairs in the original string. But this is not sufficient, as moving characters might introduce new pairs.

For example, if the original string is "VKVK", breaking the two "VK" pairs might require moving characters, but moving them could create new pairs.

But in the first sample input, the optimal solution is to swap the last two characters (VK → KV) and other swaps to get KKVV. This breaks all possible "VK" pairs.

So the approach of breaking existing "VK" pairs may not be sufficient, as new pairs can be formed during the swaps. Therefore, the solution must consider all possible ways to avoid any "VK" pairs in the final arrangement.

But how?

Alternative Idea inspired by the optimal arrangement of V's and K's:

The optimal arrangement of V's and K's is such that between any V and K in the final arrangement, there is at least one non-K character (like X or V). But since X's can be placed anywhere, perhaps the best way to avoid any VK pairs is to arrange all V's first, then K's, or arrange K's first then V's, or have V's and K's interspersed with X's.

But the presence of X's complicates things. For example, if there are no X's, then the only way to avoid VK pairs is to have all K's before V's. But if X's are present, we can place them between V and K.

But even with X's, if a V is followed by a K in the final arrangement, but they are separated by X's, then that's allowed. Only consecutive V followed by K is forbidden.

So, the problem is to arrange the V's and K's such that no two consecutive characters are V followed by K. The X's can be placed anywhere else, but their placement affects the inversion count.

This seems challenging. Let's think about the problem in terms of possible sequences of V's and K's.

The valid sequences of V's and K's are those where after a V, there cannot be a K. So, the possible sequences are:

- All K's come before all V's.

- K's and V's are arranged in such a way that any V is followed by a K only if there is at least one other character (like an X) in between.

But since the X's can be placed anywhere, perhaps the minimal inversion count is achieved when the sequence of V's and K's is such that no V is immediately followed by K. The X's are placed in their original order wherever possible.

But how to model this.

Alternative Idea inspired by the minimal number of swaps:

The minimal inversion count is achieved when the order of the characters is as close as possible to the original. So, the solution is to find the closest possible arrangement (to the original) that has no VK pairs.

Thus, the optimal solution is to break all VK pairs in the original string in the most efficient way possible. For example, for each VK pair in the original, we can decide to swap either the V or the K to break the pair. But this may introduce new pairs elsewhere.

But since the problem requires that there are no VK pairs in the final string, not just the original ones, this approach is not sufficient.

Alternative Idea inspired by the Optimal Subsequence:

Suppose we can split the original string into two subsequences: one that includes all characters except the K's that are immediately preceded by a V, and another that includes those K's. Then, arrange those subsequences in such a way that the forbidden pairs are avoided.

But I'm not sure.

Another Idea: Since the problem is to avoid any occurrence of VK in the final string, perhaps the optimal solution is to ensure that in the final string, after any V, there is a non-K character. To do this, for each V in the string, we can check if the next character is K. If it is, then we need to move either the V or the K to another position.

But moving these characters would involve a cost in swaps. How do we choose which characters to move and in what order to minimize the total swaps?

This seems like a problem that can be modeled with dynamic programming, where the state captures whether the previous character was a V. This way, when placing a new character, we can ensure that if the previous was a V, the current character is not a K.

So, the dynamic programming state can be:

dp[i][j][k][last_is_v] = minimal swaps required to arrange the first (i + j + k) characters, where i is the number of V's used, j the number of K's used, k the number of X's used, and last_is_v is a boolean indicating if the last character placed was a V.

The transitions would be:

- For each possible next character (V, K, X) that hasn't been used yet.

- If the last character was a V, then the next character cannot be a K.

- For each possible choice of next character, the cost is the number of remaining characters (V, K, X) that were originally before this next character and have not yet been placed. This represents the inversion count added by placing this character now.

For example, if the next character is a V, then the cost is the number of characters (V, K, X) that are left (i.e., not yet used) and were originally before this V.

Wait, but how do we track which V, K, or X has been used?

This approach assumes that we're choosing a type of character (V, K, or X) to place next, but not the specific instance. However, the inversion count depends on the original positions of the specific characters. So this approach may not work because it doesn't track which specific characters are used.

Thus, the problem is that the inversion count depends on the order in which the original characters are selected, not just their types.

So, this suggests that a dynamic programming approach that only tracks the counts of each type of character and the last character placed is insufficient. We need to track the specific positions of the characters that have been used, but this is impossible for n=75.

Alternative Idea inspired by Permutation Inversion Count for Grouped Elements:

Suppose we can group the characters into V's, K's, and X's. For each group, we can calculate the inversion count based on their original positions. For example, if all V's are moved to come before all K's, then the inversion count is the number of pairs where a K was originally before a V.

But this is the same as the inversion count between the V's and K's in the original string. So, if we arrange all K's before all V's, the inversion count between V's and K's is the number of K's that come after a V in the original string.

But what about the X's? The X's can be interleaved between the K's and V's, which may reduce the inversion count. But how?

Alternatively, the minimal inversion count is achieved when all K's are placed before all V's, and the X's are arranged in their original order.

But this may not be the case. For example, if moving some K's after V's (separated by X's) reduces the total inversion count.

But how can we know?

Another Idea: The optimal arrangement for V's and K's is such that no V is immediately followed by a K. This can be achieved in several ways:

1. All K's are placed before all V's. This ensures no V is followed by a K.

2. Some K's are placed after V's, but each such K is separated by at least one non-K character (X or V).

But how to compare the inversion counts of these possibilities.

But given the complexity of the problem, perhaps the optimal approach is to model this as a dynamic programming problem where we track the last character placed and the counts of V, K, X used, and for each state, track the minimal inversion count. But how to compute the inversion count contribution for each choice of next character.

But this requires knowing the original positions of the characters, which is not tracked in the state. Thus, this approach may not be feasible.

Alternative Idea inspired by the Inversion Count Calculation for Groups:

Assuming that we can arrange the V's and K's such that no V is followed by K, and the X's are arranged in their original order. Then, the inversion count can be computed as follows:

For V's and K's:

The inversion count is the number of pairs (a, b) where a is a V or K, b is a V or K, a comes after b in the original string, and a is placed before b in the target.

For X's:

The inversion count is the number of pairs (x, y) where x and y are X's, x comes after y in the original string, and x is placed before y in the target. To minimize this, the X's should be placed in their original order.

So, for the X's, their contribution to the inversion count is minimized by maintaining their original order.

Thus, the optimal arrangement for X's is to place them in their original order, but interspersed between V's and K's as needed to avoid VK pairs.

This suggests that the problem can be split into two parts:

1. Arrange the V's and K's in a way that no V is followed by K, and compute the inversion count between V's and K's.

2. Arrange the X's in their original order, interspersed between the V's and K's, and compute their inversion count contribution based on their placement.

But how to model this?

Perhaps we can model the problem as follows:

- Generate all possible valid sequences of V's and K's (no VK pairs), and for each such sequence, compute the inversion count between the sequence and the original V/K positions. Additionally, compute the inversion count caused by inserting the X's into the sequence while maintaining their original order.

The minimal total inversion count across all such valid sequences is the answer.

But with n=75, this approach is not feasible, as the number of valid sequences could be very large.

Alternative Idea inspired by the fact that X's can be placed anywhere except between V and K in the wrong order:

Wait, no. X's can be placed anywhere, including between V and K. For example, VXK is allowed, since the V and K are not consecutive.

Thus, the X's can be used to separate V's and K's. So the problem of arranging the V's and K's can be approached by first placing the X's in their original order, then inserting the V's and K's into the remaining positions, ensuring that no V is immediately followed by a K.

But how to model the inversion count for this arrangement.

Another Idea: The minimal inversion count is achieved by keeping the original order of characters as much as possible, but avoiding any VK pairs. So, the optimal solution is to find the earliest possible VK pair and break it by swapping either V or K with adjacent characters until the pair is separated.

But this greedy approach may not work because breaking one pair could create others.

But given the time constraints, perhaps the best approach is to model the problem with dynamic programming, where the state tracks the last character placed (V or not), and the positions of the V's, K's, and X's that have been used so far. But again, the problem is tracking this information for n=75.

Alternative Idea inspired by the Observation That X's Can Be Treated Separately:

Since the X's can be placed anywhere and their inversion count is minimized by keeping their original order, we can first process the V's and K's and then insert the X's into the remaining positions in their original order.

So, the problem reduces to arranging the V's and K's in a valid sequence (no consecutive VK) and computing the inversion count between the V's and K's, plus the inversion count caused by inserting X's into the arrangement.

But inserting the X's in their original order may not contribute to the inversion count if their relative order is preserved. However, the positions where they are inserted can affect the inversion count between X's and V's/K's.

So, the inversion count would be:

- The inversion count between V's and K's in their arrangement.

- The inversion count between X's and V's/K's.

- The inversion count between X's themselves (which is zero if they are kept in order).

But how to compute this.

This approach may be manageable.

Let's denote the positions of V's and K's in the original string as P_vk. The positions of X's are Q_x.

For example, suppose we have a valid arrangement of V's and K's. The positions of these V's and K's in the final string are the positions that are not occupied by X's. The X's are placed in their original order into the remaining positions.

The inversion count between the V's and K's is the number of pairs (i, j) in the original P_vk where i < j but in the target arrangement, the character at j is placed before i.

The inversion count between X's and V's/K's is the number of X's that are originally before a V/K but are placed after it in the target, plus the number of X's that are originally after a V/K but are placed before it in the target.

But how to compute this.

This seems very complex. Perhaps we can model this with dynamic programming for the V's and K's, and compute the inversion count for the X's based on their positions.

But even that may not be tractable.

Alternative Idea inspired by the fact that the X's contribute a fixed number of inversions based on their placement relative to the V's and K's:

The X's are placed in their original order. For each X in the original order, when it is placed in the target permutation, its position is determined by the number of V's and K's placed before and after it. The number of inversions contributed by this X is the number of V's and K's that were originally after it but are placed before it (which contributes to the inversion count) plus the number of V's and K's that were originally before it but are placed after it (which also contributes to the inversion count). However, this depends on the arrangement of V's and K's.

But calculating this for all X's is difficult unless we have the exact order of V's and K's.

This suggests that the problem is very complex and requires a different approach.

Final Idea:

Given the problem's constraints (n=75), perhaps a dynamic programming approach is possible with the following state:

- The number of V's used so far (v)

- The number of K's used so far (k)

- The number of X's used so far (x)

- Whether the last character was a V (last_v)

The DP state is dp[v][k][x][last_v], which represents the minimal inversion count to have used v V's, k K's, x X's, with last_v indicating whether the last character was a V.

At each step, the next character can be a V, K, or X, provided that if the last character was a V, the next character is not a K.

The inversion count for each step depends on the number of characters remaining in the original string that were originally before the selected character.

But how to compute this inversion count contribution without knowing the specific characters selected.

Wait, the key is that the inversion count is determined by the order in which the characters are selected. For example, when we select a character from the original string, all characters that were originally before it and are not yet selected contribute to the inversion count. Because those characters will be placed after this character in the target permutation, which creates an inversion.

But this seems impossible to model without tracking the original positions of each character.

Alternative Idea inspired by Preprocessing:

Precompute for each character (V, K, X) their positions in the original string. Then, during the DP transitions, when we choose to place a character of type t (V, K, X), we can track which specific character of that type we are placing (based on their original order), and compute the inversion count contribution as the number of characters that were originally before this character and have not been placed yet.

But this requires tracking not just the counts of each type but also the specific indices of the characters that have been placed. For example, for V's, we need to track which V's have been used (e.g., the first V, second V, etc.), and similarly for K's and X's. This would allow us to know the original position of the next character of type t.

This approach could be feasible.

Here's how it could work:

For each type (V, K, X), precompute a list of their original positions in the string. For example:

- vs = [i for i, c in enumerate(s) if c == 'V']

- ks = [i for i, c in enumerate(s) if c == 'K']

- xs = [i for i, c in enumerate(s) if c not in 'VK']

Then, the dynamic programming state can be:

dp[a][b][c][last_v], where:

- a is the number of V's used (so the next V to use is vs[a])

- b is the number of K's used (next K is ks[b])

- c is the number of X's used (next X is xs[c])

- last_v is a boolean indicating if the last character was a V.

The value of dp[a][b][c][last_v] is the minimal inversion count to reach this state.

The transitions are:

1. If we can add a V next (i.e., a < len(vs)), and either last_v is False or the previous character was not a V (no, the last_v indicates whether the previous character was a V. So if we add a V next, the next state's last_v will be True, but the current state's last_v doesn't affect whether we can add a V (since a V can follow any character except a V followed by a K).

Wait, no. Adding a V is allowed regardless of the previous character, except if the previous character was a V followed by a K. But the DP state only tracks whether the previous character was a V. So, if the previous character was a V, adding a K is not allowed. But adding a V is allowed.

So, when the previous character is a V (last_v is True), the next character can be V or X. When the previous character is not a V (last_v is False), the next can be V, K, or X.

So, the transitions are:

For each state (a, b, c, last_v):

- If adding a V is possible (a < len(vs)), then:

   new_last_v = True

   The cost is the number of characters not yet used that were originally before the current V's position (vs[a]) and are not yet used.

   The number of such characters is:

   (number of V's not used yet: len(vs) - a - 1) → since a is the current count used.

   Wait, no. The current V to add is vs[a], and the characters that are already used are a V's, b K's, c X's. The remaining characters are:

   For V's: vs[a+1 ... len(vs)-1]

   For K's: ks[b ... len(ks)-1]

   For X's: xs[c ... len(xs)-1]

   So, when adding vs[a], the cost contributed is the number of characters in these remaining lists that have an original position less than vs[a]. Because those characters are placed after the current V in the target permutation but were originally before it. So this contributes to the inversion count.

   Wait, no. The inversion count for the current V is the number of characters that were placed before it in the target permutation but were originally after it. So when adding vs[a], the characters that have been placed before it in the target and were originally after vs[a] are counted. But how?

   The inversion count for this step is the number of characters that were in the original string before vs[a] (i.e., their index is less than vs[a]) but are not yet placed (and thus will be placed after this V, contributing to the inversion count). Because those characters are placed after this V in the target permutation, but were originally before it. So for each such character, it will contribute 1 to the inversion count.

   So, when placing vs[a], the number of characters remaining that were originally before it is:

   (number of V's remaining after this one: len(vs) - a - 1) → because the V's after this in vs are in positions higher than vs[a].

   Wait, no. The V's after vs[a] are in the original string positions after vs[a]. So if we are placing vs[a], the remaining V's (vs[a+1] ...) are after vs[a] in the original. So their positions are larger than vs[a]. So they are not counted.

   Similarly, the K's and X's remaining are those in the original string at positions larger than vs[a] if they are in the remaining lists.

   So, the inversion count contributed by placing vs[a] is the number of characters (V, K, X) that are not yet placed and are originally before vs[a].

   But how do we calculate this?

   The characters not yet placed are:

   V's: vs[a+1 ... len(vs)-1] (original positions)

   K's: ks[b ... len(ks)-1]

   X's: xs[c ... len(xs)-1]

   For each of these, count how many have original positions < vs[a].

   So for each possible transition, the cost is:

   cost = sum(1 for v in vs[a+1:] if v < vs[a]) 

   + sum(1 for k in ks[b:] if k < vs[a])

   + sum(1 for x in xs[c:] if x < vs[a])

   This gives the number of characters that are after vs[a] in the target permutation (since they are yet to be placed) but were originally before it. Each such character contributes 1 to the inversion count.

So, for each possible transition (adding a V, K, or X), we can precompute the cost for each possible a, b, c.

This is feasible if we precompute for each possible a, b, c and for each type (V, K, X) the number of remaining characters (of each type) that are originally before the current character.

For example, when considering adding a V (a-th V), the cost is the number of remaining V's (after a) that are before a-th V's position, plus the number of K's (from b onward) that are before a-th V's position, plus the number of X's (from c onward) that are before a-th V's position.

To compute this efficiently, we can precompute for each V, K, X, and for each a, b, c, the cost.

But precomputing this for all possible a, b, c might be feasible given the constraints (n=75).

For example, for the V's:

For each a (0 to len(vs)-1), and for each possible current a (which is the index into vs), the remaining V's are vs[a+1:], and we need to count how many of them are before vs[a].

Similarly for K's and X's.

But how to compute this quickly?

We can precompute for each position in vs, the count of V's that are after it (in the vs list) and have a position in the original string less than vs[a].

This can be done using prefix sums.

For example, for the V's:

We can create a list of vs sorted by their original positions. For each a, the number of V's after a (in the vs list) that are before vs[a] in the original can be computed by binary search.

But wait, vs is already in the order of their original positions. Because vs is the list of indices of 'V's in the original string. So for example, if the original string is "VKVK", then vs = [0, 2]. The a-th V is vs[a], which has an original position of 0 when a=0, and 2 when a=1.

So, for a given a, the remaining V's are vs[a+1: ...], and their positions are all >= vs[a], since the original string's V's are ordered. Because the V's are collected in the order of their occurrence, which is their original positions. So vs is a list in increasing order.

Thus, for the V's, any V after a-th V in the vs list has a higher original position. So, for a-th V, there are zero V's in the remaining (vs[a+1:]) that have original position < vs[a]. So the contribution from V's is zero.

Similarly, for K's:

The K's in the original string are in ks list, which is in increasing order of their positions. So when we are considering placing a K, the remaining K's are after it, and have higher positions.

So for a given a-th V, the K's that are in the ks[b:] list are those with positions >= ks[b], since the K's are ordered.

But the current a-th V's original position is vs[a]. So to find how many K's in ks[b:] are before vs[a], we can perform a binary search in the ks list for the largest index where the K's position is less than vs[a]. For example, if ks is [1,3,5], and vs[a] = 4, then K's at positions 1 and 3 are before 4. So the number of K's in ks[b:] (say, if b is 0) that are before vs[a] is 2.

This can be computed using binary search.

Similarly for X's.

So the steps are:

1. Precompute the vs, ks, xs lists.

2. For each possible a, compute the number of K's in ks[b:] that are < vs[a], given b. For example, when adding a V at a-th position, b is the current count of K's used. The remaining K's are ks[b:].

3. Similarly, for X's in xs[c:], compute how many are < vs[a].

Thus, for each transition when adding a V, K, or X, we can compute the cost as the sum of:

- V's remaining: 0 (since vs is in order)

- K's in ks[b:] that are < current character's position.

- X's in xs[c:] that are < current character's position.

This is manageable.

Thus, the DP approach can proceed as follows:

- Precompute the vs, ks, xs lists.

- Precompute for each possible a, b, c, the cost of adding a V, K, or X.

But how?

For example, when adding a V at position a (a-th V), the current state is (a, b, c, last_v). The cost is the number of K's in ks[b:] with position < vs[a] plus the number of X's in xs[c:] with position < vs[a].

Similarly for adding a K (if allowed) or X.

So, the dynamic programming approach can be implemented with states (a, b, c, last_v), and transitions that add each possible next character (V, K, X) if allowed (e.g., after a V, K can't be added).

The initial state is (0, 0, 0, False), with cost 0.

The final answer is the minimal cost among all states where all characters are used (a == len(vs), b == len(ks), c == len(xs)).

But with n=75, and the lengths of vs, ks, xs up to 75 each, the state space is 75*75*75*2 = 843,750 states. For each state, there are up to 3 possible transitions (V, K, X), but some are invalid (like K after V). So the total number of transitions is manageable.

Thus, this approach is feasible.

Now, how to implement this.

Steps to Implement:

1. Read the input string and split into vs, ks, xs lists of their positions.

2. Sort these lists (they are already in order of their occurrence in the original string, which is their positions in increasing order).

3. For each possible transition in the DP:

   For a state (a, b, c, last_v), compute the cost of adding a V, K, or X (if allowed).

   For example:

   - If adding V (a < len(vs)):

      The new state is (a+1, b, c, True).

      The cost is the number of K's in ks[b:] with pos < vs[a] + number of X's in xs[c:] with pos < vs[a].

   - If adding K (b < len(ks) and last_v is False):

      new state is (a, b+1, c, False).

      cost is number of V's in vs[a:] with pos < ks[b] + number of X's in xs[c:] with pos < ks[b].

   - If adding X (c < len(xs)):

      new state is (a, b, c+1, False).

      cost is number of V's in vs[a:] with pos < xs[c] + number of K's in ks[b:] with pos < xs[c].

4. Use a memoization table (DP table) to track the minimal cost for each state.

5. The answer is the minimal cost among all states where all characters are used.

Edge Cases:

- All characters are X: the answer is 0.

- Original string has no VK pairs: the answer is 0.

- Original string has VK pairs that need to be broken.

So, the code will need to handle these cases.

Now, let's code this.

First, precompute vs, ks, xs:

s = input().strip()

vs = [i for i, c in enumerate(s) if c == 'V']
ks = [i for i, c in enumerate(s) if c == 'K']
xs = [i for i, c in enumerate(s) if c not in 'VK']

Then, the DP state is a, b, c, last_v.

The cost for adding a V is:

k_count = bisect.bisect_left(ks, vs[a], lo=b) - b

x_count = bisect.bisect_left(xs, vs[a], lo=c) - c

total_cost = k_count + x_count

Similarly for K and X.

But how to compute the number of K's in ks[b:] that are less than vs[a].

Using binary search, the number of K's in ks starting from index b that are less than vs[a] is equal to the number of elements in ks[b:] that are < vs[a]. Since ks is sorted, we can use bisect_left to find the first index in ks where the element is >= vs[a]. The number of elements before that index (starting from b) is the count.

For example, in ks, the elements are sorted. So for vs[a], we can do:

pos = bisect.bisect_left(ks, vs[a], lo=b)

count = pos - b

Similarly for xs.

So, in Python, we can use the bisect module for this.

Now, the code:

Implementing the DP using a 4-dimensional array or a memoization dictionary.

But for efficiency, use a memoization dictionary with tuples (a, b, c, last_v) as keys, and values being the minimal cost.

But given the state space size (up to 75*75*75*2 = 843,750), a memoization dictionary might be manageable.

Alternatively, use a 4-dimensional array for DP.

But in Python, a 4-dimensional list may be more efficient.

Initialize the DP with infinity, then set dp[0][0][0][False] = 0.

For each state, iterate through all possible transitions.

Thus, the code will look something like this:

import bisect

n = int(input())
s = input().strip()

vs = [i for i, c in enumerate(s) if c == 'V']
ks = [i for i, c in enumerate(s) if c == 'K']
xs = [i for i, c in enumerate(s) if c not in 'VK']

len_v = len(vs)
len_k = len(ks)
len_x = len(xs)

INF = float('inf')

# DP table: a, b, c, last_v (0/1)
dp = [[[[INF] * 2 for _ in range(len_x + 1)] for __ in range(len_k + 1)] for ___ in range(len_v + 1)]

dp[0][0][0][0] = 0  # last_v is False

for a in range(len_v + 1):
    for b in range(len_k + 1):
        for c in range(len_x + 1):
            for last_v in 0, 1:
                current_cost = dp[a][b][c][last_v]
                if current_cost == INF:
                    continue

                # Try adding a V
                if a < len_v:
                    pos_v = vs[a]
                    # K's in ks[b:] < pos_v
                    k_count = bisect.bisect_left(ks, pos_v, lo=b) - b
                    # X's in xs[c:] < pos_v
                    x_count = bisect.bisect_left(xs, pos_v, lo=c) - c
                    cost = k_count + x_count
                    new_a = a + 1
                    new_last_v = 1
                    new_cost = current_cost + cost
                    if new_cost < dp[new_a][b][c][new_last_v]:
                        dp[new_a][b][c][new_last_v] = new_cost

                # Try adding a K
                if b < len_k and not last_v:
                    pos_k = ks[b]
                    # V's in vs[a:] < pos_k
                    v_count = bisect.bisect_left(vs, pos_k, lo=a) - a
                    # X's in xs[c:] < pos_k
                    x_count = bisect.bisect_left(xs, pos_k, lo=c) - c
                    cost = v_count + x_count
                    new_b = b + 1
                    new_last_v = 0
                    new_cost = current_cost + cost
                    if new_cost < dp[a][new_b][c][new_last_v]:
                        dp[a][new_b][c][new_last_v] = new_cost

                # Try adding an X
                if c < len_x:
                    pos_x = xs[c]
                    # V's in vs[a:] < pos_x
                    v_count = bisect.bisect_left(vs, pos_x, lo=a) - a
                    # K's in ks[b:] < pos_x
                    k_count = bisect.bisect_left(ks, pos_x, lo=b) - b
                    cost = v_count + k_count
                    new_c = c + 1
                    new_last_v = 0
                    new_cost = current_cost + cost
                    if new_cost < dp[a][b][new_c][new_last_v]:
                        dp[a][b][new_c][new_last_v] = new_cost

# The answer is the minimal cost when all characters are used, in any last_v state.
min_total = min(dp[len_v][len_k][len_x][0], dp[len_v][len_k][len_x][1])
print(min_total)

Let's test this code against the sample inputs.

Sample Input 1:

4
VKVK

vs = [0, 2]
ks = [1, 3]
xs = []

The code should compute the minimal inversion count.

For example, the optimal solution is to arrange the V's and K's in the order K, K, V, V. Which requires 3 swaps.

The code's DP should compute this.

But how?

Let's see: the final state is a=2, b=2, c=0. The code checks the minimum of dp[2][2][0][0] and dp[2][2][0][1].

The code should correctly compute the inversion count for this arrangement.

Another sample:

Sample 2:

5
BVVKV

The vs are at positions 1, 2, 4. The ks are at position 3. The xs are positions 0 (B) and 4 is the K? Wait, no, the input is BVVKV.

Indices are 0: B, 1: V, 2: V, 3: K, 4: V.

So vs = [1, 2,4], ks = [3], xs = [0].

The code should compute the minimal inversion count of 2.

The code's transitions would compute the cost for placing each character, considering the order.

Thus, the code should handle these cases.

The code seems correct, and the approach is to model the DP state with a, b, c, last_v, and compute the cost based on the original positions of the characters. This approach should handle all possible cases and find the minimal inversion count.
</think>

To solve this problem, we need to minimize the number of adjacent swaps required to transform a given string such that it does not contain the substring "VK". The approach involves dynamic programming (DP) to efficiently compute the minimal number of swaps by considering the positions of 'V', 'K', and other characters (denoted as 'X') in the original string.

### Approach
1. **Problem Analysis**: The goal is to avoid any occurrence of the substring "VK" while minimizing the number of adjacent swaps. This can be achieved by rearranging the characters such that no 'V' is immediately followed by a 'K'.

2. **Dynamic Programming State**: We use a 4-dimensional DP array where `dp[a][b][c][last_v]` represents the minimal number of swaps required to place `a` 'V's, `b` 'K's, and `c` 'X's, with `last_v` indicating if the last character placed was 'V'.

3. **Transitions**: For each state, we consider adding the next character (either 'V', 'K', or 'X') and compute the associated cost (number of swaps) based on their original positions. The cost is determined by the number of characters that were originally before the current character but are placed after it in the target permutation.

4. **Binary Search**: To efficiently compute the cost, we use binary search to count how many remaining characters of other types are positioned before the current character in the original string.

### Solution Code
```python
import bisect

n = int(input())
s = input().strip()

vs = [i for i, c in enumerate(s) if c == 'V']
ks = [i for i, c in enumerate(s) if c == 'K']
xs = [i for i, c in enumerate(s) if c not in 'VK']

len_v = len(vs)
len_k = len(ks)
len_x = len(xs)

INF = float('inf')

# Initialize DP table
dp = [[[[INF] * 2 for _ in range(len_x + 1)] for __ in range(len_k + 1)] for ___ in range(len_v + 1)]
dp[0][0][0][0] = 0  # last_v is False (0)

for a in range(len_v + 1):
    for b in range(len_k + 1):
        for c in range(len_x + 1):
            for last_v in [0, 1]:
                current_cost = dp[a][b][c][last_v]
                if current_cost == INF:
                    continue

                # Add a V if possible
                if a < len_v:
                    pos_v = vs[a]
                    # Count K's in ks[b:] with pos < pos_v
                    k_count = bisect.bisect_left(ks, pos_v, b) - b
                    # Count X's in xs[c:] with pos < pos_v
                    x_count = bisect.bisect_left(xs, pos_v, c) - c
                    total = k_count + x_count
                    if dp[a+1][b][c][1] > current_cost + total:
                        dp[a+1][b][c][1] = current_cost + total

                # Add a K if possible and last is not V
                if b < len_k and not last_v:
                    pos_k = ks[b]
                    # Count V's in vs[a:] with pos < pos_k
                    v_count = bisect.bisect_left(vs, pos_k, a) - a
                    # Count X's in xs[c:] with pos < pos_k
                    x_count = bisect.bisect_left(xs, pos_k, c) - c
                    total = v_count + x_count
                    if dp[a][b+1][c][0] > current_cost + total:
                        dp[a][b+1][c][0] = current_cost + total

                # Add an X if possible
                if c < len_x:
                    pos_x = xs[c]
                    # Count V's in vs[a:] with pos < pos_x
                    v_count = bisect.bisect_left(vs, pos_x, a) - a
                    # Count K's in ks[b:] with pos < pos_x
                    k_count = bisect.bisect_left(ks, pos_x, b) - b
                    total = v_count + k_count
                    if dp[a][b][c+1][0] > current_cost + total:
                        dp[a][b][c+1][0] = current_cost + total

min_total = min(dp[len_v][len_k][len_x][0], dp[len_v][len_k][len_x][1])
print(min_total)
```

### Explanation
1. **Preprocessing**: The positions of 'V', 'K', and 'X' characters are extracted from the input string and stored in separate lists.
2. **DP Initialization**: A 4-dimensional DP array is initialized to track the minimal number of swaps required for each state.
3. **State Transitions**: For each state, transitions are considered for adding the next 'V', 'K', or 'X' character. The cost for each transition is computed using binary search to count characters that contribute to inversions.
4. **Result Extraction**: The minimal number of swaps required to form a valid string is obtained from the DP array after processing all characters.

This approach ensures that we efficiently explore all valid configurations while minimizing the number of swaps, leveraging dynamic programming and binary search for optimal performance.