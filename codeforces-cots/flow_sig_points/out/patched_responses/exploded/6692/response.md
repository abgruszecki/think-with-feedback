<think>
Okay, so I need to solve this problem where I have to determine the number of dead bulbs for each color in a garland. Let's read the problem carefully.

The garland is structured such that any four consecutive bulbs are all different colors. So the pattern repeats every four bulbs, but each group of four has unique colors. The input string has some bulbs marked with '!' which are dead. The task is to figure out how many of each color are missing (i.e., how many '!'s correspond to each color).

Hmm, the key here is to figure out the correct positions of each color based on the existing known bulbs. Since the garland follows a strict pattern where every four consecutive bulbs are all different, the entire sequence must be a rotation of a four-color cycle. Wait, but how exactly?

Wait, let's think. The problem says that the garland is made such that any four consecutive bulbs are all different. So, for example, if the first four are R, B, Y, G, then the next four must start with B, Y, G, and then the next which can't be R (since the previous three are Y, G, B?), no, wait. Wait, the four consecutive must all be different. So the sequence must be a repetition of a four-color cycle, but with each consecutive group of four overlapping by three. Like for example RYBGRYBGRY... Here, each new character is the next in the cycle, but after the fourth character (R), the next has to be the first again. Wait, but how can that work? Because if the first four are R, B, Y, G, then the next four would be B, Y, G, R (since the next character after G is R?), but then the fifth character is R. But then the four-consecutive starting at position 2 would be B, Y, G, R, which are all unique. Then the next group (positions 3-6) would be Y, G, R, B (if the next is B). Wait, maybe the entire sequence is a cycle of four colors, but shifted each time. So for example, the first four are R, B, Y, G. Then the fifth is R again? But then the group of four starting at position 2 would be B, Y, G, R—all unique. Then the next group (positions 3-6) would be Y, G, R, B—again unique. So this seems possible. Wait, but in this case, the sequence is R B Y G R B Y G..., which would have consecutive groups of four that are all unique. Wait, but each group of four consecutive is R B Y G, then B Y G R, etc. So the pattern is a rotation of the original four.

But how do we model this? The key insight here is that the sequence must form a repeating pattern of four colors, such that each consecutive set of four is a permutation. So the entire garland is a cyclic sequence of the four colors. For example, the order could be R, B, Y, G, R, B, Y, G, etc. But any rotation of this cycle would also satisfy the condition.

Wait, but if the cycle is R, B, Y, G, then the next character after G is R again. Then the four consecutive starting at position 0 is R B Y G, starting at 1 is B Y G R, etc. Each of these groups has all four colors. So the entire garland is a repetition of the four-color cycle. So the sequence must be a repetition of a four-character sequence where all four are distinct, and each consecutive group of four is a cyclic shift of the initial four.

So the entire sequence is determined by the initial four characters. But given that some of them might be unknown (i.e., replaced by '!'), but the problem states that the input is a valid garland with some dead bulbs, meaning that the non-'!' characters must conform to this pattern.

So the problem reduces to determining the original four-color cycle (the base pattern), then for each '!' in the input, we can determine which color it should be, based on its position in the sequence.

So the approach would be:

1. Determine the order of the four colors in the base pattern (the first four positions). Once we know the order, we can compute the color of any position i as pattern[i mod 4].

But how do we find the base pattern given some known characters in the input?

The input has some positions filled with R, B, Y, G. For example, the input might have some characters that are not '!', and these must fit into the base pattern. So the base pattern can be determined by finding the correct order of the four colors such that all existing non-'!' characters in the input are consistent with their positions in the pattern.

Once the base pattern is known, each '!' in the input can be replaced by the corresponding color in the pattern, and then we count how many '!' correspond to each color.

So the main challenge is to find the correct base pattern.

Let's think about how to find the base pattern. Let's denote the four positions in the base pattern as pos0, pos1, pos2, pos3. These are the four colors in order. So for any position i in the input string, the expected color is base[i mod 4]. 

