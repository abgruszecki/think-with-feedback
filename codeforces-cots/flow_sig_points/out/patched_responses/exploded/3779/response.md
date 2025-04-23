<think>
Okay, let's see. We need to determine if Vasya can force a win no matter how Petya plays. The problem is about a game where players take turns removing characters from a string until it's length 11. The final string must start with 8 for Vasya to win.

So, the key is to find out if Vasya can ensure that the final 11-character string starts with 8. But how?

First, let's think about the steps involved. The initial string has length n (which is odd). The players remove characters until the length is 11. Since n is odd, the number of moves each player makes is (n-11)/2. Wait, wait. Because each move reduces the length by 1. So starting from n, to reach 11, they remove (n-11) characters total. Since Vasya goes first, he will make ceil((n-11)/2) moves. Because n is odd and >=13, (n-11) is even. For example, n=13: 13-11=2, so 2 moves, each player once. Vasya first, then Petya. For n=15: 15-11=4 moves, Vasya 2, Petya 2. So the number of moves each player can make is (n-11)/2 each. Wait, no. Because n-11 is even. Let's say n-11 is 4. Then Vasya and Petya each take two turns. Because total is 4 moves: Vasya first, then Petya, then Vasya, then Petya. So the number of moves per player is (n-11) // 2. Wait, yes. Because (n-11) is the total moves. Since it's even and the players alternate, each will make exactly (n-11)/2 moves.

So, Vasya has to make (n-11)//2 moves, and Petya the same. Wait, no. Wait, for example, when n is 13: n-11=2. So 2 moves total. Vasya first, then Petya. Each makes 1 move. (2//2=1). So yes, each makes (n-11)/2 moves.

So the total number of moves each player makes is k = (n-11) // 2. Because (n-11) is even. So both players have k moves.

The problem reduces to selecting positions in the string such that after all moves, the remaining 11 characters have the first character as 8. But since the players are alternately removing characters, Vasya wants to maximize the chances of an 8 in the first position, while Petya wants to prevent that.

So, the key is to find whether there's a way for Vasya to choose the positions such that, even after Petya's best attempts, the earliest possible 8 in the string is within a window that can't be blocked.

Wait, perhaps the optimal strategy for Vasya is to find the earliest possible position for an 8 such that there are enough characters after it to form the 11 digits. And for Petya, he would try to eliminate that possibility.

Alternatively, think about the positions where 8s are in the original string. For each 8, we can check if there's a way to select a substring of 11 characters starting with that 8, such that Vasya can ensure that all the necessary characters (the 11 characters starting at that 8) are not removed by Petya.

But how to model this?

Another approach: Since each player can remove any character, the game is about choosing which characters to remove. But the order of removal is such that Vasya and Petya take turns removing one character each. However, the exact order of removals affects the final string.

But maybe we can model this by considering that in order for the final string to start with an 8, there must be a window of 11 characters in the original string where the first character is 8, and there are enough 8s in positions such that even after Petya's moves, Vasya can retain that 8 as the first character.

Alternatively, perhaps the key is to find the earliest possible occurrence of an 8 where there are enough positions after it to form a window of 11 characters, and Vasya can protect that 8 from being removed.

Wait, but the problem is that the players can remove any characters, not just in the window. So the final 11 characters could be formed from any subset of the original string's characters, maintaining their order.

So the problem is equivalent to choosing 11 characters from the original string (in order) such that the first is 8, and Vasya can ensure that regardless of Petya's choices, this set of 11 is selected.

But how to model this?

Alternatively, the process of deleting characters can be thought of as selecting a subsequence of length 11. Vasya and Petya take turns deleting characters, but the order in which they delete them affects the final subsequence. However, since each deletion can be any character, the players can influence which characters are kept.

But perhaps the optimal strategy is for Vasya to try to have the earliest possible 8 in the string such that in the positions up to that 8 plus 10 positions after, there are enough 8s that even after Petya removes some, there's still one left.

Wait, maybe the key is to find if there exists an index i such that in the original string, s[i] is 8, and the number of 8s in the positions from i to i+10 is at least k+1, where k is the number of moves each player has. Because each player can remove up to k characters, so Vasya can ensure that even if Petya removes k 8s in that window, there's still at least one left.

Wait, let's think about this. Suppose we have a window of 11 characters starting at position i. The first character is 8. The number of 8s in this window is m. To ensure that after all deletions, the first character of the final string is 8, Vasya needs to have m > k. Because in the worst case, Petya would try to delete as many 8s as possible in the window.

Wait, but the players can delete any characters, not just in the window. So the window is not fixed until the end. Hmm, this complicates things.

Alternatively, think of the game as both players trying to influence the final 11 characters. The players take turns removing characters until there are 11 left. Vasya's goal is to have the first of those 11 be 8.

So the question is, can Vasya force the final string's first character to be 8, no matter how Petya plays.

