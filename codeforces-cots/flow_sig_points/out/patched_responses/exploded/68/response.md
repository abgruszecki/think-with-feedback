<think>
Okay, I need to solve this problem where I have to determine the round in which two specific teams, a and b, can meet in a football tournament. The structure of the tournament is such that each round pairs up teams in order, and the winners proceed. The goal is to find out if they meet in the Final (the last round) or an earlier round.

First, let me understand the problem. The rounds work like this: in each round, the remaining teams are sorted by their IDs. Then, the first plays the second, third vs fourth, etc. Each round's matches are determined by this pairing. The winners move on. So, for two teams to meet, they have to be in the same pair in some round. But when does that happen?

Let's think about the example given. For instance, the first sample input is 4 teams, a=1, b=2. In the first round, they are paired as (1,2) and (3,4). So they meet in round 1. Hence output is 1.

In the second example, n=8, a=2 and b=6. The rounds would be:

Round 1: 8 teams. The pairs are (1-2), (3-4), (5-6), (7-8). So team 2 is in pair 1, team 6 is in pair 3. They can't meet here. The winners of these pairs proceed to round 2. Assuming both 2 and 6 win, round 2 would have 4 teams. Let's see the order. The winners are ordered by their original IDs, I think. Wait, but after each round, how are the teams arranged for the next round? The problem statement says "the remaining teams are sorted in the order of their ids". So in each round, the teams are sorted by their IDs, then paired.

So after round 1, the winners are 1 or 2, 3 or4, 5 or6, 7 or8. Suppose 2 wins, then in round 2, the teams would be 2, 3's winner (say 3), 5's winner (say 5), 7's winner (say7). Then pairs would be (2,3), (5,7). If team 2 and 6 both win their first rounds, then in round 2, 2 is in group 1, but 6's winner (5 or6) is part of the next pair. Wait, but in the first round, team 6 is paired with 5. So if 6 wins, then in round 2, the team is 6, but sorted with others. The remaining teams in round 2 are the winners of the first round, which would be 2, 3, 6, 7 (assuming 2,3,6,7 won their matches). Then they are sorted again. So sorted in order 2,3,6,7. Then pairs are (2,3), (6,7). So team 2 and 6 are not in the same pair here. Then round 3 (the final) would have the winners of those pairs, say 2 and 6. Then they meet in round 3, which is the final. So the output is "Final!".

So the key is to find the earliest round where a and b are in the same bracket. How to model this?

Hmm. Let's model the rounds. Each round, the teams are sorted, and then paired. Two teams can meet in a round only if, after sorting, they are consecutive (like 1 and 2 in round 1, etc.) and their positions are such that they are in the same pair.

But how to find out the round when a and b would meet. Let's think in terms of their positions in the sorted list at each round.

Wait, maybe there's a pattern here. Let's consider the initial positions. Let's sort a and b so that a < b. Then, in each round, the teams are arranged in order. The question is: in which round do a and b end up adjacent, with a even? Wait, no. Let me think. Each round, the teams are paired as (1,2), (3,4), etc. So for two teams to meet in a certain round, their positions in the sorted list must be consecutive and a must be even. Wait, no. Let's say in the current round's sorted list, the positions are 1-based. So if two teams are in positions i and i+1, where i is odd, then they are paired. So for example, positions 1 and 2 (i=1, which is odd) are paired. Positions 3 and 4 (i=3, odd) are paired. So for two teams to meet in a round, they must be consecutive in the sorted list, with the first being in an odd position.

So how do a and b end up in consecutive positions in some round?

Alternatively, perhaps there's a mathematical way to compute the earliest round where (a-1) and (b-1) (0-based) are in the same group of size 2^round, and are in the same pair within that group.

Wait, perhaps the idea is to find the minimal k where the (a-1) and (b-1) (0-based) are in the same group of size 2^k, but in different groups of size 2^{k-1}.

