<think>
Okay, let's see. So the problem is about two players, Yaroslav and Andrey, playing a game where they choose positions from a string of 2n characters each. They take turns picking positions, and then each builds their own binary number by rearranging the bits they collected. The goal is to determine who wins when both play optimally.

Hmm. The first thing I need to understand is how the optimal play works here. Since both players can arrange their bits in any order, their best strategy is to maximize their own number and minimize the opponent's. But since they alternate turns, they have to choose positions that will give them the best possible outcome considering the other's optimal choices.

Wait, but how do their choices affect the final bits? Let's think. Each chosen position contributes a bit to either Yaroslav's or Andrey's collection. The selection is such that each position can be chosen only once. So during the game, the players are selecting positions, and each position gives one bit to the player who picked it.

So for each turn, the player picks a position that's not taken yet. The key here is that when a player selects a position k, they add s_k (if Yaroslav) or t_k (if Andrey) to their own bits. Then, after all positions are taken, each player sorts their bits to form the largest possible number. For example, if Yaroslav has bits 1, 0, 1, he can arrange them as 110, which is 6 in binary.

The problem is to determine the outcome given that both play optimally. The answer is whether the first player (Yaroslav) can force a win, the second (Andrey) can, or it's a draw.

So the challenge is to model this game and find the optimal strategy for both players. Let's break down the problem.

First, note that the game is turn-based with 2n rounds (since each of the 2n positions is chosen once). Since Yaroslav starts first, he picks positions on the 1st, 3rd, 5th, etc., turns, while Andrey picks on the even turns.

Each time a player picks a position, they add a bit to their collection and deny that position to the other. So the selection of which positions to take is crucial. The optimal play would involve selecting positions that maximize the player's own maximum possible number while minimizing the opponent's.

But how do we model this optimally, especially given the constraints of n up to 1e6, which suggests that any O(n^2) approach is impossible. So we need an O(n) or O(n log n) solution.

Hmm. Let's think about the possible approach.

The key observation here is that each position contributes a pair of bits (s_i, t_i). For each position i, when it's chosen by a player, they add their own bit (s_i if Yaroslav, t_i if Andrey) to their collection. The other player's bit for that position is irrelevant once the position is taken.

But how do the players choose which positions to take? Since the players can choose any remaining position, the optimal strategy would involve selecting the position that gives the best advantage.

Wait, but maybe the optimal strategy can be determined by considering the combined value of each position in a certain way. For example, for each position i, the pair (s_i, t_i) determines how important that position is. The players want to take the most valuable positions first.

Alternatively, perhaps the players will prioritize positions where their own bit is 1 over those where it's 0. But also, they might want to deny the opponent their 1 bits.

But how to model this? Let's think in terms of the combined values. For each position, when it's chosen by Yaroslav, he adds s_i to his bits, and Andrey can't get t_i. Conversely, if Andrey chooses it, he adds t_i and Yaroslav can't get s_i. So each position's contribution depends on who takes it.