But since the input is a valid garland (with possible dead bulbs), the existing non-'!' characters must align with this pattern. So for each non-'!' character in the input, we can check what its position modulo 4 is, and that must be the color in the base pattern at that index mod 4.

So the approach is to collect all the constraints from the input. For each character in the input that is not '!', we know that the base pattern at position (i mod 4) must be that character.

For example, suppose the input is "!RGYB". Let's index this as positions 0 to 4 (since length is 5). 

At position 0: '!', so no info.
At position 1: 'R' → base[1 mod 4 = 1] must be 'R'.
At position 2: 'G' → base[2 mod4 =2] must be 'G'.
At position3: 'Y' → base[3 mod4=3] must be 'Y'.
At position4: 'B' → base[4 mod4=0] must be 'B'.

So the base pattern is [B, R, G, Y].

Wait, the indices mod4 for the input string are:

position 0 → 0 mod4=0 → base[0]
position 1 → 1 mod4=1 → base[1]
position 2 → 2 mod4=2 → base[2]
position3 →3 mod4=3 → base[3]
position4 →4 mod4=0 → base[0], etc.

So the input characters at positions 1,2,3,4 give the following constraints:

base[1] = 'R'
base[2] = 'G'
base[3] = 'Y'
base[0] = 'B' (from position4, which is index4 mod4=0, so base[0] = 'B').

So the base is B, R, G, Y.

Once the base is known, we can check all positions. For each '!' in the input, we can compute the mod4 of their position and get the expected color from the base pattern, then count the occurrences for each color.

So the problem reduces to determining the base pattern (the four elements in positions 0-3) that satisfy all the existing non-'!' characters in the input.

So how can we find this base pattern?

We can model this as follows:

We need to find a permutation of the four colors (R, B, Y, G) such that for every non-'!' character c in the input at position i, the base[i mod4] must be c.

So for each position in the input string, if the character is not '!', then base[i mod4] is fixed to that character. However, since the base must be a permutation of the four colors, there might be conflicting constraints. But the problem states that the input is valid, so there must be exactly one possible base pattern that fits all constraints.

Therefore, the steps are:

1. For each of the four positions in the base (0-3), collect the possible color constraints. If any of these positions has multiple different constraints, then the input is invalid, but according to the problem statement, the input is valid, so all constraints for each position must agree.

So, for each position in the input string where the character is not '!', we note the color and the mod4 position. For example, in the input "!RGYB", we have:

position1: R → mod4=1 → base[1] must be R.

position2: G → mod4=2 → base[2] must be G.

position3: Y → mod4=3 → base[3] must be Y.

position4: B → mod4=0 → base[0] must be B.

So for the four base positions, we can collect the required colors.

Once we have all the required colors for each of the four positions in the base, we can check if they form a permutation of the four colors. If they are, then that's our base. Otherwise, there's a problem, but the input is guaranteed to be valid.

Once the base is known, we can iterate through each character in the input. For each '!', we find which base position it corresponds to (i mod4) and increment the count for the base's color at that position.

So the plan is:

- Initialize a list for the base pattern of size 4, all initially None.

- Iterate over each character in the input string. For each i, if s[i] is not '!', then:

   mod_pos = i %4

   if base[mod_pos] is None: set base[mod_pos] to s[i]

   else: assert that base[mod_pos] is s[i], otherwise conflict (but problem says input is valid)

- Once all non-'!' characters are processed, check which positions in base are filled. The problem says that each color (R, B, Y, G) appears at least once in the input. So the base must have all four colors.

But if after processing the input, some positions in base are still None, we need to fill them with the missing colors.

Wait, this is possible. For example, suppose the input is "!!!!YGRB". Then the input has four '!' followed by Y G R B. Let's index the input as positions 0-7:

positions 0-3: '!'

position4: Y → mod4=0 → base[0] = Y

position5: G → mod4=1 → base[1] = G

position6: R → mod4=2 → base[2] = R

position7: B → mod4=3 → base[3] = B