Wait, let's think in terms of binary representations. For example, when n=8, each round halves the number of teams. So the first round has 8 teams, then 4, then 2. Each round, the teams are grouped into pairs, and the next round's participants are the winners.

For two teams to meet in the first possible round, the earliest round where they are adjacent in the sorted list and in the same pair.

Another approach: Let's compute for each round, the "group" in which the two teams would be. For a given round r, the size of the group is 2^r. Because in each round, the number of teams halves. Wait, no. Wait, initial round is round 1 with n teams. Then each subsequent round halves the number. So the total number of rounds is log2(n), since n must be a power of two? Wait, the problem says that the initial number of teams is such that each round has even numbers. So n must be a power of two. Because in each round, the number is divided by 2. So n must be 2^k for some k.

So for example, n=4 (2^2) has rounds 1, 2. Round 2 is the final. So in the second sample, n=8 (2^3), so rounds 1, 2, 3. Round 3 is the final.

So, for a and b to meet in round r, they must be in the same pair in that round. The process for each round is as follows: in round r, the group size is 2^{current_round}, perhaps. Wait, perhaps for the first round, the group size is 2 (each pair). So in each round, the group (the set of teams that would meet in the same subtree of the tournament bracket) is determined by higher bits of the team's ID.

Alternatively, perhaps the key is to find the number of times we can divide (a-1) and (b-1) by 2 before they become equal. Let me think.

Let me sort a and b so that a < b. Then, in each round, the teams are paired with their immediate neighbor if they are in an odd position. Wait, perhaps the idea is that each round, the teams are in a sorted list, and then paired. The next round's teams are the winners of each pair, sorted again. But to model when a and b could meet, perhaps we can model the rounds by considering the difference between their positions in the sorted list.

Alternatively, another approach is to compute the earliest round where the two teams are in the same pair. Let's see:

In each round, the teams are ordered by ID, then grouped into pairs. So for two teams a and b (a < b), they can only meet in the earliest round where (b - a) == 1 and a is odd. But that's only for the first round. If that's the case, then they meet in round 1. Otherwise, maybe they can meet in a later round.

Wait, no. For example, in the third sample: 8 teams, a=7, b=5. Sorted, they are 5 and 7. So in the first round, the pairs are (1,2), (3,4), (5,6), (7,8). So 5 and 6 are paired. So 5 and 7 can't meet in round 1. Then, assuming they both win, in round 2, the teams are 5 and 7, along with others. The teams in round 2 are sorted: 5, 6's winner (if 6 won), 7, etc. Wait, but after round 1, the winners are 5 (if 5 beats 6) and 7 (beats 8). So in round 2, the teams are 5 and 7. But in the sorted order, they would be 5,7, along with the other two winners from the other pairs. Wait, let's think of all the possible winners. Let's say the first round's winners are 2,3,5,7. Then in round 2, they are sorted as 2,3,5,7. Paired as (2,3), (5,7). So in round 2, 5 and 7 are paired. So they meet in round 2. Hence output is 2.

So the key is that in the first round, they are not in the same pair, but after being winners, they end up in the same pair in a subsequent round.

So how do we model this?

An alternative approach is to consider that two teams can meet in round k if and only if, when you divide their IDs by 2^(k-1), they are in the same group (i.e., the same quotient when divided by 2^k), but in different groups when divided by 2^{k-1}.

Wait, let's think of the first example. a=1, b=2. For k=1, 2^(k-1) is 1. So 1/1=1, 2/1=2. Then divided by 2^1 (for k=1?), no. Wait maybe another way: For each round, the teams are divided into groups of size 2^round. For example, in round 1, groups are of size 2. So teams are grouped into pairs (1,2), (3,4), etc. To meet in round 1, a and b must be in the same group. For round 2, the groups are of size 4 (since in round 2, the remaining teams are half of previous round). Wait, perhaps not. Let's see. After round 1, the remaining teams are n/2. So in round 2, the groups are of size 2 again, but the teams are arranged based on their original IDs. Wait, but the problem states that in each round, the remaining teams are sorted in the order of their IDs. So the sorting happens each round.