To model this, perhaps the key is to find the earliest possible position where an 8 can be part of the final 11, and ensure that there's a way to select that 8 as the first character such that even when Petya is trying to block, it's impossible.

Another approach is to model the problem as follows: The final string must have 11 characters. The first character is 8. Vasya and Petya take turns removing characters. The total number of moves is (n-11) = 2k. Each player removes k characters. Since Vasya starts first.

But how does their choice of which character to remove affect the final string?

It's possible that the optimal strategy for Vasya is to remove all characters that are not part of a certain 11-length substring starting with 8, while Petya tries to remove characters within that substring.

But perhaps a better way is to consider that Vasya can choose a window (a sequence of 11 characters) where the first character is 8, and the number of 8s in this window is sufficient to withstand Petya's attempts to remove them.

Wait, for example, suppose the window has m 8s. If Petya can remove (m-1) 8s from this window, then the remaining would have at least one 8. But since each player can remove up to k characters, which is (n-11)/2. But how does this relate to the window's 8 count?

Alternatively, the window of 11 characters must be such that the earliest possible 8 in the string is in a position where even after Petya removes k 8s in the window, there's still at least one 8 left.

But I'm not sure. Let's think through an example.

Take the first example input:

Input is 13, 8380011223344.

So n is 13, so k = (13-11)/2 = 1. So each player makes 1 move.

The original string is 8 3 8 0 0 1 1 2 2 3 3 4 4.

Vasya's first move is to remove the second character (3), leaving the string starting with 8, then 8, etc. Then Petya has to remove one character. But in the resulting string (after Vasya's move), the first two characters are 8 and 8. So when Petya removes any character except the first 8, the remaining string's first character is 8, leading to a telephone number. So Petya can't remove the first 8, so she has to leave it. Hence Vasya wins.

So the strategy here is to find a window where the earliest 8 is in a position that after both players' moves, there are enough 8s in the window to ensure that the first character is 8.

Wait, but in this example, the window is the entire string after removing two characters. But how did Vasya choose which characters to remove?

Another example: the second input is 15, 807345619350641. Output is NO. So Vasya can't win. Because after his first move, Petya can remove the 8. Then the remaining string has no 8s, so the final string's first character can't be 8.

So the key is that Vasya needs to have a way to ensure that in the final 11 characters, there's an 8 in the first position. To do that, he must select a set of positions where the earliest 8 is such that there are enough 8s in the possible positions that even after Petya's k moves (removing k 8s), there's at least one left.

But how to model this.

Let me think of the following approach:

For each possible 8 in the original string, check if there exists a window of 11 characters starting at that 8 (i.e., the 8 is the first character of the window) such that within this window, the number of 8s is more than the number of possible deletions that Petya can do in that window.

Wait, but the window can be formed by the players deleting other characters. For example, if the original string is long, but there's an 8 at position i, then the window of 11 characters starting at i is the substring from i to i+10. But in the process of deletion, other characters can be removed, leading to a different window. So this approach might not directly apply.

Alternatively, perhaps the optimal strategy is to find the earliest possible 8 that can be part of the final 11-length string. For each such 8, calculate whether Vasya can protect it from being deleted by Petya.

Wait, but how? Because when players delete characters, they can delete any character in the current string. So Vasya's strategy would be to remove characters that are not part of the desired window, forcing the final string to be within that window.

Hmm. Maybe another angle: Vasya wants to ensure that in the final string, the first character is 8. To do this, he must ensure that there exists a sequence of 11 characters in the original string where the first is 8, and the number of 8s in that sequence is sufficient to survive Petya's deletions.

But how?

Let me think: the players are alternately deleting characters. The final string is a subsequence of the original string, of length 11, where the first character is 8. Vasya wants to make sure that such a subsequence exists regardless of Petya's moves.

The problem is equivalent to: can Vasya choose a subset of the original string's characters (as a subsequence) of length 11, starting with 8, such that the number of 8s in that subset is greater than the number of 8s that Petya can delete during his moves.

But how to model the interaction between the players' deletions and the final subsequence.

Alternatively, think of it as a game where Vasya and Petya are trying to shape the final subsequence. Each deletion is a choice of which character to remove from the current string.

Vasya's goal is to have the first character of the final string be 8. So he needs to ensure that after all deletions, the first character of the remaining string is 8.

But the order of deletions matters. For example, if the first character is 8, and the players delete other characters, the first character remains. But if Vasya can delete other characters, and Petya can't delete the first 8 because he's not allowed (since the players can delete any character), then Vasya wins.

Wait, but Petya can delete the first 8 if he wants.

So the problem is that Vasya must protect the 8 in the first position of the final string. To do that, he must ensure that even if Petya tries to delete that 8, Vasya can prevent it by deleting other characters.

Wait, but once a character is deleted, it's gone. So perhaps the optimal strategy is to find a position in the original string where an 8 is early enough that after all deletions, it's the first remaining character.