This feels like a game where the players are trying to maximize their own sum (in terms of the binary digits, but arranged in order). But since the order can be rearranged, the number of 1's is the most important. Because a higher number of 1's leads to a larger number when arranged in order (since all 1's come first). So the optimal number for a player is determined by the count of 1's in their collected bits. For example, if a player has x 1's, their number is 1 followed by x-1 1's and then the 0's, which is the maximum possible.

Wait, wait! Wait a second. Because when you can arrange the bits in any order, the maximum possible number is simply all the 1's first, then all the 0's. So the value of the number is determined by the count of 1's. For example, 3 ones and 2 zeros would give 11100, which is 28 in decimal. So the key for each player is to collect as many 1's as possible. The actual order in which they are collected doesn't matter; only the count of 1's. Because when you can arrange them optimally, the count of 1's determines the maximum number. So for two players, the number of 1's each has determines the outcome.

Wait, this seems like a crucial insight. Because then, the problem reduces to each player trying to maximize their own count of 1's, and minimize the opponent's. So the game is really about how many 1's each can collect, considering that when a position is taken by one, the other cannot take it. But the 1's each player can get are determined by which positions they choose. So for each position i, if Yaroslav takes it, he gains s_i, and Andrey gains nothing from it. If Andrey takes it, he gains t_i, and Yaroslav gains nothing from it.

So the core of the problem is to model the selection of positions such that each player alternately picks positions, trying to maximize their own 1's minus the opponent's 1's (or some other measure). But given that the selection is turn-based, we need to find the optimal way to pick positions so that the difference between the two players' 1's is maximized (for the first player) or minimized (for the second player).

But how can we model this efficiently? Let's think about the priority of each position. For each position i, we can compute a certain value that represents how beneficial it is for the players to take it. The players would prioritize the positions with the highest such value.

But what is that value? Let's see. For position i, if Yaroslav takes it, he gains s_i (0 or 1) and Andrey doesn't get t_i. If Andrey takes it, he gains t_i (0 or 1) and Yaroslav doesn't get s_i. So the combined impact of choosing this position is (s_i + (1 - t_i)) for Yaroslav's choice, or (t_i + (1 - s_i)) for Andrey's choice. Wait, maybe not. Let me think again.

Alternatively, the value of position i could be (s_i + t_i). Because when a player takes this position, they can get their bit, and the other can't. But maybe positions where both s_i and t_i are 1 are very valuable, since taking them gives a 1 to the taker and denies a 1 to the other. But how?

Wait, perhaps the optimal strategy can be determined by sorting the positions based on the sum (s_i + t_i), but in a certain order. Let's think: for a given position, if s_i + t_i is 2 (both 1), then if Yaroslav takes it, he gains 1 and Andrey loses 1 (since he can't take it). So the net gain for Yaroslav is 2. Similarly, if Andrey takes it, he gains 1 and Yaroslav loses 1 (since s_i was 1, but Yaroslav didn't take it). So the net gain for Andrey is 2. So positions where both bits are 1 are very important.

Similarly, positions where s_i is 1 and t_i is 0: if Yaroslav takes it, he gains 1, Andrey gains 0. If Andrey takes it, he gains 0, and Yaroslav can't gain 1. So the net gain for Yaroslav taking it is 1, and if Andrey takes it, the net loss for Yaroslav is 1.

So the priority of the positions depends on the sum (s_i + t_i), and the difference between the two. So perhaps the positions should be sorted in a way that those with higher (s_i + t_i) are picked first, and then for positions with the same sum, the ones where (s_i - t_i) is higher are taken first.

So the idea is to sort all positions in a certain order, and then simulate the players taking the positions in that order, alternating turns. Since the players are trying to maximize their own advantage, they will pick the most valuable positions first.

If we can find the correct order to sort the positions, then the optimal play can be simulated by taking the positions in that order, with Yaroslav and Andrey picking alternately.

So the steps would be:

1. For each position i (from 0 to 2n-1), compute the pair (s_i, t_i). Then, sort all positions in a certain order that represents their priority.

2. Then, iterate through the sorted list. For each position, assign it to Yaroslav or Andrey based on whose turn it is. For each assigned position, add s_i to Yaroslav's count if it's his turn, or t_i to Andrey's count if it's his turn.

3. After all positions are processed, compare the total counts of 1's for each player. If Yaroslav's count is higher, he wins. If lower, then Andrey. If equal, draw.

But how to determine the correct order for sorting the positions?

The key is to find the order that maximizes the outcome for the first player (Yaroslav) when both play optimally. The optimal play would involve selecting the next best available position each turn.

So the sorting order should be such that the positions are considered in the order of their contribution to the maximum possible advantage. For each position, the priority is determined by the impact it has when it's chosen by the current player.

Let's think of each position as having a priority based on (s_i + t_i). Positions where s_i + t_i is 2 (both 1) are the highest priority. For these positions, whichever player takes them gains 1, and the other loses 1. So the net gain is 2 for the taker. So these are the most valuable positions. Next, positions where one of s_i or t_i is 1, and the other is 0. For example, s_i=1, t_i=0: if Yaroslav takes it, he gains 1 and Andrey gains 0. If Andrey takes it, he gains 0 and Yaroslav loses 1. So the net gain is 1 for the taker. Similarly, if s_i is 0 and t_i is 1, then for Yaroslav, taking it gains 0, but denying Andrey 1, so net gain is 1. Positions where both are 0 contribute nothing and can be considered last.

So the priority order is:

- First, positions where (s_i + t_i) is 2. These should be sorted in such a way that when both players can take them, the order of selection is optimal. But wait, when (s_i and t_i are both 1), whichever player takes the position gains 1 and the other loses 1. So these are critical. The order in which these are chosen may determine the outcome.

But how to sort these? For these positions, the difference (s_i - t_i) is 0. So maybe for positions where s_i + t_i is 2, the order between them doesn't matter. But when there are multiple such positions, the players will alternate taking them, starting with Yaroslav.

But then, after that, positions where s_i + t_i is 1. For these positions, which player's bit is 1? For example, (1,0) or (0,1). For (1,0), if Yaroslav takes it, he gains 1. If Andrey takes it, he gains 0. So Yaroslav would want to take this. For (0,1), if Yaroslav takes it, he gains 0, but Andrey would have taken it to gain 1. So in this case, the order matters. So perhaps the priority for s_i + t_i =1 is based on (s_i - t_i). For (1,0), s_i - t_i is 1. For (0,1), it's -1. So positions where (s_i - t_i) is higher (like 1) should be taken first.

So the sorting order would first sort by the sum (s_i + t_i) in descending order, then by (s_i - t_i) in descending order. So for positions with sum 2, they are all grouped first. Then for sum 1, they are sorted by (s_i - t_i) in descending order. Then sum 0 (both 0) are last.

By sorting in this way, the players can take the highest priority positions first, leading to optimal play.

Let's test this with the first example:

Input:
n=2
s=0111 (positions 0,1,2,3: s is '0','1','1','1')
t=0001 (t is '0','0','0','1')

The pairs for each position are:

0: (0,0) sum 0, s-t=0-0=0
1: (1,0) sum 1, s-t=1
2: (1,0) sum 1, s-t=1
3: (1,1) sum 2, s-t=0

So the sorted list will first have position 3 (sum 2), then positions 1 and 2 (sum 1, s-t 1), then 0 (sum 0). So sorted order is 3, 1, 2, 0.

The game proceeds as follows:

Total positions:4.

Players take turns in order: Yaroslav picks first, then Andrey, then Yaroslav, then Andrey.

So the order of selection is:

First turn (Yaroslav) picks position 3 (sum 2). He gains s[3] = '1'. His count is 1. Andrey can't take this position.

Second turn (Andrey) picks next highest position, which is 1 (sum 1). He gains t[1] = '0'. His count remains 0.

Third turn (Yaroslav) picks position 2. He gains s[2] = '1'. His count is 2.

Fourth turn (Andrey) picks position 0. He gains t[0] = '0'. His count remains 0.

So Yaroslav has 2 ones, Andrey has 0. Yaroslav wins. Which matches the sample output.

Another example: the third sample input.

Input:
3
111000
000111

s is '1','1','1','0','0','0'
t is '0','0','0','1','1','1'

Each position's pair:

0: (1,0) sum 1, s-t=1
1: (1,0) sum 1, s-t=1
2: (1,0) sum 1, s-t=1
3: (0,1) sum 1, s-t=-1
4: (0,1) sum 1, s-t=-1
5: (0,1) sum 1, s-t=-1

So when sorted by sum (all sum 1), then by (s-t) in descending order. So positions 0,1,2 come first (s-t 1), then 3,4,5 (s-t -1).

The sorted order is 0,1,2,3,4,5.

Now, the players alternate:

Yaroslav picks 0 (sum 1, s-t 1) → gains 1.

Andrey picks 1 (sum 1, s-t 1) → but wait, how are the positions ordered? The sorted list is [0,1,2,3,4,5]. So first turn: Yaroslav picks 0 (s=1). Second turn: Andrey picks 1 (s=1 for Yaroslav, but Andrey is taking it. So t[1] is 0. So Andrey gains 0. Third turn: Yaroslav picks 2 (s=1). Fourth turn: Andrey picks 3 (t=1). Fifth turn: Yaroslav picks 4 (t=1, but when he picks it, he gains s[4] =0. Sixth turn: Andrey picks 5 (s=0, t=1. Andrey gains 1.

So let's see:

Yaroslav's bits: positions 0 (1), 2 (1), 4 (0) → total 2 ones.

Andrey's bits: positions 1 (0), 3 (1),5 (1) → total 2 ones.

So it's a draw. Which matches the sample.

So this approach seems to work.

Therefore, the plan is:

1. Generate a list of all positions (0 to 2n-1).

2. For each position, compute (s_i, t_i).

3. Sort the positions in the following order:

   a. First, by the sum (s_i + t_i) in descending order.

   b. Then, for positions with the same sum, sort by (s_i - t_i) in descending order.

4. Then, iterate through the sorted list, and for each position, assign it to Yaroslav or Andrey in turn (Yaroslav first, then Andrey, etc.).

5. Count the number of 1's each gets from their own string in the positions they chose.

6. Compare the counts:

   - If Yaroslav's count > Andrey's: output "First".

   - If less: "Second".

   - Equal: "Draw".

But wait, how does the assignment work? Since the players take turns in the order of the sorted list. So the first position in the sorted list is taken by Yaroslav (first turn), the next by Andrey (second turn), the third by Yaroslav, and so on.

Yes. Because the players take turns, and the order of selection is determined by the sorted list. The optimal play is to take the highest priority available position each time.

So the algorithm is:

Sort the positions according to the priority, then assign them in order, alternating between Yaroslav and Andrey.

Now, the challenge is to implement this efficiently for n up to 1e6, which implies 2e6 positions.

The steps in code would be:

- Read n.

- Read s and t as strings.

- Create a list of tuples for each position i (0-based), with elements (s_val, t_val), where s_val is int(s[i]), t_val is int(t[i]).

- Sort the list of tuples based on the criteria mentioned.

But how to do the sorting efficiently? The key for each element is (- (s_val + t_val), - (s_val - t_val)). Because we want to sort in descending order of sum, then descending order of (s_val - t_val).

So in Python, the sorted list can be generated by:

sorted_list = sorted( range(2*n), key=lambda i: ( - (int(s[i]) + int(t[i])), - (int(s[i]) - int(t[i])) ) )

But for n=1e6, 2n=2e6 elements. Sorting 2e6 elements in Python can be done in O(n log n) time, which for 2e6 is manageable, but we need to make sure it's efficient.

Alternatively, perhaps using list comprehensions and precomputing the keys as tuples.

Once the sorted list is generated, we iterate through it, and for each index in the sorted list, assign it to Yaroslav or Andrey. For each even index (0-based) in the sorted_list (i.e., first, third, etc.), Yaroslav takes that position, and adds s[i] to his count. For each odd index, Andrey takes it, adding t[i] to his count.

Wait, no. The sorted list is a list of the positions in order of priority. Then, the order of selection is Yaroslav picks the first element (sorted_list[0]), Andrey picks the second (sorted_list[1]), Yaroslav picks the third (sorted_list[2]), and so on.

So for each index j in the sorted_list:

if j is even (0,2,4,...) → Yaroslav's turn.

if j is odd → Andrey's turn.

So for each position i in the sorted_list, during the j-th step (starting from 0), if j is even, Yaroslav takes i, and his count += s[i].

If j is odd, Andrey takes i, count += t[i].

So in code:

y_count = 0

a_count = 0

for idx, pos in enumerate(sorted_positions):

    if idx % 2 == 0:  # Yaroslav's turn

        y_count += int(s[pos])

    else:

        a_count += int(t[pos])

Then compare y_count and a_count.

So the code needs to:

Read n.

Read s and t.

Generate sorted_positions as per the key.

Compute the counts.

Compare.

This approach should handle all test cases efficiently.

Now, considering the constraints, 2n can be up to 2e6. Sorting 2e6 elements in Python is acceptable, as the O(n log n) time for 2e6 elements is manageable. The key for each element can be computed quickly.

But in Python, creating a list of tuples for each position (like (sum, s-t)) and then sorting might be efficient enough.

Alternatively, since for each position i, the key can be generated as a tuple (- (s[i] + t[i]), - (s[i] - t[i])), which can be used to sort the indices.

But converting each character in the strings to integers for 2e6 elements might take some time, but it's manageable.

Wait, but in Python, the strings s and t are already in memory. So for each position i, s[i] is a character '0' or '1', and similarly for t[i]. So converting them to integers can be done on the fly when computing the key.

But during the sorted key generation, for each i in 0..2n-1, the key is (- (s_i + t_i), - (s_i - t_i)), where s_i is int(s[i]), t_i is int(t[i]).

So in Python, the code for generating the sorted list would be:

sorted_positions = sorted(range(2*n), key=lambda i: (-(int(s[i]) + int(t[i])), -(int(s[i]) - int(t[i]))) )

Yes.

This should work.

But for 2e6 elements, this lambda function is called 2e6 times. Each time, it converts two characters to integers. But this is O(1) per call, so the total time is acceptable.

Once the positions are sorted, then iterate through them, and for each, add to the counts based on the turn.

Now, let's test this with the first example.

Sample Input 1:

n=2

s=0111 → '0','1','1','1'

t=0001 → '0','0','0','1'

positions are 0,1,2,3.

sorted by key:

For each position i:

i=0: s=0, t=0. sum=0. s-t=0. key is (-0, -0) → (0,0).

i=1: s=1, t=0. sum=1. s-t=1. key: (-1, -1) → (-1,-1).

Wait, no. Wait the key is (- (sum), - (s-t)).

Wait for i=1: sum is 1 + 0 =1. key's first component is -1. s-t is 1-0=1. second component is -1. So the key is (-1, -1). Wait wait, no: the lambda is:

lambda i: ( -(int(s[i]) + int(t[i])), -(int(s[i]) - int(t[i])) )

So for i=1:

int(s[i]) =1, int(t[i])=0.

sum is 1+0=1 → -(1) =-1.

s-t is 1-0=1 → -(1) =-1. So the key is (-1, -1).

Similarly for i=2, same as i=1. sum 1, s-t 1 → key (-1,-1).

i=3: sum 1+1=2 → -2. s-t=0 → -0=0. key is (-2, 0).

So the keys for each position are:

0 → (0, 0)

1 → (-1, -1)

2 → (-1, -1)

3 → (-2, 0)

When sorted in Python, the sorted function will order the keys in ascending order. So the tuple with the smallest first component comes first, then if equal, the smallest second component.

So for the keys:

position 3's key is (-2, 0) → first component is -2, which is the smallest, so it comes first.

positions 1 and 2 have keys (-1, -1), which are next. Then position 0 (0,0) comes last.

Wait, but sorted in ascending order. So the order would be:

-2 → smallest, comes first.

-1 next.

0 comes after.

So the sorted order of positions is 3, 1, 2, 0.

Then, during the iteration:

index 0 (Yaroslav's turn) → position 3. s[3] is 1 → y_count=1.

index 1 (Andrey's turn) → position1. t[1] is 0 → a_count=0.

index2 (Yaroslav's turn) → position2. s[2] is1 → y_count=2.

index3 (Andrey's turn) → position0. t[0] is0 → a_count remains 0.

Total: 2 vs 0 → First.

Which matches the sample.

So this approach works.

Another sample: input 3.

s is 111000 (positions 0-5: s is '1','1','1','0','0','0').

t is 000111 (positions 0-5: t is '0','0','0','1','1','1').

sum for each position:

i=0: s=1, t=0 → sum=1 → key (-1, -(1-0)= -1 → key (-1, -1).

i=1: same as i=0.

i=2: same as i=0.

i=3: s=0, t=1 → sum=1 → key (-1, -(0-1)=1 → key (-1,1).

i=4: same as i=3.

i=5: same as i=3.

So when sorted, the positions are:

For sum 1, the key is (-1, ...).

For i=0,1,2: key is (-1, -1).

For i=3,4,5: key is (-1, 1).

Comparing these keys:

For two positions with sum 1, the second component is sorted in ascending order. So (-1, -1) comes before (-1, 1) because -1 is smaller than 1.

So the order is:

i=0,1,2 (sorted between themselves, but their keys are same), followed by i=3,4,5.

But when sorted, the positions are ordered in the way that the key is sorted. So for i=0,1,2, their keys are all (-1, -1). So their order in the sorted list is based on their original positions. Since the original indices are 0,1,2,3,4,5, and the sorted function in Python is stable when keys are equal. So the original order is preserved. So i=0 comes first, then 1, then 2.

Then comes i=3,4,5, whose keys are (-1, 1). So their order is determined by their original positions again.

So the sorted list is [0,1,2,3,4,5].

Then during the iteration:

Yaroslav picks 0,2,4.

Andrey picks 1,3,5.

But wait, the indexes in the sorted list are 0,1,2,3,4,5. So:

index 0: Yaroslav → position0 (s is1 → y=1).

index1: Andrey → position1 (t is0 → a=0.

index2: Yaroslav → position2 (s is1 → y=2.

index3: Andrey → position3 (t is1 → a=1.

index4: Yaroslav → position4 (s is0 → y remains 2.

index5: Andrey → position5 (t is1 → a=2.

So Yaroslav has 2, Andrey has 2 → draw. Which matches the sample.

So the approach works.

Now, the code.

But how to handle the conversion from the strings s and t to integers? Since for each character in the strings, we need to check if it's '0' or '1', but in Python, converting to int is straightforward.

Now, the code steps:

Read n.

Read s and t.

sorted_positions = sorted(range(2*n), key=lambda i: ( -(int(s[i]) + int(t[i])), -(int(s[i]) - int(t[i])) ) )

Then compute y_count and a_count.

But for n=1e6, 2n=2e6 elements. Sorting 2e6 elements in Python can be done quickly enough. Let's think: the time complexity of sorting is O(n log n). For 2e6 elements, log2(2e6) is around 21. So 2e6 * 21 = 42e6 operations. Python can handle that in around a second.

Then, the iteration over sorted_positions is O(n).

So the code should be efficient enough.

Now, let's code this.

But let's also consider possible optimizations. For example, precompute the sum and the difference for each i, but I don't think that's necessary. The lambda function is straightforward.

Another optimization is to precompute the integers for the entire string. For example, convert s and t into lists of integers once, instead of converting each character every time. But for large n, this can save time.

So for example:

s = list(map(int, s))

t = list(map(int, t))

Then, in the lambda, use s[i] and t[i].

But converting the string into a list of integers is O(n) time and memory. For 2e6 elements, this is manageable.

Yes. So let's modify the code to:

n = int(input())

s = input().strip()

t = input().strip()

s_int = list(map(int, s))

t_int = list(map(int, t))

sorted_positions = sorted( range(2*n), key=lambda i: ( -(s_int[i] + t_int[i]), -(s_int[i] - t_int[i]) ) )

y = 0

a = 0

for idx, pos in enumerate(sorted_positions):

    if idx %2 ==0:

        y += s_int[pos]

    else:

        a += t_int[pos]

if y >a:

    print("First")

elif a >y:

    print("Second")

else:

    print("Draw")

This code should work.

But for very large n, converting the entire s and t into lists of integers can take some memory. For 2e6 elements, each list would take 2e6 * 4 bytes (assuming int is 4 bytes), which is about 8MB per list, which is acceptable.

This code should handle all cases efficiently.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()
    t = input_stream.readline().rstrip("\n").strip()

    s_int = list(map(int, s))
    t_int = list(map(int, t))

    sorted_positions = sorted(range(2 * n), key=lambda i: (-(s_int[i] + t_int[i]), -(s_int[i] - t_int[i])))

    y_count = 0
    a_count = 0

    for idx, pos in enumerate(sorted_positions):
        if idx % 2 == 0:
            y_count += s_int[pos]
        else:
            a_count += t_int[pos]

    if y_count > a_count:
        print("First", file=output_stream)
    elif a_count > y_count:
        print("Second", file=output_stream)
    else:
        print("Draw", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
110110
001001
""",
            "output": \
"""\
First
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

Testing against sample input 4.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()
    t = input_stream.readline().rstrip("\n").strip()

    s_int = list(map(int, s))
    t_int = list(map(int, t))

    sorted_positions = sorted(range(2 * n), key=lambda i: (-(s_int[i] + t_int[i]), -(s_int[i] - t_int[i])))

    y_count = 0
    a_count = 0

    for idx, pos in enumerate(sorted_positions):
        if idx % 2 == 0:
            y_count += s_int[pos]
        else:
            a_count += t_int[pos]

    if y_count > a_count:
        print("First", file=output_stream)
    elif a_count > y_count:
        print("Second", file=output_stream)
    else:
        print("Draw", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
01100000
10010011
""",
            "output": \
"""\
Second
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

</think>

```python
n = int(input())
s = input().strip()
t = input().strip()

s_int = list(map(int, s))
t_int = list(map(int, t))

sorted_positions = sorted(range(2 * n), key=lambda i: (-(s_int[i] + t_int[i]), -(s_int[i] - t_int[i])))

y_count = 0
a_count = 0

for idx, pos in enumerate(sorted_positions):
    if idx % 2 == 0:
        y_count += s_int[pos]
    else:
        a_count += t_int[pos]

if y_count > a_count:
    print("First")
elif a_count > y_count:
    print("Second")
else:
    print("Draw")
```