So perhaps the correct way to model this is that in each round, the teams are sorted, then grouped into consecutive pairs. To find when a and b are consecutive in this sorted list and in the same pair.

But how do we model the progression through rounds? For example, team a and team b can meet in round r only if in that round's sorted list, they are next to each other, and in a pair (so their positions are (i, i+1) where i is odd). But how does this depend on the previous rounds?

Alternatively, perhaps the problem can be approached by considering that two teams a and b will meet in the earliest round where the difference between their positions in the sorted list is 1 and the lower one is in an odd position. But this approach may not account for the fact that their positions in each round depend on their original positions and the previous winners.

Wait, but maybe we can model the rounds as if the teams continue to be in the same "bracket" regardless of which teams win. Because the problem says to determine if they can meet in a certain round. So it's possible if there's a path where both teams win all previous rounds until they meet.

So the question is: find the earliest round where a and b are in the same pair in that round's pairing, assuming that both teams a and b have won all previous rounds. So their positions in each round are determined by their original IDs, and not affected by other teams. Because even if other teams are present, as long as a and b keep winning, they will proceed to the next rounds, and their positions are determined by their original IDs.

Wait, but in each round, the remaining teams are sorted by their IDs. So even if a team has a lower ID, as long as it wins, it's in the next round. So for example, team 5 (ID=5) and team 7 (ID=7) in the third example, after the first round, they are both winners, so in the next round, they are part of the sorted list. So in round 2, the sorted list is [5,7] (assuming no other teams are left). Then they are paired. So the earliest round they can meet is 2.

So the approach is to compute the earliest round where a and b are in the same pair, considering that in each round, the teams are sorted by their original IDs.

Wait, but the teams are sorted each round. So in each round, the teams are sorted based on their original IDs, not their previous positions. For example, after round 1, the winners are sorted by their original IDs again. So the pairing for the next round is based on that sorted list.

Therefore, the path of a and b through the rounds is determined by their original IDs. So regardless of which other teams are present, as long as a and b keep winning, they will be part of the next rounds. Their positions in each round's sorted list are determined by their original IDs, because in each round, the remaining teams are sorted.

So, for a and b to meet in a round r, they must be adjacent in the sorted list of that round, and their positions must form a pair (i and i+1 where i is odd). So the problem reduces to finding the earliest round where a and b (when sorted) are consecutive and the lower one is in an odd position in the sorted list of that round.

But how to model the sorted list of each round. For example, in round 1, the sorted list is all teams. In round 2, the sorted list is the remaining teams (those that won in round 1), sorted by their original IDs. And so on.