Alternatively, the earliest possible 8 that can be the first character of the final string. Let's imagine that the final string's first character is the 8 at position i in the original string. For this to happen, all characters before i must be deleted. Because otherwise, there's a character before i in the original string that is part of the final string, which would come before the 8 at i.

So, the final first character must be the earliest possible 8 that's retained after all deletions. Therefore, Vasya's strategy is to delete all characters before this 8, except for enough that allow the 8 to be in the first position.

But how can he ensure that?

Wait, but the problem is that the players alternate deleting characters, and each can delete any character. So, for example, if there's an 8 at position i, but there are some characters before i, Petya could delete that 8 to prevent it from being the first character.

So, the key is to find an 8 such that the number of characters that need to be deleted before it is small enough that Vasya can ensure they are all deleted, and also that there are enough 8s in the remaining positions that even if Petya deletes some, one remains.

Alternatively, perhaps the optimal approach is to find the earliest possible 8 in the string, and check whether in the remaining positions (from that 8 onwards), there are enough 8s such that even after Petya's k deletions, there's at least one 8 in the first 11 characters.

Wait, maybe this is the right approach.

Let me formalize this. Let's consider that the final string is a subsequence of the original. The first character is 8. So, the first character of the final string must be the first occurrence of 8 in the original string that is not deleted by any player.

Wait, no. Because players can delete any characters, including the 8s. So, the final string's first 8 could be any 8 in the original string, but Vasya and Petya's choices will determine which one.

But how can Vasya ensure that there's an 8 left in the final string and that it is the first character.

This seems complicated. Let's think differently.

Suppose that in the original string, the positions of all 8s are stored. Let's say the positions are p1, p2, ..., pm.

For each 8 at position pi, what's the earliest possible position where the 8 can be the first character of the final string.

For this to happen, we need to delete all characters before pi. But each player can choose to delete characters.

The total number of deletions made by both players is (n-11). So, the number of characters that need to be deleted from the original string is (n-11). But the players can choose which ones.

So, for the 8 at position pi to be the first character of the final string, all characters before pi must be deleted. Because if even one character before pi remains, the final string's first character would be that character, not the 8.

So the number of characters before pi is (pi) (assuming 0-based index). Let's say the original string is 0-based. Then the number of characters before pi is pi. These all need to be deleted. Also, the number of characters after pi must be at least 10 (since the final string is 11 characters). So the original string must have pi + 10 < n.

Wait, the final string must be of length 11. So, if the first character is at position pi, the remaining 10 characters must be from positions pi+1 to the end. So, the total length from pi onwards (inclusive) must be at least 11. So, n - pi >= 11.

So for an 8 at position pi to be the first character of the final string, the following must hold:

pi <= n-11.

Because from pi onwards, there are (n - pi) characters. We need at least 11, so (n - pi) >= 11 → pi <= n-11-1 → no. Wait, pi can be as high as n-1 -10 = n-11. Because then, the next 10 characters are from pi+1 to pi+10, which is 11 characters total.

So, the condition is pi <= n-11.

So, for each 8 in the string where pi <= n-11, we can consider it as a candidate.

For each such 8 at position pi, how many characters need to be deleted before it (i.e., the number of characters before pi) is pi. Because those all need to be deleted for this 8 to be the first in the final string.

Additionally, the total number of characters that need to be deleted from the entire string is (n-11). So, the number of characters that can be deleted after pi (to reach 11 characters) is (n-11) - pi. Because deleting the first pi characters (pi deletions) and then (n-11 - pi) from the remaining (n - pi) characters.

But the players take turns deleting these. So, the total number of deletions available for the entire string is (n-11). For the 8 at pi to be the first character, all characters before pi must be deleted (pi deletions). Then, the remaining deletions (n-11 - pi) must be applied to the substring starting at pi, which has length (n - pi). The remaining after deletions is (n - pi) - (n-11 - pi) = 11, which is correct.

Now, the question is: can Vasya and Petya's deletion sequence allow that all the pi characters before pi are deleted, and that in the remaining (n-pi) characters, after deleting (n-11 - pi) characters, the first character is 8 (which is at position pi in the original string) and that the remaining 10 characters form a valid telephone number (which they do, since the first is 8, and we just need the length to be 11, which it is).

Wait, but the first character is 8, but the remaining 10 can be anything. The telephone number just requires the first to be 8 and total length 11. So as long as the first character is 8 and the total is 11, it's valid.

So, the key is to find whether there exists a position pi (where pi <=n-11) such that:

The number of deletions needed to delete all characters before pi (which is pi) is <= (n-11). Because (n-11) is the total deletions available. So pi must be <= (n-11). Which is already covered by pi <=n-11.

Then, for the remaining deletions (k_total = n-11 - pi) to be applied to the substring from pi onwards (which has length (n-pi) = len_remaining). The remaining deletions after deleting the first pi characters are (n-11 - pi).