So base is [Y, G, R, B]. But what about the first four positions (0-3) in the input? They are '!', so their positions mod4 are 0,1,2,3. So their colors would be base[0], base[1], base[2], base[3], which are Y, G, R, B. But the input has '!' in those positions. So those '!' would correspond to those colors.

But when processing the input, the non-'!' characters after position4 (positions4-7) give us the full base. So in this example, the base is filled completely.

Another example: input "!RGYB" (as before). The base positions are filled as:

base[0] = B (from position4 mod4=0), base[1] = R (position1), base[2] = G (position2), base[3] = Y (position3). So all four positions are filled.

But what if some positions in the base are not filled by the input's non-'!' characters? For example, suppose the input is "R!!!B!Y". Let's see:

Input: R ! ! ! B ! Y

Indices:

0: R → mod4=0 → base[0] = R

4: B → mod4=0 → base[0] must be B. But conflict here. So this can't happen. But the problem states that the input is valid, so such conflicts don't exist.

Wait, so the problem says that the input is a correct garland with some blown bulbs. So all non-'!' characters are in their correct positions. So the base can be determined uniquely.

So in the code, the steps are:

1. Collect all the constraints from the input's non-'!' characters. For each such character, set base[i mod4] to that character. Since the input is valid, all these constraints must agree.

2. Once the base is filled (some positions may be filled, others not), we need to find the missing colors.

Wait, but if some positions in the base are not filled, how to determine them? For example, suppose the input has some non-'!' characters, but after processing, the base has some positions filled, others not. Then, the missing positions must be the remaining colors, but in such a way that the base is a permutation of all four colors.

Wait, but the problem says that the input contains each of the four colors at least once. So the constraints must cover all four colors, but possibly some of them are in the base's positions.

Wait, no. The input has at least one of each color. So in the base, each color must appear exactly once. So the base is a permutation of the four colors.

So after collecting the constraints from the input's non-'!' characters, the base will have some positions filled. The remaining positions (those that are None) must be filled with the remaining colors. But since the base must be a permutation of all four colors, the remaining colors are those not present in the filled positions.

For example, suppose after processing the input, the base has positions 0, 1 filled with R and B. Then the remaining two positions must be Y and G, but in some order. How to determine which?

But the problem says that the input is a correct garland. So the base must be uniquely determined. So the constraints from the input must leave no ambiguity.

Hmm, this is a problem. How do we find the missing colors in the base when some positions are not filled by the input's constraints?

Wait, perhaps the input's non-'!' characters must cover all four colors. Because the problem states that the input has each of the four colors present. So the base must be a permutation of the four colors. Therefore, when building the base from the input's non-'!' characters, the filled positions must contain all four colors.

Wait, no. Because the input could have a non-'!' character in multiple positions that map to the same base position mod4. For example, if the input has R in position0 (mod4=0) and R in position4 (mod4=0), then the base[0] is R, but that would mean the base has R, and the other colors must be in the remaining positions. But how?

Wait, this can't happen because the input is a valid garland. So the base must have all four colors. So for example, if the input has R in position0 and position4 (mod4=0), then the base[0] is R. Then the other positions must be filled with the other three colors. But the input's non-'!' characters must also include at least one of each color. So in this case, other positions must have the other colors.

But in code, how can we find the missing colors? Let's think.

Suppose after processing all non-'!' characters, the base array has some positions filled. The colors present in these filled positions must be a subset of the four colors. The remaining colors (those not present in the filled positions) must be assigned to the remaining positions in the base.

But how to assign them correctly?

Wait, the problem says that the input is a valid garland, so the base is uniquely determined. So the remaining positions can be filled in only one possible way.

But how?

For example, suppose after processing the input, the base has:

base[0] = R

base[1] = B

base[2] = ?

base[3] = ?

So the remaining colors are Y and G. How to assign them to positions 2 and 3?