But since we are considering that a and b are winners in all previous rounds, their presence in each round is guaranteed until they meet. So in each round, the sorted list includes a and b (assuming they haven't met yet) and other teams. However, for the purpose of finding the earliest possible meeting round, we can ignore the other teams. Because the other teams' presence doesn't affect the positions of a and b in the sorted list. The sorted list is sorted by original IDs. So a and b's positions in each round's sorted list are determined by their original IDs, not by the path they took to get there.

Wait, for example, suppose a is 5 and b is 7. In the first round, the sorted list includes 5 and 7, along with others. But in round 2, assuming they both win, their positions are still 5 and 7, sorted in the list. So regardless of which other teams are present, as long as a and b are in the list, their positions are determined by their original IDs.

Therefore, the problem can be modeled as follows: in each round, the list of remaining teams includes a and b. The list is sorted by IDs. So a and b's positions in the list are their original order. So to find when they become adjacent and in the same pair.

Wait, but that's not correct. Because in the first round, all teams are present. In the next round, the remaining teams are the winners. So the sorted list of the next round is the winners sorted by original IDs. So a and b's positions are determined by their original IDs. So if a and b are in the next round, their positions are such that they are sorted with other remaining teams. For example, if a=5 and b=7, and other teams are 3 and 4. Then in the next round, the sorted list is 3,4,5,7. So a and b are in positions 3 and 4. So paired as (3,4) and (5,7). So they are in the same pair in this round.

Wait, but in this scenario, a and b (5 and7) are in positions 3 and 4 (0-based or 1-based? Probably 1-based here). If positions are 1-based, then 5 is in position 3, 7 in position 4. So their positions are consecutive, and since 3 is odd, they form a pair. So they meet in this round.

So the key is that in the earliest possible round where, after sorting the remaining teams (by original IDs), a and b are consecutive, and the lower one's position in the list is odd.

So the steps to solve the problem are:

1. Sort a and b so that a < b.

2. For each possible round (starting from 1), check if in that round, the positions of a and b in the sorted list are consecutive, and the lower position is odd.

But how do we model the sorted list for each round, considering that in each round, the number of teams is halved, and the teams are the winners of previous rounds. However, since we are considering the earliest possible meeting, we can assume that a and b have survived all previous rounds, so they are present in each round until they meet.

Thus, the problem reduces to finding the earliest round where the sorted list (of all remaining teams) includes a and b, and their positions in the list are such that a is at position i, b is at i+1, and i is odd.

But how to model the positions of a and b in each round's list?

Alternatively, think about the bracket structure. Each round, the pairs are formed by consecutive teams in the sorted list. So for a and b to meet in round r, they must be consecutive in the sorted list of the remaining teams in that round, and in that round's list, their indices must form a pair (i, i+1 where i is odd).

But the remaining teams in each round are the teams that have won all previous rounds. So a and b are in each round until they meet, and the other teams are irrelevant as long as they are not between a and b.

Wait, but how do other teams affect the positions of a and b? For example, in the third sample, after round 1, the teams are 5 and 7. But there are other teams in the second round as well, like the winners of other pairs. But their presence could affect the positions of a and b in the sorted list.

Wait, but the sorted list is based on original IDs. So regardless of which other teams are present, as long as a and b are in the list, their positions are determined by their original IDs. So other teams are either less than a, between a and b, or greater than b. But for a and b to be consecutive in a round's sorted list, there must be no team with ID between a and b that survives to that round.

But how to model that?

Alternatively, the earliest possible round where a and b can meet is when the group size (which is 2^r) is such that a and b are in the same group but different sub-groups (of size 2^{r-1}).

This is similar to a binary tournament bracket. For example, in a tournament with 8 teams:

Round 1: groups of 2. So teams 1-2, 3-4, 5-6, 7-8.

Round 2: groups of 4. So winners of 1-2 and 3-4 form one group (1-4), winners of 5-6 and 7-8 form another (5-8). So in round 2, the pairs are between teams from the same 4-group.

Round 3: groups of 8. The final.

So for two teams to meet in round r, they must be in the same group of size 2^r, but in different groups of size 2^{r-1}.

So for example, a=5 and b=7. They are in the same group of size 4 (5-8) in round 2, but in different groups of size 2 (5-6 and 7-8) in round 1. So they meet in round 2.

Similarly, a=2 and b=6 (second sample) are in different groups of size 4 (2 is in 1-4, 6 in 5-8), but in the same group of size 8. So they can only meet in the final.

So the general approach is to find the smallest r such that the teams are in the same group of size 2^r, but different groups of size 2^{r-1}.

Wait, perhaps this is the key. For each round r, the group size is 2^r. So for round 1, group size is 2, round 2 is 4, etc. The number of rounds is log2(n), since n is a power of two.

So the idea is to compute the earliest round r where (a-1) // (2^{r-1}) != (b-1) // (2^{r-1}), but (a-1) // (2^r) == (b-1) // (2^r).

But since a and b are sorted, a < b.

So let's take a and b, sort them so that a < b.

Compute the difference between them: d = b - a.

We can then compute how many times we can divide d by 2 until it becomes 0. But perhaps not.

Alternatively, let's compute the number of times we can subtract 1 and then divide by 2 to get the same quotient.

Wait, perhaps the correct formula is to compute the round r where (a-1) and (b-1) are in the same group of size 2^r, but different groups in size 2^{r-1}.

For example, take a=5 and b=7 (both 0-based as 4 and 6).

Group size for r=2 is 4. So (4) // 4 = 1 (since 4 is 4//4=1). (6//4=1). So same group. For r-1=1, group size is 2: 4//2=2, 6//2=3. Different groups. So they meet in round 2.

Another example: a=2 and b=6 (1-based). 0-based, 1 and 5.

Group size for r=3 (final round) is 8. (1//8=0, 5//8=0. Same group. For r-1=2, group size 4. 1//4=0,5//4=1. Different groups. So they meet in round 3.

So the formula for r is the smallest r where (a-1) // (2^{r-1}) is not equal to (b-1) // (2^{r-1}), but (a-1) // (2^r) is equal to (b-1) // (2^r).

But how to compute this.

Another way: the number of rounds is the number of times you can split the group into halves, and see when a and b are in different halves. The earliest round where they are in different halves would be the round where they meet.

Wait, no. For example, in the first sample: a=1, b=2. The group size is 2. So in round 1, they are in different halves of the group (each group is 2). So they meet in round 1.

Another example: a=5 and b=7. The group size for round 2 is 4. So their group is 5-8. Divided into two halves: 5-6 and 7-8. So in round 1, they are in different groups. So in round 2, they are in the same group but different sub-groups (from round 1). So they meet in round 2.

So the correct approach is to compute the number of times you can split the group into halves (each time doubling the group size) until a and b are in the same group but different sub-groups. The round number is then determined by how many splits were needed.

Alternatively, the round r is the number of times you can shift right the XOR of (a-1) and (b-1) until it becomes a power of two. Wait, perhaps. Because the XOR of (a-1) and (b-1) gives the binary representation of the differing bits. The number of trailing zeros plus one could give the round.

Wait, let's take the third example: a=5 (4 in 0-based), b=7 (6 in 0-based). XOR of 4 and 6 is 2 (binary 10). The number of trailing zeros is 1 (since 10 is 2, which has binary 10). So log2(2) is 1. So round is 1+1=2? Wait, that gives the correct answer. For the second example: a=2 (1), b=6 (5). XOR is 4 (100), which is 3 trailing zeros. log2(4) is 2. 3+1=4? But the answer is round 3. So that doesn't fit.

Hmm, perhaps another approach. Let's compute the XOR of a-1 and b-1, and find the highest bit where they differ. The position of that bit plus 1 gives the round.

Wait, for a=1 (0), b=2 (1). XOR is 1 (binary 1). The highest bit is 0-th position. So round is 0+1=1. Correct.

For a=5 (4) and b=7 (6): XOR is 2 (10). Highest bit is position 1. So round 1+1=2. Correct.

For a=2 (1) and b=6 (5): XOR is 4 (100). Highest bit is position 2. Round 2+1=3. Correct.

So the formula seems to be:

Compute x = (a-1) ^ (b-1). Find the position of the highest set bit in x. Then, the round is (highest_bit_pos + 1). But wait, how to compute the highest bit position.

Wait, x is the XOR of (a-1) and (b-1). The highest set bit in x represents the first place where a-1 and b-1 differ. The number of bits required to represent x is the position of the highest set bit plus one. For example, x=4 (100) is 3 bits, highest bit position is 2.

So the round is the highest bit position plus 1.

So for example:

x=1 → highest bit is 0 → round 1.

x=2 → highest bit is 1 → round 2.

x=4 → highest bit is 2 → round 3.

This seems correct.

So the steps are:

1. Sort a and b so that a < b.

2. Compute x = (a-1) XOR (b-1).

3. Find the position of the highest set bit in x. Let that be 'h'.

4. The round is h + 1.

5. Check if this round is the final round (log2(n) == h+1). If yes, output "Final!", else output the round number.

But how to compute log2(n) to determine if it's the final round.

Wait, for example, when n=8, log2(8)=3. So the rounds are 1,2,3. Round 3 is the final.

So if h+1 == log2(n), then output "Final!".

Else, output h+1.

So the algorithm is:

Compute the round as the position of the highest set bit in x, plus 1.

Then check if this round is equal to the total number of rounds. The total number of rounds is log2(n).

So for example, in the second sample, n=8. log2(8)=3. The computed round is 3. So output "Final!".

In the third sample, n=8. computed round is 2. 2 <3, so output 2.

So how to compute the highest set bit in x.

In Python, we can use the bit_length() method. The highest set bit position for x is (x.bit_length() -1). For example, x=4 (100) has bit_length 3. 3-1=2. So h=2. Round is 3.

So the code steps:

Sort a and b.

x = (a-1) ^ (b-1)

h = x.bit_length() -1

round = h +1

total_rounds = log2(n). But since n is a power of two, total_rounds is log2(n).

But how to compute log2(n) in Python. Since n is a power of two, we can use n.bit_length() -1. For example, n=8 is 1000 in binary. bit_length is 4, so 4-1=3.

So total_rounds = (n).bit_length() -1.

So, in code:

a, b = sorted([a, b])

x = (a-1) ^ (b-1)

h = x.bit_length() -1

round_number = h +1

total_rounds = n.bit_length() -1  # since n is a power of two.

if round_number == total_rounds:

    print("Final!")

else:

    print(round_number)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, a, b = map(int, input_stream.readline().rstrip("\n").split())
    a, b = sorted([a, b])
    x = (a - 1) ^ (b - 1)
    h = x.bit_length() - 1
    round_number = h + 1
    total_rounds = n.bit_length() - 1  # since n is a power of two
    print("Final!" if round_number == total_rounds else round_number, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8 2 6
""",
            "output": \
"""\
Final!
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, a, b = map(int, input_stream.readline().rstrip("\n").split())
    a, b = sorted([a, b])
    x = (a - 1) ^ (b - 1)
    h = x.bit_length() - 1
    round_number = h + 1
    total_rounds = n.bit_length() - 1  # since n is a power of two
    print("Final!" if round_number == total_rounds else round_number, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8 7 5
""",
            "output": \
"""\
2
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

Third example:

n=8. total_rounds=3.

a=5, b=7. sorted a=5, b=7.

x =4 XOR6 →4^6=2. 2 is 10 in binary. h=1. round=2. 2 <3 → output 2. Correct.

Another test case: 8 teams, a=7 and b=5 (sorted to 5 and7). same as third example. Correct.

Another test case: 256 teams. a=1, b=256. Then x is (0) ^ (255) →255. 255 is 11111111 in binary. h=7. round=8. total_rounds is 8 (since 256 is 2^8). So output "Final!".

Another example: n=16, a=3, b=5. sorted a=3, b=5.

x=2 XOR4=6 (110). highest bit is 2 (since 6 is 110, bit_length is 3, h=2). round=3. total_rounds for 16 is 4. So output 3.

Yes, in round 3, teams 3 and5 (if they survive) would meet.

So the code seems to work.

Thus, the Python code can be written as follows:

Read n, a, b.

Sort a and b.

Compute x = (a-1) ^ (b-1).

Compute h = x.bit_length() -1.

round_number = h +1.

Compute total_rounds = (n).bit_length() -1.

If round_number == total_rounds: print "Final!".

Else, print round_number.

But wait, in Python, n may not be a power of two. But the problem says that the input is such that each round has even number of teams. So n is a power of two. So this code works.

Thus, the code is straightforward.
</think>

```python
n, a, b = map(int, input().split())
a, b = sorted([a, b])
x = (a - 1) ^ (b - 1)
h = x.bit_length() - 1
round_number = h + 1
total_rounds = n.bit_length() - 1  # since n is a power of two
print("Final!" if round_number == total_rounds else round_number)
```
