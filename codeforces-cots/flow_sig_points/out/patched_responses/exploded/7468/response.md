<think>
Okay, let's try to figure out this problem. The problem is about a game between Ann and Mike where they take turns expanding a substring starting from position k. The expansion has to result in a lex smaller substring. Ann goes first, and the player who can't move loses. We need to determine for each possible k whether Ann or Mike will win if both play optimally.

Hmm. So the key here is to model the game as a series of moves where each move must lead to a lex smaller substring. The first player to have no moves loses. So for each position k, we need to compute if the starting player (Ann) has a winning strategy.

Let's think about the game rules. Each move expands the substring to include more characters on either or both ends. But the new substring must be lex smaller than the current one. The current substring starts as s[k..k], then in each step, it's replaced by a larger substring (since l' <= l and r' >= r, so the new substring includes all of the current plus possibly some more on the left and/or right) that is lex smaller.

The challenge is to model the game for each k. But considering that the string can be up to 5e5 characters, we need an O(n) or O(n log n) solution per k, which is impossible if we process each k naively. So we need a way to precompute some information for all k's efficiently.

Wait, but the problem requires processing all possible k's (each position in the string) and output the result for each. So the total time needs to be O(n) or O(n log n) overall.

Let's think about the game for a particular k. The initial substring is s[k], which is the single character at position k. Then, Ann's first move must be to choose a substring that includes this character and is lex smaller. But how?

Each possible expansion is a substring that includes the current substring. For example, the initial substring is s[k], so the next possible substrings are those that include s[k] and are longer. But wait, no: the next move can be any expansion (l' <= l, r' >= r) of the current substring, but the new substring must be lex smaller. So for the first move, Ann can choose any substring that starts at l' ≤ k and ends at r' ≥ k, such that the substring s[l', r'] is lex smaller than s[k].

Wait, but the initial l and r are both k. So the first move requires choosing l' ≤ k and r' ≥ k. So the new substring must start at l' which is ≤ k and end at r' which is ≥ k. So the substring s[l'..r'] is a superset of the initial substring.

But for the substring to be lex smaller than the initial, which is just s[k], the new substring must start with a character less than s[k]. Because when you compare lex order, the first differing character decides. So for example, if the new substring starts with a character less than s[k], then the entire substring is lex smaller. If the new substring starts with s[k], then the next character must be considered, but the original substring is just s[k], so the new substring (longer) would start with s[k], then have more characters. So in that case, the new substring is longer than the original (which is length 1), so the original would be considered smaller if the new starts with s[k] and adds more characters. Because, for example, "a" is lex smaller than "aa" or "ab" or any longer string starting with a. Wait, no. Wait, when comparing two strings of different lengths, the comparison is done up to the length of the shorter one. So if the original is "a" (length 1), and the new substring is "ab" (length 2), then the first character is 'a' in both. Then, since the original ends here, the new substring is longer. So "a" is considered lex smaller than "ab"? Wait, no. The lexicographical order compares the strings character by character. If the first min(len(a), len(b)) characters are equal, then the shorter string is considered smaller. So "a" is smaller than "ab". So the new substring must be lex smaller than the original. So in the first move, Ann needs to choose a substring that starts at l' <=k, ends at r' >=k, and s[l'..r'] is lex smaller than s[k].

So how can the new substring be lex smaller than s[k]?

If the first character of the new substring is less than s[k], then the entire substring is lex smaller, regardless of the rest. So if there's any position l' ≤ k such that s[l'] < s[k], then Ann can choose to take that l' and r' =k (so the substring is s[l'..k], which is a substring starting at l' and ending at k. Since l' <=k and r' =k >=k. The substring's first character is s[l'], which is less than s[k]. So this would be a valid move. Similarly, if there's a position r' >=k where s[r'] < s[k], then Ann can choose l' =k, r' =r where s[r'] < s[k]. Then the substring is s[k..r'], which starts with s[k] but has a longer length. Wait, but the first character is s[k], so the comparison would be s[k] (original) vs s[k] followed by other characters. Since the original is shorter, the original is considered smaller. So the new substring would be larger lex order. So that's not allowed.

