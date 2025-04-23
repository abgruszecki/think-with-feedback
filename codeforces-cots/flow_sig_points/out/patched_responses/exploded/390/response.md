<think>
Okay, let's tackle this problem. The goal is to find the maximum length of a good string that can be formed by concatenating some subset of the given a, b, and ab strings. The constraints are big—up to 1e9 for each, so any solution that isn't O(1) is probably going to be too slow. So I need to think of a mathematical approach here.

First, let's understand the problem. The good string has to alternate between a and b, no two same consecutive letters. When we concatenate the provided strings (which are "a", "b", "ab"), the order in which we place them must result in a good string. So each concatenation must not introduce consecutive same characters at the boundaries between the strings.

The "a" and "b" strings are single characters. The "ab" strings are two characters, which are already a good string of length 2. But when we put these together, the way they are arranged can affect the overall validity.

Let me think about how each of these components can fit into the final string. Let's break down the possible combinations.

First, the "ab" strings. Each "ab" contributes two characters. However, if we place two "ab" strings in a row, the last character of the first is 'b' and the first of the next is 'a', which is okay. But wait, that's allowed. Wait, no: "abab" is a good string. So multiple "ab" can be placed next to each other. For example, "ababab" is valid. So perhaps using all c "ab" strings is possible, but only if their arrangement doesn't create consecutive same characters. But since each "ab" starts with 'a' and ends with 'b', placing another "ab" after it would start with 'a', which is different from the previous 'b', so it's allowed. So the entire c "ab" strings can be concatenated together to form a string of length 2*c. However, combining these with other strings (a, b) may or may not be possible.

But wait, the problem allows us to arrange the strings in any order. So the "a" and "b" strings are single-character strings. However, when placing them adjacent to other strings, their single character must not create consecutive duplicates with the adjacent string's first or last character.

So for example, if we have a single "a" string followed by another "a" string, that's invalid. But a single "a" followed by "ab" is okay because the first "a" ends with 'a', and the next string starts with 'a'? Wait, no. Wait, the single "a" is a string of just 'a', so when concatenated with "ab", which starts with 'a', the combined string would have 'a' followed by 'a', which is invalid. So that's not allowed.

So the key challenge is to arrange the given strings in a way that the end of one string and the start of the next do not have the same character.

Hmm. So the problem reduces to arranging the available strings (a, b, ab) such that the transitions between them are valid, and then maximizing the total length.

But the available strings are:

- "a" (length 1, ends with 'a')
- "b" (length 1, ends with 'b')
- "ab" (length 2, starts with 'a', ends with 'b')

Similarly, "ab" starts with 'a' and ends with 'b'. So when you place an "ab" string, the next string must start with something other than 'b' (the end of the previous is 'b').

Wait, no. Wait, the next string's first character can't be the same as the previous string's last character. For example, if the previous string ends with 'b', the next string must start with 'a' or something else. But since the next string can only start with 'a' or 'b' (since all are made up of a and b), the next string's first character must not be 'b'.

So for example, after an "ab" (ends with 'b'), the next string can be "a" (starts with 'a'), or "ab" (starts with 'a'), but not a "b" (starts with 'b') or "ba" (but we don't have "ba" strings here).

Wait, but the "ab" strings are fixed. So the problem is that when we arrange the given strings, each consecutive pair must not have conflicting start and end characters.

So the problem is to find an ordering of the strings (each being "a", "b", or "ab") such that:

- For any two consecutive strings s1 and s2, the last character of s1 is different from the first character of s2.

And we need to maximize the total length.

But how can we model this? It's a bit complex because the order and the selection of strings matter.

Let me think about possible scenarios.

First, the "ab" strings. Each "ab" contributes two characters. If we use them all, that's 2*c. But the problem is that using them might prevent us from using some of the a and b strings.

Alternatively, maybe combining "ab" strings with a and b strings can yield a longer total length.

But how?

Another idea: the "ab" strings can be placed in a sequence, as they each end with 'b' and start with 'a'. So a sequence of c "ab" strings would start with 'a' and end with 'b', and each subsequent "ab" starts with 'a' (so the previous 'b' ends with 'b', then 'a' starts next, which is okay). So that's allowed. So the total for "ab" is 2*c.

But then, can we add any a or b strings around this?

For example, after the sequence of "ab" strings (which ends with 'b'), we can add a single "a" string. But that's allowed since the previous ends with 'b' and the next starts with 'a'. So adding one 'a' would contribute 1.

Similarly, before the sequence of "ab" strings (which starts with 'a'), we can add a single 'b' string, as that starts with 'b' and ends with 'b'. Wait, but then the sequence would start with 'b' followed by 'a' (from the first "ab"). That's allowed.

Wait, the sequence would be 'b' (from the 'b' string) followed by 'a' from the first "ab". So that's allowed.

So perhaps the optimal approach is to:

1. Use as many "ab" strings as possible, and then add some a and/or b strings to the ends if possible.

But how to determine how many a and b can be added.

Alternatively, perhaps the maximum is achieved by either:

a) Using all c "ab" strings, plus as many a and b as possible in a way that doesn't conflict.

b) Using some a and b strings, and then some "ab" strings, but this might not be better.

Wait, but the "ab" strings contribute two characters each. So using them is more efficient than using an 'a' and 'b' string each (since each of those contributes one character but uses two counts). Wait, but maybe not. Let's see: for each "ab" string, we get two characters. But using one "a" and one "b" gives two characters as well (assuming they can be arranged as 'ab' or 'ba'). However, the problem allows using a subset, so perhaps using "ab" is better when possible.

But perhaps the optimal strategy involves a combination of the "ab" strings and the a and b strings. So how to model this?

Alternatively, maybe the solution is to compute two possibilities:

1. Use all c "ab" strings, then see how many a and b can be added to the ends.

2. Not use all c "ab" strings, but arrange a and b strings in a way that allows more total length.

But this seems complicated.

Alternatively, perhaps the best approach is to model the problem as two separate cases:

Case 1: The final string starts with 'a' (and alternates).

Case 2: The final string starts with 'b' (and alternates).

Then, for each case, compute the maximum possible length.

But even this might not cover all possibilities. However, perhaps considering both cases and taking the maximum would give the optimal answer.

But how?

Alternatively, let's think of the "ab" strings as a separate component, and then model the rest.

Another approach is to note that the "ab" strings can be placed in the middle of the sequence, but this requires that their ends fit.

But perhaps the main challenge is handling the transitions between the different types of strings.

Alternatively, perhaps the "ab" strings can be arranged in a way that allows maximum utilization of a and b.

Wait, let's think of the "ab" strings as a group. Suppose we have all c of them. Then, their combined form is a string that starts with 'a' and ends with 'b' (since each "ab" starts with 'a' and ends with 'b'). So the entire group of c "ab" strings will start with 'a' and end with 'b'. So before this group, we can place a 'b' string (if available). After this group, we can place an 'a' string (if available).