But how do these deletions affect the substring starting at pi?

Because the players are alternately deleting characters. The remaining deletions (k_remaining = n-11 - pi) must be distributed between Vasya and Petya. Since the total deletions is (n-11), and we've already used pi deletions to delete the first pi characters. Wait, but those deletions are part of the total (n-11) deletions.

Ah, no. Because the pi deletions are part of the total (n-11) deletions. So, the total number of deletions available after deleting the first pi characters is (n-11) - (pi) = (n-11 - pi). These must be applied to the substring from pi onwards, which has length (n-pi). The number of deletions here is (n-11 - pi), which would leave (n-pi) - (n-11 - pi) = 11 characters.

But how do these deletions affect the first character of this substring (which is the 8 at position pi).

Vasya wants to ensure that this 8 remains after all deletions. However, during the deletions in this part (the substring starting at pi), Petya can choose to delete this 8, which would make the final first character not an 8.

So, the problem reduces to: Can Vasya, during the (n-11 - pi) deletions in the substring starting at pi, ensure that the first character (the 8) is not deleted by Petya.

But how?

The remaining deletions (k_remaining = n-11 - pi) are split between Vasya and Petya. Let's compute how many moves each has in this phase.

The total deletions made so far (pi) are part of the total (n-11). So, the remaining deletions are (n-11 - pi). But how are these divided between the players?

Wait, the order of deletions is that Vasya starts. Each player takes turns deleting one character. So the total number of deletions is (n-11) = 2k. So, the total number of moves is 2k, each player making k moves.

If the deletions of the first pi characters are all done by the players, then the players have to delete (n-11) characters. So, the first pi characters must be deleted in some order.

But this is getting complicated. Perhaps there's a better way.

Alternative approach: For each possible candidate 8 at position i (i <= n-11), check if the number of 8s in the window [i, i+10] (since the final string is 11 characters) is greater than the number of moves Petya can make in the entire game. Because in the worst case, Petya will delete as many 8s as possible in that window.

Wait, but the number of moves Petya has is k = (n-11)/2. So, if the window [i, i+10] has at least k+1 8s, then even if Petya deletes k 8s, there is still one left, which Vasya can preserve.

But how to model this.

For example, in the first sample input:

n=13, s=8380011223344.

So k = (13-11)/2 = 1. The window must be 11 characters. Let's look for the earliest 8.

The first 8 is at position 0. The window is positions 0-10 (inclusive). The 8s in this window are positions 0 and 2. So m=2. Petya can delete 1 8. So 2 -1 =1 >=1. So this window has enough 8s.

But what about the other 8 at position 2. The window would start at 2, but then the window would be 2-12 (since n=13, 2+10=12). The 8 in this window is at position 2. So m=1. Then Petya can delete 1 8, which would make m=0, so Vasya loses.

So the first window (starting at 0) has enough 8s.

So the candidate i=0 has m=2, which is greater than k=1. So answer is YES.

In the second sample input:

n=15, s=807345619350641.

k=(15-11)/2=2.