Wait, this seems confusing. Let's clarify. Let's say the original substring is s[k], which is of length 1. The new substring must be lex smaller. So for the new substring to be lex smaller than the original, the first character of the new substring must be less than s[k]. Because if the first character is equal, then since the original is shorter, the original would be considered smaller, which would make the new substring larger. So in that case, the new substring is not allowed.

So the only way the new substring can be lex smaller than s[k] is if the first character of the new substring is less than s[k]. So Ann's first move must choose a substring that starts with a character less than s[k], which is the first character of the original substring.

Wait, but the new substring can be any expansion (l' ≤k, r' >=k). So the substring could start at some l' <=k and end at some r' >=k. But the first character of the substring is s[l'], which must be less than s[k]. Because the original substring is s[k], which is a single character. So the new substring's first character must be less than s[k], regardless of the rest of the characters. Because once the first character is less, the entire substring is lex smaller.

So for Ann to have a winning strategy, there must be at least one position l' <=k where s[l'] < s[k], or a position r' >=k where the first character (s[l'] where l' <=k) is less than s[k]. Wait, no. Because for the substring s[l'..r'], the first character is s[l'], which is the leftmost character. So regardless of where r' is, as long as l' is <=k, the substring starts at l'. So if l' is <=k, and s[l'] < s[k], then the substring starts with a smaller character, hence lex smaller. Similarly, if Ann chooses to expand to the right (l' =k, r' >=k), then the first character is s[k], which is the same as the original. But then, the original is length 1, the new substring is longer. So the original is considered lex smaller. So expanding to the right would not result in a lex smaller substring. So Ann can't choose to expand to the right unless there's a character in the left of the original that is smaller.

So the first move is possible only if there exists a l' <=k such that s[l'] < s[k]. Then, Ann can choose l' = the leftmost such position (for maximum expansion) or any such position, but the choice must allow her to have a winning strategy.

Wait, but the game is turn-based. Each player can choose any valid expansion. So the outcome depends on the possible moves and the game tree.

But the key insight here is that the first move determines the outcome. Because if Ann can make a move (i.e., choose a substring that is lex smaller), then Mike will have to make a move in response. But the problem is, once Ann chooses a substring, Mike's options are based on that new substring. However, the optimal play implies that if Ann can force a win, regardless of Mike's responses, then she will win.

But considering the constraints of the game, perhaps each move can only be made once. Let's think recursively: for a given current substring, the current player can choose any valid expansion (lex smaller) and the next player takes their turn. The player loses if they have no moves.

So the outcome for a position (current substring) is either a win (the current player can make a move leading to a loss for the next player) or a loss (no moves available).

But for the problem, the initial position is the substring s[k], and the players expand from there. So for each k, we need to compute the Grundy number or determine if the starting position is a winning or losing position.

But for a string of length up to 5e5, it's impossible to compute this for all possible substrings. So there must be a pattern or a way to precompute for each k whether Ann can win.

Let me think again. The key is the first move. Because if Ann cannot make any move (no possible expansion), then Ann loses, Mike wins. So for the initial substring s[k], if there's no l' <=k or r' >=k such that s[l'..r'] is lex smaller than s[k], then Ann can't move and loses.

If Ann can make a move, then she can choose a certain expansion. Let's suppose she chooses the leftmost possible l' (i.e., the earliest possible l' to the left of k where s[l'] < s[k], if such exists). Then the new substring is l' to k. Then Mike has to make a move, which must be a further expansion (since l'' <= l' and r'' >=k). But the new substring must be lex smaller than the previous one.

Wait, but the new substring after Ann's move is s[l'..r'], where l' <=k and r' >=k, and s[l'..r'] is lex smaller than s[k]. So the next move (Mike's) must choose a substring s[l''..r''] where l'' <= l' and r'' >= r' (since the new l and r are l' and r'). And s[l''..r''] must be lex smaller than s[l'..r'].

This seems like a chain. Each move must expand the substring and make it lex smaller. The game ends when no further expansion is possible.

But for each initial k, the game outcome depends on the number of possible moves, which is the length of this chain. If the number of moves is even, then Mike wins (since Ann starts first), if it's odd, Ann wins. But wait, no. Because each move is a choice, and players play optimally. So the outcome depends on whether the first player can force a win by choosing a move that leaves the second player in a losing position.