But the 'b' string placed before the group starts with 'b', which is the same as the previous character (since the group starts with 'a'? Wait, no. If the group is placed after the 'b' string, then the 'b' string is followed by the first 'a' of the group. So that's allowed. For example, "b" followed by "abab..." gives "b a b a..." which is valid.

So adding a 'b' at the beginning and an 'a' at the end could add two more characters.

But how many can we add?

Wait, the group of c "ab" strings forms a string like ababab... (if c is 3, then ababab). So starts with a, ends with b.

So if I put a 'b' string before this, the sequence would be 'b' followed by 'a' (from the first 'ab'), which is allowed. Then, the total length for this part is 1 (from 'b') + 2*c (from 'ab's).

Then, after the 'ab's, which end with 'b', I can add an 'a' string. So that's another 1. So total is 1 + 2c +1 = 2c+2.

But this requires that a and b each have at least one available.

Alternatively, if there's a 'b' string but no 'a' after, then maybe adding just the 'b' at the beginning and 2c.

Similarly, if there's an 'a' at the end but no 'b' at the beginning, then add that.

So perhaps the maximum possible when using all c "ab" strings is 2c plus the number of a and b that can be added at the ends (but considering that each can be added at most once).

So, after using all c "ab" strings, we can add up to 1 'a' at the end and 1 'b' at the beginning, but only if available.

So the maximum possible after using all c "ab" is:

max_ab_case = 2*c + min(a, 1) (if we can add 'a' at the end) + min(b, 1) (if we can add 'b' at the beginning).

But wait, the 'a' added at the end must be available. So if a >=1, then add 1. Similarly for 'b' at the beginning.

So this would add 0, 1, or 2 to 2c, depending on a and b.

But maybe this is the way to calculate the contribution from the "ab" strings plus possible a and b.

But then there's another possibility: perhaps the 'ab' strings are not used, and instead, we arrange a and b in some way. But in that case, the maximum possible is the same as the maximum possible alternated a and b, which is min( a + b +1, 2*min(a, b) +1 if one is larger, but wait, no. The maximum possible when arranging a and b is a + b, but only if they can be arranged in a way that alternates. For example, if a and b are equal, then a + b. If one is larger by more than one, then it's 2*min(a, b) +1.

But wait, let's see. For example, a=3, b=5. The maximum possible is 2*3 +1 =7. Because arrange as bababab, which uses 5 b's and 3 a's, but the a's are placed between the b's. Wait, no. Wait, if a=3 and b=5, the maximum length would be 2*3 +1 =7 (since you can have a b followed by a, then b, then a, then b, then a, then b, then b. Wait, no. Wait, consecutive b's would break the rule. So the maximum possible is when the counts differ by at most one. So if a and b are the same, then a + b. If one is larger than the other by more than one, then the maximum is 2*min(a, b)+1. Wait, maybe the standard problem of maximum alternated string.

So the maximum possible from a and b is:

if |a - b| <=1: a + b

else: 2*min(a, b) +1.

So this is the case when we only use a and b strings. But in our problem, we also have ab strings.

So the total maximum is the maximum between:

1. The sum from using all ab strings plus possible a and b.

2. The sum from using a and b, plus possible ab.

But how to combine them.

Alternatively, perhaps the optimal solution is the maximum between:

a) The sum when all ab are used plus some a and b.

b) The sum when some ab are used, along with some a and b.

But this seems complicated.

Another approach: the presence of the ab strings can allow us to use more a and b strings.

Alternatively, perhaps using the ab strings can help in bridging between a and b strings.

But I'm getting stuck here. Let's think of the examples.

First example:

Input is 1 1 1. So a=1, b=1, c=1.

The optimal output is 4. The solution is "baba". How is this formed? Well, the "ab" string is "ab", then we add a 'b' at the beginning and 'a' at the end. So total is 1 (from 'b') + 2 (from 'ab') +1 (from 'a') =4.

So in this case, all c=1 ab strings are used, plus one a and one b.

Another example:

Input is 2 1 2. Output is 7.

The optimal string is "abababa". How is that formed? The two ab strings contribute 4, but perhaps they are arranged as abab (4 characters), then adding another a and b. Wait, but how. Wait, the example says the output is 7. So 2 ab's (each contributes 2, total 4) plus 3 more characters, but how.

Wait the input is a=2, b=1, c=2. So the example's output is 7. So perhaps the way to arrange is: abababa (length 7). How is that formed? Let's see. The "ab" strings are two in number, which would form abab (length 4). But then the remaining a is 2, but maybe the arrangement is a single a, then abab. But that would be a followed by a, which is invalid.

