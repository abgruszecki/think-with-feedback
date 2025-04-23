<think>
Okay, let's see. I need to solve this problem where Dasha has to adjust pointers on each of the n strings to form a valid password. The password needs at least one digit, one lowercase letter, and one of the symbols #, *, &. The goal is to find the minimal number of moves required to meet these criteria.

Hmm. So each of the n characters in the password is determined by the current position of a pointer on their respective string. Each string is cyclic. Each move shifts one pointer left or right by one, and each such move counts as one operation. The initial position for all pointers is index 1.

My task is to choose which characters to pick from each string such that the combined password has all three required types. Then calculate the minimal total moves needed.

First, for each of the n strings, I need to know the minimal steps required to move the pointer to any character of a certain type. For example, for each string i, find the minimal steps to get a digit, a lowercase letter, or a special symbol.

Wait, but the problem requires that the final password has at least one of each type. So, I need to select one character from each of three different categories (digit, lowercase, special) across the n strings. But each string can contribute only one character. So, how do I assign which string provides which required type?

The key is that each of the three required types must be present in the password. So, for each of the three types (digit, lowercase, special), we need to assign at least one string to contribute that type, with the minimal steps.

But the same string can't contribute to two types. So, for example, if a string has both a digit and a letter, we can choose to take the digit from it, but then we need letters from another string.