Looking for 8s. The first 8 is at position 0. The window is positions 0-10. How many 8s are in this window? The string starts with 8, then 0,7,3,4,5,6,1,9,3,5. So only one 8. So m=1. But Petya can delete 2 8s (but there's only one). So after that, there are zero 8s. So Vasya can't win.

So the answer is NO.

So the approach is: For each 8 in the original string, where the window starting at i has at least 11 characters (i.e., i <= n-11), check if the number of 8s in the window [i, i+10] is greater than k. If any such i exists, then output YES, else NO.

Because, in that case, even if Petya deletes k 8s in that window, there will be at least one left. Since the window starts with 8, the first character is 8, and the remaining 10 are part of the final string.

So the algorithm is:

1. Compute k = (n-11) // 2.

2. For each index i where s[i] is '8' and i <= n-11:

   a. Consider the window from i to i+10 (inclusive).

   b. Count the number of '8's in this window.

   c. If this count > k, then return YES.

3. If no such i is found, return NO.

Because:

- The earliest possible window is the one that starts with the first 8 in the string. Because if there's a window with enough 8s, then Vasya can choose to delete the characters before this 8, and then during the remaining deletions, Petya can delete at most k 8s, but the window has enough to survive.

Wait, but how does Vasya ensure that all the characters before the chosen 8 are deleted?

Ah, this is a critical point. For the 8 at position i to be the first character of the final string, all characters before i must be deleted. The number of characters before i is i. So, the number of deletions required to remove them is i. But the total number of deletions possible is (n-11).

But if i > (n-11), then it's impossible to delete all characters before i. So, i must be <= (n-11).

Wait, but n-11 is the total number of deletions available. So i must be <= (n-11), because otherwise, we cannot delete all i characters before it.

So, for a given 8 at position i, the number of deletions required to remove all characters before i is i. But since the total deletions available is (n-11), we must have i <= (n-11). Otherwise, it's impossible to delete all characters before i.

So, the candidate 8s must have i <= (n-11). Also, the window starting at i must have 11 characters, which requires that i+10 < n. So, i <= n-11.

Yes. So, the steps are:

For each 8 in the string at position i, where i <= (n-11):

   count the number of 8s in the window [i, i+10].

   if that count > k, return YES.

Otherwise, return NO.

This is the correct approach.

So the code can be written as follows:

Read n and s.

Compute k = (n-11) // 2.

For each i from 0 to n-1:

   if s[i] is '8' and i <= n-11:

       window is s[i : i+11] (since 11 characters)

       count = number of '8's in the window.

       if count > k:

           return YES.

After checking all such i, return NO.

Because the earliest possible 8 is the one with the smallest i, and if that window has enough 8s, Vasya can focus on that window, forcing all deletions to be from before i, and then in the window, Petya can't delete enough 8s to prevent a telephone number.

Wait, but how does Vasya ensure that all the characters before i are deleted? Because the players take turns deleting any characters.

Ah, this is the key point I'm missing. The above approach assumes that Vasya can delete all the characters before i, but in reality, both players are deleting characters. So, for the 8 at position i to be the first in the final string, all the characters before i must be deleted. The total number of characters to delete before i is i. The total number of deletions in the entire game is (n-11). So, i must be <= (n-11), which we already have in the condition.

But can Vasya and Petya's deletions of characters before i be sufficient?

Yes, because the total number of deletions possible is (n-11), which is >= i (since i <=n-11). So, Vasya can prioritize deleting the characters before i. Let's see.

Vasya's strategy would be to delete all characters before i as quickly as possible. Since there are i characters to delete, and (n-11) total deletions.

But how?

If i <= k, then Vasya can delete all i characters in his first i moves, but he has k moves. For example, if i=2 and k=3, he can delete the two characters, then delete other characters. But if i exceeds the total deletions available, it's impossible.

Wait, but i must be <= (n-11). Since (n-11) is the total number of deletions. So i <= (n-11). So, the deletions required to delete all characters before i is i, and (n-11) - i deletions are left for the window.

So, as long as i <= (n-11), the players can delete all characters before i, and then delete (n-11 -i) characters in the window.

But how is this possible when the players are taking turns?

Vasya's strategy would be to first delete all characters before i. Because if there's a choice between deleting a character before i or after, he would choose to delete before. But Petya may choose to delete characters from the window, which could include the 8.

So, the problem is that even if i is <= (n-11), Vasya cannot guarantee that all characters before i are deleted, because Petya may choose to delete characters from the window instead.

So, the approach I thought of earlier is not sufficient. Because the window's 8 count is only considered if all the characters before i are deleted. But Vasya cannot force that.

So, this approach is incorrect.

Hmm. So this complicates things.

So the previous approach is invalid. What's the correct approach?

Alternative idea:

The players can delete any character. Vasya's goal is to have the final string start with 8. To achieve this, Vasya needs to ensure that there exists a way to delete (n-11) characters such that the remaining 11 characters start with 8. But Petya is trying to prevent this.

The problem is to determine whether Vasya can win regardless of Petya's moves. So, this is a game theory problem.

In such cases, the solution often involves finding a scenario where Vasya has a move that leaves Petya with no good options.

So, perhaps the correct approach is to find the earliest 8 in the string, and see if even after deleting as many 8s as possible, there's still a sufficient number left.

Wait, perhaps the correct approach is to find the earliest possible position where there are enough 8s in the entire string such that even if Petya tries to delete all the 8s, there are enough left.

Let me think differently. For Vasya to win, there must be a scenario where the final string starts with 8. Petya will try to prevent this.

The key is to model this as a game where both players are optimally trying to maximize/minimize the number of 8s in the final string.

But this is complex.

Another approach: Since both players are deleting characters, the final string is the original string with (n-11) characters removed.

The first player (Vasya) wants to maximize the chance that the first character is 8. Petya wants to minimize it.

The problem is to determine whether there's a strategy for Vasya such that no matter what Petya does, the first character of the final string is 8.

So, the question is whether the earliest possible 8 in the original string can be preserved in the final string.

But how?

Let's think recursively. The players take turns deleting characters. The final string is determined by the order of deletions. Vasya wants to ensure that the first character is 8.

But this is not tractable for large n.

Alternative idea: For Vasya to have a winning strategy, there must be a sufficient number of 8s in the string such that Petya cannot delete enough of them to leave none in the first possible positions.

Wait, the earliest occurrence of an 8 that can be part of the final 11 characters.

Suppose the earliest 8 is at position i. For this 8 to be in the final string, there must be at least (n-11) deletions. The problem is to determine whether, even after Petya's deletions, there's a way to have this 8 as the first character.

But perhaps the solution is to find the earliest 8 in the string where the number of 8s in the entire string is sufficient to survive Petya's deletions.

Let's calculate the maximum number of 8s that Petya can delete. Since each player has k moves, Petya can delete up to k 8s. So, Vasya needs at least k+1 8s in the string. Because even if Petya deletes k 8s, there's at least one left.

But this is not sufficient. Because the 8s need to be positioned such that the first one remains.

Wait, for example, if there are k+1 8s in the entire string, but they are all after some positions, then Vasya can delete other characters to bring them to the front. But Petya can delete some 8s.

But this is not straightforward.

Alternatively, the problem can be reduced to: can Vasya select a subset of the string such that the first character is 8, and there are enough 8s in the subset to survive Petya's deletions.

But how to model this.

The minimal requirement is that there exists a subset of 11 characters that starts with 8, and the number of 8s in this subset is at least k+1. Because Petya can delete up to k 8s in this subset.

So, the solution is to find any window of 11 characters (starting with 8) that contains at least k+1 8s. Because Vasya can focus on this window, and even if Petya deletes k 8s in it, at least one remains.

So, the correct approach is:

Compute k = (n-11) // 2.

Find any index i where s[i] is '8', and i <= (n-11). Then, in the window [i, i+10], count the number of '8's. If any such window has count >= (k+1), then output YES. Otherwise, NO.

But how does this account for the need to delete the characters before i?

Ah, this is the crux. The previous approach assumes that the window [i, i+10] can be the final string. But in reality, other characters could be deleted from this window. For example, if the window has more than 11 characters, but this is not possible. Because the window is exactly 11 characters (from i to i+10, inclusive).

Wait, no. The window [i, i+10] is exactly 11 characters. So, in this window, there are 11 characters, and Vasya wants this window to be the final string. But how can he ensure that? Because the players delete characters from the entire string, and not just from this window.

But perhaps the answer is that Vasya can choose to delete characters outside this window, and Petya can't interfere.

But how?

Suppose there is a window [i, i+10] starting with 8 and containing at least k+1 8s. Then, Vasya's strategy is to delete all characters not in this window. There are (n-11) characters to delete. The players take turns deleting them. But Vasya can choose to delete characters outside the window first, and Petya may do the same.

If Vasya can delete all characters outside the window, then the remaining string is exactly the window, which starts with 8 and has enough 8s.

But there are (n-11) characters to delete. The number of characters not in the window is (n-11), so the players need to delete exactly those (n-11) characters. So, as long as the players delete all of them, the window remains.

But how can Vasya ensure that? Because Petya can choose to delete characters inside the window instead.

This is the problem. So the previous approach is incorrect.

Alternative idea: The players must delete exactly (n-11) characters. For Vasya to force the final string to be the window, he needs to ensure that all deletions are done on characters outside the window. But Petya can choose to delete characters inside the window, which would force Vasya to react.

So, the correct approach must consider that Petya can delete characters inside the window, which may remove 8s. Vasya's strategy must account for this.

But how?

So, perhaps the correct approach is to find a window [i, i+10] where:

- The number of 8s in the window is at least k+1.

And:

- The number of characters outside this window is <= the number of deletions that Vasya can force to be done there.

But this seems unclear.

Alternatively, the number of characters outside the window is (n-11), which is the total number of deletions. So, to ensure that all deletions are done outside the window, Vasya must have priority in choosing to delete them.

But since the players alternate, Vasya can only control half of the deletions.

For example, if there are m characters outside the window, and m is <= k (the number of moves each player has), then Vasya can delete them all. Otherwise, he can't.

But this is not necessarily correct.

Hmm.

Alternatively, the minimal number of deletions required to retain the window is (n-11) characters deleted outside the window. Because the window is 11 characters, and the original is n.

But the total number of deletions is (n-11), which is exactly the number of characters outside the window. So, if Vasya can ensure that all deletions are done outside the window, then the window is preserved. But how?

Because both players are taking turns deleting characters, and each can delete any character. So, Vasya can start by deleting a character outside the window. Petya can then delete a character inside the window. But this would reduce the window's characters, which is not desired.

So, to preserve the window, all deletions must be on characters outside the window.

But how can Vasya ensure that?

He can't. Because Petya can choose to delete characters inside the window.

Thus, the previous approach is incorrect.

So, what's the correct way to model this problem?

Alternative approach:

The game is a turn-based game where each player deletes a character. Vasya wants the final string's first character to be 8.

To model this, we need to find if there's a way for Vasya to force the first character to be 8 regardless of Petya's moves.

The key insight is that the earliest possible 8 in the string that can be part of the final 11 characters.

Suppose that the earliest 8 is at position i. For this 8 to be the first character of the final string, all characters before i must be deleted. Additionally, there must be at least 10 characters after i to form the rest of the 11-character string.

The total number of deletions required to delete the first i characters is i. The remaining deletions are (n-11) - i, which must be applied to the substring from i onward.

But how does this split between the two players?

The total number of deletions is (n-11) = 2k. So, Vasya makes k moves, Petya makes k moves.

Vasya needs to ensure that all i characters before i are deleted. So, the number of deletions that must be applied to the first i characters is i.

But the total deletions available is 2k. So, i must be <= 2k. Because otherwise, there aren't enough deletions to delete all i characters before i.

Wait, 2k = (n-11). So, i <= (n-11).

Yes, which is already a condition.

But how do Vasya and Petya's moves contribute to deleting these i characters?

Vasya can choose to delete characters before i, but Petya may choose to delete characters after i.

Thus, the challenge is to determine whether Vasya can ensure that at least i deletions are applied to the first i characters.

But since Petya is trying to minimize the deletions before i, this is a two-player game where Vasya wants to maximize the deletions before i, and Petya wants to minimize them.

So, the minimal number of deletions that can be achieved in the first i characters is i - (number of deletions possible in the first i characters).

Wait, no. The players can choose to delete characters from the first i or after i. Vasya will try to delete from the first i, Petya from after.

So, the maximum number of deletions in the first i characters is the number of times both players choose to delete from there. The minimal possible is the number of deletions that Vasya can force.

But this depends on the number of moves.

The problem is that Vasya wants to delete as many characters as possible from the first i, and Petya wants to delete as few as possible.

The minimal number of deletions in the first i is:

Each of Vasya's k moves can delete a character from the first i. Petya's k moves can delete characters from after i.

So, the maximal possible deletions in the first i is k (from Vasya's moves). Because Vasya can choose to delete k characters from the first i, while Petya deletes k characters from after i. This way, the total deletions is 2k = (n-11).

But if i < k, then Vasya can delete all i characters, but he has k moves. So, the minimal deletions in the first i is min(k, i).

Wait, no. Vasya can delete up to k characters from the first i, but if i > k, then he can delete at most k characters. Petya can choose to delete characters from after i.

So, the number of deletions in the first i is at least (i - (k + (i - k)) ) ? Not sure.

Alternatively, the number of characters deleted from the first i is the number of Vasya's deletions from that area plus the number of Petya's deletions from that area.

Vasya can choose to delete from the first i during his turns. Petya can choose to delete from anywhere.

The maximum number of deletions from the first i is Vasya's k deletions plus Petya's deletions, but Petya would not want to delete from the first i.

So, the maximum possible deletions from the first i is k (Vasya's deletions) + 0 (Petya's deletions). So, k deletions.

So, if i <= k, then Vasya can delete all i characters (since k >= i), but he can only delete k characters. So, if i <=k, then he can delete all i characters, and the remaining k -i deletions can be used to delete characters from after i.

But this leaves (n-11) -k = k deletions. Which is handled by Petya's deletions.

Wait, this is getting really complicated. Let's think with examples.

Example 1: n=13, k=1.

i=0 (the first 8). i=0, so the number of characters before i is 0. So, no deletions needed. The entire deletions are (13-11)=2. So, k=1 for each player.

The window is 11 characters. The number of 8s in the window is 2. k=1.

So, even if Petya deletes one 8, there's one left. So Vasya can win.

Example 2: n=15, k=2.

The first 8 is at i=0. The window has 1 8. So k=2. Petya can delete two 8s, but there's only one. So after deletion, none. So Vasya can't win.

Another example: suppose n=17, s=81818181818181818 (n=17).

k=(17-11)/2=3.

The earliest 8 is at 0. The window is 0-10: 11 characters. The number of 8s is 6. 6>3. So the answer is YES.

So, the algorithm is correct in these cases.

But why?

Because Vasya can ensure that even if Petya deletes up to k 8s in the window, there's at least one left.

But how does he ensure that the window is the one used?

Because he can delete all characters before i. But as we discussed earlier, this depends on the number of deletions possible.

Ah, but when i is small (like i=0), the number of characters before i is zero, so no deletions are needed. So the entire (n-11) deletions are applied to the window, but since the window has 11 characters, the deletions must remove (n-11) characters from it.

But how is this possible?

In this case, the window is 11 characters. The players must delete (n-11) characters from it. So, the final string will be (11 - (n-11)) characters? No, that's not possible. Wait, n is the original length. n-11 is the number of characters to delete. So, after deletions, the remaining is 11 characters.

So, in the case where i=0, the entire original string is the window. The players delete (n-11) characters from it. The first character must be 8. The number of 8s in the window is m. For Vasya to win, m must be >=k+1.

Because Petya can delete up to k 8s during her moves.

But how?

Vasya's strategy is to protect the 8s. So during his moves, he deletes non-8 characters. Petya deletes 8s.

But Vasya has k moves. Petya has k moves. So, the total number of 8s deleted is up to k (by Petya). So, if the window has m >=k+1 8s, then even after Petya deletes k, there are m -k >=1 8s left. The first of these remaining 8s will be the first character of the final string.

So, this is the correct approach.

Thus, the previous algorithm is correct.

The key insight is that if there exists a window of 11 characters (starting with 8) such that the number of 8s in this window is >k, then Vasya can win. Because during the deletions, even if Petya deletes k 8s, there's at least one left, and the first character is 8.

So, the code is to check for any such window.

But why do we need to check all possible windows starting with 8? Because the earliest possible window is the first 8 in the string. If it satisfies the condition, then Vasya can choose to focus on that window, and any other window is irrelevant. If the earliest window doesn't satisfy the condition, then no window can.

Wait, no. Because there might be a later window with a higher count of 8s that satisfies the condition.

For example, imagine a string that starts with 8 but has few 8s in the first window, but later has a window with many 8s. In that case, the earliest window may not satisfy the condition, but a later one does.

But the problem is that for a window starting at i, the first character is s[i]. So, to have a window starting with 8, i must be a position where s[i] is 8.

Thus, the code needs to check all possible windows starting with 8 and of length 11, and see if any of them has at least (k+1) 8s.

If there exists at least one such window, then Vasya can win.

Thus, the correct algorithm is:

Compute k = (n-11) // 2.

Check all positions i where s[i] is '8' and i <= (n-11). For each such i, check if the window from i to i+10 (inclusive) has at least (k+1) 8s. If any such i exists, output YES. Otherwise, NO.

This is the correct approach.

So the code can be written as follows.

Read n and s.

k = (n-11) // 2.

for i in range(len(s) - 10):

   if s[i] == '8':

       window = s[i:i+11]

       count = window.count('8')

       if count > k:

           print("YES")

           exit()

print("NO")

This code checks all possible windows of 11 characters starting with 8. If any of them has more than k 8s, output YES.

This is correct because:

- The window must be of length 11, so i can be from 0 to (n-11).

- The number of 8s in the window must be more than k. Because Petya can delete up to k of them.

Thus, the code is correct.

Now, considering the first sample input:

n=13, s=8380011223344.

The first character is 8. window is 83800112233 (the first 11 characters). The 8s are at positions 0 and 2. count is 2. k is 1. 2>1 → output YES.

Second sample:

n=15, s=807345619350641.

The first character is 8. window is 80734561935 (positions 0-10). count of 8s is 1. k=2 → 1>2 is false. Other 8s may exist, but if not, output NO.

So the code works.

Now, the code needs to be efficient. For large n (up to 1e5), the code checks up to (n-10) positions. For each, it creates a substring and counts the 8s. However, this can be optimized with a sliding window approach.

In Python, s[i:i+11].count('8') is O(11) per operation, which for n=1e5 would be O(1e5 * 11) = 1e6 operations, which is acceptable for time constraints.

Alternatively, precompute a prefix sum array of the number of 8s up to each index, then compute the count in O(1) per window.

This would optimize the time.

For example:

prefix = [0] * (n+1)

for i in range(n):

    prefix[i+1] = prefix[i] + (1 if s[i] == '8' else 0)

Then, for a window from i to i+10:

count = prefix[i+11] - prefix[i]

This is O(1) per window.

This is more efficient for large n.

Thus, the code can be optimized as follows:

Read n and s.

Compute prefix sums of 8s.

k = (n-11) // 2.

for i in range(n -10):

    if s[i] == '8':

        count = prefix[i+11] - prefix[i]

        if count > k:

            print("YES")

            exit()

print("NO")

This approach is O(n) time and O(n) space.

But since n is up to 1e5, this is acceptable.

Thus, the code with prefix sums is better.

So the code becomes:

Read n.

s = input().strip()

compute prefix.

then iterate.

This is the optimal approach.

So the code is:

n = int(input())

s = input().strip()

prefix = [0]*(n+1)

for i in range(n):

    prefix[i+1] = prefix[i] + (1 if s[i] == '8' else 0)

k = (n - 11) // 2

for i in range(n -10):

    if s[i] == '8':

        cnt = prefix[i+11] - prefix[i]

        if cnt > k:

            print("YES")

            exit()

print("NO")

Yes, this should work.

Let's test it against the examples.

First example:

n=13, s=8380011223344.

prefix is computed as follows:

indices 0: 1 (8), 1: 0 (3), 2:1 (8), etc. The sum up to i+11=11 is for i=0:

prefix[11] - prefix[0] = number of 8s in 0-10.

Which is 2.

k=1. 2>1 → output YES.

Second example:

n=15, s=807345619350641.

prefix[0+11] - prefix[0] is 1.

k=2. 1>2 is false. So no other window with 8 as first character. Output NO.

Thus, the code works.

Thus, this is the correct solution.
</think>

```python
n = int(input())
s = input().strip()

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + (1 if s[i] == '8' else 0)

k = (n - 11) // 2
for i in range(n - 10):
    if s[i] == '8':
        cnt = prefix[i+11] - prefix[i]
        if cnt > k:
            print("YES")
            exit()
print("NO")
```