Wait, perhaps the solution is to interleave the a's and ab's. For example, "a" followed by "ab" (a + ab gives aab, which starts with 'a', then 'a' again, which is invalid. So that's not allowed.

Alternatively, perhaps the two ab's are arranged as abab (4), then after that, add a, then ab. But no, that would be abab a ab, which ends with b, then a, then a. So invalid.

Wait maybe the correct arrangement is ababab a. Wait that's three ab's, but the input is c=2. Oh, the example's input is a=2, b=1, c=2. So the solution uses all two ab's (4 characters), plus three a's and one b. Wait, but how.

Wait the output is 7. So 2 ab's (4) + 3 from a and b: 7. But a is 2, b is 1, so sum is 3. But how to arrange them.

Wait, maybe the solution is "abababa", which is a sequence of a, b, a, b, a, b, a. But how to form that with the given strings.

Alternatively, the arrangement could be "ab" followed by "ab" (4 characters: abab), then followed by "a" (from a's, which is 1 character), then "b" (but b is 1). But that would be abab a b (length 6), which is 6. Not enough.

Hmm. Let's look at the example's note. The optimal string is "abababa". So it's a sequence of a, b, a, b, a, b, a. That's 7 characters. So how is this formed using a=2, b=1, c=2.

Wait, the "ab" strings contribute to a and b counts. Each "ab" is a separate string, so two "ab" strings would contribute two a's and two b's. But the a and b strings are separate. So in total:

The two "ab" strings use up two a's and two b's. But the input a is 2, b is 1. So that's impossible. Because using two "ab" strings would require two a's and two b's, but the input has a=2, but b=1. So that's not possible.

Wait, this suggests that the example's note is wrong, which can't be. So I must have misunderstood the problem.

Wait, wait, no. The problem states that a, b, c are the numbers of "a", "b", and "ab" strings. So each "a" string is a single 'a', each "b" is a single 'b', and each "ab" is a single 'ab' (two characters). So the counts for a and b in the input are the numbers of these individual strings, not the counts of a and b characters. So in the example with a=2, b=1, c=2, the total a characters from the "a" strings is 2, and the "ab" strings contribute 2 a's (each has one a) and 2 b's (each has one b). So the total a characters available from all sources is 2 (from a strings) + 2 (from ab strings) =4. Similarly, the total b characters from all sources is 1 (from b strings) +2 (from ab strings) =3. But wait, no. Because each "ab" string is a string of two characters, but when we use the "ab" string, we are using it as a whole. So when we select to use an "ab" string, it contributes exactly one 'a' and one 'b' in that order. So the total a and b counts in the final string are the sum from the selected "a", "b", and "ab" strings.

But the problem is to arrange these strings in a way that the concatenation forms a good string, which requires that the transitions between the strings are valid.

So for example, if you have a string "a" (from the a strings) followed by an "ab" string (which starts with 'a'), then the concatenation is "aab", which is invalid because the 'a's are consecutive.

So the problem is not about the total a's and b's, but about the way the strings are arranged. So even if the sum of a and ab's a's is large, you can't use them all if their arrangement causes consecutive same characters.

So the example with a=2, b=1, c=2. The output is 7. How is this achieved?

The arrangement is "abababa". Let's see how this is formed. The string is 7 characters long.

Possible breakdown into the given strings:

"ab" (from c=2) strings are two in number. Then, there's a "a" string (from a=2) and a "b" string (from b=1). But how to arrange them.

Wait, the "ab" strings are two in number. So if you concatenate them, you get "abab" (length 4). Then, the remaining a and b strings are a=2 and b=1. But the problem is that after the "abab" (ends with 'b'), you can add a "a" string (starts with 'a'), but that would result in 'b' followed by 'a' (valid), adding 1. Then, after that, can you add another 'a'? No, because the previous string ends with 'a', and adding another 'a' would start with 'a' (invalid). So maybe the arrangement is to place the "a" string before the "ab" strings.

Alternatively, perhaps the arrangement is to place the two "ab" strings, then the "a" and "b" strings in some order. But that seems tricky.

Alternatively, perhaps the arrangement is to use the "a" string first. But then the "ab" strings can't follow because the 'a' ends with 'a' and the "ab" starts with 'a'.

Wait, the example's note says that the optimal string is "abababa". Let's see:

a b a b a b a → 7 characters. Let's break this into the given strings.

Each "ab" string is two characters. So two "ab" strings would give a b a b. Then, the remaining parts are a, b, a.

But how to get those from the remaining a and b strings. The a strings are 2, and b is 1.

Hmm. Let's see:

The two "ab" strings contribute 'abab' (length 4). Then, add a 'a' (from a=2) → but that gives 'abab a' which is 'ababa', ends with 'a'. Then, adding 'b' (from b=1) → 'ababa b' (ends with 'b'). Then, adding another 'a' (from a=2) → 'ababa b a' (ends with 'a'). So the total length is 4 +1 +1 +1 =7.

But the transitions between the strings:

After the two "ab" strings (ends with 'b'), adding 'a' is allowed (starts with 'a') → no conflict.

Then, the 'a' string ends with 'a', next is 'b' (starts with 'b') → conflict. So 'a' followed by 'b' would create 'ab', but the 'a' ends with 'a', and the 'b' starts with 'b' → no conflict. Wait, no. Wait, the 'a' string is a single 'a', ends with 'a'. The 'b' string is a single 'b', starts with 'b'. So concatenating them gives 'ab' → which is allowed. So the transition between 'a' and 'b' is allowed.

So the sequence would be:

ab (from c) → ab (from c) → a (from a) → b (from b) → a (from a). 

So the transitions are:

ab (ends with 'b') → next ab starts with 'a' → allowed.

ab ends with 'b', next ab starts with 'a' → allowed.

Then, the last ab is followed by 'a' → starts with 'a' → 'b' followed by 'a' → allowed.

Then, 'a' ends with 'a' → followed by 'b' (starts with 'b') → allowed.

Then, 'b' ends with 'b' → followed by 'a' → allowed.

So this sequence is valid.

So the total usage is 2 "ab" (c=2), 2 a's (a=2), 1 b (b=1). So all are used. So total length is 2*2 (from ab) + 2*1 (from a) +1*1 (from b) = 4+2+1=7. Which matches the example.

So in this case, the arrangement is ab + ab + a + b + a. But how is this allowed? Because after the two ab's (ends with 'b'), adding 'a' is allowed. Then the 'a' is followed by 'b' (allowed), then 'a' again (allowed since the previous 'b' ends with 'b' and the next 'a' starts with 'a').

So the key here is that after the ab's, we can arrange a and b in a way that alternates, using up the available a's and b's.

But how to model this in code?

Perhaps the way to model this is to consider two cases:

Case 1: We use all c "ab" strings.

Case 2: We use c-1 "ab" strings.

Wait, but why?

Alternatively, after using all c "ab" strings, the maximum a and b that can be added is a + b, but only if they can be arranged in a way that starts with a character that follows the 'b' end of the "ab" group.

So, after the "ab" group, the end is 'b'. So the next string must start with 'a'. So any a strings can be added here (but they are single 'a's, so after adding an 'a' string, the next string must start with 'b', which could be a 'b' string or an 'ab' string. But we've already used all 'ab' strings.

So, after the "ab" group, we can add a sequence of a and b strings, but they must alternate. However, since we are adding a and b strings, each is a single character. So the maximum possible here is the same as the maximum alternating sequence of a and b counts, given that the first character must be 'a' (since the previous end is 'b').

So the maximum number of characters added after the "ab" group is the maximum possible for a and b, starting with 'a'.

Which is:

if a_remaining == 0 and b_remaining ==0: 0

else:

start with 'a' (if available), then alternate.

So the maximum is:

max_a_b_after_ab = 0

if a_remaining >=1:

then, the sequence starts with 'a', and then alternates. So the maximum is 1 + min( a_remaining-1, b_remaining ) * 2 + (1 if (b_remaining - (a_remaining-1)) >0 else 0 )

Wait, this is similar to the standard problem.

Wait, the maximum possible sequence starting with 'a' (given x a's and y b's) is:

if x ==0: 0

else:

start with 'a', then alternate. So the maximum is 1 + 2*min(x-1, y) + (1 if (y > x-1) else 0) if (y >= x-1) else 1 + 2*y.

Wait, perhaps the formula is:

if x >= y +1: then 2*y +1

else: 2*min(x, y) +1 if x != y else 2*x.

Wait, no. Let me think again. For example:

x=3, y=3: can be a b a b a b a → length 7 (x=4? No, no. Wait, x is 3, so can't have 4 a's. Wait, perhaps the formula for maximum sequence starting with 'a' is:

max_length = 0

if a_available ==0: 0

else:

max_length = 1 + min(a_available -1, b_available) * 2 + min(b_available - (a_available -1), 1) if (b_available >= a_available -1) else (a_available + b_available) if (a_available <= b_available +1) else 2*b_available +1 )

Hmm, this is getting complicated. Maybe there's a simpler way.

Alternatively, the maximum possible length starting with 'a' is:

if a_available ==0: 0

else:

max_length = min( a_available + b_available, 2 * min(a_available, b_available +1 ) + ( (a_available - (b_available +1)) >0 ? 1 : 0 ) )

Wait, perhaps it's easier to model this as:

We start with 'a', then alternate. Each 'a' after the first must be preceded by a 'b'. So the maximum number of a's is min( a_available, b_available + 1 ). And the number of b's is min( b_available, a_available ).

So the total is min( a_available, b_available +1 ) + min( b_available, a_available )

Wait, for example, a=3, b=5:

min(3,5+1) →3. min(5,3) →3. Sum 6. But the actual maximum is 3+3=6 (e.g., ababab → 6 letters). But the example in the problem says that a=3, b=5, c=2 gives a total of 11. Which is 3+5+ 2*2= 3+5+4=12? Wait, no. Wait, the output is 11. So perhaps the a and b are arranged as 5+3+ 2*2= 5+3=8 +4=12. That doesn't add up. Wait, the third example's input is a=3, b=5, c=2. The output is 11. The note says the optimal string is "bababababab" → which is 11 characters. So how is this formed?

Breaking it down:

The string is "bababababab" → which is 11 characters. This is all 'b's and 'a's in alternating order. So the counts are 6 'b's and 5 'a's. But the input has a=3, which is the number of 'a' strings, and b=5 'b' strings. So where do the 5 a's come from? Because the 'ab' strings contribute 2 a's (since c=2). So total a's: 3 (from a) + 2 (from ab) =5. Total b's:5 (from b) +2 (from ab) =7. But the string uses 5 a's and 6 b's. So this suggests that the solution uses all the a's (3) and all the ab's (2), and all the b's (5). But the ab's contribute 2 a's and 2 b's, and the a's contribute 3, and the b's contribute 5. So total a's 5 and b's 7. The arrangement uses 5 a's and 6 b's. So the problem is that the "ab" strings are being used, but their arrangement allows the remaining a's and b's to be used in a way that forms a longer string.

So the solution in this case is to use the two "ab" strings (which contribute 4 characters) and then arrange the a's and b's (3+5=8) into a longer alternating string.

But how? Because the 'ab' strings must be arranged in a way that allows their use.

Alternatively, perhaps the two "ab" strings are not used in this case, and the maximum is achieved by using a and b strings. Let's see:

The maximum possible for a=3+2=5 (from a's and ab's) and b=5+2=7 is:

if we use all a and b's, but arrange them as bababababab (11 characters). This uses 5 a's and 6 b's. So how does that fit with the counts? The a's from a strings (3) plus ab's (2) sum to 5, which is sufficient. The b's from b strings (5) plus ab's (2) sum to 7. So this is possible.

But how are the strings arranged? The two "ab" strings would contribute their a's and b's, but the arrangement must be such that the concatenation of the strings is valid.

This is getting complicated. Perhaps the key insight is that using "ab" strings can contribute to the a and b counts, but their arrangement is crucial.

But given the time constraints, perhaps the optimal approach is to model the problem as follows:

Compute the maximum possible length when using all possible "ab" strings, and then see how many a and b can be added before and after. Also, compute the maximum possible when not using all "ab" strings. Take the maximum of all possibilities.

But how to model this.

Let's think of two scenarios:

1. Use all c "ab" strings. Then, the maximum possible additional length from a and b is the maximum sequence that can be formed starting with 'a' (after the "ab" group ends with 'b') and ending with any character, given the remaining a and b.

But after the "ab" group ends with 'b', the next string must start with 'a'. So the possible a and b strings must form a sequence that starts with 'a', and alternates.

In this case, the remaining a is a_remaining = a_initial, and remaining b is b_initial. But no, because when we use the "ab" strings, each contributes to the a and b counts. Wait, no. The "ab" strings are separate entities. The a and b strings are separate. So when we use a "ab" string, we are using that string, not individual a and b characters.

Wait, this is the key misunderstanding. Each "ab" string is a single string "ab". So when we use it in the concatenation, it contributes exactly the characters 'a' followed by 'b'. So the transitions between the "ab" strings and other strings must be considered. The 'ab' strings themselves do not use up the a and b counts. The a and b counts are separate.

Wait, no. Wait, the problem statement says that you have a number of "a" strings (each is "a"), "b" strings (each is "b"), and "ab" strings (each is "ab"). So when you select to use an "ab" string, it counts towards the c count. The a and b counts are separate. So the a and b counts are the number of "a" and "b" strings available. The "ab" strings do not affect the a and b counts.

So for example, if you have a=1, b=1, c=1, you can use all three strings: "a", "b", "ab". But when you concatenate them, you need to arrange them so that the transitions are valid. For example, "a" followed by "ab" would give "aab", which is invalid. So you can't do that. But in the first example, the optimal solution is "baba", which is formed by "b", "ab", "a" → transitions are 'b' → 'a' (valid), 'b' → 'a' (valid), and 'a' → 'a' (invalid). Wait, no. Wait, "b" followed by "ab" is "b ab" → "bab". Then followed by "a" would be "bab a", which has a 'b' followed by 'a' (valid), but the 'a' is followed by nothing. So the concatenated string is "baba", which is valid. Because each consecutive pair is 'b' and 'a', then 'a' and 'b', then 'b' and 'a'. All valid.

So the "ab" string in this case contributes two characters, but does not use up any of the a or b counts. The a and b counts are separate.

So the problem is not about the total a and b characters, but about the number of "a", "b", and "ab" strings selected and their arrangement.

So the a, b, and c counts are the number of each type of string that can be used. The arrangement must be such that the transitions between the selected strings are valid.

So the challenge is to select a subset of these strings (each of type "a", "b", or "ab") and arrange them in a way that every two consecutive strings s1 and s2 have s1's last character different from s2's first character. The goal is to maximize the sum of the lengths of the selected strings.

So the total length is sum of the lengths of the selected strings (each "a" is 1, "b" is 1, "ab" is 2).

The problem is to select a subset and arrange them in such a way that the transitions are valid, and the total length is maximized.

Ah, this changes everything. So the a, b, and c are the numbers of each type of string. So for example, each "a" string is just 'a', each "b" is 'b', and each "ab" is 'ab'.

So when selecting the strings, you can use some a's, some b's, and some ab's, but their order must be such that consecutive strings don't have conflicting first and last characters.

This makes the problem more complex.

So the problem is to choose a sequence of strings (each from the a's, b's, or ab's) such that:

- For any i>1, the last character of the (i-1)-th string is not equal to the first character of the i-th string.

The goal is to maximize the sum of their lengths.

Now, the problem is to model this selection and arrangement.

This is a different problem than previously thought. So how to approach this?

The first step is to think about what's possible.

Each "a" string starts and ends with 'a'.

Each "b" string starts and ends with 'b'.

Each "ab" string starts with 'a' and ends with 'b'.

So the key is to find an order of these strings such that the last character of each string is different from the first character of the next.

We need to maximize the total length, which is the sum of the lengths of the selected strings.

So for example, if we have a lot of "ab" strings, using them all could be beneficial as each contributes 2 to the total length.

But we can only use them if they can be arranged in a way that the transitions are valid.

For example, "ab" followed by "ab" is valid, because the first ends with 'b', the next starts with 'a'.

Similarly, "ab" followed by "a" is invalid, as the next string starts with 'a', which is the same as the previous's end.

But "ab" followed by "b" is invalid (previous ends with 'b', next starts with 'b').

But "ab" followed by "ab" is valid.

So a sequence of all "ab" strings is possible, and contributes 2*c length.

But then, can we add other strings after this sequence?

The sequence of "ab" strings ends with 'b'.

So the next string must start with 'a'.

So possible candidates are "a" strings, or "ab" strings (but we have already used all c of them), or maybe "ba" strings (but we don't have any).

So after the sequence of "ab" strings, we can add an "a" string, provided that there's one left.

But after adding an "a" string (which ends with 'a'), we can add a string that starts with 'b' (e.g., "b" or "ab" again, but if we have no more "ab" strings, then "b" is possible).

So after the "ab" sequence and an "a" string, we can add a "b" string, then another "a", and so on, as long as transitions are valid.

But this is getting complicated. So perhaps the optimal solution involves using as many "ab" strings as possible, and then appending as many a and b strings as possible in a way that transitions are valid.

Similarly, it's possible to interleave "ab" strings with other strings.

But how to model all possibilities.

An alternative approach is to consider that the "ab" strings are very efficient (each contributes 2 characters), and they can be arranged in a sequence, so we should use as many as possible.

But after that, we can add a and/or b strings to the beginning or end.

So let's think of the "ab" strings as forming a block. The block starts with 'a' and ends with 'b', and has length 2*c.

Then, we can consider adding other strings before or after this block.

Before the block: possible to add a "b" string (which ends with 'b'), then the block starts with 'a' → valid.

After the block: possible to add an "a" string (starts with 'a') → invalid (block ends with 'b'), or a "b" string → invalid. Wait, the block ends with 'b', so after it can only add a string that starts with 'a'.

So after the block, we can add "a" strings or "ab" strings. But "ab" strings are already used. So after the block, we can add "a" strings, but each "a" string starts with 'a' (so the previous 'b' ends, which is allowed), but each "a" string ends with 'a', so the next string must start with 'b'. So we can have an "a" string followed by a "b" string, and so on.

But the number of "a" and "b" strings available is a and b.

So the maximum number of additional characters after the "ab" block is the maximum alternating sequence starting with 'a' and using the remaining a and b strings.

But how to compute this.

Let me think: the block ends with 'b'. So the next string must start with 'a'. So possible options are:

- "a" strings: each starts with 'a'.

- "ab" strings: but they are already used.

So the first string after the block must be an "a" string. But using an "a" string adds a single 'a', which ends with 'a'. Then the next string must start with 'b', which can be a "b" string. Then after that, starts with 'b' → must start with 'a', which could be another "a" string, and so on.

So after the block, the sequence would be a series of "a" and "b" strings in alternating order, starting with "a" and ending with either "a" or "b".

The maximum number of such strings is determined by the standard problem of maximum alternating sequence, but with the initial character being 'a'.

So the maximum number of characters added after the block is the same as the maximum length of a valid string formed by the a and b strings, starting with 'a'.

This can be computed as follows:

max_after = 0

if a_available >=1:

max_after += 1  # first "a" string

a_available -=1

then, the remaining a and b strings can be arranged in a way that alternates between 'b' and 'a' starts. But since each "b" string starts with 'b', after the first "a", the next must be a "b" string, then an "a", etc.

So the maximum is:

max_after += 2 * min(a_available, b_available)  # each pair of a and b contributes 2 characters.

if a_available > b_available:  # after using all b's, there are a_available - b_available a's left. Can we add one more a?

But no, because after the last 'b' string (ends with 'b'), adding an 'a' string (starts with 'a') is allowed, adding 1.

Similarly, if b_available > a_available, then after using all a's, there are b_available - a_available b's. But after the last 'a' string (ends with 'a'), adding a 'b' string is allowed, adding 1.

So the total after the first a is:

2 * min(a_available, b_available) + (1 if (a_available > b_available) or (b_available > a_available) else 0)

Wait, but this is only if after the first a, there are enough b's.

Alternatively:

Once the first a is used, the remaining a and b strings must alternate starting with b.

So for the remaining a_available and b_available:

The number of pairs is min(a_available, b_available). For each pair, one a and one b are used, adding 2 characters.

Then, if there are more a_available than b_available, we can add one more a (since after the last b, which ends with 'b', adding an a is allowed).

If there are more b_available than a_available, then after the last a, we can add one b.

So the formula becomes:

max_after = 1 + 2 * min(a_available, b_available) + (1 if (abs(a_available - b_available) >=1) else 0)

Wait, but this is only if the first a is used.

For example, a_available =2, b_available=1:

After using first a, remaining a=1, b=1.

Pairs: min(1,1)=1 → add 2. Then, a and b are both zero. So total is 1+2=3.

Another example: a=3, b=1.

After first a: a=2, b=1.

Pairs: 1 → add 2. Now a=1, b=0.

Since a is larger by 1, add one more a (starts with a, but previous string is 'b', ends with 'b' → allowed. So add 1. Total is 1+2+1=4.

So formula:

after_first_a = 1 + 2 * min(a_available-1, b_available) + (1 if (a_available-1) > b_available else 0) if (a_available >=1) else 0.

But perhaps a better way is:

after_ab_block = 0

if a >=1:

    after_ab_block +=1  # use one a

    remaining_a = a-1

    remaining_b = b

    pairs = min(remaining_a, remaining_b)

    after_ab_block += 2 * pairs

    remaining_a -= pairs

    remaining_b -= pairs

    if remaining_a >0:

        after_ab_block +=1  # add one more a

    elif remaining_b >0:

        after_ab_block +=1  # add one more b

So total after_ab_block is:

after_ab_block = 1 + 2*min(a-1, b) + (1 if (a-1 > b) or (b > a-1) else 0 )

But not sure.

Alternatively, after using one a:

The next string must be b, then a, then b, etc.

So the total number of additional characters after the first a is:

number of a's after the first: a_available = a-1

number of b's: b_available = b

The maximum possible is 2*min(a_available, b_available) + (1 if (a_available != b_available) else 0 )

But this depends on which is larger.

For example, a_available=3, b_available=2:

min(3,2)=2 → 2*2=4.

Then, a_available - min=1, b_available - min=0.

So we can add one a → 4+1=5. But how? The sequence would be a (1) + (b + a) *2 → 1+2*2=5.

Yes.

So the formula is:

after_first_a = 1 + 2*min(a_available-1, b_available) + (1 if (a_available-1) > b_available else 0) + (1 if (b_available > (a_available-1)) else 0 )

Wait, no. Because if (a_available-1) > b_available: after using all b_available in pairs, there are (a_available-1 - b_available) a's left. So can add one a (since after the last pair is a b, ends with b, next a is allowed. So +1.

If (b_available) > (a_available-1): after pairs, there are (b_available - (a_available-1)) b's left. Can add one b after the last a (ends with a, so adding b is allowed. So +1.

But in this case, the remaining b's are not part of the pairs, but after the pairs. So after the pairs, the last string is a, which ends with a. So adding a b string is allowed. So yes.

So after the first a, the maximum is:

min(a-1, b) *2 + 1 (for the first a) + 1 if either a-1 > b or b > a-1.

But wait, if a-1 and b are equal, then there's no extra. So the total after first a is 1 + 2 * min(a-1, b) + (1 if (a-1 != b) else 0).

So the after_ab_block contribution is:

if a >=1:

    possible_after = 1 + 2 * min(a-1, b) + (1 if (a-1 != b) else 0)

else:

    0

But how to model this.

But also, before the "ab" block, we can add a "b" string.

The "ab" block starts with 'a', so the previous string must end with 'b' or 'a' (depending on what's before).

Wait, the "ab" block's first string is 'a' (since each "ab" string starts with 'a'), so if there is a string before the block, it must end with 'b' to allow the 'a' start.

So before the block, we can add a "b" string. That starts with 'b' and ends with 'b'. Then the block starts with 'a' → allowed.

So adding a "b" string before the block contributes 1 character, and allows the block to be added.

After the block, we can add the after_ab_block contribution as discussed.

So the total contribution from using all c "ab" strings plus some a and b before and after is:

max_case1 = 0

if c >0:

    # add possible 'b' before the block

    pre_b = 0

    if b >=1:

        pre_b =1

    # add the block of c "ab" strings → 2*c

    # add possible 'a' and more after.

    post_a = after_ab_block(a, b - (pre_b), c)

    max_case1 = pre_b + 2*c + post_a

else:

    # c=0, so no "ab" block. So we need to consider just a and b.

    # handled elsewhere.

But I'm getting stuck on how to model all possibilities.

Alternatively, perhaps the optimal solution is to consider several cases:

1. The "ab" strings are used in a block. Then, we can add a "b" before and/or an "a" after.

2. The "ab" strings are not used in a block, but interleaved with a and b strings.

But this seems too broad.

Alternatively, the maximum possible length is the maximum of:

a) All "ab" strings (2*c) plus the maximum of adding a "b" before and/or an "a" after, along with any remaining a and b strings that can be arranged.

b) Not using all "ab" strings, but using some of them in a way that allows more a and b strings to be used.

But case b is likely to be negligible compared to case a, especially when c is large.

But for small c, perhaps it's better to use some "ab" strings and arrange others.

But how to model this.

An alternative idea is that the optimal solution can be found by considering the maximum of:

- Using all "ab" strings, and then adding as many a and b as possible before and after.

- Using all "ab" strings except one, and arranging the remaining "ab" strings and a and b in a way that allows longer sequences.

But this may not be feasible given the time constraints.

But given that the maximum input is up to 1e9, any algorithm must be O(1), so it must involve mathematical calculations.

So let's try to model case a) using all "ab" strings.

Case a: using all c "ab" strings.

The "ab" block has start 'a' and end 'b'.

We can try to add a "b" string before the block (if available), which starts and ends with 'b'. Then, the block starts with 'a' → valid.

Then, after the block, add an "a" string (if available), which starts with 'a' (previous end 'b' → valid).

Then, after that, add as many a and b strings as possible in alternating order.

So the steps are:

pre_b: 1 if b >=1 → subtract 1 from b.

block: 2*c.

post_a: 1 if a >=1 → subtract 1 from a.

remaining_a = a - post_a.

remaining_b = b - pre_b.

Then, after the block and post_a, add the maximum possible sequence of a and b strings, starting with 'a' (since the previous end is 'a' from the post_a string).

Wait, no. The post_a string is an "a" string, which ends with 'a'. So after that, the next string must start with 'b'.

So after post_a, the remaining a and b strings must be arranged in a way that starts with 'b'.

But after the block, if we added post_a, then the remaining a and b are (a-1, b - pre_b).

So after post_a, the sequence would need to start with 'b' strings.

So the maximum possible after post_a is the maximum possible sequence starting with 'b', using the remaining a and b.

But this is getting complicated.

Alternatively, perhaps the maximum possible after the block is:

max_after_block = 0

if a >=1:

    max_after_block +=1  # add "a" string

    a_remaining = a-1

    # now, after this "a" string (ends with 'a'), next must start with 'b'

    # the maximum sequence starting with 'b' and using a_remaining and b_remaining = b - pre_b.

    if (b_remaining := b - pre_b) >=1:

        max_after_block +=1  # add "b" string

        b_remaining -=1

        # now, alternate between a and b.

        pairs = min(a_remaining, b_remaining)

        max_after_block += 2*pairs

        a_remaining -= pairs

        b_remaining -= pairs

        if a_remaining >0 or b_remaining >0:

            # no more possible, since after the last pair, the next string would need to start with 'a' or 'b' but none left.

    else:

        # no more can be added.

So this is getting too detailed.

Perhaps the optimal way is to consider the following possibilities for the case where we use all c "ab" strings:

- We can add a "b" before the block.

- We can add an "a" after the block.

- We can add both.

- We can add neither.

For each of these possibilities, compute the maximum possible additional a and b strings that can be added, and take the maximum.

So let's model this.

Case 1: Use all c "ab" strings.

Option 1: Add a "b" before, and an "a" after.

But adding a "b" before requires b >=1.

Adding an "a" after requires a >=1.

Then, after the "a", we can add as many a and b strings as possible, starting with 'b' (since "a" ends with 'a').

Option 2: Add a "b" before, but no "a" after.

Then, after the block, we can add as many a and b strings as possible starting with 'a' (block ends with 'b').

Option 3: Add an "a" after, but no "b" before.

Then, after the block and "a", add as many a and b strings as possible starting with 'b'.

Option 4: Add neither.

Then, after the block, add as many a and b as possible starting with 'a' (since block ends with 'b').

For each of these options, compute the maximum possible total length.

Then, take the maximum among all options.

But how to compute this.

Let me think:

For option 1:

pre_b = 1 (if b >=1).

post_a = 1 (if a >=1).

Then, after the post_a, we have a_remaining = a - post_a = a-1.

b_remaining = b - pre_b = b-1.

The remaining a and b can be arranged as:

After the post_a (ends with 'a'), the next string must start with 'b'.

So the maximum possible after that is:

max_after = 0

if b_remaining >=1:

    max_after +=1  # add "b"

    b_remaining -=1

    # then, alternate between a and b.

    pairs = min(a_remaining, b_remaining)

    max_after += 2 * pairs

    a_remaining -= pairs

    b_remaining -= pairs

    # if any remaining a or b, can add one more.

    if a_remaining >0:

        # after last b (ends with 'b'), add a → allowed.

        max_after +=1

    elif b_remaining >0:

        # after last a (ends with 'a'), add b → allowed.

        max_after +=1

So the total for option1 is:

pre_b + 2*c + post_a + max_after.

But this is very complex. Perhaps there's a smarter way.

Given the time constraints, perhaps the optimal solution is to compute several possible scenarios and take the maximum.

The scenarios to consider are:

1. Using all c "ab" strings.

   a. Then, add as many a and b as possible around them.

2. Not using all c "ab" strings, perhaps using c-1, and see if that allows more a and/or b to be used.

But this may not be feasible.

Alternatively, the maximum possible length is the maximum of:

- The case where all c "ab" are used, plus possible a and b before and after.

- The case where no "ab" strings are used, and we arrange a and b to form the longest possible string.

- The case where some "ab" strings are used, but not all.

But considering the time constraints, perhaps the first case is the dominant one.

So let's focus on the case where all c "ab" are used.

In this case, the maximum possible additional length is:

pre_b (0 or 1) + post_a (0 or 1) + the maximum possible from the remaining a and b, arranged after considering the pre and post additions.

But how.

Alternatively, perhaps the maximum possible when using all c "ab" strings is:

2*c + the maximum of:

   (pre_b + post_a) + the maximum possible a and b after those additions.

But pre_b and post_a can be 0 or 1, depending on availability.

So there are four possible combinations for pre_b and post_a:

1. pre_b=0, post_a=0.

   Then, after the "ab" block (ends with 'b'), the remaining a and b can be arranged to start with 'a'.

2. pre_b=1, post_a=0.

   Block starts with 'a' (pre_b is 'b') → after the block ends with 'b', add a and/or b starting with 'a'.

3. pre_b=0, post_a=1.

   Block ends with 'b', then add 'a' (post_a=1). Then, arrange remaining a-1 and b to start with 'b'.

4. pre_b=1, post_a=1.

   Block ends with 'b', add 'a' (post_a=1). Then arrange remaining a-1 and b-1 to start with 'b'.

For each of these four possibilities, compute the possible additional a and b strings.

But this is getting too detailed.

Alternatively, perhaps the optimal solution is to compute all possibilities of adding a 'b' before and/or 'a' after the "ab" block, and then compute the maximum possible a and b strings that can be added after.

But given the time constraints, perhaps the best way to proceed is to compute several scenarios and take the maximum.

Let's try to write code for this.

But first, let's outline the steps:

1. Compute the maximum possible when using all c "ab" strings.

   a. Try adding 0 or 1 'b' before.

   b. Try adding 0 or 1 'a' after.

   c. For each combination, compute the maximum possible additional a and b.

   d. Take the maximum of all possibilities.

2. Compute the maximum possible when not using all c "ab" strings.

   a. For example, use c-1 "ab" strings and see if adding more a and/or b is possible.

But this seems difficult.

Alternatively, consider that the maximum possible when using k "ab" strings is 2*k plus the maximum possible a and b arranged around them.

But since k can be up to 1e9, we can't iterate over all possible k.

So perhaps the best approach is to compute the maximum between:

- Using all c "ab" strings, plus as many a and b as possible.

- Not using any "ab" strings, and just arranging a and b.

- Using c-1 "ab" strings, and see if that allows for more a and b to be used.

But how to model this.

Alternatively, the maximum possible when using k "ab" strings is 2*k plus the maximum possible a and b arranged in a way that the transitions are valid.

So the maximum possible for each k is 2*k plus the maximum possible a and b that can be arranged before and after the k "ab" strings.

But again, we need to find the best k.

But this is not feasible for large k.

So perhaps the optimal solution is to consider the following cases:

- Use all c "ab" strings.

- Use c-1 "ab" strings.

- Use 0 "ab" strings.

Then, compute the maximum among these.

But this might not be sufficient.

But given the examples, using all c "ab" strings and adding a and/or b before and after seems to give the correct result.

Let's try to code this.

The code will need to:

- For each possible combination of adding a 'b' before and/or 'a' after the "ab" block, compute the maximum possible a and b strings that can be added.

Let's outline this in code.

First, the case where we use all c "ab" strings.

We can have four possibilities for adding a 'b' before (if possible) and/or 'a' after (if possible).

For each possibility:

pre_b = 0 or 1 (if b >=1)

post_a = 0 or 1 (if a >=1)

remaining_a = a - post_a

remaining_b = b - pre_b

Then, after the block, after adding the 'a' (post_a), the next string must start with 'b' (since the post_a string ends with 'a').

So after the post_a, the remaining a and b can be arranged as:

if post_a is 1:

   after_sequence = maximum sequence starting with 'b', using remaining_a and remaining_b.

else:

   after_sequence = maximum sequence starting with 'a' (since the block ends with 'b'), using remaining_a and remaining_b.

So in code:

for pre_b in [0, 1]:

   if pre_b and b <1:

       continue

   for post_a in [0, 1]:

       if post_a and a <1:

           continue

       new_a = a - post_a

       new_b = b - pre_b

       if post_a:

           # after post_a, the sequence starts with 'b'

           # compute the maximum sequence starting with 'b'

           max_after = 0

           if new_b >=1:

               max_after +=1

               new_b_remaining = new_b -1

               new_a_remaining = new_a

               pairs = min(new_a_remaining, new_b_remaining)

               max_after += 2 * pairs

               new_a_remaining -= pairs

               new_b_remaining -= pairs

               if new_a_remaining >0 or new_b_remaining >0:

                   # can add one more if possible

                   if new_a_remaining >0:

                       # after last pair ends with 'b', add 'a'

                       max_after +=1

                   elif new_b_remaining >0:

                       # after last pair ends with 'a', add 'b'

                       max_after +=1

           else:

               max_after =0

       else:

           # after block, sequence starts with 'a' (block ends with 'b')

           # can add 'a' strings, but only if new_a >=1

           # compute the maximum sequence starting with 'a'

           max_after =0

           if new_a >=1:

               max_after +=1

               new_a_remaining = new_a -1

               new_b_remaining = new_b

               pairs = min(new_a_remaining, new_b_remaining)

               max_after += 2 * pairs

               new_a_remaining -= pairs

               new_b_remaining -= pairs

               if new_a_remaining >0 or new_b_remaining >0:

                   if new_a_remaining >0:

                       # after last pair ends with 'b', add 'a'

                       max_after +=1

                   else:

                       # after last pair ends with 'a', add 'b'

                       max_after +=1

           else:

               max_after =0

       total = pre_b *1 + post_a *1 + 2 * c + max_after

       max_possible = max(max_possible, total)

So this code would iterate over all four possibilities for pre_b and post_a, and for each, compute the maximum possible a and b after.

But this code is complex and may need to be optimized for large values.

But given that the code is O(1) (since it's only four possibilities), this is manageable.

Additionally, we need to compute the case where we use no "ab" strings.

This is the standard problem of arranging a and b strings to form the longest possible good string.

Which is:

max_without_ab = max_length(a, b) where max_length is the maximum possible length from a and b.

The max_length(a, b) is computed as:

if a ==0 and b ==0:

   0

else:

   if a == b:

      a + b

   else:

      2 * min(a, b) +1

But this is only if the a and b can be arranged in a way that alternates.

So for example, a=3, b=5: 5 is larger by 2. So maximum is 2*3+1=7.

But the actual maximum is 7.

So the formula holds.

So the code for max_without_ab is:

max_ab = 0

if a + b ==0:

    pass

else:

    if abs(a -b) <=1:

        max_ab = a + b

    else:

        max_ab = 2 * min(a, b) +1

So, the maximum when not using any "ab" strings is max_ab.

Another case to consider is using some "ab" strings but not all. For example, using c-1 "ab" strings and adding a 'a' and/or 'b' strings.

But this is difficult to model.

Alternatively, the code can compute the maximum between:

- The maximum case when using all c "ab" strings plus a and b.

- The maximum case when using c-1 "ab" strings plus a and b.

- The max_without_ab.

But how to compute the case when using c-1 "ab" strings.

For example, using c-1 "ab" strings (each contributing 2, so total 2*(c-1)), and then adding a 'a' or 'b' before or after.

But this is similar to the previous case.

But this may be a lot of code.

Alternatively, considering that the case when using c-1 "ab" strings can be modeled by setting c to c-1 and proceeding as before.

But given time constraints, perhaps the code can compute the maximum of all four possibilities for all c and c-1.

But this is not feasible for large c.

But given that the time limit is 1 second, even if the code has a few more cases, it would be manageable.

So, the code can compute the maximum between:

- Using all c "ab" strings and adding a and/or b.

- Using c-1 "ab" strings and adding a and/or b.

- Using no "ab" strings.

But how to compute the case when using c-1 "ab" strings.

But this may not be necessary. For example, in the fourth sample input:

Input: 2 2 1 → output is 6.

The optimal string is "ababab", which is using all 1 "ab" string (contributes 2) plus two 'ab' from a and b strings? Or how?

Wait, the input has a=2, b=2, c=1.

The output is 6, which is the length of "ababab".

This can be achieved by using the "ab" string (2 characters) plus two "a" and two "b" strings arranged as "abab".

But how?

Wait, the "ab" string is "ab". Then, the remaining a=2 and b=2.

So after the "ab" string (ends with 'b'), we can add an "a" string (a=1), then a "b" string (b=1), then another "a" (a=0), then another "b" (b=0). So the total is 2 (ab) +1 (a) +1 (b) +1 (a) +1 (b) → total 6.

But this is not possible because after the "ab" string (ends with 'b'), adding "a" is allowed. Then, "a" ends with 'a', adding "b" is allowed. Then "b" ends with 'b', adding "a" is allowed. Then "a" ends with 'a', adding "b" is allowed.

So the sequence is ab a b a b → which is valid, and has length 2 +1 +1 +1 +1 =6.

So this uses one "ab" string, and four a and b strings (a=2 and b=2), total 6.

But according to the case where all "ab" strings are used (c=1), the code would compute:

pre_b =0, post_a=0.

Then, after the block (ends with 'b'), the a and b can be arranged as starting with 'a' (since the block ends with 'b').

The remaining a is 2 and b is 2.

The maximum sequence starting with 'a' is 2+2=4. Because they are equal. So the total is 2*1 (ab) +4=6.

Which matches.

So the code for the case when all "ab" strings are used would compute this correctly.

So perhaps the code for the case of using all c "ab" strings would handle this case.

Thus, the code needs to:

- Compute the maximum possible when using all c "ab" strings, considering all four possibilities of pre_b and post_a.

- Compute the maximum possible when not using any "ab" strings.

Then, take the maximum between these two.

But what about cases where using c-1 "ab" strings is better?

For example, imagine a case where using c-1 "ab" strings allows a longer sequence.

But I can't think of such a case.

Perhaps if there are a lot of a and b strings left after using all c "ab" strings, but they can't be arranged, but using one less "ab" string allows a better arrangement.

But this seems unlikely.

Alternatively, consider a case where c=1, a=0, b=0. Then, using the "ab" string gives 2, which is better than not using it.

But if a=0, b=1, c=1. Using all c "ab" strings gives 2. But if you use one "b" before the "ab" string, you get 1 +2=3. But since a=0, you can't add anything after.

But wait, in this case, a=0, b=1, c=1.

The code would try pre_b=1 (since b >=1), post_a=0 (since a=0). Then, the block of 1 "ab" strings (2), so pre_b=1, block=2, then after, post_a=0.

Then, after the block (ends with 'b'), the remaining a=0, b=0 (since pre_b was 1, which is subtracted from b). So the after sequence is 0.

Total is 1+2=3.

Which is correct.

So the code would compute this.

Thus, the code seems to handle all cases.

Thus, the plan is:

Compute the maximum between:

1. The maximum possible when using all "ab" strings, considering adding a 'b' before and/or 'a' after, plus the remaining a and b arranged.

2. The maximum possible when using no "ab" strings.

The code for case 1 is as outlined earlier.

Now, let's code this.

First, handle the case when c is 0.

If c is 0, then the maximum is max_without_ab.

Otherwise, compute the four possibilities for using all c "ab" strings.

Then, compute the max_without_ab.

The maximum of all these is the answer.

But also, when c is 0, the max_without_ab is the answer.

So in code:

def main():

    a, b, c = map(int, input().split())

    max_total = 0

    # Case 1: use all c "ab" strings.

    if c >0:

        for pre_b in [0, 1]:

            if pre_b > b:

                continue

            for post_a in [0, 1]:

                if post_a > a:

                    continue

                remaining_a = a - post_a

                remaining_b = b - pre_b

                # after the ab block, after adding pre_b and post_a, compute the remaining.

                if post_a:

                    # after post_a (ends with 'a'), next must start with 'b'

                    # compute max sequence starting with 'b'

                    # 1. use one 'b' if available

                    current = 0

                    if remaining_b >=1:

                        current +=1

                        new_b = remaining_b -1

                        new_a = remaining_a

                        pairs = min(new_a, new_b)

                        current += 2 * pairs

                        new_a -= pairs

                        new_b -= pairs

                        # check if any remaining

                        if new_a >0:

                            current +=1

                        elif new_b >0:

                            current +=1

                    else:

                        current =0

                else:

                    # after ab block (ends with 'b'), next must start with 'a'

                    current =0

                    if remaining_a >=1:

                        current +=1

                        new_a = remaining_a -1

                        new_b = remaining_b

                        pairs = min(new_a, new_b)

                        current += 2 * pairs

                        new_a -= pairs

                        new_b -= pairs

                        if new_a >0:

                            current +=1

                        elif new_b >0:

                            current +=1

                    else:

                        current =0

                total = pre_b + 2*c + post_a + current

                if total > max_total:

                    max_total = total

    # Case 2: use no "ab" strings.

    if a ==0 and b ==0:

        current =0

    else:

        if abs(a -b) <=1:

            current = a + b

        else:

            current = 2 * min(a, b) +1

    if current > max_total:

        max_total = current

    print(max_total)

But this code may not handle all cases.

Testing the first example:

Input: 1 1 1.

Case 1: pre_b can be 1 (b=1), post_a can be 1 (a=1).

remaining_a =0, remaining_b=0.

after post_a: current is 0 (since remaining_b is 0).

So total is 1 + 2*1 +1 +0=4.

Which is correct.

The code would compute this.

Another example: input 2 2 1.

Case 1: pre_b=0, post_a=0.

remaining_a=2, remaining_b=2.

after ab block (ends with 'b'), the sequence starts with 'a'.

max_after:

if remaining_a >=1 (yes).

current =1.

new_a =1, new_b=2.

pairs = min(1, 2) →1.

current +=2 →3.

new_a=0, new_b=1.

new_b >0 → add 1.

current becomes 4.

total is 0 + 2*1 +0 +4 =6.

Which is correct.

The code would select this.

So this code seems to handle the examples correctly.

Another test case: input 1000000000 1000000000 1000000000.

The code will compute:

pre_b=1, post_a=1.

remaining_a= 1e9 -1, remaining_b=1e9-1.

after post_a: sequence starts with 'b'.

current =1 (from remaining_b=1e9-1 >=1).

new_b=1e9-2, new_a=1e9-1.

pairs = min(1e9-1, 1e9-2) →1e9-2.

current += 2*(1e9-2) → 1 + 2*(1e9-2).

new_a = (1e9-1) - (1e9-2) =1.

new_b =0.

So add new_a >0 → current +=1.

Total current is 1 + 2*(1e9-2) +1 =2*(1e9-2) +2= 2*1e9 -4 +2= 2e9-2.

Then, the total is pre_b (1) + post_a (1) + 2*c (2e9) + current (2e9-2) → 1+1 + 2e9 + 2e9-2 = 4e9.

Which matches the sample.

Thus, the code works for this case.

So this code should handle all cases.
</think>

```python
a, b, c = map(int, input().split())

max_total = 0

# Case 1: Using all 'ab' strings
if c > 0:
    for pre_b in [0, 1]:
        if pre_b > b:
            continue
        for post_a in [0, 1]:
            if post_a > a:
                continue
            rem_a = a - post_a
            rem_b = b - pre_b
            current_add = 0

            if post_a:
                # After 'a', next must start with 'b'
                if rem_b >= 1:
                    current = 1
                    new_b = rem_b - 1
                    new_a = rem_a
                    pairs = min(new_a, new_b)
                    current += 2 * pairs
                    new_a -= pairs
                    new_b -= pairs
                    if new_a > 0:
                        current += 1
                    elif new_b > 0:
                        current += 1
                    current_add = current
            else:
                # After 'ab' block (ends with 'b'), next must start with 'a'
                if rem_a >= 1:
                    current = 1
                    new_a = rem_a - 1
                    new_b = rem_b
                    pairs = min(new_a, new_b)
                    current += 2 * pairs
                    new_a -= pairs
                    new_b -= pairs
                    if new_a > 0:
                        current += 1
                    elif new_b > 0:
                        current += 1
                    current_add = current

            total = pre_b + post_a + 2 * c + current_add
            if total > max_total:
                max_total = total

# Case 2: Using no 'ab' strings
if a == 0 and b == 0:
    case2 = 0
else:
    if abs(a - b) <= 1:
        case2 = a + b
    else:
        case2 = 2 * min(a, b) + 1
if case2 > max_total:
    max_total = case2

print(max_total)
```