But perhaps the game can be modeled as a variant of the classic game of Nim, where each position is a losing or winning position. A winning position is one where the current player can make at least one move leading to a losing position for the next player. A losing position is one where all possible moves lead to winning positions for the next player.

But how to model this for our problem?

Alternatively, the game is a directed acyclic graph (DAG) where each node represents a substring (l, r), and edges represent possible moves. The outcome for each node (winning or losing) can be determined by whether there exists an edge to a losing node.

But with the substring being potentially any (l, r) pair, and the string length up to 5e5, this approach is impossible.

Thus, we need a way to compute for each k whether the initial position is a winning or losing position, considering the possible moves.

Let's think again about the initial move. For Ann to have a winning strategy, she must have at least one move that leaves Mike in a losing position.

But what determines if a position is a winning position?

The initial position is s[k]. To see if it's a winning position (Ann can win), we need to check if there's any possible expansion (l', r') such that the resulting position (l', r') is a losing position for Mike.

But how do we determine if (l', r') is a losing position?

This seems like a recursive problem. However, considering the constraints, this approach is not feasible. So perhaps there's a pattern that can be found by analyzing the problem.

Let's take the first example:

Input: abba.

Output for k=0 is Mike, k=1 is Ann, k=2 is Ann, k=3 is Mike.

Let's see.

For k=0 (s[0] is 'a'):

Ann's possible first moves are any substrings that start at l' <=0 and end at r' >=0. But since k=0 is the first character, l' can only be 0. Then, expanding to the right (r' >=0). But the substring must be lex smaller than 'a'. However, since 'a' is the smallest possible character, there are no such substrings. So Ann can't make a move. So Mike wins.

For k=1 (s[1] is 'b'):

Ann can look to the left (s[0] is 'a' < 'b'). So she can take l'=0 and r'=1, substring "ab", which is lex smaller than "b". Now, Mike's turn. He has to expand this substring to l'' <=0 and r'' >=1. The new substring must be lex smaller than "ab". So possible options are:

- Expand left: impossible (since 0 is already the left end).

- Expand right: take l''=0 and r''=2 (substring "abb") which is "abb". Compare "abb" to "ab". Since "ab" is the original (length 2), "abb" is longer. The first two characters are 'a' and 'b' in both, so the original "ab" is shorter and thus lex smaller. So "abb" is larger than "ab". So Mike can't expand to the right.

- Expand both: same as expanding right, no help.

Wait, but Mike's move must be to expand the current substring (l=0, r=1) to l' <=0 and r' >=1. So possible expansions:

The new substring must be lex smaller than "ab".

What's a possible way? Let's see. The new substring could be l''=0 and r''=1 (but that's the same as current, which is not allowed). Or l''=0 and r''=1 (same as current, which is invalid). Wait, the new l' and r' must satisfy l' <= l and r' >= r. But since l is 0, l' can't be less than 0. So l' must be 0. And r' must be >=1.

So Mike can choose r' >=1 (since l' is 0). So possible substrings are s[0..1], s[0..2], s[0..3].

But these substrings start with 'a', and the original substring is 'ab'. So for example, s[0..2] is 'abb'. Comparing to 'ab', which is length 2. Since 'abb' is longer, the first two characters are 'a' and 'b' for both. So the original is shorter and considered smaller. Therefore, the new substring 'abb' is larger than 'ab' (original), so it's not allowed. Similarly, s[0..3] is 'abba', which starts with 'ab', then 'b' and 'a'. So the original 'ab' is lex smaller. So Mike has no valid moves. So Ann's move leads to a losing position for Mike. So Ann can win. Hence, for k=1, Ann wins.

So the answer for k=1 is Ann.

This suggests that if the first move is possible, and the resulting position is a losing position (Mike can't move), then Ann wins.

So the question reduces to: for each k, can Ann make a move (i.e., there exists l' <=k where s[l'] < s[k])? If not, Mike wins. If yes, then the next question is: after making that move (like choosing the leftmost possible l' where s[l'] < s[k]), does Mike have any moves left? If not, then Ann wins. But if Mike can make another move, then the outcome depends on the parity of the number of possible moves.

But how can we model this efficiently?

Another angle: the game is a finite game. Each move expands the substring to include more characters. The maximum possible number of moves is O(n) for a particular k, but for n=5e5, this is impossible to compute for all k.

