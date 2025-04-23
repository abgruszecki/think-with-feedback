<think>
Okay, let's see. The problem is to represent a given number using the Soroban's rod representation. Each rod represents a digit from 0 to 9, and we need to output each rod's configuration in the order from the last digit (the rightmost one) to the first (leftmost). So for example, 720 is printed as three rods, each for 7, 2, 0, but the output is in the order 0, 2, 7, since the last digit is the top rod in the Soroban.

First, I need to process each digit of the input number in reverse order. For each digit, generate the corresponding Soroban representation.

Let's think about the structure of each rod's output. Each line has a fixed format. The Soroban's rod for a digit has five beads: one go-dama (the leftmost) and four ichi-damas. The reckoning bar is represented by |. The beads' positions are determined by the digit's value.

The algorithm to get the digit's representation is as follows:
- The digit's value is split into a 5 (from the go-dama) and the remainder from 0-4 (from the ichi-damas).
- For the go-dama: if the digit is 5 or more, then the go-dama is shifted to the right (so it's on the right side of the bar), otherwise it's on the left. But wait, the problem statement says: If the go-dama is shifted to the right, add 5. So for a digit d, if d >=5, then go-dama is on the right (so that 5 is added), and then the remaining is d-5, which is represented by the number of ichi-damas shifted left.

Wait, the way the digit is formed is:
- Start at 0.
- If go-dama is shifted right (so part of the right side of the bar), add 5.
- Then add the number of ichi-damas shifted to the left. The ichi-damas are the four beads. So shifted left means they are on the left of the bar? Or is it the other way around?

Wait, the problem says that the beads are arranged as per the Soroban's structure. The go-dama is the leftmost bead, then the bar, then the four ichi-damas? Or is the bar in between the go-dama and the ichi-damas? Let's look at the example.

In the first sample input, the output is O-|OO-OO. Let's parse that. The structure seems to be:

The first part is the go-dama: O followed by a -, then |. Then the ichi-damas. The sample input is 2. The digit is 2. So, since 2 <5, the go-dama is not shifted right. So the go-dama is on the left of the bar. Then the ichi-damas shifted left are 2. So how does that translate to the string?

The output line has parts: the go-dama's position, the bar, and then the ichi-damas. For the go-dama: if it's shifted to the right, then it's on the right side of the bar. So the go-dama's position is either left (O-) before the bar, or (| and then O) after?

Wait, the structure for each rod is divided into three parts: the go-dama part, the bar, and the ichi-damas. So the entire line is something like:

[Go-dama]-| [ichi-damas part]

Wait, the example for input 2 is O-|OO-OO. Let's break that down. The line is 9 characters long. Let's see:

Positions 0-3: O-|, then the next parts. Hmm, maybe the structure is as follows:

Each rod's line is made of:

- The go-dama part: either 'O' (shifted left) or '-' (shifted right?), then the bar as '|', then the four ichi-damas. But how are they arranged?

Wait, looking at the first sample input's output for digit 2. The digit is 2. Since it's less than 5, the go-dama is not shifted right. So the go-dama is on the left. The ichi-damas shifted left are 2. So the ichi-damas part would have two 'O's followed by two '-', but the output for ichi-damas part is OO-OO. Wait, that's OO-OO. So the four ichi-damas are split into two parts? Or maybe the ichi-damas are arranged as four positions, where those shifted to the left (towards the bar) are represented as 'O's, and those not shifted are '-'.

Wait, the problem statement says: add the number of ichi-damas shifted to the left. So for a digit d, after possibly subtracting 5 (if using go-dama), the remainder (0-4) is the number of ichi-damas shifted to the left. So, for example, if the remainder is 2, then two ichi-damas are shifted left. So in the ichi-damas part (four beads), how are they represented?

The four ichi-damas are arranged in some way. Let's think about the example for input 2. The output is O-|OO-OO. So after the bar (|), the ichi-damas part is OO-OO, which is four 'O's? Wait, no. Let's count: OO-OO is O O - O O. Wait, that's 5 characters. Wait, maybe the bar is a single |, and the rest of the line is divided into the go-dama part (before the bar) and the ichi-damas (after the bar).

Wait, the structure of each rod's line is as follows:

The first part is the go-dama. The go-dama is either on the left (O) or not (so it's moved to the right). Then comes the bar (|). Then the four ichi-damas are represented. 

But how are these parts arranged into the string? Let's look at the sample input 2's output: O-|OO-OO. Let's count the characters. The entire line is 9 characters. Let's break it down:

O - | O O - O O 

Wait, that's O-| followed by OO-OO. So the part after the bar is OO-OO. So the ichi-damas part is four beads, but how are they arranged? The four ichi-damas are split into two groups. Wait, maybe the ichi-damas are four beads arranged as four positions. For each ichi-dama, if it's shifted left, it's 'O'; otherwise, it's '-'. But in the sample input 2, the remainder is 2. So two of the four ichi-damas are shifted left. So the ichi-damas part would have two 'O's followed by two '-'? But the sample shows OO-OO, which is O O - O O, which is five characters, but the ichi part is after the bar. Hmm, maybe the four ichi-damas are split into one group of 4. Wait, perhaps the ichi-damas part is represented as a string where the leftmost ones are shifted. So for the remainder of r, the first r ichi-damas are shifted left (O's), and the remaining 4 - r are shifted right (represented as '-')?

Wait, let's think again. The problem says: add the number of ichi-damas shifted to the left. So the ichi-damas that are shifted to the left contribute to the digit. For example, if the remainder is 3, then 3 ichi-damas are shifted left (O's) and 1 is not (so '-').

But how is this represented in the output string? Let's look at the sample input 2's output. The ichi part is OO-OO, which is four 'O's. Wait, that's five characters. Wait, maybe I'm misunderstanding the structure. Let me re-examine the examples.

Sample Input 1:
2 → output O-|OO-OO

The digit is 2. Since it's less than 5, the go-dama is not shifted (so appears as O- on the left of the bar). The remainder is 2, so two ichi-damas are shifted left. So the ichi-damas part must have two 'O's and two '-'s. But the sample shows OO-OO. Wait, that's OO-OO, which is O O - O O. So after the bar, the part is OO-OO. That's 5 characters. Wait, maybe the ichi-damas are arranged as four beads, split into a group of 1 and 3? Or perhaps the format is that the four ichi-damas are split into two groups: one group of one and three, separated by a '-'. For example, in the sample, after the bar, it's OO-OO. So the first two are 'O's, then a '-', then two 'O's. But that sums to 2 + 1 + 2 =5 characters. Hmm, but the four ichi-damas should be four. So maybe this is a misunderstanding.

Alternatively, perhaps the ichi-damas part is written as four positions, but with a hyphen separating them. Wait, perhaps the four ichi-damas are represented as four characters, but the string has a '-' in between. For example, O-O-O-O for four beads. But that's 7 characters. Not sure.

Alternatively, maybe the four ichi-damas are represented in a particular way. Let's think about the sample input 720, which outputs three lines. The third line (for digit 7) is -O|OO-OO. Wait, that line's structure is: -O | OO-OO. So the go-dama part is -O. Wait, maybe the go-dama is the first character. So, for the go-dama's position: if the digit is >=5, the go-dama is shifted to the right (so the first part is '-O'?), but that's confusing.

Alternatively, perhaps the structure is as follows: each rod's line is split into three parts: the go-dama part, the bar, and the ichi-damas part. The go-dama part is either 'O' (if not shifted) or '-' (if shifted right). Then the bar is '|'. The ichi-damas part is arranged as four beads, but how?

Wait, perhaps the correct structure for each rod is:

The entire line is built as follows:

The go-dama is the leftmost bead. If it's shifted to the right (i.e., part of the 5), then the go-dama is on the right side of the bar. So the go-dama's representation is either before the bar (if not shifted) or after (if shifted). Wait, perhaps the go-dama is part of the left side of the bar if not shifted, and part of the right side if shifted. But how does that fit into the output line?

Looking at sample input 720's third line (the first digit 7):

The output is -O|OO-OO. So the line starts with -O, then |, then OO-OO. Wait, maybe the go-dama is represented as part of the left side. Hmm, I'm a bit confused here.

Let me re-examine the problem statement. The problem says:

Each rod is responsible for representing a single digit. The upper rod in the example shows digit 0. The output for 0 would be O-|---- (or something similar), but in the sample input 720, the first line (digit 0) is O-|-OOOO.

Wait, in the third sample input (720), the output is:

O-|-OOOO → represents 0

O-|OO-OO → represents 2

-O|OO-OO → represents 7.

So for 7, the digit is 7. Since 7 >=5, we subtract 5, getting 2. So the go-dama is shifted to the right (so contributes 5), and the ichi-damas contribute 2. So the go-dama is on the right side of the bar. How does that look in the output?

The line for 7 is -O|OO-OO. Wait, the part before the bar is '-O'? Or maybe the go-dama is represented as part of the left or right. Maybe the go-dama's position is indicated by whether it's on the left or right of the bar.

So the go-dama is a single bead. So in the output line, the go-dama is either on the left (O) or on the right (O). The bar is a |. The rest is the ichi-damas.

So for a digit d:

- If d >=5: go-dama is shifted to the right (so appears after the bar). So the line would start with '-', then the bar, then the O for the go-dama, followed by the ichi-damas.

Wait, but in the third line of sample input 720 (7's rod), the line is -O|OO-OO.

Breaking it down:

The part before the bar is '-O', then the bar, then OO-OO.

Wait, that's possible. Or perhaps the go-dama is represented as being on the right side of the bar. But then how is that shown in the string.

Alternatively, the structure of the line is:

Either:

O-|.... (go-dama on the left, not shifted)

Or:

-O|.... (go-dama on the right, shifted)

But then, how is that possible?

Wait, perhaps the go-dama is the first character. If it's shifted to the right (so contributes 5), then the first character is '-', and the go-dama is after the bar. But in the third sample line (-O|OO-OO), the part before the bar is '-O', which is two characters. That doesn't make sense. Maybe I'm missing something here.

Alternatively, maybe the first part is the go-dama's position. The go-dama is either in the left part (O-) followed by the bar. Or if it's shifted to the right, then the left part is '-', and the O is after the bar. But how?

Let's think of each line as:

[Left part] | [Right part]

The left part represents the go-dama's position. If the go-dama is shifted to the left (so not contributing 5), then the left part is 'O-'. If it's shifted to the right (contributing 5), then the left part is '-O'? But the sample input 720's third line is '-O|...', which would be the left part is '-O', then the bar. But that's two characters before the bar. So perhaps the left part is two characters. For example:

If the go-dama is on the left (not shifted), the left part is 'O-', followed by the bar. Then the right part is the ichi-damas.

If the go-dama is shifted to the right, the left part is '-O' (but how?), but that seems conflicting.

Wait, looking at the sample input 720's third line: the left part is '-O', then the bar, then OO-OO. Wait, that would imply that the go-dama is part of the left part but shifted? That seems confusing. Alternatively, maybe the go-dama is on the right side of the bar when shifted. So in that case, the left part is '-', and the bar is followed by 'O' and then the ichi-damas.

But the sample line shows '-O|...', which has O before the bar. So that's confusing.

Alternatively, perhaps the structure is as follows:

The left part is always two characters, and the go-dama is either in the left part or the right part.

Wait, perhaps the first two characters are for the go-dama. If the go-dama is not shifted (so not contributing 5), then the first character is 'O', followed by a '-'. Then comes the bar. For example, O-|...

If the go-dama is shifted to the right (so contributing 5), then the first two characters are '-O', followed by the bar. Then the ichi-damas. For example, -O|...

In the third sample line (digit 7, which is >=5), the line is -O|OO-OO. So the first two characters are '-O', indicating the go-dama is shifted to the right. Then the bar. Then the ichi-damas part.

So that makes sense. Then the ichi-damas part is after the bar, and for the remainder (d-5), which is 2 in this case, so two ichi-damas shifted to the left.

But how is the ichi-damas part structured? The sample's line for 7 has OO-OO after the bar. Let's see: OO-OO is four 'O's. But the remainder is 2, which would imply two 'O's followed by two '-'s. But that's not the case here.

Wait, maybe the ichi-damas are arranged in the four positions, but the way they are displayed is that shifted to the left (the ones that are contributing) are represented as 'O's, and those not shifted as '-'. But for the ichi-damas, the order is from left to right, so the leftmost positions are the ones shifted. For example, if the remainder is 2, then the first two ichi-damas are shifted left (O's), and the next two are not (so '-'). But how does that fit into the string structure.

Looking at the sample input 2's output line: O-|OO-OO. The ichi part is OO-OO. Breaking that down, after the bar, the part is OO-OO. Let's see: O O - O O. That's five characters, but four ichi-damas. Hmm, that doesn't add up. Wait, maybe the ichi-damas are split into a group of one and three? Or perhaps it's a typo and the correct output should be OOO- (for remainder 3?), but the sample seems to have OO-OO.

Alternatively, maybe the ichi-damas are represented as four separate positions, each represented by 'O' or '-', but the way they are printed is in two groups: the first group (of one) followed by a '-', then the next three. Wait, but that's just a guess.

Alternatively, the ichi-damas part is structured as "O" * (number of shifted) followed by "-" followed by "O" * (4 - number shifted). But that would be if there's some split. But how?

Alternatively, perhaps the four ichi-damas are divided into a top and bottom part, but that's unclear.

Alternatively, perhaps the ichi-damas part is four characters, each representing whether a bead is shifted. For example, for the remainder r, the first r are 'O's, and the rest are '-'. So for remainder 2: O O - - ? But how does that fit into the sample input 2's output where after the bar it's OO-OO. OO-OO is O O - O O, which is 5 characters. So maybe that's not the case.

Hmm, perhaps the problem statement's sample is wrong. Let's look at the sample input 2. The output is O-|OO-OO. Let's parse that:

The line is O-|OO-OO. The part after the bar is OO-OO. So that's four 'O's. But the digit is 2, which is the remainder (since 2 <5). So the remainder is 2. So how does OO-OO correspond to two shifted ichi-damas?

Wait, OO-OO is five characters. So perhaps the ichi-damas part is structured as two groups: the first group of two, then a '-', then another group of two. But then, how does that represent the remainder?

Alternatively, maybe the ichi-damas are four beads, and the way they are represented is that the beads shifted left are 'O's and the others are '-'. But the pattern is such that after the bar, the four beads are split into two parts: two on the left and two on the right, separated by a '-'.

So the format for the ichi part is two 'O's followed by '-' and then two 'O's. Wait, but that's OO-OO. But for a remainder of 2, two 'O's would be the shifted ones. So perhaps the first two positions (left of the '-') are shifted, and the next two (right of the '-') are not. But in that case, the ichi-damas part for a remainder of 2 would be O O - - -, but that's not matching the sample.

Alternatively, maybe the ichi part is structured as O's in the first r positions (counting from the left) and '-' in the remaining. But then how is that split into four beads.

Alternatively, perhaps the ichi-damas part is split into two parts: left and right of a '-', and each part represents a group. For example, the first part is the number of shifted beads in the first group (left of '-'), and the second part is the remaining beads. So for example, in the sample input 2, remainder is 2: so the first two beads are shifted left (O's) and the next two are not (so '-'), but the ichi part is OO-OO, which is OO followed by OO. That's four O's, but the remainder is 2. So that doesn't match.

This is getting confusing. Let's re-express the problem.

The ichi-damas are four beads. The number of shifted left is r. So the ichi part needs to show 'r' O's (shifted) and (4 - r) '-'s (not shifted). But how are these arranged in the output string.

Looking at the sample input 2's output line O-|OO-OO. The ichi part is OO-OO. That's OO-OO, which is five characters. So perhaps the ichi part is split into two groups of two beads, separated by a '-'. So the first two are the first group, then a '-', then the next two. So the structure is XX-XX. For example, in sample input 2, the remainder is 2. So two shifted beads. How would that be represented? If the first group is all shifted, then OO- --. But sample shows OO-OO. So maybe each group is a separate unit. But I'm not sure.

Alternatively, perhaps the ichi-damas part is split into two groups: the first group is one bead, then a '-', then three beads. But then again, the sample's output for ichi part is OO-OO. Hmm.

Alternatively, perhaps the ichi part is not directly split into groups, but the '-' is part of the rod's structure. For example, the four ichi-damas are arranged as O-O-O-O. Each bead is separated by a '-'. So for four beads, it's O-O-O-O (but that's 7 characters). But that doesn't fit the sample.

Alternatively, perhaps the ichi part is a string of four characters, each representing a bead. For example, 'OOOO' for all shifted, '----' for none. But then the sample input 2's ichi part is OO-OO, which is 5 characters. So that's not possible.

Wait, let's count the characters in the sample outputs.

Sample input 2's line is O-|OO-OO → 9 characters.

Breaking down:

O - | O O - O O → 9 characters.

So after the bar (|), there are five characters: OO-OO. That's 5 characters. So perhaps the ichi part is structured as two parts: two beads, then a '-', then two beads. So for the four ichi-damas, it's split into two groups of two, separated by a '-'. So the format is AA-BB, where AA and BB are each two beads. For each group, the number of 'O's depends on how many beads are shifted.

But how does this relate to the remainder r? For example, when r=2, how do we arrange the O's in AA and BB.

Wait, perhaps the ichi-damas part is split into two parts: left (two beads) and right (two beads). The left part is shifted if the beads are in that part. But this seems unclear.

Alternatively, the ichi part's structure is fixed: the first two beads are one group, then a '-', then the next two. For the remainder r, the number of O's in the left group plus the right group equals r. But how?

Alternatively, the ichi part is split into two groups. The left group has as many O's as the remainder, and the right group has (4 - r) O's. But that doesn't make sense. Because for example, in sample input 2, r=2, so left group would be 2 O's and the right group would be 2 O's. But that's OO-OO, which is the sample's output. So that seems to fit.

Wait, that's possible. So for the remainder r, the left group is r O's (left of the '-') and the right group is (4 - r) O's. Wait, but that would sum to 4 O's. Wait, but that's possible. For example, in sample input 2, r=2: left group is OO, right group is OO. So sum is 4 O's. But how does that represent the remainder 2?

This is conflicting. Because the remainder r is the number of shifted ichi-damas, which should equal r. But according to this structure, the number of O's is 4, not r.

Hmm, this suggests that perhaps my understanding of the problem is incorrect. Let's read the problem statement again.

Problem statement:

The value of a digit is:

0 + 5 (if go-dama is shifted to the right) + the number of ichi-damas shifted to the left.

Each rod has five beads: one go-dama and four ichi-damas.

So for a digit d:

If d >=5, then the go-dama is shifted right (so add 5). Then the remainder is d -5. Then add the number of ichi-damas shifted left (which is the remainder).

The ichi-damas are four beads. So for remainder r (0-4), exactly r of them are shifted to the left.

So how is this represented in the output?

The sample input 2's digit is 2 (r=2). The ichi part is OO-OO. So four O's, which would mean all four are shifted, but that would be r=4, not 2. So this is a contradiction.

Wait, this suggests that perhaps the ichi part's structure is such that the left side of the '-' represents the shifted beads, and the right side represents the unshifted. So for example, in the ichi part, the left group (before '-') is shifted, and the right group (after '-') is not. Then, the number of O's in the left group is the remainder r.

In sample input 2's case, r=2. So the left group (before '-') has two O's, and the right group (after '-') has two '-'s. But the sample's ichi part is OO-OO. So this would imply that both left and right groups are O's, which is conflicting.

Alternatively, perhaps the ichi part is structured as the shifted beads are on the right side of the '-' in the ichi part. So for example, the right side of the '-' is the shifted ones. But that's not clear.

Alternatively, perhaps the ichi part's '-' is part of the rod's structure, and each group represents a certain part. For example, the first part is the number of shifted beads (O's) and the second part is the unshifted ones (-). But how?

This is getting really stuck. Let's look for another sample. The third sample input is 720, and the third line (for 7) is -O|OO-OO. The remainder is 7-5=2. So the ichi part is OO-OO, which has four O's. But according to the problem statement, the remainder is 2, so two O's. So how does that fit?

This suggests that my understanding is wrong. So perhaps the ichi part is not directly the number of O's. Maybe it's the other way around: the number of '-' in the ichi part is the remainder. Or perhaps the beads that are shifted are represented by '-'.

Wait, no. The problem states that the ichi-damas shifted to the left are counted. So each shifted ichi-dama is represented by 'O', and unshifted by '-'.

So for remainder 2, two 'O's and two '-'s. But the sample shows OO-OO (four O's). So perhaps I'm missing something here.

Alternative approach: Let's think of each rod's line as follows:

The line is composed of the go-dama part, the bar, and the ichi-damas part. The go-dama part is either O- (if not shifted) or -O (if shifted). Then the ichi-damas part is four characters, which are a combination of O and -, representing shifted and unshifted beads.

But how?

Wait, the first sample input 2's output is O-|OO-OO. The ichi part is OO-OO. Which is four O's. So for remainder 2, the four ichi-damas are all shifted. But that's impossible. So there must be a misunderstanding.

Alternatively, perhaps the ichi part is structured as two groups: the first group is one bead, and the second group is three beads, separated by a '-'. For example, O-OOO. Then, the number of O's in the first group (0 or 1) plus the O's in the second group (0-3) equals the remainder.

So for remainder 2: 1 in the first group and 1 in the second group (total 2). So the ichi part would be O-OO-? Or O-O-O. Not sure.

Alternatively, the ichi part is split into four positions, each represented by a character. For example, O--- would mean one shifted, three unshifted. But in sample input 2's case, the remainder is 2. So the ichi part would be OO--. But the sample shows OO-OO.

Hmm. I'm stuck. Maybe looking for another sample would help. Let's look at the second sample input:

Input 13 → output two lines.

The output is:

O-|OOO-O → first rod (digit 3)

O-|O-OOO → second rod (digit 1)

So for the first line (digit 3):

digit 3 <5 → no go-dama shift. Remainder 3. So the ichi part is OOO-O. How does that correspond to 3?

The ichi part is OOO-O. So split into OOO (three O's) and O (one O). Total O's is 4. But remainder is 3. So this doesn't fit.

Alternatively, the ichi part is split into OOO-O → which is OOO-O. So three O's followed by a '-' and one O. That's four O's. So again, the remainder is 3, but four O's. So this suggests that my understanding is incorrect.

Alternative plan: maybe the ichi part is not directly representing the number of shifted beads. Perhaps the output is incorrect, but that's unlikely. So perhaps the structure is different.

Let's look for a pattern in the samples.

Sample Input 1 (digit 2) → output O-|OO-OO. The ichi part is OO-OO (four O's). So remainder is 2. So four O's. No obvious pattern.

Sample Input 2 (digit 3) → O-|OOO-O → ichi part OOO-O (four O's, one '-'). Remainder is 3. So again, four O's.

Sample Input 3 (digit 7) → ichi part OO-OO (four O's). Remainder 2. Again four O's.

Wait, perhaps the ichi part is always four O's. But that can't be, since the remainder varies. So this approach is not working.

Alternative Idea: Maybe the ichi part's '-' is not part of the beads. For example, the ichi part is four beads, represented as four O's. But then how to explain the '-' in the output.

Alternatively, perhaps the ichi part is structured as four beads, each represented as 'O' if not shifted and '-' if shifted. Or the other way around.

Wait, perhaps the ichi-damas shifted to the left are represented as 'O's, and the ones not shifted are '-'. So for remainder r, the ichi part has r 'O's and (4 -r) '-'s.

But then, how are these arranged?

For example, in sample input 2's case (r=2), the ichi part would have two 'O's and two '-'s. But the sample shows OO-OO (four 'O's). So this doesn't match.

Alternatively, perhaps the ichi-damas are split into two groups. For example, the first group is the ones that are shifted. So for remainder r, the first group has r beads as 'O's, followed by a '-', then the remaining (4 - r) beads as 'O's. But this also doesn't fit.

Alternatively, perhaps the ichi part's '-' is a fixed separator, and the O's are always present. But that doesn't make sense.

This is a problem. Maybe I need to find a pattern between the digits and their output lines.

Let's make a table of digits and their corresponding lines.

Sample 1:

Digit 0 → O-|-OOOO (from sample 3's first line). So ichi part is -OOOO. Wait, but the remainder is 0. So the ichi part should have 0 O's and 4 '-'s. But sample shows -OOOO. So this doesn't fit.

Sample 3's third line: digit 0's line is O-|-OOOO. The ichi part is -OOOO. Which is five characters. So perhaps the ichi part is structured with a '-' then four O's. So for remainder 0, the ichi part is - followed by four O's. But how does that relate to the remainder.

Alternatively, perhaps the ichi part's first character is '-', followed by four positions. But that's not helpful.

Alternatively, perhaps the ichi part's structure is such that all four ichi-damas are shifted to the left (O's) when the remainder is 0. But that's not possible.

Wait, perhaps the ichi part's structure is not related to the remainder. But that can't be the case.

Alternatively, perhaps the ichi part is always OOOO, but with some '-'s. Like, for example, in the first sample's ichi part, OO-OO, which is OO followed by OO. So four O's, split into two groups. But how does that relate to the remainder.

This is getting me stuck. Maybe I need to find a different approach. Let's think about how to generate the correct output for each digit.

For each digit d (0-9):

- The go-dama is shifted to the right if d >=5. So the left part is '-O' if shifted, 'O-' if not shifted.

Then, the remainder is d %5. For example, d=7 → 7-5=2.

The ichi part is then determined by the remainder. So for remainder r (0-4), we need to have r shifted ichi-damas (O's) and (4 - r) unshifted.

So the ichi part is four characters, with r O's and (4 - r) '-'s. But how are these arranged?

For example, remainder 0 → four '-': '----' → ichi part '----'.

Remainder 1 → 'O---' → but sample input 2's second line (digit 1) has ichi part O-OOO. Hmm, that's O-OOO, which is five characters. So perhaps the ichi part is structured as two parts separated by a '-'.

Wait, the sample input 13's second line is O-|O-OOO. The ichi part is O-OOO. So after the bar, it's O-OOO. Which is O-OOO (five characters). So the ichi part is O-OOO. How does this relate to remainder 1 (since digit 1 is <5, so remainder is 1).

But then, for remainder 1, the ichi part has 1 O. But O-OOO has four O's. So again, this doesn't make sense.

Hmm. Now I'm really stuck. Maybe I should look for another way to find the pattern.

Looking at the samples:

Sample 1 (digit 2):

O-|OO-OO → ichi part OO-OO (four O's). Remainder 2.

Sample 2 (digit 3):

O-|OOO-O → ichi part OOO-O (four O's). Remainder 3.

Sample 3 (digit 7):

-O|OO-OO → ichi part OO-OO (four O's). Remainder 2.

Sample 3's first line (digit 0):

O-|-OOOO → ichi part -OOOO. Remainder 0.

Hmm. For each remainder r, the ichi part has four O's, but the arrangement varies.

Wait, perhaps the ichi part is divided into two groups: the first group has r O's, then a '-', then the remaining (4 - r) O's. For example:

r=2 → OO-OO (four O's: 2 + 2).

r=3 → OOO-O (3 +1).

r=0 → -OOOO (0 +4).

r=1 → O-OOO (1 +3).

Ah, this seems to fit. So the ichi part is structured as follows: the left group is r O's, then a '-', then (4 - r) O's. So the total O's is r + (4 - r) =4. So the ichi part always has four O's, split into two groups separated by a '-'.

But how does that relate to the remainder? Because according to the problem statement, the remainder is added to the digit's value. For example, for remainder r, the ichi-damas shifted to the left contribute r. So why are all four O's in the ichi part?

This contradicts the problem statement. Unless there's a misunderstanding here. Because according to this, regardless of the remainder, all ichi-damas are shifted, which is impossible. But the problem states that the number of shifted ichi-damas is r.

So this suggests that the problem's explanation is different from the samples. Or perhaps the problem statement has a mistake. But the sample shows that for a remainder of 2, the ichi part has four O's. So perhaps the actual representation is that the number of O's in the left group before the '-' is r, and the right group after the '-' is 4 - r O's, but the beads are all shifted. But that doesn't make sense.

Alternatively, perhaps the problem statement's description is inverted. Maybe the ichi-damas that are shifted to the right are counted. Or perhaps the 'shifted to the left' means something different.

Alternatively, perhaps the ichi part's left group (before the '-') represents the number of unshifted beads, and the right group represents the shifted. Or vice versa.

But in the sample input 2's case (remainder 2), the left group has two O's and the right group has two O's. If that's the case, then the total shifted beads would be 2 (from the left group) or 2 (from the right group). Either way, it's unclear.

This seems to be a key point I'm missing. Without understanding the correct way to represent the ichi-damas, I can't proceed.

Let me try to find a pattern between the remainder and the ichi part's structure.

Let's create a table:

Digit | Remainder | Ichi part (after bar)
----- | --------- | ----------------------
0     | 0         | -OOOO
2     | 2         | OO-OO
3     | 3         | OOO-O
7 (r=2)|2         | OO-OO
1     |1          | O-OOO

Looking at these:

For remainder 0: left group is 0 O's, right group 4 O's → -OOOO.

For remainder 2: left group 2 O's, right group 2 O's → OO-OO.

For remainder 3: left group 3 O's, right group 1 O → OOO-O.

For remainder 1: left group 1 O, right group 3 O's → O-OOO.

So the pattern is:

The left group is the remainder r, and the right group is (4 - r) O's.

So the ichi part is composed of:

r O's + '-' + (4 - r) O's.

So for any remainder r (0-4), the ichi part is r O's, then a '-', then (4 - r) O's.

Thus, the ichi part is formed as follows:

ichis = 'O' * r + '-' + 'O' * (4 - r)

But why? According to the problem statement, the number of ichi-damas shifted to the left is added to the digit. So, if the remainder is r, there should be r O's in the ichi part. But according to this pattern, there are four O's in the ichi part for any r. That contradicts the problem statement.

But the samples show this pattern. So despite the problem statement's explanation, the ichi part is structured as left group (r O's) and right group (4-r O's), separated by a '-'. And the total O's is 4.

So, regardless of the remainder, the ichi part has four O's.

But according to the problem statement, the remainder should be the number of shifted beads. So this suggests that the problem's explanation is incorrect, or there's a misunderstanding.

But according to the samples, this is how it's structured. So perhaps the problem's way of counting the shifted beads is different. For example, the ichi-damas shifted to the right are counted, but the problem says shifted to the left. Or the left group is the number of beads not shifted.

Alternatively, maybe the ichi part's left group is the number of unshifted beads, and the right group is the shifted. But that would mean for remainder r, the right group has r beads. For example, in sample input 2 (r=2), the right group has 2 O's, which would be the shifted ones. But then the left group has 2 O's (unshifted?), which would imply that the remainder is 2, but there are 2 shifted beads (right group) and 2 unshifted (left group). That would sum to 2 shifted, which matches the remainder. So perhaps the right group represents the shifted beads.

But then, the ichi part's structure is:

left group (unshifted) + '-' + right group (shifted)

So, for a remainder r, the right group has r O's, and the left group has (4 - r) O's.

But in the sample input 2's case (r=2), the right group is 2 O's, so the remainder is 2. Which matches. Similarly:

Sample input 13's second line: O-|O-OOO. The remainder is 1. The right group is OOO → 3 O's. So this would imply r=3, but the digit is 1. So this doesn't fit.

Hmm. This approach also doesn't work.

Alternatively, perhaps the problem's description is wrong. Or perhaps the beads are arranged such that all four are shifted, and the remainder is represented by their positions.

But I'm not making progress here. To proceed, perhaps I should model the code based on the samples, regardless of the problem statement's description.

The pattern seems to be:

For each digit d:

If d >=5, then the go-dama is shifted (left part is '-O'), else 'O-'.

The remainder is r = d %5.

The ichi part is formed as 'O' * r + '-' + 'O' * (4 - r).

So for d=0: 0%5=0 → 'OOOO' → but sample shows -OOOO. Wait, no. For d=0, the remainder is 0. So the ichi part would be '0 O's followed by '-' and 4 O's → '-OOOO', which matches the sample.

So the code can be written as:

For each digit in reversed order:

1. Determine if go-dama is shifted (d >=5 → shifted).

   - If shifted: left_part is '-O' → then remainder is d-5.

   - else: left_part is 'O-' → remainder is d.

2. The ichi part is formed by:

   ichi_part = 'O' * remainder + '-' + 'O' * (4 - remainder)

3. The line is left_part + '|' + ichi_part

Wait, wait. Let's test this for sample input 2:

d=2 → not shifted. left_part 'O-'. remainder 2. ichi_part 'OO' + '-' + 'OO' → 'OO-OO'. So line is O-|OO-OO → matches sample.

Sample input 13's first line is digit 3. remainder 3. ichi_part 'OOO' + '-' + 'O' → 'OOO-O'. Line is O-|OOO-O → matches sample.

Sample input 720's third line is digit 7. shifted, so left_part '-O'. remainder 7-5=2. ichi_part 'OO-OO'. line is -O|OO-OO → matches sample.

Sample input 0's line is O-|-OOOO. digit 0: not shifted. remainder 0. ichi_part 'OOOO' becomes 'OOOO'? No. Wait, according to this logic, the remainder is 0, so ichi_part is 'O'*0 + '-' + 'O'*4 → '-OOOO', which matches the sample.

Yes! So this is the correct pattern. So the ichi part is built by:

ichis = 'O'*r + '-' + 'O'*(4-r)

Thus, the code should generate each rod's line as follows:

For a digit d:

left_part is 'O-' if d <5 else '-O'

remainder = d %5

ichis = 'O'*remainder + '-' + 'O'*(4-remainder)

line = left_part + '|' + ichis

Yes! This explains all the samples.

So now, the code can be written.

The steps are:

1. Read the input number n.

2. Convert n to a string, then reverse it (since we need to process digits from last to first).

3. For each digit in this reversed string:

   a. Convert to integer d.

   b. Determine left_part:

      if d >=5 → '-O'

      else → 'O-'

   c. remainder = d %5

   d. ichi_part = 'O'*remainder + '-' + 'O'*(4 - remainder)

   e. Combine left_part + '|' + ichi_part → print this line.

Edge Cases:

- n=0 → output one line: 'O-|-OOOO'.

- digits with d=5: remainder 0 → ichi_part is '-OOOO'.

Examples:

Digit 5 → left_part '-O', remainder 0 → line is -O|-OOOO.

Yes.

So this logic works.

Now, the code can be written.

But wait, how to handle the input.

The input is a single integer n, which can be 0. So, the code should process each digit of n as a string, even if it's zero.

For example, if n=0 → digits is ['0'].

If n is 720 → digits in reverse order are ['0', '2', '7'] → which in the output is printed as three lines.

So the steps are:

Read the input as a string, to avoid leading zeros being stripped.

But the problem says: "decimal representation of number n without leading zeroes". So for n=0, output one rod.

Thus, the code can be written as:

n = input().strip()

if n == '0':

   process as 0.

else:

   digits = list(n[::-1])

For each digit in digits:

   process as per the steps.

But in Python, for example, for input 13 → digits after reversing are '31' → so first line is 3, second line is 1.

Thus, the code would generate the correct output.

Thus, the code would:

Read the input as a string.

Reverse it, then iterate over each character, converting to integer.

For each digit d:

   left_part = 'O-' if d <5 else '-O'

   remainder = d %5

   ichi_part = 'O'*remainder + '-' + 'O'*(4 - remainder)

   print(left_part + '|' + ichi_part)

Now, let's test this code.

Test case 1: input 2 → output O-|OO-OO. Correct.

Test case 2: input 13 → digits are 3 and 1 (reversed). So first line for 3: O-|OOO-O. Second line for 1: O-|O-OOO. Which matches the sample.

Test case 3: input 720 → digits are 0, 2,7 (reversed). So:

For 0: O-| + remainder 0 → O-| - OOOO (O-|-OOOO). Correct.

For 2: O-|OO-OO. Correct.

For 7: 7 >=5 → left_part '-O', remainder 2 → ichi_part OO-OO. So line -O|OO-OO. Which matches the sample.

Yes.

Now, handle leading zeros. But according to the problem statement, the input n has no leading zeros. So the code can safely process the input as a string, reversed.

Thus, the code should be:

Read the input as a string.

Iterate over each character in the reversed string.

For each character, convert to int.

Then generate the line as above.

Thus, the code is:

n = input().strip()

for c in reversed(n):

    d = int(c)

    if d >=5:

        left = '-O'

    else:

        left = 'O-'

    r = d %5

    ichi = 'O'*r + '-' + 'O'*(4 - r)

    print(left + '|' + ichi)

Yes, this should work.

Testing with sample input 0:

input is '0' → reversed is '0'.

d=0 → O-.

r=0 → ichi is 'OOOO' → but no, according to the code:

r=0 → 'O'*0 → '', then '-', then 'O'*(4-0) → 'OOOO' → so ichi is '-OOOO'.

Thus, line is O-| + '-OOOO' → O-|-OOOO. Correct.

Another test case: digit 5 → left is '-O', remainder 0 → ichi is '-OOOO'. line is -O|-OOOO.

Yes.

Another test case: digit 9 → 9 >=5 → left is '-O', remainder 4. ichi is 'OOOO-' + 'O'*(4-4=0) → 'OOOO-' + 'O'*0 → 'OOOO-'. Wait, no. Wait, r=9-5=4. 'O'*4 → 'OOOO', then '-', then 'O'*0 → ''. So ichi_part is 'OOOO-'. No. Wait, no. Wait, code is 'O'*r + '-' + 'O'*(4 -r).

For r=4: 'O'*4 is 'OOOO', then '-', then 'O'*(0) → ''. So ichi_part is 'OOOO-' + '' → 'OOOO-'? Wait, no. 'O'*4 is 'OOOO', then '-', then 'O'*(0) is ''. So ichi_part is 'OOOO-' + '' → 'OOOO-'. But the sample for digit 9 would have ichi_part 'OOOO-', which is 5 characters. But in the code, the line for digit 9 would be '-O|OOOO-' → which is 9 characters (left_part is 2, | is 1, ichi_part is 5: total 8).

Wait, no. Let me count:

left_part is 2 characters ( '-O' ), then | is 1 character, then ichi_part is 5 characters. So total 2+1+5=8 characters. But sample input 2's line is 9 characters. Hmm, perhaps there's a mistake here.

Wait, in the first sample, the line is O-|OO-OO. Which is 2+1+5=8 characters. Oh wait, 2 (O-), 1 (|), 5 (OO-OO) → 8 characters. But the sample input 2's output shows O-|OO-OO as 9 characters. But perhaps I'm miscounting.

O-|OO-OO → O - | O O - O O → which is 9 characters. So why?

Wait, each part:

left_part is 'O-' → 2 characters.

| is 1.

ichi_part is 'OO-OO' → 5 characters.

Total 2+1+5=8. But O-|OO-OO is 9 characters. So there's a discrepancy here.

Ah, I see. The code may have a mistake.

Wait, let's count:

For example, in the first sample's line:

O-|OO-OO → characters are:

O - | O O - O O → 9 characters.

So the code must generate a line with 9 characters.

But according to the code:

left_part is 2 characters, then | (1), then ichi_part (5) → total 8. But the sample shows 9.

Ah, so there's a mistake. How can this be?

Wait, perhaps the code is missing a '-' in the left_part.

Wait, for d <5, left_part is 'O-' (two characters). For d >=5, left_part is '-O' (two characters). Then the bar is | (one character). Then the ichi_part is 'O'*r + '-' + 'O'*(4-r) → which is (r) +1 + (4-r) =5 characters. So total 2+1+5=8 characters. But the sample input 2's line has 9 characters.

So there's a problem here.

Wait, the sample input 2's line is O-|OO-OO → 9 characters. So how is this possible?

Let me count again:

O - | O O - O O → that's O (1), - (2), | (3), O (4), O (5), - (6), O (7), O (8). Wait, no. The string is O-|OO-OO. Let's write each character:

Index 0: O

Index 1: -

Index 2: |

Index 3: O

Index 4: O

Index 5: -

Index 6: O

Index 7: O

So total 8 characters. But sample input 2's output shows O-|OO-OO. Which is 8 characters, not 9. But the sample input's output shows it as a single line of 9 characters. Maybe the sample is formatted with a newline, but the actual length is 8.

But according to the problem's first sample input:

Input 2 → output O-|OO-OO.

The output is 8 characters. But perhaps I'm miscounting.

Wait, let's type it out:

O-|OO-OO → letters:

O, -, |, O, O, -, O, O → 8 characters.

Yes. So the code is correct. The sample's output has 8 characters, not 9. So the code is correct.

Thus, the code generates each line as 8 characters.

So the code is correct.

Thus, the code should work.
</think>

```python
n = input().strip()
for c in reversed(n):
    d = int(c)
    left = 'O-' if d < 5 else '-O'
    r = d % 5
    ichi = 'O' * r + '-' + 'O' * (4 - r)
    print(f"{left}|{ichi}")
```