But how does the input's non-'!' characters affect this? Since the input must have at least one Y and G, but maybe they are in positions that mod4 to 0 or 1, which are already filled. Wait, but the problem states that the input has each of the four colors. So, for example, the input must have at least one Y and G, which would be in some positions. But their mod4 could be to any of the four positions.

So the code must fill the base array with the correct permutation of the four colors. So how to handle cases where some positions in the base are not filled by the input's non-'!' characters?

Let's take an example. Suppose the input is "R!!!B". Then the input is "R!!!B" (length 5). The non-'!' characters are at positions0 (R) and4 (B). So:

For position0 (mod0 → base[0] = R.

For position4 (mod0 → base[0] must be B. But this contradicts the previous assignment. So this input is invalid, but according to the problem statement, the input is valid. So such cases can't happen.

So the input will not have conflicting constraints.

Now, another example. Suppose the input is "R!!!Y". Then the non-'!' characters are R (position0 mod0 → base[0] = R), and Y (position4 mod0 → base[0] = Y. This is a conflict, so input is invalid. So again, such cases are impossible.

So, in code, the input will not have any such conflicts because it is guaranteed to be valid.

So, moving back. Suppose the input has non-'!' characters that fill some positions in the base. How to fill the remaining positions?

Suppose after processing the input, the base has some positions filled. The remaining positions must be filled with the remaining colors. But how?

Wait, the base is a permutation of the four colors. So the remaining colors are the ones not present in the base's filled positions.

But how to arrange them in the remaining positions?

Ah, perhaps there is only one possible permutation of the remaining colors that would make the entire base a valid permutation, given the filled positions. But how?

Alternatively, perhaps the base is determined uniquely by the filled positions. For example, if three positions are filled with R, B, Y, then the fourth must be G.

But how to find the order of the remaining colors?

Wait, perhaps the code can collect all the colors in the filled positions, then find the missing colors and assign them to the remaining positions in any order. But this would not work. Because the order must form a cyclic pattern such that consecutive four are all distinct.

Wait, but the problem states that the input is a valid garland, so the base must be a correct pattern, which implies that the base is a permutation of the four colors. So once the filled positions are known, the remaining positions must be filled with the missing colors. But since the order is a permutation, the code needs to find the missing colors and place them in the remaining positions.

Wait, but how? For example:

Suppose the filled positions are base[0] = R, base[1] = B, and base[2] = Y. Then the remaining color is G. So base[3] must be G.

Another example: filled positions are base[0] = R, base[1] = B. The remaining colors are Y and G. How to assign them to positions 2 and 3?

But how can the code know the correct order?

Wait, but the problem statement says that the input is a valid garland. So the base must be such that all the existing non-'!' characters are correct. So the code must find a permutation that satisfies the constraints from the input and is a valid cycle.

Wait, but perhaps the remaining positions can be filled in any order as long as they are the missing colors. But then there's ambiguity. However, the input's constraints may not allow this. But the problem says that the input is valid, which implies that the code can find a unique base.

Alternatively, perhaps the code can find the base by considering that the four colors must form a permutation, and the filled positions must be compatible.

Wait, perhaps the code can collect all the filled colors, then determine the missing colors and assign them to the remaining positions. But the order in which they are assigned may not matter as long as it forms a permutation. But how does that fit with the example?

Take for example the input "!GB!RG!Y!". Let's see the output expected is 2 1 1 0.

The input is "!GB!RG!Y!".

Let's index the input as 0-based:

0: '!'
1: G → mod4=1 → base[1] = G
2: B → mod4=2 → base[2] = B
3: '!'
4: R → mod4=0 → base[0] = R
5: G → mod4=1 → base[1] = G (already set)
6: '!'
7: Y → mod4=3 → base[3] = Y
8: '!'

So the filled positions are:

base[0] = R

base[1] = G

base[2] = B

base[3] = Y

So the base is R, G, B, Y.

Then, for each '!' in the input, we look at their positions mod4:

position0: mod0 → base[0] = R → count R's dead.

position3: mod3 → base[3] = Y → count Y's dead.

position6: mod6%4=2 → base[2] = B → count B's dead.

position8: mod8%4=0 → base[0] = R → count R's dead.

So the counts are R:2, B:1, Y:1, G:0. Which matches the sample output.

So the code must correctly reconstruct the base as R, G, B, Y.

But how was base[3] determined? Because position7 is Y, mod3 → base[3] is Y.

So the code in this case filled all base positions from the input's non-'!' characters.

Another example where some positions are not filled:

Suppose the input is "R!Y!" (length 4). The non-'!' characters are R at position0, Y at position2.

So:

position0 mod4=0 → base[0] = R.

position2 mod4=2 → base[2] = Y.

Now, the base has R and Y. The remaining colors are B and G. The base positions 1 and 3 are empty. So how to assign B and G to positions 1 and3?

But according to the problem, the input is valid. So there must be a unique way to assign these.

Wait, but how? Let's see. The input is R!Y! → the first four characters are R, !, Y, !. The base is R, ?, Y, ?.

The remaining colors are B and G. So the base must be R, B, Y, G, which is a valid permutation. Then, the garland would be R B Y G R B Y G ... But wait, the input is four characters, so positions 0-3. The non-'!' characters are R (0), Y (2). So base[0]=R, base[1] must be B (since the remaining colors are B and G), base[2]=Y, base[3]=G.

But how to decide between B and G for positions1 and3?

But the problem says that the input is valid, so the code must find the correct base. But in this case, the input's non-'!' characters don't cover all four colors. But according to the problem statement, the input contains at least one of each color. So this example is impossible, because the input must have all four colors present. So in this example, the input would have at least one B and G in the non-'!' positions. So the code must have enough information to fill all base positions.

Ah, right. The problem states that the input contains each of the four colors at least once. So the code can rely on the filled base positions to have all four colors. Therefore, when filling the base, the input's non-'!' characters will cover all four colors, so the base's filled positions will have all four colors. Because even if some positions are filled via mod4, the input must contain each color at least once, which implies that the base must have all four colors.

So, for example, the input must have at least one R, B, Y, G. So, in the code, the base array will have all four colors, either from filled positions (from the input's non-'!' characters) or inferred.

But how to infer the missing ones?

Wait, the code first collects all the non-'!' characters and fills the base positions. For each such character, it's added to the base array at position (i mod4). Once all non-'!' characters are processed, the code checks if the base array is filled completely. If yes, proceed. If not, the remaining colors must be the ones missing from the base, and the code must assign them to the remaining positions.

But how?

Wait, the code can collect the colors that are already present in the base. The remaining colors are the ones not present. Then, the code can assign the remaining colors to the remaining positions in the base array.

But the code has to assign them in some order. How?

Ah, but since the input is valid, there is only one possible way to assign the missing colors such that the base is a valid permutation. But how can the code determine that?

Alternatively, perhaps the code can find the missing colors and assign them to the remaining positions in any order. But since the input is valid, the code can't make a mistake here. Wait, but how?

Wait, perhaps the code can loop through the base array, and for each position that is None, assign it the next missing color. But how does that ensure the correct permutation?

Let's take an example where the input is "Y!!!G!B!R" (hypothetical example). Let's see:

Processing the non-'!' characters:

Y is at position0 → mod0 → base[0] = Y.

G is at position4 → mod0 → base[0] = G. Conflict? So this input is invalid, but according to the problem statement, it's not possible.

Another example where the code has to fill in the missing colors:

Input: "RBYG".

All characters are present. The base is R, B, Y, G.

Another example: input "R!Y!B".

Positions:

0: R → base[0] = R.

1: '!' → no info.

2: Y → base[2] = Y.

3: '!' → no info.

4: B → base[0] = B → conflict. So invalid.

But according to the problem statement, input is valid. So such a case can't exist.

So, the code can proceed as follows:

1. Initialize base as a list of four None elements.

2. For each index i in the input string:

   if s[i] is not '!', set base[i %4] to s[i], if it's not already set. If it's already set, check that it matches, else invalid (but input is valid, so this won't happen).

3. After processing all non-'!' characters, check if all four positions in base are filled. If yes, proceed.

4. If some positions are not filled, the remaining colors must be the ones not present in the base. So collect the missing colors and fill the remaining positions in the base.

But how to collect the missing colors and assign them to the remaining positions?

For example, suppose after processing, the base is [R, None, B, None]. Then the existing colors in base are R and B. Missing colors are Y and G. So the remaining positions (1 and3) must be filled with Y and G. But which order?

But the code must have enough information from the input to determine the correct order.

But how?

Ah! Because the input is a valid garland, the code can infer the correct order based on the existing characters. For example, if the input has other characters that must be in the remaining positions, but how?

Alternatively, perhaps the code can find the missing colors and assign them to the remaining positions in any order, as long as they form a permutation. But then, how to handle the case where the order matters?

Wait, but the problem states that the input is valid, so the code can rely on the existing non-'!' characters to uniquely determine the base. So if some positions are not filled, the code can infer them based on the existing filled positions and the four-color permutation.

But how?

Maybe the code can collect the colors present in the base (after step 2), then find the missing colors, and assign them to the remaining positions in any order, as long as the resulting base is a permutation of the four colors.

But then, how can the code know which order is correct?

The problem is that there are multiple possible permutations that fit the existing filled positions and the missing colors. However, the input is valid, so there must be only one possible way to fill the remaining positions such that the existing characters are correct.

But how?

Let's take an example where two positions are missing. Suppose the input has non-'!' characters that fill base[0] as R and base[1] as B. So the missing colors are Y and G. The code needs to assign them to positions 2 and 3.

But the code has no information about which order to assign them. So how can the code decide?

But according to the problem statement, the input is valid, which implies that the code must have enough information from the input to uniquely determine the base. So in this case, the code must have additional non-'!' characters in the input that fill in the other positions. For example, if there's a Y in a position with mod4=2, then base[2] is Y, and base[3] would be G.

So the code must have sufficient constraints to fill all four positions. But the problem statement says that the input may not have all four colors in non-'!' characters. Wait, no. The problem states that the input has each of the four colors present (as non-'!'), but the code could have multiple non-'!' characters of the same color. For example, the input may have two 'R's and one 'B', 'Y', 'G'.

Wait, but the problem says that the input has each of the four colors present at least once. So the code can assume that the filled positions in the base array cover all four colors. Because even if a color is only present once in the input, but in a position that mod4 is a certain value, that color is assigned to that base position.

So, the code can collect all four colors from the filled positions. Because the input has at least one of each color. So, the code can proceed as follows:

- After step 2 (processing all non-'!' characters), the base array has some positions filled.

- The filled positions must include all four colors. Because the input has at least one of each color, and each of those non-'!' characters must be assigned to their respective base positions.

Wait, yes. For example, suppose the input has a 'Y' in position5 (mod4=1). Then base[1] = Y. So the code's base array must have Y in position1. Similarly for other colors.

So the code's filled positions must include all four colors. So even if the input has a color in only one position, which mod4 is, say, 0, then base[0] is set to that color, and the remaining positions are filled with other colors.

But in this case, how to fill the remaining positions?

For example, suppose after step2, the base is:

base[0] = R

base[1] = B

base[2] = None

base[3] = None

But the code knows that the base must have all four colors. So the filled positions include R and B. The missing colors are Y and G. So the remaining positions (2 and3) must be filled with Y and G.

But how to assign them?

But according to the problem statement, the input is valid, so there must be a unique way to assign them. But how?

The code must not have any ambiguity here. Therefore, the input must have non-'!' characters that fill the remaining positions. But how?

This suggests that the code's step2 must have filled all four positions. Because if any positions are left unfilled, then the code can't know how to assign the remaining colors. But according to the problem statement, the input is valid, so the code can assume that the step2 must have filled all four positions.

But wait, suppose the input has a non-'!' character for each color, but those characters are assigned to base positions in such a way that the base is filled completely.

For example, input is "R!Y!B" (but this input is invalid because it has only three colors, but the problem states that all four are present. So this is not possible.

So, in code, the step2 will fill the base array with all four colors. Because each color is present in the input, and each of their positions mod4 will fill their respective base positions.

Wait, for example, the input has a 'G' in position7 → mod7%4=3 → base[3] = G.

So after processing all non-'!' characters, the base array will have all four colors.

Ah, so in code, after processing all non-'!' characters, the base array will have all four colors. Because each color is present in the input, and for each color, there must be at least one non-'!' character in some position whose mod4 is a certain value. So the code can rely on the base array being filled completely after processing all non-'!' characters.

Thus, the code does not need to handle the case where some base positions are None. Because the input's non-'!' characters cover all four colors, and thus fill all base positions.

Wait, that makes sense. Because each color is present in the input, and for each color, there is at least one non-'!' character in the input. Each of those characters must be assigned to their base positions (i mod4). So for each color, there's at least one base position filled with that color. But this doesn't directly imply that all four base positions are filled. For example, if all colors are in positions that mod4 to the same value, but that's impossible because then that base position would have multiple colors, which is a conflict. But since the input is valid, this can't happen.

So the code can assume that after step2, all four positions in the base array are filled.

Wait, for example:

Input is "RBYG" → the four characters are assigned to base[0], base[1], base[2], base[3]. So all filled.

Input is "RYBGGRB..." → but any non-'!' characters would fill their respective base positions. For example, if the input has R in positions0, 4, 8, etc. (mod0), B in positions1,5,9 (mod1), Y in position2, and G in position3. Then base is [R, B, Y, G].

So in code, after processing all non-'!' characters, the base array is completely filled.

Thus, the code can proceed to build the base array as follows:

- For each non-'!' character in the input, set base[i mod4] to that character. Since the input is valid, all such assignments are consistent and all four base positions are filled.

Once the base array is filled, the code can then count the '!' characters for each position in the input. For each '!', determine its position's mod4, look up the base array, and increment the count for that color.

So the steps in code are:

Read the input string.

Initialize base = [None, None, None, None].

For each index, char in the input:

   if char != '!':

       pos = index %4

       if base[pos] is None:

           base[pos] = char

       else:

           assert base[pos] == char  # since input is valid

Once this is done, the base array must be filled with four distinct characters (R, B, Y, G).

Then, count the number of '!' in the input for each color:

count_r = 0

count_b = 0

count_y = 0

count_g = 0

for index, char in enumerate(input):

   if char == '!':

       pos = index %4

       color = base[pos]

       increment the count for color.

Finally, output the counts in order R, B, Y, G.

So that's the plan.

Now, let's test this against the sample inputs.

Sample Input 2:

!RGYB

Processing:

Indices 0: '!', no action.

Index1: 'R' → mod1 → base[1] = R.

Index2: 'G' → mod2 → base[2] = G.

Index3: 'Y' → mod3 → base[3] = Y.

Index4: 'B' → mod0 → base[0] = B.

So base is [B, R, G, Y].

The '!' is at index0 → mod0 → base[0] = B. So dead count for B is 1.

Output is 0 1 0 0 → which matches the sample.

Sample Input 3:

!!!!YGRB

Indices 0-3: '!', no action.

Index4: Y → mod0 → base[0] = Y.

Index5: G → mod1 → base[1] = G.

Index6: R → mod2 → base[2] = R.

Index7: B → mod3 → base[3] = B.

Base is [Y, G, R, B].

The '!'s are indices0,1,2,3, which mod to 0,1,2,3. So their colors are Y, G, R, B. So each color has one dead bulb. Output is 1 1 1 1 → which matches.

Sample Input4:

!GB!RG!Y!

Input string: "!GB!RG!Y!"

Indices:

0: '!'

1: G → mod1 → base[1] = G.

2: B → mod2 → base[2] = B.

3: '!'

4: R → mod0 → base[0] = R.

5: G → mod1 → base[1] = G (already set).

6: '!'

7: Y → mod3 → base[3] = Y.

8: '!'

So base is [R, G, B, Y].

The '!'s are at indices0,3,6,8:

index0 → mod0 → R → count R +=1.

index3 → mod3 → Y → count Y +=1.

index6 → mod6%4=2 → B → count B +=1.

index8 → mod8%4=0 → R → count R +=1.

So total counts: R:2, B:1, Y:1, G:0 → which matches sample output.

So the code works for the samples.

Now, how to implement this in Python.

The code needs to:

1. Read the input string.

2. Initialize base as a list of four None's.

3. Iterate over each character in the input string. For each index i, if the character is not '!', compute i mod4. If base[mod] is None, set it. Else, assume it matches (since input is valid).

4. Once the base is filled, count for each '!' in the input: compute i mod4, get the color from base[mod], and increment the corresponding count.

5. Output the counts in order R, B, Y, G.

But how to order the counts? The output requires the order kr, kb, ky, kg, which is the counts of R, B, Y, G.

So in the code, we can have a dictionary that maps each color to its count. Then, output the counts in R, B, Y, G order.

So:

count = {'R':0, 'B':0, 'Y':0, 'G':0}

Then, for each '!' in the input, compute the color and increment count[color].

Then, print(count['R'], count['B'], count['Y'], count['G']).

So the code can be written as follows:

s = input().strip()

base = [None] *4

for i, c in enumerate(s):

    if c != '!':

        pos = i %4

        if base[pos] is None:

            base[pos] = c

        else:

            # since input is valid, no conflict

            assert base[pos] == c

count = {'R':0, 'B':0, 'Y':0, 'G':0}

for i, c in enumerate(s):

    if c == '!':

        pos = i %4

        color = base[pos]

        count[color] +=1

print(count['R'], count['B'], count['Y'], count['G'])

But what about the case where the base is not filled completely? According to the problem statement, the input is valid, so the base must be filled. So the code can proceed under the assumption that after the first loop, all base elements are filled.

Testing the code:

Sample Input 1:

RYBGRYBGR

All characters are non-'!', so base is filled as:

positions0 mod0 → R

position1 mod1 → Y → but wait, the input is "RYBGRYBGR".

Let's index the input:

0: R → mod0 → base[0] = R.

1: Y → mod1 → base[1] = Y.

2: B → mod2 → base[2] = B.

3: G → mod3 → base[3] = G.

So base is R, Y, B, G.

Then, no '!'s, so output is 0 0 0 0 → which matches sample.

But wait, according to the first sample's input, the output is 0 0 0 0, but according to the code's base, the colors are R, Y, B, G. Because the input is RYBGRYBGR.

But the code's base is filled as follows:

index0: R → mod0 → base[0] = R.

index1: Y → mod1 → base[1] = Y.

index2: B → mod2 → base[2] = B.

index3: G → mod3 → base[3] = G.

So for the input "RYBGRYBGR", which is R Y B G R Y B G R.

So the code's base is R, Y, B, G.

But the sample output is 0 0 0 0.

Yes, because there are no '!'s.

So the code works.

Another test case: input "!RGYB" → sample output 0 1 0 0.

The code's base after processing is:

index1: R → mod1 → base[1] = R.

index2: G → mod2 → base[2] = G.

index3: Y → mod3 → base[3] = Y.

index4: B → mod0 → base[0] = B.

So base is [B, R, G, Y].

Then, the '!' is at index0 → mod0 → B. So count B +=1. Output 0 1 0 0.

Correct.

Thus, the code should handle all cases correctly.

So this code should be correct.
</think>

```python
s = input().strip()
base = [None] * 4

for i, c in enumerate(s):
    if c != '!':
        pos = i % 4
        if base[pos] is None:
            base[pos] = c

count = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
for i, c in enumerate(s):
    if c == '!':
        pos = i % 4
        color = base[pos]
        count[color] += 1

print(count['R'], count['B'], count['Y'], count['G'])
```