But perhaps the game can only have a certain number of moves based on the structure of the string. For example, the first player can make a move if there's a character to the left that's smaller. Then the second player can make a move only if there's a character to the left of the current l' that is smaller than the first character of the current substring. And so on. So each move is to expand to the left as far as possible, taking the earliest occurrence of a smaller character.

Wait, let's think: after the first move, the current substring is s[l'..r'], which starts with s[l']. Mike must expand to a substring that is lex smaller than s[l'..r']. To do that, he can expand to the left (if there's a character to the left of l' that is smaller than s[l']), or expand to the right (but then the first character remains s[l'], and since the substring is longer, it's lex larger, so expanding to the right won't work). So the only possible way to get a lex smaller substring is to expand to the left with a smaller character.

So the next move would require that there exists l'' <= l' such that s[l''] < s[l'].

This pattern continues. So the game can only proceed if there's a sequence of positions l0 =k, l1 < l0 where s[l1] < s[l0], l2 < l1 where s[l2] < s[l1], etc. Each step requires moving further left and finding a smaller character than the previous. The game ends when there's no such character.

Thus, the number of possible moves is determined by the length of this chain of decreasing characters. The player who makes the last move (i.e., the chain length is even or odd) will determine the outcome.

For example, if the chain length is 1 (Ann makes a move, Mike can't), Ann wins. If chain length is 2 (Ann makes first, Mike makes second, Ann can't), Mike wins. So the outcome depends on whether the chain length is even or odd.

So the problem reduces to finding, for each k, the length of the longest possible chain of characters starting at k and moving left, each time finding a smaller character than the previous in the chain. The parity of this chain length determines the winner.