Wait, no. The problem requires that the password (the combination of all the selected characters) has at least one of each type. So, each of the three required types must be covered by at least one of the n characters. So, each of the three types must be present in the password. But each character in the password can contribute to one or more types. For example, if a character is a digit and a letter (but that's impossible here since digits are separate). Or, perhaps a character is a digit and also a special symbol (but the input strings consist of digits, lowercase letters, or the three symbols. So each character is one of these: digit, lowercase, or one of #, *, &. So, each character can only be in one category. So each character in the password can contribute to at most one of the required categories.

So, for each string, when we select a character (by moving the pointer), that character can be a digit, a letter, or a special symbol. Each string's contribution is exactly one of these. Therefore, to satisfy the three required types, we need to have at least one string contributing a digit, at least one contributing a lowercase letter, and at least one contributing a special symbol. The remaining strings can be whatever, but they can't be required to contribute anything else.

But the problem is to choose which of the n strings to assign to each of the three required types. The minimal steps would then be the sum of the steps needed for each of those three strings to reach their assigned type, plus the steps from the other strings (which can be chosen to take the minimal steps, but since they don't contribute to the required types, but they have to contribute a character, but for them, the minimal steps would be to choose the closest character of any type).

Wait, no. Wait, all the strings are part of the password. Each string's selected character is part of the password. So, all n characters are part of the password. The password must have at least one digit, one lowercase letter, and one special. So, the password is a combination of all n characters. So, each of the three required types must be present in at least one of the n characters.

Therefore, the problem reduces to selecting for each string the character (by moving the pointer) such that:

- At least one of the selected characters is a digit.
- At least one is a lowercase letter.
- At least one is a special symbol (#, *, &).

The total steps needed is the sum of all steps taken to move the pointers from their initial position (index 1) to their selected positions.

The objective is to find the minimal sum of steps over all possible choices of characters that meet the three criteria.

So, how to model this?

The approach is to:

1. For each string, compute the minimal steps needed to reach a digit, a lowercase letter, or a special symbol. For example, for string i, compute min steps to digit (d_i), min steps to lowercase (l_i), min steps to special (s_i).

2. Then, select exactly three different strings (since each can contribute at most one of the required types) such that one contributes a digit, another a lowercase, and another a special. The remaining strings can contribute any of their minimal steps (but optimally, they contribute the minimal steps for any type, since their type doesn't affect the requirement once the three are covered).

Alternatively, perhaps the optimal way is to assign each required type to the string that can contribute it with the least steps, but ensuring that all three are covered.

But how?

Because each required type must be present in the password, but other strings can be anything. For example, maybe a string can contribute a digit, but another string can also contribute a digit. So the minimal steps would be to choose the minimal steps for each required type from any of the strings, but each required type must be covered by at least one string.

But how to model this? Let's think in terms of variables.

We need to select for each of the three required types (digit, lowercase, special) which string to take it from. The same string cannot be used for multiple types, because each string contributes only one character (so if a string is chosen to provide a digit, it cannot also provide a lowercase or special).

Wait, no. For example, if a string has both a digit and a lowercase letter, but that's not possible because each character in the string is either a digit, lowercase, or special. So each character is exactly one type. Therefore, each string can contribute only one type. So, when you move the pointer to a position in the string, that position's character is of a certain type, and thus the string contributes that type to the password.

Therefore, each string can contribute exactly one type (digit, lowercase, or special). So, the password's set of types is the union of all the types contributed by each string's chosen character.

So, the problem is to choose for each string the character (and thus the type) such that the union includes all three required types. And the sum of steps for moving each string's pointer to that character is minimized.

Therefore, we need to select for each string i the type t_i (digit, lowercase, or special) such that the sum of steps for all i is minimized, and the union of all t_i includes all three required types.

But how to model this? Since the required types must be covered by at least one t_i.

So, the problem is similar to a covering problem. We need to choose for each string which type to take (with the minimal steps for that type), but ensuring that at least one of the types is a digit, one is lowercase, and one is special.

This sounds like a problem where we can precompute for each string the minimal steps required to get each type, then find a combination where each of the three required types is covered by at least one string, and the sum of all steps is minimized.

But the steps are the sum of the minimal steps for each string's chosen type. But, the chosen type for a string can be any of the three, but the three required types must be covered by at least one string each.

So the approach is:

- For each string, compute the minimal steps required to reach a digit (d), a lowercase (l), a special (s). For each string, these are the possible options. If a string doesn't have a certain type (like no digits), then that option is not available. But the problem states that it's possible to form a valid password, so for each required type, at least one string has that type.

Wait, the input ensures that it's possible to form a valid password. So for each required type (digit, lowercase, special), there's at least one string that has at least one character of that type. So, for the three types, each is present in at least one of the strings.

So, for each string, for each type (digit, lowercase, special), if the string has any characters of that type, compute the minimal steps to reach such a character. If the string has no characters of that type, then that option is invalid (we cannot choose that type for that string).

But in our case, we need to select for each string a type (digits, lowercase, or special) that the string can actually reach (i.e., the string has at least one character of that type). Then, the sum of steps is the sum of the minimal steps for each selected type in each string. The constraints are that in the selected types across all strings, all three required types (digits, lowercase, special) must be present.

The problem is to find the minimal sum of steps over all possible valid selections.

This seems like a problem that can be modeled with dynamic programming, but given the constraints (n up to 50), perhaps a better approach is to precompute for all possible combinations of which strings are assigned to the three required types.

Wait, but how?

Let me think. For each required type (digits, lowercase, special), we need to select at least one string that contributes that type. The other strings can contribute any type (but preferably the one with the minimal steps).

So, perhaps the minimal total steps is achieved by selecting exactly one string for each required type (each assigned to a different type), and the rest of the strings choose the minimal possible steps (regardless of their type).

But that's not necessarily the case. For example, maybe two of the required types are covered by the same string, but that's impossible because each string contributes exactly one type. So, each required type must be covered by at least one string.

But perhaps the best approach is to select three different strings (each for one required type) and sum their minimal steps for those types, plus the sum of the minimal steps for all other strings (regardless of their type). Then, take the minimal such sum.

Wait, that's possible. Because the other strings can contribute any type, but the sum is minimized when they contribute their own minimal steps (the minimal between d, l, s for that string). But we have to ensure that all three required types are covered by the selected three strings.

Wait, but the other strings can contribute to the required types as well. For example, suppose we have four strings. We could select three of them to cover the three required types, and the fourth can contribute any type. But if the fourth contributes a required type, that's okay. So the minimal sum could involve selecting more than three strings contributing the required types, but that's allowed. The problem requires that at least one of each required type is present. So, the minimal sum is the sum of all steps for all strings, where for each string we choose a type (digits, lowercase, or special) that it can reach, and the union of all chosen types includes all three required types.

So, the problem is to choose for each string the type (d, l, s) it contributes (with minimal steps for that type), such that all three required types are covered, and the sum is minimized.

But how to model this selection?

An alternative approach is:

- For each string, compute the minimal steps for each possible type (if possible). If a string cannot contribute a certain type, then that type is not available for selection.

- Then, the problem reduces to selecting a type for each string (from available options), such that the sum is minimized, and the selected types collectively include all three required types.

So, the variables are the selected type for each string, and the constraints are that the set of selected types includes at least one of each required type.

But given that n can be up to 50, enumerating all possible combinations is not feasible.

Therefore, a better approach is needed.

Hmm. Let's think about the problem in terms of coverage. We need to cover the three required types. Each string contributes one type, which may cover one or more of the required types. The sum is the sum of the minimal steps for each string's selected type. The goal is to minimize the sum, ensuring that all three required types are covered.

But this is a set cover problem where each element (string) can cover one of the types, and the goal is to cover all three types. But since each string can contribute exactly one type, the problem becomes similar to choosing which strings to assign to each required type, but with the possibility that other strings contribute to redundant coverage.

But the sum is the sum of all selected steps for all strings, not just the ones covering the required types. So, even the strings not assigned to cover a required type contribute their steps. Therefore, the minimal sum would be achieved by covering the three required types with the minimal possible steps, and for the remaining strings, choose their own minimal possible steps (regardless of type).

Wait, perhaps the optimal way is:

- Assign each of the three required types to exactly one string (the one that can cover it with minimal steps), and for the remaining strings, choose the type that gives the minimal steps for that string, regardless of which type it is.

But this approach may not work because:

1. The same string can cover multiple required types (but only if it's allowed to contribute to all, but each string can contribute only one type. For example, a string that has both a digit and a lowercase character. But that's impossible, since each character in the string is exactly one type.

So, each string can contribute exactly one of the three required types (if it has at least one character of that type). So, the idea is to select a subset of three (not necessarily distinct) strings such that:

- One covers a digit with minimal steps, another a lowercase, another a special.

But wait, no. Because the same string can't cover two types, since it can only contribute one. So, each required type must be covered by at least one distinct string (or maybe not, if another string covers it as well). But the problem requires that all three are present in the password. So, if two required types are covered by a single string, that's impossible. Each string contributes exactly one type. Therefore, each required type must be covered by at least one different string.

Wait, no. Suppose one string contributes a digit, another contributes a lowercase, and the third contributes a special. The remaining n-3 strings can contribute any type, but their contributions don't affect the required coverage. So the sum would be the steps for all n strings (each contributing their own type), but the three required types must be present in the collection of all n types.

Therefore, the minimal sum is the sum of all steps (each string's chosen type's minimal steps) plus the condition that at least one of the three required types is present in the collection.

But how to model that.

This seems like a problem that can be modeled as a bitmask, where the state is the coverage of the required types (digit, lowercase, special). The state starts as 0 and needs to reach 7 (binary 111). For each string, when we choose its type, we can update the state by OR-ing with the bitmask of that type (digit is 001, lowercase 010, special 100). The sum is the sum of the steps for each choice. The goal is to find the minimal sum that results in a state of 7.

But how to compute this efficiently.

Given that n is up to 50, and the state is 3 bits (8 possible states), the DP approach is feasible.

Let me think. The dynamic programming state can be represented as the current coverage (mask), and the number of strings processed. For each step (processing each string), we can choose the type (d, l, s) that the string can contribute, and update the mask by OR-ing with the corresponding bits. The DP tracks the minimal sum of steps required to reach each mask after processing each string.

The initial state is mask 0 (no coverage) and sum 0. For each string, for each possible current mask, and for each possible type (d, l, s) that the string can contribute, compute the new mask (mask | type_mask) and update the sum by adding the steps required for that type. The final answer is the minimal sum in the state where mask is 7 (all three types covered) after processing all strings.

Yes, this seems manageable. The DP will have O(n * 8) states. For each of the n strings, and for each possible mask (8 possibilities), we track the minimal sum.

The steps for each string are precomputed. For each string i, we have the minimal steps to get a digit (d_steps), lowercase (l_steps), or special (s_steps). But if the string doesn't have any characters of a certain type, then that option is not available.

So for each string, we need to check which types are available. For example, if a string has no digits, then we can't choose d_steps for that string.

The DP transitions would then consider all available types for the current string and update the mask accordingly.

Let's outline the steps:

1. Precompute for each string i the minimal steps to reach each type (d, l, s). If a type is not present in the string, that entry is infinity or marked as unavailable.

   For each string, iterate through each character (from 0 to m-1 or 1 to m?), compute the distance from the initial position (1) to each character's position. The minimal steps to reach a character of a certain type is the minimal distance among all characters of that type in the string.

   The distance is the minimal steps between moving left or right. Since the string is cyclic, the minimal steps for position j (assuming the positions are 1-based) from the initial position (1) can be calculated as min(abs(j-1), m - abs(j-1)).

   So for each string, for each position, check the character's type and compute the distance. Then, for each type (digit, lowercase, special), find the minimal distance among all positions of that type in the string.

   For example, for a string, if there are digits at positions 3 and 5 (1-based), then the minimal steps for digit is the minimal of (3-1 steps to the right, m - (3-1) steps to the left) and similarly for position 5.

   Then, for each string, we collect the minimal steps for each type, if available.

   So, for each string i:

   - d_steps: minimal steps to reach a digit, or None if none exists.

   - l_steps: same for lowercase.

   - s_steps: same for special symbols.

2. Initialize a DP table. The DP state is a mask (0-7) and the current sum. For each string, we process them one by one, updating the DP state.

   The initial state is mask 0 and sum 0.

   For each string, for each possible mask (current coverage), and for each possible type (d, l, s) that the string can contribute (i.e., steps for that type are not None), we compute the new mask and new sum. The new mask is the OR of the current mask and the type's bit (e.g., d contributes 1, l contributes 2, s contributes 4). The new sum is the current sum plus the steps for that type. We keep track of the minimal sum for each new mask.

   So for each string i, and for each possible mask in the current DP, we consider all possible type choices (d, l, s) that are available for i, and update the next DP state accordingly.

3. After processing all strings, the answer is the minimal sum in the mask 7 (all three types covered).

But how to handle the DP transitions.

Let me think of the DP as a dictionary where the keys are the mask, and the value is the minimal sum to reach that mask. We start with {0: 0}.

For each string, we process the current DP and create a new DP for the next step.

For example, for each mask in the current DP, and for each possible type (d, l, s) available in the current string, compute the new mask and update the new DP accordingly.

Let me try to outline the code steps.

First, precompute for each string the minimal steps for each type.

Then, initialize dp = {0: 0}.

For each string in the list of strings:

   new_dp = {}

   for each mask in dp:

      current_sum = dp[mask]

      for each type in (d, l, s) that is available for this string:

          steps = steps_for_type

          new_mask = mask | (bit corresponding to type)

          new_sum = current_sum + steps

          if new_mask is not in new_dp or new_sum < existing value:

              new_dp[new_mask] = min(new_dp.get(new_mask, infinity), new_sum)

   dp = new_dp

Wait, but this is not exactly correct. Because for each string, you can choose exactly one type (the one you select for that string), and the mask is updated by OR-ing with that type's bit.

Yes. So, for each string, for each possible mask in the current state, and for each possible type (available for that string), we compute the new mask and add the steps.

So, after processing all strings, the dp will have masks that can be built by OR-ing the types from each string. The minimal sum for mask 7 is the answer.

Yes. Because each string's chosen type contributes to the mask. So, after processing all strings, the mask 7 (111 in binary) means that all three types are covered.

This approach seems correct.

Now, the key steps are:

1. Precompute for each string the minimal steps for each type.

2. For each string, create a list of available types and their steps.

3. Perform the DP transitions as described.

Now, handling the first step: for each string, find the minimal steps to reach each type.

So, for each string (i.e., each of the n lines after the first), we need to check each character and compute the minimal steps for each type.

For example, let's take the first sample input:

3 4

1**2 → the string is "1**2". The characters are 1, *, *, 2.

Indices 1 to 4.

Initial position is 1.

For the first string (index 1-based?), the initial pointer is at 1.

To reach each character:

At index 1: steps 0 (initial position). The character is '1', which is a digit. So, steps for digit is 0.

Other digits in the string: index 4 (character '2'). The distance from 1 to 4 is 3 steps right (1->2->3->4) or 1 step left (1->4 via cycle). So the minimal steps is 1.

So for digit steps, the minimal is min(0, 1) → 0 (from the first character).

For lowercase letters: this string has none. So l_steps is not available.

For special symbols: the characters are at positions 2, 3. Let's compute the steps from 1.

Position 2: steps right 1 (1->2) or left 3 (since m=4). Minimal steps is 1.

Position 3: steps right 2 (1->2->3) or left 2 (1->4->3). Minimal steps is 2.

So minimal steps for special is min(1, 2) → 1.

So for this string:

d_steps = 0 (available), l_steps = not available, s_steps = 1 (available).

So when processing this string in the DP, the possible choices are d (steps 0) and s (steps 1).

The second string is "a3*0".

It has a lowercase 'a' at position 1 (steps 0), digits '3' at position 2 (steps 1 right or 3 left, min 1), '0' at position 4 (steps 3 right or 1 left → min 1).

So minimal digit steps for this string is min(1 (for '3') and 1 (for '0') → 1.

The special symbols here is '*' at position 3. Steps from 1: right 2 (1->2->3) or left 2 (1->4->3). Minimal steps 2.

So for this string:

d_steps is 1, l_steps is 0 (from 'a'), s_steps is 2.

Third string is "c4**".

Lowercase 'c' at position 1 (steps 0).

Digit '4' at position 2: steps right 1 (1->2) → steps 1.

Special symbols at positions 3 and 4: for position 3, steps right 2 (1->2->3) → steps 2, or left 2 (1->4->3) → steps 2. For position 4: steps right 3 or left 1. Minimal steps 1.

So for special steps: min steps is 1 (from position 4). So s_steps is 1.

So for this string, d_steps is 1, l_steps is 0, s_steps is 1.

Now, the DP process:

Initially, dp is {0: 0}.

Processing the first string:

Possible choices: d (steps 0) or s (steps 1).

For each choice:

- Choosing d: new_mask is 0 | 1 = 1. sum is 0 + 0 = 0.

- Choosing s: new_mask is 0 | 4 = 4. sum is 0 + 1 = 1.

So new_dp after first string is {1:0, 4:1}.

Processing the second string:

For each mask in new_dp (mask 1 and 4):

For mask 1 (sum 0):

   available types: d (steps 1), l (0), s (2).

   For each type:

   - d: new_mask = 1 | 1 = 1. sum becomes 0 + 1 = 1. So existing entry for mask 1 may be updated if this sum is lower than previous (but previous was 0 for mask 1). So in this case, mask 1 already has sum 0, adding 1 would not replace it.

   - l: new_mask = 1 | 2 = 3. sum is 0 + 0 = 0. So mask 3 now has sum 0.

   - s: new_mask = 1 |4 =5. sum is 0 +2=2. So mask5: 2.

For mask 4 (sum 1):

   available types: d (1), l (0), s (2).

   - d: new_mask 4 |1=5. sum 1+1=2. So mask5's current value is 2 (from previous) and this is same as from mask4 and choosing d.

   - l: new_mask 4 |2=6. sum 1+0=1. So mask6:1.

   - s: new_mask 4 |4=4. sum 1+2=3. So mask4's sum would be 3, but existing is 1, so no update.

So after processing the second string, the new_dp will have:

mask3:0, mask1:0 (from original mask1 but for choosing l in the second string?), mask5:2, mask6:1.

Wait, maybe I should re-calculate.

Let me retrace:

After processing the first string, dp is {0b001:0, 0b100:1}.

Processing the second string:

For mask 0b001 (sum 0):

   For each possible type in the second string (d=1, l=0, s=2):

   type d: new_mask 0b001 | 0b001 = 0b001. sum 0 +1=1. So mask 001 in new_dp would be min between existing (none) and 1. So new_dp for mask 001 is 1.

   type l: new_mask 0b001 | 0b010 = 0b011. sum 0 +0=0. So mask 3 (0b011) with sum 0.

   type s: new_mask 0b001 |0b100 = 0b101. sum 0 +2=2. So mask5 (101) sum 2.

For mask 0b100 (sum 1):

   type d: new_mask 0b100 |0b001=0b101. sum 1+1=2. So mask5 sum 2 (existing is 2 from previous, same as here. So min is 2.

   type l: new_mask 0b100 |0b010=0b110. sum 1+0=1. So mask6 (110) sum 1.

   type s: new_mask 0b100 |0b100=0b100. sum 1+2=3. So mask4 sum 3. But existing mask4 in the new_dp? No, because the new_dp is built from the previous processing.

So after processing the second string, the new_dp entries are:

mask 001:1 (from mask 001, type d), mask 011:0 (from mask001, type l), mask101:2 (from mask001, type s), mask101 (from mask100, type d): sum 2, mask110:1 (from mask100, type l), mask100:3 (from mask100, type s).

But the new_dp is built by considering all possibilities. So for each possible transition, we take the minimal sum for each mask.

So for mask 001, the possible sum is 1. But in the new_dp, for each mask, we take the minimal sum.

But in the new_dp, the mask 0b011 (3) has sum 0. Mask 0b110 (6) has sum 1. Mask 0b101 (5) has sum 2.

So the new_dp after second string is:

mask3:0, mask5:2, mask6:1, mask1:1, mask4:3.

Wait, but I'm getting confused here. Maybe the correct approach is for each possible mask in the current new_dp, for each possible choice of the current string's type, and then update the new_dp with the minimal sum.

So after processing the second string, the new_dp would have entries:

- mask3 (binary 011) with sum 0 (from mask001 choosing l).

- mask6 (110) with sum 1 (from mask100 choosing l).

- mask5 (101) with sum 2 (from mask001 choosing s, or mask100 choosing d).

- mask001 (001) with sum 1 (from mask001 choosing d).

- mask4 (100) with sum 3 (from mask100 choosing s).

But when building new_dp, for each new_mask, we keep the minimal sum. So, for example, mask5 may have two entries (sum 2 and 2), so the minimal is 2.

But the new_dp is initialized as empty for each string. So for each possible transition, the new_dp is built by considering all possibilities and taking the minimal sum for each mask.

So after the second string, the new_dp would be:

mask3:0 (from mask001, l steps)

mask6:1 (from mask100, l steps)

mask5:2 (from mask001, s steps, and mask100, d steps, both sum 2)

mask1:1 (from mask001, d steps)

mask4:3 (from mask100, s steps)

But which of these is the minimal sum for each mask.

For mask3, sum 0 is the only entry.

For mask5, sum 2.

For mask6, sum 1.

For mask1, sum 1.

For mask4, sum 3.

Now, moving to the third string.

The third string has d_steps 1, l_steps 0, s_steps 1.

Processing this string:

For each mask in new_dp (mask3,6,5,1,4) with their respective sums.

Let's process each mask one by one.

For mask3 (sum 0):

Possible choices for third string: d (1), l (0), s (1).

- Choosing d: new_mask = 3 | 1 = 3. sum is 0 +1=1. So mask3's sum could be updated to 1, but since the current sum for mask3 in new_dp is 0, this is higher. So no change.

- Choosing l: new_mask = 3 | 2 = 3. sum 0 +0=0. No change.

- Choosing s: new_mask =3 |4=7. sum 0+1=1. So new_mask7:1.

For mask6 (sum 1):

Choices: d, l, s.

- d: mask6 |1=7. sum 1+1=2.

- l: mask6 |2=6. sum 1+0=1. (no change)

- s: mask6 |4=6|4=6 |4= 6's bits are 110, OR 100 is 110 |100 = 110? Wait no. Wait mask6 is 110 (binary), which is 6 (since 1*4 + 1*2 + 0*1=6). OR with 4 (100) gives 110 | 100 = 110 (binary 110), no. Wait no. 6 is 110 in binary. 4 is 100. OR is 110 | 100 = 110. So mask6 |4=6. So adding s steps (1) would give sum 1+1=2. So new_mask is 6, sum 2. But existing sum for mask6 is 1, which is lower.

For mask5 (sum 2):

Choices: d, l, s.

- d: 5 |1=5 |001= 5 (since 5 is 101). sum 2+1=3. new_mask5:3.

- l: 5 |2=7. sum 2+0=2. new_mask7:2.

- s:5 |4=5 |100= 5 |4= 5+4=9? No. 5 is 101 in binary. 4 is 100. OR is 101 | 100 = 101, which is 5. So new_mask5. sum 2+1=3. So same as before.

For mask1 (sum 1):

Choices: d, l, s.

- d:1 |1=1. sum1+1=2.

- l:1 |2=3. sum1+0=1. So new_mask3:1.

- s:1 |4=5. sum1+1=2. new_mask5:2.

For mask4 (sum3):

Choices: d, l, s.

- d:4 |1=5. sum3+1=4.

- l:4 |2=6. sum3+0=3. new_mask6:3.

- s:4 |4=4. sum3+1=4.

So after processing the third string, the new_dp would be built from all possible transitions.

But the key transitions that contribute to mask7 are:

From mask3 (sum0) choosing s steps (sum1), resulting in mask7.

From mask5 (sum2) choosing l steps (sum2), resulting in mask7.

From mask6 (sum1) choosing d steps (sum2), resulting in mask7.

Other transitions may also contribute.

But the minimal sum for mask7 is the minimal of these.

So after processing all three strings, the minimal sum for mask7 is 1 (from mask3 choosing s steps with sum 1) or 2 (from mask5 choosing l steps, sum 2+0=2) or other possibilities.

Wait, let's see.

In the first sample input, the expected output is 1. Let's see.

The first string can choose d (steps 0), second chooses l (steps 0), third chooses s (steps 1). Sum is 0+0+1=1. Which is the correct answer.

In the DP approach, this path corresponds to:

After first string, mask 1 (digits), sum 0.

Second string chooses l (steps 0), mask becomes 3 (digits and lowercase), sum 0.

Third string chooses s (steps 1), mask becomes 7, sum 0+1=1.

Yes, so the mask7 would have sum 1.

Which is the minimal.

So the DP approach should capture this.

In the processing of the third string, the mask3 (sum0) is available. Choosing s steps (1) adds sum1, and new_mask becomes 3 |4=7. So mask7's sum is 1.

Other paths could contribute higher sums. For example, the path where third string chooses l steps (sum0), but that leaves the mask as 3, not covering the special.

But after all three strings are processed, the mask7's sum would be 1.

Thus, the DP approach works.

Now, the code steps:

Implementing this in Python.

First, read n and m.

Then read n strings.

For each string, compute the minimal steps for each type (d, l, s).

For a string, we can process each character:

Loop through each position (0-based or 1-based? The input is 1-based according to the problem statement. The initial position is 1, and moving left from 1 to m, etc.)

But in code, the positions are 0-based or 1-based? Let's be careful.

The problem statement says that each pointer starts at position 1 (1-based).

Each string has m characters, positions 1-based.

So for a character at position j (1-based), the minimal steps from initial position (1) is min( (j-1), m - (j-1) ). Because moving right (j-1 steps) or left (m - (j-1)) steps.

So for each character in the string (1-based index j), compute the steps required to move from 1 to j.

So for each string:

Initialize d_steps as infinity, l_steps as infinity, s_steps as infinity.

For each position j (1-based) from 1 to m:

   char = string[j-1] (since Python strings are 0-based).

   steps = min( abs(j-1), m - abs(j-1) )

   if char is a digit:

       if steps < d_steps:

           d_steps = steps

   elif char.islower():

       if steps < l_steps:

           l_steps = steps

   elif char in {'#', '*', '&'}:

       if steps < s_steps:

           s_steps = steps

After processing all positions, for each type, if steps are still infinity, then the type is not available for this string.

But since the problem guarantees that a valid password is possible, each of the three types must be available in at least one string.

Now, for the DP.

Initialize dp as a dictionary: {0:0}.

Then, for each string in the list of strings:

   current_dp = dp.copy()

   new_dp = defaultdict(lambda: float('inf'))

   for mask in current_dp:

       current_sum = current_dp[mask]

       # check each possible type for this string

       if d_steps is not infinity:

           new_mask = mask | 1

           new_sum = current_sum + d_steps

           if new_sum < new_dp[new_mask]:

               new_dp[new_mask] = new_sum

       if l_steps is not infinity:

           new_mask = mask | 2

           new_sum = current_sum + l_steps

           if new_sum < new_dp[new_mask]:

               new_dp[new_mask] = new_sum

       if s_steps is not infinity:

           new_mask = mask | 4

           new_sum = current_sum + s_steps

           if new_sum < new_dp[new_mask]:

               new_dp[new_mask] = new_sum

   # after processing all masks, update dp

   dp = new_dp

Wait, but the initial code would overwrite dp with new_dp for each string, and new_dp starts as empty. But in Python, defaultdict might not be the best approach. Instead, for each string, create a new dictionary (new_dp) to track the minimal sums for each mask.

But in code, perhaps using a dictionary where the keys are masks and the values are the minimal sums.

So for each string:

   new_dp starts empty.

   for each mask in the current dp:

       current_sum = dp[mask]

       for each type that the string can contribute (d, l, s):

           if the steps for that type are available (not infinity):

               new_mask = mask | type_bit

               new_sum = current_sum + steps

               if new_mask is not in new_dp or new_sum < new_dp[new_mask]:

                   new_dp[new_mask] = new_sum

   then, set dp = new_dp.

Wait, but how to handle multiple transitions to the same mask. For example, multiple paths can reach the same mask, and we need to keep the minimal sum.

In code:

For each string, create a new_dp which is a dictionary. For each existing mask in the current dp, and for each possible type choice in the current string, compute new_mask and new_sum, and update new_dp accordingly.

But to do this correctly, for each existing mask in the current dp:

   for each possible type in the current string:

       compute new_mask and new_sum.

       if new_mask is already in new_dp, take the minimum between existing new_sum and the current new_sum.

So, in code:

new_dp = {}

for mask in current_dp:

    current_sum = current_dp[mask]

    # check d, l, s for current string

    if d_available:

        new_mask = mask | 1

        new_sum_val = current_sum + d_steps

        if new_mask not in new_dp or new_sum_val < new_dp[new_mask]:

            new_dp[new_mask] = new_sum_val

    if l_available:

        new_mask = mask | 2

        new_sum_val = current_sum + l_steps

        if new_mask not in new_dp or new_sum_val < new_dp[new_mask]:

            new_dp[new_mask] = new_sum_val

    if s_available:

        new_mask = mask |4

        new_sum_val = current_sum + s_steps

        if new_mask not in new_dp or new_sum_val < new_dp[new_mask]:

            new_dp[new_mask] = new_sum_val

But in Python, this can be implemented with a loop.

But note that for the new_dp, for each new_mask, we need to compare and take the minimal sum.

But the way to handle this is to, for each possible new_mask, compute the minimal sum from all possible transitions that lead to it.

So, for each existing mask in the current dp, and for each possible type in the current string, we generate new_mask and new_sum_val. For each new_mask, we check if it's already in new_dp and update it to the minimal sum.

So, the code for processing each string would be:

for each string in strings:

    new_dp = {}

    for mask in dp:

        current_sum = dp[mask]

        # process each type

        if d_steps is not None:

            nm = mask | 1

            ns = current_sum + d_steps

            if nm not in new_dp or ns < new_dp[nm]:

                new_dp[nm] = ns

        if l_steps is not None:

            nm = mask | 2

            ns = current_sum + l_steps

            if nm not in new_dp or ns < new_dp[nm]:

                new_dp[nm] = ns

        if s_steps is not None:

            nm = mask |4

            ns = current_sum + s_steps

            if nm not in new_dp or ns < new_dp[nm]:

                new_dp[nm] = ns

    # update dp to new_dp

    dp = new_dp

Wait, but after the first string, the new_dp may have multiple masks, and each is the minimal sum for that mask.

But in code, the initial dp is {0:0}.

Now, for each string, we process all possible masks in the current dp, and for each type available in the current string, we add new entries to new_dp. For each new_mask, we keep the minimal sum.

So, for example, if two different masks in the current dp (mask1 and mask2) can reach the same new_mask via different paths, the new_dp will take the minimal sum.

Yes.

Now, after processing all strings, the answer is dp[7], which is the sum of steps for the minimal path that covers all three types.

So, the code outline is:

Read n, m.

Read the n strings.

For each string:

   compute d_steps, l_steps, s_steps.

   (if a type is not present, set its steps to None or infinity.)

Initialize dp = {0:0}.

For each string in strings:

   create new_dp as empty dict.

   for each mask in dp:

       current_sum = dp[mask]

       if the string can contribute a digit:

           new_mask = mask | 1

           new_sum = current_sum + d_steps

           update new_dp[new_mask] with the minimal sum.

       same for lowercase and special.

   dp = new_dp.copy()

At the end, output dp.get(7, ...).

But the problem says that it's possible to form a valid password, so 7 must be present in dp after processing all strings.

Now, implementing this.

But wait, how to compute d_steps, l_steps, s_steps.

In code:

For each string in the input:

   d_steps = minimal steps to reach a digit.

   l_steps = minimal steps to reach a lowercase.

   s_steps = minimal steps to reach a special.

   For each position (1-based) j in the string:

       char = string[j-1]

       steps = min( (j-1) % m, m - (j-1) % m )

Wait, no: steps is min( (j-1) steps to the right (since from 1 to j), or m - (j-1) steps to the left (since moving left from 1 to j via the cycle).

For example, if j is 1, steps is 0.

If j is m (assuming m is 4), then steps right is 3, left is 1. min is 1.

So for each j (1-based) in the string:

steps = min( abs(j-1), m - abs(j-1) )

But j is from 1 to m.

Alternatively:

steps = min( (j - 1) % m, (m - (j-1)) % m )

But since j-1 can be from 0 to m-1, (j-1) mod m is j-1. (m - (j-1)) mod m is m - (j-1) when j-1 < m.

Wait, but m is the length of the string, so j can't exceed m.

So, steps is min( (j-1), m - (j-1) )

But j ranges from 1 to m.

So, for each character in the string (index j, 1-based), compute steps as min( j-1, m - (j-1) )

So, for each string:

d_steps = infinity

l_steps = infinity

s_steps = infinity

for j in range(1, m+1):

   pos = j-1 (0-based for Python)

   char = s[pos]

   steps = min(j-1, m - (j-1))

   if char.isdigit():

       if steps < d_steps:

           d_steps = steps

   elif char.islower():

       if steps < l_steps:

           l_steps = steps

   elif char in {'#', '*', '&'}:

       if steps < s_steps:

           s_steps = steps

But initializing d_steps as infinity, etc.

Then, after processing all characters, if d_steps is infinity, then the string has no digits.

Similarly for others.

But the problem says that for each of the three types, there is at least one string that can contribute it. So, for the three types, there's at least one string with d_steps not infinity, etc.

Now, in code:

We'll process each string, compute d_steps, l_steps, s_steps.

Then, for each string, if a type is not available (steps is infinity), then we skip that type in the transitions.

Now, putting this together.

In code:

n, m = map(int, input().split())

strings = [input().strip() for _ in range(n)]

# Precompute for each string the minimal steps for each type.

steps_list = []

for s in strings:

    d_steps = float('inf')

    l_steps = float('inf')

    s_steps = float('inf')

    for j in range(1, m+1):

        char = s[j-1]

        steps = min(j-1, m - (j-1))

        if char.isdigit():

            if steps < d_steps:

                d_steps = steps

        elif char.islower():

            if steps < l_steps:

                l_steps = steps

        elif char in {'#', '*', '&'}:

            if steps < s_steps:

                s_steps = steps

    # Now, collect the available types and their steps.

    steps_info = []

    if d_steps != float('inf'):

        steps_info.append( (1, d_steps) )

    if l_steps != float('inf'):

        steps_info.append( (2, l_steps) )

    if s_steps != float('inf'):

        steps_info.append( (4, s_steps) )

    steps_list.append(steps_info)

# Initialize DP.

dp = {0: 0}

for steps_info in steps_list:

    new_dp = {}

    for mask in dp:

        current_sum = dp[mask]

        for (type_bit, steps) in steps_info:

            new_mask = mask | type_bit

            new_sum = current_sum + steps

            if new_mask not in new_dp or new_sum < new_dp[new_mask]:

                new_dp[new_mask] = new_sum

    dp = new_dp

print(dp[7])

This code should work.

Let's test it against the first sample input.

Sample input 1:

3 4

1**2 → steps for digit is 0, special is 1.

a3*0 → digit steps 1, lowercase steps 0, special steps 2.

c4** → digit steps 1, lowercase steps 0, special steps 1.

Steps_list will be for each string:

1st string: [(1,0), (4,1)].

2nd string: [(1,1), (2,0), (4,2)].

3rd string: [(1,1), (2,0), (4,1)].

Processing first string:

new_dp has mask 0 |1=1 (sum0+0=0), and mask0 |4=4 (sum0+1=1). So dp is {1:0, 4:1}.

Processing second string:

For each mask in dp:

mask1 (sum0):

steps_info is [(1,1), (2,0), (4,2)].

So for each type_bit:

1: new_mask 1 |1=1. sum 0+1=1. new_dp[1] = 1.

2: new_mask 1|2=3. sum0+0=0. new_dp[3] =0.

4: new_mask 1|4=5. sum0+2=2. new_dp[5] =2.

mask4 (sum1):

steps_info same.

type_bit 1: new_mask 4|1=5. sum1+1=2. So new_dp[5] is min(2, previous 2) → 2.

type_bit 2: new_mask4|2=6. sum1+0=1. new_dp[6] =1.

type_bit4: new_mask4|4=4. sum1+2=3. new_dp[4] =3.

So new_dp after second string is:

mask3:0, mask6:1, mask5:2, mask1:1, mask4:3.

Processing third string:

steps_info is [(1,1), (2,0), (4,1)].

For each mask in dp:

mask3 (sum0):

process each type_bit:

1: new_mask3 |1=3. sum0+1=1. new_dp[3] is 1.

2: new_mask3 |2=3. sum0+0=0. new_dp[3] =0.

4: new_mask3 |4=7. sum0+1=1. new_dp[7] =1.

mask6 (sum1):

process each type_bit:

1: new_mask6 |1=7. sum1+1=2. new_dp[7] is min(1,2) → 1.

2: new_mask6 |2=6. sum1+0=1. new_dp[6] =1.

4: new_mask6 |4=6 |4=6. sum1+1=2. new_dp[6] =1 (original sum1).

mask5 (sum2):

process each type_bit:

1: new_mask5 |1=5. sum2+1=3.

2: new_mask5 |2=7. sum2+0=2. new_dp[7] is min(1,2) →1.

4: new_mask5 |4=5 |4=5. sum2+1=3.

mask1 (sum1):

process each type_bit:

1: new_mask1 |1=1. sum1+1=2.

2: new_mask1 |2=3. sum1+0=1. new_dp[3] =0 (existing sum0 is better).

4: new_mask1 |4=5. sum1+1=2.

mask4 (sum3):

process each type_bit:

1: new_mask4 |1=5. sum3+1=4.

2: new_mask4 |2=6. sum3+0=3.

4: new_mask4 |4=4. sum3+1=4.

So after processing the third string, the new_dp will have:

mask7:1 (from mask3 choosing 4), and other masks.

The minimal sum is 1.

Which matches the sample.

The second sample input:

5 5

#*&#*

*a1c&

&q2w*

#a3c#

*&#*&

Expected output:3.

The code should process this correctly.

But since the code is correct for the first sample, and the DP approach covers all possibilities, it should handle the second sample correctly.

Thus, this code should be the solution.
</think>

```python
n, m = map(int, input().split())
strings = [input().strip() for _ in range(n)]

steps_list = []
for s in strings:
    d_steps = float('inf')
    l_steps = float('inf')
    s_steps = float('inf')
    for j in range(1, m + 1):
        char = s[j-1]
        steps = min(j-1, m - (j-1))
        if char.isdigit():
            if steps < d_steps:
                d_steps = steps
        elif char.islower():
            if steps < l_steps:
                l_steps = steps
        elif char in {'#', '*', '&'}:
            if steps < s_steps:
                s_steps = steps
    steps_info = []
    if d_steps != float('inf'):
        steps_info.append((1, d_steps))
    if l_steps != float('inf'):
        steps_info.append((2, l_steps))
    if s_steps != float('inf'):
        steps_info.append((4, s_steps))
    steps_list.append(steps_info)

dp = {0: 0}
for steps_info in steps_list:
    new_dp = {}
    for mask in dp:
        current_sum = dp[mask]
        for (type_bit, steps) in steps_info:
            new_mask = mask | type_bit
            new_sum = current_sum + steps
            if new_mask in new_dp:
                if new_sum < new_dp[new_mask]:
                    new_dp[new_mask] = new_sum
            else:
                new_dp[new_mask] = new_sum
    dp = new_dp

print(dp[7])
```