Wait, but this chain is the maximum possible moves. Because each player can choose any possible expansion, but to maximize the number of moves (if needed) or to minimize (depending on what's needed to win). But since players play optimally, they will choose the path that leads to their victory.

So if the maximum possible chain length is even, then Ann wins (since she starts first and takes the first step, Mike takes the next, etc., until even steps). Wait, no. Let's see. For example:

Chain length 1: Ann takes step 1, no more steps. Mike can't. Ann wins.

Chain length 2: Ann steps (1), Mike steps (2). No more steps. Ann can't. Mike wins.

So the outcome depends on whether the chain length is even or odd. But this is only if the chain can be traversed in such a way. So if the maximum possible chain is even steps, then Mike wins. If it's odd, Ann wins.

But how to model the chain for each k?

The chain for k is the number of steps you can take moving left, each time finding a smaller character than the previous. For example:

For k, check the first position to the left of k where s[i] < s[k]. Then, from that position, check the first position to the left of i where s[j] < s[i], and so on. The length of this chain is the number of steps possible.

So for each k, the chain length is the number of steps possible. If the chain length is zero (no possible first move), Ann loses. Otherwise, if the chain length is even, Mike wins, else Ann wins.

Wait, but what about the chain length being 1. For example, Ann takes step 1 (chain length 1), then Mike can't move. So Ann wins. So chain length 1 (odd) → Ann wins.

If chain length is 2 (Ann takes step 1, Mike takes step 2 → chain length 2 even. Then Ann can't move. So Mike wins. So parity of the chain length determines the outcome.

Thus, the solution would be for each k, compute the length of the chain (number of steps possible), and then if the chain is even, Mike wins, else Ann wins.

But how to compute this chain length for each k efficiently?

We can precompute for each position k, the minimum character to the left of k (including k) up to that point. Wait, but that might not capture the steps.

Alternatively, for each position k, we need to find the leftmost occurrence of a character less than s[k], then from that position, find the next leftmost occurrence less than that character, and so on.

But this would be O(n^2) in the worst case, which is not feasible.

So we need a way to precompute for each position k, the maximum possible chain length.

Hmm. Let's think about the chain. Each step requires moving left to a position with a smaller character. So the chain is a sequence of indices l_0 =k, l_1 < l_0 where s[l_1] < s[l_0], l_2 < l_1 where s[l_2] < s[l_1], etc. The maximum possible chain is determined by how many steps can be taken in this way.

The problem is similar to finding for each position the length of the longest decreasing subsequence to the left, but each step must be strictly decreasing and each next step must be to the left.

Wait, no. Because the chain steps must form a sequence where each element is the first occurrence to the left that is smaller than the current. For example, for k=3 in 'abba' (s[3] is 'a'), the chain would be empty, because there's no left character less than 'a'. So Ann can't make a move. So Mike wins.

But for k=2 in 'abba' (s[2] is 'b'), the left characters are s[1] = 'b', s[0] = 'a'. So the first step is l'=0 (since s[0] < s[2] (a < b). Then, from l'=0, there's no further left characters (since 0 is the first position). So chain length is 1. So Ann can make one move, then Mike can't. So Ann wins.

So the chain length is 1 for k=2, which is odd → Ann wins.

Thus, the approach is:

For each k:

1. Check if there exists a character to the left (i < k) with s[i] < s[k]. If not, Ann can't make any moves, so Mike wins.

2. If there is such a character, then the chain starts. The chain length is the number of steps possible, each time moving left to the first occurrence of a smaller character than the previous.

The key is to find the maximum possible chain length starting from k, moving left each time.

The chain length is the number of steps possible. If it's odd, Ann wins. Even, Mike wins.

But how to compute this for all k efficiently?

Let's think of precomputing for each position the next smaller element to the left, but in a way that allows us to compute the chain lengths in O(1) per position.

This is similar to the "monotonic stack" approach used in problems like the next greater element.

But how?

Alternative idea: For each position i, let's find the nearest index j < i where s[j] < s[i]. Then, for position i, the chain length would be 1 + chain[j]. Because once you move to j, the chain length is 1 (current step) plus the chain length of j.

But wait, let's think. For position i, the first step is to j. Then, from j, the next step is to the nearest k < j where s[k] < s[j]. So the chain length for i is 1 plus the chain length of j. If j is such that s[j] < s[i], then chain[i] = chain[j] + 1.

But if there's no j where s[j] < s[i], then chain[i] = 0.

Wait, but in the example of 'abba', for k=1 (s[1] = 'b'), the first j is 0 (s[0] = 'a' < 'b'). Then, chain[1] = 1 + chain[0]. What is chain[0]?

For i=0, there are no elements to the left, so chain[0] = 0. So chain[1] = 1+0=1. So the chain length is 1, which is odd → Ann wins.

Similarly, for k=2 (s[2] = 'b'), the first j is 0. chain[2] = 1 + chain[0] =1 → odd, Ann wins.

For k=3 (s[3] = 'a'), there's no j <3 with s[j] < 'a'. So chain[3] =0 → even steps (0) → Mike wins.

This seems to fit the example.

So the chain for each position i is:

chain[i] = 0 if no j <i with s[j] < s[i].

Else, chain[i] = chain[j] +1, where j is the first position to the left of i where s[j] < s[i].

But wait, j could be any position left of i with s[j] < s[i]. But for the maximum chain length, we need to choose the j that gives the longest possible chain.

Wait, but this approach assumes that j is the first position to the left of i where s[j] is smaller than s[i]. But perhaps there's a j' further left than j where s[j'] < s[i], and chain[j'] is longer. For example:

Suppose i=4, and the characters are a, b, c, d, e.

The chain for i=4 would be 0, since there's no j <4 with s[j] < e.

But if the characters are c, b, a, d, e. Then for i=3 (s[i] =d), the left positions j where s[j] <d are 0,1,2. Choosing j=2 (a) would give chain[3] = 1 + chain[2]. chain[2] is 0 (no j <2 where s[j] <a). So chain[3] =1. But if there's another j (say j=1, s[j] =b <d), then chain[1] could be 1 (if there's a j <1 where s[j] <b), leading to chain[3] =1 +1=2. So choosing the j that gives the maximum chain[j] would maximize the chain[i].

But this complicates the approach because we have to consider all possible j <i where s[j] <s[i], and select the one that gives the maximum chain[j] +1. However, this would require O(n^2) time, which is not feasible for n=5e5.

But perhaps there's a way to find the j that gives the maximum chain[j] for each i. How?

Alternatively, if we can find the minimal s[j] to the left of i, then perhaps the chain[j] would be the longest possible. But I'm not sure.

Alternatively, perhaps the chain[i] is determined by the first occurrence of a character smaller than s[i], but the chain length is cumulative. But how?

Wait, let's take the example where s is "cba".

For i=0 (c), chain is 0.

i=1 (b): j=0 (c) is not smaller than b. So chain[1] is 0.

i=2 (a): j=1 (b) is not smaller than a. j=0 (c) also not. So chain[2] is 0.

So all positions have chain length 0. So Ann can't make any moves. So all outputs are Mike. Which matches the second sample.

So this approach seems to work for the samples.

Another example: s = "abcab".

For i=0: chain[0] =0.

i=1: find j=0 (a <b). chain[1] =0+1=1.

i=2: find j=1 (b <c). chain[2] =1+1=2.

i=3: find j=2 (c >a, so look further). j=1 (b >a). j=0 (a ==a, not smaller. So no j. So chain[3] =0.

i=4: find j=3 (a <b). chain[4] =0 +1=1.

So for each k, the chain length is:

k=0: 0 → Mike.

k=1:1 → Ann.

k=2:2 → Mike.

k=3:0 → Mike.

k=4:1 → Ann.

So the output would be Mike, Ann, Mike, Mike, Ann.

So for k=1, Ann can make one move (chain length 1, odd → wins). For k=2, chain length 2 → even, Mike wins.

This seems to fit.

Thus, the approach is to precompute for each i the chain[i] as follows:

chain[i] = 0 if there is no j <i where s[j] < s[i].

Otherwise, chain[i] = chain[j] +1, where j is the last position to the left of i where s[j] < s[i].

Wait, but how to find j?

If we use a monotonic stack to find, for each i, the previous smaller element (PSE), then j would be the PSE of i. The PSE is the nearest element to the left of i that is smaller than s[i]. Then, for each i, j is the PSE. If no such j exists, then chain[i] is 0. Otherwise, chain[i] is chain[j]+1.

So the problem reduces to computing the chain array, where each chain[i] is computed based on the PSE of i.

This can be done efficiently using a stack.

Let me think about how to compute the previous smaller element for each index.

The standard approach for previous smaller element is to use a stack that keeps track of elements in decreasing order.

Initialize an empty stack. For each index i from 0 to n-1:

- While the stack is not empty and the top element >= s[i], pop from the stack.

- The PSE of i is the index at the top of the stack if the stack is not empty. Otherwise, no PSE exists.

- Push the current index i onto the stack.

But the stack would store indices, and we compare s[stack.top()] with s[i].

Yes. So for each i, we can find the previous smaller element's index j. If such a j exists, then chain[i] = chain[j] +1. Otherwise, chain[i] =0.

Once we have this chain array, then for each k, the answer is Ann if chain[k] is odd, Mike otherwise (since chain[k] is the number of steps possible). Because chain[k] represents the maximum possible steps that can be taken. For example, if chain[k] is 1, Ann takes 1 step (chain[k] is 1), and Mike can't proceed. So Ann wins.

But wait, chain[k] is the maximum possible steps. So for each k, the number of moves possible is chain[k]. Because each step in the chain corresponds to a move. So if chain[k] is 0 → no moves. Ann loses. If 1 → one move (Ann's move). Mike can't move. So Ann wins. If 2 → Ann makes first move, Mike makes second. Then Ann can't. So Mike wins. So the winner is determined by whether chain[k] is even or odd. Even → Mike wins. Odd → Ann wins.

Thus, the solution is:

For each k in 0..n-1:

- If chain[k] ==0 → Mike.

- Else, if chain[k] is odd → Ann.

- Else → Mike.

So, the plan is:

1. Compute the previous smaller element (PSE) for each index i.

2. Compute the chain array using the PSE. For each i, chain[i] = 0 if no PSE, else chain[PSE[i]] +1.

3. For each k, output Ann if chain[k] is odd, else Mike.

Now, the key steps are:

- Compute the PSE for all indices.

- Compute the chain array.

Now, let's test this approach with the first sample.

Sample 1:

s = 'abba' → indices 0:a, 1:b, 2:b, 3:a.

Compute PSE for each index:

i=0:

Stack is empty. PSE[i] = -1. chain[0] =0.

Stack pushes 0.

i=1:

s[1] =b. Stack top is 0 (a <b). So PSE[1] =0. chain[1] = chain[0] +1 =0+1=1. Push 1.

i=2:

s[2]=b. Stack top is 1 (s[1]=b == s[2], so pop. Stack becomes [0]. s[0] =a <b. So PSE[2]=0. chain[2]=chain[0]+1=1. Push 2.

i=3:

s[3]=a. Stack top is 2 (s[2]=b >=a → pop. Stack becomes [1]. s[1]=b >=a → pop. Stack becomes [0]. s[0]=a >=a → pop. Stack empty. PSE[3] = -1. chain[3] =0. Push 3.

So chain array is [0,1,1,0].

For each k:

k=0 → chain 0 → Mike.

k=1 → chain 1 (odd) → Ann.

k=2 → chain 1 (odd) → Ann.

k=3 → chain 0 → Mike.

Which matches the sample.

Sample 2:

s = 'cba' → indices 0:c, 1:b, 2:a.

Compute PSE:

i=0: stack empty → PSE -1. chain 0. push 0.

i=1: s= b. stack top is 0 (c >b → pop. stack empty. PSE -1. chain 0. push 1.

i=2: s=a. stack top is 1 (b >a → pop. stack empty. PSE -1. chain 0. push 2.

So chain array is [0,0,0]. All Mike.

Which matches the second sample.

Thus, the approach seems correct.

Now, the implementation steps:

1. Precompute PSE for each index.

2. Compute chain array.

3. For each index k, output Ann if chain[k] is odd, else Mike.

Implementing this in Python.

But for large n (5e5), we need an O(n) solution for both PSE and chain.

Implementing the PSE using a stack.

Then, chain is computed in O(n) time as well.

Now, code steps:

Read the string s.

Compute PSE for each i:

Initialize stack as empty.

pse = [ -1 for _ in range(n) ]

for i in range(n):

    while stack and s[ stack[-1] ] >= s[i]:

        stack.pop()

    if stack:

        pse[i] = stack[-1]

    else:

        pse[i] = -1

    stack.append(i)

Then compute chain[i] for each i.

chain = [0]*n

for i in range(n):

    if pse[i] == -1:

        chain[i] =0

    else:

        chain[i] = chain[ pse[i] ] +1

Then, for each i:

if chain[i] ==0 → Mike.

else, if chain[i] %2 ==1 → Ann.

else → Mike.

Thus, code:

s = input().strip()

n = len(s)

pse = [ -1 ] * n

stack = []

for i in range(n):

    # current char is s[i]

    while stack and s[ stack[-1] ] >= s[i]:

        stack.pop()

    if stack:

        pse[i] = stack[-1]

    else:

        pse[i] = -1

    stack.append(i)

chain = [0]*n

for i in range(n):

    if pse[i] == -1:

        chain[i] =0

    else:

        chain[i] = chain[ pse[i] ] +1

for c in chain:

    if c ==0:

        print("Mike")

    else:

        print("Ann" if c %2 ==1 else "Mike")

But let's test this code on the first sample.

Sample1:

s = 'abba'

chain for each index:

0: pse[0] is -1 → chain[0] =0.

1: pse[1] is0 → chain[0] +1 → 1.

2: pse[2] is0 → chain[0] +1 → 1.

3: pse[3] is-1 → 0.

Outputs:

0 → Mike.

1 → Ann.

1 → Ann.

0 → Mike.

Which is correct.

Sample2:

s='cba' → chain all 0 → all Mike. Correct.

Another test case: 'abcab'.

The chain array would be:

0: 0 → Mike.

1:0's pse is0 → chain[0] is0 → 1 → Ann.

2: pse[2] is1 → chain[1] is1 → 2 → Mike.

3: pse[3] is-1 →0 → Mike.

4: pse[4] is3 → chain[3] is0 →1 → Ann.

So outputs for indices 0-4:

Mike, Ann, Mike, Mike, Ann.

Which aligns with the earlier analysis.

Thus, this code should work.
</think>

```python
s = input().strip()
n = len(s)
pse = [-1] * n
stack = []

for i in range(n):
    while stack and s[stack[-1]] >= s[i]:
        stack.pop()
    if stack:
        pse[i] = stack[-1]
    stack.append(i)

chain = [0] * n
for i in range(n):
    if pse[i] != -1:
        chain[i] = chain[pse[i]] + 1

for c in chain:
    print("Ann" if c % 2 else "Mike")
```